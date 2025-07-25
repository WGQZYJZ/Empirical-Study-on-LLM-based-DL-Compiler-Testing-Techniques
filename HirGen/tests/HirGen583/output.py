import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_29 = relay.var("var_29", dtype = "uint8", shape = (6, 9, 16))#candidate|29|(6, 9, 16)|var|uint8
var_30 = relay.var("var_30", dtype = "uint8", shape = (6, 9, 16))#candidate|30|(6, 9, 16)|var|uint8
bop_31 = relay.greater(var_29.astype('bool'), relay.reshape(var_30.astype('bool'), relay.shape_of(var_29))) # shape=(6, 9, 16)
uop_52 = relay.tan(bop_31.astype('float32')) # shape=(6, 9, 16)
output = relay.Tuple([uop_52,])
output2 = relay.Tuple([uop_52,])
func_60 = relay.Function([var_29,var_30,], output)
mod['func_60'] = func_60
mod = relay.transform.InferType()(mod)
mutated_mod['func_60'] = func_60
mutated_mod = relay.transform.InferType()(mutated_mod)
func_60_call = mutated_mod.get_global_var('func_60')
var_62 = relay.var("var_62", dtype = "uint8", shape = (6, 9, 16))#candidate|62|(6, 9, 16)|var|uint8
var_63 = relay.var("var_63", dtype = "uint8", shape = (6, 9, 16))#candidate|63|(6, 9, 16)|var|uint8
call_61 = func_60_call(var_62,var_63,)
output = call_61
func_64 = relay.Function([var_62,var_63,], output)
mutated_mod['func_64'] = func_64
mutated_mod = relay.transform.InferType()(mutated_mod)
var_86 = relay.var("var_86", dtype = "int16", shape = (16, 13, 6))#candidate|86|(16, 13, 6)|var|int16
var_87 = relay.var("var_87", dtype = "int16", shape = (16, 13, 6))#candidate|87|(16, 13, 6)|var|int16
bop_88 = relay.add(var_86.astype('int16'), relay.reshape(var_87.astype('int16'), relay.shape_of(var_86))) # shape=(16, 13, 6)
bop_102 = relay.bitwise_and(var_86.astype('uint8'), relay.reshape(var_87.astype('uint8'), relay.shape_of(var_86))) # shape=(16, 13, 6)
output = relay.Tuple([bop_88,bop_102,])
output2 = relay.Tuple([bop_88,bop_102,])
func_112 = relay.Function([var_86,var_87,], output)
mod['func_112'] = func_112
mod = relay.transform.InferType()(mod)
var_113 = relay.var("var_113", dtype = "int16", shape = (16, 13, 6))#candidate|113|(16, 13, 6)|var|int16
var_114 = relay.var("var_114", dtype = "int16", shape = (16, 13, 6))#candidate|114|(16, 13, 6)|var|int16
output = func_112(var_113,var_114,)
func_115 = relay.Function([var_113,var_114,], output)
mutated_mod['func_115'] = func_115
mutated_mod = relay.transform.InferType()(mutated_mod)
var_120 = relay.var("var_120", dtype = "bool", shape = (9, 8, 12))#candidate|120|(9, 8, 12)|var|bool
var_121 = relay.var("var_121", dtype = "bool", shape = (9, 8, 12))#candidate|121|(9, 8, 12)|var|bool
bop_122 = relay.logical_or(var_120.astype('bool'), relay.reshape(var_121.astype('bool'), relay.shape_of(var_120))) # shape=(9, 8, 12)
func_60_call = mod.get_global_var('func_60')
func_64_call = mutated_mod.get_global_var('func_64')
call_130 = relay.TupleGetItem(func_60_call(relay.reshape(var_121.astype('uint8'), [6, 9, 16]), relay.reshape(var_121.astype('uint8'), [6, 9, 16]), ), 0)
call_131 = relay.TupleGetItem(func_64_call(relay.reshape(var_121.astype('uint8'), [6, 9, 16]), relay.reshape(var_121.astype('uint8'), [6, 9, 16]), ), 0)
func_112_call = mod.get_global_var('func_112')
func_115_call = mutated_mod.get_global_var('func_115')
var_137 = relay.var("var_137", dtype = "int16", shape = (1248, 1))#candidate|137|(1248, 1)|var|int16
call_136 = relay.TupleGetItem(func_112_call(relay.reshape(var_137.astype('int16'), [16, 13, 6]), relay.reshape(var_137.astype('int16'), [16, 13, 6]), ), 0)
call_138 = relay.TupleGetItem(func_115_call(relay.reshape(var_137.astype('int16'), [16, 13, 6]), relay.reshape(var_137.astype('int16'), [16, 13, 6]), ), 0)
func_60_call = mod.get_global_var('func_60')
func_64_call = mutated_mod.get_global_var('func_64')
call_139 = relay.TupleGetItem(func_60_call(relay.reshape(var_121.astype('uint8'), [6, 9, 16]), relay.reshape(var_120.astype('uint8'), [6, 9, 16]), ), 0)
call_140 = relay.TupleGetItem(func_64_call(relay.reshape(var_121.astype('uint8'), [6, 9, 16]), relay.reshape(var_120.astype('uint8'), [6, 9, 16]), ), 0)
uop_143 = relay.acos(var_121.astype('float32')) # shape=(9, 8, 12)
output = relay.Tuple([bop_122,call_130,call_136,var_137,call_139,uop_143,])
output2 = relay.Tuple([bop_122,call_131,call_138,var_137,call_140,uop_143,])
func_158 = relay.Function([var_120,var_121,var_137,], output)
mod['func_158'] = func_158
mod = relay.transform.InferType()(mod)
mutated_mod['func_158'] = func_158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_158_call = mutated_mod.get_global_var('func_158')
var_160 = relay.var("var_160", dtype = "bool", shape = (9, 8, 12))#candidate|160|(9, 8, 12)|var|bool
var_161 = relay.var("var_161", dtype = "bool", shape = (9, 8, 12))#candidate|161|(9, 8, 12)|var|bool
var_162 = relay.var("var_162", dtype = "int16", shape = (1248, 1))#candidate|162|(1248, 1)|var|int16
call_159 = func_158_call(var_160,var_161,var_162,)
output = call_159
func_163 = relay.Function([var_160,var_161,var_162,], output)
mutated_mod['func_163'] = func_163
mutated_mod = relay.transform.InferType()(mutated_mod)
var_701 = relay.var("var_701", dtype = "int16", shape = (8, 2, 2))#candidate|701|(8, 2, 2)|var|int16
var_702 = relay.var("var_702", dtype = "int16", shape = (8, 2, 2))#candidate|702|(8, 2, 2)|var|int16
bop_703 = relay.logical_xor(var_701.astype('int16'), relay.reshape(var_702.astype('int16'), relay.shape_of(var_701))) # shape=(8, 2, 2)
output = relay.Tuple([bop_703,])
output2 = relay.Tuple([bop_703,])
func_723 = relay.Function([var_701,var_702,], output)
mod['func_723'] = func_723
mod = relay.transform.InferType()(mod)
mutated_mod['func_723'] = func_723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_723_call = mutated_mod.get_global_var('func_723')
var_725 = relay.var("var_725", dtype = "int16", shape = (8, 2, 2))#candidate|725|(8, 2, 2)|var|int16
var_726 = relay.var("var_726", dtype = "int16", shape = (8, 2, 2))#candidate|726|(8, 2, 2)|var|int16
call_724 = func_723_call(var_725,var_726,)
output = call_724
func_727 = relay.Function([var_725,var_726,], output)
mutated_mod['func_727'] = func_727
mutated_mod = relay.transform.InferType()(mutated_mod)
var_785 = relay.var("var_785", dtype = "uint8", shape = (13, 7, 15))#candidate|785|(13, 7, 15)|var|uint8
const_786 = relay.const([[[7,4,1,-6,-3,2,-7,-3,-7,7,-5,9,-3,-9,4],[-6,8,-3,-7,-9,-1,8,-5,-9,2,-6,-6,4,2,6],[9,-7,3,-7,10,-3,-7,8,-9,-6,-2,-9,9,-8,9],[7,7,5,3,-10,-8,-5,-1,-10,-2,3,-1,2,6,-1],[3,2,-1,10,1,-8,-3,5,-9,-6,1,3,-2,2,-7],[2,10,-2,3,4,1,2,-6,-10,3,-4,-5,-8,5,4],[2,4,10,-2,7,6,5,-4,8,-8,9,-7,10,-1,5]],[[7,-1,-1,8,-3,-7,-4,10,7,-3,-9,6,9,1,-1],[7,-8,-8,9,-2,2,1,6,-6,-9,6,3,4,-8,-4],[-5,-6,9,-2,1,-1,3,-6,5,-2,3,2,9,-10,5],[3,-6,1,-2,-4,-6,5,8,10,5,8,9,-4,10,-5],[-7,-2,-7,8,5,4,6,-3,-1,6,5,4,5,-2,1],[7,6,-10,-4,2,-10,-3,8,-1,-10,-4,10,-7,-7,10],[-6,5,8,-3,-4,6,-5,-10,-6,1,7,-1,5,-4,8]],[[-10,2,-4,-5,-5,-6,-4,-1,-4,-5,-2,-10,3,-10,-10],[2,-1,-9,7,6,2,-4,-4,1,1,-3,-10,4,2,10],[-2,-2,-7,2,5,-5,-9,-1,3,1,8,4,10,-3,4],[2,6,-1,-7,6,-8,-6,9,1,9,-3,-9,9,7,-10],[5,-6,-8,-3,-9,-6,1,5,-1,-1,10,1,3,7,-2],[-10,8,6,-5,2,10,-3,10,-1,6,-3,-8,-6,-4,10],[1,-1,-9,7,-9,-10,-7,-10,-10,-9,-2,5,-5,-10,5]],[[5,3,-6,-4,-8,4,-10,10,-9,10,9,8,-4,4,-4],[-6,-6,6,1,9,-10,5,5,1,-8,-1,5,-8,4,2],[2,10,7,1,3,5,-4,-5,-8,4,9,10,7,-4,-3],[-1,-4,-4,-7,7,7,-3,-4,2,7,5,-1,4,6,-9],[4,-3,-2,-7,2,-9,8,9,-2,-4,-7,7,-8,6,-8],[-1,6,9,9,-7,2,1,7,3,-3,8,-10,9,-5,9],[3,-6,-4,-9,2,5,1,5,-5,7,7,-9,-10,2,5]],[[-1,-3,-9,1,-1,1,7,1,-2,-10,6,2,-2,-6,-10],[-8,-1,-7,10,-6,2,-9,1,-1,-10,-10,10,-2,6,9],[-10,8,-9,-10,6,-2,-5,-7,2,-1,-1,-9,-5,-5,10],[9,-10,1,-6,10,9,8,4,-10,5,9,2,-9,8,10],[-8,7,-9,-9,1,5,-3,2,10,2,-5,3,8,6,6],[3,8,1,-10,10,-10,-9,-10,8,7,7,-2,1,2,5],[7,3,-10,3,-5,-1,-10,7,3,3,-9,4,-1,-3,-4]],[[3,6,9,2,-6,-4,3,-7,-7,-8,-10,9,10,9,-4],[-2,8,-5,-4,6,-4,-6,8,7,-4,4,-4,10,-4,9],[-5,7,9,-8,-8,4,7,-9,3,-8,3,-3,-8,4,3],[2,-4,-9,8,7,-2,-8,-1,3,4,-5,7,5,2,-9],[-3,-2,7,-2,-9,-3,-2,-1,9,-8,-7,-2,-10,2,-8],[-6,-10,-10,10,-4,-2,3,9,8,-9,-10,1,3,-1,-5],[5,-2,10,2,5,-2,-2,-5,-10,-8,1,-7,2,-6,-6]],[[3,-2,6,8,-3,-3,-2,-9,-7,-9,-8,-3,-3,-7,-9],[7,4,-7,-1,-10,8,7,-10,6,-5,-10,-5,10,-1,4],[1,2,-1,8,3,-4,1,10,10,-9,-1,2,6,-2,10],[-5,-9,8,7,2,4,-1,-9,-8,-7,8,8,5,-1,-8],[-5,1,1,4,5,-8,-1,-6,7,3,-1,-5,-2,-10,7],[3,-3,6,6,-4,5,2,8,-8,3,3,4,-4,6,7],[-4,-5,-9,-4,10,-5,-7,-9,-8,2,-10,-7,10,-9,5]],[[-10,-8,-7,6,1,-7,-9,5,1,-6,-5,7,1,3,-4],[7,7,-8,4,8,-10,-2,-1,-8,2,-5,-2,-9,8,6],[10,7,-1,-4,9,-10,8,9,-1,-2,-2,-10,-9,-9,10],[-10,-9,10,2,-4,-7,-3,8,-4,8,2,5,4,2,3],[-9,2,10,9,-7,6,-7,1,-8,4,3,3,9,-3,3],[3,-9,-1,9,2,2,2,-6,7,-9,9,9,3,-3,9],[10,-9,6,-7,-9,3,-8,3,9,7,2,-2,-2,-9,1]],[[1,9,-2,10,-10,-10,-2,-9,10,6,-5,-7,-9,2,-4],[-3,6,-2,7,-8,3,-1,4,-2,5,4,-8,9,-10,3],[-5,8,8,-8,4,-3,1,3,-3,2,5,-10,-8,8,9],[3,-10,3,-3,-7,6,3,4,-5,-1,7,-6,8,-3,4],[-10,3,-8,-1,7,7,6,3,5,8,-6,3,9,7,-8],[3,-8,9,3,8,-6,3,4,-5,-5,-7,6,-4,1,-9],[4,6,-8,-9,-5,-1,9,-6,-4,-4,-1,-2,2,4,-7]],[[2,-6,-3,-3,5,9,-2,2,3,-6,4,9,6,2,-7],[-6,-2,7,-7,10,-10,-8,7,-10,-7,-7,-6,7,-10,-6],[9,3,-4,-7,-1,-3,-3,-5,2,-1,4,9,4,3,-6],[10,3,-7,4,-8,-10,-9,-1,-5,10,1,2,3,8,2],[5,9,5,-4,9,-7,-10,-2,-1,-3,3,-4,-6,2,2],[-9,-4,-6,-4,10,-4,-2,3,7,-3,2,6,10,4,-7],[-6,7,7,-8,6,4,-7,4,4,-2,2,2,2,10,-4]],[[4,3,9,-5,-1,-7,10,-5,3,-8,4,-1,-7,-8,10],[-4,-3,6,-9,1,3,-6,3,9,-9,-1,6,1,6,10],[3,-8,3,8,-6,-1,-8,-4,-6,-7,2,2,-1,-3,2],[10,-7,4,4,-1,1,-1,-7,-10,-2,10,4,-3,-4,-1],[-10,-4,9,9,7,6,-10,-9,-4,9,-5,-1,2,-3,2],[3,-4,1,2,-9,-7,-1,3,-3,-8,-6,-5,9,3,-4],[-7,-7,3,-4,-7,5,9,-1,5,-3,10,3,6,-3,-7]],[[4,-3,5,-10,-2,-4,-10,-3,9,-9,-1,2,2,-10,-7],[-3,1,1,-3,-6,5,-2,-3,8,-2,-4,5,9,-4,-4],[7,9,5,-3,10,-3,-9,1,-9,6,7,-6,-6,10,7],[-10,-3,-2,8,7,5,2,-5,8,2,-9,3,-1,-4,10],[7,4,8,6,-3,3,-5,2,10,5,-3,2,10,7,-4],[-5,-7,-9,-7,3,2,-8,3,-6,-1,6,7,-9,1,1],[5,6,-5,8,-2,1,-9,10,8,-6,8,2,9,-2,-1]],[[4,9,9,5,-9,10,-2,9,-4,7,-8,1,-10,-5,-1],[-5,2,4,-1,1,-9,-10,-10,10,-7,-4,-2,9,7,4],[10,-2,-5,-6,-7,-6,7,-5,4,3,-4,8,-3,-10,9],[-8,-3,-3,-7,5,-5,-10,7,-9,5,-2,-8,7,-7,2],[2,7,10,-4,-1,1,-1,6,6,-1,-7,10,-5,-7,-5],[-10,-10,-2,9,5,8,3,5,-9,7,4,3,9,2,-10],[-6,-3,7,5,5,3,-6,-3,8,-3,-10,-6,2,8,-3]]], dtype = "uint8")#candidate|786|(13, 7, 15)|const|uint8
bop_787 = relay.left_shift(var_785.astype('uint8'), relay.reshape(const_786.astype('uint8'), relay.shape_of(var_785))) # shape=(13, 7, 15)
func_158_call = mod.get_global_var('func_158')
func_163_call = mutated_mod.get_global_var('func_163')
const_801 = relay.const([[True,False,True,False,True,False,False,True,False,False,False,False,True,True,True,True,True,True,False,False,True,False,True,True],[True,True,False,False,True,True,False,False,True,True,False,False,False,True,False,False,True,False,False,False,False,True,True,True],[True,True,False,False,True,True,False,True,False,False,True,False,True,True,False,True,True,True,True,True,False,True,True,True],[False,True,True,False,False,False,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,True,False,False],[False,False,True,False,True,False,True,True,True,False,True,True,False,True,True,False,False,True,True,True,True,True,False,True],[False,True,False,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,True,False,False,False,False,True],[True,True,False,False,False,False,True,False,True,True,False,True,False,True,False,True,False,False,False,False,True,False,False,False],[True,True,False,False,True,False,True,False,True,True,False,True,True,True,False,False,False,False,True,True,True,False,False,True],[False,False,False,True,False,False,True,False,True,False,False,False,False,True,False,False,False,False,True,True,True,True,True,True],[True,False,False,True,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,True,True,True,True,True],[True,True,False,False,False,True,False,False,True,False,True,False,True,True,False,True,False,False,True,False,True,True,False,False],[True,True,True,False,True,True,True,False,False,True,True,False,False,True,False,True,True,True,True,True,True,False,False,True],[False,True,True,True,False,True,True,True,True,False,True,False,True,False,False,True,True,True,False,True,False,False,False,False],[False,False,True,True,False,True,False,False,False,True,True,False,True,False,True,False,False,False,False,False,False,False,True,True],[False,True,False,False,False,False,False,False,False,True,True,False,False,True,False,False,False,True,False,True,True,True,True,False],[True,True,False,True,False,True,False,False,True,False,False,True,True,True,True,True,False,False,False,True,True,False,True,True],[False,False,True,True,True,False,True,True,False,True,False,False,True,True,False,False,True,False,True,False,True,False,False,False],[False,False,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,False,False,False],[False,True,False,False,True,False,False,True,False,True,False,True,True,False,True,False,False,True,False,False,True,True,False,False],[False,False,False,True,False,False,True,False,True,True,False,False,False,False,True,False,True,True,True,True,True,True,True,True],[False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,False,False,False,False,False,True,True,False,False],[False,False,True,False,True,False,True,True,True,True,True,True,False,False,False,False,False,True,True,True,False,True,False,False],[False,False,False,True,False,False,True,False,False,True,False,True,True,False,True,True,True,False,False,True,False,False,True,False],[False,True,False,False,False,False,False,False,False,False,True,False,False,True,True,True,False,True,False,True,True,True,False,False],[True,True,False,False,True,True,False,True,False,False,True,True,False,True,True,True,True,True,True,False,False,False,True,False],[False,True,True,True,True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,True,False],[True,False,False,True,True,True,True,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,False,True],[False,True,True,True,True,False,True,True,True,False,False,False,True,False,True,False,True,True,False,False,False,True,False,False],[False,False,False,False,True,False,True,True,True,True,False,True,True,True,False,False,True,False,False,True,False,True,True,True],[True,False,True,True,True,True,True,True,False,False,True,True,False,False,False,False,True,False,True,True,True,True,True,True],[True,False,False,False,True,True,True,False,True,True,True,False,False,True,True,False,True,False,True,True,True,True,True,False],[True,False,True,True,True,True,False,True,True,False,True,False,True,False,True,True,True,False,True,False,True,True,False,False],[True,False,False,False,True,True,True,True,False,False,False,True,True,False,False,False,False,True,True,True,False,False,False,True],[False,False,True,False,True,False,False,False,False,False,True,True,False,False,False,False,False,False,True,False,False,False,False,False],[True,True,False,True,True,False,True,False,False,False,False,True,False,False,False,False,True,True,False,True,True,False,True,True],[True,False,True,True,False,False,False,False,True,False,True,True,False,False,True,True,True,True,False,True,True,False,False,False]], dtype = "bool")#candidate|801|(36, 24)|const|bool
const_802 = relay.const([9,1,-8,-10,-2,-8,-4,6,-10,6,9,6,-8,9,6,-2,7,4,-2,10,5,-1,-8,4,3,-4,9,4,-10,7,-10,-3,-4,2,3,-2,-9,-9,9,5,-5,-4,10,2,-10,8,-9,7,-9,-1,-3,3,3,7,9,-4,2,1,-8,3,-3,10,-3,-7,-7,7,1,-10,-3,-6,2,7,10,7,2,-7,-3,8,5,-8,-4,-2,6,1,2,2,-7,-7,8,6,6,-4,10,2,-7,-8,7,8,-4,3,-6,10,-5,-2,-3,-4,2,7,-9,-7,-1,-9,-7,-2,-6,6,9,5,5,8,6,8,-1,1,-5,-8,7,7,-4,4,-3,2,-10,-7,-6,4,8,-1,-6,10,-3,8,-8,4,1,4,2,-7,4,-7,8,2,1,8,8,-9,-8,10,9,10,2,5,1,-6,5,-7,5,2,3,-5,7,1,-8,-1,-5,-10,-6,-10,-6,-4,-2,-5,-10,-2,6,5,1,9,7,8,-3,-8,3,4,6,4,8,-4,-6,-1,-4,-8,-2,-6,-8,-8,3,10,4,9,3,-8,3,-9,-10,3,-7,-1,-9,8,1,10,2,2,-5,7,-4,-9,9,-6,-8,-3,2,-4,10,10,-7,-5,-10,8,10,3,2,-9,-8,2,-3,-1,-10,8,4,-1,-6,-2,5,-2,-5,7,7,-2,2,-2,-10,2,5,-2,-5,10,1,-10,1,-1,6,-6,3,-9,2,10,2,2,9,8,8,7,-1,-4,-8,-9,-3,9,-10,3,-10,4,4,-1,1,-10,7,-6,4,-9,5,9,10,5,6,2,2,10,-3,2,-10,10,-8,6,-8,-4,-2,2,3,-5,-7,7,-4,-5,7,8,-10,5,-5,-1,5,-6,10,-2,-7,-2,-4,4,-5,3,-8,9,9,5,-4,-9,-4,7,-4,7,-4,6,9,5,10,-7,-9,4,2,-4,-8,5,-9,-7,9,-4,4,-10,1,6,3,10,2,2,5,-10,10,-6,8,-3,7,10,9,-4,-7,-4,4,2,7,-9,1,-7,3,-1,-9,7,-4,-9,9,5,-4,6,-10,5,4,2,-3,8,6,-6,6,3,2,-2,3,-9,-6,-6,-5,6,5,7,-8,-4,6,9,5,3,4,-2,-5,-4,8,-7,-3,2,-10,-5,-6,5,9,6,-6,5,6,-6,10,2,-4,-1,-2,4,-4,4,-6,-1,-3,-2,6,10,7,-3,-10,3,3,-10,8,1,-10,1,-2,-4,-7,-5,-6,-5,10,7,10,-3,-5,10,-6,-5,-5,-4,-9,3,7,-1,2,-3,3,-4,4,-7,-10,-2,1,-3,-6,-5,-7,2,-6,-6,-10,-3,-1,-7,-6,-3,5,-5,7,-3,6,9,-6,-7,4,3,2,-7,4,-7,-8,9,8,-8,-1,-7,8,-10,6,7,1,-4,-7,-6,-4,-3,5,-6,5,5,6,5,-7,8,-4,-3,-6,-8,9,4,-8,8,9,4,9,-4,-1,-8,-5,2,-1,4,6,-10,5,10,3,5,-3,7,-10,6,-9,-2,1,6,10,9,2,-1,-5,10,-9,9,-6,4,9,-9,-6,-5,-4,-9,10,2,-1,-9,-4,-2,6,6,10,-9,-10,7,9,3,2,-10,1,-2,-5,-9,-2,3,-4,3,9,-3,10,4,-2,3,-8,4,-4,-4,-9,-9,5,10,-3,3,5,-2,8,4,-5,-1,7,4,4,-2,2,6,7,7,1,3,-10,10,-3,5,1,-10,-3,-2,4,-4,7,-4,-9,6,4,5,8,-9,2,-10,-2,-1,-5,-6,9,7,-1,2,-3,8,-2,9,-10,1,-4,5,1,3,-1,7,8,-5,5,6,8,3,-1,-9,3,-5,1,1,5,10,-2,5,-2,-8,10,5,2,-9,10,-3,8,-10,-7,-2,6,8,10,-9,-6,9,2,5,2,6,1,-7,-7,-9,9,-7,-7,4,-10,2,-9,-3,5,-5,-3,-10,-10,5,-5,2,-10,-10,5,4,8,-5,-9,10,-8,2,7,6,-9,5,-7,-10,7,2,8,1,-4,-5,-5,-8,1,4,1,5,3,8,10,-5,-7,-1,4,3,10,-4,2,-10,1,-2,6,-6,9,8,-9,-6,-9,3,1,-5,3,-6,9,-9,9,-5,-9,5,5,5,4,2,10,-1,3,-10,3,-3,-1,5,2,-7,2,-8,5,3,-7,-5,4,8,1,-4,-5,9,9,-5,7,-3,6,-8,-7,10,-5,2,10,7,-9,6,-9,-9,-10,-1,-8,5,-6,-3,-3,-8,10,8,-2,-1,-7,5,3,-4,8,-7,-10,8,-7,-10,8,9,-9,-5,-5,4,-5,-7,2,-9,-7,-7,-3,2,8,10,-9,3,9,1,-6,5,-3,-8,-2,-5,7,5,-7,-10,8,-2,-1,6,-10,-4,-1,8,1,-9,6,1,4,-3,-4,7,-3,8,-1,-5,-1,-9,-10,-8,-4,-4,-1,-4,-3,-7,10,-9,-2,-10,-3,-3,-6,9,-1,8,2,-6,9,9,8,10,-9,-2,6,-1,7,-3,8,2,9,-7,-2,-5,4,4,9,10,3,-6,-4,-9,-2,-5,-6,-2,-6,7,3,-10,5,10,8,-9,-4,3,1,10,-6,-6,1,-7,-8,-7,-4,9,-1,-3,-9,-1,7,-10,5,4,4,-4,-1,-1,3,9,5,9,6,-6,-2,7,-10,-10,6,8,7,4,3,6,-5,5,4,5,-6,3,7,-9,-7,-6,4,-1,-8,-8,10,6,10,7,-5,-2,-5,-9,6,-1,-9,-4,-3,-8,1,1,-2,9,8,8,8,6,-6,6,-7,5,-8,-10,5,1,4,7,10,-9,-2,4,6,5,-7,4,-2,9,-9,10,-7,-9,-4,6,-4,2,2,8,-8,-10,4,10,-4,-3,-9,4,-5,-6,1,4,-9,-1,-4,8,10,10,3,-9,8,7,-6,-3,8,-3,-3,2,5,2,-2,3,10,7,3,8,9,-1,10,9,5,-5,-1,2,-4,-7,-7,-10,6,-8,-5,-2,-6,1,-9,4,-4,-4,-7,1,1,10,8,4,-7,-3,-1,-9,2,-2,2,-6,-4,1,9,5,-2,9,-4,4,-7,4,-3,-6,-2,-5,4,-3,6,-4,-8,4,-5,-9,-7,-10,9,-4,-6,-7,-1,-5,8,5,-1,-8,9,8,6,-1,-10,9,7,-2,-6,-3,3,-3,-5,-6,9,-7,5,-2,-3,-8,-6,-2,2,5,-5,8,6,1,-2,-8,-1,9,10,-1,-6,8,5,6,6,-9,10,10,-7,-7,-8,-9,-10,6,-2,7], dtype = "int16")#candidate|802|(1248,)|const|int16
call_800 = relay.TupleGetItem(func_158_call(relay.reshape(const_801.astype('bool'), [9, 8, 12]), relay.reshape(const_801.astype('bool'), [9, 8, 12]), relay.reshape(const_802.astype('int16'), [1248, 1]), ), 3)
call_803 = relay.TupleGetItem(func_163_call(relay.reshape(const_801.astype('bool'), [9, 8, 12]), relay.reshape(const_801.astype('bool'), [9, 8, 12]), relay.reshape(const_802.astype('int16'), [1248, 1]), ), 3)
func_112_call = mod.get_global_var('func_112')
func_115_call = mutated_mod.get_global_var('func_115')
call_804 = relay.TupleGetItem(func_112_call(relay.reshape(call_800.astype('int16'), [16, 13, 6]), relay.reshape(call_800.astype('int16'), [16, 13, 6]), ), 1)
call_805 = relay.TupleGetItem(func_115_call(relay.reshape(call_800.astype('int16'), [16, 13, 6]), relay.reshape(call_800.astype('int16'), [16, 13, 6]), ), 1)
func_112_call = mod.get_global_var('func_112')
func_115_call = mutated_mod.get_global_var('func_115')
call_807 = relay.TupleGetItem(func_112_call(relay.reshape(call_800.astype('int16'), [16, 13, 6]), relay.reshape(call_804.astype('int16'), [16, 13, 6]), ), 1)
call_808 = relay.TupleGetItem(func_115_call(relay.reshape(call_800.astype('int16'), [16, 13, 6]), relay.reshape(call_804.astype('int16'), [16, 13, 6]), ), 1)
func_158_call = mod.get_global_var('func_158')
func_163_call = mutated_mod.get_global_var('func_163')
call_813 = relay.TupleGetItem(func_158_call(relay.reshape(const_801.astype('bool'), [9, 8, 12]), relay.reshape(const_801.astype('bool'), [9, 8, 12]), relay.reshape(call_800.astype('int16'), [1248, 1]), ), 2)
call_814 = relay.TupleGetItem(func_163_call(relay.reshape(const_801.astype('bool'), [9, 8, 12]), relay.reshape(const_801.astype('bool'), [9, 8, 12]), relay.reshape(call_800.astype('int16'), [1248, 1]), ), 2)
func_158_call = mod.get_global_var('func_158')
func_163_call = mutated_mod.get_global_var('func_163')
call_831 = relay.TupleGetItem(func_158_call(relay.reshape(const_801.astype('bool'), [9, 8, 12]), relay.reshape(const_801.astype('bool'), [9, 8, 12]), relay.reshape(const_802.astype('int16'), [1248, 1]), ), 0)
call_832 = relay.TupleGetItem(func_163_call(relay.reshape(const_801.astype('bool'), [9, 8, 12]), relay.reshape(const_801.astype('bool'), [9, 8, 12]), relay.reshape(const_802.astype('int16'), [1248, 1]), ), 0)
bop_852 = relay.less(call_800.astype('bool'), relay.reshape(call_804.astype('bool'), relay.shape_of(call_800))) # shape=(1248, 1)
bop_855 = relay.less(call_803.astype('bool'), relay.reshape(call_805.astype('bool'), relay.shape_of(call_803))) # shape=(1248, 1)
output = relay.Tuple([bop_787,const_801,const_802,call_807,call_813,call_831,bop_852,])
output2 = relay.Tuple([bop_787,const_801,const_802,call_808,call_814,call_832,bop_855,])
func_858 = relay.Function([var_785,], output)
mod['func_858'] = func_858
mod = relay.transform.InferType()(mod)
mutated_mod['func_858'] = func_858
mutated_mod = relay.transform.InferType()(mutated_mod)
var_859 = relay.var("var_859", dtype = "uint8", shape = (13, 7, 15))#candidate|859|(13, 7, 15)|var|uint8
func_858_call = mutated_mod.get_global_var('func_858')
call_860 = func_858_call(var_859)
output = call_860
func_861 = relay.Function([var_859], output)
mutated_mod['func_861'] = func_861
mutated_mod = relay.transform.InferType()(mutated_mod)
var_923 = relay.var("var_923", dtype = "float32", shape = (4, 13, 4))#candidate|923|(4, 13, 4)|var|float32
uop_924 = relay.log2(var_923.astype('float32')) # shape=(4, 13, 4)
func_858_call = mod.get_global_var('func_858')
func_861_call = mutated_mod.get_global_var('func_861')
const_949 = relay.const([-6,5,-3,-7,-6,1,5,8,-7,9,-4,10,3,8,1,4,10,5,2,-4,-10,-6,8,-3,3,-1,-1,4,7,1,-7,5,-4,-3,-6,-3,-4,1,2,-9,8,-9,-2,-2,-5,7,7,9,6,-6,-1,-9,7,-8,-4,4,-8,-2,8,-7,8,-6,8,8,9,6,-4,-2,-5,-2,7,2,8,6,-1,-8,-9,-5,10,-2,-9,9,-3,4,1,-8,1,6,7,5,6,-6,8,1,7,8,-2,-7,8,-5,-9,-9,-7,10,-10,-2,10,9,-1,7,4,4,-10,2,-4,9,4,-4,5,-4,10,-1,-4,-8,1,-3,-1,-2,7,9,3,-7,-5,7,-4,7,5,-2,-10,-5,6,-7,-2,7,3,3,5,-10,-8,2,-7,5,9,-2,10,10,-3,2,-6,-7,7,4,7,-2,-2,-8,-7,3,-4,7,-2,1,-5,-5,4,-1,-1,2,-10,2,9,3,4,-2,-10,-4,5,10,-10,1,6,-6,-7,-2,1,1,7,-5,-9,-1,7,1,-3,-4,-5,-9,-6,-7,-3,2,-4,-5,-6,-2,-9,-3,-10,-10,7,-8,-8,-3,-3,-1,-9,2,5,-4,8,-7,-1,-5,5,4,1,4,10,-6,-10,-1,10,-4,-1,-8,-6,-7,-5,10,10,-2,7,-10,5,-1,-3,-8,6,-9,-2,-3,4,-7,-2,9,-10,-3,-8,3,-1,10,7,-10,-10,9,8,2,3,8,-8,-9,9,7,-7,1,-5,5,-1,-4,-3,-4,-4,-2,-10,2,9,-8,5,4,-6,-1,9,2,2,10,-8,6,-5,-10,-9,2,-6,-6,4,3,6,10,4,5,7,-1,2,-10,8,-1,-2,6,-1,-9,2,-6,9,-6,-9,1,6,2,1,-6,-2,9,8,-4,-8,6,6,-10,2,-10,-5,-7,-4,1,-3,-6,2,8,3,-10,4,10,-2,9,-4,-4,-1,-2,-2,-10,-9,-9,-4,-2,-9,-7,-10,5,7,5,2,-10,8,7,4,4,-4,4,-10,-6,-1,-1,9,-3,7,-8,5,1,-2,5,6,1,4,9,-4,-2,9,3,7,-4,4,-5,-2,2,5,-1,-9,-2,-8,9,-7,6,-4,3,7,-8,-1,-7,9,6,9,6,10,2,-10,-9,-2,2,3,7,-5,8,10,-9,-7,5,-4,7,-9,-3,8,6,4,5,-7,7,1,-8,-5,8,-5,9,3,5,-4,1,-8,-3,-6,2,-3,5,-8,-3,-1,-4,-5,6,-10,-10,-7,6,9,-2,8,-8,4,-4,-6,5,9,4,6,-2,2,1,-4,-7,-6,7,2,6,-9,-10,7,-4,9,-10,9,1,3,-3,9,-1,-8,1,-2,-7,5,-7,5,9,-9,-8,1,10,-9,3,2,3,2,9,10,6,5,10,-3,5,7,10,3,4,-4,10,-10,-7,6,8,-4,-1,-6,-1,9,-2,-7,4,4,-2,4,-6,6,9,-9,-9,-9,-2,-3,-5,8,1,-10,7,-3,-4,-2,5,4,-9,-1,6,1,7,10,6,-1,-5,-2,-7,-1,3,-1,-1,-2,-8,1,5,1,-3,5,-10,6,9,8,-4,7,2,8,5,-6,-5,6,-8,-3,9,-4,-6,4,10,-1,3,-4,8,-10,3,5,-4,9,9,5,-2,6,-9,5,-4,-6,4,4,9,6,-10,2,-1,8,-5,-7,1,-6,6,2,8,9,-7,6,4,9,-1,10,2,-4,-10,-3,-4,5,-10,2,-6,-2,1,-8,9,1,-8,4,10,6,-8,-2,10,4,4,-10,4,-3,1,2,-9,-10,7,-9,-3,-4,6,5,3,9,-5,10,-2,-8,4,-3,-4,-2,-8,-7,-7,-3,-9,10,10,-1,-8,-8,-4,3,6,-1,-10,3,-3,10,1,3,-4,4,-4,-2,-6,5,7,-5,8,7,-8,-6,1,9,9,-4,8,-10,-2,9,3,7,-5,-2,10,-9,-10,-7,10,4,1,4,-5,4,-7,5,-6,-7,-7,-2,-10,3,-7,-2,-8,8,-6,1,-9,1,5,-5,10,-3,-2,-2,-7,4,-9,3,-3,-9,7,2,-2,-1,9,-1,9,6,9,6,4,2,-4,-3,7,-8,1,-10,5,3,9,-2,5,10,7,2,3,7,8,-6,1,9,8,-6,-1,6,10,-6,6,-1,-1,-4,-4,4,10,-8,8,4,5,6,6,5,9,-3,9,-8,4,7,-5,-3,-2,8,6,-5,-2,8,4,6,-7,8,2,6,-2,-7,5,1,-8,-7,-3,-7,5,2,1,3,-6,5,9,-3,6,7,7,9,9,2,-10,6,8,-7,6,8,2,-8,-7,-3,3,6,-10,-7,-3,-10,10,2,-3,-9,-10,-1,-2,-5,-1,4,10,4,-5,8,2,2,-5,-1,3,7,9,-6,-6,10,9,1,-5,9,8,9,7,-1,8,-1,4,-6,6,1,-3,1,-8,3,-9,-3,-2,-8,-8,3,3,-8,-4,7,6,-3,-1,-1,7,2,6,5,-2,9,4,-5,-8,3,5,1,9,10,-8,-1,-7,-3,10,5,2,1,5,-2,-9,4,-6,7,9,-5,10,-4,-1,-4,-4,3,10,-2,10,-8,1,-4,7,10,9,-4,3,8,4,5,10,4,1,-6,1,1,8,-9,-5,4,6,4,6,3,5,-8,5,-6,-9,9,-10,2,-4,-4,1,4,8,7,2,-3,-10,-4,4,-1,-6,-5,-1,-6,-9,3,-10,7,4,1,-6,5,-7,10,2,-8,-2,-7,-1,7,3,10,-8,9,-3,-2,-7,6,7,-9,7,-9,8,3,7,1,-3,-1,-10,-5,-3,5,-5,3,-6,10,10,2,5,9,-7,-10,-1,-1,3,7,4,-5,-2,-10,-1,-2,2,-8,1,-9,-8,-9,1,-4,-10,10,3,-3,-4,-3,-7,-7,-1,8,-4,8,-5,3,-9,-10,-9,2,-4,9,2,-4,-9,10,5,1,2,-3,8,-2,-4,7,3,-7,8,8,10,-1,-2,-10,-8,6,10,-8,7,7,-4,-5,6,7,-8,4,-6,8,3,-5,-6,-10,2,7,9,9,8,10,7,-6,2,-4,2,-4,-9,7,-2,4,-6,-1,2,-6,-5,-2,6,7,7,-4,-3,-5,9,-10,10,5,4,9,-6,-6,-3,-5,-10,7,-4,-8,1,-1,-7,1,4,3,10,4,9,10,10,-1,8,8,8,10,9,-8,-10,-6,-5,-2,1,4,6,9,9,-8,7,8,-2,-3,-10,1,-1,4,-4,-4,2,2,-2,-6,3,8,10,3,4,6,8,6,2,7,8,-10,9,-8,5,4,6,5,-7,9,-4,-7,-2,-2,-5,-10,-2,1,2,-4,3,-4,9,-8,-10,2,-2,6,2,-6,-9,-9,-9,-4,-2,-10,8,6,5,-6,1,-9,-8,6,-5,8,1,6,-8,2,9,-4,8,-4,6,-6,-9,9,-1,9,7,1,3,-9,8,-2,3,-3,8,2,1,-8,-4,-10,-9,-3,6,-6,1,-1,-5,5,-9,-9,-10,-8,10,3,-2,-2,-4,7,7,9,9,9,1,3,4,6,4,7,7,-1,5,-9,-6,-6,-2,-3], dtype = "uint8")#candidate|949|(1365,)|const|uint8
call_948 = relay.TupleGetItem(func_858_call(relay.reshape(const_949.astype('uint8'), [13, 7, 15])), 6)
call_950 = relay.TupleGetItem(func_861_call(relay.reshape(const_949.astype('uint8'), [13, 7, 15])), 6)
output = relay.Tuple([uop_924,call_948,const_949,])
output2 = relay.Tuple([uop_924,call_950,const_949,])
func_961 = relay.Function([var_923,], output)
mod['func_961'] = func_961
mod = relay.transform.InferType()(mod)
mutated_mod['func_961'] = func_961
mutated_mod = relay.transform.InferType()(mutated_mod)
var_962 = relay.var("var_962", dtype = "float32", shape = (4, 13, 4))#candidate|962|(4, 13, 4)|var|float32
func_961_call = mutated_mod.get_global_var('func_961')
call_963 = func_961_call(var_962)
output = call_963
func_964 = relay.Function([var_962], output)
mutated_mod['func_964'] = func_964
mutated_mod = relay.transform.InferType()(mutated_mod)
const_991 = relay.const([[[-10,-4,9,3],[-3,-6,-6,4],[1,9,8,-3],[6,-1,9,-2],[6,9,5,1],[10,4,8,4]],[[-8,1,1,-9],[2,-1,-3,7],[6,-5,9,9],[-5,7,-1,-5],[4,-6,-2,9],[-7,4,-3,9]]], dtype = "uint32")#candidate|991|(2, 6, 4)|const|uint32
var_992 = relay.var("var_992", dtype = "uint32", shape = (2, 6, 4))#candidate|992|(2, 6, 4)|var|uint32
bop_993 = relay.equal(const_991.astype('bool'), relay.reshape(var_992.astype('bool'), relay.shape_of(const_991))) # shape=(2, 6, 4)
output = bop_993
output2 = bop_993
func_1004 = relay.Function([var_992,], output)
mod['func_1004'] = func_1004
mod = relay.transform.InferType()(mod)
mutated_mod['func_1004'] = func_1004
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1005 = relay.var("var_1005", dtype = "uint32", shape = (2, 6, 4))#candidate|1005|(2, 6, 4)|var|uint32
func_1004_call = mutated_mod.get_global_var('func_1004')
call_1006 = func_1004_call(var_1005)
output = call_1006
func_1007 = relay.Function([var_1005], output)
mutated_mod['func_1007'] = func_1007
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1202 = relay.const([[[-6.442255,4.587880,3.548842],[7.673349,4.161023,-1.525864],[-3.216905,5.410687,-5.823476],[-0.112703,8.329660,8.609629],[-1.071564,-6.655250,-5.199016],[4.908796,7.623222,-7.140107],[-8.459433,-8.278590,-9.766953],[6.795594,-6.988239,-7.576772],[2.951098,-9.477347,7.970610],[6.603939,-0.181581,2.517040],[1.333699,8.992488,2.113074]]], dtype = "float64")#candidate|1202|(1, 11, 3)|const|float64
uop_1203 = relay.log10(const_1202.astype('float64')) # shape=(1, 11, 3)
output = relay.Tuple([uop_1203,])
output2 = relay.Tuple([uop_1203,])
func_1209 = relay.Function([], output)
mod['func_1209'] = func_1209
mod = relay.transform.InferType()(mod)
mutated_mod['func_1209'] = func_1209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1209_call = mutated_mod.get_global_var('func_1209')
call_1210 = func_1209_call()
output = call_1210
func_1211 = relay.Function([], output)
mutated_mod['func_1211'] = func_1211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1209_call = mod.get_global_var('func_1209')
func_1211_call = mutated_mod.get_global_var('func_1211')
call_1220 = relay.TupleGetItem(func_1209_call(), 0)
call_1221 = relay.TupleGetItem(func_1211_call(), 0)
output = call_1220
output2 = call_1221
func_1235 = relay.Function([], output)
mod['func_1235'] = func_1235
mod = relay.transform.InferType()(mod)
mutated_mod['func_1235'] = func_1235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1235_call = mutated_mod.get_global_var('func_1235')
call_1236 = func_1235_call()
output = call_1236
func_1237 = relay.Function([], output)
mutated_mod['func_1237'] = func_1237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1235_call = mod.get_global_var('func_1235')
func_1237_call = mutated_mod.get_global_var('func_1237')
call_1279 = func_1235_call()
call_1280 = func_1235_call()
var_1287 = relay.var("var_1287", dtype = "float64", shape = (6, 11, 3))#candidate|1287|(6, 11, 3)|var|float64
bop_1288 = relay.bitwise_xor(call_1279.astype('uint64'), var_1287.astype('uint64')) # shape=(6, 11, 3)
bop_1291 = relay.bitwise_xor(call_1280.astype('uint64'), var_1287.astype('uint64')) # shape=(6, 11, 3)
output = relay.Tuple([bop_1288,])
output2 = relay.Tuple([bop_1291,])
func_1307 = relay.Function([var_1287,], output)
mod['func_1307'] = func_1307
mod = relay.transform.InferType()(mod)
var_1308 = relay.var("var_1308", dtype = "float64", shape = (6, 11, 3))#candidate|1308|(6, 11, 3)|var|float64
output = func_1307(var_1308)
func_1309 = relay.Function([var_1308], output)
mutated_mod['func_1309'] = func_1309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1235_call = mod.get_global_var('func_1235')
func_1237_call = mutated_mod.get_global_var('func_1237')
call_1316 = func_1235_call()
call_1317 = func_1235_call()
output = relay.Tuple([call_1316,])
output2 = relay.Tuple([call_1317,])
func_1326 = relay.Function([], output)
mod['func_1326'] = func_1326
mod = relay.transform.InferType()(mod)
mutated_mod['func_1326'] = func_1326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1326_call = mutated_mod.get_global_var('func_1326')
call_1327 = func_1326_call()
output = call_1327
func_1328 = relay.Function([], output)
mutated_mod['func_1328'] = func_1328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1326_call = mod.get_global_var('func_1326')
func_1328_call = mutated_mod.get_global_var('func_1328')
call_1331 = relay.TupleGetItem(func_1326_call(), 0)
call_1332 = relay.TupleGetItem(func_1328_call(), 0)
func_858_call = mod.get_global_var('func_858')
func_861_call = mutated_mod.get_global_var('func_861')
const_1376 = relay.const([-4,-4,-5,-10,6,-5,-2,7,-10,-3,-10,8,-9,1,-8,-7,-1,-3,6,1,-1,4,5,-9,4,5,-8,-5,-1,6,-7,6,-4,6,10,3,-6,-9,8,-7,-9,-8,3,-5,10,-8,6,6,-10,-1,10,4,-1,-8,-10,-3,9,-5,3,-9,-1,1,-10,9,-9,-2,4,-6,8,6,-1,6,-8,-4,-3,5,9,-3,-3,1,-1,-1,-7,-2,1,5,-4,-1,6,-3,-8,2,6,-8,-8,-1,10,-5,-6,-5,2,-10,3,-9,7,-5,-2,-6,-4,5,5,-10,7,3,-2,-10,-10,-1,4,-1,1,7,7,-10,-10,-1,-3,10,-8,-3,3,5,6,8,7,10,-9,1,-2,5,10,-7,-10,-10,1,-1,9,-10,3,2,9,-5,-10,-2,-1,-6,-6,-1,9,-5,7,5,-1,8,4,1,3,-2,6,7,3,-6,6,3,1,6,-3,3,-7,-7,2,-4,8,9,-10,-1,2,9,-5,1,-10,3,7,9,-6,7,-6,4,-7,-8,-1,-7,6,-1,10,-6,-1,6,-6,4,-3,1,-1,3,-8,-4,-10,4,-9,-7,-8,-1,-6,9,-4,-6,-5,8,2,4,4,8,1,2,-8,-10,5,-5,10,3,-8,-3,-5,-9,-2,-6,-10,-4,8,-2,-8,3,4,4,-6,10,-5,-7,3,9,8,4,10,1,-6,6,-7,-7,9,-7,-8,8,-7,6,-10,5,-10,8,-9,-10,3,-8,5,1,7,-8,4,-8,1,-3,9,-3,-9,1,-1,4,6,-4,9,6,5,9,-10,-10,-3,5,1,2,-8,-9,-5,3,-6,2,-6,1,2,1,-9,6,6,-3,-9,8,-10,-6,-1,-4,-8,2,7,-5,5,5,-9,-5,2,3,-3,-1,-9,7,8,6,-10,-9,-4,-9,2,-3,5,-7,6,-10,-10,-3,8,10,-1,-1,7,-9,-8,-1,2,-3,-2,4,8,-8,-7,-9,8,2,-6,-2,4,-5,2,3,10,1,-6,-1,-10,-5,9,-3,-1,-8,-7,9,4,6,-10,7,6,-5,2,-7,4,-1,-5,-1,7,-5,-10,8,10,9,4,3,4,2,-3,-10,2,9,-4,-4,-10,9,-5,5,10,9,-1,-4,8,3,-7,-8,4,4,8,3,1,1,9,-3,-9,5,-5,-7,6,-4,-2,-2,10,8,-8,-9,3,4,5,10,-2,-5,3,9,1,4,8,2,4,7,1,10,5,5,-3,-5,2,-3,-4,-6,-10,10,6,5,4,-1,-7,10,-7,3,1,-7,9,-8,4,10,4,-9,4,2,5,4,4,-5,8,-3,7,-10,9,1,-1,9,-9,-8,4,10,3,3,-7,-10,-6,3,-10,10,-2,5,10,-1,-2,-3,-8,6,-8,-1,-7,7,4,7,-5,-7,7,-10,-6,7,1,6,4,5,3,4,-8,3,3,8,-6,4,-7,-10,9,-4,-9,2,-6,-5,2,9,2,-2,4,4,-4,-1,5,5,9,4,10,1,-4,5,8,8,7,-7,-1,-1,9,6,-5,8,10,2,-2,8,-1,-4,10,-9,1,8,-6,8,2,1,-7,-3,-5,-9,-10,-10,3,-10,-5,9,-4,9,7,9,-3,9,1,7,7,-2,-6,-9,-8,9,7,-1,-7,3,8,-5,2,1,6,-1,5,-1,8,9,7,9,-7,7,1,-8,-1,1,5,-1,9,3,7,-6,-1,1,2,4,-10,-3,-10,-9,-2,-8,-2,9,1,7,5,3,8,-8,3,2,-4,4,4,6,-4,4,-5,7,-6,-6,-8,8,4,-10,7,-10,-7,-6,-8,8,9,7,-6,2,9,-2,6,6,-6,-6,-8,-8,3,-5,-8,-4,-8,3,-5,5,-10,2,-9,-7,-3,-1,-3,6,-1,-8,8,6,-3,10,-3,-2,6,-10,-2,-1,1,-8,9,10,-8,10,8,-2,6,-9,-10,1,-6,-10,-9,-5,-1,3,-10,-1,-9,4,9,-10,-7,4,-3,3,6,-8,-2,-3,10,4,-9,8,-6,-7,6,9,-10,3,8,3,-1,8,7,-8,-1,7,-9,-10,-7,1,-6,-9,5,-2,-1,-6,-7,6,10,-1,8,1,-2,4,7,3,8,-2,5,4,8,-6,8,8,-8,9,4,-5,10,-8,-3,-2,2,-3,-9,-2,-9,-3,2,5,8,-8,-5,-1,-10,-1,9,-5,-9,-7,-5,7,-9,3,2,3,-3,2,-6,10,-3,1,6,2,-4,6,-2,-3,3,-4,3,5,-2,3,-2,-4,-4,9,-10,-5,-2,4,-4,-4,-5,4,-10,6,-7,-8,2,6,-6,7,-5,-10,5,-10,-5,8,5,-9,-2,-4,2,8,3,-9,8,-5,-8,10,1,2,2,-5,5,-9,9,-6,7,-4,-9,-9,10,-1,-1,2,9,-9,8,-8,-9,10,4,8,1,10,-6,-10,-5,5,-10,-9,4,9,-3,5,-8,8,2,-1,-10,4,2,-2,-4,2,-5,10,10,-3,8,2,2,8,-8,8,2,3,5,10,4,1,4,1,5,-6,2,1,-10,10,7,-5,10,-2,3,4,5,-7,1,4,1,-10,-8,9,-7,-7,8,3,9,-3,-5,-8,-6,-1,4,-4,-5,-8,-3,-10,-7,-5,8,1,3,-10,4,-1,4,7,5,-2,4,-3,6,-7,2,-8,-2,-8,4,5,7,-8,8,-8,7,-5,-10,9,-4,9,-2,8,5,-9,7,6,-10,4,10,-2,2,1,8,9,8,-9,4,-2,-7,-9,7,-8,-2,6,4,10,-7,-9,-10,-6,6,-7,-5,9,-2,-6,-4,9,-7,-7,-4,7,7,-6,-4,-5,8,-9,1,-4,-8,3,5,9,6,2,-4,-3,7,-10,-2,9,5,4,10,8,-10,-2,-4,8,-7,-1,-1,4,6,9,8,-9,-8,8,10,-5,-10,9,8,-3,-8,-5,-1,-7,4,-4,-3,-5,7,-10,3,9,-2,7,-6,4,7,4,-10,-6,8,7,4,-4,-7,-7,-2,2,-7,-6,9,8,1,5,-7,-6,-10,6,-4,4,9,-10,10,-6,2,9,-2,-1,-10,-4,7,2,4,-1,2,-10,9,-1,5,-5,9,-10,2,6,8,-9,-2,2,10,-4,1,3,-3,8,-2,-7,-6,4,8,1,9,-1,-2,-7,-6,-5,5,6,2,8,-4,5,-1,9,-8,-7,2,-10,-3,-7,9,6,9,2,6,7,4,-2,-2,4,3,1,-9,8,-9,1,-8,-10,10,10,3,-6,9,9,10,3,7,7,-4,-10,-1,-9,-9,-7,2,-7,-7,9,2,9,-5,5,6,-10,10,-5,10,-1,-4,9,8,-10,-10,2,9,4,-4,6,5,-2,3,-8,-3,5,9,-3,2,3,2,-4,5,-5,-8,-10,-6,-10,2,-5,6,2,3,-4,7,-5,-3,10,-8,10,7,-1,-4,1,8,3,-5,1,10,-3,7,6,8,9,-10,-1,8,-9,2,10,-7,6,-10,9,6,-7,-9,-2,-8,10,9,6,-1,2,6,-3,-7,-4,-8,4,-5,5,-3,-9,-8,-10,10,6,2,7,10,-10,1,-3,-7,2,-8,-5,6,4,3], dtype = "uint8")#candidate|1376|(1365,)|const|uint8
call_1375 = relay.TupleGetItem(func_858_call(relay.reshape(const_1376.astype('uint8'), [13, 7, 15])), 3)
call_1377 = relay.TupleGetItem(func_861_call(relay.reshape(const_1376.astype('uint8'), [13, 7, 15])), 3)
func_961_call = mod.get_global_var('func_961')
func_964_call = mutated_mod.get_global_var('func_964')
var_1379 = relay.var("var_1379", dtype = "float32", shape = (104, 2))#candidate|1379|(104, 2)|var|float32
call_1378 = relay.TupleGetItem(func_961_call(relay.reshape(var_1379.astype('float32'), [4, 13, 4])), 0)
call_1380 = relay.TupleGetItem(func_964_call(relay.reshape(var_1379.astype('float32'), [4, 13, 4])), 0)
uop_1393 = relay.sin(var_1379.astype('float32')) # shape=(104, 2)
output = relay.Tuple([call_1331,call_1375,const_1376,call_1378,uop_1393,])
output2 = relay.Tuple([call_1332,call_1377,const_1376,call_1380,uop_1393,])
func_1396 = relay.Function([var_1379,], output)
mod['func_1396'] = func_1396
mod = relay.transform.InferType()(mod)
var_1397 = relay.var("var_1397", dtype = "float32", shape = (104, 2))#candidate|1397|(104, 2)|var|float32
output = func_1396(var_1397)
func_1398 = relay.Function([var_1397], output)
mutated_mod['func_1398'] = func_1398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1326_call = mod.get_global_var('func_1326')
func_1328_call = mutated_mod.get_global_var('func_1328')
call_1409 = relay.TupleGetItem(func_1326_call(), 0)
call_1410 = relay.TupleGetItem(func_1328_call(), 0)
output = call_1409
output2 = call_1410
func_1411 = relay.Function([], output)
mod['func_1411'] = func_1411
mod = relay.transform.InferType()(mod)
mutated_mod['func_1411'] = func_1411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1411_call = mutated_mod.get_global_var('func_1411')
call_1412 = func_1411_call()
output = call_1412
func_1413 = relay.Function([], output)
mutated_mod['func_1413'] = func_1413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1235_call = mod.get_global_var('func_1235')
func_1237_call = mutated_mod.get_global_var('func_1237')
call_1475 = func_1235_call()
call_1476 = func_1235_call()
output = relay.Tuple([call_1475,])
output2 = relay.Tuple([call_1476,])
func_1493 = relay.Function([], output)
mod['func_1493'] = func_1493
mod = relay.transform.InferType()(mod)
mutated_mod['func_1493'] = func_1493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1493_call = mutated_mod.get_global_var('func_1493')
call_1494 = func_1493_call()
output = call_1494
func_1495 = relay.Function([], output)
mutated_mod['func_1495'] = func_1495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1493_call = mod.get_global_var('func_1493')
func_1495_call = mutated_mod.get_global_var('func_1495')
call_1498 = relay.TupleGetItem(func_1493_call(), 0)
call_1499 = relay.TupleGetItem(func_1495_call(), 0)
output = call_1498
output2 = call_1499
func_1516 = relay.Function([], output)
mod['func_1516'] = func_1516
mod = relay.transform.InferType()(mod)
mutated_mod['func_1516'] = func_1516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1516_call = mutated_mod.get_global_var('func_1516')
call_1517 = func_1516_call()
output = call_1517
func_1518 = relay.Function([], output)
mutated_mod['func_1518'] = func_1518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1411_call = mod.get_global_var('func_1411')
func_1413_call = mutated_mod.get_global_var('func_1413')
call_1524 = func_1411_call()
call_1525 = func_1411_call()
output = relay.Tuple([call_1524,])
output2 = relay.Tuple([call_1525,])
func_1526 = relay.Function([], output)
mod['func_1526'] = func_1526
mod = relay.transform.InferType()(mod)
output = func_1526()
func_1527 = relay.Function([], output)
mutated_mod['func_1527'] = func_1527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1326_call = mod.get_global_var('func_1326')
func_1328_call = mutated_mod.get_global_var('func_1328')
call_1552 = relay.TupleGetItem(func_1326_call(), 0)
call_1553 = relay.TupleGetItem(func_1328_call(), 0)
output = relay.Tuple([call_1552,])
output2 = relay.Tuple([call_1553,])
func_1554 = relay.Function([], output)
mod['func_1554'] = func_1554
mod = relay.transform.InferType()(mod)
output = func_1554()
func_1555 = relay.Function([], output)
mutated_mod['func_1555'] = func_1555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1326_call = mod.get_global_var('func_1326')
func_1328_call = mutated_mod.get_global_var('func_1328')
call_1562 = relay.TupleGetItem(func_1326_call(), 0)
call_1563 = relay.TupleGetItem(func_1328_call(), 0)
func_858_call = mod.get_global_var('func_858')
func_861_call = mutated_mod.get_global_var('func_861')
const_1571 = relay.const([9,-1,7,5,-5,-3,6,-3,-6,-8,6,-1,-3,-6,1,6,-3,-4,10,6,-6,10,4,8,8,-1,5,-1,-10,-9,-4,3,-2,8,8,-9,4,4,-3,-7,10,7,2,8,-7,-5,2,8,6,-7,-9,-7,-4,-10,7,9,-5,-5,-6,-9,9,-6,3,-4,2,-3,8,4,5,10,-1,-9,7,3,8,8,7,8,-8,9,6,2,4,-5,-2,-8,5,-9,-3,6,4,1,-8,1,3,-7,-2,2,-5,-4,3,-9,-1,-9,-1,-8,-8,8,7,-5,1,-9,1,10,10,4,-6,-10,-1,3,-5,-9,-1,-1,8,9,8,-4,-1,6,8,5,-2,3,5,7,9,2,-5,-8,-9,-2,-7,5,-1,-9,2,3,10,-9,-3,6,-6,-2,3,4,9,8,-2,-3,-5,-10,-8,-3,10,-7,2,-7,-4,-7,-8,-9,-7,-2,2,-2,8,6,-6,8,4,-10,-9,-5,5,9,5,2,-7,-2,10,9,-5,-5,5,10,-9,8,-7,-10,-6,-8,1,4,-4,8,-10,3,-2,-10,-2,-8,1,8,10,-2,8,-9,2,8,2,10,-3,-1,1,-5,10,-3,-1,8,-8,-10,-10,5,4,8,9,10,-2,10,2,6,9,2,-10,-3,-9,-5,4,1,-1,-6,6,2,-8,-1,8,-10,-9,-10,3,7,6,2,-10,-8,9,-1,1,-3,8,7,1,4,2,-9,7,8,8,5,-3,10,8,-9,9,-6,-7,-4,2,10,-3,-10,7,-6,-10,-4,4,6,-7,1,-8,4,9,6,9,-9,5,3,-9,-6,1,-3,3,-7,6,-8,-4,-2,2,8,1,4,-7,7,-7,9,10,1,1,6,7,-4,8,-5,3,2,1,10,-10,-7,10,4,-8,-5,-4,-8,7,-3,-7,5,-4,-4,10,4,-10,10,-7,-10,-9,3,10,-6,3,-1,-10,10,5,8,7,9,2,-7,-2,-3,-6,4,-8,-2,-10,1,1,-1,-5,-4,-2,10,-10,3,8,3,-2,9,-7,-1,5,-6,-3,-5,-9,-1,-1,3,1,-3,3,2,-5,7,3,-1,-10,-7,6,-3,10,-6,-6,2,6,-4,-3,6,9,-2,-1,-3,9,-6,-9,-2,3,-9,6,4,-7,10,-7,8,10,-10,-10,-4,10,-6,8,-9,-5,-10,8,-2,2,-4,8,7,-1,-1,-10,2,4,3,9,3,-10,6,4,-4,-1,9,2,9,5,-6,2,8,-9,8,-3,-1,-1,-5,-2,3,-9,3,8,-7,-2,9,3,8,8,-8,-6,-6,-4,3,-1,-1,1,-2,-8,4,-1,3,-10,-4,8,9,-10,10,5,-2,-2,-7,-1,-3,-7,8,-10,2,4,8,9,-6,2,5,-1,-6,-3,5,-3,10,5,-9,-1,-5,-8,-6,10,-6,-8,-4,9,2,-4,-4,5,-10,-6,-3,2,1,-1,-7,-1,-7,-5,7,-10,5,-6,-4,7,-9,-3,-1,2,-4,-10,-8,-3,9,-4,3,-7,-2,1,4,-8,-2,-9,7,-6,-6,2,-7,-7,-5,7,8,10,7,-4,9,5,-4,-6,-6,1,-7,8,-10,-4,-7,-6,-5,3,-8,-2,-10,10,-3,-6,-7,1,-10,1,5,6,6,-6,-8,2,7,-3,-3,2,9,5,3,-3,-6,-4,10,2,3,7,-9,7,5,3,-5,3,3,4,-3,-2,1,-9,-7,7,9,5,-2,-3,4,-4,3,7,-3,-3,-7,-5,-10,-9,5,10,9,9,-8,10,-8,-5,4,-6,-2,-5,-3,-9,-7,3,4,4,-9,-9,-5,2,-5,-4,-8,8,-1,-1,5,9,-8,-4,6,-6,-2,3,-3,-3,-10,9,-1,-10,-10,-7,10,-7,-6,9,-10,6,-9,1,4,4,5,3,-10,6,-3,5,9,-10,-4,7,-5,5,-4,7,4,-5,5,-5,-1,7,4,-7,-5,-7,7,2,-9,-5,-7,2,-6,-8,-4,-5,6,9,5,2,-3,8,5,10,-1,6,9,-9,4,5,-2,3,4,7,-7,7,10,-10,9,6,6,8,-1,-2,4,-4,-10,2,10,1,-8,7,-8,-2,8,-9,-1,2,3,8,-1,-6,1,5,7,1,6,5,7,-1,5,-9,-6,-10,-5,8,3,9,2,-5,9,6,4,-9,1,5,-1,-2,-5,6,1,8,-8,7,-10,-8,-10,4,10,-4,5,-6,-4,-3,-1,9,-5,-5,5,-2,4,-1,6,8,-9,6,-2,8,1,4,-2,-3,3,9,-9,10,3,-8,9,7,-8,1,5,7,3,-5,8,2,-5,-7,2,-8,3,3,9,9,3,9,-9,2,-8,7,-7,7,-7,-8,4,-3,-1,-8,-6,-10,-6,5,-5,-9,5,9,4,8,2,2,2,-4,4,3,-8,-7,10,-4,-10,-8,-9,-1,-6,-6,-4,4,-6,9,10,-7,5,-5,-9,-1,-3,6,-7,7,-5,-2,1,-3,6,-4,3,5,9,-2,2,-7,-2,7,9,5,-6,3,4,-4,-9,5,4,-10,3,-1,-5,9,1,-9,9,4,-10,5,-4,-4,-9,-5,-10,-8,-8,7,-5,-3,2,7,-7,-7,10,2,-10,9,5,6,10,8,1,1,2,2,-7,5,2,10,-3,7,7,7,-1,-7,7,9,3,-3,8,-10,6,9,-9,-3,-1,10,-8,2,-9,2,-6,-3,-3,-5,4,5,3,2,-5,8,5,8,6,5,-10,-3,-8,-7,-5,-3,10,-10,4,-8,-7,6,8,-7,3,10,-7,-2,-1,7,3,-4,-7,-9,10,-9,6,9,9,-8,8,-6,3,1,8,10,7,6,2,-7,5,-9,3,-4,-6,3,-2,-2,-8,9,-10,-7,4,-2,-9,9,7,4,8,10,-2,-9,-3,-7,3,-7,6,-1,-9,9,4,-3,-7,-8,-7,-8,-1,-1,-5,7,8,-2,-8,-7,6,7,5,10,7,7,-6,10,2,-4,-2,7,-5,-4,-2,1,8,-9,-8,-7,6,-6,10,2,9,-9,8,-1,-6,7,-8,7,8,1,4,-8,3,-5,-4,-3,6,4,-1,-9,1,-5,6,-7,6,8,-7,2,-4,2,-5,-1,-8,-5,1,6,-9,5,10,10,1,10,8,-9,-1,10,-4,7,5,3,-7,10,-9,-3,-6,-9,-5,-6,-10,-5,3,-7,4,1,7,5,-2,-1,-7,-9,1,1,-6,-9,9,-7,7,9,9,1,3,-9,-1,7,-9,3,6,-4,-9,9,6,10,10,-5,9,-5,3,9,-8,-2,-3,-5,-6,-1,1,-3,-6,10,-2,4,-2,6,-5,-7,-3,8,-5,7,1,8,-8,8,-6,9,-5,9,-2,-3,2,-9,-1,1,9,7,5,-1,8,6,-10,-2,-8,2,-8,8,-5,4,-4,-3,-2,3,8,2,-5,-10,3,-2,4,2,1,9,9,-3,10,-5,6,2,2,-10,4,6,1,-10,-3,7,4,-9,1,5,-8,4,6,8,1,9,-7,1,-4,-4,-5,1,7,4,2,9,-8,3,-8,4,-6,-3,7,-2,-6,7,7,3,-8,2,-4,9,4,8,3,-1,4,-4,9,1,2,9], dtype = "uint8")#candidate|1571|(1365,)|const|uint8
call_1570 = relay.TupleGetItem(func_858_call(relay.reshape(const_1571.astype('uint8'), [13, 7, 15])), 4)
call_1572 = relay.TupleGetItem(func_861_call(relay.reshape(const_1571.astype('uint8'), [13, 7, 15])), 4)
output = relay.Tuple([call_1562,call_1570,const_1571,])
output2 = relay.Tuple([call_1563,call_1572,const_1571,])
func_1574 = relay.Function([], output)
mod['func_1574'] = func_1574
mod = relay.transform.InferType()(mod)
output = func_1574()
func_1575 = relay.Function([], output)
mutated_mod['func_1575'] = func_1575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1411_call = mod.get_global_var('func_1411')
func_1413_call = mutated_mod.get_global_var('func_1413')
call_1582 = func_1411_call()
call_1583 = func_1411_call()
func_1526_call = mod.get_global_var('func_1526')
func_1527_call = mutated_mod.get_global_var('func_1527')
call_1587 = relay.TupleGetItem(func_1526_call(), 0)
call_1588 = relay.TupleGetItem(func_1527_call(), 0)
bop_1602 = relay.minimum(call_1587.astype('uint16'), relay.reshape(call_1582.astype('uint16'), relay.shape_of(call_1587))) # shape=(1, 11, 3)
bop_1605 = relay.minimum(call_1588.astype('uint16'), relay.reshape(call_1583.astype('uint16'), relay.shape_of(call_1588))) # shape=(1, 11, 3)
func_112_call = mod.get_global_var('func_112')
func_115_call = mutated_mod.get_global_var('func_115')
const_1612 = relay.const([7,-7,-7,6,3,4,-7,2,-10,6,-3,-1,5,1,8,5,9,-8,5,8,4,-5,-1,-2,3,-4,-4,3,4,9,5,-7,5,1,-9,-7,1,4,1,2,4,2,10,9,9,-5,-3,-9,10,-10,8,-2,1,10,3,-8,7,-7,5,-10,6,-9,10,1,9,-10,9,8,9,-4,2,-7,5,-6,2,5,3,-8,5,4,-1,2,8,9,-10,8,-8,10,1,-4,-6,-10,4,-4,7,4,4,-5,-8,8,1,1,-10,-5,-1,-3,-9,-5,-1,3,-9,-6,-2,3,-7,-9,8,-10,-1,1,-5,8,-9,6,-2,-10,3,-5,-6,5,1,6,4,-8,-2,-8,3,-8,8,4,10,-2,9,9,6,-1,-8,6,2,6,5,8,9,-2,-1,-9,-10,5,10,5,6,5,-2,5,-7,7,-4,-9,2,-1,6,3,3,-5,1,-9,5,-10,-4,-8,-7,-2,1,-5,-3,-5,8,-6,5,-2,-1,-3,4,3,2,1,-8,2,6,-2,6,9,3,-3,-9,5,5,-8,5,8,-5,-5,-4,2,-4,9,2,-4,-5,5,1,8,10,-6,9,2,-3,-9,-6,8,-7,-2,7,4,-2,-8,1,-2,1,-7,1,6,-6,2,-6,-4,9,2,9,-10,4,-7,-5,5,-4,-8,-2,3,-7,-2,7,-8,9,2,3,-10,-9,2,-5,-10,9,-5,10,9,-5,4,4,-8,-9,2,10,1,-8,-3,-1,-3,1,-1,6,-10,-10,2,-6,8,1,-7,3,-10,2,3,6,-6,-4,8,7,-2,2,-5,-4,-4,-5,6,3,-9,9,10,8,10,1,3,-8,8,-10,-10,8,-9,-7,8,-3,4,-9,-9,10,-10,-9,-10,-9,-7,-3,-3,-1,1,1,9,-6,-8,-9,3,-6,10,-7,10,-1,7,6,-5,4,6,-5,9,-7,-8,6,4,6,7,6,-1,6,3,8,8,3,-9,-6,2,7,-10,1,5,9,1,9,6,-2,7,6,3,-9,8,1,9,-1,-1,2,-10,-7,-8,-2,4,-3,3,-6,9,-1,1,8,-1,8,1,-9,-2,-1,5,-7,9,-7,7,1,9,4,5,9,-1,10,-8,3,7,2,-9,-10,7,3,1,2,7,1,8,-9,-8,2,-10,-7,1,1,-8,-8,-8,-1,-6,-10,-10,4,2,8,-2,7,-7,1,4,8,2,-7,9,-9,2,8,4,-10,7,8,8,3,10,3,-5,5,7,10,-1,-2,10,-5,-4,-1,-2,-10,4,6,-9,-7,-8,-4,8,4,2,-2,-8,7,9,4,-4,-2,10,-2,4,3,-6,10,10,-1,10,5,10,1,-9,-3,-1,-3,2,2,-9,-10,4,6,4,8,-3,-3,4,-4,-10,10,-1,-4,10,-1,-3,-3,10,2,-7,9,1,4,-7,2,7,-1,-7,-1,3,8,-2,-4,8,-8,4,6,-3,-5,-1,10,-1,6,7,4,9,9,-1,-6,9,-8,5,-10,-6,-9,-2,-3,-1,10,6,2,-6,-9,-4,-7,-8,5,9,-2,-10,2,-1,4,5,3,-6,9,8,10,-10,4,-2,-3,-4,-5,-5,6,-3,-9,-4,2,-9,-3,-6,8,10,7,-3,-4,-3,-5,8,-6,2,9,-10,-8,-1,-6,4,6,8,-5,-2,-1,-7,-5,8,6,-7,-5,-8,-5,-4,8,5,-1,5,-5,4,-4,-2,8,10,-9,-10,3,-9,-9,-9,10,-10,6,-8,4,9,-5,-9,-1,6,6,-6,8,-7,-10,-3,-8,-3,8,-9,3,2,-9,10,10,1,6,4,3,-10,-6,3,-3,2,10,-8,9,1,-3,-9,-9,-8,8,-8,3,-3,-10,-5,-5,-6,8,7,4,-7,-1,9,-7,-8,10,5,3,-2,-6,-5,6,7,-7,-1,-6,-9,5,8,6,-8,-1,10,10,-8,1,-9,-7,8,3,-5,10,-6,2,8,2,-4,8,9,-8,-4,10,-3,-2,-3,4,3,-1,-10,5,-3,-5,-9,1,-1,-7,-7,10,6,-4,-6,6,-4,-8,-2,-4,9,-1,10,-8,-2,-6,2,2,-6,6,7,-1,8,5,4,4,9,-2,7,2,5,-10,-3,-4,9,3,1,-4,5,9,-1,3,-8,2,6,-7,-1,-9,-9,5,2,-1,4,-4,-9,8,-7,1,-7,1,7,4,4,2,6,-9,-7,-5,-8,-2,3,-8,-3,4,-1,3,2,6,1,-9,-7,-9,-1,-7,-3,-7,-1,5,-3,5,-3,-2,6,-2,5,-5,-2,-7,9,3,3,6,-6,-9,9,2,2,8,-1,-6,4,7,8,-8,-7,6,-4,7,5,-10,10,6,-8,-10,7,-3,9,-4,5,-3,6,4,4,-1,-7,-3,4,9,-6,-1,8,3,-6,-2,10,3,5,-5,7,9,-6,3,2,10,-2,10,-6,7,1,-1,7,8,-1,2,-10,4,-3,-5,-8,2,7,1,-4,-3,10,-7,-10,-8,7,-1,-2,2,1,-10,-4,10,-4,-3,9,-5,-4,5,-7,-6,-6,-3,3,6,3,-2,8,-8,-3,3,9,-3,10,6,3,-4,-1,7,-2,-6,9,-4,2,-1,3,8,-6,6,1,5,-5,2,4,8,4,-1,-5,-2,-6,-3,1,-2,4,-2,9,-6,-6,8,10,6,-1,-9,-3,-3,-5,10,8,2,-10,-5,-4,3,1,-10,9,-7,4,-7,6,-5,-6,9,-7,-6,-7,-5,-5,-1,-10,-9,8,9,1,-10,-8,8,-10,-10,7,-5,8,-7,8,1,-2,7,8,1,-4,6,8,7,-2,6,-4,6,-10,-7,5,-6,-10,-5,9,-6,1,-6,-8,6,2,1,-2,8,-4,-8,-4,-3,7,1,-8,-2,10,5,-3,-10,-2,10,2,3,4,-2,-8,-1,7,-5,-10,3,7,10,8,2,2,3,10,7,-9,-2,-6,-6,-8,9,9,8,9,-3,-7,-8,-9,-1,6,6,-9,-4,3,9,10,9,-9,5,-4,-6,7,10,-4,8,-10,-5,3,5,1,9,-1,3,7,7,-6,4,6,1,6,-10,-2,-5,-6,10,6,9,10,-7,-9,6,-7,1,6,-3,-9,-9,8,5,6,-1,7,-10,-3,-3,1,-8,-2,4,-10,10,-10,10,5,-3,-5,1,-8,8,-8,-2,10,9,-10,10,2,9,9,1,7,2,10,-3,-6,8,3,5,3,-7,-9,-2,7,4,-3,9,-10,-9,6,-9,-4,-8,-10,-10,9,5,-4,-2,8,-6,-10,10,-6,10,-2], dtype = "int16")#candidate|1612|(1248,)|const|int16
call_1611 = relay.TupleGetItem(func_112_call(relay.reshape(const_1612.astype('int16'), [16, 13, 6]), relay.reshape(const_1612.astype('int16'), [16, 13, 6]), ), 1)
call_1613 = relay.TupleGetItem(func_115_call(relay.reshape(const_1612.astype('int16'), [16, 13, 6]), relay.reshape(const_1612.astype('int16'), [16, 13, 6]), ), 1)
output = relay.Tuple([bop_1602,call_1611,const_1612,])
output2 = relay.Tuple([bop_1605,call_1613,const_1612,])
func_1628 = relay.Function([], output)
mod['func_1628'] = func_1628
mod = relay.transform.InferType()(mod)
output = func_1628()
func_1629 = relay.Function([], output)
mutated_mod['func_1629'] = func_1629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1574_call = mod.get_global_var('func_1574')
func_1575_call = mutated_mod.get_global_var('func_1575')
call_1665 = relay.TupleGetItem(func_1574_call(), 1)
call_1666 = relay.TupleGetItem(func_1575_call(), 1)
func_858_call = mod.get_global_var('func_858')
func_861_call = mutated_mod.get_global_var('func_861')
var_1671 = relay.var("var_1671", dtype = "uint8", shape = (1365,))#candidate|1671|(1365,)|var|uint8
call_1670 = relay.TupleGetItem(func_858_call(relay.reshape(var_1671.astype('uint8'), [13, 7, 15])), 4)
call_1672 = relay.TupleGetItem(func_861_call(relay.reshape(var_1671.astype('uint8'), [13, 7, 15])), 4)
func_112_call = mod.get_global_var('func_112')
func_115_call = mutated_mod.get_global_var('func_115')
call_1682 = relay.TupleGetItem(func_112_call(relay.reshape(call_1665.astype('int16'), [16, 13, 6]), relay.reshape(call_1670.astype('int16'), [16, 13, 6]), ), 0)
call_1683 = relay.TupleGetItem(func_115_call(relay.reshape(call_1665.astype('int16'), [16, 13, 6]), relay.reshape(call_1670.astype('int16'), [16, 13, 6]), ), 0)
func_1326_call = mod.get_global_var('func_1326')
func_1328_call = mutated_mod.get_global_var('func_1328')
call_1693 = relay.TupleGetItem(func_1326_call(), 0)
call_1694 = relay.TupleGetItem(func_1328_call(), 0)
func_1526_call = mod.get_global_var('func_1526')
func_1527_call = mutated_mod.get_global_var('func_1527')
call_1705 = relay.TupleGetItem(func_1526_call(), 0)
call_1706 = relay.TupleGetItem(func_1527_call(), 0)
output = relay.Tuple([call_1665,call_1670,var_1671,call_1682,call_1693,call_1705,])
output2 = relay.Tuple([call_1666,call_1672,var_1671,call_1683,call_1694,call_1706,])
func_1712 = relay.Function([var_1671,], output)
mod['func_1712'] = func_1712
mod = relay.transform.InferType()(mod)
mutated_mod['func_1712'] = func_1712
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1713 = relay.var("var_1713", dtype = "uint8", shape = (1365,))#candidate|1713|(1365,)|var|uint8
func_1712_call = mutated_mod.get_global_var('func_1712')
call_1714 = func_1712_call(var_1713)
output = call_1714
func_1715 = relay.Function([var_1713], output)
mutated_mod['func_1715'] = func_1715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1209_call = mod.get_global_var('func_1209')
func_1211_call = mutated_mod.get_global_var('func_1211')
call_1717 = relay.TupleGetItem(func_1209_call(), 0)
call_1718 = relay.TupleGetItem(func_1211_call(), 0)
var_1725 = relay.var("var_1725", dtype = "float64", shape = (10, 11, 3))#candidate|1725|(10, 11, 3)|var|float64
bop_1726 = relay.floor_mod(call_1717.astype('float64'), var_1725.astype('float64')) # shape=(10, 11, 3)
bop_1729 = relay.floor_mod(call_1718.astype('float64'), var_1725.astype('float64')) # shape=(10, 11, 3)
uop_1740 = relay.acos(var_1725.astype('float64')) # shape=(10, 11, 3)
func_1516_call = mod.get_global_var('func_1516')
func_1518_call = mutated_mod.get_global_var('func_1518')
call_1748 = func_1516_call()
call_1749 = func_1516_call()
output = relay.Tuple([bop_1726,uop_1740,call_1748,])
output2 = relay.Tuple([bop_1729,uop_1740,call_1749,])
func_1768 = relay.Function([var_1725,], output)
mod['func_1768'] = func_1768
mod = relay.transform.InferType()(mod)
var_1769 = relay.var("var_1769", dtype = "float64", shape = (10, 11, 3))#candidate|1769|(10, 11, 3)|var|float64
output = func_1768(var_1769)
func_1770 = relay.Function([var_1769], output)
mutated_mod['func_1770'] = func_1770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1209_call = mod.get_global_var('func_1209')
func_1211_call = mutated_mod.get_global_var('func_1211')
call_1815 = relay.TupleGetItem(func_1209_call(), 0)
call_1816 = relay.TupleGetItem(func_1211_call(), 0)
output = call_1815
output2 = call_1816
func_1817 = relay.Function([], output)
mod['func_1817'] = func_1817
mod = relay.transform.InferType()(mod)
mutated_mod['func_1817'] = func_1817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1817_call = mutated_mod.get_global_var('func_1817')
call_1818 = func_1817_call()
output = call_1818
func_1819 = relay.Function([], output)
mutated_mod['func_1819'] = func_1819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1516_call = mod.get_global_var('func_1516')
func_1518_call = mutated_mod.get_global_var('func_1518')
call_1839 = func_1516_call()
call_1840 = func_1516_call()
func_1554_call = mod.get_global_var('func_1554')
func_1555_call = mutated_mod.get_global_var('func_1555')
call_1850 = relay.TupleGetItem(func_1554_call(), 0)
call_1851 = relay.TupleGetItem(func_1555_call(), 0)
output = relay.Tuple([call_1839,call_1850,])
output2 = relay.Tuple([call_1840,call_1851,])
func_1858 = relay.Function([], output)
mod['func_1858'] = func_1858
mod = relay.transform.InferType()(mod)
output = func_1858()
func_1859 = relay.Function([], output)
mutated_mod['func_1859'] = func_1859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1628_call = mod.get_global_var('func_1628')
func_1629_call = mutated_mod.get_global_var('func_1629')
call_1885 = relay.TupleGetItem(func_1628_call(), 1)
call_1886 = relay.TupleGetItem(func_1629_call(), 1)
output = call_1885
output2 = call_1886
func_1905 = relay.Function([], output)
mod['func_1905'] = func_1905
mod = relay.transform.InferType()(mod)
mutated_mod['func_1905'] = func_1905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1905_call = mutated_mod.get_global_var('func_1905')
call_1906 = func_1905_call()
output = call_1906
func_1907 = relay.Function([], output)
mutated_mod['func_1907'] = func_1907
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1908 = relay.var("var_1908", dtype = "float64", shape = (1, 16, 10))#candidate|1908|(1, 16, 10)|var|float64
var_1909 = relay.var("var_1909", dtype = "float64", shape = (10, 16, 10))#candidate|1909|(10, 16, 10)|var|float64
bop_1910 = relay.mod(var_1908.astype('float64'), var_1909.astype('float64')) # shape=(10, 16, 10)
var_1914 = relay.var("var_1914", dtype = "float64", shape = (10, 16, 10))#candidate|1914|(10, 16, 10)|var|float64
bop_1915 = relay.greater(var_1909.astype('bool'), relay.reshape(var_1914.astype('bool'), relay.shape_of(var_1909))) # shape=(10, 16, 10)
uop_1920 = relay.erf(bop_1915.astype('float64')) # shape=(10, 16, 10)
bop_1923 = relay.power(uop_1920.astype('float32'), relay.reshape(bop_1915.astype('float32'), relay.shape_of(uop_1920))) # shape=(10, 16, 10)
output = relay.Tuple([bop_1910,bop_1923,])
output2 = relay.Tuple([bop_1910,bop_1923,])
func_1940 = relay.Function([var_1908,var_1909,var_1914,], output)
mod['func_1940'] = func_1940
mod = relay.transform.InferType()(mod)
var_1941 = relay.var("var_1941", dtype = "float64", shape = (1, 16, 10))#candidate|1941|(1, 16, 10)|var|float64
var_1942 = relay.var("var_1942", dtype = "float64", shape = (10, 16, 10))#candidate|1942|(10, 16, 10)|var|float64
var_1943 = relay.var("var_1943", dtype = "float64", shape = (10, 16, 10))#candidate|1943|(10, 16, 10)|var|float64
output = func_1940(var_1941,var_1942,var_1943,)
func_1944 = relay.Function([var_1941,var_1942,var_1943,], output)
mutated_mod['func_1944'] = func_1944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1905_call = mod.get_global_var('func_1905')
func_1907_call = mutated_mod.get_global_var('func_1907')
call_2012 = func_1905_call()
call_2013 = func_1905_call()
output = relay.Tuple([call_2012,])
output2 = relay.Tuple([call_2013,])
func_2019 = relay.Function([], output)
mod['func_2019'] = func_2019
mod = relay.transform.InferType()(mod)
output = func_2019()
func_2020 = relay.Function([], output)
mutated_mod['func_2020'] = func_2020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1326_call = mod.get_global_var('func_1326')
func_1328_call = mutated_mod.get_global_var('func_1328')
call_2026 = relay.TupleGetItem(func_1326_call(), 0)
call_2027 = relay.TupleGetItem(func_1328_call(), 0)
output = relay.Tuple([call_2026,])
output2 = relay.Tuple([call_2027,])
func_2031 = relay.Function([], output)
mod['func_2031'] = func_2031
mod = relay.transform.InferType()(mod)
mutated_mod['func_2031'] = func_2031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2031_call = mutated_mod.get_global_var('func_2031')
call_2032 = func_2031_call()
output = call_2032
func_2033 = relay.Function([], output)
mutated_mod['func_2033'] = func_2033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2019_call = mod.get_global_var('func_2019')
func_2020_call = mutated_mod.get_global_var('func_2020')
call_2048 = relay.TupleGetItem(func_2019_call(), 0)
call_2049 = relay.TupleGetItem(func_2020_call(), 0)
var_2053 = relay.var("var_2053", dtype = "uint8", shape = (16, 13, 6))#candidate|2053|(16, 13, 6)|var|uint8
bop_2054 = relay.floor_divide(call_2048.astype('float64'), relay.reshape(var_2053.astype('float64'), relay.shape_of(call_2048))) # shape=(16, 13, 6)
bop_2057 = relay.floor_divide(call_2049.astype('float64'), relay.reshape(var_2053.astype('float64'), relay.shape_of(call_2049))) # shape=(16, 13, 6)
output = relay.Tuple([bop_2054,])
output2 = relay.Tuple([bop_2057,])
func_2064 = relay.Function([var_2053,], output)
mod['func_2064'] = func_2064
mod = relay.transform.InferType()(mod)
var_2065 = relay.var("var_2065", dtype = "uint8", shape = (16, 13, 6))#candidate|2065|(16, 13, 6)|var|uint8
output = func_2064(var_2065)
func_2066 = relay.Function([var_2065], output)
mutated_mod['func_2066'] = func_2066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2019_call = mod.get_global_var('func_2019')
func_2020_call = mutated_mod.get_global_var('func_2020')
call_2077 = relay.TupleGetItem(func_2019_call(), 0)
call_2078 = relay.TupleGetItem(func_2020_call(), 0)
output = call_2077
output2 = call_2078
func_2085 = relay.Function([], output)
mod['func_2085'] = func_2085
mod = relay.transform.InferType()(mod)
mutated_mod['func_2085'] = func_2085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2085_call = mutated_mod.get_global_var('func_2085')
call_2086 = func_2085_call()
output = call_2086
func_2087 = relay.Function([], output)
mutated_mod['func_2087'] = func_2087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1411_call = mod.get_global_var('func_1411')
func_1413_call = mutated_mod.get_global_var('func_1413')
call_2103 = func_1411_call()
call_2104 = func_1411_call()
output = call_2103
output2 = call_2104
func_2114 = relay.Function([], output)
mod['func_2114'] = func_2114
mod = relay.transform.InferType()(mod)
output = func_2114()
func_2115 = relay.Function([], output)
mutated_mod['func_2115'] = func_2115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1905_call = mod.get_global_var('func_1905')
func_1907_call = mutated_mod.get_global_var('func_1907')
call_2159 = func_1905_call()
call_2160 = func_1905_call()
output = call_2159
output2 = call_2160
func_2183 = relay.Function([], output)
mod['func_2183'] = func_2183
mod = relay.transform.InferType()(mod)
output = func_2183()
func_2184 = relay.Function([], output)
mutated_mod['func_2184'] = func_2184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1817_call = mod.get_global_var('func_1817')
func_1819_call = mutated_mod.get_global_var('func_1819')
call_2194 = func_1817_call()
call_2195 = func_1817_call()
output = relay.Tuple([call_2194,])
output2 = relay.Tuple([call_2195,])
func_2220 = relay.Function([], output)
mod['func_2220'] = func_2220
mod = relay.transform.InferType()(mod)
mutated_mod['func_2220'] = func_2220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2220_call = mutated_mod.get_global_var('func_2220')
call_2221 = func_2220_call()
output = call_2221
func_2222 = relay.Function([], output)
mutated_mod['func_2222'] = func_2222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1493_call = mod.get_global_var('func_1493')
func_1495_call = mutated_mod.get_global_var('func_1495')
call_2226 = relay.TupleGetItem(func_1493_call(), 0)
call_2227 = relay.TupleGetItem(func_1495_call(), 0)
output = relay.Tuple([call_2226,])
output2 = relay.Tuple([call_2227,])
func_2243 = relay.Function([], output)
mod['func_2243'] = func_2243
mod = relay.transform.InferType()(mod)
output = func_2243()
func_2244 = relay.Function([], output)
mutated_mod['func_2244'] = func_2244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1817_call = mod.get_global_var('func_1817')
func_1819_call = mutated_mod.get_global_var('func_1819')
call_2250 = func_1817_call()
call_2251 = func_1817_call()
func_1516_call = mod.get_global_var('func_1516')
func_1518_call = mutated_mod.get_global_var('func_1518')
call_2252 = func_1516_call()
call_2253 = func_1516_call()
func_1905_call = mod.get_global_var('func_1905')
func_1907_call = mutated_mod.get_global_var('func_1907')
call_2254 = func_1905_call()
call_2255 = func_1905_call()
func_1326_call = mod.get_global_var('func_1326')
func_1328_call = mutated_mod.get_global_var('func_1328')
call_2256 = relay.TupleGetItem(func_1326_call(), 0)
call_2257 = relay.TupleGetItem(func_1328_call(), 0)
output = relay.Tuple([call_2250,call_2252,call_2254,call_2256,])
output2 = relay.Tuple([call_2251,call_2253,call_2255,call_2257,])
func_2265 = relay.Function([], output)
mod['func_2265'] = func_2265
mod = relay.transform.InferType()(mod)
mutated_mod['func_2265'] = func_2265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2265_call = mutated_mod.get_global_var('func_2265')
call_2266 = func_2265_call()
output = call_2266
func_2267 = relay.Function([], output)
mutated_mod['func_2267'] = func_2267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2114_call = mod.get_global_var('func_2114')
func_2115_call = mutated_mod.get_global_var('func_2115')
call_2300 = func_2114_call()
call_2301 = func_2114_call()
output = call_2300
output2 = call_2301
func_2311 = relay.Function([], output)
mod['func_2311'] = func_2311
mod = relay.transform.InferType()(mod)
mutated_mod['func_2311'] = func_2311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2311_call = mutated_mod.get_global_var('func_2311')
call_2312 = func_2311_call()
output = call_2312
func_2313 = relay.Function([], output)
mutated_mod['func_2313'] = func_2313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1326_call = mod.get_global_var('func_1326')
func_1328_call = mutated_mod.get_global_var('func_1328')
call_2331 = relay.TupleGetItem(func_1326_call(), 0)
call_2332 = relay.TupleGetItem(func_1328_call(), 0)
func_2019_call = mod.get_global_var('func_2019')
func_2020_call = mutated_mod.get_global_var('func_2020')
call_2336 = relay.TupleGetItem(func_2019_call(), 0)
call_2337 = relay.TupleGetItem(func_2020_call(), 0)
output = relay.Tuple([call_2331,call_2336,])
output2 = relay.Tuple([call_2332,call_2337,])
func_2342 = relay.Function([], output)
mod['func_2342'] = func_2342
mod = relay.transform.InferType()(mod)
output = func_2342()
func_2343 = relay.Function([], output)
mutated_mod['func_2343'] = func_2343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1209_call = mod.get_global_var('func_1209')
func_1211_call = mutated_mod.get_global_var('func_1211')
call_2471 = relay.TupleGetItem(func_1209_call(), 0)
call_2472 = relay.TupleGetItem(func_1211_call(), 0)
output = call_2471
output2 = call_2472
func_2476 = relay.Function([], output)
mod['func_2476'] = func_2476
mod = relay.transform.InferType()(mod)
mutated_mod['func_2476'] = func_2476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2476_call = mutated_mod.get_global_var('func_2476')
call_2477 = func_2476_call()
output = call_2477
func_2478 = relay.Function([], output)
mutated_mod['func_2478'] = func_2478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1905_call = mod.get_global_var('func_1905')
func_1907_call = mutated_mod.get_global_var('func_1907')
call_2487 = func_1905_call()
call_2488 = func_1905_call()
func_112_call = mod.get_global_var('func_112')
func_115_call = mutated_mod.get_global_var('func_115')
call_2507 = relay.TupleGetItem(func_112_call(relay.reshape(call_2487.astype('int16'), [16, 13, 6]), relay.reshape(call_2487.astype('int16'), [16, 13, 6]), ), 0)
call_2508 = relay.TupleGetItem(func_115_call(relay.reshape(call_2487.astype('int16'), [16, 13, 6]), relay.reshape(call_2487.astype('int16'), [16, 13, 6]), ), 0)
uop_2519 = relay.sin(call_2487.astype('float32')) # shape=(16, 13, 6)
uop_2521 = relay.sin(call_2488.astype('float32')) # shape=(16, 13, 6)
func_2311_call = mod.get_global_var('func_2311')
func_2313_call = mutated_mod.get_global_var('func_2313')
call_2525 = func_2311_call()
call_2526 = func_2311_call()
output = relay.Tuple([call_2507,uop_2519,call_2525,])
output2 = relay.Tuple([call_2508,uop_2521,call_2526,])
func_2530 = relay.Function([], output)
mod['func_2530'] = func_2530
mod = relay.transform.InferType()(mod)
mutated_mod['func_2530'] = func_2530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2530_call = mutated_mod.get_global_var('func_2530')
call_2531 = func_2530_call()
output = call_2531
func_2532 = relay.Function([], output)
mutated_mod['func_2532'] = func_2532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2265_call = mod.get_global_var('func_2265')
func_2267_call = mutated_mod.get_global_var('func_2267')
call_2566 = relay.TupleGetItem(func_2265_call(), 2)
call_2567 = relay.TupleGetItem(func_2267_call(), 2)
func_1209_call = mod.get_global_var('func_1209')
func_1211_call = mutated_mod.get_global_var('func_1211')
call_2571 = relay.TupleGetItem(func_1209_call(), 0)
call_2572 = relay.TupleGetItem(func_1211_call(), 0)
output = relay.Tuple([call_2566,call_2571,])
output2 = relay.Tuple([call_2567,call_2572,])
func_2573 = relay.Function([], output)
mod['func_2573'] = func_2573
mod = relay.transform.InferType()(mod)
output = func_2573()
func_2574 = relay.Function([], output)
mutated_mod['func_2574'] = func_2574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2265_call = mod.get_global_var('func_2265')
func_2267_call = mutated_mod.get_global_var('func_2267')
call_2575 = relay.TupleGetItem(func_2265_call(), 2)
call_2576 = relay.TupleGetItem(func_2267_call(), 2)
output = call_2575
output2 = call_2576
func_2586 = relay.Function([], output)
mod['func_2586'] = func_2586
mod = relay.transform.InferType()(mod)
mutated_mod['func_2586'] = func_2586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2586_call = mutated_mod.get_global_var('func_2586')
call_2587 = func_2586_call()
output = call_2587
func_2588 = relay.Function([], output)
mutated_mod['func_2588'] = func_2588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1326_call = mod.get_global_var('func_1326')
func_1328_call = mutated_mod.get_global_var('func_1328')
call_2592 = relay.TupleGetItem(func_1326_call(), 0)
call_2593 = relay.TupleGetItem(func_1328_call(), 0)
func_1574_call = mod.get_global_var('func_1574')
func_1575_call = mutated_mod.get_global_var('func_1575')
call_2670 = relay.TupleGetItem(func_1574_call(), 1)
call_2671 = relay.TupleGetItem(func_1575_call(), 1)
func_2586_call = mod.get_global_var('func_2586')
func_2588_call = mutated_mod.get_global_var('func_2588')
call_2698 = func_2586_call()
call_2699 = func_2586_call()
var_2710 = relay.var("var_2710", dtype = "int16", shape = (16, 13, 6))#candidate|2710|(16, 13, 6)|var|int16
bop_2711 = relay.subtract(call_2670.astype('uint32'), relay.reshape(var_2710.astype('uint32'), relay.shape_of(call_2670))) # shape=(16, 13, 6)
bop_2714 = relay.subtract(call_2671.astype('uint32'), relay.reshape(var_2710.astype('uint32'), relay.shape_of(call_2671))) # shape=(16, 13, 6)
uop_2729 = relay.sigmoid(call_2698.astype('float32')) # shape=(16, 13, 6)
uop_2731 = relay.sigmoid(call_2699.astype('float32')) # shape=(16, 13, 6)
output = relay.Tuple([call_2592,bop_2711,uop_2729,])
output2 = relay.Tuple([call_2593,bop_2714,uop_2731,])
func_2734 = relay.Function([var_2710,], output)
mod['func_2734'] = func_2734
mod = relay.transform.InferType()(mod)
mutated_mod['func_2734'] = func_2734
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2735 = relay.var("var_2735", dtype = "int16", shape = (16, 13, 6))#candidate|2735|(16, 13, 6)|var|int16
func_2734_call = mutated_mod.get_global_var('func_2734')
call_2736 = func_2734_call(var_2735)
output = call_2736
func_2737 = relay.Function([var_2735], output)
mutated_mod['func_2737'] = func_2737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1526_call = mod.get_global_var('func_1526')
func_1527_call = mutated_mod.get_global_var('func_1527')
call_2742 = relay.TupleGetItem(func_1526_call(), 0)
call_2743 = relay.TupleGetItem(func_1527_call(), 0)
func_1411_call = mod.get_global_var('func_1411')
func_1413_call = mutated_mod.get_global_var('func_1413')
call_2746 = func_1411_call()
call_2747 = func_1411_call()
output = relay.Tuple([call_2742,call_2746,])
output2 = relay.Tuple([call_2743,call_2747,])
func_2756 = relay.Function([], output)
mod['func_2756'] = func_2756
mod = relay.transform.InferType()(mod)
output = func_2756()
func_2757 = relay.Function([], output)
mutated_mod['func_2757'] = func_2757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2114_call = mod.get_global_var('func_2114')
func_2115_call = mutated_mod.get_global_var('func_2115')
call_2821 = func_2114_call()
call_2822 = func_2114_call()
func_1326_call = mod.get_global_var('func_1326')
func_1328_call = mutated_mod.get_global_var('func_1328')
call_2831 = relay.TupleGetItem(func_1326_call(), 0)
call_2832 = relay.TupleGetItem(func_1328_call(), 0)
output = relay.Tuple([call_2821,call_2831,])
output2 = relay.Tuple([call_2822,call_2832,])
func_2833 = relay.Function([], output)
mod['func_2833'] = func_2833
mod = relay.transform.InferType()(mod)
output = func_2833()
func_2834 = relay.Function([], output)
mutated_mod['func_2834'] = func_2834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1411_call = mod.get_global_var('func_1411')
func_1413_call = mutated_mod.get_global_var('func_1413')
call_2856 = func_1411_call()
call_2857 = func_1411_call()
func_1209_call = mod.get_global_var('func_1209')
func_1211_call = mutated_mod.get_global_var('func_1211')
call_2884 = relay.TupleGetItem(func_1209_call(), 0)
call_2885 = relay.TupleGetItem(func_1211_call(), 0)
bop_2905 = relay.bitwise_or(call_2856.astype('uint16'), relay.reshape(call_2884.astype('uint16'), relay.shape_of(call_2856))) # shape=(1, 11, 3)
bop_2908 = relay.bitwise_or(call_2857.astype('uint16'), relay.reshape(call_2885.astype('uint16'), relay.shape_of(call_2857))) # shape=(1, 11, 3)
func_1516_call = mod.get_global_var('func_1516')
func_1518_call = mutated_mod.get_global_var('func_1518')
call_2920 = func_1516_call()
call_2921 = func_1516_call()
func_1574_call = mod.get_global_var('func_1574')
func_1575_call = mutated_mod.get_global_var('func_1575')
call_2929 = relay.TupleGetItem(func_1574_call(), 1)
call_2930 = relay.TupleGetItem(func_1575_call(), 1)
func_1493_call = mod.get_global_var('func_1493')
func_1495_call = mutated_mod.get_global_var('func_1495')
call_2931 = relay.TupleGetItem(func_1493_call(), 0)
call_2932 = relay.TupleGetItem(func_1495_call(), 0)
func_858_call = mod.get_global_var('func_858')
func_861_call = mutated_mod.get_global_var('func_861')
const_2936 = relay.const([[-10,-3,6],[-2,10,3],[-9,7,-1],[8,1,1],[10,-3,5],[-8,-4,-10],[4,-3,-8],[-8,-5,5],[-5,-9,-8],[4,-2,3],[-6,-4,3],[1,8,4],[2,2,-6],[3,-2,10],[5,-10,-10],[-6,-1,7],[4,3,-3],[7,8,-5],[8,6,2],[-10,9,-6],[2,-5,2],[-8,1,-8],[8,-2,-7],[-3,-6,-5],[-4,-5,-6],[1,-3,-2],[10,1,1],[8,7,8],[-8,10,-1],[-2,1,-7],[8,-6,4],[-6,-10,-6],[6,-2,5],[-6,-2,-8],[-1,-5,10],[3,10,1],[-9,-10,1],[8,9,10],[-2,8,-3],[7,9,-10],[4,6,-3],[9,3,-1],[-5,-4,10],[2,-10,-6],[-7,1,-4],[4,4,-5],[-9,1,6],[-6,2,7],[4,6,10],[-9,4,4],[2,-8,-7],[5,7,-6],[9,-4,-2],[5,-10,9],[2,8,1],[5,-7,-2],[-6,-10,5],[8,10,7],[2,-7,2],[6,-6,-9],[6,10,7],[-10,9,5],[-10,9,4],[-1,5,-3],[-5,-10,-3],[10,3,5],[-4,-2,-6],[8,-10,5],[3,2,-5],[-7,-4,-5],[-6,-6,-9],[-8,5,7],[-4,5,-1],[10,8,4],[-7,-8,-5],[-9,10,-9],[-6,1,6],[-3,2,-6],[10,-7,-10],[-2,1,9],[2,9,1],[10,-5,-9],[8,1,9],[1,5,-8],[10,-1,1],[-6,-6,-7],[-3,6,-8],[10,8,6],[-3,9,-6],[1,10,-8],[2,5,9],[8,-1,-3],[-1,6,8],[-9,10,7],[6,3,-1],[-6,-5,2],[-5,7,5],[6,4,-5],[4,3,3],[-10,-9,-2],[4,-3,1],[4,-6,-3],[-4,8,10],[10,9,-8],[3,-9,10],[5,3,4],[5,-1,10],[3,2,-2],[5,6,7],[-6,9,5],[9,5,9],[-8,-9,5],[-3,-5,-8],[-7,1,6],[-5,-10,-10],[-8,-4,10],[4,8,-9],[5,1,-8],[7,3,9],[7,4,2],[2,-2,3],[-2,2,-4],[-2,4,9],[2,7,7],[7,-10,9],[4,2,-10],[7,-3,1],[-9,-6,-4],[-5,4,-4],[-8,5,3],[-1,-7,-10],[-7,-8,-8],[-10,2,2],[-5,-4,8],[10,-2,-3],[-10,9,-7],[-6,-8,7],[-5,-2,6],[-3,-10,-10],[9,-4,6],[6,-2,-5],[8,5,8],[-1,-10,-10],[-9,-7,-1],[7,8,3],[-9,-10,-5],[-3,-8,8],[-10,-1,-4],[-9,5,1],[-3,-8,-10],[-5,-9,3],[3,5,-2],[-9,2,7],[10,-10,-3],[1,-9,-9],[9,7,10],[-1,6,4],[1,-4,-3],[10,8,8],[-10,9,9],[8,1,-5],[-7,-2,4],[-3,-9,-9],[-10,6,10],[-9,-3,2],[4,10,-7],[-6,3,9],[6,-4,1],[-7,-6,-6],[9,9,-4],[5,-10,5],[2,-2,-9],[-4,-3,2],[-4,4,4],[-8,-5,-4],[-7,9,4],[5,-3,-10],[-9,1,-5],[-7,-2,10],[-1,8,5],[-7,2,10],[-9,-3,5],[7,10,-8],[-1,-3,-6],[-8,1,-2],[-1,-1,-6],[1,7,8],[-7,-5,-2],[-9,8,7],[-7,10,2],[-8,-3,-6],[-9,2,8],[7,-6,-2],[5,-3,-5],[6,3,4],[10,-8,9],[3,10,-6],[-7,4,7],[-2,-9,-7],[3,-10,1],[-4,6,-7],[-8,4,8],[-6,3,10],[8,-2,7],[3,5,10],[7,-9,8],[9,8,3],[3,3,-1],[-6,7,8],[-9,7,4],[10,-1,-4],[6,-6,7],[10,-1,6],[8,-3,-3],[-10,-1,6],[2,9,-6],[-4,-6,-5],[-2,-5,-10],[6,-4,-4],[1,-9,8],[-10,-1,6],[1,8,-10],[2,-9,-4],[-7,-8,1],[-10,-5,7],[-2,8,5],[1,-3,3],[3,7,4],[3,-4,-6],[7,9,3],[-7,-4,-10],[-10,5,1],[9,7,6],[-7,-5,-3],[6,-5,2],[-3,-6,-6],[8,-9,-9],[2,4,2],[-3,10,8],[6,-3,-10],[-10,-4,2],[5,3,-4],[4,-8,7],[10,-1,-5],[6,-4,4],[-2,9,-1],[3,2,9],[8,-3,-4],[10,-10,6],[9,-9,-9],[-7,5,6],[-8,3,-6],[-5,6,5],[-8,-5,6],[-4,-3,8],[-5,-2,2],[8,6,-1],[2,9,5],[1,10,4],[7,-1,-2],[-2,-5,-7],[2,-8,-5],[-3,8,-8],[-7,-8,4],[3,1,-4],[10,-8,-10],[-3,-10,-1],[1,-3,-7],[3,1,10],[-3,-1,-4],[7,-10,-10],[-8,5,3],[3,1,2],[1,9,-9],[9,2,6],[2,-2,8],[5,5,4],[-5,2,6],[-1,1,7],[10,2,6],[10,3,2],[-3,7,-6],[-6,9,6],[-3,-2,-8],[-4,7,-4],[8,-10,-5],[-2,9,6],[2,6,-1],[-9,-9,9],[-10,-10,3],[-9,-8,-9],[1,-3,1],[-8,3,-6],[-8,1,4],[7,-4,-2],[-2,7,-9],[-5,10,-5],[-9,-5,8],[-9,4,4],[-1,-3,-1],[-4,-5,-3],[1,-7,5],[-3,-6,9],[2,8,9],[8,-4,-6],[6,-8,-1],[5,8,-5],[5,-9,10],[5,-9,10],[7,-7,8],[8,3,3],[6,8,-2],[-8,10,-10],[-7,-2,9],[4,9,9],[-7,1,10],[4,4,9],[-4,6,4],[4,-2,8],[10,9,3],[7,4,10],[4,9,7],[-5,-7,-4],[-9,-10,5],[-4,10,-4],[-1,5,-1],[-9,-10,-2],[-10,-5,-7],[6,9,5],[-6,9,-2],[10,-6,-9],[3,-1,-8],[-7,7,5],[-3,10,-7],[-6,-5,10],[1,-1,9],[5,7,3],[8,-6,-6],[-1,-10,-10],[5,3,-4],[7,4,-2],[7,-5,5],[4,9,-10],[-10,5,9],[10,-3,6],[-5,3,-1],[2,-4,6],[6,5,-9],[2,4,-1],[3,9,-6],[5,7,1],[-5,-8,4],[10,-4,-5],[8,6,7],[6,-1,-7],[-1,-8,-8],[-6,4,4],[8,7,-9],[-6,-2,-10],[10,-8,-3],[7,5,2],[-4,8,4],[5,-6,-5],[5,-1,-4],[5,-8,-6],[-5,-5,-8],[-4,9,2],[4,5,-10],[-4,-4,3],[5,-3,-8],[-4,-1,3],[-9,-4,9],[-2,-3,-2],[9,-9,10],[-10,-7,-7],[-9,-8,-1],[-4,8,-7],[-3,-1,-7],[-9,-10,7],[8,4,-8],[2,2,-2],[1,-3,3],[9,10,2],[4,4,-10],[3,-10,-5],[7,-8,7],[4,-7,10],[-9,-5,10],[8,1,-9],[5,-2,8],[3,-7,4],[4,-6,5],[10,7,-4],[-7,1,6],[-10,2,6],[-1,5,2],[4,7,7],[-7,9,2],[-9,8,6],[1,-7,-2],[-3,1,-3],[-7,-1,8],[-10,2,-7],[3,-5,7],[6,-1,-1],[5,-6,-1],[-3,5,-5],[-9,5,4],[-8,-9,9],[4,6,-8],[8,2,-2],[-10,-3,7],[7,-5,-7],[-6,6,-8],[3,-10,-7],[7,-4,9],[4,-2,-4],[9,7,4],[2,9,-5],[-5,-8,9],[-5,-3,5],[-8,-1,10],[-9,7,-2],[10,-10,2],[-5,-6,-3],[-10,-1,-1],[7,7,-8],[-5,3,-5],[-2,-9,-5],[10,1,6],[-10,4,1],[8,-5,-6],[-2,-1,3],[-2,-2,-9],[-3,8,-6],[-7,1,8],[9,10,2],[4,-6,-3],[-1,-4,-5],[10,6,3],[4,-8,3],[7,-3,5],[-4,1,6],[-9,-6,-1],[-7,-2,-1],[-5,-9,10],[-1,4,-5],[-9,-8,8],[-4,-10,-9],[-3,2,-1],[4,-7,-9],[5,-5,3],[-7,-8,-5],[-8,1,-9],[-1,-9,10]], dtype = "uint8")#candidate|2936|(455, 3)|const|uint8
call_2935 = relay.TupleGetItem(func_858_call(relay.reshape(const_2936.astype('uint8'), [13, 7, 15])), 6)
call_2937 = relay.TupleGetItem(func_861_call(relay.reshape(const_2936.astype('uint8'), [13, 7, 15])), 6)
output = relay.Tuple([bop_2905,call_2920,call_2929,call_2931,call_2935,const_2936,])
output2 = relay.Tuple([bop_2908,call_2921,call_2930,call_2932,call_2937,const_2936,])
func_2955 = relay.Function([], output)
mod['func_2955'] = func_2955
mod = relay.transform.InferType()(mod)
mutated_mod['func_2955'] = func_2955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2955_call = mutated_mod.get_global_var('func_2955')
call_2956 = func_2955_call()
output = call_2956
func_2957 = relay.Function([], output)
mutated_mod['func_2957'] = func_2957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2311_call = mod.get_global_var('func_2311')
func_2313_call = mutated_mod.get_global_var('func_2313')
call_2966 = func_2311_call()
call_2967 = func_2311_call()
output = call_2966
output2 = call_2967
func_2968 = relay.Function([], output)
mod['func_2968'] = func_2968
mod = relay.transform.InferType()(mod)
mutated_mod['func_2968'] = func_2968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2968_call = mutated_mod.get_global_var('func_2968')
call_2969 = func_2968_call()
output = call_2969
func_2970 = relay.Function([], output)
mutated_mod['func_2970'] = func_2970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1858_call = mod.get_global_var('func_1858')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_3007 = relay.TupleGetItem(func_1858_call(), 1)
call_3008 = relay.TupleGetItem(func_1859_call(), 1)
func_2243_call = mod.get_global_var('func_2243')
func_2244_call = mutated_mod.get_global_var('func_2244')
call_3009 = relay.TupleGetItem(func_2243_call(), 0)
call_3010 = relay.TupleGetItem(func_2244_call(), 0)
output = relay.Tuple([call_3007,call_3009,])
output2 = relay.Tuple([call_3008,call_3010,])
func_3016 = relay.Function([], output)
mod['func_3016'] = func_3016
mod = relay.transform.InferType()(mod)
mutated_mod['func_3016'] = func_3016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3016_call = mutated_mod.get_global_var('func_3016')
call_3017 = func_3016_call()
output = call_3017
func_3018 = relay.Function([], output)
mutated_mod['func_3018'] = func_3018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2586_call = mod.get_global_var('func_2586')
func_2588_call = mutated_mod.get_global_var('func_2588')
call_3103 = func_2586_call()
call_3104 = func_2586_call()
output = call_3103
output2 = call_3104
func_3105 = relay.Function([], output)
mod['func_3105'] = func_3105
mod = relay.transform.InferType()(mod)
mutated_mod['func_3105'] = func_3105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3105_call = mutated_mod.get_global_var('func_3105')
call_3106 = func_3105_call()
output = call_3106
func_3107 = relay.Function([], output)
mutated_mod['func_3107'] = func_3107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1817_call = mod.get_global_var('func_1817')
func_1819_call = mutated_mod.get_global_var('func_1819')
call_3153 = func_1817_call()
call_3154 = func_1817_call()
output = call_3153
output2 = call_3154
func_3163 = relay.Function([], output)
mod['func_3163'] = func_3163
mod = relay.transform.InferType()(mod)
output = func_3163()
func_3164 = relay.Function([], output)
mutated_mod['func_3164'] = func_3164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1411_call = mod.get_global_var('func_1411')
func_1413_call = mutated_mod.get_global_var('func_1413')
call_3210 = func_1411_call()
call_3211 = func_1411_call()
func_2756_call = mod.get_global_var('func_2756')
func_2757_call = mutated_mod.get_global_var('func_2757')
call_3220 = relay.TupleGetItem(func_2756_call(), 1)
call_3221 = relay.TupleGetItem(func_2757_call(), 1)
bop_3226 = relay.right_shift(call_3220.astype('uint8'), relay.reshape(call_3210.astype('uint8'), relay.shape_of(call_3220))) # shape=(1, 11, 3)
bop_3229 = relay.right_shift(call_3221.astype('uint8'), relay.reshape(call_3211.astype('uint8'), relay.shape_of(call_3221))) # shape=(1, 11, 3)
output = bop_3226
output2 = bop_3229
func_3237 = relay.Function([], output)
mod['func_3237'] = func_3237
mod = relay.transform.InferType()(mod)
output = func_3237()
func_3238 = relay.Function([], output)
mutated_mod['func_3238'] = func_3238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2114_call = mod.get_global_var('func_2114')
func_2115_call = mutated_mod.get_global_var('func_2115')
call_3276 = func_2114_call()
call_3277 = func_2114_call()
output = call_3276
output2 = call_3277
func_3288 = relay.Function([], output)
mod['func_3288'] = func_3288
mod = relay.transform.InferType()(mod)
output = func_3288()
func_3289 = relay.Function([], output)
mutated_mod['func_3289'] = func_3289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3016_call = mod.get_global_var('func_3016')
func_3018_call = mutated_mod.get_global_var('func_3018')
call_3298 = relay.TupleGetItem(func_3016_call(), 1)
call_3299 = relay.TupleGetItem(func_3018_call(), 1)
func_1905_call = mod.get_global_var('func_1905')
func_1907_call = mutated_mod.get_global_var('func_1907')
call_3317 = func_1905_call()
call_3318 = func_1905_call()
func_60_call = mod.get_global_var('func_60')
func_64_call = mutated_mod.get_global_var('func_64')
var_3330 = relay.var("var_3330", dtype = "uint8", shape = (864,))#candidate|3330|(864,)|var|uint8
call_3329 = relay.TupleGetItem(func_60_call(relay.reshape(var_3330.astype('uint8'), [6, 9, 16]), relay.reshape(var_3330.astype('uint8'), [6, 9, 16]), ), 0)
call_3331 = relay.TupleGetItem(func_64_call(relay.reshape(var_3330.astype('uint8'), [6, 9, 16]), relay.reshape(var_3330.astype('uint8'), [6, 9, 16]), ), 0)
func_3105_call = mod.get_global_var('func_3105')
func_3107_call = mutated_mod.get_global_var('func_3107')
call_3334 = func_3105_call()
call_3335 = func_3105_call()
func_1905_call = mod.get_global_var('func_1905')
func_1907_call = mutated_mod.get_global_var('func_1907')
call_3345 = func_1905_call()
call_3346 = func_1905_call()
output = relay.Tuple([call_3298,call_3317,call_3329,var_3330,call_3334,call_3345,])
output2 = relay.Tuple([call_3299,call_3318,call_3331,var_3330,call_3335,call_3346,])
func_3361 = relay.Function([var_3330,], output)
mod['func_3361'] = func_3361
mod = relay.transform.InferType()(mod)
var_3362 = relay.var("var_3362", dtype = "uint8", shape = (864,))#candidate|3362|(864,)|var|uint8
output = func_3361(var_3362)
func_3363 = relay.Function([var_3362], output)
mutated_mod['func_3363'] = func_3363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1574_call = mod.get_global_var('func_1574')
func_1575_call = mutated_mod.get_global_var('func_1575')
call_3365 = relay.TupleGetItem(func_1574_call(), 0)
call_3366 = relay.TupleGetItem(func_1575_call(), 0)
output = relay.Tuple([call_3365,])
output2 = relay.Tuple([call_3366,])
func_3379 = relay.Function([], output)
mod['func_3379'] = func_3379
mod = relay.transform.InferType()(mod)
output = func_3379()
func_3380 = relay.Function([], output)
mutated_mod['func_3380'] = func_3380
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3433 = relay.var("var_3433", dtype = "int32", shape = ())#candidate|3433|()|var|int32
const_3434 = relay.const([[[-1,-4,3,5,10,-8,-6,10],[10,9,-4,-1,-4,-9,-7,7],[-5,-2,9,-8,9,-9,-6,-8],[-5,-4,6,5,2,-9,1,9],[-4,-4,10,3,7,4,-3,8],[3,-6,-7,-1,6,-10,-3,-5],[-1,2,-3,1,-9,3,-7,-1],[-3,9,9,-3,-9,4,-1,1]],[[-7,3,7,10,-9,7,4,-6],[4,-8,-7,-8,3,10,-10,-8],[-5,-9,-3,10,1,-7,5,1],[1,4,10,6,-5,-9,-9,-6],[-8,-9,-3,4,-6,9,6,-3],[-1,7,-3,7,9,-5,-5,-3],[7,3,-10,-5,7,8,-6,-10],[-9,10,-8,-10,-5,7,9,2]],[[-3,7,1,10,8,1,8,-2],[-8,1,-9,5,7,3,-2,-1],[9,8,9,-8,-5,-2,-10,-2],[-7,6,-3,2,-3,-3,2,-9],[1,3,-5,-1,-9,3,-9,10],[7,4,7,9,2,4,-7,7],[10,10,-10,-6,-3,-2,6,-8],[8,-7,7,4,10,-3,10,-5]],[[-9,-8,5,10,4,10,-4,7],[10,8,9,-7,1,-4,-10,-3],[-3,6,4,-5,7,-10,-6,2],[10,3,1,6,10,3,10,-8],[5,-2,1,-7,5,-7,6,-8],[9,-4,3,-2,-2,4,-3,7],[-8,8,6,-8,-5,-3,6,5],[-3,6,1,-9,-5,6,-5,7]],[[-2,3,-10,-9,7,6,-3,9],[-4,-10,-4,-9,-9,-8,-8,8],[-10,7,3,7,-8,-3,5,-5],[-8,-3,3,3,7,-8,6,4],[-8,-6,-7,-3,5,5,10,1],[6,-10,8,-3,-3,-1,-9,-5],[-5,10,-5,8,8,3,5,6],[8,2,-7,2,-8,-1,9,3]],[[-10,-8,3,4,-9,-1,-1,-8],[3,6,7,-2,-2,-1,10,4],[5,4,8,-1,-6,-1,-9,7],[-1,4,2,2,-8,4,-6,-7],[-2,9,10,7,4,3,9,7],[-3,-9,-6,1,-3,-3,5,8],[-2,9,8,-6,-8,-6,-6,-8],[-6,6,-7,8,-1,-6,3,-6]],[[-4,-5,-3,-5,-1,-9,-5,-8],[3,3,-10,-9,-1,9,-1,-9],[2,-7,6,-7,4,3,-4,-2],[-4,6,-7,-5,1,4,-9,-7],[8,7,8,10,1,-3,6,-1],[-10,6,-3,6,5,6,-1,-6],[-8,3,-10,-8,-10,-7,6,-9],[-6,-2,8,-2,5,8,10,-7]],[[10,4,4,-10,-5,-1,4,5],[-4,8,4,4,8,7,7,-6],[-5,6,6,-4,-2,2,-6,7],[-6,4,7,-1,-4,-2,-2,10],[1,-7,-4,10,9,-4,-10,6],[8,-10,-2,7,-7,6,9,9],[2,9,-8,-3,-10,1,-10,10],[9,-10,-8,6,7,-7,8,6]],[[-1,-7,3,-5,9,-5,-4,-6],[4,3,-2,-9,9,-3,3,8],[-6,2,-4,-2,-4,-1,-1,-1],[-2,7,3,5,2,-8,9,9],[-10,-3,-2,9,-2,-2,9,10],[-8,-7,2,3,-10,-9,9,-4],[-2,5,-4,10,7,10,7,-5],[-6,-6,-4,2,-1,3,-10,-1]],[[4,6,10,-5,-10,-3,7,-10],[10,-1,4,-8,-6,-5,8,1],[-1,1,5,-10,-2,-1,-9,-4],[-6,5,10,-5,2,3,5,1],[4,-7,9,3,-10,-2,5,10],[-1,-3,8,-7,9,10,5,10],[-7,-8,8,-8,6,-7,-6,-4],[2,9,-7,-2,-6,2,6,-9]],[[-3,-9,-10,7,-9,-9,-1,-3],[10,5,-6,-6,9,-4,-10,-8],[-1,3,-4,-7,5,7,7,-1],[1,8,2,10,2,8,6,-6],[-3,-8,7,1,9,10,-9,7],[-6,7,-9,-1,10,2,7,7],[-6,8,-10,7,-8,-7,5,-9],[9,1,5,-6,3,-5,7,-2]],[[-6,-6,1,8,-8,8,-9,6],[-5,5,-1,8,-2,-6,-4,-9],[9,7,-9,-9,9,10,-6,-7],[3,2,-6,8,3,6,2,-8],[-3,1,7,6,-9,6,-3,8],[-9,-8,3,3,-1,1,-4,-6],[-3,6,-9,8,1,7,10,-7],[-8,-2,-2,6,3,9,-8,4]],[[-4,-3,-5,4,8,-9,9,-5],[-3,-7,-3,-2,-4,-4,8,4],[-2,-8,2,4,-5,6,1,10],[-10,10,-2,10,5,-8,5,8],[3,-4,-8,-2,-9,7,-2,3],[4,5,-8,-1,8,8,3,1],[-2,10,-1,-4,-1,-10,8,4],[1,-7,2,-3,-1,-6,-9,-10]],[[-1,-2,3,3,-9,-6,8,-10],[-9,9,-6,6,3,4,10,-4],[4,-3,4,-2,9,-1,-8,-8],[-9,-10,9,-4,9,-6,-2,10],[-6,5,-7,4,-5,-4,9,1],[9,3,-9,-10,-3,-5,-7,-10],[-6,-5,-2,-10,8,-1,6,-3],[5,-2,-2,-3,1,9,3,-2]],[[-6,5,-6,4,-8,8,-1,10],[-6,-2,-9,5,-3,9,-4,8],[-6,8,7,-3,-9,1,-4,7],[5,8,2,-5,8,4,5,-3],[-6,-2,-5,10,-7,-5,1,-1],[-1,4,4,10,-3,5,-8,-8],[9,7,-6,1,5,-6,-8,-7],[-8,2,-10,4,-9,-1,7,-1]]], dtype = "int32")#candidate|3434|(15, 8, 8)|const|int32
bop_3435 = relay.left_shift(var_3433.astype('int32'), const_3434.astype('int32')) # shape=(15, 8, 8)
output = bop_3435
output2 = bop_3435
func_3439 = relay.Function([var_3433,], output)
mod['func_3439'] = func_3439
mod = relay.transform.InferType()(mod)
var_3440 = relay.var("var_3440", dtype = "int32", shape = ())#candidate|3440|()|var|int32
output = func_3439(var_3440)
func_3441 = relay.Function([var_3440], output)
mutated_mod['func_3441'] = func_3441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1493_call = mod.get_global_var('func_1493')
func_1495_call = mutated_mod.get_global_var('func_1495')
call_3468 = relay.TupleGetItem(func_1493_call(), 0)
call_3469 = relay.TupleGetItem(func_1495_call(), 0)
output = relay.Tuple([call_3468,])
output2 = relay.Tuple([call_3469,])
func_3504 = relay.Function([], output)
mod['func_3504'] = func_3504
mod = relay.transform.InferType()(mod)
mutated_mod['func_3504'] = func_3504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3504_call = mutated_mod.get_global_var('func_3504')
call_3505 = func_3504_call()
output = call_3505
func_3506 = relay.Function([], output)
mutated_mod['func_3506'] = func_3506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2085_call = mod.get_global_var('func_2085')
func_2087_call = mutated_mod.get_global_var('func_2087')
call_3549 = func_2085_call()
call_3550 = func_2085_call()
output = relay.Tuple([call_3549,])
output2 = relay.Tuple([call_3550,])
func_3554 = relay.Function([], output)
mod['func_3554'] = func_3554
mod = relay.transform.InferType()(mod)
mutated_mod['func_3554'] = func_3554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3554_call = mutated_mod.get_global_var('func_3554')
call_3555 = func_3554_call()
output = call_3555
func_3556 = relay.Function([], output)
mutated_mod['func_3556'] = func_3556
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2573_call = mod.get_global_var('func_2573')
func_2574_call = mutated_mod.get_global_var('func_2574')
call_3641 = relay.TupleGetItem(func_2573_call(), 1)
call_3642 = relay.TupleGetItem(func_2574_call(), 1)
output = call_3641
output2 = call_3642
func_3686 = relay.Function([], output)
mod['func_3686'] = func_3686
mod = relay.transform.InferType()(mod)
output = func_3686()
func_3687 = relay.Function([], output)
mutated_mod['func_3687'] = func_3687
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3700 = relay.var("var_3700", dtype = "float64", shape = (5, 5, 7))#candidate|3700|(5, 5, 7)|var|float64
uop_3701 = relay.sin(var_3700.astype('float64')) # shape=(5, 5, 7)
output = relay.Tuple([uop_3701,])
output2 = relay.Tuple([uop_3701,])
func_3712 = relay.Function([var_3700,], output)
mod['func_3712'] = func_3712
mod = relay.transform.InferType()(mod)
mutated_mod['func_3712'] = func_3712
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3713 = relay.var("var_3713", dtype = "float64", shape = (5, 5, 7))#candidate|3713|(5, 5, 7)|var|float64
func_3712_call = mutated_mod.get_global_var('func_3712')
call_3714 = func_3712_call(var_3713)
output = call_3714
func_3715 = relay.Function([var_3713], output)
mutated_mod['func_3715'] = func_3715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3554_call = mod.get_global_var('func_3554')
func_3556_call = mutated_mod.get_global_var('func_3556')
call_3729 = relay.TupleGetItem(func_3554_call(), 0)
call_3730 = relay.TupleGetItem(func_3556_call(), 0)
func_3016_call = mod.get_global_var('func_3016')
func_3018_call = mutated_mod.get_global_var('func_3018')
call_3737 = relay.TupleGetItem(func_3016_call(), 1)
call_3738 = relay.TupleGetItem(func_3018_call(), 1)
var_3744 = relay.var("var_3744", dtype = "uint8", shape = (16, 13, 6))#candidate|3744|(16, 13, 6)|var|uint8
bop_3745 = relay.left_shift(call_3729.astype('uint32'), relay.reshape(var_3744.astype('uint32'), relay.shape_of(call_3729))) # shape=(16, 13, 6)
bop_3748 = relay.left_shift(call_3730.astype('uint32'), relay.reshape(var_3744.astype('uint32'), relay.shape_of(call_3730))) # shape=(16, 13, 6)
output = relay.Tuple([call_3737,bop_3745,])
output2 = relay.Tuple([call_3738,bop_3748,])
func_3753 = relay.Function([var_3744,], output)
mod['func_3753'] = func_3753
mod = relay.transform.InferType()(mod)
var_3754 = relay.var("var_3754", dtype = "uint8", shape = (16, 13, 6))#candidate|3754|(16, 13, 6)|var|uint8
output = func_3753(var_3754)
func_3755 = relay.Function([var_3754], output)
mutated_mod['func_3755'] = func_3755
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3765 = relay.var("var_3765", dtype = "uint64", shape = (6, 6, 5))#candidate|3765|(6, 6, 5)|var|uint64
const_3766 = relay.const([[[3,-7,2,-5,5],[-8,1,1,9,9],[-1,-4,-6,1,-6],[-1,-4,1,10,-3],[-7,-1,10,-6,-4],[-8,-8,5,5,-3]],[[8,10,-2,10,-7],[8,-5,-4,-5,-5],[-7,-1,5,10,-5],[-1,-5,-4,1,1],[-6,-4,8,-5,8],[1,3,2,-9,10]],[[-3,4,1,7,4],[10,8,1,1,8],[-6,-9,-10,-8,3],[-2,10,-6,-6,1],[-4,-7,6,-8,-4],[10,-5,10,8,-6]],[[-8,9,4,9,2],[-7,-2,9,-4,6],[-3,-9,-3,-8,1],[-4,-10,-6,-10,-4],[4,9,8,5,4],[2,-8,-10,4,-4]],[[9,3,-2,-6,6],[5,1,-8,-3,-3],[-4,6,7,-3,-1],[-5,4,4,9,-10],[-1,-4,10,-3,5],[-10,10,1,2,-2]],[[10,5,-7,1,2],[10,-6,-6,-6,-9],[-5,-2,-7,-6,-6],[1,-6,-1,9,7],[-3,3,-1,8,-7],[10,8,-9,-4,1]]], dtype = "uint64")#candidate|3766|(6, 6, 5)|const|uint64
bop_3767 = relay.multiply(var_3765.astype('uint64'), relay.reshape(const_3766.astype('uint64'), relay.shape_of(var_3765))) # shape=(6, 6, 5)
func_1396_call = mod.get_global_var('func_1396')
func_1398_call = mutated_mod.get_global_var('func_1398')
var_3794 = relay.var("var_3794", dtype = "float32", shape = (208,))#candidate|3794|(208,)|var|float32
call_3793 = relay.TupleGetItem(func_1396_call(relay.reshape(var_3794.astype('float32'), [104, 2])), 4)
call_3795 = relay.TupleGetItem(func_1398_call(relay.reshape(var_3794.astype('float32'), [104, 2])), 4)
uop_3796 = relay.log2(call_3793.astype('float32')) # shape=(104, 2)
uop_3798 = relay.log2(call_3795.astype('float32')) # shape=(104, 2)
bop_3799 = relay.logical_xor(uop_3796.astype('uint8'), relay.reshape(var_3794.astype('uint8'), relay.shape_of(uop_3796))) # shape=(104, 2)
bop_3802 = relay.logical_xor(uop_3798.astype('uint8'), relay.reshape(var_3794.astype('uint8'), relay.shape_of(uop_3798))) # shape=(104, 2)
func_3361_call = mod.get_global_var('func_3361')
func_3363_call = mutated_mod.get_global_var('func_3363')
var_3821 = relay.var("var_3821", dtype = "uint8", shape = (1, 864))#candidate|3821|(1, 864)|var|uint8
call_3820 = relay.TupleGetItem(func_3361_call(relay.reshape(var_3821.astype('uint8'), [864,])), 5)
call_3822 = relay.TupleGetItem(func_3363_call(relay.reshape(var_3821.astype('uint8'), [864,])), 5)
output = relay.Tuple([bop_3767,bop_3799,call_3820,var_3821,])
output2 = relay.Tuple([bop_3767,bop_3802,call_3822,var_3821,])
func_3828 = relay.Function([var_3765,var_3794,var_3821,], output)
mod['func_3828'] = func_3828
mod = relay.transform.InferType()(mod)
mutated_mod['func_3828'] = func_3828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3828_call = mutated_mod.get_global_var('func_3828')
var_3830 = relay.var("var_3830", dtype = "uint64", shape = (6, 6, 5))#candidate|3830|(6, 6, 5)|var|uint64
var_3831 = relay.var("var_3831", dtype = "float32", shape = (208,))#candidate|3831|(208,)|var|float32
var_3832 = relay.var("var_3832", dtype = "uint8", shape = (1, 864))#candidate|3832|(1, 864)|var|uint8
call_3829 = func_3828_call(var_3830,var_3831,var_3832,)
output = call_3829
func_3833 = relay.Function([var_3830,var_3831,var_3832,], output)
mutated_mod['func_3833'] = func_3833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1411_call = mod.get_global_var('func_1411')
func_1413_call = mutated_mod.get_global_var('func_1413')
call_3907 = func_1411_call()
call_3908 = func_1411_call()
output = relay.Tuple([call_3907,])
output2 = relay.Tuple([call_3908,])
func_3909 = relay.Function([], output)
mod['func_3909'] = func_3909
mod = relay.transform.InferType()(mod)
mutated_mod['func_3909'] = func_3909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3909_call = mutated_mod.get_global_var('func_3909')
call_3910 = func_3909_call()
output = call_3910
func_3911 = relay.Function([], output)
mutated_mod['func_3911'] = func_3911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2085_call = mod.get_global_var('func_2085')
func_2087_call = mutated_mod.get_global_var('func_2087')
call_3919 = func_2085_call()
call_3920 = func_2085_call()
func_60_call = mod.get_global_var('func_60')
func_64_call = mutated_mod.get_global_var('func_64')
var_3954 = relay.var("var_3954", dtype = "uint8", shape = (864,))#candidate|3954|(864,)|var|uint8
call_3953 = relay.TupleGetItem(func_60_call(relay.reshape(var_3954.astype('uint8'), [6, 9, 16]), relay.reshape(var_3954.astype('uint8'), [6, 9, 16]), ), 0)
call_3955 = relay.TupleGetItem(func_64_call(relay.reshape(var_3954.astype('uint8'), [6, 9, 16]), relay.reshape(var_3954.astype('uint8'), [6, 9, 16]), ), 0)
uop_3957 = relay.acos(var_3954.astype('float64')) # shape=(864,)
func_2530_call = mod.get_global_var('func_2530')
func_2532_call = mutated_mod.get_global_var('func_2532')
call_3963 = relay.TupleGetItem(func_2530_call(), 2)
call_3964 = relay.TupleGetItem(func_2532_call(), 2)
output = relay.Tuple([call_3919,call_3953,uop_3957,call_3963,])
output2 = relay.Tuple([call_3920,call_3955,uop_3957,call_3964,])
func_3992 = relay.Function([var_3954,], output)
mod['func_3992'] = func_3992
mod = relay.transform.InferType()(mod)
var_3993 = relay.var("var_3993", dtype = "uint8", shape = (864,))#candidate|3993|(864,)|var|uint8
output = func_3992(var_3993)
func_3994 = relay.Function([var_3993], output)
mutated_mod['func_3994'] = func_3994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1209_call = mod.get_global_var('func_1209')
func_1211_call = mutated_mod.get_global_var('func_1211')
call_4024 = relay.TupleGetItem(func_1209_call(), 0)
call_4025 = relay.TupleGetItem(func_1211_call(), 0)
func_3909_call = mod.get_global_var('func_3909')
func_3911_call = mutated_mod.get_global_var('func_3911')
call_4038 = relay.TupleGetItem(func_3909_call(), 0)
call_4039 = relay.TupleGetItem(func_3911_call(), 0)
func_961_call = mod.get_global_var('func_961')
func_964_call = mutated_mod.get_global_var('func_964')
const_4044 = relay.const([3.508708,0.429201,9.103614,-8.299102,7.933195,3.467556,5.493490,-7.519177,1.593641,0.686314,-7.921217,1.871571,-9.665842,8.176246,1.146305,-3.771623,3.304080,-9.411602,-4.244896,-8.514517,-1.442369,5.189325,-8.381094,-0.334528,-8.213883,0.041163,-3.875594,-1.313763,-5.210904,-0.367587,7.825717,6.607810,-8.841436,-1.103329,-9.890645,-9.930315,-0.078846,-3.328613,8.180608,-5.947296,6.059760,7.239203,-9.340622,-2.112215,9.578082,5.989801,0.965352,-5.663890,-7.247624,9.959484,4.043356,4.760329,9.871330,-5.288770,5.767546,-6.609689,-5.444234,-8.272032,-6.375251,-2.336172,8.381358,-7.333586,-6.647906,5.842580,3.162453,6.757337,-4.613882,8.492641,4.580882,6.715591,-2.804593,7.973109,4.801757,-8.393877,-6.555593,3.516610,-2.589341,8.815962,-1.143017,8.530182,2.425456,-1.251298,1.254075,0.729533,-4.997402,6.734323,-6.546433,3.087893,-8.000246,8.608042,-3.567612,5.362217,0.191018,0.256093,9.879447,5.302954,-5.297121,-6.356587,4.717738,-9.347863,-3.635897,4.506371,-0.433960,-1.776707,-3.987510,3.878048,9.261514,8.634545,4.386173,-8.201493,2.028860,2.565816,-3.667726,1.912718,9.908494,8.956011,-0.298199,8.437805,5.480493,8.825306,1.896087,4.759316,4.592408,8.654837,0.053187,3.937037,-5.596737,-4.443431,6.274087,-4.964456,5.423527,-5.917699,-8.279247,-1.829512,-5.408135,3.993086,4.386309,-7.357372,1.227547,6.462960,4.955775,2.176654,-3.913744,-9.773220,-5.679502,-6.393134,-8.692297,7.684948,-9.946933,4.467609,7.002539,9.300525,4.969387,-9.602661,4.323533,0.428600,-0.754273,-6.086649,8.621285,-8.340774,-5.573263,4.561129,-1.451139,5.452498,3.272871,7.572884,-3.221107,0.817591,-2.179163,-2.833309,4.678888,-1.150899,3.575721,-7.603392,-8.433951,-4.948580,-3.274048,8.980703,-0.368461,5.633854,7.469905,-6.259593,5.020218,4.734839,5.743888,-3.949099,-6.453512,1.285193,6.053143,-3.910986,-9.356337,-2.843202,-0.810388,7.670805,3.572254,-1.693688,3.813360,-4.414943,-0.452646,-5.169592,6.130944,1.024985,-7.543829,3.732799,-1.807467,1.436384,-4.776845,0.196618], dtype = "float32")#candidate|4044|(208,)|const|float32
call_4043 = relay.TupleGetItem(func_961_call(relay.reshape(const_4044.astype('float32'), [4, 13, 4])), 2)
call_4045 = relay.TupleGetItem(func_964_call(relay.reshape(const_4044.astype('float32'), [4, 13, 4])), 2)
output = relay.Tuple([call_4024,call_4038,call_4043,const_4044,])
output2 = relay.Tuple([call_4025,call_4039,call_4045,const_4044,])
func_4048 = relay.Function([], output)
mod['func_4048'] = func_4048
mod = relay.transform.InferType()(mod)
mutated_mod['func_4048'] = func_4048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4048_call = mutated_mod.get_global_var('func_4048')
call_4049 = func_4048_call()
output = call_4049
func_4050 = relay.Function([], output)
mutated_mod['func_4050'] = func_4050
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4140 = relay.var("var_4140", dtype = "float32", shape = (12, 11, 7))#candidate|4140|(12, 11, 7)|var|float32
var_4141 = relay.var("var_4141", dtype = "float32", shape = (12, 11, 7))#candidate|4141|(12, 11, 7)|var|float32
bop_4142 = relay.less_equal(var_4140.astype('bool'), relay.reshape(var_4141.astype('bool'), relay.shape_of(var_4140))) # shape=(12, 11, 7)
func_1004_call = mod.get_global_var('func_1004')
func_1007_call = mutated_mod.get_global_var('func_1007')
const_4154 = relay.const([[1,-8],[-1,-4],[7,-5],[10,-6],[-4,2],[-1,8],[-10,-3],[-8,2],[10,-10],[2,-5],[1,-6],[2,1],[9,1],[-2,7],[5,6],[-6,-5],[-10,-7],[-8,-1],[-4,10],[-1,1],[-6,-1],[3,-10],[-8,4],[-7,-2]], dtype = "uint32")#candidate|4154|(24, 2)|const|uint32
call_4153 = func_1004_call(relay.reshape(const_4154.astype('uint32'), [2, 6, 4]))
call_4155 = func_1004_call(relay.reshape(const_4154.astype('uint32'), [2, 6, 4]))
func_3163_call = mod.get_global_var('func_3163')
func_3164_call = mutated_mod.get_global_var('func_3164')
call_4162 = func_3163_call()
call_4163 = func_3163_call()
func_2573_call = mod.get_global_var('func_2573')
func_2574_call = mutated_mod.get_global_var('func_2574')
call_4177 = relay.TupleGetItem(func_2573_call(), 0)
call_4178 = relay.TupleGetItem(func_2574_call(), 0)
func_60_call = mod.get_global_var('func_60')
func_64_call = mutated_mod.get_global_var('func_64')
const_4189 = relay.const([3,-1,-6,8,-4,-1,-2,-4,8,8,-7,5,4,-2,7,-8,1,-1,-4,-10,-8,5,-7,5,-3,5,6,2,3,-10,1,1,7,6,10,8,-7,6,-3,1,5,-8,5,-2,5,-1,10,-6,-5,-8,10,-1,-10,3,7,9,-2,-3,-8,7,7,-10,1,5,2,-9,3,1,6,-7,10,4,-5,-8,4,-4,5,-9,2,2,-1,-6,10,8,-3,-8,-10,-4,-3,-8,10,-9,8,1,4,-5,4,-9,-1,2,-9,7,-5,6,5,-7,8,2,-6,7,8,-4,3,9,-10,10,-1,3,-9,-6,-5,-1,-2,8,-10,7,4,2,-7,-3,-10,-8,-9,-9,-10,-3,1,-7,-9,-9,7,-6,-1,10,7,-7,-4,2,-6,2,-5,10,-8,-8,-1,5,7,10,-10,-8,-4,8,1,-3,-10,-2,9,2,10,-6,7,8,-5,-1,-9,-5,-5,-10,2,3,10,6,1,9,-6,-2,-8,-8,-7,9,-10,-8,7,1,-3,9,4,-3,3,-6,-6,-3,-7,7,-2,1,-1,6,8,7,-4,5,4,-2,-1,-6,-7,3,-2,9,9,5,-10,7,-8,9,1,-1,5,1,-4,-5,8,6,-10,-5,4,6,8,-1,-8,-10,6,3,9,-7,1,-5,-10,10,-5,-7,-2,2,-8,8,-3,6,-4,-1,1,7,10,2,2,-9,8,7,-1,-1,3,-9,-10,8,-2,-8,-6,6,6,7,-1,-4,-2,-10,-9,4,-2,10,7,-7,-8,-3,-7,-2,8,-10,6,9,-4,-1,-10,7,-9,6,-7,-5,6,-1,7,-6,3,-4,-10,4,-4,9,1,7,-4,-6,-4,8,-6,-4,2,-8,6,3,6,3,4,3,-9,9,-3,-6,3,6,-3,-4,10,10,-3,5,-2,-9,-10,6,-5,3,-8,-5,-3,4,-1,10,8,9,-3,-3,3,-3,-6,-10,-2,7,2,-4,-2,8,5,-7,8,-6,-10,-7,-1,-6,9,-6,-1,-4,-6,5,-5,1,2,4,-4,4,9,1,-2,-5,-4,-6,5,-5,8,-8,6,-4,-9,-10,-1,9,6,10,-6,2,7,3,8,4,10,1,-3,-4,-5,5,1,-8,5,-8,4,-1,8,6,5,-1,3,-1,-9,1,3,10,2,-2,7,-8,-10,3,-6,-3,10,-6,-8,-1,3,-10,8,10,-9,8,2,8,-6,9,1,-3,-8,4,-7,4,7,-8,-6,-4,1,-1,-8,5,10,-10,-6,4,3,3,-2,-3,10,3,-2,-1,1,-7,10,6,4,3,-8,-5,4,2,4,7,7,-10,-1,3,2,2,10,4,-4,5,1,-5,-9,-2,-2,-6,1,1,6,3,-2,2,4,7,10,-10,-3,7,-1,2,10,-6,6,2,-1,-10,1,-4,-7,-3,-2,-9,7,4,6,5,6,8,9,3,-6,-3,-6,-2,-8,9,7,3,-3,1,-7,-7,10,-6,-5,8,-4,8,8,5,4,-3,2,-4,7,4,4,6,7,2,10,3,3,-6,-3,6,-4,8,-7,1,-10,7,-8,-7,-4,9,10,-8,5,-1,-6,8,6,-4,-10,8,-9,5,5,-4,-10,-2,5,3,-5,-10,3,-1,-6,3,-9,8,-5,7,5,-10,-4,-7,-4,9,-7,10,-7,-1,5,8,5,4,-9,2,4,-8,4,-9,6,-10,9,4,-3,8,9,4,4,-5,-10,-6,9,-3,1,-1,-2,-3,1,6,10,-1,-1,-4,2,-7,-6,-7,1,8,-3,-3,10,-3,-1,4,-2,10,-10,8,4,2,-2,-5,-8,7,9,-4,3,-9,-6,-6,8,4,2,7,1,6,-8,-6,-1,8,2,1,9,10,5,-8,5,2,-5,-5,-10,-10,1,5,-1,-4,-4,8,6,-3,-7,-5,-2,-10,-6,3,-6,-4,-3,9,-3,6,-7,-3,4,4,-4,4,4,2,10,5,2,-1,10,8,-2,-3,1,-1,-9,-8,2,8,7,5,7,3,1,4,-5,-7,7,7,-3,6,-1,-6,8,10,-5,-5,5,4,6,-9,10,-10,-5,6,-3,-1,-7,-9,2,2,-4,-10,7,-7,1,3,-2,-8,-8,-7,9,9,-5,-2,-10,4,3,3,7,-2,5,-10,8,4,-2,-1,8,-8,-10,10,5,4,-8,-10,8,-5,-7,10,3,-3,4,8,4,5,-6,-4,8,1,-4,3,2,4,3,5,7,-10,4,1,4,1,-10,3,2,6,-4,7,8,-3,3,-8,-10,1,6,3,9,-2], dtype = "uint8")#candidate|4189|(864,)|const|uint8
call_4188 = relay.TupleGetItem(func_60_call(relay.reshape(const_4189.astype('uint8'), [6, 9, 16]), relay.reshape(const_4189.astype('uint8'), [6, 9, 16]), ), 0)
call_4190 = relay.TupleGetItem(func_64_call(relay.reshape(const_4189.astype('uint8'), [6, 9, 16]), relay.reshape(const_4189.astype('uint8'), [6, 9, 16]), ), 0)
func_158_call = mod.get_global_var('func_158')
func_163_call = mutated_mod.get_global_var('func_163')
call_4203 = relay.TupleGetItem(func_158_call(relay.reshape(const_4189.astype('bool'), [9, 8, 12]), relay.reshape(call_4188.astype('bool'), [9, 8, 12]), relay.reshape(call_4177.astype('int16'), [1248, 1]), ), 3)
call_4204 = relay.TupleGetItem(func_163_call(relay.reshape(const_4189.astype('bool'), [9, 8, 12]), relay.reshape(call_4188.astype('bool'), [9, 8, 12]), relay.reshape(call_4177.astype('int16'), [1248, 1]), ), 3)
output = relay.Tuple([bop_4142,call_4153,const_4154,call_4162,call_4177,call_4188,const_4189,call_4203,])
output2 = relay.Tuple([bop_4142,call_4155,const_4154,call_4163,call_4178,call_4190,const_4189,call_4204,])
func_4239 = relay.Function([var_4140,var_4141,], output)
mod['func_4239'] = func_4239
mod = relay.transform.InferType()(mod)
var_4240 = relay.var("var_4240", dtype = "float32", shape = (12, 11, 7))#candidate|4240|(12, 11, 7)|var|float32
var_4241 = relay.var("var_4241", dtype = "float32", shape = (12, 11, 7))#candidate|4241|(12, 11, 7)|var|float32
output = func_4239(var_4240,var_4241,)
func_4242 = relay.Function([var_4240,var_4241,], output)
mutated_mod['func_4242'] = func_4242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2114_call = mod.get_global_var('func_2114')
func_2115_call = mutated_mod.get_global_var('func_2115')
call_4247 = func_2114_call()
call_4248 = func_2114_call()
output = call_4247
output2 = call_4248
func_4254 = relay.Function([], output)
mod['func_4254'] = func_4254
mod = relay.transform.InferType()(mod)
output = func_4254()
func_4255 = relay.Function([], output)
mutated_mod['func_4255'] = func_4255
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4259 = relay.var("var_4259", dtype = "float32", shape = ())#candidate|4259|()|var|float32
var_4260 = relay.var("var_4260", dtype = "float32", shape = (1, 6, 11))#candidate|4260|(1, 6, 11)|var|float32
bop_4261 = relay.mod(var_4259.astype('float32'), var_4260.astype('float32')) # shape=(1, 6, 11)
output = relay.Tuple([bop_4261,])
output2 = relay.Tuple([bop_4261,])
func_4275 = relay.Function([var_4259,var_4260,], output)
mod['func_4275'] = func_4275
mod = relay.transform.InferType()(mod)
mutated_mod['func_4275'] = func_4275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4275_call = mutated_mod.get_global_var('func_4275')
var_4277 = relay.var("var_4277", dtype = "float32", shape = ())#candidate|4277|()|var|float32
var_4278 = relay.var("var_4278", dtype = "float32", shape = (1, 6, 11))#candidate|4278|(1, 6, 11)|var|float32
call_4276 = func_4275_call(var_4277,var_4278,)
output = call_4276
func_4279 = relay.Function([var_4277,var_4278,], output)
mutated_mod['func_4279'] = func_4279
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4302 = relay.const([[[-3.591778,-3.154787,9.485099,9.566486,7.364630,-0.748656,1.924971,1.238936,-0.601705,7.287297,9.066435,5.036585,-9.354992],[-5.009779,9.667125,8.247258,-8.712642,7.640262,-1.119277,4.885064,-5.720069,3.151304,-1.747021,-7.257757,-4.316197,-6.424000],[0.826619,-6.060167,-1.820493,0.848058,-9.802713,5.621232,-7.810790,-0.889610,8.539660,-7.300465,1.447261,3.133333,-9.184248],[7.197922,7.400143,6.488565,5.621784,-0.361774,-9.817150,9.638560,-9.124125,8.125293,-8.679795,-8.289338,-2.758694,3.997167]]], dtype = "float64")#candidate|4302|(1, 4, 13)|const|float64
uop_4303 = relay.sqrt(const_4302.astype('float64')) # shape=(1, 4, 13)
func_60_call = mod.get_global_var('func_60')
func_64_call = mutated_mod.get_global_var('func_64')
const_4321 = relay.const([-10,6,-3,5,-9,1,5,-8,-8,1,-6,9,-8,1,-10,10,3,7,-7,3,1,5,-1,-1,5,-8,-10,4,10,2,4,-10,-7,4,-9,9,10,-4,-6,9,-8,4,-3,-5,-6,5,-10,6,9,-1,-6,8,6,-8,-8,4,5,3,-8,1,7,3,-10,-7,6,9,10,-9,-1,9,-3,5,-2,-6,-7,6,2,1,8,-10,8,8,7,4,-6,7,-5,9,-9,2,1,-1,-9,2,-2,4,2,-8,1,6,3,7,4,-7,-1,2,-9,5,-5,7,-1,-7,-5,3,7,3,3,-9,-8,-1,-7,10,-5,-6,-2,-2,-4,-8,-4,-4,8,-2,-1,-9,7,-7,4,10,4,2,9,-1,-2,1,-9,8,4,10,9,2,9,10,-1,-3,-8,-3,8,7,2,-8,3,-10,-6,-2,-8,-2,-6,-10,-5,-3,7,-10,-9,-5,-7,2,10,8,-2,2,-5,-9,-1,9,2,-10,6,-4,-9,6,1,-7,-1,9,-3,5,7,10,-5,-5,1,-7,-5,1,-9,9,6,3,1,3,4,4,4,-1,-1,9,2,-8,-7,1,8,8,-6,-3,4,10,6,1,-8,-10,-9,-10,2,-7,8,7,-10,2,-7,-2,3,-2,8,10,6,-4,8,7,1,-1,4,7,-2,-1,-5,3,-8,6,8,1,-5,-10,-10,-3,3,-2,-1,-2,-7,5,7,-10,10,-1,2,-2,-7,-2,-9,8,10,-8,8,-5,4,-6,7,-6,-2,7,8,-4,2,-4,10,3,-3,-10,-3,-7,-4,-10,1,-10,-2,8,6,7,-8,9,6,-6,4,-1,1,-6,2,-8,1,-5,-6,-4,-7,-10,-5,-10,10,-9,2,-3,-7,9,-6,-2,6,-1,2,-3,-10,1,2,4,9,-8,3,-3,-2,-2,1,7,-3,10,-6,6,7,-1,1,3,-9,9,4,-4,6,5,10,-5,-2,2,-1,6,-6,-7,2,-6,-2,-5,-1,-5,5,-4,-3,1,7,3,-2,4,-6,6,4,3,9,4,-8,-6,-10,7,-3,-7,2,6,9,-1,-4,4,-10,-6,6,-10,-1,-5,-9,2,-3,-10,-1,10,-8,-4,9,-2,7,-10,10,-5,-6,-1,7,5,-4,-8,3,2,10,-6,8,-9,-6,7,-9,-6,-7,2,-10,-5,-3,-7,10,10,7,-8,-3,-9,-6,-6,9,1,-9,-9,9,-3,-6,1,-2,-5,-6,-4,-1,-2,1,1,-8,-5,7,-5,-9,-1,9,-2,-2,9,-1,-8,10,-9,-6,1,5,2,-10,-8,-5,4,10,6,5,9,10,6,7,-1,8,-8,5,-4,-9,4,3,8,5,3,-9,4,10,-1,7,-2,3,-7,2,-5,-6,-2,8,2,6,-3,-8,8,9,4,3,-3,6,5,3,-8,1,-10,2,4,7,-6,-4,-10,-6,-3,10,3,7,-3,-10,-3,-1,-1,5,4,3,-5,-6,2,-1,9,2,-5,-4,3,-9,6,-1,4,10,-8,-10,10,9,-6,-10,2,-8,4,7,-7,-6,-8,-8,3,-2,3,-5,6,6,4,8,9,-3,10,-10,8,-10,1,1,-7,4,-5,-4,2,-2,7,4,-5,-9,-9,-4,3,3,3,9,-7,2,1,-10,8,-3,3,3,6,-5,-10,-2,-2,-8,-9,4,9,5,-2,5,8,-8,-7,8,-4,-8,1,-9,5,5,4,9,3,-5,2,8,-8,-10,7,8,-3,8,-6,-5,4,-6,-9,-4,-2,9,9,-3,-4,-3,3,2,8,9,7,-5,-6,-3,-8,7,-6,-2,-6,3,10,-10,-7,-10,-2,-9,5,-4,-6,5,-4,4,1,-4,-10,6,2,2,8,-6,-1,1,-2,-6,-2,2,3,5,-1,2,7,-1,6,2,-7,4,5,5,-2,8,2,-9,8,-3,-6,-10,5,-4,9,4,-4,6,-6,9,-4,2,-6,4,-9,-3,-2,-8,6,-9,-7,3,-3,-3,1,-9,-10,2,-5,10,-1,-7,-5,3,8,-8,-5,8,-1,-1,4,9,2,-10,8,-1,10,-4,-4,10,-1,4,-1,-5,5,7,5,-3,-7,-4,-10,6,2,9,-8,-5,-7,-4,3,-5,7,-8,-9,-9,-2,3,-5,-2,-10,-2,-9,-7,6,-7,5,7,-3,4,4,10,6,7,-2,-8,-1,-3,7,-7,3,4,-7,10,8,3,7,7,7,-5,-5,3,5,-6,-8,-9,-10,-9,-6,8,4,5,5,5,5,4,6,8,5,-8,-9,-4,-8,8,3,-7,7], dtype = "uint8")#candidate|4321|(864,)|const|uint8
call_4320 = relay.TupleGetItem(func_60_call(relay.reshape(const_4321.astype('uint8'), [6, 9, 16]), relay.reshape(const_4321.astype('uint8'), [6, 9, 16]), ), 0)
call_4322 = relay.TupleGetItem(func_64_call(relay.reshape(const_4321.astype('uint8'), [6, 9, 16]), relay.reshape(const_4321.astype('uint8'), [6, 9, 16]), ), 0)
func_1411_call = mod.get_global_var('func_1411')
func_1413_call = mutated_mod.get_global_var('func_1413')
call_4335 = func_1411_call()
call_4336 = func_1411_call()
bop_4339 = relay.logical_xor(uop_4303.astype('int32'), relay.reshape(const_4302.astype('int32'), relay.shape_of(uop_4303))) # shape=(1, 4, 13)
output = relay.Tuple([call_4320,const_4321,call_4335,bop_4339,])
output2 = relay.Tuple([call_4322,const_4321,call_4336,bop_4339,])
func_4344 = relay.Function([], output)
mod['func_4344'] = func_4344
mod = relay.transform.InferType()(mod)
output = func_4344()
func_4345 = relay.Function([], output)
mutated_mod['func_4345'] = func_4345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2573_call = mod.get_global_var('func_2573')
func_2574_call = mutated_mod.get_global_var('func_2574')
call_4360 = relay.TupleGetItem(func_2573_call(), 0)
call_4361 = relay.TupleGetItem(func_2574_call(), 0)
output = call_4360
output2 = call_4361
func_4364 = relay.Function([], output)
mod['func_4364'] = func_4364
mod = relay.transform.InferType()(mod)
mutated_mod['func_4364'] = func_4364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4364_call = mutated_mod.get_global_var('func_4364')
call_4365 = func_4364_call()
output = call_4365
func_4366 = relay.Function([], output)
mutated_mod['func_4366'] = func_4366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1235_call = mod.get_global_var('func_1235')
func_1237_call = mutated_mod.get_global_var('func_1237')
call_4391 = func_1235_call()
call_4392 = func_1235_call()
func_3288_call = mod.get_global_var('func_3288')
func_3289_call = mutated_mod.get_global_var('func_3289')
call_4395 = func_3288_call()
call_4396 = func_3288_call()
bop_4397 = relay.bitwise_xor(call_4391.astype('int8'), relay.reshape(call_4395.astype('int8'), relay.shape_of(call_4391))) # shape=(1, 11, 3)
bop_4400 = relay.bitwise_xor(call_4392.astype('int8'), relay.reshape(call_4396.astype('int8'), relay.shape_of(call_4392))) # shape=(1, 11, 3)
func_2833_call = mod.get_global_var('func_2833')
func_2834_call = mutated_mod.get_global_var('func_2834')
call_4414 = relay.TupleGetItem(func_2833_call(), 1)
call_4415 = relay.TupleGetItem(func_2834_call(), 1)
output = relay.Tuple([bop_4397,call_4414,])
output2 = relay.Tuple([bop_4400,call_4415,])
func_4438 = relay.Function([], output)
mod['func_4438'] = func_4438
mod = relay.transform.InferType()(mod)
mutated_mod['func_4438'] = func_4438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4438_call = mutated_mod.get_global_var('func_4438')
call_4439 = func_4438_call()
output = call_4439
func_4440 = relay.Function([], output)
mutated_mod['func_4440'] = func_4440
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4447 = relay.var("var_4447", dtype = "float64", shape = (10, 2, 3))#candidate|4447|(10, 2, 3)|var|float64
var_4448 = relay.var("var_4448", dtype = "float64", shape = (10, 2, 3))#candidate|4448|(10, 2, 3)|var|float64
bop_4449 = relay.greater(var_4447.astype('bool'), relay.reshape(var_4448.astype('bool'), relay.shape_of(var_4447))) # shape=(10, 2, 3)
func_2586_call = mod.get_global_var('func_2586')
func_2588_call = mutated_mod.get_global_var('func_2588')
call_4469 = func_2586_call()
call_4470 = func_2586_call()
func_858_call = mod.get_global_var('func_858')
func_861_call = mutated_mod.get_global_var('func_861')
var_4481 = relay.var("var_4481", dtype = "uint8", shape = (1365,))#candidate|4481|(1365,)|var|uint8
call_4480 = relay.TupleGetItem(func_858_call(relay.reshape(var_4481.astype('uint8'), [13, 7, 15])), 2)
call_4482 = relay.TupleGetItem(func_861_call(relay.reshape(var_4481.astype('uint8'), [13, 7, 15])), 2)
func_3686_call = mod.get_global_var('func_3686')
func_3687_call = mutated_mod.get_global_var('func_3687')
call_4484 = func_3686_call()
call_4485 = func_3686_call()
bop_4493 = relay.less_equal(var_4447.astype('bool'), relay.reshape(bop_4449.astype('bool'), relay.shape_of(var_4447))) # shape=(10, 2, 3)
func_2064_call = mod.get_global_var('func_2064')
func_2066_call = mutated_mod.get_global_var('func_2066')
call_4496 = relay.TupleGetItem(func_2064_call(relay.reshape(call_4480.astype('uint8'), [16, 13, 6])), 0)
call_4497 = relay.TupleGetItem(func_2066_call(relay.reshape(call_4480.astype('uint8'), [16, 13, 6])), 0)
output = relay.Tuple([call_4469,call_4480,var_4481,call_4484,bop_4493,call_4496,])
output2 = relay.Tuple([call_4470,call_4482,var_4481,call_4485,bop_4493,call_4497,])
func_4500 = relay.Function([var_4447,var_4448,var_4481,], output)
mod['func_4500'] = func_4500
mod = relay.transform.InferType()(mod)
mutated_mod['func_4500'] = func_4500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4500_call = mutated_mod.get_global_var('func_4500')
var_4502 = relay.var("var_4502", dtype = "float64", shape = (10, 2, 3))#candidate|4502|(10, 2, 3)|var|float64
var_4503 = relay.var("var_4503", dtype = "float64", shape = (10, 2, 3))#candidate|4503|(10, 2, 3)|var|float64
var_4504 = relay.var("var_4504", dtype = "uint8", shape = (1365,))#candidate|4504|(1365,)|var|uint8
call_4501 = func_4500_call(var_4502,var_4503,var_4504,)
output = call_4501
func_4505 = relay.Function([var_4502,var_4503,var_4504,], output)
mutated_mod['func_4505'] = func_4505
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4507 = relay.var("var_4507", dtype = "float64", shape = ())#candidate|4507|()|var|float64
const_4508 = relay.const([[[3.962377,-9.362625,1.023288,-0.140561,-3.336680,-8.929863,6.081472,4.031305,-1.717493],[5.283898,-3.163272,-8.247779,-2.732871,2.632671,-1.792522,8.228131,-1.607812,3.376379],[-6.344493,4.367608,-1.608540,4.390414,9.531623,3.323362,3.365093,-6.364211,-6.085100],[0.726239,4.226739,-8.705484,5.319350,5.990055,8.908431,2.354013,-9.299450,-2.908573],[-9.811928,1.816345,-3.750631,3.399126,1.882316,2.862489,-9.820632,-3.489873,6.158339],[6.179338,3.770325,9.430672,-9.674903,-2.290862,7.276747,3.286269,-8.057594,3.700711],[4.422319,0.006337,3.008232,-5.267595,1.804602,0.171382,2.581749,7.392807,3.740736]],[[9.316030,4.576531,5.101741,-7.289709,-2.748727,2.156553,4.770340,-6.948934,3.560944],[-7.899443,9.659361,-6.160702,-8.563855,-2.153980,-0.947265,-7.102430,7.075836,-5.142731],[2.307583,8.844016,4.081839,3.084706,-5.447140,7.822533,0.305591,5.589706,9.247914],[8.125823,-1.587007,0.167238,-7.984705,-9.005257,7.308156,-9.403831,-8.416693,-4.663885],[-8.085429,-0.730836,9.833896,-0.305068,9.606827,-8.289956,4.587805,5.286763,1.242183],[4.870895,-1.759916,2.244564,-2.675126,-1.606451,2.235460,-6.640988,4.819492,-3.505343],[9.391051,7.398248,0.532047,4.846393,-5.329456,-5.961713,-0.469340,6.898551,3.710651]],[[-8.297720,-6.769735,-4.086345,-1.171481,3.074064,-5.804180,-1.338716,-6.012569,-9.083872],[7.375414,-6.060715,-7.271599,3.245840,-0.866972,-2.515521,4.877588,6.368812,6.017587],[-0.215361,4.437291,2.544771,7.794301,7.372004,-9.715482,8.123142,2.262049,6.275951],[-0.195557,-7.543482,6.833178,9.543914,-4.396788,-3.035182,-4.584324,8.266664,-8.016967],[3.701824,-1.186833,1.150894,3.249025,2.739872,-8.984792,-2.430736,0.076903,-7.166811],[6.547462,-7.348462,-8.822426,-0.417569,7.127532,-4.854836,-6.239804,6.421435,-3.198274],[1.477128,-6.470866,4.671549,9.879190,7.531694,-6.066350,5.910174,1.435831,9.505003]],[[-9.363547,8.148678,0.258390,0.039431,5.062652,1.603351,5.537963,8.848293,9.970306],[7.265089,6.232579,5.311532,-3.177750,8.532163,-8.736794,6.521227,-9.297533,-9.192452],[0.200999,-4.038595,2.856766,-1.968377,-7.822143,-5.459306,-7.771241,7.177670,-3.922628],[-2.379198,5.675158,5.376738,-0.909801,6.944869,6.233850,8.411212,0.020812,2.380958],[4.494683,-3.231552,-6.813797,5.895409,-4.337621,-5.682020,0.427363,3.468875,-6.349604],[9.167931,9.362367,-8.162347,-7.408643,1.544168,8.699628,-2.571826,9.662141,-3.585259],[9.669147,-7.213155,-6.243036,5.428344,9.168946,4.977911,2.044270,2.504059,1.307570]]], dtype = "float64")#candidate|4508|(4, 7, 9)|const|float64
bop_4509 = relay.divide(var_4507.astype('float64'), const_4508.astype('float64')) # shape=(4, 7, 9)
const_4530 = relay.const([[[4.318792,-9.263520,-8.758883,-6.225218,5.811659,-4.017974,4.858178,6.451198,-5.733121],[-0.130562,-4.033724,5.247660,8.640172,-8.508345,4.317801,1.503575,-2.459837,-0.044431],[4.288517,-5.942663,-7.154180,5.166823,9.229608,-2.630428,-5.985956,-7.623494,-2.688612],[2.729537,2.560817,2.270380,1.268445,9.536216,1.371069,-3.477050,-1.491656,6.910520],[7.329516,5.033768,0.724734,-8.775544,-1.310694,9.175001,-6.191452,-0.073930,-4.348918],[-8.678230,6.802129,7.516795,-7.182079,9.029578,6.498185,2.957944,3.120599,4.566733],[-4.061158,6.829314,-1.792451,7.879470,6.912142,-9.498863,-4.549641,1.351131,6.033561]],[[-6.498498,-7.861255,-5.019854,-1.261126,-7.015652,-8.658328,-8.794692,0.507580,-3.289166],[-7.292774,1.536380,8.337282,0.590872,-1.149496,3.451493,-2.994452,4.218595,6.719726],[-6.592586,1.931319,-8.626418,-9.080726,-6.852622,-6.579491,-2.554674,9.944348,-8.584777],[4.546190,-2.645520,-8.211142,0.152961,7.049696,4.951286,2.845025,-8.515289,-4.124655],[-2.768761,0.956222,-7.504257,2.933732,6.611856,-4.457155,-9.567947,6.919707,-3.116582],[-1.020876,-8.491923,-2.483819,1.482338,3.942483,1.040435,-5.251603,6.292886,-4.915139],[2.570805,-4.479231,-9.587958,-5.706352,-2.134144,2.410329,9.542563,7.327854,7.178282]],[[4.441172,6.795685,-3.319077,-3.136884,-8.719546,6.498810,4.866955,8.398355,4.041897],[8.048606,-8.320680,4.030770,-2.566704,1.766084,4.053860,0.804374,3.033364,8.031435],[5.085538,-0.970734,8.402109,1.614642,-2.114527,-7.867046,-6.910596,9.925278,-4.109011],[6.167241,2.095245,-5.364417,2.388827,2.991660,-8.423434,4.046175,-5.698610,3.085882],[0.107905,3.547943,2.599850,3.343928,2.939086,-3.879670,0.316927,-6.225740,2.443681],[7.016605,-3.252202,4.604575,-6.393503,8.575863,0.090900,-6.740925,5.590879,-8.852005],[-4.214645,-2.204668,2.466195,2.850311,-5.117166,2.600115,-6.042261,9.434936,-4.972656]],[[2.841582,7.069591,4.190494,8.939281,4.100554,7.703825,-6.106953,7.259057,9.025706],[3.724085,2.895873,-4.731685,0.796884,-1.659218,-1.346277,-5.062932,4.366042,-7.101587],[-1.223720,-2.129253,-0.197569,7.078031,9.844391,2.151806,3.628616,0.728321,6.152620],[-5.133144,-0.039533,0.059131,5.277880,-2.356584,5.751643,9.667789,2.402043,7.232082],[-4.473533,-9.609679,2.334116,-4.899371,-1.176302,8.593266,-3.295480,7.190129,-0.851390],[6.374404,-5.725725,-4.241909,-4.277736,4.943025,-7.606868,1.549585,1.636229,-5.754232],[2.118349,-3.566528,9.663303,5.541514,6.886897,-8.660954,2.187945,5.422522,-8.682911]]], dtype = "float64")#candidate|4530|(4, 7, 9)|const|float64
bop_4531 = relay.bitwise_and(bop_4509.astype('int32'), relay.reshape(const_4530.astype('int32'), relay.shape_of(bop_4509))) # shape=(4, 7, 9)
func_2265_call = mod.get_global_var('func_2265')
func_2267_call = mutated_mod.get_global_var('func_2267')
call_4537 = relay.TupleGetItem(func_2265_call(), 1)
call_4538 = relay.TupleGetItem(func_2267_call(), 1)
output = relay.Tuple([bop_4531,call_4537,])
output2 = relay.Tuple([bop_4531,call_4538,])
func_4557 = relay.Function([var_4507,], output)
mod['func_4557'] = func_4557
mod = relay.transform.InferType()(mod)
mutated_mod['func_4557'] = func_4557
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4558 = relay.var("var_4558", dtype = "float64", shape = ())#candidate|4558|()|var|float64
func_4557_call = mutated_mod.get_global_var('func_4557')
call_4559 = func_4557_call(var_4558)
output = call_4559
func_4560 = relay.Function([var_4558], output)
mutated_mod['func_4560'] = func_4560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1817_call = mod.get_global_var('func_1817')
func_1819_call = mutated_mod.get_global_var('func_1819')
call_4617 = func_1817_call()
call_4618 = func_1817_call()
output = call_4617
output2 = call_4618
func_4619 = relay.Function([], output)
mod['func_4619'] = func_4619
mod = relay.transform.InferType()(mod)
mutated_mod['func_4619'] = func_4619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4619_call = mutated_mod.get_global_var('func_4619')
call_4620 = func_4619_call()
output = call_4620
func_4621 = relay.Function([], output)
mutated_mod['func_4621'] = func_4621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2955_call = mod.get_global_var('func_2955')
func_2957_call = mutated_mod.get_global_var('func_2957')
call_4628 = relay.TupleGetItem(func_2955_call(), 5)
call_4629 = relay.TupleGetItem(func_2957_call(), 5)
func_1396_call = mod.get_global_var('func_1396')
func_1398_call = mutated_mod.get_global_var('func_1398')
const_4632 = relay.const([1.207757,2.355951,-1.557618,0.734062,-1.776864,-3.213596,-6.165484,4.149082,5.407720,-1.560564,-3.004044,-2.978799,-2.099612,-2.881246,2.370315,-7.885823,2.742109,7.612726,1.289103,8.385757,-2.878766,-6.818031,8.204390,-2.645465,0.111878,-0.808968,-4.191804,5.148972,0.396330,-6.838978,1.271895,-3.517729,-6.785900,-7.232359,-2.990940,7.649405,-1.564462,3.347420,-5.982651,-4.898114,-0.977723,3.913175,-0.192157,8.636393,8.965042,-8.544941,1.302373,3.207464,-2.401402,6.732995,5.491537,3.830535,6.033019,4.661556,-2.457041,7.791524,-2.896979,3.394097,4.737014,-2.149612,-9.860683,4.147747,0.547628,-8.827332,6.923050,-4.202434,-1.148478,-6.666312,9.326183,8.494332,7.317004,-7.732650,-6.030190,-4.186126,8.825206,-6.083046,-5.149267,0.752126,-4.366211,2.594732,6.179171,-4.428194,-8.710701,7.643163,-3.926380,3.866632,3.735371,9.286288,-0.554979,4.971153,-3.564323,1.606951,-3.340825,6.766185,-6.669138,-2.202084,-7.822246,-0.865532,6.384175,-5.111944,-6.888994,5.972209,-1.434992,5.301108,1.703033,-0.495264,-9.797195,-9.516302,-2.219862,6.427869,-9.657462,-1.330061,-9.489052,7.149364,9.930017,9.633047,-6.121716,4.922991,5.087352,3.562963,-8.728488,0.506583,9.356858,3.006434,1.369898,6.658360,-3.083154,-8.253891,-6.862540,-7.643381,-0.767966,7.205413,-4.919564,4.744666,-2.761510,-2.379558,-5.372135,9.954676,8.378748,1.927888,-6.828904,9.580463,-9.298160,0.935230,7.747175,-9.524483,-2.754825,-6.319965,0.156167,-3.879204,-6.483794,-0.594759,-0.608285,3.660519,-0.268594,-2.875636,9.538115,1.070566,-6.427373,-0.298002,-4.049939,7.550093,-2.560735,2.439075,0.540581,4.732130,6.910991,-0.874578,-0.077453,8.008100,-3.039524,8.370595,4.552459,5.072249,4.514419,-4.922772,8.587825,-8.764160,2.995600,2.403269,-1.803161,8.139559,-3.587339,8.543692,2.933564,4.717172,6.400786,0.406136,8.978364,-5.195611,-8.912064,-2.324531,-3.825098,2.487974,-2.974466,-9.328122,-3.638367,-2.887641,0.254527,6.507466,3.242642,-8.771372,5.784330,8.840549,-8.160419,0.445423,-9.920321,-3.557427], dtype = "float32")#candidate|4632|(208,)|const|float32
call_4631 = relay.TupleGetItem(func_1396_call(relay.reshape(const_4632.astype('float32'), [104, 2])), 1)
call_4633 = relay.TupleGetItem(func_1398_call(relay.reshape(const_4632.astype('float32'), [104, 2])), 1)
output = relay.Tuple([call_4628,call_4631,const_4632,])
output2 = relay.Tuple([call_4629,call_4633,const_4632,])
func_4642 = relay.Function([], output)
mod['func_4642'] = func_4642
mod = relay.transform.InferType()(mod)
output = func_4642()
func_4643 = relay.Function([], output)
mutated_mod['func_4643'] = func_4643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2311_call = mod.get_global_var('func_2311')
func_2313_call = mutated_mod.get_global_var('func_2313')
call_4741 = func_2311_call()
call_4742 = func_2311_call()
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_4759 = relay.TupleGetItem(func_2220_call(), 0)
call_4760 = relay.TupleGetItem(func_2222_call(), 0)
output = relay.Tuple([call_4741,call_4759,])
output2 = relay.Tuple([call_4742,call_4760,])
func_4773 = relay.Function([], output)
mod['func_4773'] = func_4773
mod = relay.transform.InferType()(mod)
mutated_mod['func_4773'] = func_4773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4773_call = mutated_mod.get_global_var('func_4773')
call_4774 = func_4773_call()
output = call_4774
func_4775 = relay.Function([], output)
mutated_mod['func_4775'] = func_4775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4773_call = mod.get_global_var('func_4773')
func_4775_call = mutated_mod.get_global_var('func_4775')
call_4776 = relay.TupleGetItem(func_4773_call(), 0)
call_4777 = relay.TupleGetItem(func_4775_call(), 0)
output = relay.Tuple([call_4776,])
output2 = relay.Tuple([call_4777,])
func_4790 = relay.Function([], output)
mod['func_4790'] = func_4790
mod = relay.transform.InferType()(mod)
mutated_mod['func_4790'] = func_4790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4790_call = mutated_mod.get_global_var('func_4790')
call_4791 = func_4790_call()
output = call_4791
func_4792 = relay.Function([], output)
mutated_mod['func_4792'] = func_4792
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4814 = relay.var("var_4814", dtype = "float32", shape = (16, 12, 15))#candidate|4814|(16, 12, 15)|var|float32
uop_4815 = relay.atan(var_4814.astype('float32')) # shape=(16, 12, 15)
output = relay.Tuple([uop_4815,])
output2 = relay.Tuple([uop_4815,])
func_4828 = relay.Function([var_4814,], output)
mod['func_4828'] = func_4828
mod = relay.transform.InferType()(mod)
mutated_mod['func_4828'] = func_4828
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4829 = relay.var("var_4829", dtype = "float32", shape = (16, 12, 15))#candidate|4829|(16, 12, 15)|var|float32
func_4828_call = mutated_mod.get_global_var('func_4828')
call_4830 = func_4828_call(var_4829)
output = call_4830
func_4831 = relay.Function([var_4829], output)
mutated_mod['func_4831'] = func_4831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4344_call = mod.get_global_var('func_4344')
func_4345_call = mutated_mod.get_global_var('func_4345')
call_4833 = relay.TupleGetItem(func_4344_call(), 0)
call_4834 = relay.TupleGetItem(func_4345_call(), 0)
func_2586_call = mod.get_global_var('func_2586')
func_2588_call = mutated_mod.get_global_var('func_2588')
call_4844 = func_2586_call()
call_4845 = func_2586_call()
uop_4847 = relay.acos(call_4844.astype('float32')) # shape=(16, 13, 6)
uop_4849 = relay.acos(call_4845.astype('float32')) # shape=(16, 13, 6)
output = relay.Tuple([call_4833,uop_4847,])
output2 = relay.Tuple([call_4834,uop_4849,])
func_4861 = relay.Function([], output)
mod['func_4861'] = func_4861
mod = relay.transform.InferType()(mod)
mutated_mod['func_4861'] = func_4861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4861_call = mutated_mod.get_global_var('func_4861')
call_4862 = func_4861_call()
output = call_4862
func_4863 = relay.Function([], output)
mutated_mod['func_4863'] = func_4863
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5053 = relay.var("var_5053", dtype = "int32", shape = (14, 14, 7))#candidate|5053|(14, 14, 7)|var|int32
const_5054 = relay.const([[[-2,-4,-8,3,8,8,-6],[-6,8,-8,5,7,-10,6],[-4,9,-7,-2,10,2,5],[-1,-6,2,8,-4,-5,-3],[-9,-8,3,10,-2,4,8],[-1,-7,6,3,1,9,4],[-8,10,6,-2,-7,9,-5],[-3,-1,7,-1,5,-2,-5],[2,6,6,9,6,-1,4],[-4,4,-1,6,-5,1,-10],[4,4,5,-10,-8,3,2],[6,-5,-4,-10,4,-3,2],[6,-8,9,8,4,5,9],[-7,-3,5,-5,-6,4,-2]],[[8,-2,10,-7,-4,3,5],[3,9,4,-4,7,-8,8],[-5,-2,6,9,5,-5,3],[10,-9,3,-2,-7,6,8],[8,-9,-6,-6,-4,-8,-1],[2,2,-3,5,-6,-4,3],[-10,-7,7,-1,-6,7,2],[-1,-8,-8,-4,-9,10,6],[-10,-4,-2,-1,7,-3,-1],[-3,6,7,-8,2,7,-9],[-9,-10,3,-1,7,5,-4],[-6,-9,-9,4,8,-2,-4],[-2,-5,-9,1,-9,9,4],[9,-2,-4,-6,7,8,10]],[[4,8,-8,-8,-10,-8,-1],[6,-1,-5,1,-6,-2,-5],[-6,10,-10,7,-3,-4,4],[-1,-9,2,3,-2,7,-1],[9,-9,2,7,10,-1,-9],[-6,-7,9,6,-5,-9,5],[-5,4,2,-10,-3,-8,1],[5,-6,-2,-10,10,-10,-4],[2,-6,-6,2,6,-4,-7],[9,6,7,-5,-5,-7,10],[10,8,-5,-10,7,-1,-3],[1,9,-9,3,7,4,4],[8,9,-8,-1,-5,6,-4],[4,-1,-9,-6,5,4,-9]],[[3,10,-5,-1,-9,-10,5],[6,-2,-9,7,3,-8,-3],[2,3,-5,-9,3,7,-2],[6,-10,7,7,5,5,7],[8,-6,-4,-6,-1,3,-4],[-7,7,4,-10,-1,6,-10],[4,4,1,-2,8,-6,-4],[-6,9,-3,-9,-4,-7,-7],[-9,-5,6,6,-9,2,8],[-10,-5,9,10,-10,8,-9],[9,9,4,-2,5,-8,8],[-4,8,-7,8,8,-9,-8],[-2,-3,4,-10,9,-1,-2],[9,-8,6,-4,-2,-10,-10]],[[-9,-7,9,4,5,-2,-8],[7,1,-9,8,9,-8,-4],[-1,9,-7,1,-6,9,-10],[6,-5,7,-10,9,2,9],[6,2,2,-7,6,2,4],[-5,-4,2,3,-5,8,10],[1,1,5,-5,3,-5,-2],[4,8,-4,-8,2,-8,6],[-1,3,8,-1,9,9,10],[2,-10,-1,4,3,-2,5],[3,3,8,8,-1,-8,-5],[-2,-10,8,-1,-10,-2,8],[9,-1,7,-6,1,-10,3],[5,-6,4,3,7,10,-10]],[[-2,6,6,-4,3,-9,-4],[-9,8,6,2,1,9,-9],[7,3,2,3,-9,10,-6],[10,-7,-8,4,-10,-1,2],[-10,1,2,7,5,1,-6],[8,1,4,7,-4,8,-7],[-6,-1,2,2,-7,-10,-10],[6,4,-7,-2,-3,-7,-3],[-3,-1,1,-3,-5,-7,-5],[-7,-7,-10,7,-4,-10,-1],[5,9,-4,5,6,8,-5],[6,-9,-7,-5,7,-4,-2],[-9,-3,-9,-2,-7,-8,-7],[6,1,-5,4,9,9,-1]],[[9,9,-10,-4,-9,10,3],[8,-6,5,-6,-8,-2,-10],[-2,-4,-8,-9,-7,5,-9],[-1,5,-6,4,8,2,10],[4,-5,-3,-7,3,-7,-1],[8,7,4,-1,-5,-4,4],[-9,-1,2,-9,-6,6,-6],[-2,5,-9,-9,6,-5,-4],[-4,-4,1,-7,-1,10,5],[-7,-6,8,-6,6,1,-7],[3,-5,8,-3,5,3,-6],[-1,6,-4,4,-6,10,-10],[-3,9,-6,4,-4,-2,7],[-2,8,-6,3,1,-3,-10]],[[6,-3,-6,-7,-7,-6,-8],[-9,-6,1,-6,2,-6,-9],[-9,-1,-8,6,-7,6,-1],[-4,-3,-7,-3,4,-5,9],[9,-2,8,5,-10,-1,1],[-10,10,-5,-6,-3,-1,10],[-5,-9,8,5,5,-1,-9],[1,-8,4,6,2,-2,-2],[-1,-6,1,3,7,3,-5],[8,-5,-8,9,-4,1,-6],[2,-5,10,9,9,1,9],[-9,-8,-10,5,7,-10,-8],[8,6,-5,3,4,-7,4],[-10,-9,7,5,10,7,-5]],[[-10,-10,8,8,-6,-9,5],[-3,1,1,-4,7,10,-1],[-7,-2,9,7,7,-1,6],[-3,-5,9,-2,7,-3,-5],[-2,-7,-3,7,-2,-9,2],[2,-1,1,5,-1,-2,-5],[3,-7,-8,-5,7,1,8],[10,10,-8,-9,7,8,-3],[6,-9,-7,5,5,4,-6],[1,5,-6,3,5,2,8],[-2,4,8,-9,2,-10,-8],[6,1,9,-9,10,8,8],[9,-2,6,1,1,-10,-5],[-9,7,6,5,4,8,-7]],[[-1,-8,10,3,8,-1,3],[-2,-2,-1,6,-6,3,-4],[6,-7,8,-9,-5,-6,8],[4,9,-10,-8,-1,-6,-7],[9,-10,-5,-1,-4,9,5],[-6,3,2,7,6,-3,-10],[-5,10,10,-8,8,-6,-10],[-6,4,-7,2,-10,1,2],[6,3,-1,-7,2,6,5],[-6,10,-9,2,1,5,-10],[-9,10,-8,-7,7,-10,9],[3,-7,-8,-9,-1,-3,4],[4,-6,-10,-8,-3,-5,-9],[1,10,-2,3,6,-7,2]],[[9,-1,1,8,6,-10,-3],[9,-2,1,-6,-1,-3,8],[5,-3,7,-7,-1,-2,3],[4,-8,7,7,2,-1,10],[-9,7,2,8,3,-10,2],[-1,-5,-10,-10,-3,-5,10],[-5,3,3,-7,9,4,1],[-8,7,6,4,5,3,1],[-2,-7,3,10,-9,1,-10],[-3,1,4,9,-10,-7,7],[4,9,10,2,5,9,8],[-5,-7,9,-8,-5,-2,9],[1,-9,-3,2,6,7,5],[7,-6,-2,-1,-10,-4,5]],[[10,-7,-10,-8,7,-4,-2],[-4,7,-10,6,-5,-3,-5],[9,-4,5,-10,10,-6,7],[-1,1,8,1,-10,-10,-3],[1,9,-9,9,-4,9,-8],[-4,6,-6,3,6,1,-10],[-2,-1,2,-5,3,-6,-6],[3,-1,8,4,-6,-5,-10],[6,-7,-2,5,10,-4,-7],[-10,-5,-6,-3,4,8,2],[-10,-2,-2,-9,7,10,-6],[-10,5,4,6,8,4,-5],[-2,8,1,2,-8,10,5],[-3,-4,-3,-5,-1,-7,-10]],[[-3,-5,-2,-10,-2,-8,3],[6,-10,10,3,5,10,-9],[-8,-2,-2,5,2,8,-8],[-2,4,3,-6,10,-6,-7],[2,7,-3,-1,6,2,1],[-9,6,-2,-9,6,7,5],[10,2,-8,-4,-8,9,-10],[1,10,-2,3,-7,-8,2],[-7,-1,-8,1,-1,-8,-7],[-4,-7,10,-7,2,-6,-6],[1,4,-4,-5,9,10,-10],[-1,-7,-5,10,-4,8,6],[-6,-10,10,-5,8,-7,-5],[-7,9,-3,2,3,-1,-6]],[[-2,3,-9,-2,-9,-3,8],[-4,-9,9,8,4,-8,-2],[1,-8,-4,-8,-3,10,-9],[9,-5,10,5,-1,9,-4],[10,6,6,4,-2,-1,-5],[9,5,1,2,-1,-1,9],[-8,7,-9,-1,4,2,-10],[-4,-5,-10,2,8,5,8],[-4,3,2,-1,-2,5,-10],[1,4,-8,8,-9,1,4],[-1,-9,-1,-8,-4,-5,3],[-2,9,-4,1,-1,-10,-1],[8,-7,10,-3,-2,-6,-9],[-3,-1,5,10,-10,-3,-10]]], dtype = "int32")#candidate|5054|(14, 14, 7)|const|int32
bop_5055 = relay.greater(var_5053.astype('bool'), relay.reshape(const_5054.astype('bool'), relay.shape_of(var_5053))) # shape=(14, 14, 7)
output = relay.Tuple([bop_5055,])
output2 = relay.Tuple([bop_5055,])
func_5062 = relay.Function([var_5053,], output)
mod['func_5062'] = func_5062
mod = relay.transform.InferType()(mod)
mutated_mod['func_5062'] = func_5062
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5063 = relay.var("var_5063", dtype = "int32", shape = (14, 14, 7))#candidate|5063|(14, 14, 7)|var|int32
func_5062_call = mutated_mod.get_global_var('func_5062')
call_5064 = func_5062_call(var_5063)
output = call_5064
func_5065 = relay.Function([var_5063], output)
mutated_mod['func_5065'] = func_5065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4344_call = mod.get_global_var('func_4344')
func_4345_call = mutated_mod.get_global_var('func_4345')
call_5086 = relay.TupleGetItem(func_4344_call(), 1)
call_5087 = relay.TupleGetItem(func_4345_call(), 1)
uop_5095 = relay.log(call_5086.astype('float64')) # shape=(864,)
uop_5097 = relay.log(call_5087.astype('float64')) # shape=(864,)
func_5062_call = mod.get_global_var('func_5062')
func_5065_call = mutated_mod.get_global_var('func_5065')
const_5101 = relay.const([-4,3,9,-10,9,2,-1,3,-8,-5,10,-2,7,2,-1,-1,-1,6,4,-10,2,-2,-5,-8,9,-1,-1,10,10,1,-10,-8,-9,-10,2,5,-6,-7,-1,-3,-8,-1,-5,9,2,7,-4,-4,1,7,8,7,8,2,-7,-2,-7,-6,-6,10,-8,-10,3,-7,-10,8,-6,-9,-7,6,5,-2,2,7,-4,-6,3,5,1,-2,6,-8,-5,7,-9,-9,-2,1,9,-2,6,-5,5,6,-4,7,-8,-4,-4,-6,-3,-1,4,-9,-1,-5,-10,-5,4,10,-10,10,4,3,-7,2,2,7,7,-10,-8,3,-7,4,4,1,-3,-3,7,4,5,-5,1,-4,7,-7,8,4,10,9,4,-9,-3,1,-8,-3,4,7,-10,-4,-4,-4,10,-8,-8,6,6,-6,-8,8,-3,-7,1,-2,7,-7,-6,-3,-9,-1,-9,6,4,6,-10,-8,-7,9,10,-8,7,10,-6,-4,-6,-3,-3,10,-2,9,-1,4,1,8,5,10,3,7,-3,-6,3,-3,8,-4,-2,-2,-8,-2,8,-2,-6,-4,2,-8,-10,5,-4,2,4,4,-8,10,1,-9,-10,1,-3,4,-4,-2,9,-2,6,6,-9,-7,-7,7,8,6,-4,5,1,7,-2,-2,6,5,-7,5,1,4,-8,-5,-6,-4,7,-10,-9,-4,5,3,9,7,-8,3,-4,-9,-10,9,-5,-6,2,-9,-4,3,8,-3,5,4,-10,-5,3,-7,6,9,-10,-4,-1,-5,-7,-4,-6,3,-7,-5,1,1,1,7,5,1,-10,-10,-7,8,3,10,-1,9,9,4,3,5,7,-3,9,10,6,-2,4,8,6,-5,10,-4,9,8,7,-5,-7,-9,-10,-8,10,1,2,1,7,4,1,4,-9,-9,-8,-3,1,-3,-4,9,-1,-7,-10,-2,4,2,-7,5,-1,-4,-9,3,-2,2,7,9,-2,2,5,-6,-1,4,7,6,4,-6,-9,-4,5,-5,7,-2,-10,-10,-10,4,9,1,-7,-3,-7,3,-9,-6,-1,1,-5,-9,-7,10,7,1,3,-1,9,1,-6,1,-1,2,-8,-2,-5,-7,-1,-2,-4,6,4,-10,-3,10,-5,-7,-8,8,3,8,-2,2,6,4,6,-9,-7,-7,10,-2,-8,3,7,1,-3,7,6,1,-3,1,-6,4,-9,-6,6,-6,-6,-10,2,2,-10,3,10,7,-10,5,-1,9,-9,3,-2,10,9,10,1,7,3,-5,-3,-8,-3,10,3,-5,4,-8,6,6,-9,-7,8,-10,-3,6,9,10,9,7,-1,4,2,-4,1,-6,-6,-1,-6,-7,-9,-4,1,2,7,-1,4,6,1,-6,9,3,4,2,-6,-8,6,-3,9,-4,-7,-5,-4,6,-10,-8,-4,-6,6,10,-9,-6,4,9,-5,10,-1,2,5,-1,-10,-5,9,-5,-1,6,5,4,-1,3,-9,-9,-9,8,-9,-8,-9,5,4,4,7,7,3,-1,8,4,8,-10,4,-10,8,-4,-3,-6,9,4,1,7,-5,-10,-4,-8,6,1,7,-5,-3,5,-7,3,-2,-3,-10,-7,-1,-6,1,-9,-4,-9,4,-10,-2,-1,6,7,4,-3,10,-7,-6,6,-9,-6,-7,-7,-8,6,-2,1,4,7,7,2,9,10,4,-5,-3,7,-4,9,-1,-4,-3,-2,2,-6,-9,-6,-10,6,-4,-9,1,-5,2,9,-10,-6,-7,-1,-10,-9,7,-1,-4,1,7,-3,7,3,3,-3,-6,-7,9,-3,-6,2,-8,10,-8,-9,2,5,-1,7,10,-8,-8,1,-4,-8,5,-6,1,-6,-7,-5,-7,8,-9,-2,4,-7,-5,-2,3,1,-8,-2,3,9,2,-8,-6,-7,-1,8,-10,-10,5,6,-9,-7,-2,-7,8,-4,2,1,10,7,-8,-1,-9,-5,-10,-2,6,8,-8,-4,3,-9,1,4,-8,5,5,-8,6,1,-4,6,2,-9,-1,9,10,10,5,-3,7,3,-5,-8,-4,-8,2,8,10,-4,-10,-4,10,10,-9,2,-4,-8,6,9,-5,-8,-10,8,-4,10,7,4,7,-3,-8,2,10,10,-6,-5,7,7,-2,9,9,-9,3,-6,-9,9,-3,-9,3,-10,10,1,1,-7,4,8,-5,-4,2,3,8,-9,4,-6,7,7,3,3,9,6,5,-9,-5,-1,2,8,-5,-10,5,8,-2,-7,5,1,-1,-9,3,9,2,2,-1,1,9,4,9,-6,-7,8,-7,7,-3,6,-4,-3,4,-8,8,-10,-5,3,-8,-5,-3,8,9,8,2,2,-9,-2,-10,8,2,-7,6,-10,-8,-9,7,1,-5,-2,4,-2,-6,-6,7,-6,-5,7,-4,4,-10,-5,4,-5,-4,5,8,3,-4,-10,-4,-1,1,10,2,7,1,-1,7,-4,-2,1,8,3,2,4,-2,-6,-2,-8,10,-8,-9,-4,8,7,6,-9,-1,-10,-10,8,-1,6,-1,-8,2,-2,9,-5,-3,-7,2,7,10,6,-4,-1,9,8,4,10,4,-6,7,1,6,1,4,1,7,-4,-2,-4,6,10,10,5,2,-8,-3,-1,7,-6,1,-4,3,-9,-7,-5,-7,-1,6,10,7,1,8,-8,-5,3,10,-6,7,7,10,-7,8,3,-5,-6,-2,-2,-8,-3,-3,-8,-6,-7,8,7,5,-5,1,8,3,-8,-10,5,-9,10,-7,-6,-3,-5,4,-8,-3,3,-3,10,7,-2,6,-7,-8,-8,7,7,4,10,-2,-8,-3,1,-4,-5,10,-9,5,-3,7,7,3,2,5,-7,10,4,-8,1,-9,-4,4,-7,-1,1,2,-2,1,4,3,3,-9,-9,5,7,-8,2,4,10,-10,5,-8,-8,-8,3,6,-7,4,-9,7,2,9,-9,3,-10,10,-4,-2,-5,7,-4,-5,-7,8,-9,-4,-2,5,3,1,-1,-9,-7,-9,1,-2,8,-7,-8,9,-2,8,-5,5,1,3,5,6,5,4,-9,3,4,2,-5,-9,5,10,8,-8,-1,10,-3,8,2,-3,10,10,-8,-6,-3,-9,-2,-8,6,1,5,3,-10,5,3,-4,-6,7,-7,8,-9,10,-5,2,-2,-9,4,6,-1,7,1,-8,-8,-2,1,-6,-6,-2,7,-4,-6,-8,3,6,5,1,-7,-4,8,-9,-5,-7,-3,3,2,-9,-10,-3,-10,-8,-4,-10,8,3,9,4,9,6,10,-2,-7,-3,9,-10,4,-2,7,-9,-8,-10,6,-3,-5,7,-6,-10,-9,10,8,6,5,2,2,6,4,6,-10,-3,6,2,8,-7,-4,6,6,-6,10,5,-9,-1,-9,-3,6,5,7,-7,9,3,-2,7,-8,1,3,1,6,-7,1,-3,-7,10,-6,-8,-3,-8,9,-3,10,-7,9,-5,10,-10,-3,7,-1,-3,-5,10,3,5,5,10,-1,8,-7,-6,6,-7,7,8,-2,-5,-3,7,4,7,9,3,-6,-3,-4,9,3,9,-9,-9,8,-10,-10,-5,10,-2,-3,2,-5,-2,1,1,9,-5,-6,1,-10,-5,1,-3,-5,-1,-1,8,7,-7,3,-6,9,-1,6,1,5,6,-7,9,5], dtype = "int32")#candidate|5101|(1372,)|const|int32
call_5100 = relay.TupleGetItem(func_5062_call(relay.reshape(const_5101.astype('int32'), [14, 14, 7])), 0)
call_5102 = relay.TupleGetItem(func_5065_call(relay.reshape(const_5101.astype('int32'), [14, 14, 7])), 0)
output = relay.Tuple([uop_5095,call_5100,const_5101,])
output2 = relay.Tuple([uop_5097,call_5102,const_5101,])
func_5118 = relay.Function([], output)
mod['func_5118'] = func_5118
mod = relay.transform.InferType()(mod)
output = func_5118()
func_5119 = relay.Function([], output)
mutated_mod['func_5119'] = func_5119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1858_call = mod.get_global_var('func_1858')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_5178 = relay.TupleGetItem(func_1858_call(), 0)
call_5179 = relay.TupleGetItem(func_1859_call(), 0)
output = call_5178
output2 = call_5179
func_5211 = relay.Function([], output)
mod['func_5211'] = func_5211
mod = relay.transform.InferType()(mod)
output = func_5211()
func_5212 = relay.Function([], output)
mutated_mod['func_5212'] = func_5212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3909_call = mod.get_global_var('func_3909')
func_3911_call = mutated_mod.get_global_var('func_3911')
call_5236 = relay.TupleGetItem(func_3909_call(), 0)
call_5237 = relay.TupleGetItem(func_3911_call(), 0)
func_4500_call = mod.get_global_var('func_4500')
func_4505_call = mutated_mod.get_global_var('func_4505')
const_5239 = relay.const([-4.473523,0.255484,-9.127996,-0.755112,0.017597,1.634488,-2.743647,4.165069,-1.954667,-3.398596,6.823778,-3.406699,4.570155,-0.632765,-2.379360,2.712454,5.601964,1.007566,5.998538,4.231115,6.317457,8.630568,-4.096866,-3.928590,-7.302968,3.214629,-3.583011,-5.439623,9.583555,-1.087479,-4.653754,-0.952048,9.029196,-2.479109,0.754945,4.443358,-3.385034,-6.691470,6.712568,6.487244,-3.360728,-7.085221,-3.566355,-6.570571,3.854715,-1.885069,-7.543056,1.157524,-1.542508,6.946134,8.686203,-5.766139,2.037734,1.872522,-4.452279,-9.060535,4.384255,5.951699,-0.812678,3.243316], dtype = "float64")#candidate|5239|(60,)|const|float64
const_5240 = relay.const([[-10],[3],[2],[4],[4],[-8],[-2],[6],[8],[-1],[-5],[10],[4],[-6],[9],[8],[-5],[-3],[-1],[-8],[7],[-10],[6],[5],[1],[5],[-10],[8],[8],[-9],[-1],[6],[8],[-2],[6],[-5],[-8],[2],[-3],[8],[-4],[4],[7],[-7],[3],[1],[1],[-2],[9],[-9],[6],[10],[1],[9],[-10],[9],[-9],[5],[4],[-2],[8],[-3],[-3],[7],[10],[6],[9],[1],[-7],[-5],[-7],[-8],[-9],[6],[-7],[-10],[-2],[-3],[9],[6],[7],[5],[-8],[-6],[-7],[2],[5],[-4],[-7],[10],[7],[-8],[-5],[5],[-2],[-1],[-4],[4],[3],[9],[-3],[5],[4],[-4],[10],[-4],[6],[-7],[6],[4],[4],[6],[-2],[-2],[-4],[-6],[-3],[-7],[-10],[8],[7],[-8],[-8],[3],[-6],[10],[2],[10],[10],[-10],[2],[-3],[7],[-1],[-5],[9],[-3],[-6],[-2],[2],[5],[2],[2],[1],[3],[-8],[9],[9],[1],[5],[1],[9],[-2],[4],[1],[-6],[10],[4],[-9],[3],[8],[6],[-3],[3],[8],[-10],[-5],[2],[4],[-3],[-10],[1],[-6],[-1],[2],[6],[5],[9],[-10],[-4],[2],[5],[4],[7],[1],[-1],[1],[-2],[-9],[-2],[9],[4],[2],[4],[6],[10],[3],[-9],[5],[3],[6],[-9],[-7],[3],[-6],[-8],[-3],[-2],[6],[8],[-5],[3],[-6],[-3],[8],[6],[-9],[10],[8],[4],[6],[-2],[6],[7],[10],[-5],[-6],[3],[1],[-4],[9],[3],[-7],[-5],[-4],[-10],[5],[-3],[-5],[-5],[6],[2],[-10],[-5],[-10],[-2],[-8],[-8],[-7],[9],[-4],[-6],[-2],[1],[7],[-6],[6],[6],[-2],[9],[-9],[10],[5],[10],[3],[-5],[-8],[-7],[8],[-10],[4],[2],[4],[5],[9],[10],[4],[-5],[10],[-1],[5],[-3],[7],[-5],[-9],[-3],[-1],[-2],[3],[2],[1],[1],[-4],[6],[-10],[-10],[-5],[9],[-4],[-8],[-1],[6],[6],[-8],[-5],[-2],[-4],[4],[7],[-3],[-7],[5],[-5],[-3],[-3],[2],[3],[-8],[5],[-1],[-8],[-7],[-6],[-2],[10],[-4],[-8],[8],[-5],[2],[3],[-2],[1],[-9],[-5],[7],[3],[-10],[4],[6],[7],[1],[-8],[1],[-2],[-1],[-9],[5],[-10],[6],[-5],[1],[-6],[9],[-2],[6],[-4],[7],[5],[-5],[-4],[-4],[-9],[3],[-1],[7],[2],[6],[-8],[10],[9],[-1],[10],[-4],[9],[4],[8],[-4],[-6],[4],[-8],[5],[-8],[7],[-5],[10],[-2],[6],[-1],[9],[-10],[3],[2],[2],[-6],[5],[-9],[5],[-1],[-7],[-1],[10],[-8],[-5],[5],[-10],[8],[4],[5],[-10],[-4],[7],[7],[-3],[4],[7],[-7],[-9],[3],[5],[-10],[4],[10],[-10],[6],[6],[-4],[5],[4],[-2],[-10],[-4],[-5],[-1],[6],[6],[-8],[-4],[10],[3],[-5],[-8],[-1],[10],[5],[-4],[10],[1],[10],[2],[5],[-2],[8],[-3],[-1],[6],[5],[-4],[-9],[4],[6],[-8],[-5],[-2],[8],[-10],[3],[7],[-9],[2],[7],[7],[2],[-10],[6],[4],[1],[10],[8],[2],[-9],[-8],[-8],[6],[5],[9],[-7],[-4],[6],[9],[-8],[-5],[4],[9],[-1],[-9],[-7],[3],[-2],[-1],[6],[-9],[-6],[2],[-8],[3],[-8],[7],[6],[-6],[-8],[7],[2],[9],[8],[2],[-1],[9],[-5],[9],[-5],[-1],[3],[-5],[-5],[7],[-7],[-9],[6],[-4],[-9],[2],[-1],[-7],[-3],[-2],[-1],[1],[1],[2],[-8],[9],[7],[6],[-7],[10],[9],[6],[-5],[8],[1],[8],[1],[5],[-9],[9],[-8],[-5],[-8],[8],[1],[9],[-10],[-2],[2],[-2],[-8],[-5],[2],[-2],[-7],[-8],[-9],[9],[2],[-3],[5],[-5],[-9],[-1],[4],[3],[6],[10],[10],[-8],[-5],[3],[9],[-3],[9],[-6],[-8],[-3],[-5],[-9],[8],[1],[-2],[1],[-7],[8],[-3],[-5],[-2],[5],[-4],[8],[-1],[8],[-5],[-5],[9],[-6],[-8],[-2],[6],[-6],[10],[3],[-10],[3],[-7],[-6],[4],[-4],[-3],[4],[4],[-4],[9],[-9],[7],[-3],[-7],[-8],[3],[2],[6],[10],[-4],[-1],[-5],[10],[4],[-4],[-1],[7],[-8],[-6],[7],[1],[7],[3],[1],[-3],[10],[-1],[-8],[-6],[4],[-7],[-5],[-2],[5],[8],[-2],[-3],[4],[4],[9],[-2],[3],[4],[6],[-8],[-2],[-5],[9],[9],[-5],[-7],[10],[10],[4],[-9],[3],[-2],[7],[-10],[7],[-1],[-2],[5],[-6],[-7],[-3],[-10],[4],[7],[3],[-1],[-7],[3],[-8],[-5],[8],[4],[-6],[1],[-3],[-3],[-3],[-1],[4],[-3],[2],[-3],[8],[5],[8],[2],[9],[6],[-5],[5],[5],[6],[4],[3],[5],[-7],[1],[-8],[-8],[6],[2],[-2],[4],[-6],[4],[8],[-1],[5],[4],[-5],[5],[6],[2],[6],[6],[3],[-10],[10],[-2],[-4],[8],[-6],[-6],[8],[9],[7],[-3],[-2],[6],[2],[10],[9],[-4],[-5],[-5],[-5],[-10],[-6],[1],[6],[-5],[-6],[7],[-3],[7],[-4],[-5],[-8],[-4],[-5],[1],[4],[8],[10],[1],[-1],[-1],[5],[4],[1],[-5],[10],[-10],[7],[3],[-4],[10],[8],[7],[-9],[-1],[7],[7],[10],[-3],[-3],[-5],[-8],[-1],[-8],[-7],[-9],[-10],[8],[4],[-10],[-8],[-9],[-2],[-6],[-7],[1],[4],[-7],[-6],[-1],[9],[1],[8],[9],[-7],[-7],[7],[-7],[4],[-1],[-2],[4],[-4],[3],[6],[-5],[4],[6],[-5],[4],[-5],[4],[6],[10],[7],[-10],[8],[5],[5],[-3],[1],[-7],[4],[-9],[-10],[9],[-3],[-7],[8],[-10],[1],[-4],[-3],[2],[-8],[-2],[3],[-6],[-3],[-3],[7],[8],[9],[-10],[5],[10],[9],[6],[4],[4],[2],[-10],[3],[9],[-10],[-1],[-6],[-6],[6],[-2],[5],[10],[7],[-8],[5],[2],[5],[-4],[10],[6],[-8],[9],[-8],[1],[-3],[7],[-4],[-2],[5],[9],[-1],[1],[4],[6],[-1],[-6],[-1],[-4],[-1],[5],[5],[-2],[10],[-7],[3],[9],[6],[-9],[5],[6],[2],[-4],[-8],[4],[-1],[-3],[-2],[5],[-8],[-1],[8],[-4],[1],[-7],[-1],[-2],[-7],[-5],[-5],[4],[7],[-4],[2],[-3],[2],[9],[5],[6],[-9],[10],[-8],[-2],[-1],[7],[8],[-3],[9],[-6],[-9],[-1],[-4],[-2],[-6],[-4],[-3],[-4],[9],[3],[-4],[7],[4],[-7],[-9],[3],[-3],[-10],[-7],[-7],[-3],[7],[-5],[7],[8],[5],[10],[2],[-4],[-6],[3],[5],[-6],[-2],[-9],[7],[7],[-8],[-8],[10],[2],[-5],[-7],[-10],[-7],[6],[-8],[3],[-7],[-10],[-5],[-6],[2],[7],[-8],[-5],[2],[7],[-9],[2],[3],[-6],[-10],[6],[6],[-4],[4],[3],[6],[5],[7],[-4],[-10],[-10],[-6],[-4],[2],[-10],[1],[-2],[4],[7],[-5],[-2],[-2],[-3],[-9],[-10],[8],[9],[-4],[-4],[5],[1],[-2],[2],[-8],[-1],[-9],[4],[-2],[-10],[5],[-3],[2],[8],[-6],[-2],[-6],[6],[7],[-1],[-7],[8],[5],[-9],[8],[-1],[1],[-6],[3],[9],[-4],[-10],[-4],[-6],[4],[-4],[10],[-1],[3],[-6],[-1],[-3],[-9],[5],[1],[-3],[3],[-7],[10],[7],[-3],[-9],[4],[-9],[-9],[-9],[-2],[-3],[1],[2],[2],[-9],[9],[-3],[9],[4],[-3],[-6],[10],[6],[-2],[10],[-7],[-2],[-10],[10],[-2],[-8],[-5],[9],[-3],[8],[6],[4],[1],[5],[-7],[7],[7],[4],[-6],[9],[5],[10],[-10],[-6],[3],[-10],[-1],[-5],[8],[-6],[-5],[9],[-4],[9],[-7],[-9],[-6],[4],[9],[-1],[-7],[-1],[7],[9],[-8],[-10],[-9],[6],[4],[-3],[-4],[5],[1],[-7],[9],[-5],[9],[3],[4],[3],[10],[-6],[4],[2],[9],[-9],[8],[-2],[3],[-1],[9],[9],[4],[6],[-7],[-9],[-2],[-7],[8],[4],[-5],[-10],[-9],[5],[-4],[-4],[-4],[3],[-8],[-5],[7],[3],[-10],[-8],[10],[-8],[7],[1],[2],[7],[2],[-1],[6],[-4],[2],[-9],[-3],[2],[3],[-4],[4],[-9],[1],[8],[-3],[1],[6],[-4],[7],[-9],[9],[-2],[10],[-6],[4],[7],[3],[10],[3],[-7],[-2],[-6],[4],[5],[9],[-2],[1],[1],[-6],[6],[10],[-9],[-9],[-6],[6],[1],[-6],[10],[-8],[-9],[8],[7],[5],[-3],[-8],[10],[-2],[8],[-7],[-6],[-10],[5],[-3],[-5],[-2],[9],[-8],[-1],[6],[-4],[5],[-2],[-5],[10],[7],[-9],[2],[-4],[-10],[7],[-3],[-2],[-7],[-4],[9],[9],[3],[2],[-2],[-2],[-8],[-7],[-4],[5],[-9],[-6],[1],[5],[-2],[-2],[8],[6],[-1],[-9],[-1],[-1],[3],[-9],[-8],[-1],[-9],[1],[-4],[9],[-5],[9],[-10],[-7],[5],[3],[9]], dtype = "uint8")#candidate|5240|(1365, 1)|const|uint8
call_5238 = relay.TupleGetItem(func_4500_call(relay.reshape(const_5239.astype('float64'), [10, 2, 3]), relay.reshape(const_5239.astype('float64'), [10, 2, 3]), relay.reshape(const_5240.astype('uint8'), [1365,]), ), 5)
call_5241 = relay.TupleGetItem(func_4505_call(relay.reshape(const_5239.astype('float64'), [10, 2, 3]), relay.reshape(const_5239.astype('float64'), [10, 2, 3]), relay.reshape(const_5240.astype('uint8'), [1365,]), ), 5)
output = relay.Tuple([call_5236,call_5238,const_5239,const_5240,])
output2 = relay.Tuple([call_5237,call_5241,const_5239,const_5240,])
func_5253 = relay.Function([], output)
mod['func_5253'] = func_5253
mod = relay.transform.InferType()(mod)
output = func_5253()
func_5254 = relay.Function([], output)
mutated_mod['func_5254'] = func_5254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4790_call = mod.get_global_var('func_4790')
func_4792_call = mutated_mod.get_global_var('func_4792')
call_5302 = relay.TupleGetItem(func_4790_call(), 0)
call_5303 = relay.TupleGetItem(func_4792_call(), 0)
func_4773_call = mod.get_global_var('func_4773')
func_4775_call = mutated_mod.get_global_var('func_4775')
call_5304 = relay.TupleGetItem(func_4773_call(), 0)
call_5305 = relay.TupleGetItem(func_4775_call(), 0)
output = relay.Tuple([call_5302,call_5304,])
output2 = relay.Tuple([call_5303,call_5305,])
func_5314 = relay.Function([], output)
mod['func_5314'] = func_5314
mod = relay.transform.InferType()(mod)
output = func_5314()
func_5315 = relay.Function([], output)
mutated_mod['func_5315'] = func_5315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3379_call = mod.get_global_var('func_3379')
func_3380_call = mutated_mod.get_global_var('func_3380')
call_5352 = relay.TupleGetItem(func_3379_call(), 0)
call_5353 = relay.TupleGetItem(func_3380_call(), 0)
output = relay.Tuple([call_5352,])
output2 = relay.Tuple([call_5353,])
func_5390 = relay.Function([], output)
mod['func_5390'] = func_5390
mod = relay.transform.InferType()(mod)
output = func_5390()
func_5391 = relay.Function([], output)
mutated_mod['func_5391'] = func_5391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2031_call = mod.get_global_var('func_2031')
func_2033_call = mutated_mod.get_global_var('func_2033')
call_5440 = relay.TupleGetItem(func_2031_call(), 0)
call_5441 = relay.TupleGetItem(func_2033_call(), 0)
output = relay.Tuple([call_5440,])
output2 = relay.Tuple([call_5441,])
func_5442 = relay.Function([], output)
mod['func_5442'] = func_5442
mod = relay.transform.InferType()(mod)
mutated_mod['func_5442'] = func_5442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5442_call = mutated_mod.get_global_var('func_5442')
call_5443 = func_5442_call()
output = call_5443
func_5444 = relay.Function([], output)
mutated_mod['func_5444'] = func_5444
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5480 = relay.const([[[0.472027,-2.001797],[5.294371,1.334929],[7.414500,7.690665],[6.124598,3.256114],[9.305380,1.442556],[-9.699946,-7.222880],[-6.011287,5.058502],[-9.090831,-9.616651],[0.936358,4.316545],[-2.763568,-6.515714],[0.068930,-6.442825],[9.173306,3.432570],[-0.297150,2.192728],[7.087581,-7.010846],[-9.098143,-4.077238],[-9.204187,-9.130632]],[[1.516361,-1.288222],[7.274486,2.507273],[4.473907,9.033772],[5.810148,4.269672],[5.792446,2.271350],[-4.191807,-7.159986],[2.772038,6.209598],[-3.231833,-8.692451],[1.458339,6.017908],[0.757640,7.788733],[-0.203915,4.399840],[-6.043337,-5.808854],[-9.746817,-0.423328],[2.703003,8.561711],[9.664002,4.739555],[4.751160,2.704115]],[[-4.255079,6.998540],[3.637274,-6.608432],[9.679435,3.833233],[7.448718,9.228217],[3.459342,-9.754402],[-6.269689,-9.232159],[4.284381,1.023210],[7.363091,9.647252],[-3.776749,0.300363],[-0.259064,3.453700],[8.401525,1.670422],[-9.563356,-9.992100],[-0.965101,2.831578],[5.039527,-6.549510],[6.397470,4.600937],[-3.501963,-3.741666]],[[0.440420,-8.384537],[-9.332580,7.980953],[-7.471205,-7.780409],[3.904540,9.927614],[1.157465,-4.197097],[-0.458981,3.300985],[5.460845,-9.934781],[-3.677148,-4.544360],[-5.457491,0.140637],[-7.982336,-9.367720],[3.329528,-7.338340],[-6.432477,-7.729757],[-8.807486,-4.292933],[6.357976,-6.716895],[-2.554519,-4.141874],[6.457106,-3.176709]],[[2.332057,-6.911387],[-9.109678,-9.642757],[2.746470,-5.190526],[-3.869868,-1.393381],[6.615343,7.583134],[-4.235129,6.409886],[-2.390905,8.492526],[-1.333039,9.793790],[2.704828,-2.495563],[4.896083,4.592886],[7.328401,-9.319419],[-5.923152,-8.781947],[4.401130,-7.103395],[5.192600,-2.800164],[7.433492,0.651404],[1.786865,0.550752]]], dtype = "float64")#candidate|5480|(5, 16, 2)|const|float64
uop_5481 = relay.tan(const_5480.astype('float64')) # shape=(5, 16, 2)
bop_5486 = relay.floor_mod(uop_5481.astype('float64'), relay.reshape(const_5480.astype('float64'), relay.shape_of(uop_5481))) # shape=(5, 16, 2)
const_5490 = relay.const([[[-9.741841,-8.732035],[-0.414703,-3.071386],[4.404894,4.475003],[8.800941,-7.027346],[-3.488819,-4.310330],[-0.328428,8.360001],[-2.776088,-9.290438],[5.777865,5.483672],[5.164375,1.553277],[-9.130013,-1.395350],[-6.223390,-2.134297],[2.403700,-2.276497],[-9.708195,-1.674742],[-1.639340,7.972947],[-0.811868,3.914601],[4.150245,5.612622]],[[-4.034797,-3.575494],[-2.938189,-9.460251],[5.796588,0.564867],[5.611708,-5.331140],[-9.161144,-6.408480],[-7.251001,9.122599],[-9.775444,-9.678147],[3.196347,-4.767157],[-3.173460,-9.326930],[2.372510,2.451139],[1.718452,-4.801024],[6.771556,-4.116686],[8.272969,-1.571855],[-4.211427,4.116805],[-2.869132,-5.350095],[9.520544,-3.261148]],[[-5.891386,5.940054],[9.113242,-9.981094],[1.163638,-0.736006],[6.398799,-4.051956],[4.978584,-3.259476],[-6.179539,-1.458787],[5.136610,9.054217],[7.292015,-0.094030],[-0.892425,-4.285489],[-0.423941,9.888182],[1.745152,-2.982570],[-6.355448,5.850865],[2.864573,-2.324611],[3.003374,1.765648],[6.372614,-0.254362],[-4.740904,-2.732064]],[[-5.993271,-1.679632],[0.831568,-6.863478],[5.848990,0.182066],[6.321645,-0.959731],[-6.958140,-9.161674],[2.554124,-1.552876],[-6.378442,-0.521774],[0.357168,-8.365504],[8.704402,3.264600],[-9.922949,4.513581],[-7.484563,1.772397],[2.489510,1.638178],[-6.589787,-3.708050],[3.508961,2.062502],[7.129492,-8.387574],[-6.998078,-6.546844]],[[1.413603,8.624193],[1.798410,-4.024548],[3.400565,3.986173],[6.090351,5.377071],[-2.762520,9.537301],[-8.073445,-7.489828],[-7.163298,2.889108],[9.461201,-3.950324],[7.374944,-5.436626],[-9.871442,-0.683022],[-7.040699,3.190204],[-4.635239,-5.644894],[-1.159834,-0.078728],[-8.185160,-6.192434],[0.796642,2.731419],[9.713749,-6.759666]]], dtype = "float64")#candidate|5490|(5, 16, 2)|const|float64
bop_5491 = relay.less_equal(const_5480.astype('bool'), relay.reshape(const_5490.astype('bool'), relay.shape_of(const_5480))) # shape=(5, 16, 2)
output = relay.Tuple([bop_5486,bop_5491,])
output2 = relay.Tuple([bop_5486,bop_5491,])
func_5500 = relay.Function([], output)
mod['func_5500'] = func_5500
mod = relay.transform.InferType()(mod)
mutated_mod['func_5500'] = func_5500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5500_call = mutated_mod.get_global_var('func_5500')
call_5501 = func_5500_call()
output = call_5501
func_5502 = relay.Function([], output)
mutated_mod['func_5502'] = func_5502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1574_call = mod.get_global_var('func_1574')
func_1575_call = mutated_mod.get_global_var('func_1575')
call_5516 = relay.TupleGetItem(func_1574_call(), 0)
call_5517 = relay.TupleGetItem(func_1575_call(), 0)
func_2586_call = mod.get_global_var('func_2586')
func_2588_call = mutated_mod.get_global_var('func_2588')
call_5526 = func_2586_call()
call_5527 = func_2586_call()
func_2476_call = mod.get_global_var('func_2476')
func_2478_call = mutated_mod.get_global_var('func_2478')
call_5528 = func_2476_call()
call_5529 = func_2476_call()
func_1235_call = mod.get_global_var('func_1235')
func_1237_call = mutated_mod.get_global_var('func_1237')
call_5530 = func_1235_call()
call_5531 = func_1235_call()
output = relay.Tuple([call_5516,call_5526,call_5528,call_5530,])
output2 = relay.Tuple([call_5517,call_5527,call_5529,call_5531,])
func_5537 = relay.Function([], output)
mod['func_5537'] = func_5537
mod = relay.transform.InferType()(mod)
output = func_5537()
func_5538 = relay.Function([], output)
mutated_mod['func_5538'] = func_5538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3016_call = mod.get_global_var('func_3016')
func_3018_call = mutated_mod.get_global_var('func_3018')
call_5664 = relay.TupleGetItem(func_3016_call(), 0)
call_5665 = relay.TupleGetItem(func_3018_call(), 0)
output = call_5664
output2 = call_5665
func_5666 = relay.Function([], output)
mod['func_5666'] = func_5666
mod = relay.transform.InferType()(mod)
mutated_mod['func_5666'] = func_5666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5666_call = mutated_mod.get_global_var('func_5666')
call_5667 = func_5666_call()
output = call_5667
func_5668 = relay.Function([], output)
mutated_mod['func_5668'] = func_5668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3105_call = mod.get_global_var('func_3105')
func_3107_call = mutated_mod.get_global_var('func_3107')
call_5713 = func_3105_call()
call_5714 = func_3105_call()
func_3163_call = mod.get_global_var('func_3163')
func_3164_call = mutated_mod.get_global_var('func_3164')
call_5718 = func_3163_call()
call_5719 = func_3163_call()
func_2265_call = mod.get_global_var('func_2265')
func_2267_call = mutated_mod.get_global_var('func_2267')
call_5728 = relay.TupleGetItem(func_2265_call(), 2)
call_5729 = relay.TupleGetItem(func_2267_call(), 2)
func_158_call = mod.get_global_var('func_158')
func_163_call = mutated_mod.get_global_var('func_163')
const_5737 = relay.const([[True,False,True,True,True,True,True,False,True,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False,False,False,False,True,False,True,False,True,True,True,True,False,False,False,True,True,True,False,True,False,False,True,False,False,True,False,True,True,True,True,True,True,True,True,True,False,False,True,True,False,False,False,False,False,False,True,True,False,False,True,False,False,False,False,False,True,True,True,True,False,False,False,True,False,False,False,False,False,True,True,False,True,False,True,True,False,False,True,False,False,False,True,False,False,True,True,False,False,False,True,False,True,True,False,True,True,False,True,False,False,False,False,True,False,True,True,True,False,False,True,False,False,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,False,False,False,True,False,False,True,True,False,True,False,False,True,False,True,False,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,False,False,False,False,False,False,True,True,False,False,True,False,False,True,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,True,True,True,False,True,False,True,True,False,True,False,False,False,True,False,False,True,True,False,True,False,True,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,True,False,False,False,False,True,False,False,True,True,True,True,True,False,True,False,True,False,False,True,True,False,True,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False,False,False,True,False,True,False,False,False,True,True,True,True,True,False,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,True,False,False,False,False,True,False,False,True,True,False,False,False,True,False,True,True,True,True,True,True,False,True,False,False,False,True,False,True,False,False,False,False,False,False,False,True,True,True,False,False,True,True,True,False,True,False,True,True,False,False,False,False,True,False,True,False,True,True,True,True,True,False,False,True,False,False,False,True,True,False,False,False,True,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,False,False],[True,True,False,True,True,True,False,True,True,False,True,False,False,False,False,True,False,True,True,True,True,True,False,True,False,False,False,False,True,False,False,True,True,False,False,False,False,False,True,True,False,False,False,False,False,False,False,False,False,True,True,True,False,True,True,False,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,False,True,True,False,True,True,False,True,True,True,True,True,True,False,False,False,False,True,False,False,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,False,False,True,False,True,True,False,True,True,True,True,False,False,True,False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,False,False,True,True,True,False,False,True,False,False,False,True,True,False,False,True,False,True,True,False,False,False,True,False,True,True,False,True,True,True,True,False,False,False,True,True,False,True,False,True,True,False,False,True,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False,False,False,False,False,False,True,False,False,True,False,True,True,False,False,True,False,True,True,False,False,False,True,False,True,False,True,True,False,False,False,False,False,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True,False,True,True,True,True,False,True,False,True,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,False,False,False,True,True,True,True,False,False,False,True,True,True,True,True,True,True,True,False,False,True,False,True,True,True,True,True,True,True,False,True,True,False,True,False,True,False,False,True,False,False,True,True,True,False,False,False,True,True,False,False,True,True,True,False,False,True,True,False,False,False,True,True,False,False,True,False,False,True,True,False,False,False,False,True,False,False,False,False,False,False,False,True,True,True,True,False,False,False,False,False,False,True,True,True,True,True,True,True,False,False,True,False,True,True,False,True,False,False,True,False,False,True,True,False,True,False,False,True,False,False,False,True,True,True,False,False,False,True,True]], dtype = "bool")#candidate|5737|(2, 432)|const|bool
call_5736 = relay.TupleGetItem(func_158_call(relay.reshape(const_5737.astype('bool'), [9, 8, 12]), relay.reshape(const_5737.astype('bool'), [9, 8, 12]), relay.reshape(call_5728.astype('int16'), [1248, 1]), ), 3)
call_5738 = relay.TupleGetItem(func_163_call(relay.reshape(const_5737.astype('bool'), [9, 8, 12]), relay.reshape(const_5737.astype('bool'), [9, 8, 12]), relay.reshape(call_5728.astype('int16'), [1248, 1]), ), 3)
output = relay.Tuple([call_5713,call_5718,call_5728,call_5736,const_5737,])
output2 = relay.Tuple([call_5714,call_5719,call_5729,call_5738,const_5737,])
func_5739 = relay.Function([], output)
mod['func_5739'] = func_5739
mod = relay.transform.InferType()(mod)
output = func_5739()
func_5740 = relay.Function([], output)
mutated_mod['func_5740'] = func_5740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3554_call = mod.get_global_var('func_3554')
func_3556_call = mutated_mod.get_global_var('func_3556')
call_5743 = relay.TupleGetItem(func_3554_call(), 0)
call_5744 = relay.TupleGetItem(func_3556_call(), 0)
func_1307_call = mod.get_global_var('func_1307')
func_1309_call = mutated_mod.get_global_var('func_1309')
const_5755 = relay.const([-0.113595,-2.851442,5.428114,-0.350763,-5.012870,8.636853,4.219627,8.763016,-5.325560,-7.900821,-3.678942,7.997749,-7.069221,7.647370,-5.269885,-2.671234,2.973452,-9.863878,2.122787,-4.297229,5.068077,4.748778,2.891705,-4.487620,-5.965682,-7.543119,-7.507331,2.191372,5.274502,-4.448387,-3.315089,-4.688979,-1.938090,-1.227186,4.689330,0.158493,-9.244996,9.446244,0.907365,8.591567,-7.717665,-2.155685,-1.312389,0.912306,-8.860933,4.549975,3.976056,-7.655606,-1.994498,7.651264,-3.269262,3.631505,7.719966,-9.618516,-6.832109,-4.386579,-8.975654,-4.923646,1.586754,-8.873752,7.346561,-8.254351,-1.977270,-7.913301,3.814448,-7.421879,-1.285477,-7.444924,3.219085,-5.636506,2.121655,-1.770324,-2.034835,-3.089114,4.496827,5.508744,-3.430441,3.618364,8.322211,-7.056464,1.581922,-7.910928,-9.446082,8.534694,6.861980,4.518057,0.248422,-6.895981,-0.619671,7.063388,-8.584785,3.414979,-0.939152,9.826572,-7.849070,-6.143794,-2.437110,-5.256373,0.524903,-2.613644,3.846447,5.590099,-0.288843,-9.955220,-1.560534,-8.394445,1.640612,-6.192499,-2.956104,8.256711,6.829724,-8.404357,-5.031365,-6.455417,-3.659598,-5.761593,-2.245915,-9.060492,-6.939860,-9.491043,-4.614710,0.357663,-7.409505,9.187271,8.687537,3.403236,-6.455330,-8.806367,-7.554172,9.226569,-4.305194,4.626782,0.470230,9.030511,-1.585229,3.860802,-4.246271,-2.877625,-5.257366,9.830938,-2.156274,-8.357016,-1.324578,5.357049,6.811184,2.896137,4.055246,-2.008605,4.580443,-3.031110,3.607050,-4.175715,-1.394708,-4.331619,0.668037,-9.912611,4.748541,-6.182946,3.841437,-3.363528,-2.028496,-4.876471,-2.969714,7.878925,-5.841811,-0.024357,6.386901,4.145821,7.986652,-7.716306,4.517708,1.477126,1.241792,-9.880211,7.945697,1.627602,0.254295,8.426504,-0.703161,9.738785,-1.747006,4.756935,-1.819434,9.581818,-8.857546,-3.665655,-2.687836,-3.005887,-7.582202,2.824639,-7.992157,5.597362,-2.667913,7.809947,7.445397,-1.058962,-2.948110,6.420452], dtype = "float64")#candidate|5755|(198,)|const|float64
call_5754 = relay.TupleGetItem(func_1307_call(relay.reshape(const_5755.astype('float64'), [6, 11, 3])), 0)
call_5756 = relay.TupleGetItem(func_1309_call(relay.reshape(const_5755.astype('float64'), [6, 11, 3])), 0)
bop_5757 = relay.mod(const_5755.astype('float64'), relay.reshape(call_5754.astype('float64'), relay.shape_of(const_5755))) # shape=(198,)
bop_5760 = relay.mod(const_5755.astype('float64'), relay.reshape(call_5756.astype('float64'), relay.shape_of(const_5755))) # shape=(198,)
output = relay.Tuple([call_5743,bop_5757,])
output2 = relay.Tuple([call_5744,bop_5760,])
func_5769 = relay.Function([], output)
mod['func_5769'] = func_5769
mod = relay.transform.InferType()(mod)
output = func_5769()
func_5770 = relay.Function([], output)
mutated_mod['func_5770'] = func_5770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3686_call = mod.get_global_var('func_3686')
func_3687_call = mutated_mod.get_global_var('func_3687')
call_5781 = func_3686_call()
call_5782 = func_3686_call()
output = call_5781
output2 = call_5782
func_5783 = relay.Function([], output)
mod['func_5783'] = func_5783
mod = relay.transform.InferType()(mod)
mutated_mod['func_5783'] = func_5783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5783_call = mutated_mod.get_global_var('func_5783')
call_5784 = func_5783_call()
output = call_5784
func_5785 = relay.Function([], output)
mutated_mod['func_5785'] = func_5785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3016_call = mod.get_global_var('func_3016')
func_3018_call = mutated_mod.get_global_var('func_3018')
call_5795 = relay.TupleGetItem(func_3016_call(), 0)
call_5796 = relay.TupleGetItem(func_3018_call(), 0)
output = relay.Tuple([call_5795,])
output2 = relay.Tuple([call_5796,])
func_5797 = relay.Function([], output)
mod['func_5797'] = func_5797
mod = relay.transform.InferType()(mod)
output = func_5797()
func_5798 = relay.Function([], output)
mutated_mod['func_5798'] = func_5798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2311_call = mod.get_global_var('func_2311')
func_2313_call = mutated_mod.get_global_var('func_2313')
call_5864 = func_2311_call()
call_5865 = func_2311_call()
func_858_call = mod.get_global_var('func_858')
func_861_call = mutated_mod.get_global_var('func_861')
var_5881 = relay.var("var_5881", dtype = "uint8", shape = (1365,))#candidate|5881|(1365,)|var|uint8
call_5880 = relay.TupleGetItem(func_858_call(relay.reshape(var_5881.astype('uint8'), [13, 7, 15])), 1)
call_5882 = relay.TupleGetItem(func_861_call(relay.reshape(var_5881.astype('uint8'), [13, 7, 15])), 1)
output = relay.Tuple([call_5864,call_5880,var_5881,])
output2 = relay.Tuple([call_5865,call_5882,var_5881,])
func_5885 = relay.Function([var_5881,], output)
mod['func_5885'] = func_5885
mod = relay.transform.InferType()(mod)
var_5886 = relay.var("var_5886", dtype = "uint8", shape = (1365,))#candidate|5886|(1365,)|var|uint8
output = func_5885(var_5886)
func_5887 = relay.Function([var_5886], output)
mutated_mod['func_5887'] = func_5887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5666_call = mod.get_global_var('func_5666')
func_5668_call = mutated_mod.get_global_var('func_5668')
call_5907 = func_5666_call()
call_5908 = func_5666_call()
func_961_call = mod.get_global_var('func_961')
func_964_call = mutated_mod.get_global_var('func_964')
var_5921 = relay.var("var_5921", dtype = "float32", shape = (208,))#candidate|5921|(208,)|var|float32
call_5920 = relay.TupleGetItem(func_961_call(relay.reshape(var_5921.astype('float32'), [4, 13, 4])), 0)
call_5922 = relay.TupleGetItem(func_964_call(relay.reshape(var_5921.astype('float32'), [4, 13, 4])), 0)
output = relay.Tuple([call_5907,call_5920,var_5921,])
output2 = relay.Tuple([call_5908,call_5922,var_5921,])
func_5933 = relay.Function([var_5921,], output)
mod['func_5933'] = func_5933
mod = relay.transform.InferType()(mod)
mutated_mod['func_5933'] = func_5933
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5934 = relay.var("var_5934", dtype = "float32", shape = (208,))#candidate|5934|(208,)|var|float32
func_5933_call = mutated_mod.get_global_var('func_5933')
call_5935 = func_5933_call(var_5934)
output = call_5935
func_5936 = relay.Function([var_5934], output)
mutated_mod['func_5936'] = func_5936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2183_call = mod.get_global_var('func_2183')
func_2184_call = mutated_mod.get_global_var('func_2184')
call_6028 = func_2183_call()
call_6029 = func_2183_call()
output = relay.Tuple([call_6028,])
output2 = relay.Tuple([call_6029,])
func_6067 = relay.Function([], output)
mod['func_6067'] = func_6067
mod = relay.transform.InferType()(mod)
output = func_6067()
func_6068 = relay.Function([], output)
mutated_mod['func_6068'] = func_6068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2833_call = mod.get_global_var('func_2833')
func_2834_call = mutated_mod.get_global_var('func_2834')
call_6106 = relay.TupleGetItem(func_2833_call(), 0)
call_6107 = relay.TupleGetItem(func_2834_call(), 0)
func_3361_call = mod.get_global_var('func_3361')
func_3363_call = mutated_mod.get_global_var('func_3363')
var_6120 = relay.var("var_6120", dtype = "uint8", shape = (864,))#candidate|6120|(864,)|var|uint8
call_6119 = relay.TupleGetItem(func_3361_call(relay.reshape(var_6120.astype('uint8'), [864,])), 3)
call_6121 = relay.TupleGetItem(func_3363_call(relay.reshape(var_6120.astype('uint8'), [864,])), 3)
func_2342_call = mod.get_global_var('func_2342')
func_2343_call = mutated_mod.get_global_var('func_2343')
call_6132 = relay.TupleGetItem(func_2342_call(), 1)
call_6133 = relay.TupleGetItem(func_2343_call(), 1)
bop_6136 = relay.power(call_6119.astype('float64'), relay.reshape(var_6120.astype('float64'), relay.shape_of(call_6119))) # shape=(864,)
bop_6139 = relay.power(call_6121.astype('float64'), relay.reshape(var_6120.astype('float64'), relay.shape_of(call_6121))) # shape=(864,)
func_2243_call = mod.get_global_var('func_2243')
func_2244_call = mutated_mod.get_global_var('func_2244')
call_6159 = relay.TupleGetItem(func_2243_call(), 0)
call_6160 = relay.TupleGetItem(func_2244_call(), 0)
uop_6164 = relay.sqrt(call_6132.astype('float32')) # shape=(16, 13, 6)
uop_6166 = relay.sqrt(call_6133.astype('float32')) # shape=(16, 13, 6)
output = relay.Tuple([call_6106,bop_6136,call_6159,uop_6164,])
output2 = relay.Tuple([call_6107,bop_6139,call_6160,uop_6166,])
func_6175 = relay.Function([var_6120,], output)
mod['func_6175'] = func_6175
mod = relay.transform.InferType()(mod)
var_6176 = relay.var("var_6176", dtype = "uint8", shape = (864,))#candidate|6176|(864,)|var|uint8
output = func_6175(var_6176)
func_6177 = relay.Function([var_6176], output)
mutated_mod['func_6177'] = func_6177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2833_call = mod.get_global_var('func_2833')
func_2834_call = mutated_mod.get_global_var('func_2834')
call_6249 = relay.TupleGetItem(func_2833_call(), 1)
call_6250 = relay.TupleGetItem(func_2834_call(), 1)
var_6259 = relay.var("var_6259", dtype = "float64", shape = (14, 11, 3))#candidate|6259|(14, 11, 3)|var|float64
bop_6260 = relay.left_shift(call_6249.astype('int32'), var_6259.astype('int32')) # shape=(14, 11, 3)
bop_6263 = relay.left_shift(call_6250.astype('int32'), var_6259.astype('int32')) # shape=(14, 11, 3)
func_2530_call = mod.get_global_var('func_2530')
func_2532_call = mutated_mod.get_global_var('func_2532')
call_6283 = relay.TupleGetItem(func_2530_call(), 1)
call_6284 = relay.TupleGetItem(func_2532_call(), 1)
func_2833_call = mod.get_global_var('func_2833')
func_2834_call = mutated_mod.get_global_var('func_2834')
call_6290 = relay.TupleGetItem(func_2833_call(), 1)
call_6291 = relay.TupleGetItem(func_2834_call(), 1)
func_1326_call = mod.get_global_var('func_1326')
func_1328_call = mutated_mod.get_global_var('func_1328')
call_6302 = relay.TupleGetItem(func_1326_call(), 0)
call_6303 = relay.TupleGetItem(func_1328_call(), 0)
func_2586_call = mod.get_global_var('func_2586')
func_2588_call = mutated_mod.get_global_var('func_2588')
call_6304 = func_2586_call()
call_6305 = func_2586_call()
func_6067_call = mod.get_global_var('func_6067')
func_6068_call = mutated_mod.get_global_var('func_6068')
call_6309 = relay.TupleGetItem(func_6067_call(), 0)
call_6310 = relay.TupleGetItem(func_6068_call(), 0)
output = relay.Tuple([bop_6260,call_6283,call_6290,call_6302,call_6304,call_6309,])
output2 = relay.Tuple([bop_6263,call_6284,call_6291,call_6303,call_6305,call_6310,])
func_6313 = relay.Function([var_6259,], output)
mod['func_6313'] = func_6313
mod = relay.transform.InferType()(mod)
mutated_mod['func_6313'] = func_6313
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6314 = relay.var("var_6314", dtype = "float64", shape = (14, 11, 3))#candidate|6314|(14, 11, 3)|var|float64
func_6313_call = mutated_mod.get_global_var('func_6313')
call_6315 = func_6313_call(var_6314)
output = call_6315
func_6316 = relay.Function([var_6314], output)
mutated_mod['func_6316'] = func_6316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5783_call = mod.get_global_var('func_5783')
func_5785_call = mutated_mod.get_global_var('func_5785')
call_6330 = func_5783_call()
call_6331 = func_5783_call()
func_5885_call = mod.get_global_var('func_5885')
func_5887_call = mutated_mod.get_global_var('func_5887')
var_6359 = relay.var("var_6359", dtype = "uint8", shape = (7, 195))#candidate|6359|(7, 195)|var|uint8
call_6358 = relay.TupleGetItem(func_5885_call(relay.reshape(var_6359.astype('uint8'), [1365,])), 1)
call_6360 = relay.TupleGetItem(func_5887_call(relay.reshape(var_6359.astype('uint8'), [1365,])), 1)
func_1712_call = mod.get_global_var('func_1712')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_6365 = relay.TupleGetItem(func_1712_call(relay.reshape(var_6359.astype('uint8'), [1365,])), 0)
call_6366 = relay.TupleGetItem(func_1715_call(relay.reshape(var_6359.astype('uint8'), [1365,])), 0)
uop_6369 = relay.tan(var_6359.astype('float64')) # shape=(7, 195)
output = relay.Tuple([call_6330,call_6358,call_6365,uop_6369,])
output2 = relay.Tuple([call_6331,call_6360,call_6366,uop_6369,])
func_6377 = relay.Function([var_6359,], output)
mod['func_6377'] = func_6377
mod = relay.transform.InferType()(mod)
mutated_mod['func_6377'] = func_6377
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6378 = relay.var("var_6378", dtype = "uint8", shape = (7, 195))#candidate|6378|(7, 195)|var|uint8
func_6377_call = mutated_mod.get_global_var('func_6377')
call_6379 = func_6377_call(var_6378)
output = call_6379
func_6380 = relay.Function([var_6378], output)
mutated_mod['func_6380'] = func_6380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5666_call = mod.get_global_var('func_5666')
func_5668_call = mutated_mod.get_global_var('func_5668')
call_6406 = func_5666_call()
call_6407 = func_5666_call()
output = call_6406
output2 = call_6407
func_6410 = relay.Function([], output)
mod['func_6410'] = func_6410
mod = relay.transform.InferType()(mod)
output = func_6410()
func_6411 = relay.Function([], output)
mutated_mod['func_6411'] = func_6411
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6473 = relay.var("var_6473", dtype = "float32", shape = (16, 4, 8))#candidate|6473|(16, 4, 8)|var|float32
const_6474 = relay.const([[[0.746595,-5.852292,-2.344027,-4.009151,0.945722,2.976801,9.922490,6.498235],[-5.662066,-6.331415,9.631421,-0.374501,8.815850,2.940512,2.004290,-3.626282],[2.768956,-1.236060,9.672768,-4.663190,4.555945,-4.313389,5.744514,-7.462442],[1.132883,-8.611525,2.791856,7.970966,2.812053,5.539500,2.268712,6.071980]],[[3.803145,-7.285648,6.644087,1.892647,-0.911810,4.847828,3.665117,7.047212],[-2.859120,-7.892680,-6.195217,8.543527,-1.153803,-5.761384,-4.963954,-2.370116],[-7.774384,-6.280099,5.859824,-9.110114,-9.938187,4.505004,5.067627,-6.763103],[2.060360,2.985280,-8.000686,8.887327,0.220858,-0.910986,-1.270991,0.930759]],[[8.130111,-5.326961,-8.617198,-5.070579,-0.349610,-1.097107,-8.067630,1.451135],[2.222546,-8.879795,7.778798,-4.229121,5.445517,9.540215,-1.444836,-3.802292],[-6.044368,-7.064750,7.102943,1.177089,2.506135,2.362227,3.249976,3.930584],[1.935954,-1.118136,5.610791,-2.873506,-5.910148,-2.578751,-8.289874,-4.015971]],[[8.322449,5.878849,-1.279915,-3.384672,5.748203,1.711940,7.908308,8.487495],[-1.139572,8.932542,5.962333,8.333673,1.827363,-9.215564,-4.117113,1.675586],[2.301913,9.287495,7.556520,6.112450,4.829845,6.675621,4.304251,-8.848450],[6.448176,-8.206642,0.720906,-3.127250,0.899812,-0.761528,5.135975,-1.103689]],[[1.366249,-8.746783,5.042931,6.992468,2.499076,2.728441,4.121846,-7.539833],[-9.594937,2.127468,-0.086075,-0.999887,-6.352757,-8.874323,-0.720704,4.500264],[-5.576284,5.472895,7.348495,-1.587899,4.237292,-6.982921,7.086070,8.724260],[6.287613,5.088685,-4.630963,7.817307,6.607789,1.653608,-0.177146,5.522629]],[[-2.343885,7.944210,3.749345,-2.198455,8.876064,7.567699,-3.170406,-7.340790],[-7.588543,6.341438,-5.867216,0.032435,-4.709577,7.615704,3.245433,0.115023],[6.266043,-9.058242,8.272943,-7.968542,9.883558,8.407355,-2.858582,3.927778],[-4.413893,-0.329728,9.951714,-8.496735,-1.795977,8.785535,-5.429034,1.837423]],[[1.511022,-4.083669,1.781172,5.134723,-9.979832,-3.760625,3.074735,4.860311],[-4.547421,-9.120396,-6.307885,-0.132464,-3.794128,-6.673576,-2.755672,9.725608],[0.780352,-2.663649,-5.730312,4.638498,0.152017,2.155596,7.633089,-4.617945],[-8.268812,-7.741839,1.492595,4.861121,-6.814329,-5.116361,-1.251575,-8.371396]],[[6.230419,-1.780588,-6.575847,-1.085932,9.604216,-2.412541,5.464954,-5.437556],[9.772529,-6.452567,5.566808,9.250310,9.951893,8.580286,1.870423,-4.071368],[-4.726053,-5.861544,-5.480979,-2.558757,-4.247435,6.931737,9.015628,-2.425727],[-0.992764,1.275658,-3.731507,6.809621,-6.441858,4.571529,-5.194564,-8.496386]],[[-8.260176,2.009336,-3.627676,-0.530789,9.170717,-9.237196,-1.050171,6.927795],[6.609757,-0.520591,8.964171,4.199355,-2.274125,7.444454,-0.350239,-7.575520],[-6.982887,-8.603494,9.500474,-2.445708,-3.253715,-8.446215,8.729895,6.265073],[-7.078344,-7.718834,7.239036,-8.711610,5.840663,-1.717280,8.268305,-0.037841]],[[-2.453774,-0.727157,-7.617217,-6.351046,3.674101,7.057209,9.413968,2.451461],[-6.999750,1.099825,-8.125910,-8.723694,-5.406289,3.661002,8.562407,2.677330],[-9.751778,1.779500,-9.640175,0.559949,-1.445962,-7.465789,0.708586,-8.228818],[-9.944667,8.808988,3.468201,-1.008647,-3.745705,6.947078,0.224135,-0.924907]],[[6.766354,-3.140208,7.316918,1.933626,-5.498089,5.335733,-6.110547,-2.726185],[-3.534790,3.385980,6.374703,3.271311,6.671164,4.244881,8.788982,9.834206],[0.474197,4.025021,2.998775,3.304135,-4.342126,-6.781605,-7.659205,6.092716],[-9.972605,-7.984489,-2.090843,-9.221985,-0.657136,7.934160,6.899572,-5.262380]],[[-2.653410,2.129099,5.257944,-7.573708,-2.416681,-5.018990,6.535048,7.143456],[-7.666861,7.545602,3.833791,-2.300487,5.956046,9.084823,-0.413063,2.559531],[5.808929,7.718112,2.593656,8.042052,-1.606898,-5.662558,5.843363,3.948495],[2.557382,4.805017,-8.621245,1.486055,6.058983,-0.471484,-4.611303,-1.345389]],[[5.142490,-9.179113,5.073177,-2.352271,8.001174,7.252374,-5.930894,-3.907415],[2.324014,-3.456444,-1.458242,0.551295,-4.769698,8.091522,-7.779620,2.260763],[6.439944,-0.427637,3.907363,-4.688291,-6.219578,3.214429,8.172355,-0.329332],[3.271128,-7.635067,-4.877317,2.173539,-5.755164,-9.358560,7.104240,-6.808925]],[[9.810771,1.698513,3.225088,-6.560248,-9.252363,-1.485254,4.398218,-2.421776],[5.935549,-3.445678,6.502428,-6.453420,7.231520,-8.895611,-7.855923,1.225448],[1.477733,-0.702449,5.010599,-7.577987,0.408449,4.740888,-6.093783,7.032699],[-3.252545,4.534784,-2.107926,9.386280,-6.887634,-3.715861,-5.551660,6.458758]],[[-0.008920,-9.477388,-9.066815,9.269382,5.094567,-1.689467,8.744687,1.296102],[-3.545934,0.708604,3.817686,-3.835109,-8.173205,-9.242223,-7.875268,-6.936734],[-3.613984,-8.312561,-2.594522,-2.266429,-7.301634,6.342261,-1.724722,-2.793597],[4.268461,2.041480,-3.381326,4.586481,-9.583840,-8.364054,2.535840,-4.423555]],[[4.903430,-1.666313,-7.628784,-8.859311,8.588933,-2.772774,-2.588491,-8.327756],[-2.350263,-3.045472,7.481352,0.325927,-0.176184,9.643795,8.753303,5.521049],[-5.938523,-6.224245,-1.282199,-3.359627,-7.411186,4.621158,8.844155,-0.398563],[-2.740456,-2.061149,-6.781288,7.931945,9.824237,-5.423621,-1.125198,-5.146809]]], dtype = "float32")#candidate|6474|(16, 4, 8)|const|float32
bop_6475 = relay.divide(var_6473.astype('float32'), relay.reshape(const_6474.astype('float32'), relay.shape_of(var_6473))) # shape=(16, 4, 8)
func_4773_call = mod.get_global_var('func_4773')
func_4775_call = mutated_mod.get_global_var('func_4775')
call_6494 = relay.TupleGetItem(func_4773_call(), 0)
call_6495 = relay.TupleGetItem(func_4775_call(), 0)
output = relay.Tuple([bop_6475,call_6494,])
output2 = relay.Tuple([bop_6475,call_6495,])
func_6511 = relay.Function([var_6473,], output)
mod['func_6511'] = func_6511
mod = relay.transform.InferType()(mod)
mutated_mod['func_6511'] = func_6511
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6512 = relay.var("var_6512", dtype = "float32", shape = (16, 4, 8))#candidate|6512|(16, 4, 8)|var|float32
func_6511_call = mutated_mod.get_global_var('func_6511')
call_6513 = func_6511_call(var_6512)
output = call_6513
func_6514 = relay.Function([var_6512], output)
mutated_mod['func_6514'] = func_6514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3379_call = mod.get_global_var('func_3379')
func_3380_call = mutated_mod.get_global_var('func_3380')
call_6520 = relay.TupleGetItem(func_3379_call(), 0)
call_6521 = relay.TupleGetItem(func_3380_call(), 0)
var_6524 = relay.var("var_6524", dtype = "float64", shape = (4, 11, 3))#candidate|6524|(4, 11, 3)|var|float64
bop_6525 = relay.mod(call_6520.astype('float64'), var_6524.astype('float64')) # shape=(4, 11, 3)
bop_6528 = relay.mod(call_6521.astype('float64'), var_6524.astype('float64')) # shape=(4, 11, 3)
output = relay.Tuple([bop_6525,])
output2 = relay.Tuple([bop_6528,])
func_6530 = relay.Function([var_6524,], output)
mod['func_6530'] = func_6530
mod = relay.transform.InferType()(mod)
mutated_mod['func_6530'] = func_6530
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6531 = relay.var("var_6531", dtype = "float64", shape = (4, 11, 3))#candidate|6531|(4, 11, 3)|var|float64
func_6530_call = mutated_mod.get_global_var('func_6530')
call_6532 = func_6530_call(var_6531)
output = call_6532
func_6533 = relay.Function([var_6531], output)
mutated_mod['func_6533'] = func_6533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5500_call = mod.get_global_var('func_5500')
func_5502_call = mutated_mod.get_global_var('func_5502')
call_6537 = relay.TupleGetItem(func_5500_call(), 1)
call_6538 = relay.TupleGetItem(func_5502_call(), 1)
func_2573_call = mod.get_global_var('func_2573')
func_2574_call = mutated_mod.get_global_var('func_2574')
call_6554 = relay.TupleGetItem(func_2573_call(), 0)
call_6555 = relay.TupleGetItem(func_2574_call(), 0)
output = relay.Tuple([call_6537,call_6554,])
output2 = relay.Tuple([call_6538,call_6555,])
func_6574 = relay.Function([], output)
mod['func_6574'] = func_6574
mod = relay.transform.InferType()(mod)
mutated_mod['func_6574'] = func_6574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6574_call = mutated_mod.get_global_var('func_6574')
call_6575 = func_6574_call()
output = call_6575
func_6576 = relay.Function([], output)
mutated_mod['func_6576'] = func_6576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5537_call = mod.get_global_var('func_5537')
func_5538_call = mutated_mod.get_global_var('func_5538')
call_6631 = relay.TupleGetItem(func_5537_call(), 3)
call_6632 = relay.TupleGetItem(func_5538_call(), 3)
func_4861_call = mod.get_global_var('func_4861')
func_4863_call = mutated_mod.get_global_var('func_4863')
call_6636 = relay.TupleGetItem(func_4861_call(), 0)
call_6637 = relay.TupleGetItem(func_4863_call(), 0)
output = relay.Tuple([call_6631,call_6636,])
output2 = relay.Tuple([call_6632,call_6637,])
func_6656 = relay.Function([], output)
mod['func_6656'] = func_6656
mod = relay.transform.InferType()(mod)
output = func_6656()
func_6657 = relay.Function([], output)
mutated_mod['func_6657'] = func_6657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3288_call = mod.get_global_var('func_3288')
func_3289_call = mutated_mod.get_global_var('func_3289')
call_6674 = func_3288_call()
call_6675 = func_3288_call()
func_6530_call = mod.get_global_var('func_6530')
func_6533_call = mutated_mod.get_global_var('func_6533')
const_6687 = relay.const([-9.744720,1.243907,-0.090288,6.879728,-2.103457,9.632491,5.630742,-8.417395,1.983356,2.475800,-1.929986,6.908542,-2.123162,-7.311688,-1.353627,-9.878777,4.202528,1.660738,-6.578702,-9.098838,-6.602918,-5.739301,-5.473729,2.624662,-1.332706,3.957389,-7.160091,4.789293,-2.678334,-3.136434,-1.369762,-1.474171,-5.231277,-3.523373,-5.767009,-7.284866,-5.450321,-3.828073,4.382524,-8.231104,-0.905662,-1.558788,-3.394047,0.551451,-0.465980,5.400694,-1.481687,-0.225043,5.643464,8.841189,9.276242,-1.732632,-5.703907,-4.114432,6.349714,-2.046827,1.117819,-3.721776,-5.303625,-8.775237,5.126748,-8.452463,2.302554,4.931031,1.938052,6.888977,-1.201864,-6.483909,-6.791483,-2.387397,2.967233,-2.568362,5.968678,-9.570775,-1.377075,-9.005908,-0.542029,-2.890144,-9.290301,-0.350972,-6.840731,-5.398612,9.821026,-7.084672,-7.429121,0.345133,6.027872,-1.713732,-2.716812,-5.243031,0.550114,1.647334,2.801447,-3.096247,0.357973,5.444738,-2.719428,-9.199954,-4.120924,3.690976,3.021947,-0.764266,-2.453978,9.263569,3.506275,-9.122412,7.920614,-0.050970,0.620391,-6.187823,7.460454,-5.736626,7.945277,-4.537403,1.521361,-6.054855,-9.431667,5.406255,2.543658,-6.274522,0.266701,-0.922930,-5.567563,4.551198,9.080372,-0.531860,-7.807988,-4.605948,7.044552,0.476821,-1.073394,4.871584], dtype = "float64")#candidate|6687|(132,)|const|float64
call_6686 = relay.TupleGetItem(func_6530_call(relay.reshape(const_6687.astype('float64'), [4, 11, 3])), 0)
call_6688 = relay.TupleGetItem(func_6533_call(relay.reshape(const_6687.astype('float64'), [4, 11, 3])), 0)
func_4773_call = mod.get_global_var('func_4773')
func_4775_call = mutated_mod.get_global_var('func_4775')
call_6695 = relay.TupleGetItem(func_4773_call(), 0)
call_6696 = relay.TupleGetItem(func_4775_call(), 0)
output = relay.Tuple([call_6674,call_6686,const_6687,call_6695,])
output2 = relay.Tuple([call_6675,call_6688,const_6687,call_6696,])
func_6718 = relay.Function([], output)
mod['func_6718'] = func_6718
mod = relay.transform.InferType()(mod)
mutated_mod['func_6718'] = func_6718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6718_call = mutated_mod.get_global_var('func_6718')
call_6719 = func_6718_call()
output = call_6719
func_6720 = relay.Function([], output)
mutated_mod['func_6720'] = func_6720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1516_call = mod.get_global_var('func_1516')
func_1518_call = mutated_mod.get_global_var('func_1518')
call_6758 = func_1516_call()
call_6759 = func_1516_call()
output = relay.Tuple([call_6758,])
output2 = relay.Tuple([call_6759,])
func_6760 = relay.Function([], output)
mod['func_6760'] = func_6760
mod = relay.transform.InferType()(mod)
mutated_mod['func_6760'] = func_6760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6760_call = mutated_mod.get_global_var('func_6760')
call_6761 = func_6760_call()
output = call_6761
func_6762 = relay.Function([], output)
mutated_mod['func_6762'] = func_6762
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6783 = relay.const([[[-0.171128,-0.586697,-9.350970,4.296107,-4.265859,3.315407,3.109015,3.779336,0.468449],[4.097193,1.103146,-4.603714,0.087252,-4.460363,2.546789,-2.109767,3.381527,-8.631915],[0.798838,2.763103,4.815944,2.733726,7.750690,0.303134,5.720023,8.276502,-8.767993],[-9.169115,-8.601057,-4.300776,-8.529213,1.855496,-5.265963,4.222752,1.582375,0.619667],[1.054991,5.611011,8.803601,7.548598,4.280768,1.850472,-5.328438,-5.523341,-4.657473],[-2.928816,1.171875,8.984437,-7.157557,1.119618,3.353730,-2.638866,9.188896,2.729089],[-3.958190,-2.580377,5.579564,-0.997309,1.492530,-5.520105,6.006004,-0.527074,9.795564],[-5.656399,-7.466931,3.689480,-0.957989,-7.816484,-2.763410,-9.014454,-2.395144,-2.796498],[4.887702,7.016046,6.053212,-9.226655,8.232752,-1.163656,-3.496251,-8.857714,-6.786991],[-9.670989,5.105089,4.718750,-4.530654,-1.110721,-1.149360,5.661313,8.568260,-3.149206],[-5.476225,-9.365305,1.610598,-8.744037,6.466202,-3.838428,8.628407,5.871667,7.464576]],[[-0.326504,-3.323503,-9.266428,6.141300,-5.967795,-0.237900,-8.527044,-8.500185,-8.779332],[3.034666,0.136782,0.532680,-8.787528,7.217876,8.189753,-3.951694,-0.774332,0.588267],[3.052126,-5.629853,6.701405,-6.774111,-9.168765,-2.660251,-8.201333,8.521386,6.665410],[5.062350,0.154728,1.803570,1.268393,-4.240219,-7.243298,-2.619914,3.821402,-4.910976],[-5.081799,-2.699648,1.136364,3.685583,-5.299227,4.210748,-9.385873,5.117995,1.638121],[-0.112839,8.376299,3.320025,-7.144344,4.673118,-3.695915,1.006391,9.537464,6.206733],[-6.547879,-9.523201,-4.593643,-6.249575,3.052680,-3.619538,-4.244969,9.866817,-9.258091],[-6.389852,7.912349,-8.874928,9.660579,-2.495612,6.131077,6.820911,-6.490280,-7.958921],[0.153970,7.082321,-4.427833,-7.363532,4.639179,-8.589653,-4.253271,-3.454411,7.879755],[5.851184,-6.409081,6.745528,-5.688560,-8.586453,-5.027978,8.268433,6.597161,-4.633437],[-7.729380,4.733123,9.986706,3.299985,-2.147272,5.911691,-9.264644,-7.406277,-2.949213]],[[-3.808664,-5.566187,4.508133,5.564918,-4.198913,-9.002327,9.490881,7.336531,-9.654375],[-3.936987,-4.189228,4.464896,-7.482529,5.571288,3.910497,-8.725783,-7.660769,-1.696087],[-4.470088,-4.592199,-4.238355,3.481847,9.211912,-7.902057,5.412297,-4.228868,5.137493],[6.883355,8.679340,-6.434109,-0.710729,5.903168,9.949589,5.977940,7.300310,1.386728],[-7.818573,7.550545,5.413071,6.320170,4.775084,5.319365,9.824162,-0.714118,2.016676],[5.831139,-9.286619,-8.386600,-2.870726,8.057276,4.106474,-2.644334,6.241612,1.335343],[5.611584,-3.547218,-6.369564,-8.097078,-0.340416,4.190508,5.919008,-7.352063,5.625135],[-4.408817,-2.523789,4.200583,-1.321493,7.412268,-9.326570,-3.207714,7.315481,-0.610008],[-2.454353,5.705082,4.996939,-9.113766,-1.583578,-7.366458,2.596426,0.314181,-0.481333],[7.170801,-4.079416,5.448615,-7.119519,3.719156,-1.673567,6.824410,-0.603441,8.125465],[7.676461,-2.871004,-3.462937,7.360651,4.081732,5.416247,-8.035723,-2.949599,9.095730]],[[9.880596,-6.259338,0.979580,-1.747898,3.842023,-1.316471,-7.457160,7.320365,0.059350],[-2.414327,4.010321,7.586360,0.910534,-3.537357,3.894027,4.361643,0.486750,1.487223],[-1.858858,8.269661,-7.274382,3.628079,-9.378922,8.689884,-4.096107,-1.135997,-1.222739],[8.805170,9.413143,2.382006,3.366146,6.103101,-7.274280,-1.413575,-1.462412,8.276789],[1.732954,-3.215773,7.648082,6.976918,4.595397,2.713380,3.995914,0.090004,-5.026695],[6.855979,-1.756998,-5.218064,8.550106,8.565903,5.043873,-8.821688,0.664493,-1.764903],[4.090599,9.412696,8.961264,-5.546965,7.381827,-0.427419,-7.640455,0.782964,-2.069835],[-9.708841,-3.014607,-7.252479,-6.614434,-2.365417,7.990892,-5.238975,-5.812815,1.057702],[-0.375329,3.707331,1.595159,-5.081695,3.761335,-3.180852,5.826180,-3.588631,1.595429],[4.622213,2.298091,7.114700,-5.024811,3.706634,4.604561,4.947331,-6.125878,8.914793],[-1.844627,-1.016857,-6.787464,5.239356,2.160857,1.411008,-2.044876,-0.910800,3.212914]],[[-9.045871,6.587029,-0.349511,-3.325274,-7.464755,-2.446234,5.531727,6.421515,4.710785],[-8.387603,-3.007398,-9.152278,-4.074026,-1.781201,-9.252542,1.027287,-0.727657,3.887242],[7.067816,-5.359334,-4.707667,-0.480871,3.448459,7.312141,2.875908,9.911690,6.440260],[8.099144,3.980947,-9.735925,7.798487,-2.580095,-2.557970,2.243251,-9.910665,-1.123356],[-6.613314,-1.169987,-3.475449,-0.790260,2.263704,6.041928,8.530039,8.563494,5.858332],[3.222309,0.488167,-2.719805,0.028497,8.303089,4.387561,-7.523249,-6.783598,9.521335],[3.810668,-7.997423,3.078177,7.390695,1.271800,2.881049,9.293291,9.564223,4.095553],[-9.470314,9.655508,-2.255166,7.844893,0.016647,6.989111,9.695658,-1.366572,9.051566],[1.173735,0.553176,0.467250,8.268687,8.210042,0.397810,-9.375576,6.286042,-1.730237],[-4.502972,-2.236863,1.027457,-4.259191,-1.348536,8.402020,4.431863,9.761356,2.353258],[7.057635,8.632131,7.170743,0.974832,-7.238316,-4.129511,-7.054153,3.752326,-2.362476]],[[-2.939653,3.548228,3.405781,7.428004,6.503642,9.054903,3.946773,-9.659534,3.854254],[-6.915696,9.932435,9.570193,5.137596,7.686035,7.869920,6.295105,-0.389623,-0.971957],[5.525941,-7.726817,-0.819295,5.672346,3.565804,-1.727416,-3.007946,7.047210,-8.179462],[3.972812,2.401016,-3.296413,-1.354215,-4.079450,-5.333108,-0.752433,-5.209812,-7.977823],[9.978778,8.994268,8.876159,5.774574,-8.708087,-5.644673,-7.348774,-4.890012,-2.569009],[-6.207851,-0.341816,2.518665,6.125542,8.712479,7.307731,0.766133,3.432669,5.989526],[-3.578864,-8.142999,2.167940,5.643278,-2.847723,3.453624,-4.044597,9.075000,3.385190],[2.881544,1.028925,-3.195348,5.087397,7.587632,-5.967591,9.650077,4.034781,1.983237],[-9.740477,-2.068966,-4.081472,8.546368,7.152665,-3.979986,-6.184111,-4.519738,-8.549276],[-8.201666,-0.792176,-4.023996,-9.042882,0.076216,-4.923156,-6.410209,-9.937355,2.385421],[4.171142,5.007941,-7.588641,6.330515,-0.218700,-4.887919,-5.116118,-2.808485,-9.813734]],[[-4.324271,-1.566025,-9.367549,-1.250216,-0.945407,-9.238108,-8.785789,-9.710534,-3.444408],[4.244127,2.990724,9.342299,-0.573425,-1.347526,-1.655680,0.231965,6.759667,8.941429],[-7.461382,6.787385,-2.260564,1.999355,1.041407,-7.283168,-8.082857,6.345445,3.154314],[9.130427,-2.529784,-8.919510,-9.116543,8.312637,-3.143246,7.689699,3.137223,6.782161],[-7.837142,-8.828382,-9.984255,-7.401146,-2.774571,9.902428,-8.333344,6.688434,-5.972129],[-9.219015,9.871371,8.069367,-2.530661,6.710439,1.869704,2.957877,8.666666,3.528420],[-5.631907,-1.311935,7.912822,4.160346,-0.715110,-3.777280,-0.048092,9.436242,2.559444],[5.009130,7.406747,1.198973,8.297381,0.151106,-4.300169,9.106856,-4.801000,7.442332],[8.337905,2.517479,6.080989,-7.552330,-7.281292,6.155477,-4.287155,1.081449,6.912413],[-9.522549,1.924801,8.618655,-4.634238,7.636851,-9.120539,-6.726778,3.200245,8.984129],[-0.961234,-3.411084,7.860017,-9.694154,4.860656,-9.358015,-0.457811,7.263102,-2.083237]]], dtype = "float64")#candidate|6783|(7, 11, 9)|const|float64
var_6784 = relay.var("var_6784", dtype = "float64", shape = (7, 11, 9))#candidate|6784|(7, 11, 9)|var|float64
bop_6785 = relay.floor_divide(const_6783.astype('float64'), relay.reshape(var_6784.astype('float64'), relay.shape_of(const_6783))) # shape=(7, 11, 9)
bop_6790 = relay.minimum(const_6783.astype('uint32'), relay.reshape(bop_6785.astype('uint32'), relay.shape_of(const_6783))) # shape=(7, 11, 9)
output = relay.Tuple([bop_6790,])
output2 = relay.Tuple([bop_6790,])
func_6798 = relay.Function([var_6784,], output)
mod['func_6798'] = func_6798
mod = relay.transform.InferType()(mod)
var_6799 = relay.var("var_6799", dtype = "float64", shape = (7, 11, 9))#candidate|6799|(7, 11, 9)|var|float64
output = func_6798(var_6799)
func_6800 = relay.Function([var_6799], output)
mutated_mod['func_6800'] = func_6800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2311_call = mod.get_global_var('func_2311')
func_2313_call = mutated_mod.get_global_var('func_2313')
call_6804 = func_2311_call()
call_6805 = func_2311_call()
func_3712_call = mod.get_global_var('func_3712')
func_3715_call = mutated_mod.get_global_var('func_3715')
var_6835 = relay.var("var_6835", dtype = "float64", shape = (175,))#candidate|6835|(175,)|var|float64
call_6834 = relay.TupleGetItem(func_3712_call(relay.reshape(var_6835.astype('float64'), [5, 5, 7])), 0)
call_6836 = relay.TupleGetItem(func_3715_call(relay.reshape(var_6835.astype('float64'), [5, 5, 7])), 0)
func_6377_call = mod.get_global_var('func_6377')
func_6380_call = mutated_mod.get_global_var('func_6380')
const_6869 = relay.const([-7,-9,9,-2,7,10,-2,-9,1,8,3,-3,-8,-1,8,5,1,2,1,10,-1,3,9,-6,3,10,-5,3,5,8,-7,1,-8,-1,7,6,-4,-3,-4,-5,10,2,-10,3,-8,1,5,-3,-6,-3,-6,3,9,-2,5,-9,-5,-4,-8,2,-7,9,-6,-6,-7,-5,9,2,4,-2,-3,5,2,3,-6,5,-2,7,7,10,6,8,5,-3,5,-9,-6,6,-6,9,-8,5,-9,7,10,1,-5,1,-10,-3,2,3,8,8,-10,6,-9,7,-5,-3,2,-1,2,10,-6,9,5,-6,3,7,-8,3,-3,-7,-5,-3,6,-5,-6,2,-8,-2,3,5,1,-1,-2,8,5,4,-8,8,-1,-4,-9,-10,9,9,-9,10,-4,-9,-5,2,4,1,-2,-10,3,-1,2,9,-5,-3,-1,-4,-2,-1,-2,9,6,-2,1,3,-5,4,8,-9,2,-9,5,-5,-10,5,9,10,6,-4,-3,10,-3,-7,8,6,-10,-2,-2,-3,5,-4,6,10,7,10,2,10,-4,8,5,-3,-1,-1,4,-5,3,-3,-5,-10,8,-2,8,8,9,6,-10,-8,-4,5,-2,-6,10,-2,2,-5,4,3,-9,5,-8,1,-8,10,7,-9,-6,4,4,-10,9,-9,5,6,6,2,-10,4,2,-1,1,-8,3,-2,-9,5,8,-3,-7,-6,10,-5,-9,-10,4,1,-1,2,-10,-3,7,-9,10,-9,-10,-8,-3,3,-3,-4,-4,2,-4,9,9,5,10,2,-5,-6,7,7,10,-3,-5,-2,2,6,8,-1,9,-2,7,8,-6,1,10,-5,-10,-3,-5,-5,9,-4,9,4,9,-7,-2,10,-9,3,-1,-10,-7,7,8,-9,-5,1,-6,2,-1,-4,3,-10,7,4,2,-8,-6,10,-6,8,4,5,-6,-7,-5,-9,7,5,-7,-1,-10,9,-3,-10,10,10,9,5,-2,4,5,10,-7,7,1,-2,-6,-8,9,-8,8,-6,5,4,-6,-7,-4,-7,1,4,2,6,6,-9,-4,8,6,8,-7,-9,3,-6,-4,-9,-6,10,10,8,-9,-4,5,-2,-6,-4,-7,6,10,8,-6,10,1,-4,5,-6,10,-7,2,7,4,-2,4,-10,3,-10,-4,-3,-10,5,-8,10,-10,4,-8,1,2,-10,3,-3,-7,-5,1,5,2,7,-10,-7,-5,2,2,5,9,10,-7,-8,4,-7,-9,8,-2,-3,-3,-5,-1,-2,-2,-7,-6,3,-2,10,-4,4,-9,7,7,-6,-10,7,-7,6,-7,10,-4,7,-6,3,-3,-3,7,-6,10,5,4,-1,2,-2,-2,4,-7,-1,7,-3,9,5,-8,2,-6,7,-8,2,-8,1,-9,6,-6,-1,9,5,1,-5,2,4,4,-7,10,6,-4,-7,-2,10,-8,-2,4,6,-9,4,-10,-1,-2,1,-10,1,6,8,9,-7,-7,-5,-8,8,-5,1,3,-4,-2,8,-3,-5,-4,-6,-3,3,4,2,-10,9,3,3,-2,8,1,6,-4,1,-6,-3,10,8,4,5,-10,-1,6,6,8,-4,1,-3,2,3,10,8,3,-5,-8,1,7,-1,-6,3,-3,3,6,1,1,-8,1,3,4,1,8,-9,5,-10,-7,5,9,-3,3,4,7,4,-8,2,-7,-3,6,-2,10,-10,-4,-6,-2,-9,-5,10,3,-10,3,2,-6,6,6,2,1,-4,8,7,1,8,7,7,-4,-2,10,8,10,9,2,-4,7,8,-10,-7,3,8,-1,-1,-4,1,-8,2,-3,-3,-4,7,-9,-9,2,-1,-9,-6,-5,-7,-9,-3,-9,6,-7,8,10,-7,2,7,9,-10,8,-1,2,-2,-8,9,-1,1,6,3,5,-2,-3,-3,-6,3,9,-6,3,4,-2,-1,8,5,1,9,-8,-5,1,-5,10,-10,3,-2,6,2,-8,3,6,1,5,-5,4,-4,-9,1,-7,10,1,-10,7,4,-4,-3,-4,10,-8,-2,7,9,-5,5,5,5,7,-10,-5,4,-3,2,3,9,-8,-8,-7,1,7,-5,1,-6,-5,-5,-5,2,5,-7,9,-4,7,4,-6,9,8,6,3,-10,-2,-9,-5,5,6,-2,8,-1,-7,10,-9,9,-2,-9,-10,-3,5,1,4,1,6,6,9,-8,4,4,-6,1,9,-4,10,-5,-1,4,-10,7,10,1,-3,-10,8,10,-6,-3,2,5,-5,6,7,-3,-7,-3,6,-8,3,-5,9,-7,8,-1,-5,2,-7,8,-10,-10,-9,-6,9,3,-2,-4,-6,6,-1,4,-3,8,7,-7,4,4,2,-10,3,-4,-4,6,7,3,10,4,4,-7,-7,-7,-2,4,-8,5,-10,6,5,-3,5,2,3,-1,9,9,-10,7,-7,6,-7,-7,-7,-10,-5,7,-9,7,5,1,4,10,-8,8,9,-1,2,-3,2,-1,8,-9,7,1,2,7,-3,1,-5,-7,2,1,5,-5,1,4,-4,-6,-8,4,-10,7,-10,-7,1,9,1,9,8,-10,2,8,-8,-8,3,8,2,9,6,-7,1,10,8,5,-5,-2,-3,-2,5,7,1,1,1,-5,9,3,6,1,5,7,-5,7,-1,8,9,4,-3,3,-9,2,-8,8,-8,-9,7,3,7,7,-8,-4,2,-9,4,-8,10,-1,-3,-6,7,6,-1,5,10,8,1,-5,1,-6,5,6,-2,-8,7,9,-9,-10,-5,-2,1,3,1,2,1,7,-2,5,-1,10,-7,1,-4,-10,-8,-6,-10,10,6,-3,10,6,4,-7,-4,-2,5,-1,-6,10,1,4,6,5,6,10,8,9,7,7,-4,-4,-2,-8,4,-4,-7,-6,-2,4,9,-7,9,-10,-3,-8,6,4,7,-8,-3,5,1,-2,2,-3,1,9,8,-8,8,6,10,-2,5,5,2,-7,-1,6,-6,-6,10,8,-5,-7,-4,7,-6,-8,-10,-8,-5,5,-5,-1,3,9,-3,1,5,10,-2,3,9,6,6,-4,-10,-9,2,-7,9,8,3,9,7,7,-10,7,4,9,-9,3,3,-2,3,-2,5,4,7,-8,-5,-4,-7,-2,-6,1,7,-3,-7,7,-6,4,-9,1,-2,-10,6,-9,7,-4,-6,8,-10,-4,-8,6,-10,-7,-7,-4,-7,-7,10,-6,9,2,6,9,-3,-2,5,-8,6,-1,2,-3,2,4,6,-1,-1,-2,-4,-2,7,-1,1,7,-3,-10,6,5,-3,-9,8,-8,4,-5,-3,7,-2,4,6,-1,-10,7,4,3,3,-10,2,10,-8,-4,6,4,-10,1,8,6,-3,-5,6,-8,-9,-10,6,7,-6,8,-2,2,-9,-9,-7,6,-7,8,-8,-2,7,-8,-1,9,-9,1,-9,3,-8,-4,7,-4,10,10,10,-5,-4,-10,-1,2,5,-1,-6,2,-9,8,8,-2,8,6,-4,5,-3,2,-3,4,-8,2,-1,10,3,-6,2,7,2,7,4,5,-6,-3,-1,-1,-2,-5,-7,3,-10,1,8,1,-3,5,10,-7,7,9,9,-7,3,5,6,2,-6,-8,-10,4,9], dtype = "uint8")#candidate|6869|(1365,)|const|uint8
call_6868 = relay.TupleGetItem(func_6377_call(relay.reshape(const_6869.astype('uint8'), [7, 195])), 2)
call_6870 = relay.TupleGetItem(func_6380_call(relay.reshape(const_6869.astype('uint8'), [7, 195])), 2)
uop_6889 = relay.atan(var_6835.astype('float32')) # shape=(175,)
output = relay.Tuple([call_6804,call_6834,call_6868,const_6869,uop_6889,])
output2 = relay.Tuple([call_6805,call_6836,call_6870,const_6869,uop_6889,])
func_6892 = relay.Function([var_6835,], output)
mod['func_6892'] = func_6892
mod = relay.transform.InferType()(mod)
mutated_mod['func_6892'] = func_6892
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6893 = relay.var("var_6893", dtype = "float64", shape = (175,))#candidate|6893|(175,)|var|float64
func_6892_call = mutated_mod.get_global_var('func_6892')
call_6894 = func_6892_call(var_6893)
output = call_6894
func_6895 = relay.Function([var_6893], output)
mutated_mod['func_6895'] = func_6895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4364_call = mod.get_global_var('func_4364')
func_4366_call = mutated_mod.get_global_var('func_4366')
call_7068 = func_4364_call()
call_7069 = func_4364_call()
output = call_7068
output2 = call_7069
func_7077 = relay.Function([], output)
mod['func_7077'] = func_7077
mod = relay.transform.InferType()(mod)
output = func_7077()
func_7078 = relay.Function([], output)
mutated_mod['func_7078'] = func_7078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1235_call = mod.get_global_var('func_1235')
func_1237_call = mutated_mod.get_global_var('func_1237')
call_7114 = func_1235_call()
call_7115 = func_1235_call()
var_7137 = relay.var("var_7137", dtype = "float64", shape = (4, 11, 3))#candidate|7137|(4, 11, 3)|var|float64
bop_7138 = relay.bitwise_and(call_7114.astype('uint16'), var_7137.astype('uint16')) # shape=(4, 11, 3)
bop_7141 = relay.bitwise_and(call_7115.astype('uint16'), var_7137.astype('uint16')) # shape=(4, 11, 3)
output = relay.Tuple([bop_7138,])
output2 = relay.Tuple([bop_7141,])
func_7149 = relay.Function([var_7137,], output)
mod['func_7149'] = func_7149
mod = relay.transform.InferType()(mod)
var_7150 = relay.var("var_7150", dtype = "float64", shape = (4, 11, 3))#candidate|7150|(4, 11, 3)|var|float64
output = func_7149(var_7150)
func_7151 = relay.Function([var_7150], output)
mutated_mod['func_7151'] = func_7151
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7207 = relay.var("var_7207", dtype = "uint8", shape = (16, 7, 8))#candidate|7207|(16, 7, 8)|var|uint8
var_7208 = relay.var("var_7208", dtype = "uint8", shape = (16, 7, 8))#candidate|7208|(16, 7, 8)|var|uint8
bop_7209 = relay.equal(var_7207.astype('bool'), relay.reshape(var_7208.astype('bool'), relay.shape_of(var_7207))) # shape=(16, 7, 8)
func_5062_call = mod.get_global_var('func_5062')
func_5065_call = mutated_mod.get_global_var('func_5065')
const_7215 = relay.const([[3,-8,-2,-1,-8,-5,-10,8,5,2,1,-7,9,10],[7,-6,2,3,4,-8,-5,-3,-3,8,-3,1,4,2],[-7,-1,-6,7,10,-3,-4,-9,5,3,-2,-10,-9,1],[-7,9,5,10,-8,9,-7,-4,-5,-1,4,-10,2,3],[1,7,7,3,7,-3,-8,-4,-7,5,1,2,-7,6],[-4,-3,3,2,7,1,-7,-8,7,10,-10,3,1,9],[-10,7,3,9,-9,7,-4,-9,-1,6,1,-1,10,-2],[-1,-1,7,-7,10,-8,4,-5,2,-9,-3,2,-2,-4],[-8,5,9,-2,-4,7,-4,-4,-8,9,5,6,5,-3],[-2,-9,-3,-2,10,7,5,-9,10,-9,4,-10,-8,-8],[-4,-9,-10,-7,-5,-5,2,-3,7,6,-7,6,3,-10],[-2,-3,1,-5,4,-4,-10,6,-1,9,-2,5,-9,9],[-9,-4,-7,-9,1,-9,-5,-4,2,-7,10,8,10,-9],[6,-5,-7,6,-6,-6,9,1,-10,9,6,2,-1,-8],[-6,3,5,5,-7,-9,5,1,3,-8,-9,-3,-4,-1],[-5,-9,7,3,10,-5,-8,-1,2,-7,-3,5,3,-9],[1,3,10,-7,5,-9,7,-1,10,7,3,-4,10,-10],[-7,1,10,6,-7,-9,4,-7,-3,5,10,5,6,2],[1,9,3,-6,6,-5,4,5,-3,8,-1,-1,-4,6],[10,-4,-10,-8,4,7,5,-5,7,6,2,-8,-6,-8],[7,-8,10,7,6,-4,-7,-2,-3,1,7,-10,1,6],[8,8,5,-4,10,6,7,8,-1,8,9,3,-9,7],[-2,-9,-4,-8,3,-6,5,10,-4,-6,3,10,-3,8],[-8,4,-5,-2,10,-9,-4,-7,-9,-9,-7,9,-8,2],[1,-5,-2,-9,-2,7,1,-4,-1,1,7,-2,-4,-6],[9,6,-7,-9,10,9,6,-3,-4,-9,-7,6,10,-10],[-10,-9,-6,8,-7,-6,4,-8,-1,-7,-7,1,-7,-8],[6,3,8,-4,-8,10,1,2,-1,-6,-3,-9,-9,2],[7,5,10,9,10,4,8,-3,10,-6,6,-5,-5,9],[5,2,-3,-5,-4,3,-8,4,-1,-6,-10,3,-4,-7],[5,7,-7,-3,-7,-5,5,-9,-5,10,7,8,-8,-7],[1,5,10,-7,-2,-7,-3,2,-2,-2,1,4,9,9],[-5,2,-10,4,-1,-7,5,2,8,-5,-4,-9,8,4],[9,5,-10,2,5,8,-10,7,-8,-1,-2,9,3,10],[3,-7,7,-6,8,-5,-5,7,9,-9,2,3,8,9],[-10,-1,4,5,7,-8,-1,-5,9,10,-5,-5,10,-2],[-2,8,-1,6,4,-7,-5,5,10,-10,4,-7,10,-8],[9,-7,-5,2,-3,-3,2,-7,5,-2,-3,-5,2,-6],[1,-3,7,9,4,-8,-10,3,1,8,3,4,-2,-3],[-1,9,6,-2,1,-5,-5,-1,5,8,3,5,-5,1],[8,-4,-6,2,-2,-5,8,-7,4,-9,-1,5,4,-9],[9,-6,6,7,-10,4,-3,-6,-8,3,10,-10,-10,4],[-7,5,-3,-4,-1,-10,1,-7,-2,5,-6,1,4,-7],[-8,-10,-4,-10,6,-3,-6,9,9,-2,-9,-3,7,10],[-5,8,10,6,-5,-10,-2,-7,7,4,2,-7,4,5],[-3,-5,-6,4,2,-1,-8,-7,5,7,-2,8,-8,6],[-6,-3,7,-7,-10,-10,-1,-9,-3,9,10,10,6,5],[-4,6,-1,-8,7,-3,8,-9,-6,10,-5,-9,-5,-7],[8,7,-3,3,1,4,9,-5,3,-6,2,-10,4,-4],[-10,-10,-4,-2,9,3,-7,8,-4,-10,6,-6,3,9],[-7,4,3,6,10,-4,-3,9,-6,5,9,-9,-3,-5],[-2,2,5,-7,-10,8,8,9,1,-1,-4,-8,-4,-7],[-5,3,-5,7,3,-10,6,4,-10,-7,-10,9,-7,-6],[6,-7,-6,-8,-5,2,-10,2,-10,10,-7,2,-7,3],[10,4,5,-8,-4,-3,-3,9,-7,9,-5,-9,8,-2],[-2,9,-8,-9,8,5,6,-1,5,4,10,1,-4,8],[4,7,8,-10,-2,-9,-6,2,-4,-3,-4,-3,2,-10],[6,8,-9,-8,4,-3,-6,-9,-7,-6,-8,2,-8,8],[10,-4,-7,8,1,5,3,4,-10,-4,5,-2,1,-7],[-10,6,-5,10,-7,10,-4,3,-4,-9,-9,-5,-2,-7],[10,1,9,2,2,-3,-10,-6,9,4,-6,10,-5,-8],[-10,2,-9,2,2,1,5,2,-9,10,8,3,-6,-7],[-8,9,-4,-9,-4,10,-4,10,6,-5,-8,5,8,8],[-1,-6,-4,6,-8,10,8,7,-2,1,7,-1,10,1],[-3,5,-7,-4,8,8,7,-9,9,-6,3,7,7,6],[-5,7,-7,-6,5,-7,2,-10,-5,-5,-5,5,2,7],[-1,7,10,-8,8,3,-5,-8,-8,-7,7,5,-3,-1],[2,2,-1,-3,-3,-9,-6,4,-5,-8,3,3,-5,4],[-9,-5,-3,8,6,-4,-2,-1,7,2,10,-2,5,-2],[6,-10,-1,7,2,7,-7,-8,-5,-9,-8,4,-1,10],[-2,6,-10,-2,-9,-4,-6,-8,3,-4,-9,-3,-4,-5],[-3,-8,-7,4,1,8,-7,-1,-5,-6,7,9,2,2],[-6,10,-4,-6,-5,8,-6,-5,1,8,7,4,-3,-9],[-4,-3,-2,10,3,6,-6,-3,-3,9,-6,-1,10,-6],[-10,-10,-8,5,-5,-5,-10,-8,5,1,10,3,-5,-9],[-2,10,10,4,-4,-7,3,9,2,10,-9,-5,-8,-6],[-3,-10,8,6,-1,-5,1,-5,-5,-8,2,-4,8,1],[-8,-9,-2,7,-10,-7,3,-9,7,9,-10,8,-4,4],[-2,5,2,2,-6,5,1,-8,-5,9,3,-5,-2,7],[-7,-7,6,10,8,3,10,10,1,6,-7,9,10,2],[-8,9,10,4,-7,-5,8,-9,-7,2,8,-5,2,4],[-9,-7,5,-2,-1,10,-5,-5,4,-3,-2,10,-2,3],[-10,-9,5,-6,1,5,6,-2,-10,-4,-8,7,2,9],[4,-10,-9,3,-5,4,7,-10,5,-4,10,9,-4,9],[8,10,10,-6,10,-4,-6,-5,-8,-8,8,5,-9,-5],[5,-9,-1,-2,-2,9,8,1,2,9,-10,10,-10,-7],[1,3,7,6,-2,7,9,-8,-9,-2,-2,8,1,-1],[3,9,-1,10,4,-5,8,-2,10,-5,8,10,2,3],[8,-4,3,6,6,3,-6,6,-10,3,8,-1,-9,6],[10,5,-7,-2,-10,6,8,6,6,8,-2,-8,-8,7],[-9,-9,4,9,-2,-2,1,8,7,-3,-8,1,-1,2],[-5,7,4,2,-1,-1,-4,-5,3,6,9,-5,10,9],[-4,-1,2,4,5,7,-9,-6,3,9,5,10,-5,-3],[2,4,-6,6,2,-5,-5,10,-1,6,8,-4,3,8],[-10,2,-4,-7,-1,8,4,-10,-6,-3,-7,-4,8,-9],[-1,-8,-10,2,-9,4,-3,-5,8,6,-8,-10,1,1],[2,-8,-8,4,1,2,7,9,-10,9,-2,1,-5,6],[-5,-5,10,1,-2,-4,3,2,-3,1,7,-9,-4,-2]], dtype = "int32")#candidate|7215|(98, 14)|const|int32
call_7214 = relay.TupleGetItem(func_5062_call(relay.reshape(const_7215.astype('int32'), [14, 14, 7])), 0)
call_7216 = relay.TupleGetItem(func_5065_call(relay.reshape(const_7215.astype('int32'), [14, 14, 7])), 0)
output = relay.Tuple([bop_7209,call_7214,const_7215,])
output2 = relay.Tuple([bop_7209,call_7216,const_7215,])
func_7221 = relay.Function([var_7207,var_7208,], output)
mod['func_7221'] = func_7221
mod = relay.transform.InferType()(mod)
var_7222 = relay.var("var_7222", dtype = "uint8", shape = (16, 7, 8))#candidate|7222|(16, 7, 8)|var|uint8
var_7223 = relay.var("var_7223", dtype = "uint8", shape = (16, 7, 8))#candidate|7223|(16, 7, 8)|var|uint8
output = func_7221(var_7222,var_7223,)
func_7224 = relay.Function([var_7222,var_7223,], output)
mutated_mod['func_7224'] = func_7224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4619_call = mod.get_global_var('func_4619')
func_4621_call = mutated_mod.get_global_var('func_4621')
call_7226 = func_4619_call()
call_7227 = func_4619_call()
output = relay.Tuple([call_7226,])
output2 = relay.Tuple([call_7227,])
func_7230 = relay.Function([], output)
mod['func_7230'] = func_7230
mod = relay.transform.InferType()(mod)
mutated_mod['func_7230'] = func_7230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7230_call = mutated_mod.get_global_var('func_7230')
call_7231 = func_7230_call()
output = call_7231
func_7232 = relay.Function([], output)
mutated_mod['func_7232'] = func_7232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2968_call = mod.get_global_var('func_2968')
func_2970_call = mutated_mod.get_global_var('func_2970')
call_7233 = func_2968_call()
call_7234 = func_2968_call()
output = relay.Tuple([call_7233,])
output2 = relay.Tuple([call_7234,])
func_7244 = relay.Function([], output)
mod['func_7244'] = func_7244
mod = relay.transform.InferType()(mod)
output = func_7244()
func_7245 = relay.Function([], output)
mutated_mod['func_7245'] = func_7245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4790_call = mod.get_global_var('func_4790')
func_4792_call = mutated_mod.get_global_var('func_4792')
call_7259 = relay.TupleGetItem(func_4790_call(), 0)
call_7260 = relay.TupleGetItem(func_4792_call(), 0)
output = call_7259
output2 = call_7260
func_7300 = relay.Function([], output)
mod['func_7300'] = func_7300
mod = relay.transform.InferType()(mod)
mutated_mod['func_7300'] = func_7300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7300_call = mutated_mod.get_global_var('func_7300')
call_7301 = func_7300_call()
output = call_7301
func_7302 = relay.Function([], output)
mutated_mod['func_7302'] = func_7302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1905_call = mod.get_global_var('func_1905')
func_1907_call = mutated_mod.get_global_var('func_1907')
call_7306 = func_1905_call()
call_7307 = func_1905_call()
func_7230_call = mod.get_global_var('func_7230')
func_7232_call = mutated_mod.get_global_var('func_7232')
call_7316 = relay.TupleGetItem(func_7230_call(), 0)
call_7317 = relay.TupleGetItem(func_7232_call(), 0)
output = relay.Tuple([call_7306,call_7316,])
output2 = relay.Tuple([call_7307,call_7317,])
func_7325 = relay.Function([], output)
mod['func_7325'] = func_7325
mod = relay.transform.InferType()(mod)
output = func_7325()
func_7326 = relay.Function([], output)
mutated_mod['func_7326'] = func_7326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1411_call = mod.get_global_var('func_1411')
func_1413_call = mutated_mod.get_global_var('func_1413')
call_7334 = func_1411_call()
call_7335 = func_1411_call()
func_2243_call = mod.get_global_var('func_2243')
func_2244_call = mutated_mod.get_global_var('func_2244')
call_7336 = relay.TupleGetItem(func_2243_call(), 0)
call_7337 = relay.TupleGetItem(func_2244_call(), 0)
output = relay.Tuple([call_7334,call_7336,])
output2 = relay.Tuple([call_7335,call_7337,])
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
func_6574_call = mod.get_global_var('func_6574')
func_6576_call = mutated_mod.get_global_var('func_6576')
call_7376 = relay.TupleGetItem(func_6574_call(), 0)
call_7377 = relay.TupleGetItem(func_6576_call(), 0)
func_2476_call = mod.get_global_var('func_2476')
func_2478_call = mutated_mod.get_global_var('func_2478')
call_7378 = func_2476_call()
call_7379 = func_2476_call()
output = relay.Tuple([call_7376,call_7378,])
output2 = relay.Tuple([call_7377,call_7379,])
func_7388 = relay.Function([], output)
mod['func_7388'] = func_7388
mod = relay.transform.InferType()(mod)
mutated_mod['func_7388'] = func_7388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7388_call = mutated_mod.get_global_var('func_7388')
call_7389 = func_7388_call()
output = call_7389
func_7390 = relay.Function([], output)
mutated_mod['func_7390'] = func_7390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7300_call = mod.get_global_var('func_7300')
func_7302_call = mutated_mod.get_global_var('func_7302')
call_7492 = func_7300_call()
call_7493 = func_7300_call()
output = relay.Tuple([call_7492,])
output2 = relay.Tuple([call_7493,])
func_7517 = relay.Function([], output)
mod['func_7517'] = func_7517
mod = relay.transform.InferType()(mod)
mutated_mod['func_7517'] = func_7517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7517_call = mutated_mod.get_global_var('func_7517')
call_7518 = func_7517_call()
output = call_7518
func_7519 = relay.Function([], output)
mutated_mod['func_7519'] = func_7519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3504_call = mod.get_global_var('func_3504')
func_3506_call = mutated_mod.get_global_var('func_3506')
call_7602 = relay.TupleGetItem(func_3504_call(), 0)
call_7603 = relay.TupleGetItem(func_3506_call(), 0)
output = call_7602
output2 = call_7603
func_7610 = relay.Function([], output)
mod['func_7610'] = func_7610
mod = relay.transform.InferType()(mod)
mutated_mod['func_7610'] = func_7610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7610_call = mutated_mod.get_global_var('func_7610')
call_7611 = func_7610_call()
output = call_7611
func_7612 = relay.Function([], output)
mutated_mod['func_7612'] = func_7612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4790_call = mod.get_global_var('func_4790')
func_4792_call = mutated_mod.get_global_var('func_4792')
call_7668 = relay.TupleGetItem(func_4790_call(), 0)
call_7669 = relay.TupleGetItem(func_4792_call(), 0)
var_7680 = relay.var("var_7680", dtype = "float64", shape = (10, 11, 3))#candidate|7680|(10, 11, 3)|var|float64
bop_7681 = relay.subtract(call_7668.astype('int64'), var_7680.astype('int64')) # shape=(10, 11, 3)
bop_7684 = relay.subtract(call_7669.astype('int64'), var_7680.astype('int64')) # shape=(10, 11, 3)
const_7687 = relay.const([[[-1,-9,-10],[3,-1,5],[5,-8,-2],[-7,-4,5],[-6,8,-2],[-5,-5,3],[-7,1,5],[5,-7,8],[9,-2,-4],[-7,-3,-6],[5,-1,-8]],[[-8,-3,2],[6,-9,-4],[2,4,-8],[-10,9,-2],[-10,6,9],[-6,-10,-7],[-6,-2,4],[3,9,8],[4,-2,1],[7,1,5],[-9,7,1]],[[-4,7,-3],[3,-6,1],[-2,4,-7],[-8,-10,-10],[-8,-7,8],[1,6,-9],[-8,5,5],[-10,1,10],[10,-4,8],[-5,-5,-3],[2,-7,3]],[[-9,6,-7],[-10,-7,10],[10,-7,10],[10,-4,-8],[10,-3,2],[2,-9,5],[-1,-10,5],[10,-9,2],[2,5,-9],[-5,6,-5],[-3,10,-9]],[[-7,-10,-1],[-8,2,7],[9,6,-7],[6,5,9],[-10,8,6],[7,-8,-2],[-3,9,8],[-9,-7,-10],[1,6,9],[7,2,9],[5,-3,4]],[[1,6,3],[7,-2,9],[9,-9,8],[-4,7,-10],[-6,-6,-7],[6,6,-9],[-9,-2,-9],[4,-1,-6],[-3,1,6],[10,-8,5],[-7,-3,-5]],[[3,-9,7],[-4,-7,-8],[-3,3,2],[-7,5,9],[3,1,8],[-8,-3,5],[-4,-5,-5],[6,-3,-2],[-2,9,8],[-7,5,-7],[-7,-5,-2]],[[2,-1,-1],[-9,4,7],[9,7,-5],[8,-6,-10],[-8,-5,-7],[3,-5,6],[3,-4,-7],[3,8,-6],[6,7,-6],[2,5,-7],[6,-4,6]],[[-8,5,-4],[-1,-10,6],[6,-7,4],[1,7,3],[8,4,2],[-2,-9,-2],[-7,1,-6],[3,-8,2],[-6,-8,-8],[-7,-2,-8],[2,-7,-5]],[[5,4,1],[-2,-9,-5],[-4,5,-5],[3,-1,4],[-1,1,9],[-7,-10,-8],[-10,-7,3],[-3,4,7],[2,1,6],[5,2,-5],[2,3,2]]], dtype = "int64")#candidate|7687|(10, 11, 3)|const|int64
bop_7688 = relay.mod(bop_7681.astype('float32'), relay.reshape(const_7687.astype('float32'), relay.shape_of(bop_7681))) # shape=(10, 11, 3)
bop_7691 = relay.mod(bop_7684.astype('float32'), relay.reshape(const_7687.astype('float32'), relay.shape_of(bop_7684))) # shape=(10, 11, 3)
func_1574_call = mod.get_global_var('func_1574')
func_1575_call = mutated_mod.get_global_var('func_1575')
call_7695 = relay.TupleGetItem(func_1574_call(), 0)
call_7696 = relay.TupleGetItem(func_1575_call(), 0)
output = relay.Tuple([bop_7688,call_7695,])
output2 = relay.Tuple([bop_7691,call_7696,])
func_7704 = relay.Function([var_7680,], output)
mod['func_7704'] = func_7704
mod = relay.transform.InferType()(mod)
mutated_mod['func_7704'] = func_7704
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7705 = relay.var("var_7705", dtype = "float64", shape = (10, 11, 3))#candidate|7705|(10, 11, 3)|var|float64
func_7704_call = mutated_mod.get_global_var('func_7704')
call_7706 = func_7704_call(var_7705)
output = call_7706
func_7707 = relay.Function([var_7705], output)
mutated_mod['func_7707'] = func_7707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5253_call = mod.get_global_var('func_5253')
func_5254_call = mutated_mod.get_global_var('func_5254')
call_7757 = relay.TupleGetItem(func_5253_call(), 1)
call_7758 = relay.TupleGetItem(func_5254_call(), 1)
func_4773_call = mod.get_global_var('func_4773')
func_4775_call = mutated_mod.get_global_var('func_4775')
call_7775 = relay.TupleGetItem(func_4773_call(), 1)
call_7776 = relay.TupleGetItem(func_4775_call(), 1)
output = relay.Tuple([call_7757,call_7775,])
output2 = relay.Tuple([call_7758,call_7776,])
func_7789 = relay.Function([], output)
mod['func_7789'] = func_7789
mod = relay.transform.InferType()(mod)
output = func_7789()
func_7790 = relay.Function([], output)
mutated_mod['func_7790'] = func_7790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7230_call = mod.get_global_var('func_7230')
func_7232_call = mutated_mod.get_global_var('func_7232')
call_7819 = relay.TupleGetItem(func_7230_call(), 0)
call_7820 = relay.TupleGetItem(func_7232_call(), 0)
output = call_7819
output2 = call_7820
func_7821 = relay.Function([], output)
mod['func_7821'] = func_7821
mod = relay.transform.InferType()(mod)
output = func_7821()
func_7822 = relay.Function([], output)
mutated_mod['func_7822'] = func_7822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4364_call = mod.get_global_var('func_4364')
func_4366_call = mutated_mod.get_global_var('func_4366')
call_7830 = func_4364_call()
call_7831 = func_4364_call()
func_6377_call = mod.get_global_var('func_6377')
func_6380_call = mutated_mod.get_global_var('func_6380')
const_7838 = relay.const([4,3,8,-6,-7,-4,8,-1,-6,1,9,-2,8,8,-4,7,9,-5,7,4,8,9,9,3,8,-9,-1,-5,-5,-6,-7,8,2,7,-9,-5,8,6,-3,-3,2,9,7,2,-8,2,1,3,7,5,10,-6,-6,-4,-1,2,-2,-7,-5,-10,9,-8,6,-4,-1,1,-10,8,9,-5,-2,6,-7,1,-3,-5,-7,-3,-4,5,5,-7,-7,1,8,8,4,-1,6,3,7,10,-2,-6,-9,4,-1,10,-5,-3,6,2,-3,1,7,7,-3,-7,-3,3,-3,7,-7,9,-6,6,4,-4,-9,6,-8,-9,3,7,-8,-7,7,-5,9,-8,-8,8,2,-1,-8,8,-2,-8,2,3,4,-1,2,-7,1,7,-2,3,9,-5,-1,-3,-2,9,4,6,-2,1,4,-6,-3,-4,7,9,1,1,6,6,4,-4,7,-8,-6,2,7,2,-10,5,6,-3,7,-9,-9,3,-2,2,4,10,-7,7,-10,-3,9,-8,-3,2,-7,5,7,9,-4,1,-1,7,3,3,6,6,6,-10,4,-1,4,7,5,-1,7,8,-2,5,10,9,-5,-1,8,4,-3,5,2,-1,7,7,-3,-1,1,-10,-7,-6,3,-5,-1,5,3,-5,1,3,7,4,-6,-7,-5,7,6,-2,5,2,-6,1,-8,-4,10,8,9,9,9,4,3,-5,7,9,-7,-7,7,-10,-6,-5,4,-6,-5,10,-9,9,-6,-10,-2,-4,-10,-9,10,-4,-6,3,-2,4,-3,3,-9,-5,-7,-7,-4,7,1,-2,9,-7,5,-4,-10,6,5,7,-4,-8,-9,-1,5,6,-5,-8,6,-9,7,2,4,-5,7,-2,6,3,4,-6,-1,-6,5,-3,9,-6,5,-8,-5,-9,-4,-5,-10,6,2,4,8,-10,-2,-6,4,9,-7,2,1,6,2,-6,10,8,-3,3,-2,4,7,5,1,3,-5,2,8,-1,-7,-5,-8,9,7,5,-7,3,1,9,4,-10,9,-4,9,-7,2,-5,9,4,-6,-5,-9,10,8,2,1,2,-3,7,2,10,8,-6,7,-4,2,7,10,1,-5,2,4,-8,-2,3,-10,10,8,6,-10,10,10,3,-3,7,-9,7,-5,-2,-1,3,-8,9,10,1,6,10,-7,5,7,-1,3,10,3,4,-9,-5,-9,2,2,9,-5,3,2,-5,9,7,-3,7,3,10,-10,10,9,-9,7,6,-7,-7,6,9,-9,-5,-5,8,8,9,-3,7,1,3,-4,-2,-10,1,3,9,-8,4,-1,-9,-2,-4,7,9,7,-6,10,3,8,-6,-8,3,-1,9,-1,10,-9,8,-6,-4,8,-8,-1,-8,7,-8,-9,2,7,-2,2,-2,6,6,9,-9,-3,5,7,1,-7,10,-1,6,4,8,9,4,2,-9,2,-7,-4,9,6,-5,2,-9,-6,4,-4,-3,-2,8,10,2,7,9,4,1,9,-4,-1,-5,-9,-6,-1,4,7,5,3,-9,9,-2,-7,2,10,8,-1,10,-4,-1,-5,-6,10,2,-1,4,1,4,2,6,3,5,9,-2,-2,-5,9,-1,-5,10,6,-9,-3,-6,8,-9,6,-3,-1,-5,7,10,-3,4,-6,5,10,8,6,8,-6,5,1,4,-4,-5,-8,8,7,-1,-6,-4,2,-10,6,4,-3,3,-8,5,5,-4,4,8,2,4,-8,4,10,2,-2,-7,5,10,-8,-5,5,-8,1,-2,-7,-3,-3,-9,-3,-9,7,-9,-8,6,-3,1,-2,9,-6,10,-7,10,-4,-5,10,-9,1,-7,-6,-7,8,7,6,5,6,5,10,3,4,10,-1,-9,8,3,3,-1,9,-2,3,-7,5,-10,9,9,-9,-7,8,5,6,-8,-10,-9,-8,-6,-8,-7,6,8,-1,1,5,-2,-6,7,-5,-10,-5,-5,-9,3,3,2,7,7,6,10,3,-2,-9,10,7,10,-8,4,-6,-9,-9,8,-1,-6,10,6,-9,4,-1,-3,-4,-10,-10,4,-3,2,-3,10,5,1,-3,1,-7,-2,-9,7,-8,8,1,-3,-4,-8,7,-1,1,10,-10,6,7,-8,-2,10,1,-9,1,-9,-7,5,5,6,9,2,6,7,-5,-10,1,9,1,6,-8,-10,-4,-8,-1,4,10,-9,5,10,2,-9,3,7,-5,-7,-10,9,9,4,10,10,-6,-8,5,-1,9,2,-9,5,3,-9,8,8,5,-7,-10,7,-6,-6,-3,1,-8,-6,-3,-9,3,-9,7,-8,9,-9,4,6,-1,2,1,7,-6,6,-6,-8,-4,1,4,4,-5,-4,-1,9,-7,5,4,-9,7,-4,10,-1,6,-6,1,6,4,-7,4,-6,-8,-1,5,7,-3,4,-10,8,8,8,5,-9,8,4,5,5,3,8,-5,-1,-5,-2,3,-2,-7,2,8,2,1,-10,-8,-10,8,-8,-2,-1,-5,3,-6,-8,-7,4,-4,-1,-2,1,-5,-8,8,6,-6,-10,-4,8,-8,-1,-9,-10,1,7,-2,1,9,10,9,1,5,-6,-2,8,-3,5,-4,-4,-6,-8,1,-6,3,10,-4,-9,2,-9,-2,-4,-6,6,4,6,-4,10,8,-8,4,4,10,-8,-9,-7,-3,-5,-10,10,-4,3,5,-3,-9,-3,-10,-10,8,-5,2,7,2,4,-6,3,-3,6,-2,-10,-2,6,1,4,-4,8,10,-3,9,4,4,-5,-6,6,10,10,10,-5,2,2,-10,-1,-6,-5,-2,10,6,2,6,3,5,-9,-9,-7,6,6,8,8,-4,10,-2,1,-6,4,-2,-10,-10,3,3,-2,-1,-7,-8,4,-10,7,5,-1,-2,2,4,4,-3,3,8,7,6,8,-8,7,7,1,-3,-2,9,-2,8,-7,2,6,-7,-9,6,-8,-2,-4,8,-10,8,-9,-9,-10,-4,7,6,6,-8,-6,-4,3,-9,4,2,2,9,-9,-10,-5,-7,-10,10,8,-1,-4,-1,1,-4,9,3,6,-3,-10,3,9,10,4,-7,7,7,5,10,7,-2,-10,10,-7,-8,-9,-4,2,2,-3,-6,-9,6,2,1,-10,8,8,-3,-4,-3,5,-3,-1,-10,-4,-9,-1,8,-10,3,-1,-9,2,5,-4,-10,6,-5,8,3,4,-6,6,-10,-2,6,7,-4,7,4,-6,2,8,10,5,-10,5,5,2,8,10,9,7,-6,-1,-8,9,-10,9,4,5,-2,2,4,5,-9,-5,-4,-2,-9,-5,3,-8,10,4,9,8,10,1,3,5,2,-2,4,-1,8,-9,9,-5,7,4,9,-9,1,2,-7,8,8,-8,-4,5,-6,-5,4,-5,-7,8,1,4,7,-10,6,-6,7,-7,4,5,8,4,-7,-4,-7,2,-10,-2,4,-1,-9,5,2,9,5,3,-3,7,5,-6,-4,8,5,-10,3,9,2,-10,-7,-8,2,-10,-10,4,-10,6,9,9,6,-2,3,-1,-5,-9,7,-7,-1,-3,-3,4,7,9,-6,1,8,-10,-5,7,-9,4,-6,-6,-9,-7,8,-8,-3,-3,7,-10,-7,7,-9,-4,3], dtype = "uint8")#candidate|7838|(1365,)|const|uint8
call_7837 = relay.TupleGetItem(func_6377_call(relay.reshape(const_7838.astype('uint8'), [7, 195])), 0)
call_7839 = relay.TupleGetItem(func_6380_call(relay.reshape(const_7838.astype('uint8'), [7, 195])), 0)
output = relay.Tuple([call_7830,call_7837,const_7838,])
output2 = relay.Tuple([call_7831,call_7839,const_7838,])
func_7848 = relay.Function([], output)
mod['func_7848'] = func_7848
mod = relay.transform.InferType()(mod)
mutated_mod['func_7848'] = func_7848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7848_call = mutated_mod.get_global_var('func_7848')
call_7849 = func_7848_call()
output = call_7849
func_7850 = relay.Function([], output)
mutated_mod['func_7850'] = func_7850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6067_call = mod.get_global_var('func_6067')
func_6068_call = mutated_mod.get_global_var('func_6068')
call_7874 = relay.TupleGetItem(func_6067_call(), 0)
call_7875 = relay.TupleGetItem(func_6068_call(), 0)
func_1768_call = mod.get_global_var('func_1768')
func_1770_call = mutated_mod.get_global_var('func_1770')
var_7919 = relay.var("var_7919", dtype = "float64", shape = (330,))#candidate|7919|(330,)|var|float64
call_7918 = relay.TupleGetItem(func_1768_call(relay.reshape(var_7919.astype('float64'), [10, 11, 3])), 2)
call_7920 = relay.TupleGetItem(func_1770_call(relay.reshape(var_7919.astype('float64'), [10, 11, 3])), 2)
func_2064_call = mod.get_global_var('func_2064')
func_2066_call = mutated_mod.get_global_var('func_2066')
call_7928 = relay.TupleGetItem(func_2064_call(relay.reshape(call_7874.astype('uint8'), [16, 13, 6])), 0)
call_7929 = relay.TupleGetItem(func_2066_call(relay.reshape(call_7874.astype('uint8'), [16, 13, 6])), 0)
output = relay.Tuple([call_7874,call_7918,var_7919,call_7928,])
output2 = relay.Tuple([call_7875,call_7920,var_7919,call_7929,])
func_7939 = relay.Function([var_7919,], output)
mod['func_7939'] = func_7939
mod = relay.transform.InferType()(mod)
mutated_mod['func_7939'] = func_7939
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7940 = relay.var("var_7940", dtype = "float64", shape = (330,))#candidate|7940|(330,)|var|float64
func_7939_call = mutated_mod.get_global_var('func_7939')
call_7941 = func_7939_call(var_7940)
output = call_7941
func_7942 = relay.Function([var_7940], output)
mutated_mod['func_7942'] = func_7942
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7961 = relay.var("var_7961", dtype = "float32", shape = (12, 11, 1))#candidate|7961|(12, 11, 1)|var|float32
const_7962 = relay.const([[[-1.442680,0.374652,-5.109048,-4.702543,-3.784625,5.370343,6.758427,7.110576,4.186711,3.243731,1.307779,-6.239742,1.624852,9.824401,-9.898847,1.524182],[8.493307,8.699320,3.080421,5.106039,-8.062927,-8.592450,-2.046385,-9.243266,6.864800,9.356838,-7.755133,-7.796194,-4.524752,0.346751,-8.464914,4.882820],[-9.829730,5.402643,5.147895,4.357806,-5.706769,4.434858,6.679916,-9.425381,-2.382201,8.774620,8.205862,-6.982807,8.933203,-6.161334,6.142557,-6.173086],[-7.368165,4.167494,-2.430466,-8.592167,-2.322852,3.108121,0.192724,5.597746,-9.533763,-5.451630,-0.985944,8.268729,6.885252,0.254165,6.069168,-4.054451],[2.257028,9.517325,-1.922271,-8.144641,-1.787811,-7.340943,-3.754710,2.552635,-2.760799,-7.953082,-1.056647,-7.379473,-3.733295,-2.765046,2.283339,3.829783],[-0.520701,8.559510,-5.528861,-7.895079,0.053287,-8.633460,-8.629979,-1.616961,-8.579305,5.945741,-1.646112,-8.893644,9.302672,4.547245,6.984827,3.721050],[9.157265,-2.315742,2.565021,-1.253712,3.266838,-4.346123,-8.871783,-8.386941,6.444497,-1.978188,3.565651,-7.611444,1.708762,-6.286155,1.818236,8.590358],[-6.947904,-9.240443,-9.516555,-0.226099,-7.168070,7.691006,-7.187437,5.030685,0.006180,1.568416,-3.669878,0.760183,5.870268,-0.671349,4.261863,-9.460358],[8.015443,9.208134,3.774646,2.640451,-9.026116,2.496292,-3.219754,7.036551,-7.458847,-8.594658,-6.134443,-1.009331,0.501398,-2.467714,-5.191050,-1.634805],[-7.309332,9.822950,-4.877665,7.248796,4.113417,6.574552,2.305105,7.728570,8.521816,-4.712214,4.852957,-0.930256,6.550275,-7.206426,9.442176,9.451683],[-1.261294,1.191297,5.275954,-7.385162,8.559088,-8.904371,-4.199859,-7.363238,6.688523,1.817787,-6.639773,-4.038318,2.242726,7.919844,1.850462,-8.150945]],[[-1.786474,-2.138845,-3.459106,-1.960957,-0.718626,-8.531157,6.783423,1.105420,9.956846,4.088239,-0.725648,2.112686,-7.423133,-4.354297,2.842988,-9.885045],[-9.579954,7.673489,5.887831,5.956778,-5.494098,-6.066899,-6.655062,-9.624606,-8.497962,7.698259,6.411069,-7.873703,-5.205864,-4.814306,4.720261,3.332845],[4.288245,-0.162189,-2.330127,5.247811,8.209522,-2.760881,4.243454,9.344241,1.093882,-4.607606,5.347262,-3.539689,9.641380,1.597416,2.650349,-9.365006],[0.081113,3.285170,-3.274808,-1.674319,-1.406791,-0.123976,-4.206417,-8.903162,-3.330527,-9.556045,1.485933,6.192710,7.770246,-2.745867,1.176973,-4.536047],[8.504366,8.934447,-4.183259,-9.877348,-1.747838,-8.819239,-2.117360,-0.860591,8.917156,0.141815,-1.843304,0.471226,2.411836,-5.760456,-7.060563,-5.247697],[3.310659,-1.693858,9.502290,-4.978960,9.001833,-1.942615,7.871743,-6.645900,-3.329896,-3.339586,0.553077,-9.282748,4.141166,0.952375,5.732894,3.966326],[4.937710,-0.566009,-2.536326,1.257862,7.024831,-9.007146,-3.627984,3.429857,-1.707823,0.161301,8.668688,-3.279732,2.244828,3.888288,2.539101,6.424464],[-6.561238,-7.292694,-4.388557,-4.787539,4.983347,7.832061,0.693286,-6.934061,-4.013678,1.477270,-8.525749,-7.082405,-6.060252,-9.880091,-6.272554,-0.713147],[-3.144742,-1.246549,-2.940952,-6.648289,6.769412,-8.899492,0.228184,-1.412542,-5.669281,5.144091,0.753326,-1.018014,7.978131,-6.217472,-4.095693,-7.990872],[2.428406,-6.647207,6.347339,1.719144,-3.527390,-7.623667,1.344582,2.488507,-5.712263,-6.963431,-1.729926,1.353071,1.636990,5.358688,8.392493,-2.579085],[-4.150581,-5.299658,-5.098342,-1.538460,7.132204,-8.894193,1.746705,7.467322,-2.201322,-6.140392,-2.678761,4.376631,6.996856,-5.901463,-8.626779,4.715132]],[[7.003672,2.617162,6.157935,-4.733958,-4.101420,7.399557,-6.482396,2.002018,-3.915853,8.555631,-6.852802,0.435532,7.167335,-8.597665,-2.636195,3.577285],[5.948736,3.663051,-3.531591,-4.586172,-5.183410,4.883626,-5.935626,-0.422632,-1.008288,4.181717,-7.540938,-3.796291,-2.748852,9.113985,-2.459410,-1.633807],[2.973505,-5.419092,6.028820,-0.253690,7.416959,-0.256517,1.622618,-3.452872,-0.067989,-5.348739,-1.630737,2.735915,6.920535,-3.996904,4.586283,7.625521],[-6.093476,-0.783215,-7.688967,-8.993894,-3.484724,8.277258,2.641627,5.321723,-3.119870,-4.051723,-0.858142,5.334035,-2.961015,1.508848,9.893580,4.017473],[2.742257,8.590484,-6.978678,7.745904,9.703422,-2.443499,-3.517871,-1.787522,4.567262,-0.308020,-7.064220,2.540756,9.675467,-3.948809,-1.277716,-4.829520],[-5.512838,3.847222,3.236233,9.654982,-5.279607,2.585567,-0.778786,1.625557,-0.849404,4.112438,2.370532,-6.193259,-2.832418,5.959356,-5.273445,-7.133019],[-3.575842,6.209251,-2.160593,-2.938188,9.746889,3.890720,2.389625,9.915766,-5.982497,9.970026,-9.945863,-7.795291,-9.020513,4.801531,-2.264403,7.598052],[9.646520,-4.434409,-8.149588,-1.003881,9.401139,7.844067,-1.053304,-9.987831,2.857508,4.173834,1.250876,-0.004515,6.294227,-5.999070,6.812717,-4.924206],[3.833819,-6.542437,7.779208,2.060614,0.648078,-8.710636,4.762574,-9.368456,-3.972604,-6.217246,-9.861191,0.785792,-6.938511,4.823852,-5.693377,0.021786],[-8.439811,4.553813,-4.754086,-6.752828,1.391119,-6.722917,-3.328426,7.110455,-4.319685,-2.840888,9.995303,-9.996510,-4.237130,1.917738,-9.536294,-9.266885],[7.184711,-4.003061,-3.084858,6.448449,2.948096,-5.357078,-9.468959,-9.390511,-0.157515,6.890117,7.699864,2.828593,7.867257,-3.420156,5.727109,6.975906]],[[-6.750266,9.324264,-5.228636,-7.639644,-9.804780,3.328344,-8.224349,3.944685,6.975319,-9.643241,-7.058773,-1.382666,5.092604,4.050811,7.800575,1.360140],[0.406806,-9.145524,3.515478,3.457551,9.896344,-9.009775,4.346460,-5.991644,7.040527,9.634244,8.291230,9.922291,-4.201780,6.397463,2.773146,4.363171],[3.977531,9.352822,-9.112350,-0.110995,6.416306,2.907624,-5.696778,9.672967,6.338489,-8.814210,-2.577878,5.311140,-1.604028,-5.161004,2.925363,-7.751299],[7.197639,1.726855,9.839199,-7.946092,-3.304287,7.728723,4.654150,-7.976225,7.322755,7.127489,6.407682,-6.606085,-0.049345,6.233138,-7.926385,-0.010889],[3.988886,6.927644,-9.261978,-2.449865,9.677141,7.240838,-9.892444,2.463175,-8.257929,-0.344914,8.720779,-4.509053,3.114460,1.544036,2.006383,-5.446103],[9.944464,0.783495,8.414183,4.105226,2.599473,8.291048,-7.226762,7.185230,-2.420983,-7.372044,-1.867348,7.746156,8.778669,6.860391,-0.062272,8.485565],[4.927134,4.770044,-6.070252,-6.052863,-1.689876,-2.273832,-2.289311,2.039955,2.908042,4.853193,-5.809799,6.006704,9.528372,1.101667,-0.947417,-3.535504],[5.106985,-5.955589,-4.931191,-2.005646,7.952108,6.711697,-5.974996,-9.185282,6.572641,-3.846575,-2.029628,8.050202,-3.721134,9.464993,5.383650,3.883673],[-9.013314,9.012951,-8.878085,7.788623,-9.316077,4.654803,1.785999,-2.039192,5.993944,7.180964,-5.979941,-5.987461,7.743774,-1.404903,5.135538,5.450927],[8.325173,-3.533553,-0.577144,3.424422,-4.809213,-0.884729,-6.622125,-4.506816,6.249647,0.998795,-9.006923,-7.177189,-0.325192,5.092099,-9.520759,7.993189],[1.603324,2.729001,8.648829,-2.165642,-1.531942,3.666697,9.360345,-3.869428,8.119082,-4.309141,0.696514,7.431002,1.318639,3.900342,-4.298069,-2.823773]],[[-9.042858,8.653822,-2.142907,-3.952634,-7.068421,-0.458182,0.892446,-6.020884,-7.795301,9.572352,-4.329166,4.563630,9.867670,4.321745,4.538427,3.286214],[-4.336661,2.354339,-6.417757,9.013072,-4.645487,-6.508138,-3.456447,-0.044014,4.833187,9.140082,6.136453,-8.021484,7.655727,-6.046632,6.330267,7.606622],[-4.032896,-9.222965,-1.305682,-0.590913,9.440887,-6.411838,8.168398,9.145293,-8.368726,-5.162982,2.111747,-1.133240,0.582894,-5.741291,-5.179281,-6.321009],[-4.837978,2.965259,-5.676963,8.092185,-5.086607,5.420544,4.189457,4.683956,2.294124,0.189904,-0.982007,-4.630650,-3.621908,-9.337259,-1.238177,4.532830],[4.963465,9.350571,-4.553207,-0.542296,-8.766873,0.372291,-8.217677,-0.075214,-4.296183,-3.893730,1.487595,-1.128391,9.051462,8.144106,8.709821,7.279284],[9.424247,-1.019192,7.551209,9.083980,9.267011,0.629993,1.891396,7.020695,5.915621,-2.429161,-5.480876,-9.764688,3.955174,9.597203,9.612527,4.556309],[8.487284,-5.351598,-3.428393,8.002665,-2.471784,6.157734,-3.160325,-3.978517,7.406293,-9.054751,4.419007,4.801653,-4.944756,-4.244332,3.341200,0.796197],[1.603236,-7.200590,0.618342,2.039503,-2.307380,2.691660,-7.957261,4.609647,-9.510399,6.625327,-6.556200,-9.051591,-9.912269,-3.961413,-5.048806,-5.310547],[-2.008877,-0.092616,-9.870908,0.192943,-0.452927,0.187893,-0.249832,-0.059271,4.120760,5.299930,9.638059,-8.230882,-7.800217,4.943731,-5.625652,-4.179257],[-0.505632,-4.727889,5.246395,-9.743045,-8.117983,-4.882394,-2.038342,0.072040,-8.580133,2.398300,-4.220016,6.812266,9.673642,-3.612008,0.858904,-3.436108],[4.464357,-2.958520,-0.015287,-8.773918,1.360170,-5.349532,-3.843014,8.791222,-8.268362,-5.492744,-1.990226,6.385966,-2.142618,-9.477556,-9.157279,-0.853899]],[[2.660319,-7.414069,2.125119,2.067635,7.826132,-8.870011,8.257253,7.179084,-7.415348,2.068556,8.746345,-3.745216,-0.560181,8.249022,9.864457,-8.019230],[5.775842,4.794855,9.240353,3.129295,-8.898797,-1.371049,0.583824,4.263401,4.173379,-8.163564,1.609459,0.229984,8.946101,-6.815909,-3.595221,-0.476486],[-0.008721,-1.118998,-4.405955,-9.641771,8.904053,-8.312275,-1.373967,-4.806537,-0.498066,1.704803,-8.219917,4.223381,0.813378,-3.283651,-3.518355,4.071741],[-8.162746,2.929337,9.758676,1.122242,-5.974775,4.570253,3.494493,9.725880,4.646798,3.470135,9.910763,6.174961,0.803165,-2.059345,-3.451313,-6.378753],[9.579774,3.191164,4.161010,4.983757,1.169270,2.739645,-5.855428,-1.427235,7.420627,9.689936,9.005160,2.255883,8.564663,-0.187995,-0.466622,-8.107820],[-9.631527,-5.414509,0.466188,-2.954742,5.238157,6.405157,-3.759060,2.613153,-7.769022,-3.155638,9.185500,-1.773738,7.024589,5.702051,0.149949,5.597047],[0.810611,3.653506,5.154359,5.306630,9.970388,-4.252635,2.362246,4.935199,8.217065,1.656197,-7.900298,6.094671,-9.374880,6.526780,-2.085582,-5.583040],[-1.576764,-9.545651,9.968495,-2.118372,9.070609,-9.075853,-7.400131,-9.427660,0.935453,3.763235,6.916342,7.532156,3.683615,6.856232,6.494728,6.898604],[6.561484,9.778004,-5.206849,-4.118432,-0.793841,-5.566986,-2.331534,-3.907155,-3.953440,1.661371,-7.360068,5.049702,9.328937,-0.870902,-9.159366,8.708224],[0.032007,-1.658495,-9.190653,6.712634,9.063644,-5.475737,-2.340411,5.180735,-6.269986,-4.849395,5.051668,-6.228002,-7.445409,8.092631,-8.875491,3.232777],[4.688998,9.895439,-7.442771,0.031425,-5.978097,8.002263,-0.321815,5.816597,-4.498829,-3.250334,-9.508790,-1.147130,3.219541,2.338491,-5.062233,9.972917]],[[9.816945,-7.448878,-3.185540,7.393557,5.365927,3.831133,-0.301805,-3.911499,7.436197,-4.412016,0.911871,-4.405537,0.775023,-0.691491,-8.309671,8.019443],[7.557263,8.107446,0.655024,-9.648875,-3.263887,1.156695,5.632969,8.035626,-8.455448,-1.601432,-2.967786,-9.761774,-2.650012,-4.296519,-1.026201,-9.024453],[4.327922,3.150359,9.798943,9.082104,-3.189169,-0.894034,-9.815224,-4.396255,7.189219,-9.329959,5.976465,1.251591,5.323975,7.546297,-7.916438,4.155946],[8.623317,-5.320308,0.676459,-5.927905,-5.166897,9.097338,-0.442300,4.631359,-6.848679,-6.363569,-5.190195,1.512275,9.567558,-9.486374,0.927253,3.648178],[-6.842452,9.240853,9.834363,6.196517,-7.557553,-9.330877,-2.136521,-2.073218,2.026050,5.331385,6.800140,9.314583,0.581202,-4.960410,-2.489932,3.786119],[4.720811,-6.126969,2.017693,9.251115,-2.359978,-3.269312,4.103110,0.047605,8.500215,7.266867,3.078109,6.167979,-0.514522,5.124833,9.013216,8.490101],[4.853390,1.629003,-0.554024,-9.075458,-4.767371,0.426753,-4.140440,-2.194516,3.361654,-0.352133,8.613329,9.374884,1.468771,-6.247074,-6.396230,0.461051],[9.732194,-6.132790,6.168369,-4.326628,6.327670,-0.401535,-4.216195,-0.081044,-5.939011,-0.612470,-1.830229,6.558698,7.567630,5.192449,4.629384,0.323828],[2.455174,-8.368928,0.499324,7.094454,6.267351,-4.257968,-6.954223,8.697846,1.405485,-9.112674,-2.118797,6.599388,6.175443,3.043519,4.118028,6.460229],[-8.940885,-3.408404,-6.427769,-4.790940,5.759484,0.156834,1.953718,-3.646671,8.044769,6.132093,-4.973255,1.503763,7.939606,-3.439352,3.041157,8.333179],[-6.556300,5.961398,8.881023,-7.996156,-2.323927,0.126766,-1.642290,-9.258475,-2.077283,7.639014,-5.584968,5.469917,8.795421,1.769452,8.856544,-6.293847]],[[-2.622947,9.287351,-4.015651,-8.110888,8.936955,-3.690214,4.269240,1.875789,-4.240062,-3.220981,3.134320,-4.558095,4.369214,-0.268587,1.714243,-7.681945],[-8.688086,6.691248,3.311181,-4.706169,6.533963,3.523005,4.097004,0.477770,1.487292,1.391122,1.684863,-1.866690,0.439465,0.136383,3.422305,-0.815269],[7.954660,-3.958737,1.626167,-5.200017,-5.126244,5.969472,-8.158510,1.513348,-5.528877,4.115675,9.783351,-5.585996,-3.260983,5.379366,-9.157313,0.337637],[1.247851,-5.935448,-3.506641,-7.148681,-8.013888,9.911529,-6.581886,5.117078,6.915130,-0.168242,-8.737851,4.198436,-5.827755,-7.151034,-2.290252,8.765022],[-6.867494,-2.971035,-9.458618,3.364213,-3.050286,3.792828,6.994634,5.253692,2.140246,0.125884,-8.198877,-9.118422,3.160601,6.461069,2.317806,-7.381584],[2.638854,-0.737363,2.118310,-8.839856,-0.544185,-7.527615,-4.596003,-4.587494,1.952627,8.687840,-3.183309,-1.103499,0.388377,6.525010,-5.303611,-8.280341],[-7.452699,9.190167,-3.146517,8.072827,-6.311582,-7.721247,9.623541,-6.646180,5.660506,4.796162,-7.497851,0.655926,8.067512,-5.999851,-8.832873,9.559367],[2.616103,-9.078429,6.518147,4.980839,5.251361,-5.972548,-0.046277,0.492206,5.167059,-2.777892,7.538178,0.521325,-6.361467,-4.612579,-7.872556,-1.150527],[5.415941,2.257251,-5.887221,-0.812706,-3.910115,0.059266,2.263449,-8.710502,0.242236,-8.658010,7.071730,6.222942,4.445342,-9.989180,-7.886580,-6.417733],[-7.733955,-0.075744,-4.803361,-4.144431,2.208553,6.459254,9.101278,2.690102,-9.540320,5.357215,0.895529,-1.841395,-6.429035,-2.521171,5.979845,-7.182613],[-7.548715,-6.805453,7.649308,-7.030881,-4.338684,-4.773607,9.270947,-3.902916,2.659854,8.498911,4.028970,-9.320751,3.790733,-5.449967,3.599711,-4.283702]],[[3.357402,-4.343710,9.091642,8.603593,-5.771720,9.119266,-2.193192,-3.418993,9.888851,-8.176449,5.128128,3.950736,-2.140130,3.544342,-6.715740,4.610472],[-7.057451,0.070739,-7.344572,-3.353679,-0.139968,6.256523,5.822598,-0.289768,3.780046,8.585651,0.175858,2.609282,-8.558677,1.164134,-2.116889,-5.650025],[-8.291776,1.471308,3.869050,-8.958410,3.430274,-5.283308,9.570501,-7.546732,3.267315,3.663572,-3.827653,-5.539603,8.797881,8.349422,3.994454,-9.042099],[5.508799,-2.363215,4.054322,-3.392850,-3.669429,-4.809571,-4.587074,4.479455,-6.607688,-4.162529,5.135091,-3.220519,0.633275,3.185750,2.912600,-4.149942],[9.241528,5.434508,8.226094,9.036478,-6.903217,7.453670,-8.323953,2.725367,4.640407,9.099860,-3.973633,3.424891,-1.505098,-5.405400,2.946154,-7.270272],[-7.024478,9.605603,-6.181323,8.949475,-9.284322,5.613158,2.249855,-8.313428,-7.647786,-6.304169,4.499465,-5.183157,-4.039612,0.433175,-1.794655,-5.663054],[-2.306624,-9.793034,-9.806850,3.270434,8.898087,-7.797063,1.198563,7.852909,-8.750206,3.060020,-5.161399,7.372128,-2.719308,-7.876417,3.383456,4.846584],[-0.721593,-2.869003,-6.969312,-4.321937,-5.630422,-6.626053,1.032827,6.092534,1.857950,7.856027,6.499676,-4.559956,4.546638,-3.935285,0.491989,-7.917682],[9.466410,1.108826,1.778319,6.172950,-1.539031,8.872871,-4.943206,8.873894,8.087332,0.350086,-2.355624,3.691840,-0.987252,-5.708231,9.207322,5.350893],[9.373132,-7.701274,-7.751025,-0.071435,-2.200821,-2.086490,-5.220232,-7.781373,-3.524065,-5.256435,-7.015340,4.889550,8.784187,-2.460695,-8.033485,-0.119710],[-4.117918,-1.147202,-0.557869,9.004815,8.736408,8.621566,-9.405345,6.540682,5.850556,1.225429,6.295261,-3.530735,-5.728199,-7.842479,5.403557,-6.342348]],[[4.747248,-0.119704,4.316296,-0.586966,-3.292873,-5.544864,-4.298590,7.253437,-8.003340,8.761316,0.436807,-1.018744,-4.137837,7.536210,0.626518,-2.369002],[-0.732551,8.740731,-2.025131,-2.171409,3.380400,7.979088,2.905369,-9.683626,3.812534,9.027840,9.753237,-0.403200,-9.851321,7.683601,4.799001,4.961822],[3.764600,9.316300,-2.416104,-4.762551,0.325128,6.331610,-2.914024,-2.268246,6.033306,5.937641,0.959892,9.895015,7.320920,-6.676719,-1.361591,-8.223741],[-8.804756,3.262402,-1.213094,-5.996915,-8.356880,-6.107792,2.308877,-0.836246,-1.252178,-2.753754,-4.417935,-5.760085,-8.949295,-4.257679,-3.401301,-4.470959],[6.095715,9.645742,6.194301,7.417751,-5.698578,5.487767,-1.724625,-9.780656,8.984509,-0.966890,-1.727301,5.402649,9.872955,3.014299,-1.735728,-3.829961],[-9.913045,3.281667,-8.268682,0.664250,-2.036852,-9.250723,-0.322945,-8.154757,5.755504,8.075479,5.311800,8.240153,7.077321,-0.167710,-9.471833,9.201424],[-1.328210,2.700713,9.752493,5.059888,3.408331,-8.933764,9.734507,5.135254,7.585058,-0.591184,2.723761,-2.823540,2.478964,-3.114613,7.257049,-8.516980],[3.407310,-2.497948,-0.925058,-3.709183,-3.554436,0.764224,1.737506,-0.423528,-2.641291,9.336516,-0.821464,-6.653086,-3.414911,-8.073908,-1.124149,-4.119095],[-6.185264,-5.480911,-5.610527,-2.413301,3.326531,-5.671885,-0.035266,9.162102,-6.814084,-6.230953,-1.513896,-6.031785,4.868037,7.415044,6.928971,8.685153],[-8.032796,-0.794541,0.397553,5.386730,-1.469833,3.371051,6.077789,0.379594,-5.561456,-0.871882,-6.960951,5.982519,6.427464,3.066634,-9.476786,-6.933376],[-1.949031,-0.453585,9.179306,-9.061240,8.081403,-7.487439,4.658919,-5.685609,0.257350,-7.113375,1.373303,-2.532703,-3.840931,4.448386,-9.106260,-9.836391]],[[-2.270512,-1.445954,-7.825995,-9.379000,7.857158,-1.003264,-8.440028,-6.807466,-4.932647,-5.806770,-4.516871,-9.386733,-5.572071,-5.286526,-5.610624,-9.410686],[9.933370,-9.722172,8.579399,9.283188,-2.223403,0.426021,0.679187,-2.131011,9.051661,3.602468,2.880085,-1.544884,-3.453389,0.380145,2.316597,6.034600],[-9.655733,4.718239,-2.401139,-4.312356,-9.032999,-2.972013,8.011745,7.700205,4.561985,6.930162,6.598861,-3.673297,-5.773478,-4.346455,1.186487,-7.494428],[2.200596,-4.365568,-1.737004,-2.337924,-8.963800,-6.238571,-6.976109,-1.016424,4.400650,-5.459316,-7.798862,-0.441005,-5.947452,-7.148461,-0.391691,-2.785423],[-3.973493,-5.202562,8.225294,-9.918094,4.187581,-4.545055,-6.370224,7.893398,-2.783419,-2.553806,-4.754692,8.049948,4.296763,0.146622,-1.152075,-2.467847],[-9.555129,8.540997,5.517366,9.194857,6.059917,-5.898339,7.889224,8.214098,-4.907776,-8.553598,-1.479163,2.858409,8.263098,1.284187,-3.637143,3.030821],[-3.189186,7.282962,-0.570992,-2.196894,-1.425171,0.359949,-5.960366,0.257676,8.052304,-7.994951,8.292319,6.200379,-2.239938,-8.048361,-8.142761,5.789220],[-2.168489,3.208473,4.095873,-5.749765,-2.832289,0.042241,-0.609526,3.107344,-4.260668,7.629299,-7.416623,6.355237,-2.103161,1.397929,4.611030,9.568949],[4.737207,-1.824775,1.068203,-4.905433,-6.770815,-4.566885,-3.942562,-1.684238,5.445935,-8.994549,8.983581,-8.043125,8.554302,-8.793596,-2.992811,2.509489],[-1.001202,2.446062,-2.417342,-9.739802,1.681956,-3.618566,-7.241287,8.145157,-6.077830,8.586236,7.070219,0.923627,-3.603114,8.591239,-4.864022,-4.246214],[-0.190592,-3.624214,-8.042747,9.246155,2.626628,4.733590,5.956873,-0.833342,2.977359,1.648410,6.093926,8.249460,-8.120652,8.345322,3.010709,-2.169980]],[[3.380421,3.823270,8.156700,4.446574,-5.564915,-2.160851,7.498003,2.089323,2.144438,4.815275,-1.336949,-2.387084,8.096089,5.518700,8.275216,-1.244947],[-6.581144,-0.732170,9.565798,-2.988675,4.623705,2.495668,5.460972,8.189761,4.200688,-3.015531,0.769396,-5.309827,-0.824113,-7.606139,4.143013,-5.874552],[-7.832626,9.937647,-0.058370,4.662791,6.761608,4.971754,9.907333,0.397019,7.012561,-1.138293,-6.287415,-6.894723,-7.070280,-6.592453,5.837642,2.755399],[-4.713366,7.102963,1.109888,-3.765667,4.342889,3.965862,-9.116761,3.060573,-6.169039,-3.823933,5.843186,9.818274,3.033859,7.414066,-5.836867,-2.723911],[-2.874669,-3.888485,-4.404697,-6.385965,-1.366624,3.609848,-4.449005,-4.039810,-7.230753,8.474287,1.455166,-3.010030,-9.270631,-5.475668,-1.286544,1.861928],[-3.970217,-7.420686,-1.439338,9.200251,8.839742,9.754479,2.171479,-4.018446,4.993801,3.075720,5.002124,7.501019,-5.755201,-8.746382,0.951359,0.132570],[2.690959,-0.759675,-7.644556,-5.361055,-8.465542,5.730974,-0.104517,-0.868466,8.214336,-3.347282,0.279771,-6.005899,9.002706,-0.941734,8.758515,6.034967],[-4.882260,-3.021554,5.212308,-8.669077,1.983775,6.362151,1.170955,1.260161,-5.135243,2.293089,7.625049,8.139557,6.313935,4.165301,8.873581,4.033953],[0.202412,-2.431477,9.480852,-0.771299,-7.787226,-9.467293,5.661054,-1.412009,6.591662,7.135880,0.002411,-5.164334,7.752978,7.987297,-9.359473,-0.345738],[3.715979,-2.861206,5.661801,8.389413,-9.238479,8.404001,6.134710,5.932888,-2.311066,2.512039,0.193954,-3.163376,-5.659478,2.441328,-2.391819,-1.287831],[-6.591290,-4.882676,5.358674,3.934862,7.173745,-8.405821,-2.920242,-2.733731,-6.388683,0.992242,4.342868,-2.734643,1.362571,-5.867347,6.655757,6.630709]]], dtype = "float32")#candidate|7962|(12, 11, 16)|const|float32
bop_7963 = relay.mod(var_7961.astype('float32'), const_7962.astype('float32')) # shape=(12, 11, 16)
bop_7967 = relay.greater_equal(const_7962.astype('bool'), var_7961.astype('bool')) # shape=(12, 11, 16)
output = relay.Tuple([bop_7963,bop_7967,])
output2 = relay.Tuple([bop_7963,bop_7967,])
func_7971 = relay.Function([var_7961,], output)
mod['func_7971'] = func_7971
mod = relay.transform.InferType()(mod)
var_7972 = relay.var("var_7972", dtype = "float32", shape = (12, 11, 1))#candidate|7972|(12, 11, 1)|var|float32
output = func_7971(var_7972)
func_7973 = relay.Function([var_7972], output)
mutated_mod['func_7973'] = func_7973
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7978 = relay.var("var_7978", dtype = "float64", shape = (1, 5, 11))#candidate|7978|(1, 5, 11)|var|float64
const_7979 = relay.const([[[8.549645,-1.608637,-6.226339,9.330625,9.211304,-6.806102,-6.898991,-0.846683,2.505860,0.346043,-8.316653],[7.100687,-3.677973,-4.783179,3.481494,-6.616569,-9.483793,2.826068,9.511250,9.705377,2.822128,-7.883300],[-7.916172,8.346752,0.014364,-5.092380,6.157208,2.446626,-8.857926,8.557744,-1.848570,-3.889294,-5.476810],[5.546179,6.925837,4.654818,0.378033,-4.379559,-6.267966,4.409516,-4.644025,7.300009,6.123661,8.557678],[-6.606339,-5.892007,8.650864,5.700831,-0.274074,4.358281,-1.623904,-1.763878,-8.194501,9.745343,-9.894479]],[[-9.623419,-9.449137,2.696569,3.243439,-4.750217,8.945544,-2.106626,7.316101,-9.156406,-1.141301,1.171644],[-4.966455,-7.748849,5.065945,3.565144,4.837620,-4.305307,9.522773,1.127782,0.412417,8.397944,-0.967496],[1.126434,6.704124,-2.078953,9.147514,-3.933557,7.355998,-3.389124,-6.135884,7.226249,3.848472,-3.148987],[9.517829,8.642308,7.970629,5.139199,-4.680063,4.810676,-9.447179,-8.625253,-8.419602,-5.939185,7.698774],[-1.957189,-2.711082,7.687986,7.593884,9.400838,-0.820250,1.712443,8.681776,0.217896,8.888876,4.427680]]], dtype = "float64")#candidate|7979|(2, 5, 11)|const|float64
bop_7980 = relay.divide(var_7978.astype('float64'), const_7979.astype('float64')) # shape=(2, 5, 11)
func_7300_call = mod.get_global_var('func_7300')
func_7302_call = mutated_mod.get_global_var('func_7302')
call_7990 = func_7300_call()
call_7991 = func_7300_call()
output = relay.Tuple([bop_7980,call_7990,])
output2 = relay.Tuple([bop_7980,call_7991,])
func_8009 = relay.Function([var_7978,], output)
mod['func_8009'] = func_8009
mod = relay.transform.InferType()(mod)
var_8010 = relay.var("var_8010", dtype = "float64", shape = (1, 5, 11))#candidate|8010|(1, 5, 11)|var|float64
output = func_8009(var_8010)
func_8011 = relay.Function([var_8010], output)
mutated_mod['func_8011'] = func_8011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2019_call = mod.get_global_var('func_2019')
func_2020_call = mutated_mod.get_global_var('func_2020')
call_8037 = relay.TupleGetItem(func_2019_call(), 0)
call_8038 = relay.TupleGetItem(func_2020_call(), 0)
uop_8044 = relay.acosh(call_8037.astype('float32')) # shape=(16, 13, 6)
uop_8046 = relay.acosh(call_8038.astype('float32')) # shape=(16, 13, 6)
output = uop_8044
output2 = uop_8046
func_8068 = relay.Function([], output)
mod['func_8068'] = func_8068
mod = relay.transform.InferType()(mod)
output = func_8068()
func_8069 = relay.Function([], output)
mutated_mod['func_8069'] = func_8069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6067_call = mod.get_global_var('func_6067')
func_6068_call = mutated_mod.get_global_var('func_6068')
call_8086 = relay.TupleGetItem(func_6067_call(), 0)
call_8087 = relay.TupleGetItem(func_6068_call(), 0)
func_6175_call = mod.get_global_var('func_6175')
func_6177_call = mutated_mod.get_global_var('func_6177')
const_8101 = relay.const([-5,-6,9,1,-6,-6,-10,-5,-7,-9,3,2,3,2,-4,-6,9,-5,-2,6,1,3,6,6,-5,10,3,3,4,3,-8,4,3,-8,6,-2,-8,10,-5,7,-1,7,-7,-4,-6,8,8,-1,-3,-7,-5,-6,6,-6,2,10,-10,-1,-7,-9,-2,7,1,4,-1,3,-9,-10,4,-5,-1,4,-2,-2,2,2,-10,-5,-10,-5,9,8,6,5,6,-6,5,-10,-7,-5,-6,2,-7,9,5,8,-3,-1,4,8,-8,-7,-6,-9,1,-9,-1,3,7,5,7,7,-10,6,6,4,-8,-4,-9,-5,-7,9,7,-5,-3,8,4,7,-4,7,-9,-2,3,-1,-1,5,3,7,8,-6,-2,3,2,7,-5,7,-7,-10,7,5,8,-9,5,-2,-7,4,-7,-5,-6,-6,-9,4,-4,-6,-6,10,-10,6,4,-8,8,-2,8,-5,-2,-7,4,8,-8,10,5,7,-10,1,-8,-6,-3,-3,-8,7,-9,-4,6,2,6,7,1,-7,4,4,-8,-10,9,-4,-2,-10,5,-4,5,6,-8,-3,4,8,9,-2,2,-10,7,-1,-4,10,4,2,-1,-9,1,6,1,7,-9,6,1,4,1,7,-6,-7,-10,-10,-9,-10,2,-10,-3,2,4,-3,6,-4,-5,-4,-7,-3,-2,-8,1,-3,-3,5,-8,7,-7,-8,8,-1,3,3,-8,9,-9,-3,4,-3,-9,-4,-7,10,1,-8,1,1,-7,-6,-1,7,1,-10,7,3,-4,-2,9,-5,-1,-7,-4,-8,5,8,-8,-7,8,-5,3,-1,-6,7,7,4,-7,-2,-9,2,4,-9,-8,1,-6,-8,-4,-5,2,-6,8,-6,-10,3,-1,-5,-6,7,-3,-9,7,-7,6,3,-5,-6,-6,-5,-5,8,-7,8,9,7,-8,-8,-4,7,-6,8,9,4,10,-4,2,-10,-6,2,6,5,6,10,-10,-1,-9,-10,5,-8,5,-2,5,-6,10,4,7,-1,-7,-2,10,-3,-2,-9,-9,4,10,-1,-5,6,4,1,-1,2,-3,-5,10,2,-3,1,-10,3,10,-3,-2,-10,10,6,4,-9,6,10,4,-8,-4,6,-5,-4,-5,-1,7,-3,-5,-8,7,-7,-3,-9,-2,-1,-9,2,6,-8,-4,-9,-10,-8,9,5,-3,-1,1,3,-10,-10,1,-2,8,9,-8,-3,-9,5,-6,6,-5,8,-8,1,-3,-6,3,-1,-7,-4,-9,5,-7,5,-3,5,-9,-5,-1,-6,9,1,1,4,-4,-5,5,-2,2,-8,-10,4,5,8,-8,-4,-8,9,-9,-9,3,-10,4,3,-9,1,-3,9,-6,7,1,1,6,-1,6,2,2,8,-1,-3,1,10,-9,-5,3,-9,1,4,-1,-4,4,4,7,-3,-4,-1,-10,-2,-9,4,-7,8,4,-5,8,-1,7,-8,9,5,10,10,-8,-9,-9,10,-7,-4,-2,-5,10,3,-1,-4,-4,8,4,2,-10,8,5,3,-8,-2,-8,1,2,7,-4,-6,9,-10,1,4,4,-1,4,10,3,-2,-8,-10,6,-4,8,9,-5,2,-3,-9,10,6,6,-6,8,3,-3,-8,2,-9,3,10,9,6,-8,-8,7,-4,10,5,10,-5,10,-1,-7,-3,-2,-10,4,-10,-3,3,-2,4,-7,-1,-6,1,2,-8,-6,-9,3,7,9,10,-6,3,-9,2,-5,-4,-1,-5,-9,-2,-6,-1,-4,8,6,5,-2,3,-3,-7,10,-9,6,-6,9,-10,-10,-3,9,-6,-9,8,9,-3,6,3,3,7,-8,-6,10,1,7,4,5,-3,-5,8,-2,-6,-2,4,-1,-9,-5,-5,1,7,-9,-5,3,3,-9,-1,3,-9,8,-4,-6,7,8,-6,-9,-8,-4,-5,1,6,-10,-10,6,-1,5,-3,-6,2,-4,2,9,-2,-5,1,-6,5,-6,8,-6,-4,4,-2,10,6,-10,9,-10,-4,9,-10,-4,10,2,10,9,-9,-3,-5,2,-1,2,4,3,7,-7,7,-4,1,-7,3,7,8,10,-7,5,-7,-7,8,-10,4,-4,1,9,3,3,3,6,3,7,10,-9,-8,9,8,3,-9,2,2,-1,9,-10,5,-6,-6,10,6,3,6,1,3,6,8,1,-9,-6,-6,1,-6,2,9,-8,-3,-8,-4,5,-3,-7,-6,5,-9,-4,-9,6,1,7,-2,-4,5,4,-2,-5,9,-8,-2,-10,3,-6,8,-10,-2,8,10,-8,5,6,-2,-2,5,-8,2,8,4], dtype = "uint8")#candidate|8101|(864,)|const|uint8
call_8100 = relay.TupleGetItem(func_6175_call(relay.reshape(const_8101.astype('uint8'), [864,])), 2)
call_8102 = relay.TupleGetItem(func_6177_call(relay.reshape(const_8101.astype('uint8'), [864,])), 2)
func_3379_call = mod.get_global_var('func_3379')
func_3380_call = mutated_mod.get_global_var('func_3380')
call_8104 = relay.TupleGetItem(func_3379_call(), 0)
call_8105 = relay.TupleGetItem(func_3380_call(), 0)
func_2968_call = mod.get_global_var('func_2968')
func_2970_call = mutated_mod.get_global_var('func_2970')
call_8109 = func_2968_call()
call_8110 = func_2968_call()
func_112_call = mod.get_global_var('func_112')
func_115_call = mutated_mod.get_global_var('func_115')
call_8122 = relay.TupleGetItem(func_112_call(relay.reshape(call_8086.astype('int16'), [16, 13, 6]), relay.reshape(call_8086.astype('int16'), [16, 13, 6]), ), 0)
call_8123 = relay.TupleGetItem(func_115_call(relay.reshape(call_8086.astype('int16'), [16, 13, 6]), relay.reshape(call_8086.astype('int16'), [16, 13, 6]), ), 0)
output = relay.Tuple([call_8086,call_8100,const_8101,call_8104,call_8109,call_8122,])
output2 = relay.Tuple([call_8087,call_8102,const_8101,call_8105,call_8110,call_8123,])
func_8125 = relay.Function([], output)
mod['func_8125'] = func_8125
mod = relay.transform.InferType()(mod)
mutated_mod['func_8125'] = func_8125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8125_call = mutated_mod.get_global_var('func_8125')
call_8126 = func_8125_call()
output = call_8126
func_8127 = relay.Function([], output)
mutated_mod['func_8127'] = func_8127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5211_call = mod.get_global_var('func_5211')
func_5212_call = mutated_mod.get_global_var('func_5212')
call_8145 = func_5211_call()
call_8146 = func_5211_call()
output = call_8145
output2 = call_8146
func_8153 = relay.Function([], output)
mod['func_8153'] = func_8153
mod = relay.transform.InferType()(mod)
mutated_mod['func_8153'] = func_8153
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8153_call = mutated_mod.get_global_var('func_8153')
call_8154 = func_8153_call()
output = call_8154
func_8155 = relay.Function([], output)
mutated_mod['func_8155'] = func_8155
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8182 = relay.var("var_8182", dtype = "float32", shape = ())#candidate|8182|()|var|float32
var_8183 = relay.var("var_8183", dtype = "float32", shape = (2, 1, 8))#candidate|8183|(2, 1, 8)|var|float32
bop_8184 = relay.floor_divide(var_8182.astype('float32'), var_8183.astype('float32')) # shape=(2, 1, 8)
func_4344_call = mod.get_global_var('func_4344')
func_4345_call = mutated_mod.get_global_var('func_4345')
call_8197 = relay.TupleGetItem(func_4344_call(), 2)
call_8198 = relay.TupleGetItem(func_4345_call(), 2)
func_1526_call = mod.get_global_var('func_1526')
func_1527_call = mutated_mod.get_global_var('func_1527')
call_8203 = relay.TupleGetItem(func_1526_call(), 0)
call_8204 = relay.TupleGetItem(func_1527_call(), 0)
output = relay.Tuple([bop_8184,call_8197,call_8203,])
output2 = relay.Tuple([bop_8184,call_8198,call_8204,])
func_8207 = relay.Function([var_8182,var_8183,], output)
mod['func_8207'] = func_8207
mod = relay.transform.InferType()(mod)
mutated_mod['func_8207'] = func_8207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8207_call = mutated_mod.get_global_var('func_8207')
var_8209 = relay.var("var_8209", dtype = "float32", shape = ())#candidate|8209|()|var|float32
var_8210 = relay.var("var_8210", dtype = "float32", shape = (2, 1, 8))#candidate|8210|(2, 1, 8)|var|float32
call_8208 = func_8207_call(var_8209,var_8210,)
output = call_8208
func_8211 = relay.Function([var_8209,var_8210,], output)
mutated_mod['func_8211'] = func_8211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2183_call = mod.get_global_var('func_2183')
func_2184_call = mutated_mod.get_global_var('func_2184')
call_8223 = func_2183_call()
call_8224 = func_2183_call()
output = call_8223
output2 = call_8224
func_8228 = relay.Function([], output)
mod['func_8228'] = func_8228
mod = relay.transform.InferType()(mod)
mutated_mod['func_8228'] = func_8228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8228_call = mutated_mod.get_global_var('func_8228')
call_8229 = func_8228_call()
output = call_8229
func_8230 = relay.Function([], output)
mutated_mod['func_8230'] = func_8230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4254_call = mod.get_global_var('func_4254')
func_4255_call = mutated_mod.get_global_var('func_4255')
call_8277 = func_4254_call()
call_8278 = func_4254_call()
output = call_8277
output2 = call_8278
func_8305 = relay.Function([], output)
mod['func_8305'] = func_8305
mod = relay.transform.InferType()(mod)
mutated_mod['func_8305'] = func_8305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8305_call = mutated_mod.get_global_var('func_8305')
call_8306 = func_8305_call()
output = call_8306
func_8307 = relay.Function([], output)
mutated_mod['func_8307'] = func_8307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8125_call = mod.get_global_var('func_8125')
func_8127_call = mutated_mod.get_global_var('func_8127')
call_8445 = relay.TupleGetItem(func_8125_call(), 4)
call_8446 = relay.TupleGetItem(func_8127_call(), 4)
func_7221_call = mod.get_global_var('func_7221')
func_7224_call = mutated_mod.get_global_var('func_7224')
var_8452 = relay.var("var_8452", dtype = "uint8", shape = (14, 64))#candidate|8452|(14, 64)|var|uint8
call_8451 = relay.TupleGetItem(func_7221_call(relay.reshape(var_8452.astype('uint8'), [16, 7, 8]), relay.reshape(var_8452.astype('uint8'), [16, 7, 8]), ), 0)
call_8453 = relay.TupleGetItem(func_7224_call(relay.reshape(var_8452.astype('uint8'), [16, 7, 8]), relay.reshape(var_8452.astype('uint8'), [16, 7, 8]), ), 0)
output = relay.Tuple([call_8445,call_8451,var_8452,])
output2 = relay.Tuple([call_8446,call_8453,var_8452,])
func_8454 = relay.Function([var_8452,], output)
mod['func_8454'] = func_8454
mod = relay.transform.InferType()(mod)
var_8455 = relay.var("var_8455", dtype = "uint8", shape = (14, 64))#candidate|8455|(14, 64)|var|uint8
output = func_8454(var_8455)
func_8456 = relay.Function([var_8455], output)
mutated_mod['func_8456'] = func_8456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6760_call = mod.get_global_var('func_6760')
func_6762_call = mutated_mod.get_global_var('func_6762')
call_8469 = relay.TupleGetItem(func_6760_call(), 0)
call_8470 = relay.TupleGetItem(func_6762_call(), 0)
output = relay.Tuple([call_8469,])
output2 = relay.Tuple([call_8470,])
func_8482 = relay.Function([], output)
mod['func_8482'] = func_8482
mod = relay.transform.InferType()(mod)
output = func_8482()
func_8483 = relay.Function([], output)
mutated_mod['func_8483'] = func_8483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3163_call = mod.get_global_var('func_3163')
func_3164_call = mutated_mod.get_global_var('func_3164')
call_8523 = func_3163_call()
call_8524 = func_3163_call()
output = call_8523
output2 = call_8524
func_8527 = relay.Function([], output)
mod['func_8527'] = func_8527
mod = relay.transform.InferType()(mod)
mutated_mod['func_8527'] = func_8527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8527_call = mutated_mod.get_global_var('func_8527')
call_8528 = func_8527_call()
output = call_8528
func_8529 = relay.Function([], output)
mutated_mod['func_8529'] = func_8529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1493_call = mod.get_global_var('func_1493')
func_1495_call = mutated_mod.get_global_var('func_1495')
call_8541 = relay.TupleGetItem(func_1493_call(), 0)
call_8542 = relay.TupleGetItem(func_1495_call(), 0)
func_5253_call = mod.get_global_var('func_5253')
func_5254_call = mutated_mod.get_global_var('func_5254')
call_8569 = relay.TupleGetItem(func_5253_call(), 0)
call_8570 = relay.TupleGetItem(func_5254_call(), 0)
output = relay.Tuple([call_8541,call_8569,])
output2 = relay.Tuple([call_8542,call_8570,])
func_8571 = relay.Function([], output)
mod['func_8571'] = func_8571
mod = relay.transform.InferType()(mod)
mutated_mod['func_8571'] = func_8571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8571_call = mutated_mod.get_global_var('func_8571')
call_8572 = func_8571_call()
output = call_8572
func_8573 = relay.Function([], output)
mutated_mod['func_8573'] = func_8573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5118_call = mod.get_global_var('func_5118')
func_5119_call = mutated_mod.get_global_var('func_5119')
call_8593 = relay.TupleGetItem(func_5118_call(), 1)
call_8594 = relay.TupleGetItem(func_5119_call(), 1)
func_6656_call = mod.get_global_var('func_6656')
func_6657_call = mutated_mod.get_global_var('func_6657')
call_8599 = relay.TupleGetItem(func_6656_call(), 0)
call_8600 = relay.TupleGetItem(func_6657_call(), 0)
func_2183_call = mod.get_global_var('func_2183')
func_2184_call = mutated_mod.get_global_var('func_2184')
call_8603 = func_2183_call()
call_8604 = func_2183_call()
func_5500_call = mod.get_global_var('func_5500')
func_5502_call = mutated_mod.get_global_var('func_5502')
call_8607 = relay.TupleGetItem(func_5500_call(), 1)
call_8608 = relay.TupleGetItem(func_5502_call(), 1)
var_8609 = relay.var("var_8609", dtype = "uint8", shape = (16, 13, 6))#candidate|8609|(16, 13, 6)|var|uint8
bop_8610 = relay.logical_or(call_8603.astype('bool'), relay.reshape(var_8609.astype('bool'), relay.shape_of(call_8603))) # shape=(16, 13, 6)
bop_8613 = relay.logical_or(call_8604.astype('bool'), relay.reshape(var_8609.astype('bool'), relay.shape_of(call_8604))) # shape=(16, 13, 6)
output = relay.Tuple([call_8593,call_8599,call_8607,bop_8610,])
output2 = relay.Tuple([call_8594,call_8600,call_8608,bop_8613,])
func_8619 = relay.Function([var_8609,], output)
mod['func_8619'] = func_8619
mod = relay.transform.InferType()(mod)
mutated_mod['func_8619'] = func_8619
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8620 = relay.var("var_8620", dtype = "uint8", shape = (16, 13, 6))#candidate|8620|(16, 13, 6)|var|uint8
func_8619_call = mutated_mod.get_global_var('func_8619')
call_8621 = func_8619_call(var_8620)
output = call_8621
func_8622 = relay.Function([var_8620], output)
mutated_mod['func_8622'] = func_8622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2573_call = mod.get_global_var('func_2573')
func_2574_call = mutated_mod.get_global_var('func_2574')
call_8624 = relay.TupleGetItem(func_2573_call(), 1)
call_8625 = relay.TupleGetItem(func_2574_call(), 1)
const_8637 = relay.const([[[5.581566,9.449731,-9.595779],[-3.041384,-3.349267,-5.533362],[-0.462925,3.222625,-2.336221],[1.079001,1.536164,-5.153818],[-8.232426,8.686142,-7.888378],[-9.000964,4.143415,-0.551701],[4.714449,4.896071,4.536714],[-3.599804,2.735860,1.550187],[-1.353735,4.748487,0.352731],[-1.064828,-4.157488,9.676789],[-9.749201,-1.473538,3.717381]],[[2.058178,6.910585,-5.752793],[-7.801864,-5.571149,8.571858],[0.397747,3.925873,0.320089],[0.241039,-8.837112,2.170564],[-2.721238,-3.466122,9.749536],[6.324970,-2.819927,-3.787737],[9.609353,-8.742772,-9.817441],[2.051434,0.803184,-5.728275],[3.696864,-1.461245,7.251728],[-4.893210,-2.242382,-9.029578],[-7.700932,-1.978026,-7.276885]],[[-4.548144,-5.797444,-3.966329],[-6.024836,-8.746993,-6.829360],[-2.314111,-0.766941,4.854078],[-4.459480,4.726668,-8.205480],[9.745379,-5.623122,-3.929441],[-6.223709,-1.618056,3.052251],[9.914816,6.911279,9.964158],[7.184275,8.509468,-3.268690],[3.816375,-2.593496,8.023756],[0.662602,-7.693761,4.711447],[-0.974895,6.033528,-8.052032]],[[5.330139,-6.785789,7.719506],[-0.800541,5.549928,3.764002],[9.553536,-9.152743,6.503191],[-7.706461,-5.015841,-5.245986],[1.271386,9.176797,-4.124147],[2.050064,-5.964821,-0.604707],[5.731326,-4.885012,-6.947601],[9.820832,-4.785611,-7.910001],[6.439028,-7.339124,4.695283],[6.524015,-9.049911,7.311103],[-2.430641,-3.806877,-2.596137]],[[8.445809,-3.553227,-8.817167],[8.319719,-9.011066,0.791015],[4.483896,7.467295,2.451965],[5.953764,-0.675145,5.999571],[-0.247486,-5.343333,-5.821955],[9.558638,7.057329,2.778072],[-9.066647,0.147374,8.384164],[8.952166,2.509121,-8.687360],[2.869572,-1.657369,0.949436],[1.122654,3.192854,2.767622],[-4.643700,8.794053,-2.100691]],[[0.103994,1.991913,3.674251],[-0.561767,-7.044736,3.118822],[-1.646808,-9.875638,-7.346966],[-2.147593,7.482273,-4.809795],[-2.451229,5.062552,-8.003740],[-0.773561,-3.402034,-0.384675],[-8.111576,5.302931,-1.191924],[-9.326831,2.420757,8.522459],[-1.033799,-7.739618,-2.122246],[-9.869019,2.926987,-2.407057],[6.602568,-8.304741,9.356387]],[[3.256459,2.200476,-2.693170],[-4.613442,-3.457968,6.946099],[1.841267,0.397981,9.577025],[-3.121353,-8.340413,2.593583],[6.091699,-5.389199,-7.000982],[-0.106307,2.606517,-2.579194],[-0.248385,-9.430075,9.774707],[-7.417357,-6.714565,-9.910204],[6.165046,8.242838,-0.527876],[8.811026,-0.967472,4.231510],[1.543849,-1.506330,8.692140]],[[-0.097195,5.295460,-4.327639],[-2.957237,-7.083760,6.848789],[-1.895086,1.966663,-7.894680],[-4.842026,-8.643220,2.301110],[3.688967,2.202259,-2.099423],[8.902579,-1.785456,2.698710],[6.467467,-9.603581,-6.689216],[-4.284992,-5.494656,2.958511],[7.434818,-6.203025,-0.172759],[-8.169787,-6.897991,5.200413],[-6.134172,2.655637,-8.366252]],[[-9.749770,-3.126216,1.732190],[-6.931691,1.190116,7.613637],[9.908624,-0.128401,-8.108791],[-3.277215,3.041943,7.477468],[4.826636,9.598268,-7.716821],[6.936299,6.181289,0.800482],[2.386543,-0.131954,5.138752],[2.091935,-2.768353,-4.248719],[-1.468901,6.998790,-5.846589],[-3.519400,6.390363,-6.512799],[1.216356,-4.396787,-7.347358]]], dtype = "float64")#candidate|8637|(9, 11, 3)|const|float64
bop_8638 = relay.mod(call_8624.astype('float32'), const_8637.astype('float32')) # shape=(9, 11, 3)
bop_8641 = relay.mod(call_8625.astype('float32'), const_8637.astype('float32')) # shape=(9, 11, 3)
func_1940_call = mod.get_global_var('func_1940')
func_1944_call = mutated_mod.get_global_var('func_1944')
const_8647 = relay.const([4.267966,5.927075,1.863241,-8.578824,-7.752656,-1.264050,-1.545100,-2.018167,-0.906591,4.197675,-5.342061,3.330370,-3.400272,-5.799168,-8.581771,-5.157423,2.131519,5.974945,-3.085398,2.505137,-8.492922,0.399119,6.830187,-6.581208,5.436824,6.068655,1.602164,1.921340,-1.310492,2.666284,-2.904317,9.950167,1.559871,7.056143,-4.766237,-4.152694,-3.183293,8.065304,2.103733,5.940817,-1.484136,5.429394,4.548224,3.357168,-9.530487,-7.264306,-5.930637,-1.667916,-2.467062,-1.720565,4.620945,0.482744,-1.541140,2.378313,-4.119168,-8.841498,-8.366414,7.402797,5.533963,5.896656,2.311137,-1.110664,3.721692,-1.722466,-6.093204,-3.533759,0.746123,-3.193125,9.771389,-8.421478,-6.838374,-3.352864,-4.317406,5.347761,-4.386364,2.360592,-2.238070,3.524820,-7.293838,-8.043985,-1.997227,-4.895068,-4.483046,1.514034,7.525378,-7.128799,0.865594,-4.798035,-8.696791,4.305066,-6.629953,-5.623773,-8.651050,7.444314,2.964050,-5.300207,-3.573965,-2.574889,0.131152,-7.128268,3.064301,-4.679940,5.208845,-9.639631,-3.097646,-1.420513,-9.146839,-1.344686,7.917635,2.323318,1.935026,-7.475010,7.798816,-3.382797,2.519686,4.663059,5.357218,3.469575,-1.767176,-5.177900,6.967659,6.909775,-0.601102,-5.273793,6.486700,-5.806993,9.773572,7.468720,7.107519,3.556782,-1.922995,1.732635,6.457156,6.855275,-0.330571,-7.653370,-0.737646,7.911782,5.357921,-9.586480,-4.827907,5.200335,-5.304559,-2.302057,5.062354,-3.611699,-4.442006,3.572795,-0.092967,0.868674,8.635029,-6.941208,9.750426,-1.820132,9.644476,-5.884071,4.579998,-3.702778,-6.953570,-9.443757], dtype = "float64")#candidate|8647|(160,)|const|float64
var_8648 = relay.var("var_8648", dtype = "float64", shape = (1600,))#candidate|8648|(1600,)|var|float64
call_8646 = relay.TupleGetItem(func_1940_call(relay.reshape(const_8647.astype('float64'), [1, 16, 10]), relay.reshape(var_8648.astype('float64'), [10, 16, 10]), relay.reshape(var_8648.astype('float64'), [10, 16, 10]), ), 1)
call_8649 = relay.TupleGetItem(func_1944_call(relay.reshape(const_8647.astype('float64'), [1, 16, 10]), relay.reshape(var_8648.astype('float64'), [10, 16, 10]), relay.reshape(var_8648.astype('float64'), [10, 16, 10]), ), 1)
uop_8651 = relay.asinh(const_8637.astype('float32')) # shape=(9, 11, 3)
func_4642_call = mod.get_global_var('func_4642')
func_4643_call = mutated_mod.get_global_var('func_4643')
call_8657 = relay.TupleGetItem(func_4642_call(), 0)
call_8658 = relay.TupleGetItem(func_4643_call(), 0)
output = relay.Tuple([bop_8638,call_8646,const_8647,var_8648,uop_8651,call_8657,])
output2 = relay.Tuple([bop_8641,call_8649,const_8647,var_8648,uop_8651,call_8658,])
func_8662 = relay.Function([var_8648,], output)
mod['func_8662'] = func_8662
mod = relay.transform.InferType()(mod)
var_8663 = relay.var("var_8663", dtype = "float64", shape = (1600,))#candidate|8663|(1600,)|var|float64
output = func_8662(var_8663)
func_8664 = relay.Function([var_8663], output)
mutated_mod['func_8664'] = func_8664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6410_call = mod.get_global_var('func_6410')
func_6411_call = mutated_mod.get_global_var('func_6411')
call_8679 = func_6410_call()
call_8680 = func_6410_call()
func_2265_call = mod.get_global_var('func_2265')
func_2267_call = mutated_mod.get_global_var('func_2267')
call_8695 = relay.TupleGetItem(func_2265_call(), 3)
call_8696 = relay.TupleGetItem(func_2267_call(), 3)
output = relay.Tuple([call_8679,call_8695,])
output2 = relay.Tuple([call_8680,call_8696,])
func_8704 = relay.Function([], output)
mod['func_8704'] = func_8704
mod = relay.transform.InferType()(mod)
output = func_8704()
func_8705 = relay.Function([], output)
mutated_mod['func_8705'] = func_8705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7244_call = mod.get_global_var('func_7244')
func_7245_call = mutated_mod.get_global_var('func_7245')
call_8706 = relay.TupleGetItem(func_7244_call(), 0)
call_8707 = relay.TupleGetItem(func_7245_call(), 0)
output = call_8706
output2 = call_8707
func_8708 = relay.Function([], output)
mod['func_8708'] = func_8708
mod = relay.transform.InferType()(mod)
mutated_mod['func_8708'] = func_8708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8708_call = mutated_mod.get_global_var('func_8708')
call_8709 = func_8708_call()
output = call_8709
func_8710 = relay.Function([], output)
mutated_mod['func_8710'] = func_8710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4438_call = mod.get_global_var('func_4438')
func_4440_call = mutated_mod.get_global_var('func_4440')
call_8722 = relay.TupleGetItem(func_4438_call(), 0)
call_8723 = relay.TupleGetItem(func_4440_call(), 0)
output = relay.Tuple([call_8722,])
output2 = relay.Tuple([call_8723,])
func_8754 = relay.Function([], output)
mod['func_8754'] = func_8754
mod = relay.transform.InferType()(mod)
mutated_mod['func_8754'] = func_8754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8754_call = mutated_mod.get_global_var('func_8754')
call_8755 = func_8754_call()
output = call_8755
func_8756 = relay.Function([], output)
mutated_mod['func_8756'] = func_8756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5442_call = mod.get_global_var('func_5442')
func_5444_call = mutated_mod.get_global_var('func_5444')
call_8807 = relay.TupleGetItem(func_5442_call(), 0)
call_8808 = relay.TupleGetItem(func_5444_call(), 0)
func_1209_call = mod.get_global_var('func_1209')
func_1211_call = mutated_mod.get_global_var('func_1211')
call_8813 = relay.TupleGetItem(func_1209_call(), 0)
call_8814 = relay.TupleGetItem(func_1211_call(), 0)
func_5933_call = mod.get_global_var('func_5933')
func_5936_call = mutated_mod.get_global_var('func_5936')
var_8820 = relay.var("var_8820", dtype = "float32", shape = (208, 1))#candidate|8820|(208, 1)|var|float32
call_8819 = relay.TupleGetItem(func_5933_call(relay.reshape(var_8820.astype('float32'), [208,])), 0)
call_8821 = relay.TupleGetItem(func_5936_call(relay.reshape(var_8820.astype('float32'), [208,])), 0)
output = relay.Tuple([call_8807,call_8813,call_8819,var_8820,])
output2 = relay.Tuple([call_8808,call_8814,call_8821,var_8820,])
func_8835 = relay.Function([var_8820,], output)
mod['func_8835'] = func_8835
mod = relay.transform.InferType()(mod)
var_8836 = relay.var("var_8836", dtype = "float32", shape = (208, 1))#candidate|8836|(208, 1)|var|float32
output = func_8835(var_8836)
func_8837 = relay.Function([var_8836], output)
mutated_mod['func_8837'] = func_8837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1326_call = mod.get_global_var('func_1326')
func_1328_call = mutated_mod.get_global_var('func_1328')
call_8846 = relay.TupleGetItem(func_1326_call(), 0)
call_8847 = relay.TupleGetItem(func_1328_call(), 0)
output = call_8846
output2 = call_8847
func_8856 = relay.Function([], output)
mod['func_8856'] = func_8856
mod = relay.transform.InferType()(mod)
mutated_mod['func_8856'] = func_8856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8856_call = mutated_mod.get_global_var('func_8856')
call_8857 = func_8856_call()
output = call_8857
func_8858 = relay.Function([], output)
mutated_mod['func_8858'] = func_8858
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8913 = relay.var("var_8913", dtype = "float64", shape = (7, 13, 7))#candidate|8913|(7, 13, 7)|var|float64
uop_8914 = relay.sigmoid(var_8913.astype('float64')) # shape=(7, 13, 7)
output = relay.Tuple([uop_8914,])
output2 = relay.Tuple([uop_8914,])
func_8923 = relay.Function([var_8913,], output)
mod['func_8923'] = func_8923
mod = relay.transform.InferType()(mod)
mutated_mod['func_8923'] = func_8923
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8924 = relay.var("var_8924", dtype = "float64", shape = (7, 13, 7))#candidate|8924|(7, 13, 7)|var|float64
func_8923_call = mutated_mod.get_global_var('func_8923')
call_8925 = func_8923_call(var_8924)
output = call_8925
func_8926 = relay.Function([var_8924], output)
mutated_mod['func_8926'] = func_8926
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8962 = relay.var("var_8962", dtype = "float64", shape = (13, 14, 4))#candidate|8962|(13, 14, 4)|var|float64
uop_8963 = relay.acos(var_8962.astype('float64')) # shape=(13, 14, 4)
func_4254_call = mod.get_global_var('func_4254')
func_4255_call = mutated_mod.get_global_var('func_4255')
call_8974 = func_4254_call()
call_8975 = func_4254_call()
output = relay.Tuple([uop_8963,call_8974,])
output2 = relay.Tuple([uop_8963,call_8975,])
func_8976 = relay.Function([var_8962,], output)
mod['func_8976'] = func_8976
mod = relay.transform.InferType()(mod)
mutated_mod['func_8976'] = func_8976
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8977 = relay.var("var_8977", dtype = "float64", shape = (13, 14, 4))#candidate|8977|(13, 14, 4)|var|float64
func_8976_call = mutated_mod.get_global_var('func_8976')
call_8978 = func_8976_call(var_8977)
output = call_8978
func_8979 = relay.Function([var_8977], output)
mutated_mod['func_8979'] = func_8979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2573_call = mod.get_global_var('func_2573')
func_2574_call = mutated_mod.get_global_var('func_2574')
call_9000 = relay.TupleGetItem(func_2573_call(), 1)
call_9001 = relay.TupleGetItem(func_2574_call(), 1)
var_9015 = relay.var("var_9015", dtype = "float64", shape = (4, 11, 3))#candidate|9015|(4, 11, 3)|var|float64
bop_9016 = relay.logical_or(call_9000.astype('bool'), var_9015.astype('bool')) # shape=(4, 11, 3)
bop_9019 = relay.logical_or(call_9001.astype('bool'), var_9015.astype('bool')) # shape=(4, 11, 3)
output = relay.Tuple([bop_9016,])
output2 = relay.Tuple([bop_9019,])
func_9021 = relay.Function([var_9015,], output)
mod['func_9021'] = func_9021
mod = relay.transform.InferType()(mod)
mutated_mod['func_9021'] = func_9021
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9022 = relay.var("var_9022", dtype = "float64", shape = (4, 11, 3))#candidate|9022|(4, 11, 3)|var|float64
func_9021_call = mutated_mod.get_global_var('func_9021')
call_9023 = func_9021_call(var_9022)
output = call_9023
func_9024 = relay.Function([var_9022], output)
mutated_mod['func_9024'] = func_9024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3163_call = mod.get_global_var('func_3163')
func_3164_call = mutated_mod.get_global_var('func_3164')
call_9044 = func_3163_call()
call_9045 = func_3163_call()
func_8153_call = mod.get_global_var('func_8153')
func_8155_call = mutated_mod.get_global_var('func_8155')
call_9052 = func_8153_call()
call_9053 = func_8153_call()
func_60_call = mod.get_global_var('func_60')
func_64_call = mutated_mod.get_global_var('func_64')
const_9069 = relay.const([2,3,-6,-4,-3,3,-5,-7,-1,-7,8,3,-3,-4,-5,10,9,-7,-2,-3,7,6,-3,3,10,1,3,7,-5,8,-8,-9,2,1,-9,8,-10,-8,-1,-5,4,-1,9,3,-9,-8,-9,-5,3,4,-2,-9,-9,3,1,-3,3,-10,-1,10,3,-8,-5,3,3,-3,10,-7,-1,10,-8,5,-4,8,9,5,8,-4,10,-2,-7,-8,-8,-7,-5,1,8,7,-10,-7,-6,10,-10,6,6,-3,-4,-9,5,-1,10,6,-7,-10,-9,-7,3,-9,-4,3,5,-2,-8,-3,-4,3,-6,4,1,2,2,7,9,-8,-10,-2,8,6,-4,1,3,3,-5,5,-10,-8,-6,-10,10,7,-1,-5,-6,7,9,-9,-1,2,-1,4,1,6,6,4,3,3,2,-3,10,8,7,10,2,-8,6,-6,1,-6,-9,-2,-4,8,-5,-4,-2,-4,2,1,-3,-10,-10,-8,10,9,-6,6,7,6,9,-7,-6,4,-5,5,3,-9,-2,5,10,-3,-4,-6,5,3,6,4,2,-2,-2,-5,10,9,10,4,-7,-8,-8,-2,-10,6,6,8,8,5,6,-7,5,-8,10,-6,-1,-8,1,-1,-6,7,-8,1,6,6,-7,8,-8,8,-8,-5,-7,9,4,8,-8,-3,1,-10,2,-7,-8,-3,-1,4,-3,10,3,-9,9,10,-4,4,9,-2,-2,9,6,-6,-3,8,-1,-8,-8,-5,6,-6,8,-8,6,5,-3,-9,8,-5,10,-5,-2,5,-1,6,-6,10,2,1,9,9,-2,-10,6,1,9,-6,10,8,4,9,-6,-3,6,-8,2,5,-8,6,10,-1,-3,9,-10,3,1,-3,-10,7,2,8,-5,-10,10,8,-3,-1,5,10,-9,7,-4,6,9,-7,-1,5,-2,8,2,3,4,-2,4,-4,4,2,4,-1,3,3,4,9,-4,-7,-2,2,4,7,-5,-2,4,8,-4,-10,8,9,3,10,-5,-6,7,7,5,1,6,-10,7,-10,-6,8,-6,-7,-4,-8,6,-8,-3,6,10,7,-3,6,-6,3,-7,-7,-5,-1,3,-10,3,-4,4,6,9,9,2,-4,-4,-10,7,5,4,-2,7,-6,1,-9,-9,-8,10,-4,5,-1,-6,-1,8,4,-1,-1,-8,9,6,-2,-4,-7,8,-7,9,1,8,-8,-7,10,-7,-6,-5,-4,-6,-8,-9,-5,6,1,9,-3,-5,3,1,9,2,5,-2,-10,9,9,5,-6,-7,8,-2,-2,2,-8,7,-3,5,-8,-8,7,8,-5,1,6,2,-5,7,-1,1,1,9,6,-1,10,5,-7,3,-6,7,6,7,4,-7,2,4,-5,-7,-6,-9,10,-6,-7,-10,5,6,-7,-1,9,-5,7,8,4,-6,6,9,-9,10,5,-8,9,2,-9,6,4,-10,-3,-4,4,9,5,-3,-4,8,-6,10,10,-9,8,4,-9,2,5,-8,3,-10,-7,3,-7,-1,-7,8,4,4,-5,3,-5,5,-8,-10,10,1,2,-9,5,3,2,9,1,7,2,-9,4,8,8,-4,7,-6,-1,1,6,10,-7,3,2,3,9,-2,7,6,9,4,9,-6,-6,10,3,7,1,-6,-9,9,-3,2,3,7,-9,-8,10,9,-3,5,9,5,-1,2,-10,-9,-4,-4,8,6,2,-4,-2,-8,1,2,-7,-1,8,10,6,2,10,-4,-7,6,6,2,4,-4,5,-7,3,-5,-3,8,4,-7,7,-5,-4,4,10,10,9,-10,-2,-9,7,7,-8,-9,-6,-9,8,7,-4,1,-8,7,-7,-2,-4,-5,6,2,6,8,-8,6,2,7,4,-9,1,2,3,-6,-6,9,-2,7,10,1,-6,-5,10,-4,2,-9,-9,2,4,8,-8,5,8,7,9,8,-6,-6,5,-1,5,-1,-10,6,-2,7,3,-9,3,-3,-5,-10,3,7,7,-6,-1,-7,-1,-6,-9,-10,-4,5,6,-10,8,2,-7,1,1,8,-6,3,-2,-10,-2,5,-1,3,-10,-8,6,-2,-3,9,-10,-3,4,4,7,-6,4,6,4,3,-4,-2,5,3,7,-9,9,-5,-10,-10,3,-5,-9,-6,-10,-7,-2,-3,5,2,-8,-10,4,3,-4,-10,-10,8,6,4,-3,-8,-2,-3,-9,-10,7,-5,3,5,-2,6,10,1,8,-9,8,7,10,-8,6,-7,8,-3,1,-10,-3,-7,2,6,-3,2,-4,-3,10,5,-9,-8,6,8,9], dtype = "uint8")#candidate|9069|(864,)|const|uint8
call_9068 = relay.TupleGetItem(func_60_call(relay.reshape(const_9069.astype('uint8'), [6, 9, 16]), relay.reshape(const_9069.astype('uint8'), [6, 9, 16]), ), 0)
call_9070 = relay.TupleGetItem(func_64_call(relay.reshape(const_9069.astype('uint8'), [6, 9, 16]), relay.reshape(const_9069.astype('uint8'), [6, 9, 16]), ), 0)
output = relay.Tuple([call_9044,call_9052,call_9068,const_9069,])
output2 = relay.Tuple([call_9045,call_9053,call_9070,const_9069,])
func_9078 = relay.Function([], output)
mod['func_9078'] = func_9078
mod = relay.transform.InferType()(mod)
mutated_mod['func_9078'] = func_9078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9078_call = mutated_mod.get_global_var('func_9078')
call_9079 = func_9078_call()
output = call_9079
func_9080 = relay.Function([], output)
mutated_mod['func_9080'] = func_9080
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9086 = relay.var("var_9086", dtype = "bool", shape = (4, 3, 11))#candidate|9086|(4, 3, 11)|var|bool
var_9087 = relay.var("var_9087", dtype = "bool", shape = (4, 3, 11))#candidate|9087|(4, 3, 11)|var|bool
bop_9088 = relay.logical_and(var_9086.astype('bool'), relay.reshape(var_9087.astype('bool'), relay.shape_of(var_9086))) # shape=(4, 3, 11)
output = bop_9088
output2 = bop_9088
func_9103 = relay.Function([var_9086,var_9087,], output)
mod['func_9103'] = func_9103
mod = relay.transform.InferType()(mod)
var_9104 = relay.var("var_9104", dtype = "bool", shape = (4, 3, 11))#candidate|9104|(4, 3, 11)|var|bool
var_9105 = relay.var("var_9105", dtype = "bool", shape = (4, 3, 11))#candidate|9105|(4, 3, 11)|var|bool
output = func_9103(var_9104,var_9105,)
func_9106 = relay.Function([var_9104,var_9105,], output)
mutated_mod['func_9106'] = func_9106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1411_call = mod.get_global_var('func_1411')
func_1413_call = mutated_mod.get_global_var('func_1413')
call_9121 = func_1411_call()
call_9122 = func_1411_call()
func_7971_call = mod.get_global_var('func_7971')
func_7973_call = mutated_mod.get_global_var('func_7973')
var_9126 = relay.var("var_9126", dtype = "float32", shape = (132,))#candidate|9126|(132,)|var|float32
call_9125 = relay.TupleGetItem(func_7971_call(relay.reshape(var_9126.astype('float32'), [12, 11, 1])), 0)
call_9127 = relay.TupleGetItem(func_7973_call(relay.reshape(var_9126.astype('float32'), [12, 11, 1])), 0)
func_6175_call = mod.get_global_var('func_6175')
func_6177_call = mutated_mod.get_global_var('func_6177')
const_9129 = relay.const([-8,1,8,-10,3,-1,-10,-3,-1,-2,8,-8,-6,7,5,-7,-9,-7,-4,9,8,6,7,8,-2,8,2,8,6,-7,7,8,-2,-4,-3,6,5,9,1,1,-8,3,6,7,7,4,7,2,8,8,9,3,3,-7,1,-8,-8,8,-2,-5,-10,3,-3,-9,-10,-10,-8,-4,-5,7,-10,5,-6,1,10,5,7,9,4,10,-4,3,-3,3,10,4,-5,-10,-1,-8,-9,3,2,7,-2,8,-7,-6,-9,-8,10,-1,-10,5,1,4,-6,-7,1,-4,1,8,6,10,-4,-4,-10,-9,-5,-2,10,6,5,6,-9,10,4,-2,2,6,10,-2,7,1,-8,6,-2,-5,8,-4,2,9,-4,8,2,-5,6,-3,9,-2,-10,6,-5,-9,-2,1,1,-2,10,-2,-4,5,4,-2,3,-9,-6,-4,-6,3,-8,-2,4,-3,-5,-7,3,10,9,10,8,4,4,3,1,-8,10,-7,5,1,6,-1,-9,6,-5,-1,-6,6,-2,-4,7,-1,3,1,7,-9,9,2,1,7,6,8,2,-6,5,7,-9,8,6,9,3,-8,8,-2,10,6,7,8,9,4,-3,5,9,3,5,1,-1,-2,-9,-9,-6,-6,10,2,7,3,-7,1,4,-1,9,-8,-9,9,-7,-10,3,5,10,-3,3,9,4,6,-6,-8,-9,5,-7,7,-5,6,-2,1,8,9,2,1,-7,-6,6,-10,-8,-2,-9,8,7,-2,-3,-1,1,-2,9,8,2,1,-6,2,3,-1,-2,-6,3,10,-5,8,-10,-6,6,4,-8,8,5,-9,2,3,-9,7,-9,1,-5,-9,-9,-5,-8,7,-4,-1,-2,9,10,-2,-1,4,-3,3,4,-6,-6,10,-9,-2,-1,-4,-3,9,-5,6,-9,5,3,-3,-1,-2,7,2,10,-3,-7,5,9,5,6,-9,2,-8,-1,4,7,8,-7,-2,-4,-7,1,3,6,6,-1,-7,-9,10,6,-4,1,9,-2,-4,-7,9,2,9,-4,-10,-10,-10,3,-10,5,2,-4,3,-3,4,9,-7,9,-9,-1,-8,7,1,-9,9,-3,-1,3,6,-2,-7,6,-1,1,8,10,-4,-5,7,6,-9,10,-7,-5,-10,-5,-9,2,-6,10,5,-1,9,2,9,3,-6,-1,7,-7,-4,-3,-3,-2,7,4,-4,-9,-10,-8,-10,8,-3,10,-4,6,-1,-8,-5,7,2,2,-6,-6,1,-5,4,-6,10,-8,4,2,-4,-4,-1,-1,-2,-1,-3,3,1,-6,1,6,9,-8,8,2,10,-3,5,-8,-4,-5,5,2,8,-3,-9,2,2,2,-10,6,-10,-3,-10,2,-7,2,5,-8,-9,1,1,-7,-3,-7,-5,5,9,-10,8,-4,1,8,7,10,-8,-5,6,4,-2,4,-1,5,-6,10,9,2,-9,5,-6,-3,5,5,-1,-3,-9,2,-6,1,-2,-10,6,-10,-10,-4,-9,5,6,-7,9,4,7,-8,-5,-6,2,7,-6,7,-1,6,-8,3,-1,3,-10,-7,-4,-1,6,5,5,-7,8,-1,-5,-6,8,-8,-10,8,-9,1,2,10,1,-7,7,7,10,-2,-5,-7,-10,1,-8,-1,7,-8,-4,-6,-4,-1,-9,-6,-6,-3,9,-3,6,10,-6,9,-5,-2,-7,-3,-3,4,3,-10,-10,-10,-2,-9,-9,-2,-2,-6,-10,-5,9,8,4,-4,1,8,5,-4,2,-7,4,6,2,4,-2,-9,-9,-3,-8,-2,8,-2,-9,-4,-2,2,2,-2,1,4,-5,4,-9,-8,1,8,1,6,8,1,-1,-4,2,-5,3,6,-4,3,7,-10,5,-10,10,8,-6,-6,3,-9,-7,6,6,8,-4,5,4,10,3,-6,7,-1,-3,1,-6,-1,-5,-2,10,-2,3,-4,3,6,7,1,8,-7,8,6,-8,-6,3,5,10,-8,5,1,7,5,1,-7,7,-7,4,6,10,7,4,7,-9,8,-6,-1,-4,8,-2,4,9,-4,-7,-6,-4,10,-3,3,-1,-6,-8,1,-5,9,4,-9,-7,7,-3,10,-4,-7,-9,-8,1,-9,-5,3,1,-9,7,9,9,7,7,-1,-8,-7,-1,7,-3,1,1,7,-9,-7,2,-10,10,-5,3,-9,6,-9,-4,-9,5,2,7,7,6,2,-2,1,10,-10,-1,5,6,4,-2,-5,-4,-2,8,7,-7,-2,-1,-10,8,-5,10,8,-6,6,-7,5,-1,4,-8,5,-10,-2,-9], dtype = "uint8")#candidate|9129|(864,)|const|uint8
call_9128 = relay.TupleGetItem(func_6175_call(relay.reshape(const_9129.astype('uint8'), [864,])), 1)
call_9130 = relay.TupleGetItem(func_6177_call(relay.reshape(const_9129.astype('uint8'), [864,])), 1)
output = relay.Tuple([call_9121,call_9125,var_9126,call_9128,const_9129,])
output2 = relay.Tuple([call_9122,call_9127,var_9126,call_9130,const_9129,])
func_9131 = relay.Function([var_9126,], output)
mod['func_9131'] = func_9131
mod = relay.transform.InferType()(mod)
var_9132 = relay.var("var_9132", dtype = "float32", shape = (132,))#candidate|9132|(132,)|var|float32
output = func_9131(var_9132)
func_9133 = relay.Function([var_9132], output)
mutated_mod['func_9133'] = func_9133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7244_call = mod.get_global_var('func_7244')
func_7245_call = mutated_mod.get_global_var('func_7245')
call_9135 = relay.TupleGetItem(func_7244_call(), 0)
call_9136 = relay.TupleGetItem(func_7245_call(), 0)
var_9156 = relay.var("var_9156", dtype = "float64", shape = (3, 11, 3))#candidate|9156|(3, 11, 3)|var|float64
bop_9157 = relay.bitwise_and(call_9135.astype('int16'), var_9156.astype('int16')) # shape=(3, 11, 3)
bop_9160 = relay.bitwise_and(call_9136.astype('int16'), var_9156.astype('int16')) # shape=(3, 11, 3)
func_2220_call = mod.get_global_var('func_2220')
func_2222_call = mutated_mod.get_global_var('func_2222')
call_9164 = relay.TupleGetItem(func_2220_call(), 0)
call_9165 = relay.TupleGetItem(func_2222_call(), 0)
func_6798_call = mod.get_global_var('func_6798')
func_6800_call = mutated_mod.get_global_var('func_6800')
var_9174 = relay.var("var_9174", dtype = "float64", shape = (7, 99))#candidate|9174|(7, 99)|var|float64
call_9173 = relay.TupleGetItem(func_6798_call(relay.reshape(var_9174.astype('float64'), [7, 11, 9])), 0)
call_9175 = relay.TupleGetItem(func_6800_call(relay.reshape(var_9174.astype('float64'), [7, 11, 9])), 0)
uop_9178 = relay.log2(call_9173.astype('float32')) # shape=(7, 11, 9)
uop_9180 = relay.log2(call_9175.astype('float32')) # shape=(7, 11, 9)
func_6574_call = mod.get_global_var('func_6574')
func_6576_call = mutated_mod.get_global_var('func_6576')
call_9196 = relay.TupleGetItem(func_6574_call(), 0)
call_9197 = relay.TupleGetItem(func_6576_call(), 0)
func_5500_call = mod.get_global_var('func_5500')
func_5502_call = mutated_mod.get_global_var('func_5502')
call_9215 = relay.TupleGetItem(func_5500_call(), 1)
call_9216 = relay.TupleGetItem(func_5502_call(), 1)
func_8125_call = mod.get_global_var('func_8125')
func_8127_call = mutated_mod.get_global_var('func_8127')
call_9226 = relay.TupleGetItem(func_8125_call(), 4)
call_9227 = relay.TupleGetItem(func_8127_call(), 4)
uop_9230 = relay.acos(uop_9178.astype('float64')) # shape=(7, 11, 9)
uop_9232 = relay.acos(uop_9180.astype('float64')) # shape=(7, 11, 9)
output = relay.Tuple([bop_9157,call_9164,var_9174,call_9196,call_9215,call_9226,uop_9230,])
output2 = relay.Tuple([bop_9160,call_9165,var_9174,call_9197,call_9216,call_9227,uop_9232,])
func_9236 = relay.Function([var_9156,var_9174,], output)
mod['func_9236'] = func_9236
mod = relay.transform.InferType()(mod)
var_9237 = relay.var("var_9237", dtype = "float64", shape = (3, 11, 3))#candidate|9237|(3, 11, 3)|var|float64
var_9238 = relay.var("var_9238", dtype = "float64", shape = (7, 99))#candidate|9238|(7, 99)|var|float64
output = func_9236(var_9237,var_9238,)
func_9239 = relay.Function([var_9237,var_9238,], output)
mutated_mod['func_9239'] = func_9239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2476_call = mod.get_global_var('func_2476')
func_2478_call = mutated_mod.get_global_var('func_2478')
call_9324 = func_2476_call()
call_9325 = func_2476_call()
func_4861_call = mod.get_global_var('func_4861')
func_4863_call = mutated_mod.get_global_var('func_4863')
call_9329 = relay.TupleGetItem(func_4861_call(), 1)
call_9330 = relay.TupleGetItem(func_4863_call(), 1)
output = relay.Tuple([call_9324,call_9329,])
output2 = relay.Tuple([call_9325,call_9330,])
func_9331 = relay.Function([], output)
mod['func_9331'] = func_9331
mod = relay.transform.InferType()(mod)
mutated_mod['func_9331'] = func_9331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9331_call = mutated_mod.get_global_var('func_9331')
call_9332 = func_9331_call()
output = call_9332
func_9333 = relay.Function([], output)
mutated_mod['func_9333'] = func_9333
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9349 = relay.const([[[9.388917,4.139482,8.127585,-7.140075,-8.600357,-4.632129,-5.288811,-8.606900,-2.733576,3.087453,-5.783837,2.435492,-7.839994,-5.603545,8.313316],[-7.537563,-4.792551,-6.273624,5.673112,-6.221331,-8.049654,-6.255872,-5.250670,-2.390899,-6.137813,-1.776601,-3.968327,-4.048716,9.533522,-8.017899],[-1.027761,3.713337,-4.559451,0.606058,-5.138098,7.198157,-6.232586,0.252915,1.846134,4.006973,-7.071643,-2.214060,2.617549,6.527097,6.253734],[-8.860801,3.159341,5.203435,7.703225,1.396855,-0.842554,9.768427,-3.405050,7.445912,-9.358755,4.671067,5.953547,4.745338,-2.029986,1.477052],[-6.646044,-7.838958,-6.060374,-4.020593,-1.915630,1.863186,-9.256528,4.993056,-5.401291,-5.872193,-7.625327,8.487705,-0.183131,-5.385897,1.817313],[-4.094655,2.616308,5.691839,-3.454901,-4.777699,2.084633,-7.708917,-3.196612,6.560196,-0.677339,4.516864,8.230992,-2.626015,-9.940377,4.093356],[1.234576,8.646018,-4.939249,-2.659283,-3.994436,6.865335,-0.938918,-1.037245,5.148694,7.818595,8.241731,-5.098561,6.553005,-7.436651,-2.504945],[-4.892635,-8.106263,-9.193888,-6.812970,1.716462,5.208579,8.631583,-6.563735,-7.063465,6.877223,-8.066283,1.833318,5.710827,4.777897,-8.595811],[1.357664,7.090844,-6.067253,-4.378778,-4.699271,-6.667821,-6.056064,-6.790317,4.352102,7.567881,-9.547741,7.807683,-0.671354,2.810185,3.454182],[9.118788,-3.379500,-8.435870,6.576675,2.739559,-7.420374,5.713419,2.764391,-9.044687,2.314220,3.809762,2.891902,6.563739,-5.171495,9.565464],[-8.363873,-2.053329,-5.360721,0.718711,-5.283117,6.264137,-2.548070,0.678568,-6.801875,-7.923697,6.336770,-1.260245,5.056983,0.144349,-7.281837],[3.489957,3.318395,7.886974,-5.567385,8.932597,5.245671,8.232447,-2.097628,-1.805626,-7.107601,-1.473427,-4.239467,-8.137513,-1.948684,8.659068],[6.332869,1.890156,5.564769,-8.489916,4.772888,-0.896945,-4.338821,1.921277,-2.544181,-2.274588,-2.113028,3.174021,1.271009,-4.797621,2.565741],[-0.589056,-3.407834,1.343716,-4.478635,2.982534,-4.936376,-2.314505,-9.227581,7.973495,3.852619,1.805588,-3.693903,2.852801,1.892317,7.985588]],[[5.289528,5.480655,1.414380,2.234822,-5.845769,6.346412,-0.374051,1.835728,5.051507,-7.583394,-0.381995,7.921832,-7.908351,-2.593476,-6.867725],[-9.171188,7.908202,-8.377688,-3.929692,-1.383335,-0.184952,6.817440,-3.524281,9.337815,5.344439,-3.303090,-2.206673,-7.608057,-1.664156,-8.536216],[-1.306131,9.489980,-7.044996,-3.644645,4.839975,1.694701,7.722185,4.804148,8.696949,1.523011,-3.344898,8.729645,6.428055,2.410236,-8.536310],[8.301807,-0.064102,9.457391,-8.306349,0.438345,-7.774238,7.939218,-6.370511,8.678015,-9.551732,-0.145509,2.567078,9.272678,-7.581393,-0.567214],[-8.100286,9.131813,-5.393920,5.001372,1.257084,9.529146,8.444621,6.542996,7.658857,7.802201,8.562367,-2.848917,2.344046,-9.139733,-1.181000],[8.126040,-7.190591,2.473972,0.583312,0.393646,0.751197,-3.584052,7.002899,-0.418009,1.966662,-9.393819,-4.764402,9.541761,-1.672905,5.355421],[-4.030421,1.260530,9.936537,-9.478392,8.490619,1.390665,-8.718288,2.199608,3.883045,-9.413681,-1.482367,-5.294175,7.594992,-3.798628,8.936263],[-9.127163,-7.445670,-3.955991,-2.754289,-8.579215,-9.864842,-1.553377,-2.203245,-8.641240,-1.042173,-7.817987,-7.119817,1.426025,-8.578684,3.050848],[8.114664,7.202767,-6.547184,1.301082,-0.349070,-4.344111,-6.880599,5.272681,9.966783,-4.356028,-1.540715,-8.665620,0.237832,-2.111781,8.649566],[5.963359,3.608360,0.026927,-8.747033,-7.868640,-7.523322,4.009051,-3.640666,4.538779,6.589928,2.728963,-3.657454,-0.641189,2.451295,7.524224],[-1.852822,6.656760,-3.981171,2.052328,8.393881,6.727466,3.372395,-0.422740,-8.097470,0.802830,-0.801053,3.191822,-8.668645,-0.689175,8.060031],[-4.146887,6.051580,6.288286,-2.076693,-1.057742,9.255934,-8.531290,1.496436,-0.887996,-0.852042,5.010214,-2.272081,-2.449197,-3.280014,-9.371406],[-3.502742,1.394533,-4.711352,8.488018,-3.219182,-2.854291,-1.154813,-4.185505,-3.254836,8.040956,-8.868703,0.770194,5.475390,6.830504,-7.394316],[2.521381,-9.620189,-9.106817,-9.706401,-6.669753,-2.186958,-5.727499,2.347605,-1.889824,8.735322,-3.587798,-6.871463,-0.954786,7.431417,8.614637]],[[6.482698,3.264060,6.965389,-4.997084,4.566080,-4.617327,8.081123,-8.913408,8.121472,-1.035013,-6.417956,-2.510104,-7.611405,6.262763,-5.452972],[-1.688305,2.376319,-5.093053,1.693904,-8.896647,1.805414,-1.045184,0.043723,0.808933,3.069229,6.670679,-1.660314,-2.942751,-3.380004,9.644592],[-6.958140,-2.674722,9.704356,1.301426,3.724350,1.631720,-7.392997,-3.020716,8.066964,0.349902,1.654390,-8.494911,-6.717665,2.430160,-4.642730],[-2.856625,-0.404500,1.147000,8.544229,-8.867255,-3.917701,1.459773,-0.308060,8.135723,7.692820,-3.226024,0.444329,-8.790766,-8.266933,1.110296],[-8.579548,8.874218,-7.973706,-3.697832,7.285260,4.117969,9.102025,3.852620,-0.348113,0.337764,3.995252,-2.549536,-4.989125,-0.079779,-3.630346],[-2.677328,7.360505,3.836133,-7.771102,9.609609,8.602775,6.028136,2.032463,-6.756460,5.712733,4.073330,8.703924,-5.391758,4.346686,-9.505530],[-6.613872,-7.821025,4.807457,7.331257,-0.962513,5.235161,4.226734,-4.325996,1.883676,-6.374114,-7.445924,6.776982,-2.056795,9.617215,3.972039],[6.393964,-7.969147,6.670712,-9.364154,8.835872,-5.012728,-6.929173,-2.980353,-5.871149,8.980045,-5.602624,4.715741,5.974928,7.780038,8.371088],[7.894991,-5.424986,-0.080763,9.204137,0.093066,6.690436,9.035696,8.104587,-7.089025,-7.247244,3.769608,8.467920,-4.715033,-0.036733,-6.942573],[-1.543329,-1.466985,8.025404,1.192213,2.866074,-6.183069,-9.228025,-4.825499,2.346235,0.023246,-7.759178,-6.943233,5.636683,5.543613,4.528594],[0.867539,1.477859,-5.681476,0.295511,9.992052,-5.760959,8.097175,9.898054,0.839402,4.145425,-7.390915,7.189913,7.055326,-5.880549,-1.282853],[-0.254841,1.440042,6.635227,0.706593,4.874649,-4.940447,-2.159888,-1.870679,9.156235,-2.026819,8.629931,4.457419,0.492916,6.991487,4.882790],[1.820910,-3.604340,2.700379,6.650926,-8.241693,4.450390,-4.727517,-3.475085,0.686280,-5.838084,-3.096204,5.362698,-3.347491,0.297451,-5.149907],[2.695817,-0.853401,-8.147507,-3.957471,-8.175995,4.389697,9.584018,5.322656,-0.768871,7.530308,-9.145097,-2.558400,8.235762,2.295245,3.910800]],[[8.807867,8.098509,-3.431614,8.619193,4.219180,7.386704,0.011401,1.112376,-6.865423,-2.726752,-9.306306,-1.614701,-7.265888,-6.171987,-8.605878],[8.561141,-4.784566,8.544079,-2.265348,6.557022,5.337401,-4.566292,2.300285,3.520463,-1.441777,-6.296638,4.275795,6.345897,-3.046073,8.634225],[9.819636,3.855831,5.659282,-5.829054,1.057189,-3.556733,-7.771568,-7.961368,-4.108780,-6.757137,1.239118,5.298024,4.000658,-8.020863,-5.602250],[-6.181709,-8.243673,-0.214391,-0.680105,5.098822,-0.607988,-2.435172,3.384421,9.844677,8.456970,-2.845940,-5.940831,4.902694,-8.614189,3.301726],[9.752552,7.996758,3.086217,0.232675,-3.071910,-5.291838,-4.154849,-2.236384,9.948367,2.624995,9.879542,2.771421,-1.481437,6.917180,-9.909846],[9.944265,-3.968928,1.663061,-0.639936,0.915333,3.465890,-5.732032,5.637318,4.731521,-9.378072,0.737357,-3.532979,1.281685,7.965524,-6.590462],[6.208425,3.392192,-1.450038,-4.382589,2.659615,4.269065,4.733342,6.134637,-1.429244,1.564056,8.727068,-4.824512,3.569038,-6.035728,-1.422117],[-5.427982,3.373900,0.573722,-9.538590,-8.266513,-2.115248,-5.798166,2.798360,-3.633467,0.166094,-6.906891,-5.945561,-1.266801,-2.584432,-5.219600],[7.618763,4.570315,-8.084147,-6.774949,-4.399031,-2.012651,3.346660,-8.256460,-1.722242,-8.852505,-4.343161,8.866782,-8.997152,-5.873467,-1.493861],[2.145277,5.474666,-6.643485,-6.766630,-3.626541,-9.945488,3.934255,7.539786,-8.211978,-8.817936,6.630166,-6.573241,3.950838,1.519811,4.577508],[-5.791848,8.546900,0.217314,2.256683,5.185495,-7.754451,-3.987853,3.465970,5.111975,-4.421890,-7.267251,-3.382608,-6.044520,5.383892,4.246413],[1.326973,-9.597169,9.577737,2.931185,3.868001,-1.161856,-5.280653,0.945863,8.571465,2.959467,-2.779805,1.772918,-7.336759,-3.171431,8.711389],[1.958301,3.421191,-0.455246,4.044119,2.950313,-9.518676,0.390130,-0.742903,-4.814469,7.377635,2.846408,5.648424,3.883496,-0.959441,-6.938352],[1.285938,5.886088,9.075196,-9.277855,1.173444,4.548611,6.903229,-3.668512,4.916896,9.213986,-0.924353,-6.494870,-4.072940,-7.787573,5.324658]],[[-7.447816,-0.526127,1.871856,2.947918,-2.356623,9.456441,-2.255695,-8.936232,-9.672519,8.637965,8.744378,0.019701,-5.399590,4.865439,-2.761114],[6.071676,7.220585,-5.304550,7.820618,-9.881755,-2.712523,9.482963,0.167851,4.147323,7.213762,9.456417,2.283082,-6.848289,-7.362019,-4.911756],[-5.667179,-4.089530,7.486239,-0.687409,-9.785270,-1.759745,-3.150928,-5.505319,-0.013656,7.657025,-0.325484,-2.221190,2.511155,1.267927,-0.014106],[0.282168,3.824783,-9.066298,-8.557819,2.651011,-1.634338,-9.343521,6.578976,-7.688092,-1.496616,4.931842,-2.171574,-2.178742,-6.973022,-1.411196],[7.008803,7.477368,4.401646,7.176126,-6.244368,-2.745409,2.874453,2.117987,9.610334,-9.024982,-7.373758,2.772041,4.373365,-5.318085,3.729730],[-2.140041,-9.269567,-3.918277,2.513916,-8.824308,-5.299650,-7.586757,6.406421,7.066210,7.941577,-7.799206,5.921929,5.348284,-1.311981,2.914973],[-0.606363,-6.304697,9.113948,-0.163760,2.418691,9.425191,2.124926,7.699450,9.642552,-4.445983,-5.045466,-2.454831,-8.484669,-5.931928,-0.605239],[-1.783094,8.365892,0.055359,0.817462,9.447441,-9.185614,7.240102,8.548552,-5.785120,5.345742,2.127741,-4.841842,1.149529,1.164449,7.915436],[3.772434,-4.174292,-6.004310,-2.867839,5.448655,-9.429260,-6.390524,-5.414292,-4.558555,-9.287906,4.097053,6.792553,-5.023668,-5.635836,-0.762075],[7.079780,1.941034,-5.026426,0.692655,-5.601372,4.106051,3.297176,-4.825162,2.818549,-1.512572,-7.422616,3.129340,4.996524,-7.501639,-0.356500],[7.566323,9.306793,8.485562,6.146837,-2.622147,-9.728521,-1.876161,8.096290,1.254776,-8.519765,-1.241114,0.882571,-8.056585,4.369451,-1.302833],[-9.642282,3.922787,-4.032638,7.167461,-5.157389,1.405561,2.007899,-4.347128,-7.440918,2.027438,0.836591,0.424431,-2.881205,-2.990441,0.759504],[0.346621,-8.467991,0.788563,3.042727,-5.847158,-4.702057,-1.381448,-3.287486,-2.622419,-0.588438,5.091019,4.444874,-9.384091,-4.438324,-0.717206],[7.692263,1.427753,-0.811177,4.859406,-9.070095,1.601246,5.259979,-3.883107,-0.404117,4.834232,5.164984,4.263220,4.162767,-0.583994,-1.968684]]], dtype = "float64")#candidate|9349|(5, 14, 15)|const|float64
uop_9350 = relay.log10(const_9349.astype('float64')) # shape=(5, 14, 15)
func_1712_call = mod.get_global_var('func_1712')
func_1715_call = mutated_mod.get_global_var('func_1715')
const_9356 = relay.const([-1,-10,-8,-6,9,-9,8,-2,1,1,-7,2,-8,6,-6,-5,1,-1,10,4,-3,-10,10,-3,5,-9,-2,-10,6,8,1,8,-9,-1,-8,8,-7,-4,2,10,-3,10,9,-6,8,-6,7,8,-7,-7,-3,6,-5,7,-10,-3,-7,8,4,3,-8,-8,-5,3,7,-6,-4,10,-3,-5,5,5,4,8,-7,-10,9,10,-6,5,2,4,4,-5,3,1,1,-8,7,-3,-6,-9,-2,-9,3,-4,7,-1,3,9,8,-2,6,-2,-7,-9,-7,-9,7,-7,-4,-5,10,4,-2,7,-5,-8,10,-3,-6,-1,-1,2,-8,10,2,7,-1,-3,-5,4,-9,2,2,-6,8,-1,-8,8,-4,10,-4,-9,-9,8,5,6,4,-5,3,-5,1,-3,9,-4,10,10,-2,-8,1,5,-8,10,-8,8,-6,-4,9,5,9,-4,5,2,2,8,-6,1,-3,5,6,5,-6,-1,8,-6,7,-7,-3,2,9,-1,3,8,-5,-9,8,-4,-3,-9,1,10,-5,-2,6,-6,-4,-9,-10,-4,3,3,7,4,-2,-5,-10,3,-1,-4,9,-1,6,1,-10,1,10,3,-3,9,1,8,-8,7,-6,-4,10,7,7,3,2,-9,8,-8,-8,-6,-3,-8,-5,-8,-5,-5,8,-2,7,2,-7,-10,2,6,8,-7,-4,10,2,-2,10,4,9,-5,-9,-6,10,1,-5,-10,-7,-2,3,-4,-1,2,4,-3,9,-9,-7,-7,10,-6,7,10,4,8,-5,4,9,-9,-1,-7,-10,-1,1,3,7,10,7,7,1,3,-8,-2,-3,9,3,4,-4,10,2,9,-3,3,-9,5,6,6,5,10,-8,9,6,-5,-10,-6,-8,-4,-5,3,9,-2,8,-10,5,-10,-10,-6,-4,-9,-8,9,-3,9,1,-10,1,-7,1,1,-7,2,-10,6,-1,-8,-1,5,9,-1,-5,1,6,-7,5,-4,-7,-2,5,10,-4,-3,7,-10,-3,9,4,5,9,-7,-8,-9,-9,3,-10,10,-5,-10,2,-1,2,2,-9,8,-9,-4,-7,-3,3,-10,2,8,2,10,-9,8,8,-9,-7,6,-3,-2,-5,-7,-2,3,7,-1,-1,-3,-9,-4,-9,7,2,-1,-6,-5,7,-9,-9,2,4,-2,-2,7,-6,-2,6,2,-3,-2,3,9,-9,8,1,-3,1,1,-2,9,-9,-4,10,-2,-6,-1,-2,-10,9,1,6,-4,-1,2,-3,-3,10,7,3,5,4,10,-8,-10,-8,6,5,3,-7,1,-4,2,2,-5,9,-4,-6,2,7,-1,-1,1,1,3,-8,7,7,-9,-1,1,4,4,2,-6,-7,5,5,5,-1,1,-1,3,-10,-6,-7,-10,4,3,-1,8,5,8,-1,-4,-3,2,-7,-3,-7,9,-8,5,4,-2,6,-5,-3,-10,7,-7,-1,4,5,-7,4,4,-5,-6,8,6,-5,-4,-3,5,10,-8,-4,-1,8,9,3,6,6,-9,-9,8,-5,4,-9,-5,4,10,-6,5,10,-7,-1,5,4,-2,10,-7,-4,-10,-2,2,8,4,-4,7,-4,8,-7,3,-6,4,-6,-8,4,3,-5,-3,-6,9,5,3,2,5,4,-3,-6,8,-10,2,6,-3,10,-6,-3,6,4,-9,1,-8,-5,-9,9,-1,-4,2,-8,-3,-3,5,-7,-5,-10,-7,-2,8,-7,-8,-2,5,4,8,-4,-10,-1,4,6,8,6,7,-2,5,3,8,-2,3,-2,-8,1,3,5,-9,7,-6,-3,-2,9,-4,1,-8,-7,-9,-10,-5,-4,-5,8,-9,9,9,-8,7,-8,-10,5,2,-8,8,7,-1,4,10,-9,-8,-2,-10,-7,8,10,-6,5,-6,8,-1,9,-6,7,4,2,-4,-8,5,-1,-3,-2,-5,-9,-9,7,2,3,9,-3,-8,5,-1,8,10,-10,2,4,-8,10,-9,-9,-1,10,-4,4,-8,-6,4,7,-5,7,-9,-5,-5,6,2,-5,-8,4,8,6,9,-6,-5,-4,-10,-8,-3,5,9,-2,-9,-5,-3,-10,9,8,-7,-8,7,-3,-5,5,-5,8,4,-7,10,-1,-3,4,7,7,-8,6,-8,-4,1,5,-2,2,-6,2,-2,-6,3,4,-6,2,7,1,1,2,-7,-10,1,-8,2,10,-10,-9,-10,3,-6,-10,-4,-2,-8,-7,-1,-5,-10,9,2,7,10,7,9,-4,4,9,6,-5,6,-3,-10,1,-3,3,2,1,6,-9,-7,-1,8,-1,3,-3,9,-8,-4,8,-9,-5,10,2,4,-10,-6,-4,-3,3,2,-7,-1,9,-1,-5,5,-3,7,-1,-7,-2,4,-9,10,2,-9,-2,-3,-8,-7,7,6,-6,-5,4,8,7,3,-8,10,-4,1,1,-8,-2,-3,-6,9,2,1,-6,-3,10,8,6,1,9,9,-8,9,1,-9,1,-8,-1,-8,-7,-9,6,8,7,3,1,-4,-8,-9,6,-5,-5,9,-2,-3,9,-10,1,-6,-5,-4,10,5,2,-8,-1,5,-6,2,-3,-8,10,7,4,-2,2,-7,-6,2,-6,8,3,-3,-8,-6,-1,5,-4,3,-6,9,10,2,-8,-4,7,10,-5,-9,-8,-8,-1,2,-5,-5,1,1,-10,7,-7,10,5,6,-5,-5,-1,-5,5,-8,-4,3,7,-7,5,4,-7,8,6,-3,8,-5,-10,1,-6,8,-4,-5,3,7,-6,-1,-7,4,-4,4,5,-3,8,2,5,-5,-9,1,10,1,10,10,3,-1,-3,3,2,4,-1,5,-4,-6,-9,-6,-6,-7,-9,6,-3,2,-9,3,-10,3,-3,7,7,2,-2,-6,-5,7,-2,-9,9,10,-8,-1,-9,-10,-1,10,4,-3,-10,7,2,3,-8,-8,4,6,10,-10,10,-1,-1,-8,-5,-3,9,-2,5,-4,8,1,7,-5,5,-8,-9,5,-2,-7,3,3,10,-3,-3,-2,-9,6,-2,-3,-8,1,1,-7,8,-9,-4,3,10,-2,2,-5,-7,-7,1,6,-4,-5,1,-6,-8,10,-9,-7,-10,3,3,5,8,10,5,-9,3,1,-7,-4,4,-6,-8,6,-4,-2,-7,-6,10,-4,-4,-1,6,2,9,-8,-2,9,-9,-10,2,-9,-10,5,5,-2,-2,-5,-4,-4,4,9,-8,8,3,-2,1,-5,-10,-8,10,1,4,2,6,-3,10,8,10,9,5,8,5,-4,4,10,-5,-9,1,-7,9,-7,3,9,1,-7,-1,2,-10,3,-10,9,-5,4,-2,-3,2,10,-5,-9,8,5,-2,-9,5,6,4,1,-6,7,6,6,10,-5,8,-3,1,8,-7,6,9,-9,9,-4,5,-2,-1,-2,8,-6,-3,-3,-9,10,7,9,-9,-1,-8,-3,6,7,6,8,7,10,-5,4,5,-1,9,-10,-10,-7,8,5,-9,-3,10,-9,-5,6,-2,-3,2,1,6,2,-4,6,10,6,-4,4,-10,2,4,5,-6,-4,4,4,7,-8,4,3,-7,-3,9,6,2,7,6,1,4,-4,1,10,3,-10,-4,-1,3,-4,3,6,-10,1,-8,-9,8], dtype = "uint8")#candidate|9356|(1365,)|const|uint8
call_9355 = relay.TupleGetItem(func_1712_call(relay.reshape(const_9356.astype('uint8'), [1365,])), 3)
call_9357 = relay.TupleGetItem(func_1715_call(relay.reshape(const_9356.astype('uint8'), [1365,])), 3)
output = relay.Tuple([uop_9350,call_9355,const_9356,])
output2 = relay.Tuple([uop_9350,call_9357,const_9356,])
func_9367 = relay.Function([], output)
mod['func_9367'] = func_9367
mod = relay.transform.InferType()(mod)
mutated_mod['func_9367'] = func_9367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9367_call = mutated_mod.get_global_var('func_9367')
call_9368 = func_9367_call()
output = call_9368
func_9369 = relay.Function([], output)
mutated_mod['func_9369'] = func_9369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6410_call = mod.get_global_var('func_6410')
func_6411_call = mutated_mod.get_global_var('func_6411')
call_9392 = func_6410_call()
call_9393 = func_6410_call()
output = call_9392
output2 = call_9393
func_9406 = relay.Function([], output)
mod['func_9406'] = func_9406
mod = relay.transform.InferType()(mod)
mutated_mod['func_9406'] = func_9406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9406_call = mutated_mod.get_global_var('func_9406')
call_9407 = func_9406_call()
output = call_9407
func_9408 = relay.Function([], output)
mutated_mod['func_9408'] = func_9408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5783_call = mod.get_global_var('func_5783')
func_5785_call = mutated_mod.get_global_var('func_5785')
call_9450 = func_5783_call()
call_9451 = func_5783_call()
func_2968_call = mod.get_global_var('func_2968')
func_2970_call = mutated_mod.get_global_var('func_2970')
call_9485 = func_2968_call()
call_9486 = func_2968_call()
output = relay.Tuple([call_9450,call_9485,])
output2 = relay.Tuple([call_9451,call_9486,])
func_9490 = relay.Function([], output)
mod['func_9490'] = func_9490
mod = relay.transform.InferType()(mod)
output = func_9490()
func_9491 = relay.Function([], output)
mutated_mod['func_9491'] = func_9491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8704_call = mod.get_global_var('func_8704')
func_8705_call = mutated_mod.get_global_var('func_8705')
call_9494 = relay.TupleGetItem(func_8704_call(), 0)
call_9495 = relay.TupleGetItem(func_8705_call(), 0)
func_7848_call = mod.get_global_var('func_7848')
func_7850_call = mutated_mod.get_global_var('func_7850')
call_9510 = relay.TupleGetItem(func_7848_call(), 1)
call_9511 = relay.TupleGetItem(func_7850_call(), 1)
output = relay.Tuple([call_9494,call_9510,])
output2 = relay.Tuple([call_9495,call_9511,])
func_9515 = relay.Function([], output)
mod['func_9515'] = func_9515
mod = relay.transform.InferType()(mod)
output = func_9515()
func_9516 = relay.Function([], output)
mutated_mod['func_9516'] = func_9516
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9517 = relay.const([[[9.591878,-8.137208,8.218669,-9.026821,2.046226,-1.788201,-0.892048],[-4.929444,-3.522200,-9.712870,0.498215,0.490313,-6.770069,7.337499],[-0.911484,7.289613,6.569673,-6.481559,-1.730090,1.628927,5.280000]],[[9.000685,-8.093267,-6.691124,-8.823496,-3.538354,8.250699,-1.326744],[1.745525,9.787450,-2.513293,8.363790,3.378308,-9.218407,0.179402],[9.010908,3.608170,-0.675449,-0.770288,6.450808,1.950751,-9.975089]]], dtype = "float64")#candidate|9517|(2, 3, 7)|const|float64
uop_9518 = relay.sqrt(const_9517.astype('float64')) # shape=(2, 3, 7)
output = relay.Tuple([uop_9518,])
output2 = relay.Tuple([uop_9518,])
func_9520 = relay.Function([], output)
mod['func_9520'] = func_9520
mod = relay.transform.InferType()(mod)
output = func_9520()
func_9521 = relay.Function([], output)
mutated_mod['func_9521'] = func_9521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3379_call = mod.get_global_var('func_3379')
func_3380_call = mutated_mod.get_global_var('func_3380')
call_9558 = relay.TupleGetItem(func_3379_call(), 0)
call_9559 = relay.TupleGetItem(func_3380_call(), 0)
func_6798_call = mod.get_global_var('func_6798')
func_6800_call = mutated_mod.get_global_var('func_6800')
var_9564 = relay.var("var_9564", dtype = "float64", shape = (693,))#candidate|9564|(693,)|var|float64
call_9563 = relay.TupleGetItem(func_6798_call(relay.reshape(var_9564.astype('float64'), [7, 11, 9])), 0)
call_9565 = relay.TupleGetItem(func_6800_call(relay.reshape(var_9564.astype('float64'), [7, 11, 9])), 0)
func_7342_call = mod.get_global_var('func_7342')
func_7344_call = mutated_mod.get_global_var('func_7344')
call_9569 = relay.TupleGetItem(func_7342_call(), 0)
call_9570 = relay.TupleGetItem(func_7344_call(), 0)
func_6656_call = mod.get_global_var('func_6656')
func_6657_call = mutated_mod.get_global_var('func_6657')
call_9574 = relay.TupleGetItem(func_6656_call(), 0)
call_9575 = relay.TupleGetItem(func_6657_call(), 0)
bop_9576 = relay.logical_xor(call_9574.astype('uint64'), relay.reshape(call_9569.astype('uint64'), relay.shape_of(call_9574))) # shape=(1, 11, 3)
bop_9579 = relay.logical_xor(call_9575.astype('uint64'), relay.reshape(call_9570.astype('uint64'), relay.shape_of(call_9575))) # shape=(1, 11, 3)
output = relay.Tuple([call_9558,call_9563,var_9564,bop_9576,])
output2 = relay.Tuple([call_9559,call_9565,var_9564,bop_9579,])
func_9580 = relay.Function([var_9564,], output)
mod['func_9580'] = func_9580
mod = relay.transform.InferType()(mod)
var_9581 = relay.var("var_9581", dtype = "float64", shape = (693,))#candidate|9581|(693,)|var|float64
output = func_9580(var_9581)
func_9582 = relay.Function([var_9581], output)
mutated_mod['func_9582'] = func_9582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1554_call = mod.get_global_var('func_1554')
func_1555_call = mutated_mod.get_global_var('func_1555')
call_9636 = relay.TupleGetItem(func_1554_call(), 0)
call_9637 = relay.TupleGetItem(func_1555_call(), 0)
var_9653 = relay.var("var_9653", dtype = "float64", shape = (14, 11, 3))#candidate|9653|(14, 11, 3)|var|float64
bop_9654 = relay.add(call_9636.astype('uint64'), var_9653.astype('uint64')) # shape=(14, 11, 3)
bop_9657 = relay.add(call_9637.astype('uint64'), var_9653.astype('uint64')) # shape=(14, 11, 3)
output = relay.Tuple([bop_9654,])
output2 = relay.Tuple([bop_9657,])
func_9659 = relay.Function([var_9653,], output)
mod['func_9659'] = func_9659
mod = relay.transform.InferType()(mod)
var_9660 = relay.var("var_9660", dtype = "float64", shape = (14, 11, 3))#candidate|9660|(14, 11, 3)|var|float64
output = func_9659(var_9660)
func_9661 = relay.Function([var_9660], output)
mutated_mod['func_9661'] = func_9661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3686_call = mod.get_global_var('func_3686')
func_3687_call = mutated_mod.get_global_var('func_3687')
call_9753 = func_3686_call()
call_9754 = func_3686_call()
func_6313_call = mod.get_global_var('func_6313')
func_6316_call = mutated_mod.get_global_var('func_6316')
var_9764 = relay.var("var_9764", dtype = "float64", shape = (462,))#candidate|9764|(462,)|var|float64
call_9763 = relay.TupleGetItem(func_6313_call(relay.reshape(var_9764.astype('float64'), [14, 11, 3])), 5)
call_9765 = relay.TupleGetItem(func_6316_call(relay.reshape(var_9764.astype('float64'), [14, 11, 3])), 5)
func_4500_call = mod.get_global_var('func_4500')
func_4505_call = mutated_mod.get_global_var('func_4505')
const_9768 = relay.const([[-4.095865,-6.034227,-3.744696,8.157553],[4.565209,-6.572614,2.425048,-6.250032],[-2.647779,2.937788,5.532061,-4.604496],[7.793535,8.580619,-1.988781,-5.041869],[6.377659,-2.731982,4.051153,5.978525],[3.402477,7.071532,-1.445477,-2.886448],[-0.689599,6.586182,5.299191,-0.724516],[-4.236186,-1.105122,4.079114,2.908990],[7.371932,-7.350953,1.171548,-1.563073],[0.106824,-3.292478,8.464756,2.792140],[-0.585656,-3.540866,-3.905083,-4.600945],[-3.769449,9.119102,-3.674358,2.869218],[5.156276,-8.572741,3.910693,7.332400],[-1.135545,-9.756645,-6.674211,4.624065],[7.598654,-6.523371,4.086821,-3.343739]], dtype = "float64")#candidate|9768|(15, 4)|const|float64
const_9769 = relay.const([-6,9,-8,-6,1,-10,-6,-5,2,-10,-8,6,8,7,4,-8,-2,2,7,7,-5,7,5,4,-5,2,5,-7,8,8,5,-2,-7,8,-2,10,-5,-1,-8,6,9,9,8,8,9,9,6,-2,6,4,7,7,2,-2,3,4,-6,8,8,-1,6,10,9,-2,3,3,2,4,8,-6,2,6,4,1,2,8,1,-9,-1,-3,8,4,6,8,2,8,4,1,8,10,5,9,6,-4,10,1,5,-8,3,-8,9,-10,-8,1,-6,-7,6,5,-3,-9,10,10,5,-10,-5,-5,4,7,8,-9,6,-5,1,4,-1,-6,-5,8,-6,8,5,-4,-7,-3,9,-9,-8,-7,6,-5,-6,-8,1,9,-2,-9,-8,-8,-3,2,-4,7,7,5,5,10,2,2,-4,1,8,5,-2,-5,-7,-9,9,-5,9,-2,1,-6,2,8,-9,-1,8,4,-2,-5,5,-10,-9,5,-6,-2,10,9,6,-9,-4,-3,-8,-2,-6,-9,-2,-9,3,-9,-2,-3,-9,-8,10,9,8,8,-8,6,9,9,4,2,-4,6,2,-10,-4,5,6,9,5,-9,10,-1,3,-10,-9,-4,-3,-9,-2,5,9,-1,5,8,9,-5,7,8,7,8,-10,9,5,-10,10,4,-7,-6,-4,4,-6,-2,6,-4,8,1,6,-1,9,-9,-9,10,-7,8,-1,-7,-1,9,-1,-2,-4,-6,2,-1,-1,10,5,-5,6,-6,-6,-3,3,6,-6,-2,-1,1,8,-4,4,10,-6,2,8,1,10,-3,-8,7,-7,-4,-9,-4,9,-7,-4,2,2,1,9,-4,-6,6,-5,-9,3,-3,-10,-9,-2,4,5,-5,-8,-9,-8,10,9,9,-8,-6,-4,3,-5,7,-3,5,-4,5,7,-1,-6,-1,6,8,-2,4,5,-2,-2,-10,-9,-2,-5,9,2,7,2,2,-9,3,-9,7,-4,6,9,2,-1,5,1,8,-3,-1,4,-2,-6,-4,1,10,-4,5,4,-3,2,-1,-9,6,3,-6,3,-9,4,5,-9,-5,5,6,5,-4,-5,-10,3,8,-5,4,4,-6,-9,8,-10,-10,-10,2,-6,-4,3,-5,2,-2,-10,5,-10,-4,4,8,4,-8,-4,2,9,1,2,6,-1,-2,-7,-5,-8,7,-3,-7,-2,-1,-5,6,-1,-4,3,8,10,-7,5,-3,2,-8,-6,-4,-9,-5,-10,-8,10,-5,-4,8,-10,-3,6,-1,-8,5,-3,-2,-6,7,-2,8,-9,-4,5,-8,-9,-4,-9,-5,-4,-4,-1,-9,5,-2,3,10,4,-6,8,-6,7,1,-2,6,7,3,6,5,-10,-2,-9,-4,6,2,5,10,5,-1,-10,-5,9,-6,-9,-8,-8,-1,-1,-9,-8,1,-10,-7,-2,4,-7,10,-6,-1,-5,-6,-9,1,-4,9,3,5,-10,-8,5,6,-2,8,-1,7,-9,-1,9,-10,-4,7,8,-1,-8,-3,-5,-3,-5,7,1,4,-8,-8,-8,-2,-9,2,-2,-6,-3,1,7,-5,6,-8,9,-5,-10,-3,-3,-3,-5,10,7,8,-4,-8,-5,-1,6,-8,-3,1,9,-4,-9,5,-1,9,-8,5,-8,-2,7,-5,-5,7,7,-3,-2,-9,3,2,8,9,-2,9,-9,-2,4,-1,-10,7,8,6,-9,10,-2,4,-6,5,1,-8,4,-9,7,7,10,-9,-6,-8,-3,-6,1,-2,-7,6,2,10,-6,-6,1,-4,-9,-9,9,1,4,-6,1,3,-6,6,5,-8,7,3,7,-10,10,5,-7,-1,6,-7,5,5,-8,-3,-8,-3,-5,4,-6,2,4,-5,-6,1,6,-8,-7,-6,5,10,-10,-8,-9,-9,-5,-1,8,9,4,7,7,1,-10,8,6,-7,-1,3,7,5,5,-2,-1,9,10,-7,1,8,-7,-9,4,-9,-2,5,6,-3,5,6,-8,-5,-10,5,10,-5,2,10,-9,-1,3,10,7,10,9,-9,-10,-5,-7,-2,-4,4,2,-1,4,1,9,5,-7,9,-1,-4,5,1,-10,10,1,-9,9,3,-6,-9,8,-3,10,-10,10,-4,-3,-8,-8,-8,-2,2,-9,-5,9,-1,9,-1,-6,4,7,3,-2,3,-7,9,-8,-3,5,-3,1,3,-8,2,7,9,3,2,-1,3,7,-1,2,3,3,4,-10,5,1,-1,1,-10,2,-8,-10,4,5,-4,1,-8,5,-6,7,4,-9,6,-7,-6,10,-3,-9,8,2,2,-1,-6,2,-3,5,9,-6,-6,3,1,8,-4,9,-10,3,-4,4,-3,4,-7,7,3,-1,6,4,7,-9,6,2,1,-2,2,-5,-2,4,7,3,5,-2,-10,-6,6,-6,5,2,5,-3,8,3,6,-9,-9,5,-10,2,-1,5,-6,-4,10,9,8,2,9,-7,-5,9,1,-5,-1,9,7,-1,-6,4,-1,-9,4,-6,-1,1,9,7,4,-3,2,8,7,-2,4,-8,2,3,-1,2,-2,-7,1,-3,7,-1,-9,8,-10,-8,10,-1,-3,10,-3,-7,3,6,-7,10,-6,-3,-2,10,3,8,3,-8,4,-4,10,4,3,-9,10,4,-4,2,10,-8,9,8,5,-10,-6,8,6,-1,-1,-9,4,8,2,4,9,5,-7,-1,3,-3,-6,6,2,-10,2,3,-7,-1,-10,-1,6,8,10,-8,-3,-1,2,2,7,-5,5,4,-1,-1,2,2,7,-1,-1,10,-10,4,8,-3,10,-5,-10,-7,6,3,-9,5,-7,4,7,-2,7,-8,2,2,-1,-6,-6,3,-2,-9,3,10,-10,8,10,-4,-7,-2,4,-2,-10,10,-3,9,1,-8,-10,6,3,-9,3,-8,6,1,3,-6,2,-1,9,2,-8,6,-9,9,-6,2,2,2,-1,9,-6,9,1,5,-1,-3,7,8,2,7,8,9,-1,-7,6,6,-2,-10,-8,4,9,-8,-7,-2,4,6,1,1,8,4,-5,-6,9,10,8,-5,-1,7,1,-4,-1,6,-8,1,8,-2,8,-10,1,-2,-3,-9,-4,-10,-6,-10,9,-8,-5,-4,6,6,3,1,-7,4,4,4,-10,10,1,2,8,-8,10,-7,-8,-10,-10,-7,-6,7,-6,7,-7,3,-9,-9,-6,-1,9,-3,-1,-9,4,8,-9,-1,5,-3,4,-10,5,-9,6,-7,8,-1,-3,-1,-8,-8,-5,-6,-4,5,-6,-3,6,-2,-4,7,-9,2,-1,-10,4,-8,4,9,2,9,1,-1,-6,7,-1,1,-3,3,-7,-4,8,10,-3,-3,-5,5,4,2,8,-7,6,-1,2,4,7,-10,10,-9,3,10,-4,-3,-2,8,6,8,-5,2,3,7,-4,4,-1,8,9,-1,4,3,10,-3,7,10,-10,-9,8,10,-7,7,1,9,5,3,3,-3,-7,9,8,6,-2,1,-3,4,-7,-7,10,10,-5,3,1,10,4,4,9,-10,-6,-10,3,-10,-9,-1,-2,-2,-6,-4,-3,-6,4,-9,-9,5,-9,4,-1,2,-1,8,-6,10,-7,10,9,-5,8,-7,2,-2,-8,-4,-1,10,-1,-5], dtype = "uint8")#candidate|9769|(1365,)|const|uint8
call_9767 = relay.TupleGetItem(func_4500_call(relay.reshape(const_9768.astype('float64'), [10, 2, 3]), relay.reshape(const_9768.astype('float64'), [10, 2, 3]), relay.reshape(const_9769.astype('uint8'), [1365,]), ), 0)
call_9770 = relay.TupleGetItem(func_4505_call(relay.reshape(const_9768.astype('float64'), [10, 2, 3]), relay.reshape(const_9768.astype('float64'), [10, 2, 3]), relay.reshape(const_9769.astype('uint8'), [1365,]), ), 0)
var_9783 = relay.var("var_9783", dtype = "float64", shape = (462,))#candidate|9783|(462,)|var|float64
bop_9784 = relay.greater_equal(var_9764.astype('bool'), relay.reshape(var_9783.astype('bool'), relay.shape_of(var_9764))) # shape=(462,)
output = relay.Tuple([call_9753,call_9763,call_9767,const_9768,const_9769,bop_9784,])
output2 = relay.Tuple([call_9754,call_9765,call_9770,const_9768,const_9769,bop_9784,])
func_9794 = relay.Function([var_9764,var_9783,], output)
mod['func_9794'] = func_9794
mod = relay.transform.InferType()(mod)
var_9795 = relay.var("var_9795", dtype = "float64", shape = (462,))#candidate|9795|(462,)|var|float64
var_9796 = relay.var("var_9796", dtype = "float64", shape = (462,))#candidate|9796|(462,)|var|float64
output = func_9794(var_9795,var_9796,)
func_9797 = relay.Function([var_9795,var_9796,], output)
mutated_mod['func_9797'] = func_9797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3909_call = mod.get_global_var('func_3909')
func_3911_call = mutated_mod.get_global_var('func_3911')
call_9830 = relay.TupleGetItem(func_3909_call(), 0)
call_9831 = relay.TupleGetItem(func_3911_call(), 0)
output = relay.Tuple([call_9830,])
output2 = relay.Tuple([call_9831,])
func_9833 = relay.Function([], output)
mod['func_9833'] = func_9833
mod = relay.transform.InferType()(mod)
output = func_9833()
func_9834 = relay.Function([], output)
mutated_mod['func_9834'] = func_9834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4642_call = mod.get_global_var('func_4642')
func_4643_call = mutated_mod.get_global_var('func_4643')
call_9859 = relay.TupleGetItem(func_4642_call(), 1)
call_9860 = relay.TupleGetItem(func_4643_call(), 1)
func_2586_call = mod.get_global_var('func_2586')
func_2588_call = mutated_mod.get_global_var('func_2588')
call_9861 = func_2586_call()
call_9862 = func_2586_call()
func_8976_call = mod.get_global_var('func_8976')
func_8979_call = mutated_mod.get_global_var('func_8979')
var_9866 = relay.var("var_9866", dtype = "float64", shape = (1, 728))#candidate|9866|(1, 728)|var|float64
call_9865 = relay.TupleGetItem(func_8976_call(relay.reshape(var_9866.astype('float64'), [13, 14, 4])), 0)
call_9867 = relay.TupleGetItem(func_8979_call(relay.reshape(var_9866.astype('float64'), [13, 14, 4])), 0)
output = relay.Tuple([call_9859,call_9861,call_9865,var_9866,])
output2 = relay.Tuple([call_9860,call_9862,call_9867,var_9866,])
func_9883 = relay.Function([var_9866,], output)
mod['func_9883'] = func_9883
mod = relay.transform.InferType()(mod)
var_9884 = relay.var("var_9884", dtype = "float64", shape = (1, 728))#candidate|9884|(1, 728)|var|float64
output = func_9883(var_9884)
func_9885 = relay.Function([var_9884], output)
mutated_mod['func_9885'] = func_9885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5797_call = mod.get_global_var('func_5797')
func_5798_call = mutated_mod.get_global_var('func_5798')
call_9918 = relay.TupleGetItem(func_5797_call(), 0)
call_9919 = relay.TupleGetItem(func_5798_call(), 0)
func_3712_call = mod.get_global_var('func_3712')
func_3715_call = mutated_mod.get_global_var('func_3715')
var_9926 = relay.var("var_9926", dtype = "float64", shape = (175,))#candidate|9926|(175,)|var|float64
call_9925 = relay.TupleGetItem(func_3712_call(relay.reshape(var_9926.astype('float64'), [5, 5, 7])), 0)
call_9927 = relay.TupleGetItem(func_3715_call(relay.reshape(var_9926.astype('float64'), [5, 5, 7])), 0)
func_4790_call = mod.get_global_var('func_4790')
func_4792_call = mutated_mod.get_global_var('func_4792')
call_9928 = relay.TupleGetItem(func_4790_call(), 0)
call_9929 = relay.TupleGetItem(func_4792_call(), 0)
output = relay.Tuple([call_9918,call_9925,var_9926,call_9928,])
output2 = relay.Tuple([call_9919,call_9927,var_9926,call_9929,])
func_9931 = relay.Function([var_9926,], output)
mod['func_9931'] = func_9931
mod = relay.transform.InferType()(mod)
var_9932 = relay.var("var_9932", dtype = "float64", shape = (175,))#candidate|9932|(175,)|var|float64
output = func_9931(var_9932)
func_9933 = relay.Function([var_9932], output)
mutated_mod['func_9933'] = func_9933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5390_call = mod.get_global_var('func_5390')
func_5391_call = mutated_mod.get_global_var('func_5391')
call_9942 = relay.TupleGetItem(func_5390_call(), 0)
call_9943 = relay.TupleGetItem(func_5391_call(), 0)
func_9794_call = mod.get_global_var('func_9794')
func_9797_call = mutated_mod.get_global_var('func_9797')
const_9949 = relay.const([1.908193,-7.591824,-4.239087,-8.436336,4.358559,-7.641889,8.196729,0.718802,-5.969418,-9.014192,6.041841,1.773377,-6.949661,6.724856,-1.736010,5.535798,-9.825944,-0.109311,3.274825,0.439849,-2.747265,-9.721820,-2.086380,7.783187,6.841795,-8.410011,-9.528599,7.994156,-3.471511,7.917401,-8.080670,6.996832,-6.918776,3.222088,-9.768298,-7.403861,3.150107,-7.391966,4.179642,-1.067874,-6.890680,0.126183,-7.145093,7.021807,2.313765,1.746813,-6.572261,-6.045268,2.218347,-4.154797,-7.363780,-8.591353,6.130180,8.436813,8.684483,4.525570,8.783347,-7.238743,7.158502,-0.092885,-4.175355,1.098434,-9.243237,-3.973006,6.488745,8.003406,3.613748,0.675538,9.037859,9.651161,-4.458503,-7.985149,5.578001,-9.327488,-1.234691,5.170756,-5.224340,3.530048,3.568090,-2.608649,-9.133896,-7.281204,-9.041047,-5.396492,9.554272,-8.180323,7.732487,1.372475,1.943738,1.615546,-0.806170,3.206903,0.357001,-1.463562,-6.908603,-5.177010,-7.218964,-9.148167,-0.256256,-7.189546,1.376944,-9.303844,3.203812,6.027637,1.286797,7.520653,-7.270813,-1.726784,5.087145,-5.099468,-7.038717,7.885668,1.263282,3.087067,-9.400610,0.071261,-4.597588,-6.401836,7.137501,-5.184823,0.249903,2.137374,-6.789872,0.114139,-2.264353,9.096815,-6.900669,8.127060,7.366565,-9.296463,2.146243,2.272935,0.532391,4.135750,8.240591,2.239292,9.637543,-8.436473,-7.410921,-2.287767,4.497676,1.973309,-6.163866,-0.423691,0.347446,3.020381,-7.734884,-8.855752,3.736389,9.378904,-8.599265,5.928564,3.736800,3.179598,2.534115,-8.894472,-0.580396,9.067216,-1.409186,-5.267590,-1.562752,-9.281499,-0.893300,-5.180444,3.529497,-9.921641,-3.884228,2.077479,-9.286744,1.678456,-5.583247,-8.451609,-3.167242,8.777107,1.719560,-4.876720,-6.981734,2.625569,-0.474503,-8.348458,0.472924,4.082244,-2.311296,9.743687,7.029358,-6.409584,-0.722225,-6.280651,-9.619622,3.996426,3.405257,8.420957,3.449748,-1.661898,-2.016907,8.977486,-1.633118,7.800526,7.283104,5.875341,-6.603318,8.985825,-8.166462,2.240441,3.359616,6.863693,-8.757239,-3.878429,3.018502,4.815091,9.156586,8.846097,5.355887,-9.071559,5.568765,-3.436362,-6.091554,-6.315542,4.273023,1.058251,-9.082829,-1.185515,-9.254326,-7.440614,6.258910,0.252236,-0.856192,-4.333119,-4.598164,3.002083,-2.321909,1.300534,8.388096,-4.384511,2.402577,3.368269,-5.328792,-6.734645,3.510277,-8.762076,0.338105,7.514876,-7.959228,5.763812,9.284414,-1.403569,-0.128613,-2.634104,6.495030,6.053445,-8.260044,-9.577973,-9.386728,1.662556,-5.254123,-6.491146,-8.004573,4.267900,-6.130080,5.126370,9.707526,4.220573,1.893250,3.062544,-1.695812,6.668170,-9.555573,7.564535,-1.036460,-8.590532,-7.838983,-4.497263,-6.737343,4.500781,6.076164,-7.557668,-0.645909,-8.368093,4.017094,-6.818558,-3.857194,4.282924,-4.286196,2.400667,9.529687,6.255989,7.965201,-2.332930,9.847244,-0.230951,-4.814114,-1.153799,-8.614905,-0.963370,-4.884330,-8.177506,-0.299949,7.850549,-9.834733,-9.661135,-2.230158,-0.217146,9.638504,-5.908657,-2.261507,3.952282,1.195068,-0.543191,0.516884,-4.458951,8.829760,-6.131646,-0.988792,-4.031564,7.716416,-7.674789,-3.888017,9.928916,-6.862045,9.033118,-6.046647,8.949680,-4.537123,2.538057,5.045678,2.343172,-1.875843,-4.799029,-9.751282,-1.312465,0.174019,9.750017,8.108467,-6.316161,-2.927836,-3.075340,-6.889851,5.820189,2.977411,-0.286402,-0.130495,-8.236423,-0.790259,7.034647,1.334864,-5.409656,-8.078490,2.911432,-2.513917,5.408282,2.754981,3.039547,-0.643478,-6.613544,6.543814,-4.329014,-2.166117,0.359422,1.901639,6.966170,-0.814236,-3.546300,-7.865099,-8.196549,1.630524,9.887639,2.166881,-1.794892,9.382993,-9.990807,-7.903853,-9.491477,3.530250,1.486770,-5.852353,1.305057,-9.787811,-7.402306,8.451910,0.796416,-8.280065,4.327729,3.758443,4.969111,-2.339479,5.777543,-7.226315,-3.748165,8.582760,6.251423,-8.317629,-1.148360,-7.841328,9.905054,1.360823,-1.685308,-4.103652,-8.511240,4.978723,-9.703724,0.850902,-2.109476,-9.259951,0.652892,-7.033414,6.666669,0.744578,6.994068,-1.475434,-7.478166,2.032501,-2.294379,-4.792605,5.108697,-3.170510,-7.927858,-8.497307,-1.503824,2.595446,-9.067072,-4.604487,-0.409361,-8.952648,6.590981,1.575708,-7.968531,-0.625398,-9.863811,9.031051,-9.531748,1.103494,3.378182,-2.630779,-4.998360,7.827098,5.888140,8.242935,-9.461312,-9.794687,-3.485815,8.279698,-7.602814,6.058501,-0.893808,0.496797,0.593972,5.853368,-5.886771,-4.890039,6.762902,5.743675,6.581902,2.057980,-0.298336,9.570553,3.925304,-2.006245,-8.612536,-2.359836,-5.048147,6.001075,-6.099650], dtype = "float64")#candidate|9949|(462,)|const|float64
call_9948 = relay.TupleGetItem(func_9794_call(relay.reshape(const_9949.astype('float64'), [462,]), relay.reshape(const_9949.astype('float64'), [462,]), ), 4)
call_9950 = relay.TupleGetItem(func_9797_call(relay.reshape(const_9949.astype('float64'), [462,]), relay.reshape(const_9949.astype('float64'), [462,]), ), 4)
func_8708_call = mod.get_global_var('func_8708')
func_8710_call = mutated_mod.get_global_var('func_8710')
call_9964 = func_8708_call()
call_9965 = func_8708_call()
output = relay.Tuple([call_9942,call_9948,const_9949,call_9964,])
output2 = relay.Tuple([call_9943,call_9950,const_9949,call_9965,])
func_9968 = relay.Function([], output)
mod['func_9968'] = func_9968
mod = relay.transform.InferType()(mod)
output = func_9968()
func_9969 = relay.Function([], output)
mutated_mod['func_9969'] = func_9969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2085_call = mod.get_global_var('func_2085')
func_2087_call = mutated_mod.get_global_var('func_2087')
call_9970 = func_2085_call()
call_9971 = func_2085_call()
output = call_9970
output2 = call_9971
func_9977 = relay.Function([], output)
mod['func_9977'] = func_9977
mod = relay.transform.InferType()(mod)
mutated_mod['func_9977'] = func_9977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9977_call = mutated_mod.get_global_var('func_9977')
call_9978 = func_9977_call()
output = call_9978
func_9979 = relay.Function([], output)
mutated_mod['func_9979'] = func_9979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8482_call = mod.get_global_var('func_8482')
func_8483_call = mutated_mod.get_global_var('func_8483')
call_9985 = relay.TupleGetItem(func_8482_call(), 0)
call_9986 = relay.TupleGetItem(func_8483_call(), 0)
var_10006 = relay.var("var_10006", dtype = "float64", shape = (13, 11, 3))#candidate|10006|(13, 11, 3)|var|float64
bop_10007 = relay.greater_equal(call_9985.astype('bool'), var_10006.astype('bool')) # shape=(13, 11, 3)
bop_10010 = relay.greater_equal(call_9986.astype('bool'), var_10006.astype('bool')) # shape=(13, 11, 3)
func_4619_call = mod.get_global_var('func_4619')
func_4621_call = mutated_mod.get_global_var('func_4621')
call_10022 = func_4619_call()
call_10023 = func_4619_call()
output = relay.Tuple([bop_10007,call_10022,])
output2 = relay.Tuple([bop_10010,call_10023,])
func_10028 = relay.Function([var_10006,], output)
mod['func_10028'] = func_10028
mod = relay.transform.InferType()(mod)
var_10029 = relay.var("var_10029", dtype = "float64", shape = (13, 11, 3))#candidate|10029|(13, 11, 3)|var|float64
output = func_10028(var_10029)
func_10030 = relay.Function([var_10029], output)
mutated_mod['func_10030'] = func_10030
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10051 = relay.var("var_10051", dtype = "int64", shape = (8, 5, 13))#candidate|10051|(8, 5, 13)|var|int64
const_10052 = relay.const([[[2,5,-1,-3,10,5,-4,6,3,-7,7,8,-5],[3,8,7,10,-10,-9,-9,2,10,-10,-5,2,-9],[2,-6,-4,9,1,-3,-6,-3,-5,7,-6,-3,-1],[-1,-10,1,10,1,6,-5,7,-9,-1,9,5,-3],[-1,9,-5,-7,3,-9,7,6,-3,10,8,-3,10]],[[-5,8,-5,-4,-4,-5,6,-9,10,8,-9,8,10],[-7,-5,5,-1,7,3,-10,-10,8,-4,2,4,1],[-10,-3,7,3,8,-3,2,-4,-3,2,1,1,8],[1,-3,7,3,6,-9,-3,7,-5,8,-6,6,-4],[9,-2,1,10,10,-9,-7,-5,4,-3,-4,1,-8]],[[2,-4,-10,-4,-1,10,10,1,2,-6,4,5,-10],[4,2,8,-7,-10,7,-3,-10,-2,-2,-2,8,-3],[8,10,8,1,7,4,6,-4,10,1,-10,-2,5],[9,4,6,4,1,-9,2,4,3,-1,-2,4,-3],[-6,1,3,-7,-3,-6,-8,-9,-9,-6,-8,-2,-7]],[[2,-8,10,-3,7,10,-10,6,2,-3,4,5,-7],[-10,1,-5,-1,-9,-9,9,-8,-8,5,-4,-2,7],[1,6,4,8,5,10,6,-6,-4,1,-7,-10,-6],[7,-3,2,8,-3,7,-10,9,-8,-1,-2,-1,-7],[-3,-9,1,-5,-2,-10,8,-3,-9,7,4,2,2]],[[-2,-6,-3,8,-8,-10,5,1,-4,-1,3,-1,7],[-8,3,-3,-4,6,10,1,-4,2,-5,-5,3,10],[-5,8,8,-2,-7,8,6,1,9,-5,-5,10,-9],[10,2,-9,1,-10,-3,-2,7,-4,-5,8,-6,-4],[-9,10,-1,9,-10,-10,-8,-10,1,3,-1,1,-1]],[[9,-2,-10,-7,-9,3,-2,8,6,2,-9,9,1],[9,7,10,1,8,3,4,-4,1,1,-7,5,2],[-2,-6,-2,-6,-6,4,-10,-9,-8,4,1,9,7],[7,-7,6,2,4,-8,5,-7,-3,1,-10,6,-10],[-1,7,7,10,6,5,9,-4,-2,-2,7,-7,-7]],[[5,3,8,-8,-4,2,-1,1,6,5,-8,8,7],[-5,-4,-1,6,8,-10,3,-1,5,1,8,-5,-9],[2,-2,5,-3,-10,7,8,3,2,-1,9,5,-3],[9,-5,-2,-10,-6,-2,1,3,1,5,-9,-8,-10],[-8,8,5,9,10,9,-6,2,-3,-3,4,10,-5]],[[-8,1,3,10,-1,1,-7,3,-10,10,-8,-8,1],[-4,1,10,-4,7,2,-9,4,-3,2,8,7,-5],[-3,8,4,7,-1,5,9,5,9,4,-7,-8,-5],[4,-6,-6,1,-5,6,-2,-8,-6,-9,8,-8,-5],[9,5,-10,3,7,5,5,-5,-1,-2,4,-5,9]]], dtype = "int64")#candidate|10052|(8, 5, 13)|const|int64
bop_10053 = relay.right_shift(var_10051.astype('int64'), relay.reshape(const_10052.astype('int64'), relay.shape_of(var_10051))) # shape=(8, 5, 13)
bop_10058 = relay.multiply(var_10051.astype('uint8'), relay.reshape(const_10052.astype('uint8'), relay.shape_of(var_10051))) # shape=(8, 5, 13)
output = relay.Tuple([bop_10053,bop_10058,])
output2 = relay.Tuple([bop_10053,bop_10058,])
func_10061 = relay.Function([var_10051,], output)
mod['func_10061'] = func_10061
mod = relay.transform.InferType()(mod)
mutated_mod['func_10061'] = func_10061
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10062 = relay.var("var_10062", dtype = "int64", shape = (8, 5, 13))#candidate|10062|(8, 5, 13)|var|int64
func_10061_call = mutated_mod.get_global_var('func_10061')
call_10063 = func_10061_call(var_10062)
output = call_10063
func_10064 = relay.Function([var_10062], output)
mutated_mod['func_10064'] = func_10064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5211_call = mod.get_global_var('func_5211')
func_5212_call = mutated_mod.get_global_var('func_5212')
call_10098 = func_5211_call()
call_10099 = func_5211_call()
output = relay.Tuple([call_10098,])
output2 = relay.Tuple([call_10099,])
func_10106 = relay.Function([], output)
mod['func_10106'] = func_10106
mod = relay.transform.InferType()(mod)
output = func_10106()
func_10107 = relay.Function([], output)
mutated_mod['func_10107'] = func_10107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8153_call = mod.get_global_var('func_8153')
func_8155_call = mutated_mod.get_global_var('func_8155')
call_10116 = func_8153_call()
call_10117 = func_8153_call()
func_1712_call = mod.get_global_var('func_1712')
func_1715_call = mutated_mod.get_global_var('func_1715')
const_10124 = relay.const([[5,3,6],[-4,2,-5],[-3,-8,2],[-7,-10,8],[4,-8,4],[-6,-3,9],[-7,-6,-2],[-3,10,9],[-3,-8,5],[-1,-6,7],[7,8,-2],[-9,1,-8],[-8,10,-4],[1,-7,-10],[-5,-3,-10],[-10,4,8],[7,3,-5],[-3,-3,3],[1,-5,-3],[3,6,10],[4,4,7],[4,-9,2],[-7,9,5],[7,5,6],[-9,-7,-5],[-10,6,9],[-7,-7,-9],[2,-1,7],[-2,4,8],[-7,-1,1],[-3,6,-8],[3,9,2],[7,3,-5],[-6,7,-4],[3,4,-6],[-1,10,8],[-4,3,-9],[1,-9,5],[-7,10,-4],[10,4,1],[-3,-10,-2],[10,7,9],[-8,-5,-5],[2,-5,5],[-5,-7,1],[10,2,6],[8,10,-1],[5,-9,10],[-1,3,3],[5,3,8],[4,7,-9],[10,2,3],[10,5,-8],[-1,-7,7],[2,-7,-6],[10,-2,7],[-3,9,8],[-9,1,8],[-8,10,-5],[5,-1,-6],[-7,10,-5],[-3,4,4],[-3,2,6],[5,3,1],[-6,-7,9],[7,-8,-7],[2,1,-1],[1,7,-10],[-5,9,4],[-6,-6,-7],[-4,3,1],[-7,10,-2],[5,7,-7],[5,3,10],[3,8,-6],[-4,-1,-4],[-9,-7,3],[9,3,9],[2,1,-9],[-3,-4,-2],[7,-5,-5],[3,2,-2],[-1,10,-7],[-3,-5,6],[-5,6,1],[-4,-6,-1],[5,-6,5],[-1,-8,-4],[2,-6,4],[-2,-3,10],[8,6,-10],[6,10,4],[9,4,6],[4,7,-6],[-6,-10,9],[-4,-2,3],[-5,9,3],[1,-1,-1],[4,7,-9],[-2,5,3],[10,3,8],[-5,-6,-8],[-10,-3,7],[9,1,-5],[-3,5,-7],[-10,-8,10],[-8,8,-1],[-3,9,-3],[-9,-10,-10],[-3,9,9],[-10,2,3],[-3,7,4],[-10,-9,4],[5,-4,-6],[-7,-9,10],[-2,-8,-8],[6,-1,3],[-1,6,-1],[-1,4,9],[-4,-2,3],[-1,-4,-9],[10,-4,-8],[-8,-9,8],[3,-6,7],[-10,2,-3],[5,9,-1],[-2,6,1],[2,-3,-4],[-2,-4,-7],[-4,3,-10],[-10,-8,-2],[9,-1,-9],[-9,4,5],[6,-8,-4],[1,-3,-3],[-9,-5,5],[-8,-3,-9],[3,-5,-1],[6,8,6],[-8,-1,9],[3,-8,-7],[-8,-9,-3],[-3,-8,3],[1,-7,-3],[10,-1,-4],[6,10,-8],[8,3,-6],[4,3,10],[-1,5,-9],[-4,2,1],[-8,5,-10],[7,8,-3],[-6,-6,1],[5,8,-4],[8,7,3],[-8,-4,9],[8,1,-5],[2,3,8],[-5,-8,3],[-9,9,-5],[-3,-3,7],[-10,9,-3],[-8,-4,5],[7,-7,5],[6,-4,-2],[-9,-1,-2],[4,5,3],[-8,3,2],[-5,9,5],[-3,10,7],[-6,6,9],[-8,-10,-8],[1,6,7],[-3,8,-4],[10,5,7],[-3,-8,-2],[9,-2,3],[3,-4,-9],[8,3,5],[-10,-9,4],[-7,-10,-6],[-2,2,-3],[3,-10,-5],[-8,-10,1],[-10,-10,-6],[-4,-1,-5],[-7,-1,2],[4,2,-2],[3,-1,3],[-10,-3,-2],[5,9,10],[-3,5,-4],[10,4,-5],[10,-8,-3],[-3,4,1],[4,-1,2],[-10,-8,10],[4,1,-3],[-4,-4,-2],[-3,-8,-10],[10,5,-8],[3,-1,-5],[-3,1,6],[-2,-7,-5],[5,-3,-5],[-4,-10,8],[-7,7,4],[-8,-2,-2],[-5,1,3],[10,-3,1],[-9,-5,-5],[6,-4,9],[-7,-4,10],[-7,2,-8],[3,-3,2],[-6,-8,-9],[-2,6,-9],[3,-3,-3],[4,-9,-8],[-1,4,9],[7,-8,-4],[9,-1,-3],[9,-4,-2],[-9,-7,-5],[5,5,-10],[-7,10,4],[-10,2,-10],[-2,9,-5],[-5,1,1],[8,-10,7],[-9,-8,8],[3,-9,-3],[-7,9,-3],[1,9,3],[-8,7,-5],[-9,-9,-3],[3,8,2],[10,-6,-7],[5,10,-2],[5,-5,-9],[9,5,8],[-6,8,2],[7,9,-3],[4,-8,4],[-9,-1,3],[7,1,1],[-1,-10,-3],[9,4,-5],[6,-7,-6],[-4,1,-1],[7,-8,1],[-6,8,-3],[8,-1,10],[1,7,-8],[-2,10,-8],[-8,1,3],[-5,4,5],[-4,-7,-7],[-3,3,-10],[-3,-3,-4],[3,8,-9],[-4,2,-8],[5,-1,-7],[9,9,-9],[3,9,-4],[1,-6,1],[-1,-10,5],[9,-7,10],[1,7,-3],[10,10,-2],[-4,-2,-1],[8,8,-5],[5,10,-8],[-10,-4,-10],[-5,1,-2],[8,7,10],[2,1,7],[4,-2,6],[7,-9,-4],[7,9,-3],[-2,-9,-2],[8,7,4],[3,-8,4],[-5,1,-3],[-4,4,-10],[-6,-9,-1],[4,-3,-9],[4,6,-9],[5,3,-9],[-3,-7,-6],[-4,-9,-7],[-2,-10,-1],[5,-2,-9],[-1,-4,-2],[-1,6,2],[2,4,8],[2,2,6],[-4,1,2],[-7,-4,-7],[6,1,-5],[3,8,-1],[-9,-6,-8],[4,-3,-5],[5,-10,-3],[-7,-7,2],[-1,1,2],[-6,4,4],[4,3,-3],[6,10,-6],[3,3,-2],[-3,-10,2],[4,-5,-10],[2,4,-5],[4,4,-5],[7,6,9],[-5,-2,-7],[-4,-4,1],[7,10,-9],[-8,-4,6],[-7,-9,-3],[4,3,10],[2,-10,5],[2,7,3],[7,-8,6],[-2,7,9],[-2,-7,-10],[-4,2,-1],[-7,9,5],[1,-5,-2],[-5,5,8],[3,8,-6],[6,1,5],[-7,2,-8],[9,-8,-8],[-5,-7,-4],[-6,-4,6],[1,1,10],[-3,-8,-2],[-4,4,5],[-4,-7,-3],[-5,-10,3],[10,-8,7],[7,-4,7],[-1,-6,2],[-9,2,-9],[-8,3,-5],[2,4,8],[-7,-3,10],[-8,10,-10],[-7,-9,6],[3,-2,10],[7,-5,-3],[2,8,10],[5,2,3],[-8,-10,9],[-6,-8,1],[8,-1,6],[-7,-3,-6],[-6,-4,-8],[8,-5,-6],[-2,9,3],[-9,5,-5],[5,1,-9],[-2,2,1],[3,10,10],[4,-8,-4],[-2,-1,5],[10,-10,-10],[10,3,-10],[-3,-6,2],[-9,-7,-9],[8,-6,-8],[7,-2,9],[-5,6,2],[-2,8,8],[-3,-6,3],[-3,-7,-10],[-1,1,3],[9,-8,3],[10,6,5],[-8,10,9],[9,4,3],[1,2,-1],[-1,-2,3],[10,5,3],[-2,6,-7],[7,9,4],[-9,5,-6],[-8,-7,7],[-8,-5,-4],[2,-9,10],[-5,2,10],[5,-10,1],[-9,2,-9],[-5,-7,-1],[7,1,-4],[-2,9,3],[1,-9,8],[-6,8,2],[8,-6,8],[-7,3,-2],[10,5,9],[9,4,10],[9,-9,-3],[-8,-8,5],[-4,-10,-2],[-3,6,2],[-4,7,10],[-9,3,-9],[9,-7,-2],[1,-7,-2],[-3,3,-2],[7,5,-3],[-1,-7,-2],[-9,4,8],[-10,-1,-1],[-6,-9,-6],[-4,-5,6],[6,-2,-2],[-9,-3,-8],[-10,-1,-3],[-5,9,-10],[5,7,-10],[9,2,1],[6,-6,-3],[-2,-3,4],[-7,9,-5],[10,-10,1],[4,8,-3],[-2,8,-8],[4,-6,4],[5,10,-5],[2,4,-4],[3,-7,4],[1,9,-3],[10,6,4],[-5,1,-4],[10,-4,7],[-1,6,1],[-8,-5,2],[3,-5,10],[-10,10,-2],[-8,10,1],[1,-10,-2],[6,-3,-6],[-1,1,-9],[-5,7,10],[2,4,-9],[-1,-8,7],[10,-9,-4],[-2,-5,1],[3,5,-3],[-9,-1,7],[9,2,7],[-7,-3,-3]], dtype = "uint8")#candidate|10124|(455, 3)|const|uint8
call_10123 = relay.TupleGetItem(func_1712_call(relay.reshape(const_10124.astype('uint8'), [1365,])), 0)
call_10125 = relay.TupleGetItem(func_1715_call(relay.reshape(const_10124.astype('uint8'), [1365,])), 0)
func_6175_call = mod.get_global_var('func_6175')
func_6177_call = mutated_mod.get_global_var('func_6177')
const_10162 = relay.const([[-8,6,-5,7,-7,-1,-10,-7,7,-7,-5,-9,-2,3,6,-1,-10,2,-5,-5,2,7,-8,-8,-2,4,-9,2,-7,7,2,-8,5,8,-8,6,1,-1,-8,4,6,-1,-2,-8,-10,10,5,4,7,1,7,5,-1,-6,7,-10,1,-2,4,2,5,8,10,-9,4,-4,7,10,8,-6,-10,-2,8,4,3,8,7,-9,5,-6,10,-1,-1,-5,-9,-8,9,-9,-5,9,-6,6,-2,-10,3,-8,-8,-9,2,-10,7,9,9,3,3,-1,-10,2,-4,-8,2,1,5,-1,-4,-7,10,-8,-7,4,-4,9,-4,5,7,6,-1,9,6,2,-2,2,-8,2,1,5,3,-9,-7,6,10,-3,-10,7,-2,-6,2,6,-6,7,-6,-3,8,-7,-8,9,8,1,4,-2,8,3,-5,2,-9,1,3,6,7,6,-10,-7,7,-4,5,9,7,-5,-1,6,-8,-7,2,-2,-1,-8,3,7,1,-3,1,-2,-4,-1,-6,6,3,-6,-9,7,9,10,1,6,-1,2,10,8,-1,-8,-5,2,8,-4,10,-8,9,3,-3,5,7,-6,9,1,-3,8,1,-8,2,7,-5,1,3,5,-4,-2,6,-9,1,7,-7,4,9,-9,3,-2,-3,4,8,3,-10,6,2,2,-3,9,-6,-10,-4,5,-6,-8,2,4,9,-4,4,-4,-5,-2,-7,-10,6,9,8,-9,-3,-3,9,4,7,-7,-10,-7,-9,-5,2,1,-3,9,-6,-6,-5,1,6,-2,-7,-4,-3,-4,-10,1,4,9,4,-9,-8,9,-3,9,-8,-4,1,-2,1,-7,2,-2,-1,4,-10,-6,-9,2,-5,-5,4,-8,9,9,5,-10,3,-5,-4,-10,3,3,-10,8,-7,-10,4,6,-9,3,1,1,7,8,5,6,-5,10,5,5,-2,-3,-3,10,-3,6,-8,8,2,-5,-6,-3,-9,10,-2,5,10,-10,6,4,3,-3,-6,-4,-7,-5,9,5,2,1,-10,10,6,-2,-10,-2,-8,-3,4,-3,8,3,6,7,-3,4,7,-1,3,-5,-2,5,-2,4,-8,8,-5,-5,-10,10,3,7,7,-4,3,-5,-6,3,-9,-5,-6,-2,5,1,-2,-9],[7,8,5,-6,9,3,2,-5,-5,-7,-5,-1,10,6,-4,-8,10,-5,-8,-3,-4,4,2,-6,-10,-7,4,7,-1,8,7,-6,-4,2,-4,8,-1,4,2,2,3,-8,9,-2,10,6,6,4,3,-1,-3,6,1,-9,10,-4,-3,9,-2,10,1,-9,8,-6,-1,7,-3,-10,-3,-7,10,-5,8,3,-6,-9,-1,-1,-2,-7,3,-9,-10,-1,7,5,1,-8,-3,6,4,-6,6,3,6,2,-5,-6,-1,-8,-6,4,3,8,-3,-7,2,3,3,-5,-5,6,8,-6,10,-7,-7,6,3,9,-10,6,-2,-7,4,-1,9,-2,1,7,-2,-10,7,10,-1,7,-7,-3,-3,-3,-4,-7,-4,-3,-7,-8,7,9,-5,-4,-9,-10,-6,-5,-7,8,-5,-6,6,-3,10,-1,9,-10,10,-5,-7,-5,-9,-3,-1,8,8,4,-3,-8,-6,1,10,2,-5,6,3,6,4,-8,2,2,2,-5,-2,-2,-3,-6,2,10,-6,-9,10,10,-7,-2,6,1,1,-7,-1,3,-9,7,-10,1,5,-4,-7,2,3,-5,9,9,3,5,4,-8,-9,-6,-1,-3,-9,3,1,2,-9,-3,2,-8,-9,-9,-1,7,1,6,-2,-8,8,-9,-5,1,9,-2,-7,5,5,10,-2,-5,4,-3,-2,9,10,-9,2,-9,-5,1,-3,-9,-4,-4,9,7,3,-10,-1,-5,9,-8,-3,2,-1,-9,1,3,-8,-10,-8,-10,9,6,-9,2,4,-10,8,2,-7,4,-10,5,-5,6,-4,-4,6,-2,10,6,-2,8,10,-9,-2,5,9,-1,7,-10,6,1,-4,9,-4,8,1,8,-8,8,-10,-4,-5,5,-4,2,-9,-2,-5,-6,5,-9,-10,10,5,-7,-3,6,-8,9,-4,-4,3,5,-8,-8,-5,-1,-5,-2,-9,5,-4,9,10,5,-8,-8,-8,8,3,1,5,4,5,8,7,-7,2,2,-5,-7,-10,3,-7,-6,-8,-10,-10,-1,-10,-10,-2,-7,-4,-10,8,1,2,5,-6,-2,9,7,6,-6,-9,-5,-5,7,3,-6,5,-10,3,10,8,4,-4,7,-9,6,9,-8,4,-2,5,10,7,-10,-7,8,10,3]], dtype = "uint8")#candidate|10162|(2, 432)|const|uint8
call_10161 = relay.TupleGetItem(func_6175_call(relay.reshape(const_10162.astype('uint8'), [864,])), 2)
call_10163 = relay.TupleGetItem(func_6177_call(relay.reshape(const_10162.astype('uint8'), [864,])), 2)
output = relay.Tuple([call_10116,call_10123,const_10124,call_10161,const_10162,])
output2 = relay.Tuple([call_10117,call_10125,const_10124,call_10163,const_10162,])
func_10171 = relay.Function([], output)
mod['func_10171'] = func_10171
mod = relay.transform.InferType()(mod)
output = func_10171()
func_10172 = relay.Function([], output)
mutated_mod['func_10172'] = func_10172
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10210 = relay.var("var_10210", dtype = "float32", shape = (14, 3, 8))#candidate|10210|(14, 3, 8)|var|float32
const_10211 = relay.const([[[-1.992864,-1.634825,-9.330330,-2.511553,1.688517,-8.146108,-5.838750,-5.012758],[2.101718,-4.128732,7.248286,-4.920371,4.723498,-4.245777,-9.866335,-8.936055],[1.037365,-5.433624,2.399584,-9.907410,7.179873,3.838162,2.610756,-3.594987]],[[-2.750594,6.269271,-9.071544,-3.850246,-3.114350,9.853546,-3.165571,-3.479770],[-8.211326,9.585746,6.009475,-3.918237,-4.338768,-1.717914,-2.489884,-8.891554],[8.555068,-1.490862,-0.992635,8.821010,5.389672,7.432555,-0.900046,3.812427]],[[-8.765785,-3.713133,8.175369,-0.622585,-7.619469,8.714780,-8.173250,9.150639],[3.489108,4.121258,-9.098157,0.817137,6.695338,-7.103481,-8.655690,-8.475379],[-6.409271,-9.562708,-4.373386,-7.944544,9.789236,6.367994,1.419877,8.299004]],[[-5.460461,-6.071308,6.435398,-9.834059,-2.905384,-3.141080,1.142218,-1.774386],[7.574901,2.531957,6.122612,7.276481,5.894319,-7.007918,4.897452,-1.712511],[-8.834034,5.573297,-7.579956,-5.392463,-6.157744,2.702328,-1.251745,1.627743]],[[-4.554044,5.427673,-4.998029,-1.655485,4.555314,8.174027,-9.075332,-8.597547],[-3.405956,-6.944372,9.693528,-1.027086,5.301347,8.093813,8.010940,0.610668],[7.557986,7.288122,3.449946,-8.863917,4.867691,-7.639532,4.930946,-0.011933]],[[-7.780574,-7.648187,-0.103657,3.789878,-8.409984,0.692560,6.194483,7.560861],[4.585881,6.097143,-8.154354,6.075814,7.297304,1.509972,-0.475631,-1.557364],[-1.624455,-2.648341,4.865691,-5.178483,2.908747,4.424457,-4.449451,3.316711]],[[-8.827676,5.597902,-8.364381,-9.182540,-5.631303,-5.982821,5.845163,5.121073],[7.905617,-3.626976,1.109382,-0.670917,-0.962028,4.967427,-3.049230,-4.065508],[4.088715,0.258006,-7.173082,4.176397,8.088008,0.551496,7.023091,-5.579641]],[[0.574655,0.943611,4.934562,5.722860,-6.243757,7.508490,6.087070,3.069592],[1.139633,2.709942,-3.046349,-0.765200,-7.545585,-9.238571,-5.485552,1.700161],[-7.884302,-8.152987,-3.662109,6.986276,-4.929056,-7.163673,8.749571,6.273958]],[[-4.259460,-4.220506,8.342080,5.436899,0.746418,1.012858,-5.460888,1.210214],[-7.943304,3.649765,5.750276,4.822745,5.482715,5.024042,7.856610,4.099485],[5.271691,-3.716912,-3.092854,5.232777,8.196608,0.425225,6.157947,-6.713021]],[[-8.841088,-0.634611,7.852726,7.677618,7.668157,8.965939,4.444868,0.933533],[-1.237712,-9.631929,2.978070,-9.587410,-1.915303,-4.695221,-9.403800,2.977370],[-3.767624,-7.390502,1.054007,-9.533917,5.478242,5.307293,-5.843634,8.137278]],[[-7.495230,7.651246,2.627021,0.261944,6.124865,0.029496,-1.072108,-5.623929],[3.490767,-1.639394,8.548755,8.514015,-1.820270,1.219104,0.972697,-6.246895],[-1.016288,0.300929,0.872873,-5.825365,3.132068,7.779818,-8.241516,-9.521321]],[[-6.564344,8.846493,-0.812258,-7.271722,4.396766,5.878397,1.214301,9.020978],[-6.821902,6.410486,1.178500,-6.629025,-5.311990,-5.314496,-3.600794,-5.123105],[-3.891361,-7.388798,-1.263431,8.927467,-4.020331,1.111069,-4.270693,-9.666189]],[[5.415531,2.391290,2.738633,0.750549,7.369594,-2.727834,4.738981,-6.073007],[-5.998616,-1.949258,-2.359325,3.241666,-3.151118,-3.738972,5.602640,5.395394],[-5.751484,4.643894,2.877636,1.898869,-1.653801,-0.260294,-1.135150,4.386628]],[[1.880765,-4.050420,-1.519102,-7.176495,-6.624002,2.445720,1.998717,-3.216939],[3.424859,4.696135,7.306895,0.638111,8.614630,1.719580,8.857037,-0.280128],[-7.810806,-2.546745,-4.275581,1.812860,8.152164,-1.469811,-5.719710,-9.869673]]], dtype = "float32")#candidate|10211|(14, 3, 8)|const|float32
bop_10212 = relay.equal(var_10210.astype('bool'), relay.reshape(const_10211.astype('bool'), relay.shape_of(var_10210))) # shape=(14, 3, 8)
uop_10225 = relay.rsqrt(bop_10212.astype('float64')) # shape=(14, 3, 8)
output = relay.Tuple([uop_10225,])
output2 = relay.Tuple([uop_10225,])
func_10229 = relay.Function([var_10210,], output)
mod['func_10229'] = func_10229
mod = relay.transform.InferType()(mod)
var_10230 = relay.var("var_10230", dtype = "float32", shape = (14, 3, 8))#candidate|10230|(14, 3, 8)|var|float32
output = func_10229(var_10230)
func_10231 = relay.Function([var_10230], output)
mutated_mod['func_10231'] = func_10231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3237_call = mod.get_global_var('func_3237')
func_3238_call = mutated_mod.get_global_var('func_3238')
call_10259 = func_3237_call()
call_10260 = func_3237_call()
func_8228_call = mod.get_global_var('func_8228')
func_8230_call = mutated_mod.get_global_var('func_8230')
call_10274 = func_8228_call()
call_10275 = func_8228_call()
func_6718_call = mod.get_global_var('func_6718')
func_6720_call = mutated_mod.get_global_var('func_6720')
call_10280 = relay.TupleGetItem(func_6718_call(), 1)
call_10281 = relay.TupleGetItem(func_6720_call(), 1)
output = relay.Tuple([call_10259,call_10274,call_10280,])
output2 = relay.Tuple([call_10260,call_10275,call_10281,])
func_10284 = relay.Function([], output)
mod['func_10284'] = func_10284
mod = relay.transform.InferType()(mod)
output = func_10284()
func_10285 = relay.Function([], output)
mutated_mod['func_10285'] = func_10285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4344_call = mod.get_global_var('func_4344')
func_4345_call = mutated_mod.get_global_var('func_4345')
call_10286 = relay.TupleGetItem(func_4344_call(), 1)
call_10287 = relay.TupleGetItem(func_4345_call(), 1)
func_8619_call = mod.get_global_var('func_8619')
func_8622_call = mutated_mod.get_global_var('func_8622')
var_10296 = relay.var("var_10296", dtype = "uint8", shape = (8, 156))#candidate|10296|(8, 156)|var|uint8
call_10295 = relay.TupleGetItem(func_8619_call(relay.reshape(var_10296.astype('uint8'), [16, 13, 6])), 1)
call_10297 = relay.TupleGetItem(func_8622_call(relay.reshape(var_10296.astype('uint8'), [16, 13, 6])), 1)
func_8662_call = mod.get_global_var('func_8662')
func_8664_call = mutated_mod.get_global_var('func_8664')
const_10320 = relay.const([[8.539392,-5.746635,3.824023,4.412260,-3.763159,-2.054496,2.056146,-2.272618,3.439933,-1.731229,7.469121,-6.273487,6.326669,-8.054596,-7.099565,5.780326,4.542034,-4.393606,0.054403,1.136957,-1.580466,2.951845,8.935475,-4.249757,-0.005115,-4.581621,-8.739503,5.599759,-5.020185,5.479498,7.411615,-0.524168,7.421403,-7.102332,1.450886,-1.001377,4.096922,3.517938,0.515009,1.332356,-6.520725,-9.511623,-8.951567,-6.920248,5.055583,-4.717509,3.645218,6.199552,2.688497,0.375860,2.690906,-1.634547,9.007550,3.756043,3.284742,9.783984,5.553528,-7.716188,9.035548,-3.903760,4.798860,7.843064,-2.253392,3.841109,-2.822391,-1.173268,-7.912837,-9.295660,-0.841836,9.575395,-5.504165,-2.091700,-8.813022,-9.942311,0.161251,-5.508649,4.425095,1.891071,5.675135,9.408562,-9.193868,1.973945,-2.612855,-9.961844,-4.604440,-8.820319,-2.417404,-5.515022,4.356097,-1.178885,9.805085,2.829773,0.996293,-1.375690,3.824517,-7.582939,7.051756,5.300538,-2.592222,4.509521,8.025099,6.021185,-6.770922,-8.820309,-7.303221,-4.212398,7.178185,-8.814290,1.997424,1.322405,-4.879248,-0.709937,-0.237526,3.810595,5.800338,6.972519,-0.737538,5.333674,-5.997185,4.367262,-2.028354,-6.929647,9.357053,-5.028964,-0.367957,-8.586623,-8.421143,-6.076038,-7.415086,5.948103,-0.849786,-3.528334,3.298559,8.414346,9.882760,2.471426,6.400886,3.122882,-0.782278,0.353081,-2.551586,-2.673068,-5.748194,9.558534,-5.817795,-5.782994,5.823016,-6.139607,-1.188386,-1.101452,-0.070182,-9.140466,1.019643,-1.493433,6.984755,-2.677448,8.526228,-4.786646,-1.254190,-6.156437,-5.364849,2.305557,5.207635,1.772901,-9.855421,8.488894,9.211665,-4.457134,-0.833092,-2.018111,-3.943871,8.325633,1.312631,6.841631,4.971564,7.616419,-1.885278,3.872409,-2.636786,-7.212134,-8.968227,6.294563,7.269308,-8.410599,-4.260021,0.738355,-1.927333,5.139231,7.825035,1.676352,-6.081646,-9.361696,6.480300,5.834010,-9.475697,-4.845462,8.969394,-0.449067,7.096827,-6.553426,-7.491440,-2.628445,-6.898119,-2.095780,-8.239617,-5.800799,-0.284062,-8.414289,-6.940749,5.336592,4.378041,8.649734,1.762883,0.579582,4.316702,0.797448,5.031426,-3.347213,5.188589,6.559310,-1.904382,-4.399758,4.162434,-2.699456,-5.310617,-8.057948,-7.406325,0.527631,-7.343532,-3.730392,-9.015744,1.972315,-9.582442,-1.062252,-8.259517,5.456962,0.429191,-5.278502,-6.463852,4.495189,-5.072964,-8.772075,6.856875,7.169617,-3.160365,6.455328,4.226616,5.383855,-0.005917,5.827838,5.433276,1.148407,-1.432294,6.233219,1.569692,-3.990846,5.594343,-6.521271,-7.564612,-9.957718,2.999543,2.430464,-4.699616,-9.984339,-9.563233,4.046850,8.943097,0.342882,-7.043980,-6.872187,9.010805,-6.929843,-5.011965,2.885717,-9.828191,5.781064,-3.989025,-2.844403,4.580024,1.809304,-0.861942,-5.212539,-1.685712,8.475544,-4.407832,-9.313800,-2.580107,-1.381980,3.928342,4.172494,1.060639,6.847468,-6.509637,-8.869870,7.190620,2.673166,8.927877,9.064401,9.811884,-8.077120,-7.019622,7.913384,9.826575,3.719675,-6.040026,-0.947772,-2.872951,1.790501,1.114904,-1.565573,4.133716,-8.446459,4.318228,-0.034443,7.856835,1.736045,1.181376,-4.624047,-5.023789,8.558901,6.458741,5.284913,-5.684094,-2.981973,-1.915025,-4.708576,-9.521488,-2.034077,-3.483945,5.654256,-1.424444,5.342139,9.497203,-7.604524,-8.797605,-5.244129,-7.440786,0.087405,-5.144009,-9.976026,-9.096634,0.573970,-0.190025,3.690712,-1.244813,-2.124250,7.401282,6.836478,1.054851,-8.047847,7.320375,9.716380,-0.415280,-0.829806,-0.739100,-7.005099,9.019857,-8.832817,4.056059,-7.895207,-4.148655,-9.987571,2.202319,-6.393441,-0.408533,-1.208074,-3.152213,5.349654,-0.116867,1.971447,-2.879540,1.099346,6.434613,6.388399,3.412386,1.705915,-7.039338,1.473683,4.610446,8.127357,0.272921,7.401917,6.794444,-5.978920,9.192094,5.781579,2.756956,5.612731,-7.076203,-2.817396,9.914849,3.054704,7.014004,2.527533,-6.304696,-8.827775,-2.510746,3.220253,-6.544359,3.301185,-6.522323,-7.318426,0.313868,-2.911196,-1.943752,-3.438033,-1.192581,-2.348056,-6.327122,-5.290439,-0.528450,-2.632671,9.754411,-2.243524,-0.072754,0.478298,-7.484401,-3.679077,8.581734,5.996726,4.744710,6.683759,8.089193,-9.982207,7.541757,0.865421,8.733366,-6.973008,8.948840,8.875030,-0.401481,-6.100678,-3.320636,4.599909,-3.289897,8.406649,-1.408052,4.191017,-3.596768,2.141913,3.844690,9.378356,4.855147,0.262127,6.296281,-2.375510,5.188318,-7.842650,2.951643,4.327068,5.008163,-1.227290,-3.732884,1.412292,5.218921,-7.607783,2.733634,7.228572,-4.745243,-8.432347,0.998831,9.349897,9.781246,-8.236165,3.842566,-0.274571,8.054009,-8.110026,7.191193,-8.701684,0.422539,6.205338,0.239143,6.457722,3.862855,3.955147,-4.839851,1.957118,-4.262079,-5.448588,6.329993,-0.599988,8.789568,-6.971190,6.124267,1.250263,-4.147819,2.586554,-6.725034,8.097983,-4.140991,-7.761539,7.932513,1.756087,-8.846632,-0.836933,-1.473369,-5.196676,9.595343,-0.701955,7.535263,8.856085,-3.311347,9.638985,6.850937,-2.021824,6.133832,-2.285236,-9.388471,5.408250,-2.777324,5.932617,-0.774801,-0.105213,-0.280462,-3.566599,3.457871,2.736435,5.076390,-7.776119,7.171478,-3.219274,1.723958,-6.288463,-7.949844,-8.504808,7.129249,-1.944882,9.531185,1.684602,8.196622,-4.655347,-7.297057,6.901728,-4.249420,-5.182301,-2.248880,2.284521,-0.594260,-4.060007,0.721846,9.500359,-4.140593,-5.626126,-5.172715,2.392718,-1.748397,-9.125786,-8.611823,-4.196588,1.809484,-0.508424,5.970037,-4.259846,5.603239,1.751677,2.458007,5.001201,-1.501449,-4.874402,-3.636497,-8.103263,1.809179,2.839718,-6.282100,-2.481778,-7.521692,-8.010091,-2.355276,0.456348,4.305943,-5.731555,6.191733,-7.315053,-3.470279,3.155560,-8.234597,6.935002,-0.102628,6.987802,-0.509536,5.741369,8.289190,-8.038299,-3.713951,3.479978,-6.224212,-2.168163,-0.202227,3.665545,3.772681,3.646240,1.794559,3.851615,1.170244,-8.750978,4.514586,-5.657298,3.397496,-1.885276,5.059212,3.158607,-0.989941,1.685779,-6.549733,5.000479,2.610059,-5.725548,1.264783,9.778481,-6.549867,-5.852641,4.116027,-2.636155,7.956493,-4.053491,3.339207,4.953680,2.463943,-6.534950,6.433665,-1.299057,-5.752557,6.766081,-7.608851,-1.901700,4.887016,-1.125228,7.406931,6.230135,-9.033739,2.157232,-2.444704,6.610479,-4.051331,5.011224,5.018711,-8.951551,-6.414778,6.863491,-5.567556,-9.120637,-9.632067,-6.051099,9.637047,-7.029287,3.319274,5.291696,-8.277378,-9.144727,-7.636577,4.670467,4.923299,9.947551,3.610854,-4.617958,-3.785665,8.678518,-2.835140,6.510999,-4.847276,4.403617,9.171807,5.307803,0.651813,-6.749564,2.425200,9.073994,-7.420938,5.943177,8.637306,7.020202,-9.483446,-6.784998,5.352239,-1.046509,2.037411,1.061782,5.373721,8.724886,-6.489851,-9.199251,3.409499,-0.040459,7.228096,7.715625,-7.660604,-0.605226,-7.877009,4.406406,-5.943558,8.144838,3.823040,5.453207,6.966073,7.229915,-4.228673,7.273519,0.565559,7.287303,4.742940,4.998309,-1.440794,-7.065036,-1.284607,-1.648615,-1.291266,-6.464216,-1.839362,-0.749874,-0.364786,-3.395829,0.289543,-5.945618,0.438753,9.135533,1.415625,-0.594515,5.226696,-9.353436,-0.477411,-2.795711,-6.702553,-3.845081,-5.901992,-6.867483,-1.778282,-0.388737,-2.838127,-1.129238,-8.135871,0.712511,-7.836774,0.315704,-7.034231,3.577860,-0.241225,2.331540,4.287354,-0.497932,-0.065674,-0.825392,7.058035,7.799356,-7.906346,3.019586,9.467670,-7.999182,8.355317,2.195630,6.986253,-2.518482,1.276575,-7.934118,-6.620384,-1.830920,4.003354,5.413875,0.280932,-2.947071,4.200537,1.473122,-5.518984,-7.738421,8.702459,-8.927895,7.053457,0.505862,-3.066289,9.076946,-7.114791,-8.642180,-3.450678,-1.309908,-4.371131,5.235556,-2.915343,-3.736891,-2.995355,-1.076307,0.647737,-1.335278,-1.700889,7.950929,6.521395,7.631463,-9.405168,5.052899,7.806007,1.820349,3.491427,8.566928,4.029379,-7.132854,2.677454,7.169904,6.236113,3.963243,3.007478,3.336220,9.161014,-8.075421,-7.228395,-7.011962,9.666864,3.500348,6.668637,7.797333,-3.342118,-9.810219,-2.521088,-8.090761,-2.147248,7.743183,-1.270070,-3.727685,6.232418,-3.972547,9.389941,-0.066411,-0.680455,4.609963,-2.453534,-5.639992,-7.253276,-5.856432,-6.802165,3.517600,-3.289675,2.213844,8.645035,-2.468859,-7.440568,-0.297214,-2.404197,2.402699,-2.856727,-6.334334,7.601611,1.964423,3.540196,-5.982216,2.579704,-8.201507,2.279740,-5.543885,-4.370569,9.323306,5.731815,-4.589555,-6.767474,-5.915732,-5.426354,-4.687939,7.017861,9.562983,1.561079,1.047820,5.257531,8.546677,3.807117,3.448702,-1.533718,-7.537290,-3.789333,4.064931,-9.995005,1.999232,-5.888108,-0.879422,-4.341842,8.157044,-1.846597,-2.695070,-5.366638,-2.838314,4.456518,7.425348,-9.275591,-5.385367,-7.358915,-0.874950,8.978780,1.486571,8.163409,-6.195918,-5.651061,8.757175,-1.353903,-0.359902,0.512048,-5.754810,6.126225,2.205417,7.671052,-2.697406,0.714473,7.554594,7.781852,5.853326,-2.291457,-1.609220,4.200944,4.526682,7.577012,-2.771569,-3.866291,5.124478,1.868322,-1.155007,-0.003476,-3.686068,9.492694,8.181335,6.825873,7.529036,-8.746955,-4.767232,5.972271,4.188276,2.512292,-1.128125,-0.162541,3.809111,-6.322711,-4.480260,4.534064,-6.287223,-9.317859,3.721993,-0.966321,-4.533630,-1.606514,-6.352930,-4.497296,-2.619693,-0.115396,-8.249785,-7.264073,-5.311730,0.601611,-0.488224,1.577113,6.385607,-9.515617,4.628940,7.243269,2.340804,-3.443875,3.336467,1.403707,5.151520,-4.130496,-6.967900,6.194584,2.481725,6.855931,2.329670,8.509043,5.415960,4.695568,-2.253732,-5.547186,-8.880150,-6.700203,3.661288,1.119106,4.936549,-9.171677,0.471848,-8.406073,-6.592369,-1.971505,-1.862957,-5.370977,0.883950,1.062524,-7.640453,9.919779,-6.764482,3.531163,5.794783,-1.771140,-4.650870,-9.187547,2.609613,6.242574,-4.712891,4.860976,4.853717,-4.083523,-4.491427,-1.291882,4.617711,3.309649,6.696692,-4.355826,-7.843413,9.593124,2.356281,-1.332888,-3.832953,6.898335,2.255920,-5.789930,-9.717607,5.078682,-6.184589,-6.664334,2.147345,6.558648,-4.898562,3.383461,8.272926,2.195930,-1.353399,2.176778,3.742596,6.218053,4.517810,4.695402,2.056382,-2.768898,4.229856,8.324773,6.427714,7.369489,-8.561019,-9.962896,-4.959053,8.980233,1.018643,7.909051,6.147724,0.214700,-7.855581,-1.038520,6.716456,9.014827,6.569833,1.988354,-7.119649,-8.077104,1.566211,-1.268484,0.702116,-0.689558,-1.244740,2.202754,-5.693506,-4.285064,-9.834913,-2.410163,-2.727734,-8.234314,6.228576,-8.680421,-6.010550,-0.114206,5.769667,3.817770,-7.985669,2.114423,-6.283163,-7.990727,3.529001,2.897298,-4.963633,8.865107,-2.061719,-5.248751,9.371823,1.669718,-7.154390,5.460182,-8.345209,-5.533273,-3.910324,7.581965,-3.915551,4.523621,-3.020094,3.001200,2.964254,1.171260,-6.381469,5.848110,-3.106112,-7.450935,-5.305748,-7.091467,-2.915227,-7.733955,-5.151577,6.459525,1.117043,-6.218604,-2.699610,-4.342078,-8.668377,3.254997,-3.950303,-3.859828,7.656257,8.537513,-3.908636,-1.080565,-2.480648,1.985138,-4.784504,3.769054,-1.670086,7.549531,-6.217706,-1.790591,-4.137293,5.488863,-8.692994,8.696402,-2.926126,9.789817,9.479023,-1.461925,-6.999896,-4.608146,-0.907115,5.895062,-7.255064,3.530970,-9.360104,0.046119,7.484507,6.457901,5.134017,1.974288,5.897637,-9.927725,-5.700373,-9.181659,0.379918,0.060433,0.738215,-1.021740,-0.679190,-4.605875,8.779377,3.329357,-0.324521,-5.669786,1.900059,-4.087902,-9.665731,1.878812,7.065441,-5.608814,5.936326,-5.967943,-5.626471,-0.708136,8.749737,5.185971,-3.762572,7.903407,-0.611857,-9.639825,-6.521913,-4.447215,-8.105347,7.850742,-9.984299,-0.998523,-1.654252,-6.395587,7.705340,3.929840,4.773588,8.684462,5.610943,-3.259080,-6.275720,4.342677,7.489583,7.437610,-0.245755,0.970711,-7.447800,-8.147396,1.212343,3.028642,5.246742,1.006088,-1.919727,-9.888730,3.756537,2.265622,-1.224748,-5.621464,-6.992659,3.669920,7.502064,4.096342,-7.727651,-3.632397,-9.584426,-8.357314,-2.993743,-8.505711,-9.130958,-5.330709,-3.329062,7.615119,-9.414707,-8.691683,4.701970,8.981659,8.153430,1.637080,-7.281558,7.520640,3.956227,-3.576377,9.840919,-3.344178,-7.623728,3.174960,-3.068534,3.144042,9.768274,-0.405060,7.936976,0.150519,-0.928672,-1.996126,-8.551826,-1.259400,1.677966,6.782660,3.010280,-4.179657,-8.871956,-1.009621,-7.523906,2.954543,-9.508823,-6.102764,-1.234904,-7.553549,-5.951799,0.177043,-2.795190,1.568355,3.921061,-2.819487,-4.467381,-4.204979,-9.725353,-4.031951,-3.006743,-8.419489,1.055972,-1.533236,-6.823568,-7.848358,5.876031,8.443212,7.242190,4.342602,6.316434,-1.077792,-0.247296,-5.328290,6.682462,4.560504,9.150267,-5.740667,-9.720318,-9.310299,0.748129,-0.548386,-9.771892,-1.510060,-6.732905,-1.048207,7.104334,5.526154,2.172286,0.101714,-0.370986,-8.490451,-2.923451,-8.807970,2.589832,-4.064478,-2.971349,2.432489,-5.135268,-7.015221,1.675252,7.713151,2.064150,-1.659446,-1.608830,-7.378006,-4.042517,-4.294717,1.985542,-7.368213,9.912548,-2.965262,3.354176,4.406112,5.851487,-6.714036,-5.177189,-3.648631,-7.038212,8.322309,-1.954822,-7.499750,-2.670421,8.984788,4.442223,2.445899,-9.080989,-0.744075,8.480667,-9.543528,-5.149197,-2.641468,-9.063275,-0.043526,3.916365,3.895174,3.727260,7.089295,5.825503,-5.754884,-4.408593,7.775972,8.329785,-4.468293,6.191041,9.291552,0.044738,3.524875,-1.508097,-2.975297,8.978347,7.018491,9.231466,-7.506418,-6.144863,-3.037968,-1.778762,1.698065,0.022140,7.183407,-4.944377,-3.059451,-1.981779,3.549260,-7.201410,-0.973287,-3.095401,-9.645395,-9.695304,-4.985189,8.140045,6.030786,-1.169909,1.259107,-7.002360,0.634240,-9.786048,-2.480451,9.417701,8.160012,-2.043039,1.091518,-5.242678,-9.317087,-6.845802,1.811193,3.095898,-4.446202,1.794503,-7.815175,-9.706560,0.881181,0.646848,4.800661,3.114428,-0.900038,-5.407958,-7.592372,-0.847483,-3.395888,7.791425,-8.908567,-9.546267,0.629073,1.658619,-8.869085,7.212004,-3.919811,2.344604,6.445188,-2.043429,-4.619550,5.191531,9.154740,-3.136432,-9.333694,8.226475,-5.144872,6.638284,-2.272978,2.409736,-5.905267,-6.124260,-4.978762,-8.845974,-5.395701,5.272766,-2.303084,-0.550054,-6.683666,0.820028,-7.527660,-6.485749,-1.901612,-6.549538,-0.022360,8.331813,-9.238580,4.101809,-6.220416,-3.928455,-2.394661,2.056373,-9.100374,6.607434,-7.399932,-7.909543,3.304439,-8.843618,-2.598920,-3.632484,-6.373335,-4.252947,1.926965,5.822843,9.921723,8.811634,-4.507405,-5.531102,-4.651387,0.769277,-8.877489,5.797099,-4.829263,-2.868206,4.695112,2.308637,-3.453255,-7.210625,4.613952,0.393475,-4.990205,2.504127,-8.150435,2.747772,8.637675,5.098027,-0.270361,0.797950,-1.680104,-2.658315,4.026648,-8.760582,8.367235,2.964679,-5.292833,9.135961,9.031581,4.044466,1.374477,-0.580751,-8.435785,-5.761338,5.836872,3.705220,8.069246,7.039090,-2.399688,6.633652,-8.519531,-0.929897,0.451881,0.830142,-5.619020,-0.118890,-9.807416,-1.087186,4.209632,1.729297,2.339435,-7.186294,-4.611202,6.706364,5.803792,-6.278922,4.545871,2.942636,4.334103,-8.241612,7.380528,5.312646,2.036647,-5.004392,-1.508256,7.614591,4.053237,8.718617,5.634802,-1.865596,7.082700,2.790732,6.223330,9.379932,3.202523,0.666172,4.335205,-0.121373,-3.630714,1.208994,1.559484,-2.888803,-3.930608,-4.212501,-7.345239,6.090261,-4.614001,6.029285,7.009763,-9.584576,-8.982925,0.575334,-8.251870,-8.142371,8.984043,1.869533,3.475458,6.640604,3.815928,6.020824,-8.526151,6.217351,7.728835,-2.949149,-1.110910,-8.312292,-0.817152,-1.862739,4.766254,-1.910180,-6.682391,6.537037,8.103021,1.944602,2.012739,6.220806,6.440620,-3.648945,7.339301,8.677898,2.011311,-1.903252,-3.013798,-3.327141,9.918754,-4.898576,-4.427529,6.806606,-7.463129,0.419618,-8.839655,1.785469,7.923720,-0.985129,-6.540374,-4.620918,5.629752,-5.649985,1.375222,-8.315062,9.148817,-4.227074,-4.895626,0.724155]], dtype = "float64")#candidate|10320|(1, 1600)|const|float64
call_10319 = relay.TupleGetItem(func_8662_call(relay.reshape(const_10320.astype('float64'), [1600,])), 4)
call_10321 = relay.TupleGetItem(func_8664_call(relay.reshape(const_10320.astype('float64'), [1600,])), 4)
func_5118_call = mod.get_global_var('func_5118')
func_5119_call = mutated_mod.get_global_var('func_5119')
call_10323 = relay.TupleGetItem(func_5118_call(), 1)
call_10324 = relay.TupleGetItem(func_5119_call(), 1)
var_10326 = relay.var("var_10326", dtype = "uint8", shape = (8, 156))#candidate|10326|(8, 156)|var|uint8
bop_10327 = relay.not_equal(var_10296.astype('bool'), relay.reshape(var_10326.astype('bool'), relay.shape_of(var_10296))) # shape=(8, 156)
const_10334 = relay.const([[[3.495755,-0.332438,7.384977],[-1.082519,2.850706,-5.784136],[4.609572,-3.132612,-8.380915],[5.585716,-7.855700,-3.601401],[0.709823,-8.674544,-3.712541],[-3.033234,-0.271541,1.359368],[6.208510,6.383872,3.228404],[4.932587,-5.134771,1.273503],[-7.062428,-3.145972,-2.203704],[-8.272683,-8.842178,-3.652731],[-9.339506,-3.904161,5.189667]],[[-7.382042,5.115186,8.025198],[8.327127,5.214015,9.153076],[6.974088,8.549540,-3.008272],[-5.063542,-6.943015,2.814049],[7.117295,1.153044,3.407697],[-9.834078,-5.206819,9.299417],[-9.866373,-3.740131,-0.749071],[-2.532322,-6.734487,-9.004382],[1.984991,4.314797,2.988486],[-6.435651,-8.091936,8.011621],[5.028433,6.756604,6.104524]],[[8.741613,4.844737,-7.965024],[2.268195,6.292051,-5.027228],[6.303462,-5.817199,9.292904],[9.608683,6.816263,-4.495043],[8.934146,-5.560012,2.107834],[-9.655400,5.760526,-0.629036],[6.511654,5.377214,7.173617],[-1.391423,3.593812,9.375842],[0.545414,5.459264,-7.431327],[0.169851,1.736190,-6.024567],[3.443226,4.398339,1.883721]],[[-0.784989,-5.157732,1.261365],[-9.000571,-8.243638,5.800348],[-5.800571,-4.928285,6.854260],[8.418010,8.851893,-2.629927],[9.656155,-5.576319,-1.095158],[8.255600,-9.451373,-1.900062],[8.244471,-3.314684,7.110036],[-5.976680,-9.341096,0.080763],[8.057335,-3.122465,3.415691],[2.218837,-0.100755,2.061702],[9.098349,-8.906883,-6.542833]],[[3.692765,8.847898,1.144313],[0.935795,-2.513695,7.919544],[7.536757,2.536540,9.466945],[-5.427643,6.064369,-2.564450],[-8.968736,5.978775,6.735528],[1.659236,-4.351649,-0.446783],[6.467820,3.854807,7.704208],[8.097866,6.146880,-3.427436],[7.263460,5.158479,-9.806373],[-8.219776,5.190361,2.827815],[7.750361,-5.276995,9.117762]],[[-6.263580,-8.817622,-7.321073],[-6.163405,5.266508,-0.485822],[-5.348260,-3.310498,6.970813],[8.622102,3.794332,9.150575],[9.001788,-3.680754,-7.895521],[1.299405,-8.044694,-7.060532],[8.805954,6.550145,2.593052],[5.645951,4.438764,5.714198],[-9.224480,-0.485562,-7.798930],[-9.011910,4.117383,5.388845],[-3.179873,-8.856774,-1.671650]],[[0.576212,5.009225,-4.283244],[7.116867,-3.554651,-1.941847],[3.900376,-8.314433,-3.208911],[9.234852,-9.209857,6.929452],[0.165373,-3.656798,6.949448],[-1.041367,5.211045,0.921994],[-1.581773,4.397691,6.894226],[9.249690,-4.544986,5.956423],[-4.786072,8.199716,3.886275],[-2.966348,-6.903019,-7.458964],[7.109081,-8.500578,-4.627073]],[[7.672217,-5.176349,2.788334],[-5.420074,-9.830174,-6.728773],[2.723734,2.934814,2.789020],[-8.435219,4.003450,2.465609],[-1.305004,-3.901186,4.328402],[-4.788732,-0.212881,2.058169],[-9.798515,-5.326580,-6.746045],[-5.481174,1.388626,-0.446038],[-8.254051,-1.156225,1.597163],[1.557638,-0.723452,-0.625662],[-4.067685,-0.314985,-6.716517]],[[-6.644288,6.395727,1.623563],[9.249877,-9.949080,5.897228],[-5.198172,4.618637,9.781878],[-8.432423,-8.624506,5.331110],[-9.158507,4.357850,-7.416319],[-0.231488,-5.875743,4.203796],[5.902547,-0.494442,7.634329],[-8.047001,0.405097,-0.651267],[-5.156928,-4.853072,7.912673],[1.720350,8.430695,1.750354],[-6.584870,3.322251,2.168697]]], dtype = "float32")#candidate|10334|(9, 11, 3)|const|float32
bop_10335 = relay.divide(call_10319.astype('float32'), relay.reshape(const_10334.astype('float32'), relay.shape_of(call_10319))) # shape=(9, 11, 3)
bop_10338 = relay.divide(call_10321.astype('float32'), relay.reshape(const_10334.astype('float32'), relay.shape_of(call_10321))) # shape=(9, 11, 3)
output = relay.Tuple([call_10286,call_10295,const_10320,call_10323,bop_10327,bop_10335,])
output2 = relay.Tuple([call_10287,call_10297,const_10320,call_10324,bop_10327,bop_10338,])
func_10341 = relay.Function([var_10296,var_10326,], output)
mod['func_10341'] = func_10341
mod = relay.transform.InferType()(mod)
mutated_mod['func_10341'] = func_10341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10341_call = mutated_mod.get_global_var('func_10341')
var_10343 = relay.var("var_10343", dtype = "uint8", shape = (8, 156))#candidate|10343|(8, 156)|var|uint8
var_10344 = relay.var("var_10344", dtype = "uint8", shape = (8, 156))#candidate|10344|(8, 156)|var|uint8
call_10342 = func_10341_call(var_10343,var_10344,)
output = call_10342
func_10345 = relay.Function([var_10343,var_10344,], output)
mutated_mod['func_10345'] = func_10345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9515_call = mod.get_global_var('func_9515')
func_9516_call = mutated_mod.get_global_var('func_9516')
call_10513 = relay.TupleGetItem(func_9515_call(), 1)
call_10514 = relay.TupleGetItem(func_9516_call(), 1)
output = call_10513
output2 = call_10514
func_10532 = relay.Function([], output)
mod['func_10532'] = func_10532
mod = relay.transform.InferType()(mod)
output = func_10532()
func_10533 = relay.Function([], output)
mutated_mod['func_10533'] = func_10533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2955_call = mod.get_global_var('func_2955')
func_2957_call = mutated_mod.get_global_var('func_2957')
call_10534 = relay.TupleGetItem(func_2955_call(), 2)
call_10535 = relay.TupleGetItem(func_2957_call(), 2)
func_1574_call = mod.get_global_var('func_1574')
func_1575_call = mutated_mod.get_global_var('func_1575')
call_10536 = relay.TupleGetItem(func_1574_call(), 2)
call_10537 = relay.TupleGetItem(func_1575_call(), 2)
output = relay.Tuple([call_10534,call_10536,])
output2 = relay.Tuple([call_10535,call_10537,])
func_10553 = relay.Function([], output)
mod['func_10553'] = func_10553
mod = relay.transform.InferType()(mod)
mutated_mod['func_10553'] = func_10553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10553_call = mutated_mod.get_global_var('func_10553')
call_10554 = func_10553_call()
output = call_10554
func_10555 = relay.Function([], output)
mutated_mod['func_10555'] = func_10555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5797_call = mod.get_global_var('func_5797')
func_5798_call = mutated_mod.get_global_var('func_5798')
call_10709 = relay.TupleGetItem(func_5797_call(), 0)
call_10710 = relay.TupleGetItem(func_5798_call(), 0)
output = relay.Tuple([call_10709,])
output2 = relay.Tuple([call_10710,])
func_10711 = relay.Function([], output)
mod['func_10711'] = func_10711
mod = relay.transform.InferType()(mod)
output = func_10711()
func_10712 = relay.Function([], output)
mutated_mod['func_10712'] = func_10712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5783_call = mod.get_global_var('func_5783')
func_5785_call = mutated_mod.get_global_var('func_5785')
call_10759 = func_5783_call()
call_10760 = func_5783_call()
output = call_10759
output2 = call_10760
func_10766 = relay.Function([], output)
mod['func_10766'] = func_10766
mod = relay.transform.InferType()(mod)
output = func_10766()
func_10767 = relay.Function([], output)
mutated_mod['func_10767'] = func_10767
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10801 = relay.const(5, dtype = "int32")#candidate|10801|()|const|int32
var_10802 = relay.var("var_10802", dtype = "int32", shape = (6, 12, 16))#candidate|10802|(6, 12, 16)|var|int32
bop_10803 = relay.less_equal(const_10801.astype('bool'), var_10802.astype('bool')) # shape=(6, 12, 16)
func_5783_call = mod.get_global_var('func_5783')
func_5785_call = mutated_mod.get_global_var('func_5785')
call_10808 = func_5783_call()
call_10809 = func_5783_call()
func_10711_call = mod.get_global_var('func_10711')
func_10712_call = mutated_mod.get_global_var('func_10712')
call_10823 = relay.TupleGetItem(func_10711_call(), 0)
call_10824 = relay.TupleGetItem(func_10712_call(), 0)
func_2243_call = mod.get_global_var('func_2243')
func_2244_call = mutated_mod.get_global_var('func_2244')
call_10830 = relay.TupleGetItem(func_2243_call(), 0)
call_10831 = relay.TupleGetItem(func_2244_call(), 0)
output = relay.Tuple([bop_10803,call_10808,call_10823,call_10830,])
output2 = relay.Tuple([bop_10803,call_10809,call_10824,call_10831,])
func_10841 = relay.Function([var_10802,], output)
mod['func_10841'] = func_10841
mod = relay.transform.InferType()(mod)
mutated_mod['func_10841'] = func_10841
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10842 = relay.var("var_10842", dtype = "int32", shape = (6, 12, 16))#candidate|10842|(6, 12, 16)|var|int32
func_10841_call = mutated_mod.get_global_var('func_10841')
call_10843 = func_10841_call(var_10842)
output = call_10843
func_10844 = relay.Function([var_10842], output)
mutated_mod['func_10844'] = func_10844
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5211_call = mod.get_global_var('func_5211')
func_5212_call = mutated_mod.get_global_var('func_5212')
call_10873 = func_5211_call()
call_10874 = func_5211_call()
output = call_10873
output2 = call_10874
func_10890 = relay.Function([], output)
mod['func_10890'] = func_10890
mod = relay.transform.InferType()(mod)
mutated_mod['func_10890'] = func_10890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10890_call = mutated_mod.get_global_var('func_10890')
call_10891 = func_10890_call()
output = call_10891
func_10892 = relay.Function([], output)
mutated_mod['func_10892'] = func_10892
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10914 = relay.var("var_10914", dtype = "int16", shape = (4, 11, 12))#candidate|10914|(4, 11, 12)|var|int16
var_10915 = relay.var("var_10915", dtype = "int16", shape = (4, 11, 12))#candidate|10915|(4, 11, 12)|var|int16
bop_10916 = relay.not_equal(var_10914.astype('bool'), relay.reshape(var_10915.astype('bool'), relay.shape_of(var_10914))) # shape=(4, 11, 12)
uop_10934 = relay.exp(bop_10916.astype('float64')) # shape=(4, 11, 12)
func_3992_call = mod.get_global_var('func_3992')
func_3994_call = mutated_mod.get_global_var('func_3994')
const_10938 = relay.const([8,-5,-10,-2,-1,2,-6,-2,-5,-4,8,9,8,-10,4,-4,-5,-5,-7,-4,2,6,10,-7,-5,-9,2,6,-9,3,-8,-8,-5,5,-9,-2,4,1,8,-8,-6,7,7,9,10,9,-8,-10,-9,-5,-6,3,7,-4,3,-7,1,10,7,-5,-3,4,1,-4,-1,-1,10,-8,10,-3,4,-4,5,-6,-3,-7,3,-8,7,7,3,-6,-3,-1,6,8,3,6,5,-10,3,5,-1,10,-4,-6,6,1,6,-6,5,2,-7,-8,2,-1,5,1,-8,2,2,1,1,1,4,-10,1,-1,-4,-1,6,1,7,-7,-7,-6,-8,8,9,-7,-7,3,10,-6,-2,-1,10,-2,-6,-3,10,3,-8,-9,10,-9,-4,-5,-8,-9,10,1,-1,-9,1,-3,3,3,9,-8,10,8,-2,8,-5,-10,-6,7,3,-6,7,-7,5,2,2,3,-9,-5,3,3,-2,-5,6,-6,9,5,-9,-8,2,8,-2,-7,-1,6,-8,4,-3,-10,2,-8,-8,-8,-7,3,8,5,-2,3,-5,-1,-7,4,-7,-9,-2,9,1,-9,4,8,-3,2,-3,3,5,10,-1,9,1,-7,4,1,3,-4,3,-1,-4,4,-9,7,10,-5,4,-7,4,7,9,-5,-9,-1,2,-9,-6,-8,-7,-10,-2,8,-1,-2,10,-6,7,-3,-2,-9,8,-5,-8,-1,5,3,-8,-7,9,-7,7,10,-5,-2,-9,3,6,4,-8,10,10,-5,8,9,-9,6,8,-4,1,1,-5,-9,-2,-5,-10,8,-10,-8,2,6,4,1,-2,-4,-9,10,9,4,-2,4,6,4,4,6,9,-1,-8,4,5,10,3,9,1,5,-4,7,-2,8,3,4,-6,5,-5,-3,-7,6,4,1,-9,-9,5,3,-7,3,-2,3,10,-5,7,7,10,-1,1,10,-8,4,-6,-1,5,6,1,-9,-5,7,-2,-5,10,-7,-10,4,9,-3,3,10,8,-9,-5,-9,5,-2,10,9,5,-4,6,-5,6,-10,4,8,7,-2,-10,-1,-6,-1,-4,10,-8,-4,-4,9,-9,-8,-10,4,6,8,-6,10,-5,2,-3,7,-9,-8,-4,-1,-6,5,-7,-3,-4,8,1,-5,1,6,-10,-5,-7,-1,8,3,1,3,-6,1,-9,-3,-9,9,-6,1,-9,6,-9,-5,9,2,8,7,2,-6,-1,3,7,-9,4,-10,8,9,3,4,-3,-1,4,5,-10,-8,1,-10,-3,3,10,-10,-9,6,4,3,8,8,-4,9,3,-4,1,5,2,1,3,-10,2,-4,6,4,1,-8,-5,8,6,-4,-5,-1,9,9,-3,2,-3,-2,4,-4,7,2,9,-10,4,-2,-5,6,-4,3,1,5,-4,4,-2,-4,10,-1,-6,4,4,-8,10,2,6,3,3,-1,4,6,4,5,6,3,-6,3,-4,1,-5,-9,-10,-8,10,-9,-7,-2,-5,-4,-4,4,-3,-4,-7,10,7,3,-2,10,4,-8,-4,-1,1,1,-4,7,-3,-4,-5,-6,-6,10,2,1,1,7,4,-6,5,10,6,9,-8,4,1,-6,9,-6,7,-6,-9,-4,3,5,9,9,5,-7,-3,6,8,-1,-7,-9,4,-3,-10,-5,-8,3,10,-3,4,-7,10,10,-5,-7,8,9,1,7,10,6,-6,5,3,-10,7,-3,-9,7,4,8,-1,-3,8,6,2,6,-1,4,9,2,-1,5,7,-6,7,10,9,-10,3,-7,-8,-5,-3,4,4,10,-10,-7,-8,-8,5,2,-3,-4,-10,3,3,-4,10,-8,3,-10,-2,10,10,-6,-7,-10,3,-9,3,9,-4,2,-3,8,8,-9,-7,-10,-8,-1,-7,9,4,-2,-2,5,-8,-7,7,6,-5,6,7,-8,-4,-4,-9,10,-9,-10,-3,-4,-10,-3,8,2,6,7,6,10,4,9,-7,5,-1,-6,8,7,-4,-6,-10,10,-10,1,2,-4,-9,8,-3,-1,-7,-1,10,-6,-8,9,-3,-6,-5,9,-2,4,9,5,-4,-6,-5,8,5,-2,-6,-3,-1,4,-5,3,-7,9,8,5,2,5,-10,-5,-8,-2,-7,5,-1,3,-3,5,5,5,-6,7,4,5,8,-3,-6,-1,7,2,7,5,-2,-2,-2,2,7,-8,-3,7,5,-6,-2,-6,4,-6,-3,-3,-1,4,1,-3,-3,-1,6,-6,7,-1,-10,7,-5,5,6,-5,-4,-10,2,5,-4,4,4,2,3,-10,2,-4], dtype = "uint8")#candidate|10938|(864,)|const|uint8
call_10937 = relay.TupleGetItem(func_3992_call(relay.reshape(const_10938.astype('uint8'), [864,])), 1)
call_10939 = relay.TupleGetItem(func_3994_call(relay.reshape(const_10938.astype('uint8'), [864,])), 1)
func_7517_call = mod.get_global_var('func_7517')
func_7519_call = mutated_mod.get_global_var('func_7519')
call_10941 = relay.TupleGetItem(func_7517_call(), 0)
call_10942 = relay.TupleGetItem(func_7519_call(), 0)
uop_10943 = relay.atanh(var_10915.astype('float64')) # shape=(4, 11, 12)
func_10284_call = mod.get_global_var('func_10284')
func_10285_call = mutated_mod.get_global_var('func_10285')
call_10947 = relay.TupleGetItem(func_10284_call(), 1)
call_10948 = relay.TupleGetItem(func_10285_call(), 1)
func_8708_call = mod.get_global_var('func_8708')
func_8710_call = mutated_mod.get_global_var('func_8710')
call_10949 = func_8708_call()
call_10950 = func_8708_call()
bop_10952 = relay.less(call_10949.astype('bool'), relay.reshape(call_10941.astype('bool'), relay.shape_of(call_10949))) # shape=(1, 11, 3)
bop_10955 = relay.less(call_10950.astype('bool'), relay.reshape(call_10942.astype('bool'), relay.shape_of(call_10950))) # shape=(1, 11, 3)
output = relay.Tuple([uop_10934,call_10937,const_10938,uop_10943,call_10947,bop_10952,])
output2 = relay.Tuple([uop_10934,call_10939,const_10938,uop_10943,call_10948,bop_10955,])
func_10960 = relay.Function([var_10914,var_10915,], output)
mod['func_10960'] = func_10960
mod = relay.transform.InferType()(mod)
var_10961 = relay.var("var_10961", dtype = "int16", shape = (4, 11, 12))#candidate|10961|(4, 11, 12)|var|int16
var_10962 = relay.var("var_10962", dtype = "int16", shape = (4, 11, 12))#candidate|10962|(4, 11, 12)|var|int16
output = func_10960(var_10961,var_10962,)
func_10963 = relay.Function([var_10961,var_10962,], output)
mutated_mod['func_10963'] = func_10963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3288_call = mod.get_global_var('func_3288')
func_3289_call = mutated_mod.get_global_var('func_3289')
call_10998 = func_3288_call()
call_10999 = func_3288_call()
func_9131_call = mod.get_global_var('func_9131')
func_9133_call = mutated_mod.get_global_var('func_9133')
const_11010 = relay.const([[3.665234,-2.285776,2.148148,8.805067,3.100714,-4.707489,8.425551,-9.681994,-7.093012,6.650386,6.963279,0.414557,-5.889438,1.236561,1.851839,4.104606,-4.782946,-9.953903,-1.460004,0.176564,-7.086206,6.867066,-3.518681,-5.954166,0.840323,-1.643348,6.865519,-4.970208,-8.901478,0.605291,4.732663,-3.875641,-0.789652,4.516459,-0.644154,-9.395718,-8.203260,-7.493139,5.554479,-0.268647,-6.771699,-0.840980,-9.744468,-2.287478,-8.085352,3.900268,-3.693364,4.265477,-5.033148,5.387849,-0.732637,6.477813,2.087127,9.181553,-1.570367,7.904131,-1.909776,9.739935,-3.569378,-1.443237,9.424817,-4.985479,1.614504,-6.177267,8.264421,8.592462,1.997835,-3.434324,-2.771728,6.800006,8.870970,-8.717788,-5.000262,2.876835,2.735985,3.636642,8.776289,-6.949757,-9.549979,-4.148487,-3.060654,5.792278,8.267550,-7.456881,8.914113,-9.775130,-0.830618,3.230697,-9.519888,5.809168,-4.425249,-4.267766,-2.607758,-5.798260,6.106019,-3.650057,-2.330697,8.751207,-2.391547,-9.115097,-3.632767,-5.309347,4.801004,0.617485,-2.859669,4.496410,-4.843231,-8.752627,-1.823442,4.187715,-4.367519,7.119618,0.534002,-9.684916,-3.297249,3.315738,9.931502,4.360721,1.894229,9.029412,4.641276,-5.636157,-4.984491,-7.210316,-8.174525,9.800895,-6.703452,9.518140,8.828724,3.079157,-0.764516,-8.337524]], dtype = "float32")#candidate|11010|(1, 132)|const|float32
call_11009 = relay.TupleGetItem(func_9131_call(relay.reshape(const_11010.astype('float32'), [132,])), 4)
call_11011 = relay.TupleGetItem(func_9133_call(relay.reshape(const_11010.astype('float32'), [132,])), 4)
uop_11021 = relay.asinh(const_11010.astype('float32')) # shape=(1, 132)
func_3105_call = mod.get_global_var('func_3105')
func_3107_call = mutated_mod.get_global_var('func_3107')
call_11037 = func_3105_call()
call_11038 = func_3105_call()
func_2311_call = mod.get_global_var('func_2311')
func_2313_call = mutated_mod.get_global_var('func_2313')
call_11045 = func_2311_call()
call_11046 = func_2311_call()
bop_11055 = relay.logical_and(uop_11021.astype('bool'), relay.reshape(const_11010.astype('bool'), relay.shape_of(uop_11021))) # shape=(1, 132)
output = relay.Tuple([call_10998,call_11009,call_11037,call_11045,bop_11055,])
output2 = relay.Tuple([call_10999,call_11011,call_11038,call_11046,bop_11055,])
func_11062 = relay.Function([], output)
mod['func_11062'] = func_11062
mod = relay.transform.InferType()(mod)
mutated_mod['func_11062'] = func_11062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11062_call = mutated_mod.get_global_var('func_11062')
call_11063 = func_11062_call()
output = call_11063
func_11064 = relay.Function([], output)
mutated_mod['func_11064'] = func_11064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7821_call = mod.get_global_var('func_7821')
func_7822_call = mutated_mod.get_global_var('func_7822')
call_11143 = func_7821_call()
call_11144 = func_7821_call()
output = call_11143
output2 = call_11144
func_11157 = relay.Function([], output)
mod['func_11157'] = func_11157
mod = relay.transform.InferType()(mod)
output = func_11157()
func_11158 = relay.Function([], output)
mutated_mod['func_11158'] = func_11158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4254_call = mod.get_global_var('func_4254')
func_4255_call = mutated_mod.get_global_var('func_4255')
call_11173 = func_4254_call()
call_11174 = func_4254_call()
output = relay.Tuple([call_11173,])
output2 = relay.Tuple([call_11174,])
func_11181 = relay.Function([], output)
mod['func_11181'] = func_11181
mod = relay.transform.InferType()(mod)
mutated_mod['func_11181'] = func_11181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11181_call = mutated_mod.get_global_var('func_11181')
call_11182 = func_11181_call()
output = call_11182
func_11183 = relay.Function([], output)
mutated_mod['func_11183'] = func_11183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5537_call = mod.get_global_var('func_5537')
func_5538_call = mutated_mod.get_global_var('func_5538')
call_11184 = relay.TupleGetItem(func_5537_call(), 2)
call_11185 = relay.TupleGetItem(func_5538_call(), 2)
output = relay.Tuple([call_11184,])
output2 = relay.Tuple([call_11185,])
func_11191 = relay.Function([], output)
mod['func_11191'] = func_11191
mod = relay.transform.InferType()(mod)
mutated_mod['func_11191'] = func_11191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11191_call = mutated_mod.get_global_var('func_11191')
call_11192 = func_11191_call()
output = call_11192
func_11193 = relay.Function([], output)
mutated_mod['func_11193'] = func_11193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2114_call = mod.get_global_var('func_2114')
func_2115_call = mutated_mod.get_global_var('func_2115')
call_11194 = func_2114_call()
call_11195 = func_2114_call()
func_8571_call = mod.get_global_var('func_8571')
func_8573_call = mutated_mod.get_global_var('func_8573')
call_11225 = relay.TupleGetItem(func_8571_call(), 0)
call_11226 = relay.TupleGetItem(func_8573_call(), 0)
func_5783_call = mod.get_global_var('func_5783')
func_5785_call = mutated_mod.get_global_var('func_5785')
call_11230 = func_5783_call()
call_11231 = func_5783_call()
output = relay.Tuple([call_11194,call_11225,call_11230,])
output2 = relay.Tuple([call_11195,call_11226,call_11231,])
func_11232 = relay.Function([], output)
mod['func_11232'] = func_11232
mod = relay.transform.InferType()(mod)
output = func_11232()
func_11233 = relay.Function([], output)
mutated_mod['func_11233'] = func_11233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6718_call = mod.get_global_var('func_6718')
func_6720_call = mutated_mod.get_global_var('func_6720')
call_11260 = relay.TupleGetItem(func_6718_call(), 3)
call_11261 = relay.TupleGetItem(func_6720_call(), 3)
func_8662_call = mod.get_global_var('func_8662')
func_8664_call = mutated_mod.get_global_var('func_8664')
const_11324 = relay.const([5.819192,-3.807199,-9.485770,6.187171,-7.191054,-0.245402,2.995641,2.211548,-3.349038,-8.275091,3.048890,6.641206,-0.509735,5.666815,1.994243,8.400619,-4.174853,-7.164376,9.709931,9.893268,-0.271214,-7.893589,5.850827,2.264223,-0.793147,-3.747624,8.334671,-1.621223,4.996588,1.028425,6.248932,-6.216231,-0.458651,-9.738908,-6.478184,6.334802,-0.900449,7.127178,5.901633,8.595658,-1.471373,9.430719,7.826944,2.135209,-8.199033,3.518286,3.696462,2.024504,-2.668285,-1.392271,-9.972780,-4.300836,1.448867,-0.290907,-9.395424,-7.066352,-1.093233,-5.805028,8.336295,-7.478450,2.100897,1.279680,5.996385,-4.998936,3.870420,4.389907,9.924412,-3.155726,2.379379,1.258901,-8.666034,-5.994208,-0.902158,-9.683875,9.325801,6.399291,-8.200636,0.349813,3.694826,5.805196,-1.648030,-5.070483,-2.170675,-2.854804,-0.043159,9.854971,8.529928,3.170401,7.188399,-8.483438,-4.700235,9.791416,-3.009535,7.994169,-4.711823,-2.941022,2.285133,-6.037299,3.680633,1.395244,7.289807,-4.252582,-8.015895,-2.294437,2.668104,-0.751510,-2.020569,-5.306745,6.033436,-9.128789,0.019508,-5.871718,-3.131822,-7.249612,-0.639477,2.649893,3.060906,-4.527200,8.304131,8.655275,8.381887,-2.205462,9.687804,4.815336,-3.543809,-5.720927,-6.163294,-9.646957,-0.293880,5.761170,-3.872957,-3.493708,-2.140753,-7.663791,2.778515,7.596136,8.268820,-1.034928,-7.006169,2.426060,5.613189,-6.546488,4.107536,-0.010242,-4.237808,-0.763269,-2.184509,-0.948179,1.011516,-8.573672,-5.556161,-3.610008,-0.260986,-0.461523,-9.363395,3.472031,6.145980,6.752614,1.869807,-8.841451,2.380393,-9.115014,7.626070,3.178865,5.121943,2.180941,2.594368,-8.059717,-6.129183,-3.943847,-2.612261,9.252165,-6.156602,-0.521134,-1.181233,9.566581,0.671084,-5.737194,-6.791317,-7.756120,3.700504,8.430344,5.041439,-3.460549,-3.200182,-4.862605,3.273993,-8.633608,-6.604895,6.929367,-1.647529,9.361260,-3.385255,-2.766307,8.472114,4.382925,4.059156,6.270542,-2.289955,-3.543565,-9.224528,3.097171,-2.445611,7.202012,8.334085,-4.981556,8.928308,5.951639,1.131020,-3.200732,-5.980072,6.250006,-1.216370,-6.527888,3.387873,9.224254,2.648408,5.660311,2.922912,3.973786,6.034970,-1.245844,7.592473,-6.761331,2.156978,2.050245,-4.139994,7.788182,0.857844,2.517140,7.505506,-4.846424,-3.805607,-4.423233,4.599443,-2.706272,0.970572,9.541622,-4.633691,9.519962,4.727333,-2.927892,-3.761589,-9.840478,3.610640,-4.522240,0.139739,-8.693841,-7.550246,3.456986,-8.443010,-7.497189,-9.356498,-9.327942,1.136891,-8.602820,-8.031053,8.877523,4.101747,-9.240122,6.513829,3.127563,7.216698,-4.459743,-6.093088,4.588633,6.738855,3.529552,-6.193116,1.907098,3.866567,-4.636755,-4.632975,-7.207381,2.517989,-0.187538,0.811036,1.571841,4.565714,-4.503008,7.941990,-3.055275,0.412416,-6.623628,9.394455,-5.303708,-0.037689,-0.220390,-1.539759,-4.895399,0.454985,-9.119651,-7.304001,-6.162779,-1.014244,8.937929,-1.886652,-1.981437,7.580832,8.711727,-7.854818,-3.591515,-6.031924,3.003797,9.732712,5.228626,1.361557,-6.701781,8.207233,7.179740,0.921301,-0.103044,2.941854,-6.052291,6.002158,0.423874,7.985910,-6.909174,2.988802,-3.117195,3.320276,3.477143,5.663885,-8.639179,-4.207802,-6.300345,6.656362,-5.384659,-7.078164,0.598756,-6.885189,3.683659,-8.981521,-1.987028,-2.938379,6.777705,-4.555035,-1.716772,-8.702835,-6.818890,-2.136518,-2.368240,8.154719,-5.788921,9.314197,-7.230633,7.376756,4.945247,5.543899,9.408625,-9.111683,-5.234724,5.251511,7.871621,5.054756,7.302738,-9.914766,0.628247,-2.347873,0.938697,-7.640845,3.587524,-0.905194,0.025959,-7.977382,3.564751,9.185442,6.727390,-0.889065,-8.998780,2.003366,6.290218,-5.254061,4.140646,7.569472,-7.664848,-4.608501,8.980429,5.696582,3.419687,7.088598,-0.385761,-5.371647,8.982120,-7.587285,-0.464183,0.499558,-1.276319,5.000915,-5.191971,-2.171867,-7.570849,0.393910,7.843719,-1.859347,-3.572220,7.541086,8.642686,7.258543,-1.985815,-1.314812,8.203088,3.090852,0.342290,6.155052,5.357734,9.573364,1.957918,6.734927,1.914473,6.472584,2.919720,-2.477206,-7.419259,6.426412,-8.416382,4.366135,-9.458385,1.882157,4.009064,4.819543,-7.683379,-4.594698,4.751054,8.423517,-5.295249,3.765331,3.100265,-2.825017,4.518077,1.932334,7.630712,8.848334,0.534738,-3.445989,5.902070,8.477621,-6.523333,1.842294,3.101240,-2.580773,7.634309,9.718961,4.109587,-8.344284,4.664457,-7.674456,2.072985,-3.757567,-7.975515,7.114242,8.149053,-9.799832,7.200666,4.811149,-3.431645,-2.988353,7.933311,-7.817663,5.390442,4.232131,-1.816913,6.228315,4.223172,-9.722915,-0.964745,-1.039785,-4.054304,0.114055,-9.626223,-7.126742,-5.194190,9.539429,-0.537148,4.939495,-5.739798,1.386620,-8.367515,-1.972514,-1.464050,-0.979344,8.814720,-6.804050,0.627602,3.097790,5.650757,-7.385581,-8.019390,7.676974,9.489388,-4.949085,-0.215090,1.453917,-3.315692,-2.045701,-3.596085,-0.759924,5.557831,-9.424482,-3.249305,5.586488,1.601845,-1.551156,1.464535,7.916258,-2.027353,-4.470540,2.300997,5.338349,-5.362725,-7.501848,-3.126603,-7.968200,-7.932574,-3.916741,-9.694221,-5.678806,5.340040,3.554485,-4.225585,-7.000101,-0.111509,9.729738,-6.974982,8.563745,6.916147,0.042050,-9.984517,1.003658,-8.581754,-8.854525,1.341977,2.589772,9.804894,8.695771,3.250350,-6.062016,5.636144,5.384729,-2.645333,-2.632485,-8.215266,-3.227812,9.580343,9.745121,3.551619,-1.249453,-5.459429,-6.027106,-9.859153,-1.837166,5.786766,2.558427,-0.632995,-2.044569,4.291914,-7.572258,-6.802375,4.053772,8.579568,-5.632378,-4.777793,2.440700,-0.280461,-9.883509,-8.946436,-1.338023,0.579222,-1.389441,-0.891682,-9.270739,3.645889,6.530661,9.686991,6.234574,-2.231871,-4.512714,-8.457851,4.871598,9.126233,1.452612,-3.341445,5.404183,2.519419,-1.713142,-5.693479,9.610775,3.582171,8.038963,6.872399,3.147781,-5.340721,-5.132724,-2.261399,0.563128,3.692986,2.578821,-8.392680,3.636525,-8.741077,9.398448,9.089726,-2.740849,-9.612507,7.472484,-5.794258,5.459073,-9.020065,5.079989,2.220148,-1.401437,5.905443,7.989217,-5.488033,6.289627,-2.230288,3.078017,5.743686,-2.452844,-3.553860,-3.940860,5.963658,7.708401,3.906651,-7.791007,-1.658151,-8.992536,-4.193840,5.839038,-1.763841,9.202960,-3.018574,-5.076040,-1.099202,4.309789,8.518680,2.494898,0.899028,-2.291276,2.719327,1.701589,-8.317892,6.014263,6.151905,6.340445,6.154565,-1.088666,-6.953347,0.508086,-8.396637,3.148407,-5.948204,-2.627655,7.984552,4.461363,4.672531,-9.241341,-7.711309,-8.248451,4.337567,5.427456,-0.608705,-9.295378,6.298155,7.094406,-5.717076,0.168300,8.794643,-1.266698,-7.504694,4.799875,-8.501245,7.719003,0.271107,3.380041,-9.871689,4.452189,-1.182094,7.522021,2.965214,6.251441,1.814320,2.539652,-9.767140,6.025515,0.770481,-4.987183,7.781605,-5.997952,3.960199,4.399145,-3.189881,-2.963239,-6.518760,-9.325202,-6.323318,8.218335,-3.757558,-7.697479,-3.774389,-7.851087,-9.678136,2.908563,-6.479751,-3.848131,1.208251,8.545617,-5.374961,5.558764,0.825978,6.919024,2.281959,4.108027,5.946154,9.199053,-0.622556,0.158437,-6.135236,-8.887091,-0.844750,3.201464,-5.672207,5.332729,-9.370826,5.613649,0.914886,-2.852566,4.088066,-4.145519,3.788006,-0.256303,7.142046,0.068011,-0.753719,8.784796,-7.164009,7.536392,2.350750,-3.361767,3.168651,-9.071601,-9.176659,2.608667,-2.647036,-9.487375,7.503123,2.812777,-8.001023,9.417943,-1.877109,9.361933,9.074058,0.367812,2.523602,-6.129659,4.936932,2.738397,8.934401,2.824963,0.729385,-1.641073,-1.801050,7.880825,-3.631315,-9.369174,8.690213,8.450632,-8.795726,-3.686936,-5.865189,-6.363964,0.165540,8.043415,-3.766716,-4.027770,-7.526633,8.443259,4.589976,0.028035,6.853540,-3.458432,6.053687,2.833019,3.643180,-4.497604,-6.833672,7.459286,-1.288586,3.444980,-3.877736,-0.580715,-9.052705,1.248431,7.351107,2.246446,-7.936093,9.551959,3.644047,4.019916,-5.428698,7.217484,-5.621651,-8.065707,8.778021,-1.898150,-9.782320,2.468077,-4.889562,-4.702484,9.119325,-4.615077,5.531884,-8.584010,-4.684046,9.962393,8.582244,9.313152,-7.305470,-7.870505,5.122054,5.322844,-0.836903,-0.717658,7.498724,-7.131004,-9.968294,7.042348,-2.889591,0.684500,2.604201,-5.758665,5.493404,7.417674,9.784469,1.548701,-2.237387,-0.070483,8.023420,2.737160,3.510926,-6.259251,-4.495362,-9.996300,0.845701,0.211989,-3.636905,6.790893,8.250442,9.688105,-5.717616,-4.010680,2.809495,8.417450,8.297625,-9.247313,-1.781424,9.895024,-8.245095,-2.798754,0.075489,-0.925595,1.699953,1.382642,-1.812197,3.058255,1.827921,0.611960,8.410115,-7.644618,8.545138,5.020027,0.031317,-8.607893,-2.465300,2.854309,-2.632994,-5.980310,8.240386,6.187418,-6.155508,-1.027103,-5.246256,0.771395,6.258149,-0.089271,-0.656407,-5.856273,-8.081274,1.055153,8.203285,-7.641072,-2.194506,4.759621,-8.524287,-0.391453,-9.371454,3.052370,-2.971283,-0.284722,-3.377332,4.930223,-9.157941,-7.806608,-8.024229,-1.049947,-5.775797,-1.034722,7.748638,-3.191724,-5.481437,-3.566919,5.831472,1.272328,-4.070111,9.816384,-7.341571,4.667643,2.374999,-0.782589,3.807320,1.841110,7.501468,3.355134,-6.025477,2.974004,-0.227897,2.346574,5.089910,7.132987,-4.219624,-1.674063,5.995938,1.809852,4.772871,3.828276,-6.097840,-2.301651,-4.142227,-8.437244,5.272510,1.206298,-3.755877,8.824577,1.785171,1.158899,-6.786134,-4.049861,-1.242755,-3.750387,6.493814,-0.909799,-0.858436,-7.275687,-0.983789,0.320384,-7.335028,4.608973,9.237676,-9.470398,-4.203325,-6.629953,5.560162,-9.327380,5.136440,1.960276,-6.009080,-6.405585,-0.664774,3.005621,-7.009937,-3.101221,1.964705,8.275355,-2.425985,6.167662,8.108574,6.467986,8.317558,-5.433800,-0.513635,4.789405,-7.585911,-4.065262,-6.695913,6.084213,-3.460746,6.392120,-0.966340,8.073644,-3.445370,0.860553,-8.046231,-8.226860,-0.719645,-3.619602,-5.237425,-9.582763,-8.996268,8.868940,-3.192091,8.313207,-9.581842,3.143942,4.039401,-1.760263,4.489999,4.184505,-2.990286,2.098276,3.855232,-6.624855,-0.431467,-8.374196,4.336286,5.079023,-4.401393,-6.626068,-8.159738,3.602403,-8.022139,4.714359,2.413472,-0.118955,3.591884,8.119839,1.988945,-4.838088,-4.736708,-0.200555,2.277055,3.567599,-6.887556,-9.321608,6.492150,-9.118440,5.435350,-5.558733,3.716506,7.253064,-5.671546,0.943016,-1.292957,7.831013,-3.194810,-5.881365,-2.088317,8.083524,5.379634,4.234781,-0.387210,7.243849,0.127453,-1.233762,-1.878715,4.140060,-9.662061,-4.733011,5.860494,9.950751,-3.387322,5.985867,-5.655357,2.936772,-8.913546,-7.203989,8.954155,4.198941,0.293856,0.677664,6.353842,5.106842,9.291822,-1.150308,4.158309,-7.253445,1.042984,-0.909224,-3.491614,4.969665,-9.229320,3.207567,9.689223,8.996706,2.958384,-0.861639,0.434896,-1.079580,-2.595033,5.255681,9.601968,2.542197,5.148303,-1.834383,4.186423,0.022819,3.858461,5.076378,1.193076,-0.638585,4.114918,4.567092,-6.030586,4.703117,-8.347490,-9.368899,-0.066830,-1.288916,-6.077863,-4.749237,-3.774332,9.056643,-9.876486,3.579954,5.644607,-2.538958,-5.500713,-5.059795,-0.165878,8.069810,-8.742343,-3.458775,3.469391,7.339810,6.500305,-1.429151,8.454017,2.360912,-4.859652,1.646496,-6.873515,6.096663,9.192201,8.380701,5.995219,-4.211248,1.896472,7.409068,7.045076,-7.451178,-2.956935,-1.468374,-7.591523,2.599596,-4.982945,1.926537,0.279263,-8.700224,-2.818775,-0.897773,-6.122598,1.912227,5.895745,7.388638,0.201096,0.606096,-0.775333,6.527936,2.713754,6.532021,9.678753,1.532295,0.867817,0.510751,0.212383,-2.250173,-4.332511,2.703642,-8.750511,-9.077318,-6.613454,3.962306,-3.139304,-4.888170,9.214427,5.962622,-0.412345,4.960666,-0.005272,4.935456,-6.549713,-7.949164,4.990806,-4.651324,-8.085825,-1.009752,-9.337912,3.316532,-2.944042,3.888606,7.258009,2.790021,8.586367,-2.977542,3.120839,4.971386,1.676749,0.010885,-0.482346,-0.087292,-8.360824,2.508027,-1.149891,4.958264,-3.414160,-2.534900,-8.164648,4.993555,0.583179,7.545879,4.087185,-0.609683,-6.814539,-4.251379,-9.664025,6.142715,0.278655,7.635115,0.475157,-5.267576,5.305342,-0.126432,-1.338345,2.527711,2.902429,3.343673,-9.715258,3.010768,9.431064,6.668132,-1.839923,-4.557462,7.315012,0.990153,1.331303,1.752653,-1.476651,-7.219378,0.550858,-0.885111,-0.064285,-0.334295,-4.663539,-6.039728,4.573827,2.707484,-4.143716,7.919372,5.119196,5.197639,-1.424724,-9.072274,-1.446464,-2.036918,-5.490477,-4.295457,-0.833886,3.620957,-5.087286,-7.775320,6.294464,4.789179,3.904977,-6.867005,0.447471,9.985195,-7.313284,-7.762591,-9.147628,-6.079537,-9.699822,-3.936649,5.626546,3.093781,3.009896,7.424211,7.665877,-8.898134,2.675913,9.248676,-7.480413,4.746929,-9.580005,4.046018,-0.752031,-3.365751,-2.607843,8.428385,-7.387062,7.316087,-3.672986,6.639332,8.747458,-9.580060,-1.226364,7.141388,7.153579,8.942945,9.441565,-0.417166,-7.008031,-0.166814,3.359561,0.355905,-0.482438,6.402566,0.496513,-2.516794,2.801951,-8.607129,-4.018130,-5.050507,-1.042334,-9.018062,0.135916,5.123850,0.924887,-0.304379,2.041325,-1.379133,8.101759,-3.331285,-7.991880,6.879378,5.007569,9.463950,-1.633191,2.405625,7.367013,-1.346588,4.881627,1.728233,1.229154,2.558894,2.380718,-1.931484,-2.919913,8.045280,6.054067,-1.292943,-4.537337,-3.149431,6.438117,3.518817,2.866956,5.701903,9.928621,5.123814,2.523754,6.178305,9.204773,3.632730,-6.058494,-3.481027,1.962229,5.096205,0.216419,-8.253727,8.933676,4.239896,2.497294,8.904759,1.464995,8.673324,-2.688906,6.751114,-0.977112,7.013664,-2.943873,-1.472440,-8.699454,9.257429,-0.810405,-3.433126,-2.130241,-7.497984,3.191390,-1.255944,5.304193,9.395839,2.026670,1.367001,1.001492,-5.360895,-3.020948,0.748251,-0.695495,-8.697935,7.966187,0.175625,4.348196,8.107127,9.511583,8.112726,-5.382709,-9.597768,-0.268111,5.411884,-7.216556,6.033728,2.994867,7.508547,6.452713,-2.522792,1.983844,-2.258124,7.919945,4.579848,-6.988766,1.123142,4.338399,-1.261646,5.455360,0.042771,5.622958,4.774447,7.374517,7.796419,-9.917887,0.659760,9.273278,-1.444226,-9.815022,4.919425,1.907692,8.447238,4.627055,-8.066187,4.793022,-4.175899,-1.485414,5.378255,2.372479,-2.512979,-6.867629,2.532191,-4.852800,3.749100,3.259659,9.485980,4.738042,3.449987,-3.005594,-8.298459,1.933673,-3.508432,-3.632227,4.067924,-4.804410,8.161596,-7.812430,-3.864404,8.098642,0.436645,1.448608,7.702593,1.970648,6.405577,-5.048294,0.677495,-5.698315,3.268893,-4.096102,-1.041338,-9.896287,8.140334,-6.793880,1.183891,4.917195,-6.391212,4.175068,-6.202841,-7.838732,-4.940305,5.460052,-7.755445,-2.381228,-8.158706,6.739068,4.453798,-5.725553,-7.133235,2.157395,-2.948760,-1.345297,1.951120,-2.318131,-6.990574,8.075062,9.010925,-6.158207,-9.415338,4.987320,7.814772,-6.766402,1.268288,-9.773440,7.573713,3.619041,-3.487989,9.547062,-4.275347,5.711816,-7.690490,8.248090,5.833983,-4.687852,-1.775670,-5.701222,-5.512282,0.759961,-5.264216,6.975193,3.096843,1.718864,-0.865626,7.612355,9.751904,0.059725,1.371237,4.897461,-8.355094,-3.153374,-2.593182,5.576549,9.849089,-6.284911,-3.944050,-4.568983,-9.669973,5.583316,-1.570192,5.658052,-4.442073,3.774238,-8.813935,-0.312401,-7.261340,8.824496,-7.322907,8.659798,1.434408,2.080499,4.440800,6.074184,4.643232,-3.795812,0.338527,7.682395,-7.433518,7.907030,-5.578140,-0.606554,3.823491,4.138982,-9.694247,8.385347,-5.448806,5.772528,-4.742912,7.894545,9.269106,0.603086,-5.574056,-6.413597,-4.125475,1.466452,-0.924074,1.292017,1.608389,2.319748,-8.102645,-3.098819,2.921722,-5.590559,-6.358779,0.634690,-0.443660,1.068063,-3.566342,4.548417,1.852932,6.397135,-7.563608,2.807383,2.101537,7.505941,-0.015658,-6.128142,3.017936,2.187790,-4.127318,-1.914093,-6.628022,6.153234,8.652773,0.890833,9.033572,-2.047223,2.714997,-4.386728], dtype = "float64")#candidate|11324|(1600,)|const|float64
call_11323 = relay.TupleGetItem(func_8662_call(relay.reshape(const_11324.astype('float64'), [1600,])), 5)
call_11325 = relay.TupleGetItem(func_8664_call(relay.reshape(const_11324.astype('float64'), [1600,])), 5)
func_3686_call = mod.get_global_var('func_3686')
func_3687_call = mutated_mod.get_global_var('func_3687')
call_11326 = func_3686_call()
call_11327 = func_3686_call()
func_3361_call = mod.get_global_var('func_3361')
func_3363_call = mutated_mod.get_global_var('func_3363')
const_11334 = relay.const([-2,-10,-4,-9,8,9,1,2,10,8,3,-3,-1,2,1,1,6,-2,-2,1,8,-1,-6,1,-8,-5,-8,-7,3,-10,5,-6,5,-1,10,8,-4,6,-3,-7,7,-3,10,3,7,6,5,3,1,-6,8,6,2,-1,1,5,1,5,5,-3,-9,6,-2,-3,-7,-3,-4,6,-2,-2,-6,-3,4,8,-5,-4,1,-10,3,7,6,-2,8,-8,-6,5,7,10,-7,-1,-9,-9,-8,-7,-2,-8,2,-1,-1,-3,9,-2,-6,-8,-1,5,5,-2,3,-2,4,5,4,-8,-5,4,9,-10,6,-9,-8,-9,-10,-4,2,10,-9,-2,3,8,3,1,7,8,-3,2,-5,2,4,8,3,-10,5,5,-3,3,6,7,-9,-7,-4,-2,2,4,-2,-9,-2,-9,-2,2,-9,3,-1,9,9,-10,6,4,8,3,-10,-6,3,7,8,-5,4,-2,-10,5,-6,-2,1,-2,4,8,8,-6,7,-8,-5,-4,1,-6,-7,-10,-9,7,8,8,5,-6,10,-5,5,4,8,-1,-5,10,1,5,4,-10,1,2,6,8,10,-2,7,-7,5,-4,8,-2,-5,8,1,10,8,10,10,9,-1,4,-1,3,-10,8,-4,-6,-7,8,4,2,2,7,9,-3,-9,10,-10,7,3,-10,6,-6,2,-3,-4,8,8,-9,1,1,2,3,-6,4,6,6,1,6,-6,10,5,-5,5,-4,-7,-8,8,-3,-2,6,2,-9,-4,6,4,-7,4,-6,7,5,6,-4,-7,-9,-3,-6,-6,8,9,-9,2,4,7,6,1,-9,7,9,10,4,4,-8,4,-10,2,8,3,-9,-3,6,6,-8,9,-8,9,2,-1,-2,6,2,9,-1,1,7,-7,-7,-10,-10,6,10,2,-7,-2,-10,10,8,1,6,-1,7,7,3,-2,-8,10,4,-10,7,-1,-10,-8,-4,8,-2,-4,9,4,9,-4,4,5,-8,-8,-4,-1,-2,3,-9,-6,7,9,-1,7,-8,-1,9,-10,-10,3,9,-10,-4,-7,-1,-3,4,6,6,7,8,-4,-3,-3,3,9,-9,-3,4,-5,4,5,1,-5,-9,-9,-10,4,-9,8,-3,6,-10,7,10,8,10,-3,-7,8,-1,-2,3,-6,-3,4,3,-9,10,6,-10,5,-10,-2,5,4,8,6,-10,-4,9,10,-10,7,-7,-2,-7,-6,5,5,-10,7,5,-9,-8,-9,-3,-10,-1,2,8,-4,3,6,-10,10,-10,-5,-4,1,9,8,-2,-2,-5,-1,-2,-2,7,-3,-8,4,-3,4,-7,-9,8,6,-8,-3,7,-6,8,-4,-3,-1,-1,1,-6,-1,-10,9,8,8,-4,-6,4,9,-9,7,9,7,5,-6,-10,3,-5,-10,8,6,-10,2,-6,5,4,-1,2,-5,-3,7,5,-7,-4,3,8,3,-6,1,-8,9,-8,6,-8,4,-9,-7,3,-7,1,-9,3,-7,9,-1,4,-10,2,-4,-5,2,-1,10,-10,-9,1,2,-9,5,8,-6,7,7,-2,-8,9,-4,-6,4,-3,1,-10,10,-5,-9,10,-5,3,-6,3,3,3,-4,-4,-9,1,3,-6,-3,7,-3,-9,-5,10,-9,-7,-7,-2,1,9,-2,-1,-4,-9,7,-10,6,1,-4,-5,6,-5,-2,3,-2,-5,-5,-1,-5,-5,-6,-5,8,4,-8,5,10,-8,9,-8,-6,-7,-1,-9,9,-1,2,-7,-3,-10,-3,7,-5,8,10,6,10,8,-10,-8,-2,-5,-4,-3,-5,-9,10,-2,3,-10,5,-1,-9,-6,8,9,-4,4,-7,6,2,2,1,8,3,9,5,-5,-10,5,-7,-8,7,1,-9,-7,10,4,3,-9,3,6,-9,4,4,-7,-4,-3,7,6,-9,-8,2,4,7,2,1,-9,1,-10,-3,-9,2,-7,-6,-4,5,7,5,3,-5,1,4,-6,3,1,5,-4,-2,5,-5,-2,-2,-10,-8,-10,-7,-9,-10,6,-3,1,7,-4,-8,4,1,-4,4,-1,-6,-7,1,-3,-3,6,6,-5,-5,-1,-9,6,2,4,-5,-8,5,5,-3,6,-7,-3,2,-7,6,-9,4,6,7,-2,4,-5,-7,-2,-9,6,1,-1,5,9,8,6,-5,-8,2,-7,1,-5,2,-9,-6,-1,4,7,1,-3,-3,-3,-3,3,4,-2,-1,3,4,6,-7,-6,-8,2,-8,2,-4,-2,-7,-2,4,-6,-3,-10,-9,7,-5,6,-6,5,-5,-7,-2,-6], dtype = "uint8")#candidate|11334|(864,)|const|uint8
call_11333 = relay.TupleGetItem(func_3361_call(relay.reshape(const_11334.astype('uint8'), [864,])), 5)
call_11335 = relay.TupleGetItem(func_3363_call(relay.reshape(const_11334.astype('uint8'), [864,])), 5)
func_3909_call = mod.get_global_var('func_3909')
func_3911_call = mutated_mod.get_global_var('func_3911')
call_11346 = relay.TupleGetItem(func_3909_call(), 0)
call_11347 = relay.TupleGetItem(func_3911_call(), 0)
const_11356 = relay.const([-8.492758,-0.437398,-2.839760,6.123156,5.687299,-3.310496,-0.731640,5.187370,-1.389615,-5.470303,1.141461,2.201225,-1.812515,4.991979,-8.183354,-5.286040,-3.970353,-9.388262,9.475736,4.750458,-8.282384,5.150865,8.660897,6.419950,-5.257784,-9.445668,2.068690,-3.806001,2.784732,5.484484,9.054024,8.522971,-5.002537,-3.832741,9.799928,6.290305,9.928295,-6.173315,9.125075,-6.404185,-0.712731,3.878207,-9.149665,2.865721,-4.255796,-8.519290,3.082417,6.362246,4.784794,2.482231,-4.953338,-5.938540,2.499280,-9.275025,-0.333808,-7.986908,3.744713,0.541424,-1.805544,4.015894,7.228173,-9.988131,4.419911,6.463858,2.889400,-9.717214,6.013874,2.890687,9.552089,4.485366,-1.470136,-6.508815,-7.717523,2.470920,9.248850,2.929884,-8.453821,5.605000,4.277445,7.125075,5.869212,-2.248632,-6.030849,8.805218,1.284928,-1.953638,1.519326,3.018062,-8.605448,-9.456229,-2.931171,-7.491978,0.814984,-2.780680,-2.991253,2.030988,4.664015,-6.578562,3.836167,-4.660405,7.009791,-6.856939,5.666150,-0.060263,-8.749848,3.486651,-3.281004,-7.123012,6.435150,-4.583767,-9.715357,3.231729,-5.235215,9.140921,-3.678576,-3.742233,-8.548351,-0.942080,8.653675,7.775819,6.563038,-9.768905,8.985634,3.768778,2.235649,-8.360825,7.360530,-5.811272,-4.674320,7.575451,9.965052,-9.182663,-5.653843,4.458413,9.123679,5.241595,-3.478198,-5.212638,-4.473293,-8.760527,5.521397,0.423594,7.468636,-4.886455,-2.409651,-0.697657,-8.777809,7.145737,5.733180,-6.853169,-8.376268,8.203115,7.718400,-0.143640,2.067765,4.691197,7.394374,1.614441,-6.565349,-5.972798,7.407409,-4.452897,2.521691,-4.074640,7.527188,1.056048,-5.877165,-0.298332,-8.004037,-7.699584,3.980923,9.457631,-0.716912,1.860656,-4.848878,6.605643,-7.233101,8.711993,-4.655345,-2.773532,-6.328184,2.690028,-7.889688,-5.037493,-4.090487,-5.193603,5.006169,-3.818191,-1.105017,-1.984863,-9.294122,-6.173792,-7.735519,-2.207799,9.534496,-6.289089,6.559722,5.234554,7.838043,-4.390248,-1.310584,5.131629,-0.324456,0.863383,-8.439044,-0.359636,-1.337306,9.920535,-8.313376,5.969622,3.993472,-2.553452,5.812206,-5.909160,3.816778,-7.790039,-6.870548,1.448036,1.341378,8.689455,5.793254,-5.250122,0.238239,-2.482880,-8.772788,7.588621,7.578415,-2.411728,9.837651,6.429228,2.914289,-3.561286,8.659904,1.477331,7.259975,-9.137388,-5.385847,-0.243976,9.141789,8.750166,-4.663203,5.568838,-0.913008,-4.979908,-1.983210,5.821875,2.979150,7.429967,3.287714,2.847571,-7.147806,2.778699,4.278804,-0.318715,-8.484428,-8.917252,-3.722147,-4.906109,4.813920,3.100192,-3.727066,8.518759,-4.592306,1.221723,0.924361,-1.636075,-9.150943,-3.095186,7.714317,-1.046622,6.466788,-1.369790,-0.168239,-6.660513,1.537108,-9.260554,-1.326989,9.008995,-1.016710,4.461679,-7.113174,0.346693,1.266508,-4.221356,-7.165179,0.012584,7.083983,-6.774408,-7.111789,4.103058,-7.214657,-8.013977,0.022363,5.819303,-7.933310,-9.852212,7.757503,3.179646,3.279451,8.793903,9.297323,6.680239,2.073523,-1.744853,8.740719,7.271834,2.785862,-0.619272,-9.302616,8.279600,-2.755192,8.740243,7.271130,4.078185,-4.689590,2.002088,0.111474,-9.554603,-2.214117,-6.162436,-5.804602,0.404965,0.547727,-1.384237,3.643838,-4.747959,7.705179,9.305332,7.995068,-5.813252,-4.386433,2.752306,-1.830651,-3.559862,-2.600397,-4.339279,-6.013502,9.842525,-5.202235,2.860214,6.801655,8.277313,2.375314,8.497024,1.137936,-8.829466,4.121564,6.859241,4.326307,-4.778697,5.310448,-1.825650,-3.430901,8.526186,-6.185606,5.985546,4.193799,-1.777224,4.371951,4.887593,1.710666,-6.471263,4.908540,6.162953,6.205759,-4.782336,-3.184037,5.891137,-1.518422,7.472385,8.463522,-9.610589,-9.706978,-1.507586,3.983798,-1.133078,0.045925,8.697934,3.561113,-2.227938,6.614013,4.863011,9.217528,-1.201112,9.358458,-1.227585,-2.705752,5.917498,-3.667054,7.090400,9.272039,-1.464851,-4.217051,5.243795,-9.610994,0.305764,2.505784,-1.411514,4.402170,-4.253698,-5.841985,4.956655,-9.844966,0.842263,-2.394364,-6.995114,7.724707,5.116186,-1.554214,2.532940,-9.440263,-2.608729,0.030411,-0.640840,-7.081359,9.586109,-1.665741,0.034303,-6.214380,3.331408,0.658171,-6.948273,-8.426829,7.557679,0.879486,-2.702292,8.133289,0.212033,8.600005,9.003772,-5.676345,-7.979398,0.822038,8.338222,1.186704,4.269530,-4.108592,7.868421,8.409208,-6.351363,3.888542,-2.904887,3.153693,0.601100,3.749745,-3.158277,8.898985,-0.393207,2.888592,-1.061397,-6.332989,2.947735,-3.631716,-4.384032,0.178270,-5.372420,3.980390,2.291120,-9.096466,6.104412,6.220521,8.175363,-3.896184,-9.077613,-7.097709,-1.721303,-1.489853,4.315513,-7.546163,-4.473368,-3.798396,-2.573917,0.409583,3.916460,-1.104126,4.043651,-0.313153,6.963169,9.974443,-3.625937,-3.140967,-4.177741,8.281466,4.866211,4.710249,8.967726,-9.506309,9.755550,-1.987315,6.927861,3.050081,-3.415674,-8.446972,5.644399,3.683409,6.971412,-7.054054,-6.502138,2.741207,-4.061555,9.821321,6.542465,2.870520,5.155780,4.771617,2.282904,-6.361450,-3.637277,8.575335,-1.186899,-6.699702,-7.692661,1.935517,-4.037663,4.140183,-8.140877,-6.477334,-9.634043,-8.616783,6.081867,0.288622,2.897628,6.088922,-3.485943,7.624744,3.162406,-1.628868,-7.966586,1.452107,-5.722701,2.830095,7.492004,-3.866466,-4.051180,-4.921043,-5.754256,-3.529233,8.386343,-8.423450,-7.677338,-5.425550,2.261589,8.559430,-3.194092,-2.111865,6.998361,5.967966,9.063064,3.276966,9.773203,-3.029286,5.276457,7.164156,-8.420656,-8.594028,0.994508,-5.618464,7.864158,-6.649370,-7.395993,-1.122431,7.310632,7.513777,-7.394820,-1.182123,-9.533932,5.440928,0.781131,-2.638175,-8.007370,-2.982194,6.746179,-6.966176,-5.311382,-8.727786,2.982040,2.649192,8.928006,-0.791826,0.632024,1.697788,0.078418,2.923748,2.616596,-3.597547,-0.051023,7.304606,8.628388,-7.015518,-3.099220,1.435385,9.817633,-7.363229,4.478178,-7.714905,0.646912,-2.278953,8.652344,8.808249,9.631611,-7.822814,-7.199182,6.805607,-8.410892,-0.701087,-6.888151,-9.951463,-8.779261,-8.588436,3.698105,-5.724183,-3.709254,6.624016,-0.026938,-5.642323,-0.413505,4.636574,-2.835530,2.333160,-9.150023,-1.587086,3.174044,-4.663587,0.034097,5.374578,-5.574821,-9.674857,-0.326000,-1.180992,-8.496328,-5.192331,6.658480,-4.762140,-7.103224,-7.186402,8.605968,4.091502,-1.201250,-9.796395,9.221597,-8.359231,1.116939,-2.654848,2.159241,-6.410391,-1.970675,-8.768401,-1.232252,0.661962,-6.820063,6.305017,-8.444407,-3.712139,-2.470599,8.698656,-5.587137,4.407460,-4.300023,4.291196,-2.274474,2.353645,-4.348199,7.889817,-7.457080,7.248734,-4.674688,-7.277330,-3.841847,8.096913,9.318088,-3.034163,0.645564,5.317557,6.106155,5.688948,-4.382989,-7.326417,-8.058683,1.330460,6.440876,-6.646676,7.943619,-2.459123,5.250733,1.802505,-3.210396,0.373484,4.926881,3.307950,7.985180,0.966389,-0.549304,2.093776,3.112654,7.646886,1.562238,-9.270611,2.024564,-4.226445,7.966818,5.276511,4.543032,9.177792,-1.476235,-0.524567,8.563153,3.359805,4.119606,-6.314732,-4.644150,0.486078,0.946826,-8.501646,1.156978,-1.722781,-6.743893,-3.911413,-1.334528,6.242897,7.401997,-4.078392,4.137240,-8.520799,-9.221090,4.830354,-4.114814,7.831510,-0.120875,-0.205609,-7.237130,-7.369291,2.794688,7.212297,-7.710158,-6.569497,-6.021134,-7.227912,-8.167904,-0.699651,-2.961565,7.189635,1.055565,-8.352848,7.264644,9.301312,1.462224,-7.346564,-0.402017,-5.718916,-8.344581,-5.598598,-8.948900,-5.840035,0.924518,9.826069,-7.693843,2.977745,4.087736,-6.089361,-4.330089,5.039176,7.756868,-6.736057,4.081635,4.418930,5.234646,-7.796969,-4.725489,9.950300,5.783327,0.776126,2.658538,5.932085,3.651275,1.433872,9.524435,3.617683,5.027454,4.935505,1.537696,-7.846187,-0.158367,-5.268951,-1.185948,9.569447,-9.781017,0.114498,2.381636,5.662892,-0.923524,-3.043134,3.987876,6.542870,-5.310379,7.391440,6.329039,-9.028520,-6.037844,-1.043643,-0.220938,-3.433797,1.401574,7.844081,4.234709,9.246255,0.810159,8.850422,9.836359,5.135209,9.569345,1.798585,5.935618,5.696052,-9.821267,-1.839624,0.880460,-8.810961,-9.471465,6.640996,-9.504545,-4.079170,-6.602705,-3.378509,-7.550188,7.476234,-0.414619,-9.904269,4.109553,8.542603,8.185299,-3.792430,-5.330302,1.592325,-6.275830,-4.692996,4.711541,3.433222,2.603469,-7.457210,3.516934,1.335929,-5.234905,8.351517,9.411211,-8.099543,-3.169013,1.539343,7.372884,-8.441192,7.316957,-4.258589,6.668547,7.414910,2.884823,-8.765724,2.955252,-5.670606,0.821603,0.870211,-8.262099,3.564389,1.850453,8.433578,-2.427243,-0.324992,9.152098,-9.823149,-0.137999,5.972257,1.837527,9.485244,5.332334,0.241617,0.930926,-6.454601,-2.127363,6.827769,-9.996042,-0.372850,-5.318739,6.989658,7.066317,-4.283772,0.449370,6.083018,9.339155,6.078477,-1.268113,3.894988,-8.919159,4.925173,2.182695,-2.951869,9.421116,-5.166061,1.056336,9.542080,-3.359178,8.488423,6.439362,-5.056790,8.124364,-5.547033,-5.307615,9.462583,5.378122,4.854826,1.490019,-6.104056,-1.070416,-5.674665,-1.265659,-1.132565,3.437986,-4.766989,-1.660039,7.485813,3.391800,5.604761,8.315420,-1.243868,8.240517,-1.787800,0.673106,-5.679080,1.154580,6.329218,-7.456032,-3.687122,1.287113,3.707783,-0.438218,4.417022,-2.790636,9.195524,-9.710553,-4.624131,-6.508214,-1.435929,4.648946,1.715866,-8.367263,1.674133,6.466363,-0.751582,-3.691605,-3.821957,4.889366,-5.032627,9.681430,8.116191,6.814144,2.265730,-7.287332,0.189299,-3.465976,8.167868,-5.971193,-2.405329,-9.591903,-5.819176,-7.540856,2.935343,8.533347,1.043390,-8.882229,-9.888745,-1.832916,7.579778,7.370777,-1.246660,4.701422,-5.462393,-2.284929,6.434761,-0.718423,-7.177815,9.057990,-4.277292,8.290814,6.596595,-6.223512,-2.735809,5.235518,-9.904350,-5.806729,2.886347,-3.737153,8.018025,-1.930693,5.459724,7.181620,5.368826,-6.084741,5.787800,1.248943,3.699490,-2.958210,-6.752614,3.507481,-7.667448,5.382530,8.204183,-6.036061,8.842277,-0.240985,7.277729,-0.725449,-1.768002,-9.326534,-2.343706,-2.420284,5.537246,2.988838,-6.635193,-8.209654,0.742308,-5.350543,6.163184,6.663496,0.035528,-3.389439,7.352671,4.881892,9.366034,4.460011,0.551535,0.646911,-4.145330,-8.310422,8.862308,-1.984776,5.200418,3.708237,6.683807,4.707118,-0.264816,1.231292,-9.345480,0.182928,-2.775802,3.971909,-5.107466,-7.364469,-2.874820,-4.042167,-7.461082,-0.403566,0.567353,-3.302851,-0.552405,-6.428015,6.509092,9.445845,-7.501321,3.719103,8.697426,7.603950,7.905362,9.908749,-4.984487,4.291425,-6.404059,-1.284045,-5.859219,-9.094734,-9.600994,5.169879,-3.832668,3.033397,-9.993932,2.267190,-8.821615,0.063357,-6.453978,9.316493,-7.854735,3.716217,-0.397525,5.130812,6.666443,7.316006,-4.393897,0.864519,6.752313,6.409787,-2.716482,-3.522431,2.016837,-7.985788,-3.566845,4.685180,6.784979,2.887056,-3.554664,-4.844902,-1.775320,-5.593834,-9.228170,9.231035,-7.323110,9.448216,8.106116,1.109958,-0.551776,-4.866390,7.673490,8.660519,8.713269,-7.109831,4.958589,7.231102,7.229631,-6.798284,0.935061,0.003549,4.701011,-8.806830,-8.813297,2.506308,-0.992364,2.553484,1.292676,-5.824081,9.427698,3.914298,5.010361,-1.230136,-0.583221,-0.607338,-7.444380,9.119191,8.079553,-8.959682,-6.267484,-2.190552,-9.458788,-1.991465,-6.491982,-1.986425,-3.678151,9.471863,-7.767957,-5.494556,-3.731626,-4.639599,-3.797663,-9.145191,-7.898090,-2.386120,6.749711,7.341987,-0.446589,6.875506,-3.825517,0.904200,2.492650,-7.091301,-3.362064,-4.446660,0.643885,-5.258620,9.463184,0.939990,6.686220,-2.112488,-2.613293,-0.752174,1.809578,-0.083182,8.672696,-1.593504,-7.480289,-4.063266,9.540122,6.313930,-3.886725,0.587864,6.726215,3.840193,-7.049992,7.001208,8.444040,0.346292,5.811099,-2.641285,4.933088,-0.902940,4.404772,8.172123,3.853075,2.591977,-6.833554,9.131233,-4.651749,-8.135141,-2.927699,5.962665,-5.483757,5.596268,-7.369814,-2.586810,-7.019241,7.438765,-3.802692,6.777430,-0.127404,7.456416,0.397476,-5.488315,1.139026,-3.261579,-1.589207,7.550427,-6.607563,-8.023863,-4.722104,4.075177,4.652507,-4.521581,2.264551,-7.524189,-0.160327,-8.684932,-0.060982,2.386209,7.027939,-1.458772,-9.360312,-8.938738,-4.385568,3.654172,-7.193712,4.283464,-5.035533,8.648414,8.329762,4.152453,5.024973,2.332488,-1.079820,0.843171,-4.664303,6.249223,0.084043,-2.765418,-0.411562,-4.057889,-6.161663,4.854751,7.574722,-6.872355,-5.345403,-6.228389,0.420465,2.853002,6.000892,2.516352,-3.546455,-8.216318,7.473864,1.865816,-4.749543,-8.616852,-0.214505,5.146059,-9.529628,-7.951317,5.473218,-6.858558,5.884357,-3.993069,-9.573950,-0.214278,-9.208847,-4.363558,4.906777,-8.955502,8.616366,-0.848795,-5.223079,7.260971,3.683242,7.737116,-0.296676,5.194322,8.901388,-4.197592,-2.467560,1.094525,8.079217,-8.732102,2.923365,1.587239,4.223624,-9.807023,2.454856,-4.302123,-8.168861,-9.137344,7.767257,-6.191480,0.106080,-2.568686,9.642399,1.071875,2.982222,-4.998100,-0.015627,7.741236,3.704452,9.874196,5.951441,-4.324850,6.870190,-0.494454,-2.347691,5.033817,-1.164391,0.317050,3.688736,-9.222205,-5.810776,-9.128849,-6.876463,-8.828534,7.646202,8.040998,4.051918,-4.425172,-4.509923,6.975596,7.043928,-1.624012,-3.137966,-1.116385,-8.004852,-0.692139,6.739454,6.461764,-2.574596,9.961854,6.796001,-2.982743,-4.962496,0.385966,-5.105791,-1.629016,-8.246078,1.951430,-4.903306,-0.253045,-4.498961,-1.649856,2.002687,-8.350472,9.246613,-6.326081,-6.385977,-1.184899,0.677161,8.844691,-0.667839,-5.794896,-2.493078,-8.685031,0.064786,-1.503319,6.506346,8.983737,-4.474417,3.880691,5.560403,2.755739,-0.963774,7.096870,9.354078,8.224556,-1.710794,-7.012615,6.104726,5.038440,-1.030140,9.258969,-8.622035,-9.943049,-8.773266,9.991088,6.827847,7.011791,-9.267866,-7.622880,3.831733,1.563097,7.497500,-8.165129,-4.275701,5.653063,1.121495,3.240514,3.062088,7.869388,5.099980,3.774649,8.446456,-7.612115,0.141794,6.888212,9.940982,-7.814445,3.788262,1.287903,6.053625,-2.343280,1.349845,-4.642978,1.249550,-0.145812,-5.362503,-0.728558,-9.799154,4.362375,1.794164,-2.065252,-3.026896,9.917165,-7.436791,0.682627,6.255450,-4.024831,4.332342,4.087783,-1.761172,4.414890,5.808033,-2.064996,8.739503,-7.638589,7.858009,0.890605,3.946372,5.470549,8.578171,7.935716,-4.484005,-3.933759,2.381163,-5.311545,5.528806,-1.329724,1.553128,4.783671,3.680762,8.100192,-9.543299,-8.668753,4.098319,9.598453,-0.520994,8.109651,5.074191,2.885099,4.428773,-4.030050,0.124656,-6.916029,-2.305752,6.337205,4.540495,-0.434245,3.419428,3.419975,-5.218037,-5.023889,-1.552370,5.735231,7.486008,-5.278044,-9.302023,9.643013,3.060949,5.879049,8.024167,1.862240,5.766632,6.498415,-4.307898,-8.639690,2.964744,-3.141776,-7.240431,7.512479,-6.001223,6.834729,4.969865,-4.601402,-9.126542,-2.523692,1.029102,-1.859990,1.768756,4.885324,-2.189811,-3.961636,-6.674947,2.419310,-1.155203,-8.034119,-3.865607,7.416259,0.064230,3.983126,6.183223,6.287500,4.261900,-1.346761,4.284785,5.206171,5.886851,-7.466122,-1.171201,-9.476651,-2.950740,0.292409,-9.164248,-9.176909,-3.871501,7.354574,3.185530,-1.578090,-6.628480,5.237720,9.086917,-9.138138,-8.819054,-3.921026,-6.963591,6.627510,-3.231563,-0.558313,-1.878044,-6.663533,-6.812766,-5.687806,-6.470843,-2.467041,6.256823,6.580088,-3.541125,8.331997,-9.755364,3.919362,8.231621,6.428911,1.579268,-3.400516,6.541333,3.238685,5.346073,1.105889,-1.498409,-4.276082,-4.863995,-0.170204,6.530705,9.560363,-7.655838,2.454512,-5.662065,9.708456,-3.858451,7.896240,-0.174867,7.888099,-4.976462,2.984419,-0.234047,1.868078,0.144670,-5.761782,6.370345,-0.401432,-4.529875,5.140783,7.456020,0.123523,6.803945,9.282339,4.299486,1.579017,3.081563,-9.781395,-3.956872,-4.901095,-2.244347,2.550057,8.391983,4.403374,1.730569,-5.495441], dtype = "float64")#candidate|11356|(1600,)|const|float64
bop_11357 = relay.less(const_11324.astype('bool'), relay.reshape(const_11356.astype('bool'), relay.shape_of(const_11324))) # shape=(1600,)
output = relay.Tuple([call_11260,call_11323,call_11326,call_11333,const_11334,call_11346,bop_11357,])
output2 = relay.Tuple([call_11261,call_11325,call_11327,call_11335,const_11334,call_11347,bop_11357,])
func_11365 = relay.Function([], output)
mod['func_11365'] = func_11365
mod = relay.transform.InferType()(mod)
mutated_mod['func_11365'] = func_11365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11365_call = mutated_mod.get_global_var('func_11365')
call_11366 = func_11365_call()
output = call_11366
func_11367 = relay.Function([], output)
mutated_mod['func_11367'] = func_11367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2955_call = mod.get_global_var('func_2955')
func_2957_call = mutated_mod.get_global_var('func_2957')
call_11420 = relay.TupleGetItem(func_2955_call(), 1)
call_11421 = relay.TupleGetItem(func_2957_call(), 1)
func_7230_call = mod.get_global_var('func_7230')
func_7232_call = mutated_mod.get_global_var('func_7232')
call_11429 = relay.TupleGetItem(func_7230_call(), 0)
call_11430 = relay.TupleGetItem(func_7232_call(), 0)
output = relay.Tuple([call_11420,call_11429,])
output2 = relay.Tuple([call_11421,call_11430,])
func_11452 = relay.Function([], output)
mod['func_11452'] = func_11452
mod = relay.transform.InferType()(mod)
output = func_11452()
func_11453 = relay.Function([], output)
mutated_mod['func_11453'] = func_11453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7077_call = mod.get_global_var('func_7077')
func_7078_call = mutated_mod.get_global_var('func_7078')
call_11460 = func_7077_call()
call_11461 = func_7077_call()
output = call_11460
output2 = call_11461
func_11467 = relay.Function([], output)
mod['func_11467'] = func_11467
mod = relay.transform.InferType()(mod)
mutated_mod['func_11467'] = func_11467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11467_call = mutated_mod.get_global_var('func_11467')
call_11468 = func_11467_call()
output = call_11468
func_11469 = relay.Function([], output)
mutated_mod['func_11469'] = func_11469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10106_call = mod.get_global_var('func_10106')
func_10107_call = mutated_mod.get_global_var('func_10107')
call_11512 = relay.TupleGetItem(func_10106_call(), 0)
call_11513 = relay.TupleGetItem(func_10107_call(), 0)
func_3504_call = mod.get_global_var('func_3504')
func_3506_call = mutated_mod.get_global_var('func_3506')
call_11529 = relay.TupleGetItem(func_3504_call(), 0)
call_11530 = relay.TupleGetItem(func_3506_call(), 0)
func_9794_call = mod.get_global_var('func_9794')
func_9797_call = mutated_mod.get_global_var('func_9797')
var_11532 = relay.var("var_11532", dtype = "float64", shape = (231, 2))#candidate|11532|(231, 2)|var|float64
call_11531 = relay.TupleGetItem(func_9794_call(relay.reshape(var_11532.astype('float64'), [462,]), relay.reshape(var_11532.astype('float64'), [462,]), ), 2)
call_11533 = relay.TupleGetItem(func_9797_call(relay.reshape(var_11532.astype('float64'), [462,]), relay.reshape(var_11532.astype('float64'), [462,]), ), 2)
bop_11538 = relay.floor_divide(call_11512.astype('float64'), relay.reshape(call_11529.astype('float64'), relay.shape_of(call_11512))) # shape=(1, 11, 3)
bop_11541 = relay.floor_divide(call_11513.astype('float64'), relay.reshape(call_11530.astype('float64'), relay.shape_of(call_11513))) # shape=(1, 11, 3)
output = relay.Tuple([call_11531,var_11532,bop_11538,])
output2 = relay.Tuple([call_11533,var_11532,bop_11541,])
F = relay.Function([var_11532,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_11532,], output2)
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
