import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_684 = relay.var("var_684", dtype = "uint64", shape = (1, 3, 4))#candidate|684|(1, 3, 4)|var|uint64
var_685 = relay.var("var_685", dtype = "uint64", shape = (5, 3, 4))#candidate|685|(5, 3, 4)|var|uint64
bop_686 = relay.bitwise_and(var_684.astype('uint64'), var_685.astype('uint64')) # shape=(5, 3, 4)
uop_697 = relay.cos(bop_686.astype('float64')) # shape=(5, 3, 4)
output = uop_697
output2 = uop_697
func_703 = relay.Function([var_684,var_685,], output)
mod['func_703'] = func_703
mod = relay.transform.InferType()(mod)
var_704 = relay.var("var_704", dtype = "uint64", shape = (1, 3, 4))#candidate|704|(1, 3, 4)|var|uint64
var_705 = relay.var("var_705", dtype = "uint64", shape = (5, 3, 4))#candidate|705|(5, 3, 4)|var|uint64
output = func_703(var_704,var_705,)
func_706 = relay.Function([var_704,var_705,], output)
mutated_mod['func_706'] = func_706
mutated_mod = relay.transform.InferType()(mutated_mod)
const_817 = relay.const([[[2,-9,3,4,-6,1,2,-3,4,-1,10,4],[1,-9,-2,10,5,5,-3,-10,-1,-4,-10,-5],[4,3,-1,-4,-2,-7,3,6,-7,8,1,-10],[10,5,-8,-4,6,10,6,-2,-8,3,-8,-3],[-2,-4,10,3,-5,2,1,-8,5,6,4,10],[-9,-7,-1,-2,3,6,-10,-5,-9,10,5,9]],[[-8,9,-5,5,-1,-10,3,5,-8,1,-10,-2],[-5,1,2,8,-4,-1,-8,-10,-7,1,-2,5],[-7,-7,5,8,-2,10,8,4,-6,9,-1,3],[1,9,-2,3,-3,8,10,5,-6,3,-2,-4],[-4,-2,-5,-5,1,-10,-8,-2,-5,-6,8,-4],[10,-8,6,3,-8,5,2,-10,3,5,4,2]],[[-10,4,-4,4,-8,6,-6,-4,-4,8,10,-8],[-7,-4,-2,10,-7,-2,3,-4,-10,-4,1,-3],[-10,10,8,-3,-3,-7,5,7,-2,-4,-6,-7],[-1,7,1,-7,-10,1,5,4,-10,2,-8,7],[9,6,-10,-6,-6,-2,-2,9,6,-9,-5,8],[1,1,1,1,9,-7,-2,1,3,-4,2,6]],[[-5,-6,7,-6,-6,-10,-6,6,8,-8,6,8],[-3,-6,-8,-1,-7,-3,-3,-7,-5,7,-7,1],[-8,-8,6,-4,10,4,-2,9,1,8,-1,6],[-9,9,6,3,-7,-8,9,-4,4,5,2,-7],[-7,9,-9,4,-8,6,-3,9,2,-4,1,-9],[5,-1,1,-2,-5,6,5,-2,5,8,8,9]],[[-5,2,3,1,9,-7,-1,9,-9,10,7,9],[-1,-9,2,-1,-2,-3,8,5,5,10,-10,-2],[5,6,-5,1,10,6,-9,1,4,6,-7,1],[-2,9,-1,-4,-4,-6,3,-6,-9,-7,3,-10],[5,1,7,-5,5,1,-5,-10,-3,-8,6,-1],[10,3,-9,2,-9,5,7,4,-4,-7,10,-7]],[[-4,3,-3,-4,4,6,-2,-7,-3,8,-2,1],[-7,-4,6,2,-8,-9,-9,2,2,-9,8,7],[10,-1,-8,-10,-9,-2,8,4,-10,5,-7,5],[8,-6,-1,8,-10,4,1,3,-10,6,10,2],[-2,1,5,-1,-1,-9,-1,4,8,-1,3,1],[-8,9,-7,-10,-9,10,-9,7,1,-2,5,-6]],[[-5,-3,9,-10,-3,7,-2,-10,-9,3,3,-8],[5,7,-8,-2,9,9,-1,9,10,1,4,-2],[-4,-3,-6,1,2,1,2,3,1,1,3,-4],[-7,-6,8,6,-5,-9,9,-2,10,1,1,5],[-5,3,-8,10,4,6,4,-4,-10,-9,2,2],[-7,4,-6,-9,5,9,-1,-9,-7,-6,9,-1]],[[4,-2,3,8,6,9,3,2,-2,-3,2,-5],[-9,1,3,-8,3,-5,3,-6,7,2,-5,-8],[-7,-7,3,7,5,9,-9,-6,9,9,-5,3],[-4,2,1,-4,2,-7,-5,6,-2,1,4,-6],[-9,4,-3,7,-4,-7,-10,-3,-6,9,5,-3],[-2,2,4,-10,-6,8,-5,-9,6,4,-8,-10]],[[9,6,-7,-3,-5,-9,-5,-3,-5,-10,-6,9],[-4,-9,2,-7,-1,5,5,-8,-2,-1,-6,-8],[5,-3,-7,-4,5,-5,5,6,-8,5,-10,6],[-2,1,-1,-10,8,-9,6,-8,-9,8,9,-1],[4,10,8,7,5,7,6,-6,1,-9,-1,7],[-2,-5,8,7,9,-7,-7,7,2,-10,1,3]],[[1,10,3,-3,2,-5,3,4,3,-9,6,4],[9,-6,-10,-4,-5,5,2,2,-6,-4,-10,3],[2,6,7,5,4,6,-2,-4,-5,-2,7,-10],[-10,-3,7,-8,7,4,-3,-2,10,-10,-10,-1],[3,1,9,4,10,-2,3,-3,-5,6,5,7],[-6,2,-3,-1,6,6,-3,-5,-10,-7,8,-3]],[[8,10,-7,-1,-4,-9,5,3,9,-7,2,7],[-10,4,6,-10,9,8,-9,-9,3,9,-7,1],[4,10,9,-7,-4,8,2,-6,10,-9,4,-1],[7,7,2,9,4,-1,9,-6,3,-4,-2,6],[-4,-8,-4,-7,8,-4,-10,6,2,-10,9,3],[10,5,-8,3,-9,-4,1,-3,-5,-1,9,2]],[[-7,2,8,8,-5,-9,5,6,-4,-6,-10,-4],[-7,2,4,-9,6,-9,-9,2,9,6,5,7],[-10,4,3,7,-5,-5,-4,-10,-8,-9,-5,2],[4,7,7,7,-6,-1,9,8,-8,-2,9,-7],[10,-5,-6,-8,-4,10,-8,1,7,2,10,1],[3,4,-3,9,6,-8,-1,-7,-1,6,-3,3]],[[9,-10,-3,8,-2,8,-5,3,-10,-8,-9,-6],[1,10,-1,5,-6,10,6,7,-2,7,1,1],[-1,4,3,10,4,-7,1,-4,9,-10,1,4],[2,1,1,7,-10,-2,3,-6,-2,-1,-4,-1],[8,-9,9,-4,-7,6,-8,2,6,-2,7,-9],[8,-3,-6,7,-8,-4,-2,-7,3,10,8,1]],[[7,-6,-9,3,-6,4,-9,-5,9,-3,10,-3],[7,6,5,-1,1,5,4,-1,-2,-10,6,-9],[7,-10,-6,-1,6,8,5,2,-9,-7,-6,-3],[3,-1,-1,6,4,6,-8,-3,-2,-4,2,-4],[6,6,-10,-10,2,-2,4,2,3,-2,-3,-5],[-7,4,6,2,1,-4,7,-4,7,-2,5,3]]], dtype = "uint32")#candidate|817|(14, 6, 12)|const|uint32
var_818 = relay.var("var_818", dtype = "uint32", shape = (14, 6, 12))#candidate|818|(14, 6, 12)|var|uint32
bop_819 = relay.left_shift(const_817.astype('uint32'), relay.reshape(var_818.astype('uint32'), relay.shape_of(const_817))) # shape=(14, 6, 12)
output = bop_819
output2 = bop_819
func_834 = relay.Function([var_818,], output)
mod['func_834'] = func_834
mod = relay.transform.InferType()(mod)
var_835 = relay.var("var_835", dtype = "uint32", shape = (14, 6, 12))#candidate|835|(14, 6, 12)|var|uint32
output = func_834(var_835)
func_836 = relay.Function([var_835], output)
mutated_mod['func_836'] = func_836
mutated_mod = relay.transform.InferType()(mutated_mod)
const_867 = relay.const([[[7,2,-6,-9,9,5,-8,9,-6],[-1,-1,8,9,6,8,-9,-9,-7],[6,-3,-3,-3,9,-2,-9,9,-9],[-10,5,-8,-3,-10,-10,1,-4,-10],[-3,9,-9,8,2,-9,-8,-1,-5],[8,8,2,4,5,-8,-6,-10,-4],[3,-8,-1,10,-6,-4,10,8,-7],[-5,2,10,4,10,10,2,5,-10],[7,-10,1,-3,-4,-8,-1,-4,2],[2,10,10,5,-3,4,-1,-5,5],[4,6,8,1,-6,10,-10,4,6],[2,-9,-4,-10,5,7,-1,5,1]],[[1,1,-8,5,-7,2,4,5,-8],[-6,7,4,-1,-4,-4,10,-6,5],[5,-6,1,-6,-9,-8,-3,5,-6],[-3,-6,5,-2,9,9,-4,4,-7],[-7,9,5,2,2,5,8,6,4],[6,-8,6,9,-2,-1,9,1,3],[-5,-3,2,-6,-7,-4,8,9,-7],[3,-6,-8,-3,4,-6,1,1,10],[-5,4,1,-5,2,-6,2,2,4],[4,10,3,-4,-7,10,8,4,-9],[4,5,-9,-4,10,-8,9,-4,-9],[-2,1,8,7,-9,10,7,2,-1]],[[-2,-2,10,-9,-2,-5,-7,-6,8],[-2,-9,-5,8,6,-3,1,-1,-10],[-2,9,9,9,-5,-6,8,-8,-8],[-8,3,6,-3,3,-9,5,1,9],[2,-6,2,9,-10,7,-8,-6,-10],[-8,1,-7,4,6,-7,-5,-3,-7],[-3,-3,3,-2,-4,3,3,9,5],[-6,7,6,7,7,2,-4,-10,7],[8,4,8,-8,-1,4,-2,-8,-10],[-4,-6,6,-3,-3,9,6,-9,-1],[-8,-7,5,-8,2,7,10,1,-2],[-6,-9,-10,10,6,-4,6,8,-4]],[[5,-2,-8,10,-10,-6,8,-7,-2],[7,-3,-1,2,3,-1,2,9,-2],[5,-6,5,-7,-5,-1,-3,9,1],[-3,7,2,-10,-3,-10,-9,1,10],[-9,-8,-3,-1,7,-10,-2,-9,8],[-7,8,9,-9,3,-4,-3,-1,-7],[-1,-1,-10,5,6,1,7,-4,9],[3,4,7,2,-10,2,9,8,10],[-5,-10,-10,4,-10,-4,-2,9,6],[3,-8,3,4,1,-4,-10,7,9],[-2,7,-1,-4,-10,10,-1,-4,-8],[8,10,4,10,2,-3,-7,4,-8]]], dtype = "uint16")#candidate|867|(4, 12, 9)|const|uint16
var_868 = relay.var("var_868", dtype = "uint16", shape = (4, 12, 9))#candidate|868|(4, 12, 9)|var|uint16
bop_869 = relay.greater(const_867.astype('bool'), relay.reshape(var_868.astype('bool'), relay.shape_of(const_867))) # shape=(4, 12, 9)
func_703_call = mod.get_global_var('func_703')
func_706_call = mutated_mod.get_global_var('func_706')
var_887 = relay.var("var_887", dtype = "uint64", shape = (12,))#candidate|887|(12,)|var|uint64
var_888 = relay.var("var_888", dtype = "uint64", shape = (60, 1))#candidate|888|(60, 1)|var|uint64
call_886 = func_703_call(relay.reshape(var_887.astype('uint64'), [1, 3, 4]), relay.reshape(var_888.astype('uint64'), [5, 3, 4]), )
call_889 = func_703_call(relay.reshape(var_887.astype('uint64'), [1, 3, 4]), relay.reshape(var_888.astype('uint64'), [5, 3, 4]), )
func_703_call = mod.get_global_var('func_703')
func_706_call = mutated_mod.get_global_var('func_706')
call_900 = func_703_call(relay.reshape(var_887.astype('uint64'), [1, 3, 4]), relay.reshape(call_886.astype('uint64'), [5, 3, 4]), )
call_901 = func_703_call(relay.reshape(var_887.astype('uint64'), [1, 3, 4]), relay.reshape(call_886.astype('uint64'), [5, 3, 4]), )
const_903 = relay.const([[[9,7,6,4,-1,-2,-6,-10,3],[-2,10,-9,8,-4,2,-6,-9,-1],[-5,10,-7,-9,-9,2,6,10,-8],[3,-8,5,-4,-3,8,-7,10,8],[-10,-2,10,10,10,2,-9,-7,1],[9,3,-10,9,-3,-7,-8,-2,7],[-6,7,-4,-5,-3,-2,-4,-4,6],[-9,3,3,3,-10,-6,6,-1,10],[-10,-10,9,9,-4,2,7,2,3],[4,1,-2,9,8,9,-7,5,5],[-1,7,7,3,1,6,5,2,1],[2,2,-10,-8,-3,4,6,10,1]],[[5,1,-3,1,-4,3,-7,-5,-5],[-9,4,7,-7,5,6,-5,2,-8],[1,-3,10,-2,1,5,4,10,-5],[-6,-9,10,-7,-6,-10,-3,4,10],[2,-3,9,10,2,-1,-6,-9,-10],[-10,-3,9,1,-8,8,10,-8,-4],[9,-2,3,-7,-2,3,5,-2,-10],[-4,3,-7,-10,10,10,-6,-5,9],[2,8,-2,10,4,6,1,8,-1],[-4,4,8,-7,10,-5,-1,-6,-4],[9,4,4,-1,9,10,4,1,-7],[9,-7,7,1,10,-8,-4,6,2]],[[7,6,3,-7,1,7,1,3,9],[10,9,-5,-2,-6,6,-10,-3,2],[4,7,7,5,-1,6,10,8,-7],[8,4,10,6,-7,-6,-9,6,8],[-9,3,-1,10,6,3,-4,3,-9],[-8,-4,-5,1,3,-9,3,3,-10],[7,-6,-1,-6,-1,1,-3,4,5],[8,-5,-5,1,4,6,-8,7,5],[4,1,2,5,4,-3,-1,4,3],[2,-9,-9,2,7,-3,7,4,3],[1,-1,9,3,6,-6,9,4,4],[-3,1,8,-10,3,3,10,-6,-9]],[[5,-7,-9,10,10,-6,-7,5,-10],[-2,-5,6,1,-2,-7,3,2,2],[2,-1,-6,-9,7,1,-6,-10,7],[1,-10,-6,5,-8,7,10,2,2],[-8,10,-6,5,-3,-6,-10,8,-1],[8,4,-5,-6,8,4,-5,-2,2],[-6,-3,1,-9,8,1,-4,5,5],[-6,-5,-8,-8,-3,-7,-2,1,4],[-5,-3,2,2,4,-1,7,9,-6],[3,9,-6,-3,1,-2,-8,-8,9],[6,6,-1,7,6,2,-1,8,10],[-8,10,7,-4,10,7,-2,3,10]]], dtype = "uint16")#candidate|903|(4, 12, 9)|const|uint16
bop_904 = relay.minimum(var_868.astype('int8'), relay.reshape(const_903.astype('int8'), relay.shape_of(var_868))) # shape=(4, 12, 9)
output = relay.Tuple([bop_869,call_886,var_887,var_888,call_900,bop_904,])
output2 = relay.Tuple([bop_869,call_889,var_887,var_888,call_901,bop_904,])
func_907 = relay.Function([var_868,var_887,var_888,], output)
mod['func_907'] = func_907
mod = relay.transform.InferType()(mod)
mutated_mod['func_907'] = func_907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_907_call = mutated_mod.get_global_var('func_907')
var_909 = relay.var("var_909", dtype = "uint16", shape = (4, 12, 9))#candidate|909|(4, 12, 9)|var|uint16
var_910 = relay.var("var_910", dtype = "uint64", shape = (12,))#candidate|910|(12,)|var|uint64
var_911 = relay.var("var_911", dtype = "uint64", shape = (60, 1))#candidate|911|(60, 1)|var|uint64
call_908 = func_907_call(var_909,var_910,var_911,)
output = call_908
func_912 = relay.Function([var_909,var_910,var_911,], output)
mutated_mod['func_912'] = func_912
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1224 = relay.var("var_1224", dtype = "bool", shape = (16, 13, 16))#candidate|1224|(16, 13, 16)|var|bool
const_1225 = relay.const([[[False,False,False,True,False,False,False,False,False,True,True,True,False,False,False,False],[False,False,False,True,False,True,False,False,False,True,True,False,False,False,False,False],[False,False,True,True,False,False,True,False,True,False,True,True,False,True,False,False],[False,False,True,False,True,True,False,True,False,False,True,False,False,True,True,True],[True,False,False,True,False,True,True,True,True,False,True,True,False,True,True,False],[True,False,False,True,False,True,False,False,True,False,True,True,True,False,False,True],[False,False,False,True,True,False,False,False,False,True,True,False,False,False,False,False],[True,True,True,True,False,True,True,True,True,False,False,True,False,True,False,True],[True,False,False,True,False,False,True,True,False,True,True,False,True,False,False,False],[True,True,True,True,True,True,False,False,True,False,True,False,True,True,True,True],[False,True,False,False,True,True,True,True,False,True,False,False,True,False,False,False],[False,False,True,True,True,True,True,False,True,True,False,True,False,True,False,False],[False,False,True,False,True,False,True,False,True,True,False,False,False,False,False,False]],[[False,True,True,True,False,False,False,False,True,False,True,False,False,True,False,False],[True,True,False,False,False,False,False,True,True,False,False,True,True,False,True,True],[False,False,True,False,True,True,False,False,True,True,False,True,False,True,False,True],[False,False,False,False,False,False,False,False,True,False,True,False,False,True,True,False],[True,False,True,False,True,True,True,True,True,True,False,True,False,False,True,True],[True,True,True,True,True,True,True,False,True,True,False,False,False,False,False,True],[False,True,False,False,True,True,True,False,False,True,True,True,False,False,False,True],[True,True,False,True,True,False,True,False,True,False,False,True,False,True,False,False],[False,False,False,True,True,True,True,False,True,True,True,True,True,True,False,True],[False,False,False,True,False,True,False,True,True,False,False,True,True,True,False,False],[True,False,True,True,False,True,True,True,False,False,False,True,True,False,False,True],[False,False,True,True,False,True,False,True,True,True,True,True,False,True,True,True],[True,False,False,True,True,True,False,True,True,False,True,False,False,True,False,True]],[[False,True,False,False,False,False,True,True,True,False,False,True,True,True,True,True],[False,True,False,True,True,True,True,False,True,False,True,False,True,True,True,True],[False,True,True,False,True,True,True,True,True,False,False,True,True,True,False,True],[True,False,True,False,True,False,False,True,False,True,True,True,False,False,True,False],[True,False,False,False,True,False,True,True,False,False,False,True,True,False,True,False],[False,False,False,False,False,True,True,False,False,False,True,True,False,False,True,True],[True,False,True,False,False,True,True,False,True,True,True,False,True,False,True,False],[False,True,False,False,False,True,False,True,True,False,False,True,False,True,False,True],[True,True,False,True,False,True,True,True,True,True,False,False,True,True,False,False],[False,False,False,True,True,True,False,False,True,False,True,True,True,True,True,True],[True,True,False,True,False,False,True,True,True,True,False,False,False,False,False,False],[True,True,True,False,False,True,True,True,True,False,False,True,False,True,False,True],[False,False,False,True,False,True,False,True,False,False,False,False,True,False,True,False]],[[True,False,False,True,False,True,False,True,False,True,False,False,False,False,True,True],[True,True,False,True,True,False,True,True,True,True,False,False,True,True,False,True],[True,False,False,True,False,True,True,False,False,True,False,False,False,True,True,True],[False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True],[True,True,True,True,False,False,True,False,True,True,True,True,False,False,False,True],[False,True,False,False,False,True,True,True,False,False,True,False,True,False,False,False],[True,True,False,False,True,True,False,False,True,True,False,True,False,False,False,False],[True,True,False,False,False,True,True,True,True,False,True,False,False,True,False,True],[False,False,True,True,False,False,False,True,True,False,False,True,False,True,True,False],[False,True,False,False,False,True,True,True,True,True,True,True,False,False,False,True],[False,False,False,False,False,False,True,True,False,False,True,True,True,False,True,True],[False,True,True,False,False,True,False,True,False,True,False,False,True,False,True,False],[False,False,False,False,False,False,False,True,False,True,False,True,True,True,False,True]],[[False,True,False,False,False,False,True,False,True,True,True,True,True,False,True,False],[False,True,False,True,True,False,False,True,True,False,False,True,True,False,False,True],[False,False,True,False,False,False,True,False,True,False,True,False,False,False,False,True],[True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,True],[True,True,False,True,True,True,True,False,True,False,False,True,False,True,False,False],[False,False,True,True,False,True,False,False,False,False,True,False,True,True,True,False],[False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,True],[False,True,False,False,False,True,True,True,True,False,True,False,False,False,False,False],[False,False,False,False,True,True,False,False,True,True,False,False,False,False,True,False],[True,False,True,False,True,False,True,False,False,False,True,False,False,True,True,False],[True,True,True,False,False,True,True,False,False,True,False,False,False,False,True,True],[False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True],[True,False,False,True,True,True,True,True,False,False,False,False,False,True,False,False]],[[True,True,True,True,False,False,True,False,True,False,True,True,False,True,False,True],[True,False,True,True,True,False,False,False,False,False,False,False,True,False,False,False],[False,True,True,False,False,True,False,True,True,False,False,False,True,False,True,False],[True,False,True,False,True,False,False,True,False,True,False,False,True,False,False,True],[False,False,True,False,True,False,True,False,False,True,False,True,True,False,True,False],[False,True,True,True,True,True,True,True,False,True,True,False,True,False,True,True],[False,True,True,True,True,False,True,True,True,False,False,True,False,True,True,False],[False,False,False,True,False,True,True,False,False,False,False,True,False,False,True,False],[True,False,True,False,True,True,True,False,True,True,True,True,False,True,True,True],[True,True,False,True,False,True,False,False,False,False,False,False,False,True,True,True],[True,False,True,False,True,False,True,False,True,False,True,False,True,True,True,True],[False,True,False,True,True,False,True,True,True,True,True,True,False,False,True,False],[True,False,False,False,True,True,True,False,False,False,False,True,True,True,False,False]],[[True,True,True,False,True,False,True,False,False,False,False,False,True,True,False,False],[True,True,False,False,False,True,True,False,False,True,False,True,True,False,True,False],[True,False,False,True,True,True,True,True,True,True,True,False,False,False,False,False],[True,True,False,True,False,True,False,False,True,False,False,False,False,True,False,False],[False,False,True,True,True,False,False,False,False,True,True,False,True,True,False,False],[False,True,False,True,False,False,True,True,False,True,True,False,True,True,False,True],[True,True,False,False,False,False,True,False,True,False,False,True,True,True,True,False],[False,True,True,False,True,False,False,True,False,True,False,True,True,False,False,False],[False,False,True,False,False,False,False,True,False,False,False,True,True,False,True,True],[True,False,False,True,True,False,False,True,True,False,False,False,True,False,True,True],[False,False,True,False,False,True,True,False,True,False,True,True,False,True,False,True],[True,False,False,False,False,True,True,False,True,True,False,False,True,True,True,True],[True,False,True,True,True,True,True,True,True,True,False,True,False,False,False,True]],[[True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,True],[False,True,False,True,False,False,False,True,True,False,False,True,True,True,False,False],[False,False,True,False,False,True,True,True,True,True,True,False,True,True,True,True],[True,False,False,True,False,True,True,True,True,True,False,False,False,False,False,False],[True,False,False,True,True,False,False,False,True,True,False,False,True,False,True,False],[False,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False],[True,True,True,False,True,True,False,True,True,True,True,False,True,True,False,True],[True,True,True,False,False,False,False,False,True,True,False,False,True,True,True,False],[True,False,True,False,False,True,True,True,False,True,True,True,False,True,False,True],[False,True,True,False,True,True,False,False,True,True,True,False,False,False,False,True],[False,True,False,False,True,True,True,True,False,False,True,False,True,True,True,False],[True,False,False,False,False,True,True,True,False,False,True,False,False,True,False,False],[True,False,True,False,True,False,True,False,True,False,False,False,False,False,False,True]],[[False,True,True,False,False,False,True,False,False,False,False,False,False,False,True,True],[False,False,True,False,False,False,False,True,True,False,False,True,False,False,False,True],[True,True,True,True,False,True,True,False,True,False,True,True,False,False,False,True],[False,True,True,False,False,True,False,True,True,False,False,False,False,False,True,False],[True,False,True,True,True,True,False,True,True,True,False,True,True,True,False,True],[False,True,True,False,False,True,True,False,True,True,False,False,True,True,False,True],[True,True,False,True,False,False,False,True,True,False,True,False,True,True,True,False],[True,True,False,True,False,False,True,False,True,True,False,True,False,False,False,False],[True,False,True,False,True,True,True,False,True,False,True,True,False,False,True,True],[True,True,False,False,True,False,False,True,True,False,False,False,False,False,False,True],[False,True,True,True,False,True,False,True,True,True,False,True,True,True,False,True],[True,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False],[True,False,True,True,True,True,True,False,False,True,False,False,True,False,True,False]],[[True,False,False,False,True,False,True,False,True,True,True,True,False,True,True,True],[True,False,True,False,False,False,True,False,True,True,False,False,True,True,False,True],[True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False],[True,False,True,True,False,False,True,False,True,False,False,False,True,True,True,True],[False,True,True,True,True,False,True,True,True,True,True,False,True,True,True,False],[True,False,True,False,False,True,False,True,True,False,True,False,True,True,True,True],[False,True,False,True,True,False,True,False,True,False,True,False,True,False,True,True],[False,False,True,False,True,True,True,False,True,False,True,True,True,False,False,True],[True,True,True,False,True,False,True,False,False,False,False,False,False,True,True,False],[False,False,False,True,True,True,False,False,True,True,True,True,True,False,False,True],[True,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False],[True,False,True,False,True,True,False,True,False,False,False,False,False,False,True,True],[False,False,True,True,True,True,True,True,True,True,False,True,False,False,True,True]],[[True,True,True,False,False,False,True,True,False,True,True,False,False,False,True,False],[False,False,True,True,True,True,True,False,False,True,False,True,True,True,False,False],[False,False,True,True,False,False,False,False,False,True,False,False,True,True,False,True],[True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,False],[False,False,True,False,False,True,False,False,False,False,False,True,True,False,True,False],[False,False,False,False,False,True,True,True,True,True,True,True,False,False,False,False],[False,True,True,True,True,True,True,True,False,False,True,True,False,False,False,False],[False,False,True,False,True,False,True,True,False,False,False,False,True,False,False,True],[False,True,False,True,True,False,False,True,False,True,False,False,True,False,True,True],[True,False,True,False,False,False,True,False,True,False,False,False,False,True,True,False],[False,False,True,True,False,False,False,False,True,True,False,True,True,True,False,False],[True,False,True,False,False,False,False,True,False,True,True,True,False,True,True,False],[True,True,False,True,True,False,True,False,True,True,True,True,True,False,True,False]],[[False,False,False,False,True,True,False,True,False,True,False,False,False,False,False,True],[True,False,False,False,True,True,False,False,True,False,True,False,False,True,False,False],[True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,True],[True,False,True,False,False,False,False,True,False,False,True,False,True,True,False,False],[False,False,True,False,True,True,False,True,True,False,True,False,True,True,True,False],[False,True,False,False,True,False,True,True,False,False,True,True,True,True,False,False],[True,True,False,False,False,True,True,True,True,True,True,False,False,True,False,False],[False,False,False,True,True,True,False,True,True,True,True,True,False,True,True,True],[False,True,False,False,False,True,True,False,False,True,False,True,False,True,True,False],[True,False,True,False,True,True,False,True,False,True,False,False,False,True,True,False],[False,True,False,True,True,True,True,True,False,True,False,False,False,False,False,False],[False,True,False,True,False,False,False,False,True,False,False,True,True,False,True,False],[True,True,True,False,True,False,False,True,True,False,False,False,False,False,False,False]],[[False,False,False,False,True,False,True,False,True,True,False,False,True,True,False,True],[True,True,True,False,True,True,True,True,False,True,True,False,False,True,True,False],[True,True,False,False,True,True,True,False,True,True,True,False,False,True,True,True],[True,True,True,False,False,True,True,False,False,False,True,False,True,False,False,True],[True,True,True,False,False,False,True,True,True,False,False,False,True,True,True,False],[False,True,True,True,False,False,True,False,True,False,True,False,False,True,True,True],[False,True,False,True,True,True,False,True,True,False,True,False,False,False,True,False],[True,False,True,True,False,True,False,True,True,True,False,False,False,True,True,True],[False,True,False,False,False,False,True,True,True,False,False,True,False,True,True,False],[True,True,True,True,False,True,True,True,False,True,True,True,False,True,False,True],[False,False,True,True,False,False,False,True,False,False,False,False,True,False,False,False],[True,False,False,True,True,True,False,False,False,False,True,False,True,True,True,True],[True,False,False,True,False,True,True,False,True,True,True,True,True,True,True,False]],[[True,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False],[True,True,True,True,False,False,False,True,False,True,False,True,False,False,False,False],[True,True,True,False,True,False,False,True,False,True,False,True,False,True,True,True],[False,False,False,False,True,False,True,True,True,False,False,False,False,False,False,True],[False,True,True,True,True,False,True,True,True,True,False,True,False,True,False,False],[True,True,False,False,True,False,True,True,False,False,True,False,False,True,True,False],[False,True,False,True,True,True,False,False,False,False,False,True,True,False,True,False],[True,False,True,True,False,False,False,False,False,True,False,True,False,True,True,False],[False,True,True,True,False,True,False,True,True,False,False,False,False,True,False,False],[True,True,True,True,False,True,True,False,False,True,True,False,True,True,False,True],[False,True,True,True,False,True,False,True,True,False,True,True,True,True,True,True],[True,False,False,True,True,False,True,True,True,True,True,False,False,True,False,False],[False,True,True,False,False,True,True,True,True,False,False,True,False,False,False,True]],[[False,False,False,False,False,True,True,False,False,True,False,False,False,False,True,True],[True,False,True,True,False,True,False,True,True,True,False,True,True,False,False,True],[True,False,True,True,False,True,True,False,False,False,True,False,False,False,True,False],[False,True,True,False,False,False,False,True,True,False,True,False,True,True,True,False],[False,True,True,False,False,True,False,False,True,True,False,True,True,False,True,False],[True,True,False,True,True,False,False,False,True,True,False,False,True,True,False,True],[False,True,True,False,False,True,False,True,True,True,True,False,True,False,False,False],[True,True,True,False,True,True,False,False,True,False,False,False,False,False,True,False],[False,False,True,False,True,True,False,False,False,True,True,True,True,True,True,True],[False,False,True,False,False,False,False,True,False,True,True,False,True,False,True,True],[False,False,False,True,True,False,False,False,True,True,True,False,False,True,True,True],[True,True,True,True,True,True,False,True,False,True,False,False,True,True,True,True],[True,True,True,False,True,True,False,False,False,False,True,False,True,False,True,False]],[[True,False,False,False,False,False,False,False,False,False,False,True,True,False,True,False],[True,False,False,True,True,True,True,True,True,False,True,False,True,True,False,False],[True,False,True,True,True,True,False,True,True,False,False,False,False,True,False,False],[True,False,True,False,True,False,True,False,True,True,False,False,False,True,False,True],[True,True,True,False,False,True,True,True,True,False,True,False,True,True,False,True],[False,True,True,True,True,True,False,False,False,False,False,False,True,True,True,True],[False,False,True,True,True,True,False,True,True,False,True,False,True,True,True,True],[False,True,True,True,False,True,False,False,True,False,False,True,True,True,False,False],[False,True,True,True,False,True,False,True,True,True,False,True,False,True,False,False],[False,True,False,False,False,False,False,False,False,False,True,False,False,True,False,False],[False,True,True,True,False,False,False,False,True,False,True,False,False,True,False,False],[True,False,True,True,False,True,True,True,False,False,True,False,True,True,False,False],[False,True,True,False,True,True,False,True,False,True,True,False,True,True,False,False]]], dtype = "bool")#candidate|1225|(16, 13, 16)|const|bool
bop_1226 = relay.logical_and(var_1224.astype('bool'), relay.reshape(const_1225.astype('bool'), relay.shape_of(var_1224))) # shape=(16, 13, 16)
func_907_call = mod.get_global_var('func_907')
func_912_call = mutated_mod.get_global_var('func_912')
const_1232 = relay.const([6,-10,5,-6,2,-2,10,5,-6,-10,7,-3,-10,10,-6,7,-2,-3,-10,3,-10,-3,3,-6,-2,-9,6,-2,10,2,-6,8,-5,-7,7,6,-5,8,4,-8,10,-7,-9,3,-2,5,-3,6,-3,-2,2,-10,9,-6,-3,1,-4,-10,-9,2,7,9,-2,7,-9,8,8,-10,-7,10,-3,-3,-1,-9,7,4,-1,-5,10,-10,10,-10,-5,5,-9,2,-8,-6,-10,-9,-8,-1,8,6,6,8,-4,-8,1,3,-10,9,-1,-7,1,6,-1,-10,2,10,2,8,6,-6,-9,8,-5,-9,3,-7,-4,-6,1,5,-2,3,-2,-1,-7,7,6,-7,-2,7,-10,2,9,-8,-5,-4,-9,2,-8,-2,-10,2,4,-6,6,4,8,-10,3,7,-5,5,-8,5,-10,4,6,5,-5,-8,6,7,-7,1,6,-8,-9,-5,1,-4,9,-10,-3,-4,-10,7,4,8,-2,-3,-6,-9,3,-1,-8,-5,2,1,-4,4,-9,8,7,-7,6,7,-1,7,2,8,5,-6,-3,-2,4,-3,-7,6,-8,2,3,7,6,7,2,-8,3,3,3,-4,-3,9,7,-3,10,-8,3,-6,9,-6,1,9,-2,-1,-10,-3,2,-3,9,6,3,4,-9,-6,-8,-1,-8,4,-7,-6,-9,-1,1,2,2,-3,1,-3,-2,1,1,8,4,-1,6,-9,-8,-8,4,1,9,5,3,-10,-6,2,5,-1,3,-2,-1,6,1,8,-5,5,5,3,7,1,-6,-1,5,10,3,-9,-4,4,8,-3,3,8,-6,-3,6,-6,-9,3,-10,3,6,-10,6,6,-7,8,4,5,-7,-5,-4,-3,-10,8,9,3,-3,6,8,3,8,5,-7,4,-1,-7,9,-8,6,9,7,-3,-9,-2,-10,4,8,1,-2,-9,5,-9,-6,5,3,1,10,-4,2,5,3,-1,-1,-6,7,-7,1,-9,3,3,2,7,8,8,-7,4,-4,-1,-5,-7,2,9,8,-2,-3,-6,-9,-4,6,8,7,-5,5,4,-1,-4,-5,-6,-10,3,-5,8,-5,2,-6,-5,2,-4,4,-7,-8,-9,6,5,8,-1,8,9,-2,5,1,3,-9,-10,-4,9,-10,7], dtype = "uint16")#candidate|1232|(432,)|const|uint16
var_1233 = relay.var("var_1233", dtype = "uint64", shape = (12,))#candidate|1233|(12,)|var|uint64
const_1234 = relay.const([-2,6,-2,3,8,-3,7,-2,-2,1,-1,-8,-3,-6,6,4,2,8,-7,-1,1,3,2,6,10,-10,10,-10,4,3,-7,-8,8,-4,-8,-9,-1,-7,-8,6,10,6,3,-4,-6,-7,-3,4,2,6,5,7,8,8,4,-3,-8,-4,-9,-10], dtype = "uint64")#candidate|1234|(60,)|const|uint64
call_1231 = relay.TupleGetItem(func_907_call(relay.reshape(const_1232.astype('uint16'), [4, 12, 9]), relay.reshape(var_1233.astype('uint64'), [12,]), relay.reshape(const_1234.astype('uint64'), [60, 1]), ), 4)
call_1235 = relay.TupleGetItem(func_912_call(relay.reshape(const_1232.astype('uint16'), [4, 12, 9]), relay.reshape(var_1233.astype('uint64'), [12,]), relay.reshape(const_1234.astype('uint64'), [60, 1]), ), 4)
output = relay.Tuple([bop_1226,call_1231,const_1232,var_1233,const_1234,])
output2 = relay.Tuple([bop_1226,call_1235,const_1232,var_1233,const_1234,])
func_1239 = relay.Function([var_1224,var_1233,], output)
mod['func_1239'] = func_1239
mod = relay.transform.InferType()(mod)
mutated_mod['func_1239'] = func_1239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1239_call = mutated_mod.get_global_var('func_1239')
var_1241 = relay.var("var_1241", dtype = "bool", shape = (16, 13, 16))#candidate|1241|(16, 13, 16)|var|bool
var_1242 = relay.var("var_1242", dtype = "uint64", shape = (12,))#candidate|1242|(12,)|var|uint64
call_1240 = func_1239_call(var_1241,var_1242,)
output = call_1240
func_1243 = relay.Function([var_1241,var_1242,], output)
mutated_mod['func_1243'] = func_1243
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1475 = relay.var("var_1475", dtype = "bool", shape = ())#candidate|1475|()|var|bool
var_1476 = relay.var("var_1476", dtype = "bool", shape = (12, 9, 7))#candidate|1476|(12, 9, 7)|var|bool
bop_1477 = relay.logical_and(var_1475.astype('bool'), var_1476.astype('bool')) # shape=(12, 9, 7)
output = bop_1477
output2 = bop_1477
func_1496 = relay.Function([var_1475,var_1476,], output)
mod['func_1496'] = func_1496
mod = relay.transform.InferType()(mod)
mutated_mod['func_1496'] = func_1496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1496_call = mutated_mod.get_global_var('func_1496')
var_1498 = relay.var("var_1498", dtype = "bool", shape = ())#candidate|1498|()|var|bool
var_1499 = relay.var("var_1499", dtype = "bool", shape = (12, 9, 7))#candidate|1499|(12, 9, 7)|var|bool
call_1497 = func_1496_call(var_1498,var_1499,)
output = call_1497
func_1500 = relay.Function([var_1498,var_1499,], output)
mutated_mod['func_1500'] = func_1500
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1527 = relay.var("var_1527", dtype = "float32", shape = (2, 4, 16))#candidate|1527|(2, 4, 16)|var|float32
uop_1528 = relay.log2(var_1527.astype('float32')) # shape=(2, 4, 16)
output = relay.Tuple([uop_1528,])
output2 = relay.Tuple([uop_1528,])
func_1534 = relay.Function([var_1527,], output)
mod['func_1534'] = func_1534
mod = relay.transform.InferType()(mod)
var_1535 = relay.var("var_1535", dtype = "float32", shape = (2, 4, 16))#candidate|1535|(2, 4, 16)|var|float32
output = func_1534(var_1535)
func_1536 = relay.Function([var_1535], output)
mutated_mod['func_1536'] = func_1536
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1596 = relay.const([[[-3.872739,6.725122,-2.734201,6.505971,-8.140081],[-0.041908,9.436752,4.942987,4.514120,-0.627567],[-4.383432,3.164084,-4.211372,1.585579,-4.021901],[-1.882427,4.635494,-5.877902,-6.253663,-5.771523],[-4.118570,-6.641946,9.687051,-8.291476,7.379114],[0.144365,8.304312,-6.278396,5.958092,7.404600],[-4.495259,-1.676643,-6.781123,7.557045,-9.122273],[7.790148,-1.733235,5.020726,7.520259,-2.752130],[-1.826431,6.469540,7.385677,-0.149243,5.363682],[-6.493723,4.088566,7.760763,5.022132,2.088228],[-1.443078,-0.902665,-8.074279,-8.899227,2.003464],[-1.195395,3.415195,-3.331649,7.015332,7.588270],[-0.587550,9.237631,7.852336,7.922429,8.462316]],[[-8.208420,-3.943251,3.491667,-6.462449,-4.718291],[-1.524223,-1.617617,-9.406257,-3.905306,4.122876],[-2.291978,7.755161,1.741585,9.704705,1.953752],[9.377870,-1.987818,2.196552,-1.763573,-1.150787],[2.416213,-7.311458,-6.899297,-6.746822,-0.202799],[-2.250674,-7.903392,-0.838005,-1.871778,-5.885714],[8.505322,-0.481693,7.698164,5.953264,2.376219],[9.445117,-4.587434,-3.931287,-0.068204,-0.013602],[-8.982249,-0.344176,-6.770631,9.046591,-8.720614],[0.468142,6.012663,8.450598,4.744778,7.284174],[-3.762096,2.751847,-4.486975,8.474024,9.823775],[9.341439,9.314375,-5.353550,4.881157,-6.929408],[8.922689,1.422084,7.138958,-1.580768,0.632515]],[[-0.614692,-1.606212,-8.152977,6.861289,7.548654],[9.725737,9.907839,-8.198385,7.285866,2.949260],[3.949965,7.173959,1.587353,-8.201062,9.077061],[5.600809,0.598829,8.278883,-8.821163,-3.284678],[1.672700,8.642525,-1.452931,-1.805078,8.751675],[8.097624,8.917475,3.068636,-1.115461,-5.552443],[5.956628,0.642749,2.062357,-9.821561,0.198758],[6.784075,2.232902,4.410156,5.837465,5.896908],[9.362707,0.999133,7.576248,-3.704634,-4.536570],[9.738941,-2.651840,2.472089,4.230191,-0.785702],[-3.724238,-6.140454,-7.329739,3.566089,4.112959],[-8.505480,1.485974,0.556671,-8.046573,-5.273566],[-5.206587,-9.579774,-1.591637,-3.815199,6.415963]]], dtype = "float64")#candidate|1596|(3, 13, 5)|const|float64
uop_1597 = relay.erf(const_1596.astype('float64')) # shape=(3, 13, 5)
output = uop_1597
output2 = uop_1597
func_1602 = relay.Function([], output)
mod['func_1602'] = func_1602
mod = relay.transform.InferType()(mod)
mutated_mod['func_1602'] = func_1602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1602_call = mutated_mod.get_global_var('func_1602')
call_1603 = func_1602_call()
output = call_1603
func_1604 = relay.Function([], output)
mutated_mod['func_1604'] = func_1604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1602_call = mod.get_global_var('func_1602')
func_1604_call = mutated_mod.get_global_var('func_1604')
call_1626 = func_1602_call()
call_1627 = func_1602_call()
func_1534_call = mod.get_global_var('func_1534')
func_1536_call = mutated_mod.get_global_var('func_1536')
const_1629 = relay.const([7.488514,-8.091277,-2.858406,-9.009732,2.596390,3.712201,-9.710988,2.313634,-2.662620,3.305497,-8.918484,3.779157,-8.697758,-2.049185,-0.354535,-2.432131,-6.967643,6.600083,3.017816,-1.094261,-1.229081,-1.057279,-3.221542,6.338510,-9.926103,-4.263996,-1.535328,-9.699354,3.714473,-9.111943,-1.343105,-1.037520,8.675059,0.796298,8.517679,8.705383,6.205109,-5.225090,-3.181587,-4.688620,-5.048910,1.502181,4.272963,7.197324,-4.407441,-8.052549,-9.296190,7.565640,-2.292501,-1.127707,4.934451,-9.913545,-7.262886,-2.954637,-2.461101,7.496925,0.972891,2.696449,-7.943975,-2.942734,-7.002157,2.308566,7.261490,-6.501126,6.975841,6.666746,-3.668766,6.617322,6.929086,8.914588,3.349993,-5.517342,8.408731,9.386118,9.266933,-0.111426,-7.536317,-3.668649,1.190812,-0.950784,-3.271624,5.832300,0.506936,5.814682,-6.338581,-0.963847,0.110127,2.745682,-1.169256,-4.203754,-1.170516,1.319565,-8.698744,-8.360219,-1.955603,-1.335334,-1.944767,2.830239,-9.493385,-8.086680,-2.643407,-4.393687,-9.293488,-4.437791,-2.597747,-9.800991,-6.464414,-1.733779,8.285313,-5.693951,1.034157,-4.347278,-5.487387,6.934269,-3.377448,3.749749,-8.402914,-0.485751,0.258621,0.672532,4.635086,-7.144495,9.609295,-6.709175,6.329007,-8.977186,5.517143,9.344696], dtype = "float32")#candidate|1629|(128,)|const|float32
call_1628 = relay.TupleGetItem(func_1534_call(relay.reshape(const_1629.astype('float32'), [2, 4, 16])), 0)
call_1630 = relay.TupleGetItem(func_1536_call(relay.reshape(const_1629.astype('float32'), [2, 4, 16])), 0)
output = relay.Tuple([call_1626,call_1628,const_1629,])
output2 = relay.Tuple([call_1627,call_1630,const_1629,])
func_1642 = relay.Function([], output)
mod['func_1642'] = func_1642
mod = relay.transform.InferType()(mod)
output = func_1642()
func_1643 = relay.Function([], output)
mutated_mod['func_1643'] = func_1643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1642_call = mod.get_global_var('func_1642')
func_1643_call = mutated_mod.get_global_var('func_1643')
call_1673 = relay.TupleGetItem(func_1642_call(), 2)
call_1674 = relay.TupleGetItem(func_1643_call(), 2)
uop_1693 = relay.rsqrt(call_1673.astype('float64')) # shape=(128,)
uop_1695 = relay.rsqrt(call_1674.astype('float64')) # shape=(128,)
func_1534_call = mod.get_global_var('func_1534')
func_1536_call = mutated_mod.get_global_var('func_1536')
call_1702 = relay.TupleGetItem(func_1534_call(relay.reshape(uop_1693.astype('float32'), [2, 4, 16])), 0)
call_1703 = relay.TupleGetItem(func_1536_call(relay.reshape(uop_1693.astype('float32'), [2, 4, 16])), 0)
output = relay.Tuple([uop_1693,call_1702,])
output2 = relay.Tuple([uop_1695,call_1703,])
func_1707 = relay.Function([], output)
mod['func_1707'] = func_1707
mod = relay.transform.InferType()(mod)
output = func_1707()
func_1708 = relay.Function([], output)
mutated_mod['func_1708'] = func_1708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1602_call = mod.get_global_var('func_1602')
func_1604_call = mutated_mod.get_global_var('func_1604')
call_1709 = func_1602_call()
call_1710 = func_1602_call()
uop_1735 = relay.tan(call_1709.astype('float64')) # shape=(3, 13, 5)
uop_1737 = relay.tan(call_1710.astype('float64')) # shape=(3, 13, 5)
func_1707_call = mod.get_global_var('func_1707')
func_1708_call = mutated_mod.get_global_var('func_1708')
call_1754 = relay.TupleGetItem(func_1707_call(), 0)
call_1755 = relay.TupleGetItem(func_1708_call(), 0)
func_1239_call = mod.get_global_var('func_1239')
func_1243_call = mutated_mod.get_global_var('func_1243')
const_1762 = relay.const([False,True,False,False,False,True,True,False,False,False,False,False,True,False,False,True,False,True,True,False,False,True,True,True,True,False,False,True,False,False,True,False,True,False,False,True,True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,False,True,True,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False,True,False,True,False,False,False,False,True,True,True,True,False,False,False,True,False,False,True,True,True,False,True,False,True,False,True,True,True,False,False,True,True,True,False,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,False,True,True,True,False,False,False,False,True,True,True,True,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,False,False,False,False,False,False,True,False,False,False,True,True,True,True,True,True,True,False,False,True,False,False,True,True,True,False,False,False,False,True,True,False,True,False,True,True,False,False,True,False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,True,True,False,False,True,False,True,True,False,False,True,True,True,True,True,True,False,False,False,True,False,False,False,True,True,False,False,False,False,False,True,True,True,True,True,False,True,False,True,False,False,False,True,False,False,True,True,False,True,True,True,True,True,False,False,False,False,False,False,False,False,False,True,True,True,True,False,True,True,True,True,False,False,False,False,False,True,True,False,False,False,True,True,True,True,True,True,True,False,False,True,False,False,True,False,True,False,False,False,True,True,True,True,True,False,True,True,True,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False,False,True,False,False,True,True,False,False,False,True,True,True,False,False,True,True,True,False,True,False,True,False,True,True,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,False,False,False,False,False,False,True,True,True,False,False,True,False,True,False,True,False,False,False,False,True,True,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,True,True,False,False,False,False,True,False,True,False,False,True,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,False,True,True,False,True,True,False,True,True,True,True,True,True,True,True,False,False,False,False,False,True,True,False,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,False,True,True,False,False,False,True,False,True,False,False,True,False,False,True,True,True,True,True,False,True,False,False,False,False,False,False,False,True,False,False,False,True,True,False,True,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,True,True,True,False,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,True,False,False,True,True,True,False,False,True,False,True,True,True,False,False,False,False,False,False,True,True,True,False,True,True,False,False,False,False,False,False,False,False,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,True,True,False,False,False,True,True,False,True,True,False,True,True,False,True,False,True,False,False,False,True,True,False,False,True,True,False,False,False,True,True,True,False,True,True,True,False,False,True,True,False,True,True,True,True,False,True,False,False,False,False,True,True,False,True,True,False,True,True,False,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,False,True,True,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,False,False,True,False,True,False,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,False,True,False,False,True,True,True,False,False,False,False,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True,True,True,True,False,False,True,True,True,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,True,False,False,True,False,False,True,True,True,False,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,False,True,False,True,False,True,False,False,True,True,False,True,False,False,True,False,True,False,True,True,True,False,False,True,True,False,False,False,True,True,True,True,False,True,True,False,False,True,False,False,True,True,True,True,True,False,False,False,True,True,True,False,True,True,True,True,True,True,True,True,True,False,False,True,False,True,False,False,True,False,False,False,True,False,True,False,False,True,False,True,False,True,True,False,True,False,True,False,False,False,True,True,True,False,False,True,True,False,True,False,True,False,False,False,False,False,True,False,True,True,False,False,True,True,False,False,False,True,False,False,True,False,True,False,False,True,True,True,False,True,False,True,True,False,True,True,False,False,True,False,False,True,False,True,True,False,True,True,True,True,True,False,True,False,True,True,True,False,True,True,True,True,False,False,True,False,True,False,False,True,False,False,False,False,True,True,False,False,False,True,False,True,True,True,True,False,True,True,True,False,False,False,True,True,True,False,True,False,False,True,True,False,False,False,False,True,True,False,False,False,True,False,True,True,True,True,True,False,False,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,False,True,True,True,False,True,True,True,True,True,False,True,False,False,True,False,False,False,False,True,True,False,True,True,False,False,False,False,False,True,False,False,False,False,True,False,True,True,False,True,False,False,False,False,False,True,False,True,True,False,False,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,False,True,False,False,False,True,True,True,False,True,True,True,False,True,True,False,True,True,False,True,True,False,False,True,True,True,False,False,True,True,False,False,False,False,False,True,False,True,False,False,True,True,True,True,False,True,True,True,False,True,False,True,True,False,False,True,True,False,True,True,True,True,True,False,False,True,True,False,True,True,False,False,False,False,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False,False,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,True,False,True,False,False,False,False,False,False,False,True,True,True,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,True,True,True,False,True,False,True,True,True,True,True,False,False,True,False,False,False,False,True,True,False,False,False,True,False,True,False,True,True,True,True,False,False,False,True,True,False,False,False,False,False,False,False,False,True,False,False,True,False,True,False,False,True,True,True,False,False,True,True,True,False,False,False,False,False,True,False,True,True,False,True,True,False,True,True,False,True,True,True,True,True,False,True,False,True,False,False,True,True,False,True,True,False,True,True,True,False,True,False,True,False,True,True,False,False,False,False,True,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True,False,False,False,True,False,False,True,False,False,False,True,False,False,True,True,True,True,True,True,False,True,False,False,False,True,False,False,True,False,False,False,False,False,True,False,True,True,True,True,True,False,False,True,False,True,False,False,True,True,True,True,False,False,True,False,True,True,True,True,True,True,True,False,True,False,False,False,True,True,True,False,True,True,False,False,True,False,False,False,False,True,True,False,True,True,True,True,False,False,False,False,True,True,False,False,False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,False,False,False,True,False,True,False,True,False,False,True,False,True,False,False,True,False,False,False,False,True,True,False,False,True,False,True,False,False,False,True,True,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,False,True,True,False,False,False,False,True,True,False,False,True,False,True,False,True,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,True,False,False,True,True,False,True,False,True,True,False,False,False,True,False,True,True,True,True,False,False,False,True,True,False,True,False,False,True,True,True,False,False,True,False,True,True,True,True,False,True,True,False,True,True,False,False,False,False,True,True,False,False,False,True,False,False,True,False,True,True,False,True,True,True,True,False,True,True,True,True,False,False,False,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,False,False,True,False,True,True,True,True,False,False,False,True,False,True,True,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,True,True,True,True,True,False,False,False,False,False,True,False,True,True,True,True,True,False,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,True,True,True,True,True,False,True,True,True,False,True,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,False,False,False,True,True,True,False,True,True,False,False,False,True,False,True,False,False,True,True,True,False,True,True,True,False,True,False,True,False,False,False,True,True,False,False,False,False,False,True,True,True,False,True,False,False,True,False,False,False,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,True,True,True,False,False,True,False,False,False,True,True,False,True,True,False,False,False,False,False,True,True,False,False,False,True,True,True,False,False,True,False,False,False,False,False,False,True,False,True,True,True,False,False,True,True,False,True,True,False,False,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,True,True,True,False,False,True,False,False,False,False,True,True,True,True,False,False,True,True,True,True,False,False,True,False,True,True,True,False,False,False,True,False,True,False,False,True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,False,False,True,False,False,True,True,True,True,False,True,True,False,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,True,True,False,False,True,True,False,True,False,True,False,False,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,False,True,True,True,False,True,True,True,True,True,False,True,True,False,True,False,True,False,False,False,True,False,False,True,True,True,True,False,False,False,True,False,True,False,False,True,False,True,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,False,False,True,True,True,True,True,False,False,False,True,True,False,True,True,True,True,False,False,False,False,False,False,False,True,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,False,False,False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,True,True,False,True,True,True,True,False,True,False,False,False,True,True,False,False,True,True,True,True,True,True,False,False,True,True,True,True,True,False,True,False,True,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,False,False,False,False,True,False,False,False,True,True,True,False,True,False,True,False,True,True,False,True,False,False,True,True,False,False,True,False,False,False,True,False,False,True,False,True,False,False,True,True,True,False,False,False,True,True,False,False,False,False,False,False,False,True,True,True,True,False,True,True,False,False,False,False,True,False,True,True,True,False,True,False,True,True,True,False,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,False,False,True,False,True,False,False,False,False,True,True,True,True,True,True,False,True,True,False,True,True,False,False,True,True,False,True,True,False,False,False,False,False,True,False,True,True,True,False,True,False,True,True,False,True,False,False,False,True,False,False,False,False,False,True,True,False,True,True,False,True,True,True,True,False,True,False,True,False,False,False,True,False,True,True,True,True,True,True,False,True,True,True,False,False,False,True,False,True,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,True,False,True,True,False,False,False,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,True,False,True,False,True,False,False,True,False,False,True,True,True,False,False,True,True,False,False,True,False,True,True,True,True,True,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,False,True,False,False,True,False,True,True,True,True,False,False,False,True,True,True,False,False,False,False,False,False,False,False,False,True,False,True,False,True,True,False,False,False,True,True,False,False,False,True,True,False,False,False,True,True,True,True,True,True,False,True,False,False,True,False,True,False,True,True,True,False,False,True,False,True,True,False,True,True,False,False,False,False,False,True,True,False,True,True,True,True,False,True,True,False,True,True,False,False,False,True,True,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,False,True,False,True,False,False,True,False,True,True,False,True,False,True,False,False,True,True,False,True,False,True,True,True,False,True,False,False,False,False,False,True,True,False,False,True,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,False,True,False,True,True,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,False,True,False,True,False,False,False,True,True,True,True,False,False,True,False,True,True,False,True,True,False,False,False,False,True,False,True,True,False,False,True,False,True,True,False,False,False,False,True,True,True,False,True,True,True,True,True,False,True,False,True,True,True,True,False,False,False,True,False,False,True,True,True,True,True,True,True,True,True,False,False,False,False,True,False,False,True,True,False,False,True,False,False,False,True,False,True,True,True,True,False,True,False,True,False,True,False,True,False,True,True,False,True,True,False,True,True,True,False,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,False,False,False,False,True,True,True,False,True,False,True,True,False,True,False,False,True,False,False,True,True,True,False,True,False,True,False,True,False,False,False,False,False,False,False,True,True,True,True,True,False,False,False,False,True,True,False,False,True,True,True,False,False,False,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,False,True,False,True,False,True,False,True,True,False,True,True,False,True,False,False,True,False,True,True,True,True,False,False,True,True,True,True,True,True,False,False,True,False,True,True,True,True,False,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,True,True,True,True,False,True,True,False,False,False,True,True,True,False,True,False,True,True,False,True,False,True,False,False,True,True,False,True,False,False,True,True,True,True,False,True,False,False,False,False,False,True,True,True,False,False,False,True,False,False,False,False,True,True,True,True,False,True,False,False,True,False,False,False,True,False,True,True,False,True,True,False,True,False,False,True,False,False,False,False,False,True,True,False,False,False,True,False,True,True,True,False,True,True,False,False,True,True,True,False,True,False,False,False,False,False,True,True,False,True,True,True,False,False,True,False,False,False,True,True,True,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,False,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,False,True,False,True,True,False,True,False,True,True,False,False,False,True,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,True,True,False,False,True,True,True,False,False,True,True,True,True,True,True,True,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True,True,False,True,False,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,True,False,True,True,True,False,True,True,True,False,True,False,True,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False,False,False,False,False,False,True,True,True,True,False,False,False,True,False,True,False,True,False,False,False,False,True,False,True,False,True,False,False,True,False,False,True,False,False,True,True,True,True,False,True,True,True,True,False,True,False,True,False,True,True], dtype = "bool")#candidate|1762|(3328,)|const|bool
var_1763 = relay.var("var_1763", dtype = "uint64", shape = (12,))#candidate|1763|(12,)|var|uint64
call_1761 = relay.TupleGetItem(func_1239_call(relay.reshape(const_1762.astype('bool'), [16, 13, 16]), relay.reshape(var_1763.astype('uint64'), [12,]), ), 0)
call_1764 = relay.TupleGetItem(func_1243_call(relay.reshape(const_1762.astype('bool'), [16, 13, 16]), relay.reshape(var_1763.astype('uint64'), [12,]), ), 0)
func_1602_call = mod.get_global_var('func_1602')
func_1604_call = mutated_mod.get_global_var('func_1604')
call_1778 = func_1602_call()
call_1779 = func_1602_call()
func_1707_call = mod.get_global_var('func_1707')
func_1708_call = mutated_mod.get_global_var('func_1708')
call_1783 = relay.TupleGetItem(func_1707_call(), 1)
call_1784 = relay.TupleGetItem(func_1708_call(), 1)
output = relay.Tuple([uop_1735,call_1754,call_1761,const_1762,var_1763,call_1778,call_1783,])
output2 = relay.Tuple([uop_1737,call_1755,call_1764,const_1762,var_1763,call_1779,call_1784,])
func_1785 = relay.Function([var_1763,], output)
mod['func_1785'] = func_1785
mod = relay.transform.InferType()(mod)
var_1786 = relay.var("var_1786", dtype = "uint64", shape = (12,))#candidate|1786|(12,)|var|uint64
output = func_1785(var_1786)
func_1787 = relay.Function([var_1786], output)
mutated_mod['func_1787'] = func_1787
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1815 = relay.var("var_1815", dtype = "float32", shape = (4, 8, 13))#candidate|1815|(4, 8, 13)|var|float32
uop_1816 = relay.tan(var_1815.astype('float32')) # shape=(4, 8, 13)
output = uop_1816
output2 = uop_1816
func_1820 = relay.Function([var_1815,], output)
mod['func_1820'] = func_1820
mod = relay.transform.InferType()(mod)
mutated_mod['func_1820'] = func_1820
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1821 = relay.var("var_1821", dtype = "float32", shape = (4, 8, 13))#candidate|1821|(4, 8, 13)|var|float32
func_1820_call = mutated_mod.get_global_var('func_1820')
call_1822 = func_1820_call(var_1821)
output = call_1822
func_1823 = relay.Function([var_1821], output)
mutated_mod['func_1823'] = func_1823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1707_call = mod.get_global_var('func_1707')
func_1708_call = mutated_mod.get_global_var('func_1708')
call_1836 = relay.TupleGetItem(func_1707_call(), 0)
call_1837 = relay.TupleGetItem(func_1708_call(), 0)
var_1848 = relay.var("var_1848", dtype = "float64", shape = (128,))#candidate|1848|(128,)|var|float64
bop_1849 = relay.floor_divide(call_1836.astype('float32'), relay.reshape(var_1848.astype('float32'), relay.shape_of(call_1836))) # shape=(128,)
bop_1852 = relay.floor_divide(call_1837.astype('float32'), relay.reshape(var_1848.astype('float32'), relay.shape_of(call_1837))) # shape=(128,)
uop_1854 = relay.sqrt(var_1848.astype('float32')) # shape=(128,)
output = relay.Tuple([bop_1849,uop_1854,])
output2 = relay.Tuple([bop_1852,uop_1854,])
func_1858 = relay.Function([var_1848,], output)
mod['func_1858'] = func_1858
mod = relay.transform.InferType()(mod)
mutated_mod['func_1858'] = func_1858
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1859 = relay.var("var_1859", dtype = "float64", shape = (128,))#candidate|1859|(128,)|var|float64
func_1858_call = mutated_mod.get_global_var('func_1858')
call_1860 = func_1858_call(var_1859)
output = call_1860
func_1861 = relay.Function([var_1859], output)
mutated_mod['func_1861'] = func_1861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1707_call = mod.get_global_var('func_1707')
func_1708_call = mutated_mod.get_global_var('func_1708')
call_1869 = relay.TupleGetItem(func_1707_call(), 0)
call_1870 = relay.TupleGetItem(func_1708_call(), 0)
func_1820_call = mod.get_global_var('func_1820')
func_1823_call = mutated_mod.get_global_var('func_1823')
const_1899 = relay.const([-9.825467,6.941560,6.866414,-1.905766,-7.542128,7.757719,5.993597,-6.642119,1.475743,-3.480245,0.856345,-4.730513,5.547882,-6.062918,2.818069,2.668186,1.541463,7.291527,0.669235,-0.199702,5.267489,-1.114828,5.521993,5.739475,6.290238,-2.553794,-3.903834,7.206205,-7.730534,3.797431,1.535570,-3.816980,0.657964,-3.515047,2.255479,-7.235525,-9.462668,0.905180,-2.122236,-9.680579,5.065409,-2.820825,7.220679,1.593967,-8.091844,3.636033,9.381605,-4.379176,7.056442,1.511047,9.123926,9.858795,7.956336,9.639450,3.037117,0.354835,8.814574,3.658902,2.605999,-5.479457,9.512161,1.135064,1.072953,7.445189,-4.872079,3.502227,-4.287117,5.826320,-0.133547,3.923502,-5.213810,-7.194229,0.951767,-4.209228,-7.004276,-0.979752,-7.076382,-9.388041,7.213781,-7.231044,-6.414666,8.936938,4.163943,-4.919565,-8.038891,7.375997,-2.402312,-4.830948,3.492368,-3.265305,6.749181,2.722886,0.376381,-5.350980,0.303430,-9.343294,-0.909590,9.449194,6.802517,8.760236,5.763155,-7.995664,-2.670604,0.296461,-7.538401,3.124962,-1.454020,6.288997,-7.276189,-1.967955,9.906739,-7.298429,9.729838,1.826617,9.870304,-1.245578,1.003409,8.779745,7.014714,-9.387236,-8.232344,3.103703,-6.723352,-6.404102,-7.142899,8.203235,-0.309371,-2.380201,8.456321,-7.598562,-9.931244,9.004594,5.983465,-2.659544,-3.251409,-0.588709,-5.659008,4.735669,5.855491,-7.152009,4.468610,1.244149,9.555007,7.804291,8.381531,5.713499,-5.179004,3.571347,4.919770,-0.224823,-1.183222,8.869980,-5.851791,-5.526907,-1.528978,-2.747139,-1.356347,2.523673,8.041592,-3.201895,-6.683708,-2.153902,-8.024080,0.836778,8.773652,5.393269,-6.761825,6.562264,-1.056152,-8.537347,-9.060507,-1.888211,-4.663932,-7.200793,-3.598071,-8.157104,-2.155951,1.661315,7.852916,7.342419,-8.553647,-8.847936,2.202697,5.773210,7.560396,-3.184353,-3.068273,-7.524658,9.594428,-5.443036,9.302857,-6.488128,-7.079481,5.512992,-4.326819,-3.660776,5.701825,-4.808351,-3.793890,-1.077519,5.529880,9.569589,6.392193,8.015870,-7.634688,-2.666757,-3.263497,-2.554842,-6.953700,-2.968507,-8.293087,7.276381,-0.067280,-1.338954,-8.598554,-0.869002,4.317007,0.932932,-1.191812,9.499781,1.861354,-8.731454,2.569418,-2.376724,-4.806099,-4.786052,7.556845,9.558926,2.501012,1.570211,-6.842324,-2.836084,4.438372,2.416410,-2.524492,0.955389,-2.376559,5.151303,-0.408718,-3.336724,4.323702,8.175723,-6.155180,-6.107144,-0.523595,9.081541,5.322586,-0.792490,-5.973501,-2.272312,3.816281,-4.303095,-1.073845,7.293108,5.915988,1.772997,-1.477040,4.465864,5.512928,8.375527,3.881716,1.807430,-5.973098,-2.250197,9.290660,2.279494,-2.906507,-0.680309,9.074631,4.163971,9.497590,5.519071,3.587291,0.737403,-4.516188,-0.408943,7.201071,9.146950,8.176218,-8.659550,-1.079126,7.383973,3.502929,0.672024,9.387344,9.359754,-5.992096,3.723462,-9.890933,-4.113464,9.521325,-0.984319,-5.487466,-3.063519,5.448573,-3.275320,-8.974657,-2.511868,-6.237614,-4.019179,-3.163477,-8.974558,1.600226,-5.606398,-7.063441,-0.904231,4.241202,3.977020,-2.377195,-3.873363,-9.220271,-0.566932,-0.820757,2.035581,-8.142539,0.412350,3.800452,2.394945,7.818052,-4.941552,2.199749,5.898150,-7.369754,-1.657633,-5.595916,-3.752940,-5.520990,3.468171,-0.858430,5.480526,-1.769555,1.117034,-8.505653,-3.151644,1.220989,-8.836607,-2.004792,0.336913,-5.676379,0.431579,-7.060636,2.905687,-4.578364,-2.538535,6.778942,-0.031213,-3.496718,-7.773072,-3.280043,-7.184988,6.095140,-4.485698,-1.687957,-8.410697,-2.306960,8.327231,-6.101089,3.636477,6.316880,0.015601,7.193083,-7.640550,3.857933,-6.012494,-5.516591,3.592300,5.967657,8.340089,-8.659378,-4.821687,4.891238,4.449151,9.982475,3.481356,-3.215907,5.752277,-3.818074,5.002273,-3.896283,0.042002,-6.902376,7.605337,2.072932,7.822806,-8.897007,-9.395634,2.952196,9.623970,-2.162659,4.820206,0.700769,-9.049549,8.614074,-6.234086,8.623477,-1.469398,-5.237147,-4.445740,-7.268753,0.569673,9.920482,-2.727542,-4.447296,9.263624,-4.358903,2.044930,-8.581856,8.318225,-7.734657,1.953068,-0.454906,3.869346,8.169402,-7.743340,-6.333000,1.911233], dtype = "float32")#candidate|1899|(416,)|const|float32
call_1898 = func_1820_call(relay.reshape(const_1899.astype('float32'), [4, 8, 13]))
call_1900 = func_1820_call(relay.reshape(const_1899.astype('float32'), [4, 8, 13]))
output = relay.Tuple([call_1869,call_1898,const_1899,])
output2 = relay.Tuple([call_1870,call_1900,const_1899,])
func_1905 = relay.Function([], output)
mod['func_1905'] = func_1905
mod = relay.transform.InferType()(mod)
output = func_1905()
func_1906 = relay.Function([], output)
mutated_mod['func_1906'] = func_1906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1642_call = mod.get_global_var('func_1642')
func_1643_call = mutated_mod.get_global_var('func_1643')
call_1907 = relay.TupleGetItem(func_1642_call(), 1)
call_1908 = relay.TupleGetItem(func_1643_call(), 1)
uop_1929 = relay.cos(call_1907.astype('float32')) # shape=(2, 4, 16)
uop_1931 = relay.cos(call_1908.astype('float32')) # shape=(2, 4, 16)
func_1642_call = mod.get_global_var('func_1642')
func_1643_call = mutated_mod.get_global_var('func_1643')
call_1953 = relay.TupleGetItem(func_1642_call(), 2)
call_1954 = relay.TupleGetItem(func_1643_call(), 2)
bop_1956 = relay.floor_mod(call_1907.astype('float32'), relay.reshape(call_1953.astype('float32'), relay.shape_of(call_1907))) # shape=(2, 4, 16)
bop_1959 = relay.floor_mod(call_1908.astype('float32'), relay.reshape(call_1954.astype('float32'), relay.shape_of(call_1908))) # shape=(2, 4, 16)
output = relay.Tuple([uop_1929,bop_1956,])
output2 = relay.Tuple([uop_1931,bop_1959,])
func_1968 = relay.Function([], output)
mod['func_1968'] = func_1968
mod = relay.transform.InferType()(mod)
mutated_mod['func_1968'] = func_1968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1968_call = mutated_mod.get_global_var('func_1968')
call_1969 = func_1968_call()
output = call_1969
func_1970 = relay.Function([], output)
mutated_mod['func_1970'] = func_1970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1905_call = mod.get_global_var('func_1905')
func_1906_call = mutated_mod.get_global_var('func_1906')
call_2189 = relay.TupleGetItem(func_1905_call(), 1)
call_2190 = relay.TupleGetItem(func_1906_call(), 1)
output = relay.Tuple([call_2189,])
output2 = relay.Tuple([call_2190,])
func_2191 = relay.Function([], output)
mod['func_2191'] = func_2191
mod = relay.transform.InferType()(mod)
mutated_mod['func_2191'] = func_2191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2191_call = mutated_mod.get_global_var('func_2191')
call_2192 = func_2191_call()
output = call_2192
func_2193 = relay.Function([], output)
mutated_mod['func_2193'] = func_2193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1707_call = mod.get_global_var('func_1707')
func_1708_call = mutated_mod.get_global_var('func_1708')
call_2210 = relay.TupleGetItem(func_1707_call(), 0)
call_2211 = relay.TupleGetItem(func_1708_call(), 0)
func_1968_call = mod.get_global_var('func_1968')
func_1970_call = mutated_mod.get_global_var('func_1970')
call_2214 = relay.TupleGetItem(func_1968_call(), 1)
call_2215 = relay.TupleGetItem(func_1970_call(), 1)
func_1858_call = mod.get_global_var('func_1858')
func_1861_call = mutated_mod.get_global_var('func_1861')
call_2221 = relay.TupleGetItem(func_1858_call(relay.reshape(call_2210.astype('float64'), [128,])), 1)
call_2222 = relay.TupleGetItem(func_1861_call(relay.reshape(call_2210.astype('float64'), [128,])), 1)
func_1707_call = mod.get_global_var('func_1707')
func_1708_call = mutated_mod.get_global_var('func_1708')
call_2224 = relay.TupleGetItem(func_1707_call(), 0)
call_2225 = relay.TupleGetItem(func_1708_call(), 0)
output = relay.Tuple([call_2210,call_2214,call_2221,call_2224,])
output2 = relay.Tuple([call_2211,call_2215,call_2222,call_2225,])
func_2240 = relay.Function([], output)
mod['func_2240'] = func_2240
mod = relay.transform.InferType()(mod)
mutated_mod['func_2240'] = func_2240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2240_call = mutated_mod.get_global_var('func_2240')
call_2241 = func_2240_call()
output = call_2241
func_2242 = relay.Function([], output)
mutated_mod['func_2242'] = func_2242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1642_call = mod.get_global_var('func_1642')
func_1643_call = mutated_mod.get_global_var('func_1643')
call_2243 = relay.TupleGetItem(func_1642_call(), 0)
call_2244 = relay.TupleGetItem(func_1643_call(), 0)
output = call_2243
output2 = call_2244
func_2252 = relay.Function([], output)
mod['func_2252'] = func_2252
mod = relay.transform.InferType()(mod)
mutated_mod['func_2252'] = func_2252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2252_call = mutated_mod.get_global_var('func_2252')
call_2253 = func_2252_call()
output = call_2253
func_2254 = relay.Function([], output)
mutated_mod['func_2254'] = func_2254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2240_call = mod.get_global_var('func_2240')
func_2242_call = mutated_mod.get_global_var('func_2242')
call_2268 = relay.TupleGetItem(func_2240_call(), 1)
call_2269 = relay.TupleGetItem(func_2242_call(), 1)
var_2278 = relay.var("var_2278", dtype = "float32", shape = (2, 4, 16))#candidate|2278|(2, 4, 16)|var|float32
bop_2279 = relay.maximum(call_2268.astype('int64'), relay.reshape(var_2278.astype('int64'), relay.shape_of(call_2268))) # shape=(2, 4, 16)
bop_2282 = relay.maximum(call_2269.astype('int64'), relay.reshape(var_2278.astype('int64'), relay.shape_of(call_2269))) # shape=(2, 4, 16)
output = bop_2279
output2 = bop_2282
func_2291 = relay.Function([var_2278,], output)
mod['func_2291'] = func_2291
mod = relay.transform.InferType()(mod)
mutated_mod['func_2291'] = func_2291
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2292 = relay.var("var_2292", dtype = "float32", shape = (2, 4, 16))#candidate|2292|(2, 4, 16)|var|float32
func_2291_call = mutated_mod.get_global_var('func_2291')
call_2293 = func_2291_call(var_2292)
output = call_2293
func_2294 = relay.Function([var_2292], output)
mutated_mod['func_2294'] = func_2294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1642_call = mod.get_global_var('func_1642')
func_1643_call = mutated_mod.get_global_var('func_1643')
call_2301 = relay.TupleGetItem(func_1642_call(), 1)
call_2302 = relay.TupleGetItem(func_1643_call(), 1)
output = relay.Tuple([call_2301,])
output2 = relay.Tuple([call_2302,])
func_2322 = relay.Function([], output)
mod['func_2322'] = func_2322
mod = relay.transform.InferType()(mod)
output = func_2322()
func_2323 = relay.Function([], output)
mutated_mod['func_2323'] = func_2323
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2462 = relay.var("var_2462", dtype = "float32", shape = (4, 14, 9))#candidate|2462|(4, 14, 9)|var|float32
uop_2463 = relay.log2(var_2462.astype('float32')) # shape=(4, 14, 9)
func_1968_call = mod.get_global_var('func_1968')
func_1970_call = mutated_mod.get_global_var('func_1970')
call_2468 = relay.TupleGetItem(func_1968_call(), 1)
call_2469 = relay.TupleGetItem(func_1970_call(), 1)
output = relay.Tuple([uop_2463,call_2468,])
output2 = relay.Tuple([uop_2463,call_2469,])
func_2478 = relay.Function([var_2462,], output)
mod['func_2478'] = func_2478
mod = relay.transform.InferType()(mod)
mutated_mod['func_2478'] = func_2478
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2479 = relay.var("var_2479", dtype = "float32", shape = (4, 14, 9))#candidate|2479|(4, 14, 9)|var|float32
func_2478_call = mutated_mod.get_global_var('func_2478')
call_2480 = func_2478_call(var_2479)
output = call_2480
func_2481 = relay.Function([var_2479], output)
mutated_mod['func_2481'] = func_2481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1905_call = mod.get_global_var('func_1905')
func_1906_call = mutated_mod.get_global_var('func_1906')
call_2494 = relay.TupleGetItem(func_1905_call(), 2)
call_2495 = relay.TupleGetItem(func_1906_call(), 2)
var_2498 = relay.var("var_2498", dtype = "float32", shape = (416,))#candidate|2498|(416,)|var|float32
bop_2499 = relay.floor_divide(call_2494.astype('float32'), relay.reshape(var_2498.astype('float32'), relay.shape_of(call_2494))) # shape=(416,)
bop_2502 = relay.floor_divide(call_2495.astype('float32'), relay.reshape(var_2498.astype('float32'), relay.shape_of(call_2495))) # shape=(416,)
func_834_call = mod.get_global_var('func_834')
func_836_call = mutated_mod.get_global_var('func_836')
const_2514 = relay.const([3,1,10,3,-7,6,-10,4,-6,-10,-6,-8,1,5,8,-5,3,-4,-5,-3,-5,6,-1,7,-5,-4,4,-9,8,7,8,-9,-9,8,-10,-6,-1,10,-3,7,-6,1,5,-4,-6,10,-2,-8,2,5,-6,-6,-5,7,7,-8,-7,10,-8,6,5,9,7,-8,-3,2,6,-4,-6,7,-9,6,-3,-9,-3,5,2,-5,1,-7,-8,4,7,-3,3,8,-6,-7,5,7,10,5,-6,-1,4,3,-7,6,-7,10,-8,1,5,2,-3,-7,1,-4,-2,5,-5,8,7,7,-10,5,5,3,-3,1,5,8,-10,4,9,6,2,-7,9,-5,1,8,-6,-8,-7,3,-7,-8,3,-8,5,-8,9,6,-1,8,10,10,8,-5,8,-7,-8,3,10,6,5,-2,1,-4,-2,-4,8,-8,-5,1,2,-10,4,-2,5,2,3,-6,-6,9,-1,-10,-9,5,-3,7,6,-4,1,7,-7,5,2,6,-10,-6,10,-1,-4,2,3,-3,-7,9,4,-3,4,-2,-9,-6,5,-3,-8,3,1,9,7,4,8,3,1,6,-3,-4,9,5,-4,9,3,3,-1,9,-4,-1,8,8,-9,-7,-3,9,4,7,10,-7,-10,-8,-5,-9,2,3,6,-1,8,-1,2,-4,-4,4,7,-9,-4,-9,4,7,-2,7,-4,4,10,-2,5,-9,-6,-5,4,3,-2,4,2,1,-4,3,9,-9,-3,1,8,1,3,-9,1,-3,-4,-9,10,2,10,-3,3,8,-6,5,9,10,-1,6,-10,-5,10,3,-5,6,-2,-4,3,-10,9,3,-3,-9,-1,-8,-8,7,8,9,-7,-7,-6,-4,3,9,1,-1,6,-1,-6,2,-4,1,-1,3,7,-6,1,3,-6,-5,6,-1,5,-1,-1,-3,2,-6,6,10,9,8,10,3,4,10,3,4,3,9,8,10,-7,4,6,-7,-4,5,8,7,-8,-4,8,1,5,7,1,5,4,1,5,-4,-5,-2,-1,-5,-8,1,8,9,-3,9,6,2,-5,-9,-1,9,6,-10,-2,5,5,8,-2,-7,5,-7,-9,-10,-1,3,4,9,7,6,-4,9,-8,3,4,-3,3,2,8,-4,-3,-3,3,8,3,9,-6,7,5,-4,-7,10,8,1,5,6,-4,-8,3,7,1,-3,4,1,-9,10,3,-7,-3,-8,6,8,-5,9,2,3,-1,8,-6,5,-3,1,-7,6,9,-8,-10,-4,-3,-2,-10,8,-3,7,5,-5,8,-6,-6,-5,-8,7,1,2,6,-9,-1,8,-3,-1,8,1,-2,3,1,3,2,7,3,7,5,6,3,8,-10,6,-7,-7,4,-8,-7,6,1,5,3,5,-2,-4,6,10,-4,-5,-5,-1,2,4,10,-1,3,7,1,-6,3,-7,3,-5,6,-8,-4,-10,8,-6,-5,-1,6,-6,10,-10,-3,1,4,3,-8,1,-1,8,4,-10,-4,7,3,-7,-9,-5,3,8,-4,7,3,-3,6,6,5,1,8,-9,5,-3,2,5,-6,1,8,-1,6,7,-5,-4,-8,-10,-4,9,-5,-2,-2,10,-3,-9,3,-2,-4,-2,10,9,-2,-4,6,-6,6,7,8,-8,-10,-10,5,-1,8,7,-9,4,3,-10,3,-1,-5,-7,-6,3,-1,1,2,-6,5,-6,10,-8,2,-6,-5,4,-3,-4,-7,5,8,2,7,-10,-3,-9,-10,8,6,-7,-8,2,3,10,-4,5,-10,4,7,10,-2,-1,-5,-6,-2,3,-5,3,2,5,-8,-10,9,6,7,4,-2,-6,5,-7,5,10,4,8,-9,-1,-5,-7,-4,8,6,3,-8,-6,-10,-1,2,7,-7,1,-9,-2,5,7,-10,-3,7,-6,-4,8,-5,3,2,-3,-6,-4,-9,9,6,5,3,4,-3,-6,5,3,5,-7,-7,-8,7,9,-8,1,-6,-10,2,10,-6,-4,-2,-3,2,-6,10,-3,-5,2,1,-7,-10,10,3,-9,8,-2,-10,-7,-4,-3,-4,3,7,3,1,-8,9,4,8,4,7,-6,2,-1,-4,-3,1,10,-3,9,-4,-4,-5,-8,-4,-10,-8,-9,-10,7,7,4,7,-7,6,-4,-10,-7,7,-7,8,1,4,8,-2,-7,6,6,-5,4,6,-4,-6,-3,-6,3,8,2,6,7,7,-9,-7,-8,8,4,10,4,10,-9,8,2,8,9,6,-3,1,-5,7,-1,-5,-10,-2,1,10,10,-3,-3,6,4,9,4,9,10,-5,2,-5,-5,7,-1,-7,6,-3,1,-4,-3,2,6,-7,9,7,-1,4,-9,3,1,-1,2,-7,-5,-7,5,-4,-3,7,-4,-1,-7,1,5,8,-8,4,-2,2,-3,6,8,-1,2,1,2,-8,-7,5,-7,-2,1,-4,7,2,2,-10,-5,-3,8,-2,-8,-9,3,8,6,-2,6,-10,1,2,10,-6,-10,-4,3,-9,8,5,-2,9,5,-5,-9,-3,-8,4,7,-5,-10,-5,4,-3,10,2,-5,9,6,2,-8,-8,9,4,-3,-3,5,6,-2,2,9,3,8,-5,-4,2,1,8,-1,6,-1,-6,4,8,1,7,7,-5,2,9,-6,-1,10,-6,4,-4,-8,-1,-2], dtype = "uint32")#candidate|2514|(1008,)|const|uint32
call_2513 = func_834_call(relay.reshape(const_2514.astype('uint32'), [14, 6, 12]))
call_2515 = func_834_call(relay.reshape(const_2514.astype('uint32'), [14, 6, 12]))
output = relay.Tuple([bop_2499,call_2513,const_2514,])
output2 = relay.Tuple([bop_2502,call_2515,const_2514,])
func_2541 = relay.Function([var_2498,], output)
mod['func_2541'] = func_2541
mod = relay.transform.InferType()(mod)
var_2542 = relay.var("var_2542", dtype = "float32", shape = (416,))#candidate|2542|(416,)|var|float32
output = func_2541(var_2542)
func_2543 = relay.Function([var_2542], output)
mutated_mod['func_2543'] = func_2543
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2611 = relay.var("var_2611", dtype = "float32", shape = (13, 4, 16))#candidate|2611|(13, 4, 16)|var|float32
var_2612 = relay.var("var_2612", dtype = "float32", shape = (13, 4, 16))#candidate|2612|(13, 4, 16)|var|float32
bop_2613 = relay.floor_mod(var_2611.astype('float32'), relay.reshape(var_2612.astype('float32'), relay.shape_of(var_2611))) # shape=(13, 4, 16)
uop_2616 = relay.sqrt(var_2612.astype('float64')) # shape=(13, 4, 16)
uop_2626 = relay.acos(uop_2616.astype('float64')) # shape=(13, 4, 16)
func_1707_call = mod.get_global_var('func_1707')
func_1708_call = mutated_mod.get_global_var('func_1708')
call_2630 = relay.TupleGetItem(func_1707_call(), 0)
call_2631 = relay.TupleGetItem(func_1708_call(), 0)
bop_2644 = relay.divide(var_2611.astype('float64'), relay.reshape(var_2612.astype('float64'), relay.shape_of(var_2611))) # shape=(13, 4, 16)
bop_2649 = relay.mod(uop_2626.astype('float64'), relay.reshape(uop_2616.astype('float64'), relay.shape_of(uop_2626))) # shape=(13, 4, 16)
bop_2667 = relay.less(uop_2626.astype('bool'), relay.reshape(var_2611.astype('bool'), relay.shape_of(uop_2626))) # shape=(13, 4, 16)
bop_2680 = relay.add(bop_2649.astype('int16'), relay.reshape(uop_2626.astype('int16'), relay.shape_of(bop_2649))) # shape=(13, 4, 16)
uop_2696 = relay.tan(uop_2626.astype('float32')) # shape=(13, 4, 16)
func_1602_call = mod.get_global_var('func_1602')
func_1604_call = mutated_mod.get_global_var('func_1604')
call_2698 = func_1602_call()
call_2699 = func_1602_call()
func_907_call = mod.get_global_var('func_907')
func_912_call = mutated_mod.get_global_var('func_912')
const_2701 = relay.const([-5,-6,-9,-9,2,-10,-10,-2,-2,8,2,4,10,-9,-3,8,1,7,8,10,9,-2,5,-1,-1,-9,-2,2,4,8,2,-7,2,10,10,-10,9,8,-6,-3,10,1,-4,4,6,3,-10,8,4,1,-7,-3,-5,-4,-1,-1,8,5,-4,-10,-10,6,-3,1,-4,1,7,2,4,6,-3,-8,-8,-5,-9,3,-7,-9,-7,10,-5,5,-5,-6,2,-6,-9,-8,-5,-9,9,6,-5,8,7,3,1,6,2,-6,-3,9,-7,9,1,8,2,-6,1,8,2,-10,7,8,9,6,-6,-6,-2,-5,-4,1,-7,4,-10,3,-4,-6,2,-2,8,5,-3,-7,5,-7,2,-9,-6,-4,5,-10,-4,-2,10,5,4,-4,-10,-1,10,8,-8,3,-7,-10,-6,-3,-5,-5,3,-5,-2,1,7,-9,-1,-10,-3,1,-2,4,1,8,-4,-3,5,-3,4,-2,-7,-9,-7,7,4,10,9,5,3,8,-6,-6,8,1,5,-4,-4,1,5,-3,-6,-6,9,4,3,-3,4,4,-9,5,-6,-6,-3,-4,-5,-9,2,-5,-7,6,3,-2,9,1,9,-1,5,7,-6,-8,2,1,5,8,5,3,-1,6,-1,7,-3,6,8,7,6,5,5,3,-2,-1,3,6,10,-4,-3,10,-1,-3,8,3,7,4,-3,-3,8,-3,-9,6,3,10,-3,1,5,-5,7,-8,9,8,1,-7,5,-9,-1,4,7,1,2,-5,7,1,1,8,-1,2,-8,-10,-10,-7,-6,-4,-5,-4,-6,-6,-1,7,-6,2,1,-1,4,2,-2,5,-10,-2,4,3,-7,5,6,1,-6,1,-8,8,4,6,-9,-6,7,-5,6,-3,9,-2,-7,-6,8,2,-10,8,2,-1,-4,-1,7,-4,-8,-7,-2,-3,-1,-5,8,7,-10,1,-10,5,3,4,4,4,-4,8,-9,-8,1,1,3,-5,-4,4,-3,5,5,-6,9,2,1,3,2,-2,7,10,3,2,6,-1,-5,4,10,-10,10,-4,1,-2,-3,5,10,-9,-5,-2,8,-9,-4,4,3,-2,-5,5,-8,-10,1,-10,-3,8,1,-8,-5,-2,9,10,-8,-6,-1,-1,-6,-9,-8,-10], dtype = "uint16")#candidate|2701|(432,)|const|uint16
const_2702 = relay.const([8,9,-6,2,3,2,5,8,-4,-10,7,8], dtype = "uint64")#candidate|2702|(12,)|const|uint64
const_2703 = relay.const([-4,-5,-4,-10,9,-7,-4,10,4,7,-7,-2,-6,3,6,9,6,2,9,2,7,-6,-10,6,-4,-9,-4,7,9,-5,9,-6,10,-4,-9,4,8,9,-8,5,8,2,4,-3,1,-7,-3,-5,10,-1,-8,8,-7,-5,4,7,-1,-5,10,7], dtype = "uint64")#candidate|2703|(60,)|const|uint64
call_2700 = relay.TupleGetItem(func_907_call(relay.reshape(const_2701.astype('uint16'), [4, 12, 9]), relay.reshape(const_2702.astype('uint64'), [12,]), relay.reshape(const_2703.astype('uint64'), [60, 1]), ), 2)
call_2704 = relay.TupleGetItem(func_912_call(relay.reshape(const_2701.astype('uint16'), [4, 12, 9]), relay.reshape(const_2702.astype('uint64'), [12,]), relay.reshape(const_2703.astype('uint64'), [60, 1]), ), 2)
output = relay.Tuple([bop_2613,call_2630,bop_2644,bop_2667,bop_2680,uop_2696,call_2698,call_2700,const_2701,const_2702,const_2703,])
output2 = relay.Tuple([bop_2613,call_2631,bop_2644,bop_2667,bop_2680,uop_2696,call_2699,call_2704,const_2701,const_2702,const_2703,])
func_2708 = relay.Function([var_2611,var_2612,], output)
mod['func_2708'] = func_2708
mod = relay.transform.InferType()(mod)
mutated_mod['func_2708'] = func_2708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2708_call = mutated_mod.get_global_var('func_2708')
var_2710 = relay.var("var_2710", dtype = "float32", shape = (13, 4, 16))#candidate|2710|(13, 4, 16)|var|float32
var_2711 = relay.var("var_2711", dtype = "float32", shape = (13, 4, 16))#candidate|2711|(13, 4, 16)|var|float32
call_2709 = func_2708_call(var_2710,var_2711,)
output = call_2709
func_2712 = relay.Function([var_2710,var_2711,], output)
mutated_mod['func_2712'] = func_2712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1905_call = mod.get_global_var('func_1905')
func_1906_call = mutated_mod.get_global_var('func_1906')
call_2724 = relay.TupleGetItem(func_1905_call(), 1)
call_2725 = relay.TupleGetItem(func_1906_call(), 1)
var_2728 = relay.var("var_2728", dtype = "float32", shape = (4, 8, 13))#candidate|2728|(4, 8, 13)|var|float32
bop_2729 = relay.floor_divide(call_2724.astype('float64'), relay.reshape(var_2728.astype('float64'), relay.shape_of(call_2724))) # shape=(4, 8, 13)
bop_2732 = relay.floor_divide(call_2725.astype('float64'), relay.reshape(var_2728.astype('float64'), relay.shape_of(call_2725))) # shape=(4, 8, 13)
func_2291_call = mod.get_global_var('func_2291')
func_2294_call = mutated_mod.get_global_var('func_2294')
var_2746 = relay.var("var_2746", dtype = "float32", shape = (128,))#candidate|2746|(128,)|var|float32
call_2745 = func_2291_call(relay.reshape(var_2746.astype('float32'), [2, 4, 16]))
call_2747 = func_2291_call(relay.reshape(var_2746.astype('float32'), [2, 4, 16]))
output = relay.Tuple([bop_2729,call_2745,var_2746,])
output2 = relay.Tuple([bop_2732,call_2747,var_2746,])
func_2749 = relay.Function([var_2728,var_2746,], output)
mod['func_2749'] = func_2749
mod = relay.transform.InferType()(mod)
var_2750 = relay.var("var_2750", dtype = "float32", shape = (4, 8, 13))#candidate|2750|(4, 8, 13)|var|float32
var_2751 = relay.var("var_2751", dtype = "float32", shape = (128,))#candidate|2751|(128,)|var|float32
output = func_2749(var_2750,var_2751,)
func_2752 = relay.Function([var_2750,var_2751,], output)
mutated_mod['func_2752'] = func_2752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1642_call = mod.get_global_var('func_1642')
func_1643_call = mutated_mod.get_global_var('func_1643')
call_2769 = relay.TupleGetItem(func_1642_call(), 1)
call_2770 = relay.TupleGetItem(func_1643_call(), 1)
output = relay.Tuple([call_2769,])
output2 = relay.Tuple([call_2770,])
func_2775 = relay.Function([], output)
mod['func_2775'] = func_2775
mod = relay.transform.InferType()(mod)
output = func_2775()
func_2776 = relay.Function([], output)
mutated_mod['func_2776'] = func_2776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1707_call = mod.get_global_var('func_1707')
func_1708_call = mutated_mod.get_global_var('func_1708')
call_2784 = relay.TupleGetItem(func_1707_call(), 1)
call_2785 = relay.TupleGetItem(func_1708_call(), 1)
output = call_2784
output2 = call_2785
func_2786 = relay.Function([], output)
mod['func_2786'] = func_2786
mod = relay.transform.InferType()(mod)
output = func_2786()
func_2787 = relay.Function([], output)
mutated_mod['func_2787'] = func_2787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1602_call = mod.get_global_var('func_1602')
func_1604_call = mutated_mod.get_global_var('func_1604')
call_2792 = func_1602_call()
call_2793 = func_1602_call()
func_2291_call = mod.get_global_var('func_2291')
func_2294_call = mutated_mod.get_global_var('func_2294')
const_2806 = relay.const([-2.550625,5.217607,-4.770155,-6.232054,8.332790,-2.705605,0.291098,2.079849,0.750347,-6.013746,1.475499,-6.261372,-0.332916,8.221380,6.791296,-1.028389,0.487622,8.177555,6.929806,-6.837153,-3.762374,-0.599768,4.069165,-1.032352,6.765062,-3.163864,-3.925972,-7.622990,1.451567,-0.353848,8.296771,-8.819177,-0.987059,-5.192147,1.087300,5.291685,-4.600386,8.801893,6.101228,-4.146308,-8.248688,3.949315,9.523478,-3.541890,-4.219412,5.899850,8.523559,-5.545335,-2.676233,0.899882,0.250760,2.426783,-9.644945,9.482786,-2.681922,-1.247041,-6.708104,-6.323560,7.852972,-5.167919,6.264924,0.643241,9.126368,1.083371,9.847975,6.280664,3.449932,-6.908212,-3.646541,9.725023,6.853711,5.574173,-4.123385,5.172873,-4.989098,8.075103,-9.938301,-8.849085,-3.241243,2.932351,-7.857967,-4.027670,9.593161,1.760352,-8.247610,-3.385166,1.213920,6.951692,3.357578,0.405747,0.214121,-6.021127,-6.228910,3.677403,-1.278702,-9.212588,-5.944258,-4.696725,9.343671,3.438630,-0.722630,4.422569,7.934823,4.848636,2.035334,2.810796,1.683283,-4.918199,-9.097051,-9.028180,-1.721847,-0.948552,1.006633,-1.748084,-9.499032,-2.269208,-9.418678,-2.747255,8.772211,-9.101263,9.367294,1.437718,3.872693,-7.969538,1.840270,-0.227375,7.326822,-8.532712], dtype = "float32")#candidate|2806|(128,)|const|float32
call_2805 = func_2291_call(relay.reshape(const_2806.astype('float32'), [2, 4, 16]))
call_2807 = func_2291_call(relay.reshape(const_2806.astype('float32'), [2, 4, 16]))
func_2478_call = mod.get_global_var('func_2478')
func_2481_call = mutated_mod.get_global_var('func_2481')
const_2818 = relay.const([-8.375066,-5.166971,-8.820547,-8.628325,4.280330,-3.598253,-9.789658,7.884177,-0.882547,-7.275196,0.382360,5.764225,7.627746,-6.243102,-1.573719,-3.100065,-3.879940,5.443330,-4.190257,-8.136337,2.047840,-3.143428,-5.438298,9.192699,9.453221,6.358296,-9.843815,-7.163425,-9.605868,-7.988130,-7.331065,-6.629506,1.575035,3.666207,0.412986,-3.576273,1.391424,-2.950071,-0.558461,-5.015932,2.920829,-0.994620,-5.466377,-4.277578,-0.877000,2.214829,3.697791,9.184280,7.681645,-0.415803,3.307698,-9.038068,1.300620,-9.148559,-0.006040,-0.116946,-1.070787,3.363281,4.060946,0.191492,-8.462310,-3.763148,-8.952097,3.286503,1.041352,3.672099,-8.134660,9.903462,-0.314982,8.650690,-6.181445,6.916460,-1.102153,-8.971246,-6.559337,2.167470,-8.573652,-4.940705,-0.260570,2.971899,2.657856,-8.686203,-5.642631,-1.509400,4.721909,6.158342,5.793005,-3.137437,-5.303097,3.211053,-7.968453,6.648466,-2.913249,-6.019402,5.097068,-4.360010,-5.875122,-8.642101,-0.592007,5.275499,-0.707469,-2.326244,1.779528,-8.191218,1.264957,-9.406886,-5.477827,-3.145150,4.158064,8.201371,-4.588463,-7.600569,-0.691617,9.146250,9.641302,-8.922369,-0.252380,3.854037,5.864550,1.578751,5.905379,7.453933,9.176432,-4.055113,-9.022388,-7.078000,-1.456059,2.071978,6.943190,2.325129,1.092293,7.487278,-8.747034,-1.989003,-6.103229,-5.019257,1.474498,2.793449,-7.884395,-4.102858,-3.419533,7.125682,7.125566,9.699429,-8.178652,7.390113,0.307630,2.542507,3.816147,4.991160,9.539047,3.936718,5.345317,7.586544,-1.034376,-5.867221,-6.324506,6.893389,-5.951781,3.152062,-9.795288,5.549814,7.426043,0.966430,-6.625961,-9.846008,4.022446,-3.597845,-8.575942,-6.806252,6.153938,0.157141,-9.930835,4.047897,-0.275670,8.606282,7.432863,-4.240226,2.454747,2.211458,-7.695217,1.664532,6.601518,9.721117,-6.675988,3.209627,-4.078883,9.945117,9.797283,-9.893399,5.324157,-3.950516,-7.752778,7.869130,1.707439,3.707451,-2.362282,6.973848,-2.979288,-6.721485,-1.870131,7.856709,-9.887078,3.999365,2.603819,2.804344,-4.727824,-1.113637,-8.577028,-3.024999,-2.554388,-0.889299,2.324707,0.752648,-4.867101,-7.471750,4.122120,7.816969,-3.057446,5.480491,-5.545676,5.413085,3.287159,1.077764,1.523700,9.458806,9.892093,3.085031,1.816791,1.562161,-6.445029,-2.651744,6.272591,3.781261,-3.927604,6.798882,-0.902824,7.920595,-2.566946,4.428309,3.939327,-1.235823,-4.940057,7.919953,-9.653977,9.950304,-4.504288,-3.866656,-2.485453,2.205957,-9.984095,0.046316,9.824665,-0.178053,-3.133230,-6.117522,-8.285547,-2.134930,-7.646186,-9.701410,-4.925484,7.570152,6.676864,-3.152067,0.592619,5.267517,4.127431,-2.714715,9.329964,-9.177052,5.709900,2.385689,0.179749,-8.454977,3.577691,-9.076599,7.048750,-2.447771,5.267054,-5.559562,9.147970,9.687079,-9.181662,8.177013,-6.519575,8.858717,-0.595974,-8.364576,0.436597,1.631526,5.002621,-0.229835,5.903246,-0.542408,-9.804891,-2.989880,-5.334033,-7.935330,2.043246,-5.037281,6.315501,1.320252,7.583432,-2.296369,2.703266,4.466502,3.115110,9.796185,6.625488,-0.785546,-7.015129,2.375639,-0.936036,2.626389,9.170201,1.858185,-9.246132,4.652084,-3.018390,-2.379010,9.751829,6.961146,5.837482,-3.464899,-5.790639,-5.918361,2.578666,2.240868,6.591085,5.964184,-3.230850,-4.822563,-1.931931,-4.310836,9.176025,-2.721355,4.598556,1.715456,-5.412702,4.483789,-1.661496,7.414670,2.757953,8.356554,2.723423,2.217884,-7.761709,-4.262899,4.881053,4.209326,9.922957,-2.762261,8.071895,-3.932467,3.756746,-0.991483,3.203244,2.620230,-9.714222,-1.474361,1.257960,-4.761549,3.199115,-3.760457,6.314304,1.763318,2.181074,8.766900,0.930873,-6.994172,7.426499,1.995011,-3.501358,3.908811,5.774250,4.111154,-6.223265,-2.895275,-2.766849,-9.014568,9.650603,0.481055,6.490554,0.897818,-6.363041,8.989476,1.973473,-0.155636,4.468910,-6.685328,3.442671,-1.809671,0.993493,7.445588,3.777222,-3.801966,8.290668,-2.967655,-2.757316,-8.193976,8.040751,8.038458,-4.565271,8.261016,0.596385,-4.977095,0.955067,-4.310286,-2.872872,-5.359510,-1.830612,-6.790922,-8.249123,-5.969338,-8.278943,1.480266,6.970098,-8.141990,2.145784,4.855723,-3.449954,5.475740,-4.011148,-0.791103,-8.961894,7.594424,8.704944,-7.303665,-6.652119,5.124669,3.794185,-4.150552,1.814039,-7.520806,-3.458042,4.144909,-9.704158,-1.107164,9.531208,3.727496,-3.702856,-6.799144,-5.843552,5.305836,2.524451,1.344174,-3.450945,7.165658,3.185331,-8.885800,-2.345812,-9.174858,-0.786357,5.046168,7.081614,3.183521,8.581339,-5.516986,2.168597,-6.194226,-1.983300,2.676945,-0.758847,-0.271255,6.746332,8.336254,-4.157736,-4.100500,0.463643,-1.741859,-2.208630,-8.108748,9.251364,7.202542,-3.473340,-4.227714,7.734196,8.549846,-1.877076,1.159263,-1.857443,0.029149,-9.477323,-2.744172,-8.056138,5.131217,-6.168687,-3.031052,-3.556667,-1.120737,-1.741528,0.692045,5.974525,4.716602,-7.930993,7.516810,7.369001,6.906958,-7.088191,3.290438,8.356417,6.386498,-5.953649,5.685533], dtype = "float32")#candidate|2818|(504,)|const|float32
call_2817 = relay.TupleGetItem(func_2478_call(relay.reshape(const_2818.astype('float32'), [4, 14, 9])), 1)
call_2819 = relay.TupleGetItem(func_2481_call(relay.reshape(const_2818.astype('float32'), [4, 14, 9])), 1)
output = relay.Tuple([call_2792,call_2805,const_2806,call_2817,const_2818,])
output2 = relay.Tuple([call_2793,call_2807,const_2806,call_2819,const_2818,])
func_2824 = relay.Function([], output)
mod['func_2824'] = func_2824
mod = relay.transform.InferType()(mod)
mutated_mod['func_2824'] = func_2824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2824_call = mutated_mod.get_global_var('func_2824')
call_2825 = func_2824_call()
output = call_2825
func_2826 = relay.Function([], output)
mutated_mod['func_2826'] = func_2826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1905_call = mod.get_global_var('func_1905')
func_1906_call = mutated_mod.get_global_var('func_1906')
call_2941 = relay.TupleGetItem(func_1905_call(), 0)
call_2942 = relay.TupleGetItem(func_1906_call(), 0)
var_2954 = relay.var("var_2954", dtype = "float64", shape = (128,))#candidate|2954|(128,)|var|float64
bop_2955 = relay.add(call_2941.astype('uint32'), relay.reshape(var_2954.astype('uint32'), relay.shape_of(call_2941))) # shape=(128,)
bop_2958 = relay.add(call_2942.astype('uint32'), relay.reshape(var_2954.astype('uint32'), relay.shape_of(call_2942))) # shape=(128,)
var_2960 = relay.var("var_2960", dtype = "float64", shape = (128,))#candidate|2960|(128,)|var|float64
bop_2961 = relay.minimum(var_2954.astype('uint64'), relay.reshape(var_2960.astype('uint64'), relay.shape_of(var_2954))) # shape=(128,)
output = relay.Tuple([bop_2955,bop_2961,])
output2 = relay.Tuple([bop_2958,bop_2961,])
func_2966 = relay.Function([var_2954,var_2960,], output)
mod['func_2966'] = func_2966
mod = relay.transform.InferType()(mod)
var_2967 = relay.var("var_2967", dtype = "float64", shape = (128,))#candidate|2967|(128,)|var|float64
var_2968 = relay.var("var_2968", dtype = "float64", shape = (128,))#candidate|2968|(128,)|var|float64
output = func_2966(var_2967,var_2968,)
func_2969 = relay.Function([var_2967,var_2968,], output)
mutated_mod['func_2969'] = func_2969
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2973 = relay.var("var_2973", dtype = "uint16", shape = (11, 11, 10))#candidate|2973|(11, 11, 10)|var|uint16
const_2974 = relay.const([[[-4,-7,-1,7,-4,-5,-8,4,-9,7],[2,3,-2,-3,-5,-3,2,-7,8,-9],[1,-3,1,5,8,9,5,-4,-8,-3],[2,1,-7,8,-4,-8,-1,4,-10,-5],[2,-6,6,3,7,-7,2,-2,6,-4],[7,5,-3,-1,9,-1,9,-5,9,1],[4,6,5,6,-8,-4,-2,-2,-10,-10],[-8,-10,-10,4,-5,-7,10,-6,1,-8],[4,-3,-3,-5,-9,-1,-8,6,8,-9],[-4,1,-10,-10,-10,-10,-10,-3,10,-5],[-5,-8,9,-10,5,-1,4,4,10,-4]],[[2,-7,7,-7,-9,7,-1,6,-10,-9],[4,3,-2,1,-1,-4,-9,7,-4,4],[-9,9,8,1,10,5,2,1,5,7],[6,-8,4,-2,2,-4,-9,-2,-8,6],[-5,-1,9,10,-5,1,-10,-8,-6,3],[-8,-8,1,3,5,7,-2,-6,4,6],[-4,-3,-8,9,1,4,2,-6,4,-2],[1,-8,10,4,1,-3,9,-3,7,10],[7,-7,8,2,3,10,3,-8,3,9],[4,-2,8,-9,-7,-10,5,-1,-3,4],[7,1,-3,7,1,-9,-7,-7,4,7]],[[6,-6,-9,3,-2,-7,2,-10,-6,-10],[-2,1,10,4,3,9,-3,10,2,1],[2,-4,5,-1,1,-8,-2,4,-9,10],[-2,-3,2,6,-7,-1,-4,-5,-8,-9],[-8,4,8,-4,8,8,10,4,3,7],[6,10,2,-2,2,1,-8,9,-5,-2],[-4,-3,-2,-8,7,-6,3,5,-1,-6],[-8,-2,4,-4,-4,-1,9,-5,-9,5],[-8,8,-8,7,-2,2,-1,-8,-6,3],[-1,10,-6,-10,-8,10,-7,-7,5,-4],[-10,7,-3,-8,1,8,-6,3,-5,-9]],[[-9,9,9,-1,-4,1,5,5,5,4],[-5,-10,-5,2,-6,-3,2,-3,9,-5],[-2,7,6,-3,5,9,-4,-2,-3,-8],[-7,-6,-4,10,-2,6,-3,1,-5,2],[-4,2,1,-6,8,5,-3,-2,9,-10],[-9,5,9,3,10,6,8,1,-9,6],[-9,3,-2,-10,-9,2,-9,1,-4,-4],[10,8,7,9,-4,-3,6,6,-3,8],[9,9,10,-7,-4,9,-10,-4,-6,-3],[10,7,4,-3,-2,-8,-3,-10,-6,-7],[6,4,3,-3,3,-3,-3,-8,-4,3]],[[-1,8,9,7,2,6,8,-6,-2,-1],[-4,-7,-5,-4,-3,4,10,-8,-7,-4],[6,9,-2,6,3,-8,-4,-5,-7,5],[-10,5,-10,-8,-7,7,4,1,2,-1],[-7,-3,-3,9,1,-3,-4,10,-1,-2],[-5,-6,-7,-7,6,-4,-9,3,7,-4],[-5,-9,3,-4,2,-7,-7,5,9,4],[10,-8,7,10,5,-4,1,9,5,-10],[-9,3,9,-9,10,6,1,8,9,-4],[4,-5,1,6,-7,-4,-5,-2,5,-5],[-5,6,8,6,3,-2,-7,-9,8,8]],[[-6,-2,1,5,5,2,4,-10,3,-10],[7,3,-8,4,-10,3,-5,6,9,2],[1,4,2,-8,9,1,-1,-1,7,-6],[8,-4,4,-10,9,-5,-6,8,4,-4],[7,8,-10,-8,4,5,-3,6,-8,8],[-8,10,5,-3,5,1,-3,-9,-8,9],[10,6,4,1,-10,-9,-4,-2,8,-8],[-3,4,-8,8,-1,9,-10,3,1,-5],[-2,9,3,7,-9,4,-3,-9,-3,-6],[1,-4,-2,-6,-2,2,-7,-2,-4,-2],[5,6,-4,7,-1,2,8,-4,4,3]],[[-5,1,-10,2,3,9,-10,6,-10,-3],[-5,3,-4,6,-1,5,-6,7,1,-9],[1,-2,3,-7,10,5,9,-1,-7,1],[7,-3,2,10,7,-8,9,1,8,6],[2,-5,9,3,4,3,10,6,-6,-5],[-8,-3,-5,-9,-6,2,4,10,3,9],[-7,-9,-10,1,1,-1,1,4,-2,-10],[7,8,-9,-7,2,-10,-10,-8,-3,-8],[-6,-3,-7,-4,1,-9,8,-2,-8,9],[-6,-10,7,-9,-8,-7,10,-3,1,7],[-3,-2,8,6,-4,-7,-6,-9,7,-5]],[[6,9,-2,-4,2,-4,-8,6,2,-1],[8,7,6,-5,3,-8,-2,7,-1,-6],[10,6,8,-5,3,-7,5,3,1,4],[9,-4,-9,6,2,1,-2,4,-10,-10],[-9,3,2,-5,7,-6,-9,9,3,-8],[-7,-1,-7,-1,-5,9,10,8,-2,-7],[-2,5,-5,-1,-10,-7,9,6,-2,2],[-9,-9,-5,-3,10,3,-4,3,-7,-10],[-5,-3,-5,-8,-9,-4,1,9,2,2],[3,4,-6,-7,-3,-9,3,1,-5,5],[-1,-2,2,-10,-3,-6,10,4,-9,8]],[[-7,10,-10,-10,-4,-9,-3,9,10,10],[4,10,8,-9,-4,-10,-3,-2,3,-10],[-4,2,-7,3,-2,1,-2,7,6,8],[-2,-10,7,10,4,5,-8,-7,7,2],[-4,-5,-3,-6,-10,-8,1,9,-2,9],[10,3,-2,1,-10,-9,6,-3,-6,-10],[5,9,8,5,-7,-5,10,-5,8,-2],[-8,7,4,-5,-10,9,2,1,-5,9],[3,-1,2,5,-1,-10,-9,5,6,-6],[-6,10,-10,-10,-7,9,5,-3,5,6],[-5,6,-5,7,-2,6,7,-6,8,4]],[[-6,-7,10,-7,8,-10,2,-6,9,-8],[6,1,-1,2,4,7,8,1,4,2],[1,-6,2,-2,5,3,4,-7,-4,6],[-5,-10,-9,-1,-8,6,9,-2,3,-1],[4,2,-2,4,-9,4,5,9,4,8],[4,-9,7,-3,7,-9,-10,8,-1,5],[-3,6,-4,4,4,8,-6,-3,2,3],[10,2,-4,-1,5,5,-7,-7,-5,-7],[-3,-6,-3,3,-5,-7,-8,-4,-1,7],[10,-3,-2,-6,-3,5,9,4,2,-9],[6,1,-5,8,1,2,-9,10,7,-10]],[[10,-6,-9,-1,10,8,-6,-9,6,-6],[5,10,-5,7,8,-2,-3,7,1,-10],[10,6,-7,-6,4,-1,2,-3,2,8],[-5,8,9,9,5,-10,5,2,10,-4],[4,5,7,-2,8,-10,-10,-3,4,-8],[1,-8,3,10,-10,10,-10,-9,-5,-7],[-10,-7,5,-7,4,-2,5,-1,1,-2],[8,6,-8,-6,-5,3,-1,-6,-2,7],[-10,1,10,4,3,-2,-7,-8,3,-6],[-8,6,3,8,-6,-1,8,2,4,-7],[1,8,8,-2,4,3,-1,3,-2,-9]]], dtype = "uint16")#candidate|2974|(11, 11, 10)|const|uint16
bop_2975 = relay.bitwise_xor(var_2973.astype('uint16'), relay.reshape(const_2974.astype('uint16'), relay.shape_of(var_2973))) # shape=(11, 11, 10)
output = bop_2975
output2 = bop_2975
func_2985 = relay.Function([var_2973,], output)
mod['func_2985'] = func_2985
mod = relay.transform.InferType()(mod)
var_2986 = relay.var("var_2986", dtype = "uint16", shape = (11, 11, 10))#candidate|2986|(11, 11, 10)|var|uint16
output = func_2985(var_2986)
func_2987 = relay.Function([var_2986], output)
mutated_mod['func_2987'] = func_2987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2786_call = mod.get_global_var('func_2786')
func_2787_call = mutated_mod.get_global_var('func_2787')
call_3046 = func_2786_call()
call_3047 = func_2786_call()
output = relay.Tuple([call_3046,])
output2 = relay.Tuple([call_3047,])
func_3052 = relay.Function([], output)
mod['func_3052'] = func_3052
mod = relay.transform.InferType()(mod)
mutated_mod['func_3052'] = func_3052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3052_call = mutated_mod.get_global_var('func_3052')
call_3053 = func_3052_call()
output = call_3053
func_3054 = relay.Function([], output)
mutated_mod['func_3054'] = func_3054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2824_call = mod.get_global_var('func_2824')
func_2826_call = mutated_mod.get_global_var('func_2826')
call_3066 = relay.TupleGetItem(func_2824_call(), 3)
call_3067 = relay.TupleGetItem(func_2826_call(), 3)
func_2708_call = mod.get_global_var('func_2708')
func_2712_call = mutated_mod.get_global_var('func_2712')
const_3075 = relay.const([-7.348137,1.142075,-6.502354,-0.336968,-4.307279,-2.505200,-0.589243,-6.723899,-3.883103,-1.644901,3.795049,-1.235910,-2.291755,5.544441,9.829163,6.452088,-7.303873,5.417933,4.846287,-3.936790,0.682491,-6.180093,-5.879783,2.228733,0.316253,0.036490,1.126099,1.140934,-9.759105,6.275977,-6.298255,0.081536,8.950348,6.165086,-9.475372,-7.115085,-8.532474,-8.522879,-5.918601,-7.674329,0.927446,-6.999433,7.867859,-2.653312,2.945533,4.331118,-0.809044,-9.492360,4.546570,2.570541,-8.286641,-0.732649,-6.858529,3.293955,-0.970548,4.547469,-7.644032,-8.776451,4.777186,0.152211,1.107240,-4.928883,3.180916,4.934950,-3.397506,8.642672,9.131818,0.319552,-1.971030,-2.096661,-9.775424,-8.912952,4.047958,-3.066140,5.303559,1.020158,-5.216755,8.436081,8.452610,5.647517,0.300147,-7.487998,-6.687295,-8.098559,-3.885731,8.647295,-1.049039,0.585336,5.690666,-8.236574,5.407555,1.609829,6.872484,-9.004656,3.264492,-5.773085,-6.050747,1.928958,3.761652,2.462974,-4.778264,-7.696058,-8.448771,4.434151,-2.329123,-6.880208,3.828672,7.654991,-7.321255,3.908541,4.223824,-2.470193,-5.326876,-0.968268,-4.627012,-4.374874,2.591303,9.177107,-6.616213,9.516539,1.907295,4.959762,6.889758,5.686116,-6.158813,4.638078,0.484620,7.295613,-1.420980,6.073835,3.171370,1.829515,-6.305959,-3.388369,4.770316,8.983375,8.156970,-9.334072,-9.817008,3.439217,-4.738913,-1.956014,-2.657407,-3.011288,-8.840790,2.054435,6.377253,-5.816210,-2.083706,-8.074994,-8.802971,-0.881236,-2.742639,-0.047624,-6.534348,8.847467,-5.153877,-6.313884,4.272170,6.613136,-8.034903,9.667970,-5.668785,-9.525320,-1.947456,-9.141308,-9.091458,8.488358,5.254982,3.104750,0.333308,4.505403,1.134316,-4.631334,-8.880833,-3.447635,4.472003,-7.030688,6.762258,-1.348127,1.221847,-3.961994,0.156810,3.289229,7.149799,-1.764501,6.602161,-7.999148,-1.667977,-0.299352,5.613676,3.749070,-8.555473,-7.013570,-6.413846,-1.817498,2.995231,-6.214517,-2.161446,-8.046617,-7.083306,-4.997026,-7.299233,-7.520194,6.245415,8.907607,7.261521,5.482283,-0.362731,7.747079,-9.356289,-0.873686,-1.406954,-8.621955,-7.631224,-1.206050,-0.321875,5.014840,-9.005402,9.344716,-1.948672,-7.013599,3.357540,0.732822,1.669651,2.518555,-7.837413,8.406055,-7.901200,8.308333,-3.641835,1.478504,-3.483338,8.376862,1.714921,8.378335,4.077298,3.522681,7.127553,-8.866303,-1.194272,3.484665,-9.570903,5.958552,-9.332777,2.029162,3.561206,6.198067,0.271737,-7.167352,3.274909,-7.617750,8.092213,-8.558282,6.934841,5.885875,-2.512018,-8.293989,1.566649,8.697810,3.165316,3.683647,3.299307,-5.877094,5.031843,6.754894,-7.702899,-0.367820,-6.112971,9.578253,8.853935,0.197505,2.243990,-8.531873,7.418235,-9.424438,5.749748,1.217268,6.277831,3.561954,-8.780758,6.454270,4.998612,-8.057055,-1.393151,4.252724,-6.081293,5.640272,-3.772735,0.288491,1.964385,-8.189199,2.985079,-3.527757,-3.381236,5.421720,-6.628942,7.179716,-7.509559,2.793655,8.214956,2.538406,7.170188,1.838346,-6.076762,-0.595172,6.748174,-5.541711,-8.661243,4.557000,6.841921,-0.463823,9.259231,8.982806,5.989640,5.982204,3.947063,9.216810,0.619823,-4.732028,7.266963,-5.871931,-5.334645,7.183946,3.964525,0.840031,3.020869,-6.580937,7.690459,6.901391,9.658013,-7.366397,9.323143,7.715862,-7.526924,-7.253349,-4.933363,-8.799688,-3.516805,-6.925618,-5.244533,-6.253371,6.788720,8.655906,-1.672683,5.438995,5.619977,-0.192500,8.167565,7.110822,7.729626,6.502765,-9.268447,-1.094977,2.150567,-0.419036,-6.122280,-4.394204,-7.943188,5.106831,-0.371763,-9.456254,-9.192891,-0.807083,-6.164831,6.196728,9.976104,-6.226295,0.550770,-1.606603,3.245844,-6.981861,6.657131,1.442274,-2.471226,-9.411507,3.131736,-3.004105,0.767563,-6.910061,4.829844,-7.058675,-8.120825,-9.621549,0.600125,7.285162,-4.243949,0.582861,-1.259305,0.582747,7.498712,3.519340,-0.979322,-4.454574,-0.166740,5.872327,-0.910971,-6.663864,-3.866795,-2.651945,-8.458213,-0.247581,-6.431476,-0.238792,-4.904489,5.555206,-6.335357,0.472553,1.261706,-7.661156,-2.529924,4.170112,5.113431,0.417316,-3.912949,-2.873800,4.428344,3.914576,-0.350907,-0.438137,4.010938,-4.148541,-1.489172,-5.493370,7.686146,6.634900,5.624952,-5.257076,7.411728,-1.503137,-2.771944,-1.122784,-1.131324,0.201290,7.149740,8.792307,5.280972,-4.121067,4.368947,1.176774,-0.248612,-3.784351,0.704600,-9.513600,2.456351,9.989730,4.971288,4.240708,4.593437,-1.397534,3.599132,-5.546265,1.684090,-1.970538,0.294947,8.410223,5.947952,2.479192,5.518806,4.762816,9.970707,-7.353815,-0.721653,-2.005884,-6.027702,-1.574480,-9.535475,-3.077474,-3.216012,5.867477,2.778057,1.039029,-0.895045,4.185216,-1.502177,-7.073863,8.167626,0.324164,9.239325,-6.636212,-5.475477,8.131756,2.620311,4.390867,-2.252517,5.151493,9.575537,-7.501062,-0.433149,2.737570,-6.615502,-3.537907,-8.964330,7.334918,2.986787,5.571797,4.440830,-5.956591,7.320023,-6.798892,-4.159056,1.356350,-2.312670,-5.970148,9.513072,1.398128,9.570027,-7.177798,8.888612,0.403679,0.375211,5.943339,0.402954,5.137573,8.423349,8.434336,6.895910,2.288459,-2.202612,-2.388836,-5.932906,-7.895827,4.934458,0.999787,-9.506761,9.570096,-7.146099,-4.091519,3.289875,-8.072836,9.786364,-9.631521,-2.572267,-6.522635,6.661009,-8.222642,0.080086,-4.239692,1.252603,0.819209,-9.348959,2.353304,3.791319,8.722422,3.147359,3.146120,4.701532,-3.483302,-3.352075,-4.270392,9.252259,8.047730,9.563431,-3.186994,7.068177,3.899600,-3.884673,-6.660390,-1.478612,-5.382339,0.931098,4.546746,-5.877406,-4.262012,-5.319886,-4.829668,-2.333697,-8.234748,5.623941,-4.858271,5.283844,2.856888,6.792568,6.540933,7.444218,4.717591,-9.232339,3.674288,-9.664470,7.288229,-0.017365,1.725209,9.727359,6.908868,-8.797209,4.558715,4.689533,8.588672,0.322286,-2.409724,5.202937,1.845865,-2.018487,-5.502687,4.692965,-5.926748,1.773112,-6.864494,6.814085,-6.196036,8.738109,2.904249,-5.838998,4.337287,-3.516401,-4.052459,-2.103260,5.526596,-9.227188,2.808491,8.629792,5.633726,0.815284,0.099701,8.153412,-5.587176,9.905035,4.561413,7.288751,0.517481,8.338418,8.731309,-4.347936,-8.093636,-9.316545,-4.551522,1.464001,-4.618159,9.320968,-0.437557,5.963262,7.719712,-6.748366,-9.710759,-3.933337,9.217531,3.926595,5.357307,0.333334,-1.938352,4.965276,4.062816,7.772362,-6.581834,3.585457,1.385980,8.169693,-3.663268,-0.559045,7.241195,-7.036815,-8.469780,6.014441,7.213421,2.686564,-1.118481,-8.485639,-5.560354,-9.437548,-1.291437,7.355054,-2.716026,8.326512,-1.563200,-1.978554,-6.420256,1.782550,-4.627562,-7.751138,8.251888,-5.608232,-9.913036,-0.387481,-3.838007,4.221521,-1.713120,-9.014735,-5.347053,1.047869,8.601479,-5.188751,8.109681,-7.468129,7.134607,1.663145,6.341026,-3.915276,3.819873,-4.867168,4.411066,-0.255871,-1.927702,5.209337,-5.384937,3.241743,-9.285660,4.446569,3.416502,9.322606,-3.143522,-3.620811,-7.712994,-9.931343,6.213354,0.549833,-2.962233,-4.849335,3.706580,1.137484,9.672627,8.182665,2.429909,7.964394,8.175686,5.440742,2.251372,6.556918,-2.096720,0.370364,-3.431471,2.561810,5.545606,9.733740,6.052917,-1.507574,2.185930,-4.794491,1.202422,-1.660469,-5.688416,-0.211317,5.636632,-4.045673,4.307827,6.981404,-4.749698,8.238713,-7.063691,-0.598339,4.610681,-1.678962,5.207607,9.078250,-7.711646,0.256716,2.075554,5.184292,7.354603,8.135676,7.037743,-8.437740,6.784107,7.699953,-5.894197,4.640145,5.391699,-3.226520,-5.499403,0.401319,4.085958,7.629246,-3.371639,5.887364,-1.865734,4.873984,9.512020,-3.360412,3.606245,6.368496,3.217187,8.544964,-9.641207,2.092588,-6.927864,-3.600942,6.027289,-4.463298,-4.237547,7.467528,-3.632380,-3.082374,-6.518236,-5.835096,9.928154,0.018097,-3.250130,2.776047,8.444544,1.165810,2.171600,3.270025,-1.822238,-4.189985,-2.065496,6.026870,-2.945517,-0.902559,-3.528526,-0.440651,-9.647850,1.143863,5.764830,-9.964443,6.423476,-1.920591,9.133762,-1.548471,0.336212,-9.617173,-1.106650,5.588098,5.512924,-2.957721,-1.464541,8.581861,-6.910856,-0.429468,9.027924,-2.833947,-1.574486,6.437190,2.747418,3.722599,1.228904,-9.269738,-7.195269,-7.083974,9.915024,1.430477,-6.018490,8.167468,5.071861], dtype = "float32")#candidate|3075|(832,)|const|float32
call_3074 = relay.TupleGetItem(func_2708_call(relay.reshape(const_3075.astype('float32'), [13, 4, 16]), relay.reshape(const_3075.astype('float32'), [13, 4, 16]), ), 2)
call_3076 = relay.TupleGetItem(func_2712_call(relay.reshape(const_3075.astype('float32'), [13, 4, 16]), relay.reshape(const_3075.astype('float32'), [13, 4, 16]), ), 2)
output = relay.Tuple([call_3066,call_3074,const_3075,])
output2 = relay.Tuple([call_3067,call_3076,const_3075,])
func_3080 = relay.Function([], output)
mod['func_3080'] = func_3080
mod = relay.transform.InferType()(mod)
mutated_mod['func_3080'] = func_3080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3080_call = mutated_mod.get_global_var('func_3080')
call_3081 = func_3080_call()
output = call_3081
func_3082 = relay.Function([], output)
mutated_mod['func_3082'] = func_3082
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3133 = relay.var("var_3133", dtype = "uint64", shape = ())#candidate|3133|()|var|uint64
var_3134 = relay.var("var_3134", dtype = "uint64", shape = (16, 12, 1))#candidate|3134|(16, 12, 1)|var|uint64
bop_3135 = relay.bitwise_or(var_3133.astype('uint64'), var_3134.astype('uint64')) # shape=(16, 12, 1)
bop_3143 = relay.minimum(bop_3135.astype('float32'), var_3133.astype('float32')) # shape=(16, 12, 1)
output = relay.Tuple([bop_3143,])
output2 = relay.Tuple([bop_3143,])
func_3162 = relay.Function([var_3133,var_3134,], output)
mod['func_3162'] = func_3162
mod = relay.transform.InferType()(mod)
var_3163 = relay.var("var_3163", dtype = "uint64", shape = ())#candidate|3163|()|var|uint64
var_3164 = relay.var("var_3164", dtype = "uint64", shape = (16, 12, 1))#candidate|3164|(16, 12, 1)|var|uint64
output = func_3162(var_3163,var_3164,)
func_3165 = relay.Function([var_3163,var_3164,], output)
mutated_mod['func_3165'] = func_3165
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3184 = relay.var("var_3184", dtype = "float32", shape = (10, 13, 4))#candidate|3184|(10, 13, 4)|var|float32
uop_3185 = relay.atanh(var_3184.astype('float32')) # shape=(10, 13, 4)
uop_3187 = relay.log2(uop_3185.astype('float32')) # shape=(10, 13, 4)
output = relay.Tuple([uop_3187,])
output2 = relay.Tuple([uop_3187,])
func_3208 = relay.Function([var_3184,], output)
mod['func_3208'] = func_3208
mod = relay.transform.InferType()(mod)
mutated_mod['func_3208'] = func_3208
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3209 = relay.var("var_3209", dtype = "float32", shape = (10, 13, 4))#candidate|3209|(10, 13, 4)|var|float32
func_3208_call = mutated_mod.get_global_var('func_3208')
call_3210 = func_3208_call(var_3209)
output = call_3210
func_3211 = relay.Function([var_3209], output)
mutated_mod['func_3211'] = func_3211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2775_call = mod.get_global_var('func_2775')
func_2776_call = mutated_mod.get_global_var('func_2776')
call_3231 = relay.TupleGetItem(func_2775_call(), 0)
call_3232 = relay.TupleGetItem(func_2776_call(), 0)
func_2985_call = mod.get_global_var('func_2985')
func_2987_call = mutated_mod.get_global_var('func_2987')
var_3239 = relay.var("var_3239", dtype = "uint16", shape = (1210,))#candidate|3239|(1210,)|var|uint16
call_3238 = func_2985_call(relay.reshape(var_3239.astype('uint16'), [11, 11, 10]))
call_3240 = func_2985_call(relay.reshape(var_3239.astype('uint16'), [11, 11, 10]))
func_1785_call = mod.get_global_var('func_1785')
func_1787_call = mutated_mod.get_global_var('func_1787')
const_3251 = relay.const([[10,7,3,10,9,2,-2,-4,-5,-10,2,10]], dtype = "uint64")#candidate|3251|(1, 12)|const|uint64
call_3250 = relay.TupleGetItem(func_1785_call(relay.reshape(const_3251.astype('uint64'), [12,])), 0)
call_3252 = relay.TupleGetItem(func_1787_call(relay.reshape(const_3251.astype('uint64'), [12,])), 0)
func_3162_call = mod.get_global_var('func_3162')
func_3165_call = mutated_mod.get_global_var('func_3165')
const_3266 = relay.const(-8, dtype = "uint64")#candidate|3266|()|const|uint64
var_3267 = relay.var("var_3267", dtype = "uint64", shape = (192,))#candidate|3267|(192,)|var|uint64
call_3265 = relay.TupleGetItem(func_3162_call(relay.reshape(const_3266.astype('uint64'), []), relay.reshape(var_3267.astype('uint64'), [16, 12, 1]), ), 0)
call_3268 = relay.TupleGetItem(func_3165_call(relay.reshape(const_3266.astype('uint64'), []), relay.reshape(var_3267.astype('uint64'), [16, 12, 1]), ), 0)
output = relay.Tuple([call_3231,call_3238,var_3239,call_3250,const_3251,call_3265,const_3266,var_3267,])
output2 = relay.Tuple([call_3232,call_3240,var_3239,call_3252,const_3251,call_3268,const_3266,var_3267,])
func_3275 = relay.Function([var_3239,var_3267,], output)
mod['func_3275'] = func_3275
mod = relay.transform.InferType()(mod)
mutated_mod['func_3275'] = func_3275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3275_call = mutated_mod.get_global_var('func_3275')
var_3277 = relay.var("var_3277", dtype = "uint16", shape = (1210,))#candidate|3277|(1210,)|var|uint16
var_3278 = relay.var("var_3278", dtype = "uint64", shape = (192,))#candidate|3278|(192,)|var|uint64
call_3276 = func_3275_call(var_3277,var_3278,)
output = call_3276
func_3279 = relay.Function([var_3277,var_3278,], output)
mutated_mod['func_3279'] = func_3279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1602_call = mod.get_global_var('func_1602')
func_1604_call = mutated_mod.get_global_var('func_1604')
call_3386 = func_1602_call()
call_3387 = func_1602_call()
func_2824_call = mod.get_global_var('func_2824')
func_2826_call = mutated_mod.get_global_var('func_2826')
call_3405 = relay.TupleGetItem(func_2824_call(), 0)
call_3406 = relay.TupleGetItem(func_2826_call(), 0)
output = relay.Tuple([call_3386,call_3405,])
output2 = relay.Tuple([call_3387,call_3406,])
func_3410 = relay.Function([], output)
mod['func_3410'] = func_3410
mod = relay.transform.InferType()(mod)
output = func_3410()
func_3411 = relay.Function([], output)
mutated_mod['func_3411'] = func_3411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1905_call = mod.get_global_var('func_1905')
func_1906_call = mutated_mod.get_global_var('func_1906')
call_3450 = relay.TupleGetItem(func_1905_call(), 1)
call_3451 = relay.TupleGetItem(func_1906_call(), 1)
func_2775_call = mod.get_global_var('func_2775')
func_2776_call = mutated_mod.get_global_var('func_2776')
call_3455 = relay.TupleGetItem(func_2775_call(), 0)
call_3456 = relay.TupleGetItem(func_2776_call(), 0)
var_3459 = relay.var("var_3459", dtype = "float32", shape = (4, 8, 13))#candidate|3459|(4, 8, 13)|var|float32
bop_3460 = relay.equal(call_3450.astype('bool'), relay.reshape(var_3459.astype('bool'), relay.shape_of(call_3450))) # shape=(4, 8, 13)
bop_3463 = relay.equal(call_3451.astype('bool'), relay.reshape(var_3459.astype('bool'), relay.shape_of(call_3451))) # shape=(4, 8, 13)
output = relay.Tuple([call_3455,bop_3460,])
output2 = relay.Tuple([call_3456,bop_3463,])
func_3466 = relay.Function([var_3459,], output)
mod['func_3466'] = func_3466
mod = relay.transform.InferType()(mod)
var_3467 = relay.var("var_3467", dtype = "float32", shape = (4, 8, 13))#candidate|3467|(4, 8, 13)|var|float32
output = func_3466(var_3467)
func_3468 = relay.Function([var_3467], output)
mutated_mod['func_3468'] = func_3468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1968_call = mod.get_global_var('func_1968')
func_1970_call = mutated_mod.get_global_var('func_1970')
call_3505 = relay.TupleGetItem(func_1968_call(), 0)
call_3506 = relay.TupleGetItem(func_1970_call(), 0)
func_2708_call = mod.get_global_var('func_2708')
func_2712_call = mutated_mod.get_global_var('func_2712')
const_3517 = relay.const([-2.538688,1.437545,6.824388,4.869959,-7.873779,-1.335215,-4.844850,5.189383,3.789094,3.428153,-1.280937,3.000359,-8.597935,0.660121,9.341065,-0.244495,-8.916016,0.250589,8.925161,2.698026,-7.576714,1.109543,4.739420,-6.637963,9.056623,5.761257,9.954951,-1.344588,-1.503950,8.168025,8.869932,-0.146037,-6.370246,6.990747,-7.987571,7.188341,-0.893322,-6.401470,8.691310,-1.511951,-2.863073,-5.679537,-8.497004,9.760973,-1.521223,0.495838,0.210763,-6.967274,0.037955,0.278514,-4.386141,8.469730,7.188495,3.121965,-4.544014,-1.736608,3.610761,4.748748,5.340677,-3.639716,2.474830,7.689588,9.450259,-5.261589,7.514236,3.340585,-4.092408,-0.398982,-7.887164,-4.408534,-0.162394,4.231671,-7.778175,3.181248,-5.439036,7.445164,3.947410,-3.983977,-7.107746,-3.727206,-6.305563,-0.755148,-2.411469,4.164759,-0.333395,6.839060,-1.329802,-6.609573,7.150638,-6.920635,9.803514,-0.167096,7.007792,-6.769638,1.672626,5.456548,-7.363815,2.740237,8.680980,0.534303,-6.356417,-5.229084,6.816287,8.901455,-0.049808,-3.470625,-1.516785,7.541119,5.374054,9.417245,-8.392061,9.668280,-9.647253,9.689989,7.783432,4.409557,8.162230,-0.313094,-2.082569,-4.894472,5.360829,8.469511,5.278485,5.101363,-3.932368,9.166670,-6.641552,1.461638,0.296857,-0.285231,4.521697,0.228975,2.175482,4.056051,6.358344,-3.544691,6.785308,-6.196048,-5.747016,3.798019,1.672991,3.997853,3.916949,-6.270848,5.980693,5.809613,5.309630,-1.829287,-3.143471,-7.088742,1.023191,7.573853,-4.216811,9.711844,2.142565,0.304738,3.842210,-9.155685,8.788860,-5.195126,5.991382,7.766099,-2.949330,2.954989,-9.422705,-3.819836,2.732446,-8.624623,-5.665302,-7.163661,-0.910309,-5.192012,1.425105,9.812241,7.570242,1.874907,1.991222,9.251824,-4.809014,2.366486,1.012158,-8.013914,5.545685,-1.795003,-3.494293,0.271247,6.776274,2.148298,1.399148,1.331259,-0.361661,3.136189,-3.724038,4.332444,-7.094873,3.847486,-2.886985,-5.342862,-8.364831,6.092457,8.717240,7.231484,-0.736817,7.680178,2.550947,9.346074,-0.505707,-9.233733,9.556573,0.858139,-4.384105,2.267612,5.085458,-4.384668,6.647020,-7.118858,-0.625325,0.661415,-7.733077,-1.127521,0.548314,9.073880,3.898895,-6.909891,3.742218,-7.412052,-7.351805,5.652944,2.221304,2.717654,8.248322,0.348720,-3.502304,9.853769,-0.126108,-4.310397,7.654320,8.608624,7.716457,1.466137,1.967821,-4.234216,-8.565774,5.830361,1.826973,-8.698178,4.515551,3.996780,-5.906852,-9.760058,-3.145297,-2.696805,7.996560,-7.924265,-2.118212,1.418082,5.690227,3.621682,9.781082,5.765150,-9.342182,-7.064540,-3.211744,6.084367,-7.275344,7.892543,-4.954307,-6.786715,6.792871,1.608550,-0.513690,2.125943,-3.498794,2.227641,-3.505009,3.838737,-2.353609,-6.617669,9.817973,3.302396,9.028727,-0.720341,2.146321,8.210535,-0.728173,-6.599537,-6.272789,-7.285879,-1.262517,-2.957835,3.334932,5.627526,0.984949,-6.080165,9.861991,-1.454311,-3.896342,5.041792,7.651930,-0.599339,0.849018,3.350710,-8.513851,-6.469794,2.155063,8.546036,-0.647627,6.327014,-4.633194,-3.148010,6.316743,3.382828,-2.201756,4.966391,3.334086,0.671087,-8.629526,-0.410570,-7.790933,-2.699260,-5.358132,-1.271259,-9.777367,-4.632567,9.146419,0.073394,-5.324184,-1.567666,3.798113,-4.167138,0.143948,3.147669,-0.216781,9.867478,-5.488802,0.441729,2.678297,-2.273879,4.963561,9.023933,5.890025,9.603294,1.422140,-3.099632,-3.286070,2.964545,-2.056864,3.328230,3.027421,-7.106352,-1.195861,-1.555977,7.965542,-2.172423,0.225109,-1.010783,-6.336013,-7.757517,0.702109,-3.552949,-1.676272,-7.970108,-9.892296,5.264089,-4.799382,9.734037,8.070731,-4.048334,-7.403038,6.920187,-4.130616,3.707258,-7.946413,-6.335974,-1.168133,2.739171,5.274406,-5.795522,1.288913,8.754760,4.024431,4.103881,-3.117406,4.067787,-7.926481,-7.752036,-9.343904,7.234751,-4.824331,7.409818,-1.049253,3.340564,-7.681095,7.406250,8.916774,4.534142,0.719598,-6.719183,-5.108070,8.536628,-1.902743,-2.458436,6.044575,4.189796,0.095103,-9.115962,6.049145,5.600819,8.617384,-2.046687,5.847049,5.989189,-0.612051,-4.588251,-2.339914,3.130438,-7.759906,7.453957,8.676910,1.021708,7.524915,-5.470787,4.117624,-5.501412,-0.838044,2.852417,-4.997354,-7.601053,-3.728941,-3.100240,-8.479577,-0.178906,4.096351,-1.822300,-7.749814,1.224290,-2.506602,3.592520,-4.964320,-5.602488,-6.806480,-5.343127,9.024374,8.550111,-3.185529,-5.221560,7.565869,9.549156,-1.908429,8.107380,5.685308,1.331775,-3.913899,5.507382,-1.143430,2.155974,6.363215,-7.292889,-0.916302,3.764905,9.670846,-1.887416,-3.338422,0.021819,2.234976,5.176655,0.472028,-8.236169,2.242200,-5.538147,-1.827986,-0.960782,-9.639074,-1.131374,-4.207871,4.834992,4.574461,-3.117149,0.324185,-5.313021,-9.850410,6.050654,-6.479336,1.873471,6.506141,-3.581062,6.012279,2.557692,2.171543,8.578412,5.257207,8.567179,-1.736771,-6.336296,3.549775,-9.390405,4.357398,4.639557,-5.165965,5.225430,5.463708,2.969732,0.244374,-3.676818,-4.631066,-5.406301,-5.001286,-2.896799,-6.183139,-3.880762,2.731693,6.346938,-9.628903,8.312385,-7.744935,-6.221892,-0.060558,-7.681704,-4.065081,-3.293171,-5.222915,1.424105,-9.015609,5.162875,-6.225074,-4.918408,8.136351,-1.905667,-7.913587,-6.285217,2.740585,-1.861060,-1.967881,0.845171,6.919641,9.361377,-7.284385,-6.863697,-1.272579,6.186488,6.392392,-6.758614,-7.005260,-2.408086,-4.333215,4.082619,4.174580,2.545091,-0.481146,2.986888,-7.925150,-2.010944,4.725805,7.851639,-8.160593,-0.413810,-0.216370,-5.963425,-8.067005,-2.769807,3.692587,-6.764414,7.189373,-7.727084,-2.604517,-8.941244,-8.780774,2.329194,4.745023,0.713233,-6.047413,-3.578263,6.980041,4.393809,8.102499,-0.746669,6.138925,-6.331331,2.772976,-9.179849,-7.429687,-1.227245,2.549893,-9.317069,2.138965,7.828865,3.578617,-3.571105,-0.801001,-7.321925,2.354496,8.181580,8.402305,-7.121322,-8.004666,-9.386459,4.516731,-8.810227,5.906298,5.239749,-7.435548,-4.903728,-1.320975,-9.920974,-2.193199,4.463264,-8.740211,-8.013942,-7.337527,-1.177502,8.239545,4.722527,1.726339,-8.337584,-2.721585,0.526186,-7.303573,-2.617921,5.424632,0.271738,-7.861032,4.361394,8.188268,-3.707365,-2.765572,3.510957,-2.046051,-2.844134,-0.323313,-8.805410,7.653308,1.774130,7.626261,-9.254551,2.576018,-7.662430,-7.834010,-0.226400,3.757455,3.109883,8.079760,3.846212,6.567927,6.871584,-2.370880,-4.107024,-5.207644,8.908397,-9.370702,-6.763876,-2.489035,6.685677,-9.907776,-3.324358,-2.792340,-9.852894,-4.268501,9.326647,8.974019,2.158889,-1.763139,9.508433,-2.970241,-5.580945,5.639734,-2.655455,9.223243,-2.571490,9.747126,5.631582,4.396368,5.451339,-8.815372,5.616476,7.169568,1.456325,3.056476,-9.419635,-6.582784,-7.074740,6.885971,0.027852,-3.334559,7.023193,-2.187673,7.470790,-9.701943,-1.573765,-5.323585,-5.523747,-6.708691,9.887220,5.923085,4.128548,6.988448,8.163341,-0.122574,0.577398,-9.892036,-3.287697,-1.858232,-0.982558,-6.113069,7.851124,9.721245,7.513900,7.034489,2.440666,-0.110049,-9.000030,-9.105499,9.008383,-0.901523,2.206386,7.359396,-6.245280,8.404228,-7.121864,7.488926,-1.265362,4.850999,-9.124903,9.215387,5.948876,4.295649,5.205304,6.901408,-1.123304,8.731264,0.070412,-5.359796,-1.917697,-4.828004,8.470902,-2.353171,-6.552206,5.677441,7.896750,-9.992101,3.517492,-0.226753,3.816082,4.142092,-3.908752,4.567866,9.527034,9.072576,-9.677725,-8.183169,9.981044,6.227971,-0.515653,-5.406253,1.486701,2.225496,-5.148624,3.411152,4.608083,-8.276180,-0.531791,6.920993,2.250211,3.432575,7.329167,8.759094,4.146630,-6.774745,-0.954776,7.544169,-9.558134,-3.807966,-1.256368,-9.424813,-1.642609,7.065674,2.590953,-0.607587,5.830228,-5.929556,8.102348,1.885257,-8.824927,-1.986017,9.966335,4.217040,-5.715489,-9.946429,5.338676,9.588997,0.960909,-9.887918,8.790058,6.007513,2.304740,1.606454,-7.996546,1.896012,1.718540,3.790559,6.582199,-9.212882,-1.232338,-6.667347,2.208469,2.185690,0.049484,8.165999,-1.033722,3.190719,-1.666332,-4.446385,-8.777838,-7.533191,1.071066,-8.834165,-7.528179,5.172090,5.487852,-6.701535,2.022127,-2.540484,-1.679545,7.559372,-4.636717,-7.504199,-1.563699,8.459752,-2.833288,-3.167762,5.465574,-8.719605,9.236002], dtype = "float32")#candidate|3517|(832,)|const|float32
call_3516 = relay.TupleGetItem(func_2708_call(relay.reshape(const_3517.astype('float32'), [13, 4, 16]), relay.reshape(const_3517.astype('float32'), [13, 4, 16]), ), 10)
call_3518 = relay.TupleGetItem(func_2712_call(relay.reshape(const_3517.astype('float32'), [13, 4, 16]), relay.reshape(const_3517.astype('float32'), [13, 4, 16]), ), 10)
func_2775_call = mod.get_global_var('func_2775')
func_2776_call = mutated_mod.get_global_var('func_2776')
call_3522 = relay.TupleGetItem(func_2775_call(), 0)
call_3523 = relay.TupleGetItem(func_2776_call(), 0)
func_3052_call = mod.get_global_var('func_3052')
func_3054_call = mutated_mod.get_global_var('func_3054')
call_3524 = relay.TupleGetItem(func_3052_call(), 0)
call_3525 = relay.TupleGetItem(func_3054_call(), 0)
func_3275_call = mod.get_global_var('func_3275')
func_3279_call = mutated_mod.get_global_var('func_3279')
const_3536 = relay.const([[-2,-7],[-2,7],[-4,7],[-3,-4],[10,2],[-3,-1],[2,10],[-9,-4],[-3,-3],[7,7],[9,5],[-3,-6],[-2,-8],[-5,-3],[-10,-10],[5,-9],[-5,3],[4,-5],[6,-6],[-10,1],[-1,8],[-9,-4],[8,-7],[6,-1],[-10,-4],[6,9],[1,10],[-8,-7],[9,4],[8,8],[-1,-7],[3,-9],[2,-9],[-3,10],[-6,9],[-1,-2],[2,10],[-3,6],[-3,1],[10,-1],[3,1],[-2,2],[-9,-9],[-9,-3],[-6,-3],[-3,-3],[1,-4],[-3,-3],[7,-2],[5,5],[7,6],[-7,-9],[2,-4],[-8,-1],[10,-9],[-10,-9],[6,-4],[-7,5],[-4,-2],[-8,6],[2,4],[6,8],[-1,-10],[9,8],[3,4],[-10,6],[8,7],[-10,7],[-2,9],[-8,-5],[-5,-10],[4,-8],[9,-7],[-1,-4],[-2,6],[-5,-1],[3,4],[-10,-2],[4,7],[-1,5],[7,10],[-8,6],[7,-1],[4,-9],[3,-10],[-2,7],[-6,4],[-9,7],[4,3],[-6,-1],[10,7],[-3,5],[-2,10],[-9,10],[9,-3],[6,4],[1,-1],[6,-10],[-3,2],[-5,-3],[-2,-1],[-9,-4],[-8,7],[-9,5],[8,-7],[-7,1],[-5,-7],[8,7],[4,-10],[-10,3],[3,3],[3,-4],[-3,7],[7,1],[1,-2],[9,-10],[9,8],[-6,9],[-3,3],[-10,8],[7,3],[-3,8],[4,4],[1,-8],[4,2],[-9,9],[-5,9],[-9,-9],[2,10],[8,-9],[10,-6],[7,-1],[-2,-1],[6,-4],[-2,6],[-1,8],[7,-9],[8,7],[-3,-8],[7,-9],[4,1],[-10,9],[-7,3],[-10,-3],[1,-3],[-2,-6],[5,5],[-3,10],[-6,5],[5,8],[-1,-2],[-2,-1],[9,-9],[-6,5],[-8,3],[5,-7],[6,7],[-8,-7],[-3,-1],[6,-7],[7,3],[2,-7],[8,-2],[-5,6],[-4,5],[7,2],[-1,-7],[8,9],[2,1],[1,6],[7,-4],[10,-6],[-2,-6],[-2,-9],[5,1],[1,-9],[3,-9],[-7,6],[5,-6],[2,9],[2,-3],[8,-9],[-1,4],[-10,7],[10,-10],[10,-1],[-7,-2],[-1,-5],[10,7],[-3,9],[-5,-5],[6,8],[7,3],[5,-6],[2,-3],[1,-6],[-7,9],[9,5],[-10,9],[-4,2],[-7,1],[-10,4],[5,5],[-5,-8],[-3,-4],[2,-6],[-2,8],[4,-7],[4,2],[-5,8],[-4,-7],[-3,3],[2,8],[-9,-8],[-1,-8],[6,-7],[5,6],[6,1],[4,-8],[5,-3],[-9,2],[-7,-8],[9,-7],[-3,-5],[6,10],[5,1],[-1,6],[-8,-4],[-4,-6],[1,1],[-2,-2],[3,-3],[9,8],[-5,3],[7,4],[2,4],[-6,-5],[4,4],[-4,-1],[6,-3],[-7,10],[1,-10],[5,-6],[1,1],[10,-6],[-3,2],[-1,-4],[9,1],[-8,10],[4,-10],[3,6],[-7,5],[4,-4],[4,-4],[-1,1],[6,7],[-4,-5],[-8,-7],[-10,9],[9,-7],[-5,-2],[8,-5],[4,10],[9,6],[-6,-4],[-8,7],[4,-7],[10,-8],[4,-8],[-5,3],[1,1],[-3,-5],[-10,5],[-10,7],[-8,6],[8,-7],[-3,-7],[7,10],[-5,8],[-2,9],[2,1],[6,-3],[-10,-4],[-5,1],[3,-8],[7,-10],[3,-10],[-1,-6],[-3,-4],[-2,-3],[7,1],[8,4],[9,4],[2,-10],[-2,-7],[-1,5],[-9,-3],[7,3],[5,10],[7,5],[-5,-4],[10,1],[4,6],[-2,-9],[1,2],[-10,-4],[1,6],[-7,6],[9,9],[3,3],[10,5],[2,3],[-6,1],[-9,8],[-8,-10],[7,-7],[7,8],[-7,-1],[2,-9],[8,10],[-6,-9],[-6,7],[-3,-9],[6,-9],[-3,4],[1,9],[1,-10],[9,-4],[-10,9],[10,-2],[-4,5],[8,-2],[-2,10],[-4,-7],[-6,-4],[4,1],[-1,-2],[8,-5],[-4,2],[-4,-10],[3,-8],[-1,-1],[-1,-4],[-3,10],[5,6],[-3,-8],[1,8],[6,-2],[2,-9],[-6,-9],[-7,3],[-8,-5],[-5,10],[10,-7],[-10,8],[5,-9],[1,-9],[8,5],[3,-5],[-3,5],[1,-7],[3,-2],[1,1],[2,-4],[-5,2],[-2,-7],[7,5],[-4,7],[10,-4],[8,-6],[-8,6],[4,-4],[2,2],[-5,9],[3,-1],[8,10],[-3,-1],[-4,1],[-5,-3],[8,9],[3,6],[-10,-1],[10,-10],[1,-6],[-6,-7],[-5,4],[9,8],[5,7],[-9,-8],[-7,4],[1,8],[5,6],[3,4],[6,-8],[7,10],[3,2],[10,3],[-6,-7],[-2,-9],[-8,-2],[10,9],[-6,-9],[-2,5],[-8,-9],[6,8],[-10,7],[9,-3],[-2,-6],[-1,-8],[-1,-9],[8,10],[10,6],[3,8],[-10,-9],[2,4],[5,6],[-4,-4],[-1,-7],[7,-5],[-7,5],[-7,-5],[-9,-6],[6,-4],[-1,-8],[3,9],[3,3],[3,10],[-2,-2],[-9,8],[3,10],[-3,10],[-5,8],[-10,-3],[4,6],[-7,9],[-1,-10],[10,-10],[-1,2],[-3,9],[-3,-7],[5,8],[8,-7],[10,4],[-7,-4],[2,7],[4,-9],[-2,-6],[-7,-9],[-5,-2],[-3,-9],[6,-6],[10,9],[-6,5],[-6,9],[-5,4],[-10,-6],[10,-9],[10,-5],[1,-9],[-5,-3],[5,-3],[4,-2],[8,3],[-8,2],[-9,-2],[7,5],[-1,9],[3,1],[1,8],[7,-4],[-5,-1],[-8,-3],[-4,-7],[-2,-8],[-7,3],[10,5],[-7,7],[-4,-8],[-10,3],[4,6],[-1,-8],[5,10],[-5,-9],[8,-6],[-10,8],[6,4],[7,-5],[-5,8],[3,-3],[-1,10],[7,-3],[-5,7],[-4,9],[4,-5],[3,1],[-10,-6],[-6,1],[1,3],[3,10],[-7,-3],[-3,-8],[-10,-8],[-2,10],[2,4],[2,-5],[-9,8],[6,-9],[-6,-1],[-9,-8],[3,-9],[-8,6],[-7,-8],[-6,-2],[3,8],[-10,4],[1,7],[-6,6],[-10,2],[-8,-8],[9,-3],[-10,1],[-7,-5],[-5,-4],[-4,-8],[-5,-10],[1,-5],[-10,-3],[-10,5],[1,5],[4,6],[-1,-8],[3,-7],[-10,5],[9,-2],[4,10],[-10,-6],[-9,-1],[-3,4],[9,-8],[10,1],[10,-3],[8,10],[1,-8],[4,-3],[6,-8],[1,10],[-4,2],[-4,3],[-1,-5],[-2,-2],[6,3],[7,1],[-10,-2],[-10,2],[-3,-9],[-9,10],[-9,-10],[-1,-1],[4,5],[9,-5],[-6,9],[9,2],[-6,-8],[-3,5],[-5,-2],[-9,1],[6,7],[3,-6],[8,7],[-7,-1],[7,-9],[8,-2],[-1,7],[-7,5],[6,9],[-5,10],[-10,-1],[3,-3],[-1,-3],[-8,-10],[-9,-1],[9,8],[-8,-7],[-3,6],[-4,-4],[9,1],[10,9],[-9,7],[9,-2],[3,-4],[-8,6],[9,-7],[-1,2],[-10,1],[7,8],[-10,3],[4,-8],[5,8],[4,-9],[7,8],[8,-7],[-4,-8],[10,-8],[4,10],[7,3]], dtype = "uint16")#candidate|3536|(605, 2)|const|uint16
const_3537 = relay.const([[-6,7,4,8,-3,-9,-6,1,-10,7,1,-2,-7,4,2,10,-4,1,3,1,-10,8,-1,-4,-7,-10,10,-9,-2,8,8,3,-7,9,-4,5,-3,10,1,-3,-6,9,5,-4,10,1,2,-9],[10,8,-10,-10,7,5,7,-6,-2,-10,2,4,-7,-1,2,-7,-2,10,9,5,3,4,9,-4,7,-10,9,-5,10,7,-8,8,-9,-1,8,4,5,1,2,-7,-1,-9,10,9,2,5,2,7],[2,2,4,-3,-6,7,2,-6,-2,5,1,-3,2,2,-1,-5,-8,5,3,-5,4,6,7,-1,8,-10,-10,3,-2,3,-5,8,-5,7,3,-6,5,5,5,10,9,-4,2,-10,2,8,4,-3],[1,9,-4,-10,-1,3,-10,7,1,-10,-9,-7,-6,10,-3,2,-5,-7,-8,-9,4,4,3,3,3,8,4,4,-2,-1,-7,10,-6,10,6,2,1,1,-7,9,10,3,3,-5,10,-2,10,9]], dtype = "uint64")#candidate|3537|(4, 48)|const|uint64
call_3535 = relay.TupleGetItem(func_3275_call(relay.reshape(const_3536.astype('uint16'), [1210,]), relay.reshape(const_3537.astype('uint64'), [192,]), ), 1)
call_3538 = relay.TupleGetItem(func_3279_call(relay.reshape(const_3536.astype('uint16'), [1210,]), relay.reshape(const_3537.astype('uint64'), [192,]), ), 1)
func_1642_call = mod.get_global_var('func_1642')
func_1643_call = mutated_mod.get_global_var('func_1643')
call_3554 = relay.TupleGetItem(func_1642_call(), 0)
call_3555 = relay.TupleGetItem(func_1643_call(), 0)
bop_3569 = relay.logical_xor(const_3536.astype('int8'), relay.reshape(call_3535.astype('int8'), relay.shape_of(const_3536))) # shape=(605, 2)
bop_3572 = relay.logical_xor(const_3536.astype('int8'), relay.reshape(call_3538.astype('int8'), relay.shape_of(const_3536))) # shape=(605, 2)
func_1534_call = mod.get_global_var('func_1534')
func_1536_call = mutated_mod.get_global_var('func_1536')
call_3574 = relay.TupleGetItem(func_1534_call(relay.reshape(call_3522.astype('float32'), [2, 4, 16])), 0)
call_3575 = relay.TupleGetItem(func_1536_call(relay.reshape(call_3522.astype('float32'), [2, 4, 16])), 0)
bop_3580 = relay.minimum(call_3505.astype('int8'), relay.reshape(call_3574.astype('int8'), relay.shape_of(call_3505))) # shape=(2, 4, 16)
bop_3583 = relay.minimum(call_3506.astype('int8'), relay.reshape(call_3575.astype('int8'), relay.shape_of(call_3506))) # shape=(2, 4, 16)
var_3587 = relay.var("var_3587", dtype = "float32", shape = (2, 4, 16))#candidate|3587|(2, 4, 16)|var|float32
bop_3588 = relay.less_equal(call_3522.astype('bool'), relay.reshape(var_3587.astype('bool'), relay.shape_of(call_3522))) # shape=(2, 4, 16)
bop_3591 = relay.less_equal(call_3523.astype('bool'), relay.reshape(var_3587.astype('bool'), relay.shape_of(call_3523))) # shape=(2, 4, 16)
func_2775_call = mod.get_global_var('func_2775')
func_2776_call = mutated_mod.get_global_var('func_2776')
call_3602 = relay.TupleGetItem(func_2775_call(), 0)
call_3603 = relay.TupleGetItem(func_2776_call(), 0)
uop_3611 = relay.log10(const_3537.astype('float32')) # shape=(4, 48)
uop_3614 = relay.cos(uop_3611.astype('float64')) # shape=(4, 48)
output = relay.Tuple([call_3516,const_3517,call_3524,call_3554,bop_3569,bop_3580,bop_3588,call_3602,uop_3614,])
output2 = relay.Tuple([call_3518,const_3517,call_3525,call_3555,bop_3572,bop_3583,bop_3591,call_3603,uop_3614,])
func_3626 = relay.Function([var_3587,], output)
mod['func_3626'] = func_3626
mod = relay.transform.InferType()(mod)
var_3627 = relay.var("var_3627", dtype = "float32", shape = (2, 4, 16))#candidate|3627|(2, 4, 16)|var|float32
output = func_3626(var_3627)
func_3628 = relay.Function([var_3627], output)
mutated_mod['func_3628'] = func_3628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1905_call = mod.get_global_var('func_1905')
func_1906_call = mutated_mod.get_global_var('func_1906')
call_3655 = relay.TupleGetItem(func_1905_call(), 2)
call_3656 = relay.TupleGetItem(func_1906_call(), 2)
var_3681 = relay.var("var_3681", dtype = "float32", shape = (416,))#candidate|3681|(416,)|var|float32
bop_3682 = relay.less_equal(call_3655.astype('bool'), relay.reshape(var_3681.astype('bool'), relay.shape_of(call_3655))) # shape=(416,)
bop_3685 = relay.less_equal(call_3656.astype('bool'), relay.reshape(var_3681.astype('bool'), relay.shape_of(call_3656))) # shape=(416,)
func_2708_call = mod.get_global_var('func_2708')
func_2712_call = mutated_mod.get_global_var('func_2712')
var_3687 = relay.var("var_3687", dtype = "float32", shape = (416, 2))#candidate|3687|(416, 2)|var|float32
call_3686 = relay.TupleGetItem(func_2708_call(relay.reshape(var_3687.astype('float32'), [13, 4, 16]), relay.reshape(var_3687.astype('float32'), [13, 4, 16]), ), 8)
call_3688 = relay.TupleGetItem(func_2712_call(relay.reshape(var_3687.astype('float32'), [13, 4, 16]), relay.reshape(var_3687.astype('float32'), [13, 4, 16]), ), 8)
output = relay.Tuple([bop_3682,call_3686,var_3687,])
output2 = relay.Tuple([bop_3685,call_3688,var_3687,])
func_3698 = relay.Function([var_3681,var_3687,], output)
mod['func_3698'] = func_3698
mod = relay.transform.InferType()(mod)
var_3699 = relay.var("var_3699", dtype = "float32", shape = (416,))#candidate|3699|(416,)|var|float32
var_3700 = relay.var("var_3700", dtype = "float32", shape = (416, 2))#candidate|3700|(416, 2)|var|float32
output = func_3698(var_3699,var_3700,)
func_3701 = relay.Function([var_3699,var_3700,], output)
mutated_mod['func_3701'] = func_3701
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3778 = relay.const([[[-9.408773,-6.516624,9.379124,8.394991,9.844305,8.394719,1.861583],[-6.123763,6.686384,-5.546831,-7.508565,3.218715,-4.647758,-0.156756],[5.220509,5.059688,4.324404,-4.576750,-2.832584,-5.178395,-6.349207],[6.490665,-4.120832,-7.475545,3.980872,4.872848,-2.968021,0.476321],[-2.142765,-4.580019,6.658504,5.980060,6.535628,-1.365627,6.946734],[6.074170,-0.503646,8.228301,8.298720,1.038801,-7.494188,-6.150036]],[[0.852799,9.228664,8.201175,0.539861,1.257282,0.404087,-4.263892],[8.009609,4.197740,-5.394756,6.836791,-3.595904,1.500510,-2.348901],[-7.762057,-4.510029,-0.619216,9.496893,6.226875,6.523307,6.647233],[-4.096516,-5.042158,0.805830,-7.767666,4.492968,6.713225,-3.410496],[6.848727,-2.660165,7.205387,8.276408,-7.908188,-2.268831,9.034275],[1.739145,-8.554708,1.896490,6.755912,-2.278495,-7.492907,3.068311]],[[-5.938189,-0.582737,-7.482532,4.491498,-6.712165,-1.523282,-4.463070],[-2.716649,-9.425133,-9.119599,5.409900,0.208042,4.493857,9.516366],[1.185077,3.503747,-2.106716,-2.097583,4.655817,8.062511,-4.678628],[-8.457161,-0.307587,9.965268,-3.183798,5.787642,9.992979,-8.030935],[2.567586,-6.246787,6.120483,-2.676907,7.693046,-8.029244,-5.082731],[-1.393866,9.970785,5.035271,-8.926938,-7.770039,4.535802,-5.466329]],[[-7.390834,8.090717,-6.890948,4.296334,3.517066,-8.742722,-0.595569],[5.775308,-0.538860,3.295263,8.955228,5.262562,0.589259,-4.815778],[1.796455,7.358389,-7.399197,5.597921,-7.985580,-2.757897,-7.405812],[1.165358,2.762064,-7.235254,-2.193512,-8.164885,-9.866281,2.761244],[3.076753,-5.658817,3.063003,0.253964,-9.895177,-8.635470,0.976727],[7.236308,7.412953,-0.250674,9.972674,-3.047377,-7.131425,3.208354]],[[-3.505715,4.646515,5.544575,2.854856,2.500014,-6.611051,5.399827],[5.923058,9.693659,3.093204,7.743040,5.222981,-0.939053,-4.943715],[-7.003613,6.467673,6.355564,5.444807,4.327289,1.434807,7.266411],[-8.129554,-3.574054,1.641501,-6.098501,3.596007,-8.364775,0.134974],[-0.978197,9.966621,6.578354,-1.397831,2.615507,3.529515,-0.324075],[-6.793699,-0.896452,-0.879008,-4.335099,-0.229773,-8.234394,-9.952600]],[[2.209307,0.069934,6.553858,-0.819155,-8.637567,6.057585,-7.517449],[-8.677977,5.649876,-6.952635,7.927454,4.154826,-6.860271,1.595622],[9.236112,4.925139,9.884905,-8.302052,-3.782547,6.286279,3.308842],[-3.496388,-6.166994,-6.251349,9.220759,6.205484,-8.282277,-2.010216],[5.410830,4.800205,0.771039,6.325850,-9.438948,-6.082807,-3.148770],[5.208794,-8.064653,-4.271796,-8.797635,4.411858,2.854070,-5.222054]],[[8.202974,8.445093,-0.150560,9.605013,6.750830,-7.872226,-3.862599],[-3.676636,7.358540,4.869214,-6.355855,-9.172321,-1.727060,-3.743678],[-6.024104,1.141550,-3.732685,-2.776805,-4.062538,-0.738164,-8.875120],[9.729366,8.745911,-4.136928,5.029417,4.066297,9.496208,-5.956641],[9.160839,6.665800,2.018580,9.914969,4.654894,5.450188,8.965018],[-9.086352,-4.635788,-7.452325,6.826377,-3.447381,-6.006701,-1.678905]],[[5.727473,-1.973952,-9.822101,9.057147,-8.486026,1.744073,-4.368491],[4.278699,-0.654658,-8.122182,3.462047,5.318638,4.766990,1.042568],[2.474292,5.523000,-8.585714,2.544275,9.161333,3.797160,0.585242],[-4.603246,6.030277,4.723442,7.823136,-0.092317,-1.035727,6.761655],[-7.791465,-5.530751,8.423938,-3.271286,4.154567,-7.294465,-5.586030],[-8.177186,-5.799807,-1.712251,7.408934,9.158437,8.962716,0.929088]],[[1.457480,8.525994,-5.301232,4.389315,8.629964,1.560841,6.699190],[4.281821,1.791525,4.374033,-8.079783,9.609157,6.675188,-0.927507],[1.447131,6.229944,5.771483,-0.543768,-5.907336,2.401785,2.805887],[-0.711378,-7.028494,2.510063,8.382492,7.948318,-5.140450,5.006750],[8.970526,-2.546645,-9.757111,-1.709689,-2.006680,6.219133,-4.582986],[-8.135413,5.887950,9.831008,-3.702555,-0.028452,0.068450,-7.027941]],[[-7.348298,-9.941501,3.933126,-8.352831,-4.072330,0.089616,4.593530],[6.660099,9.897491,-0.545446,-0.527072,-6.852589,-4.567543,-7.881571],[-0.381685,0.485274,4.687422,4.794815,-3.524636,-0.669959,-0.827306],[1.456638,-0.158237,5.780647,-5.933264,-9.313061,9.475002,8.047149],[7.562466,-3.378078,-9.879054,7.797581,2.528290,4.264738,-4.205681],[-4.373506,1.719532,4.158853,-5.798636,-7.197041,-8.617216,1.494308]],[[4.547724,2.709615,-9.262069,2.538290,7.894719,-5.094330,8.141942],[-9.764309,9.432765,-9.834724,-9.562753,-8.152891,-4.663582,0.576441],[-3.734149,1.912073,0.059675,-7.791609,-9.101224,0.279730,-8.234888],[-6.838570,3.360456,-2.817596,1.619962,9.861388,-2.481971,-8.727416],[-6.332623,8.999639,-0.996248,7.672701,2.497516,1.778116,6.854247],[9.673421,3.484634,3.444994,-4.023290,6.505787,-9.603517,8.467577]],[[9.046667,8.303122,0.161354,-9.837467,8.943137,7.078891,7.172442],[-8.895232,4.794501,3.951507,1.803309,7.362877,-8.399609,0.928609],[-6.698890,4.742325,-9.727522,9.809782,2.022923,7.391262,0.658892],[6.238608,-2.326572,5.169238,7.286257,-0.428221,9.732768,-5.003225],[-2.844960,-7.841589,-8.331235,-0.349752,2.462388,-5.099231,7.574626],[4.417955,-9.050308,-7.455000,4.075308,4.885935,-1.819583,9.968741]],[[8.277853,5.750543,-1.497112,-0.682690,5.091852,5.006760,6.278613],[6.621793,-4.605528,0.590865,5.898706,2.814511,-2.819500,4.236319],[-7.153731,-7.582199,-5.550897,5.455600,-5.327019,7.211805,3.809701],[-7.689833,-5.251958,6.674296,-1.618140,6.582748,-4.280733,-2.772760],[5.836009,5.255498,6.213414,-5.758158,3.006279,-2.758079,0.865092],[6.857929,-4.800473,1.127715,7.028709,3.985536,-4.586908,5.143536]]], dtype = "float64")#candidate|3778|(13, 6, 7)|const|float64
uop_3779 = relay.exp(const_3778.astype('float64')) # shape=(13, 6, 7)
uop_3782 = relay.atanh(const_3778.astype('float64')) # shape=(13, 6, 7)
func_1239_call = mod.get_global_var('func_1239')
func_1243_call = mutated_mod.get_global_var('func_1243')
var_3789 = relay.var("var_3789", dtype = "bool", shape = (3328,))#candidate|3789|(3328,)|var|bool
const_3790 = relay.const([-6,-5,8,-1,-10,-5,5,6,-1,-7,-1,-4], dtype = "uint64")#candidate|3790|(12,)|const|uint64
call_3788 = relay.TupleGetItem(func_1239_call(relay.reshape(var_3789.astype('bool'), [16, 13, 16]), relay.reshape(const_3790.astype('uint64'), [12,]), ), 2)
call_3791 = relay.TupleGetItem(func_1243_call(relay.reshape(var_3789.astype('bool'), [16, 13, 16]), relay.reshape(const_3790.astype('uint64'), [12,]), ), 2)
output = relay.Tuple([uop_3779,uop_3782,call_3788,var_3789,const_3790,])
output2 = relay.Tuple([uop_3779,uop_3782,call_3791,var_3789,const_3790,])
func_3829 = relay.Function([var_3789,], output)
mod['func_3829'] = func_3829
mod = relay.transform.InferType()(mod)
var_3830 = relay.var("var_3830", dtype = "bool", shape = (3328,))#candidate|3830|(3328,)|var|bool
output = func_3829(var_3830)
func_3831 = relay.Function([var_3830], output)
mutated_mod['func_3831'] = func_3831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1602_call = mod.get_global_var('func_1602')
func_1604_call = mutated_mod.get_global_var('func_1604')
call_3843 = func_1602_call()
call_3844 = func_1602_call()
uop_3845 = relay.cos(call_3843.astype('float32')) # shape=(3, 13, 5)
uop_3847 = relay.cos(call_3844.astype('float32')) # shape=(3, 13, 5)
output = relay.Tuple([uop_3845,])
output2 = relay.Tuple([uop_3847,])
func_3867 = relay.Function([], output)
mod['func_3867'] = func_3867
mod = relay.transform.InferType()(mod)
output = func_3867()
func_3868 = relay.Function([], output)
mutated_mod['func_3868'] = func_3868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1905_call = mod.get_global_var('func_1905')
func_1906_call = mutated_mod.get_global_var('func_1906')
call_3880 = relay.TupleGetItem(func_1905_call(), 0)
call_3881 = relay.TupleGetItem(func_1906_call(), 0)
output = call_3880
output2 = call_3881
func_3888 = relay.Function([], output)
mod['func_3888'] = func_3888
mod = relay.transform.InferType()(mod)
mutated_mod['func_3888'] = func_3888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3888_call = mutated_mod.get_global_var('func_3888')
call_3889 = func_3888_call()
output = call_3889
func_3890 = relay.Function([], output)
mutated_mod['func_3890'] = func_3890
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3896 = relay.var("var_3896", dtype = "int32", shape = ())#candidate|3896|()|var|int32
const_3897 = relay.const([[1],[-3]], dtype = "int32")#candidate|3897|(2, 1)|const|int32
bop_3898 = relay.maximum(var_3896.astype('int32'), const_3897.astype('int32')) # shape=(2, 1)
func_1534_call = mod.get_global_var('func_1534')
func_1536_call = mutated_mod.get_global_var('func_1536')
var_3925 = relay.var("var_3925", dtype = "float32", shape = (128,))#candidate|3925|(128,)|var|float32
call_3924 = relay.TupleGetItem(func_1534_call(relay.reshape(var_3925.astype('float32'), [2, 4, 16])), 0)
call_3926 = relay.TupleGetItem(func_1536_call(relay.reshape(var_3925.astype('float32'), [2, 4, 16])), 0)
bop_3928 = relay.greater(call_3924.astype('bool'), var_3896.astype('bool')) # shape=(2, 4, 16)
bop_3931 = relay.greater(call_3926.astype('bool'), var_3896.astype('bool')) # shape=(2, 4, 16)
bop_3943 = relay.not_equal(var_3925.astype('bool'), bop_3898.astype('bool')) # shape=(2, 128)
var_3949 = relay.var("var_3949", dtype = "bool", shape = (2, 4, 16))#candidate|3949|(2, 4, 16)|var|bool
bop_3950 = relay.right_shift(bop_3928.astype('int32'), relay.reshape(var_3949.astype('int32'), relay.shape_of(bop_3928))) # shape=(2, 4, 16)
bop_3953 = relay.right_shift(bop_3931.astype('int32'), relay.reshape(var_3949.astype('int32'), relay.shape_of(bop_3931))) # shape=(2, 4, 16)
func_1968_call = mod.get_global_var('func_1968')
func_1970_call = mutated_mod.get_global_var('func_1970')
call_3962 = relay.TupleGetItem(func_1968_call(), 1)
call_3963 = relay.TupleGetItem(func_1970_call(), 1)
bop_3968 = relay.equal(bop_3943.astype('bool'), var_3925.astype('bool')) # shape=(2, 128)
uop_3982 = relay.exp(bop_3968.astype('float32')) # shape=(2, 128)
output = relay.Tuple([bop_3950,call_3962,uop_3982,])
output2 = relay.Tuple([bop_3953,call_3963,uop_3982,])
func_3993 = relay.Function([var_3896,var_3925,var_3949,], output)
mod['func_3993'] = func_3993
mod = relay.transform.InferType()(mod)
var_3994 = relay.var("var_3994", dtype = "int32", shape = ())#candidate|3994|()|var|int32
var_3995 = relay.var("var_3995", dtype = "float32", shape = (128,))#candidate|3995|(128,)|var|float32
var_3996 = relay.var("var_3996", dtype = "bool", shape = (2, 4, 16))#candidate|3996|(2, 4, 16)|var|bool
output = func_3993(var_3994,var_3995,var_3996,)
func_3997 = relay.Function([var_3994,var_3995,var_3996,], output)
mutated_mod['func_3997'] = func_3997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2240_call = mod.get_global_var('func_2240')
func_2242_call = mutated_mod.get_global_var('func_2242')
call_4015 = relay.TupleGetItem(func_2240_call(), 2)
call_4016 = relay.TupleGetItem(func_2242_call(), 2)
func_2252_call = mod.get_global_var('func_2252')
func_2254_call = mutated_mod.get_global_var('func_2254')
call_4033 = func_2252_call()
call_4034 = func_2252_call()
var_4052 = relay.var("var_4052", dtype = "float32", shape = (128,))#candidate|4052|(128,)|var|float32
bop_4053 = relay.logical_or(call_4015.astype('bool'), relay.reshape(var_4052.astype('bool'), relay.shape_of(call_4015))) # shape=(128,)
bop_4056 = relay.logical_or(call_4016.astype('bool'), relay.reshape(var_4052.astype('bool'), relay.shape_of(call_4016))) # shape=(128,)
func_3162_call = mod.get_global_var('func_3162')
func_3165_call = mutated_mod.get_global_var('func_3165')
const_4064 = relay.const(-9, dtype = "uint64")#candidate|4064|()|const|uint64
var_4065 = relay.var("var_4065", dtype = "uint64", shape = (48, 4))#candidate|4065|(48, 4)|var|uint64
call_4063 = relay.TupleGetItem(func_3162_call(relay.reshape(const_4064.astype('uint64'), []), relay.reshape(var_4065.astype('uint64'), [16, 12, 1]), ), 0)
call_4066 = relay.TupleGetItem(func_3165_call(relay.reshape(const_4064.astype('uint64'), []), relay.reshape(var_4065.astype('uint64'), [16, 12, 1]), ), 0)
uop_4068 = relay.cos(var_4065.astype('float64')) # shape=(48, 4)
var_4074 = relay.var("var_4074", dtype = "uint64", shape = (48, 4))#candidate|4074|(48, 4)|var|uint64
bop_4075 = relay.divide(var_4065.astype('float64'), relay.reshape(var_4074.astype('float64'), relay.shape_of(var_4065))) # shape=(48, 4)
uop_4102 = relay.exp(uop_4068.astype('float32')) # shape=(48, 4)
func_2541_call = mod.get_global_var('func_2541')
func_2543_call = mutated_mod.get_global_var('func_2543')
const_4116 = relay.const([[1.073359,-4.118324,-5.801514,1.862209,4.900962,-2.402558,-4.362187,-6.381523,7.962566,-1.015396,-2.585816,-4.816993,-3.672325,-8.831213,2.947301,7.032846,-5.632261,-5.070288,-4.900792,-9.070829,-7.284352,4.969370,2.277242,6.923638,7.624524,-5.139187,9.398061,7.726492,-3.196261,-1.237976,0.348248,7.481495,4.843941,-9.330337,2.236186,-7.927172,2.182040,-2.905704,2.127504,4.538344,0.053147,2.074267,-5.568023,-4.920852,-6.509600,-4.767665,-5.429739,1.009204,7.190284,-0.076020,4.055928,2.562506,-1.352622,1.245918,7.864324,1.836458,-7.272892,5.198105,3.813745,-1.951709,-9.131355,0.735667,-4.774639,-2.321526,-5.400111,-9.895598,7.809439,2.053763,5.469836,-5.103937,8.712502,6.307511,-0.325837,6.793515,8.132577,1.763442,-9.811740,-4.732829,2.609629,3.571528,5.173356,1.786332,3.009518,7.936138,-7.739450,3.368356,7.141210,0.359860,6.402691,9.775911,-9.037847,-0.630826,-1.525541,9.886246,2.782856,4.848586,-6.651347,-1.163176,9.160256,-0.794339,7.891969,-2.589106,4.930972,-5.407181,-0.666010,0.988970,-3.461549,0.376640,-4.200777,-5.003238,0.149722,4.335749,6.094919,2.703455,5.087035,-3.847173,2.252470,6.660056,-4.159027,3.003167,4.250120,-3.548018,-6.555416,-9.114219,-2.866442,2.587042,8.946720,-4.510013,-3.085916,1.587970,8.680447,-3.008353,-2.304069,9.364794,4.453258,6.512438,2.641051,-6.537626,-8.740508,2.826009,6.794553,-4.725036,5.913324,2.159382,5.166816,5.757644,-4.404455,3.191878,5.832543,-9.378952,-4.133993,1.948099,3.010952,0.498360,8.170047,-4.779745,2.379785,5.406836,1.641475,-6.730468,5.044529,-3.924800,6.872850,9.575281,-1.703793,2.524842,6.131670,5.769455,-7.266319,-5.836774,7.374585,5.033434,-4.640496,2.777982,2.938656,-0.928321,5.455671,4.710213,-5.549919,1.168189,-6.187521,4.415804,2.285361,-5.061440,-0.915866,8.473299,7.075588,-7.336477,9.224891,-5.139565,-3.054384,-5.607072,0.526981,-2.760652,-6.867013,-3.769214,2.322665,-9.746994,-3.158152,-5.286067,-0.629673,-9.733170,-9.033698,3.257552,-4.943244,9.287071,-9.068401,-2.357953],[6.814029,7.759066,-4.917007,-8.107337,-1.910151,5.093786,2.664190,2.103170,9.340160,7.610511,-6.375578,-1.368304,-9.684644,5.401475,6.600275,-0.656583,6.963464,-0.308925,-7.481820,9.667501,2.336059,1.756211,-5.188618,-6.809382,8.851521,-9.473528,-1.418354,-6.162712,-1.848268,8.497428,-5.316948,-5.443856,-2.946819,6.397235,2.455312,7.551648,4.221958,0.618442,2.086918,-7.338576,2.005835,-9.741262,2.225442,5.784197,7.308004,7.456504,-8.464485,4.587637,-5.661657,9.392019,9.030467,-2.591989,-8.969687,-5.533249,-5.779255,-1.576869,0.628371,3.606769,0.790905,-5.307458,-0.958256,-4.019353,1.193308,0.002103,5.815570,8.812469,9.725197,0.738383,9.439574,4.069195,-2.209407,-1.665327,-7.912349,-9.411647,-9.736478,-7.515406,-4.950445,6.738337,-8.314970,2.733887,-6.718226,-6.975532,8.545991,3.764622,-4.323556,-6.716361,-7.543655,-5.780248,-1.248089,-5.928157,-9.602702,6.499450,-3.811178,-5.349910,6.862440,-6.371314,5.225047,1.223166,-7.696698,4.009780,0.473215,-3.082309,-8.096426,6.994330,8.220318,4.540273,-5.373389,0.813438,-2.052315,-9.989667,6.476039,9.927461,4.926154,0.737973,2.112135,-9.419697,-8.104149,-7.991921,-4.953274,-4.674674,9.155682,5.863219,-6.495225,-3.786250,-2.554143,2.147531,4.980324,-1.422955,4.293139,5.750192,7.585400,-3.220842,-9.225165,-8.448351,-0.852185,-7.668930,0.729227,9.724978,-9.729667,-6.119616,-9.956665,0.173494,-9.016447,2.529244,5.132822,-4.021151,-9.890801,4.688264,8.973470,7.287219,-1.172331,9.975238,5.602535,1.861242,1.025925,1.314823,9.946207,2.899266,-1.850260,-4.948416,0.896545,-3.416133,1.607534,-9.795499,-6.596489,-9.121075,-1.194646,-5.018101,-9.953724,2.477556,9.025531,-8.066589,2.303267,-7.456471,-7.064525,-1.235651,0.239937,5.639588,-6.096154,0.649305,-9.094611,5.931009,4.625354,-7.299551,3.680051,8.805228,-4.535438,-1.994408,-8.800280,-5.731860,3.338987,-0.597681,9.052507,4.604216,-0.015072,-6.342969,-5.519013,2.828362,3.664601,7.169852,8.392245,8.348641,-0.170944,-6.051038,-4.531330,9.406221,5.158338,-0.322211]], dtype = "float32")#candidate|4116|(2, 208)|const|float32
call_4115 = relay.TupleGetItem(func_2541_call(relay.reshape(const_4116.astype('float32'), [416,])), 0)
call_4117 = relay.TupleGetItem(func_2543_call(relay.reshape(const_4116.astype('float32'), [416,])), 0)
bop_4118 = relay.power(uop_4102.astype('float32'), relay.reshape(var_4074.astype('float32'), relay.shape_of(uop_4102))) # shape=(48, 4)
output = relay.Tuple([call_4033,bop_4053,call_4063,const_4064,bop_4075,call_4115,const_4116,bop_4118,])
output2 = relay.Tuple([call_4034,bop_4056,call_4066,const_4064,bop_4075,call_4117,const_4116,bop_4118,])
func_4124 = relay.Function([var_4052,var_4065,var_4074,], output)
mod['func_4124'] = func_4124
mod = relay.transform.InferType()(mod)
var_4125 = relay.var("var_4125", dtype = "float32", shape = (128,))#candidate|4125|(128,)|var|float32
var_4126 = relay.var("var_4126", dtype = "uint64", shape = (48, 4))#candidate|4126|(48, 4)|var|uint64
var_4127 = relay.var("var_4127", dtype = "uint64", shape = (48, 4))#candidate|4127|(48, 4)|var|uint64
output = func_4124(var_4125,var_4126,var_4127,)
func_4128 = relay.Function([var_4125,var_4126,var_4127,], output)
mutated_mod['func_4128'] = func_4128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2322_call = mod.get_global_var('func_2322')
func_2323_call = mutated_mod.get_global_var('func_2323')
call_4149 = relay.TupleGetItem(func_2322_call(), 0)
call_4150 = relay.TupleGetItem(func_2323_call(), 0)
var_4162 = relay.var("var_4162", dtype = "float32", shape = (2, 4, 16))#candidate|4162|(2, 4, 16)|var|float32
bop_4163 = relay.bitwise_or(call_4149.astype('int64'), relay.reshape(var_4162.astype('int64'), relay.shape_of(call_4149))) # shape=(2, 4, 16)
bop_4166 = relay.bitwise_or(call_4150.astype('int64'), relay.reshape(var_4162.astype('int64'), relay.shape_of(call_4150))) # shape=(2, 4, 16)
output = bop_4163
output2 = bop_4166
func_4172 = relay.Function([var_4162,], output)
mod['func_4172'] = func_4172
mod = relay.transform.InferType()(mod)
mutated_mod['func_4172'] = func_4172
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4173 = relay.var("var_4173", dtype = "float32", shape = (2, 4, 16))#candidate|4173|(2, 4, 16)|var|float32
func_4172_call = mutated_mod.get_global_var('func_4172')
call_4174 = func_4172_call(var_4173)
output = call_4174
func_4175 = relay.Function([var_4173], output)
mutated_mod['func_4175'] = func_4175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3052_call = mod.get_global_var('func_3052')
func_3054_call = mutated_mod.get_global_var('func_3054')
call_4195 = relay.TupleGetItem(func_3052_call(), 0)
call_4196 = relay.TupleGetItem(func_3054_call(), 0)
func_3698_call = mod.get_global_var('func_3698')
func_3701_call = mutated_mod.get_global_var('func_3701')
const_4205 = relay.const([-2.204358,0.806333,3.159646,6.820811,-9.566681,-6.268073,-4.765148,2.031637,8.382337,8.409693,4.816920,3.671532,-3.843039,-5.353488,0.458949,-1.040152,-5.363565,-4.411438,-8.110865,6.786053,-7.208730,7.012046,6.112683,-6.026169,2.121969,-6.194859,1.573205,7.374665,-3.517762,5.669175,8.321227,-6.872871,4.317612,1.481942,-1.828968,-8.610865,6.607422,6.160351,-8.306555,7.976187,2.317400,-9.174547,5.519594,-5.030071,-2.244084,1.685203,7.457245,2.875908,-0.238488,-9.613752,3.951324,-7.369714,-5.252476,9.151516,2.784849,-6.093678,-6.285400,9.843483,-3.405878,-9.788588,5.448582,-2.498032,7.137777,-6.152065,-5.686438,-5.312344,2.221635,-0.615548,-1.119133,1.854060,-2.208408,-0.958584,-2.984992,-2.219168,4.708549,7.469436,-3.240732,9.986804,-4.679122,-8.538979,-6.831007,-5.631712,0.687423,7.488815,1.466884,1.515591,-1.204389,-0.491614,1.017217,7.996615,8.265155,6.664595,-0.157294,1.774250,-9.239633,0.850131,-8.924877,8.273415,9.369642,1.818722,9.380541,-0.140713,-6.279316,-9.207844,-4.796028,-8.198316,3.675417,4.462823,-8.843730,-9.255179,-6.630350,4.178472,4.806638,-8.860589,9.584247,8.369878,-9.272945,-9.655951,8.537097,-7.923964,-0.024680,9.900940,8.356786,7.171165,-0.860232,-1.884109,-2.816739,2.469434,-6.649790,-1.197889,-0.525433,-3.728902,4.702048,3.466558,-5.914648,-7.459236,5.140098,-3.136581,6.390195,-8.216206,9.243089,-4.453142,5.413978,9.027870,-6.166898,6.836288,-2.953232,5.614540,7.362554,-1.430108,1.927431,-6.623982,-0.784958,1.553314,7.809329,7.140996,-9.788674,-9.662124,-3.994612,-2.432655,1.805736,2.239003,1.646481,0.914396,6.376816,-2.774488,8.639522,3.823956,8.747633,2.420046,8.021401,5.531900,-6.299141,4.647323,-1.838667,8.980096,0.332536,0.010878,-6.236209,1.672925,-8.559389,-8.703114,4.808489,9.821065,-4.469418,5.405193,-8.580536,6.905347,-8.819481,3.253364,-7.804268,-2.583376,4.796176,6.020228,-6.134292,7.496123,-3.057922,-3.373634,-7.971082,5.668952,-7.739472,-4.698899,3.093860,-2.443619,-2.543923,-5.819586,-1.567408,-2.536549,-9.238516,8.310065,4.811598,7.111561,-3.178754,3.828244,-4.643903,3.733235,1.727246,9.196465,-3.186414,-9.905306,3.855124,9.382679,8.783807,7.755600,9.119804,-5.958871,7.595409,5.380362,-2.198095,-7.939180,3.588874,0.340833,5.348537,2.490912,-8.254905,-2.344852,4.790625,-1.811687,-3.593638,-5.286925,-4.136881,-2.784973,1.737226,-3.438582,-7.759948,-0.298542,-6.488263,-6.423157,-4.424085,6.528196,6.772179,-6.658928,-5.886921,0.946450,-0.990533,-1.241572,-1.201998,-9.415231,-1.187707,6.525782,-6.905596,-3.761240,-4.548955,-5.078618,4.422917,5.356859,-4.132712,3.481536,-4.753784,8.177374,-8.450900,-4.769188,-3.700786,-2.552794,7.662887,4.229877,0.504355,-6.721079,-9.011499,-3.357189,2.615262,-3.031822,5.745692,-8.391619,-7.683895,-0.824453,0.891094,8.769512,-5.256932,1.966136,-9.245329,1.955403,-6.126968,1.542977,-6.261681,-1.241150,1.529414,7.692043,-7.125483,2.244765,3.515072,-5.138052,-0.409785,-4.483188,3.546091,-0.750986,-3.281810,-5.903246,9.231492,8.502841,6.295189,6.991757,-4.028312,-8.237636,-3.555409,1.045556,5.756029,5.372195,-7.710718,-0.377908,6.156782,8.273964,-1.794058,-9.079592,0.068470,-0.641438,-4.072600,2.613143,-9.989589,1.342672,6.642756,9.890648,-7.946700,-2.931744,-7.929515,2.613136,6.683510,-4.746166,-2.676711,-9.788630,-2.907457,-1.995027,-6.345049,-9.377157,2.708075,-3.535189,-4.161514,-2.205018,-7.262806,5.651589,8.690358,-6.829813,8.350322,2.786465,7.141360,9.511466,-1.709077,-5.680817,-0.736767,9.327996,6.528328,-2.552625,1.617901,-5.661152,-0.050595,9.181261,-6.190685,-5.840764,-9.591917,7.404146,8.398097,1.630759,2.786332,0.283827,-9.813863,8.691658,-5.348266,-9.694320,-1.563825,8.018821,-1.892771,4.989452,-1.179512,8.197619,6.043470,-3.326570,2.216457,-2.949010,-7.014679,-7.597420,-6.283579,-1.879862,-6.291618,3.538458,2.415295,6.031987,7.997149,7.606617,-9.295353,-7.857471,7.933997,8.977724,-9.847704,8.682758,7.938963,-3.777261,-6.175858,-4.476191,5.456053,5.418785,-0.603424,-2.395915,2.521158,8.313009,-8.376240,9.865011], dtype = "float32")#candidate|4205|(416,)|const|float32
var_4206 = relay.var("var_4206", dtype = "float32", shape = (832,))#candidate|4206|(832,)|var|float32
call_4204 = relay.TupleGetItem(func_3698_call(relay.reshape(const_4205.astype('float32'), [416,]), relay.reshape(var_4206.astype('float32'), [416, 2]), ), 2)
call_4207 = relay.TupleGetItem(func_3701_call(relay.reshape(const_4205.astype('float32'), [416,]), relay.reshape(var_4206.astype('float32'), [416, 2]), ), 2)
uop_4212 = relay.asinh(call_4195.astype('float32')) # shape=(2, 4, 16)
uop_4214 = relay.asinh(call_4196.astype('float32')) # shape=(2, 4, 16)
var_4218 = relay.var("var_4218", dtype = "float32", shape = (416, 2))#candidate|4218|(416, 2)|var|float32
bop_4219 = relay.add(call_4204.astype('uint64'), relay.reshape(var_4218.astype('uint64'), relay.shape_of(call_4204))) # shape=(416, 2)
bop_4222 = relay.add(call_4207.astype('uint64'), relay.reshape(var_4218.astype('uint64'), relay.shape_of(call_4207))) # shape=(416, 2)
output = relay.Tuple([const_4205,var_4206,uop_4212,bop_4219,])
output2 = relay.Tuple([const_4205,var_4206,uop_4214,bop_4222,])
func_4225 = relay.Function([var_4206,var_4218,], output)
mod['func_4225'] = func_4225
mod = relay.transform.InferType()(mod)
var_4226 = relay.var("var_4226", dtype = "float32", shape = (832,))#candidate|4226|(832,)|var|float32
var_4227 = relay.var("var_4227", dtype = "float32", shape = (416, 2))#candidate|4227|(416, 2)|var|float32
output = func_4225(var_4226,var_4227,)
func_4228 = relay.Function([var_4226,var_4227,], output)
mutated_mod['func_4228'] = func_4228
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4241 = relay.var("var_4241", dtype = "float32", shape = (3, 11))#candidate|4241|(3, 11)|var|float32
uop_4242 = relay.log2(var_4241.astype('float32')) # shape=(3, 11)
output = relay.Tuple([uop_4242,])
output2 = relay.Tuple([uop_4242,])
func_4246 = relay.Function([var_4241,], output)
mod['func_4246'] = func_4246
mod = relay.transform.InferType()(mod)
mutated_mod['func_4246'] = func_4246
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4247 = relay.var("var_4247", dtype = "float32", shape = (3, 11))#candidate|4247|(3, 11)|var|float32
func_4246_call = mutated_mod.get_global_var('func_4246')
call_4248 = func_4246_call(var_4247)
output = call_4248
func_4249 = relay.Function([var_4247], output)
mutated_mod['func_4249'] = func_4249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1968_call = mod.get_global_var('func_1968')
func_1970_call = mutated_mod.get_global_var('func_1970')
call_4251 = relay.TupleGetItem(func_1968_call(), 1)
call_4252 = relay.TupleGetItem(func_1970_call(), 1)
uop_4259 = relay.log(call_4251.astype('float32')) # shape=(2, 4, 16)
uop_4261 = relay.log(call_4252.astype('float32')) # shape=(2, 4, 16)
func_3698_call = mod.get_global_var('func_3698')
func_3701_call = mutated_mod.get_global_var('func_3701')
const_4276 = relay.const([2.192881,-0.055571,-2.633663,4.021235,-3.761116,7.085103,-9.714371,4.237190,5.607539,9.406744,4.096413,-9.797584,-2.611410,5.554993,8.323968,-2.977089,-2.988862,2.918827,5.263011,4.958741,-3.772212,-8.682119,5.397810,9.281196,7.475704,3.115664,1.803890,-7.326026,0.404103,6.568845,4.903984,-2.040754,8.205513,-2.196736,-1.560277,-8.782869,-0.707424,4.637096,-8.250582,-5.458673,-5.316085,4.762156,-8.059539,3.198962,5.814427,-7.147215,-8.927612,3.024239,7.870168,1.216859,7.932038,-3.215263,-8.114096,-3.776383,0.311806,2.941426,-2.145392,1.452586,-4.481178,-5.821244,1.641944,-5.111517,4.516064,1.773646,7.889918,-2.672000,7.134518,9.262245,2.270683,-7.386835,-2.000883,-4.279789,-1.950515,9.100930,-9.837310,0.218093,3.024672,-6.186251,4.188347,6.977555,-8.905697,6.863864,-6.392613,3.265693,-2.182861,-2.598952,1.440867,3.118553,-1.631620,7.798010,8.363010,2.741938,-6.598319,7.482691,0.233638,2.033578,6.489355,5.078643,5.297980,1.770697,2.524112,-8.836934,-1.366165,-0.819383,7.684818,4.632156,-0.217850,9.467046,-8.909951,-7.834127,0.231823,8.047120,5.209234,-5.208710,-3.130779,-4.442558,-5.290767,-5.421913,6.927367,1.912379,-1.685232,8.696344,3.065857,-1.857064,0.513561,-3.886125,-5.305275,7.543781,-6.061806,-2.804294,0.550310,-8.649419,7.132913,-5.955644,-7.165000,8.870979,2.922744,4.834287,3.500914,-9.660284,4.591515,6.759864,3.004049,6.202255,2.884543,-9.367914,-2.981116,-8.822333,4.649257,-6.660905,-0.430470,8.923470,-1.151941,1.060320,-0.727747,5.516101,-8.893935,9.681447,2.329119,5.871143,-3.858236,-9.047609,1.325738,-5.099281,1.885009,-9.424462,0.447934,9.928246,-0.435769,6.298609,5.243585,-1.157283,-6.623830,6.718860,-1.614829,-9.089865,-9.538516,-8.274349,8.334747,-1.103523,9.991104,-0.034609,-7.343245,1.484257,-8.639298,3.602673,2.652447,3.375326,7.670017,1.447845,-4.613969,-8.347571,-1.803790,-7.031760,-2.593559,4.651735,3.781530,-9.301506,6.349031,-3.470233,-6.857698,7.078983,-8.389104,9.755412,6.674713,5.963919,-1.991704,-4.239173,-0.368159,-4.121018,-7.173412,8.850761,-0.612322,5.671002,1.668409,0.165888,-7.431730,8.013145,-8.650007,-8.397627,4.108542,7.761846,-0.530512,0.637391,-6.441794,2.319453,1.048516,-0.650165,-0.423531,4.767714,7.781671,7.707740,-3.416054,-2.592112,-4.179189,-8.233538,3.954151,8.577649,-3.354812,-1.914121,3.402544,8.514482,-9.224094,-7.806531,3.584507,-2.944043,-2.777717,-3.687455,-3.681416,6.844330,-4.894279,4.089224,1.125901,2.121613,6.359325,-9.858980,0.765263,8.985823,5.735036,-3.972948,6.603659,-2.999081,-8.295971,-8.849851,8.668680,0.025146,-1.511719,9.815310,-5.701104,7.593137,4.495989,-9.252923,1.141605,-8.912151,2.921023,7.349938,-7.463238,-9.711196,4.200433,1.196899,0.579106,-3.052880,1.997969,8.400618,-3.009491,8.303919,3.368151,-8.782666,9.671900,2.377251,1.746472,-8.853561,-3.914222,-1.436305,3.139610,0.138433,8.042801,-9.478350,6.627841,-5.120742,-3.310449,8.134153,5.428523,-5.030145,4.724134,7.923569,0.952622,-6.977086,-6.733971,6.895165,-7.379197,-4.544581,-5.702427,6.501292,5.670874,1.460889,0.286259,4.431866,-4.582444,-2.213019,9.331931,-7.774794,5.893902,8.248271,2.954099,0.689717,8.521927,6.087657,7.783031,4.940179,-0.888223,-4.614379,-3.075389,-5.531509,-0.782222,-8.327499,-0.209708,-2.494727,6.185265,-0.320571,-8.351320,-8.093880,3.254579,0.793336,-9.084904,3.004824,6.255493,9.590184,7.602132,-0.061395,-5.917273,-0.015274,4.053351,-3.461728,-6.733821,6.556037,-0.797497,-9.605124,-0.467659,-4.990025,-7.306975,2.804992,-1.667594,2.914777,4.659786,9.537438,-0.314217,-2.904811,-4.085416,-0.386674,9.578327,2.442482,-0.471446,-5.105116,7.875018,9.005347,-4.485799,0.556516,9.651297,9.002921,-7.305304,-4.732009,-0.753139,-6.753281,8.599925,4.105101,-5.139055,9.684933,-2.833495,4.650505,-4.055308,1.440804,-5.926545,0.293017,-5.749607,-7.784626,6.900917,7.881670,3.805895,-3.189809,9.241146,-4.925542,-5.958546,-2.219903,5.356415,-6.502880,-3.994126,-3.794302,-4.285411,2.507357,-5.204187,0.707839,-1.922516,5.501587,-4.911356,8.286127], dtype = "float32")#candidate|4276|(416,)|const|float32
const_4277 = relay.const([[-1.911855,-9.922356,-7.100784,6.371892,2.959743,4.820310,-0.498989,-7.246264,4.306796,-3.170426,1.674125,5.095646,-8.657135,-1.073455,-2.097734,3.268118,-0.418122,-7.874068,6.684317,2.435981,8.955296,1.710795,4.634864,-6.825768,-1.798689,0.246734,7.492505,-8.668438,-9.432545,-4.151786,-2.930279,1.811679,-8.549489,-8.308817,3.579258,-5.404039,-2.095949,-3.359800,-9.744541,-8.845503,-1.071690,-4.686003,-2.142122,9.664306,1.624985,-2.745670,-3.018028,-4.455248,0.110426,-1.346254,-5.473289,7.445193,-3.457241,-8.390603,-6.369661,5.128811,0.993152,5.707833,7.460928,-3.142434,-0.201708,-4.141890,-6.695490,1.723047,5.874754,2.175174,7.158532,-9.937803,-5.401315,-6.245885,-4.129131,5.214645,4.760678,2.737789,-4.484442,1.444661,-5.800866,8.688907,-9.568384,-8.182835,-0.655817,9.275372,1.701998,5.361300,9.958978,-3.494720,4.358396,3.742604,-5.530659,2.591884,-6.936190,-5.192651,6.763473,3.837574,-8.797457,0.369065,6.109152,-3.039496,7.263759,4.598368,5.753883,-5.247622,8.758408,4.592221,-2.869483,-6.806268,3.551793,-1.616792,-8.024891,-1.378712,3.484353,6.192622,0.047223,8.048945,3.430747,9.486313,7.773955,-2.363799,4.512804,-6.649420,-0.141144,-9.233522,6.918846,-4.399860,-4.543262,5.657144,5.327295,9.822121,-0.141698,3.760312,0.052235,5.090591,-0.593975,0.993681,1.396201,5.994475,5.932109,-1.622581,-7.413128,-7.734190,5.540506,3.990295,6.035763,7.438627,4.374297,5.004654,0.932251,2.351672,-1.172797,1.674106,8.850835,-8.198431,-1.627435,8.601259,4.062812,-6.535674,2.854821,6.131431,-9.802230,6.237885,2.856294,-2.137828,2.011568,-9.951667,-6.562074,6.774635,7.868188,-2.327245,-7.263242,-2.697746,-5.440112,4.090448,-0.136301,-6.763755,0.198537,7.041968,-1.863865,-4.724501,2.121984,-6.662721,-3.260517,2.205058,4.756070,-9.687164,-6.593469,1.347903,1.127571,-3.219588,-5.992021,-4.820089,-8.966125,-1.231233,5.781218,-1.644160,-9.579046,-3.054522,5.661388,-2.878451,-9.692380,-2.195429,1.414298,6.252619,-0.212347,6.346189,-1.721671,6.551208,8.659943,6.819922,-6.862588,2.882713,-2.962241,3.965356,-7.065095,-2.965519,-3.977707,0.475672,2.574953,-7.571829,-3.875430,-9.166452,3.735511,-9.784821,2.781218,5.775650,9.526486,-8.724040,3.480875,8.394604,4.857222,-2.644996,6.781964,-3.484894,-9.378819,-2.055140,-3.300422,1.158010,-1.526268,-1.497257,0.940978,7.577333,-2.587460,2.159051,-2.786457,5.177231,-5.413980,3.730851,1.929622,-7.511056,5.760925,3.096950,7.379039,1.934121,-0.264482,-5.731409,-4.097933,-0.352671,5.183745,-3.563686,5.962417,-4.067891,0.276504,7.042039,5.945503,-1.911442,-5.392269,-2.310885,-5.811901,-8.751032,1.233550,-8.121706,-2.032219,-2.372273,-8.934613,5.103486,3.976267,-0.401167,-1.445714,2.511806,7.851292,-9.161273,8.067523,-6.140783,-0.333406,-9.332057,9.352824,6.520964,-7.341893,4.225037,-5.935979,-0.181373,-2.689888,-7.664879,-9.949314,-5.482943,0.923623,3.465623,6.262584,-6.491066,-4.792819,2.944831,-2.577504,-4.491243,5.122801,5.517617,-2.943132,4.919057,-2.272540,8.020135,5.012530,1.677127,-6.753714,-6.749248,-7.176225,-8.881509,5.978561,-3.940174,-7.335085,-2.794287,-7.124550,-0.009031,3.180876,-5.914635,3.920595,-5.085100,5.010192,-7.758438,6.284738,-9.894940,4.616746,-9.293482,-9.143480,-9.131789,1.506586,-2.745464,7.180853,0.858904,-5.682821,-0.547961,2.588887,8.252283,-5.620425,4.304098,-6.125117,2.216996,-8.603894,-0.710356,-6.137865,1.659939,-2.027083,-0.744465,-2.049281,-5.863218,1.034183,8.043882,-2.187191,0.157338,-0.690408,-1.150775,-0.413948,-5.371199,1.089920,-0.840093,-3.268974,-6.660889,0.873875,-4.154389,-4.427266,6.981146,5.158722,-7.631963,6.066074,8.672194,-5.520084,-9.498549,2.286862,8.740434,3.792469,6.357255,-4.428631,-3.328495,-9.764569,9.984764,-6.974328,-1.477759,0.046650,7.391091,-8.264841,-6.383773,-1.210077,-8.834165,-8.689605,-8.181671,1.395630,2.238462,5.031560,2.474834,-8.480639,-0.142804,2.298701,-3.287421,-4.540385,8.749506,-5.740798,6.111138,-4.513450,9.448649,-9.139351,9.385438,2.586000,9.550721,-8.908753,-9.670292,1.719708,7.471280,5.961598,-7.100004,8.101961,-8.902880,2.932994,-8.461410,0.832358,-6.062095,-6.089554,1.938312,-7.883877,-8.245487,-3.829940,1.465577,-9.529998,-6.484319,9.070725,8.902447,4.036023,-5.708604,0.391735,-7.281066,-1.542900,-3.691640,-3.185651,-3.506828,-3.725059,-5.174915,2.724394,1.363328,-6.149365,9.901599,-8.466788,5.842244,7.173827,-7.195795,-5.775506,2.413758,-2.165928,4.630816,-1.610824,3.059736,3.360823,0.945062,-9.151368,-3.380920,-5.915961,-2.216095,-7.403887,-7.714516,6.813841,-4.975177,-2.758828,0.637559,-2.168220,9.539825,-3.508837,7.597034,-9.356433,9.650068,9.781708,-0.627156,9.635343,-8.736789,-8.971775,3.508392,-9.921617,2.427130,-6.475677,6.730547,-8.882332,0.856829,5.157257,-3.624644,2.460134,-8.244595,2.299764,-7.225186,8.297445,-0.119335,-3.931140,-6.024204,1.885518,6.594439,-1.126474,-5.302008,3.596262,5.980976,4.139362,3.399388,2.555985,6.170452,-8.441926,-3.701457,9.130663,8.067232,-7.052590,-2.946220,5.221181,4.817832,-6.884404,-9.102676,8.143217,-2.875081,1.680724,5.928834,-5.457111,1.887070,0.828457,-6.997195,-6.771241,-8.429346,9.845505,1.758308,-5.910971,-8.632196,-2.888324,-1.625157,9.279390,-4.657963,-7.055153,1.619918,5.866130,7.328936,-1.664907,2.068149,9.395130,-6.070904,-9.758910,-2.988125,-7.519951,9.781302,2.157626,7.438976,-1.512946,-4.763908,2.553926,6.744235,-8.651155,7.826877,6.424459,-0.862383,-0.976927,6.008254,-0.930285,3.570569,2.034257,9.059981,2.651432,1.296747,0.068221,-8.506476,4.476748,8.379657,4.587972,9.477871,0.282857,3.241125,-6.977282,-9.792368,-8.112711,1.471526,-7.699788,2.311384,3.115737,1.881013,-1.085093,-4.049532,-0.449614,8.977121,-0.317065,-6.568428,-1.484459,-6.183066,-1.599586,1.148564,-5.645390,-0.328735,-2.316516,-0.145849,-6.184585,-0.813075,-3.821998,2.051602,-6.298677,-6.107161,8.090666,-0.292652,-1.878683,-3.321404,1.312982,-0.826319,-7.780203,-5.167171,-7.826240,5.536712,-8.652044,3.935683,-6.471688,9.917083,9.009198,5.490908,-8.868639,0.618170,-6.317082,-9.945469,9.839039,-1.421748,2.459805,-1.184383,7.254788,4.101804,8.628869,-8.281612,1.614925,-3.267706,6.536205,3.435452,7.372550,8.506053,-5.701321,2.786928,-4.867993,1.749329,-9.157143,9.413439,4.902291,-5.134339,6.178085,-2.545073,-3.895870,1.207409,5.223851,-1.660933,1.657170,-6.197800,6.708321,-2.722671,1.019675,0.820028,7.086859,-8.745859,3.453263,-1.122486,9.435008,1.823217,3.025205,-9.161509,3.168123,-6.825069,-9.800868,-6.924671,-9.335145,6.424382,8.989209,-2.101203,3.370025,3.982417,9.762140,1.799072,6.042157,-0.060326,4.366669,1.640159,7.122457,-2.685448,-1.162304,9.416469,8.643636,3.721651,-1.743268,1.376304,-3.397718,-9.888829,-0.300681,-7.673316,9.277468,8.171285,7.347422,9.730184,-1.850118,-1.504043,9.076060,2.198223,-4.846398,6.954822,-7.943793,-3.296751,3.851494,-2.408744,-7.312160,7.610567,-9.074667,5.633486,1.872686,-6.094850,-3.074279,0.047256,7.362850,-7.315990,0.737149,-9.394490,-9.331252,-6.216210,8.433978,-2.175758,5.306315,9.729520,-8.628112,-7.423149,-0.869308,7.316187,9.215644,-3.081547,8.068697,3.681754,-1.205251,8.319342,-0.296305,-0.436827,-9.461177,-2.099818,2.941108,5.428257,-2.365496,0.203812,7.651942,7.487265,5.085285,3.266313,-5.561970,1.168093,-0.932488,1.337561,-4.890209,-5.263378,-7.991993,1.424584,9.355361,3.676765,-2.783243,-8.023746,2.361227,-1.345381,2.333178,-8.208574,-0.936085,-1.905844,-6.560363,-5.842161,4.647038,0.740572,2.521723,9.447304,-9.696737,-9.542125,-3.214190,-6.229493,-4.078440,-6.547029,-8.953909,9.151810,4.023713,8.394623,3.897501,-2.869556,-6.584204,8.527460,-1.782853,-4.524064,5.384798,4.721023,8.048252,-1.252951,6.162840,3.558585,9.617054,-5.828063,-4.662170,-0.082741,2.074215,6.666462,-3.187922,5.242568,6.190410,6.714497,-7.467155,-6.987735,-7.480273,0.185179,-1.230103,3.242337,2.294045,-1.832226,6.284877,-5.732761,3.388105,8.404285,-4.515739,6.430724,-7.140510,-6.218119,6.896789,8.785533,0.151732,2.270142,0.681263,7.123857,7.660642,0.741104,-1.045445,7.284885,4.174422,-8.230099,-2.663161,9.623943,-5.618975,9.977612]], dtype = "float32")#candidate|4277|(1, 832)|const|float32
call_4275 = relay.TupleGetItem(func_3698_call(relay.reshape(const_4276.astype('float32'), [416,]), relay.reshape(const_4277.astype('float32'), [416, 2]), ), 2)
call_4278 = relay.TupleGetItem(func_3701_call(relay.reshape(const_4276.astype('float32'), [416,]), relay.reshape(const_4277.astype('float32'), [416, 2]), ), 2)
uop_4295 = relay.sqrt(uop_4259.astype('float32')) # shape=(2, 4, 16)
uop_4297 = relay.sqrt(uop_4261.astype('float32')) # shape=(2, 4, 16)
func_2291_call = mod.get_global_var('func_2291')
func_2294_call = mutated_mod.get_global_var('func_2294')
call_4298 = func_2291_call(relay.reshape(call_4251.astype('float32'), [2, 4, 16]))
call_4299 = func_2291_call(relay.reshape(call_4251.astype('float32'), [2, 4, 16]))
func_2252_call = mod.get_global_var('func_2252')
func_2254_call = mutated_mod.get_global_var('func_2254')
call_4301 = func_2252_call()
call_4302 = func_2252_call()
bop_4309 = relay.left_shift(uop_4295.astype('uint64'), relay.reshape(uop_4259.astype('uint64'), relay.shape_of(uop_4295))) # shape=(2, 4, 16)
bop_4312 = relay.left_shift(uop_4297.astype('uint64'), relay.reshape(uop_4261.astype('uint64'), relay.shape_of(uop_4297))) # shape=(2, 4, 16)
uop_4315 = relay.exp(uop_4259.astype('float64')) # shape=(2, 4, 16)
uop_4317 = relay.exp(uop_4261.astype('float64')) # shape=(2, 4, 16)
func_3208_call = mod.get_global_var('func_3208')
func_3211_call = mutated_mod.get_global_var('func_3211')
var_4324 = relay.var("var_4324", dtype = "float32", shape = (260, 2))#candidate|4324|(260, 2)|var|float32
call_4323 = relay.TupleGetItem(func_3208_call(relay.reshape(var_4324.astype('float32'), [10, 13, 4])), 0)
call_4325 = relay.TupleGetItem(func_3211_call(relay.reshape(var_4324.astype('float32'), [10, 13, 4])), 0)
output = relay.Tuple([call_4275,const_4276,const_4277,call_4298,call_4301,bop_4309,uop_4315,call_4323,var_4324,])
output2 = relay.Tuple([call_4278,const_4276,const_4277,call_4299,call_4302,bop_4312,uop_4317,call_4325,var_4324,])
func_4326 = relay.Function([var_4324,], output)
mod['func_4326'] = func_4326
mod = relay.transform.InferType()(mod)
var_4327 = relay.var("var_4327", dtype = "float32", shape = (260, 2))#candidate|4327|(260, 2)|var|float32
output = func_4326(var_4327)
func_4328 = relay.Function([var_4327], output)
mutated_mod['func_4328'] = func_4328
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4344 = relay.var("var_4344", dtype = "float64", shape = (3, 11, 3))#candidate|4344|(3, 11, 3)|var|float64
const_4345 = relay.const([[[-8.084781,-8.838898,-5.806128],[-4.637226,-6.988654,0.801250],[1.271553,-9.537716,-5.267141],[-5.115421,-3.729909,0.854183],[7.924282,-3.296773,-4.430197],[-7.184342,4.808487,6.923934],[8.918771,-4.377513,3.209284],[4.355306,-7.232098,9.845749],[6.661105,9.677896,-5.318704],[3.769528,6.684502,-8.161827],[1.714121,5.923237,-4.609296]],[[-9.393401,-5.542064,9.873273],[0.255526,-8.452439,-3.999075],[-5.893313,1.047907,-0.629448],[-2.984387,2.541950,8.732470],[7.714235,-0.152126,3.330685],[-5.699758,3.681081,9.909372],[-0.489251,3.233694,-8.347237],[9.929775,2.483819,-3.188192],[-7.436249,8.978584,2.824480],[8.864442,-8.335451,8.096335],[-7.180290,7.186304,-7.716949]],[[-7.517852,7.605067,1.508577],[-4.366537,-6.350488,2.949489],[4.245562,8.870478,5.572173],[6.435240,-7.867720,4.280726],[-2.709497,6.116105,2.555926],[-6.866013,-1.629256,4.323436],[9.254995,-6.519326,1.166901],[-5.874225,3.742181,5.854385],[-0.159189,-7.102425,-7.497043],[-6.222599,1.162258,3.668612],[1.514299,5.426621,9.801827]]], dtype = "float64")#candidate|4345|(3, 11, 3)|const|float64
bop_4346 = relay.divide(var_4344.astype('float64'), relay.reshape(const_4345.astype('float64'), relay.shape_of(var_4344))) # shape=(3, 11, 3)
uop_4352 = relay.sinh(const_4345.astype('float32')) # shape=(3, 11, 3)
bop_4361 = relay.equal(bop_4346.astype('bool'), relay.reshape(uop_4352.astype('bool'), relay.shape_of(bop_4346))) # shape=(3, 11, 3)
uop_4366 = relay.tan(var_4344.astype('float32')) # shape=(3, 11, 3)
output = relay.Tuple([bop_4361,uop_4366,])
output2 = relay.Tuple([bop_4361,uop_4366,])
func_4368 = relay.Function([var_4344,], output)
mod['func_4368'] = func_4368
mod = relay.transform.InferType()(mod)
var_4369 = relay.var("var_4369", dtype = "float64", shape = (3, 11, 3))#candidate|4369|(3, 11, 3)|var|float64
output = func_4368(var_4369)
func_4370 = relay.Function([var_4369], output)
mutated_mod['func_4370'] = func_4370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1968_call = mod.get_global_var('func_1968')
func_1970_call = mutated_mod.get_global_var('func_1970')
call_4413 = relay.TupleGetItem(func_1968_call(), 1)
call_4414 = relay.TupleGetItem(func_1970_call(), 1)
var_4415 = relay.var("var_4415", dtype = "float32", shape = (2, 4, 16))#candidate|4415|(2, 4, 16)|var|float32
bop_4416 = relay.logical_and(call_4413.astype('bool'), relay.reshape(var_4415.astype('bool'), relay.shape_of(call_4413))) # shape=(2, 4, 16)
bop_4419 = relay.logical_and(call_4414.astype('bool'), relay.reshape(var_4415.astype('bool'), relay.shape_of(call_4414))) # shape=(2, 4, 16)
func_2749_call = mod.get_global_var('func_2749')
func_2752_call = mutated_mod.get_global_var('func_2752')
var_4431 = relay.var("var_4431", dtype = "float32", shape = (416,))#candidate|4431|(416,)|var|float32
call_4430 = relay.TupleGetItem(func_2749_call(relay.reshape(var_4431.astype('float32'), [4, 8, 13]), relay.reshape(var_4415.astype('float32'), [128,]), ), 1)
call_4432 = relay.TupleGetItem(func_2752_call(relay.reshape(var_4431.astype('float32'), [4, 8, 13]), relay.reshape(var_4415.astype('float32'), [128,]), ), 1)
bop_4450 = relay.power(call_4430.astype('float32'), relay.reshape(var_4415.astype('float32'), relay.shape_of(call_4430))) # shape=(2, 4, 16)
bop_4453 = relay.power(call_4432.astype('float32'), relay.reshape(var_4415.astype('float32'), relay.shape_of(call_4432))) # shape=(2, 4, 16)
output = relay.Tuple([bop_4416,var_4431,bop_4450,])
output2 = relay.Tuple([bop_4419,var_4431,bop_4453,])
func_4456 = relay.Function([var_4415,var_4431,], output)
mod['func_4456'] = func_4456
mod = relay.transform.InferType()(mod)
mutated_mod['func_4456'] = func_4456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4456_call = mutated_mod.get_global_var('func_4456')
var_4458 = relay.var("var_4458", dtype = "float32", shape = (2, 4, 16))#candidate|4458|(2, 4, 16)|var|float32
var_4459 = relay.var("var_4459", dtype = "float32", shape = (416,))#candidate|4459|(416,)|var|float32
call_4457 = func_4456_call(var_4458,var_4459,)
output = call_4457
func_4460 = relay.Function([var_4458,var_4459,], output)
mutated_mod['func_4460'] = func_4460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2775_call = mod.get_global_var('func_2775')
func_2776_call = mutated_mod.get_global_var('func_2776')
call_4475 = relay.TupleGetItem(func_2775_call(), 0)
call_4476 = relay.TupleGetItem(func_2776_call(), 0)
output = relay.Tuple([call_4475,])
output2 = relay.Tuple([call_4476,])
func_4482 = relay.Function([], output)
mod['func_4482'] = func_4482
mod = relay.transform.InferType()(mod)
output = func_4482()
func_4483 = relay.Function([], output)
mutated_mod['func_4483'] = func_4483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2240_call = mod.get_global_var('func_2240')
func_2242_call = mutated_mod.get_global_var('func_2242')
call_4558 = relay.TupleGetItem(func_2240_call(), 2)
call_4559 = relay.TupleGetItem(func_2242_call(), 2)
func_4368_call = mod.get_global_var('func_4368')
func_4370_call = mutated_mod.get_global_var('func_4370')
const_4615 = relay.const([3.598310,3.136350,-9.447255,-3.297989,-5.340178,5.654225,-0.023492,3.724030,2.805416,-9.611586,-6.091963,2.616276,-6.716772,-8.253485,0.281842,-9.550300,-4.059455,-3.544906,4.653515,-8.466171,4.385128,-3.556445,-7.193423,5.545084,6.127010,-9.644161,-9.282761,-8.812533,-3.746371,-5.043247,4.526350,-3.771660,9.654113,-4.881326,4.017587,-3.767114,4.626288,-9.528246,1.978032,8.049029,9.518323,-7.003706,-0.229177,-8.017853,3.608517,-1.523434,-1.857978,-8.493555,0.307389,-7.325331,-6.146644,3.357489,8.412998,4.172603,1.759477,5.223714,-9.886900,5.379007,5.096082,3.334146,-6.070233,8.913774,-2.088680,-1.169873,-6.134229,-1.992611,-7.845297,-3.004455,6.921343,-4.019272,9.039219,7.344411,4.538114,-6.782566,-6.590043,-8.456353,0.933574,9.614905,6.434672,0.187691,-4.181157,-9.929956,-9.754298,-9.384203,-8.195504,-5.422606,9.731791,2.408264,-5.218760,7.336331,8.546172,-0.722863,0.510316,-5.325064,2.811133,-8.660778,7.277998,-0.753116,-6.420710], dtype = "float64")#candidate|4615|(99,)|const|float64
call_4614 = relay.TupleGetItem(func_4368_call(relay.reshape(const_4615.astype('float64'), [3, 11, 3])), 0)
call_4616 = relay.TupleGetItem(func_4370_call(relay.reshape(const_4615.astype('float64'), [3, 11, 3])), 0)
func_4225_call = mod.get_global_var('func_4225')
func_4228_call = mutated_mod.get_global_var('func_4228')
const_4636 = relay.const([-3.422708,-7.694489,2.111427,8.818546,-4.506407,7.879296,3.438182,-2.489296,-2.096925,-4.121950,-0.424403,-4.379502,6.755410,9.620433,-2.623560,2.129913,-2.577555,-3.522370,-1.861494,8.570021,-1.585041,6.374114,-2.883309,-9.244656,-7.277476,-7.937935,1.806540,7.527468,6.000571,-5.944439,2.440548,-9.838023,9.223189,2.006775,-6.497583,-6.435748,6.089156,-4.136365,8.728911,-2.805060,2.744238,-3.754408,-9.222426,7.337622,-0.098299,6.766203,-5.535149,8.109052,-9.014833,1.321401,0.980809,-3.176244,-6.990182,-0.547759,4.496237,4.654993,4.181072,4.945874,2.360429,2.339454,-4.699137,0.871441,-2.776474,-6.742908,-6.481385,2.880194,8.729667,-7.887376,-0.188280,0.824900,-2.982057,7.860210,-3.055539,3.833802,3.503847,-3.165893,0.204441,-6.814676,-3.212602,-8.403699,1.444702,2.235320,6.149408,-3.817907,-7.858838,5.600473,-0.689992,2.540536,-4.401166,8.910829,7.935147,5.131453,1.087174,4.720568,7.573288,-4.164736,0.570398,9.008365,-3.072433,0.774135,-7.434404,8.933811,5.297697,9.825802,7.265646,2.006078,-2.559024,5.662532,3.954513,-9.476038,-3.249364,9.331326,-2.775442,6.828516,-9.980044,1.492669,6.826791,6.104331,4.942147,-2.355101,2.407452,-0.678612,4.210381,-1.290786,-8.511842,1.727822,1.540430,-8.568235,4.576311,-0.814320,-0.144151,-1.170169,-7.973242,-0.658322,4.696754,-8.048307,5.328680,-2.964293,-2.223948,5.798017,8.668217,-6.464845,3.039140,-1.781361,-0.191489,-7.060068,7.213835,-9.192212,-8.264306,1.765586,-7.600558,8.476203,-5.986833,-0.800069,-0.303501,2.566532,-1.411630,-8.334882,0.099842,-6.995901,-7.795657,-9.726043,-3.442821,6.521588,-7.437888,-7.304623,3.683121,-7.040173,4.288331,-5.558724,-6.188416,-5.009895,4.545955,-1.036223,9.313166,-9.131429,6.856476,8.880010,-4.802387,-8.137066,-2.400574,3.262647,-5.089269,4.607576,-3.232298,3.898233,-2.452409,2.509119,3.189905,-6.642558,-2.951689,-3.148752,1.031083,8.659051,-3.297753,-7.910364,-0.139510,-5.135792,2.402124,0.218051,-4.288438,-8.146530,-3.014349,-2.390532,5.877249,-4.310834,-1.800217,1.756735,7.296009,5.696911,9.935651,-0.347617,7.994351,-1.895146,-6.672166,-5.964067,1.060030,5.562783,-2.749402,9.113255,-3.485043,2.777690,-4.426657,8.804225,-9.156365,8.918840,-3.840994,5.614538,6.933865,2.239390,3.960058,-3.321593,-3.019425,-9.947098,2.442001,4.165109,-8.394371,-7.030060,1.674308,-9.371567,-2.027170,1.777282,3.850433,-9.262880,9.953126,-2.035638,2.856668,9.360351,4.181181,-0.179003,2.330558,-1.971646,2.190675,-5.604374,-5.766198,-0.590407,-1.816288,-4.128858,-4.120743,-5.242508,-4.227737,6.796460,1.870371,1.948352,-7.078415,-8.727876,6.753437,9.762175,8.481846,-4.775281,-6.633973,4.235303,-8.581585,-2.504014,-7.042936,-5.268603,-8.874159,5.866116,-3.406504,-2.548949,-7.108967,-5.150185,4.927502,-9.364327,6.631378,6.609422,5.017456,7.699567,-5.007348,9.171439,-7.092267,1.084217,5.905639,8.652629,3.030360,-3.616023,-6.196513,-0.897304,0.419614,-3.781502,6.510761,-5.876417,-3.005614,-1.287760,-2.237275,-7.430877,-6.781591,6.611749,-8.126846,0.507497,-1.926146,7.516204,1.491680,-1.441528,5.825394,9.159732,-7.745174,4.752785,1.665667,3.787745,4.472492,7.115581,2.891604,9.548799,0.285442,-8.441002,7.315511,-7.616518,4.432204,0.410185,6.855587,7.576359,-2.587726,7.117958,-9.381470,4.121552,-4.889845,8.070046,5.449423,6.027955,-4.588567,-9.889659,3.634458,-8.832511,-4.067408,9.959384,-7.857504,0.575966,-4.780950,8.702552,-2.485711,-1.781850,1.951318,-6.662015,2.613059,9.822602,9.830610,2.969431,-1.086591,8.232470,0.180241,-1.688694,1.417525,-2.174227,-3.534945,6.312204,2.372469,0.490995,7.675316,0.019813,0.178900,-8.490240,1.554704,-7.288708,4.975493,-6.573524,-3.465888,2.118210,-7.234760,0.764794,1.518825,8.085045,5.586720,8.667451,4.216976,2.948507,6.730439,1.067064,5.098241,-4.381216,-7.602699,4.437374,8.265002,-4.360697,-1.861116,3.010704,-4.973078,-5.444261,1.804033,9.067263,1.782020,-6.492353,-6.528390,4.246720,3.379742,8.670905,-3.226161,-0.605760,2.256569,6.798855,9.002070,9.670834,-9.881860,3.684830,3.764922,-5.935814,0.463877,0.703324,-1.624402,2.715171,-9.974811,4.349560,9.306187,-1.234868,8.634088,-4.921622,-8.757190,-4.750960,-3.661063,4.316058,-1.050183,-0.058840,-8.627554,-9.895169,-5.966546,-5.513418,-5.969077,5.792697,5.367199,-6.065397,2.357610,1.830093,-2.093371,-5.114526,1.967221,-5.346302,4.852032,3.722685,-0.722011,5.243804,8.692812,1.129842,2.694504,8.317593,-8.420898,0.244891,6.821501,-0.518047,6.203509,-6.371083,-7.163787,-1.737645,1.228201,2.854449,8.851318,-1.154423,-3.745461,-4.832392,-0.408496,-4.941135,8.679321,-5.817052,2.956819,-1.921203,-0.967289,1.584740,6.748250,-1.033870,-3.791949,-3.995988,-8.616636,-0.103236,-0.172997,3.239398,4.374538,-9.301164,7.493673,6.462758,9.156310,3.417365,-8.400956,-1.572954,9.393774,-4.538492,-0.918150,3.042728,7.250186,8.398361,1.635747,-3.403886,-6.603366,1.939360,9.325427,-8.000424,4.735387,-7.599283,5.119810,0.670565,-9.296109,-8.480243,6.636038,2.450410,3.296462,-5.902858,8.931947,6.624674,5.151908,-2.629778,8.681822,4.531776,-9.546604,-2.485291,-9.447451,-5.715629,8.435325,9.310250,7.160184,1.972100,6.206878,8.462926,-7.656380,1.905953,9.332629,4.771456,-9.736657,5.970251,-7.511568,-5.960047,-6.184473,9.147981,9.897895,-4.367111,-8.776893,-7.034707,3.527724,-2.076555,-2.373824,-0.468218,6.015064,9.985850,-0.559954,1.799477,-2.931068,-5.591820,-7.049818,8.800300,-2.224843,-6.675080,7.731116,7.640730,-1.628740,6.895209,6.029767,6.298362,1.820664,-6.894041,3.216734,-7.143570,-7.514482,-7.886934,2.841436,-0.615056,0.745761,-9.904240,7.701189,-1.310154,4.923172,2.482498,4.977382,-9.762813,4.073648,-7.344567,-4.497525,-8.949951,3.067988,9.836605,-4.837722,8.019469,8.590976,9.635579,4.501057,-7.274412,1.450285,5.767178,-9.714356,1.106035,-1.474978,1.352635,-8.578633,4.122787,-9.669332,-4.389145,3.116737,4.119896,3.068932,9.510036,-3.456143,-3.879613,9.699898,-3.276436,0.029342,6.933784,8.546116,-6.649724,2.555133,-4.772578,-6.142691,-1.425228,-3.584839,-9.329685,-7.118682,-1.266982,-4.358881,-2.247247,-3.401779,5.693864,-2.215898,4.103914,8.622802,-1.551398,-7.279862,7.711859,6.103218,-2.505215,8.095095,-5.275413,-0.576474,-1.624395,8.143915,5.275735,7.963077,4.857178,3.427707,1.360743,-4.761423,4.948221,-1.256618,4.511907,0.421164,9.083099,0.501116,-8.523143,-4.744895,-6.563072,-9.177537,1.041892,-1.012584,7.113626,-3.932971,5.513643,-6.754876,3.150858,2.143425,2.684194,-3.812016,9.234025,-8.495233,4.014039,-8.219806,-2.161590,7.466708,-6.462507,-2.445554,-9.658375,-8.916174,5.435723,-4.090463,-6.141442,8.062099,-5.023249,-7.040254,9.180584,-6.360781,-5.082698,-2.938106,7.613234,-8.434392,-6.043514,4.608048,8.445865,-7.439417,1.217812,0.421556,-6.979487,8.217579,-6.435541,-8.693667,-2.733483,4.008813,5.172439,7.261106,6.537464,-2.751383,-2.935163,-3.213354,0.543208,-9.428631,-2.134183,-3.139934,-7.863237,0.154423,-3.127497,4.689475,-5.842039,8.123829,-6.110358,-9.730809,-9.411657,0.969514,7.878273,7.251355,-9.124627,9.770696,9.660914,6.572103,7.353935,0.266120,-9.188831,-9.517532,2.744579,-3.058470,-4.474533,8.466335,9.060300,5.363991,9.802120,-6.613156,-3.836042,-0.011012,0.058806,0.730087,-8.573357,-1.977333,7.757729,-3.281646,-7.812705,5.571196,2.770154,-8.170647,4.334097,5.850112,-9.569648,9.148440,3.250620,-4.125730,3.919516,2.783487,-0.668707,2.262254,-2.614866,-0.348773,-3.710048,2.283098,1.463308,0.643375,2.980914,0.963369,-9.137301,-1.390022,-8.869259,-4.428382,7.464332,3.394098,-1.962311,2.870689,-9.272521,4.826388,6.098565,7.032977,-9.531050,-9.413385,1.808244,6.557932,-3.892060,-5.975051,5.785104,-5.963627,-2.103416,-6.761901,-8.483170,-0.269922,-2.149734,-4.135604,-9.485153,-7.766862,-6.246152,2.666739,-6.762408,9.284358,-5.988515,4.883049,-6.541032,-7.244102,9.088687,9.454318,6.144790,2.511564,-3.515290,7.872821,0.790468,5.339243,-2.995753,3.469926,-3.005896,6.854277,-1.003207,-0.260974,3.030211,-3.088710,0.951338,-2.471012,1.647591,-3.138414,1.948556,-4.818075,0.473040,-8.827066,-5.382585,-7.277110,-1.964832,-6.751007,-6.637010], dtype = "float32")#candidate|4636|(832,)|const|float32
call_4635 = relay.TupleGetItem(func_4225_call(relay.reshape(const_4636.astype('float32'), [832,]), relay.reshape(const_4636.astype('float32'), [416, 2]), ), 3)
call_4637 = relay.TupleGetItem(func_4228_call(relay.reshape(const_4636.astype('float32'), [832,]), relay.reshape(const_4636.astype('float32'), [416, 2]), ), 3)
output = relay.Tuple([call_4558,call_4614,const_4615,call_4635,const_4636,])
output2 = relay.Tuple([call_4559,call_4616,const_4615,call_4637,const_4636,])
func_4645 = relay.Function([], output)
mod['func_4645'] = func_4645
mod = relay.transform.InferType()(mod)
output = func_4645()
func_4646 = relay.Function([], output)
mutated_mod['func_4646'] = func_4646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2775_call = mod.get_global_var('func_2775')
func_2776_call = mutated_mod.get_global_var('func_2776')
call_4656 = relay.TupleGetItem(func_2775_call(), 0)
call_4657 = relay.TupleGetItem(func_2776_call(), 0)
func_4124_call = mod.get_global_var('func_4124')
func_4128_call = mutated_mod.get_global_var('func_4128')
var_4704 = relay.var("var_4704", dtype = "uint64", shape = (1, 192))#candidate|4704|(1, 192)|var|uint64
call_4703 = relay.TupleGetItem(func_4124_call(relay.reshape(call_4656.astype('float32'), [128,]), relay.reshape(var_4704.astype('uint64'), [48, 4]), relay.reshape(var_4704.astype('uint64'), [48, 4]), ), 3)
call_4705 = relay.TupleGetItem(func_4128_call(relay.reshape(call_4656.astype('float32'), [128,]), relay.reshape(var_4704.astype('uint64'), [48, 4]), relay.reshape(var_4704.astype('uint64'), [48, 4]), ), 3)
var_4717 = relay.var("var_4717", dtype = "float32", shape = (2, 4, 16))#candidate|4717|(2, 4, 16)|var|float32
bop_4718 = relay.bitwise_and(call_4656.astype('int8'), relay.reshape(var_4717.astype('int8'), relay.shape_of(call_4656))) # shape=(2, 4, 16)
bop_4721 = relay.bitwise_and(call_4657.astype('int8'), relay.reshape(var_4717.astype('int8'), relay.shape_of(call_4657))) # shape=(2, 4, 16)
uop_4724 = relay.atan(var_4704.astype('float32')) # shape=(1, 192)
uop_4732 = relay.cosh(uop_4724.astype('float64')) # shape=(1, 192)
output = relay.Tuple([call_4703,bop_4718,uop_4732,])
output2 = relay.Tuple([call_4705,bop_4721,uop_4732,])
func_4747 = relay.Function([var_4704,var_4717,], output)
mod['func_4747'] = func_4747
mod = relay.transform.InferType()(mod)
var_4748 = relay.var("var_4748", dtype = "uint64", shape = (1, 192))#candidate|4748|(1, 192)|var|uint64
var_4749 = relay.var("var_4749", dtype = "float32", shape = (2, 4, 16))#candidate|4749|(2, 4, 16)|var|float32
output = func_4747(var_4748,var_4749,)
func_4750 = relay.Function([var_4748,var_4749,], output)
mutated_mod['func_4750'] = func_4750
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1642_call = mod.get_global_var('func_1642')
func_1643_call = mutated_mod.get_global_var('func_1643')
call_4826 = relay.TupleGetItem(func_1642_call(), 1)
call_4827 = relay.TupleGetItem(func_1643_call(), 1)
output = relay.Tuple([call_4826,])
output2 = relay.Tuple([call_4827,])
func_4839 = relay.Function([], output)
mod['func_4839'] = func_4839
mod = relay.transform.InferType()(mod)
output = func_4839()
func_4840 = relay.Function([], output)
mutated_mod['func_4840'] = func_4840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3410_call = mod.get_global_var('func_3410')
func_3411_call = mutated_mod.get_global_var('func_3411')
call_4856 = relay.TupleGetItem(func_3410_call(), 0)
call_4857 = relay.TupleGetItem(func_3411_call(), 0)
output = call_4856
output2 = call_4857
func_4879 = relay.Function([], output)
mod['func_4879'] = func_4879
mod = relay.transform.InferType()(mod)
output = func_4879()
func_4880 = relay.Function([], output)
mutated_mod['func_4880'] = func_4880
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1602_call = mod.get_global_var('func_1602')
func_1604_call = mutated_mod.get_global_var('func_1604')
call_4886 = func_1602_call()
call_4887 = func_1602_call()
uop_4899 = relay.exp(call_4886.astype('float64')) # shape=(3, 13, 5)
uop_4901 = relay.exp(call_4887.astype('float64')) # shape=(3, 13, 5)
func_1858_call = mod.get_global_var('func_1858')
func_1861_call = mutated_mod.get_global_var('func_1861')
const_4906 = relay.const([-8.626174,9.660481,-5.449943,9.902335,-3.937647,2.414682,0.192578,-1.066694,1.390850,4.008673,9.311338,5.201867,2.327860,-6.467493,-8.182728,0.985236,-9.015082,2.227288,7.228073,-0.712035,4.914506,-2.794951,-4.348639,1.507823,-6.100371,-7.876685,-8.649073,-6.675064,-7.196936,-0.373275,-2.180047,1.319727,-9.751729,-2.597034,2.377565,2.323713,-7.143895,-0.597598,-7.831138,2.781963,-6.687060,-6.881111,3.695155,-5.877242,2.303027,-9.700146,-8.430602,-7.490963,-5.569663,4.051495,6.030512,-4.510061,-6.280619,-1.164009,-6.347191,9.915454,6.086001,6.964068,4.317395,-4.921232,-1.387107,-3.888818,3.121277,2.065739,2.341015,7.830632,8.954078,3.085316,-8.115262,2.487239,8.212463,7.920548,-1.724392,9.829349,-8.509861,6.949449,-8.210110,-4.686073,-8.240369,2.840198,-0.534765,9.838958,-1.755909,1.888873,-1.241279,9.179580,-0.668200,1.817676,5.198135,-3.288534,-3.360423,-6.405572,2.764151,-8.724113,-0.259604,-2.905576,3.156332,-9.358827,-7.708859,-9.701726,-6.634395,-3.474927,4.649256,-8.581291,-1.942025,-6.330961,-3.984679,0.133208,3.783615,7.198172,5.611341,-8.750206,9.354616,-6.409831,6.701574,5.230385,-8.094302,-9.158165,6.859947,-0.825146,2.073655,-4.931691,3.052381,5.508076,-8.430056,-7.320745,-7.935337,-5.864802], dtype = "float64")#candidate|4906|(128,)|const|float64
call_4905 = relay.TupleGetItem(func_1858_call(relay.reshape(const_4906.astype('float64'), [128,])), 0)
call_4907 = relay.TupleGetItem(func_1861_call(relay.reshape(const_4906.astype('float64'), [128,])), 0)
func_3626_call = mod.get_global_var('func_3626')
func_3628_call = mutated_mod.get_global_var('func_3628')
call_4909 = relay.TupleGetItem(func_3626_call(relay.reshape(const_4906.astype('float32'), [2, 4, 16])), 6)
call_4910 = relay.TupleGetItem(func_3628_call(relay.reshape(const_4906.astype('float32'), [2, 4, 16])), 6)
output = relay.Tuple([uop_4899,call_4905,const_4906,call_4909,])
output2 = relay.Tuple([uop_4901,call_4907,const_4906,call_4910,])
func_4934 = relay.Function([], output)
mod['func_4934'] = func_4934
mod = relay.transform.InferType()(mod)
mutated_mod['func_4934'] = func_4934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4934_call = mutated_mod.get_global_var('func_4934')
call_4935 = func_4934_call()
output = call_4935
func_4936 = relay.Function([], output)
mutated_mod['func_4936'] = func_4936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4645_call = mod.get_global_var('func_4645')
func_4646_call = mutated_mod.get_global_var('func_4646')
call_5002 = relay.TupleGetItem(func_4645_call(), 2)
call_5003 = relay.TupleGetItem(func_4646_call(), 2)
output = call_5002
output2 = call_5003
func_5006 = relay.Function([], output)
mod['func_5006'] = func_5006
mod = relay.transform.InferType()(mod)
mutated_mod['func_5006'] = func_5006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5006_call = mutated_mod.get_global_var('func_5006')
call_5007 = func_5006_call()
output = call_5007
func_5008 = relay.Function([], output)
mutated_mod['func_5008'] = func_5008
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5015 = relay.var("var_5015", dtype = "float64", shape = (11, 1, 5))#candidate|5015|(11, 1, 5)|var|float64
uop_5016 = relay.acos(var_5015.astype('float64')) # shape=(11, 1, 5)
func_1534_call = mod.get_global_var('func_1534')
func_1536_call = mutated_mod.get_global_var('func_1536')
const_5019 = relay.const([6.002107,4.334178,4.684418,2.352830,-3.508685,1.030740,-0.505256,6.408303,-9.471816,-2.070309,-6.821749,-5.252380,-0.449254,-3.585309,-4.979122,-9.528880,-1.333587,0.505695,-3.692876,-7.072512,-9.538994,8.245162,7.789647,-5.614637,-3.254242,2.963181,-5.591467,8.877858,0.771649,-4.035135,5.572984,-5.318733,-3.176349,1.048270,-3.872351,9.709711,2.503186,-3.679496,-9.099903,-9.372522,8.786185,4.057682,3.590575,6.211422,-0.389806,0.329287,-4.505220,3.781094,8.251289,6.866118,0.393883,-6.940093,0.276173,1.050792,-8.803659,2.306189,7.771309,4.177185,9.023334,-5.001786,-2.500196,2.572491,4.434563,5.856319,7.672734,-7.003328,-3.466697,4.910751,6.199446,3.712042,-6.815807,-9.969088,4.620144,-8.781358,-7.714032,-1.744572,-9.887005,1.025754,5.869803,-2.434017,4.490668,1.554194,-7.496042,-8.959628,7.332510,9.677024,-5.774456,1.256173,5.710885,-5.186770,-2.371359,-9.557927,-9.625756,-9.595888,-4.463120,-7.770714,-3.915456,0.768523,-8.151526,-4.480698,7.382065,8.259234,2.697148,0.021860,-5.282553,-2.275863,2.408689,-1.582869,-6.520667,9.015159,9.892646,1.343685,1.187999,-0.119936,-5.784581,2.750702,-8.084490,3.648050,2.369928,-3.146674,-4.480347,7.848123,0.854390,1.871553,-1.832971,1.975010,-0.098787,4.947171], dtype = "float32")#candidate|5019|(128,)|const|float32
call_5018 = relay.TupleGetItem(func_1534_call(relay.reshape(const_5019.astype('float32'), [2, 4, 16])), 0)
call_5020 = relay.TupleGetItem(func_1536_call(relay.reshape(const_5019.astype('float32'), [2, 4, 16])), 0)
output = relay.Tuple([uop_5016,call_5018,const_5019,])
output2 = relay.Tuple([uop_5016,call_5020,const_5019,])
func_5038 = relay.Function([var_5015,], output)
mod['func_5038'] = func_5038
mod = relay.transform.InferType()(mod)
mutated_mod['func_5038'] = func_5038
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5039 = relay.var("var_5039", dtype = "float64", shape = (11, 1, 5))#candidate|5039|(11, 1, 5)|var|float64
func_5038_call = mutated_mod.get_global_var('func_5038')
call_5040 = func_5038_call(var_5039)
output = call_5040
func_5041 = relay.Function([var_5039], output)
mutated_mod['func_5041'] = func_5041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3410_call = mod.get_global_var('func_3410')
func_3411_call = mutated_mod.get_global_var('func_3411')
call_5051 = relay.TupleGetItem(func_3410_call(), 1)
call_5052 = relay.TupleGetItem(func_3411_call(), 1)
func_2291_call = mod.get_global_var('func_2291')
func_2294_call = mutated_mod.get_global_var('func_2294')
const_5063 = relay.const([2.878576,3.953851,2.872649,-1.924397,0.538758,0.544525,4.803763,-0.290673,7.029883,3.835801,-0.812039,4.392971,6.471216,-5.459673,4.760202,9.253755,-3.619791,-6.408198,-6.365412,9.823785,0.888129,-4.264433,-3.326440,-3.685341,5.608429,-7.449021,-0.298122,-6.863621,8.645512,-2.863700,-5.887015,7.189755,7.410330,-8.728405,-2.222109,3.592929,8.281402,-1.033460,8.049442,5.270895,-7.807113,-3.294182,8.619213,1.048732,2.117119,6.196957,9.810115,9.551480,-1.285761,-4.701515,8.086940,-1.409895,7.839530,-6.044158,-4.290678,-2.450188,2.732347,3.042565,6.501456,4.732214,7.490761,-4.126747,7.010244,9.658888,-1.641887,-7.160081,2.670300,-6.732005,-7.174140,5.616257,-8.229574,0.274971,-2.022397,-6.715890,7.377695,2.057598,-3.376535,1.909866,4.899208,-6.520484,4.932658,1.018484,3.217247,8.559905,-1.484055,-8.066997,-3.070470,-4.535601,7.684791,-5.140437,-7.096887,9.902876,-2.647749,-8.105226,1.593254,1.365924,6.526074,7.818689,-2.202575,-8.327896,-7.312868,4.151860,5.979049,5.547519,-1.893159,9.529965,8.450238,4.270509,-6.382926,7.385157,-8.732963,-0.122018,7.598025,8.540201,-1.442793,-4.974910,-6.344354,-8.565789,2.508156,-0.503150,2.373222,-9.169004,-8.461515,-3.389203,8.929365,-0.929350,-8.130180,-8.116783], dtype = "float32")#candidate|5063|(128,)|const|float32
call_5062 = func_2291_call(relay.reshape(const_5063.astype('float32'), [2, 4, 16]))
call_5064 = func_2291_call(relay.reshape(const_5063.astype('float32'), [2, 4, 16]))
output = relay.Tuple([call_5051,call_5062,const_5063,])
output2 = relay.Tuple([call_5052,call_5064,const_5063,])
func_5070 = relay.Function([], output)
mod['func_5070'] = func_5070
mod = relay.transform.InferType()(mod)
output = func_5070()
func_5071 = relay.Function([], output)
mutated_mod['func_5071'] = func_5071
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5072 = relay.var("var_5072", dtype = "float32", shape = (1, 3, 1))#candidate|5072|(1, 3, 1)|var|float32
const_5073 = relay.const([[[6.439220,-5.529373,7.455008,6.518382,-6.018309,-4.412799,-3.318271,0.658207,-2.537737,8.132103,-2.272486,-9.345040],[-7.124070,8.858556,-5.184309,-8.374861,8.587275,0.215305,5.407262,-8.163988,-8.017771,8.002588,-9.773069,-0.599678],[-8.280080,-0.323704,-4.041498,2.450327,-9.950636,0.610197,3.935824,-9.892340,6.742188,4.085551,6.091622,-0.644437]],[[-1.769817,-8.697267,-1.058501,9.676174,-5.933084,-2.628030,-6.519343,4.075016,-4.259771,5.677425,1.855018,-7.321967],[-7.152771,7.985928,2.026620,4.787457,-1.703481,-9.197592,-6.056739,6.353175,-5.234324,4.778892,6.061067,1.981497],[-8.082142,6.401638,5.134403,-5.366928,2.270790,8.379146,7.511827,-4.847888,-5.024214,-0.676738,-8.888254,-0.010016]],[[8.864494,-3.343971,-2.535167,-2.791730,-0.433663,-3.008189,1.938847,2.226114,8.945828,-6.829824,-1.916757,-3.673536],[8.972310,0.203704,-4.282735,-6.775032,-7.338928,-5.985943,9.355660,2.621598,-7.474273,4.630647,-8.470007,-6.298000],[9.888253,-9.942534,9.651462,-5.314660,5.834391,-6.532649,6.709372,-9.472371,3.653822,4.200508,1.158851,9.395100]],[[-2.536490,-8.696737,1.168769,-3.921434,6.955320,-0.633462,5.522918,1.625535,4.092033,-6.581854,1.025413,-9.278964],[2.580152,0.264590,-2.687478,-6.296035,6.001539,7.966667,0.382101,8.011696,-0.411633,2.289226,-1.249968,-1.962837],[8.104906,0.634893,0.454847,8.747259,9.690847,-2.768955,0.277175,-2.472944,3.720366,-9.976689,-7.627308,5.462626]],[[7.765089,-5.555372,5.963406,5.832463,-8.386573,4.622264,-0.186445,-8.226002,3.310374,0.848260,-7.328763,4.974463],[0.066859,-5.909854,8.205368,-4.455797,0.701341,5.965415,-6.836699,7.338052,1.024801,-8.658963,8.889885,0.673706],[6.152800,-8.457276,-1.102094,4.119047,4.804133,7.035890,2.457252,3.282270,5.065438,-0.847776,-4.041051,-5.318443]],[[-7.008228,5.564405,8.309820,2.074251,-5.111687,-4.004006,0.887799,-6.110650,-1.574719,-1.315809,-0.483768,-7.793237],[-6.505388,6.026218,-5.908379,-5.828336,-6.502042,-7.878328,-8.880662,1.277889,5.780216,8.455231,2.398847,3.073575],[-8.675262,-7.750962,-8.735189,-3.009604,5.886251,8.368878,3.450659,-1.313690,7.807672,0.216824,-8.276643,-7.159528]],[[8.190903,3.311553,-8.424828,-0.252320,-1.750000,5.453105,1.903574,9.294320,9.962982,-5.080067,-9.768836,-4.173326],[4.817507,1.877696,-9.570608,-5.179390,8.453626,5.829989,-9.829030,-9.166529,-7.220685,6.997567,7.451770,-0.087024],[9.921147,3.571875,7.061396,-5.501813,-6.476674,2.134236,2.586591,-3.349678,4.154958,-0.378992,7.767447,-4.783783]],[[-3.520020,4.882461,-4.129038,-1.510411,-6.848943,0.588374,-7.429310,-6.846516,3.265760,2.234898,7.456146,5.101940],[7.461479,5.597669,5.746016,-4.362999,6.240722,0.810543,9.551557,-9.923851,-8.114459,-5.531201,0.785096,3.947089],[-4.819983,0.047540,-2.399709,-5.051362,8.686216,-0.274978,0.420106,-1.464594,-4.072283,-7.102771,-7.529460,5.646796]],[[-6.677981,1.911033,-6.300849,-7.077508,6.896765,9.445252,-6.159844,-6.273024,0.514427,-4.752732,2.872396,3.178150],[3.868543,-0.382606,-8.762158,-1.340193,8.556822,-5.229462,-0.803608,-4.599586,4.782801,9.037566,9.965188,0.385922],[-9.291053,8.173559,-8.014507,9.330385,-9.536500,0.359567,4.505877,3.822821,3.900674,-1.681671,-7.514087,-7.233323]]], dtype = "float32")#candidate|5073|(9, 3, 12)|const|float32
bop_5074 = relay.floor_divide(var_5072.astype('float32'), const_5073.astype('float32')) # shape=(9, 3, 12)
output = relay.Tuple([bop_5074,])
output2 = relay.Tuple([bop_5074,])
func_5083 = relay.Function([var_5072,], output)
mod['func_5083'] = func_5083
mod = relay.transform.InferType()(mod)
var_5084 = relay.var("var_5084", dtype = "float32", shape = (1, 3, 1))#candidate|5084|(1, 3, 1)|var|float32
output = func_5083(var_5084)
func_5085 = relay.Function([var_5084], output)
mutated_mod['func_5085'] = func_5085
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5136 = relay.var("var_5136", dtype = "float64", shape = (2, 13, 9))#candidate|5136|(2, 13, 9)|var|float64
uop_5137 = relay.rsqrt(var_5136.astype('float64')) # shape=(2, 13, 9)
var_5143 = relay.var("var_5143", dtype = "float64", shape = (2, 13, 9))#candidate|5143|(2, 13, 9)|var|float64
bop_5144 = relay.minimum(uop_5137.astype('uint8'), relay.reshape(var_5143.astype('uint8'), relay.shape_of(uop_5137))) # shape=(2, 13, 9)
uop_5154 = relay.sqrt(var_5143.astype('float64')) # shape=(2, 13, 9)
func_2775_call = mod.get_global_var('func_2775')
func_2776_call = mutated_mod.get_global_var('func_2776')
call_5164 = relay.TupleGetItem(func_2775_call(), 0)
call_5165 = relay.TupleGetItem(func_2776_call(), 0)
func_1239_call = mod.get_global_var('func_1239')
func_1243_call = mutated_mod.get_global_var('func_1243')
var_5167 = relay.var("var_5167", dtype = "bool", shape = (3328,))#candidate|5167|(3328,)|var|bool
var_5168 = relay.var("var_5168", dtype = "uint64", shape = (12,))#candidate|5168|(12,)|var|uint64
call_5166 = relay.TupleGetItem(func_1239_call(relay.reshape(var_5167.astype('bool'), [16, 13, 16]), relay.reshape(var_5168.astype('uint64'), [12,]), ), 4)
call_5169 = relay.TupleGetItem(func_1243_call(relay.reshape(var_5167.astype('bool'), [16, 13, 16]), relay.reshape(var_5168.astype('uint64'), [12,]), ), 4)
uop_5179 = relay.cosh(var_5167.astype('float64')) # shape=(3328,)
bop_5191 = relay.mod(var_5143.astype('float64'), relay.reshape(uop_5137.astype('float64'), relay.shape_of(var_5143))) # shape=(2, 13, 9)
output = relay.Tuple([bop_5144,uop_5154,call_5164,call_5166,var_5168,uop_5179,bop_5191,])
output2 = relay.Tuple([bop_5144,uop_5154,call_5165,call_5169,var_5168,uop_5179,bop_5191,])
func_5209 = relay.Function([var_5136,var_5143,var_5167,var_5168,], output)
mod['func_5209'] = func_5209
mod = relay.transform.InferType()(mod)
var_5210 = relay.var("var_5210", dtype = "float64", shape = (2, 13, 9))#candidate|5210|(2, 13, 9)|var|float64
var_5211 = relay.var("var_5211", dtype = "float64", shape = (2, 13, 9))#candidate|5211|(2, 13, 9)|var|float64
var_5212 = relay.var("var_5212", dtype = "bool", shape = (3328,))#candidate|5212|(3328,)|var|bool
var_5213 = relay.var("var_5213", dtype = "uint64", shape = (12,))#candidate|5213|(12,)|var|uint64
output = func_5209(var_5210,var_5211,var_5212,var_5213,)
func_5214 = relay.Function([var_5210,var_5211,var_5212,var_5213,], output)
mutated_mod['func_5214'] = func_5214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5070_call = mod.get_global_var('func_5070')
func_5071_call = mutated_mod.get_global_var('func_5071')
call_5250 = relay.TupleGetItem(func_5070_call(), 1)
call_5251 = relay.TupleGetItem(func_5071_call(), 1)
func_1496_call = mod.get_global_var('func_1496')
func_1500_call = mutated_mod.get_global_var('func_1500')
var_5254 = relay.var("var_5254", dtype = "bool", shape = ())#candidate|5254|()|var|bool
const_5255 = relay.const([True,True,True,True,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,True,False,False,True,True,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,True,False,True,True,False,False,True,True,True,False,True,False,True,True,False,False,True,False,True,False,False,False,False,True,False,False,False,True,False,True,True,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,False,True,False,True,False,False,False,False,True,False,False,False,True,True,True,False,False,True,False,True,True,True,False,True,False,True,False,False,True,False,False,True,True,False,True,True,False,True,False,True,True,False,True,False,True,True,False,False,False,False,True,False,True,True,True,False,False,True,False,True,True,False,True,False,False,False,False,False,True,False,True,False,False,True,False,False,False,False,False,False,False,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,False,False,True,False,True,True,False,False,True,False,False,True,False,True,True,False,True,True,True,True,True,False,True,True,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,False,False,False,True,False,True,True,False,False,False,True,True,False,False,True,True,True,False,True,True,True,False,False,False,False,True,True,True,False,False,False,True,False,False,False,True,True,True,True,False,False,True,True,False,True,False,True,False,False,False,True,True,True,False,True,True,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,False,False,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,True,True,True,False,False,True,False,False,True,True,True,False,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False,True,True,True,False,False,True,True,True,True,False,False,False,True,False,True,False,False,False,True,True,True,False,True,True,True,False,True,False,True,True,False,True,False,False,True,False,True,False,True,False,False,False,False,True,False,True,True,False,True,False,True,False,False,True,True,False,True,True,False,False,False,True,True,False,True,False,True,False,False,False,False,False,False,True,False,False,False,True,False,False,False,False,False,False,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,True,True,False,True,False,True,True,False,True,True,False,True,True,True,True,False,True,False,True,False,True,True,False,True,False,False,True,True,True,False,False,True,False,True,False,False,False,True,False,True,False,True,False,False,False,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,True,True,True,True,False,True,True,False,True,True,True,True,False,False,True,True,False,True,True,False,False,True,False,False,True,True,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,False,True,True,False,False,True,True,True,False,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,True,False,False,True,True,False,False,False,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,False,False,True,False,True,True,False,False,False,True,False,True,False,False,True,False,False,True,False,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,False,True,True,False,True,True,True,True,False,False,False,True,False,False,True,True,True,False,True,True,False,False,False,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,True,False,False,True,True,True,False,False,False,False,True,False,False,True,False,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,False,False,True,False,False,True,False,False,False], dtype = "bool")#candidate|5255|(756,)|const|bool
call_5253 = func_1496_call(relay.reshape(var_5254.astype('bool'), []), relay.reshape(const_5255.astype('bool'), [12, 9, 7]), )
call_5256 = func_1496_call(relay.reshape(var_5254.astype('bool'), []), relay.reshape(const_5255.astype('bool'), [12, 9, 7]), )
output = relay.Tuple([call_5250,call_5253,var_5254,const_5255,])
output2 = relay.Tuple([call_5251,call_5256,var_5254,const_5255,])
func_5265 = relay.Function([var_5254,], output)
mod['func_5265'] = func_5265
mod = relay.transform.InferType()(mod)
var_5266 = relay.var("var_5266", dtype = "bool", shape = ())#candidate|5266|()|var|bool
output = func_5265(var_5266)
func_5267 = relay.Function([var_5266], output)
mutated_mod['func_5267'] = func_5267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2252_call = mod.get_global_var('func_2252')
func_2254_call = mutated_mod.get_global_var('func_2254')
call_5298 = func_2252_call()
call_5299 = func_2252_call()
output = relay.Tuple([call_5298,])
output2 = relay.Tuple([call_5299,])
func_5310 = relay.Function([], output)
mod['func_5310'] = func_5310
mod = relay.transform.InferType()(mod)
mutated_mod['func_5310'] = func_5310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5310_call = mutated_mod.get_global_var('func_5310')
call_5311 = func_5310_call()
output = call_5311
func_5312 = relay.Function([], output)
mutated_mod['func_5312'] = func_5312
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1968_call = mod.get_global_var('func_1968')
func_1970_call = mutated_mod.get_global_var('func_1970')
call_5326 = relay.TupleGetItem(func_1968_call(), 0)
call_5327 = relay.TupleGetItem(func_1970_call(), 0)
output = call_5326
output2 = call_5327
func_5328 = relay.Function([], output)
mod['func_5328'] = func_5328
mod = relay.transform.InferType()(mod)
output = func_5328()
func_5329 = relay.Function([], output)
mutated_mod['func_5329'] = func_5329
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5333 = relay.const([[2,9,2,-1],[6,1,-9,-2],[-1,-5,3,-6],[7,7,-6,10],[-10,-4,-2,3],[10,-9,8,-7],[-4,-8,10,-1],[8,7,-1,-9],[-5,-3,1,-6],[-10,8,-6,9],[-1,-6,-10,10],[-7,1,-1,8],[5,-4,7,-7],[-8,-7,2,-2],[-4,6,7,2]], dtype = "uint64")#candidate|5333|(15, 4)|const|uint64
var_5334 = relay.var("var_5334", dtype = "uint64", shape = (15, 4))#candidate|5334|(15, 4)|var|uint64
bop_5335 = relay.minimum(const_5333.astype('uint64'), relay.reshape(var_5334.astype('uint64'), relay.shape_of(const_5333))) # shape=(15, 4)
output = relay.Tuple([bop_5335,])
output2 = relay.Tuple([bop_5335,])
func_5342 = relay.Function([var_5334,], output)
mod['func_5342'] = func_5342
mod = relay.transform.InferType()(mod)
mutated_mod['func_5342'] = func_5342
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5343 = relay.var("var_5343", dtype = "uint64", shape = (15, 4))#candidate|5343|(15, 4)|var|uint64
func_5342_call = mutated_mod.get_global_var('func_5342')
call_5344 = func_5342_call(var_5343)
output = call_5344
func_5345 = relay.Function([var_5343], output)
mutated_mod['func_5345'] = func_5345
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5366 = relay.var("var_5366", dtype = "int64", shape = (1, 14, 2))#candidate|5366|(1, 14, 2)|var|int64
const_5367 = relay.const([[[-4,-1],[6,-6],[-6,-10],[3,6],[7,6],[3,5],[-7,-8],[1,-5],[4,-7],[-5,3],[1,10],[9,5],[6,-9],[-3,6]],[[7,3],[3,2],[-5,8],[-1,3],[6,-6],[-9,-10],[4,3],[-4,-7],[4,10],[9,7],[-2,-4],[-5,6],[2,6],[-3,-6]],[[8,6],[10,-4],[5,-4],[-7,-8],[5,3],[-1,-1],[9,6],[-4,2],[-4,5],[-2,-10],[4,-1],[6,-1],[3,1],[2,-9]],[[-7,-4],[-7,-4],[-5,-7],[-9,-5],[-3,-5],[8,-10],[-9,5],[10,2],[-8,2],[-5,10],[-7,-8],[-6,-9],[-1,-9],[-8,10]],[[-7,9],[-10,9],[-9,7],[7,-3],[-4,1],[6,-10],[2,-8],[8,10],[-4,7],[1,-3],[-4,2],[8,8],[-6,4],[6,-9]],[[-5,1],[-6,1],[3,5],[1,-4],[-10,10],[2,2],[4,-10],[-1,-1],[7,-8],[-4,-4],[-6,-10],[-6,-3],[1,-4],[9,10]],[[1,-6],[-10,-7],[-10,9],[-5,-10],[1,9],[4,-4],[5,-7],[4,-10],[9,7],[2,6],[10,-5],[-8,7],[6,-9],[-8,-9]],[[-2,9],[-6,-1],[6,4],[-4,9],[6,1],[10,-5],[6,1],[6,-8],[6,4],[-6,-7],[-5,-10],[9,-4],[-3,1],[5,-2]],[[-10,4],[2,-2],[-9,8],[-1,10],[6,-6],[-9,-2],[-7,8],[8,2],[2,2],[10,-10],[-10,4],[5,-7],[4,-8],[4,-7]],[[-2,3],[-2,8],[3,-6],[5,1],[6,7],[1,-4],[9,-10],[-1,-4],[-10,3],[-3,6],[2,-10],[9,4],[-9,9],[-5,5]],[[-5,9],[-1,-9],[1,5],[-4,2],[6,-6],[-3,2],[-9,2],[-4,-10],[-3,4],[-3,7],[4,7],[-6,7],[3,6],[-2,-10]],[[1,-7],[-10,-5],[7,6],[-10,-3],[6,6],[1,3],[5,-1],[-10,-7],[2,8],[-4,-2],[-10,-10],[-5,9],[-3,5],[-6,-9]]], dtype = "int64")#candidate|5367|(12, 14, 2)|const|int64
bop_5368 = relay.logical_xor(var_5366.astype('int64'), const_5367.astype('int64')) # shape=(12, 14, 2)
uop_5371 = relay.erf(var_5366.astype('float64')) # shape=(1, 14, 2)
bop_5388 = relay.less(uop_5371.astype('bool'), const_5367.astype('bool')) # shape=(12, 14, 2)
func_2985_call = mod.get_global_var('func_2985')
func_2987_call = mutated_mod.get_global_var('func_2987')
var_5397 = relay.var("var_5397", dtype = "uint16", shape = (1, 1210))#candidate|5397|(1, 1210)|var|uint16
call_5396 = func_2985_call(relay.reshape(var_5397.astype('uint16'), [11, 11, 10]))
call_5398 = func_2985_call(relay.reshape(var_5397.astype('uint16'), [11, 11, 10]))
func_907_call = mod.get_global_var('func_907')
func_912_call = mutated_mod.get_global_var('func_912')
const_5410 = relay.const([-4,2,4,-10,9,-9,-3,-2,-9,4,4,-8,-10,-4,-8,1,-3,-6,8,-1,4,-7,5,9,8,1,-9,-4,6,9,5,7,-2,7,7,-9,6,-9,7,-4,3,8,8,10,2,-7,-9,4,-7,5,1,-4,-2,-7,-3,4,10,-10,4,10,9,-2,4,-2,-1,5,-1,-8,-4,-1,-7,6,7,-6,6,-8,5,-5,-7,2,-4,-9,-7,-5,1,-1,3,8,3,-2,9,-8,-1,5,-10,8,-5,-8,-4,-7,-10,-5,-6,-4,6,2,7,2,-2,8,6,-5,-4,5,-5,5,3,-10,-3,-9,-10,6,10,-5,-5,-4,10,-3,-4,2,-3,7,-7,4,-9,10,-2,7,4,-4,-9,-9,-10,3,1,5,4,-7,-9,2,-3,-7,9,-9,-10,-2,-3,-5,-3,9,8,5,6,-1,-4,10,7,2,-5,-1,-4,-1,-3,-10,-9,-10,2,6,-9,2,-2,-1,-4,-7,4,4,-10,-4,3,1,4,-8,-7,6,-5,-1,3,-8,-9,-3,-2,2,4,-6,2,1,-7,6,-7,-1,-3,1,-6,-10,-3,-9,-2,6,-7,-2,-8,-6,-2,-10,-7,1,-5,3,-1,-8,7,-9,6,-2,-10,3,7,-4,4,-10,-6,8,-3,-3,-3,9,8,-9,-5,-7,-7,-2,10,7,-1,4,8,-9,2,-5,2,-6,-10,-5,8,-10,4,1,-2,-9,-5,-10,-4,2,-2,-2,-1,-5,5,-7,-3,10,-1,-1,-9,-5,3,5,-6,-5,6,-3,8,-7,7,8,1,7,-8,4,-9,10,-6,-1,-4,3,6,6,-3,8,6,-9,-3,8,5,9,-3,-7,-5,-3,5,-10,1,6,8,-3,-2,-1,1,6,-3,1,3,-7,8,-9,8,-5,-5,3,7,-8,-10,-3,2,8,-4,3,1,-6,-2,4,-4,8,-2,-3,-7,-9,1,10,3,9,1,7,-4,10,9,5,-5,-1,4,-9,6,-9,-1,-10,-1,4,-3,-5,-5,2,-1,5,9,-4,-1,-5,-10,-4,5,7,-7,1,1,8,1,8,-8,-7,-1,10,-1,-9,-9,-1,-10,-4,9,-8,9,6,7,-3,9,2,10,-3,8,3,-8,-4,5,7,3,-6,-5,-4,8,-9,-9,10], dtype = "uint16")#candidate|5410|(432,)|const|uint16
var_5411 = relay.var("var_5411", dtype = "uint64", shape = (12,))#candidate|5411|(12,)|var|uint64
var_5412 = relay.var("var_5412", dtype = "uint64", shape = (3, 20))#candidate|5412|(3, 20)|var|uint64
call_5409 = relay.TupleGetItem(func_907_call(relay.reshape(const_5410.astype('uint16'), [4, 12, 9]), relay.reshape(var_5411.astype('uint64'), [12,]), relay.reshape(var_5412.astype('uint64'), [60, 1]), ), 5)
call_5413 = relay.TupleGetItem(func_912_call(relay.reshape(const_5410.astype('uint16'), [4, 12, 9]), relay.reshape(var_5411.astype('uint64'), [12,]), relay.reshape(var_5412.astype('uint64'), [60, 1]), ), 5)
func_5310_call = mod.get_global_var('func_5310')
func_5312_call = mutated_mod.get_global_var('func_5312')
call_5433 = relay.TupleGetItem(func_5310_call(), 0)
call_5434 = relay.TupleGetItem(func_5312_call(), 0)
output = relay.Tuple([bop_5368,bop_5388,call_5396,var_5397,call_5409,const_5410,var_5411,var_5412,call_5433,])
output2 = relay.Tuple([bop_5368,bop_5388,call_5398,var_5397,call_5413,const_5410,var_5411,var_5412,call_5434,])
func_5447 = relay.Function([var_5366,var_5397,var_5411,var_5412,], output)
mod['func_5447'] = func_5447
mod = relay.transform.InferType()(mod)
mutated_mod['func_5447'] = func_5447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5447_call = mutated_mod.get_global_var('func_5447')
var_5449 = relay.var("var_5449", dtype = "int64", shape = (1, 14, 2))#candidate|5449|(1, 14, 2)|var|int64
var_5450 = relay.var("var_5450", dtype = "uint16", shape = (1, 1210))#candidate|5450|(1, 1210)|var|uint16
var_5451 = relay.var("var_5451", dtype = "uint64", shape = (12,))#candidate|5451|(12,)|var|uint64
var_5452 = relay.var("var_5452", dtype = "uint64", shape = (3, 20))#candidate|5452|(3, 20)|var|uint64
call_5448 = func_5447_call(var_5449,var_5450,var_5451,var_5452,)
output = call_5448
func_5453 = relay.Function([var_5449,var_5450,var_5451,var_5452,], output)
mutated_mod['func_5453'] = func_5453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4482_call = mod.get_global_var('func_4482')
func_4483_call = mutated_mod.get_global_var('func_4483')
call_5472 = relay.TupleGetItem(func_4482_call(), 0)
call_5473 = relay.TupleGetItem(func_4483_call(), 0)
output = call_5472
output2 = call_5473
func_5475 = relay.Function([], output)
mod['func_5475'] = func_5475
mod = relay.transform.InferType()(mod)
output = func_5475()
func_5476 = relay.Function([], output)
mutated_mod['func_5476'] = func_5476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3080_call = mod.get_global_var('func_3080')
func_3082_call = mutated_mod.get_global_var('func_3082')
call_5510 = relay.TupleGetItem(func_3080_call(), 2)
call_5511 = relay.TupleGetItem(func_3082_call(), 2)
var_5522 = relay.var("var_5522", dtype = "float32", shape = (832,))#candidate|5522|(832,)|var|float32
bop_5523 = relay.minimum(call_5510.astype('uint16'), relay.reshape(var_5522.astype('uint16'), relay.shape_of(call_5510))) # shape=(832,)
bop_5526 = relay.minimum(call_5511.astype('uint16'), relay.reshape(var_5522.astype('uint16'), relay.shape_of(call_5511))) # shape=(832,)
func_1602_call = mod.get_global_var('func_1602')
func_1604_call = mutated_mod.get_global_var('func_1604')
call_5548 = func_1602_call()
call_5549 = func_1602_call()
output = relay.Tuple([bop_5523,call_5548,])
output2 = relay.Tuple([bop_5526,call_5549,])
func_5551 = relay.Function([var_5522,], output)
mod['func_5551'] = func_5551
mod = relay.transform.InferType()(mod)
mutated_mod['func_5551'] = func_5551
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5552 = relay.var("var_5552", dtype = "float32", shape = (832,))#candidate|5552|(832,)|var|float32
func_5551_call = mutated_mod.get_global_var('func_5551')
call_5553 = func_5551_call(var_5552)
output = call_5553
func_5554 = relay.Function([var_5552], output)
mutated_mod['func_5554'] = func_5554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4839_call = mod.get_global_var('func_4839')
func_4840_call = mutated_mod.get_global_var('func_4840')
call_5589 = relay.TupleGetItem(func_4839_call(), 0)
call_5590 = relay.TupleGetItem(func_4840_call(), 0)
output = call_5589
output2 = call_5590
func_5596 = relay.Function([], output)
mod['func_5596'] = func_5596
mod = relay.transform.InferType()(mod)
mutated_mod['func_5596'] = func_5596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5596_call = mutated_mod.get_global_var('func_5596')
call_5597 = func_5596_call()
output = call_5597
func_5598 = relay.Function([], output)
mutated_mod['func_5598'] = func_5598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3052_call = mod.get_global_var('func_3052')
func_3054_call = mutated_mod.get_global_var('func_3054')
call_5645 = relay.TupleGetItem(func_3052_call(), 0)
call_5646 = relay.TupleGetItem(func_3054_call(), 0)
func_1968_call = mod.get_global_var('func_1968')
func_1970_call = mutated_mod.get_global_var('func_1970')
call_5652 = relay.TupleGetItem(func_1968_call(), 1)
call_5653 = relay.TupleGetItem(func_1970_call(), 1)
func_2749_call = mod.get_global_var('func_2749')
func_2752_call = mutated_mod.get_global_var('func_2752')
const_5655 = relay.const([[1.406218,-0.188925,1.476753,-5.134945,-3.843339,-1.609745,-2.321240,2.227036,-5.249542,-2.703919,1.659318,0.375807,-4.025270,7.604056,-9.638740,-1.445319,3.861394,-9.100604,-0.581256,-0.650057,5.302121,-8.727234,7.056241,-9.626145,-9.018448,-4.777881,1.326694,5.113052,6.421107,6.325232,-6.161693,9.498210,-9.630993,-4.056669,-3.702592,0.772987,-5.662136,-8.970823,-7.509604,6.039140,7.334889,-6.730091,-5.319126,-5.802355,-7.284114,9.464483,6.321862,-8.062896,-1.365985,3.790050,4.934472,-7.730079,-0.480618,4.345221,9.988075,8.170642,9.874213,7.821565,8.926400,6.472350,6.311440,-5.402226,2.810854,1.654473,-5.282613,8.184890,2.551727,4.688630,-8.045377,-8.719321,2.579740,-6.939434,8.692514,-5.275181,1.136197,-1.344102,-0.033234,-9.345685,-6.237344,5.658660,-8.203796,-3.535933,-9.949121,1.542765,1.090332,-4.311994,-5.601958,9.693381,3.653884,-4.024280,6.051155,9.024885,-0.440276,5.297397,5.044535,2.908225,4.493522,-1.079420,4.546352,-0.684881,7.310365,8.027941,0.532469,-2.478595],[7.491913,-8.000196,7.939342,-5.627669,9.465212,-0.515265,7.608942,-5.241934,-4.514682,-8.889867,-8.873712,-1.840203,-7.899535,7.601460,-4.970206,-0.271297,7.593628,-8.315355,-5.535920,-0.401006,-0.465426,6.266021,-0.379447,0.714613,-0.702587,-9.929880,-6.673872,-8.411828,-0.313099,1.532502,0.770355,-7.118001,-5.674714,-3.650782,-6.712889,-9.839776,0.721236,-2.056230,2.724704,-4.985556,3.661038,-3.040022,0.833682,-1.554854,7.317623,-1.612346,5.677095,2.534949,2.334565,2.078259,-2.014548,5.773516,4.892621,4.149414,5.198316,-7.720523,-0.474187,-9.208890,7.999301,8.086930,-3.287657,-1.455715,9.265497,7.407674,5.331161,-0.444391,-0.694842,9.823276,6.152078,-9.260929,0.413806,7.461631,-3.836787,8.302601,0.440447,-0.526545,8.971269,5.602126,-5.301262,8.411541,1.320061,4.988305,0.862493,4.532495,7.266574,2.426768,-7.255634,-6.074505,8.651850,6.256880,-0.106322,-5.711831,-0.403203,-4.137185,8.896550,-6.883284,8.782138,-1.479490,-7.304861,3.351188,-3.977153,-4.084302,-3.462454,2.819737],[6.304548,-9.555524,-4.332533,9.105236,-2.604058,7.120481,1.030957,6.699889,3.326561,-2.938479,9.809941,6.250085,-2.660708,3.541220,-4.357731,-2.703648,9.538543,9.034667,-7.311691,-3.362535,0.312308,-1.608263,9.595274,7.057708,2.294550,-5.892814,-0.801404,-8.216445,-7.325020,4.644281,-7.442790,-3.607506,-2.053140,2.663721,-4.177926,9.231601,1.714563,-6.057791,1.714684,2.665665,5.088348,-8.834626,8.483437,0.486810,-2.140943,-5.754087,-1.020536,-3.785126,8.367187,8.790540,3.580840,9.865573,-0.829150,6.331575,6.950260,7.086555,-3.758554,-0.564175,-3.182046,4.629887,-5.469188,-7.963798,-8.375860,6.545514,-1.893320,2.158463,-7.610783,7.009982,9.431045,-1.740275,6.241123,1.397791,4.517628,-7.211554,2.634880,-8.863583,8.508188,4.248074,8.771652,9.150662,9.725959,2.057411,3.892713,8.350470,1.549735,-1.111527,5.036467,8.063869,1.592498,-5.005488,7.404842,6.925140,8.149127,3.567722,9.203825,6.394691,4.868938,-6.434221,5.124356,4.063764,-4.714912,4.115586,-2.420635,-5.231861],[-8.919416,-7.024850,-7.755052,1.249613,-2.987037,-4.678950,3.117580,5.727542,8.809646,-6.149141,7.440355,1.695373,7.007478,3.979954,7.922552,5.409344,-2.814796,-2.284619,1.277066,6.949843,-8.974996,-4.359594,1.780355,-1.532606,6.046430,8.343440,1.327483,-0.063606,5.774917,-5.066306,-1.678437,4.652525,2.671137,0.646014,4.093869,0.260042,-3.443294,8.112491,6.936416,-3.037172,-8.578880,4.817154,8.248445,-4.911291,9.844679,3.775750,2.011199,-6.770041,-8.279004,2.155169,-9.504148,9.541193,-0.333693,-4.551635,6.563452,3.412518,-0.407665,0.008172,-3.877714,3.202229,-2.909657,8.143036,5.214012,-1.360715,7.811079,3.197946,-3.463093,8.014611,4.527788,-2.562674,-0.439403,0.994752,-5.561550,-0.789064,-5.970946,-8.780709,4.639957,-1.968026,-8.272805,-9.284004,2.360397,2.424367,9.786742,-3.574932,2.183358,0.291667,-2.950150,-0.263436,3.540187,-8.102609,-4.823774,-0.777990,-6.574957,-1.776785,8.312067,4.864211,-8.665166,2.250891,6.789750,3.118400,-5.352997,-4.020237,5.745849,-5.373811]], dtype = "float32")#candidate|5655|(4, 104)|const|float32
call_5654 = relay.TupleGetItem(func_2749_call(relay.reshape(const_5655.astype('float32'), [4, 8, 13]), relay.reshape(call_5652.astype('float32'), [128,]), ), 1)
call_5656 = relay.TupleGetItem(func_2752_call(relay.reshape(const_5655.astype('float32'), [4, 8, 13]), relay.reshape(call_5652.astype('float32'), [128,]), ), 1)
func_4368_call = mod.get_global_var('func_4368')
func_4370_call = mutated_mod.get_global_var('func_4370')
var_5658 = relay.var("var_5658", dtype = "float64", shape = (99,))#candidate|5658|(99,)|var|float64
call_5657 = relay.TupleGetItem(func_4368_call(relay.reshape(var_5658.astype('float64'), [3, 11, 3])), 1)
call_5659 = relay.TupleGetItem(func_4370_call(relay.reshape(var_5658.astype('float64'), [3, 11, 3])), 1)
uop_5660 = relay.log2(var_5658.astype('float32')) # shape=(99,)
bop_5669 = relay.greater_equal(call_5654.astype('bool'), relay.reshape(call_5645.astype('bool'), relay.shape_of(call_5654))) # shape=(2, 4, 16)
bop_5672 = relay.greater_equal(call_5656.astype('bool'), relay.reshape(call_5646.astype('bool'), relay.shape_of(call_5656))) # shape=(2, 4, 16)
func_1239_call = mod.get_global_var('func_1239')
func_1243_call = mutated_mod.get_global_var('func_1243')
var_5688 = relay.var("var_5688", dtype = "bool", shape = (3328,))#candidate|5688|(3328,)|var|bool
const_5689 = relay.const([10,10,-4,-4,-10,1,-9,-7,10,4,-3,1], dtype = "uint64")#candidate|5689|(12,)|const|uint64
call_5687 = relay.TupleGetItem(func_1239_call(relay.reshape(var_5688.astype('bool'), [16, 13, 16]), relay.reshape(const_5689.astype('uint64'), [12,]), ), 1)
call_5690 = relay.TupleGetItem(func_1243_call(relay.reshape(var_5688.astype('bool'), [16, 13, 16]), relay.reshape(const_5689.astype('uint64'), [12,]), ), 1)
output = relay.Tuple([call_5652,const_5655,call_5657,uop_5660,bop_5669,call_5687,var_5688,const_5689,])
output2 = relay.Tuple([call_5653,const_5655,call_5659,uop_5660,bop_5672,call_5690,var_5688,const_5689,])
func_5701 = relay.Function([var_5658,var_5688,], output)
mod['func_5701'] = func_5701
mod = relay.transform.InferType()(mod)
mutated_mod['func_5701'] = func_5701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5701_call = mutated_mod.get_global_var('func_5701')
var_5703 = relay.var("var_5703", dtype = "float64", shape = (99,))#candidate|5703|(99,)|var|float64
var_5704 = relay.var("var_5704", dtype = "bool", shape = (3328,))#candidate|5704|(3328,)|var|bool
call_5702 = func_5701_call(var_5703,var_5704,)
output = call_5702
func_5705 = relay.Function([var_5703,var_5704,], output)
mutated_mod['func_5705'] = func_5705
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5727 = relay.var("var_5727", dtype = "int8", shape = (11, 16, 16))#candidate|5727|(11, 16, 16)|var|int8
var_5728 = relay.var("var_5728", dtype = "int8", shape = (11, 16, 16))#candidate|5728|(11, 16, 16)|var|int8
bop_5729 = relay.minimum(var_5727.astype('int8'), relay.reshape(var_5728.astype('int8'), relay.shape_of(var_5727))) # shape=(11, 16, 16)
bop_5735 = relay.floor_divide(var_5728.astype('float64'), relay.reshape(bop_5729.astype('float64'), relay.shape_of(var_5728))) # shape=(11, 16, 16)
output = relay.Tuple([bop_5735,])
output2 = relay.Tuple([bop_5735,])
func_5744 = relay.Function([var_5727,var_5728,], output)
mod['func_5744'] = func_5744
mod = relay.transform.InferType()(mod)
var_5745 = relay.var("var_5745", dtype = "int8", shape = (11, 16, 16))#candidate|5745|(11, 16, 16)|var|int8
var_5746 = relay.var("var_5746", dtype = "int8", shape = (11, 16, 16))#candidate|5746|(11, 16, 16)|var|int8
output = func_5744(var_5745,var_5746,)
func_5747 = relay.Function([var_5745,var_5746,], output)
mutated_mod['func_5747'] = func_5747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3867_call = mod.get_global_var('func_3867')
func_3868_call = mutated_mod.get_global_var('func_3868')
call_5749 = relay.TupleGetItem(func_3867_call(), 0)
call_5750 = relay.TupleGetItem(func_3868_call(), 0)
output = call_5749
output2 = call_5750
func_5754 = relay.Function([], output)
mod['func_5754'] = func_5754
mod = relay.transform.InferType()(mod)
mutated_mod['func_5754'] = func_5754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5754_call = mutated_mod.get_global_var('func_5754')
call_5755 = func_5754_call()
output = call_5755
func_5756 = relay.Function([], output)
mutated_mod['func_5756'] = func_5756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2252_call = mod.get_global_var('func_2252')
func_2254_call = mutated_mod.get_global_var('func_2254')
call_5762 = func_2252_call()
call_5763 = func_2252_call()
output = call_5762
output2 = call_5763
func_5778 = relay.Function([], output)
mod['func_5778'] = func_5778
mod = relay.transform.InferType()(mod)
output = func_5778()
func_5779 = relay.Function([], output)
mutated_mod['func_5779'] = func_5779
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5785 = relay.var("var_5785", dtype = "uint64", shape = (14, 11, 1))#candidate|5785|(14, 11, 1)|var|uint64
const_5786 = relay.const([[[-9,3,4,10,7,6,-4],[6,5,-4,-10,-8,5,8],[6,-8,-10,-8,2,8,10],[5,-6,-4,2,-4,10,-7],[-4,7,-2,-6,7,1,-4],[9,4,9,-6,-2,1,-3],[8,6,-4,-3,-9,1,4],[7,10,3,-9,5,-7,6],[-5,-9,-8,6,-9,8,-9],[-5,-10,3,8,5,10,5],[-9,5,9,-6,10,-8,-10]],[[-8,5,3,6,7,-6,3],[4,-5,-10,-8,6,-7,5],[-7,2,-7,-9,-2,8,8],[4,10,-1,5,-5,2,9],[10,-7,-1,4,-5,10,-7],[9,-2,7,4,-9,1,2],[-7,-5,6,-6,2,-7,-1],[6,-5,3,1,9,10,-4],[2,-6,-8,-6,4,3,1],[5,-5,2,-8,-7,-9,-4],[-6,9,6,-9,-8,-1,8]],[[-10,-4,-5,-6,10,3,2],[-6,10,5,-2,-7,-7,7],[-9,2,5,6,4,8,5],[1,-5,4,-1,-5,9,-5],[8,6,6,-9,-3,-3,-7],[3,2,9,-3,1,1,-8],[-1,-9,-4,8,-1,2,-4],[-3,4,2,1,3,4,7],[-1,6,-7,-3,-9,2,-10],[6,-7,-6,4,-7,9,9],[4,-7,-3,9,9,3,-2]],[[8,7,-7,-2,5,1,2],[-2,3,9,2,-4,-3,10],[-9,-9,6,10,2,6,-1],[-1,-7,6,-8,-10,6,-1],[7,5,8,4,3,9,7],[3,4,-2,9,-1,-2,9],[-6,-7,4,10,7,5,-7],[5,10,1,4,-5,9,9],[-10,9,9,-9,-9,4,-3],[6,-1,-2,-9,-7,6,3],[9,-9,2,-4,-6,-5,-4]],[[-1,-6,-6,7,2,-3,-8],[-2,-6,-7,-1,-3,-10,-10],[3,4,2,2,10,4,-5],[10,5,6,-4,-6,-2,10],[9,-8,5,-8,-3,2,10],[-7,4,10,-1,3,-9,-10],[10,-2,-1,5,2,10,-4],[3,10,-10,-9,-4,-7,8],[5,-5,-10,-6,-7,5,-4],[7,9,5,9,-2,6,-9],[-2,-8,-4,2,2,-5,10]],[[-8,-6,4,4,5,-5,-2],[-4,5,-7,-2,8,7,3],[8,-3,-8,3,6,-3,3],[-1,-8,-7,10,-6,8,-8],[3,-8,-5,-9,-2,8,2],[-3,9,3,9,-10,5,-3],[9,8,5,3,9,-4,4],[2,-3,-4,-9,2,6,-8],[10,-2,5,3,5,9,-9],[6,-8,1,1,6,2,-9],[9,-9,-1,10,-2,7,8]],[[-3,2,10,6,-1,-9,-9],[4,1,-7,4,3,7,6],[5,9,-1,-7,-1,4,-10],[-1,-6,-8,10,-1,-5,-8],[-2,-4,8,-4,6,-2,4],[1,1,-4,-8,-7,-8,-3],[-3,-5,5,1,-5,-4,8],[-2,-4,-8,-6,3,5,-2],[-6,-7,-6,-3,2,-6,-1],[-9,-6,9,3,-4,-10,-3],[-5,-9,8,2,-8,6,-1]],[[6,1,-10,6,7,-9,-8],[-8,-5,6,5,-1,9,-4],[-7,5,8,9,-5,7,4],[-4,6,-5,-6,6,6,-8],[7,8,-10,7,1,6,-3],[-9,-1,-1,-7,-10,9,4],[-3,8,6,-2,-1,4,9],[9,5,10,2,-4,10,-2],[10,-4,-8,-1,-10,-3,-5],[4,-9,5,10,-1,-7,-1],[-1,-7,7,-3,6,1,8]],[[9,-1,9,-4,5,10,-6],[2,-5,8,-3,-3,-2,-10],[-5,5,4,-6,7,5,-4],[7,-3,5,2,-10,-10,1],[4,-3,10,4,5,6,10],[1,8,3,-8,1,-4,7],[6,8,-1,-10,8,-6,-5],[-4,-4,10,4,5,-4,4],[-7,-3,-8,4,3,-10,-1],[-5,-9,-1,3,-4,5,-9],[-6,-8,-3,-10,4,-2,-10]],[[-10,-1,7,-2,-2,2,-4],[-7,-9,-7,8,9,-4,-3],[-2,1,6,-4,1,-3,-5],[-10,5,1,2,10,9,-9],[-2,7,5,-3,1,6,-7],[6,-6,-8,-4,5,-8,-10],[-4,-8,-1,-10,5,9,-5],[8,4,2,10,2,-1,-2],[4,4,10,4,-6,-10,-10],[-7,-4,4,10,-7,-8,-4],[8,9,-9,7,4,-3,-6]],[[3,1,-10,8,-2,-2,7],[-10,10,-9,9,2,9,9],[-10,2,10,5,8,-4,10],[-1,-5,-9,8,-3,-8,-3],[3,-9,-7,-8,6,-9,-7],[-7,10,-5,9,-9,4,2],[-1,10,-8,-8,-2,4,-8],[-4,-7,-1,1,1,9,-6],[5,6,-2,-9,7,-7,-4],[9,-5,8,-6,-10,-4,-8],[2,10,10,3,-4,4,2]],[[10,-2,7,-2,1,3,-6],[4,-3,-5,-6,-9,-1,-3],[-2,-6,-10,-1,-8,-1,10],[2,-4,7,-3,-10,-9,9],[-2,5,-7,8,1,-4,2],[-10,1,8,8,-3,-10,-1],[-2,9,3,9,6,7,7],[-8,9,3,2,7,9,-3],[5,-1,4,-2,-3,7,6],[-9,-5,4,-7,-4,-8,-10],[-1,9,-9,-2,10,10,-2]],[[-5,10,3,-2,-9,-4,9],[6,-1,4,-2,2,-6,9],[-8,-10,1,-8,5,-3,-1],[9,-1,1,1,-5,10,8],[-8,9,-8,-8,9,7,-5],[10,9,6,-6,3,-4,-2],[-4,10,7,-9,-8,-8,-4],[-5,-7,-7,-6,-6,3,10],[8,2,2,7,1,6,4],[10,-1,10,-2,2,-1,-8],[10,4,10,1,9,-1,3]],[[-2,5,6,9,-2,3,8],[-6,8,6,5,7,-10,-3],[7,-10,2,4,-1,-4,-3],[1,-10,-2,3,10,6,4],[-6,-6,-5,-3,-4,-5,-10],[-10,-5,-8,7,3,8,10],[3,-7,-2,-3,1,-4,-4],[10,9,1,-2,-8,7,-1],[-7,8,-6,10,-9,-3,-10],[5,-5,10,-6,9,-9,9],[8,-2,2,6,6,3,8]]], dtype = "uint64")#candidate|5786|(14, 11, 7)|const|uint64
bop_5787 = relay.not_equal(var_5785.astype('bool'), const_5786.astype('bool')) # shape=(14, 11, 7)
func_2541_call = mod.get_global_var('func_2541')
func_2543_call = mutated_mod.get_global_var('func_2543')
var_5791 = relay.var("var_5791", dtype = "float32", shape = (2, 208))#candidate|5791|(2, 208)|var|float32
call_5790 = relay.TupleGetItem(func_2541_call(relay.reshape(var_5791.astype('float32'), [416,])), 0)
call_5792 = relay.TupleGetItem(func_2543_call(relay.reshape(var_5791.astype('float32'), [416,])), 0)
output = relay.Tuple([bop_5787,call_5790,var_5791,])
output2 = relay.Tuple([bop_5787,call_5792,var_5791,])
func_5794 = relay.Function([var_5785,var_5791,], output)
mod['func_5794'] = func_5794
mod = relay.transform.InferType()(mod)
var_5795 = relay.var("var_5795", dtype = "uint64", shape = (14, 11, 1))#candidate|5795|(14, 11, 1)|var|uint64
var_5796 = relay.var("var_5796", dtype = "float32", shape = (2, 208))#candidate|5796|(2, 208)|var|float32
output = func_5794(var_5795,var_5796,)
func_5797 = relay.Function([var_5795,var_5796,], output)
mutated_mod['func_5797'] = func_5797
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5876 = relay.var("var_5876", dtype = "bool", shape = (12, 9, 5))#candidate|5876|(12, 9, 5)|var|bool
var_5877 = relay.var("var_5877", dtype = "bool", shape = (12, 9, 5))#candidate|5877|(12, 9, 5)|var|bool
bop_5878 = relay.logical_and(var_5876.astype('bool'), relay.reshape(var_5877.astype('bool'), relay.shape_of(var_5876))) # shape=(12, 9, 5)
func_3080_call = mod.get_global_var('func_3080')
func_3082_call = mutated_mod.get_global_var('func_3082')
call_5884 = relay.TupleGetItem(func_3080_call(), 1)
call_5885 = relay.TupleGetItem(func_3082_call(), 1)
uop_5887 = relay.cosh(var_5876.astype('float64')) # shape=(12, 9, 5)
func_5265_call = mod.get_global_var('func_5265')
func_5267_call = mutated_mod.get_global_var('func_5267')
var_5907 = relay.var("var_5907", dtype = "bool", shape = ())#candidate|5907|()|var|bool
call_5906 = relay.TupleGetItem(func_5265_call(relay.reshape(var_5907.astype('bool'), [])), 2)
call_5908 = relay.TupleGetItem(func_5267_call(relay.reshape(var_5907.astype('bool'), [])), 2)
output = relay.Tuple([bop_5878,call_5884,uop_5887,call_5906,var_5907,])
output2 = relay.Tuple([bop_5878,call_5885,uop_5887,call_5908,var_5907,])
func_5921 = relay.Function([var_5876,var_5877,var_5907,], output)
mod['func_5921'] = func_5921
mod = relay.transform.InferType()(mod)
mutated_mod['func_5921'] = func_5921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5921_call = mutated_mod.get_global_var('func_5921')
var_5923 = relay.var("var_5923", dtype = "bool", shape = (12, 9, 5))#candidate|5923|(12, 9, 5)|var|bool
var_5924 = relay.var("var_5924", dtype = "bool", shape = (12, 9, 5))#candidate|5924|(12, 9, 5)|var|bool
var_5925 = relay.var("var_5925", dtype = "bool", shape = ())#candidate|5925|()|var|bool
call_5922 = func_5921_call(var_5923,var_5924,var_5925,)
output = call_5922
func_5926 = relay.Function([var_5923,var_5924,var_5925,], output)
mutated_mod['func_5926'] = func_5926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4934_call = mod.get_global_var('func_4934')
func_4936_call = mutated_mod.get_global_var('func_4936')
call_5950 = relay.TupleGetItem(func_4934_call(), 1)
call_5951 = relay.TupleGetItem(func_4936_call(), 1)
var_5955 = relay.var("var_5955", dtype = "float32", shape = (128,))#candidate|5955|(128,)|var|float32
bop_5956 = relay.greater_equal(call_5950.astype('bool'), relay.reshape(var_5955.astype('bool'), relay.shape_of(call_5950))) # shape=(128,)
bop_5959 = relay.greater_equal(call_5951.astype('bool'), relay.reshape(var_5955.astype('bool'), relay.shape_of(call_5951))) # shape=(128,)
output = relay.Tuple([bop_5956,])
output2 = relay.Tuple([bop_5959,])
func_5968 = relay.Function([var_5955,], output)
mod['func_5968'] = func_5968
mod = relay.transform.InferType()(mod)
mutated_mod['func_5968'] = func_5968
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5969 = relay.var("var_5969", dtype = "float32", shape = (128,))#candidate|5969|(128,)|var|float32
func_5968_call = mutated_mod.get_global_var('func_5968')
call_5970 = func_5968_call(var_5969)
output = call_5970
func_5971 = relay.Function([var_5969], output)
mutated_mod['func_5971'] = func_5971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5475_call = mod.get_global_var('func_5475')
func_5476_call = mutated_mod.get_global_var('func_5476')
call_6066 = func_5475_call()
call_6067 = func_5475_call()
output = relay.Tuple([call_6066,])
output2 = relay.Tuple([call_6067,])
func_6076 = relay.Function([], output)
mod['func_6076'] = func_6076
mod = relay.transform.InferType()(mod)
output = func_6076()
func_6077 = relay.Function([], output)
mutated_mod['func_6077'] = func_6077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1905_call = mod.get_global_var('func_1905')
func_1906_call = mutated_mod.get_global_var('func_1906')
call_6227 = relay.TupleGetItem(func_1905_call(), 0)
call_6228 = relay.TupleGetItem(func_1906_call(), 0)
func_4124_call = mod.get_global_var('func_4124')
func_4128_call = mutated_mod.get_global_var('func_4128')
var_6242 = relay.var("var_6242", dtype = "uint64", shape = (192,))#candidate|6242|(192,)|var|uint64
call_6241 = relay.TupleGetItem(func_4124_call(relay.reshape(call_6227.astype('float32'), [128,]), relay.reshape(var_6242.astype('uint64'), [48, 4]), relay.reshape(var_6242.astype('uint64'), [48, 4]), ), 4)
call_6243 = relay.TupleGetItem(func_4128_call(relay.reshape(call_6227.astype('float32'), [128,]), relay.reshape(var_6242.astype('uint64'), [48, 4]), relay.reshape(var_6242.astype('uint64'), [48, 4]), ), 4)
output = relay.Tuple([call_6227,call_6241,var_6242,])
output2 = relay.Tuple([call_6228,call_6243,var_6242,])
func_6245 = relay.Function([var_6242,], output)
mod['func_6245'] = func_6245
mod = relay.transform.InferType()(mod)
var_6246 = relay.var("var_6246", dtype = "uint64", shape = (192,))#candidate|6246|(192,)|var|uint64
output = func_6245(var_6246)
func_6247 = relay.Function([var_6246], output)
mutated_mod['func_6247'] = func_6247
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6283 = relay.const([[[-10,10,-6,10,10,7,7,9,-2,-9,7,9,-10,10,-5,-1],[7,-1,-8,-4,6,6,-9,-9,-10,-2,-2,3,-5,9,-9,4],[-4,8,-6,2,-6,-5,-5,-5,-5,-4,-7,1,7,-1,4,2],[-2,2,3,-10,-4,3,1,4,5,5,4,6,-7,10,2,-9]],[[-10,-4,7,-3,1,8,-4,-8,-10,-2,8,-8,5,-6,7,1],[6,-2,9,4,1,-2,4,-5,10,3,-7,2,-8,-9,2,4],[-5,-3,-4,-6,8,-2,-5,-9,6,4,-2,3,3,-6,-2,-6],[-1,-5,5,1,-9,-8,-2,3,10,3,-4,-3,-8,3,-1,1]],[[10,-6,7,-10,2,3,6,4,-3,-9,3,3,1,5,7,-4],[2,-3,1,7,1,9,-6,-3,-2,-6,-4,-8,7,7,-9,-2],[-4,2,-10,9,1,-1,3,-5,-8,-1,2,-7,5,4,8,-7],[-2,-8,-9,6,-6,-8,10,-5,-6,1,8,-8,6,6,-9,6]],[[3,-6,2,-2,-8,9,-6,8,-3,-2,1,-1,-4,-10,-10,-6],[10,-5,5,-9,10,5,-4,-7,-4,-7,9,-1,-7,-5,5,9],[-5,-8,-4,7,6,-1,5,-9,-7,3,6,-8,-2,9,-4,5],[-7,-4,-9,-6,-3,5,-4,-6,-1,-6,10,10,-5,-1,1,10]],[[8,-6,7,2,-8,-7,-3,1,9,-1,-1,2,1,-7,-9,8],[-3,4,8,-9,5,9,6,-2,-9,-5,-3,8,-10,6,-4,-7],[-1,-8,-9,5,4,1,-4,-6,-5,5,7,4,6,7,4,-8],[6,-2,-4,10,1,-7,-6,9,-3,-1,-8,8,-5,-6,8,4]],[[10,1,-4,-2,-6,-3,-4,-4,-9,-7,-2,-2,9,-7,-2,3],[10,-5,-6,-1,-6,5,-9,6,5,-6,10,5,-4,8,-5,9],[4,-2,-1,-3,9,8,6,-7,-1,10,-1,-3,-9,-2,-2,10],[4,-4,-6,5,-4,5,-9,1,-7,3,7,-4,9,-1,-8,-4]],[[-4,9,-7,5,-9,3,3,10,-6,10,3,10,-4,2,1,-4],[6,6,10,-9,2,-9,-6,6,5,7,-2,9,-5,7,9,-4],[-9,-2,-2,9,3,-8,8,2,2,9,-4,1,1,7,1,5],[-2,8,8,-5,-5,9,-8,7,10,-7,6,6,-8,-9,6,1]],[[-3,-9,8,9,8,-9,10,-10,1,5,-7,-9,5,6,-2,-7],[-7,3,2,-1,1,-9,-5,1,8,7,8,2,2,5,4,8],[-2,-9,4,-5,9,7,-4,-1,-4,-8,2,8,-8,9,-8,-5],[7,-3,1,7,-3,-3,-3,-9,-3,-1,-5,-1,3,4,7,2]],[[-3,-9,4,-4,10,-5,-4,-2,-1,3,4,-10,-4,-10,6,-6],[-8,3,1,-2,9,-8,4,-1,4,3,-6,7,-1,-10,9,-8],[-3,1,-10,-6,10,3,3,9,6,3,8,3,-9,6,10,-6],[-7,-4,-10,8,-4,4,-5,-3,8,4,-8,-5,9,-6,7,10]],[[9,-1,-6,-8,1,10,-6,6,10,8,-6,-6,6,4,4,-9],[9,9,-8,8,9,-5,2,7,-5,2,1,6,10,3,3,-4],[-2,10,1,1,-7,-5,10,-10,8,-6,-10,6,-2,1,-1,-10],[9,2,9,8,-10,4,6,4,-6,4,-5,-3,9,2,8,-4]],[[-3,6,10,7,-8,1,-7,-7,7,6,-2,-7,-4,5,-5,8],[3,-10,-8,2,-2,-10,-10,-9,-8,7,5,-5,6,-10,6,9],[-3,-4,-9,-9,-1,-7,5,6,-10,-7,8,1,-9,5,8,7],[-4,-2,-7,-2,-9,-7,-5,-10,-5,-10,-9,7,2,5,7,-3]],[[3,1,-6,8,2,-2,10,1,-8,-10,-4,7,10,-9,-6,-5],[-8,10,-1,-1,-4,9,-4,-1,5,-1,8,-6,2,3,-8,6],[7,1,-4,1,7,4,-4,8,-6,-8,-9,-3,2,8,6,-5],[1,3,10,5,-5,3,-6,9,-9,6,-3,-6,5,-4,-9,-6]]], dtype = "uint64")#candidate|6283|(12, 4, 16)|const|uint64
var_6284 = relay.var("var_6284", dtype = "uint64", shape = (12, 4, 16))#candidate|6284|(12, 4, 16)|var|uint64
bop_6285 = relay.right_shift(const_6283.astype('uint64'), relay.reshape(var_6284.astype('uint64'), relay.shape_of(const_6283))) # shape=(12, 4, 16)
output = relay.Tuple([bop_6285,])
output2 = relay.Tuple([bop_6285,])
func_6295 = relay.Function([var_6284,], output)
mod['func_6295'] = func_6295
mod = relay.transform.InferType()(mod)
var_6296 = relay.var("var_6296", dtype = "uint64", shape = (12, 4, 16))#candidate|6296|(12, 4, 16)|var|uint64
output = func_6295(var_6296)
func_6297 = relay.Function([var_6296], output)
mutated_mod['func_6297'] = func_6297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5006_call = mod.get_global_var('func_5006')
func_5008_call = mutated_mod.get_global_var('func_5008')
call_6383 = func_5006_call()
call_6384 = func_5006_call()
output = call_6383
output2 = call_6384
func_6406 = relay.Function([], output)
mod['func_6406'] = func_6406
mod = relay.transform.InferType()(mod)
mutated_mod['func_6406'] = func_6406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6406_call = mutated_mod.get_global_var('func_6406')
call_6407 = func_6406_call()
output = call_6407
func_6408 = relay.Function([], output)
mutated_mod['func_6408'] = func_6408
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6439 = relay.const(8.329657, dtype = "float64")#candidate|6439|()|const|float64
var_6440 = relay.var("var_6440", dtype = "float64", shape = (3, 1, 16))#candidate|6440|(3, 1, 16)|var|float64
bop_6441 = relay.divide(const_6439.astype('float64'), var_6440.astype('float64')) # shape=(3, 1, 16)
func_4879_call = mod.get_global_var('func_4879')
func_4880_call = mutated_mod.get_global_var('func_4880')
call_6444 = func_4879_call()
call_6445 = func_4879_call()
var_6447 = relay.var("var_6447", dtype = "float64", shape = (3, 15, 16))#candidate|6447|(3, 15, 16)|var|float64
bop_6448 = relay.logical_and(var_6440.astype('bool'), var_6447.astype('bool')) # shape=(3, 15, 16)
func_2966_call = mod.get_global_var('func_2966')
func_2969_call = mutated_mod.get_global_var('func_2969')
var_6462 = relay.var("var_6462", dtype = "float64", shape = (128,))#candidate|6462|(128,)|var|float64
call_6461 = relay.TupleGetItem(func_2966_call(relay.reshape(var_6462.astype('float64'), [128,]), relay.reshape(var_6462.astype('float64'), [128,]), ), 1)
call_6463 = relay.TupleGetItem(func_2969_call(relay.reshape(var_6462.astype('float64'), [128,]), relay.reshape(var_6462.astype('float64'), [128,]), ), 1)
output = relay.Tuple([bop_6441,call_6444,bop_6448,call_6461,var_6462,])
output2 = relay.Tuple([bop_6441,call_6445,bop_6448,call_6463,var_6462,])
func_6473 = relay.Function([var_6440,var_6447,var_6462,], output)
mod['func_6473'] = func_6473
mod = relay.transform.InferType()(mod)
var_6474 = relay.var("var_6474", dtype = "float64", shape = (3, 1, 16))#candidate|6474|(3, 1, 16)|var|float64
var_6475 = relay.var("var_6475", dtype = "float64", shape = (3, 15, 16))#candidate|6475|(3, 15, 16)|var|float64
var_6476 = relay.var("var_6476", dtype = "float64", shape = (128,))#candidate|6476|(128,)|var|float64
output = func_6473(var_6474,var_6475,var_6476,)
func_6477 = relay.Function([var_6474,var_6475,var_6476,], output)
mutated_mod['func_6477'] = func_6477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4934_call = mod.get_global_var('func_4934')
func_4936_call = mutated_mod.get_global_var('func_4936')
call_6493 = relay.TupleGetItem(func_4934_call(), 1)
call_6494 = relay.TupleGetItem(func_4936_call(), 1)
output = call_6493
output2 = call_6494
func_6495 = relay.Function([], output)
mod['func_6495'] = func_6495
mod = relay.transform.InferType()(mod)
output = func_6495()
func_6496 = relay.Function([], output)
mutated_mod['func_6496'] = func_6496
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6504 = relay.const(3, dtype = "uint64")#candidate|6504|()|const|uint64
var_6505 = relay.var("var_6505", dtype = "uint64", shape = (5, 13, 13))#candidate|6505|(5, 13, 13)|var|uint64
bop_6506 = relay.not_equal(const_6504.astype('bool'), var_6505.astype('bool')) # shape=(5, 13, 13)
func_5754_call = mod.get_global_var('func_5754')
func_5756_call = mutated_mod.get_global_var('func_5756')
call_6513 = func_5754_call()
call_6514 = func_5754_call()
uop_6518 = relay.cos(bop_6506.astype('float64')) # shape=(5, 13, 13)
func_5070_call = mod.get_global_var('func_5070')
func_5071_call = mutated_mod.get_global_var('func_5071')
call_6521 = relay.TupleGetItem(func_5070_call(), 1)
call_6522 = relay.TupleGetItem(func_5071_call(), 1)
output = relay.Tuple([call_6513,uop_6518,call_6521,])
output2 = relay.Tuple([call_6514,uop_6518,call_6522,])
func_6530 = relay.Function([var_6505,], output)
mod['func_6530'] = func_6530
mod = relay.transform.InferType()(mod)
var_6531 = relay.var("var_6531", dtype = "uint64", shape = (5, 13, 13))#candidate|6531|(5, 13, 13)|var|uint64
output = func_6530(var_6531)
func_6532 = relay.Function([var_6531], output)
mutated_mod['func_6532'] = func_6532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5328_call = mod.get_global_var('func_5328')
func_5329_call = mutated_mod.get_global_var('func_5329')
call_6534 = func_5328_call()
call_6535 = func_5328_call()
func_4456_call = mod.get_global_var('func_4456')
func_4460_call = mutated_mod.get_global_var('func_4460')
var_6540 = relay.var("var_6540", dtype = "float32", shape = (16, 26))#candidate|6540|(16, 26)|var|float32
call_6539 = relay.TupleGetItem(func_4456_call(relay.reshape(call_6534.astype('float32'), [2, 4, 16]), relay.reshape(var_6540.astype('float32'), [416,]), ), 0)
call_6541 = relay.TupleGetItem(func_4460_call(relay.reshape(call_6534.astype('float32'), [2, 4, 16]), relay.reshape(var_6540.astype('float32'), [416,]), ), 0)
func_1496_call = mod.get_global_var('func_1496')
func_1500_call = mutated_mod.get_global_var('func_1500')
const_6543 = relay.const(False, dtype = "bool")#candidate|6543|()|const|bool
const_6544 = relay.const([[False,False,True,False,False,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,False,False,True,False,False,True,True,True,True,False,True,True,False,True,False,True,False,False,False,False,True,True,False,False,True,True,False,True,False,True,False,False,True,True,True,True,False,False,True,True,False,False,False,True,True,False,False,True,False,False,True,False,True,False,False,False,True,False,True,True,True],[True,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,True,True,True,True,True,True,True,True,True,True,False,False,True,True,True,False,False,False,True,True,False,True,False,True,True,True,False,True,False,False,True,True,True,False,False,False,True,True,True,True,True,True,True,False,False,False,False,True,False,True,False,False,True,False,True,False,True,True,True,True,True,False,False,True,True,True,True,False],[False,True,True,True,False,False,True,True,True,False,False,True,True,False,False,False,False,True,False,True,True,True,True,False,False,True,True,True,False,True,True,True,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,True,False,True,False,True,False,True,False,True,True,True,True,False,True,True,True,True,True,True,True,True,False,True,True,False,True,True,True,True,True],[True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,False,True,True,True,False,False,True,True,True,False,True,False,True,False,False,False,True,False,False,False,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,False,True,False,True,False,True,True,False,False,True,False,False,False,True,False,True,True,False,False,True,True,True,False,True,True],[True,False,True,False,True,False,False,False,True,False,False,False,True,False,False,False,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True,False,False,False,False,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,True,True,True,True,True,True,True,True,False,False,True,True,False,False,False,False,True,True,False,True,True,False,True,False,True,False],[False,False,True,False,False,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,True,False,True,False,True,False,False,True,True,True,True,False,True,True,True,True,True,False,True,False,True,False,False,False,True,False,True,True,True,False,False,False,False,True,False,False,True,False,True,False,False,False,True,True,True,False,False,True,True,True,True,False],[False,True,False,True,True,True,False,False,True,False,True,False,True,True,False,True,False,True,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,False,False,True,False,True,True,True,True,False,True,True,False,True,False,False,True,True,False,True,False,True,False,True,True,True,True,True,True,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,False,False,True,True,False,True,False,False],[True,False,True,False,True,False,True,False,True,False,True,False,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True,True,False,True,False,True,False,True,False,False,False,True,True,False,False,False,True,False,False,False,False,True,True,True,False,False,True,False,True,True,False,True,True,True,False,True,False,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,False,False,True,False,False],[False,False,False,False,True,True,True,False,True,False,False,False,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,True,True,False,True,True,True,False,False,True,True,False,True,False,True,True,False,True,True,True,True,True,True,True,False,False,True,False,True,False,False,False,True,True,False,False,False,True,False,False,False,True,True,True,True,False,True,True,False,False,False,True,True,True,False]], dtype = "bool")#candidate|6544|(9, 84)|const|bool
call_6542 = func_1496_call(relay.reshape(const_6543.astype('bool'), []), relay.reshape(const_6544.astype('bool'), [12, 9, 7]), )
call_6545 = func_1496_call(relay.reshape(const_6543.astype('bool'), []), relay.reshape(const_6544.astype('bool'), [12, 9, 7]), )
uop_6566 = relay.asinh(const_6544.astype('float64')) # shape=(9, 84)
output = relay.Tuple([call_6534,call_6539,var_6540,call_6542,const_6543,uop_6566,])
output2 = relay.Tuple([call_6535,call_6541,var_6540,call_6545,const_6543,uop_6566,])
F = relay.Function([var_6540,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6540,], output2)
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
