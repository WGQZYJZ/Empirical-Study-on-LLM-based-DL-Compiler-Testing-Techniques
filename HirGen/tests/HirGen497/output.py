import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_69 = relay.var("var_69", dtype = "bool", shape = (13, 16, 14))#candidate|69|(13, 16, 14)|var|bool
const_70 = relay.const([[[True,False,False,False,False,True,False,True,False,False,False,False,True,False],[True,False,False,False,False,False,False,True,False,False,True,True,False,False],[False,False,True,True,False,True,False,True,False,False,False,False,True,False],[True,False,True,False,False,True,False,True,False,True,False,False,True,False],[True,True,False,True,True,True,True,True,True,True,False,True,True,False],[False,False,True,True,True,False,True,True,True,False,False,True,True,True],[True,False,True,False,True,True,False,False,True,True,True,False,False,False],[True,True,False,True,False,True,False,True,True,False,False,True,False,True],[False,True,False,False,True,True,False,False,False,False,False,True,True,True],[True,True,True,True,True,False,False,True,True,True,False,True,True,False],[False,True,True,False,False,True,False,True,False,True,True,True,True,True],[False,True,False,False,False,False,True,True,False,True,False,True,False,False],[False,True,True,False,False,False,True,False,False,True,True,False,False,False],[True,False,True,False,True,False,False,True,False,True,True,False,False,True],[True,True,False,False,False,True,False,True,True,True,True,True,True,True],[False,True,True,True,True,True,True,False,True,True,False,True,False,True]],[[True,True,False,False,False,False,False,False,True,True,True,True,False,True],[False,True,False,False,True,True,False,False,False,True,True,True,True,True],[False,True,False,True,False,False,False,False,True,False,True,False,True,False],[True,False,True,False,True,True,False,False,True,False,True,True,False,False],[True,True,True,True,False,True,True,True,True,True,True,False,True,False],[True,True,True,False,True,False,False,False,False,True,True,True,True,False],[False,True,False,True,False,True,True,True,False,False,False,True,True,True],[False,False,False,True,True,True,True,False,True,False,True,True,True,False],[False,False,False,True,False,False,False,False,True,True,True,True,True,True],[False,False,True,False,True,True,True,False,False,True,True,True,True,False],[True,False,False,True,False,False,False,False,False,True,True,True,False,False],[False,False,False,False,False,True,True,True,False,False,False,False,True,True],[True,False,True,False,False,True,False,True,True,False,True,True,True,False],[False,False,True,False,False,True,False,False,False,True,False,False,False,False],[False,True,True,True,False,False,False,False,True,False,True,False,False,True],[True,False,True,True,False,False,True,False,True,True,False,True,True,False]],[[True,True,False,True,False,True,True,False,True,True,True,False,True,False],[False,True,True,True,True,True,False,True,True,True,True,True,True,False],[False,False,False,False,True,True,True,True,False,False,False,False,True,True],[False,False,True,True,False,True,False,True,False,True,True,True,False,False],[False,True,False,True,True,True,True,False,False,False,False,False,True,False],[False,False,True,True,True,False,False,True,True,False,False,True,True,True],[True,False,False,True,True,False,False,True,True,True,True,True,False,True],[False,True,True,False,True,False,True,False,True,True,True,False,False,False],[False,True,True,True,True,True,False,True,False,True,False,True,False,True],[True,False,True,True,True,False,True,True,True,True,True,False,False,True],[False,False,True,False,False,False,True,True,False,False,False,False,True,False],[True,True,False,False,False,True,True,True,True,True,False,False,False,False],[False,False,True,True,True,False,True,True,False,True,False,False,True,True],[False,False,True,False,True,True,False,True,False,False,True,False,True,True],[False,True,True,True,True,False,False,False,False,True,True,True,False,False],[True,True,True,False,True,False,False,True,False,False,False,False,False,True]],[[False,True,True,True,False,False,False,False,True,False,False,True,True,False],[False,False,False,False,True,True,False,True,True,False,False,True,False,False],[False,True,False,False,False,True,True,True,True,True,True,False,True,True],[False,True,True,False,True,True,False,False,False,False,True,False,False,True],[True,True,False,True,False,False,False,False,True,True,True,False,True,False],[True,False,False,True,True,True,True,False,True,False,True,True,False,False],[True,True,False,True,False,False,False,False,False,False,False,True,False,False],[True,True,False,False,True,False,True,True,False,True,True,True,True,False],[False,True,True,False,False,True,True,False,True,True,False,True,False,True],[False,False,True,True,True,True,False,False,False,True,True,False,False,True],[True,True,True,True,True,False,True,True,True,False,False,False,False,False],[True,False,True,True,False,False,True,True,False,True,True,False,False,True],[False,True,False,True,False,True,False,True,False,False,True,True,False,True],[False,False,True,True,False,True,True,False,True,False,True,True,True,True],[True,True,False,True,False,False,False,True,True,True,False,True,True,True],[True,True,False,True,False,False,False,False,True,True,True,False,True,False]],[[False,False,True,True,False,True,True,False,True,True,True,True,False,False],[False,True,True,True,True,False,False,True,False,True,True,True,False,False],[True,False,True,True,False,False,True,False,False,False,True,True,True,False],[False,False,False,True,True,False,False,False,False,True,True,False,False,True],[True,False,True,False,False,False,False,True,True,True,True,True,True,False],[False,False,True,True,False,True,False,False,True,False,False,True,True,False],[True,True,True,False,False,False,True,False,True,True,True,False,False,True],[True,True,True,True,True,False,False,False,False,False,False,True,True,False],[True,False,False,False,False,True,True,False,False,False,False,True,True,False],[True,True,True,False,False,False,True,True,True,False,True,True,False,True],[False,True,False,True,False,False,False,False,False,True,False,False,True,False],[True,False,False,False,True,True,False,True,False,True,False,True,True,False],[False,False,True,False,True,True,False,True,False,False,True,False,True,True],[False,False,False,True,False,False,True,True,False,True,False,False,False,False],[True,False,False,True,False,False,True,True,True,True,True,True,True,False],[True,False,False,True,False,False,False,False,False,True,True,False,False,True]],[[False,True,False,True,True,False,False,True,False,False,False,False,True,True],[True,True,False,True,True,False,False,False,False,True,False,False,False,False],[True,True,True,True,False,True,True,True,False,True,False,False,True,False],[False,True,False,False,False,False,True,True,False,True,True,False,False,False],[False,True,False,True,False,True,True,False,True,False,True,True,True,True],[True,True,True,False,False,True,False,False,True,True,True,True,False,True],[True,True,True,False,False,True,True,False,False,False,False,True,False,True],[False,False,False,False,True,True,False,True,True,False,True,False,True,False],[False,True,True,True,False,False,True,False,True,True,False,False,True,False],[True,False,True,False,False,True,False,True,True,False,False,False,False,True],[False,True,True,False,False,True,False,True,True,True,True,True,False,False],[True,False,False,False,False,False,False,False,True,False,True,False,False,True],[False,False,False,True,True,True,True,False,False,True,True,False,True,False],[True,True,False,False,True,True,False,True,True,True,True,False,True,False],[True,False,True,True,False,True,False,False,True,False,False,True,True,True],[True,False,True,False,False,False,False,True,True,True,True,False,False,False]],[[False,True,True,True,True,False,True,False,False,True,False,True,True,False],[False,True,True,False,True,False,False,True,False,True,True,True,False,False],[True,False,False,False,True,True,True,True,False,False,True,False,False,True],[True,True,True,True,False,False,True,False,False,False,True,True,True,False],[False,True,False,False,True,True,False,False,False,True,True,False,False,False],[False,False,True,True,True,False,True,False,False,False,False,True,False,True],[False,True,False,False,False,False,False,True,True,False,False,False,False,True],[False,False,False,True,False,True,False,True,False,True,True,False,False,True],[True,False,True,True,False,True,False,False,True,False,False,True,True,False],[True,True,True,True,True,True,False,True,True,True,False,True,False,False],[True,False,True,True,True,False,False,True,True,False,True,True,True,True],[False,False,True,True,True,True,False,False,False,True,True,True,False,True],[False,False,True,False,True,True,True,False,True,True,True,True,False,False],[False,True,False,False,True,True,True,False,False,True,False,True,False,True],[False,False,False,True,True,False,True,False,True,False,False,False,True,True],[True,True,True,True,False,True,True,True,True,False,True,True,False,True]],[[False,False,False,True,True,True,False,False,True,True,False,False,True,False],[False,False,True,False,False,False,True,False,False,True,False,True,True,True],[False,True,True,True,False,True,False,True,False,False,True,True,True,True],[True,False,True,False,False,False,False,False,False,True,True,False,False,True],[True,False,False,False,True,True,True,True,True,True,False,True,True,True],[True,False,False,False,False,True,False,False,True,False,True,False,False,False],[False,False,True,False,False,True,False,False,True,True,True,False,False,False],[True,True,True,False,True,False,True,True,True,True,True,True,False,False],[True,False,False,True,False,True,True,True,True,True,True,False,False,False],[False,False,False,True,True,False,False,False,False,True,True,True,False,True],[False,False,True,True,False,False,True,True,True,False,False,False,False,True],[False,False,True,False,True,False,False,False,False,False,True,False,True,False],[True,True,True,False,False,True,True,False,True,False,True,False,True,True],[True,True,False,True,True,False,False,False,False,False,True,False,False,False],[False,True,False,True,False,False,True,False,True,True,True,False,True,False],[False,False,False,True,True,False,True,True,False,True,True,False,True,False]],[[False,True,False,False,False,True,False,False,True,True,True,False,False,False],[False,False,False,False,False,False,False,False,True,True,True,True,False,False],[False,True,True,False,False,True,True,False,False,True,False,True,False,True],[True,True,True,True,True,False,False,True,False,False,True,True,True,False],[True,True,True,True,False,False,True,False,True,False,False,False,True,False],[True,False,False,True,True,True,False,False,True,False,True,False,False,True],[True,True,True,False,False,False,True,False,False,True,False,False,True,False],[False,True,True,True,True,True,False,False,False,True,False,False,True,True],[False,False,False,True,True,False,False,False,False,True,False,True,False,True],[True,False,True,True,True,False,False,False,True,True,False,False,False,False],[False,True,True,False,True,False,True,True,False,True,True,False,True,True],[True,True,False,False,True,False,True,False,False,False,False,False,True,False],[False,True,False,False,False,False,False,False,False,True,True,False,True,False],[False,False,True,False,True,False,False,True,False,False,True,False,False,False],[False,True,False,False,False,True,False,False,True,False,False,True,False,True],[True,True,True,True,True,True,True,False,True,False,True,True,False,True]],[[True,False,True,False,True,True,False,True,False,True,True,True,True,False],[False,True,True,True,False,True,True,True,False,False,False,True,False,True],[False,False,False,True,False,True,True,True,True,False,False,True,True,False],[True,False,False,True,False,True,True,False,False,False,False,False,False,False],[True,True,True,True,True,False,True,False,True,False,True,False,False,False],[False,True,False,True,False,False,False,False,True,True,False,False,True,False],[False,False,False,False,True,False,True,False,False,False,False,True,True,False],[False,True,False,False,True,False,True,True,False,True,True,True,True,True],[True,False,False,False,False,False,False,True,False,True,False,False,False,False],[False,True,False,False,False,False,False,True,False,True,False,False,False,True],[False,True,True,True,False,True,True,False,True,True,False,False,True,False],[False,True,False,False,False,True,False,False,True,False,False,False,True,False],[False,False,False,False,True,True,False,True,False,True,False,True,True,False],[True,False,False,False,True,False,False,True,True,True,True,True,True,True],[True,True,False,True,True,False,False,False,True,False,False,True,True,False],[False,False,False,False,False,False,False,True,False,False,False,False,True,False]],[[True,True,True,False,False,True,True,True,True,True,True,False,True,True],[True,True,True,False,True,True,False,False,True,False,True,False,False,False],[False,False,False,True,True,True,True,True,True,False,False,False,False,True],[True,True,True,False,False,False,False,False,False,False,False,True,False,True],[True,True,True,True,True,True,False,False,True,True,True,False,False,True],[False,False,False,True,True,True,False,False,False,False,False,False,True,False],[True,True,True,True,False,True,False,True,False,True,True,True,False,False],[True,False,True,False,False,False,True,False,True,True,False,True,False,False],[True,True,False,True,False,True,False,True,False,False,False,True,True,False],[False,False,False,False,False,False,False,True,False,True,True,True,True,True],[True,True,True,False,False,True,True,False,False,True,True,True,False,False],[False,True,False,False,True,False,False,False,False,False,True,False,False,False],[False,True,True,True,False,False,True,False,True,True,False,True,False,False],[False,False,False,False,False,False,True,True,False,True,True,True,False,False],[True,False,False,True,True,True,False,True,True,False,True,False,True,True],[False,True,True,False,False,True,True,False,True,False,True,False,True,True]],[[True,True,True,False,True,False,False,False,True,False,True,True,False,False],[True,True,False,True,True,True,False,True,True,True,True,False,True,False],[False,False,True,True,False,True,False,True,True,False,False,False,False,True],[True,True,False,True,False,False,False,True,True,False,False,False,True,True],[True,False,False,True,True,True,True,True,False,True,False,True,True,False],[False,True,False,True,False,False,False,True,False,True,False,True,True,True],[False,True,False,True,True,False,False,False,False,True,True,False,False,False],[False,True,False,False,True,False,True,True,False,False,False,False,True,True],[False,False,False,False,True,False,True,True,True,True,True,True,True,True],[True,True,True,True,True,True,True,False,False,True,True,False,True,False],[True,False,True,True,False,True,True,False,True,False,True,False,True,False],[True,False,True,True,False,False,False,True,False,False,True,False,True,False],[False,False,False,True,False,True,False,False,False,True,False,False,True,True],[False,True,False,False,True,True,True,True,False,True,False,False,True,True],[False,False,False,False,False,False,False,False,False,False,True,False,False,True],[False,True,True,True,False,True,True,False,False,False,True,False,True,False]],[[False,True,True,False,True,True,True,False,False,True,False,False,True,True],[False,True,True,True,True,False,False,True,True,True,True,True,True,True],[False,False,True,False,True,False,True,True,False,False,True,False,True,True],[False,False,True,False,False,False,True,True,False,True,False,True,False,False],[False,True,True,False,False,False,True,True,False,False,False,False,False,True],[False,True,True,False,True,False,True,True,False,False,False,False,False,True],[True,False,True,True,False,False,False,False,False,True,True,False,True,False],[True,True,True,True,False,False,False,True,False,True,True,False,True,True],[False,True,False,True,False,True,True,False,True,True,False,True,False,True],[False,True,True,True,False,True,False,False,True,False,True,False,True,False],[False,True,False,True,False,False,False,False,False,True,False,True,False,False],[True,False,False,True,True,True,False,True,False,False,True,False,True,True],[False,False,True,False,True,True,True,False,False,False,False,False,True,True],[True,False,True,False,False,True,True,False,True,True,True,True,False,True],[True,True,False,True,True,True,False,True,True,True,True,True,True,True],[True,True,False,False,True,False,True,True,True,False,True,False,False,True]]], dtype = "bool")#candidate|70|(13, 16, 14)|const|bool
bop_71 = relay.logical_and(var_69.astype('bool'), relay.reshape(const_70.astype('bool'), relay.shape_of(var_69))) # shape=(13, 16, 14)
output = bop_71
output2 = bop_71
func_76 = relay.Function([var_69,], output)
mod['func_76'] = func_76
mod = relay.transform.InferType()(mod)
mutated_mod['func_76'] = func_76
mutated_mod = relay.transform.InferType()(mutated_mod)
var_77 = relay.var("var_77", dtype = "bool", shape = (13, 16, 14))#candidate|77|(13, 16, 14)|var|bool
func_76_call = mutated_mod.get_global_var('func_76')
call_78 = func_76_call(var_77)
output = call_78
func_79 = relay.Function([var_77], output)
mutated_mod['func_79'] = func_79
mutated_mod = relay.transform.InferType()(mutated_mod)
const_298 = relay.const([[[-1,-10,-6,-5,-4,-6,8,7,-3,-5,-5],[-5,-4,8,-4,-10,6,5,1,-2,2,2],[-6,-2,-9,-5,-9,-3,-7,-7,-2,9,6],[-1,6,4,3,-8,6,9,-6,-8,-9,9],[4,9,2,-7,2,7,-1,-5,-10,-5,-2],[2,1,2,4,5,7,5,4,10,-8,-5],[10,5,-5,-6,5,5,-9,5,10,1,-6],[9,-8,7,5,-7,1,5,-2,-3,1,10],[-6,-5,-7,-6,-5,-6,-5,1,4,-7,9],[3,6,-6,-5,-9,5,9,-2,-6,1,10],[-4,8,-8,-3,8,10,-1,1,7,8,5],[4,2,4,2,1,-4,4,-5,-1,-2,-7],[9,10,9,6,3,9,9,-1,7,9,-1],[3,9,-9,7,5,-5,10,2,5,-5,3],[8,-7,3,8,8,-2,-7,1,6,-10,10],[2,-5,9,3,-5,5,-8,9,-4,7,-5]],[[6,8,1,-2,7,5,3,3,-8,-9,-2],[1,10,8,3,2,9,-3,6,-1,1,7],[10,2,-10,-10,7,-4,9,4,7,-3,-6],[7,4,-6,-4,1,-3,-1,-5,5,-4,-8],[-5,7,8,8,-8,7,1,-7,6,-8,-2],[-2,-1,8,8,-10,-10,-4,-9,-4,7,7],[7,-2,1,-2,2,1,-10,1,-6,-2,-8],[-5,-1,1,2,-6,1,2,10,8,-5,-5],[1,5,-7,-4,-5,1,9,4,2,-10,9],[-9,-3,1,8,-5,4,-6,8,5,10,1],[-9,-1,-6,4,-3,6,-9,-6,-7,-6,10],[9,10,3,-1,9,9,9,-3,3,-7,3],[-10,-5,-9,-5,10,9,9,2,-4,9,5],[1,2,-3,4,9,7,10,-4,5,8,-6],[5,8,2,-7,3,4,-3,-8,-5,3,-8],[7,6,8,7,-3,-3,-4,-6,4,8,-9]],[[-7,9,4,3,5,-4,4,-6,-5,5,-2],[6,1,-1,8,-1,-7,-6,-4,-2,2,1],[9,7,8,3,3,2,-9,-5,3,1,-8],[-2,9,1,-4,-5,10,9,8,-10,1,-6],[-4,-7,-9,-10,7,-1,-10,8,-5,-6,-7],[-4,7,5,-7,8,4,-2,-6,-1,-8,1],[-7,1,2,-10,2,-3,10,-7,-2,2,-2],[10,9,-5,6,-5,3,-6,3,5,9,-4],[-7,-10,8,5,-6,-10,-8,4,-10,-8,4],[7,1,-5,-1,1,-10,9,3,-9,-8,-6],[5,10,-10,8,4,5,9,-6,-7,-8,-8],[-6,-10,-9,-4,-7,-8,4,-7,4,-8,-5],[-7,7,7,-4,10,-3,-4,1,9,7,-4],[7,-3,-3,10,-10,-8,-4,2,-10,-7,-3],[7,-7,1,-6,-6,8,-4,2,8,2,9],[-3,-3,3,7,-8,-1,3,-10,-9,-9,-8]],[[6,8,4,-4,-3,5,-1,5,6,2,-10],[-9,3,-9,-5,-7,8,6,3,-6,6,-4],[10,7,-5,-3,-6,-5,2,-1,-2,-7,4],[-4,-3,5,2,8,-1,7,-4,8,3,-8],[9,10,-8,4,10,8,8,5,-3,1,-8],[7,-9,1,-10,6,8,3,-5,-9,6,-10],[-1,6,8,7,8,-7,10,-8,10,-4,-10],[-6,5,-9,3,5,4,5,1,-9,7,-5],[-5,1,-4,4,1,8,5,5,9,-1,3],[7,7,2,-2,-3,9,4,9,9,10,-4],[-7,3,8,8,-10,-5,3,-5,4,3,1],[7,3,-10,1,8,-2,3,6,1,-8,-5],[4,5,-7,9,4,-10,10,-2,3,-1,2],[4,7,4,-2,6,10,-3,-10,8,8,2],[7,1,3,-4,-7,-3,-4,2,9,-1,9],[-7,-6,-4,-5,4,-10,4,8,10,-6,2]],[[1,5,1,-8,-2,3,10,-4,-6,8,3],[9,10,1,-2,6,-8,-3,1,-3,-6,2],[-4,2,-3,5,-10,9,6,6,4,3,-4],[-1,8,7,10,2,6,-3,-4,-6,7,-6],[7,2,5,3,10,4,10,1,-3,-6,-9],[-9,-9,9,10,8,-7,-1,4,2,10,3],[1,1,-1,4,-6,-2,8,1,-7,7,9],[-8,4,10,-8,-3,9,5,-1,-9,-4,3],[2,-9,-5,7,-6,9,-5,-1,4,-3,10],[-4,-9,-9,3,2,-6,-8,-9,4,-8,-3],[-6,7,2,4,8,-4,-2,-7,-5,-4,-1],[-1,-7,-6,-10,9,3,5,-6,9,8,2],[-6,-6,-9,3,1,10,9,-3,3,4,-10],[3,-9,-1,-6,8,3,7,2,-1,4,-3],[7,3,-9,-10,-9,6,-7,-4,1,9,5],[5,-5,-2,-10,-3,10,7,-6,-8,-1,-2]],[[1,-1,9,-8,5,-2,10,1,-9,-4,-4],[-8,-9,-5,1,9,7,-6,-2,-1,-8,9],[-6,-7,-7,-4,6,-9,-8,-5,4,-3,-6],[7,5,-6,2,-2,-8,-5,-4,3,-1,-4],[9,-8,-7,-5,-3,-2,-10,-3,6,3,8],[8,-7,1,5,6,9,8,6,9,-6,10],[-1,-10,-2,-2,9,2,3,1,-9,2,1],[-3,5,-8,5,9,-5,-7,-10,-9,3,4],[-5,3,-3,3,7,3,-10,-5,3,4,-10],[6,2,-8,7,10,-8,5,8,-5,3,-8],[-3,9,4,-5,-4,4,-6,-2,6,-2,-3],[-6,-2,7,-1,8,8,9,1,-8,-6,-3],[-7,-5,5,5,-4,-10,-2,-4,3,-8,-1],[5,-2,9,7,10,6,-5,3,-10,3,-7],[-6,9,-5,2,-5,-10,-2,-4,-10,3,10],[-7,-9,1,-7,-8,-9,4,-5,2,3,-6]],[[-2,2,-5,-7,2,-7,1,5,-4,10,-10],[-9,-1,3,-4,7,-1,7,-3,-10,-10,-7],[5,-8,-5,-4,5,7,4,-7,3,6,4],[-10,10,5,-7,1,-6,-2,-9,3,-2,7],[-4,-6,-2,-9,-8,5,-8,-7,3,-8,-9],[10,-9,-10,-5,8,-5,6,-7,-2,-3,2],[-7,6,-7,1,-5,3,-3,-6,2,-8,8],[-2,9,1,-3,1,2,-4,-2,-6,-5,2],[4,8,1,2,-10,-4,10,-10,8,5,-1],[-10,3,1,-5,-7,10,-4,9,-2,-10,-7],[2,3,1,2,6,-4,-6,-8,7,-1,-9],[9,10,-9,10,1,5,3,-4,7,-5,-1],[-5,5,4,-10,8,5,3,-8,-3,-4,-5],[-4,2,-10,-2,9,10,9,7,-1,9,4],[-1,4,3,10,-4,6,-8,4,-5,-7,-6],[-3,6,-9,9,6,8,-1,7,-9,-10,9]],[[-9,-9,-6,3,5,-5,1,5,-1,-1,-10],[-2,-8,9,5,-7,1,-3,6,-8,-4,-3],[1,7,10,3,-2,8,5,7,7,4,-2],[4,-5,-1,7,3,2,2,-10,10,7,2],[-7,-1,3,-2,-4,-4,-9,7,-7,-6,2],[8,10,-4,8,-10,-4,-9,8,-3,8,-1],[-10,-2,1,-7,5,-7,-5,-3,-6,10,-6],[7,10,6,7,4,-8,-6,6,3,1,6],[10,1,-2,6,-9,2,4,9,7,-1,-2],[5,-2,-9,6,-9,3,-2,8,-3,-2,-10],[4,8,-5,-8,7,4,10,2,-9,2,-8],[8,-4,-7,-9,3,-6,-5,-1,7,4,7],[7,10,8,-9,-8,-4,-2,-9,8,4,-6],[-7,2,4,9,10,3,-3,5,9,1,-6],[-6,5,6,10,-8,8,2,6,7,7,-9],[3,2,-5,-7,9,-5,-9,-4,4,7,2]]], dtype = "uint32")#candidate|298|(8, 16, 11)|const|uint32
var_299 = relay.var("var_299", dtype = "uint32", shape = (8, 16, 11))#candidate|299|(8, 16, 11)|var|uint32
bop_300 = relay.bitwise_xor(const_298.astype('uint32'), relay.reshape(var_299.astype('uint32'), relay.shape_of(const_298))) # shape=(8, 16, 11)
func_76_call = mod.get_global_var('func_76')
func_79_call = mutated_mod.get_global_var('func_79')
var_316 = relay.var("var_316", dtype = "bool", shape = (2912,))#candidate|316|(2912,)|var|bool
call_315 = func_76_call(relay.reshape(var_316.astype('bool'), [13, 16, 14]))
call_317 = func_76_call(relay.reshape(var_316.astype('bool'), [13, 16, 14]))
func_76_call = mod.get_global_var('func_76')
func_79_call = mutated_mod.get_global_var('func_79')
call_319 = func_76_call(relay.reshape(var_316.astype('bool'), [13, 16, 14]))
call_320 = func_76_call(relay.reshape(var_316.astype('bool'), [13, 16, 14]))
output = relay.Tuple([bop_300,call_315,var_316,call_319,])
output2 = relay.Tuple([bop_300,call_317,var_316,call_320,])
func_336 = relay.Function([var_299,var_316,], output)
mod['func_336'] = func_336
mod = relay.transform.InferType()(mod)
mutated_mod['func_336'] = func_336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_336_call = mutated_mod.get_global_var('func_336')
var_338 = relay.var("var_338", dtype = "uint32", shape = (8, 16, 11))#candidate|338|(8, 16, 11)|var|uint32
var_339 = relay.var("var_339", dtype = "bool", shape = (2912,))#candidate|339|(2912,)|var|bool
call_337 = func_336_call(var_338,var_339,)
output = call_337
func_340 = relay.Function([var_338,var_339,], output)
mutated_mod['func_340'] = func_340
mutated_mod = relay.transform.InferType()(mutated_mod)
const_453 = relay.const(6.184248, dtype = "float32")#candidate|453|()|const|float32
var_454 = relay.var("var_454", dtype = "float32", shape = (1, 3, 16))#candidate|454|(1, 3, 16)|var|float32
bop_455 = relay.floor_divide(const_453.astype('float32'), var_454.astype('float32')) # shape=(1, 3, 16)
func_76_call = mod.get_global_var('func_76')
func_79_call = mutated_mod.get_global_var('func_79')
var_461 = relay.var("var_461", dtype = "bool", shape = (104, 28))#candidate|461|(104, 28)|var|bool
call_460 = func_76_call(relay.reshape(var_461.astype('bool'), [13, 16, 14]))
call_462 = func_76_call(relay.reshape(var_461.astype('bool'), [13, 16, 14]))
output = relay.Tuple([bop_455,call_460,var_461,])
output2 = relay.Tuple([bop_455,call_462,var_461,])
func_471 = relay.Function([var_454,var_461,], output)
mod['func_471'] = func_471
mod = relay.transform.InferType()(mod)
mutated_mod['func_471'] = func_471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_471_call = mutated_mod.get_global_var('func_471')
var_473 = relay.var("var_473", dtype = "float32", shape = (1, 3, 16))#candidate|473|(1, 3, 16)|var|float32
var_474 = relay.var("var_474", dtype = "bool", shape = (104, 28))#candidate|474|(104, 28)|var|bool
call_472 = func_471_call(var_473,var_474,)
output = call_472
func_475 = relay.Function([var_473,var_474,], output)
mutated_mod['func_475'] = func_475
mutated_mod = relay.transform.InferType()(mutated_mod)
var_539 = relay.var("var_539", dtype = "uint32", shape = (10, 15, 12))#candidate|539|(10, 15, 12)|var|uint32
var_540 = relay.var("var_540", dtype = "uint32", shape = (10, 15, 12))#candidate|540|(10, 15, 12)|var|uint32
bop_541 = relay.bitwise_or(var_539.astype('uint32'), relay.reshape(var_540.astype('uint32'), relay.shape_of(var_539))) # shape=(10, 15, 12)
output = relay.Tuple([bop_541,])
output2 = relay.Tuple([bop_541,])
func_551 = relay.Function([var_539,var_540,], output)
mod['func_551'] = func_551
mod = relay.transform.InferType()(mod)
var_552 = relay.var("var_552", dtype = "uint32", shape = (10, 15, 12))#candidate|552|(10, 15, 12)|var|uint32
var_553 = relay.var("var_553", dtype = "uint32", shape = (10, 15, 12))#candidate|553|(10, 15, 12)|var|uint32
output = func_551(var_552,var_553,)
func_554 = relay.Function([var_552,var_553,], output)
mutated_mod['func_554'] = func_554
mutated_mod = relay.transform.InferType()(mutated_mod)
const_568 = relay.const([[[2,-4,-9,-8,-7,-6,-9,10],[-3,1,-9,-2,8,-7,7,-8],[5,-10,6,-3,-2,3,-8,-5],[3,-10,-10,-3,-6,5,-6,-4],[4,7,-1,2,1,-7,2,10],[6,8,-4,-6,-3,-6,3,-10],[-4,-6,-9,-8,-6,1,-7,-3],[-3,-2,-2,-7,-9,-4,3,-9],[4,1,4,6,-6,-9,-8,-7],[3,-7,-8,-10,7,9,-9,-8],[6,8,1,-1,1,-2,-4,9]],[[8,2,10,3,7,9,4,1],[-7,9,3,4,4,2,-5,-3],[4,-9,9,-4,-7,4,-10,-9],[-4,-4,-2,10,4,-4,-2,10],[-4,2,2,-2,7,-10,3,-4],[10,5,-4,-8,6,7,-8,-5],[7,-8,3,8,5,9,-7,-4],[-8,-1,-3,-3,2,8,9,4],[3,5,-1,-8,-2,4,-9,-10],[-7,-1,1,-1,6,-7,-5,10],[-3,5,-9,10,-7,5,-3,3]],[[6,-8,2,4,-9,4,1,3],[1,8,9,3,4,-4,-1,-5],[-2,5,-4,-3,-9,-8,-1,2],[9,1,-2,5,-2,-1,7,1],[-2,-5,-7,-1,5,5,-2,-5],[-9,-10,3,-6,-6,10,-4,-3],[1,-3,6,5,3,7,-8,-6],[-1,9,2,10,2,-9,3,5],[10,2,-3,-9,-6,-4,9,1],[-8,5,-6,8,-5,6,-1,-1],[2,8,8,-6,2,-9,1,2]],[[-2,9,-9,6,4,-1,-5,-5],[-6,2,10,10,-7,-4,3,-8],[-2,3,-4,7,-10,-2,-3,-2],[1,2,-4,-5,3,1,-7,1],[8,5,10,9,-2,-5,-7,3],[2,9,-10,-7,6,-9,9,-6],[-3,-8,-3,-2,-7,2,-5,1],[-2,1,7,-5,8,-9,5,3],[-6,-10,7,6,3,5,4,-5],[-8,-10,-6,9,-10,-10,-2,2],[1,9,-8,-1,4,8,4,6]]], dtype = "uint8")#candidate|568|(4, 11, 8)|const|uint8
var_569 = relay.var("var_569", dtype = "uint8", shape = (4, 11, 8))#candidate|569|(4, 11, 8)|var|uint8
bop_570 = relay.minimum(const_568.astype('uint8'), relay.reshape(var_569.astype('uint8'), relay.shape_of(const_568))) # shape=(4, 11, 8)
bop_576 = relay.left_shift(var_569.astype('int16'), relay.reshape(bop_570.astype('int16'), relay.shape_of(var_569))) # shape=(4, 11, 8)
func_551_call = mod.get_global_var('func_551')
func_554_call = mutated_mod.get_global_var('func_554')
var_581 = relay.var("var_581", dtype = "uint32", shape = (1800,))#candidate|581|(1800,)|var|uint32
call_580 = relay.TupleGetItem(func_551_call(relay.reshape(var_581.astype('uint32'), [10, 15, 12]), relay.reshape(var_581.astype('uint32'), [10, 15, 12]), ), 0)
call_582 = relay.TupleGetItem(func_554_call(relay.reshape(var_581.astype('uint32'), [10, 15, 12]), relay.reshape(var_581.astype('uint32'), [10, 15, 12]), ), 0)
func_336_call = mod.get_global_var('func_336')
func_340_call = mutated_mod.get_global_var('func_340')
const_584 = relay.const([4,-9,-7,2,-10,1,-1,-2,5,-4,-5,-9,-4,7,-2,-9,6,-1,-6,-10,1,8,10,9,-1,4,-5,-2,-2,2,-7,-2,-9,-5,3,1,-9,-8,-8,-6,-9,-6,7,-3,7,3,-8,-7,8,-2,-9,7,-2,7,-9,3,-7,-4,9,3,5,-9,3,-10,8,-1,2,3,10,-8,-4,1,-9,8,-4,-3,-9,4,8,2,-3,-3,1,-3,-7,-2,-1,4,9,8,-3,4,3,3,-1,7,7,3,5,9,-6,-3,-5,6,7,9,5,1,1,-9,-10,-8,-4,5,6,1,8,-8,-9,6,8,-5,9,1,1,-4,-6,-7,3,2,-7,-3,5,7,6,1,9,7,3,9,1,4,-6,-10,3,2,4,-3,7,-6,-3,6,-2,-1,-4,6,6,3,-1,4,-6,1,10,-3,-6,-1,-4,3,2,1,-8,1,7,7,8,1,6,6,-10,4,-5,-4,-3,-7,3,-3,4,-5,10,10,-3,-2,5,-6,6,-10,4,2,-1,4,-6,4,-1,-3,-9,8,4,-1,-9,-3,-7,-8,6,-10,-10,10,-1,7,3,2,-3,-6,-2,7,5,6,4,5,-5,-7,-1,-2,3,-4,-7,10,9,-8,-4,4,-4,3,6,8,-5,6,-3,-6,-6,-5,-7,5,-3,-8,-8,6,3,-10,7,10,-4,-8,7,-7,6,-7,9,2,-5,-8,-3,2,6,-6,-1,-7,-7,6,-2,-6,-5,3,3,5,-6,-10,1,-6,6,-2,-2,-6,5,-10,2,-3,-9,10,-2,1,-10,-8,2,10,7,9,-8,-8,-4,9,-6,-5,-1,-8,-10,2,7,2,3,1,1,-9,4,3,-8,6,-7,1,-5,-10,6,-6,-9,6,2,1,-7,4,10,1,-2,-3,7,-6,3,-7,5,3,4,7,7,9,8,7,-3,-7,-5,-5,-4,-5,4,-5,-5,-6,-8,-5,10,-10,7,8,6,-6,-6,5,9,-7,4,-3,-2,10,-9,6,-6,2,4,3,5,-2,8,3,9,-8,1,4,10,3,8,1,-6,7,-4,1,-8,2,-2,3,2,8,5,-7,7,-6,-1,-1,9,6,-8,3,-2,4,-8,7,10,-5,9,-2,6,-1,5,2,10,7,7,-8,7,-2,10,-6,5,7,-7,-10,7,8,3,-5,-7,5,-4,-2,-4,7,4,-6,7,4,-2,-5,-6,-10,2,-4,-10,5,-1,-7,1,-8,-9,5,8,10,-4,1,-9,-10,8,3,4,-4,-7,9,8,5,10,3,-1,-7,1,6,-1,-10,4,-9,-3,3,-7,-6,-10,2,10,9,10,6,-6,-1,1,-5,7,5,-6,-8,3,-8,6,4,-5,9,10,9,10,-2,1,7,-3,8,1,4,3,-6,2,-4,4,4,-9,-10,1,9,1,-4,6,-6,9,10,2,8,7,-8,-7,3,-5,4,-4,10,1,-10,5,6,5,-5,-4,-8,-6,10,-1,1,7,-2,10,-6,5,10,3,-3,1,-5,10,6,2,-1,-10,-8,10,7,1,1,-1,-5,6,-3,5,-2,1,-5,5,-5,10,1,3,-2,-1,-2,5,-7,7,-7,-5,-1,8,-9,-4,9,8,-6,8,-9,10,-1,1,5,5,-4,5,-7,3,-8,-10,3,-7,-9,8,3,-1,2,-2,2,2,-8,-3,-10,2,-5,4,-10,-8,5,-9,3,-3,-2,3,2,1,-2,8,-3,9,3,-6,6,6,-10,-10,-4,10,-7,1,-8,-1,9,2,8,-9,-7,-7,-1,-4,7,3,-8,9,-6,7,5,6,-5,-7,2,-7,-1,3,7,-4,-3,8,-2,9,9,3,3,-1,8,3,-2,-8,-5,8,8,6,8,5,1,7,-1,6,-8,2,5,-5,-6,-1,-5,10,-10,7,10,-6,-9,1,-3,-3,3,8,-1,-4,-9,-7,-5,-10,-3,3,-10,-2,-1,-10,-1,-7,8,-4,-10,7,5,-4,1,5,10,7,6,10,4,4,-2,-2,8,-3,-4,8,4,-2,-3,-9,5,-2,7,10,1,-9,-9,-5,-6,-5,-9,-2,2,-8,-8,-7,-6,6,2,-7,4,-8,-8,7,-1,4,5,5,-7,2,3,-2,8,-10,-6,3,-4,2,-4,-4,1,-7,6,-4,6,-2,-5,5,10,4,-6,-5,-10,10,6,-8,-4,5,-8,4,-7,2,9,-7,-7,-7,10,1,1,-3,-5,-5,-8,10,-1,10,1,10,-1,2,-8,9,3,7,1,-10,-2,5,7,-6,2,-4,9,-4,1,-8,-5,6,-7,1,-4,4,7,-8,7,-1,-1,3,-1,8,-2,-10,3,6,-2,8,9,-3,-3,1,4,-2,-8,-3,-1,2,9,-10,-9,-2,5,-8,6,-1,10,-1,-5,-7,8,-6,3,2,-10,-4,-1,10,10,10,-7,5,4,-4,-10,6,3,7,-7,-7,1,6,10,8,3,-6,-9,-2,8,6,6,-8,-3,6,5,-9,-7,-10,2,-6,6,-9,-4,9,-6,-4,6,-3,8,-1,5,1,6,8,1,-4,8,3,-4,-6,7,5,1,-4,-7,3,-6,3,-8,-9,5,-6,-9,-4,1,-3,9,4,6,-8,5,-7,8,3,1,4,7,10,9,1,4,-10,2,3,-4,-2,-4,9,1,5,4,-9,-1,1,2,2,5,-7,6,6,-10,-8,-9,6,7,-5,3,5,2,-4,7,-10,-7,-9,8,-4,6,-5,-7,9,2,-8,-8,9,-9,6,-10,-8,7,10,7,-6,-6,-9,1,10,10,10,-10,-9,3,-7,-4,-10,6,-8,5,-3,-4,5,-10,3,-2,-9,-2,-3,4,8,9,-10,-7,6,-2,-5,3,4,-5,-3,-9,-9,-1,-8,4,-6,3,8,4,-5,4,3,-10,-1,5,9,-8,-7,-3,-7,-2,-2,7,-8,-3,-7,1,-4,-8,-3,1,-9,2,-10,-2,4,10,-10,3,7,-8,-2,-4,-1,1,5,8,3,-9,-7,-9,-6,6,-5,-3,6,9,-4,4,5,-1,-7,4,1,4,6,-2,4,10,8,4,-9,-1,5,-8,1,3,-8,-10,2,-10,9,3,-9,-3,-8,-2,9,10,1,6,-7,3,-6,6,-7,8,-8,7,6,8,-6,-1,-4,-9,-8,8,-6,1,-4,-1,7,8,2,5,-7,4,-3,-8,-7,-3,-4,10,-4,1,2,-2,3,4,-5,-5,-2,-6,3,4,-3,-5,-10,8,-8,3,-2,8,-4,1,1,-2,5,10,5,10,-10,6,9,-5,10,-6,-4,-8,-7,8,6,-3,-1,1,-6,2,3,6,-2,1,-1,-6,1,3,-4,-8,-10,-3,1,-5,-4,-2,8,1,1,2,8,6,2,7,-8,-8,3,1,5,2,-6,-6,-4,-4,6,-4,-4,4,-10,3,6,-10,3,7,-9,7,5,10,10,-4,-10,1,-9,-1,7,-8,-9,4,-10,-2,-1,-6,2,-6,2,9,8,-7,6,-7,3,-8,4,6,4,-4,-7,-3,-6,9,1,-9,9,-8,-3,-10,2,3,-9,-1,5,7,-4,10,1,10,-9,-1,-5,5,-5,6,-10,-5,-8,-3,-2,6,1,7,-5,-4,-4,-5,3,8,-3,-5,-5,-4,-7,-5,-7,4,-9,2,8,10,-10,-2,3,10,4,10,6,-2,3,1,-10,-10,5,-3,-9,-6,8,-1,-6,8,8,1,4,-10,-1,-6], dtype = "uint32")#candidate|584|(1408,)|const|uint32
const_585 = relay.const([True,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,False,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,True,False,False,False,True,True,True,True,True,True,False,True,True,False,False,True,True,False,True,False,True,True,False,True,True,False,True,True,True,True,True,True,True,False,True,False,True,False,True,False,True,False,False,True,False,False,False,True,True,True,True,False,False,False,True,True,False,False,True,False,False,False,True,True,False,False,False,True,True,True,False,False,True,False,True,False,False,True,True,True,False,True,True,False,True,False,False,True,True,True,True,True,True,False,False,False,True,False,True,False,False,True,False,True,True,False,True,False,True,True,True,False,False,True,False,True,True,False,False,False,True,False,True,True,False,False,True,True,False,False,True,False,False,False,False,True,False,True,True,True,False,True,True,False,False,False,True,True,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False,False,True,False,False,True,False,True,True,False,False,False,True,False,False,False,False,True,False,False,True,False,True,False,True,True,False,True,True,False,False,True,True,False,False,True,True,False,False,False,False,True,True,True,True,True,False,True,False,False,True,True,True,True,True,False,False,True,True,True,False,True,False,True,True,False,False,True,False,False,True,True,True,False,False,True,False,False,False,False,True,False,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,False,True,True,False,False,False,False,True,True,True,True,True,True,True,False,True,True,False,False,True,False,True,False,True,True,True,False,False,True,False,True,True,True,False,True,True,True,True,False,False,False,True,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,True,False,False,False,True,False,False,True,True,True,True,True,False,True,True,False,False,True,True,False,True,True,False,False,True,True,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,True,True,True,True,True,True,False,False,True,True,False,False,True,False,True,False,False,True,False,True,False,False,True,True,False,False,False,False,False,False,True,False,True,False,True,False,True,False,False,False,True,True,True,False,True,False,False,True,True,True,True,True,True,False,False,True,False,False,False,False,False,True,False,True,True,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,True,False,True,False,False,False,True,False,False,True,True,True,True,True,False,False,False,False,True,True,True,False,False,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,False,True,True,False,True,True,False,True,True,True,True,True,True,True,True,False,True,True,True,False,False,True,False,True,False,False,False,False,True,False,False,False,False,False,False,True,True,True,False,False,False,True,True,False,True,False,False,False,True,True,False,True,True,False,True,True,False,True,True,False,False,False,False,False,False,False,True,True,True,False,False,False,True,True,False,False,False,False,False,True,False,False,True,True,False,False,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,False,True,False,True,False,False,False,False,True,True,True,True,True,False,False,False,True,True,True,False,True,False,True,False,True,False,False,True,False,True,True,True,False,False,False,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,False,True,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,True,True,True,False,False,True,False,True,False,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,False,True,True,True,True,True,True,True,False,True,False,False,False,False,False,False,True,True,True,True,True,True,False,False,False,False,True,False,True,False,True,True,True,False,False,False,True,True,True,False,True,True,False,True,True,False,True,True,True,True,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False,False,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,True,False,True,True,True,False,True,True,False,False,False,False,True,False,False,True,False,True,False,False,False,True,False,False,False,True,True,False,False,False,True,True,True,False,True,False,False,False,False,False,True,False,True,False,False,True,False,False,True,False,False,True,True,False,True,False,True,False,False,True,False,True,False,True,False,True,False,False,False,False,True,True,False,False,True,False,True,True,False,False,False,False,True,True,False,False,True,True,False,False,False,True,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,False,False,False,True,False,False,False,True,False,True,True,True,True,True,True,False,False,False,True,False,False,True,False,False,False,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,True,False,False,False,True,True,True,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,True,False,True,False,False,True,False,True,False,True,True,False,False,True,False,False,True,True,True,True,True,False,False,False,False,False,True,False,False,False,False,True,False,True,True,False,False,True,False,False,True,True,False,True,False,False,True,False,True,True,True,True,True,True,True,True,True,False,True,True,False,True,False,False,False,True,True,False,True,True,True,False,False,True,True,False,False,False,False,True,True,True,False,False,False,True,False,True,True,True,False,True,True,False,False,True,False,True,False,True,False,True,True,False,False,False,False,False,False,True,False,False,False,False,False,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,False,False,True,True,False,False,True,False,False,False,True,False,False,False,True,False,True,True,True,True,False,True,False,True,False,False,False,False,True,False,True,False,False,False,True,False,False,True,True,True,True,False,True,True,False,False,True,True,True,False,True,False,True,True,True,True,True,False,False,True,False,True,True,True,True,False,True,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,False,True,True,False,False,True,False,False,False,False,True,True,True,True,True,True,True,True,True,False,True,False,False,True,False,True,False,True,False,True,True,False,False,False,False,True,True,False,True,True,True,True,False,False,False,False,True,True,True,True,True,False,True,True,True,True,True,True,False,True,True,True,True,True,False,False,False,True,False,False,True,True,True,True,False,True,True,True,False,False,False,True,True,False,False,False,True,True,False,False,False,True,True,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,True,True,False,False,False,False,False,True,True,False,True,True,False,False,True,False,False,False,False,True,True,True,False,True,True,False,True,True,True,False,False,False,True,False,False,False,False,True,True,False,True,False,True,True,False,False,False,False,True,False,False,False,True,False,False,False,True,True,True,False,True,False,True,False,False,True,False,True,False,True,True,True,True,False,True,True,True,True,False,False,True,False,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,True,False,True,True,True,False,False,False,True,False,True,False,False,True,False,False,True,True,False,False,False,False,True,True,False,False,False,True,True,False,True,False,False,False,True,False,True,False,False,False,False,True,True,False,False,True,False,True,False,False,True,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,False,True,True,False,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,True,False,True,True,False,False,True,True,True,True,False,False,True,True,True,True,True,True,True,True,False,True,True,True,False,False,False,True,False,False,False,True,False,True,False,False,True,True,False,True,True,False,True,False,False,False,False,True,True,True,True,True,True,False,False,True,False,False,False,False,False,False,True,False,False,True,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,False,True,False,False,False,True,True,False,False,False,True,False,True,False,False,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,False,False,False,False,True,False,False,True,False,False,True,True,False,False,False,False,True,True,False,False,False,True,True,False,False,False,True,True,False,True,False,False,True,True,True,False,True,True,False,True,False,True,False,False,False,True,False,True,False,False,False,False,False,True,True,False,False,False,False,False,False,False,True,True,True,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,True,False,False,True,False,False,True,True,False,False,False,False,True,False,False,False,True,False,True,True,True,False,True,True,False,True,False,False,False,True,True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False,False,False,True,True,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,True,True,True,False,True,False,True,False,False,False,False,False,True,True,False,False,True,True,True,False,True,True,True,True,True,True,False,True,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,False,False,False,True,False,True,False,True,False,True,False,False,True,True,False,True,True,False,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,False,True,True,False,True,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,True,True,False,False,True,False,True,True,True,False,False,False,True,True,False,False,True,False,False,True,True,False,True,False,False,True,False,True,False,True,True,False,False,False,False,True,False,True,True,True,True,True,True,True,False,False,True,True,False,True,False,False,False,True,False,False,True,False,True,True,True,False,True,False,False,False,True,False,True,False,False,True,True,True,False,False,True,True,True,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,True,True,True,True,True,True,True,True,False,True,True,False,True,False,True,False,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,True,False,True,False,True,False,False,True,False,True,False,False,False,False,False,False,True,False,True,True,False,True,False,False,True,False,True,False,False,False,False,False,False,True,False,True,False,False,False,False,True,False,True,True,True,True,False,False,True,True,True,True,False,True,False,True,False,True,True,False,True,True,False,True,True,True,False,True,True,True,True,True,True,False,False,False,True,False,False,True,True,False,False,True,True,False,True,True,True,False,False,False,False,False,True,True,True,False,False,True,True,True,False,False,False,False,True,True,True,True,False,False,True,True,False,True,True,True,False,True,True,False,True,True,True,True,False,False,True,False,True,False,False,True,False,False,False,True,True,True,True,False,True,False,True,True,True,False,False,False,True,False,False,True,True,True,False,False,False,True,False,True,True,False,True,True,False,True,True,False,False,False,False,True,False,True,True,False,True,True,False,True,True,False,False,True,False,False,True,False,True,True,True,False,False,False,True,False,True,False,False,True,False,False,True,True,True,False,True,True,True,True,False,True,True,False,False,True,False,True,True,True,False,True,True,False,True,False,True,True,True,True,False,True,False,True,False,True,True,True,False,True,False,False,False,False,False,False,True,False,True,True,True,True,False,False,False,True,True,True,False,False,False,True,True,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True,False,False,False,True,True,False,False,True,False,True,False,False,True,True,True,False,True,False,False,True,False,False,False,True,False,True,False,False,False,True,True,False,True,False,False,False,False,False,False,False,True,False,True,False,True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,False,False,False,False,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,True,True,True,True,False,False,False,True,True,True,True,False,True,True,False,False,True,True,False,True,False,True,True,True,False,True,False,False,True,True,False,False,False,True,False,False,True,False,False,False,True,True,False,True,False,False,True,True,True,True,False,True,False,True,True,True,True,True,True,False,False,True,True,False,False,True,True,True,True,True,True,False,False,True,True,False,True,False,False,True,False,False,False,False,False,True,True,True,False,False,True,False,True,False,True,True,True,False,False,False,True,True,True,True,False,False,True,False,True,True,True,True,False,True,True,False,True,True,True,True,True,False,False,True,True,True,False,False,True,True,True,False,False,False,True,True,False,False,True,True,False,False,False,False,True,False,False,False,True,True,False,False,True,False,True,False,True,False,True,False,True,False,False,True,False,True,False,False,True,True,False,True,True,False,True,True,False,True,True,True,False,True,False,False,True,True,False,False,True,True,False,False,True,False,False,True,True,False,False,True,False,False,False,True,False,False,False,True,True,False,False,False,True,False,False,True,False,False,True,True,False,False,False,True,False,False,True,False,False,True,True,False,True,True,False,True,True,False,False,True,False,True,True,False,True,True,True,True,True,False,True,True,False,True,True,True,True,False,True,True,True,False,False,False,True,False,True,True,False,False,False,True,True,True,True,False,False,False,False,True,False,True,True,True,False,False,False,True,False,True,False,True,True,False,True,False,False,False,True,True,False,True,False,True,False,True,False,False,True,False,False,True,True,True,False,True,True,False,False,True,True,False,False,False,True,True,True,True,True,False,False,False,False,False,True,False,True,True,True,False,True,True,False,False,False,False,True,True,True,True,False,False,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,True,True,False,True,True,True,True,True,True,False,True,False,True,False,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,False,True,True,False,True,False,True,False,False,False,False,True,False,True,True,False,True,False,False,True,True,True,False,True,True,True,False,True,False,True,True,True,False,False,True,True,True,True,False,True,True,False,False,False,False,True,False,True,True,True,False,True,False,False,False,True,True,True,False,False,False,True,True,False,False,False,False,True,True,False,False,True,False,False,True,False,True,True,True,True,False,False,False,True,False,False,False,False,True,True,False,True,False,True,False,False,True,False,True,True], dtype = "bool")#candidate|585|(2912,)|const|bool
call_583 = relay.TupleGetItem(func_336_call(relay.reshape(const_584.astype('uint32'), [8, 16, 11]), relay.reshape(const_585.astype('bool'), [2912,]), ), 2)
call_586 = relay.TupleGetItem(func_340_call(relay.reshape(const_584.astype('uint32'), [8, 16, 11]), relay.reshape(const_585.astype('bool'), [2912,]), ), 2)
func_336_call = mod.get_global_var('func_336')
func_340_call = mutated_mod.get_global_var('func_340')
call_591 = relay.TupleGetItem(func_336_call(relay.reshape(const_584.astype('uint32'), [8, 16, 11]), relay.reshape(call_583.astype('bool'), [2912,]), ), 2)
call_592 = relay.TupleGetItem(func_340_call(relay.reshape(const_584.astype('uint32'), [8, 16, 11]), relay.reshape(call_583.astype('bool'), [2912,]), ), 2)
output = relay.Tuple([bop_576,call_580,var_581,call_583,const_584,const_585,call_591,])
output2 = relay.Tuple([bop_576,call_582,var_581,call_586,const_584,const_585,call_592,])
func_593 = relay.Function([var_569,var_581,], output)
mod['func_593'] = func_593
mod = relay.transform.InferType()(mod)
var_594 = relay.var("var_594", dtype = "uint8", shape = (4, 11, 8))#candidate|594|(4, 11, 8)|var|uint8
var_595 = relay.var("var_595", dtype = "uint32", shape = (1800,))#candidate|595|(1800,)|var|uint32
output = func_593(var_594,var_595,)
func_596 = relay.Function([var_594,var_595,], output)
mutated_mod['func_596'] = func_596
mutated_mod = relay.transform.InferType()(mutated_mod)
const_657 = relay.const([[[2.714414,-3.643580,-4.784974,3.369120,-8.766119,0.588181,9.374061,0.959462]],[[-1.179958,-7.756311,-2.937331,-0.998093,-8.992423,-5.252779,2.104777,-8.646706]],[[-8.959100,3.007629,6.234434,6.348761,-5.759290,4.961225,9.103072,3.411624]],[[-9.354519,4.970047,-9.371174,9.494533,-6.102529,0.583245,8.416382,-2.154175]],[[7.799289,-2.894584,-7.652077,-9.064026,-6.772887,-7.419153,-3.308079,-4.040862]],[[-6.646646,0.495818,2.280462,3.011175,-3.815828,4.349069,4.334879,-7.573754]],[[1.366240,3.831940,-4.081798,-4.640153,2.878266,-8.989231,-3.025601,-6.777912]],[[8.775525,-0.209350,-0.398684,-2.306287,-7.249143,-5.993604,4.947795,-8.811931]],[[8.887752,-9.414969,2.784681,-1.470113,5.603484,-9.389827,8.609150,-1.132488]],[[-7.905401,7.554267,2.576314,-8.243681,-5.864606,7.029427,9.970337,-9.488601]],[[6.286543,-9.002584,-6.486171,6.870509,-2.929057,0.033919,-7.922573,-9.003065]],[[-2.968754,4.273242,2.823790,-6.894716,-2.741127,2.809066,1.706910,-7.862772]]], dtype = "float64")#candidate|657|(12, 1, 8)|const|float64
uop_658 = relay.sigmoid(const_657.astype('float64')) # shape=(12, 1, 8)
func_471_call = mod.get_global_var('func_471')
func_475_call = mutated_mod.get_global_var('func_475')
const_661 = relay.const([-7.438700,6.778467,-5.233761,-6.480259,-8.795367,4.956914,-4.907028,-6.739513,7.631923,-3.643628,8.351633,-8.013802,-1.185216,-3.325007,-9.671205,8.627425,8.177460,-7.734998,1.354991,3.427966,3.722599,-5.101527,1.775642,3.798113,3.291085,-4.472376,-5.882460,5.348269,-5.364885,6.988964,-2.417048,8.411368,0.760254,-2.576216,-8.283690,-1.021144,-2.818082,6.593615,2.528619,-7.939779,-2.990806,9.003677,8.080804,8.476904,7.840951,8.160358,3.422297,6.086292], dtype = "float32")#candidate|661|(48,)|const|float32
var_662 = relay.var("var_662", dtype = "bool", shape = (2912,))#candidate|662|(2912,)|var|bool
call_660 = relay.TupleGetItem(func_471_call(relay.reshape(const_661.astype('float32'), [1, 3, 16]), relay.reshape(var_662.astype('bool'), [104, 28]), ), 2)
call_663 = relay.TupleGetItem(func_475_call(relay.reshape(const_661.astype('float32'), [1, 3, 16]), relay.reshape(var_662.astype('bool'), [104, 28]), ), 2)
func_593_call = mod.get_global_var('func_593')
func_596_call = mutated_mod.get_global_var('func_596')
const_673 = relay.const([9,8,9,-9,3,5,10,7,5,5,-10,-2,-3,4,-7,6,1,1,10,-10,-7,-3,6,2,-10,7,-4,-5,-3,4,9,7,4,9,-5,8,-6,1,-3,-1,10,4,-10,-10,9,-4,-4,10,8,-3,-8,7,4,-6,-10,9,-7,-3,-4,-2,7,-3,7,-10,-3,-8,-5,-7,-2,5,1,2,-9,-7,-10,-5,-2,-1,-10,-4,5,5,6,1,6,1,-2,-5,10,3,10,-10,-4,3,-1,8,10,9,5,7,-8,9,1,-10,-8,4,10,-2,2,-8,-4,-10,10,-4,1,-6,-10,-10,1,-4,4,-6,-10,7,-4,9,-3,-6,-10,8,4,10,-1,4,2,-8,6,9,2,1,2,6,9,-8,2,10,-2,-9,3,-2,3,-1,5,8,7,1,-9,5,-9,-7,-9,-7,9,1,-1,-7,6,-7,10,-6,5,4,-6,-2,-4,-6,-5,-3,2,6,-8,10,-3,-4,-4,-7,10,3,-2,1,-5,8,-1,-4,-6,6,5,7,7,-10,2,10,-1,-7,9,1,-4,-5,2,10,10,-2,-6,-5,-2,3,-2,-7,-5,8,-10,-9,-7,-3,-4,7,-9,-2,-7,7,10,3,-3,7,-3,-6,-3,1,-9,-1,7,10,-4,-2,-7,-10,1,3,4,-1,-4,-3,-4,-8,-9,8,6,4,10,3,-7,8,-6,9,8,8,9,-8,-4,-5,-5,8,3,-3,10,-2,-9,-2,-9,5,-4,-1,2,5,-8,-10,-5,8,2,1,-7,8,3,-1,2,-2,-6,-1,-6,6,-9,9,-5,-2,-8,1,-7,-1,9,-3,-7,9,-1,2,7,1,4,-9,-9,-8,-7,-4,5,5,9,-7,6,-8,4,-4,9,6,7,4,8,5,-10,10,-6,1,4,10,4,4,-1,1,-4,-5,2,-9,3,8], dtype = "uint8")#candidate|673|(352,)|const|uint8
var_674 = relay.var("var_674", dtype = "uint32", shape = (1800,))#candidate|674|(1800,)|var|uint32
call_672 = relay.TupleGetItem(func_593_call(relay.reshape(const_673.astype('uint8'), [4, 11, 8]), relay.reshape(var_674.astype('uint32'), [1800,]), ), 3)
call_675 = relay.TupleGetItem(func_596_call(relay.reshape(const_673.astype('uint8'), [4, 11, 8]), relay.reshape(var_674.astype('uint32'), [1800,]), ), 3)
uop_678 = relay.acosh(uop_658.astype('float64')) # shape=(12, 1, 8)
func_471_call = mod.get_global_var('func_471')
func_475_call = mutated_mod.get_global_var('func_475')
call_685 = relay.TupleGetItem(func_471_call(relay.reshape(const_661.astype('float32'), [1, 3, 16]), relay.reshape(call_660.astype('bool'), [104, 28]), ), 2)
call_686 = relay.TupleGetItem(func_475_call(relay.reshape(const_661.astype('float32'), [1, 3, 16]), relay.reshape(call_660.astype('bool'), [104, 28]), ), 2)
func_593_call = mod.get_global_var('func_593')
func_596_call = mutated_mod.get_global_var('func_596')
call_695 = relay.TupleGetItem(func_593_call(relay.reshape(const_673.astype('uint8'), [4, 11, 8]), relay.reshape(var_674.astype('uint32'), [1800,]), ), 2)
call_696 = relay.TupleGetItem(func_596_call(relay.reshape(const_673.astype('uint8'), [4, 11, 8]), relay.reshape(var_674.astype('uint32'), [1800,]), ), 2)
uop_699 = relay.sqrt(uop_658.astype('float64')) # shape=(12, 1, 8)
bop_721 = relay.bitwise_xor(uop_658.astype('uint64'), relay.reshape(const_657.astype('uint64'), relay.shape_of(uop_658))) # shape=(12, 1, 8)
bop_734 = relay.floor_divide(uop_678.astype('float32'), relay.reshape(uop_699.astype('float32'), relay.shape_of(uop_678))) # shape=(12, 1, 8)
output = relay.Tuple([call_660,const_661,var_662,call_672,const_673,var_674,call_685,call_695,bop_721,bop_734,])
output2 = relay.Tuple([call_663,const_661,var_662,call_675,const_673,var_674,call_686,call_696,bop_721,bop_734,])
func_740 = relay.Function([var_662,var_674,], output)
mod['func_740'] = func_740
mod = relay.transform.InferType()(mod)
var_741 = relay.var("var_741", dtype = "bool", shape = (2912,))#candidate|741|(2912,)|var|bool
var_742 = relay.var("var_742", dtype = "uint32", shape = (1800,))#candidate|742|(1800,)|var|uint32
output = func_740(var_741,var_742,)
func_743 = relay.Function([var_741,var_742,], output)
mutated_mod['func_743'] = func_743
mutated_mod = relay.transform.InferType()(mutated_mod)
var_956 = relay.var("var_956", dtype = "int8", shape = (2, 15, 16))#candidate|956|(2, 15, 16)|var|int8
var_957 = relay.var("var_957", dtype = "int8", shape = (2, 15, 16))#candidate|957|(2, 15, 16)|var|int8
bop_958 = relay.add(var_956.astype('int8'), relay.reshape(var_957.astype('int8'), relay.shape_of(var_956))) # shape=(2, 15, 16)
func_336_call = mod.get_global_var('func_336')
func_340_call = mutated_mod.get_global_var('func_340')
const_962 = relay.const([1,-8,-9,1,-6,2,-5,2,9,-6,-8,7,-7,3,-10,2,2,4,10,1,-10,5,-9,3,-8,10,-9,-6,-7,-10,5,10,-9,-1,10,6,-8,-5,-7,6,7,-1,-4,-5,-4,-5,4,-10,-10,3,-4,9,-7,8,5,9,-9,-10,-5,-1,-7,-2,6,5,3,-5,6,-9,-10,-7,3,7,-6,5,10,-2,6,10,-6,-7,3,-3,8,2,-1,3,6,-5,6,6,10,5,-4,8,-7,6,-9,-7,-3,4,-9,-7,6,-7,-4,8,-3,-9,-5,-6,4,-2,-2,-9,-1,10,-8,5,9,-6,-7,8,-7,-8,6,7,-7,-2,-2,-6,1,-1,1,5,-1,4,5,-9,-10,7,10,-3,-2,6,5,-7,5,7,5,9,-3,4,-6,-4,-10,10,2,-5,-10,10,-2,-2,-4,-5,1,5,-7,-5,1,-7,8,-9,3,-9,-6,8,6,6,-1,9,5,7,2,-4,1,4,-1,2,-8,6,-1,-5,-6,-7,2,-8,-3,-8,7,9,-5,9,-5,-9,3,-10,-2,3,6,5,-7,6,8,-4,7,-4,6,6,6,6,-1,-8,-1,-10,-1,6,6,8,5,-10,7,3,-1,7,-4,-1,-1,-7,7,9,10,6,5,-3,-9,-3,9,2,-4,-9,3,-5,-6,5,10,9,-9,-10,-10,7,6,-6,5,-6,8,-1,-3,3,9,-3,6,-10,1,-1,3,-10,9,5,-5,-5,4,4,-2,-9,9,-9,7,9,-1,9,-10,4,-7,5,10,7,-8,3,1,1,7,-6,1,-2,-8,8,-4,-9,-3,-4,-4,7,5,-2,-4,-8,-2,5,10,8,2,7,-10,6,-9,-6,-3,-7,-5,-7,-1,-7,-1,-6,2,10,2,8,4,-7,6,7,8,-10,-2,-1,-5,-6,3,-1,8,8,1,-5,-2,9,10,9,-2,1,9,-9,-10,-3,8,7,7,7,-1,-2,-7,-3,7,-4,-3,4,-7,-8,-7,10,-5,3,-2,10,5,10,-3,8,5,10,7,9,5,2,8,-7,-1,-7,-1,8,-10,-7,-1,2,6,-3,-6,-6,-2,2,10,-5,2,-4,2,8,-10,5,-9,-7,-9,-8,3,-5,-4,-6,-10,7,-4,4,5,-8,-8,-6,9,4,2,-4,-9,1,-8,10,-8,10,8,-8,6,7,8,-1,-7,-5,-8,-7,10,8,4,7,-5,-6,9,-7,1,-8,-9,3,5,-6,-1,-8,10,-10,-6,-10,2,-7,1,5,-9,-10,4,-6,-3,10,5,4,5,-2,1,-5,10,-5,5,-3,-4,7,-8,7,-5,-7,6,-6,7,6,-1,-10,-3,2,-4,-4,-7,8,-4,-7,3,-9,-7,-2,4,10,-8,-4,7,9,-10,10,6,3,3,8,5,-5,-2,-5,-4,10,9,-3,10,8,6,7,5,9,3,-6,-3,-1,7,-1,-4,4,-5,-10,8,-4,5,4,3,-10,1,7,6,-10,5,-5,-2,-4,4,1,1,6,-7,8,6,-6,-3,-2,10,-3,5,8,4,4,6,-2,1,3,-8,7,8,-2,8,-1,8,-7,-1,-2,-7,-5,-2,-9,4,-2,-4,8,-4,-4,-4,3,10,-7,-3,8,-5,-2,-9,-1,-5,-5,2,1,-4,8,-2,10,-1,5,-5,-3,-5,9,-5,4,3,-9,5,-3,-6,6,4,-10,-2,8,-7,8,-7,3,-7,-4,-8,-9,6,1,5,-8,3,5,-4,-3,-7,2,-9,-5,-3,1,5,-6,2,-1,-5,7,8,5,6,-4,2,6,-10,-8,-2,-4,-8,8,-8,-8,-7,-2,8,10,7,8,7,-1,-7,-7,7,-5,-2,5,-1,4,8,6,3,-2,9,2,-4,-2,1,1,3,-2,-1,4,2,2,3,-5,-4,-9,-7,-7,-3,3,10,-1,-9,7,-4,2,10,5,9,-10,-7,4,-1,8,-1,7,4,-2,2,3,-2,-9,6,-4,4,-10,6,-8,6,-10,-6,8,-4,4,-2,2,-1,-4,5,-4,5,-1,-7,-7,-4,9,3,-1,-8,3,-2,-1,7,2,7,-2,-1,5,-3,-2,-9,-8,-6,1,4,3,-8,10,4,-7,9,5,-4,9,-3,4,-2,6,1,-4,-3,10,-3,-9,4,10,-5,5,-5,7,-5,-2,1,-7,-7,-9,7,-2,-2,9,-6,9,-4,-3,9,7,-10,3,8,6,-10,-6,4,9,-10,2,-9,-1,5,2,-3,8,-7,-7,-8,10,9,4,7,-1,-4,-5,6,-6,10,-3,-6,-8,-1,-9,1,-8,7,-6,-7,-1,2,6,2,8,-1,-8,-3,1,3,-2,1,-7,-2,-5,9,-2,4,8,-1,9,-9,-10,-3,-4,-2,3,6,4,-2,-9,-6,4,2,-7,10,4,5,10,4,8,-2,-9,-2,8,-1,5,-9,-9,-2,-3,-4,-2,2,7,-7,2,-6,8,4,-2,-3,4,7,-5,10,3,-5,-3,8,3,-4,3,-5,-10,6,-6,10,-3,5,-9,-5,9,9,9,1,-1,8,-9,-6,4,2,3,3,-2,-3,3,3,-2,-5,10,-4,3,8,4,10,5,1,-3,-3,3,5,-8,10,-3,-10,1,5,-5,-5,-6,-1,6,-1,6,-5,4,5,-8,-1,-9,5,6,-3,2,3,2,1,6,8,-5,-1,1,-10,-2,-2,-3,-3,7,-1,-4,9,8,6,1,8,-5,7,-6,8,10,-10,-7,2,-9,-2,-9,10,10,-3,-8,-9,9,-2,4,2,-8,-7,-3,8,3,-4,-3,-4,-8,8,-8,-2,4,2,4,2,-4,8,9,9,7,8,6,5,-9,-4,9,-3,-10,2,7,-5,-6,-8,8,-9,-1,-7,9,2,6,-4,-2,1,-10,-5,9,-7,4,10,-3,8,-7,2,10,5,-2,2,-4,7,6,-2,-3,-9,-4,-8,9,-2,3,-4,8,9,-8,5,6,9,-5,6,-10,4,6,-3,-1,3,9,-9,9,-6,-10,1,2,-7,-1,-6,10,6,-3,10,6,-10,-3,3,-6,8,-1,-4,-1,1,-6,6,6,-1,-3,-2,6,-7,10,8,-8,-6,9,1,2,3,-8,3,3,2,9,-6,-8,4,2,6,2,8,-9,-1,-2,9,3,1,-10,-3,-8,5,-1,-4,3,-2,1,4,10,2,-10,-1,5,-1,6,-5,3,2,9,9,-5,8,-3,-5,10,7,8,-4,-2,9,9,4,-6,-9,2,8,1,3,-8,8,-6,7,1,-1,8,-2,-4,2,3,-6,9,10,9,3,4,7,-4,-5,8,9,6,5,-8,-1,-6,5,10,-5,-1,-8,8,4,-10,9,5,-3,1,-2,-5,-1,-1,-8,2,-1,2,5,-7,-3,7,4,-2,-4,5,4,-10,-10,-1,-1,-2,5,6,-5,8,9,-2,9,9,6,1,5,7,2,6,1,8,3,8,6,-5,-3,-7,10,-8,-2,-8,-8,-4,5,4,7,3,-7,-7,-7,7,9,4,9,-8,1,-10,3,9,-2,-3,8,-1,7,9,4,5,9,-5,-1,1,-8,-1,3,-6,-5,-7,5,10,-8,5,5,5,9,-4,2,-4,-8,-9,7,7,-6,-4,2,2,-3,2,-7,1,7,-8,-1,-9,-9,2,-6,7,3,5,-7,7,-6,-5,-8,-10,-2,-5,-5,3,-3,-10,-4,-4,-10,4,10,7,-10,10,1,-2,10,-7], dtype = "uint32")#candidate|962|(1408,)|const|uint32
var_963 = relay.var("var_963", dtype = "bool", shape = (2912,))#candidate|963|(2912,)|var|bool
call_961 = relay.TupleGetItem(func_336_call(relay.reshape(const_962.astype('uint32'), [8, 16, 11]), relay.reshape(var_963.astype('bool'), [2912,]), ), 0)
call_964 = relay.TupleGetItem(func_340_call(relay.reshape(const_962.astype('uint32'), [8, 16, 11]), relay.reshape(var_963.astype('bool'), [2912,]), ), 0)
const_977 = relay.const([True,True,False,False,True,True,False,True,False,False,False,False,False,True,True,False,True,True,False,True,False,False,True,False,False,False,False,False,True,True,False,False,False,False,False,False,False,True,True,False,True,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,False,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,True,True,False,False,True,True,True,True,True,False,True,False,False,True,False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,False,False,True,True,False,True,True,False,False,False,True,True,True,True,True,False,True,False,False,False,False,False,True,True,True,True,True,False,True,True,False,False,False,False,True,False,True,False,False,False,True,True,True,False,True,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,True,True,False,True,True,False,True,True,False,False,True,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,True,True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,False,True,True,False,True,True,True,False,False,True,False,False,True,False,True,False,True,True,False,True,False,False,True,False,True,True,True,True,True,True,False,True,False,True,True,True,False,False,False,True,False,False,True,True,True,False,False,False,True,False,True,True,False,False,True,True,True,True,False,True,False,False,False,False,True,False,True,False,False,True,True,False,False,False,False,True,True,False,True,False,False,True,False,True,True,True,False,True,False,True,False,False,True,False,False,True,False,False,True,True,True,False,True,True,False,True,False,True,True,False,False,False,True,False,True,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,True,False,False,True,False,False,False,False,False,False,False,False,False,True,False,True,False,True,False,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,False,False,False,False,True,False,False,True,False,False,True,False,True,True,False,False,False,True,True,True,True,False,False,False,False,False,False,False,True,True,False,True,True,False,True,False,True,False,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,False,True,True,False,False,True,True,True,True,False,False,True,False,True,False,False,True,False,False,False,False,False,False,False,False,False,True,True,False,False,False,True,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,False,True,False,False,True,True,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,True,False,True,True,True,False,True,False,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,False,False,False,True,False,False,True,True,False,False,False,False,False,True,False,True,True,False,False,False,False,False,False,True,True,False,False,True,True,False,False,False,False,False,True,False,False,False,True,True,True,False,True,True,True,True,False,False,False,True,False,False,True,False,True,True,False,True,False,False,True,False,False,True,False,True,True,False,True,True,True,False,True,False,False,False,False,False,True,False,True,True,False,True,False,True,False,False,False,False,False,False,False,False,True,False,True,True,False,True,False,False,True,True,False,True,True,False,False,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,True,True,False,True,False,True,False,False,True,True,True,True,True,True,False,True,True,False,False,True,True,True,True,False,True,False,False,False,True,False,False,False,False,True,True,False,False,True,True,True,True,False,False,False,True,False,True,True,True,True,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,True,False,True,False,True,False,True,True,True,True,True,True,False,False,False,False,False,False,False,False,True,False,False,False,False,True,True,True,True,True,False,False,True,False,False,False,False,False,True,True,True,False,True,False,False,True,False,True,False,False,True,True,True,False,True,True,True,False,False,False,True,True,False,False,True,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True,True,True,False,False,True,True,True,True,False,False,True,True,True,False,False,False,True,False,True,False,False,False,False,True,False,True,False,False,True,False,True,False,True,False,False,True,True,False,False,True,False,True,True,True,True,True,True,False,True,False,False,False,True,True,True,True,False,True,True,True,True,True,False,False,True,False,True,False,False,True,False,False,True,True,True,False,False,False,True,True,True,True,True,False,False,False,True,False,True,True,False,False,False,False,True,True,False,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,False,True,False,False,False,False,True,True,True,True,False,True,True,True,False,True,True,True,False,True,True,False,False,True,True,False,False,False,False,False,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,True,True,True,False,True,False,False,True,True,True,True,True,True,False,True,False,False,True,False,True,False,True,True,True,False,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,True,False,True,False,False,False,True,False,True,True,False,False,False,True,True,False,False,False,False,False,False,True,False,False,True,False,True,True,False,False,False,True,False,True,False,False,False,True,False,True,False,False,True,False,False,True,True,False,True,True,False,True,False,True,False,True,True,True,False,False,True,False,True,True,False,True,True,False,False,False,True,False,False,True,True,False,False,False,False,True,True,True,False,True,False,False,False,True,False,False,True,True,False,True,True,False,False,False,False,True,False,False,True,True,True,False,True,True,False,False,False,True,True,False,False,True,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,False,True,True,False,False,False,False,True,True,True,True,True,False,False,True,True,True,False,False,False,False,False,False,False,True,False,False,False,True,True,True,True,False,False,True,False,False,False,True,True,True,True,True,False,True,False,True,False,True,True,False,True,False,True,True,True,True,False,True,True,True,True,False,True,True,False,True,False,False,True,True,True,False,False,True,True,True,False,True,False,False,True,True,False,False,False,True,False,False,False,True,True,True,True,False,True,True,False,True,True,True,False,True,True,True,False,False,False,True,True,False,True,False,True,True,True,True,False,True,False,False,False,True,False,True,False,True,True,False,False,False,True,False,True,False,True,False,False,True,True,True,True,False,True,False,True,False,False,True,True,False,True,True,True,True,True,True,False,False,True,False,False,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,True,False,True,True,False,False,False,True,False,True,True,False,True,False,True,False,True,False,False,True,False,False,False,False,True,True,False,False,False,False,False,False,False,True,True,False,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,False,False,False,False,False,False,True,True,True,False,True,True,True,False,False,True,True,False,False,True,True,False,True,False,True,True,False,False,True,True,False,True,False,False,True,False,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,False,True,True,True,False,False,True,False,True,False,False,False,False,True,True,False,True,True,False,True,False,True,False,True,False,True,False,True,False,True,True,True,False,False,False,False,False,True,False,True,True,True,True,False,False,False,False,True,False,False,False,False,True,False,True,False,True,True,True,False,False,True,True,False,True,True,False,False,False,True,True,True,False,True,True,False,True,False,True,True,False,False,True,False,False,True,False,False,False,True,False,True,False,True,True,False,False,False,False,False,True,True,True,True,False,True,True,False,True,False,True,True,False,True,True,True,False,True,True,False,True,True,True,True,False,True,True,False,True,True,False,False,True,True,True,True,False,False,True,True,False,True,True,True,False,False,False,False,False,True,False,True,False,False,False,False,True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,True,False,False,False,False,True,False,False,True,True,True,False,True,True,False,True,False,False,True,False,False,True,False,False,True,True,False,True,False,False,False,True,False,True,False,True,False,False,True,True,False,False,True,True,True,True,True,True,False,False,True,False,False,True,False,True,False,True,False,False,True,False,False,True,True,False,False,True,False,False,False,False,False,True,False,False,True,True,True,True,True,True,True,True,False,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,False,False,False,False,False,True,True,True,False,True,False,True,False,True,False,True,False,True,True,True,False,False,True,True,True,False,True,True,False,False,True,True,False,True,True,False,False,True,False,False,False,False,True,False,True,False,True,True,True,True,True,True,True,False,True,False,False,False,True,True,False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,True,False,True,False,True,False,True,True,False,False,True,False,False,True,True,True,False,True,False,False,True,True,True,True,True,True,False,True,False,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,False,True,False,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,False,False,False,True,True,True,False,True,True,True,False,True,False,True,False,True,True,True,True,False,True,True,True,True,False,False,False,False,False,True,True,False,True,True,False,False,False,False,True,True,True,True,False,True,False,True,False,False,False,False,False,False,True,True,True,False,False,True,False,False,False,True,False,True,False,False,True,True,False,False,False,True,False,True,True,False,False,True,False,False,True,True,False,True,False,True,True,False,True,True,False,True,True,True,True,True,True,False,False,False,True,True,True,True,False,False,True,False,False,False,False,True,True,True,False,True,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,True,True,True,False,True,True,True,False,True,False,True,False,True,False,True,False,False,False,True,False,True,True,True,False,False,True,True,True,False,True,False,True,True,False,True,False,True,True,False,False,True,False,False,False,False,True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,True,False,True,False,True,False,False,False,True,True,True,False,False,True,True,True,False,True,True,True,True,True,False,True,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False,False,True,True,False,False,False,True,False,True,True,False,True,False,False,True,True,False,False,False,False,False,True,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,False,False,True,True,False,False,True,True,True,False,True,False,True,True,False,False,False,True,False,True,False,False,False,False,True,False,False,False,True,True,False,False,True,True,True,False,True,True,True,False,True,False,False,False,True,True,False,True,False,False,False,False,True,True,False,False,True,True,False,False,False,False,False,True,True,False,True,False,True,False,True,False,False,True,True,True,False,True,True,False,False,True,True,True,False,True,True,True,False,True,False,False,False,False,False,True,False,True,False,True,False,True,False,False,False,True,False,True,False,True,True,False,False,False,True,True,False,False,False,False,False,False,True,False,True,True,True,True,False,True,True,False,False,True,True,True,False,True,False,False,False,True,True,False,False,False,True,False,True,False,False,True,False,True,True,True,False,False,True,True,False,False,True,False,True,False,True,True,True,True,True,True,True,False,False,True,True,True,True,False,True,True,True,False,True,False,True,True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True,True,False,True,False,True,True,True,True,False,False,False,False,True,False,False,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,False,True,False,True,False,False,True,True,True,True,True,True,False,False,True,True,False,False,True,False,True,True,True,False,True,False,True,False,False,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,True,True,True,True,False,False,True,True,True,True,True,False,True,False,True,False,False,False,False,False,False,False,False,False,True,True,True,True,True,True,True,False,False,False,True,False,True,True,True,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False,True,False,True,False,True,False,True,True,True,True,False,False,True,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False,True,False,False,True,False,False,False,True,True,False,True,False,True,False,True,False,True,False,False,False,False,False,False,False,True,False,False,False,True,True,True,False,False,True,True,False,False,True,False,True,True,True,True,True,False,False,True,True,True,True,True,True,True,False,True,False,False,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,True,False,True,False,True,True,True,True,False,False,False,False,True,True,True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,False,True,False,False,True,True,True,False,True,False,False,True,True,False,True,False,False,True,False,True,False,False,True,False,False,True,False,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,True,False,False,False,True,False,False,False,False,True,True,False,True,True,True,False,True,False,True,True,True,False,False,True,True,True,True,True,True,True,False,True,True,True,True,False,True,True,True,True,False,False,False,True,True,True,True,False,True,False,False,False,True,False,True,False,True,False,True,True,True,True,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,False,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,True,False,False,False,False,False,True,False,True,False,True,False,False,False,False,False,True,True,True,False,True,False,True,True,False,True,True,False,True,False,False,False,True,True,True,True,True,False,True,False,False,True,False,False,True,False,True,False,True,False,False,True,False,True,False,False,False,True,True,True,True,True,False,False,False,True,True,True,True,True,True,True,False,True,True,True,True,False,True,True,False,True,False,True,False,False,True,False,True,False,False,False,False,False,True,False,True,False,False,False,True,True,True,True,True,False,False,False,True,True,True,True,False,True,False,False], dtype = "bool")#candidate|977|(2912,)|const|bool
bop_978 = relay.bitwise_or(var_963.astype('int32'), relay.reshape(const_977.astype('int32'), relay.shape_of(var_963))) # shape=(2912,)
output = relay.Tuple([bop_958,call_961,const_962,bop_978,])
output2 = relay.Tuple([bop_958,call_964,const_962,bop_978,])
func_981 = relay.Function([var_956,var_957,var_963,], output)
mod['func_981'] = func_981
mod = relay.transform.InferType()(mod)
var_982 = relay.var("var_982", dtype = "int8", shape = (2, 15, 16))#candidate|982|(2, 15, 16)|var|int8
var_983 = relay.var("var_983", dtype = "int8", shape = (2, 15, 16))#candidate|983|(2, 15, 16)|var|int8
var_984 = relay.var("var_984", dtype = "bool", shape = (2912,))#candidate|984|(2912,)|var|bool
output = func_981(var_982,var_983,var_984,)
func_985 = relay.Function([var_982,var_983,var_984,], output)
mutated_mod['func_985'] = func_985
mutated_mod = relay.transform.InferType()(mutated_mod)
var_999 = relay.var("var_999", dtype = "int32", shape = (1, 7, 12))#candidate|999|(1, 7, 12)|var|int32
var_1000 = relay.var("var_1000", dtype = "int32", shape = (8, 7, 12))#candidate|1000|(8, 7, 12)|var|int32
bop_1001 = relay.multiply(var_999.astype('int32'), var_1000.astype('int32')) # shape=(8, 7, 12)
bop_1012 = relay.greater(var_999.astype('bool'), var_1000.astype('bool')) # shape=(8, 7, 12)
output = relay.Tuple([bop_1001,bop_1012,])
output2 = relay.Tuple([bop_1001,bop_1012,])
func_1040 = relay.Function([var_999,var_1000,], output)
mod['func_1040'] = func_1040
mod = relay.transform.InferType()(mod)
mutated_mod['func_1040'] = func_1040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1040_call = mutated_mod.get_global_var('func_1040')
var_1042 = relay.var("var_1042", dtype = "int32", shape = (1, 7, 12))#candidate|1042|(1, 7, 12)|var|int32
var_1043 = relay.var("var_1043", dtype = "int32", shape = (8, 7, 12))#candidate|1043|(8, 7, 12)|var|int32
call_1041 = func_1040_call(var_1042,var_1043,)
output = call_1041
func_1044 = relay.Function([var_1042,var_1043,], output)
mutated_mod['func_1044'] = func_1044
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1080 = relay.var("var_1080", dtype = "float64", shape = (11, 5, 3))#candidate|1080|(11, 5, 3)|var|float64
const_1081 = relay.const([[[-4.559550,-5.352958,0.609716],[0.346007,8.076021,-8.452209],[-2.127656,-9.926908,-6.103554],[-5.513225,-1.762784,3.580872],[-5.522732,-8.823450,0.481971]],[[-8.714662,-3.776630,1.891488],[8.090350,1.762977,-3.111631],[4.499007,-9.730533,0.113808],[-5.305087,2.402250,0.971616],[-9.133822,-6.425998,-6.387912]],[[0.167450,1.981418,1.642584],[3.379586,7.698307,5.871802],[-4.926410,-6.750771,-1.555152],[4.462817,2.453089,8.109197],[-6.290783,-9.890635,-1.696118]],[[-0.293551,8.239085,9.840063],[-3.310128,-4.817688,3.144971],[-5.593243,-0.126663,-2.749985],[-3.019296,8.713262,1.273168],[-5.819100,4.539545,-6.565725]],[[5.946264,9.258961,-2.927100],[8.274983,5.261826,8.740720],[-0.738160,5.132448,-2.637203],[0.183540,5.869520,1.083710],[-6.061882,-3.146169,-8.758928]],[[5.837892,8.927038,8.112352],[-8.598393,4.164271,-7.246368],[-6.673541,-9.007914,5.347868],[-0.122602,9.890581,-7.942702],[-1.407084,-6.481952,-4.257501]],[[1.119180,-3.451361,-4.646682],[-9.498096,-6.597765,-3.095374],[-1.534174,8.375192,-0.102563],[-0.918212,-2.889099,9.838244],[-6.353548,6.472594,-9.554555]],[[0.738095,0.109429,0.843860],[7.625976,-2.429878,1.226654],[-1.971855,-3.900165,-3.764471],[6.111913,5.819462,-0.569984],[-7.983700,-4.247768,9.956000]],[[9.780621,-6.335711,-6.162883],[-5.106102,3.847110,7.853980],[6.334952,9.708411,-2.530530],[8.220258,-1.308283,2.824601],[4.112243,8.400306,3.885626]],[[-6.783550,9.622597,7.270551],[-4.368988,-0.721393,3.262145],[-2.549355,8.530308,-1.057376],[9.187272,4.137289,-0.015109],[-4.173621,-0.657991,2.131976]],[[-3.101183,-5.195477,-2.098483],[5.434737,6.314133,-5.089058],[-6.416811,-7.758839,-9.521153],[6.629922,-4.045400,4.688147],[8.827451,-2.618117,7.844446]]], dtype = "float64")#candidate|1081|(11, 5, 3)|const|float64
bop_1082 = relay.floor_mod(var_1080.astype('float64'), relay.reshape(const_1081.astype('float64'), relay.shape_of(var_1080))) # shape=(11, 5, 3)
uop_1092 = relay.log(bop_1082.astype('float32')) # shape=(11, 5, 3)
func_981_call = mod.get_global_var('func_981')
func_985_call = mutated_mod.get_global_var('func_985')
var_1107 = relay.var("var_1107", dtype = "int8", shape = (480,))#candidate|1107|(480,)|var|int8
const_1108 = relay.const([[False,True,False,False,True,False,False,True,True,False,False,False,True,True,True,True,True,True,True,True,True,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,False,False,False,True,False,False,False,True,True,True,False,False,True,True,True,True,True,True,True,True,True,True,False,False,False,False,True,True,True,False,True,False,False,False,True,False,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,True,True,True,False,True,True,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,False,True,True,True,False,False,False,False,True,True,True,False,False,True,False,True,False,False,False,True,False,True,False,False,True,False,True,True,True,True,True,True,False,False,True,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,False,False,False,True,False,True,False,True,False,True,True,False,False,False,True,True,True,True,True,False,True,True,False,True,False,False,True,True,True,False,False,True,False,False,False,False,True,True,False,True,False,True,False,False,True,True,True,False,False,False,False,False,False,True,True,False,True,False,True,False,False,True,True,True,False,False,True,True,True,True,True,True,False,True,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,True,True,False,False,True,True,False,True,False,False,False,False,True,True,False,False,True,False,False,True,False,False,True,False,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,True,False,False,False,False,True,False,False,False,False,False,True,False,True,False,False,False,True,True,False,True,False,False,False,True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True],[False,False,True,False,True,False,False,True,False,False,True,False,True,True,False,True,True,False,True,True,True,True,False,True,False,True,True,False,True,True,True,False,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,False,True,False,True,False,True,True,True,True,False,False,True,False,True,True,False,False,False,False,False,True,False,False,True,False,True,False,False,True,True,False,True,False,False,True,True,False,False,False,True,True,True,True,True,False,False,True,True,False,True,True,True,True,True,True,True,False,True,True,False,False,False,True,False,False,False,True,False,True,False,False,False,True,True,True,True,True,False,False,True,True,False,False,False,True,True,True,False,False,True,False,False,True,True,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,True,True,True,True,True,True,True,True,False,True,True,True,True,False,False,False,True,False,False,True,False,True,False,False,False,True,True,False,False,True,False,False,False,True,True,True,False,False,False,True,True,False,False,False,False,True,True,True,True,True,False,True,True,False,True,True,False,False,False,False,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True,True,False,False,True,False,True,False,True,False,True,True,False,True,True,True,False,False,False,False,False,False,False,False,True,False,False,False,False,True,True,True,False,True,True,True,False,False,True,True,False,True,False,False,False,True,True,False,True,True,False,True,True,True,False,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,True,True,False,True,True,False,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,False,True,True,True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,True,False,False,True,True,True,False,False,False,False,False,False,False,True,False,True,False,False,False],[False,False,False,False,False,True,True,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,True,True,False,False,True,True,False,True,True,False,True,False,True,False,True,False,True,True,True,True,False,False,False,True,False,False,True,False,False,False,False,True,True,False,True,False,True,True,True,True,False,True,True,True,True,False,True,False,True,True,True,True,True,True,False,True,True,False,True,False,False,True,True,True,True,True,True,False,False,False,True,False,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,True,False,False,True,False,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,True,True,False,True,True,False,False,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False,False,True,False,True,False,False,False,False,False,True,True,True,True,False,False,False,True,False,True,False,True,True,True,False,True,False,False,False,False,False,False,False,True,False,False,True,False,False,True,True,True,True,False,False,True,False,False,False,False,False,True,True,True,False,False,False,False,False,False,False,True,True,True,False,True,True,False,False,True,True,True,False,False,True,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,True,False,False,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,True,True,False,False,False,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,False,True,False,False,False,False,False,False,False,True,False,True,False,False,True,False,False,True,True,True,True,False,False,False,True,True,False,True,True,False,True,True,False],[True,False,False,False,False,False,False,True,False,False,True,True,True,False,True,False,True,False,True,False,False,True,True,False,True,False,True,False,True,False,False,True,False,False,True,False,False,True,True,True,True,True,False,True,True,True,True,False,True,True,False,True,False,True,True,False,True,False,False,True,True,False,False,True,False,True,False,False,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,False,False,False,False,True,True,False,False,False,False,False,True,False,True,True,False,False,True,False,False,True,True,True,True,False,True,True,True,True,True,False,True,True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,False,True,True,True,True,False,False,True,False,True,False,True,True,True,False,False,False,True,True,False,False,True,False,True,True,True,False,False,False,True,False,False,True,True,False,False,False,False,True,False,False,True,True,True,False,True,True,False,False,True,False,False,False,False,True,True,False,True,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,False,False,False,True,False,True,True,True,True,True,True,False,False,False,False,True,True,False,True,True,True,True,False,False,False,True,False,True,False,True,True,False,False,True,True,False,False,False,True,False,True,False,False,True,False,False,False,True,False,True,False,False,False,False,False,True,True,False,False,True,False,True,True,False,False,False,False,True,False,True,True,True,True,True,False,True,True,False,False,True,False,True,True,False,True,False,True,True,False,True,False,False,False,False,False,True,False,False,False,True,True,True,False,False,False,True,True,True,True,False,False,True,True,False,False,False,False,True,True,False,True,False,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,True,False,False,True,True,False,False,True,False,True,True,True,False,True,False,False,False,False,False,False,False,True,False],[True,False,True,False,False,True,False,True,True,False,False,False,True,False,True,False,False,False,True,True,False,True,False,True,True,False,True,True,False,False,True,True,True,True,False,True,False,False,True,True,False,True,False,False,True,True,False,True,True,False,False,True,True,False,False,False,False,False,False,True,False,True,False,True,False,False,True,True,False,False,False,True,True,False,True,False,True,True,True,False,True,True,False,False,False,False,True,False,False,True,True,True,False,False,False,True,False,True,False,True,True,False,False,False,True,True,False,False,False,True,True,False,True,True,False,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,False,False,False,False,True,True,False,False,True,False,True,False,True,False,False,True,False,True,True,False,True,False,True,False,True,False,False,True,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,True,False,False,False,False,True,False,True,False,False,False,True,True,False,True,True,True,False,True,True,True,False,False,True,False,True,True,True,True,True,True,False,False,True,False,False,False,False,True,True,False,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,True,False,False,True,False,False,True,True,False,False,True,False,True,False,False,False,True,False,False,False,True,False,False,False,False,False,True,True,True,True,False,True,True,False,False,True,False,True,True,False,True,False,True,True,False,True,True,True,True,True,True,True,True,True,True,False,False,False,True,True,True,True,False,False,False,True,False,False,False,True,True,False,True,False,True,False,True,False,True,True,True,True,False,True,False,True,True,False,True,False,False,False,True],[False,False,True,True,False,False,False,True,True,False,True,True,True,True,False,True,False,True,False,True,True,True,False,False,False,False,True,False,False,True,False,True,False,True,False,False,True,False,False,False,False,True,True,True,False,False,False,False,True,True,False,True,False,False,True,True,False,True,True,True,False,True,False,False,True,False,True,False,True,True,True,True,False,False,True,False,False,True,False,False,False,False,True,True,False,False,False,True,True,True,False,False,True,False,False,False,False,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,False,True,False,True,False,False,True,False,True,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,False,False,True,True,False,True,False,False,False,False,False,False,True,False,False,True,False,False,True,False,False,True,True,True,True,False,False,True,False,True,False,True,False,True,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True,True,False,False,True,False,False,True,False,False,True,True,False,True,False,True,False,False,False,False,True,False,True,True,True,False,False,True,False,True,True,True,False,False,True,True,False,True,False,False,True,True,False,True,True,False,True,True,False,True,True,False,True,True,True,False,True,True,True,True,False,True,True,True,True,False,False,True,False,True,True,True,False,True,True,True,False,False,True,False,True,False,False,False,True,True,False,False,False,True,False,True,False,True,False,True,True,False,False,True,True,False,True,False,True,False,True,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,True,True,True,False,True,False,False,True,False,False,True,False,True],[False,False,False,True,False,True,False,True,True,True,False,False,True,False,True,False,False,False,True,True,True,True,True,True,True,False,True,True,True,True,False,False,False,False,True,False,True,True,True,True,False,False,True,True,False,False,True,False,False,True,True,True,False,False,True,False,False,False,True,False,False,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,False,True,True,True,True,False,False,False,False,False,False,True,False,False,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,False,True,True,False,False,False,True,False,False,True,False,True,True,False,True,False,True,False,False,True,True,True,True,True,False,False,False,True,False,True,False,False,False,True,False,False,False,True,True,False,False,True,True,False,True,True,False,True,True,False,False,False,False,False,True,False,False,False,False,False,True,False,True,True,False,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,False,False,False,False,False,True,True,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,False,False,True,True,True,True,True,False,True,True,False,True,False,False,False,True,False,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,True,False,False,False,True,True,False,False,False,False,True,False,False,True,True,False,True,True,True,True,False,False,False,True,False,True,False,False,False,True,True,True,True,True,True,False,False,False,True,False,False,False,True,True,False,False,True,True,False,False,False,False,True,False,False,True,False,False,True,False,True,False,True,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,False,True,False,False,False,True,True,False,False,True,False,True,True,False,False,False,False,True],[False,True,True,True,True,True,False,False,False,False,False,True,True,False,True,True,True,True,False,False,True,False,True,True,False,False,True,False,False,False,True,False,True,False,True,True,True,True,True,True,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,True,False,True,True,False,True,True,False,False,True,False,True,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,False,False,True,False,False,False,True,False,True,True,False,True,True,True,True,True,True,False,False,True,False,False,True,True,False,True,True,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,False,True,True,False,True,True,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,False,False,True,True,True,True,False,True,True,False,True,False,False,False,True,False,False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,True,True,True,True,True,False,False,True,True,True,False,False,False,False,False,True,True,False,False,False,False,True,False,True,True,True,True,False,False,True,True,True,False,False,False,True,True,True,False,False,False,False,False,False,False,False,False,True,True,False,False,True,True,False,True,False,False,False,False,False,True,False,True,True,False,False,False,True,True,False,False,True,True,False,True,True,True,True,True,False,False,True,True,True,True,False,False,True,False,False,True,True,False,True,False,True,True,False,False,False,True,False,True,False,True,False,True,False,False,False,False,False,True,True,True,True,False,True,False,False,False,False,False,False,True,False,True,False,True,False,False,False,False,True,False,True,True,True,True,True,False,True,True,True,True,True,False,True,False,True,True,False,True,True,True,False,False,False,False,True,False,False,True,True,True,True,False,False,False]], dtype = "bool")#candidate|1108|(8, 364)|const|bool
call_1106 = relay.TupleGetItem(func_981_call(relay.reshape(var_1107.astype('int8'), [2, 15, 16]), relay.reshape(var_1107.astype('int8'), [2, 15, 16]), relay.reshape(const_1108.astype('bool'), [2912,]), ), 3)
call_1109 = relay.TupleGetItem(func_985_call(relay.reshape(var_1107.astype('int8'), [2, 15, 16]), relay.reshape(var_1107.astype('int8'), [2, 15, 16]), relay.reshape(const_1108.astype('bool'), [2912,]), ), 3)
func_336_call = mod.get_global_var('func_336')
func_340_call = mutated_mod.get_global_var('func_340')
const_1113 = relay.const([1,-7,-3,8,3,-10,8,-5,7,-5,-1,-7,-3,-7,-7,-5,4,7,-5,5,9,-9,1,9,7,-8,-2,9,9,-6,-4,-7,3,6,-10,-5,6,-9,9,-4,-4,7,7,-1,3,5,8,-4,5,-8,10,-6,-9,-5,3,-7,4,-2,9,9,3,-9,-5,4,4,-5,-7,-5,5,7,1,-2,-7,4,-8,-7,-7,1,-3,2,-9,4,-7,4,-8,10,6,-2,6,8,1,4,4,-9,-2,-4,9,7,-6,-8,6,2,9,5,-2,-9,8,10,-9,-1,-2,-2,-5,-7,-1,-3,-4,-9,1,-10,6,-5,-3,8,-5,-2,6,-6,-2,9,-7,-10,-9,5,2,-2,-5,3,-3,-9,-10,3,-3,-6,-3,10,-9,-10,9,10,-1,10,-1,-3,3,-5,2,-10,9,2,1,2,2,10,-9,5,-3,7,9,10,-3,7,-3,10,3,3,-6,3,9,1,4,-8,-2,-4,-5,5,9,5,8,-7,-9,-4,7,3,3,-2,2,5,-4,-7,3,-9,1,-6,9,-10,6,-3,1,9,-2,10,-10,9,2,-5,7,7,7,-9,-9,-7,10,9,6,5,10,1,8,4,-6,-5,4,-1,9,9,8,4,8,1,-3,3,2,3,-5,-2,-7,-4,-2,4,-4,9,1,-9,-9,2,-7,-3,-10,-8,3,-6,10,-1,-4,2,-8,-9,4,-7,-8,-3,7,-3,4,1,-3,8,-6,4,6,7,6,-4,-4,3,1,7,4,4,-1,-7,-4,8,6,10,-9,-7,-3,-7,-1,8,-8,9,-3,2,-1,-10,4,5,-1,3,3,7,10,-10,-6,-2,-3,6,5,2,7,-3,10,-4,-4,-3,6,1,-7,6,1,-8,10,-10,4,-2,-4,3,-2,6,-3,-1,2,4,4,3,-9,-8,4,3,-10,8,-10,7,-5,8,-6,6,2,7,3,3,-10,-8,-1,-2,-8,4,-1,-1,-5,-6,-9,-1,6,9,8,9,5,2,-2,6,7,9,-10,-6,-1,-8,-7,-3,6,10,6,-4,1,-6,2,-3,9,-7,-6,5,-5,8,-1,5,-5,-3,-8,-1,-5,-2,-6,-6,-10,-5,7,-2,3,4,-2,-1,-8,5,1,5,-2,3,-3,-4,-5,7,-7,4,-2,-3,-9,-1,-9,3,4,-6,-4,-4,-1,7,-5,7,5,3,-10,-2,-1,6,-9,1,-6,10,9,4,-2,5,-7,-3,-2,10,5,10,4,9,4,9,-7,7,-4,-6,-4,-6,-5,-1,-9,10,-2,-1,6,-10,-10,-10,7,-2,10,9,-3,3,6,-5,-7,-9,5,3,-2,2,3,8,1,3,2,-3,7,-10,-4,-7,10,-9,-8,6,7,-1,-2,-10,-10,2,5,6,-5,-4,-1,-9,-1,-6,3,10,-10,2,-1,-4,-7,3,-6,-1,-5,-10,-10,-9,-1,9,-7,-6,9,10,2,2,-2,9,-6,-9,-9,-9,-9,-9,3,4,8,-8,10,8,-2,1,-5,-2,-5,2,-1,3,9,-2,-2,2,-8,7,-8,4,-3,-6,7,9,-10,-8,-2,-4,-2,3,5,-2,-6,5,-3,-6,3,-7,1,-2,9,-3,-10,-1,-5,6,2,5,6,3,-6,-8,-2,-7,2,-3,1,1,-7,4,9,-2,-10,10,-4,7,-2,6,3,7,7,6,8,-9,-2,-6,7,-1,-2,2,3,-3,8,1,5,7,-7,-9,-2,1,3,4,-5,6,-5,-3,-10,5,8,-9,3,-4,-9,-9,-3,-3,-10,-6,-2,-4,3,-7,-6,10,8,8,5,4,-8,5,3,-8,6,10,8,-7,3,-1,6,-4,3,6,7,4,-10,7,-8,8,8,-2,-4,-7,-2,-8,2,-3,-6,-4,6,8,-6,1,9,8,9,-6,-8,2,1,-10,-1,-7,1,-2,1,3,5,1,-5,-3,-8,1,-2,-8,4,6,-3,4,8,1,6,-5,9,-8,5,-1,2,9,-7,-7,-6,-8,-9,3,8,5,9,6,-7,2,-6,5,9,4,-2,8,-5,9,7,-9,7,9,-5,-3,9,-4,-10,-5,-4,6,-9,6,-9,5,-10,-10,-10,2,-6,-8,2,-2,-3,-3,3,3,-2,-5,5,-8,8,-1,-9,-4,7,1,-7,4,-9,7,6,5,8,-2,2,5,8,-8,8,-5,5,-8,1,2,-9,-4,-6,7,-9,-6,-7,-10,-8,5,10,5,-7,10,3,8,1,-10,-10,-3,-4,-1,2,9,10,8,-3,9,-3,8,1,9,7,-8,-6,8,-10,2,-2,1,-2,-6,-9,-7,-4,-10,10,-4,9,-5,-5,-5,-6,4,-8,2,4,-7,2,5,10,8,7,8,-8,-2,-10,5,-6,3,-5,-3,2,-4,-5,-10,-6,-4,2,8,-7,-2,-9,-2,-7,-8,10,3,-1,-6,-8,9,7,-7,-7,1,-7,-10,8,-1,7,-7,-9,8,-7,-6,3,9,1,10,-10,2,2,6,-4,-6,4,-7,-6,-7,-1,8,-10,-5,4,9,-6,3,-2,9,6,8,-1,-5,10,-9,-6,-7,5,-7,9,5,10,-7,-9,-10,-4,-4,-3,-9,2,-6,-7,3,8,3,10,7,7,2,-10,8,-1,8,-3,9,-7,2,-9,-5,8,4,-5,-8,3,-10,-4,-9,-3,9,4,-1,-2,-4,-9,5,7,7,-10,-6,-5,-8,-5,4,-3,-3,-2,9,-7,-4,-2,-6,-10,-10,-8,-5,-5,1,-1,-7,1,-3,-6,6,7,-2,9,-7,10,9,-6,-10,9,-10,-8,7,10,-2,-4,10,8,-10,9,-8,-5,-7,-5,-1,-10,-5,1,-10,3,5,-10,-1,-6,-9,-8,-6,-6,-3,1,5,6,-10,3,-6,-1,8,-6,2,-9,9,-10,10,9,6,7,1,-3,-8,10,7,-5,-3,-3,4,-7,-9,9,2,-3,10,-2,-1,4,5,5,5,6,-2,-4,3,1,-10,-1,2,3,-2,-5,-3,-4,2,2,-9,5,9,10,-3,-4,-3,5,1,-1,4,7,4,-6,9,4,-8,9,-2,-9,-10,-10,-10,-10,5,-3,7,6,9,10,10,6,-6,-5,-4,5,-7,-6,-10,-5,10,-3,8,-8,1,-7,-3,1,9,-8,-10,4,-8,2,7,-4,-7,-3,6,2,-1,-2,-3,4,9,-3,-6,6,-7,3,-8,-2,4,10,9,9,2,-6,4,-4,-3,4,6,-3,-10,1,-5,-5,-10,-1,6,1,-1,10,1,10,5,-5,-6,5,7,4,-9,-1,3,-10,-1,-6,9,10,1,4,-6,6,7,7,-5,6,-1,5,-8,-2,5,1,-3,-4,5,-2,-8,4,-10,-1,-6,-1,5,-3,-10,-2,-5,8,8,-4,-3,5,-7,-9,1,-1,9,6,-9,-9,-5,1,3,-8,3,-3,10,-8,-6,1,-8,-6,8,3,10,4,2,-3,-7,6,-5,-8,7,-2,-4,-2,-9,9,8,-5,-5,-4,-6,-2,8,-7,-8,-9,-1,-10,6,-7,-8,-2,-10,7,-8,10,7,-9,1,1,-2,-4,1,-10,-6,4,3,2,-3,-9,-1,-6,-3,5,-2,-3,5,7,-1,-5,-4,-1,-4,-2,-4,-1,2,-3,-2,-8,5,9,9,7,3,-5,2,-3,10,7,-6,1,4,4,-2,-10,-4,-8,5,2,-1,4,-4,-2,-4,-8,-7,-10,-3,-9,-7,-6,10,-3,-1,-4,2,8,6,-10,-10], dtype = "uint32")#candidate|1113|(1408,)|const|uint32
call_1112 = relay.TupleGetItem(func_336_call(relay.reshape(const_1113.astype('uint32'), [8, 16, 11]), relay.reshape(const_1108.astype('bool'), [2912,]), ), 3)
call_1114 = relay.TupleGetItem(func_340_call(relay.reshape(const_1113.astype('uint32'), [8, 16, 11]), relay.reshape(const_1108.astype('bool'), [2912,]), ), 3)
func_1040_call = mod.get_global_var('func_1040')
func_1044_call = mutated_mod.get_global_var('func_1044')
var_1120 = relay.var("var_1120", dtype = "int32", shape = (84, 1))#candidate|1120|(84, 1)|var|int32
var_1121 = relay.var("var_1121", dtype = "int32", shape = (672,))#candidate|1121|(672,)|var|int32
call_1119 = relay.TupleGetItem(func_1040_call(relay.reshape(var_1120.astype('int32'), [1, 7, 12]), relay.reshape(var_1121.astype('int32'), [8, 7, 12]), ), 0)
call_1122 = relay.TupleGetItem(func_1044_call(relay.reshape(var_1120.astype('int32'), [1, 7, 12]), relay.reshape(var_1121.astype('int32'), [8, 7, 12]), ), 0)
output = relay.Tuple([uop_1092,call_1106,var_1107,const_1108,call_1112,const_1113,call_1119,var_1120,var_1121,])
output2 = relay.Tuple([uop_1092,call_1109,var_1107,const_1108,call_1114,const_1113,call_1122,var_1120,var_1121,])
func_1124 = relay.Function([var_1080,var_1107,var_1120,var_1121,], output)
mod['func_1124'] = func_1124
mod = relay.transform.InferType()(mod)
mutated_mod['func_1124'] = func_1124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1124_call = mutated_mod.get_global_var('func_1124')
var_1126 = relay.var("var_1126", dtype = "float64", shape = (11, 5, 3))#candidate|1126|(11, 5, 3)|var|float64
var_1127 = relay.var("var_1127", dtype = "int8", shape = (480,))#candidate|1127|(480,)|var|int8
var_1128 = relay.var("var_1128", dtype = "int32", shape = (84, 1))#candidate|1128|(84, 1)|var|int32
var_1129 = relay.var("var_1129", dtype = "int32", shape = (672,))#candidate|1129|(672,)|var|int32
call_1125 = func_1124_call(var_1126,var_1127,var_1128,var_1129,)
output = call_1125
func_1130 = relay.Function([var_1126,var_1127,var_1128,var_1129,], output)
mutated_mod['func_1130'] = func_1130
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1306 = relay.const([[[-8.234321,0.557497,-2.195161,-8.830492,-5.107049,-3.880088,3.556169,-5.625784,3.093217,-5.169170,9.641147,9.856454,-1.118514,8.493848,1.758376],[0.064213,-3.786339,0.448673,2.712391,-6.124293,0.555729,2.474639,-7.959192,2.315086,-1.170720,-6.762980,-3.142111,3.673742,-4.621613,-8.018772],[4.066548,8.519850,5.218175,-1.551363,-3.317676,-2.749797,3.026292,8.238989,-6.483288,7.748597,-0.693464,-7.440974,5.418652,9.970910,6.851335],[5.513284,5.990457,-3.388864,9.325564,8.689193,-4.395104,3.075118,7.211829,7.534106,-4.339827,-2.068580,-2.891526,8.694273,-6.216991,2.990865],[7.096089,-3.408085,-1.862605,8.624031,5.197226,0.994013,-7.518416,1.417272,9.333000,0.597371,5.385798,2.429972,2.797313,-8.802543,7.854602],[6.166532,-2.555644,-5.009896,-3.271464,6.322586,-8.875965,0.151661,7.963738,6.763532,-3.634322,-1.030399,-7.112253,1.484605,6.759932,-2.215362],[-8.854661,2.807160,5.239353,4.633756,8.956906,-3.538324,0.138012,-2.557149,-7.176664,-7.982955,2.464324,9.745272,-3.162451,9.321425,-9.950230],[-1.913306,6.410393,3.687195,4.046662,-2.039521,7.455574,7.692033,1.314467,-3.063483,5.850050,-7.750395,7.793295,-6.480926,-2.892874,8.993952],[8.424251,9.915934,1.992211,-4.666191,7.543398,2.485384,9.440430,-0.362377,8.188879,-6.544582,1.256293,3.663223,-6.605273,-4.442532,8.892190],[7.193531,4.475855,9.798664,-1.546429,-8.234597,-7.503780,-9.059898,-2.742899,-9.890000,4.497168,-5.264670,4.706283,-1.395165,6.213946,1.837200],[-5.751712,-8.312424,9.826682,5.345874,4.535726,-0.262433,8.669874,8.113084,6.295092,6.221689,-7.789249,4.822155,6.999664,-0.477036,-6.506533],[2.524076,-7.896692,-7.175956,1.766484,2.918059,7.276329,6.555111,2.824507,-9.758128,-2.680949,6.900956,5.077643,0.080363,-5.620509,-5.334397],[5.478110,-5.895672,7.028047,0.411462,-3.658246,4.287764,-1.360950,-4.953998,4.117885,-1.723638,8.875881,-0.939581,-7.772903,2.134252,2.241222],[3.460704,-2.055530,5.247235,5.754348,-9.225407,0.425258,5.816878,-5.226737,9.484400,9.089137,-0.640167,-2.044742,9.645706,-6.236282,9.968428],[-4.198481,-4.518435,-7.704611,-5.460491,-2.066495,4.816230,-3.543977,-4.617152,7.971009,-3.155095,6.860894,7.539848,-8.431750,9.720778,2.407137]],[[-8.174749,2.105930,-2.274694,-8.857013,8.335700,-9.152626,6.893779,-3.807731,0.794150,6.310757,-0.363767,-4.592999,-5.314719,-4.613134,7.371333],[9.955495,-3.009186,-9.955346,-1.977943,9.357826,-9.591953,6.510115,6.894086,4.015558,6.953881,-8.873538,7.179234,7.343024,5.861933,4.146032],[0.575436,4.918153,-1.528194,6.166014,-0.555045,-0.412732,-5.775230,-7.649278,8.028623,-5.085734,6.291176,-4.845791,-9.863368,-1.815752,-2.796329],[-2.767165,-7.048936,1.055984,-7.542072,-3.492648,0.489437,4.190041,-4.836930,7.827670,3.160567,-2.893471,3.130217,1.720414,-2.919574,7.106767],[-8.941702,-9.170875,8.367400,9.176462,-3.128866,2.864201,-1.602647,4.567105,-7.504003,9.930739,9.432753,-6.167172,-7.052996,-0.512596,-6.934562],[3.129855,1.982156,9.657749,4.006291,-3.472474,-7.731786,-0.077753,-0.151604,2.209651,-2.547658,-8.743648,-6.767276,-9.702020,8.528370,6.624870],[4.751402,-4.712027,9.334923,6.181352,-5.349200,-4.156756,2.239389,8.357070,2.961320,4.081490,4.291259,5.062418,-9.174097,7.019627,-4.313215],[6.591301,4.643802,-6.801801,-7.752060,-1.893160,-7.491083,8.022674,2.735454,5.511522,-9.480403,-0.380819,8.154603,8.727502,-3.823880,5.698958],[-1.951846,-0.815374,-3.270291,-7.827268,-4.141240,5.389269,4.544375,9.942567,1.007412,2.803602,3.300156,-5.459395,8.092694,-9.890891,-0.434488],[-3.579991,2.517184,-3.031691,-3.939803,-6.660922,0.202561,1.708057,-2.409497,1.957642,1.325168,3.221676,3.140714,1.757743,-2.799534,-9.920857],[8.633246,4.164814,6.942796,-2.406952,-3.557280,-5.217002,-9.562194,-4.784198,-3.660180,7.697713,3.077562,-5.980954,-5.022707,4.629749,-0.662178],[2.912376,6.315797,-5.249229,-8.575758,-8.562274,1.324483,2.212971,-3.913662,-5.443499,3.007610,-5.267540,6.227151,9.489391,3.976813,-0.027126],[-7.882913,7.360209,-1.934893,-0.853333,9.376363,7.964471,-5.836291,-2.669525,-6.155664,3.589171,-9.867513,-1.530965,5.620526,3.419011,5.470218],[-5.736247,7.852499,7.202936,1.173118,4.427317,-7.624052,1.946104,2.699371,8.992028,-4.684398,4.777256,-6.855058,-1.841214,-7.239973,-1.982249],[6.347524,6.004293,6.093438,-1.196484,6.570322,9.700229,-7.188013,-7.482176,-9.807862,-3.519321,-3.530312,-3.242745,1.938098,-9.815836,-5.631086]],[[5.744224,3.287133,0.079219,1.237098,2.534648,5.157825,-5.365695,5.444288,4.003820,-3.796629,1.761075,3.976552,-4.520975,-3.891899,-1.773415],[0.379154,6.678552,5.681301,2.321759,-0.715887,4.591168,4.371326,-0.242723,-8.723525,2.316693,3.897602,7.264805,-9.355958,6.575891,9.766697],[3.186907,-5.375095,8.927759,9.771071,-3.997215,-9.770656,0.790588,-9.507969,-6.520696,8.334478,2.354973,-5.752218,-0.799514,-1.048288,-7.532004],[0.282125,3.425882,-5.922578,4.732832,1.496434,0.238550,0.950567,-4.849177,-6.286679,-1.234864,-0.968296,-8.705052,4.310174,9.972136,1.261325],[7.663838,7.583503,-6.000919,2.587046,-8.997877,1.720353,-3.072821,-6.055793,-2.754445,-3.427323,2.581198,8.006003,3.371713,-3.047287,-4.860084],[-2.564563,-8.363278,-5.589034,6.756310,4.753252,0.516829,-4.721999,9.390881,-1.599884,4.630502,1.007203,5.789391,3.718640,8.300605,4.690580],[1.497987,3.326876,7.141289,-6.391086,5.078952,-5.126332,-4.458989,1.132178,-2.460840,-1.043171,-7.796857,-5.220492,-5.802806,-4.858978,5.765838],[9.210868,-6.497010,-2.675275,6.460607,-3.699800,-8.276030,3.547041,4.322665,1.498248,-5.149949,-2.872613,8.368410,-7.357677,-1.896694,0.196402],[-2.102477,-4.674344,1.616732,-7.642279,4.219898,2.621980,-8.691087,-2.009567,8.013812,0.997556,6.902235,-8.976379,-8.361458,-8.426800,-7.025083],[-9.341750,2.906540,4.986085,1.283898,8.147998,-4.340733,1.186245,4.587927,7.179762,7.829296,-0.395710,-5.842484,5.627423,3.537391,7.039316],[5.235836,-1.716047,-8.881474,7.122215,5.420847,-4.328931,8.450104,-5.032224,1.266111,-3.023146,-7.333991,-1.252030,9.902909,7.144227,1.073950],[-0.752996,-6.065432,7.268467,-8.773025,9.658999,8.584910,-1.231268,9.996660,1.037740,-9.267050,9.964954,-1.946038,4.513265,5.960321,-1.631621],[8.834250,1.934480,2.281792,-1.181259,5.833056,-2.996000,1.181162,4.459976,0.534334,1.851076,-9.838305,1.515559,-8.470675,2.252036,7.567928],[0.040590,-2.395535,0.426897,0.452091,-1.544515,6.978800,-0.056685,6.283022,6.288555,-8.754169,-7.392983,0.438426,-2.296073,-0.961064,0.129038],[3.311808,-0.436506,5.348759,-6.831844,3.245534,5.928897,1.276651,1.039410,0.518436,6.891597,3.677754,5.767582,1.825449,8.620951,6.000632]],[[-6.850634,9.837179,-4.465416,-7.151131,8.221194,9.901728,-0.640844,-9.100052,9.052801,-8.913496,-4.272634,-9.488103,-6.683133,7.155367,2.903795],[-1.569423,5.087601,-4.479526,-7.596062,-2.009298,-8.276562,-6.538448,-3.257368,-8.085765,-0.728784,4.237389,1.159419,-6.783094,3.637534,9.268615],[-2.246232,-5.910694,5.897262,-6.856857,5.379377,5.724481,-3.576897,-6.259961,6.106034,5.852587,6.618037,-3.078459,-2.424713,-2.102288,-7.200206],[9.129016,2.592358,-5.422102,-9.372356,-8.118116,-9.996558,-7.850350,4.107861,7.763501,3.844063,5.034209,2.626878,2.644947,-0.916606,-1.280982],[3.994668,-7.885292,5.060085,6.261208,5.706308,-1.727840,-5.443843,-9.385210,5.557116,-3.703418,-5.161498,-5.063086,0.016433,-3.829298,4.979802],[-4.737278,-4.768023,-1.206377,1.035709,8.033849,8.285051,-8.125920,-3.746070,-7.865987,8.880121,3.663157,-3.167820,2.200494,4.049897,8.523768],[-0.340710,-1.676924,-3.838837,2.083565,-7.595824,-7.551912,-8.581653,9.398366,-5.369576,-0.243343,-8.277740,4.829133,4.657477,-1.383285,-8.240005],[-8.853600,5.165026,9.908106,7.433518,-9.314230,-3.781428,8.026806,0.261659,4.865429,-7.763988,7.205290,3.089358,9.667938,-9.929753,-6.283623],[-9.932926,6.669737,9.718655,8.459851,0.208624,-0.420525,9.866599,-6.085570,9.314525,-5.405641,-9.957871,-4.616596,-1.852871,-8.120466,-4.866678],[-2.261705,8.347568,-5.748407,-7.066619,7.779542,5.141677,2.827793,-1.901857,-2.112476,-2.657228,4.491453,-9.294530,-9.282207,-2.930955,5.549801],[2.206974,8.351660,-5.223544,1.017972,9.252927,-0.493996,6.598147,0.743880,-8.006146,9.958314,-9.632800,8.031082,-3.548677,-5.850120,-3.524568],[6.204987,6.177597,4.158504,7.766756,-6.639048,2.549099,9.804611,9.756164,-5.555111,-2.536351,-5.003725,6.196667,-5.609847,6.214059,-0.534928],[-4.377502,-4.564406,-6.855817,4.235986,-2.918393,-6.389988,0.456188,-9.060240,9.825340,-3.833430,-1.264401,-5.536161,-1.139078,-3.349843,6.922914],[1.722457,-4.557070,9.603891,7.360154,-3.142092,5.430617,-7.174223,4.472369,2.836648,6.174664,-7.120431,-1.408600,2.947732,6.798457,-3.704088],[-9.814582,9.056592,5.377156,2.935583,1.755619,8.664908,9.366701,7.843901,-9.563022,2.632918,-1.959566,-5.302885,-9.764918,8.367095,3.156458]]], dtype = "float32")#candidate|1306|(4, 15, 15)|const|float32
uop_1307 = relay.acosh(const_1306.astype('float32')) # shape=(4, 15, 15)
output = relay.Tuple([uop_1307,])
output2 = relay.Tuple([uop_1307,])
func_1319 = relay.Function([], output)
mod['func_1319'] = func_1319
mod = relay.transform.InferType()(mod)
output = func_1319()
func_1320 = relay.Function([], output)
mutated_mod['func_1320'] = func_1320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1319_call = mod.get_global_var('func_1319')
func_1320_call = mutated_mod.get_global_var('func_1320')
call_1446 = relay.TupleGetItem(func_1319_call(), 0)
call_1447 = relay.TupleGetItem(func_1320_call(), 0)
uop_1500 = relay.sin(call_1446.astype('float64')) # shape=(4, 15, 15)
uop_1502 = relay.sin(call_1447.astype('float64')) # shape=(4, 15, 15)
output = relay.Tuple([uop_1500,])
output2 = relay.Tuple([uop_1502,])
func_1510 = relay.Function([], output)
mod['func_1510'] = func_1510
mod = relay.transform.InferType()(mod)
output = func_1510()
func_1511 = relay.Function([], output)
mutated_mod['func_1511'] = func_1511
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1614 = relay.const([[[1,-4,-2,3],[-10,1,-1,-6],[3,3,1,-1],[6,3,-1,10],[5,-2,-1,-5],[8,-4,2,-4],[-7,-1,8,-7],[-5,10,1,8],[6,-3,5,-5],[5,-3,-3,-3]],[[6,9,5,-10],[-4,6,2,3],[4,-4,5,3],[1,6,7,-2],[-5,-8,-5,-3],[-9,-6,3,-1],[-5,-7,4,-10],[-7,7,-8,-6],[-2,-3,3,7],[5,4,-3,4]],[[-8,10,-10,-7],[7,-1,-4,9],[-3,2,8,-7],[5,2,4,7],[8,6,-6,-5],[8,1,4,8],[2,-3,-1,5],[2,3,-3,10],[6,9,10,8],[-3,1,-6,-7]],[[1,1,10,10],[-3,-8,5,-10],[-7,-4,5,6],[-10,-5,8,-7],[2,4,3,-4],[9,5,-1,5],[-3,6,3,-8],[-10,9,5,-10],[-3,-8,10,-5],[3,3,6,-3]],[[-8,-9,-2,-4],[-9,2,-9,2],[-1,-2,-2,2],[-6,9,-2,3],[1,1,-6,-8],[7,9,-4,-10],[1,8,9,-9],[2,9,10,5],[1,-7,-10,3],[4,-3,-3,5]],[[-7,7,2,10],[-4,9,-2,-7],[10,-1,-8,-8],[-6,-3,6,-5],[3,-6,10,9],[9,-9,-2,-4],[-10,-5,-9,1],[5,-6,-3,3],[-5,-9,9,10],[-5,8,5,2]],[[-7,4,-1,3],[2,-7,2,-1],[1,3,-9,7],[-2,-3,-5,2],[3,9,-4,10],[-2,1,6,-1],[3,6,-9,-7],[-6,-9,7,-4],[-9,4,5,-9],[10,-9,1,5]],[[7,5,-4,8],[3,2,7,10],[-1,9,-10,-1],[6,9,1,1],[-7,4,1,3],[7,5,3,2],[-2,10,-9,2],[-2,-5,7,2],[6,-5,-8,-2],[6,-3,-5,-5]],[[-7,-10,-5,-4],[-5,9,-8,-6],[-7,-1,9,-3],[1,4,-10,4],[3,4,8,6],[-10,7,-7,2],[6,-10,5,2],[9,5,-6,-7],[-4,-8,10,10],[-8,-7,2,9]],[[-1,6,4,5],[5,-1,8,9],[-10,6,10,9],[5,-3,5,6],[4,-5,10,-10],[-9,-4,-10,1],[-2,9,3,10],[-7,-4,8,10],[1,-8,5,-4],[10,3,4,7]]], dtype = "int64")#candidate|1614|(10, 10, 4)|const|int64
var_1615 = relay.var("var_1615", dtype = "int64", shape = (10, 10, 4))#candidate|1615|(10, 10, 4)|var|int64
bop_1616 = relay.subtract(const_1614.astype('int64'), relay.reshape(var_1615.astype('int64'), relay.shape_of(const_1614))) # shape=(10, 10, 4)
output = bop_1616
output2 = bop_1616
func_1619 = relay.Function([var_1615,], output)
mod['func_1619'] = func_1619
mod = relay.transform.InferType()(mod)
mutated_mod['func_1619'] = func_1619
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1620 = relay.var("var_1620", dtype = "int64", shape = (10, 10, 4))#candidate|1620|(10, 10, 4)|var|int64
func_1619_call = mutated_mod.get_global_var('func_1619')
call_1621 = func_1619_call(var_1620)
output = call_1621
func_1622 = relay.Function([var_1620], output)
mutated_mod['func_1622'] = func_1622
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1651 = relay.const([[[6.923653,8.981202,-2.229011,-2.710054,0.809820,4.948618,-4.488518],[-4.238550,6.357638,1.860092,-7.346774,7.351152,-0.436021,-0.957853],[-6.395366,0.278578,9.447415,-5.534643,-1.037242,-9.537198,5.642054],[8.548641,4.769973,5.602255,9.106669,0.214870,-4.074766,2.007107],[0.674359,-7.126600,8.151342,5.933005,7.436142,4.877504,2.412562],[9.873214,7.430329,-0.808910,3.727276,2.028887,-1.185085,-6.941489],[-4.892486,8.838505,-9.293644,1.880329,1.094937,-5.470613,-2.406001],[6.960745,6.469102,-7.981407,6.922394,8.824591,-5.541359,5.388610],[-2.726260,0.024957,8.596106,-4.662381,0.496473,-6.083589,1.890430],[1.530149,-8.133962,8.854988,3.950948,-3.992123,-7.761515,1.814273],[4.859604,-5.738563,6.646756,-7.995728,-7.370084,-5.238166,-6.578350]],[[7.293571,7.503984,4.985166,7.254683,2.387567,-0.609863,0.743080],[3.017703,3.362778,7.192105,-7.610004,3.815648,9.042689,-6.036466],[8.175001,-2.834260,-7.986808,8.802776,5.941688,-9.729646,-5.712797],[1.536325,3.286101,-4.816898,6.044663,-9.750481,-3.358453,-7.103461],[-1.398760,2.391714,2.985045,-7.891733,0.777106,3.543772,-6.027589],[6.869411,-0.290939,-4.481170,-1.330412,-8.116787,-1.501430,2.701598],[-3.424192,-9.820154,-0.825003,4.800951,-8.529378,7.275850,2.629136],[-2.814086,-7.002472,-7.455430,-3.350776,8.424730,-3.009865,-6.547329],[-2.223965,2.701067,2.777286,8.242903,-7.203616,5.384895,-3.640668],[-7.464266,4.468811,2.110912,7.231222,-8.687976,-9.061479,-6.070253],[6.226513,2.854055,-9.241091,1.249503,7.504854,-8.238659,2.964993]],[[-2.287053,-5.387894,4.513143,4.385485,-2.048010,3.007041,9.643508],[-4.417109,-7.474034,-3.757260,3.825723,-2.521901,2.289043,-2.700195],[4.730143,6.593468,2.360680,5.079199,-8.307379,-9.992562,3.266185],[5.744467,9.285376,-2.944981,-6.342183,-5.260096,5.686928,-5.133686],[-2.975529,-3.711445,-0.462674,3.987806,-4.732336,-7.547638,1.405660],[7.268853,-1.568226,3.389462,-6.649785,8.235534,2.677947,-8.233835],[6.337660,7.929627,2.976001,9.333356,8.949591,-9.293549,7.003084],[-1.261694,2.916278,0.263668,5.891745,4.349420,-7.370161,-7.585954],[-0.099944,8.739499,2.059977,6.091378,-9.136628,-6.989964,0.770673],[9.596895,1.137249,-7.743208,0.155882,7.583780,-7.814598,-4.779368],[8.118912,-7.248529,-9.765763,5.390754,-0.620025,-6.702424,-6.920487]]], dtype = "float64")#candidate|1651|(3, 11, 7)|const|float64
uop_1652 = relay.erf(const_1651.astype('float64')) # shape=(3, 11, 7)
bop_1658 = relay.multiply(const_1651.astype('float32'), relay.reshape(uop_1652.astype('float32'), relay.shape_of(const_1651))) # shape=(3, 11, 7)
var_1663 = relay.var("var_1663", dtype = "float32", shape = (3, 11, 7))#candidate|1663|(3, 11, 7)|var|float32
bop_1664 = relay.not_equal(bop_1658.astype('bool'), relay.reshape(var_1663.astype('bool'), relay.shape_of(bop_1658))) # shape=(3, 11, 7)
func_981_call = mod.get_global_var('func_981')
func_985_call = mutated_mod.get_global_var('func_985')
var_1670 = relay.var("var_1670", dtype = "int8", shape = (8, 60))#candidate|1670|(8, 60)|var|int8
var_1671 = relay.var("var_1671", dtype = "bool", shape = (1, 2912))#candidate|1671|(1, 2912)|var|bool
call_1669 = relay.TupleGetItem(func_981_call(relay.reshape(var_1670.astype('int8'), [2, 15, 16]), relay.reshape(var_1670.astype('int8'), [2, 15, 16]), relay.reshape(var_1671.astype('bool'), [2912,]), ), 1)
call_1672 = relay.TupleGetItem(func_985_call(relay.reshape(var_1670.astype('int8'), [2, 15, 16]), relay.reshape(var_1670.astype('int8'), [2, 15, 16]), relay.reshape(var_1671.astype('bool'), [2912,]), ), 1)
output = relay.Tuple([bop_1664,call_1669,var_1670,var_1671,])
output2 = relay.Tuple([bop_1664,call_1672,var_1670,var_1671,])
func_1684 = relay.Function([var_1663,var_1670,var_1671,], output)
mod['func_1684'] = func_1684
mod = relay.transform.InferType()(mod)
var_1685 = relay.var("var_1685", dtype = "float32", shape = (3, 11, 7))#candidate|1685|(3, 11, 7)|var|float32
var_1686 = relay.var("var_1686", dtype = "int8", shape = (8, 60))#candidate|1686|(8, 60)|var|int8
var_1687 = relay.var("var_1687", dtype = "bool", shape = (1, 2912))#candidate|1687|(1, 2912)|var|bool
output = func_1684(var_1685,var_1686,var_1687,)
func_1688 = relay.Function([var_1685,var_1686,var_1687,], output)
mutated_mod['func_1688'] = func_1688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1510_call = mod.get_global_var('func_1510')
func_1511_call = mutated_mod.get_global_var('func_1511')
call_1725 = relay.TupleGetItem(func_1510_call(), 0)
call_1726 = relay.TupleGetItem(func_1511_call(), 0)
uop_1732 = relay.cosh(call_1725.astype('float32')) # shape=(4, 15, 15)
uop_1734 = relay.cosh(call_1726.astype('float32')) # shape=(4, 15, 15)
output = relay.Tuple([uop_1732,])
output2 = relay.Tuple([uop_1734,])
func_1739 = relay.Function([], output)
mod['func_1739'] = func_1739
mod = relay.transform.InferType()(mod)
mutated_mod['func_1739'] = func_1739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1739_call = mutated_mod.get_global_var('func_1739')
call_1740 = func_1739_call()
output = call_1740
func_1741 = relay.Function([], output)
mutated_mod['func_1741'] = func_1741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1510_call = mod.get_global_var('func_1510')
func_1511_call = mutated_mod.get_global_var('func_1511')
call_1755 = relay.TupleGetItem(func_1510_call(), 0)
call_1756 = relay.TupleGetItem(func_1511_call(), 0)
output = call_1755
output2 = call_1756
func_1759 = relay.Function([], output)
mod['func_1759'] = func_1759
mod = relay.transform.InferType()(mod)
output = func_1759()
func_1760 = relay.Function([], output)
mutated_mod['func_1760'] = func_1760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1319_call = mod.get_global_var('func_1319')
func_1320_call = mutated_mod.get_global_var('func_1320')
call_1798 = relay.TupleGetItem(func_1319_call(), 0)
call_1799 = relay.TupleGetItem(func_1320_call(), 0)
output = relay.Tuple([call_1798,])
output2 = relay.Tuple([call_1799,])
func_1811 = relay.Function([], output)
mod['func_1811'] = func_1811
mod = relay.transform.InferType()(mod)
mutated_mod['func_1811'] = func_1811
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1811_call = mutated_mod.get_global_var('func_1811')
call_1812 = func_1811_call()
output = call_1812
func_1813 = relay.Function([], output)
mutated_mod['func_1813'] = func_1813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1759_call = mod.get_global_var('func_1759')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_1825 = func_1759_call()
call_1826 = func_1759_call()
func_1759_call = mod.get_global_var('func_1759')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_1838 = func_1759_call()
call_1839 = func_1759_call()
output = relay.Tuple([call_1825,call_1838,])
output2 = relay.Tuple([call_1826,call_1839,])
func_1844 = relay.Function([], output)
mod['func_1844'] = func_1844
mod = relay.transform.InferType()(mod)
output = func_1844()
func_1845 = relay.Function([], output)
mutated_mod['func_1845'] = func_1845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1811_call = mod.get_global_var('func_1811')
func_1813_call = mutated_mod.get_global_var('func_1813')
call_1852 = relay.TupleGetItem(func_1811_call(), 0)
call_1853 = relay.TupleGetItem(func_1813_call(), 0)
output = call_1852
output2 = call_1853
func_1864 = relay.Function([], output)
mod['func_1864'] = func_1864
mod = relay.transform.InferType()(mod)
output = func_1864()
func_1865 = relay.Function([], output)
mutated_mod['func_1865'] = func_1865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1811_call = mod.get_global_var('func_1811')
func_1813_call = mutated_mod.get_global_var('func_1813')
call_1885 = relay.TupleGetItem(func_1811_call(), 0)
call_1886 = relay.TupleGetItem(func_1813_call(), 0)
uop_1894 = relay.cos(call_1885.astype('float64')) # shape=(4, 15, 15)
uop_1896 = relay.cos(call_1886.astype('float64')) # shape=(4, 15, 15)
output = uop_1894
output2 = uop_1896
func_1915 = relay.Function([], output)
mod['func_1915'] = func_1915
mod = relay.transform.InferType()(mod)
output = func_1915()
func_1916 = relay.Function([], output)
mutated_mod['func_1916'] = func_1916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1844_call = mod.get_global_var('func_1844')
func_1845_call = mutated_mod.get_global_var('func_1845')
call_1965 = relay.TupleGetItem(func_1844_call(), 0)
call_1966 = relay.TupleGetItem(func_1845_call(), 0)
func_1759_call = mod.get_global_var('func_1759')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_1985 = func_1759_call()
call_1986 = func_1759_call()
output = relay.Tuple([call_1965,call_1985,])
output2 = relay.Tuple([call_1966,call_1986,])
func_1991 = relay.Function([], output)
mod['func_1991'] = func_1991
mod = relay.transform.InferType()(mod)
output = func_1991()
func_1992 = relay.Function([], output)
mutated_mod['func_1992'] = func_1992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1759_call = mod.get_global_var('func_1759')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_1998 = func_1759_call()
call_1999 = func_1759_call()
func_1759_call = mod.get_global_var('func_1759')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_2010 = func_1759_call()
call_2011 = func_1759_call()
func_593_call = mod.get_global_var('func_593')
func_596_call = mutated_mod.get_global_var('func_596')
const_2015 = relay.const([3,-2,9,1,-5,-4,5,4,2,-8,4,3,-2,-3,10,-9,-1,9,10,-7,2,-7,-1,-10,6,1,3,-1,6,4,-6,-10,3,-9,9,1,9,2,-8,4,4,3,-1,2,6,3,8,-1,5,7,7,-9,5,-8,-4,8,8,-5,6,8,3,8,-7,6,10,-7,-1,-5,6,3,6,9,-5,-6,-2,-4,6,-10,-10,6,-10,-7,7,-1,-5,-4,6,-6,-8,1,-7,-6,-7,-7,-3,-9,3,-5,-7,-5,1,-5,5,-5,4,-6,10,-5,10,-8,-2,-7,-2,-7,-9,3,-4,-4,-10,3,-4,6,-2,-3,-10,5,-7,-6,5,9,-6,5,-1,-8,-9,-8,1,-8,-4,3,-3,7,-1,8,8,9,10,-3,-4,-5,-3,7,-8,7,8,-7,8,-1,-8,-4,-8,10,8,10,-6,6,-9,-5,8,8,-4,8,-6,-3,-2,1,-2,8,4,-4,5,10,-3,-9,-7,-8,10,4,-9,-2,-4,10,2,7,-6,-6,1,2,-1,4,8,10,1,5,1,-10,-10,10,-8,10,8,-2,-10,-10,5,-8,7,2,1,8,5,-6,8,-9,-3,-10,-2,9,-7,4,4,-7,-1,-8,8,-4,-6,10,-8,-2,-7,-3,5,3,-10,5,9,6,-3,-2,-10,6,9,-2,4,-10,-4,-1,5,-2,1,1,-1,1,1,7,-4,-9,-8,1,-5,-2,-4,-8,9,7,7,-1,5,4,-7,-9,-3,-3,-9,10,7,-3,-7,1,-2,5,6,-10,9,-9,5,5,-8,9,-5,3,3,3,10,-7,2,-2,9,3,5,4,2,10,-10,-1,-9,6,-2,-3,3,-5,-3,7,-10,-2,2,7,-5,-8,-7,9,5,8,-4,-2,-1,6,-3,-8,3,9,5,-1,-6,-5,-8,-7,-10,10,5,3], dtype = "uint8")#candidate|2015|(352,)|const|uint8
var_2016 = relay.var("var_2016", dtype = "uint32", shape = (1800, 1))#candidate|2016|(1800, 1)|var|uint32
call_2014 = relay.TupleGetItem(func_593_call(relay.reshape(const_2015.astype('uint8'), [4, 11, 8]), relay.reshape(var_2016.astype('uint32'), [1800,]), ), 3)
call_2017 = relay.TupleGetItem(func_596_call(relay.reshape(const_2015.astype('uint8'), [4, 11, 8]), relay.reshape(var_2016.astype('uint32'), [1800,]), ), 3)
func_76_call = mod.get_global_var('func_76')
func_79_call = mutated_mod.get_global_var('func_79')
call_2018 = func_76_call(relay.reshape(call_2014.astype('bool'), [13, 16, 14]))
call_2019 = func_76_call(relay.reshape(call_2014.astype('bool'), [13, 16, 14]))
output = relay.Tuple([call_1998,call_2010,call_2014,const_2015,var_2016,call_2018,])
output2 = relay.Tuple([call_1999,call_2011,call_2017,const_2015,var_2016,call_2019,])
func_2020 = relay.Function([var_2016,], output)
mod['func_2020'] = func_2020
mod = relay.transform.InferType()(mod)
var_2021 = relay.var("var_2021", dtype = "uint32", shape = (1800, 1))#candidate|2021|(1800, 1)|var|uint32
output = func_2020(var_2021)
func_2022 = relay.Function([var_2021], output)
mutated_mod['func_2022'] = func_2022
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2028 = relay.var("var_2028", dtype = "float64", shape = (7, 8, 1))#candidate|2028|(7, 8, 1)|var|float64
uop_2029 = relay.atanh(var_2028.astype('float64')) # shape=(7, 8, 1)
var_2050 = relay.var("var_2050", dtype = "float64", shape = (7, 8, 8))#candidate|2050|(7, 8, 8)|var|float64
bop_2051 = relay.maximum(uop_2029.astype('float32'), var_2050.astype('float32')) # shape=(7, 8, 8)
func_1040_call = mod.get_global_var('func_1040')
func_1044_call = mutated_mod.get_global_var('func_1044')
const_2057 = relay.const([-8,-8,-3,7,-4,-4,-9,7,5,-9,9,6,-7,9,6,2,8,-9,8,-6,10,9,-2,-7,-8,-5,10,5,2,3,-3,-4,-7,-3,-8,-7,-8,-10,-1,-9,-3,3,8,3,3,9,-1,6,-7,2,7,6,6,-10,-4,5,5,-3,8,-6,9,7,-8,9,2,-1,-1,-6,4,3,5,5,5,-7,-3,-4,-8,-4,3,-2,-7,4,1,-4], dtype = "int32")#candidate|2057|(84,)|const|int32
var_2058 = relay.var("var_2058", dtype = "int32", shape = (672,))#candidate|2058|(672,)|var|int32
call_2056 = relay.TupleGetItem(func_1040_call(relay.reshape(const_2057.astype('int32'), [1, 7, 12]), relay.reshape(var_2058.astype('int32'), [8, 7, 12]), ), 0)
call_2059 = relay.TupleGetItem(func_1044_call(relay.reshape(const_2057.astype('int32'), [1, 7, 12]), relay.reshape(var_2058.astype('int32'), [8, 7, 12]), ), 0)
func_471_call = mod.get_global_var('func_471')
func_475_call = mutated_mod.get_global_var('func_475')
var_2072 = relay.var("var_2072", dtype = "float32", shape = (48,))#candidate|2072|(48,)|var|float32
var_2073 = relay.var("var_2073", dtype = "bool", shape = (2912,))#candidate|2073|(2912,)|var|bool
call_2071 = relay.TupleGetItem(func_471_call(relay.reshape(var_2072.astype('float32'), [1, 3, 16]), relay.reshape(var_2073.astype('bool'), [104, 28]), ), 1)
call_2074 = relay.TupleGetItem(func_475_call(relay.reshape(var_2072.astype('float32'), [1, 3, 16]), relay.reshape(var_2073.astype('bool'), [104, 28]), ), 1)
bop_2083 = relay.divide(uop_2029.astype('float64'), var_2050.astype('float64')) # shape=(7, 8, 8)
func_551_call = mod.get_global_var('func_551')
func_554_call = mutated_mod.get_global_var('func_554')
var_2089 = relay.var("var_2089", dtype = "uint32", shape = (1800,))#candidate|2089|(1800,)|var|uint32
call_2088 = relay.TupleGetItem(func_551_call(relay.reshape(var_2089.astype('uint32'), [10, 15, 12]), relay.reshape(var_2089.astype('uint32'), [10, 15, 12]), ), 0)
call_2090 = relay.TupleGetItem(func_554_call(relay.reshape(var_2089.astype('uint32'), [10, 15, 12]), relay.reshape(var_2089.astype('uint32'), [10, 15, 12]), ), 0)
func_1040_call = mod.get_global_var('func_1040')
func_1044_call = mutated_mod.get_global_var('func_1044')
call_2092 = relay.TupleGetItem(func_1040_call(relay.reshape(const_2057.astype('int32'), [1, 7, 12]), relay.reshape(var_2058.astype('int32'), [8, 7, 12]), ), 0)
call_2093 = relay.TupleGetItem(func_1044_call(relay.reshape(const_2057.astype('int32'), [1, 7, 12]), relay.reshape(var_2058.astype('int32'), [8, 7, 12]), ), 0)
bop_2098 = relay.maximum(uop_2029.astype('uint32'), const_2057.astype('uint32')) # shape=(7, 8, 84)
uop_2121 = relay.acos(var_2050.astype('float32')) # shape=(7, 8, 8)
output = relay.Tuple([bop_2051,call_2056,var_2058,call_2071,var_2072,var_2073,bop_2083,call_2088,var_2089,call_2092,bop_2098,uop_2121,])
output2 = relay.Tuple([bop_2051,call_2059,var_2058,call_2074,var_2072,var_2073,bop_2083,call_2090,var_2089,call_2093,bop_2098,uop_2121,])
func_2125 = relay.Function([var_2028,var_2050,var_2058,var_2072,var_2073,var_2089,], output)
mod['func_2125'] = func_2125
mod = relay.transform.InferType()(mod)
mutated_mod['func_2125'] = func_2125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2125_call = mutated_mod.get_global_var('func_2125')
var_2127 = relay.var("var_2127", dtype = "float64", shape = (7, 8, 1))#candidate|2127|(7, 8, 1)|var|float64
var_2128 = relay.var("var_2128", dtype = "float64", shape = (7, 8, 8))#candidate|2128|(7, 8, 8)|var|float64
var_2129 = relay.var("var_2129", dtype = "int32", shape = (672,))#candidate|2129|(672,)|var|int32
var_2130 = relay.var("var_2130", dtype = "float32", shape = (48,))#candidate|2130|(48,)|var|float32
var_2131 = relay.var("var_2131", dtype = "bool", shape = (2912,))#candidate|2131|(2912,)|var|bool
var_2132 = relay.var("var_2132", dtype = "uint32", shape = (1800,))#candidate|2132|(1800,)|var|uint32
call_2126 = func_2125_call(var_2127,var_2128,var_2129,var_2130,var_2131,var_2132,)
output = call_2126
func_2133 = relay.Function([var_2127,var_2128,var_2129,var_2130,var_2131,var_2132,], output)
mutated_mod['func_2133'] = func_2133
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2166 = relay.var("var_2166", dtype = "float64", shape = (1, 7, 12))#candidate|2166|(1, 7, 12)|var|float64
uop_2167 = relay.tan(var_2166.astype('float64')) # shape=(1, 7, 12)
bop_2171 = relay.floor_divide(uop_2167.astype('float64'), relay.reshape(var_2166.astype('float64'), relay.shape_of(uop_2167))) # shape=(1, 7, 12)
output = bop_2171
output2 = bop_2171
func_2185 = relay.Function([var_2166,], output)
mod['func_2185'] = func_2185
mod = relay.transform.InferType()(mod)
mutated_mod['func_2185'] = func_2185
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2186 = relay.var("var_2186", dtype = "float64", shape = (1, 7, 12))#candidate|2186|(1, 7, 12)|var|float64
func_2185_call = mutated_mod.get_global_var('func_2185')
call_2187 = func_2185_call(var_2186)
output = call_2187
func_2188 = relay.Function([var_2186], output)
mutated_mod['func_2188'] = func_2188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1991_call = mod.get_global_var('func_1991')
func_1992_call = mutated_mod.get_global_var('func_1992')
call_2215 = relay.TupleGetItem(func_1991_call(), 0)
call_2216 = relay.TupleGetItem(func_1992_call(), 0)
output = call_2215
output2 = call_2216
func_2265 = relay.Function([], output)
mod['func_2265'] = func_2265
mod = relay.transform.InferType()(mod)
output = func_2265()
func_2266 = relay.Function([], output)
mutated_mod['func_2266'] = func_2266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1864_call = mod.get_global_var('func_1864')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_2267 = func_1864_call()
call_2268 = func_1864_call()
output = call_2267
output2 = call_2268
func_2278 = relay.Function([], output)
mod['func_2278'] = func_2278
mod = relay.transform.InferType()(mod)
mutated_mod['func_2278'] = func_2278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2278_call = mutated_mod.get_global_var('func_2278')
call_2279 = func_2278_call()
output = call_2279
func_2280 = relay.Function([], output)
mutated_mod['func_2280'] = func_2280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2265_call = mod.get_global_var('func_2265')
func_2266_call = mutated_mod.get_global_var('func_2266')
call_2298 = func_2265_call()
call_2299 = func_2265_call()
output = relay.Tuple([call_2298,])
output2 = relay.Tuple([call_2299,])
func_2300 = relay.Function([], output)
mod['func_2300'] = func_2300
mod = relay.transform.InferType()(mod)
output = func_2300()
func_2301 = relay.Function([], output)
mutated_mod['func_2301'] = func_2301
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2316 = relay.var("var_2316", dtype = "float32", shape = (10, 7, 5))#candidate|2316|(10, 7, 5)|var|float32
uop_2317 = relay.erf(var_2316.astype('float32')) # shape=(10, 7, 5)
func_1040_call = mod.get_global_var('func_1040')
func_1044_call = mutated_mod.get_global_var('func_1044')
var_2331 = relay.var("var_2331", dtype = "int32", shape = (84,))#candidate|2331|(84,)|var|int32
const_2332 = relay.const([-3,-10,-9,2,1,7,7,-1,-8,-1,-10,-1,-5,6,-3,-8,9,9,-6,-3,6,-8,7,1,4,-4,-7,3,-8,-3,-7,-7,8,6,8,10,-9,-6,8,2,7,6,-10,8,-7,-9,2,3,-4,4,8,6,2,4,9,-2,1,-2,9,9,1,-2,-3,-2,2,1,-2,9,-8,4,10,-4,5,2,-8,-10,8,-3,-7,-8,-3,-10,5,-8,2,-2,9,-5,-4,8,7,-10,-2,-6,7,7,-2,-4,-6,-1,6,1,1,-10,5,6,8,7,-8,6,-8,5,7,8,-4,2,-2,5,-10,-8,-3,-7,10,-10,10,4,-6,-7,-10,8,5,4,-6,-1,-4,-1,5,7,-5,-6,2,10,-10,-4,-3,-4,4,-6,-7,-7,9,-7,8,-2,10,6,9,-1,-7,3,9,8,5,4,-2,2,-8,6,2,1,-7,5,4,-8,3,1,-9,5,-5,-8,9,8,9,-5,3,5,4,-7,10,-9,5,4,1,7,-8,2,-5,7,6,6,-8,9,-3,-10,10,-5,-1,10,-2,-5,4,-10,-10,4,6,5,-3,6,1,-10,-5,-9,-7,6,7,-10,3,-1,-6,8,9,8,10,-7,-9,-3,3,1,-10,-7,-2,-10,-8,7,10,-8,3,-10,-9,3,5,4,-9,-7,-4,7,-5,3,2,7,-7,10,10,-2,-8,-7,-4,-2,-6,1,-5,-9,7,-4,-2,-10,8,1,-1,-9,2,3,-6,9,4,-5,-8,7,-6,2,-4,9,4,9,4,4,3,2,-2,5,-10,-3,3,-4,3,-7,10,-8,-5,-10,5,7,-3,9,-1,-1,5,9,-8,-8,-7,-7,-10,-1,-3,6,-7,8,-3,7,-3,2,4,5,4,-2,-8,-10,-5,-7,-4,-6,5,10,5,1,6,6,-7,-2,6,-4,5,5,4,6,-5,8,-8,-2,-8,1,-8,-5,-7,8,3,10,-3,-7,6,-5,-8,5,-3,-1,9,8,8,-2,2,-10,1,2,6,-1,5,-5,10,10,-6,6,-4,1,-8,1,-5,5,-3,-10,-8,-1,-8,5,6,-1,8,-8,-4,6,-5,1,8,-8,5,-9,-10,6,-7,-5,-8,-7,-8,1,-5,-3,2,10,2,-2,-7,-9,-1,4,10,3,8,6,-5,5,2,10,-3,-5,-10,9,-7,-4,-7,-4,-6,5,-7,7,8,3,1,3,6,7,6,-3,8,9,4,10,-2,-3,6,2,5,3,9,-1,5,-10,6,3,-1,-9,10,4,-4,3,-10,-5,2,-2,-5,5,3,-4,9,4,2,4,1,-3,8,9,3,-4,4,-6,-10,-1,-6,-3,2,6,9,7,-1,-6,-8,-8,9,-8,9,3,4,-2,9,-7,3,9,5,-1,-6,-5,4,-7,-5,-7,8,-4,4,-5,3,7,7,-7,10,1,7,-10,9,-5,2,-9,-3,-5,10,1,-1,-9,-4,3,6,-10,9,-5,9,5,5,-4,-8,5,-6,-3,-5,-7,1,-3,-3,-10,-2,5,9,5,-5,-10,5,-2,2,-9,-8,-5,8,5,-10,-8,-2,-6,-2,-4,-7,9,-2,6,-4,2,-3,2,7,-5,-4,1,-3,-8,-7,9,7,-9,-8,-4,10,-6,-2,-4,-8,4,-9,8,4,-8,-8,-7,6,-7,-9,-7,-4,-9,3,-3,-2,3,-4,5,8,-8,-10,-5,-9,1,1,4,-2,10,-8,-6,-2,2,-3,3,-10,-10,-4,-9,9,-10,7,-6,8,-4,-10,5,-1,-7,5,8], dtype = "int32")#candidate|2332|(672,)|const|int32
call_2330 = relay.TupleGetItem(func_1040_call(relay.reshape(var_2331.astype('int32'), [1, 7, 12]), relay.reshape(const_2332.astype('int32'), [8, 7, 12]), ), 0)
call_2333 = relay.TupleGetItem(func_1044_call(relay.reshape(var_2331.astype('int32'), [1, 7, 12]), relay.reshape(const_2332.astype('int32'), [8, 7, 12]), ), 0)
output = relay.Tuple([uop_2317,call_2330,var_2331,const_2332,])
output2 = relay.Tuple([uop_2317,call_2333,var_2331,const_2332,])
func_2346 = relay.Function([var_2316,var_2331,], output)
mod['func_2346'] = func_2346
mod = relay.transform.InferType()(mod)
mutated_mod['func_2346'] = func_2346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2346_call = mutated_mod.get_global_var('func_2346')
var_2348 = relay.var("var_2348", dtype = "float32", shape = (10, 7, 5))#candidate|2348|(10, 7, 5)|var|float32
var_2349 = relay.var("var_2349", dtype = "int32", shape = (84,))#candidate|2349|(84,)|var|int32
call_2347 = func_2346_call(var_2348,var_2349,)
output = call_2347
func_2350 = relay.Function([var_2348,var_2349,], output)
mutated_mod['func_2350'] = func_2350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2265_call = mod.get_global_var('func_2265')
func_2266_call = mutated_mod.get_global_var('func_2266')
call_2360 = func_2265_call()
call_2361 = func_2265_call()
output = relay.Tuple([call_2360,])
output2 = relay.Tuple([call_2361,])
func_2376 = relay.Function([], output)
mod['func_2376'] = func_2376
mod = relay.transform.InferType()(mod)
mutated_mod['func_2376'] = func_2376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2376_call = mutated_mod.get_global_var('func_2376')
call_2377 = func_2376_call()
output = call_2377
func_2378 = relay.Function([], output)
mutated_mod['func_2378'] = func_2378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1915_call = mod.get_global_var('func_1915')
func_1916_call = mutated_mod.get_global_var('func_1916')
call_2395 = func_1915_call()
call_2396 = func_1915_call()
output = relay.Tuple([call_2395,])
output2 = relay.Tuple([call_2396,])
func_2400 = relay.Function([], output)
mod['func_2400'] = func_2400
mod = relay.transform.InferType()(mod)
mutated_mod['func_2400'] = func_2400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2400_call = mutated_mod.get_global_var('func_2400')
call_2401 = func_2400_call()
output = call_2401
func_2402 = relay.Function([], output)
mutated_mod['func_2402'] = func_2402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1811_call = mod.get_global_var('func_1811')
func_1813_call = mutated_mod.get_global_var('func_1813')
call_2406 = relay.TupleGetItem(func_1811_call(), 0)
call_2407 = relay.TupleGetItem(func_1813_call(), 0)
func_1991_call = mod.get_global_var('func_1991')
func_1992_call = mutated_mod.get_global_var('func_1992')
call_2411 = relay.TupleGetItem(func_1991_call(), 1)
call_2412 = relay.TupleGetItem(func_1992_call(), 1)
func_2278_call = mod.get_global_var('func_2278')
func_2280_call = mutated_mod.get_global_var('func_2280')
call_2416 = func_2278_call()
call_2417 = func_2278_call()
func_2400_call = mod.get_global_var('func_2400')
func_2402_call = mutated_mod.get_global_var('func_2402')
call_2424 = relay.TupleGetItem(func_2400_call(), 0)
call_2425 = relay.TupleGetItem(func_2402_call(), 0)
func_2376_call = mod.get_global_var('func_2376')
func_2378_call = mutated_mod.get_global_var('func_2378')
call_2432 = relay.TupleGetItem(func_2376_call(), 0)
call_2433 = relay.TupleGetItem(func_2378_call(), 0)
output = relay.Tuple([call_2406,call_2411,call_2416,call_2424,call_2432,])
output2 = relay.Tuple([call_2407,call_2412,call_2417,call_2425,call_2433,])
func_2446 = relay.Function([], output)
mod['func_2446'] = func_2446
mod = relay.transform.InferType()(mod)
mutated_mod['func_2446'] = func_2446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2446_call = mutated_mod.get_global_var('func_2446')
call_2447 = func_2446_call()
output = call_2447
func_2448 = relay.Function([], output)
mutated_mod['func_2448'] = func_2448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2376_call = mod.get_global_var('func_2376')
func_2378_call = mutated_mod.get_global_var('func_2378')
call_2510 = relay.TupleGetItem(func_2376_call(), 0)
call_2511 = relay.TupleGetItem(func_2378_call(), 0)
output = call_2510
output2 = call_2511
func_2512 = relay.Function([], output)
mod['func_2512'] = func_2512
mod = relay.transform.InferType()(mod)
mutated_mod['func_2512'] = func_2512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2512_call = mutated_mod.get_global_var('func_2512')
call_2513 = func_2512_call()
output = call_2513
func_2514 = relay.Function([], output)
mutated_mod['func_2514'] = func_2514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2512_call = mod.get_global_var('func_2512')
func_2514_call = mutated_mod.get_global_var('func_2514')
call_2517 = func_2512_call()
call_2518 = func_2512_call()
func_1915_call = mod.get_global_var('func_1915')
func_1916_call = mutated_mod.get_global_var('func_1916')
call_2523 = func_1915_call()
call_2524 = func_1915_call()
func_1759_call = mod.get_global_var('func_1759')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_2528 = func_1759_call()
call_2529 = func_1759_call()
output = relay.Tuple([call_2517,call_2523,call_2528,])
output2 = relay.Tuple([call_2518,call_2524,call_2529,])
func_2534 = relay.Function([], output)
mod['func_2534'] = func_2534
mod = relay.transform.InferType()(mod)
output = func_2534()
func_2535 = relay.Function([], output)
mutated_mod['func_2535'] = func_2535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1811_call = mod.get_global_var('func_1811')
func_1813_call = mutated_mod.get_global_var('func_1813')
call_2542 = relay.TupleGetItem(func_1811_call(), 0)
call_2543 = relay.TupleGetItem(func_1813_call(), 0)
uop_2558 = relay.asin(call_2542.astype('float32')) # shape=(4, 15, 15)
uop_2560 = relay.asin(call_2543.astype('float32')) # shape=(4, 15, 15)
output = relay.Tuple([uop_2558,])
output2 = relay.Tuple([uop_2560,])
func_2576 = relay.Function([], output)
mod['func_2576'] = func_2576
mod = relay.transform.InferType()(mod)
output = func_2576()
func_2577 = relay.Function([], output)
mutated_mod['func_2577'] = func_2577
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2589 = relay.const([[-0.280573,-2.958855],[7.469422,9.328324],[3.417267,2.616560],[2.543202,-6.975087],[-5.554998,8.558509],[9.874855,7.645108],[1.719300,-7.758161],[2.641208,9.605485]], dtype = "float32")#candidate|2589|(8, 2)|const|float32
uop_2590 = relay.exp(const_2589.astype('float32')) # shape=(8, 2)
func_2376_call = mod.get_global_var('func_2376')
func_2378_call = mutated_mod.get_global_var('func_2378')
call_2633 = relay.TupleGetItem(func_2376_call(), 0)
call_2634 = relay.TupleGetItem(func_2378_call(), 0)
output = relay.Tuple([uop_2590,call_2633,])
output2 = relay.Tuple([uop_2590,call_2634,])
func_2636 = relay.Function([], output)
mod['func_2636'] = func_2636
mod = relay.transform.InferType()(mod)
output = func_2636()
func_2637 = relay.Function([], output)
mutated_mod['func_2637'] = func_2637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1844_call = mod.get_global_var('func_1844')
func_1845_call = mutated_mod.get_global_var('func_1845')
call_2650 = relay.TupleGetItem(func_1844_call(), 0)
call_2651 = relay.TupleGetItem(func_1845_call(), 0)
const_2675 = relay.const([[[7.349064,7.571261,-5.882900,7.873177,7.036737,7.802719,7.009027,5.217247,-8.652812,5.003852,6.590229,8.847150,-1.003156,-2.152093,6.667758],[2.242535,-5.399084,7.776630,1.400398,6.524840,-8.522171,-7.795991,-2.961782,9.359453,2.702079,-9.615940,7.679310,-0.041069,-5.395576,4.663276],[-0.654293,-1.386590,3.769397,6.638431,-2.524100,2.329474,-3.546982,0.507166,4.295725,9.182163,3.024302,1.636071,7.612565,-3.237710,-5.304265],[-1.134501,2.912653,-0.974086,-4.820575,7.923298,-4.157527,-3.206497,4.778709,3.541501,-5.360930,7.303512,1.023339,-9.390340,-8.504056,-0.467287],[-1.176398,8.093922,3.689481,3.706319,-8.479633,6.696945,8.743663,1.803265,9.345350,-9.906425,6.019261,3.068109,-1.110242,-2.352451,-6.308700],[-4.864491,8.031528,-8.422621,1.730510,-0.276247,3.236833,-9.576654,8.756328,1.245651,2.443171,-3.472238,7.199104,0.748979,-0.833553,0.138024],[-3.156918,9.882531,4.524596,-1.003859,4.129798,-3.457828,-1.269914,-7.720141,-4.469010,-8.772287,1.635049,0.994448,-4.424066,-5.498277,-2.331926],[-8.076805,2.473744,-9.135147,8.944071,1.644076,8.815791,4.011801,2.675232,-8.031745,4.184794,0.241857,6.298818,-1.203369,2.546195,-2.156703],[-3.946817,-0.878729,4.449943,-3.668666,8.834308,0.432395,-6.430951,4.292566,-9.310385,2.120000,-2.232336,-2.412840,7.212684,-5.099323,-8.115223],[-3.303166,9.383629,-8.784717,7.398735,6.922152,8.188017,-3.948380,-6.102789,3.447198,0.320999,-2.451794,3.799544,8.901739,2.281240,7.771612],[9.457574,-0.267396,-0.637900,8.552413,-7.323429,-9.613992,0.094688,4.179310,-4.301986,6.391714,1.142030,-5.906774,-2.199805,-7.727249,5.606361],[1.447500,5.916861,2.157573,2.258305,-9.704739,7.153359,4.755432,8.230742,-4.478693,8.076004,5.832148,-4.137985,5.191288,6.980391,-1.745227],[8.751847,5.587296,-0.247925,-4.350686,3.318550,8.272659,0.543298,-9.982457,1.263651,6.903810,-9.336241,7.424294,-8.438939,6.059140,-0.985599],[-1.927834,-5.627734,0.030712,-9.706279,-5.048354,-9.152561,-8.179323,-0.140084,-1.297209,-3.406552,-9.407928,-9.068125,0.485399,-2.962480,-3.010607],[-1.552460,-4.334089,3.632673,0.271399,4.559509,4.853713,6.242997,2.748661,-0.349212,8.134532,0.319432,4.772745,-3.837941,-8.755051,-9.634653]],[[6.495428,2.743105,9.181700,0.739773,-1.164688,-0.858141,-6.274130,-9.230973,5.157414,5.656792,4.140613,-5.642610,-4.808398,2.668369,4.881665],[-4.570423,-2.499817,-2.250077,-9.327088,7.336030,-1.251460,-8.668935,7.458641,-4.570164,-6.061514,-5.973350,7.992180,-9.024183,5.827644,-3.301172],[2.650432,9.014897,9.587932,4.206245,-4.190913,-7.128554,-2.824348,9.460420,7.139022,-7.909040,-3.911963,8.690279,6.884152,0.686275,7.693672],[2.516589,-3.614854,8.272275,-5.137283,5.324456,0.927990,6.490407,4.596303,6.263090,3.657128,-6.198505,-6.496097,5.793284,9.905636,-8.113717],[-8.776313,-2.436444,7.102224,-9.998145,-7.501247,-5.954542,-3.760657,-6.041256,-9.373835,-6.094686,0.014312,3.530967,3.383976,-0.809608,-0.699825],[7.399301,-3.891767,7.047564,3.294497,-0.987933,-1.883017,5.685580,-8.484545,-9.940893,-3.130599,-1.505737,5.679130,4.599303,-8.121015,7.547515],[1.054297,-3.760607,-1.698904,0.999898,5.895119,-8.902185,-6.991389,-8.993232,5.104858,3.594639,-5.164164,4.199541,-3.233261,-9.107216,-3.015414],[1.795979,-3.256984,-6.976262,6.638123,1.989416,0.386708,-5.760143,2.982619,-5.458074,2.203551,-3.581237,-1.732064,6.572789,9.013345,5.833051],[-8.205714,7.683832,-9.795238,6.387516,4.818629,4.061457,-7.517456,-2.530561,-5.484106,-9.279381,-8.201224,0.433865,8.199810,2.330010,-4.013699],[-3.972849,1.633895,-2.373469,6.541426,-5.368923,-6.750594,4.325032,9.052432,-3.642994,0.121757,-8.290970,-0.554199,-2.744833,-2.657797,-0.694699],[-7.966374,8.072442,-3.812165,-1.752491,-8.016462,-3.952765,-9.069839,1.956222,1.918359,8.419382,9.491570,-6.907272,-6.912014,0.435819,3.884514],[5.282059,-4.803865,2.756392,-1.260330,9.590953,-4.294801,7.594694,1.891220,9.398534,9.289021,3.437094,-5.705720,-8.516138,-1.642841,1.027670],[3.455838,-0.575835,-1.277313,-5.812189,2.826152,1.255814,7.511531,-3.782979,1.862282,0.533481,-1.519631,6.912708,-1.708972,3.936397,5.820875],[-9.213829,-2.362558,2.988082,8.868407,0.651047,2.327083,-9.124506,-4.035789,4.592696,-2.539356,-4.402957,-8.821459,0.060369,0.258838,4.873075],[-6.359870,4.211418,-0.438599,5.157254,-0.407625,-5.715759,4.932252,-9.295245,5.802904,2.231275,-2.666071,4.905230,-6.950297,3.947794,0.388944]],[[-7.831423,9.696221,-3.614347,-0.787301,8.768545,8.487048,-8.965766,-3.097094,-8.076825,8.753967,-4.726776,2.380782,-9.524473,-9.450627,4.674298],[-2.758008,4.445402,0.422180,-9.993651,0.157693,-4.659649,6.249071,9.423355,7.581351,-6.443237,-1.111818,-7.033918,-6.031472,9.215242,-9.424194],[-6.823547,-0.961657,-8.006774,-3.787304,-3.633819,-6.813990,-2.210839,3.903063,-3.703440,1.826810,3.908754,3.510409,7.474963,-0.012792,-9.493364],[5.349998,-8.911110,0.127317,7.495957,9.417428,7.398514,-5.965313,1.688572,-4.611298,-6.046076,-6.728973,9.212865,3.492288,4.963537,8.296896],[-7.071381,7.034564,-3.245291,-3.425831,-8.499601,3.017026,7.460576,5.581225,-1.231302,-6.390870,7.293094,-1.661509,-9.489322,0.977093,-6.061083],[-6.717642,1.053273,3.853937,-3.951329,8.042730,6.112109,-4.647010,-3.982904,4.015515,7.370908,0.309461,4.901260,8.369448,5.131084,2.289786],[6.781921,-0.362992,2.459845,5.715563,9.023588,-0.071286,1.875262,-7.661506,-5.400473,-6.436783,5.118054,-5.736200,-5.813684,7.952214,-7.269057],[3.076550,-1.948881,-0.362503,6.666637,8.598451,-1.804165,6.154881,-6.786715,5.587730,3.400792,9.513059,8.109022,0.734702,9.840661,7.949514],[-8.741844,-3.094911,9.240417,-2.341966,-4.910538,0.106036,-8.259798,-4.846977,-8.720242,2.819664,-3.550817,3.210464,9.465294,5.350814,4.463335],[-6.050222,9.753812,-8.826692,-5.271970,4.715717,-3.390037,9.008736,8.459636,5.961073,-4.395381,5.916655,6.214968,-5.834867,-8.350628,-4.218860],[6.385176,0.838788,2.620884,2.563069,-1.020513,-8.309869,8.372531,7.896400,1.488377,5.323407,-4.765923,-2.202797,8.608871,-3.461932,-7.245341],[8.035403,9.356342,-0.476031,-8.673393,-6.747313,-3.355763,8.879181,1.553262,-7.047212,2.470473,-2.592772,9.259631,-1.210837,9.159110,-4.272394],[8.793184,1.420881,-0.384101,4.889251,9.171785,9.297523,-2.814431,-4.723449,-6.507084,-1.814948,-3.840112,7.953224,-2.631496,-9.686911,-2.052351],[3.363710,-7.821102,-6.846150,9.981516,4.272413,-8.784913,-3.070347,6.481924,-3.079952,-1.957236,2.241820,4.909357,-0.291287,-2.509967,0.802053],[7.496930,-9.507081,-1.291933,-8.783915,-9.007740,-0.905703,-5.493573,8.332189,9.900651,1.373033,0.254822,-6.147733,9.280937,-8.684465,1.269729]],[[-1.698833,-0.716359,-4.562038,-2.337901,-7.093774,-5.401341,6.076379,-8.104398,-3.640179,-3.733161,7.338777,1.535750,-6.483755,-2.698737,-1.011869],[-8.888671,-9.130908,-6.404793,8.321546,3.080970,5.664928,2.165130,-6.646292,-8.061733,5.705848,2.309801,-4.927712,7.877122,3.238200,2.495114],[0.022624,2.010997,-8.736105,7.496400,-0.300227,-5.094599,-5.442639,-6.942168,5.154721,-3.643080,4.453041,4.384511,-2.504671,-1.318543,-1.845801],[9.260811,1.003992,4.884209,-5.491293,-9.865988,0.213989,9.152931,-9.610255,-4.243509,-6.473047,-3.417242,-4.636508,3.527415,-8.977251,2.782548],[3.302372,8.375135,8.517280,-1.909221,2.877964,-2.584413,9.326132,-5.911780,1.677520,2.155978,0.467667,3.074694,0.680702,-4.645842,-5.907016],[-8.089371,3.618953,-0.501407,-7.157323,-6.686145,4.359998,-4.975989,-9.168347,-7.939140,-1.874161,3.929907,-5.562296,4.374250,2.318449,2.896547],[0.829837,8.083564,5.863944,6.867237,9.587224,9.155671,-4.307565,6.962385,0.681874,-9.308026,-8.765627,7.227295,-1.248545,-3.609371,5.445630],[6.054532,-1.577103,2.599510,4.010177,3.257751,-4.325285,4.959563,7.626655,-0.185252,0.505642,-5.349304,-8.313048,-9.358799,-8.110307,3.088676],[-5.696369,7.986316,9.371310,7.376708,8.462048,7.470778,2.122083,8.004452,-2.016938,7.995436,-7.113067,4.387650,-4.894734,-3.509644,-3.392743],[-9.741802,-3.483731,3.838096,-0.864521,-3.594843,-2.625222,9.176859,8.961722,-1.915545,-1.725427,1.855835,9.829522,-9.218299,-2.375416,-1.959552],[-3.916859,2.726680,-5.120701,-7.279369,0.355142,3.515386,2.739272,-8.049490,1.418470,-2.000055,-2.375327,-3.886957,-9.804804,7.903079,7.248861],[0.719162,-6.552521,4.148708,-1.944562,9.647835,-3.146990,2.258459,-6.115590,-5.325607,-0.456825,2.759656,-8.171815,-7.712960,-4.720964,9.497277],[1.546323,0.115906,-4.310857,0.366765,2.772437,-6.368413,3.737976,2.773710,4.563528,3.623156,-6.108738,0.319654,-4.661826,3.029583,6.882939],[3.692337,1.772401,4.564867,6.508688,-1.571883,9.934547,-6.921569,-4.068229,-9.817425,-0.067753,5.938975,6.326105,0.212910,-7.815464,-0.682209],[-8.259787,5.476519,7.018106,3.173999,7.296475,2.236137,-2.178838,6.431772,1.791046,1.753734,0.047540,-7.096593,3.099191,-3.216608,-6.249600]]], dtype = "float64")#candidate|2675|(4, 15, 15)|const|float64
bop_2676 = relay.maximum(call_2650.astype('float64'), relay.reshape(const_2675.astype('float64'), relay.shape_of(call_2650))) # shape=(4, 15, 15)
bop_2679 = relay.maximum(call_2651.astype('float64'), relay.reshape(const_2675.astype('float64'), relay.shape_of(call_2651))) # shape=(4, 15, 15)
output = relay.Tuple([bop_2676,])
output2 = relay.Tuple([bop_2679,])
func_2680 = relay.Function([], output)
mod['func_2680'] = func_2680
mod = relay.transform.InferType()(mod)
mutated_mod['func_2680'] = func_2680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2680_call = mutated_mod.get_global_var('func_2680')
call_2681 = func_2680_call()
output = call_2681
func_2682 = relay.Function([], output)
mutated_mod['func_2682'] = func_2682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2512_call = mod.get_global_var('func_2512')
func_2514_call = mutated_mod.get_global_var('func_2514')
call_2691 = func_2512_call()
call_2692 = func_2512_call()
output = call_2691
output2 = call_2692
func_2701 = relay.Function([], output)
mod['func_2701'] = func_2701
mod = relay.transform.InferType()(mod)
mutated_mod['func_2701'] = func_2701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2701_call = mutated_mod.get_global_var('func_2701')
call_2702 = func_2701_call()
output = call_2702
func_2703 = relay.Function([], output)
mutated_mod['func_2703'] = func_2703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2512_call = mod.get_global_var('func_2512')
func_2514_call = mutated_mod.get_global_var('func_2514')
call_2704 = func_2512_call()
call_2705 = func_2512_call()
output = call_2704
output2 = call_2705
func_2724 = relay.Function([], output)
mod['func_2724'] = func_2724
mod = relay.transform.InferType()(mod)
output = func_2724()
func_2725 = relay.Function([], output)
mutated_mod['func_2725'] = func_2725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1811_call = mod.get_global_var('func_1811')
func_1813_call = mutated_mod.get_global_var('func_1813')
call_2740 = relay.TupleGetItem(func_1811_call(), 0)
call_2741 = relay.TupleGetItem(func_1813_call(), 0)
func_1759_call = mod.get_global_var('func_1759')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_2768 = func_1759_call()
call_2769 = func_1759_call()
bop_2771 = relay.floor_mod(call_2740.astype('float64'), relay.reshape(call_2768.astype('float64'), relay.shape_of(call_2740))) # shape=(4, 15, 15)
bop_2774 = relay.floor_mod(call_2741.astype('float64'), relay.reshape(call_2769.astype('float64'), relay.shape_of(call_2741))) # shape=(4, 15, 15)
func_2300_call = mod.get_global_var('func_2300')
func_2301_call = mutated_mod.get_global_var('func_2301')
call_2776 = relay.TupleGetItem(func_2300_call(), 0)
call_2777 = relay.TupleGetItem(func_2301_call(), 0)
output = relay.Tuple([bop_2771,call_2776,])
output2 = relay.Tuple([bop_2774,call_2777,])
func_2783 = relay.Function([], output)
mod['func_2783'] = func_2783
mod = relay.transform.InferType()(mod)
output = func_2783()
func_2784 = relay.Function([], output)
mutated_mod['func_2784'] = func_2784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1759_call = mod.get_global_var('func_1759')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_2806 = func_1759_call()
call_2807 = func_1759_call()
output = call_2806
output2 = call_2807
func_2817 = relay.Function([], output)
mod['func_2817'] = func_2817
mod = relay.transform.InferType()(mod)
output = func_2817()
func_2818 = relay.Function([], output)
mutated_mod['func_2818'] = func_2818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2446_call = mod.get_global_var('func_2446')
func_2448_call = mutated_mod.get_global_var('func_2448')
call_2832 = relay.TupleGetItem(func_2446_call(), 3)
call_2833 = relay.TupleGetItem(func_2448_call(), 3)
uop_2835 = relay.atanh(call_2832.astype('float32')) # shape=(4, 15, 15)
uop_2837 = relay.atanh(call_2833.astype('float32')) # shape=(4, 15, 15)
output = relay.Tuple([uop_2835,])
output2 = relay.Tuple([uop_2837,])
func_2849 = relay.Function([], output)
mod['func_2849'] = func_2849
mod = relay.transform.InferType()(mod)
output = func_2849()
func_2850 = relay.Function([], output)
mutated_mod['func_2850'] = func_2850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1739_call = mod.get_global_var('func_1739')
func_1741_call = mutated_mod.get_global_var('func_1741')
call_2915 = relay.TupleGetItem(func_1739_call(), 0)
call_2916 = relay.TupleGetItem(func_1741_call(), 0)
func_1684_call = mod.get_global_var('func_1684')
func_1688_call = mutated_mod.get_global_var('func_1688')
const_2918 = relay.const([5.446097,-8.677670,9.876358,8.556344,2.137717,7.415179,-1.844415,-9.178275,3.645446,-3.291384,-5.758168,0.081582,2.608307,8.831195,2.315809,-6.115456,-0.907882,6.702568,-3.662130,-3.457451,4.112711,-8.999038,-1.444756,1.541053,-7.648958,8.487670,1.012467,-5.125912,2.253804,3.660338,-2.690479,1.463903,-6.572867,-6.055555,6.419645,-8.742243,-4.905069,-6.270124,1.048451,-7.133934,9.913074,-4.876358,1.853674,8.701058,0.465523,0.673197,8.532325,-0.475924,6.124282,-6.143678,8.990913,-2.027085,1.285769,-4.411335,-3.039499,-7.466046,6.850657,-7.186419,0.675439,0.233963,-6.757398,0.669888,7.603584,1.991242,-5.916558,8.330198,3.512104,-7.555362,-2.008414,3.266596,5.397947,-7.321057,7.644483,6.065460,2.187615,3.787866,-7.699329,8.269990,-7.429232,-0.180129,-9.202472,-8.070645,5.809987,-3.339925,-8.103907,-2.258115,-4.557174,-9.717867,9.767203,-0.908781,-7.521438,-8.430528,-5.574437,-8.728624,6.481148,-1.242530,-0.008615,4.823899,4.870527,4.017721,2.697501,6.384350,-7.972774,5.807446,-3.003128,-9.408703,0.598099,4.285935,-6.178114,-8.952317,-7.987483,2.894484,-9.011121,2.135639,8.720372,2.360882,-3.122359,-6.165177,-7.760085,7.391497,8.064928,4.495998,-0.597204,7.801213,-3.849724,-4.324689,-8.901017,8.797826,-6.051501,-1.801731,9.338831,9.158956,-5.757426,-8.752890,7.514871,6.926860,-5.028016,-3.122625,9.827527,8.377646,1.738939,8.016847,-3.627731,-5.984137,2.687691,-7.275012,-0.787768,-8.744504,0.885386,3.786639,-3.659827,1.320333,8.066000,-6.539794,1.083685,-0.179926,2.830270,-9.175540,-6.750389,9.213760,1.910915,-3.111334,0.025586,3.227456,-0.853856,8.921419,2.868090,2.199276,-5.209544,-7.879363,7.221154,3.030152,-9.413500,-5.906935,-8.895520,-3.445241,2.354310,-1.513326,1.308174,8.507855,-7.576815,5.723320,-1.437583,8.565134,-2.967128,-2.591546,-4.972858,-5.823806,-5.909042,-5.435971,-4.199733,-3.150110,9.734420,-2.345130,-2.542324,-5.223877,0.634771,0.737259,-2.322239,-3.854194,-9.448875,0.202093,-4.837813,3.937447,-8.582934,-6.264321,-2.996271,0.193143,3.797594,-7.420897,8.143918,-5.381089,-9.417375,-7.010816,-2.192756,5.878959,-0.974968,-8.419751,7.976174,9.519565,8.285608,-5.183905,-1.337313,9.268476,-7.712371,-7.370072,8.864047,-7.385280,-3.019463,-4.068742,3.723027], dtype = "float32")#candidate|2918|(231,)|const|float32
const_2919 = relay.const([[-5,-10,-2,-3,3,4,5,2,-7,-9,-2,-3],[-9,10,4,-9,-10,9,-5,-5,-6,-2,6,-3],[8,5,-4,-1,-3,2,8,-8,2,2,-4,8],[5,-2,-3,-5,-4,2,-9,10,-5,1,6,4],[1,-9,-5,6,6,-3,1,-1,2,-5,-8,5],[9,-7,-9,7,8,-6,3,-5,10,-2,-9,9],[8,-2,-1,10,-5,9,7,-6,3,10,-4,7],[-2,-8,-3,10,-3,8,9,5,4,-10,1,-7],[-7,-10,-1,-8,7,-6,5,2,8,3,7,-5],[-4,-5,10,9,1,2,-8,7,-8,-8,8,-2],[-9,6,-5,-10,-6,5,-6,-7,6,1,2,1],[-10,3,-8,-4,2,-4,3,-5,8,-8,4,3],[5,-6,-1,-6,-8,9,-6,5,-7,4,-5,-10],[8,-9,-3,4,4,6,-9,-6,-3,-4,-10,-6],[8,-6,10,-5,-5,-3,-7,-8,-9,8,-9,6],[1,-9,-9,-7,-7,-1,10,5,10,-4,7,8],[10,-5,-10,9,2,-2,6,-9,2,-8,-8,8],[3,7,-5,7,2,-4,-4,4,4,-7,7,1],[-8,2,6,-3,3,8,-4,-3,6,9,-10,-5],[10,3,8,7,-7,-1,10,-1,-4,10,3,-4],[-9,-8,-7,3,5,-5,4,-10,-2,1,4,4],[2,-6,5,5,-5,3,7,9,6,6,5,-8],[-10,-8,2,2,4,-8,-10,-5,7,6,5,-6],[7,-8,2,1,8,6,-1,-3,-8,8,-5,4],[-10,-6,6,-8,5,-7,-4,7,-10,-2,-1,8],[10,-1,8,7,-8,4,2,-6,10,4,-4,7],[-3,-4,6,8,-7,-10,-4,2,-9,-3,8,10],[5,-1,-4,-2,9,-3,-6,-10,-8,8,9,-4],[-6,-1,-10,-4,4,3,-4,-5,9,-8,9,-1],[-10,10,1,-10,-5,-3,10,8,-3,-4,-8,-1],[-6,-5,9,-3,5,10,7,2,9,-5,-5,6],[7,-6,-6,-1,6,-9,-2,-5,6,-2,5,5],[3,4,-6,-5,-8,-8,-10,1,7,-2,-4,5],[-2,5,2,9,1,-3,-6,1,-1,-2,-8,-8],[5,-3,7,-1,6,4,5,1,-1,-4,-5,2],[-4,7,-7,8,-7,3,10,2,-9,1,-2,-1],[-9,9,-1,-9,5,-6,3,6,-4,1,-2,-7],[-9,-4,-5,5,1,-7,7,7,2,-6,-7,4],[-9,7,-7,-2,-5,1,-3,-3,2,-9,5,-3],[-1,-1,-9,-2,-9,-2,5,7,2,1,4,-2]], dtype = "int8")#candidate|2919|(40, 12)|const|int8
const_2920 = relay.const([[True,True,False,False,False,False,True,True,False,False,False,True,True,True,False,False,False,True,False,False,False,False,True,False,False,True,True,True,False,False,True,True,False,False,True,False,False,False,True,False,True,True,False,False,False,False,False,False,True,False,True,False,False,False,False,False,True,False,True,True,False,True,False,False,True,False,False,True,False,True,True,True,False,True,True,True,False,True,True,True,True,False,True,False,False,False,False,False,False,False,True,False,True,False,True,False,False,True,True,False,True,False,False,True,False,True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,True,False,True,False,False,False,False,False,False,True,True,True,True,True,False,True,False,True,True,True,True,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,False,False,True,False,True,False,True,True,True,True,False,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,True,True,True,False,True,True,False,False,True,False,False,False,True,True,False,True,True,False,True,False,False,False,True,True,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,False,True,True,False,False,False,False,False,True,True,True,True,True,False,False,False,True,True,False,True,False,False,False,True,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,False,False,True,True,True,True,False,True,True,True,True,False,True,True,False,True,False,False,True,False,False,True,True,False,True,True,False,True,False,True,True,False,True,False,True,False,False,True,True,True,False,True,True,False,False,True,True,False,True,False,True,True,False,False,True,True,False,False,False,False,True,True,False,True,True,True,True,True,True,True,False,True,False,True,True,False,True,False,True,False,True,False,False,True,False,True,False,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,False,False,False,False,True,True,False,False,True,True,False,True,False,False,True,False,True,False,False,True,True,True,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,False,True,True,True,True,False,False,True,True,False,False,False,True,False,True,False,False,True,False,False,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,False,False,False,False,True,False,True,False,True,True,False,False,False,False,True,False,True,False,False,True,False,False,True,False,False,False,True,False,True,True,False,True,False,True,False,True,True,True,True,False,False,True,False,False,True,False,False,True,False,True,False,False,True,True,False,False,True,True,False,False,True,False,False,True,True,False,False,False,True,False,True,False,True,True,False,True,True,True,False,True,False,False,True,True,True,False,True,False,True,True,False,False,False,False,True,True,False,False,False,False,False,True,False,True,False,False,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,False,True,False,True,True,False,True,True,True,False,False,True,True,True,True,False,False,False,True,False,False,False,False,True,False,True,False,True,True,True,True,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,False,False,False,True,False,False,True,False,True,True,False,True,False,True,False,False,False,False,True,True,False,True,False,False,False,False,True,True,False,False,False,False,False,False,True,True,True,False,True,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,True,True,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,True,True,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False,False,False,True,True,True,False,False,False,False,True,True,False,True,False],[False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,True,False,True,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,True,False,True,False,True,False,False,False,True,False,False,False,True,False,False,True,False,False,True,True,True,False,False,True,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,False,True,False,False,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,False,False,False,True,False,False,False,False,True,True,True,True,False,False,False,True,False,True,False,False,True,True,True,False,False,True,False,True,False,False,False,False,False,False,True,False,False,True,False,False,False,True,True,False,True,True,False,True,True,False,False,False,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False,True,True,False,True,False,True,True,False,True,False,False,False,True,True,False,True,False,False,True,False,False,True,False,True,True,True,True,True,False,True,True,True,True,True,True,True,True,False,True,False,False,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,True,False,True,True,True,True,False,False,False,True,True,True,True,True,True,False,True,False,False,False,True,True,True,False,False,True,True,True,True,False,True,False,False,False,True,True,True,True,False,False,True,True,True,False,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,True,True,False,True,True,True,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,False,False,False,False,True,False,False,True,True,False,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,True,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,True,False,False,True,False,True,False,False,True,False,False,False,False,True,False,True,False,False,True,True,False,True,False,True,True,False,False,False,False,False,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,True,True,False,False,False,True,False,True,True,True,False,True,False,True,True,False,False,True,False,True,True,False,True,False,True,True,False,False,False,False,False,False,True,False,False,True,False,False,False,True,False,False,True,False,True,False,False,True,True,False,False,True,False,False,True,True,True,True,True,True,True,True,True,False,False,True,True,False,False,True,True,False,False,False,False,True,True,False,True,False,False,True,True,False,True,True,False,False,False,True,False,False,True,True,False,True,True,False,True,True,True,False,True,True,True,True,True,False,True,False,False,True,True,False,True,True,True,True,True,True,True,True,True,False,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,False,True,True,False,False,False,True,False,False,False,True,True,False,True,False,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False,False,True,True,False,True,False,False,False,False,False,True,True,False,True,False,False,True,False,True,True,False,False,False,False,False,True,False,False,True,False,True,False,True,False,False,True,False,False,True,False,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,True,False,True,False,False,False,False,False,True,False,True,True,True,False,False,False,True,True,True,False,True,False,True,False,True,False,False,False,False,False,True,True,False,False,False,True,True,False,True,False,True,False,True,False,False,True,False,True,True,True,False,False,True,True,False,False,True,False,False,False,False,True,True,True,False,True,False,True,False,True,True,True,True,False,True,True,False,True,True,True,False,True,True,True,False,True,False,True,False,False,True,False,False,True,True,False],[False,True,True,False,False,False,True,True,False,False,True,False,True,False,True,True,True,False,True,True,False,True,False,False,True,False,False,True,True,False,True,True,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,True,True,True,True,False,True,False,False,False,False,True,True,True,False,True,True,False,True,True,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,False,True,False,False,True,False,False,False,True,False,False,True,True,True,False,False,False,True,False,True,True,False,True,True,True,True,False,True,False,True,False,False,False,False,True,True,False,True,True,False,True,False,True,True,True,True,True,True,False,True,True,True,True,False,False,True,True,True,False,True,False,True,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,False,True,False,False,False,True,True,False,False,False,False,True,True,True,True,False,True,True,True,False,False,True,True,False,True,True,True,False,False,False,False,False,True,False,False,True,False,False,False,False,False,False,True,True,True,False,True,True,True,True,True,True,False,False,True,False,True,False,False,True,True,True,False,False,True,False,False,True,False,False,True,True,False,False,False,True,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,True,True,True,False,False,False,False,False,False,False,True,True,False,False,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,False,True,True,True,True,True,False,False,False,False,True,False,True,True,False,True,False,True,False,True,True,False,False,False,False,False,True,False,False,False,False,False,True,True,False,False,False,False,False,True,False,True,True,True,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,False,True,True,False,False,True,False,False,True,False,False,False,True,True,True,False,False,False,True,False,True,False,False,False,True,False,False,False,False,True,True,False,False,True,False,False,False,True,False,True,True,False,False,False,False,True,True,False,False,False,False,True,True,False,True,False,False,False,True,False,True,False,False,False,True,True,False,True,False,True,True,True,True,True,False,True,False,True,True,False,True,False,True,False,False,True,True,True,True,False,True,False,False,False,False,False,True,True,True,True,False,False,False,True,True,False,True,False,True,False,False,True,False,False,True,True,True,False,False,False,False,True,False,True,True,True,True,False,False,False,True,False,True,False,True,False,False,False,False,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,False,False,False,True,True,False,False,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,False,False,True,True,True,False,False,True,True,False,True,False,True,False,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,True,True,False,True,False,True,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,False,True,False,False,True,False,True,True,True,True,True,True,False,True,False,False,False,False,False,False,False,True,False,True,True,False,True,False,True,False,False,True,True,False,False,False,False,True,True,False,True,False,True,True,False,True,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,False],[True,True,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False,False,False,False,False,False,True,False,False,True,False,True,True,False,True,False,True,False,True,False,False,False,False,True,True,False,True,True,True,False,True,True,False,True,False,True,True,True,True,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,True,True,True,False,False,False,False,False,False,False,True,False,True,True,True,False,False,False,True,False,True,True,True,False,False,False,True,False,False,False,False,True,True,True,True,True,False,True,False,False,False,True,False,True,False,False,True,False,False,False,True,True,True,False,True,True,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,False,False,False,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,False,False,True,False,False,True,False,True,True,True,False,True,True,False,True,False,False,False,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,False,False,False,True,False,True,False,True,True,True,False,True,False,True,True,False,False,True,True,False,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,True,False,True,False,True,True,False,False,True,False,False,True,True,False,False,False,False,False,True,False,False,True,True,True,True,False,False,False,False,True,True,True,True,True,True,False,False,True,True,True,True,True,True,True,True,True,True,False,False,False,False,False,True,True,True,True,True,False,True,False,True,False,True,False,True,True,False,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False,False,False,False,True,True,True,True,False,True,False,False,True,False,False,False,True,False,False,False,True,False,True,False,True,True,False,True,True,False,False,True,False,False,True,True,True,True,True,True,False,True,True,True,False,True,True,True,True,False,True,True,False,False,True,False,True,True,True,False,True,True,False,True,True,True,False,False,False,True,True,True,True,True,False,True,False,False,False,False,False,True,True,False,False,False,False,True,True,False,False,False,True,False,True,True,True,True,True,False,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,False,True,False,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,False,False,True,False,True,False,True,False,False,True,False,False,True,True,True,True,True,False,False,True,False,False,True,False,True,False,True,True,False,True,True,False,True,False,False,False,False,False,False,True,True,False,True,False,True,False,True,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,True,False,True,False,False,False,False,False,True,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,True,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,True,False,False,False,False,True,True,False,True,True,False,True,False,False,True,True,False,True,True,True,True,True,True,True,True,False,True,True,True,False,True,True,False,False,True,True,True,False,True,False,True,True,True,True,True,False,False,True,False,True,False,True,False,False,True,True,False,False,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,True,True,False,False,False,False,True,False,False,True,False,False,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,True,True,False,True,True,True,True,False,True,True,False,True]], dtype = "bool")#candidate|2920|(4, 728)|const|bool
call_2917 = relay.TupleGetItem(func_1684_call(relay.reshape(const_2918.astype('float32'), [3, 11, 7]), relay.reshape(const_2919.astype('int8'), [8, 60]), relay.reshape(const_2920.astype('bool'), [1, 2912]), ), 3)
call_2921 = relay.TupleGetItem(func_1688_call(relay.reshape(const_2918.astype('float32'), [3, 11, 7]), relay.reshape(const_2919.astype('int8'), [8, 60]), relay.reshape(const_2920.astype('bool'), [1, 2912]), ), 3)
output = relay.Tuple([call_2915,call_2917,const_2918,const_2919,const_2920,])
output2 = relay.Tuple([call_2916,call_2921,const_2918,const_2919,const_2920,])
func_2927 = relay.Function([], output)
mod['func_2927'] = func_2927
mod = relay.transform.InferType()(mod)
output = func_2927()
func_2928 = relay.Function([], output)
mutated_mod['func_2928'] = func_2928
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2929 = relay.var("var_2929", dtype = "float32", shape = ())#candidate|2929|()|var|float32
const_2930 = relay.const([[[-7.988316,7.795661,-9.362720,-7.734499,-2.406335,9.031288,4.162038,-7.827550,-9.444992,-5.170796,2.603180,0.367624],[-6.261368,2.708080,0.994891,-4.750134,-1.233186,1.960075,-1.606967,0.925768,-3.363372,3.586960,-3.176895,0.835659]],[[4.656093,8.882608,-3.540289,-2.662567,-7.881100,-9.949119,-7.489121,2.240718,-6.043274,5.233022,3.790859,8.553366],[-5.035494,6.962251,-0.011965,2.371258,-1.280034,8.418131,1.704666,3.564152,8.621228,6.802345,2.469394,-5.506197]],[[8.221559,-9.578820,-4.780586,-9.206795,-1.268709,0.058651,-5.176300,2.720782,-8.271294,-9.154957,-3.090158,1.766156],[6.619896,6.681581,-2.961222,-8.122210,7.352635,-4.092613,-6.276396,-0.509580,-1.134476,9.830387,-3.551258,5.070285]],[[8.934863,-6.599812,4.217348,5.710879,8.155939,7.675201,7.217627,9.137095,-8.884151,-9.296075,9.724248,-5.468202],[9.994595,-6.671309,-9.841152,-7.305560,4.667351,8.748972,-0.407784,5.472862,0.142564,2.035025,-2.419998,0.186137]],[[-3.304950,3.520731,8.051858,1.231990,-6.775001,-8.394427,0.985430,-6.680461,-1.688277,-8.462552,1.982778,-3.824267],[-6.848302,4.017047,-2.047849,-4.887824,-1.527743,-4.710013,9.716906,-3.966334,-5.332594,-2.564380,8.439199,-4.553948]],[[-0.529104,2.535467,4.158578,-3.910883,0.914937,-0.848149,-2.761824,9.145104,2.379528,-4.518030,5.272647,-9.131042],[-5.807696,-7.860423,4.763385,6.854771,7.382738,1.633169,-7.900105,-6.440304,5.760397,6.495074,0.191661,2.380926]],[[5.742137,5.301081,-4.187855,-2.712208,-3.613743,2.914566,5.083372,3.354876,2.489544,2.378456,-7.359008,8.275121],[9.499467,-7.124423,2.668022,0.262557,4.092104,-0.863482,-6.056888,-3.584921,3.030433,-0.561777,-9.186737,6.126142]],[[8.308515,8.839997,-0.806387,9.679043,-0.527473,7.292605,9.606744,-6.933714,1.222340,9.667201,4.870014,3.969529],[4.563316,0.894573,9.737500,9.012522,-7.362027,5.668122,3.993920,-0.698515,-6.526134,-2.057941,-6.455466,-6.411282]],[[1.596748,8.050468,-5.829715,1.212146,-2.427117,5.538756,7.113808,-4.757049,-0.288257,-5.625594,1.616307,4.306655],[-5.507138,6.646463,-8.046222,5.626995,5.020498,-3.441050,5.724490,7.364810,-7.986720,1.066513,5.054757,2.042188]]], dtype = "float32")#candidate|2930|(9, 2, 12)|const|float32
bop_2931 = relay.greater_equal(var_2929.astype('bool'), const_2930.astype('bool')) # shape=(9, 2, 12)
output = bop_2931
output2 = bop_2931
func_2936 = relay.Function([var_2929,], output)
mod['func_2936'] = func_2936
mod = relay.transform.InferType()(mod)
mutated_mod['func_2936'] = func_2936
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2937 = relay.var("var_2937", dtype = "float32", shape = ())#candidate|2937|()|var|float32
func_2936_call = mutated_mod.get_global_var('func_2936')
call_2938 = func_2936_call(var_2937)
output = call_2938
func_2939 = relay.Function([var_2937], output)
mutated_mod['func_2939'] = func_2939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2265_call = mod.get_global_var('func_2265')
func_2266_call = mutated_mod.get_global_var('func_2266')
call_2975 = func_2265_call()
call_2976 = func_2265_call()
output = call_2975
output2 = call_2976
func_2986 = relay.Function([], output)
mod['func_2986'] = func_2986
mod = relay.transform.InferType()(mod)
mutated_mod['func_2986'] = func_2986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2986_call = mutated_mod.get_global_var('func_2986')
call_2987 = func_2986_call()
output = call_2987
func_2988 = relay.Function([], output)
mutated_mod['func_2988'] = func_2988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1915_call = mod.get_global_var('func_1915')
func_1916_call = mutated_mod.get_global_var('func_1916')
call_2998 = func_1915_call()
call_2999 = func_1915_call()
func_2936_call = mod.get_global_var('func_2936')
func_2939_call = mutated_mod.get_global_var('func_2939')
const_3039 = relay.const(-9.840327, dtype = "float32")#candidate|3039|()|const|float32
call_3038 = func_2936_call(relay.reshape(const_3039.astype('float32'), []))
call_3040 = func_2936_call(relay.reshape(const_3039.astype('float32'), []))
output = relay.Tuple([call_2998,call_3038,const_3039,])
output2 = relay.Tuple([call_2999,call_3040,const_3039,])
func_3042 = relay.Function([], output)
mod['func_3042'] = func_3042
mod = relay.transform.InferType()(mod)
mutated_mod['func_3042'] = func_3042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3042_call = mutated_mod.get_global_var('func_3042')
call_3043 = func_3042_call()
output = call_3043
func_3044 = relay.Function([], output)
mutated_mod['func_3044'] = func_3044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1739_call = mod.get_global_var('func_1739')
func_1741_call = mutated_mod.get_global_var('func_1741')
call_3063 = relay.TupleGetItem(func_1739_call(), 0)
call_3064 = relay.TupleGetItem(func_1741_call(), 0)
func_1124_call = mod.get_global_var('func_1124')
func_1130_call = mutated_mod.get_global_var('func_1130')
var_3072 = relay.var("var_3072", dtype = "float64", shape = (165,))#candidate|3072|(165,)|var|float64
const_3073 = relay.const([-3,5,4,4,-3,-7,1,6,6,-4,-10,-5,-6,1,8,-8,-3,-10,5,5,1,10,10,3,10,10,10,2,-6,9,1,2,2,-2,-6,-8,9,-2,6,6,-3,-5,2,1,10,-9,-1,6,-2,4,-5,8,-10,4,-4,-9,-7,-1,2,4,-6,-5,-5,-2,-1,-9,-7,-2,-5,-3,9,7,-6,4,4,8,-4,-5,-5,-7,3,3,-3,9,3,9,3,9,-6,-5,-4,10,-7,-8,2,-9,3,7,6,6,-7,3,-2,-7,-9,9,-7,-1,6,7,5,4,-7,-6,8,-6,6,3,4,-6,-4,6,6,6,-7,9,-8,-1,-6,1,10,7,7,-4,3,5,7,-9,-1,6,-5,-1,9,-9,1,-9,7,7,-9,8,2,-9,5,3,-10,-3,5,-1,5,1,2,-9,7,5,-8,8,-6,-1,3,-8,-5,2,-4,4,5,-7,5,-5,1,-8,1,-1,1,8,5,10,7,-10,7,10,9,-6,-3,-7,-1,5,9,8,5,-5,-2,-10,7,9,2,-5,-7,7,3,6,1,5,5,-1,1,-3,-2,-3,-1,-2,-10,-7,-9,-8,-10,-6,4,-10,-9,3,6,-5,7,7,8,4,-10,6,-5,2,9,-6,-1,3,-7,10,-10,-4,-2,-8,4,-10,-1,4,5,1,5,-6,-6,-6,3,8,2,-2,-7,-7,-2,-7,-7,9,6,3,-9,-8,8,-10,2,4,-2,-10,-9,-1,-6,-4,-7,5,6,5,-7,-10,8,5,8,6,8,-10,-5,-9,-7,-3,5,2,-6,-7,-1,-7,9,-1,-3,-10,4,-9,-10,1,-1,-4,2,10,-2,-4,-7,3,5,4,10,-1,3,3,-10,1,-9,-10,2,3,-8,-10,-10,-3,-5,-2,-1,9,-5,-7,9,6,6,2,-7,-3,-2,2,-4,-6,1,3,-1,4,-7,10,-1,-5,-2,5,4,6,1,-7,-2,5,2,-5,-4,-8,-2,-8,-5,-9,2,8,-2,-9,4,-1,2,10,-5,7,-6,10,-3,8,-1,-5,-1,-6,-9,7,4,2,3,8,-8,7,9,-1,-8,-2,-6,-2,2,-9,7,-6,3,7,-1,3,-1,5,-10,4,-5,-6,3,-9,8,-8,5,7,4,-1,-10,-8,5,-1,-8,-2,9,-4,-6,9,-3,10,-5,-6,-1,-5,1,2,-5,-2,7,-7,-10,1,4,-1,-1,4,9,2,-7,3,-10,-6,7,9,-2,10,-7,-9,5,1,4,-9,-7,5,9,4], dtype = "int8")#candidate|3073|(480,)|const|int8
var_3074 = relay.var("var_3074", dtype = "int32", shape = (84,))#candidate|3074|(84,)|var|int32
var_3075 = relay.var("var_3075", dtype = "int32", shape = (1, 672))#candidate|3075|(1, 672)|var|int32
call_3071 = relay.TupleGetItem(func_1124_call(relay.reshape(var_3072.astype('float64'), [11, 5, 3]), relay.reshape(const_3073.astype('int8'), [480,]), relay.reshape(var_3074.astype('int32'), [84, 1]), relay.reshape(var_3075.astype('int32'), [672,]), ), 6)
call_3076 = relay.TupleGetItem(func_1130_call(relay.reshape(var_3072.astype('float64'), [11, 5, 3]), relay.reshape(const_3073.astype('int8'), [480,]), relay.reshape(var_3074.astype('int32'), [84, 1]), relay.reshape(var_3075.astype('int32'), [672,]), ), 6)
func_1619_call = mod.get_global_var('func_1619')
func_1622_call = mutated_mod.get_global_var('func_1622')
const_3085 = relay.const([-4,2,-9,-3,-5,8,7,9,1,9,9,7,1,-8,-4,-10,-4,-8,-9,9,3,-9,-5,10,-6,5,2,-3,9,10,2,2,4,-1,5,7,9,6,4,-10,-6,-8,-7,1,-2,-1,-1,-10,-5,8,-1,7,10,-4,9,7,-8,-4,-3,5,6,-10,9,1,-3,3,3,3,-3,-8,-10,-10,9,5,8,9,-6,-10,9,8,-10,5,10,7,-7,-10,9,7,-3,-9,-4,7,-7,4,10,-9,2,-4,-4,-8,5,9,-5,9,1,-10,-6,7,-6,9,-1,-4,2,5,-10,-8,10,-6,-4,-6,-5,-1,5,-4,7,5,-4,2,9,-4,2,-4,9,-9,5,7,-2,-10,-6,-6,-10,2,-1,3,-2,1,-9,6,2,-1,9,-8,-8,-5,-5,-7,3,-10,-4,6,-10,-7,9,8,-9,2,-9,-8,-9,1,-6,-8,10,3,10,9,6,10,-1,1,-7,7,-1,5,8,5,-6,4,10,-1,7,-2,-6,-10,-1,7,4,-6,-9,-7,6,-2,5,-10,1,7,1,-5,-4,-6,-6,4,8,-6,-10,-3,-7,1,-9,8,4,2,-7,-6,1,-7,-6,-10,-9,-3,-1,7,1,1,3,-2,7,6,-2,-6,-4,-2,1,7,8,3,6,7,-10,-9,-8,-3,6,10,10,1,-6,-6,-4,-1,5,-4,-3,-8,9,-7,-10,-1,-10,6,-6,5,3,1,6,-2,5,2,4,1,9,2,10,8,6,-1,-3,6,-10,3,-10,-7,-10,-3,10,10,3,9,-7,3,-2,-8,1,-3,1,-6,-3,-4,-3,9,-10,-3,3,8,10,5,-6,-9,5,9,-9,6,10,-5,8,6,-5,1,-10,9,-10,2,-7,6,-6,-9,2,7,5,4,-9,1,7,1,-3,-7,-3,1,-3,-4,-4,2,-6,9,-4,-5,3,-7,10,-10,-6,-5,8,-1,-3,-8,7,4,-10,7,5,-8,-7,-9,-3,-9,-5,-2,-8,-2,9,1,-1,-9,5,-6,7,-9,1,1,-6,-6,3,-6,10,-6,-9,5,10,-2], dtype = "int64")#candidate|3085|(400,)|const|int64
call_3084 = func_1619_call(relay.reshape(const_3085.astype('int64'), [10, 10, 4]))
call_3086 = func_1619_call(relay.reshape(const_3085.astype('int64'), [10, 10, 4]))
output = relay.Tuple([call_3063,call_3071,var_3072,const_3073,var_3074,var_3075,call_3084,const_3085,])
output2 = relay.Tuple([call_3064,call_3076,var_3072,const_3073,var_3074,var_3075,call_3086,const_3085,])
func_3087 = relay.Function([var_3072,var_3074,var_3075,], output)
mod['func_3087'] = func_3087
mod = relay.transform.InferType()(mod)
mutated_mod['func_3087'] = func_3087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3087_call = mutated_mod.get_global_var('func_3087')
var_3089 = relay.var("var_3089", dtype = "float64", shape = (165,))#candidate|3089|(165,)|var|float64
var_3090 = relay.var("var_3090", dtype = "int32", shape = (84,))#candidate|3090|(84,)|var|int32
var_3091 = relay.var("var_3091", dtype = "int32", shape = (1, 672))#candidate|3091|(1, 672)|var|int32
call_3088 = func_3087_call(var_3089,var_3090,var_3091,)
output = call_3088
func_3092 = relay.Function([var_3089,var_3090,var_3091,], output)
mutated_mod['func_3092'] = func_3092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2636_call = mod.get_global_var('func_2636')
func_2637_call = mutated_mod.get_global_var('func_2637')
call_3134 = relay.TupleGetItem(func_2636_call(), 1)
call_3135 = relay.TupleGetItem(func_2637_call(), 1)
func_2125_call = mod.get_global_var('func_2125')
func_2133_call = mutated_mod.get_global_var('func_2133')
var_3138 = relay.var("var_3138", dtype = "float64", shape = (56,))#candidate|3138|(56,)|var|float64
var_3139 = relay.var("var_3139", dtype = "float64", shape = (2, 224))#candidate|3139|(2, 224)|var|float64
var_3140 = relay.var("var_3140", dtype = "int32", shape = (672,))#candidate|3140|(672,)|var|int32
const_3141 = relay.const([-3.798417,1.572805,-7.083347,8.212501,-2.243113,-2.859207,0.001378,4.741955,1.536991,9.963600,8.761884,-9.577930,-3.553570,2.845184,8.992936,-8.861661,3.116540,-6.529253,0.701943,9.920676,4.220965,0.391668,-9.133862,-4.789134,-5.145536,7.708434,6.265126,8.167744,-0.075422,4.909628,-4.270871,0.777116,3.721133,-4.564525,2.987063,7.300820,6.132213,4.147062,0.239069,1.364183,7.821318,5.255337,0.505959,4.191952,-1.902257,0.668578,-0.217302,-7.201469], dtype = "float32")#candidate|3141|(48,)|const|float32
const_3142 = relay.const([True,False,False,False,True,True,False,True,True,True,True,False,True,True,True,False,True,False,False,False,False,True,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True,False,True,False,True,False,True,True,True,False,True,True,False,True,True,True,False,True,True,True,True,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,False,False,False,True,True,True,False,False,False,True,True,True,False,True,True,True,False,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,False,True,False,True,True,True,True,False,False,True,False,False,True,True,True,True,True,False,True,True,True,True,False,True,True,True,True,False,True,False,True,True,False,True,False,True,True,False,True,True,True,False,False,False,True,True,True,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,False,True,True,True,True,True,True,False,True,True,False,False,False,False,True,True,True,True,True,True,True,False,False,False,False,False,False,False,True,True,True,True,False,False,True,False,True,False,False,False,True,True,True,True,True,False,False,False,True,True,True,False,True,True,False,True,True,False,True,False,True,False,False,True,True,True,True,False,True,False,True,False,True,False,True,False,False,True,False,True,False,True,True,True,False,True,False,False,True,True,False,False,False,False,True,True,True,True,True,False,True,False,False,False,False,True,False,False,False,False,True,False,True,False,True,True,True,True,True,False,True,False,False,True,False,False,False,False,True,True,False,False,False,True,False,False,False,False,True,True,False,False,True,True,True,True,False,False,False,False,True,True,False,True,False,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,True,False,False,True,True,True,False,False,True,False,False,False,False,False,False,False,False,True,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,True,True,False,True,False,True,True,True,False,True,False,True,True,False,False,False,False,False,True,True,False,True,True,False,False,False,False,False,False,True,True,True,True,True,False,True,False,True,False,True,True,False,False,False,True,True,True,True,True,False,False,True,True,True,True,False,False,True,False,False,True,False,False,False,True,False,True,False,False,True,True,True,True,True,True,False,False,False,True,False,True,False,True,False,True,True,False,True,False,True,False,True,True,False,True,False,False,False,False,False,True,True,True,True,True,True,True,True,True,True,True,False,True,True,True,False,False,True,False,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,True,True,False,False,True,True,False,True,False,True,False,False,True,False,False,True,False,False,True,False,False,True,False,True,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,False,True,True,True,True,True,True,True,False,False,True,True,True,False,True,True,False,True,False,False,True,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,True,True,True,False,False,False,False,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,True,False,False,True,False,False,True,True,True,False,False,False,False,False,False,True,True,False,True,True,True,False,True,False,False,True,True,False,False,False,True,False,False,True,True,True,True,True,False,False,True,True,False,False,True,False,True,False,True,False,False,False,False,True,False,True,False,True,True,True,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,False,True,False,False,False,False,False,False,False,False,True,True,False,False,True,True,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,True,False,False,True,False,False,False,True,True,False,False,False,False,False,True,False,False,True,False,False,False,True,True,True,False,False,False,True,True,False,False,False,False,False,True,True,True,True,False,False,True,False,False,False,False,False,False,True,True,False,True,True,False,True,True,False,True,True,True,False,True,True,False,False,False,True,True,True,True,True,True,False,True,True,False,True,True,False,False,False,True,False,False,True,True,True,True,False,False,False,False,False,False,False,False,False,True,True,True,False,False,False,True,True,True,True,False,True,False,True,True,True,True,True,False,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,False,False,False,True,True,False,False,True,True,False,False,False,True,True,False,True,True,False,False,True,True,False,True,False,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,False,False,True,False,True,False,False,True,True,False,False,False,False,False,True,True,True,True,False,False,False,False,False,True,False,False,True,True,True,True,True,False,True,False,False,True,False,False,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,True,True,True,False,True,True,True,True,True,False,False,False,False,True,True,False,True,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,True,True,True,False,False,True,True,False,True,False,False,False,True,False,True,True,False,False,True,True,False,False,True,False,True,True,False,True,True,True,True,True,False,True,True,False,False,True,False,True,True,False,True,False,False,True,True,False,True,False,True,True,False,False,False,True,True,False,False,True,True,False,False,True,True,True,True,True,False,True,False,True,True,True,True,True,False,False,False,True,False,True,True,False,False,True,False,True,True,False,False,False,False,False,True,True,False,False,False,False,True,False,False,False,False,True,True,False,False,True,False,False,True,True,True,True,False,True,False,True,True,True,True,False,True,False,True,True,False,False,False,True,False,False,True,False,True,False,True,True,False,True,False,True,False,True,False,False,False,False,True,True,True,False,True,True,False,True,False,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,True,False,False,True,False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,True,False,False,True,False,False,False,True,True,False,True,False,False,True,False,False,False,False,True,False,True,False,True,False,True,False,True,False,True,False,False,False,False,False,True,False,False,True,False,True,True,True,False,True,False,False,True,False,False,False,False,True,False,False,True,True,False,False,True,True,True,True,False,True,True,True,False,False,True,False,True,False,True,True,False,True,True,True,False,True,False,False,True,False,False,False,False,False,True,True,False,False,True,False,True,False,True,True,False,False,True,False,True,False,True,True,False,True,False,False,False,False,False,True,True,True,False,True,True,True,False,True,True,True,True,False,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,True,False,False,True,True,True,True,False,True,False,True,False,True,False,False,True,False,True,True,True,False,True,True,True,True,True,False,True,False,False,True,False,True,True,True,False,True,False,True,False,False,False,False,True,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,False,False,True,True,True,False,True,False,False,False,False,False,False,True,True,True,True,False,False,True,False,False,True,True,True,False,True,False,True,False,False,True,False,True,False,True,False,False,False,False,False,False,True,True,True,False,False,True,False,False,False,False,False,True,True,True,True,False,False,False,False,False,False,False,True,False,False,True,False,False,False,True,False,True,False,False,True,False,True,False,False,True,False,False,False,False,True,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,True,False,True,True,False,True,True,True,True,True,False,True,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,True,False,True,False,False,True,True,True,True,False,True,False,True,False,False,True,False,False,False,True,True,False,True,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,False,True,True,True,True,True,False,True,False,True,False,True,True,False,True,True,True,True,True,False,True,True,False,False,False,False,False,True,True,False,False,True,True,True,True,True,False,True,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,False,False,True,False,True,True,False,True,True,True,True,False,False,False,False,False,False,True,False,True,True,False,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True,False,False,True,False,True,True,True,False,False,True,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,False,True,False,False,False,False,False,True,False,True,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,True,True,True,False,False,True,True,False,True,True,False,False,False,True,True,True,True,True,False,False,False,False,False,True,True,True,True,False,True,True,True,False,False,False,False,False,True,True,True,True,False,True,True,True,False,False,False,True,False,False,True,False,False,True,True,True,True,True,True,False,False,False,False,False,False,True,False,True,False,True,False,True,True,True,False,True,False,False,True,False,False,False,False,False,False,True,True,True,False,False,True,False,False,True,False,False,False,True,True,True,False,False,False,True,True,False,True,True,False,False,True,False,False,True,False,False,True,True,True,True,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,False,True,False,True,True,False,True,True,True,False,True,True,True,False,True,True,True,True,True,False,True,True,True,False,True,False,True,True,False,True,False,False,False,True,False,False,True,True,True,False,True,True,False,True,True,True,False,True,False,True,True,False,False,True,False,True,True,True,False,True,False,True,False,True,False,False,True,True,True,False,False,False,True,False,True,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,True,False,False,True,True,True,False,False,True,False,True,True,False,False,False,True,False,False,False,False,True,True,False,True,True,False,False,False,True,True,False,False,False,False,True,True,False,True,True,True,True,True,True,True,True,True,True,False,True,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,True,False,True,True,True,False,False,True,True,True,False,True,True,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,False,True,False,True,True,True,False,True,False,True,False,True,False,False,False,True,False,True,False,False,False,True,True,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,True,True,False,True,True,True,True,True,False,True,True,False,False,True,False,True,True,True,False,True,True,True,True,True,False,True,True,True,True,False,True,False,False,True,True,True,False,True,False,True,False,True,True,False,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,False,True,False,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,True,False,True,False,True,False,False,True,True,False,True,False,True,False,True,True,True,True,False,True,True,True,True,True,True,True,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,False,True,True,False,True,False,False,False,False,True,True,False,False,True,True,False,False,False,False,True,False,False,False,False,True,False,False,True,True,True,False,True,False,True,False,True,False,False,True,False,True,True,False,False,False,False,False,False,False,False,True,True,False,True,True,False,True,True,True,False,False,True,True,False,True,True,False,True,True,True,True,True,False,False,True,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,True,True,True,True,False,False,False,False,True,False,True,False,True,False,False,False,False,False,True,True,True,False,False,False,False,True,True,False,False,False,False,False,False,True,True,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,True,False,False,True,True,False,False,False,True,True,False,True,True,False,False,False,False,True,True,False,True,True,False,True,True,True,False,False,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,False,False,False,False,True,True,False,True,False,True,True,True,False,True,False,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,True,True,False,False,True,True,False,True,True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,True,False,False,False,True,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,False,False,False,True,False,True,False,True,False,True,False,False,True,True,False,True,True,False,False,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,False,True,True,False,False,True,True,False,False,True,False,True,True,True,False,False,True,False,False,False,False,False,False,False,True,False,False,True,True,True,True,True,False,True,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,False,False,True,False,False,True,True,True,True,False,False,True,False,True,True,True,True,False,True,False,True,True,True,False,False,True,True,True,True,True,False,True,True,True,True,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,False,False,False,True,False,False,False,True,True,True,False,True,False,True,True,True,True,False,False,True,False,False,False,False,True,False,True,False,True,False,True,True,False,False,False,False,False,False,False,False,True,False,True,True,False,False,True,True,False,True,False,True,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,False,False,True,False,True,False,True,True,True,False,False,True,False,False,False,True,True,True,False,True,True,True,True,True,False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,False,True,False,False,False,True,False,False,False,True,False,False,False,False,True,False,True,False,True,False,True,False,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,False,True,True,True,True,True,True,True,False,True,True,True,False,True,False,True,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False,True,True,True,False,False,True,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,True,True,True,True,False,False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,True,True,True,True,False,False,False,False,False,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False], dtype = "bool")#candidate|3142|(2912,)|const|bool
const_3143 = relay.const([[2,-9,-2,-2],[-2,-6,-9,-3],[5,-1,-10,7],[3,9,-8,5],[8,-9,-2,-7],[-9,9,9,4],[10,4,-2,3],[5,-7,6,-2],[-7,5,1,-6],[-8,-8,-7,-2],[10,8,7,7],[-5,2,8,6],[-7,7,-4,10],[-7,10,3,-2],[-5,4,2,-3],[-8,8,1,3],[6,7,4,1],[-6,-7,2,5],[-2,9,-2,2],[-7,6,-6,-5],[-1,-2,8,6],[6,-6,-3,-4],[-9,10,5,-1],[-2,-8,6,-9],[-4,1,6,-9],[-9,9,-5,8],[7,-7,-9,3],[-5,-8,-6,7],[-9,3,6,-10],[-8,-8,3,9],[1,2,-4,1],[-10,10,7,-6],[-8,6,3,-8],[4,-6,-9,8],[-10,-1,-7,-4],[1,-1,-3,-9],[-7,4,10,1],[-5,10,3,-7],[-8,9,-9,2],[-7,2,-1,-1],[-5,-8,-5,8],[7,8,-6,5],[1,9,7,4],[8,3,7,10],[7,9,-9,5],[-3,-8,-8,-2],[4,-3,-7,-4],[2,-6,1,3],[4,-1,-6,-10],[1,-9,10,-10],[-5,7,9,-8],[-9,10,-8,10],[-2,6,-9,-9],[4,-9,-1,9],[1,1,7,9],[-2,8,1,-2],[10,4,-4,-10],[-3,1,10,-4],[-5,-9,2,8],[8,-4,3,5],[-5,3,-4,-6],[-5,-2,8,-6],[-1,-5,4,7],[-9,-4,-8,-6],[-7,-10,1,7],[6,1,-5,9],[1,-9,7,-8],[8,9,-8,-6],[-3,6,-6,-9],[2,6,-6,-5],[9,1,-9,-4],[-10,4,-7,5],[-9,-5,-5,7],[4,-7,8,-7],[-6,-5,-9,4],[4,-9,8,-3],[8,4,-2,-3],[4,-9,3,-1],[6,4,7,-9],[7,1,4,4],[2,7,9,-10],[-1,-5,-5,-3],[-4,-10,-6,1],[-7,-9,-8,6],[3,4,5,-2],[3,1,8,2],[-1,-3,1,2],[-8,-10,-6,-6],[10,-10,6,-1],[1,-8,6,-1],[10,7,9,1],[10,4,8,6],[2,2,8,-6],[7,-6,-1,3],[-10,-5,10,6],[9,-8,4,6],[-10,3,-4,-6],[2,-6,-10,6],[-7,-1,-9,7],[-1,-5,-2,10],[-1,-1,9,-6],[1,3,8,5],[2,-4,-7,1],[7,2,8,1],[-2,-4,10,-3],[1,6,7,7],[-9,2,-2,-3],[-8,-8,4,6],[4,10,-10,-6],[-9,10,-4,-7],[8,1,2,-10],[-9,-7,-10,1],[-10,7,-4,-1],[-5,-10,8,4],[-9,-7,-8,-1],[3,-10,-10,-6],[-1,-10,-6,-9],[4,2,9,7],[10,8,8,3],[-9,8,-3,10],[7,-1,5,-4],[1,8,-1,-9],[10,6,-9,3],[3,7,-4,-4],[-9,6,6,10],[3,7,-6,4],[6,-3,-1,2],[6,2,6,-4],[10,10,7,3],[-9,-5,-9,-10],[9,9,-10,3],[-8,-9,-10,3],[3,8,-5,-2],[-1,1,6,-4],[-5,-6,-4,2],[-6,10,5,10],[7,8,8,6],[8,1,7,10],[10,8,7,-8],[2,-2,1,5],[-7,8,2,5],[1,4,3,1],[-2,-7,-10,3],[-5,9,5,4],[6,9,7,-7],[-10,-6,7,-6],[6,-9,10,-10],[-6,-3,-4,7],[10,-9,-10,5],[9,4,-1,-8],[-8,5,8,-5],[4,-9,6,8],[2,4,6,-5],[-3,3,-1,-2],[8,7,3,-2],[9,-7,7,-2],[5,-2,-5,5],[6,-1,7,-6],[-3,10,-4,-4],[6,-9,-7,4],[6,2,-3,-9],[-3,7,-8,-6],[5,-6,2,3],[9,1,-4,-9],[-2,-4,-6,-5],[-5,-10,5,-3],[-3,1,-9,3],[10,-6,-10,-5],[-4,9,-1,-8],[9,1,-5,6],[5,3,-6,2],[10,-8,-2,3],[3,-5,-6,-3],[2,-1,-10,5],[8,9,-4,-8],[8,-5,1,8],[1,8,-10,-4],[-9,-1,4,4],[6,4,6,-6],[-7,7,-10,2],[10,-9,-3,3],[6,10,-10,1],[-2,7,6,2],[-4,-1,-4,4],[-5,4,-3,-1],[-1,-10,9,-8],[-8,-7,-8,-8],[-8,7,-4,-7],[3,8,-8,-9],[-1,-9,-2,-9],[2,5,-7,-2],[-1,-10,-9,5],[-8,-10,-3,-3],[-7,7,9,-2],[-4,-9,-9,7],[-2,-7,1,5],[-7,6,-3,8],[-1,-3,-1,-1],[1,5,3,-10],[-8,-5,10,-10],[6,-1,-7,3],[2,-8,1,7],[1,2,5,-8],[10,1,5,1],[7,10,-8,2],[9,4,-1,-1],[-6,-6,-4,3],[-10,-6,-6,-4],[-6,7,-7,6],[10,5,-3,-4],[9,10,-4,7],[-7,-7,-7,-6],[-7,-7,-3,-2],[6,-4,4,-8],[10,6,10,8],[-4,10,7,-4],[-10,-1,-7,8],[2,2,2,1],[-7,3,-10,-7],[-7,-6,3,-1],[3,8,6,-3],[7,-8,-3,-10],[8,2,-6,2],[5,8,-10,-3],[-10,2,6,-8],[-9,2,5,-6],[5,1,-6,5],[-3,-1,1,-5],[-4,8,-2,-3],[-3,7,-6,3],[9,-5,8,-6],[4,-3,1,7],[-7,-5,3,4],[-2,-4,-1,10],[-10,7,-6,7],[2,8,-10,-1],[1,-7,-4,8],[9,-4,6,2],[-10,4,-4,9],[-2,1,9,-8],[10,5,-6,9],[5,-6,7,7],[-9,-5,-3,-2],[9,-7,-7,-1],[4,-8,8,-6],[1,4,-3,7],[-3,6,-9,10],[-4,-8,-6,6],[6,-10,3,5],[-9,-4,-9,2],[-7,7,9,-4],[4,1,-5,-10],[3,3,-6,-2],[7,-5,10,10],[8,-1,-3,-9],[9,9,-9,2],[10,9,-6,-1],[8,-3,3,-4],[-9,1,2,-10],[-10,-4,1,2],[-3,-7,2,6],[-2,-6,10,-10],[-7,-2,-9,-7],[-3,-1,-8,6],[-3,-4,9,-5],[-9,-7,-3,10],[8,-6,-4,9],[5,-2,2,-4],[-8,-2,-8,-9],[-9,8,5,-1],[-1,1,1,3],[-9,-9,-2,8],[1,9,8,-8],[6,9,5,-6],[9,10,-7,-8],[-9,-9,-1,-2],[-6,4,3,-1],[8,-2,-1,7],[-6,-4,1,1],[-10,-2,-7,3],[-9,9,7,-1],[-9,-7,-9,-4],[1,-10,-1,-4],[-9,-2,-5,2],[-2,-4,-1,5],[7,-4,-6,3],[-6,4,2,-10],[6,-9,-9,-5],[-2,-1,3,4],[-9,8,7,-7],[-4,2,-10,-1],[6,-7,3,-7],[10,-9,-7,-5],[-1,4,-4,-3],[-1,-8,-9,7],[-1,10,8,-10],[-9,-1,3,-3],[-9,-2,-7,5],[10,-10,2,-4],[-6,8,6,-10],[6,9,7,4],[8,-9,3,-6],[-7,1,8,4],[-2,5,10,-10],[9,6,1,2],[-5,6,-6,10],[9,-5,-9,-10],[-3,8,2,-10],[9,-7,-3,10],[1,-8,8,-2],[-1,5,-8,-2],[2,6,10,-5],[9,9,-2,-4],[5,-1,1,-2],[-10,6,-4,3],[-8,9,3,5],[5,-8,3,1],[-3,2,4,10],[-5,-4,-3,-4],[-3,9,7,2],[7,1,1,9],[4,9,9,4],[6,-2,4,-9],[1,7,-3,-3],[6,-2,8,10],[-5,10,10,8],[1,-6,8,-3],[5,-8,-6,7],[-7,-10,2,-6],[1,-1,-9,9],[-2,6,10,10],[7,4,-1,7],[1,4,7,10],[-8,-1,3,9],[-6,-5,4,4],[3,5,8,-3],[-9,-2,-7,-6],[-5,-3,8,-4],[-7,-3,-4,2],[-2,5,-1,8],[-5,8,-5,6],[3,10,1,8],[-3,-1,-5,-8],[10,-8,10,-2],[-8,-7,-5,5],[-4,1,-9,5],[9,2,-7,-4],[2,9,-8,8],[-9,9,10,4],[-8,-9,-6,-10],[-10,-1,-3,-5],[7,-6,5,8],[-9,-10,10,-2],[10,5,6,1],[10,-3,8,-7],[-2,-7,8,-2],[4,-7,7,3],[1,-1,5,-4],[-5,7,7,-8],[8,-7,-3,-3],[-1,1,2,-3],[-2,-1,-8,2],[-4,-9,-5,-9],[4,-9,-2,-6],[-5,-3,1,-9],[2,-1,-4,6],[-6,-6,-9,3],[-10,-2,5,9],[5,6,-8,2],[-4,2,10,6],[10,4,-9,-5],[-9,3,-7,3],[-4,9,-1,-2],[5,-3,-2,8],[2,-1,1,2],[-5,2,-9,3],[4,-3,-4,-2],[-1,-4,5,-2],[6,-2,3,6],[10,9,5,-1],[7,-5,-1,10],[3,2,7,-9],[-9,-9,4,10],[3,3,3,-8],[8,-1,-2,8],[6,7,1,-6],[8,3,-1,6],[-2,4,3,-6],[-7,7,-10,5],[4,-9,10,7],[1,10,1,-9],[-6,-8,7,9],[1,-1,2,4],[2,1,1,7],[-8,-5,4,-1],[7,7,-3,7],[-4,-2,-8,2],[-2,-9,-3,-4],[-5,9,2,-8],[-9,-4,5,6],[-10,6,7,-8],[-3,1,-5,-4],[-5,-10,2,8],[6,4,1,-1],[-8,-9,-4,-3],[3,-10,10,-1],[-8,-2,10,4],[1,-7,9,5],[4,-2,2,7],[1,6,-3,6],[7,-4,7,-4],[5,1,9,1],[2,6,-9,9],[-10,9,1,7],[-3,-6,-8,-9],[2,-6,7,-8],[1,3,7,-7],[-7,2,-4,-8],[9,-9,4,9],[9,-1,-3,7],[3,1,2,-6],[-8,6,9,-1],[8,3,-8,-10],[-8,-5,-1,4],[-2,3,6,-4],[-2,-8,-6,7],[-9,-8,5,-5],[-10,-3,-5,-7],[3,-3,-1,-5],[7,4,-2,-9],[-3,7,-4,10],[-5,7,1,6],[-3,-5,4,-1],[-1,6,6,-4],[10,-7,-4,-2],[-2,-8,4,9],[1,-4,-3,-7],[10,10,7,-4],[-5,-3,10,9],[-6,-4,-1,8],[8,8,-8,10],[6,-3,3,-2],[-10,1,-10,-1],[1,7,-10,-3],[-6,2,6,2],[-1,5,-6,-6],[1,6,2,-8],[-3,-3,9,-3],[-9,-10,6,-4],[-1,-3,-7,-3]], dtype = "uint32")#candidate|3143|(450, 4)|const|uint32
call_3137 = relay.TupleGetItem(func_2125_call(relay.reshape(var_3138.astype('float64'), [7, 8, 1]), relay.reshape(var_3139.astype('float64'), [7, 8, 8]), relay.reshape(var_3140.astype('int32'), [672,]), relay.reshape(const_3141.astype('float32'), [48,]), relay.reshape(const_3142.astype('bool'), [2912,]), relay.reshape(const_3143.astype('uint32'), [1800,]), ), 5)
call_3144 = relay.TupleGetItem(func_2133_call(relay.reshape(var_3138.astype('float64'), [7, 8, 1]), relay.reshape(var_3139.astype('float64'), [7, 8, 8]), relay.reshape(var_3140.astype('int32'), [672,]), relay.reshape(const_3141.astype('float32'), [48,]), relay.reshape(const_3142.astype('bool'), [2912,]), relay.reshape(const_3143.astype('uint32'), [1800,]), ), 5)
output = relay.Tuple([call_3134,call_3137,var_3138,var_3139,var_3140,const_3141,const_3142,const_3143,])
output2 = relay.Tuple([call_3135,call_3144,var_3138,var_3139,var_3140,const_3141,const_3142,const_3143,])
func_3145 = relay.Function([var_3138,var_3139,var_3140,], output)
mod['func_3145'] = func_3145
mod = relay.transform.InferType()(mod)
mutated_mod['func_3145'] = func_3145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3145_call = mutated_mod.get_global_var('func_3145')
var_3147 = relay.var("var_3147", dtype = "float64", shape = (56,))#candidate|3147|(56,)|var|float64
var_3148 = relay.var("var_3148", dtype = "float64", shape = (2, 224))#candidate|3148|(2, 224)|var|float64
var_3149 = relay.var("var_3149", dtype = "int32", shape = (672,))#candidate|3149|(672,)|var|int32
call_3146 = func_3145_call(var_3147,var_3148,var_3149,)
output = call_3146
func_3150 = relay.Function([var_3147,var_3148,var_3149,], output)
mutated_mod['func_3150'] = func_3150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2849_call = mod.get_global_var('func_2849')
func_2850_call = mutated_mod.get_global_var('func_2850')
call_3267 = relay.TupleGetItem(func_2849_call(), 0)
call_3268 = relay.TupleGetItem(func_2850_call(), 0)
func_2446_call = mod.get_global_var('func_2446')
func_2448_call = mutated_mod.get_global_var('func_2448')
call_3271 = relay.TupleGetItem(func_2446_call(), 1)
call_3272 = relay.TupleGetItem(func_2448_call(), 1)
func_2636_call = mod.get_global_var('func_2636')
func_2637_call = mutated_mod.get_global_var('func_2637')
call_3273 = relay.TupleGetItem(func_2636_call(), 1)
call_3274 = relay.TupleGetItem(func_2637_call(), 1)
func_1739_call = mod.get_global_var('func_1739')
func_1741_call = mutated_mod.get_global_var('func_1741')
call_3275 = relay.TupleGetItem(func_1739_call(), 0)
call_3276 = relay.TupleGetItem(func_1741_call(), 0)
func_471_call = mod.get_global_var('func_471')
func_475_call = mutated_mod.get_global_var('func_475')
const_3278 = relay.const([[5.605212,7.275596,-5.949083,3.593097,-8.594441,-2.546628,1.012022,-6.565826,-0.708100,-9.805103,6.288058,2.911585,5.883059,-2.901718,-6.017046,1.945718,-4.145934,8.768577,-1.006445,-1.254959,7.443005,8.567424,-2.241245,-3.627733],[-7.824627,6.383715,-2.896746,-2.130363,-4.115073,5.906448,7.617763,-9.322117,-4.990388,-4.749998,-4.351189,5.463799,-0.369213,-9.839387,-4.627952,7.630953,-1.537406,3.426023,5.673084,-6.403939,-5.478915,0.632468,-7.498783,3.463007]], dtype = "float32")#candidate|3278|(2, 24)|const|float32
const_3279 = relay.const([False,False,False,True,False,True,True,True,True,False,False,True,True,True,True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,True,True,True,True,True,False,False,True,True,False,True,True,False,False,False,False,True,False,True,True,False,False,True,True,True,False,False,True,True,True,False,False,True,True,True,False,True,True,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False,False,False,False,True,False,True,True,True,False,True,True,False,False,True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,False,True,True,False,True,False,False,True,False,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False,False,True,True,True,False,False,False,False,False,True,True,True,True,True,False,True,True,False,False,False,True,False,False,True,True,False,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,True,True,False,True,False,False,False,False,True,False,True,False,False,False,False,False,False,False,True,False,True,True,True,False,True,True,True,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,False,True,True,True,True,True,False,False,False,True,False,True,False,False,False,True,False,True,False,False,True,True,False,False,True,False,False,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,True,False,True,True,True,True,False,True,True,False,True,False,True,False,False,False,True,False,True,False,False,False,False,True,False,True,False,True,False,True,True,True,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,True,True,True,False,True,True,True,False,False,True,True,False,False,False,False,True,False,False,True,True,True,False,False,True,True,False,True,False,False,True,False,True,False,True,True,True,False,False,True,True,False,True,True,False,True,True,True,True,True,True,True,False,True,True,True,False,True,True,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False,True,True,True,False,False,True,True,True,True,True,True,False,False,True,False,True,False,True,False,True,False,True,True,False,True,False,True,False,False,True,False,True,False,True,True,True,False,False,False,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,True,True,False,False,True,False,True,True,True,False,False,False,True,True,False,True,False,True,True,False,True,True,False,True,False,True,False,True,True,True,False,False,False,False,True,False,False,False,True,True,False,False,True,True,True,True,True,True,True,False,True,False,True,True,True,False,True,False,True,False,True,True,False,True,False,True,True,False,False,True,False,False,True,True,False,False,True,True,True,False,True,True,False,False,False,False,False,True,False,True,True,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False,True,True,False,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,True,False,False,True,True,True,True,True,False,True,True,False,False,False,False,False,True,True,False,False,True,True,False,False,False,False,True,True,False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False,True,True,True,True,True,True,True,True,False,False,False,True,True,True,True,False,False,False,False,False,False,False,False,False,True,False,False,False,True,True,True,False,False,False,False,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,False,False,False,False,False,True,False,True,True,False,True,True,False,False,True,False,False,True,False,True,True,False,False,True,False,True,True,True,True,False,False,True,True,True,True,True,False,False,False,False,False,True,True,False,False,False,False,False,True,False,False,True,False,False,False,False,True,False,True,False,False,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,True,False,False,False,False,False,True,True,False,False,True,True,False,True,True,False,True,False,False,False,True,False,True,True,True,True,False,True,True,False,True,False,True,True,True,True,False,False,False,False,False,False,False,False,True,True,True,False,False,True,False,True,True,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,False,False,False,True,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,True,True,True,True,True,True,True,False,True,True,False,True,True,False,False,False,True,False,False,False,False,True,True,True,False,False,False,True,True,False,True,False,True,False,True,False,True,False,True,False,True,True,False,True,False,False,True,True,False,False,False,False,True,True,True,True,True,True,False,False,False,False,False,True,False,False,False,False,False,True,False,False,False,False,True,False,False,False,False,False,False,False,False,False,True,True,True,True,True,False,True,True,False,False,False,False,False,False,False,False,True,True,False,False,True,True,False,False,False,False,False,False,False,True,False,False,False,False,True,True,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,True,True,True,True,True,False,False,True,False,True,False,False,True,False,True,True,False,False,True,False,False,False,False,True,False,True,False,True,True,True,False,True,False,True,False,True,True,False,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,True,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,True,False,False,True,True,False,False,False,True,False,True,False,False,False,False,True,True,True,False,False,False,True,False,True,True,True,True,True,True,False,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,False,False,False,True,False,True,True,True,True,True,False,False,False,True,True,True,True,True,True,True,False,True,True,False,False,True,False,True,True,False,True,True,False,True,False,True,False,True,False,False,False,True,False,True,False,False,False,True,True,True,False,False,False,False,False,True,True,False,False,False,False,True,True,True,True,True,False,True,False,False,True,True,True,False,False,False,False,False,True,True,True,False,True,False,False,True,True,True,True,True,True,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,True,True,False,False,False,False,False,False,False,False,True,True,True,True,False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,True,False,False,False,False,True,False,False,True,False,False,False,False,True,True,True,False,False,False,True,False,False,True,False,True,False,True,True,False,False,True,True,False,True,True,True,False,True,True,False,False,False,False,False,True,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False,False,False,True,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,True,False,False,True,True,True,True,True,True,False,False,False,False,False,False,False,True,True,False,False,True,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,True,True,True,False,False,True,False,False,True,False,False,True,False,False,True,True,True,True,True,False,False,False,True,False,True,False,True,False,False,True,False,True,True,False,False,True,True,False,True,True,True,True,False,True,False,True,False,True,False,True,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,True,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False,True,False,False,False,False,True,False,False,True,True,False,False,True,False,True,False,False,True,True,True,True,False,True,True,False,True,True,False,False,False,False,True,False,True,True,False,False,False,False,True,True,True,True,True,True,False,True,False,True,True,True,False,True,True,True,True,False,True,False,False,True,False,False,True,True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,False,False,False,True,True,True,False,True,True,True,True,False,False,True,False,True,True,True,True,False,True,True,True,False,False,False,False,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,True,False,True,True,True,False,True,False,False,False,True,True,False,True,False,False,False,False,True,True,False,True,False,False,True,False,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,False,True,False,False,True,False,False,True,True,False,False,True,False,True,True,False,True,True,False,False,False,True,False,False,False,False,False,False,False,True,True,False,True,True,False,False,False,False,True,True,True,False,True,True,True,False,False,False,True,False,False,True,True,False,False,False,False,False,False,True,True,True,True,False,False,False,True,False,False,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,True,False,False,False,False,False,True,False,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,False,True,False,False,False,True,True,False,True,True,True,False,True,False,True,False,False,True,True,True,False,True,True,True,False,True,False,False,False,True,True,False,False,True,False,False,True,True,True,False,True,False,True,False,False,False,False,True,True,False,False,False,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,True,False,False,True,False,False,True,False,True,False,True,False,True,True,False,False,True,True,True,False,False,False,False,False,True,False,False,True,False,False,False,True,False,False,False,True,False,True,True,False,True,False,False,True,False,False,True,True,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,False,False,True,True,False,True,False,False,False,True,False,True,True,True,False,False,False,False,True,False,True,False,False,False,True,False,True,True,False,True,False,False,True,True,False,True,False,False,False,True,True,False,False,False,True,True,False,False,True,True,False,False,True,False,True,True,False,False,False,False,True,False,False,False,True,False,False,False,True,False,True,False,False,True,True,False,False,True,False,False,True,False,False,False,False,True,True,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,False,False,True,True,False,False,True,False,False,False,False,False,False,False,False,False,False,False,True,False,True,True,True,True,False,False,True,True,False,True,True,False,False,False,False,False,False,True,True,False,True,True,True,True,False,True,True,False,True,True,True,False,False,False,False,False,False,True,True,False,True,False,False,True,False,False,True,True,True,False,True,False,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,True,False,True,True,True,True,False,False,False,False,False,True,False,False,False,False,False,True,False,False,False,False,True,True,False,False,False,True,False,True,True,True,True,True,True,True,False,True,True,False,True,True,True,True,False,False,False,False,True,False,True,True,False,False,False,True,False,False,False,False,True,True,False,True,False,True,False,True,False,True,True,True,True,True,True,True,True,True,True,False,True,False,True,False,False,False,True,True,False,True,True,False,False,True,True,True,False,True,False,False,False,True,False,True,False,True,False,True,False,False,True,True,False,True,True,True,True,False,False,True,True,True,True,False,True,False,True,True,True,True,False,False,False,False,True,True,True,False,False,True,False,False,False,False,True,False,True,False,False,True,True,False,True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,False,False,False,True,False,False,False,True,True,False,False,True,False,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,True,True,True,True,False,True,True,True,False,True,False,False,True,False,True,False,False,False,False,False,False,False,True,False,True,False,False,True,True,False,True,False,True,False,False,True,True,True,False,False,False,True,False,True,True,True,True,True,True,True,False,False,True,True,False,False,True,True,True,True,True,False,True,False,True,True,True,False,False,False,False,False,True,True,True,False,False,False,False,False,True,False,False,True,True,False,True,False,True,True,True,False,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,True,True,True,False,False,True,True,True,True,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,True,False,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,False,False,True,False,False,False,False,True,False,True,False,False,False,True,True,False,False,True,True,True,True,True,True,False,False,False,False,False,False,False,True,True,True,False,True,True,False,False,False,False,True,False,False,True,True,True,True,False,False,True,True,True,False,False,False,True,False,False,True,False,True,False,True,False,False,True,True,False,True,True,False,False,True,True,False,True,False,True,True,True,False,False,False,True,False,False,False,False,True,True,False,False,True,False,False,True,True,True,True,False,False,True,False,True,False,False,False,True,False,True,False,False,True,False,True,True,True,True,True,False,False,False,False,True,False,False,False,True,True,True,True,True,True,True,False,True,False,True,False,False,False,False,False,False,True,False,True,False,True,True,False,False,True,False,True,True,False,False,False,True,True,True,False,False,False,False,False,False,True,False,False,False,True,True,False,False,True,True,False,False,False,False,False,True,False,False,False,False,False,False,True,True,True,True,False,False,True,False,False,True,False,True,True,True,False,True,True,True,False,True,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,True,True,True,True,True,False,False,False,True,True,False,False,True,True,False,False,True,True,False,True,False,True,True,True,True,True,False,True,False,True,True,False,False,False,True,False,False,True,False,True,True,True,True,False,False,True,False,True,True,False,False,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,False,True,False,True,False,True,False,True,True,False,True,True,False,False,False,False,True,False,False,True,True,False,True,True,True,True,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,True,False,False,True,False,False,False,False,False,True,True,True,False,True], dtype = "bool")#candidate|3279|(2912,)|const|bool
call_3277 = relay.TupleGetItem(func_471_call(relay.reshape(const_3278.astype('float32'), [1, 3, 16]), relay.reshape(const_3279.astype('bool'), [104, 28]), ), 2)
call_3280 = relay.TupleGetItem(func_475_call(relay.reshape(const_3278.astype('float32'), [1, 3, 16]), relay.reshape(const_3279.astype('bool'), [104, 28]), ), 2)
output = relay.Tuple([call_3267,call_3271,call_3273,call_3275,call_3277,const_3278,const_3279,])
output2 = relay.Tuple([call_3268,call_3272,call_3274,call_3276,call_3280,const_3278,const_3279,])
func_3282 = relay.Function([], output)
mod['func_3282'] = func_3282
mod = relay.transform.InferType()(mod)
mutated_mod['func_3282'] = func_3282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3282_call = mutated_mod.get_global_var('func_3282')
call_3283 = func_3282_call()
output = call_3283
func_3284 = relay.Function([], output)
mutated_mod['func_3284'] = func_3284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2986_call = mod.get_global_var('func_2986')
func_2988_call = mutated_mod.get_global_var('func_2988')
call_3325 = func_2986_call()
call_3326 = func_2986_call()
var_3327 = relay.var("var_3327", dtype = "float64", shape = (4, 15, 15))#candidate|3327|(4, 15, 15)|var|float64
bop_3328 = relay.not_equal(call_3325.astype('bool'), relay.reshape(var_3327.astype('bool'), relay.shape_of(call_3325))) # shape=(4, 15, 15)
bop_3331 = relay.not_equal(call_3326.astype('bool'), relay.reshape(var_3327.astype('bool'), relay.shape_of(call_3326))) # shape=(4, 15, 15)
func_2680_call = mod.get_global_var('func_2680')
func_2682_call = mutated_mod.get_global_var('func_2682')
call_3334 = relay.TupleGetItem(func_2680_call(), 0)
call_3335 = relay.TupleGetItem(func_2682_call(), 0)
output = relay.Tuple([bop_3328,call_3334,])
output2 = relay.Tuple([bop_3331,call_3335,])
func_3336 = relay.Function([var_3327,], output)
mod['func_3336'] = func_3336
mod = relay.transform.InferType()(mod)
var_3337 = relay.var("var_3337", dtype = "float64", shape = (4, 15, 15))#candidate|3337|(4, 15, 15)|var|float64
output = func_3336(var_3337)
func_3338 = relay.Function([var_3337], output)
mutated_mod['func_3338'] = func_3338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2400_call = mod.get_global_var('func_2400')
func_2402_call = mutated_mod.get_global_var('func_2402')
call_3353 = relay.TupleGetItem(func_2400_call(), 0)
call_3354 = relay.TupleGetItem(func_2402_call(), 0)
func_1040_call = mod.get_global_var('func_1040')
func_1044_call = mutated_mod.get_global_var('func_1044')
const_3364 = relay.const([-5,-1,10,1,8,6,9,-7,5,9,1,6,-4,10,3,8,-2,1,4,-5,-1,4,-6,-6,-8,-4,5,-7,-2,-6,2,5,4,5,9,10,10,10,2,-7,-9,1,9,-2,3,-8,-3,-9,10,-4,-6,6,6,-2,-2,-1,9,6,8,-3,-7,7,3,-4,2,1,-2,-3,-5,-9,5,-9,-9,-6,-4,-9,-9,8,4,6,-1,3,-4,-2], dtype = "int32")#candidate|3364|(84,)|const|int32
const_3365 = relay.const([-7,8,-7,-2,8,-2,-6,5,5,-9,5,-8,3,-7,2,-5,-2,-6,2,2,5,-8,4,-6,-5,10,4,8,-1,-4,7,-1,-2,8,4,-5,1,-9,-9,6,1,-1,3,4,-4,-6,-6,10,3,-2,-7,7,10,-2,2,-10,3,9,1,-1,-4,8,5,9,-7,8,-8,1,-2,7,-3,8,8,-4,-5,-6,4,-10,-3,9,-10,3,2,7,8,-10,1,-7,-7,2,5,-2,3,8,-1,-5,5,-10,-3,-3,-1,4,-10,4,1,1,3,7,-7,9,3,8,5,5,5,1,-10,9,-5,9,-7,1,6,-4,-2,-1,-1,3,7,4,-7,-9,9,8,8,-9,10,5,-8,10,-3,5,2,-10,7,2,-10,-2,8,4,-7,-1,2,4,-4,-10,-5,-1,-2,-7,-4,4,1,-2,5,-3,8,9,9,-10,8,-1,2,10,-2,2,8,-9,-1,6,-8,6,4,-6,9,-7,3,-9,-2,8,8,2,-7,6,6,1,2,8,5,8,-7,10,-5,-6,10,2,5,5,-7,-7,3,-4,9,3,-7,7,-8,-5,-8,1,-4,-3,7,8,-8,-8,7,10,-6,-10,-3,-7,6,5,3,-9,9,4,1,-1,-1,4,10,1,-4,-9,10,8,-9,7,9,7,-9,3,4,-10,10,2,5,-8,-6,8,2,-9,10,-3,3,6,-10,3,2,1,-7,-4,6,-3,-8,6,8,-2,-3,-5,4,10,10,-10,-7,4,3,6,9,-10,2,-6,-3,-9,3,5,-5,1,-6,-8,3,-7,-10,-4,4,-6,3,-9,10,5,1,-1,2,-4,5,3,3,-2,5,-4,3,-7,9,3,5,-3,7,-5,-7,9,-10,-8,4,-8,8,-10,-9,7,5,9,7,6,-7,-3,7,-6,6,-2,6,1,-9,6,8,-7,-1,-2,-10,2,-7,-4,9,-3,-6,7,-2,-7,-9,-2,4,7,8,6,8,-7,-3,1,-1,-6,9,10,-4,-6,-1,8,-8,5,-6,5,-6,-9,3,10,-6,2,2,9,-10,6,3,-9,1,-10,2,1,6,-9,-1,3,-7,-3,7,-4,-8,10,-6,-6,-2,2,-10,4,-2,-4,-5,-10,-2,-1,8,-7,6,10,6,-9,-2,2,3,-9,2,9,2,8,-4,-4,6,9,-9,-6,-4,-3,5,10,3,4,-7,-3,-2,-5,-1,7,10,-9,-4,6,-9,6,-6,3,-10,-7,10,5,10,-6,-9,-8,10,10,4,4,4,-9,-10,2,-1,-6,8,3,-1,10,-6,9,-8,2,4,7,-7,10,1,9,2,5,7,7,10,8,-6,2,5,-3,-1,6,-9,7,-10,-3,2,-10,7,6,7,-3,-10,-4,-10,-3,9,9,8,9,-10,10,-10,10,-10,-5,10,-9,-5,-7,-1,-4,-10,10,8,-5,2,8,-8,1,5,-4,-6,-7,-5,5,-3,-8,-3,2,-8,8,4,3,-6,-9,-2,8,-5,10,9,8,6,6,6,9,-7,-5,-6,-3,5,-3,-3,9,-8,-10,4,-1,-5,10,-7,7,-7,-4,-1,5,-7,6,-1,-9,-2,6,-10,8,3,7,6,-3,6,-6,-4,-4,-9,-2,3,-1,-2,-5,-3,-8,-9,-8,8,-8,9,-3,2,4,8,-4,-7,10,-2,-2,5,3,4,9,-3,8,10,6,1,-5,-4,-1,-2,10,5,-10,1,-4,-7,9,-9,-3,-10,-1,9,-9,-5,-5,1,-2,7,-7,-7,3,4,-5,9,-2], dtype = "int32")#candidate|3365|(672,)|const|int32
call_3363 = relay.TupleGetItem(func_1040_call(relay.reshape(const_3364.astype('int32'), [1, 7, 12]), relay.reshape(const_3365.astype('int32'), [8, 7, 12]), ), 1)
call_3366 = relay.TupleGetItem(func_1044_call(relay.reshape(const_3364.astype('int32'), [1, 7, 12]), relay.reshape(const_3365.astype('int32'), [8, 7, 12]), ), 1)
func_1844_call = mod.get_global_var('func_1844')
func_1845_call = mutated_mod.get_global_var('func_1845')
call_3378 = relay.TupleGetItem(func_1844_call(), 1)
call_3379 = relay.TupleGetItem(func_1845_call(), 1)
output = relay.Tuple([call_3353,call_3363,const_3364,const_3365,call_3378,])
output2 = relay.Tuple([call_3354,call_3366,const_3364,const_3365,call_3379,])
func_3381 = relay.Function([], output)
mod['func_3381'] = func_3381
mod = relay.transform.InferType()(mod)
mutated_mod['func_3381'] = func_3381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3381_call = mutated_mod.get_global_var('func_3381')
call_3382 = func_3381_call()
output = call_3382
func_3383 = relay.Function([], output)
mutated_mod['func_3383'] = func_3383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2300_call = mod.get_global_var('func_2300')
func_2301_call = mutated_mod.get_global_var('func_2301')
call_3397 = relay.TupleGetItem(func_2300_call(), 0)
call_3398 = relay.TupleGetItem(func_2301_call(), 0)
func_2534_call = mod.get_global_var('func_2534')
func_2535_call = mutated_mod.get_global_var('func_2535')
call_3418 = relay.TupleGetItem(func_2534_call(), 2)
call_3419 = relay.TupleGetItem(func_2535_call(), 2)
output = relay.Tuple([call_3397,call_3418,])
output2 = relay.Tuple([call_3398,call_3419,])
func_3429 = relay.Function([], output)
mod['func_3429'] = func_3429
mod = relay.transform.InferType()(mod)
mutated_mod['func_3429'] = func_3429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3429_call = mutated_mod.get_global_var('func_3429')
call_3430 = func_3429_call()
output = call_3430
func_3431 = relay.Function([], output)
mutated_mod['func_3431'] = func_3431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2265_call = mod.get_global_var('func_2265')
func_2266_call = mutated_mod.get_global_var('func_2266')
call_3432 = func_2265_call()
call_3433 = func_2265_call()
func_2125_call = mod.get_global_var('func_2125')
func_2133_call = mutated_mod.get_global_var('func_2133')
var_3438 = relay.var("var_3438", dtype = "float64", shape = (56,))#candidate|3438|(56,)|var|float64
const_3439 = relay.const([-7.197140,-7.138269,-2.301259,2.252921,-3.210238,9.029689,-8.595905,5.019100,3.944741,-4.414544,9.414018,-7.583870,3.840157,-2.869798,3.779559,0.049109,4.793798,2.010253,-5.682155,4.659360,-6.354988,4.144865,-3.837329,-5.313383,6.787844,2.825579,-4.136661,-7.851930,1.186364,-2.281521,7.475005,-9.683122,3.459012,-8.598818,1.782075,8.006279,-7.485126,-0.317022,6.884268,-4.612434,8.937663,0.844845,-3.919321,0.650830,7.684889,-7.998423,5.995805,8.532916,-6.707621,9.969570,3.123179,0.466810,5.134990,-0.199976,4.411213,4.545221,-0.388829,-8.640759,-9.414957,-2.298299,-6.669959,-6.675792,-8.327012,-0.694383,5.306356,-1.772058,-9.659214,-4.572632,5.792637,6.282506,-2.418817,9.325835,9.654476,0.777149,3.415960,5.818374,-0.630724,0.406449,9.215081,9.909597,6.637500,9.982127,1.900777,6.059354,-2.156441,5.080038,0.303843,3.856628,1.594692,7.576518,9.360040,-1.845349,-4.734566,-2.609249,5.094334,1.804906,3.660449,8.269803,-2.554634,6.088597,0.030676,3.263718,9.619019,3.699548,1.012187,7.236600,-9.153434,-1.368778,2.300445,-9.834740,-3.337423,-9.412129,0.774262,9.448131,-9.640717,-6.854141,7.560892,4.274181,8.622587,9.504250,1.148906,8.565421,-5.624304,-9.446556,-1.644998,7.388229,-5.027565,-2.723706,4.054186,-7.578319,-1.576450,7.176374,-8.632649,-1.552996,5.690791,0.714150,-8.087486,-7.823735,-8.421070,-4.365614,-2.600218,-8.949560,1.401696,-5.099468,-8.337733,4.652693,8.472446,-1.082325,2.146625,5.720914,7.750877,7.057316,5.952611,-0.787195,-9.833101,-6.511428,-5.740181,-0.473634,2.702939,-3.805578,4.289371,-8.203565,-8.986584,-7.640168,5.127793,4.285279,-6.312418,-6.213839,-6.507265,-9.002586,-3.422581,3.355051,1.662501,-4.654104,-4.888086,-9.001073,-4.935520,6.786604,5.702553,-3.831375,0.046192,8.547346,-2.128701,-8.680583,9.543980,-0.139960,2.579210,-7.004539,5.372771,-7.280254,-1.473369,6.659122,1.570510,0.537045,-3.694580,-3.668640,3.292752,-7.899741,7.711731,1.877839,9.282249,-7.723076,0.301368,9.466308,-8.207275,8.983187,-8.205502,7.458752,0.665161,-1.851851,2.034890,8.064971,3.066610,-1.634163,-4.285414,7.888558,1.833061,4.045410,-1.628453,9.901748,-6.693316,9.119961,5.454917,-3.902100,-7.506393,6.718894,1.590507,-8.501073,-6.847732,-6.008248,-7.506184,-3.663026,6.663840,1.595828,-5.277127,-3.119600,7.938634,7.286319,1.415866,1.215745,-9.205654,8.455362,7.457338,-4.417376,-7.324803,9.853610,-2.940312,7.257484,6.928706,-4.288070,8.138751,-1.881393,-1.877627,-9.810472,0.210329,4.927409,-7.882406,-8.185701,4.709727,1.125773,6.041734,-4.460510,-7.029650,7.785873,-6.240686,3.851830,3.155921,-6.252279,6.310671,4.849493,-0.213420,-8.517610,0.836265,5.282588,-7.069112,-1.785798,8.543515,1.847359,-6.657555,4.810908,-7.096273,8.171874,-3.107985,-2.185283,-3.812929,-1.760789,-6.813133,9.705313,3.495413,-2.151670,3.991208,6.294025,-1.398492,-3.123450,-5.525228,1.583456,-2.931140,-6.025580,0.455839,-9.498211,-7.886896,-8.193605,6.196008,-4.006304,-3.736822,-2.401152,0.873007,-0.453827,9.626114,0.618808,-1.290913,-1.204343,1.764212,0.607370,3.178409,-3.038776,4.957740,4.804835,-3.978715,1.564434,-7.624020,-4.386174,-7.811991,3.362057,6.519256,7.722725,-2.721596,-2.794418,-6.270924,-7.771127,3.333658,1.133839,4.992157,7.968800,-5.614561,1.624083,1.471905,-9.910143,-4.251861,2.497899,-3.892974,-3.046751,-0.420663,-4.638827,-0.262446,6.853269,9.377584,-2.449710,2.842157,-9.363690,4.686200,-6.918204,4.926161,-0.660380,2.310302,0.640755,-3.200106,-6.782102,-8.770239,8.464618,9.412343,-3.729702,2.836984,9.674323,0.015644,-4.221995,6.734258,9.660077,7.451327,0.450332,1.766912,6.314931,-6.299775,-3.391685,-7.724539,2.226094,-4.194803,0.408216,6.604408,-4.619527,-5.924718,1.824905,-2.186601,7.697239,-6.261099,-6.427761,5.317910,5.203631,8.766703,6.548620,7.955994,3.684007,-8.145689,0.729393,3.754904,-5.214404,-1.250946,-1.673768,-2.194818,-9.001055,-2.956389,-9.417132,-4.287922,5.195367,-9.801391,-1.207129,3.866825,0.431782,-7.462293,0.553816,5.586872,8.202675,8.650531,-1.300957,7.204323,-0.477768,5.396926,-9.355473,-3.083486,0.274976,-3.664536,-5.507788,9.204878,7.719643,-9.557207,8.856753,1.516575,9.810900,-3.727863,-7.344555,3.606858,4.936160,-1.768522,-2.571657,5.439588,3.988216,7.730140,-3.181670,8.278941,-4.761375,-9.672792,8.677599,5.089163,1.462896,-9.601229,9.820636,-3.642627,-5.669671], dtype = "float64")#candidate|3439|(448,)|const|float64
var_3440 = relay.var("var_3440", dtype = "int32", shape = (168, 4))#candidate|3440|(168, 4)|var|int32
const_3441 = relay.const([-1.249616,-8.783494,0.769396,3.119237,-7.162430,8.021045,-5.805748,1.934677,3.085323,5.293170,-6.705673,4.112978,6.653993,-9.529656,8.710049,-7.554071,1.176347,1.834913,-9.578641,4.870588,6.283391,-6.461299,0.371133,6.354986,4.275591,-9.339920,1.905136,-2.046198,-7.414965,3.327564,7.965415,9.108965,-8.396484,6.223354,1.328736,3.108831,5.094003,0.709668,-5.485224,-2.553855,8.139225,5.299478,-0.745386,6.442238,6.010181,-6.852682,5.542854,7.123088], dtype = "float32")#candidate|3441|(48,)|const|float32
var_3442 = relay.var("var_3442", dtype = "bool", shape = (2912,))#candidate|3442|(2912,)|var|bool
const_3443 = relay.const([[3,7,7,10,-9,9,3,5,-2,1,5,9,5,-4,-5,-4,4,-10,5,2,-10,-7,9,-4,-5,8,-9,1,4,9,-2,2,6,-6,3,-4,-9,6,3,10,-9,5,-3,5,2,9,-9,-9,-2,-4,2,-9,-1,10,-7,3,9,5,6,1,6,-3,2,7,-8,-10,3,3,4,-9,6,-10,-9,6,5,-5,-9,5,2,-5,5,1,5,-1,1,-2,1,1,7,7,-7,4,-1,-5,-10,-3,4,-2,-2,-7,-2,-10,-3,3,10,-1,-2,-1,5,-8,-6,10,7,-10,7,-1,-8,-2,-4,10,-6,-3,7,3,-1,7,-4,-9,10,-9,7,-6,1,-6,4,10,-9,8,8,8,-4,7,1,-8,-3,8,7,5,-3,-6,8,-6,-9,-1,-10,6,-3,2,7,8,9,2,-1,5,-9,-2,-6,-4,-5,-4,5,8,1,5,-2,-9,-9,6,-9,6,1,-9,-6,-4,9,5,5,5,3,-5,-2,-7,-7,-3,-5,8,-6,-5,-9,3,-6,-3,10,-7,5,10,-10,8,-10,-6,9,1,1,8,-6,8,-9,-2,-7,4,3,-1,8,10,2,3,10,-7,-1,-2,7,-6,3,5,-7,3,-10,-2,-6,6,-10,9,2,-2,-4,7,-6,-8,-1,8,10,9,-6,10,-5,1,-3,5,10,-8,4,6,10,-7,-4,10,-8,6,2,-7,-10,2,9,-1,-7,-3,-6,-8,-10,-9,2,8,10,4,-10,9,-9,5,8,-9,7,-5,9,-9,-10,1,8,2,5,-10],[-10,5,1,9,8,-6,8,-5,-5,-5,-3,-7,-8,-10,8,6,-10,7,-2,1,-4,2,8,-10,4,-6,-2,9,-3,-2,9,-8,10,-8,-4,10,-8,2,2,9,-7,-2,-9,8,-9,2,8,-5,-7,-1,-6,9,-5,-1,2,2,6,-6,-6,6,7,-3,10,-3,3,-8,-7,4,-5,-9,-7,-4,-5,-8,9,6,6,10,7,4,9,10,6,-8,-9,8,5,8,6,-3,-2,8,-8,5,-4,-9,9,-9,-3,8,1,7,9,10,-3,-8,-1,4,-5,-9,6,-1,5,-9,-6,-10,2,7,-5,5,-7,5,-1,9,6,6,4,-6,-9,9,4,4,-9,7,7,1,7,4,-5,-6,3,-10,9,-7,-2,4,6,-4,-1,8,-5,4,7,1,-2,-2,9,1,-9,-6,5,-9,-10,-5,-3,6,3,3,-7,1,-3,4,4,-2,4,-4,-10,7,3,8,4,-6,-6,-7,3,-6,-9,-10,6,6,10,8,-2,-9,-6,2,4,8,-7,7,-3,6,-3,-6,8,8,1,-9,10,9,6,-7,9,2,-10,-6,2,-6,-10,-2,4,6,6,10,5,4,-1,2,8,-6,5,-3,3,9,-10,4,3,-1,7,-6,3,4,3,-5,-1,1,-10,2,4,1,-4,-9,-4,7,6,-4,5,4,-5,1,8,2,8,5,3,7,-8,-4,1,-6,7,5,-7,10,-7,-7,-4,-5,1,4,4,3,10,-6,1,5,3,9,-10,-1,-1,2,-7,8,6,4,-3,-4,4,-3],[4,-4,9,-7,2,4,8,9,-4,5,-8,2,6,6,7,-7,-7,-8,-4,-5,-4,-10,-6,10,-5,-10,4,8,-7,1,6,-7,-1,-1,-1,-1,-3,9,-9,9,-6,1,-10,-1,3,-5,2,-2,-8,-7,-9,-7,-9,-4,-7,-6,-2,2,-4,-3,7,-8,9,-3,4,7,8,6,10,8,2,10,-1,-8,-5,3,-8,-10,-10,-5,3,-6,7,10,3,-7,-4,-1,-9,-9,1,-6,-1,-5,1,5,-1,7,-4,-5,9,-2,-9,9,1,2,-9,10,-7,3,6,-6,-1,-4,1,2,3,4,-4,-2,10,8,4,-1,4,1,-2,-6,9,7,-3,-2,10,10,9,-2,6,10,7,-1,5,-2,8,-1,-10,-8,7,1,8,-3,5,-7,5,-1,7,5,5,-1,5,-3,-10,10,-3,-7,6,7,5,-4,-1,3,8,-10,-3,-9,2,-5,-5,2,-6,8,-8,3,10,4,-4,-9,-6,7,-1,10,-10,-10,10,2,8,9,-8,-9,-10,10,-3,8,10,-1,-4,6,5,-9,-7,-2,5,-1,4,1,-7,9,2,1,3,-4,-4,10,-6,6,-2,-8,-8,9,-3,5,5,-1,-1,10,-4,-8,-7,-8,9,-6,-2,9,-5,3,3,7,-4,-7,-1,-7,-1,3,-7,-1,-7,-7,-3,-1,7,6,4,5,4,-2,-9,1,-6,-10,-7,9,-9,-3,3,1,-9,-9,4,8,-8,-2,1,-8,8,-10,-10,7,5,4,-7,9,5,7,-2,5,7,-6,3,-5,-4,3],[6,-5,-3,1,5,-4,-8,8,-7,-1,-2,-5,10,5,-7,-8,-10,5,2,-1,-10,5,-7,-9,8,1,6,7,7,10,10,-8,10,4,-3,-9,2,-2,-9,-5,10,8,-1,-4,9,-4,-1,-9,-10,-5,10,10,7,10,3,-2,-1,-1,-9,5,-8,-7,3,-1,1,-10,9,-4,9,2,-1,-7,7,7,4,4,-2,2,-8,-10,1,1,-1,-6,-1,4,-3,6,-10,7,-6,-7,-3,4,2,-10,8,-2,-8,-9,7,1,-6,-3,2,2,3,6,8,5,6,4,-9,-2,5,6,-5,-3,5,-7,5,5,-9,-4,-3,-9,-6,-4,9,10,7,7,2,-1,7,-4,-7,2,9,5,7,-10,6,8,10,-3,-5,-9,4,5,-7,-6,9,-2,-4,-10,-10,-5,-6,6,-2,-3,1,7,-1,5,-3,-4,-8,9,-5,4,1,4,4,-3,8,7,-7,3,7,8,10,10,-2,10,2,-5,-7,10,10,10,-1,-7,9,8,1,-6,2,9,-9,-1,4,1,4,3,-7,4,-9,-6,-3,6,2,7,8,-8,-4,7,5,-1,1,5,-6,6,9,6,8,-8,-2,6,10,8,-3,3,-2,6,-8,-1,-1,-2,9,-4,9,-9,8,2,9,1,-6,-7,9,-2,-8,3,-8,-10,4,3,-6,4,-8,-4,-8,-9,9,3,-3,5,5,-9,-5,-1,-2,2,-9,-4,3,-5,2,5,2,-9,2,6,-4,-4,3,7,2,-5,-4,-7,6,-9,-8,10,-4,-6,-5,-8],[7,-7,7,-6,-1,-7,10,5,-10,4,1,-9,-5,5,-5,-10,-3,3,-10,9,9,-8,2,5,-10,-1,7,9,-2,3,-5,2,-9,-10,-5,10,-6,5,6,1,2,-10,-1,10,-3,-3,-5,8,1,5,-10,-1,5,-4,7,8,9,-8,-7,4,-1,-8,-1,2,-8,-7,2,-5,-6,-10,6,4,-6,-4,1,10,-4,-8,-7,-6,-5,-3,2,4,7,-3,-1,-8,9,9,1,-10,10,-9,-6,3,-9,8,4,-1,5,-4,9,5,-6,-6,6,2,-3,4,-8,-3,-3,10,3,8,3,8,6,2,8,8,5,9,-1,-7,1,-5,1,2,7,5,4,6,7,-3,-5,10,-1,7,-3,10,-6,-8,2,-2,4,3,-3,9,4,-8,4,-10,-6,-8,3,4,-7,-6,-6,10,-8,-7,9,-2,9,3,-7,-10,-9,-3,-8,-2,1,2,6,5,-4,-6,10,5,9,5,-2,-10,-3,5,-2,-4,3,-2,1,-5,-2,7,3,5,1,-10,5,6,-5,-9,8,-1,3,-1,1,-9,-1,8,8,5,-1,4,7,6,-1,-8,-2,9,2,-10,-10,-9,5,4,-9,3,-6,-10,5,2,10,-4,-10,-10,4,7,-10,4,6,-9,9,-6,6,-7,-1,8,10,6,8,-2,5,-8,-10,10,-10,-10,8,-3,4,-9,8,8,1,8,1,4,1,-3,-4,-6,2,3,-4,6,6,-4,-3,2,8,5,-10,-5,1,-4,1,-1,-8,2,-3,-3,-6,-3,1,4,5,-1],[10,-8,4,-8,-3,-7,-7,6,-1,-1,6,-7,1,-8,-3,-9,-5,-6,8,5,4,2,-2,3,7,-2,10,-2,3,5,-1,8,1,6,-9,3,-2,5,3,-9,2,5,-1,10,1,9,-2,-9,-3,4,-5,-3,2,-4,8,7,-7,3,-3,1,10,7,8,-5,-10,-3,6,5,6,4,5,5,8,-9,10,-7,1,-2,-10,10,-8,7,8,3,-3,9,10,9,1,1,9,10,1,-9,-1,-3,9,-2,-3,-3,3,6,8,-3,5,-8,1,-4,-2,-5,9,1,-9,-7,9,1,-5,-7,-2,10,6,2,8,2,-7,4,-7,6,-9,10,-6,-1,-10,2,3,-1,-1,-6,9,10,9,3,-8,-3,3,-6,4,10,8,-8,-5,7,2,-7,-5,6,-1,-9,-8,-8,6,10,9,-8,3,5,-4,5,10,-6,9,9,1,-8,2,1,-8,-2,4,-6,-5,-4,5,-3,-9,10,-3,7,10,-4,-1,-2,10,10,5,1,-6,9,4,6,2,-3,-8,-8,6,-1,-1,-10,9,4,-3,-4,-2,10,-4,9,-6,-9,-3,-1,9,9,-6,-10,6,-9,-1,-8,3,-8,6,-10,-2,-7,8,-5,1,-8,3,-2,-3,8,1,6,-5,2,2,6,-3,-8,-2,-7,-8,-9,-2,-8,1,1,-3,7,-1,-1,-1,8,9,-4,-10,-3,-7,-9,-3,-5,4,-6,3,5,10,-9,-1,4,5,-1,10,-5,-8,3,-3,6,4,-4,-3,1,3,6,-8,-5,10,-10,-4,5]], dtype = "uint32")#candidate|3443|(6, 300)|const|uint32
call_3437 = relay.TupleGetItem(func_2125_call(relay.reshape(var_3438.astype('float64'), [7, 8, 1]), relay.reshape(const_3439.astype('float64'), [7, 8, 8]), relay.reshape(var_3440.astype('int32'), [672,]), relay.reshape(const_3441.astype('float32'), [48,]), relay.reshape(var_3442.astype('bool'), [2912,]), relay.reshape(const_3443.astype('uint32'), [1800,]), ), 4)
call_3444 = relay.TupleGetItem(func_2133_call(relay.reshape(var_3438.astype('float64'), [7, 8, 1]), relay.reshape(const_3439.astype('float64'), [7, 8, 8]), relay.reshape(var_3440.astype('int32'), [672,]), relay.reshape(const_3441.astype('float32'), [48,]), relay.reshape(var_3442.astype('bool'), [2912,]), relay.reshape(const_3443.astype('uint32'), [1800,]), ), 4)
output = relay.Tuple([call_3432,call_3437,var_3438,const_3439,var_3440,const_3441,var_3442,const_3443,])
output2 = relay.Tuple([call_3433,call_3444,var_3438,const_3439,var_3440,const_3441,var_3442,const_3443,])
func_3451 = relay.Function([var_3438,var_3440,var_3442,], output)
mod['func_3451'] = func_3451
mod = relay.transform.InferType()(mod)
mutated_mod['func_3451'] = func_3451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3451_call = mutated_mod.get_global_var('func_3451')
var_3453 = relay.var("var_3453", dtype = "float64", shape = (56,))#candidate|3453|(56,)|var|float64
var_3454 = relay.var("var_3454", dtype = "int32", shape = (168, 4))#candidate|3454|(168, 4)|var|int32
var_3455 = relay.var("var_3455", dtype = "bool", shape = (2912,))#candidate|3455|(2912,)|var|bool
call_3452 = func_3451_call(var_3453,var_3454,var_3455,)
output = call_3452
func_3456 = relay.Function([var_3453,var_3454,var_3455,], output)
mutated_mod['func_3456'] = func_3456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2724_call = mod.get_global_var('func_2724')
func_2725_call = mutated_mod.get_global_var('func_2725')
call_3458 = func_2724_call()
call_3459 = func_2724_call()
func_2817_call = mod.get_global_var('func_2817')
func_2818_call = mutated_mod.get_global_var('func_2818')
call_3464 = func_2817_call()
call_3465 = func_2817_call()
output = relay.Tuple([call_3458,call_3464,])
output2 = relay.Tuple([call_3459,call_3465,])
func_3480 = relay.Function([], output)
mod['func_3480'] = func_3480
mod = relay.transform.InferType()(mod)
mutated_mod['func_3480'] = func_3480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3480_call = mutated_mod.get_global_var('func_3480')
call_3481 = func_3480_call()
output = call_3481
func_3482 = relay.Function([], output)
mutated_mod['func_3482'] = func_3482
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3555 = relay.var("var_3555", dtype = "float64", shape = (3, 6, 6))#candidate|3555|(3, 6, 6)|var|float64
var_3556 = relay.var("var_3556", dtype = "float64", shape = (3, 6, 6))#candidate|3556|(3, 6, 6)|var|float64
bop_3557 = relay.multiply(var_3555.astype('float64'), relay.reshape(var_3556.astype('float64'), relay.shape_of(var_3555))) # shape=(3, 6, 6)
output = bop_3557
output2 = bop_3557
func_3561 = relay.Function([var_3555,var_3556,], output)
mod['func_3561'] = func_3561
mod = relay.transform.InferType()(mod)
var_3562 = relay.var("var_3562", dtype = "float64", shape = (3, 6, 6))#candidate|3562|(3, 6, 6)|var|float64
var_3563 = relay.var("var_3563", dtype = "float64", shape = (3, 6, 6))#candidate|3563|(3, 6, 6)|var|float64
output = func_3561(var_3562,var_3563,)
func_3564 = relay.Function([var_3562,var_3563,], output)
mutated_mod['func_3564'] = func_3564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2701_call = mod.get_global_var('func_2701')
func_2703_call = mutated_mod.get_global_var('func_2703')
call_3646 = func_2701_call()
call_3647 = func_2701_call()
func_2512_call = mod.get_global_var('func_2512')
func_2514_call = mutated_mod.get_global_var('func_2514')
call_3658 = func_2512_call()
call_3659 = func_2512_call()
func_1684_call = mod.get_global_var('func_1684')
func_1688_call = mutated_mod.get_global_var('func_1688')
var_3666 = relay.var("var_3666", dtype = "float32", shape = (231,))#candidate|3666|(231,)|var|float32
var_3667 = relay.var("var_3667", dtype = "int8", shape = (480,))#candidate|3667|(480,)|var|int8
const_3668 = relay.const([[True,True,True,True,False,False,False,False,False,True,False,False,True,True,True,False,True,True,False,True,True,True,False,False,True,False,False,True],[False,True,True,False,False,True,True,False,True,True,True,False,False,True,False,False,False,True,False,True,True,False,False,False,False,True,True,True],[True,True,False,False,False,False,False,False,True,True,True,False,True,False,False,True,True,True,True,True,False,False,True,True,False,True,False,False],[False,True,True,False,False,False,False,False,False,False,False,True,True,True,True,False,True,False,False,False,True,True,False,True,True,True,True,False],[False,True,False,True,False,False,True,False,False,True,False,False,True,False,True,False,False,False,True,True,False,True,False,True,False,False,True,False],[True,False,False,True,True,False,False,True,False,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,True,False,False],[True,True,False,False,True,False,True,False,True,False,True,True,True,False,False,False,True,False,True,False,False,True,False,False,False,True,False,False],[False,False,True,True,True,True,True,False,False,False,False,True,False,True,False,False,True,False,False,False,True,True,True,True,True,True,True,True],[False,True,False,False,False,True,True,True,False,False,False,False,False,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True],[False,True,True,False,True,True,False,True,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,True,False,False,False,True],[True,True,False,True,False,True,True,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,True,True,True,False,False,True],[False,False,False,False,True,True,True,False,False,True,True,True,False,False,True,True,True,False,False,False,False,True,True,True,True,False,False,False],[False,False,True,True,False,False,True,False,True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,True,True,False,False,False],[False,False,False,True,False,True,False,False,True,True,False,False,True,False,False,True,False,False,True,True,False,False,False,True,True,True,False,False],[True,False,False,True,False,False,False,False,False,False,False,True,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,False],[False,False,True,True,False,True,False,False,False,True,False,False,True,False,True,True,True,True,False,True,True,False,False,False,True,True,True,False],[False,True,False,False,True,True,True,True,True,False,True,True,True,True,True,False,True,False,True,True,False,True,False,True,True,False,True,False],[False,False,False,False,True,True,True,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,False,False,True,False,True,False],[False,True,True,False,True,True,True,True,False,False,True,True,False,True,False,True,True,True,False,True,False,False,False,False,False,False,False,True],[False,False,True,False,True,False,True,False,False,False,True,False,False,True,True,False,False,False,True,True,True,False,False,True,False,False,False,False],[False,False,True,False,False,True,True,True,True,False,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,False,False,False],[True,False,True,True,False,False,False,True,True,True,False,True,True,False,False,True,False,False,True,False,False,True,True,True,True,True,False,True],[True,False,False,False,False,True,False,False,True,False,True,True,True,False,False,False,False,False,True,False,True,False,True,True,True,False,False,True],[True,False,False,False,False,False,True,False,True,True,True,True,True,False,False,False,False,False,False,True,False,True,True,True,True,False,False,False],[False,True,True,True,True,False,False,False,False,True,False,False,False,True,True,True,False,True,True,False,True,True,True,True,False,True,True,True],[True,True,True,False,False,True,True,False,True,True,False,True,False,False,True,False,False,False,True,False,True,False,False,False,True,False,False,True],[True,True,False,False,False,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,True,False,True,True,False,False,True,False],[False,True,True,True,False,False,True,True,False,False,False,True,False,True,True,True,False,False,True,True,True,False,True,True,False,False,False,False],[False,True,False,False,True,False,True,True,False,True,False,False,True,False,True,True,True,False,False,True,False,False,True,False,False,False,True,False],[False,True,False,True,False,True,True,True,True,True,True,True,False,True,True,True,False,False,False,True,False,False,True,False,False,False,False,False],[False,True,False,False,False,True,True,True,False,True,False,True,False,True,False,False,True,True,True,True,True,True,False,True,True,True,True,False],[True,False,False,True,True,True,False,False,False,True,True,False,False,True,True,False,True,True,False,False,False,True,True,True,False,True,False,False],[True,True,False,False,True,False,False,True,True,False,True,True,True,False,True,False,True,False,False,False,True,True,False,True,False,True,False,True],[True,False,True,False,False,True,False,True,True,False,False,True,False,True,False,False,True,False,False,True,False,False,True,False,True,False,True,False],[True,False,True,False,False,False,False,False,True,True,False,False,True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,False],[False,False,False,True,False,True,False,False,True,False,True,False,True,True,False,True,True,False,True,True,False,True,True,False,True,True,False,True],[True,True,True,True,True,True,True,True,False,True,True,True,True,False,True,True,True,False,False,True,False,True,False,False,False,True,False,True],[True,False,False,False,True,False,False,False,True,True,True,False,False,True,True,True,True,True,False,True,True,False,False,True,True,False,True,True],[False,True,False,True,True,True,True,True,True,True,True,False,False,True,False,False,False,False,False,True,True,False,False,False,True,False,True,False],[True,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,False,True,False,False,True,False,True,False,False,False,False,True],[False,True,False,True,True,False,False,False,False,False,True,False,False,False,False,True,True,True,False,True,True,False,True,False,False,True,True,True],[True,True,False,True,True,False,True,False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,True,False,False,True,False,False],[False,True,True,True,True,False,False,False,False,True,False,True,True,True,False,True,True,True,True,False,False,False,False,True,True,True,True,True],[False,False,False,False,True,True,True,False,True,False,False,False,True,True,True,False,False,True,True,False,False,False,False,False,False,False,False,False],[True,True,True,False,True,True,False,True,True,False,True,False,False,False,False,True,True,True,False,True,False,True,True,False,False,True,True,False],[True,True,False,True,False,False,True,False,True,True,True,False,True,False,True,True,False,True,True,True,True,True,True,True,False,False,False,False],[False,True,True,True,False,True,False,False,True,True,False,True,True,True,True,False,False,False,False,False,False,True,False,True,False,True,False,False],[True,False,True,True,True,False,True,True,True,True,False,True,True,False,False,False,False,True,False,False,False,False,False,False,True,False,True,True],[True,True,False,True,False,True,False,True,True,True,True,False,True,True,True,False,True,True,False,True,True,False,True,True,True,False,True,False],[False,False,False,False,True,False,True,True,True,True,True,False,True,False,False,False,True,False,False,False,True,False,False,False,False,True,True,True],[True,False,False,False,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,True,True,False,True,True,False,True,False],[True,True,True,True,True,True,True,False,True,True,False,True,False,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False],[False,True,False,True,False,False,False,True,True,True,True,True,False,True,False,False,True,True,True,True,False,True,True,True,False,True,False,True],[True,True,False,True,False,False,True,False,False,True,False,False,True,True,True,True,True,True,False,False,False,True,True,True,False,False,False,False],[False,False,False,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,False,True,True,False,True,False,True,False,True,True],[True,True,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,True,False,True,False,True,True,False,True,False],[False,False,True,True,False,True,False,False,False,True,False,False,False,False,False,False,False,True,True,False,True,False,True,True,False,False,False,True],[False,False,False,False,False,True,False,False,False,False,False,True,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,True],[True,False,True,True,False,True,True,True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False,False,False,True,False],[True,True,True,False,True,False,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,False,True],[True,True,True,False,False,False,False,True,True,True,True,False,True,False,False,True,True,True,True,True,False,True,False,False,False,True,False,False],[False,False,True,True,True,False,True,True,True,True,True,False,False,False,False,True,True,True,True,False,False,False,True,True,True,False,True,True],[True,False,False,True,False,True,False,False,False,True,True,True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,False,False],[True,True,False,False,True,False,True,False,True,True,False,True,False,True,False,False,False,True,False,True,True,False,True,True,False,True,False,True],[False,False,False,False,False,False,False,True,False,False,True,True,True,True,True,False,True,True,False,True,True,True,False,False,True,True,True,True],[False,False,True,False,False,True,False,False,True,True,False,True,True,True,False,False,True,True,False,False,True,True,True,False,False,True,False,True],[False,True,False,False,True,True,False,False,False,True,False,True,False,False,False,True,False,True,True,True,False,False,True,True,True,False,True,True],[True,True,False,True,True,False,True,False,False,True,False,False,False,True,False,False,True,False,True,True,True,True,False,False,True,True,True,False],[True,True,True,False,False,True,True,True,True,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,True,True,False,False],[False,True,False,False,False,True,False,True,False,False,False,False,False,False,True,False,True,True,True,False,True,False,True,False,False,False,False,False],[True,False,False,True,True,True,True,False,False,False,True,True,False,True,True,False,False,False,True,True,False,False,True,True,False,True,True,False],[True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,True,True,False,True,True,True,False,False,True,False,False,False,False],[True,False,True,False,True,True,False,True,False,True,False,False,False,True,True,True,True,False,False,False,True,False,False,False,False,False,True,True],[False,True,True,True,True,False,True,True,False,True,False,False,True,False,True,True,True,False,True,False,False,True,False,True,True,False,True,False],[True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,True,False,False,False,True,False,True,True,True,True,False,False,False],[False,False,False,True,False,True,True,False,False,False,False,True,False,False,False,False,True,True,True,True,False,False,True,False,True,False,True,False],[False,False,True,True,False,True,False,False,True,True,True,True,True,True,False,False,True,False,False,False,True,False,False,True,False,True,False,True],[True,True,False,False,True,True,True,True,False,True,False,True,True,True,False,False,False,False,False,True,False,True,False,False,True,False,True,True],[True,True,False,False,True,False,False,False,True,True,False,False,True,False,True,False,True,False,False,True,False,True,False,True,False,False,True,True],[False,False,False,True,False,False,False,True,True,False,True,False,False,True,False,True,True,False,True,False,False,True,True,False,False,False,True,False],[False,False,True,True,True,True,False,True,False,False,False,True,True,True,True,True,True,False,False,False,False,True,True,False,False,False,False,True],[False,False,True,True,False,True,False,True,False,False,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,False,True,False],[True,True,True,True,True,True,False,False,False,False,True,False,True,False,True,False,False,False,False,False,True,True,True,False,False,True,True,False],[True,False,False,False,False,False,False,True,True,False,True,True,True,True,True,False,True,False,False,True,True,False,False,False,True,True,True,True],[False,False,True,False,True,True,False,True,True,False,False,False,True,False,True,False,True,True,False,False,True,False,True,False,False,True,True,True],[True,False,False,True,False,True,True,True,False,False,False,False,False,True,False,True,True,False,True,False,True,True,False,False,True,True,True,True],[True,False,False,False,False,False,True,False,True,True,False,False,True,False,False,True,True,False,True,False,False,False,False,True,False,False,False,True],[False,True,True,True,True,True,True,True,False,False,True,True,True,True,True,False,False,True,False,True,False,True,False,False,True,False,False,True],[True,False,True,True,True,False,False,False,True,True,True,True,True,False,True,True,False,False,True,False,False,True,True,False,False,True,False,False],[False,False,True,True,False,False,False,True,False,False,True,False,True,False,True,False,True,False,True,True,True,True,True,True,False,False,True,True],[False,True,True,False,False,False,True,False,True,True,False,True,True,True,True,False,False,True,False,True,True,False,False,False,True,True,True,True],[True,False,False,True,False,True,True,False,False,False,False,True,True,False,False,False,False,False,False,False,True,True,True,False,True,True,True,False],[False,False,True,True,True,False,True,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True],[False,True,True,False,False,True,True,True,True,False,False,False,True,True,False,False,False,False,False,False,True,True,False,False,True,False,False,True],[True,True,True,True,False,False,True,False,True,True,True,False,True,True,True,False,False,True,False,True,True,True,True,True,False,False,True,True],[False,False,True,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,False,False,False,False,True,False,True,False],[False,False,True,False,False,False,False,True,False,False,True,True,True,True,True,True,False,True,False,True,True,False,True,True,True,True,True,False],[True,False,False,True,True,False,False,True,False,False,True,True,False,False,False,True,True,True,False,True,False,True,True,True,True,False,True,False],[True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,False,True,True,True,False,True,True,False,False,False,False,False],[False,True,False,True,True,True,False,False,True,True,False,False,True,False,False,False,False,True,False,True,False,True,False,False,False,True,True,True],[True,True,True,True,False,True,True,True,True,True,False,False,False,False,False,False,False,True,False,True,False,False,False,True,True,False,True,False],[False,False,True,True,True,False,True,True,True,False,True,False,True,True,False,False,True,True,False,False,False,False,True,False,True,True,True,False],[True,True,False,True,True,True,True,True,True,False,False,True,False,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True],[False,True,True,True,False,False,True,True,True,False,False,True,False,True,False,False,False,True,True,True,True,True,True,False,False,True,True,False]], dtype = "bool")#candidate|3668|(104, 28)|const|bool
call_3665 = relay.TupleGetItem(func_1684_call(relay.reshape(var_3666.astype('float32'), [3, 11, 7]), relay.reshape(var_3667.astype('int8'), [8, 60]), relay.reshape(const_3668.astype('bool'), [1, 2912]), ), 1)
call_3669 = relay.TupleGetItem(func_1688_call(relay.reshape(var_3666.astype('float32'), [3, 11, 7]), relay.reshape(var_3667.astype('int8'), [8, 60]), relay.reshape(const_3668.astype('bool'), [1, 2912]), ), 1)
uop_3670 = relay.sqrt(const_3668.astype('float32')) # shape=(104, 28)
uop_3673 = relay.sqrt(call_3646.astype('float32')) # shape=(4, 15, 15)
uop_3675 = relay.sqrt(call_3647.astype('float32')) # shape=(4, 15, 15)
uop_3681 = relay.rsqrt(uop_3670.astype('float64')) # shape=(104, 28)
var_3697 = relay.var("var_3697", dtype = "float64", shape = (104, 28))#candidate|3697|(104, 28)|var|float64
bop_3698 = relay.right_shift(uop_3681.astype('uint32'), relay.reshape(var_3697.astype('uint32'), relay.shape_of(uop_3681))) # shape=(104, 28)
bop_3702 = relay.bitwise_and(bop_3698.astype('uint64'), relay.reshape(uop_3670.astype('uint64'), relay.shape_of(bop_3698))) # shape=(104, 28)
output = relay.Tuple([call_3658,call_3665,var_3666,var_3667,uop_3673,bop_3702,])
output2 = relay.Tuple([call_3659,call_3669,var_3666,var_3667,uop_3675,bop_3702,])
func_3706 = relay.Function([var_3666,var_3667,var_3697,], output)
mod['func_3706'] = func_3706
mod = relay.transform.InferType()(mod)
var_3707 = relay.var("var_3707", dtype = "float32", shape = (231,))#candidate|3707|(231,)|var|float32
var_3708 = relay.var("var_3708", dtype = "int8", shape = (480,))#candidate|3708|(480,)|var|int8
var_3709 = relay.var("var_3709", dtype = "float64", shape = (104, 28))#candidate|3709|(104, 28)|var|float64
output = func_3706(var_3707,var_3708,var_3709,)
func_3710 = relay.Function([var_3707,var_3708,var_3709,], output)
mutated_mod['func_3710'] = func_3710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2534_call = mod.get_global_var('func_2534')
func_2535_call = mutated_mod.get_global_var('func_2535')
call_3725 = relay.TupleGetItem(func_2534_call(), 1)
call_3726 = relay.TupleGetItem(func_2535_call(), 1)
func_1124_call = mod.get_global_var('func_1124')
func_1130_call = mutated_mod.get_global_var('func_1130')
var_3729 = relay.var("var_3729", dtype = "float64", shape = (165,))#candidate|3729|(165,)|var|float64
var_3730 = relay.var("var_3730", dtype = "int8", shape = (8, 60))#candidate|3730|(8, 60)|var|int8
const_3731 = relay.const([-8,7,1,1,-1,8,7,3,3,3,-9,-3,5,-9,-2,-4,7,10,-1,-7,6,-8,1,4,-1,8,-1,8,7,-2,4,-3,-9,-1,6,3,-1,-4,6,-6,6,-6,-9,2,2,8,1,-8,-6,3,5,1,-10,-10,-4,3,2,-8,4,8,-3,-3,-8,9,10,-4,-9,-2,-4,7,-1,-10,10,6,8,-1,10,9,6,10,1,10,-2,1], dtype = "int32")#candidate|3731|(84,)|const|int32
const_3732 = relay.const([2,8,6,9,-1,8,10,-7,6,7,9,1,-10,-4,-9,-8,-4,4,-4,4,10,7,-9,-10,-8,-2,-5,-8,6,-5,-6,7,-9,2,1,-1,7,2,-4,1,-9,9,-6,10,-1,-8,-10,-9,-5,4,-6,-9,-3,-8,-5,-9,4,10,-6,-5,-9,-4,-9,10,3,-9,1,3,-1,10,-2,10,-10,-7,3,3,-6,-1,-1,6,-4,-4,-5,8,-8,9,1,9,10,-10,-9,-6,-2,-9,-7,7,-1,8,-8,9,-9,7,8,3,-3,2,6,6,-5,8,-1,7,6,8,-4,-9,5,-4,3,10,10,7,-2,-1,7,10,6,9,-3,-7,4,-9,-5,2,10,-3,6,4,2,-6,7,-8,3,9,2,2,-6,-5,-4,9,10,4,-4,5,-6,-7,-7,7,2,-6,4,10,-7,-10,-1,4,-1,-7,-7,-2,-3,5,6,2,10,2,-5,3,-1,-4,-2,-4,-7,9,-7,-8,-2,2,6,5,1,-9,4,-8,-7,-7,-1,1,6,-5,-2,1,5,-1,-9,-7,6,7,-10,-2,9,5,10,9,7,-7,6,-3,5,-4,-2,5,6,5,6,2,-7,-7,-4,-5,2,-10,-1,-1,-8,-1,5,6,7,-9,1,10,10,-6,-4,5,-2,4,7,2,-2,6,10,-9,3,9,9,1,5,-4,-8,-4,-2,-6,8,6,4,5,2,-8,-2,-1,6,-2,9,1,5,-10,8,7,7,-5,-3,-2,6,2,-8,-1,-6,7,-1,5,-6,2,-2,-9,2,7,-4,-10,2,10,-6,-6,6,-10,-4,10,1,-5,10,-1,7,8,8,4,4,9,7,-4,1,-9,-8,-4,-2,1,2,-6,1,-10,4,10,10,-9,7,9,7,10,8,6,2,1,1,-2,-1,-1,8,2,1,2,-5,3,-10,9,8,5,-5,3,-6,-6,7,2,7,3,5,5,6,-2,-10,4,8,-7,8,9,-4,10,2,-9,6,-8,-7,3,-10,2,7,7,7,-8,-3,8,-4,3,8,7,-5,-7,10,8,6,-10,-5,-8,-1,7,5,-5,4,7,1,-8,-8,9,-6,8,6,-4,-4,-5,-1,3,8,7,8,-3,-7,-5,7,-5,-8,2,-2,5,9,3,2,7,5,-1,-9,4,-5,-3,1,-5,2,3,4,-9,9,4,-1,-3,-7,1,-9,4,-2,-8,6,1,1,-1,3,-1,-4,-4,-7,1,-1,2,5,-8,2,9,-9,5,6,8,-7,-4,3,-6,-6,8,7,-9,-7,-1,-3,6,-3,-4,10,8,1,6,1,8,-9,3,6,10,9,2,-2,-3,-3,3,9,9,-5,-5,9,2,-10,5,8,-9,9,-10,2,-7,10,-6,-3,-2,4,-5,-3,-10,-3,-6,4,-2,7,-5,3,3,4,-6,-8,5,8,-4,8,-1,-1,-6,4,-8,-7,-1,-7,-8,8,5,-4,8,4,-2,-6,-5,-2,3,-8,9,4,-8,6,1,1,2,8,-7,9,-7,2,3,-3,-8,-7,-6,8,-3,9,-10,10,6,-9,-2,-4,-7,-1,8,7,4,-4,-7,6,7,-4,8,9,3,8,-10,4,-9,-8,-8,-5,-10,-5,-3,9,-6,9,4,-9,7,2,-2,-5,-1,7,9,-4,-1,8,-9,6,-9,-1,-2,-1,2,6,-2,-2,-3,4,1,5,-6,9,-1,3,7,-2,-8,10,8,1,-7,5,-6,-6,-7,-10,-3,10,-4,-3,-1,-2,9,9,9,9,7,-10,1], dtype = "int32")#candidate|3732|(672,)|const|int32
call_3728 = relay.TupleGetItem(func_1124_call(relay.reshape(var_3729.astype('float64'), [11, 5, 3]), relay.reshape(var_3730.astype('int8'), [480,]), relay.reshape(const_3731.astype('int32'), [84, 1]), relay.reshape(const_3732.astype('int32'), [672,]), ), 0)
call_3733 = relay.TupleGetItem(func_1130_call(relay.reshape(var_3729.astype('float64'), [11, 5, 3]), relay.reshape(var_3730.astype('int8'), [480,]), relay.reshape(const_3731.astype('int32'), [84, 1]), relay.reshape(const_3732.astype('int32'), [672,]), ), 0)
func_2125_call = mod.get_global_var('func_2125')
func_2133_call = mutated_mod.get_global_var('func_2133')
const_3738 = relay.const([3.955603,1.485527,1.735103,4.403219,0.834023,5.901835,2.874958,-2.824879,-7.959202,6.197783,-5.933254,2.729373,-8.966651,-4.074571,1.842819,-2.407115,-8.744400,-8.759859,1.788893,-5.266943,7.001250,-1.289030,8.367712,-9.482782,7.524907,1.244936,4.163594,-2.872586,-0.745338,6.739826,-6.894124,-9.959906,0.465920,-5.123377,-1.015686,-8.779387,9.194674,-2.314709,6.169158,-7.914212,6.192984,-4.579303,-5.006168,-1.864035,-6.550327,-2.101758,-7.759817,7.283992,5.254792,-1.309397,-1.987634,4.586676,9.257841,-3.245869,-1.625730,-6.154021], dtype = "float64")#candidate|3738|(56,)|const|float64
const_3739 = relay.const([1.700055,-2.403080,-4.362051,1.771897,7.970232,-3.695340,-2.954856,-6.848052,6.200097,-1.260917,5.304058,6.081770,8.177591,2.830358,4.160046,-5.642996,4.268904,-0.441117,6.586537,-0.328758,-4.483914,3.805636,8.011123,-1.410284,8.984841,-1.893155,2.028652,-4.823154,3.966810,8.789690,3.462421,5.412173,-3.757193,-3.106817,0.186557,-5.083150,-2.010884,1.523009,6.291365,-1.525551,-4.294940,-7.744286,8.409651,1.663968,-9.346113,4.220470,-8.118536,-5.348182,-4.867321,7.620103,6.704146,8.202520,4.804183,-0.171543,-5.774965,-8.589307,1.073179,8.227163,7.091018,2.089592,9.423689,-6.327203,8.260471,7.731828,4.355828,-2.562911,-4.625052,-5.735843,-8.323494,8.265960,-4.401247,7.578196,-6.113458,-3.312652,9.857243,0.076219,-7.982567,7.624515,5.728628,8.813053,8.540633,2.699453,4.504757,9.212544,-3.528747,5.096202,-1.512492,-5.632924,9.639998,2.624999,-1.201927,0.492839,-9.865205,9.479799,2.749859,-3.297223,-2.562806,7.702362,-0.146316,1.657569,8.408827,6.468191,9.936972,-1.674836,-0.672268,-5.132903,-4.959993,3.766975,-3.764825,-1.803056,0.379616,-8.769665,2.108183,2.234941,-3.994070,-0.520524,5.649878,-3.033014,-0.299585,3.171598,-9.437477,1.382318,-0.926128,8.200546,0.946535,-3.309253,-2.207595,-8.571768,-9.378934,1.673652,-8.648933,-3.124000,5.610851,0.169477,1.145323,-5.801591,-1.335952,7.926179,-3.642857,0.147333,-6.252737,-3.814546,-4.103323,-1.248363,2.995217,3.949616,-9.710225,3.350601,-1.924365,1.699562,-3.854599,5.994046,9.273105,9.080216,0.760943,-9.182709,-7.756504,1.571051,7.318219,-2.180156,7.091460,4.744425,3.429497,-2.782696,9.062402,-4.595047,7.888078,-4.049193,-1.140456,2.502449,-9.390513,6.268471,-2.592398,6.788294,6.509633,-6.042067,5.784971,-5.005387,2.424620,3.176036,-7.868740,-6.780750,6.744777,-8.048378,-9.620006,-5.088388,7.630810,5.362447,-0.300140,-9.315891,-4.357278,-2.875072,-7.710759,4.841446,9.438264,-5.663497,-9.425286,-2.475475,6.242692,1.885433,-3.847607,-4.509441,0.567008,9.329341,-2.453507,9.521223,3.550354,-0.564502,-2.899050,0.786915,-9.752126,0.720433,-5.553596,2.072460,3.050237,9.957359,-7.047638,8.859360,9.036191,9.291314,-7.039464,7.350052,-2.051413,0.367663,8.760235,4.803921,-3.553332,-3.492973,-0.161831,-9.976128,-0.329230,5.905447,0.598032,-6.416618,5.177098,-7.620565,5.559585,2.360834,-3.961519,-7.154207,3.003305,3.506828,2.639434,-3.863545,3.155411,8.109840,-2.329518,-4.879204,1.333209,0.239663,-6.356444,7.077157,0.612965,-2.451797,1.548286,0.939209,-6.037716,5.666489,-8.628020,6.328136,-0.333166,0.324968,8.671744,5.084815,-9.874265,6.600150,-4.866480,-5.137742,-2.258471,2.931329,-3.386037,-3.138205,-7.157297,-4.772864,-3.718891,-5.091212,-5.644546,7.390825,-1.358964,-5.156877,8.710553,7.099019,-1.136520,6.080610,-6.435183,8.511171,9.552578,0.318107,2.939009,-6.206108,8.954728,-8.876483,-0.972725,4.346871,-8.277545,-3.435895,-5.371856,-0.579748,0.524692,5.379824,-5.275030,-6.299709,-9.238187,6.429018,7.393816,3.001618,7.117192,-6.179538,-5.561247,-1.326257,-9.751427,-1.250456,-4.023266,4.112929,7.916415,-7.120930,2.325911,3.214390,-8.001269,4.320269,3.053602,6.195695,1.849411,-8.382410,3.998371,-9.328023,9.191294,-2.599756,9.664959,-1.208218,-4.112386,6.777337,7.770329,-3.178398,6.378740,-8.836413,-7.367722,2.259652,8.053749,6.770716,-0.300137,-6.156422,9.354374,-5.972075,5.149917,5.416384,5.194652,9.198415,8.612771,-3.036639,-0.898031,1.016338,-2.025202,-2.765724,6.324364,4.695241,7.378498,0.190330,-2.586744,-9.098802,-7.022135,-8.578775,-5.710063,2.903526,5.629647,-6.060364,-7.234920,-2.458244,0.046123,-8.087578,1.541914,-8.514488,-9.037620,3.971650,5.476217,-7.038741,0.622494,1.438033,-8.381997,9.918712,3.522495,4.007755,-4.977026,-7.974745,-6.850676,-1.614840,-3.718404,2.033222,-1.631728,-2.515341,-9.548478,-7.980231,3.169314,6.104119,-1.540480,0.557873,-5.698778,8.963981,-2.699084,-1.683566,-3.135581,-0.450408,-1.870555,5.786170,-8.390075,-9.865579,-8.866063,-6.927173,0.371917,-4.165851,8.293604,9.976653,-1.604856,-7.967357,-6.047156,-2.424845,6.269957,-4.707884,-4.785389,-0.504352,5.916085,2.400234,1.478386,0.350464,2.428026,-6.448587,9.319580,-9.807892,-8.213664,-3.326429,-5.212946,-8.581030,-3.463563,0.503755,-3.352684,5.845873,-2.739522,-8.827194,1.300004,-1.240483,4.917436,2.131843,-5.523043,-1.507723,-9.927173,-8.606971,6.487833,-5.257625], dtype = "float64")#candidate|3739|(448,)|const|float64
var_3740 = relay.var("var_3740", dtype = "float32", shape = (48,))#candidate|3740|(48,)|var|float32
const_3741 = relay.const([True,False,True,False,False,True,False,True,False,True,False,False,False,True,True,True,True,True,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,False,True,True,True,False,False,False,False,True,False,True,True,True,True,False,True,True,False,True,False,True,False,True,False,True,True,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,True,True,True,False,True,True,False,True,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,False,False,False,True,False,False,False,True,True,True,True,True,False,False,True,False,True,False,True,True,False,True,False,False,False,False,False,False,False,False,False,True,False,False,False,True,False,False,False,True,False,True,True,False,False,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,False,True,True,False,True,False,True,False,True,False,False,False,True,False,False,False,True,False,False,False,False,True,True,True,False,False,True,True,False,True,False,False,False,True,False,True,False,True,True,True,False,True,True,True,False,False,True,True,False,False,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True,False,True,True,True,True,False,True,False,False,True,False,False,False,True,False,False,True,False,True,False,False,False,True,True,False,True,True,False,False,True,False,False,True,True,False,False,False,True,False,False,False,True,False,True,False,False,True,True,False,True,True,True,True,True,False,False,False,False,False,False,True,False,True,False,False,True,False,False,False,True,False,True,False,False,False,False,False,True,False,False,False,True,True,False,False,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,True,False,True,True,False,False,True,False,False,True,False,True,True,False,False,True,False,False,True,True,True,False,False,True,False,True,False,True,False,False,False,True,False,False,False,True,False,True,True,False,False,True,True,True,False,True,False,False,False,True,True,True,False,True,True,False,False,True,True,False,True,False,True,False,False,True,True,False,False,False,False,True,True,True,False,True,True,True,False,True,False,True,False,False,True,True,True,True,True,False,False,False,False,True,False,False,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,False,False,False,True,True,False,False,False,True,False,False,True,True,False,False,True,True,True,False,False,True,False,True,False,False,False,False,True,False,True,True,False,True,False,True,False,False,True,False,True,False,True,False,True,True,False,False,False,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,True,False,True,True,False,True,False,True,True,True,False,False,False,False,False,False,False,True,False,True,False,False,False,True,True,False,False,True,False,True,True,False,True,False,True,False,True,True,True,False,False,True,False,False,False,True,False,False,False,True,False,False,True,False,True,False,False,False,True,True,True,False,True,False,True,False,False,False,False,False,True,False,True,True,True,True,False,True,False,False,False,False,False,True,False,False,False,True,False,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,False,True,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,True,False,True,True,True,False,True,False,True,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,True,True,True,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,False,True,True,False,False,False,False,True,True,False,True,True,True,True,False,True,True,False,True,True,True,True,True,False,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,False,False,True,True,True,True,False,False,False,True,False,False,True,True,False,True,False,True,False,True,True,False,False,False,False,False,True,True,True,False,False,True,False,True,False,True,False,False,False,False,False,False,False,True,True,False,False,True,True,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,True,True,True,False,True,True,False,True,True,True,False,False,False,False,True,False,False,False,True,True,True,True,True,False,True,True,True,True,True,False,False,False,True,True,False,False,False,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,False,True,False,False,True,False,False,True,False,False,True,True,False,True,True,True,False,False,True,False,False,True,False,False,False,True,False,True,True,False,False,True,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,False,True,True,False,False,False,True,False,True,False,False,False,True,False,False,False,False,False,False,False,True,True,False,True,True,True,True,False,True,True,False,True,False,True,True,False,True,False,False,False,False,False,False,True,True,False,False,True,True,False,True,False,True,True,True,True,False,True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False,False,False,True,True,False,False,False,True,True,False,False,True,False,True,True,True,False,True,True,True,True,True,True,True,False,True,False,False,True,True,False,True,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,True,False,False,True,True,True,False,True,False,False,True,True,True,False,True,False,False,False,True,True,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,False,True,True,False,True,True,True,False,False,True,True,False,True,True,False,False,False,False,True,True,True,False,False,True,False,True,True,True,True,False,True,True,True,False,True,True,True,False,True,True,True,True,False,False,False,False,True,False,False,False,False,True,False,False,True,False,True,False,True,False,False,True,False,False,True,True,True,True,False,False,False,True,True,False,False,False,False,True,False,False,True,False,False,True,False,True,False,False,True,True,False,False,False,False,False,False,False,True,True,False,True,True,True,True,False,True,True,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,True,True,True,True,False,False,False,True,True,True,False,True,False,True,False,False,False,False,True,True,True,True,False,True,False,True,False,True,True,False,True,False,True,False,False,True,False,False,False,True,True,True,True,True,False,True,True,True,True,False,False,True,True,False,False,False,True,False,True,False,False,False,False,True,False,False,True,False,False,True,True,True,False,False,False,True,True,True,False,True,False,False,False,True,False,False,True,True,False,False,True,True,False,True,False,False,False,True,False,False,True,False,False,True,False,False,False,False,False,False,True,False,False,True,True,False,True,True,True,True,True,False,False,False,False,True,False,False,False,True,False,True,True,False,True,True,True,True,True,True,False,False,True,False,True,False,True,False,True,False,False,True,True,False,True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,False,False,False,True,True,False,False,True,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,True,True,False,True,True,False,True,False,True,True,True,True,False,True,False,False,False,False,True,True,True,True,True,False,False,False,True,True,True,True,True,False,False,True,False,False,True,True,False,False,False,False,True,False,True,True,False,True,False,True,False,True,False,True,True,False,False,True,False,True,False,True,False,True,False,False,True,False,True,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,False,True,True,True,True,False,False,False,False,True,False,False,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,True,True,True,True,False,False,True,True,True,True,True,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,False,True,False,False,True,True,True,True,True,True,True,False,False,False,True,True,False,True,True,False,True,True,True,False,False,True,True,False,True,True,False,True,False,True,True,True,False,True,False,True,False,False,True,True,False,False,False,False,True,True,False,False,False,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,False,True,False,False,True,True,True,True,False,False,False,True,True,False,False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,True,True,True,True,False,False,False,False,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,False,False,False,False,False,True,False,False,False,True,True,True,True,True,False,False,True,False,True,False,False,True,False,False,True,False,False,True,False,False,True,False,False,True,True,False,True,True,True,True,True,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,True,False,False,False,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,True,True,False,False,False,False,True,False,False,False,True,False,True,True,False,False,False,False,True,True,False,True,False,False,True,False,False,True,True,False,True,False,True,True,False,True,True,True,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False,False,False,True,True,False,True,False,False,False,False,True,True,False,False,True,False,False,False,False,True,False,True,True,True,False,False,True,True,False,True,False,False,True,True,True,True,False,True,True,False,True,False,False,False,False,True,False,False,True,False,True,True,True,True,True,True,True,False,True,True,True,True,True,False,False,True,True,True,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,True,True,False,False,False,False,True,True,True,False,True,True,True,False,False,False,False,False,True,False,False,True,False,True,True,False,False,True,False,False,True,True,False,True,False,False,False,True,False,True,False,True,True,True,True,True,True,True,False,False,False,False,True,False,True,True,True,True,False,True,False,True,True,False,True,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,True,False,False,True,True,True,False,False,True,False,True,False,False,False,True,True,True,True,True,False,False,True,True,True,True,False,False,True,True,True,True,True,True,False,False,True,True,False,True,False,True,False,False,True,True,True,False,False,True,False,False,True,True,False,False,False,False,False,False,False,True,True,True,True,True,True,False,True,True,True,True,False,True,False,False,False,True,False,True,False,False,True,True,True,True,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,False,True,False,True,True,False,False,True,False,True,True,True,False,True,False,False,True,False,False,True,False,False,True,False,True,False,True,True,True,True,False,True,False,False,True,False,False,True,True,True,False,False,False,False,True,False,False,False,True,False,False,True,False,True,True,True,False,False,False,True,True,True,True,False,True,False,False,False,True,True,True,True,True,True,True,True,True,False,True,False,False,True,False,True,True,True,False,True,False,True,False,True,False,True,True,True,True,True,True,False,False,False,True,False,True,True,True,True,True,False,True,True,False,True,False,True,True,True,False,True,False,False,False,False,False,False,True,True,True,True,False,False,True,True,False,True,False,True,False,True,True,True,True,True,True,True,False,False,False,False,True,False,True,True,False,True,True,False,False,True,True,False,True,False,False,True,True,False,False,True,False,True,True,True,True,False,False,True,False,True,False,True,True,True,False,False,False,False,False,False,True,True,True,False,True,True,True,True,True,True,False,True,False,True,False,True,True,True,True,True,False,True,False,True,False,True,True,False,True,True,False,False,False,True,False,False,False,True,True,False,False,True,True,False,True,False,False,False,True,True,False,True,False,False,False,False,True,False,False,False,True,False,False,False,False,False,False,False,True,True,False,True,False,False,False,True,False,False,False,True,True,False,False,True,False,False,True,False,False,True,False,False,True,True,False,True,True,False,False,True,True,False,False,True,False,False,True,False,False,True,True,True,True,True,False,True,False,True,True,False,False,False,False,False,True,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,True,True,False,False,True,False,True,True,True,True,False,True,False,False,False,False,False,True,False,False,False,False,False,False,True,True,True,False,False,True,False,True,True,False,True,False,False,False,True,True,True,True,True,False,True,True,False,True,False,False,True,True,False,False,True,False,True,True,False,True,False,False,False,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,False,False,False,False,True,False,False,True,False,True,False,False,True,False,False,True,False,False,True,True,True,False,False,True,False,True,False,False,False,False,False,True,False,False,True,False,False,True,True,True,False,True,True,True,True,False,True,True,False,False,True,True,False,True,False,False,False,False,False,True,False,False,False,True,False,True,True,True,False,False,False,False,True,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,True,True,True,True,False,False,False,True,True,False,True,True,True,False,False,True,False,False,False,False,False,True,True,True,True,True,True,False,False,False,True,True,True,False,True,True,False,True,False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,False,True,True,False,True,True,False,False,False,True,False,True,False,True,True,False,False,True,True,True,False,False,False,False,True,True,False,True,False,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False,False,True,False,False,True,False,True,True,True,True,False,False,False,True,False,False,False,True,True,False,True,False,False,False,False,True,False,True,False,True,False,True,False,False,True,True,False,True,False,False,False,False,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,True,False,True,False,False,False,False,False,False,True,True,True,True,True,True,False,True,False,True,False,True,True,True,True,True,False,True,True,False,False,False,True,False,False,False,False,False,False,False,False,False,True,True,True,False,True,True,False,True,True,False,False,False,True,True,False,False,False,True,False,False,False,True,False,False,True,False,False,False,True,True,False,False,False,True,True,True,True,True,False,False,True,False,False,True,True,False,True,False,False,True,False,False,False,True,False,False,True,False,False,False,True,False,True,False,True,False,True,False,True,False,False,False,False,True,True,False,True,False,False,True,True,False,True,False,True,True,False,True,False,False,True,True,False,False,True,True,False,True,False], dtype = "bool")#candidate|3741|(2912,)|const|bool
var_3742 = relay.var("var_3742", dtype = "uint32", shape = (1800,))#candidate|3742|(1800,)|var|uint32
call_3737 = relay.TupleGetItem(func_2125_call(relay.reshape(const_3738.astype('float64'), [7, 8, 1]), relay.reshape(const_3739.astype('float64'), [7, 8, 8]), relay.reshape(const_3732.astype('int32'), [672,]), relay.reshape(var_3740.astype('float32'), [48,]), relay.reshape(const_3741.astype('bool'), [2912,]), relay.reshape(var_3742.astype('uint32'), [1800,]), ), 4)
call_3743 = relay.TupleGetItem(func_2133_call(relay.reshape(const_3738.astype('float64'), [7, 8, 1]), relay.reshape(const_3739.astype('float64'), [7, 8, 8]), relay.reshape(const_3732.astype('int32'), [672,]), relay.reshape(var_3740.astype('float32'), [48,]), relay.reshape(const_3741.astype('bool'), [2912,]), relay.reshape(var_3742.astype('uint32'), [1800,]), ), 4)
output = relay.Tuple([call_3725,call_3728,var_3729,var_3730,const_3731,const_3732,call_3737,const_3738,const_3739,var_3740,const_3741,var_3742,])
output2 = relay.Tuple([call_3726,call_3733,var_3729,var_3730,const_3731,const_3732,call_3743,const_3738,const_3739,var_3740,const_3741,var_3742,])
func_3749 = relay.Function([var_3729,var_3730,var_3740,var_3742,], output)
mod['func_3749'] = func_3749
mod = relay.transform.InferType()(mod)
var_3750 = relay.var("var_3750", dtype = "float64", shape = (165,))#candidate|3750|(165,)|var|float64
var_3751 = relay.var("var_3751", dtype = "int8", shape = (8, 60))#candidate|3751|(8, 60)|var|int8
var_3752 = relay.var("var_3752", dtype = "float32", shape = (48,))#candidate|3752|(48,)|var|float32
var_3753 = relay.var("var_3753", dtype = "uint32", shape = (1800,))#candidate|3753|(1800,)|var|uint32
output = func_3749(var_3750,var_3751,var_3752,var_3753,)
func_3754 = relay.Function([var_3750,var_3751,var_3752,var_3753,], output)
mutated_mod['func_3754'] = func_3754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3381_call = mod.get_global_var('func_3381')
func_3383_call = mutated_mod.get_global_var('func_3383')
call_3844 = relay.TupleGetItem(func_3381_call(), 2)
call_3845 = relay.TupleGetItem(func_3383_call(), 2)
output = relay.Tuple([call_3844,])
output2 = relay.Tuple([call_3845,])
func_3852 = relay.Function([], output)
mod['func_3852'] = func_3852
mod = relay.transform.InferType()(mod)
output = func_3852()
func_3853 = relay.Function([], output)
mutated_mod['func_3853'] = func_3853
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2278_call = mod.get_global_var('func_2278')
func_2280_call = mutated_mod.get_global_var('func_2280')
call_3862 = func_2278_call()
call_3863 = func_2278_call()
output = call_3862
output2 = call_3863
func_3888 = relay.Function([], output)
mod['func_3888'] = func_3888
mod = relay.transform.InferType()(mod)
output = func_3888()
func_3889 = relay.Function([], output)
mutated_mod['func_3889'] = func_3889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2512_call = mod.get_global_var('func_2512')
func_2514_call = mutated_mod.get_global_var('func_2514')
call_3992 = func_2512_call()
call_3993 = func_2512_call()
output = call_3992
output2 = call_3993
func_3994 = relay.Function([], output)
mod['func_3994'] = func_3994
mod = relay.transform.InferType()(mod)
output = func_3994()
func_3995 = relay.Function([], output)
mutated_mod['func_3995'] = func_3995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2783_call = mod.get_global_var('func_2783')
func_2784_call = mutated_mod.get_global_var('func_2784')
call_4001 = relay.TupleGetItem(func_2783_call(), 0)
call_4002 = relay.TupleGetItem(func_2784_call(), 0)
func_3282_call = mod.get_global_var('func_3282')
func_3284_call = mutated_mod.get_global_var('func_3284')
call_4017 = relay.TupleGetItem(func_3282_call(), 1)
call_4018 = relay.TupleGetItem(func_3284_call(), 1)
output = relay.Tuple([call_4001,call_4017,])
output2 = relay.Tuple([call_4002,call_4018,])
func_4036 = relay.Function([], output)
mod['func_4036'] = func_4036
mod = relay.transform.InferType()(mod)
output = func_4036()
func_4037 = relay.Function([], output)
mutated_mod['func_4037'] = func_4037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1759_call = mod.get_global_var('func_1759')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_4092 = func_1759_call()
call_4093 = func_1759_call()
output = relay.Tuple([call_4092,])
output2 = relay.Tuple([call_4093,])
func_4094 = relay.Function([], output)
mod['func_4094'] = func_4094
mod = relay.transform.InferType()(mod)
output = func_4094()
func_4095 = relay.Function([], output)
mutated_mod['func_4095'] = func_4095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2724_call = mod.get_global_var('func_2724')
func_2725_call = mutated_mod.get_global_var('func_2725')
call_4096 = func_2724_call()
call_4097 = func_2724_call()
uop_4098 = relay.rsqrt(call_4096.astype('float64')) # shape=(4, 15, 15)
uop_4100 = relay.rsqrt(call_4097.astype('float64')) # shape=(4, 15, 15)
output = uop_4098
output2 = uop_4100
func_4101 = relay.Function([], output)
mod['func_4101'] = func_4101
mod = relay.transform.InferType()(mod)
mutated_mod['func_4101'] = func_4101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4101_call = mutated_mod.get_global_var('func_4101')
call_4102 = func_4101_call()
output = call_4102
func_4103 = relay.Function([], output)
mutated_mod['func_4103'] = func_4103
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4118 = relay.var("var_4118", dtype = "int16", shape = (3, 12, 9))#candidate|4118|(3, 12, 9)|var|int16
var_4119 = relay.var("var_4119", dtype = "int16", shape = (3, 12, 9))#candidate|4119|(3, 12, 9)|var|int16
bop_4120 = relay.left_shift(var_4118.astype('int16'), relay.reshape(var_4119.astype('int16'), relay.shape_of(var_4118))) # shape=(3, 12, 9)
func_3042_call = mod.get_global_var('func_3042')
func_3044_call = mutated_mod.get_global_var('func_3044')
call_4135 = relay.TupleGetItem(func_3042_call(), 2)
call_4136 = relay.TupleGetItem(func_3044_call(), 2)
uop_4138 = relay.rsqrt(var_4118.astype('float64')) # shape=(3, 12, 9)
uop_4142 = relay.asinh(uop_4138.astype('float64')) # shape=(3, 12, 9)
output = relay.Tuple([bop_4120,call_4135,uop_4142,])
output2 = relay.Tuple([bop_4120,call_4136,uop_4142,])
func_4145 = relay.Function([var_4118,var_4119,], output)
mod['func_4145'] = func_4145
mod = relay.transform.InferType()(mod)
mutated_mod['func_4145'] = func_4145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4145_call = mutated_mod.get_global_var('func_4145')
var_4147 = relay.var("var_4147", dtype = "int16", shape = (3, 12, 9))#candidate|4147|(3, 12, 9)|var|int16
var_4148 = relay.var("var_4148", dtype = "int16", shape = (3, 12, 9))#candidate|4148|(3, 12, 9)|var|int16
call_4146 = func_4145_call(var_4147,var_4148,)
output = call_4146
func_4149 = relay.Function([var_4147,var_4148,], output)
mutated_mod['func_4149'] = func_4149
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4161 = relay.const([[[6,-4,-6,4,-5,8,-3],[-3,-4,10,3,-5,-3,-9],[-2,-1,-4,5,-9,8,9],[1,10,4,-3,7,4,-10],[-7,-2,-5,-9,9,-1,-4]],[[-4,6,4,-1,9,5,-3],[-7,6,2,-7,2,-6,-2],[3,7,-9,-3,10,-1,2],[-4,-5,-8,7,10,6,1],[-4,8,-9,5,9,-10,5]],[[-5,-7,2,2,-4,1,-4],[-7,9,-10,-1,6,-6,5],[2,-7,-7,-8,8,-2,-8],[8,1,8,9,1,-6,7],[9,-10,-3,10,3,2,5]],[[-4,8,6,7,9,4,7],[4,4,7,-6,10,2,-1],[3,-8,-2,8,6,-4,3],[-5,-7,-4,2,-4,-4,4],[8,-10,-3,9,-5,-3,-4]],[[5,6,10,9,-6,-7,-1],[7,-7,-1,5,5,9,-10],[-2,1,4,9,3,-7,-9],[1,7,5,2,-9,10,-10],[-6,1,-7,-9,-4,-6,-4]],[[-7,-9,-5,8,-10,-6,9],[5,-4,2,-2,10,3,-8],[10,-1,-7,7,9,-1,-8],[-8,-2,-6,5,-4,10,-6],[9,-9,-6,-7,-3,4,-2]],[[10,4,8,-2,-6,4,-2],[3,5,-4,10,7,2,4],[3,-4,7,-1,-8,9,10],[2,-8,-1,-7,-9,4,6],[7,3,7,3,7,-7,8]],[[7,-9,-9,-3,2,-5,1],[-9,5,-9,6,-6,-8,-2],[6,-2,8,-3,10,7,-8],[-5,10,-5,9,-3,-8,3],[-2,4,7,-2,-9,1,-10]]], dtype = "uint8")#candidate|4161|(8, 5, 7)|const|uint8
const_4162 = relay.const([[[9,-1,10,3,4,8,4],[-4,10,-7,-5,-1,-4,-1],[-8,-1,8,6,-6,3,-4],[-9,-7,-3,-3,6,-5,-9],[6,4,-10,2,8,7,6]],[[-5,-1,1,9,6,4,-2],[-3,-8,2,4,8,3,4],[2,-9,8,-3,-9,3,-4],[9,6,8,10,5,-3,10],[10,5,-1,9,6,10,-4]],[[-3,2,4,-4,1,2,8],[10,1,-1,2,-1,-3,2],[-4,-10,5,-1,-9,1,8],[5,-9,3,7,-6,-6,-3],[-8,6,-1,1,8,5,4]],[[7,-1,10,-1,2,7,-10],[-9,-5,8,-8,-8,7,10],[5,-9,-8,9,2,10,-10],[6,-1,-1,-1,-8,9,2],[3,-7,-8,5,9,-5,-3]],[[-7,-2,-3,7,9,-4,-10],[2,7,4,6,-10,-7,6],[-10,-6,2,-9,3,10,5],[-7,-4,-7,-6,5,-2,-4],[6,10,9,-2,-8,-7,-8]],[[-2,-10,9,10,7,8,2],[10,6,6,-9,-4,9,3],[-2,4,5,-5,-1,2,-2],[3,8,-10,7,-2,2,-9],[-9,-8,3,-7,7,3,-4]],[[8,-5,10,2,8,5,-8],[-8,-9,-9,-10,-8,-1,6],[4,8,5,-3,-7,-4,-6],[4,5,1,9,-2,2,-5],[-6,-8,-10,-6,-10,-10,6]],[[1,-3,6,-9,4,6,-8],[-6,3,1,-6,-10,5,-9],[-8,-9,9,-5,9,-1,-1],[-9,-9,-9,8,-6,10,5],[5,-10,-1,1,10,4,-10]]], dtype = "uint8")#candidate|4162|(8, 5, 7)|const|uint8
bop_4163 = relay.bitwise_xor(const_4161.astype('uint8'), relay.reshape(const_4162.astype('uint8'), relay.shape_of(const_4161))) # shape=(8, 5, 7)
func_3381_call = mod.get_global_var('func_3381')
func_3383_call = mutated_mod.get_global_var('func_3383')
call_4166 = relay.TupleGetItem(func_3381_call(), 4)
call_4167 = relay.TupleGetItem(func_3383_call(), 4)
var_4182 = relay.var("var_4182", dtype = "uint8", shape = (8, 5, 7))#candidate|4182|(8, 5, 7)|var|uint8
bop_4183 = relay.divide(const_4161.astype('float32'), relay.reshape(var_4182.astype('float32'), relay.shape_of(const_4161))) # shape=(8, 5, 7)
bop_4188 = relay.left_shift(var_4182.astype('int8'), relay.reshape(bop_4163.astype('int8'), relay.shape_of(var_4182))) # shape=(8, 5, 7)
func_3994_call = mod.get_global_var('func_3994')
func_3995_call = mutated_mod.get_global_var('func_3995')
call_4192 = func_3994_call()
call_4193 = func_3994_call()
func_3451_call = mod.get_global_var('func_3451')
func_3456_call = mutated_mod.get_global_var('func_3456')
var_4204 = relay.var("var_4204", dtype = "float64", shape = (1, 56))#candidate|4204|(1, 56)|var|float64
const_4205 = relay.const([-5,4,5,-7,-6,-5,-10,1,-10,-10,6,8,3,-4,-5,9,1,6,-5,-3,10,4,-8,1,-7,-10,-7,8,2,-3,9,6,7,-8,-5,-3,-8,-4,1,4,-6,-3,-5,-5,3,3,-9,-3,-1,1,3,10,1,8,9,4,-10,-10,-7,3,10,5,-5,10,-1,-3,-6,-6,10,1,-5,7,-1,10,2,2,-9,3,-5,-3,5,9,-2,-10,-8,-10,-7,10,-3,-10,6,-7,8,1,7,10,-2,5,5,-4,8,7,2,5,-10,2,-6,-10,-3,8,7,-3,-8,-2,-4,5,4,-9,-9,-6,9,2,-9,10,5,1,7,-2,-10,7,3,-10,-3,-5,-3,-1,9,8,8,-9,9,5,-3,10,-1,9,-8,-3,8,-3,-1,3,-10,9,2,-2,-7,4,4,-5,-10,1,5,-9,3,4,-8,5,10,7,1,3,-6,8,-3,-5,7,-1,1,5,-1,10,-6,7,-9,9,2,8,1,8,-8,8,-10,-10,-10,6,4,3,1,7,4,7,-2,-6,10,-8,10,6,9,-2,10,2,-4,-5,5,-6,-10,7,-10,4,8,8,9,7,-1,7,-6,5,-4,-6,2,7,5,-5,-8,4,-10,3,10,7,8,-3,3,-6,-8,-5,6,-6,8,7,10,-2,-6,2,-7,-5,5,1,6,4,-2,8,-2,1,4,6,9,-6,2,-3,7,6,-8,9,-6,9,3,-8,-2,5,-8,1,8,4,-3,1,-5,-3,3,8,-8,-7,-6,6,-5,3,-1,-3,-10,-10,-4,-7,7,-3,-4,2,-7,5,-6,-1,-3,6,-9,-4,6,5,5,10,-4,4,3,1,5,-3,-6,-3,9,2,8,8,-10,-5,-7,-8,-9,8,-8,-4,-3,-5,-3,10,8,1,-10,4,-4,-6,6,-9,-6,-9,-3,7,-3,-9,-1,-6,2,8,8,3,-1,-10,-3,-3,5,-3,-8,6,-3,6,5,6,1,1,-6,-9,3,3,8,5,10,2,6,-7,-5,6,7,5,-6,5,-1,10,-6,10,-10,7,-10,-8,-9,9,8,-3,-7,-2,7,6,2,1,-8,-1,-7,8,1,6,-1,-3,-10,3,-5,2,-2,9,4,-3,-3,1,-7,7,-3,8,-10,4,-7,9,1,3,2,1,-4,-10,-1,6,2,-5,-10,10,4,-2,-10,-3,6,6,10,6,4,-8,1,-4,-9,7,-4,9,-10,8,-4,2,-9,-10,8,2,3,6,5,-6,-10,4,-1,-1,6,10,-2,-3,-1,-1,-8,10,4,7,9,-6,6,3,6,8,-7,3,-1,2,9,2,10,-9,9,6,9,6,-3,-3,-7,9,9,3,10,1,-1,-5,6,-5,-9,-2,-10,-4,-9,10,-7,-10,-4,-4,6,-4,-10,-8,-4,-1,4,3,-4,-9,-3,-1,-1,-7,-3,9,-8,-8,1,-7,1,-10,-3,-8,-10,-4,-7,5,7,1,3,-1,5,1,5,3,-6,-10,-5,-8,7,-10,-10,-10,-5,6,5,8,7,5,7,-8,10,2,8,2,3,-2,7,9,-5,1,-4,-9,10,3,-4,8,10,-1,1,6,7,8,-9,9,6,7,1,-9,2,8,-4,1,-8,4,10,-7,7,-3,6,4,4,-10,-7,-7,2,6,2,9,2,1,-3,-8,-6,1,-5,-4,6,3,4,4,-5,-1,8,9,3,-3,-10,1,4,-10,8,-7,7,-10,1,-6,-4,3,6,3,2,6,-7,-10,10,9,3,2,7,2], dtype = "int32")#candidate|4205|(672,)|const|int32
var_4206 = relay.var("var_4206", dtype = "bool", shape = (2912,))#candidate|4206|(2912,)|var|bool
call_4203 = relay.TupleGetItem(func_3451_call(relay.reshape(var_4204.astype('float64'), [56,]), relay.reshape(const_4205.astype('int32'), [168, 4]), relay.reshape(var_4206.astype('bool'), [2912,]), ), 6)
call_4207 = relay.TupleGetItem(func_3456_call(relay.reshape(var_4204.astype('float64'), [56,]), relay.reshape(const_4205.astype('int32'), [168, 4]), relay.reshape(var_4206.astype('bool'), [2912,]), ), 6)
func_740_call = mod.get_global_var('func_740')
func_743_call = mutated_mod.get_global_var('func_743')
var_4212 = relay.var("var_4212", dtype = "uint32", shape = (1800,))#candidate|4212|(1800,)|var|uint32
call_4211 = relay.TupleGetItem(func_740_call(relay.reshape(var_4206.astype('bool'), [2912,]), relay.reshape(var_4212.astype('uint32'), [1800,]), ), 5)
call_4213 = relay.TupleGetItem(func_743_call(relay.reshape(var_4206.astype('bool'), [2912,]), relay.reshape(var_4212.astype('uint32'), [1800,]), ), 5)
func_336_call = mod.get_global_var('func_336')
func_340_call = mutated_mod.get_global_var('func_340')
const_4224 = relay.const([-9,-7,-3,-3,9,10,-5,-6,8,-3,-6,-10,5,-8,-6,-8,-5,-6,-1,9,-2,-3,3,-1,3,-7,-9,7,1,-1,-2,2,3,-6,-10,-6,3,9,-7,8,-6,-1,1,9,3,9,-8,-5,-2,5,3,2,1,1,-4,9,5,3,10,-8,-1,-10,-1,-9,-5,2,-8,-3,8,8,-6,-9,9,-9,-7,5,5,6,10,6,4,5,-4,2,4,-1,-6,-1,6,7,-6,-9,6,8,5,-3,-4,2,9,-8,-1,-3,-1,4,-6,-9,3,-5,7,7,7,-2,10,-9,-7,4,-7,-7,-3,8,-3,-2,-6,7,8,7,6,6,-3,-7,-3,-10,-9,-1,-9,-2,5,-9,10,-8,10,8,5,3,9,10,-2,2,-7,-4,1,1,9,-9,-7,-1,-4,-4,3,9,-9,5,1,-1,-10,7,10,-9,9,1,-7,-5,-1,10,-6,7,-9,-7,10,1,4,3,-5,6,-8,-1,1,-6,5,-8,4,-6,-8,5,2,9,-3,9,-3,-3,-4,-8,10,-7,9,-6,1,-7,-7,-6,-8,5,7,9,-1,-1,-7,-9,-2,-2,10,-5,1,1,-6,-9,1,-8,-9,8,-9,4,9,-5,-10,3,6,-2,-2,9,9,4,9,10,-9,8,9,-6,-5,-1,-9,-4,4,3,8,-6,9,7,-2,-6,5,-8,7,-5,6,-7,2,-9,-7,4,6,2,-10,3,-6,-4,4,7,8,6,-2,9,4,2,-2,-9,-6,4,-10,1,-6,8,7,-3,-9,-10,-2,5,-9,-1,3,9,-3,-7,-10,10,1,9,-5,-6,-1,-5,5,1,7,5,2,-9,-9,-9,-3,8,-8,6,9,-8,-8,5,5,7,6,3,-8,-4,-9,9,-3,-9,-3,-4,7,-5,5,8,6,3,7,-1,-8,-3,9,10,8,4,-4,-6,-10,-4,2,6,-7,-9,5,-1,-6,-10,8,-10,-9,10,1,-4,8,8,2,-6,-3,5,-7,-10,5,-10,10,-1,-4,-2,-6,8,6,4,9,5,6,-9,8,-8,9,-6,-9,10,8,10,10,-10,5,-2,-5,-6,9,-6,3,10,5,1,-10,9,4,-2,1,-9,-5,9,-8,-10,8,-3,-3,5,8,-4,-8,6,4,6,-1,10,-6,5,3,2,-3,-6,-8,4,6,4,-1,-6,10,2,7,-7,-2,6,8,-1,-4,7,8,10,1,10,8,-1,-9,10,-7,-8,9,-8,-3,10,-6,1,-10,7,-7,-5,4,3,-7,9,2,-2,-3,-10,9,-6,-8,-10,8,-10,-6,-7,-9,4,-3,-1,-2,8,5,-2,9,-1,2,7,-1,-4,2,-7,-2,-8,-6,4,3,-3,-1,5,10,-8,9,4,-2,7,2,6,7,-10,4,10,5,6,-8,-7,8,3,-3,-5,9,-9,-6,-4,-1,-5,-10,2,10,-3,-10,-9,8,-4,-10,5,1,-10,-1,7,1,-6,-8,-6,6,-9,2,5,-9,-2,-7,8,-3,4,-5,7,-4,-6,-1,3,2,6,-7,5,-1,4,-5,6,5,3,1,-3,-3,7,1,-5,-3,8,-3,5,9,-2,6,-2,7,8,-5,1,1,-6,-2,-7,2,-5,8,9,-1,-4,8,-7,-1,-1,9,-8,3,-5,3,-8,-7,9,2,7,-10,2,4,1,8,4,5,10,-6,-3,-6,5,5,-3,4,2,-10,10,-6,1,-4,-3,-9,-8,-9,5,3,3,3,-5,-5,-1,-3,-8,3,-5,8,-9,-3,1,10,-9,5,-3,5,3,6,6,-6,-10,-6,7,5,1,5,-9,-10,-9,8,1,-9,7,10,-7,-10,7,-4,-9,2,-6,-6,3,-3,10,4,9,10,1,9,-8,8,4,2,10,7,-3,3,8,-8,-9,4,6,-4,-5,6,4,1,-6,3,-8,-4,-3,9,-2,2,7,-1,-1,9,-10,1,1,-1,-6,-4,5,7,4,-9,-3,10,-8,-3,8,7,1,3,10,10,10,-2,4,3,7,4,5,-2,-5,-6,-8,-2,-10,2,10,-6,8,5,9,-9,2,-8,9,3,-6,-10,9,5,6,-9,-1,-7,5,2,2,4,-9,2,-2,-6,2,-3,6,2,7,-10,-6,-9,1,-7,-5,8,3,3,-6,4,-5,-1,-6,4,-2,-2,-3,1,4,-8,9,4,9,7,-8,-3,1,5,7,-3,-6,-9,-7,3,-8,-2,-1,9,6,5,-1,9,2,-1,5,-10,-10,10,-9,9,-7,6,-7,-8,-5,9,1,9,-3,-2,6,-9,-3,6,-5,-1,5,-10,4,-7,1,6,3,-5,8,5,1,2,7,6,-2,4,-2,-2,-2,-5,5,5,7,-6,-7,-8,-9,2,8,-5,3,-10,4,3,-10,-1,2,-5,-3,-5,-6,-1,-5,8,-9,4,4,10,5,-6,-4,2,-2,-6,-9,-7,3,-9,-9,10,2,3,-9,6,6,2,10,5,-2,8,1,-6,1,1,-4,9,8,-4,3,-4,5,-9,10,8,7,3,1,-10,-7,-4,5,-7,-5,1,-4,-9,3,-3,-3,2,8,6,7,2,1,4,-1,-1,3,-6,-9,5,4,4,10,-5,-3,8,1,1,7,-9,6,5,-2,-8,8,4,1,7,-3,-10,7,4,1,9,-3,-8,-8,10,-6,4,2,-5,-5,-4,9,5,-5,4,-8,-8,3,2,1,-3,2,10,-3,-7,-9,9,9,4,4,-4,2,3,-5,7,7,-2,5,-5,9,9,6,-6,1,-1,-7,-9,-4,-4,-9,7,-1,7,3,6,-5,-1,-2,-6,-8,-2,-1,-4,5,-5,1,4,-1,9,4,-7,2,-8,5,-9,-10,-8,2,-5,3,3,10,-7,-10,-4,-4,1,-8,-2,2,8,2,10,-1,1,5,-10,-3,7,-7,-8,-3,-9,-10,6,10,-4,1,6,-1,7,-3,10,-6,-9,-7,4,-6,10,3,7,-1,6,7,7,-1,1,-1,-1,-7,2,9,-5,-10,-2,3,6,10,-8,-6,-4,-9,-2,-7,1,-5,-9,8,1,9,1,-3,-7,-9,-2,10,-1,-1,1,-7,-4,-5,7,9,3,9,1,9,7,-5,-2,-2,-5,-7,3,-9,6,-1,1,-1,9,8,-4,-10,-6,9,-9,10,-8,-10,-1,-9,7,10,-2,-2,-2,3,-9,8,-7,1,10,9,8,-8,-10,-8,6,5,-8,9,7,-8,4,-10,-1,-4,-4,-8,4,-3,-10,1,10,6,-3,8,6,8,1,8,1,-2,6,-9,-5,-5,5,3,-2,-3,-3,-8,-8,8,6,-1,9,-4,-5,-3,7,-7,4,8,-8,-4,4,1,-10,-3,-4,-3,-8,-6,-10,-3,-9,-9,-10,-2,10,1,-9,9,-1,6,-5,-8,6,7,-5,10,3,-8,8,5,-5,3,-1,3,-3,7,10,4,-9,9,-5,9,-2,-3,8,-8,8,-9,6,-1,3,-8,7,-8,-4,2,9,7,10,-10,2,3,3,-7,6,-7,-9,-1,-6,-3,-7,10,-8,-5,-9,-9,7,8,-2,7,6,6,-9,-2,-7,7,-1,9,-4,-10,-1,3,-8,8,-8,9,-8,-1,-3,2,-9,-3,-6,2,7,2,-2,6,7,-2,-8,1,6,-1,-5,9,1,-6,4,-6,3,-9,-6,5,-8,10,-7,-1,3,2,-4,3,2,-4,-1,-7,2,-7,10,2,8,5,-3,6], dtype = "uint32")#candidate|4224|(1408,)|const|uint32
call_4223 = relay.TupleGetItem(func_336_call(relay.reshape(const_4224.astype('uint32'), [8, 16, 11]), relay.reshape(call_4203.astype('bool'), [2912,]), ), 3)
call_4225 = relay.TupleGetItem(func_340_call(relay.reshape(const_4224.astype('uint32'), [8, 16, 11]), relay.reshape(call_4203.astype('bool'), [2912,]), ), 3)
output = relay.Tuple([call_4166,bop_4183,bop_4188,call_4192,call_4203,var_4204,const_4205,var_4206,call_4211,var_4212,call_4223,const_4224,])
output2 = relay.Tuple([call_4167,bop_4183,bop_4188,call_4193,call_4207,var_4204,const_4205,var_4206,call_4213,var_4212,call_4225,const_4224,])
func_4229 = relay.Function([var_4182,var_4204,var_4206,var_4212,], output)
mod['func_4229'] = func_4229
mod = relay.transform.InferType()(mod)
mutated_mod['func_4229'] = func_4229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4229_call = mutated_mod.get_global_var('func_4229')
var_4231 = relay.var("var_4231", dtype = "uint8", shape = (8, 5, 7))#candidate|4231|(8, 5, 7)|var|uint8
var_4232 = relay.var("var_4232", dtype = "float64", shape = (1, 56))#candidate|4232|(1, 56)|var|float64
var_4233 = relay.var("var_4233", dtype = "bool", shape = (2912,))#candidate|4233|(2912,)|var|bool
var_4234 = relay.var("var_4234", dtype = "uint32", shape = (1800,))#candidate|4234|(1800,)|var|uint32
call_4230 = func_4229_call(var_4231,var_4232,var_4233,var_4234,)
output = call_4230
func_4235 = relay.Function([var_4231,var_4232,var_4233,var_4234,], output)
mutated_mod['func_4235'] = func_4235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2636_call = mod.get_global_var('func_2636')
func_2637_call = mutated_mod.get_global_var('func_2637')
call_4250 = relay.TupleGetItem(func_2636_call(), 0)
call_4251 = relay.TupleGetItem(func_2637_call(), 0)
func_2125_call = mod.get_global_var('func_2125')
func_2133_call = mutated_mod.get_global_var('func_2133')
var_4269 = relay.var("var_4269", dtype = "float64", shape = (56,))#candidate|4269|(56,)|var|float64
const_4270 = relay.const([8.900424,-5.791060,8.660901,-7.177362,-3.891299,5.336617,-6.163222,-0.296012,0.333073,3.505981,1.179868,7.920705,2.693447,3.468543,4.326316,-3.518950,9.608392,-6.931917,-1.130686,-1.092188,5.167707,1.780629,-0.314549,-9.939538,-9.856216,7.409603,4.511543,7.244431,5.886503,6.523070,-2.041375,7.184606,-0.194810,-9.114158,4.447409,2.527637,9.315486,-0.924512,-4.453271,3.126157,9.550202,-5.406520,9.334441,7.746577,1.156919,1.924089,-5.848815,0.712560,8.779272,-6.789382,-8.139418,0.734949,-8.751291,-4.478222,-0.802351,6.587667,-1.982616,-6.113793,-0.640962,-5.977361,-2.026872,0.999832,-1.137861,9.018746,-5.555335,-3.645302,-7.830751,-3.005443,-2.771141,6.371871,-2.542389,-7.190037,3.482644,7.647795,-1.562972,9.752467,1.864123,-9.096210,3.058008,9.454004,7.541113,7.181795,4.240691,-5.545157,-8.735401,4.935766,-2.667982,8.846339,-5.737707,2.732065,-1.160029,-3.804030,6.235822,9.756514,-9.355833,4.135772,0.658543,6.372236,-9.489963,-2.154250,-5.963600,-2.129812,4.688671,-1.086354,-4.211528,-0.374833,-2.709998,-1.615238,0.294958,-5.789375,9.184795,6.444830,-2.718663,2.483300,-6.985828,4.645861,8.357058,-2.659449,3.865686,3.571872,-0.746574,-5.522689,-4.831050,7.102278,6.745367,6.442662,3.083637,9.103214,-9.879073,-4.468854,-9.992378,9.951125,3.116731,-7.776460,-2.094089,-2.900531,5.159128,6.454310,-3.306853,-5.682315,-8.366029,-1.193488,-0.847393,-7.483174,-2.837330,-7.115065,-9.342486,9.974876,0.949783,6.019494,0.460016,-8.721325,-0.791309,-8.026469,-7.129028,-6.100876,-4.589956,-7.121242,-8.621348,4.289570,-0.429572,0.566941,9.998484,-3.417416,-4.382402,-9.597320,-8.698378,8.343705,-3.925403,4.737687,-9.429975,-1.530049,-5.503615,3.696525,9.090250,1.154273,-2.908989,-0.237981,4.817823,-6.842902,-9.353703,7.291582,-8.433602,-8.990475,-9.650423,5.245840,6.297861,-7.518206,1.081222,3.882244,-1.541735,-8.667024,9.971801,2.255861,7.389864,7.386933,-7.424112,-1.715111,2.502987,-3.130555,-4.002929,-3.853239,1.135832,3.241244,-8.144261,2.248967,-7.240409,-7.261604,-8.215835,-9.175541,7.129934,-3.734105,2.852949,-3.818010,9.713099,-0.503474,1.388517,1.570424,1.658459,8.167400,3.460603,8.730934,-8.229479,-3.522249,1.242954,-6.503901,-9.488785,-9.883242,-1.012109,-9.035064,4.072850,7.829055,4.471497,6.610272,-8.747660,-1.204438,3.064390,6.177798,8.857756,9.182237,-2.979740,-2.466365,-1.946644,-0.039496,1.421535,-7.571364,-4.187016,3.053313,-5.053533,-5.621316,6.108958,6.239497,-4.129949,-1.712970,-1.554617,-7.473335,-9.010354,5.695063,-8.744486,7.564710,-7.966279,-2.876343,4.037642,-5.037942,7.629308,-7.942036,9.917692,7.489086,-2.082550,-4.834182,5.792979,-3.598442,7.014397,-5.883615,4.599201,7.050817,9.458490,-4.366694,-3.619072,4.498502,-0.311619,-8.467388,7.363882,1.448053,-3.625429,-1.608559,5.104956,9.181670,-9.821033,-1.547890,2.584069,8.034807,5.247363,7.024584,-6.369986,8.834982,9.153699,-0.899198,-1.941999,-3.912198,2.279476,-5.202033,8.663461,5.762452,-4.364960,-7.312611,-5.638907,-3.235892,8.161899,7.329488,-7.453550,-1.337493,-1.304567,-5.422829,4.754433,5.276211,1.163479,6.578168,0.881662,-7.607873,-3.664013,7.668317,-2.652480,-6.656513,-1.389888,0.296988,3.859685,-5.261876,7.662022,-2.188915,1.695125,5.876680,4.185919,-1.964153,-4.055543,-9.134831,4.823267,1.258422,-5.945712,5.237363,1.477131,8.860705,7.071951,-6.751769,0.996815,4.810755,9.475254,0.954495,7.552062,9.713150,7.563289,-3.182003,-3.103460,-1.229249,4.687732,5.591495,3.900008,9.094821,-0.567899,2.935931,-1.726757,-7.721264,7.109156,9.657345,3.490217,-6.486712,-1.620009,5.217936,-2.604677,1.344062,-5.521256,-3.665528,-8.756598,-7.894843,-1.592304,-7.620951,-6.473708,-6.890503,-3.125439,-3.818907,-7.975757,-8.539372,3.661598,2.113317,-1.884275,7.074718,3.718645,-7.500991,-6.148488,-0.402217,-4.131342,7.542902,-5.539188,-4.232918,5.228541,-0.261028,-6.429639,0.373168,5.093003,8.278870,1.288347,-7.091977,7.150620,-1.235888,0.896994,-4.576569,9.167087,-9.609676,9.505095,7.079996,7.036259,-3.291909,-4.847631,2.510100,2.466461,9.109373,1.907231,1.829074,-3.495850,-4.087250,9.363780,0.736052,0.783005,-9.298602,4.053783,2.585059,6.985887,-0.926549,8.520184,0.083409,-9.333150,-0.035658,-1.291624,-7.717826,0.037047,-7.573532,8.661980,-4.604039,6.471549,0.657078,-6.980414,8.135366,5.861988,7.308557,5.832958,1.267300,-9.857274,-7.373448], dtype = "float64")#candidate|4270|(448,)|const|float64
const_4271 = relay.const([3,4,-2,2,-3,-7,9,-4,-8,1,-9,9,-4,9,3,6,8,2,10,-7,-8,3,-10,8,-6,-1,-9,-6,-7,3,-10,7,-10,8,-4,-2,-9,-2,4,7,6,-8,8,-9,6,6,10,4,6,-9,-6,3,-8,4,-4,1,-9,-4,-2,6,5,-3,-7,7,10,-4,-9,-2,1,-8,-7,4,9,-6,2,-8,-4,-6,-10,6,10,-8,6,-7,-6,-3,-3,10,4,-2,8,7,-3,-4,-5,4,-10,-6,2,5,-8,10,3,5,8,8,-9,7,-6,-4,-1,8,-1,-8,-10,1,-9,-3,-3,-4,8,-6,-4,9,-3,-3,-1,6,7,-5,6,7,8,-2,8,1,-5,-5,9,-1,8,9,-6,1,10,2,-3,5,-9,-4,10,-5,2,4,-3,-6,-10,10,9,-9,1,-6,10,-8,6,-8,-5,1,-2,-1,-3,-5,9,9,9,8,1,6,5,2,4,-8,-2,8,-6,-8,3,2,-1,1,-10,9,3,5,-9,-9,-7,-2,6,3,-7,2,4,-4,-4,-4,6,-8,-1,8,9,1,-6,7,10,-5,8,-9,-3,5,9,-4,5,7,4,-3,5,-3,6,-3,7,-5,7,-9,-8,10,6,-4,7,-4,-7,5,9,-2,-7,1,-5,1,2,-4,4,10,9,10,7,6,9,7,1,-4,4,-2,-6,5,-3,-8,3,9,-2,-8,1,3,7,-9,-9,7,-2,6,-4,-4,10,-5,10,4,1,2,-8,-3,5,3,6,-1,9,-6,8,9,4,10,-8,-7,-8,2,-4,-1,8,4,4,-4,-5,-7,2,1,-1,-1,7,7,-7,-3,5,-1,-10,7,-2,-10,-1,10,-4,-9,-1,-4,-8,-6,-2,-5,3,-10,-3,-8,7,-4,4,4,-4,-2,5,3,-1,-8,8,-1,-3,3,-7,-1,-10,7,-8,1,-5,-6,3,6,10,6,-1,-8,-8,-8,-3,-1,5,-6,-10,4,-4,-8,2,10,9,-10,2,3,-9,7,2,-7,-8,10,2,3,-4,2,4,10,7,-4,-5,1,9,-10,-7,-10,9,-3,3,6,9,-5,-9,8,2,7,8,5,-7,10,9,-9,7,-9,9,10,-3,-1,-8,2,-1,-9,-6,-6,-9,-7,6,7,7,6,1,-4,-8,9,-5,8,-10,7,-1,-1,9,9,3,9,-1,-5,-10,7,5,-4,8,8,-8,6,-8,-10,-2,-4,-4,-6,-9,-5,2,-7,-9,9,2,5,-4,9,-7,-1,-7,-5,-10,-4,-4,10,-1,4,7,-9,-3,-8,7,-9,6,5,-4,2,3,-5,-5,2,-1,7,-10,-6,3,1,1,4,9,1,-10,-9,1,10,10,-3,8,10,8,-2,2,-1,-3,-2,-4,6,-10,-9,-3,-6,-10,-6,10,-8,-4,1,4,-2,-7,-9,-9,-7,4,-9,-6,9,-7,6,-3,-8,-5,-6,1,7,-2,10,-5,-2,4,5,-8,8,1,3,-8,-4,9,3,-6,9,9,9,6,-3,3,-2,4,6,-4,1,1,-5,5,-10,10,-9,9,-5,1,7,7,7,-9,-9,4,-3,7,-5,5,3,7,4,-2,-2,8,9,9,7,8,1,7,-7,3,7,7,5,4,9,8,-10,-1,2,-4,-9,4,-4,-3,5,1,6,-4,4,-10,-7,-4,-7,-8,4,9,-2,-3,-5,-5,4,4,8,3,-7,6,-5,1,-5,2,-10,-3,5,-9,4,-3,-4,2,-7,5,-8,-8,-1,-7,-7,-6,-10,-9,8], dtype = "int32")#candidate|4271|(672,)|const|int32
const_4272 = relay.const([-7.951768,5.426932,7.201415,8.614172,5.079210,-0.799286,3.613585,5.476812,-0.405854,2.098045,8.728341,0.398824,-9.015601,-4.771012,-8.155571,7.521553,0.084544,-9.143281,-3.240638,1.661535,-8.657613,1.946542,9.774184,5.586395,-8.756856,4.400044,-9.390673,3.696386,-8.201075,3.401097,-9.468068,3.886811,4.718572,-3.749875,9.050889,3.008969,-1.667945,0.874720,0.926686,0.170488,6.839124,-7.810700,8.695268,-8.901123,2.837202,-4.967869,-2.273384,-5.950815], dtype = "float32")#candidate|4272|(48,)|const|float32
var_4273 = relay.var("var_4273", dtype = "bool", shape = (2912,))#candidate|4273|(2912,)|var|bool
var_4274 = relay.var("var_4274", dtype = "uint32", shape = (1800,))#candidate|4274|(1800,)|var|uint32
call_4268 = relay.TupleGetItem(func_2125_call(relay.reshape(var_4269.astype('float64'), [7, 8, 1]), relay.reshape(const_4270.astype('float64'), [7, 8, 8]), relay.reshape(const_4271.astype('int32'), [672,]), relay.reshape(const_4272.astype('float32'), [48,]), relay.reshape(var_4273.astype('bool'), [2912,]), relay.reshape(var_4274.astype('uint32'), [1800,]), ), 8)
call_4275 = relay.TupleGetItem(func_2133_call(relay.reshape(var_4269.astype('float64'), [7, 8, 1]), relay.reshape(const_4270.astype('float64'), [7, 8, 8]), relay.reshape(const_4271.astype('int32'), [672,]), relay.reshape(const_4272.astype('float32'), [48,]), relay.reshape(var_4273.astype('bool'), [2912,]), relay.reshape(var_4274.astype('uint32'), [1800,]), ), 8)
func_2849_call = mod.get_global_var('func_2849')
func_2850_call = mutated_mod.get_global_var('func_2850')
call_4276 = relay.TupleGetItem(func_2849_call(), 0)
call_4277 = relay.TupleGetItem(func_2850_call(), 0)
output = relay.Tuple([call_4250,call_4268,var_4269,const_4270,const_4271,const_4272,var_4273,var_4274,call_4276,])
output2 = relay.Tuple([call_4251,call_4275,var_4269,const_4270,const_4271,const_4272,var_4273,var_4274,call_4277,])
func_4280 = relay.Function([var_4269,var_4273,var_4274,], output)
mod['func_4280'] = func_4280
mod = relay.transform.InferType()(mod)
var_4281 = relay.var("var_4281", dtype = "float64", shape = (56,))#candidate|4281|(56,)|var|float64
var_4282 = relay.var("var_4282", dtype = "bool", shape = (2912,))#candidate|4282|(2912,)|var|bool
var_4283 = relay.var("var_4283", dtype = "uint32", shape = (1800,))#candidate|4283|(1800,)|var|uint32
output = func_4280(var_4281,var_4282,var_4283,)
func_4284 = relay.Function([var_4281,var_4282,var_4283,], output)
mutated_mod['func_4284'] = func_4284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2400_call = mod.get_global_var('func_2400')
func_2402_call = mutated_mod.get_global_var('func_2402')
call_4292 = relay.TupleGetItem(func_2400_call(), 0)
call_4293 = relay.TupleGetItem(func_2402_call(), 0)
func_3561_call = mod.get_global_var('func_3561')
func_3564_call = mutated_mod.get_global_var('func_3564')
var_4311 = relay.var("var_4311", dtype = "float64", shape = (108,))#candidate|4311|(108,)|var|float64
call_4310 = func_3561_call(relay.reshape(var_4311.astype('float64'), [3, 6, 6]), relay.reshape(var_4311.astype('float64'), [3, 6, 6]), )
call_4312 = func_3561_call(relay.reshape(var_4311.astype('float64'), [3, 6, 6]), relay.reshape(var_4311.astype('float64'), [3, 6, 6]), )
bop_4323 = relay.add(call_4310.astype('uint32'), relay.reshape(var_4311.astype('uint32'), relay.shape_of(call_4310))) # shape=(3, 6, 6)
bop_4326 = relay.add(call_4312.astype('uint32'), relay.reshape(var_4311.astype('uint32'), relay.shape_of(call_4312))) # shape=(3, 6, 6)
func_2534_call = mod.get_global_var('func_2534')
func_2535_call = mutated_mod.get_global_var('func_2535')
call_4329 = relay.TupleGetItem(func_2534_call(), 0)
call_4330 = relay.TupleGetItem(func_2535_call(), 0)
output = relay.Tuple([call_4292,bop_4323,call_4329,])
output2 = relay.Tuple([call_4293,bop_4326,call_4330,])
func_4342 = relay.Function([var_4311,], output)
mod['func_4342'] = func_4342
mod = relay.transform.InferType()(mod)
var_4343 = relay.var("var_4343", dtype = "float64", shape = (108,))#candidate|4343|(108,)|var|float64
output = func_4342(var_4343)
func_4344 = relay.Function([var_4343], output)
mutated_mod['func_4344'] = func_4344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1739_call = mod.get_global_var('func_1739')
func_1741_call = mutated_mod.get_global_var('func_1741')
call_4359 = relay.TupleGetItem(func_1739_call(), 0)
call_4360 = relay.TupleGetItem(func_1741_call(), 0)
func_2185_call = mod.get_global_var('func_2185')
func_2188_call = mutated_mod.get_global_var('func_2188')
var_4371 = relay.var("var_4371", dtype = "float64", shape = (84,))#candidate|4371|(84,)|var|float64
call_4370 = func_2185_call(relay.reshape(var_4371.astype('float64'), [1, 7, 12]))
call_4372 = func_2185_call(relay.reshape(var_4371.astype('float64'), [1, 7, 12]))
output = relay.Tuple([call_4359,call_4370,var_4371,])
output2 = relay.Tuple([call_4360,call_4372,var_4371,])
func_4382 = relay.Function([var_4371,], output)
mod['func_4382'] = func_4382
mod = relay.transform.InferType()(mod)
mutated_mod['func_4382'] = func_4382
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4383 = relay.var("var_4383", dtype = "float64", shape = (84,))#candidate|4383|(84,)|var|float64
func_4382_call = mutated_mod.get_global_var('func_4382')
call_4384 = func_4382_call(var_4383)
output = call_4384
func_4385 = relay.Function([var_4383], output)
mutated_mod['func_4385'] = func_4385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4036_call = mod.get_global_var('func_4036')
func_4037_call = mutated_mod.get_global_var('func_4037')
call_4395 = relay.TupleGetItem(func_4036_call(), 1)
call_4396 = relay.TupleGetItem(func_4037_call(), 1)
output = call_4395
output2 = call_4396
func_4399 = relay.Function([], output)
mod['func_4399'] = func_4399
mod = relay.transform.InferType()(mod)
output = func_4399()
func_4400 = relay.Function([], output)
mutated_mod['func_4400'] = func_4400
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4403 = relay.const(8, dtype = "int16")#candidate|4403|()|const|int16
var_4404 = relay.var("var_4404", dtype = "int16", shape = (3, 2, 10))#candidate|4404|(3, 2, 10)|var|int16
bop_4405 = relay.greater_equal(const_4403.astype('bool'), var_4404.astype('bool')) # shape=(3, 2, 10)
output = relay.Tuple([bop_4405,])
output2 = relay.Tuple([bop_4405,])
func_4414 = relay.Function([var_4404,], output)
mod['func_4414'] = func_4414
mod = relay.transform.InferType()(mod)
mutated_mod['func_4414'] = func_4414
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4415 = relay.var("var_4415", dtype = "int16", shape = (3, 2, 10))#candidate|4415|(3, 2, 10)|var|int16
func_4414_call = mutated_mod.get_global_var('func_4414')
call_4416 = func_4414_call(var_4415)
output = call_4416
func_4417 = relay.Function([var_4415], output)
mutated_mod['func_4417'] = func_4417
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4426 = relay.const([[[3.184399],[-6.872876],[-3.512704],[-7.980875],[0.286556]],[[-1.139554],[-5.059547],[-3.337136],[-8.595507],[-7.658862]],[[-5.336423],[-3.388822],[-4.489934],[1.086950],[-0.664800]],[[-5.303215],[8.256338],[4.197171],[-9.792243],[-8.880142]]], dtype = "float32")#candidate|4426|(4, 5, 1)|const|float32
uop_4427 = relay.sqrt(const_4426.astype('float32')) # shape=(4, 5, 1)
func_1739_call = mod.get_global_var('func_1739')
func_1741_call = mutated_mod.get_global_var('func_1741')
call_4430 = relay.TupleGetItem(func_1739_call(), 0)
call_4431 = relay.TupleGetItem(func_1741_call(), 0)
output = relay.Tuple([uop_4427,call_4430,])
output2 = relay.Tuple([uop_4427,call_4431,])
func_4434 = relay.Function([], output)
mod['func_4434'] = func_4434
mod = relay.transform.InferType()(mod)
output = func_4434()
func_4435 = relay.Function([], output)
mutated_mod['func_4435'] = func_4435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1844_call = mod.get_global_var('func_1844')
func_1845_call = mutated_mod.get_global_var('func_1845')
call_4467 = relay.TupleGetItem(func_1844_call(), 1)
call_4468 = relay.TupleGetItem(func_1845_call(), 1)
var_4492 = relay.var("var_4492", dtype = "float64", shape = (4, 15, 15))#candidate|4492|(4, 15, 15)|var|float64
bop_4493 = relay.left_shift(call_4467.astype('int32'), relay.reshape(var_4492.astype('int32'), relay.shape_of(call_4467))) # shape=(4, 15, 15)
bop_4496 = relay.left_shift(call_4468.astype('int32'), relay.reshape(var_4492.astype('int32'), relay.shape_of(call_4468))) # shape=(4, 15, 15)
func_3888_call = mod.get_global_var('func_3888')
func_3889_call = mutated_mod.get_global_var('func_3889')
call_4503 = func_3888_call()
call_4504 = func_3888_call()
var_4507 = relay.var("var_4507", dtype = "int32", shape = (4, 15, 15))#candidate|4507|(4, 15, 15)|var|int32
bop_4508 = relay.greater_equal(bop_4493.astype('bool'), relay.reshape(var_4507.astype('bool'), relay.shape_of(bop_4493))) # shape=(4, 15, 15)
bop_4511 = relay.greater_equal(bop_4496.astype('bool'), relay.reshape(var_4507.astype('bool'), relay.shape_of(bop_4496))) # shape=(4, 15, 15)
output = relay.Tuple([call_4503,bop_4508,])
output2 = relay.Tuple([call_4504,bop_4511,])
func_4514 = relay.Function([var_4492,var_4507,], output)
mod['func_4514'] = func_4514
mod = relay.transform.InferType()(mod)
var_4515 = relay.var("var_4515", dtype = "float64", shape = (4, 15, 15))#candidate|4515|(4, 15, 15)|var|float64
var_4516 = relay.var("var_4516", dtype = "int32", shape = (4, 15, 15))#candidate|4516|(4, 15, 15)|var|int32
output = func_4514(var_4515,var_4516,)
func_4517 = relay.Function([var_4515,var_4516,], output)
mutated_mod['func_4517'] = func_4517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1811_call = mod.get_global_var('func_1811')
func_1813_call = mutated_mod.get_global_var('func_1813')
call_4561 = relay.TupleGetItem(func_1811_call(), 0)
call_4562 = relay.TupleGetItem(func_1813_call(), 0)
func_2927_call = mod.get_global_var('func_2927')
func_2928_call = mutated_mod.get_global_var('func_2928')
call_4564 = relay.TupleGetItem(func_2927_call(), 3)
call_4565 = relay.TupleGetItem(func_2928_call(), 3)
func_1124_call = mod.get_global_var('func_1124')
func_1130_call = mutated_mod.get_global_var('func_1130')
var_4575 = relay.var("var_4575", dtype = "float64", shape = (165,))#candidate|4575|(165,)|var|float64
const_4576 = relay.const([7,-3,2,-4,4,-7,1,4,7,-1,4,8,-2,6,-10,3,8,6,3,-4,1,7,-3,5,-6,6,-8,7,7,-7,2,-6,5,10,-1,6,-6,-6,-7,-8,-7,5,1,5,-7,6,-2,8,6,7,4,1,-10,8,-8,-10,-3,10,9,5,-8,3,-5,9,-3,-1,2,7,-7,-9,3,9,6,-1,7,-1,7,6,7,5,2,6,-6,-7], dtype = "int32")#candidate|4576|(84,)|const|int32
var_4577 = relay.var("var_4577", dtype = "int32", shape = (336, 2))#candidate|4577|(336, 2)|var|int32
call_4574 = relay.TupleGetItem(func_1124_call(relay.reshape(var_4575.astype('float64'), [11, 5, 3]), relay.reshape(call_4564.astype('int8'), [480,]), relay.reshape(const_4576.astype('int32'), [84, 1]), relay.reshape(var_4577.astype('int32'), [672,]), ), 3)
call_4578 = relay.TupleGetItem(func_1130_call(relay.reshape(var_4575.astype('float64'), [11, 5, 3]), relay.reshape(call_4564.astype('int8'), [480,]), relay.reshape(const_4576.astype('int32'), [84, 1]), relay.reshape(var_4577.astype('int32'), [672,]), ), 3)
func_471_call = mod.get_global_var('func_471')
func_475_call = mutated_mod.get_global_var('func_475')
const_4590 = relay.const([-8.795282,-6.295417,5.477325,4.851817,4.336484,-7.570890,9.609560,8.363529,3.213105,0.362430,0.335721,9.176563,9.560566,-6.250654,8.462872,-3.468079,0.099415,7.969570,9.805669,-1.075428,0.272040,3.239313,7.546657,-5.208323,0.593653,3.377876,-4.743034,7.361373,3.992682,-4.658493,-7.734462,-9.966147,-4.652568,-9.072485,-9.890893,-8.127237,2.356488,-1.613667,-4.858246,-3.325001,8.328333,-5.452812,-9.587558,5.720760,-2.953000,5.600822,-1.786866,-5.198704], dtype = "float32")#candidate|4590|(48,)|const|float32
call_4589 = relay.TupleGetItem(func_471_call(relay.reshape(const_4590.astype('float32'), [1, 3, 16]), relay.reshape(call_4574.astype('bool'), [104, 28]), ), 2)
call_4591 = relay.TupleGetItem(func_475_call(relay.reshape(const_4590.astype('float32'), [1, 3, 16]), relay.reshape(call_4574.astype('bool'), [104, 28]), ), 2)
output = relay.Tuple([call_4561,call_4564,call_4574,var_4575,const_4576,var_4577,call_4589,const_4590,])
output2 = relay.Tuple([call_4562,call_4565,call_4578,var_4575,const_4576,var_4577,call_4591,const_4590,])
func_4617 = relay.Function([var_4575,var_4577,], output)
mod['func_4617'] = func_4617
mod = relay.transform.InferType()(mod)
mutated_mod['func_4617'] = func_4617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4617_call = mutated_mod.get_global_var('func_4617')
var_4619 = relay.var("var_4619", dtype = "float64", shape = (165,))#candidate|4619|(165,)|var|float64
var_4620 = relay.var("var_4620", dtype = "int32", shape = (336, 2))#candidate|4620|(336, 2)|var|int32
call_4618 = func_4617_call(var_4619,var_4620,)
output = call_4618
func_4621 = relay.Function([var_4619,var_4620,], output)
mutated_mod['func_4621'] = func_4621
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4625 = relay.var("var_4625", dtype = "float32", shape = (15, 15, 6))#candidate|4625|(15, 15, 6)|var|float32
uop_4626 = relay.sqrt(var_4625.astype('float32')) # shape=(15, 15, 6)
output = relay.Tuple([uop_4626,])
output2 = relay.Tuple([uop_4626,])
func_4634 = relay.Function([var_4625,], output)
mod['func_4634'] = func_4634
mod = relay.transform.InferType()(mod)
var_4635 = relay.var("var_4635", dtype = "float32", shape = (15, 15, 6))#candidate|4635|(15, 15, 6)|var|float32
output = func_4634(var_4635)
func_4636 = relay.Function([var_4635], output)
mutated_mod['func_4636'] = func_4636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3480_call = mod.get_global_var('func_3480')
func_3482_call = mutated_mod.get_global_var('func_3482')
call_4658 = relay.TupleGetItem(func_3480_call(), 1)
call_4659 = relay.TupleGetItem(func_3482_call(), 1)
func_1510_call = mod.get_global_var('func_1510')
func_1511_call = mutated_mod.get_global_var('func_1511')
call_4666 = relay.TupleGetItem(func_1510_call(), 0)
call_4667 = relay.TupleGetItem(func_1511_call(), 0)
func_551_call = mod.get_global_var('func_551')
func_554_call = mutated_mod.get_global_var('func_554')
const_4683 = relay.const([[-5,3,5,7,3,1,-5,-1,-4,-3,2,-5,-3,-7,-4,-5,2,-9,5,8,-9,2,-7,5,7,-6,5,6,-4,2,2,9,5,-4,3,-10,2,-6,-6,10,-10,-2,10,3,-3,-3,2,2,9,-10,7,-5,-4,7,4,5,8,7,9,3,2,-8,8,-6,5,7,7,-10,3,-5,7,-10,-9,-4,-4,-2,-2,5,-10,7,6,-5,6,-6,-5,7,-2,8,4,2,8,6,-4,-2,-1,-10,-2,2,2,-10],[-10,8,4,3,-7,-7,9,-5,-6,7,-5,-8,2,7,-7,-9,-4,7,3,7,7,5,9,10,8,-7,-4,1,3,8,-5,-7,5,8,-7,6,-10,1,10,7,9,-2,-6,-7,-9,1,5,4,3,8,6,4,-4,7,4,-5,-9,6,-7,6,-1,1,-4,-5,-6,7,-6,10,-3,5,5,2,4,9,2,-9,-2,-8,5,1,4,-3,-8,10,2,-1,-7,8,5,-5,3,-10,4,9,-3,9,10,-8,5,-10],[-5,-3,-7,4,-10,-7,-4,-8,-8,6,-1,9,-8,-10,4,1,4,-2,5,-1,6,10,8,8,4,7,10,-9,-2,-3,-10,8,8,-4,-7,-2,6,4,-7,-10,-8,-8,-5,-9,7,-5,-8,-2,-4,-3,-3,7,4,-3,-4,4,2,-10,-1,5,-3,-5,-5,7,-3,-2,5,8,-1,-10,6,6,-8,-4,-7,4,-1,-1,4,-4,10,7,-7,5,-6,2,-1,-9,-9,7,-3,-6,-10,9,-6,-2,2,4,-4,5],[3,1,10,-2,-4,4,10,2,-8,-3,-7,-3,-6,-6,5,10,1,-4,1,1,-7,-3,-7,-6,-7,9,3,2,-10,-10,2,-5,-1,-5,6,-6,-10,-9,-3,2,-3,-5,-5,-8,5,-2,-7,-9,7,-1,-1,8,-5,8,4,-1,1,7,-2,2,4,4,10,-10,-1,-2,7,4,6,3,10,-9,7,-8,1,-6,-4,6,6,-3,-8,-9,-2,8,-3,-2,-4,-3,-6,-2,10,4,10,10,-8,3,5,-1,-5,6],[10,10,-8,-5,-5,-5,-4,-1,-9,-2,-1,10,-9,4,2,9,-10,7,5,6,10,-4,-8,-1,-5,1,8,-1,-4,8,-7,-9,-9,4,-10,-3,-2,5,4,-7,8,5,1,2,3,5,-10,-6,1,-2,-2,1,2,4,-1,2,-10,7,5,9,1,9,-8,-10,-8,-2,-5,-6,1,2,-2,-3,-3,4,-2,-9,8,-2,-4,-9,-3,5,-6,-5,-3,-10,1,-9,-6,6,7,10,-3,6,-5,2,-8,7,1,2],[1,1,7,-8,-3,2,-10,-7,-3,10,6,7,2,9,-8,-7,4,2,-8,-6,-5,-10,9,7,8,1,3,9,3,-9,10,-9,4,6,4,-4,8,-3,1,10,-1,-5,-10,8,-6,-4,2,9,-7,-1,-6,-9,9,1,5,-9,-4,-9,-1,-6,3,-3,5,5,8,-2,-9,9,4,7,-3,4,-3,10,1,2,7,-10,-9,6,-1,2,-1,9,2,5,-2,-3,-3,10,-10,-9,-6,-3,6,-2,8,-8,-4,-4],[-4,-4,-9,3,1,-5,4,1,-3,-6,-2,7,-4,-10,-5,-7,-5,-7,-9,8,6,2,-7,1,-5,-2,-9,8,-3,4,-5,7,5,4,-6,3,-6,-1,5,-7,-3,1,6,-7,-10,-9,5,4,-1,1,1,-9,-8,1,4,-6,-5,-9,6,3,9,10,-9,-2,-3,8,-9,-2,-7,10,1,10,-3,-10,-7,7,-5,9,-3,2,6,-1,-7,1,6,-7,9,2,8,-3,4,-2,10,3,-4,9,-5,6,3,-9],[-1,3,-6,2,-8,-9,-8,1,2,-9,-9,8,-1,7,2,-3,2,10,5,-2,-8,5,-3,4,-8,-4,3,10,-6,10,-3,-10,-10,-5,-6,-6,-1,2,5,1,-1,10,-9,-10,9,5,-2,9,7,7,-10,-10,3,-4,8,-4,4,-4,6,8,-3,-7,9,-9,9,-2,6,-1,3,-9,-5,-1,9,-10,9,-10,2,-9,5,-9,-1,-5,-4,10,-4,-10,2,-5,-7,7,4,10,7,9,7,-8,1,-9,-10,4],[-6,10,-8,-10,-10,2,-6,-2,-2,-7,-2,-7,-6,10,3,-7,-10,8,2,6,-5,-7,-1,-4,-3,9,-3,8,5,5,-4,9,-1,-4,5,8,8,-2,6,1,-6,5,-9,1,1,-1,2,8,7,10,-2,5,-4,9,3,-9,2,-8,-7,4,9,-10,7,6,-2,7,3,-5,7,8,6,8,-1,9,-7,5,-10,9,-3,-1,-9,10,-10,-10,-9,-6,-6,-2,-3,5,6,8,-5,1,-1,-6,1,-6,-8,-8],[5,-5,10,-9,10,3,-6,-2,-9,2,5,2,-1,-7,-5,10,-10,-10,-2,-1,5,-8,8,-1,-5,9,-8,-8,-9,9,-1,-5,-4,9,-6,-8,-8,-9,8,-5,2,3,-5,2,-7,10,-10,6,10,9,10,4,-8,6,4,9,3,7,-2,-2,9,-6,4,4,1,-1,-5,-1,-9,-8,-8,8,-8,1,-5,-10,4,-7,8,-6,9,10,-10,6,9,2,-1,-1,9,-1,-7,-1,7,-1,1,3,-3,-5,-7,-4],[-5,4,-1,4,-8,-4,-6,-6,-7,7,4,-10,-5,2,4,-8,6,-4,10,-7,-3,-5,-8,-1,8,2,9,1,-7,-8,2,-1,-10,5,2,-10,3,-5,6,7,-5,-10,-3,8,5,-10,-2,5,-5,-3,2,-4,-9,-7,7,1,-3,4,-1,5,-8,2,5,3,-10,6,8,-7,1,3,10,-9,4,-8,-8,2,-7,8,-4,1,-5,-5,9,1,-8,5,8,-10,7,-7,10,-3,-4,10,-9,-1,7,9,-10,3],[3,-5,-4,-3,-4,6,-2,2,9,5,2,-4,3,-5,2,-10,-10,7,-1,-4,3,-8,10,-10,-3,-9,-10,-4,-4,4,8,4,1,1,2,-7,-7,7,-9,6,-9,-5,-8,1,-9,-10,1,7,5,-5,3,-1,9,8,4,-7,9,-3,-2,-8,9,10,-2,-3,-4,4,-10,-8,3,-6,9,10,-9,6,-7,-4,2,8,2,-3,-10,4,1,1,-9,9,-4,10,3,-7,-10,-7,-7,-8,-6,5,-5,-8,-2,-10],[-7,1,-9,-5,6,-3,2,-7,-4,-8,-6,-6,2,9,2,7,8,1,8,2,-9,-10,-4,10,4,10,-8,10,2,-6,-9,-4,-10,4,2,-3,2,1,-10,6,6,-3,4,-6,5,1,-2,10,-1,-1,-2,-3,8,10,5,-2,-4,7,10,-6,-5,8,-9,1,-5,-2,-7,-3,1,2,1,-8,1,-7,-1,8,8,-5,-6,-9,-1,10,-6,-2,8,2,10,-6,-7,3,-6,6,-5,-2,-1,4,2,9,-6,-6],[7,-4,9,-9,5,-6,3,6,7,10,9,-10,-7,8,2,-8,3,7,5,10,-9,2,10,-9,8,-5,-3,-7,-3,-4,10,-3,5,4,-7,-2,1,-8,4,8,-7,8,-9,10,1,-5,5,1,-10,-2,9,3,9,-9,-9,4,3,5,8,-3,9,-7,8,4,3,4,9,-10,-9,1,9,3,9,3,5,-4,4,7,-1,9,-9,6,8,-6,8,-4,-5,8,-9,1,6,8,-7,3,8,-2,3,-4,-5,-10],[8,-9,-3,6,1,-7,3,9,10,9,-4,-2,-10,-7,-7,-7,1,7,-6,-9,2,-6,-9,6,8,5,8,-8,4,-3,-4,-5,10,-2,-6,-5,-5,3,7,3,-7,-7,6,1,-5,-10,-7,-6,8,3,-9,4,7,-7,-9,10,-9,-8,4,-6,6,-8,4,7,-1,7,9,3,-1,2,3,5,-1,-10,2,6,5,-10,9,10,-8,-10,-10,-4,-5,2,-8,-3,-10,8,10,-10,9,3,-7,-5,-2,3,10,-7],[-4,5,6,5,-3,-7,-6,-8,-9,10,-4,3,2,1,5,-6,-5,-3,3,6,-10,6,2,-8,5,-8,-4,8,-9,5,5,3,6,-2,5,-2,-2,10,4,-6,-7,-1,-3,5,6,-6,-5,2,8,-10,-5,-7,-3,-1,-6,-10,-9,-1,8,6,8,-6,4,4,-3,4,-7,4,-9,-10,2,-7,-1,-7,4,2,9,5,-5,5,3,5,-4,1,4,8,1,8,4,10,1,10,-1,5,-3,-3,2,6,9,-1],[9,8,7,-4,5,8,6,-8,-4,3,3,-4,6,-1,9,7,-3,10,4,8,-7,-5,-6,-2,-6,-8,2,4,-3,-4,-8,10,5,9,3,-9,6,5,-7,-2,3,1,-3,-3,9,7,-8,7,7,5,5,-2,7,3,-4,6,7,3,2,6,-5,9,10,-7,3,-6,-5,9,6,6,7,7,1,5,8,-7,4,4,-3,10,-2,-4,7,-9,-5,2,10,5,-1,-9,2,10,1,10,7,-9,8,-8,-9,7],[5,-6,-1,8,-3,-1,-10,-9,-6,-6,10,-2,1,5,-8,-3,-4,-5,2,-6,-10,-8,-7,3,9,-4,5,9,-7,-7,9,-5,-3,-7,-4,9,-10,-6,7,10,-9,5,2,3,10,-2,3,1,8,8,1,-5,6,7,3,9,2,9,10,1,1,1,1,-10,10,-10,-7,9,8,-9,1,-2,-4,7,2,-5,3,9,-6,2,8,6,-7,-1,10,6,7,-6,-1,-4,5,8,-5,-2,5,-6,4,-10,-6,-5]], dtype = "uint32")#candidate|4683|(18, 100)|const|uint32
call_4682 = relay.TupleGetItem(func_551_call(relay.reshape(const_4683.astype('uint32'), [10, 15, 12]), relay.reshape(const_4683.astype('uint32'), [10, 15, 12]), ), 0)
call_4684 = relay.TupleGetItem(func_554_call(relay.reshape(const_4683.astype('uint32'), [10, 15, 12]), relay.reshape(const_4683.astype('uint32'), [10, 15, 12]), ), 0)
bop_4685 = relay.less(const_4683.astype('bool'), relay.reshape(call_4682.astype('bool'), relay.shape_of(const_4683))) # shape=(18, 100)
bop_4688 = relay.less(const_4683.astype('bool'), relay.reshape(call_4684.astype('bool'), relay.shape_of(const_4683))) # shape=(18, 100)
output = relay.Tuple([call_4658,call_4666,bop_4685,])
output2 = relay.Tuple([call_4659,call_4667,bop_4688,])
func_4702 = relay.Function([], output)
mod['func_4702'] = func_4702
mod = relay.transform.InferType()(mod)
mutated_mod['func_4702'] = func_4702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4702_call = mutated_mod.get_global_var('func_4702')
call_4703 = func_4702_call()
output = call_4703
func_4704 = relay.Function([], output)
mutated_mod['func_4704'] = func_4704
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4752 = relay.var("var_4752", dtype = "float64", shape = (7, 2, 9))#candidate|4752|(7, 2, 9)|var|float64
uop_4753 = relay.sinh(var_4752.astype('float64')) # shape=(7, 2, 9)
bop_4755 = relay.equal(uop_4753.astype('bool'), relay.reshape(var_4752.astype('bool'), relay.shape_of(uop_4753))) # shape=(7, 2, 9)
func_4414_call = mod.get_global_var('func_4414')
func_4417_call = mutated_mod.get_global_var('func_4417')
const_4765 = relay.const([-5,3,-10,7,-9,-1,10,-7,-7,-9,4,5,5,4,-7,7,9,-7,6,-4,-5,-5,2,-3,3,-5,10,-2,7,4,-8,-5,-8,9,-6,-10,5,-7,-7,5,-2,8,-2,9,-4,-1,-4,3,-9,-8,3,-8,-3,-7,-5,10,-5,-1,9,-6], dtype = "int16")#candidate|4765|(60,)|const|int16
call_4764 = relay.TupleGetItem(func_4414_call(relay.reshape(const_4765.astype('int16'), [3, 2, 10])), 0)
call_4766 = relay.TupleGetItem(func_4417_call(relay.reshape(const_4765.astype('int16'), [3, 2, 10])), 0)
bop_4771 = relay.bitwise_or(bop_4755.astype('uint16'), relay.reshape(uop_4753.astype('uint16'), relay.shape_of(bop_4755))) # shape=(7, 2, 9)
uop_4781 = relay.log(uop_4753.astype('float64')) # shape=(7, 2, 9)
output = relay.Tuple([call_4764,const_4765,bop_4771,uop_4781,])
output2 = relay.Tuple([call_4766,const_4765,bop_4771,uop_4781,])
func_4791 = relay.Function([var_4752,], output)
mod['func_4791'] = func_4791
mod = relay.transform.InferType()(mod)
var_4792 = relay.var("var_4792", dtype = "float64", shape = (7, 2, 9))#candidate|4792|(7, 2, 9)|var|float64
output = func_4791(var_4792)
func_4793 = relay.Function([var_4792], output)
mutated_mod['func_4793'] = func_4793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3042_call = mod.get_global_var('func_3042')
func_3044_call = mutated_mod.get_global_var('func_3044')
call_4795 = relay.TupleGetItem(func_3042_call(), 1)
call_4796 = relay.TupleGetItem(func_3044_call(), 1)
func_2680_call = mod.get_global_var('func_2680')
func_2682_call = mutated_mod.get_global_var('func_2682')
call_4803 = relay.TupleGetItem(func_2680_call(), 0)
call_4804 = relay.TupleGetItem(func_2682_call(), 0)
func_2680_call = mod.get_global_var('func_2680')
func_2682_call = mutated_mod.get_global_var('func_2682')
call_4807 = relay.TupleGetItem(func_2680_call(), 0)
call_4808 = relay.TupleGetItem(func_2682_call(), 0)
func_2936_call = mod.get_global_var('func_2936')
func_2939_call = mutated_mod.get_global_var('func_2939')
var_4812 = relay.var("var_4812", dtype = "float32", shape = ())#candidate|4812|()|var|float32
call_4811 = func_2936_call(relay.reshape(var_4812.astype('float32'), []))
call_4813 = func_2936_call(relay.reshape(var_4812.astype('float32'), []))
output = relay.Tuple([call_4795,call_4803,call_4807,call_4811,var_4812,])
output2 = relay.Tuple([call_4796,call_4804,call_4808,call_4813,var_4812,])
func_4825 = relay.Function([var_4812,], output)
mod['func_4825'] = func_4825
mod = relay.transform.InferType()(mod)
var_4826 = relay.var("var_4826", dtype = "float32", shape = ())#candidate|4826|()|var|float32
output = func_4825(var_4826)
func_4827 = relay.Function([var_4826], output)
mutated_mod['func_4827'] = func_4827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3042_call = mod.get_global_var('func_3042')
func_3044_call = mutated_mod.get_global_var('func_3044')
call_4845 = relay.TupleGetItem(func_3042_call(), 1)
call_4846 = relay.TupleGetItem(func_3044_call(), 1)
func_3087_call = mod.get_global_var('func_3087')
func_3092_call = mutated_mod.get_global_var('func_3092')
const_4863 = relay.const([[-8.898335,8.643828,-5.628198,2.371534,-6.516435],[0.208310,-0.780864,5.664693,1.126684,-2.266795],[-0.774621,9.283395,-3.596592,7.628063,-9.455165],[6.537912,-0.341867,4.999762,8.044309,7.516553],[-1.520997,3.913032,-4.570052,5.887367,4.449778],[0.549645,-9.846551,-2.400055,-2.042850,3.230625],[-9.518776,4.932465,8.264593,-7.505881,-0.011347],[-5.018582,-8.708351,6.028003,-7.433320,-5.751730],[-3.945029,2.288814,-0.417033,-4.787029,7.078891],[-0.947235,-5.036691,6.446718,-6.790174,-0.781504],[5.879900,6.344648,1.106665,7.452597,-8.328203],[7.723968,4.835278,9.100161,7.175739,-8.534256],[9.119780,-7.683890,5.308422,2.000179,3.815920],[-7.395307,-4.203553,7.682412,-7.169852,8.627236],[-3.732866,0.352228,-6.040275,-5.301385,-7.494164],[-1.960562,4.951083,0.401443,-8.500571,-3.405398],[1.468860,1.171621,2.806265,5.297362,8.909611],[-3.173024,8.054372,1.705763,-8.468934,5.705982],[5.800563,-5.197795,0.009769,1.194091,-6.951714],[0.390938,-8.282128,3.253142,6.007879,8.052305],[8.252878,4.182248,6.458600,-7.155344,-3.005236],[8.825311,-2.748427,-2.603639,8.185045,5.595138],[1.014842,3.936817,2.203196,4.450596,9.649491],[5.453143,-5.500336,-5.064222,-5.401582,4.658505],[-5.133817,-5.977986,-1.642070,-1.408661,-9.691493],[9.233920,6.584639,0.152306,2.428318,3.267216],[9.178276,-4.097560,7.248738,5.617801,9.354498],[-2.779621,2.916228,-9.899001,1.746612,-3.931474],[8.046522,-1.945421,-1.481467,0.989177,-8.557885],[0.455404,-3.126526,-2.970500,-8.936600,8.932164],[-0.916029,8.624659,-2.891506,-3.533427,3.946535],[0.092354,-3.528028,3.694191,0.636239,3.649694],[2.660571,3.641910,-8.808820,-7.513581,1.150006]], dtype = "float64")#candidate|4863|(33, 5)|const|float64
var_4864 = relay.var("var_4864", dtype = "int32", shape = (84,))#candidate|4864|(84,)|var|int32
var_4865 = relay.var("var_4865", dtype = "int32", shape = (672,))#candidate|4865|(672,)|var|int32
call_4862 = relay.TupleGetItem(func_3087_call(relay.reshape(const_4863.astype('float64'), [165,]), relay.reshape(var_4864.astype('int32'), [84,]), relay.reshape(var_4865.astype('int32'), [1, 672]), ), 7)
call_4866 = relay.TupleGetItem(func_3092_call(relay.reshape(const_4863.astype('float64'), [165,]), relay.reshape(var_4864.astype('int32'), [84,]), relay.reshape(var_4865.astype('int32'), [1, 672]), ), 7)
output = relay.Tuple([call_4845,call_4862,const_4863,var_4864,var_4865,])
output2 = relay.Tuple([call_4846,call_4866,const_4863,var_4864,var_4865,])
func_4875 = relay.Function([var_4864,var_4865,], output)
mod['func_4875'] = func_4875
mod = relay.transform.InferType()(mod)
var_4876 = relay.var("var_4876", dtype = "int32", shape = (84,))#candidate|4876|(84,)|var|int32
var_4877 = relay.var("var_4877", dtype = "int32", shape = (672,))#candidate|4877|(672,)|var|int32
output = func_4875(var_4876,var_4877,)
func_4878 = relay.Function([var_4876,var_4877,], output)
mutated_mod['func_4878'] = func_4878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1864_call = mod.get_global_var('func_1864')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_4910 = func_1864_call()
call_4911 = func_1864_call()
func_2446_call = mod.get_global_var('func_2446')
func_2448_call = mutated_mod.get_global_var('func_2448')
call_4914 = relay.TupleGetItem(func_2446_call(), 1)
call_4915 = relay.TupleGetItem(func_2448_call(), 1)
output = relay.Tuple([call_4910,call_4914,])
output2 = relay.Tuple([call_4911,call_4915,])
func_4918 = relay.Function([], output)
mod['func_4918'] = func_4918
mod = relay.transform.InferType()(mod)
mutated_mod['func_4918'] = func_4918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4918_call = mutated_mod.get_global_var('func_4918')
call_4919 = func_4918_call()
output = call_4919
func_4920 = relay.Function([], output)
mutated_mod['func_4920'] = func_4920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1739_call = mod.get_global_var('func_1739')
func_1741_call = mutated_mod.get_global_var('func_1741')
call_5007 = relay.TupleGetItem(func_1739_call(), 0)
call_5008 = relay.TupleGetItem(func_1741_call(), 0)
output = call_5007
output2 = call_5008
func_5014 = relay.Function([], output)
mod['func_5014'] = func_5014
mod = relay.transform.InferType()(mod)
mutated_mod['func_5014'] = func_5014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5014_call = mutated_mod.get_global_var('func_5014')
call_5015 = func_5014_call()
output = call_5015
func_5016 = relay.Function([], output)
mutated_mod['func_5016'] = func_5016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2701_call = mod.get_global_var('func_2701')
func_2703_call = mutated_mod.get_global_var('func_2703')
call_5083 = func_2701_call()
call_5084 = func_2701_call()
output = relay.Tuple([call_5083,])
output2 = relay.Tuple([call_5084,])
func_5121 = relay.Function([], output)
mod['func_5121'] = func_5121
mod = relay.transform.InferType()(mod)
output = func_5121()
func_5122 = relay.Function([], output)
mutated_mod['func_5122'] = func_5122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1759_call = mod.get_global_var('func_1759')
func_1760_call = mutated_mod.get_global_var('func_1760')
call_5126 = func_1759_call()
call_5127 = func_1759_call()
output = call_5126
output2 = call_5127
func_5138 = relay.Function([], output)
mod['func_5138'] = func_5138
mod = relay.transform.InferType()(mod)
output = func_5138()
func_5139 = relay.Function([], output)
mutated_mod['func_5139'] = func_5139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3429_call = mod.get_global_var('func_3429')
func_3431_call = mutated_mod.get_global_var('func_3431')
call_5182 = relay.TupleGetItem(func_3429_call(), 1)
call_5183 = relay.TupleGetItem(func_3431_call(), 1)
output = call_5182
output2 = call_5183
func_5191 = relay.Function([], output)
mod['func_5191'] = func_5191
mod = relay.transform.InferType()(mod)
output = func_5191()
func_5192 = relay.Function([], output)
mutated_mod['func_5192'] = func_5192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2576_call = mod.get_global_var('func_2576')
func_2577_call = mutated_mod.get_global_var('func_2577')
call_5197 = relay.TupleGetItem(func_2576_call(), 0)
call_5198 = relay.TupleGetItem(func_2577_call(), 0)
output = relay.Tuple([call_5197,])
output2 = relay.Tuple([call_5198,])
func_5231 = relay.Function([], output)
mod['func_5231'] = func_5231
mod = relay.transform.InferType()(mod)
mutated_mod['func_5231'] = func_5231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5231_call = mutated_mod.get_global_var('func_5231')
call_5232 = func_5231_call()
output = call_5232
func_5233 = relay.Function([], output)
mutated_mod['func_5233'] = func_5233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2576_call = mod.get_global_var('func_2576')
func_2577_call = mutated_mod.get_global_var('func_2577')
call_5307 = relay.TupleGetItem(func_2576_call(), 0)
call_5308 = relay.TupleGetItem(func_2577_call(), 0)
output = relay.Tuple([call_5307,])
output2 = relay.Tuple([call_5308,])
func_5316 = relay.Function([], output)
mod['func_5316'] = func_5316
mod = relay.transform.InferType()(mod)
output = func_5316()
func_5317 = relay.Function([], output)
mutated_mod['func_5317'] = func_5317
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5334 = relay.var("var_5334", dtype = "float64", shape = (11, 5, 6))#candidate|5334|(11, 5, 6)|var|float64
uop_5335 = relay.cosh(var_5334.astype('float64')) # shape=(11, 5, 6)
output = uop_5335
output2 = uop_5335
func_5370 = relay.Function([var_5334,], output)
mod['func_5370'] = func_5370
mod = relay.transform.InferType()(mod)
var_5371 = relay.var("var_5371", dtype = "float64", shape = (11, 5, 6))#candidate|5371|(11, 5, 6)|var|float64
output = func_5370(var_5371)
func_5372 = relay.Function([var_5371], output)
mutated_mod['func_5372'] = func_5372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3282_call = mod.get_global_var('func_3282')
func_3284_call = mutated_mod.get_global_var('func_3284')
call_5399 = relay.TupleGetItem(func_3282_call(), 3)
call_5400 = relay.TupleGetItem(func_3284_call(), 3)
func_3087_call = mod.get_global_var('func_3087')
func_3092_call = mutated_mod.get_global_var('func_3092')
const_5433 = relay.const([8.876933,-0.664584,6.066734,-3.027681,-6.634429,9.312145,-5.815358,-7.948840,1.923797,-5.242527,-2.982047,-3.394371,-1.954422,-4.083037,1.541950,6.129454,-9.192779,-3.435582,-6.566487,-3.441323,-9.481523,-2.949698,-1.092281,-2.603817,-9.558999,3.751089,-7.031066,-0.348794,6.169842,-4.001237,6.652983,9.124354,0.068454,2.824848,-1.229772,6.425561,3.120814,3.147325,-0.460449,-2.184263,-4.485887,0.088353,7.953808,8.387484,0.890884,7.305315,0.808415,-9.598877,-6.967544,-6.834478,-9.511733,9.060752,8.326934,2.368795,-6.584860,-3.322516,0.218018,0.073119,9.277961,7.945368,-5.482939,8.166093,1.208409,1.777455,6.238791,-8.238426,5.103135,-1.247584,-4.749753,-4.794273,7.887722,4.079091,4.402141,8.176844,1.332633,4.832298,5.720032,8.929781,-8.137160,-6.898191,-4.789526,9.113668,2.352885,-9.892838,4.323218,-5.584393,-9.272216,9.160349,8.130174,-0.297456,9.995048,-8.699181,2.705857,2.340891,-4.261946,7.265968,-3.883567,-4.078676,-2.431071,4.844350,-7.857316,-5.373797,1.815659,-3.728652,-7.562937,0.499349,-7.213291,-7.681697,0.877260,0.228112,-0.676476,-0.530250,-5.419409,-3.546992,-3.534168,-7.207188,6.549966,6.780347,9.862976,3.823817,-3.965200,3.127367,2.436338,-1.912452,-1.970637,-8.041850,3.631293,4.132929,-0.690711,-4.085625,-5.761337,6.052643,-3.219741,-1.073529,-2.165858,8.497537,7.087164,6.389525,9.841501,5.937033,1.243839,-3.409458,5.597058,-7.258009,1.104901,-1.722030,-1.767084,0.795590,-3.943251,-5.148963,-4.627308,7.205228,-2.286086,-7.663934,8.259623,4.676195,2.868136,0.760488,-7.760759,-6.842676,-2.389669,1.547602,-8.592153,7.222770,-3.912882], dtype = "float64")#candidate|5433|(165,)|const|float64
const_5434 = relay.const([8,8,4,5,-7,10,7,2,5,5,4,2,-3,5,6,8,4,1,9,7,4,-4,5,9,8,6,10,-9,1,-2,-10,10,6,3,9,1,-7,-6,-1,-4,1,-10,-8,-5,-3,-7,-7,8,-10,9,10,5,-3,2,6,-2,6,7,8,-4,-10,7,-9,9,7,1,5,9,-4,3,-6,6,-6,-7,-4,-9,-3,-2,-1,-4,-8,-8,-8,5], dtype = "int32")#candidate|5434|(84,)|const|int32
const_5435 = relay.const([-4,3,-7,1,-3,-5,1,-9,2,3,-10,8,6,-4,-10,8,-6,-1,10,-4,-1,7,9,-3,6,7,-7,-6,3,-5,-3,-8,-4,9,-5,8,6,-5,1,-5,6,-5,-9,7,10,-8,4,9,6,-3,5,-4,5,7,9,-5,6,-7,2,8,7,5,1,-1,-6,-8,6,-3,3,-8,-1,-7,-4,3,-10,8,-8,-1,6,8,8,4,-9,-4,-4,7,7,4,8,-5,-10,-8,-5,7,-2,-5,2,6,-4,-6,-5,8,6,-3,-9,3,-3,-8,-1,-2,-2,5,4,-7,-4,-1,-3,10,10,4,-4,-1,-9,5,-5,-4,4,1,3,-8,-1,7,-5,3,-2,7,5,5,6,-7,9,-8,-5,10,-6,-4,-7,-3,9,10,-5,7,2,8,-2,-8,8,-3,-4,-10,1,-9,6,1,-8,-5,7,-4,6,6,9,-8,-10,8,1,-6,4,1,7,-3,4,-9,2,9,-9,5,-10,3,-3,2,10,8,-3,-2,-2,9,-5,-6,-4,-6,-9,9,5,9,-4,3,1,8,2,-6,6,-2,-4,1,-1,-2,-9,2,-4,3,-2,-4,2,6,-1,-10,-8,10,-9,1,-8,-4,4,1,7,-8,4,3,-3,8,3,-2,8,-4,-3,-9,-8,7,9,1,-6,6,-8,-4,9,-4,-9,5,8,-8,-6,1,-10,-7,-8,4,7,2,10,-4,-7,3,-7,-7,2,6,-2,4,-5,10,1,-9,-5,-4,6,-8,-8,-3,1,-10,5,1,-2,9,7,-3,5,-9,-3,-9,-10,-6,-8,-3,-10,2,-6,-5,7,8,-5,-6,-2,-3,5,6,7,-6,-10,3,-2,7,7,8,8,-10,6,-3,9,3,-8,-1,-10,9,6,2,-9,7,3,-10,1,5,-7,4,-6,2,-8,8,-10,10,1,5,2,-5,-7,-7,-4,4,3,-7,-6,3,-4,2,8,-1,7,-10,-7,-6,-8,3,-7,5,-8,9,3,-10,10,2,-7,10,10,2,3,-6,-3,6,9,-10,-6,-2,10,8,5,10,5,-5,10,-6,7,5,-2,-2,4,7,2,1,-1,-1,-10,-2,3,-4,5,7,4,4,4,-7,7,-10,-1,-10,-9,3,-6,-6,2,-1,2,1,-9,-1,10,-3,10,-7,-4,7,1,-5,-5,-5,3,-4,-5,10,-7,-1,9,-5,5,3,-8,-3,10,-6,-8,-10,9,5,-8,-10,-8,-3,4,9,7,-9,2,-3,-1,-9,-8,-2,-2,2,4,4,-2,-10,-4,-6,-2,-5,-8,-9,7,-7,-7,-3,6,9,-9,1,-2,8,1,-9,10,7,4,4,-2,-8,10,9,7,5,3,-7,-8,-2,-8,1,-5,-5,-4,10,-2,6,10,-1,3,4,3,-10,-8,-1,3,6,10,-7,-2,2,-5,-9,2,-5,5,1,-3,-10,-1,-9,5,-2,-7,-9,8,-3,10,10,-2,-8,-6,-5,-8,-10,-8,-5,2,-7,-8,8,-10,1,-2,3,-7,1,10,2,2,8,9,-4,5,-10,10,9,8,1,2,-6,-4,4,-6,1,6,-10,5,4,7,-2,-1,-6,-2,2,10,-7,-8,6,5,2,9,4,7,-3,-3,1,8,6,-4,-6,-6,-9,-3,-8,4,-8,3,-6,-2,-7,4,1,-5,3,-5,6,-3,-6,1,5,-6,-6,-6,1,3,-5,6,-10,2,2,4,9,-4,6,-10,9,-3,-7,9,-7,8,1,5,-6,-5,-6,-8,-8,3,6,-4,-1,1,-4,-8,5], dtype = "int32")#candidate|5435|(672,)|const|int32
call_5432 = relay.TupleGetItem(func_3087_call(relay.reshape(const_5433.astype('float64'), [165,]), relay.reshape(const_5434.astype('int32'), [84,]), relay.reshape(const_5435.astype('int32'), [1, 672]), ), 0)
call_5436 = relay.TupleGetItem(func_3092_call(relay.reshape(const_5433.astype('float64'), [165,]), relay.reshape(const_5434.astype('int32'), [84,]), relay.reshape(const_5435.astype('int32'), [1, 672]), ), 0)
output = relay.Tuple([call_5399,call_5432,const_5433,const_5434,const_5435,])
output2 = relay.Tuple([call_5400,call_5436,const_5433,const_5434,const_5435,])
func_5438 = relay.Function([], output)
mod['func_5438'] = func_5438
mod = relay.transform.InferType()(mod)
output = func_5438()
func_5439 = relay.Function([], output)
mutated_mod['func_5439'] = func_5439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1510_call = mod.get_global_var('func_1510')
func_1511_call = mutated_mod.get_global_var('func_1511')
call_5469 = relay.TupleGetItem(func_1510_call(), 0)
call_5470 = relay.TupleGetItem(func_1511_call(), 0)
func_4617_call = mod.get_global_var('func_4617')
func_4621_call = mutated_mod.get_global_var('func_4621')
var_5477 = relay.var("var_5477", dtype = "float64", shape = (11, 15))#candidate|5477|(11, 15)|var|float64
const_5478 = relay.const([[-8,3,5,-7,-6,10,9,-5,6,-2,9,10,-2,-4,-10,1,7,5,5,10,1,7,9,8,2,-8,7,10,2,-6,-8,-2,1,8,7,1,-10,-8,10,4,6,-2,10,2,4,4,-5,1,-2,-3,-7,-7,-1,-3,2,5,-9,-3,-9,-1,-5,8,-9,-5,8,-2,-10,-9,5,-6,-1,-7,9,1,6,-4,-5,8,-1,-7,-1,-1,7,4],[4,-8,-2,-7,-4,-3,-10,-9,9,-1,10,-9,-8,-2,2,6,7,-3,9,-1,8,-1,-3,3,2,2,3,-5,-6,5,-4,-6,-7,1,8,-6,8,-5,2,2,-4,-5,8,10,-6,3,-8,-10,-7,10,5,-4,-5,-3,-8,10,1,-9,-5,4,5,-3,8,7,-6,-3,-3,3,5,-7,-3,5,2,7,-2,-1,10,-10,-7,4,-6,-4,3,8],[-5,2,-2,6,-2,3,3,1,-8,-10,1,-8,-10,-5,10,-4,8,5,-3,-6,-1,9,5,-5,-4,-7,10,2,-8,4,4,-2,-6,-4,7,5,9,10,-5,-8,-2,6,2,4,8,-9,8,5,-8,4,-9,3,-1,3,-10,9,-5,5,-4,7,-9,-4,-8,2,8,-3,-2,-6,-1,-3,1,6,6,3,-2,-1,1,-9,-6,6,8,-10,10,-5],[6,-4,9,-5,1,4,10,-6,5,-9,10,-5,-9,-9,3,-9,-2,-8,-3,4,10,-9,7,3,-3,-1,2,-1,10,-9,4,6,1,4,6,9,-8,-10,6,-5,10,3,-1,-2,-4,6,8,-1,5,-4,5,-10,-4,10,-6,10,-2,-7,-9,5,-9,-1,-4,-8,10,-1,7,-10,4,2,4,5,7,8,-10,-9,-6,5,-5,-9,7,1,-3,-7],[-2,8,-3,1,-6,3,-2,4,3,7,2,-4,-8,-5,8,10,2,-6,-5,-2,8,7,-10,-9,10,-2,10,3,2,8,9,4,10,-6,-8,5,4,5,5,-8,8,9,-7,-7,-10,3,-7,-3,-6,1,7,-10,-10,-6,1,-1,-5,8,-3,-5,3,4,-4,4,-6,-3,-3,-4,10,-7,4,-9,-8,-3,5,4,5,-6,7,-8,-7,5,-8,2],[-9,-8,-6,-5,7,3,-7,7,-7,10,5,6,-3,-1,-2,-8,1,-5,4,-1,-10,-10,-3,7,-2,-5,-9,8,-4,2,1,6,-3,-6,2,7,-2,-7,5,-7,4,-3,-3,-2,1,4,3,1,2,4,-7,-6,-7,-5,8,1,-4,-5,-7,-5,-1,8,8,2,9,3,-7,4,-3,-8,3,-5,4,-5,6,-7,8,3,-5,7,10,-1,-3,3],[-5,9,10,4,-3,-3,10,8,-7,5,7,-7,4,-6,-2,2,-7,5,4,-1,10,-8,6,-10,10,-5,7,-5,-10,7,7,-9,-10,-4,-8,5,-1,-10,-8,9,4,-4,6,4,-10,7,-10,-4,3,-9,4,-8,-7,-1,-9,-5,-6,5,-8,-7,-10,8,3,4,-1,-6,7,10,-4,-8,-3,5,-2,1,-7,-10,3,1,-9,1,-8,-5,-2,-6],[7,-7,-7,-10,-3,10,-9,9,6,9,4,3,8,-4,4,5,8,-2,6,-5,-2,1,3,7,-1,-3,8,-7,-6,5,5,-1,-5,7,4,-2,-4,10,-4,-5,1,10,-7,-6,-9,5,2,-4,-9,-10,-2,-9,-5,4,-4,-6,10,-6,4,10,-4,7,10,-5,-4,-10,-7,-3,-8,6,7,-10,-10,3,-10,-9,-7,2,-10,4,2,-2,-5,-5]], dtype = "int32")#candidate|5478|(8, 84)|const|int32
call_5476 = relay.TupleGetItem(func_4617_call(relay.reshape(var_5477.astype('float64'), [165,]), relay.reshape(const_5478.astype('int32'), [336, 2]), ), 7)
call_5479 = relay.TupleGetItem(func_4621_call(relay.reshape(var_5477.astype('float64'), [165,]), relay.reshape(const_5478.astype('int32'), [336, 2]), ), 7)
output = relay.Tuple([call_5469,call_5476,var_5477,const_5478,])
output2 = relay.Tuple([call_5470,call_5479,var_5477,const_5478,])
func_5495 = relay.Function([var_5477,], output)
mod['func_5495'] = func_5495
mod = relay.transform.InferType()(mod)
mutated_mod['func_5495'] = func_5495
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5496 = relay.var("var_5496", dtype = "float64", shape = (11, 15))#candidate|5496|(11, 15)|var|float64
func_5495_call = mutated_mod.get_global_var('func_5495')
call_5497 = func_5495_call(var_5496)
output = call_5497
func_5498 = relay.Function([var_5496], output)
mutated_mod['func_5498'] = func_5498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5191_call = mod.get_global_var('func_5191')
func_5192_call = mutated_mod.get_global_var('func_5192')
call_5518 = func_5191_call()
call_5519 = func_5191_call()
func_336_call = mod.get_global_var('func_336')
func_340_call = mutated_mod.get_global_var('func_340')
const_5523 = relay.const([-4,7,-7,-5,4,3,7,10,-3,-4,8,-2,8,9,-7,-7,-7,4,5,-8,7,-10,7,-6,-3,-3,4,3,-7,5,-3,4,-9,3,-8,-6,10,1,8,-2,-10,3,-2,6,-9,3,7,9,6,9,-2,-2,1,-2,1,-9,10,-4,8,-2,-5,10,-2,8,-2,-5,2,-7,-1,3,2,2,5,4,10,-4,-1,-6,3,3,1,-10,-5,7,3,-7,-5,8,-9,-5,8,-3,-4,-2,-1,2,2,4,-8,-3,-4,-7,1,8,8,8,-3,-5,-8,-3,1,-10,9,2,8,10,8,-10,5,-1,-1,8,-10,2,9,8,5,5,-3,-3,4,2,1,3,9,-8,6,8,-9,5,-10,-8,-8,-10,9,1,-7,5,6,5,-5,8,10,-7,-8,9,-3,4,-9,6,10,-1,-2,-6,-6,4,5,-3,9,6,-4,7,1,1,-8,9,-4,-4,9,-7,-2,-8,-4,-3,-3,-2,5,4,-3,-7,-4,8,9,6,-3,-4,-3,-3,5,10,7,5,-3,10,-4,8,5,7,9,3,6,6,-2,-6,7,5,8,-7,-8,9,-2,-1,-3,3,2,4,5,-7,7,4,-7,-7,10,8,-1,-4,-1,1,5,-6,10,-5,9,4,3,-1,8,7,-2,-7,-9,-5,6,-6,10,8,-3,-6,4,8,7,-10,-7,-4,4,-3,4,7,4,1,-7,-5,-1,-5,-3,4,2,7,-5,-10,4,-3,-1,-8,-6,-10,-7,5,10,-5,-3,-2,-5,6,-10,10,-10,-2,-5,-8,9,-4,-5,-6,-9,7,-4,-6,-8,10,1,-1,2,1,-4,-6,9,9,1,10,-8,3,-5,-2,3,10,9,4,7,-7,-6,-1,-7,10,8,9,6,10,10,6,-2,-7,10,-10,-9,-7,4,-10,10,6,-10,6,6,9,5,-9,-4,8,10,-10,-7,-1,-6,-9,-1,-6,1,-8,5,-4,5,-7,-2,10,3,10,-8,10,-4,-10,-5,5,-8,4,2,-4,-1,-3,-6,-6,6,10,7,-8,10,-5,6,-2,4,-8,3,-3,-2,9,3,8,1,3,-7,-10,-9,-1,-6,-9,-8,1,6,-8,-2,8,-2,5,2,1,9,6,6,-2,10,-5,6,-10,9,3,-4,-9,5,8,-3,1,-8,-9,4,-7,3,-5,-7,3,4,9,7,2,1,-1,1,-6,1,-5,7,1,5,10,2,10,-9,2,7,10,-8,-4,-5,9,-8,-10,6,6,9,3,-1,-7,-4,-8,5,-2,-1,3,9,-3,-4,-3,-6,2,-8,9,2,2,5,8,10,-4,-6,-8,-6,-3,3,3,-8,-7,3,-6,1,10,9,-5,-8,1,-5,1,1,-4,-2,6,-3,6,10,-3,-9,-5,3,-9,-9,6,-1,-5,-3,-9,-7,4,-9,-8,-2,9,5,10,-6,-8,-9,-8,1,5,2,8,-10,-9,-5,-9,9,-8,4,2,-7,4,5,10,-5,10,10,7,2,-10,-5,4,9,-8,-10,-4,1,6,-1,-1,-3,4,-1,-3,8,-2,4,-9,-7,-9,-9,7,2,7,-10,-2,1,4,6,7,-5,-9,6,-4,-6,10,-8,5,-10,7,-1,3,-2,6,-8,-4,-3,-2,10,1,-10,1,-10,10,-9,10,-4,3,-1,8,3,10,4,6,7,9,-8,5,-5,8,2,5,2,-5,-9,2,-4,10,4,9,-3,7,9,1,-7,-9,8,8,-5,5,-4,8,7,6,-3,-3,3,10,-1,7,10,10,1,-10,-9,-10,1,-2,5,-10,-3,7,-2,-10,-7,-5,-3,7,-1,2,-3,4,10,2,4,-6,-6,2,9,3,7,7,2,-5,2,-4,10,8,-6,5,-4,-6,3,8,-8,-2,-8,-8,-2,5,10,10,9,-2,-8,-6,8,-3,-8,3,-2,4,3,-2,4,-8,7,6,7,3,-5,-10,-9,-1,3,-6,10,-9,-1,-9,-6,-9,6,1,5,9,-10,-10,1,7,-9,1,2,-4,8,-6,-2,-1,4,10,-3,7,7,2,3,1,4,-1,1,7,-1,-8,-10,1,-9,1,-1,7,10,-7,-1,-2,2,1,-3,7,-1,-8,3,5,2,6,-8,3,-2,-8,-9,-8,-6,-6,-7,-4,5,-9,3,2,2,9,9,-6,2,-6,6,2,2,2,9,8,-10,-2,-1,-8,-2,-2,7,-4,4,10,3,-2,9,6,2,2,1,4,-10,-6,9,3,-6,5,-6,-7,-8,-6,5,-3,-6,-8,10,-8,6,3,1,-1,7,-4,2,4,2,-5,1,-3,-4,3,-7,-4,-4,8,7,2,-5,6,10,9,7,-3,3,-5,-1,3,-9,10,-8,-9,-8,-8,9,-2,4,-5,7,-1,-3,9,5,1,1,-9,8,3,-1,8,-6,9,2,-1,1,9,-8,-8,-2,-9,8,3,6,-3,8,-6,-2,4,-10,-4,7,-5,-6,8,-1,1,4,7,-2,8,-10,6,-9,9,-5,10,-8,7,-7,-2,-3,-8,-8,9,-5,-2,1,-10,-6,2,2,3,9,4,4,-4,8,6,-1,6,9,-3,-5,1,-10,3,6,-3,-6,1,-4,9,-9,10,9,5,5,8,-1,-1,5,4,-2,4,-6,9,10,-4,2,-10,-1,9,-3,3,-10,-6,10,4,-8,9,-3,-6,6,-1,-3,1,8,-9,9,-4,6,-3,9,-8,6,-1,-6,2,-8,-2,6,4,-3,4,4,-10,9,9,-1,-4,-6,5,-3,-6,2,1,-1,-1,-7,6,-4,-4,-10,-10,1,9,3,1,-1,-7,3,10,-5,8,-5,-7,-1,-1,-5,-3,6,-6,-5,5,4,-10,3,2,-2,-2,-5,7,10,-8,-8,-3,-2,-3,6,7,-1,-8,1,-2,10,-2,-5,-10,9,-1,-10,1,-5,-3,2,2,6,-8,8,10,4,-3,-2,-3,3,-8,-10,7,5,6,-7,-1,-8,10,8,6,-5,-8,-1,8,7,-7,6,10,-1,9,7,-10,10,1,-3,10,5,5,-1,10,-8,2,-10,-5,1,8,5,-2,-2,-3,-9,1,10,-10,8,8,-8,1,-7,6,2,5,-3,-4,-10,-10,-9,7,-6,2,-8,1,5,1,-10,-9,2,-8,10,10,9,3,10,1,6,3,6,-9,7,2,-8,8,6,6,9,8,-7,-8,-10,6,-2,1,2,10,1,-7,-4,10,2,-6,6,-1,-6,2,7,5,7,-1,5,10,-5,6,3,-9,-3,-8,-10,2,7,5,1,5,-3,9,-10,-5,-10,-4,6,8,2,-8,4,-10,5,-4,5,-6,-8,8,8,2,-4,-10,2,10,3,-6,-10,-7,4,-3,1,-9,8,6,1,-3,4,3,-1,-10,3,-1,-6,9,-8,-1,4,1,-7,8,-4,-1,4,4,9,10,-4,4,-7,-2,-3,-7,2,9,-4,-7,7,7,-4,-5,-9,-2,5,-2,6,1,-8,-8,-6,-2,-3,-9,9,-4,-8,-3,-3,9,10,2,7,7,2,8,2,8,-8,-8,2,-9,10,-9,-8,2,-4,-4,-8,8,6,-7,5,4,4,-2,5,-9,5,9,-10,1,-7,-5,-6,8,9,10,3,-9,7,3,5,6,-2,1,-8,-4,-7,-2,3,7,-5,8,-3,3,10,-2,8,3,5,-9,-8,7,-5,-10,-9,2,4,-4,-9,-8,4,4,-10,-1,-10,-5], dtype = "uint32")#candidate|5523|(1408,)|const|uint32
const_5524 = relay.const([True,True,False,False,False,False,False,True,False,True,False,True,False,False,False,True,True,False,False,False,False,True,True,True,False,True,False,False,False,False,False,True,True,False,True,True,False,True,True,True,False,True,False,False,True,True,False,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,False,False,False,False,True,True,True,False,False,False,False,True,True,False,True,False,False,False,True,True,True,False,False,False,False,True,False,True,True,False,False,True,False,False,True,False,True,True,False,True,True,False,False,False,True,True,False,True,False,True,True,True,True,True,True,False,True,True,True,False,False,True,True,False,True,False,False,False,True,False,True,False,True,True,False,False,True,False,True,True,False,False,False,True,False,True,True,True,True,True,True,True,False,False,True,False,False,False,False,False,False,False,False,True,True,True,True,False,True,True,True,True,True,True,True,True,True,False,False,False,True,True,True,False,True,False,False,False,False,False,False,True,False,False,False,False,True,False,False,True,True,False,False,False,True,True,False,False,False,False,False,True,False,True,True,True,False,True,True,False,False,True,True,False,False,False,False,True,False,True,False,True,True,True,True,False,False,True,True,False,False,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,True,True,False,True,True,False,True,False,False,False,True,True,True,False,False,False,True,True,False,False,True,False,True,False,True,True,False,False,True,True,False,False,False,True,True,True,True,False,True,True,False,False,False,False,True,False,False,False,False,False,True,True,True,False,False,False,False,False,False,True,True,True,True,False,False,False,True,True,False,True,True,False,True,True,False,False,False,False,True,False,True,False,True,False,False,True,False,False,False,False,True,True,True,False,True,True,False,True,True,False,False,False,True,True,True,True,False,True,False,True,True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,True,True,False,True,False,False,True,False,True,True,True,True,True,False,True,False,False,False,False,False,True,False,False,False,True,True,False,False,True,True,True,True,False,False,False,False,False,True,False,True,False,False,False,False,False,True,False,False,False,True,True,True,True,True,True,False,True,True,False,False,False,False,True,True,False,False,True,False,True,False,True,False,False,True,False,False,True,False,False,True,True,True,False,False,True,False,True,False,True,True,False,False,True,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False,True,False,True,False,False,False,True,False,True,True,False,False,False,False,False,False,True,True,False,True,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False,True,False,False,True,True,True,True,True,True,True,True,True,False,True,True,False,False,True,False,True,False,False,True,False,True,True,True,True,False,True,False,True,True,False,False,False,True,False,True,True,True,True,False,False,False,False,False,False,True,False,True,True,False,False,True,False,False,False,True,False,True,True,True,False,True,True,False,True,True,False,False,True,True,False,True,True,False,True,True,True,True,False,False,True,True,False,True,True,False,True,True,False,False,False,False,False,True,True,True,True,True,True,False,False,True,True,True,False,False,False,True,True,False,False,False,True,False,False,False,False,True,True,False,True,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,False,False,False,False,False,False,False,False,False,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,False,False,True,True,False,False,False,False,True,False,True,True,True,True,False,True,True,True,True,True,False,False,True,True,False,True,True,True,False,True,False,False,True,True,False,False,False,False,False,True,True,True,False,False,False,False,True,False,True,False,True,False,False,False,True,True,False,False,False,False,True,False,False,True,False,False,True,False,True,True,True,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,True,True,False,True,False,False,False,True,False,False,False,False,True,False,True,True,True,True,True,False,True,True,False,False,True,True,False,True,False,False,True,False,True,True,True,False,True,True,True,False,False,False,False,True,False,False,True,True,True,False,True,False,True,True,False,False,False,False,False,True,True,True,True,False,False,False,False,True,False,False,True,False,False,False,True,False,False,False,True,True,True,False,True,False,False,True,True,False,False,True,True,True,False,False,True,False,True,False,True,True,False,True,True,False,True,False,False,True,True,True,False,False,True,True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,True,False,False,True,True,True,True,False,True,True,True,False,False,True,False,True,False,True,True,False,False,True,True,True,False,False,True,False,True,False,True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,True,True,True,False,False,True,False,True,False,True,True,True,True,False,False,True,True,True,True,True,False,False,True,True,True,True,False,True,False,False,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,True,True,False,True,True,False,False,False,True,True,True,True,False,True,False,True,True,False,True,False,True,False,True,False,False,True,False,False,True,True,True,False,True,True,True,False,True,True,True,False,False,False,False,False,False,False,False,True,True,True,True,False,False,True,False,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,True,False,False,True,False,False,False,True,True,False,True,True,True,False,False,True,True,True,True,True,True,False,True,True,True,True,True,False,False,True,False,True,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,False,True,True,True,True,False,True,False,True,False,True,True,True,True,False,False,True,True,True,True,True,False,False,False,True,True,True,True,False,True,True,False,False,False,False,True,False,True,False,True,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,True,False,False,False,False,True,True,True,True,True,True,True,True,False,True,False,True,False,False,True,False,True,True,True,True,False,True,False,False,True,True,True,True,False,False,False,True,True,True,True,True,False,False,False,False,True,True,True,True,True,False,True,False,True,False,True,True,True,True,False,False,True,True,False,True,True,False,False,True,True,True,False,True,True,False,True,False,True,False,True,True,False,False,True,True,False,True,False,True,False,False,False,True,False,False,False,True,False,True,False,True,False,False,False,False,True,True,False,False,True,False,True,True,False,True,False,True,False,False,False,False,True,False,False,True,False,False,False,False,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,True,True,False,False,True,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,False,True,False,False,True,False,True,True,True,False,True,False,True,False,False,True,True,False,True,True,True,True,False,True,True,True,True,True,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,True,True,False,False,True,True,True,True,False,True,False,False,True,True,True,True,True,True,True,True,False,True,False,False,True,False,True,True,True,False,True,True,True,True,True,True,True,True,False,True,False,False,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,True,True,False,False,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,True,False,False,False,True,False,True,False,True,True,False,False,False,True,False,True,True,False,False,True,False,False,False,True,True,False,False,False,False,True,True,True,True,True,True,True,True,False,True,True,False,True,True,False,False,False,True,True,False,False,False,False,False,False,False,True,True,False,True,True,True,False,False,False,False,False,True,True,False,False,False,False,True,False,True,True,False,False,True,False,False,True,False,False,False,False,False,True,False,True,False,True,False,False,False,False,False,True,True,True,False,False,True,True,False,False,True,False,True,False,False,True,True,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False,True,False,False,True,False,False,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,True,True,False,False,False,True,True,False,False,False,True,True,False,True,False,False,False,True,False,True,False,True,True,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,False,True,False,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,True,False,False,True,True,True,True,True,True,True,False,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,True,False,True,True,True,False,True,False,False,True,True,True,False,True,False,False,True,False,True,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,True,True,True,False,True,True,False,True,True,True,False,False,True,False,False,True,False,True,True,False,True,True,True,False,True,False,True,False,True,True,False,False,False,True,False,True,False,False,True,False,False,True,False,True,True,False,False,True,True,False,True,False,True,True,True,False,True,False,True,False,True,True,True,False,False,True,True,False,False,False,False,False,True,False,True,False,False,False,False,False,False,True,False,True,False,True,False,False,True,True,False,True,False,True,True,False,True,False,False,True,True,True,True,False,True,False,True,False,False,True,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True,True,False,False,True,False,False,False,False,True,True,False,True,False,False,True,True,False,True,False,False,False,True,False,True,False,False,False,False,False,False,True,True,False,True,False,False,False,True,False,True,False,False,False,False,True,False,True,True,True,True,True,False,True,False,True,True,False,False,False,False,False,True,True,False,True,True,True,True,False,True,False,True,False,False,True,True,False,True,False,False,False,False,False,True,False,True,True,False,True,True,False,True,False,True,False,True,False,True,False,True,False,False,False,False,True,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,True,True,False,False,True,True,True,False,True,True,False,False,False,False,True,False,False,True,True,True,True,True,False,True,False,True,True,False,False,True,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,False,True,False,False,True,True,True,True,True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,True,True,True,False,False,False,True,False,False,False,False,False,True,False,True,False,True,False,True,True,False,True,True,False,True,False,False,False,False,False,True,True,True,True,True,True,True,False,False,True,True,False,False,False,False,True,True,True,False,False,True,False,True,False,False,False,False,False,False,True,True,False,False,False,True,False,False,False,False,False,True,True,False,True,False,True,True,True,False,True,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,False,True,False,False,True,False,False,True,True,False,False,False,True,True,True,False,False,False,False,False,True,True,True,True,True,False,True,False,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,True,False,False,True,False,False,True,False,True,False,True,False,True,True,False,False,False,True,True,False,False,False,True,True,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,False,True,True,False,True,True,False,True,True,True,False,True,True,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,True,False,True,True,False,True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,False,False,True,False,False,False,False,True,True,True,True,True,True,False,True,True,True,True,True,True,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,True,False,True,False,True,False,True,True,False,False,True,True,True,False,True,True,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,True,True,True,False,True,False,False,True,False,True,False,False,False,True,True,False,False,True,True,False,True,False,False,False,False,True,False,False,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,False,True,True,False,False,False,True,True,True,False,False,False,False,False,False,True,False,False,False,False,True,True,True,True,False,True,False,False,True,True,True,True,False,False,True,False,True,False,True,False,False,True,False,False,True,True,False,True,True,False,True,False,True,True,False,True,False,False,False,True,True,True,False,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,True,False,True,False,False,True,False,True,False,True,False,False,False,True,True,False,True,False,False,True,True,False,True,True,False,True,False,False,False,True,False,True,True,True,True,True,True,False,False,True,True,False,True,False,True,False,False,True,True,False,False,False,False,False,True,False,True,True,False,True,False,False,False,True,False,True,False,True,True,False,False,True,False,True,True,True,True,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False,True,True,True,True,True,False,False,False,False,True,True,True,True,False,False,False,False,True,True,False,True,False,True,True,False,True,False,True,False,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,True,False,False,False,False,True,False,False,False,False,True,True,True,False,False,False,False,True,False,True,True,False,False,False,True,False,False,True,False,True,True,True,False,True,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,True,False,True,True,False,True,True,False,True,False,False,True,True,False,True,False,False,True,False,False,False,True,False,True,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,False,True,False,True,True,False,True,False,False,True,False,False,False,False,False,False,True,True,False,False,True,False,False,False,False,False,False,True,True,True,False], dtype = "bool")#candidate|5524|(2912,)|const|bool
call_5522 = relay.TupleGetItem(func_336_call(relay.reshape(const_5523.astype('uint32'), [8, 16, 11]), relay.reshape(const_5524.astype('bool'), [2912,]), ), 3)
call_5525 = relay.TupleGetItem(func_340_call(relay.reshape(const_5523.astype('uint32'), [8, 16, 11]), relay.reshape(const_5524.astype('bool'), [2912,]), ), 3)
func_2376_call = mod.get_global_var('func_2376')
func_2378_call = mutated_mod.get_global_var('func_2378')
call_5534 = relay.TupleGetItem(func_2376_call(), 0)
call_5535 = relay.TupleGetItem(func_2378_call(), 0)
func_4382_call = mod.get_global_var('func_4382')
func_4385_call = mutated_mod.get_global_var('func_4385')
const_5540 = relay.const([1.426198,-1.148187,-1.517945,6.480662,3.063313,-6.758945,-8.325593,0.554215,-6.497047,-1.509736,7.974092,-5.237676,-3.592810,-5.183034,1.530182,6.041200,-0.392244,0.682729,1.722167,-0.612333,4.926060,9.871706,5.501355,6.858877,0.940726,-0.709020,4.606596,-1.913657,8.971541,0.260010,-7.676897,8.012993,-2.161808,4.550334,1.359253,-6.239995,-2.161780,-2.457431,-0.093063,-2.559040,3.203870,-5.654406,6.202080,-7.147300,-5.077569,4.293894,-0.017003,1.226269,8.598941,-6.298281,-3.699543,-1.938261,-1.988090,-0.319830,-7.292027,0.269933,7.156346,-1.035929,-3.420038,8.681055,-9.654510,-4.433689,4.138435,9.021307,-3.079295,9.502599,-4.377560,-4.112581,-6.865948,-8.571782,0.801202,-2.502605,9.846356,4.568250,-2.166826,-4.377270,2.701763,4.962179,-1.534303,3.922880,0.601672,6.914931,-7.388709,-3.498772], dtype = "float64")#candidate|5540|(84,)|const|float64
call_5539 = relay.TupleGetItem(func_4382_call(relay.reshape(const_5540.astype('float64'), [84,])), 1)
call_5541 = relay.TupleGetItem(func_4385_call(relay.reshape(const_5540.astype('float64'), [84,])), 1)
output = relay.Tuple([call_5518,call_5522,const_5523,const_5524,call_5534,call_5539,const_5540,])
output2 = relay.Tuple([call_5519,call_5525,const_5523,const_5524,call_5535,call_5541,const_5540,])
func_5546 = relay.Function([], output)
mod['func_5546'] = func_5546
mod = relay.transform.InferType()(mod)
output = func_5546()
func_5547 = relay.Function([], output)
mutated_mod['func_5547'] = func_5547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2265_call = mod.get_global_var('func_2265')
func_2266_call = mutated_mod.get_global_var('func_2266')
call_5583 = func_2265_call()
call_5584 = func_2265_call()
func_4229_call = mod.get_global_var('func_4229')
func_4235_call = mutated_mod.get_global_var('func_4235')
var_5586 = relay.var("var_5586", dtype = "uint8", shape = (280,))#candidate|5586|(280,)|var|uint8
const_5587 = relay.const([[-1.751673,6.449140,-6.831654,-5.847235],[0.953631,-3.155900,6.501115,-0.534003],[5.794323,1.333240,-3.913583,-2.328403],[-5.381691,-2.038532,-8.358357,9.025209],[-6.818786,-2.536136,-4.350837,9.312452],[-7.246180,-4.932258,-4.774723,5.088303],[7.405354,8.032485,-4.770553,-8.994468],[3.700701,5.987511,8.325419,-4.973963],[0.995623,7.254510,2.100820,5.066758],[-7.809898,-8.473091,-9.304707,-0.130484],[-3.602823,2.246053,8.512838,3.596652],[-6.778348,0.798948,9.483107,2.712192],[-7.960020,-7.194019,9.456676,5.165337],[8.439128,-1.823954,6.174556,-4.656434]], dtype = "float64")#candidate|5587|(14, 4)|const|float64
const_5588 = relay.const([False,False,True,False,False,True,False,False,True,False,True,False,True,True,False,False,True,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,False,True,True,False,False,False,True,True,False,False,True,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,False,True,True,False,False,True,True,False,False,True,False,True,False,False,True,True,True,True,False,True,False,True,False,True,True,True,True,False,False,False,True,True,True,False,True,False,False,True,False,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,False,True,False,False,False,False,False,True,True,True,False,True,True,False,False,True,False,False,True,True,True,True,True,False,True,True,True,True,False,True,False,True,False,False,True,False,True,True,False,False,False,False,True,False,False,True,True,False,False,True,True,True,False,False,True,True,True,False,True,False,True,True,True,False,False,False,False,True,True,False,True,True,False,True,True,False,False,True,False,False,False,True,False,False,False,True,False,True,False,True,True,True,False,False,True,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,True,True,True,True,False,True,False,False,True,False,True,False,False,True,True,True,False,True,True,True,True,False,False,False,True,False,False,False,True,False,False,False,True,False,True,True,True,True,True,False,False,False,True,False,False,False,True,False,True,True,True,False,True,False,False,False,False,True,False,True,True,True,True,False,True,False,False,False,False,True,True,False,False,False,False,False,False,True,False,True,False,True,False,True,True,False,True,False,True,False,True,False,True,True,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,False,True,True,False,True,True,True,True,False,True,True,False,True,True,True,False,False,True,True,True,False,True,False,True,False,False,True,False,True,False,True,True,True,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,True,True,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False,True,False,True,False,False,True,False,True,False,False,False,False,True,True,True,False,True,True,False,False,False,True,True,False,True,True,False,True,False,False,True,True,True,False,True,True,False,False,True,False,False,True,False,True,False,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,True,True,True,False,True,True,False,True,True,True,True,True,False,True,False,False,True,False,True,True,True,True,False,False,True,False,True,True,True,True,True,True,False,False,True,False,True,True,True,False,False,True,True,False,False,False,False,True,False,False,True,True,True,True,False,False,True,True,True,True,True,False,False,True,True,True,True,False,True,True,True,True,False,False,False,False,False,False,False,True,False,True,False,True,False,False,False,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,True,False,True,True,True,True,False,True,False,True,True,False,True,True,False,True,False,False,False,False,True,True,True,True,True,True,False,False,True,False,True,False,True,False,False,False,False,False,True,False,True,False,True,True,True,True,False,False,True,True,False,False,False,False,True,True,True,True,True,False,False,False,True,True,False,True,True,False,True,False,True,True,True,False,False,False,True,False,False,False,True,True,True,True,True,False,False,False,False,True,False,False,True,True,True,False,False,False,False,False,False,True,True,True,True,True,False,False,True,False,True,True,True,False,False,False,False,True,False,False,False,True,False,False,False,True,False,True,True,False,True,False,False,False,True,True,True,True,False,False,False,True,True,True,True,False,False,True,True,False,False,True,True,False,True,False,False,True,True,True,False,False,True,False,False,True,True,True,False,True,True,False,False,True,False,True,True,False,True,False,False,True,True,False,True,True,False,True,False,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,False,False,True,True,False,False,True,True,True,True,True,True,False,True,False,False,False,True,True,True,False,True,False,True,True,False,True,True,True,False,True,False,False,False,True,True,True,True,False,False,False,True,True,False,False,False,False,False,True,True,True,True,True,True,True,False,True,False,True,False,False,False,False,True,True,False,False,False,True,False,False,True,True,False,True,True,False,True,True,True,True,False,True,False,True,False,False,False,False,False,False,True,False,True,False,True,True,False,True,False,False,False,True,True,False,False,False,False,True,True,True,False,True,False,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,False,False,False,True,True,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,False,False,True,False,True,False,False,True,True,True,False,True,False,False,False,False,False,True,True,True,True,False,False,False,True,False,False,False,False,False,True,False,False,True,False,True,True,False,True,False,True,True,True,True,True,True,True,False,True,False,True,False,False,True,True,True,True,True,True,True,True,True,True,False,False,True,True,True,True,False,True,False,True,True,True,True,False,False,True,True,False,False,False,False,True,True,True,False,False,False,True,False,True,False,False,True,True,True,False,False,False,False,False,True,True,True,False,True,True,True,True,True,True,True,True,False,False,False,False,False,False,True,False,False,True,False,True,False,False,False,False,False,False,False,True,True,True,False,False,False,True,True,True,True,False,False,True,False,False,False,True,True,True,True,True,True,False,False,True,False,False,False,False,False,False,True,True,False,True,False,False,True,True,False,False,False,False,True,False,True,True,True,False,True,True,True,False,True,True,True,True,False,True,True,False,False,False,False,False,False,False,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,True,True,False,False,False,False,False,True,True,False,False,True,False,False,True,False,True,False,True,False,False,False,False,False,False,False,True,False,True,False,True,False,True,True,True,False,False,True,True,True,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,False,True,True,False,True,True,True,True,False,True,False,False,True,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,True,False,False,True,False,False,True,False,False,True,True,True,False,False,False,True,False,False,True,True,True,False,False,False,True,True,True,True,False,True,True,False,False,True,True,False,False,False,False,False,True,True,False,True,False,False,True,False,False,False,False,True,False,False,True,True,True,True,True,False,False,False,False,False,True,True,True,True,True,True,False,True,True,False,False,True,False,True,True,False,False,True,True,False,True,True,False,True,False,True,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,False,False,False,True,True,True,False,True,True,False,True,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,False,True,True,True,False,False,True,False,True,False,True,True,True,False,True,True,False,False,False,True,False,False,True,False,True,False,False,True,True,True,False,True,False,True,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,False,True,True,False,True,True,True,True,False,False,False,True,False,True,False,False,True,False,True,False,True,False,True,False,True,True,False,False,True,False,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,True,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False,True,False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,True,False,False,False,True,False,True,False,False,True,False,True,False,False,True,True,False,False,True,False,False,False,False,False,False,True,False,True,False,False,False,True,False,False,True,False,False,True,False,True,False,False,False,False,False,False,False,False,False,True,False,False,True,False,True,True,False,True,True,False,True,True,False,False,True,True,False,True,False,False,False,False,False,True,True,True,True,True,True,True,False,False,False,True,False,True,False,False,False,True,True,False,False,True,False,True,False,False,True,True,False,True,True,False,False,False,True,True,True,True,True,True,True,True,False,True,False,True,False,False,False,True,False,True,False,False,False,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,False,False,True,True,False,True,False,False,True,False,True,False,True,True,False,False,True,True,True,True,True,False,False,False,False,True,True,True,False,False,True,True,True,False,False,True,True,False,True,False,False,False,False,False,True,True,False,False,False,True,True,True,False,True,False,False,True,True,True,True,True,False,False,False,False,False,True,True,False,False,True,True,False,False,True,True,True,True,False,True,False,True,False,False,True,False,False,False,True,True,True,True,True,False,True,True,False,True,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,False,True,False,True,True,False,False,True,True,True,False,True,True,False,False,False,False,True,True,False,True,True,False,False,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,False,False,False,True,True,True,True,False,True,False,False,False,True,False,False,True,True,False,True,False,True,False,True,True,True,True,False,False,False,False,False,False,True,False,True,False,False,True,True,True,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,False,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,False,False,True,True,False,True,False,True,False,True,True,True,True,False,True,True,False,True,False,True,False,True,False,True,False,False,True,False,False,False,False,False,True,False,True,True,True,False,True,True,True,False,True,False,False,False,False,False,False,False,True,False,True,True,True,True,False,True,True,False,True,False,False,False,False,False,False,True,False,True,False,True,True,True,True,True,False,True,True,False,True,True,False,False,False,True,False,False,False,True,False,False,True,True,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,True,False,False,False,False,True,False,False,True,True,False,False,True,False,False,False,True,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,False,True,False,True,False,False,True,True,True,True,False,True,False,False,True,True,True,True,False,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,True,False,True,False,True,True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,True,True,False,True,False,False,True,False,True,False,True,False,False,False,False,False,True,False,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,True,True,False,True,False,True,False,False,False,True,True,False,True,True,True,True,False,False,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,False,True,True,True,False,True,False,True,True,True,False,False,True,False,False,True,True,True,True,True,False,True,False,False,True,False,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,True,True,True,True,False,False,False,True,True,True,True,False,True,True,True,True,True,False,False,False,False,False,False,False,False,True,False,True,False,False,True,False,True,False,True,True,False,False,False,True,True,True,True,True,False,True,False,True,True,True,True,True,True,False,True,True,True,False,False,True,False,True,True,True,True,True,True,True,True,True,False,False,True,False,True,True,True,False,True,False,True,False,True,False,False,True,True,True,True,False,True,True,True,False,False,True,True,True,False,False,True,True,True,False,True,False,True,False,False,False,False,True,True,True,True,True,False,True,True,True,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,False,False,True,False,False,True,False,False,False,True,True,False,False,False,True,True,True,True,False,False,True,True,True,True,True,True,False,True,False,True,False,False,True,True,False,False,True,False,False,True,False,True,True,False,False,False,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,True,True,True,True,False,True,False,False,True,True,False,True,True,False,True,True,False,False,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,False,False,True,False,True,True,True,False,False,True,True,True,True,False,False,True,False,False,True,True,True,True,False,False,False,True,True,False,True,True,False,True,True,True,True,True,False,False,True,False,False,True,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,False,True,True,False,False,True,True,True,True,False,True,True,True,True,True,False,False,True,True,True,True,True,True,True,False,True,False,True,False,True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,True,False,False,False,False,True,True,False,True,True,False,True,True,True,False,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,True,True,True,True,True,True,False,False,True,False,False,False,True,True,True,True,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,False,True,True,True,True,False,True,True,False,True,True,False,False,False,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,False,True,False,True,False,False,False,False,False,True,False,True,True,False,True,False,True,False,True,False,False,False,True,False,False,False,True,True,True,True,False,False,False,False,True,False,True,True,False,True,True,False,False,False,False,True,False,True,True,True,True,True,True,False,True,True,True,False,False,False,True,True,False,True,True,False,True,False,True,True,True,False,True,True,True,True,False,True,True,True,True,False,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,True,True,False,True,True,True,False,False,False,False,True,True,True,False,False,True,True,True,False,False,True,False,True,True,True,True,True,False,True,False,True,True,True,True,False,False,False,False,True,False,False,False,False,True,False,False,True,False,True,True,False,False,False,True,False,True,False,True,True,False,True,False,True,False,True,True,True,False,True,False,False,False,False,False,True,False,True,False,False,False,False,False,True,False,True,True,True,False,False,False,False,True,False,True,True,True,False,False,True,True,False,False,True,False,False,True,True,True,True], dtype = "bool")#candidate|5588|(2912,)|const|bool
var_5589 = relay.var("var_5589", dtype = "uint32", shape = (1800,))#candidate|5589|(1800,)|var|uint32
call_5585 = relay.TupleGetItem(func_4229_call(relay.reshape(var_5586.astype('uint8'), [8, 5, 7]), relay.reshape(const_5587.astype('float64'), [1, 56]), relay.reshape(const_5588.astype('bool'), [2912,]), relay.reshape(var_5589.astype('uint32'), [1800,]), ), 3)
call_5590 = relay.TupleGetItem(func_4235_call(relay.reshape(var_5586.astype('uint8'), [8, 5, 7]), relay.reshape(const_5587.astype('float64'), [1, 56]), relay.reshape(const_5588.astype('bool'), [2912,]), relay.reshape(var_5589.astype('uint32'), [1800,]), ), 3)
func_4229_call = mod.get_global_var('func_4229')
func_4235_call = mutated_mod.get_global_var('func_4235')
call_5614 = relay.TupleGetItem(func_4229_call(relay.reshape(var_5586.astype('uint8'), [8, 5, 7]), relay.reshape(const_5587.astype('float64'), [1, 56]), relay.reshape(const_5588.astype('bool'), [2912,]), relay.reshape(var_5589.astype('uint32'), [1800,]), ), 5)
call_5615 = relay.TupleGetItem(func_4235_call(relay.reshape(var_5586.astype('uint8'), [8, 5, 7]), relay.reshape(const_5587.astype('float64'), [1, 56]), relay.reshape(const_5588.astype('bool'), [2912,]), relay.reshape(var_5589.astype('uint32'), [1800,]), ), 5)
output = relay.Tuple([call_5583,call_5585,var_5586,const_5587,const_5588,var_5589,call_5614,])
output2 = relay.Tuple([call_5584,call_5590,var_5586,const_5587,const_5588,var_5589,call_5615,])
func_5618 = relay.Function([var_5586,var_5589,], output)
mod['func_5618'] = func_5618
mod = relay.transform.InferType()(mod)
var_5619 = relay.var("var_5619", dtype = "uint8", shape = (280,))#candidate|5619|(280,)|var|uint8
var_5620 = relay.var("var_5620", dtype = "uint32", shape = (1800,))#candidate|5620|(1800,)|var|uint32
output = func_5618(var_5619,var_5620,)
func_5621 = relay.Function([var_5619,var_5620,], output)
mutated_mod['func_5621'] = func_5621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2849_call = mod.get_global_var('func_2849')
func_2850_call = mutated_mod.get_global_var('func_2850')
call_5636 = relay.TupleGetItem(func_2849_call(), 0)
call_5637 = relay.TupleGetItem(func_2850_call(), 0)
output = relay.Tuple([call_5636,])
output2 = relay.Tuple([call_5637,])
func_5645 = relay.Function([], output)
mod['func_5645'] = func_5645
mod = relay.transform.InferType()(mod)
output = func_5645()
func_5646 = relay.Function([], output)
mutated_mod['func_5646'] = func_5646
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5697 = relay.var("var_5697", dtype = "bool", shape = ())#candidate|5697|()|var|bool
var_5698 = relay.var("var_5698", dtype = "bool", shape = (6, 3, 9))#candidate|5698|(6, 3, 9)|var|bool
bop_5699 = relay.logical_or(var_5697.astype('bool'), var_5698.astype('bool')) # shape=(6, 3, 9)
func_1124_call = mod.get_global_var('func_1124')
func_1130_call = mutated_mod.get_global_var('func_1130')
const_5703 = relay.const([2.677351,-6.192101,4.696980,-9.340481,4.863383,5.795556,2.923221,-3.793381,-4.001094,0.154742,9.327392,0.988518,0.825116,1.670014,4.136307,2.667390,7.732759,3.497977,2.774766,9.698570,4.531940,-7.188913,-1.890913,9.169924,3.688804,9.816221,1.414936,4.523634,-6.830908,8.101547,8.687744,2.450631,-6.119461,2.640747,-6.134543,-8.357486,1.442070,-5.535958,5.977776,-8.992761,-3.403514,2.578654,3.869016,-7.554708,1.942679,0.598357,-1.296937,4.861982,6.607453,-9.412993,7.988525,3.630076,-8.494175,-3.113689,3.022473,-2.815224,-6.689686,8.552086,-9.904259,-8.144260,8.713415,-6.640647,-7.805740,-0.169748,8.427833,9.545610,3.754600,2.859866,-5.308542,1.252868,9.967410,-9.998319,3.813332,5.700135,3.238418,0.271163,2.558556,2.376889,8.964201,4.743086,-9.391795,-8.296957,-4.698005,2.483942,3.638718,-4.132212,8.448706,1.390585,0.922970,-8.760885,-1.837814,7.350341,-2.838808,1.364906,8.618282,-5.133042,5.044515,8.724234,-3.425812,-4.096093,-9.919650,-7.907128,5.400612,-5.318589,-3.784685,-6.491765,0.427444,-5.156183,-7.465595,9.893965,8.989664,8.450370,-9.878102,-9.837973,-8.030218,7.398335,1.161258,-9.120311,5.141151,0.626311,1.118554,-7.329666,-5.581437,-6.921061,-8.808792,-4.299735,5.666868,-0.698146,-5.632626,5.782188,3.595681,6.584499,-9.551675,-9.060473,7.974907,-7.092305,0.279287,3.880292,1.814250,-0.711205,0.962422,9.471968,-3.146008,0.663523,-5.971982,4.321939,2.869767,8.789283,-1.373260,2.358874,7.736927,5.908809,-5.160705,-8.645378,-2.503852,5.770731,0.132799,2.189677,-0.281869,9.358041,8.178831,-7.883512,6.683071,-3.841622,5.716572], dtype = "float64")#candidate|5703|(165,)|const|float64
const_5704 = relay.const([3,-10,-2,-6,-10,-8,-8,-8,-5,5,10,-2,7,9,4,-9,-10,4,8,6,10,10,8,-6,4,-2,7,-5,7,-2,-8,10,8,3,-5,-3,-2,1,-8,-2,10,7,7,10,8,7,-2,7,10,-5,6,9,8,-5,-9,-1,2,-4,1,-6,-7,6,-9,-9,-10,5,-2,-3,4,-1,6,2,9,10,-2,-1,-9,-8,10,7,-4,6,-7,-8,-9,-6,10,-5,-5,-1,1,-6,8,7,1,-8,8,-3,-4,-8,2,8,-3,3,9,-5,-5,-1,4,3,-3,2,-6,8,8,3,-1,1,7,2,-7,6,-7,-7,6,8,-10,3,-5,-7,9,2,4,-4,5,-7,-4,-6,-10,1,2,5,10,-7,-1,10,6,-1,-3,-9,2,3,-9,-6,10,4,9,-4,-1,5,-7,3,-7,4,-9,10,-9,7,10,8,3,3,-3,-2,-10,-6,6,-2,2,-4,-9,2,7,-7,-5,10,6,1,-10,4,1,-9,-1,-9,5,4,10,-3,7,6,6,1,7,3,-6,9,9,6,7,3,-1,-7,4,7,-3,-5,-7,2,10,-3,-4,-8,8,-3,1,8,-2,2,8,-9,-10,-1,3,-3,1,-3,-8,-8,-5,3,4,8,10,-5,-9,1,-1,8,-8,-10,7,-3,-4,-1,-1,-5,-6,4,10,4,4,-1,-10,2,10,-8,-5,3,-4,-8,-9,-2,3,2,-5,-7,4,5,-4,3,-9,4,1,-3,10,-2,4,5,-1,-3,5,-7,-7,-4,-1,7,-7,-4,-8,5,-8,-8,-2,10,-2,-2,-2,-8,3,-1,9,6,1,-4,5,-7,-6,-5,-10,2,7,-10,2,9,-2,-2,8,-8,-6,-8,-2,5,-9,-6,5,-10,-9,1,-10,7,-1,-4,-6,2,5,-6,4,-4,-4,-2,8,1,-4,-9,5,8,-6,8,5,6,9,-6,7,-6,2,-10,-9,6,-7,10,2,9,2,-9,-9,-6,1,9,-4,9,-2,4,1,-7,-6,10,6,-5,-9,5,1,4,3,-10,-10,-1,-7,4,-7,-8,-1,-1,10,-7,-10,8,-4,-3,-8,4,-1,10,1,10,8,-3,8,8,-9,8,-7,-1,9,-2,9,6,-2,-10,10,-5,9,9,-1,7,2,-9,2,-2,6,-9,-9,-4,9,7,5,-2,-9,4,-6,10,-6,6,9,-10,-3,9,-4,-4,9,4,3,-10,5,-2,5,-8,1,1,-6,-6,-10,3,-7,6,-10,2,8,-6,8,-5], dtype = "int8")#candidate|5704|(480,)|const|int8
var_5705 = relay.var("var_5705", dtype = "int32", shape = (84,))#candidate|5705|(84,)|var|int32
const_5706 = relay.const([[-7,6],[7,-10],[-7,8],[1,-4],[-8,-10],[5,-9],[-8,3],[-1,1],[-7,9],[-1,6],[3,-3],[1,-5],[-6,10],[-9,-4],[-2,-10],[3,2],[8,-5],[-8,7],[6,6],[-7,4],[8,-5],[-5,-5],[-7,1],[-6,-9],[2,-3],[4,4],[2,-5],[2,4],[-5,6],[-7,8],[-4,3],[10,4],[5,-6],[9,-9],[1,2],[5,-1],[5,2],[-6,8],[-7,-2],[3,3],[-3,-7],[9,3],[-9,-1],[-1,5],[-10,9],[-7,-8],[6,-3],[5,-6],[-5,3],[8,3],[-3,10],[-7,-9],[3,-2],[5,-7],[9,-1],[-8,-7],[10,6],[-7,5],[-3,3],[3,-6],[-2,-7],[8,9],[3,-4],[-4,5],[-10,-4],[-10,-7],[8,-5],[-6,5],[9,6],[-5,-7],[-2,1],[-1,-4],[7,-5],[10,10],[-4,7],[5,-9],[-4,-2],[-9,-9],[-9,10],[7,8],[-5,9],[-9,-1],[5,4],[-10,4],[9,2],[6,-2],[2,-4],[8,-10],[-7,8],[1,10],[7,-4],[6,-8],[-6,4],[4,7],[-9,-4],[3,2],[5,7],[-9,-2],[10,1],[5,-10],[4,5],[1,3],[-4,-7],[-2,-8],[-8,5],[-1,-4],[-2,-6],[6,2],[-3,7],[8,2],[-6,-1],[-9,-7],[4,-4],[8,8],[3,-1],[-2,-1],[9,-9],[-8,10],[-1,4],[10,6],[-5,10],[10,-5],[2,4],[-8,-8],[-10,5],[7,2],[4,9],[7,-7],[10,6],[-5,-3],[-9,-2],[-1,-6],[-9,-9],[-4,-8],[6,4],[5,-6],[9,2],[-4,-5],[-1,2],[1,-3],[8,-9],[-4,3],[-4,-5],[-8,-1],[4,-5],[10,5],[-8,3],[4,-10],[-9,-7],[5,3],[6,-6],[9,-5],[3,-3],[-9,4],[5,7],[-5,-4],[-5,7],[2,9],[8,-4],[5,9],[-9,-10],[-3,8],[-4,-9],[-3,3],[-5,-7],[-8,5],[-4,-2],[10,8],[8,-8],[2,10],[10,-5],[2,10],[-6,-4],[-7,-2],[-10,9],[-10,9],[-5,-10],[4,5],[7,8],[7,9],[-9,10],[2,7],[8,1],[-3,7],[-9,6],[-5,9],[10,5],[7,1],[-7,-2],[-4,-2],[-2,-2],[7,-4],[-6,-2],[-1,5],[10,9],[4,-3],[-2,9],[-1,10],[-7,-2],[-4,1],[-7,3],[3,9],[7,-1],[1,-1],[9,1],[-2,7],[7,-2],[-4,-3],[5,8],[5,9],[9,-5],[6,-3],[8,6],[7,1],[-1,-5],[5,7],[-5,8],[-6,5],[9,-8],[-6,9],[-7,5],[-8,-7],[9,-5],[3,6],[9,-9],[-3,2],[4,6],[-1,5],[-1,3],[7,8],[4,-2],[-7,7],[4,-1],[-10,-8],[3,6],[10,3],[2,-1],[-7,-6],[-2,8],[-9,-5],[2,-8],[1,7],[-2,1],[4,1],[9,6],[-1,-7],[-1,4],[1,-10],[7,5],[6,3],[7,-7],[-7,9],[-2,-4],[-7,8],[7,5],[1,-2],[3,-6],[3,6],[5,-3],[2,10],[8,9],[-4,-1],[-8,2],[-4,-8],[4,-8],[3,-9],[5,-1],[-7,-5],[5,-10],[10,2],[10,7],[-8,10],[7,1],[2,-10],[-3,6],[-2,-4],[-4,7],[-6,9],[-3,-9],[-1,5],[7,-10],[7,5],[-3,-1],[-1,-3],[9,-8],[9,10],[-6,-2],[-10,-5],[-4,-7],[6,-2],[-5,5],[8,-3],[-6,-2],[10,6],[3,-1],[7,-1],[2,4],[1,7],[1,-4],[-10,5],[-7,2],[3,3],[5,10],[-1,-5],[-10,-3],[6,-7],[-1,-3],[-5,8],[9,1],[-7,-9],[-8,6],[-1,-2],[-9,4],[-4,2],[9,8],[-6,-9],[-6,9],[3,-8],[9,10],[-5,5],[-7,1],[7,1],[-9,-3],[7,3],[2,-9],[-2,-6],[10,-2],[-10,1],[5,3],[7,9],[2,2],[4,5],[7,-1],[-8,9],[4,-5],[8,4]], dtype = "int32")#candidate|5706|(336, 2)|const|int32
call_5702 = relay.TupleGetItem(func_1124_call(relay.reshape(const_5703.astype('float64'), [11, 5, 3]), relay.reshape(const_5704.astype('int8'), [480,]), relay.reshape(var_5705.astype('int32'), [84, 1]), relay.reshape(const_5706.astype('int32'), [672,]), ), 7)
call_5707 = relay.TupleGetItem(func_1130_call(relay.reshape(const_5703.astype('float64'), [11, 5, 3]), relay.reshape(const_5704.astype('int8'), [480,]), relay.reshape(var_5705.astype('int32'), [84, 1]), relay.reshape(const_5706.astype('int32'), [672,]), ), 7)
uop_5717 = relay.rsqrt(const_5706.astype('float32')) # shape=(336, 2)
func_981_call = mod.get_global_var('func_981')
func_985_call = mutated_mod.get_global_var('func_985')
var_5720 = relay.var("var_5720", dtype = "bool", shape = (2912,))#candidate|5720|(2912,)|var|bool
call_5719 = relay.TupleGetItem(func_981_call(relay.reshape(const_5704.astype('int8'), [2, 15, 16]), relay.reshape(const_5704.astype('int8'), [2, 15, 16]), relay.reshape(var_5720.astype('bool'), [2912,]), ), 1)
call_5721 = relay.TupleGetItem(func_985_call(relay.reshape(const_5704.astype('int8'), [2, 15, 16]), relay.reshape(const_5704.astype('int8'), [2, 15, 16]), relay.reshape(var_5720.astype('bool'), [2912,]), ), 1)
output = relay.Tuple([bop_5699,call_5702,const_5703,const_5704,var_5705,uop_5717,call_5719,var_5720,])
output2 = relay.Tuple([bop_5699,call_5707,const_5703,const_5704,var_5705,uop_5717,call_5721,var_5720,])
func_5729 = relay.Function([var_5697,var_5698,var_5705,var_5720,], output)
mod['func_5729'] = func_5729
mod = relay.transform.InferType()(mod)
mutated_mod['func_5729'] = func_5729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5729_call = mutated_mod.get_global_var('func_5729')
var_5731 = relay.var("var_5731", dtype = "bool", shape = ())#candidate|5731|()|var|bool
var_5732 = relay.var("var_5732", dtype = "bool", shape = (6, 3, 9))#candidate|5732|(6, 3, 9)|var|bool
var_5733 = relay.var("var_5733", dtype = "int32", shape = (84,))#candidate|5733|(84,)|var|int32
var_5734 = relay.var("var_5734", dtype = "bool", shape = (2912,))#candidate|5734|(2912,)|var|bool
call_5730 = func_5729_call(var_5731,var_5732,var_5733,var_5734,)
output = call_5730
func_5735 = relay.Function([var_5731,var_5732,var_5733,var_5734,], output)
mutated_mod['func_5735'] = func_5735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5138_call = mod.get_global_var('func_5138')
func_5139_call = mutated_mod.get_global_var('func_5139')
call_5754 = func_5138_call()
call_5755 = func_5138_call()
output = call_5754
output2 = call_5755
func_5756 = relay.Function([], output)
mod['func_5756'] = func_5756
mod = relay.transform.InferType()(mod)
output = func_5756()
func_5757 = relay.Function([], output)
mutated_mod['func_5757'] = func_5757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2512_call = mod.get_global_var('func_2512')
func_2514_call = mutated_mod.get_global_var('func_2514')
call_5775 = func_2512_call()
call_5776 = func_2512_call()
uop_5777 = relay.log(call_5775.astype('float32')) # shape=(4, 15, 15)
uop_5779 = relay.log(call_5776.astype('float32')) # shape=(4, 15, 15)
func_2927_call = mod.get_global_var('func_2927')
func_2928_call = mutated_mod.get_global_var('func_2928')
call_5785 = relay.TupleGetItem(func_2927_call(), 2)
call_5786 = relay.TupleGetItem(func_2928_call(), 2)
func_3429_call = mod.get_global_var('func_3429')
func_3431_call = mutated_mod.get_global_var('func_3431')
call_5800 = relay.TupleGetItem(func_3429_call(), 1)
call_5801 = relay.TupleGetItem(func_3431_call(), 1)
output = relay.Tuple([uop_5777,call_5785,call_5800,])
output2 = relay.Tuple([uop_5779,call_5786,call_5801,])
func_5802 = relay.Function([], output)
mod['func_5802'] = func_5802
mod = relay.transform.InferType()(mod)
output = func_5802()
func_5803 = relay.Function([], output)
mutated_mod['func_5803'] = func_5803
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5833 = relay.var("var_5833", dtype = "uint32", shape = (13, 16, 11))#candidate|5833|(13, 16, 11)|var|uint32
const_5834 = relay.const([[[3,3,1,10,-4,7,7,5,1,-3,8],[6,7,-2,3,1,2,-6,4,2,-10,-8],[-3,10,-4,10,4,9,-2,-4,-7,-3,-9],[-3,8,2,4,-4,4,10,7,-7,-6,2],[-1,4,-3,8,7,-6,-7,-10,10,-8,10],[-2,10,9,10,-5,-8,-9,-8,-3,-8,-8],[9,4,6,4,1,-4,-7,-6,-4,6,-2],[1,1,6,4,4,6,3,-1,-7,-4,3],[1,8,10,7,10,5,3,3,-5,-9,7],[2,-10,10,7,-7,3,-6,-3,9,3,7],[5,-3,8,-3,5,-5,-2,1,8,-10,5],[-6,-8,-2,-8,7,10,6,-2,-3,2,-4],[-2,-6,10,3,-1,-4,5,2,-6,9,-10],[3,3,1,-3,2,7,-8,-3,4,2,-4],[5,-2,-6,-8,5,-8,-7,-4,3,8,3],[9,-6,9,-3,7,-1,-1,-10,-3,8,3]],[[-2,8,4,-5,1,-2,-9,5,4,-9,10],[1,-7,-5,8,2,9,-7,-5,10,8,-3],[3,-8,1,-1,7,1,8,9,-5,8,-1],[7,-9,2,-10,-4,-4,-1,10,-5,6,1],[3,-10,10,-2,-4,9,-7,3,-5,-2,1],[-3,7,-8,-6,-9,-8,7,8,3,10,9],[2,-3,-1,7,10,5,-9,-2,-3,-6,-9],[-10,-4,-3,4,2,-4,-4,-1,6,-2,9],[-3,8,2,-8,-9,-2,-1,7,-6,3,3],[-2,-10,-6,-1,-4,7,-2,-8,-4,9,9],[-10,7,-5,-6,10,5,-8,4,9,6,2],[9,-8,-4,-8,9,9,-5,-8,7,9,-2],[6,-8,6,2,-4,5,-1,-1,3,-8,7],[9,2,-7,-9,-10,5,-9,-2,6,-10,-7],[3,2,7,-10,-3,10,-6,-8,6,-9,6],[1,-9,-1,1,1,-6,-9,5,7,-8,-7]],[[6,9,-3,-2,-6,-4,-1,3,-5,-5,9],[3,-1,4,-9,-4,-6,6,9,8,-4,-2],[9,6,-2,-4,5,7,-10,-7,-9,4,4],[-5,-2,2,-5,-1,-10,8,-2,-6,-10,6],[1,-10,6,8,-6,7,-7,-5,3,-7,-7],[-6,-7,-5,-5,-8,-4,-1,-4,2,-3,9],[-6,-2,-2,-2,6,-5,2,2,1,-4,-8],[-5,3,2,6,5,8,1,-8,9,2,-7],[-6,-2,8,-3,-10,-9,-6,10,-4,6,-4],[-4,-9,-6,-8,7,-1,10,4,6,-2,8],[7,3,-3,-5,-3,1,1,7,2,3,3],[-5,-9,-1,-7,10,-7,5,-10,-6,9,-9],[7,-2,-7,4,-10,-9,9,9,-10,-8,-2],[6,-5,-8,-2,-7,-10,7,5,1,8,2],[9,3,-10,6,-6,-5,7,-5,10,-7,2],[10,-5,3,-9,1,6,-7,5,-10,6,-1]],[[-1,-1,10,-1,-1,-2,-2,-8,-9,10,4],[-4,1,-9,-3,9,9,-5,5,5,-9,-10],[9,-5,-8,-6,4,-1,-5,-1,3,4,-7],[4,7,8,4,6,-8,4,7,8,9,4],[2,-4,-5,-8,7,6,1,9,-4,9,-7],[-9,2,-4,9,-4,-5,-5,-7,5,-6,10],[-5,-1,4,-10,-4,5,-6,-8,1,5,2],[-8,-4,-7,-2,-6,-3,-3,-10,10,-1,1],[-8,-2,2,-4,-7,5,3,-2,6,1,6],[10,8,9,7,-7,-8,3,-4,6,7,-5],[-3,7,-2,1,-6,-3,1,4,-1,-4,-9],[2,-3,-9,8,-3,8,10,-10,-9,4,-1],[-3,4,7,6,4,-3,6,7,3,-5,-2],[2,-8,6,-2,-6,1,2,9,-6,-8,9],[-9,8,-8,3,-7,-2,6,6,7,5,-5],[6,7,-6,8,-8,6,9,8,6,8,2]],[[-5,2,-4,10,3,1,7,-4,-5,-4,-8],[-6,6,2,7,-8,4,-6,6,-6,-1,1],[-6,-5,-9,3,3,-4,1,-4,3,3,-1],[-6,5,6,-10,-6,-5,-1,-1,4,4,-6],[7,5,2,-7,-7,8,6,-7,-2,-5,5],[1,-10,1,-4,-9,7,-9,2,-9,-9,-2],[-2,1,4,-1,4,5,9,-8,-3,4,-2],[8,-8,-6,4,2,-7,-10,-3,-9,6,-10],[2,-10,6,-6,6,4,-10,3,-8,-10,9],[7,-4,8,-2,7,-6,-10,10,1,-9,1],[7,3,-8,2,4,1,6,8,-6,4,1],[-4,-10,-10,-4,-8,7,-8,-4,-4,10,8],[5,-5,-2,-4,-1,-7,-5,-9,10,-4,7],[-3,2,3,5,9,-9,10,1,4,4,4],[8,2,9,4,6,10,5,2,-5,9,-5],[-5,4,-10,-1,-10,8,-9,-8,4,10,-3]],[[-7,6,-6,-6,-5,7,10,-10,4,2,-3],[-10,5,4,9,-2,-2,8,3,-7,5,-10],[3,-8,1,8,2,-5,-1,-2,-6,-7,-3],[6,-9,6,9,2,7,7,-9,-4,-3,8],[7,4,-4,-4,4,-3,-3,10,7,3,2],[-2,5,2,4,-9,9,6,2,10,-2,-2],[2,-8,-4,2,9,8,9,-1,1,-6,3],[4,4,5,7,-2,1,-7,-8,-2,-3,2],[-10,7,-3,2,6,5,-1,7,-10,-6,-6],[-10,4,-3,2,-10,-10,-6,9,1,5,7],[-10,4,3,3,-5,-6,-4,-5,-6,-3,-2],[-9,8,-8,10,10,10,-10,-6,-2,5,-9],[7,-7,8,9,-8,3,-2,8,-6,2,4],[7,-4,-10,-7,9,-4,-10,8,-4,-10,4],[-6,4,1,-8,-7,-5,-5,9,6,9,6],[-2,-9,-3,-1,-2,9,1,-3,5,5,8]],[[-6,4,-7,-10,10,-7,10,9,7,10,-9],[-6,-9,10,-2,4,9,8,10,-9,1,1],[-8,-3,-4,-10,4,-3,8,9,-6,-8,8],[1,5,8,7,-9,2,1,7,-8,9,5],[7,-9,-6,7,2,-2,7,-7,3,-9,-8],[-10,-4,-7,10,-2,8,9,8,-10,4,-9],[3,-5,-2,1,7,-6,-8,3,6,4,-5],[-10,8,3,-1,3,10,10,2,-1,-5,-9],[-9,10,6,-9,-6,5,-8,-8,-3,-3,-8],[-5,6,-9,-3,3,-9,-7,-6,7,5,10],[2,-2,-8,10,-8,6,10,-5,2,-5,1],[-7,8,1,-7,7,-10,8,4,3,2,-3],[5,-5,6,-1,2,3,3,3,6,3,1],[-3,-7,4,-8,-4,-9,-1,1,-9,9,10],[6,5,-5,8,-8,-10,7,-6,5,7,1],[8,-9,4,8,1,-9,-8,5,-2,-6,9]],[[10,-8,7,8,3,-9,-2,-2,7,8,2],[-2,-3,9,7,-3,-5,-2,6,2,8,4],[4,-2,-1,-7,-6,1,3,9,10,-7,-2],[-9,10,10,3,-8,9,-8,-10,-5,-5,-6],[-6,8,-4,3,5,6,3,3,-9,-3,-1],[-1,7,7,-2,-10,-5,-6,-7,-9,-1,10],[-1,10,-6,-8,-5,9,-5,-3,9,-7,4],[-7,4,-3,-1,9,-8,1,3,2,-8,-9],[7,-4,-3,-3,6,-8,-6,-5,6,8,-4],[-9,-8,-6,-1,-1,-5,7,8,7,-7,-4],[5,-9,-5,6,-6,10,-5,-10,9,7,8],[4,-1,2,5,3,9,-3,-9,-6,4,-8],[-2,7,4,5,-5,10,9,8,-1,-4,-2],[-5,-5,-7,6,-10,-8,8,-1,3,-4,-4],[8,7,-2,8,-7,9,3,-3,-3,-7,-1],[2,2,8,10,-8,-5,-8,3,2,-10,-4]],[[-7,3,-1,1,-7,-4,10,-2,-7,1,-3],[-10,6,8,5,10,-10,-3,3,-7,-7,-7],[6,-7,10,-6,6,3,1,9,-5,7,-10],[-8,-4,-1,-7,-10,-8,3,-7,-4,6,7],[7,3,-5,-7,3,-7,-2,10,9,-10,8],[-6,4,-10,-5,10,-2,-6,-5,1,-10,-5],[-9,2,6,6,9,9,-1,-6,5,-2,10],[6,-3,-3,7,7,-6,5,-5,6,-2,7],[-3,2,10,-4,4,-8,-9,1,-3,-4,-1],[1,-10,10,-1,7,-2,1,-5,-4,7,5],[5,5,-6,6,-10,5,-3,3,-2,9,9],[7,7,2,-5,1,5,-9,7,-2,4,6],[-10,3,-9,-5,-10,-2,-4,-2,-3,9,1],[3,-5,4,10,-5,10,4,10,-8,2,9],[6,6,-6,-1,5,6,7,-7,1,9,2],[1,-3,-2,10,-2,5,-10,-5,2,5,7]],[[-8,-8,8,10,-1,2,9,10,7,10,1],[5,-10,-5,-4,6,-9,-3,-4,-7,-4,-10],[2,4,3,3,5,2,-4,-10,-1,2,-3],[-9,8,1,-6,6,-10,-9,-6,6,10,-7],[-5,3,-3,8,-2,2,-4,3,-3,-9,-9],[3,1,-7,7,5,10,10,5,-1,6,8],[-8,1,1,-4,10,-8,-9,10,-10,8,5],[7,-7,-8,4,4,-8,-3,6,-3,-5,7],[-7,-1,-4,-9,8,-8,4,7,-1,-10,-7],[9,-10,-2,-5,-10,10,3,10,-2,8,1],[-5,2,9,-6,-4,-2,9,-9,4,9,9],[-7,-6,7,-10,-7,-7,10,4,-4,1,3],[1,6,-3,1,-9,-3,9,8,-6,-4,-8],[9,-10,-10,-1,3,-9,9,-6,-6,-1,1],[-6,-9,5,-7,8,7,-1,9,2,-3,-10],[4,7,2,-6,-7,-1,-7,2,1,10,-7]],[[7,-2,-7,1,-1,5,5,-5,-10,5,3],[-10,-6,4,-1,8,9,6,-8,3,-3,9],[-6,9,9,7,-8,4,8,-3,-10,-4,2],[5,8,-1,-8,7,5,10,-3,-3,-4,6],[-8,8,9,-7,1,-3,3,9,4,-5,-3],[-10,-4,9,1,-7,-4,7,6,-6,-9,7],[3,-1,-2,-6,3,-3,-1,2,-8,3,5],[-7,5,9,2,-5,-4,2,5,2,5,5],[-10,10,-8,-9,-2,-6,-2,4,-3,-1,-7],[2,2,-2,-1,-3,-5,-8,5,-8,6,7],[-8,-1,9,-7,-4,10,5,3,8,7,-10],[-10,10,3,3,3,-2,-4,8,-7,10,-8],[-9,1,8,3,-10,-4,-5,10,8,9,10],[1,5,-10,-5,-2,-1,2,-10,9,1,4],[-2,-2,-8,10,-6,-5,1,6,4,-8,10],[6,6,3,9,-3,-2,3,8,5,4,-5]],[[-5,-1,-8,4,1,-1,7,6,1,-9,4],[10,-5,8,-7,6,-3,-1,-6,-10,-6,5],[4,1,1,-8,-2,-9,-7,8,-7,8,-9],[-10,5,-5,-2,8,2,-3,9,-9,10,-10],[4,-3,-10,2,9,8,5,-6,-2,3,4],[-8,-7,-6,7,-6,-3,6,7,5,-4,-1],[-4,6,-1,-1,-6,10,10,-2,3,1,-6],[-7,7,-8,-5,-9,-6,-7,5,6,1,-5],[-3,9,5,-9,-9,4,10,-8,-3,-4,-4],[-7,-10,-10,-8,-1,2,-4,2,-9,-2,6],[7,9,-2,8,-5,-5,-8,6,-10,7,-9],[-10,-6,9,-2,-2,-10,8,3,8,-10,2],[5,-6,-7,8,5,6,-9,-1,-3,-1,-3],[4,4,5,2,6,7,4,-4,-1,-2,-8],[3,3,4,8,-2,5,-6,-4,8,-8,9],[-1,8,-9,9,3,-1,-10,10,-10,2,-10]],[[6,7,-3,8,-8,-4,1,7,5,3,-6],[-8,-9,-9,-6,9,5,5,-10,-10,4,-5],[1,4,-3,1,8,-8,-2,9,-7,1,2],[-10,10,1,5,-8,1,4,9,-5,-7,-7],[9,-8,-4,-8,6,1,7,-10,9,1,-10],[-3,-10,-9,1,-7,-1,7,-7,-4,-5,9],[-6,-6,-6,4,-2,8,-5,-1,10,7,7],[7,-10,-5,5,-7,-2,7,-2,6,9,-7],[1,-1,6,-2,-3,-6,-9,8,-4,6,-9],[-6,3,-4,7,9,7,-9,-9,7,2,-4],[4,-5,-6,6,4,-6,-7,-1,2,-2,-1],[4,-4,3,4,-6,-1,7,-2,5,-9,4],[1,-10,-5,-4,5,-8,8,-6,-1,3,3],[-3,6,-2,-1,9,-10,-7,-3,-3,8,1],[5,10,-8,-1,-4,-8,2,-5,6,7,3],[5,2,6,1,7,5,-3,-4,-5,-9,-9]]], dtype = "uint32")#candidate|5834|(13, 16, 11)|const|uint32
bop_5835 = relay.not_equal(var_5833.astype('bool'), relay.reshape(const_5834.astype('bool'), relay.shape_of(var_5833))) # shape=(13, 16, 11)
output = relay.Tuple([bop_5835,])
output2 = relay.Tuple([bop_5835,])
func_5848 = relay.Function([var_5833,], output)
mod['func_5848'] = func_5848
mod = relay.transform.InferType()(mod)
mutated_mod['func_5848'] = func_5848
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5849 = relay.var("var_5849", dtype = "uint32", shape = (13, 16, 11))#candidate|5849|(13, 16, 11)|var|uint32
func_5848_call = mutated_mod.get_global_var('func_5848')
call_5850 = func_5848_call(var_5849)
output = call_5850
func_5851 = relay.Function([var_5849], output)
mutated_mod['func_5851'] = func_5851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5802_call = mod.get_global_var('func_5802')
func_5803_call = mutated_mod.get_global_var('func_5803')
call_5894 = relay.TupleGetItem(func_5802_call(), 2)
call_5895 = relay.TupleGetItem(func_5803_call(), 2)
func_5014_call = mod.get_global_var('func_5014')
func_5016_call = mutated_mod.get_global_var('func_5016')
call_5896 = func_5014_call()
call_5897 = func_5014_call()
func_4434_call = mod.get_global_var('func_4434')
func_4435_call = mutated_mod.get_global_var('func_4435')
call_5911 = relay.TupleGetItem(func_4434_call(), 0)
call_5912 = relay.TupleGetItem(func_4435_call(), 0)
output = relay.Tuple([call_5894,call_5896,call_5911,])
output2 = relay.Tuple([call_5895,call_5897,call_5912,])
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
func_5121_call = mod.get_global_var('func_5121')
func_5122_call = mutated_mod.get_global_var('func_5122')
call_5929 = relay.TupleGetItem(func_5121_call(), 0)
call_5930 = relay.TupleGetItem(func_5122_call(), 0)
func_2849_call = mod.get_global_var('func_2849')
func_2850_call = mutated_mod.get_global_var('func_2850')
call_5933 = relay.TupleGetItem(func_2849_call(), 0)
call_5934 = relay.TupleGetItem(func_2850_call(), 0)
output = relay.Tuple([call_5929,call_5933,])
output2 = relay.Tuple([call_5930,call_5934,])
func_5977 = relay.Function([], output)
mod['func_5977'] = func_5977
mod = relay.transform.InferType()(mod)
mutated_mod['func_5977'] = func_5977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5977_call = mutated_mod.get_global_var('func_5977')
call_5978 = func_5977_call()
output = call_5978
func_5979 = relay.Function([], output)
mutated_mod['func_5979'] = func_5979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5645_call = mod.get_global_var('func_5645')
func_5646_call = mutated_mod.get_global_var('func_5646')
call_5988 = relay.TupleGetItem(func_5645_call(), 0)
call_5989 = relay.TupleGetItem(func_5646_call(), 0)
func_551_call = mod.get_global_var('func_551')
func_554_call = mutated_mod.get_global_var('func_554')
const_5995 = relay.const([-10,9,-2,4,9,8,3,7,-2,4,-5,2,-4,7,3,1,4,5,6,-7,1,8,-7,-10,2,-8,8,2,-1,3,10,7,-3,-9,-4,-4,2,-9,-9,-7,2,7,-3,5,6,8,-9,2,-9,-2,7,-10,-10,-9,-7,-9,4,-10,-4,3,-2,-8,7,-6,8,9,-4,6,9,10,-4,6,6,4,-2,10,9,-6,5,-3,8,10,-3,5,-2,8,5,-3,-2,10,6,-8,7,1,6,5,-8,-7,3,-4,8,-2,-8,3,-4,3,-5,4,9,-4,-1,-10,-5,-3,10,3,1,-2,-10,10,9,3,8,-6,5,1,-8,-5,1,-1,-5,-10,10,9,6,4,-5,-1,-6,-10,-4,5,4,-5,9,-8,8,3,10,10,1,3,-2,-9,-1,7,9,-7,3,-10,8,7,5,-6,1,-3,9,-10,-10,7,-7,-7,10,1,-8,6,-8,3,-4,-8,-2,-1,7,-2,-10,10,-7,6,-3,-9,-8,8,-9,-1,8,1,-2,-3,-2,8,7,-9,-7,10,-2,2,5,7,-8,8,-10,10,-1,-1,-9,3,6,-8,7,-4,8,-6,-5,8,3,-3,-7,5,5,1,4,10,5,5,-8,8,5,9,-1,5,-5,7,1,-1,9,-10,3,-4,-8,2,-8,-3,8,-4,1,3,10,-9,3,5,10,-6,5,-5,1,-10,10,3,-5,5,8,5,9,9,4,5,-9,-10,2,-7,5,-3,3,10,-3,-6,-4,-9,5,-6,-1,-6,5,5,3,2,3,2,-3,4,1,9,2,-10,-7,9,-1,-8,-3,4,9,6,3,-6,2,2,-1,-9,-10,-2,-7,-3,-6,-5,-6,-6,6,6,2,8,1,9,1,-7,-9,8,-9,-6,-3,-5,9,5,5,-7,-3,-5,4,-8,-4,-8,5,-10,-8,-1,-7,-2,-8,-4,-8,2,-7,-6,2,8,3,8,-3,-2,5,1,-10,10,10,2,6,-7,-2,-6,1,8,-1,3,7,4,-9,-5,8,6,1,5,-2,4,9,8,-3,5,-7,9,-4,-5,2,1,-9,-9,4,10,8,2,4,-7,-10,-3,1,-10,-9,-9,7,10,-8,6,2,-10,2,8,-5,4,-9,10,-3,6,-5,2,4,10,10,4,4,2,9,5,-7,7,8,-6,10,-2,5,-9,-7,-9,-6,10,-8,-9,4,-8,3,-5,-7,-1,-2,-3,8,-6,-2,-1,-1,-10,5,5,-1,10,-2,-4,-7,5,-9,-8,10,-3,10,-3,-7,9,2,3,9,-9,10,10,-10,9,-3,8,1,-8,-7,2,-5,8,-7,5,8,-6,7,8,-1,9,-3,9,-8,7,-9,-1,-1,4,-4,5,2,10,9,9,4,4,-4,-3,10,-10,-10,5,-4,3,-7,7,2,-1,5,1,-7,-9,9,-3,-4,10,-8,7,-4,-9,9,-4,-3,-1,4,-10,-8,2,-4,8,2,2,-5,-1,1,1,5,-2,10,-9,-7,7,-9,-5,-8,1,-3,9,5,-6,-7,6,-4,-10,-2,-1,9,6,-9,-3,4,-6,-10,-4,2,-1,8,-2,-8,9,3,-10,-9,4,-7,-6,2,9,-6,7,4,-8,-5,-7,5,2,-7,2,-7,6,5,5,6,9,9,-10,2,-7,10,-10,1,5,-2,-4,5,-3,5,-8,-5,3,-1,-9,2,-9,-2,-9,1,-1,-1,4,-6,-8,6,-2,-3,7,7,-8,-1,-3,-8,-8,-6,-1,-3,-5,-1,-1,-9,10,-9,5,-2,-7,9,-10,2,-3,-6,-5,9,-9,3,9,-7,1,7,-2,-6,-4,8,-2,-9,-1,1,-5,8,-3,5,10,-5,8,6,1,-8,8,8,-10,-5,3,7,-8,-1,5,-7,10,7,-3,7,-8,8,2,-6,-2,-3,8,-2,-6,-1,3,-5,9,-2,-6,6,-5,-10,10,-1,-6,1,6,-4,8,-3,-3,-3,-2,-7,-3,4,9,7,7,-6,-2,-9,-10,-3,10,9,-6,-8,-9,-9,-1,-10,-7,4,5,-9,6,-7,2,-7,6,6,10,2,-2,-2,6,-5,-1,8,-6,-2,6,-1,9,-1,-3,9,-2,3,-4,6,8,-4,10,-4,-9,-1,8,-3,9,2,-10,7,3,-5,6,-8,5,-3,6,-1,4,9,-3,8,4,-8,-2,8,7,-4,-9,7,-6,6,8,8,1,-5,-8,8,5,-10,-1,4,-4,-10,3,-4,6,3,-9,-5,8,5,-2,-10,1,8,10,9,-10,-6,6,4,-2,-5,7,3,9,3,-3,2,5,-7,2,9,-6,-7,-7,-4,9,1,-9,-1,-4,-4,7,2,-4,9,4,-7,2,-3,-4,-9,-6,1,7,-6,8,10,3,-9,1,-4,5,7,5,8,7,-6,-10,-8,9,-9,-1,-2,3,3,7,-10,9,2,7,7,7,-7,-10,-5,-9,4,3,6,5,-9,9,7,-7,5,-6,10,-8,10,3,5,-10,-4,4,9,1,4,-9,1,-9,-2,1,-10,-10,-4,-8,7,-9,2,-2,3,-1,7,-7,6,3,10,-1,-2,3,-5,7,8,6,-9,1,4,-8,-1,-9,8,-6,-7,-1,7,-7,4,6,-1,-3,1,-2,-5,-7,-5,7,10,4,-10,6,-8,4,6,7,2,-10,2,-9,-4,7,-5,-3,-8,2,-1,-9,-9,2,-3,-5,-6,10,-8,-9,5,2,-2,5,-1,2,-3,-10,4,-2,-10,1,-3,-8,-10,-3,-4,-7,9,8,6,1,-9,-6,4,1,4,-4,5,-7,-10,9,5,-2,-7,6,8,-5,-10,-1,8,8,6,-8,-3,-5,5,-9,-10,-9,-9,10,-2,-6,5,-5,-1,-4,7,7,7,5,6,4,-2,4,-8,1,-1,-10,-6,1,2,-4,7,8,-5,-6,6,-8,-5,-2,-7,2,-1,6,9,-3,-3,9,10,4,10,-6,-1,7,-7,8,-3,3,3,9,9,5,1,-1,-1,8,-6,8,-9,3,3,1,2,-9,-7,8,-2,-9,-7,4,7,9,-6,-9,3,2,-7,-3,-1,5,3,-6,-8,-8,7,-5,3,6,-3,6,-10,6,-5,4,3,4,5,-1,-6,10,-2,-6,10,-6,-8,1,-3,3,7,-4,9,8,-1,-10,9,-10,4,-6,7,-7,6,-3,6,9,-5,6,2,-9,5,7,1,5,-3,-2,-4,-7,9,-9,8,-10,10,7,10,-2,7,-8,-9,6,5,6,6,-8,-5,-2,5,-6,-8,7,-2,2,10,-10,5,3,-3,-9,-2,8,6,-2,1,-7,2,-6,5,-6,8,-6,-1,2,9,4,10,1,-1,-6,1,-1,9,9,-5,-9,-10,-7,3,4,-3,-3,2,9,-7,8,-10,4,8,3,8,-8,6,-9,7,1,6,2,-10,-3,-8,8,10,9,-5,1,4,-2,-5,9,6,1,-4,2,-6,2,4,3,-1,-3,-5,-2,4,-7,-6,-10,-6,6,5,-5,-3,-4,8,4,-10,-6,1,-3,-1,-5,-9,-3,7,-9,9,5,3,-10,9,-10,1,5,3,9,10,-3,3,6,-7,-4,10,-8,-9,4,2,-6,-8,-5,8,-7,9,7,-5,-2,9,1,-5,2,9,1,-10,6,-7,10,-6,4,-6,7,-6,-8,-5,6,-7,-4,-6,10,10,-7,5,-2,6,-6,9,-6,4,-1,2,-1,-8,5,-7,-2,-9,6,6,-6,-6,-7,-10,1,8,3,9,-8,8,-3,-8,-4,3,2,-1,-4,-5,-1,3,-8,-4,-10,4,2,-1,7,-9,6,-2,-3,-1,10,-7,10,5,-2,9,-3,-8,-5,1,8,-2,4,-7,6,6,-5,-7,5,-2,-2,-9,-4,-10,-7,10,3,-2,-5,-3,-8,-5,2,-7,-5,-3,2,1,-8,6,2,-1,-5,1,5,-10,-3,-5,8,-1,2,9,-6,9,-1,-9,8,-1,6,-4,-6,-3,9,5,1,2,1,-5,-2,-1,7,10,-4,10,-3,-1,9,9,6,-7,9,10,9,-7,10,-7,-1,-4,-8,-7,1,9,3,-9,-1,6,4,-9,1,-5,7,-8,1,-3,6,-1,7,-6,7,1,-2,9,5,8,-6,-7,-6,-1,-8,-7,6,1,7,6,-5,-3,6,-2,10,6,-4,10,9,9,8,2,-2,-7,-4,-5,10,5,-8,8,6,5,-1,2,-4,7,-6,6,-6,9,6,9,9,-3,-3,-6,-8,-1,-4,7,3,-2,5,-7,10,10,-9,1,5,7,-8,-10,-2,3,5,3,-6,-7,2,-1,-3,8,10,-9,5,4,9,-10,-7,6,-3,-10,-4,1,4,-8,-2,8,-6,-8,5,6,8,-4,9,4,10,2,-2,10,4,2,4,10,7,5,-2,3,-9,2,8,1,-10,10,7,-10,9,6,10,-7,6,6,-5,5,-7,-3,2,10,8,-6,3,-5,-5,-8,-9,-1,-9,2,-7,9,3,-6,-5,-7,-8,9,10,-4,8,-2,-10,-3,-2,-4,-9,3,-2,-7,7,1,8,7,-3,4,4,10,9,-3,-6,1,8,9,5,9,1,-7,8,-8,-4,4,-8,-2,-6,9,-1,-1,-4,-3,6,1,9,-10,-4,10,1,-8,8,6,-6,-10,-7,10,-1,10,-2,-7,-9,-8,5,2,3,7,-9,-9,-9,-4,10,-8,6,8,-9,8,4,-2,5,-7,4,-2,-8,-10,2,3,-9,-2,-9,2,9,-7,-6,-2,-2,1,-4,1,-6,8,6], dtype = "uint32")#candidate|5995|(1800,)|const|uint32
call_5994 = relay.TupleGetItem(func_551_call(relay.reshape(const_5995.astype('uint32'), [10, 15, 12]), relay.reshape(const_5995.astype('uint32'), [10, 15, 12]), ), 0)
call_5996 = relay.TupleGetItem(func_554_call(relay.reshape(const_5995.astype('uint32'), [10, 15, 12]), relay.reshape(const_5995.astype('uint32'), [10, 15, 12]), ), 0)
output = relay.Tuple([call_5988,call_5994,const_5995,])
output2 = relay.Tuple([call_5989,call_5996,const_5995,])
func_6000 = relay.Function([], output)
mod['func_6000'] = func_6000
mod = relay.transform.InferType()(mod)
mutated_mod['func_6000'] = func_6000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6000_call = mutated_mod.get_global_var('func_6000')
call_6001 = func_6000_call()
output = call_6001
func_6002 = relay.Function([], output)
mutated_mod['func_6002'] = func_6002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5924_call = mod.get_global_var('func_5924')
func_5926_call = mutated_mod.get_global_var('func_5926')
call_6097 = relay.TupleGetItem(func_5924_call(), 1)
call_6098 = relay.TupleGetItem(func_5926_call(), 1)
output = call_6097
output2 = call_6098
func_6099 = relay.Function([], output)
mod['func_6099'] = func_6099
mod = relay.transform.InferType()(mod)
output = func_6099()
func_6100 = relay.Function([], output)
mutated_mod['func_6100'] = func_6100
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6113 = relay.var("var_6113", dtype = "float32", shape = (16, 15, 11))#candidate|6113|(16, 15, 11)|var|float32
uop_6114 = relay.log10(var_6113.astype('float32')) # shape=(16, 15, 11)
output = relay.Tuple([uop_6114,])
output2 = relay.Tuple([uop_6114,])
func_6119 = relay.Function([var_6113,], output)
mod['func_6119'] = func_6119
mod = relay.transform.InferType()(mod)
var_6120 = relay.var("var_6120", dtype = "float32", shape = (16, 15, 11))#candidate|6120|(16, 15, 11)|var|float32
output = func_6119(var_6120)
func_6121 = relay.Function([var_6120], output)
mutated_mod['func_6121'] = func_6121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3042_call = mod.get_global_var('func_3042')
func_3044_call = mutated_mod.get_global_var('func_3044')
call_6145 = relay.TupleGetItem(func_3042_call(), 2)
call_6146 = relay.TupleGetItem(func_3044_call(), 2)
func_4702_call = mod.get_global_var('func_4702')
func_4704_call = mutated_mod.get_global_var('func_4704')
call_6152 = relay.TupleGetItem(func_4702_call(), 1)
call_6153 = relay.TupleGetItem(func_4704_call(), 1)
func_1811_call = mod.get_global_var('func_1811')
func_1813_call = mutated_mod.get_global_var('func_1813')
call_6168 = relay.TupleGetItem(func_1811_call(), 0)
call_6169 = relay.TupleGetItem(func_1813_call(), 0)
output = relay.Tuple([call_6145,call_6152,call_6168,])
output2 = relay.Tuple([call_6146,call_6153,call_6169,])
func_6179 = relay.Function([], output)
mod['func_6179'] = func_6179
mod = relay.transform.InferType()(mod)
output = func_6179()
func_6180 = relay.Function([], output)
mutated_mod['func_6180'] = func_6180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3429_call = mod.get_global_var('func_3429')
func_3431_call = mutated_mod.get_global_var('func_3431')
call_6181 = relay.TupleGetItem(func_3429_call(), 1)
call_6182 = relay.TupleGetItem(func_3431_call(), 1)
output = call_6181
output2 = call_6182
func_6209 = relay.Function([], output)
mod['func_6209'] = func_6209
mod = relay.transform.InferType()(mod)
mutated_mod['func_6209'] = func_6209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6209_call = mutated_mod.get_global_var('func_6209')
call_6210 = func_6209_call()
output = call_6210
func_6211 = relay.Function([], output)
mutated_mod['func_6211'] = func_6211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5977_call = mod.get_global_var('func_5977')
func_5979_call = mutated_mod.get_global_var('func_5979')
call_6232 = relay.TupleGetItem(func_5977_call(), 0)
call_6233 = relay.TupleGetItem(func_5979_call(), 0)
func_5977_call = mod.get_global_var('func_5977')
func_5979_call = mutated_mod.get_global_var('func_5979')
call_6248 = relay.TupleGetItem(func_5977_call(), 1)
call_6249 = relay.TupleGetItem(func_5979_call(), 1)
output = relay.Tuple([call_6232,call_6248,])
output2 = relay.Tuple([call_6233,call_6249,])
func_6252 = relay.Function([], output)
mod['func_6252'] = func_6252
mod = relay.transform.InferType()(mod)
mutated_mod['func_6252'] = func_6252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6252_call = mutated_mod.get_global_var('func_6252')
call_6253 = func_6252_call()
output = call_6253
func_6254 = relay.Function([], output)
mutated_mod['func_6254'] = func_6254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6252_call = mod.get_global_var('func_6252')
func_6254_call = mutated_mod.get_global_var('func_6254')
call_6255 = relay.TupleGetItem(func_6252_call(), 0)
call_6256 = relay.TupleGetItem(func_6254_call(), 0)
output = relay.Tuple([call_6255,])
output2 = relay.Tuple([call_6256,])
func_6261 = relay.Function([], output)
mod['func_6261'] = func_6261
mod = relay.transform.InferType()(mod)
mutated_mod['func_6261'] = func_6261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6261_call = mutated_mod.get_global_var('func_6261')
call_6262 = func_6261_call()
output = call_6262
func_6263 = relay.Function([], output)
mutated_mod['func_6263'] = func_6263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5645_call = mod.get_global_var('func_5645')
func_5646_call = mutated_mod.get_global_var('func_5646')
call_6299 = relay.TupleGetItem(func_5645_call(), 0)
call_6300 = relay.TupleGetItem(func_5646_call(), 0)
output = call_6299
output2 = call_6300
func_6301 = relay.Function([], output)
mod['func_6301'] = func_6301
mod = relay.transform.InferType()(mod)
output = func_6301()
func_6302 = relay.Function([], output)
mutated_mod['func_6302'] = func_6302
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6335 = relay.const([[[-8],[2],[4]],[[-8],[3],[9]],[[-4],[1],[-8]],[[6],[6],[9]],[[-6],[-7],[2]],[[5],[-8],[3]],[[10],[-6],[1]],[[-8],[-10],[6]],[[6],[3],[8]],[[4],[-2],[10]],[[-10],[3],[9]]], dtype = "uint64")#candidate|6335|(11, 3, 1)|const|uint64
var_6336 = relay.var("var_6336", dtype = "uint64", shape = (11, 3, 16))#candidate|6336|(11, 3, 16)|var|uint64
bop_6337 = relay.bitwise_or(const_6335.astype('uint64'), var_6336.astype('uint64')) # shape=(11, 3, 16)
output = relay.Tuple([bop_6337,])
output2 = relay.Tuple([bop_6337,])
func_6350 = relay.Function([var_6336,], output)
mod['func_6350'] = func_6350
mod = relay.transform.InferType()(mod)
var_6351 = relay.var("var_6351", dtype = "uint64", shape = (11, 3, 16))#candidate|6351|(11, 3, 16)|var|uint64
output = func_6350(var_6351)
func_6352 = relay.Function([var_6351], output)
mutated_mod['func_6352'] = func_6352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1864_call = mod.get_global_var('func_1864')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_6360 = func_1864_call()
call_6361 = func_1864_call()
func_3706_call = mod.get_global_var('func_3706')
func_3710_call = mutated_mod.get_global_var('func_3710')
const_6377 = relay.const([-5.587929,-2.535372,2.027232,-2.646176,1.367491,-9.593549,-7.343043,-6.923806,-6.091527,6.375887,5.030949,-6.443973,-5.922244,-0.226119,4.567008,5.755239,-8.746781,1.343052,2.417183,-6.233839,5.024155,9.115802,-3.400365,5.328883,-7.224805,8.547525,-9.762584,1.740017,-8.472265,-6.243448,-7.853340,2.773489,4.000885,-0.087719,7.439333,7.600096,0.352733,-4.047079,2.507998,9.260962,-0.482926,4.885462,-4.134879,-3.232893,-6.207324,-1.843762,-8.206120,-0.457627,3.306873,-0.530578,9.809639,2.914225,-2.173588,-0.732986,0.644339,7.647425,-9.290165,-0.500555,8.697030,3.164888,-2.363702,-3.905249,-4.451050,-2.185254,-0.796465,-5.501462,3.506331,-9.247438,0.520923,1.887476,-9.673624,-5.178514,8.501877,-3.738191,3.987786,8.904367,5.041415,-3.252870,-1.097998,5.908115,6.007495,-9.177575,3.115718,9.398253,-8.840479,1.476869,3.473191,8.556851,0.840658,-2.543030,-8.517808,-2.983261,4.994665,3.729129,5.358473,-3.805823,-3.451720,2.979740,-7.262179,-8.008325,0.493271,9.284516,6.640232,-8.344823,-6.744166,-8.569257,-3.040717,9.888720,6.730432,9.679652,0.946077,-3.068008,-1.674653,-0.520169,-1.506020,7.907892,-0.719879,-3.423538,-9.385673,-0.127376,2.796315,2.389331,7.298075,-8.202129,0.647241,-1.536716,5.186336,-5.886850,-8.494548,-4.837538,9.452753,0.056940,8.762196,3.258782,-1.676817,-6.882883,-1.174681,4.961869,-9.639659,7.047122,0.316148,8.663188,-3.104846,-2.852161,-1.477715,4.224520,3.523800,8.093541,-6.521159,-5.798297,8.380871,9.036569,-7.842912,6.063441,-1.220820,-7.835691,-0.588492,-3.353869,5.169195,-4.589678,-8.403284,2.318129,-9.520669,-7.920472,2.931971,5.120917,4.145755,4.654307,9.322321,8.637937,0.394916,6.755793,5.070388,-5.223451,-2.004323,-4.341264,-1.700122,-3.640270,-5.946785,0.136583,1.915108,-0.247802,0.613794,-8.033581,3.472141,-9.719049,8.180154,-9.778551,-1.139121,4.599496,8.833942,6.620596,4.142111,-2.104928,-0.040827,-0.990506,-9.649928,-9.995635,-3.665927,-1.228362,-6.907404,-2.492356,-6.593573,-9.877223,9.649133,-3.110640,7.274274,-6.859855,3.815973,1.951241,-9.141400,-6.488874,-7.984694,3.624384,5.660104,-0.032284,-9.575538,-8.014719,-1.327051,0.499289,-7.155344,-0.442990,9.169487,6.900615,-5.838756,-1.984177,-2.486919,8.893990,-8.206807,5.745267,2.839934], dtype = "float32")#candidate|6377|(231,)|const|float32
const_6378 = relay.const([8,2,5,10,2,-1,-9,-10,-5,10,-7,-10,-7,9,-4,-10,4,-10,9,-5,5,-8,6,7,-2,-3,-5,2,-7,9,-1,-6,2,-6,-6,-2,8,3,-9,-7,9,-2,2,6,6,3,-6,-2,2,1,-8,7,4,-10,-4,4,9,-8,9,-10,-9,4,-1,6,-4,-1,8,10,2,5,-1,1,-4,-2,-3,9,7,-1,-10,4,-2,10,-7,-3,4,-4,6,6,-4,-4,1,3,7,-6,1,-2,-7,6,-3,-2,9,-2,3,7,-6,-6,-2,-3,-5,5,1,10,10,-3,-4,-1,-10,10,-1,-3,-5,4,-10,-8,7,10,1,-7,5,-3,4,-4,7,10,-8,-6,1,-4,-8,5,-8,-5,-6,-1,4,-2,7,5,-9,-3,7,3,1,1,2,5,5,-10,-4,-4,6,-7,3,9,6,-10,-3,-2,-2,4,-1,5,-6,-6,5,-9,7,4,-9,-3,-4,9,-8,4,6,-4,-4,10,4,-2,-6,-10,8,-5,8,3,3,-1,-7,-10,10,9,-5,-6,6,9,-1,-5,4,8,-7,4,-5,10,-8,4,-8,-4,1,-1,-7,9,9,7,-5,5,-5,4,4,9,-6,-1,-5,7,-4,5,9,1,9,3,-4,7,-7,-9,-5,-4,3,-9,-2,-4,-7,10,-2,-5,-1,-4,7,4,2,-7,-4,-2,-6,-5,7,5,-10,-9,-7,5,3,3,-1,-3,10,2,1,-1,4,7,7,5,-8,10,-1,3,4,-3,3,-10,8,-7,9,-7,-5,-4,8,-10,6,-4,-4,-10,-3,5,-8,8,-10,-4,4,2,8,2,9,-6,3,-1,-9,9,-3,7,-1,9,2,2,5,-5,-2,-10,-2,-8,-8,-4,-10,-6,-7,-6,10,2,9,5,-8,8,1,2,6,-8,9,-9,5,3,2,2,5,1,-10,9,-1,9,-6,-5,3,7,7,2,-5,6,6,-9,-4,6,-9,1,3,3,-4,-4,-4,-10,8,7,-9,-1,2,6,10,-1,9,10,3,1,-4,4,-5,10,-8,-7,1,10,5,1,-1,6,-4,10,-10,5,-6,-3,-5,4,-2,-10,6,8,9,-9,-2,8,1,-3,1,-6,-1,7,4,9,10,-10,-1,-10,-8,9,-3,-5,-7,5,8,-6,-10,5,4,-3,5,-3,-4,7,3,1,4,-10,4,-2,5,-9,1,-1,10,-1,7,-1,6,-2,-5,5,-9,-2,-8,-5,-4,-2,-10,10,-6,5,5,-6,-4,-10,-3,10], dtype = "int8")#candidate|6378|(480,)|const|int8
const_6379 = relay.const([9.064194,3.304912,3.801132,2.199569,-6.814531,-2.233041,-2.305575,9.484415,-4.811023,-4.061158,-0.310973,2.422684,-0.807732,-3.699085,-7.903438,-9.683744,-6.603447,-0.934703,8.751127,5.630099,-6.124461,-8.813549,-4.892744,7.798431,2.358898,4.674825,-1.617624,0.416844,8.794172,-8.461814,-3.119694,3.221517,-5.549185,-0.551871,-9.961387,-8.571861,8.704373,5.062699,-7.062317,-3.071986,-1.559215,-9.012332,-9.670625,-2.582477,8.714252,-0.603191,6.238202,-3.607700,5.416794,5.483916,-7.161340,-9.322710,-9.927515,-0.684456,-5.146949,6.465940,-9.184888,4.144633,2.590940,-2.070077,4.477172,-9.034988,1.692309,-8.804756,6.642634,-7.770201,1.757187,3.598151,-7.796132,6.835950,0.466562,-3.589396,-7.405082,-2.461783,8.562221,-3.572904,9.293853,5.210637,7.975430,-1.982213,-5.609438,-2.156928,1.044256,0.385712,2.482236,0.847334,6.119427,-1.286781,0.279722,0.696102,-7.911501,2.015517,-4.554554,-4.111060,0.216096,-0.154390,0.081821,2.707834,4.562825,-8.935667,0.775321,3.569285,9.615047,-9.811640,-0.706850,9.695490,9.122195,8.986908,-1.463610,9.586748,-5.723548,4.047263,5.795811,-1.518617,8.657563,8.046283,-7.167702,-0.887426,4.743089,2.465826,-8.285729,-4.920213,4.417586,-1.973279,5.258442,0.177247,2.712357,7.196015,-4.696592,4.303875,-3.176409,-6.332906,6.031104,4.362432,-6.686271,1.811233,4.442848,-9.450294,8.985481,-2.184708,0.731216,-0.643881,-3.342704,7.547943,9.720123,7.981733,2.364138,8.401916,-3.363904,8.670056,0.138477,3.757542,-8.571579,2.268989,-4.100057,-8.471120,-6.673186,5.344317,-8.495062,5.018759,7.034026,-3.936771,-4.126661,-8.336225,-8.279714,5.564624,-5.307043,-0.520886,7.433375,-8.998130,-8.813108,1.797657,1.299607,2.814739,2.174945,1.029744,1.468543,0.860007,4.278991,-4.971715,-4.964178,6.475660,3.699503,5.239557,-5.767187,-7.040767,3.004451,0.731831,-9.773860,-1.558628,8.012001,2.669357,6.151082,-0.727900,-6.708820,-9.079825,9.624933,7.144370,-9.340335,8.000946,-6.819994,5.866290,6.775450,-6.640627,1.840584,1.052239,-1.421696,-6.526857,4.149081,9.076631,8.155928,-6.946204,4.459154,0.340290,2.090426,-7.801469,6.876590,0.271425,-2.304155,-0.900135,-3.518071,-4.753708,-1.718879,4.867981,-1.502989,5.337964,-2.855478,-8.660074,0.589589,9.172905,-0.662031,-0.252613,5.591835,-0.555202,7.244807,-8.321964,-2.403193,0.187438,2.098912,-4.827044,0.010456,3.368264,-3.270892,3.753838,-5.610186,-0.966828,2.245819,-8.828679,-6.012162,-1.036495,0.657885,1.225475,-2.649660,3.623775,4.011286,3.480530,2.319077,0.733225,-1.584115,-7.240534,5.291909,2.020523,5.497337,-1.754295,-5.454016,-4.461218,1.662432,6.647670,-2.716157,2.231885,-7.520838,-7.198671,0.833461,8.236488,-3.425395,-1.829996,-1.211634,-0.376743,2.109069,2.518355,-7.178423,-7.191895,-8.311795,7.707615,-2.755014,-8.942271,9.260627,-4.035545,-3.836010,-3.870375,7.284379,4.433387,-0.923180,-1.648000,-7.449665,5.539128,5.413692,-8.029279,9.455109,-2.282149,-8.280738,-3.166812,8.752096,-5.051817,8.616060,-7.810370,-6.187848,-2.736306,-6.160347,-5.196028,9.818706,4.564692,0.030542,-0.510320,0.638721,-3.669910,9.307783,9.701976,-8.978626,5.686327,-7.153416,-8.015703,6.098704,8.722802,5.809426,-5.787669,9.792212,4.583929,5.290789,1.559952,-8.066680,-0.905619,-1.997181,-5.394822,8.858424,-4.660448,-6.004378,-6.423746,-6.769355,9.334231,-9.609926,-6.854058,4.978851,-0.043033,9.761418,0.452597,-0.412040,6.573554,9.791559,6.408943,3.225409,-7.862063,-3.322152,5.255138,-2.250688,5.146754,-8.704892,-6.744935,5.291362,-4.632084,-9.206256,5.255676,7.138387,2.890560,-8.871953,-6.142617,9.357936,4.641984,3.180855,-5.894378,6.295247,-3.750639,5.479077,0.161678,-8.912715,1.532367,7.514284,5.001697,7.216137,1.767957,2.455300,-5.389952,-0.460308,-1.388016,-6.540885,8.134828,-8.859083,-2.328981,-3.687024,7.417675,0.709096,0.419765,4.977871,-7.416113,-6.265280,-3.252891,2.954109,-4.345709,2.246459,0.606834,9.867415,5.549432,6.994402,1.664781,-9.804662,-1.390738,6.454130,-0.711646,-7.211234,8.909101,9.205076,-6.292201,-8.486905,-8.501113,6.055670,-6.962783,6.805946,7.093574,3.105287,-9.660544,1.802289,2.320663,4.899319,1.431243,-8.725283,-5.426226,-8.442891,-7.555018,5.353864,-7.933249,6.826846,0.527456,2.842975,3.107288,8.524703,-3.867663,-1.190395,2.204060,2.368203,2.845674,0.412340,6.260424,-3.864625,5.355639,3.111438,-7.863983,-4.542160,1.447218,-5.067549,-6.446334,-3.706983,-3.022993,-4.073705,-8.637472,-4.178877,-8.671787,6.468967,-4.041926,0.682000,3.934636,1.559093,7.135991,8.933082,8.216524,6.033598,0.265886,-5.417841,-0.247598,2.015887,3.349720,-3.367012,-4.662879,0.789883,5.778152,-7.989533,2.437303,5.627006,6.784037,0.766881,-9.247615,-4.158963,9.096208,-7.810426,1.126493,-6.370719,3.049057,-9.803491,0.656794,-8.694037,5.601640,9.171962,7.339984,2.729815,-8.189702,5.338005,-8.301939,-3.733051,1.304696,6.871458,6.628160,4.224651,6.127613,-0.005337,8.435768,2.847564,9.212267,-3.135670,7.273509,5.060288,-2.744914,9.686547,-1.612455,-0.481439,-2.772224,-8.566296,-6.226920,-6.175549,-0.657473,-1.836716,-4.735402,-6.984013,-1.056008,-1.975604,-3.342776,5.007504,-7.234610,6.785716,1.076306,-5.930627,-7.610443,1.152132,-7.003803,-7.715490,-5.523609,7.416867,-2.257104,-4.190046,-1.940464,2.810155,-2.008191,5.950670,8.177783,9.727638,8.029477,-9.188536,-1.084184,-0.314060,3.468651,3.117903,6.285844,-5.002566,-8.100996,-9.402557,5.366576,-9.689731,3.376075,4.517094,-7.522127,7.266906,-8.919399,5.666488,9.609571,-1.009711,-1.630063,-0.295467,-7.621925,-8.994846,5.805481,3.280190,-5.248859,-7.422599,8.932700,-4.330462,-3.490508,6.964597,7.388581,1.261095,-6.485078,3.542240,-6.379415,-6.934965,9.655006,8.548186,-9.212452,3.458128,-7.809565,-3.896406,2.111597,-7.595637,-4.584916,3.784852,-2.508639,-2.090327,-4.424409,-5.568087,2.579226,9.624069,5.889395,0.802127,1.826643,-7.907937,-6.749203,4.443957,9.165711,8.935392,-6.908901,7.850626,4.906077,1.404802,4.119213,-4.465676,4.893606,2.879489,1.360041,-9.984521,-9.626496,-4.741660,9.841605,-3.957948,0.805049,-5.486952,-2.515059,5.922800,7.531664,5.681014,-2.059216,7.140100,0.305244,-9.780331,8.222217,6.528936,5.339000,-2.656919,-5.754279,0.963726,-4.268475,9.007144,8.903168,-9.985557,5.218957,1.716083,-1.450533,1.099003,-5.516778,-1.341536,-1.204904,5.970966,4.738280,-8.898710,-5.215959,-3.532049,7.026223,-7.859676,-9.852978,9.683654,-0.137647,2.991148,5.199921,8.916759,-7.086450,8.531332,4.296935,-6.207641,-1.071419,-4.991577,-5.069336,8.345632,-9.905764,-1.572298,1.103693,3.686334,-0.289200,-9.630836,5.216674,9.317936,8.068581,2.300678,7.139550,6.126652,-9.704264,6.602321,-1.861763,2.546421,-9.422758,8.625593,7.629639,5.996360,4.033107,-1.762430,1.506184,-9.444202,-3.941989,-3.205725,5.832291,-8.526836,1.331063,-1.500221,-5.128307,7.261423,7.667132,-3.371240,5.225115,7.423745,2.941136,1.706808,2.346060,2.451343,3.019953,-8.138567,-3.220888,6.081814,-6.096952,9.493829,0.716816,5.339693,-3.883867,9.546855,9.954258,-0.685612,-1.045750,-8.252455,-7.368400,-5.622403,0.089750,-9.956979,2.315803,2.068122,-7.266065,-5.091911,0.169515,-4.071165,-7.826713,7.979370,-8.238579,-2.476827,-8.350390,1.172320,6.688811,-4.622421,-0.603066,-3.576953,-7.346081,7.472666,-1.633063,-2.354630,9.029399,5.403548,6.875525,1.961432,8.889324,-8.993134,-1.441185,-6.153441,4.873985,-0.797582,4.346641,8.318592,7.397710,-7.457934,6.971504,6.919937,-3.049025,-3.094246,-2.496448,5.965184,6.771324,7.579607,1.774644,8.507366,-6.622573,-5.641574,-3.033676,-1.536993,-8.844994,-1.960515,7.925302,-9.050039,-7.114049,0.187302,2.096056,-2.095755,0.155830,-3.767361,5.580563,4.330027,-6.969549,-8.500226,-7.123527,-0.273377,0.727496,-3.767444,-5.966782,-6.900098,6.666511,2.561376,8.634619,2.011811,9.562633,6.251025,-9.241974,4.774612,0.170306,9.360671,-0.899764,-3.125708,-4.319021,-1.289744,-4.290149,-9.727684,6.457249,-0.207391,1.989987,9.196306,0.837936,-6.396511,7.188861,-4.602460,4.933475,-6.191924,4.030236,4.257582,0.830286,4.313875,9.996087,8.286713,6.365493,8.877982,-7.887721,-1.511797,6.818811,2.984398,-2.982717,7.993164,8.404435,2.658256,7.326695,5.131448,-8.608435,-4.513697,-2.241578,-4.673398,4.505499,-5.579375,-4.323793,3.892355,1.956893,9.755112,8.115793,8.282393,-2.563961,8.891095,-1.290201,7.432682,8.542982,-7.419618,7.492999,-4.474578,-5.911182,-2.619513,7.665822,-6.274429,-2.948925,-4.071310,5.845043,6.458711,-6.743073,0.936985,9.611819,9.414219,-0.641794,-7.955982,9.487467,-5.634573,8.323856,-1.074030,-5.935811,-9.618110,-1.496261,-3.852440,-6.454445,-3.406921,8.899575,6.150703,-7.495999,8.009786,-0.571799,-6.283896,-4.016515,4.662414,-4.977378,-4.929390,7.532143,5.022068,2.850326,7.114438,6.684566,-2.443534,6.976970,6.975031,5.382494,-5.850415,-3.164509,7.363636,8.468526,5.233346,-0.748056,-7.847025,-6.835086,-9.587637,-3.600292,9.843889,8.887450,-9.991395,-3.198614,-7.615135,-3.006301,3.376030,3.966600,-1.091316,-8.363995,-8.781763,3.390758,-7.445068,3.747160,-5.200936,-9.112834,9.446653,0.217997,-4.056247,-7.915998,9.099464,9.060952,1.470770,5.821182,0.203181,9.056571,0.623124,-0.106108,-8.136919,-4.657277,5.074577,6.821220,-8.310258,-8.038469,-1.822454,9.978147,-2.907278,-7.350341,6.866270,6.446200,3.669040,2.995948,8.384390,-7.246532,0.326663,-6.411836,7.427796,0.156058,8.637818,-3.933175,-0.481591,0.986643,-8.786918,7.095860,-6.433892,-2.150271,5.236932,-5.320204,-2.371757,2.750260,4.323995,-8.481837,1.023538,-3.610355,-9.655691,-5.975476,-6.223968,1.894317,9.488427,-3.107762,5.165176,-5.370195,-1.988306,8.175629,0.786268,-8.968214,5.334141,-1.881148,9.177818,1.475893,0.966665,-2.984616,6.659070,1.047706,-6.432193,-5.187500,-5.949311,0.377515,0.064142,3.326527,4.414449,8.979248,9.583236,4.734124,-1.659029,-1.940979,-7.929367,1.567988,-8.761056,-3.252364,3.582070,-5.140286,5.093440,-1.306221,-0.516235,-5.695375,-4.836459,-0.469248,5.078383,-2.153636,-1.316941,3.758573,8.370714,3.835359,0.715338,7.158888,-5.868630,7.254634,7.524409,3.548295,8.691872,4.306656,6.702602,0.134259,4.449348,3.846659,-7.972304,-3.129833,1.797728,2.020572,0.721109,5.129914,-8.987830,-0.674250,9.649746,-2.804275,8.056931,-8.274627,8.857562,9.031591,4.443868,3.800211,4.163616,0.809215,5.735196,-1.050568,1.420881,-9.100298,-0.663751,4.174987,-8.857690,-8.641010,4.840612,7.152788,5.823090,1.439151,5.987228,-9.507558,-1.793120,4.413153,3.248505,7.008705,-5.116937,-6.858425,-9.294023,-2.403192,8.436522,-9.921125,4.174099,-1.538505,-0.116483,2.046344,-4.217509,-1.278179,4.402536,-4.156532,1.323959,-3.876757,6.312243,-3.947124,-9.668869,2.887672,-3.240583,1.147404,9.763917,-1.644288,2.388767,9.661941,5.456694,3.174508,9.481583,1.081571,5.098697,-6.641123,6.207888,-1.895419,4.234226,9.332360,1.637381,5.967655,-5.887674,-3.339833,7.625004,1.882875,1.631096,-4.750796,-1.958494,-9.964239,1.933218,0.508486,1.665816,-0.032523,9.907439,-3.563361,-9.178853,8.140764,7.925665,4.767708,9.195306,-3.897149,7.541855,9.288980,-6.347990,9.939174,7.297712,-9.665229,-1.536322,3.381170,0.950973,-1.952399,-8.915962,-4.119138,2.297282,-8.956836,8.536462,1.986227,3.185188,-5.968534,-3.526383,2.914059,-0.110446,4.760642,9.381738,-1.980518,-7.441189,-8.617539,-5.005801,5.084578,-8.116806,-1.174983,-2.089995,-3.096996,1.019979,0.852112,-7.123625,7.077660,7.881181,4.566442,1.954797,8.391000,-7.292891,-2.574885,-1.533674,-9.861797,-5.757854,-0.051754,9.435259,-0.421312,-4.046754,-4.477851,1.375576,8.106860,-5.475148,1.001122,6.095439,-6.032124,-0.212834,-9.560152,-0.628668,-9.933347,-4.570912,0.491325,8.513495,-8.502224,7.981104,2.667291,-4.907320,1.176291,1.275446,-5.203487,5.386554,8.886315,-9.287463,5.469535,-3.009018,1.241474,-6.004512,-6.443162,-9.982779,0.787903,-3.707481,-7.994756,-2.771122,5.151540,-5.674393,-6.487215,-8.279050,-7.266642,5.294268,9.463634,8.875069,-6.636193,4.559788,1.127718,9.132864,-2.182456,8.879391,-8.024798,-4.569454,-0.680842,-0.390419,5.517435,-1.720491,0.512446,9.029350,7.965189,9.996993,-3.282487,0.927759,-8.398352,0.499670,-2.681907,-1.994132,-7.202870,-5.967577,1.587856,9.262203,-2.139602,-2.814610,9.082552,-4.721501,-4.714594,5.365348,5.268418,1.821314,7.399909,-9.250008,0.099413,7.863078,3.469954,-2.599042,-6.732666,5.124208,2.758131,-3.280697,4.853996,-8.454556,-7.255186,1.660806,-9.245184,5.965773,1.743637,7.027678,-4.960613,-8.070839,-4.804700,3.298166,-4.336846,8.447967,-4.000828,-9.085370,0.589280,-0.868872,-0.816561,2.244393,-8.062614,2.884290,-9.601160,-5.822482,8.609945,-0.631071,-3.094855,-9.011025,2.760384,-0.779230,3.046984,8.140105,7.200109,-8.244952,4.204485,-3.670679,-2.548540,4.370113,-3.431736,-4.484457,-4.073799,-3.283011,-7.066098,2.074774,-8.582954,1.416314,4.556497,-6.952765,-2.628178,-6.679557,-8.590047,4.642593,-8.971912,8.354451,6.177481,-6.925157,0.903165,-5.756683,6.124561,9.355484,7.037877,6.041934,9.210077,-9.321045,-6.615748,-4.977495,5.012313,-6.751652,-4.126609,8.355031,6.948241,-6.421144,-8.613730,-9.354346,-9.194731,1.485939,-6.618386,-0.078081,5.898424,-1.589020,-6.913726,-2.246608,-0.957836,9.941820,7.719386,-6.357777,2.228626,6.853642,0.196276,6.084274,8.429970,-7.039101,-1.795118,5.731214,4.652337,4.302206,-6.947394,3.227655,-5.783609,-9.000887,8.539612,-9.649169,8.785702,-6.479858,9.326444,-1.497321,1.038824,2.390392,-4.198228,9.420666,-2.251128,8.913902,-4.420622,5.633295,4.379474,-8.177202,5.515042,2.698268,-5.121478,8.312531,-2.624005,-9.419989,-2.572853,6.712631,1.057470,-7.339829,0.916353,-2.628571,9.868446,3.042289,0.083333,7.961153,-3.795803,2.682627,5.451188,8.469814,9.940398,7.841618,7.408944,-3.352259,1.050483,-2.596360,-1.108122,-4.104801,-8.532804,-3.208302,-4.145201,-7.219064,7.424457,6.444874,0.892566,-4.810798,4.662044,-2.166091,-0.538789,2.403044,-2.748075,-6.256050,-0.957503,-3.622683,-9.716851,5.699973,-9.176824,-6.158165,7.758361,-2.661636,-5.109844,6.113000,-9.529219,-6.175158,-3.698260,-0.591821,0.843547,3.207586,-8.491816,-3.429523,7.723797,8.986378,-0.784627,3.709496,7.200374,-8.732065,-5.725081,9.707684,6.783177,6.202587,4.709819,-6.278812,-5.816097,5.185717,2.848717,-1.749200,5.323563,5.538352,8.723475,9.621480,-9.945766,-0.808693,-0.627799,-9.935176,6.567348,5.239137,3.726221,9.196984,-0.461569,-5.532850,-4.999798,-0.713619,-6.882539,9.393370,-6.540885,9.645479,-0.678569,5.181901,1.252272,4.384730,4.671154,-2.482892,-2.751928,-4.760339,-6.855078,0.872503,0.044189,-6.270076,2.286720,6.340364,-6.003719,-2.095122,-6.208271,6.609628,4.051991,-4.923124,-7.163447,-7.483538,-9.733406,9.081159,9.498285,-8.926138,-9.452539,4.416477,-4.780028,6.858889,3.779099,-7.439113,2.129341,8.686303,-4.016981,0.446178,-7.428746,6.945319,-4.640697,8.889435,3.197389,9.812988,-5.188658,3.401665,1.106459,-0.057189,4.772639,3.916495,-6.250590,7.213482,-2.389963,1.603307,-9.941265,-2.499505,6.431453,3.330331,9.745709,-4.347115,6.815041,-0.546879,-5.228620,1.126285,7.364746,-5.084541,6.537565,-1.622479,-7.492713,3.584950,3.733477,-5.490324,0.917684,4.291054,-7.387299,7.610708,-9.816381,-7.025928,-3.711178,-8.941589,-5.084409,6.537263,-0.840264,-8.106525,-2.588725,-4.560818,6.587892,-5.333958,-9.343256,1.445636,-1.447187,-4.125711,-7.512965,0.743153,-1.579575,6.067662,7.692530,-0.484910,-8.614352,-7.286870,-9.371596,-6.889109,6.577142,0.367215,6.219539,-9.275567,3.256119,-0.924221,-6.416678,-6.010534,6.815695,0.057361,-6.968528,-2.814965,-0.293678,4.196133,3.183586,-8.322418,8.046844,-6.914664,-6.476927,-6.283433,0.749033,-6.179809,-3.098983,-0.844382,-2.806055,-2.057580,-2.682953,8.886075,-6.726685,6.394330,0.777740,-9.512032,6.009067,0.191826,-1.350276,2.758538,-4.706423,3.793225,-3.428900,-5.214956,3.111671,-1.511638,0.500210,8.005178,-4.431155,-9.666048,-1.579214,-7.648993,8.724120,-3.535118,1.031886,-5.681723,2.621053,1.424143,3.557292,-3.851449,-5.853018,-1.554631,-3.040854,8.908041,8.156862,-2.121325,5.138529,2.776251,-2.010245,-2.426105,-7.877251,0.888053,-6.850976,2.063657,-3.682663,-8.041205,-5.261700,7.746256,-6.674966,-2.062854,-8.564506,-8.971602,1.585338,-3.014397,2.734756,-3.493155,2.613295,0.021841,-1.816450,-2.414959,-8.744545,9.793818,9.704473,8.815879,-2.428151,9.983310,7.666087,-3.171793,-0.556398,-1.669598,6.828896,6.870304,8.589446,-8.898464,8.200485,-5.034996,6.628750,8.981310,-4.274443,2.192121,-4.973106,2.694688,-3.375016,-4.460255,0.152070,-2.226163,2.879148,9.024326,-1.246033,-0.568904,-9.201753,4.427724,2.079401,5.976867,2.865107,-1.891549,8.001294,6.519874,6.949156,-4.977534,9.899156,1.670006,-9.659409,2.818290,-1.646135,6.254880,-7.852857,-9.934270,0.656820,-1.005488,-4.097458,-2.152757,-4.161526,5.779570,9.990663,-1.837935,-3.808912,-3.562890,7.739001,5.616231,6.629190,-2.846506,2.471194,4.775288,-7.021166,-7.408253,-8.999553,8.644750,-5.476894,-3.338993,-1.856101,-0.906208,-4.638827,-1.018363,-0.687128,8.015519,-5.579857,-7.983219,8.717672,-1.076332,5.055885,-1.869401,2.554789,-1.416531,4.182618,8.590295,-3.610920,-3.369014,-5.857322,-6.710850,8.063611,7.003954,9.812522,6.133966,4.148643,7.907527,-9.148560,1.596586,4.828508,-9.275523,-3.121122,-3.492096,0.957478,-1.775328,4.382222,4.785424,-7.830370,-9.885543,-8.343817,-7.221059,7.926422,-8.128409,-7.698118,0.299804,0.371123,-4.648326,-6.833744,-6.511669,2.397050,6.813329,5.613927,8.917533,1.795127,-7.829719,-9.459286,-2.152037,-0.392636,3.600948,-5.817774,-3.135774,-5.175108,2.853646,4.988861,7.818266,-9.180132,-9.255193,9.877352,-4.113242,9.735234,-8.022448,1.296614,-4.960752,4.020966,-8.229621,-1.450213,3.421868,0.139665,5.190553,2.837324,-9.065753,-1.600631,3.437725,-4.287185,-8.405722,-9.487115,4.540917,0.127661,0.763349,-7.335401,-4.768789,-9.133963,3.701176,8.151518,2.598360,5.267553,-9.801516,-6.896094,2.761861,9.253258,-3.493708,-1.121953,-2.116630,9.349205,-1.456769,5.473908,1.459780,7.618551,-3.909359,0.365112,8.404025,1.052404,-5.459265,1.652984,-9.207639,-2.985902,6.202510,5.747605,-5.447483,1.956349,-1.985319,-8.567824,1.567202,-8.869344,-8.503241,0.884805,9.929565,3.620462,-8.055642,3.453141,-5.717802,6.104097,6.280313,3.967922,-8.562809,-7.076267,1.294597,-1.570429,-9.831713,-4.406348,-6.134646,-3.044671,-0.315706,-1.248738,5.971802,-7.433145,0.855569,3.988591,-7.957765,-3.005545,8.390097,2.478437,7.683019,0.215905,-1.880688,-6.728089,7.916071,-2.826166,7.699873,-2.431768,1.909338,-5.295471,6.967186,2.078145,-4.724434,-5.707199,-0.133404,-2.828178,0.030084,-7.417169,-1.115281,-7.573148,2.909683,9.040076,9.565882,8.280828,-6.886779,4.877857,6.045921,6.348542,9.898483,-7.398381,3.188991,7.667290,-6.063349,9.022487,0.978025,2.236762,-5.722615,9.222328,-0.410061,-2.314392,-6.147282,-1.263037,-7.419921,9.196731,9.516052,-6.249135,-5.792660,5.533946,3.736336,6.007624,8.158527,5.574587,-9.091233,1.204984,-4.136857,9.441552,-8.964468,-2.761655,-2.351245,-5.722250,9.945957,-9.451681,-5.593366,2.483922,-2.265621,-5.479031,6.902125,-0.551183,-7.978586,-0.641769,8.094320,7.760680,-5.389826,3.226711,3.151847,-6.225645,-8.959663,0.297274,4.423691,-2.524353,7.513098,7.483707,-8.582960,-5.672237,2.063783,9.896651,2.559024,-4.848476,5.256841,-6.933616,4.329152,6.208220,0.360676,0.263356,8.698097,3.607124,-4.206552,3.989693,-2.470100,-5.805101,5.921355,-6.022261,-5.132975,-0.582791,-0.523446,2.969868,1.945722,4.312504,1.086022,2.142895,-5.919310,4.011053,8.183021,-3.168764,2.653098,-4.643026,-5.868384,3.382431,0.522452,-9.370158,-3.771867,-9.063175,5.215993,-9.856010,-5.078267,6.515922,-0.646233,9.480944,-0.881007,7.017513,-4.282121,-4.675121,2.255605,-1.076369,6.926546,-8.040081,-6.779025,6.710912,6.175948,-8.279949,-2.918696,-5.761566,-5.949384,-2.927215,7.239961,-4.371547,2.507499,5.121207,-5.982071,-2.465666,-7.875167,6.332381,6.198596,-3.063294,3.283988,-2.274275,4.395299,-1.539218,-6.101824,-0.003942,3.271013,-0.559575,3.895563,1.068231,9.276821,6.158136,-8.894619,-1.787075,2.726698,-7.272192,3.609571,-2.799649,-4.726337,-2.303504,-7.098497,-5.220843,-8.716437,-6.063979,-7.246548,5.612328,0.111186,-8.632312,-3.975923,8.630817,8.586274,-3.377507,-9.100618,5.652484,8.854264,-0.011087,-3.326182,2.201113,6.075026,-1.539143,1.556869,6.380464,-1.791759,3.403512,-7.317697,3.084435,-5.751532,-1.955782,-4.630435,8.513535,3.009280,5.611277,2.037877,-8.243352,1.465943,-2.201505,1.618223,6.856388,0.248749,-5.036132,-9.696490,-0.068272,6.588572,9.383714,-2.522806,8.156188,-5.526969,-5.768302,-1.866689,-4.171695,1.637690,-3.268210,-0.702455,8.586196,-3.436566,7.551437,9.175554,-4.394459,-7.574019,-8.560452,-3.482346,9.436705,8.865562,-4.991095,-7.486300,3.712524,-6.409858,-9.697141,9.993937,-4.160315,7.635758,-1.487893,8.196587,0.847497,7.204625,5.052083,-5.743631,-2.363103,-5.033702,4.473514,-1.247538,-5.775667,-3.830576,2.965099,-7.372807,-6.222089,-9.061493,-1.353663,1.029960,6.129375,-2.018990,-7.074511,0.808071,-2.051572,-5.125293,9.454985,-0.442257,9.947416,-6.030315,-2.772779,-8.282818,4.522621,-9.594795,1.207212,3.652580,-2.758133,3.817861,-4.390966,2.797524,-6.405007,-2.014755,-2.466501,5.092478,-6.821949,6.712680,0.457136,8.397032,-9.114525,-5.145386,3.750307,-0.227200,6.453915,-4.043139,1.980178,-6.423418,5.694243,0.126092,5.145285,1.931402,-0.850537,7.886344,8.006952,-8.762847,-9.786950,3.976328,9.320088,8.242129,3.955108,-4.933970,0.392093,-6.847368,-7.920818,7.555089,-2.604028,6.546909,3.326773,-6.971783,5.649701,-4.209587,-6.625987,1.791023,2.270851,-0.777233,-7.830887,5.200104,-4.724894,2.645036,8.227093,-9.556030,3.128084,7.734531,-7.711799,4.177161,-4.677713,8.340761,6.628490,-0.690180,0.273576,4.408906,-0.636528,-2.719245,-1.148348,9.443357,-4.029038,-5.765049,5.718876,-4.198877,5.027983,0.354596,9.353432,-7.906402,8.177516,8.290787,-8.272392,-5.459420,-6.238185,4.683261,-5.457727,-7.827214,-6.941685,5.650827,-0.269749,-5.500504,6.428670,-7.085734,-6.389724,-8.506960,5.687816,6.914793,-4.746063,-5.234896,-1.730425,-1.102409,-7.111451,1.927831,2.469599,-9.232877,-7.806101,0.336649,-1.209039,-7.702586,4.659952,-4.620856,-3.032915,-5.514373,-4.863254,8.672956,-6.946229,1.464494,0.243432,6.325603,9.085139,-4.486177,-6.962519,-5.472291,5.722285,-5.472635,1.424212,-3.472866,-4.503138,-3.802106,2.519775,2.142177,9.021233,8.517110,5.989874,1.613293,-4.206893,-1.603441,-3.834405,-8.788958,5.326945,-6.858610,5.885013,-5.011230,0.887338,-0.324069,7.487129,-3.588373,6.711202,6.701218,-7.074194,2.473683,-4.282081,-2.417075,-1.208101,4.059289,5.153716,-5.745630,-2.874991,-1.203519,-8.266567,-0.803560,-9.140434,-6.096635,-2.575894,-7.390136,4.196739,-5.433102,3.358576,-4.239367,9.086765,2.388997,5.133716,0.461261,-2.597197,2.292355,9.970064,-0.328923,-1.774961,6.242385,-6.171530,5.492879,2.588887,-0.973752,-9.136772,8.411359,-8.320802,-2.770381,-4.272178,6.424817,7.280316,0.108772,-3.565412,-0.481464,9.514922,-8.353456,4.262520,8.521164,3.965707,7.238743,-3.842063,2.153334,3.906790,-7.443668,0.119127,2.280507,-6.101296,9.798164,-8.078645,4.133912,7.411909,-3.751104,4.424092,-9.588384,1.077289,5.244178,-5.940335,-7.606033,-0.898431,8.335349,-5.678307,0.447718,-5.635188,0.973984,-6.724591,-2.448871,-6.104524,6.099501,-2.070489,-1.643493,7.112327,9.243286,-1.974868,-4.381134,-8.767955,8.669633,-7.199258,4.302971,3.510603,5.427863,2.520834,-0.026076,-1.367657,1.513708,1.901802,-5.116890,6.230493,-9.209508,0.406018,7.724865,-9.997983,-7.878280,0.375406,9.437165,2.000262,-1.195547,-8.615371,-3.959368,-8.017538,2.492972,-7.962172,7.352806,0.192858,6.912985,-7.321995,-7.578472,1.354383,8.173535,-5.987334,-4.019479,2.214215,-6.212077,9.950982,5.713173,8.770488,5.474978,-2.741544,3.263275,-9.652281,7.878133,6.323620,9.698744,-3.212959,8.372925,-6.026761,-5.454083,8.348233,0.056362,-7.151282,-6.544011,-9.971518,1.896143,-2.662625,-6.721733,6.473571,7.757218,-8.161864,-4.735060,1.352262,9.389952,2.336669,-2.004274,7.173258,6.417028,-2.628762,4.115541,9.868052,4.062808,1.997937,-2.158600,2.492516,-9.521652,-0.405690,2.621828,-0.708101,5.468075,-9.300468,-3.642552,-1.979684,0.387489,-2.898546,6.082459,1.896857,5.780830,-0.346005,-2.637659,-0.702313,5.282805,6.158881,-8.120541,-0.935808,8.782140,5.063160,-7.497142,2.341606,-5.914651,-2.718341,4.355187,2.573441,-2.367730,-0.037852,1.530813,7.566940,9.398805,7.170532,7.519214,-5.346633,8.941248,-3.781752,2.600755,2.960880,2.513351,8.758561,-3.767560,-7.825885,-1.496283,5.753486,1.026697,8.332313,5.420285,-3.832943,-4.563748,6.810753,7.147696,6.625630,7.198905,-4.988391,-5.156613,0.729705,-4.196695,6.615954,-4.815608,2.792424,-5.092467,-1.961147,9.869875,-1.246854,5.590651,0.090704,3.595776,8.102466,-6.777265,-4.707567,7.370448,6.263738,9.600439,5.830614,5.924302,7.379259,1.955278,5.328028,-7.948173,-3.833143,2.555125,-6.550390,-1.713202,0.419084,-2.590897,1.482869,6.502670,6.603038,8.029826,-8.759031,5.285874,-1.732834,6.319368,-6.438986,6.648146,-8.657560,-7.106480,-7.301239,-5.948216,6.353774,7.859683,1.364899,9.134335,0.887076,6.062509,6.159154,7.110610,5.580059,9.144864,-3.253494,-2.610660,5.261566,-4.752796,6.882696,1.445854,1.384659,4.078598,3.508684,3.937483,9.522757,-0.008233,-9.302142,5.322477,9.883938,7.875644,6.075754,-5.399776,-3.901481,-8.711230,2.350572,8.743448,-8.210758,8.279905,4.005796,-4.771940,0.613230,-3.196258,-1.399296,5.366221,-0.505976,-1.033517,-1.987451,9.580689,3.322813,-7.108017,4.922752,9.808782,-1.035362,-0.503164,3.477938,0.233457,2.992228,-1.880844,1.404955,9.519801,-2.946401,3.058923,-4.419743,-4.394134,4.989373,6.237747,-1.959281,-3.577305,6.781133,-9.331514,-5.854307,-1.963833,6.537633,9.083193,-6.761963,9.736616,-3.959195,-5.641865,5.905139,-0.581280,6.468109,8.185754,-4.635602,6.284890,-1.109632,1.216822,6.208194,5.120349,-2.437382,0.423871,4.600751,-1.964336,5.004946,7.463649,3.190526,3.813152,6.107656,-1.307470,7.565370,1.269566,0.905471,-3.183455,-6.849345,-5.588779,-4.964887,-0.704534,-5.273674,-3.195074,6.108804,-5.067218,3.318993,7.879724,-8.857319,7.794820,4.912147,-3.471264,7.978623,7.800805,-3.854961,-4.202510,0.404953,-0.303572,1.936394,-5.070495,-2.329008,3.775365,-7.128821,-6.028196,-2.310721,-3.208299,8.782165,2.196149,6.308375,-6.350021,-1.528456,7.855044,3.530425,5.985339,-8.070160,6.726619,-0.919928,-0.119881,-6.122414,4.054294,-1.194467,-6.092415,-6.247217,-7.186912,9.502652,5.805080,-4.185324,4.059861,2.783567,-1.520992,-5.132588,-4.930638,3.709242,-6.870055,-8.922538,-7.137347,5.161744,-3.465795,-8.178305,-4.988258,1.928220,8.040798,-9.790123,-6.824099,9.226058,8.461346,-9.682606,-6.145759,-6.426872,9.298414,2.685683,-7.648125,3.659998,-4.690858,7.098433,8.436481,1.991920,-5.471935,4.197288,6.434938,-6.804449,2.772914,-3.565861,-4.107537,-2.262909,0.772731,0.596749,-7.320647,-6.786230,7.462093,6.243946,1.002800,8.011827,-5.448323,-1.776076,-8.103219,-0.919695,0.695374,4.089659,-5.025585,-3.765756,1.849024,0.610136,-7.658820,3.271789,5.521713,-1.353539,1.928504,3.138458,-0.043463,0.911457,-0.157239,-0.788960,-4.677108,4.435767,9.845211,3.698118,0.460107,1.537059,-0.577947,6.249181,2.677400,-2.416631,-9.434046,6.691639,3.900425,7.417917,-2.137029,-2.046431,2.197999,9.660383,3.225637,-6.953249,2.229490,-6.465293,-8.295025,-3.905551,2.453755,-2.042946,-8.496780,-6.156184,-9.214136,7.225160,-8.080812,1.029862,2.659394,-3.683712,4.199945,8.376654,-6.653561,1.577950,-2.904358,8.079110,-9.827146,9.681308,6.142220,8.729953,8.280950,-9.370601,-2.739089,9.762518,1.233082,-0.520201,-3.162021,2.731210,7.670363,6.519482,-5.343679,1.743913,-2.203929,9.754029,-5.494153,4.600025,8.673215,3.590918,-3.709249,5.882073,2.748442,-9.678375,-3.414147,-8.594717,-5.053663,4.579091,-0.302705,-8.038926,9.248034,-0.543216,-4.163143,3.412998,-6.508356,5.062468,0.552939,-1.458399,-4.439517,1.472822,-9.664402,-0.796936,1.521190,-9.907584,-0.032066,9.300146,-3.172919,6.187973,4.044002,7.266726,-5.047053,-6.546920,3.229698,-4.902015,-6.819498,-8.151539,6.275829,0.560010,-3.195303,3.763540,-8.421176,-2.727966,-9.915904,7.389566,-7.346399,2.071454,8.615961,8.928901,-0.345650,-8.565062,0.949820,-2.815246,2.992133,3.107709,8.089500,-8.468347,3.659644,-8.762476,5.321510,-5.862978,-2.348407,-8.271032,0.694160,6.528251,1.596474,-2.773624], dtype = "float64")#candidate|6379|(2912,)|const|float64
call_6376 = relay.TupleGetItem(func_3706_call(relay.reshape(const_6377.astype('float32'), [231,]), relay.reshape(const_6378.astype('int8'), [480,]), relay.reshape(const_6379.astype('float64'), [104, 28]), ), 3)
call_6380 = relay.TupleGetItem(func_3710_call(relay.reshape(const_6377.astype('float32'), [231,]), relay.reshape(const_6378.astype('int8'), [480,]), relay.reshape(const_6379.astype('float64'), [104, 28]), ), 3)
output = relay.Tuple([call_6360,call_6376,const_6377,const_6378,const_6379,])
output2 = relay.Tuple([call_6361,call_6380,const_6377,const_6378,const_6379,])
func_6382 = relay.Function([], output)
mod['func_6382'] = func_6382
mod = relay.transform.InferType()(mod)
mutated_mod['func_6382'] = func_6382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6382_call = mutated_mod.get_global_var('func_6382')
call_6383 = func_6382_call()
output = call_6383
func_6384 = relay.Function([], output)
mutated_mod['func_6384'] = func_6384
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6525 = relay.var("var_6525", dtype = "uint8", shape = (4, 8, 1))#candidate|6525|(4, 8, 1)|var|uint8
const_6526 = relay.const([[[9,-1,-9],[-5,3,9],[-6,-6,-7],[-1,-2,4],[1,3,2],[-3,-9,4],[-3,8,-6],[5,-10,-10]],[[-10,1,-5],[4,-4,3],[6,-5,-10],[-2,-1,-10],[7,-10,8],[5,10,-2],[10,10,-4],[10,-8,-4]],[[7,3,8],[4,9,-4],[3,-7,-7],[9,-8,1],[-3,-1,-7],[9,-10,-1],[-4,-4,8],[-1,1,-3]],[[8,4,-2],[-7,8,-4],[-10,-1,5],[-9,-7,-5],[-2,6,-6],[-2,3,-2],[2,8,5],[7,6,8]]], dtype = "uint8")#candidate|6526|(4, 8, 3)|const|uint8
bop_6527 = relay.add(var_6525.astype('uint8'), const_6526.astype('uint8')) # shape=(4, 8, 3)
func_5370_call = mod.get_global_var('func_5370')
func_5372_call = mutated_mod.get_global_var('func_5372')
const_6531 = relay.const([7.451693,9.924091,-6.470927,-4.005863,-0.664850,-7.452004,8.222343,9.506288,1.993378,-3.417598,6.968510,4.069465,-2.165727,8.699759,8.485104,-1.077071,-0.788697,1.651073,-1.991742,-4.147877,1.473217,-4.105238,5.462760,6.033432,0.256896,4.633706,-2.027815,-2.500142,0.555408,-8.990749,-3.567079,1.371491,-1.963423,-4.794474,-2.274174,6.166314,8.435214,-5.333551,-0.807945,-8.980771,-1.669442,-1.820845,-4.047385,1.840692,-7.519202,-7.810235,-2.439737,4.246416,3.908877,6.934005,-9.689978,3.342457,0.834654,9.155126,-2.164865,9.195393,9.883234,6.226096,2.856068,0.443308,-1.767005,-8.155504,1.077881,-4.811779,7.092352,-8.924125,-2.563907,-7.149258,-0.665878,3.614328,9.757338,9.425577,5.208358,-9.501281,8.124319,-1.272872,-5.665558,-7.588018,4.885684,-5.840058,-4.002835,-2.920175,-6.952452,-0.460230,-9.162367,9.455612,3.969102,1.402125,6.278969,7.643453,5.917445,4.955698,-1.889766,-2.778461,-4.904885,0.363758,3.175674,1.148086,-4.550850,-4.738275,-5.577644,-0.799118,-0.656693,-6.528492,7.892670,-6.888881,5.586548,-0.877870,2.483320,2.963565,0.973738,0.774681,0.756850,7.583658,-8.156444,-4.743394,9.870682,-3.907408,-5.021963,-8.974342,-1.420625,0.853974,-0.788913,-6.344957,-1.941650,3.322863,-4.306124,-3.419232,2.491120,7.017888,-0.123245,-8.967187,-7.333286,6.644554,5.904771,-1.047967,3.418217,-4.396708,-7.745367,1.538216,-1.296090,-0.936024,5.852609,-0.852524,-4.102314,1.828723,-3.430865,9.894814,-7.507734,9.385773,-7.952111,-5.565218,5.046183,6.031950,2.622330,-5.063516,6.740296,-9.623461,-6.650214,2.582291,-5.298895,0.219924,4.797239,4.741921,7.655478,3.814441,-3.634378,1.053573,-8.624620,5.529740,-2.997304,-1.429467,3.592904,-2.563852,5.511813,-9.142662,-2.771462,-9.490589,-6.018014,-5.829183,1.490567,4.539770,2.669890,5.597452,0.788373,1.120875,6.184646,5.186496,-5.297964,-1.720424,-8.190830,4.086127,-1.472254,-3.922734,8.224029,-6.652514,-5.564675,-1.116795,6.984316,-1.544665,5.742118,-4.705012,0.681641,4.656905,1.540942,7.489168,-7.688961,3.285192,8.435678,-1.992092,-8.600534,6.172986,-5.965804,-3.732907,8.699265,1.445591,-1.093959,2.513931,0.912575,3.617019,-2.757699,-0.418255,0.206777,4.895718,5.126441,4.928451,8.063040,6.868406,-9.456312,8.412089,-5.099191,-2.306216,-7.739882,-2.376400,-0.401868,-8.675097,-7.424083,-5.398824,-3.221399,-5.214693,1.663872,1.094440,-6.816199,-0.476133,-8.679534,0.427298,-5.437931,9.352497,2.445663,2.131757,6.000463,9.474913,-1.978867,9.681020,2.463788,6.784658,3.127419,9.275132,3.864564,7.032568,9.795129,-0.222243,-1.268770,-6.050312,5.320057,-4.187470,-7.084916,-8.118007,9.595201,0.873428,-1.598332,5.775396,-2.413423,7.938411,-5.210808,7.562937,7.966274,-3.358320,-1.244596,-5.653162,-7.804919,-9.313185,-8.602075,1.128132,3.139971,-2.422047,7.448191,2.228148,5.906780,9.682664,7.452251,0.725644,-4.313166,0.519146,2.282777,-8.684688,-8.630167,-6.076934,-9.936412,-7.299174,-8.814535,2.558075,-8.383433,8.549161,7.700814,0.280331,-7.159483,-5.298168,-7.988387,4.305789,8.776058,6.013314,-0.800959,-7.934371,-7.755731,-2.212024,2.266537,-5.819571,4.831243,4.838363,6.244178,0.058833,-7.361423,-0.111706,6.716829,-8.172328,-7.815260,-1.772639,5.669520,9.460848], dtype = "float64")#candidate|6531|(330,)|const|float64
call_6530 = func_5370_call(relay.reshape(const_6531.astype('float64'), [11, 5, 6]))
call_6532 = func_5370_call(relay.reshape(const_6531.astype('float64'), [11, 5, 6]))
output = relay.Tuple([bop_6527,call_6530,const_6531,])
output2 = relay.Tuple([bop_6527,call_6532,const_6531,])
func_6536 = relay.Function([var_6525,], output)
mod['func_6536'] = func_6536
mod = relay.transform.InferType()(mod)
var_6537 = relay.var("var_6537", dtype = "uint8", shape = (4, 8, 1))#candidate|6537|(4, 8, 1)|var|uint8
output = func_6536(var_6537)
func_6538 = relay.Function([var_6537], output)
mutated_mod['func_6538'] = func_6538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5645_call = mod.get_global_var('func_5645')
func_5646_call = mutated_mod.get_global_var('func_5646')
call_6554 = relay.TupleGetItem(func_5645_call(), 0)
call_6555 = relay.TupleGetItem(func_5646_call(), 0)
func_1915_call = mod.get_global_var('func_1915')
func_1916_call = mutated_mod.get_global_var('func_1916')
call_6565 = func_1915_call()
call_6566 = func_1915_call()
output = relay.Tuple([call_6554,call_6565,])
output2 = relay.Tuple([call_6555,call_6566,])
func_6568 = relay.Function([], output)
mod['func_6568'] = func_6568
mod = relay.transform.InferType()(mod)
output = func_6568()
func_6569 = relay.Function([], output)
mutated_mod['func_6569'] = func_6569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2265_call = mod.get_global_var('func_2265')
func_2266_call = mutated_mod.get_global_var('func_2266')
call_6638 = func_2265_call()
call_6639 = func_2265_call()
output = call_6638
output2 = call_6639
func_6655 = relay.Function([], output)
mod['func_6655'] = func_6655
mod = relay.transform.InferType()(mod)
mutated_mod['func_6655'] = func_6655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6655_call = mutated_mod.get_global_var('func_6655')
call_6656 = func_6655_call()
output = call_6656
func_6657 = relay.Function([], output)
mutated_mod['func_6657'] = func_6657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1991_call = mod.get_global_var('func_1991')
func_1992_call = mutated_mod.get_global_var('func_1992')
call_6663 = relay.TupleGetItem(func_1991_call(), 0)
call_6664 = relay.TupleGetItem(func_1992_call(), 0)
func_5924_call = mod.get_global_var('func_5924')
func_5926_call = mutated_mod.get_global_var('func_5926')
call_6665 = relay.TupleGetItem(func_5924_call(), 0)
call_6666 = relay.TupleGetItem(func_5926_call(), 0)
output = relay.Tuple([call_6663,call_6665,])
output2 = relay.Tuple([call_6664,call_6666,])
func_6671 = relay.Function([], output)
mod['func_6671'] = func_6671
mod = relay.transform.InferType()(mod)
output = func_6671()
func_6672 = relay.Function([], output)
mutated_mod['func_6672'] = func_6672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2534_call = mod.get_global_var('func_2534')
func_2535_call = mutated_mod.get_global_var('func_2535')
call_6691 = relay.TupleGetItem(func_2534_call(), 2)
call_6692 = relay.TupleGetItem(func_2535_call(), 2)
func_471_call = mod.get_global_var('func_471')
func_475_call = mutated_mod.get_global_var('func_475')
const_6720 = relay.const([1.211693,-6.725775,-8.293290,3.181136,2.763609,-4.022407,3.725065,-5.143940,-0.804593,9.876009,8.434397,-8.882006,-9.307378,-4.356064,7.306020,9.979119,-5.757255,-8.352046,-5.509308,-1.746829,-9.303720,9.189931,-2.957635,-8.556897,4.354163,8.062421,-0.861548,-0.764780,5.751746,4.558248,-9.501653,9.031382,-2.052578,-8.856122,9.595512,-9.838266,0.874256,3.561021,1.428177,-7.201916,2.976407,-5.806553,9.012864,-3.983460,1.591430,-6.751449,5.917140,8.033151], dtype = "float32")#candidate|6720|(48,)|const|float32
const_6721 = relay.const([True,False,True,True,True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,False,True,False,False,False,True,True,False,True,False,False,False,False,True,True,True,True,False,False,True,True,True,True,False,True,False,True,False,True,False,False,True,True,False,False,False,True,True,False,False,True,False,True,True,False,False,True,True,True,True,False,False,True,False,True,False,False,False,True,False,True,True,True,False,True,True,False,True,True,True,True,False,True,False,False,True,True,True,False,False,False,True,False,True,True,True,False,True,False,True,True,True,False,True,True,True,False,False,False,True,True,False,False,False,False,False,False,True,True,False,True,True,True,False,True,False,True,True,False,True,False,True,False,False,False,False,True,True,False,False,False,True,False,False,True,False,False,True,False,True,False,True,True,True,True,False,False,True,True,False,False,True,True,True,True,False,True,False,True,True,False,True,False,False,False,True,True,False,True,True,False,True,False,True,False,False,True,False,True,False,False,True,True,False,False,False,False,True,False,True,False,True,False,False,True,False,False,False,True,True,True,True,False,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,False,False,False,True,True,True,True,True,True,True,True,False,False,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,False,True,False,False,False,False,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,False,True,True,False,False,False,True,False,False,False,True,False,False,True,True,True,True,False,True,False,False,False,True,False,True,False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,False,False,False,False,True,True,False,False,False,False,True,True,True,False,False,False,False,False,True,True,True,True,True,True,True,True,True,False,False,True,True,False,False,False,True,True,True,True,True,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,False,True,False,True,True,True,False,False,False,True,True,False,True,False,False,True,False,False,False,True,False,False,True,True,False,False,True,True,False,False,True,False,False,True,True,True,False,True,True,False,False,True,False,True,True,False,False,True,False,False,False,False,False,True,True,True,False,False,False,False,True,True,False,True,False,True,False,False,False,True,False,False,False,False,True,False,False,True,True,False,True,False,True,True,True,False,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,True,False,True,True,True,False,False,True,True,False,False,False,True,True,True,True,False,True,True,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,True,True,True,True,True,True,False,True,False,True,True,False,False,False,False,False,True,False,False,True,True,False,True,False,False,False,True,False,True,True,True,False,False,False,True,False,False,True,True,False,True,False,False,True,False,False,False,True,False,False,False,False,False,True,False,False,False,True,True,True,False,False,True,False,False,False,False,False,True,True,True,False,True,True,False,False,False,False,True,False,False,False,False,False,True,False,False,True,True,True,False,True,True,True,False,False,True,False,False,True,False,True,True,True,True,True,True,True,True,True,True,True,True,False,True,False,False,False,False,False,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True,False,True,True,True,True,False,False,False,True,False,False,True,True,False,True,True,True,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,True,True,True,False,False,False,False,False,True,False,False,False,False,False,True,False,False,True,False,False,True,True,False,False,False,True,False,True,False,False,False,True,True,True,False,True,True,False,True,False,True,False,True,True,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,False,True,True,True,False,False,False,True,False,True,False,True,True,True,True,False,False,True,True,True,True,True,True,False,True,False,False,True,True,False,False,True,True,True,False,True,True,False,False,True,True,False,True,False,False,False,False,False,False,False,True,True,True,False,False,False,False,False,False,True,False,False,False,False,True,False,True,True,False,False,False,True,False,True,False,False,False,False,False,False,False,True,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True,False,False,True,False,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,False,False,True,True,True,False,False,True,False,True,False,False,False,False,True,True,True,True,True,True,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,True,True,True,True,True,False,False,False,True,False,True,True,True,False,False,False,False,False,False,True,True,False,False,True,False,False,True,False,True,False,False,False,False,True,True,True,False,True,True,True,False,False,False,True,False,False,True,True,False,False,False,False,False,False,True,False,False,False,False,True,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,False,True,True,True,False,True,True,True,True,True,False,True,True,True,True,False,True,False,True,False,True,False,True,True,False,False,False,False,True,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,False,False,False,True,True,False,True,False,False,False,True,True,True,True,True,False,False,False,True,False,True,False,True,False,False,False,False,True,False,True,True,False,False,True,False,True,True,True,True,False,False,False,True,True,False,False,True,False,False,False,True,False,False,False,False,False,False,False,True,False,True,False,True,True,False,True,False,True,False,True,True,False,False,False,True,False,False,False,False,True,True,True,True,True,True,True,False,False,True,True,False,False,False,True,False,False,False,False,True,True,False,True,True,False,True,True,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,False,False,True,True,False,True,False,True,True,True,True,False,False,True,True,True,True,True,True,True,False,True,True,False,True,True,True,True,False,True,True,False,False,False,False,False,False,False,True,True,True,False,True,True,True,False,True,False,False,False,False,False,True,True,True,True,False,False,False,True,False,True,True,False,False,True,False,False,True,False,True,False,False,False,False,False,False,True,False,False,True,False,True,False,False,False,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,False,False,True,False,False,True,True,True,False,True,False,False,False,True,False,False,False,True,True,False,False,True,False,True,False,True,False,True,True,False,False,True,False,True,False,True,True,True,False,True,False,True,True,True,False,False,True,False,True,False,True,True,False,True,True,False,False,True,True,True,True,True,True,True,False,True,False,True,False,True,False,False,False,False,True,False,False,True,False,True,True,True,False,True,False,True,True,True,False,False,False,True,True,True,True,False,False,True,True,False,False,False,True,False,False,False,False,False,True,True,True,True,False,True,False,True,True,False,False,True,False,False,True,False,False,False,False,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,True,False,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,True,True,True,True,True,True,False,False,False,False,False,False,False,True,True,False,False,False,True,False,False,False,False,False,True,False,False,True,False,False,False,True,False,True,False,True,False,True,True,True,True,True,True,True,False,False,False,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,False,True,True,True,True,True,False,False,False,True,False,False,False,False,False,False,True,True,False,False,False,True,True,True,False,False,False,False,True,False,False,False,True,True,True,False,True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,False,False,True,True,True,True,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,False,True,True,True,True,False,False,True,True,False,True,False,True,False,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,False,True,False,False,False,True,False,True,False,False,True,True,False,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False,True,False,False,False,False,False,True,False,True,False,False,False,False,True,True,True,False,False,False,True,True,True,False,True,False,False,False,False,True,True,False,False,True,False,False,True,False,True,True,False,True,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,True,False,False,False,True,False,False,False,False,False,True,False,True,False,False,False,True,False,True,False,True,True,False,False,True,False,True,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,False,False,False,True,True,False,False,True,True,False,True,False,False,True,False,True,True,True,True,False,True,False,True,True,False,True,True,False,False,True,False,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True,True,False,False,True,False,False,True,True,True,False,True,False,False,True,True,True,True,True,True,False,False,False,False,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,True,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,True,True,False,False,False,True,True,False,True,True,True,False,False,False,False,True,False,True,True,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,False,False,True,True,False,False,False,False,False,True,False,False,False,True,True,False,False,True,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,False,True,False,False,False,False,False,True,True,True,True,False,False,True,False,False,False,True,True,True,False,False,True,False,False,False,False,False,False,False,False,False,True,True,True,True,True,True,False,False,False,False,False,True,True,False,True,True,True,False,False,True,True,True,True,True,False,True,False,False,True,False,False,True,True,True,False,True,True,True,True,True,True,False,False,False,False,True,False,False,False,False,True,True,False,True,False,False,False,False,False,False,True,False,True,False,False,True,True,True,False,True,False,True,True,True,False,True,False,False,True,False,False,True,True,False,False,False,False,False,False,False,False,True,True,True,False,True,True,True,False,True,False,False,True,True,True,True,True,False,True,False,False,True,True,False,False,True,False,False,False,False,True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False,True,True,False,False,False,False,False,False,False,False,True,True,True,False,False,True,False,True,True,True,False,True,False,True,False,True,False,True,True,True,True,False,True,True,False,True,True,False,False,False,False,True,True,False,False,True,True,False,True,False,True,True,False,True,False,False,False,True,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,False,True,False,False,True,False,True,True,True,False,True,False,False,False,True,True,True,False,False,False,False,True,True,True,False,False,False,True,True,True,False,False,True,False,False,False,True,True,True,False,True,True,True,True,True,False,True,False,False,True,False,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,True,True,False,True,False,False,False,True,True,True,False,True,True,True,True,True,True,True,False,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,True,False,True,False,False,False,False,True,True,True,True,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,False,True,False,True,False,True,True,True,False,True,True,False,True,False,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,False,False,True,True,False,False,True,False,False,False,True,True,True,False,True,True,True,True,True,False,False,False,True,True,False,False,False,False,False,True,False,True,False,True,False,False,False,True,False,False,False,False,True,True,False,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,True,True,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,False,True,True,False,False,True,True,True,False,True,True,False,False,False,False,True,False,True,True,True,True,False,True,False,True,True,False,True,False,True,False,True,False,True,True,True,False,False,False,True,False,True,True,False,False,True,True,False,True,False,True,False,False,False,False,True,True,True,True,False,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,True,True,False,True,False,False,True,True,True,True,True,False,True,False,True,True,False,True,False,True,False,False,False,True,True,False,False,False,True,False,True,False,True,True,True,False,False,False,True,True,False,False,True,True,True,True,False,True,False,False,False,False,False,True,True,False,True,True,False,False,True,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,True,True,True,True,True,True,True,True,False,False,True,True,False,False,True,True,False,True,False,True,True,True,True,True,True,True,True,False,True,False,True,False,True,False,True,False,False,False,True,False,True,True,False,True,True,True,False,True,True,True,False,False,False,True,True,False,True,False,False,False,False,True,True,True,False,False,True,False,True,False,False,False,True,False,True,False,False,True,True,True,False,False,True,True,True,False,True,False,False,True,True,False,False,False,True,False,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False,False,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,True,False,True,True,True,False,True,False,False,False,True,True,False,False,False,False,True,False,True,False,True,False,True,True,True,False,False,False,False,True,False,True,True,True,False,False,True,True,False,False,False,False,True,False,False,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False,True,True,False,True,True,False,False,True,False,False,False,False,False,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True,True,True,False,True,False,False,False,True,False,False], dtype = "bool")#candidate|6721|(2912,)|const|bool
call_6719 = relay.TupleGetItem(func_471_call(relay.reshape(const_6720.astype('float32'), [1, 3, 16]), relay.reshape(const_6721.astype('bool'), [104, 28]), ), 0)
call_6722 = relay.TupleGetItem(func_475_call(relay.reshape(const_6720.astype('float32'), [1, 3, 16]), relay.reshape(const_6721.astype('bool'), [104, 28]), ), 0)
func_2817_call = mod.get_global_var('func_2817')
func_2818_call = mutated_mod.get_global_var('func_2818')
call_6726 = func_2817_call()
call_6727 = func_2817_call()
output = relay.Tuple([call_6691,call_6719,const_6720,const_6721,call_6726,])
output2 = relay.Tuple([call_6692,call_6722,const_6720,const_6721,call_6727,])
func_6734 = relay.Function([], output)
mod['func_6734'] = func_6734
mod = relay.transform.InferType()(mod)
output = func_6734()
func_6735 = relay.Function([], output)
mutated_mod['func_6735'] = func_6735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1991_call = mod.get_global_var('func_1991')
func_1992_call = mutated_mod.get_global_var('func_1992')
call_6778 = relay.TupleGetItem(func_1991_call(), 0)
call_6779 = relay.TupleGetItem(func_1992_call(), 0)
func_5138_call = mod.get_global_var('func_5138')
func_5139_call = mutated_mod.get_global_var('func_5139')
call_6783 = func_5138_call()
call_6784 = func_5138_call()
output = relay.Tuple([call_6778,call_6783,])
output2 = relay.Tuple([call_6779,call_6784,])
func_6788 = relay.Function([], output)
mod['func_6788'] = func_6788
mod = relay.transform.InferType()(mod)
mutated_mod['func_6788'] = func_6788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6788_call = mutated_mod.get_global_var('func_6788')
call_6789 = func_6788_call()
output = call_6789
func_6790 = relay.Function([], output)
mutated_mod['func_6790'] = func_6790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2576_call = mod.get_global_var('func_2576')
func_2577_call = mutated_mod.get_global_var('func_2577')
call_6799 = relay.TupleGetItem(func_2576_call(), 0)
call_6800 = relay.TupleGetItem(func_2577_call(), 0)
output = relay.Tuple([call_6799,])
output2 = relay.Tuple([call_6800,])
func_6802 = relay.Function([], output)
mod['func_6802'] = func_6802
mod = relay.transform.InferType()(mod)
output = func_6802()
func_6803 = relay.Function([], output)
mutated_mod['func_6803'] = func_6803
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6814 = relay.const(-6, dtype = "uint8")#candidate|6814|()|const|uint8
var_6815 = relay.var("var_6815", dtype = "uint8", shape = (1, 14, 13))#candidate|6815|(1, 14, 13)|var|uint8
bop_6816 = relay.left_shift(const_6814.astype('uint8'), var_6815.astype('uint8')) # shape=(1, 14, 13)
bop_6835 = relay.greater_equal(bop_6816.astype('bool'), const_6814.astype('bool')) # shape=(1, 14, 13)
bop_6847 = relay.not_equal(const_6814.astype('bool'), var_6815.astype('bool')) # shape=(1, 14, 13)
output = relay.Tuple([bop_6835,bop_6847,])
output2 = relay.Tuple([bop_6835,bop_6847,])
func_6853 = relay.Function([var_6815,], output)
mod['func_6853'] = func_6853
mod = relay.transform.InferType()(mod)
mutated_mod['func_6853'] = func_6853
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6854 = relay.var("var_6854", dtype = "uint8", shape = (1, 14, 13))#candidate|6854|(1, 14, 13)|var|uint8
func_6853_call = mutated_mod.get_global_var('func_6853')
call_6855 = func_6853_call(var_6854)
output = call_6855
func_6856 = relay.Function([var_6854], output)
mutated_mod['func_6856'] = func_6856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5977_call = mod.get_global_var('func_5977')
func_5979_call = mutated_mod.get_global_var('func_5979')
call_6930 = relay.TupleGetItem(func_5977_call(), 0)
call_6931 = relay.TupleGetItem(func_5979_call(), 0)
output = relay.Tuple([call_6930,])
output2 = relay.Tuple([call_6931,])
func_6948 = relay.Function([], output)
mod['func_6948'] = func_6948
mod = relay.transform.InferType()(mod)
mutated_mod['func_6948'] = func_6948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6948_call = mutated_mod.get_global_var('func_6948')
call_6949 = func_6948_call()
output = call_6949
func_6950 = relay.Function([], output)
mutated_mod['func_6950'] = func_6950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6948_call = mod.get_global_var('func_6948')
func_6950_call = mutated_mod.get_global_var('func_6950')
call_6951 = relay.TupleGetItem(func_6948_call(), 0)
call_6952 = relay.TupleGetItem(func_6950_call(), 0)
output = call_6951
output2 = call_6952
func_6976 = relay.Function([], output)
mod['func_6976'] = func_6976
mod = relay.transform.InferType()(mod)
output = func_6976()
func_6977 = relay.Function([], output)
mutated_mod['func_6977'] = func_6977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3429_call = mod.get_global_var('func_3429')
func_3431_call = mutated_mod.get_global_var('func_3431')
call_6978 = relay.TupleGetItem(func_3429_call(), 1)
call_6979 = relay.TupleGetItem(func_3431_call(), 1)
func_2125_call = mod.get_global_var('func_2125')
func_2133_call = mutated_mod.get_global_var('func_2133')
const_6985 = relay.const([-2.859264,-4.475449,-6.374278,-9.863931,9.878995,-1.654620,0.066146,0.187244,-2.683272,9.113953,-5.334892,-5.439289,9.805865,-9.334132,-0.912580,-0.597510,-3.579015,9.542074,-6.545862,3.636868,0.660224,5.927590,-2.891505,-7.527274,0.687106,-1.412791,6.524910,-1.807298,6.016785,-3.459478,9.749371,-3.244501,2.877480,-7.278754,3.099307,8.564574,-3.299049,3.451801,3.152593,0.540368,7.846537,-6.030059,-5.943864,0.890136,5.510706,0.408468,5.576539,9.408254,7.623111,-0.412217,3.915118,1.426459,-3.477868,9.822676,4.384948,0.585703], dtype = "float64")#candidate|6985|(56,)|const|float64
var_6986 = relay.var("var_6986", dtype = "float64", shape = (448,))#candidate|6986|(448,)|var|float64
var_6987 = relay.var("var_6987", dtype = "int32", shape = (168, 4))#candidate|6987|(168, 4)|var|int32
var_6988 = relay.var("var_6988", dtype = "float32", shape = (48,))#candidate|6988|(48,)|var|float32
var_6989 = relay.var("var_6989", dtype = "bool", shape = (2912,))#candidate|6989|(2912,)|var|bool
var_6990 = relay.var("var_6990", dtype = "uint32", shape = (1800,))#candidate|6990|(1800,)|var|uint32
call_6984 = relay.TupleGetItem(func_2125_call(relay.reshape(const_6985.astype('float64'), [7, 8, 1]), relay.reshape(var_6986.astype('float64'), [7, 8, 8]), relay.reshape(var_6987.astype('int32'), [672,]), relay.reshape(var_6988.astype('float32'), [48,]), relay.reshape(var_6989.astype('bool'), [2912,]), relay.reshape(var_6990.astype('uint32'), [1800,]), ), 6)
call_6991 = relay.TupleGetItem(func_2133_call(relay.reshape(const_6985.astype('float64'), [7, 8, 1]), relay.reshape(var_6986.astype('float64'), [7, 8, 8]), relay.reshape(var_6987.astype('int32'), [672,]), relay.reshape(var_6988.astype('float32'), [48,]), relay.reshape(var_6989.astype('bool'), [2912,]), relay.reshape(var_6990.astype('uint32'), [1800,]), ), 6)
var_6999 = relay.var("var_6999", dtype = "uint32", shape = (1800,))#candidate|6999|(1800,)|var|uint32
bop_7000 = relay.mod(var_6990.astype('float32'), relay.reshape(var_6999.astype('float32'), relay.shape_of(var_6990))) # shape=(1800,)
output = relay.Tuple([call_6978,call_6984,const_6985,var_6986,var_6987,var_6988,var_6989,bop_7000,])
output2 = relay.Tuple([call_6979,call_6991,const_6985,var_6986,var_6987,var_6988,var_6989,bop_7000,])
func_7008 = relay.Function([var_6986,var_6987,var_6988,var_6989,var_6990,var_6999,], output)
mod['func_7008'] = func_7008
mod = relay.transform.InferType()(mod)
mutated_mod['func_7008'] = func_7008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7008_call = mutated_mod.get_global_var('func_7008')
var_7010 = relay.var("var_7010", dtype = "float64", shape = (448,))#candidate|7010|(448,)|var|float64
var_7011 = relay.var("var_7011", dtype = "int32", shape = (168, 4))#candidate|7011|(168, 4)|var|int32
var_7012 = relay.var("var_7012", dtype = "float32", shape = (48,))#candidate|7012|(48,)|var|float32
var_7013 = relay.var("var_7013", dtype = "bool", shape = (2912,))#candidate|7013|(2912,)|var|bool
var_7014 = relay.var("var_7014", dtype = "uint32", shape = (1800,))#candidate|7014|(1800,)|var|uint32
var_7015 = relay.var("var_7015", dtype = "uint32", shape = (1800,))#candidate|7015|(1800,)|var|uint32
call_7009 = func_7008_call(var_7010,var_7011,var_7012,var_7013,var_7014,var_7015,)
output = call_7009
func_7016 = relay.Function([var_7010,var_7011,var_7012,var_7013,var_7014,var_7015,], output)
mutated_mod['func_7016'] = func_7016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4702_call = mod.get_global_var('func_4702')
func_4704_call = mutated_mod.get_global_var('func_4704')
call_7047 = relay.TupleGetItem(func_4702_call(), 0)
call_7048 = relay.TupleGetItem(func_4704_call(), 0)
output = call_7047
output2 = call_7048
func_7069 = relay.Function([], output)
mod['func_7069'] = func_7069
mod = relay.transform.InferType()(mod)
mutated_mod['func_7069'] = func_7069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7069_call = mutated_mod.get_global_var('func_7069')
call_7070 = func_7069_call()
output = call_7070
func_7071 = relay.Function([], output)
mutated_mod['func_7071'] = func_7071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3480_call = mod.get_global_var('func_3480')
func_3482_call = mutated_mod.get_global_var('func_3482')
call_7072 = relay.TupleGetItem(func_3480_call(), 1)
call_7073 = relay.TupleGetItem(func_3482_call(), 1)
func_1991_call = mod.get_global_var('func_1991')
func_1992_call = mutated_mod.get_global_var('func_1992')
call_7074 = relay.TupleGetItem(func_1991_call(), 1)
call_7075 = relay.TupleGetItem(func_1992_call(), 1)
output = relay.Tuple([call_7072,call_7074,])
output2 = relay.Tuple([call_7073,call_7075,])
func_7076 = relay.Function([], output)
mod['func_7076'] = func_7076
mod = relay.transform.InferType()(mod)
output = func_7076()
func_7077 = relay.Function([], output)
mutated_mod['func_7077'] = func_7077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1811_call = mod.get_global_var('func_1811')
func_1813_call = mutated_mod.get_global_var('func_1813')
call_7103 = relay.TupleGetItem(func_1811_call(), 0)
call_7104 = relay.TupleGetItem(func_1813_call(), 0)
func_3336_call = mod.get_global_var('func_3336')
func_3338_call = mutated_mod.get_global_var('func_3338')
call_7107 = relay.TupleGetItem(func_3336_call(relay.reshape(call_7103.astype('float64'), [4, 15, 15])), 1)
call_7108 = relay.TupleGetItem(func_3338_call(relay.reshape(call_7103.astype('float64'), [4, 15, 15])), 1)
output = relay.Tuple([call_7103,call_7107,])
output2 = relay.Tuple([call_7104,call_7108,])
func_7110 = relay.Function([], output)
mod['func_7110'] = func_7110
mod = relay.transform.InferType()(mod)
output = func_7110()
func_7111 = relay.Function([], output)
mutated_mod['func_7111'] = func_7111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6099_call = mod.get_global_var('func_6099')
func_6100_call = mutated_mod.get_global_var('func_6100')
call_7142 = func_6099_call()
call_7143 = func_6099_call()
output = call_7142
output2 = call_7143
func_7149 = relay.Function([], output)
mod['func_7149'] = func_7149
mod = relay.transform.InferType()(mod)
mutated_mod['func_7149'] = func_7149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7149_call = mutated_mod.get_global_var('func_7149')
call_7150 = func_7149_call()
output = call_7150
func_7151 = relay.Function([], output)
mutated_mod['func_7151'] = func_7151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7076_call = mod.get_global_var('func_7076')
func_7077_call = mutated_mod.get_global_var('func_7077')
call_7169 = relay.TupleGetItem(func_7076_call(), 1)
call_7170 = relay.TupleGetItem(func_7077_call(), 1)
output = relay.Tuple([call_7169,])
output2 = relay.Tuple([call_7170,])
func_7182 = relay.Function([], output)
mod['func_7182'] = func_7182
mod = relay.transform.InferType()(mod)
output = func_7182()
func_7183 = relay.Function([], output)
mutated_mod['func_7183'] = func_7183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3429_call = mod.get_global_var('func_3429')
func_3431_call = mutated_mod.get_global_var('func_3431')
call_7194 = relay.TupleGetItem(func_3429_call(), 0)
call_7195 = relay.TupleGetItem(func_3431_call(), 0)
func_3852_call = mod.get_global_var('func_3852')
func_3853_call = mutated_mod.get_global_var('func_3853')
call_7238 = relay.TupleGetItem(func_3852_call(), 0)
call_7239 = relay.TupleGetItem(func_3853_call(), 0)
func_471_call = mod.get_global_var('func_471')
func_475_call = mutated_mod.get_global_var('func_475')
var_7242 = relay.var("var_7242", dtype = "float32", shape = (4, 12))#candidate|7242|(4, 12)|var|float32
var_7243 = relay.var("var_7243", dtype = "bool", shape = (2912,))#candidate|7243|(2912,)|var|bool
call_7241 = relay.TupleGetItem(func_471_call(relay.reshape(var_7242.astype('float32'), [1, 3, 16]), relay.reshape(var_7243.astype('bool'), [104, 28]), ), 1)
call_7244 = relay.TupleGetItem(func_475_call(relay.reshape(var_7242.astype('float32'), [1, 3, 16]), relay.reshape(var_7243.astype('bool'), [104, 28]), ), 1)
func_2376_call = mod.get_global_var('func_2376')
func_2378_call = mutated_mod.get_global_var('func_2378')
call_7249 = relay.TupleGetItem(func_2376_call(), 0)
call_7250 = relay.TupleGetItem(func_2378_call(), 0)
func_3852_call = mod.get_global_var('func_3852')
func_3853_call = mutated_mod.get_global_var('func_3853')
call_7255 = relay.TupleGetItem(func_3852_call(), 0)
call_7256 = relay.TupleGetItem(func_3853_call(), 0)
output = relay.Tuple([call_7194,call_7238,call_7241,var_7242,var_7243,call_7249,call_7255,])
output2 = relay.Tuple([call_7195,call_7239,call_7244,var_7242,var_7243,call_7250,call_7256,])
func_7260 = relay.Function([var_7242,var_7243,], output)
mod['func_7260'] = func_7260
mod = relay.transform.InferType()(mod)
var_7261 = relay.var("var_7261", dtype = "float32", shape = (4, 12))#candidate|7261|(4, 12)|var|float32
var_7262 = relay.var("var_7262", dtype = "bool", shape = (2912,))#candidate|7262|(2912,)|var|bool
output = func_7260(var_7261,var_7262,)
func_7263 = relay.Function([var_7261,var_7262,], output)
mutated_mod['func_7263'] = func_7263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4918_call = mod.get_global_var('func_4918')
func_4920_call = mutated_mod.get_global_var('func_4920')
call_7265 = relay.TupleGetItem(func_4918_call(), 0)
call_7266 = relay.TupleGetItem(func_4920_call(), 0)
output = relay.Tuple([call_7265,])
output2 = relay.Tuple([call_7266,])
func_7269 = relay.Function([], output)
mod['func_7269'] = func_7269
mod = relay.transform.InferType()(mod)
mutated_mod['func_7269'] = func_7269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7269_call = mutated_mod.get_global_var('func_7269')
call_7270 = func_7269_call()
output = call_7270
func_7271 = relay.Function([], output)
mutated_mod['func_7271'] = func_7271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6948_call = mod.get_global_var('func_6948')
func_6950_call = mutated_mod.get_global_var('func_6950')
call_7282 = relay.TupleGetItem(func_6948_call(), 0)
call_7283 = relay.TupleGetItem(func_6950_call(), 0)
output = call_7282
output2 = call_7283
func_7288 = relay.Function([], output)
mod['func_7288'] = func_7288
mod = relay.transform.InferType()(mod)
output = func_7288()
func_7289 = relay.Function([], output)
mutated_mod['func_7289'] = func_7289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6734_call = mod.get_global_var('func_6734')
func_6735_call = mutated_mod.get_global_var('func_6735')
call_7307 = relay.TupleGetItem(func_6734_call(), 4)
call_7308 = relay.TupleGetItem(func_6735_call(), 4)
output = relay.Tuple([call_7307,])
output2 = relay.Tuple([call_7308,])
func_7314 = relay.Function([], output)
mod['func_7314'] = func_7314
mod = relay.transform.InferType()(mod)
output = func_7314()
func_7315 = relay.Function([], output)
mutated_mod['func_7315'] = func_7315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1991_call = mod.get_global_var('func_1991')
func_1992_call = mutated_mod.get_global_var('func_1992')
call_7324 = relay.TupleGetItem(func_1991_call(), 1)
call_7325 = relay.TupleGetItem(func_1992_call(), 1)
func_740_call = mod.get_global_var('func_740')
func_743_call = mutated_mod.get_global_var('func_743')
const_7346 = relay.const([[False,True,False,False,False,False,True,False,True,True,True,True,False,False,True,True,True,False,True,False,True,False,True,False,True,False,False,False,False,False,False,False,True,True,True,True,True,False,True,True,True,False,False,True,False,False,True,False,False,False,False,True,False,True,True,True,True,False,True,True,False,False,False,True,True,True,False,False,True,True,True,False,True,False,True,False,False,False,False,False,False,False,False,False,True,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,True,False,True,True,False,True,True,False,True,True,False,False,True,False,False,False,False,False,False,True,True,True,True,False,True,True,False,True,False,False,True,True,False,False,False,False,True,True,False,True,False,True,True,True,True,True,True,True,True,True,True,False,True,False,False,False,True,False,True,True,True,False,True,True,True,True,False,False,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,True,True,False,True,True,True,False,False,False,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,True,True,True,True,True,True,False,True,True,False,False,False,True,False,False,True,True,False,True,False,False,False,True,True,False,False,False,False,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,False,True,True,True,True,True,True,True,False,True,False,True,True,False,True,True,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,False,True,False,False,False,True,True,True,True,False,True,True,True,True,False,False,True,False,True,False,False,True,False,True,False,False,False,True,False,False,False,True,True,False,True,False,True,False,True,True,False,True,False,True,False,False,True,False,False,False,False,True,True,False,False,True,True,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,True,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,True,False,False,False,False,True,True,True,False,False,True,True,True,False,True,False,True,True,False,True,False,True,False,False,False,True,True,True,False,True,True,True,True,True,True,True,True,False,True,True,False,False,False,True,False,False,False,False,True,False,True,True,False,True,True,False,False,False,True,False,True,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False,False,True,True,True,True,False,True,False,False,False,False,False,True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,True,False,False,True,True,True,True,False,True,True,True,True,True,True,False,True,False,True,True,False,False,False,True,True,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,True,False,False,True,True,True,True,True,False,False,False,False,False,False,True,False,True,False,True,True,False,True,False,False,True,True,False,True,True,False,False,True,False,True,False,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,True,True,True,True,False,True,False,True,True,False,False,False,True,False,False,False,True,True,False,False,False,True,False,True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False,True,False,True,False,True,False,True,False,True,True,False,False,False,True,True,True,True,False,True,False,False,False,True,False,False,True,True,True,False,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,False,False,True,True,True,True,True,True,True,True,False,False,False,True,True,False,True,True,True,False,False,False,True,True,True,True,True,True,False,False,True,True,True,True,False,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,True,True,True,True,False,False,True,True,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,True,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,True,False,False,False,False,False,True,False,False,False,False,False,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,False,False,True,False,True,True,False,True,True,False,False,True,False,False,True,True,False,False,False,True,True,False,True,False,True,False,True,False,True,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,True,False,False,True,True,True,False,False,True,True,False,True,False,False,False,False,True,True,False,True,False,False,False,True,False,False,False,False,False,True,False,True,True,False,False,False,True,False,False,True,False,True,False,False,True,False,False,False,True,False,True,False,True,False,True,True,False,True,True,False,False,False,True,False,False,True,False,False,False,True,True,False,False,True,False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False,True,True,False,False,True,True,True,True,True,True,False,False,True,False,True,True,True,False,False,True,False,True,False,True,True,True,False,False,False,True,False,True,False,True,True,True,False,False,False,True,False,True,True,True,True,False,True,True,False,True,False,False,False,False,True,True,True,False,True,True,True,True,False,True,False,True,False,False,True,False,True,True,True,False,True,True,False,False,False,False,True,False,True,True,False,False,False,True,False,True,False,True,False,False,False,True,True,False,True,False,True,True,False,False,True,True,True,False,True,True,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,False,True,True,True,True,False,False,False,False,False,True,True,False,True,False,True,False,False,True,True,True,False,True,False,True,False,False,True,False,False,False,False,False,True,True,True,True,True,True,True,False,False,False,False,False,False,True,False,False,False,True,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,False,False,False,False,False,False,False,False,False,True,False,False,True,False,False,True,True,True,False,True,False,False,True,True,False,False,False,False,True,True,True,False,False,True,False,False,True,False,True,False,True,True,False,True,True,False,False,True,True,False,False,True,False,True,False,False,False,True,False,True,False,True,True,False,False,True,True,False,False,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,True,False,False,False,False,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,False,True,False,False,True,False,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,False,False,False,True,True,True,False,True,False,False,False,True,False,True,False,True,True,False,False,True,True,False,True,False,True,False,True,True,False,False,True,True,False,False,False,True,True,False,True,False,False,True,True,True,False,True,False,True,False,False,False,True,True,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,False,False,True,False,True,True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,True,True,True,False,False,False,False,False,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,False,True,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,True,False,True,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,True,False,False,False,True,False,False,False,True,False,False,False,True,True,True,False,False,False,True,True,False,True,True,False,True,True,True,True,False,True,True,True,False,True,True,True,True,True,True,True,True,True,True,False,False,False,True,False,False,False,False,True,False,True,True,True,False,False,False,False,False,True,True,False,False,False,True,False,True,False,True,True,False,False,True,False,True,False,True,True,True,True,False,True,False,True,False,True,False,False,True,False,False,True,False,False,True,True,False,True,True,True,False,True,False,True,False,True,False,True,False,True,False,True,False,False,False,False,True,False,False,True,False,False,False,False,True,True,True,True,False,True,True,False,False,True,False,False,False,False,True,False,True,True,True,True,False,False,True,True,False,True,False,True,False,False,True,True,False,True,False,False,False,True,True,False,False,True,True,False,True,False,True,False,False,False,True,False,False,False,True,True,True,False,False,True,False,True,False,False,False,True,True,False,False,False,True,True,True,False,True,False,False,False,False,False,True,True,False,True,True,False,False,False,False,False,False,False,False,False,True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,True,True,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,False,False,False,True,True,True,True,True,True,True,True,False,True,False,True,True,False,True,False,True,False,True,False,False,False,False,False,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,False,True,True,True,False,True,False,False,False,True,False,False,True,False,False,True,False,False,False,True,False,False,False,True,True,True,True,True,True,True,False,True,True,True,False,True,False,True,False,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,True,False,True,True,False,False,False,False,True,True,False,False,True,False,True,True,True,True,True,True,False,True,False,False,True,False,False,True,True,True,False,False,False,True,True,False,False,False,False,True,True,False,True,False,True,False,True,False,True,False,True,True,True,True,True,True,False,False,False,True,True,False,True,True,False,True,True,False,True,False,True,False,False,True,True,True,True,False,True,True,True,True,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,False,True,False,False,True,True,True,False,False,False,True,False,True,False,True,False,False,True,False,False,False,False,False,True,True,False,False,False,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,False,False,False,False,True,True,False,True,True,False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,True,True,True,False,False,True,True,False,False,True,False,False,False,False,True,False,True,True,False,False,True,True,False,True,False,True,True,False,True,False,True,False,False,False,False,False,False,False,False,False,True,False,True,True,True,False,True,False,False,True,True,True,False,True,False,False,False,True,True,True,True,False,True,True,True,False,False,True,False,False,True,True,True,False,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,True,True,False,True,True,False,False,True,False,True,True,False,True,False,True,True,False,True,False,True,False,True,False,True,True,False,False,True,False,False,False,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,True,True,False,True,False,False,True,True,False,False,True,False,False,True,False,False,False,False,True,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,False,True,True,True,False,True,True,True,True,True,False,True,False,False,False,True,False,True,False,False,True,True,False,True,False,True,True,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False,True,True,False,False,True,False,True,True,True,False,False,True,False,True,True,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False,True,False,False,False,False,True,False,False,False,False,True,False,True,False,False,False,False,False,True,True,True,False,True,True,False,False,True,True,False,False,True,True,False,False,True,False,True,True,True,False,False,False,False,True,False,True,False,False,True,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,False,False,True,True,True,False,True,True,True,False,True,True,True,True,False,False,False,False,False,False,True,True,True,False,True,False,False,True,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,False,True,True,False,False,True,False,False,False,True,True,False,False,True,False,True,True,True,False,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,True,True,True,True,True,True,False,False,True,False,False,False,True,True,True,True,True,False,True,False,False,False,False,True,False,True,False,True,False,True,True,True,False,False,False,True,True,False,False,False,False,False,False,True,True,True,True,False,False,False,False,False,False,False,True,False,True,True,True,True,True,False,False,True,False,False,True,True,False,True,False,False,True,False,False,False,False,True,True,False,True,True,False,False,False,True,False,True,False,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,True,False,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,False,True,True,True,True,True,False,True,False,False,False,False,True,True,False,False,True,False,True,True,True,False,False,False,False,False,False,True,False,False,True,True,True,False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,False,False,True,True,False,False,True,True,True,False,True,False,True,True,False,False,False,True,False,False,False,True,False,False,True,True,True,True,True,False,True,True,False,False,False,False,True,False,False,False,False,True,True,True,False,True,True,False,False,False,False,False,True,True,True,False,False,False,False,True,True,True,True,True,True,True,False,False,True,False,True,False,True,False,True,False,True,True,False,True,True,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True,False,False,False,False,False,True,False,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,True,False,False,True,False,False,False,False,True,True,False,True,True,False,False,True,False,True,False,True,True,True,True,True,False,False,False,False,True,True,True,True,True,True,False,True,True,True,False,True,False,False,False,True,True,True,False,True,False,False,False,False,True,False,True,False,False,True,False,False,False,False,True,True,True,True,True,True,False,True,False,False,True,False,True,False,True,True,True,False,False,False,False,True,False,True,True,False,False,False,False,True,False,True,False,True,True,True,False,True,False,False,False,False,True,True,False,False,True,False,False,True,False,False,False,False,True,False,False,False,False,True,True,False,False,True,True,True,True,False,True,True,False,True,True,True,False,False,False,True,False,False,False,False,True,True,False,False,True,False,False]], dtype = "bool")#candidate|7346|(1, 2912)|const|bool
var_7347 = relay.var("var_7347", dtype = "uint32", shape = (1800,))#candidate|7347|(1800,)|var|uint32
call_7345 = relay.TupleGetItem(func_740_call(relay.reshape(const_7346.astype('bool'), [2912,]), relay.reshape(var_7347.astype('uint32'), [1800,]), ), 9)
call_7348 = relay.TupleGetItem(func_743_call(relay.reshape(const_7346.astype('bool'), [2912,]), relay.reshape(var_7347.astype('uint32'), [1800,]), ), 9)
uop_7349 = relay.atan(const_7346.astype('float32')) # shape=(1, 2912)
bop_7354 = relay.subtract(uop_7349.astype('uint32'), relay.reshape(const_7346.astype('uint32'), relay.shape_of(uop_7349))) # shape=(1, 2912)
bop_7363 = relay.bitwise_xor(const_7346.astype('int32'), relay.reshape(uop_7349.astype('int32'), relay.shape_of(const_7346))) # shape=(1, 2912)
bop_7373 = relay.not_equal(const_7346.astype('bool'), relay.reshape(uop_7349.astype('bool'), relay.shape_of(const_7346))) # shape=(1, 2912)
const_7376 = relay.const([[-2,-5,-4,-2,-9,7,4,-5,-3,8,2,-7,6,8,3,-8,-1,-7,-3,5,1,1,1,-2,5,-10,8,1,-3,-1,-7,5,-3,4,-1,-9,-10,6,6,-6,10,7,-3,-1,7,7,3,3,-4,2,-5,8,3,9,-1,-10,2,8,-6,-4,-3,7,4,-1,-7,2,6,-7,3,8,-2,-7,-6,10,6,-4,-6,4,-3,8,10,1,-1,4,-4,-2,-1,-1,-5,-6,6,9,-5,3,8,5,3,-3,-4,-8,9,5,10,4,6,6,4,-3,6,6,-7,-1,8,-5,-1,1,5,-10,1,-10,-8,8,-10,10,8,2,-6,8,-7,6,-7,7,-4,-7,-3,-3,-3,-2,5,1,-9,-1,-5,8,-1,7,-3,10,-3,4,3,-6,10,9,1,9,2,6,-8,-9,-1,4,1,1,2,10,3,-2,-6,-8,-3,-9,-6,4,9,10,-10,-2,-10,-4,8,-8,2,4,4,-4,-7,-6,8,-7,-3,-5,-3,3,1,8,3,-10,7,-10,-6,-10,9,-7,5,-4,-1,9,-7,9,-10,-9,4,-8,5,-4,4,3,-9,10,2,-2,4,-9,6,3,7,-10,3,-2,6,9,-9,5,1,-1,1,10,-7,-8,-8,-10,3,4,8,6,1,5,-8,-7,8,-5,-5,6,-1,6,5,4,6,8,5,7,9,-7,2,7,-4,-9,-5,-1,-9,-8,3,-6,2,-10,-10,-7,6,-6,-8,8,-5,-2,-2,-9,-2,-9,8,1,-1,-9,7,-10,7,-3,10,10,-10,6,-5,-7,9,-1,3,-9,4,-7,-3,6,-6,-7,-2,-2,9,-6,-10,-3,-9,9,6,-8,5,1,-4,-8,-8,7,-3,-4,-6,7,3,8,-4,-6,3,9,1,6,7,-8,-8,-6,-3,-3,1,6,2,8,10,-4,-7,-3,-5,4,10,8,6,-10,4,-9,-5,-9,-10,3,-10,-5,4,-5,-4,10,2,5,-1,8,-10,2,-1,-4,-9,-1,6,4,-1,-8,10,10,-7,10,1,5,5,5,-8,7,6,6,3,3,-1,-10,10,-2,6,-4,10,-6,-9,-10,-2,6,-4,-1,2,-10,6,3,9,-2,9,-2,9,5,9,-5,-2,-8,-3,5,4,10,5,-5,-1,9,-4,1,9,1,9,8,9,10,-6,9,10,9,3,10,-2,3,2,-1,-8,-8,8,-2,5,-1,9,-10,-9,4,4,5,-7,-1,-2,9,-3,-1,-6,-10,-7,1,-10,4,-9,-1,-6,-8,-7,-1,1,3,10,7,-8,-6,-1,-10,-7,2,5,-10,2,-4,-7,7,7,-2,-3,3,-9,6,-6,-10,-1,1,-6,8,7,4,-7,1,-3,2,-3,7,6,1,10,-6,-4,8,6,-5,-6,-8,-3,6,4,-10,-3,-1,10,2,5,-10,3,-8,-2,3,-3,-10,9,-10,5,2,-9,-8,6,1,-8,-8,-9,-1,9,-10,4,-9,-9,6,3,4,2,2,-4,7,6,-2,-4,-7,-4,7,8,-10,7,10,7,-3,-6,7,10,1,-3,-2,-5,-10,-7,-8,5,1,-6,-3,5,-2,-10,2,-4,5,-5,4,5,8,3,6,-3,-1,10,-4,9,-9,-6,1,1,7,5,5,-7,4,10,-7,9,-4,1,5,5,-1,4,-2,9,2,-3,6,1,-10,-9,3,-5,10,-4,-8,-10,1,2,-10,3,5,-10,-5,-10,-1,-2,-1,-1,2,6,6,8,10,1,1,4,1,8,7,3,-8,-4,1,-10,3,-5,-3,-8,-5,5,-4,-3,-4,-3,10,1,-2,-7,-10,-7,4,-4,5,10,-3,-5,5,-4,-10,10,-4,7,5,10,-2,10,1,5,-8,-5,9,9,-9,-2,9,-8,-4,10,9,-7,-1,1,1,-7,8,-1,3,2,3,2,10,7,-4,-3,9,6,-7,1,10,8,-9,8,8,-7,-5,-3,6,1,6,-3,-4,-6,-5,-10,4,-6,8,6,-3,9,1,-7,1,-9,1,-4,2,-7,-7,-5,-6,4,4,-4,-5,8,-4,-5,10,3,-7,-6,7,9,2,-4,4,4,8,-4,10,8,-7,-8,6,-8,-10,-3,10,2,-3,-2,-2,4,6,-4,-2,-10,-7,5,2,8,10,1,-3,-1,9,5,2,3,9,-6,-4,-7,-5,-6,-6,10,-8,-5,4,-7,-3,-6,4,-5,-9,-2,-7,3,1,-10,-4,4,-3,-2,9,2,4,9,7,10,4,8,1,5,1,-1,-8,-8,8,-10,1,-10,-9,-4,-2,-2,-6,-2,-2,-9,2,9,-8,3,-6,2,-4,-6,-1,9,5,-4,2,8,-10,-8,-8,4,-3,-10,9,-8,-6,10,-7,3,-2,2,2,7,-8,6,-1,10,7,-3,-5,3,-9,9,2,7,8,8,-1,1,2,-5,-8,-7,8,5,-4,5,1,-7,-7,-7,-4,-4,-9,-6,2,2,-8,-9,10,10,-2,5,-10,-6,-7,-1,-7,-7,1,7,-5,-7,9,-9,-2,3,3,-9,10,-9,10,9,-8,4,-2,-5,10,-1,-8,8,-9,-3,-8,-5,-10,5,-8,-9,-1,-6,-4,1,2,2,2,9,-10,-2,-9,-5,3,10,6,-8,10,1,4,7,4,6,-9,7,-1,8,-8,-8,-4,-2,8,9,-3,-4,-2,1,-10,4,-3,-9,-10,2,-1,-8,-9,-7,-10,4,7,-10,-9,-7,-9,-8,-1,-5,-7,8,-9,3,5,-4,-6,-8,-8,-2,-9,-6,1,1,3,3,-6,8,-7,3,2,-9,-8,3,-5,-3,-5,5,2,-10,-3,-7,-3,-4,7,-4,-7,-9,-10,-2,-9,-1,3,10,3,2,-2,5,-5,8,8,-3,5,-1,4,9,-10,8,6,1,-10,7,4,-9,-3,-3,1,8,-7,8,-4,-5,-7,10,-2,5,5,-6,-4,-10,-4,-7,-6,-10,6,4,-4,6,3,7,6,9,-3,-10,10,3,-10,8,9,-1,-5,-7,-6,-4,-9,-6,2,6,-2,4,4,-7,-10,-2,-2,-4,-8,10,3,2,-5,-9,-6,4,-9,2,-6,2,6,4,7,-7,-8,10,10,-5,2,2,9,8,4,3,-10,7,9,4,-1,4,7,-3,5,2,4,-5,-3,10,4,-9,-8,-10,10,-6,6,-10,-1,-2,3,-4,-1,9,-2,1,-2,-10,-7,-9,6,-7,5,-5,-2,-3,-2,-3,3,-5,3,-3,-8,-7,-5,1,-4,-4,-8,3,6,5,10,1,2,-10,-3,9,-6,-6,5,-4,8,5,-7,-3,4,-2,-8,10,10,6,-5,-5,-1,3,10,4,3,3,-8,4,-6,8,1,5,-2,-7,6,-9,4,-5,-9,-2,10,4,-4,2,5,6,-2,7,4,10,-5,8,-10,4,4,2,3,-2,6,-9,-3,-7,5,-8,8,-8,-6,-2,1,-6,4,-9,-5,6,-4,-4,-9,4,5,-5,-10,5,9,-2,5,-5,7,-8,4,6,10,-7,-1,6,-4,10,-4,-2,4,5,-4,-8,6,-7,-1,-10,-5,3,9,3,-10,7,-9,9,3,-3,-8,-9,-9,9,-9,5,8,-9,5,2,4,1,8,-7,6,9,-2,-10,-7,5,8,10,-7,-4,-3,-10,-6,10,-1,-5,8,-10,-6,-5,7,-9,-9,-10,-9,9,-1,-1,-9,10,-10,6,-1,-2,7,10,-7,-1,-7,3,7,10,-10,-4,-3,-9,-9,3,-9,9,-2,2,-5,6,-3,-1,-2,8,-3,-10,-7,1,4,-6,-1,-1,-3,4,5,1,10,10,-5,3,1,6,2,3,-3,9,5,9,-2,-7,3,-4,-2,-5,3,6,-1,3,10,-1,9,9,1,-4,-8,-9,1,-4,-10,-3,-6,8,-1,-3,8,-6,-6,-3,-2,2,-9,1,-6,6,-5,-8,6,-8,-6,-10,9,-3,10,3,-4,1,6,5,8,-8,10,4,10,5,-5,10,10,8,-9,1,6,7,4,5,-5,5,-7,-1,10,-2,-2,10,10,-1,9,-2,-4,8,-3,9,6,-3,-10,-9,-2,-7,7,-6,5,6,1,-10,9,4,3,-3,-7,1,3,-10,-2,9,4,6,5,3,10,-1,-5,4,-8,6,-3,3,-8,-3,1,2,9,3,8,2,-3,-10,7,8,-2,3,3,1,10,-4,6,-4,-1,-1,-7,10,5,10,-5,1,5,3,9,-1,-10,10,10,2,-5,2,-5,3,4,6,-2,-9,9,4,9,-9,-10,-6,-6,-2,3,-4,8,-2,1,-6,-3,9,-10,-3,8,-8,2,-7,-4,9,2,-8,1,7,-8,-4,-9,-4,-5,7,-9,-2,-1,-1,-7,-4,6,-3,4,8,2,-2,4,-7,-4,-4,9,6,-4,-7,-9,-4,-5,-9,-5,-10,8,8,-9,-3,-1,-8,3,-2,-2,10,4,-6,8,-7,-4,-2,10,-6,-8,1,-6,-10,4,-5,-3,-8,6,-5,9,1,-10,6,4,-10,-1,-2,2,5,3,2,5,-4,-6,-9,-2,10,3,3,-8,-10,4,5,3,1,1,4,5,-9,9,-8,6,5,4,9,-3,-10,-10,-4,-8,-10,10,5,4,-6,1,5,2,9,2,-7,-8,1,-5,-2,9,9,8,5,-7,-6,-7,-8,-5,-4,-6,9,1,3,-6,-8,-6,6,-3,7,-4,-10,8,-9,-8,7,7,9,7,-3,-6,-9,7,8,8,2,2,2,-2,2,-7,6,-4,-1,5,-7,-4,5,4,3,-1,-2,9,-3,-7,2,4,8,-3,3,3,-8,6,8,7,10,8,-2,-7,9,2,2,9,5,8,-9,6,6,1,2,5,9,-5,10,8,10,1,7,1,-2,-10,10,8,-9,-9,-10,-2,-10,10,3,-1,9,4,-2,7,-3,-4,-4,8,3,4,-6,2,5,7,-1,2,10,5,-10,5,9,6,-2,-7,-4,10,-9,-5,6,4,-10,-7,-10,-2,5,6,7,-7,10,7,7,3,2,10,-2,5,-1,-4,-3,3,-4,-1,-5,-1,6,-7,5,-9,-2,5,5,9,10,-7,10,2,3,6,-4,10,-2,5,1,-4,-2,8,-7,-3,10,2,2,-3,-9,-2,5,5,1,7,-3,-6,10,-2,10,-7,-5,-10,5,5,-4,9,1,7,3,5,-6,8,-4,6,6,-2,-2,-2,-6,1,4,-9,3,6,-1,9,-3,-5,9,-8,-3,-8,3,-2,-8,8,4,-6,5,-10,-4,-4,-7,-3,8,-1,-4,-6,2,-5,-4,2,-2,4,2,-4,4,-3,-4,-7,-10,5,-1,8,-10,4,9,3,-4,-1,-10,5,2,5,6,10,2,7,-6,-9,-1,-2,10,-4,-2,-3,9,-6,-5,8,-5,-7,-2,2,-1,-6,-3,5,-4,8,-5,8,-8,-6,7,6,2,9,-10,-4,2,-5,8,8,10,-8,8,10,10,9,-2,7,8,8,9,-9,1,7,6,9,-3,1,-1,-7,9,-8,3,-4,3,1,5,-4,5,-4,-9,7,2,-5,-2,-5,10,-1,9,6,-9,-6,8,-1,-1,6,-9,-2,-2,3,-9,7,2,-4,5,-4,8,1,10,-1,-8,-1,-9,-10,-1,-6,-1,-10,3,3,8,4,-7,-4,-10,10,-9,7,-5,10,9,-6,1,5,-4,1,8,-7,-4,-4,5,2,-6,-3,-7,-6,-9,9,2,3,6,7,-3,1,-5,-2,10,6,5,6,10,-8,-6,-2,-5,-6,1,5,10,-3,-10,5,9,5,-1,-3,2,-4,10,-9,-1,6,-10,7,-6,5,5,7,3,7,-10,5,-4,2,-2,-9,-8,6,5,-8,-8,-8,-2,7,6,7,4,9,10,-2,-4,7,5,2,1,-10,10,1,2,9,-2,3,10,-6,3,5,8,-1,-9,4,10,10,3,-6,-9,-2,-1,9,-6,2,-4,7,10,6,1,-1,5,3,-3,2,3,-5,8,6,10,3,6,5,-10,-7,-2,-1,10,-6,4,6,-1,-2,8,2,5,-3,7,-6,10,9,-2,10,6,-6,1,8,5,-2,-7,1,2,-2,2,8,-9,-6,9,2,2,-8,10,-7,-7,7,3,-5,-2,6,4,7,-2,6,-9,-7,-8,3,10,-2,1,10,-7,-9,-3,-2,10,2,-10,-1,9,-9,-10,5,-4,-6,6,9,2,-2,-6,4,4,5,-6,-5,4,-10,-8,-6,-1,9,8,-3,-9,-7,-1,-10,9,-1,2,10,1,2,-2,-4,-1,-2,-3,9,-10,-7,-9,6,-2,5,-2,-2,2,2,4,-10,-1,4,-5,-5,3,-8,9,-2,-10,5,-9,-6,-2,-8,-4,-1,-9,8,2,-3,-5,7,2,3,6,5,-6,8,-9,4,5,10,-4,1,2,-9,2,3,5,7,3,-7,-5,6,-5,9,10,5,-10,8,-8,-2,-2,4,10,-9,7,3,4,6,-2,7,-6,3,-9,-9,7,7,4,-7,5,7,-5,-4,10,6,4,-3,8,-8,9,3,-1,-5,4,-1,-1,10,1,-3,-3,4,-4,2,4,-8,9,9,4,7,10,-6,6,-7,2,-7,-10,-6,9,6,-8,-8,-10,9,3,-1,-1,5,6,2,3,5,-2,8,9,-5,-2,5,10,-5,9,-7,6,-8,8,-10,-1,4,8,-3,8,5,10,2,-4,-2,-5,-3,-5,-1,1,1,8,3,9,-4,-5,7,-9,-3,5,5,-8,-9,9,3,-5,2,-2,-1,3,8,-2,-3,-3,5,-4,8,-1,3,10,2,4,9,10,-9,-5,3,3,10,2,5,-8,-6,-1,10,6,-7,5,8,-5,-10,-3,10,9,-3,-7,-5,-1,-5,1,-4,-7,-1,6,-10,4,3,-3,5,-7,10,-7,1,9,10,1,-9,4,1,-9,3,10,-3,1,4,-8,-1,1,-3,-8,-10,-9,-7,1,3,6,-5,1,9,8,9,-8,-1,4,1,6,-1,4,-8,-6,5,8,-8,10,1,1,-1,10,-1,-5,8,-6,8,9,-5,8,6,-1,-5,4,-8,5,7,3,-2,2,2,1,8,-8,4,2,-2,-6,4,10,-4,-3,-2,9,-5,-4,-9,-6,6,7,-10,9,3,-6,5,1,2,-2,-10,-8,2,-9,8,7,9,-3,-6,-8,10,-10,-3,6,-4,-2,9,-7,-4,3,4,-8,-7,-10,7,-2,4,-4,2,4,8,2,6,10,8,5,-5,-4,6,-5,-4,10,10,6,-3,2,8,9,-5,-5,-4,6,-1,-4,-6,10,8,9,3,4,8,7,9,-10,-7,-1,5,-10,10,5,-5,-6,-4,-4,4,3,3,-10,8,-9,6,5,7,-10,-1,3,-10,10,-5,3,10,1,-7,-6,-10,-7,-6,8,8,-2,-2,7,-5,-8,-9,10,-8,-5,-4,8,-9,-2,9,-10,-9,8,-7,-5,-9,-3,-3,-2,-7,-4,9,9,-8,2,-3,4,3,5,-6,2,-1,-8,1,-5,-6,-9,2,-4,9,10,8,-5,-8,3,-1,9,-4,-10,6,3,-6,-10,2,-1,-10,4,6,1,2,-8,-10,6,-4,9,2,4,6,-8,-8,9,1,5,3,-1,-9,9,-6,3,3,-9,-6,3,-7,-8,10,-2,-9,10,3,10,-10,1,-5,-7,-8,1,1,4,7,-4,7,9,3,1,-1,-5,-9,-9,3],[-1,4,3,-10,-3,10,3,3,5,-3,9,-7,-7,3,1,1,6,-7,-1,7,3,3,-5,10,-2,6,7,8,-2,-9,6,6,-7,3,10,-4,-7,9,-5,2,1,1,-5,-1,9,-9,-2,-8,-10,7,-9,10,-9,-8,7,-2,-9,-8,9,1,-1,-4,7,-2,-1,4,-9,5,-5,-2,4,3,-4,-8,-2,2,1,-6,6,-3,8,-8,-4,-5,-8,1,1,-7,-5,-8,6,-10,-4,3,-6,-8,6,1,10,6,5,2,-1,8,6,3,-6,8,3,1,-10,4,-6,3,-3,2,6,3,-2,3,1,-9,1,6,-9,-3,-7,-4,-4,-6,7,6,-3,1,3,3,-2,-10,10,-8,4,-5,-10,3,5,2,1,-5,8,10,-2,5,5,-6,1,3,7,8,6,-1,3,3,3,8,6,5,3,3,-5,-3,2,2,4,7,1,3,5,-10,5,-2,-8,-2,-6,8,-3,8,9,-7,1,-2,-3,-8,2,7,-8,2,-3,-6,7,-10,7,6,-9,-8,6,-5,-7,-7,3,-8,-2,-6,5,8,5,2,8,-9,-2,9,9,7,7,6,-2,8,5,1,-5,3,8,4,-5,3,10,-3,6,-4,8,10,4,-3,3,2,4,-1,-1,8,-10,1,-5,-8,8,3,-3,5,-4,-8,-6,-8,-6,-3,-6,2,6,-5,-10,1,6,-6,-10,6,-1,2,7,-8,-8,9,-3,-7,6,9,6,6,7,-3,-4,2,5,3,-1,6,-3,1,-8,7,4,-2,10,-4,-9,-4,6,-8,-10,-7,-1,10,10,4,-4,1,-8,8,-10,-5,-7,-2,6,6,-1,7,-5,-8,10,2,2,4,6,-8,-2,5,-1,-4,7,1,2,9,-6,-2,-6,2,8,8,8,10,8,-9,2,-5,5,4,7,5,-8,-10,3,-6,10,5,-1,-7,-10,-9,-2,-1,2,6,-7,-3,-10,-3,8,4,-3,-5,-5,3,-3,-8,-7,-3,2,-10,-10,8,-7,5,-10,3,-9,8,-5,9,-5,2,-4,5,-4,-9,-10,-6,-7,2,1,3,-8,-4,-3,-10,8,10,-8,-9,10,9,-4,6,-10,-1,6,1,-4,-8,5,-5,1,-4,10,3,5,9,1,-3,4,9,9,-5,-2,9,-10,-10,-10,1,-2,-2,-6,-6,-6,5,-4,-3,6,-5,-2,6,1,-4,4,2,8,3,-5,-1,10,5,4,-7,8,7,-6,-2,2,-7,9,-2,-5,1,6,3,1,7,7,-4,-6,3,-7,-9,10,5,7,-6,-4,2,-2,5,-4,9,-6,6,-5,4,-5,10,10,5,-5,-8,2,1,7,-7,8,-4,-8,-8,3,-4,-6,-4,-10,-4,3,-5,3,9,2,3,-2,8,-1,-5,-2,-3,-3,-5,-7,1,-2,-3,4,5,7,-8,8,3,4,-2,-6,5,1,6,10,7,6,6,-1,-6,10,-9,1,8,9,2,-6,-9,-8,6,-4,1,-1,8,10,10,9,8,3,-7,-7,-10,-7,-9,-5,6,-8,-7,-4,10,-10,-3,4,-9,9,-9,-7,9,-7,-1,-5,-2,-4,1,6,1,4,5,7,-4,9,5,2,10,-4,4,7,-2,6,10,-7,-8,-7,10,6,-2,-7,1,-1,-1,-3,6,-2,3,-4,-2,6,-3,-4,8,-6,4,-9,3,7,5,-10,10,-9,-1,-5,-3,4,3,8,-7,4,-10,-8,1,8,3,-8,9,5,-2,5,-1,-3,5,6,8,3,10,-10,7,10,-5,3,8,5,8,7,-9,4,4,7,-9,-9,-2,-2,8,-8,-10,8,-1,-8,-3,10,5,-5,3,2,-2,1,-1,-4,-4,-3,-5,4,4,-7,-9,8,-3,5,-4,-10,-8,-4,-5,-10,-1,7,2,2,-5,2,9,2,-2,10,3,-4,-2,-2,5,7,-2,1,-6,-1,-3,-7,-10,4,5,8,5,-1,-10,-3,-4,2,5,-2,-6,1,4,10,6,-6,8,-1,7,2,-4,4,-7,3,-10,4,8,5,-5,7,-1,-4,-6,3,-6,3,-2,-5,-5,-1,-5,-3,10,4,7,9,-4,-8,-10,6,-8,4,-5,-8,-9,-5,4,7,8,-1,3,-2,3,-7,-2,8,1,-9,3,7,4,8,10,4,-9,2,5,8,5,-10,10,5,2,-8,-1,8,-6,5,-2,-5,-4,-2,2,-8,7,4,-5,-9,-4,1,1,-3,6,3,7,-8,7,-1,-9,-6,6,-4,-10,10,-1,1,2,6,-2,-5,-7,1,2,2,2,10,9,-10,10,-5,3,-10,8,1,5,8,-9,-5,-2,6,5,3,-1,-3,3,1,-1,-8,-7,8,7,5,6,8,-4,-3,10,3,9,4,5,7,-6,-5,-6,-6,-1,-6,8,-7,8,-3,6,-2,5,6,-9,4,-7,-8,-3,5,-5,1,7,-8,-9,-3,-9,9,-1,2,9,-5,6,-9,-10,-5,5,8,5,7,9,9,7,1,-5,9,-10,10,10,7,4,-6,-9,3,2,-5,3,8,2,-9,-4,-10,-3,-2,-2,4,10,-6,-6,-2,10,9,3,-5,-1,-3,3,9,6,8,10,-3,-1,9,10,6,-1,5,-6,-9,5,2,-5,-3,-4,-8,-2,-5,2,10,7,3,-3,-2,-9,6,2,3,10,-10,-6,9,1,-2,-9,-4,10,-6,6,-4,8,-8,-9,-10,6,3,8,1,-5,-2,-5,3,-4,10,7,-4,5,7,-4,5,7,-3,10,-6,-4,1,7,-9,-5,2,5,8,9,-6,-2,-4,-8,4,8,3,8,-5,8,-5,-3,4,2,-9,-7,5,-5,8,5,-9,2,7,6,7,4,-4,1,-6,-9,-6,-10,-8,2,-8,6,10,-1,-9,6,10,10,-8,3,-5,-9,-1,-4,5,2,10,3,9,-4,-3,-6,2,-7,8,6,-4,-4,3,-5,1,4,-9,-1,2,-7,-8,8,-3,-2,-8,-2,-3,-9,-4,7,-4,-7,7,-9,5,-6,3,5,-2,6,-7,-4,7,-9,8,6,-6,-4,3,3,-1,1,6,9,4,8,6,-2,-7,-3,6,6,-6,-4,-4,-7,8,1,5,-2,7,-2,3,-5,-6,5,10,3,-4,5,6,4,-3,7,-5,8,-10,5,6,-6,-8,6,2,4,-8,5,2,-7,-4,-2,3,3,2,-9,-5,3,-5,1,-10,-5,-1,-2,10,7,-4,-3,9,-2,-1,1,5,-1,-5,-8,-5,-5,3,-1,-9,-7,7,1,5,9,4,3,-4,-10,9,3,-2,2,6,-10,-4,-9,4,-7,3,4,5,-9,-4,-5,-8,6,-9,-7,4,1,2,-8,-7,-5,2,10,-9,-6,5,-7,-2,-4,3,-7,9,-6,-5,9,-1,4,6,-3,-10,-9,2,1,10,6,-7,2,-10,-8,5,9,-2,9,9,-2,-3,-6,-8,3,-2,-3,2,6,-4,-7,2,4,10,-9,-7,8,1,-9,2,-6,10,5,5,-6,-8,9,-10,3,8,1,-2,-7,2,1,-7,10,6,-3,-9,-1,3,-6,-3,-7,10,8,6,4,-3,-3,1,10,-9,10,2,-4,9,10,-8,5,-4,9,-10,7,7,4,1,7,8,9,-7,5,-2,2,-3,-9,9,4,-10,-3,-10,5,2,3,-9,10,-5,6,1,9,-4,-10,6,-2,-6,3,3,-9,-2,-3,-5,9,-9,9,-2,5,-9,-8,-2,3,-7,-5,-6,5,7,1,2,-3,-6,10,-3,3,-3,-6,3,-2,6,3,2,-10,-6,10,-2,9,-7,3,6,-1,8,4,7,-4,-5,-4,4,3,-6,6,-10,-5,3,-7,5,10,5,5,-9,-6,-7,-1,-6,-9,-9,-2,1,6,-7,-5,-10,6,-8,-9,1,1,-6,8,-7,6,-3,7,-6,-10,-7,-5,-9,-2,1,3,-7,-1,9,4,-8,5,9,-5,-6,-7,-9,8,3,-4,3,8,4,-10,-1,-10,-5,10,7,-8,-10,6,9,-7,5,-7,-9,-8,-6,-7,-5,6,3,5,-1,5,-9,-1,4,-3,7,9,6,-10,-10,-1,-7,-6,-5,4,-5,5,9,-4,-4,-6,-6,-9,-4,9,10,-10,9,9,8,-7,-2,9,-10,6,10,5,7,-2,-4,7,-1,1,5,-1,3,8,-4,-7,-9,-10,-7,7,-10,-8,-10,-8,-4,-10,-9,5,-10,-7,9,-1,-9,1,6,1,-9,-8,-6,9,-5,10,-9,-6,-8,-5,9,9,-7,-5,8,-6,-6,5,3,3,-10,-4,10,8,-4,-8,9,10,-6,8,2,-3,10,-2,10,3,-10,1,-8,9,1,3,-3,-7,-10,6,-1,-10,-7,-6,-8,8,-7,-8,-7,-6,-2,-2,4,7,6,-5,2,-10,10,7,6,-5,-4,9,-2,2,8,1,3,7,3,8,9,-4,3,-8,7,-3,8,2,9,-4,-8,-10,-4,2,-8,3,-8,8,-8,-2,10,6,7,8,2,4,8,2,-10,-9,7,-10,1,-10,-4,4,8,-2,7,-3,-1,-10,-3,-2,9,3,-5,2,-9,-5,-5,-7,-6,-7,8,-4,9,9,-10,-4,2,6,-8,-3,3,2,-6,10,-7,-7,-9,3,8,-9,-2,-7,10,-2,-4,-9,-5,-4,9,3,2,-2,-2,10,-8,-6,4,5,-7,-6,3,9,-8,7,6,5,9,-1,-4,-8,-2,1,10,-3,2,-9,5,-1,10,10,9,5,5,-8,9,-9,4,10,-5,-2,-2,-10,-10,10,2,-5,-9,10,10,-1,7,1,-2,-5,2,2,8,-1,-6,8,4,8,8,5,9,5,10,7,-7,-8,10,2,-3,-6,-5,6,10,3,3,3,6,8,-6,-7,-5,-9,-5,3,-6,-7,-5,-10,-9,2,1,-6,3,-4,-6,9,7,6,-1,-2,-10,-7,3,10,10,-6,5,-7,-3,-9,-3,-2,-10,-2,7,-9,-4,4,4,1,-3,-5,8,-1,7,2,10,-10,-10,1,-6,-8,7,-10,-3,-6,-6,9,5,7,-9,1,10,-10,-6,10,1,4,10,-8,-3,-1,5,4,-9,-3,-9,8,8,10,8,5,7,-7,3,10,-2,-6,-3,9,3,-10,8,2,5,1,-1,5,6,-7,-1,-5,-1,10,-3,-4,2,-1,-2,-10,2,-4,-8,4,-3,2,-9,-7,-10,-2,5,-1,2,1,4,4,-3,-10,-7,4,5,-4,-5,-5,-7,1,-7,-10,4,-4,3,6,-6,6,1,5,-7,2,-7,8,8,-5,2,5,-9,6,-8,-9,-1,2,-6,-9,4,-7,-2,7,4,6,-9,4,1,1,6,-8,6,8,4,7,3,-1,8,-7,-1,-10,8,-8,6,10,1,9,-7,9,6,-1,7,4,-1,-10,7,-3,-4,4,2,1,4,-1,7,-4,6,-10,9,-10,6,-3,10,8,10,-3,7,-6,-4,-2,8,3,-3,-9,-8,5,1,-9,-5,-4,-8,-7,-2,6,3,8,5,-5,4,-1,3,8,-5,4,3,-6,6,8,8,4,1,3,3,4,-10,-2,2,-8,9,8,-1,-5,-8,4,8,-7,2,-6,-6,6,9,2,10,-8,-3,10,-9,-2,1,-2,6,9,1,-4,-8,-4,10,8,-7,6,-3,5,-5,-10,1,-5,-3,-6,10,3,2,-6,-5,-2,-1,2,9,7,-4,-8,10,3,-8,10,-1,-9,-10,7,7,10,2,-1,1,2,-4,-2,6,10,4,-5,2,-2,-6,2,10,1,-5,-2,-2,-4,7,-3,-9,10,-2,2,8,8,3,-9,-1,-7,-7,-5,-3,7,2,4,2,9,-8,8,3,4,-8,-10,-7,7,6,-3,10,-9,-10,6,-7,-6,3,3,-1,-5,1,-10,-4,2,-7,-9,7,-9,-8,-8,9,-10,-9,-2,1,1,-3,-10,-6,-7,9,9,-3,-2,-3,-6,4,7,-8,-4,-6,-10,-6,8,-5,4,-2,-2,3,-5,-6,-1,6,6,8,-4,-6,7,-9,3,-1,-1,-2,-7,-9,-1,3,9,-1,7,6,-6,-8,-4,8,-2,-8,4,-6,-7,3,-1,-10,-10,-5,2,8,4,1,-2,9,7,-5,-7,2,-5,2,3,-6,4,-10,3,-4,-4,8,3,-10,-3,1,-5,6,10,-7,1,-8,7,3,5,-8,2,7,-3,8,-1,8,4,7,1,8,7,8,5,-5,-1,-9,9,10,2,-8,9,-10,-1,10,1,5,-4,-4,-6,-9,-4,-10,6,-4,8,-1,9,3,-8,-1,10,1,-1,-5,5,-2,4,-1,1,-7,7,-7,1,6,2,-2,-7,8,-9,-5,-7,-5,-8,-1,4,-10,-8,-9,9,-8,-7,5,5,-2,-8,-1,3,-6,-4,1,-7,-9,8,-1,5,9,-2,-6,10,1,2,-3,-10,7,7,2,-9,-8,10,3,1,-7,-6,1,-10,4,-6,8,-9,2,5,10,6,10,-7,1,-6,-4,3,10,10,7,4,-4,2,-9,-1,-8,8,10,2,-5,2,-3,-7,-8,1,-4,1,-8,-5,10,5,-10,-8,8,4,10,-5,8,-8,-10,4,-1,-4,-9,-5,7,-7,-5,-9,-6,-8,-6,-7,-6,5,-1,-2,5,3,-6,-3,8,-10,-4,8,2,6,3,-6,-8,7,-9,6,-6,6,-5,5,-8,8,3,-3,6,-3,-3,-7,10,-2,4,1,-5,2,-5,-7,1,6,-3,-7,6,-7,-10,2,2,-7,2,-6,4,-8,4,-1,-3,9,5,7,7,-2,10,-5,8,9,-9,-6,5,-1,1,6,-8,-2,-10,-4,-4,-1,10,7,9,5,-10,-10,-7,6,4,6,4,7,-8,10,-9,6,-9,7,-8,-6,5,5,-9,-4,4,9,7,-1,-8,6,-2,-9,5,8,10,4,-2,-9,-4,5,10,-6,-1,3,10,9,2,-4,5,2,8,3,9,-10,-5,-2,9,4,-7,-1,6,8,9,-7,-3,-2,-9,10,6,-2,5,8,10,-3,-10,-3,-4,4,-2,-10,10,-6,8,6,4,-7,-9,-2,-8,7,1,2,-8,9,-7,-5,-4,7,-4,5,10,6,8,10,5,2,7,1,2,5,10,10,10,-5,-10,-4,-4,-2,10,-6,9,-1,6,4,-4,9,1,-10,-5,-7,5,7,-4,2,1,1,10,8,5,-3,-9,5,-10,-2,9,-3,-1,-6,7,2,-7,-10,6,2,8,-2,-6,8,1,-4,-9,9,-5,-8,-4,-4,3,10,10,3,-7,-6,2,-10,1,-7,1,2,-2,2,-9,9,-10,1,2,7,-9,-4,-4,7,-10,-10,10,-9,-2,-10,-9,5,9,7,-2,-3,-7,5,1,1,-8,-4,-2,-3,-6,-7,2,-4,8,6,-8,-4,-8,-8,-10,-2,-1,7,9,-8,-10,10,7,-5,-5,-6,2,10,6,10,-9,4,-9,3,-10,-3,-6,-4,-4,7,-2,4,10,5,-2,-3,5,10,8,-2,-2,1,-5,-10,-4,2,-7,-1,8,6,8,2,-9,-9,-4,5,3,6,1,-1,-3,2,-7,9,-6,7,4,-9,-2,10,-9,-3,-3,2,-7,8,4,-9,2,10,3,-3,-7,-8,3,4,-4,-6,-10,-10,1,-8,-9,-10,5,8,7,2,6,-2,1,10,-5,-2,-5,3,-4,5,-5,2,-4,7]], dtype = "uint32")#candidate|7376|(2, 2912)|const|uint32
bop_7377 = relay.mod(bop_7354.astype('float64'), const_7376.astype('float64')) # shape=(2, 2912)
output = relay.Tuple([call_7324,call_7345,var_7347,bop_7363,bop_7373,bop_7377,])
output2 = relay.Tuple([call_7325,call_7348,var_7347,bop_7363,bop_7373,bop_7377,])
func_7387 = relay.Function([var_7347,], output)
mod['func_7387'] = func_7387
mod = relay.transform.InferType()(mod)
var_7388 = relay.var("var_7388", dtype = "uint32", shape = (1800,))#candidate|7388|(1800,)|var|uint32
output = func_7387(var_7388)
func_7389 = relay.Function([var_7388], output)
mutated_mod['func_7389'] = func_7389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2849_call = mod.get_global_var('func_2849')
func_2850_call = mutated_mod.get_global_var('func_2850')
call_7394 = relay.TupleGetItem(func_2849_call(), 0)
call_7395 = relay.TupleGetItem(func_2850_call(), 0)
func_4875_call = mod.get_global_var('func_4875')
func_4878_call = mutated_mod.get_global_var('func_4878')
var_7397 = relay.var("var_7397", dtype = "int32", shape = (84,))#candidate|7397|(84,)|var|int32
const_7398 = relay.const([6,7,-9,10,-7,-5,2,-5,5,-5,-7,-1,-9,-7,-3,-10,2,-4,4,-10,-5,-5,10,3,4,-6,-9,5,2,-9,-6,1,-8,10,7,4,-7,-10,-9,-4,-2,-5,7,-3,3,1,2,-9,7,2,-9,9,-7,5,-3,-10,-9,-8,-4,3,-2,9,8,-4,-7,-2,-5,4,-9,10,8,-7,-5,-3,-5,-8,-3,-10,-5,8,1,2,-9,7,-5,-2,-7,2,-1,4,-1,2,1,5,-6,-8,2,-4,6,1,-10,-8,9,2,-5,7,-9,2,-4,-6,9,-9,5,2,-9,-7,-5,8,5,7,6,-7,-4,7,-5,8,8,-7,-3,6,-3,10,6,-5,6,2,-3,-7,6,-4,-6,9,2,-6,-6,-6,5,-10,-2,3,-4,-9,2,5,-9,-2,-3,-8,-8,7,-9,4,9,-5,6,10,-5,-6,-5,8,2,-1,-1,-8,-5,5,-10,-6,-3,-1,-2,-1,-9,3,-10,10,-1,6,9,-2,-1,-8,6,-1,6,-1,2,-3,-1,-5,-7,4,5,9,4,-10,-8,5,4,-4,9,-9,7,1,8,10,2,-5,-2,3,-6,10,-3,2,2,-8,-3,-1,8,-8,-8,4,-10,7,3,-7,-6,7,-3,-9,-4,5,5,-8,10,9,-4,-7,4,-8,7,10,-4,7,5,-2,4,-6,5,-9,-10,2,5,-10,-5,-8,4,8,-4,-5,10,7,5,2,-9,-3,-1,-5,-4,7,-3,-6,2,7,8,6,9,3,-9,4,-7,-7,3,5,6,1,-7,-6,-10,7,-5,9,6,-8,8,-3,2,-3,3,-4,-10,-6,-1,-7,5,10,-5,-4,10,8,-3,-3,2,-9,2,3,10,10,-4,-2,-9,1,-3,8,4,-1,8,3,8,6,7,5,-9,-9,-1,3,5,-5,8,2,-9,10,-7,-7,5,6,-3,7,5,6,-7,6,-5,-10,6,5,-5,1,6,-8,1,2,6,-5,-5,6,2,-6,5,-1,10,-6,-9,-8,7,7,-9,-2,-8,5,-10,5,-5,10,-9,-10,-5,1,-3,2,-4,-8,7,7,6,9,4,-7,-7,6,-6,-2,-3,8,3,-6,10,-1,3,-4,-1,-3,9,2,7,-3,-6,-7,-9,7,-4,10,-6,-2,-10,-7,9,5,-2,-5,7,-3,2,-4,-4,6,5,-1,-8,1,9,-8,8,8,10,-8,-3,10,10,8,-4,-1,10,-9,4,6,-7,-4,8,6,5,-3,-6,4,6,9,6,-8,-1,7,-8,-1,-9,-2,6,5,4,10,2,6,-5,9,-5,10,-5,-1,3,-9,-6,-7,1,-4,9,-6,5,8,-7,3,-5,7,-3,-4,10,-7,6,-9,-8,-1,6,-10,1,2,7,9,-10,4,5,-8,-3,1,10,8,4,5,-9,10,-2,-8,-6,3,-3,9,-6,3,3,1,-6,1,10,-8,2,-9,-10,5,3,-4,-4,-2,-10,-10,-9,-6,1,4,3,10,-10,2,-5,-6,5,-3,-2,9,-2,-7,-1,-7,-2,6,3,-1,-7,4,9,10,-1,1,10,9,9,4,-1,-4,9,8,-8,-6,-1,-8,-2,4,-3,-1,7,6,6,-9,10,7,5,-3,4,9,2,8,8,-1,1,4,10,5,10,2,-7,-9,-4,-7,-4,4,6,3,-5,4,6,3,8,3,-2,-9,-6,3,-3,-8,9,-6,-5,-8,5,8,10,9,-1,-7,9,-4,-6,-5,-7,7,-5,10,2,-2,-2,8,2,-9,2,-8,3,8], dtype = "int32")#candidate|7398|(672,)|const|int32
call_7396 = relay.TupleGetItem(func_4875_call(relay.reshape(var_7397.astype('int32'), [84,]), relay.reshape(const_7398.astype('int32'), [672,]), ), 3)
call_7399 = relay.TupleGetItem(func_4878_call(relay.reshape(var_7397.astype('int32'), [84,]), relay.reshape(const_7398.astype('int32'), [672,]), ), 3)
func_1124_call = mod.get_global_var('func_1124')
func_1130_call = mutated_mod.get_global_var('func_1130')
const_7402 = relay.const([[-7.649560,2.400347,4.041876,6.898968,4.871921,-5.527939,-5.738124,-3.388965,-0.060415,7.480128,-3.756625,-0.932020,8.427964,1.276854,-7.566013,-5.281990,9.012231,4.295932,-0.564185,-9.961420,8.499767,2.508400,3.316157,-6.598400,7.159291,9.805640,-5.285766,-2.843234,-8.153215,-4.229113,-6.694035,0.014935,-4.055027,-4.593927,1.675233,-0.519974,-7.765144,4.451641,-0.028227,8.617149,5.508543,3.236930,6.352562,8.891879,-4.845666,-5.832667,-1.346456,-5.186784,-2.358776,3.296780,9.616132,-2.236474,-5.765752,0.206949,-5.261634,-0.020375,0.350470,6.203296,2.604293,-0.142987,-5.638305,-1.531117,-7.266044,-8.542056,-7.247047,2.743821,5.489344,6.092765,2.458587,-9.044304,1.681906,0.450442,1.126886,4.809277,-4.721627,-9.121886,0.625618,6.856097,0.278944,-8.599943,-1.864726,7.649738,-7.833645,0.108659,4.762331,2.416270,-4.307938,4.311777,4.959703,9.978550,3.504277,7.579237,-7.658757,-9.890540,-3.733141,4.072733,-8.441357,-1.537615,1.435089,-9.393534,-8.642156,-8.910471,8.512490,-7.285955,-8.842415,-8.253263,5.507153,-3.532335,-3.051683,5.142869,-0.979072,2.936331,8.276143,9.887117,6.273999,1.112472,7.990472,8.720392,5.183921,1.069406,5.886863,0.976840,8.351753,-7.646975,6.479984,-3.554600,5.042851,-0.979007,-2.007562,4.334816,-9.568738,3.168005,-2.840447,-0.581164,-9.246127,-8.423995,8.361782,-7.377212,1.736320,-1.856736,-1.860667,-3.156063,2.605222,-2.288741,-7.662739,2.715330,-9.825528,-6.109484,4.604587,-3.161904,8.947160,9.417199,0.209083,6.132794,1.236959,6.751866,2.039496,6.503354,-9.677170,-7.780332,6.316562,7.343983,-9.928629,9.803775,-0.017505]], dtype = "float64")#candidate|7402|(1, 165)|const|float64
const_7403 = relay.const([[-2,8,-8,4,6,3,2,-5,7,8,-9,-10,2,-6,1,-9,-2,6,1,2,-1,1,8,-10,-10,-5,-9,-1,-1,9,-8,-7,-5,-8,3,6,-8,7,4,3,6,-1,10,-9,-1,-5,7,9,4,-10,1,1,2,-5,7,-10,-5,9,-3,8,-9,4,4,-1,3,5,7,1,-4,-8,6,4,-1,9,-3,9,-10,9,-6,-10,2,-1,1,-10,2,-4,8,-10,-2,2,-5,-7,-5,9,-9,-10,-4,1,7,-10,1,-7,-3,7,-7,-1,1,-9,6,-8,9,-7,-1,8,-10,-6,4,10,-2,3,8,-4,-1,5,-3,4,1,4,-8,9,-3,-6,8,-4,-5,-8,10,9,-6,-1,-5,10,-4,7,7,9,1,-8,-3,7,-9,8,8,-1,4,-3,6,-5,6,-4,10,-4,1,7,-4,2,9,5,9,-2,-9,-2,-8,5,2,8,3,10,6,9,-4,-3,3,2,5,7,-9,-9,7,-3,-3,1,-5,-1,-2,8,1,9,-1,-6,-5,2,-3,4,-5,10,-8,-6,-4,1,-7,-2,-4,2,3,4,4,-3,7,6,-4,3,-9,-4,-8,-1,-6,5,3,7,-9,6,-9,10,-6,-1,5,2,-3,-7],[1,-7,-10,-9,4,-10,9,6,-5,-7,3,3,9,9,4,-6,5,-4,-8,9,10,-4,-5,8,-5,1,2,3,1,-5,10,-2,5,-10,-10,4,8,1,-8,-3,4,10,-10,-7,-7,-8,6,-3,-5,-3,-2,4,-4,-3,-4,5,2,3,-10,-5,-5,-5,-4,-1,1,-3,-10,7,4,8,8,-7,9,-2,-2,-8,-1,-5,3,-3,9,-9,5,-5,-8,8,-8,-6,-4,-8,7,-3,-10,5,-4,8,-6,-4,-5,-1,-4,8,-3,1,-3,6,-6,2,7,9,-6,7,-8,-5,2,5,-7,1,7,9,-2,4,4,-4,-3,-4,-4,3,4,4,-5,3,3,-2,-6,4,8,6,4,-4,-6,8,-1,-1,-10,-2,-5,-7,-9,-1,-1,-2,5,-10,-1,7,-5,5,-5,-1,-1,-10,-8,-5,5,3,-4,-5,-5,7,-9,1,-9,-10,-5,9,-3,-2,-5,9,4,-8,-7,7,-7,-5,-1,2,5,4,4,7,4,8,8,-1,-9,3,1,-5,-8,-7,-9,9,-3,-7,8,-4,-3,4,-2,-8,-4,-7,2,-5,2,-9,5,8,-1,-4,-9,3,-5,-5,-2,9,5,2,6,8,-3,3,-3,5,6,-6,2,-6]], dtype = "int8")#candidate|7403|(2, 240)|const|int8
call_7401 = relay.TupleGetItem(func_1124_call(relay.reshape(const_7402.astype('float64'), [11, 5, 3]), relay.reshape(const_7403.astype('int8'), [480,]), relay.reshape(call_7396.astype('int32'), [84, 1]), relay.reshape(const_7398.astype('int32'), [672,]), ), 6)
call_7404 = relay.TupleGetItem(func_1130_call(relay.reshape(const_7402.astype('float64'), [11, 5, 3]), relay.reshape(const_7403.astype('int8'), [480,]), relay.reshape(call_7396.astype('int32'), [84, 1]), relay.reshape(const_7398.astype('int32'), [672,]), ), 6)
output = relay.Tuple([call_7394,call_7396,var_7397,const_7398,call_7401,const_7402,const_7403,])
output2 = relay.Tuple([call_7395,call_7399,var_7397,const_7398,call_7404,const_7402,const_7403,])
func_7413 = relay.Function([var_7397,], output)
mod['func_7413'] = func_7413
mod = relay.transform.InferType()(mod)
mutated_mod['func_7413'] = func_7413
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7414 = relay.var("var_7414", dtype = "int32", shape = (84,))#candidate|7414|(84,)|var|int32
func_7413_call = mutated_mod.get_global_var('func_7413')
call_7415 = func_7413_call(var_7414)
output = call_7415
func_7416 = relay.Function([var_7414], output)
mutated_mod['func_7416'] = func_7416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5802_call = mod.get_global_var('func_5802')
func_5803_call = mutated_mod.get_global_var('func_5803')
call_7418 = relay.TupleGetItem(func_5802_call(), 1)
call_7419 = relay.TupleGetItem(func_5803_call(), 1)
output = call_7418
output2 = call_7419
func_7420 = relay.Function([], output)
mod['func_7420'] = func_7420
mod = relay.transform.InferType()(mod)
output = func_7420()
func_7421 = relay.Function([], output)
mutated_mod['func_7421'] = func_7421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3042_call = mod.get_global_var('func_3042')
func_3044_call = mutated_mod.get_global_var('func_3044')
call_7442 = relay.TupleGetItem(func_3042_call(), 1)
call_7443 = relay.TupleGetItem(func_3044_call(), 1)
func_5977_call = mod.get_global_var('func_5977')
func_5979_call = mutated_mod.get_global_var('func_5979')
call_7444 = relay.TupleGetItem(func_5977_call(), 1)
call_7445 = relay.TupleGetItem(func_5979_call(), 1)
var_7451 = relay.var("var_7451", dtype = "bool", shape = (9, 2, 12))#candidate|7451|(9, 2, 12)|var|bool
bop_7452 = relay.power(call_7442.astype('float32'), relay.reshape(var_7451.astype('float32'), relay.shape_of(call_7442))) # shape=(9, 2, 12)
bop_7455 = relay.power(call_7443.astype('float32'), relay.reshape(var_7451.astype('float32'), relay.shape_of(call_7443))) # shape=(9, 2, 12)
func_5495_call = mod.get_global_var('func_5495')
func_5498_call = mutated_mod.get_global_var('func_5498')
var_7457 = relay.var("var_7457", dtype = "float64", shape = (165,))#candidate|7457|(165,)|var|float64
call_7456 = relay.TupleGetItem(func_5495_call(relay.reshape(var_7457.astype('float64'), [11, 15])), 1)
call_7458 = relay.TupleGetItem(func_5498_call(relay.reshape(var_7457.astype('float64'), [11, 15])), 1)
func_5121_call = mod.get_global_var('func_5121')
func_5122_call = mutated_mod.get_global_var('func_5122')
call_7460 = relay.TupleGetItem(func_5121_call(), 0)
call_7461 = relay.TupleGetItem(func_5122_call(), 0)
func_2185_call = mod.get_global_var('func_2185')
func_2188_call = mutated_mod.get_global_var('func_2188')
const_7466 = relay.const([-9.052961,4.852939,7.215082,7.864154,4.751605,9.720510,-3.377711,6.879664,6.185140,-6.365005,2.208226,3.845214,-0.222393,-0.459585,0.556447,1.663847,0.547570,0.172915,-7.726802,2.144029,-6.592082,3.618050,-3.611451,9.022959,-9.632995,8.251907,-8.789555,-4.486159,-1.150077,7.663237,9.889046,6.891518,8.660483,-2.643328,6.860093,3.685679,-4.343243,-8.020939,-4.285509,-4.237645,0.312596,-3.754571,-9.724750,-9.367180,2.293691,4.017096,-8.173220,8.122338,6.674686,-6.644546,2.453843,9.782513,-9.608613,-4.712604,8.241406,2.458485,6.680932,7.592286,3.299937,-5.064091,7.627633,2.709614,-3.311385,8.068538,-3.715495,-3.579385,5.894364,7.049021,9.147799,-6.742440,8.420408,6.567270,6.720110,-9.721717,5.947313,7.161773,-3.254019,-8.904343,1.483243,0.067005,9.598713,-5.248179,8.075010,-1.561244], dtype = "float64")#candidate|7466|(84,)|const|float64
call_7465 = func_2185_call(relay.reshape(const_7466.astype('float64'), [1, 7, 12]))
call_7467 = func_2185_call(relay.reshape(const_7466.astype('float64'), [1, 7, 12]))
bop_7470 = relay.maximum(var_7451.astype('int64'), relay.reshape(call_7442.astype('int64'), relay.shape_of(var_7451))) # shape=(9, 2, 12)
bop_7473 = relay.maximum(var_7451.astype('int64'), relay.reshape(call_7443.astype('int64'), relay.shape_of(var_7451))) # shape=(9, 2, 12)
func_4145_call = mod.get_global_var('func_4145')
func_4149_call = mutated_mod.get_global_var('func_4149')
var_7477 = relay.var("var_7477", dtype = "int16", shape = (324,))#candidate|7477|(324,)|var|int16
call_7476 = relay.TupleGetItem(func_4145_call(relay.reshape(var_7477.astype('int16'), [3, 12, 9]), relay.reshape(var_7477.astype('int16'), [3, 12, 9]), ), 1)
call_7478 = relay.TupleGetItem(func_4149_call(relay.reshape(var_7477.astype('int16'), [3, 12, 9]), relay.reshape(var_7477.astype('int16'), [3, 12, 9]), ), 1)
output = relay.Tuple([call_7444,bop_7452,call_7456,var_7457,call_7460,call_7465,const_7466,bop_7470,call_7476,var_7477,])
output2 = relay.Tuple([call_7445,bop_7455,call_7458,var_7457,call_7461,call_7467,const_7466,bop_7473,call_7478,var_7477,])
func_7483 = relay.Function([var_7451,var_7457,var_7477,], output)
mod['func_7483'] = func_7483
mod = relay.transform.InferType()(mod)
var_7484 = relay.var("var_7484", dtype = "bool", shape = (9, 2, 12))#candidate|7484|(9, 2, 12)|var|bool
var_7485 = relay.var("var_7485", dtype = "float64", shape = (165,))#candidate|7485|(165,)|var|float64
var_7486 = relay.var("var_7486", dtype = "int16", shape = (324,))#candidate|7486|(324,)|var|int16
output = func_7483(var_7484,var_7485,var_7486,)
func_7487 = relay.Function([var_7484,var_7485,var_7486,], output)
mutated_mod['func_7487'] = func_7487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1319_call = mod.get_global_var('func_1319')
func_1320_call = mutated_mod.get_global_var('func_1320')
call_7492 = relay.TupleGetItem(func_1319_call(), 0)
call_7493 = relay.TupleGetItem(func_1320_call(), 0)
output = relay.Tuple([call_7492,])
output2 = relay.Tuple([call_7493,])
func_7506 = relay.Function([], output)
mod['func_7506'] = func_7506
mod = relay.transform.InferType()(mod)
output = func_7506()
func_7507 = relay.Function([], output)
mutated_mod['func_7507'] = func_7507
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7518 = relay.var("var_7518", dtype = "uint64", shape = (1, 1, 9))#candidate|7518|(1, 1, 9)|var|uint64
var_7519 = relay.var("var_7519", dtype = "uint64", shape = (15, 3, 9))#candidate|7519|(15, 3, 9)|var|uint64
bop_7520 = relay.logical_xor(var_7518.astype('uint64'), var_7519.astype('uint64')) # shape=(15, 3, 9)
bop_7536 = relay.bitwise_and(bop_7520.astype('uint32'), relay.reshape(var_7519.astype('uint32'), relay.shape_of(bop_7520))) # shape=(15, 3, 9)
uop_7543 = relay.asin(var_7518.astype('float32')) # shape=(1, 1, 9)
func_4702_call = mod.get_global_var('func_4702')
func_4704_call = mutated_mod.get_global_var('func_4704')
call_7553 = relay.TupleGetItem(func_4702_call(), 2)
call_7554 = relay.TupleGetItem(func_4704_call(), 2)
var_7555 = relay.var("var_7555", dtype = "float32", shape = (2, 1, 9))#candidate|7555|(2, 1, 9)|var|float32
bop_7556 = relay.floor_divide(uop_7543.astype('float32'), var_7555.astype('float32')) # shape=(2, 1, 9)
output = relay.Tuple([bop_7536,call_7553,bop_7556,])
output2 = relay.Tuple([bop_7536,call_7554,bop_7556,])
func_7560 = relay.Function([var_7518,var_7519,var_7555,], output)
mod['func_7560'] = func_7560
mod = relay.transform.InferType()(mod)
mutated_mod['func_7560'] = func_7560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7560_call = mutated_mod.get_global_var('func_7560')
var_7562 = relay.var("var_7562", dtype = "uint64", shape = (1, 1, 9))#candidate|7562|(1, 1, 9)|var|uint64
var_7563 = relay.var("var_7563", dtype = "uint64", shape = (15, 3, 9))#candidate|7563|(15, 3, 9)|var|uint64
var_7564 = relay.var("var_7564", dtype = "float32", shape = (2, 1, 9))#candidate|7564|(2, 1, 9)|var|float32
call_7561 = func_7560_call(var_7562,var_7563,var_7564,)
output = call_7561
func_7565 = relay.Function([var_7562,var_7563,var_7564,], output)
mutated_mod['func_7565'] = func_7565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6209_call = mod.get_global_var('func_6209')
func_6211_call = mutated_mod.get_global_var('func_6211')
call_7569 = func_6209_call()
call_7570 = func_6209_call()
func_7506_call = mod.get_global_var('func_7506')
func_7507_call = mutated_mod.get_global_var('func_7507')
call_7571 = relay.TupleGetItem(func_7506_call(), 0)
call_7572 = relay.TupleGetItem(func_7507_call(), 0)
func_2020_call = mod.get_global_var('func_2020')
func_2022_call = mutated_mod.get_global_var('func_2022')
const_7574 = relay.const([-3,-1,-3,7,2,-8,2,-7,5,-2,-2,3,-4,-9,-4,-8,-1,-6,-7,-6,2,9,2,-9,-8,9,9,6,-2,-10,5,-5,-8,-1,-3,5,4,9,10,3,1,9,-2,5,-10,-2,4,1,10,6,-2,-9,7,-10,-8,-6,-5,-8,8,2,-10,-4,4,6,-9,9,5,8,8,8,3,4,9,-6,7,6,2,2,5,-2,-2,8,9,-9,5,2,3,7,-9,-8,1,-4,4,-1,-7,5,-3,7,8,8,5,-1,-7,-10,-9,1,-4,5,4,-9,8,-10,-7,-3,-3,8,3,6,-6,-4,-5,-9,3,-1,9,-8,5,7,5,7,-3,3,4,5,6,-9,8,3,1,10,3,-6,-6,-8,-3,8,-2,3,2,10,-1,10,6,-1,-5,-6,9,-5,-2,-9,-2,4,-7,1,-7,9,9,-7,3,1,-1,8,-8,-6,-10,7,1,5,8,-9,-9,3,8,-5,8,-10,-5,-8,3,-3,-10,-2,-4,10,5,7,10,3,9,-10,6,-5,-10,3,-8,6,-9,-8,-7,4,-8,7,-10,5,-8,4,4,-2,2,-10,2,-8,-4,3,-5,-5,-6,10,-3,-3,9,-5,-9,-9,-4,3,3,-6,-10,-8,4,7,-6,-7,-1,9,10,-4,3,-9,-2,-3,-6,4,8,10,-7,-5,3,1,-2,3,-4,-10,2,-4,-6,3,-5,-5,-1,8,-1,1,3,-7,4,-9,-8,-5,-2,5,5,-7,5,5,8,-5,4,-2,-2,6,-10,-4,5,7,10,5,-1,8,-6,-3,-6,-5,8,1,-10,-6,1,-9,9,6,-9,5,-5,8,-5,8,-3,2,-2,-1,-10,-3,7,1,-7,7,8,-5,-4,4,4,-1,-5,-8,7,-1,6,-10,-3,9,8,5,-8,8,-3,-5,4,-6,10,10,-5,4,3,6,-5,-8,-1,-8,3,-4,8,-7,-5,5,-9,3,-6,-5,3,6,6,-10,7,9,3,8,3,8,-6,-5,8,9,9,4,5,9,-6,-8,6,-2,-3,10,4,7,-1,-5,4,-2,7,-4,-7,-4,1,-5,1,4,6,1,-2,-9,1,-1,-9,-8,2,-9,-5,2,-6,3,-2,1,-2,7,-1,8,-2,8,3,-10,-8,-4,1,-10,-2,-4,1,4,8,-9,10,2,6,5,-8,6,3,10,5,1,-5,4,10,9,-9,-8,6,3,2,3,3,7,-9,-2,-6,-4,9,5,3,-9,4,3,9,-4,-4,-2,-8,6,3,6,2,10,-7,3,3,-4,1,-9,-3,-1,1,5,2,1,-9,7,-6,-3,4,-2,-7,-3,6,-9,4,6,-5,7,2,7,2,3,10,10,1,10,10,8,-5,7,-9,7,5,5,9,-9,5,10,7,1,1,9,9,9,6,-3,10,3,3,3,2,-4,3,4,3,-1,1,8,-7,3,-3,-2,-8,8,-5,-5,4,-3,5,-10,-3,3,-1,3,7,3,2,-3,-2,-2,-6,3,-6,1,-4,-10,-2,-2,-1,10,10,-8,-3,-5,-5,-2,-1,3,1,-9,-6,1,-1,10,-9,9,-8,-4,-9,-3,-3,7,10,-3,3,6,-2,-7,2,-4,10,10,2,8,-10,-6,-8,1,3,8,8,7,-3,-3,-4,3,2,-5,-7,6,5,-2,-6,-2,-7,-7,6,-4,-10,1,-8,9,8,-6,6,4,-5,6,-9,2,-9,-10,-5,-4,-3,-1,9,-1,-6,4,9,5,4,9,8,-7,2,-1,-4,-6,-10,-10,-8,8,7,6,-1,4,-2,9,6,-6,5,-7,-4,8,9,7,-8,-1,-8,-3,-8,6,-1,10,3,6,-5,7,-8,-7,2,4,8,4,-2,7,-5,-10,8,-4,5,-8,-4,4,-9,-1,-7,-10,-2,-3,1,-6,2,3,-5,-10,-4,5,-3,-10,-3,3,5,3,8,-4,7,-5,6,-9,-2,5,7,-4,10,5,6,-1,3,-10,1,10,-4,7,1,-2,6,9,-7,6,-10,3,10,8,-2,-4,2,1,9,5,5,-2,-5,8,5,-1,6,-10,-10,10,9,-4,-8,-9,4,-6,3,2,9,10,-4,1,-5,-6,1,6,2,3,5,-8,7,-6,1,8,7,-8,-9,1,-9,-10,3,-2,-3,6,8,5,-7,8,10,-10,6,-8,-6,-10,5,7,5,4,8,-6,-3,4,3,-10,1,-9,-9,-3,-5,-1,-2,-2,-2,7,-8,6,3,3,-5,-10,-4,-1,-8,-9,-7,7,1,-10,-4,2,-9,5,-10,9,-3,10,-10,2,7,-2,2,-8,9,-5,-3,6,7,4,-10,-3,-4,10,-7,-3,-4,1,-6,-8,-4,-7,1,-9,-5,-8,-7,-7,3,4,-10,4,-4,9,-1,5,1,2,-7,2,3,-6,10,-1,3,-5,-4,8,-6,-10,-5,2,-8,9,7,-7,3,1,9,8,-7,4,4,1,-8,-6,-5,10,-5,9,2,2,-9,1,-7,7,-4,7,-4,5,-9,-6,9,8,-5,-8,2,4,-5,9,-6,5,-9,5,1,5,10,4,7,3,-8,-9,-3,2,-10,7,7,-5,4,-10,-9,-5,-8,10,9,-5,6,-7,-9,-4,-8,-2,-5,-1,-6,-4,-8,5,5,9,-9,-3,10,-2,9,-5,-9,3,-5,-2,5,-9,-4,9,10,-5,2,-5,-6,-1,-5,3,5,-7,-10,3,-7,-8,-7,-10,5,-9,3,-1,-5,5,1,5,4,8,2,-1,4,-10,6,-1,7,-2,-5,1,-7,9,6,6,7,6,-5,-10,6,-1,2,-5,-3,-3,-2,-8,3,-9,-3,-1,-8,2,3,10,2,2,-5,-4,6,9,-4,-8,-6,5,3,2,2,3,-5,-5,-6,2,-3,-2,-6,8,-7,4,-7,-7,-7,-2,-4,-6,-9,6,7,-9,-4,3,9,7,-10,-3,4,-7,-8,1,3,-1,-10,8,-2,-10,-7,6,4,3,-6,1,8,-10,7,8,-1,-2,5,10,6,-4,3,-8,3,1,10,7,1,4,-9,8,3,-2,-2,6,2,-3,-7,-2,-4,10,-6,-4,4,-5,-2,2,-6,4,7,-6,-7,4,9,6,10,1,-3,-4,-3,-8,3,2,6,-7,-3,4,3,-6,5,-8,-8,-2,4,-5,-5,3,5,-7,-9,-8,7,-2,1,3,-10,10,9,-8,-7,9,-6,-8,-6,-5,-7,-7,4,-5,7,-8,8,-4,1,-10,-5,-8,9,-3,3,10,-1,-6,-6,10,8,8,-8,-1,-6,-7,9,-1,3,3,-2,-10,10,7,-7,-9,5,-1,2,1,-4,-9,4,-1,-4,5,-9,-6,-10,-7,10,-4,-5,-7,6,7,6,2,5,-9,8,-2,10,8,-3,-9,-2,7,7,-4,-1,4,6,5,9,-10,-9,-4,4,-1,8,1,2,-7,1,-3,-4,-10,-2,4,1,8,10,-9,5,-3,-9,-5,4,1,5,10,10,2,4,-3,1,5,3,-6,-5,5,7,4,-2,-9,-8,6,10,9,-3,-9,4,-6,9,9,-2,7,-4,1,7,-5,-10,4,-9,3,7,-6,7,2,-3,1,5,7,10,-9,9,-3,-5,10,-2,-3,7,2,1,-2,-4,2,-3,-1,6,-2,-4,-5,-4,10,-7,6,4,6,1,10,2,-5,10,10,5,-2,-8,7,-9,9,2,10,3,-3,-5,-8,-6,4,10,-3,-7,-6,-1,9,10,8,3,-9,-3,9,-5,4,1,-7,-1,7,-5,-3,6,6,1,-7,1,9,10,1,6,-7,5,-1,6,4,-3,-8,10,4,-10,-6,-8,-5,4,4,-1,-8,-8,-3,-8,-6,6,9,-9,-9,-3,10,-1,-2,10,4,10,8,-2,-2,9,-1,-1,-5,3,-9,-9,10,3,5,-1,-5,-3,-6,-7,7,-6,3,1,8,-9,10,8,-10,-5,4,-3,4,-5,3,1,-8,-10,-4,6,-5,-1,-5,-7,9,9,8,4,10,-6,-1,-4,-4,7,-5,4,-10,-5,3,9,5,-7,3,-7,-1,7,10,1,8,-5,-5,-5,5,9,5,10,-7,3,8,-3,4,3,3,-9,-5,6,-5,-4,-2,-8,10,-4,-7,-9,8,-6,-1,-8,4,-5,-4,-9,-1,-1,6,7,1,5,10,-7,-5,3,-3,-2,8,7,10,3,1,-4,5,-4,-5,-6,-2,-7,7,7,-1,-8,10,-3,3,2,1,-2,-1,7,-5,3,8,-6,-10,-3,-4,9,6,4,9,-5,6,-1,4,-1,10,8,-3,-1,7,-3,-6,-5,-6,4,-7,-8,-8,9,4,3,-5,-2,-5,-1,-8,5,9,-8,1,10,3,-2,-4,5,1,2,8,4,6,6,-2,-7,3,5,7,1,-3,1,1,5,-5,-8,10,8,9,-9,-7,3,-2,-3,4,-9,6,-6,7,1,-10,-6,-10,6,2,-10,2,8,-2,2,-4,4,-10,-7,4,10,-6,4,-5,-5,8,6,1,-5,-7,-10,8,3,6,5,-7,-4,5,10,10,5,-3,7,8,-4,9,-8,-9,4,-8,-3,-6,-1,-5,-9,6,-3,8,10,2,-1,-9,-7,-7,-2,-10,1,4,-4,-2,-5,8,5,8,2,-3,-2,-9,1,-9,-10,-9,-4,-4,3,-3,4,4,9,-9,1,-1,2,-3,-5,-5,-1,7,-7,-6,-7,-7,-2,2,-5,4,1,-1,7,-8,-6,7,-7,-3,-5,7,7,5,-6,-3,-8,-7,4,1], dtype = "uint32")#candidate|7574|(1800,)|const|uint32
call_7573 = relay.TupleGetItem(func_2020_call(relay.reshape(const_7574.astype('uint32'), [1800, 1])), 2)
call_7575 = relay.TupleGetItem(func_2022_call(relay.reshape(const_7574.astype('uint32'), [1800, 1])), 2)
func_4434_call = mod.get_global_var('func_4434')
func_4435_call = mutated_mod.get_global_var('func_4435')
call_7576 = relay.TupleGetItem(func_4434_call(), 1)
call_7577 = relay.TupleGetItem(func_4435_call(), 1)
func_2534_call = mod.get_global_var('func_2534')
func_2535_call = mutated_mod.get_global_var('func_2535')
call_7580 = relay.TupleGetItem(func_2534_call(), 2)
call_7581 = relay.TupleGetItem(func_2535_call(), 2)
func_5546_call = mod.get_global_var('func_5546')
func_5547_call = mutated_mod.get_global_var('func_5547')
call_7582 = relay.TupleGetItem(func_5546_call(), 4)
call_7583 = relay.TupleGetItem(func_5547_call(), 4)
output = relay.Tuple([call_7569,call_7571,call_7573,const_7574,call_7576,call_7580,call_7582,])
output2 = relay.Tuple([call_7570,call_7572,call_7575,const_7574,call_7577,call_7581,call_7583,])
func_7607 = relay.Function([], output)
mod['func_7607'] = func_7607
mod = relay.transform.InferType()(mod)
mutated_mod['func_7607'] = func_7607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7607_call = mutated_mod.get_global_var('func_7607')
call_7608 = func_7607_call()
output = call_7608
func_7609 = relay.Function([], output)
mutated_mod['func_7609'] = func_7609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5121_call = mod.get_global_var('func_5121')
func_5122_call = mutated_mod.get_global_var('func_5122')
call_7676 = relay.TupleGetItem(func_5121_call(), 0)
call_7677 = relay.TupleGetItem(func_5122_call(), 0)
output = call_7676
output2 = call_7677
func_7684 = relay.Function([], output)
mod['func_7684'] = func_7684
mod = relay.transform.InferType()(mod)
output = func_7684()
func_7685 = relay.Function([], output)
mutated_mod['func_7685'] = func_7685
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7692 = relay.var("var_7692", dtype = "float64", shape = ())#candidate|7692|()|var|float64
var_7693 = relay.var("var_7693", dtype = "float64", shape = (8, 1, 4))#candidate|7693|(8, 1, 4)|var|float64
bop_7694 = relay.floor_divide(var_7692.astype('float64'), var_7693.astype('float64')) # shape=(8, 1, 4)
bop_7711 = relay.mod(bop_7694.astype('float64'), var_7692.astype('float64')) # shape=(8, 1, 4)
bop_7716 = relay.divide(bop_7694.astype('float64'), relay.reshape(bop_7711.astype('float64'), relay.shape_of(bop_7694))) # shape=(8, 1, 4)
output = bop_7716
output2 = bop_7716
func_7723 = relay.Function([var_7692,var_7693,], output)
mod['func_7723'] = func_7723
mod = relay.transform.InferType()(mod)
mutated_mod['func_7723'] = func_7723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7723_call = mutated_mod.get_global_var('func_7723')
var_7725 = relay.var("var_7725", dtype = "float64", shape = ())#candidate|7725|()|var|float64
var_7726 = relay.var("var_7726", dtype = "float64", shape = (8, 1, 4))#candidate|7726|(8, 1, 4)|var|float64
call_7724 = func_7723_call(var_7725,var_7726,)
output = call_7724
func_7727 = relay.Function([var_7725,var_7726,], output)
mutated_mod['func_7727'] = func_7727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3282_call = mod.get_global_var('func_3282')
func_3284_call = mutated_mod.get_global_var('func_3284')
call_7732 = relay.TupleGetItem(func_3282_call(), 0)
call_7733 = relay.TupleGetItem(func_3284_call(), 0)
output = relay.Tuple([call_7732,])
output2 = relay.Tuple([call_7733,])
func_7737 = relay.Function([], output)
mod['func_7737'] = func_7737
mod = relay.transform.InferType()(mod)
output = func_7737()
func_7738 = relay.Function([], output)
mutated_mod['func_7738'] = func_7738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5191_call = mod.get_global_var('func_5191')
func_5192_call = mutated_mod.get_global_var('func_5192')
call_7801 = func_5191_call()
call_7802 = func_5191_call()
func_6261_call = mod.get_global_var('func_6261')
func_6263_call = mutated_mod.get_global_var('func_6263')
call_7829 = relay.TupleGetItem(func_6261_call(), 0)
call_7830 = relay.TupleGetItem(func_6263_call(), 0)
output = relay.Tuple([call_7801,call_7829,])
output2 = relay.Tuple([call_7802,call_7830,])
func_7835 = relay.Function([], output)
mod['func_7835'] = func_7835
mod = relay.transform.InferType()(mod)
mutated_mod['func_7835'] = func_7835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7835_call = mutated_mod.get_global_var('func_7835')
call_7836 = func_7835_call()
output = call_7836
func_7837 = relay.Function([], output)
mutated_mod['func_7837'] = func_7837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1864_call = mod.get_global_var('func_1864')
func_1865_call = mutated_mod.get_global_var('func_1865')
call_7857 = func_1864_call()
call_7858 = func_1864_call()
func_4414_call = mod.get_global_var('func_4414')
func_4417_call = mutated_mod.get_global_var('func_4417')
var_7870 = relay.var("var_7870", dtype = "int16", shape = (60,))#candidate|7870|(60,)|var|int16
call_7869 = relay.TupleGetItem(func_4414_call(relay.reshape(var_7870.astype('int16'), [3, 2, 10])), 0)
call_7871 = relay.TupleGetItem(func_4417_call(relay.reshape(var_7870.astype('int16'), [3, 2, 10])), 0)
func_1040_call = mod.get_global_var('func_1040')
func_1044_call = mutated_mod.get_global_var('func_1044')
const_7876 = relay.const([-7,-5,5,10,-2,5,-2,-8,-2,1,7,-10,7,10,-4,8,-7,2,4,10,-9,-1,8,1,8,-5,-9,-2,8,-4,2,-8,6,3,-3,5,-9,-2,-8,8,-6,3,-9,10,6,4,7,-8,-1,10,-5,-6,1,-3,3,-7,4,4,4,3,-9,9,-8,-6,2,-2,3,3,-8,-5,8,9,1,-7,9,-6,-6,4,-5,-2,-8,-4,-4,7], dtype = "int32")#candidate|7876|(84,)|const|int32
const_7877 = relay.const([-2,5,5,5,2,4,2,-4,-6,9,-6,4,-10,-8,10,-8,-4,-4,-10,3,-2,-1,-6,1,3,-10,8,10,-10,-2,10,3,-6,3,3,-7,2,9,4,8,1,8,-1,7,5,-2,-1,10,-1,3,-10,10,10,-8,3,-2,5,6,-8,-7,-2,9,5,1,2,-1,6,-4,5,1,-9,4,4,-10,-3,-7,-6,-8,-8,9,5,-4,-5,9,10,8,4,-5,-2,-3,10,9,10,8,-8,-10,9,6,-2,-4,7,-4,-5,-1,4,3,-8,1,-10,6,6,-1,-1,8,3,8,5,-1,2,9,-8,9,3,-1,-9,-10,-4,9,-9,-1,-1,2,-4,8,5,-4,-8,-8,-5,5,-8,8,-6,-9,5,9,2,4,4,-4,7,-3,-10,-7,10,8,7,-1,-2,9,-2,-7,-10,10,3,5,9,7,9,-6,-6,-6,-2,-5,7,4,-2,4,2,-8,-6,-6,-10,-8,-7,-7,-3,-5,10,-9,-3,8,6,9,-6,4,1,10,-5,2,5,4,-2,10,8,-1,-4,6,1,-9,-2,10,5,5,-8,-1,-6,-10,-3,-2,-2,1,2,-8,-3,-9,-10,-8,-8,-4,-2,1,9,6,-4,4,-1,-3,-4,-7,8,4,6,-4,9,-5,10,-8,-9,-2,5,10,2,-3,6,5,-6,5,-5,10,-6,4,1,4,8,-3,-1,1,6,-2,-3,-10,10,-3,-4,-8,8,-6,-5,6,-8,8,-2,3,-4,4,-3,-8,-8,7,-4,2,-8,10,9,-9,-7,-6,-10,10,-5,-1,7,-9,-10,8,-3,7,-9,7,7,4,-4,4,9,-8,-6,-3,8,-1,10,4,2,-3,2,-8,7,-2,2,5,-10,8,-1,3,4,-10,3,-6,-9,5,-10,-10,-5,-7,10,10,6,10,-10,-9,-6,9,-6,6,5,-9,-4,-1,3,8,4,5,-8,7,7,2,-6,-5,-5,10,-4,-6,-7,-9,-7,-6,-5,-10,8,-8,-3,10,-3,-6,8,10,-4,-2,3,5,-6,-2,-4,3,8,-6,-4,-4,3,-7,5,-5,-6,-4,-6,-1,-8,5,-3,-3,-10,4,7,-2,10,-3,7,-8,5,-1,8,5,-5,9,9,-1,-5,2,4,4,3,1,-3,4,10,9,9,6,-4,-4,-9,1,-9,-3,9,1,5,6,2,8,-7,-7,-2,-2,8,-9,-10,-8,-7,4,-10,-10,8,3,-5,-9,9,-1,-1,-7,-9,-3,-1,8,3,4,8,8,-9,5,5,6,-1,3,10,-8,-8,-5,-3,-5,-8,4,2,-3,5,4,-3,-4,-7,-4,-8,-3,-5,-5,5,9,-8,3,-4,-10,-6,1,-5,2,1,-9,8,5,-4,2,-10,-5,3,-10,-4,-6,-7,10,1,5,7,2,8,9,-8,1,3,10,-2,2,5,6,4,-5,7,-10,-6,2,-10,5,-5,9,2,3,-2,-10,3,-8,-4,-6,4,7,-6,3,-1,5,-7,-3,4,3,-3,2,10,4,2,7,6,6,-5,10,-1,2,-1,-7,5,2,4,3,-1,-10,-7,-9,-10,-6,7,-9,-5,6,-9,3,-2,1,7,2,1,3,6,2,10,-1,8,-5,4,-8,-4,-7,6,-4,2,-2,-7,-2,10,3,5,-7,3,-5,3,9,4,6,4,4,-8,-8,5,2,-5,3,8,-3,2,-7,9,4,2,7,2,3,-10,-8,10,-10,4,6,-5,-2,-7,4,5,-1,-8,6,-10,1,-7,-6,-9,-5,-2,-7], dtype = "int32")#candidate|7877|(672,)|const|int32
call_7875 = relay.TupleGetItem(func_1040_call(relay.reshape(const_7876.astype('int32'), [1, 7, 12]), relay.reshape(const_7877.astype('int32'), [8, 7, 12]), ), 1)
call_7878 = relay.TupleGetItem(func_1044_call(relay.reshape(const_7876.astype('int32'), [1, 7, 12]), relay.reshape(const_7877.astype('int32'), [8, 7, 12]), ), 1)
output = relay.Tuple([call_7857,call_7869,var_7870,call_7875,const_7876,const_7877,])
output2 = relay.Tuple([call_7858,call_7871,var_7870,call_7878,const_7876,const_7877,])
func_7880 = relay.Function([var_7870,], output)
mod['func_7880'] = func_7880
mod = relay.transform.InferType()(mod)
mutated_mod['func_7880'] = func_7880
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7881 = relay.var("var_7881", dtype = "int16", shape = (60,))#candidate|7881|(60,)|var|int16
func_7880_call = mutated_mod.get_global_var('func_7880')
call_7882 = func_7880_call(var_7881)
output = call_7882
func_7883 = relay.Function([var_7881], output)
mutated_mod['func_7883'] = func_7883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6802_call = mod.get_global_var('func_6802')
func_6803_call = mutated_mod.get_global_var('func_6803')
call_7909 = relay.TupleGetItem(func_6802_call(), 0)
call_7910 = relay.TupleGetItem(func_6803_call(), 0)
output = relay.Tuple([call_7909,])
output2 = relay.Tuple([call_7910,])
func_7913 = relay.Function([], output)
mod['func_7913'] = func_7913
mod = relay.transform.InferType()(mod)
output = func_7913()
func_7914 = relay.Function([], output)
mutated_mod['func_7914'] = func_7914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2783_call = mod.get_global_var('func_2783')
func_2784_call = mutated_mod.get_global_var('func_2784')
call_8010 = relay.TupleGetItem(func_2783_call(), 1)
call_8011 = relay.TupleGetItem(func_2784_call(), 1)
func_5924_call = mod.get_global_var('func_5924')
func_5926_call = mutated_mod.get_global_var('func_5926')
call_8026 = relay.TupleGetItem(func_5924_call(), 2)
call_8027 = relay.TupleGetItem(func_5926_call(), 2)
uop_8055 = relay.sinh(call_8026.astype('float64')) # shape=(4, 5, 1)
uop_8057 = relay.sinh(call_8027.astype('float64')) # shape=(4, 5, 1)
output = relay.Tuple([call_8010,uop_8055,])
output2 = relay.Tuple([call_8011,uop_8057,])
func_8075 = relay.Function([], output)
mod['func_8075'] = func_8075
mod = relay.transform.InferType()(mod)
output = func_8075()
func_8076 = relay.Function([], output)
mutated_mod['func_8076'] = func_8076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6802_call = mod.get_global_var('func_6802')
func_6803_call = mutated_mod.get_global_var('func_6803')
call_8086 = relay.TupleGetItem(func_6802_call(), 0)
call_8087 = relay.TupleGetItem(func_6803_call(), 0)
output = call_8086
output2 = call_8087
func_8089 = relay.Function([], output)
mod['func_8089'] = func_8089
mod = relay.transform.InferType()(mod)
mutated_mod['func_8089'] = func_8089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8089_call = mutated_mod.get_global_var('func_8089')
call_8090 = func_8089_call()
output = call_8090
func_8091 = relay.Function([], output)
mutated_mod['func_8091'] = func_8091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6655_call = mod.get_global_var('func_6655')
func_6657_call = mutated_mod.get_global_var('func_6657')
call_8184 = func_6655_call()
call_8185 = func_6655_call()
func_7560_call = mod.get_global_var('func_7560')
func_7565_call = mutated_mod.get_global_var('func_7565')
const_8187 = relay.const([3,5,-3,-3,-7,-2,-8,9,6], dtype = "uint64")#candidate|8187|(9,)|const|uint64
var_8188 = relay.var("var_8188", dtype = "uint64", shape = (405,))#candidate|8188|(405,)|var|uint64
var_8189 = relay.var("var_8189", dtype = "float32", shape = (18,))#candidate|8189|(18,)|var|float32
call_8186 = relay.TupleGetItem(func_7560_call(relay.reshape(const_8187.astype('uint64'), [1, 1, 9]), relay.reshape(var_8188.astype('uint64'), [15, 3, 9]), relay.reshape(var_8189.astype('float32'), [2, 1, 9]), ), 1)
call_8190 = relay.TupleGetItem(func_7565_call(relay.reshape(const_8187.astype('uint64'), [1, 1, 9]), relay.reshape(var_8188.astype('uint64'), [15, 3, 9]), relay.reshape(var_8189.astype('float32'), [2, 1, 9]), ), 1)
output = relay.Tuple([call_8184,call_8186,const_8187,var_8188,var_8189,])
output2 = relay.Tuple([call_8185,call_8190,const_8187,var_8188,var_8189,])
func_8203 = relay.Function([var_8188,var_8189,], output)
mod['func_8203'] = func_8203
mod = relay.transform.InferType()(mod)
var_8204 = relay.var("var_8204", dtype = "uint64", shape = (405,))#candidate|8204|(405,)|var|uint64
var_8205 = relay.var("var_8205", dtype = "float32", shape = (18,))#candidate|8205|(18,)|var|float32
output = func_8203(var_8204,var_8205,)
func_8206 = relay.Function([var_8204,var_8205,], output)
mutated_mod['func_8206'] = func_8206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7506_call = mod.get_global_var('func_7506')
func_7507_call = mutated_mod.get_global_var('func_7507')
call_8250 = relay.TupleGetItem(func_7506_call(), 0)
call_8251 = relay.TupleGetItem(func_7507_call(), 0)
func_3561_call = mod.get_global_var('func_3561')
func_3564_call = mutated_mod.get_global_var('func_3564')
var_8257 = relay.var("var_8257", dtype = "float64", shape = (108,))#candidate|8257|(108,)|var|float64
call_8256 = func_3561_call(relay.reshape(var_8257.astype('float64'), [3, 6, 6]), relay.reshape(var_8257.astype('float64'), [3, 6, 6]), )
call_8258 = func_3561_call(relay.reshape(var_8257.astype('float64'), [3, 6, 6]), relay.reshape(var_8257.astype('float64'), [3, 6, 6]), )
func_4875_call = mod.get_global_var('func_4875')
func_4878_call = mutated_mod.get_global_var('func_4878')
const_8283 = relay.const([-7,10,7,6,-2,3,3,-9,-9,5,-3,-1,2,-5,-10,3,-3,-5,-2,4,-4,-1,3,7,10,9,3,-2,-1,7,-7,-1,5,5,-9,-3,-8,-9,6,-4,8,-8,5,-7,8,10,-6,10,-6,-9,5,-7,6,-5,4,9,-3,4,-8,4,4,-5,-4,-2,-1,-7,-2,-1,-2,1,6,-7,-6,6,-9,1,-6,-6,1,-3,8,9,4,-8], dtype = "int32")#candidate|8283|(84,)|const|int32
var_8284 = relay.var("var_8284", dtype = "int32", shape = (672,))#candidate|8284|(672,)|var|int32
call_8282 = relay.TupleGetItem(func_4875_call(relay.reshape(const_8283.astype('int32'), [84,]), relay.reshape(var_8284.astype('int32'), [672,]), ), 4)
call_8285 = relay.TupleGetItem(func_4878_call(relay.reshape(const_8283.astype('int32'), [84,]), relay.reshape(var_8284.astype('int32'), [672,]), ), 4)
output = relay.Tuple([call_8250,call_8256,var_8257,call_8282,const_8283,var_8284,])
output2 = relay.Tuple([call_8251,call_8258,var_8257,call_8285,const_8283,var_8284,])
func_8287 = relay.Function([var_8257,var_8284,], output)
mod['func_8287'] = func_8287
mod = relay.transform.InferType()(mod)
mutated_mod['func_8287'] = func_8287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8287_call = mutated_mod.get_global_var('func_8287')
var_8289 = relay.var("var_8289", dtype = "float64", shape = (108,))#candidate|8289|(108,)|var|float64
var_8290 = relay.var("var_8290", dtype = "int32", shape = (672,))#candidate|8290|(672,)|var|int32
call_8288 = func_8287_call(var_8289,var_8290,)
output = call_8288
func_8291 = relay.Function([var_8289,var_8290,], output)
mutated_mod['func_8291'] = func_8291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6788_call = mod.get_global_var('func_6788')
func_6790_call = mutated_mod.get_global_var('func_6790')
call_8377 = relay.TupleGetItem(func_6788_call(), 1)
call_8378 = relay.TupleGetItem(func_6790_call(), 1)
output = relay.Tuple([call_8377,])
output2 = relay.Tuple([call_8378,])
func_8385 = relay.Function([], output)
mod['func_8385'] = func_8385
mod = relay.transform.InferType()(mod)
output = func_8385()
func_8386 = relay.Function([], output)
mutated_mod['func_8386'] = func_8386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1319_call = mod.get_global_var('func_1319')
func_1320_call = mutated_mod.get_global_var('func_1320')
call_8445 = relay.TupleGetItem(func_1319_call(), 0)
call_8446 = relay.TupleGetItem(func_1320_call(), 0)
func_1124_call = mod.get_global_var('func_1124')
func_1130_call = mutated_mod.get_global_var('func_1130')
var_8449 = relay.var("var_8449", dtype = "float64", shape = (165,))#candidate|8449|(165,)|var|float64
const_8450 = relay.const([6,9,6,-2,4,-3,7,-10,-4,-3,5,-7,4,-6,-7,3,-8,5,-4,4,-8,2,-5,-10,-3,-4,-3,-9,-1,9,-9,-9,-3,-1,-3,4,-2,-7,-3,5,-7,6,10,-9,8,8,2,-8,-4,-3,6,8,-6,-6,-9,-6,-10,8,-6,2,9,-5,9,-6,-2,2,8,5,-5,4,-2,4,-3,-5,-1,4,8,1,-3,-2,7,3,6,-1,7,-8,-6,-2,-5,7,-3,-8,-10,-8,-7,8,-6,3,-8,-6,-10,5,-5,6,-3,5,-5,7,-1,10,7,6,-8,-9,1,-1,-8,-10,1,-2,-2,10,-2,-5,-4,-3,-1,-6,7,-5,-1,-1,1,3,-1,8,-3,-1,5,-10,-8,-10,3,10,-3,10,1,4,-5,6,1,-9,2,3,-3,6,9,4,2,-4,9,1,-5,2,10,-6,-1,9,-3,9,-5,-1,1,-6,9,9,4,-8,3,-7,-7,7,-5,9,7,6,-5,8,-10,10,-4,7,-9,7,4,-6,-6,-9,9,1,-8,-10,3,8,2,-5,6,-6,-7,-6,6,4,-7,3,10,2,10,-2,9,8,-9,2,5,10,-1,-4,10,-9,8,-3,-7,-10,-6,-1,4,6,2,-7,-6,-10,-5,5,10,-4,-7,1,-9,-2,3,10,5,-9,4,4,4,6,-6,-7,-7,7,6,-10,8,10,7,1,5,-7,-7,-8,6,-10,-7,1,8,7,-7,-8,1,8,-9,-8,-8,-3,7,-6,7,7,5,-7,-7,8,3,9,-6,-2,6,9,-4,-1,-6,-7,-2,-9,2,1,-2,1,5,-1,-9,-7,-2,2,-1,-8,7,9,10,10,6,1,-10,-5,-4,-9,-7,9,5,7,4,2,-3,-3,-1,-4,4,-4,8,3,-6,-7,9,4,9,9,-7,5,5,10,10,-4,-1,-9,8,3,4,-8,-9,-6,-2,-2,-7,-6,4,10,-1,-6,-5,-1,9,-8,5,-8,6,3,-9,4,1,-10,-7,-6,-7,1,1,6,8,-5,-9,9,4,-3,6,-3,-1,-1,5,7,4,-5,-9,-5,6,2,-10,1,3,-1,5,-10,-6,3,10,5,-7,9,1,3,-3,-3,5,10,-9,-1,-4,-1,3,4,-5,9,9,-7,1,10,-4,8,-8,-1,9,3,2,6,1,9,8,7,-6,-10,4,-1,-6,2,-7,-2,5,-10,1,-2,-5,-10,1,-2,2,3,3,-6,5,2,-1,10,2,-2,-7,7,7,5,-5,-4,1,4], dtype = "int8")#candidate|8450|(480,)|const|int8
const_8451 = relay.const([5,-10,-10,3,-4,-2,-10,-3,1,6,-6,4,-7,7,-1,4,8,4,3,-10,4,5,8,-3,-6,6,-8,-3,-5,8,1,-3,6,-7,-5,-7,-8,3,10,5,-4,1,-1,-9,-7,4,3,-6,-3,9,1,-8,-2,-5,8,-10,2,6,-6,-2,6,-10,1,9,9,5,5,9,8,-10,5,-1,-1,-2,4,1,-8,-8,-7,5,4,-7,5,8], dtype = "int32")#candidate|8451|(84,)|const|int32
const_8452 = relay.const([10,-8,-3,-7,-8,-7,-2,8,-5,8,2,-10,-3,-5,6,9,-10,-6,5,-7,4,-2,10,6,-4,5,-8,-4,-8,2,-3,-10,9,7,9,9,-10,10,10,5,-2,-9,-3,-3,-4,-7,-7,1,4,10,-3,-7,-9,-3,4,-2,-6,1,5,-2,-9,5,7,4,3,-5,2,-9,8,9,-10,2,-1,7,5,5,10,1,-8,-1,10,7,-7,-4,-10,10,-3,6,-5,2,-4,-5,-6,4,-3,5,8,-5,2,-1,-2,10,1,-9,-1,-8,7,9,-4,-9,7,-2,8,1,9,-10,-1,6,8,-10,-8,4,-4,1,6,-6,-4,10,-6,-1,1,5,6,5,9,-3,-6,4,-9,-7,-3,-10,1,-10,-8,-1,-4,2,10,-4,-5,-9,3,10,-8,-9,-1,-9,-8,1,-10,5,-1,-4,6,-3,6,-1,-3,2,-9,-2,9,-3,10,3,6,-4,6,-9,7,-3,-2,-1,-3,-8,-4,-3,2,2,-1,4,2,6,7,2,7,-6,-10,-6,9,-7,4,8,7,-2,4,8,3,5,9,-5,-3,-7,-9,7,-7,-1,-4,1,-10,10,8,-9,1,-2,-1,7,9,6,7,5,8,6,-6,3,-9,-9,2,7,-10,-4,-7,7,-8,-3,-8,10,-6,-10,-5,-8,8,1,-3,-3,-9,-8,-1,4,9,4,-8,5,-1,6,-8,2,2,-5,-6,-10,7,-3,2,-6,7,-8,4,-8,-8,5,-9,-9,-2,5,-3,3,4,8,5,9,-6,6,-2,-7,1,6,10,-10,-10,-10,-4,2,-9,6,-4,6,5,10,-8,-10,10,8,1,-10,-5,-3,3,8,6,8,10,10,7,3,-8,6,-6,5,4,-8,8,-9,7,-7,-1,2,8,-7,3,-2,-2,6,3,-7,9,-10,-7,1,6,8,2,1,6,-5,-7,-8,5,8,7,9,-3,4,7,5,-3,3,6,5,1,9,-9,8,2,6,-1,7,3,3,9,5,4,-7,-3,2,-4,-3,-9,9,-5,3,9,2,-1,1,-7,-2,-6,1,1,3,-6,8,-5,9,1,10,1,-3,-8,-2,1,-6,-3,4,2,-1,4,-4,-8,1,-8,-1,-2,3,9,7,-1,6,-1,10,-10,2,2,-4,-2,2,-5,-8,7,1,7,7,10,-4,6,4,6,-1,-3,-9,-2,-2,-5,-8,-2,-10,6,6,1,-8,-3,2,-8,8,-9,-6,-9,10,9,-6,-4,9,-4,-5,-5,3,-5,9,-9,7,-3,1,-1,6,8,10,-10,3,6,-10,-2,2,7,3,8,8,-4,5,-9,-7,5,-10,-8,1,-10,6,-6,-9,10,1,-3,9,-7,3,5,2,9,7,4,3,10,3,-10,9,4,7,-8,-5,1,2,7,-10,-5,-6,-4,2,-10,8,-9,9,-8,3,5,2,7,5,-7,2,9,-2,7,-7,-10,7,3,-5,4,-8,7,4,3,7,2,1,-7,6,-6,1,9,5,5,6,1,8,-3,3,-4,5,2,-9,8,3,10,10,-3,5,9,7,5,-10,-10,4,5,-1,-7,4,-8,9,-10,-9,-6,-10,6,-4,3,-9,7,8,-5,7,-9,-5,-9,-5,5,-1,-8,3,8,-5,3,5,-7,2,-10,-2,-1,6,-3,-8,-4,-9,-7,8,-2,-6,5,5,-4,4,7,5,-4,7,-9,-8,-3,7,1,-7,8,-10,-7,-5,-3,7,6,7,2,-7,-10,-5,-4,-4,10,10,7,1,4,-8], dtype = "int32")#candidate|8452|(672,)|const|int32
call_8448 = relay.TupleGetItem(func_1124_call(relay.reshape(var_8449.astype('float64'), [11, 5, 3]), relay.reshape(const_8450.astype('int8'), [480,]), relay.reshape(const_8451.astype('int32'), [84, 1]), relay.reshape(const_8452.astype('int32'), [672,]), ), 3)
call_8453 = relay.TupleGetItem(func_1130_call(relay.reshape(var_8449.astype('float64'), [11, 5, 3]), relay.reshape(const_8450.astype('int8'), [480,]), relay.reshape(const_8451.astype('int32'), [84, 1]), relay.reshape(const_8452.astype('int32'), [672,]), ), 3)
func_4101_call = mod.get_global_var('func_4101')
func_4103_call = mutated_mod.get_global_var('func_4103')
call_8464 = func_4101_call()
call_8465 = func_4101_call()
output = relay.Tuple([call_8445,call_8448,var_8449,const_8450,const_8451,const_8452,call_8464,])
output2 = relay.Tuple([call_8446,call_8453,var_8449,const_8450,const_8451,const_8452,call_8465,])
func_8468 = relay.Function([var_8449,], output)
mod['func_8468'] = func_8468
mod = relay.transform.InferType()(mod)
var_8469 = relay.var("var_8469", dtype = "float64", shape = (165,))#candidate|8469|(165,)|var|float64
output = func_8468(var_8469)
func_8470 = relay.Function([var_8469], output)
mutated_mod['func_8470'] = func_8470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2278_call = mod.get_global_var('func_2278')
func_2280_call = mutated_mod.get_global_var('func_2280')
call_8493 = func_2278_call()
call_8494 = func_2278_call()
output = call_8493
output2 = call_8494
func_8500 = relay.Function([], output)
mod['func_8500'] = func_8500
mod = relay.transform.InferType()(mod)
mutated_mod['func_8500'] = func_8500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8500_call = mutated_mod.get_global_var('func_8500')
call_8501 = func_8500_call()
output = call_8501
func_8502 = relay.Function([], output)
mutated_mod['func_8502'] = func_8502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5756_call = mod.get_global_var('func_5756')
func_5757_call = mutated_mod.get_global_var('func_5757')
call_8511 = func_5756_call()
call_8512 = func_5756_call()
func_2724_call = mod.get_global_var('func_2724')
func_2725_call = mutated_mod.get_global_var('func_2725')
call_8521 = func_2724_call()
call_8522 = func_2724_call()
func_1619_call = mod.get_global_var('func_1619')
func_1622_call = mutated_mod.get_global_var('func_1622')
const_8524 = relay.const([5,10,-9,6,-4,-8,-9,-2,2,9,-7,-1,9,-9,4,-1,-2,-6,10,4,-4,2,3,-10,-7,-2,1,-3,-7,-7,8,1,-8,9,-8,-3,9,8,1,-6,-8,5,4,-10,-10,-3,4,6,-10,10,-10,-4,10,9,-1,10,-3,-1,-2,-9,9,-1,-7,-4,4,7,-9,-2,-5,8,8,-7,2,-10,-10,-7,1,1,6,5,1,3,6,-1,-6,7,9,-5,-4,5,3,3,1,2,-9,-7,-2,2,-6,7,2,-8,-1,-1,-9,1,10,8,7,-7,8,9,-6,5,6,6,9,-10,-10,-5,7,2,1,-9,1,-7,9,10,8,9,-1,-1,-10,1,2,-10,-4,-6,-6,3,10,10,-5,7,8,-5,-1,-9,5,-3,-8,6,9,6,9,-3,-9,-8,-3,-8,-1,10,-9,-4,-1,-3,-2,-10,3,6,-5,-8,-2,-7,-5,8,7,-9,8,-1,2,5,-3,5,-1,7,-10,8,-5,-8,1,-6,3,5,9,-8,1,5,10,-1,2,5,-5,3,10,-10,-7,-9,2,-2,9,-3,5,4,9,4,-3,3,-6,10,8,-6,8,3,-1,-2,5,1,-3,-5,2,6,-10,5,-3,-1,7,-4,-7,5,-4,-8,-10,8,6,8,3,-5,-10,1,7,6,3,9,9,-8,8,-1,-5,-4,2,-10,5,-10,-8,-2,-4,9,8,-7,-9,-9,1,5,-7,-8,2,-4,3,-6,6,6,-6,-9,-10,-1,-1,5,-10,-7,-1,8,3,2,7,-9,-6,4,7,-8,10,-5,2,5,2,1,-9,9,-4,-9,9,-5,-2,-8,-4,7,6,7,4,1,5,1,4,7,-1,8,-4,-6,4,7,-10,2,-10,5,-2,-2,-2,-3,3,2,-6,-3,-5,-9,2,-7,-2,-8,7,-6,2,7,1,10,-10,7,5,8,-10,9,3,-6,-4,-7,10,1,1,7,8,7,10,-5,5,-6,-10,-1,-2,8,-1,-6,-10,6,5,-3,-1,-2,-6,7,-2,-8,-8,3,-6,-6,8,10,9,9,-9,8], dtype = "int64")#candidate|8524|(400,)|const|int64
call_8523 = func_1619_call(relay.reshape(const_8524.astype('int64'), [10, 10, 4]))
call_8525 = func_1619_call(relay.reshape(const_8524.astype('int64'), [10, 10, 4]))
output = relay.Tuple([call_8511,call_8521,call_8523,const_8524,])
output2 = relay.Tuple([call_8512,call_8522,call_8525,const_8524,])
func_8531 = relay.Function([], output)
mod['func_8531'] = func_8531
mod = relay.transform.InferType()(mod)
mutated_mod['func_8531'] = func_8531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8531_call = mutated_mod.get_global_var('func_8531')
call_8532 = func_8531_call()
output = call_8532
func_8533 = relay.Function([], output)
mutated_mod['func_8533'] = func_8533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3429_call = mod.get_global_var('func_3429')
func_3431_call = mutated_mod.get_global_var('func_3431')
call_8556 = relay.TupleGetItem(func_3429_call(), 0)
call_8557 = relay.TupleGetItem(func_3431_call(), 0)
output = relay.Tuple([call_8556,])
output2 = relay.Tuple([call_8557,])
func_8571 = relay.Function([], output)
mod['func_8571'] = func_8571
mod = relay.transform.InferType()(mod)
output = func_8571()
func_8572 = relay.Function([], output)
mutated_mod['func_8572'] = func_8572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2376_call = mod.get_global_var('func_2376')
func_2378_call = mutated_mod.get_global_var('func_2378')
call_8666 = relay.TupleGetItem(func_2376_call(), 0)
call_8667 = relay.TupleGetItem(func_2378_call(), 0)
func_8571_call = mod.get_global_var('func_8571')
func_8572_call = mutated_mod.get_global_var('func_8572')
call_8668 = relay.TupleGetItem(func_8571_call(), 0)
call_8669 = relay.TupleGetItem(func_8572_call(), 0)
func_6179_call = mod.get_global_var('func_6179')
func_6180_call = mutated_mod.get_global_var('func_6180')
call_8680 = relay.TupleGetItem(func_6179_call(), 0)
call_8681 = relay.TupleGetItem(func_6180_call(), 0)
func_3429_call = mod.get_global_var('func_3429')
func_3431_call = mutated_mod.get_global_var('func_3431')
call_8682 = relay.TupleGetItem(func_3429_call(), 1)
call_8683 = relay.TupleGetItem(func_3431_call(), 1)
output = relay.Tuple([call_8666,call_8668,call_8680,call_8682,])
output2 = relay.Tuple([call_8667,call_8669,call_8681,call_8683,])
func_8688 = relay.Function([], output)
mod['func_8688'] = func_8688
mod = relay.transform.InferType()(mod)
mutated_mod['func_8688'] = func_8688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8688_call = mutated_mod.get_global_var('func_8688')
call_8689 = func_8688_call()
output = call_8689
func_8690 = relay.Function([], output)
mutated_mod['func_8690'] = func_8690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8531_call = mod.get_global_var('func_8531')
func_8533_call = mutated_mod.get_global_var('func_8533')
call_8724 = relay.TupleGetItem(func_8531_call(), 2)
call_8725 = relay.TupleGetItem(func_8533_call(), 2)
uop_8740 = relay.log10(call_8724.astype('float32')) # shape=(10, 10, 4)
uop_8742 = relay.log10(call_8725.astype('float32')) # shape=(10, 10, 4)
func_4634_call = mod.get_global_var('func_4634')
func_4636_call = mutated_mod.get_global_var('func_4636')
var_8747 = relay.var("var_8747", dtype = "float32", shape = (1, 1350))#candidate|8747|(1, 1350)|var|float32
call_8746 = relay.TupleGetItem(func_4634_call(relay.reshape(var_8747.astype('float32'), [15, 15, 6])), 0)
call_8748 = relay.TupleGetItem(func_4636_call(relay.reshape(var_8747.astype('float32'), [15, 15, 6])), 0)
output = relay.Tuple([uop_8740,call_8746,var_8747,])
output2 = relay.Tuple([uop_8742,call_8748,var_8747,])
func_8752 = relay.Function([var_8747,], output)
mod['func_8752'] = func_8752
mod = relay.transform.InferType()(mod)
var_8753 = relay.var("var_8753", dtype = "float32", shape = (1, 1350))#candidate|8753|(1, 1350)|var|float32
output = func_8752(var_8753)
func_8754 = relay.Function([var_8753], output)
mutated_mod['func_8754'] = func_8754
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8762 = relay.var("var_8762", dtype = "uint16", shape = (1, 5, 5))#candidate|8762|(1, 5, 5)|var|uint16
var_8763 = relay.var("var_8763", dtype = "uint16", shape = (8, 5, 5))#candidate|8763|(8, 5, 5)|var|uint16
bop_8764 = relay.greater_equal(var_8762.astype('bool'), var_8763.astype('bool')) # shape=(8, 5, 5)
output = bop_8764
output2 = bop_8764
func_8777 = relay.Function([var_8762,var_8763,], output)
mod['func_8777'] = func_8777
mod = relay.transform.InferType()(mod)
var_8778 = relay.var("var_8778", dtype = "uint16", shape = (1, 5, 5))#candidate|8778|(1, 5, 5)|var|uint16
var_8779 = relay.var("var_8779", dtype = "uint16", shape = (8, 5, 5))#candidate|8779|(8, 5, 5)|var|uint16
output = func_8777(var_8778,var_8779,)
func_8780 = relay.Function([var_8778,var_8779,], output)
mutated_mod['func_8780'] = func_8780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2278_call = mod.get_global_var('func_2278')
func_2280_call = mutated_mod.get_global_var('func_2280')
call_8846 = func_2278_call()
call_8847 = func_2278_call()
func_4414_call = mod.get_global_var('func_4414')
func_4417_call = mutated_mod.get_global_var('func_4417')
var_8851 = relay.var("var_8851", dtype = "int16", shape = (60,))#candidate|8851|(60,)|var|int16
call_8850 = relay.TupleGetItem(func_4414_call(relay.reshape(var_8851.astype('int16'), [3, 2, 10])), 0)
call_8852 = relay.TupleGetItem(func_4417_call(relay.reshape(var_8851.astype('int16'), [3, 2, 10])), 0)
func_4414_call = mod.get_global_var('func_4414')
func_4417_call = mutated_mod.get_global_var('func_4417')
call_8871 = relay.TupleGetItem(func_4414_call(relay.reshape(var_8851.astype('int16'), [3, 2, 10])), 0)
call_8872 = relay.TupleGetItem(func_4417_call(relay.reshape(var_8851.astype('int16'), [3, 2, 10])), 0)
output = relay.Tuple([call_8846,call_8850,var_8851,call_8871,])
output2 = relay.Tuple([call_8847,call_8852,var_8851,call_8872,])
func_8880 = relay.Function([var_8851,], output)
mod['func_8880'] = func_8880
mod = relay.transform.InferType()(mod)
mutated_mod['func_8880'] = func_8880
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8881 = relay.var("var_8881", dtype = "int16", shape = (60,))#candidate|8881|(60,)|var|int16
func_8880_call = mutated_mod.get_global_var('func_8880')
call_8882 = func_8880_call(var_8881)
output = call_8882
func_8883 = relay.Function([var_8881], output)
mutated_mod['func_8883'] = func_8883
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8906 = relay.var("var_8906", dtype = "float64", shape = (2, 8, 10))#candidate|8906|(2, 8, 10)|var|float64
var_8907 = relay.var("var_8907", dtype = "float64", shape = (2, 8, 10))#candidate|8907|(2, 8, 10)|var|float64
bop_8908 = relay.divide(var_8906.astype('float64'), relay.reshape(var_8907.astype('float64'), relay.shape_of(var_8906))) # shape=(2, 8, 10)
func_76_call = mod.get_global_var('func_76')
func_79_call = mutated_mod.get_global_var('func_79')
const_8912 = relay.const([[False,True,True,True,True,True,True,False,True,True,True,True,True,False,True,True,False,True,True,True,True,False,True,False,True,False,True,False,False,False,False,False,True,True,False,False,False,True,True,False,False,False,True,True,True,True,False,True,False,True,False,True,False,True,False,True,True,True,False,True,False,False,False,True,True,False,False,False,True,True,False,True,True,True,False,False,False,True,True,True,False,False,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,True,True,True,False,True,False,False,True,True,False,True,False,False,False,False,False,True,True,True,True,True,False,True,True,True,True,True,True,True,False,False,False,False,True,True,True,False,True,False,True,True,False,True,True,False,True,True,True,False,True,True,True,True,False,False,False,False,True,False,True,False,False,True,False,True,False,True,True,True,False,False,True,False,True,False,False,True,False,False,True,True,True,True,False,True,True,True,True,True,True,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,True,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,True,True,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,False,False,True,False,False,True,False,True,True,True,True,False,True,False,True,False,False,True,False,True,True,False,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,False,False,True,True,False,True,False,False,True,False,True,False,False,False,True,False,True,False,False,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True,False,False,True,False,True,False,False,False,False,False,False,True,False,True,True,False,True,True,True,True,True,False,False,False,True,True,False,True,False,True,True,False,True,False,False,False,False,False,False,False,False,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,True,True],[True,True,False,False,True,False,False,True,False,False,True,True,False,True,True,True,False,True,True,True,True,False,True,True,True,False,False,False,False,True,True,True,True,False,False,False,False,False,False,False,True,True,True,True,True,True,True,True,False,False,False,True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,False,False,True,True,True,True,True,False,False,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,True,False,True,False,False,False,False,False,True,True,False,False,False,True,False,True,False,False,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,True,True,True,False,True,True,True,False,True,True,True,True,True,False,True,True,True,False,False,True,True,True,True,True,True,True,True,False,True,True,True,True,False,False,True,False,True,False,False,True,True,True,False,False,True,True,False,True,False,False,False,True,True,False,True,True,True,False,True,False,True,False,True,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,False,False,True,True,True,True,False,False,False,True,True,False,False,True,False,False,True,False,False,True,True,True,True,False,True,False,False,False,False,False,True,False,False,False,True,False,True,False,False,True,True,False,True,True,True,True,False,True,False,False,False,True,True,True,True,False,True,False,True,True,False,False,True,True,False,True,True,True,True,True,False,False,True,True,True,True,True,True,False,True,False,False,False,True,True,True,False,True,True,True,False,False,True,False,True,True,True,False,False,False,True,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,True,False,False,True,True,True,False,True,True,False,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,False,False,True],[False,False,False,False,False,False,True,True,False,False,True,False,False,False,True,False,True,False,False,False,True,False,True,True,False,False,False,False,False,False,True,True,False,True,True,False,True,False,False,True,True,True,True,True,True,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,False,False,False,True,True,False,False,True,False,True,False,True,False,False,False,False,False,True,True,False,False,True,True,False,False,False,False,False,True,True,True,True,True,True,False,False,False,False,False,False,True,False,False,True,False,False,False,False,True,True,True,True,False,False,True,False,True,False,False,False,True,False,False,True,True,False,True,True,True,True,False,False,False,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,False,False,False,False,False,True,True,False,True,True,True,False,True,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,True,False,True,True,False,True,True,False,True,True,False,False,False,False,False,True,False,True,False,False,False,True,False,False,True,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,True,True,False,True,False,True,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,True,False,True,True,False,True,True,True,True,True,False,False,False,True,False,True,False,True,True,True,False,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,False,True,True,True,False,True,False,False,False,False,False,False,False,True,True,False,True,True,False,True,True,False,True,False,False,True,True,False,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,False,True,True,False,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,False,False,False,False,False,True,False,True,False,True,True,False,False,False,True,False,True,True,True,True,False,True,True,False],[False,True,False,False,True,True,False,True,True,True,True,False,False,True,True,True,True,False,True,True,True,True,True,False,False,False,True,True,False,False,True,False,False,False,True,True,True,True,False,False,False,True,False,True,False,True,False,True,False,True,False,True,False,True,True,True,False,True,False,False,True,True,False,True,True,True,False,False,True,False,True,True,True,True,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False,False,False,True,False,False,False,True,True,True,True,True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,False,True,True,True,True,False,False,False,False,False,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,True,True,True,True,True,True,False,False,False,True,True,True,False,False,True,False,True,False,True,True,False,False,True,False,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,True,True,False,False,True,False,True,True,True,True,False,True,False,True,False,False,False,False,False,True,True,True,True,True,False,True,True,False,False,True,True,True,True,True,False,False,True,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,True,False,False,True,True,False,False,True,True,True,True,False,False,True,True,True,False,True,True,True,True,True,False,True,True,False,True,True,True,False,False,False,False,False,False,False,False,False,True,False,True,False,False,True,True,True,False,False,False,True,True,False,False,False,True,True,False,False,False,True,False,False,False,False,True,False,False,True,False,False,True,True,False,False,False,False,True,False,False,False,True,True,False,False,True,True,True,True,True,False,True,True,False,True,True,True,True,False,True,True,False,False,False,False,False,False,False,False,False,False,False,True],[False,False,True,True,True,True,True,False,True,False,True,True,True,False,True,False,False,False,True,False,False,True,True,True,True,True,True,True,False,True,False,False,True,False,True,False,True,False,False,False,False,True,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,True,True,False,False,True,True,False,False,True,True,True,True,True,True,False,False,True,True,True,False,True,True,True,False,False,False,True,False,True,False,True,False,True,True,False,False,False,False,True,True,True,False,False,False,True,False,True,False,False,False,True,True,True,False,True,False,False,True,False,True,True,False,False,True,True,False,True,False,True,False,True,False,False,False,True,False,False,False,False,False,False,True,False,True,True,True,True,False,False,False,True,False,False,True,True,True,False,False,True,True,True,True,True,True,True,False,True,True,False,False,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,True,True,False,True,False,True,False,True,False,False,False,True,True,False,True,True,False,False,True,False,False,False,True,True,True,True,True,True,True,False,True,False,True,True,False,False,False,False,True,True,False,False,False,False,False,True,True,False,True,False,False,True,False,True,True,True,True,False,True,False,False,False,True,False,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,False,False,True,False,False,True,True,False,False,True,True,False,True,True,True,True,True,False,True,False,False,True,True,False,False,True,False,False,False,True,True,False,True,True,False,False,False,True,False,False,False,True,False,False,False,False,True,False,False,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,True,False,False,True,False,False,False,True,False,True,True,True,True,True,True,False,True,False,False,False,True,True,False,False],[False,False,True,False,True,True,True,False,True,True,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,True,True,False,False,True,False,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False,False,False,True,True,False,False,True,True,True,True,True,False,False,True,False,False,True,True,False,True,False,False,False,False,False,True,False,True,False,False,True,True,False,False,False,True,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,True,False,True,True,False,False,False,True,True,False,True,False,False,True,False,True,False,True,True,False,False,True,False,False,True,True,False,True,False,False,False,False,False,True,True,False,False,True,True,True,True,False,True,False,False,True,True,False,False,True,False,True,False,False,True,True,True,True,True,False,True,True,False,True,True,True,True,True,True,False,False,False,True,True,False,True,False,False,True,False,True,True,True,True,True,False,False,True,True,True,True,False,True,True,True,False,False,False,True,True,True,True,False,False,False,False,True,False,False,False,False,True,True,False,False,False,False,True,True,False,False,False,False,True,True,False,True,False,False,False,True,True,True,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,True,True,False,False,False,True,True,True,True,True,True,True,True,True,True,True,False,False,False,False,True,False,True,True,False,True,True,False,True,True,False,True,False,True,True,False,False,False,False,True,True,True,False,True,False,True,False,True,False,False,True,True,False,False,False,False,True,True,False,True,False,True,False,True,False,True,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,True,False,False,True,False,False,False,True,False,True,True,True,True,False,True,True,True,False,False,False,True,True,False,True,False,False,True],[True,True,True,True,False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,False,True,True,False,False,True,False,False,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,True,True,False,False,True,False,True,True,False,True,False,False,True,True,True,False,False,True,True,False,True,True,False,True,False,False,False,True,True,False,True,True,False,True,True,True,False,False,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,True,False,True,True,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,False,False,True,True,False,False,False,True,True,False,True,False,False,True,False,False,False,False,True,True,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,False,True,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,False,False,False,False,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,False,False,False,False,False,False,False,True,False,True,False,False,True,False,True,True,True,True,True,True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,True,False,True,True,True,False,False,True,False,True,True,True,False,False,True,False,False,False,True,False,True,False,False,True,True,True,False,False,False,False,False,True,False,True,False,True,True,False,False,False,False,True,True,False,False,False,False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,True,True,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,False,False,False,True,True,True,False,True,False],[False,False,True,True,True,False,False,False,False,True,True,False,True,True,True,True,True,True,False,True,False,True,True,False,True,True,True,False,True,True,False,True,True,True,True,False,True,True,False,True,False,False,True,False,True,True,True,False,False,True,True,False,False,True,True,False,False,False,False,True,True,True,True,True,False,False,True,False,True,False,True,False,False,True,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,False,False,True,True,False,True,False,False,False,False,False,True,False,False,True,True,False,True,False,True,False,False,False,True,False,False,True,False,False,False,True,False,False,True,True,False,False,True,False,False,True,False,True,True,False,False,True,False,True,True,False,True,False,False,True,False,False,False,False,False,False,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,False,True,False,True,True,False,True,True,True,False,True,True,False,True,True,False,True,True,True,False,True,False,False,True,True,False,True,False,True,False,True,True,False,True,False,True,True,False,True,False,False,False,True,False,False,False,True,True,True,False,False,False,True,False,True,False,False,True,False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,False,True,False,True,False,False,False,True,False,True,False,False,False,False,True,True,True,False,True,False,True,False,True,False,True,False,True,True,True,False,False,True,True,False,False,False,False,True,True,False,False,True,True,False,True,False,False,False,False,True,True,True,True,False,True,True,False,False,False,True,False,False,True,False,True,True,False,True,False,True,False,False,False,True,True,True,True,True,False,True,False,True,True,True,True,False,False,False,True,True,True,True,True,False,True,False,False,True,False,False,False,False,True,False,True,False,False,False,True,False,True]], dtype = "bool")#candidate|8912|(8, 364)|const|bool
call_8911 = func_76_call(relay.reshape(const_8912.astype('bool'), [13, 16, 14]))
call_8913 = func_76_call(relay.reshape(const_8912.astype('bool'), [13, 16, 14]))
output = relay.Tuple([bop_8908,call_8911,const_8912,])
output2 = relay.Tuple([bop_8908,call_8913,const_8912,])
func_8926 = relay.Function([var_8906,var_8907,], output)
mod['func_8926'] = func_8926
mod = relay.transform.InferType()(mod)
mutated_mod['func_8926'] = func_8926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8926_call = mutated_mod.get_global_var('func_8926')
var_8928 = relay.var("var_8928", dtype = "float64", shape = (2, 8, 10))#candidate|8928|(2, 8, 10)|var|float64
var_8929 = relay.var("var_8929", dtype = "float64", shape = (2, 8, 10))#candidate|8929|(2, 8, 10)|var|float64
call_8927 = func_8926_call(var_8928,var_8929,)
output = call_8927
func_8930 = relay.Function([var_8928,var_8929,], output)
mutated_mod['func_8930'] = func_8930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1915_call = mod.get_global_var('func_1915')
func_1916_call = mutated_mod.get_global_var('func_1916')
call_9008 = func_1915_call()
call_9009 = func_1915_call()
output = call_9008
output2 = call_9009
func_9029 = relay.Function([], output)
mod['func_9029'] = func_9029
mod = relay.transform.InferType()(mod)
mutated_mod['func_9029'] = func_9029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9029_call = mutated_mod.get_global_var('func_9029')
call_9030 = func_9029_call()
output = call_9030
func_9031 = relay.Function([], output)
mutated_mod['func_9031'] = func_9031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1319_call = mod.get_global_var('func_1319')
func_1320_call = mutated_mod.get_global_var('func_1320')
call_9032 = relay.TupleGetItem(func_1319_call(), 0)
call_9033 = relay.TupleGetItem(func_1320_call(), 0)
output = relay.Tuple([call_9032,])
output2 = relay.Tuple([call_9033,])
func_9090 = relay.Function([], output)
mod['func_9090'] = func_9090
mod = relay.transform.InferType()(mod)
output = func_9090()
func_9091 = relay.Function([], output)
mutated_mod['func_9091'] = func_9091
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9142 = relay.var("var_9142", dtype = "float32", shape = (3, 3, 15))#candidate|9142|(3, 3, 15)|var|float32
uop_9143 = relay.acosh(var_9142.astype('float32')) # shape=(3, 3, 15)
output = uop_9143
output2 = uop_9143
func_9147 = relay.Function([var_9142,], output)
mod['func_9147'] = func_9147
mod = relay.transform.InferType()(mod)
mutated_mod['func_9147'] = func_9147
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9148 = relay.var("var_9148", dtype = "float32", shape = (3, 3, 15))#candidate|9148|(3, 3, 15)|var|float32
func_9147_call = mutated_mod.get_global_var('func_9147')
call_9149 = func_9147_call(var_9148)
output = call_9149
func_9150 = relay.Function([var_9148], output)
mutated_mod['func_9150'] = func_9150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9029_call = mod.get_global_var('func_9029')
func_9031_call = mutated_mod.get_global_var('func_9031')
call_9152 = func_9029_call()
call_9153 = func_9029_call()
output = call_9152
output2 = call_9153
func_9160 = relay.Function([], output)
mod['func_9160'] = func_9160
mod = relay.transform.InferType()(mod)
mutated_mod['func_9160'] = func_9160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9160_call = mutated_mod.get_global_var('func_9160')
call_9161 = func_9160_call()
output = call_9161
func_9162 = relay.Function([], output)
mutated_mod['func_9162'] = func_9162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3994_call = mod.get_global_var('func_3994')
func_3995_call = mutated_mod.get_global_var('func_3995')
call_9182 = func_3994_call()
call_9183 = func_3994_call()
output = call_9182
output2 = call_9183
func_9184 = relay.Function([], output)
mod['func_9184'] = func_9184
mod = relay.transform.InferType()(mod)
mutated_mod['func_9184'] = func_9184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9184_call = mutated_mod.get_global_var('func_9184')
call_9185 = func_9184_call()
output = call_9185
func_9186 = relay.Function([], output)
mutated_mod['func_9186'] = func_9186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7737_call = mod.get_global_var('func_7737')
func_7738_call = mutated_mod.get_global_var('func_7738')
call_9243 = relay.TupleGetItem(func_7737_call(), 0)
call_9244 = relay.TupleGetItem(func_7738_call(), 0)
func_7506_call = mod.get_global_var('func_7506')
func_7507_call = mutated_mod.get_global_var('func_7507')
call_9262 = relay.TupleGetItem(func_7506_call(), 0)
call_9263 = relay.TupleGetItem(func_7507_call(), 0)
output = relay.Tuple([call_9243,call_9262,])
output2 = relay.Tuple([call_9244,call_9263,])
func_9268 = relay.Function([], output)
mod['func_9268'] = func_9268
mod = relay.transform.InferType()(mod)
mutated_mod['func_9268'] = func_9268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9268_call = mutated_mod.get_global_var('func_9268')
call_9269 = func_9268_call()
output = call_9269
func_9270 = relay.Function([], output)
mutated_mod['func_9270'] = func_9270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9184_call = mod.get_global_var('func_9184')
func_9186_call = mutated_mod.get_global_var('func_9186')
call_9292 = func_9184_call()
call_9293 = func_9184_call()
uop_9330 = relay.asinh(call_9292.astype('float32')) # shape=(4, 15, 15)
uop_9332 = relay.asinh(call_9293.astype('float32')) # shape=(4, 15, 15)
func_6568_call = mod.get_global_var('func_6568')
func_6569_call = mutated_mod.get_global_var('func_6569')
call_9352 = relay.TupleGetItem(func_6568_call(), 1)
call_9353 = relay.TupleGetItem(func_6569_call(), 1)
output = relay.Tuple([uop_9330,call_9352,])
output2 = relay.Tuple([uop_9332,call_9353,])
func_9365 = relay.Function([], output)
mod['func_9365'] = func_9365
mod = relay.transform.InferType()(mod)
output = func_9365()
func_9366 = relay.Function([], output)
mutated_mod['func_9366'] = func_9366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4918_call = mod.get_global_var('func_4918')
func_4920_call = mutated_mod.get_global_var('func_4920')
call_9464 = relay.TupleGetItem(func_4918_call(), 0)
call_9465 = relay.TupleGetItem(func_4920_call(), 0)
output = call_9464
output2 = call_9465
func_9472 = relay.Function([], output)
mod['func_9472'] = func_9472
mod = relay.transform.InferType()(mod)
output = func_9472()
func_9473 = relay.Function([], output)
mutated_mod['func_9473'] = func_9473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6976_call = mod.get_global_var('func_6976')
func_6977_call = mutated_mod.get_global_var('func_6977')
call_9480 = func_6976_call()
call_9481 = func_6976_call()
func_5191_call = mod.get_global_var('func_5191')
func_5192_call = mutated_mod.get_global_var('func_5192')
call_9492 = func_5191_call()
call_9493 = func_5191_call()
func_7913_call = mod.get_global_var('func_7913')
func_7914_call = mutated_mod.get_global_var('func_7914')
call_9502 = relay.TupleGetItem(func_7913_call(), 0)
call_9503 = relay.TupleGetItem(func_7914_call(), 0)
func_6671_call = mod.get_global_var('func_6671')
func_6672_call = mutated_mod.get_global_var('func_6672')
call_9509 = relay.TupleGetItem(func_6671_call(), 1)
call_9510 = relay.TupleGetItem(func_6672_call(), 1)
func_8089_call = mod.get_global_var('func_8089')
func_8091_call = mutated_mod.get_global_var('func_8091')
call_9517 = func_8089_call()
call_9518 = func_8089_call()
output = relay.Tuple([call_9480,call_9492,call_9502,call_9509,call_9517,])
output2 = relay.Tuple([call_9481,call_9493,call_9503,call_9510,call_9518,])
func_9519 = relay.Function([], output)
mod['func_9519'] = func_9519
mod = relay.transform.InferType()(mod)
output = func_9519()
func_9520 = relay.Function([], output)
mutated_mod['func_9520'] = func_9520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5802_call = mod.get_global_var('func_5802')
func_5803_call = mutated_mod.get_global_var('func_5803')
call_9524 = relay.TupleGetItem(func_5802_call(), 0)
call_9525 = relay.TupleGetItem(func_5803_call(), 0)
func_4145_call = mod.get_global_var('func_4145')
func_4149_call = mutated_mod.get_global_var('func_4149')
var_9530 = relay.var("var_9530", dtype = "int16", shape = (324,))#candidate|9530|(324,)|var|int16
call_9529 = relay.TupleGetItem(func_4145_call(relay.reshape(var_9530.astype('int16'), [3, 12, 9]), relay.reshape(var_9530.astype('int16'), [3, 12, 9]), ), 2)
call_9531 = relay.TupleGetItem(func_4149_call(relay.reshape(var_9530.astype('int16'), [3, 12, 9]), relay.reshape(var_9530.astype('int16'), [3, 12, 9]), ), 2)
func_6382_call = mod.get_global_var('func_6382')
func_6384_call = mutated_mod.get_global_var('func_6384')
call_9533 = relay.TupleGetItem(func_6382_call(), 4)
call_9534 = relay.TupleGetItem(func_6384_call(), 4)
uop_9537 = relay.rsqrt(var_9530.astype('float32')) # shape=(324,)
func_9090_call = mod.get_global_var('func_9090')
func_9091_call = mutated_mod.get_global_var('func_9091')
call_9559 = relay.TupleGetItem(func_9090_call(), 0)
call_9560 = relay.TupleGetItem(func_9091_call(), 0)
func_9519_call = mod.get_global_var('func_9519')
func_9520_call = mutated_mod.get_global_var('func_9520')
call_9578 = relay.TupleGetItem(func_9519_call(), 2)
call_9579 = relay.TupleGetItem(func_9520_call(), 2)
output = relay.Tuple([call_9524,call_9529,call_9533,uop_9537,call_9559,call_9578,])
output2 = relay.Tuple([call_9525,call_9531,call_9534,uop_9537,call_9560,call_9579,])
func_9580 = relay.Function([var_9530,], output)
mod['func_9580'] = func_9580
mod = relay.transform.InferType()(mod)
var_9581 = relay.var("var_9581", dtype = "int16", shape = (324,))#candidate|9581|(324,)|var|int16
output = func_9580(var_9581)
func_9582 = relay.Function([var_9581], output)
mutated_mod['func_9582'] = func_9582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7069_call = mod.get_global_var('func_7069')
func_7071_call = mutated_mod.get_global_var('func_7071')
call_9629 = func_7069_call()
call_9630 = func_7069_call()
output = call_9629
output2 = call_9630
func_9642 = relay.Function([], output)
mod['func_9642'] = func_9642
mod = relay.transform.InferType()(mod)
output = func_9642()
func_9643 = relay.Function([], output)
mutated_mod['func_9643'] = func_9643
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9647 = relay.const(7, dtype = "uint8")#candidate|9647|()|const|uint8
var_9648 = relay.var("var_9648", dtype = "uint8", shape = (11, 6, 12))#candidate|9648|(11, 6, 12)|var|uint8
bop_9649 = relay.greater(const_9647.astype('bool'), var_9648.astype('bool')) # shape=(11, 6, 12)
func_4434_call = mod.get_global_var('func_4434')
func_4435_call = mutated_mod.get_global_var('func_4435')
call_9659 = relay.TupleGetItem(func_4434_call(), 1)
call_9660 = relay.TupleGetItem(func_4435_call(), 1)
func_9160_call = mod.get_global_var('func_9160')
func_9162_call = mutated_mod.get_global_var('func_9162')
call_9668 = func_9160_call()
call_9669 = func_9160_call()
func_2446_call = mod.get_global_var('func_2446')
func_2448_call = mutated_mod.get_global_var('func_2448')
call_9670 = relay.TupleGetItem(func_2446_call(), 1)
call_9671 = relay.TupleGetItem(func_2448_call(), 1)
func_4145_call = mod.get_global_var('func_4145')
func_4149_call = mutated_mod.get_global_var('func_4149')
var_9687 = relay.var("var_9687", dtype = "int16", shape = (324,))#candidate|9687|(324,)|var|int16
call_9686 = relay.TupleGetItem(func_4145_call(relay.reshape(var_9687.astype('int16'), [3, 12, 9]), relay.reshape(var_9687.astype('int16'), [3, 12, 9]), ), 2)
call_9688 = relay.TupleGetItem(func_4149_call(relay.reshape(var_9687.astype('int16'), [3, 12, 9]), relay.reshape(var_9687.astype('int16'), [3, 12, 9]), ), 2)
output = relay.Tuple([bop_9649,call_9659,call_9668,call_9670,call_9686,var_9687,])
output2 = relay.Tuple([bop_9649,call_9660,call_9669,call_9671,call_9688,var_9687,])
func_9695 = relay.Function([var_9648,var_9687,], output)
mod['func_9695'] = func_9695
mod = relay.transform.InferType()(mod)
var_9696 = relay.var("var_9696", dtype = "uint8", shape = (11, 6, 12))#candidate|9696|(11, 6, 12)|var|uint8
var_9697 = relay.var("var_9697", dtype = "int16", shape = (324,))#candidate|9697|(324,)|var|int16
output = func_9695(var_9696,var_9697,)
func_9698 = relay.Function([var_9696,var_9697,], output)
mutated_mod['func_9698'] = func_9698
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9721 = relay.var("var_9721", dtype = "int8", shape = (11, 2, 15))#candidate|9721|(11, 2, 15)|var|int8
var_9722 = relay.var("var_9722", dtype = "int8", shape = (11, 2, 15))#candidate|9722|(11, 2, 15)|var|int8
bop_9723 = relay.greater(var_9721.astype('bool'), relay.reshape(var_9722.astype('bool'), relay.shape_of(var_9721))) # shape=(11, 2, 15)
func_4145_call = mod.get_global_var('func_4145')
func_4149_call = mutated_mod.get_global_var('func_4149')
const_9733 = relay.const([4,-6,-4,-5,9,8,-10,-6,-6,8,5,10,-3,10,-7,-2,4,3,4,6,-2,9,-9,-6,-9,-1,-10,-8,5,8,-2,3,10,-3,8,10,-4,-3,4,-5,6,9,8,-8,-7,7,9,-5,-7,-5,-6,4,4,4,-7,-2,7,-8,9,10,-2,-5,-8,-10,-9,-10,2,8,1,5,-10,-10,10,-4,2,7,2,5,-4,-4,3,-9,-6,-2,-6,-5,-6,5,-1,-7,4,8,-7,5,9,-4,3,-7,10,-6,-6,7,5,8,-1,-10,-8,-1,3,-6,-5,-7,6,7,-3,4,-5,-3,-3,8,-7,-6,-1,10,5,8,-8,8,9,10,10,3,-7,8,7,-1,-6,-1,-6,-1,-9,-10,-4,-9,-6,4,4,-3,-4,-8,-9,-7,-6,2,-9,2,9,-5,10,7,4,2,-1,-9,-8,-5,-8,1,-3,7,-5,-2,-8,-9,-2,4,8,-5,3,-3,3,-9,2,-6,-5,9,-3,-4,7,-1,8,6,-1,6,-7,8,-8,-2,9,5,4,-3,4,-7,-1,-1,-4,-6,8,-1,-10,6,6,-8,9,-10,-9,9,10,-6,4,9,-4,5,6,6,4,4,3,8,7,-4,-1,-10,9,-10,-3,1,4,9,1,-8,9,-9,-5,-2,-5,7,-9,6,4,1,7,-5,9,2,9,-6,-3,-9,-2,-9,9,-10,6,4,-2,-7,8,-9,-6,-6,-5,1,7,-6,-5,3,-2,2,-9,-8,-3,1,9,-6,-4,-9,-5,5,-4,-1,8,1,-9,8,9,-10,-4,-4,10,9,-2,-1,1,-9,8,2,-3,6,7,-9,-3,-1,-9,-2,-4,-5,9,3,5,-5,-1,-9], dtype = "int16")#candidate|9733|(324,)|const|int16
call_9732 = relay.TupleGetItem(func_4145_call(relay.reshape(const_9733.astype('int16'), [3, 12, 9]), relay.reshape(const_9733.astype('int16'), [3, 12, 9]), ), 1)
call_9734 = relay.TupleGetItem(func_4149_call(relay.reshape(const_9733.astype('int16'), [3, 12, 9]), relay.reshape(const_9733.astype('int16'), [3, 12, 9]), ), 1)
func_7314_call = mod.get_global_var('func_7314')
func_7315_call = mutated_mod.get_global_var('func_7315')
call_9737 = relay.TupleGetItem(func_7314_call(), 0)
call_9738 = relay.TupleGetItem(func_7315_call(), 0)
func_4094_call = mod.get_global_var('func_4094')
func_4095_call = mutated_mod.get_global_var('func_4095')
call_9739 = relay.TupleGetItem(func_4094_call(), 0)
call_9740 = relay.TupleGetItem(func_4095_call(), 0)
func_8089_call = mod.get_global_var('func_8089')
func_8091_call = mutated_mod.get_global_var('func_8091')
call_9743 = func_8089_call()
call_9744 = func_8089_call()
bop_9753 = relay.multiply(var_9722.astype('uint8'), call_9732.astype('uint8')) # shape=(11, 2, 15)
bop_9756 = relay.multiply(var_9722.astype('uint8'), call_9734.astype('uint8')) # shape=(11, 2, 15)
output = relay.Tuple([bop_9723,const_9733,call_9737,call_9739,call_9743,bop_9753,])
output2 = relay.Tuple([bop_9723,const_9733,call_9738,call_9740,call_9744,bop_9756,])
F = relay.Function([var_9721,var_9722,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_9721,var_9722,], output2)
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
