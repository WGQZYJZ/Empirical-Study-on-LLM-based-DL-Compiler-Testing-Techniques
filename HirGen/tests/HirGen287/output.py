import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_103 = relay.var("var_103", dtype = "uint16", shape = (2, 13, 9))#candidate|103|(2, 13, 9)|var|uint16
const_104 = relay.const([[[1,-2,1,-6,7,7,-3,2,-7],[9,5,6,-2,10,-8,-9,-8,-4],[4,9,-8,-5,-3,2,1,-3,7],[8,-8,1,5,-8,3,-1,-4,6],[-9,6,2,-1,-9,-9,6,8,-6],[-3,-8,-1,3,-8,4,-10,7,-2],[1,-3,-2,7,-10,3,3,-6,-6],[-4,10,-5,-5,7,10,2,7,-4],[-8,6,-5,5,-6,10,9,-1,3],[-5,-3,-2,-4,-4,2,7,-8,-9],[5,-10,-4,-4,-4,3,-3,6,1],[-8,-4,3,2,-5,6,-3,7,-1],[-6,3,-10,-5,-7,10,1,-2,-2]],[[-1,8,5,2,-2,-3,-10,-7,-7],[1,1,-7,5,-9,-2,-5,-7,9],[-6,10,-9,-10,10,-6,-4,10,-5],[8,-6,-1,10,-1,1,-9,-2,5],[-9,-2,2,-7,5,4,6,-3,1],[-1,2,-7,4,7,4,9,7,-4],[9,7,-1,-5,-5,9,4,6,-10],[8,9,-9,-9,8,-10,-5,6,-5],[7,1,-2,-7,-10,4,-5,5,-10],[-9,-5,-7,1,-5,5,3,-2,3],[7,-10,-2,7,9,-3,8,-9,1],[7,-7,-1,2,6,8,-10,1,10],[-6,-1,10,-3,-8,-9,-8,2,-9]]], dtype = "uint16")#candidate|104|(2, 13, 9)|const|uint16
bop_105 = relay.multiply(var_103.astype('uint16'), relay.reshape(const_104.astype('uint16'), relay.shape_of(var_103))) # shape=(2, 13, 9)
output = bop_105
output2 = bop_105
func_108 = relay.Function([var_103,], output)
mod['func_108'] = func_108
mod = relay.transform.InferType()(mod)
mutated_mod['func_108'] = func_108
mutated_mod = relay.transform.InferType()(mutated_mod)
var_109 = relay.var("var_109", dtype = "uint16", shape = (2, 13, 9))#candidate|109|(2, 13, 9)|var|uint16
func_108_call = mutated_mod.get_global_var('func_108')
call_110 = func_108_call(var_109)
output = call_110
func_111 = relay.Function([var_109], output)
mutated_mod['func_111'] = func_111
mutated_mod = relay.transform.InferType()(mutated_mod)
var_491 = relay.var("var_491", dtype = "bool", shape = (16, 14, 14))#candidate|491|(16, 14, 14)|var|bool
const_492 = relay.const([[[True,False,True,True,False,False,False,True,False,False,True,False,False,False],[True,False,True,False,False,True,False,True,False,False,True,True,True,False],[False,True,False,True,True,False,True,True,False,True,True,False,True,False],[False,True,True,True,False,False,True,False,True,False,False,False,False,True],[True,True,False,False,False,False,True,True,False,False,True,False,False,False],[False,True,False,False,True,True,False,True,True,True,True,True,True,True],[True,True,True,False,False,True,False,False,True,False,False,False,False,True],[False,False,True,True,False,True,True,True,True,True,False,False,True,True],[True,False,True,False,False,False,True,False,True,True,True,False,True,True],[False,False,False,True,False,True,False,False,False,True,True,True,True,True],[False,False,True,True,False,False,False,False,False,True,True,True,False,False],[True,False,True,False,False,True,True,False,False,True,True,False,False,False],[False,True,False,False,True,True,True,False,True,True,False,True,False,True],[False,True,True,True,True,False,True,True,True,False,True,True,True,False]],[[False,False,True,False,True,True,False,True,False,True,True,True,True,True],[False,True,True,False,False,False,True,True,True,True,False,False,True,False],[False,True,False,False,True,True,False,False,False,False,True,False,True,False],[True,False,False,True,False,True,True,False,True,True,False,False,False,False],[True,True,False,True,False,True,True,True,False,True,False,True,True,True],[True,False,False,True,True,False,False,True,True,False,True,False,True,True],[True,True,False,False,False,False,True,True,True,False,False,False,True,False],[True,False,False,False,False,False,True,True,False,False,False,True,False,False],[True,True,True,False,False,True,False,False,False,True,True,True,True,False],[True,False,False,False,False,False,True,True,False,False,False,False,False,True],[True,False,True,True,True,False,True,True,False,False,False,False,True,True],[True,True,True,True,True,False,True,False,False,False,True,True,True,True],[True,True,False,True,False,True,False,True,False,True,True,False,True,True],[False,True,False,True,False,False,False,True,False,False,True,False,False,False]],[[True,True,False,True,True,False,False,True,False,False,False,False,True,True],[False,True,False,False,False,True,True,False,True,False,True,True,False,True],[True,False,True,True,False,True,False,True,False,False,False,False,False,False],[False,True,False,False,False,False,False,False,True,True,False,False,True,False],[True,True,True,True,False,False,False,False,False,False,True,False,False,True],[False,False,True,False,True,True,False,False,False,False,False,True,True,True],[False,True,True,True,False,False,False,False,False,False,False,False,False,True],[False,False,False,False,False,False,False,False,True,False,False,True,False,False],[True,False,True,True,True,False,False,True,False,True,False,True,True,False],[True,False,False,False,False,False,False,True,False,True,True,False,True,True],[True,False,True,False,False,True,True,True,True,False,False,False,True,False],[True,False,True,False,False,True,False,True,True,True,False,False,False,True],[False,True,False,True,True,True,False,True,False,True,False,False,True,True],[False,False,True,True,True,False,True,True,True,False,False,True,True,False]],[[True,True,True,True,False,True,False,False,True,False,True,True,False,False],[True,True,True,True,False,False,False,True,True,False,False,False,False,True],[True,True,True,False,False,True,True,False,False,False,False,True,False,False],[True,False,False,False,False,True,False,False,True,False,True,False,False,True],[True,False,False,False,True,False,True,True,True,False,False,True,False,False],[True,True,False,False,True,False,False,True,True,False,True,True,True,False],[True,True,False,False,False,False,True,True,False,False,True,True,False,True],[True,True,True,False,False,False,False,True,False,False,True,False,True,False],[True,False,True,False,True,True,True,True,True,False,True,False,False,False],[True,False,True,False,True,False,False,True,False,False,True,True,True,False],[True,False,False,False,False,True,False,True,False,True,True,False,True,False],[False,True,False,True,False,True,False,True,True,False,True,False,True,False],[True,False,False,False,False,False,False,False,False,False,True,False,False,False],[False,True,False,False,True,False,False,True,True,False,False,True,False,True]],[[True,True,True,False,True,True,False,True,False,False,True,False,False,True],[False,False,True,True,False,False,True,True,False,True,False,False,True,False],[True,False,False,False,True,True,False,True,True,False,False,True,False,False],[True,False,True,True,True,False,False,True,False,False,False,True,True,False],[True,True,False,False,True,False,False,False,False,False,True,True,False,False],[False,False,False,True,False,True,False,True,True,True,False,False,True,False],[True,False,False,False,True,True,False,False,True,False,True,True,False,False],[False,False,False,False,False,False,True,False,True,False,False,True,True,False],[True,False,True,False,False,True,False,False,False,False,False,False,False,True],[True,False,False,False,False,False,False,False,True,False,False,False,False,False],[True,True,True,False,True,False,False,True,True,False,True,False,False,False],[False,False,True,True,False,True,True,False,False,False,False,True,False,True],[True,False,True,True,True,False,True,False,False,False,True,False,False,True],[False,True,True,False,True,False,True,False,False,True,False,False,True,True]],[[True,True,False,False,True,True,True,False,False,True,False,False,True,True],[False,True,False,False,False,True,False,False,False,False,False,False,True,False],[False,False,True,True,True,True,True,False,True,True,False,True,False,False],[True,True,True,False,False,False,False,True,True,True,True,True,True,True],[True,False,True,True,False,True,False,True,False,False,True,True,True,True],[False,True,True,False,False,False,False,False,False,False,True,False,True,False],[True,False,True,True,False,True,False,False,False,True,True,False,True,False],[False,False,True,False,True,False,False,True,True,False,True,True,True,True],[True,False,True,True,True,True,False,True,False,False,False,False,True,True],[False,False,False,False,False,True,True,True,False,True,False,True,False,False],[False,True,True,False,True,False,True,False,True,True,False,True,True,False],[True,True,True,False,True,True,False,False,True,True,True,True,True,False],[False,True,False,False,False,True,False,True,True,True,False,True,False,False],[False,False,False,False,True,True,False,False,True,False,False,False,False,False]],[[True,True,False,True,False,False,True,False,True,False,True,False,True,True],[True,False,True,False,False,True,False,True,True,False,True,False,False,False],[False,False,False,True,True,False,False,True,False,True,True,True,True,True],[True,True,False,True,True,False,True,True,True,True,False,False,True,True],[False,True,True,False,False,True,True,True,True,True,True,True,True,False],[False,False,True,False,True,False,True,False,False,False,True,True,True,True],[False,False,True,False,True,False,True,True,False,False,True,True,False,False],[True,True,False,True,True,False,True,True,False,False,True,False,False,True],[True,True,False,True,True,True,False,True,False,True,False,False,True,True],[True,True,True,False,False,False,False,False,False,True,True,False,False,False],[False,False,True,True,False,False,True,True,True,True,False,True,False,True],[True,True,False,True,True,False,True,True,False,True,True,False,True,False],[False,True,True,False,True,False,True,True,False,False,True,False,True,True],[True,True,False,True,True,True,False,False,True,True,True,True,True,True]],[[True,False,True,True,True,False,True,False,True,False,False,True,True,True],[True,False,False,True,False,True,False,True,False,False,True,True,True,False],[False,False,True,True,False,True,False,True,True,True,False,False,True,False],[False,False,True,True,True,True,False,True,False,False,False,False,False,True],[True,False,True,True,False,True,False,True,False,False,False,True,True,False],[False,True,False,False,True,True,True,False,True,False,True,True,False,True],[False,True,False,True,True,False,True,True,True,True,False,True,False,True],[False,True,True,False,False,False,False,False,True,False,False,False,False,False],[False,False,True,False,True,False,True,False,False,False,False,True,False,False],[False,False,True,False,True,True,True,False,True,True,False,False,True,False],[True,True,False,True,False,False,True,True,False,False,False,False,True,False],[True,True,False,True,True,False,True,False,True,False,False,False,False,False],[False,True,True,True,True,True,False,True,True,True,False,True,False,False],[True,True,False,False,False,True,True,True,True,True,True,False,True,False]],[[False,True,False,False,True,True,False,False,True,False,True,False,False,True],[False,False,False,True,True,False,False,True,True,True,False,False,False,True],[False,False,True,False,True,False,True,False,True,True,False,False,True,True],[True,True,True,True,True,True,False,False,True,False,True,True,False,True],[True,False,True,False,False,False,False,False,False,True,False,False,False,True],[False,False,False,True,True,True,False,True,False,True,True,False,True,True],[True,True,False,False,False,True,False,False,False,True,False,False,False,True],[False,True,False,True,True,False,False,False,False,True,True,False,False,True],[False,True,False,True,True,False,False,True,False,False,True,False,True,False],[False,False,True,True,True,True,False,False,True,False,False,True,True,False],[False,True,True,False,True,True,False,False,True,False,True,True,False,False],[True,False,False,False,False,True,True,True,False,True,True,False,True,True],[True,True,True,True,False,False,False,True,True,False,True,True,False,False],[False,False,True,False,False,True,False,False,True,True,True,True,False,False]],[[True,True,False,True,False,True,False,True,False,False,False,True,False,False],[False,False,False,True,True,True,True,True,True,True,False,False,False,True],[True,False,False,True,True,False,False,False,True,False,True,True,True,True],[True,True,True,True,False,False,False,True,True,True,False,False,False,False],[False,False,False,False,False,False,True,False,False,True,False,True,True,True],[True,False,False,False,False,False,True,False,False,False,True,True,True,True],[False,False,False,False,False,False,False,True,False,True,True,False,False,True],[True,False,False,False,False,False,False,False,False,False,False,False,False,True],[False,True,True,False,True,True,False,False,True,True,True,True,False,False],[True,True,True,False,True,True,True,True,True,True,False,False,True,False],[False,True,False,False,True,True,False,False,False,True,False,True,False,True],[False,False,True,True,True,False,True,False,True,False,False,True,False,False],[True,True,False,True,True,False,False,False,True,False,False,True,True,True],[False,True,False,False,False,False,True,True,False,True,False,False,True,False]],[[True,True,False,False,True,False,True,False,True,True,False,False,False,False],[False,True,True,False,True,False,True,True,False,False,False,False,True,False],[False,True,False,True,False,False,True,True,True,True,True,False,False,True],[False,False,False,False,False,True,True,True,True,False,False,True,False,False],[False,False,True,False,True,True,False,True,False,True,True,True,False,False],[True,True,False,True,True,False,False,True,True,True,False,True,True,False],[False,True,True,False,True,False,True,False,True,True,False,True,False,True],[False,True,True,True,False,True,True,True,True,True,True,True,False,True],[False,True,False,False,False,True,True,False,True,False,False,False,True,False],[False,True,True,False,False,True,False,False,False,True,False,False,False,True],[True,False,False,True,True,False,True,True,True,False,True,False,False,False],[True,True,False,True,True,False,True,True,True,True,False,True,False,False],[True,False,True,False,False,True,True,True,False,True,True,True,True,False],[False,False,False,True,True,True,False,False,True,True,False,False,True,False]],[[True,True,False,True,False,True,True,False,False,True,False,False,False,True],[False,True,True,False,True,False,True,True,True,True,True,False,False,True],[False,True,True,True,True,True,False,True,False,False,True,True,True,True],[True,True,False,True,False,False,True,False,False,False,True,True,True,False],[True,False,False,True,True,True,False,False,True,True,True,True,True,True],[False,False,False,False,True,True,True,True,True,True,True,True,True,False],[False,True,True,True,True,True,False,False,False,False,True,True,True,False],[True,False,True,True,False,False,True,True,True,True,True,False,False,False],[True,True,True,True,False,False,False,True,True,False,False,True,False,True],[True,False,True,False,False,True,True,True,True,True,False,False,False,True],[False,False,False,True,True,True,False,False,True,False,True,False,False,True],[True,False,False,False,False,False,False,True,True,False,False,False,True,False],[False,True,False,False,True,False,True,False,True,True,False,False,True,False],[False,True,True,True,True,False,False,False,False,False,True,True,False,True]],[[True,True,True,True,False,True,True,True,True,False,False,False,True,False],[False,False,False,False,True,False,False,False,False,False,False,False,False,True],[True,True,False,False,False,False,True,True,True,False,False,True,False,False],[True,True,True,False,True,True,False,False,True,False,False,True,False,True],[True,True,False,False,False,True,False,False,True,True,True,False,True,False],[True,True,False,True,False,True,True,True,True,True,True,False,False,False],[False,False,True,True,True,True,False,True,False,False,False,True,False,True],[False,True,True,True,True,False,False,True,True,True,True,False,True,False],[True,True,False,True,True,True,False,True,True,False,False,True,True,False],[True,True,False,True,False,True,False,True,True,True,True,True,False,False],[True,True,False,False,False,True,True,False,False,False,True,True,False,True],[True,True,False,False,False,False,True,True,True,True,False,True,False,True],[False,True,True,True,False,False,False,True,True,True,True,True,True,False],[True,False,True,False,True,True,False,False,True,True,True,True,False,True]],[[False,True,True,False,False,False,True,False,False,True,True,True,True,False],[True,False,False,False,False,False,False,False,True,False,False,True,True,True],[False,True,False,False,False,True,False,False,False,True,True,False,True,False],[False,False,True,True,False,True,True,True,True,True,True,True,True,True],[False,False,False,False,True,False,False,False,False,False,False,False,True,True],[False,False,False,False,False,True,True,True,False,False,False,False,True,True],[True,False,False,True,False,False,True,False,False,True,False,False,True,False],[False,False,False,True,True,False,True,True,True,True,False,True,True,False],[True,True,True,False,True,True,True,False,True,False,False,False,True,False],[False,False,False,True,True,False,False,False,False,True,True,True,False,False],[True,False,False,False,True,False,True,False,True,False,False,True,True,False],[True,False,False,True,True,True,False,False,True,False,False,False,False,True],[True,False,True,False,False,False,True,True,False,False,False,True,False,False],[False,True,True,True,False,True,True,True,False,True,True,False,False,True]],[[False,False,False,True,False,False,False,True,False,True,False,False,True,False],[True,True,True,False,True,False,True,True,True,False,False,False,False,True],[False,False,False,False,False,False,True,False,False,True,True,False,False,False],[False,True,False,False,True,True,False,False,True,True,True,True,False,True],[True,False,False,True,False,False,True,False,False,False,False,True,False,False],[True,False,False,False,False,False,False,True,False,False,True,True,True,False],[False,True,True,True,True,True,False,True,True,True,True,True,False,False],[False,False,False,False,False,False,False,False,False,False,True,False,False,False],[False,True,False,False,True,True,False,False,False,False,False,True,False,True],[True,False,True,True,False,True,True,False,True,True,True,False,True,False],[False,True,True,False,True,True,True,False,True,True,False,True,True,False],[True,True,False,False,True,True,True,True,True,True,False,False,False,True],[False,False,True,True,True,False,True,False,False,False,False,True,True,True],[False,True,True,True,False,True,True,False,True,True,True,False,False,True]],[[False,False,False,True,False,False,False,False,False,True,False,False,False,True],[True,True,False,False,False,True,True,True,True,True,True,False,False,False],[False,False,False,False,False,False,True,True,False,True,True,True,True,True],[True,True,False,True,False,False,True,True,False,False,False,True,True,True],[True,True,True,True,True,True,True,False,False,True,True,False,False,False],[True,True,True,True,False,False,False,True,False,True,False,False,True,False],[True,True,True,False,False,False,True,False,False,True,False,False,False,True],[False,False,True,False,False,False,True,False,False,True,True,True,False,True],[True,True,True,True,False,False,True,True,True,True,True,True,False,True],[True,False,False,True,False,True,True,False,True,False,True,False,True,False],[True,True,False,False,True,True,True,True,False,True,False,True,False,True],[False,False,False,True,False,False,False,False,True,False,True,True,False,False],[True,False,False,False,True,False,False,False,False,False,False,False,True,False],[True,True,False,True,True,False,False,True,True,False,True,False,False,False]]], dtype = "bool")#candidate|492|(16, 14, 14)|const|bool
bop_493 = relay.logical_or(var_491.astype('bool'), relay.reshape(const_492.astype('bool'), relay.shape_of(var_491))) # shape=(16, 14, 14)
output = relay.Tuple([bop_493,])
output2 = relay.Tuple([bop_493,])
func_499 = relay.Function([var_491,], output)
mod['func_499'] = func_499
mod = relay.transform.InferType()(mod)
var_500 = relay.var("var_500", dtype = "bool", shape = (16, 14, 14))#candidate|500|(16, 14, 14)|var|bool
output = func_499(var_500)
func_501 = relay.Function([var_500], output)
mutated_mod['func_501'] = func_501
mutated_mod = relay.transform.InferType()(mutated_mod)
var_548 = relay.var("var_548", dtype = "float32", shape = (10, 4, 16))#candidate|548|(10, 4, 16)|var|float32
uop_549 = relay.acos(var_548.astype('float32')) # shape=(10, 4, 16)
func_499_call = mod.get_global_var('func_499')
func_501_call = mutated_mod.get_global_var('func_501')
const_561 = relay.const([[True,False],[True,True],[False,True],[True,False],[False,True],[True,False],[False,True],[True,True],[True,False],[False,False],[True,False],[False,True],[True,False],[False,False],[False,True],[False,True],[True,True],[True,False],[False,False],[False,False],[True,True],[False,True],[False,False],[False,False],[False,True],[False,True],[True,True],[False,False],[True,False],[False,False],[True,False],[True,True],[True,False],[True,True],[True,True],[True,False],[False,False],[False,False],[False,False],[False,False],[True,True],[False,True],[False,False],[True,True],[True,False],[True,False],[False,True],[True,False],[True,False],[True,False],[True,True],[True,True],[True,True],[False,True],[True,False],[True,True],[True,True],[False,True],[False,True],[True,True],[True,False],[True,False],[True,True],[False,True],[True,True],[True,True],[False,False],[False,True],[True,False],[False,True],[True,False],[False,False],[True,False],[False,True],[True,True],[False,True],[True,False],[True,True],[True,True],[False,False],[False,True],[True,True],[False,False],[False,True],[False,True],[False,True],[True,False],[False,False],[False,False],[False,False],[True,False],[True,False],[False,False],[True,True],[True,True],[False,True],[True,True],[False,True],[True,True],[False,False],[False,True],[True,True],[True,True],[True,False],[True,True],[False,False],[False,True],[True,False],[True,False],[False,False],[False,False],[True,True],[True,False],[False,True],[True,False],[True,True],[True,False],[False,True],[False,True],[True,True],[True,True],[False,True],[False,True],[True,True],[True,True],[True,True],[True,False],[False,True],[False,False],[False,True],[True,True],[False,False],[True,False],[True,True],[False,False],[True,True],[True,True],[False,True],[False,True],[False,True],[True,True],[True,False],[False,True],[True,False],[False,True],[False,True],[False,False],[True,False],[True,True],[True,True],[True,False],[False,True],[True,False],[False,True],[True,True],[True,False],[False,False],[True,False],[True,False],[True,True],[False,True],[False,False],[True,False],[False,False],[True,False],[True,False],[False,True],[True,False],[True,False],[True,True],[True,False],[True,True],[False,False],[False,False],[True,True],[True,True],[False,False],[True,True],[False,False],[False,True],[False,True],[True,False],[True,True],[False,False],[True,False],[True,False],[False,True],[True,True],[True,True],[True,False],[False,False],[True,False],[False,True],[False,False],[True,False],[True,True],[True,True],[True,False],[False,False],[True,True],[False,False],[True,False],[True,False],[True,True],[False,False],[True,False],[True,True],[True,True],[False,True],[False,True],[True,True],[False,False],[False,True],[True,False],[True,False],[True,True],[False,False],[False,False],[True,True],[True,True],[False,False],[True,True],[True,False],[False,True],[True,False],[False,False],[False,False],[True,False],[False,False],[True,True],[False,False],[True,False],[True,True],[False,False],[False,True],[True,False],[False,False],[True,True],[True,False],[True,False],[False,True],[True,False],[False,False],[True,False],[False,False],[True,False],[False,False],[False,True],[True,True],[True,False],[False,False],[False,False],[True,False],[False,False],[False,True],[False,False],[False,True],[True,False],[True,False],[False,True],[False,False],[True,False],[False,False],[False,False],[True,True],[False,True],[False,False],[False,True],[False,False],[True,False],[True,True],[True,True],[True,False],[False,False],[False,False],[False,False],[False,True],[False,True],[True,False],[True,False],[False,True],[False,False],[True,False],[True,False],[False,False],[False,True],[True,True],[False,False],[True,False],[True,True],[True,True],[True,True],[False,False],[False,False],[False,True],[False,False],[False,False],[False,False],[False,True],[False,False],[True,False],[True,True],[False,False],[True,True],[False,False],[True,True],[True,False],[True,False],[False,True],[False,True],[True,False],[True,True],[True,False],[True,True],[True,True],[False,True],[False,True],[False,False],[True,True],[True,False],[False,False],[True,True],[True,False],[True,True],[False,True],[False,True],[False,False],[False,True],[False,False],[False,True],[True,False],[False,True],[False,False],[True,True],[False,True],[True,False],[True,True],[True,False],[True,True],[False,True],[False,False],[False,False],[False,True],[True,False],[True,False],[False,False],[False,False],[False,False],[True,True],[False,True],[False,True],[True,False],[False,False],[False,False],[True,False],[True,False],[True,False],[False,True],[True,False],[False,False],[False,False],[False,False],[False,False],[True,True],[False,True],[False,False],[False,True],[False,True],[False,True],[True,True],[True,False],[True,False],[False,False],[False,True],[False,False],[True,False],[False,False],[False,False],[False,True],[False,False],[False,False],[True,True],[False,True],[False,False],[False,True],[True,False],[True,True],[False,False],[True,False],[True,True],[False,True],[True,False],[True,True],[True,True],[True,True],[False,True],[True,True],[False,True],[False,False],[True,True],[True,True],[True,True],[False,True],[True,True],[False,False],[False,False],[True,True],[True,False],[False,False],[False,True],[True,False],[True,False],[True,True],[False,True],[False,True],[False,True],[False,True],[False,False],[True,True],[True,True],[False,True],[True,True],[False,False],[False,True],[False,False],[False,True],[False,True],[False,True],[True,False],[False,True],[True,True],[False,False],[False,True],[False,True],[False,False],[False,False],[True,False],[False,False],[False,False],[True,True],[False,True],[False,False],[True,False],[True,False],[False,True],[True,False],[False,True],[False,True],[False,False],[False,True],[False,True],[True,False],[True,True],[False,True],[True,True],[False,True],[False,True],[True,True],[True,False],[True,False],[False,False],[False,False],[False,False],[True,False],[False,False],[True,True],[True,True],[True,False],[False,True],[True,False],[False,False],[True,False],[True,True],[False,False],[True,True],[False,True],[False,False],[False,False],[False,True],[False,True],[True,False],[False,False],[True,True],[False,True],[False,False],[True,False],[False,True],[False,True],[False,False],[True,True],[False,False],[True,False],[False,True],[False,True],[False,False],[False,False],[False,False],[False,True],[True,True],[True,True],[True,False],[True,True],[True,True],[False,True],[False,True],[True,False],[True,False],[False,False],[True,False],[True,True],[False,True],[True,True],[True,False],[False,False],[True,True],[True,False],[False,False],[True,True],[True,True],[True,True],[False,False],[True,False],[False,True],[False,True],[True,True],[False,False],[False,False],[True,True],[False,True],[True,True],[True,False],[True,True],[False,False],[False,True],[True,True],[True,True],[True,False],[True,True],[False,True],[False,True],[False,True],[True,False],[True,False],[True,True],[False,False],[False,True],[False,True],[False,False],[True,False],[False,False],[False,True],[True,True],[True,True],[True,True],[False,True],[True,True],[False,False],[True,True],[True,True],[False,True],[True,False],[False,False],[True,False],[False,False],[False,False],[False,False],[True,False],[False,True],[True,True],[False,True],[False,True],[False,True],[False,False],[False,True],[True,True],[False,False],[True,False],[False,True],[False,True],[True,False],[True,False],[True,True],[False,True],[False,True],[False,False],[False,False],[False,True],[True,False],[True,False],[True,False],[True,True],[False,False],[True,True],[True,True],[False,True],[True,True],[True,False],[False,True],[True,False],[False,True],[True,False],[False,True],[True,True],[True,False],[True,False],[False,False],[True,True],[True,False],[False,False],[True,False],[True,False],[True,False],[True,False],[True,False],[False,True],[False,True],[False,False],[False,True],[True,True],[False,True],[True,False],[True,False],[True,False],[False,True],[True,True],[True,False],[False,True],[True,True],[True,False],[True,True],[False,True],[True,False],[True,True],[True,True],[True,True],[False,False],[False,True],[True,True],[False,True],[True,True],[True,False],[True,True],[True,False],[False,False],[True,True],[False,True],[True,True],[True,False],[False,False],[True,True],[False,True],[False,False],[True,True],[True,True],[False,False],[False,True],[True,True],[False,False],[False,False],[True,True],[False,True],[False,True],[False,True],[True,False],[True,True],[False,True],[False,False],[True,True],[True,True],[False,True],[True,False],[True,False],[False,True],[True,False],[False,False],[True,False],[True,True],[True,True],[False,False],[True,True],[True,True],[True,False],[True,False],[True,False],[True,False],[False,True],[False,True],[True,False],[False,False],[False,False],[False,True],[False,True],[False,True],[False,False],[False,False],[False,True],[True,True],[True,True],[True,True],[True,True],[True,True],[False,True],[False,True],[False,True],[False,False],[True,False],[False,False],[False,False],[True,False],[True,True],[False,True],[True,False],[False,False],[True,True],[True,False],[False,False],[False,False],[False,False],[False,False],[True,False],[False,True],[False,False],[True,False],[True,False],[True,False],[False,True],[True,True],[True,True],[True,False],[False,True],[True,True],[True,True],[True,True],[True,True],[True,True],[True,False],[False,False],[False,True],[False,True],[True,True],[True,True],[True,False],[False,False],[True,False],[True,False],[True,False],[True,False],[True,False],[False,False],[False,True],[True,True],[True,True],[True,False],[False,False],[True,False],[True,True],[True,False],[True,False],[True,True],[False,False],[True,True],[False,False],[True,True],[False,True],[True,False],[True,True],[False,False],[False,True],[False,True],[True,False],[True,True],[True,False],[True,False],[False,False],[True,False],[False,False],[True,False],[False,True],[True,True],[False,True],[True,True],[False,True],[False,False],[True,False],[True,False],[False,False],[True,True],[True,True],[False,True],[True,True],[False,False],[False,True],[False,False],[False,False],[True,True],[True,True],[False,True],[False,False],[True,True],[True,True],[False,True],[True,True],[True,False],[False,True],[False,False],[False,False],[False,False],[True,False],[True,False],[False,False],[True,True],[True,True],[False,False],[False,False],[True,True],[True,True],[False,False],[True,True],[True,True],[False,True],[True,True],[True,True],[True,False],[False,False],[False,False],[True,True],[False,False],[True,False],[False,True],[False,False],[False,True],[True,False],[False,False],[False,True],[False,False],[False,True],[True,True],[True,True],[True,True],[True,False],[True,False],[True,True],[True,False],[False,True],[True,False],[True,True],[False,True],[False,False],[True,False],[True,True],[False,True],[True,False],[False,False],[True,True],[True,False],[True,False],[True,True],[False,False],[True,False],[True,True],[False,True],[False,False],[False,False],[False,True],[False,True],[True,True],[False,False],[True,False],[False,False],[False,True],[False,True],[True,True],[False,True],[True,False],[True,True],[True,False],[False,True],[False,False],[False,True],[True,False],[False,False],[True,True],[False,False],[True,False],[False,True],[True,True],[True,True],[False,True],[False,False],[True,False],[True,False],[False,True],[False,False],[True,False],[True,False],[False,False],[True,False],[True,True],[False,False],[False,True],[False,True],[False,True],[False,False],[False,True],[False,False],[True,True],[False,True],[False,False],[True,True],[False,True],[False,True],[True,True],[True,False],[False,True],[False,False],[False,False],[False,False],[True,False],[True,False],[True,True],[False,False],[True,False],[True,True],[True,True],[True,True],[False,True],[False,True],[False,True],[True,False],[True,True],[True,True],[False,True],[False,True],[True,True],[True,True],[False,True],[True,True],[False,True],[True,True],[False,False],[False,False],[True,True],[True,True],[False,False],[True,True],[True,False],[True,True],[True,True],[True,True],[False,False],[False,False],[False,True],[False,False],[False,True],[True,False],[True,True],[False,False],[False,True],[True,True],[True,False],[False,True],[True,True],[False,False],[False,True],[True,False],[False,True],[True,False],[True,True],[False,True],[False,True],[False,True],[False,False],[True,True],[False,False],[False,True],[False,False],[False,True],[False,True],[False,False],[False,True],[True,False],[True,False],[False,False],[True,False],[True,True],[True,True],[False,False],[False,True],[True,False],[True,True],[True,True],[True,False],[True,True],[True,True],[False,True],[False,True],[False,True],[True,False],[True,False],[True,True],[True,False],[False,True],[False,False],[False,True],[False,True],[False,False],[False,False],[False,True],[True,True],[False,True],[False,True],[False,False],[False,True],[True,False],[True,False],[True,False],[False,True],[True,True],[False,True],[False,False],[False,True],[False,True],[True,False],[False,False],[True,True],[False,False],[False,False],[False,False],[False,True],[False,True],[True,True],[False,False],[True,True],[True,True],[True,True],[True,True],[False,False],[False,True],[False,True],[False,False],[False,False],[False,False],[False,False],[False,False],[False,True],[False,True],[False,False],[True,True],[True,False],[False,False],[False,False],[False,False],[False,False],[False,False],[True,False],[False,True],[False,False],[True,False],[True,False],[True,True],[True,True],[False,True],[True,False],[True,False],[False,True],[True,False],[True,True],[True,True],[True,True],[False,True],[True,False],[False,True],[True,False],[True,False],[False,False],[True,True],[True,True],[False,False],[True,True],[True,False],[True,False],[False,False],[True,True],[False,False],[False,False],[True,True],[False,False],[False,True],[False,False],[True,False],[False,False],[True,False],[False,True],[False,True],[True,True],[True,False],[True,False],[False,False],[True,False],[True,False],[False,False],[True,True],[False,False],[False,False],[False,False],[False,False],[False,True],[False,False],[True,True],[False,False],[False,True],[False,False],[True,False],[False,True],[True,True],[True,True],[False,False],[False,False],[False,True],[True,False],[True,True],[True,True],[True,True],[False,False],[False,False],[False,True],[True,False],[True,True],[False,True],[False,True],[True,True],[True,True],[True,True],[True,False],[False,False],[False,True],[False,True],[True,True],[True,True],[True,True],[True,True],[False,False],[True,True],[True,True],[True,True],[True,False],[False,False],[True,False],[True,False],[False,False],[True,False],[True,True],[False,False],[False,True],[True,True],[False,False],[False,True],[True,True],[False,False],[False,True],[False,True],[True,False],[True,False],[False,True],[True,False],[True,False],[True,False],[True,True],[True,True],[False,False],[False,False],[True,False],[True,False],[True,False],[False,True],[True,False],[True,True],[True,False],[True,True],[True,False],[False,False],[False,True],[True,True],[False,False],[False,False],[False,False],[False,True],[False,False],[True,True],[False,False],[True,True],[False,False],[False,True],[False,False],[True,False],[False,True],[False,True],[False,True],[False,False],[True,True],[False,False],[True,False],[True,False],[False,True],[True,False],[True,False],[False,True],[False,False],[True,True],[False,False],[True,True],[True,True],[False,True],[True,False],[True,False],[True,True],[False,True],[True,False],[True,False],[True,False],[False,False],[True,False],[True,True],[True,False],[False,True],[False,True],[False,True],[True,False],[False,False],[True,True],[False,False],[False,True],[True,False],[True,False],[False,False],[True,False],[False,False],[True,True],[True,False],[False,False],[True,False],[True,False],[False,False],[False,False],[False,True],[False,True],[False,False],[False,True],[False,True],[False,False],[True,True],[True,True],[True,False],[False,False],[False,False],[False,True],[True,False],[True,True],[False,False],[True,True],[True,True],[False,True],[False,False],[True,False],[True,True],[True,False],[False,False],[True,True],[False,True],[True,False],[False,False],[True,True],[False,True],[False,False],[True,True],[True,False],[True,True],[False,True],[True,True],[True,False],[False,False],[False,False],[False,True],[True,False],[True,False],[False,True],[False,False],[False,False],[True,False],[True,False],[True,False],[False,False],[False,False],[True,True],[True,True],[False,True],[True,False],[True,False],[False,False],[False,True],[True,True],[False,True],[True,False],[False,False],[False,True],[False,True],[True,False],[False,True],[True,True],[True,False],[False,True],[False,False],[True,True],[False,True],[False,False],[False,True],[True,False],[False,False],[False,False],[False,False],[True,False],[False,True],[True,False],[False,False],[True,True],[False,False],[False,False],[False,False],[False,False],[True,False],[False,False],[True,False],[False,True],[False,True],[False,True],[True,True],[True,True],[False,False],[True,True],[False,True],[False,True],[True,True],[True,True],[True,True],[True,False],[True,True],[False,False],[True,True],[False,False],[False,False],[True,True],[True,False],[True,False],[True,False],[True,True],[True,True],[False,False],[False,False],[True,True],[True,False],[False,True],[False,False],[True,True],[True,True],[True,True],[True,False],[True,True],[True,False],[True,False],[False,False],[True,False],[True,False],[False,False],[False,False],[True,True],[False,True],[False,False],[False,False],[False,True],[True,True],[True,True],[False,False],[False,True],[False,True],[True,False],[True,False],[False,False],[False,True],[False,False],[True,False],[False,True],[True,False],[False,True],[False,False],[True,False],[True,False],[True,True],[False,True],[False,False],[False,True],[False,True],[False,True],[True,False],[False,False],[True,True],[False,True],[False,True],[True,False],[True,False],[False,False],[False,False],[False,True],[True,False],[False,False],[False,False],[True,False],[True,True],[True,False],[False,True],[False,True],[False,False],[False,True],[False,True],[True,True],[True,False],[True,True],[False,True],[False,True],[True,False],[True,True],[False,True],[True,True],[False,True],[False,False],[False,False],[True,True],[True,True],[False,True],[True,True],[False,False],[True,True],[False,True],[False,False],[True,True],[True,False],[False,True],[True,True],[True,False],[False,True],[False,True],[True,False],[False,False],[True,False],[True,False],[True,True],[True,True],[False,True],[False,False],[True,True],[True,False],[False,True],[False,True],[True,True],[True,True],[False,False],[False,True],[False,False],[False,True],[False,True],[False,False],[True,True],[True,True],[False,True],[False,True],[True,True],[False,True],[True,False],[False,False],[True,False],[True,True],[False,False],[False,False],[False,False],[True,True],[False,True],[True,True],[False,False],[False,False],[True,False],[False,False],[False,False],[True,True],[False,False],[True,True],[False,False],[False,False],[False,False],[False,True],[True,True],[False,True],[True,True],[False,True],[True,False],[False,False],[True,False],[True,True],[False,False],[False,False],[False,True],[True,False],[True,True],[False,False],[True,False],[True,False],[False,True],[True,True],[False,True],[False,True],[False,False],[True,True],[False,False],[False,False],[True,False],[False,True],[True,True],[False,False],[False,False],[False,False],[True,True],[False,True],[False,False],[False,False],[True,False],[True,True],[True,True],[False,True],[True,False],[False,False],[False,False],[False,True],[False,False],[False,False],[False,False],[False,True],[False,True],[False,False],[True,False],[True,False],[True,False],[False,False],[True,False],[True,True],[True,True],[True,True],[False,True],[True,False],[True,True],[False,False],[True,True],[True,True],[False,False],[False,True],[False,True],[True,True],[True,True],[True,True],[False,True],[False,True]], dtype = "bool")#candidate|561|(1568, 2)|const|bool
call_560 = relay.TupleGetItem(func_499_call(relay.reshape(const_561.astype('bool'), [16, 14, 14])), 0)
call_562 = relay.TupleGetItem(func_501_call(relay.reshape(const_561.astype('bool'), [16, 14, 14])), 0)
func_499_call = mod.get_global_var('func_499')
func_501_call = mutated_mod.get_global_var('func_501')
call_569 = relay.TupleGetItem(func_499_call(relay.reshape(call_560.astype('bool'), [16, 14, 14])), 0)
call_570 = relay.TupleGetItem(func_501_call(relay.reshape(call_560.astype('bool'), [16, 14, 14])), 0)
bop_572 = relay.multiply(const_561.astype('int32'), relay.reshape(call_560.astype('int32'), relay.shape_of(const_561))) # shape=(1568, 2)
bop_575 = relay.multiply(const_561.astype('int32'), relay.reshape(call_562.astype('int32'), relay.shape_of(const_561))) # shape=(1568, 2)
uop_585 = relay.log2(call_569.astype('float32')) # shape=(16, 14, 14)
uop_587 = relay.log2(call_570.astype('float32')) # shape=(16, 14, 14)
func_108_call = mod.get_global_var('func_108')
func_111_call = mutated_mod.get_global_var('func_111')
const_600 = relay.const([[-4,-3,10,4,-9,-2],[-3,-7,-10,-6,2,6],[-3,-3,6,1,6,4],[10,-5,-6,-5,4,7],[-6,6,8,3,-8,6],[-6,5,-3,-9,8,1],[-9,-5,8,-10,5,-4],[9,6,2,3,-9,9],[9,4,-1,3,3,4],[2,-10,9,-1,9,-10],[-9,10,-1,-7,-8,10],[-8,-9,5,-6,9,-5],[10,-9,-3,-2,1,-10],[3,-5,-10,10,1,3],[-5,2,-5,-2,-3,3],[-1,-10,-9,7,10,2],[-8,-2,-4,-5,-3,2],[-2,-2,7,-4,-2,-1],[7,-2,-9,-8,9,-7],[4,3,-7,-5,9,-5],[-3,-5,5,8,1,10],[-6,-10,-10,-9,7,4],[-7,4,-8,-4,-9,-8],[2,-8,-5,6,9,-6],[1,5,-7,3,-2,10],[7,3,-3,-2,-6,-10],[9,2,-2,-8,6,-2],[-4,7,-3,6,-10,-5],[9,-10,8,-5,7,-4],[8,1,-5,6,-9,5],[-7,9,-9,2,4,2],[3,-6,9,-9,-1,-10],[5,-8,-7,4,6,-3],[2,5,-9,-5,-8,-1],[10,-3,-2,9,-9,2],[10,1,-1,-4,-2,-8],[-8,3,3,-3,6,6],[-9,5,-2,3,3,1],[-8,9,-4,3,10,-7]], dtype = "uint16")#candidate|600|(39, 6)|const|uint16
call_599 = func_108_call(relay.reshape(const_600.astype('uint16'), [2, 13, 9]))
call_601 = func_108_call(relay.reshape(const_600.astype('uint16'), [2, 13, 9]))
uop_606 = relay.log10(call_599.astype('float32')) # shape=(2, 13, 9)
uop_608 = relay.log10(call_601.astype('float32')) # shape=(2, 13, 9)
func_499_call = mod.get_global_var('func_499')
func_501_call = mutated_mod.get_global_var('func_501')
call_610 = relay.TupleGetItem(func_499_call(relay.reshape(call_569.astype('bool'), [16, 14, 14])), 0)
call_611 = relay.TupleGetItem(func_501_call(relay.reshape(call_569.astype('bool'), [16, 14, 14])), 0)
func_499_call = mod.get_global_var('func_499')
func_501_call = mutated_mod.get_global_var('func_501')
call_613 = relay.TupleGetItem(func_499_call(relay.reshape(uop_585.astype('bool'), [16, 14, 14])), 0)
call_614 = relay.TupleGetItem(func_501_call(relay.reshape(uop_585.astype('bool'), [16, 14, 14])), 0)
bop_622 = relay.equal(uop_606.astype('bool'), relay.reshape(const_600.astype('bool'), relay.shape_of(uop_606))) # shape=(2, 13, 9)
bop_625 = relay.equal(uop_608.astype('bool'), relay.reshape(const_600.astype('bool'), relay.shape_of(uop_608))) # shape=(2, 13, 9)
output = relay.Tuple([uop_549,bop_572,uop_585,call_610,call_613,bop_622,])
output2 = relay.Tuple([uop_549,bop_575,uop_587,call_611,call_614,bop_625,])
func_629 = relay.Function([var_548,], output)
mod['func_629'] = func_629
mod = relay.transform.InferType()(mod)
mutated_mod['func_629'] = func_629
mutated_mod = relay.transform.InferType()(mutated_mod)
var_630 = relay.var("var_630", dtype = "float32", shape = (10, 4, 16))#candidate|630|(10, 4, 16)|var|float32
func_629_call = mutated_mod.get_global_var('func_629')
call_631 = func_629_call(var_630)
output = call_631
func_632 = relay.Function([var_630], output)
mutated_mod['func_632'] = func_632
mutated_mod = relay.transform.InferType()(mutated_mod)
var_894 = relay.var("var_894", dtype = "float64", shape = (2, 7, 13))#candidate|894|(2, 7, 13)|var|float64
uop_895 = relay.acos(var_894.astype('float64')) # shape=(2, 7, 13)
output = relay.Tuple([uop_895,])
output2 = relay.Tuple([uop_895,])
func_904 = relay.Function([var_894,], output)
mod['func_904'] = func_904
mod = relay.transform.InferType()(mod)
mutated_mod['func_904'] = func_904
mutated_mod = relay.transform.InferType()(mutated_mod)
var_905 = relay.var("var_905", dtype = "float64", shape = (2, 7, 13))#candidate|905|(2, 7, 13)|var|float64
func_904_call = mutated_mod.get_global_var('func_904')
call_906 = func_904_call(var_905)
output = call_906
func_907 = relay.Function([var_905], output)
mutated_mod['func_907'] = func_907
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1035 = relay.const([[[4,4,6,-3,4,-6,-10],[2,-9,9,6,-10,6,-9],[1,-4,-3,2,-4,6,1]],[[-4,9,5,10,5,3,-6],[-7,9,1,5,-4,3,-10],[-5,1,1,5,9,10,-5]],[[9,10,-6,-4,-6,3,5],[-5,-7,3,-2,-9,10,6],[1,-3,-3,-6,3,8,-10]],[[9,-8,-10,9,-4,-10,9],[2,2,-7,4,7,8,2],[1,-6,-7,7,9,1,-4]],[[-8,-2,10,-4,6,-6,-1],[-3,10,-7,4,-3,1,4],[9,4,-3,-8,8,-8,1]],[[7,10,-5,6,1,5,-9],[-7,-10,-3,4,1,-8,3],[5,-2,5,4,4,-3,-10]],[[-8,9,-1,4,3,9,7],[5,3,-5,4,-7,-2,-10],[6,5,8,1,-3,5,-10]],[[-4,-2,-8,-8,-2,-5,-3],[-9,-1,-3,-1,2,-2,5],[-3,-4,2,5,-2,5,7]],[[2,6,-5,8,-5,10,-9],[4,-4,6,3,3,-10,-1],[9,-4,10,-2,-6,4,7]]], dtype = "int64")#candidate|1035|(9, 3, 7)|const|int64
var_1036 = relay.var("var_1036", dtype = "int64", shape = (9, 3, 7))#candidate|1036|(9, 3, 7)|var|int64
bop_1037 = relay.multiply(const_1035.astype('int64'), relay.reshape(var_1036.astype('int64'), relay.shape_of(const_1035))) # shape=(9, 3, 7)
output = bop_1037
output2 = bop_1037
func_1047 = relay.Function([var_1036,], output)
mod['func_1047'] = func_1047
mod = relay.transform.InferType()(mod)
var_1048 = relay.var("var_1048", dtype = "int64", shape = (9, 3, 7))#candidate|1048|(9, 3, 7)|var|int64
output = func_1047(var_1048)
func_1049 = relay.Function([var_1048], output)
mutated_mod['func_1049'] = func_1049
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1575 = relay.const([[[-1.008984,-0.215815,8.790905,-8.616793],[-9.586216,-4.621561,-3.766064,0.578889],[5.319043,3.090004,8.586981,-1.813065],[1.009879,2.870818,-9.557225,9.582036],[7.677362,-3.111961,-1.581228,-8.951753],[3.069475,-6.379572,-3.148941,9.256634],[-3.989015,-0.252276,-7.466580,5.649576],[-7.098169,-4.960173,2.201695,4.620718],[3.643061,2.920414,-2.850403,-8.860902],[-4.878774,6.457996,-5.046194,-4.087375],[5.880152,9.048603,7.635033,9.494640],[4.121233,-5.057469,2.375183,-8.915458],[-9.277508,-8.842204,1.381987,-7.861516],[-0.015899,-6.672757,-2.499648,4.244638],[-4.657032,-8.235357,3.098403,0.824488]],[[4.846567,-5.354781,-7.021961,1.000316],[-8.479152,8.939743,3.778428,-7.411916],[-4.191180,-2.506524,8.359676,-9.667202],[-2.253585,-4.772311,8.538202,7.746438],[4.729209,9.679491,-9.056477,-5.681657],[9.955739,-0.555773,-6.800009,-5.255010],[3.916461,3.148543,-8.916189,-9.138198],[-4.779561,-2.136971,5.543935,-0.852916],[2.905279,-3.307107,4.295358,8.718614],[-0.766374,6.859262,-1.525478,3.501584],[-5.436155,-8.792825,1.363399,-8.687210],[7.766772,3.888084,-9.789747,-6.290329],[6.969019,5.228964,4.727769,6.676989],[-7.545723,-0.923291,-1.452223,-1.570845],[8.280809,1.794945,-0.332651,-4.407740]],[[3.422563,-3.501800,-8.256523,1.376858],[3.592547,-5.810156,5.657283,-8.594825],[-7.096045,-6.397354,4.540233,4.860832],[-7.494040,3.730872,-2.402832,-0.002848],[7.502232,6.717269,9.712085,8.785838],[0.320014,-7.576976,-6.576055,-6.360474],[7.081996,1.484865,-7.883611,3.665818],[-9.071411,4.471048,5.331726,-3.985017],[-9.782360,-2.580019,-1.142756,-9.792541],[5.814527,2.799109,1.015063,-9.797650],[-2.227285,2.216823,-8.718935,7.741657],[8.974748,-9.323236,7.691291,8.159470],[-0.096427,9.746956,-5.946910,0.387670],[-1.001037,8.530510,-7.346113,1.297187],[4.569842,8.655064,8.264805,-6.232618]],[[5.095879,9.479174,7.524763,-3.076545],[-3.316824,0.318301,2.444834,-6.164164],[8.403821,-9.866730,1.446725,-1.172635],[-8.752355,0.442842,9.176069,3.983614],[-7.854886,4.775674,6.846921,1.975349],[1.321441,-3.440556,6.529203,7.046225],[-3.080138,8.446064,2.720215,1.550972],[3.278653,3.516946,-9.430173,-0.424894],[-3.205434,7.841590,3.763120,7.651718],[5.118408,-2.371437,4.374465,1.381324],[0.190106,9.662489,-0.742429,-5.766749],[2.110013,-4.639874,-1.882280,-9.520640],[-1.592119,8.433209,5.863696,8.054227],[-5.278505,7.671901,4.895986,-7.451696],[2.541108,3.431913,-6.213953,-6.548609]],[[0.858217,3.214107,2.843160,-4.948287],[0.191850,1.376688,4.871389,6.540750],[-3.516995,0.105344,9.932432,-0.385877],[5.609302,1.379694,-8.721389,-7.058850],[-2.091608,8.013033,1.420021,-5.669392],[8.697208,7.216577,-6.584594,0.429811],[-1.114549,-2.226485,-2.914617,-6.571557],[-3.848243,5.854384,2.093797,-0.611652],[7.188710,7.302366,-4.883828,-3.516710],[-7.647308,-7.638194,-0.576935,0.342446],[-8.237355,6.844036,6.840413,-6.640357],[5.895624,-0.877805,8.595122,-0.882033],[-6.448789,-3.498965,1.723405,4.355083],[-6.703851,-4.839393,4.468443,7.013859],[9.023289,-8.205007,9.946495,-8.785331]],[[-7.621310,2.440100,-4.789441,-5.886205],[-4.612129,5.863277,7.524068,4.931428],[-5.748634,8.548722,1.064870,8.116271],[0.925633,7.985972,-4.179812,5.012901],[-6.811302,2.869260,-7.667094,-7.300530],[-7.941014,3.669836,-9.930023,3.608440],[-0.437264,-8.585650,-2.571614,3.287567],[1.045290,-1.592893,-2.328235,-2.887487],[-3.563254,7.593780,3.254598,0.057116],[7.191615,-5.714995,6.805487,-2.735438],[-6.509859,-0.811001,-3.814799,-2.879903],[-8.286164,-1.971815,-0.026702,-4.560374],[-4.145628,3.327417,6.995990,0.662323],[1.709538,-4.112093,2.985206,2.797295],[8.432855,-7.738906,2.626596,2.218229]],[[8.419612,-4.900260,-0.713382,6.429434],[8.273444,-7.250169,2.617336,9.697947],[0.067584,-2.075825,7.862125,-7.800309],[8.468854,-3.462507,3.057973,-2.490702],[6.374363,-9.448262,0.661182,-4.241417],[6.616925,2.891421,-0.852495,9.094711],[-5.572117,0.025917,4.058925,-8.011413],[-3.395882,7.820859,-2.474057,9.880246],[1.276873,0.318538,3.595060,6.003098],[1.657881,9.004679,4.977467,8.431442],[-9.251875,4.180168,8.904155,-1.018812],[0.153143,9.044973,-4.134118,5.271682],[9.797095,-2.523086,9.817552,8.910762],[6.710623,-6.736232,0.931748,-2.384699],[-1.005529,-5.625830,-6.257154,-1.283490]],[[-7.964676,3.978074,-4.566629,-4.500151],[-8.121643,-1.105239,-4.068277,-6.647949],[-7.454627,3.026369,-2.208980,-2.762955],[7.689690,-1.916885,4.140284,6.696969],[0.150818,-8.010826,-0.238893,7.448277],[-5.284637,-7.479882,0.365490,-9.754661],[3.165071,5.646613,4.761125,6.584759],[-7.935537,-5.566224,-2.451229,-6.524104],[4.860327,4.882976,3.075888,-1.981147],[-6.328642,8.216620,1.166230,7.295197],[6.061864,-4.181833,-7.068623,7.750307],[-8.829071,3.233293,-1.526144,-4.803192],[-5.952404,1.570499,-3.184580,9.920072],[-3.035471,-7.648064,-3.538396,-8.457645],[-9.368189,3.588545,-9.573076,-5.614978]],[[-3.661372,1.020451,8.637311,-8.135525],[1.089916,3.810888,0.699487,-5.656289],[6.624067,6.320312,2.580787,4.836495],[0.841390,-0.581091,-5.466152,-5.847957],[-8.654085,6.596970,6.792784,-7.300472],[9.607587,-3.959576,-4.420266,-6.208404],[3.876229,-3.675746,6.255201,-1.668135],[-8.347366,3.482420,7.377345,4.388525],[5.278706,8.433953,4.401517,-7.501421],[-4.250225,4.719467,3.953757,-9.003905],[-3.281092,8.715717,8.167964,-7.464299],[9.516020,-1.929580,2.604174,-4.678937],[-4.300688,2.278259,4.591051,-8.092778],[-4.751921,8.494987,3.540351,-2.356483],[-8.830054,1.595896,0.052756,4.976451]],[[8.050512,-3.618448,8.321092,-3.148923],[-0.034671,5.249934,1.033901,9.801311],[-7.483601,0.607120,2.200252,0.397946],[-1.932639,2.347180,-6.025495,-9.043604],[-3.189502,-1.840977,1.693011,6.060020],[-5.562962,-3.279242,-2.412569,1.870654],[-5.271328,-0.342241,-6.258527,7.134842],[-1.035707,-3.266604,0.063764,4.677100],[6.415633,4.303072,-4.301588,7.646707],[-0.376785,-9.665343,2.321264,8.253958],[-7.662805,7.013159,3.113711,6.683419],[4.072585,-7.774604,-6.488643,-4.527124],[9.243370,8.957867,-9.307662,-4.408535],[-4.827984,7.853948,-1.486771,9.212585],[-1.430663,6.660746,5.548520,-4.849837]],[[-7.636213,9.438659,-2.976983,9.877403],[7.563952,5.426257,2.076070,-6.225850],[-3.235903,0.137621,-5.876607,6.274258],[-3.836880,-3.427874,-0.056383,-4.785888],[2.574320,3.326007,-6.976504,5.025816],[5.351147,2.344614,-9.641920,-3.932592],[-6.444223,1.979697,-0.415880,0.865069],[5.999671,-7.743566,-6.880068,3.193488],[-5.202156,0.358057,8.240779,2.150663],[9.778381,4.256803,-9.870320,-6.828413],[5.062524,-7.533232,2.944582,-4.464825],[5.853492,-7.511013,-6.263084,-4.684910],[-6.390656,3.547050,-5.011697,7.468936],[9.466321,-5.733692,-3.080475,-8.363704],[-6.078499,-7.595520,1.845934,4.803809]],[[9.920748,-7.000077,7.431442,5.387098],[7.011929,2.210162,4.668857,1.741136],[7.485737,-4.184732,3.362086,9.251409],[9.212143,2.950316,9.841317,-5.403148],[-6.689269,-5.545730,3.271388,4.857767],[-3.557142,-3.961356,3.791228,-1.339356],[2.555120,1.215968,-6.570698,4.640635],[-3.124561,-6.414810,1.745570,-2.096454],[0.822271,3.699930,-9.832543,1.473552],[8.374661,-4.057336,-1.959376,0.830271],[-6.543004,-8.644204,3.689463,-3.226318],[-5.544176,2.259683,7.053188,9.003001],[-9.589704,4.864492,4.861814,2.408110],[5.390038,-7.607659,6.063009,0.241558],[-1.467613,-7.994620,4.402545,6.196042]]], dtype = "float64")#candidate|1575|(12, 15, 4)|const|float64
uop_1576 = relay.sqrt(const_1575.astype('float64')) # shape=(12, 15, 4)
func_1047_call = mod.get_global_var('func_1047')
func_1049_call = mutated_mod.get_global_var('func_1049')
var_1581 = relay.var("var_1581", dtype = "int64", shape = (189,))#candidate|1581|(189,)|var|int64
call_1580 = func_1047_call(relay.reshape(var_1581.astype('int64'), [9, 3, 7]))
call_1582 = func_1047_call(relay.reshape(var_1581.astype('int64'), [9, 3, 7]))
func_904_call = mod.get_global_var('func_904')
func_907_call = mutated_mod.get_global_var('func_907')
const_1585 = relay.const([3.977935,-8.274637,7.328850,6.123225,-8.682967,6.821489,-7.038177,2.385638,-8.280494,1.683282,2.008353,-9.180303,4.499463,-2.463557,-4.296335,-7.847099,1.944958,9.564690,-1.623977,-8.308021,-2.234161,-2.711039,4.149605,-8.711765,-7.149827,9.872718,-6.096087,-8.535958,-6.028730,7.537182,-5.418663,1.465266,-5.701535,6.192090,7.386064,6.806035,7.619262,-5.539849,2.242378,-2.795080,-9.983533,-6.609011,4.397258,-1.969736,0.854615,-7.760665,3.052671,3.584039,-5.015739,-7.599659,-2.155292,-4.591984,4.974013,1.873451,1.775239,9.915716,1.508502,6.031498,-1.126289,-5.340501,9.245190,2.272979,-0.239804,-8.546690,4.832550,3.712561,-9.192866,9.324883,-0.722953,4.666316,-2.888089,-8.792815,-6.107131,7.314581,5.086488,-5.650230,-5.171823,-7.259429,-8.683526,-5.722832,4.470121,9.365395,0.808261,-6.317673,0.690726,8.482057,-7.924268,2.270580,3.199646,1.920503,6.763671,6.530835,1.419692,-2.672941,-1.418773,-8.985053,-5.169831,-5.422633,-0.357356,-2.970713,-2.243659,-4.810347,2.569417,3.000627,-6.405714,1.023495,-2.948814,4.368556,-3.862028,0.091373,-0.840922,5.688398,5.080995,-3.097251,-3.404545,-7.906227,2.821103,1.140904,-9.059426,0.430275,8.080604,-8.579438,-1.494057,8.908577,-4.155704,2.326891,-1.059616,7.936786,-2.353987,-3.073198,-7.495937,8.050651,5.293109,-5.819627,8.190168,-9.322351,8.649838,-9.249721,-0.478703,-8.681233,-2.335092,-9.854591,-0.727667,3.274960,1.089778,8.839773,-6.248629,0.339875,3.491332,5.251912,-8.703135,7.393739,1.541185,9.099460,-1.662304,-5.785398,3.462221,7.993303,-8.527323,0.360487,-3.317287,-7.461686,0.342465,-5.926736,1.905763,-9.652489,0.064047,3.440690,2.126693,8.547201,6.259126,2.383386,-7.772497,-5.778850,8.315758,-1.549777,5.367233,-3.850801,5.995753,8.207752,-5.981274,-1.594216], dtype = "float64")#candidate|1585|(182,)|const|float64
call_1584 = relay.TupleGetItem(func_904_call(relay.reshape(const_1585.astype('float64'), [2, 7, 13])), 0)
call_1586 = relay.TupleGetItem(func_907_call(relay.reshape(const_1585.astype('float64'), [2, 7, 13])), 0)
func_108_call = mod.get_global_var('func_108')
func_111_call = mutated_mod.get_global_var('func_111')
var_1588 = relay.var("var_1588", dtype = "uint16", shape = (234,))#candidate|1588|(234,)|var|uint16
call_1587 = func_108_call(relay.reshape(var_1588.astype('uint16'), [2, 13, 9]))
call_1589 = func_108_call(relay.reshape(var_1588.astype('uint16'), [2, 13, 9]))
output = relay.Tuple([uop_1576,call_1580,var_1581,call_1584,const_1585,call_1587,var_1588,])
output2 = relay.Tuple([uop_1576,call_1582,var_1581,call_1586,const_1585,call_1589,var_1588,])
func_1618 = relay.Function([var_1581,var_1588,], output)
mod['func_1618'] = func_1618
mod = relay.transform.InferType()(mod)
mutated_mod['func_1618'] = func_1618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1618_call = mutated_mod.get_global_var('func_1618')
var_1620 = relay.var("var_1620", dtype = "int64", shape = (189,))#candidate|1620|(189,)|var|int64
var_1621 = relay.var("var_1621", dtype = "uint16", shape = (234,))#candidate|1621|(234,)|var|uint16
call_1619 = func_1618_call(var_1620,var_1621,)
output = call_1619
func_1622 = relay.Function([var_1620,var_1621,], output)
mutated_mod['func_1622'] = func_1622
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1789 = relay.var("var_1789", dtype = "uint16", shape = (7, 9, 15))#candidate|1789|(7, 9, 15)|var|uint16
var_1790 = relay.var("var_1790", dtype = "uint16", shape = (7, 9, 15))#candidate|1790|(7, 9, 15)|var|uint16
bop_1791 = relay.bitwise_and(var_1789.astype('uint16'), relay.reshape(var_1790.astype('uint16'), relay.shape_of(var_1789))) # shape=(7, 9, 15)
output = bop_1791
output2 = bop_1791
func_1798 = relay.Function([var_1789,var_1790,], output)
mod['func_1798'] = func_1798
mod = relay.transform.InferType()(mod)
mutated_mod['func_1798'] = func_1798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1798_call = mutated_mod.get_global_var('func_1798')
var_1800 = relay.var("var_1800", dtype = "uint16", shape = (7, 9, 15))#candidate|1800|(7, 9, 15)|var|uint16
var_1801 = relay.var("var_1801", dtype = "uint16", shape = (7, 9, 15))#candidate|1801|(7, 9, 15)|var|uint16
call_1799 = func_1798_call(var_1800,var_1801,)
output = call_1799
func_1802 = relay.Function([var_1800,var_1801,], output)
mutated_mod['func_1802'] = func_1802
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2260 = relay.var("var_2260", dtype = "uint8", shape = ())#candidate|2260|()|var|uint8
var_2261 = relay.var("var_2261", dtype = "uint8", shape = (9, 9, 15))#candidate|2261|(9, 9, 15)|var|uint8
bop_2262 = relay.right_shift(var_2260.astype('uint8'), var_2261.astype('uint8')) # shape=(9, 9, 15)
bop_2267 = relay.less(var_2261.astype('bool'), var_2260.astype('bool')) # shape=(9, 9, 15)
output = relay.Tuple([bop_2262,bop_2267,])
output2 = relay.Tuple([bop_2262,bop_2267,])
func_2276 = relay.Function([var_2260,var_2261,], output)
mod['func_2276'] = func_2276
mod = relay.transform.InferType()(mod)
mutated_mod['func_2276'] = func_2276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2276_call = mutated_mod.get_global_var('func_2276')
var_2278 = relay.var("var_2278", dtype = "uint8", shape = ())#candidate|2278|()|var|uint8
var_2279 = relay.var("var_2279", dtype = "uint8", shape = (9, 9, 15))#candidate|2279|(9, 9, 15)|var|uint8
call_2277 = func_2276_call(var_2278,var_2279,)
output = call_2277
func_2280 = relay.Function([var_2278,var_2279,], output)
mutated_mod['func_2280'] = func_2280
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2508 = relay.var("var_2508", dtype = "float64", shape = (8, 13, 5))#candidate|2508|(8, 13, 5)|var|float64
uop_2509 = relay.atan(var_2508.astype('float64')) # shape=(8, 13, 5)
bop_2515 = relay.floor_mod(uop_2509.astype('float32'), relay.reshape(var_2508.astype('float32'), relay.shape_of(uop_2509))) # shape=(8, 13, 5)
func_2276_call = mod.get_global_var('func_2276')
func_2280_call = mutated_mod.get_global_var('func_2280')
var_2521 = relay.var("var_2521", dtype = "uint8", shape = ())#candidate|2521|()|var|uint8
var_2522 = relay.var("var_2522", dtype = "uint8", shape = (81, 15))#candidate|2522|(81, 15)|var|uint8
call_2520 = relay.TupleGetItem(func_2276_call(relay.reshape(var_2521.astype('uint8'), []), relay.reshape(var_2522.astype('uint8'), [9, 9, 15]), ), 1)
call_2523 = relay.TupleGetItem(func_2280_call(relay.reshape(var_2521.astype('uint8'), []), relay.reshape(var_2522.astype('uint8'), [9, 9, 15]), ), 1)
func_108_call = mod.get_global_var('func_108')
func_111_call = mutated_mod.get_global_var('func_111')
var_2526 = relay.var("var_2526", dtype = "uint16", shape = (234,))#candidate|2526|(234,)|var|uint16
call_2525 = func_108_call(relay.reshape(var_2526.astype('uint16'), [2, 13, 9]))
call_2527 = func_108_call(relay.reshape(var_2526.astype('uint16'), [2, 13, 9]))
output = relay.Tuple([bop_2515,call_2520,var_2521,var_2522,call_2525,var_2526,])
output2 = relay.Tuple([bop_2515,call_2523,var_2521,var_2522,call_2527,var_2526,])
func_2535 = relay.Function([var_2508,var_2521,var_2522,var_2526,], output)
mod['func_2535'] = func_2535
mod = relay.transform.InferType()(mod)
var_2536 = relay.var("var_2536", dtype = "float64", shape = (8, 13, 5))#candidate|2536|(8, 13, 5)|var|float64
var_2537 = relay.var("var_2537", dtype = "uint8", shape = ())#candidate|2537|()|var|uint8
var_2538 = relay.var("var_2538", dtype = "uint8", shape = (81, 15))#candidate|2538|(81, 15)|var|uint8
var_2539 = relay.var("var_2539", dtype = "uint16", shape = (234,))#candidate|2539|(234,)|var|uint16
output = func_2535(var_2536,var_2537,var_2538,var_2539,)
func_2540 = relay.Function([var_2536,var_2537,var_2538,var_2539,], output)
mutated_mod['func_2540'] = func_2540
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3190 = relay.const([[[3.201158,8.502741,-9.667194,2.011000,6.536183,-5.090483,8.494683,2.764772,-5.048921,-4.918584,-6.823730,5.861705,-1.017544],[2.610811,4.530300,-2.626421,4.681065,-3.069114,3.532354,2.291467,-6.795778,2.491069,-4.976772,6.165104,-9.412031,-3.141132],[6.270278,9.813856,-0.854263,1.066576,6.258707,-5.220963,1.476887,-8.686904,-5.890393,-5.236942,6.421134,-7.159669,-5.609461]],[[-3.216756,7.037552,-9.995909,-1.642207,-6.854017,-2.259034,6.224658,4.853335,-0.122899,-1.506986,4.125951,1.972395,7.852716],[-8.197351,-4.044394,-0.826643,7.226780,4.892624,-5.037073,9.827812,0.169511,-1.243814,8.893742,-1.561572,2.502958,-6.140489],[-9.970635,-3.782668,-7.572492,9.911364,8.927604,-8.633993,-7.548266,-8.838376,7.130958,2.428074,-2.753138,7.439166,-6.615741]],[[7.637089,-4.610177,-6.701931,0.336047,9.774923,9.840450,-8.324341,-4.640523,-7.438855,6.959379,5.324506,-6.495001,6.487274],[-9.546550,5.100461,-3.668192,-6.075632,-9.886262,6.112752,6.651965,-0.818848,-6.842726,-7.839236,6.304439,2.468011,7.730009],[7.672550,3.510575,-7.178734,-9.552165,-9.540151,6.295649,8.724895,-2.579852,3.637845,4.594806,-0.734228,4.155148,-7.410084]],[[7.459952,8.525071,-0.633853,5.568080,1.003655,-0.369181,8.024311,-0.469789,6.820451,-5.624240,1.158969,-3.942045,0.331554],[-1.455124,0.789325,0.361270,-4.681535,4.984479,-2.987484,-1.171937,7.578394,1.580175,-3.265662,4.195328,1.168081,7.228405],[1.701535,-4.604015,-1.200109,6.298395,4.248198,3.357130,7.518543,3.804766,0.432318,2.731573,-0.068931,2.254348,7.674552]],[[-1.098596,-1.655022,5.526433,6.729921,0.198704,-8.500889,5.760801,0.990059,9.802078,-3.873937,-8.811357,-7.634342,-0.350024],[-6.620421,5.131134,-8.301049,9.563349,4.230313,-0.756710,-6.796544,6.891023,9.144177,-1.773316,8.869621,1.478085,-7.524456],[7.677721,-4.834292,9.156135,7.159641,-9.274297,3.547692,-1.072229,-9.803299,4.652941,-4.311621,0.207236,-6.822713,3.457199]],[[2.028695,4.177179,-2.982876,-5.122789,-8.308935,-4.599752,1.978818,2.137244,-6.980309,2.705399,-6.186722,6.015490,2.297744],[-1.835019,-7.491027,6.306054,6.251913,-2.072002,7.571133,-0.127253,-0.814435,4.257107,4.354638,-1.267895,0.552837,-8.347171],[2.229744,-8.088336,-3.603124,-4.680768,-9.857772,-4.719854,-5.710059,-8.871106,9.798688,1.238048,8.837568,3.757320,9.924434]],[[-3.953158,-4.805968,-8.568306,-3.866525,-1.670269,-3.030692,7.696230,9.614368,-7.305999,-8.689728,9.702464,8.801438,-7.502096],[-1.827544,9.103324,5.695504,-8.176776,-9.147175,5.569200,9.891555,9.455703,-1.907354,4.200643,-5.863408,4.274103,-3.319398],[-9.488525,5.192632,-6.849905,7.652565,8.793853,1.857801,-7.195346,7.289689,-1.737086,9.705693,-8.001443,-7.638042,7.859513]],[[3.647919,-1.226234,-4.136303,9.206968,4.519713,8.811603,8.026089,4.859690,-3.562464,-8.937827,-8.043742,-9.695899,-6.861690],[7.988004,-1.106698,9.031955,-4.937059,9.499536,-7.358218,-0.879084,-9.848900,-8.569343,2.899769,-7.686878,3.603452,6.977312],[2.123379,-2.777282,-3.610532,0.184341,-7.521557,-5.578062,-2.371863,1.838826,-5.787560,-6.931420,2.231976,-8.859877,-3.582934]],[[-4.724085,6.548358,3.438364,-3.817465,-4.258284,-8.889458,7.883289,-9.747321,6.250435,-5.305085,3.143127,-0.695226,6.055266],[0.035935,-1.962277,7.997057,9.243382,-0.159096,1.943344,-6.355078,8.555853,0.938307,-2.092416,-4.445145,-0.917945,-6.571122],[0.351802,3.140426,2.306074,-6.132595,5.315384,-0.672363,-9.963373,9.569901,4.531601,1.511524,-9.011505,-2.396181,-4.142645]],[[-0.326964,8.080826,2.087593,-9.729231,8.887307,4.150306,0.481329,0.325803,0.090262,3.445758,-4.697866,4.949297,2.901821],[-5.107230,-5.222752,3.393959,-1.794472,4.731023,9.070081,-8.519096,0.843689,0.980895,-5.814932,6.754797,-2.957234,2.171433],[6.672749,6.649710,-6.802298,-1.769733,-0.305755,-7.503789,-0.521950,-7.910129,7.982884,2.418079,-6.613413,1.577643,0.927809]],[[2.815470,0.277816,-1.322622,0.346178,-9.034924,-5.610629,-0.995158,-8.321284,7.030555,-2.425514,-6.624687,-6.892864,7.249786],[-6.861779,-7.695800,4.759536,-9.285465,-0.293960,9.023597,-6.329634,8.844707,2.542501,6.794376,-8.608654,-8.558904,5.223580],[-8.920466,-3.393679,-1.740932,6.030014,4.704931,-8.371459,5.293921,-6.270523,-7.433007,-0.305770,1.774186,4.630873,8.319668]],[[2.493215,3.425390,7.914751,2.212893,6.433271,-4.653033,-6.641647,6.818798,5.867473,5.825000,5.816454,-9.959313,0.318787],[0.873451,3.872773,5.420514,9.438442,5.656184,-6.932516,-9.832346,-8.018725,-4.761842,-7.485729,-4.105216,6.373456,-9.571084],[4.238202,-1.655303,-5.802636,-9.041656,5.322028,9.220301,-1.972599,2.549806,9.913109,-8.320723,-8.712138,-7.973428,-0.662229]],[[0.350141,-9.742639,-6.568329,-5.706579,-6.678464,9.030986,-1.732175,-7.531379,9.604711,-6.562354,-6.187038,-2.750324,-2.078378],[5.821273,-7.087256,4.208929,3.074399,0.180104,1.853691,5.186775,-2.735163,-5.810301,3.048508,-3.803285,7.466927,2.942026],[-7.014435,-1.284884,-0.492911,9.065780,2.827178,-0.644633,-6.939406,4.474975,-0.242514,-6.392587,3.377995,9.368427,3.128904]]], dtype = "float64")#candidate|3190|(13, 3, 13)|const|float64
uop_3191 = relay.erf(const_3190.astype('float64')) # shape=(13, 3, 13)
func_1618_call = mod.get_global_var('func_1618')
func_1622_call = mutated_mod.get_global_var('func_1622')
var_3194 = relay.var("var_3194", dtype = "int64", shape = (189,))#candidate|3194|(189,)|var|int64
const_3195 = relay.const([5,2,-5,-9,6,-2,-7,-8,-4,3,-2,-5,2,2,-1,2,5,2,-8,-2,1,9,-9,-8,10,4,-4,5,-4,-9,-3,3,-8,-9,5,1,5,5,4,10,7,-8,-3,-6,-9,4,-9,-10,-1,3,10,2,-3,1,4,-3,-5,1,-3,7,-5,4,9,1,4,-5,-8,-10,-8,2,2,3,6,7,5,3,-6,-4,-4,-4,8,1,-8,1,-1,8,-6,-3,6,-6,-6,9,-10,7,-7,-10,-2,-5,3,-8,6,-10,-6,-9,-4,3,5,-2,-6,-7,-1,10,-10,-6,10,7,-10,8,-9,8,1,-3,-5,1,3,-4,5,-10,10,9,-9,-6,3,-5,-3,6,-6,10,4,-3,-9,3,-3,-2,10,3,-8,-8,-4,-3,-10,3,-8,7,6,10,7,1,8,-4,-5,-8,7,3,-3,-10,-7,-6,6,8,-3,7,-2,1,2,-8,2,9,6,-1,-8,9,-4,10,-10,1,-9,-5,-7,-2,-10,5,8,1,5,10,-3,-9,-6,6,-9,1,-5,10,-3,-10,-3,-6,10,7,-1,9,8,2,8,1,-5,7,1,2,10,-10,9,-7,3,-6,-3,-10,-4,-6,-10,-4,-1,5], dtype = "uint16")#candidate|3195|(234,)|const|uint16
call_3193 = relay.TupleGetItem(func_1618_call(relay.reshape(var_3194.astype('int64'), [189,]), relay.reshape(const_3195.astype('uint16'), [234,]), ), 3)
call_3196 = relay.TupleGetItem(func_1622_call(relay.reshape(var_3194.astype('int64'), [189,]), relay.reshape(const_3195.astype('uint16'), [234,]), ), 3)
func_629_call = mod.get_global_var('func_629')
func_632_call = mutated_mod.get_global_var('func_632')
const_3208 = relay.const([-3.363156,-1.585626,-3.050756,-7.343209,-8.318283,-1.163995,-2.163212,-3.280096,-0.682364,5.629562,6.951416,-4.705300,0.147650,2.675196,-4.498841,7.269358,8.144637,9.467427,2.145157,4.455943,4.565972,5.756602,9.004908,-0.509892,8.426296,-1.444481,-8.315710,-2.097165,-9.798738,-3.575034,-4.542482,5.042427,-7.556004,5.785633,5.069241,1.276439,-3.137761,-0.464178,-7.671787,-1.183863,-8.413660,-6.647709,0.911387,-6.522648,-3.543721,-3.933964,3.816368,-7.119886,-4.693964,5.687449,-4.121804,-8.428651,-9.190397,-5.385708,7.721833,-2.925060,-7.563967,9.799727,3.459546,1.879824,-1.814658,-8.415353,-2.691834,7.796642,0.938237,-5.402122,5.418422,-1.228221,9.204560,-6.415889,6.547633,-8.723809,2.602927,8.101278,-2.384670,-5.530474,2.811367,-0.291561,1.809716,-4.790731,-1.426015,-4.163464,-3.055921,7.023553,-4.473497,-7.258769,0.777073,1.840322,-4.415256,8.259183,0.108149,-4.998715,4.361745,-8.688262,-6.256364,9.921090,7.923974,7.786367,-4.969931,1.374209,-3.449179,2.581256,8.987404,8.859685,5.095995,-4.220353,-3.494616,9.511293,4.378332,8.965719,6.407983,-2.282367,-8.158497,-9.447353,6.487036,7.933390,1.307254,3.514197,5.573779,8.978852,1.010859,-4.556174,-1.167975,2.345022,0.498581,2.820902,8.380627,-9.466797,3.931933,7.029847,-6.341553,9.155910,8.140192,-7.282966,1.200411,1.462153,2.427649,-7.772612,-1.872768,4.992553,-6.930324,-8.076909,6.230563,-4.069381,4.319320,1.169827,-4.482233,9.790129,2.155563,7.499313,7.183015,2.801533,-8.970432,-7.521933,-7.224238,-3.860304,8.129589,-9.300248,2.220988,6.892643,-2.989428,3.721515,2.156455,-8.242833,-6.145966,5.682454,7.392934,8.571808,3.868151,-7.981156,6.513825,-2.944010,4.252077,3.818674,5.703236,8.586572,4.825955,3.844782,5.726331,6.923407,1.216608,-7.411877,-3.929949,-4.214363,2.897784,6.098501,0.306975,5.204189,-7.741063,-4.221000,-8.928627,-8.131627,-4.651978,-4.893887,3.254986,8.475393,2.472785,6.509646,5.738974,0.690943,-5.402379,-4.199546,-6.890440,-8.231011,-4.981136,0.242949,-7.746139,0.393486,6.385088,5.958632,8.818379,6.369653,-4.874760,-3.345635,-0.478664,-0.580236,-5.241042,-6.707756,9.239661,-9.844826,9.597951,-5.557514,0.998551,-7.666080,1.283040,2.221944,1.368506,4.902065,-6.272543,3.262453,9.794018,3.663235,-1.989911,6.679618,2.536805,-4.222765,2.457772,-0.627259,-8.552432,9.902550,-3.810485,-2.954042,5.791062,7.657465,-2.444507,-8.355742,7.166386,2.908016,4.145509,5.503296,-0.937332,-5.783671,-5.237168,-7.061171,9.658027,-8.241747,6.058372,0.032882,8.508478,-9.942629,-3.088860,7.320507,-2.340158,2.223568,4.328745,-7.129258,-0.575169,3.125867,-6.380502,2.789815,3.768826,7.029862,7.663638,1.280658,-2.498408,-1.679226,-7.933361,-3.817096,-8.402613,2.569554,-7.217736,-7.456709,-4.065879,3.869072,7.453191,-5.099147,-6.943537,5.507790,0.827435,-0.038721,-5.965811,-8.638411,3.819419,-0.375734,-0.691005,7.816725,3.152796,-5.883546,-0.109760,-4.284859,-6.795622,-4.646795,0.507984,-2.998789,2.337558,-7.200117,8.143014,-9.540824,8.780571,2.790227,-3.061526,-6.522450,-0.207563,7.372829,-5.426876,-0.509022,9.852656,7.632597,5.119519,1.054111,2.280540,-8.876740,-2.091189,1.567709,4.458932,7.775010,4.435541,-7.934945,-2.398534,-1.172035,0.797526,-5.442393,-5.934132,7.048657,4.252793,-4.981226,-5.815514,-4.106652,5.954107,-4.030525,-3.618670,8.726107,8.837011,4.477784,9.483293,-2.756067,-4.189089,2.451648,6.277190,-5.396466,3.480251,5.084984,-3.547835,-2.962721,8.064482,-3.393229,9.240863,9.276451,2.549445,-6.968309,3.072049,-0.976967,8.212988,-0.244079,-0.486445,-4.833451,7.377500,-0.220132,1.515002,1.920293,1.633871,-1.403037,1.959971,-9.605369,-6.962605,-0.639975,5.127885,2.268501,-6.335605,2.968065,8.300289,2.699760,6.209377,-6.247754,-2.710159,5.497010,7.379355,-1.200215,-5.393470,-0.053180,-0.035506,-3.835774,5.196765,-7.843791,5.359213,-0.041591,0.236087,9.638701,9.390215,2.637130,3.230606,-3.898116,-5.299158,-7.841851,0.049464,2.695148,8.090400,9.021859,-8.929999,-9.861276,-2.894719,-4.457769,-0.913016,-0.690218,6.168272,-9.364245,3.242507,8.185883,0.860206,-4.070610,-0.224459,-3.274759,2.711652,-0.508526,-5.338369,6.410932,-9.830720,-1.487703,7.257644,-6.741964,3.169318,6.151393,8.860831,-8.735085,-7.229134,2.171380,3.970791,-1.035413,-0.954892,-6.945663,-0.876237,1.224915,1.046079,3.457595,-6.094732,1.494603,-6.177985,-1.599958,8.804964,7.280129,2.175629,6.019583,-9.355509,7.711720,-4.496066,8.633615,9.135533,7.967119,2.896360,0.033935,3.212393,2.518636,-0.017391,1.100986,-7.455333,2.079919,-4.748981,-5.692822,3.865157,4.604444,5.890291,-0.990744,6.365014,0.603028,-1.842116,-6.168270,3.668361,-2.639269,-2.832529,-0.987228,-9.653527,-5.490642,-0.780935,7.369036,6.737288,6.685292,-9.026827,7.205844,-3.583486,-7.869419,-0.090701,-2.015043,-4.676501,5.447230,-0.277066,4.025341,7.375638,9.241240,7.793899,9.976852,7.825126,2.768411,-3.604854,9.084481,-0.874597,-2.586664,5.054967,-6.942474,7.249149,-7.342763,5.966716,-7.535192,1.827991,-8.001868,-9.512350,0.184407,4.705763,0.931239,-1.628860,-5.938826,-3.537336,6.405809,3.030151,3.844722,8.461851,-8.273013,-9.588022,4.116333,6.425140,-2.305696,-9.902259,3.071818,-8.311839,9.916403,-2.699344,9.930502,-7.587267,-8.498491,8.083070,-5.757277,9.602679,4.010331,7.251521,3.680396,0.418265,3.586700,-5.762553,0.960225,2.103449,6.287751,-4.353255,4.990852,7.184567,-7.978721,5.605939,1.167796,3.672578,-5.805357,4.926050,9.818156,1.611455,-3.595528,-4.992321,9.675443,5.262344,2.264909,5.761295,-4.769787,-2.699204,5.093794,-8.242210,-5.073671,-7.541773,-3.942904,-4.359730,-3.142131,-7.437753,9.255779,-4.992023,5.177221,4.489649,8.451392,4.430416,8.552227,-0.661707,3.055631,5.545393,-1.829027,3.570595,-0.166425,9.214610,3.397916,8.009785,-8.944352,0.130945,3.554451,-1.800620,-5.380320,9.927960,3.901268,-1.099114,-0.766800,-9.763179,1.496985,3.432884,7.038994,-7.231173,1.016289,-6.962393,7.324994,0.935944,-0.367415,0.115165,6.192269,2.967709,-0.679972,3.846621,7.475067,-8.001662,1.405030,-5.504987,-0.933736,-4.622266,0.696416,6.550333,-1.756167,3.984968,-1.077769,1.299186,6.850283,-3.364994,7.128452,-2.562346,2.438932,9.714189,0.135980,2.167456,8.894530,6.256565,-0.219965], dtype = "float32")#candidate|3208|(640,)|const|float32
call_3207 = relay.TupleGetItem(func_629_call(relay.reshape(const_3208.astype('float32'), [10, 4, 16])), 2)
call_3209 = relay.TupleGetItem(func_632_call(relay.reshape(const_3208.astype('float32'), [10, 4, 16])), 2)
func_499_call = mod.get_global_var('func_499')
func_501_call = mutated_mod.get_global_var('func_501')
call_3217 = relay.TupleGetItem(func_499_call(relay.reshape(call_3207.astype('bool'), [16, 14, 14])), 0)
call_3218 = relay.TupleGetItem(func_501_call(relay.reshape(call_3207.astype('bool'), [16, 14, 14])), 0)
output = relay.Tuple([uop_3191,call_3193,var_3194,const_3195,call_3207,const_3208,call_3217,])
output2 = relay.Tuple([uop_3191,call_3196,var_3194,const_3195,call_3209,const_3208,call_3218,])
func_3221 = relay.Function([var_3194,], output)
mod['func_3221'] = func_3221
mod = relay.transform.InferType()(mod)
mutated_mod['func_3221'] = func_3221
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3222 = relay.var("var_3222", dtype = "int64", shape = (189,))#candidate|3222|(189,)|var|int64
func_3221_call = mutated_mod.get_global_var('func_3221')
call_3223 = func_3221_call(var_3222)
output = call_3223
func_3224 = relay.Function([var_3222], output)
mutated_mod['func_3224'] = func_3224
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3335 = relay.const([[[4,-5,-2,6,-4],[-9,2,1,6,-2],[-7,8,5,-4,-7],[-6,4,9,-6,-1],[6,5,-2,1,-2],[-8,5,10,1,-5],[-3,-9,-4,-1,3],[-3,2,6,-4,-1],[-9,5,4,-4,-1],[3,-1,1,3,6],[-3,-5,-6,-10,-10],[-7,9,-5,-9,-8],[-9,6,-7,7,-6]],[[6,-3,6,-3,-2],[-7,-4,-2,9,-7],[6,2,-7,-7,-9],[-1,-4,-5,6,9],[3,-8,2,5,3],[-2,7,9,5,10],[10,-6,-8,7,10],[-1,-1,9,8,7],[-3,10,-5,6,6],[-3,-9,-3,1,-2],[-7,2,-1,1,5],[3,-9,10,4,5],[3,-6,-6,-3,10]]], dtype = "uint16")#candidate|3335|(2, 13, 5)|const|uint16
const_3336 = relay.const([[[-6,10,-1,7,-6],[-5,-6,-5,3,-6],[-6,9,7,-3,10],[-10,-9,2,-3,-1],[5,-3,-4,1,-10],[10,-9,9,-10,-2],[-2,-7,-3,8,-7],[-4,-6,-3,-7,8],[3,-5,-8,-10,-7],[-9,5,10,4,-5],[-9,-3,-7,-5,-3],[4,-2,-8,-5,1],[9,3,-5,-3,2]],[[-1,-6,-6,-3,7],[-6,1,2,-2,-8],[-9,2,-2,-6,7],[-10,9,-3,10,7],[-1,10,5,-3,-9],[10,1,-3,-1,7],[-6,-6,-2,-1,-6],[-2,5,3,4,-7],[-9,2,-8,-3,3],[-9,-7,-4,-6,3],[-3,-3,5,-8,-1],[1,-1,10,-9,10],[-10,-8,4,6,-7]]], dtype = "uint16")#candidate|3336|(2, 13, 5)|const|uint16
bop_3337 = relay.minimum(const_3335.astype('uint16'), relay.reshape(const_3336.astype('uint16'), relay.shape_of(const_3335))) # shape=(2, 13, 5)
bop_3346 = relay.floor_mod(bop_3337.astype('float32'), relay.reshape(const_3336.astype('float32'), relay.shape_of(bop_3337))) # shape=(2, 13, 5)
output = bop_3346
output2 = bop_3346
func_3351 = relay.Function([], output)
mod['func_3351'] = func_3351
mod = relay.transform.InferType()(mod)
output = func_3351()
func_3352 = relay.Function([], output)
mutated_mod['func_3352'] = func_3352
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3375 = relay.var("var_3375", dtype = "float32", shape = (5, 7, 15))#candidate|3375|(5, 7, 15)|var|float32
var_3376 = relay.var("var_3376", dtype = "float32", shape = (5, 7, 15))#candidate|3376|(5, 7, 15)|var|float32
bop_3377 = relay.floor_mod(var_3375.astype('float32'), relay.reshape(var_3376.astype('float32'), relay.shape_of(var_3375))) # shape=(5, 7, 15)
output = relay.Tuple([bop_3377,])
output2 = relay.Tuple([bop_3377,])
func_3380 = relay.Function([var_3375,var_3376,], output)
mod['func_3380'] = func_3380
mod = relay.transform.InferType()(mod)
var_3381 = relay.var("var_3381", dtype = "float32", shape = (5, 7, 15))#candidate|3381|(5, 7, 15)|var|float32
var_3382 = relay.var("var_3382", dtype = "float32", shape = (5, 7, 15))#candidate|3382|(5, 7, 15)|var|float32
output = func_3380(var_3381,var_3382,)
func_3383 = relay.Function([var_3381,var_3382,], output)
mutated_mod['func_3383'] = func_3383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3351_call = mod.get_global_var('func_3351')
func_3352_call = mutated_mod.get_global_var('func_3352')
call_3455 = func_3351_call()
call_3456 = func_3351_call()
uop_3484 = relay.acos(call_3455.astype('float32')) # shape=(2, 13, 5)
uop_3486 = relay.acos(call_3456.astype('float32')) # shape=(2, 13, 5)
func_499_call = mod.get_global_var('func_499')
func_501_call = mutated_mod.get_global_var('func_501')
const_3489 = relay.const([True,True,True,True,True,True,False,False,False,True,False,False,False,False,True,True,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,False,True,True,False,False,True,True,True,True,False,False,True,False,False,False,True,False,True,False,False,True,True,True,True,False,False,True,False,False,True,False,False,False,True,True,False,True,False,True,False,False,True,True,False,True,True,True,False,True,False,False,False,True,True,False,False,True,True,False,True,False,False,False,False,True,True,False,False,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,False,False,False,False,True,True,False,True,True,False,True,True,False,False,False,False,True,False,True,False,True,False,True,False,True,False,True,True,True,False,False,False,False,False,False,False,False,True,True,True,True,False,True,True,False,True,False,True,True,True,True,False,True,False,True,True,True,False,False,False,True,False,False,True,True,True,True,True,False,False,False,True,False,True,True,False,False,True,True,True,False,False,False,True,True,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,False,False,True,False,True,False,True,False,True,False,True,True,True,True,True,False,False,True,False,False,False,False,False,False,True,False,False,True,False,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,False,True,True,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False,False,True,False,True,False,False,True,True,False,False,False,True,False,True,False,True,False,True,False,False,False,False,True,True,False,True,False,False,True,False,False,True,True,False,True,True,False,False,True,False,False,True,True,False,False,True,False,True,False,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,True,False,True,True,False,False,False,False,True,True,False,True,True,False,False,True,True,True,False,True,False,True,False,False,True,False,True,False,True,False,True,False,False,False,True,False,False,True,False,True,True,True,True,False,True,True,True,False,True,False,False,True,True,False,True,False,False,False,False,True,True,False,True,True,False,True,False,True,False,False,False,True,True,True,True,True,True,True,True,False,True,True,True,False,True,False,False,False,False,True,True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False,True,False,True,True,True,True,False,True,False,False,False,False,True,True,False,False,False,True,True,True,True,False,False,True,False,True,True,True,True,True,True,True,True,False,False,True,True,True,False,False,True,False,False,False,True,False,True,True,True,False,True,False,True,True,False,True,False,True,False,True,False,True,False,False,True,True,True,True,False,True,True,True,False,True,False,True,False,True,True,True,True,False,False,False,True,False,True,True,True,True,False,False,False,True,False,False,False,True,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,False,False,False,False,True,True,False,False,True,False,False,False,True,False,False,False,True,True,False,False,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,False,False,True,True,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,True,False,False,False,True,True,True,True,True,True,True,False,True,True,True,True,False,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,False,False,True,True,True,False,False,True,True,True,True,False,True,False,True,True,True,False,True,False,True,False,True,False,False,True,True,False,True,True,True,True,False,False,True,True,False,True,False,True,True,True,True,False,True,True,True,False,True,False,True,False,True,False,False,True,False,True,False,True,True,True,True,True,False,False,False,False,True,True,False,False,False,True,False,False,False,True,False,True,False,True,True,True,False,True,False,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,True,False,False,True,True,True,True,True,False,True,False,False,False,False,False,True,True,False,True,False,True,True,True,True,False,False,True,True,True,False,True,False,False,False,True,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,False,False,True,False,False,False,False,False,True,True,False,True,True,False,False,False,True,True,True,True,True,True,True,False,False,True,True,True,False,True,False,True,False,True,True,False,False,True,False,True,True,False,False,False,False,False,False,True,False,True,True,True,False,False,False,True,False,True,False,False,True,True,True,True,False,True,True,False,False,True,True,True,False,False,False,False,False,False,False,False,False,True,False,False,True,False,True,True,True,False,False,False,True,True,True,True,False,False,False,True,False,True,False,False,True,False,False,False,True,False,False,True,True,False,True,True,False,True,False,False,True,False,False,False,False,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,True,True,False,True,True,False,False,False,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,False,True,False,False,True,True,True,True,False,False,True,True,True,True,True,True,False,False,True,False,True,False,False,False,False,False,True,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,False,False,True,True,True,True,True,True,False,False,True,False,False,True,False,False,True,True,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,True,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,False,True,False,False,False,False,True,True,False,False,False,True,False,False,False,False,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,True,True,False,True,True,True,False,False,True,True,False,True,False,True,True,True,True,True,True,False,False,False,True,False,True,False,False,True,True,True,True,False,False,False,False,True,True,False,True,False,True,True,False,True,False,True,False,True,False,True,True,True,True,False,True,False,False,True,True,False,False,True,False,False,True,False,True,False,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,False,True,False,True,False,False,True,True,True,True,False,False,True,True,False,True,False,False,True,False,True,False,True,True,True,True,False,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,False,True,True,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,False,False,True,False,True,False,True,True,True,False,True,True,False,False,False,True,True,False,True,False,False,True,True,False,True,False,False,False,True,False,False,True,True,True,True,False,False,False,True,True,False,False,False,False,False,True,True,True,True,False,True,True,False,True,True,True,True,True,False,False,False,False,True,True,False,False,True,False,False,False,True,True,False,True,True,False,False,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True,True,True,True,False,True,False,False,False,True,False,False,False,False,False,True,True,False,True,True,True,False,True,True,True,True,True,False,False,True,False,True,False,True,True,False,True,True,False,True,False,False,True,False,False,False,False,True,False,True,True,True,True,False,False,True,True,False,True,True,True,True,True,False,True,False,False,False,True,True,True,True,True,True,True,False,True,True,True,True,False,False,False,False,False,False,True,False,False,False,True,False,False,False,False,True,False,False,True,True,True,False,False,True,True,False,True,False,True,False,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,False,False,False,True,True,True,False,False,False,True,True,False,False,False,True,True,True,True,False,True,True,True,True,False,True,True,False,False,False,True,True,False,False,True,True,True,True,False,True,True,True,True,True,False,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,True,True,False,True,False,False,True,True,False,False,False,True,True,True,True,False,False,False,True,False,True,False,True,False,True,True,True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,True,True,False,False,True,True,False,False,True,False,True,False,True,False,True,True,False,False,True,True,True,True,True,True,False,False,True,False,False,True,False,True,False,False,False,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,True,False,True,False,True,True,False,False,True,True,True,True,False,True,True,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,False,True,True,False,True,False,True,True,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,False,False,True,True,False,False,False,True,False,False,False,False,True,True,True,False,True,True,True,False,False,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,False,False,False,True,True,True,False,False,False,True,False,True,True,False,True,True,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,True,True,True,False,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,False,False,True,False,False,False,False,False,False,False,True,True,True,True,True,True,True,False,True,False,True,False,True,True,True,False,True,False,False,False,False,False,False,False,True,False,False,True,True,False,True,False,False,True,True,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,True,False,False,False,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,True,True,False,True,False,True,False,True,False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,False,False,True,False,True,False,False,False,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False,False,True,True,True,False,False,True,False,False,True,True,False,False,True,False,False,False,True,True,False,False,False,False,False,True,False,False,True,True,False,True,True,True,False,False,False,False,True,False,True,True,True,True,True,False,False,False,False,True,True,False,True,True,False,True,False,True,False,False,False,False,True,False,True,False,False,True,False,False,True,True,True,False,True,False,False,True,False,False,False,True,True,True,True,True,True,True,False,True,True,True,True,True,True,False,True,True,False,True,True,True,True,False,False,False,True,False,True,True,True,True,True,False,False,False,True,True,True,False,False,True,True,True,False,False,False,True,True,False,False,True,True,True,True,True,True,False,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,True,True,True,True,True,False,True,True,True,False,True,False,True,False,False,False,False,False,False,True,False,True,False,False,False,True,True,False,True,True,False,True,True,True,False,False,False,True,False,True,True,True,True,True,True,True,True,False,False,True,True,False,False,False,False,False,True,True,False,False,True,False,True,False,False,False,False,False,True,False,True,True,True,False,False,True,False,True,True,False,False,False,False,False,False,False,False,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,False,True,False,False,False,False,True,True,False,True,True,False,True,False,False,True,True,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True,True,True,False,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False,False,True,False,True,False,False,False,False,False,True,True,False,False,False,False,True,True,True,True,False,False,False,True,True,True,True,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,False,False,True,False,False,False,True,True,True,True,True,True,False,True,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,False,True,False,False,False,False,False,True,True,True,False,True,True,False,True,False,True,True,False,False,True,True,True,False,False,False,True,True,True,True,False,False,False,False,False,False,True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,False,False,False,True,False,True,False,False,False,False,False,True,False,False,False,True,True,True,True,False,False,True,True,False,False,False,True,False,False,True,False,True,True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,True,True,True,True,False,False,False,False,False,True,False,True,True,False,False,False,True,False,False,True,False,False,True,False,False,False,True,False,False,True,True,True,False,True,True,False,True,True,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,True,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,False,False,False,False,False,True,False,True,True,False,False,True,False,True,False,False,True,False,True,True,True,True,False,False,False,False,False,False,True,False,False,False,False,False,False,False,True,False,False,False,True,False,True,True,True,True,False,True,False,True,False,True,True,False,True,True,True,True,False,False,False,False,False,False,False,True,True,True,True,True,False,False,True,True,False,False,True,False,True,True,True,True,False,False,False,True,False,True,True,False,True,True,False,False,True,False,True,False,True,False,True,True,True,False,True,True,True,False,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,False,True,True,False,False,False,False,False,True,False,True,False,True,True,True,False,False,True,False,True,False,False,True,True,True,True,False,True,True,True,False,True,False,True,False,True,True,False,True,False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,True,False,True,False,False,True,False,True,True,False,True,False,True,True,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True,True,True,True,True,True,False,False,True,True,False,False,False,True,False,True,True,False,True,False,False,True,False,False,True,True,False,False,True,False,True,True,True,True,False,False,False,False,False,True,True,False,False,True,False,False,True,True,False,False,True,False,True,True,False,False,False,False,True,False,False,False,True,True,True,True,True,False,True,False,True,False,False,True,False,False,True,True,False,True,True,True,True,False,True,True,True,True,True,False,True,True,False,False,False,False,True,False,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,True,True,True,True,False,True,False,False,False,False,True,True,False,True,False,False,True,True,False,False,False,True,True,True,False,False,True,True,False,False,True,True,True,True,False,False,False,True,False,False,True,True,True,True,False,False,False,True,True,False,False,True,True,True,False,True,True,True,False,True,True,False,True,False,True,True,False,True,False,True,True,True,False,True,True,True,True,True,False,False,True,False,True,True,False,True,False,True,False,True,True,True,True,False,True,False,True,False,True,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,False,False,True,True,False,True,False,False,True,True,True,False,False,False,False,False,False,True,False,False,False,False,False,True,True,False,True,True,False,True,True,True,False,False,False,False,True,False,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,False,False,False,True,True,True,True,True,True,False,True,True,False,True,True,True,True,True,True,True,False,True,True,True,False,True,True,True,False,False,False,False,False,False,True,True,False,True,False,True,True,True,False,False,False,True,True,False,True], dtype = "bool")#candidate|3489|(3136,)|const|bool
call_3488 = relay.TupleGetItem(func_499_call(relay.reshape(const_3489.astype('bool'), [16, 14, 14])), 0)
call_3490 = relay.TupleGetItem(func_501_call(relay.reshape(const_3489.astype('bool'), [16, 14, 14])), 0)
bop_3505 = relay.multiply(uop_3484.astype('uint16'), relay.reshape(call_3455.astype('uint16'), relay.shape_of(uop_3484))) # shape=(2, 13, 5)
bop_3508 = relay.multiply(uop_3486.astype('uint16'), relay.reshape(call_3456.astype('uint16'), relay.shape_of(uop_3486))) # shape=(2, 13, 5)
bop_3510 = relay.add(call_3488.astype('int64'), relay.reshape(const_3489.astype('int64'), relay.shape_of(call_3488))) # shape=(16, 14, 14)
bop_3513 = relay.add(call_3490.astype('int64'), relay.reshape(const_3489.astype('int64'), relay.shape_of(call_3490))) # shape=(16, 14, 14)
bop_3517 = relay.bitwise_xor(uop_3484.astype('int8'), relay.reshape(bop_3505.astype('int8'), relay.shape_of(uop_3484))) # shape=(2, 13, 5)
bop_3520 = relay.bitwise_xor(uop_3486.astype('int8'), relay.reshape(bop_3508.astype('int8'), relay.shape_of(uop_3486))) # shape=(2, 13, 5)
bop_3528 = relay.maximum(bop_3505.astype('int64'), relay.reshape(call_3455.astype('int64'), relay.shape_of(bop_3505))) # shape=(2, 13, 5)
bop_3531 = relay.maximum(bop_3508.astype('int64'), relay.reshape(call_3456.astype('int64'), relay.shape_of(bop_3508))) # shape=(2, 13, 5)
output = relay.Tuple([bop_3510,bop_3517,bop_3528,])
output2 = relay.Tuple([bop_3513,bop_3520,bop_3531,])
func_3534 = relay.Function([], output)
mod['func_3534'] = func_3534
mod = relay.transform.InferType()(mod)
mutated_mod['func_3534'] = func_3534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3534_call = mutated_mod.get_global_var('func_3534')
call_3535 = func_3534_call()
output = call_3535
func_3536 = relay.Function([], output)
mutated_mod['func_3536'] = func_3536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3351_call = mod.get_global_var('func_3351')
func_3352_call = mutated_mod.get_global_var('func_3352')
call_3547 = func_3351_call()
call_3548 = func_3351_call()
uop_3566 = relay.asinh(call_3547.astype('float64')) # shape=(2, 13, 5)
uop_3568 = relay.asinh(call_3548.astype('float64')) # shape=(2, 13, 5)
uop_3573 = relay.erf(call_3547.astype('float64')) # shape=(2, 13, 5)
uop_3575 = relay.erf(call_3548.astype('float64')) # shape=(2, 13, 5)
output = relay.Tuple([uop_3566,uop_3573,])
output2 = relay.Tuple([uop_3568,uop_3575,])
func_3580 = relay.Function([], output)
mod['func_3580'] = func_3580
mod = relay.transform.InferType()(mod)
output = func_3580()
func_3581 = relay.Function([], output)
mutated_mod['func_3581'] = func_3581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3351_call = mod.get_global_var('func_3351')
func_3352_call = mutated_mod.get_global_var('func_3352')
call_3595 = func_3351_call()
call_3596 = func_3351_call()
func_904_call = mod.get_global_var('func_904')
func_907_call = mutated_mod.get_global_var('func_907')
var_3613 = relay.var("var_3613", dtype = "float64", shape = (182,))#candidate|3613|(182,)|var|float64
call_3612 = relay.TupleGetItem(func_904_call(relay.reshape(var_3613.astype('float64'), [2, 7, 13])), 0)
call_3614 = relay.TupleGetItem(func_907_call(relay.reshape(var_3613.astype('float64'), [2, 7, 13])), 0)
output = relay.Tuple([call_3595,call_3612,var_3613,])
output2 = relay.Tuple([call_3596,call_3614,var_3613,])
func_3623 = relay.Function([var_3613,], output)
mod['func_3623'] = func_3623
mod = relay.transform.InferType()(mod)
mutated_mod['func_3623'] = func_3623
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3624 = relay.var("var_3624", dtype = "float64", shape = (182,))#candidate|3624|(182,)|var|float64
func_3623_call = mutated_mod.get_global_var('func_3623')
call_3625 = func_3623_call(var_3624)
output = call_3625
func_3626 = relay.Function([var_3624], output)
mutated_mod['func_3626'] = func_3626
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3634 = relay.var("var_3634", dtype = "float64", shape = (4, 4, 1))#candidate|3634|(4, 4, 1)|var|float64
uop_3635 = relay.acosh(var_3634.astype('float64')) # shape=(4, 4, 1)
output = relay.Tuple([uop_3635,])
output2 = relay.Tuple([uop_3635,])
func_3641 = relay.Function([var_3634,], output)
mod['func_3641'] = func_3641
mod = relay.transform.InferType()(mod)
var_3642 = relay.var("var_3642", dtype = "float64", shape = (4, 4, 1))#candidate|3642|(4, 4, 1)|var|float64
output = func_3641(var_3642)
func_3643 = relay.Function([var_3642], output)
mutated_mod['func_3643'] = func_3643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3351_call = mod.get_global_var('func_3351')
func_3352_call = mutated_mod.get_global_var('func_3352')
call_3755 = func_3351_call()
call_3756 = func_3351_call()
output = relay.Tuple([call_3755,])
output2 = relay.Tuple([call_3756,])
func_3786 = relay.Function([], output)
mod['func_3786'] = func_3786
mod = relay.transform.InferType()(mod)
mutated_mod['func_3786'] = func_3786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3786_call = mutated_mod.get_global_var('func_3786')
call_3787 = func_3786_call()
output = call_3787
func_3788 = relay.Function([], output)
mutated_mod['func_3788'] = func_3788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3786_call = mod.get_global_var('func_3786')
func_3788_call = mutated_mod.get_global_var('func_3788')
call_3794 = relay.TupleGetItem(func_3786_call(), 0)
call_3795 = relay.TupleGetItem(func_3788_call(), 0)
func_3580_call = mod.get_global_var('func_3580')
func_3581_call = mutated_mod.get_global_var('func_3581')
call_3803 = relay.TupleGetItem(func_3580_call(), 1)
call_3804 = relay.TupleGetItem(func_3581_call(), 1)
func_2276_call = mod.get_global_var('func_2276')
func_2280_call = mutated_mod.get_global_var('func_2280')
const_3811 = relay.const(-6, dtype = "uint8")#candidate|3811|()|const|uint8
const_3812 = relay.const([6,6,-10,-5,6,-6,5,4,8,-2,-6,5,1,-1,10,4,6,8,-10,6,-2,-4,6,5,-4,6,-4,-3,-3,-6,4,1,-9,9,3,-7,8,3,1,-9,-7,-7,5,7,-4,-5,4,10,6,-3,5,-3,3,-6,-4,-9,1,3,6,8,-5,-2,-8,2,-4,-10,-7,1,-10,2,3,4,-7,-1,-7,7,-1,-10,-1,-2,9,3,6,-4,2,-2,-7,-10,3,9,2,5,3,2,-10,-9,8,-3,-4,3,-4,3,-1,-10,-6,-8,5,2,1,-3,8,-7,2,5,10,-3,2,10,9,-2,8,-3,-3,10,9,-2,5,-5,3,4,7,10,5,5,-7,-9,6,8,5,3,3,-2,9,5,7,-7,-9,6,-6,-8,-7,-10,8,-4,5,-6,-5,7,6,-5,-3,9,-9,6,7,8,10,7,-5,-1,-8,-1,7,-6,9,-8,-6,-4,4,-10,-3,-3,6,9,2,-4,-8,5,4,-8,7,-5,5,-7,9,-7,6,5,3,7,-3,8,-7,-7,-6,-4,-5,7,-8,8,-2,2,-9,3,-1,9,-1,-7,2,9,-3,3,2,7,-4,1,-1,7,-10,-4,-1,6,10,4,9,1,6,9,6,10,-2,10,-2,3,-9,4,10,4,3,-3,1,6,10,5,-3,7,-4,9,6,-9,-9,-5,-2,10,-8,2,6,7,5,-1,-9,-2,-9,-10,-4,-8,-3,-3,-3,-2,3,10,-2,-5,-1,5,-7,2,9,1,-10,-6,1,7,10,4,-5,-5,1,6,-6,-1,-8,-1,4,8,-2,-8,4,8,7,9,6,1,-4,3,-5,-5,7,10,9,-7,2,3,-1,8,-2,-1,1,-10,-8,4,-7,-8,6,-8,-6,5,10,-2,8,-10,8,-3,-3,5,3,-9,-10,-5,-5,-1,-5,8,6,-6,-1,7,8,-10,2,-6,-5,-5,2,-1,-2,9,-3,-5,-7,5,7,-7,1,-10,3,8,-9,-2,3,-9,10,-2,-2,-3,-8,-7,10,4,9,4,7,9,5,8,-9,-2,-4,-3,1,-5,2,-4,6,-4,1,7,2,-4,1,4,9,-8,-10,1,-5,-10,10,9,-3,1,3,-10,7,-1,-7,8,-10,-1,7,4,10,-1,8,-6,-5,5,-8,10,-10,-4,7,-7,6,9,-1,5,5,-2,6,-5,7,-8,4,8,10,-3,4,3,-9,3,-5,1,-6,4,1,4,9,2,-1,-9,2,7,-3,6,-3,2,-1,10,8,-1,5,-8,9,-8,-10,-9,-1,10,7,6,7,9,-2,7,-3,8,6,-10,6,3,-7,8,-1,3,-4,-7,8,-1,5,10,-6,5,6,7,5,8,4,-1,-4,-2,-3,1,5,2,8,7,4,-8,-9,-2,4,-8,4,3,6,-8,4,-10,9,-10,-8,3,-1,10,-5,-4,-2,1,-4,6,2,10,-1,-7,-4,9,4,-4,4,-4,-6,-10,-3,-4,7,-6,4,-5,6,-9,-8,4,2,-8,-10,5,-1,6,-10,-10,2,4,-1,3,10,10,10,-10,10,9,2,-9,3,-6,8,9,-1,-6,-1,-2,2,-1,-7,-7,10,-10,1,5,5,-8,7,-2,10,3,-8,-4,-8,-5,5,4,7,8,-3,4,2,10,-9,8,-10,-1,-5,-1,10,-9,-5,10,9,9,-1,-10,7,2,10,-5,10,-1,1,-9,-7,5,5,3,3,4,9,7,-3,1,-1,-6,-2,-8,-8,-3,-9,-6,-6,-8,4,-3,7,-8,2,-6,6,6,10,3,2,4,6,8,10,1,8,-7,-5,-5,-4,10,2,10,-9,-9,-8,-4,2,4,-8,6,-8,-2,9,2,8,-5,-5,10,7,6,-2,-10,6,6,1,-1,8,4,1,-1,7,9,3,7,-9,-5,-7,5,1,7,-5,10,2,-1,9,3,-9,9,2,-2,-1,1,-4,-9,-8,-4,5,-8,-10,-3,10,7,8,3,-4,-10,2,10,8,10,8,-10,-9,-3,7,10,-3,9,2,1,7,-10,-5,-6,4,10,9,6,-10,9,-4,-7,5,-8,9,5,-3,6,7,-10,7,2,3,6,-6,3,1,9,-7,4,-8,-2,4,-10,10,-2,1,-3,-4,8,-3,2,-2,-1,-9,6,2,10,-6,8,10,4,-6,8,7,9,-8,5,3,-8,9,-10,2,8,10,-7,-6,4,8,-1,7,-5,3,4,6,-6,5,-7,-8,4,-10,2,2,9,7,4,-10,-8,1,-6,-3,-1,2,3,4,10,10,2,-8,-3,9,-1,-8,-3,-3,5,3,4,5,-5,-9,-5,-9,-3,5,3,1,6,-5,8,8,-3,1,-8,5,7,10,-2,-8,5,-9,9,2,-1,2,2,5,5,-3,2,8,-3,-3,9,-10,-3,1,-10,7,10,1,3,9,1,3,-1,5,1,-9,-9,5,7,-6,-10,8,-2,4,-4,3,7,9,9,4,-1,-10,-1,4,10,-4,-3,-2,9,2,9,7,3,7,-1,2,1,4,-7,-9,8,-9,4,-8,9,8,-5,-5,-2,-10,3,-5,-4,-6,7,9,-1,-8,4,-9,4,-1,2,-7,8,7,7,-6,1,3,-9,3,5,-6,7,-9,5,-10,-4,1,-4,3,-10,-4,3,7,2,-4,3,-3,7,1,-10,9,8,7,-10,-5,3,1,9,-10,10,-5,5,-3,-9,-4,-5,-6,7,-7,6,-7,-1,5,-8,10,-8,-3,4,7,2,4,-6,-10,-6,10,-9,10,-7,2,1,-5,9,-4,-6,6,-4,-5,3,-5,-2,-10,4,-3,-9,8,8,-9,-1,-10,3,7,8,-10,-7,1,-10,2,-3,6,-1,9,8,-6,10,8,-2,3,-6,3,7,-5,-5,2,-4,-7,5,-4,-6,3,-6,1,5,6,-4,5,2,-8,-6,4,-3,7,-9,-10,-3,2,6,-5,-7,2,-1,3,-8,-10,-5,4,-5,3,-4,-10,-8,4,6,-4,-2,4,-5,9,-2,-8,3,-5,3,-4,-3,-3,9,-4,9,-7,4,6,-10,3,-6,-7,2,-9,9,3,-10,-4,6,-3,4,5,1,7,6,1,2,-1,1,-3,-5,-6,-5,-5,6,3,10,-8,-9,2,9,-7,5,-7,-2,-9,-7,4,-5,2,-1,-1,-4,1,6,-1,1,7,-10,2,-3,8,8,-1], dtype = "uint8")#candidate|3812|(1215,)|const|uint8
call_3810 = relay.TupleGetItem(func_2276_call(relay.reshape(const_3811.astype('uint8'), []), relay.reshape(const_3812.astype('uint8'), [9, 9, 15]), ), 0)
call_3813 = relay.TupleGetItem(func_2280_call(relay.reshape(const_3811.astype('uint8'), []), relay.reshape(const_3812.astype('uint8'), [9, 9, 15]), ), 0)
output = relay.Tuple([call_3794,call_3803,call_3810,const_3811,const_3812,])
output2 = relay.Tuple([call_3795,call_3804,call_3813,const_3811,const_3812,])
func_3833 = relay.Function([], output)
mod['func_3833'] = func_3833
mod = relay.transform.InferType()(mod)
mutated_mod['func_3833'] = func_3833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mutated_mod.get_global_var('func_3833')
call_3834 = func_3833_call()
output = call_3834
func_3835 = relay.Function([], output)
mutated_mod['func_3835'] = func_3835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3580_call = mod.get_global_var('func_3580')
func_3581_call = mutated_mod.get_global_var('func_3581')
call_3841 = relay.TupleGetItem(func_3580_call(), 0)
call_3842 = relay.TupleGetItem(func_3581_call(), 0)
output = call_3841
output2 = call_3842
func_3862 = relay.Function([], output)
mod['func_3862'] = func_3862
mod = relay.transform.InferType()(mod)
output = func_3862()
func_3863 = relay.Function([], output)
mutated_mod['func_3863'] = func_3863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3786_call = mod.get_global_var('func_3786')
func_3788_call = mutated_mod.get_global_var('func_3788')
call_3866 = relay.TupleGetItem(func_3786_call(), 0)
call_3867 = relay.TupleGetItem(func_3788_call(), 0)
func_108_call = mod.get_global_var('func_108')
func_111_call = mutated_mod.get_global_var('func_111')
var_3869 = relay.var("var_3869", dtype = "uint16", shape = (234,))#candidate|3869|(234,)|var|uint16
call_3868 = func_108_call(relay.reshape(var_3869.astype('uint16'), [2, 13, 9]))
call_3870 = func_108_call(relay.reshape(var_3869.astype('uint16'), [2, 13, 9]))
uop_3874 = relay.cos(call_3866.astype('float64')) # shape=(2, 13, 5)
uop_3876 = relay.cos(call_3867.astype('float64')) # shape=(2, 13, 5)
func_1047_call = mod.get_global_var('func_1047')
func_1049_call = mutated_mod.get_global_var('func_1049')
const_3890 = relay.const([-10,-1,2,-2,2,7,-4,-8,9,-4,-2,-1,-4,5,5,-5,8,5,5,-8,5,10,-4,-8,-6,3,-1,-1,1,2,-10,3,2,-10,5,-3,3,4,2,2,2,-9,10,-9,8,9,10,-5,-1,-1,-5,1,-8,7,4,-9,5,-3,-8,9,4,3,1,-8,3,3,4,5,-6,1,2,-8,7,-5,4,10,-2,-3,1,7,1,-3,3,-6,-10,1,-6,-10,-2,10,7,-5,-5,1,-10,-3,6,5,-3,10,-7,-3,2,7,-6,-2,-1,1,-5,-3,9,-7,9,8,-4,-3,-7,-7,-2,5,-3,3,1,-9,6,-3,-7,4,6,-8,-8,3,-1,-8,-7,3,7,-6,-1,9,7,6,4,-10,2,3,10,9,6,-6,-8,5,-6,8,-5,9,-8,-6,5,-3,5,-8,1,8,-5,-2,-5,2,7,-1,4,-4,4,-5,9,7,3,1,-5,3,3,-4,-4,10,-6,-6,2,1,4], dtype = "int64")#candidate|3890|(189,)|const|int64
call_3889 = func_1047_call(relay.reshape(const_3890.astype('int64'), [9, 3, 7]))
call_3891 = func_1047_call(relay.reshape(const_3890.astype('int64'), [9, 3, 7]))
output = relay.Tuple([call_3868,var_3869,uop_3874,call_3889,const_3890,])
output2 = relay.Tuple([call_3870,var_3869,uop_3876,call_3891,const_3890,])
func_3895 = relay.Function([var_3869,], output)
mod['func_3895'] = func_3895
mod = relay.transform.InferType()(mod)
mutated_mod['func_3895'] = func_3895
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3896 = relay.var("var_3896", dtype = "uint16", shape = (234,))#candidate|3896|(234,)|var|uint16
func_3895_call = mutated_mod.get_global_var('func_3895')
call_3897 = func_3895_call(var_3896)
output = call_3897
func_3898 = relay.Function([var_3896], output)
mutated_mod['func_3898'] = func_3898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3862_call = mod.get_global_var('func_3862')
func_3863_call = mutated_mod.get_global_var('func_3863')
call_3917 = func_3862_call()
call_3918 = func_3862_call()
output = call_3917
output2 = call_3918
func_3947 = relay.Function([], output)
mod['func_3947'] = func_3947
mod = relay.transform.InferType()(mod)
mutated_mod['func_3947'] = func_3947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3947_call = mutated_mod.get_global_var('func_3947')
call_3948 = func_3947_call()
output = call_3948
func_3949 = relay.Function([], output)
mutated_mod['func_3949'] = func_3949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3580_call = mod.get_global_var('func_3580')
func_3581_call = mutated_mod.get_global_var('func_3581')
call_3967 = relay.TupleGetItem(func_3580_call(), 0)
call_3968 = relay.TupleGetItem(func_3581_call(), 0)
func_2276_call = mod.get_global_var('func_2276')
func_2280_call = mutated_mod.get_global_var('func_2280')
const_3976 = relay.const(5, dtype = "uint8")#candidate|3976|()|const|uint8
var_3977 = relay.var("var_3977", dtype = "uint8", shape = (1215,))#candidate|3977|(1215,)|var|uint8
call_3975 = relay.TupleGetItem(func_2276_call(relay.reshape(const_3976.astype('uint8'), []), relay.reshape(var_3977.astype('uint8'), [9, 9, 15]), ), 1)
call_3978 = relay.TupleGetItem(func_2280_call(relay.reshape(const_3976.astype('uint8'), []), relay.reshape(var_3977.astype('uint8'), [9, 9, 15]), ), 1)
output = relay.Tuple([call_3967,call_3975,const_3976,var_3977,])
output2 = relay.Tuple([call_3968,call_3978,const_3976,var_3977,])
func_3982 = relay.Function([var_3977,], output)
mod['func_3982'] = func_3982
mod = relay.transform.InferType()(mod)
var_3983 = relay.var("var_3983", dtype = "uint8", shape = (1215,))#candidate|3983|(1215,)|var|uint8
output = func_3982(var_3983)
func_3984 = relay.Function([var_3983], output)
mutated_mod['func_3984'] = func_3984
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4028 = relay.var("var_4028", dtype = "float32", shape = (6, 9, 16))#candidate|4028|(6, 9, 16)|var|float32
uop_4029 = relay.sinh(var_4028.astype('float32')) # shape=(6, 9, 16)
bop_4034 = relay.greater_equal(uop_4029.astype('bool'), relay.reshape(var_4028.astype('bool'), relay.shape_of(uop_4029))) # shape=(6, 9, 16)
output = relay.Tuple([bop_4034,])
output2 = relay.Tuple([bop_4034,])
func_4041 = relay.Function([var_4028,], output)
mod['func_4041'] = func_4041
mod = relay.transform.InferType()(mod)
mutated_mod['func_4041'] = func_4041
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4042 = relay.var("var_4042", dtype = "float32", shape = (6, 9, 16))#candidate|4042|(6, 9, 16)|var|float32
func_4041_call = mutated_mod.get_global_var('func_4041')
call_4043 = func_4041_call(var_4042)
output = call_4043
func_4044 = relay.Function([var_4042], output)
mutated_mod['func_4044'] = func_4044
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4046 = relay.var("var_4046", dtype = "float64", shape = (7, 11, 15))#candidate|4046|(7, 11, 15)|var|float64
uop_4047 = relay.log10(var_4046.astype('float64')) # shape=(7, 11, 15)
func_1618_call = mod.get_global_var('func_1618')
func_1622_call = mutated_mod.get_global_var('func_1622')
const_4061 = relay.const([4,1,6,3,7,-10,-6,2,4,-3,2,-8,8,3,8,-5,9,-10,-9,-6,8,5,-10,7,6,7,-9,10,8,-7,7,-1,-8,-3,3,3,-7,7,-7,5,4,1,4,-3,7,1,2,4,4,-8,9,10,10,-7,-4,10,2,-3,3,1,6,7,3,-7,-9,5,4,5,-7,-1,-5,-10,2,-3,9,-8,5,2,-5,6,2,5,1,2,-4,-8,5,4,-3,-4,-3,9,8,-8,8,8,-7,6,4,-5,-2,-5,-1,4,-8,-8,1,-8,7,-3,-10,-5,-5,-5,10,7,-3,6,-3,-7,9,3,3,10,-7,-4,-5,4,-9,-8,10,-8,-8,-6,5,4,-1,7,-10,1,-9,4,4,-3,-10,-2,6,1,4,-9,-1,6,-1,5,9,7,-2,1,3,-9,-7,-1,-10,-9,10,-7,10,-4,-6,2,-6,3,-2,-4,-10,-7,-3,-10,-1,-1,-6,5,-2,8,-7,-3,-1,-10,3], dtype = "int64")#candidate|4061|(189,)|const|int64
const_4062 = relay.const([[-6,10,-9,-7,-4,3,4,6,8,1,-9,-10,5,-10,-2,5,3,3,10,10,-8,8,2,5,9,-2,10,-5,5,-3,-10,-6,-6,4,8,9,-6,7,3,9,-7,-2,2,10,-5,-6,-3,-7,-1,4,6,5,-2,-1,4,1,-3,-6,10,-2,-1,9,3,3,-8,5,-10,-7,3,-9,10,-8,-3,-5,4,-10,-10,-1,5,-8,8,-1,4,-3,6,5,4,-6,-10,1,-2,1,10,-4,-5,-9,6,1,8,8,-6,9,-6,6,-7,2,-6,3,6,-10,-2,3,-1,-9,-10,2,-9,7,-7,3,-10,5,-9,-3,-6,5,-5,7,5,-4,2,-1,8,-6,1,-9,6,8,-2,2,5,5,8,-6,9,-7,6,4,6,-9,1,1,-3,3,-9,3,-2,5,-2,2,9,-4,7,-10,-8,-3,8,6,-10,-7,4,6,8,-6,10,-4,7,-7,6,9,-8,-2,-4,-10,-7,-7,6,-9,-3,-7,-4,4,-8,6,-10,-7,7,5,-10,-6,-1,-10,-6,-1,3,-4,8,-8,10,-8,1,7,7,-7,-10,-3,-8,7,-1,3,-6,-1,-4,1,-5,2,-6,-3,-4,7,-5,-4,3,-7]], dtype = "uint16")#candidate|4062|(1, 234)|const|uint16
call_4060 = relay.TupleGetItem(func_1618_call(relay.reshape(const_4061.astype('int64'), [189,]), relay.reshape(const_4062.astype('uint16'), [234,]), ), 4)
call_4063 = relay.TupleGetItem(func_1622_call(relay.reshape(const_4061.astype('int64'), [189,]), relay.reshape(const_4062.astype('uint16'), [234,]), ), 4)
output = relay.Tuple([uop_4047,call_4060,const_4061,const_4062,])
output2 = relay.Tuple([uop_4047,call_4063,const_4061,const_4062,])
func_4068 = relay.Function([var_4046,], output)
mod['func_4068'] = func_4068
mod = relay.transform.InferType()(mod)
var_4069 = relay.var("var_4069", dtype = "float64", shape = (7, 11, 15))#candidate|4069|(7, 11, 15)|var|float64
output = func_4068(var_4069)
func_4070 = relay.Function([var_4069], output)
mutated_mod['func_4070'] = func_4070
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4080 = relay.var("var_4080", dtype = "float64", shape = (9, 16, 14))#candidate|4080|(9, 16, 14)|var|float64
uop_4081 = relay.acos(var_4080.astype('float64')) # shape=(9, 16, 14)
output = relay.Tuple([uop_4081,])
output2 = relay.Tuple([uop_4081,])
func_4085 = relay.Function([var_4080,], output)
mod['func_4085'] = func_4085
mod = relay.transform.InferType()(mod)
mutated_mod['func_4085'] = func_4085
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4086 = relay.var("var_4086", dtype = "float64", shape = (9, 16, 14))#candidate|4086|(9, 16, 14)|var|float64
func_4085_call = mutated_mod.get_global_var('func_4085')
call_4087 = func_4085_call(var_4086)
output = call_4087
func_4088 = relay.Function([var_4086], output)
mutated_mod['func_4088'] = func_4088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3862_call = mod.get_global_var('func_3862')
func_3863_call = mutated_mod.get_global_var('func_3863')
call_4090 = func_3862_call()
call_4091 = func_3862_call()
func_2276_call = mod.get_global_var('func_2276')
func_2280_call = mutated_mod.get_global_var('func_2280')
var_4098 = relay.var("var_4098", dtype = "uint8", shape = ())#candidate|4098|()|var|uint8
var_4099 = relay.var("var_4099", dtype = "uint8", shape = (1215,))#candidate|4099|(1215,)|var|uint8
call_4097 = relay.TupleGetItem(func_2276_call(relay.reshape(var_4098.astype('uint8'), []), relay.reshape(var_4099.astype('uint8'), [9, 9, 15]), ), 0)
call_4100 = relay.TupleGetItem(func_2280_call(relay.reshape(var_4098.astype('uint8'), []), relay.reshape(var_4099.astype('uint8'), [9, 9, 15]), ), 0)
func_3351_call = mod.get_global_var('func_3351')
func_3352_call = mutated_mod.get_global_var('func_3352')
call_4104 = func_3351_call()
call_4105 = func_3351_call()
func_3641_call = mod.get_global_var('func_3641')
func_3643_call = mutated_mod.get_global_var('func_3643')
const_4113 = relay.const([[-4.029070,-9.615746,-8.231366,-0.851669],[0.202019,-7.995014,-3.645958,1.173337],[-1.724989,7.690077,9.671857,0.364540],[5.371320,2.771055,5.669451,0.681172]], dtype = "float64")#candidate|4113|(4, 4)|const|float64
call_4112 = relay.TupleGetItem(func_3641_call(relay.reshape(const_4113.astype('float64'), [4, 4, 1])), 0)
call_4114 = relay.TupleGetItem(func_3643_call(relay.reshape(const_4113.astype('float64'), [4, 4, 1])), 0)
output = relay.Tuple([call_4090,call_4097,var_4098,var_4099,call_4104,call_4112,const_4113,])
output2 = relay.Tuple([call_4091,call_4100,var_4098,var_4099,call_4105,call_4114,const_4113,])
func_4118 = relay.Function([var_4098,var_4099,], output)
mod['func_4118'] = func_4118
mod = relay.transform.InferType()(mod)
var_4119 = relay.var("var_4119", dtype = "uint8", shape = ())#candidate|4119|()|var|uint8
var_4120 = relay.var("var_4120", dtype = "uint8", shape = (1215,))#candidate|4120|(1215,)|var|uint8
output = func_4118(var_4119,var_4120,)
func_4121 = relay.Function([var_4119,var_4120,], output)
mutated_mod['func_4121'] = func_4121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3786_call = mod.get_global_var('func_3786')
func_3788_call = mutated_mod.get_global_var('func_3788')
call_4123 = relay.TupleGetItem(func_3786_call(), 0)
call_4124 = relay.TupleGetItem(func_3788_call(), 0)
output = call_4123
output2 = call_4124
func_4159 = relay.Function([], output)
mod['func_4159'] = func_4159
mod = relay.transform.InferType()(mod)
mutated_mod['func_4159'] = func_4159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4159_call = mutated_mod.get_global_var('func_4159')
call_4160 = func_4159_call()
output = call_4160
func_4161 = relay.Function([], output)
mutated_mod['func_4161'] = func_4161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3580_call = mod.get_global_var('func_3580')
func_3581_call = mutated_mod.get_global_var('func_3581')
call_4178 = relay.TupleGetItem(func_3580_call(), 0)
call_4179 = relay.TupleGetItem(func_3581_call(), 0)
output = call_4178
output2 = call_4179
func_4206 = relay.Function([], output)
mod['func_4206'] = func_4206
mod = relay.transform.InferType()(mod)
output = func_4206()
func_4207 = relay.Function([], output)
mutated_mod['func_4207'] = func_4207
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4220 = relay.const([[[4.946686,-0.185905,8.302366,0.004169,5.150888,-2.203071,-5.834586,1.084526,4.354360,5.110405,-7.169626],[8.515229,-1.374868,-6.668289,4.111871,-2.780766,5.509447,2.890380,6.784839,2.237970,8.302709,-2.497650],[-1.314235,6.190842,7.573007,-8.961011,-6.477251,-0.104614,0.933843,-0.026157,6.286173,-7.491188,-6.473103],[6.809785,-2.235903,-0.977425,-4.054571,9.345294,-5.529585,4.890028,-8.167419,4.161045,3.729123,8.785490]],[[7.023556,-7.231070,-4.498980,5.389133,-7.074970,3.455733,5.411957,1.176690,-0.628291,-4.522796,9.889339],[-9.815413,-4.438406,9.720087,1.950000,-5.820966,-9.286879,4.745492,4.463383,1.717771,-7.890519,5.569824],[-7.412379,1.325725,9.667048,-6.374515,2.171454,-8.412565,-4.247838,-0.261566,-4.333450,-9.546036,5.819928],[-2.548320,-2.342958,-3.327197,-3.948945,8.074475,-5.645358,8.076724,-4.893557,8.527734,-5.166661,8.805831]]], dtype = "float64")#candidate|4220|(2, 4, 11)|const|float64
uop_4221 = relay.atan(const_4220.astype('float64')) # shape=(2, 4, 11)
func_3786_call = mod.get_global_var('func_3786')
func_3788_call = mutated_mod.get_global_var('func_3788')
call_4229 = relay.TupleGetItem(func_3786_call(), 0)
call_4230 = relay.TupleGetItem(func_3788_call(), 0)
var_4232 = relay.var("var_4232", dtype = "float64", shape = (2, 4, 11))#candidate|4232|(2, 4, 11)|var|float64
bop_4233 = relay.logical_and(uop_4221.astype('bool'), relay.reshape(var_4232.astype('bool'), relay.shape_of(uop_4221))) # shape=(2, 4, 11)
bop_4239 = relay.minimum(bop_4233.astype('uint8'), relay.reshape(uop_4221.astype('uint8'), relay.shape_of(bop_4233))) # shape=(2, 4, 11)
func_3862_call = mod.get_global_var('func_3862')
func_3863_call = mutated_mod.get_global_var('func_3863')
call_4243 = func_3862_call()
call_4244 = func_3862_call()
func_4068_call = mod.get_global_var('func_4068')
func_4070_call = mutated_mod.get_global_var('func_4070')
var_4251 = relay.var("var_4251", dtype = "float64", shape = (1155,))#candidate|4251|(1155,)|var|float64
call_4250 = relay.TupleGetItem(func_4068_call(relay.reshape(var_4251.astype('float64'), [7, 11, 15])), 3)
call_4252 = relay.TupleGetItem(func_4070_call(relay.reshape(var_4251.astype('float64'), [7, 11, 15])), 3)
output = relay.Tuple([call_4229,bop_4239,call_4243,call_4250,var_4251,])
output2 = relay.Tuple([call_4230,bop_4239,call_4244,call_4252,var_4251,])
func_4276 = relay.Function([var_4232,var_4251,], output)
mod['func_4276'] = func_4276
mod = relay.transform.InferType()(mod)
var_4277 = relay.var("var_4277", dtype = "float64", shape = (2, 4, 11))#candidate|4277|(2, 4, 11)|var|float64
var_4278 = relay.var("var_4278", dtype = "float64", shape = (1155,))#candidate|4278|(1155,)|var|float64
output = func_4276(var_4277,var_4278,)
func_4279 = relay.Function([var_4277,var_4278,], output)
mutated_mod['func_4279'] = func_4279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3351_call = mod.get_global_var('func_3351')
func_3352_call = mutated_mod.get_global_var('func_3352')
call_4356 = func_3351_call()
call_4357 = func_3351_call()
output = relay.Tuple([call_4356,])
output2 = relay.Tuple([call_4357,])
func_4378 = relay.Function([], output)
mod['func_4378'] = func_4378
mod = relay.transform.InferType()(mod)
output = func_4378()
func_4379 = relay.Function([], output)
mutated_mod['func_4379'] = func_4379
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4398 = relay.var("var_4398", dtype = "float64", shape = (6, 7, 13))#candidate|4398|(6, 7, 13)|var|float64
uop_4399 = relay.cos(var_4398.astype('float64')) # shape=(6, 7, 13)
var_4401 = relay.var("var_4401", dtype = "float64", shape = (6, 7, 13))#candidate|4401|(6, 7, 13)|var|float64
bop_4402 = relay.subtract(uop_4399.astype('float64'), relay.reshape(var_4401.astype('float64'), relay.shape_of(uop_4399))) # shape=(6, 7, 13)
bop_4406 = relay.right_shift(bop_4402.astype('int32'), relay.reshape(uop_4399.astype('int32'), relay.shape_of(bop_4402))) # shape=(6, 7, 13)
func_2276_call = mod.get_global_var('func_2276')
func_2280_call = mutated_mod.get_global_var('func_2280')
var_4426 = relay.var("var_4426", dtype = "uint8", shape = ())#candidate|4426|()|var|uint8
const_4427 = relay.const([[-7,4,-1],[7,4,4],[10,6,-6],[8,-8,8],[-6,2,-10],[1,-3,-9],[3,-4,1],[-4,8,8],[-4,3,-3],[-8,7,6],[-10,5,1],[-10,7,1],[1,-7,-5],[6,-3,9],[-10,-4,1],[-4,-6,6],[2,-4,-7],[-7,10,1],[2,5,8],[3,5,5],[-9,6,-8],[5,-8,9],[3,6,-3],[-9,6,-2],[9,4,-7],[1,8,1],[10,5,4],[3,-1,1],[8,1,-5],[2,-10,-10],[-5,-3,8],[8,2,8],[-7,-1,4],[4,-3,7],[8,2,6],[-7,2,-4],[3,-10,5],[-1,1,-5],[-6,-6,-2],[5,-4,7],[10,1,-3],[-2,-6,3],[10,-8,-8],[3,-9,-2],[-4,10,7],[-10,-3,-7],[-5,-3,1],[6,2,10],[6,5,-6],[6,-6,-8],[6,-10,-8],[-5,5,-5],[6,8,5],[9,3,7],[-10,9,-1],[-1,-6,6],[-7,6,1],[-8,5,4],[-4,-1,6],[8,1,4],[-6,-1,-5],[6,-7,5],[6,-4,9],[-10,2,2],[1,6,9],[4,-6,-10],[1,4,-6],[8,2,2],[-2,6,6],[-4,10,-9],[-9,-8,9],[7,-2,9],[-9,2,9],[-5,-8,6],[1,-1,7],[1,4,-2],[-7,-4,-1],[-7,-10,-4],[-2,-9,-1],[6,-5,2],[8,10,5],[6,3,1],[3,-4,8],[1,8,2],[-6,-1,5],[5,-1,7],[8,-9,5],[5,-9,-2],[-9,-9,-6],[-8,1,-5],[5,2,-4],[-3,4,1],[2,-1,7],[10,-8,-2],[-1,-1,10],[-9,-6,2],[-9,10,6],[7,9,1],[-1,1,1],[8,-2,6],[-4,8,5],[-8,2,10],[-3,-6,-6],[8,9,9],[-3,-3,5],[-8,4,9],[-5,-6,6],[4,4,2],[6,-7,1],[6,4,-10],[1,-10,-3],[4,7,-4],[-5,-10,8],[-9,4,-1],[4,1,-9],[1,-1,4],[-1,2,8],[8,-4,-4],[-2,1,1],[-3,1,4],[-6,-1,3],[1,-4,1],[10,-5,10],[9,2,-10],[-3,-7,10],[6,4,3],[1,-1,-8],[4,2,4],[-9,-3,-2],[2,-7,-10],[8,-3,3],[10,-1,-8],[-5,-6,-4],[-10,3,3],[-8,1,-6],[2,-8,8],[2,-5,3],[9,10,9],[-6,-8,-2],[-4,-8,8],[7,1,9],[-7,9,2],[-7,-2,-8],[10,7,5],[-9,-4,6],[-4,-5,10],[-4,3,-1],[7,-9,5],[-7,-3,3],[8,7,-2],[5,7,10],[-2,-6,-10],[-3,5,6],[-9,-4,-1],[-2,-10,2],[-3,-5,7],[-8,4,7],[9,10,9],[-3,-1,3],[-4,3,-4],[-6,-2,-7],[-8,9,9],[5,3,3],[3,2,-4],[10,-2,2],[5,-2,8],[-7,4,-10],[9,2,-3],[6,10,-4],[5,-4,4],[-2,5,10],[-3,2,1],[2,-9,2],[7,10,5],[4,7,-6],[6,-3,-2],[-4,10,-2],[-10,-10,9],[1,-1,-5],[-6,-8,-9],[-5,2,3],[3,-9,-3],[-3,-7,2],[-9,2,-5],[-8,-6,-3],[3,-9,9],[9,9,-4],[-8,7,-2],[-9,-5,10],[-8,10,-9],[10,-4,6],[-10,5,10],[-4,-6,6],[-2,-8,-8],[7,-9,1],[-2,9,-7],[-9,-10,6],[6,10,3],[-2,1,-1],[10,-4,-7],[-8,-5,4],[2,10,-10],[3,8,-9],[-9,5,-1],[-8,8,-2],[8,-3,7],[-4,-3,-2],[-3,-8,-8],[2,-8,-7],[7,9,-9],[8,9,8],[-9,4,9],[6,10,-2],[10,6,-5],[6,8,7],[6,-5,-9],[2,7,1],[-3,7,10],[2,5,10],[8,-2,-3],[6,-6,-6],[-5,-2,-6],[8,9,-3],[-7,7,-2],[4,4,8],[6,-7,-6],[7,5,4],[4,3,9],[10,-10,10],[5,1,9],[-5,3,5],[-8,9,-4],[5,6,9],[3,-1,-6],[4,-2,-1],[4,6,-9],[-9,5,-10],[-2,7,2],[-3,-5,7],[-3,3,8],[8,9,1],[7,6,-7],[-3,9,7],[7,-6,2],[4,-4,5],[-2,-6,-9],[10,5,9],[10,1,3],[-3,-7,1],[-4,-7,3],[-2,4,-7],[-3,10,10],[-1,1,-2],[-3,-5,5],[10,-10,-8],[8,9,6],[-7,-10,8],[-6,2,5],[2,-10,8],[2,5,-2],[6,-2,2],[-10,8,3],[1,9,7],[-9,1,7],[-5,7,2],[10,9,-4],[10,9,-5],[4,-4,-9],[-6,-3,8],[-8,10,10],[7,9,-3],[-7,6,-1],[-2,6,9],[-8,-4,5],[10,4,1],[1,5,3],[2,3,10],[8,-10,-8],[10,5,5],[-7,-3,7],[6,-1,-8],[10,-6,10],[8,6,4],[8,-9,9],[5,1,10],[4,-5,-8],[-1,3,-3],[3,-2,-1],[4,10,4],[-7,7,7],[-7,-3,5],[-5,2,-4],[-2,-6,10],[9,-7,-7],[-8,10,-6],[3,5,6],[-7,-8,3],[-4,1,-9],[9,6,9],[-9,-10,4],[-3,9,-3],[9,8,-1],[-9,5,-8],[2,-4,-7],[2,10,4],[-7,-1,8],[1,-7,5],[9,-4,-6],[1,-2,-6],[8,5,-9],[-3,8,1],[9,-3,3],[4,-4,6],[-3,-9,4],[5,5,-1],[1,-9,8],[-6,5,3],[9,-10,6],[-6,5,-3],[3,10,-8],[-10,-4,7],[-2,1,4],[3,-9,-10],[-9,3,2],[-2,4,2],[-2,10,-3],[10,-1,3],[6,3,-9],[2,1,-1],[-1,-7,4],[6,2,-3],[-2,2,-7],[1,1,9],[-8,7,6],[2,2,2],[-1,-3,4],[-9,3,2],[-6,-3,8],[6,-5,-5],[10,10,-9],[7,3,-2],[-8,-5,-4],[-10,1,-7],[7,7,4],[-3,-9,8],[7,7,-7],[-9,4,5],[1,8,1],[3,7,-10],[-1,-7,7],[-8,1,6],[-8,5,9],[8,7,1],[1,8,3],[-1,2,-5],[-5,7,10],[-6,-8,-10],[10,6,4],[-7,-1,-3],[4,9,3],[-9,6,-4],[7,7,-10],[-2,-5,-8],[-6,-3,4],[3,1,-6],[-3,3,-10],[10,-7,-5],[-3,7,-5],[-6,4,8],[-5,-5,-3],[9,7,7],[-8,-5,3],[-4,-6,4],[-8,2,10],[-9,1,1],[7,9,-3],[9,3,-8],[3,5,-3],[-1,-1,-4],[-3,6,-6],[-9,9,7],[6,3,4],[-10,-5,8],[-5,-10,4],[-7,-6,-2],[-2,-9,2],[-2,6,2],[9,6,-6],[-4,5,-7],[-10,5,-9],[-2,9,3],[7,-10,3],[2,-3,-7],[-7,9,-5],[-1,3,10],[-5,5,4],[-5,-3,6],[8,-9,-8],[-9,-5,7],[7,4,-5],[1,9,-2],[-4,-5,-4],[5,9,-1],[8,4,-10],[-5,10,-6]], dtype = "uint8")#candidate|4427|(405, 3)|const|uint8
call_4425 = relay.TupleGetItem(func_2276_call(relay.reshape(var_4426.astype('uint8'), []), relay.reshape(const_4427.astype('uint8'), [9, 9, 15]), ), 1)
call_4428 = relay.TupleGetItem(func_2280_call(relay.reshape(var_4426.astype('uint8'), []), relay.reshape(const_4427.astype('uint8'), [9, 9, 15]), ), 1)
func_4041_call = mod.get_global_var('func_4041')
func_4044_call = mutated_mod.get_global_var('func_4044')
const_4434 = relay.const([[-4.057423,1.380032,-8.709102,-8.803441],[6.241572,1.758086,-9.374942,6.052742],[-3.836336,-7.006081,-7.604692,-9.677831],[-4.540418,-2.395676,2.347732,3.303537],[-2.318656,4.890584,-2.755985,-1.211203],[0.305560,0.912698,-0.083655,-0.251777],[-7.233198,-8.459637,8.572765,7.327338],[-8.283826,-6.458308,4.986433,-8.129801],[9.702214,-9.498035,1.164835,6.461495],[9.659194,-3.145243,5.767260,-0.422194],[5.651005,-0.505140,-7.719380,-9.187746],[5.796154,-9.780570,-9.996284,-3.500803],[-4.511568,6.566599,7.466478,-5.527293],[-4.151532,-1.105575,6.191179,5.864763],[-7.481033,5.198567,-3.317733,9.709687],[4.580999,-3.575088,-5.942006,6.892859],[4.098729,-0.996447,7.149492,1.032967],[0.386484,2.634111,7.531496,-3.489182],[-8.254059,-5.182772,0.299556,-9.470900],[2.140857,8.525516,-0.756087,-7.308869],[1.643693,-0.566474,8.524188,-8.700979],[-6.165582,1.192156,9.117622,8.661332],[-4.667664,-6.342488,8.981416,-2.509405],[7.829175,7.366202,-6.197546,8.781939],[-5.813138,-1.458186,-8.896716,1.081114],[-9.865940,-4.841689,-5.954944,4.429562],[9.941169,-7.757683,-4.168350,8.183519],[-3.800150,3.869090,-2.829141,3.807209],[8.391610,-4.733204,-9.011498,-2.967094],[-9.093700,-1.760145,-7.444648,1.152158],[9.083105,-5.799128,-0.241581,9.918657],[-6.393737,6.366216,-5.744421,-2.743729],[-7.435051,6.993621,-0.624459,4.347309],[-6.469878,8.871111,7.798187,-1.791597],[-1.368945,7.862836,-4.809527,-0.425593],[9.760111,3.911131,-0.024095,1.191065],[-3.728126,0.645806,-8.289143,1.358794],[4.085777,1.067426,-7.249728,8.011915],[1.728256,0.890968,-4.320539,-3.741343],[-2.365173,6.668406,8.814349,2.502929],[1.510363,-4.950036,-2.311243,-3.317781],[-4.458339,-7.153964,8.257438,-4.283194],[-5.654189,-0.791669,0.265579,2.107689],[-3.267836,-0.861094,1.677467,2.456703],[-0.771372,6.510180,7.449921,-8.892179],[3.141608,-0.012925,0.475602,4.347444],[5.438432,-2.666165,8.271716,-5.630005],[-9.035626,6.410878,-9.928265,-9.198537],[6.368210,5.333058,9.018253,-7.879572],[5.909444,7.292992,5.456406,-1.936862],[-3.540234,6.288613,-4.500806,5.783388],[-8.557408,2.027013,1.874996,-0.556278],[9.965731,8.504179,2.188971,3.924255],[7.459733,9.958578,-1.992552,1.324749],[-2.643771,-0.784287,-3.502412,0.885712],[-6.438383,1.526703,-8.782824,-8.796629],[-7.760660,-5.581604,-1.752142,-2.723017],[-0.783087,-2.765773,1.999637,4.220822],[2.755386,2.112047,5.907747,-1.660412],[8.364421,2.827019,1.269439,0.371399],[-0.726682,-1.957958,0.601079,-9.870398],[-7.132533,-8.036811,-5.354131,-9.387142],[3.120280,3.932833,-4.885314,0.054675],[3.450702,-5.045996,-8.790042,-2.860047],[4.751228,3.829341,4.614934,2.025675],[0.789194,-0.848242,9.188661,1.366595],[-0.159829,-8.941421,-0.113728,-5.856889],[-2.518766,3.341473,-2.772960,6.213504],[-7.400997,-6.060220,-3.457876,6.750234],[-8.825134,5.711443,-5.857408,-4.583278],[3.260636,-1.770646,-0.800863,-8.908030],[4.289407,-2.998993,3.940070,8.279992],[-9.933560,-6.723989,9.337746,-7.672700],[1.887971,-7.264835,-9.587112,-2.375047],[7.274318,-2.685943,4.829707,-3.281298],[-7.639324,-4.789348,6.467856,7.115652],[2.888295,-8.350059,9.148437,-9.176715],[3.523380,6.571620,-2.029124,5.098496],[-7.316637,1.292562,-4.407136,-8.977851],[-2.747679,2.891379,-6.408239,-4.020803],[-4.353119,5.870473,4.775074,-5.922217],[-3.106626,3.371530,5.542211,-2.598120],[-5.942594,5.737733,1.249333,9.959357],[-1.966990,8.842816,0.776811,-3.364840],[3.364414,1.358828,-0.087804,2.711370],[2.715559,6.322415,6.072866,-1.113956],[4.514080,0.866579,7.172310,0.243492],[1.952294,9.292991,-6.553356,-7.932659],[0.203270,-3.089276,8.587500,-2.775810],[-2.289768,0.196099,8.403431,9.169286],[3.092147,2.854435,1.290717,-0.234608],[-5.517807,1.847172,6.056088,-1.437557],[-1.868134,-3.965511,-0.455719,-9.767221],[-0.177542,-5.228552,-5.406379,7.761669],[-6.667419,-7.458568,4.957706,-8.020176],[-4.971214,-9.448175,7.200135,-3.524153],[0.171032,0.416813,0.303371,2.348575],[7.296007,9.976595,3.958167,6.632404],[-3.202533,-9.563349,-8.179343,0.810570],[-0.743071,5.863556,-2.256405,8.859689],[-0.343228,4.261547,2.089797,-1.075661],[-7.913761,-4.435736,-8.041378,-4.696250],[8.205413,-3.849614,1.205237,5.243715],[1.973414,-4.519637,-0.786208,0.790480],[-8.256410,6.301844,3.177220,0.442898],[7.248603,-5.070207,4.973016,-7.780827],[2.925249,2.411019,-5.691295,-2.877076],[5.899427,5.786980,9.766878,-2.292687],[2.259256,7.002911,1.857816,5.298766],[-9.069181,-9.806693,-9.951596,-0.443650],[7.346306,-6.936675,-5.344532,1.001122],[3.446183,-3.634589,-5.292078,9.524689],[-3.096608,-4.323278,3.271870,-9.327993],[2.728042,1.826940,-9.343413,3.429156],[8.862335,0.908228,5.297727,5.652089],[-6.751630,8.350350,6.063640,-1.326730],[9.609691,6.793896,-0.341072,-8.808076],[7.302721,5.588922,1.642304,7.389400],[1.725720,8.351537,-2.642547,7.835864],[-1.931450,2.657661,3.923517,2.586358],[-2.477191,7.373043,-3.459936,2.912915],[-6.438405,6.865568,0.098170,-4.549160],[-7.746799,2.780379,6.039959,2.994526],[0.292711,9.143253,-1.660694,4.296137],[4.387734,-2.015162,-3.888369,8.666739],[-8.227805,2.287341,-8.562882,-3.541668],[3.302736,6.781345,2.314261,-1.943725],[3.469069,3.783773,-1.114057,-0.082870],[-5.151720,7.913371,-8.071230,4.814175],[-0.371760,5.537869,-6.092521,8.218909],[2.527003,-2.271869,1.090716,-2.030538],[-6.667042,-4.180901,-3.716586,4.266417],[1.213272,-4.587416,7.684503,6.262704],[-6.388245,-8.485348,-4.351347,-4.154399],[-5.624041,-3.769946,1.968550,-9.852592],[7.166869,-2.141504,-9.597733,-7.278266],[-3.928443,3.096299,-9.643340,6.653299],[3.049964,5.602727,4.381395,-7.027752],[8.402125,2.882974,8.226922,-0.617541],[9.006232,-7.086464,-8.973989,1.441776],[8.135881,0.434708,7.030650,-3.935696],[-5.063880,0.359655,4.925771,-9.755149],[-0.333084,8.604862,8.512216,-4.651091],[-1.016282,-3.659649,6.579298,-8.991092],[2.601064,-8.597346,-6.577632,2.427359],[6.885101,9.849642,-5.243851,1.087650],[3.025185,-9.384217,-6.267352,4.886234],[-4.554306,-4.597186,-5.497170,-5.898105],[-2.695507,-5.500076,-2.856466,6.423609],[-3.614397,-1.240134,-2.206776,-6.637334],[3.819384,9.690969,6.069848,-2.178541],[-7.149155,-1.972746,9.282566,-4.541325],[0.868062,5.332742,5.858324,1.659701],[4.317128,-0.634455,8.331608,3.382936],[-6.339366,4.638830,-1.356613,2.319741],[-2.632124,9.018621,-3.119379,8.744551],[-1.653563,6.204001,6.349390,-8.085960],[4.882170,9.900180,7.894121,5.662315],[6.944749,7.712837,-3.187771,-9.700731],[-4.048786,5.055860,-1.733149,7.712368],[2.757901,-4.310919,7.038031,2.217082],[8.237888,-7.367285,3.222902,-6.995397],[-2.347295,-4.224273,-3.955580,3.827424],[-5.347158,-2.933231,6.119582,-6.896642],[-1.041827,4.878600,1.869345,-9.469426],[6.110223,7.619489,-4.702043,5.137043],[6.641427,-0.336740,6.640600,9.430867],[-4.625469,-1.352540,0.467307,-5.707282],[3.934108,1.661682,-7.777014,0.950984],[-9.613988,-6.743068,4.169391,1.965591],[-4.381708,-1.535892,7.483315,3.848921],[0.198441,5.014954,-8.730046,9.312832],[-8.051453,-5.702915,-3.052930,-2.891478],[-7.009144,-8.175760,2.271298,0.428324],[0.977308,4.855920,1.303106,-4.316537],[-6.663118,3.642819,4.679250,-3.199425],[5.359347,-2.865975,-9.395500,3.315656],[0.006254,-2.702003,3.286266,-4.340360],[-9.341394,-0.224294,3.511100,-1.386925],[-2.105355,-3.128885,-4.201043,6.466264],[-1.329272,-0.816398,9.062230,3.700246],[5.327336,1.830552,3.353449,3.119670],[4.393012,1.580200,-4.383753,-1.733089],[8.997216,-2.003354,3.978572,-3.526486],[5.350496,-8.637199,-7.305672,7.843450],[-1.251296,-6.243288,1.341010,6.891923],[5.628968,1.457268,-7.668669,1.521594],[-5.951050,-1.089662,3.648141,9.063977],[7.635332,9.243784,-6.936623,3.886825],[1.671975,-4.423867,7.932949,7.253379],[1.336262,-2.884698,-4.137527,4.384653],[8.690322,-6.306731,-2.230701,6.985651],[-6.286894,9.946212,8.794236,6.916169],[6.150292,3.252312,0.197662,0.213118],[3.610795,-2.667271,1.742359,5.314313],[9.724788,-4.349369,0.301198,4.008653],[-0.158668,-0.865622,6.147030,9.659766],[-7.087377,1.666280,3.407136,-9.007569],[-8.790378,0.004542,-7.399665,-9.018065],[-3.265132,-9.961220,-4.022359,1.653387],[-8.651773,0.735072,3.758726,-7.285448],[7.910548,7.700618,5.676649,-4.989001],[2.319908,1.479198,-1.098678,8.373865],[-3.053756,-8.130422,-2.063849,-6.568202],[-4.320791,-4.518531,-0.626142,0.311552],[5.287057,-6.210413,-5.672054,-3.551618],[-8.939918,1.905944,-2.943380,-8.441792],[-4.435417,6.950313,-7.916938,-6.488179],[4.253275,0.702115,0.843205,-5.530670],[8.157272,1.900592,6.552248,0.092309],[-1.720961,-8.128119,-1.878479,8.133980],[1.855490,5.210095,-3.184950,-0.787702],[-6.596374,2.469889,-4.770660,-3.706321],[3.966177,0.270830,-3.241011,-4.113868],[-1.409682,1.866332,3.774378,0.502731],[2.731566,0.996653,-6.089745,-7.626285]], dtype = "float32")#candidate|4434|(216, 4)|const|float32
call_4433 = relay.TupleGetItem(func_4041_call(relay.reshape(const_4434.astype('float32'), [6, 9, 16])), 0)
call_4435 = relay.TupleGetItem(func_4044_call(relay.reshape(const_4434.astype('float32'), [6, 9, 16])), 0)
func_3351_call = mod.get_global_var('func_3351')
func_3352_call = mutated_mod.get_global_var('func_3352')
call_4437 = func_3351_call()
call_4438 = func_3351_call()
func_3982_call = mod.get_global_var('func_3982')
func_3984_call = mutated_mod.get_global_var('func_3984')
call_4447 = relay.TupleGetItem(func_3982_call(relay.reshape(const_4427.astype('uint8'), [1215,])), 1)
call_4448 = relay.TupleGetItem(func_3984_call(relay.reshape(const_4427.astype('uint8'), [1215,])), 1)
output = relay.Tuple([bop_4406,call_4425,var_4426,const_4427,call_4433,const_4434,call_4437,call_4447,])
output2 = relay.Tuple([bop_4406,call_4428,var_4426,const_4427,call_4435,const_4434,call_4438,call_4448,])
func_4454 = relay.Function([var_4398,var_4401,var_4426,], output)
mod['func_4454'] = func_4454
mod = relay.transform.InferType()(mod)
mutated_mod['func_4454'] = func_4454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4454_call = mutated_mod.get_global_var('func_4454')
var_4456 = relay.var("var_4456", dtype = "float64", shape = (6, 7, 13))#candidate|4456|(6, 7, 13)|var|float64
var_4457 = relay.var("var_4457", dtype = "float64", shape = (6, 7, 13))#candidate|4457|(6, 7, 13)|var|float64
var_4458 = relay.var("var_4458", dtype = "uint8", shape = ())#candidate|4458|()|var|uint8
call_4455 = func_4454_call(var_4456,var_4457,var_4458,)
output = call_4455
func_4459 = relay.Function([var_4456,var_4457,var_4458,], output)
mutated_mod['func_4459'] = func_4459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3351_call = mod.get_global_var('func_3351')
func_3352_call = mutated_mod.get_global_var('func_3352')
call_4461 = func_3351_call()
call_4462 = func_3351_call()
func_3623_call = mod.get_global_var('func_3623')
func_3626_call = mutated_mod.get_global_var('func_3626')
var_4464 = relay.var("var_4464", dtype = "float64", shape = (26, 7))#candidate|4464|(26, 7)|var|float64
call_4463 = relay.TupleGetItem(func_3623_call(relay.reshape(var_4464.astype('float64'), [182,])), 1)
call_4465 = relay.TupleGetItem(func_3626_call(relay.reshape(var_4464.astype('float64'), [182,])), 1)
uop_4467 = relay.tan(call_4463.astype('float64')) # shape=(2, 7, 13)
uop_4469 = relay.tan(call_4465.astype('float64')) # shape=(2, 7, 13)
bop_4472 = relay.bitwise_xor(var_4464.astype('uint8'), relay.reshape(call_4463.astype('uint8'), relay.shape_of(var_4464))) # shape=(26, 7)
bop_4475 = relay.bitwise_xor(var_4464.astype('uint8'), relay.reshape(call_4465.astype('uint8'), relay.shape_of(var_4464))) # shape=(26, 7)
output = relay.Tuple([call_4461,uop_4467,bop_4472,])
output2 = relay.Tuple([call_4462,uop_4469,bop_4475,])
func_4478 = relay.Function([var_4464,], output)
mod['func_4478'] = func_4478
mod = relay.transform.InferType()(mod)
mutated_mod['func_4478'] = func_4478
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4479 = relay.var("var_4479", dtype = "float64", shape = (26, 7))#candidate|4479|(26, 7)|var|float64
func_4478_call = mutated_mod.get_global_var('func_4478')
call_4480 = func_4478_call(var_4479)
output = call_4480
func_4481 = relay.Function([var_4479], output)
mutated_mod['func_4481'] = func_4481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3862_call = mod.get_global_var('func_3862')
func_3863_call = mutated_mod.get_global_var('func_3863')
call_4507 = func_3862_call()
call_4508 = func_3862_call()
output = relay.Tuple([call_4507,])
output2 = relay.Tuple([call_4508,])
func_4517 = relay.Function([], output)
mod['func_4517'] = func_4517
mod = relay.transform.InferType()(mod)
output = func_4517()
func_4518 = relay.Function([], output)
mutated_mod['func_4518'] = func_4518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4517_call = mod.get_global_var('func_4517')
func_4518_call = mutated_mod.get_global_var('func_4518')
call_4522 = relay.TupleGetItem(func_4517_call(), 0)
call_4523 = relay.TupleGetItem(func_4518_call(), 0)
func_3221_call = mod.get_global_var('func_3221')
func_3224_call = mutated_mod.get_global_var('func_3224')
var_4541 = relay.var("var_4541", dtype = "int64", shape = (189,))#candidate|4541|(189,)|var|int64
call_4540 = relay.TupleGetItem(func_3221_call(relay.reshape(var_4541.astype('int64'), [189,])), 1)
call_4542 = relay.TupleGetItem(func_3224_call(relay.reshape(var_4541.astype('int64'), [189,])), 1)
func_3786_call = mod.get_global_var('func_3786')
func_3788_call = mutated_mod.get_global_var('func_3788')
call_4546 = relay.TupleGetItem(func_3786_call(), 0)
call_4547 = relay.TupleGetItem(func_3788_call(), 0)
func_4085_call = mod.get_global_var('func_4085')
func_4088_call = mutated_mod.get_global_var('func_4088')
const_4574 = relay.const([5.652091,4.849566,-8.614897,-4.875989,2.535287,9.361929,-8.739891,2.375727,-7.736743,6.184974,-9.610711,3.863135,-4.439576,-9.041947,4.185919,0.587426,-7.286719,6.285489,-6.730897,-8.943114,3.379069,2.216331,-6.762686,-1.694510,-6.756424,4.647383,-2.104245,6.058894,-9.984478,-1.512461,-5.701877,-5.680644,6.339514,6.070187,8.043834,9.420058,0.403547,-4.393387,4.344511,8.997729,-0.556266,-2.441351,4.452933,3.089144,0.590790,-9.209572,-8.352656,0.107325,-9.331224,4.266703,-8.232219,-7.552385,6.208451,5.638402,5.272524,-1.607379,-5.925573,8.050969,6.070834,9.389475,-4.398932,-9.447783,-7.321998,-7.591117,-2.591886,-9.290944,-2.962506,3.710555,3.745708,-5.395834,4.958021,6.676460,9.324501,8.362905,3.320265,-5.005911,-4.708220,-4.342803,-2.118551,-6.365661,-6.458986,6.543232,5.961558,-1.681789,-9.111626,-1.119921,-6.249904,1.662889,-1.819626,-2.357134,6.519568,3.895541,3.896197,-0.366485,6.354434,-9.436912,4.240572,-0.463732,-6.591860,0.632909,-6.416790,-9.723914,1.415945,-5.481194,0.298289,-8.378416,8.145856,-0.444229,7.163528,-7.583510,4.861684,6.532150,4.317736,-4.694771,-9.232667,-1.525449,2.484875,5.861386,-0.293690,-4.845495,-0.104663,-8.206013,-0.828254,-1.303414,2.833371,-8.425021,-1.026770,9.517753,-3.712135,7.703054,3.815775,3.218757,1.927204,-9.022298,-2.787716,4.742755,2.420139,6.057488,-1.811864,4.164758,-0.137039,7.644365,7.703225,-9.771868,-1.206217,2.084220,5.293605,-9.378167,9.264128,-8.929458,4.521133,5.489298,7.607122,-0.316773,-1.598798,5.113923,-3.049830,6.349143,4.851588,2.901404,-2.033970,-7.650711,0.908822,-9.413512,0.188091,-1.277968,-9.227959,6.673428,-0.217865,5.341274,4.434309,-0.923983,3.251256,-4.548160,4.534965,-2.480515,-7.504689,-4.600927,0.709915,-6.980743,4.919371,6.653918,-7.727254,-2.793481,8.232655,-3.199692,-8.630748,-4.033982,-5.379652,8.141279,-8.895693,8.173342,-1.593029,-3.601351,-6.636162,-1.661888,6.174909,6.502261,-9.501589,7.037035,-9.672365,-3.383395,-9.099443,-6.182181,1.542990,-6.707745,-5.497337,-7.362933,2.324704,-8.005559,-1.916368,-6.537533,2.382119,4.336250,0.490523,6.700996,-6.379673,-4.234919,-1.795177,-1.141447,-6.722500,7.490505,-5.839893,0.202189,-6.182205,-9.870606,-0.843962,-6.840689,-4.158850,5.443678,-6.218052,9.358809,5.249221,2.193731,8.070693,5.001274,7.039170,-9.599886,3.972771,6.064396,2.598502,-1.475386,-8.536794,5.882085,-8.912353,-5.865690,5.455424,-2.431446,-5.046231,-7.502828,2.208624,2.156774,-6.663006,-5.538503,-1.722593,5.114572,8.561443,2.444664,8.744357,8.126623,-6.002875,-2.014536,8.426641,-0.968195,7.763105,1.586169,-1.870734,6.477570,-7.140949,-2.343957,1.654208,6.155165,5.475008,0.825395,6.410905,5.752558,-9.686024,-3.485123,-6.113110,2.785095,1.791400,-6.432578,-6.828116,6.105128,7.889540,8.265980,8.885208,-7.305385,2.626245,4.458643,-1.515444,-9.597925,3.800620,-3.063545,6.298041,7.301799,5.709489,3.763298,5.293821,-8.931429,-8.867242,4.504805,-6.766275,9.469923,5.416837,4.062160,1.101528,4.255681,-4.040887,-8.683004,9.976339,-3.870059,3.425309,-0.146202,-1.635296,8.302358,-2.687221,5.530341,-1.302632,5.552643,6.500742,0.115131,-1.365921,3.479588,6.000027,2.858976,0.853871,3.034333,3.755637,1.535341,-8.460663,-9.819295,-2.828973,-1.561421,-9.714363,-2.036057,-4.341668,-9.410731,-8.395739,6.606659,0.680999,9.339111,-2.178862,8.794096,-3.244420,-5.035485,-3.042014,-4.210120,-4.525286,5.889219,-2.305455,-5.085933,-2.407459,5.343174,9.036914,-5.692919,9.308859,1.081664,-0.854316,3.429404,-4.265081,2.963997,1.554423,0.857007,-3.538205,-5.922668,-3.847923,1.381829,-3.241125,-2.311491,2.302306,-8.474600,-6.134833,6.889387,3.717230,5.802158,-4.898194,-9.382175,-2.692808,0.444050,-4.451659,1.695817,-0.634946,3.217438,-3.202917,-1.897477,-5.727881,-9.886499,6.645350,7.218017,1.084252,-8.520339,-5.945708,1.773079,-6.124674,4.463697,-8.886828,0.214489,-9.174623,1.242486,-6.608612,-5.530982,5.569075,3.437487,-6.492509,5.457088,-0.107139,1.532705,-7.758612,3.427118,9.015935,2.996862,-9.379459,2.634803,-5.823981,4.193681,-7.841544,9.977611,-5.470342,-5.491046,-0.225053,-1.262727,1.852983,1.048893,-2.515677,-5.016436,5.766200,-3.592738,3.839193,-8.609011,-7.955222,-7.783572,-7.979233,-9.966792,5.746750,5.020413,-9.934721,-1.268834,-8.935160,0.491263,-1.920909,-7.523981,-6.107666,9.482132,-0.887490,2.239235,8.692350,-5.885302,3.240910,4.659858,0.933024,-7.984190,-4.864203,-8.676008,-6.934585,-4.775314,1.962163,8.487111,6.357011,7.226947,-6.302006,-6.130988,3.925492,0.221694,-3.086836,4.400982,-8.409659,5.691986,-9.686614,3.449739,-7.295740,9.607746,-9.843115,8.017731,-3.828383,-7.431912,7.651115,-9.003263,0.036182,2.743878,-0.693397,3.325693,7.817573,-7.108763,-0.048985,-5.335817,7.621796,0.101510,-2.790277,3.276889,2.818665,-2.570329,-9.400660,4.268897,-6.197273,6.373905,1.915392,4.199247,-7.562702,-9.264600,8.722494,8.934774,0.123439,0.608023,4.554326,-9.384686,-9.933530,9.716823,0.385522,-0.405667,3.183226,4.269841,-8.445061,1.344277,-4.835893,-9.695893,6.036381,-4.807021,-5.842985,-9.025035,-7.554014,-6.240695,4.933322,3.828161,2.872391,3.222829,-0.118099,3.060316,5.618892,8.976965,6.162186,-6.285232,4.255175,5.766153,-7.819886,9.579143,-9.653763,0.837693,0.195891,-4.981233,-6.637981,5.581138,-5.584564,0.732275,-7.769638,1.807647,-8.215563,-3.610739,-0.785773,4.400999,1.639935,5.996640,4.165701,-3.485937,-4.340057,6.225022,-0.317072,2.583512,2.098155,-8.804669,3.253414,8.982433,7.321174,7.193471,3.445695,-3.545293,7.339870,-1.373120,-9.295943,5.466623,-8.702017,7.446965,8.135314,0.121329,-2.911467,-4.944557,-3.910071,0.906894,0.031593,1.907275,-9.076946,-0.921533,-1.277432,-7.590362,9.671966,3.365702,-8.493891,-5.830253,1.734426,-7.624618,2.415704,5.326354,0.363901,-2.928719,4.260416,7.973879,9.782188,0.746230,8.518190,2.827429,7.701273,-1.518962,4.134941,0.240728,-1.717596,-4.126556,8.488931,5.015184,3.107948,0.422328,-6.783168,-1.238131,-8.082909,4.433927,8.616107,-0.402580,0.937321,-1.369254,3.591885,1.230441,3.481606,-5.433063,7.044322,1.122181,7.084098,6.389534,-5.279036,1.566225,8.133957,-6.081448,4.900110,9.449689,9.212723,-9.979866,8.234405,-0.635597,6.585335,8.254683,1.758244,8.378217,-3.489048,-0.153675,-9.904135,1.003255,-8.018985,-3.268164,9.852856,-1.235246,3.435611,6.574133,-4.159163,-7.198343,-5.965890,-6.767172,-5.870173,-8.914533,-9.646440,9.820737,3.134181,-7.989882,-8.413479,7.765715,-5.168059,-4.856435,-8.372905,-3.241063,-0.822519,5.691376,9.522750,-6.740653,7.857337,-3.037008,7.856515,6.621559,-4.690459,-3.102953,-3.620084,-4.456363,4.133636,9.613992,2.757910,-2.863359,-0.806847,-4.452392,0.139489,1.436094,-5.741862,-6.888955,-1.534122,-7.975055,2.196149,5.879447,-1.657303,-4.826735,5.985499,-7.312270,7.545400,-3.647631,-0.481013,4.353057,8.139435,-5.662940,-2.133714,4.708951,-5.303514,-4.795187,-9.839462,-5.843570,6.846806,-5.689175,-9.052291,1.323642,4.038490,0.547166,5.190874,6.155125,2.918932,-1.897011,-7.095506,-9.543888,4.295231,-3.107621,9.679232,-1.943056,2.995351,9.585783,4.006799,5.757898,-1.906195,-8.431695,-8.028781,-4.338216,-1.702329,0.554136,-9.787943,4.500693,-6.117289,3.586472,-5.252207,9.025752,-3.194144,8.637543,6.641551,-7.003624,3.495574,2.853611,-0.605557,-7.913439,-2.784570,6.357383,8.118919,-3.738139,-6.280469,5.203755,-1.955515,-0.158750,7.288774,-4.287411,-6.719029,-3.375357,-5.486596,0.997092,5.384464,9.732073,-0.911294,-8.525405,9.329355,9.824042,-0.838043,2.244985,8.580070,8.712552,8.561922,-0.381161,-9.938371,-3.470810,-5.015367,3.680708,2.721765,-4.680787,2.102207,2.524700,7.942221,-7.468245,-3.957913,-2.783468,5.752327,-9.024600,-8.914821,7.616570,-9.656394,4.852966,8.042854,-9.001099,3.058410,-5.981327,-5.862352,7.923624,7.228369,4.125195,0.901465,3.266424,-9.569890,-8.791353,-7.895029,6.464067,5.503727,-0.449779,-0.200140,6.366543,3.037919,-6.628243,0.669536,7.860263,-2.402322,-1.612520,4.909764,-8.863740,-7.356389,-8.937489,-3.522315,4.353264,-4.712907,4.116033,-4.009865,-2.309584,-6.333963,0.872948,-4.129408,-2.692077,-1.813715,2.294208,3.370823,9.504592,-9.551255,-1.584850,6.392432,-9.579445,6.032589,-5.426127,-7.712891,1.333504,-3.980262,-5.650018,-7.478903,0.980729,-9.021840,-9.373236,-3.002820,9.286922,3.750297,-3.593806,8.683708,-3.339714,-1.814496,-0.271353,1.128147,1.311491,0.094803,-4.822980,7.638959,-5.860158,-9.304556,8.324775,-9.805636,9.596121,-5.005211,-9.371182,-1.208199,7.256943,-9.831177,3.673641,6.338794,5.154936,8.005847,-8.862432,6.129326,-7.118739,4.030288,-3.341970,-0.268548,7.793878,2.489927,-2.943981,-3.444842,-0.301570,1.380426,-8.289570,9.683057,4.070531,-8.530646,0.391108,-3.359190,6.915311,6.503323,5.327456,-0.119145,-4.275003,9.654156,6.985612,-6.804783,-5.333587,-2.921966,2.701967,-8.976004,-7.839652,-7.167075,-0.962430,0.111408,8.493346,4.638314,-8.432247,3.022542,-0.321829,1.899455,2.197753,8.968942,3.405091,-3.205401,9.785050,-8.080253,9.526275,1.300859,2.164998,-3.835191,5.952292,-6.461156,6.248036,8.742227,-7.845714,9.287793,-1.788669,3.809184,-1.011026,-0.350676,-1.977426,8.092578,-6.477156,3.577055,0.838498,-0.010837,8.579719,-0.978881,-3.320321,-0.610102,-5.370840,-2.389214,2.370305,0.056373,-6.467393,2.210715,-1.518198,-6.796190,-8.593835,-1.937404,3.231648,-5.249276,4.505748,9.109246,-1.212197,-6.607745,-8.915031,-3.331602,-4.428213,5.610993,9.265240,2.477974,-0.525687,-3.006247,6.554702,-9.537455,9.189575,-9.494294,-5.014997,2.694926,9.186649,0.274298,-6.032733,6.198556,4.583627,5.936726,-2.417600,-9.068826,7.258892,2.064392,-3.140270,0.825594,-8.927473,-1.339857,-2.043555,-4.211889,-2.829078,1.497169,2.313197,6.220633,2.686686,5.874140,-5.319884,-9.040421,9.746976,-8.095177,-2.271059,6.133248,8.017112,3.764446,7.159426,-3.322724,0.638442,0.571034,-7.663779,-6.536587,9.620526,8.766273,3.578302,8.781466,2.338047,-6.964588,-2.132097,4.554481,-2.503190,1.306688,-2.017600,1.489903,6.726382,-8.795642,7.063000,6.158697,-2.313749,-9.372783,9.022717,-0.216884,-3.162969,-5.059345,9.163202,-5.015566,-0.066752,7.135070,3.786903,-3.470714,5.398311,7.508911,2.878920,-1.393432,0.211567,-9.042181,-5.340944,-0.192338,6.008900,1.716921,-3.495556,-8.856462,4.106008,7.931580,-8.649937,7.361672,-1.927063,6.879986,-2.530281,3.002766,-6.025387,-0.843172,8.219187,1.519315,6.265034,9.939104,2.791975,-5.214699,4.716899,4.908654,1.148112,-3.775680,5.148036,-4.291369,7.390383,-3.975871,2.985712,-7.394624,4.056636,8.518999,6.683070,-3.170349,6.948250,5.136093,-5.650256,-2.725850,-3.548319,9.723631,-5.673191,7.269144,2.723700,-1.568535,-3.111612,5.326670,-4.114540,-2.599520,2.899460,-9.474097,6.638217,-2.045540,9.097378,7.533585,8.432225,2.095229,-3.170767,5.062526,-0.154549,-9.512779,-2.877495,-5.593200,5.030881,-7.095892,5.936694,2.633818,2.123428,-0.734121,-5.070720,-2.191873,-9.293160,-5.453168,-8.647357,7.456931,4.873604,8.903544,0.793930,-9.584474,-4.028141,-2.876471,-7.029278,-2.158715,7.806045,-8.345787,-3.935806,0.871289,-4.950795,-3.625410,1.516075,-8.157643,8.206185,-6.320571,8.323458,4.420404,-0.084400,-8.013295,5.607603,-5.915915,8.766594,5.570312,8.050319,2.847301,-0.294841,-9.933633,5.302243,-9.595819,-4.641748,2.790936,1.366530,6.968199,-4.219279,-7.165543,-8.873956,-5.313155,2.409723,5.073312,-9.998681,3.697650,-2.197627,-4.309772,-1.133353,3.809288,-6.368527,-3.115214,5.158556,8.246527,5.752207,-0.283029,-2.909625,-8.549377,-1.168166,-0.784991,-0.732080,6.070443,8.828207,-8.753408,-9.574179,-8.478635,-8.390866,-1.727036,-0.834012,-6.895566,-7.480931,3.056977,4.494886,-0.684417,2.521982,5.868399,-6.608287,1.736728,-5.931582,5.598951,5.458072,5.459446,1.835329,2.530555,6.871497,6.760484,-4.674672,-5.959599,-5.814994,4.479051,0.155594,9.365299,0.845715,5.206578,-5.245930,-9.123712,-5.879843,-2.263670,-8.495246,8.997776,7.501945,3.712662,5.786845,8.253641,-0.554967,-3.355552,2.450624,-1.905590,-3.880588,4.632319,-1.370596,-3.752578,2.997588,-2.511617,-0.235073,-2.224867,1.432417,-2.151834,6.233992,-6.883650,-5.727840,-4.472131,2.950149,1.527191,-6.545783,-9.391497,-7.231480,-3.636789,3.243602,6.064678,-7.187572,3.916842,8.834721,7.653501,-9.031388,5.658698,-8.127231,-0.426965,-7.554355,6.550321,-7.665805,8.359291,-1.578507,5.398554,3.839683,8.862864,-5.866286,8.560769,-9.346161,-3.122696,-6.532739,-3.163090,5.706125,-8.237201,-4.168533,7.447548,-0.021560,1.791455,-3.169961,-9.409584,-4.847713,7.553632,7.170259,-6.619992,2.880103,-7.756095,-6.085756,-9.696934,9.322925,8.114845,-2.436896,0.753368,-3.508547,5.496995,8.782550,-5.405281,-3.706700,-9.498809,-2.026730,9.640954,8.449918,8.208721,-2.569044,-9.303619,5.323710,6.522199,-9.484593,-4.886861,-7.799614,2.869721,0.993053,7.370217,5.548306,6.611408,-4.086354,-3.718613,-3.979855,-1.168326,2.755737,0.445091,-2.452171,2.986384,0.942647,7.636161,4.130727,3.205887,-7.772681,-2.820711,-9.839147,4.499230,1.984705,-9.182897,-4.601396,-5.224115,3.601607,-0.719891,3.969605,-7.156598,9.165640,-9.408362,-5.273883,1.552254,-2.179254,2.525283,-0.618591,9.025206,-7.410255,9.144645,-3.681680,-7.489442,8.622637,-0.020771,-3.445246,0.323094,-1.416934,9.396449,4.536578,-2.760103,-7.114318,-9.892035,-0.314288,-3.314326,-8.138666,7.443078,-3.030703,-1.830207,-9.163479,-5.565492,-0.272225,-5.045504,0.977984,7.966059,3.895937,-3.412532,4.876081,-9.168614,-8.172289,-9.905420,-0.068062,-8.663886,-0.535246,8.742768,6.339132,7.698436,9.653748,-8.391359,6.981640,-0.325900,1.400790,0.091246,7.661066,9.877231,-6.501120,-2.857758,4.412891,6.329623,-2.405226,5.331320,-4.824212,7.025649,-8.514264,-0.621368,9.565016,-5.470746,1.477384,-3.236683,2.745214,3.579105,3.739631,2.176245,-9.562008,-2.992486,7.081190,-9.920448,1.840645,1.433567,1.969562,0.968303,-5.523209,-5.238832,5.251658,8.236559,-1.928647,3.345530,-9.555716,-0.346993,7.780256,9.739270,-3.543843,8.139295,9.190634,-6.487360,-5.681211,-0.298106,3.660691,9.251455,2.640985,-9.348160,7.437936,4.512423,-7.700636,-8.800274,2.661030,-7.703218,8.580814,7.574587,-8.465371,5.781164,9.041673,-7.863460,-0.621716,-7.852681,-4.850882,8.926397,-7.160253,7.196058,6.897169,-6.919615,-3.645678,-3.612337,-8.238150,-0.724988,4.739276,-6.896283,1.559472,-6.346512,-1.857080,0.016310,4.269214,-0.710108,-0.255032,-2.090125,6.571331,-1.732308,5.372215,2.613648,-9.370083,-4.148507,5.345211,-5.052988,1.743730,9.614789,7.924817,-3.702440,6.673392,-5.899564,9.626686,7.745399,-8.259928,-7.161203,6.874962,1.288857,8.307012,0.768496,-9.843968,-2.091897,-0.192963,7.004945,-5.898459,-3.033884,-4.838814,2.092388,4.277847,-2.876004,-4.211787,0.754970,-1.416970,2.766453,1.716802,0.967881,9.484677,6.805248,5.591111,5.215809,7.533091,5.607655,2.408824,3.286986,-4.828657,-2.011962,-3.090137,-0.492341,-5.380311,-2.640894,-1.624268,-8.031165,0.417333,-3.022645,-9.258763,9.878055,9.835570,-5.906485,2.389512,-7.695673,5.953980,9.117213,-1.413070,6.874649,6.301114,-6.980519,5.982439,1.563499,6.376712,4.415948,-0.679902,0.689694,9.898713,-8.257226,9.814076,-4.690059,4.748490,-9.711866,0.308291,-9.338215,5.036273,9.071303,3.723856,-3.948903,-2.600059,8.188289,-2.351123,-9.018271,-1.921212,-4.056682,0.220998,-5.229821,-5.525019,7.654247,-8.392718,2.346780,-1.779385,-3.935446,8.099337,-0.690551,-7.924990,-2.668147,-0.831452,0.838329,7.077219,-3.317919,-0.852457,1.946400,8.612308,6.576107,8.159545,-7.810630,0.002221,4.853130,9.949725,-1.536053,7.203326,-7.853251,5.401084,-1.412296,6.157880,-2.098011,-7.038905,5.116077,-8.966544,0.272360,9.504920,0.900386,3.567277,1.151510,0.546925,-7.488006,7.925363,-9.663730,-7.852238,3.534147,-2.366474,-1.305657,-9.077906,-4.438818,-1.604834,-5.016180,3.018056,-2.051512,-3.447661,1.745625,8.269739,3.918919,-3.977408,6.449770,-9.074362,2.346321,-5.247054,0.010730,0.823823,1.335524,-1.744772,2.152988,-4.166563,-6.334600,7.799177,-3.061408,3.548693,6.213803,2.178926,2.894507,-6.527296,-2.592898,-3.921037,7.855576,-7.509047,7.986668,-4.762843,-6.586155,-9.554924,3.183147,9.717371,-6.510227,0.655132,-2.375962,-8.336997,6.653832,-6.505955,-3.561622,7.161825,-7.089211,-3.935422,-1.727785,-9.714814,6.651412,5.149062,1.876058,-5.774271,-5.745597,1.882639,6.462039,-2.386024,-5.328056,-7.221050,9.996027,-8.733409,6.925604,0.618658,5.547276,1.599420,-1.027470,-6.045251,4.787120,1.241921,-2.867192,-6.706920,-4.604790,-4.320887,-0.750646,3.451286,3.347810,8.754328,4.544009,-9.612247,4.177652,3.595148,6.639448,8.147913,2.869939,-5.688569,4.214600,6.443648,7.617285,7.379792,-1.956033,0.578604,-1.077012,6.883697,9.867961,7.015869,7.152070,-1.671666,-8.840795,3.964577,-3.376410,7.445515,-3.823575,7.636336,6.556268,7.581569,-8.767034,9.047428,-0.248791,-0.395653,-3.909601,-9.325742,-9.153215,-1.514895,-9.408432,-7.561096,5.098252,-3.547451,-9.477750,9.037387,-0.567697,-2.589220,4.883447,-9.230788,-6.323766,9.959848,-4.967612,-1.911539,-7.935821,2.849870,-2.127099,8.651679,6.549758,2.032748,-1.117097,0.597693,-3.819206,9.497779,6.081405,9.062732,-6.446941,5.357459,-3.795972,7.687985,-8.329820,2.194546,2.872807,4.657327,-9.846686,-9.170082,7.433763,-8.342669,9.741551,-1.338114,1.737867,-5.267039,-6.377333,-2.816387,7.646752,-1.718317,-5.018475,-3.015130,-6.702435,-2.909114,8.095726,4.099290,8.760645,-7.494822,8.816766,7.713044,-7.009916,-2.265801,1.536116,7.982292,6.029781,7.872503,6.991443,8.165833,1.884893,-4.572808,-3.770230,1.894896,4.508925,7.941433,-8.703293,1.389323,-3.953570,-5.687621,-2.882732,8.679472,2.859901,1.621690,-2.223941,-8.650249,6.940747,-1.844650,1.641189,3.693457,4.537940,4.935556,9.261253,-7.826749,0.803387,-8.372675,-4.381298,7.177870,-1.778383,-8.817616,4.569115,-7.427242,-8.042575,-4.799496,-8.624317,-7.811688,-0.080887,-3.414725,4.366155,-1.550755,1.924766,-0.919823,-4.929496,6.552360,5.259784,4.059136,-6.507944,3.220784,2.721846,-4.505380,7.677607,8.909857,7.028205,0.027184,8.336075,1.679663,-2.020967,-0.346511,0.986762,6.042342,-8.125259,8.067276,-9.559497,9.490092,-8.763862,-3.191423,-7.277772,-0.297680,1.758550,-3.936912,4.903369,8.148533,-2.121224,-0.024869,5.315325,-4.238026,-0.255071,-8.398333,-0.661661,-7.100347,-7.477346,-0.717907,5.404281,-0.625064,-3.104539,4.732745,-2.274003,-3.168450,-2.703916,-2.586821,-9.127060,7.614472,-5.270311,-3.398285,2.890745,8.523230,2.967382,3.565480,-6.878100,6.052075,-7.947892,-9.555845,5.395573,6.103211,4.999558,8.881487,-0.991714,4.687874,-8.473158,5.222772,-9.683682,0.825838,-1.838520,-6.199400,-6.621805,-7.249075,-5.592822,9.894291,3.909652,-9.623690,-0.254663,-4.578760,-2.577784,4.131245,0.895272,1.697209,-6.608489,6.594520,2.178990,7.740865,0.919516,-0.273555,5.061658,1.934287,5.341522,9.780077,3.947954,-8.648926,4.755483,3.751813,5.690802,2.197030,3.482676,-3.549316,-5.750685,6.671032,4.280759,-3.269336,5.656099,9.860280,9.820425,8.895832,0.005344,-7.928898,8.392166,4.293887,-7.785521,-0.196546,-8.534032,-1.379892,1.158797,-0.465638,-8.721906,3.753988,2.879438,-7.637274,2.090406,7.677897,3.213250,-7.823677,4.375491,9.200770,-3.453219,-4.021199,5.129626,7.516790,-0.693098,9.645016,-9.936520,-3.772946,-2.969039,-0.580070,-1.382277,-2.249660,-7.101394,1.520038,-0.256014,3.285345,-9.422643,2.048602,1.346830,-7.437766,8.723122,-2.716331,-9.192886,8.213880,1.465726,7.137108,5.408417,6.226534,-1.711102,-1.006033,-8.701033,8.034259,2.145827,-6.141543,8.299776,-7.286999,-2.136998,0.202589,1.435562,3.586950,-1.862270,7.377661,-0.460877,7.542519,9.228077,-1.456130,-9.007176,-6.405423,-8.719074,-7.548076,-7.680192,-5.243380,7.823493,9.648088], dtype = "float64")#candidate|4574|(2016,)|const|float64
call_4573 = relay.TupleGetItem(func_4085_call(relay.reshape(const_4574.astype('float64'), [9, 16, 14])), 0)
call_4575 = relay.TupleGetItem(func_4088_call(relay.reshape(const_4574.astype('float64'), [9, 16, 14])), 0)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_4577 = relay.TupleGetItem(func_3534_call(), 1)
call_4578 = relay.TupleGetItem(func_3536_call(), 1)
uop_4579 = relay.asin(call_4546.astype('float64')) # shape=(2, 13, 5)
uop_4581 = relay.asin(call_4547.astype('float64')) # shape=(2, 13, 5)
func_3351_call = mod.get_global_var('func_3351')
func_3352_call = mutated_mod.get_global_var('func_3352')
call_4582 = func_3351_call()
call_4583 = func_3351_call()
func_1047_call = mod.get_global_var('func_1047')
func_1049_call = mutated_mod.get_global_var('func_1049')
call_4588 = func_1047_call(relay.reshape(var_4541.astype('int64'), [9, 3, 7]))
call_4589 = func_1047_call(relay.reshape(var_4541.astype('int64'), [9, 3, 7]))
output = relay.Tuple([call_4522,call_4540,var_4541,call_4573,const_4574,call_4577,uop_4579,call_4582,call_4588,])
output2 = relay.Tuple([call_4523,call_4542,var_4541,call_4575,const_4574,call_4578,uop_4581,call_4583,call_4589,])
func_4596 = relay.Function([var_4541,], output)
mod['func_4596'] = func_4596
mod = relay.transform.InferType()(mod)
mutated_mod['func_4596'] = func_4596
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4597 = relay.var("var_4597", dtype = "int64", shape = (189,))#candidate|4597|(189,)|var|int64
func_4596_call = mutated_mod.get_global_var('func_4596')
call_4598 = func_4596_call(var_4597)
output = call_4598
func_4599 = relay.Function([var_4597], output)
mutated_mod['func_4599'] = func_4599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3862_call = mod.get_global_var('func_3862')
func_3863_call = mutated_mod.get_global_var('func_3863')
call_4625 = func_3862_call()
call_4626 = func_3862_call()
output = relay.Tuple([call_4625,])
output2 = relay.Tuple([call_4626,])
func_4635 = relay.Function([], output)
mod['func_4635'] = func_4635
mod = relay.transform.InferType()(mod)
mutated_mod['func_4635'] = func_4635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4635_call = mutated_mod.get_global_var('func_4635')
call_4636 = func_4635_call()
output = call_4636
func_4637 = relay.Function([], output)
mutated_mod['func_4637'] = func_4637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mod.get_global_var('func_3833')
func_3835_call = mutated_mod.get_global_var('func_3835')
call_4764 = relay.TupleGetItem(func_3833_call(), 4)
call_4765 = relay.TupleGetItem(func_3835_call(), 4)
func_2535_call = mod.get_global_var('func_2535')
func_2540_call = mutated_mod.get_global_var('func_2540')
const_4767 = relay.const([6.570985,-1.812003,-5.446691,-6.189741,8.949150,8.651940,-4.847033,2.316479,-9.662509,1.396037,6.888433,8.391471,-2.375199,-4.231338,2.502993,-1.929931,8.940434,-5.247303,-7.411413,4.300744,-7.006407,9.243471,-3.683553,-0.373672,3.368547,-1.327089,-2.134008,-1.263232,-3.084850,-7.107919,-3.974597,-5.482193,6.826102,7.408032,-0.570306,-9.096861,2.128930,8.882621,-6.062687,-5.279617,0.889636,3.874414,9.401525,-6.534115,-3.884268,2.578681,3.736046,0.976725,-4.375814,-3.563001,9.151592,9.276361,4.503025,-6.811126,-7.406664,2.144952,-0.426039,-9.773921,7.669412,8.183286,9.390394,-9.743692,-2.097519,-9.994757,7.548229,1.906480,8.760010,2.972281,-6.876174,-2.325849,9.353472,-4.111923,-9.394373,7.511689,-1.634886,-5.110719,0.573280,-4.570424,-2.748096,-8.208069,-6.530796,-3.532980,-6.919392,-2.444298,2.975697,-5.262681,-8.532437,-4.397597,5.795935,-6.477134,-0.690700,3.455003,-5.678507,-3.248846,-6.053030,-2.553317,-6.533804,-8.100261,-7.400370,0.820829,-0.295414,-0.102829,1.859332,0.198436,-0.961762,-6.053372,-3.356292,-9.377610,4.344655,2.411322,8.792666,-5.908109,-7.729797,9.548076,6.135224,9.620495,-8.270209,5.811298,-8.569229,-1.901221,-7.004105,-1.791310,-5.644352,0.951115,5.081367,-0.030503,-8.052432,-8.675659,1.371357,-5.834300,0.176266,-6.408217,3.112931,2.196730,8.823895,1.320756,-8.051697,-0.307147,-9.965672,-4.196911,0.519912,8.099082,-2.330661,-0.634857,6.515196,-1.585637,-5.702162,-3.262251,-8.124496,-0.913858,8.528645,-7.088668,2.563905,-0.253802,-3.744996,1.302811,0.203547,-3.664619,-9.243964,-2.473439,6.589912,-0.248627,4.779782,7.064299,-1.271227,4.776317,7.280011,2.540266,6.495027,8.366911,8.677082,3.164458,7.978924,-8.300807,-5.554534,5.063180,9.952503,-1.575291,-6.291975,7.109035,7.133772,-3.393444,-9.556995,0.792146,7.068256,0.616487,7.662282,-2.937777,-4.877506,-7.831047,3.263046,-2.152731,-4.784264,2.499837,1.970482,7.812232,-0.360234,8.236136,-0.802795,-2.874689,3.540147,-2.406431,-4.181365,8.305300,2.315214,6.121391,3.398779,9.240031,-6.408185,-4.515362,0.961827,-8.075212,2.640308,-4.286530,-2.002967,-6.899601,0.070134,-8.863416,1.642196,-3.127326,-8.253040,7.812665,-4.960113,2.993180,4.279848,-4.042146,9.650296,-4.077203,-2.958440,-5.299768,4.272242,8.448568,0.934962,-6.397718,7.836159,9.935072,2.771161,-2.256604,-0.845078,-9.071835,9.711057,-4.965348,-3.433965,-2.375760,-6.002207,8.098065,4.483430,-9.867487,6.755743,8.979541,5.170275,-6.532183,8.833462,-5.589071,-1.653842,6.971912,9.362956,-1.440083,4.890610,1.318136,-4.616082,1.009555,2.396357,-8.373566,4.780374,5.278617,1.077470,9.417226,-3.571011,-1.896422,-4.938237,1.734484,3.385417,0.799089,-9.707511,-9.542177,-4.742636,-2.229133,1.718813,-4.501755,-8.470971,-9.839936,4.399498,-9.567829,7.154307,-0.406348,-6.146258,-7.400790,5.197630,-3.876253,-2.803136,-0.365743,1.589428,-9.279225,-5.923609,4.017097,-5.855340,-2.465761,0.952025,-7.865928,8.010739,-5.210045,-5.897289,2.495279,3.528425,8.269122,0.650577,-0.029889,-6.828015,4.605445,6.082327,8.526229,-8.100457,7.932583,-4.286520,6.743603,-3.119678,9.379354,-6.258230,-0.066937,4.829665,8.444622,-7.859672,0.992749,-6.297281,4.121669,1.544565,2.092472,-5.233827,0.754739,-4.085122,-2.232299,-5.380633,2.117723,-0.590290,-3.531080,1.934843,-4.447740,1.427856,-4.840847,2.374027,4.697343,-7.506319,-7.139946,2.693004,9.490745,-2.950952,-0.345532,-4.081489,7.822871,-5.266254,-4.277912,2.233037,3.695245,-6.921260,-7.682490,2.114853,-7.764899,8.215808,-3.000660,-2.672763,-5.409902,9.391104,6.713472,9.701228,-2.012162,5.117921,4.095432,-8.641484,8.651197,5.550171,-7.088291,-6.713211,-8.313741,9.283693,-8.199881,8.782735,0.900007,-4.108725,-0.207415,2.773694,3.109342,5.294732,-1.852123,0.415144,-9.595881,6.697126,0.663733,2.177962,4.693091,-9.130232,-9.466568,4.067845,-9.324527,-7.882602,4.938927,3.797762,-3.851794,6.601649,-2.847758,2.392682,8.022637,3.927521,-8.698765,6.967600,-3.555897,9.207664,5.865174,-2.840196,-3.935777,-4.858929,-9.225167,-0.847098,-0.617122,0.886383,-7.173998,2.922852,-5.710960,-3.478113,8.252577,-6.431047,4.945674,-9.322603,-5.819432,-4.776160,9.356813,-7.977564,0.471703,5.245161,4.730575,-0.560849,9.053394,1.039796,3.858513,-8.013848,2.440568,-3.334161,-9.011835,1.074744,0.728426,-1.895698,-8.546952,-0.341683,2.120899,0.503071,9.389336,7.972310,8.018596,-3.369182,-5.709377,6.751972,9.602832,6.104039,-8.295156,6.587519,-6.200882,5.626940,-6.380161,-6.870695,7.607915,-3.640510,-4.233974,1.624655,9.562088,-2.951606,-7.172611,2.084047,9.262221,0.830281,-4.220081,5.641154,-8.335026,7.061360,-9.112000,2.698130,-9.595190,-1.335686,4.803181,-8.784876,7.196845,-1.238730,5.182943,-4.801192,-3.432299,-8.900843,-9.135901,-6.019883,-5.714273,8.787124,0.462946,-1.113424,5.021546,-9.768781,-7.018178,7.907059,6.474532,2.654852,6.362173,2.530474,-4.387510,-3.992972,8.824367,0.175279,9.173942,6.517088,7.220996,-8.640734,-5.842812,0.739478,6.566033,5.874026,2.546346,8.399462,-1.262051,-3.958293,1.919423,3.460487,1.956156,-1.585731,4.003433], dtype = "float64")#candidate|4767|(520,)|const|float64
var_4768 = relay.var("var_4768", dtype = "uint8", shape = ())#candidate|4768|()|var|uint8
const_4769 = relay.const([9,-8,-8,1,3,1,-2,-4,-5,4,-5,9,8,4,-8,-4,7,-7,10,-4,10,8,-10,-4,-3,-5,1,-6,5,-9,-9,2,-6,10,7,-9,-1,2,9,-6,-4,-1,-5,4,-1,5,-7,-3,-3,8,-6,10,6,-9,-8,9,6,-9,-9,10,-7,7,1,-6,2,6,-3,-7,6,5,-9,-8,-6,-5,-1,4,-2,-1,-2,7,2,-6,-8,7,-7,2,9,-2,-6,-10,3,-4,-7,-8,-1,-7,-8,2,-3,4,3,7,-3,-7,-5,-5,-2,-3,-3,10,-8,10,9,4,3,4,-1,8,-2,-6,-1,-5,-9,4,1,-7,-10,-7,-9,2,8,-7,-9,-6,7,5,-2,-3,-1,4,-2,5,7,2,2,9,-2,-8,9,-9,5,-8,-6,-7,-9,-1,1,4,7,-6,-2,6,1,-2,-9,1,-4,-10,-2,-7,5,4,5,5,-8,8,6,-5,-1,1,9,-3,-1,-3,-9,5,-2,1,-1,-7,7,-10,-1,-2,-1,2,5,2,8,10,-8,3,-8,-5,-1,7,-10,-1,-1,5,3,9,-3,-3,-6,10,10,4,-8,-6,-5,-4,-1,8,-5,-1,2,-8,2,-8,4,4,1,-1], dtype = "uint16")#candidate|4769|(234,)|const|uint16
call_4766 = relay.TupleGetItem(func_2535_call(relay.reshape(const_4767.astype('float64'), [8, 13, 5]), relay.reshape(var_4768.astype('uint8'), []), relay.reshape(call_4764.astype('uint8'), [81, 15]), relay.reshape(const_4769.astype('uint16'), [234,]), ), 3)
call_4770 = relay.TupleGetItem(func_2540_call(relay.reshape(const_4767.astype('float64'), [8, 13, 5]), relay.reshape(var_4768.astype('uint8'), []), relay.reshape(call_4764.astype('uint8'), [81, 15]), relay.reshape(const_4769.astype('uint16'), [234,]), ), 3)
output = relay.Tuple([call_4764,call_4766,const_4767,var_4768,const_4769,])
output2 = relay.Tuple([call_4765,call_4770,const_4767,var_4768,const_4769,])
func_4771 = relay.Function([var_4768,], output)
mod['func_4771'] = func_4771
mod = relay.transform.InferType()(mod)
var_4772 = relay.var("var_4772", dtype = "uint8", shape = ())#candidate|4772|()|var|uint8
output = func_4771(var_4772)
func_4773 = relay.Function([var_4772], output)
mutated_mod['func_4773'] = func_4773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4517_call = mod.get_global_var('func_4517')
func_4518_call = mutated_mod.get_global_var('func_4518')
call_4792 = relay.TupleGetItem(func_4517_call(), 0)
call_4793 = relay.TupleGetItem(func_4518_call(), 0)
func_3947_call = mod.get_global_var('func_3947')
func_3949_call = mutated_mod.get_global_var('func_3949')
call_4815 = func_3947_call()
call_4816 = func_3947_call()
output = relay.Tuple([call_4792,call_4815,])
output2 = relay.Tuple([call_4793,call_4816,])
func_4825 = relay.Function([], output)
mod['func_4825'] = func_4825
mod = relay.transform.InferType()(mod)
output = func_4825()
func_4826 = relay.Function([], output)
mutated_mod['func_4826'] = func_4826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4378_call = mod.get_global_var('func_4378')
func_4379_call = mutated_mod.get_global_var('func_4379')
call_4855 = relay.TupleGetItem(func_4378_call(), 0)
call_4856 = relay.TupleGetItem(func_4379_call(), 0)
const_4857 = relay.const([[[-7.375866,-3.921551,-4.817520,-5.973105,-9.901192],[7.338659,8.523620,2.012918,0.950219,6.921166],[7.149310,1.514913,1.315279,-5.312797,-5.606431],[1.993068,6.653794,-8.490751,1.187065,-1.126367],[2.280840,9.133124,-7.964781,6.269764,8.421337],[3.249614,9.196919,6.648965,-7.155515,-3.585177],[1.148973,8.420075,8.215248,-5.563790,-7.519775],[7.843159,-7.294758,-4.159768,4.492932,2.374732],[-0.584282,2.008431,6.240754,4.624539,-5.229459],[-6.259211,5.490415,7.974200,7.878120,4.474578],[-1.077395,4.578801,-5.145961,9.989098,-4.298697],[-0.004729,7.859684,-5.838992,-5.966152,-6.483259],[1.768745,3.582654,-2.018842,-6.328473,-8.224242]],[[0.647906,-4.794278,-5.976460,-6.079376,-9.273163],[-5.811926,-7.710824,3.544124,-9.849005,-3.919719],[-3.563995,-7.663704,-5.522644,-0.772220,-3.969125],[4.735027,3.424456,0.079368,-1.838471,3.322491],[-2.378614,9.309129,-4.991507,2.390173,-9.080224],[7.208890,9.796894,-8.133143,2.426014,-1.667902],[-3.210281,0.288606,8.090288,9.616689,4.589503],[1.646234,-7.985068,-4.687846,9.523004,5.143341],[2.915601,-0.571631,-9.928417,-9.537566,-2.494862],[-4.741387,-1.479204,-1.815000,-4.659831,4.542157],[1.799901,9.928973,7.911729,-1.338393,1.655133],[0.589503,-8.862296,1.442585,-2.078651,-2.007208],[1.193366,5.394465,7.030252,7.502197,1.073009]]], dtype = "float32")#candidate|4857|(2, 13, 5)|const|float32
bop_4858 = relay.right_shift(call_4855.astype('uint64'), relay.reshape(const_4857.astype('uint64'), relay.shape_of(call_4855))) # shape=(2, 13, 5)
bop_4861 = relay.right_shift(call_4856.astype('uint64'), relay.reshape(const_4857.astype('uint64'), relay.shape_of(call_4856))) # shape=(2, 13, 5)
func_4068_call = mod.get_global_var('func_4068')
func_4070_call = mutated_mod.get_global_var('func_4070')
const_4863 = relay.const([-5.949538,5.377973,-2.675515,3.408983,-7.944233,9.595545,3.783357,0.290100,-4.583266,4.493745,9.052486,-9.293661,-6.073339,-3.991189,-4.405617,-2.520149,-9.155000,1.113035,5.017325,3.441658,7.775179,-8.733232,9.854095,6.688313,-2.875202,3.567735,-7.028169,-6.934997,-1.394351,-4.194572,-4.482571,9.296202,-9.562978,3.995666,-7.702770,3.044432,-6.455282,-5.345115,-3.433347,8.272538,-2.858423,-8.418338,7.410492,5.809426,-4.405944,-3.857399,-0.832600,0.934792,-9.993345,0.935307,6.695397,-2.032084,-4.857420,-8.892383,3.310937,6.345499,-3.415809,-3.889757,-5.560192,-6.047562,5.800344,0.866898,-4.933521,5.001203,-2.323453,9.721474,3.103714,7.708832,-1.385898,-0.038667,4.107598,-5.877178,-9.077340,2.416831,-5.067580,2.511136,9.171840,-4.430303,5.597090,-2.653430,-8.583093,9.606923,-0.055844,1.917519,-0.226356,-0.313230,1.816368,-6.766092,4.964583,6.845546,1.241872,3.135508,5.257231,-8.100552,7.240384,-5.347649,0.046246,-9.038576,-6.932335,-1.937898,3.457592,4.768327,8.891842,-0.308870,6.854616,0.202206,-9.430338,9.383697,-8.194492,-8.065315,4.748587,9.087553,4.223209,-8.634585,7.858431,-7.035024,3.047611,0.136509,8.225317,0.734148,6.491125,1.497651,0.842735,-1.606761,8.539050,-2.333816,9.486147,1.599682,1.173677,8.946284,-8.185939,3.420795,6.401081,5.662181,1.529382,4.722993,6.395115,-5.630277,-3.721920,-0.325011,-5.501966,-2.881432,-7.755136,-2.108929,1.125609,-3.111868,5.969966,9.471535,-7.931330,-2.709925,3.650301,0.740905,-3.973910,7.982919,-1.282821,-0.023782,-1.505951,-1.367302,-7.054564,-5.751445,-3.336295,-8.591450,5.098098,-8.938191,-8.014296,0.998225,2.787603,-8.192356,-9.756052,-9.711447,3.514488,0.596352,8.364531,-5.518919,-2.777176,1.518933,5.472378,6.675686,6.010831,-8.754735,-7.839224,3.297003,-9.881424,5.887693,0.678407,9.614016,3.464670,5.003490,0.007465,-7.614858,-4.403332,-3.655503,2.310094,-7.689820,-5.177911,-8.864838,-2.434215,-2.944927,9.719261,-3.229206,7.431883,2.762548,-0.049817,3.656678,-2.945045,-8.270262,7.220963,-6.301925,-8.480878,9.060611,-1.880364,0.889866,5.930476,1.138992,3.317546,3.010302,-1.509415,6.158078,7.758472,-8.509275,4.924825,5.026674,5.119845,8.583305,-2.031133,-7.991972,2.307036,-9.531573,6.469252,7.386941,2.209543,3.333193,-3.350188,-0.410072,0.641942,1.403364,9.485665,8.858490,9.819875,-7.911180,2.835857,-5.106025,-8.108880,1.920114,-9.367139,4.510933,-8.521090,1.322550,3.908436,-5.933419,-6.188183,5.125485,-2.350600,3.278574,-5.463444,-0.094466,-3.110136,-8.113473,5.928092,5.279077,-8.222546,1.459614,1.882717,2.629385,-2.382747,-4.831317,-2.147022,1.935343,-3.559478,-1.262208,-1.566586,8.349368,9.774711,-2.661848,0.679286,-1.848214,-8.402248,-3.206309,4.030258,-1.985607,-4.494558,-3.337747,1.062374,3.004811,-0.697525,-0.266099,-5.168249,-4.087652,1.585494,-2.006469,-1.379557,-4.906069,-7.970879,-9.568155,0.901566,-9.616869,3.040716,-2.741866,-0.296334,5.842717,3.118011,0.197546,0.783235,8.473058,-9.630595,4.862955,-8.310287,2.078956,6.019510,-4.725097,1.017095,-1.642909,-1.010802,4.022538,-3.464009,8.438723,-2.492568,-6.102241,-9.287771,-0.116946,5.850624,0.748623,2.581524,3.062091,5.175271,5.008908,-5.870771,6.165455,-2.952958,0.764930,2.311778,-1.138039,1.261524,6.322472,-8.253711,1.916438,-5.524513,-9.694394,6.684057,-3.992955,4.648920,0.550547,4.008679,-1.346114,1.693697,-2.079253,6.163292,-4.919740,4.416775,-0.389096,8.445702,-1.520727,1.914296,-7.622595,-7.733752,4.048484,-2.144098,8.391583,0.030140,-4.999887,3.667412,-0.205436,4.048448,4.012338,-0.487235,9.833489,5.602112,8.328027,-1.984424,-2.412144,-7.719855,-2.711052,-0.439452,-6.149451,-2.109913,3.725055,-2.043883,-3.823065,-7.240142,-5.220906,6.852755,8.371258,9.137111,4.161282,-8.684794,-6.342079,5.334142,7.742498,-1.664649,-5.471005,-1.190109,-7.964051,2.597681,2.841236,1.007998,-9.687241,1.999805,0.550364,7.951323,-0.763198,-9.656813,-3.215090,5.961429,-1.378397,-0.128716,-5.285639,-7.272885,1.569602,5.833459,8.977264,-4.496740,-1.155422,4.772576,1.257892,-6.147963,-3.874527,-3.279018,1.885473,4.697028,-0.410317,-9.020943,-3.479640,0.259622,-3.607719,-1.081369,2.171146,4.051990,-4.291780,-4.890394,2.775497,5.806238,5.328930,8.826266,-3.606836,-7.034848,-0.486827,7.772034,1.538954,-9.141517,-0.514165,-0.578801,2.512044,8.966537,-7.230139,9.894655,-8.850058,-3.979829,8.357126,-5.500427,-1.633055,-6.631147,4.409215,6.413665,-3.034853,-2.418932,8.645985,5.870526,0.870117,-8.440614,-8.020889,3.262102,9.190337,-7.492197,0.318472,-2.418997,-4.688597,-0.684094,-0.829384,-9.608375,8.716411,0.418067,4.073116,-4.039024,1.783702,8.083857,-5.443119,2.468071,-7.796293,-4.719886,-6.044124,3.713548,1.307180,2.767102,5.278622,7.557142,-6.323283,9.702214,6.553047,-2.537896,8.085032,-3.717055,2.178663,8.556988,2.327330,3.653880,-2.715258,-4.572020,7.552370,2.233358,-4.050916,9.738820,-8.489631,-8.016088,-5.056759,-0.044540,-6.906340,-5.964122,-0.687061,6.305934,9.433433,-3.520588,5.348092,-5.369386,-7.953137,-5.359289,-4.406175,7.445221,-9.789726,-8.933146,2.555303,-0.240315,2.745210,0.268530,-6.154789,0.887576,1.559396,2.396398,5.016804,1.504541,-0.030215,-6.197273,-0.175258,3.144119,1.204857,2.047917,-4.176525,7.307925,-5.846158,-1.487968,6.111588,5.758070,0.479218,-6.646658,-4.894659,-2.430982,8.349689,5.276502,-4.606572,-9.697449,-5.547277,-2.391677,-1.498075,-5.806783,-3.386598,8.781563,-0.021251,1.006280,-2.996067,-3.167559,9.980666,2.733074,3.765474,-9.524641,5.012795,-5.376296,3.469272,-6.592612,-8.633632,-0.345802,1.863942,-1.703915,-7.875211,7.482904,4.665237,9.489378,-6.289586,0.815153,9.408816,-4.622287,2.602647,-6.060325,2.834621,-9.451319,5.265450,6.970095,-1.870793,9.971704,5.169762,6.395128,-1.516165,6.514804,7.963711,3.263740,6.603002,5.244341,-8.105207,7.175806,0.089907,2.191599,-3.683537,4.346814,-0.287777,-2.926459,-4.247685,1.406455,-6.649461,6.051177,0.037037,2.912537,-6.153977,7.594609,-9.093059,3.801844,-4.667774,6.132824,3.670052,-8.053369,2.803047,7.491385,-2.940485,-0.459647,1.062980,6.708888,-6.712188,2.781860,0.668023,6.122298,6.045180,2.966079,4.887204,6.607586,-7.204818,8.990662,-7.960306,2.841743,4.074951,5.363871,4.728678,5.139946,2.109269,2.816659,-8.128417,5.378128,4.819034,8.377268,5.871527,4.322707,-0.693785,2.261680,2.924201,-9.792189,-7.535031,6.407075,-7.129042,-0.373407,-5.138491,-9.014783,-2.621151,-5.855333,7.129755,5.175147,-0.412300,-4.705659,3.868899,5.458002,-8.401920,9.500835,-7.172379,-7.717183,5.387467,-8.421111,-5.285115,-5.507885,-7.738106,-3.924401,1.820462,-3.529471,-4.331756,-1.374883,-1.024759,-7.051107,6.060431,-0.479790,3.478328,-6.031475,9.405384,-2.938746,-6.270560,-5.748867,7.367313,-6.041950,-5.590670,8.683772,6.641646,-6.975529,3.834421,-4.713045,-0.442325,-2.568611,4.685489,8.570773,-7.135661,8.440154,-8.327878,4.872140,-3.581085,-6.587289,8.244527,-4.180518,-3.867785,-6.269987,2.348641,-2.100746,9.905670,5.574943,-7.549324,3.908618,-9.081268,6.687567,1.899839,6.708249,-0.017232,-3.783670,7.139853,-0.888448,-7.087035,2.099916,3.770415,2.996611,6.256028,4.790623,0.084359,-9.177554,9.357765,3.355135,-1.776287,6.763858,-2.606400,-8.668914,-4.008218,9.980001,-6.788613,-5.890998,9.406212,-4.867466,9.350897,-5.189848,7.512607,-6.257941,-5.038301,9.695323,-8.683545,2.427160,-9.142323,-5.106544,-0.525097,5.287236,3.980319,-9.098451,-2.848996,3.683329,-1.292552,-4.244239,-1.554550,5.984434,-5.229613,8.307280,8.357088,-9.187689,5.943060,-6.072349,-1.812415,-0.729942,4.208655,-2.206804,6.568248,0.130021,4.132561,8.738646,3.912409,-1.991294,9.234919,-9.274105,-9.571103,4.344640,-7.915625,1.276379,0.177630,-3.187316,-7.946425,-3.421415,-2.964872,-1.483500,-6.289852,8.712650,-2.455120,8.669643,9.230597,-2.223745,-3.900005,1.023398,6.978693,-2.604029,-5.080785,5.420242,3.169171,2.955162,-2.088386,-2.758551,4.578551,-2.099069,9.590222,-3.750950,4.631441,2.920041,-0.308876,-6.302462,5.813780,-9.295708,2.757337,3.555844,-7.229992,-1.265922,-2.975208,0.192261,-8.040219,9.027864,2.097505,5.179964,-7.582342,4.911885,2.886391,-9.201543,-1.041150,9.331588,-0.804600,-7.836587,6.313524,2.761072,2.106415,0.136156,-3.042383,-2.939302,-1.787303,2.737687,-2.322872,2.111655,-5.139516,-7.243329,3.378198,7.569774,-0.177883,-2.275773,-5.027013,2.327835,-2.574941,-1.778834,5.447942,-3.212285,-2.591393,-4.584821,-6.509639,-4.949686,3.927293,7.636404,-2.583014,4.156037,5.032992,-5.286683,0.353719,5.797978,1.517393,8.846771,-2.687286,-5.281252,2.560351,3.095085,9.655937,-3.741452,1.585126,5.187035,-0.647205,-5.773099,-1.081238,-0.525284,1.548646,5.117500,9.531980,9.338012,-0.098886,-5.880598,7.883121,-2.151063,6.740533,2.632491,-3.532598,9.371255,1.492089,-7.556900,-0.866933,-8.838735,7.904821,-1.880691,-5.506983,-4.035676,-0.748741,-5.093002,9.394122,-0.524550,4.893212,7.383776,-3.551428,0.863148,-1.834254,6.988421,-8.175108,-9.100625,2.641839,-4.086581,3.160481,-4.610072,6.653869,2.110213,7.108699,6.956848,9.008447,4.054044,4.263560,-5.724232,-7.938271,0.272328,8.755891,-0.487075,-2.550671,-7.143929,-8.640039,7.194953,3.675786,-9.765653,-5.793899,0.244815,-3.143941,8.330521,3.619040,8.548765,6.350419,-8.158350,0.235679,3.351578,8.225574,7.946525,2.527114,0.271840,3.499116,6.779657,-8.918222,7.845388,3.720730,-6.766614,-5.556244,1.394655,-7.527245,-3.684031,-9.786844,-3.810917,3.031071,2.256106,-6.488544,9.774310,-2.504341,-5.114342,-1.298451,6.553104,-7.996422,-4.227650,-5.296885,8.676107,-8.033184,-5.734103,4.507705,-7.968892,-2.133411,6.381622,8.105543,-7.009647,-9.548736,-0.374845,-2.141992,-8.527321,3.023667,-2.091905,-3.524143,3.469374,5.061109,-6.404169,-2.487946,-3.564900,-2.831739,9.400573,-3.507031,-0.150483,-7.397129,2.653924,-7.555095,-3.606789,1.028803,4.739951,-5.138070,-7.463137,-9.175026,-3.827574,3.050226,1.425347,5.063572,8.126230,-2.520097,-5.242504,-7.577174,-4.122819,8.148236,0.121252,8.079463,1.879332,3.176493,3.710084,-2.636943,-7.322583,-6.158476,8.476555,-1.393872,-4.144206,-8.449076,-8.074169,-4.718250,-3.048024,2.806099,-2.241545,-7.647516,-1.731138,7.444876,-3.667104,4.516394,-2.426991,-9.992964,5.147282,-7.654131,-3.634954,-6.019535,-9.832487,3.588689,7.853246,-2.005786,3.207187,4.338689,-5.396919,0.449199,-7.941368,3.141283,9.393916,-0.288231,-8.943415,-4.762917,-2.537151,9.419493,3.713238,0.254900,0.607813,1.915801,-2.575680,-1.437598,6.094951,7.015662,2.894647,-8.501255,1.049896,3.498286,-3.380192,-0.241640,5.942422,4.674878,-3.602895,1.053135,-6.501647,-5.201950,1.897818,9.483756,-0.656105,-1.402946,5.943802,-3.320811,2.406201,-3.961457,3.015609,-6.680873,8.452157,-9.286648,-4.896542,2.810625,-1.211243,-0.461227,8.413694,-8.526403,-2.929147,0.243086,-1.446696,-4.955240,6.679751,9.305340,6.909174,4.452154,0.584633,-1.136452,5.548745,-5.070248,7.940388,2.914379,-2.398709,7.420638,-9.797339,-4.616627,-9.727062,5.825600,2.263903,0.988065,-2.833373,2.808690,-6.769212,-5.189435,-1.493337,1.417572,6.924064,-6.120003,-3.439015,-5.940256,-7.497066,5.926988,-0.068093,-1.108614,4.370151,-8.601866,7.412631,6.240690,-4.477008,7.272827,-2.352484,-4.895831,-1.952794,6.414882,-9.341419,2.272145,-9.958405,-3.159908,3.669782,4.941909,-1.085917], dtype = "float64")#candidate|4863|(1155,)|const|float64
call_4862 = relay.TupleGetItem(func_4068_call(relay.reshape(const_4863.astype('float64'), [7, 11, 15])), 3)
call_4864 = relay.TupleGetItem(func_4070_call(relay.reshape(const_4863.astype('float64'), [7, 11, 15])), 3)
func_4068_call = mod.get_global_var('func_4068')
func_4070_call = mutated_mod.get_global_var('func_4070')
call_4878 = relay.TupleGetItem(func_4068_call(relay.reshape(const_4863.astype('float64'), [7, 11, 15])), 1)
call_4879 = relay.TupleGetItem(func_4070_call(relay.reshape(const_4863.astype('float64'), [7, 11, 15])), 1)
func_904_call = mod.get_global_var('func_904')
func_907_call = mutated_mod.get_global_var('func_907')
call_4881 = relay.TupleGetItem(func_904_call(relay.reshape(call_4878.astype('float64'), [2, 7, 13])), 0)
call_4882 = relay.TupleGetItem(func_907_call(relay.reshape(call_4878.astype('float64'), [2, 7, 13])), 0)
uop_4887 = relay.cosh(call_4862.astype('float32')) # shape=(1, 234)
uop_4889 = relay.cosh(call_4864.astype('float32')) # shape=(1, 234)
var_4891 = relay.var("var_4891", dtype = "float32", shape = (1, 234))#candidate|4891|(1, 234)|var|float32
bop_4892 = relay.bitwise_and(uop_4887.astype('int8'), relay.reshape(var_4891.astype('int8'), relay.shape_of(uop_4887))) # shape=(1, 234)
bop_4895 = relay.bitwise_and(uop_4889.astype('int8'), relay.reshape(var_4891.astype('int8'), relay.shape_of(uop_4889))) # shape=(1, 234)
output = relay.Tuple([bop_4858,const_4863,call_4878,call_4881,bop_4892,])
output2 = relay.Tuple([bop_4861,const_4863,call_4879,call_4882,bop_4895,])
func_4902 = relay.Function([var_4891,], output)
mod['func_4902'] = func_4902
mod = relay.transform.InferType()(mod)
var_4903 = relay.var("var_4903", dtype = "float32", shape = (1, 234))#candidate|4903|(1, 234)|var|float32
output = func_4902(var_4903)
func_4904 = relay.Function([var_4903], output)
mutated_mod['func_4904'] = func_4904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_4916 = relay.TupleGetItem(func_3534_call(), 1)
call_4917 = relay.TupleGetItem(func_3536_call(), 1)
func_4159_call = mod.get_global_var('func_4159')
func_4161_call = mutated_mod.get_global_var('func_4161')
call_4932 = func_4159_call()
call_4933 = func_4159_call()
var_4934 = relay.var("var_4934", dtype = "float32", shape = (2, 13, 5))#candidate|4934|(2, 13, 5)|var|float32
bop_4935 = relay.not_equal(call_4932.astype('bool'), relay.reshape(var_4934.astype('bool'), relay.shape_of(call_4932))) # shape=(2, 13, 5)
bop_4938 = relay.not_equal(call_4933.astype('bool'), relay.reshape(var_4934.astype('bool'), relay.shape_of(call_4933))) # shape=(2, 13, 5)
func_4085_call = mod.get_global_var('func_4085')
func_4088_call = mutated_mod.get_global_var('func_4088')
var_4940 = relay.var("var_4940", dtype = "float64", shape = (2016, 1))#candidate|4940|(2016, 1)|var|float64
call_4939 = relay.TupleGetItem(func_4085_call(relay.reshape(var_4940.astype('float64'), [9, 16, 14])), 0)
call_4941 = relay.TupleGetItem(func_4088_call(relay.reshape(var_4940.astype('float64'), [9, 16, 14])), 0)
output = relay.Tuple([call_4916,bop_4935,call_4939,var_4940,])
output2 = relay.Tuple([call_4917,bop_4938,call_4941,var_4940,])
func_4953 = relay.Function([var_4934,var_4940,], output)
mod['func_4953'] = func_4953
mod = relay.transform.InferType()(mod)
var_4954 = relay.var("var_4954", dtype = "float32", shape = (2, 13, 5))#candidate|4954|(2, 13, 5)|var|float32
var_4955 = relay.var("var_4955", dtype = "float64", shape = (2016, 1))#candidate|4955|(2016, 1)|var|float64
output = func_4953(var_4954,var_4955,)
func_4956 = relay.Function([var_4954,var_4955,], output)
mutated_mod['func_4956'] = func_4956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_4971 = relay.TupleGetItem(func_3534_call(), 1)
call_4972 = relay.TupleGetItem(func_3536_call(), 1)
func_4902_call = mod.get_global_var('func_4902')
func_4904_call = mutated_mod.get_global_var('func_4904')
var_4975 = relay.var("var_4975", dtype = "float32", shape = (234,))#candidate|4975|(234,)|var|float32
call_4974 = relay.TupleGetItem(func_4902_call(relay.reshape(var_4975.astype('float32'), [1, 234])), 4)
call_4976 = relay.TupleGetItem(func_4904_call(relay.reshape(var_4975.astype('float32'), [1, 234])), 4)
func_4276_call = mod.get_global_var('func_4276')
func_4279_call = mutated_mod.get_global_var('func_4279')
var_4978 = relay.var("var_4978", dtype = "float64", shape = (88,))#candidate|4978|(88,)|var|float64
const_4979 = relay.const([-0.143191,0.015618,5.435586,2.971943,-6.325831,0.901180,-1.188801,3.319920,-9.179315,-0.460860,0.838847,-8.731441,-4.936505,5.125946,-5.105293,-1.922872,-5.632316,1.954344,-9.911213,-4.344292,-1.864217,-1.489212,9.787246,4.687518,9.791134,-1.229119,-0.081620,-9.466737,-5.158050,-4.771095,-9.479687,4.701207,-2.552624,6.805293,0.195152,-3.962430,3.419568,-3.218762,-8.404442,-1.252696,-4.787470,-1.248084,-2.818288,7.453804,-6.981862,1.119436,-8.630534,2.140988,6.290562,-4.739379,-5.928868,-3.074904,0.065963,-5.352397,2.946137,-9.658395,-5.248102,-6.067146,0.748167,6.169458,0.005612,8.917946,-7.085916,-4.429599,8.179687,-3.185449,4.968962,0.680577,-7.501920,-2.013523,9.397084,8.364754,-1.782014,-9.371346,6.165142,6.059088,-1.745165,-1.576812,-0.028190,-9.944072,3.781800,0.650481,-7.842023,-3.000692,8.547617,-2.087386,6.603046,-0.292228,5.868555,5.537250,-9.224121,8.042538,8.903080,9.799495,-7.986527,6.091849,6.820318,9.537249,-2.266012,-6.129975,-7.941986,-6.707049,-2.161775,9.903786,7.898804,-0.924744,-8.042918,-5.395596,4.492517,3.379208,3.638261,-8.602093,5.182933,-7.758139,3.680191,8.504283,5.524440,6.462150,-3.674725,7.250313,6.838691,-2.499618,0.147801,-0.404807,-6.015332,7.321557,-6.592853,-4.603076,8.983721,3.596016,7.053793,-5.562302,-8.808415,-8.855003,3.257250,-8.312543,2.350530,-2.847479,5.166893,-3.442747,-3.366131,-0.542874,3.333638,-5.334987,8.839248,7.998404,5.239577,-3.093893,2.188465,-9.991986,-0.036261,1.453836,5.560452,8.159035,-0.889216,5.300534,2.278333,-8.465272,-7.883194,1.107857,-1.689142,8.149227,-1.682538,-2.983837,-1.748824,-7.931557,3.171072,2.207249,8.162180,-6.729227,-6.383231,-7.382882,6.094433,-6.081015,-5.157901,4.186002,-1.768484,-6.768606,-5.732868,-0.382050,3.357683,-5.630189,-1.059141,-4.361227,-8.308637,-5.034652,-1.421325,-1.717528,6.112466,1.904665,-4.486358,-8.564736,1.603667,5.960162,4.706213,1.289338,6.379692,-3.957096,2.755773,8.920391,6.296344,-1.912265,8.684591,3.490164,0.261368,-7.815846,9.220206,-4.220107,1.501352,2.386650,4.419756,3.662201,-8.240352,-3.235996,-8.953642,2.376572,0.706299,3.376161,-2.568934,3.184076,-7.713598,0.017571,4.025080,-9.491973,1.075214,1.984683,-9.481121,5.825666,-0.829530,-6.574882,-6.560044,-7.908078,1.990207,-1.116320,-7.018582,4.619778,6.813401,0.344868,-5.969643,8.574582,0.107837,-9.320228,7.003972,-3.936059,-1.032697,9.728836,-5.348405,-1.778412,9.126331,2.379500,5.768833,-7.166378,7.340944,9.855288,-5.839082,4.551018,5.786645,5.853209,-4.632637,1.989465,8.587424,6.852449,-5.718745,3.268948,-9.699093,-3.930240,-9.335004,-2.206271,-8.641861,3.875849,-3.087720,-7.402720,8.572961,-8.834609,6.055733,-8.252135,-5.287081,-5.783641,2.564922,9.910964,-9.676891,4.433567,-7.607821,-9.652883,0.435703,8.769285,-7.543075,-2.825083,-6.539827,7.232596,-1.532153,-9.131936,1.241635,7.065258,-8.149816,-9.471679,-1.410785,9.715212,7.266263,4.706858,-7.904958,-5.551818,-8.701064,-2.470647,-7.253891,-6.165457,4.084418,7.928973,2.827705,9.818664,6.214892,-4.091771,-5.801949,9.255722,3.826361,-2.268963,1.642509,9.355995,2.440578,-0.714644,7.857838,-7.793147,4.086179,-5.698307,3.194295,4.676153,7.928467,-7.657199,6.161574,-8.958547,0.706811,-6.660607,9.813110,-5.356787,8.048559,-5.213333,-2.175289,6.484312,8.256291,-0.857189,-5.446672,3.993564,-6.761146,6.613879,1.912601,-2.145133,-7.354661,-3.602819,-9.648154,7.788744,0.790077,3.155261,-6.666779,-1.913787,-3.491429,-0.949075,-6.174443,-5.738737,-1.086841,-0.174902,2.671230,-9.026772,-6.541840,-4.808680,3.553565,-6.441145,5.967349,-6.637990,7.122846,5.658986,-9.555032,-7.957724,-1.664319,5.931562,-1.017259,-6.660952,-1.713210,9.846959,1.714646,-8.817142,6.137191,-2.604392,-1.993933,7.707915,1.203706,0.233438,-0.198746,-1.984279,-0.768893,4.114133,5.958259,8.773635,-5.286750,-6.834166,-1.161092,3.287484,-9.425377,-5.060736,-6.870396,-3.975282,2.854614,9.593661,6.453306,-3.321109,1.868103,-2.558753,0.973428,0.676204,-3.018277,-2.671990,-5.018613,8.393819,8.962781,8.384844,4.774914,7.810111,7.945498,-9.000815,-9.488321,-1.567599,5.417029,-2.545373,-2.391122,-0.345701,-5.107197,1.467597,-7.955707,7.760152,9.666323,-8.931950,-0.815428,6.465725,-5.267357,-6.500619,-3.447087,6.225494,4.782014,-7.756758,6.890621,-1.412719,3.392361,-7.460335,-2.463326,6.387742,-4.245745,-8.287349,0.091201,-2.280032,-6.860490,-0.556283,1.873149,-3.294027,-9.052487,7.239868,4.277002,5.449268,2.062122,7.017862,8.526660,8.131251,-3.604181,-7.649458,4.898345,4.241625,1.128527,-3.334162,4.126742,3.050264,-8.766650,1.074540,-7.896883,-3.197881,-9.377250,-7.217718,3.905952,2.735871,6.223891,8.371335,-8.576369,-9.777225,8.982399,5.190091,7.103040,-8.595899,4.673676,-0.729817,-9.347756,9.899863,-9.366201,-5.981752,-3.915856,4.044344,4.723800,-5.886417,4.929269,7.909389,-5.846590,-3.492489,6.531913,4.095971,-7.780433,-0.282561,-3.230368,-7.515465,1.837081,-6.547675,-8.941852,-7.064870,7.684393,-5.050913,5.788868,9.252622,-7.237264,-6.511797,-5.991571,-0.368606,2.900370,5.283886,-6.412936,-7.195139,-6.397175,9.168424,-5.757778,-2.632018,9.679858,-7.499927,-4.765908,-1.329701,9.412449,-0.376277,-0.762316,4.145302,7.370975,0.223459,-6.537040,-5.238874,4.438854,0.125186,1.233494,8.085248,-2.110460,6.094819,4.551503,1.623049,-7.253127,-9.477017,-6.197411,-2.444496,-2.444897,-6.786920,7.342833,9.655575,-5.769663,-6.468135,-5.208767,-9.219463,-0.546712,0.520838,3.886827,-9.939047,-0.643498,-5.998917,-8.475191,-6.773078,3.983907,0.056603,3.145425,4.683013,-4.027138,0.246247,8.703132,1.450321,-1.777250,8.376378,-1.141630,9.323000,-2.862177,3.086348,1.966531,7.032237,-6.014372,2.593035,3.583157,-0.023534,9.431406,-0.200645,6.632694,-3.482414,-5.436934,-3.037505,7.609025,6.155421,8.554631,9.683593,-0.976230,0.801719,9.551050,5.746571,1.667011,-5.126391,1.987155,0.824254,0.030477,-1.398754,6.513975,-9.775288,9.924336,-5.958606,-6.917366,8.981534,-1.501847,-9.757696,0.237657,-8.581216,6.879429,0.354348,2.595533,0.269614,-6.230435,-6.560331,-5.874728,4.841663,-4.415819,4.205921,2.378579,-8.817059,5.617685,5.991080,-1.161394,-2.372437,0.745188,-4.569643,-2.388166,0.876057,-5.554244,9.009528,-8.519178,-1.530476,-7.526558,8.498283,-1.032188,-0.356958,-2.822030,-5.152752,3.709141,-2.082312,3.494909,-3.352033,3.513547,-8.161476,5.803693,-3.962881,-5.388872,3.783191,-9.572259,-4.033735,-0.742557,8.953185,6.741827,6.952921,-8.528239,3.540982,-7.791537,1.317654,2.164457,1.212309,1.886743,-8.332230,-2.565189,2.677086,-2.032698,2.459490,-6.999022,-1.743050,1.921312,-1.255549,3.010993,9.422075,3.688100,3.136859,-5.491406,-4.977683,1.343632,-0.406328,-0.182720,-5.723362,8.989469,5.815708,-2.629389,0.367181,3.852469,8.486311,8.724585,-4.432940,-3.207256,7.589526,0.589324,-5.752624,-0.609207,-0.914246,-8.899936,-2.394899,7.959334,0.671643,5.348392,2.687222,8.816107,9.533443,6.152477,3.691129,-8.265495,-6.918885,-0.792065,-5.905467,3.000838,9.352723,4.865150,-1.774546,0.796601,0.214125,-3.226768,0.865003,4.035700,8.598597,4.171611,-2.220561,4.016543,3.189730,-5.289227,6.784899,-3.852241,0.118088,-8.071685,-2.196575,-3.159082,-5.090365,-3.653300,-4.494009,-0.163534,-5.788324,-5.940952,9.324638,-8.185219,-9.111490,-2.702222,-9.630079,-1.266674,2.185902,4.047927,9.394507,4.253485,9.549873,2.384233,3.209673,2.761666,1.941935,8.727743,8.863593,2.991545,-3.980052,8.952130,8.775451,-9.534642,-7.312828,-5.830387,0.637443,7.407633,-6.569444,-7.001995,7.562131,6.850393,-8.136566,1.797787,-3.334712,2.206309,1.166877,-9.691214,-8.275240,1.384287,-8.289705,-8.932492,2.881567,-8.103129,8.088543,6.265265,-0.516301,9.746532,4.547987,2.986973,-2.906681,-1.319594,3.389927,-2.527113,-1.569073,4.666077,3.941718,-9.867899,7.458210,-8.746924,-3.414896,7.203592,1.719870,6.985469,-6.643375,-6.786070,1.885373,-3.428213,0.769477,-5.766775,-5.865037,4.860643,-9.548794,-1.198743,-9.358874,-7.612927,-9.616355,-8.904282,-8.601586,0.433189,-7.082451,4.822947,-9.630667,-3.342305,-5.131213,0.465370,-7.018231,2.694150,5.140475,5.097060,-4.872190,-1.488546,7.369899,-3.689425,-4.562684,-5.217013,-5.898252,-3.812535,0.432013,-7.591318,1.427434,-1.847504,-1.621303,-5.336858,7.140814,-4.773262,0.240505,2.098315,5.981250,8.121346,2.878711,-1.611846,4.152050,-6.863884,3.745090,2.623940,9.687732,4.175377,2.489928,4.934077,1.916011,-0.154339,-1.043167,3.891893,-2.876162,3.235772,1.137408,5.826441,-3.201254,4.960998,-2.814400,-7.449210,7.904460,-9.137921,-8.308076,1.698743,6.770737,-2.585143,9.903587,4.637157,-0.192704,8.101043,-4.939836,1.931272,1.925276,-2.578055,6.506001,0.658820,-2.320676,9.137908,1.379398,-1.149347,-4.601275,-7.967617,9.505518,6.722243,-8.865639,4.893724,0.346651,3.517950,6.726893,9.184712,-1.427692,9.031766,-1.231527,6.094758,-0.215557,-7.215335,2.728870,-7.481576,-2.538947,-8.598529,3.276025,6.345187,-4.006139,3.710705,-3.552950,-4.401906,0.053654,-7.046193,-2.629980,9.648006,2.178728,-4.740804,-5.758780,5.342964,-9.194861,7.253683,8.889670,8.960668,2.256673,-2.651153,0.222425,-5.575826,-0.671409,-8.640073,2.517595,6.121479,6.290634,1.322918,0.460331,-7.683412,-8.253894,1.572671,-9.922345,-2.968007,2.962722,1.870384,7.413097,8.973648,-8.321441,8.835633,1.425594,2.343185,-8.124286,-4.914512,7.739392,2.000434,-5.134377,-9.876572,2.772309,-0.083901,7.284012,4.755393,5.428646,-2.906529,-1.941853,0.715341,0.098975,-8.537627,0.452234,9.720371,8.009190,1.282402,7.360023,-1.997818,-7.604440,8.771476,3.500998,-1.752886,6.230054,-4.217632,-7.361625,1.874805,-1.738245,9.477448,-5.453713,3.182985,-8.285033,6.045391,-3.805900,-8.411512,-0.481597,-3.839904,4.112581,-5.160901,7.127079,-4.350174,1.931796,2.718393,-6.205821,4.086972,4.762296,-5.610815,1.689241,8.411672,-5.702448,-8.351369,9.760850,-7.833796,-5.536298,9.483559,0.095883,0.656704,3.249675,5.399275,-0.630574,-4.853087,0.264507,5.680588,-0.498019,-4.913565,-6.130007,9.288776,1.107423,-7.484637,7.584492,7.057778,-2.641336,6.569759,-9.739636,0.915409,3.614334,-5.793852,-7.445173,-8.371497,2.280474,6.207642,9.030642,1.971026,-3.307225,-7.143537,-6.407740,2.242705,0.574155,-9.814008,0.562750,-4.112542,-2.799095,6.961434,-0.695305,9.439940,-9.950132,7.323136,-2.456469,-1.765474,4.031743,-3.669675,-9.494759,-2.855048,-0.532315,9.881363,-3.664456,-3.920845,0.159647,8.214750,5.003283,2.204014,-0.729920,-4.672453,3.256164,1.608911,0.400528,-8.201176,3.728635,5.337461,-9.833820,4.887141,-0.510110,9.336954,6.144270,3.535955,1.682146,-3.941025,-8.850462,-7.177161,3.488229,-1.344267,7.762393,4.106823,0.987723,-4.603331,3.877717,-7.112351,-1.309368,4.338769,-2.488423,-7.245309,3.234046,7.734882,9.183804,-4.853876,-1.885195,-8.069646,9.712387,-0.420776,-9.533688,-0.352441,9.022637,-9.440430,-7.502735,7.278155,-2.878462,8.498597,0.284307,5.696892,-5.775818,2.036680,-4.791923,1.336065,6.304886,-2.278432,-0.304836,-3.657619,9.771206,1.845259,-9.910948,4.032429,3.780100,6.240753,9.025891,2.693828,-9.250831,-4.168015,-8.439425,-8.015559,-9.570601,-6.370938,-9.199077,-3.956504,5.092826,9.390405,-6.466797,-1.349211,7.702258,-0.167329,4.656443,8.320218,9.844041,-5.661180,3.014211,6.566827,-0.371235,-9.265337,-9.166239,-3.360055], dtype = "float64")#candidate|4979|(1155,)|const|float64
call_4977 = relay.TupleGetItem(func_4276_call(relay.reshape(var_4978.astype('float64'), [2, 4, 11]), relay.reshape(const_4979.astype('float64'), [1155,]), ), 0)
call_4980 = relay.TupleGetItem(func_4279_call(relay.reshape(var_4978.astype('float64'), [2, 4, 11]), relay.reshape(const_4979.astype('float64'), [1155,]), ), 0)
func_3862_call = mod.get_global_var('func_3862')
func_3863_call = mutated_mod.get_global_var('func_3863')
call_4984 = func_3862_call()
call_4985 = func_3862_call()
func_3982_call = mod.get_global_var('func_3982')
func_3984_call = mutated_mod.get_global_var('func_3984')
const_5007 = relay.const([[-3,-4,3,-9,9,-1,-1,-6,-9,3,2,-1,-10,-6,10,2,4,8,-5,-2,-2,-5,-6,-10,-5,-10,-2,7,-6,2,-1,-9,10,2,-2,-10,-1,-7,-9,1,2,2,-4,4,4,-6,-10,-1,10,-8,2,-9,6,-8,-5,-10,10,-2,2,4,4,2,5,-6,1,-9,5,-3,-6,-7,-10,9,-10,-6,-9,-10,-10,-6,-10,-10,-8,1,9,-4,7,-5,10,-10,-6,-5,-7,-5,9,-4,4,9,4,-5,6,-7,5,-9,-7,5,5,8,5,3,-7,-3,2,2,4,9,9,2,-10,-8,9,-2,-3,10,-6,-4,-1,-1,-8,1,2,-1,-7,-6,-3,-4,8,-1,-6,1,-4,-2,-1,-10,-10,1,10,-5,-5,6,5,-2,-5,6,-4,5,9,4,2,8,-2,6,-5,1,-3,-9,8,-3,-6,6,5,7,9,-5,5,3,-6,-3,1,2,2,2,5,-3,-6,1,8,-7,-1,-8,-10,6,-1,9,-5,-5,2,-5,3,-8,-6,-10,6,3,-4,4,5,1,10,-9,-1,-10,-2,-10,4,3,6,8,3,-9,-6,2,-4,-9,-1,7,-1,-4,5,-7,3,-1,-5,1,2,-6,5,-10,-1,3,-5,5,-9,-10,-5,3,9,7,3,-4,9,3,-10,-3,2,-4,-8,5,-9,2,-6,-2,-1,10,4,-10,8,7,6,2,9,7,6,-5,-8,9,-3,10,-7,-7,6,5,1,-5,-3,-7,2,10,-5,-1,3,7,-10,-10,-9,7,4,-1,-6,-2,-1,3,-2,-9,7,9,1,-6,5,7,2,-9,-6,1,-7,2,3,-1,-6,3,-4,5,-10,-8,8,-1,9,-9,2,-8,-7,9,6,7,2,-7,-4,-6,5,1,9,-6,-4,3,6,-5,4,5,3,1,-3,6,1,2,-3,-1,-7,-1,3,6,-7,-4,-4,8,10,5,-10,-1,-2,-8,9,9,8,8,-6,-5,-5,4,8,7,3,-5,4,3,10,4,3,-7,3,-4,-10,-2,8,4,-9,-7,-4,5,-8,-7,2,-10,-5,5,2,7,-8],[9,-6,-1,-6,9,-9,-10,-5,-5,-8,-1,2,1,7,8,-10,9,-1,-10,9,7,-4,-6,5,5,8,6,-3,-6,6,4,-2,-1,5,8,-3,-3,3,7,1,-1,9,9,-4,-4,10,6,3,4,3,2,-8,-4,-4,-9,4,-6,-5,6,-1,-2,8,-2,7,7,-8,5,-3,7,1,-2,3,-7,2,-10,4,1,-1,-3,9,-8,8,-2,-4,6,-2,8,6,-6,1,-1,-9,8,-7,8,-10,2,-2,9,-3,9,5,3,-7,10,-4,-2,3,-2,-1,-6,-7,-9,5,2,6,3,3,5,-2,5,-7,-10,-6,-3,-3,8,-9,8,6,2,-3,5,9,-3,6,1,-6,-6,-5,1,-9,-9,-5,-2,7,5,9,6,-2,10,-1,-3,-4,-1,-9,-9,3,-9,-5,1,7,3,-8,3,-10,-9,-6,7,-5,-10,-5,5,7,8,6,-7,7,-8,-9,-6,6,1,10,-3,-8,-1,10,-9,-9,2,-8,8,-10,-2,-9,-9,4,6,-8,10,2,7,7,-10,4,-4,2,8,10,1,8,4,-2,7,1,-5,1,4,9,6,7,-8,4,3,5,5,5,-5,-4,-6,4,-8,3,-4,-10,-10,2,8,-5,4,-6,-3,-10,10,5,-9,-9,-3,-2,7,-9,9,-4,-9,-9,-8,10,7,-2,-4,-5,5,1,-6,-6,5,9,-7,10,-3,7,-5,5,-10,9,5,6,-7,9,-10,-8,2,-8,4,5,8,-1,2,2,-2,-6,6,8,-1,-9,-3,7,-4,-6,-4,6,-6,4,2,10,9,-2,9,10,-8,-2,-6,8,-3,-8,7,8,2,1,-10,-7,-10,5,10,9,4,9,-10,2,1,-2,-6,2,-2,2,-8,10,10,5,-3,-8,-6,9,-1,-1,2,1,-4,8,7,-10,8,3,7,10,4,7,2,-8,-10,7,2,2,10,2,9,-4,-1,-9,-7,-8,-4,3,-2,10,9,4,5,7,-7,5,-10,6,-8,-2,3,-5,5,-4,-10,1,-2,-3,2,-2,-1,-6,6,6,7,8,-8,-9,-3],[-1,7,-2,-10,6,5,2,5,-8,-2,-6,2,10,-8,-10,2,-4,7,2,9,9,5,1,-1,-2,5,1,3,5,2,2,1,7,-2,-5,-6,-6,-8,-1,-9,-2,-3,10,-6,-7,2,-2,-7,-9,7,-9,-8,2,-5,-5,-9,7,-9,10,-3,4,8,8,-7,4,1,-5,-10,7,3,10,-6,-4,5,2,10,-5,4,-4,10,-2,-1,4,-5,9,-2,10,7,4,-7,-1,-2,7,-2,6,-1,5,-7,-5,9,-10,2,-8,5,10,8,-1,10,8,-1,3,3,5,-8,-2,-4,-5,-4,7,5,-3,1,-5,4,-4,-8,-6,-7,-2,-1,10,-9,-6,-10,-2,10,-9,-9,-5,-10,9,-6,-10,6,-5,-8,-4,4,2,3,-10,-9,-6,-5,-3,-10,2,7,-8,-4,2,2,1,-8,-7,-6,3,-5,-8,-10,5,3,-5,-9,-5,-7,-7,7,-2,-10,5,7,-5,-9,-5,4,-10,-7,-7,-9,9,3,5,-3,-4,-10,-3,7,1,9,-6,8,-9,-10,-1,-3,4,-6,4,8,6,-7,4,5,1,-3,-6,-2,6,-3,2,7,10,7,-7,-3,2,10,-7,3,-10,6,9,-2,9,-4,-9,-7,6,-6,8,6,1,-7,-2,8,-9,9,-10,3,-4,2,-9,6,-6,10,4,-5,-3,-5,3,8,-6,9,6,9,10,7,4,-5,-8,4,3,6,10,-3,-5,-6,-8,10,7,-7,-3,-6,-10,5,8,-9,-9,-6,-8,-5,-10,7,3,1,7,7,-2,4,4,9,1,4,5,-2,-9,-10,-5,6,-4,-10,-6,-8,-9,-2,4,-6,1,8,10,-1,-6,-9,-7,10,5,-2,-6,1,3,-8,-5,5,-4,2,-2,4,-3,10,9,1,10,5,4,-9,9,7,4,8,4,4,2,-5,-3,6,4,8,-1,-8,-10,3,6,3,-1,-10,10,2,-3,8,-3,-2,4,-3,-2,1,9,3,-3,7,-7,8,10,1,8,-3,-6,9,2,6,-2,8,-10,-7,7,-4,1,-2,-3,-8,4,1,4,-1,-2]], dtype = "uint8")#candidate|5007|(3, 405)|const|uint8
call_5006 = relay.TupleGetItem(func_3982_call(relay.reshape(const_5007.astype('uint8'), [1215,])), 2)
call_5008 = relay.TupleGetItem(func_3984_call(relay.reshape(const_5007.astype('uint8'), [1215,])), 2)
output = relay.Tuple([call_4971,call_4974,var_4975,call_4977,var_4978,const_4979,call_4984,call_5006,const_5007,])
output2 = relay.Tuple([call_4972,call_4976,var_4975,call_4980,var_4978,const_4979,call_4985,call_5008,const_5007,])
func_5017 = relay.Function([var_4975,var_4978,], output)
mod['func_5017'] = func_5017
mod = relay.transform.InferType()(mod)
var_5018 = relay.var("var_5018", dtype = "float32", shape = (234,))#candidate|5018|(234,)|var|float32
var_5019 = relay.var("var_5019", dtype = "float64", shape = (88,))#candidate|5019|(88,)|var|float64
output = func_5017(var_5018,var_5019,)
func_5020 = relay.Function([var_5018,var_5019,], output)
mutated_mod['func_5020'] = func_5020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4517_call = mod.get_global_var('func_4517')
func_4518_call = mutated_mod.get_global_var('func_4518')
call_5031 = relay.TupleGetItem(func_4517_call(), 0)
call_5032 = relay.TupleGetItem(func_4518_call(), 0)
output = call_5031
output2 = call_5032
func_5042 = relay.Function([], output)
mod['func_5042'] = func_5042
mod = relay.transform.InferType()(mod)
mutated_mod['func_5042'] = func_5042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5042_call = mutated_mod.get_global_var('func_5042')
call_5043 = func_5042_call()
output = call_5043
func_5044 = relay.Function([], output)
mutated_mod['func_5044'] = func_5044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3862_call = mod.get_global_var('func_3862')
func_3863_call = mutated_mod.get_global_var('func_3863')
call_5053 = func_3862_call()
call_5054 = func_3862_call()
var_5055 = relay.var("var_5055", dtype = "float64", shape = (2, 13, 5))#candidate|5055|(2, 13, 5)|var|float64
bop_5056 = relay.divide(call_5053.astype('float64'), relay.reshape(var_5055.astype('float64'), relay.shape_of(call_5053))) # shape=(2, 13, 5)
bop_5059 = relay.divide(call_5054.astype('float64'), relay.reshape(var_5055.astype('float64'), relay.shape_of(call_5054))) # shape=(2, 13, 5)
output = relay.Tuple([bop_5056,])
output2 = relay.Tuple([bop_5059,])
func_5060 = relay.Function([var_5055,], output)
mod['func_5060'] = func_5060
mod = relay.transform.InferType()(mod)
var_5061 = relay.var("var_5061", dtype = "float64", shape = (2, 13, 5))#candidate|5061|(2, 13, 5)|var|float64
output = func_5060(var_5061)
func_5062 = relay.Function([var_5061], output)
mutated_mod['func_5062'] = func_5062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4378_call = mod.get_global_var('func_4378')
func_4379_call = mutated_mod.get_global_var('func_4379')
call_5117 = relay.TupleGetItem(func_4378_call(), 0)
call_5118 = relay.TupleGetItem(func_4379_call(), 0)
func_3380_call = mod.get_global_var('func_3380')
func_3383_call = mutated_mod.get_global_var('func_3383')
var_5135 = relay.var("var_5135", dtype = "float32", shape = (525,))#candidate|5135|(525,)|var|float32
call_5134 = relay.TupleGetItem(func_3380_call(relay.reshape(var_5135.astype('float32'), [5, 7, 15]), relay.reshape(var_5135.astype('float32'), [5, 7, 15]), ), 0)
call_5136 = relay.TupleGetItem(func_3383_call(relay.reshape(var_5135.astype('float32'), [5, 7, 15]), relay.reshape(var_5135.astype('float32'), [5, 7, 15]), ), 0)
uop_5147 = relay.acos(call_5134.astype('float32')) # shape=(5, 7, 15)
uop_5149 = relay.acos(call_5136.astype('float32')) # shape=(5, 7, 15)
func_4517_call = mod.get_global_var('func_4517')
func_4518_call = mutated_mod.get_global_var('func_4518')
call_5155 = relay.TupleGetItem(func_4517_call(), 0)
call_5156 = relay.TupleGetItem(func_4518_call(), 0)
output = relay.Tuple([call_5117,var_5135,uop_5147,call_5155,])
output2 = relay.Tuple([call_5118,var_5135,uop_5149,call_5156,])
func_5178 = relay.Function([var_5135,], output)
mod['func_5178'] = func_5178
mod = relay.transform.InferType()(mod)
var_5179 = relay.var("var_5179", dtype = "float32", shape = (525,))#candidate|5179|(525,)|var|float32
output = func_5178(var_5179)
func_5180 = relay.Function([var_5179], output)
mutated_mod['func_5180'] = func_5180
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5185 = relay.var("var_5185", dtype = "float32", shape = (5, 3, 6))#candidate|5185|(5, 3, 6)|var|float32
uop_5186 = relay.sin(var_5185.astype('float32')) # shape=(5, 3, 6)
bop_5191 = relay.mod(uop_5186.astype('float64'), relay.reshape(var_5185.astype('float64'), relay.shape_of(uop_5186))) # shape=(5, 3, 6)
var_5194 = relay.var("var_5194", dtype = "float64", shape = (5, 3, 6))#candidate|5194|(5, 3, 6)|var|float64
bop_5195 = relay.logical_xor(bop_5191.astype('int64'), relay.reshape(var_5194.astype('int64'), relay.shape_of(bop_5191))) # shape=(5, 3, 6)
func_3641_call = mod.get_global_var('func_3641')
func_3643_call = mutated_mod.get_global_var('func_3643')
const_5204 = relay.const([0.151969,7.278043,-5.189356,-8.717462,9.989122,-8.342367,-0.194282,-4.515580,4.617426,9.198948,3.611521,2.393318,-8.183654,4.417321,-4.886345,-5.082280], dtype = "float64")#candidate|5204|(16,)|const|float64
call_5203 = relay.TupleGetItem(func_3641_call(relay.reshape(const_5204.astype('float64'), [4, 4, 1])), 0)
call_5205 = relay.TupleGetItem(func_3643_call(relay.reshape(const_5204.astype('float64'), [4, 4, 1])), 0)
output = relay.Tuple([bop_5195,call_5203,const_5204,])
output2 = relay.Tuple([bop_5195,call_5205,const_5204,])
func_5211 = relay.Function([var_5185,var_5194,], output)
mod['func_5211'] = func_5211
mod = relay.transform.InferType()(mod)
var_5212 = relay.var("var_5212", dtype = "float32", shape = (5, 3, 6))#candidate|5212|(5, 3, 6)|var|float32
var_5213 = relay.var("var_5213", dtype = "float64", shape = (5, 3, 6))#candidate|5213|(5, 3, 6)|var|float64
output = func_5211(var_5212,var_5213,)
func_5214 = relay.Function([var_5212,var_5213,], output)
mutated_mod['func_5214'] = func_5214
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5237 = relay.var("var_5237", dtype = "uint32", shape = (4, 14, 1))#candidate|5237|(4, 14, 1)|var|uint32
var_5238 = relay.var("var_5238", dtype = "uint32", shape = (4, 14, 15))#candidate|5238|(4, 14, 15)|var|uint32
bop_5239 = relay.less(var_5237.astype('bool'), var_5238.astype('bool')) # shape=(4, 14, 15)
uop_5245 = relay.atan(bop_5239.astype('float64')) # shape=(4, 14, 15)
func_4276_call = mod.get_global_var('func_4276')
func_4279_call = mutated_mod.get_global_var('func_4279')
const_5256 = relay.const([-6.191288,9.779470,2.831254,7.451115,6.736398,3.181320,7.803769,-6.423422,4.434722,4.349593,-9.897709,7.651963,-5.934202,7.081425,-6.228766,-7.915248,8.547156,2.823119,6.031633,6.184458,-4.295075,-8.264981,1.046112,-7.796962,-9.831335,-5.347907,7.011081,-4.087896,9.988301,8.832008,3.135548,-0.507302,5.961474,0.620940,4.407061,9.839745,0.946712,3.978913,8.531508,0.703737,7.513910,-1.705166,7.231087,-7.337778,3.557284,-2.085894,8.545444,6.571075,5.675783,-9.119574,-0.552618,-2.512355,9.926383,-2.903373,4.331009,7.171712,-1.867243,4.565055,-4.388530,-8.797677,9.507622,-5.624397,6.199800,-0.106101,-3.677204,7.104055,-1.691923,-4.658314,1.216467,-3.130914,-5.757400,0.547927,-6.841551,8.803216,2.389281,-8.010757,-5.355671,4.320768,-1.098939,-9.189567,-3.931869,1.095666,6.903645,0.333744,6.484789,-6.902256,1.220105,-8.367218], dtype = "float64")#candidate|5256|(88,)|const|float64
var_5257 = relay.var("var_5257", dtype = "float64", shape = (7, 165))#candidate|5257|(7, 165)|var|float64
call_5255 = relay.TupleGetItem(func_4276_call(relay.reshape(const_5256.astype('float64'), [2, 4, 11]), relay.reshape(var_5257.astype('float64'), [1155,]), ), 2)
call_5258 = relay.TupleGetItem(func_4279_call(relay.reshape(const_5256.astype('float64'), [2, 4, 11]), relay.reshape(var_5257.astype('float64'), [1155,]), ), 2)
var_5261 = relay.var("var_5261", dtype = "float64", shape = (4, 14, 15))#candidate|5261|(4, 14, 15)|var|float64
bop_5262 = relay.bitwise_or(uop_5245.astype('int8'), relay.reshape(var_5261.astype('int8'), relay.shape_of(uop_5245))) # shape=(4, 14, 15)
func_3786_call = mod.get_global_var('func_3786')
func_3788_call = mutated_mod.get_global_var('func_3788')
call_5266 = relay.TupleGetItem(func_3786_call(), 0)
call_5267 = relay.TupleGetItem(func_3788_call(), 0)
var_5276 = relay.var("var_5276", dtype = "int8", shape = (4, 14, 15))#candidate|5276|(4, 14, 15)|var|int8
bop_5277 = relay.bitwise_xor(bop_5262.astype('int64'), relay.reshape(var_5276.astype('int64'), relay.shape_of(bop_5262))) # shape=(4, 14, 15)
bop_5283 = relay.add(bop_5277.astype('int64'), relay.reshape(var_5238.astype('int64'), relay.shape_of(bop_5277))) # shape=(4, 14, 15)
func_3982_call = mod.get_global_var('func_3982')
func_3984_call = mutated_mod.get_global_var('func_3984')
var_5289 = relay.var("var_5289", dtype = "uint8", shape = (1215,))#candidate|5289|(1215,)|var|uint8
call_5288 = relay.TupleGetItem(func_3982_call(relay.reshape(var_5289.astype('uint8'), [1215,])), 3)
call_5290 = relay.TupleGetItem(func_3984_call(relay.reshape(var_5289.astype('uint8'), [1215,])), 3)
func_2535_call = mod.get_global_var('func_2535')
func_2540_call = mutated_mod.get_global_var('func_2540')
var_5301 = relay.var("var_5301", dtype = "float64", shape = (520, 1))#candidate|5301|(520, 1)|var|float64
const_5302 = relay.const(1, dtype = "uint8")#candidate|5302|()|const|uint8
const_5303 = relay.const([-10,6,10,-7,9,4,9,4,-6,-8,6,-1,4,2,-10,1,3,-5,1,9,6,-7,9,-6,6,1,9,2,6,9,2,-7,9,8,-4,10,-2,-4,2,5,7,10,8,9,6,1,10,-3,-7,-9,-7,2,9,8,7,9,-9,-10,-9,-2,-9,-4,-10,5,7,-10,-6,4,8,7,5,-9,-3,1,10,-8,6,-5,1,6,6,4,8,-9,10,-2,-10,-9,-2,6,4,8,-9,6,4,8,8,4,-10,2,7,-4,7,-3,-4,10,4,-5,10,3,-3,-6,2,9,-2,-1,7,9,9,-2,10,8,-9,-7,6,6,10,2,-1,4,-4,-4,10,-6,7,1,-1,1,6,2,7,-1,8,-9,-6,4,-7,4,6,-8,1,8,10,3,-9,-8,-1,-3,4,-1,2,4,-6,9,-10,2,-6,-3,-4,-4,1,9,-3,-4,2,-9,1,-6,-4,10,1,3,-4,8,3,1,4,-8,10,-3,-7,9,-8,6,1,3,-8,1,-5,10,-3,-3,-10,-3,5,3,10,2,8,-9,-4,10,1,3,-4,-3,7,3,1,8,-4,9,-4,2,-9,-10,3,4,-3,7,4,-2,10,-8], dtype = "uint16")#candidate|5303|(234,)|const|uint16
call_5300 = relay.TupleGetItem(func_2535_call(relay.reshape(var_5301.astype('float64'), [8, 13, 5]), relay.reshape(const_5302.astype('uint8'), []), relay.reshape(var_5289.astype('uint8'), [81, 15]), relay.reshape(const_5303.astype('uint16'), [234,]), ), 5)
call_5304 = relay.TupleGetItem(func_2540_call(relay.reshape(var_5301.astype('float64'), [8, 13, 5]), relay.reshape(const_5302.astype('uint8'), []), relay.reshape(var_5289.astype('uint8'), [81, 15]), relay.reshape(const_5303.astype('uint16'), [234,]), ), 5)
output = relay.Tuple([call_5255,const_5256,var_5257,call_5266,bop_5283,call_5288,var_5289,call_5300,var_5301,const_5302,const_5303,])
output2 = relay.Tuple([call_5258,const_5256,var_5257,call_5267,bop_5283,call_5290,var_5289,call_5304,var_5301,const_5302,const_5303,])
func_5307 = relay.Function([var_5237,var_5238,var_5257,var_5261,var_5276,var_5289,var_5301,], output)
mod['func_5307'] = func_5307
mod = relay.transform.InferType()(mod)
mutated_mod['func_5307'] = func_5307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5307_call = mutated_mod.get_global_var('func_5307')
var_5309 = relay.var("var_5309", dtype = "uint32", shape = (4, 14, 1))#candidate|5309|(4, 14, 1)|var|uint32
var_5310 = relay.var("var_5310", dtype = "uint32", shape = (4, 14, 15))#candidate|5310|(4, 14, 15)|var|uint32
var_5311 = relay.var("var_5311", dtype = "float64", shape = (7, 165))#candidate|5311|(7, 165)|var|float64
var_5312 = relay.var("var_5312", dtype = "float64", shape = (4, 14, 15))#candidate|5312|(4, 14, 15)|var|float64
var_5313 = relay.var("var_5313", dtype = "int8", shape = (4, 14, 15))#candidate|5313|(4, 14, 15)|var|int8
var_5314 = relay.var("var_5314", dtype = "uint8", shape = (1215,))#candidate|5314|(1215,)|var|uint8
var_5315 = relay.var("var_5315", dtype = "float64", shape = (520, 1))#candidate|5315|(520, 1)|var|float64
call_5308 = func_5307_call(var_5309,var_5310,var_5311,var_5312,var_5313,var_5314,var_5315,)
output = call_5308
func_5316 = relay.Function([var_5309,var_5310,var_5311,var_5312,var_5313,var_5314,var_5315,], output)
mutated_mod['func_5316'] = func_5316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3786_call = mod.get_global_var('func_3786')
func_3788_call = mutated_mod.get_global_var('func_3788')
call_5331 = relay.TupleGetItem(func_3786_call(), 0)
call_5332 = relay.TupleGetItem(func_3788_call(), 0)
output = relay.Tuple([call_5331,])
output2 = relay.Tuple([call_5332,])
func_5333 = relay.Function([], output)
mod['func_5333'] = func_5333
mod = relay.transform.InferType()(mod)
mutated_mod['func_5333'] = func_5333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5333_call = mutated_mod.get_global_var('func_5333')
call_5334 = func_5333_call()
output = call_5334
func_5335 = relay.Function([], output)
mutated_mod['func_5335'] = func_5335
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5340 = relay.var("var_5340", dtype = "float32", shape = (13, 3, 3))#candidate|5340|(13, 3, 3)|var|float32
var_5341 = relay.var("var_5341", dtype = "float32", shape = (13, 3, 3))#candidate|5341|(13, 3, 3)|var|float32
bop_5342 = relay.floor_divide(var_5340.astype('float32'), relay.reshape(var_5341.astype('float32'), relay.shape_of(var_5340))) # shape=(13, 3, 3)
func_4378_call = mod.get_global_var('func_4378')
func_4379_call = mutated_mod.get_global_var('func_4379')
call_5345 = relay.TupleGetItem(func_4378_call(), 0)
call_5346 = relay.TupleGetItem(func_4379_call(), 0)
uop_5348 = relay.asin(bop_5342.astype('float64')) # shape=(13, 3, 3)
output = relay.Tuple([call_5345,uop_5348,])
output2 = relay.Tuple([call_5346,uop_5348,])
func_5365 = relay.Function([var_5340,var_5341,], output)
mod['func_5365'] = func_5365
mod = relay.transform.InferType()(mod)
mutated_mod['func_5365'] = func_5365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5365_call = mutated_mod.get_global_var('func_5365')
var_5367 = relay.var("var_5367", dtype = "float32", shape = (13, 3, 3))#candidate|5367|(13, 3, 3)|var|float32
var_5368 = relay.var("var_5368", dtype = "float32", shape = (13, 3, 3))#candidate|5368|(13, 3, 3)|var|float32
call_5366 = func_5365_call(var_5367,var_5368,)
output = call_5366
func_5369 = relay.Function([var_5367,var_5368,], output)
mutated_mod['func_5369'] = func_5369
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5394 = relay.var("var_5394", dtype = "float64", shape = (12, 8))#candidate|5394|(12, 8)|var|float64
uop_5395 = relay.log2(var_5394.astype('float64')) # shape=(12, 8)
output = uop_5395
output2 = uop_5395
func_5401 = relay.Function([var_5394,], output)
mod['func_5401'] = func_5401
mod = relay.transform.InferType()(mod)
mutated_mod['func_5401'] = func_5401
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5402 = relay.var("var_5402", dtype = "float64", shape = (12, 8))#candidate|5402|(12, 8)|var|float64
func_5401_call = mutated_mod.get_global_var('func_5401')
call_5403 = func_5401_call(var_5402)
output = call_5403
func_5404 = relay.Function([var_5402], output)
mutated_mod['func_5404'] = func_5404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3351_call = mod.get_global_var('func_3351')
func_3352_call = mutated_mod.get_global_var('func_3352')
call_5507 = func_3351_call()
call_5508 = func_3351_call()
output = call_5507
output2 = call_5508
func_5521 = relay.Function([], output)
mod['func_5521'] = func_5521
mod = relay.transform.InferType()(mod)
output = func_5521()
func_5522 = relay.Function([], output)
mutated_mod['func_5522'] = func_5522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4635_call = mod.get_global_var('func_4635')
func_4637_call = mutated_mod.get_global_var('func_4637')
call_5562 = relay.TupleGetItem(func_4635_call(), 0)
call_5563 = relay.TupleGetItem(func_4637_call(), 0)
var_5570 = relay.var("var_5570", dtype = "float64", shape = (2, 13, 5))#candidate|5570|(2, 13, 5)|var|float64
bop_5571 = relay.greater(call_5562.astype('bool'), relay.reshape(var_5570.astype('bool'), relay.shape_of(call_5562))) # shape=(2, 13, 5)
bop_5574 = relay.greater(call_5563.astype('bool'), relay.reshape(var_5570.astype('bool'), relay.shape_of(call_5563))) # shape=(2, 13, 5)
output = bop_5571
output2 = bop_5574
func_5625 = relay.Function([var_5570,], output)
mod['func_5625'] = func_5625
mod = relay.transform.InferType()(mod)
mutated_mod['func_5625'] = func_5625
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5626 = relay.var("var_5626", dtype = "float64", shape = (2, 13, 5))#candidate|5626|(2, 13, 5)|var|float64
func_5625_call = mutated_mod.get_global_var('func_5625')
call_5627 = func_5625_call(var_5626)
output = call_5627
func_5628 = relay.Function([var_5626], output)
mutated_mod['func_5628'] = func_5628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_5633 = relay.TupleGetItem(func_3534_call(), 2)
call_5634 = relay.TupleGetItem(func_3536_call(), 2)
output = relay.Tuple([call_5633,])
output2 = relay.Tuple([call_5634,])
func_5638 = relay.Function([], output)
mod['func_5638'] = func_5638
mod = relay.transform.InferType()(mod)
mutated_mod['func_5638'] = func_5638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5638_call = mutated_mod.get_global_var('func_5638')
call_5639 = func_5638_call()
output = call_5639
func_5640 = relay.Function([], output)
mutated_mod['func_5640'] = func_5640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3947_call = mod.get_global_var('func_3947')
func_3949_call = mutated_mod.get_global_var('func_3949')
call_5660 = func_3947_call()
call_5661 = func_3947_call()
output = call_5660
output2 = call_5661
func_5663 = relay.Function([], output)
mod['func_5663'] = func_5663
mod = relay.transform.InferType()(mod)
mutated_mod['func_5663'] = func_5663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5663_call = mutated_mod.get_global_var('func_5663')
call_5664 = func_5663_call()
output = call_5664
func_5665 = relay.Function([], output)
mutated_mod['func_5665'] = func_5665
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5687 = relay.const([[[-7.524568,1.715891,8.625508,4.516114,-9.330075,5.734633,-5.088065,-9.412793],[-9.390580,8.987137,4.484490,-7.121169,-4.028729,-1.079463,-5.426026,-7.048343],[-3.325995,-8.054845,-6.965687,9.021639,-9.612365,9.005547,-1.189703,-3.002318],[7.811245,1.480960,1.025372,6.864068,-8.792925,-5.895146,7.324062,-7.044978],[7.765631,5.445991,-3.010221,-1.920977,-9.107520,4.904758,3.262956,0.753110],[7.534004,5.739612,-8.685781,-8.101603,-9.909388,3.357897,-9.346448,7.353096],[-1.834415,7.284444,-4.804259,-9.568488,1.821388,6.576248,2.603907,0.665236],[6.581576,8.612828,8.088484,8.149203,1.341430,-1.453687,-8.117212,3.425074],[-9.659371,7.599252,-0.315838,1.782650,0.292810,3.838000,0.348727,4.194012],[3.171232,9.688528,-6.580295,9.782310,9.764570,5.151339,5.720856,9.551035],[-4.484797,-4.503700,-3.128911,-2.441792,-6.568405,-0.632194,5.758123,2.303613],[-4.948600,1.329568,8.076040,-4.291826,-9.534096,-7.832931,-9.369359,-9.609053]],[[-8.034841,-4.001806,-8.872755,-9.834993,-9.132603,7.419743,-6.157980,-1.447354],[5.576186,2.633535,-1.658636,4.830470,-3.386453,5.942320,2.207272,9.652158],[-1.716163,-3.713767,-5.282134,-3.648040,5.457024,-3.079585,-5.944486,1.758266],[8.813256,-3.128238,-2.803260,-6.713694,4.405179,-1.701817,6.423501,-0.298385],[4.559068,6.597487,3.073554,-1.600508,2.846258,-3.828215,1.172782,6.576848],[-8.393424,1.711865,8.954910,7.407896,7.968454,-3.925445,1.560567,-1.341990],[3.087143,6.369146,5.726535,-2.235684,-3.730763,-3.661597,-5.210130,-4.142254],[5.034462,8.539693,-6.629717,0.195151,-2.524498,-6.189510,-5.415670,-0.487704],[-6.497110,-7.672144,7.846947,-7.940694,0.272913,-1.188253,-7.296000,5.396970],[-7.146095,9.576189,9.501044,-9.250131,-0.614276,-1.329360,1.934296,-7.530326],[-4.527987,-5.481246,7.736145,3.764699,3.248259,-3.904782,8.233928,-8.950945],[9.397916,-9.180854,-5.535047,-3.511571,0.146829,-1.579979,-9.192541,5.867391]],[[6.273037,-9.978560,-3.419429,-7.622519,8.743085,-3.940657,-7.467323,-2.544935],[-9.768271,-4.172016,7.698912,6.493833,8.757013,-9.233714,-1.871276,-1.820607],[8.962961,1.047814,1.694368,8.015589,-9.698211,8.618591,-9.851851,-7.237660],[-5.528145,-8.483171,-6.140121,-1.922311,5.294795,5.593879,-0.313401,2.844083],[-0.873240,-1.917102,-8.773350,5.301643,1.614236,8.672148,-4.716043,-4.286624],[7.109991,3.853742,-6.810399,4.004607,-5.121154,2.209345,2.994949,-9.460567],[8.458915,2.824055,-0.012207,4.669026,0.866755,-6.533680,-4.091074,-1.659060],[6.408505,4.936765,0.359666,5.658319,8.268401,2.171708,5.205824,4.033113],[-4.881345,5.482775,1.038739,-4.489529,3.340258,-0.136821,2.410867,7.070560],[-7.751386,-6.780497,-1.712652,6.384445,-4.280615,-0.519137,-1.275868,3.312000],[-9.285596,-1.212465,9.592554,-7.977163,5.736980,-2.913269,6.893445,2.912348],[1.695607,3.686839,1.152080,5.995929,5.713314,1.380178,3.232235,-4.358302]],[[0.942484,0.675167,7.021847,-6.857442,7.232068,2.623306,-8.014794,-7.937329],[-5.180736,1.183050,3.326516,-9.425293,-8.974243,-3.603341,-7.545763,0.366498],[8.443708,-9.880616,-3.508312,2.100932,7.024137,-2.291256,1.485798,5.778632],[5.172664,4.152811,-8.126356,1.781948,-0.138547,-9.051135,8.887696,-1.929630],[1.254356,5.001417,3.949038,9.770995,-1.296838,0.508564,-1.558896,4.725468],[4.301184,-5.558298,-1.556166,6.135527,-1.744182,1.700091,4.584717,-6.617146],[-7.313218,3.708130,0.864477,9.681016,-8.531372,7.557091,9.229959,-1.104998],[-8.174916,-3.753022,2.748716,2.963670,-0.043509,3.254406,-1.250292,-6.513811],[9.185756,9.680177,-8.155735,-0.549472,9.964497,5.352818,0.263507,5.831351],[6.421071,-2.008171,1.959904,-5.671878,3.970707,-2.702923,3.964023,-4.442478],[-9.588964,3.511708,-1.081493,9.242596,-3.467939,4.379631,1.947843,7.951658],[-4.609644,3.387408,9.212720,2.580426,8.035128,-2.471077,-0.131497,7.194654]],[[-1.660497,0.517029,1.982655,-6.892594,-6.672511,9.957249,9.608992,-5.368416],[-5.067604,2.480744,4.317865,-0.763674,-7.272512,5.321687,-8.741730,3.041072],[-3.745657,4.697661,-7.214940,4.929604,2.902284,-7.687279,4.914229,0.228184],[-7.516804,4.976994,4.004478,-3.302624,-8.643670,6.850427,-3.060619,-7.454962],[2.675137,-3.510028,9.846108,-4.870656,-5.275996,4.835513,9.735122,-5.461840],[-1.206210,4.024218,2.287127,0.444275,-8.672301,-7.859756,-6.933702,0.605982],[0.152423,6.702761,5.742653,0.562514,-7.290188,6.208990,3.198019,6.258127],[0.751914,-6.660897,-2.840747,-3.479485,-9.432179,3.129693,3.356777,-9.981239],[0.875875,-5.791621,-5.362579,-1.834788,-6.281576,-9.922697,9.201327,5.664552],[8.326987,-9.634147,-6.122003,-8.456179,6.488578,1.409736,-9.328195,1.240068],[6.867850,-6.756081,-6.687182,-2.069949,-9.504319,-8.037316,-2.420804,-8.296382],[2.551692,6.720637,5.675766,-4.770274,0.003286,-8.695810,-7.911367,9.327076]]], dtype = "float32")#candidate|5687|(5, 12, 8)|const|float32
uop_5688 = relay.cos(const_5687.astype('float32')) # shape=(5, 12, 8)
func_1798_call = mod.get_global_var('func_1798')
func_1802_call = mutated_mod.get_global_var('func_1802')
var_5710 = relay.var("var_5710", dtype = "uint16", shape = (945,))#candidate|5710|(945,)|var|uint16
call_5709 = func_1798_call(relay.reshape(var_5710.astype('uint16'), [7, 9, 15]), relay.reshape(var_5710.astype('uint16'), [7, 9, 15]), )
call_5711 = func_1798_call(relay.reshape(var_5710.astype('uint16'), [7, 9, 15]), relay.reshape(var_5710.astype('uint16'), [7, 9, 15]), )
output = relay.Tuple([uop_5688,call_5709,var_5710,])
output2 = relay.Tuple([uop_5688,call_5711,var_5710,])
func_5714 = relay.Function([var_5710,], output)
mod['func_5714'] = func_5714
mod = relay.transform.InferType()(mod)
var_5715 = relay.var("var_5715", dtype = "uint16", shape = (945,))#candidate|5715|(945,)|var|uint16
output = func_5714(var_5715)
func_5716 = relay.Function([var_5715], output)
mutated_mod['func_5716'] = func_5716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3862_call = mod.get_global_var('func_3862')
func_3863_call = mutated_mod.get_global_var('func_3863')
call_5744 = func_3862_call()
call_5745 = func_3862_call()
output = relay.Tuple([call_5744,])
output2 = relay.Tuple([call_5745,])
func_5782 = relay.Function([], output)
mod['func_5782'] = func_5782
mod = relay.transform.InferType()(mod)
mutated_mod['func_5782'] = func_5782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5782_call = mutated_mod.get_global_var('func_5782')
call_5783 = func_5782_call()
output = call_5783
func_5784 = relay.Function([], output)
mutated_mod['func_5784'] = func_5784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_5820 = relay.TupleGetItem(func_3534_call(), 0)
call_5821 = relay.TupleGetItem(func_3536_call(), 0)
func_3580_call = mod.get_global_var('func_3580')
func_3581_call = mutated_mod.get_global_var('func_3581')
call_5822 = relay.TupleGetItem(func_3580_call(), 1)
call_5823 = relay.TupleGetItem(func_3581_call(), 1)
func_5060_call = mod.get_global_var('func_5060')
func_5062_call = mutated_mod.get_global_var('func_5062')
call_5847 = relay.TupleGetItem(func_5060_call(relay.reshape(call_5822.astype('float64'), [2, 13, 5])), 0)
call_5848 = relay.TupleGetItem(func_5062_call(relay.reshape(call_5822.astype('float64'), [2, 13, 5])), 0)
uop_5861 = relay.log(call_5820.astype('float32')) # shape=(16, 14, 14)
uop_5863 = relay.log(call_5821.astype('float32')) # shape=(16, 14, 14)
var_5864 = relay.var("var_5864", dtype = "float32", shape = (16, 14, 14))#candidate|5864|(16, 14, 14)|var|float32
bop_5865 = relay.bitwise_and(uop_5861.astype('uint32'), relay.reshape(var_5864.astype('uint32'), relay.shape_of(uop_5861))) # shape=(16, 14, 14)
bop_5868 = relay.bitwise_and(uop_5863.astype('uint32'), relay.reshape(var_5864.astype('uint32'), relay.shape_of(uop_5863))) # shape=(16, 14, 14)
output = relay.Tuple([call_5822,call_5847,bop_5865,])
output2 = relay.Tuple([call_5823,call_5848,bop_5868,])
func_5872 = relay.Function([var_5864,], output)
mod['func_5872'] = func_5872
mod = relay.transform.InferType()(mod)
var_5873 = relay.var("var_5873", dtype = "float32", shape = (16, 14, 14))#candidate|5873|(16, 14, 14)|var|float32
output = func_5872(var_5873)
func_5874 = relay.Function([var_5873], output)
mutated_mod['func_5874'] = func_5874
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5899 = relay.var("var_5899", dtype = "float32", shape = (6, 8, 12))#candidate|5899|(6, 8, 12)|var|float32
uop_5900 = relay.sinh(var_5899.astype('float32')) # shape=(6, 8, 12)
uop_5903 = relay.rsqrt(uop_5900.astype('float32')) # shape=(6, 8, 12)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_5906 = relay.TupleGetItem(func_3534_call(), 2)
call_5907 = relay.TupleGetItem(func_3536_call(), 2)
bop_5912 = relay.greater_equal(uop_5903.astype('bool'), relay.reshape(uop_5900.astype('bool'), relay.shape_of(uop_5903))) # shape=(6, 8, 12)
func_4771_call = mod.get_global_var('func_4771')
func_4773_call = mutated_mod.get_global_var('func_4773')
var_5920 = relay.var("var_5920", dtype = "uint8", shape = ())#candidate|5920|()|var|uint8
call_5919 = relay.TupleGetItem(func_4771_call(relay.reshape(var_5920.astype('uint8'), [])), 3)
call_5921 = relay.TupleGetItem(func_4773_call(relay.reshape(var_5920.astype('uint8'), [])), 3)
func_5017_call = mod.get_global_var('func_5017')
func_5020_call = mutated_mod.get_global_var('func_5020')
const_5928 = relay.const([-9.866481,-1.980893,-3.776156,0.500139,-5.672127,2.610219,1.412445,3.273655,6.137303,-3.596131,-8.585606,-3.410400,-9.298353,-1.128307,1.913632,6.313234,-4.809317,1.892562,3.598451,-1.307890,-9.395122,-5.262900,-8.950077,-6.542639,-2.559292,8.124457,-6.409726,0.151359,8.370083,-4.365210,1.115151,3.548814,2.327601,4.221334,1.264059,-4.129698,2.451685,4.291092,-6.113768,5.716365,-3.100623,6.501582,-1.395036,8.077549,-1.009388,4.699714,9.328651,-9.654649,6.676934,-1.269149,7.634903,-2.708776,4.133907,0.062692,6.369079,-9.898975,1.585221,-2.621146,6.258833,5.444721,6.150589,2.486378,1.387480,1.455565,0.589230,5.313623,-8.239139,-2.814348,0.442999,1.748310,-3.240181,-3.024126,-8.013763,-1.934314,0.319211,4.144759,-5.241914,1.997576,-6.840940,-7.236028,-0.373164,6.035725,-0.835451,1.071190,1.356088,-5.930904,-3.166835,7.359006,-5.238213,-7.945794,9.340971,-2.544607,0.505045,-5.394641,7.611265,6.395177,-4.813875,-0.046646,-7.881277,4.169059,9.823788,-1.049385,-5.173116,-1.054588,3.585388,-4.043040,-8.871411,-4.357096,3.020398,-7.151260,7.670216,-7.468734,-0.604934,-9.232934,-1.937995,-4.675577,-2.735833,-0.624507,-1.496059,6.751047,4.419473,-7.333227,-3.547034,3.626312,8.946105,-1.964742,-1.638189,7.254383,-2.381878,6.352612,2.004520,-9.605732,-6.291667,-9.242367,4.297957,-6.323091,-1.594090,-6.347761,1.797445,-2.149899,9.744313,-0.552643,8.834770,-8.307340,7.669097,0.744706,7.097440,-4.863869,-5.651039,-5.571610,-9.192767,-0.346787,-0.361090,-9.647714,8.985182,-7.783798,1.728691,-1.055128,-8.739839,-4.310968,-2.003431,-3.253174,3.249404,-6.725870,-2.415331,1.116414,8.940200,0.558850,9.280632,-9.669728,-3.511492,7.053552,8.213226,-5.637793,3.252896,7.670674,-9.983475,8.377799,7.317713,3.728682,5.363873,-0.262388,4.628799,-9.326451,0.388979,1.128607,8.846908,-7.676894,-7.513392,4.974369,2.043548,1.899467,-0.493464,-5.279206,-0.959724,2.696590,-3.799740,5.354287,6.319491,-3.569676,-3.563853,-3.990590,1.789473,-6.696686,-2.900525,9.615460,-5.929263,0.053359,2.444481,-8.662324,-3.067832,0.406696,-5.947706,-5.638014,-2.787847,-5.401137,-4.746957,9.910685,7.393086,2.234522,3.294494,-1.991526,7.076278,-7.046947,0.537482,4.353128,4.196855,-3.787705,0.332194,3.022396,-6.266024,-9.016551,4.134840,-8.805598], dtype = "float32")#candidate|5928|(234,)|const|float32
const_5929 = relay.const([-2.444277,-4.048697,-4.654645,-3.008507,-3.734538,9.275333,2.809463,7.118375,-3.436871,-2.951342,-8.489570,6.181350,-4.640686,6.566580,0.659198,-2.415136,-1.293529,-9.192249,-2.868802,-8.373963,-5.060903,-3.349571,2.352578,-9.498172,-1.345530,-1.170973,4.311524,-0.258421,5.724561,1.105947,9.464356,-9.321414,-1.183607,3.732444,-9.954392,9.132264,7.439288,-7.790148,2.995507,5.827464,8.023081,8.509123,2.028160,5.227609,1.610720,-4.312254,-6.523824,-7.675149,0.580199,5.862891,0.788074,-3.594034,-8.191083,9.660254,6.102243,-6.450667,1.237171,2.727628,3.879688,1.743667,6.964354,-9.136308,4.501606,-9.620241,-9.635222,-2.313103,9.721614,-5.486277,7.850599,0.201617,-4.599323,1.036748,5.304505,9.232223,7.968918,4.125836,-8.766085,0.937274,-2.820913,-2.533171,0.842690,-4.460877,1.387390,3.631974,8.078111,7.440574,-0.034441,8.054330], dtype = "float64")#candidate|5929|(88,)|const|float64
call_5927 = relay.TupleGetItem(func_5017_call(relay.reshape(const_5928.astype('float32'), [234,]), relay.reshape(const_5929.astype('float64'), [88,]), ), 4)
call_5930 = relay.TupleGetItem(func_5020_call(relay.reshape(const_5928.astype('float32'), [234,]), relay.reshape(const_5929.astype('float64'), [88,]), ), 4)
output = relay.Tuple([call_5906,bop_5912,call_5919,var_5920,call_5927,const_5928,const_5929,])
output2 = relay.Tuple([call_5907,bop_5912,call_5921,var_5920,call_5930,const_5928,const_5929,])
func_5938 = relay.Function([var_5899,var_5920,], output)
mod['func_5938'] = func_5938
mod = relay.transform.InferType()(mod)
mutated_mod['func_5938'] = func_5938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5938_call = mutated_mod.get_global_var('func_5938')
var_5940 = relay.var("var_5940", dtype = "float32", shape = (6, 8, 12))#candidate|5940|(6, 8, 12)|var|float32
var_5941 = relay.var("var_5941", dtype = "uint8", shape = ())#candidate|5941|()|var|uint8
call_5939 = func_5938_call(var_5940,var_5941,)
output = call_5939
func_5942 = relay.Function([var_5940,var_5941,], output)
mutated_mod['func_5942'] = func_5942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3351_call = mod.get_global_var('func_3351')
func_3352_call = mutated_mod.get_global_var('func_3352')
call_5979 = func_3351_call()
call_5980 = func_3351_call()
output = call_5979
output2 = call_5980
func_5981 = relay.Function([], output)
mod['func_5981'] = func_5981
mod = relay.transform.InferType()(mod)
output = func_5981()
func_5982 = relay.Function([], output)
mutated_mod['func_5982'] = func_5982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3580_call = mod.get_global_var('func_3580')
func_3581_call = mutated_mod.get_global_var('func_3581')
call_6006 = relay.TupleGetItem(func_3580_call(), 0)
call_6007 = relay.TupleGetItem(func_3581_call(), 0)
func_3833_call = mod.get_global_var('func_3833')
func_3835_call = mutated_mod.get_global_var('func_3835')
call_6029 = relay.TupleGetItem(func_3833_call(), 2)
call_6030 = relay.TupleGetItem(func_3835_call(), 2)
func_1798_call = mod.get_global_var('func_1798')
func_1802_call = mutated_mod.get_global_var('func_1802')
var_6033 = relay.var("var_6033", dtype = "uint16", shape = (945,))#candidate|6033|(945,)|var|uint16
call_6032 = func_1798_call(relay.reshape(var_6033.astype('uint16'), [7, 9, 15]), relay.reshape(var_6033.astype('uint16'), [7, 9, 15]), )
call_6034 = func_1798_call(relay.reshape(var_6033.astype('uint16'), [7, 9, 15]), relay.reshape(var_6033.astype('uint16'), [7, 9, 15]), )
var_6043 = relay.var("var_6043", dtype = "uint8", shape = (9, 9, 15))#candidate|6043|(9, 9, 15)|var|uint8
bop_6044 = relay.less_equal(call_6029.astype('bool'), relay.reshape(var_6043.astype('bool'), relay.shape_of(call_6029))) # shape=(9, 9, 15)
bop_6047 = relay.less_equal(call_6030.astype('bool'), relay.reshape(var_6043.astype('bool'), relay.shape_of(call_6030))) # shape=(9, 9, 15)
func_4378_call = mod.get_global_var('func_4378')
func_4379_call = mutated_mod.get_global_var('func_4379')
call_6052 = relay.TupleGetItem(func_4378_call(), 0)
call_6053 = relay.TupleGetItem(func_4379_call(), 0)
uop_6056 = relay.rsqrt(call_6029.astype('float32')) # shape=(9, 9, 15)
uop_6058 = relay.rsqrt(call_6030.astype('float32')) # shape=(9, 9, 15)
func_5638_call = mod.get_global_var('func_5638')
func_5640_call = mutated_mod.get_global_var('func_5640')
call_6062 = relay.TupleGetItem(func_5638_call(), 0)
call_6063 = relay.TupleGetItem(func_5640_call(), 0)
output = relay.Tuple([call_6006,call_6032,var_6033,bop_6044,call_6052,uop_6056,call_6062,])
output2 = relay.Tuple([call_6007,call_6034,var_6033,bop_6047,call_6053,uop_6058,call_6063,])
func_6071 = relay.Function([var_6033,var_6043,], output)
mod['func_6071'] = func_6071
mod = relay.transform.InferType()(mod)
mutated_mod['func_6071'] = func_6071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6071_call = mutated_mod.get_global_var('func_6071')
var_6073 = relay.var("var_6073", dtype = "uint16", shape = (945,))#candidate|6073|(945,)|var|uint16
var_6074 = relay.var("var_6074", dtype = "uint8", shape = (9, 9, 15))#candidate|6074|(9, 9, 15)|var|uint8
call_6072 = func_6071_call(var_6073,var_6074,)
output = call_6072
func_6075 = relay.Function([var_6073,var_6074,], output)
mutated_mod['func_6075'] = func_6075
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6083 = relay.var("var_6083", dtype = "uint64", shape = (13, 5, 6))#candidate|6083|(13, 5, 6)|var|uint64
var_6084 = relay.var("var_6084", dtype = "uint64", shape = (13, 5, 6))#candidate|6084|(13, 5, 6)|var|uint64
bop_6085 = relay.logical_xor(var_6083.astype('uint64'), relay.reshape(var_6084.astype('uint64'), relay.shape_of(var_6083))) # shape=(13, 5, 6)
output = relay.Tuple([bop_6085,])
output2 = relay.Tuple([bop_6085,])
func_6095 = relay.Function([var_6083,var_6084,], output)
mod['func_6095'] = func_6095
mod = relay.transform.InferType()(mod)
var_6096 = relay.var("var_6096", dtype = "uint64", shape = (13, 5, 6))#candidate|6096|(13, 5, 6)|var|uint64
var_6097 = relay.var("var_6097", dtype = "uint64", shape = (13, 5, 6))#candidate|6097|(13, 5, 6)|var|uint64
output = func_6095(var_6096,var_6097,)
func_6098 = relay.Function([var_6096,var_6097,], output)
mutated_mod['func_6098'] = func_6098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5521_call = mod.get_global_var('func_5521')
func_5522_call = mutated_mod.get_global_var('func_5522')
call_6103 = func_5521_call()
call_6104 = func_5521_call()
output = call_6103
output2 = call_6104
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
func_5333_call = mod.get_global_var('func_5333')
func_5335_call = mutated_mod.get_global_var('func_5335')
call_6136 = relay.TupleGetItem(func_5333_call(), 0)
call_6137 = relay.TupleGetItem(func_5335_call(), 0)
const_6171 = relay.const([[[-6.113115,-9.712815,-8.318778,0.248517,0.003111],[-8.893058,1.255437,8.556393,5.596939,9.277799],[-9.760991,7.898226,-6.534520,-7.578352,-2.608262],[9.668982,-0.834964,-4.375404,2.164876,-4.351971],[-8.406149,-5.356397,-8.336460,8.948497,-0.595007],[8.178647,6.859999,8.805834,0.282484,-2.444335],[-7.669902,-5.069332,1.648806,0.652444,-9.912765],[2.710341,-2.939248,0.836158,1.057123,-6.393519],[8.097598,0.548524,4.342871,-5.254629,-8.738655],[-6.761729,-5.777659,7.997414,7.544255,-2.256377],[-9.221729,-1.723269,7.679512,8.817877,9.321218],[-1.924764,7.062436,6.752432,-6.418082,1.945900],[-3.390225,3.758124,5.249715,-6.124817,6.961384]],[[-7.883668,-2.295086,4.749212,-2.246026,-3.371352],[-1.631607,-9.373905,-7.714072,-5.829111,0.499204],[8.999489,1.170896,-1.065391,7.127745,-5.304558],[2.168215,3.469708,6.454006,2.614793,5.509021],[3.240300,-9.832199,-5.589624,0.901018,-6.529485],[-9.093423,-0.192504,-6.196670,-2.099794,6.508623],[5.463257,-0.173501,-3.283151,8.890429,5.555607],[-8.698900,-1.202431,6.882641,5.049738,-0.610619],[7.154952,-5.483288,-6.457319,0.246819,-3.745011],[5.999843,3.882144,-0.985957,-8.350613,-5.374117],[8.042503,-6.829453,9.367266,-3.595909,0.325619],[-5.355422,5.933359,-8.332897,-4.065243,9.627753],[8.760460,-4.537860,-9.482121,-6.151185,-1.325539]]], dtype = "float32")#candidate|6171|(2, 13, 5)|const|float32
bop_6172 = relay.logical_or(call_6136.astype('bool'), relay.reshape(const_6171.astype('bool'), relay.shape_of(call_6136))) # shape=(2, 13, 5)
bop_6175 = relay.logical_or(call_6137.astype('bool'), relay.reshape(const_6171.astype('bool'), relay.shape_of(call_6137))) # shape=(2, 13, 5)
func_3786_call = mod.get_global_var('func_3786')
func_3788_call = mutated_mod.get_global_var('func_3788')
call_6182 = relay.TupleGetItem(func_3786_call(), 0)
call_6183 = relay.TupleGetItem(func_3788_call(), 0)
output = relay.Tuple([bop_6172,call_6182,])
output2 = relay.Tuple([bop_6175,call_6183,])
func_6185 = relay.Function([], output)
mod['func_6185'] = func_6185
mod = relay.transform.InferType()(mod)
mutated_mod['func_6185'] = func_6185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6185_call = mutated_mod.get_global_var('func_6185')
call_6186 = func_6185_call()
output = call_6186
func_6187 = relay.Function([], output)
mutated_mod['func_6187'] = func_6187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6185_call = mod.get_global_var('func_6185')
func_6187_call = mutated_mod.get_global_var('func_6187')
call_6193 = relay.TupleGetItem(func_6185_call(), 0)
call_6194 = relay.TupleGetItem(func_6187_call(), 0)
output = relay.Tuple([call_6193,])
output2 = relay.Tuple([call_6194,])
func_6195 = relay.Function([], output)
mod['func_6195'] = func_6195
mod = relay.transform.InferType()(mod)
output = func_6195()
func_6196 = relay.Function([], output)
mutated_mod['func_6196'] = func_6196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4517_call = mod.get_global_var('func_4517')
func_4518_call = mutated_mod.get_global_var('func_4518')
call_6197 = relay.TupleGetItem(func_4517_call(), 0)
call_6198 = relay.TupleGetItem(func_4518_call(), 0)
func_5872_call = mod.get_global_var('func_5872')
func_5874_call = mutated_mod.get_global_var('func_5874')
const_6212 = relay.const([-9.783726,-8.846701,-6.729269,-6.838266,2.249819,-0.142546,9.492071,8.258740,8.574057,2.818678,-6.117215,2.598975,-8.283122,-0.608593,9.300892,7.036750,7.879299,-2.082159,-9.868479,7.945130,-5.110933,-7.394361,5.838525,-6.162957,-8.288754,-3.865690,-1.058655,-7.756151,-5.157808,-2.075166,-1.759958,3.579342,-3.573659,3.412307,-1.453396,-6.220565,-1.171709,4.208669,-1.734935,-1.651057,5.832663,-3.287971,-5.949354,-6.519075,2.731695,1.463027,-2.942963,-3.466579,-9.652397,-0.289406,-7.243723,5.885485,0.222993,2.760308,-0.268067,-0.510300,-5.281142,0.275245,-1.356186,4.637785,1.015249,4.202024,-9.854068,-0.170945,7.519994,8.976971,5.979533,-6.545648,5.885125,-9.615604,-3.959427,-8.680556,4.876968,1.224679,1.147537,-1.674206,6.084318,5.311815,1.765919,1.089435,-8.759430,-7.999940,9.376899,-3.448684,-4.842370,3.572512,-9.766364,7.948219,3.536879,8.885879,-6.852627,7.181296,5.884755,8.930557,-3.966158,1.672850,7.270817,-6.441092,-5.300813,-7.137293,-6.414162,0.373293,7.305587,-6.660352,-1.002590,5.350066,3.289351,-3.778719,3.148852,5.022849,-4.710719,-6.101991,4.016040,7.756735,-0.254201,-7.191707,7.657595,5.891611,2.609730,0.608121,8.410160,-4.309261,-3.087446,6.389412,-8.354401,3.101636,6.453958,-0.986242,4.516907,-9.564512,8.969396,-5.400081,0.152362,2.256917,2.628507,-7.604475,-5.241018,-7.683873,5.178449,-8.664824,-9.254500,5.847497,-3.897661,-1.427394,9.531589,1.629874,-8.612832,4.001374,9.170984,-7.589288,4.180557,5.317476,3.624908,-7.411279,0.713591,-6.503646,7.767478,1.456270,4.610762,0.874001,-3.611094,-0.342608,-5.881928,-1.471537,-7.908992,-4.383139,9.347133,7.242074,8.850250,-3.161884,9.084993,1.919240,-7.135839,-5.517163,-7.596434,-5.483145,-5.153211,6.394095,-4.249920,-5.822976,-8.089106,-7.802578,-0.071396,-3.470213,-9.585746,-9.214188,1.980057,-5.959712,-5.451316,-8.373862,-6.845655,8.444022,1.588667,1.845856,5.645075,-5.908531,-7.446232,7.567391,4.657048,5.199180,-2.414185,6.819728,6.359587,1.411366,-8.179811,-4.557130,-8.867776,6.772111,5.797195,8.922057,-5.758677,-3.242077,7.785208,9.741274,-8.930499,-7.158514,-3.174871,-9.660465,9.725039,0.752176,1.145207,-3.011896,7.631435,2.955412,-4.373273,6.517029,9.351452,6.643423,-0.461797,2.399333,1.894708,8.433435,4.895933,3.528496,-9.633343,-3.538867,2.190124,8.836960,-4.380815,4.802473,-1.615272,2.783890,-1.238487,-0.473864,5.086570,5.536447,5.266257,-1.567582,7.339865,8.414831,-4.970695,5.467893,-9.977288,-4.632110,-1.241540,1.231231,2.343645,-6.338221,2.623138,-0.535093,-7.272227,-7.918664,-9.680387,-6.678451,-4.943309,4.579890,4.775109,-1.827930,-0.121920,-0.583217,-4.397368,8.007303,-3.528527,-1.377518,-3.557162,-6.014307,-2.268508,-9.310994,2.545725,-0.025911,-4.580719,-5.669334,6.062700,3.132913,7.913299,-8.869155,9.693116,2.757661,4.335813,8.531829,-2.223779,-7.469080,-1.367330,-2.790325,0.172753,-8.905580,-2.123566,6.393290,1.764269,1.838888,-7.643041,1.052305,4.728849,6.008168,-4.097486,-5.116301,-8.326933,9.415716,8.110614,-8.536171,9.326076,-7.748754,4.995441,8.100950,-3.673373,2.317942,-6.608044,-3.669154,-7.035096,-6.790627,0.407389,6.223875,4.899632,-5.883592,-8.695219,5.898137,5.977612,-0.753649,0.929008,-4.855951,-3.236018,-5.563156,-0.679935,8.648692,-2.009665,7.081646,-5.907672,1.025369,9.910640,0.384902,-4.787824,2.930533,-4.619141,-5.984347,5.664054,-1.035163,-2.763262,-8.772884,6.968843,5.225230,9.959427,1.581276,-0.343761,0.792048,4.120602,2.571249,8.579455,3.147332,-6.945024,3.249640,-1.655786,-6.280317,-0.193490,0.225919,-0.941374,9.304285,6.452437,6.350425,0.546520,-8.153546,8.684721,-4.696086,-4.286622,0.330845,7.392930,4.606630,-7.381977,8.654659,-5.951071,-0.557689,8.619175,9.817063,6.853909,-4.469617,4.616089,9.721390,3.334221,-0.058909,2.361758,-4.198702,-8.916836,4.972702,1.179046,-6.344923,9.485669,-2.038245,-5.314853,-5.546102,5.714218,5.625850,5.643515,0.976395,-9.455101,-1.169909,1.823651,8.085570,-6.056739,-1.941201,9.208926,-8.752927,-7.391099,7.190437,-0.426745,-6.245313,5.547193,-6.566848,-1.574135,1.301245,9.874471,-8.798619,-0.924098,2.036297,-6.120374,6.041869,-3.894941,7.642102,-0.126045,1.591654,-5.195160,-3.131570,0.795790,-3.956159,2.448556,1.392288,5.023540,6.382672,2.627786,8.824025,3.931149,6.802439,-2.683980,-6.663262,2.701400,6.626177,1.592480,7.266183,-4.281953,-3.210829,6.432375,6.142473,0.135314,4.401476,5.573438,9.480290,9.774415,-7.896052,7.676621,-5.243305,-9.253643,-8.563711,-3.242874,8.792523,0.520002,-5.713424,7.523595,5.865800,-9.073788,5.064351,6.774447,-7.368426,1.228808,-7.083048,6.245620,3.710195,-3.135104,2.562330,-6.396118,-8.239284,-8.232536,-6.627312,-0.679523,5.045218,-2.090245,-5.020729,7.956078,-6.914273,3.258567,2.076927,-1.826470,-2.405618,-8.364776,7.484758,-2.228884,-9.333185,-3.738192,-4.912003,-4.266814,7.565460,-8.618904,0.230505,0.609997,-3.381406,-8.922248,6.721081,8.094990,-8.585668,-0.334079,-1.695214,9.152129,3.039165,3.599898,-3.410265,3.450423,4.016832,4.845087,4.868701,-6.345765,5.538187,9.986287,4.863346,-0.657418,-5.791001,5.404198,-2.393931,7.491861,-7.961839,5.434973,7.917355,4.236001,9.662349,0.331048,2.122437,-4.759493,-0.868196,3.817342,-5.694819,7.815454,-2.529867,3.226556,8.980937,4.188567,-7.121199,-8.466163,1.215642,-4.382448,-5.323026,-7.939291,2.771588,-8.356563,-1.611199,-0.457147,-2.772989,-5.420078,-6.864031,5.807721,-5.332228,-2.084502,8.023720,-1.639737,-1.948529,5.932485,-3.241926,-8.255623,2.993910,-0.395397,-6.367771,-1.970457,-5.243612,-2.928293,7.150681,2.842599,-5.057238,-8.991008,-4.919144,-9.475586,6.128830,-8.530914,2.852643,8.376304,0.820843,0.594273,-2.542631,-6.272925,-4.981439,-3.061078,-7.868421,6.085715,4.787047,0.244006,9.498567,-8.037501,4.534881,-6.406394,9.075021,1.962036,0.297283,-3.838133,4.018459,5.909022,5.883366,5.519333,9.742574,-2.211247,-9.384800,-6.937777,-3.870760,-6.530587,8.038409,-7.239564,-1.449597,-5.431207,-8.582017,-1.845348,6.130517,2.557732,8.585444,2.758157,-9.283413,0.278304,8.154801,-8.055487,-0.015834,4.963135,8.018430,-5.852226,-4.946857,-0.973574,5.389130,-0.189343,-3.174264,-1.186106,-4.367941,-6.169997,0.046342,7.743955,7.680800,-0.088386,-9.638384,-9.910972,-9.668331,5.498877,0.551354,6.875562,-6.098436,0.633500,-1.070492,-0.255411,7.219460,4.547908,-3.939556,9.340424,-5.800004,8.980976,-9.591512,-8.042270,-8.621807,5.668905,1.382510,1.086618,-9.157770,-9.642714,-4.757824,6.163758,4.495579,-0.721723,5.715540,-1.018859,-7.997116,-9.417518,2.201906,1.222882,-2.582224,4.727399,9.298148,-0.601492,8.946633,-1.109242,7.799427,-2.052163,-5.272132,4.908600,-2.818312,5.977654,4.156593,7.958362,6.794255,2.938212,4.379906,5.185029,1.364600,-2.156441,3.480417,-2.429286,-9.798520,4.676848,6.318023,-2.199626,-5.938739,-9.215759,3.898398,-5.149553,-3.052635,3.918737,-8.990242,6.149308,-8.067569,9.827298,-2.082580,-4.510833,-8.642865,-9.367523,-0.476445,8.960494,-9.716810,1.054277,-1.865862,-2.429959,6.310940,-1.226361,3.453044,2.394909,-4.883195,8.365181,-7.316125,7.201738,9.884909,-4.494532,7.201848,9.065494,-3.694110,1.290122,-7.909208,2.816310,3.646965,-3.374366,3.156272,-4.763081,-7.849940,7.130881,-8.430325,1.069941,-2.987200,1.175503,2.052708,6.900211,8.307806,-2.235233,1.297118,8.761877,-5.420762,3.748759,0.281462,8.176584,8.506078,-1.227815,6.012700,3.810214,-9.036692,7.792853,7.024186,7.727095,-1.525993,2.394555,4.321368,-1.840811,-2.210616,-2.386545,-0.058491,4.492849,-7.155512,2.086567,7.011738,2.884367,1.311346,6.160623,2.002712,-8.300702,5.122811,1.047315,-1.156547,-9.845014,1.333612,1.982587,-3.295872,5.778613,-9.405407,-2.508861,-0.546224,6.021866,0.992495,-9.481542,0.099351,-9.299470,-6.458677,-4.707543,5.259858,9.662618,8.719354,-8.620825,8.625747,-4.134807,-1.363485,7.976438,-3.872877,7.639563,-3.238311,-1.901227,-1.589994,-1.439035,9.165645,9.584639,0.318233,6.057151,0.861517,-2.870268,-2.258705,4.421259,1.995915,3.638811,6.417738,1.491175,-2.675425,-9.360054,-3.051792,-1.414803,5.970872,4.190198,-3.476401,9.931330,-0.512117,6.003711,-4.159667,-5.769889,1.916839,0.976703,-1.260305,-9.110193,-5.289155,0.059795,7.427758,-2.731598,4.622010,1.870551,9.859860,-7.520113,-3.291470,-4.351354,-8.482454,4.359697,-8.247520,-7.492021,1.558995,2.387936,1.834293,5.398853,-5.595293,5.106831,7.830149,-1.173048,6.315085,-7.614851,-1.406017,-4.036807,0.068618,-7.860295,-0.668642,-3.805785,-6.655786,-0.183184,-1.657865,-2.957819,4.208273,0.598759,2.672793,6.200950,-6.961335,-9.518337,-6.220539,8.377337,-3.378202,6.470910,-8.608605,9.201182,-7.366733,5.778399,4.187160,3.459086,3.029811,2.009763,-5.763109,-3.835252,-1.461682,3.636977,0.104282,5.750641,4.338873,7.038680,-0.835672,-9.726229,-8.398403,-8.155508,9.476165,-9.128781,-6.474031,7.710317,1.685655,6.536534,0.155077,-3.945223,4.581344,-1.727048,0.632011,-0.300389,-0.156777,-8.896468,-9.005162,-3.316988,-2.575222,0.887502,-4.531855,-2.857155,-3.897455,-2.025174,-1.947138,-6.516606,-4.173131,-9.431881,-1.546574,0.654247,3.973607,5.060476,-4.875004,-1.994186,1.039612,2.341237,-8.301061,0.636388,3.171465,-1.187762,-5.155122,5.506787,-0.958844,-9.156453,8.814925,5.619542,9.702152,-3.342493,3.540608,3.785427,-0.328143,-7.526945,-8.348062,7.051118,7.253536,5.037517,6.401324,-2.366853,5.186103,-5.876233,8.978891,3.177294,1.392272,-4.800679,-3.074067,9.597690,4.137911,-1.672845,8.802784,0.931954,2.807062,-8.614352,-3.255910,-2.724048,-1.919451,-5.685023,5.423592,-5.246222,1.564753,6.447888,-5.809257,3.779344,-0.063125,0.204023,9.685270,4.649739,-4.100500,3.935750,-5.628090,-1.265081,8.014002,-6.396713,-2.552437,6.703527,-5.712615,-5.911468,0.527425,-2.987859,1.066239,8.934871,-3.802049,9.073525,-3.696469,3.639928,3.586931,0.035740,-9.094367,6.507504,8.602674,6.170659,9.332446,-5.718270,4.190326,-4.604232,2.746541,4.442997,-8.821465,-5.994110,-2.110405,-8.652689,3.998863,-3.331652,6.350601,-7.360874,-2.603722,-6.562270,8.157300,-6.392093,4.208316,6.059966,-5.664317,1.819454,-8.080785,6.403663,0.954092,-9.840372,-5.260106,8.528398,-9.323188,-5.599038,2.327078,-2.570966,8.676821,6.895249,6.385992,3.475250,5.141178,6.836922,-1.750198,-1.906004,-8.427172,-5.059914,2.580249,-1.815174,-9.499820,-9.911190,-5.887108,-2.417613,4.616550,-4.495772,8.854435,-2.241624,-6.809754,-4.678170,8.000050,9.560751,1.325668,-3.668618,3.218007,-3.130092,5.083531,1.530667,9.013227,3.709100,7.998199,8.558214,-8.984658,3.164288,9.665595,9.625659,3.614942,-3.112316,5.908968,0.379160,-5.130011,-1.019868,9.638648,3.406504,5.491364,2.681720,-0.370061,6.957928,1.942007,-8.215261,-1.203680,4.113429,-5.753914,-3.108741,-7.969484,-7.165038,7.796614,-3.129187,-3.072234,5.118861,-7.236539,-1.921744,-0.956536,1.024205,-2.099207,-0.401239,-2.146050,-1.141625,-5.728867,-9.665532,7.890822,7.450042,0.262719,8.053890,3.475584,7.311764,4.457990,-2.040664,-9.459832,5.234670,3.722167,7.979293,7.769894,-5.907101,8.136572,-7.465998,5.879671,2.916679,7.207482,-5.881846,-9.062937,5.653120,6.180330,7.570847,7.702734,2.420562,-2.203645,-5.358499,-6.983884,9.514501,1.970108,-2.032100,5.709416,9.054075,-1.069697,0.521254,-2.558862,0.944192,4.596250,5.470129,2.368276,6.644016,1.596972,-7.195708,2.664266,2.267181,2.835377,1.357793,-5.389852,-6.525373,6.437971,6.859004,-1.048185,2.493877,6.333526,-9.587295,8.014092,-2.251223,-0.864653,4.542483,8.350157,-2.999062,-7.751593,9.536061,0.107908,-4.049339,-7.800357,-4.127677,-4.790050,-8.842728,-0.859430,-5.642130,-8.766273,-8.065025,2.022120,-2.758389,3.236314,-0.605156,6.411065,-1.670212,4.296280,2.597396,-4.441865,-6.799276,7.442102,-5.604745,1.419482,-1.082035,7.524084,-8.989930,-5.198659,8.839664,-4.150343,3.898324,-5.269446,-2.881440,-4.506335,7.993551,6.788631,5.753324,-7.825386,-4.451241,9.132803,8.274298,7.240817,3.574640,4.129927,0.308206,-2.142380,8.160110,-9.033063,-3.416731,8.231892,2.948959,5.166175,1.203723,-6.126299,-8.219013,-8.520950,1.755394,0.598122,3.244583,7.338368,-7.883930,-9.710701,-7.614231,9.745465,2.288060,-1.677260,8.785219,-7.096962,5.340666,-8.941245,-1.562385,-8.145698,0.818495,-5.758978,-0.417332,8.296458,-5.201547,-9.565854,3.111480,0.045016,-8.426042,3.344388,-4.302635,-9.416817,8.446690,6.578886,-7.554632,0.059448,8.653280,-5.972958,3.376596,0.534512,5.200002,5.297674,7.877923,-8.710641,-1.885796,-6.692256,6.225167,4.491762,6.546518,-5.345225,-7.595141,6.367039,7.173412,7.862177,-3.973425,-3.564280,-3.566262,-5.137100,9.675447,1.509633,-3.839650,-0.964307,-9.709011,-6.809710,-2.143049,2.138105,-1.105329,-2.062723,6.627383,4.957870,-9.989746,2.326932,0.369116,4.490661,-8.735285,-4.241677,-0.343972,-3.122147,-1.437424,-5.365621,5.340452,2.303761,8.850329,-0.658473,7.804462,-8.724273,0.404600,-6.184329,1.532798,9.959883,-2.178896,-7.809604,-8.556201,-0.877940,-1.652519,7.148666,-8.204637,5.500239,3.802505,-2.157788,3.394042,-0.417441,6.060735,2.610791,-7.090913,-4.417525,4.336712,1.739173,-2.906121,-7.688769,2.451239,-3.358037,6.944252,3.717051,6.122051,9.913487,-8.151959,-2.627500,0.271541,-8.389283,-4.086043,-8.144741,9.506689,-6.911246,5.447098,-4.609048,-0.635454,2.990391,5.708863,-1.496591,-5.113752,6.905444,-2.978014,-3.292037,-9.474616,8.157259,-4.194794,-4.180247,-4.714829,9.643393,9.539953,-9.390424,-5.331071,5.112221,-4.194699,8.184008,-3.256307,8.146131,-2.895267,-8.087652,-6.471464,3.671839,1.031686,-0.653573,-2.610391,-1.416116,-5.618870,-3.277057,-8.427402,-7.916125,1.859814,5.817399,-6.599612,-7.553933,8.949651,0.382021,2.840216,-6.974785,-9.514240,-9.293610,-7.587923,6.871144,8.970084,7.358909,4.324225,-2.781992,9.049738,-2.970139,-0.436520,-9.062051,2.267281,1.503225,0.202261,-1.511424,-6.790239,-7.115375,3.786036,0.281285,0.064940,-1.726440,-1.517217,-2.768699,-5.840066,-5.085005,9.202832,-6.833546,-8.537128,0.581167,6.334275,-7.648066,-4.303163,-4.952614,-9.120060,-3.324045,9.661084,-5.002184,5.395258,5.347147,-2.431129,-9.328969,0.072646,-9.757596,-7.913407,1.749102,6.307249,-7.813023,-1.969763,3.316008,-3.191474,1.907826,-1.691868,-0.361670,-4.595518,-5.897316,6.047737,-9.763332,2.659356,-8.510782,1.427260,-9.539048,2.993164,-0.080978,9.535208,-3.716204,-1.316984,8.830724,-7.721707,-7.128565,-2.996312,9.401552,-7.008508,-5.090622,-2.842482,8.956074,-1.653936,9.821401,-5.736330,7.096514,1.905117,-3.535435,7.642468,0.623417,7.399191,-2.961563,-5.807157,6.248385,-3.174575,-6.232003,-5.428394,-3.582285,2.777179,3.350436,1.313239,-6.947038,-6.507326,-1.156389,-0.851196,2.919897,-5.676744,2.406526,7.001391,9.869607,-6.232987,7.127138,8.149778,8.379071,3.662064,5.965555,-5.678823,4.046531,-5.361204,-9.923127,4.634477,-9.242119,-9.101938,-9.606389,-4.548884,1.288316,-1.016718,7.929621,-7.297244,-5.202563,4.825347,-5.072827,2.596642,2.554195,-7.319797,9.866858,0.273605,1.066552,2.205117,-1.928745,5.821860,1.449436,-4.814705,5.908901,2.926123,-8.633115,9.161376,-6.598301,-3.303009,-8.779930,-7.180858,6.596627,0.104339,5.865733,-1.084034,-7.176512,1.041943,1.275704,3.246591,-4.433158,5.710772,1.210278,6.327104,6.448191,6.415538,-5.721479,7.595531,-2.652082,-9.103872,-7.132118,4.578183,-3.291325,-9.908186,-6.783542,7.637367,-1.151272,5.893763,3.258201,-5.214981,-7.179390,5.461910,2.066343,-4.418732,0.436141,1.825463,-6.215776,4.068659,7.847817,-5.479704,1.145197,-4.927216,-7.509996,5.152184,-0.322764,9.247297,-2.493444,-6.079510,6.291499,7.143996,4.444494,-3.194572,5.964951,1.037202,6.072825,-9.071078,1.277804,0.319335,-6.598691,2.871768,-5.695012,2.753137,2.883417,-4.199634,7.768047,-8.199670,-6.577214,-6.860708,-8.591858,-1.874956,3.146500,-9.900517,6.730339,9.808494,-4.585272,-2.686443,9.884146,1.264634,1.911711,9.169418,8.584096,-2.457610,5.550639,2.412036,-7.049098,4.895311,-3.874008,-7.318644,1.212213,0.346526,-8.367379,-9.898898,-9.999396,0.844547,9.181270,-2.518194,-7.414829,-8.773531,7.053696,7.866858,5.542657,4.493856,-5.539362,8.676290,2.977643,4.372128,3.365807,7.015258,-5.027381,9.483506,-0.298159,-4.967249,-5.158900,-6.106575,7.618260,4.711837,-1.944604,-3.759470,-4.410640,8.151573,7.264801,-8.787498,-7.633598,-7.799731,-3.539568,5.873610,6.042191,2.648768,-5.990461,4.451983,6.144612,3.848895,0.189843,-2.851401,0.280736,-0.197503,-9.554927,2.780135,-7.609740,8.558622,-3.431373,2.536496,0.302888,7.061111,-7.474374,4.404954,-4.094348,-0.555277,-4.907884,8.428240,-6.875210,-6.971335,-9.316111,7.924135,9.301615,9.617623,8.507582,2.379455,1.122541,5.492915,7.721135,3.756822,6.979151,-6.158391,-7.931313,2.943509,7.067569,-0.978353,-7.697232,-8.642602,-4.217710,0.798003,4.967485,-6.598173,5.114739,-7.256717,-5.186225,-3.581418,0.189904,-6.175926,3.493419,-7.987342,9.566415,-0.167936,7.727647,-9.876556,8.867967,2.307361,-8.009601,2.687523,1.517273,0.953398,-1.774849,5.014367,-5.406182,3.451200,-2.516295,-3.943627,-9.452045,5.375025,2.193793,-0.167503,4.035756,9.669128,5.278016,2.041634,0.364760,5.592953,1.909474,9.746218,-1.514191,5.517510,4.874736,-2.539302,-6.686568,7.079175,4.232496,-4.347482,3.195582,4.707169,6.830209,-5.250663,9.286295,-1.422123,-5.296987,-0.383628,-6.997258,4.458907,3.056202,-0.144645,0.394355,2.919239,6.922294,1.756782,-6.466762,3.201102,-7.520101,-2.201471,7.370472,-7.356792,-9.307611,-2.056546,-0.567237,-1.105426,-2.219089,3.797599,-2.125259,-5.358288,2.555034,7.004115,-2.432882,4.389489,-3.649659,-7.577112,-9.375530,4.143696,8.530876,9.244354,-8.157435,5.681488,-3.643836,-7.600031,-7.410601,-1.906760,3.080000,0.573660,2.214114,-7.590819,-2.923671,3.075799,6.172832,8.377277,5.615391,-2.927900,5.259424,-1.833368,-5.307199,-9.647063,0.071761,-3.011598,-1.034457,5.219552,-9.686843,7.158224,-5.858864,6.528671,-2.283980,3.790731,-1.580330,2.545087,1.011994,4.760453,-5.640337,-9.544816,1.219417,-8.370450,-3.001013,2.279965,7.029031,5.235913,0.634263,8.109822,-6.490863,3.628562,-8.973448,-9.788775,-4.157675,-4.259507,1.097024,0.213663,8.964807,5.001494,2.596399,7.255611,8.273988,-5.910699,9.602397,-6.155721,-0.682463,-1.712886,-9.026412,9.784656,6.744327,-5.320810,-8.651898,3.742624,3.328747,-2.532523,9.501974,-1.995561,-5.928657,7.264163,-5.985698,3.569720,-2.559144,-8.457909,-2.524873,6.240642,5.521192,2.447469,3.746599,1.795835,0.626889,0.228012,1.267500,1.924535,1.072354,-8.065508,4.193505,-3.513467,5.956166,-5.971761,-4.561123,9.896060,8.657320,-1.933366,0.299159,-6.463403,0.070146,0.363344,2.852069,-7.184984,-4.906186,-9.979358,8.219268,0.866846,1.854245,-7.243062,1.384100,9.440288,-1.860635,-8.100955,-4.672438,-3.002487,-7.812626,-3.197017,3.898835,-4.374504,3.750159,6.338994,-8.706239,-6.135966,-0.951036,3.719142,-4.604836,3.670963,-9.102445,8.627633,-8.133821,-3.328915,0.667107,-4.120098,-3.710707,-1.839256,4.264291,-4.941026,-4.970935,-4.247760,0.145100,6.501243,-6.357664,2.494499,-7.031778,3.421116,-7.225582,5.133395,3.343514,-6.698134,0.868104,6.173576,-2.631561,-5.188068,-1.646064,-7.699185,-7.588988,-1.721127,-6.821123,-4.142979,-9.490884,8.288452,1.229841,-1.109958,-9.492338,-3.344431,-0.634081,-5.385143,2.632633,0.157675,9.905587,-9.518754,8.620661,8.416389,-8.428440,-2.706531,1.331592,4.965005,5.962035,3.813518,6.565585,7.677425,-5.924852,-8.286948,-1.666038,8.798003,2.916731,4.741902,-7.522236,-9.939728,-0.338359,7.833662,-8.706495,2.635868,7.009629,3.627704,-8.623089,-6.627505,5.843807,4.123867,-9.629084,5.336515,-5.069116,1.661449,4.752613,5.339473,-7.312727,-6.390965,8.319766,-2.662486,-8.898426,9.387460,-5.425894,6.605210,0.937709,2.575809,-5.079708,0.059563,-8.082869,8.453416,9.554367,9.427266,-2.197845,-3.540735,0.751855,-3.778138,9.775004,8.173713,7.947171,6.711507,5.940768,-6.406367,1.167362,-1.372024,-2.439600,-0.066698,-3.341149,-6.124998,2.086780,-8.213509,2.884372,-0.221690,2.861646,6.294301,5.420930,8.155605,5.810346,-0.212341,6.746146,-3.049772,-2.061401,8.765755,5.771862,9.087335,6.215658,5.543645,-8.451781,4.616865,1.243112,-3.763146,5.325029,5.660529,-0.309651,3.773737,-3.472402,3.085106,-5.183064,0.801208,-0.737890,-5.243036,8.706646,9.585115,-0.983334,5.826164,5.380071,-1.218801,5.916703,5.242961,2.615057,9.630999,2.474430,-7.088500,-2.997810,3.720412,0.471961,-0.526372,3.859671,-4.491161,-9.529914,-5.470759,-6.055742,-9.313585,-3.973003,9.531950,-6.648769,-7.806748,2.692454,-1.146745,-5.885820,2.024750,6.689237,-9.458282,5.807714,-4.186347,-1.156165,1.917740,2.606792,-7.920892,2.307634,8.605800,5.579070,4.960588,9.763175,-9.779387,4.247038,5.777605,9.120949,-0.877523,-6.997090,-6.634315,0.104979,7.760649,3.873317,-7.174592,3.196094,-6.056523,8.615332,-6.288458,8.888411,6.345465,-4.939341,-9.626406,-8.142835,-8.773215,6.425233,-7.828746,-4.168262,-5.172584,9.312781,-0.783651,-5.716247,6.036418,5.838531,-7.020895,-4.374673,8.039454,-2.087521,-4.673962,-2.136985,-7.827603,9.538865,-8.477053,-7.123172,1.583153,-8.905360,0.342188,0.648643,-4.707565,-7.404409,3.560125,-7.009760,8.283995,-7.590718,-3.442133,-1.523392,9.276193,1.375882,6.991695,-3.080232,7.411123,-6.526386,5.549752,-9.775560,-8.535971,6.447113,9.862209,7.758262,-9.484477,7.375353,-4.902961,1.624170,7.477172,-3.792888,4.138455,-3.358651,6.998646,7.326737,-6.097088,-1.789623,-2.907501,-4.545328,-9.704978,-0.904985,-5.957209,6.444780,2.784432,-7.923037,0.496493,8.041896,1.666903,6.297949,-5.666727,6.496773,-4.284169,-1.733264,4.039148,6.409140,-5.279295,9.696671,3.945867,4.905868,5.005479,8.463323,-1.924145,8.144385,-2.426447,-4.618830,0.895348,6.646683,-6.944487,-3.990242,2.588117,5.210801,0.650769,-9.761982,3.521251,3.325031,9.191864,4.875842,7.292039,3.387682,2.751715,3.110388,2.532912,8.048291,-0.352826,-9.353877,0.595290,3.798609,-1.480141,7.971706,1.225354,-5.968646,1.848341,5.100761,6.977567,7.461483,-2.124242,8.513875,4.635118,9.089900,4.639335,7.141588,3.879554,6.300680,-6.096106,6.837882,-0.901945,-1.977169,3.778672,-7.393383,-4.946928,-1.634485,-8.529095,9.576659,-2.318599,2.791219,-7.901291,-2.519804,8.144669,4.851493,-9.501319,-8.880174,-8.301140,-8.018588,-5.938403,-7.559352,-0.025249,0.488558,5.936641,8.954983,-2.219307,2.909872,3.859149,-0.531043,1.671755,5.614721,0.386164,-9.793825,-3.871973,8.658568,-8.078374,-1.606697,-1.827091,6.471405,-6.487247,2.151277,-1.005530,8.082349,-4.197942,-3.551265,4.615235,0.061123,6.620845,-8.303099,1.145493,-8.381480,-6.142335,-1.547543,8.316818,-9.837959,-0.924672,-7.012435,-1.521392,7.308682,1.622057,-2.836929,0.389015,4.497185,-6.338327,-5.047967,-7.492613,1.251767,5.490685,2.820023,4.572951,-7.835801,-1.057069,-7.375618,-2.978112,1.517626,-8.546349,-2.705715,-9.542923,-9.785618,-6.166601,-2.673666,-9.544234,1.814552,1.250757,-1.471045,-3.277392,9.965958,9.481920,8.407678,4.426503,6.513549,-8.345024,1.584393,-9.163828,9.010521,-1.122148,4.848261,0.155735,1.166080,1.731646,-4.217908,-9.298002,-7.465519,8.957265,-4.153158,0.934456,-7.076039,2.837375,-6.600969,-6.977324,-6.497669,0.473300,0.892769,-1.875531,1.135455,-2.127138,4.359387,8.099622,-8.659689,2.375343,4.775979,-3.793292,8.236210,9.632190,8.392288,5.610987,5.009955,8.296463,-7.150696,1.100467,-0.186908,9.965185,-8.504080,1.974176,7.696359,6.211724,4.211681,1.231680,-2.089634,-3.686585,-4.817654,9.452125,-4.571453,-6.723038,2.251589,8.868294,5.998797,3.364355,7.118780,-6.821008,-6.421229,-8.967600,6.234381,-8.316402,-6.101506,-0.735696,-6.085102,-1.591768,-7.880679,5.650868,-5.750281,4.000660,0.691227,-0.081582,-6.633881,-8.889674,-9.452595,-0.722205,-0.698701,9.044612,-6.806972,7.879980,-7.764619,4.116160,-8.362777,-5.801233,9.377716,-4.665879,-2.093240,-6.067687,9.582205,8.615890,8.480871,7.690589,-3.949537,-5.745524,-5.443797,-8.836717,-5.032458,-2.575758,-8.934505,2.974255,-7.849965,5.068756,-3.866697,0.112810,-9.327881,-8.830726,5.376082,5.667615,-2.484580,-0.217559,9.447812,7.232690,-8.319831,-7.252471,-9.174047,6.656289,5.042728,-5.556488,-4.405330,1.612357,-3.192516,-1.595957,3.971407,-3.071629,5.749379,9.493072,3.785604,-8.112850,-8.268681,-7.575365,6.442348,7.417439,-3.826010,-0.350732,-4.090344,7.808003,3.825367,-7.326223,5.873418,5.315380,0.563459,4.832811,7.725947,-2.279537,-9.093087,8.173654,-3.282383,-9.267188,-4.039846,7.832463,-3.857918,1.461710,-6.732439,5.786928,-9.037493,9.958312,9.118876,-5.561233,-5.380182,-9.027352,-6.315238,-4.927499,-3.794163,5.410515,-2.984105,9.871897,-9.937399,-3.862000,-5.461134,-4.334297,-3.946421,-5.420660,0.299904,4.414455,-6.362549,-2.887400,2.690461,1.643091,-1.932916,-3.517402,-3.789039,6.038030,-1.721833,6.391351,4.067162,-4.626592,6.359912,9.638867,5.674164,5.812727,-6.964107,-8.661469,-3.772976,-0.782769,0.923214,2.195710,-1.266381,-8.068302,5.262211,-3.821164,3.360331,-9.295256,2.671564,7.928716,-1.279172,-3.156056,6.548244,-3.214136,9.503079,-3.447790,7.658213,-8.245569,-2.434183,4.530998,-3.001836,2.309425,-9.898460,3.689570,1.191875,-7.497432,2.176327,0.185100,-7.122509,-0.012574,-0.624717,-0.818476,5.918218,5.305301,5.501336,9.289741,-5.013586,6.836172,-0.493720,2.662984,-5.685643,-6.019778,-2.406239,-5.289071,0.728444,-9.089220,0.499744,-4.162478,4.638681,-4.710636,-1.425783,8.234997,-5.294769,0.309273,7.115599,3.074071,-8.677877,5.224140,1.243840,7.547720,-1.541469,-9.681248,-2.840823,-9.012490,-3.506350,-9.404486,-6.685227,-6.688141,6.232563,-6.636473,-7.117189,-4.583772,3.464923,7.986499,8.737885,3.140493,6.735551,6.206441,-2.081278,4.752978,-9.999851,9.307677,2.306481,-5.612734,9.198008,4.282531,-6.031652,7.829911,9.604948,-7.637385,9.190103,1.671898,9.868025,8.070404,-4.714625,-5.463906,-1.756115,-4.110124,9.566408,-3.670630,9.895330,-9.960851,1.934702,8.319960,3.653147,6.962543,0.874329,2.069928,6.712083,7.628275,4.976598,2.562068,0.137694,-8.913642,-7.729510,-6.591867,-5.121103,0.556372,-8.616323,7.623965,-3.406026,-4.805924,7.616648,-7.376303,-2.178311,-5.303098,5.013792,-5.917187,4.857091,-7.226987,0.492089,3.922171,5.293582,-4.606158,1.261940,5.630339,-1.108882,-9.300811,7.595469,5.374948,-2.112414,-9.098988,5.588154,-5.133898,5.706983,-5.599646,5.006057,-2.049349,-6.738879,-3.997802,-1.114235,3.065315,-9.298361,-7.234729,-0.078780,6.976084,-7.955360,-8.604363,-9.676228,-8.558206,0.310754,1.862093,5.830900,-1.723076,-9.771430,1.648357,-0.116733,4.137250,-1.541789,5.755404,1.755158,0.846656,-8.267652,4.889761,8.824726,-7.157446,-3.198342,5.068774,7.458660,8.801853,2.331120,9.157778,9.439389,-3.388036,-6.707046,-8.915260,-9.971871,7.880365,-2.402404,-1.387933,9.072915,-9.373569,-4.532767,7.481869,7.655291,8.842751,3.928870,4.157331,1.033977,0.491060,2.412836,-7.449784,8.185698,-7.399840,-3.211563,9.848751,2.780824,-1.049489,-2.235263,1.584954,-3.663572,-7.450172,1.238895,5.110991,4.069585,0.948745,-5.563261,-1.508771,0.755183,1.768417,3.674133,6.560582,8.927237,-9.139513,8.130153,0.699796,-0.950137,-8.614322,3.759785,4.839624,-8.456362,3.084553,-1.380067,-7.032239,-3.807106,0.359470,0.710441,-8.909088,-4.792991,-0.023431,4.267638,-2.578926,5.267515,6.133959,-3.625472,5.260281,4.018902,6.671726,-9.679618,-7.742021,-9.608335,9.081639,-4.885138,-8.633302,-2.039713,5.581752,-4.379251,-7.704812,-8.292197,6.030289,-0.824405,4.188844,8.418634,9.940257,-0.678359,9.600627,1.050017,-9.063456,-4.764102,3.513848,1.018511,-9.758676,-4.858910,1.408301,0.758862,3.326259,3.081507,0.159826,0.594956,3.341229,-8.604444,-4.865832,7.978730,-4.611154,3.639424,-2.342358,-1.795079,7.842500,4.962890,4.093412,8.232057,-5.179511,0.996680,5.128402,-5.073613,-8.116536,8.058762,9.579104,-5.528394,0.002497,5.893888,-6.948897,-4.052902,-9.360629,7.267466,-9.545417,-6.093569,4.794158,6.335240,-7.960670,2.518888,-0.631042,-6.933366,3.841922,1.132730,-3.522458,4.910859,-6.891868,-4.179244,1.114299,-6.716140,-4.155048,9.364383,-6.998654,5.615134,-8.089425,-0.569647,7.736136,-0.784113,8.991036,9.214140,-1.510621,-9.939663,6.722600,2.206923,-7.101279,-5.443304,-4.591577,5.682489,-7.155412,-1.691255,9.534187,-4.516030,0.102325,-8.489925,-8.016597,-8.828458,-9.672453,-4.182417,-0.044189,-0.194511,1.795233,1.406896,-7.111590,2.369706,1.546659,-7.107502,-1.339305,-0.655664,0.214284,-0.925407,-3.642841,9.017097,6.072381,-3.312569,1.245504,1.896944,-6.481038,9.700589,7.600963,1.731870,-4.979137,4.608771,-1.617709,-1.326869,-3.555800,-0.883264,4.020117,8.203324,8.372308,-5.538922,5.960435,5.739722,2.720274,-0.770975,9.373630,6.300571,8.276259,-4.345295,-4.279224,-0.548940,4.364971,-2.670299,-3.024360,-4.182641,5.893260,-2.202109,-4.010251,-1.505323,-8.224257,-3.182779,7.146379,1.347748,-7.777819,-4.850235,-7.174765,-1.453868,1.673881,1.443260,-6.112525,2.604792,-5.459696,-1.749262,-5.616293,-6.241376,-0.918940,-8.238585,4.957109,-1.491413,-5.632934,-9.934393,7.614075,-8.638731,0.444636,-1.523111,9.463094,-5.645154,-9.625682,-9.640343,4.112359,9.785511,1.167573,8.538994,-9.909594,9.861464,1.515085,9.702568,-8.375689,0.148073,5.548022,6.993842,-0.392396,9.357561,2.880253,1.966122,-3.989210,-2.652261,-8.625548,-4.004360,8.389244,7.318831,-6.352424,-5.960175,0.720893,-6.129222,4.534252,5.615927,4.145564,-8.894082,2.934875,-6.987635,5.565672,0.496804,-7.563169,-6.851115,5.232744,-1.027576,-9.256187,-0.805873,4.372245,8.828732,9.422927,-5.507608,7.401329,9.704937,-7.080590,-4.780124,-2.941227,7.230032,-4.359895,-4.553232,-2.529706,2.699421,7.807526,-3.636235,-6.119542,-9.869266,-5.769626,5.108148,7.422399,-9.319029,-8.445771,2.932734,5.043814,5.293294,-1.225722,1.320615,3.318642,-5.043826,3.728310,3.454801,-6.821914,9.584790,-3.864394,-9.635117,5.709774,5.008517,7.677372,-5.023363,4.652977,-5.869784,5.624236,-8.835800,-1.423664,-7.519185,9.971058,-8.092597,6.495100,8.484208,-5.416952,3.283296,-3.113635,2.727161,-7.570118,-2.475720,3.108558,9.929432,1.481150,9.812641,-8.580607,6.771894,3.775292,4.211945,8.050936,-8.433717,-5.083273,2.251224,-8.301605,2.584349,-7.108432,4.045018,-2.859131,-1.951490,-1.737274,-2.160669,9.011146,7.200104,9.579886,8.428669,5.162455,-5.225546,-2.637323,-2.927957,-3.622365,6.654387,-0.602157,-2.800245,6.961408,-8.342288,2.611639,6.981871,-9.919396,4.775588,8.633545,-7.226111,2.329296,8.262596,-1.111064,-6.689066,9.663184,3.095247,-9.358362,-1.459469,-3.285425,-2.166259,2.796320,6.644140,-1.292992,3.530332,7.450754,-0.413851,-3.483180,-3.011210,0.450054,5.582668,-0.173650,-9.838728,0.275672,0.045574,9.143323,2.239904,4.065854,-5.623492,6.999090,6.854418,2.952377,6.800685], dtype = "float32")#candidate|6212|(3136,)|const|float32
call_6211 = relay.TupleGetItem(func_5872_call(relay.reshape(const_6212.astype('float32'), [16, 14, 14])), 2)
call_6213 = relay.TupleGetItem(func_5874_call(relay.reshape(const_6212.astype('float32'), [16, 14, 14])), 2)
func_6195_call = mod.get_global_var('func_6195')
func_6196_call = mutated_mod.get_global_var('func_6196')
call_6214 = relay.TupleGetItem(func_6195_call(), 0)
call_6215 = relay.TupleGetItem(func_6196_call(), 0)
output = relay.Tuple([call_6197,call_6211,const_6212,call_6214,])
output2 = relay.Tuple([call_6198,call_6213,const_6212,call_6215,])
func_6221 = relay.Function([], output)
mod['func_6221'] = func_6221
mod = relay.transform.InferType()(mod)
mutated_mod['func_6221'] = func_6221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6221_call = mutated_mod.get_global_var('func_6221')
call_6222 = func_6221_call()
output = call_6222
func_6223 = relay.Function([], output)
mutated_mod['func_6223'] = func_6223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5782_call = mod.get_global_var('func_5782')
func_5784_call = mutated_mod.get_global_var('func_5784')
call_6242 = relay.TupleGetItem(func_5782_call(), 0)
call_6243 = relay.TupleGetItem(func_5784_call(), 0)
func_4041_call = mod.get_global_var('func_4041')
func_4044_call = mutated_mod.get_global_var('func_4044')
var_6281 = relay.var("var_6281", dtype = "float32", shape = (864,))#candidate|6281|(864,)|var|float32
call_6280 = relay.TupleGetItem(func_4041_call(relay.reshape(var_6281.astype('float32'), [6, 9, 16])), 0)
call_6282 = relay.TupleGetItem(func_4044_call(relay.reshape(var_6281.astype('float32'), [6, 9, 16])), 0)
bop_6283 = relay.not_equal(call_6280.astype('bool'), relay.reshape(var_6281.astype('bool'), relay.shape_of(call_6280))) # shape=(6, 9, 16)
bop_6286 = relay.not_equal(call_6282.astype('bool'), relay.reshape(var_6281.astype('bool'), relay.shape_of(call_6282))) # shape=(6, 9, 16)
output = relay.Tuple([call_6242,bop_6283,])
output2 = relay.Tuple([call_6243,bop_6286,])
func_6310 = relay.Function([var_6281,], output)
mod['func_6310'] = func_6310
mod = relay.transform.InferType()(mod)
mutated_mod['func_6310'] = func_6310
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6311 = relay.var("var_6311", dtype = "float32", shape = (864,))#candidate|6311|(864,)|var|float32
func_6310_call = mutated_mod.get_global_var('func_6310')
call_6312 = func_6310_call(var_6311)
output = call_6312
func_6313 = relay.Function([var_6311], output)
mutated_mod['func_6313'] = func_6313
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6322 = relay.const(True, dtype = "bool")#candidate|6322|()|const|bool
var_6323 = relay.var("var_6323", dtype = "bool", shape = (7, 2, 9))#candidate|6323|(7, 2, 9)|var|bool
bop_6324 = relay.logical_or(const_6322.astype('bool'), var_6323.astype('bool')) # shape=(7, 2, 9)
output = bop_6324
output2 = bop_6324
func_6332 = relay.Function([var_6323,], output)
mod['func_6332'] = func_6332
mod = relay.transform.InferType()(mod)
var_6333 = relay.var("var_6333", dtype = "bool", shape = (7, 2, 9))#candidate|6333|(7, 2, 9)|var|bool
output = func_6332(var_6333)
func_6334 = relay.Function([var_6333], output)
mutated_mod['func_6334'] = func_6334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mod.get_global_var('func_3833')
func_3835_call = mutated_mod.get_global_var('func_3835')
call_6336 = relay.TupleGetItem(func_3833_call(), 0)
call_6337 = relay.TupleGetItem(func_3835_call(), 0)
output = relay.Tuple([call_6336,])
output2 = relay.Tuple([call_6337,])
func_6365 = relay.Function([], output)
mod['func_6365'] = func_6365
mod = relay.transform.InferType()(mod)
output = func_6365()
func_6366 = relay.Function([], output)
mutated_mod['func_6366'] = func_6366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4825_call = mod.get_global_var('func_4825')
func_4826_call = mutated_mod.get_global_var('func_4826')
call_6403 = relay.TupleGetItem(func_4825_call(), 1)
call_6404 = relay.TupleGetItem(func_4826_call(), 1)
func_4068_call = mod.get_global_var('func_4068')
func_4070_call = mutated_mod.get_global_var('func_4070')
var_6429 = relay.var("var_6429", dtype = "float64", shape = (1155,))#candidate|6429|(1155,)|var|float64
call_6428 = relay.TupleGetItem(func_4068_call(relay.reshape(var_6429.astype('float64'), [7, 11, 15])), 0)
call_6430 = relay.TupleGetItem(func_4070_call(relay.reshape(var_6429.astype('float64'), [7, 11, 15])), 0)
func_904_call = mod.get_global_var('func_904')
func_907_call = mutated_mod.get_global_var('func_907')
var_6434 = relay.var("var_6434", dtype = "float64", shape = (182,))#candidate|6434|(182,)|var|float64
call_6433 = relay.TupleGetItem(func_904_call(relay.reshape(var_6434.astype('float64'), [2, 7, 13])), 0)
call_6435 = relay.TupleGetItem(func_907_call(relay.reshape(var_6434.astype('float64'), [2, 7, 13])), 0)
output = relay.Tuple([call_6403,call_6428,var_6429,call_6433,var_6434,])
output2 = relay.Tuple([call_6404,call_6430,var_6429,call_6435,var_6434,])
func_6442 = relay.Function([var_6429,var_6434,], output)
mod['func_6442'] = func_6442
mod = relay.transform.InferType()(mod)
var_6443 = relay.var("var_6443", dtype = "float64", shape = (1155,))#candidate|6443|(1155,)|var|float64
var_6444 = relay.var("var_6444", dtype = "float64", shape = (182,))#candidate|6444|(182,)|var|float64
output = func_6442(var_6443,var_6444,)
func_6445 = relay.Function([var_6443,var_6444,], output)
mutated_mod['func_6445'] = func_6445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5782_call = mod.get_global_var('func_5782')
func_5784_call = mutated_mod.get_global_var('func_5784')
call_6500 = relay.TupleGetItem(func_5782_call(), 0)
call_6501 = relay.TupleGetItem(func_5784_call(), 0)
func_4517_call = mod.get_global_var('func_4517')
func_4518_call = mutated_mod.get_global_var('func_4518')
call_6506 = relay.TupleGetItem(func_4517_call(), 0)
call_6507 = relay.TupleGetItem(func_4518_call(), 0)
func_4206_call = mod.get_global_var('func_4206')
func_4207_call = mutated_mod.get_global_var('func_4207')
call_6519 = func_4206_call()
call_6520 = func_4206_call()
output = relay.Tuple([call_6500,call_6506,call_6519,])
output2 = relay.Tuple([call_6501,call_6507,call_6520,])
func_6540 = relay.Function([], output)
mod['func_6540'] = func_6540
mod = relay.transform.InferType()(mod)
mutated_mod['func_6540'] = func_6540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6540_call = mutated_mod.get_global_var('func_6540')
call_6541 = func_6540_call()
output = call_6541
func_6542 = relay.Function([], output)
mutated_mod['func_6542'] = func_6542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_6566 = relay.TupleGetItem(func_3534_call(), 1)
call_6567 = relay.TupleGetItem(func_3536_call(), 1)
func_4953_call = mod.get_global_var('func_4953')
func_4956_call = mutated_mod.get_global_var('func_4956')
var_6595 = relay.var("var_6595", dtype = "float64", shape = (2016,))#candidate|6595|(2016,)|var|float64
call_6594 = relay.TupleGetItem(func_4953_call(relay.reshape(call_6566.astype('float32'), [2, 13, 5]), relay.reshape(var_6595.astype('float64'), [2016, 1]), ), 0)
call_6596 = relay.TupleGetItem(func_4956_call(relay.reshape(call_6566.astype('float32'), [2, 13, 5]), relay.reshape(var_6595.astype('float64'), [2016, 1]), ), 0)
func_4596_call = mod.get_global_var('func_4596')
func_4599_call = mutated_mod.get_global_var('func_4599')
const_6622 = relay.const([8,7,1,-2,-6,4,3,-1,1,2,9,6,-7,-8,-8,4,-4,5,2,-2,8,-10,5,-1,-1,4,8,-10,8,1,-9,-2,-3,8,6,8,6,-4,1,-7,-10,-10,3,-3,-10,-7,-9,-3,7,2,3,-7,7,-10,-7,-1,-8,-5,-3,-1,5,5,6,8,9,-7,1,-1,-5,7,10,9,8,-10,-4,-7,9,-5,-10,-10,-7,3,-3,4,-9,-10,-8,-6,4,-1,-7,9,2,2,-9,3,1,1,4,2,8,-2,-2,7,4,-6,8,-8,-9,2,-5,3,-3,-2,2,10,-7,-8,-1,-8,-3,-8,8,-3,6,-5,2,-7,-4,2,2,-6,4,-1,-9,10,3,-4,3,10,-3,-10,-4,-8,7,-4,3,1,2,-2,1,2,9,-7,-3,4,1,-9,-5,3,8,-3,5,-8,-8,-9,-2,4,-9,6,5,8,-5,3,7,-4,-3,-7,2,9,-6,8,-1,1,-3,-4,10,6,-2], dtype = "int64")#candidate|6622|(189,)|const|int64
call_6621 = relay.TupleGetItem(func_4596_call(relay.reshape(const_6622.astype('int64'), [189,])), 0)
call_6623 = relay.TupleGetItem(func_4599_call(relay.reshape(const_6622.astype('int64'), [189,])), 0)
output = relay.Tuple([call_6566,call_6594,var_6595,call_6621,const_6622,])
output2 = relay.Tuple([call_6567,call_6596,var_6595,call_6623,const_6622,])
func_6633 = relay.Function([var_6595,], output)
mod['func_6633'] = func_6633
mod = relay.transform.InferType()(mod)
var_6634 = relay.var("var_6634", dtype = "float64", shape = (2016,))#candidate|6634|(2016,)|var|float64
output = func_6633(var_6634)
func_6635 = relay.Function([var_6634], output)
mutated_mod['func_6635'] = func_6635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3351_call = mod.get_global_var('func_3351')
func_3352_call = mutated_mod.get_global_var('func_3352')
call_6684 = func_3351_call()
call_6685 = func_3351_call()
uop_6708 = relay.log2(call_6684.astype('float32')) # shape=(2, 13, 5)
uop_6710 = relay.log2(call_6685.astype('float32')) # shape=(2, 13, 5)
func_5042_call = mod.get_global_var('func_5042')
func_5044_call = mutated_mod.get_global_var('func_5044')
call_6726 = func_5042_call()
call_6727 = func_5042_call()
output = relay.Tuple([uop_6708,call_6726,])
output2 = relay.Tuple([uop_6710,call_6727,])
func_6730 = relay.Function([], output)
mod['func_6730'] = func_6730
mod = relay.transform.InferType()(mod)
mutated_mod['func_6730'] = func_6730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6730_call = mutated_mod.get_global_var('func_6730')
call_6731 = func_6730_call()
output = call_6731
func_6732 = relay.Function([], output)
mutated_mod['func_6732'] = func_6732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4517_call = mod.get_global_var('func_4517')
func_4518_call = mutated_mod.get_global_var('func_4518')
call_6762 = relay.TupleGetItem(func_4517_call(), 0)
call_6763 = relay.TupleGetItem(func_4518_call(), 0)
output = relay.Tuple([call_6762,])
output2 = relay.Tuple([call_6763,])
func_6768 = relay.Function([], output)
mod['func_6768'] = func_6768
mod = relay.transform.InferType()(mod)
mutated_mod['func_6768'] = func_6768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6768_call = mutated_mod.get_global_var('func_6768')
call_6769 = func_6768_call()
output = call_6769
func_6770 = relay.Function([], output)
mutated_mod['func_6770'] = func_6770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5981_call = mod.get_global_var('func_5981')
func_5982_call = mutated_mod.get_global_var('func_5982')
call_6771 = func_5981_call()
call_6772 = func_5981_call()
func_1798_call = mod.get_global_var('func_1798')
func_1802_call = mutated_mod.get_global_var('func_1802')
var_6776 = relay.var("var_6776", dtype = "uint16", shape = (5, 189))#candidate|6776|(5, 189)|var|uint16
call_6775 = func_1798_call(relay.reshape(var_6776.astype('uint16'), [7, 9, 15]), relay.reshape(var_6776.astype('uint16'), [7, 9, 15]), )
call_6777 = func_1798_call(relay.reshape(var_6776.astype('uint16'), [7, 9, 15]), relay.reshape(var_6776.astype('uint16'), [7, 9, 15]), )
uop_6782 = relay.acosh(var_6776.astype('float64')) # shape=(5, 189)
bop_6789 = relay.maximum(uop_6782.astype('int8'), relay.reshape(call_6775.astype('int8'), relay.shape_of(uop_6782))) # shape=(5, 189)
bop_6792 = relay.maximum(uop_6782.astype('int8'), relay.reshape(call_6777.astype('int8'), relay.shape_of(uop_6782))) # shape=(5, 189)
output = relay.Tuple([call_6771,bop_6789,])
output2 = relay.Tuple([call_6772,bop_6792,])
func_6798 = relay.Function([var_6776,], output)
mod['func_6798'] = func_6798
mod = relay.transform.InferType()(mod)
var_6799 = relay.var("var_6799", dtype = "uint16", shape = (5, 189))#candidate|6799|(5, 189)|var|uint16
output = func_6798(var_6799)
func_6800 = relay.Function([var_6799], output)
mutated_mod['func_6800'] = func_6800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5663_call = mod.get_global_var('func_5663')
func_5665_call = mutated_mod.get_global_var('func_5665')
call_6802 = func_5663_call()
call_6803 = func_5663_call()
output = relay.Tuple([call_6802,])
output2 = relay.Tuple([call_6803,])
func_6808 = relay.Function([], output)
mod['func_6808'] = func_6808
mod = relay.transform.InferType()(mod)
mutated_mod['func_6808'] = func_6808
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6808_call = mutated_mod.get_global_var('func_6808')
call_6809 = func_6808_call()
output = call_6809
func_6810 = relay.Function([], output)
mutated_mod['func_6810'] = func_6810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5663_call = mod.get_global_var('func_5663')
func_5665_call = mutated_mod.get_global_var('func_5665')
call_6836 = func_5663_call()
call_6837 = func_5663_call()
uop_6847 = relay.sqrt(call_6836.astype('float32')) # shape=(2, 13, 5)
uop_6849 = relay.sqrt(call_6837.astype('float32')) # shape=(2, 13, 5)
output = relay.Tuple([uop_6847,])
output2 = relay.Tuple([uop_6849,])
func_6857 = relay.Function([], output)
mod['func_6857'] = func_6857
mod = relay.transform.InferType()(mod)
output = func_6857()
func_6858 = relay.Function([], output)
mutated_mod['func_6858'] = func_6858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5333_call = mod.get_global_var('func_5333')
func_5335_call = mutated_mod.get_global_var('func_5335')
call_6944 = relay.TupleGetItem(func_5333_call(), 0)
call_6945 = relay.TupleGetItem(func_5335_call(), 0)
func_4517_call = mod.get_global_var('func_4517')
func_4518_call = mutated_mod.get_global_var('func_4518')
call_6948 = relay.TupleGetItem(func_4517_call(), 0)
call_6949 = relay.TupleGetItem(func_4518_call(), 0)
func_4041_call = mod.get_global_var('func_4041')
func_4044_call = mutated_mod.get_global_var('func_4044')
const_6955 = relay.const([-0.801454,-4.677033,-1.779696,3.251101,-7.112661,-6.384524,-2.702366,6.360674,1.780893,-8.470906,-0.771341,5.628845,0.319384,5.124364,-9.022023,-3.977643,-7.945986,-7.584420,-3.433757,-2.499786,8.479880,5.134098,0.719435,8.366102,5.856678,-6.138487,6.709012,-7.359149,9.998397,-3.257594,-4.418354,5.123657,8.349204,8.197707,9.753327,-3.762522,-9.794595,-9.687355,-6.751523,5.652834,-7.006361,1.946035,0.861438,-9.950963,-3.251211,-7.782382,-9.380894,4.006851,7.826551,1.222918,-0.812090,-5.401181,8.468725,0.391693,-2.428281,1.349410,-5.450650,5.154625,-9.861628,-3.028339,-2.971163,-3.545698,-6.616347,-4.309635,-2.722433,-2.299032,3.277054,-2.159400,-3.530350,-2.416059,-0.437490,4.179638,9.905750,-8.729070,-9.441427,-7.053662,4.815198,7.715987,-5.795130,8.482237,2.920201,-6.899925,-4.695904,4.957681,-0.271522,-9.335227,-0.475988,4.207731,-7.318317,0.541777,-7.490885,1.489643,-9.220102,-4.285678,-5.105002,-3.099352,1.946525,-9.614608,4.194098,-4.270707,4.092678,-8.472814,-4.583934,6.360928,6.071432,-8.869881,-0.491862,6.798382,-4.376309,-6.948449,3.243565,9.647087,2.611956,0.082807,2.936803,-1.650034,-5.890796,-4.212141,-0.379347,8.400117,5.158133,1.763559,8.550544,-9.824494,-1.989574,-0.580393,1.140278,3.396505,9.866222,0.103040,-5.933194,6.125573,-2.006353,-6.283071,-2.893785,-3.790335,6.000295,9.605689,-5.409585,-8.300723,-8.175514,2.146476,-9.647576,-5.141585,1.566405,1.019476,7.892855,-6.984930,-7.359210,-9.830502,-4.133826,-7.627271,4.683985,-5.157783,-7.619548,-8.035998,5.145369,-7.245516,-1.002272,4.051875,2.372800,-7.004533,8.289736,-1.077860,4.122669,-1.656032,-0.633580,3.314994,4.668038,9.647819,-0.131909,-3.075824,9.857757,-8.333400,-4.376278,4.655890,-0.212451,-5.604652,-1.713196,9.089165,-1.627485,4.136143,5.590641,-7.441257,-0.674463,-0.509143,4.255147,-4.752401,8.866202,1.657617,-2.765609,9.105653,-8.658426,7.404444,9.172428,-0.999766,-4.495271,-8.051390,-2.486470,-9.418696,-1.312554,5.934582,-3.371147,2.251110,-3.405674,1.264304,0.252535,9.953438,-7.081271,1.622607,-2.285208,5.790728,1.676079,-3.665119,-5.313355,3.355205,1.706586,0.432232,-6.447780,6.788399,7.445650,-5.246382,-4.966025,-8.788654,-5.353726,-4.313620,3.814933,4.488206,8.752543,-7.134691,4.345566,-5.553036,-3.221578,-5.697382,-6.827069,-1.877088,-6.724849,9.063888,-0.809651,2.337027,6.965260,6.672129,-5.070136,1.073942,-5.957479,0.358203,8.427688,-8.777236,5.948215,4.040872,9.121955,8.113973,-5.666711,-7.187115,-5.503101,6.013299,6.821268,-2.219201,2.366115,4.681497,4.171039,6.428477,-9.178688,1.018551,-8.315747,-7.920981,-3.402420,5.555717,-1.056390,5.070219,-1.952062,-2.532794,-8.560510,2.444306,-1.933048,2.974982,2.514708,5.541384,2.869945,-2.822327,7.198940,3.292146,-7.478413,-0.188762,-5.580076,-7.502882,-0.692693,-0.398483,6.631440,-2.274657,-3.600707,-9.245614,7.785880,0.494544,-2.657501,-4.455546,-9.758797,9.787143,4.379462,1.961698,8.449191,-6.365107,-4.254772,-8.747111,-4.464354,-1.434543,7.787133,-7.147645,-4.169423,1.040633,6.351408,-7.638257,5.544839,4.997647,1.365273,-8.134355,-3.667160,-6.661994,9.621260,-2.443235,1.363281,-5.359173,0.132687,2.310265,-8.416823,-9.678852,3.830622,-0.444463,-1.530369,7.920258,-2.891738,7.768211,-4.997437,-6.863695,-1.650578,8.207077,1.032558,-2.308642,-9.004571,-8.609668,-9.182758,6.191804,8.018495,-9.586117,5.467797,4.117048,6.478066,-9.583540,-4.319831,5.248918,1.165109,-9.505460,-8.752594,-0.625639,0.239098,-6.592987,2.712606,4.088047,3.735403,3.222370,3.614640,-7.397874,7.084620,-4.234792,2.844812,-0.444941,-0.309924,5.923876,-1.682219,0.906977,-4.851364,0.616441,3.532180,-3.894491,8.079895,3.343574,-3.823446,7.005377,-6.638468,6.246132,-2.519281,6.375494,1.626803,3.409755,-8.434647,7.865777,-7.721208,-9.674438,2.103731,-6.183057,-9.797042,3.041575,-0.648921,-7.344380,-1.016851,-4.063108,-0.292189,1.039859,9.241236,4.035370,5.555050,-5.682222,9.579907,-6.157074,-9.890047,9.048577,-9.563045,6.867012,-6.445266,-8.848803,-4.815838,3.504561,-8.832005,-6.789733,4.960907,0.551539,-5.675564,6.757872,-0.258906,-2.001271,-5.546094,-0.045741,-0.964288,3.733853,3.643898,5.000881,2.887193,-6.952597,1.251030,2.866085,-7.467229,2.595105,-0.346787,4.279609,-7.453498,5.423131,0.155169,-4.143124,-7.796035,-5.041098,0.211022,6.194240,-9.539937,-7.048179,-4.180460,2.450764,-9.387130,1.221524,1.126662,7.142347,-5.883992,-4.550774,-9.333227,1.232221,4.147425,5.172448,3.186514,8.584957,-7.398095,1.884921,5.104717,-2.561894,5.370664,-0.914582,-3.297324,7.893521,6.500478,-5.471909,-5.738343,-0.999054,-8.006366,-6.278451,-5.042735,1.755796,7.153613,7.216842,4.516729,-4.681473,1.424349,3.017092,-4.030451,-9.369051,4.519849,-8.614084,-6.399219,9.252909,-5.115968,-1.789372,4.169372,5.139266,-7.716414,9.861968,-0.347706,-4.346606,-6.644288,3.189130,-3.055257,-9.719957,4.648646,8.084635,8.886216,-5.854759,-7.475986,-2.655738,-1.548782,-3.872446,-2.714633,5.065666,1.056412,-1.962639,3.446290,7.434152,4.331534,7.391060,-7.330682,-9.852306,2.147771,0.694978,0.380388,8.058299,2.473529,-2.899963,9.563278,1.355257,-6.908881,8.041230,3.935726,9.638067,-1.493344,6.155341,-5.019538,0.049480,-4.984819,0.090662,-7.816795,-4.332560,6.714019,-7.712057,-0.593682,6.832838,9.671522,-7.085744,4.376488,-0.029186,3.601466,-1.896727,7.711934,6.976419,-5.021605,-9.570702,-3.249513,0.336470,5.286770,-3.332794,4.255976,-5.800856,-2.176944,4.398596,1.458622,-8.174383,-5.101952,-8.946942,-7.075022,8.640574,-0.172114,9.239592,-0.202093,-6.589297,-7.116442,3.864916,6.634979,2.118791,0.726440,5.057281,-6.626117,2.142087,8.993974,-2.672360,0.108222,-7.483614,9.312936,-0.688217,-5.292377,-8.254271,-7.505905,-9.937856,5.193275,7.582390,1.522610,0.764613,-1.360610,-3.275045,-3.311497,5.441929,-8.096097,-2.820011,-6.771965,-7.386193,3.259435,2.861374,-4.915378,5.970854,4.125548,-2.810506,-5.450392,-6.532138,-4.174147,-9.839932,-0.894200,7.873880,9.690997,-3.573524,-4.566320,3.729656,1.422035,3.463483,-4.467100,-8.536913,-6.042925,-1.250539,-6.402093,6.657914,3.890956,-3.084342,-8.739284,7.252175,7.885331,5.195504,-8.724686,5.361842,7.651331,5.866626,-2.195295,-1.644775,9.616558,2.678103,7.818213,-0.882003,-1.218474,-9.913469,-3.810411,-0.446434,-0.885658,-4.682483,-6.971995,-4.937861,-5.101689,-9.176913,9.264357,1.316229,4.633184,4.660747,-9.596517,-2.485477,-9.143186,3.044511,-1.376414,-4.350642,7.400974,7.271130,-5.282829,1.066013,8.070710,6.860265,-2.640941,9.979510,7.948314,9.021879,8.651384,-0.281800,-2.776889,-0.699118,-1.495776,7.187001,0.041165,4.262910,8.492227,4.158215,-2.833664,0.667164,9.508373,0.959746,9.107316,-4.777415,-0.178913,-1.659835,-8.214770,8.891938,4.009669,-6.951850,2.286548,6.486969,5.143234,6.060051,5.704261,-6.526491,-9.408433,-9.015687,-1.176410,-7.782111,5.606443,-5.957902,5.509905,-0.598562,-4.601994,-5.844529,3.267839,-4.640921,-3.944500,-8.061408,4.317421,-4.713131,-7.535511,9.531161,-3.099818,2.924268,8.190745,2.606380,3.832381,5.326799,3.737557,9.196856,9.986361,0.982637,-7.666143,-1.198825,-0.166527,1.840842,8.013771,-5.715048,-8.565257,3.944852,1.968828,-4.547653,0.378173,-6.619171,4.340591,1.923460,-1.859845,-1.216861,-2.353649,-5.741616,-1.829152,-1.956689,-3.921234,3.624621,-6.137678,-5.358504,7.822264,2.576790,4.575616,6.443182,0.997270,4.770444,7.609018,-2.218956,-0.576995,1.798810,-2.339802,-6.073038,-4.873176,4.594684,3.755473,-7.227552,8.315114,4.416996,0.205456,9.582898,3.755005,-0.885960,7.777407,-0.332366,2.809336,-9.799648,6.878427,6.611000,-7.785520,8.846130,-4.078209,-7.424386,3.531130,-6.526847,2.007034,5.068173,3.878936,1.114220,9.698270,-6.426654,7.727266,-3.087556,-1.990783,-9.130674,1.784224,-7.861817,0.752622,3.392889,-3.264443,-6.375603,8.590698,-9.813079,4.506034,3.018584,4.976547,-8.098011,-7.923143,-7.381302,-0.855188,0.496481,-6.363941,4.834500,1.875754,-0.873777,3.461680,5.804708,-3.494712,6.731321,5.875365,-7.543783,-5.121560,-0.955813,-0.643607,4.989074,0.904930,-0.233514,-4.975031,-1.616354,-9.410678,3.456803,1.882707,-4.456121,-3.358374,5.141449,7.815370,2.537939,-3.795674,-6.243811,-5.698686,3.886509,1.770385,5.950298,-0.915132,3.976129,-3.709056,-6.873564,3.282745,5.365098,-5.984605,7.256041,9.164055,6.066164,-7.633734,-9.572466,-0.985549,8.729822,6.011903,6.804800,-9.043533,-7.522528,-0.051526,-9.019602,3.358145,2.658347,-3.171124,1.944686], dtype = "float32")#candidate|6955|(864,)|const|float32
call_6954 = relay.TupleGetItem(func_4041_call(relay.reshape(const_6955.astype('float32'), [6, 9, 16])), 0)
call_6956 = relay.TupleGetItem(func_4044_call(relay.reshape(const_6955.astype('float32'), [6, 9, 16])), 0)
func_1618_call = mod.get_global_var('func_1618')
func_1622_call = mutated_mod.get_global_var('func_1622')
const_6984 = relay.const([[10,-7,6,7,5,8,-10,2,7,4,3,9,8,-6,5,-10,-7,-1,-8,2,-8,9,-3,9,2,-1,5,4,-7,-8,2,9,-7,-2,-3,-8,-3,3,9,-5,7,-8,8,-8,2,-9,-3,4,3,5,-10,-8,-2,-10,-5,2,3,-8,9,5,-9,-6,7],[2,-7,5,-2,4,-6,-2,1,6,-3,-6,8,6,8,-2,5,4,-3,-1,3,-8,2,-1,6,-7,-2,5,-4,9,-4,-6,7,1,8,6,9,-2,3,-4,-1,-10,-3,2,4,3,2,-7,9,10,3,-3,-7,-5,-8,-1,-1,-3,4,6,-9,-7,8,2],[5,-9,8,-3,4,-7,-9,5,-7,-6,6,-10,9,-7,-5,-6,-1,-1,4,-3,-3,3,7,4,8,9,-4,-8,8,1,6,-6,-10,-7,-2,-3,1,9,-5,3,6,5,1,-2,3,-6,9,-6,-8,3,3,5,3,-1,-8,10,-8,-4,2,-2,9,2,10]], dtype = "int64")#candidate|6984|(3, 63)|const|int64
const_6985 = relay.const([10,6,-8,-7,-6,9,-7,-7,-6,6,7,3,-5,-4,-4,3,-2,9,-1,-3,7,10,-3,-10,10,-8,-5,-2,5,-7,8,-7,10,-10,-4,-7,-5,6,-4,6,4,10,5,2,-10,3,1,-8,-3,2,-1,10,-6,5,-3,-5,-5,6,8,1,9,4,3,-10,10,6,3,-9,-10,-10,-5,8,9,-1,-2,-5,-8,10,2,-8,6,-6,-7,9,-1,-10,5,8,4,2,-4,8,7,1,-9,-2,10,3,4,5,-4,-4,5,-4,-3,-4,5,-9,9,10,9,-3,1,-8,-10,2,10,-3,-2,-3,-5,-2,-6,-1,-10,-2,-4,-10,3,-9,3,-6,-1,-9,10,-8,6,5,10,8,10,1,-5,8,10,-10,3,9,9,-7,-7,-3,-4,6,8,-5,4,-2,-8,-8,10,-5,-7,6,-10,4,7,-2,-8,6,2,4,-1,6,9,-10,-3,-1,-9,6,-10,-9,-8,8,9,3,7,-9,6,-8,1,-3,4,5,-8,5,9,-5,-6,4,8,9,9,-4,5,-1,1,-1,5,-8,-4,3,8,-10,-10,2,-4,-3,-10,9,8,-4,-1,4,8,10,-9,-5,2,3,-2,2,-7,10], dtype = "uint16")#candidate|6985|(234,)|const|uint16
call_6983 = relay.TupleGetItem(func_1618_call(relay.reshape(const_6984.astype('int64'), [189,]), relay.reshape(const_6985.astype('uint16'), [234,]), ), 3)
call_6986 = relay.TupleGetItem(func_1622_call(relay.reshape(const_6984.astype('int64'), [189,]), relay.reshape(const_6985.astype('uint16'), [234,]), ), 3)
uop_7005 = relay.log(call_6948.astype('float64')) # shape=(2, 13, 5)
uop_7007 = relay.log(call_6949.astype('float64')) # shape=(2, 13, 5)
var_7008 = relay.var("var_7008", dtype = "bool", shape = (6, 9, 16))#candidate|7008|(6, 9, 16)|var|bool
bop_7009 = relay.less(call_6954.astype('bool'), relay.reshape(var_7008.astype('bool'), relay.shape_of(call_6954))) # shape=(6, 9, 16)
bop_7012 = relay.less(call_6956.astype('bool'), relay.reshape(var_7008.astype('bool'), relay.shape_of(call_6956))) # shape=(6, 9, 16)
uop_7018 = relay.log2(const_6984.astype('float64')) # shape=(3, 63)
uop_7038 = relay.cos(bop_7009.astype('float32')) # shape=(6, 9, 16)
uop_7040 = relay.cos(bop_7012.astype('float32')) # shape=(6, 9, 16)
output = relay.Tuple([call_6944,const_6955,call_6983,const_6985,uop_7005,uop_7018,uop_7038,])
output2 = relay.Tuple([call_6945,const_6955,call_6986,const_6985,uop_7007,uop_7018,uop_7040,])
func_7043 = relay.Function([var_7008,], output)
mod['func_7043'] = func_7043
mod = relay.transform.InferType()(mod)
mutated_mod['func_7043'] = func_7043
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7044 = relay.var("var_7044", dtype = "bool", shape = (6, 9, 16))#candidate|7044|(6, 9, 16)|var|bool
func_7043_call = mutated_mod.get_global_var('func_7043')
call_7045 = func_7043_call(var_7044)
output = call_7045
func_7046 = relay.Function([var_7044], output)
mutated_mod['func_7046'] = func_7046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3862_call = mod.get_global_var('func_3862')
func_3863_call = mutated_mod.get_global_var('func_3863')
call_7066 = func_3862_call()
call_7067 = func_3862_call()
func_3982_call = mod.get_global_var('func_3982')
func_3984_call = mutated_mod.get_global_var('func_3984')
const_7071 = relay.const([[-1,6,7,-2,5,4,-2,-5,4,5,5,-1,8,-6,4],[-6,8,-8,10,-7,1,-2,-6,7,-7,2,-8,2,7,-4],[1,7,-4,6,4,-10,7,-7,-2,-4,1,-2,9,6,3],[-8,-10,6,1,-7,-7,9,2,6,-4,-3,-6,-3,-9,10],[7,-8,4,-10,-8,-9,5,-1,-6,8,-7,5,6,-8,-5],[6,-8,-10,8,7,-6,-3,6,5,-10,4,-6,3,-4,-6],[1,10,6,-4,-9,-4,-9,5,10,-9,-5,-10,-9,2,3],[-2,-1,6,4,4,10,8,5,-7,3,7,-7,10,9,-9],[1,-9,-6,8,4,3,9,7,5,9,8,-6,3,2,8],[-8,-5,-9,-3,-10,10,3,5,3,4,7,-8,-10,9,-4],[-3,3,-1,-8,-3,1,4,-5,6,10,-8,3,-10,-6,4],[3,6,5,2,10,-4,1,5,-6,5,-2,-10,8,7,-8],[-8,8,7,-1,-9,-6,-2,-8,4,9,-9,-2,-5,1,-8],[4,-10,-2,-8,-7,2,9,-4,-2,-2,-10,1,3,4,-1],[-3,-2,9,-1,7,-3,5,4,8,8,6,-2,9,6,-9],[10,1,-8,-6,-7,-9,1,-2,-3,-2,2,-6,8,10,-1],[-2,-3,-2,5,-10,-2,-3,-4,9,-5,8,-8,4,2,-9],[-2,-5,-6,-8,7,-3,10,2,-1,1,2,5,-4,8,-10],[-10,-10,1,-1,6,8,7,-3,2,-1,-10,-10,5,-2,9],[-1,-8,3,-8,-8,-4,-2,-6,1,-9,-9,-7,5,-3,8],[1,-1,10,-8,-8,-3,-5,-3,-9,7,9,10,6,-2,2],[-1,9,2,5,8,-6,-6,-5,2,-3,6,6,2,9,1],[1,-4,3,10,8,3,-10,-7,-8,-10,7,-5,-2,-4,-10],[-2,-6,-1,-4,9,10,8,-1,-6,-5,9,4,6,2,7],[-5,-3,5,2,-7,-5,-2,-9,-9,1,-5,5,-6,-5,1],[10,-9,8,7,7,-10,-2,-5,-5,-8,-8,7,-2,4,-3],[7,2,-6,-2,-10,-6,-3,-3,1,-5,-4,-2,6,-6,-3],[-7,2,-8,2,1,1,4,-8,-2,-9,-8,10,6,5,-10],[10,-1,-9,-9,9,4,-7,-3,9,4,2,1,-1,10,8],[6,-7,10,-4,-8,-1,4,-3,3,-2,-8,-6,-6,5,-6],[-6,-10,-9,-1,-1,7,-1,10,-8,6,1,-4,-4,-5,-8],[1,-3,-1,5,-7,-2,8,7,-9,-4,-9,-8,1,5,2],[-9,9,6,-6,1,7,10,-7,7,6,-1,-4,7,-3,-3],[6,-8,6,7,4,5,-1,9,4,6,-7,2,-5,9,1],[-3,-6,2,-4,1,-6,1,1,-7,-6,-4,9,-4,-5,2],[-5,-3,-7,-2,-5,-9,9,-10,10,5,10,6,-5,4,3],[4,-3,10,3,1,3,6,-9,-2,4,4,-9,5,-3,4],[7,6,6,-9,6,-4,1,-2,-8,1,6,-8,-6,-8,2],[-6,9,-6,-6,3,-7,4,7,-8,2,7,-5,-10,-7,-1],[-10,5,-7,-6,10,-8,6,-4,-7,8,-4,-5,1,9,4],[7,6,-7,7,-7,-3,-3,-6,2,1,-3,6,-1,3,-6],[-1,3,7,10,3,10,-4,-5,-9,-6,-6,3,-6,8,8],[8,-7,7,-1,7,-6,-10,-7,3,-9,-6,9,-6,8,4],[-7,5,3,9,9,-10,2,-7,4,-5,-2,-9,-2,8,10],[-6,-6,3,5,5,-8,10,6,9,9,4,-6,-2,9,-8],[2,10,-7,7,-4,5,-9,10,-2,5,2,3,-4,6,-5],[-6,10,-6,6,-8,-8,-2,10,2,10,3,9,-2,1,8],[-2,-6,8,-1,7,-9,-6,2,5,-6,-3,9,-7,5,-8],[-5,-7,5,2,4,-7,4,3,9,-2,-3,6,-9,2,10],[-8,10,-5,-3,-3,6,-1,5,-6,2,-9,-7,10,5,-9],[-1,9,2,-8,-3,-3,3,7,8,2,5,8,4,7,9],[6,3,-5,3,2,-6,-3,1,-9,-7,-2,10,-4,7,6],[7,9,-1,-5,-10,8,-5,7,3,8,6,-2,-9,1,-8],[-5,-10,5,1,-4,8,-8,-5,3,-10,-9,9,3,10,6],[-2,2,-7,3,-6,8,-3,9,1,5,10,-10,-5,-1,-6],[2,-9,-9,-9,2,-3,1,7,3,1,1,-2,-4,-3,-4],[9,-6,10,5,-2,-7,9,1,8,-4,-2,2,-6,-2,9],[-8,2,9,1,-3,2,10,-8,7,-4,4,-6,1,3,2],[7,-2,-6,-1,6,-2,4,10,-4,7,-8,6,-9,9,-8],[6,1,-4,-1,-5,-9,-7,-10,6,-4,2,3,-7,4,-6],[4,-8,8,-3,-9,7,-5,2,9,-9,-8,-4,-10,-5,6],[-7,-3,-7,-6,-1,-9,2,3,9,-9,-7,-1,2,-4,4],[-10,10,5,-4,10,-6,4,-2,2,-10,-10,-2,8,2,10],[-1,6,-4,1,-10,3,-9,-5,-3,2,10,10,3,-5,-1],[-1,-7,-6,-6,9,9,3,7,8,-7,-5,4,-10,-3,-2],[-1,-7,-9,-9,3,2,-10,-1,-7,8,9,2,7,10,10],[-4,-8,1,-5,4,-10,9,5,6,-9,7,-6,-3,2,4],[-9,5,9,-7,-8,-10,9,-6,-1,8,7,-10,-4,-7,-8],[2,-7,-7,3,-1,-4,9,2,2,10,-3,-5,1,8,10],[8,5,9,4,-7,4,5,9,-1,-1,10,7,9,-7,-5],[-4,8,-8,5,-8,-6,4,-8,-9,1,-1,5,8,-5,2],[-1,2,-10,-6,-4,-5,-9,-4,-1,7,4,-5,-5,5,-8],[-9,-5,-8,-5,10,-1,2,6,-10,-8,1,2,-10,-10,8],[-4,-9,-9,-8,3,4,2,5,-1,-5,1,-8,3,-1,-5],[-3,5,-1,-8,9,-6,-3,-10,-4,-3,-9,-6,-7,-6,-2],[-7,-1,-6,7,1,3,-2,6,9,4,-1,-8,9,-6,6],[-6,-4,5,9,-3,-1,-10,7,6,5,7,2,-5,-1,-6],[10,9,-8,3,10,10,4,-4,-5,4,2,-8,-7,7,-3],[-6,-4,-6,-1,10,6,-1,-3,3,9,9,-9,8,-9,5],[-6,6,5,-2,4,-8,-5,3,5,-5,-3,6,1,-9,8],[4,-6,6,4,-8,2,-9,4,-3,7,-5,-2,2,6,-4]], dtype = "uint8")#candidate|7071|(81, 15)|const|uint8
call_7070 = relay.TupleGetItem(func_3982_call(relay.reshape(const_7071.astype('uint8'), [1215,])), 2)
call_7072 = relay.TupleGetItem(func_3984_call(relay.reshape(const_7071.astype('uint8'), [1215,])), 2)
output = relay.Tuple([call_7066,call_7070,const_7071,])
output2 = relay.Tuple([call_7067,call_7072,const_7071,])
func_7077 = relay.Function([], output)
mod['func_7077'] = func_7077
mod = relay.transform.InferType()(mod)
output = func_7077()
func_7078 = relay.Function([], output)
mutated_mod['func_7078'] = func_7078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mod.get_global_var('func_3833')
func_3835_call = mutated_mod.get_global_var('func_3835')
call_7088 = relay.TupleGetItem(func_3833_call(), 0)
call_7089 = relay.TupleGetItem(func_3835_call(), 0)
output = relay.Tuple([call_7088,])
output2 = relay.Tuple([call_7089,])
func_7100 = relay.Function([], output)
mod['func_7100'] = func_7100
mod = relay.transform.InferType()(mod)
output = func_7100()
func_7101 = relay.Function([], output)
mutated_mod['func_7101'] = func_7101
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7122 = relay.var("var_7122", dtype = "uint16", shape = (13, 8, 1))#candidate|7122|(13, 8, 1)|var|uint16
var_7123 = relay.var("var_7123", dtype = "uint16", shape = (13, 8, 10))#candidate|7123|(13, 8, 10)|var|uint16
bop_7124 = relay.less_equal(var_7122.astype('bool'), var_7123.astype('bool')) # shape=(13, 8, 10)
func_6633_call = mod.get_global_var('func_6633')
func_6635_call = mutated_mod.get_global_var('func_6635')
const_7131 = relay.const([5.135300,0.059974,6.973325,-9.256692,6.366093,-2.513954,8.323970,2.430284,3.111286,3.453372,7.735744,0.276394,-6.076545,-7.606631,8.089520,0.846586,-1.314578,5.111566,-1.830006,9.421119,-7.987734,-2.482799,4.322814,-2.292584,4.886929,4.031734,-0.499432,-4.904283,-6.169912,-9.503355,-3.010594,0.444411,-3.978178,7.096021,-6.174616,1.751649,-5.035581,8.661537,9.697527,-0.915794,8.350488,1.427980,-1.568208,-2.195248,7.154317,0.257952,-7.505145,-2.405488,1.211543,-8.453471,-6.738278,6.344313,8.261431,-9.349281,-6.440454,5.581665,-1.671201,2.182615,6.417789,-2.409058,8.548473,-1.469160,-9.802345,-2.149775,-0.474387,8.755527,-4.795874,-5.384916,0.313062,-7.469160,5.111577,-9.556066,5.902730,4.703752,2.794419,2.194125,2.541061,2.887259,-9.482205,0.172134,-2.606276,9.464569,8.998217,-5.432676,-9.436990,5.863605,4.543343,-3.802415,6.690348,6.118979,6.613808,7.308053,-7.786349,-7.332741,7.309487,-6.218409,-2.883834,-4.505799,0.060342,0.633529,-1.380134,9.886505,-9.394671,-1.812523,5.566338,-2.076820,-3.005599,0.223583,-3.185981,2.048797,-0.118659,1.119241,2.863800,-2.791602,6.189155,-0.987213,-2.876802,5.520060,5.606539,2.787998,9.488285,5.519299,4.544098,-2.279562,-4.189274,6.208954,6.796553,-0.198807,4.726333,7.418540,-5.678963,-8.800731,-5.521940,7.548792,2.279937,-6.695101,-1.904752,-4.260207,0.304553,-1.129940,-4.272346,-9.554149,-7.365935,-7.740287,3.758285,-1.598640,0.511556,4.967307,-8.822282,-6.106135,4.585179,-0.050271,-9.379616,2.366450,-7.166771,-7.758965,-1.984379,-7.985783,2.598555,-2.975591,1.239953,-8.081637,9.939161,-8.839644,-6.174423,2.674915,6.663524,1.196369,-6.262159,6.945074,-1.738792,0.560215,-4.285709,-0.039834,-9.933856,5.094952,0.273410,-9.146876,8.866639,9.548150,7.987123,6.632451,-1.947239,8.079078,0.671251,0.274116,-4.041111,-6.296391,9.475279,-4.009042,9.732735,0.263218,7.692964,0.225577,-7.602079,-1.808323,1.778955,-5.872067,-6.160346,-8.980479,0.474074,-6.699192,-6.520383,-1.706672,5.396831,2.207415,-3.319233,5.931859,8.019965,-0.417595,0.263100,9.661057,-0.089030,4.209682,8.658481,5.981794,0.091648,-6.940198,-6.187111,4.591305,7.387980,4.390600,1.502321,7.526698,5.964269,-8.257793,-0.647330,-6.735691,-6.645515,-2.419240,9.055450,-1.733213,0.194632,8.254694,2.946992,6.970014,0.106152,3.850310,8.339780,4.738831,-5.638088,-3.960046,-9.810641,-3.906801,-8.701692,-5.382999,-0.041767,-2.444786,-9.975530,9.520053,0.588836,-6.659382,0.535019,9.230641,9.858284,-5.164187,9.693173,-6.084344,9.670780,-3.821026,1.980952,9.221588,4.716321,5.459367,7.864966,1.932076,1.359485,-4.453062,4.805189,-4.472886,-9.685983,5.954265,7.899997,1.295022,-9.941855,-2.434915,0.864718,5.044053,4.069489,-2.706025,7.330722,3.565856,8.552537,-1.826098,-8.587918,0.782722,4.995488,-1.582474,8.393181,4.320146,0.882700,2.249706,0.171760,2.552389,-5.906167,-7.064608,3.189329,-8.273129,2.462793,-7.192414,9.329720,-1.409553,-2.423179,8.270338,1.629811,2.780830,-1.289156,7.812225,1.534534,1.875721,-2.916210,0.406884,0.610677,-1.271110,-2.603132,-4.098043,1.648047,-8.558055,2.997052,3.945446,-7.660423,1.841025,7.535970,3.741059,0.144489,-0.489959,-4.452927,-6.529656,-3.449683,-1.792395,7.800560,-0.551904,9.449116,-6.062946,3.245816,8.362702,-2.152471,-2.012418,7.182722,-9.728607,-4.622452,-4.703954,-7.568615,1.964891,-1.089746,-7.299942,-0.520269,-2.451399,9.385448,7.783766,-3.351728,3.600049,9.619790,-2.655468,4.814471,-4.566478,-3.794911,-4.841668,6.067578,1.562738,6.421643,0.926009,-9.612655,4.105249,-7.245151,-4.842841,-3.803420,9.309290,-5.129876,-8.448908,-8.522933,1.269966,-4.698672,2.632354,1.386283,5.660852,-4.725397,3.142906,-7.084180,6.529996,8.723055,8.937110,0.317293,2.432531,-7.418817,2.554353,-6.294908,3.079819,-2.383998,-0.728020,4.351278,-9.711794,-1.144122,5.705171,-3.094422,9.831300,-2.763707,3.075753,7.995140,4.383603,6.252062,-5.961601,-8.434607,-8.575317,3.785455,-3.521977,-5.427992,-7.986477,-8.495950,8.368970,-4.234040,-0.505097,2.886127,-8.436939,1.967307,-2.769798,-4.948869,-4.231431,5.259463,3.942274,-3.824201,5.158299,-2.844937,4.407075,7.176136,-4.680827,-6.682364,0.873453,-9.251269,-6.627014,4.061473,-7.336437,-5.935153,-9.320836,6.332601,-9.188726,-0.221298,-9.389817,0.925060,7.250913,-1.528109,4.391380,7.564767,-5.041034,-6.412568,0.809981,-6.628697,-4.635156,-0.604237,-6.278511,-5.030857,9.978577,-1.261779,-2.567924,-9.486885,7.684499,7.600728,2.590024,8.890993,-4.367412,-0.466499,6.565951,-4.252228,1.996918,9.497453,-1.219790,-3.079185,-1.405386,-8.882447,5.338640,-8.621377,2.593663,5.880185,-4.455777,0.151807,-9.775236,-2.405144,-4.295652,0.605757,-4.846381,4.581189,8.815692,-9.577066,-1.781206,-2.549873,2.839092,-3.957311,-0.001856,2.993145,-9.719719,9.566678,8.746905,8.487295,-1.449142,1.312892,3.008083,-6.582061,5.029021,-7.019306,5.910324,3.511460,2.837403,7.523437,5.636706,3.836487,0.871924,-1.826528,-2.214164,-6.305700,7.056181,2.244786,-6.070546,7.693141,8.697816,-6.700208,-8.420552,5.243953,9.997221,3.576574,-2.652441,2.619392,3.703517,-4.570909,8.824853,6.751124,-7.447067,3.384545,-1.307647,-1.070768,-4.796155,-0.496280,-8.367859,-8.559840,-9.658215,-2.597297,-4.832703,2.621412,-7.798639,-2.893379,-6.221461,-9.664210,-3.723086,-3.842616,-4.053745,-8.766909,0.838927,6.294398,6.776326,6.041709,4.962434,-1.097496,8.452901,3.143848,7.207969,7.002676,2.033549,-8.317402,4.336825,-4.218427,-3.730399,-1.196945,3.363436,7.190556,-9.068400,6.638569,2.380575,0.174367,1.374228,-4.590220,-0.389493,-6.148013,8.785131,-4.876703,5.011817,-5.229789,2.994973,5.373144,-7.571926,6.354008,-9.852834,-8.224279,-7.054774,-5.191823,-9.284342,-0.921629,7.004183,1.678840,-2.718395,5.092844,-4.002540,4.573019,7.578044,6.405611,8.597462,-1.664692,0.452286,7.601660,-7.181755,9.645919,-2.502831,-3.853450,-1.943401,-4.047627,1.385070,4.552065,2.054332,2.989949,6.656818,-8.314206,-1.438355,-9.573000,5.031325,7.804977,-6.057447,7.446243,9.491244,-9.598649,5.767639,-9.463638,-4.057755,-6.160794,-2.969910,-5.520454,-3.752286,-5.676442,0.507002,-7.730818,4.781649,9.481889,-8.416262,-6.984481,-1.125592,-0.358047,-0.968172,-4.171052,-7.478314,-5.198114,-7.276346,-1.943809,-1.660453,6.762965,-2.374749,-2.782234,-5.381105,0.416176,-2.355470,-6.969241,-1.653675,-0.947957,3.153431,9.186609,-2.066454,-9.516209,0.867846,5.095293,3.835202,4.485881,3.339868,7.175046,2.609481,-5.835971,0.787446,-0.490592,4.907010,-0.909689,3.719866,-0.376559,5.502002,8.496430,-6.197192,-4.044475,8.693737,8.266733,-0.410773,-0.974823,7.822479,0.138814,8.606740,-3.950694,1.552423,5.726751,-1.621363,-1.831702,-7.675204,-3.113027,-8.905611,2.106840,2.644936,-1.545474,9.718440,6.380928,-4.859900,0.325655,0.554943,-8.562025,-6.513591,3.968007,-2.067331,4.339846,0.195658,5.313379,-1.429897,-6.612738,4.006177,5.967000,5.989430,2.293191,-5.859521,-5.345939,-2.518652,-8.903824,-2.880138,4.951558,7.802053,-5.240958,1.840922,-7.805176,-1.317070,7.847763,-0.432842,-8.578040,2.045424,4.710292,4.681342,3.030524,-9.022821,-9.262451,-6.844525,6.394348,-2.355147,-7.136948,7.146798,-0.412735,8.344523,3.873183,-5.536034,-2.491590,5.101410,3.268813,2.350391,-1.737254,-0.646057,-8.869842,6.347557,-3.975520,0.589241,1.772760,-5.902063,-1.121694,9.530704,9.555150,-9.014430,3.016338,8.259705,-7.511951,-3.859394,-4.190324,1.019005,7.964150,0.448248,3.865083,-0.426805,3.879198,-6.160065,2.860606,-9.876666,1.085225,-1.061981,-6.744592,-0.234902,-7.511502,-2.501922,4.489116,0.069906,-1.617338,4.038143,-0.074101,-4.972697,-8.161385,9.435858,-4.549390,-8.484617,-1.824823,-1.904588,-2.552723,3.667319,3.470348,0.475575,-5.577898,6.272163,3.889047,-5.251347,6.697855,-6.412694,1.731317,6.060467,3.695953,6.723139,-3.018962,-0.992907,-6.229905,8.460229,7.241395,3.649759,7.479030,-3.599495,3.947121,-1.964226,4.704110,-8.549748,5.164035,-9.876444,8.722401,-3.081498,-4.973517,-1.184608,0.195126,-5.858302,-3.798014,-6.080259,4.292918,5.171618,2.025030,3.512450,-3.504134,5.972638,0.643045,-0.158359,3.361142,-7.273254,8.135562,9.516363,-7.763167,-4.057697,4.463970,-0.084675,4.697619,2.332343,-0.664267,-3.835813,-2.929051,-8.535225,2.180339,-3.406424,4.991143,-7.744187,3.475566,1.584036,-1.614527,-3.313198,-8.146451,-6.442533,-8.441594,-6.916325,-4.283961,9.576355,-6.003609,-1.402093,-7.595665,2.456991,5.715671,8.755193,8.170939,-5.889910,-7.005139,0.205227,2.260511,-9.272716,2.334135,-3.488824,6.295920,-5.290897,8.301173,-4.372140,3.583766,-2.996598,8.875537,5.820139,-2.304170,-4.705120,-3.975401,-5.156747,6.565894,-2.727222,6.202069,-8.930045,-9.176036,5.425899,3.468660,-2.643248,0.471821,3.307164,-1.726124,2.253367,-2.311948,3.689038,9.194525,1.358446,-4.183085,8.582197,-7.278397,2.160886,-3.303558,1.128753,-2.344987,-7.428491,-2.848629,-9.582075,-2.033119,8.092924,-2.909624,6.972648,-6.728589,-2.351955,-1.183322,7.194992,-6.424481,-4.450428,3.332943,-2.940091,7.668993,4.866174,3.508103,-2.746741,1.158365,-8.435506,-8.638189,0.908644,-4.060232,2.748812,9.335708,-1.358288,9.738257,-0.381500,-3.969659,-9.688422,3.030564,7.357467,-4.743936,-0.774981,4.459141,4.112439,-9.444204,8.829230,-7.356777,-6.165651,7.694777,7.428574,5.710116,9.626271,0.201679,3.108473,4.906178,3.495054,-6.619992,0.293698,-9.107361,1.999119,2.864065,-5.974963,9.948350,1.561497,5.205493,-8.159838,-6.653295,-6.790983,8.482619,-8.929225,-5.997919,-9.780811,5.712628,-4.572718,-4.983989,-1.688573,-1.669875,-0.230490,5.593166,-5.183589,-9.961368,3.118764,-8.097977,-7.512724,2.857487,-2.702925,-9.727410,-7.370547,-5.125844,-5.096099,-3.957215,-4.189943,7.907108,6.635082,-7.885116,3.511602,-4.045313,8.504970,-4.281290,-4.007090,-1.528262,9.127290,-8.846810,-8.946687,-5.006317,7.578833,-3.934014,-3.129900,-5.214380,-7.435311,3.855189,-0.283309,3.629741,6.150885,1.473461,0.671003,-4.789782,6.835075,4.327619,-4.250311,-0.774709,-0.796500,4.712808,-3.238950,-2.468587,6.402190,-5.221046,9.331155,1.241920,3.270436,6.144325,6.990032,0.892041,-2.059928,-8.589318,-0.496967,-7.402384,3.042995,2.343111,-4.735994,2.834955,-7.868838,7.039175,6.852502,-1.462886,0.711468,8.353066,0.742137,5.834424,5.729654,-3.315695,-8.818960,2.102764,3.138218,4.884328,-8.499366,1.503317,-5.477814,0.488961,5.706382,-7.096879,7.087819,7.405525,-4.965131,-0.311522,4.225700,-7.238646,3.627639,5.262573,-7.922678,-1.057455,1.951186,5.027656,-2.055241,2.107411,-9.082209,2.036352,-9.009980,5.520723,5.687796,-1.156681,-0.542915,6.929111,-3.577026,-1.304391,7.112031,-6.081973,-9.480620,7.282017,-8.191111,1.281058,-1.799502,-3.668112,2.254149,-0.743896,3.734189,1.092525,3.739628,6.028969,-3.637928,-6.226466,9.922776,-0.395713,1.271895,-7.506063,3.468324,-4.141195,-6.273890,-2.938586,-6.136278,9.746679,5.856217,-4.871470,9.631565,5.222544,0.054283,2.882564,-8.558898,1.303830,5.578563,4.286352,7.186234,7.507581,-6.752951,3.517865,-3.522889,-3.408358,-7.118298,-5.202221,-0.929913,0.492849,0.020697,-3.620019,-1.615915,5.151185,-1.162441,-4.386561,8.143878,4.861277,4.206861,-9.580488,8.831110,-5.701973,2.673595,5.350727,-2.795258,-0.936084,-4.725437,0.329956,-9.052517,-5.770656,7.216791,-6.737348,-6.994852,-6.614192,-8.062166,3.036975,3.803614,6.890310,-7.093653,-2.653598,2.455836,9.631864,-4.436890,2.957191,3.596522,2.362675,-3.646466,9.286839,7.141844,7.227638,0.559611,-2.259852,-0.221614,3.627938,-2.268824,8.775089,-8.490438,6.317743,9.312249,1.250282,4.943303,9.895261,-1.135184,-8.581734,-6.739913,-6.714305,8.445600,-7.827350,-7.414362,-8.438881,9.032625,0.477973,-2.178413,-4.785601,1.859396,1.109643,-5.556411,-5.510471,5.040615,0.166851,-6.562215,6.327700,-8.245198,9.269026,-9.686207,1.788719,1.824347,0.962303,-0.620585,5.406573,-5.837148,-6.677157,7.445229,5.877391,7.905486,-0.008541,-2.824180,5.875816,7.286200,-6.853308,3.820724,-4.742469,-5.086212,-9.362657,1.877425,-4.469204,-6.376075,2.439157,7.109250,7.255501,9.214582,7.264213,2.962977,-1.170253,1.365786,-8.292140,-6.725394,-3.115838,8.583974,3.405888,-0.793202,-8.221726,-2.673121,4.486205,-1.448391,3.337040,-0.785809,-1.449725,1.272003,7.784607,9.981179,6.916023,-7.189937,-2.297505,8.494819,-4.310883,6.024011,-6.367082,-5.001930,2.449870,-0.120489,-1.518030,5.082632,6.525489,5.324892,-8.408130,-9.486782,6.048480,2.387229,-4.430546,1.691776,-0.513216,0.883772,3.979438,-5.092055,2.248840,1.837330,-6.839551,-5.648841,6.549334,-3.496280,-3.620552,-9.418968,4.137799,2.416051,-8.252444,-1.576499,7.579356,5.927131,-5.290949,2.753183,8.141180,2.411394,-2.627249,3.093110,-6.910589,4.215904,-8.294096,-5.607053,0.488796,-5.073291,-0.433156,-9.833925,-3.079474,-5.617381,-7.435756,-0.538589,-2.003965,7.386277,2.402560,7.551471,-4.477770,-2.947038,-5.853309,-2.929946,-3.823309,7.858698,4.432228,-4.528898,8.455796,-9.392767,0.977214,7.066364,9.322917,-6.934167,1.962259,-1.055896,-3.877738,8.479992,8.125169,-4.691270,-4.601994,-1.638784,2.528260,3.986310,-8.648544,-0.731664,3.860334,0.690271,-1.218418,8.332735,8.227365,1.063785,9.215847,-1.484720,-2.309342,-5.863528,-9.223929,9.944947,-3.256685,7.315862,-4.331399,-3.178986,6.339295,-8.413742,0.587267,-6.446380,0.441123,-1.790032,-2.050791,1.266576,2.909664,3.199061,2.134229,5.132941,6.825342,-8.557561,2.645087,1.887959,-0.946061,-6.796066,-6.360896,7.418336,2.821710,-6.288677,-2.005537,-8.583295,6.762805,-3.779617,-2.933746,-7.838830,-4.403532,-9.598631,1.757643,-1.837451,6.949515,5.480779,6.742061,-3.778919,-9.430206,-9.045579,-3.131328,-4.430579,-6.348302,-1.194898,7.375662,4.636097,2.238891,8.598787,7.716181,2.819524,-2.629446,-3.365758,7.503579,-8.817253,3.970612,-5.173360,-7.395044,-0.245261,6.384309,8.805731,6.677383,-1.380082,-5.227733,-2.191110,-0.490109,3.809765,-2.553840,-6.179464,-6.165037,-4.661470,-0.441867,1.262179,0.367100,3.093226,4.600874,7.322017,7.058625,3.084566,9.057521,-2.837852,0.626966,7.649709,1.027236,0.026486,-7.884278,-5.694040,5.407787,8.500193,3.787098,1.726412,-6.409280,4.960343,5.974410,4.265880,-8.785525,-8.804829,0.586930,-9.284601,2.033083,-5.263149,7.194931,-9.205553,2.919178,8.944424,5.766577,1.308390,-2.598835,2.695509,2.443017,-6.572105,-4.338412,-2.055807,-4.129031,4.168174,-7.484926,-7.524280,-6.912371,-4.993288,-6.151256,-6.203265,2.634562,3.101562,-7.650885,4.304743,-7.555387,-6.465131,-4.958186,-1.072713,9.560728,-3.059582,-6.263019,3.706250,-3.104570,-0.080889,7.803427,-9.720601,-0.427116,-4.608646,-4.480980,-9.490156,-5.582443,-8.157011,5.776114,3.706337,-2.738079,6.379290,-6.291910,2.837776,-8.126653,-8.063348,-1.193802,-5.371996,-6.886331,3.576034,-0.461839,5.594341,-7.711454,4.603097,6.484098,-7.996355,2.432995,-8.454235,-5.231459,-5.342978,9.727323,9.094826,6.860973,-3.045712,-4.168342,-5.136521,5.571220,6.605749,1.406513,-5.769001,-2.549538,-7.286614,-4.765063,5.340960,-6.678207,3.087864,-9.214971,4.586929,7.251821,-2.627239,-3.864345,-2.022346,-8.824737,4.867704,7.749532,-8.617022,4.808320,0.981024,0.044454,-5.170724,-7.812690,7.779486,-2.152022,-9.929589,-5.634612,-2.901019,2.368033,9.683799,-7.770829,-2.545898,-6.359076,8.768209,9.970707,4.220531,-8.997943,4.819427,0.844090,6.023306,3.287772,5.334313,-9.552098,-0.617897,6.076933,-5.349069,4.303051,0.391968,2.514670,4.368810,4.472176,-8.290802,-5.269840,-5.350653,-9.139821,-2.707741,1.266134,-1.602586,0.559606,5.838403,-9.193716,-3.720660,-2.779270,2.631907,4.528794,7.029992,1.977377,-5.434182,5.319319,7.164185,-6.025575,5.283674,-2.102648,-3.156210,0.623862,-6.721416,2.103728,9.177011,-5.778467,8.055154,0.535856,-1.294146,-5.593467,-9.464315,6.214955,-2.702403,8.112839,8.232487,4.595499,7.588075,0.819093,-4.407212,7.075927,6.680003,-4.354623,4.847099,2.156922,-8.900694,-2.133332,5.989932,-7.071885,0.061348,2.554758,4.713203,-9.945765,2.708015,-1.628041,-6.594916,1.834248,0.821682,2.813225,5.799156,-9.249897,-9.936738,1.907736,-0.389683,4.043900,0.650576,-8.852313,2.748851,-2.445741,0.922126,-6.618725,-6.472096,8.046545,9.327302,-9.473914,5.300984,-9.255781,8.618267,6.433780,-9.663181,4.183317,9.238266,-7.801684,9.472240,-9.825308,-3.258087,-8.426333,-8.813148,-4.141660,-0.918100,0.703176,-4.006958,-5.684936,2.720627,0.027169,-2.002477,3.334193,7.397267,6.787852,-5.690868,1.493988,-5.946145,0.947398,9.234380,0.777531,-7.163753,7.179208,-2.935037,-4.349693,3.655640,7.583462,5.652716,0.642937,4.514545,0.421311,-4.315388,-2.810222,-1.793401,-0.949402,6.417310,-7.147757,-0.607357,-9.877217,9.393515,-3.052671,4.131302,-4.530096,-2.860522,9.673332,-0.950910,-9.531021,4.982358,-0.829929,-0.942262,0.084886,-6.655265,-1.140897,0.056550,0.933687,1.044497,8.069647,-1.666123,7.479210,7.861190,-6.386464,7.731110,3.910541,0.737361,3.413805,-4.678426,1.729120,-0.320701,6.600747,9.231199,-1.445192,-0.828673,1.756905,9.801063,3.112946,1.701659,6.155259,-3.097926,0.946911,-4.852863,-5.283415,5.771494,0.162623,1.455844,5.816787,1.408946,0.241592,7.588147,-4.583120,-8.556287,3.857520,6.180947,-2.442781,7.407540,9.322059,-7.671698,-9.130939,-8.854161,7.493669,-3.294678,-7.331109,-7.121430,1.662237,-3.219052,0.554270,-7.297679,-0.063293,9.044056,2.311856,-8.109300,-9.058427,-9.188055,-1.565250,-7.265559,-3.522128,-3.780276,-0.893972,0.851157,-6.828239,-7.003042,-5.385316,-9.997409,-2.747910,8.777565,3.476654,2.558201,4.701073,-0.072477,-0.647618,2.545907,-3.323534,3.033145,5.189635,-6.956906,-1.622874,9.650748,6.203705,4.768946,1.206704,-4.553593,-9.677890,-5.831634,7.704580,6.847036,6.710960,5.976122,-8.262317,-1.831426,3.865331,8.152087,4.779812,-8.049421,-8.718227,9.738360,-8.853902,-4.937937,5.739884,-4.471541,-2.188771,-8.805464,6.067360,6.085669,-8.307515,8.789086,-9.387269,5.180553,1.592667,8.527087,8.469633,9.775846,-3.868103,-1.893761,-2.722531,-7.399582,-7.918170,-0.632497,-9.006323,5.671326,8.373019,-8.663491,8.485960,-2.534920,0.449106,-0.896333,-0.958556,6.982366,-9.422812,-8.534104,-4.540666,0.546110,5.575742,-2.854158,9.168309,-2.109548,-0.574565,-7.892748,-1.281397,-9.232398,-9.416321,-3.846833,-9.401088,9.462472,5.206453,6.870826,9.457102,-3.062975,-7.339887,-5.773429,-9.197495,4.404581,-9.850480,-3.867549,-6.408252,-9.699869,0.936695,7.330920,-8.797014,-7.298116,-8.050149,-4.580861,-9.618819,-6.984964,3.733270,-7.367973,0.596220,3.326589,-1.583000,-7.564593,-3.143795,0.888054,8.099026,-6.566854,-9.200360,9.441783,-9.938871,-3.787686,-5.567331,-9.398659,5.606631,8.033123,-0.339826,-2.864224,-4.110892,6.427780,-8.535543,-8.547388,9.715311,6.828489,-0.020166,-8.542587,-8.913492,0.916600,1.305948,7.589395,4.883143,2.111998,4.068976,-0.186876,-3.608871,-0.617413,-0.891646,-9.604128,9.886600,7.580663,-2.650831,9.444964,-4.230705,0.951637,-7.934819,2.939817,6.432207,1.149498,-9.132405,-6.568597,3.887819,0.297559,3.439737,4.410904,-1.201024,-4.566702,-0.576967,9.150435,6.113628,-4.560570,6.232199,1.654485,-3.180615,3.015013,-3.958035,4.604011,2.430346,0.935913,-6.933669,6.317546,-7.268032,8.314086,7.330994,4.990881,2.977590,-7.887761,6.436036,3.089407,-0.520981,6.274973,-1.203011,-9.612590,2.295080,-1.199475,-7.938911,-3.219087,-2.323248,6.510983,1.369148,-5.549596,-3.422544,4.652288,-7.468549,2.430479,-1.785337,1.494287,7.598162,-9.180311,3.558634,-9.503495,-5.879230,-6.678185,-9.925915,1.082235,8.376460,-0.383008,-0.544973,1.413373,-2.520570,-1.059561,9.141603,5.851730,5.331964,-4.900314,2.945394,7.215423,4.661103,-2.673469,3.811769,3.588581,5.201784,0.939583,-7.526317,-3.966605,4.907294,2.290154,-2.092641,-2.866458,-0.025459,-5.356227,7.795646,3.428777,-1.642886,0.090861], dtype = "float64")#candidate|7131|(2016,)|const|float64
call_7130 = relay.TupleGetItem(func_6633_call(relay.reshape(const_7131.astype('float64'), [2016,])), 2)
call_7132 = relay.TupleGetItem(func_6635_call(relay.reshape(const_7131.astype('float64'), [2016,])), 2)
func_6857_call = mod.get_global_var('func_6857')
func_6858_call = mutated_mod.get_global_var('func_6858')
call_7139 = relay.TupleGetItem(func_6857_call(), 0)
call_7140 = relay.TupleGetItem(func_6858_call(), 0)
func_5211_call = mod.get_global_var('func_5211')
func_5214_call = mutated_mod.get_global_var('func_5214')
const_7142 = relay.const([-7.763962,8.327251,-2.781361,6.367218,-2.750409,-0.985853,6.516775,0.467821,-5.088976,6.940920,9.916268,-0.211915,-5.271932,9.614559,-0.556244,6.225800,7.587440,-4.826240,5.626216,2.749280,-5.376721,9.283575,-1.977314,-3.291577,-7.141957,-0.346296,6.687156,9.301767,-7.853359,-8.414453,8.987904,1.224259,-0.940578,0.058167,-8.068399,2.403457,-9.243677,-0.513385,2.725914,7.273364,-6.231181,-3.051262,-7.410629,7.563137,-8.600674,9.360107,9.638009,-2.672812,-4.150410,5.084538,1.145226,6.749190,4.214353,-7.137012,-5.201180,5.994292,-5.360068,7.228921,4.513521,1.120897,-7.830727,-8.283439,8.578968,9.903563,-7.007705,-0.788396,6.811862,4.113346,8.333414,-9.703144,9.926707,-1.455849,6.773519,-8.199501,-2.578385,-7.475485,-3.477768,-8.980075,1.518698,-1.175718,-6.579545,9.353896,-8.728187,5.360463,4.873218,-8.476699,0.064805,-0.887889,-0.059993,1.448800], dtype = "float32")#candidate|7142|(90,)|const|float32
call_7141 = relay.TupleGetItem(func_5211_call(relay.reshape(const_7142.astype('float32'), [5, 3, 6]), relay.reshape(const_7142.astype('float64'), [5, 3, 6]), ), 1)
call_7143 = relay.TupleGetItem(func_5214_call(relay.reshape(const_7142.astype('float32'), [5, 3, 6]), relay.reshape(const_7142.astype('float64'), [5, 3, 6]), ), 1)
bop_7147 = relay.bitwise_xor(const_7131.astype('uint16'), var_7122.astype('uint16')) # shape=(13, 8, 2016)
bop_7155 = relay.bitwise_or(bop_7124.astype('int16'), var_7122.astype('int16')) # shape=(13, 8, 10)
func_4478_call = mod.get_global_var('func_4478')
func_4481_call = mutated_mod.get_global_var('func_4481')
var_7171 = relay.var("var_7171", dtype = "float64", shape = (182, 1))#candidate|7171|(182, 1)|var|float64
call_7170 = relay.TupleGetItem(func_4478_call(relay.reshape(var_7171.astype('float64'), [26, 7])), 1)
call_7172 = relay.TupleGetItem(func_4481_call(relay.reshape(var_7171.astype('float64'), [26, 7])), 1)
func_1047_call = mod.get_global_var('func_1047')
func_1049_call = mutated_mod.get_global_var('func_1049')
const_7179 = relay.const([-3,7,-3,-10,-1,-6,-2,7,-10,-8,-8,-6,4,8,-3,3,-5,10,7,5,-4,-2,-5,-10,-9,-2,9,-1,-1,-4,8,-10,8,-3,10,7,-10,-4,-10,-1,-1,8,-2,5,-10,8,6,10,-10,3,4,7,8,10,4,-9,-8,-6,-7,-2,10,6,-7,-4,-3,8,6,1,7,-4,-7,-9,-3,5,-6,1,-6,3,-5,-2,-3,-8,-8,-5,-2,-7,3,6,-10,7,8,3,-5,9,3,-2,4,5,9,-8,-10,-4,10,10,10,6,-7,2,-7,-4,2,7,6,-9,-6,9,-3,-9,-2,-3,-8,8,9,-7,-1,-7,9,-1,9,-1,9,9,3,-5,8,-7,8,-2,-7,3,2,-1,3,-5,3,5,7,4,-3,7,6,10,9,-10,4,4,-1,-6,-10,9,10,5,-10,-7,7,-8,8,-6,-3,5,8,-3,8,-7,4,-10,-10,2,-4,-6,-3,-4,4,9,-4,5,6,5,9], dtype = "int64")#candidate|7179|(189,)|const|int64
call_7178 = func_1047_call(relay.reshape(const_7179.astype('int64'), [9, 3, 7]))
call_7180 = func_1047_call(relay.reshape(const_7179.astype('int64'), [9, 3, 7]))
output = relay.Tuple([call_7130,call_7139,call_7141,const_7142,bop_7147,bop_7155,call_7170,var_7171,call_7178,const_7179,])
output2 = relay.Tuple([call_7132,call_7140,call_7143,const_7142,bop_7147,bop_7155,call_7172,var_7171,call_7180,const_7179,])
func_7182 = relay.Function([var_7122,var_7123,var_7171,], output)
mod['func_7182'] = func_7182
mod = relay.transform.InferType()(mod)
mutated_mod['func_7182'] = func_7182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7182_call = mutated_mod.get_global_var('func_7182')
var_7184 = relay.var("var_7184", dtype = "uint16", shape = (13, 8, 1))#candidate|7184|(13, 8, 1)|var|uint16
var_7185 = relay.var("var_7185", dtype = "uint16", shape = (13, 8, 10))#candidate|7185|(13, 8, 10)|var|uint16
var_7186 = relay.var("var_7186", dtype = "float64", shape = (182, 1))#candidate|7186|(182, 1)|var|float64
call_7183 = func_7182_call(var_7184,var_7185,var_7186,)
output = call_7183
func_7187 = relay.Function([var_7184,var_7185,var_7186,], output)
mutated_mod['func_7187'] = func_7187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3580_call = mod.get_global_var('func_3580')
func_3581_call = mutated_mod.get_global_var('func_3581')
call_7233 = relay.TupleGetItem(func_3580_call(), 0)
call_7234 = relay.TupleGetItem(func_3581_call(), 0)
func_7043_call = mod.get_global_var('func_7043')
func_7046_call = mutated_mod.get_global_var('func_7046')
const_7236 = relay.const([True,True,False,False,False,True,True,True,True,True,True,False,False,False,False,False,True,False,True,False,True,False,True,True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,True,True,False,False,True,False,False,False,False,False,False,False,False,True,False,True,True,True,False,True,False,False,False,False,False,True,True,False,True,True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,True,True,False,False,False,False,False,False,False,False,False,False,True,True,False,False,False,True,False,True,True,True,True,True,False,True,True,True,True,False,False,False,True,False,True,True,False,True,True,False,True,True,True,False,True,True,True,True,True,True,False,False,False,True,True,False,False,False,True,True,False,True,False,True,True,True,False,True,False,True,False,True,True,True,True,False,False,False,True,True,False,False,True,False,True,False,True,False,True,False,True,True,False,True,True,True,False,True,True,False,True,True,True,False,False,True,False,False,True,True,False,True,True,True,False,True,False,True,True,True,True,False,False,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,True,True,True,True,False,True,True,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,True,True,False,True,True,True,True,True,True,False,False,False,False,True,True,True,True,False,False,False,False,True,False,True,False,True,True,True,True,False,True,False,True,True,False,False,True,True,True,False,True,True,False,True,True,False,False,False,False,True,True,True,False,True,False,False,False,True,False,False,True,True,False,False,False,False,False,True,True,True,True,False,False,False,False,True,False,False,False,False,True,True,True,False,False,True,False,False,False,False,False,True,True,True,True,False,True,True,True,True,False,True,True,True,True,True,False,True,False,False,True,True,True,True,True,True,False,False,False,True,False,False,False,False,True,False,False,True,True,True,False,False,False,True,True,True,True,True,False,True,False,False,False,True,True,False,True,True,False,True,False,False,True,True,False,True,True,False,False,False,False,False,False,False,True,True,False,False,True,False,True,True,False,False,False,True,False,True,True,False,False,True,False,False,False,True,True,True,True,True,False,True,True,False,False,False,False,False,True,True,False,False,False,True,False,False,False,False,False,True,False,False,True,True,False,True,False,True,True,True,False,True,True,True,True,True,False,True,True,True,False,True,True,False,False,False,True,True,False,True,False,True,True,True,False,False,True,False,True,False,True,False,True,False,True,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,True,False,True,False,True,True,False,False,True,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,True,True,False,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,False,False,True,False,False,False,True,True,False,False,True,True,False,True,True,False,False,False,True,False,False,True,True,True,True,False,False,False,True,True,True,False,True,True,False,True,True,True,False,True,True,False,True,False,True,False,False,True,False,True,True,False,False,False,True,True,True,False,False,False,True,True,False,False,False,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,True,False,True,False,False,False,True,False,False,True,True,False,False,True,False,False,True,False,False,False,False,True,False,False,False,False,True,True,False,True,True,False,False,False,False,False,True,True,False,True,False,True,True,False,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,True,True,False,True,True,True,True,True,False,False,True,True,False,False,True,True,True,True,False,True,True,True,True,False,True,True,True,True,False,True,False,True,False,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,True,False,True,False,True,False,False,False,False,True,True,False,False,True,True,True,False,True,True,True,False,False,True,True,True,False,False,True,False,True,True,True,True,True,True,True,True,False,True,True,True,True,True,False,False,False,True,False,True,False,False,True,False,True,False,False,True,True,True,True,False,False,False,True,True,True,False,True,True,False,False,True,True,False,True,True,False,False,False,False,False,False,True,False,True,False,False,False,True,True,True,True,False,True,False,True,False,True,False,False,True,True,True], dtype = "bool")#candidate|7236|(864,)|const|bool
call_7235 = relay.TupleGetItem(func_7043_call(relay.reshape(const_7236.astype('bool'), [6, 9, 16])), 0)
call_7237 = relay.TupleGetItem(func_7046_call(relay.reshape(const_7236.astype('bool'), [6, 9, 16])), 0)
func_4118_call = mod.get_global_var('func_4118')
func_4121_call = mutated_mod.get_global_var('func_4121')
const_7241 = relay.const(-3, dtype = "uint8")#candidate|7241|()|const|uint8
var_7242 = relay.var("var_7242", dtype = "uint8", shape = (1215,))#candidate|7242|(1215,)|var|uint8
call_7240 = relay.TupleGetItem(func_4118_call(relay.reshape(const_7241.astype('uint8'), []), relay.reshape(var_7242.astype('uint8'), [1215,]), ), 3)
call_7243 = relay.TupleGetItem(func_4121_call(relay.reshape(const_7241.astype('uint8'), []), relay.reshape(var_7242.astype('uint8'), [1215,]), ), 3)
uop_7247 = relay.exp(const_7236.astype('float64')) # shape=(864,)
var_7254 = relay.var("var_7254", dtype = "uint8", shape = (1215,))#candidate|7254|(1215,)|var|uint8
bop_7255 = relay.power(var_7242.astype('float32'), relay.reshape(var_7254.astype('float32'), relay.shape_of(var_7242))) # shape=(1215,)
output = relay.Tuple([call_7233,call_7235,call_7240,const_7241,uop_7247,bop_7255,])
output2 = relay.Tuple([call_7234,call_7237,call_7243,const_7241,uop_7247,bop_7255,])
func_7258 = relay.Function([var_7242,var_7254,], output)
mod['func_7258'] = func_7258
mod = relay.transform.InferType()(mod)
var_7259 = relay.var("var_7259", dtype = "uint8", shape = (1215,))#candidate|7259|(1215,)|var|uint8
var_7260 = relay.var("var_7260", dtype = "uint8", shape = (1215,))#candidate|7260|(1215,)|var|uint8
output = func_7258(var_7259,var_7260,)
func_7261 = relay.Function([var_7259,var_7260,], output)
mutated_mod['func_7261'] = func_7261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mod.get_global_var('func_3833')
func_3835_call = mutated_mod.get_global_var('func_3835')
call_7313 = relay.TupleGetItem(func_3833_call(), 3)
call_7314 = relay.TupleGetItem(func_3835_call(), 3)
func_1618_call = mod.get_global_var('func_1618')
func_1622_call = mutated_mod.get_global_var('func_1622')
const_7330 = relay.const([3,-1,-4,8,-2,-3,-6,-7,7,1,4,9,-8,9,1,-9,-2,5,-9,-2,-4,6,-10,-10,-3,-5,8,-6,5,10,-1,-10,3,1,-6,3,-7,-1,-1,2,-4,1,-10,-8,4,9,-9,10,-4,-4,-3,-4,7,7,-8,2,-7,4,1,4,-2,-3,-4,2,6,-10,-4,-1,-10,9,-9,-10,3,8,7,-9,5,-7,7,-6,-7,1,-1,-4,-1,8,3,8,3,-10,-8,-7,-3,1,-8,-10,-5,6,-3,6,-3,-4,6,2,2,2,-1,2,-5,-3,-1,-8,5,-2,-6,2,7,-6,10,4,10,-1,-5,8,-7,5,-5,6,-8,-8,-1,6,8,10,-1,-9,10,-3,-4,-7,1,3,-6,8,9,8,6,-5,7,-2,10,9,-5,5,5,-2,-5,-4,4,-2,-8,1,6,8,-3,-2,-6,-5,5,-10,-3,1,-7,-8,7,-4,-2,-10,-10,4,1,-8,-8,7,4,-6,-2,-6,1], dtype = "int64")#candidate|7330|(189,)|const|int64
var_7331 = relay.var("var_7331", dtype = "uint16", shape = (234,))#candidate|7331|(234,)|var|uint16
call_7329 = relay.TupleGetItem(func_1618_call(relay.reshape(const_7330.astype('int64'), [189,]), relay.reshape(var_7331.astype('uint16'), [234,]), ), 1)
call_7332 = relay.TupleGetItem(func_1622_call(relay.reshape(const_7330.astype('int64'), [189,]), relay.reshape(var_7331.astype('uint16'), [234,]), ), 1)
uop_7335 = relay.cos(call_7329.astype('float64')) # shape=(9, 3, 7)
uop_7337 = relay.cos(call_7332.astype('float64')) # shape=(9, 3, 7)
func_5714_call = mod.get_global_var('func_5714')
func_5716_call = mutated_mod.get_global_var('func_5716')
const_7343 = relay.const([4,-8,3,1,5,-9,-8,10,-5,7,-4,-1,-6,-7,6,10,9,-5,2,-6,-5,-5,7,9,4,-3,4,1,-8,8,2,4,-6,6,8,6,6,-4,-9,-6,1,-1,-5,7,-3,-9,-3,-6,5,8,7,-7,-7,5,6,-1,5,3,4,-5,-5,2,9,-8,4,-8,-1,-4,-7,-6,-2,-1,-9,-7,4,-2,6,6,5,-2,1,-10,6,-3,-4,-8,-6,-5,5,9,-4,8,-6,9,-10,10,10,4,-5,1,-7,-6,-7,-9,-3,-2,9,10,4,-9,-10,-6,1,8,-10,-5,-5,-10,-2,-7,-9,-5,-10,-6,-4,-9,-3,5,-6,10,-10,-2,6,9,3,4,-6,-2,3,1,4,10,-6,1,-7,-9,-6,4,-3,1,-3,-9,5,5,1,3,-9,-3,9,-8,-7,-5,-8,-6,-4,-10,-3,7,-2,5,-10,7,3,-6,-3,1,3,-2,7,-5,-4,-9,4,6,8,-7,2,-2,5,-9,2,8,-8,-8,10,-7,8,3,3,8,-3,-4,1,9,-1,6,-10,3,-7,-2,-4,-1,-8,6,6,-5,-1,3,2,-7,10,-10,-8,-8,-2,1,-3,2,-9,-3,2,-5,8,4,9,4,-7,-10,5,-1,8,7,-6,-1,7,9,5,-2,-1,-2,10,-10,10,5,5,6,-7,5,4,-8,1,10,-3,-8,3,-7,-7,1,4,-5,-1,2,-6,3,2,-10,-1,10,5,10,-9,-10,-3,-4,-6,-6,9,-6,7,-4,-1,4,5,7,6,-7,-6,1,-7,-6,3,-1,-4,-9,6,-1,-6,-10,1,-10,-7,-1,-3,2,-7,-2,-4,5,9,8,7,-2,-4,-5,-10,-1,-1,9,7,1,-2,4,-7,-2,3,2,9,5,6,8,5,2,4,-10,-3,-4,-6,-10,7,9,-4,-10,-7,-6,-4,-1,-4,3,-4,-8,3,-1,10,4,-5,-9,-8,-2,3,9,2,6,-3,-5,-1,-6,-7,-5,-10,4,4,4,4,6,-4,5,-5,4,-10,-8,2,-7,-3,-5,3,-10,-5,-8,10,6,-1,2,4,7,-4,6,9,4,8,-6,-3,10,1,-8,-4,-7,-9,-2,-4,6,-3,4,8,5,1,8,8,-3,6,1,8,-6,6,8,4,-10,10,1,3,-5,7,-8,1,-5,-3,-8,4,-7,-9,-2,1,-4,-7,-1,10,5,-7,-4,4,-5,6,9,-7,-10,-1,3,-8,5,9,6,-9,-7,-3,5,10,8,5,-6,2,-1,10,-7,9,4,5,7,10,-2,-7,-4,-9,3,-8,6,-4,-4,-1,5,-2,-7,-10,3,-2,-4,-2,-6,-1,-4,-7,-10,7,7,9,-7,-2,8,-3,-1,5,-4,6,-7,8,-7,-4,-5,-2,-9,4,-2,2,-8,4,-10,7,-6,-3,-1,4,7,4,9,6,-9,-7,7,-4,6,4,-4,9,5,3,-6,-1,-5,7,-3,5,1,2,1,3,-1,-1,-8,-7,6,-9,8,-5,5,8,-5,9,-3,6,-6,-9,-5,-5,5,-8,-1,3,-6,-2,-10,-10,-3,1,-9,-10,-5,5,-1,3,-2,7,7,-3,-8,-8,5,-1,7,4,10,-3,3,5,6,-10,-10,-2,-6,-3,-9,-3,9,3,-8,1,1,5,2,7,-9,-8,5,7,4,8,-1,10,-6,5,1,4,-2,5,-8,-1,1,-5,9,2,1,9,-10,3,1,2,4,6,-4,9,3,-8,-9,-3,-4,-4,-4,9,9,1,-10,3,-8,1,10,-5,-9,-1,5,-7,-8,6,-3,7,-10,3,1,5,7,-3,-3,-3,-3,-1,6,-9,-10,-8,3,4,-2,-3,-6,-4,4,1,-8,-10,-7,-1,-10,1,7,-4,3,-4,-6,9,5,5,3,-7,-8,-3,-9,-2,-5,10,10,-2,3,-1,-3,10,-6,-5,1,-9,10,-6,6,-9,-10,-3,-6,-7,-1,7,9,-9,-2,-3,10,-4,5,1,-9,-4,-3,1,-2,-6,7,6,-1,-2,-3,6,8,-4,-9,6,-7,-6,7,-8,8,-3,-7,2,8,-1,-10,4,6,-2,-3,4,9,8,9,-9,10,-3,-3,-7,10,1,6,7,1,8,8,-4,1,-4,-10,9,-5,8,-7,8,-4,5,-2,1,-2,9,-2,6,9,-6,-1,10,7,-5,-5,-4,-1,9,3,-9,1,-4,5,8,8,-4,1,6,-3,4,3,7,7,9,5,5,-10,-1,-7,-8,3,5,-5,1,1,8,-3,9,-10,-10,-8,5,3,2,2,-6,-1,8,5,6,5,1,-10,8,9,-6,-10,-3,-6,-5,-5,3,4,-4,1,5,5,-3,-6,-6,6,10,-3,-1,9,7,-6,2,4,-9,9,10,-9,10,4,10,7,8,-4,1,6,9,-10,2,-10,-8,4,-4,3,-8,-7,-6,10,-4,-4,10,-5,-2,2,9,-4,1,-7,2,-9,6,9,-10,-8,3,-1,4,4,1,9,-9], dtype = "uint16")#candidate|7343|(945,)|const|uint16
call_7342 = relay.TupleGetItem(func_5714_call(relay.reshape(const_7343.astype('uint16'), [945,])), 2)
call_7344 = relay.TupleGetItem(func_5716_call(relay.reshape(const_7343.astype('uint16'), [945,])), 2)
uop_7346 = relay.rsqrt(const_7330.astype('float32')) # shape=(189,)
output = relay.Tuple([call_7313,var_7331,uop_7335,call_7342,const_7343,uop_7346,])
output2 = relay.Tuple([call_7314,var_7331,uop_7337,call_7344,const_7343,uop_7346,])
func_7348 = relay.Function([var_7331,], output)
mod['func_7348'] = func_7348
mod = relay.transform.InferType()(mod)
var_7349 = relay.var("var_7349", dtype = "uint16", shape = (234,))#candidate|7349|(234,)|var|uint16
output = func_7348(var_7349)
func_7350 = relay.Function([var_7349], output)
mutated_mod['func_7350'] = func_7350
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7355 = relay.var("var_7355", dtype = "uint8", shape = (14, 3, 7))#candidate|7355|(14, 3, 7)|var|uint8
var_7356 = relay.var("var_7356", dtype = "uint8", shape = (14, 3, 7))#candidate|7356|(14, 3, 7)|var|uint8
bop_7357 = relay.right_shift(var_7355.astype('uint8'), relay.reshape(var_7356.astype('uint8'), relay.shape_of(var_7355))) # shape=(14, 3, 7)
var_7360 = relay.var("var_7360", dtype = "uint8", shape = (14, 3, 7))#candidate|7360|(14, 3, 7)|var|uint8
bop_7361 = relay.floor_divide(bop_7357.astype('float64'), relay.reshape(var_7360.astype('float64'), relay.shape_of(bop_7357))) # shape=(14, 3, 7)
bop_7365 = relay.logical_and(bop_7361.astype('bool'), relay.reshape(bop_7357.astype('bool'), relay.shape_of(bop_7361))) # shape=(14, 3, 7)
output = bop_7365
output2 = bop_7365
func_7369 = relay.Function([var_7355,var_7356,var_7360,], output)
mod['func_7369'] = func_7369
mod = relay.transform.InferType()(mod)
var_7370 = relay.var("var_7370", dtype = "uint8", shape = (14, 3, 7))#candidate|7370|(14, 3, 7)|var|uint8
var_7371 = relay.var("var_7371", dtype = "uint8", shape = (14, 3, 7))#candidate|7371|(14, 3, 7)|var|uint8
var_7372 = relay.var("var_7372", dtype = "uint8", shape = (14, 3, 7))#candidate|7372|(14, 3, 7)|var|uint8
output = func_7369(var_7370,var_7371,var_7372,)
func_7373 = relay.Function([var_7370,var_7371,var_7372,], output)
mutated_mod['func_7373'] = func_7373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5042_call = mod.get_global_var('func_5042')
func_5044_call = mutated_mod.get_global_var('func_5044')
call_7408 = func_5042_call()
call_7409 = func_5042_call()
output = relay.Tuple([call_7408,])
output2 = relay.Tuple([call_7409,])
func_7418 = relay.Function([], output)
mod['func_7418'] = func_7418
mod = relay.transform.InferType()(mod)
output = func_7418()
func_7419 = relay.Function([], output)
mutated_mod['func_7419'] = func_7419
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_7458 = relay.TupleGetItem(func_3534_call(), 2)
call_7459 = relay.TupleGetItem(func_3536_call(), 2)
func_6332_call = mod.get_global_var('func_6332')
func_6334_call = mutated_mod.get_global_var('func_6334')
var_7465 = relay.var("var_7465", dtype = "bool", shape = (126,))#candidate|7465|(126,)|var|bool
call_7464 = func_6332_call(relay.reshape(var_7465.astype('bool'), [7, 2, 9]))
call_7466 = func_6332_call(relay.reshape(var_7465.astype('bool'), [7, 2, 9]))
func_4068_call = mod.get_global_var('func_4068')
func_4070_call = mutated_mod.get_global_var('func_4070')
var_7468 = relay.var("var_7468", dtype = "float64", shape = (1, 1155))#candidate|7468|(1, 1155)|var|float64
call_7467 = relay.TupleGetItem(func_4068_call(relay.reshape(var_7468.astype('float64'), [7, 11, 15])), 2)
call_7469 = relay.TupleGetItem(func_4070_call(relay.reshape(var_7468.astype('float64'), [7, 11, 15])), 2)
output = relay.Tuple([call_7458,call_7464,var_7465,call_7467,var_7468,])
output2 = relay.Tuple([call_7459,call_7466,var_7465,call_7469,var_7468,])
func_7472 = relay.Function([var_7465,var_7468,], output)
mod['func_7472'] = func_7472
mod = relay.transform.InferType()(mod)
var_7473 = relay.var("var_7473", dtype = "bool", shape = (126,))#candidate|7473|(126,)|var|bool
var_7474 = relay.var("var_7474", dtype = "float64", shape = (1, 1155))#candidate|7474|(1, 1155)|var|float64
output = func_7472(var_7473,var_7474,)
func_7475 = relay.Function([var_7473,var_7474,], output)
mutated_mod['func_7475'] = func_7475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_7477 = relay.TupleGetItem(func_3534_call(), 2)
call_7478 = relay.TupleGetItem(func_3536_call(), 2)
func_4953_call = mod.get_global_var('func_4953')
func_4956_call = mutated_mod.get_global_var('func_4956')
var_7484 = relay.var("var_7484", dtype = "float64", shape = (2016,))#candidate|7484|(2016,)|var|float64
call_7483 = relay.TupleGetItem(func_4953_call(relay.reshape(call_7477.astype('float32'), [2, 13, 5]), relay.reshape(var_7484.astype('float64'), [2016, 1]), ), 2)
call_7485 = relay.TupleGetItem(func_4956_call(relay.reshape(call_7477.astype('float32'), [2, 13, 5]), relay.reshape(var_7484.astype('float64'), [2016, 1]), ), 2)
var_7503 = relay.var("var_7503", dtype = "float64", shape = (2016,))#candidate|7503|(2016,)|var|float64
bop_7504 = relay.floor_divide(var_7484.astype('float64'), relay.reshape(var_7503.astype('float64'), relay.shape_of(var_7484))) # shape=(2016,)
output = relay.Tuple([call_7477,call_7483,bop_7504,])
output2 = relay.Tuple([call_7478,call_7485,bop_7504,])
func_7507 = relay.Function([var_7484,var_7503,], output)
mod['func_7507'] = func_7507
mod = relay.transform.InferType()(mod)
mutated_mod['func_7507'] = func_7507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7507_call = mutated_mod.get_global_var('func_7507')
var_7509 = relay.var("var_7509", dtype = "float64", shape = (2016,))#candidate|7509|(2016,)|var|float64
var_7510 = relay.var("var_7510", dtype = "float64", shape = (2016,))#candidate|7510|(2016,)|var|float64
call_7508 = func_7507_call(var_7509,var_7510,)
output = call_7508
func_7511 = relay.Function([var_7509,var_7510,], output)
mutated_mod['func_7511'] = func_7511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5521_call = mod.get_global_var('func_5521')
func_5522_call = mutated_mod.get_global_var('func_5522')
call_7541 = func_5521_call()
call_7542 = func_5521_call()
func_7507_call = mod.get_global_var('func_7507')
func_7511_call = mutated_mod.get_global_var('func_7511')
var_7554 = relay.var("var_7554", dtype = "float64", shape = (2016,))#candidate|7554|(2016,)|var|float64
call_7553 = relay.TupleGetItem(func_7507_call(relay.reshape(var_7554.astype('float64'), [2016,]), relay.reshape(var_7554.astype('float64'), [2016,]), ), 1)
call_7555 = relay.TupleGetItem(func_7511_call(relay.reshape(var_7554.astype('float64'), [2016,]), relay.reshape(var_7554.astype('float64'), [2016,]), ), 1)
output = relay.Tuple([call_7541,call_7553,var_7554,])
output2 = relay.Tuple([call_7542,call_7555,var_7554,])
func_7569 = relay.Function([var_7554,], output)
mod['func_7569'] = func_7569
mod = relay.transform.InferType()(mod)
mutated_mod['func_7569'] = func_7569
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7570 = relay.var("var_7570", dtype = "float64", shape = (2016,))#candidate|7570|(2016,)|var|float64
func_7569_call = mutated_mod.get_global_var('func_7569')
call_7571 = func_7569_call(var_7570)
output = call_7571
func_7572 = relay.Function([var_7570], output)
mutated_mod['func_7572'] = func_7572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_7648 = relay.TupleGetItem(func_3534_call(), 0)
call_7649 = relay.TupleGetItem(func_3536_call(), 0)
func_6365_call = mod.get_global_var('func_6365')
func_6366_call = mutated_mod.get_global_var('func_6366')
call_7662 = relay.TupleGetItem(func_6365_call(), 0)
call_7663 = relay.TupleGetItem(func_6366_call(), 0)
output = relay.Tuple([call_7648,call_7662,])
output2 = relay.Tuple([call_7649,call_7663,])
func_7690 = relay.Function([], output)
mod['func_7690'] = func_7690
mod = relay.transform.InferType()(mod)
mutated_mod['func_7690'] = func_7690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7690_call = mutated_mod.get_global_var('func_7690')
call_7691 = func_7690_call()
output = call_7691
func_7692 = relay.Function([], output)
mutated_mod['func_7692'] = func_7692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_7734 = relay.TupleGetItem(func_3534_call(), 0)
call_7735 = relay.TupleGetItem(func_3536_call(), 0)
output = relay.Tuple([call_7734,])
output2 = relay.Tuple([call_7735,])
func_7772 = relay.Function([], output)
mod['func_7772'] = func_7772
mod = relay.transform.InferType()(mod)
output = func_7772()
func_7773 = relay.Function([], output)
mutated_mod['func_7773'] = func_7773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5521_call = mod.get_global_var('func_5521')
func_5522_call = mutated_mod.get_global_var('func_5522')
call_7852 = func_5521_call()
call_7853 = func_5521_call()
output = relay.Tuple([call_7852,])
output2 = relay.Tuple([call_7853,])
func_7859 = relay.Function([], output)
mod['func_7859'] = func_7859
mod = relay.transform.InferType()(mod)
mutated_mod['func_7859'] = func_7859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7859_call = mutated_mod.get_global_var('func_7859')
call_7860 = func_7859_call()
output = call_7860
func_7861 = relay.Function([], output)
mutated_mod['func_7861'] = func_7861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_7908 = relay.TupleGetItem(func_3534_call(), 0)
call_7909 = relay.TupleGetItem(func_3536_call(), 0)
var_7910 = relay.var("var_7910", dtype = "int64", shape = (16, 14, 14))#candidate|7910|(16, 14, 14)|var|int64
bop_7911 = relay.maximum(call_7908.astype('uint64'), relay.reshape(var_7910.astype('uint64'), relay.shape_of(call_7908))) # shape=(16, 14, 14)
bop_7914 = relay.maximum(call_7909.astype('uint64'), relay.reshape(var_7910.astype('uint64'), relay.shape_of(call_7909))) # shape=(16, 14, 14)
bop_7917 = relay.divide(var_7910.astype('float64'), relay.reshape(call_7908.astype('float64'), relay.shape_of(var_7910))) # shape=(16, 14, 14)
bop_7920 = relay.divide(var_7910.astype('float64'), relay.reshape(call_7909.astype('float64'), relay.shape_of(var_7910))) # shape=(16, 14, 14)
func_5017_call = mod.get_global_var('func_5017')
func_5020_call = mutated_mod.get_global_var('func_5020')
var_7932 = relay.var("var_7932", dtype = "float32", shape = (234,))#candidate|7932|(234,)|var|float32
const_7933 = relay.const([-2.283025,7.114090,-1.286754,-7.380390,-2.700574,-8.273044,8.461580,-2.879033,7.462483,-0.959146,8.467477,5.386018,-6.844630,-1.593803,-0.828096,-4.498774,3.452420,4.582017,7.989861,-9.024170,-8.529305,1.944247,-8.939107,2.495185,4.435195,-3.547005,-8.274616,4.009777,-4.310276,-1.998387,9.207678,6.305673,2.939443,-7.251974,-4.701765,-0.230573,8.075197,-6.542601,0.727380,-2.673590,-9.236065,-4.096777,-1.152793,4.543165,9.621312,7.670470,2.017532,9.633220,5.582778,8.248942,4.155321,-8.816862,-8.668499,-0.057256,5.468877,-3.077964,2.770859,-8.093393,-0.041621,-1.660294,2.245912,-1.930212,-4.034887,1.363738,0.376309,-2.127161,2.102632,-3.916983,1.691106,5.860151,9.692214,-1.217750,-3.366661,-5.203879,4.729670,9.246276,-3.554081,1.875049,3.388401,-9.430566,5.824716,1.246189,-7.691590,-5.136241,2.008953,-3.220980,-1.752461,9.685840], dtype = "float64")#candidate|7933|(88,)|const|float64
call_7931 = relay.TupleGetItem(func_5017_call(relay.reshape(var_7932.astype('float32'), [234,]), relay.reshape(const_7933.astype('float64'), [88,]), ), 4)
call_7934 = relay.TupleGetItem(func_5020_call(relay.reshape(var_7932.astype('float32'), [234,]), relay.reshape(const_7933.astype('float64'), [88,]), ), 4)
func_7472_call = mod.get_global_var('func_7472')
func_7475_call = mutated_mod.get_global_var('func_7475')
var_7943 = relay.var("var_7943", dtype = "bool", shape = (126,))#candidate|7943|(126,)|var|bool
var_7944 = relay.var("var_7944", dtype = "float64", shape = (7, 165))#candidate|7944|(7, 165)|var|float64
call_7942 = relay.TupleGetItem(func_7472_call(relay.reshape(var_7943.astype('bool'), [126,]), relay.reshape(var_7944.astype('float64'), [1, 1155]), ), 2)
call_7945 = relay.TupleGetItem(func_7475_call(relay.reshape(var_7943.astype('bool'), [126,]), relay.reshape(var_7944.astype('float64'), [1, 1155]), ), 2)
uop_7966 = relay.cosh(bop_7917.astype('float32')) # shape=(16, 14, 14)
uop_7968 = relay.cosh(bop_7920.astype('float32')) # shape=(16, 14, 14)
func_4596_call = mod.get_global_var('func_4596')
func_4599_call = mutated_mod.get_global_var('func_4599')
var_7971 = relay.var("var_7971", dtype = "int64", shape = (63, 3))#candidate|7971|(63, 3)|var|int64
call_7970 = relay.TupleGetItem(func_4596_call(relay.reshape(var_7971.astype('int64'), [189,])), 1)
call_7972 = relay.TupleGetItem(func_4599_call(relay.reshape(var_7971.astype('int64'), [189,])), 1)
bop_7975 = relay.minimum(uop_7966.astype('float32'), relay.reshape(bop_7911.astype('float32'), relay.shape_of(uop_7966))) # shape=(16, 14, 14)
bop_7978 = relay.minimum(uop_7968.astype('float32'), relay.reshape(bop_7914.astype('float32'), relay.shape_of(uop_7968))) # shape=(16, 14, 14)
func_6310_call = mod.get_global_var('func_6310')
func_6313_call = mutated_mod.get_global_var('func_6313')
const_7980 = relay.const([-0.966305,-7.545100,-3.262943,-1.850447,4.003112,3.615605,-7.163774,-3.872157,4.071407,8.892290,6.744308,-0.181745,3.656904,2.023411,-0.436228,-9.617470,1.300718,-4.121216,-7.176947,2.198533,-0.891933,-5.402088,-4.437108,8.092140,-1.566738,2.999523,1.155461,8.459982,3.536410,2.258503,8.536145,-1.452545,-8.511998,-9.822816,2.572878,-9.286142,1.061202,2.967075,1.875236,6.770493,9.197722,9.505646,-7.930489,6.240999,-3.341001,-2.656681,0.179505,-7.510979,6.866193,-0.486670,-7.551234,9.619636,6.223793,7.589456,7.460901,-1.369123,-2.167404,1.422564,5.073588,-5.317038,-7.194254,6.568312,8.337833,9.298972,0.641120,-6.853470,5.255764,6.573439,-2.963439,6.379402,9.133531,-6.814442,-9.167601,5.606918,-0.393691,9.887937,-9.141406,-2.113273,-1.819342,-8.981663,6.383267,-1.366756,-6.954143,-2.628909,-0.766925,-2.927207,9.637673,0.564500,6.131638,4.006257,-2.452713,-6.386689,-4.537628,5.202003,-2.101576,-5.002155,-0.541347,-3.959424,-8.174480,1.866131,3.632220,-2.090922,-4.415671,-8.423029,-3.003960,0.535827,-8.024916,2.901951,9.516026,4.434141,8.686086,0.579055,-0.301150,-6.045529,-4.941705,-4.089279,-7.816238,7.724197,-1.071732,-4.318124,9.588842,-3.521443,7.254723,-6.155263,-9.922350,-0.577482,6.822726,5.614985,-3.138255,-5.154030,7.834561,-2.233882,-2.194275,-6.700847,6.194414,2.849439,-6.502741,-2.713434,-4.400834,-0.507033,-0.032830,-6.998163,3.967220,-1.253318,8.125875,-9.888013,5.398912,-8.556230,-2.056637,-9.023961,7.268053,5.644410,7.341485,5.223859,-3.992808,-9.184344,0.434445,3.556615,-6.139508,-1.549405,-5.578596,-3.971312,3.511812,2.612174,0.231529,0.315450,-1.107044,7.965828,-7.868555,0.651379,-1.929859,8.149107,-0.869353,-9.310111,-6.518099,-7.796872,-7.776302,-7.334818,-0.897376,1.502231,-9.307737,-9.339717,6.336261,-7.186293,1.693754,8.089272,-0.025233,3.316273,1.522492,3.915451,-6.694843,-9.330734,0.113590,-3.689070,2.601962,9.980604,-0.870470,-6.605978,1.668529,6.813526,-9.769171,6.089194,4.594959,0.061244,-4.523596,5.215877,-4.300162,9.762347,-4.024746,2.926387,-2.193755,5.230669,2.238938,-6.194121,0.155478,6.542677,-4.458785,-1.616610,1.564062,-3.046146,-8.058527,-1.991803,-9.117233,-5.198029,8.992161,-5.201168,1.968534,-7.578121,0.689463,3.135817,-4.482959,-3.444900,3.499785,-1.343015,-8.901122,1.852997,-5.341214,2.500304,9.739792,-7.129505,-7.743129,-7.155178,-0.337341,-7.523541,-1.353370,-7.049028,-8.059949,7.493644,4.385638,-0.871856,0.542197,5.566866,3.874784,-1.176418,-2.048392,9.755639,8.362349,-3.694988,-3.134155,8.801689,3.515349,7.413483,-8.087964,1.883476,-4.991703,4.195303,5.650046,-2.992213,1.896280,-1.329146,9.554233,-1.865660,6.615265,-2.977415,6.291046,-6.778001,-1.526266,-7.862547,0.368257,-2.654091,5.026397,9.995878,-7.149924,9.900399,-7.162738,-2.764807,0.423400,-6.860629,2.083467,-1.912340,-0.561274,0.611467,-2.668970,8.007982,-2.878970,-7.685756,4.200226,-2.216536,9.345483,4.000079,9.858416,5.801184,5.235698,-2.894079,-1.880033,9.003053,5.551540,9.389642,8.113439,2.779444,2.232606,8.187365,2.001392,-2.178255,-8.584461,-2.918150,2.304434,-9.825234,5.154907,-4.592120,-4.712481,-1.264784,-6.707374,3.640337,-4.261773,9.855471,-8.111133,-4.219407,7.208178,-7.972729,5.706724,1.390802,-1.274662,3.379415,-4.399906,-3.755580,5.961978,4.339950,-3.825445,4.267919,7.653298,-0.278980,-3.522769,-6.622047,-7.350216,1.434926,5.104531,-5.304795,-7.242589,-5.764397,6.998344,4.021286,6.783627,4.627961,-7.803977,0.479174,3.239405,3.457846,-8.453433,8.376841,6.327220,-0.911762,-8.642374,-5.044677,-7.607951,0.696282,2.678824,1.386520,0.825609,4.753818,4.394945,-2.734445,-1.476933,-1.874176,1.320461,4.203836,-7.992842,9.837767,5.524145,-9.165979,-8.601464,7.543392,-1.585692,9.065387,7.672900,9.190202,7.638075,-5.625328,-3.629396,-2.069537,-5.804422,-4.572491,-5.424567,5.313836,7.003319,9.916442,-7.921535,-9.069498,3.681135,-4.969431,-6.308612,-1.415183,0.326672,5.476145,3.711324,2.433610,-9.695575,7.446039,-4.620424,-2.995638,-1.262361,3.332343,-7.850659,1.991456,1.774815,7.692951,-5.728955,3.542782,-2.063741,4.980246,8.194549,5.667891,-9.581239,-0.365653,-6.271254,-0.716256,-8.437987,4.567613,2.243479,6.914401,-8.906061,-1.865202,-4.287277,1.748829,6.584848,-1.382474,6.410380,-7.235907,-5.043701,-1.862750,0.517053,7.670366,2.848076,-5.798766,-9.997916,8.333768,-1.642624,4.653438,-9.723924,9.632163,2.320315,-8.505064,-4.765813,-9.912705,4.930325,9.071897,9.734655,-8.954678,4.140241,-0.077353,-5.234566,-2.125499,8.392575,5.955526,-4.255843,5.949289,9.612754,1.045487,-4.030583,-4.262854,-8.058953,-5.855295,0.448718,-1.057342,-4.220808,-0.082662,9.579498,4.443707,-1.907665,-2.448831,-3.274544,-6.106172,7.688182,5.752898,8.826666,0.041861,5.619391,7.997430,-2.151043,8.274546,-8.282237,-7.803862,-9.145154,6.045106,-5.703059,-8.051906,9.822867,-6.236730,-6.731072,7.690918,-0.447437,8.258947,-6.732282,-3.041096,5.940209,6.150233,9.378558,7.273452,-2.144250,-6.958913,-2.516920,0.501213,3.839992,-0.655567,7.487804,0.644827,-6.419877,1.202040,2.588420,4.380717,3.394740,1.992890,-2.052848,-7.948157,6.736321,-6.893955,0.286421,5.127940,2.020670,-9.487974,5.955007,-9.445950,7.564764,2.513694,5.799511,3.046198,4.806998,5.556047,5.034478,-0.970213,-9.173797,-2.295783,-2.564785,-2.365391,3.003694,-1.956867,-2.463324,-3.805008,-4.773528,6.663641,-9.100325,-8.472435,9.570604,-0.578835,-2.976549,0.474137,9.629697,-8.817147,8.987167,3.314082,-8.596887,-2.206220,2.407465,-2.188013,-2.998435,4.211749,-7.441017,-1.759642,-8.375614,-9.601778,-2.151939,1.245579,9.159325,9.293690,7.609666,8.366773,9.323964,-3.624348,-5.889657,-6.390145,-9.323242,9.163515,-2.346163,-4.356337,-3.016287,1.961238,-2.884351,-6.250032,-4.246210,6.433959,2.959695,2.023287,-2.618537,1.771296,-5.755793,4.207860,8.695000,3.901601,-1.241883,-3.277739,-1.589922,2.950196,2.626476,-6.699454,-2.503164,3.531818,-5.238330,-6.709975,-2.826088,8.649489,5.119855,-1.458809,-1.900994,-0.947754,0.357529,4.814211,-4.618953,2.195539,9.282658,-4.009653,1.636610,8.569033,-1.436831,-6.918726,4.468759,-1.036240,-7.536998,2.763006,-5.409271,4.074190,9.195639,-1.135898,-9.976687,4.049731,9.309418,5.192092,1.654015,6.030355,-1.292323,-5.096485,1.738144,-6.753825,9.859419,-4.881224,-3.981485,-3.335684,6.707478,9.200048,-8.749724,0.238239,-9.993832,-6.655551,3.825006,-6.636112,4.452260,3.289844,9.806662,-7.457798,6.940565,-2.298268,-8.551677,7.412022,8.748173,4.029422,5.067454,-2.250866,7.881825,1.855834,-0.204708,-4.133418,6.820953,-1.684679,-3.719958,3.233909,-4.524710,7.828243,-1.797981,-8.095496,5.694726,7.910997,-2.427168,0.173915,-0.253456,-3.717174,-1.143227,-3.857274,-9.299357,-5.658360,6.307689,-5.059952,4.397281,2.713760,0.432260,-0.435765,0.591701,2.334727,9.735822,-5.417455,-0.881578,-3.692107,3.369184,-1.088180,4.427106,-0.992538,-7.990135,-5.004120,-3.082448,-5.667304,0.506493,7.493586,-4.749487,-8.212163,5.122406,-9.988480,4.151821,-0.976207,6.266594,-9.266892,9.121875,-6.620014,-9.667808,1.449395,-5.786348,-7.324028,-3.007645,-4.754226,-2.547555,-9.560817,0.426619,8.043322,4.289367,-6.413377,-1.334796,-9.537628,4.284464,-0.797582,3.171337,6.214041,2.172056,-1.981020,7.634621,-5.262894,9.945088,6.290621,4.763120,-9.261910,-9.128967,-3.979677,5.176052,-2.968748,1.355879,-3.494782,-2.912922,-7.378348,8.036744,-2.352804,9.924317,1.262689,5.872250,-0.338287,7.135250,-2.922644,1.786591,4.224391,8.329418,1.023080,-4.803399,6.196397,9.429224,-3.985625,-2.958116,8.896857,8.635737,1.714626,3.685793,-7.538828,-9.142096,-0.752359,0.770910,-5.888470,5.048040,8.000616,-0.699050,1.581181,-6.104738,-1.755413,-2.241619,-0.251914,-8.087692,-2.336077,8.404100,4.309717,2.276889,6.874585,3.552390,4.186645,-7.515638,-6.463946,-1.939910,-7.026466,2.138813,2.043220,7.449927,0.036641,2.309657,9.435711,-2.672117,-8.087942,6.452398,-0.866921,-0.583199,4.589014,-5.235543,3.660953,4.425252,7.934338,-8.031631,-4.420657,3.676196,-2.051937,-8.454393,5.909317,-9.517660,-1.124563,-5.538351,-6.351142,0.578006,9.450074,5.712026,-3.015493,-4.031080,3.028066,-4.063505,-6.434000,1.035844,0.891711,1.275126,1.248955,-4.253093,9.863121,-9.801854,3.611468,7.560613,-6.735723,0.594641,-6.113293,-7.479769,7.419050,3.123841,-3.624552,-8.303852,-9.377204,0.827358,9.756557,-9.429153,-0.919452,-3.729241,-2.413295,-3.561530,-7.424184,9.255981,8.344895,-8.453891,-5.952357], dtype = "float32")#candidate|7980|(864,)|const|float32
call_7979 = relay.TupleGetItem(func_6310_call(relay.reshape(const_7980.astype('float32'), [864,])), 1)
call_7981 = relay.TupleGetItem(func_6313_call(relay.reshape(const_7980.astype('float32'), [864,])), 1)
func_6857_call = mod.get_global_var('func_6857')
func_6858_call = mutated_mod.get_global_var('func_6858')
call_7986 = relay.TupleGetItem(func_6857_call(), 0)
call_7987 = relay.TupleGetItem(func_6858_call(), 0)
func_7182_call = mod.get_global_var('func_7182')
func_7187_call = mutated_mod.get_global_var('func_7187')
var_7990 = relay.var("var_7990", dtype = "uint16", shape = (1, 104))#candidate|7990|(1, 104)|var|uint16
const_7991 = relay.const([-10,4,8,-5,-8,-10,7,-4,-6,-4,6,5,5,-10,2,2,6,5,9,6,7,10,7,-1,-1,-9,7,10,-9,4,2,5,-2,-4,2,-10,-6,-5,6,-8,-4,-5,1,2,-10,1,-4,1,-7,-9,-5,-10,-1,7,-4,6,4,-7,-1,-4,7,2,-2,-7,8,-9,-7,5,5,-7,7,-7,9,5,-4,8,2,3,10,2,6,-10,-10,2,9,6,-7,6,-8,-3,-9,6,-10,7,8,10,1,-8,-7,8,-2,-1,-9,4,-9,2,7,-1,-4,8,6,-8,8,-9,6,8,-2,-8,5,8,8,-1,-7,-3,9,-3,-9,-3,6,-9,-9,-2,-5,2,4,-3,-2,-9,-5,10,-6,-10,-5,-4,-6,5,2,-6,10,7,10,6,2,-10,2,4,4,-4,8,-2,-3,-10,6,9,4,2,6,7,-5,-9,-1,-6,-7,-6,10,-1,-6,-5,-9,-10,2,8,-10,-6,-5,4,7,3,-2,-1,8,5,-5,10,-5,-6,4,5,-10,-1,-7,3,6,-10,-6,1,4,-9,6,-4,2,10,-5,-10,-9,2,-7,-9,-10,3,1,9,2,6,-1,-1,-10,7,-9,10,9,1,6,10,1,3,9,-9,4,-9,6,6,-2,-9,3,6,-1,9,-10,-5,-4,3,2,2,-7,-9,-10,9,1,2,7,-5,8,-8,-4,-7,3,2,4,-1,7,-4,-6,-1,-10,8,-3,-8,6,-7,-10,9,-8,9,6,-3,-2,10,-1,-3,-3,10,6,7,5,4,-2,-1,5,10,-1,-4,3,1,6,9,-6,7,9,6,10,3,5,2,-5,-3,9,-9,3,8,-3,9,6,-1,-2,2,7,5,9,-1,-2,-1,2,-3,10,-4,-8,4,3,-2,-2,-8,-8,-10,2,1,6,3,2,4,-9,8,-5,3,8,2,8,1,-5,-4,2,1,7,-5,1,-4,-10,-8,-5,-1,-6,2,-3,1,4,4,-1,4,-8,7,-10,10,3,3,8,-8,-6,-10,5,-8,-7,5,-9,3,9,9,-3,7,8,2,5,10,-4,4,-2,-10,-7,6,-5,-3,1,4,-2,9,-5,6,3,-3,6,8,-10,-6,5,-4,1,5,-1,7,1,3,-7,6,-5,-10,-8,1,-7,6,-9,2,-8,-3,7,-2,5,6,2,-5,3,-10,-2,-9,-9,10,-3,-9,9,-10,5,-5,-5,4,5,8,3,-6,-8,5,-8,-7,-7,-2,2,3,3,-8,10,-8,9,2,-4,10,-3,-3,-2,-4,7,-7,9,6,1,10,6,-8,-6,9,-9,5,-6,5,-9,8,6,-6,-7,-6,-6,2,8,7,2,-7,-6,5,1,7,8,7,-3,8,7,10,2,-5,4,6,9,9,6,-5,-3,-8,-10,-4,9,-4,-5,10,-8,10,1,10,-7,-5,-2,-1,-7,-5,-3,-1,-2,-9,-7,6,5,9,-2,-4,-7,-4,-1,5,2,-6,-10,9,10,-9,-6,4,3,-5,-2,5,-2,-10,2,3,-7,2,4,9,9,4,-3,5,2,10,-3,-3,4,7,1,3,-9,-5,-6,10,2,-9,2,2,7,8,-9,-4,8,-10,-3,7,5,6,6,-7,10,5,3,8,9,10,8,-2,7,-5,2,2,-4,1,6,10,5,2,1,7,-5,-10,1,1,-4,6,-10,5,9,-6,5,5,-9,7,-4,-2,1,3,-5,-10,3,-5,6,-9,-6,-4,-10,3,5,-3,-6,9,8,9,-8,-2,-7,-4,-7,-10,7,-3,2,-10,6,9,8,-9,-1,2,9,10,3,9,-6,-4,-4,2,5,-4,-3,2,10,-10,4,-2,-9,9,6,-1,-8,5,-4,-9,-9,9,-7,-5,-4,9,8,1,4,9,-9,-2,7,-10,-4,-9,3,7,9,-8,-9,-3,8,6,5,2,8,-2,3,8,-10,-2,-5,2,1,8,-6,-8,-6,-8,10,2,6,-4,5,-6,-7,7,-7,7,-8,-1,6,9,-4,3,-7,-3,-9,1,9,1,8,-9,9,-7,10,1,7,-10,-9,6,-7,10,-6,-2,-2,10,-10,-7,4,6,-1,-2,9,1,4,-7,-8,7,-9,8,1,-1,8,8,3,-8,2,-5,1,-10,-5,3,3,-7,8,-6,-5,10,7,7,-3,-8,-6,-6,1,1,-5,9,-6,-10,4,-5,-3,4,2,-3,8,-8,4,-1,-1,1,7,-4,8,9,-2,-3,-7,8,-10,-4,10,-3,7,-9,4,-6,2,6,-8,4,-7,-8,5,4,6,-4,-2,-1,8,-9,10,7,-9,-3,-6,-8,5,-7,-3,4,1,-4,-4,1,-4,8,10,-7,-6,8,1,-5,6,-7,-3,6,10,6,-6,-7,1,-6,9,-2,8,-7,9,-3,3,2,2,1,-10,5,-6,-6,-8,-10,8,3,1,2,3,-5,-7,4,6,3,-2,10,3,-7,-10,9,8,-3,4,-10,-3,3,3,1,-3,-5,-3,5,3,-6,-10,1,10,10,9,3,7,4,-3,1,-9,3,1,9,-3,-9,1,2,5,-7,3,8,6,-10,-9,7,7,-2,-9,4,-6,-4,6,10,9,6,5,-2,8,-10,-4,4,4,-2,7,-4,1,-9,5,8,5,5,-2,1,-8,-6,5,-4,8,-3,-1,7,4,-1,-5,2,-5,-2,-2,6,3,4,3,-10,-3,-5,9,-8,-8,-3,-10,-5,-1,-1,-9,5,-8,-3,-9,2], dtype = "uint16")#candidate|7991|(1040,)|const|uint16
call_7989 = relay.TupleGetItem(func_7182_call(relay.reshape(var_7990.astype('uint16'), [13, 8, 1]), relay.reshape(const_7991.astype('uint16'), [13, 8, 10]), relay.reshape(call_7970.astype('float64'), [182, 1]), ), 0)
call_7992 = relay.TupleGetItem(func_7187_call(relay.reshape(var_7990.astype('uint16'), [13, 8, 1]), relay.reshape(const_7991.astype('uint16'), [13, 8, 10]), relay.reshape(call_7970.astype('float64'), [182, 1]), ), 0)
func_6857_call = mod.get_global_var('func_6857')
func_6858_call = mutated_mod.get_global_var('func_6858')
call_7993 = relay.TupleGetItem(func_6857_call(), 0)
call_7994 = relay.TupleGetItem(func_6858_call(), 0)
uop_7997 = relay.acos(bop_7975.astype('float64')) # shape=(16, 14, 14)
uop_7999 = relay.acos(bop_7978.astype('float64')) # shape=(16, 14, 14)
output = relay.Tuple([call_7931,var_7932,const_7933,call_7942,var_7943,var_7944,call_7970,var_7971,call_7979,const_7980,call_7986,call_7989,var_7990,const_7991,call_7993,uop_7997,])
output2 = relay.Tuple([call_7934,var_7932,const_7933,call_7945,var_7943,var_7944,call_7972,var_7971,call_7981,const_7980,call_7987,call_7992,var_7990,const_7991,call_7994,uop_7999,])
func_8007 = relay.Function([var_7910,var_7932,var_7943,var_7944,var_7971,var_7990,], output)
mod['func_8007'] = func_8007
mod = relay.transform.InferType()(mod)
var_8008 = relay.var("var_8008", dtype = "int64", shape = (16, 14, 14))#candidate|8008|(16, 14, 14)|var|int64
var_8009 = relay.var("var_8009", dtype = "float32", shape = (234,))#candidate|8009|(234,)|var|float32
var_8010 = relay.var("var_8010", dtype = "bool", shape = (126,))#candidate|8010|(126,)|var|bool
var_8011 = relay.var("var_8011", dtype = "float64", shape = (7, 165))#candidate|8011|(7, 165)|var|float64
var_8012 = relay.var("var_8012", dtype = "int64", shape = (63, 3))#candidate|8012|(63, 3)|var|int64
var_8013 = relay.var("var_8013", dtype = "uint16", shape = (1, 104))#candidate|8013|(1, 104)|var|uint16
output = func_8007(var_8008,var_8009,var_8010,var_8011,var_8012,var_8013,)
func_8014 = relay.Function([var_8008,var_8009,var_8010,var_8011,var_8012,var_8013,], output)
mutated_mod['func_8014'] = func_8014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6185_call = mod.get_global_var('func_6185')
func_6187_call = mutated_mod.get_global_var('func_6187')
call_8024 = relay.TupleGetItem(func_6185_call(), 0)
call_8025 = relay.TupleGetItem(func_6187_call(), 0)
output = call_8024
output2 = call_8025
func_8028 = relay.Function([], output)
mod['func_8028'] = func_8028
mod = relay.transform.InferType()(mod)
mutated_mod['func_8028'] = func_8028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8028_call = mutated_mod.get_global_var('func_8028')
call_8029 = func_8028_call()
output = call_8029
func_8030 = relay.Function([], output)
mutated_mod['func_8030'] = func_8030
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8051 = relay.var("var_8051", dtype = "bool", shape = (13, 6, 1))#candidate|8051|(13, 6, 1)|var|bool
const_8052 = relay.const([[[False,False,True,True,False,True,True,False,False,False,False,True,True,False],[True,True,False,False,True,False,False,False,True,False,True,False,True,False],[False,True,False,True,True,True,False,True,False,True,False,False,True,False],[True,False,False,True,True,False,True,False,False,True,False,False,False,False],[False,True,False,False,False,False,True,True,True,True,True,True,False,True],[True,True,True,False,True,True,True,False,True,True,True,True,False,True]],[[True,False,True,True,False,True,False,False,True,True,False,False,True,True],[True,True,False,False,True,True,True,False,False,False,True,True,True,False],[False,False,True,False,False,True,True,False,False,True,True,False,True,True],[False,False,False,False,True,False,False,False,True,True,True,True,False,False],[False,True,False,False,True,True,False,False,False,False,False,True,True,True],[True,False,False,True,False,False,True,False,False,False,False,True,True,True]],[[False,True,True,False,True,True,True,False,True,True,False,True,True,True],[False,True,False,True,True,True,True,False,True,False,False,False,False,False],[True,False,False,False,True,True,False,False,True,True,True,False,True,True],[True,False,False,False,True,True,True,True,False,False,True,True,True,True],[True,True,True,True,True,True,True,True,True,True,True,False,True,False],[False,False,False,True,False,False,True,False,True,True,True,True,True,False]],[[True,False,True,False,False,False,True,True,False,False,False,True,False,False],[True,True,False,True,True,False,False,True,True,False,True,False,True,False],[False,False,False,True,True,True,True,True,False,True,False,False,True,True],[True,True,True,False,False,True,True,True,False,True,True,True,True,False],[True,False,True,True,True,True,False,False,True,False,True,True,True,True],[True,False,False,False,False,True,False,False,True,True,False,True,False,True]],[[False,False,True,True,False,False,True,True,False,True,True,True,True,False],[False,False,False,True,True,False,True,True,False,True,True,True,False,True],[False,False,False,False,False,False,True,True,False,False,False,False,False,False],[True,True,False,True,False,False,False,True,True,True,False,True,False,True],[False,False,True,False,True,True,False,True,True,True,False,False,False,True],[False,False,True,False,True,True,True,True,False,False,False,True,True,False]],[[False,False,False,False,False,True,False,True,False,False,True,False,True,True],[False,True,False,False,True,True,False,True,True,False,False,True,False,True],[False,True,True,False,True,True,False,False,False,False,True,True,False,False],[True,True,False,True,True,False,True,False,False,False,True,True,False,False],[False,False,True,False,True,False,False,True,False,False,True,False,False,False],[True,False,True,False,True,True,True,False,True,True,True,True,True,False]],[[False,True,False,False,True,True,False,False,False,False,True,False,False,False],[False,False,True,False,False,False,False,False,True,False,False,False,True,True],[False,False,False,False,True,False,True,False,False,True,False,False,False,False],[False,False,False,False,True,True,False,True,True,True,True,False,True,False],[True,False,True,True,False,True,True,True,False,False,True,False,False,True],[False,False,True,False,False,False,False,True,True,True,True,True,False,False]],[[True,True,False,False,True,False,True,True,True,True,False,True,True,True],[True,True,False,True,True,False,True,False,False,False,True,True,True,False],[False,True,True,False,False,True,False,True,True,False,False,True,True,False],[False,False,True,False,False,True,True,True,True,True,True,True,True,True],[True,False,True,True,True,False,True,True,False,False,False,True,False,False],[False,True,False,True,True,True,True,True,False,False,True,False,True,False]],[[True,False,True,False,False,True,False,True,True,True,False,True,True,False],[True,True,False,True,False,False,False,False,True,True,True,False,False,False],[False,True,True,True,False,False,False,False,True,False,False,True,True,False],[False,True,True,True,False,True,True,True,False,True,True,True,True,False],[True,True,True,True,False,False,True,False,False,True,True,False,True,True],[True,False,True,True,True,False,True,False,False,False,True,False,True,False]],[[True,False,False,True,True,True,False,False,True,True,False,False,False,True],[False,True,False,True,False,False,False,True,False,True,True,False,True,False],[False,True,False,False,True,True,True,True,False,True,True,False,True,True],[False,True,True,False,True,True,True,True,True,True,False,False,True,False],[False,False,False,True,True,True,True,True,False,False,False,False,True,True],[False,False,False,False,False,True,False,True,True,True,False,False,True,False]],[[False,False,False,True,False,True,False,False,False,True,True,False,True,True],[False,False,False,True,True,False,True,True,False,False,False,True,True,False],[True,False,False,False,False,True,True,True,False,True,True,False,False,False],[False,True,True,False,True,True,True,False,True,True,True,True,True,True],[False,False,True,False,True,False,False,True,True,True,False,True,False,True],[True,False,True,True,True,False,True,False,True,True,True,True,False,False]],[[False,True,False,True,True,True,True,False,True,True,False,False,False,False],[True,False,False,False,False,True,True,True,False,True,True,True,False,False],[False,False,True,True,True,True,False,False,False,True,True,False,False,True],[False,False,True,False,False,True,False,False,True,False,True,True,True,False],[False,True,True,True,True,False,False,False,True,False,False,True,True,True],[True,True,False,False,True,False,False,True,True,False,True,False,False,False]],[[True,True,False,False,False,True,True,True,True,True,True,False,True,False],[False,False,True,True,True,False,True,False,False,True,True,True,False,False],[False,False,False,True,False,False,True,False,False,False,False,True,True,True],[False,False,True,False,False,True,True,True,True,True,True,True,False,False],[False,False,False,False,True,False,False,True,True,True,True,True,False,True],[False,True,True,False,False,False,False,False,True,False,False,False,True,True]]], dtype = "bool")#candidate|8052|(13, 6, 14)|const|bool
bop_8053 = relay.logical_or(var_8051.astype('bool'), const_8052.astype('bool')) # shape=(13, 6, 14)
output = bop_8053
output2 = bop_8053
func_8058 = relay.Function([var_8051,], output)
mod['func_8058'] = func_8058
mod = relay.transform.InferType()(mod)
mutated_mod['func_8058'] = func_8058
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8059 = relay.var("var_8059", dtype = "bool", shape = (13, 6, 1))#candidate|8059|(13, 6, 1)|var|bool
func_8058_call = mutated_mod.get_global_var('func_8058')
call_8060 = func_8058_call(var_8059)
output = call_8060
func_8061 = relay.Function([var_8059], output)
mutated_mod['func_8061'] = func_8061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6730_call = mod.get_global_var('func_6730')
func_6732_call = mutated_mod.get_global_var('func_6732')
call_8080 = relay.TupleGetItem(func_6730_call(), 1)
call_8081 = relay.TupleGetItem(func_6732_call(), 1)
func_4118_call = mod.get_global_var('func_4118')
func_4121_call = mutated_mod.get_global_var('func_4121')
const_8083 = relay.const(-1, dtype = "uint8")#candidate|8083|()|const|uint8
var_8084 = relay.var("var_8084", dtype = "uint8", shape = (1215,))#candidate|8084|(1215,)|var|uint8
call_8082 = relay.TupleGetItem(func_4118_call(relay.reshape(const_8083.astype('uint8'), []), relay.reshape(var_8084.astype('uint8'), [1215,]), ), 5)
call_8085 = relay.TupleGetItem(func_4121_call(relay.reshape(const_8083.astype('uint8'), []), relay.reshape(var_8084.astype('uint8'), [1215,]), ), 5)
func_4953_call = mod.get_global_var('func_4953')
func_4956_call = mutated_mod.get_global_var('func_4956')
const_8096 = relay.const([[2.867681],[-0.211206],[-9.810467],[6.582317],[-8.396775],[9.027392],[5.975163],[8.112396],[-3.640042],[-8.031449],[-2.999019],[-5.258510],[-8.382452],[-4.399539],[7.961948],[8.774172],[2.926963],[-5.004071],[-8.493923],[-1.153233],[-1.173188],[5.278355],[-7.538212],[1.678704],[2.337472],[-1.153697],[-5.073407],[-6.215471],[-6.815670],[3.813942],[2.267382],[-4.456326],[4.906282],[-1.324221],[-1.465668],[-7.204107],[6.579375],[4.623976],[-6.569147],[-6.019015],[-4.040346],[6.115278],[2.691179],[-7.691329],[-2.455052],[-9.541156],[-5.816926],[8.715071],[7.307980],[0.820567],[-6.991193],[-4.641779],[-4.059627],[8.204103],[-2.865403],[-4.056705],[-1.613983],[-5.728698],[2.077692],[3.546669],[-9.943101],[3.273957],[-0.605641],[-8.509796],[-1.250134],[1.748302],[-2.768526],[-1.619786],[5.481960],[9.666866],[1.458550],[8.684868],[-3.335641],[-6.333954],[-8.180543],[0.526219],[2.767069],[3.757729],[8.600146],[6.818107],[-1.012399],[-1.324668],[-1.991266],[4.592051],[-7.684342],[4.853837],[-9.326692],[3.956368],[-9.661006],[-0.427701],[0.608016],[-8.008508],[-1.138506],[-5.459118],[0.079553],[4.455845],[5.929656],[-9.021790],[1.193347],[8.684634],[5.752443],[7.319108],[3.423131],[-0.475319],[-0.311446],[-1.414264],[-8.162946],[-5.569933],[8.672491],[8.948456],[-8.265122],[-5.430918],[-2.461163],[4.016638],[-4.414691],[-1.034439],[-6.087671],[4.232443],[-6.035185],[8.344149],[-9.115234],[8.540694],[-7.084137],[7.028342],[-1.943957],[0.553309],[7.500866],[-0.652373],[-0.588970],[2.127687],[6.134607],[-7.036415],[-0.674915],[4.139018],[2.367813],[9.833212],[0.181554],[8.276814],[5.080756],[8.800319],[6.216801],[-4.191333],[-9.254389],[-1.954099],[9.744538],[5.107548],[9.951870],[-5.809832],[1.280005],[0.609429],[-8.171885],[-1.507769],[5.634612],[-2.169940],[-3.369627],[-4.721901],[-4.432927],[-1.143429],[-5.776238],[0.041801],[4.688325],[-4.393621],[4.760736],[-9.837936],[-9.864856],[9.736471],[-1.202977],[-0.498697],[6.117000],[-7.763272],[-9.746024],[9.263112],[-9.718566],[2.916785],[6.236222],[-0.423381],[7.620268],[9.350046],[0.323473],[3.452606],[7.020602],[-5.458337],[-2.835626],[9.837031],[3.603132],[6.561363],[3.830507],[-1.107112],[2.852688],[-7.151255],[3.212092],[6.781569],[1.763134],[5.325025],[-4.634939],[-7.997606],[6.755602],[7.833891],[-5.012633],[-0.148993],[0.984564],[8.145513],[-0.693024],[-4.506002],[-8.035416],[-2.175730],[2.162881],[-2.584039],[6.139503],[3.162758],[7.043385],[2.349293],[-5.707009],[-9.803831],[-9.302867],[9.213969],[9.438726],[-6.077706],[-2.498951],[2.981529],[2.395158],[-2.504156],[6.209743],[5.853989],[-1.131439],[-8.291017],[-0.272298],[9.148097],[-7.549116],[1.341257],[-1.215114],[-9.032185],[-4.047135],[5.665277],[3.767598],[2.407833],[2.828310],[4.435838],[-8.171503],[6.120429],[1.143832],[-4.271993],[6.256335],[7.849711],[-3.654551],[-6.849087],[8.341928],[-9.526090],[3.288935],[-9.746879],[-8.947142],[1.486512],[-9.219362],[-4.146462],[1.711613],[4.737493],[5.066822],[3.386179],[9.833538],[-4.238579],[1.582463],[-2.167277],[-8.507958],[-9.001200],[1.493961],[-4.806586],[-9.025261],[5.721457],[2.664351],[-7.275546],[8.219490],[3.579947],[0.783993],[9.975378],[0.084861],[-9.562888],[5.077501],[3.599800],[3.144647],[5.587307],[3.724435],[-1.205352],[-4.372908],[-7.189099],[3.886765],[-2.972518],[-4.484930],[3.952413],[-5.718688],[5.773884],[3.289426],[6.833662],[-4.129515],[-0.645938],[-4.855497],[-4.269893],[0.606484],[-4.819766],[-2.973703],[2.955629],[6.818586],[-6.994582],[-2.969136],[0.843481],[6.840696],[-5.122938],[3.102262],[6.752121],[0.008830],[8.719552],[0.169954],[1.356354],[4.570863],[-9.292478],[-4.880397],[6.640279],[-8.078851],[6.384305],[-4.341565],[6.820381],[6.431497],[-7.802745],[7.438037],[0.796335],[7.845241],[1.585612],[-1.791334],[8.900807],[-9.270713],[-6.612074],[-4.371172],[-6.738996],[9.973137],[1.846911],[-2.916780],[5.327663],[-1.275872],[-5.723004],[2.888988],[-4.991014],[7.971258],[-5.183800],[-4.616450],[4.796634],[3.931600],[2.522702],[8.720491],[-1.831453],[-8.761815],[-3.579539],[5.437805],[-1.973213],[3.752762],[2.932060],[-3.816507],[0.781157],[1.372331],[-0.375697],[-1.103869],[-1.796185],[8.669247],[4.017642],[3.023656],[6.055197],[5.019963],[4.010963],[-1.270557],[-5.171093],[-4.089095],[-9.328554],[-2.789135],[-3.357428],[3.404846],[9.305545],[-9.171670],[-8.490860],[-9.416055],[9.151611],[1.522379],[4.170397],[-8.282151],[5.568412],[-3.544898],[3.596890],[-9.594085],[-0.909861],[5.428098],[-1.612120],[5.086274],[-5.374977],[-2.689113],[2.026390],[-1.134264],[-6.745688],[4.075247],[-6.945088],[-0.731832],[-4.812724],[-9.248550],[-2.439885],[-7.424034],[2.291822],[5.775262],[-1.137120],[8.558994],[5.815185],[8.588098],[-9.031757],[6.128163],[-1.162483],[-8.456748],[-7.120043],[-4.329294],[-0.272748],[-9.293501],[2.862807],[7.910110],[2.581491],[2.878869],[8.042207],[-8.572079],[-4.146101],[7.157619],[-1.006010],[5.261994],[5.467878],[4.196539],[1.251490],[0.902364],[-0.828715],[-9.239656],[-9.384685],[-8.409966],[-6.422643],[6.923339],[8.179597],[-3.240394],[-3.204708],[-4.555152],[-9.129360],[0.579603],[-8.540481],[-5.412800],[-6.575603],[8.978144],[0.030574],[3.985756],[0.728670],[2.013205],[7.817772],[6.674369],[8.534781],[-5.955711],[9.014406],[-8.897977],[-8.351789],[2.311707],[-7.777951],[-6.054580],[1.044186],[-6.067194],[5.036776],[-7.296976],[3.777818],[4.689744],[7.520744],[6.212528],[-1.412297],[-2.245047],[9.661512],[-3.519887],[-6.760205],[-9.658118],[0.476486],[6.917084],[-9.058700],[4.895876],[8.720772],[-5.571827],[-7.941889],[4.661757],[-2.592768],[-9.176011],[-5.649788],[-5.418979],[4.511873],[-1.403310],[-9.372343],[-5.515726],[2.522479],[9.722085],[3.395301],[-5.801460],[-8.303415],[-8.643744],[-6.021694],[-4.448793],[-2.403355],[2.391991],[2.218468],[-3.884425],[-2.531021],[-7.981501],[8.283650],[-1.164419],[6.679815],[-4.727825],[5.800829],[9.566142],[1.781318],[-4.176298],[-3.200073],[-4.883783],[0.537798],[2.741719],[1.676975],[8.681798],[-4.219675],[7.995083],[-4.123322],[3.575763],[7.862945],[6.743157],[-9.866694],[-0.370128],[-6.743742],[6.336185],[-1.850281],[4.645521],[6.657122],[-8.482015],[7.047247],[6.608919],[-8.563009],[0.229052],[-5.545218],[-2.657930],[3.300095],[-5.103628],[-8.618634],[5.669002],[1.540463],[6.278135],[0.157700],[9.780304],[-9.773919],[5.191711],[7.796901],[3.129789],[4.990744],[0.436962],[5.623929],[4.637794],[6.687555],[-6.152461],[7.193299],[-6.464006],[-9.987159],[-7.263125],[-9.363684],[1.259768],[5.008170],[-7.535499],[4.762910],[-3.611553],[9.105768],[-3.058220],[2.417995],[1.879677],[-5.684620],[7.389842],[8.074531],[-8.520452],[5.209432],[8.261310],[6.854392],[-3.588006],[-4.310327],[6.840629],[0.621898],[-2.442849],[2.429739],[3.601662],[5.131190],[7.962530],[1.412592],[7.137461],[-2.065982],[-2.520426],[-5.682084],[-8.752513],[-1.805718],[-6.029033],[1.519001],[-7.139611],[-8.834999],[8.952977],[-9.067019],[-7.205435],[6.047965],[9.955762],[-7.927495],[-6.508724],[-7.021644],[7.300232],[-2.516508],[-7.730083],[-1.185509],[6.861988],[2.548904],[-5.482764],[9.276737],[5.074217],[1.442318],[2.530434],[-8.462029],[5.400658],[2.723322],[3.611454],[-5.011194],[-9.564688],[-0.957616],[-3.226914],[4.640479],[6.210372],[5.777419],[-9.244396],[8.199525],[-0.078861],[-4.539002],[-0.549219],[-2.105513],[7.922233],[5.602776],[-7.766814],[3.397482],[-0.486380],[7.877662],[3.878022],[7.108647],[9.126865],[-7.841512],[9.210839],[-3.359138],[-0.335316],[0.383421],[4.755390],[-6.715536],[9.493726],[6.308541],[-0.850720],[-4.494975],[1.597675],[7.251669],[-1.980288],[9.760383],[6.449342],[-2.060358],[4.014183],[7.925944],[6.353016],[-4.165836],[-2.502229],[2.064248],[-2.872758],[5.618584],[-0.025169],[-2.306171],[-8.623382],[-8.588341],[-2.415624],[-8.964502],[0.909922],[-9.932758],[2.926058],[9.158708],[-8.871018],[4.448601],[-2.233470],[-5.437549],[-0.796493],[6.399972],[6.793980],[-5.385983],[4.181846],[-4.816151],[-0.328174],[-1.951795],[1.275912],[-8.739610],[-2.874611],[8.890555],[-6.988054],[5.282931],[-4.445632],[3.166596],[-7.930636],[0.986577],[-3.477303],[6.832822],[-5.975151],[1.979544],[-1.861052],[-8.098375],[-3.780073],[7.881180],[-0.525313],[1.217579],[8.116212],[-5.206701],[-3.563981],[-4.857469],[-1.226013],[-0.803816],[8.934924],[5.029999],[-1.103032],[-6.347504],[-4.412393],[-4.783054],[-0.408595],[0.308276],[2.229883],[5.794162],[9.276838],[-6.208394],[3.692971],[-9.161775],[-1.134430],[3.055176],[-0.050493],[4.655138],[0.791697],[-7.703033],[-3.118797],[5.525986],[-4.672954],[-4.838629],[6.891005],[-1.934631],[7.268793],[9.157029],[-9.332573],[-8.525772],[-9.424299],[-2.360131],[-4.155695],[0.279655],[-7.241062],[8.858721],[5.006575],[9.988090],[7.579034],[6.063828],[9.411855],[-8.123462],[-8.468128],[1.490553],[4.548417],[5.713602],[3.469640],[7.277380],[9.290800],[-2.550909],[-8.786263],[-5.949316],[-3.271073],[7.767852],[8.279627],[-0.627773],[-4.898058],[6.238633],[-3.090653],[9.553596],[0.572965],[-0.998894],[4.636847],[-3.801845],[-1.652796],[-9.253351],[3.311186],[-8.354260],[-8.098277],[8.825133],[-6.729884],[-2.572464],[-9.462222],[1.666749],[-5.211766],[2.506852],[6.185114],[5.527249],[5.947762],[9.504484],[-2.331328],[-0.525592],[1.562243],[9.606044],[-6.124777],[9.182133],[-2.375148],[2.598935],[-2.635520],[-0.998362],[-6.413583],[-7.439249],[0.244472],[-1.648657],[7.150508],[-3.237944],[6.323762],[3.114007],[-4.196275],[-4.855986],[-4.985818],[9.563139],[7.383804],[7.274294],[-7.365842],[-0.132077],[8.123276],[-8.296520],[-3.699835],[0.480610],[8.683318],[6.763304],[-3.289945],[0.424831],[7.255802],[2.013375],[7.353838],[7.635666],[-9.180799],[-1.700975],[-8.261069],[7.532556],[7.033175],[-5.134026],[-5.634231],[-6.231192],[7.922020],[-7.555259],[-4.639407],[-2.364339],[5.506874],[2.912879],[6.844166],[6.694513],[-0.159027],[-0.787908],[-5.836881],[-6.328285],[3.215332],[-6.381120],[1.607392],[7.693408],[-1.449160],[-5.147921],[9.704760],[5.316525],[4.073200],[-9.436718],[1.185571],[-7.729556],[0.434472],[-3.347226],[-4.290658],[-3.069219],[9.489875],[3.252832],[7.003391],[5.628351],[-5.036526],[-5.724795],[2.950443],[-7.597741],[4.929249],[3.252392],[-6.020579],[-6.294145],[-3.009278],[6.516740],[3.398083],[-5.339885],[-4.272821],[7.293167],[0.017614],[-1.514461],[4.801808],[3.538514],[-0.888449],[8.410709],[-3.721752],[-4.517638],[-3.420146],[1.530000],[0.509900],[5.258969],[-2.572810],[7.599915],[6.945675],[-4.085137],[7.399287],[-7.283856],[4.751539],[6.764807],[3.087266],[9.529875],[6.931711],[-6.301164],[-2.000790],[-9.912782],[-1.631573],[8.726849],[-1.856900],[-8.835302],[3.923031],[-3.468809],[4.178139],[5.624344],[-6.328675],[-1.667723],[5.949778],[-5.895905],[1.198822],[-7.276204],[-8.542657],[8.797480],[-8.841866],[2.708919],[4.202512],[-2.893589],[-0.331394],[2.398705],[3.304479],[-9.041707],[-6.509093],[9.362420],[4.955366],[-9.610197],[-4.016664],[-2.720923],[-1.051275],[-6.487453],[-0.380552],[3.473544],[2.444909],[8.823065],[-0.692234],[3.700062],[3.144571],[6.492261],[-3.865153],[-8.932506],[-0.596640],[-0.342521],[3.799112],[0.866092],[-0.596464],[4.807353],[2.084259],[-9.715763],[-3.077355],[-6.519653],[-4.970929],[4.309133],[-8.757853],[4.536721],[3.413587],[-1.530359],[5.913570],[8.290738],[0.660594],[-4.795917],[-5.249630],[3.065901],[-0.065689],[-4.080364],[0.975241],[7.627862],[-8.948138],[5.488660],[3.450849],[9.812156],[-4.725591],[9.433685],[-3.491547],[1.815380],[4.887365],[3.043354],[3.585043],[-3.542005],[-6.755799],[-7.767944],[1.659179],[3.639713],[-1.891748],[-7.775717],[-3.072726],[4.367784],[8.881670],[-4.116604],[8.941420],[-8.092066],[1.735279],[-1.559142],[-5.295207],[-0.358752],[4.347454],[-4.521344],[-5.322633],[-2.735618],[-4.248599],[-1.729229],[-8.155787],[-0.257126],[-5.281988],[8.136550],[-7.173386],[5.233419],[5.322413],[-6.817278],[-7.100607],[-0.087757],[6.978807],[-3.986439],[-7.774624],[0.768585],[-0.652871],[0.106993],[2.822805],[-9.531259],[-1.460429],[7.833940],[5.526565],[-9.407761],[-7.154976],[-1.124435],[8.965797],[-3.799853],[0.052902],[-4.402629],[9.317620],[3.991397],[-6.765297],[-9.834246],[-7.540664],[5.828416],[-4.312776],[5.580824],[4.696748],[-9.579595],[-3.648839],[-8.126153],[8.716213],[-4.367860],[-3.274207],[-9.661435],[-2.258758],[2.424977],[4.370740],[-3.271011],[-7.308349],[-2.826058],[-6.584272],[2.224714],[-1.916844],[8.824305],[-6.932269],[-8.711671],[-7.267797],[4.707661],[-5.784448],[-5.163561],[9.829461],[1.970699],[2.415620],[-5.744867],[8.714065],[-6.162121],[-1.599684],[-7.038025],[9.242470],[5.063965],[4.640336],[4.662716],[-6.973743],[-0.233262],[6.198938],[-9.424201],[-4.313948],[4.878085],[5.516888],[-3.461327],[-7.829293],[3.120345],[-2.544354],[8.429261],[4.773024],[5.137173],[6.277766],[0.469960],[1.693024],[-1.832993],[-9.467323],[0.936977],[-9.499327],[1.640085],[-4.983164],[-6.417705],[-8.534893],[6.174144],[8.923382],[6.670398],[9.423088],[-5.693759],[0.979236],[1.674004],[1.086892],[1.321422],[-1.810950],[0.467907],[1.461288],[-1.607089],[-9.231256],[7.041799],[-0.682018],[5.295685],[6.533843],[0.124832],[5.427504],[1.411183],[7.581791],[-4.482327],[-4.380037],[-1.621962],[-2.833759],[2.641460],[-1.019484],[-6.654964],[3.236969],[-0.604824],[-7.681598],[5.309562],[-8.942519],[9.020169],[-3.920505],[-8.584859],[0.819235],[6.530360],[4.375447],[-2.866138],[2.429631],[0.589794],[9.919401],[-1.593363],[4.856432],[2.480120],[-9.454613],[-3.574991],[9.367767],[-9.198456],[-1.952424],[3.265582],[7.066819],[-9.181530],[-9.606209],[1.680624],[-0.155709],[-6.215629],[-5.514848],[-5.233117],[0.518508],[6.656399],[7.944800],[-7.162627],[7.768450],[-0.585628],[7.252428],[7.384282],[-0.194331],[5.892974],[-9.910632],[-1.902099],[-3.037199],[2.499708],[6.186999],[-0.800396],[4.382010],[-0.803612],[8.949550],[3.895545],[-1.445078],[5.576949],[8.286545],[-5.843580],[-4.809090],[-4.432630],[-2.607642],[6.596755],[5.388257],[4.724802],[3.254105],[9.881021],[-1.484847],[3.571945],[-6.124308],[-9.546501],[-6.083978],[4.481428],[4.591231],[-4.045163],[0.756007],[-4.492439],[1.772123],[-4.614044],[-5.146105],[-4.194721],[-5.558328],[-6.371052],[4.933705],[-6.911954],[-2.274103],[-3.999286],[-1.259306],[-7.428386],[-1.431683],[4.837374],[-4.131943],[1.901034],[-9.885715],[-1.297435],[-0.498620],[-7.322332],[1.358569],[7.966605],[-5.552368],[-4.482174],[-9.153490],[8.315064],[-7.911863],[-8.838491],[-0.338496],[9.874597],[-7.968676],[9.136562],[-0.383754],[6.978347],[-5.277191],[5.604628],[7.498245],[-9.641611],[2.510167],[-1.129609],[-6.401252],[-0.063261],[-2.022221],[1.381349],[2.177763],[6.900626],[0.443468],[-9.339827],[-6.165479],[-1.832378],[0.012394],[-6.398534],[-1.434201],[-6.898013],[-4.686435],[-2.013165],[-5.039452],[6.152599],[1.032299],[-8.392203],[2.062296],[-6.352769],[-2.853629],[6.374639],[7.036600],[7.125768],[4.060237],[5.813454],[-1.091984],[3.280860],[-2.827997],[5.899427],[7.200066],[6.754679],[6.482005],[8.193689],[2.970150],[-5.294172],[-8.056825],[0.865787],[7.198680],[-9.751456],[-7.566982],[4.637008],[3.419568],[7.027286],[-6.124119],[-4.550254],[-3.613466],[-9.974722],[8.867880],[-4.413992],[-8.619381],[-0.355897],[-1.494165],[-4.344724],[-5.783810],[5.678848],[-0.674321],[-9.875292],[1.667253],[2.352328],[-2.731362],[3.717190],[-0.072323],[2.129334],[8.728798],[-4.831712],[-4.037667],[-4.919077],[-2.691742],[-5.985087],[9.335273],[-8.662006],[-0.837682],[8.588577],[-5.141054],[6.685604],[3.952428],[8.679284],[9.992012],[5.661901],[9.174117],[-6.329029],[2.716027],[-1.102190],[3.005106],[-5.624481],[-3.054381],[-5.258986],[8.556378],[8.843998],[-1.736873],[9.624693],[4.148137],[2.935255],[9.441532],[-7.092070],[1.621437],[-9.178089],[3.213920],[-7.046620],[4.808628],[-3.378428],[1.985438],[8.889342],[-2.954795],[6.323421],[8.491785],[-9.742318],[5.813881],[8.582920],[0.200745],[7.762194],[-1.218241],[3.283586],[6.144039],[-4.351107],[-1.425028],[-4.417507],[2.610911],[4.682156],[-2.158224],[2.643562],[7.275065],[8.557103],[3.737987],[9.027200],[-1.977080],[1.253687],[-8.272847],[-8.777301],[7.248491],[-9.890609],[4.281181],[4.802275],[-6.651842],[4.527300],[8.633542],[5.207932],[-5.188926],[-4.922833],[8.964988],[-9.050878],[-8.459870],[6.766522],[-2.282564],[-2.558764],[-0.747252],[-5.770495],[-6.139708],[6.974303],[-5.671993],[2.248693],[0.039977],[-2.160724],[5.433731],[2.485001],[-6.961358],[-2.362227],[-2.827856],[4.025914],[-8.521557],[-6.158171],[-4.045273],[-4.498602],[-4.821224],[-0.077426],[-2.467810],[5.850795],[-4.724620],[-0.262112],[-1.339844],[-0.480574],[9.737422],[9.127299],[-0.399429],[0.189787],[3.692940],[-2.466600],[-0.046437],[-7.120493],[-4.419994],[4.226102],[-0.675155],[-2.971412],[-0.211427],[8.930118],[-0.344431],[4.086045],[-5.657943],[5.806526],[0.882669],[4.275040],[-5.112592],[-6.998997],[9.489976],[-3.431896],[9.192275],[-4.347038],[-5.093503],[-9.988844],[8.095235],[2.299212],[-9.965857],[-0.686894],[3.469529],[2.154541],[-0.329373],[9.220807],[-4.115201],[1.396285],[-2.820948],[6.566824],[3.360891],[-9.384668],[-3.313393],[-6.779513],[-9.265432],[-5.642049],[-7.526653],[9.796917],[-5.484347],[-4.354798],[-6.842101],[-3.388917],[9.946776],[-1.485416],[0.663722],[-6.059556],[4.479992],[-1.296432],[8.893665],[-1.265596],[-6.108058],[-3.214144],[4.050901],[-6.071926],[3.920185],[-3.324347],[8.966447],[-5.147185],[-0.670416],[-0.940695],[9.852354],[-2.139825],[5.380358],[-7.115627],[9.832298],[-9.088710],[7.889410],[-9.606356],[5.872310],[3.243471],[4.763899],[-1.595679],[-0.531566],[9.496962],[7.045939],[-2.767266],[-4.053261],[7.718865],[3.518690],[2.092373],[-2.287454],[-9.707169],[-9.181637],[-9.190614],[7.308418],[-4.910918],[8.765089],[8.482493],[-4.496137],[-7.835695],[4.884888],[-7.371655],[0.713161],[1.408650],[0.333706],[0.029461],[5.438821],[-5.016181],[-4.527607],[5.422273],[-5.381680],[-8.047781],[-3.719976],[5.370251],[2.668866],[-5.219225],[-0.829272],[-4.098475],[-8.289041],[-1.877044],[-6.075074],[-5.549324],[6.031607],[-7.719318],[6.210652],[9.796886],[2.391091],[-5.290661],[-1.129322],[-1.715026],[6.994795],[-1.484452],[0.493240],[-6.471734],[-9.940136],[-1.462506],[-2.062139],[-4.136791],[2.054886],[-9.781507],[-3.670356],[-8.704094],[3.334335],[5.886330],[-4.130047],[5.853822],[-4.018762],[0.021167],[9.938224],[-7.437345],[-8.276691],[-4.460790],[8.464700],[-6.499785],[8.225730],[0.938488],[-9.469798],[-1.815411],[-2.036601],[9.462770],[0.276165],[7.789416],[-5.714305],[-1.883483],[-2.423650],[-2.877977],[9.398270],[7.200701],[8.630665],[8.034100],[-1.258354],[1.815776],[-6.767290],[3.529006],[5.550201],[7.066055],[4.740217],[7.803709],[1.117651],[7.589558],[-5.303066],[-4.982005],[2.811687],[-4.632814],[1.193441],[8.760322],[-6.994178],[-2.048417],[-4.825987],[-9.412377],[1.311108],[9.475539],[-4.663078],[-1.249398],[-0.682712],[1.782488],[3.859850],[-6.549365],[9.228258],[-5.299384],[-3.967286],[0.333639],[-2.241577],[4.143676],[7.431139],[-6.604486],[7.881393],[5.592596],[-2.249373],[5.703394],[-1.567039],[5.558113],[-1.600841],[-0.939972],[-7.907761],[-3.009449],[-7.374704],[-7.122009],[2.437722],[-9.946561],[3.754892],[4.889866],[-9.077302],[-5.696312],[2.581454],[5.358776],[-9.754614],[2.596260],[-9.545138],[-2.625605],[-5.680049],[7.016499],[-6.782804],[2.792280],[5.365710],[-9.539971],[0.057415],[5.192972],[9.805535],[-3.425587],[1.417698],[-6.639024],[4.801985],[-0.014161],[5.332407],[-2.741446],[6.582740],[-3.908640],[4.335664],[4.427441],[8.618236],[4.724375],[-7.817460],[-6.439000],[-9.901835],[-7.773926],[-1.408236],[0.753726],[-9.123138],[7.686382],[2.656525],[-5.331182],[4.605752],[-9.027272],[-2.127170],[6.978137],[-9.398866],[-8.866377],[5.505996],[-7.743492],[-0.679470],[8.518188],[7.035131],[-6.641342],[-7.642668],[0.681181],[0.283723],[-7.663317],[-4.331830],[-1.392166],[1.368406],[9.432240],[-1.881257],[-8.808524],[-0.879900],[-5.567360],[1.816334],[-6.794958],[-8.454098],[-9.729156],[-7.725478],[-2.880050],[0.951591],[5.921187],[-5.208488],[2.967213],[3.042914],[5.120109],[-2.998632],[-3.952297],[-4.467256],[8.042403],[-2.023209],[-8.466509],[-9.549889],[-1.897530],[-4.076091],[9.871892],[7.395712],[8.791953],[-0.478754],[3.268541],[6.413058],[1.670596],[-4.804340],[1.880243],[-9.866836],[-5.667943],[-1.891063],[-2.325937],[-4.540936],[1.792527],[3.597505],[-0.314745],[7.012717],[-8.202588],[-6.037517],[-5.388261],[-1.916936],[-1.800794],[6.386321],[4.352676],[-2.290294],[-5.497295],[-4.918214],[-5.559087],[9.018190],[1.002825],[-5.154148],[-0.853222],[-9.142779],[3.224247],[-6.859575],[-9.254055],[7.946249],[-2.345294],[-6.538992],[0.826835],[3.310516],[6.948793],[-4.558876],[-2.442013],[-9.281870],[-8.462598],[-3.120820],[-1.767337],[-8.994178],[2.073378],[5.527798],[6.252476],[-3.069718],[6.032551],[-2.691832],[-3.637417],[0.698165],[0.138609],[9.553178],[2.730735],[-0.223405],[-2.560263],[-4.180406],[3.811742],[-9.159060],[-8.037623],[-6.985094],[-7.606384],[4.691609],[-4.096709],[-4.688983],[7.641158],[-9.410909],[2.615037],[8.002067],[4.689164],[4.282594],[-8.200548],[1.431831],[-8.544983],[-2.753897],[9.068793],[-2.032873],[-2.198140],[-2.325898],[1.450411],[8.839500],[-1.338140],[-2.276435],[7.443691],[-3.862501],[1.927130],[-5.904511],[-9.876845],[0.034956],[9.606814],[2.629845],[-0.130504],[-0.002364],[7.105232],[5.619091],[-0.566358],[1.738870],[2.326434],[-2.152269],[1.454449],[4.221151],[-5.397448],[-7.598065],[8.733404],[0.027714],[-1.780540],[-1.407158],[7.658388],[5.247967],[6.823250],[8.056190],[9.965095],[-5.076674],[-2.224933],[9.578054],[6.189559],[-2.166587],[-3.412986],[-9.039683],[-0.484629],[-9.600896],[-0.767550],[-2.668630],[8.526395],[-9.842913],[-5.156002],[-9.321517],[3.978764],[-9.262151],[-8.576621],[8.721172],[8.621560],[4.281049],[5.723138],[8.757421],[-1.186067],[-6.373677],[-6.213134],[-6.608758],[-5.766450],[-5.692788],[-3.806621],[-4.476796],[9.164414],[-7.745633],[-7.176844],[-9.700475],[5.929944],[0.618313],[6.916503],[6.510577],[-4.807291],[9.678125],[-3.252355],[-9.791749],[-9.215688],[3.909834],[-1.375718],[-5.139688],[9.543997],[3.476458],[4.781735],[9.804336],[4.054769],[5.272228],[5.798983],[-9.298324],[-0.493483],[0.819090],[2.520842],[0.084148],[-7.279044],[7.386737],[-0.505626],[8.922075],[-5.266705],[7.114868],[-4.308334],[-0.401069],[2.707377],[-6.287572],[-0.848378],[-1.464571],[-8.412648],[0.109269],[8.121274],[-9.079484],[-0.208268],[-3.131684],[6.111788],[-6.885497],[-9.904294],[9.419868],[-2.257981],[4.127495],[8.028105],[-2.154074],[-9.729171],[-3.564292],[-8.028241],[3.149984],[-1.142517],[-0.920042],[4.463650],[1.391004],[-8.975353],[-1.019788],[6.940539],[9.433448],[3.862885],[0.984338],[-0.736466],[9.535782],[-2.417283],[-2.603319],[0.768706],[9.714557],[2.132187],[-9.486366],[-4.654147],[0.453940],[5.374181],[-3.172505],[-4.518641],[-5.231915],[-8.336258],[-7.355152],[-6.795432],[7.286623],[-1.870683],[0.539869],[1.976772],[0.757276],[-5.451915],[0.362294],[-4.591236],[8.044729],[-6.693860],[-0.203128],[6.235461],[0.551640],[1.743127],[5.905854],[6.350423],[-3.664092],[-3.097530],[4.762295],[-3.555061],[-6.750385],[3.793945],[-0.195234],[-0.029605],[8.813010],[8.517282],[6.582587],[4.351203],[-2.764731],[3.379744],[-2.831981],[-5.002962],[-3.320897],[-0.725383],[2.736478],[-2.036670],[-3.848794],[9.136186],[2.499631],[-9.084085],[2.413532],[4.208299],[8.608901],[4.051731],[5.175982],[4.685777]], dtype = "float64")#candidate|8096|(2016, 1)|const|float64
call_8095 = relay.TupleGetItem(func_4953_call(relay.reshape(call_8080.astype('float32'), [2, 13, 5]), relay.reshape(const_8096.astype('float64'), [2016, 1]), ), 1)
call_8097 = relay.TupleGetItem(func_4956_call(relay.reshape(call_8080.astype('float32'), [2, 13, 5]), relay.reshape(const_8096.astype('float64'), [2016, 1]), ), 1)
uop_8106 = relay.atanh(var_8084.astype('float64')) # shape=(1215,)
bop_8110 = relay.logical_xor(uop_8106.astype('uint32'), relay.reshape(var_8084.astype('uint32'), relay.shape_of(uop_8106))) # shape=(1215,)
output = relay.Tuple([call_8080,call_8082,const_8083,call_8095,const_8096,bop_8110,])
output2 = relay.Tuple([call_8081,call_8085,const_8083,call_8097,const_8096,bop_8110,])
func_8116 = relay.Function([var_8084,], output)
mod['func_8116'] = func_8116
mod = relay.transform.InferType()(mod)
var_8117 = relay.var("var_8117", dtype = "uint8", shape = (1215,))#candidate|8117|(1215,)|var|uint8
output = func_8116(var_8117)
func_8118 = relay.Function([var_8117], output)
mutated_mod['func_8118'] = func_8118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6768_call = mod.get_global_var('func_6768')
func_6770_call = mutated_mod.get_global_var('func_6770')
call_8155 = relay.TupleGetItem(func_6768_call(), 0)
call_8156 = relay.TupleGetItem(func_6770_call(), 0)
output = relay.Tuple([call_8155,])
output2 = relay.Tuple([call_8156,])
func_8157 = relay.Function([], output)
mod['func_8157'] = func_8157
mod = relay.transform.InferType()(mod)
mutated_mod['func_8157'] = func_8157
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8157_call = mutated_mod.get_global_var('func_8157')
call_8158 = func_8157_call()
output = call_8158
func_8159 = relay.Function([], output)
mutated_mod['func_8159'] = func_8159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6119_call = mod.get_global_var('func_6119')
func_6121_call = mutated_mod.get_global_var('func_6121')
call_8198 = func_6119_call()
call_8199 = func_6119_call()
output = call_8198
output2 = call_8199
func_8203 = relay.Function([], output)
mod['func_8203'] = func_8203
mod = relay.transform.InferType()(mod)
output = func_8203()
func_8204 = relay.Function([], output)
mutated_mod['func_8204'] = func_8204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6195_call = mod.get_global_var('func_6195')
func_6196_call = mutated_mod.get_global_var('func_6196')
call_8267 = relay.TupleGetItem(func_6195_call(), 0)
call_8268 = relay.TupleGetItem(func_6196_call(), 0)
output = call_8267
output2 = call_8268
func_8269 = relay.Function([], output)
mod['func_8269'] = func_8269
mod = relay.transform.InferType()(mod)
mutated_mod['func_8269'] = func_8269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8269_call = mutated_mod.get_global_var('func_8269')
call_8270 = func_8269_call()
output = call_8270
func_8271 = relay.Function([], output)
mutated_mod['func_8271'] = func_8271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5333_call = mod.get_global_var('func_5333')
func_5335_call = mutated_mod.get_global_var('func_5335')
call_8283 = relay.TupleGetItem(func_5333_call(), 0)
call_8284 = relay.TupleGetItem(func_5335_call(), 0)
func_8028_call = mod.get_global_var('func_8028')
func_8030_call = mutated_mod.get_global_var('func_8030')
call_8287 = func_8028_call()
call_8288 = func_8028_call()
func_6768_call = mod.get_global_var('func_6768')
func_6770_call = mutated_mod.get_global_var('func_6770')
call_8290 = relay.TupleGetItem(func_6768_call(), 0)
call_8291 = relay.TupleGetItem(func_6770_call(), 0)
func_5625_call = mod.get_global_var('func_5625')
func_5628_call = mutated_mod.get_global_var('func_5628')
call_8298 = func_5625_call(relay.reshape(call_8287.astype('float64'), [2, 13, 5]))
call_8299 = func_5625_call(relay.reshape(call_8287.astype('float64'), [2, 13, 5]))
output = relay.Tuple([call_8283,call_8287,call_8290,call_8298,])
output2 = relay.Tuple([call_8284,call_8288,call_8291,call_8299,])
func_8305 = relay.Function([], output)
mod['func_8305'] = func_8305
mod = relay.transform.InferType()(mod)
output = func_8305()
func_8306 = relay.Function([], output)
mutated_mod['func_8306'] = func_8306
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8321 = relay.var("var_8321", dtype = "float64", shape = (9, 11, 11))#candidate|8321|(9, 11, 11)|var|float64
uop_8322 = relay.sigmoid(var_8321.astype('float64')) # shape=(9, 11, 11)
func_499_call = mod.get_global_var('func_499')
func_501_call = mutated_mod.get_global_var('func_501')
var_8327 = relay.var("var_8327", dtype = "bool", shape = (3136,))#candidate|8327|(3136,)|var|bool
call_8326 = relay.TupleGetItem(func_499_call(relay.reshape(var_8327.astype('bool'), [16, 14, 14])), 0)
call_8328 = relay.TupleGetItem(func_501_call(relay.reshape(var_8327.astype('bool'), [16, 14, 14])), 0)
func_5981_call = mod.get_global_var('func_5981')
func_5982_call = mutated_mod.get_global_var('func_5982')
call_8329 = func_5981_call()
call_8330 = func_5981_call()
output = relay.Tuple([uop_8322,call_8326,var_8327,call_8329,])
output2 = relay.Tuple([uop_8322,call_8328,var_8327,call_8330,])
func_8332 = relay.Function([var_8321,var_8327,], output)
mod['func_8332'] = func_8332
mod = relay.transform.InferType()(mod)
mutated_mod['func_8332'] = func_8332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8332_call = mutated_mod.get_global_var('func_8332')
var_8334 = relay.var("var_8334", dtype = "float64", shape = (9, 11, 11))#candidate|8334|(9, 11, 11)|var|float64
var_8335 = relay.var("var_8335", dtype = "bool", shape = (3136,))#candidate|8335|(3136,)|var|bool
call_8333 = func_8332_call(var_8334,var_8335,)
output = call_8333
func_8336 = relay.Function([var_8334,var_8335,], output)
mutated_mod['func_8336'] = func_8336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_8359 = relay.TupleGetItem(func_3534_call(), 2)
call_8360 = relay.TupleGetItem(func_3536_call(), 2)
output = call_8359
output2 = call_8360
func_8364 = relay.Function([], output)
mod['func_8364'] = func_8364
mod = relay.transform.InferType()(mod)
mutated_mod['func_8364'] = func_8364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8364_call = mutated_mod.get_global_var('func_8364')
call_8365 = func_8364_call()
output = call_8365
func_8366 = relay.Function([], output)
mutated_mod['func_8366'] = func_8366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4825_call = mod.get_global_var('func_4825')
func_4826_call = mutated_mod.get_global_var('func_4826')
call_8469 = relay.TupleGetItem(func_4825_call(), 0)
call_8470 = relay.TupleGetItem(func_4826_call(), 0)
func_4825_call = mod.get_global_var('func_4825')
func_4826_call = mutated_mod.get_global_var('func_4826')
call_8471 = relay.TupleGetItem(func_4825_call(), 0)
call_8472 = relay.TupleGetItem(func_4826_call(), 0)
func_5211_call = mod.get_global_var('func_5211')
func_5214_call = mutated_mod.get_global_var('func_5214')
const_8475 = relay.const([-0.359514,5.425186,4.290907,-7.445494,-7.237008,1.599002,2.746485,-9.452748,-2.076952,-5.809390,-4.090529,9.740994,-2.168173,9.364726,5.259720,5.320208,1.231677,3.139400,2.897212,0.900197,9.018062,1.936661,-6.678087,-3.675158,7.474219,2.134109,3.790094,-2.451529,3.821587,9.872334,9.552131,5.217236,-6.588765,9.541224,-7.715156,8.852940,-8.984230,-5.686238,-9.704248,5.110777,-4.702342,6.072092,3.921512,6.040461,6.102553,6.173147,0.975673,-7.126631,5.218401,-8.903170,-5.611663,-7.381825,-7.849769,-9.481277,2.709378,-5.666975,-4.539401,2.456223,-4.895247,-4.046295,-7.249928,-0.999354,-9.834951,9.562020,-9.398711,7.407777,4.556199,3.983717,4.286857,2.089179,1.755124,-0.347417,4.358835,7.047686,-4.070671,-1.943502,8.908859,1.701059,8.862757,-3.340789,-6.027542,-6.674315,9.956000,0.376300,4.362617,2.882967,6.061839,-5.206186,0.937177,-2.635122], dtype = "float32")#candidate|8475|(90,)|const|float32
call_8474 = relay.TupleGetItem(func_5211_call(relay.reshape(const_8475.astype('float32'), [5, 3, 6]), relay.reshape(const_8475.astype('float64'), [5, 3, 6]), ), 1)
call_8476 = relay.TupleGetItem(func_5214_call(relay.reshape(const_8475.astype('float32'), [5, 3, 6]), relay.reshape(const_8475.astype('float64'), [5, 3, 6]), ), 1)
func_6071_call = mod.get_global_var('func_6071')
func_6075_call = mutated_mod.get_global_var('func_6075')
const_8481 = relay.const([[-2,-1,-4,7,5,3,-4,-9,7,3,-9,5,-7,-8,5,-6,1,-3,8,-4,-5,-6,-6,-6,-10,5,7,9,-8,-4,-1,1,10,6,5,10,-6,9,-1,5,3,3,1,-3,8,-4,-10,10,1,7,-7,6,-3,-5,1,8,-1,3,4,3,-7,-3,-5],[8,-1,4,2,-9,-6,-9,-8,10,-1,-1,2,7,2,8,-4,-3,-3,-1,6,10,-8,-8,10,-4,-2,-6,-3,-6,2,2,2,9,2,-10,1,2,-1,-4,10,-1,-6,-9,-9,-2,8,-9,1,6,7,4,8,-7,-6,-1,8,-9,9,1,-2,1,1,10],[7,7,-2,3,-7,-8,-1,9,2,-4,-5,-1,10,-7,-3,4,3,-7,2,-6,2,2,-4,3,-1,7,3,-3,3,5,6,-7,9,-5,-5,10,6,9,4,-6,-8,-3,2,-4,-7,-10,-8,-4,-2,-8,10,2,-1,-6,4,2,-6,3,-4,-2,7,5,-10],[2,8,6,-7,5,-1,5,-2,5,3,-5,-6,7,10,7,-1,-1,9,6,-8,-8,-2,4,1,4,-9,10,-8,9,10,-10,-6,-7,-10,3,-6,7,-3,5,-10,7,-10,7,5,-7,-1,-6,-8,2,-8,6,-7,3,3,1,7,-5,6,-6,-5,7,-8,4],[6,5,-10,-7,3,-6,-9,2,-6,4,8,-4,1,-10,2,8,-10,1,2,-9,-9,-3,-4,6,-3,-4,10,-5,-9,3,-1,-9,-4,2,-10,2,8,10,10,3,-8,-4,5,3,-4,-7,-7,-5,9,-8,-8,10,6,7,-8,1,7,6,5,-8,-6,-6,-3],[6,8,-1,-2,2,1,-6,-2,-2,-2,-3,-8,8,7,-8,4,-2,-6,9,-2,-6,2,9,-8,-5,1,-9,-10,-4,-10,-7,4,7,2,8,8,-6,-7,-6,-10,-7,-8,2,3,7,10,-10,-5,6,4,1,9,4,-4,3,9,5,-8,7,4,-7,-8,-9],[-7,-8,1,2,-9,-8,-7,7,2,-5,-10,2,-4,10,-9,5,-4,-6,4,-4,4,-8,-4,-9,10,7,-4,-7,1,2,-6,5,-2,6,-8,-3,-4,-5,9,-7,8,10,-4,-2,-2,-4,-3,-10,-9,-5,7,-3,-8,-1,2,5,-1,-2,9,9,-2,10,1],[2,-6,-1,2,6,-10,-6,-5,2,5,-1,2,6,3,9,5,8,-10,-4,10,-4,-7,7,-3,-9,5,-3,-2,-10,4,-10,3,-10,-6,-5,6,-1,2,-6,8,-3,7,-1,4,5,1,9,-5,8,5,10,-3,-4,-10,9,-8,-1,8,-6,-3,4,-6,9],[4,-5,-1,10,-7,-10,-7,-4,-3,1,-7,8,8,6,-3,-7,4,-7,8,-2,4,-1,3,7,2,-9,-5,-1,-7,8,3,8,-9,4,-2,2,10,-8,-1,-9,1,4,-3,8,3,1,-1,-5,5,8,8,5,5,1,6,-9,-7,4,1,1,8,-9,-2],[9,-6,5,7,1,3,8,-9,-10,-3,6,6,5,1,3,10,1,1,1,-7,-1,-4,4,7,2,8,-1,7,-8,-2,2,-5,2,-10,-5,5,1,-5,3,-9,-2,-2,5,1,-8,6,-6,4,8,-1,2,7,3,8,-5,-10,-8,-8,-4,6,-1,-3,-3],[7,2,2,-1,-7,4,2,-2,4,7,-3,-2,-4,-1,-2,-5,-6,6,-10,1,-5,3,-2,-2,-7,10,-9,-8,7,-9,4,9,-10,7,6,-7,3,-8,7,3,8,-3,-6,-9,8,2,-1,-1,-8,1,6,-4,-8,-6,-4,-6,-10,9,-9,9,-8,9,-3],[-10,-1,-6,-9,-8,5,-9,-2,-1,-3,10,-9,-1,-1,-6,-3,9,9,2,8,-4,-3,1,-7,10,3,4,-9,10,-7,6,5,3,1,-4,5,-1,1,6,6,-10,3,4,-10,2,1,9,-3,1,-8,-2,-3,5,-7,-1,-4,6,6,-1,-4,-6,-3,2],[7,-10,10,-10,-7,6,6,8,10,-9,-2,5,-5,1,-3,-6,8,-7,-9,3,4,9,1,-9,-1,-7,1,9,4,4,4,-10,-5,3,6,10,-9,9,8,1,10,-10,-2,7,-10,-3,-2,-7,10,2,9,-5,3,-8,-5,8,-7,-4,-9,2,3,-4,-8],[1,4,-3,5,1,3,-9,-6,-4,7,-9,1,6,9,-1,2,7,5,-10,10,-10,-1,-3,-8,-10,-5,9,-2,-1,6,10,-4,-7,8,1,7,1,2,4,1,3,5,-1,9,-10,4,7,8,6,9,4,-9,-5,10,-1,5,4,-7,9,-9,-5,10,2],[5,-5,-5,2,3,7,9,4,-3,6,-5,10,-3,-10,6,-10,-10,-7,4,-1,9,10,-9,3,-3,3,-3,6,7,-6,8,6,-3,-4,-4,-3,4,-2,8,-6,8,2,4,5,4,8,1,1,-9,-10,10,8,9,-9,-9,9,-6,-7,9,-4,7,-6,-6]], dtype = "uint16")#candidate|8481|(15, 63)|const|uint16
var_8482 = relay.var("var_8482", dtype = "uint8", shape = (1215, 1))#candidate|8482|(1215, 1)|var|uint8
call_8480 = relay.TupleGetItem(func_6071_call(relay.reshape(const_8481.astype('uint16'), [945,]), relay.reshape(var_8482.astype('uint8'), [9, 9, 15]), ), 5)
call_8483 = relay.TupleGetItem(func_6075_call(relay.reshape(const_8481.astype('uint16'), [945,]), relay.reshape(var_8482.astype('uint8'), [9, 9, 15]), ), 5)
output = relay.Tuple([call_8469,call_8471,call_8474,const_8475,call_8480,const_8481,var_8482,])
output2 = relay.Tuple([call_8470,call_8472,call_8476,const_8475,call_8483,const_8481,var_8482,])
func_8487 = relay.Function([var_8482,], output)
mod['func_8487'] = func_8487
mod = relay.transform.InferType()(mod)
var_8488 = relay.var("var_8488", dtype = "uint8", shape = (1215, 1))#candidate|8488|(1215, 1)|var|uint8
output = func_8487(var_8488)
func_8489 = relay.Function([var_8488], output)
mutated_mod['func_8489'] = func_8489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4635_call = mod.get_global_var('func_4635')
func_4637_call = mutated_mod.get_global_var('func_4637')
call_8533 = relay.TupleGetItem(func_4635_call(), 0)
call_8534 = relay.TupleGetItem(func_4637_call(), 0)
output = relay.Tuple([call_8533,])
output2 = relay.Tuple([call_8534,])
func_8537 = relay.Function([], output)
mod['func_8537'] = func_8537
mod = relay.transform.InferType()(mod)
output = func_8537()
func_8538 = relay.Function([], output)
mutated_mod['func_8538'] = func_8538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6119_call = mod.get_global_var('func_6119')
func_6121_call = mutated_mod.get_global_var('func_6121')
call_8539 = func_6119_call()
call_8540 = func_6119_call()
func_5365_call = mod.get_global_var('func_5365')
func_5369_call = mutated_mod.get_global_var('func_5369')
var_8555 = relay.var("var_8555", dtype = "float32", shape = (117, 1))#candidate|8555|(117, 1)|var|float32
call_8554 = relay.TupleGetItem(func_5365_call(relay.reshape(var_8555.astype('float32'), [13, 3, 3]), relay.reshape(var_8555.astype('float32'), [13, 3, 3]), ), 0)
call_8556 = relay.TupleGetItem(func_5369_call(relay.reshape(var_8555.astype('float32'), [13, 3, 3]), relay.reshape(var_8555.astype('float32'), [13, 3, 3]), ), 0)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_8564 = relay.TupleGetItem(func_3534_call(), 0)
call_8565 = relay.TupleGetItem(func_3536_call(), 0)
func_7472_call = mod.get_global_var('func_7472')
func_7475_call = mutated_mod.get_global_var('func_7475')
const_8579 = relay.const([True,True,False,False,True,False,True,False,True,True,True,False,False,True,False,False,True,True,True,False,False,False,True,False,True,False,False,True,False,False,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True,True,False,False,False,False,False,False,False,False,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,False,False,True,False,False,True,True,False,True,False,False,True,False,True,True,False,True,False,True,True,True,True,False,False,False,True,True,True,True,True,False,False,False,True,False,False,False,True,True,False,True,True,True,False,True], dtype = "bool")#candidate|8579|(126,)|const|bool
const_8580 = relay.const([3.434512,-8.570910,-7.962618,-1.151197,4.032230,-9.334539,-4.061591,3.145853,-2.002756,-4.196474,-0.489867,7.666419,8.756037,-6.142820,4.577784,4.465949,-3.125534,-8.164027,-9.038517,-6.361629,6.097950,4.452202,0.664582,8.673051,1.266738,5.003312,-0.166976,5.332957,-3.492949,7.585102,1.306752,-4.936454,-6.143630,1.179899,1.338296,-1.109490,-9.636842,6.821793,-8.305412,9.599652,-8.746135,-4.264016,6.537916,-4.916482,0.899186,4.192288,5.410073,-9.865871,-2.344280,-0.762849,8.740546,-9.813261,-9.686586,-8.364233,-4.409815,-9.674478,-2.922854,-7.454047,-9.448332,5.732004,-3.066327,1.813149,-5.861021,6.858874,8.577793,-6.856163,-1.431306,-0.196749,-2.057867,9.335020,-6.407174,4.867826,-8.154313,-9.352674,8.451897,-1.643000,-4.839799,4.028296,8.321596,6.417958,-5.826504,-3.762981,9.398914,8.432038,5.244638,-2.364842,1.054712,-5.424458,9.736134,-6.017302,-8.516406,-9.796290,-7.469128,1.071098,-7.135819,-6.456178,-9.497568,4.423797,6.476296,-0.447416,-9.887423,-6.582302,-8.270307,9.160646,5.842452,-1.431434,1.578353,-5.242222,-2.840931,1.884198,9.333688,9.696999,-9.016955,3.649564,-4.539586,-9.343816,-2.018255,-8.343861,8.221776,4.042237,8.440619,-3.374178,-0.597558,4.766417,-0.388642,-4.261094,-5.031999,-3.768271,-2.856080,1.455539,5.688841,9.436513,-6.576102,-2.620642,-0.654137,6.424444,-2.395152,-9.722428,-6.224699,6.917474,-6.719520,-6.257711,-6.312994,-3.155191,-9.916768,6.065202,9.228873,-9.388356,-8.796204,-3.304740,-7.331718,-4.362024,4.339285,4.861914,-3.016874,8.277452,-7.615467,-7.592042,-3.422872,-7.463828,-3.595665,-9.727478,-8.876983,3.198747,2.142533,0.390025,7.963638,-5.923649,-9.322373,2.194377,3.988963,-8.798937,-1.745217,-3.450681,6.592367,-6.327895,-5.653110,1.770316,0.906718,8.641958,-4.875437,-1.583859,-4.155969,7.991775,-6.161707,-2.931345,6.513739,-8.054138,5.882654,-5.209653,8.991777,-1.513625,5.422258,-8.382609,-3.186610,9.687973,7.506622,0.237928,7.953018,-9.305622,1.843403,0.106973,8.817330,-0.284525,-8.061843,0.771013,1.930411,8.942792,-0.182181,6.322894,3.502197,8.247136,-5.743795,-0.218691,3.582002,-6.538413,4.024145,6.361839,7.666449,5.707757,-4.597738,4.934241,-8.696577,-5.564252,-2.037774,-5.667110,5.231418,-0.525001,-4.687313,0.290242,-4.210617,-5.589946,1.218340,-2.542021,6.693439,-2.782421,3.139694,-7.466766,-4.322361,-8.607510,-8.012728,-2.916362,-1.477582,-7.786127,4.361943,0.218843,9.709448,-4.493338,1.526176,7.439745,-8.134142,2.291184,1.172752,-4.159593,-9.927378,-2.024167,1.046044,-9.781912,-3.356499,-5.649281,-2.872463,1.924702,4.967644,-4.813730,-7.733440,5.762986,0.020734,-7.945276,-2.412846,-7.316694,6.539710,-5.742993,4.167606,4.053733,6.361696,-7.722170,0.433742,5.516248,1.608568,9.590292,1.432677,-1.457202,8.008945,7.148017,7.030958,8.225766,-5.286543,3.735456,-3.850033,9.248682,-4.655199,-9.234365,5.750152,-2.978595,4.195404,2.902264,1.526861,-2.361432,-1.369998,-5.143634,2.004517,3.800876,3.449351,-8.066343,4.678836,1.282019,1.145294,4.990623,7.087721,1.150868,7.774543,5.636288,-1.592631,-5.550999,3.346442,9.471980,-9.506246,0.427120,1.808308,8.498441,1.953334,1.908078,-2.976507,-3.477749,-6.668123,3.187095,-7.964619,-7.388234,-0.781228,9.206120,-2.910494,-6.450463,6.404502,-6.635724,9.818268,3.187963,7.666497,5.221256,9.627109,8.024030,2.536968,-0.970317,-5.814735,8.694486,5.974709,-6.863059,3.180174,-7.621691,-1.593864,6.665962,-0.223680,3.475599,4.757748,-0.493744,-6.212624,6.368918,-9.253891,0.977366,-9.442062,2.539791,0.863619,3.095830,-5.809861,-1.968382,0.424394,3.633207,-1.415017,3.535644,9.929847,5.219397,5.641081,-1.591323,-9.749980,-1.153986,-7.248898,-7.507463,-3.788009,-0.280235,7.668681,5.589409,-3.733386,-2.587677,9.596866,9.023288,1.620727,-7.142038,0.539677,-3.169115,-0.328309,-9.866466,-4.941339,9.758276,6.818685,-1.037347,-5.773484,7.822644,-5.031288,6.098749,0.772795,-1.110883,1.216376,1.493441,2.249760,-1.223124,5.919467,-6.951767,6.547621,-8.745251,2.197079,4.347441,-6.252905,0.289760,2.801592,1.272051,6.959147,6.409644,-9.480182,5.869441,5.676149,-9.255597,-1.895157,-7.413533,-9.518238,-8.226813,1.737720,5.749055,-2.234461,-3.184364,5.773051,-6.466749,-7.802397,-4.779525,1.626237,-8.404404,2.394803,4.506668,-6.993083,-8.861024,-4.173245,-2.166528,-7.065336,5.616235,-2.648955,-2.587727,3.743700,-9.061450,6.401656,9.407884,-8.208378,8.102580,-6.174854,-8.450990,-3.452980,6.127141,5.407810,3.533630,9.375261,0.648555,-0.211541,3.194965,-9.318133,1.184548,-3.898252,-2.908966,9.035684,0.421152,-6.250000,-4.437794,-4.127970,0.037880,0.703038,4.173066,-4.121128,8.338779,8.795352,-5.850378,-2.389358,4.073302,-2.926392,-4.584650,0.257450,5.794737,8.334635,-0.095142,6.777665,6.811086,-3.320564,1.353432,0.882191,-0.637783,-0.301621,2.518796,-2.528642,6.213166,-0.004661,-8.108444,4.135386,-4.201449,5.674286,-1.773300,-6.886014,-6.207166,0.881690,5.310249,-9.517054,8.490606,1.793393,7.862954,1.937970,-2.433139,-2.641247,8.691924,0.777309,-5.881742,-8.651689,9.582483,2.690180,-4.355213,-8.288283,5.356484,6.702432,1.100764,2.265249,-9.934018,8.480329,6.372028,-2.195327,-0.713863,-3.868641,-2.275497,4.601132,1.938146,4.969183,2.411998,-6.580519,-9.327964,3.830512,-0.216094,4.361893,4.499314,8.241083,-0.372479,3.134233,9.843930,-8.336803,8.532127,-8.941525,-9.412692,-9.663979,6.468184,-8.659708,-7.296768,1.649557,7.718996,0.123518,7.949615,9.829068,-9.940268,-7.018688,-5.528529,-7.723598,1.303534,-5.001533,-7.162659,0.481109,5.885029,-9.615967,-7.390656,-8.346300,-2.489591,-1.549201,1.845919,3.905750,2.779326,5.586989,-0.672556,6.666650,-4.761505,5.856538,-6.660874,-4.647631,6.067144,0.620780,-1.485657,7.186160,8.329227,8.107813,2.570295,7.116390,-2.055983,-3.705695,-2.593254,-8.089822,4.882719,2.756027,3.352205,-2.327917,-4.005268,-7.313608,7.101684,3.740506,1.655823,1.551726,-4.701508,5.371689,-6.779351,9.200217,3.684632,8.809639,-3.659542,-1.086340,7.052474,-1.102480,-9.287386,-8.250555,-5.858341,0.764627,-5.559859,-7.793279,6.378388,-6.131112,3.425066,-8.070617,5.420364,2.150170,-6.322212,5.364804,-5.761405,-6.956663,-8.962295,3.933419,-4.883148,2.533674,2.828334,9.801299,1.216880,-4.847375,-9.884262,-3.098882,1.683028,9.713280,5.055053,5.818142,-2.588671,7.824743,-5.440046,9.436572,3.985546,-0.514380,-0.688889,6.791029,8.685574,-5.556838,-8.708610,0.654335,-3.685000,4.884325,-2.713692,-8.295933,-9.829173,5.376406,-0.459068,-3.366370,5.706453,-3.334258,-9.365532,-4.421709,-4.032334,1.210124,6.957408,-1.043212,7.973196,2.326830,-2.743716,-3.420834,7.089560,2.537009,-6.158769,9.981466,-4.143415,0.122672,8.623861,-1.377109,-7.441971,-2.636453,8.882758,-2.694056,1.847048,-4.976997,3.884527,-5.492689,-9.031291,-0.524583,9.797075,4.755741,8.360332,5.438447,-4.141857,-2.660983,2.949328,-2.437607,0.994477,-3.491189,-5.966221,-5.113953,5.155404,4.494227,6.903915,7.618071,9.341427,-2.772314,4.956860,-2.666918,-3.359438,2.053652,0.287538,-5.287483,-5.594932,6.932071,7.534615,-8.518961,1.609230,-4.868514,2.259569,8.634532,-4.246722,3.408362,7.222771,9.982096,8.639532,-6.920032,-1.432935,9.468236,1.925314,-8.198148,6.612559,6.297809,-3.535856,0.025989,7.809650,-8.706323,-4.226496,-0.982047,8.536871,8.433564,-7.466716,-3.417064,-6.680516,4.031871,-1.697800,-6.412466,-4.071582,-3.012557,-6.572559,-0.013307,5.288485,6.986644,-6.998327,0.448286,-6.746230,-4.795396,-6.332053,9.463680,8.811877,-4.803736,-2.583609,5.288436,4.378957,6.163697,4.662505,6.430954,3.425648,-9.312048,-1.835553,9.919422,4.030753,4.607223,-9.013292,-6.011753,6.341851,-7.671746,-4.692326,-6.097246,5.685857,2.228873,5.773715,1.885239,8.543229,8.738698,-2.417118,-4.641425,-4.751369,4.038646,8.664234,-4.629249,3.846931,-5.212793,-3.181324,2.392985,7.875081,-8.601030,9.231772,1.725855,-6.046586,8.182914,1.689947,-6.989251,8.359491,8.147437,5.071728,-5.049671,-8.084071,-2.382199,6.486263,-5.853087,-0.284615,-6.111663,6.445289,2.939955,-4.192467,-6.143840,-4.468742,9.375654,-0.284944,-4.940309,7.094289,-0.254093,-1.510252,-2.291152,-2.994161,-4.624739,-0.494476,2.464175,-1.505767,0.419846,7.562449,-4.258469,-3.133478,6.545168,-0.838399,-5.653911,-8.869555,7.015481,-8.032429,6.654243,3.874248,8.799755,-9.457754,1.827933,4.301411,5.058840,-1.382418,8.761733,7.323310,0.629251,-7.583541,2.677811,7.211869,9.170044,3.807568,-3.140802,-5.541790,-6.031416,-3.236067,2.438240,-9.076124,-3.442770,4.770799,9.007557,0.812284,-2.608942,-8.716355,-8.083123,4.573834,2.402543,-1.407389,3.653320,-3.831182,1.937409,7.625818,-6.795512,3.901997,-6.088575,-8.435441,-6.167763,-6.382796,-1.184150,-1.306515,-2.569828,-0.443668,-8.123118,-4.325830,-1.919883,5.590389,5.576871,-8.756488,-7.870113,0.843160,-0.375043,-7.495258,1.111972,-5.979790,-7.312379,-1.312313,-7.121549,-9.124924,-6.161174,-7.597592,4.410155,-5.642720,-8.518406,0.156672,7.427224,3.444728,-8.819039,-5.282480,-8.094054,8.582212,6.151102,-6.510198,4.771439,6.699288,8.708303,-5.586145,7.057888,8.918185,0.881969,6.004126,4.317132,3.567304,-7.604456,9.900995,-0.276490,6.637473,5.894847,0.623252,7.914994,-1.269070,-6.927090,8.633729,7.547911,9.215639,0.905108,7.925111,2.830957,0.471376,-3.167839,-6.424113,6.594539,4.382019,6.917466,7.255655,9.829872,4.854507,-8.055456,3.765623,-6.654290,4.591970,7.262373,-7.055212,3.816161,5.442911,8.286498,-6.753241,9.736700,2.659252,-6.565627,6.943010,-6.697392,3.291682,-7.184859,-9.763712,6.660858,-0.013352,9.852269,1.729852,-5.717838,-7.924449,-2.869114,2.609697,-4.115686,9.505370,5.693422,-8.545454,9.484822,8.533836,2.200507,-5.008575,2.034220,6.359943,-2.085973,6.510695,5.592773,-2.513732,-8.300494,-2.835531,-6.589196,6.454240,-7.232935,7.917537,7.287981,4.898226,-8.078981,9.760909,6.260002,-9.906732,0.194556,-5.250033,-5.593196,-7.955539,-2.391617,7.673162,-9.982970,8.488546,3.657061,9.441897,0.822952,0.180988,-7.234039,1.324570,2.734485,3.579499,3.086641,-9.702789,-7.036837,-6.432913,2.597124,4.476297,-8.876971,-6.274296,6.896340,-0.564036,7.622697,8.254737,-6.581941,4.726492,-1.435600,-4.416703,-8.640632,7.897752,7.929120,-8.055699,-7.577301,0.568067,-0.849037,-8.139647,2.125496,-8.391089,-1.397109,-9.247530,-9.204081,-6.754422,2.093706,-0.605337,7.979546,-6.333070,5.152517,4.964815,2.855409,-3.044911,7.784552,0.144706,9.750197,8.177171,3.256155,-0.804181,5.619837,8.292944,5.365873,-2.412514,4.785993,9.410523,3.191752,-4.799669,9.983052,-9.982076,2.854500,9.690544,5.171514,-7.488079,2.028176,-8.503902,-2.154081,4.075851,0.529076,-5.944307,-2.479799,4.331782,8.615378,-8.187815,-9.781013,2.896969,6.398754,-7.555751,9.943174,2.061710,4.077715,3.294954,4.982379,8.717422,-7.415354,-1.178315,-6.439090,3.296838,2.088160,-7.639806,-0.855153,-1.781791,9.020293,9.234975,4.030147,0.530411,-6.570524,-7.447042,4.032366,1.561404,-2.640598,-4.076142,5.041668,-4.558821,-6.563766,0.405085,-6.115033,-8.602080,-1.977711,-1.591124,-0.075668,9.570238,-7.302311,7.650373,3.428008,7.790976,-0.442321,-8.075582,6.127125,-7.684885,-1.159507,0.633273,2.055324,-1.640522,2.573813,-0.514954,-3.092372,-4.101147,1.311403,-5.424147,-8.693939,-4.855287,5.466610,4.935703,2.115562,-1.505909,3.753456,-9.280466,8.736351], dtype = "float64")#candidate|8580|(1155,)|const|float64
call_8578 = relay.TupleGetItem(func_7472_call(relay.reshape(const_8579.astype('bool'), [126,]), relay.reshape(const_8580.astype('float64'), [1, 1155]), ), 3)
call_8581 = relay.TupleGetItem(func_7475_call(relay.reshape(const_8579.astype('bool'), [126,]), relay.reshape(const_8580.astype('float64'), [1, 1155]), ), 3)
bop_8589 = relay.bitwise_xor(const_8580.astype('uint64'), var_8555.astype('uint64')) # shape=(117, 1155)
output = relay.Tuple([call_8539,call_8554,call_8564,call_8578,const_8579,bop_8589,])
output2 = relay.Tuple([call_8540,call_8556,call_8565,call_8581,const_8579,bop_8589,])
F = relay.Function([var_8555,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8555,], output2)
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
