import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_112 = relay.var("var_112", dtype = "int64", shape = (6, 7, 14))#candidate|112|(6, 7, 14)|var|int64
var_113 = relay.var("var_113", dtype = "int64", shape = (6, 7, 14))#candidate|113|(6, 7, 14)|var|int64
bop_114 = relay.not_equal(var_112.astype('bool'), relay.reshape(var_113.astype('bool'), relay.shape_of(var_112))) # shape=(6, 7, 14)
output = bop_114
output2 = bop_114
func_123 = relay.Function([var_112,var_113,], output)
mod['func_123'] = func_123
mod = relay.transform.InferType()(mod)
mutated_mod['func_123'] = func_123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_123_call = mutated_mod.get_global_var('func_123')
var_125 = relay.var("var_125", dtype = "int64", shape = (6, 7, 14))#candidate|125|(6, 7, 14)|var|int64
var_126 = relay.var("var_126", dtype = "int64", shape = (6, 7, 14))#candidate|126|(6, 7, 14)|var|int64
call_124 = func_123_call(var_125,var_126,)
output = call_124
func_127 = relay.Function([var_125,var_126,], output)
mutated_mod['func_127'] = func_127
mutated_mod = relay.transform.InferType()(mutated_mod)
const_135 = relay.const(-4, dtype = "uint16")#candidate|135|()|const|uint16
var_136 = relay.var("var_136", dtype = "uint16", shape = (8, 7, 14))#candidate|136|(8, 7, 14)|var|uint16
bop_137 = relay.left_shift(const_135.astype('uint16'), var_136.astype('uint16')) # shape=(8, 7, 14)
uop_145 = relay.sigmoid(var_136.astype('float64')) # shape=(8, 7, 14)
func_123_call = mod.get_global_var('func_123')
func_127_call = mutated_mod.get_global_var('func_127')
var_151 = relay.var("var_151", dtype = "int64", shape = (588,))#candidate|151|(588,)|var|int64
call_150 = func_123_call(relay.reshape(var_151.astype('int64'), [6, 7, 14]), relay.reshape(var_151.astype('int64'), [6, 7, 14]), )
call_152 = func_123_call(relay.reshape(var_151.astype('int64'), [6, 7, 14]), relay.reshape(var_151.astype('int64'), [6, 7, 14]), )
func_123_call = mod.get_global_var('func_123')
func_127_call = mutated_mod.get_global_var('func_127')
call_157 = func_123_call(relay.reshape(call_150.astype('int64'), [6, 7, 14]), relay.reshape(var_151.astype('int64'), [6, 7, 14]), )
call_158 = func_123_call(relay.reshape(call_150.astype('int64'), [6, 7, 14]), relay.reshape(var_151.astype('int64'), [6, 7, 14]), )
func_123_call = mod.get_global_var('func_123')
func_127_call = mutated_mod.get_global_var('func_127')
call_159 = func_123_call(relay.reshape(call_157.astype('int64'), [6, 7, 14]), relay.reshape(var_151.astype('int64'), [6, 7, 14]), )
call_160 = func_123_call(relay.reshape(call_157.astype('int64'), [6, 7, 14]), relay.reshape(var_151.astype('int64'), [6, 7, 14]), )
output = relay.Tuple([bop_137,uop_145,call_150,var_151,call_157,call_159,])
output2 = relay.Tuple([bop_137,uop_145,call_152,var_151,call_158,call_160,])
func_168 = relay.Function([var_136,var_151,], output)
mod['func_168'] = func_168
mod = relay.transform.InferType()(mod)
mutated_mod['func_168'] = func_168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_168_call = mutated_mod.get_global_var('func_168')
var_170 = relay.var("var_170", dtype = "uint16", shape = (8, 7, 14))#candidate|170|(8, 7, 14)|var|uint16
var_171 = relay.var("var_171", dtype = "int64", shape = (588,))#candidate|171|(588,)|var|int64
call_169 = func_168_call(var_170,var_171,)
output = call_169
func_172 = relay.Function([var_170,var_171,], output)
mutated_mod['func_172'] = func_172
mutated_mod = relay.transform.InferType()(mutated_mod)
var_221 = relay.var("var_221", dtype = "uint32", shape = (1, 4, 5))#candidate|221|(1, 4, 5)|var|uint32
const_222 = relay.const([[[-10,4,-7,3,4],[-8,1,7,10,-7],[-7,7,-7,2,-7],[5,-9,-3,1,-8]],[[2,-8,-7,8,-9],[6,-7,7,-5,-6],[-5,2,-2,-10,10],[8,3,-5,-10,-10]],[[6,-4,-8,7,-9],[8,3,-8,4,8],[6,-4,-3,-9,-1],[-2,4,-2,-7,8]],[[3,10,5,-3,-7],[-10,8,-10,-4,3],[-10,2,1,8,4],[-5,-1,3,4,4]],[[-6,4,8,-4,-5],[-8,2,-8,-6,4],[-2,7,6,1,5],[-3,10,6,3,10]],[[8,4,-8,4,1],[-3,9,-8,9,6],[5,-4,7,10,-3],[8,8,3,4,-1]],[[-7,8,6,10,-5],[9,8,-2,-5,-4],[5,-10,-6,3,10],[7,-10,-3,2,2]]], dtype = "uint32")#candidate|222|(7, 4, 5)|const|uint32
bop_223 = relay.greater(var_221.astype('bool'), const_222.astype('bool')) # shape=(7, 4, 5)
func_123_call = mod.get_global_var('func_123')
func_127_call = mutated_mod.get_global_var('func_127')
const_227 = relay.const([[6,4,-10,4,5,2,-3,2,2,-4,-10,10,4,-3,-3,-2,10,1,-8,1,6,-9,-8,9,-5,-6,-9,-7,2,6,8,-6,-6,8,1,-7,-3,-8,-9,10,9,-9],[4,-3,-5,-2,7,-9,3,8,5,5,-2,-8,9,7,5,6,1,6,8,-6,5,7,3,4,-1,-7,-1,5,4,-7,7,8,3,-3,3,-6,-7,6,8,-9,10,-3],[-2,10,10,6,-1,7,-10,6,2,-10,5,-8,-10,4,-2,3,-5,1,-2,-5,3,8,-6,5,-8,-6,4,8,10,8,-10,7,5,3,5,2,-1,1,7,-5,4,-8],[5,4,9,-7,-2,6,-2,-5,-6,7,9,5,6,1,-1,-8,-4,-2,-2,-3,1,2,-8,-2,-5,-2,-9,-10,-8,4,-9,-8,5,-7,-8,3,-2,5,-3,-6,8,-3],[-6,-3,-6,-6,9,8,-3,-1,7,-10,-9,3,-4,10,-5,-10,-10,5,-9,-8,6,-2,-3,10,9,3,5,-1,2,-10,6,10,-4,-1,8,3,7,3,-10,-2,-2,-8],[10,7,-1,-1,-8,3,7,-7,3,-1,5,2,6,6,-10,7,4,-4,-3,-1,7,3,10,-1,9,-5,7,-2,3,2,-4,7,-5,4,7,8,-1,-8,-2,6,-4,-8],[8,3,-7,9,6,-1,7,10,1,8,3,-5,-6,8,1,8,-5,-3,7,-4,-7,7,-10,-8,7,5,1,-4,-8,-6,8,8,-8,-6,4,10,-6,-7,-4,-9,10,-8],[1,-9,-6,-10,10,10,1,-3,-7,-8,9,-1,-2,-1,-2,5,-5,-4,1,7,-2,-1,4,-9,8,6,-3,-10,7,9,-4,-5,-9,10,-5,-1,-6,1,6,-3,-7,4],[7,-7,7,8,-10,-8,3,9,7,-4,-2,-4,-5,5,-7,-2,-2,1,-4,-1,-1,1,9,2,10,10,3,2,-1,1,-7,4,-1,9,3,10,-10,-10,3,-6,1,6],[-8,-3,-7,-10,-7,-4,-9,-6,4,10,6,-5,-1,-1,5,-6,6,-5,-4,-7,-9,-3,-5,-3,-4,-5,3,9,-10,-8,-8,9,6,6,9,2,4,8,-4,-10,-6,-9],[4,-4,-8,1,-7,-1,6,-4,3,-5,-3,8,-6,6,-3,10,4,-4,-4,-2,5,5,-3,8,-5,4,-6,5,-3,1,-9,5,-4,-8,4,-1,-1,2,-5,9,1,-8],[-8,-6,-8,-8,7,10,4,10,-6,-9,-9,-3,9,-4,7,-7,7,-7,4,9,1,-5,-5,-3,7,-2,-10,9,-8,2,-5,4,6,-4,-9,2,-2,2,-1,10,4,-4],[-6,-6,6,-4,6,-2,9,3,-10,-5,9,2,2,-9,4,3,-6,6,6,4,8,-6,-5,3,3,10,7,3,-3,-8,-4,9,-9,-4,7,-10,-6,-1,7,-6,4,-2],[7,-2,8,7,10,-3,-3,5,7,-4,-4,-3,1,-1,7,-7,1,-3,9,2,-8,-8,4,-10,1,-3,8,-5,-7,-5,-10,-9,2,-7,-3,-8,-5,-9,-2,-7,2,-7]], dtype = "int64")#candidate|227|(14, 42)|const|int64
call_226 = func_123_call(relay.reshape(const_227.astype('int64'), [6, 7, 14]), relay.reshape(const_227.astype('int64'), [6, 7, 14]), )
call_228 = func_123_call(relay.reshape(const_227.astype('int64'), [6, 7, 14]), relay.reshape(const_227.astype('int64'), [6, 7, 14]), )
output = relay.Tuple([bop_223,call_226,const_227,])
output2 = relay.Tuple([bop_223,call_228,const_227,])
func_237 = relay.Function([var_221,], output)
mod['func_237'] = func_237
mod = relay.transform.InferType()(mod)
var_238 = relay.var("var_238", dtype = "uint32", shape = (1, 4, 5))#candidate|238|(1, 4, 5)|var|uint32
output = func_237(var_238)
func_239 = relay.Function([var_238], output)
mutated_mod['func_239'] = func_239
mutated_mod = relay.transform.InferType()(mutated_mod)
const_851 = relay.const([[[1,-3,-9,2,-3,-10,-6,-8,5,-8,-3],[7,-7,4,-9,4,-2,-5,-10,-5,-7,-3],[-8,-6,6,-9,-8,-8,1,1,-1,-7,3],[-4,-10,5,5,-10,10,-6,-1,-3,1,4],[-5,1,-1,9,-2,-7,3,10,2,3,-8],[-8,3,-8,5,6,8,-6,-8,10,-1,4],[1,-3,6,6,-4,2,6,-4,3,-2,9],[-9,4,-9,-8,-10,9,-3,1,8,4,3]],[[-2,-2,8,8,-2,4,-6,-3,-10,-5,-8],[3,-10,5,2,3,-6,1,-6,1,7,6],[-10,10,-3,8,-5,-3,1,8,-7,-7,5],[8,8,1,-7,-9,-7,-9,-5,-4,-10,-5],[4,-4,4,5,-1,3,4,-7,1,10,-6],[-8,7,-1,-8,8,10,4,-3,-5,6,6],[-2,-1,-10,10,-1,8,2,-5,-6,6,-6],[1,-1,-6,2,7,6,6,-10,-3,-9,-10]],[[-10,3,9,3,-10,-7,-1,-10,-4,9,-6],[7,3,8,10,-3,3,8,7,-9,6,-10],[8,1,8,3,7,1,-1,4,-6,-4,4],[3,3,-8,10,5,-9,-10,-8,-2,-7,7],[-1,9,-7,-8,-5,2,-5,-7,8,2,2],[-8,-7,7,5,-1,-4,-6,5,2,5,10],[-6,-6,10,-4,2,-3,4,4,-2,6,7],[-7,-7,6,4,-3,-2,-5,-9,-3,2,-1]],[[-3,-6,1,-3,5,3,-10,6,-5,-6,-10],[-7,3,1,5,-2,8,-7,1,9,1,-1],[-1,7,-6,2,6,-6,-9,-4,10,7,5],[6,4,-5,-9,6,-1,-7,7,-4,9,10],[6,4,-2,-5,7,-5,9,7,-6,8,-7],[-6,-2,-5,-8,-9,-1,-4,6,-9,3,5],[4,7,-5,7,10,4,2,3,6,-8,-8],[9,-2,-8,-2,4,-3,4,-8,7,2,9]],[[3,-6,5,8,-6,7,7,2,8,-5,-9],[-6,10,4,-9,8,7,2,9,7,-9,5],[2,7,-5,9,-1,-2,2,-7,-1,2,-10],[-1,-6,-8,5,-3,3,6,-4,4,2,8],[-2,-7,-9,-2,-5,10,3,6,-1,4,-3],[-2,5,-10,-1,-5,3,-7,-10,1,-6,-7],[-1,9,-6,-6,3,-3,3,9,6,-9,5],[1,-9,-3,5,5,6,8,7,10,3,2]],[[1,-1,5,-3,-8,-10,-9,1,4,10,10],[-2,3,8,-7,1,4,-2,4,1,-2,-10],[-5,-6,8,9,-5,6,-4,3,7,-9,8],[9,-1,-5,-5,-5,-7,-9,7,3,-2,-8],[-3,8,-7,-10,10,-8,-2,-3,9,7,-9],[2,-6,-5,-4,-5,-6,-9,-1,7,-8,2],[7,7,3,3,-10,-7,-10,5,9,-4,-2],[-7,10,4,-8,-10,-4,-4,-10,-1,4,9]],[[2,9,-3,-6,6,7,9,3,-10,6,-9],[2,-7,-4,-1,-6,-8,-2,-8,5,4,-9],[5,-10,-7,8,-7,9,-1,7,-5,-5,-8],[3,7,-1,10,-4,3,10,2,-6,-6,5],[8,-9,4,8,-1,7,9,-9,-7,-3,-8],[-8,1,-9,1,-2,5,5,-7,1,-2,-8],[-8,1,1,-6,9,9,-10,-4,-2,3,10],[-9,9,-5,-10,-3,1,4,9,10,3,-5]],[[8,7,6,1,6,-2,-2,7,1,2,5],[3,5,-10,-3,-5,-4,4,10,7,5,-2],[-8,1,-2,-1,-9,1,-8,-4,7,3,-10],[1,-2,10,8,8,-5,-5,-2,-4,-1,-4],[-5,1,8,3,-2,-1,-5,-6,5,8,3],[-6,10,-5,-2,-1,9,-1,9,-6,8,-9],[-8,-5,9,4,-9,-6,-8,-3,9,-9,7],[5,4,8,9,-7,2,-4,7,2,6,-8]],[[-8,7,4,-6,-8,6,-4,-3,2,4,4],[-3,-3,9,-3,-6,-6,10,10,1,-9,-7],[-3,-10,2,9,1,7,8,-5,-2,4,3],[10,-2,-1,-1,-5,-1,-9,8,-9,1,5],[1,-2,1,3,-10,7,-3,4,-7,8,6],[10,-7,-5,4,-10,7,10,-10,2,-5,1],[-7,3,3,-3,1,3,4,-10,5,5,-2],[10,9,1,2,3,-8,-7,-8,-2,-6,8]],[[-2,-8,8,2,10,3,5,3,-9,-9,3],[-10,6,9,-8,2,5,8,5,5,-4,-7],[6,6,-8,-2,1,-1,3,-7,-9,10,8],[1,-10,1,7,-2,-7,8,-5,8,2,1],[1,8,-6,8,-10,9,7,5,7,-7,-8],[-2,5,7,9,-5,-7,-2,3,6,9,3],[-7,-10,-6,9,-3,-6,-10,8,-2,-10,7],[-1,2,-6,-5,6,9,-4,-2,8,-7,6]],[[9,7,-6,-10,10,5,-9,2,-10,-3,4],[-4,4,4,8,9,1,-9,-4,1,-8,-8],[5,-8,10,-4,3,-1,-9,8,-4,-5,2],[3,2,-2,10,7,1,10,9,6,-1,-8],[-3,-8,-3,1,6,3,-7,8,6,3,-1],[7,-7,3,-9,10,9,-8,-2,2,-4,-8],[2,10,-1,3,6,-3,2,-2,-1,4,10],[-4,2,2,1,-9,-6,-10,2,9,5,10]],[[10,-10,-6,-2,-8,-9,-4,-8,-1,-7,6],[1,3,5,-4,5,8,-6,2,1,4,-10],[-2,-3,-5,-9,-10,-10,-2,10,1,9,-3],[-4,-3,-2,-6,5,-3,1,1,-9,-10,-5],[-4,-8,2,-4,4,-9,4,6,-6,-10,-1],[6,-2,-4,-6,5,-6,4,-2,-5,6,-3],[-9,-2,10,-5,4,-3,-8,9,8,1,10],[-5,4,7,8,-10,-1,-2,-6,-1,8,-7]],[[5,-10,1,-8,-7,-3,5,-10,-2,-9,-5],[-3,10,1,10,-6,-3,7,-8,-7,1,7],[-2,10,9,6,-10,7,2,8,6,-6,-10],[5,1,-2,-3,-8,-6,-6,6,9,10,-8],[3,-4,-1,8,-7,-9,4,-9,-10,2,5],[-9,2,1,-5,4,-6,-5,-3,8,5,-8],[-7,-7,-6,-3,7,-6,-3,2,-5,-3,7],[7,10,-9,1,3,-6,8,-9,5,-4,-6]]], dtype = "int8")#candidate|851|(13, 8, 11)|const|int8
const_852 = relay.const([[[-10,1,-7,3,8,-5,-5,4,-5,-9,2],[6,5,-7,-2,2,-6,-7,5,8,-5,-6],[-6,-2,-7,-7,-3,5,8,-5,-6,2,2],[-6,-9,-10,-9,-5,-9,5,8,-9,9,-10],[-5,-9,6,5,-1,4,-5,-6,-3,1,-8],[9,2,-10,1,8,-9,-7,8,-2,2,1],[-2,-4,-10,8,3,7,-5,-4,6,-2,-9],[-7,-10,-4,-7,-2,3,-4,2,10,-9,-1]],[[-3,3,-9,2,4,2,2,-8,2,8,5],[8,-3,-5,7,-9,2,-10,6,8,-3,8],[8,-4,6,-8,3,-10,-6,9,10,-6,9],[-3,7,-7,-2,8,2,2,2,-1,-6,1],[8,9,-7,10,8,3,3,-8,6,4,-5],[-6,-6,4,-9,-6,-5,5,-10,2,-8,-5],[-6,5,6,9,-6,10,3,-4,1,9,6],[1,-9,-6,-5,-8,-4,2,4,3,8,2]],[[9,6,-7,-5,-1,1,-9,-6,7,-7,9],[-3,3,-3,-9,-4,10,-8,7,9,10,-9],[-6,3,-1,8,-10,-2,-7,7,7,-4,-3],[3,-6,9,2,-6,5,6,10,7,-5,6],[-4,-7,4,10,-4,9,-7,9,-8,-2,4],[2,-3,7,-10,9,-6,8,10,1,-3,5],[1,-9,-8,-6,10,8,7,-9,-10,2,7],[-10,-8,-2,-9,10,2,1,-2,-4,-4,-6]],[[-2,9,-5,8,3,-10,8,3,-8,9,4],[-2,6,-1,-10,5,-1,-4,7,10,-1,-2],[-2,-6,10,2,5,10,-10,6,-7,-4,3],[-5,-9,2,-5,8,-1,-8,10,-5,-4,8],[8,-7,-3,3,8,-8,-5,8,-9,7,-9],[-1,7,-3,10,6,-3,3,2,4,6,-7],[-4,-2,1,3,6,-10,7,-3,-5,5,2],[6,3,-5,1,1,9,8,-3,-10,4,-10]],[[-3,8,-2,8,2,-9,1,6,-6,-7,10],[-4,8,-2,6,-3,-6,9,-5,-1,10,-2],[4,2,4,-4,7,-5,-4,7,-8,-8,-3],[-2,3,-5,-5,-3,4,-10,7,3,2,10],[5,-5,-10,-9,10,-1,-9,6,-3,5,-6],[-8,-7,-8,-8,-6,-10,8,-3,-2,10,-6],[2,-3,2,-4,2,-3,10,-9,-4,1,-5],[-3,-8,1,-10,9,2,-7,-1,-3,1,-2]],[[-9,-9,-6,-6,-1,-1,-6,1,1,6,-3],[8,-3,6,8,7,1,-2,-10,9,-7,-2],[-3,9,-2,-7,-9,10,-5,10,-6,-3,-4],[-3,-3,-6,3,5,3,-1,-10,-2,3,-1],[-10,-4,-9,-1,-1,-7,-9,9,5,9,10],[4,8,9,2,10,2,-8,10,-3,-6,-9],[7,6,-4,1,4,-5,3,-2,5,-7,-5],[-7,-4,5,-3,6,2,2,-8,-1,-8,5]],[[-10,6,-10,-10,8,9,8,-4,10,-10,4],[10,9,-4,-8,10,-9,-1,1,-5,1,-3],[-2,1,-6,6,-5,2,8,10,-9,3,-9],[9,10,-1,2,9,10,5,10,-6,8,10],[-5,1,3,10,-2,3,4,2,-7,-9,-10],[-3,-6,9,6,-9,2,-3,-5,10,-3,-9],[9,3,2,-1,6,7,2,5,7,-8,-5],[-5,-5,10,-10,-9,2,-4,-5,9,10,5]],[[-3,-9,6,1,-10,4,3,-5,4,-1,5],[-3,2,-4,-9,4,9,4,1,-9,-4,-6],[10,2,-7,-2,-8,-5,-6,-3,-5,-1,-10],[-2,-2,4,7,-3,-3,-2,-9,3,9,10],[-4,-2,-1,5,-8,4,1,6,-10,-4,-5],[3,9,1,-3,-5,3,-10,-10,6,6,-10],[10,3,-4,-4,1,2,3,-10,-4,7,-2],[-2,2,2,1,-2,-7,-2,-4,-1,4,-7]],[[-9,-3,-1,4,7,-8,5,-6,-2,-9,7],[-2,-6,6,-10,-6,9,4,2,-5,-4,-8],[3,-7,-4,5,-8,2,4,3,-10,-3,-10],[1,4,1,-7,1,4,-8,-4,2,2,5],[2,7,7,-1,6,-1,5,2,-2,5,-9],[-6,6,5,2,3,8,-5,2,3,7,-2],[-7,-6,5,5,-4,9,9,-9,3,-6,-4],[7,-5,7,6,4,-4,-2,-4,5,8,-10]],[[-7,1,-1,-3,5,4,-2,-4,10,2,2],[3,1,-4,1,9,2,-7,4,-7,-10,3],[-4,10,6,-8,-8,-4,10,-9,3,8,-5],[-8,7,-9,10,10,-8,-6,4,5,-8,10],[-1,10,6,-1,4,-1,-9,-1,4,-1,-4],[1,4,2,6,-9,-3,-3,8,2,-5,5],[5,3,9,-4,-2,5,-10,7,10,-3,6],[2,9,-5,8,10,-8,-3,-8,4,-3,-5]],[[7,-8,-1,-10,4,10,5,-10,7,-6,-3],[-4,7,1,8,-2,-10,-1,-9,8,2,-9],[-3,-10,8,-7,-7,10,-10,4,6,4,6],[9,-4,-9,6,3,-8,2,-1,7,-10,1],[-7,-10,3,-3,9,2,-10,10,-2,7,-6],[-6,-8,6,-9,1,-4,-10,-7,5,4,9],[-2,-10,-2,6,8,8,4,-7,10,10,-9],[2,5,3,-9,-5,-1,-5,4,4,3,9]],[[3,2,-3,9,7,9,-1,3,-5,10,3],[-3,-9,10,-7,9,4,3,-6,-1,-6,-6],[5,8,8,-9,5,8,7,6,-7,-3,-8],[10,3,-8,-4,-7,-4,2,-4,2,3,5],[-10,-5,6,9,8,-2,3,-1,6,9,-4],[-3,3,2,-9,-7,6,7,-4,9,-8,-5],[3,-9,6,1,8,-2,1,-7,9,-1,-8],[8,-9,-5,8,-9,8,9,5,-5,6,-5]],[[1,9,-8,6,3,9,1,-8,-8,1,6],[-1,2,5,5,-4,4,6,-4,-9,6,-8],[3,-9,4,8,-2,10,-7,9,-6,8,-6],[1,9,-8,7,-4,-1,-5,5,-4,2,-10],[-10,-3,-3,8,7,1,9,-3,-5,-1,1],[3,9,4,5,2,-4,4,6,-9,1,-1],[1,-1,2,-7,7,-3,-1,-10,1,-2,9],[-4,-7,-1,7,1,7,-6,-5,4,-5,10]]], dtype = "int8")#candidate|852|(13, 8, 11)|const|int8
bop_853 = relay.minimum(const_851.astype('int8'), relay.reshape(const_852.astype('int8'), relay.shape_of(const_851))) # shape=(13, 8, 11)
func_168_call = mod.get_global_var('func_168')
func_172_call = mutated_mod.get_global_var('func_172')
const_865 = relay.const([7,-7,-8,8,-10,-1,-2,-4,2,-1,-4,7,4,8,-10,-2,-9,-7,-8,6,-4,6,2,6,-5,-6,-7,-1,-9,-1,-8,-3,-3,-5,-9,-10,9,-10,-7,-4,-5,-3,5,5,3,-10,8,7,6,-4,-2,-10,4,2,8,6,-6,4,-3,5,5,-6,-1,-8,-6,3,-9,-8,3,-8,6,4,3,5,-9,1,-6,-8,-1,-3,9,4,1,2,-4,6,-4,-3,-10,-2,-9,-2,-1,1,7,10,3,5,-8,7,9,3,4,2,-4,-3,-9,-7,7,4,-5,-1,8,10,5,7,1,-7,4,6,-4,-1,6,-5,8,-7,2,9,4,-6,-9,2,1,-2,9,-2,-9,-7,-3,-5,10,1,-10,3,-4,-4,10,-10,5,7,-1,6,4,-2,6,7,1,-1,2,6,3,-6,6,-5,9,-5,-2,2,-6,2,-4,-9,9,-10,2,-5,-6,7,9,2,-3,-2,-10,1,-1,-8,-4,-1,-7,-1,7,-3,9,6,3,7,9,-2,-6,-4,8,1,9,4,-3,4,-1,4,8,-7,1,10,5,-8,-7,-5,4,-8,8,-10,4,-2,2,4,-7,2,7,10,6,-3,8,-9,-4,7,6,4,1,7,-1,5,4,-7,-1,-2,-5,-1,3,-7,-6,2,2,-6,-1,8,5,-1,1,9,5,9,6,-4,2,9,-6,2,6,-2,-10,-10,-4,-4,-9,6,-4,-5,-7,-1,-10,6,1,5,3,-4,-10,8,5,10,4,-1,3,1,5,-8,2,3,2,-3,-9,-10,1,-4,3,-2,10,-7,9,2,2,3,5,-9,5,-4,9,5,5,8,-5,-6,6,-7,-1,-1,10,7,1,2,8,-2,3,10,-1,7,1,-1,7,3,7,-3,9,2,-7,-6,4,5,7,9,-6,-4,-10,-5,2,-8,-4,-6,2,1,-6,-8,6,8,-9,-1,-3,-3,9,3,5,-10,2,-2,-8,6,1,-2,9,10,9,4,-8,7,4,9,-1,8,7,-8,2,-8,-7,-10,2,-6,-3,5,5,7,1,-1,-6,-6,1,-7,7,8,6,2,-9,-9,7,2,-5,5,6,10,5,5,7,10,7,-10,5,-3,8,-5,-5,1,7,-7,2,-4,-1,-2,1,4,10,-3,6,9,9,1,2,-5,7,-1,1,-5,-4,-3,-3,-5,1,-7,-5,10,-2,-7,4,5,-5,-2,2,9,8,-1,10,-3,-5,9,9,-3,2,-7,-3,2,9,-4,-3,6,-6,-2,4,-1,-6,-8,-10,7,-10,-10,7,1,-6,-8,10,10,-3,-6,6,6,6,6,-5,-7,7,10,-9,-1,-7,-4,7,7,-4,8,10,9,-10,-1,-8,-1,-8,-1,5,-2,5,1,9,1,-1,-1,-3,-7,7,-9,8,2,-5,5,-8,-2,4,-4,-3,4,4,-5,8,-1,1,10,1,7,6,4,2,7,-1,-1,-6,8,-2,8,-6,5,-10,-7,8,7,-8,7,10,8,-5,-6,3,2,9,-5,10,4,-6,10,-7,-5,-9,4,8,-1,-10,5,-2,-1,6,8,8,3,5,6,-2,6,5,3,4,6,2,9,8,-7,-6,10,8,-7,-9,-2,6,-4,-8,4,-10,7,-4,6,-6,6,-9,-7,-10,-10,9,-9,10,6,10,-1,2,2,4,-8,2,-4,10,8,8,-8,9,-10,1,-6,-5,1,5,-3,-3,9,5,-6,5,-7,-9,-9,-2,-7,4,4,-2,-7,8,6,-1,7,-10,-2,-7,9,-4,4,5,9,-7,-9,7,6,5,9,6,-5,10,-3,-8,5,-1,8,-2,-7,1,8,1,-5,3,-4,1,7,-9,-8,-3,9,-2,9,-5,3,-2,5,-4,-2,4,7,-7,7,-7,1,8,5,6,-5,2,-10,-10,10,5,10,9,-5,4,-10,-6,2,-2,5,-2,-10,10,-9,-5,2,-10,-9,10,5,7,4,10,-9,-2,10,-7,-8,-2,-7,7,-7,2,8,-2,-5,-2,-2,6,3,-6,-1,5,1,-8,6,-8,4,1,-3,9,-1,8,1,5,-1], dtype = "uint16")#candidate|865|(784,)|const|uint16
const_866 = relay.const([5,3,3,2,9,-2,-1,7,5,-3,-6,10,-6,-3,5,1,10,-3,5,4,-5,-9,1,-2,3,-3,-8,-8,7,3,5,-9,8,-8,7,-7,10,9,-1,8,-8,-2,-3,1,2,-1,10,4,9,-10,-5,9,4,-5,-10,-8,-3,5,3,-5,1,-3,-5,10,-10,10,-9,9,10,-8,-6,-9,1,4,-1,10,-6,-7,-2,2,-7,-7,5,10,1,-6,-6,-7,-10,-2,1,-6,-7,-5,10,-2,2,-3,-7,-2,3,-7,-4,10,5,-8,-4,-1,-9,-9,-6,6,-10,6,-4,-6,-8,-7,-9,-10,-9,-1,5,1,10,1,-10,-5,7,-6,2,9,-6,4,-3,10,-5,4,-2,-1,6,-8,10,5,-5,-10,4,6,-6,-7,-5,3,-7,9,4,2,4,6,-3,3,3,-2,-1,-1,9,7,7,3,7,-3,-1,-2,-7,1,1,-6,5,3,8,-4,4,-10,-1,4,4,10,-4,-2,-1,1,-5,6,8,-10,7,-1,5,-1,4,-2,-5,-6,5,2,-9,7,1,-5,-7,3,-9,5,6,8,-3,10,5,9,-4,-5,3,6,-7,2,6,-8,-2,8,-8,9,9,1,5,-3,10,-9,-9,-6,-8,2,4,8,2,-5,4,-4,-3,-6,-5,-7,-6,8,3,-6,2,4,6,3,10,8,4,-5,-9,5,-2,10,9,7,-4,3,-9,-4,-1,-2,-7,-4,-4,-7,-2,6,-7,1,-6,7,9,6,9,4,-6,-10,9,-5,-3,-6,9,8,-10,-1,7,-6,10,-6,-1,10,9,2,3,8,4,-10,6,8,-7,2,-8,10,-10,8,9,1,-7,-3,-2,8,-7,-10,6,-8,-6,-7,-9,-4,-5,2,-2,3,6,2,9,6,8,-8,4,9,6,-6,-5,8,5,-6,-1,-6,5,6,10,9,-8,6,10,-5,1,5,-4,-6,1,5,10,-10,3,-8,-8,3,-1,9,4,10,-7,-1,-8,-9,-8,-10,8,-5,5,-4,-10,8,-5,5,-3,5,1,-3,3,-7,-8,1,-6,7,-10,4,-7,1,1,1,2,6,-4,-2,10,-9,-6,-4,-7,-6,1,8,2,10,-7,7,-1,-5,-1,1,6,-8,10,-9,-3,5,4,-2,3,2,-4,-9,4,-7,1,-4,8,1,6,-7,4,-2,7,9,-5,10,-9,-4,5,8,1,-4,6,9,5,2,9,-10,-8,-6,9,4,-7,1,-4,-9,-2,4,-10,9,-10,-5,-5,-5,3,9,7,9,4,9,10,-2,3,-10,10,8,-2,-9,9,3,-5,-5,-8,10,6,-1,-9,1,-1,-7,-2,-1,10,-5,-3,-5,3,-3,-4,-4,-4,7,7,5,8,-9,9,-9,9,1,4,-10,-6,9,-8,10,-7,-5,-4,-2,-4,-7,10,-3,-1,1,-2,4,6,8,8,5,-5,-10,1,-1,3,-10,-5,-2,-1,4,3,-1,-3,2,7,5,-8,-10,8,-7,-1,-4,2,-1,-8,-6,4,8,8,-7,9,-6,-8,7,-10,-9,-1,-5,10,8], dtype = "int64")#candidate|866|(588,)|const|int64
call_864 = relay.TupleGetItem(func_168_call(relay.reshape(const_865.astype('uint16'), [8, 7, 14]), relay.reshape(const_866.astype('int64'), [588,]), ), 0)
call_867 = relay.TupleGetItem(func_172_call(relay.reshape(const_865.astype('uint16'), [8, 7, 14]), relay.reshape(const_866.astype('int64'), [588,]), ), 0)
func_237_call = mod.get_global_var('func_237')
func_239_call = mutated_mod.get_global_var('func_239')
var_872 = relay.var("var_872", dtype = "uint32", shape = (20,))#candidate|872|(20,)|var|uint32
call_871 = relay.TupleGetItem(func_237_call(relay.reshape(var_872.astype('uint32'), [1, 4, 5])), 1)
call_873 = relay.TupleGetItem(func_239_call(relay.reshape(var_872.astype('uint32'), [1, 4, 5])), 1)
output = relay.Tuple([bop_853,call_864,const_865,const_866,call_871,var_872,])
output2 = relay.Tuple([bop_853,call_867,const_865,const_866,call_873,var_872,])
func_875 = relay.Function([var_872,], output)
mod['func_875'] = func_875
mod = relay.transform.InferType()(mod)
mutated_mod['func_875'] = func_875
mutated_mod = relay.transform.InferType()(mutated_mod)
var_876 = relay.var("var_876", dtype = "uint32", shape = (20,))#candidate|876|(20,)|var|uint32
func_875_call = mutated_mod.get_global_var('func_875')
call_877 = func_875_call(var_876)
output = call_877
func_878 = relay.Function([var_876], output)
mutated_mod['func_878'] = func_878
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1054 = relay.var("var_1054", dtype = "float32", shape = (4, 4, 7))#candidate|1054|(4, 4, 7)|var|float32
uop_1055 = relay.acos(var_1054.astype('float32')) # shape=(4, 4, 7)
func_168_call = mod.get_global_var('func_168')
func_172_call = mutated_mod.get_global_var('func_172')
var_1089 = relay.var("var_1089", dtype = "uint16", shape = (784,))#candidate|1089|(784,)|var|uint16
var_1090 = relay.var("var_1090", dtype = "int64", shape = (588, 1))#candidate|1090|(588, 1)|var|int64
call_1088 = relay.TupleGetItem(func_168_call(relay.reshape(var_1089.astype('uint16'), [8, 7, 14]), relay.reshape(var_1090.astype('int64'), [588,]), ), 4)
call_1091 = relay.TupleGetItem(func_172_call(relay.reshape(var_1089.astype('uint16'), [8, 7, 14]), relay.reshape(var_1090.astype('int64'), [588,]), ), 4)
func_875_call = mod.get_global_var('func_875')
func_878_call = mutated_mod.get_global_var('func_878')
const_1095 = relay.const([8,-4,9,4,7,-6,5,-3,-4,6,7,-10,9,-1,7,-2,2,-4,5,10], dtype = "uint32")#candidate|1095|(20,)|const|uint32
call_1094 = relay.TupleGetItem(func_875_call(relay.reshape(const_1095.astype('uint32'), [20,])), 0)
call_1096 = relay.TupleGetItem(func_878_call(relay.reshape(const_1095.astype('uint32'), [20,])), 0)
output = relay.Tuple([uop_1055,call_1088,var_1089,var_1090,call_1094,const_1095,])
output2 = relay.Tuple([uop_1055,call_1091,var_1089,var_1090,call_1096,const_1095,])
func_1113 = relay.Function([var_1054,var_1089,var_1090,], output)
mod['func_1113'] = func_1113
mod = relay.transform.InferType()(mod)
mutated_mod['func_1113'] = func_1113
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1113_call = mutated_mod.get_global_var('func_1113')
var_1115 = relay.var("var_1115", dtype = "float32", shape = (4, 4, 7))#candidate|1115|(4, 4, 7)|var|float32
var_1116 = relay.var("var_1116", dtype = "uint16", shape = (784,))#candidate|1116|(784,)|var|uint16
var_1117 = relay.var("var_1117", dtype = "int64", shape = (588, 1))#candidate|1117|(588, 1)|var|int64
call_1114 = func_1113_call(var_1115,var_1116,var_1117,)
output = call_1114
func_1118 = relay.Function([var_1115,var_1116,var_1117,], output)
mutated_mod['func_1118'] = func_1118
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1757 = relay.var("var_1757", dtype = "float64", shape = (1, 3, 1))#candidate|1757|(1, 3, 1)|var|float64
const_1758 = relay.const([[[-4.319361,6.569709,2.493875,-0.910988,-3.753302,9.137282,6.533787,7.691965,-6.388074,8.295915,2.170775,9.025973],[7.367592,6.503006,-6.449703,-8.091137,-5.488242,9.428318,-0.608094,-1.395659,-9.785234,9.521854,-5.119357,-4.408282],[5.149869,0.510234,-0.203074,-6.324927,-9.409705,-5.913775,-7.176286,7.810971,-7.937865,-3.863324,-7.221774,3.674604]],[[-3.980861,-0.029265,-8.866555,8.470526,-4.768422,-2.699079,1.344232,-9.343071,-5.929829,-1.044652,9.429528,1.314423],[-8.196001,6.364539,-4.021027,-9.343241,7.410400,-1.164700,5.745495,4.389637,-0.852625,-6.679832,-9.297333,2.478636],[3.207790,2.177557,1.914991,8.555119,-7.291127,-6.062761,8.163158,0.293571,-3.557404,-4.896373,3.773406,7.051390]],[[9.211790,-6.952512,3.371157,-4.894036,5.872413,0.590056,7.047888,9.788669,3.424257,-0.458054,-9.986017,8.080703],[5.709509,-4.557236,4.045661,-2.230314,2.303858,-1.531272,-3.493360,-7.071570,-0.049142,-8.891996,-5.895336,0.622353],[-8.440653,-9.306771,5.358768,7.926093,-1.711930,-9.375380,5.420799,-8.238459,4.983934,1.823623,-8.313347,6.495226]],[[-6.462706,-2.929867,8.219802,-2.896739,6.392435,-0.621767,0.159348,-7.758343,0.536365,4.148968,3.536732,-4.821460],[4.220712,4.638903,1.584969,-9.259967,-0.108236,-9.745826,1.853043,8.259783,2.955443,3.090544,8.418298,-4.250046],[-1.868613,-9.488934,-6.940017,-9.749804,-3.478803,5.905301,5.653780,9.023090,-4.834476,4.921537,7.634366,-5.315091]],[[4.663905,0.336918,8.701453,3.774743,2.567663,-8.128134,-3.784299,3.356265,-5.204408,-7.518290,3.663482,5.596335],[1.556119,9.367901,-8.594555,-9.793133,4.387615,-9.528475,7.808646,8.858051,2.258687,-4.220885,-7.791458,1.332015],[-4.068294,-5.946698,8.802271,6.941081,6.016456,4.573943,8.549198,9.590857,7.731148,2.336052,3.064578,-0.631015]],[[-7.800976,3.759735,-7.290206,6.313629,-5.695531,-0.280547,-9.571590,4.654722,-6.925124,1.408611,-5.785550,4.783854],[-4.848250,-9.001378,5.248025,1.443619,-5.803497,-1.502276,5.523929,4.853099,-0.761130,3.067215,-2.471933,-0.646258],[-5.819880,-0.489044,-1.115336,-1.700602,-3.059418,-4.042955,8.395059,-2.512084,-9.482738,9.710761,-2.929137,-7.217852]],[[-7.518127,2.647981,-0.441017,-5.022194,8.581488,3.597347,-0.952361,1.474876,-0.327016,-1.264835,8.382865,4.144891],[0.891704,2.243918,-1.432613,-8.891324,3.968803,9.145720,2.132314,-2.120082,-1.851830,-9.870026,-0.550625,7.118740],[-1.227313,-2.376786,-0.647355,7.685249,-9.832075,-4.796400,-4.070009,-4.458862,-4.798241,4.927678,8.451408,8.280035]],[[5.204009,-8.411776,2.801048,7.528778,9.382692,4.809522,0.908820,9.633245,5.731663,-3.278649,6.269720,9.365205],[-6.714430,1.727791,6.482230,0.076374,2.069383,-0.372285,-9.003038,-8.219514,5.678670,8.164780,-5.064734,8.331373],[-8.058280,-0.228239,-2.775577,-8.169245,-5.716141,-6.131630,-2.840834,9.545362,8.860954,-0.614341,7.029469,8.909210]]], dtype = "float64")#candidate|1758|(8, 3, 12)|const|float64
bop_1759 = relay.divide(var_1757.astype('float64'), const_1758.astype('float64')) # shape=(8, 3, 12)
bop_1765 = relay.not_equal(bop_1759.astype('bool'), relay.reshape(const_1758.astype('bool'), relay.shape_of(bop_1759))) # shape=(8, 3, 12)
bop_1780 = relay.bitwise_or(bop_1765.astype('uint16'), var_1757.astype('uint16')) # shape=(8, 3, 12)
output = bop_1780
output2 = bop_1780
func_1790 = relay.Function([var_1757,], output)
mod['func_1790'] = func_1790
mod = relay.transform.InferType()(mod)
mutated_mod['func_1790'] = func_1790
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1791 = relay.var("var_1791", dtype = "float64", shape = (1, 3, 1))#candidate|1791|(1, 3, 1)|var|float64
func_1790_call = mutated_mod.get_global_var('func_1790')
call_1792 = func_1790_call(var_1791)
output = call_1792
func_1793 = relay.Function([var_1791], output)
mutated_mod['func_1793'] = func_1793
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1803 = relay.var("var_1803", dtype = "uint64", shape = ())#candidate|1803|()|var|uint64
var_1804 = relay.var("var_1804", dtype = "uint64", shape = (6, 4, 14))#candidate|1804|(6, 4, 14)|var|uint64
bop_1805 = relay.subtract(var_1803.astype('uint64'), var_1804.astype('uint64')) # shape=(6, 4, 14)
output = relay.Tuple([bop_1805,])
output2 = relay.Tuple([bop_1805,])
func_1809 = relay.Function([var_1803,var_1804,], output)
mod['func_1809'] = func_1809
mod = relay.transform.InferType()(mod)
var_1810 = relay.var("var_1810", dtype = "uint64", shape = ())#candidate|1810|()|var|uint64
var_1811 = relay.var("var_1811", dtype = "uint64", shape = (6, 4, 14))#candidate|1811|(6, 4, 14)|var|uint64
output = func_1809(var_1810,var_1811,)
func_1812 = relay.Function([var_1810,var_1811,], output)
mutated_mod['func_1812'] = func_1812
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1861 = relay.const(10, dtype = "int32")#candidate|1861|()|const|int32
const_1862 = relay.const([[[1,10,8],[-10,-9,6],[-2,4,-8],[-3,2,-2],[-6,6,-9],[3,-6,8]],[[2,-2,4],[5,-8,8],[-5,3,-8],[-10,10,-4],[6,-1,-10],[-6,-6,5]],[[8,-6,1],[4,-4,-5],[2,7,-5],[2,-8,-4],[1,-3,10],[-7,-10,-7]],[[-8,10,8],[6,-3,3],[-6,1,-8],[-4,-7,-8],[-7,-7,9],[-1,-7,-8]]], dtype = "int32")#candidate|1862|(4, 6, 3)|const|int32
bop_1863 = relay.greater(const_1861.astype('bool'), const_1862.astype('bool')) # shape=(4, 6, 3)
func_1809_call = mod.get_global_var('func_1809')
func_1812_call = mutated_mod.get_global_var('func_1812')
var_1879 = relay.var("var_1879", dtype = "uint64", shape = (336,))#candidate|1879|(336,)|var|uint64
call_1878 = relay.TupleGetItem(func_1809_call(relay.reshape(const_1861.astype('uint64'), []), relay.reshape(var_1879.astype('uint64'), [6, 4, 14]), ), 0)
call_1880 = relay.TupleGetItem(func_1812_call(relay.reshape(const_1861.astype('uint64'), []), relay.reshape(var_1879.astype('uint64'), [6, 4, 14]), ), 0)
var_1882 = relay.var("var_1882", dtype = "bool", shape = (4, 6, 3))#candidate|1882|(4, 6, 3)|var|bool
bop_1883 = relay.bitwise_or(bop_1863.astype('uint32'), relay.reshape(var_1882.astype('uint32'), relay.shape_of(bop_1863))) # shape=(4, 6, 3)
output = relay.Tuple([call_1878,var_1879,bop_1883,])
output2 = relay.Tuple([call_1880,var_1879,bop_1883,])
func_1891 = relay.Function([var_1879,var_1882,], output)
mod['func_1891'] = func_1891
mod = relay.transform.InferType()(mod)
mutated_mod['func_1891'] = func_1891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1891_call = mutated_mod.get_global_var('func_1891')
var_1893 = relay.var("var_1893", dtype = "uint64", shape = (336,))#candidate|1893|(336,)|var|uint64
var_1894 = relay.var("var_1894", dtype = "bool", shape = (4, 6, 3))#candidate|1894|(4, 6, 3)|var|bool
call_1892 = func_1891_call(var_1893,var_1894,)
output = call_1892
func_1895 = relay.Function([var_1893,var_1894,], output)
mutated_mod['func_1895'] = func_1895
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2139 = relay.var("var_2139", dtype = "int16", shape = ())#candidate|2139|()|var|int16
const_2140 = relay.const([[[5,-9,-10,-4,1,3,-6,9,3],[-6,6,1,-8,-6,-4,4,7,-6],[8,-5,-9,-4,1,10,1,8,-9]]], dtype = "int16")#candidate|2140|(1, 3, 9)|const|int16
bop_2141 = relay.multiply(var_2139.astype('int16'), const_2140.astype('int16')) # shape=(1, 3, 9)
bop_2152 = relay.left_shift(bop_2141.astype('uint64'), var_2139.astype('uint64')) # shape=(1, 3, 9)
bop_2162 = relay.equal(bop_2141.astype('bool'), var_2139.astype('bool')) # shape=(1, 3, 9)
func_1891_call = mod.get_global_var('func_1891')
func_1895_call = mutated_mod.get_global_var('func_1895')
var_2172 = relay.var("var_2172", dtype = "uint64", shape = (336,))#candidate|2172|(336,)|var|uint64
const_2173 = relay.const([False,True,True,True,True,False,False,True,True,False,True,True,False,True,False,True,True,True,False,False,False,True,False,True,True,True,True,False,False,True,True,False,False,False,False,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,True,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False], dtype = "bool")#candidate|2173|(72,)|const|bool
call_2171 = relay.TupleGetItem(func_1891_call(relay.reshape(var_2172.astype('uint64'), [336,]), relay.reshape(const_2173.astype('bool'), [4, 6, 3]), ), 0)
call_2174 = relay.TupleGetItem(func_1895_call(relay.reshape(var_2172.astype('uint64'), [336,]), relay.reshape(const_2173.astype('bool'), [4, 6, 3]), ), 0)
func_1790_call = mod.get_global_var('func_1790')
func_1793_call = mutated_mod.get_global_var('func_1793')
var_2176 = relay.var("var_2176", dtype = "float64", shape = (3,))#candidate|2176|(3,)|var|float64
call_2175 = func_1790_call(relay.reshape(var_2176.astype('float64'), [1, 3, 1]))
call_2177 = func_1790_call(relay.reshape(var_2176.astype('float64'), [1, 3, 1]))
output = relay.Tuple([bop_2152,bop_2162,call_2171,var_2172,const_2173,call_2175,var_2176,])
output2 = relay.Tuple([bop_2152,bop_2162,call_2174,var_2172,const_2173,call_2177,var_2176,])
func_2181 = relay.Function([var_2139,var_2172,var_2176,], output)
mod['func_2181'] = func_2181
mod = relay.transform.InferType()(mod)
var_2182 = relay.var("var_2182", dtype = "int16", shape = ())#candidate|2182|()|var|int16
var_2183 = relay.var("var_2183", dtype = "uint64", shape = (336,))#candidate|2183|(336,)|var|uint64
var_2184 = relay.var("var_2184", dtype = "float64", shape = (3,))#candidate|2184|(3,)|var|float64
output = func_2181(var_2182,var_2183,var_2184,)
func_2185 = relay.Function([var_2182,var_2183,var_2184,], output)
mutated_mod['func_2185'] = func_2185
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2417 = relay.const([[[-1,4,10,-2,8,-7,6,4],[-8,-2,10,4,-5,-1,-1,-1],[-8,4,7,-6,-7,-9,-4,9],[-1,10,3,7,8,-4,-3,-3],[-10,-6,2,-1,4,2,-3,1],[-3,7,-6,3,4,-2,2,5]],[[-2,-10,-4,3,-1,7,7,-9],[-10,6,1,-9,7,-10,-9,-3],[-10,7,-4,-4,-7,-10,-9,-5],[-5,7,2,-1,-1,10,-9,-3],[5,-3,-4,3,-5,6,-2,-7],[1,5,9,-4,10,-2,-6,6]],[[-9,-2,5,2,10,6,-10,1],[6,-7,-3,-7,5,-1,-6,-4],[-7,6,4,2,8,6,-10,9],[4,-10,7,9,7,-4,-7,6],[5,-4,9,-2,3,-5,6,8],[10,-4,-7,10,3,7,-10,-3]],[[-4,-5,2,-2,-5,9,-10,9],[7,6,8,-8,-10,10,7,-7],[8,-5,-7,-9,-3,6,-7,3],[10,-8,7,-9,10,-7,1,-7],[5,-3,-1,7,-1,5,-7,2],[8,-6,-5,-2,-6,-9,2,-8]],[[-9,9,3,4,-8,4,9,-5],[-5,2,7,2,-2,10,10,-8],[1,1,-5,2,5,-3,1,3],[-8,-3,-10,10,-9,-3,10,-9],[1,7,-6,1,4,-8,-1,-10],[-8,8,1,8,-8,-8,-4,-3]],[[9,-3,10,8,8,-8,1,-10],[2,-6,3,2,7,-4,-9,8],[-7,-4,-4,1,-2,-1,-9,-9],[8,-4,1,4,8,-9,-7,6],[7,-10,-4,-5,4,-9,-8,5],[-6,-8,-5,-5,2,-9,-2,-2]]], dtype = "int8")#candidate|2417|(6, 6, 8)|const|int8
var_2418 = relay.var("var_2418", dtype = "int8", shape = (6, 6, 8))#candidate|2418|(6, 6, 8)|var|int8
bop_2419 = relay.minimum(const_2417.astype('int8'), relay.reshape(var_2418.astype('int8'), relay.shape_of(const_2417))) # shape=(6, 6, 8)
output = relay.Tuple([bop_2419,])
output2 = relay.Tuple([bop_2419,])
func_2430 = relay.Function([var_2418,], output)
mod['func_2430'] = func_2430
mod = relay.transform.InferType()(mod)
mutated_mod['func_2430'] = func_2430
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2431 = relay.var("var_2431", dtype = "int8", shape = (6, 6, 8))#candidate|2431|(6, 6, 8)|var|int8
func_2430_call = mutated_mod.get_global_var('func_2430')
call_2432 = func_2430_call(var_2431)
output = call_2432
func_2433 = relay.Function([var_2431], output)
mutated_mod['func_2433'] = func_2433
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3331 = relay.var("var_3331", dtype = "int8", shape = ())#candidate|3331|()|var|int8
var_3332 = relay.var("var_3332", dtype = "int8", shape = (1, 14, 2))#candidate|3332|(1, 14, 2)|var|int8
bop_3333 = relay.greater(var_3331.astype('bool'), var_3332.astype('bool')) # shape=(1, 14, 2)
func_1891_call = mod.get_global_var('func_1891')
func_1895_call = mutated_mod.get_global_var('func_1895')
const_3346 = relay.const([-4,-10,3,2,-3,-5,9,-8,5,-1,-4,-5,-5,2,-4,1,-9,-1,-10,4,-1,-8,-5,3,10,-7,9,9,-10,-1,2,-2,-5,-5,8,-8,-8,-1,-1,-5,8,-7,-3,5,1,-10,8,-6,-5,-7,2,-5,-10,-3,1,-5,-1,-10,-3,10,2,7,-1,2,3,10,5,-6,-2,-9,9,5,-6,-4,9,3,3,-1,2,-10,-5,10,8,6,-5,4,-8,-3,2,-5,1,-4,9,-9,-1,8,1,-7,-4,-8,9,-6,-9,-5,-6,3,2,4,-3,2,3,-1,8,3,4,-4,1,1,-8,-2,1,-6,5,2,-4,-3,4,1,-3,-7,-4,-9,2,-9,-8,-7,-8,-10,4,2,-8,-4,8,-8,8,7,8,-8,-6,1,10,3,-4,3,-6,-5,-8,9,-6,7,2,-7,10,9,4,9,1,-2,-6,-2,-7,-7,9,3,2,-9,-5,-3,4,10,5,2,3,10,8,-2,-8,-2,-6,2,8,-10,-8,8,6,-9,-9,-6,4,2,7,-9,-4,4,7,-7,7,-7,-2,-6,5,9,8,-4,3,-4,-1,-5,-3,2,3,4,7,-5,-6,-7,-8,-3,-6,-9,-7,7,-8,-1,-1,3,-4,-4,-8,-2,-3,5,9,-8,-9,2,-3,-1,3,-4,-7,-8,5,4,2,10,-4,7,-7,8,3,1,3,7,-6,-10,-9,5,-10,-9,-4,-10,-8,-4,1,10,-4,-9,2,10,-8,-2,9,-1,6,-3,-1,-9,-9,3,-4,3,-3,-4,-10,-3,-7,5,2,-6,8,-9,2,7,10,9,-2,-4,7,-7,4,-7,-7,-8,-8,7,2,4,-3,-5,-2,9,-9,6,2,-6,5,7,6,1,8,2,2,-7,-9,-8], dtype = "uint64")#candidate|3346|(336,)|const|uint64
const_3347 = relay.const([[False,False,True,False,True,True,True,False,False,True,True,False],[False,True,False,True,False,True,False,False,False,False,False,True],[False,True,False,False,True,True,False,True,True,True,True,True],[True,True,True,True,False,False,True,True,True,False,False,True],[True,False,True,True,False,False,False,True,True,True,True,True],[False,True,False,False,False,False,True,True,True,False,False,True]], dtype = "bool")#candidate|3347|(6, 12)|const|bool
call_3345 = relay.TupleGetItem(func_1891_call(relay.reshape(const_3346.astype('uint64'), [336,]), relay.reshape(const_3347.astype('bool'), [4, 6, 3]), ), 0)
call_3348 = relay.TupleGetItem(func_1895_call(relay.reshape(const_3346.astype('uint64'), [336,]), relay.reshape(const_3347.astype('bool'), [4, 6, 3]), ), 0)
output = relay.Tuple([bop_3333,call_3345,const_3346,const_3347,])
output2 = relay.Tuple([bop_3333,call_3348,const_3346,const_3347,])
func_3356 = relay.Function([var_3331,var_3332,], output)
mod['func_3356'] = func_3356
mod = relay.transform.InferType()(mod)
mutated_mod['func_3356'] = func_3356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3356_call = mutated_mod.get_global_var('func_3356')
var_3358 = relay.var("var_3358", dtype = "int8", shape = ())#candidate|3358|()|var|int8
var_3359 = relay.var("var_3359", dtype = "int8", shape = (1, 14, 2))#candidate|3359|(1, 14, 2)|var|int8
call_3357 = func_3356_call(var_3358,var_3359,)
output = call_3357
func_3360 = relay.Function([var_3358,var_3359,], output)
mutated_mod['func_3360'] = func_3360
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3491 = relay.var("var_3491", dtype = "float64", shape = (4, 4, 2))#candidate|3491|(4, 4, 2)|var|float64
uop_3492 = relay.log10(var_3491.astype('float64')) # shape=(4, 4, 2)
uop_3495 = relay.log(uop_3492.astype('float32')) # shape=(4, 4, 2)
bop_3497 = relay.greater(var_3491.astype('bool'), relay.reshape(uop_3495.astype('bool'), relay.shape_of(var_3491))) # shape=(4, 4, 2)
bop_3502 = relay.power(uop_3495.astype('float64'), relay.reshape(uop_3492.astype('float64'), relay.shape_of(uop_3495))) # shape=(4, 4, 2)
func_123_call = mod.get_global_var('func_123')
func_127_call = mutated_mod.get_global_var('func_127')
var_3509 = relay.var("var_3509", dtype = "int64", shape = (98, 6))#candidate|3509|(98, 6)|var|int64
call_3508 = func_123_call(relay.reshape(var_3509.astype('int64'), [6, 7, 14]), relay.reshape(var_3509.astype('int64'), [6, 7, 14]), )
call_3510 = func_123_call(relay.reshape(var_3509.astype('int64'), [6, 7, 14]), relay.reshape(var_3509.astype('int64'), [6, 7, 14]), )
func_1809_call = mod.get_global_var('func_1809')
func_1812_call = mutated_mod.get_global_var('func_1812')
var_3512 = relay.var("var_3512", dtype = "uint64", shape = ())#candidate|3512|()|var|uint64
var_3513 = relay.var("var_3513", dtype = "uint64", shape = (336,))#candidate|3513|(336,)|var|uint64
call_3511 = relay.TupleGetItem(func_1809_call(relay.reshape(var_3512.astype('uint64'), []), relay.reshape(var_3513.astype('uint64'), [6, 4, 14]), ), 0)
call_3514 = relay.TupleGetItem(func_1812_call(relay.reshape(var_3512.astype('uint64'), []), relay.reshape(var_3513.astype('uint64'), [6, 4, 14]), ), 0)
output = relay.Tuple([bop_3497,bop_3502,call_3508,var_3509,call_3511,var_3512,var_3513,])
output2 = relay.Tuple([bop_3497,bop_3502,call_3510,var_3509,call_3514,var_3512,var_3513,])
func_3527 = relay.Function([var_3491,var_3509,var_3512,var_3513,], output)
mod['func_3527'] = func_3527
mod = relay.transform.InferType()(mod)
var_3528 = relay.var("var_3528", dtype = "float64", shape = (4, 4, 2))#candidate|3528|(4, 4, 2)|var|float64
var_3529 = relay.var("var_3529", dtype = "int64", shape = (98, 6))#candidate|3529|(98, 6)|var|int64
var_3530 = relay.var("var_3530", dtype = "uint64", shape = ())#candidate|3530|()|var|uint64
var_3531 = relay.var("var_3531", dtype = "uint64", shape = (336,))#candidate|3531|(336,)|var|uint64
output = func_3527(var_3528,var_3529,var_3530,var_3531,)
func_3532 = relay.Function([var_3528,var_3529,var_3530,var_3531,], output)
mutated_mod['func_3532'] = func_3532
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3899 = relay.const([[[4.714281,7.829093,7.850422,-5.367205,1.256264,-3.829937,2.386992,-9.864590,2.211130,-8.411980,-3.878598,-8.953824,1.809707,-7.159690,2.871236,-2.616912],[8.542526,0.140744,5.127523,-9.287873,-1.684552,-5.912695,-8.282993,2.714345,7.094532,9.748598,-2.999881,0.357785,9.994946,-3.957096,4.340631,2.744218],[-1.286199,6.132692,8.152762,-8.018787,4.155266,0.488673,-1.972889,3.013640,-7.027255,0.754552,-5.477651,-3.003508,-6.715035,-2.353751,-3.171689,3.760607],[1.818067,-9.631610,-7.347040,-3.817796,5.056583,5.669248,-9.120486,5.630654,6.401458,-2.087777,3.595863,-0.683761,7.591942,3.932703,-0.568537,-9.578202],[-9.238177,-7.004662,8.483945,-2.481048,-6.560857,-1.534443,-8.620012,-5.668869,1.182671,5.764723,1.208134,-3.668701,-8.452461,-1.599852,-1.438524,-4.213964],[3.817960,-7.877707,5.846016,-1.748168,-3.289603,2.973949,-7.743611,2.368575,-1.596545,8.996834,-0.684672,-7.678434,7.717181,2.880913,4.869756,-9.110529],[1.728546,3.953224,7.070020,-3.953317,2.178835,-5.724335,1.859953,0.674645,-2.187620,-2.353798,-1.297040,-8.432697,0.541056,-7.986076,9.555914,-5.697329]]], dtype = "float32")#candidate|3899|(1, 7, 16)|const|float32
uop_3900 = relay.acos(const_3899.astype('float32')) # shape=(1, 7, 16)
output = uop_3900
output2 = uop_3900
func_3910 = relay.Function([], output)
mod['func_3910'] = func_3910
mod = relay.transform.InferType()(mod)
output = func_3910()
func_3911 = relay.Function([], output)
mutated_mod['func_3911'] = func_3911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3910_call = mod.get_global_var('func_3910')
func_3911_call = mutated_mod.get_global_var('func_3911')
call_3941 = func_3910_call()
call_3942 = func_3910_call()
output = relay.Tuple([call_3941,])
output2 = relay.Tuple([call_3942,])
func_3955 = relay.Function([], output)
mod['func_3955'] = func_3955
mod = relay.transform.InferType()(mod)
mutated_mod['func_3955'] = func_3955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3955_call = mutated_mod.get_global_var('func_3955')
call_3956 = func_3955_call()
output = call_3956
func_3957 = relay.Function([], output)
mutated_mod['func_3957'] = func_3957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3955_call = mod.get_global_var('func_3955')
func_3957_call = mutated_mod.get_global_var('func_3957')
call_3989 = relay.TupleGetItem(func_3955_call(), 0)
call_3990 = relay.TupleGetItem(func_3957_call(), 0)
func_1809_call = mod.get_global_var('func_1809')
func_1812_call = mutated_mod.get_global_var('func_1812')
const_3992 = relay.const(-5, dtype = "uint64")#candidate|3992|()|const|uint64
const_3993 = relay.const([-1,-2,-6,10,-7,-4,-8,-4,-10,8,8,10,-3,1,4,-3,9,-9,-2,-2,4,9,6,2,4,5,7,4,-6,7,9,9,7,-4,7,-2,-3,-2,4,-4,-3,10,4,-9,1,2,-7,-9,-1,7,-8,-10,8,9,-7,10,-1,9,6,-8,3,8,-3,4,7,-3,-10,7,6,-2,8,2,-4,-5,-6,-7,2,-8,-10,8,-6,4,7,-6,7,7,-9,5,9,-4,-2,5,6,-1,-8,8,2,-1,-3,-4,-4,8,-10,-7,-4,6,-1,1,6,8,3,-9,-7,-5,-7,3,-10,5,5,-10,2,-8,-7,-4,3,7,5,-10,-6,5,6,7,10,-5,-5,-7,-1,1,3,8,-7,-1,-1,-7,8,4,-9,-9,2,-5,10,-3,-6,-6,-2,-5,9,3,9,-9,-1,2,-4,10,-6,5,8,7,-4,3,9,-5,5,10,-8,-2,2,1,-6,3,10,8,-6,4,-9,-8,-6,-7,-2,9,-8,9,7,-7,2,5,-10,10,9,7,-2,4,-9,10,-2,1,10,-1,9,7,9,-3,-6,-6,6,1,-10,5,8,9,4,1,10,-10,1,2,9,1,-8,-10,-10,-2,6,10,-5,-5,10,3,-9,1,-8,1,8,-5,-9,-3,-6,1,-4,-7,9,8,-9,1,1,7,5,-1,10,-1,2,1,-1,-9,3,-6,1,4,-2,-9,7,4,-6,6,10,-8,-3,10,9,-1,-9,-7,-10,2,5,6,-9,-1,5,2,7,8,9,6,-9,-2,-7,-1,-9,-10,4,4,6,8,-7,5,-2,-3,-2,9,-9,2,-10,-2,3,3,8,1,-7,3,1,5,4,-2,-1,10,2,6,4,-10,10,6,-3,1,-8,-1], dtype = "uint64")#candidate|3993|(336,)|const|uint64
call_3991 = relay.TupleGetItem(func_1809_call(relay.reshape(const_3992.astype('uint64'), []), relay.reshape(const_3993.astype('uint64'), [6, 4, 14]), ), 0)
call_3994 = relay.TupleGetItem(func_1812_call(relay.reshape(const_3992.astype('uint64'), []), relay.reshape(const_3993.astype('uint64'), [6, 4, 14]), ), 0)
uop_4007 = relay.exp(call_3991.astype('float64')) # shape=(6, 4, 14)
uop_4009 = relay.exp(call_3994.astype('float64')) # shape=(6, 4, 14)
func_2430_call = mod.get_global_var('func_2430')
func_2433_call = mutated_mod.get_global_var('func_2433')
const_4020 = relay.const([9,1,4,7,-1,-3,6,2,-4,-7,-2,9,-3,-6,-10,-4,-10,6,-2,-6,-4,3,4,-7,6,3,2,-6,4,7,4,7,-6,-2,6,1,-4,9,10,6,-9,-3,-10,-8,-10,2,-6,-8,2,3,7,-7,8,10,-1,3,-5,4,5,2,7,-9,-3,-5,8,-2,-2,7,4,-10,-4,-8,1,-8,4,-2,-4,-3,-10,1,-6,3,1,-10,9,-1,-6,4,10,4,2,6,8,4,-8,6,-9,6,10,6,-7,-2,7,-8,10,3,-9,9,-8,5,-1,4,9,1,-5,9,-5,4,-9,-10,-6,2,-4,5,5,10,9,5,5,9,2,-1,-1,10,7,10,3,-1,2,-10,3,6,-7,4,-8,9,1,8,3,1,-7,3,2,8,-7,-4,10,6,10,7,-3,7,-6,-5,2,-1,8,9,-8,-7,-5,9,10,5,5,7,10,-1,10,7,5,-10,-4,4,-6,-10,3,-8,-5,2,-5,-8,-4,1,-7,5,8,7,-4,3,4,-3,-3,8,6,-9,-1,-5,-6,-1,7,-4,-3,7,2,1,5,10,7,-7,-10,-3,3,-7,6,-3,8,-8,-8,2,4,7,7,7,-7,-6,-3,9,-9,-7,6,8,7,5,-8,7,-10,1,-2,-9,5,6,-4,-3,1,8,8,-1,1,-10,5,-10,2,10,10,-10,5,-2,-1,4,3,-7,-7,7,4,-8,7,-2,1,-2,3,7,-10,-1,-4,-10,6,-9], dtype = "int8")#candidate|4020|(288,)|const|int8
call_4019 = relay.TupleGetItem(func_2430_call(relay.reshape(const_4020.astype('int8'), [6, 6, 8])), 0)
call_4021 = relay.TupleGetItem(func_2433_call(relay.reshape(const_4020.astype('int8'), [6, 6, 8])), 0)
output = relay.Tuple([call_3989,const_3992,const_3993,uop_4007,call_4019,const_4020,])
output2 = relay.Tuple([call_3990,const_3992,const_3993,uop_4009,call_4021,const_4020,])
func_4023 = relay.Function([], output)
mod['func_4023'] = func_4023
mod = relay.transform.InferType()(mod)
mutated_mod['func_4023'] = func_4023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4023_call = mutated_mod.get_global_var('func_4023')
call_4024 = func_4023_call()
output = call_4024
func_4025 = relay.Function([], output)
mutated_mod['func_4025'] = func_4025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4023_call = mod.get_global_var('func_4023')
func_4025_call = mutated_mod.get_global_var('func_4025')
call_4044 = relay.TupleGetItem(func_4023_call(), 2)
call_4045 = relay.TupleGetItem(func_4025_call(), 2)
output = relay.Tuple([call_4044,])
output2 = relay.Tuple([call_4045,])
func_4049 = relay.Function([], output)
mod['func_4049'] = func_4049
mod = relay.transform.InferType()(mod)
mutated_mod['func_4049'] = func_4049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4049_call = mutated_mod.get_global_var('func_4049')
call_4050 = func_4049_call()
output = call_4050
func_4051 = relay.Function([], output)
mutated_mod['func_4051'] = func_4051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3955_call = mod.get_global_var('func_3955')
func_3957_call = mutated_mod.get_global_var('func_3957')
call_4079 = relay.TupleGetItem(func_3955_call(), 0)
call_4080 = relay.TupleGetItem(func_3957_call(), 0)
output = relay.Tuple([call_4079,])
output2 = relay.Tuple([call_4080,])
func_4081 = relay.Function([], output)
mod['func_4081'] = func_4081
mod = relay.transform.InferType()(mod)
output = func_4081()
func_4082 = relay.Function([], output)
mutated_mod['func_4082'] = func_4082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3910_call = mod.get_global_var('func_3910')
func_3911_call = mutated_mod.get_global_var('func_3911')
call_4142 = func_3910_call()
call_4143 = func_3910_call()
output = call_4142
output2 = call_4143
func_4144 = relay.Function([], output)
mod['func_4144'] = func_4144
mod = relay.transform.InferType()(mod)
output = func_4144()
func_4145 = relay.Function([], output)
mutated_mod['func_4145'] = func_4145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4081_call = mod.get_global_var('func_4081')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_4173 = relay.TupleGetItem(func_4081_call(), 0)
call_4174 = relay.TupleGetItem(func_4082_call(), 0)
output = relay.Tuple([call_4173,])
output2 = relay.Tuple([call_4174,])
func_4193 = relay.Function([], output)
mod['func_4193'] = func_4193
mod = relay.transform.InferType()(mod)
output = func_4193()
func_4194 = relay.Function([], output)
mutated_mod['func_4194'] = func_4194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4081_call = mod.get_global_var('func_4081')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_4200 = relay.TupleGetItem(func_4081_call(), 0)
call_4201 = relay.TupleGetItem(func_4082_call(), 0)
output = relay.Tuple([call_4200,])
output2 = relay.Tuple([call_4201,])
func_4204 = relay.Function([], output)
mod['func_4204'] = func_4204
mod = relay.transform.InferType()(mod)
output = func_4204()
func_4205 = relay.Function([], output)
mutated_mod['func_4205'] = func_4205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4144_call = mod.get_global_var('func_4144')
func_4145_call = mutated_mod.get_global_var('func_4145')
call_4212 = func_4144_call()
call_4213 = func_4144_call()
func_4144_call = mod.get_global_var('func_4144')
func_4145_call = mutated_mod.get_global_var('func_4145')
call_4223 = func_4144_call()
call_4224 = func_4144_call()
bop_4227 = relay.minimum(call_4212.astype('int8'), relay.reshape(call_4223.astype('int8'), relay.shape_of(call_4212))) # shape=(1, 7, 16)
bop_4230 = relay.minimum(call_4213.astype('int8'), relay.reshape(call_4224.astype('int8'), relay.shape_of(call_4213))) # shape=(1, 7, 16)
func_4193_call = mod.get_global_var('func_4193')
func_4194_call = mutated_mod.get_global_var('func_4194')
call_4233 = relay.TupleGetItem(func_4193_call(), 0)
call_4234 = relay.TupleGetItem(func_4194_call(), 0)
output = relay.Tuple([bop_4227,call_4233,])
output2 = relay.Tuple([bop_4230,call_4234,])
func_4235 = relay.Function([], output)
mod['func_4235'] = func_4235
mod = relay.transform.InferType()(mod)
output = func_4235()
func_4236 = relay.Function([], output)
mutated_mod['func_4236'] = func_4236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4204_call = mod.get_global_var('func_4204')
func_4205_call = mutated_mod.get_global_var('func_4205')
call_4243 = relay.TupleGetItem(func_4204_call(), 0)
call_4244 = relay.TupleGetItem(func_4205_call(), 0)
func_123_call = mod.get_global_var('func_123')
func_127_call = mutated_mod.get_global_var('func_127')
var_4248 = relay.var("var_4248", dtype = "int64", shape = (588,))#candidate|4248|(588,)|var|int64
call_4247 = func_123_call(relay.reshape(var_4248.astype('int64'), [6, 7, 14]), relay.reshape(var_4248.astype('int64'), [6, 7, 14]), )
call_4249 = func_123_call(relay.reshape(var_4248.astype('int64'), [6, 7, 14]), relay.reshape(var_4248.astype('int64'), [6, 7, 14]), )
func_1113_call = mod.get_global_var('func_1113')
func_1118_call = mutated_mod.get_global_var('func_1118')
const_4251 = relay.const([5,6,-4,6,-10,-2,-1,8,3,7,-6,-8,-3,10,-6,-3,-6,8,-2,7,-3,-2,-4,-4,-6,-10,8,-5,-2,4,1,1,-8,9,-3,-1,9,-3,-4,9,-8,2,8,6,-2,10,-10,3,9,-8,-2,9,2,4,8,6,4,-1,5,6,8,3,6,5,-9,8,-4,3,-10,2,2,-4,-5,-3,-2,8,-3,-7,-8,-4,9,-10,-10,9,-2,10,10,-2,-8,-5,-4,-10,3,-5,10,-8,3,2,-1,-3,-5,-8,-6,-9,-7,-5,-7,-7,-2,1,-4,-3,-7,10,9,2,6,-8,-2,9,1,-8,10,-7,10,6,-9,10,-5,3,-2,7,-4,-2,-2,-6,8,-9,1,-1,-6,-4,-8,-10,-3,-7,9,-6,-9,-9,-1,1,-1,8,-8,3,-7,-10,1,10,-2,-2,-2,-6,-7,9,-2,-9,-3,-2,-7,-7,-4,-1,-7,-1,-7,2,1,8,2,10,-2,-6,-8,-5,3,-9,-9,2,-9,-6,5,-6,7,6,3,-3,5,-9,-8,-5,-8,-10,5,2,-6,-2,8,9,2,-5,1,2,-9,-8,5,10,10,-10,-1,-8,-3,-9,-8,6,-4,-7,-1,1,-9,-7,-2,10,6,-6,-4,-3,7,-10,10,5,9,7,10,-9,6,-5,-10,10,-9,-2,-3,2,9,-2,-7,3,8,5,-7,-9,10,-3,1,8,-2,-2,7,4,3,-7,5,-8,1,1,8,2,3,8,-9,-5,7,5,-1,-4,-6,-7,-2,-4,-8,10,6,-4,9,5,8,-8,-7,-1,-3,5,5,-2,6,-9,-2,2,2,7,10,9,1,-3,2,9,10,-9,-5,-1,7,-7,10,9,7,-7,-9,5,6,10,-3,-5,2,-7,5,8,-9,-2,-6,4,8,-10,-8,9,-4,-3,-8,9,2,-5,-7,10,-7,6,-5,7,-4,2,-4,7,10,7,8,-7,4,-7,6,7,-2,-7,7,-4,-10,4,-5,-4,-9,-2,6,7,-1,3,4,1,6,6,-1,-4,-5,5,-9,7,-9,-3,8,9,6,9,3,-9,7,4,-4,-8,-7,10,-1,4,-4,7,8,-3,7,6,1,8,-1,-5,1,3,-6,5,-10,7,5,7,-9,10,2,5,3,1,-8,-8,-10,8,-6,3,-2,-9,4,2,6,-9,-2,-10,-8,1,-7,-4,2,3,6,5,6,-7,-1,6,-3,-4,9,-1,6,2,3,-2,-7,6,-1,-1,4,-9,-7,2,2,-8,-1,8,3,5,-6,-2,4,-6,8,3,-5,8,-9,-3,-6,2,10,-9,9,-8,2,8,9,-10,1,-2,8,-8,10,-8,2,6,-1,4,8,3,-3,6,4,2,3,-2,2,8,1,10,7,3,10,5,1,-10,10,-8,-5,-10,4,7,-1,-8,2,-6,-4,6,8,4,1,6,1,6,4,-4,9,4,8,-2,2,9,9,-9,-7,8,8,-1,-6,5,-4,-10,-2,-3,-8,1,5,5,-5,2,-9,4,-2,6,-2,2,2,7,8,-6,-6,-6,7,6,-8,-8,1,-2,-6,3,-1,-2,-6,-9,-2,3,-2,-1,-2,2,7,7,-1,1,9,-3,-8,5,7,-2,-9,-7,6,7,-6,8,-9,3,5,-5,-9,-5,5,-3,-4,-1,10,1,9,3,-8,-1,7,-7,8,-7,10,4,-9,-10,-3,-5,3,8,3,5,4,8,-10,4,-5,-4,2,-2,6,4,-5,2,-5,7,-4,9,10,9,-10,-9,3,-4,3,6,10,-9,-10,-2,-3,-5,5,5,1,5,-9,10,10,-7,-10,2,-4,6,2,-1,8,4,-9,-9,2,-4,8,3,8,1,-4,9,-4,3,2,2,9,-3,4,-1,-6,7,8,2,-3,-3,5,-6,6,4,-5,-8,-2,-5,3,-3,8,2,2,-2,-6,2,9,-8,-9,-5,-9,-9,5,7,7,-4,-10,2,10,-6,1,8,8,-8,-8,-1,7,-10,-3,10,-7,-6,-1,-6,2,-7,-4,4,-3,-8,5,-10,9,-5,-8,-4,-1,9,-7,-5,9,-2,9,4,6,2], dtype = "uint16")#candidate|4251|(784,)|const|uint16
call_4250 = relay.TupleGetItem(func_1113_call(relay.reshape(call_4243.astype('float32'), [4, 4, 7]), relay.reshape(const_4251.astype('uint16'), [784,]), relay.reshape(var_4248.astype('int64'), [588, 1]), ), 3)
call_4252 = relay.TupleGetItem(func_1118_call(relay.reshape(call_4243.astype('float32'), [4, 4, 7]), relay.reshape(const_4251.astype('uint16'), [784,]), relay.reshape(var_4248.astype('int64'), [588, 1]), ), 3)
func_4023_call = mod.get_global_var('func_4023')
func_4025_call = mutated_mod.get_global_var('func_4025')
call_4254 = relay.TupleGetItem(func_4023_call(), 5)
call_4255 = relay.TupleGetItem(func_4025_call(), 5)
output = relay.Tuple([call_4243,call_4247,var_4248,call_4250,const_4251,call_4254,])
output2 = relay.Tuple([call_4244,call_4249,var_4248,call_4252,const_4251,call_4255,])
func_4269 = relay.Function([var_4248,], output)
mod['func_4269'] = func_4269
mod = relay.transform.InferType()(mod)
mutated_mod['func_4269'] = func_4269
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4270 = relay.var("var_4270", dtype = "int64", shape = (588,))#candidate|4270|(588,)|var|int64
func_4269_call = mutated_mod.get_global_var('func_4269')
call_4271 = func_4269_call(var_4270)
output = call_4271
func_4272 = relay.Function([var_4270], output)
mutated_mod['func_4272'] = func_4272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4081_call = mod.get_global_var('func_4081')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_4290 = relay.TupleGetItem(func_4081_call(), 0)
call_4291 = relay.TupleGetItem(func_4082_call(), 0)
var_4292 = relay.var("var_4292", dtype = "float32", shape = (3, 7, 16))#candidate|4292|(3, 7, 16)|var|float32
bop_4293 = relay.power(call_4290.astype('float64'), var_4292.astype('float64')) # shape=(3, 7, 16)
bop_4296 = relay.power(call_4291.astype('float64'), var_4292.astype('float64')) # shape=(3, 7, 16)
func_2430_call = mod.get_global_var('func_2430')
func_2433_call = mutated_mod.get_global_var('func_2433')
const_4300 = relay.const([7,3,5,-5,-10,-1,9,-9,3,5,-8,4,10,8,1,-9,7,-4,-3,1,1,4,4,-7,9,-10,-6,-4,-8,-6,8,-7,-7,-9,1,-4,2,2,-1,6,2,-4,-2,7,-1,-9,10,5,-9,10,6,2,-9,-7,-5,10,-9,-8,-3,3,7,4,-9,5,-7,8,6,-3,-6,7,3,9,-2,-5,1,10,1,5,6,8,4,7,7,7,2,7,1,-7,2,-7,-9,10,10,-10,5,10,-5,9,8,-7,10,-6,-9,-2,-5,5,6,6,1,2,5,5,-10,-1,-10,9,-2,1,-7,2,3,-6,3,5,-7,3,-1,-1,3,-9,2,-5,4,6,8,-3,-5,10,-10,-5,-1,10,-7,3,3,-4,-2,9,-2,9,-3,3,-5,10,-5,4,-3,8,-5,1,2,5,4,-2,-1,8,-7,-3,-3,8,10,-4,6,5,2,9,1,10,10,-2,4,4,-3,2,10,4,1,2,-1,-7,5,8,2,3,-9,2,7,5,-2,5,-8,-1,6,-4,-4,-1,9,-7,9,-4,5,4,-3,-1,7,-7,5,-1,5,10,-8,-8,-2,7,-5,2,8,-9,6,-6,-5,9,2,1,-7,5,-3,2,10,-9,-2,-2,-8,1,-2,-10,-9,9,10,7,2,-3,-8,2,-6,-10,3,-3,6,8,1,7,6,-1,5,-4,-3,1,3,7,4,2,-3,8,-8,-7,4,-1,9,9,-2,-10,1,6,3,-5,-5,4], dtype = "int8")#candidate|4300|(288,)|const|int8
call_4299 = relay.TupleGetItem(func_2430_call(relay.reshape(const_4300.astype('int8'), [6, 6, 8])), 0)
call_4301 = relay.TupleGetItem(func_2433_call(relay.reshape(const_4300.astype('int8'), [6, 6, 8])), 0)
func_4049_call = mod.get_global_var('func_4049')
func_4051_call = mutated_mod.get_global_var('func_4051')
call_4311 = relay.TupleGetItem(func_4049_call(), 0)
call_4312 = relay.TupleGetItem(func_4051_call(), 0)
func_1113_call = mod.get_global_var('func_1113')
func_1118_call = mutated_mod.get_global_var('func_1118')
const_4321 = relay.const([-2,-1,-3,-2,-6,-5,8,3,-3,-3,3,2,7,-9,-9,-10,-5,-6,4,3,-10,-9,8,-6,-6,-5,-7,2,3,8,-4,-4,1,-9,-8,5,1,-8,7,-1,-1,1,-1,3,6,5,2,-1,1,-8,-2,-9,-8,-3,-9,7,1,9,2,-6,-5,-8,-2,10,7,-4,-10,4,-8,-2,-3,8,-6,8,10,6,-8,-2,3,4,1,-1,-9,-8,3,-5,-10,10,9,-6,3,6,-8,2,2,1,5,4,-8,2,-4,-8,9,10,8,-1,-10,2,5,9,-1,-1,-4,-10,-9,2,1,-8,7,-2,-6,6,8,-3,-6,-2,-3,-3,8,-9,-8,-10,10,3,6,2,6,5,10,9,-2,-2,2,4,-1,-6,-4,9,-4,1,6,1,5,-8,-6,10,-7,-3,-8,-10,-9,-7,5,-7,8,9,3,-10,6,5,6,-9,8,2,8,4,-10,-8,-6,-4,-3,2,10,6,9,-7,-7,-8,6,-10,3,2,4,8,5,6,-2,-5,2,8,3,8,2,4,5,-2,7,-2,4,-10,-2,6,-7,-8,-2,-2,-4,4,6,3,1,2,1,-6,-3,-5,-5,1,-4,2,-7,-1,-5,-6,3,4,9,10,9,-7,4,-9,5,-2,-3,6,-9,1,-2,-6,-10,-10,6,9,8,10,-7,3,-1,4,-9,3,7,-1,5,-5,10,2,-5,-1,-6,-9,10,-7,-6,6,-1,-3,-7,7,-4,4,10,-7,-8,2,-9,-7,10,1,-6,1,-8,-6,-1,-4,7,-8,-8,6,5,-8,-6,3,-2,3,-3,-5,-1,3,-4,-8,7,-10,2,10,3,-2,-4,6,-3,-4,-5,5,-8,1,-7,4,4,-8,-9,4,6,-10,2,8,7,10,-9,-10,-5,-10,10,8,-8,-10,5,-9,-1,3,7,9,-3,5,-7,-10,8,7,-4,3,1,8,-1,-9,8,-6,-5,-6,-5,10,-10,4,-10,7,6,-3,7,-5,8,1,-9,-10,3,3,-1,-9,3,8,-6,7,-6,1,2,2,-1,8,9,4,-6,-9,2,-7,-3,8,9,-3,8,8,1,1,-2,-4,9,-10,-5,-3,9,1,4,-3,-7,-7,2,4,-5,7,-6,-8,-9,3,7,10,-5,-8,-2,-1,9,3,-3,-7,2,8,5,6,-4,7,-6,-9,-9,1,10,-10,1,-4,-10,5,-7,3,-8,-5,9,-6,-10,-7,4,2,-1,-4,-6,7,9,10,-4,9,2,-2,7,-6,-3,-8,3,10,4,6,-2,6,4,9,-8,8,2,1,-2,-8,1,1,-8,10,4,-2,9,-2,-3,-1,-9,1,2,3,-8,-6,-9,-3,-7,10,8,-2,9,10,-4,3,1,-9,3,-7,-4,-9,2,-3,6,-4,3,-3,-9,4,-5,9,10,-9,1,-5,-10,10,-10,-3,-6,5,3,4,3,5,7,-4,-3,4,-10,9,-7,2,-3,6,-1,1,-8,-4,-4,-7,-5,8,5,-10,-2,4,9,5,-10,3,1,-5,-8,-10,-8,-3,-9,10,4,-10,10,-4,-2,3,1,5,-2,2,7,-2,8,-9,6,-2,9,7,-6,10,-9,1,-1,-1,-5,2,-3,-9,10,2,7,-8,-6,6,3,1,1,1,8,-6,5,7,2,10,5,-8,6,9,-1,5,2,-8,-7,8,1,10,-10,3,-4,4,5,-10,-9,2,-5,-6,2,-2,2,-6,-2,8,-3,3,-4,-5,-8,9,-5,9,-7,-6,10,-9,10,7,2,-5,8,2,-7,-2,-5,4,3,9,10,-8,7,-3,3,-8,-5,9,3,5,10,6,-10,5,-6,3,2,-6,-1,6,9,8,-9,9,-8,-3,-4,4,-1,-7,-3,-3,-6,-4,8,-2,5,10,8,-7,6,7,-1,3,-7,-1,5,-5,-2,9,-10,6,-4,3,-8,10,-10,-3,5,-5,8,-3,9,-5,9,-3,-6,8,7,-4,10,8,-1,5,9,-10,-5,10,-1,6,-1,-10,-8,-9,-8,2,8,-1,5,5,-5,10,8,-3,7,10,8,6,-10,3,-9,7,-8,-4], dtype = "uint16")#candidate|4321|(784,)|const|uint16
var_4322 = relay.var("var_4322", dtype = "int64", shape = (588,))#candidate|4322|(588,)|var|int64
call_4320 = relay.TupleGetItem(func_1113_call(relay.reshape(call_4290.astype('float32'), [4, 4, 7]), relay.reshape(const_4321.astype('uint16'), [784,]), relay.reshape(var_4322.astype('int64'), [588, 1]), ), 0)
call_4323 = relay.TupleGetItem(func_1118_call(relay.reshape(call_4290.astype('float32'), [4, 4, 7]), relay.reshape(const_4321.astype('uint16'), [784,]), relay.reshape(var_4322.astype('int64'), [588, 1]), ), 0)
output = relay.Tuple([bop_4293,call_4299,const_4300,call_4311,call_4320,const_4321,var_4322,])
output2 = relay.Tuple([bop_4296,call_4301,const_4300,call_4312,call_4323,const_4321,var_4322,])
func_4325 = relay.Function([var_4292,var_4322,], output)
mod['func_4325'] = func_4325
mod = relay.transform.InferType()(mod)
var_4326 = relay.var("var_4326", dtype = "float32", shape = (3, 7, 16))#candidate|4326|(3, 7, 16)|var|float32
var_4327 = relay.var("var_4327", dtype = "int64", shape = (588,))#candidate|4327|(588,)|var|int64
output = func_4325(var_4326,var_4327,)
func_4328 = relay.Function([var_4326,var_4327,], output)
mutated_mod['func_4328'] = func_4328
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4366 = relay.var("var_4366", dtype = "uint8", shape = (5, 9, 1))#candidate|4366|(5, 9, 1)|var|uint8
var_4367 = relay.var("var_4367", dtype = "uint8", shape = (5, 9, 9))#candidate|4367|(5, 9, 9)|var|uint8
bop_4368 = relay.bitwise_or(var_4366.astype('uint8'), var_4367.astype('uint8')) # shape=(5, 9, 9)
func_875_call = mod.get_global_var('func_875')
func_878_call = mutated_mod.get_global_var('func_878')
const_4374 = relay.const([-2,-3,-1,9,-9,-4,-8,-2,-1,6,-6,-8,3,-3,5,-10,1,8,-10,1], dtype = "uint32")#candidate|4374|(20,)|const|uint32
call_4373 = relay.TupleGetItem(func_875_call(relay.reshape(const_4374.astype('uint32'), [20,])), 4)
call_4375 = relay.TupleGetItem(func_878_call(relay.reshape(const_4374.astype('uint32'), [20,])), 4)
func_1113_call = mod.get_global_var('func_1113')
func_1118_call = mutated_mod.get_global_var('func_1118')
var_4377 = relay.var("var_4377", dtype = "float32", shape = (112,))#candidate|4377|(112,)|var|float32
const_4378 = relay.const([5,10,-6,3,2,6,-3,1,6,8,4,-3,5,-9,-3,8,-6,3,7,-5,-3,-8,-8,6,4,-7,-7,1,-6,-8,7,-8,6,-6,-5,-1,4,5,-10,-7,-4,-3,3,-4,4,-10,9,7,-9,-10,6,5,5,-1,2,9,4,-8,6,8,3,5,7,-1,5,-3,5,10,-9,-4,10,-6,5,-3,-5,5,10,1,-1,4,-4,-6,6,-10,6,-7,-9,-3,8,-7,7,-2,-1,-2,5,-8,-4,1,-8,-6,-5,3,5,-10,1,5,-1,-3,-10,-7,-3,-8,-9,7,-10,-4,-6,-10,-4,-4,-8,-1,6,3,8,-2,5,8,-7,-1,-7,-1,-3,-4,1,-10,-8,10,-4,9,3,5,-1,9,-7,4,-7,-7,-8,-5,-10,8,5,-2,-10,-5,2,8,2,-1,10,-2,-2,7,-1,-7,-9,-7,-4,5,9,5,-7,-5,2,7,3,1,8,3,2,10,-8,6,-7,-4,-1,8,-3,9,10,9,5,9,8,5,-4,1,-2,-4,8,-5,-8,-6,-9,4,1,3,3,-1,3,-3,1,-3,-1,-3,-4,7,-5,-2,-8,-4,-2,-4,8,-8,-1,2,-8,-4,9,-7,8,-6,9,-5,-4,5,-7,-1,-4,8,3,-7,2,-10,-1,-7,-3,1,-10,-6,-7,-10,-1,9,-1,1,4,5,-9,10,-1,10,7,3,-8,-2,1,-9,-3,8,-3,10,-8,7,7,9,2,2,-1,-9,-6,-5,-2,-1,-3,1,-9,5,-3,7,10,9,-5,3,6,4,10,-10,4,-7,2,4,8,-9,4,2,1,-7,-10,2,-10,-9,8,5,1,-10,2,6,-5,-1,-10,4,4,-10,10,2,10,2,-1,1,-1,-6,-7,2,-7,5,-6,1,-10,6,-4,-2,8,-2,3,2,8,-6,2,9,1,-9,2,-6,-2,2,1,-10,-10,-9,-8,6,10,-3,9,2,-5,-6,-2,9,7,9,9,-6,-4,3,-7,-9,2,9,-3,1,5,-7,10,-2,1,-4,3,-9,-4,-10,-1,7,-3,5,9,-6,-3,-1,10,1,-7,2,-4,8,1,-10,8,-8,-6,-7,-10,1,-7,-6,8,-10,2,-6,3,6,-3,-8,6,10,-2,-8,1,4,4,6,-9,8,8,-8,9,5,-10,10,1,-9,8,-5,-7,-6,-1,4,1,-9,-7,8,-1,-7,-7,9,1,-3,3,8,7,2,10,-7,-7,8,5,9,10,-7,5,9,3,-4,9,8,-10,3,-6,9,-9,7,-6,10,-4,-4,-4,-4,-2,3,10,7,-10,10,-5,9,-9,-9,-5,-10,7,-8,7,-8,-10,-2,2,2,2,-8,-4,-2,-3,5,-10,-7,-9,10,4,-6,-2,-7,-8,6,1,-6,3,8,-6,4,-10,-7,-5,-6,8,3,8,2,-9,5,-4,-4,8,-3,-5,-2,-7,3,-5,-2,10,-1,-5,4,3,5,10,-2,-1,3,-1,10,-4,-9,3,4,-7,10,9,-10,-3,10,4,2,-7,3,1,-6,-10,8,8,-5,-8,-9,-10,1,-3,7,-3,5,5,7,-3,1,-8,7,10,3,6,6,2,-9,10,-4,-8,-4,9,7,4,7,8,10,-5,-7,-4,9,2,-10,-6,7,5,7,3,-8,-3,-1,-1,10,-3,-7,9,2,3,-6,-8,5,4,-9,-7,4,-4,-10,5,10,-6,-4,2,6,9,8,-5,-3,6,-6,3,-2,6,-3,-3,-8,10,6,7,1,6,-5,4,-9,-4,-5,8,3,1,-2,8,5,-1,2,-5,-8,-4,-1,3,-1,7,-3,3,-9,-1,-3,3,7,-1,6,1,6,-6,-4,-6,-5,8,10,-1,8,-9,1,10,-8,6,-6,5,-2,8,-10,-8,-9,-1,2,5,-6,-2,8,4,3,-1,4,-3,-9,-2,-3,-3,9,-1,-8,2,3,-2,5,9,3,-9,8,-3,10,5,8,-8,-2,9,-5,7,-2,-3,2,-5,3,-1,-5,-7,2,2,10,8,-9,3,7,-6,-6,5,10,-4,-5,4,-3,-7,-3,-6,9,4,-2,-3,-6], dtype = "uint16")#candidate|4378|(784,)|const|uint16
call_4376 = relay.TupleGetItem(func_1113_call(relay.reshape(var_4377.astype('float32'), [4, 4, 7]), relay.reshape(const_4378.astype('uint16'), [784,]), relay.reshape(call_4373.astype('int64'), [588, 1]), ), 3)
call_4379 = relay.TupleGetItem(func_1118_call(relay.reshape(var_4377.astype('float32'), [4, 4, 7]), relay.reshape(const_4378.astype('uint16'), [784,]), relay.reshape(call_4373.astype('int64'), [588, 1]), ), 3)
uop_4385 = relay.tan(call_4376.astype('float64')) # shape=(588, 1)
uop_4387 = relay.tan(call_4379.astype('float64')) # shape=(588, 1)
func_3527_call = mod.get_global_var('func_3527')
func_3532_call = mutated_mod.get_global_var('func_3532')
var_4389 = relay.var("var_4389", dtype = "float64", shape = (4, 8))#candidate|4389|(4, 8)|var|float64
const_4390 = relay.const(6, dtype = "uint64")#candidate|4390|()|const|uint64
var_4391 = relay.var("var_4391", dtype = "uint64", shape = (168, 2))#candidate|4391|(168, 2)|var|uint64
call_4388 = relay.TupleGetItem(func_3527_call(relay.reshape(var_4389.astype('float64'), [4, 4, 2]), relay.reshape(call_4373.astype('int64'), [98, 6]), relay.reshape(const_4390.astype('uint64'), []), relay.reshape(var_4391.astype('uint64'), [336,]), ), 6)
call_4392 = relay.TupleGetItem(func_3532_call(relay.reshape(var_4389.astype('float64'), [4, 4, 2]), relay.reshape(call_4373.astype('int64'), [98, 6]), relay.reshape(const_4390.astype('uint64'), []), relay.reshape(var_4391.astype('uint64'), [336,]), ), 6)
uop_4393 = relay.acosh(uop_4385.astype('float64')) # shape=(588, 1)
uop_4395 = relay.acosh(uop_4387.astype('float64')) # shape=(588, 1)
func_1809_call = mod.get_global_var('func_1809')
func_1812_call = mutated_mod.get_global_var('func_1812')
call_4397 = relay.TupleGetItem(func_1809_call(relay.reshape(const_4390.astype('uint64'), []), relay.reshape(var_4391.astype('uint64'), [6, 4, 14]), ), 0)
call_4398 = relay.TupleGetItem(func_1812_call(relay.reshape(const_4390.astype('uint64'), []), relay.reshape(var_4391.astype('uint64'), [6, 4, 14]), ), 0)
output = relay.Tuple([bop_4368,call_4373,const_4374,var_4377,const_4378,call_4388,var_4389,const_4390,var_4391,uop_4393,call_4397,])
output2 = relay.Tuple([bop_4368,call_4375,const_4374,var_4377,const_4378,call_4392,var_4389,const_4390,var_4391,uop_4395,call_4398,])
func_4401 = relay.Function([var_4366,var_4367,var_4377,var_4389,var_4391,], output)
mod['func_4401'] = func_4401
mod = relay.transform.InferType()(mod)
var_4402 = relay.var("var_4402", dtype = "uint8", shape = (5, 9, 1))#candidate|4402|(5, 9, 1)|var|uint8
var_4403 = relay.var("var_4403", dtype = "uint8", shape = (5, 9, 9))#candidate|4403|(5, 9, 9)|var|uint8
var_4404 = relay.var("var_4404", dtype = "float32", shape = (112,))#candidate|4404|(112,)|var|float32
var_4405 = relay.var("var_4405", dtype = "float64", shape = (4, 8))#candidate|4405|(4, 8)|var|float64
var_4406 = relay.var("var_4406", dtype = "uint64", shape = (168, 2))#candidate|4406|(168, 2)|var|uint64
output = func_4401(var_4402,var_4403,var_4404,var_4405,var_4406,)
func_4407 = relay.Function([var_4402,var_4403,var_4404,var_4405,var_4406,], output)
mutated_mod['func_4407'] = func_4407
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4463 = relay.const([[[9,10,-2,6,-7,-2],[9,9,7,3,5,7],[-9,4,7,-4,7,-2],[6,-2,6,3,10,-7],[3,6,-2,-5,-8,-3],[-9,3,-10,7,-4,-8],[-3,-6,-4,-9,-2,4],[-7,-7,7,2,-8,2],[-2,5,-7,6,5,-2],[-4,-3,-5,-10,-5,9]],[[-8,10,8,3,2,-5],[10,-9,-3,3,2,-4],[4,-1,-3,-3,-5,-7],[6,2,8,6,-9,5],[4,9,-6,2,9,9],[8,-2,-4,6,9,-5],[-7,8,-6,10,-5,-5],[-4,-10,-4,4,10,5],[-5,1,10,2,1,-5],[-7,6,-4,10,1,10]],[[1,-7,9,5,4,-7],[-6,-4,-1,3,-4,7],[-1,7,-10,-7,-10,-2],[-8,-3,4,7,-9,6],[-9,-7,7,10,-2,10],[-3,-3,-3,2,-1,-4],[-4,-5,-1,2,-10,-3],[-4,3,-10,-8,-3,-8],[7,8,4,4,-4,-1],[-2,2,-2,6,-8,2]],[[3,-4,2,-3,-9,-8],[4,1,3,-2,4,4],[1,-2,9,8,5,-10],[-4,-7,-7,-8,-8,-10],[10,3,-6,-2,7,5],[-9,9,6,2,-6,3],[-7,-4,-9,-4,-6,6],[6,-10,-1,8,-9,3],[-8,-5,7,8,8,-9],[-6,-9,1,-6,-3,-7]],[[-1,-4,2,8,-6,6],[1,-7,6,8,-8,4],[-2,6,9,10,10,2],[3,6,3,1,4,4],[4,1,9,-3,8,-6],[5,-6,-2,-9,-6,-2],[-4,4,-3,-7,-8,-8],[6,10,1,8,4,10],[-2,-10,-1,9,7,5],[-10,8,-3,-9,-8,-10]],[[4,6,3,5,5,4],[-8,-3,-8,7,-1,8],[-1,-10,5,-9,-9,9],[1,7,-9,-1,-6,4],[-3,2,5,-7,-8,-7],[-8,-1,3,8,6,-1],[-6,4,7,6,8,-3],[7,-9,-8,7,3,10],[10,2,-3,4,5,3],[-5,-3,6,-6,-7,-7]],[[3,8,4,4,8,-3],[-8,2,3,7,-4,-3],[-6,3,-7,-8,-6,6],[8,5,5,1,-5,7],[8,-7,4,-5,2,8],[10,-8,4,-8,4,-10],[-3,4,-4,5,-7,-6],[-6,-5,-9,-8,9,-5],[1,-7,7,6,8,8],[-3,6,7,2,5,4]],[[10,-2,7,4,-1,3],[-8,-9,-8,-10,10,-10],[-10,-2,10,8,7,9],[-9,10,-3,9,-1,-10],[5,-10,6,4,2,2],[2,-2,-1,-3,-3,10],[7,7,-8,-6,7,-8],[6,10,7,-10,3,10],[-4,-2,-7,10,2,1],[-4,-2,3,-7,-1,-6]],[[10,-9,-9,-5,-1,9],[9,-1,9,-2,-9,8],[-6,10,2,6,-2,-3],[4,-4,-4,5,4,-8],[-10,-8,7,-10,10,10],[3,-2,-1,-8,2,9],[6,-1,10,5,-10,-10],[10,-9,9,10,3,9],[-8,8,10,6,-1,-8],[8,2,8,-4,9,7]],[[-1,2,-1,-10,9,-9],[-5,-6,-3,9,8,9],[1,-2,-9,10,8,-5],[-4,-7,5,1,2,8],[2,9,7,3,3,10],[-6,3,-2,-4,5,9],[-9,2,8,7,9,9],[3,-6,9,10,6,-9],[2,-5,5,9,-4,5],[2,3,7,-9,-6,-1]],[[-1,-10,4,7,3,5],[4,1,-4,2,-10,9],[-7,-2,-3,7,3,3],[7,5,2,7,3,-7],[-6,-5,2,-6,2,1],[10,-1,5,2,6,1],[9,-7,8,9,1,-2],[8,3,5,-5,-3,-8],[10,2,9,-5,1,-1],[6,-5,-6,3,5,5]]], dtype = "uint16")#candidate|4463|(11, 10, 6)|const|uint16
var_4464 = relay.var("var_4464", dtype = "uint16", shape = (11, 10, 6))#candidate|4464|(11, 10, 6)|var|uint16
bop_4465 = relay.maximum(const_4463.astype('uint16'), relay.reshape(var_4464.astype('uint16'), relay.shape_of(const_4463))) # shape=(11, 10, 6)
func_3955_call = mod.get_global_var('func_3955')
func_3957_call = mutated_mod.get_global_var('func_3957')
call_4502 = relay.TupleGetItem(func_3955_call(), 0)
call_4503 = relay.TupleGetItem(func_3957_call(), 0)
func_168_call = mod.get_global_var('func_168')
func_172_call = mutated_mod.get_global_var('func_172')
var_4505 = relay.var("var_4505", dtype = "uint16", shape = (392, 2))#candidate|4505|(392, 2)|var|uint16
var_4506 = relay.var("var_4506", dtype = "int64", shape = (588,))#candidate|4506|(588,)|var|int64
call_4504 = relay.TupleGetItem(func_168_call(relay.reshape(var_4505.astype('uint16'), [8, 7, 14]), relay.reshape(var_4506.astype('int64'), [588,]), ), 4)
call_4507 = relay.TupleGetItem(func_172_call(relay.reshape(var_4505.astype('uint16'), [8, 7, 14]), relay.reshape(var_4506.astype('int64'), [588,]), ), 4)
func_4023_call = mod.get_global_var('func_4023')
func_4025_call = mutated_mod.get_global_var('func_4025')
call_4508 = relay.TupleGetItem(func_4023_call(), 3)
call_4509 = relay.TupleGetItem(func_4025_call(), 3)
output = relay.Tuple([bop_4465,call_4502,call_4504,var_4505,var_4506,call_4508,])
output2 = relay.Tuple([bop_4465,call_4503,call_4507,var_4505,var_4506,call_4509,])
func_4510 = relay.Function([var_4464,var_4505,var_4506,], output)
mod['func_4510'] = func_4510
mod = relay.transform.InferType()(mod)
mutated_mod['func_4510'] = func_4510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4510_call = mutated_mod.get_global_var('func_4510')
var_4512 = relay.var("var_4512", dtype = "uint16", shape = (11, 10, 6))#candidate|4512|(11, 10, 6)|var|uint16
var_4513 = relay.var("var_4513", dtype = "uint16", shape = (392, 2))#candidate|4513|(392, 2)|var|uint16
var_4514 = relay.var("var_4514", dtype = "int64", shape = (588,))#candidate|4514|(588,)|var|int64
call_4511 = func_4510_call(var_4512,var_4513,var_4514,)
output = call_4511
func_4515 = relay.Function([var_4512,var_4513,var_4514,], output)
mutated_mod['func_4515'] = func_4515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4081_call = mod.get_global_var('func_4081')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_4592 = relay.TupleGetItem(func_4081_call(), 0)
call_4593 = relay.TupleGetItem(func_4082_call(), 0)
output = relay.Tuple([call_4592,])
output2 = relay.Tuple([call_4593,])
func_4600 = relay.Function([], output)
mod['func_4600'] = func_4600
mod = relay.transform.InferType()(mod)
output = func_4600()
func_4601 = relay.Function([], output)
mutated_mod['func_4601'] = func_4601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4023_call = mod.get_global_var('func_4023')
func_4025_call = mutated_mod.get_global_var('func_4025')
call_4602 = relay.TupleGetItem(func_4023_call(), 5)
call_4603 = relay.TupleGetItem(func_4025_call(), 5)
output = relay.Tuple([call_4602,])
output2 = relay.Tuple([call_4603,])
func_4665 = relay.Function([], output)
mod['func_4665'] = func_4665
mod = relay.transform.InferType()(mod)
output = func_4665()
func_4666 = relay.Function([], output)
mutated_mod['func_4666'] = func_4666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4235_call = mod.get_global_var('func_4235')
func_4236_call = mutated_mod.get_global_var('func_4236')
call_4697 = relay.TupleGetItem(func_4235_call(), 1)
call_4698 = relay.TupleGetItem(func_4236_call(), 1)
output = relay.Tuple([call_4697,])
output2 = relay.Tuple([call_4698,])
func_4704 = relay.Function([], output)
mod['func_4704'] = func_4704
mod = relay.transform.InferType()(mod)
output = func_4704()
func_4705 = relay.Function([], output)
mutated_mod['func_4705'] = func_4705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3955_call = mod.get_global_var('func_3955')
func_3957_call = mutated_mod.get_global_var('func_3957')
call_4711 = relay.TupleGetItem(func_3955_call(), 0)
call_4712 = relay.TupleGetItem(func_3957_call(), 0)
func_4325_call = mod.get_global_var('func_4325')
func_4328_call = mutated_mod.get_global_var('func_4328')
var_4719 = relay.var("var_4719", dtype = "float32", shape = (1, 336))#candidate|4719|(1, 336)|var|float32
const_4720 = relay.const([-5,-10,-9,-6,6,-7,-2,1,3,5,-3,4,9,-7,4,-1,-2,-7,-7,-4,-1,-5,5,-5,8,-6,7,8,-6,10,-7,-8,1,-10,10,-3,-6,-4,-6,9,8,-2,-3,-10,-5,2,-1,-1,-8,1,6,9,-4,-2,3,-2,-7,8,5,3,-8,4,-5,-2,-9,-1,8,-8,4,-1,-1,9,-7,10,-5,-4,7,-6,4,-3,2,-7,-5,-3,4,7,-8,5,-5,9,-7,-7,-2,5,1,-8,-4,-5,1,10,-3,3,5,-7,1,2,-1,-2,-2,-1,-9,-5,-6,-3,-10,2,-10,-3,1,7,9,1,8,5,2,-2,4,5,-10,5,-1,-3,2,-8,-7,-8,-4,-8,-4,-2,-8,-9,-4,10,-1,3,-4,3,-2,10,5,10,8,-2,1,-3,10,9,6,-7,-6,1,9,-5,-4,-4,4,-10,10,-7,8,9,-1,2,-10,4,-3,6,-10,5,-8,5,-3,-6,-7,-5,2,2,2,3,-5,10,4,2,-8,8,-5,10,5,10,-1,-6,-7,-8,-2,-3,-8,7,-10,3,-5,4,3,-8,1,4,-3,5,-9,-10,-4,2,-7,-3,9,5,-9,3,-4,-4,-9,7,9,1,-4,10,4,-9,10,-8,-10,-2,3,-2,-6,-1,5,6,-9,1,-8,1,-3,-4,4,2,6,-4,-1,5,-3,2,-6,1,5,-1,2,-4,-4,-8,2,-4,-5,-7,-5,4,3,-5,6,4,-9,-2,-9,-8,7,-3,7,7,-4,-10,9,6,-2,10,-8,-7,9,9,-8,-1,2,-3,-1,-3,-5,3,-7,-3,-9,-6,7,-7,-5,-6,-3,7,3,4,-10,-9,10,-6,-9,7,-4,-9,6,-9,2,3,4,-1,-10,1,4,5,-1,2,-10,2,-1,4,4,-10,9,-2,-5,-2,-7,-7,4,-4,10,9,-4,5,1,-5,-5,1,-10,8,5,-10,-6,5,6,-7,5,10,6,-7,7,1,-10,-7,-9,-4,7,-9,9,-3,3,-3,7,-10,-1,1,2,9,6,10,2,-10,-6,-2,-2,1,-8,-6,10,-9,4,10,-1,5,6,3,-9,-7,-3,-1,-5,-2,1,-7,3,-3,-3,10,1,-1,1,4,-10,-7,1,10,4,-10,-10,-7,2,-10,2,-1,5,9,8,10,-6,1,-6,-5,10,5,-2,-3,-2,-1,2,7,-4,7,-2,1,3,9,-10,-10,-2,2,-7,8,9,4,-1,-3,7,-8,7,1,1,9,-6,4,4,-2,5,10,1,-7,5,9,10,-5,7,4,5,7,-2,9,-1,9,-3,9,-5,6,8,5,3,4,-5,-5,-4,4,-7,4,-4,-1,-3,10,-1,-1,-4,-9,-6,6,-3,-2,5,-5,-8,8,3,10,-4,-8,-9,-5,5,9,-7,1,-5,-9,8,3,-2,-10,2,4,10,-10,1,3,9,7,8,6,-4,6,-8,10,1,6,7,1,4,-8,7,2,5,2,1,7,-4,7,-3,1,-6,9,-8,3,-2,-8,-4,6,4,-3,7,-2,4,-2,-6,-2,1,8], dtype = "int64")#candidate|4720|(588,)|const|int64
call_4718 = relay.TupleGetItem(func_4325_call(relay.reshape(var_4719.astype('float32'), [3, 7, 16]), relay.reshape(const_4720.astype('int64'), [588,]), ), 0)
call_4721 = relay.TupleGetItem(func_4328_call(relay.reshape(var_4719.astype('float32'), [3, 7, 16]), relay.reshape(const_4720.astype('int64'), [588,]), ), 0)
output = relay.Tuple([call_4711,call_4718,var_4719,const_4720,])
output2 = relay.Tuple([call_4712,call_4721,var_4719,const_4720,])
func_4752 = relay.Function([var_4719,], output)
mod['func_4752'] = func_4752
mod = relay.transform.InferType()(mod)
var_4753 = relay.var("var_4753", dtype = "float32", shape = (1, 336))#candidate|4753|(1, 336)|var|float32
output = func_4752(var_4753)
func_4754 = relay.Function([var_4753], output)
mutated_mod['func_4754'] = func_4754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4081_call = mod.get_global_var('func_4081')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_4800 = relay.TupleGetItem(func_4081_call(), 0)
call_4801 = relay.TupleGetItem(func_4082_call(), 0)
output = call_4800
output2 = call_4801
func_4811 = relay.Function([], output)
mod['func_4811'] = func_4811
mod = relay.transform.InferType()(mod)
output = func_4811()
func_4812 = relay.Function([], output)
mutated_mod['func_4812'] = func_4812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4144_call = mod.get_global_var('func_4144')
func_4145_call = mutated_mod.get_global_var('func_4145')
call_4825 = func_4144_call()
call_4826 = func_4144_call()
uop_4832 = relay.asin(call_4825.astype('float64')) # shape=(1, 7, 16)
uop_4834 = relay.asin(call_4826.astype('float64')) # shape=(1, 7, 16)
output = uop_4832
output2 = uop_4834
func_4838 = relay.Function([], output)
mod['func_4838'] = func_4838
mod = relay.transform.InferType()(mod)
output = func_4838()
func_4839 = relay.Function([], output)
mutated_mod['func_4839'] = func_4839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4235_call = mod.get_global_var('func_4235')
func_4236_call = mutated_mod.get_global_var('func_4236')
call_4893 = relay.TupleGetItem(func_4235_call(), 0)
call_4894 = relay.TupleGetItem(func_4236_call(), 0)
uop_4902 = relay.asinh(call_4893.astype('float32')) # shape=(1, 7, 16)
uop_4904 = relay.asinh(call_4894.astype('float32')) # shape=(1, 7, 16)
bop_4920 = relay.divide(uop_4902.astype('float64'), relay.reshape(call_4893.astype('float64'), relay.shape_of(uop_4902))) # shape=(1, 7, 16)
bop_4923 = relay.divide(uop_4904.astype('float64'), relay.reshape(call_4894.astype('float64'), relay.shape_of(uop_4904))) # shape=(1, 7, 16)
output = relay.Tuple([bop_4920,])
output2 = relay.Tuple([bop_4923,])
func_4931 = relay.Function([], output)
mod['func_4931'] = func_4931
mod = relay.transform.InferType()(mod)
output = func_4931()
func_4932 = relay.Function([], output)
mutated_mod['func_4932'] = func_4932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4049_call = mod.get_global_var('func_4049')
func_4051_call = mutated_mod.get_global_var('func_4051')
call_4982 = relay.TupleGetItem(func_4049_call(), 0)
call_4983 = relay.TupleGetItem(func_4051_call(), 0)
output = call_4982
output2 = call_4983
func_4990 = relay.Function([], output)
mod['func_4990'] = func_4990
mod = relay.transform.InferType()(mod)
output = func_4990()
func_4991 = relay.Function([], output)
mutated_mod['func_4991'] = func_4991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4023_call = mod.get_global_var('func_4023')
func_4025_call = mutated_mod.get_global_var('func_4025')
call_5000 = relay.TupleGetItem(func_4023_call(), 4)
call_5001 = relay.TupleGetItem(func_4025_call(), 4)
output = call_5000
output2 = call_5001
func_5021 = relay.Function([], output)
mod['func_5021'] = func_5021
mod = relay.transform.InferType()(mod)
mutated_mod['func_5021'] = func_5021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5021_call = mutated_mod.get_global_var('func_5021')
call_5022 = func_5021_call()
output = call_5022
func_5023 = relay.Function([], output)
mutated_mod['func_5023'] = func_5023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4023_call = mod.get_global_var('func_4023')
func_4025_call = mutated_mod.get_global_var('func_4025')
call_5046 = relay.TupleGetItem(func_4023_call(), 1)
call_5047 = relay.TupleGetItem(func_4025_call(), 1)
output = relay.Tuple([call_5046,])
output2 = relay.Tuple([call_5047,])
func_5054 = relay.Function([], output)
mod['func_5054'] = func_5054
mod = relay.transform.InferType()(mod)
mutated_mod['func_5054'] = func_5054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5054_call = mutated_mod.get_global_var('func_5054')
call_5055 = func_5054_call()
output = call_5055
func_5056 = relay.Function([], output)
mutated_mod['func_5056'] = func_5056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4990_call = mod.get_global_var('func_4990')
func_4991_call = mutated_mod.get_global_var('func_4991')
call_5063 = func_4990_call()
call_5064 = func_4990_call()
output = call_5063
output2 = call_5064
func_5119 = relay.Function([], output)
mod['func_5119'] = func_5119
mod = relay.transform.InferType()(mod)
mutated_mod['func_5119'] = func_5119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5119_call = mutated_mod.get_global_var('func_5119')
call_5120 = func_5119_call()
output = call_5120
func_5121 = relay.Function([], output)
mutated_mod['func_5121'] = func_5121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5054_call = mod.get_global_var('func_5054')
func_5056_call = mutated_mod.get_global_var('func_5056')
call_5137 = relay.TupleGetItem(func_5054_call(), 0)
call_5138 = relay.TupleGetItem(func_5056_call(), 0)
func_5021_call = mod.get_global_var('func_5021')
func_5023_call = mutated_mod.get_global_var('func_5023')
call_5143 = func_5021_call()
call_5144 = func_5021_call()
func_1113_call = mod.get_global_var('func_1113')
func_1118_call = mutated_mod.get_global_var('func_1118')
const_5149 = relay.const([-4.913979,2.944914,-8.156999,-1.166563,6.531343,3.337873,3.714141,-5.117800,-1.006632,-2.894973,7.700880,-9.431486,1.233538,3.787744,9.354445,1.188560,6.213422,-4.820117,-3.442907,-8.129876,5.817170,1.216901,-9.617827,-0.770869,4.359187,-8.310255,6.642981,3.169998,6.552189,5.025708,-9.608594,-3.911021,-9.549717,8.963294,6.064101,-0.358482,4.198417,-5.050449,4.857422,-1.401379,3.481918,-6.839108,-2.625778,5.333053,-7.727653,-5.233334,-9.916146,2.088393,-3.223387,8.928284,-7.674078,-3.503535,9.666126,9.351173,1.506348,8.210858,-5.666055,-0.772211,-7.255616,2.784550,-2.741177,7.551108,-8.439030,3.122563,9.490146,7.785291,-9.372244,-4.744248,-7.062066,6.485005,8.525601,-6.883996,-9.912454,-3.786977,-6.856337,0.291449,-2.021890,4.367346,3.667311,5.686930,5.720002,6.865408,-4.727179,-7.551618,5.165369,0.493380,-5.939133,7.048850,-3.257903,3.373464,8.121676,8.819224,4.820263,-3.114777,-4.677304,-6.418860,-8.855766,4.883759,4.217765,8.887009,5.978893,7.389533,-4.324237,-5.006219,3.247479,-8.117185,7.946846,-2.899904,-4.561429,2.646436,-0.194765,3.521292], dtype = "float32")#candidate|5149|(112,)|const|float32
const_5150 = relay.const([-8,7,-10,-6,-5,-1,7,4,1,8,-6,-6,7,-5,5,-4,8,5,-8,-4,5,-7,7,4,7,-7,-4,-6,-9,5,8,-7,1,-2,-4,-4,-6,-1,2,-10,9,4,2,-4,2,5,9,4,-3,-10,5,-5,-7,-3,-2,-10,10,-2,-5,-3,6,-6,-9,4,9,8,10,-4,-10,7,-7,10,-4,-2,-1,-7,7,1,-6,-8,2,8,9,-10,6,-10,-6,-2,5,9,-3,4,-10,5,-1,-10,9,7,-7,-9,-4,-7,9,1,5,1,-4,7,-9,1,-5,5,6,-4,-8,-5,-9,-3,4,-6,3,9,4,3,-8,5,3,7,-9,4,1,-10,-4,3,-8,-8,-8,-8,5,-6,-8,-8,1,2,-6,9,-8,2,-3,-1,-3,2,8,-6,3,-9,2,-2,3,-5,10,8,5,9,2,9,-9,-1,-10,3,8,2,7,5,10,1,-5,8,-7,-8,-9,8,-7,-8,-5,-10,-10,5,8,1,1,8,1,8,4,-8,-4,-2,7,-7,10,-5,10,10,-9,6,3,10,9,-1,-5,-6,7,-1,8,7,5,-8,10,-5,-9,1,-2,-5,8,-3,-6,3,9,-10,-1,-6,-6,3,4,-5,8,6,-6,10,10,-6,-4,-2,2,-3,6,9,-6,8,-2,-5,-10,2,-6,9,-8,2,5,-9,7,-7,-1,-7,-3,-9,9,-5,8,6,-2,10,1,3,10,-2,-4,-10,-7,6,-3,5,10,2,9,-4,4,-10,9,-2,7,-6,4,8,4,-1,10,8,6,-9,-7,-6,10,7,-1,-8,4,1,-1,-7,-4,9,-4,5,-6,-5,-1,5,8,9,-10,10,-1,10,-2,5,7,2,-3,-1,3,-4,-8,-6,-1,-8,1,7,-10,4,-5,-10,6,-2,-10,10,9,-10,10,-3,-8,-4,-2,-3,-7,6,7,-4,9,2,9,5,-3,-6,8,8,2,-6,-2,-7,-5,10,-1,5,-10,-9,8,-8,-8,5,-4,3,4,2,-10,2,-2,-7,9,-2,8,10,7,6,4,3,-4,-6,8,4,-7,-3,-1,3,-4,-8,8,10,-8,3,10,10,4,4,-5,10,-5,10,-5,3,-8,4,9,-5,2,8,6,8,5,-2,10,-2,-4,10,-5,-1,-6,-3,8,-3,-6,4,9,1,-6,6,-6,-1,-1,2,-4,3,7,-4,-3,-7,7,2,5,-2,8,-9,6,-5,-8,5,7,1,-3,10,3,-5,-1,8,10,-9,8,1,5,-1,2,-7,3,2,5,3,9,10,-5,-6,-8,5,2,-10,-3,-3,8,-3,-8,-10,-9,2,-1,10,9,-2,2,3,-5,-2,-7,-5,-5,-7,-7,5,-9,8,7,5,3,-3,9,10,10,-4,8,-1,10,-5,6,-5,-9,5,10,-4,-1,7,-4,4,10,2,-9,-1,4,8,-6,-6,-5,-2,5,7,4,6,2,5,-9,-9,9,-9,-4,4,-1,6,1,2,-6,2,4,10,-7,7,-2,-6,4,6,6,1,-8,5,7,-7,-8,-4,6,-10,9,-3,-2,3,-6,-8,-9,-10,-6,-8,4,-5,-6,-7,-3,7,2,2,-9,-4,4,-7,-8,1,4,6,-5,-2,-10,-3,-6,4,2,-6,2,8,-1,-10,4,5,-9,7,10,6,10,2,4,6,1,-7,-1,9,-1,-10,-8,-6,6,2,-5,-7,-10,1,-2,-9,8,-3,2,10,1,-10,-7,-6,10,-8,-8,9,3,-3,-8,7,8,-6,4,-6,8,-1,-2,7,-7,-6,1,5,9,8,-10,-5,6,1,-7,-2,2,-9,2,-6,-2,-4,-2,-6,6,-8,10,-7,7,6,-4,7,6,10,-2,7,-1,-7,-1,-1,9,-3,7,5,7,-5,4,7,-8,7,5,1,6,-6,1,6,-1,8,9,1,7,-9,10,8,-4,7,1,-5,6,-6,3,6,2,-3,7,9,1,-4,3,-8,-9,6,3,-8,5,7,-7,3,6,2,-1,7,8,-5,-3,10,10,-3,1,3,5,-5,2,2,3,9,-7,-8,-8,-8,5,-5,7,-7], dtype = "uint16")#candidate|5150|(784,)|const|uint16
const_5151 = relay.const([-4,9,-7,-5,-9,4,-2,4,6,2,7,3,2,9,-6,-1,-1,8,-3,8,3,8,3,-7,8,-2,-7,-6,-4,-10,3,1,-4,-1,-3,-7,-1,4,-8,2,8,-10,10,4,3,4,-5,-10,-3,-6,-10,-5,-7,-8,7,3,-5,-10,1,8,-10,-9,-5,-6,10,7,2,-4,8,-5,9,2,-5,8,8,1,8,5,-7,-4,-2,8,2,4,-1,6,-9,5,-3,-1,10,-9,9,2,4,4,6,1,-3,1,-5,5,7,9,6,-1,1,-5,-3,-8,-2,6,-6,9,3,5,-6,4,-4,-3,5,5,5,6,-6,6,9,-7,8,-6,5,-9,-6,6,9,8,-5,-10,4,8,-2,-9,8,-8,3,7,7,-9,-10,1,-4,3,-4,10,1,-10,-2,-4,9,7,5,-8,-2,7,3,1,-9,-9,-9,2,6,-3,-5,9,8,-3,-1,-9,-1,-7,4,-2,-4,7,9,-3,5,3,2,3,-9,-7,1,-5,10,-5,-2,9,-9,9,-8,-2,8,-1,9,-4,-2,3,5,-4,-2,1,-9,9,-7,-7,-1,-5,6,1,2,8,-4,-5,-10,6,-1,5,-9,7,3,2,3,-2,5,-6,9,-3,2,-6,9,4,10,10,-6,-7,1,2,9,2,-9,3,10,-5,-5,7,-2,6,2,5,-2,-6,2,-4,-4,-6,-5,-3,6,9,6,7,-9,-3,-8,-9,-1,-1,5,-5,-4,-1,10,5,-1,-7,-2,-8,7,4,-10,-6,-9,5,6,4,10,10,1,-8,-4,1,9,-9,-1,-4,5,1,8,-10,5,-4,-3,-7,-2,9,9,-1,1,9,-2,-2,-2,1,-8,-2,-8,10,-1,-8,-1,8,-8,10,-9,-1,1,-8,-6,-3,-1,-7,-1,10,3,4,4,-4,1,2,-5,10,6,-9,6,-7,6,4,1,9,2,8,5,8,7,5,5,-10,-3,1,10,6,2,-3,-6,6,8,-3,7,-1,3,8,3,-7,6,8,8,4,-6,4,1,-9,6,-4,-5,-9,2,4,-3,2,3,-7,-5,-2,8,-4,-5,-10,7,6,-10,8,-10,5,-7,5,8,10,5,-6,-9,-3,-5,7,-8,4,6,8,-8,1,4,5,2,-7,1,-9,4,-3,5,-3,-3,-1,-2,-6,5,-6,-5,-1,10,1,1,-10,-2,-6,-4,-1,9,-7,4,1,-9,8,-2,1,9,3,-4,7,-9,4,-3,2,9,-4,1,4,-4,5,3,10,-8,4,-6,-7,-5,8,-7,1,-10,-1,-10,-2,-7,-10,3,-4,3,-4,-10,-5,3,2,-6,6,-6,8,1,-10,-8,-1,-2,-3,-3,-5,-1,8,6,6,3,-9,-8,-6,-8,7,1,-7,3,8,-1,10,7,-6,8,-6,-3,-9,-5,-1,-3,7,6,-7,-5,4,-9,-8,2,9,7,10,-4,10,-4,-10,-9,1,2,4,-4,-3,-5,-9,-4,-9,-8,10,6,9,3,10,-8,-9,10,8,-6,-7,2,9,8,9,-7,-6,-3,6,6,-9,-7,-5], dtype = "int64")#candidate|5151|(588,)|const|int64
call_5148 = relay.TupleGetItem(func_1113_call(relay.reshape(const_5149.astype('float32'), [4, 4, 7]), relay.reshape(const_5150.astype('uint16'), [784,]), relay.reshape(const_5151.astype('int64'), [588, 1]), ), 5)
call_5152 = relay.TupleGetItem(func_1118_call(relay.reshape(const_5149.astype('float32'), [4, 4, 7]), relay.reshape(const_5150.astype('uint16'), [784,]), relay.reshape(const_5151.astype('int64'), [588, 1]), ), 5)
bop_5157 = relay.greater_equal(call_5137.astype('bool'), const_5151.astype('bool')) # shape=(588,)
bop_5160 = relay.greater_equal(call_5138.astype('bool'), const_5151.astype('bool')) # shape=(588,)
func_4990_call = mod.get_global_var('func_4990')
func_4991_call = mutated_mod.get_global_var('func_4991')
call_5163 = func_4990_call()
call_5164 = func_4990_call()
output = relay.Tuple([call_5143,call_5148,const_5149,const_5150,bop_5157,call_5163,])
output2 = relay.Tuple([call_5144,call_5152,const_5149,const_5150,bop_5160,call_5164,])
func_5171 = relay.Function([], output)
mod['func_5171'] = func_5171
mod = relay.transform.InferType()(mod)
output = func_5171()
func_5172 = relay.Function([], output)
mutated_mod['func_5172'] = func_5172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5171_call = mod.get_global_var('func_5171')
func_5172_call = mutated_mod.get_global_var('func_5172')
call_5196 = relay.TupleGetItem(func_5171_call(), 2)
call_5197 = relay.TupleGetItem(func_5172_call(), 2)
output = relay.Tuple([call_5196,])
output2 = relay.Tuple([call_5197,])
func_5229 = relay.Function([], output)
mod['func_5229'] = func_5229
mod = relay.transform.InferType()(mod)
mutated_mod['func_5229'] = func_5229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5229_call = mutated_mod.get_global_var('func_5229')
call_5230 = func_5229_call()
output = call_5230
func_5231 = relay.Function([], output)
mutated_mod['func_5231'] = func_5231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4665_call = mod.get_global_var('func_4665')
func_4666_call = mutated_mod.get_global_var('func_4666')
call_5232 = relay.TupleGetItem(func_4665_call(), 0)
call_5233 = relay.TupleGetItem(func_4666_call(), 0)
func_4144_call = mod.get_global_var('func_4144')
func_4145_call = mutated_mod.get_global_var('func_4145')
call_5240 = func_4144_call()
call_5241 = func_4144_call()
func_4838_call = mod.get_global_var('func_4838')
func_4839_call = mutated_mod.get_global_var('func_4839')
call_5256 = func_4838_call()
call_5257 = func_4838_call()
func_5054_call = mod.get_global_var('func_5054')
func_5056_call = mutated_mod.get_global_var('func_5056')
call_5259 = relay.TupleGetItem(func_5054_call(), 0)
call_5260 = relay.TupleGetItem(func_5056_call(), 0)
func_5119_call = mod.get_global_var('func_5119')
func_5121_call = mutated_mod.get_global_var('func_5121')
call_5264 = func_5119_call()
call_5265 = func_5119_call()
func_3910_call = mod.get_global_var('func_3910')
func_3911_call = mutated_mod.get_global_var('func_3911')
call_5266 = func_3910_call()
call_5267 = func_3910_call()
bop_5277 = relay.add(call_5256.astype('float32'), relay.reshape(call_5266.astype('float32'), relay.shape_of(call_5256))) # shape=(1, 7, 16)
bop_5280 = relay.add(call_5257.astype('float32'), relay.reshape(call_5267.astype('float32'), relay.shape_of(call_5257))) # shape=(1, 7, 16)
output = relay.Tuple([call_5232,call_5240,call_5259,call_5264,bop_5277,])
output2 = relay.Tuple([call_5233,call_5241,call_5260,call_5265,bop_5280,])
func_5289 = relay.Function([], output)
mod['func_5289'] = func_5289
mod = relay.transform.InferType()(mod)
mutated_mod['func_5289'] = func_5289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5289_call = mutated_mod.get_global_var('func_5289')
call_5290 = func_5289_call()
output = call_5290
func_5291 = relay.Function([], output)
mutated_mod['func_5291'] = func_5291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4144_call = mod.get_global_var('func_4144')
func_4145_call = mutated_mod.get_global_var('func_4145')
call_5336 = func_4144_call()
call_5337 = func_4144_call()
func_5119_call = mod.get_global_var('func_5119')
func_5121_call = mutated_mod.get_global_var('func_5121')
call_5343 = func_5119_call()
call_5344 = func_5119_call()
func_4193_call = mod.get_global_var('func_4193')
func_4194_call = mutated_mod.get_global_var('func_4194')
call_5348 = relay.TupleGetItem(func_4193_call(), 0)
call_5349 = relay.TupleGetItem(func_4194_call(), 0)
func_237_call = mod.get_global_var('func_237')
func_239_call = mutated_mod.get_global_var('func_239')
const_5365 = relay.const([[4,3],[7,-1],[-2,-2],[7,-2],[7,-9],[6,3],[-6,-6],[-1,-2],[10,-2],[-3,-2]], dtype = "uint32")#candidate|5365|(10, 2)|const|uint32
call_5364 = relay.TupleGetItem(func_237_call(relay.reshape(const_5365.astype('uint32'), [1, 4, 5])), 2)
call_5366 = relay.TupleGetItem(func_239_call(relay.reshape(const_5365.astype('uint32'), [1, 4, 5])), 2)
func_3910_call = mod.get_global_var('func_3910')
func_3911_call = mutated_mod.get_global_var('func_3911')
call_5368 = func_3910_call()
call_5369 = func_3910_call()
output = relay.Tuple([call_5336,call_5343,call_5348,call_5364,const_5365,call_5368,])
output2 = relay.Tuple([call_5337,call_5344,call_5349,call_5366,const_5365,call_5369,])
func_5370 = relay.Function([], output)
mod['func_5370'] = func_5370
mod = relay.transform.InferType()(mod)
output = func_5370()
func_5371 = relay.Function([], output)
mutated_mod['func_5371'] = func_5371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4990_call = mod.get_global_var('func_4990')
func_4991_call = mutated_mod.get_global_var('func_4991')
call_5382 = func_4990_call()
call_5383 = func_4990_call()
func_123_call = mod.get_global_var('func_123')
func_127_call = mutated_mod.get_global_var('func_127')
var_5415 = relay.var("var_5415", dtype = "int64", shape = (588,))#candidate|5415|(588,)|var|int64
call_5414 = func_123_call(relay.reshape(var_5415.astype('int64'), [6, 7, 14]), relay.reshape(var_5415.astype('int64'), [6, 7, 14]), )
call_5416 = func_123_call(relay.reshape(var_5415.astype('int64'), [6, 7, 14]), relay.reshape(var_5415.astype('int64'), [6, 7, 14]), )
func_4204_call = mod.get_global_var('func_4204')
func_4205_call = mutated_mod.get_global_var('func_4205')
call_5417 = relay.TupleGetItem(func_4204_call(), 0)
call_5418 = relay.TupleGetItem(func_4205_call(), 0)
const_5419 = relay.const([[[-1.925678,-6.590697,-5.238189,-4.604302,6.438403,-1.697978,-0.906636,-7.174194,-7.217878,-4.522583,-0.546264,0.438565,-1.884702,-2.838579,0.987025,-1.367622],[-0.349813,5.685956,-0.673434,2.059279,-1.439660,3.433802,-6.325444,-1.142074,-8.310925,-6.601474,5.447583,0.219667,1.985781,-1.040224,1.032707,-5.394137],[0.388181,0.556547,-5.561183,0.857760,-1.199881,7.972755,-6.342534,5.790257,-3.252270,9.280243,4.425860,6.169773,-4.338267,1.821372,8.391705,-5.818031],[-6.969404,-6.246391,-7.128096,5.436966,-2.852613,0.325611,-5.493269,-8.669192,9.266324,4.319991,-4.904451,2.447165,-1.339255,5.413025,-7.907444,-3.698353],[4.622902,6.077889,-4.156988,-3.647665,6.637515,0.763031,-9.661737,2.779909,6.888365,-7.290324,6.197787,-9.948348,-2.794271,1.410285,5.266632,6.206391],[-7.560329,-9.116939,-8.686258,-5.092533,7.823123,8.363222,5.254126,3.059740,2.156671,-2.057706,1.374421,-3.042131,-6.567811,-0.257616,5.804495,-1.170245],[3.732620,-7.936450,9.944083,1.364905,-9.150386,-8.570234,7.046999,-7.563865,6.540023,-6.430132,-6.811978,2.408151,-0.298234,-9.614759,4.565525,-4.365206]],[[-5.453359,-9.267003,4.153858,-4.893562,4.091412,0.985837,-2.909259,7.967794,-9.336459,-9.687905,0.512840,-9.209129,3.013161,6.351650,1.086469,2.817144],[0.772578,-3.908977,-0.533027,-0.639127,0.976899,-8.068424,-8.993450,-2.647737,0.422813,6.150769,-9.831489,3.590912,-5.889480,-0.088892,-9.306712,7.031062],[-2.382049,-3.285095,-7.455814,-1.008074,-1.417454,1.013920,-3.062585,0.057808,-3.126878,-3.669869,-9.008657,8.077021,6.006991,9.375049,8.647661,8.202427],[-2.141250,-5.102791,-4.895650,-9.850513,-9.630117,8.711647,7.196975,-1.638039,6.611291,-6.321345,-0.101953,0.430966,-1.977032,9.572635,7.380626,2.030181],[-0.052586,4.855087,-4.536743,9.240845,2.877219,2.438225,-9.387251,6.326311,9.070352,2.956238,8.268760,7.195620,4.731465,5.444707,8.970678,-0.258464],[9.573453,-1.067571,-6.689541,-0.432011,0.308482,-7.811107,1.119440,4.415929,-0.119727,6.128093,3.990229,3.829988,8.341219,-0.026883,3.958998,1.194133],[-4.279590,-5.972168,7.569707,-4.139438,-0.982963,-5.152316,-9.275036,-7.425725,3.884613,-4.452122,-8.325916,8.901405,5.110337,-3.636171,2.444857,8.525340]],[[-9.928992,-0.622626,-7.925809,-4.766960,1.212159,-2.509828,-9.303273,-4.752009,-0.908862,2.574520,-5.789439,2.585318,-7.055586,-4.875076,2.695943,7.282514],[2.645322,8.842966,-7.577165,1.243068,7.321472,-0.698887,-1.393123,7.589743,9.864061,-8.919731,9.263711,8.722491,1.760000,2.377089,7.592425,-3.453787],[-6.427236,-7.143873,6.379157,3.303614,-1.994339,4.707833,-6.417669,4.957283,1.804206,-9.943088,1.403100,-8.355491,6.797399,5.721402,-9.253298,-3.057421],[-8.279715,1.120925,-7.540015,-3.719729,-8.224971,8.281451,-0.156292,8.666425,-4.269379,-2.987607,9.262326,3.295588,0.743737,-6.956380,-3.564925,-6.296959],[1.918400,9.306714,-6.971795,-2.233207,9.694529,-9.162729,9.981802,6.140475,7.969200,7.675062,-2.790711,5.537791,-9.585799,4.291748,-3.171014,9.706707],[9.936198,2.591187,-2.715264,2.790382,-3.068971,3.957231,3.880081,6.022791,-5.397621,2.115067,7.193451,-6.657432,-4.071712,9.726731,-6.096418,7.760861],[7.269875,7.004804,-3.246471,7.404229,-9.522791,-1.335834,5.619478,-3.233492,9.361978,-9.888499,2.928266,-9.441157,-3.912625,-7.945563,-7.457178,-4.472471]],[[6.191082,3.167202,-2.504364,-1.149226,9.075362,-8.564892,-2.292258,-9.948488,6.296181,2.924652,-2.796099,-5.337718,2.490302,2.603665,-3.548893,9.919630],[3.904884,-7.913094,6.231634,1.449744,2.006668,0.440125,-7.324376,0.068361,-8.885710,-7.488230,-7.244301,6.096478,-0.188644,1.117449,-9.204451,-9.150408],[4.115488,-3.621099,3.447331,9.103112,5.042110,-5.924808,1.977069,0.654462,-1.413481,-2.956901,9.980762,-0.235782,-4.054173,-2.005650,-6.014115,-4.176802],[3.242099,-4.013677,-9.714139,-6.497205,-9.653740,-9.285264,-1.325112,3.104514,7.299542,-7.978050,5.587329,-0.991346,-1.646333,1.384901,3.947435,7.147000],[-1.072038,6.819835,9.808890,-7.020911,1.104633,6.915313,2.858434,-7.459555,-6.278383,4.041563,-0.246620,9.108768,-2.809564,1.647464,3.167393,1.772542],[8.191768,-6.951374,-0.017916,-6.126661,9.532317,2.999393,9.997454,-2.152382,-4.861691,7.609395,0.862308,-1.953830,7.185837,-1.947780,-5.538166,-2.496440],[-1.891171,-1.351901,-8.508923,-9.435397,3.698261,-3.047357,-0.571772,-5.022752,-7.607293,7.152499,5.958552,8.255508,3.709589,2.445977,4.748060,2.990613]],[[-6.100609,-7.098939,5.150760,4.188230,1.432662,4.114909,-7.081351,-7.812658,1.750878,-6.164437,6.265089,-7.169979,3.679284,-2.086716,7.796919,0.986662],[-9.952214,-9.422921,-3.214228,-4.100749,2.854487,7.245612,9.425836,-2.385263,1.085055,6.575266,0.806167,-1.355114,9.467765,5.379859,-9.616418,8.501272],[7.779343,-5.233170,8.562328,1.097114,-1.201745,-6.734426,-9.693669,3.623225,5.351250,7.630447,-1.202408,-1.105161,-8.769933,-9.323631,-2.412420,3.276923],[-3.592610,3.839038,-6.199611,-5.927587,-0.947916,9.013979,-8.434785,-5.639305,1.582739,-9.796084,5.996067,-6.179168,-3.609392,4.901923,-5.969298,-4.496678],[-9.794938,-0.316149,-2.267944,-2.562724,8.463937,-5.229302,-0.383850,0.565837,-7.229866,4.389677,-6.273908,6.316321,-4.711971,8.322471,-0.909390,8.980895],[-2.901535,6.134584,9.493898,4.090422,9.240291,-7.842536,-6.421002,-3.972469,2.412493,9.553499,0.812963,-9.150495,8.955316,-4.649972,-6.698992,-2.793449],[9.537559,5.491569,4.225336,5.311471,-7.324148,-9.745280,3.943903,6.028868,-1.131963,6.661357,-2.632221,-0.180832,2.211192,3.414597,-3.037734,-6.076479]],[[3.647566,-1.723665,-8.942475,-5.441956,0.562829,-7.053090,7.535087,9.977379,-3.804591,8.098060,9.939833,-6.226922,-3.287511,-4.436179,4.386639,-8.461212],[-9.056646,-6.461548,-8.011368,-0.230422,8.248683,-9.263110,-8.515573,0.521277,-1.263508,7.759815,-1.433923,4.930538,6.732536,2.619308,-3.551812,-5.406126],[3.453917,-4.730385,5.945667,5.392307,6.808782,0.069824,-9.965746,-5.301153,5.443202,-6.913265,4.285899,-3.540651,0.115624,7.631026,3.183953,-7.222995],[-3.977116,-4.463634,3.558310,5.606790,7.933719,7.902422,5.840445,4.194904,1.589007,-7.128867,0.975420,-3.187291,-9.726681,-7.294907,9.852699,-6.381840],[1.634983,7.012994,7.953583,0.591815,1.714257,-5.540817,-0.063914,9.830546,1.278798,-2.681760,-8.741888,8.182399,8.439193,-6.192505,-4.567874,-3.963931],[6.305896,2.763185,-2.345441,3.858134,0.121606,-4.364024,3.149166,7.177724,5.730022,1.328339,-2.851386,4.224493,9.950397,-7.574411,-7.284235,6.820230],[-4.275086,-7.324225,-1.939804,-7.629189,2.462934,3.387748,-6.951713,4.320018,0.458896,6.916578,8.664571,8.756491,-9.279160,0.240990,-5.220654,-1.429285]],[[1.207510,-2.172543,3.323025,8.346845,5.344470,6.973336,2.175275,-7.149701,-4.933818,4.658326,-2.790095,-7.524544,-5.840968,0.376291,-4.484774,-9.685754],[0.164122,3.116425,5.048047,9.752470,-1.925585,9.389247,-0.922709,-8.457506,6.699510,-7.331937,-7.943149,7.875425,-9.926487,9.717994,-1.960426,-3.783923],[-3.230775,-2.878523,-5.444699,4.338475,2.154202,9.131228,-1.524653,-6.746213,0.026403,2.311444,8.578864,-4.534077,7.947288,-5.217497,1.335279,5.747101],[4.050132,-1.148950,-9.167636,-4.748704,-3.916769,3.707838,2.610444,-1.473452,-2.815190,-0.616444,-2.677946,-5.399023,-6.433559,-3.572883,4.686217,-8.787078],[9.030434,4.530824,-9.741681,6.338725,8.383346,0.080408,-2.866558,3.612260,9.548085,-8.654062,-8.828109,1.663876,-6.171277,9.851121,-7.756089,-3.235356],[-3.849055,6.022827,3.932812,7.921512,1.965298,3.448233,-6.276538,-7.588111,-0.486653,-9.304497,4.124583,7.986832,9.055319,-8.998664,-9.749140,7.112217],[-6.765301,1.819162,-2.115919,-4.323145,0.347652,5.829207,-0.938744,6.206012,0.609613,5.799059,-5.983307,-2.331982,0.129595,7.784467,5.006218,-5.717243]],[[1.804441,2.860840,-6.911846,4.815700,5.747057,-0.842558,-3.248043,-6.263289,1.538391,2.358392,-6.688314,2.985113,-2.752672,-0.097152,7.852367,3.249435],[-8.917717,-6.749386,-1.184185,1.874351,7.065401,5.054520,2.529539,7.265179,2.962118,-1.914222,-1.602729,-4.373344,-6.257835,-1.245355,1.683717,-2.807327],[-0.998766,4.663401,-4.982665,-7.683185,-8.008084,-4.492260,5.565159,-6.431153,-9.876795,-7.785696,-5.345131,8.407575,5.122514,-8.051925,7.985947,3.507034],[-4.803015,-0.627676,4.828528,-3.447125,-8.535435,6.106899,-1.697014,-7.457403,2.896320,6.720897,1.482382,-3.488000,-9.074042,-7.043492,-3.349019,6.070786],[-5.857396,8.166578,-9.552009,8.319819,-7.723271,-3.720554,-8.091371,2.668217,0.633492,2.015037,2.987617,-3.973304,-1.236160,0.059609,-9.987324,5.135669],[-7.308902,-8.193426,-7.412271,5.996071,-6.690964,1.570761,9.947776,-3.973299,5.788653,1.250995,-6.308094,-8.534307,-1.751213,9.800644,-2.777796,2.457860],[8.815183,1.840107,7.684578,5.557342,-5.595989,-3.892032,6.666469,8.814155,-4.273950,-1.481828,-8.551440,-2.471993,-7.011777,0.371810,-3.319861,-7.114355]],[[-1.030301,-7.106645,-1.827617,8.765416,-6.675073,-2.105952,8.083776,3.843775,2.076331,-0.667655,-4.755953,-4.995976,-6.700496,-9.288304,0.101332,-9.438130],[-0.839825,5.598626,-2.025066,-7.858093,4.290424,7.855080,-4.977445,-1.715847,-5.908579,5.067664,0.954273,5.947817,3.576519,2.131885,-0.109992,-3.663156],[-3.307441,-2.375682,-4.239531,8.536671,5.924028,-0.385153,8.890795,5.643221,8.270722,8.678353,8.858187,-8.979934,-3.984574,7.787517,-5.612599,7.220270],[1.026242,8.996052,-6.667749,2.625666,9.194144,0.982988,1.377435,-8.053324,3.750190,7.873839,1.668328,5.003390,7.347808,-4.055729,-3.743048,-8.950922],[8.852221,-4.022272,3.757181,-1.933258,9.105432,8.236911,-7.886895,-3.961550,3.159754,-9.683256,0.603865,-7.671329,-9.022801,-4.997240,9.531155,1.941084],[1.796830,-9.591043,3.365131,1.040731,5.926202,2.756920,8.291849,1.158201,-9.333922,9.146755,-2.229411,-1.718968,-4.058030,7.335083,-3.433003,7.578458],[-2.283565,-8.404234,-9.991440,7.581271,-2.655759,6.175355,-6.773525,0.346166,2.029309,-4.309674,-0.906900,-9.501990,-6.976659,-8.444527,-6.336216,-0.517163]],[[-4.634520,1.161530,-0.054906,-9.109289,7.737560,-1.295503,-5.912959,-6.364374,-0.450475,7.572759,-9.918602,-8.481151,-2.178619,0.053673,-0.366771,8.978705],[-5.954237,5.871966,6.284363,4.221156,8.399592,-4.080787,1.199841,2.421070,-7.961288,4.479651,5.668292,8.564255,-5.847427,-1.913231,-1.388252,6.417888],[-3.400616,3.541630,-2.778091,7.715809,7.002395,-9.477793,-4.216989,-3.792461,-3.271370,7.305650,9.489415,4.618819,9.446077,-4.032039,-2.970690,-6.911856],[-0.037828,-3.922486,3.925722,3.297391,-3.908119,2.910812,0.595343,3.700647,7.416910,6.387050,0.153155,3.349206,6.492312,-0.811409,8.652633,-6.030491],[-2.029640,5.523760,-3.095383,-0.564499,-6.058648,-1.706377,-5.039184,8.415857,-3.083397,-1.094639,-1.282400,9.019124,-6.322080,4.879247,-0.940380,9.005049],[-6.648178,-5.063455,2.565054,3.713272,6.555065,-4.181887,6.066395,2.865985,-6.945869,4.188566,2.228889,-5.364299,-7.812522,-5.674356,-3.867577,-3.363036],[-9.786078,6.569084,6.005081,8.202157,-3.984908,-6.630738,9.119529,-2.676173,-8.365616,-3.824873,-8.811169,4.569829,-6.520233,9.766843,8.180968,-8.809458]],[[6.095304,-0.876588,-6.892496,1.164063,4.845192,0.422146,8.403091,-9.580694,6.054496,-2.349574,-8.473044,4.271677,1.816921,6.571560,-7.467327,-1.915507],[1.237724,-0.595787,-8.907617,8.192697,-0.177849,-2.541991,-5.762014,2.222943,-2.608757,2.945831,9.731260,3.962334,0.349827,2.197063,-2.922387,9.410681],[-9.788902,-0.697408,0.606547,-5.167650,-7.300271,-9.237124,-7.312615,-9.423502,1.861034,4.632428,-4.848367,4.413854,0.149024,3.886864,-1.343460,7.430566],[7.004942,6.248646,5.973547,-5.370407,-6.988544,-5.155596,-6.974615,4.818815,-5.376559,-3.271808,-6.451339,3.134005,-8.851258,9.615435,6.171772,-2.910797],[-0.378239,-4.203168,4.182455,8.396764,2.707866,-9.625891,4.920997,1.944322,-2.249416,-9.848572,9.756900,-1.784378,6.756072,-5.529730,1.037657,5.606024],[-0.485153,4.053311,-2.245999,1.403374,2.734729,7.725178,-8.832501,-0.192118,-1.600307,7.352512,-7.588629,1.967095,9.339986,2.534351,-8.268653,6.737955],[-5.492642,0.670964,7.846698,-1.606215,-8.727222,6.225359,-4.957162,-4.998236,2.985118,-3.796427,7.027537,5.432549,7.382585,5.594858,6.770685,-1.408399]],[[-0.277654,-8.598192,-7.221246,-9.176758,-0.109842,5.443443,4.666964,1.395318,6.481162,6.649319,9.274845,-3.165995,2.863395,9.320161,-2.471060,-5.311523],[6.475920,-6.490564,7.457137,-9.133249,9.884218,-4.064279,0.390570,3.935028,2.893831,-3.455399,9.369537,2.879303,-0.703838,7.932672,-0.732241,0.124666],[-8.922381,5.176493,-2.058757,1.458968,-7.100735,2.105668,7.508515,-3.693415,7.723215,0.444334,7.709704,2.065146,7.261173,-8.970194,-8.445276,2.393747],[-5.567319,-3.138412,2.932502,-9.606711,3.163732,9.371652,-1.509842,8.045327,-8.574988,-1.931075,6.172031,-4.698762,-9.620081,-9.832543,-1.863291,3.785436],[-7.896554,-7.155359,7.087206,9.297384,-2.648902,6.539148,0.272376,-8.569361,7.235306,9.251157,-7.268307,-6.786471,4.241986,3.981197,-5.419868,-6.692739],[-7.970841,-0.443836,1.002297,-1.494071,8.632116,-6.410341,-6.364357,-7.091360,3.225991,-1.633358,1.797444,-9.806915,3.414399,6.846324,-0.686177,-4.618928],[-3.336765,-4.307313,8.378843,3.993505,-0.505699,2.784613,-9.275600,-0.058385,7.117281,9.618174,7.369181,9.913239,2.488731,5.172254,-3.378341,-5.846709]],[[-4.353746,-0.855605,5.176247,-9.453139,2.850265,-2.548796,-2.582918,0.571802,6.522422,-1.138897,-2.415829,8.472464,-0.502135,2.710039,-3.041138,5.867365],[-3.739830,-8.700295,1.597479,5.251241,-3.272349,-0.704782,7.797063,6.851441,-8.111092,4.979660,1.103280,-6.103704,7.518403,4.615167,8.368378,2.732365],[-1.630909,7.776949,-9.995073,5.666113,-9.971755,1.894523,2.379767,-7.544686,9.214622,2.210617,-6.518319,-9.889254,6.914077,-6.849041,5.945833,3.336690],[2.456045,0.299859,2.941169,2.353806,2.115974,1.933655,9.152248,-1.980832,-5.628130,7.881913,-6.324764,-7.794857,8.834578,-0.102939,-1.306119,0.276459],[5.493291,-3.576991,1.118482,-7.493280,-1.059615,1.192357,-1.746020,-9.410189,1.772858,4.927291,-3.351410,-1.072091,-0.262452,-6.689706,-8.448420,9.235635],[-6.127777,-1.214483,3.492345,-5.599229,2.327515,7.746976,-1.682783,-6.824175,4.495534,5.608764,1.849963,-1.792127,-0.638908,3.005034,-7.449332,-1.116409],[-3.545292,-3.630644,-8.910244,5.255118,-3.311376,2.082418,4.791292,7.451782,0.759760,-9.465397,-1.015122,7.603751,7.768455,6.517841,7.410453,-2.899504]],[[-7.105841,1.988202,-0.966761,-7.396749,8.532008,1.569013,9.650759,0.391762,9.903378,-4.860122,-8.037956,-2.267207,-4.988163,9.279555,-1.496595,9.106758],[-3.385920,3.839050,8.208942,-3.810435,2.252924,8.662630,-1.564545,8.817669,-4.951237,9.653683,3.463811,-1.827842,1.504148,6.805523,-5.012705,-5.313227],[7.847058,2.021438,-8.122587,0.245010,2.711340,-8.927456,-4.988069,8.626044,7.574732,5.790529,-1.782726,-3.228656,-2.606863,7.069558,-9.522432,4.656388],[3.659782,2.419026,-3.943832,8.590518,1.700020,7.068614,-4.512258,7.135810,7.143087,-0.319289,-3.984953,7.924280,4.342331,1.804806,3.689423,5.058326],[2.226327,-4.226809,-8.877367,9.080436,6.498211,7.084188,2.259970,-0.875665,0.938290,4.591485,0.360754,-7.821060,6.168671,8.294970,4.679866,-0.119382],[3.721797,-6.313862,-8.880932,9.543313,6.830560,5.240316,4.046753,5.056449,2.892476,8.891426,-0.378138,1.029432,1.881614,-4.518793,9.687325,-3.236247],[1.906016,-7.348882,-0.209815,0.256119,-1.982384,2.717627,-8.978056,4.221367,4.012255,4.000912,-5.349750,9.599652,3.634908,-7.526680,-4.295879,4.576824]],[[-2.547614,-9.960437,0.491021,-0.954470,-5.499507,-0.931525,-9.638150,-3.326346,-3.955898,6.223625,-6.854170,-4.126471,-1.227879,6.984141,3.750879,-2.607374],[-4.296936,3.035487,2.489304,-5.420316,0.241427,-3.719360,-8.924391,2.732124,-6.327182,4.543861,6.244917,-5.049836,6.810825,9.746993,-5.019757,-6.478851],[-6.499742,4.696511,9.840793,5.986493,-8.691022,-1.448540,9.096872,7.930752,7.043521,-6.775508,-5.632789,-1.296626,-1.967824,5.421744,-6.513127,-9.769276],[0.471625,-2.296990,1.300021,5.284996,3.900335,-4.603873,0.552497,7.631992,-9.744493,0.115649,-8.230166,-7.647578,1.211740,-8.338584,6.405577,-3.250583],[-0.766524,8.366420,5.038432,5.772245,3.484489,0.890421,5.010932,4.741408,-2.995126,-4.736674,-3.990108,-5.686021,-6.702643,4.412451,9.986046,-1.935695],[-9.165046,5.430937,-2.176903,3.422586,-8.366080,-7.699985,9.558969,5.614974,1.327018,-6.754017,3.142823,3.923294,1.905897,4.791387,9.017591,-7.261203],[-2.931631,3.111593,-1.632497,-1.643991,2.606491,-6.250968,-4.287570,-6.011414,-3.345472,4.585720,8.585032,8.468532,-9.520973,5.777941,4.758696,7.619727]]], dtype = "float32")#candidate|5419|(15, 7, 16)|const|float32
bop_5420 = relay.power(call_5417.astype('float64'), const_5419.astype('float64')) # shape=(15, 7, 16)
bop_5423 = relay.power(call_5418.astype('float64'), const_5419.astype('float64')) # shape=(15, 7, 16)
uop_5424 = relay.erf(call_5417.astype('float64')) # shape=(1, 7, 16)
uop_5426 = relay.erf(call_5418.astype('float64')) # shape=(1, 7, 16)
bop_5431 = relay.greater(uop_5424.astype('bool'), bop_5420.astype('bool')) # shape=(15, 7, 16)
bop_5434 = relay.greater(uop_5426.astype('bool'), bop_5423.astype('bool')) # shape=(15, 7, 16)
func_3527_call = mod.get_global_var('func_3527')
func_3532_call = mutated_mod.get_global_var('func_3532')
const_5443 = relay.const([[-0.965503,4.504448,4.006428,-3.898248,-5.291208,-7.880231,-2.835217,-2.816771,-9.821021,-7.288867,1.103338,5.223977,8.276834,0.826619,5.176400,-5.578177,4.031079,8.982531,6.732093,-8.547370,5.724169,0.587885,0.814450,-2.498043,3.652865,-7.597147,3.720321,1.061709,-2.772957,6.448366,6.871874,6.803551]], dtype = "float64")#candidate|5443|(1, 32)|const|float64
const_5444 = relay.const(-4, dtype = "uint64")#candidate|5444|()|const|uint64
call_5442 = relay.TupleGetItem(func_3527_call(relay.reshape(const_5443.astype('float64'), [4, 4, 2]), relay.reshape(var_5415.astype('int64'), [98, 6]), relay.reshape(const_5444.astype('uint64'), []), relay.reshape(call_5382.astype('uint64'), [336,]), ), 6)
call_5445 = relay.TupleGetItem(func_3532_call(relay.reshape(const_5443.astype('float64'), [4, 4, 2]), relay.reshape(var_5415.astype('int64'), [98, 6]), relay.reshape(const_5444.astype('uint64'), []), relay.reshape(call_5382.astype('uint64'), [336,]), ), 6)
output = relay.Tuple([call_5382,call_5414,var_5415,bop_5431,call_5442,const_5443,const_5444,])
output2 = relay.Tuple([call_5383,call_5416,var_5415,bop_5434,call_5445,const_5443,const_5444,])
func_5454 = relay.Function([var_5415,], output)
mod['func_5454'] = func_5454
mod = relay.transform.InferType()(mod)
var_5455 = relay.var("var_5455", dtype = "int64", shape = (588,))#candidate|5455|(588,)|var|int64
output = func_5454(var_5455)
func_5456 = relay.Function([var_5455], output)
mutated_mod['func_5456'] = func_5456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4931_call = mod.get_global_var('func_4931')
func_4932_call = mutated_mod.get_global_var('func_4932')
call_5477 = relay.TupleGetItem(func_4931_call(), 0)
call_5478 = relay.TupleGetItem(func_4932_call(), 0)
var_5481 = relay.var("var_5481", dtype = "float64", shape = (9, 7, 16))#candidate|5481|(9, 7, 16)|var|float64
bop_5482 = relay.not_equal(call_5477.astype('bool'), var_5481.astype('bool')) # shape=(9, 7, 16)
bop_5485 = relay.not_equal(call_5478.astype('bool'), var_5481.astype('bool')) # shape=(9, 7, 16)
func_3356_call = mod.get_global_var('func_3356')
func_3360_call = mutated_mod.get_global_var('func_3360')
const_5497 = relay.const(7, dtype = "int8")#candidate|5497|()|const|int8
var_5498 = relay.var("var_5498", dtype = "int8", shape = (28,))#candidate|5498|(28,)|var|int8
call_5496 = relay.TupleGetItem(func_3356_call(relay.reshape(const_5497.astype('int8'), []), relay.reshape(var_5498.astype('int8'), [1, 14, 2]), ), 2)
call_5499 = relay.TupleGetItem(func_3360_call(relay.reshape(const_5497.astype('int8'), []), relay.reshape(var_5498.astype('int8'), [1, 14, 2]), ), 2)
var_5513 = relay.var("var_5513", dtype = "float64", shape = (4, 7, 16))#candidate|5513|(4, 7, 16)|var|float64
bop_5514 = relay.logical_xor(call_5477.astype('int16'), var_5513.astype('int16')) # shape=(4, 7, 16)
bop_5517 = relay.logical_xor(call_5478.astype('int16'), var_5513.astype('int16')) # shape=(4, 7, 16)
output = relay.Tuple([bop_5482,call_5496,const_5497,var_5498,bop_5514,])
output2 = relay.Tuple([bop_5485,call_5499,const_5497,var_5498,bop_5517,])
func_5525 = relay.Function([var_5481,var_5498,var_5513,], output)
mod['func_5525'] = func_5525
mod = relay.transform.InferType()(mod)
var_5526 = relay.var("var_5526", dtype = "float64", shape = (9, 7, 16))#candidate|5526|(9, 7, 16)|var|float64
var_5527 = relay.var("var_5527", dtype = "int8", shape = (28,))#candidate|5527|(28,)|var|int8
var_5528 = relay.var("var_5528", dtype = "float64", shape = (4, 7, 16))#candidate|5528|(4, 7, 16)|var|float64
output = func_5525(var_5526,var_5527,var_5528,)
func_5529 = relay.Function([var_5526,var_5527,var_5528,], output)
mutated_mod['func_5529'] = func_5529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5370_call = mod.get_global_var('func_5370')
func_5371_call = mutated_mod.get_global_var('func_5371')
call_5549 = relay.TupleGetItem(func_5370_call(), 3)
call_5550 = relay.TupleGetItem(func_5371_call(), 3)
func_3356_call = mod.get_global_var('func_3356')
func_3360_call = mutated_mod.get_global_var('func_3360')
var_5560 = relay.var("var_5560", dtype = "int8", shape = ())#candidate|5560|()|var|int8
var_5561 = relay.var("var_5561", dtype = "int8", shape = (28,))#candidate|5561|(28,)|var|int8
call_5559 = relay.TupleGetItem(func_3356_call(relay.reshape(var_5560.astype('int8'), []), relay.reshape(var_5561.astype('int8'), [1, 14, 2]), ), 3)
call_5562 = relay.TupleGetItem(func_3360_call(relay.reshape(var_5560.astype('int8'), []), relay.reshape(var_5561.astype('int8'), [1, 14, 2]), ), 3)
uop_5566 = relay.exp(call_5549.astype('float32')) # shape=(14, 42)
uop_5568 = relay.exp(call_5550.astype('float32')) # shape=(14, 42)
output = relay.Tuple([call_5559,var_5560,var_5561,uop_5566,])
output2 = relay.Tuple([call_5562,var_5560,var_5561,uop_5568,])
func_5573 = relay.Function([var_5560,var_5561,], output)
mod['func_5573'] = func_5573
mod = relay.transform.InferType()(mod)
mutated_mod['func_5573'] = func_5573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5573_call = mutated_mod.get_global_var('func_5573')
var_5575 = relay.var("var_5575", dtype = "int8", shape = ())#candidate|5575|()|var|int8
var_5576 = relay.var("var_5576", dtype = "int8", shape = (28,))#candidate|5576|(28,)|var|int8
call_5574 = func_5573_call(var_5575,var_5576,)
output = call_5574
func_5577 = relay.Function([var_5575,var_5576,], output)
mutated_mod['func_5577'] = func_5577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3955_call = mod.get_global_var('func_3955')
func_3957_call = mutated_mod.get_global_var('func_3957')
call_5670 = relay.TupleGetItem(func_3955_call(), 0)
call_5671 = relay.TupleGetItem(func_3957_call(), 0)
output = relay.Tuple([call_5670,])
output2 = relay.Tuple([call_5671,])
func_5680 = relay.Function([], output)
mod['func_5680'] = func_5680
mod = relay.transform.InferType()(mod)
output = func_5680()
func_5681 = relay.Function([], output)
mutated_mod['func_5681'] = func_5681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4838_call = mod.get_global_var('func_4838')
func_4839_call = mutated_mod.get_global_var('func_4839')
call_5735 = func_4838_call()
call_5736 = func_4838_call()
uop_5751 = relay.atanh(call_5735.astype('float64')) # shape=(1, 7, 16)
uop_5753 = relay.atanh(call_5736.astype('float64')) # shape=(1, 7, 16)
bop_5761 = relay.power(uop_5751.astype('float32'), relay.reshape(call_5735.astype('float32'), relay.shape_of(uop_5751))) # shape=(1, 7, 16)
bop_5764 = relay.power(uop_5753.astype('float32'), relay.reshape(call_5736.astype('float32'), relay.shape_of(uop_5753))) # shape=(1, 7, 16)
output = bop_5761
output2 = bop_5764
func_5770 = relay.Function([], output)
mod['func_5770'] = func_5770
mod = relay.transform.InferType()(mod)
mutated_mod['func_5770'] = func_5770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5770_call = mutated_mod.get_global_var('func_5770')
call_5771 = func_5770_call()
output = call_5771
func_5772 = relay.Function([], output)
mutated_mod['func_5772'] = func_5772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4838_call = mod.get_global_var('func_4838')
func_4839_call = mutated_mod.get_global_var('func_4839')
call_5846 = func_4838_call()
call_5847 = func_4838_call()
output = relay.Tuple([call_5846,])
output2 = relay.Tuple([call_5847,])
func_5860 = relay.Function([], output)
mod['func_5860'] = func_5860
mod = relay.transform.InferType()(mod)
mutated_mod['func_5860'] = func_5860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5860_call = mutated_mod.get_global_var('func_5860')
call_5861 = func_5860_call()
output = call_5861
func_5862 = relay.Function([], output)
mutated_mod['func_5862'] = func_5862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4193_call = mod.get_global_var('func_4193')
func_4194_call = mutated_mod.get_global_var('func_4194')
call_5877 = relay.TupleGetItem(func_4193_call(), 0)
call_5878 = relay.TupleGetItem(func_4194_call(), 0)
func_4049_call = mod.get_global_var('func_4049')
func_4051_call = mutated_mod.get_global_var('func_4051')
call_5880 = relay.TupleGetItem(func_4049_call(), 0)
call_5881 = relay.TupleGetItem(func_4051_call(), 0)
func_3955_call = mod.get_global_var('func_3955')
func_3957_call = mutated_mod.get_global_var('func_3957')
call_5905 = relay.TupleGetItem(func_3955_call(), 0)
call_5906 = relay.TupleGetItem(func_3957_call(), 0)
output = relay.Tuple([call_5877,call_5880,call_5905,])
output2 = relay.Tuple([call_5878,call_5881,call_5906,])
func_5908 = relay.Function([], output)
mod['func_5908'] = func_5908
mod = relay.transform.InferType()(mod)
output = func_5908()
func_5909 = relay.Function([], output)
mutated_mod['func_5909'] = func_5909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5229_call = mod.get_global_var('func_5229')
func_5231_call = mutated_mod.get_global_var('func_5231')
call_5958 = relay.TupleGetItem(func_5229_call(), 0)
call_5959 = relay.TupleGetItem(func_5231_call(), 0)
output = relay.Tuple([call_5958,])
output2 = relay.Tuple([call_5959,])
func_5965 = relay.Function([], output)
mod['func_5965'] = func_5965
mod = relay.transform.InferType()(mod)
mutated_mod['func_5965'] = func_5965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5965_call = mutated_mod.get_global_var('func_5965')
call_5966 = func_5965_call()
output = call_5966
func_5967 = relay.Function([], output)
mutated_mod['func_5967'] = func_5967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5680_call = mod.get_global_var('func_5680')
func_5681_call = mutated_mod.get_global_var('func_5681')
call_6003 = relay.TupleGetItem(func_5680_call(), 0)
call_6004 = relay.TupleGetItem(func_5681_call(), 0)
func_5021_call = mod.get_global_var('func_5021')
func_5023_call = mutated_mod.get_global_var('func_5023')
call_6005 = func_5021_call()
call_6006 = func_5021_call()
func_5525_call = mod.get_global_var('func_5525')
func_5529_call = mutated_mod.get_global_var('func_5529')
const_6012 = relay.const([-7.986374,8.983776,7.853623,8.265551,6.751593,-9.088598,3.179320,-3.955142,4.858768,0.295787,-0.777093,0.132688,-2.349719,5.434629,0.634859,2.621692,0.314577,5.099449,-1.000865,4.216822,-3.529751,-5.234913,-7.479178,-4.395604,-4.988891,-0.001054,-6.355857,-6.580713,-0.776597,-3.562915,-3.364944,-6.654456,-4.229899,-2.996387,-3.814702,1.344578,1.359723,-2.454911,-3.600744,-1.635659,-7.344012,8.052616,-1.015477,8.349784,-7.307656,-2.114439,-2.159569,-3.038050,-4.206387,3.294284,2.537703,9.355091,0.302212,-4.951012,-1.239103,-0.973462,1.680213,1.622002,7.502660,4.115373,-9.939332,-2.423778,-8.446440,-6.628506,-7.357558,7.693758,-4.566144,-2.043230,5.555126,9.070142,9.555150,-2.397487,4.978964,-6.303066,0.968503,-7.429257,4.430880,-6.440456,-7.118981,-3.794882,-4.157123,-1.391568,-4.644857,-8.950239,9.567238,-5.519714,-7.005217,9.792552,-3.607327,-5.898091,5.664614,-0.810099,-4.042145,-1.891213,9.019337,6.820619,8.856508,-6.484546,-1.474686,4.211857,-0.544120,0.541812,-4.758703,-6.124288,-8.016495,-4.707224,-3.160615,5.660416,6.925070,5.171326,-6.140867,7.323691,-0.520216,-8.815056,-5.887873,-9.499242,7.012685,0.289508,-4.975775,-3.058871,6.981186,3.097328,0.096099,-0.454235,-0.777976,9.616564,-4.269503,-5.076587,-3.900470,3.724127,-6.803188,9.139527,3.658595,-1.108780,4.515649,6.867126,3.506492,-9.547473,6.269769,-6.633722,-1.448306,-0.464898,-0.595172,9.067879,1.998509,9.082430,-5.899336,2.646305,-2.247641,2.101709,9.211865,-7.488576,0.385772,9.663705,2.256166,9.814798,-5.233868,-0.319803,-2.345880,9.280048,-7.412510,-1.092341,-8.584265,6.513236,5.322060,-8.188886,1.509066,8.500770,9.221374,1.197322,-1.033724,-8.662862,-2.418488,3.126316,-9.373367,5.058542,-9.849367,7.242664,3.665822,5.628155,6.073428,1.980301,-2.516195,-7.278301,-6.507624,-9.251970,-3.673274,3.458110,1.315128,2.960100,6.397643,-5.505114,-8.809829,-6.676082,-1.592547,-9.785348,7.079093,-5.041697,0.088547,5.263558,-1.456422,-4.321865,-8.942483,-3.838977,9.617423,8.166610,-8.531110,-5.335438,9.153341,-6.821278,-5.211542,-0.594763,4.668375,0.490672,6.927146,-4.587572,-6.558900,-7.290140,-1.466458,-8.922429,-0.297461,-0.983191,3.553592,-0.586073,-5.570599,6.601782,0.359322,-0.317927,-8.232992,1.928768,9.481083,-8.935312,1.118188,-7.070689,3.314537,9.537469,4.672639,-1.502617,-6.344866,5.792387,9.645204,2.240893,-4.975644,3.551782,5.370872,-3.257318,-2.236654,-0.124373,1.160936,7.894974,9.066182,1.676574,6.359478,8.307695,-6.213383,-6.969241,0.206113,-4.433813,2.376549,8.998189,9.282622,1.233144,-9.594511,2.586783,8.431898,-2.983458,0.133803,6.915057,0.636046,-9.304877,1.392180,9.221115,-1.114725,4.362890,-5.972428,-5.498747,-4.723914,3.171587,2.335077,4.852043,-6.527036,2.394129,2.232391,-1.796137,4.804532,-9.486168,1.838202,-9.099595,4.109576,5.739633,-2.537579,5.278195,-5.336763,4.186534,5.628486,-9.820178,-7.829536,9.418716,-0.107170,-3.607209,-7.835995,-5.971246,-0.851838,3.475089,-3.456692,9.928699,-2.890793,-2.175158,-5.149598,-9.627873,-1.655141,4.301674,-9.807126,-1.014770,-1.981059,9.863046,9.159002,-8.630618,-9.100614,2.040672,-0.745451,0.603489,-9.561945,2.755972,4.701214,-5.538741,-9.071979,-5.916295,4.180218,1.253832,1.081544,-5.374375,9.537974,-3.689153,4.628881,-7.491955,7.882211,-7.567854,3.168628,-0.674905,-8.424385,-4.426417,-4.569058,5.439119,1.374103,7.629776,9.458612,7.370463,-2.033451,-5.619104,-0.700990,0.397454,-7.025008,5.578857,-7.010698,-0.097069,-2.396438,7.980389,0.278211,-8.808761,-2.828381,1.676749,-6.176291,-3.650424,9.174260,-5.433399,1.583441,4.507533,2.818726,-4.974909,-7.248795,-8.343211,5.008415,6.427790,9.746331,-8.867424,9.491791,4.491502,-5.785788,-7.454275,1.146900,7.710774,-8.620934,-1.778317,2.562007,1.557903,-8.208465,0.381559,-3.595992,-9.734185,-5.444228,6.892318,4.662091,3.532900,-3.725335,7.538695,-3.456761,-0.293074,6.514408,2.907377,7.317112,-1.748154,-4.496211,-9.116074,-1.192420,-4.958913,7.905677,-9.655196,6.165945,-4.286304,5.328515,9.495141,9.008314,-5.900999,-6.890272,3.171984,5.287978,4.406537,2.319201,-1.964724,0.199262,0.363226,-5.778297,1.573012,0.279175,1.183177,9.616458,0.705046,-0.004473,3.051315,3.918650,6.535156,-6.421797,-5.487915,-2.796949,5.041845,-7.477832,-4.138732,-9.188194,-4.012830,8.411388,-6.984546,-3.971394,4.646379,2.856073,6.343042,-8.975723,9.000417,-0.896528,-7.688618,-5.991408,-8.220279,-3.886931,9.386118,-9.541180,4.630388,1.420240,-0.416748,7.008728,4.366326,-9.405241,1.286404,3.193741,8.643242,-7.429474,-6.317221,5.144053,0.495752,9.328141,-2.206662,-4.356457,0.467188,6.528173,2.886195,-1.925684,7.577128,-3.716026,8.763053,-1.563894,5.295904,-5.480083,8.870132,-9.038266,-5.731657,-8.318499,8.949735,-6.768604,-3.599095,-0.126480,-3.593711,-9.266946,0.788862,-5.051183,-5.123985,4.787783,4.177632,4.696160,8.483359,-5.660866,5.025190,-7.596801,0.948418,-6.155289,-8.830436,-9.555739,8.369617,-0.607696,1.616582,4.822038,9.692597,0.151750,-9.205610,-8.556450,-6.217551,0.147926,9.542797,-6.734646,-7.228180,-0.710766,6.653868,9.019928,-8.915488,4.135002,-3.224587,8.024509,4.256245,5.492399,-6.930049,7.824697,-9.856693,-1.230636,-9.800427,-2.072479,5.377952,4.692517,9.467521,3.825161,-4.379628,5.791330,3.184436,7.550585,4.869607,1.674440,-1.426965,-4.944105,1.001480,-1.377849,6.582819,9.840717,7.847934,2.635810,8.111800,-5.580724,1.995832,5.993506,2.108056,3.459240,0.664521,-2.434062,1.629366,-8.116199,5.841786,-4.316541,8.134139,-2.803379,-7.410192,-9.457593,-4.163173,-6.355540,-7.007566,5.893255,-2.717664,4.599819,4.862580,8.787802,-3.053089,4.658142,-6.492507,4.159931,1.425122,-8.860069,3.424923,-4.229700,-4.628365,-2.463745,-8.125958,-6.765741,-2.933457,-2.526553,5.433192,4.022477,6.417493,6.648021,-9.512731,0.066301,-0.540084,-2.144321,-0.675287,-3.369146,7.731876,-4.691274,-8.250682,-5.855310,-7.891025,-1.270692,-9.765769,8.605837,-7.599978,8.479092,8.401095,6.883481,-9.160200,-3.330273,-9.235689,8.349514,0.985862,9.269818,-8.652096,-2.157845,-1.883391,-8.216921,-2.928420,-3.741631,4.004519,-3.845052,-9.528722,-5.181616,3.416132,-2.930459,9.977974,8.721110,9.709021,-9.303211,-7.573811,-9.677765,3.444058,1.736061,-0.880998,8.394421,6.309477,2.536865,8.044647,-7.722111,-7.531001,-4.675264,0.747217,-5.064073,-7.435513,-6.808171,2.546414,8.849320,-0.484367,9.267221,-9.622719,-1.553909,-4.938762,7.083820,5.746256,-1.328358,-9.281599,-4.488400,-7.893173,-4.461651,7.400134,3.098146,2.997394,-9.791729,6.204887,2.718742,-2.517077,0.579877,7.460582,-3.765879,-8.395233,-0.082111,2.447230,-0.618034,9.117018,-9.201425,-6.386957,3.228525,-5.242693,5.389115,6.626695,0.182341,-9.053296,-7.521585,4.239058,-4.515687,3.048189,7.543696,5.607541,-9.348263,-6.803178,-0.459451,-8.595838,2.886975,9.109864,-0.196624,5.512960,-1.537564,-8.554119,1.472313,8.413540,-1.627627,-7.696772,2.922317,4.708577,-7.407633,-9.005974,-7.444250,-4.522007,6.875287,-7.732377,1.991479,0.570301,9.780081,-4.360624,8.357857,2.961682,4.169716,8.362905,6.525205,-8.166194,0.950385,-6.889534,-5.127607,4.259788,-6.737033,3.833519,6.206974,7.492881,2.378425,0.867480,2.603378,-9.423202,-0.808796,1.777781,-5.355759,5.897985,-3.446437,-4.581060,-4.032315,-7.096322,9.434252,-2.847815,-8.335693,-3.661533,-7.030727,6.276405,-5.652263,-1.074646,3.703847,-1.712314,6.493268,7.765265,-5.039282,-5.202189,1.154052,4.315040,8.020369,7.005062,-5.243438,0.880487,1.752812,-9.958808,-7.268761,-1.781867,3.722775,1.094628,-1.011248,-3.177086,-4.528341,-9.902798,-0.761197,5.265297,8.617425,0.135692,-5.179121,-3.893144,4.642572,2.079942,0.270257,-7.008307,-6.206985,-9.736872,-6.992709,4.014436,5.344602,8.628581,-1.577208,2.899030,9.721314,3.380182,6.451449,-4.662899,-0.268635,-1.924930,0.287227,-0.404673,6.168397,5.272674,-0.146960,-5.297382,-3.000534,2.638265,-0.051169,-7.233858,2.535109,8.591968,-9.450205,-6.800626,6.113581,-0.202465,1.034444,3.048784,0.553087,-7.968353,9.640437,-4.100066,-3.424310,-6.080842,-7.228978,5.595612,-7.093829,2.678640,-9.295252,-4.512592,-5.579275,-1.051183,9.038140,-3.437612,-4.990041,-4.781783,-6.383081,2.772898,-0.361873,8.231531,0.589310,5.541992,-9.047659,-7.949128,-4.166022,-1.724240,0.006843,-1.009256,-6.222514,-0.224639,0.950988,3.070373,0.653385,4.326345,-4.264916,-5.677415,8.046146,-8.963342,-0.611989,-6.396149,9.520842,-3.011185,9.816104,5.192008,4.747262,9.699476,7.801166,-5.842457,3.705642,-7.862041,5.333781,8.774052,-4.994197,-8.507790,-3.635761,7.130946,7.265400,2.824574,-1.967535,8.138075,-4.652183,8.275783,0.846103,-8.155235,8.529008,-4.209359,8.062897,5.148351,6.222741,1.586369,-9.336409,6.524247,-0.576640,-1.169286,-8.128176,-6.096232,-7.514114,-7.932293,-0.146629,8.980159,8.094234,-2.374478,5.225209,4.129783,9.850027,7.030826,3.464768,6.697599,3.540149,5.544710,9.487035,-1.074164,7.916781,1.213963,5.557034,1.628798,3.748989,4.581193,5.072826,7.422625,2.487111,-1.289204,-7.997035,-0.232522,8.432279,6.008304,-4.342156,4.556989,-9.607055,6.689581,4.681547,-6.010389,-5.602237,4.371961,-6.049221,-3.697434,5.520577,7.817883,-2.714144,0.198375,2.144844,7.189568,-7.937991,1.316784,4.570805,-5.716908,6.957219,6.512447,8.353494,7.690717,-5.255424,1.761750,-0.921951,8.201316,4.992111,-8.002360,0.171106,-2.190960,-5.479010,-7.214881,-6.876094,-0.880145,4.751980,1.385481,9.978055,4.352026,-2.528141,9.833074,9.428337,3.524743,-1.492525,0.667100,4.678935,3.064655,3.447270,-3.933357,4.154292,7.999848,-9.637792,4.807072,5.132557,5.722131,7.619599,-7.693435,5.411941,0.173653,9.488618,5.138119,-4.539564,0.832591,-9.938164,3.252214,-4.588492,8.673395,6.597826,-4.195228,7.028496,-4.220185,6.764644,3.625058,6.037470,-9.306624,3.691561,7.891978,-1.909341,0.132751,-4.426999,-5.169006,8.765664,-0.003508], dtype = "float64")#candidate|6012|(1008,)|const|float64
var_6013 = relay.var("var_6013", dtype = "int8", shape = (28,))#candidate|6013|(28,)|var|int8
var_6014 = relay.var("var_6014", dtype = "float64", shape = (448,))#candidate|6014|(448,)|var|float64
call_6011 = relay.TupleGetItem(func_5525_call(relay.reshape(const_6012.astype('float64'), [9, 7, 16]), relay.reshape(var_6013.astype('int8'), [28,]), relay.reshape(var_6014.astype('float64'), [4, 7, 16]), ), 2)
call_6015 = relay.TupleGetItem(func_5529_call(relay.reshape(const_6012.astype('float64'), [9, 7, 16]), relay.reshape(var_6013.astype('int8'), [28,]), relay.reshape(var_6014.astype('float64'), [4, 7, 16]), ), 2)
output = relay.Tuple([call_6003,call_6005,call_6011,const_6012,var_6013,var_6014,])
output2 = relay.Tuple([call_6004,call_6006,call_6015,const_6012,var_6013,var_6014,])
func_6030 = relay.Function([var_6013,var_6014,], output)
mod['func_6030'] = func_6030
mod = relay.transform.InferType()(mod)
mutated_mod['func_6030'] = func_6030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6030_call = mutated_mod.get_global_var('func_6030')
var_6032 = relay.var("var_6032", dtype = "int8", shape = (28,))#candidate|6032|(28,)|var|int8
var_6033 = relay.var("var_6033", dtype = "float64", shape = (448,))#candidate|6033|(448,)|var|float64
call_6031 = func_6030_call(var_6032,var_6033,)
output = call_6031
func_6034 = relay.Function([var_6032,var_6033,], output)
mutated_mod['func_6034'] = func_6034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4023_call = mod.get_global_var('func_4023')
func_4025_call = mutated_mod.get_global_var('func_4025')
call_6039 = relay.TupleGetItem(func_4023_call(), 5)
call_6040 = relay.TupleGetItem(func_4025_call(), 5)
output = relay.Tuple([call_6039,])
output2 = relay.Tuple([call_6040,])
func_6057 = relay.Function([], output)
mod['func_6057'] = func_6057
mod = relay.transform.InferType()(mod)
output = func_6057()
func_6058 = relay.Function([], output)
mutated_mod['func_6058'] = func_6058
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6075 = relay.var("var_6075", dtype = "float64", shape = (13, 2, 13))#candidate|6075|(13, 2, 13)|var|float64
uop_6076 = relay.acosh(var_6075.astype('float64')) # shape=(13, 2, 13)
func_4510_call = mod.get_global_var('func_4510')
func_4515_call = mutated_mod.get_global_var('func_4515')
const_6088 = relay.const([10,-10,-5,-3,-9,-8,-10,-2,-7,2,-7,7,-9,6,-1,-4,6,9,-10,-6,-3,3,-1,-8,7,10,4,-9,-6,-6,7,-10,-3,-6,-3,-3,1,10,10,-10,-2,4,-10,7,-9,5,-3,1,-3,-9,1,5,-8,6,4,7,-8,10,-6,-4,-1,9,1,10,-8,10,-10,3,-9,6,-7,-9,-3,-1,-7,-4,-3,2,4,9,10,-1,-6,10,5,9,8,5,9,2,2,-4,-8,2,-8,-4,-10,-3,-1,-2,-9,-8,-10,-2,-2,5,-10,-10,5,2,3,-4,-1,1,-9,10,-7,7,-3,8,-3,9,2,-4,5,10,2,-3,2,6,-9,9,7,3,5,5,-4,3,-6,-3,-5,-9,7,-3,-5,2,7,10,-9,2,-6,-4,-3,-6,-4,-10,-2,-7,2,-9,8,3,-5,9,-9,8,8,-6,8,10,3,-4,-2,5,10,-2,-7,4,-9,-6,6,4,7,-4,5,1,-7,-4,-6,2,-7,6,9,-8,5,-7,-9,4,4,-4,-4,-7,-10,10,2,-3,6,4,9,6,-5,2,5,-1,4,7,2,10,7,-9,-4,9,-10,-7,-5,1,-7,4,-9,-2,2,-4,3,6,4,10,-8,9,-2,-4,-3,-4,10,-4,-5,-3,-8,-3,10,3,-7,-3,-2,10,3,10,1,-6,-4,-1,1,-9,-10,1,4,-6,-9,-5,-3,6,2,-2,1,-3,2,-3,-9,-1,-5,-1,-8,-1,7,-9,-4,8,2,9,10,8,8,-5,6,-6,-10,-1,5,7,-7,-6,-3,6,-6,9,-7,-10,-8,1,-2,-4,-5,3,6,-6,6,3,6,-7,4,-2,2,-3,-8,-4,-1,-5,5,8,7,6,6,5,1,-6,-7,-4,-10,-1,3,-1,6,-3,-3,4,-7,-5,2,-2,-3,7,-7,-1,10,-5,7,-9,1,6,5,6,-4,4,3,8,4,-8,-8,8,-10,1,9,10,6,-4,8,4,2,-8,3,3,-5,10,1,-1,3,6,-4,1,-4,10,6,-6,1,5,1,-1,10,-10,-1,2,3,-5,-6,-8,3,4,3,8,-3,-7,-1,-3,-10,-2,3,5,3,4,8,10,1,3,-4,-9,-5,3,5,-7,-10,7,4,-9,4,6,7,-5,2,4,8,6,8,-9,7,7,6,1,8,7,-3,-3,-1,-1,-6,-2,8,6,-7,-8,-3,-2,-1,-9,10,10,-10,-8,-3,7,-3,2,5,9,4,-4,4,-6,-8,-5,-2,4,10,-7,10,-10,1,6,3,7,3,-4,9,4,-4,6,4,2,-3,-6,-2,-7,2,8,1,3,-7,2,7,-1,-7,-9,-8,-6,1,-5,-10,-4,8,-8,-7,4,5,10,-4,-5,10,3,-6,-1,2,-7,-10,5,-5,8,1,6,10,10,-4,4,-8,4,-7,-10,-10,-9,10,-10,-6,-4,10,5,-3,3,-9,-5,-5,8,3,9,4,8,6,8,-6,-1,4,8,2,-9,2,5,-3,9,2,3,-10,2,9,-7,2,-5,5,-4,-7,-5,6,-6,6,7,5,-6,1,10,5,6,7,-6,5,9,-4,2,-6,-9,4,-10,5,6,3,-7,3,-8,3,1,5,-1,-6,-8,-1,-7,-4,6,5,7,-7,-8,6,-9,1,10,-1,4,-3,-10,-9,9,-3,5,8,6,4,4,-2,-2,2,-9,-2,10,7,-10,-4,2,-8,5,-6,-9,-7,-4,-5,-1], dtype = "uint16")#candidate|6088|(660,)|const|uint16
var_6089 = relay.var("var_6089", dtype = "uint16", shape = (784,))#candidate|6089|(784,)|var|uint16
var_6090 = relay.var("var_6090", dtype = "int64", shape = (588,))#candidate|6090|(588,)|var|int64
call_6087 = relay.TupleGetItem(func_4510_call(relay.reshape(const_6088.astype('uint16'), [11, 10, 6]), relay.reshape(var_6089.astype('uint16'), [392, 2]), relay.reshape(var_6090.astype('int64'), [588,]), ), 4)
call_6091 = relay.TupleGetItem(func_4515_call(relay.reshape(const_6088.astype('uint16'), [11, 10, 6]), relay.reshape(var_6089.astype('uint16'), [392, 2]), relay.reshape(var_6090.astype('int64'), [588,]), ), 4)
func_1809_call = mod.get_global_var('func_1809')
func_1812_call = mutated_mod.get_global_var('func_1812')
const_6108 = relay.const(9, dtype = "uint64")#candidate|6108|()|const|uint64
const_6109 = relay.const([[-7,-2,1,5,-8,7,-5,-2,-5,-6,-4,5,10,-1,-2,-8,8,-3,-5,-2,-7,8,9,6,-10,-6,-3,-6,-3,-9,8,3,9,-6,4,-7,6,-6,-5,10,5,10],[7,10,-2,4,-8,5,-4,-4,-6,3,8,10,2,-1,-4,-4,6,10,4,-8,-2,4,4,8,10,-4,3,-4,-4,1,-3,-8,10,8,3,-10,1,-4,-3,4,6,-4],[4,5,10,-5,-2,3,-2,-9,9,3,-3,-4,3,-2,10,9,3,-1,7,-5,10,2,10,-10,-1,8,1,-4,2,3,-1,5,4,6,-5,-4,-10,-8,10,-9,10,-6],[-1,-7,-8,6,-3,-3,10,-10,-10,-9,-1,-1,4,1,-9,-7,9,5,4,-7,4,-4,9,7,-8,-8,-1,9,8,9,9,8,-10,7,4,-1,-4,-1,8,-10,4,3],[-8,-1,2,-4,8,1,6,-1,10,9,6,-6,-9,9,6,-9,4,-1,-1,-7,8,4,6,4,-7,1,-4,8,-5,7,8,-8,-5,9,3,-5,-6,2,-6,7,9,9],[-6,7,1,-3,-9,1,9,1,10,2,5,-9,10,4,-5,-3,7,2,-3,7,5,7,2,7,-4,-7,5,-9,3,6,-6,8,-8,-3,5,-4,-2,8,1,-5,4,-3],[9,4,5,7,-9,-9,7,-2,6,5,-9,1,8,-4,-9,3,-8,7,7,9,10,6,1,-10,-6,-4,-9,4,2,-2,-4,6,-2,-7,8,-8,3,-6,4,3,2,-4],[4,-10,5,-7,9,-2,6,-1,-5,-5,-2,7,8,5,-7,2,-8,-8,-6,-3,8,-5,5,1,4,-2,-6,4,9,5,-2,-7,-1,3,-2,2,2,-8,-3,6,-6,6]], dtype = "uint64")#candidate|6109|(8, 42)|const|uint64
call_6107 = relay.TupleGetItem(func_1809_call(relay.reshape(const_6108.astype('uint64'), []), relay.reshape(const_6109.astype('uint64'), [6, 4, 14]), ), 0)
call_6110 = relay.TupleGetItem(func_1812_call(relay.reshape(const_6108.astype('uint64'), []), relay.reshape(const_6109.astype('uint64'), [6, 4, 14]), ), 0)
uop_6111 = relay.log2(uop_6076.astype('float64')) # shape=(13, 2, 13)
func_4931_call = mod.get_global_var('func_4931')
func_4932_call = mutated_mod.get_global_var('func_4932')
call_6113 = relay.TupleGetItem(func_4931_call(), 0)
call_6114 = relay.TupleGetItem(func_4932_call(), 0)
output = relay.Tuple([call_6087,const_6088,var_6089,var_6090,call_6107,const_6108,const_6109,uop_6111,call_6113,])
output2 = relay.Tuple([call_6091,const_6088,var_6089,var_6090,call_6110,const_6108,const_6109,uop_6111,call_6114,])
func_6121 = relay.Function([var_6075,var_6089,var_6090,], output)
mod['func_6121'] = func_6121
mod = relay.transform.InferType()(mod)
var_6122 = relay.var("var_6122", dtype = "float64", shape = (13, 2, 13))#candidate|6122|(13, 2, 13)|var|float64
var_6123 = relay.var("var_6123", dtype = "uint16", shape = (784,))#candidate|6123|(784,)|var|uint16
var_6124 = relay.var("var_6124", dtype = "int64", shape = (588,))#candidate|6124|(588,)|var|int64
output = func_6121(var_6122,var_6123,var_6124,)
func_6125 = relay.Function([var_6122,var_6123,var_6124,], output)
mutated_mod['func_6125'] = func_6125
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6147 = relay.const([[[-9,-5,1,-4,1,9],[-5,10,-10,5,-8,8],[1,-10,-10,-8,-7,3],[2,9,7,9,4,-1],[2,-4,1,4,-1,-6],[-9,9,-7,7,10,-1],[6,10,-3,8,5,8],[1,7,-8,-4,7,-6]],[[6,2,-9,-4,6,7],[-4,-5,-7,4,-4,-4],[6,-3,9,-5,-1,10],[1,7,9,5,10,-2],[-2,7,-9,-2,8,6],[-3,2,-8,-5,8,6],[-7,1,-2,4,-9,-2],[3,3,-9,9,-2,5]],[[-5,10,-4,3,9,7],[-6,5,-4,-6,-3,8],[-2,4,-10,-5,-1,8],[-1,-7,4,-2,-6,6],[8,-7,-2,4,4,5],[9,8,-5,7,7,8],[7,2,9,-3,9,-1],[-9,-5,5,6,2,-5]],[[-2,4,-8,1,-2,-1],[2,-1,6,-3,5,9],[-10,5,10,-8,4,-2],[-4,-2,-7,-9,-8,9],[10,-10,-2,6,-3,3],[-1,-6,4,-1,-2,-7],[5,7,8,-7,9,-5],[6,2,-4,-5,-9,4]],[[-10,4,-10,-10,-10,-10],[2,-7,5,-4,7,10],[-3,8,7,-5,-7,-6],[3,1,2,2,-9,7],[-2,6,-6,-1,-3,-1],[1,5,7,4,-1,3],[-6,-9,3,10,-6,-7],[5,3,8,-8,10,-8]],[[9,8,9,-3,-6,2],[8,-7,10,-7,3,-3],[-4,2,6,-2,4,-5],[1,7,-10,-7,1,-1],[7,6,-9,-2,9,8],[6,2,-10,-2,-5,-10],[-8,-1,8,-1,-1,-6],[-5,-1,2,2,9,-9]],[[-9,4,10,8,1,-8],[-1,-6,6,-1,10,-5],[-3,-2,9,5,-2,3],[-3,1,-10,2,8,2],[-10,2,6,4,-4,-4],[-10,4,-10,-6,-10,6],[8,9,-8,9,-5,9],[10,-5,-10,1,9,-3]],[[-2,1,-8,10,-7,-1],[4,-2,-2,-4,-2,7],[7,-3,-3,5,-7,-7],[-3,10,-10,4,2,-4],[-7,-7,5,-5,3,-9],[4,2,-10,6,-10,5],[1,3,-5,10,-5,-5],[10,-5,7,9,-7,3]]], dtype = "int32")#candidate|6147|(8, 8, 6)|const|int32
var_6148 = relay.var("var_6148", dtype = "int32", shape = (8, 8, 6))#candidate|6148|(8, 8, 6)|var|int32
bop_6149 = relay.equal(const_6147.astype('bool'), relay.reshape(var_6148.astype('bool'), relay.shape_of(const_6147))) # shape=(8, 8, 6)
var_6152 = relay.var("var_6152", dtype = "bool", shape = (8, 8, 6))#candidate|6152|(8, 8, 6)|var|bool
bop_6153 = relay.power(bop_6149.astype('float64'), relay.reshape(var_6152.astype('float64'), relay.shape_of(bop_6149))) # shape=(8, 8, 6)
func_1790_call = mod.get_global_var('func_1790')
func_1793_call = mutated_mod.get_global_var('func_1793')
const_6174 = relay.const([-4.637851,-9.456534,-8.086453], dtype = "float64")#candidate|6174|(3,)|const|float64
call_6173 = func_1790_call(relay.reshape(const_6174.astype('float64'), [1, 3, 1]))
call_6175 = func_1790_call(relay.reshape(const_6174.astype('float64'), [1, 3, 1]))
func_4144_call = mod.get_global_var('func_4144')
func_4145_call = mutated_mod.get_global_var('func_4145')
call_6201 = func_4144_call()
call_6202 = func_4144_call()
func_4811_call = mod.get_global_var('func_4811')
func_4812_call = mutated_mod.get_global_var('func_4812')
call_6212 = func_4811_call()
call_6213 = func_4811_call()
func_5454_call = mod.get_global_var('func_5454')
func_5456_call = mutated_mod.get_global_var('func_5456')
var_6216 = relay.var("var_6216", dtype = "int64", shape = (588,))#candidate|6216|(588,)|var|int64
call_6215 = relay.TupleGetItem(func_5454_call(relay.reshape(var_6216.astype('int64'), [588,])), 2)
call_6217 = relay.TupleGetItem(func_5456_call(relay.reshape(var_6216.astype('int64'), [588,])), 2)
output = relay.Tuple([bop_6153,call_6173,const_6174,call_6201,call_6212,call_6215,var_6216,])
output2 = relay.Tuple([bop_6153,call_6175,const_6174,call_6202,call_6213,call_6217,var_6216,])
func_6225 = relay.Function([var_6148,var_6152,var_6216,], output)
mod['func_6225'] = func_6225
mod = relay.transform.InferType()(mod)
var_6226 = relay.var("var_6226", dtype = "int32", shape = (8, 8, 6))#candidate|6226|(8, 8, 6)|var|int32
var_6227 = relay.var("var_6227", dtype = "bool", shape = (8, 8, 6))#candidate|6227|(8, 8, 6)|var|bool
var_6228 = relay.var("var_6228", dtype = "int64", shape = (588,))#candidate|6228|(588,)|var|int64
output = func_6225(var_6226,var_6227,var_6228,)
func_6229 = relay.Function([var_6226,var_6227,var_6228,], output)
mutated_mod['func_6229'] = func_6229
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6251 = relay.var("var_6251", dtype = "uint32", shape = (3, 16, 9))#candidate|6251|(3, 16, 9)|var|uint32
const_6252 = relay.const([[[2,-3,-9,2,8,-4,-9,-1,-8],[-1,7,7,-1,-5,5,-6,1,-5],[6,8,7,10,4,7,10,-8,5],[10,-2,-1,-4,4,-6,6,8,-5],[5,-3,9,-3,-7,-5,6,-8,-8],[-7,-8,8,4,8,-7,9,8,-2],[-1,5,-4,8,-6,10,9,-8,10],[3,-9,6,-5,7,6,-2,4,4],[-10,8,1,9,5,9,3,-9,-4],[-8,1,-4,-5,-3,4,7,-2,-9],[4,4,-7,-9,6,3,-5,1,-6],[-3,1,-2,-7,-10,-7,-1,9,2],[-8,-4,-9,4,-10,9,2,-9,-2],[-10,3,6,-9,10,-4,-1,3,7],[-4,7,-10,10,-10,2,3,3,-2],[-3,-7,6,-7,-4,-4,-4,5,-2]],[[10,6,-2,-4,-2,10,-5,2,8],[-3,-7,-7,1,-9,3,-3,5,2],[10,4,-2,-4,7,-9,8,-4,-1],[3,-2,-8,6,-9,1,-8,-9,2],[5,6,-6,1,-7,8,-5,9,5],[-4,3,10,5,4,8,-5,4,9],[8,-3,-4,-4,1,-4,-3,5,-2],[-9,-3,-10,10,6,-7,-3,4,10],[4,4,-7,2,-9,-7,2,-7,-10],[-7,-10,-6,9,-2,5,8,-5,-7],[-5,4,5,-4,-7,3,-5,10,5],[-6,5,-7,9,-4,-10,-9,-9,8],[4,3,10,-1,-8,4,-8,8,-8],[6,2,4,-2,-8,5,4,-5,-5],[3,-4,8,4,8,-9,-9,-6,6],[3,-4,-8,-5,10,-9,9,-10,5]],[[-2,-4,-3,9,-10,2,-4,4,4],[-8,-4,2,-5,7,5,3,-1,8],[-2,7,-1,-7,-2,4,5,-6,10],[2,1,1,1,3,-3,-7,7,8],[-1,-4,8,-10,10,9,7,5,1],[4,-2,-6,-6,-1,-7,1,-3,-4],[3,-3,-1,10,6,-6,1,-10,6],[7,9,7,8,5,-2,-4,2,-5],[10,2,3,4,7,7,10,-5,6],[6,-9,5,1,-6,7,-7,-9,2],[7,5,9,-7,-10,7,-6,7,-5],[7,-4,-8,-4,-7,-4,-4,6,-6],[3,-4,-8,6,6,-7,10,7,-9],[-2,-10,8,7,-6,1,-9,-5,-7],[6,7,1,-2,-10,-2,4,3,-2],[-1,-1,3,8,8,5,-8,-1,2]]], dtype = "uint32")#candidate|6252|(3, 16, 9)|const|uint32
bop_6253 = relay.greater_equal(var_6251.astype('bool'), relay.reshape(const_6252.astype('bool'), relay.shape_of(var_6251))) # shape=(3, 16, 9)
func_5770_call = mod.get_global_var('func_5770')
func_5772_call = mutated_mod.get_global_var('func_5772')
call_6259 = func_5770_call()
call_6260 = func_5770_call()
output = relay.Tuple([bop_6253,call_6259,])
output2 = relay.Tuple([bop_6253,call_6260,])
func_6262 = relay.Function([var_6251,], output)
mod['func_6262'] = func_6262
mod = relay.transform.InferType()(mod)
var_6263 = relay.var("var_6263", dtype = "uint32", shape = (3, 16, 9))#candidate|6263|(3, 16, 9)|var|uint32
output = func_6262(var_6263)
func_6264 = relay.Function([var_6263], output)
mutated_mod['func_6264'] = func_6264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5965_call = mod.get_global_var('func_5965')
func_5967_call = mutated_mod.get_global_var('func_5967')
call_6299 = relay.TupleGetItem(func_5965_call(), 0)
call_6300 = relay.TupleGetItem(func_5967_call(), 0)
func_5119_call = mod.get_global_var('func_5119')
func_5121_call = mutated_mod.get_global_var('func_5121')
call_6306 = func_5119_call()
call_6307 = func_5119_call()
func_4990_call = mod.get_global_var('func_4990')
func_4991_call = mutated_mod.get_global_var('func_4991')
call_6315 = func_4990_call()
call_6316 = func_4990_call()
output = relay.Tuple([call_6299,call_6306,call_6315,])
output2 = relay.Tuple([call_6300,call_6307,call_6316,])
func_6328 = relay.Function([], output)
mod['func_6328'] = func_6328
mod = relay.transform.InferType()(mod)
mutated_mod['func_6328'] = func_6328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6328_call = mutated_mod.get_global_var('func_6328')
call_6329 = func_6328_call()
output = call_6329
func_6330 = relay.Function([], output)
mutated_mod['func_6330'] = func_6330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5021_call = mod.get_global_var('func_5021')
func_5023_call = mutated_mod.get_global_var('func_5023')
call_6433 = func_5021_call()
call_6434 = func_5021_call()
uop_6446 = relay.atan(call_6433.astype('float32')) # shape=(6, 6, 8)
uop_6448 = relay.atan(call_6434.astype('float32')) # shape=(6, 6, 8)
output = relay.Tuple([uop_6446,])
output2 = relay.Tuple([uop_6448,])
func_6449 = relay.Function([], output)
mod['func_6449'] = func_6449
mod = relay.transform.InferType()(mod)
output = func_6449()
func_6450 = relay.Function([], output)
mutated_mod['func_6450'] = func_6450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4081_call = mod.get_global_var('func_4081')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_6527 = relay.TupleGetItem(func_4081_call(), 0)
call_6528 = relay.TupleGetItem(func_4082_call(), 0)
func_2430_call = mod.get_global_var('func_2430')
func_2433_call = mutated_mod.get_global_var('func_2433')
const_6536 = relay.const([5,-8,-2,2,-4,-5,4,-1,-7,-2,-3,7,-8,2,-9,2,4,5,-5,-7,-3,-5,10,-2,4,-7,-4,-5,-7,8,3,2,-2,-3,-3,5,3,-4,7,-3,10,7,4,6,10,7,-8,1,7,6,-4,-5,10,-3,5,-7,6,7,-8,3,-1,-1,1,-6,8,6,2,3,3,10,-2,1,10,9,-4,-6,-3,1,-1,-2,-8,2,-2,-1,-1,-10,-7,4,-2,-7,-5,9,-2,-4,7,1,-4,3,-8,-10,-7,-5,-3,6,-1,-10,-8,8,9,-10,-8,2,-3,-8,1,-1,8,5,-4,7,-3,-4,7,-10,4,3,-2,5,-9,-8,1,-1,7,2,-4,-9,-7,-8,6,1,8,3,-10,-7,3,1,7,3,-5,-7,4,-6,10,-5,3,-10,1,-3,4,-2,-5,9,3,8,-8,9,-3,-3,10,-1,6,-4,-5,-10,4,5,2,-1,-7,5,6,-7,8,1,-10,8,6,-4,8,-9,5,4,-8,-4,-6,10,4,10,-7,-9,5,-2,-1,9,2,2,4,7,-10,6,-2,7,-4,-8,-8,-8,4,2,-8,-5,-1,-8,-4,6,7,-2,-10,7,-8,5,-1,8,4,-3,3,3,-6,10,7,3,-9,3,6,5,4,-9,-6,-2,-7,3,4,3,-8,-1,-10,-8,-1,-10,2,10,-9,3,-4,-6,-2,10,-6,10,-7,-8,5,-5,1,-3,5,1,10,9,-10,4,3,-10,8,-2,8,1,-8,-10], dtype = "int8")#candidate|6536|(288,)|const|int8
call_6535 = relay.TupleGetItem(func_2430_call(relay.reshape(const_6536.astype('int8'), [6, 6, 8])), 0)
call_6537 = relay.TupleGetItem(func_2433_call(relay.reshape(const_6536.astype('int8'), [6, 6, 8])), 0)
output = relay.Tuple([call_6527,call_6535,const_6536,])
output2 = relay.Tuple([call_6528,call_6537,const_6536,])
func_6541 = relay.Function([], output)
mod['func_6541'] = func_6541
mod = relay.transform.InferType()(mod)
output = func_6541()
func_6542 = relay.Function([], output)
mutated_mod['func_6542'] = func_6542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5680_call = mod.get_global_var('func_5680')
func_5681_call = mutated_mod.get_global_var('func_5681')
call_6543 = relay.TupleGetItem(func_5680_call(), 0)
call_6544 = relay.TupleGetItem(func_5681_call(), 0)
output = call_6543
output2 = call_6544
func_6560 = relay.Function([], output)
mod['func_6560'] = func_6560
mod = relay.transform.InferType()(mod)
mutated_mod['func_6560'] = func_6560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6560_call = mutated_mod.get_global_var('func_6560')
call_6561 = func_6560_call()
output = call_6561
func_6562 = relay.Function([], output)
mutated_mod['func_6562'] = func_6562
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6563 = relay.var("var_6563", dtype = "bool", shape = ())#candidate|6563|()|var|bool
var_6564 = relay.var("var_6564", dtype = "bool", shape = (1, 13, 12))#candidate|6564|(1, 13, 12)|var|bool
bop_6565 = relay.logical_and(var_6563.astype('bool'), var_6564.astype('bool')) # shape=(1, 13, 12)
func_4081_call = mod.get_global_var('func_4081')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_6597 = relay.TupleGetItem(func_4081_call(), 0)
call_6598 = relay.TupleGetItem(func_4082_call(), 0)
bop_6616 = relay.greater(bop_6565.astype('bool'), var_6563.astype('bool')) # shape=(1, 13, 12)
func_5908_call = mod.get_global_var('func_5908')
func_5909_call = mutated_mod.get_global_var('func_5909')
call_6619 = relay.TupleGetItem(func_5908_call(), 2)
call_6620 = relay.TupleGetItem(func_5909_call(), 2)
output = relay.Tuple([call_6597,bop_6616,call_6619,])
output2 = relay.Tuple([call_6598,bop_6616,call_6620,])
func_6639 = relay.Function([var_6563,var_6564,], output)
mod['func_6639'] = func_6639
mod = relay.transform.InferType()(mod)
var_6640 = relay.var("var_6640", dtype = "bool", shape = ())#candidate|6640|()|var|bool
var_6641 = relay.var("var_6641", dtype = "bool", shape = (1, 13, 12))#candidate|6641|(1, 13, 12)|var|bool
output = func_6639(var_6640,var_6641,)
func_6642 = relay.Function([var_6640,var_6641,], output)
mutated_mod['func_6642'] = func_6642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6541_call = mod.get_global_var('func_6541')
func_6542_call = mutated_mod.get_global_var('func_6542')
call_6685 = relay.TupleGetItem(func_6541_call(), 1)
call_6686 = relay.TupleGetItem(func_6542_call(), 1)
output = relay.Tuple([call_6685,])
output2 = relay.Tuple([call_6686,])
func_6704 = relay.Function([], output)
mod['func_6704'] = func_6704
mod = relay.transform.InferType()(mod)
output = func_6704()
func_6705 = relay.Function([], output)
mutated_mod['func_6705'] = func_6705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4023_call = mod.get_global_var('func_4023')
func_4025_call = mutated_mod.get_global_var('func_4025')
call_6727 = relay.TupleGetItem(func_4023_call(), 3)
call_6728 = relay.TupleGetItem(func_4025_call(), 3)
func_4235_call = mod.get_global_var('func_4235')
func_4236_call = mutated_mod.get_global_var('func_4236')
call_6737 = relay.TupleGetItem(func_4235_call(), 0)
call_6738 = relay.TupleGetItem(func_4236_call(), 0)
output = relay.Tuple([call_6727,call_6737,])
output2 = relay.Tuple([call_6728,call_6738,])
func_6756 = relay.Function([], output)
mod['func_6756'] = func_6756
mod = relay.transform.InferType()(mod)
mutated_mod['func_6756'] = func_6756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6756_call = mutated_mod.get_global_var('func_6756')
call_6757 = func_6756_call()
output = call_6757
func_6758 = relay.Function([], output)
mutated_mod['func_6758'] = func_6758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4204_call = mod.get_global_var('func_4204')
func_4205_call = mutated_mod.get_global_var('func_4205')
call_6762 = relay.TupleGetItem(func_4204_call(), 0)
call_6763 = relay.TupleGetItem(func_4205_call(), 0)
output = relay.Tuple([call_6762,])
output2 = relay.Tuple([call_6763,])
func_6765 = relay.Function([], output)
mod['func_6765'] = func_6765
mod = relay.transform.InferType()(mod)
output = func_6765()
func_6766 = relay.Function([], output)
mutated_mod['func_6766'] = func_6766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5908_call = mod.get_global_var('func_5908')
func_5909_call = mutated_mod.get_global_var('func_5909')
call_6805 = relay.TupleGetItem(func_5908_call(), 1)
call_6806 = relay.TupleGetItem(func_5909_call(), 1)
func_6057_call = mod.get_global_var('func_6057')
func_6058_call = mutated_mod.get_global_var('func_6058')
call_6827 = relay.TupleGetItem(func_6057_call(), 0)
call_6828 = relay.TupleGetItem(func_6058_call(), 0)
func_2430_call = mod.get_global_var('func_2430')
func_2433_call = mutated_mod.get_global_var('func_2433')
call_6845 = relay.TupleGetItem(func_2430_call(relay.reshape(call_6827.astype('int8'), [6, 6, 8])), 0)
call_6846 = relay.TupleGetItem(func_2433_call(relay.reshape(call_6827.astype('int8'), [6, 6, 8])), 0)
func_4269_call = mod.get_global_var('func_4269')
func_4272_call = mutated_mod.get_global_var('func_4272')
const_6852 = relay.const([6,3,8,5,-4,5,4,8,-1,-2,-9,-7,2,-4,-2,5,10,-5,8,2,-9,-2,7,8,-3,4,1,7,-9,-6,-9,10,1,-2,7,8,2,-9,-4,-7,-1,-10,-2,6,7,-4,-5,8,4,-6,5,-7,6,6,-4,8,3,10,3,9,-9,8,9,-1,-7,4,-1,-1,-6,8,9,7,-1,9,10,4,1,3,-10,-3,-1,9,7,-10,6,-4,1,-8,6,-8,5,8,-6,8,-9,-10,-9,4,-8,8,2,8,-1,8,4,-8,10,7,-10,1,-5,10,10,9,-8,-4,8,4,6,9,-9,-1,4,6,-10,-3,-8,8,-7,-7,-3,-3,-1,-10,-2,1,7,-2,-7,-7,3,-3,-1,8,9,2,6,-2,-6,-8,-1,-2,8,-1,2,3,8,-8,-6,-8,4,6,7,9,-8,2,3,-2,-7,7,1,-7,-3,-9,-3,-5,-6,9,8,-7,-4,-10,2,-9,2,-8,-5,3,2,-8,-8,-2,-5,-8,-10,9,-3,-2,-8,-3,6,-7,-8,8,4,-5,-10,-9,-9,-7,-1,4,7,10,-8,8,-4,-6,7,2,-1,-6,-3,7,1,10,2,7,-1,-5,-9,2,9,-8,1,10,5,4,-10,-2,5,-4,-8,-4,-9,8,1,-3,-8,-9,-1,3,-8,5,-8,-8,9,-1,4,-5,-4,10,3,-10,-6,-9,9,-4,9,-4,6,-3,7,-1,-9,3,-1,1,-10,-4,9,3,7,6,7,-4,-3,6,-1,10,-7,-3,7,2,-6,-2,-2,-4,2,-5,-1,2,8,-3,-6,8,5,-4,7,8,2,10,-8,-3,6,1,-6,1,-10,-2,-7,-2,2,-5,-1,4,-4,9,1,-4,9,6,6,-1,4,-5,-4,3,4,-4,-10,10,3,8,1,-4,-7,6,-10,2,-10,6,5,-9,7,3,2,-5,-3,10,7,4,4,1,-9,-1,1,5,7,4,5,-5,-3,3,-3,1,7,-6,-9,9,10,-9,7,9,-5,-2,-2,-9,-5,-2,5,10,3,5,3,-10,-3,-5,10,-4,7,-7,-3,4,9,6,-3,6,-2,-6,4,-9,-2,5,8,-8,7,4,4,-6,5,-8,10,-4,4,7,-3,-5,1,-8,-1,-4,4,8,7,4,8,10,-8,2,4,2,-6,-4,-6,7,-1,-8,10,-4,2,9,-9,-9,5,9,-1,-7,-7,-5,3,4,5,-8,8,2,-1,-9,9,-9,9,4,-10,-6,-1,-4,5,8,-10,6,10,9,6,4,-7,-2,3,-4,-4,-2,1,9,5,-7,4,4,-9,7,-2,5,-6,-4,10,3,-8,8,4,5,-5,-4,-6,-2,1,4,-2,3,-3,-6,2,-8,-8,-10,-6,-10,9,-9,-2,4,2,-7,7,2,-6,5,-10,10,1,-10,7,7,6,3,-9,-3,6,-5,1,-5,6,7,-2,5,7,10,9,-1,3,3,2,-5,8,-1,7,-6,-5,2,9,3,-5,3,-10,9,10,-7,9,-3,2,-8,2,-6,8,-8,-5,7,4,4,-6,-9], dtype = "int64")#candidate|6852|(588,)|const|int64
call_6851 = relay.TupleGetItem(func_4269_call(relay.reshape(const_6852.astype('int64'), [588,])), 4)
call_6853 = relay.TupleGetItem(func_4272_call(relay.reshape(const_6852.astype('int64'), [588,])), 4)
func_4325_call = mod.get_global_var('func_4325')
func_4328_call = mutated_mod.get_global_var('func_4328')
call_6864 = relay.TupleGetItem(func_4325_call(relay.reshape(call_6805.astype('float32'), [3, 7, 16]), relay.reshape(const_6852.astype('int64'), [588,]), ), 4)
call_6865 = relay.TupleGetItem(func_4328_call(relay.reshape(call_6805.astype('float32'), [3, 7, 16]), relay.reshape(const_6852.astype('int64'), [588,]), ), 4)
output = relay.Tuple([call_6805,call_6827,call_6845,call_6851,const_6852,call_6864,])
output2 = relay.Tuple([call_6806,call_6828,call_6846,call_6853,const_6852,call_6865,])
func_6872 = relay.Function([], output)
mod['func_6872'] = func_6872
mod = relay.transform.InferType()(mod)
output = func_6872()
func_6873 = relay.Function([], output)
mutated_mod['func_6873'] = func_6873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4144_call = mod.get_global_var('func_4144')
func_4145_call = mutated_mod.get_global_var('func_4145')
call_6877 = func_4144_call()
call_6878 = func_4144_call()
output = relay.Tuple([call_6877,])
output2 = relay.Tuple([call_6878,])
func_6896 = relay.Function([], output)
mod['func_6896'] = func_6896
mod = relay.transform.InferType()(mod)
output = func_6896()
func_6897 = relay.Function([], output)
mutated_mod['func_6897'] = func_6897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6328_call = mod.get_global_var('func_6328')
func_6330_call = mutated_mod.get_global_var('func_6330')
call_6903 = relay.TupleGetItem(func_6328_call(), 1)
call_6904 = relay.TupleGetItem(func_6330_call(), 1)
output = call_6903
output2 = call_6904
func_6914 = relay.Function([], output)
mod['func_6914'] = func_6914
mod = relay.transform.InferType()(mod)
output = func_6914()
func_6915 = relay.Function([], output)
mutated_mod['func_6915'] = func_6915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4931_call = mod.get_global_var('func_4931')
func_4932_call = mutated_mod.get_global_var('func_4932')
call_6939 = relay.TupleGetItem(func_4931_call(), 0)
call_6940 = relay.TupleGetItem(func_4932_call(), 0)
output = call_6939
output2 = call_6940
func_6943 = relay.Function([], output)
mod['func_6943'] = func_6943
mod = relay.transform.InferType()(mod)
mutated_mod['func_6943'] = func_6943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6943_call = mutated_mod.get_global_var('func_6943')
call_6944 = func_6943_call()
output = call_6944
func_6945 = relay.Function([], output)
mutated_mod['func_6945'] = func_6945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5021_call = mod.get_global_var('func_5021')
func_5023_call = mutated_mod.get_global_var('func_5023')
call_7019 = func_5021_call()
call_7020 = func_5021_call()
output = call_7019
output2 = call_7020
func_7024 = relay.Function([], output)
mod['func_7024'] = func_7024
mod = relay.transform.InferType()(mod)
output = func_7024()
func_7025 = relay.Function([], output)
mutated_mod['func_7025'] = func_7025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5770_call = mod.get_global_var('func_5770')
func_5772_call = mutated_mod.get_global_var('func_5772')
call_7029 = func_5770_call()
call_7030 = func_5770_call()
func_6030_call = mod.get_global_var('func_6030')
func_6034_call = mutated_mod.get_global_var('func_6034')
const_7034 = relay.const([-8,8,10,-8,5,8,4,2,-8,-3,-5,-9,6,-4,-10,8,7,10,2,-8,1,-2,-4,7,1,6,-2,-4], dtype = "int8")#candidate|7034|(28,)|const|int8
const_7035 = relay.const([[-6.151459,8.360184,-0.773816,6.379954,-8.235474,1.237888,-9.327139,-5.781004,-9.836468,-5.059535,7.759134,6.101505,7.012809,7.269673,5.478240,-0.760115,-0.376271,-8.786267,-5.252197,-0.253169,-6.689425,-5.829390,-7.980083,3.747141,-9.425075,8.976421,-0.122305,5.352719,0.551223,7.698049,2.193505,5.426584,-2.712384,2.835784,1.041161,0.224569,1.045180,-7.627625,-8.005369,-4.555982,3.577643,-0.810079,-6.420813,4.028400,-8.923516,-0.125200,9.639920,-8.407262,8.207608,-0.608148,6.539442,1.998093,-7.930987,-3.376291,0.291118,7.192685,0.230788,-8.661185,0.159908,6.547053,3.654798,3.585601,4.475852,-7.750298,9.147947,5.748892,-8.691095,5.140603,-4.140991,6.739922,-4.049816,0.006253,-6.789815,-2.809168,1.929333,0.486305,7.409517,2.286303,-3.126101,-4.782473,6.490525,9.014696,-7.008173,-4.756508,-5.550235,-1.859271,-6.583763,-9.557343,3.011190,-8.845592,5.903300,7.453919,-5.867115,2.840770,-5.821680,1.363249,-6.388959,1.490841,1.922273,9.604782,6.669757,6.786990,4.579799,-1.115716,-2.690718,-3.029677,1.837325,-1.317214,-7.444241,-7.850609,0.845242,-6.463459,-4.349141,-9.228630,5.312402,-7.512055,5.930752,-2.830322,2.311544,-4.468516,1.345521,1.932043,-1.933665,6.267473,-5.953489,-3.677415,2.907717,5.798751,-4.431582,8.010497,6.021304,8.474034,6.401288,-4.670187,-8.176335,-8.763843,2.317535,-4.491537,-5.412574,-6.699606,-1.162961,-0.275775,-7.281834,9.163102,-5.816895,-8.930692,-8.725223,-0.845010,-3.646708,0.650360,5.169102,-9.360800,5.559528,9.165975,-6.702999,-9.486058,-0.888303,-4.193427,-3.434086,1.358956,6.931371,5.152450,1.332591,5.301026,-6.417990,0.581258,7.554983,-8.611340,-2.929927,-7.265727,0.918373,6.477569,3.857777,-8.990949,-4.281273,-6.458564,-4.336787,1.405844,-0.389136,6.958619,1.969216,-7.421011,-7.796385,-5.857258,-7.003107,-6.376571,9.547359,9.575799,2.205031,3.906990,-7.105182,1.905356,2.718670,-0.735128,-5.687322,-3.063515,-8.582743,-6.932693,2.562952,-9.807990,4.835919,3.840711,-2.710625,4.767968,9.956063,1.745452,1.471394,-2.588972,-4.130921,-3.447939,-4.030342,-0.224340,0.314691,0.876471,3.233532,5.597563,-4.384406,-2.668570,6.185047,8.200332,-1.154942,-0.005004,5.301388,-4.549043,-6.480362,-8.130250,3.574922,2.894302,2.793266,9.676733,-6.485213,3.643197,6.764688,-3.244182,-2.188221,2.875253,-3.937640,-8.739016,-3.359309,9.194402,2.756041,4.670616,0.810289,2.653547,-6.145758,9.734407,4.295330,1.785653,-6.285752,-6.078794,0.169373,9.361335,9.418605,-7.387839,-5.705398,-1.833508,7.251151,-9.700866,6.289906,-0.947428,-4.183931,-2.621592,-7.021977,4.627588,9.605479,4.714642,1.568515,6.561119,-9.073491,0.740701,6.533593,-4.434057,8.155565,6.992356,0.794023,-3.297531,-4.346899,5.727500,3.346223,4.590484,-5.334845,2.961254,-3.100018,4.200889,-3.705329,1.589945,-1.812954,3.732660,7.123989,-9.172317,-0.043262,-2.179226,-5.356492,8.766441,-9.034782,-2.213341,-1.106346,1.412453,-5.123331,4.511603,6.659503,2.633931,7.710645,7.349186,9.173229,6.081027,4.338853,-2.551906,4.076700,3.165510,3.581429,1.178614,8.601001,-2.916546,1.307710,3.878544,-7.520537,-7.390682,4.915010,-4.037311,-4.442757,-4.805053,-3.494415,0.657242,-7.142511,9.157169,-4.448168,5.845089,1.861620,-5.681324,-1.036888,8.339344,-8.823143,-4.409285,-2.295682,-9.414419,-7.386499,-5.573612,-7.321314,-6.939753,-6.288215,-1.937129,-8.140210,-1.212333,0.858169,-5.733903,-0.205491,-6.400303,-6.681370,-8.325864,-8.183714,4.543204,5.142285,8.028414,2.037895,7.332712,2.880207,-6.426933,5.405846,-3.960259,4.760961,-8.486140,-1.390356,-2.904780,2.266667,3.850620,-6.570683,-8.069419,-5.246287,2.425328,-1.194313,8.923243,-1.731848,0.535527,7.119617,-8.779971,2.744155,-1.511439,8.271314,-4.056710,-9.023966,-4.049122,-8.040474,-9.456906,-5.998363,-9.533902,-4.178303,8.335970,6.203221,5.663588,-8.347762,-8.727083,-4.548239,2.290993,8.126799,6.308949,-2.370118,-4.427863,-2.120073,8.332666,-3.716401,0.743090,-8.845087,3.174825,-0.513531,-9.412117,-1.597349,-5.131473,9.650528,6.401504,2.122220,-7.116109,-0.931835,-6.232258,-5.670511,-3.282850,2.129790,8.531317,-4.618397,0.300946,8.463169,0.858441,-2.828377,9.015434,7.942678,1.454496,7.036647,-8.718290,-0.798581,-7.561880,0.617217,-7.358476,0.153677,-3.586750,-3.646290,-3.432074,6.133755,-5.795254,6.463623,0.427503,-4.466073,6.756819,7.718715,1.488522,-2.642704,-4.997399,-0.065151,-1.982891]], dtype = "float64")#candidate|7035|(1, 448)|const|float64
call_7033 = relay.TupleGetItem(func_6030_call(relay.reshape(const_7034.astype('int8'), [28,]), relay.reshape(const_7035.astype('float64'), [448,]), ), 1)
call_7036 = relay.TupleGetItem(func_6034_call(relay.reshape(const_7034.astype('int8'), [28,]), relay.reshape(const_7035.astype('float64'), [448,]), ), 1)
func_4023_call = mod.get_global_var('func_4023')
func_4025_call = mutated_mod.get_global_var('func_4025')
call_7039 = relay.TupleGetItem(func_4023_call(), 1)
call_7040 = relay.TupleGetItem(func_4025_call(), 1)
func_1790_call = mod.get_global_var('func_1790')
func_1793_call = mutated_mod.get_global_var('func_1793')
const_7051 = relay.const([[-4.565267],[5.926681],[0.497060]], dtype = "float64")#candidate|7051|(3, 1)|const|float64
call_7050 = func_1790_call(relay.reshape(const_7051.astype('float64'), [1, 3, 1]))
call_7052 = func_1790_call(relay.reshape(const_7051.astype('float64'), [1, 3, 1]))
output = relay.Tuple([call_7029,call_7033,const_7034,const_7035,call_7039,call_7050,const_7051,])
output2 = relay.Tuple([call_7030,call_7036,const_7034,const_7035,call_7040,call_7052,const_7051,])
func_7053 = relay.Function([], output)
mod['func_7053'] = func_7053
mod = relay.transform.InferType()(mod)
output = func_7053()
func_7054 = relay.Function([], output)
mutated_mod['func_7054'] = func_7054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4081_call = mod.get_global_var('func_4081')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_7076 = relay.TupleGetItem(func_4081_call(), 0)
call_7077 = relay.TupleGetItem(func_4082_call(), 0)
output = relay.Tuple([call_7076,])
output2 = relay.Tuple([call_7077,])
func_7087 = relay.Function([], output)
mod['func_7087'] = func_7087
mod = relay.transform.InferType()(mod)
output = func_7087()
func_7088 = relay.Function([], output)
mutated_mod['func_7088'] = func_7088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6560_call = mod.get_global_var('func_6560')
func_6562_call = mutated_mod.get_global_var('func_6562')
call_7120 = func_6560_call()
call_7121 = func_6560_call()
func_5680_call = mod.get_global_var('func_5680')
func_5681_call = mutated_mod.get_global_var('func_5681')
call_7144 = relay.TupleGetItem(func_5680_call(), 0)
call_7145 = relay.TupleGetItem(func_5681_call(), 0)
func_6765_call = mod.get_global_var('func_6765')
func_6766_call = mutated_mod.get_global_var('func_6766')
call_7160 = relay.TupleGetItem(func_6765_call(), 0)
call_7161 = relay.TupleGetItem(func_6766_call(), 0)
func_6639_call = mod.get_global_var('func_6639')
func_6642_call = mutated_mod.get_global_var('func_6642')
const_7164 = relay.const(False, dtype = "bool")#candidate|7164|()|const|bool
var_7165 = relay.var("var_7165", dtype = "bool", shape = (156,))#candidate|7165|(156,)|var|bool
call_7163 = relay.TupleGetItem(func_6639_call(relay.reshape(const_7164.astype('bool'), []), relay.reshape(var_7165.astype('bool'), [1, 13, 12]), ), 1)
call_7166 = relay.TupleGetItem(func_6642_call(relay.reshape(const_7164.astype('bool'), []), relay.reshape(var_7165.astype('bool'), [1, 13, 12]), ), 1)
func_4704_call = mod.get_global_var('func_4704')
func_4705_call = mutated_mod.get_global_var('func_4705')
call_7179 = relay.TupleGetItem(func_4704_call(), 0)
call_7180 = relay.TupleGetItem(func_4705_call(), 0)
output = relay.Tuple([call_7120,call_7144,call_7160,call_7163,const_7164,var_7165,call_7179,])
output2 = relay.Tuple([call_7121,call_7145,call_7161,call_7166,const_7164,var_7165,call_7180,])
func_7183 = relay.Function([var_7165,], output)
mod['func_7183'] = func_7183
mod = relay.transform.InferType()(mod)
var_7184 = relay.var("var_7184", dtype = "bool", shape = (156,))#candidate|7184|(156,)|var|bool
output = func_7183(var_7184)
func_7185 = relay.Function([var_7184], output)
mutated_mod['func_7185'] = func_7185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6704_call = mod.get_global_var('func_6704')
func_6705_call = mutated_mod.get_global_var('func_6705')
call_7242 = relay.TupleGetItem(func_6704_call(), 0)
call_7243 = relay.TupleGetItem(func_6705_call(), 0)
func_4049_call = mod.get_global_var('func_4049')
func_4051_call = mutated_mod.get_global_var('func_4051')
call_7259 = relay.TupleGetItem(func_4049_call(), 0)
call_7260 = relay.TupleGetItem(func_4051_call(), 0)
const_7273 = relay.const([[[8,-2,-1,7,5,-5,-8,-1],[-3,3,-1,-3,2,-1,-6,9],[-7,10,4,-2,-3,-7,-9,5],[9,8,-4,7,5,-7,1,4],[8,5,-3,10,5,-8,-6,-6],[3,-6,-5,3,3,2,7,-1]],[[9,-9,-3,2,-6,2,-5,8],[-4,-5,1,8,9,7,5,-10],[-6,-1,-8,6,-5,-8,9,-8],[-4,2,10,-9,-2,-4,-6,5],[3,-10,-9,5,-5,4,-10,-8],[7,8,-2,6,-3,2,5,9]],[[5,9,6,-8,6,6,6,10],[4,1,-7,1,-1,9,-2,4],[-10,1,-6,8,5,-9,7,-4],[-1,10,-6,-8,-6,3,-9,-5],[-1,-4,7,10,-7,-3,-2,7],[6,1,-8,8,-8,-2,-9,6]],[[3,-6,4,-4,-9,-5,-6,4],[10,3,-6,2,4,-3,-10,1],[-10,6,7,3,9,-6,-2,6],[-6,2,1,-6,-9,-8,-7,-4],[9,1,2,-1,3,5,-8,7],[-3,5,-4,-1,-1,4,9,5]],[[2,4,-9,6,-2,7,-5,5],[-5,3,3,-6,2,-4,-2,1],[-6,-7,-1,9,5,3,-2,7],[1,1,-4,10,-7,-9,5,2],[-8,-8,-3,2,3,-9,6,-4],[-3,-2,-2,-3,9,7,-5,-7]],[[9,1,2,-3,1,-2,5,5],[-3,-7,9,1,5,4,-10,-2],[-6,-2,-8,-5,-6,-7,5,10],[-9,10,-10,-6,2,4,10,-10],[1,-5,8,8,-7,4,7,9],[-3,-3,-3,-8,10,-6,10,-7]]], dtype = "int8")#candidate|7273|(6, 6, 8)|const|int8
bop_7274 = relay.less(call_7242.astype('bool'), relay.reshape(const_7273.astype('bool'), relay.shape_of(call_7242))) # shape=(6, 6, 8)
bop_7277 = relay.less(call_7243.astype('bool'), relay.reshape(const_7273.astype('bool'), relay.shape_of(call_7243))) # shape=(6, 6, 8)
output = relay.Tuple([call_7259,bop_7274,])
output2 = relay.Tuple([call_7260,bop_7277,])
func_7295 = relay.Function([], output)
mod['func_7295'] = func_7295
mod = relay.transform.InferType()(mod)
mutated_mod['func_7295'] = func_7295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7295_call = mutated_mod.get_global_var('func_7295')
call_7296 = func_7295_call()
output = call_7296
func_7297 = relay.Function([], output)
mutated_mod['func_7297'] = func_7297
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7311 = relay.var("var_7311", dtype = "float32", shape = (15, 4, 13))#candidate|7311|(15, 4, 13)|var|float32
var_7312 = relay.var("var_7312", dtype = "float32", shape = (15, 4, 13))#candidate|7312|(15, 4, 13)|var|float32
bop_7313 = relay.mod(var_7311.astype('float32'), relay.reshape(var_7312.astype('float32'), relay.shape_of(var_7311))) # shape=(15, 4, 13)
func_2430_call = mod.get_global_var('func_2430')
func_2433_call = mutated_mod.get_global_var('func_2433')
const_7322 = relay.const([[-1],[3],[-10],[-2],[-3],[4],[4],[-10],[7],[4],[1],[-6],[3],[1],[-7],[-4],[-1],[4],[-5],[6],[9],[10],[8],[-2],[9],[-10],[-10],[-3],[4],[-4],[4],[1],[6],[-9],[-4],[-8],[5],[-6],[7],[-7],[6],[9],[6],[6],[5],[-2],[1],[-4],[-1],[-5],[-10],[-7],[1],[9],[1],[-6],[-3],[-2],[4],[-10],[-9],[8],[6],[-6],[-9],[-1],[6],[-5],[3],[-4],[-9],[-1],[5],[3],[1],[-10],[6],[2],[-4],[-8],[-1],[-5],[10],[3],[5],[8],[-10],[-8],[2],[6],[-5],[-4],[8],[2],[6],[6],[-10],[4],[10],[-3],[-5],[-9],[-2],[9],[6],[-5],[-4],[1],[-9],[-4],[2],[2],[-9],[-4],[-2],[-4],[-10],[1],[7],[5],[-5],[-6],[1],[1],[-10],[-5],[-4],[-6],[3],[-2],[9],[-3],[10],[-10],[-4],[-2],[-7],[-10],[-8],[10],[-5],[-2],[-2],[-2],[8],[-10],[-1],[-5],[-5],[-7],[2],[-9],[-2],[9],[7],[9],[2],[1],[-10],[9],[-6],[-3],[1],[9],[5],[-6],[7],[-5],[-4],[10],[2],[5],[1],[-10],[-8],[6],[-9],[2],[-9],[8],[9],[10],[-1],[7],[-9],[-9],[4],[-7],[-2],[5],[7],[6],[2],[-7],[-1],[6],[1],[7],[3],[7],[9],[-5],[2],[10],[-10],[-5],[-6],[-4],[-3],[1],[6],[-5],[5],[8],[6],[-10],[-3],[-1],[-6],[2],[4],[2],[10],[-8],[8],[8],[-9],[10],[-7],[-10],[6],[-9],[4],[6],[9],[-3],[-5],[2],[-4],[8],[-2],[-6],[1],[4],[4],[10],[-5],[-9],[-9],[6],[-4],[10],[7],[-5],[-4],[5],[-1],[-6],[-6],[-10],[-6],[2],[-9],[10],[-7],[5],[-9],[-1],[9],[-9],[10],[9],[-4],[-4],[7],[3],[-4],[7],[-6],[-1],[-3],[-4],[-1],[9],[10],[-3],[2],[2]], dtype = "int8")#candidate|7322|(288, 1)|const|int8
call_7321 = relay.TupleGetItem(func_2430_call(relay.reshape(const_7322.astype('int8'), [6, 6, 8])), 0)
call_7323 = relay.TupleGetItem(func_2433_call(relay.reshape(const_7322.astype('int8'), [6, 6, 8])), 0)
bop_7344 = relay.floor_divide(bop_7313.astype('float64'), relay.reshape(var_7311.astype('float64'), relay.shape_of(bop_7313))) # shape=(15, 4, 13)
output = relay.Tuple([call_7321,const_7322,bop_7344,])
output2 = relay.Tuple([call_7323,const_7322,bop_7344,])
func_7357 = relay.Function([var_7311,var_7312,], output)
mod['func_7357'] = func_7357
mod = relay.transform.InferType()(mod)
var_7358 = relay.var("var_7358", dtype = "float32", shape = (15, 4, 13))#candidate|7358|(15, 4, 13)|var|float32
var_7359 = relay.var("var_7359", dtype = "float32", shape = (15, 4, 13))#candidate|7359|(15, 4, 13)|var|float32
output = func_7357(var_7358,var_7359,)
func_7360 = relay.Function([var_7358,var_7359,], output)
mutated_mod['func_7360'] = func_7360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4235_call = mod.get_global_var('func_4235')
func_4236_call = mutated_mod.get_global_var('func_4236')
call_7410 = relay.TupleGetItem(func_4235_call(), 0)
call_7411 = relay.TupleGetItem(func_4236_call(), 0)
output = call_7410
output2 = call_7411
func_7413 = relay.Function([], output)
mod['func_7413'] = func_7413
mod = relay.transform.InferType()(mod)
mutated_mod['func_7413'] = func_7413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7413_call = mutated_mod.get_global_var('func_7413')
call_7414 = func_7413_call()
output = call_7414
func_7415 = relay.Function([], output)
mutated_mod['func_7415'] = func_7415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5908_call = mod.get_global_var('func_5908')
func_5909_call = mutated_mod.get_global_var('func_5909')
call_7450 = relay.TupleGetItem(func_5908_call(), 1)
call_7451 = relay.TupleGetItem(func_5909_call(), 1)
func_4811_call = mod.get_global_var('func_4811')
func_4812_call = mutated_mod.get_global_var('func_4812')
call_7453 = func_4811_call()
call_7454 = func_4811_call()
output = relay.Tuple([call_7450,call_7453,])
output2 = relay.Tuple([call_7451,call_7454,])
func_7455 = relay.Function([], output)
mod['func_7455'] = func_7455
mod = relay.transform.InferType()(mod)
mutated_mod['func_7455'] = func_7455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7455_call = mutated_mod.get_global_var('func_7455')
call_7456 = func_7455_call()
output = call_7456
func_7457 = relay.Function([], output)
mutated_mod['func_7457'] = func_7457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7455_call = mod.get_global_var('func_7455')
func_7457_call = mutated_mod.get_global_var('func_7457')
call_7477 = relay.TupleGetItem(func_7455_call(), 0)
call_7478 = relay.TupleGetItem(func_7457_call(), 0)
output = relay.Tuple([call_7477,])
output2 = relay.Tuple([call_7478,])
func_7511 = relay.Function([], output)
mod['func_7511'] = func_7511
mod = relay.transform.InferType()(mod)
mutated_mod['func_7511'] = func_7511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7511_call = mutated_mod.get_global_var('func_7511')
call_7512 = func_7511_call()
output = call_7512
func_7513 = relay.Function([], output)
mutated_mod['func_7513'] = func_7513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7413_call = mod.get_global_var('func_7413')
func_7415_call = mutated_mod.get_global_var('func_7415')
call_7581 = func_7413_call()
call_7582 = func_7413_call()
output = call_7581
output2 = call_7582
func_7590 = relay.Function([], output)
mod['func_7590'] = func_7590
mod = relay.transform.InferType()(mod)
mutated_mod['func_7590'] = func_7590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7590_call = mutated_mod.get_global_var('func_7590')
call_7591 = func_7590_call()
output = call_7591
func_7592 = relay.Function([], output)
mutated_mod['func_7592'] = func_7592
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7606 = relay.var("var_7606", dtype = "float64", shape = (8, 7, 7))#candidate|7606|(8, 7, 7)|var|float64
uop_7607 = relay.tan(var_7606.astype('float64')) # shape=(8, 7, 7)
func_4665_call = mod.get_global_var('func_4665')
func_4666_call = mutated_mod.get_global_var('func_4666')
call_7611 = relay.TupleGetItem(func_4665_call(), 0)
call_7612 = relay.TupleGetItem(func_4666_call(), 0)
func_4704_call = mod.get_global_var('func_4704')
func_4705_call = mutated_mod.get_global_var('func_4705')
call_7622 = relay.TupleGetItem(func_4704_call(), 0)
call_7623 = relay.TupleGetItem(func_4705_call(), 0)
func_4269_call = mod.get_global_var('func_4269')
func_4272_call = mutated_mod.get_global_var('func_4272')
var_7633 = relay.var("var_7633", dtype = "int64", shape = (588,))#candidate|7633|(588,)|var|int64
call_7632 = relay.TupleGetItem(func_4269_call(relay.reshape(var_7633.astype('int64'), [588,])), 2)
call_7634 = relay.TupleGetItem(func_4272_call(relay.reshape(var_7633.astype('int64'), [588,])), 2)
uop_7635 = relay.acos(var_7633.astype('float64')) # shape=(588,)
var_7641 = relay.var("var_7641", dtype = "float64", shape = (588,))#candidate|7641|(588,)|var|float64
bop_7642 = relay.left_shift(uop_7635.astype('uint8'), relay.reshape(var_7641.astype('uint8'), relay.shape_of(uop_7635))) # shape=(588,)
func_6328_call = mod.get_global_var('func_6328')
func_6330_call = mutated_mod.get_global_var('func_6330')
call_7646 = relay.TupleGetItem(func_6328_call(), 1)
call_7647 = relay.TupleGetItem(func_6330_call(), 1)
output = relay.Tuple([uop_7607,call_7611,call_7622,call_7632,bop_7642,call_7646,])
output2 = relay.Tuple([uop_7607,call_7612,call_7623,call_7634,bop_7642,call_7647,])
func_7652 = relay.Function([var_7606,var_7633,var_7641,], output)
mod['func_7652'] = func_7652
mod = relay.transform.InferType()(mod)
var_7653 = relay.var("var_7653", dtype = "float64", shape = (8, 7, 7))#candidate|7653|(8, 7, 7)|var|float64
var_7654 = relay.var("var_7654", dtype = "int64", shape = (588,))#candidate|7654|(588,)|var|int64
var_7655 = relay.var("var_7655", dtype = "float64", shape = (588,))#candidate|7655|(588,)|var|float64
output = func_7652(var_7653,var_7654,var_7655,)
func_7656 = relay.Function([var_7653,var_7654,var_7655,], output)
mutated_mod['func_7656'] = func_7656
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7666 = relay.var("var_7666", dtype = "float64", shape = (4, 6, 12))#candidate|7666|(4, 6, 12)|var|float64
uop_7667 = relay.atan(var_7666.astype('float64')) # shape=(4, 6, 12)
func_5021_call = mod.get_global_var('func_5021')
func_5023_call = mutated_mod.get_global_var('func_5023')
call_7674 = func_5021_call()
call_7675 = func_5021_call()
output = relay.Tuple([uop_7667,call_7674,])
output2 = relay.Tuple([uop_7667,call_7675,])
func_7678 = relay.Function([var_7666,], output)
mod['func_7678'] = func_7678
mod = relay.transform.InferType()(mod)
mutated_mod['func_7678'] = func_7678
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7679 = relay.var("var_7679", dtype = "float64", shape = (4, 6, 12))#candidate|7679|(4, 6, 12)|var|float64
func_7678_call = mutated_mod.get_global_var('func_7678')
call_7680 = func_7678_call(var_7679)
output = call_7680
func_7681 = relay.Function([var_7679], output)
mutated_mod['func_7681'] = func_7681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7590_call = mod.get_global_var('func_7590')
func_7592_call = mutated_mod.get_global_var('func_7592')
call_7708 = func_7590_call()
call_7709 = func_7590_call()
func_7590_call = mod.get_global_var('func_7590')
func_7592_call = mutated_mod.get_global_var('func_7592')
call_7712 = func_7590_call()
call_7713 = func_7590_call()
func_6225_call = mod.get_global_var('func_6225')
func_6229_call = mutated_mod.get_global_var('func_6229')
const_7724 = relay.const([-3,9,-6,-4,10,1,-10,-1,-2,5,9,-10,5,-9,8,4,-9,-3,-4,3,-4,1,5,-3,7,2,1,8,3,4,-3,5,3,-8,2,-3,6,-2,-6,-7,-3,10,10,10,5,-9,2,10,-9,-4,-2,9,9,-6,-8,-9,-1,-5,-6,6,-8,-8,6,-10,10,8,-9,7,-10,-4,-5,9,1,-7,-10,-6,8,3,-6,1,-4,-6,-5,2,6,-2,-8,-9,9,-4,8,9,6,4,-4,-5,-3,1,4,3,-9,2,-8,-4,6,-5,-8,4,6,-3,10,-9,1,-1,3,-4,1,-8,7,-5,10,9,6,-1,9,3,3,4,-1,-6,9,7,-8,-8,-8,9,-4,-5,2,-3,9,-10,-5,6,-9,10,-6,7,-3,10,9,7,-10,4,-8,2,-10,-2,7,2,-4,-6,-1,-6,-8,-6,-8,10,7,7,-8,5,-1,6,-8,-6,5,3,-4,2,5,-9,-1,10,-1,-5,8,-9,-10,-1,-5,1,8,6,4,6,-6,-2,-3,6,1,-5,3,2,-10,2,-9,-5,-8,10,1,-1,8,5,-8,-5,4,2,5,3,-4,-1,9,-1,-9,8,5,-6,-3,-6,3,1,-3,-7,6,2,-6,-4,-8,-1,-6,-6,8,-5,2,5,-5,3,1,4,1,-7,10,-3,8,7,4,-4,3,7,-3,1,9,5,3,7,-5,2,-8,4,-10,10,4,8,7,3,8,-9,-7,6,4,-3,-10,6,1,-5,-3,-4,-1,4,-8,10,-2,-2,3,-8,-1,-8,9,10,4,-8,-10,-3,5,-1,-6,-8,1,-7,7,-3,-10,9,5,-7,5,-7,10,-8,-7,7,-1,2,-4,-6,6,-9,-10,-6,-10,-5,10,9,-2,-2,-7,4,5,-10,5,-10,-5,9,-9,-10,8,5,-7,-6,1,-10,9,6,10,-1,-4,-7,-1,-4,-1,-1,-2,-5,-1,10,8,-2,-3,-9,6,1,-2,-7,-7,5,-7,-7,1,8,2,3,7,7], dtype = "int32")#candidate|7724|(384,)|const|int32
const_7725 = relay.const([1,-7,-10,8,2,8,8,5,5,4,-10,-1,8,8,-2,7,4,6,9,-10,5,-10,-3,1,-4,5,8,3,-4,7,8,1,-6,-8,10,5,5,10,-2,-5,6,10,-7,-1,-6,9,10,7,-7,-2,2,-4,-5,-4,-5,-3,10,6,6,8,-4,5,-7,2,7,2,-1,6,-3,3,9,1,-9,9,-2,7,-4,-2,5,6,9,-9,8,-6,-6,-9,7,8,-6,-1,-2,4,9,10,1,-5,-5,1,-2,6,-8,-4,-4,-10,7,-9,-10,-8,1,4,-3,-2,-5,-4,10,2,-5,-4,9,9,7,-9,-1,7,-5,3,10,-6,6,2,10,-5,-2,-3,-5,1,8,-9,6,-10,7,-9,-9,-3,-7,-1,9,-9,7,4,-4,-3,4,3,10,-3,7,5,8,-10,-3,9,9,4,2,9,4,8,4,10,-5,10,-6,9,-4,-7,2,-10,-8,8,-6,-7,8,10,7,7,-4,5,3,4,-2,6,-10,4,3,-7,-10,-9,10,-2,1,2,-8,7,-10,1,-3,8,3,1,-6,5,3,-2,-5,-1,-6,6,-9,-5,6,-4,3,2,2,2,-4,-3,2,1,2,6,4,-9,-4,5,-2,-9,-9,-1,-6,10,-9,-8,-8,8,8,7,-5,8,-3,-9,10,-10,-1,-1,-3,1,-3,2,-6,5,-6,8,9,1,9,-8,10,-9,8,-1,2,-4,-9,-10,9,-10,6,-6,-6,-10,7,-3,4,9,3,-5,-2,-9,5,5,-5,-7,-5,-9,-10,-5,4,5,1,2,-3,-8,-5,-7,8,-2,-9,5,2,2,-10,-8,-4,-6,8,-8,6,8,-2,-10,7,3,-3,-7,-10,-8,5,-9,-10,3,-3,-8,6,10,1,6,4,-1,6,3,-8,-10,-8,1,2,-5,-6,3,1,9,3,-7,5,-5,7,-10,-10,5,9,-7,3,-7,-7,2,-4,-9,6,-6,-5,5,3,-4,-6,-1,8,-6,-2,-1,-3,-6,-5,6,10,-4,6,-4,5,-10,-8,7,-10,6,-6,-10,1,10,10,7,9,-2,1,2,5,-10,-6,8,10,8,2,-6,4,7,3,4,5,7,-4,-5,-4,4,10,5,-8,5,-3,-3,9,2,3,-6,-2,6,3,-6,6,6,-6,5,6,-5,3,7,-9,-5,-3,-3,-3,2,2,-2,10,6,1,-9,1,5,4,-9,-10,-5,5,-7,-9,-6,-7,-1,10,-2,-7,5,8,6,-3,5,1,-6,10,-7,-4,-1,-5,9,-8,-4,3,4,1,-5,7,8,2,4,-7,2,-8,-2,3,-8,-4,5,4,-1,3,1,-6,8,3,9,-7,-3,1,-5,9,-5,-8,10,-2,-8,7,-7,-8,-8,-8,-3,7,9,-3,4,8,3,-10,7,-6,-8,-4,-3,-1,5,9,4,4,-5,8,9,7,-3,6,2,4,-4,-7,5,7,5,8,1,-3,-10,-6,-8,-2,-1,-10,2,-4,-4,-3,-7,9,-8,3,10,8,8,1,-8,-6,3,3,-10,2,-6,-5,7,8,10], dtype = "int64")#candidate|7725|(588,)|const|int64
call_7723 = relay.TupleGetItem(func_6225_call(relay.reshape(const_7724.astype('int32'), [8, 8, 6]), relay.reshape(const_7724.astype('bool'), [8, 8, 6]), relay.reshape(const_7725.astype('int64'), [588,]), ), 3)
call_7726 = relay.TupleGetItem(func_6229_call(relay.reshape(const_7724.astype('int32'), [8, 8, 6]), relay.reshape(const_7724.astype('bool'), [8, 8, 6]), relay.reshape(const_7725.astype('int64'), [588,]), ), 3)
func_5370_call = mod.get_global_var('func_5370')
func_5371_call = mutated_mod.get_global_var('func_5371')
call_7727 = relay.TupleGetItem(func_5370_call(), 2)
call_7728 = relay.TupleGetItem(func_5371_call(), 2)
func_6121_call = mod.get_global_var('func_6121')
func_6125_call = mutated_mod.get_global_var('func_6125')
const_7778 = relay.const([-0.467453,-6.997814,4.466933,-0.788684,-9.798650,8.959157,3.107929,-0.939594,4.557699,-3.712178,-7.113879,9.705471,2.934362,-3.906020,4.069461,3.637144,1.104637,7.018767,-9.741702,1.774301,-3.983084,-8.596081,5.636310,6.655718,3.526335,-5.948670,6.255280,3.478198,8.004077,8.416277,5.083142,-5.228238,-0.655254,4.408557,-4.413079,6.806268,9.721127,-4.704699,-9.576325,1.071599,0.678350,-0.531346,-2.368171,-4.023447,1.744936,-6.793401,-6.618650,1.074337,-2.071555,2.447431,-9.928161,-6.680459,-5.855791,-4.057543,-6.277788,-4.587269,1.684122,-3.219155,-5.084920,-7.378517,-9.133634,1.320342,7.379506,-0.713983,9.755201,-7.315694,-7.745124,-5.593449,9.890632,-4.603347,-0.660846,-3.141129,6.033249,1.907208,2.874893,8.714009,1.762200,-5.279923,8.530470,-7.335899,-9.700450,-8.715194,4.130414,0.633992,-9.704112,-1.225742,-5.464594,-3.432384,5.924923,-8.108464,0.409415,6.130599,-6.669950,-0.601205,-4.688612,-7.004517,5.025547,9.885969,5.046777,-0.272719,-1.767388,5.597334,3.891499,-4.925192,1.836877,3.430363,-0.511552,8.108212,-8.144659,5.822656,7.849763,9.859803,-5.152893,3.364867,6.424227,7.703869,9.977817,-9.947046,5.515466,4.124196,8.040633,8.480171,1.722380,-7.317883,-2.311430,-6.891807,-8.086863,8.087309,7.822751,-1.238114,-8.416921,-4.157135,-5.374763,-8.164077,-2.371495,4.921762,-4.976362,1.051480,7.052606,3.897705,4.796463,2.196437,1.518230,8.470540,-0.800123,2.973036,7.782382,-8.866276,-6.978978,7.887870,-8.431897,1.942419,-2.962089,2.311024,-5.427337,4.656646,-9.702202,4.576782,0.595904,-0.800663,0.007183,-9.796478,-3.785842,-6.102528,7.991198,5.980878,-7.030899,-1.086950,0.735198,4.483539,-9.568447,-7.367664,9.159480,-4.045407,-4.416430,-4.175181,-0.207742,-6.352113,1.534998,-3.895705,0.424226,4.388429,-4.780639,-3.327130,9.405023,4.476931,-2.594446,-9.393228,-5.255029,1.557454,-6.420554,-9.917781,-9.406934,8.864352,6.702210,7.034678,7.308525,6.674415,-1.327444,2.009646,3.344602,-1.656480,-0.610326,9.980642,1.447105,1.947974,2.000903,4.213076,3.891075,5.758326,-7.871504,2.641279,5.593744,7.710646,-4.506325,8.868914,2.997400,2.627664,3.736527,-4.314826,5.269229,-1.467350,7.016791,8.003920,-0.942965,-7.431237,2.382574,-6.281351,-6.179846,-9.162760,-5.174478,-1.954793,6.213795,-9.208290,-9.053663,-9.494778,-4.828210,-9.791772,-3.696220,-3.662584,5.665947,6.703151,-8.174019,2.737981,4.592110,0.690278,-0.934189,7.443597,-1.516595,-4.735110,1.570363,-3.285868,0.701208,7.711809,-9.567704,-1.298871,-3.165049,-0.682958,6.963919,3.119169,-2.832101,-3.009230,-0.428031,-3.528698,6.967205,-7.927293,0.930442,0.584860,5.815536,-0.706287,-0.344520,0.111337,-9.996582,-6.426631,-0.953041,-5.780280,-2.035026,6.031032,3.426182,7.697513,-2.571692,1.559158,7.618668,-1.755147,6.400571,-8.097755,8.893315,9.316457,-5.739797,0.667039,7.418433,6.673673,-5.875086,6.261950,-8.377180,9.813995,-3.929283,1.485452,3.569027,-3.009399,-5.668143,-9.157396,1.084955,-5.543139,9.349403,-4.263284,9.723504,3.781759,-2.347426,6.177695,9.460561,0.890328,8.082803,3.368791,-9.053203,-8.438231,6.387790,-9.911775,-0.413107,-7.909668,-1.303603,-0.810531,-7.685652,1.127137,-4.371122,1.507108,1.596470,5.528079,3.063076,7.963310,3.508195,1.935417,3.913293,2.991345,-8.329782,7.626823,-6.285055,-5.684052], dtype = "float64")#candidate|7778|(338,)|const|float64
const_7779 = relay.const([-9,1,-2,-6,3,-5,-7,-10,5,9,3,1,-5,-8,-8,-4,-3,6,-7,4,10,-8,2,-4,-1,-7,6,-2,3,-9,-3,7,-7,3,7,5,-9,-6,10,8,-2,6,2,-8,-10,-5,9,10,5,3,1,1,2,-10,7,6,2,-7,1,-1,-2,3,8,-1,-7,7,4,-7,-5,-1,-7,-2,-8,-5,-2,-10,-3,-8,-6,-4,-3,10,-6,4,-8,-4,1,-3,-2,-7,-7,3,-10,8,1,-9,-10,-2,10,8,2,-10,-7,-3,3,7,9,-9,10,4,-9,6,4,8,5,-9,-1,1,3,-8,5,8,7,2,-7,1,-9,-7,-4,-4,-4,-7,1,-2,-3,1,-8,-4,8,-4,-4,1,1,-6,-3,-7,5,-2,1,3,4,6,4,-1,-7,5,10,-5,-4,-8,-5,-3,-9,9,9,-8,5,-9,3,1,-4,1,4,5,-1,4,9,6,-2,-10,8,-6,-1,4,-4,5,-3,2,-4,-5,1,1,-7,-10,6,2,7,7,-2,3,7,-3,-4,-8,-1,3,2,-6,5,-6,5,2,-5,-1,9,-4,-9,7,-4,-2,-9,1,-1,8,10,-4,3,8,-7,6,10,-4,-9,-2,7,-9,9,8,6,5,-2,-2,6,-3,-8,1,-1,9,-6,-4,-7,1,-5,-5,7,-9,-10,5,3,-9,9,3,4,1,-4,-5,1,8,-9,9,4,6,-2,-10,-1,8,-8,9,4,2,-8,-1,-4,-5,2,8,5,-10,7,2,8,7,10,7,-7,-1,7,3,1,-6,-5,10,10,-5,-1,-4,-6,6,6,-9,6,9,-4,-7,-2,9,-9,5,1,8,-6,3,-3,5,4,-2,6,6,-4,4,-7,-1,-1,8,6,-6,-8,4,9,1,-5,-6,4,2,4,-4,-8,9,-3,3,-3,-4,9,-2,-9,-4,6,5,1,-10,3,7,-10,3,3,7,-5,9,-8,2,4,2,-7,9,-6,6,2,-3,10,-8,-1,9,5,-10,8,2,10,-1,-3,-7,-1,10,-6,8,10,9,10,-7,-7,-9,3,-7,5,1,2,9,-1,-9,-4,5,4,5,-3,10,-1,4,-10,8,1,-5,7,6,-5,-7,1,-10,7,8,10,-9,-7,-7,-6,-6,2,9,5,7,2,8,-7,8,-6,3,6,-8,-7,-2,10,9,9,-1,-5,6,-4,1,-5,-5,-7,6,10,-6,1,-9,8,-2,8,-3,6,10,-6,-3,-10,-1,-7,-8,-2,-6,-6,3,7,-1,1,-7,3,-6,8,9,10,-5,-6,-5,-9,1,-10,-7,10,-1,2,-7,-7,6,-4,3,3,-10,1,9,-8,5,-5,-2,-2,7,3,3,-6,-5,-1,6,-6,-5,2,9,6,-8,10,-7,5,8,-7,7,-7,-6,3,-4,-8,8,-3,-10,2,-10,-1,5,-3,5,-6,-3,-5,3,9,-6,6,-7,-10,-8,8,-5,8,-5,6,9,2,-5,1,4,-5,8,-6,-10,3,-1,9,10,-7,-6,-6,-5,7,5,7,-7,-4,6,10,-8,-6,-4,4,-10,-10,6,-1,2,10,-3,1,-1,-5,-4,-5,-7,-1,5,6,8,2,-2,6,9,3,3,4,-8,-3,3,7,8,-3,-3,6,7,-9,1,2,9,1,-1,10,-3,4,-10,8,-8,8,-1,7,4,-4,-9,-4,4,-4,10,6,6,9,-10,-3,7,-2,-8,4,-4,7,-7,-4,8,-5,2,2,-1,4,-10,-10,10,7,10,2,-2,-7,-1,9,9,-8,5,-10,2,6,3,-3,9,-1,-1,-4,3,1,2,-3,-4,-3,2,-3,-7,8,-6,-1,1,5,6,-3,1,-4,4,6,-10,-4,2,7,-8,-7,8,-1,-3,-10,-8,-9,7,-3,-3,-8,8,5,1,9,-1,-4,-6,9,-5,-8,2,-3,-3,1,-5,-10,2,5,9,1,-10,-8,-1,-8,6,9,-5,8,-9,5,9,-7,1,4,-5,10,1,-4,7,-9,7,-2,10,-2,10,-5,3,9,5,5,-6,5,-7,2,-8,8,8,-8,1,-1,7,7,7], dtype = "uint16")#candidate|7779|(784,)|const|uint16
call_7777 = relay.TupleGetItem(func_6121_call(relay.reshape(const_7778.astype('float64'), [13, 2, 13]), relay.reshape(const_7779.astype('uint16'), [784,]), relay.reshape(const_7725.astype('int64'), [588,]), ), 8)
call_7780 = relay.TupleGetItem(func_6125_call(relay.reshape(const_7778.astype('float64'), [13, 2, 13]), relay.reshape(const_7779.astype('uint16'), [784,]), relay.reshape(const_7725.astype('int64'), [588,]), ), 8)
output = relay.Tuple([call_7708,call_7712,call_7723,const_7724,const_7725,call_7727,call_7777,const_7778,const_7779,])
output2 = relay.Tuple([call_7709,call_7713,call_7726,const_7724,const_7725,call_7728,call_7780,const_7778,const_7779,])
func_7788 = relay.Function([], output)
mod['func_7788'] = func_7788
mod = relay.transform.InferType()(mod)
mutated_mod['func_7788'] = func_7788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7788_call = mutated_mod.get_global_var('func_7788')
call_7789 = func_7788_call()
output = call_7789
func_7790 = relay.Function([], output)
mutated_mod['func_7790'] = func_7790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5370_call = mod.get_global_var('func_5370')
func_5371_call = mutated_mod.get_global_var('func_5371')
call_7881 = relay.TupleGetItem(func_5370_call(), 3)
call_7882 = relay.TupleGetItem(func_5371_call(), 3)
uop_7904 = relay.sqrt(call_7881.astype('float64')) # shape=(14, 42)
uop_7906 = relay.sqrt(call_7882.astype('float64')) # shape=(14, 42)
func_6896_call = mod.get_global_var('func_6896')
func_6897_call = mutated_mod.get_global_var('func_6897')
call_7908 = relay.TupleGetItem(func_6896_call(), 0)
call_7909 = relay.TupleGetItem(func_6897_call(), 0)
output = relay.Tuple([uop_7904,call_7908,])
output2 = relay.Tuple([uop_7906,call_7909,])
func_7918 = relay.Function([], output)
mod['func_7918'] = func_7918
mod = relay.transform.InferType()(mod)
mutated_mod['func_7918'] = func_7918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7918_call = mutated_mod.get_global_var('func_7918')
call_7919 = func_7918_call()
output = call_7919
func_7920 = relay.Function([], output)
mutated_mod['func_7920'] = func_7920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4931_call = mod.get_global_var('func_4931')
func_4932_call = mutated_mod.get_global_var('func_4932')
call_7929 = relay.TupleGetItem(func_4931_call(), 0)
call_7930 = relay.TupleGetItem(func_4932_call(), 0)
func_5525_call = mod.get_global_var('func_5525')
func_5529_call = mutated_mod.get_global_var('func_5529')
var_7977 = relay.var("var_7977", dtype = "float64", shape = (2, 504))#candidate|7977|(2, 504)|var|float64
const_7978 = relay.const([10,6,1,-4,-2,3,8,1,-2,-2,9,-5,2,-7,6,-6,5,8,-3,-4,-3,-4,4,10,4,-3,10,7], dtype = "int8")#candidate|7978|(28,)|const|int8
const_7979 = relay.const([-7.928605,2.675663,1.208624,2.163652,-6.354873,8.519046,0.581098,6.067818,-3.700446,9.698877,-7.693984,1.404605,-8.563165,-1.340516,8.856878,-0.911775,-9.120821,-1.130069,-2.605157,9.350393,3.218955,3.747411,-8.022052,4.763077,-7.867739,9.665172,4.700047,5.962259,2.391270,-1.012730,5.017094,5.214102,-4.415553,-8.273589,8.948836,6.790896,-4.759886,-7.247284,2.644573,9.823614,-7.151067,1.554141,-2.894428,-9.199472,-1.585526,-2.994472,6.647778,0.396319,4.720064,-1.246974,-0.872203,7.722897,-3.786418,9.446630,4.319590,5.613764,0.982292,-9.295853,8.197452,4.228227,6.229688,-4.522454,9.900812,-4.268121,9.934898,-4.384827,-6.058628,-1.144412,9.463351,-4.051761,3.395084,-9.198904,-6.469820,-7.490635,2.214389,-8.234306,6.389158,3.204340,-8.414553,0.972576,-0.627089,2.244165,-5.690673,0.864226,2.595634,-4.123073,-3.622926,2.803374,4.496898,-1.446066,-6.953993,7.230207,4.790462,-9.159738,-4.729305,7.440591,4.237948,9.353860,9.167397,3.337070,2.355126,7.257443,2.053110,-2.980311,-7.435258,2.042043,4.028196,-3.032029,-6.826989,6.619034,-0.272919,9.712974,7.558336,1.870052,-9.650096,-4.257969,9.378074,4.892001,-6.010039,2.986428,-7.177505,7.805857,-6.544464,4.004897,6.073707,7.414609,8.245979,7.551962,-3.229127,7.240399,-9.601102,-9.908740,1.977120,-7.383662,3.147096,-6.061996,-2.579600,-5.085756,8.964269,2.098818,-1.298322,4.682073,-0.105373,-6.571680,3.025353,6.332604,5.135649,4.845951,9.036178,8.860696,-2.939425,-0.819127,8.708830,5.510853,-6.727849,2.247658,9.765421,3.396338,-2.825861,-0.951324,8.784911,2.433476,6.398930,-8.318723,-0.011742,-6.604995,8.075413,6.538984,2.276691,-2.312099,-7.362421,-5.300498,-2.562370,4.063198,8.327027,-5.148473,1.306644,-4.308269,5.559512,0.350231,-3.821216,-2.416257,-5.749276,-7.161956,-9.575890,-4.935851,3.442389,-7.161586,-0.311165,-7.627909,-0.702216,-5.348162,-2.694701,-6.016557,4.499737,7.720438,4.750622,-0.509631,9.807828,9.048506,7.809956,-5.651002,-3.313509,-1.243757,-8.476946,7.813374,1.237563,-1.632897,-7.921902,3.506618,-5.595263,5.007319,-2.511463,-8.969735,-0.107846,9.970704,8.062024,-2.712549,9.232701,-4.992465,4.166603,-2.049219,6.205323,-9.305825,0.360593,-8.483204,-3.383943,-7.628922,4.164303,4.539465,-2.266379,7.781474,-1.445724,-7.837549,-2.110050,-8.044527,-7.383702,-6.557333,3.749699,8.634594,8.394280,9.015246,4.784445,-8.055861,-6.348873,-5.708281,9.861048,-6.793212,-6.334467,6.348464,4.160128,-9.169335,-0.754191,3.658008,-2.063019,-1.178503,-4.973216,0.665532,9.153578,-9.605731,7.654365,2.135676,-4.368707,6.939944,-5.741722,7.807786,-5.253208,8.506944,6.499241,-6.490033,3.136996,2.323941,-2.424394,6.677319,-8.241685,6.610693,-3.308712,-0.543950,-3.070978,8.878376,-9.014112,-5.006908,7.106661,0.234566,9.692163,-9.351364,2.225809,-6.162649,-1.708484,6.453626,-4.316458,0.612507,3.997910,7.454932,4.535670,-1.744609,-4.943649,-4.944645,-2.240280,-7.585182,6.359066,-4.892533,-3.200570,1.569476,-8.717081,5.793276,0.740246,-7.834395,0.039004,9.179965,-2.592026,-1.674956,-3.989454,-5.221465,4.413773,-4.786736,6.136735,5.500717,-6.619961,1.199416,5.605715,6.979836,1.272597,-2.779911,3.107121,2.926457,2.485742,-1.338274,-5.713850,5.953920,2.153503,-0.278077,-8.964121,-8.988488,-9.479273,-0.828824,5.813902,0.458460,6.739705,0.845236,5.011228,-8.197609,-3.487980,-5.818686,-3.609903,-2.648680,-6.609910,-9.528657,-1.066652,9.024861,-4.772171,4.570350,5.812260,-2.415438,-4.743164,8.572670,-9.950041,-0.018936,0.201271,8.086115,-1.693663,3.597607,0.920887,-3.087581,4.213562,-3.407309,6.087962,7.966367,-1.279833,3.553006,4.179853,-3.528330,-2.626234,-3.119019,-4.572870,9.924779,-1.848891,4.495969,7.679921,4.202209,2.215053,-1.510503,9.968149,0.441497,-3.216745,-6.967602,8.435260,1.352841,-8.741451,2.388396,-3.113661,9.059323,-2.783189,-2.643824,-2.252182,-4.941691,3.801051,-8.647596,-0.455118,9.713355,-4.234340,-7.277185,-8.966466,-5.239943,5.447659,7.643599,-4.294892,-9.503145,4.975529,-2.921361,8.696864,6.965515,-2.698499,0.608316,1.742455,1.314973,6.131596,-9.483713,5.321920,-8.131601,-9.147680,-2.863117,-6.729548,7.701659,7.222440,-2.912509,-2.923232,-5.518383,8.622219,3.448112,-5.227532,4.868558,-4.057296,3.725235,-3.874165,5.591045,-0.503347,6.357965,-0.024421,-4.757727,5.919593,-3.248394,0.630529,-6.476726,0.348527,1.183260,-5.774969,8.490470], dtype = "float64")#candidate|7979|(448,)|const|float64
call_7976 = relay.TupleGetItem(func_5525_call(relay.reshape(var_7977.astype('float64'), [9, 7, 16]), relay.reshape(const_7978.astype('int8'), [28,]), relay.reshape(const_7979.astype('float64'), [4, 7, 16]), ), 3)
call_7980 = relay.TupleGetItem(func_5529_call(relay.reshape(var_7977.astype('float64'), [9, 7, 16]), relay.reshape(const_7978.astype('int8'), [28,]), relay.reshape(const_7979.astype('float64'), [4, 7, 16]), ), 3)
var_7985 = relay.var("var_7985", dtype = "float64", shape = (2, 504))#candidate|7985|(2, 504)|var|float64
bop_7986 = relay.logical_or(var_7977.astype('bool'), relay.reshape(var_7985.astype('bool'), relay.shape_of(var_7977))) # shape=(2, 504)
func_4811_call = mod.get_global_var('func_4811')
func_4812_call = mutated_mod.get_global_var('func_4812')
call_7991 = func_4811_call()
call_7992 = func_4811_call()
uop_8002 = relay.log(var_7977.astype('float32')) # shape=(2, 504)
output = relay.Tuple([call_7929,call_7976,const_7978,const_7979,bop_7986,call_7991,uop_8002,])
output2 = relay.Tuple([call_7930,call_7980,const_7978,const_7979,bop_7986,call_7992,uop_8002,])
func_8004 = relay.Function([var_7977,var_7985,], output)
mod['func_8004'] = func_8004
mod = relay.transform.InferType()(mod)
mutated_mod['func_8004'] = func_8004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8004_call = mutated_mod.get_global_var('func_8004')
var_8006 = relay.var("var_8006", dtype = "float64", shape = (2, 504))#candidate|8006|(2, 504)|var|float64
var_8007 = relay.var("var_8007", dtype = "float64", shape = (2, 504))#candidate|8007|(2, 504)|var|float64
call_8005 = func_8004_call(var_8006,var_8007,)
output = call_8005
func_8008 = relay.Function([var_8006,var_8007,], output)
mutated_mod['func_8008'] = func_8008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4204_call = mod.get_global_var('func_4204')
func_4205_call = mutated_mod.get_global_var('func_4205')
call_8025 = relay.TupleGetItem(func_4204_call(), 0)
call_8026 = relay.TupleGetItem(func_4205_call(), 0)
func_4049_call = mod.get_global_var('func_4049')
func_4051_call = mutated_mod.get_global_var('func_4051')
call_8027 = relay.TupleGetItem(func_4049_call(), 0)
call_8028 = relay.TupleGetItem(func_4051_call(), 0)
output = relay.Tuple([call_8025,call_8027,])
output2 = relay.Tuple([call_8026,call_8028,])
func_8033 = relay.Function([], output)
mod['func_8033'] = func_8033
mod = relay.transform.InferType()(mod)
output = func_8033()
func_8034 = relay.Function([], output)
mutated_mod['func_8034'] = func_8034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7053_call = mod.get_global_var('func_7053')
func_7054_call = mutated_mod.get_global_var('func_7054')
call_8105 = relay.TupleGetItem(func_7053_call(), 3)
call_8106 = relay.TupleGetItem(func_7054_call(), 3)
func_4510_call = mod.get_global_var('func_4510')
func_4515_call = mutated_mod.get_global_var('func_4515')
const_8109 = relay.const([7,-5,1,4,7,-6,10,3,-5,7,-1,2,-9,1,-4,-8,-10,7,-4,1,4,-6,-3,4,-7,4,9,6,-4,10,5,8,-4,-1,8,10,9,-6,4,10,10,7,-9,9,-2,-3,10,-4,-6,3,-7,6,10,8,-2,5,-4,1,-7,-9,3,8,3,8,-9,5,-3,-1,3,-6,10,4,6,-9,10,-2,2,-6,3,6,4,-5,-2,-9,8,9,9,-5,-1,-7,-4,3,10,5,-3,3,-4,-4,7,-1,-3,4,-4,-6,-5,5,4,7,9,-7,-3,-10,9,3,-1,2,7,-5,-6,7,6,3,9,-3,-2,-1,-1,3,-6,5,-3,1,-4,2,-7,-1,10,-2,4,7,8,-4,-8,-6,-5,4,-9,-9,-1,-2,9,-3,7,-8,-3,-10,1,-7,-3,7,-5,6,-6,-6,6,-7,-1,-4,6,-3,6,-9,7,10,-10,-6,8,10,8,10,5,-1,-8,9,8,2,-3,-3,-6,10,7,-10,9,8,-7,3,8,10,-10,1,-1,4,-3,-4,-7,4,2,1,-5,9,9,-5,6,6,-4,-6,9,9,-4,-8,9,8,-5,5,8,-1,-7,-8,2,9,-1,3,4,10,8,2,2,-1,9,-9,1,5,-6,9,7,6,-6,7,-2,9,-5,-7,10,-5,5,7,-4,2,-7,10,2,3,-6,7,5,9,-8,8,6,9,5,-7,-8,9,-1,-9,-6,10,-1,1,2,8,6,-10,-7,-6,-2,-1,4,-8,-8,8,9,5,5,-8,6,9,-3,-8,7,-3,9,-1,-6,7,-4,-10,-3,7,-3,-6,-2,-10,-3,5,2,-9,6,3,-7,-7,-5,7,4,-5,8,3,-8,5,3,3,10,8,2,-7,4,-1,3,-7,2,1,5,10,-8,7,6,9,-2,3,2,2,-6,-5,2,3,5,-4,1,-6,-10,2,-10,6,-2,3,-9,-8,-1,3,6,-9,-1,3,-8,2,-9,8,7,-1,-10,-1,-1,-3,5,-8,-3,3,-8,7,5,-6,4,-6,-5,-10,-1,-6,-1,7,-7,8,-9,-6,-7,-5,-10,1,-4,-5,-1,-7,-5,7,6,-3,-8,-4,1,-6,-1,-3,3,-5,10,-7,4,-5,9,-6,-7,-7,-9,2,9,10,-8,-2,-6,7,6,9,9,8,8,-4,-2,-2,2,-1,-3,-2,4,1,1,-8,-3,7,-2,4,9,-9,-9,-10,-6,-5,-1,-9,10,-7,-7,10,-3,-5,-1,7,7,1,-6,8,-3,10,-9,-1,6,-2,4,-4,-8,-3,8,-9,5,-8,2,-4,10,-8,-10,9,-6,10,2,6,3,-9,9,-3,-9,-9,10,7,-7,8,-4,3,6,10,9,8,-7,-4,-8,-5,9,-9,7,-8,10,2,-1,-4,2,6,3,-3,4,7,4,8,-5,-6,-2,-9,-10,-6,7,1,5,-1,3,9,1,9,9,3,-6,-6,-3,3,-7,-6,1,4,-5,6,-8,5,-10,-9,2,3,-8,8,-6,-7,-10,-7,-10,-6,-5,1,7,5,10,8,-5,-4,2,6,-3,-10,6,3,-10,1,1,-1,9,8,1,5,-7,-8,-9,6,9,-4,-7,3,5,-3,7,7,-1,7,-8,-5,-9,3,-1,-1,-7,7,3,-1,5,7,7,2,-6,7,1,-9,7,2,1,8,10,1,-9,-4,-6,8,6,1,-9,7,2,-2,-10,-9,-8,8,-4,3,-3,8,1,-3], dtype = "uint16")#candidate|8109|(660,)|const|uint16
var_8110 = relay.var("var_8110", dtype = "uint16", shape = (784,))#candidate|8110|(784,)|var|uint16
var_8111 = relay.var("var_8111", dtype = "int64", shape = (588,))#candidate|8111|(588,)|var|int64
call_8108 = relay.TupleGetItem(func_4510_call(relay.reshape(const_8109.astype('uint16'), [11, 10, 6]), relay.reshape(var_8110.astype('uint16'), [392, 2]), relay.reshape(var_8111.astype('int64'), [588,]), ), 5)
call_8112 = relay.TupleGetItem(func_4515_call(relay.reshape(const_8109.astype('uint16'), [11, 10, 6]), relay.reshape(var_8110.astype('uint16'), [392, 2]), relay.reshape(var_8111.astype('int64'), [588,]), ), 5)
output = relay.Tuple([call_8105,call_8108,const_8109,var_8110,var_8111,])
output2 = relay.Tuple([call_8106,call_8112,const_8109,var_8110,var_8111,])
func_8118 = relay.Function([var_8110,var_8111,], output)
mod['func_8118'] = func_8118
mod = relay.transform.InferType()(mod)
mutated_mod['func_8118'] = func_8118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8118_call = mutated_mod.get_global_var('func_8118')
var_8120 = relay.var("var_8120", dtype = "uint16", shape = (784,))#candidate|8120|(784,)|var|uint16
var_8121 = relay.var("var_8121", dtype = "int64", shape = (588,))#candidate|8121|(588,)|var|int64
call_8119 = func_8118_call(var_8120,var_8121,)
output = call_8119
func_8122 = relay.Function([var_8120,var_8121,], output)
mutated_mod['func_8122'] = func_8122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7053_call = mod.get_global_var('func_7053')
func_7054_call = mutated_mod.get_global_var('func_7054')
call_8145 = relay.TupleGetItem(func_7053_call(), 0)
call_8146 = relay.TupleGetItem(func_7054_call(), 0)
func_4752_call = mod.get_global_var('func_4752')
func_4754_call = mutated_mod.get_global_var('func_4754')
var_8155 = relay.var("var_8155", dtype = "float32", shape = (336,))#candidate|8155|(336,)|var|float32
call_8154 = relay.TupleGetItem(func_4752_call(relay.reshape(var_8155.astype('float32'), [1, 336])), 2)
call_8156 = relay.TupleGetItem(func_4754_call(relay.reshape(var_8155.astype('float32'), [1, 336])), 2)
func_7788_call = mod.get_global_var('func_7788')
func_7790_call = mutated_mod.get_global_var('func_7790')
call_8161 = relay.TupleGetItem(func_7788_call(), 0)
call_8162 = relay.TupleGetItem(func_7790_call(), 0)
output = relay.Tuple([call_8145,call_8154,var_8155,call_8161,])
output2 = relay.Tuple([call_8146,call_8156,var_8155,call_8162,])
func_8165 = relay.Function([var_8155,], output)
mod['func_8165'] = func_8165
mod = relay.transform.InferType()(mod)
mutated_mod['func_8165'] = func_8165
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8166 = relay.var("var_8166", dtype = "float32", shape = (336,))#candidate|8166|(336,)|var|float32
func_8165_call = mutated_mod.get_global_var('func_8165')
call_8167 = func_8165_call(var_8166)
output = call_8167
func_8168 = relay.Function([var_8166], output)
mutated_mod['func_8168'] = func_8168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6943_call = mod.get_global_var('func_6943')
func_6945_call = mutated_mod.get_global_var('func_6945')
call_8186 = func_6943_call()
call_8187 = func_6943_call()
func_4325_call = mod.get_global_var('func_4325')
func_4328_call = mutated_mod.get_global_var('func_4328')
var_8209 = relay.var("var_8209", dtype = "float32", shape = (336,))#candidate|8209|(336,)|var|float32
const_8210 = relay.const([[-5,-2],[-10,2],[-3,-1],[-9,6],[8,-9],[1,-8],[3,-6],[9,-10],[3,-3],[7,9],[2,-1],[-10,8],[-6,-8],[2,-2],[3,10],[9,6],[4,-9],[7,-2],[-5,-1],[-1,4],[7,-6],[5,5],[-7,-1],[7,-2],[-9,3],[-6,-6],[-10,-9],[-7,8],[-4,-6],[-4,8],[10,-10],[9,9],[1,-5],[-8,2],[-7,9],[-2,9],[-3,7],[-9,-7],[-4,-3],[8,-2],[-5,6],[5,1],[8,7],[9,8],[-2,7],[9,8],[2,-6],[-7,-9],[-5,-6],[-4,-4],[7,4],[7,7],[-6,1],[-10,-7],[-4,3],[3,-2],[9,-9],[-2,-5],[2,6],[9,9],[8,9],[10,-2],[-10,4],[9,2],[-3,-8],[1,6],[1,5],[5,-7],[5,-1],[-3,9],[-10,-9],[-10,-4],[9,8],[7,5],[7,-10],[-3,5],[5,5],[9,-1],[7,-7],[-10,-10],[4,1],[3,9],[-8,-2],[6,-1],[3,8],[9,2],[-1,3],[-9,10],[-2,-5],[9,-8],[-1,-7],[8,-9],[-3,-5],[-8,8],[-8,-1],[-5,-2],[-4,-5],[9,7],[4,8],[-4,-4],[-5,7],[8,3],[8,4],[-6,2],[1,2],[-1,-9],[-5,-6],[7,-3],[-9,-8],[-8,4],[6,1],[4,4],[1,5],[-3,8],[3,-6],[-3,5],[-1,-8],[3,-7],[10,2],[1,9],[-10,-5],[-9,4],[4,6],[-8,9],[3,2],[-1,-6],[-7,5],[6,2],[-8,-2],[8,1],[-3,1],[-8,-5],[-10,-7],[-6,-4],[-3,2],[4,-5],[1,-9],[1,-4],[9,-8],[-8,5],[7,-8],[5,7],[10,-7],[-3,7],[8,-2],[-8,-5],[-2,1],[5,-7],[-8,-7],[-7,-2],[4,-3],[10,1],[-8,8],[9,-10],[-6,10],[-8,4],[-4,-10],[-5,-1],[-2,8],[-6,1],[-1,-7],[-2,-3],[1,10],[4,7],[6,8],[2,2],[4,7],[8,4],[-6,-4],[-10,-9],[-2,-10],[4,4],[-7,-1],[4,4],[-5,7],[-8,7],[-4,4],[-7,6],[-1,-6],[4,-3],[4,1],[-1,-5],[-3,-4],[-5,-6],[-9,2],[-1,-5],[-5,-7],[3,-1],[8,-3],[6,-7],[-10,1],[-1,4],[-5,-6],[-3,1],[2,-8],[-2,9],[2,8],[10,8],[-8,5],[5,-9],[-6,-9],[4,8],[9,-10],[-6,10],[-3,-5],[-8,4],[1,5],[-1,-6],[-7,-5],[-6,8],[10,10],[-9,3],[1,-6],[2,-6],[1,10],[-6,-6],[-5,6],[5,-1],[-2,-10],[-1,6],[4,4],[-3,-10],[-2,6],[-1,4],[5,-9],[4,7],[1,10],[2,-6],[7,2],[-10,4],[-5,1],[5,3],[-5,-2],[2,-8],[7,-7],[-3,5],[10,-10],[2,-4],[6,-4],[-3,1],[-1,9],[-4,-8],[-9,2],[-7,4],[4,10],[9,2],[9,6],[-5,10],[-2,1],[9,9],[-4,10],[7,9],[-7,7],[2,9],[5,3],[-2,8],[-3,-2],[-8,-10],[1,4],[-1,9],[-3,-4],[-6,-6],[8,-3],[-2,6],[9,10],[8,-2],[10,-9],[10,-1],[-4,5],[7,1],[1,-8],[4,-10],[2,2],[2,1],[9,-2],[-7,9],[-7,-1],[8,-2],[5,-3],[3,-6],[5,-7],[2,-8],[-9,10],[-5,-7],[-5,-9],[-10,3],[-10,-8],[2,-10],[-2,4],[6,-2],[2,10],[3,10],[-6,3],[9,-1]], dtype = "int64")#candidate|8210|(294, 2)|const|int64
call_8208 = relay.TupleGetItem(func_4325_call(relay.reshape(var_8209.astype('float32'), [3, 7, 16]), relay.reshape(const_8210.astype('int64'), [588,]), ), 5)
call_8211 = relay.TupleGetItem(func_4328_call(relay.reshape(var_8209.astype('float32'), [3, 7, 16]), relay.reshape(const_8210.astype('int64'), [588,]), ), 5)
output = relay.Tuple([call_8186,call_8208,var_8209,const_8210,])
output2 = relay.Tuple([call_8187,call_8211,var_8209,const_8210,])
func_8250 = relay.Function([var_8209,], output)
mod['func_8250'] = func_8250
mod = relay.transform.InferType()(mod)
mutated_mod['func_8250'] = func_8250
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8251 = relay.var("var_8251", dtype = "float32", shape = (336,))#candidate|8251|(336,)|var|float32
func_8250_call = mutated_mod.get_global_var('func_8250')
call_8252 = func_8250_call(var_8251)
output = call_8252
func_8253 = relay.Function([var_8251], output)
mutated_mod['func_8253'] = func_8253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5021_call = mod.get_global_var('func_5021')
func_5023_call = mutated_mod.get_global_var('func_5023')
call_8298 = func_5021_call()
call_8299 = func_5021_call()
uop_8300 = relay.asin(call_8298.astype('float64')) # shape=(6, 6, 8)
uop_8302 = relay.asin(call_8299.astype('float64')) # shape=(6, 6, 8)
uop_8304 = relay.sqrt(uop_8300.astype('float64')) # shape=(6, 6, 8)
uop_8306 = relay.sqrt(uop_8302.astype('float64')) # shape=(6, 6, 8)
func_6704_call = mod.get_global_var('func_6704')
func_6705_call = mutated_mod.get_global_var('func_6705')
call_8310 = relay.TupleGetItem(func_6704_call(), 0)
call_8311 = relay.TupleGetItem(func_6705_call(), 0)
func_5965_call = mod.get_global_var('func_5965')
func_5967_call = mutated_mod.get_global_var('func_5967')
call_8323 = relay.TupleGetItem(func_5965_call(), 0)
call_8324 = relay.TupleGetItem(func_5967_call(), 0)
func_4049_call = mod.get_global_var('func_4049')
func_4051_call = mutated_mod.get_global_var('func_4051')
call_8327 = relay.TupleGetItem(func_4049_call(), 0)
call_8328 = relay.TupleGetItem(func_4051_call(), 0)
output = relay.Tuple([uop_8304,call_8310,call_8323,call_8327,])
output2 = relay.Tuple([uop_8306,call_8311,call_8324,call_8328,])
func_8335 = relay.Function([], output)
mod['func_8335'] = func_8335
mod = relay.transform.InferType()(mod)
mutated_mod['func_8335'] = func_8335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8335_call = mutated_mod.get_global_var('func_8335')
call_8336 = func_8335_call()
output = call_8336
func_8337 = relay.Function([], output)
mutated_mod['func_8337'] = func_8337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6914_call = mod.get_global_var('func_6914')
func_6915_call = mutated_mod.get_global_var('func_6915')
call_8347 = func_6914_call()
call_8348 = func_6914_call()
func_5119_call = mod.get_global_var('func_5119')
func_5121_call = mutated_mod.get_global_var('func_5121')
call_8356 = func_5119_call()
call_8357 = func_5119_call()
func_1113_call = mod.get_global_var('func_1113')
func_1118_call = mutated_mod.get_global_var('func_1118')
const_8369 = relay.const([-9.853757,1.673283,0.943300,5.825035,4.512315,-5.215127,7.072384,-6.812162,-6.418610,-4.155009,1.940651,-1.611635,5.253133,6.378316,-1.932389,-5.046934,9.435504,-4.533990,-9.379883,8.193132,9.780378,1.499489,6.441704,8.533644,-1.372287,-0.284429,1.756471,-5.924753,6.486040,4.790932,7.366670,1.038453,-3.678383,2.267145,7.715162,-0.769602,8.624418,3.354798,0.338464,-1.006037,-4.443545,2.799478,5.286269,-7.718750,-9.625818,7.920594,8.835593,-0.818804,-4.049264,-1.796507,-2.890905,-9.128454,-5.487678,-0.028223,-6.099475,-9.154417,8.654083,-1.023536,8.668901,6.597121,4.488439,9.110914,5.009015,-2.985756,-7.680019,5.473719,6.635799,-0.703482,3.075371,0.607757,9.840519,-5.437630,8.887192,2.630861,4.279299,-5.575853,8.440925,7.922571,7.778649,-0.004011,-6.731399,-4.017974,2.712227,-5.292975,8.572436,0.390434,3.115903,0.159845,-3.426374,0.599976,-2.820052,-3.740873,8.697203,-5.313254,4.620497,-5.731389,1.731753,3.570459,7.604886,3.923393,2.908920,6.662661,5.093994,-2.246089,-5.590445,2.614621,2.565667,-8.216284,-7.143390,-2.176046,-1.899435,9.178373], dtype = "float32")#candidate|8369|(112,)|const|float32
const_8370 = relay.const([-6,-8,-8,6,1,-9,4,8,9,9,-2,-6,4,1,-1,2,-3,-6,-7,9,2,8,-1,9,-2,10,3,-8,5,6,-10,-5,3,3,6,9,1,3,-4,2,1,1,-7,1,-10,9,-7,2,6,9,-7,-9,6,10,4,-9,3,9,10,-3,-6,10,-5,-3,-6,-2,-9,-1,2,-8,-3,-3,4,6,3,4,-2,-3,7,-7,-6,-7,-9,-3,-8,-1,-5,-7,8,3,-5,-1,1,3,9,2,8,-2,6,1,-4,6,7,-10,-9,6,-10,-10,-2,1,-10,9,-10,6,-8,-1,9,4,1,3,-7,-1,-8,7,1,-3,1,-2,5,-7,4,7,-5,1,5,3,5,-10,-6,-4,5,9,-1,6,-8,-1,3,10,-1,2,-7,9,-1,-6,5,6,-9,-7,6,6,-8,-8,7,7,-1,5,7,9,-2,-7,-4,1,7,-4,1,7,-9,10,-5,5,7,-1,3,-4,-4,3,3,-1,-2,-3,7,4,-5,1,1,-5,5,7,-7,-4,-2,-10,1,-5,-8,-7,8,-8,-8,-4,-4,-9,4,-8,7,-3,9,5,-5,-4,-1,-8,4,2,7,-1,5,-2,8,-2,-10,-5,8,-8,2,-8,4,-10,1,8,-9,1,-1,-5,-2,1,3,10,7,6,1,10,1,-4,3,-2,-3,6,-5,2,-9,-9,10,-6,1,-4,-8,-10,6,3,7,2,6,5,-9,9,9,-2,1,-4,2,7,-4,-8,2,-10,7,-1,9,6,-3,8,7,1,-8,10,-4,-9,-5,-9,-10,-10,-10,-10,8,-7,-3,3,4,7,10,9,6,4,-5,-2,3,-10,2,-4,-7,1,5,-7,-9,-9,4,7,-6,-3,6,-5,-7,4,8,10,-8,-3,-7,1,9,-9,10,2,6,8,-3,3,-10,9,-4,3,-2,-6,-1,6,-7,-10,10,-4,9,10,-4,2,-7,-4,-2,4,5,2,7,5,-7,-10,9,5,5,-10,6,5,-4,6,-5,-7,-10,-6,1,10,8,-4,5,5,-3,-1,6,4,-4,-6,-3,-1,4,-10,1,-4,2,-4,-5,9,3,-9,-3,-8,5,5,-7,-1,-6,-9,-10,5,-8,1,9,5,7,10,-9,6,-4,-2,-9,-5,5,-1,-4,-9,7,-8,-9,6,-7,7,-9,-1,-5,-6,-5,1,-3,-7,1,9,-5,4,-2,-1,9,6,-10,-2,8,-9,-9,5,5,8,7,3,8,7,10,-8,5,-8,9,-9,-6,-3,3,6,1,3,5,3,5,-1,9,3,-3,10,1,-10,10,-3,-3,-10,-4,4,10,1,9,-10,3,-2,-6,-10,-4,5,6,-6,6,-5,10,10,-9,5,4,6,-9,-6,3,-4,-8,10,5,-3,5,-1,-9,4,3,6,5,9,-10,-10,2,-9,-3,4,-8,-10,7,7,4,4,1,5,9,1,-8,4,7,10,-6,-9,-3,7,-10,-6,6,-2,-9,4,-2,1,9,1,1,-7,8,-1,-3,-1,-5,-9,-8,-9,-7,-6,1,10,3,6,-3,-10,7,9,4,-4,8,1,4,2,-4,-2,-6,-4,4,-4,3,5,7,-1,-6,1,10,-10,3,-8,2,1,2,8,5,10,-6,-9,3,-8,-9,-4,1,5,-10,1,3,-2,1,-9,-4,6,6,-4,7,9,-1,7,9,-5,5,10,2,-10,-4,9,2,7,-3,8,-5,8,-9,7,6,-6,-2,8,-10,6,1,-1,5,10,1,7,-4,1,1,1,3,-8,-6,8,-7,2,-4,-9,-3,4,-7,-1,10,-2,1,8,-3,-7,-3,6,1,-7,1,3,-7,7,10,2,-7,10,-2,-1,3,5,-5,7,7,3,4,-1,3,-2,3,4,2,9,10,-10,-10,-10,-6,-4,-5,-2,-3,7,-8,-10,6,-2,-5,4,-4,10,-9,-10,-9,9,-1,2,-1,-9,-1,1,-2,8,5,5,-8,3,5,-6,8,-10,-4,3,3,-6,3,-4,10,4,-7,7,2,-5,-5,-1,6,-4,-4,-8,2,-3,-3,2,10,1,3,-3,9,-1,-8,-9], dtype = "uint16")#candidate|8370|(784,)|const|uint16
var_8371 = relay.var("var_8371", dtype = "int64", shape = (588,))#candidate|8371|(588,)|var|int64
call_8368 = relay.TupleGetItem(func_1113_call(relay.reshape(const_8369.astype('float32'), [4, 4, 7]), relay.reshape(const_8370.astype('uint16'), [784,]), relay.reshape(var_8371.astype('int64'), [588, 1]), ), 1)
call_8372 = relay.TupleGetItem(func_1118_call(relay.reshape(const_8369.astype('float32'), [4, 4, 7]), relay.reshape(const_8370.astype('uint16'), [784,]), relay.reshape(var_8371.astype('int64'), [588, 1]), ), 1)
func_6896_call = mod.get_global_var('func_6896')
func_6897_call = mutated_mod.get_global_var('func_6897')
call_8378 = relay.TupleGetItem(func_6896_call(), 0)
call_8379 = relay.TupleGetItem(func_6897_call(), 0)
uop_8398 = relay.log(call_8368.astype('float32')) # shape=(6, 7, 14)
uop_8400 = relay.log(call_8372.astype('float32')) # shape=(6, 7, 14)
output = relay.Tuple([call_8347,call_8356,const_8369,const_8370,var_8371,call_8378,uop_8398,])
output2 = relay.Tuple([call_8348,call_8357,const_8369,const_8370,var_8371,call_8379,uop_8400,])
func_8401 = relay.Function([var_8371,], output)
mod['func_8401'] = func_8401
mod = relay.transform.InferType()(mod)
mutated_mod['func_8401'] = func_8401
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8402 = relay.var("var_8402", dtype = "int64", shape = (588,))#candidate|8402|(588,)|var|int64
func_8401_call = mutated_mod.get_global_var('func_8401')
call_8403 = func_8401_call(var_8402)
output = call_8403
func_8404 = relay.Function([var_8402], output)
mutated_mod['func_8404'] = func_8404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4990_call = mod.get_global_var('func_4990')
func_4991_call = mutated_mod.get_global_var('func_4991')
call_8474 = func_4990_call()
call_8475 = func_4990_call()
output = call_8474
output2 = call_8475
func_8478 = relay.Function([], output)
mod['func_8478'] = func_8478
mod = relay.transform.InferType()(mod)
mutated_mod['func_8478'] = func_8478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8478_call = mutated_mod.get_global_var('func_8478')
call_8479 = func_8478_call()
output = call_8479
func_8480 = relay.Function([], output)
mutated_mod['func_8480'] = func_8480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6704_call = mod.get_global_var('func_6704')
func_6705_call = mutated_mod.get_global_var('func_6705')
call_8514 = relay.TupleGetItem(func_6704_call(), 0)
call_8515 = relay.TupleGetItem(func_6705_call(), 0)
var_8516 = relay.var("var_8516", dtype = "int8", shape = (6, 6, 8))#candidate|8516|(6, 6, 8)|var|int8
bop_8517 = relay.bitwise_or(call_8514.astype('uint64'), relay.reshape(var_8516.astype('uint64'), relay.shape_of(call_8514))) # shape=(6, 6, 8)
bop_8520 = relay.bitwise_or(call_8515.astype('uint64'), relay.reshape(var_8516.astype('uint64'), relay.shape_of(call_8515))) # shape=(6, 6, 8)
output = relay.Tuple([bop_8517,])
output2 = relay.Tuple([bop_8520,])
func_8523 = relay.Function([var_8516,], output)
mod['func_8523'] = func_8523
mod = relay.transform.InferType()(mod)
var_8524 = relay.var("var_8524", dtype = "int8", shape = (6, 6, 8))#candidate|8524|(6, 6, 8)|var|int8
output = func_8523(var_8524)
func_8525 = relay.Function([var_8524], output)
mutated_mod['func_8525'] = func_8525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4081_call = mod.get_global_var('func_4081')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_8580 = relay.TupleGetItem(func_4081_call(), 0)
call_8581 = relay.TupleGetItem(func_4082_call(), 0)
output = call_8580
output2 = call_8581
func_8589 = relay.Function([], output)
mod['func_8589'] = func_8589
mod = relay.transform.InferType()(mod)
output = func_8589()
func_8590 = relay.Function([], output)
mutated_mod['func_8590'] = func_8590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4193_call = mod.get_global_var('func_4193')
func_4194_call = mutated_mod.get_global_var('func_4194')
call_8647 = relay.TupleGetItem(func_4193_call(), 0)
call_8648 = relay.TupleGetItem(func_4194_call(), 0)
func_8478_call = mod.get_global_var('func_8478')
func_8480_call = mutated_mod.get_global_var('func_8480')
call_8651 = func_8478_call()
call_8652 = func_8478_call()
output = relay.Tuple([call_8647,call_8651,])
output2 = relay.Tuple([call_8648,call_8652,])
func_8654 = relay.Function([], output)
mod['func_8654'] = func_8654
mod = relay.transform.InferType()(mod)
output = func_8654()
func_8655 = relay.Function([], output)
mutated_mod['func_8655'] = func_8655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6449_call = mod.get_global_var('func_6449')
func_6450_call = mutated_mod.get_global_var('func_6450')
call_8658 = relay.TupleGetItem(func_6449_call(), 0)
call_8659 = relay.TupleGetItem(func_6450_call(), 0)
func_5770_call = mod.get_global_var('func_5770')
func_5772_call = mutated_mod.get_global_var('func_5772')
call_8673 = func_5770_call()
call_8674 = func_5770_call()
output = relay.Tuple([call_8658,call_8673,])
output2 = relay.Tuple([call_8659,call_8674,])
func_8695 = relay.Function([], output)
mod['func_8695'] = func_8695
mod = relay.transform.InferType()(mod)
mutated_mod['func_8695'] = func_8695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8695_call = mutated_mod.get_global_var('func_8695')
call_8696 = func_8695_call()
output = call_8696
func_8697 = relay.Function([], output)
mutated_mod['func_8697'] = func_8697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6872_call = mod.get_global_var('func_6872')
func_6873_call = mutated_mod.get_global_var('func_6873')
call_8747 = relay.TupleGetItem(func_6872_call(), 1)
call_8748 = relay.TupleGetItem(func_6873_call(), 1)
func_8250_call = mod.get_global_var('func_8250')
func_8253_call = mutated_mod.get_global_var('func_8253')
const_8760 = relay.const([7.660064,-6.690615,-9.104309,2.167004,-9.804705,9.982483,4.511779,8.688537,-3.261653,8.406006,-4.460424,-2.830563,-8.410837,8.386829,2.414913,8.278621,-3.915576,-9.784812,-5.766292,7.617085,-9.599512,-6.392610,7.639319,6.652975,-6.775952,-9.111290,2.062518,0.777559,-5.005485,-0.322925,1.549475,-4.474236,9.616986,-4.266112,1.653258,-4.040556,-3.217286,5.301674,1.347181,2.644522,5.939879,-9.759792,-1.457953,-3.440581,-2.498094,-0.783579,7.955727,-8.609604,8.854323,-4.415039,-9.552929,6.279597,-2.378095,-5.687822,7.383642,1.611390,6.543883,-3.101067,7.663003,-1.595597,6.866103,0.351965,-9.013336,4.003071,-8.926303,-0.220480,8.434677,7.514695,-8.657952,7.664237,-7.927965,7.407396,-3.753362,6.075505,-0.852294,-4.763410,3.574125,-9.919685,9.868751,9.699911,-6.195255,-1.836563,0.529115,4.365587,6.590335,-8.402890,7.454938,5.848954,8.223682,6.657884,-3.511223,7.512590,6.556415,9.942234,1.542934,-8.083429,-8.003698,0.241836,-0.597668,-6.456108,7.003837,7.102119,-9.927054,8.457638,-5.109027,9.725266,-0.874689,-4.379529,4.646586,-0.255039,-6.283522,-2.716305,0.352605,3.086590,-7.881526,9.988889,-4.497247,-3.617047,3.483266,-4.776664,-2.548920,-6.949427,-3.678280,-0.531619,3.558907,-3.328915,7.103819,-6.439911,7.514159,-3.557922,4.609111,2.568273,2.721789,-0.596959,8.590998,-9.886715,1.022224,-2.939907,9.570885,5.873972,9.356744,-3.181529,-1.247697,2.537080,-2.303823,9.357595,7.763964,8.691952,-9.255472,2.888651,-4.826019,5.519057,4.893368,0.302232,-5.579230,0.073105,8.357700,-0.004059,-3.189950,9.455414,9.594167,1.168423,8.196671,4.878000,-5.795372,-4.937558,-8.092814,-7.822531,1.844366,-2.488907,-3.601912,-5.994487,-1.696899,6.559679,-4.723203,5.291946,0.360311,2.302513,-8.378230,-2.044650,9.576160,9.064599,-8.378386,9.523262,-4.860533,5.310661,8.338701,-9.446201,-0.967261,7.304420,-6.116275,3.752919,1.466856,-8.710230,9.638047,-3.403693,1.076509,6.261318,-9.490523,-3.853285,-7.905758,8.207805,5.042085,5.070439,-6.868747,-5.494426,-6.598104,-6.670132,-3.194172,3.776463,-0.763123,6.089710,7.825818,3.804325,9.591878,-7.134320,-5.206706,-4.704999,5.508357,5.508630,-7.822444,-5.558085,9.915437,-0.801254,-9.703298,-2.320555,9.231227,-3.188469,-1.987210,-5.918003,6.118746,8.898908,8.882127,5.458704,-6.987265,-0.375752,3.427015,3.020104,0.790832,-9.752677,0.096152,-2.945659,-4.287093,9.067272,3.141389,6.979636,3.932348,-6.370212,-8.840377,1.620783,-8.545020,2.765173,4.472112,2.367323,-4.432656,-6.176678,-1.838375,-7.365140,0.784802,6.361662,-1.918455,-0.234097,4.930581,-6.472790,-2.798561,-9.991558,1.234137,-7.538906,-1.375993,0.232005,-6.517201,-4.260771,3.717001,3.970860,7.996935,4.797107,0.328401,6.806290,-9.704671,-3.769678,2.947121,3.176539,-2.095041,4.739722,7.266075,9.353920,-9.736320,-9.567575,5.718608,9.975462,-9.642892,-4.469826,-8.454297,4.184347,0.166413,1.850030,-9.966997,4.321304,2.905731,-6.585304,3.660299,-9.827476,3.162626,0.659623,-2.583872,9.242465,9.309300,2.432464,6.431814,-9.407045,-5.496210,-3.824156,2.993568,-9.783342,-6.150011,7.477472,-1.345276,-4.115230,0.061198,-7.338237,-5.898789,-0.787850,8.936986,1.855539,-5.560339,1.663595,8.277850,-7.027954,1.681076,9.226396,0.437057,-8.435473,-7.695679,4.382266,-8.306727,-6.510353], dtype = "float32")#candidate|8760|(336,)|const|float32
call_8759 = relay.TupleGetItem(func_8250_call(relay.reshape(const_8760.astype('float32'), [336,])), 0)
call_8761 = relay.TupleGetItem(func_8253_call(relay.reshape(const_8760.astype('float32'), [336,])), 0)
output = relay.Tuple([call_8747,call_8759,const_8760,])
output2 = relay.Tuple([call_8748,call_8761,const_8760,])
func_8770 = relay.Function([], output)
mod['func_8770'] = func_8770
mod = relay.transform.InferType()(mod)
mutated_mod['func_8770'] = func_8770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8770_call = mutated_mod.get_global_var('func_8770')
call_8771 = func_8770_call()
output = call_8771
func_8772 = relay.Function([], output)
mutated_mod['func_8772'] = func_8772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6560_call = mod.get_global_var('func_6560')
func_6562_call = mutated_mod.get_global_var('func_6562')
call_8787 = func_6560_call()
call_8788 = func_6560_call()
func_3955_call = mod.get_global_var('func_3955')
func_3957_call = mutated_mod.get_global_var('func_3957')
call_8812 = relay.TupleGetItem(func_3955_call(), 0)
call_8813 = relay.TupleGetItem(func_3957_call(), 0)
output = relay.Tuple([call_8787,call_8812,])
output2 = relay.Tuple([call_8788,call_8813,])
func_8826 = relay.Function([], output)
mod['func_8826'] = func_8826
mod = relay.transform.InferType()(mod)
output = func_8826()
func_8827 = relay.Function([], output)
mutated_mod['func_8827'] = func_8827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8335_call = mod.get_global_var('func_8335')
func_8337_call = mutated_mod.get_global_var('func_8337')
call_8850 = relay.TupleGetItem(func_8335_call(), 2)
call_8851 = relay.TupleGetItem(func_8337_call(), 2)
output = relay.Tuple([call_8850,])
output2 = relay.Tuple([call_8851,])
func_8873 = relay.Function([], output)
mod['func_8873'] = func_8873
mod = relay.transform.InferType()(mod)
mutated_mod['func_8873'] = func_8873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8873_call = mutated_mod.get_global_var('func_8873')
call_8874 = func_8873_call()
output = call_8874
func_8875 = relay.Function([], output)
mutated_mod['func_8875'] = func_8875
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8478_call = mod.get_global_var('func_8478')
func_8480_call = mutated_mod.get_global_var('func_8480')
call_8880 = func_8478_call()
call_8881 = func_8478_call()
func_8654_call = mod.get_global_var('func_8654')
func_8655_call = mutated_mod.get_global_var('func_8655')
call_8895 = relay.TupleGetItem(func_8654_call(), 0)
call_8896 = relay.TupleGetItem(func_8655_call(), 0)
output = relay.Tuple([call_8880,call_8895,])
output2 = relay.Tuple([call_8881,call_8896,])
func_8917 = relay.Function([], output)
mod['func_8917'] = func_8917
mod = relay.transform.InferType()(mod)
mutated_mod['func_8917'] = func_8917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8917_call = mutated_mod.get_global_var('func_8917')
call_8918 = func_8917_call()
output = call_8918
func_8919 = relay.Function([], output)
mutated_mod['func_8919'] = func_8919
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8949 = relay.var("var_8949", dtype = "float32", shape = (5, 14, 4))#candidate|8949|(5, 14, 4)|var|float32
uop_8950 = relay.tan(var_8949.astype('float32')) # shape=(5, 14, 4)
func_7087_call = mod.get_global_var('func_7087')
func_7088_call = mutated_mod.get_global_var('func_7088')
call_8965 = relay.TupleGetItem(func_7087_call(), 0)
call_8966 = relay.TupleGetItem(func_7088_call(), 0)
func_1113_call = mod.get_global_var('func_1113')
func_1118_call = mutated_mod.get_global_var('func_1118')
var_8984 = relay.var("var_8984", dtype = "uint16", shape = (784, 1))#candidate|8984|(784, 1)|var|uint16
const_8985 = relay.const([3,8,10,-10,-10,4,3,-7,-6,-5,9,4,8,5,3,9,-9,-1,1,-10,8,8,-3,-4,-5,-4,4,8,-5,-9,4,-4,7,4,9,-8,7,10,10,8,2,4,3,-7,-7,-5,-4,-6,4,-8,3,2,1,9,-6,1,-1,6,-6,-2,-9,6,6,6,-3,5,-4,7,10,9,4,-6,2,1,-6,1,-10,1,-8,-7,5,8,-10,-5,2,6,1,-1,7,10,-6,1,7,-3,-2,9,-2,-7,1,-3,-7,9,3,2,3,-3,5,7,5,1,10,-5,7,7,7,3,10,-1,-1,3,6,-4,-10,-5,1,-4,-3,7,2,-10,-5,10,-4,-6,-3,10,7,-10,-7,3,10,2,6,-5,-3,-7,7,-4,10,5,-1,7,-3,4,-2,9,-2,-5,-10,9,5,-2,7,3,-5,3,5,3,-6,9,4,2,-9,-6,-7,-4,3,5,1,-7,8,4,1,3,-6,7,-10,-8,6,-10,1,7,10,-3,-2,9,4,5,-3,-5,1,-9,-3,-10,10,-3,-3,-4,4,4,-10,8,-8,-9,3,8,-8,-5,-3,-9,6,-4,2,-2,5,-2,2,-9,5,9,-4,10,-5,2,-1,-3,-10,-5,-6,9,-6,-8,-1,7,7,-1,-5,4,7,10,-4,2,1,-8,-6,-10,-8,-9,5,6,-1,4,10,-8,1,-3,-2,-3,-4,-9,10,5,6,-8,1,7,-10,10,9,7,5,-9,8,-9,2,5,7,-9,-5,6,-2,-7,-3,4,-2,-2,-2,-3,2,7,10,-8,-3,10,6,1,8,-10,-3,-3,-7,4,-7,-2,-1,-4,10,-7,-9,-10,-2,2,-6,-3,9,8,2,-5,-10,-9,-7,-1,-3,1,-5,6,9,9,2,-6,9,-7,5,1,3,8,3,9,10,-9,-1,4,4,-7,7,-7,9,-9,-6,-4,10,-8,-3,-10,-7,8,5,7,-7,-8,-2,-3,9,-7,-2,-3,-3,7,10,-7,-10,4,-8,7,-7,-10,-7,2,-4,-10,-10,-1,6,8,-7,2,1,3,8,3,-2,-6,5,-7,-5,-7,4,9,-6,-7,-2,-10,-4,2,-10,7,1,5,9,7,2,10,-10,5,6,8,-2,2,-1,8,-3,-7,10,10,-5,7,1,-3,-6,8,2,-1,6,10,10,-9,5,-7,8,-6,6,-10,1,-9,-4,1,7,-8,-5,-10,-6,-8,-7,-8,2,-9,7,7,-5,-7,5,4,-7,-5,-1,-7,-6,-10,10,7,3,-4,7,10,-8,-10,-2,7,7,4,-8,6,6,6,-3,-1,1,7,-5,-2,4,7,8,-7,-7,4,-2,1,6,5,2,-6,-1,3,-9,-2,10,-9,5,-3,7,-10,-8,6,-8,-3,-8,3,1,-7,2,-5,1,9,10,-8,1,-5,-9,-3,3,-5,-5,2,4,-8,1,9,9,-7,1,-7,3,3,6,-7,4,-2,10,-6,-7,3,10,-9,-9,10,-2,-4,3,-7,7,-10,5,9,9,-2,-10,4,4,-8,10,2,-7,4,-8,-10,4,4], dtype = "int64")#candidate|8985|(588,)|const|int64
call_8983 = relay.TupleGetItem(func_1113_call(relay.reshape(call_8965.astype('float32'), [4, 4, 7]), relay.reshape(var_8984.astype('uint16'), [784,]), relay.reshape(const_8985.astype('int64'), [588, 1]), ), 1)
call_8986 = relay.TupleGetItem(func_1118_call(relay.reshape(call_8965.astype('float32'), [4, 4, 7]), relay.reshape(var_8984.astype('uint16'), [784,]), relay.reshape(const_8985.astype('int64'), [588, 1]), ), 1)
output = relay.Tuple([uop_8950,call_8965,call_8983,var_8984,const_8985,])
output2 = relay.Tuple([uop_8950,call_8966,call_8986,var_8984,const_8985,])
func_8989 = relay.Function([var_8949,var_8984,], output)
mod['func_8989'] = func_8989
mod = relay.transform.InferType()(mod)
mutated_mod['func_8989'] = func_8989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8989_call = mutated_mod.get_global_var('func_8989')
var_8991 = relay.var("var_8991", dtype = "float32", shape = (5, 14, 4))#candidate|8991|(5, 14, 4)|var|float32
var_8992 = relay.var("var_8992", dtype = "uint16", shape = (784, 1))#candidate|8992|(784, 1)|var|uint16
call_8990 = func_8989_call(var_8991,var_8992,)
output = call_8990
func_8993 = relay.Function([var_8991,var_8992,], output)
mutated_mod['func_8993'] = func_8993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6756_call = mod.get_global_var('func_6756')
func_6758_call = mutated_mod.get_global_var('func_6758')
call_9027 = relay.TupleGetItem(func_6756_call(), 0)
call_9028 = relay.TupleGetItem(func_6758_call(), 0)
output = call_9027
output2 = call_9028
func_9029 = relay.Function([], output)
mod['func_9029'] = func_9029
mod = relay.transform.InferType()(mod)
output = func_9029()
func_9030 = relay.Function([], output)
mutated_mod['func_9030'] = func_9030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5021_call = mod.get_global_var('func_5021')
func_5023_call = mutated_mod.get_global_var('func_5023')
call_9050 = func_5021_call()
call_9051 = func_5021_call()
output = relay.Tuple([call_9050,])
output2 = relay.Tuple([call_9051,])
func_9071 = relay.Function([], output)
mod['func_9071'] = func_9071
mod = relay.transform.InferType()(mod)
mutated_mod['func_9071'] = func_9071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9071_call = mutated_mod.get_global_var('func_9071')
call_9072 = func_9071_call()
output = call_9072
func_9073 = relay.Function([], output)
mutated_mod['func_9073'] = func_9073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8654_call = mod.get_global_var('func_8654')
func_8655_call = mutated_mod.get_global_var('func_8655')
call_9151 = relay.TupleGetItem(func_8654_call(), 0)
call_9152 = relay.TupleGetItem(func_8655_call(), 0)
output = call_9151
output2 = call_9152
func_9173 = relay.Function([], output)
mod['func_9173'] = func_9173
mod = relay.transform.InferType()(mod)
mutated_mod['func_9173'] = func_9173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9173_call = mutated_mod.get_global_var('func_9173')
call_9174 = func_9173_call()
output = call_9174
func_9175 = relay.Function([], output)
mutated_mod['func_9175'] = func_9175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8826_call = mod.get_global_var('func_8826')
func_8827_call = mutated_mod.get_global_var('func_8827')
call_9193 = relay.TupleGetItem(func_8826_call(), 0)
call_9194 = relay.TupleGetItem(func_8827_call(), 0)
func_8873_call = mod.get_global_var('func_8873')
func_8875_call = mutated_mod.get_global_var('func_8875')
call_9211 = relay.TupleGetItem(func_8873_call(), 0)
call_9212 = relay.TupleGetItem(func_8875_call(), 0)
output = relay.Tuple([call_9193,call_9211,])
output2 = relay.Tuple([call_9194,call_9212,])
func_9216 = relay.Function([], output)
mod['func_9216'] = func_9216
mod = relay.transform.InferType()(mod)
output = func_9216()
func_9217 = relay.Function([], output)
mutated_mod['func_9217'] = func_9217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3955_call = mod.get_global_var('func_3955')
func_3957_call = mutated_mod.get_global_var('func_3957')
call_9246 = relay.TupleGetItem(func_3955_call(), 0)
call_9247 = relay.TupleGetItem(func_3957_call(), 0)
output = call_9246
output2 = call_9247
func_9289 = relay.Function([], output)
mod['func_9289'] = func_9289
mod = relay.transform.InferType()(mod)
mutated_mod['func_9289'] = func_9289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9289_call = mutated_mod.get_global_var('func_9289')
call_9290 = func_9289_call()
output = call_9290
func_9291 = relay.Function([], output)
mutated_mod['func_9291'] = func_9291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6896_call = mod.get_global_var('func_6896')
func_6897_call = mutated_mod.get_global_var('func_6897')
call_9329 = relay.TupleGetItem(func_6896_call(), 0)
call_9330 = relay.TupleGetItem(func_6897_call(), 0)
func_4193_call = mod.get_global_var('func_4193')
func_4194_call = mutated_mod.get_global_var('func_4194')
call_9353 = relay.TupleGetItem(func_4193_call(), 0)
call_9354 = relay.TupleGetItem(func_4194_call(), 0)
output = relay.Tuple([call_9329,call_9353,])
output2 = relay.Tuple([call_9330,call_9354,])
func_9360 = relay.Function([], output)
mod['func_9360'] = func_9360
mod = relay.transform.InferType()(mod)
mutated_mod['func_9360'] = func_9360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9360_call = mutated_mod.get_global_var('func_9360')
call_9361 = func_9360_call()
output = call_9361
func_9362 = relay.Function([], output)
mutated_mod['func_9362'] = func_9362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4193_call = mod.get_global_var('func_4193')
func_4194_call = mutated_mod.get_global_var('func_4194')
call_9380 = relay.TupleGetItem(func_4193_call(), 0)
call_9381 = relay.TupleGetItem(func_4194_call(), 0)
uop_9382 = relay.tan(call_9380.astype('float64')) # shape=(1, 7, 16)
uop_9384 = relay.tan(call_9381.astype('float64')) # shape=(1, 7, 16)
func_5171_call = mod.get_global_var('func_5171')
func_5172_call = mutated_mod.get_global_var('func_5172')
call_9388 = relay.TupleGetItem(func_5171_call(), 4)
call_9389 = relay.TupleGetItem(func_5172_call(), 4)
var_9398 = relay.var("var_9398", dtype = "float64", shape = (8, 7, 16))#candidate|9398|(8, 7, 16)|var|float64
bop_9399 = relay.mod(uop_9382.astype('float64'), var_9398.astype('float64')) # shape=(8, 7, 16)
bop_9402 = relay.mod(uop_9384.astype('float64'), var_9398.astype('float64')) # shape=(8, 7, 16)
output = relay.Tuple([call_9388,bop_9399,])
output2 = relay.Tuple([call_9389,bop_9402,])
func_9404 = relay.Function([var_9398,], output)
mod['func_9404'] = func_9404
mod = relay.transform.InferType()(mod)
var_9405 = relay.var("var_9405", dtype = "float64", shape = (8, 7, 16))#candidate|9405|(8, 7, 16)|var|float64
output = func_9404(var_9405)
func_9406 = relay.Function([var_9405], output)
mutated_mod['func_9406'] = func_9406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6541_call = mod.get_global_var('func_6541')
func_6542_call = mutated_mod.get_global_var('func_6542')
call_9408 = relay.TupleGetItem(func_6541_call(), 0)
call_9409 = relay.TupleGetItem(func_6542_call(), 0)
output = relay.Tuple([call_9408,])
output2 = relay.Tuple([call_9409,])
func_9412 = relay.Function([], output)
mod['func_9412'] = func_9412
mod = relay.transform.InferType()(mod)
output = func_9412()
func_9413 = relay.Function([], output)
mutated_mod['func_9413'] = func_9413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4144_call = mod.get_global_var('func_4144')
func_4145_call = mutated_mod.get_global_var('func_4145')
call_9457 = func_4144_call()
call_9458 = func_4144_call()
func_5860_call = mod.get_global_var('func_5860')
func_5862_call = mutated_mod.get_global_var('func_5862')
call_9459 = relay.TupleGetItem(func_5860_call(), 0)
call_9460 = relay.TupleGetItem(func_5862_call(), 0)
output = relay.Tuple([call_9457,call_9459,])
output2 = relay.Tuple([call_9458,call_9460,])
func_9467 = relay.Function([], output)
mod['func_9467'] = func_9467
mod = relay.transform.InferType()(mod)
output = func_9467()
func_9468 = relay.Function([], output)
mutated_mod['func_9468'] = func_9468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6704_call = mod.get_global_var('func_6704')
func_6705_call = mutated_mod.get_global_var('func_6705')
call_9503 = relay.TupleGetItem(func_6704_call(), 0)
call_9504 = relay.TupleGetItem(func_6705_call(), 0)
func_7918_call = mod.get_global_var('func_7918')
func_7920_call = mutated_mod.get_global_var('func_7920')
call_9515 = relay.TupleGetItem(func_7918_call(), 1)
call_9516 = relay.TupleGetItem(func_7920_call(), 1)
func_6914_call = mod.get_global_var('func_6914')
func_6915_call = mutated_mod.get_global_var('func_6915')
call_9522 = func_6914_call()
call_9523 = func_6914_call()
output = relay.Tuple([call_9503,call_9515,call_9522,])
output2 = relay.Tuple([call_9504,call_9516,call_9523,])
func_9542 = relay.Function([], output)
mod['func_9542'] = func_9542
mod = relay.transform.InferType()(mod)
mutated_mod['func_9542'] = func_9542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9542_call = mutated_mod.get_global_var('func_9542')
call_9543 = func_9542_call()
output = call_9543
func_9544 = relay.Function([], output)
mutated_mod['func_9544'] = func_9544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4081_call = mod.get_global_var('func_4081')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_9573 = relay.TupleGetItem(func_4081_call(), 0)
call_9574 = relay.TupleGetItem(func_4082_call(), 0)
func_6560_call = mod.get_global_var('func_6560')
func_6562_call = mutated_mod.get_global_var('func_6562')
call_9591 = func_6560_call()
call_9592 = func_6560_call()
func_8250_call = mod.get_global_var('func_8250')
func_8253_call = mutated_mod.get_global_var('func_8253')
var_9595 = relay.var("var_9595", dtype = "float32", shape = (8, 42))#candidate|9595|(8, 42)|var|float32
call_9594 = relay.TupleGetItem(func_8250_call(relay.reshape(var_9595.astype('float32'), [336,])), 1)
call_9596 = relay.TupleGetItem(func_8253_call(relay.reshape(var_9595.astype('float32'), [336,])), 1)
func_4144_call = mod.get_global_var('func_4144')
func_4145_call = mutated_mod.get_global_var('func_4145')
call_9599 = func_4144_call()
call_9600 = func_4144_call()
func_9542_call = mod.get_global_var('func_9542')
func_9544_call = mutated_mod.get_global_var('func_9544')
call_9607 = relay.TupleGetItem(func_9542_call(), 0)
call_9608 = relay.TupleGetItem(func_9544_call(), 0)
output = relay.Tuple([call_9573,call_9591,call_9594,var_9595,call_9599,call_9607,])
output2 = relay.Tuple([call_9574,call_9592,call_9596,var_9595,call_9600,call_9608,])
func_9609 = relay.Function([var_9595,], output)
mod['func_9609'] = func_9609
mod = relay.transform.InferType()(mod)
var_9610 = relay.var("var_9610", dtype = "float32", shape = (8, 42))#candidate|9610|(8, 42)|var|float32
output = func_9609(var_9610)
func_9611 = relay.Function([var_9610], output)
mutated_mod['func_9611'] = func_9611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9360_call = mod.get_global_var('func_9360')
func_9362_call = mutated_mod.get_global_var('func_9362')
call_9665 = relay.TupleGetItem(func_9360_call(), 1)
call_9666 = relay.TupleGetItem(func_9362_call(), 1)
output = call_9665
output2 = call_9666
func_9686 = relay.Function([], output)
mod['func_9686'] = func_9686
mod = relay.transform.InferType()(mod)
output = func_9686()
func_9687 = relay.Function([], output)
mutated_mod['func_9687'] = func_9687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5229_call = mod.get_global_var('func_5229')
func_5231_call = mutated_mod.get_global_var('func_5231')
call_9707 = relay.TupleGetItem(func_5229_call(), 0)
call_9708 = relay.TupleGetItem(func_5231_call(), 0)
output = relay.Tuple([call_9707,])
output2 = relay.Tuple([call_9708,])
func_9713 = relay.Function([], output)
mod['func_9713'] = func_9713
mod = relay.transform.InferType()(mod)
output = func_9713()
func_9714 = relay.Function([], output)
mutated_mod['func_9714'] = func_9714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6943_call = mod.get_global_var('func_6943')
func_6945_call = mutated_mod.get_global_var('func_6945')
call_9767 = func_6943_call()
call_9768 = func_6943_call()
output = call_9767
output2 = call_9768
func_9790 = relay.Function([], output)
mod['func_9790'] = func_9790
mod = relay.transform.InferType()(mod)
mutated_mod['func_9790'] = func_9790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9790_call = mutated_mod.get_global_var('func_9790')
call_9791 = func_9790_call()
output = call_9791
func_9792 = relay.Function([], output)
mutated_mod['func_9792'] = func_9792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7295_call = mod.get_global_var('func_7295')
func_7297_call = mutated_mod.get_global_var('func_7297')
call_10014 = relay.TupleGetItem(func_7295_call(), 0)
call_10015 = relay.TupleGetItem(func_7297_call(), 0)
func_9289_call = mod.get_global_var('func_9289')
func_9291_call = mutated_mod.get_global_var('func_9291')
call_10018 = func_9289_call()
call_10019 = func_9289_call()
var_10023 = relay.var("var_10023", dtype = "float32", shape = (1, 7, 16))#candidate|10023|(1, 7, 16)|var|float32
bop_10024 = relay.subtract(call_10018.astype('float64'), relay.reshape(var_10023.astype('float64'), relay.shape_of(call_10018))) # shape=(1, 7, 16)
bop_10027 = relay.subtract(call_10019.astype('float64'), relay.reshape(var_10023.astype('float64'), relay.shape_of(call_10019))) # shape=(1, 7, 16)
func_8401_call = mod.get_global_var('func_8401')
func_8404_call = mutated_mod.get_global_var('func_8404')
var_10029 = relay.var("var_10029", dtype = "int64", shape = (588,))#candidate|10029|(588,)|var|int64
call_10028 = relay.TupleGetItem(func_8401_call(relay.reshape(var_10029.astype('int64'), [588,])), 1)
call_10030 = relay.TupleGetItem(func_8404_call(relay.reshape(var_10029.astype('int64'), [588,])), 1)
func_8478_call = mod.get_global_var('func_8478')
func_8480_call = mutated_mod.get_global_var('func_8480')
call_10038 = func_8478_call()
call_10039 = func_8478_call()
output = relay.Tuple([call_10014,bop_10024,call_10028,var_10029,call_10038,])
output2 = relay.Tuple([call_10015,bop_10027,call_10030,var_10029,call_10039,])
func_10045 = relay.Function([var_10023,var_10029,], output)
mod['func_10045'] = func_10045
mod = relay.transform.InferType()(mod)
var_10046 = relay.var("var_10046", dtype = "float32", shape = (1, 7, 16))#candidate|10046|(1, 7, 16)|var|float32
var_10047 = relay.var("var_10047", dtype = "int64", shape = (588,))#candidate|10047|(588,)|var|int64
output = func_10045(var_10046,var_10047,)
func_10048 = relay.Function([var_10046,var_10047,], output)
mutated_mod['func_10048'] = func_10048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7087_call = mod.get_global_var('func_7087')
func_7088_call = mutated_mod.get_global_var('func_7088')
call_10066 = relay.TupleGetItem(func_7087_call(), 0)
call_10067 = relay.TupleGetItem(func_7088_call(), 0)
func_6914_call = mod.get_global_var('func_6914')
func_6915_call = mutated_mod.get_global_var('func_6915')
call_10069 = func_6914_call()
call_10070 = func_6914_call()
func_6225_call = mod.get_global_var('func_6225')
func_6229_call = mutated_mod.get_global_var('func_6229')
const_10079 = relay.const([1,6,4,8,-5,4,8,9,-9,9,-6,-7,10,-7,-3,10,-10,-3,-6,-6,7,10,10,-7,8,4,-3,-2,9,1,4,9,10,10,-2,9,-8,7,10,5,-9,3,2,-5,9,-4,-9,-8,-4,7,7,-7,4,-3,5,-4,8,6,-5,10,7,6,6,9,6,-6,-1,-8,-7,9,8,8,-3,6,5,1,-10,2,-2,-6,6,-1,-6,-1,-1,-7,-6,-5,-1,-4,-6,10,3,-4,2,5,-3,-4,9,-4,-8,9,9,-2,6,-7,-2,-10,9,-1,-3,1,-5,9,-2,4,5,5,-7,4,-10,8,8,-6,2,-9,6,-3,9,-4,-6,-3,10,-6,-3,-4,9,-7,-10,5,-2,8,-6,-8,-2,8,-1,-10,-8,-1,5,6,-7,-5,9,8,-4,-1,7,7,-4,-9,5,7,6,-6,3,-8,-6,7,1,-9,4,-9,-1,-4,3,-9,5,-4,6,-3,-2,9,-4,-7,4,1,-6,-2,-9,4,-10,-2,1,-5,6,5,-10,9,-1,-8,2,4,2,-7,-2,4,-3,6,-4,2,2,-1,-10,-6,-7,-5,-6,9,4,-10,6,-8,-2,-5,-7,8,4,10,10,-2,-2,5,7,5,-7,-8,3,-4,-2,3,7,7,-9,-3,4,-5,6,4,4,-5,-6,-6,2,-6,-8,-2,-10,-6,7,-9,7,-7,4,4,-1,-10,5,10,5,-2,4,-10,2,-5,-5,1,-8,3,-2,-1,10,-3,-5,-2,8,-5,-7,-7,1,1,-6,-6,-3,-8,9,-7,1,4,3,-8,2,-3,8,-2,-4,5,-5,6,-1,2,-6,-9,-1,4,-2,4,8,7,-7,-7,9,-1,-2,-4,-1,-2,-7,5,7,1,6,7,1,1,10,7,7,-8,4,1,8,6,8,3,-3,-7,8,-2,-8,8,-9,1,-4,-5,9,-6,3,2,3,9,10,2,1,-8,7,9,1,-3,9,3,-6,-6,-1,10,-4,10,4,1,-8,-2,-4,-2], dtype = "int32")#candidate|10079|(384,)|const|int32
var_10080 = relay.var("var_10080", dtype = "int64", shape = (588,))#candidate|10080|(588,)|var|int64
call_10078 = relay.TupleGetItem(func_6225_call(relay.reshape(const_10079.astype('int32'), [8, 8, 6]), relay.reshape(const_10079.astype('bool'), [8, 8, 6]), relay.reshape(var_10080.astype('int64'), [588,]), ), 5)
call_10081 = relay.TupleGetItem(func_6229_call(relay.reshape(const_10079.astype('int32'), [8, 8, 6]), relay.reshape(const_10079.astype('bool'), [8, 8, 6]), relay.reshape(var_10080.astype('int64'), [588,]), ), 5)
output = relay.Tuple([call_10066,call_10069,call_10078,const_10079,var_10080,])
output2 = relay.Tuple([call_10067,call_10070,call_10081,const_10079,var_10080,])
func_10083 = relay.Function([var_10080,], output)
mod['func_10083'] = func_10083
mod = relay.transform.InferType()(mod)
var_10084 = relay.var("var_10084", dtype = "int64", shape = (588,))#candidate|10084|(588,)|var|int64
output = func_10083(var_10084)
func_10085 = relay.Function([var_10084], output)
mutated_mod['func_10085'] = func_10085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7590_call = mod.get_global_var('func_7590')
func_7592_call = mutated_mod.get_global_var('func_7592')
call_10093 = func_7590_call()
call_10094 = func_7590_call()
func_1891_call = mod.get_global_var('func_1891')
func_1895_call = mutated_mod.get_global_var('func_1895')
const_10098 = relay.const([10,3,-6,7,-9,6,9,-4,9,7,6,-9,2,9,7,-7,-1,-5,9,7,-3,10,8,-6,6,2,-9,-8,-1,7,5,4,-6,-3,1,5,-2,-7,-10,7,6,8,4,-8,-5,2,-9,-7,3,2,-1,9,3,-4,-9,-7,-4,-10,-2,-1,3,6,10,-7,-3,-9,9,8,4,-4,-4,-7,7,7,8,-4,-3,-3,4,-6,-10,-1,-2,10,10,-6,7,3,3,-3,9,-1,10,5,-3,-10,5,3,-8,-3,9,3,5,1,-5,8,-2,8,3,3,-4,1,4,-9,9,3,1,5,1,3,-8,1,2,-1,3,-2,-9,-8,-7,9,7,5,7,4,-5,3,-10,7,-6,-6,4,-5,3,8,-10,-7,9,7,-3,2,-7,-5,-3,-8,9,-7,-4,-6,8,6,-2,-9,6,-5,-6,-8,5,-2,6,-7,-6,7,-9,-6,10,-8,-6,1,4,4,4,5,-7,-8,-8,7,-1,1,-1,10,-10,4,-7,1,-3,-1,7,6,4,-7,1,6,10,4,6,-1,-2,4,9,1,10,-1,-10,3,3,8,-5,7,-2,7,5,-4,-4,-8,-6,7,9,-5,4,-4,-9,10,5,-9,8,-4,-3,-2,9,-10,-9,10,-4,8,4,-3,-2,-9,2,-5,4,-7,-2,-6,9,5,-4,5,-2,3,4,-1,3,-7,-9,-7,-4,2,3,6,-5,-1,9,-6,-10,-9,7,3,1,6,4,5,-8,-3,-6,-5,3,-9,-4,5,3,10,-7,1,5,-10,-1,-9,1,-1,3,7,4,10,10,-3,3,-5,8,-8,1,4,-2,-2,4,-9,9,-5,-1,-10,4,6,-9,-6,4,2,4,1,10,9,5,3,2,-7,-4,-6], dtype = "uint64")#candidate|10098|(336,)|const|uint64
var_10099 = relay.var("var_10099", dtype = "bool", shape = (72,))#candidate|10099|(72,)|var|bool
call_10097 = relay.TupleGetItem(func_1891_call(relay.reshape(const_10098.astype('uint64'), [336,]), relay.reshape(var_10099.astype('bool'), [4, 6, 3]), ), 0)
call_10100 = relay.TupleGetItem(func_1895_call(relay.reshape(const_10098.astype('uint64'), [336,]), relay.reshape(var_10099.astype('bool'), [4, 6, 3]), ), 0)
output = relay.Tuple([call_10093,call_10097,const_10098,var_10099,])
output2 = relay.Tuple([call_10094,call_10100,const_10098,var_10099,])
func_10123 = relay.Function([var_10099,], output)
mod['func_10123'] = func_10123
mod = relay.transform.InferType()(mod)
var_10124 = relay.var("var_10124", dtype = "bool", shape = (72,))#candidate|10124|(72,)|var|bool
output = func_10123(var_10124)
func_10125 = relay.Function([var_10124], output)
mutated_mod['func_10125'] = func_10125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6765_call = mod.get_global_var('func_6765')
func_6766_call = mutated_mod.get_global_var('func_6766')
call_10148 = relay.TupleGetItem(func_6765_call(), 0)
call_10149 = relay.TupleGetItem(func_6766_call(), 0)
func_7918_call = mod.get_global_var('func_7918')
func_7920_call = mutated_mod.get_global_var('func_7920')
call_10153 = relay.TupleGetItem(func_7918_call(), 1)
call_10154 = relay.TupleGetItem(func_7920_call(), 1)
func_9467_call = mod.get_global_var('func_9467')
func_9468_call = mutated_mod.get_global_var('func_9468')
call_10157 = relay.TupleGetItem(func_9467_call(), 1)
call_10158 = relay.TupleGetItem(func_9468_call(), 1)
bop_10163 = relay.equal(call_10157.astype('bool'), relay.reshape(call_10153.astype('bool'), relay.shape_of(call_10157))) # shape=(1, 7, 16)
bop_10166 = relay.equal(call_10158.astype('bool'), relay.reshape(call_10154.astype('bool'), relay.shape_of(call_10158))) # shape=(1, 7, 16)
func_9790_call = mod.get_global_var('func_9790')
func_9792_call = mutated_mod.get_global_var('func_9792')
call_10168 = func_9790_call()
call_10169 = func_9790_call()
output = relay.Tuple([call_10148,bop_10163,call_10168,])
output2 = relay.Tuple([call_10149,bop_10166,call_10169,])
func_10182 = relay.Function([], output)
mod['func_10182'] = func_10182
mod = relay.transform.InferType()(mod)
mutated_mod['func_10182'] = func_10182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10182_call = mutated_mod.get_global_var('func_10182')
call_10183 = func_10182_call()
output = call_10183
func_10184 = relay.Function([], output)
mutated_mod['func_10184'] = func_10184
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10264 = relay.var("var_10264", dtype = "int64", shape = (10, 8, 6))#candidate|10264|(10, 8, 6)|var|int64
var_10265 = relay.var("var_10265", dtype = "int64", shape = (10, 8, 6))#candidate|10265|(10, 8, 6)|var|int64
bop_10266 = relay.greater_equal(var_10264.astype('bool'), relay.reshape(var_10265.astype('bool'), relay.shape_of(var_10264))) # shape=(10, 8, 6)
func_8589_call = mod.get_global_var('func_8589')
func_8590_call = mutated_mod.get_global_var('func_8590')
call_10272 = func_8589_call()
call_10273 = func_8589_call()
output = relay.Tuple([bop_10266,call_10272,])
output2 = relay.Tuple([bop_10266,call_10273,])
func_10280 = relay.Function([var_10264,var_10265,], output)
mod['func_10280'] = func_10280
mod = relay.transform.InferType()(mod)
mutated_mod['func_10280'] = func_10280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10280_call = mutated_mod.get_global_var('func_10280')
var_10282 = relay.var("var_10282", dtype = "int64", shape = (10, 8, 6))#candidate|10282|(10, 8, 6)|var|int64
var_10283 = relay.var("var_10283", dtype = "int64", shape = (10, 8, 6))#candidate|10283|(10, 8, 6)|var|int64
call_10281 = func_10280_call(var_10282,var_10283,)
output = call_10281
func_10284 = relay.Function([var_10282,var_10283,], output)
mutated_mod['func_10284'] = func_10284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9686_call = mod.get_global_var('func_9686')
func_9687_call = mutated_mod.get_global_var('func_9687')
call_10417 = func_9686_call()
call_10418 = func_9686_call()
output = relay.Tuple([call_10417,])
output2 = relay.Tuple([call_10418,])
func_10441 = relay.Function([], output)
mod['func_10441'] = func_10441
mod = relay.transform.InferType()(mod)
output = func_10441()
func_10442 = relay.Function([], output)
mutated_mod['func_10442'] = func_10442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4811_call = mod.get_global_var('func_4811')
func_4812_call = mutated_mod.get_global_var('func_4812')
call_10515 = func_4811_call()
call_10516 = func_4811_call()
func_4325_call = mod.get_global_var('func_4325')
func_4328_call = mutated_mod.get_global_var('func_4328')
const_10518 = relay.const([4.120843,-3.735668,-3.693552,-0.232423,6.409387,-4.266034,-6.598643,-9.798124,9.299167,-2.182189,4.161113,-8.210667,2.839757,-8.413663,2.913022,-4.042484,-3.492391,1.327598,-4.208688,-2.878564,1.138148,4.391212,-9.911143,-8.598570,-7.082446,6.526707,-1.382876,-3.012084,1.578746,0.816554,-2.704386,7.344856,-3.968665,5.218089,-3.440049,-4.837673,-9.886707,8.400158,3.421344,-9.730219,-9.423100,-4.381150,9.526163,8.819369,2.004036,-9.593431,-0.784963,2.881813,-5.615988,7.519071,-3.689804,-3.545062,2.264727,-9.647875,-5.567536,-7.858194,-9.601479,2.438505,1.260451,-9.438365,3.640919,-0.017980,-9.230493,-3.503975,-6.941688,-2.875982,4.196871,-8.595721,-5.536523,-7.258773,9.802728,-4.584293,6.214915,-7.112992,-9.677069,9.476934,5.507851,1.688833,1.475819,-8.237449,4.167321,6.753997,-9.303124,0.498248,-2.689412,0.531476,5.135456,3.388186,7.078593,3.029022,-0.069290,-5.355388,5.011970,6.588798,9.790994,-4.320443,-7.371456,-5.090521,2.992369,-5.510711,6.304363,-4.269913,5.722444,8.172947,7.641669,-4.154543,7.718607,4.023520,-8.592126,-4.308689,-8.197173,-7.531828,-1.688361,3.099796,-7.881244,6.461606,5.897313,-9.609474,1.670112,-2.458766,7.709625,-1.761607,4.628488,9.227543,-8.118689,9.314961,-3.697376,-3.497883,-1.503682,9.962804,4.136774,-0.058210,-4.537335,7.966828,-2.946991,-5.056696,-2.892940,2.717552,-9.774950,9.346091,-8.362168,6.402858,-8.031509,7.069351,-8.018653,7.507063,8.475057,-3.270460,3.185068,0.496359,9.997011,0.162302,-1.961062,6.187246,4.281466,1.436359,-6.199345,-4.343660,-0.272460,3.285074,-8.882102,-2.059524,3.749985,7.109561,-8.329405,-3.227597,-4.564045,3.409528,-1.858553,6.622107,9.103013,4.687990,-4.252638,-7.427883,1.655499,1.143623,3.531237,5.733639,-8.662460,9.853671,3.255183,1.978964,4.246237,-2.261500,7.933575,3.651781,6.474199,-9.633067,-1.959525,-7.319149,1.576873,-5.771335,-5.655798,6.623615,-8.816067,3.563794,-1.807213,-7.327533,-8.239775,-2.582558,-1.911336,-6.073690,-3.173651,2.939326,-6.503822,8.135078,4.783682,-5.749207,7.993571,0.673612,-6.846576,-1.115574,7.568485,-0.455567,9.840762,8.909716,-1.614120,9.668095,0.226387,3.549994,7.851841,8.682006,-8.131853,-4.483460,7.580412,-7.902036,-2.378497,-0.766136,3.865336,5.234105,4.976293,-2.450718,5.754531,3.001012,6.342371,-4.607283,1.100646,3.126268,6.068198,9.746322,7.607677,-6.074307,-8.393175,9.155218,4.514213,3.596712,-2.277919,-9.469335,5.740439,-3.071687,-5.491928,7.788994,-4.800925,-1.116175,-2.669644,-8.331490,3.538552,-3.590546,5.686346,4.567905,-2.674368,-1.339327,-4.959404,-2.243972,-9.245892,-6.264025,8.824465,-6.709640,5.517463,8.173841,-8.758739,4.288138,-8.291181,-5.831858,-6.046755,-6.183223,-0.891322,9.273691,6.901969,-5.729788,-7.741146,9.425059,5.726925,2.421135,-2.318527,-1.999703,-7.414505,-0.349885,9.893048,-9.211625,-9.071917,5.347834,3.732483,6.159534,-1.412836,-7.307895,8.502483,9.055346,3.189836,5.498217,5.002922,7.593140,6.505299,5.739839,-9.869504,-3.322747,-4.436341,9.674769,-2.268850,0.770316,-4.501677,1.130707,7.453205,-4.162999,2.404561,-2.386696,-9.048613,-8.684430,8.639211,-9.644876,-7.636315,-3.789296,-8.824798,-5.728649,-7.073062,-8.908800,-9.024361,-6.465969,-0.089300,-5.818784,-0.957420,-0.088338,-1.604970,8.350322,-1.839066,5.245931], dtype = "float32")#candidate|10518|(336,)|const|float32
var_10519 = relay.var("var_10519", dtype = "int64", shape = (1, 588))#candidate|10519|(1, 588)|var|int64
call_10517 = relay.TupleGetItem(func_4325_call(relay.reshape(const_10518.astype('float32'), [3, 7, 16]), relay.reshape(var_10519.astype('int64'), [588,]), ), 6)
call_10520 = relay.TupleGetItem(func_4328_call(relay.reshape(const_10518.astype('float32'), [3, 7, 16]), relay.reshape(var_10519.astype('int64'), [588,]), ), 6)
bop_10521 = relay.floor_divide(call_10517.astype('float32'), relay.reshape(var_10519.astype('float32'), relay.shape_of(call_10517))) # shape=(588,)
bop_10524 = relay.floor_divide(call_10520.astype('float32'), relay.reshape(var_10519.astype('float32'), relay.shape_of(call_10520))) # shape=(588,)
output = relay.Tuple([call_10515,const_10518,bop_10521,])
output2 = relay.Tuple([call_10516,const_10518,bop_10524,])
func_10528 = relay.Function([var_10519,], output)
mod['func_10528'] = func_10528
mod = relay.transform.InferType()(mod)
var_10529 = relay.var("var_10529", dtype = "int64", shape = (1, 588))#candidate|10529|(1, 588)|var|int64
output = func_10528(var_10529)
func_10530 = relay.Function([var_10529], output)
mutated_mod['func_10530'] = func_10530
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10555 = relay.const([[[4.887672,7.450773,5.967907,4.718522,-3.362286,1.215599,-5.566574,-6.018379,6.019928,-7.499885,8.377243,0.729106],[-8.978483,3.389845,6.312479,-3.364141,-9.238027,-1.055459,0.580664,-9.574936,-1.613420,-4.368723,5.186085,9.263931],[3.224943,1.309502,-8.766439,9.640049,-4.275823,5.049427,0.190914,-8.182972,8.928109,-3.436737,-1.837667,-1.560599],[-3.273948,-4.146745,7.254927,-1.898175,9.058546,-2.808998,-2.611548,-1.014240,-6.342333,-8.828150,-9.654977,4.985076],[-9.485578,-3.871785,-1.538862,8.311653,5.005905,-6.508578,4.291793,-9.631326,9.448112,-2.591330,-9.365452,-1.662758],[-9.469047,5.284582,9.943363,-4.824186,-8.356373,-1.636075,-6.161321,7.109225,2.053395,-9.546683,0.363794,-7.771485],[0.957433,-6.990385,2.508269,8.213887,-4.927646,-7.650432,9.385802,0.563405,3.945842,8.102922,9.780018,-2.947255]],[[-7.451549,3.796936,4.330930,-1.238640,-9.149003,-1.818566,1.771152,1.524089,-9.981198,2.111118,-1.619603,8.783016],[8.028419,9.315821,-5.430464,5.608226,3.786604,-1.453331,-0.708271,4.342037,4.391938,8.466200,8.949639,-2.179893],[-9.057168,-9.293605,-3.805817,5.529217,-8.932115,-9.754917,-7.290850,7.220233,-0.560562,-2.280992,0.834236,6.761676],[0.530686,0.576044,2.236596,3.048189,-7.830640,5.289434,6.241560,-7.744808,6.589749,-9.214007,-6.586878,5.737535],[2.761757,-0.721663,-4.479133,-2.224148,-7.140392,-4.495398,3.995394,0.886703,8.453995,1.109543,5.113735,-9.786643],[-4.968703,-1.387521,7.170918,-0.425982,6.155906,0.212346,-7.512080,-3.247498,1.188150,8.460923,-1.642901,-9.144611],[2.338023,-3.558439,9.119435,8.711357,-3.896405,1.169295,-8.152914,-7.262538,-6.745670,3.688994,7.550991,4.920226]],[[-4.109827,-8.112191,1.745554,9.128379,-1.043069,-1.289609,-7.192009,6.622931,8.996106,-8.491863,-4.113296,-6.898543],[-4.341182,-2.538376,2.490235,5.675328,-9.348934,-2.326148,-7.523209,-8.308083,6.939183,8.925858,-5.849642,-7.134408],[3.200795,4.250246,-7.412208,-5.934055,5.364980,-7.747152,-0.673818,9.197887,2.672144,-4.786710,5.281026,-4.484925],[0.091106,-8.970336,1.838402,-5.593396,-2.963319,-2.136928,5.071097,1.685184,2.627792,6.518043,6.468589,-8.892858],[-6.610876,5.962366,5.298833,-6.631653,7.222000,7.217611,-6.810991,1.092381,1.481349,7.550325,-9.528048,-2.261513],[-8.838761,7.610539,-4.106679,0.044173,-3.910635,-5.210316,-1.972254,3.526215,9.832569,-6.664981,-4.424381,-1.403645],[-9.818580,-0.686414,6.479644,-8.016984,-7.687253,4.352567,-2.390109,4.869121,6.082534,-6.421854,-1.045116,3.473691]]], dtype = "float64")#candidate|10555|(3, 7, 12)|const|float64
uop_10556 = relay.log10(const_10555.astype('float64')) # shape=(3, 7, 12)
func_7413_call = mod.get_global_var('func_7413')
func_7415_call = mutated_mod.get_global_var('func_7415')
call_10565 = func_7413_call()
call_10566 = func_7413_call()
func_3955_call = mod.get_global_var('func_3955')
func_3957_call = mutated_mod.get_global_var('func_3957')
call_10570 = relay.TupleGetItem(func_3955_call(), 0)
call_10571 = relay.TupleGetItem(func_3957_call(), 0)
func_6765_call = mod.get_global_var('func_6765')
func_6766_call = mutated_mod.get_global_var('func_6766')
call_10580 = relay.TupleGetItem(func_6765_call(), 0)
call_10581 = relay.TupleGetItem(func_6766_call(), 0)
output = relay.Tuple([uop_10556,call_10565,call_10570,call_10580,])
output2 = relay.Tuple([uop_10556,call_10566,call_10571,call_10581,])
func_10582 = relay.Function([], output)
mod['func_10582'] = func_10582
mod = relay.transform.InferType()(mod)
output = func_10582()
func_10583 = relay.Function([], output)
mutated_mod['func_10583'] = func_10583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7788_call = mod.get_global_var('func_7788')
func_7790_call = mutated_mod.get_global_var('func_7790')
call_10679 = relay.TupleGetItem(func_7788_call(), 6)
call_10680 = relay.TupleGetItem(func_7790_call(), 6)
func_5908_call = mod.get_global_var('func_5908')
func_5909_call = mutated_mod.get_global_var('func_5909')
call_10685 = relay.TupleGetItem(func_5908_call(), 1)
call_10686 = relay.TupleGetItem(func_5909_call(), 1)
func_9467_call = mod.get_global_var('func_9467')
func_9468_call = mutated_mod.get_global_var('func_9468')
call_10693 = relay.TupleGetItem(func_9467_call(), 0)
call_10694 = relay.TupleGetItem(func_9468_call(), 0)
func_7357_call = mod.get_global_var('func_7357')
func_7360_call = mutated_mod.get_global_var('func_7360')
var_10712 = relay.var("var_10712", dtype = "float32", shape = (780,))#candidate|10712|(780,)|var|float32
call_10711 = relay.TupleGetItem(func_7357_call(relay.reshape(var_10712.astype('float32'), [15, 4, 13]), relay.reshape(var_10712.astype('float32'), [15, 4, 13]), ), 0)
call_10713 = relay.TupleGetItem(func_7360_call(relay.reshape(var_10712.astype('float32'), [15, 4, 13]), relay.reshape(var_10712.astype('float32'), [15, 4, 13]), ), 0)
var_10716 = relay.var("var_10716", dtype = "float32", shape = (780,))#candidate|10716|(780,)|var|float32
bop_10717 = relay.multiply(var_10712.astype('uint16'), relay.reshape(var_10716.astype('uint16'), relay.shape_of(var_10712))) # shape=(780,)
output = relay.Tuple([call_10679,call_10685,call_10693,call_10711,bop_10717,])
output2 = relay.Tuple([call_10680,call_10686,call_10694,call_10713,bop_10717,])
func_10722 = relay.Function([var_10712,var_10716,], output)
mod['func_10722'] = func_10722
mod = relay.transform.InferType()(mod)
mutated_mod['func_10722'] = func_10722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10722_call = mutated_mod.get_global_var('func_10722')
var_10724 = relay.var("var_10724", dtype = "float32", shape = (780,))#candidate|10724|(780,)|var|float32
var_10725 = relay.var("var_10725", dtype = "float32", shape = (780,))#candidate|10725|(780,)|var|float32
call_10723 = func_10722_call(var_10724,var_10725,)
output = call_10723
func_10726 = relay.Function([var_10724,var_10725,], output)
mutated_mod['func_10726'] = func_10726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4990_call = mod.get_global_var('func_4990')
func_4991_call = mutated_mod.get_global_var('func_4991')
call_10735 = func_4990_call()
call_10736 = func_4990_call()
output = relay.Tuple([call_10735,])
output2 = relay.Tuple([call_10736,])
func_10762 = relay.Function([], output)
mod['func_10762'] = func_10762
mod = relay.transform.InferType()(mod)
output = func_10762()
func_10763 = relay.Function([], output)
mutated_mod['func_10763'] = func_10763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9289_call = mod.get_global_var('func_9289')
func_9291_call = mutated_mod.get_global_var('func_9291')
call_10814 = func_9289_call()
call_10815 = func_9289_call()
func_5171_call = mod.get_global_var('func_5171')
func_5172_call = mutated_mod.get_global_var('func_5172')
call_10841 = relay.TupleGetItem(func_5171_call(), 4)
call_10842 = relay.TupleGetItem(func_5172_call(), 4)
output = relay.Tuple([call_10814,call_10841,])
output2 = relay.Tuple([call_10815,call_10842,])
func_10853 = relay.Function([], output)
mod['func_10853'] = func_10853
mod = relay.transform.InferType()(mod)
mutated_mod['func_10853'] = func_10853
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10853_call = mutated_mod.get_global_var('func_10853')
call_10854 = func_10853_call()
output = call_10854
func_10855 = relay.Function([], output)
mutated_mod['func_10855'] = func_10855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5289_call = mod.get_global_var('func_5289')
func_5291_call = mutated_mod.get_global_var('func_5291')
call_10892 = relay.TupleGetItem(func_5289_call(), 4)
call_10893 = relay.TupleGetItem(func_5291_call(), 4)
output = call_10892
output2 = call_10893
func_10903 = relay.Function([], output)
mod['func_10903'] = func_10903
mod = relay.transform.InferType()(mod)
output = func_10903()
func_10904 = relay.Function([], output)
mutated_mod['func_10904'] = func_10904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6704_call = mod.get_global_var('func_6704')
func_6705_call = mutated_mod.get_global_var('func_6705')
call_10907 = relay.TupleGetItem(func_6704_call(), 0)
call_10908 = relay.TupleGetItem(func_6705_call(), 0)
output = call_10907
output2 = call_10908
func_10955 = relay.Function([], output)
mod['func_10955'] = func_10955
mod = relay.transform.InferType()(mod)
mutated_mod['func_10955'] = func_10955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10955_call = mutated_mod.get_global_var('func_10955')
call_10956 = func_10955_call()
output = call_10956
func_10957 = relay.Function([], output)
mutated_mod['func_10957'] = func_10957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7918_call = mod.get_global_var('func_7918')
func_7920_call = mutated_mod.get_global_var('func_7920')
call_10982 = relay.TupleGetItem(func_7918_call(), 0)
call_10983 = relay.TupleGetItem(func_7920_call(), 0)
output = relay.Tuple([call_10982,])
output2 = relay.Tuple([call_10983,])
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
var_10998 = relay.var("var_10998", dtype = "float32", shape = (12, 10, 9))#candidate|10998|(12, 10, 9)|var|float32
uop_10999 = relay.asin(var_10998.astype('float32')) # shape=(12, 10, 9)
func_6030_call = mod.get_global_var('func_6030')
func_6034_call = mutated_mod.get_global_var('func_6034')
const_11004 = relay.const([[-5,-10,9,5,-4,-1,-10,5,-2,2,-8,-2,5,6,1,2,4,4,-7,-5,1,-7,-3,-1,-3,2,-9,10]], dtype = "int8")#candidate|11004|(1, 28)|const|int8
var_11005 = relay.var("var_11005", dtype = "float64", shape = (448,))#candidate|11005|(448,)|var|float64
call_11003 = relay.TupleGetItem(func_6030_call(relay.reshape(const_11004.astype('int8'), [28,]), relay.reshape(var_11005.astype('float64'), [448,]), ), 2)
call_11006 = relay.TupleGetItem(func_6034_call(relay.reshape(const_11004.astype('int8'), [28,]), relay.reshape(var_11005.astype('float64'), [448,]), ), 2)
func_9360_call = mod.get_global_var('func_9360')
func_9362_call = mutated_mod.get_global_var('func_9362')
call_11009 = relay.TupleGetItem(func_9360_call(), 0)
call_11010 = relay.TupleGetItem(func_9362_call(), 0)
var_11017 = relay.var("var_11017", dtype = "float32", shape = (12, 10, 9))#candidate|11017|(12, 10, 9)|var|float32
bop_11018 = relay.divide(uop_10999.astype('float32'), relay.reshape(var_11017.astype('float32'), relay.shape_of(uop_10999))) # shape=(12, 10, 9)
func_7511_call = mod.get_global_var('func_7511')
func_7513_call = mutated_mod.get_global_var('func_7513')
call_11030 = relay.TupleGetItem(func_7511_call(), 0)
call_11031 = relay.TupleGetItem(func_7513_call(), 0)
output = relay.Tuple([call_11003,const_11004,var_11005,call_11009,bop_11018,call_11030,])
output2 = relay.Tuple([call_11006,const_11004,var_11005,call_11010,bop_11018,call_11031,])
func_11040 = relay.Function([var_10998,var_11005,var_11017,], output)
mod['func_11040'] = func_11040
mod = relay.transform.InferType()(mod)
mutated_mod['func_11040'] = func_11040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11040_call = mutated_mod.get_global_var('func_11040')
var_11042 = relay.var("var_11042", dtype = "float32", shape = (12, 10, 9))#candidate|11042|(12, 10, 9)|var|float32
var_11043 = relay.var("var_11043", dtype = "float64", shape = (448,))#candidate|11043|(448,)|var|float64
var_11044 = relay.var("var_11044", dtype = "float32", shape = (12, 10, 9))#candidate|11044|(12, 10, 9)|var|float32
call_11041 = func_11040_call(var_11042,var_11043,var_11044,)
output = call_11041
func_11045 = relay.Function([var_11042,var_11043,var_11044,], output)
mutated_mod['func_11045'] = func_11045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8589_call = mod.get_global_var('func_8589')
func_8590_call = mutated_mod.get_global_var('func_8590')
call_11113 = func_8589_call()
call_11114 = func_8589_call()
output = call_11113
output2 = call_11114
func_11138 = relay.Function([], output)
mod['func_11138'] = func_11138
mod = relay.transform.InferType()(mod)
mutated_mod['func_11138'] = func_11138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11138_call = mutated_mod.get_global_var('func_11138')
call_11139 = func_11138_call()
output = call_11139
func_11140 = relay.Function([], output)
mutated_mod['func_11140'] = func_11140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9542_call = mod.get_global_var('func_9542')
func_9544_call = mutated_mod.get_global_var('func_9544')
call_11174 = relay.TupleGetItem(func_9542_call(), 0)
call_11175 = relay.TupleGetItem(func_9544_call(), 0)
uop_11186 = relay.sinh(call_11174.astype('float32')) # shape=(6, 6, 8)
uop_11188 = relay.sinh(call_11175.astype('float32')) # shape=(6, 6, 8)
func_5573_call = mod.get_global_var('func_5573')
func_5577_call = mutated_mod.get_global_var('func_5577')
const_11197 = relay.const(8, dtype = "int8")#candidate|11197|()|const|int8
const_11198 = relay.const([4,5,-2,1,1,-5,-7,9,2,-1,5,-1,-6,9,10,6,-5,-3,3,6,3,-10,2,6,-3,-10,4,3], dtype = "int8")#candidate|11198|(28,)|const|int8
call_11196 = relay.TupleGetItem(func_5573_call(relay.reshape(const_11197.astype('int8'), []), relay.reshape(const_11198.astype('int8'), [28,]), ), 1)
call_11199 = relay.TupleGetItem(func_5577_call(relay.reshape(const_11197.astype('int8'), []), relay.reshape(const_11198.astype('int8'), [28,]), ), 1)
output = relay.Tuple([uop_11186,call_11196,const_11197,const_11198,])
output2 = relay.Tuple([uop_11188,call_11199,const_11197,const_11198,])
func_11200 = relay.Function([], output)
mod['func_11200'] = func_11200
mod = relay.transform.InferType()(mod)
mutated_mod['func_11200'] = func_11200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11200_call = mutated_mod.get_global_var('func_11200')
call_11201 = func_11200_call()
output = call_11201
func_11202 = relay.Function([], output)
mutated_mod['func_11202'] = func_11202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9360_call = mod.get_global_var('func_9360')
func_9362_call = mutated_mod.get_global_var('func_9362')
call_11203 = relay.TupleGetItem(func_9360_call(), 0)
call_11204 = relay.TupleGetItem(func_9362_call(), 0)
func_8118_call = mod.get_global_var('func_8118')
func_8122_call = mutated_mod.get_global_var('func_8122')
var_11246 = relay.var("var_11246", dtype = "uint16", shape = (784,))#candidate|11246|(784,)|var|uint16
var_11247 = relay.var("var_11247", dtype = "int64", shape = (588,))#candidate|11247|(588,)|var|int64
call_11245 = relay.TupleGetItem(func_8118_call(relay.reshape(var_11246.astype('uint16'), [784,]), relay.reshape(var_11247.astype('int64'), [588,]), ), 4)
call_11248 = relay.TupleGetItem(func_8122_call(relay.reshape(var_11246.astype('uint16'), [784,]), relay.reshape(var_11247.astype('int64'), [588,]), ), 4)
output = relay.Tuple([call_11203,call_11245,var_11246,var_11247,])
output2 = relay.Tuple([call_11204,call_11248,var_11246,var_11247,])
func_11260 = relay.Function([var_11246,var_11247,], output)
mod['func_11260'] = func_11260
mod = relay.transform.InferType()(mod)
mutated_mod['func_11260'] = func_11260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11260_call = mutated_mod.get_global_var('func_11260')
var_11262 = relay.var("var_11262", dtype = "uint16", shape = (784,))#candidate|11262|(784,)|var|uint16
var_11263 = relay.var("var_11263", dtype = "int64", shape = (588,))#candidate|11263|(588,)|var|int64
call_11261 = func_11260_call(var_11262,var_11263,)
output = call_11261
func_11264 = relay.Function([var_11262,var_11263,], output)
mutated_mod['func_11264'] = func_11264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7053_call = mod.get_global_var('func_7053')
func_7054_call = mutated_mod.get_global_var('func_7054')
call_11325 = relay.TupleGetItem(func_7053_call(), 1)
call_11326 = relay.TupleGetItem(func_7054_call(), 1)
output = relay.Tuple([call_11325,])
output2 = relay.Tuple([call_11326,])
func_11331 = relay.Function([], output)
mod['func_11331'] = func_11331
mod = relay.transform.InferType()(mod)
output = func_11331()
func_11332 = relay.Function([], output)
mutated_mod['func_11332'] = func_11332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4049_call = mod.get_global_var('func_4049')
func_4051_call = mutated_mod.get_global_var('func_4051')
call_11355 = relay.TupleGetItem(func_4049_call(), 0)
call_11356 = relay.TupleGetItem(func_4051_call(), 0)
output = call_11355
output2 = call_11356
func_11357 = relay.Function([], output)
mod['func_11357'] = func_11357
mod = relay.transform.InferType()(mod)
output = func_11357()
func_11358 = relay.Function([], output)
mutated_mod['func_11358'] = func_11358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5289_call = mod.get_global_var('func_5289')
func_5291_call = mutated_mod.get_global_var('func_5291')
call_11390 = relay.TupleGetItem(func_5289_call(), 2)
call_11391 = relay.TupleGetItem(func_5291_call(), 2)
func_10045_call = mod.get_global_var('func_10045')
func_10048_call = mutated_mod.get_global_var('func_10048')
var_11393 = relay.var("var_11393", dtype = "float32", shape = (112,))#candidate|11393|(112,)|var|float32
var_11394 = relay.var("var_11394", dtype = "int64", shape = (1, 588))#candidate|11394|(1, 588)|var|int64
call_11392 = relay.TupleGetItem(func_10045_call(relay.reshape(var_11393.astype('float32'), [1, 7, 16]), relay.reshape(var_11394.astype('int64'), [588,]), ), 0)
call_11395 = relay.TupleGetItem(func_10048_call(relay.reshape(var_11393.astype('float32'), [1, 7, 16]), relay.reshape(var_11394.astype('int64'), [588,]), ), 0)
func_9713_call = mod.get_global_var('func_9713')
func_9714_call = mutated_mod.get_global_var('func_9714')
call_11401 = relay.TupleGetItem(func_9713_call(), 0)
call_11402 = relay.TupleGetItem(func_9714_call(), 0)
func_3955_call = mod.get_global_var('func_3955')
func_3957_call = mutated_mod.get_global_var('func_3957')
call_11411 = relay.TupleGetItem(func_3955_call(), 0)
call_11412 = relay.TupleGetItem(func_3957_call(), 0)
output = relay.Tuple([call_11390,call_11392,var_11393,var_11394,call_11401,call_11411,])
output2 = relay.Tuple([call_11391,call_11395,var_11393,var_11394,call_11402,call_11412,])
func_11417 = relay.Function([var_11393,var_11394,], output)
mod['func_11417'] = func_11417
mod = relay.transform.InferType()(mod)
var_11418 = relay.var("var_11418", dtype = "float32", shape = (112,))#candidate|11418|(112,)|var|float32
var_11419 = relay.var("var_11419", dtype = "int64", shape = (1, 588))#candidate|11419|(1, 588)|var|int64
output = func_11417(var_11418,var_11419,)
func_11420 = relay.Function([var_11418,var_11419,], output)
mutated_mod['func_11420'] = func_11420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8589_call = mod.get_global_var('func_8589')
func_8590_call = mutated_mod.get_global_var('func_8590')
call_11517 = func_8589_call()
call_11518 = func_8589_call()
output = call_11517
output2 = call_11518
func_11523 = relay.Function([], output)
mod['func_11523'] = func_11523
mod = relay.transform.InferType()(mod)
mutated_mod['func_11523'] = func_11523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11523_call = mutated_mod.get_global_var('func_11523')
call_11524 = func_11523_call()
output = call_11524
func_11525 = relay.Function([], output)
mutated_mod['func_11525'] = func_11525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7087_call = mod.get_global_var('func_7087')
func_7088_call = mutated_mod.get_global_var('func_7088')
call_11533 = relay.TupleGetItem(func_7087_call(), 0)
call_11534 = relay.TupleGetItem(func_7088_call(), 0)
uop_11564 = relay.sqrt(call_11533.astype('float64')) # shape=(1, 7, 16)
uop_11566 = relay.sqrt(call_11534.astype('float64')) # shape=(1, 7, 16)
var_11579 = relay.var("var_11579", dtype = "float64", shape = (1, 7, 16))#candidate|11579|(1, 7, 16)|var|float64
bop_11580 = relay.right_shift(uop_11564.astype('uint16'), relay.reshape(var_11579.astype('uint16'), relay.shape_of(uop_11564))) # shape=(1, 7, 16)
bop_11583 = relay.right_shift(uop_11566.astype('uint16'), relay.reshape(var_11579.astype('uint16'), relay.shape_of(uop_11566))) # shape=(1, 7, 16)
func_4081_call = mod.get_global_var('func_4081')
func_4082_call = mutated_mod.get_global_var('func_4082')
call_11587 = relay.TupleGetItem(func_4081_call(), 0)
call_11588 = relay.TupleGetItem(func_4082_call(), 0)
output = relay.Tuple([bop_11580,call_11587,])
output2 = relay.Tuple([bop_11583,call_11588,])
func_11601 = relay.Function([var_11579,], output)
mod['func_11601'] = func_11601
mod = relay.transform.InferType()(mod)
mutated_mod['func_11601'] = func_11601
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11602 = relay.var("var_11602", dtype = "float64", shape = (1, 7, 16))#candidate|11602|(1, 7, 16)|var|float64
func_11601_call = mutated_mod.get_global_var('func_11601')
call_11603 = func_11601_call(var_11602)
output = call_11603
func_11604 = relay.Function([var_11602], output)
mutated_mod['func_11604'] = func_11604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7511_call = mod.get_global_var('func_7511')
func_7513_call = mutated_mod.get_global_var('func_7513')
call_11606 = relay.TupleGetItem(func_7511_call(), 0)
call_11607 = relay.TupleGetItem(func_7513_call(), 0)
func_5370_call = mod.get_global_var('func_5370')
func_5371_call = mutated_mod.get_global_var('func_5371')
call_11610 = relay.TupleGetItem(func_5370_call(), 3)
call_11611 = relay.TupleGetItem(func_5371_call(), 3)
var_11614 = relay.var("var_11614", dtype = "int64", shape = (14, 42))#candidate|11614|(14, 42)|var|int64
bop_11615 = relay.divide(call_11610.astype('float32'), relay.reshape(var_11614.astype('float32'), relay.shape_of(call_11610))) # shape=(14, 42)
bop_11618 = relay.divide(call_11611.astype('float32'), relay.reshape(var_11614.astype('float32'), relay.shape_of(call_11611))) # shape=(14, 42)
uop_11624 = relay.cosh(var_11614.astype('float64')) # shape=(14, 42)
uop_11626 = relay.acos(bop_11615.astype('float64')) # shape=(14, 42)
uop_11628 = relay.acos(bop_11618.astype('float64')) # shape=(14, 42)
output = relay.Tuple([call_11606,uop_11624,uop_11626,])
output2 = relay.Tuple([call_11607,uop_11624,uop_11628,])
func_11634 = relay.Function([var_11614,], output)
mod['func_11634'] = func_11634
mod = relay.transform.InferType()(mod)
var_11635 = relay.var("var_11635", dtype = "int64", shape = (14, 42))#candidate|11635|(14, 42)|var|int64
output = func_11634(var_11635)
func_11636 = relay.Function([var_11635], output)
mutated_mod['func_11636'] = func_11636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9071_call = mod.get_global_var('func_9071')
func_9073_call = mutated_mod.get_global_var('func_9073')
call_11724 = relay.TupleGetItem(func_9071_call(), 0)
call_11725 = relay.TupleGetItem(func_9073_call(), 0)
func_8826_call = mod.get_global_var('func_8826')
func_8827_call = mutated_mod.get_global_var('func_8827')
call_11739 = relay.TupleGetItem(func_8826_call(), 0)
call_11740 = relay.TupleGetItem(func_8827_call(), 0)
func_6756_call = mod.get_global_var('func_6756')
func_6758_call = mutated_mod.get_global_var('func_6758')
call_11741 = relay.TupleGetItem(func_6756_call(), 1)
call_11742 = relay.TupleGetItem(func_6758_call(), 1)
output = relay.Tuple([call_11724,call_11739,call_11741,])
output2 = relay.Tuple([call_11725,call_11740,call_11742,])
func_11744 = relay.Function([], output)
mod['func_11744'] = func_11744
mod = relay.transform.InferType()(mod)
mutated_mod['func_11744'] = func_11744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11744_call = mutated_mod.get_global_var('func_11744')
call_11745 = func_11744_call()
output = call_11745
func_11746 = relay.Function([], output)
mutated_mod['func_11746'] = func_11746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6560_call = mod.get_global_var('func_6560')
func_6562_call = mutated_mod.get_global_var('func_6562')
call_11800 = func_6560_call()
call_11801 = func_6560_call()
output = call_11800
output2 = call_11801
func_11808 = relay.Function([], output)
mod['func_11808'] = func_11808
mod = relay.transform.InferType()(mod)
output = func_11808()
func_11809 = relay.Function([], output)
mutated_mod['func_11809'] = func_11809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9216_call = mod.get_global_var('func_9216')
func_9217_call = mutated_mod.get_global_var('func_9217')
call_11890 = relay.TupleGetItem(func_9216_call(), 0)
call_11891 = relay.TupleGetItem(func_9217_call(), 0)
output = call_11890
output2 = call_11891
func_11892 = relay.Function([], output)
mod['func_11892'] = func_11892
mod = relay.transform.InferType()(mod)
output = func_11892()
func_11893 = relay.Function([], output)
mutated_mod['func_11893'] = func_11893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9071_call = mod.get_global_var('func_9071')
func_9073_call = mutated_mod.get_global_var('func_9073')
call_11917 = relay.TupleGetItem(func_9071_call(), 0)
call_11918 = relay.TupleGetItem(func_9073_call(), 0)
func_11200_call = mod.get_global_var('func_11200')
func_11202_call = mutated_mod.get_global_var('func_11202')
call_11941 = relay.TupleGetItem(func_11200_call(), 2)
call_11942 = relay.TupleGetItem(func_11202_call(), 2)
output = relay.Tuple([call_11917,call_11941,])
output2 = relay.Tuple([call_11918,call_11942,])
func_11962 = relay.Function([], output)
mod['func_11962'] = func_11962
mod = relay.transform.InferType()(mod)
mutated_mod['func_11962'] = func_11962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11962_call = mutated_mod.get_global_var('func_11962')
call_11963 = func_11962_call()
output = call_11963
func_11964 = relay.Function([], output)
mutated_mod['func_11964'] = func_11964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8826_call = mod.get_global_var('func_8826')
func_8827_call = mutated_mod.get_global_var('func_8827')
call_12003 = relay.TupleGetItem(func_8826_call(), 0)
call_12004 = relay.TupleGetItem(func_8827_call(), 0)
var_12016 = relay.var("var_12016", dtype = "float32", shape = (16, 7, 16))#candidate|12016|(16, 7, 16)|var|float32
bop_12017 = relay.less(call_12003.astype('bool'), var_12016.astype('bool')) # shape=(16, 7, 16)
bop_12020 = relay.less(call_12004.astype('bool'), var_12016.astype('bool')) # shape=(16, 7, 16)
bop_12022 = relay.logical_xor(bop_12017.astype('int8'), call_12003.astype('int8')) # shape=(16, 7, 16)
bop_12025 = relay.logical_xor(bop_12020.astype('int8'), call_12004.astype('int8')) # shape=(16, 7, 16)
output = relay.Tuple([bop_12022,])
output2 = relay.Tuple([bop_12025,])
func_12031 = relay.Function([var_12016,], output)
mod['func_12031'] = func_12031
mod = relay.transform.InferType()(mod)
var_12032 = relay.var("var_12032", dtype = "float32", shape = (16, 7, 16))#candidate|12032|(16, 7, 16)|var|float32
output = func_12031(var_12032)
func_12033 = relay.Function([var_12032], output)
mutated_mod['func_12033'] = func_12033
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12054 = relay.var("var_12054", dtype = "uint32", shape = (12, 3, 2))#candidate|12054|(12, 3, 2)|var|uint32
var_12055 = relay.var("var_12055", dtype = "uint32", shape = (12, 3, 2))#candidate|12055|(12, 3, 2)|var|uint32
bop_12056 = relay.multiply(var_12054.astype('uint32'), relay.reshape(var_12055.astype('uint32'), relay.shape_of(var_12054))) # shape=(12, 3, 2)
func_7087_call = mod.get_global_var('func_7087')
func_7088_call = mutated_mod.get_global_var('func_7088')
call_12060 = relay.TupleGetItem(func_7087_call(), 0)
call_12061 = relay.TupleGetItem(func_7088_call(), 0)
func_6328_call = mod.get_global_var('func_6328')
func_6330_call = mutated_mod.get_global_var('func_6330')
call_12065 = relay.TupleGetItem(func_6328_call(), 1)
call_12066 = relay.TupleGetItem(func_6330_call(), 1)
output = relay.Tuple([bop_12056,call_12060,call_12065,])
output2 = relay.Tuple([bop_12056,call_12061,call_12066,])
func_12068 = relay.Function([var_12054,var_12055,], output)
mod['func_12068'] = func_12068
mod = relay.transform.InferType()(mod)
var_12069 = relay.var("var_12069", dtype = "uint32", shape = (12, 3, 2))#candidate|12069|(12, 3, 2)|var|uint32
var_12070 = relay.var("var_12070", dtype = "uint32", shape = (12, 3, 2))#candidate|12070|(12, 3, 2)|var|uint32
output = func_12068(var_12069,var_12070,)
func_12071 = relay.Function([var_12069,var_12070,], output)
mutated_mod['func_12071'] = func_12071
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12097 = relay.const(1, dtype = "uint64")#candidate|12097|()|const|uint64
var_12098 = relay.var("var_12098", dtype = "uint64", shape = (1, 9, 12))#candidate|12098|(1, 9, 12)|var|uint64
bop_12099 = relay.maximum(const_12097.astype('uint64'), var_12098.astype('uint64')) # shape=(1, 9, 12)
func_4510_call = mod.get_global_var('func_4510')
func_4515_call = mutated_mod.get_global_var('func_4515')
var_12105 = relay.var("var_12105", dtype = "uint16", shape = (660, 1))#candidate|12105|(660, 1)|var|uint16
const_12106 = relay.const([1,5,8,-8,-8,-9,2,-5,-7,2,-7,-10,-4,3,-5,4,-10,8,10,6,4,-4,1,-5,-10,-4,7,-9,-8,-10,7,-9,-3,-3,-2,3,-4,4,-8,6,7,5,1,4,-4,-6,-8,-8,-3,-8,-9,3,-9,1,-8,-5,4,-9,-4,8,-7,9,-9,-10,7,7,8,1,1,-5,8,3,2,1,-3,3,1,-7,10,-3,5,5,4,-1,10,1,7,-4,-6,-4,1,-8,3,3,3,10,-7,-1,3,-5,7,-4,2,3,10,6,7,6,-1,3,8,-2,-10,-6,-5,7,9,-6,9,6,7,5,-7,-3,-1,-2,10,3,-9,5,2,-7,5,-1,-5,6,-8,-5,1,5,6,2,-5,8,-6,9,-6,10,-2,-6,7,-10,-4,-1,-4,-8,6,-6,4,5,6,-9,-10,4,9,10,3,-10,4,-3,-10,7,-8,6,-7,-4,-5,-5,-4,-9,-10,-1,-7,-9,4,9,2,9,1,4,6,-2,4,6,-8,-3,3,1,-4,-1,4,-2,8,-6,9,-6,1,8,9,3,10,-8,-7,3,1,10,3,-4,7,9,-2,-5,-5,6,8,1,-5,-10,-8,-6,6,6,9,-2,10,4,-6,-6,-3,-5,4,-10,-5,-1,-3,3,4,1,-1,-2,2,-4,-7,1,3,-1,-2,-5,-1,-1,5,4,-5,-3,-7,9,10,-10,-4,-9,7,-5,10,7,8,8,3,-3,6,-7,10,4,1,-9,3,3,7,-10,-10,10,6,-1,9,-9,9,-10,4,-9,6,-10,-5,2,1,-10,-8,8,10,10,3,-6,7,-9,10,6,5,8,8,-1,1,-1,6,10,9,7,1,-4,1,-9,-3,-8,2,-10,5,1,-5,-4,2,-6,6,-4,-7,7,-4,-9,-5,7,5,8,-1,8,3,-8,8,5,7,4,8,4,-10,-2,1,2,9,8,1,7,-9,-9,8,2,-5,-1,-8,6,-7,-4,-10,-4,6,-10,-9,-3,1,-7,7,-6,6,5,2,3,-2,10,3,2,6,-8,-8,-5,-2,9,4,2,-5,-5,2,8,6,7,-2,9,-2,4,8,10,4,1,-7,7,2,8,-9,-8,-4,4,-6,3,10,10,9,-9,-1,10,-5,-9,8,-1,-6,1,5,-6,-8,9,-8,-7,-10,1,-7,9,-7,-1,10,1,-2,-5,-10,10,-10,8,-7,-9,3,8,1,4,-10,3,8,3,8,6,9,-8,4,-10,-2,10,7,5,-7,-5,3,-6,-2,10,-7,8,4,-8,3,-1,-5,10,9,1,6,3,-4,2,-8,-3,-1,-2,6,-3,-7,4,3,3,1,10,-10,9,-3,-9,5,7,-3,-1,10,8,8,7,-9,-5,-6,10,-7,-9,1,-3,-10,-2,-9,1,-7,-7,4,4,8,-6,4,10,6,-4,-9,-1,5,-3,-6,-6,-5,6,8,-5,-1,1,-8,9,-2,8,9,-4,5,-3,-2,-2,3,-10,-1,-5,7,-8,-7,-6,-1,4,-6,-6,-6,9,-7,4,-10,9,9,-4,2,-1,2,-1,4,2,-4,2,-5,-7,-4,10,-7,-7,-7,-5,6,9,5,-8,-5,-10,7,8,-3,-4,-6,-2,5,9,2,-10,-10,-4,-9,6,3,5,-6,-1,8,7,-2,-8,8,-9,-3,-9,-10,-8,7,4,-9,-9,-4,5,8,9,-1,-6,-4,1,6,10,3,6,3,-10,-1,-9,-9,-8,-6,-6,-3,6,-7,-5,-5,10,3,9,-8,-8,10,-5,-2,8,1,3,-6,9,5,10,-9,9,-6,7,1,-2,-5,-10,9,2,-1,4,-5,-3,-7,10,3,9,2,-3,3,2,2,4,-1,1,-3,-9,8,-9,-7,4,-10,9,-8,5,-6,9,10,-9,-2,-2,7,-5,5,3,-5,-10,-7,9,1,-7,2,5,9,-2,8,8,-7,-10,7,4,10,8,-3,3,10,3,3,-3,-3,5,-1,9,-6,-10,-4,-6,8,-10,-3,-7,10,-5,7,9,-7,3,7,-7,1,-9,-2,9,-1,1,1,-6,-9,8,-3,7,-1,-9], dtype = "uint16")#candidate|12106|(784,)|const|uint16
var_12107 = relay.var("var_12107", dtype = "int64", shape = (588,))#candidate|12107|(588,)|var|int64
call_12104 = relay.TupleGetItem(func_4510_call(relay.reshape(var_12105.astype('uint16'), [11, 10, 6]), relay.reshape(const_12106.astype('uint16'), [392, 2]), relay.reshape(var_12107.astype('int64'), [588,]), ), 1)
call_12108 = relay.TupleGetItem(func_4515_call(relay.reshape(var_12105.astype('uint16'), [11, 10, 6]), relay.reshape(const_12106.astype('uint16'), [392, 2]), relay.reshape(var_12107.astype('int64'), [588,]), ), 1)
var_12110 = relay.var("var_12110", dtype = "uint64", shape = (11, 9, 12))#candidate|12110|(11, 9, 12)|var|uint64
bop_12111 = relay.floor_mod(var_12098.astype('float64'), var_12110.astype('float64')) # shape=(11, 9, 12)
func_8004_call = mod.get_global_var('func_8004')
func_8008_call = mutated_mod.get_global_var('func_8008')
const_12124 = relay.const([5.392228,-5.435845,6.684375,7.630400,-1.051780,-7.583394,9.333820,-8.585650,9.253169,2.312132,-8.203986,8.262399,3.724458,1.107315,6.707768,-5.661479,2.520800,8.984651,-8.744614,9.890032,-3.258058,9.288348,6.933441,7.492901,-2.584599,-4.757578,-4.114194,8.822762,-1.895565,-1.506302,2.927916,8.655540,5.297741,1.231792,7.754347,7.598441,6.871086,-7.648791,-9.026289,1.164870,-2.750214,7.473584,3.386046,8.639542,5.475033,-5.049997,-8.323666,-4.385970,-9.163236,1.588617,-1.945749,-2.943548,5.527271,8.807947,-3.361807,-6.674845,-0.264085,7.456403,7.150983,8.901155,-5.550854,6.506738,8.286924,-2.167079,-8.489374,-3.692790,-3.443657,-5.232830,3.792231,-4.066283,-7.640053,-1.379525,-6.269473,-0.483380,-5.531011,4.544957,7.063311,1.200697,-5.026682,9.760725,8.228458,8.464942,-9.214463,2.973026,6.815120,8.525337,3.660004,-9.011464,2.433057,3.087607,2.468737,-4.197017,2.464813,2.044008,3.626538,-9.798488,-0.397260,2.696618,7.260097,-3.748487,-8.160807,-5.973752,-6.712171,4.103419,-6.184839,5.466623,0.109544,-4.930583,-1.294211,-5.543814,-4.599590,-7.602638,1.793766,6.748324,0.607826,8.267294,4.865182,4.548707,7.044754,9.282799,1.760690,0.790207,-7.866791,6.906186,9.681158,7.383700,6.290368,3.059241,6.959743,6.558626,-0.343391,-2.140273,7.338593,5.846036,-7.546124,-9.327063,-6.270475,3.004858,9.188177,6.300983,-8.626829,7.398029,-7.954369,-7.536888,5.451746,-1.504768,1.208582,-6.030106,-2.146242,0.927664,-3.507142,-2.738490,2.666749,-3.781410,3.142853,1.837710,-9.439927,5.536983,6.563069,-2.145100,8.329927,9.596942,8.821899,1.351744,2.616488,-6.358797,-9.210855,-3.095089,-4.846560,8.643489,-3.303994,-1.710251,7.354397,-9.533508,7.868214,9.724021,2.605478,5.976014,-8.421577,9.285369,0.242274,-0.284364,-5.836411,9.593039,3.735180,-9.865883,-9.690284,-9.691918,-3.001956,-7.716211,7.560045,8.014931,-3.854662,8.735161,0.761723,3.088371,-2.375297,0.817352,-5.717196,-5.772071,5.376774,-5.544130,8.041625,1.139441,5.557220,0.598748,3.542121,0.011906,-4.451465,1.247879,3.248002,-5.038564,-6.869021,7.545441,2.072883,-4.869332,-5.355374,-4.360026,0.957765,-4.068299,8.123907,1.243718,-8.995138,2.298348,4.461377,-9.662957,9.601019,-5.409079,-7.910914,-3.083038,7.463509,-5.828721,5.527162,3.209880,-4.922376,4.588735,-3.173823,9.889768,-9.464442,3.686512,1.852631,-6.539811,-7.033148,-0.817375,-3.144330,-8.738082,2.018455,-0.673799,5.264332,8.224475,1.508347,-9.426559,6.076613,-9.828650,-6.377205,3.324124,3.683025,-7.982979,-4.355478,5.377349,4.777790,6.518587,-3.303478,-7.159795,3.511921,-4.635206,-0.077781,-7.012134,-5.845886,9.100665,-3.371094,-4.203387,1.586648,-9.575838,5.706651,-1.208309,6.996872,8.143714,2.401199,-4.475115,6.178119,7.641832,5.810166,5.351051,-5.024386,-3.707623,6.556592,7.745547,6.739299,-3.080020,7.857600,3.899382,-8.568256,-8.193581,-6.170596,7.167810,6.941374,-9.475567,-2.652346,-5.378326,-4.852515,-5.099231,9.131179,-0.113101,1.326760,4.979198,-8.338020,5.988710,8.565737,-6.140337,-3.800493,2.441831,1.274185,-8.794627,2.420798,-4.264384,8.195489,7.715841,-4.161908,7.202387,8.534000,-7.841733,-2.820310,-1.845759,-1.049558,0.444447,-4.040965,-2.348606,-8.391781,-1.558699,-9.534951,-5.334100,7.150029,-2.769004,9.118809,2.241987,6.234140,-3.874811,0.796858,5.948464,-2.517164,4.486120,-1.040643,-5.139489,-9.296257,-4.359016,4.990009,1.271283,3.299047,8.270782,8.853582,0.087867,-7.875462,-3.630678,-2.442599,4.751309,5.293140,-4.953118,0.283944,-1.054290,8.836662,-7.757048,2.398703,4.058535,5.004768,-5.906302,3.122817,0.047059,3.745120,1.307279,-2.763549,-1.198205,7.292820,9.592481,4.257632,5.867470,-1.650716,-3.679631,6.546311,-9.626666,-6.668307,0.563105,-6.746413,9.905944,7.353092,-8.134542,-7.152695,7.781005,7.918389,-7.464904,-4.891624,1.434828,7.839533,9.610434,8.764285,8.783073,-5.484420,0.642619,-5.035502,-5.091429,8.496329,3.586537,-0.641976,-2.117223,7.099048,-3.246778,-0.262747,-2.420878,3.727507,-2.168543,-4.876507,-9.671937,-0.302478,9.101213,2.513619,-2.293031,-4.809389,-3.064396,-1.873793,-7.976895,4.748190,-3.255280,-1.367259,1.683620,-2.964008,-1.614896,9.824101,8.754813,-1.851764,-5.397234,-7.128720,0.783353,-9.654452,4.797238,-3.337239,-8.924500,3.576662,3.158079,-1.198686,6.544173,-7.204693,7.132368,6.847594,2.786463,7.002641,0.826272,7.373924,2.578727,-1.195955,-4.249673,-7.614924,-7.580532,8.740442,-2.438371,-9.694990,-3.611787,1.413950,-2.226565,-8.950626,0.064055,-2.754863,-6.911168,8.503485,9.636120,-7.693859,-7.089417,2.307064,-6.678671,-2.552013,-1.852446,5.636290,2.405597,-7.654979,3.097155,1.026985,-9.939044,6.083928,1.528829,-0.928217,-8.090557,6.358160,-7.987617,8.487098,1.193945,6.473362,-3.775960,7.956927,8.841752,2.101315,-6.759991,5.341568,-3.795271,5.042292,3.718606,8.390928,2.615008,-0.653318,8.835162,-2.614314,8.078386,-4.020573,-7.365017,5.155356,2.507449,-2.960888,-7.450510,-1.878891,-6.608037,-8.926927,-6.507319,7.556744,-2.981333,5.796433,4.489695,0.102002,6.830411,-6.185737,7.902409,5.713453,7.833301,-3.891356,-2.679459,-6.350887,8.559007,-4.103457,-8.598399,2.131279,-5.859783,-0.835713,-8.545405,-9.913832,5.997871,-9.792003,8.060470,7.692593,0.412958,-6.485910,8.494412,1.783152,3.890447,-8.761117,2.574091,1.599980,-8.945596,-2.537946,4.983073,-7.963464,1.844858,5.376378,-4.433499,6.087884,-5.576467,4.983917,4.550401,-6.369145,3.852967,-9.941559,-8.850981,-1.366435,-2.461234,-9.048747,9.287880,-0.275858,0.156419,7.761225,9.003525,3.981535,-8.720416,9.601350,3.723478,4.390161,-2.420463,-8.789660,1.813838,1.062156,8.668875,3.289551,-5.081921,5.744493,6.503099,1.418181,-5.847277,-6.402098,-7.841096,-8.658007,-1.298010,-5.242753,3.340341,5.760318,1.736360,-8.259276,-6.323880,0.754225,-0.112396,-2.340943,-2.163794,-2.123715,8.012722,8.636734,-5.431585,7.071681,6.709716,1.375442,-2.503424,9.601764,9.912015,-9.776855,5.378507,-5.890825,9.025801,3.905259,-0.383146,-5.393475,3.271337,7.013442,6.254238,-9.122059,-1.692677,4.967367,-3.042103,-8.867476,6.432661,-6.331407,7.412000,-7.129051,9.539079,-9.462343,9.038479,7.638416,-9.681063,-0.330649,-0.591230,5.670600,-0.475247,9.371092,8.301273,-5.231960,1.819775,-1.610782,7.591578,0.944384,-1.414176,-4.616648,-4.370617,-6.348660,6.742560,-2.933488,1.105863,-8.630847,-7.348427,8.754366,-7.523522,-4.397580,-9.679415,-0.299142,6.802541,-1.357713,2.522957,5.061713,0.002061,-4.661837,-1.202096,-4.529671,-4.964402,0.957224,-5.491136,9.144819,-2.010330,-4.038354,-7.164443,-3.802888,-7.212021,2.439651,-3.362570,9.857094,3.889493,-1.670267,-5.191759,4.444960,1.019731,-4.902679,2.536852,-1.108581,4.294409,-3.137865,2.666022,-7.070809,-4.991972,3.737857,-8.999606,-8.080311,6.410645,-4.678351,1.850084,-4.246137,-1.655359,-3.550720,-3.051161,-4.697139,-1.196797,7.785927,4.266782,2.984377,-5.109986,-6.650642,-3.479071,-6.378186,9.624777,1.500634,-1.279159,-5.263157,-6.816723,9.285850,1.793912,9.936052,-4.034381,-4.564436,-5.999834,4.659564,-0.627624,8.097941,-3.576774,-6.977415,-5.454497,-2.746306,-5.351687,-3.568357,-5.528801,6.118491,9.347251,8.939384,-2.090812,1.279456,2.948753,6.867664,2.386020,-0.034854,-5.723152,5.369267,6.055253,6.064160,-5.998082,-6.351850,1.964891,1.313719,-5.653586,6.989712,-1.686040,5.762998,2.321399,5.005906,-4.216516,2.161382,3.661474,0.046185,-9.442974,-2.554808,-3.568646,4.417314,-5.018673,-0.208083,4.139753,1.572110,1.628566,-0.106673,0.838108,4.822958,0.413454,-0.468428,5.763016,2.092555,2.297936,7.205912,0.415520,5.688296,8.223867,-3.235499,3.262583,-8.177725,4.138076,-0.318378,-8.801322,-5.540858,-7.690400,-4.145737,-9.427294,7.289725,8.142007,-1.441129,-8.321813,5.785280,1.791272,-2.940949,0.601179,1.804275,2.751950,-7.193199,6.418017,-3.353021,0.125030,-4.425936,-2.837804,7.458927,-1.472738,-2.108368,-7.250624,-2.073273,-7.110245,-1.382576,2.429082,-4.586533,2.453907,-4.159133,5.418640,-0.907131,-8.815180,-9.866883,2.742570,-1.199847,3.276261,-1.345390,-6.970448,-2.698242,9.415331,3.157952,-5.588961,-2.615991,-8.447337,8.192908,1.910969,-5.668888,-7.712375,-7.204687,1.093553,4.862904,-8.862091,-3.351750,-3.242120,7.500107,4.847738,-4.177079,-2.025310,-2.447964,9.456371,-0.657517,0.135820,-5.014850,9.559904,6.068346,-5.472967,-8.862691,-9.198692,2.376427,2.635879,3.814781,7.565415,-4.353655,-1.275877,-8.350566,-4.971831,-5.641976,-4.102411,5.887582,2.787480,-7.158086,6.189429,-9.632215,7.131667,-8.995851,-4.826901,3.752013,9.473408,2.184928,-9.939986,-0.458632,-4.584807,4.298258,9.483703,2.487317,2.462485,-2.626697,-3.788101,6.817031,2.440049,-5.310537,5.663407,3.947671,4.873137,-3.776181,1.217782,0.565488,5.060472,-0.712973,3.966948,4.687586,8.160326,-3.556530,2.101157,5.025464,2.989762,-6.070086,4.073618,-3.897007,9.663970,8.996163,9.280722,-0.734546,1.014500,6.320644,-3.924925,7.078070,6.200713,7.949632,6.929352,0.471683,-7.161873,9.783740,8.605464,8.370977,-0.284176,8.368687,1.056868,-8.596405,-0.070864,9.486817,7.437729,-5.376475,-1.705086,4.897198,-0.669585,9.618574,-5.874312,0.398434,-2.558261,-0.713032,7.508504,-5.739002,-4.693544,5.666182,-2.389061,2.560848,0.104160,-0.014168,-4.975472,-2.278167,-2.797068,3.791923,-6.708565,1.834751,0.254988,-6.729384,9.152517,7.856991,5.964047,4.453450,-1.051407,1.594293,-9.369590,1.038095,9.082918,-7.836518,3.625679,0.743169,-9.453129,-4.458787,-1.981389,-0.657948,5.364726,3.476822,-1.126188,8.770950,-4.838183,-9.008090,-5.974290,5.705586,6.258034,-8.339234,0.955402,0.780666,-1.106287,-0.752238,-1.094855,-5.856107,-7.212107,-6.374904,-6.772063,9.087479,3.998102,-8.253154,-2.282415,4.200187,4.114445,-9.936683,7.885248,-1.967515,-0.537901,6.936011,6.489153,-5.017354,5.981618,-8.346742,-3.497748,-3.214943,7.034748,-1.419686,-8.614777,-4.825674,5.362269], dtype = "float64")#candidate|12124|(1008,)|const|float64
call_12123 = relay.TupleGetItem(func_8004_call(relay.reshape(const_12124.astype('float64'), [2, 504]), relay.reshape(const_12124.astype('float64'), [2, 504]), ), 6)
call_12125 = relay.TupleGetItem(func_8008_call(relay.reshape(const_12124.astype('float64'), [2, 504]), relay.reshape(const_12124.astype('float64'), [2, 504]), ), 6)
output = relay.Tuple([bop_12099,call_12104,var_12105,const_12106,var_12107,bop_12111,call_12123,const_12124,])
output2 = relay.Tuple([bop_12099,call_12108,var_12105,const_12106,var_12107,bop_12111,call_12125,const_12124,])
func_12144 = relay.Function([var_12098,var_12105,var_12107,var_12110,], output)
mod['func_12144'] = func_12144
mod = relay.transform.InferType()(mod)
mutated_mod['func_12144'] = func_12144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12144_call = mutated_mod.get_global_var('func_12144')
var_12146 = relay.var("var_12146", dtype = "uint64", shape = (1, 9, 12))#candidate|12146|(1, 9, 12)|var|uint64
var_12147 = relay.var("var_12147", dtype = "uint16", shape = (660, 1))#candidate|12147|(660, 1)|var|uint16
var_12148 = relay.var("var_12148", dtype = "int64", shape = (588,))#candidate|12148|(588,)|var|int64
var_12149 = relay.var("var_12149", dtype = "uint64", shape = (11, 9, 12))#candidate|12149|(11, 9, 12)|var|uint64
call_12145 = func_12144_call(var_12146,var_12147,var_12148,var_12149,)
output = call_12145
func_12150 = relay.Function([var_12146,var_12147,var_12148,var_12149,], output)
mutated_mod['func_12150'] = func_12150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5021_call = mod.get_global_var('func_5021')
func_5023_call = mutated_mod.get_global_var('func_5023')
call_12152 = func_5021_call()
call_12153 = func_5021_call()
output = call_12152
output2 = call_12153
func_12160 = relay.Function([], output)
mod['func_12160'] = func_12160
mod = relay.transform.InferType()(mod)
mutated_mod['func_12160'] = func_12160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12160_call = mutated_mod.get_global_var('func_12160')
call_12161 = func_12160_call()
output = call_12161
func_12162 = relay.Function([], output)
mutated_mod['func_12162'] = func_12162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10762_call = mod.get_global_var('func_10762')
func_10763_call = mutated_mod.get_global_var('func_10763')
call_12184 = relay.TupleGetItem(func_10762_call(), 0)
call_12185 = relay.TupleGetItem(func_10763_call(), 0)
output = call_12184
output2 = call_12185
func_12202 = relay.Function([], output)
mod['func_12202'] = func_12202
mod = relay.transform.InferType()(mod)
mutated_mod['func_12202'] = func_12202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12202_call = mutated_mod.get_global_var('func_12202')
call_12203 = func_12202_call()
output = call_12203
func_12204 = relay.Function([], output)
mutated_mod['func_12204'] = func_12204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9686_call = mod.get_global_var('func_9686')
func_9687_call = mutated_mod.get_global_var('func_9687')
call_12205 = func_9686_call()
call_12206 = func_9686_call()
func_9713_call = mod.get_global_var('func_9713')
func_9714_call = mutated_mod.get_global_var('func_9714')
call_12211 = relay.TupleGetItem(func_9713_call(), 0)
call_12212 = relay.TupleGetItem(func_9714_call(), 0)
bop_12231 = relay.left_shift(call_12205.astype('int8'), relay.reshape(call_12211.astype('int8'), relay.shape_of(call_12205))) # shape=(1, 7, 16)
bop_12234 = relay.left_shift(call_12206.astype('int8'), relay.reshape(call_12212.astype('int8'), relay.shape_of(call_12206))) # shape=(1, 7, 16)
output = bop_12231
output2 = bop_12234
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
func_9360_call = mod.get_global_var('func_9360')
func_9362_call = mutated_mod.get_global_var('func_9362')
call_12273 = relay.TupleGetItem(func_9360_call(), 0)
call_12274 = relay.TupleGetItem(func_9362_call(), 0)
output = call_12273
output2 = call_12274
func_12277 = relay.Function([], output)
mod['func_12277'] = func_12277
mod = relay.transform.InferType()(mod)
mutated_mod['func_12277'] = func_12277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12277_call = mutated_mod.get_global_var('func_12277')
call_12278 = func_12277_call()
output = call_12278
func_12279 = relay.Function([], output)
mutated_mod['func_12279'] = func_12279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8770_call = mod.get_global_var('func_8770')
func_8772_call = mutated_mod.get_global_var('func_8772')
call_12297 = relay.TupleGetItem(func_8770_call(), 0)
call_12298 = relay.TupleGetItem(func_8772_call(), 0)
func_1809_call = mod.get_global_var('func_1809')
func_1812_call = mutated_mod.get_global_var('func_1812')
const_12304 = relay.const(9, dtype = "uint64")#candidate|12304|()|const|uint64
const_12305 = relay.const([-2,3,8,8,6,-10,9,2,-1,10,-9,-2,8,-6,-5,-3,7,6,3,-3,3,-5,-1,6,7,1,-1,-4,10,-5,9,1,-3,5,-10,6,-2,-6,9,5,7,3,-1,-6,9,6,-9,-5,-4,10,-7,-9,-9,-1,6,6,4,-3,8,-5,-3,4,8,4,-8,-9,-3,5,3,2,-4,7,10,4,-1,5,-10,8,8,3,6,-2,-10,3,-3,-7,5,-8,3,-7,10,10,10,-1,10,6,-6,7,5,1,6,6,9,-10,-5,9,-6,-9,-5,-9,-4,2,-3,-6,-8,-8,-5,8,8,8,-3,-1,6,-7,10,-7,-1,2,8,2,-9,2,5,-9,8,-8,-6,1,-9,-4,-6,-1,10,1,-5,7,5,5,-1,-3,-4,1,-10,-2,1,-5,-7,-4,-2,-6,-9,-9,4,2,-2,6,8,8,10,-6,-7,7,-1,-2,5,-10,-3,-7,-4,-6,-6,4,10,3,-1,-10,-3,-2,-8,-7,-2,-5,5,4,3,-8,2,4,-4,-3,-7,1,2,4,6,4,10,3,-3,7,-6,-4,8,2,6,-7,10,7,-1,-5,4,-7,1,10,-8,10,5,-4,-4,5,4,7,9,-8,-6,-9,4,-5,-7,-7,-3,9,-2,10,-9,-10,-8,7,-10,10,-1,4,-7,8,-3,7,5,5,10,3,-4,-2,-9,-2,5,-5,-2,-2,10,-1,7,1,5,-9,-3,2,-7,-10,3,-7,5,-7,-1,-4,-8,-5,2,-7,4,-1,2,4,10,-6,-7,3,5,7,-8,-6,-7,-1,9,-5,8,9,1,-7,-9,-6,-8,-10,-9,-8,9,3,-6,-4,-4,7,-9,10,-2,-1,-4,1,7,4,8,5,5,-5,4,-6,-2,-10], dtype = "uint64")#candidate|12305|(336,)|const|uint64
call_12303 = relay.TupleGetItem(func_1809_call(relay.reshape(const_12304.astype('uint64'), []), relay.reshape(const_12305.astype('uint64'), [6, 4, 14]), ), 0)
call_12306 = relay.TupleGetItem(func_1812_call(relay.reshape(const_12304.astype('uint64'), []), relay.reshape(const_12305.astype('uint64'), [6, 4, 14]), ), 0)
output = relay.Tuple([call_12297,call_12303,const_12304,const_12305,])
output2 = relay.Tuple([call_12298,call_12306,const_12304,const_12305,])
func_12311 = relay.Function([], output)
mod['func_12311'] = func_12311
mod = relay.transform.InferType()(mod)
output = func_12311()
func_12312 = relay.Function([], output)
mutated_mod['func_12312'] = func_12312
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6449_call = mod.get_global_var('func_6449')
func_6450_call = mutated_mod.get_global_var('func_6450')
call_12350 = relay.TupleGetItem(func_6449_call(), 0)
call_12351 = relay.TupleGetItem(func_6450_call(), 0)
output = relay.Tuple([call_12350,])
output2 = relay.Tuple([call_12351,])
func_12358 = relay.Function([], output)
mod['func_12358'] = func_12358
mod = relay.transform.InferType()(mod)
output = func_12358()
func_12359 = relay.Function([], output)
mutated_mod['func_12359'] = func_12359
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10992_call = mod.get_global_var('func_10992')
func_10994_call = mutated_mod.get_global_var('func_10994')
call_12433 = relay.TupleGetItem(func_10992_call(), 0)
call_12434 = relay.TupleGetItem(func_10994_call(), 0)
func_5289_call = mod.get_global_var('func_5289')
func_5291_call = mutated_mod.get_global_var('func_5291')
call_12435 = relay.TupleGetItem(func_5289_call(), 1)
call_12436 = relay.TupleGetItem(func_5291_call(), 1)
uop_12449 = relay.asinh(call_12433.astype('float32')) # shape=(14, 42)
uop_12451 = relay.asinh(call_12434.astype('float32')) # shape=(14, 42)
func_9713_call = mod.get_global_var('func_9713')
func_9714_call = mutated_mod.get_global_var('func_9714')
call_12463 = relay.TupleGetItem(func_9713_call(), 0)
call_12464 = relay.TupleGetItem(func_9714_call(), 0)
func_6262_call = mod.get_global_var('func_6262')
func_6264_call = mutated_mod.get_global_var('func_6264')
const_12471 = relay.const([8,10,9,-7,9,2,1,2,4,5,1,-4,1,8,-2,10,6,3,5,-10,3,10,4,10,-10,-6,2,-10,10,10,-8,-9,10,10,5,-2,3,-4,5,-5,-8,-8,10,3,5,-1,4,5,-3,-1,-4,9,-4,4,-7,-4,7,7,-1,9,-6,7,10,3,-9,-4,-7,10,-5,1,-1,-9,9,10,-6,4,-9,1,-4,-3,-1,6,9,1,10,6,-9,4,10,-7,-2,10,3,1,8,-2,2,-10,6,4,3,9,-4,-9,-8,-3,-7,-2,-6,10,8,4,-10,8,6,-1,-2,3,5,2,-8,4,10,8,10,2,7,-5,-10,2,6,7,4,-4,3,2,3,-9,-1,-8,2,-8,-6,8,5,4,-3,-9,-4,-8,9,8,-8,-4,1,-2,2,4,1,5,-3,-9,-3,-5,-3,2,5,-5,-7,3,-3,-1,-3,4,-8,-3,-10,-7,-3,8,7,8,-1,6,2,-4,-4,-9,-1,-2,3,-9,-10,-4,1,8,5,2,1,-4,7,9,4,-8,-2,-3,8,8,2,-10,7,3,-6,-7,-4,1,8,3,-1,-6,-3,-7,-5,-8,8,-2,-4,6,1,-6,-2,-6,-8,-4,-4,-1,1,8,5,-5,-2,8,1,7,-7,6,-1,-2,3,-7,8,4,7,7,9,-7,-6,-8,-10,8,-7,7,-7,6,-6,-9,-2,4,-6,-5,1,-8,6,-4,1,4,-6,-6,1,-5,9,-1,-8,4,4,-10,9,3,-4,-4,1,-4,6,-2,-4,-3,-2,5,7,-5,-7,7,-5,-3,-7,3,-2,5,-7,-6,3,-7,6,-4,-1,6,-3,6,-3,-6,-8,8,-8,-2,9,7,9,-6,5,-10,6,8,10,7,5,-6,4,4,9,6,-4,-10,8,10,6,2,5,-1,-6,-10,2,3,-10,-8,3,-6,7,-1,-2,10,2,-9,-4,4,1,-10,-8,8,9,6,10,-10,8,1,4,-9,3,-3,-8,-6,9,-1,8,4,7,-1,3,-3,-5,-2,-6,-5,-9,-8,3,8,-10,8,10,7,-3,-2,2,-7,10,7,-2,-6,9,10,8,4,6,-7,-6,-4,5,-5,-1,-5,4,6,-2,-7,-8,5,-4,5,-2,8,9,9], dtype = "uint32")#candidate|12471|(432,)|const|uint32
call_12470 = relay.TupleGetItem(func_6262_call(relay.reshape(const_12471.astype('uint32'), [3, 16, 9])), 0)
call_12472 = relay.TupleGetItem(func_6264_call(relay.reshape(const_12471.astype('uint32'), [3, 16, 9])), 0)
bop_12473 = relay.mod(uop_12449.astype('float64'), relay.reshape(call_12433.astype('float64'), relay.shape_of(uop_12449))) # shape=(14, 42)
bop_12476 = relay.mod(uop_12451.astype('float64'), relay.reshape(call_12434.astype('float64'), relay.shape_of(uop_12451))) # shape=(14, 42)
func_3356_call = mod.get_global_var('func_3356')
func_3360_call = mutated_mod.get_global_var('func_3360')
var_12481 = relay.var("var_12481", dtype = "int8", shape = ())#candidate|12481|()|var|int8
const_12482 = relay.const([[-6],[-6],[-6],[6],[1],[-5],[-4],[1],[-6],[-2],[3],[9],[-3],[10],[6],[8],[2],[-4],[1],[4],[-9],[-2],[-5],[5],[-3],[10],[-4],[3]], dtype = "int8")#candidate|12482|(28, 1)|const|int8
call_12480 = relay.TupleGetItem(func_3356_call(relay.reshape(var_12481.astype('int8'), []), relay.reshape(const_12482.astype('int8'), [1, 14, 2]), ), 1)
call_12483 = relay.TupleGetItem(func_3360_call(relay.reshape(var_12481.astype('int8'), []), relay.reshape(const_12482.astype('int8'), [1, 14, 2]), ), 1)
var_12495 = relay.var("var_12495", dtype = "float64", shape = (14, 42))#candidate|12495|(14, 42)|var|float64
bop_12496 = relay.power(bop_12473.astype('float64'), relay.reshape(var_12495.astype('float64'), relay.shape_of(bop_12473))) # shape=(14, 42)
bop_12499 = relay.power(bop_12476.astype('float64'), relay.reshape(var_12495.astype('float64'), relay.shape_of(bop_12476))) # shape=(14, 42)
uop_12500 = relay.acosh(bop_12496.astype('float32')) # shape=(14, 42)
uop_12502 = relay.acosh(bop_12499.astype('float32')) # shape=(14, 42)
bop_12505 = relay.floor_mod(uop_12449.astype('float64'), var_12481.astype('float64')) # shape=(14, 42)
bop_12508 = relay.floor_mod(uop_12451.astype('float64'), var_12481.astype('float64')) # shape=(14, 42)
func_4325_call = mod.get_global_var('func_4325')
func_4328_call = mutated_mod.get_global_var('func_4328')
call_12513 = relay.TupleGetItem(func_4325_call(relay.reshape(call_12480.astype('float32'), [3, 7, 16]), relay.reshape(call_12433.astype('int64'), [588,]), ), 0)
call_12514 = relay.TupleGetItem(func_4328_call(relay.reshape(call_12480.astype('float32'), [3, 7, 16]), relay.reshape(call_12433.astype('int64'), [588,]), ), 0)
func_8250_call = mod.get_global_var('func_8250')
func_8253_call = mutated_mod.get_global_var('func_8253')
call_12515 = relay.TupleGetItem(func_8250_call(relay.reshape(call_12513.astype('float32'), [336,])), 1)
call_12516 = relay.TupleGetItem(func_8253_call(relay.reshape(call_12513.astype('float32'), [336,])), 1)
func_11331_call = mod.get_global_var('func_11331')
func_11332_call = mutated_mod.get_global_var('func_11332')
call_12517 = relay.TupleGetItem(func_11331_call(), 0)
call_12518 = relay.TupleGetItem(func_11332_call(), 0)
output = relay.Tuple([call_12435,call_12463,call_12470,const_12471,call_12480,const_12482,uop_12500,bop_12505,call_12513,call_12515,call_12517,])
output2 = relay.Tuple([call_12436,call_12464,call_12472,const_12471,call_12483,const_12482,uop_12502,bop_12508,call_12514,call_12516,call_12518,])
func_12519 = relay.Function([var_12481,var_12495,], output)
mod['func_12519'] = func_12519
mod = relay.transform.InferType()(mod)
var_12520 = relay.var("var_12520", dtype = "int8", shape = ())#candidate|12520|()|var|int8
var_12521 = relay.var("var_12521", dtype = "float64", shape = (14, 42))#candidate|12521|(14, 42)|var|float64
output = func_12519(var_12520,var_12521,)
func_12522 = relay.Function([var_12520,var_12521,], output)
mutated_mod['func_12522'] = func_12522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8033_call = mod.get_global_var('func_8033')
func_8034_call = mutated_mod.get_global_var('func_8034')
call_12591 = relay.TupleGetItem(func_8033_call(), 1)
call_12592 = relay.TupleGetItem(func_8034_call(), 1)
output = call_12591
output2 = call_12592
func_12594 = relay.Function([], output)
mod['func_12594'] = func_12594
mod = relay.transform.InferType()(mod)
mutated_mod['func_12594'] = func_12594
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12594_call = mutated_mod.get_global_var('func_12594')
call_12595 = func_12594_call()
output = call_12595
func_12596 = relay.Function([], output)
mutated_mod['func_12596'] = func_12596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9542_call = mod.get_global_var('func_9542')
func_9544_call = mutated_mod.get_global_var('func_9544')
call_12660 = relay.TupleGetItem(func_9542_call(), 1)
call_12661 = relay.TupleGetItem(func_9544_call(), 1)
output = call_12660
output2 = call_12661
func_12672 = relay.Function([], output)
mod['func_12672'] = func_12672
mod = relay.transform.InferType()(mod)
output = func_12672()
func_12673 = relay.Function([], output)
mutated_mod['func_12673'] = func_12673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5860_call = mod.get_global_var('func_5860')
func_5862_call = mutated_mod.get_global_var('func_5862')
call_12685 = relay.TupleGetItem(func_5860_call(), 0)
call_12686 = relay.TupleGetItem(func_5862_call(), 0)
func_8004_call = mod.get_global_var('func_8004')
func_8008_call = mutated_mod.get_global_var('func_8008')
const_12690 = relay.const([-9.808645,-0.590436,-0.138340,-8.888885,0.367401,-0.082365,-7.223620,2.176210,3.863192,-0.375523,9.485412,-5.277019,-8.307676,7.532589,8.267661,8.054182,-6.005934,5.756657,8.526215,4.887790,1.631714,3.578721,1.445509,7.692320,8.418810,-9.144516,6.081423,-6.415631,-3.229856,8.800677,-7.011782,-9.196372,8.243430,2.034214,4.575999,6.540270,6.902763,-5.672171,0.190030,8.484167,7.411719,-0.862733,-9.956480,-5.858586,-8.109241,-0.139754,-9.726530,8.502843,6.693233,-8.831970,8.589966,9.007197,-9.673314,2.288653,1.050765,-1.050970,-3.968911,3.949799,4.735234,-7.209420,-1.983452,8.159483,3.751183,-9.096303,7.577925,7.434722,-5.253891,3.443718,-8.613335,7.238574,9.848493,-8.918438,-2.550084,-6.328328,-7.412384,3.571432,-7.484380,2.591339,2.861517,-3.945702,5.226111,-5.776162,-7.224254,-5.180424,-4.304937,-9.524372,-9.547904,-1.438973,-5.115642,-7.051972,1.515023,0.987378,-2.472016,1.403059,-9.836557,2.518253,8.933846,-4.503151,8.348750,-7.637765,-5.469808,-9.446069,3.731338,8.829834,3.318759,-1.946228,5.007547,-3.540713,7.222457,3.167084,9.441503,3.060466,-2.697835,-1.554211,-1.107421,-4.204197,6.804821,0.138282,2.429686,2.774244,6.621504,0.281165,5.835692,-8.168171,3.896933,8.549439,-6.152865,6.314766,-1.113280,1.510735,-6.545048,3.838969,-3.191664,-8.133778,2.849005,-2.507645,-6.241240,6.175995,-7.722927,-9.223344,0.421544,-2.564132,-2.345508,3.952280,-0.042688,6.015103,-1.326943,-5.434709,-4.384053,-1.559070,-0.551589,-9.048857,-4.502990,0.444233,0.539179,-8.888315,4.938578,3.323889,-4.076435,-9.712329,2.101417,6.285867,-8.552866,-8.971601,-7.236762,-1.506959,3.603157,6.954150,-5.639537,-2.439563,-2.373978,-1.894198,-0.736980,6.296757,-5.150311,6.540740,-0.907189,0.191728,-8.429094,0.562324,-3.693587,-9.423795,-2.326315,7.906935,-5.519444,-0.780460,-3.114184,-2.635565,-5.668770,8.411011,3.844552,-8.229491,5.464320,-1.856112,4.440965,5.316865,9.251281,-5.223057,0.107033,-2.549564,4.063942,2.422425,4.545097,-0.435259,3.279702,4.463713,-9.906610,-9.693192,5.477777,-4.198444,-7.003904,6.994793,1.186200,5.066501,1.068271,-4.248300,7.362364,2.323726,0.109763,-3.221813,4.425312,8.619855,-8.211975,-7.437805,-5.690763,-7.333912,-4.483964,-5.848523,3.495782,-0.429557,5.852633,-6.114856,-3.504253,7.715314,1.444469,8.270176,7.366416,6.763615,-6.323340,-7.643906,-9.221567,-8.496340,-7.363921,-3.517453,-8.724223,-6.590535,7.118522,-1.373914,-1.770971,5.008660,-0.847162,6.956221,1.073992,3.650785,-8.543679,-4.578664,-1.190332,4.860512,3.569030,6.210346,-0.920006,5.150280,-7.916255,-1.291459,4.887278,-2.435224,-4.534153,-5.661777,-3.048263,0.365589,6.352118,0.350861,-7.221508,-3.043747,-1.236167,-4.680813,5.295824,-7.226113,2.029872,3.454347,-0.355234,-7.498508,4.435379,-6.118018,-5.841291,-3.395807,6.197926,-3.556230,-3.191894,9.489188,-8.721989,4.147774,0.310415,1.410792,-3.202600,-1.853107,-4.912426,0.529597,3.575723,-6.784181,-0.494611,8.090624,-9.497235,0.003518,-0.045414,-6.614349,-5.753786,-6.811173,6.579734,5.899571,-5.142707,0.721182,-7.424322,-7.585505,-7.406177,-4.044547,5.361298,1.036413,4.753346,-6.519511,5.419233,-3.405814,8.610571,-3.855379,-6.024503,-6.207433,5.182376,0.274646,2.616200,6.980570,-6.892222,-2.252246,0.831151,-2.612767,-9.359073,-7.389880,5.168649,-7.743291,2.356961,5.804629,-8.151413,5.066305,0.620778,4.878931,-8.161074,8.261075,-5.458587,0.265916,8.944449,-1.460075,-5.962544,5.422905,2.619938,-3.755380,-2.998171,-8.591624,-9.094954,-3.718883,6.793481,-1.254463,-1.233530,-9.745023,8.383090,-8.967237,2.825710,-3.353069,4.534486,1.083024,7.961396,-0.077995,-0.154845,-7.039312,-9.614148,-2.792854,6.295638,4.167237,-0.608000,-9.796005,9.715240,-0.732104,-5.934868,0.455418,8.413886,-8.823906,-2.540339,-9.889472,-1.234445,5.163089,-6.302677,-8.567352,-2.833739,3.387122,5.481167,-1.811548,3.555567,-3.000281,-0.546205,8.640081,-2.731705,-9.945020,-0.752894,2.674630,-1.276600,5.664327,8.112802,-1.436538,-1.141598,-1.104572,7.078652,-4.152994,-3.547662,-3.709361,-4.028729,-9.956116,-0.421434,-9.529683,3.169806,9.068036,-3.864551,-6.626474,-7.071701,-8.925311,0.336232,-6.180949,6.931552,5.591153,9.258874,-9.252352,1.225226,4.763402,-0.999337,5.516447,4.615606,7.554012,3.622343,2.339764,-0.655322,-7.310621,7.644825,-8.372490,-4.663338,-9.228962,-1.187914,0.262279,8.175918,3.876362,-4.401583,6.613845,9.882064,-1.545223,1.831436,-3.631188,9.930001,2.217330,7.390677,0.807505,4.956761,-6.645707,3.353889,8.362314,-4.022963,-1.279481,5.741260,-2.084070,-5.922601,-7.098458,5.154117,4.857210,8.996886,9.024399,-5.747327,-3.674994,-7.654195,9.910943,1.907739,-4.514027,4.834661,-8.090165,-6.933781,0.877476,2.255014,-3.891554,-1.040847,1.009030,-7.970617,3.620003,-7.821219,-9.149844,-3.182107,-7.988713,3.324030,2.642539,2.422451,7.445060,-4.560278,-4.567906,-9.087244,-7.099431,-2.189900,1.480249,-3.006250,7.821013,-2.776688,2.541924,-7.443065,-4.234210,-9.527401,-1.715152,-1.022845,-3.099403,7.417264,-6.453084,4.296869,-1.896913,5.657323,0.308273,-7.292274,-0.942306,-3.974243,9.446234,5.847188,-4.587779,7.621991,9.339940,7.931701,7.411311,-2.547312,-6.443489,-0.941884,0.481442,-9.024222,-6.115074,7.919108,-9.341979,-3.354229,-3.151552,8.388144,-9.438839,-2.145043,-6.845101,1.934374,-0.295342,-3.158879,1.215164,5.047326,-9.363819,9.834837,7.851086,4.327921,3.932384,3.078261,6.785979,-3.414383,-1.317276,4.488428,-8.515680,-7.112830,-0.675999,-5.530783,3.013589,-7.320118,7.455923,-9.005315,-5.939072,-4.248742,-0.163733,-9.303800,1.701961,9.326337,9.771398,-5.304531,2.059520,-1.634751,4.483851,4.246092,-4.431447,-1.152072,-1.118268,-8.066384,-2.375587,-5.699472,2.918650,-6.421874,0.046414,-3.988795,-2.295346,8.229203,6.623785,0.697536,-5.241866,7.110789,-2.953730,-3.020225,0.652398,-7.591887,-9.782092,-6.206134,7.885141,-4.328563,-3.875046,3.337645,3.342466,-2.905434,-4.822614,-4.418529,-3.704447,9.994682,3.089575,2.572647,1.903585,0.207074,-7.008988,0.221362,-3.499565,6.011528,-0.935961,-0.442699,1.713843,-3.035240,-1.722761,-9.727013,-5.088323,-9.781127,6.346688,-3.445669,7.234705,-0.635371,7.522297,1.547623,3.873978,-5.636015,0.250713,-8.736202,7.192777,-8.029785,1.725315,5.246834,-3.446938,9.209646,0.105486,-0.367943,2.920267,3.567708,-8.309489,7.335107,4.260657,8.818804,-6.317207,6.393014,-5.959179,5.632729,-8.585632,-8.914321,-4.506090,-5.325107,1.612741,-5.718648,-3.478733,-1.831148,-8.101101,-4.715788,9.273965,-4.108961,1.232931,-7.766677,7.591689,8.476224,-2.392289,7.952506,-6.706498,-1.799605,-8.945955,-3.391212,-6.836818,-6.317530,-2.474669,-8.800222,-6.376531,7.631415,-6.893890,-4.784755,-7.537395,2.984479,3.168086,2.383792,0.407078,2.978230,6.264662,-8.574838,-8.151123,-9.723980,3.740155,2.381398,-5.487218,-9.057696,-3.136392,-5.434528,-5.275777,1.675879,-6.548887,1.711214,-2.944012,-5.806971,2.835354,-3.124040,1.917469,-3.461661,2.509497,-3.002340,3.978723,3.446239,7.565963,-0.512821,5.767422,5.026586,-7.916210,3.193194,-6.797777,-4.326489,-0.922363,5.360898,-7.075427,7.039171,9.746214,0.766045,-9.253281,-0.047505,-0.477942,3.239108,-7.695703,-3.837613,-6.971473,-7.779297,1.387917,-2.213269,5.910271,0.261234,2.465410,7.856946,-8.329108,0.879320,5.067682,6.818694,-1.086247,-7.366227,0.010247,-6.110519,-0.693342,-8.538451,7.593842,-7.846434,5.680632,-9.172942,-5.960851,3.510347,-2.145886,7.431420,6.016347,-2.427516,3.312364,-6.496771,0.728931,-2.993339,6.540869,9.949989,1.033484,8.590946,1.861467,-1.719044,-9.433392,-2.653990,-9.126962,-2.174118,-1.888128,-2.270375,9.527573,3.720640,8.007611,7.284217,-3.391859,4.699429,-5.371757,-4.547925,8.818022,9.804002,2.830108,-5.696002,2.116069,4.776381,0.195378,1.285453,-6.254963,4.657251,3.288678,0.998465,4.071771,6.747521,9.172745,5.798716,-1.460753,-4.699708,2.846899,-8.043549,-4.873450,-2.345703,9.664848,-6.661080,-9.493739,2.488047,-7.024363,-5.258589,2.333597,3.644677,7.228973,3.417820,8.474670,2.732497,6.018558,8.314570,5.900751,9.680291,-3.744978,6.514739,-5.053012,-5.171309,7.240423,-7.527092,-8.075736,3.634690,0.191727,-6.028040,7.746105,7.395037,0.378670,-3.470370,-4.279779,4.205618,8.812128,-6.986245,2.049746,1.825952,0.183920,9.268192,0.676298,3.402438,-9.367525,-8.168230,-4.135192,-9.695728,-1.157317,-2.137892,-4.070202,4.757410,-9.389126,9.283346,-1.831695,-4.062640,5.471374,-8.995696,4.799256,7.387763,8.709557,2.432842,4.525058,4.389192,-9.020803,-8.908008,0.133371,-8.186527,4.328192,3.547587,-0.523731,7.224326,2.476919,2.180068,-4.105434,-4.674118,-4.295355,2.066360,5.733107,5.102327,-4.036988,0.488959,-2.456341,-1.686059,0.732364,5.001380,1.177705,9.396601,-2.935961,3.635987,8.464161,-1.821139,0.836510,3.385736,-7.675742,-1.764740,5.208524,-7.328887,-4.830658,7.654951,-8.864190,6.150024,-6.396797,7.174012,5.717706,2.852815,-3.848453,-1.742850,5.361021,8.448531,1.358134,-9.302102,0.218326,-4.276936,5.799054,3.694394,-1.457586,-3.128647,-8.357285,-1.510124,-5.736677,-4.926764,8.202783,9.105057,9.679445,7.302787,-2.878432,2.577697,-5.005718,4.234394,9.896633,-4.943137,-7.865902,-3.937911,-7.466368,-4.989065,-0.604402,0.764734,-2.779512,-0.233163,3.954493,-3.812171,-2.219756,3.269383,1.507940,-2.209215,-8.115240,-8.172263,4.575416,2.278125,1.927698,1.467602,-3.220693,-1.092251,5.328145,-9.611005,-9.547742,-9.209098,-7.575603,5.510124,5.933381,0.451983,-8.641161,-6.758380,-6.511092,8.122045,1.717995,-9.918900,-0.001457,-4.071174,5.182193,-3.353901,0.260753,-8.176127,2.749644,4.071382,-7.427107,-2.060568,5.315214,-9.852790,-1.904468,7.497570,-9.986881,8.298747,-3.969829,-2.667228,4.906936,2.227812,-7.244967,-8.634037,-0.978659,-1.408426,-2.187586,7.599928,0.516797,-6.414216,-0.136138,9.354022,7.609110,3.616999,6.778919,6.326488,-2.867076,0.934806,9.961498,-6.145254,-7.384283], dtype = "float64")#candidate|12690|(1008,)|const|float64
call_12689 = relay.TupleGetItem(func_8004_call(relay.reshape(const_12690.astype('float64'), [2, 504]), relay.reshape(const_12690.astype('float64'), [2, 504]), ), 2)
call_12691 = relay.TupleGetItem(func_8008_call(relay.reshape(const_12690.astype('float64'), [2, 504]), relay.reshape(const_12690.astype('float64'), [2, 504]), ), 2)
func_8335_call = mod.get_global_var('func_8335')
func_8337_call = mutated_mod.get_global_var('func_8337')
call_12702 = relay.TupleGetItem(func_8335_call(), 0)
call_12703 = relay.TupleGetItem(func_8337_call(), 0)
uop_12715 = relay.cosh(call_12685.astype('float64')) # shape=(1, 7, 16)
uop_12717 = relay.cosh(call_12686.astype('float64')) # shape=(1, 7, 16)
func_9071_call = mod.get_global_var('func_9071')
func_9073_call = mutated_mod.get_global_var('func_9073')
call_12727 = relay.TupleGetItem(func_9071_call(), 0)
call_12728 = relay.TupleGetItem(func_9073_call(), 0)
uop_12732 = relay.log(uop_12715.astype('float32')) # shape=(1, 7, 16)
uop_12734 = relay.log(uop_12717.astype('float32')) # shape=(1, 7, 16)
output = relay.Tuple([call_12689,const_12690,call_12702,call_12727,uop_12732,])
output2 = relay.Tuple([call_12691,const_12690,call_12703,call_12728,uop_12734,])
func_12740 = relay.Function([], output)
mod['func_12740'] = func_12740
mod = relay.transform.InferType()(mod)
mutated_mod['func_12740'] = func_12740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12740_call = mutated_mod.get_global_var('func_12740')
call_12741 = func_12740_call()
output = call_12741
func_12742 = relay.Function([], output)
mutated_mod['func_12742'] = func_12742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7511_call = mod.get_global_var('func_7511')
func_7513_call = mutated_mod.get_global_var('func_7513')
call_12793 = relay.TupleGetItem(func_7511_call(), 0)
call_12794 = relay.TupleGetItem(func_7513_call(), 0)
func_4401_call = mod.get_global_var('func_4401')
func_4407_call = mutated_mod.get_global_var('func_4407')
const_12808 = relay.const([5,6,4,-3,-6,-1,-3,-3,7,8,-10,-6,6,1,7,-5,-2,10,6,6,-4,5,1,8,3,-1,6,7,-1,2,-6,8,-7,1,-2,9,5,5,-3,2,-8,-8,2,-10,6], dtype = "uint8")#candidate|12808|(45,)|const|uint8
const_12809 = relay.const([-10,8,-7,-3,10,-5,8,-9,-3,-5,-7,9,8,2,-3,4,10,-3,2,6,-9,-7,10,-8,-8,-6,-5,4,-4,7,-9,-1,4,-6,1,10,-2,7,-2,5,-7,5,-3,7,-5,-5,7,3,-9,10,4,9,5,-8,-10,-7,5,3,2,5,6,4,-7,7,-10,5,-6,-10,10,-8,-2,-1,10,4,4,1,-1,-5,4,6,10,-5,-6,7,-2,8,3,-10,-1,-5,8,-7,1,-9,6,6,-7,-2,6,8,-8,4,4,-4,-2,4,-5,9,4,10,1,8,8,10,-1,4,5,-1,-5,5,-6,-5,9,10,10,-5,-7,-1,-3,1,-9,3,6,-2,1,-6,8,9,-3,-3,8,-6,-1,1,9,-7,-10,10,-6,-5,-2,5,2,7,4,10,8,-8,6,10,-5,2,9,1,6,2,9,-8,-3,8,-5,-9,8,-1,-9,8,9,-9,-3,2,8,-7,-3,-10,2,-2,-10,-9,6,-3,-2,-9,2,-9,-10,-6,9,7,-2,6,7,-10,-7,-7,10,10,-2,5,8,-3,-7,7,4,-7,3,8,-9,8,7,3,-7,1,3,-5,10,-1,7,-4,-2,-5,4,6,4,-1,9,-10,8,-8,-7,-4,-1,7,-5,-6,2,3,-7,-9,-2,3,4,-10,5,5,-8,-1,6,-4,-9,-7,6,-8,8,3,10,1,-9,6,6,-6,-10,3,4,-6,-2,5,2,8,-3,-10,-10,6,-10,3,-6,10,5,4,3,-2,3,-10,1,7,-2,6,5,-1,-6,1,-3,-10,8,-6,3,5,-5,5,6,1,-6,-2,-9,-8,-7,-7,-1,9,-2,-10,4,3,4,-7,-9,-2,7,7,-7,1,5,-8,-6,6,3,2,-5,9,4,-2,8,9,-6,-1,1,-10,-1,-3,-5,-4,-8,10,-5,3,-8,-2,8,10,-8,-8,-3,7,9,1,-2,-6,5,-4,-4,-10,3,-7,-5,-5,-9,4,-3,6,-3,-8,3,-3,-8,9,-5,4,-2,9,9,-2,8,8,9,5,-2,4,7,-6,-8,8,-3,-1,5,-4,-3], dtype = "uint8")#candidate|12809|(405,)|const|uint8
const_12810 = relay.const([-2.964669,-1.319338,2.476416,-7.059325,2.554233,5.413649,-0.816476,-7.816289,6.880149,-4.417004,-6.744095,7.070633,-4.241369,1.073796,-2.415457,6.709263,-6.416596,8.208356,8.558484,-5.969894,-4.179143,-3.433610,-2.151733,2.600216,-3.061314,7.524762,-7.495700,6.581531,-2.307638,-1.394741,5.985666,-9.772530,0.546920,4.961296,2.067307,4.158675,0.591155,8.575948,5.657233,1.825955,-8.807063,-5.345534,9.430266,4.471585,2.447580,-2.919879,1.202416,-8.488172,7.186898,-6.352375,-1.289208,-9.901727,1.155612,4.149672,-0.693319,-5.111158,8.072739,1.458110,-2.638389,7.175523,-5.257401,-7.943245,-6.410088,6.208492,-3.072971,-7.215522,5.081748,5.726139,-0.534328,0.660299,1.973689,4.494078,9.650515,-4.108385,6.906204,1.768413,5.982447,-4.520081,-9.346902,5.732557,6.207308,9.761535,4.068580,4.418543,9.311432,-1.877861,-1.646205,-2.912118,3.162605,-2.330881,-2.571246,-7.285472,3.923608,8.142965,-6.315761,4.489046,-9.820561,5.669342,5.865511,-3.741002,8.640209,2.457248,-6.667869,0.378550,-1.508456,9.877844,4.868234,9.909359,-1.405102,5.160164,2.175913,-4.089017], dtype = "float32")#candidate|12810|(112,)|const|float32
const_12811 = relay.const([-1.697792,-8.980085,1.432608,0.099165,1.326279,2.051554,-7.893305,-6.488379,-7.830587,0.326015,-9.363644,-1.822307,3.092880,5.112429,-8.379160,8.659536,-7.319656,-4.364299,6.033116,-9.879595,7.850641,5.865066,-0.380870,6.714905,8.025503,7.484294,8.521967,4.123500,-1.096558,-9.276237,-4.816464,6.388906], dtype = "float64")#candidate|12811|(32,)|const|float64
call_12807 = relay.TupleGetItem(func_4401_call(relay.reshape(const_12808.astype('uint8'), [5, 9, 1]), relay.reshape(const_12809.astype('uint8'), [5, 9, 9]), relay.reshape(const_12810.astype('float32'), [112,]), relay.reshape(const_12811.astype('float64'), [4, 8]), relay.reshape(call_12793.astype('uint64'), [168, 2]), ), 1)
call_12812 = relay.TupleGetItem(func_4407_call(relay.reshape(const_12808.astype('uint8'), [5, 9, 1]), relay.reshape(const_12809.astype('uint8'), [5, 9, 9]), relay.reshape(const_12810.astype('float32'), [112,]), relay.reshape(const_12811.astype('float64'), [4, 8]), relay.reshape(call_12793.astype('uint64'), [168, 2]), ), 1)
output = relay.Tuple([call_12793,call_12807,const_12808,const_12809,const_12810,const_12811,])
output2 = relay.Tuple([call_12794,call_12812,const_12808,const_12809,const_12810,const_12811,])
func_12822 = relay.Function([], output)
mod['func_12822'] = func_12822
mod = relay.transform.InferType()(mod)
output = func_12822()
func_12823 = relay.Function([], output)
mutated_mod['func_12823'] = func_12823
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12824 = relay.const([[[8.163156,2.455644,6.120157,-2.261800,-8.557577,5.978295,2.839122]],[[-4.579341,-4.693394,-1.783465,9.393724,3.371195,-6.117246,1.318755]],[[-7.296545,-2.756995,3.708560,-0.618395,1.833463,3.316357,1.317764]],[[-6.908410,7.361031,-2.994265,9.757976,-8.833285,8.028578,-7.575277]],[[2.039065,-2.865814,-8.244436,8.030884,-9.941602,8.069206,3.449177]],[[-8.574578,8.807155,1.696646,6.922563,8.203384,-5.944612,0.940088]],[[3.044997,5.827375,2.823657,-2.434812,-2.078053,6.090918,2.274308]],[[-5.483213,8.284109,8.054401,-9.896850,2.301447,1.633189,-1.582996]],[[5.404269,7.941814,6.550248,0.715854,-8.486276,7.613982,7.671308]],[[-2.045820,0.843993,9.928281,9.504908,4.734361,6.862733,9.009875]],[[7.441802,-2.924723,4.151038,8.170555,8.836089,8.139813,-1.028152]],[[-3.373827,-4.691105,-8.047205,-4.082748,-2.719158,1.319177,6.112860]],[[3.324780,3.773994,-5.402650,4.256828,6.325432,-7.881065,7.127455]],[[1.127849,-9.374586,2.692153,-4.216438,-4.103577,-3.042479,-0.030580]],[[1.589124,-9.176829,-7.617099,7.743361,-3.381236,-2.082974,-3.886163]],[[-7.535453,-3.544804,7.922157,5.213779,7.266109,7.987597,-8.465005]]], dtype = "float32")#candidate|12824|(16, 1, 7)|const|float32
const_12825 = relay.const([[[-3.650830,7.021888,2.423520,9.556998,8.301004,1.866031,9.467169],[0.576603,4.653617,-2.509103,9.621300,-3.219033,-5.691651,-8.179856],[0.232926,-8.295158,-8.619372,-1.916459,-7.931967,0.438794,7.214538],[6.300741,-9.205172,2.126585,-4.774635,-9.525832,5.404663,-0.954315],[-7.361858,6.506210,-9.988050,5.182643,2.342829,-1.851664,-1.904952],[3.389843,-3.842745,-2.402730,1.867631,4.764813,9.383074,-7.427095],[-2.917718,-3.747711,4.810621,4.028867,7.707855,-9.137064,-7.555456],[5.888557,-0.838713,6.133500,7.121088,9.652539,8.347675,-4.265845],[3.204247,0.397823,4.042915,-2.172083,-4.839924,-9.193591,-3.881477]],[[-3.938011,3.263513,9.003871,0.382475,2.410572,-0.870894,7.982891],[3.446594,8.670199,-0.183467,-0.593346,-6.861199,1.022069,-2.351659],[6.978367,-9.603608,-9.005968,7.276726,-4.820111,-0.086663,9.116231],[-7.907280,-1.571390,1.870793,-0.178527,-5.182758,7.687607,8.839561],[8.655254,7.065726,9.190576,7.321386,2.052844,8.869735,6.473608],[7.103661,8.741704,9.209280,6.812734,1.427465,9.840071,5.856305],[-5.521785,5.097463,-9.234494,-2.117577,-4.287355,2.309303,-8.354192],[5.479961,-2.831308,9.060006,2.063467,8.113215,5.327709,-2.998886],[9.609975,0.576856,8.348986,8.215153,4.331079,0.457667,0.399196]],[[-4.168676,2.728280,9.702333,-4.611042,5.187150,-8.035018,6.764752],[2.206216,-7.574638,2.412465,0.473609,-4.286789,-7.638983,-2.899682],[9.120087,5.020556,-2.525488,-1.672132,-3.664950,-4.861889,-0.356298],[1.937605,-3.816288,2.559017,8.376121,-4.018269,5.548416,5.782032],[5.492933,4.824690,-0.682527,-6.773471,-5.474765,-7.905031,0.456135],[-5.908516,1.795212,2.939648,9.893623,-1.371279,7.249261,4.555302],[5.547284,0.403628,-3.777927,-1.399978,9.277726,8.256747,9.376437],[-0.999619,-4.641678,-0.296122,-6.905909,3.635428,-2.362534,-9.758626],[0.961374,1.878420,4.864053,9.869175,1.376465,-9.882012,-2.530577]],[[-8.072613,0.287522,-2.988180,-2.539779,-0.466937,9.169092,-7.151448],[5.256641,9.872726,-6.881072,-4.478197,0.919396,2.661792,8.298002],[8.371706,-2.523510,8.648956,0.839386,7.858156,-4.947476,-9.241978],[-6.885361,9.872882,-0.935340,-0.683080,4.847411,-1.727662,-9.152937],[-4.673712,3.962843,4.348378,4.693129,1.360475,-5.942858,-5.005171],[-7.885799,-3.634589,9.339200,8.468655,7.037588,-4.559096,-2.985704],[7.107551,2.121644,-6.593236,-8.541012,-4.355355,-5.031493,-5.343615],[-4.842422,5.719087,5.968364,4.925801,1.273872,-6.161590,-5.210395],[-9.833661,6.802319,3.161796,8.242599,0.639943,0.049549,7.420283]],[[-9.766783,4.902991,8.557292,5.905531,-7.054295,4.510230,6.853788],[-4.503935,0.368154,-8.293833,4.016060,4.061872,3.817251,-7.616619],[-2.615277,-7.583274,7.752873,2.675680,-9.449898,0.260233,-8.505937],[8.375890,5.406896,1.585107,-1.318110,3.981774,-4.895646,-7.380550],[-6.096169,-4.548017,-6.938132,0.340377,-0.729657,-7.494574,1.568890],[-0.302684,2.708443,-2.164388,5.625997,2.469672,0.046908,6.755659],[3.898552,-7.054478,-6.836305,-9.182798,3.563970,-7.095694,-9.220376],[7.291284,9.239663,0.075638,4.172362,7.341461,-2.202095,-6.072613],[5.627785,3.806725,1.128500,-8.349272,-2.082452,-2.566551,-4.963552]],[[-2.713588,-5.393733,2.311506,9.260233,-7.235119,-3.318244,2.273089],[-9.887332,-4.456029,-7.864621,-9.292590,7.310559,8.284204,7.337152],[-6.022029,5.880266,-5.542901,-0.383745,4.992375,9.277542,-1.175736],[9.837087,-3.683697,2.796563,3.471661,-6.132889,5.134878,0.693480],[4.573194,-2.603254,-4.200599,-5.703015,2.077350,-6.811799,-2.205797],[-3.243857,1.649801,6.049671,1.930964,7.305412,-4.886938,-2.262356],[1.443548,-3.889824,-3.625351,-4.273819,-0.084466,-4.708615,1.804631],[-5.528055,-7.769936,-5.121209,-6.391195,1.045264,-4.248835,4.589066],[-8.268455,-5.346542,2.077723,-9.645598,-4.951023,-5.618000,-6.724634]],[[-2.825744,-8.614942,2.730895,-9.191396,-4.584912,9.617923,-2.353007],[-3.377889,-1.606357,-7.267495,8.793186,-8.708652,0.081963,-8.586626],[9.140042,-6.378619,4.409602,3.833674,3.280379,-1.232465,-0.644689],[9.730670,-0.147798,-6.709747,-5.832050,5.837429,-1.345180,-6.657318],[-8.087093,-1.440572,7.753179,-9.590884,0.223667,5.311680,5.825145],[-0.654444,-9.401543,-3.776232,-6.762267,3.507930,9.742711,-8.914213],[-2.688859,-2.407982,1.624803,7.945248,8.235016,1.973926,8.239248],[-3.466660,4.380827,-9.192220,-0.643945,-8.341420,-6.945996,-6.406560],[-9.677680,8.950609,1.970968,-1.769887,-2.748025,6.405602,8.458503]],[[-4.931847,8.520153,8.245101,-7.631327,-8.966704,-1.942760,6.308393],[3.781558,8.421817,-9.386774,-7.135463,-1.582876,-5.354854,-4.965267],[-1.645607,2.822782,-9.227577,7.439551,7.373985,-4.067267,5.496906],[-3.097081,3.595882,-9.700424,0.698889,5.655082,-9.580071,-4.523078],[7.459908,-9.882259,-9.547989,-1.456522,-8.460081,-8.205802,2.065434],[-2.464209,-0.078051,9.955318,-3.575540,-3.935589,-9.135550,7.147561],[3.754031,-0.672505,6.852656,-8.453567,-6.558861,-2.466400,6.748502],[-5.861944,6.643417,4.420078,9.382250,0.805265,-8.446832,2.497504],[-5.700700,6.749218,9.081897,-3.393508,-0.204469,-4.246607,8.806369]],[[8.941537,-0.788706,-4.103280,-2.069400,4.895085,-5.216123,7.262947],[-7.573000,-8.462260,-4.659509,-4.555940,1.103260,-4.610595,9.866613],[-0.148372,9.179179,0.831216,7.810821,-8.509998,1.326683,2.876152],[-0.480708,-3.241250,0.509448,7.483899,-3.224755,5.996848,-4.697881],[7.135010,8.615410,4.851219,-6.582547,-6.704303,-6.622329,3.581645],[-9.289272,0.692946,-6.836831,9.153519,-7.398766,9.340311,-8.248081],[-4.490048,-0.973619,-7.319409,1.943905,-8.239757,9.689697,8.931550],[0.382835,0.951424,4.451645,6.016571,9.423910,-0.574050,8.784211],[-2.092147,-1.974569,6.246046,1.898698,-6.311250,1.141112,-9.760828]],[[5.337455,-7.896775,-2.601056,-4.737564,-2.872254,0.485894,-0.808423],[-1.234768,3.101485,4.711547,3.236140,-2.360914,2.546628,-3.759629],[-4.003274,4.215242,-4.698972,-8.617722,3.775361,9.090030,-5.345528],[9.442032,-5.459586,5.018882,5.957536,2.287148,2.717855,6.564922],[8.900116,5.086548,-1.580298,2.959941,-3.773156,9.517557,3.505880],[6.011462,-6.731741,-7.485137,-2.526715,-8.549490,2.255811,0.891475],[-5.516882,6.715137,-5.052583,4.012911,9.739796,4.556638,-1.575084],[2.092868,8.076585,-3.851854,-6.630852,-3.435701,-6.250049,-2.560712],[2.153019,-8.251377,-0.287845,1.051772,-7.960059,8.469219,4.429234]],[[4.226729,4.796775,8.171889,7.137299,-1.194505,2.366562,2.052293],[-6.739939,1.577019,4.781986,1.199141,4.013340,-2.227356,2.430336],[5.970314,-8.326876,-2.539521,4.357420,8.666594,3.456353,-4.384260],[-5.099803,-0.471542,1.944336,-3.433938,9.936539,-2.027742,-8.704445],[-3.509173,-5.538908,4.091584,-7.451278,6.517479,3.888588,0.864332],[-4.475854,1.356189,4.574826,7.143475,2.883990,4.757591,6.109917],[6.719549,-6.972593,4.566932,8.163789,3.725471,4.974770,-1.905651],[8.700819,0.627758,9.485294,9.778464,1.115605,-7.127844,-9.925972],[1.898595,2.163419,-2.908374,1.747419,1.537422,-3.400710,-5.912613]],[[2.422504,-4.881598,-2.114204,-0.267220,8.995042,-3.927401,8.452184],[4.889103,-9.064836,7.180598,-1.984980,5.473658,-5.719830,-9.009973],[-8.971973,-3.276253,5.170057,-7.948969,-4.838964,-7.020031,-9.695274],[-1.978481,4.293067,-8.147937,4.038507,1.030108,8.520443,2.502948],[5.533099,-0.569050,-7.770278,2.536266,1.960684,-2.411378,2.663379],[4.470799,2.109564,6.287044,-5.826208,2.181910,8.297368,4.601523],[6.582716,-6.491840,-6.853467,-6.833394,4.702623,1.238088,-6.304205],[7.879447,-4.001763,4.926866,-3.161493,-0.111222,-7.924492,-7.564195],[-4.896833,-2.163903,-1.889008,9.074741,0.524689,-9.384473,7.021061]],[[-8.099381,0.135670,1.279163,-0.164348,6.445472,0.515457,5.385863],[6.712759,-7.330980,2.174311,-6.724244,0.897055,1.029043,2.706722],[-8.897560,9.312019,-1.420403,-1.888354,-7.640388,1.637642,7.294894],[4.838998,-2.724317,5.542075,-3.000139,-9.785259,-6.716161,-5.654128],[-6.716144,3.928985,8.838961,2.427344,5.087343,8.705586,0.612207],[-9.609318,-9.309069,3.684430,-8.609949,1.681540,-1.927409,3.544677],[0.726908,-0.221899,-8.069738,-3.722160,-2.500573,1.640711,9.824690],[0.120951,4.493921,-6.011588,2.717851,0.437179,-7.892398,-0.872881],[-0.642482,7.960399,-6.327293,7.308809,-3.646794,-2.901815,-3.422377]],[[-0.155111,-0.321388,-5.325931,4.649244,6.800607,-4.551157,6.365201],[6.203494,6.795680,1.232894,-0.682642,-5.175768,-0.091504,1.886720],[8.638313,7.045087,-4.741404,1.141841,1.932755,8.295798,9.747764],[7.455310,-8.114235,2.331171,-7.879122,-9.626021,-8.627330,7.354780],[3.751169,2.323040,-4.825011,9.553574,-5.148046,2.449009,7.465813],[8.442715,-1.400330,1.622454,9.301635,6.180393,-9.029453,-9.956569],[-5.511589,4.499120,6.393241,4.255532,9.497988,-1.256649,2.148598],[-0.231728,-4.333641,-3.931055,-3.890851,8.340680,-8.904870,-8.543160],[-6.516127,3.592093,-0.171598,6.913303,9.736196,4.097806,2.327118]],[[-2.638796,5.169220,1.161948,-1.436705,-9.354097,-5.154782,8.492834],[-0.563302,7.432852,-3.116944,-1.146275,6.070053,-9.489663,-5.218408],[-6.899649,2.213261,-7.715256,4.627614,-3.198570,1.784146,-7.031076],[-1.631553,-6.258623,2.299507,-8.972442,-7.512183,-6.029071,-8.429955],[-3.386398,-4.643321,-9.505750,-8.594036,-4.665501,-1.408935,9.492556],[-3.397360,2.494952,3.229823,8.435846,2.026855,6.698714,-5.879056],[-1.060275,-8.620523,5.669686,7.766115,6.544200,9.501449,4.120100],[-4.688885,7.486287,-3.482558,-0.391508,0.450493,5.287809,8.109578],[-3.043521,-8.197912,-5.793750,-4.961925,-4.062419,9.569886,4.675237]],[[4.758841,-3.273448,2.189864,-9.341119,2.078530,-4.747535,5.432396],[3.879811,-0.962663,-6.786945,-4.341310,2.266079,1.599579,-3.820303],[6.942205,1.433227,-8.604429,6.636589,4.254219,-6.579464,-3.897931],[4.519187,-6.319858,-9.365115,8.977868,2.491134,6.276068,-7.792361],[-1.532916,1.280062,-3.006356,1.400425,-2.841141,-2.184474,-9.215036],[-8.565692,4.471231,-4.883556,2.190356,-7.158742,-4.278978,-8.207819],[3.348871,-0.997941,-4.584289,2.425716,-8.573655,3.723083,8.149433],[-9.761526,-9.091285,-3.235713,5.520138,3.492342,8.387419,4.686066],[-5.684050,5.606861,-3.402088,3.910554,4.645673,4.382734,1.341378]]], dtype = "float32")#candidate|12825|(16, 9, 7)|const|float32
bop_12826 = relay.maximum(const_12824.astype('float32'), const_12825.astype('float32')) # shape=(16, 9, 7)
func_8826_call = mod.get_global_var('func_8826')
func_8827_call = mutated_mod.get_global_var('func_8827')
call_12835 = relay.TupleGetItem(func_8826_call(), 0)
call_12836 = relay.TupleGetItem(func_8827_call(), 0)
func_12594_call = mod.get_global_var('func_12594')
func_12596_call = mutated_mod.get_global_var('func_12596')
call_12843 = func_12594_call()
call_12844 = func_12594_call()
output = relay.Tuple([bop_12826,call_12835,call_12843,])
output2 = relay.Tuple([bop_12826,call_12836,call_12844,])
func_12848 = relay.Function([], output)
mod['func_12848'] = func_12848
mod = relay.transform.InferType()(mod)
output = func_12848()
func_12849 = relay.Function([], output)
mutated_mod['func_12849'] = func_12849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9412_call = mod.get_global_var('func_9412')
func_9413_call = mutated_mod.get_global_var('func_9413')
call_12912 = relay.TupleGetItem(func_9412_call(), 0)
call_12913 = relay.TupleGetItem(func_9413_call(), 0)
func_10853_call = mod.get_global_var('func_10853')
func_10855_call = mutated_mod.get_global_var('func_10855')
call_12918 = relay.TupleGetItem(func_10853_call(), 1)
call_12919 = relay.TupleGetItem(func_10855_call(), 1)
output = relay.Tuple([call_12912,call_12918,])
output2 = relay.Tuple([call_12913,call_12919,])
func_12925 = relay.Function([], output)
mod['func_12925'] = func_12925
mod = relay.transform.InferType()(mod)
output = func_12925()
func_12926 = relay.Function([], output)
mutated_mod['func_12926'] = func_12926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4204_call = mod.get_global_var('func_4204')
func_4205_call = mutated_mod.get_global_var('func_4205')
call_13055 = relay.TupleGetItem(func_4204_call(), 0)
call_13056 = relay.TupleGetItem(func_4205_call(), 0)
const_13073 = relay.const([[[9.491531,1.946878,-7.551158,-6.700875,4.300900,0.467113,-2.323259,-7.971438,4.407707,0.101849,4.215874,8.621779,6.397353,8.329087,-8.829384,-8.102763],[-9.382695,8.875553,7.298397,7.303372,-8.376093,-1.396192,-6.213503,-3.261235,-0.771820,5.738609,-2.661025,1.957678,-4.969174,6.520261,3.985842,-5.907386],[2.730279,-5.478137,-3.469992,9.124399,-2.710336,4.324554,1.195425,-0.263522,1.355706,9.628700,-9.309995,-1.518119,-6.630323,4.925109,7.507421,4.187022],[8.546599,4.845031,9.642628,-5.689614,-2.715456,3.874051,9.063352,-7.642492,6.999493,1.506101,-3.530249,-2.013375,6.857928,-4.298069,-1.582644,5.031830],[3.248174,6.866113,-0.068206,-6.820764,6.270887,-1.281221,3.166192,-8.049503,-5.740409,-9.489661,2.964883,0.111135,-9.504692,0.751082,4.876830,-9.114545],[-1.932475,-6.386445,1.274762,8.460025,-8.615181,-0.216563,-2.903322,-1.510026,-9.353098,2.396790,-5.833495,-2.165928,-5.767179,3.661967,-3.645644,-1.206021],[8.118912,1.518729,3.203587,2.961975,-0.682133,8.524539,-0.182433,-1.045334,-6.180740,-7.320493,-9.373305,9.914254,9.066206,7.466010,-4.544716,-0.758563]],[[-6.593961,1.569502,-9.427033,0.380319,-9.710556,-2.887055,-6.698746,2.354525,-9.851732,9.131600,-5.401783,-1.859974,5.764428,6.597952,5.210534,1.680565],[-1.570239,-7.524832,-9.880659,9.229902,-2.263148,2.117046,-2.878236,-5.206452,7.155541,-3.550886,-7.547146,7.811918,-1.066646,-7.905504,-7.322052,3.760726],[-3.879323,1.463984,8.344142,1.093374,-6.216262,-5.516395,6.129626,-3.059983,1.863662,-1.639299,7.063890,6.281849,-7.898161,1.893846,-5.880092,3.195555],[-3.898971,9.884931,-8.277813,-7.224372,3.848216,1.647499,2.351593,5.485755,-2.021804,-2.154278,6.091104,1.539575,9.673274,-0.150065,0.445464,-7.138023],[5.182334,2.419922,-7.173540,-4.415335,8.012136,-1.370402,8.427546,8.803793,2.845546,4.059816,4.495195,8.607294,-5.409507,-7.163439,1.816573,7.089012],[-2.891749,-4.947493,-1.694680,1.679933,2.104973,-2.491686,2.759759,-3.958142,-9.333278,-9.367175,1.388915,-8.511400,7.394558,2.255661,-2.181338,8.792487],[-1.334260,1.279906,8.802566,-7.609201,1.163632,9.192305,-8.204938,6.772827,-9.278865,-6.957214,4.690195,8.821855,-3.391803,-3.344756,1.127585,6.481715]],[[2.662541,6.494795,3.701682,5.327831,-9.347004,-0.652842,0.541558,1.042139,9.803189,6.647964,6.768860,0.234478,5.841141,-1.307658,-8.084080,-3.343960],[-4.036830,-4.184239,0.709218,-1.138291,-7.813011,-1.864354,3.779817,0.927687,-0.136161,6.050383,5.630143,1.176170,-3.202947,-8.143305,2.534350,1.968902],[-3.451459,-4.358931,0.808560,7.291692,7.977332,4.824984,-8.930623,3.355179,3.699986,-9.787091,6.411920,-7.892598,2.062485,-4.045341,8.691525,-4.784427],[8.978043,-9.715096,-7.435465,9.340991,6.618418,-8.022313,3.698915,-7.090096,-7.872108,-0.113819,-2.946399,-9.316428,2.766913,9.062418,-0.258611,-0.973032],[-2.576519,-8.688861,-9.776421,-0.395572,4.607525,2.810227,-6.553096,7.091673,-0.007255,-7.982205,-8.022290,-9.391262,-8.707356,6.274638,-2.737020,-1.664777],[-1.156263,1.534216,-6.220330,-5.649193,-0.388120,6.285100,-3.904933,1.391838,-2.230719,4.492191,-1.349486,-5.363706,7.504444,6.395411,1.857366,-2.972584],[6.932636,-5.277531,6.242674,2.144554,7.254182,-0.916220,5.200200,-0.628661,-7.331390,8.040280,-1.163071,2.133721,4.358067,4.989930,-7.930854,-7.255090]],[[7.807432,-8.101033,9.034738,-5.150640,-2.882913,-7.658128,-9.279853,3.706162,8.591526,-8.608358,-4.701128,7.878913,-9.368259,-8.194772,6.778658,-8.257412],[0.708887,1.957365,-5.673631,6.893682,4.890844,7.531291,9.695077,-5.379835,4.635547,-9.387787,-6.514755,3.376810,-6.898077,7.037871,-6.627911,-1.816125],[-5.684998,-6.487803,9.594872,0.641687,-1.434703,-3.349049,7.552058,-2.747942,5.908405,-6.716508,-1.056130,8.124928,7.977068,-5.728151,-7.206719,-6.257333],[2.206605,-5.518813,-4.369690,3.698024,-7.539723,-3.825885,-5.027622,-7.649058,0.982054,9.629453,-2.012223,-2.306033,6.698905,8.771481,9.071486,8.816038],[-5.101843,3.332256,2.446873,0.782809,2.533913,-9.659946,-5.859130,0.574740,7.397719,-6.217316,5.954118,-6.617094,8.855128,7.627306,0.442688,4.937740],[-0.809217,-3.878898,6.694164,1.823228,-7.370641,-7.925487,-6.046628,-9.580100,-7.057917,3.858912,-7.209914,0.926213,5.702756,-6.172500,7.045504,-4.962661],[2.637526,1.117694,5.728948,4.105921,-6.202276,-8.958324,4.434826,8.824963,6.395654,-7.438253,-0.846055,-1.526940,-8.680416,-8.034558,-5.078122,5.105710]],[[2.285980,2.575067,4.752520,-6.093801,-4.257420,-1.561268,-4.018980,-3.096425,-9.984301,9.428196,-8.701844,-9.734706,-8.479882,-3.188882,8.619687,-1.465325],[-0.801782,2.338916,-2.506350,-8.876822,1.335762,2.971169,-9.366579,4.239740,-4.002384,5.944899,-3.427632,8.692465,-3.707461,-9.383487,3.536030,-9.041617],[-9.577318,6.912891,-6.601133,6.715168,-8.183987,5.813224,-1.955346,3.084069,2.773372,7.964447,-4.598053,-0.771610,-2.024676,-9.749388,-8.018577,-4.804444],[3.699317,0.623037,3.962619,6.405946,1.548363,-8.153633,8.158191,-7.399514,-1.489314,6.347277,-3.879468,1.160872,-3.567032,-8.044652,-0.138320,5.709339],[-4.648096,4.421054,2.578274,3.952983,0.841718,0.853114,7.812707,6.474681,5.645135,-0.805503,6.505120,9.363053,-9.132927,-7.680445,-5.439722,-2.380692],[-6.308128,-3.519116,-5.597963,2.944956,1.910562,-4.634871,-8.672810,-9.207147,-1.953943,-1.940095,-6.733655,4.756422,4.149607,4.731070,8.137919,5.240802],[-7.751345,-5.346784,7.206564,-8.623124,-3.061691,-1.872497,5.945081,-1.955904,5.755390,1.925885,-8.514233,-6.823831,-7.065680,7.835078,5.643410,1.111945]]], dtype = "float32")#candidate|13073|(5, 7, 16)|const|float32
bop_13074 = relay.right_shift(call_13055.astype('uint16'), const_13073.astype('uint16')) # shape=(5, 7, 16)
bop_13077 = relay.right_shift(call_13056.astype('uint16'), const_13073.astype('uint16')) # shape=(5, 7, 16)
output = relay.Tuple([bop_13074,])
output2 = relay.Tuple([bop_13077,])
func_13079 = relay.Function([], output)
mod['func_13079'] = func_13079
mod = relay.transform.InferType()(mod)
output = func_13079()
func_13080 = relay.Function([], output)
mutated_mod['func_13080'] = func_13080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11744_call = mod.get_global_var('func_11744')
func_11746_call = mutated_mod.get_global_var('func_11746')
call_13098 = relay.TupleGetItem(func_11744_call(), 0)
call_13099 = relay.TupleGetItem(func_11746_call(), 0)
output = call_13098
output2 = call_13099
func_13101 = relay.Function([], output)
mod['func_13101'] = func_13101
mod = relay.transform.InferType()(mod)
mutated_mod['func_13101'] = func_13101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13101_call = mutated_mod.get_global_var('func_13101')
call_13102 = func_13101_call()
output = call_13102
func_13103 = relay.Function([], output)
mutated_mod['func_13103'] = func_13103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6765_call = mod.get_global_var('func_6765')
func_6766_call = mutated_mod.get_global_var('func_6766')
call_13153 = relay.TupleGetItem(func_6765_call(), 0)
call_13154 = relay.TupleGetItem(func_6766_call(), 0)
func_10123_call = mod.get_global_var('func_10123')
func_10125_call = mutated_mod.get_global_var('func_10125')
const_13161 = relay.const([False,True,False,True,False,False,False,False,True,False,False,True,False,False,False,False,True,True,True,True,False,True,False,False,False,False,False,True,False,False,False,False,True,False,True,False,True,True,False,False,True,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,True,False,True,True,False,True,True,False,False,False,False,True,True,False,True,True], dtype = "bool")#candidate|13161|(72,)|const|bool
call_13160 = relay.TupleGetItem(func_10123_call(relay.reshape(const_13161.astype('bool'), [72,])), 3)
call_13162 = relay.TupleGetItem(func_10125_call(relay.reshape(const_13161.astype('bool'), [72,])), 3)
output = relay.Tuple([call_13153,call_13160,const_13161,])
output2 = relay.Tuple([call_13154,call_13162,const_13161,])
func_13164 = relay.Function([], output)
mod['func_13164'] = func_13164
mod = relay.transform.InferType()(mod)
mutated_mod['func_13164'] = func_13164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13164_call = mutated_mod.get_global_var('func_13164')
call_13165 = func_13164_call()
output = call_13165
func_13166 = relay.Function([], output)
mutated_mod['func_13166'] = func_13166
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13255 = relay.var("var_13255", dtype = "int64", shape = ())#candidate|13255|()|var|int64
var_13256 = relay.var("var_13256", dtype = "int64", shape = (15, 8, 13))#candidate|13256|(15, 8, 13)|var|int64
bop_13257 = relay.maximum(var_13255.astype('int64'), var_13256.astype('int64')) # shape=(15, 8, 13)
func_9713_call = mod.get_global_var('func_9713')
func_9714_call = mutated_mod.get_global_var('func_9714')
call_13262 = relay.TupleGetItem(func_9713_call(), 0)
call_13263 = relay.TupleGetItem(func_9714_call(), 0)
func_9173_call = mod.get_global_var('func_9173')
func_9175_call = mutated_mod.get_global_var('func_9175')
call_13264 = func_9173_call()
call_13265 = func_9173_call()
func_6057_call = mod.get_global_var('func_6057')
func_6058_call = mutated_mod.get_global_var('func_6058')
call_13270 = relay.TupleGetItem(func_6057_call(), 0)
call_13271 = relay.TupleGetItem(func_6058_call(), 0)
bop_13297 = relay.logical_or(var_13256.astype('bool'), var_13255.astype('bool')) # shape=(15, 8, 13)
func_5119_call = mod.get_global_var('func_5119')
func_5121_call = mutated_mod.get_global_var('func_5121')
call_13329 = func_5119_call()
call_13330 = func_5119_call()
func_8770_call = mod.get_global_var('func_8770')
func_8772_call = mutated_mod.get_global_var('func_8772')
call_13331 = relay.TupleGetItem(func_8770_call(), 2)
call_13332 = relay.TupleGetItem(func_8772_call(), 2)
output = relay.Tuple([bop_13257,call_13262,call_13264,call_13270,bop_13297,call_13329,call_13331,])
output2 = relay.Tuple([bop_13257,call_13263,call_13265,call_13271,bop_13297,call_13330,call_13332,])
func_13333 = relay.Function([var_13255,var_13256,], output)
mod['func_13333'] = func_13333
mod = relay.transform.InferType()(mod)
var_13334 = relay.var("var_13334", dtype = "int64", shape = ())#candidate|13334|()|var|int64
var_13335 = relay.var("var_13335", dtype = "int64", shape = (15, 8, 13))#candidate|13335|(15, 8, 13)|var|int64
output = func_13333(var_13334,var_13335,)
func_13336 = relay.Function([var_13334,var_13335,], output)
mutated_mod['func_13336'] = func_13336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12822_call = mod.get_global_var('func_12822')
func_12823_call = mutated_mod.get_global_var('func_12823')
call_13338 = relay.TupleGetItem(func_12822_call(), 3)
call_13339 = relay.TupleGetItem(func_12823_call(), 3)
func_168_call = mod.get_global_var('func_168')
func_172_call = mutated_mod.get_global_var('func_172')
const_13345 = relay.const([-8,-9,-6,5,7,1,-7,5,5,6,-7,-7,-4,8,-10,-10,-2,1,4,-8,-1,4,-9,-6,9,6,-7,-10,-1,3,-7,-2,-3,-5,-9,7,3,-10,4,-7,-9,9,-8,-7,7,-2,2,-3,7,2,-2,7,-4,-8,-4,9,7,-1,9,4,9,-10,10,-6,1,4,-8,-9,-2,9,1,9,-8,-3,-8,2,-2,8,6,-10,3,2,-7,-2,-7,4,2,4,-6,6,-5,-3,3,-9,-7,-7,5,2,10,10,6,3,-9,-10,7,1,6,-9,5,-9,-8,-3,-10,4,10,7,-2,-3,-1,-8,-9,-10,-2,6,-8,-2,-5,-1,1,-5,1,-6,-4,4,4,-6,10,9,-5,-1,-2,-1,-9,10,-8,-10,6,-2,5,-8,1,-1,9,4,7,-9,8,5,-2,7,9,9,-1,10,10,-6,-3,1,-9,8,-10,-4,-6,-8,-6,-8,-2,4,9,-3,1,9,6,-6,7,-10,10,7,-5,-4,-10,7,9,-7,-3,-9,-8,8,10,-1,-9,-4,-7,5,-6,2,-1,-5,-8,1,3,-8,8,-6,-2,-7,-8,-2,-2,8,7,-3,8,-3,2,-10,3,5,5,-2,-10,2,10,4,2,-1,1,1,1,8,7,-8,9,2,7,-3,-10,7,-10,5,3,2,9,-3,-9,-4,2,-5,-5,5,8,1,4,2,-6,-5,-3,3,2,2,1,-6,-6,-2,-7,-5,6,6,1,-1,5,8,-2,-9,8,-6,7,-10,4,-6,-10,7,-8,-3,1,7,-9,-3,7,5,-5,-4,2,5,-7,-6,-3,-2,-6,-1,-10,-2,-5,-2,-10,8,10,6,-6,-8,4,-2,9,-10,-1,-1,-9,-2,9,-7,-2,4,6,4,3,-7,-7,5,-2,-10,-6,-6,3,9,3,-1,-10,-9,-7,10,-6,-8,-3,9,-8,10,10,-8,5,5,3,5,2,-2,6,8,7,2,-9,-7,10,2,5,-2,-9,-10,-4,-8,8,3,9,3,9,8,-8,6,4,9,2,-2,8,-3,-7,-9,10,7,5,-5,-7,2,-10,5,-10,5,-6,3,9,8,-9,-10,-9,8,7,10,-8,1,-5,-4,-1,-7,10,-2,-5,4,7,3,-1,4,4,-3,-6,-2,1,6,-7,-2,10,-5,-6,1,4,-1,-4,-6,7,-5,-4,-6,3,8,4,8,-3,10,-5,-5,4,-8,1,1,3,-2,10,-1,-1,-6,10,8,-10,-5,9,6,5,6,-7,-3,10,5,-5,-5,-9,1,9,-5,10,-4,9,6,5,8,-6,10,8,6,-6,-2,-5,4,-6,1,-8,-7,-8,-1,-5,-2,-1,7,-2,7,-7,4,-3,6,-9,5,3,-4,-5,3,-5,-2,-9,-10,-5,10,-5,4,3,5,-8,-9,2,-1,10,8,-8,6,1,-10,-10,-8,7,2,3,-3,-8,3,8,1,-7,7,-1,-7,-8,9,-9,4,-1,5,-4,7,1,-5,6,-8,5,2,-8,-8,-6,-4,-6,-9,5,-2,-10,-4,-1,-9,5,1,3,-7,10,7,2,9,10,-4,-1,5,-7,2,7,6,9,1,-9,-2,4,7,1,-4,5,7,6,5,2,-3,9,9,5,9,-8,4,-10,-10,8,-3,3,7,3,-5,1,2,-5,9,2,-5,1,-4,2,-4,-7,-1,7,2,-4,-5,-2,5,9,-9,-2,-5,4,3,-3,-6,6,-1,-9,-4,-7,-6,-7,8,4,9,2,8,3,-3,10,7,9,10,-8,-1,-3,-5,9,-6,-1,-9,-9,10,-10,-10,-4,-8,-2,1,3,6,10,-4,-7,9,5,2,7,-10,4,-1,5,-1,8,-9,-5,-6,-8,-3,-3,2,2,-4,5,10,-1,10,-10,5,5,10,-8,-7,9,1,4,-1,-7,-7,-8,4,6,7,4,-4,5,1,2,-2,-9,4,6,10,-10,-6,2,8,-1,-5,-7,6,-5,-5,-8,-10,10,10,1,9,-7,-2,4,-8,-6,-2,2,-7,6,5,-9,-10,-3,4,10,-7,-8,-5,-2,-9,-8,3,2,8,-2,-3,8,-9,-4,6], dtype = "uint16")#candidate|13345|(784,)|const|uint16
var_13346 = relay.var("var_13346", dtype = "int64", shape = (588,))#candidate|13346|(588,)|var|int64
call_13344 = relay.TupleGetItem(func_168_call(relay.reshape(const_13345.astype('uint16'), [8, 7, 14]), relay.reshape(var_13346.astype('int64'), [588,]), ), 0)
call_13347 = relay.TupleGetItem(func_172_call(relay.reshape(const_13345.astype('uint16'), [8, 7, 14]), relay.reshape(var_13346.astype('int64'), [588,]), ), 0)
output = relay.Tuple([call_13338,call_13344,const_13345,var_13346,])
output2 = relay.Tuple([call_13339,call_13347,const_13345,var_13346,])
func_13350 = relay.Function([var_13346,], output)
mod['func_13350'] = func_13350
mod = relay.transform.InferType()(mod)
var_13351 = relay.var("var_13351", dtype = "int64", shape = (588,))#candidate|13351|(588,)|var|int64
output = func_13350(var_13351)
func_13352 = relay.Function([var_13351], output)
mutated_mod['func_13352'] = func_13352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7511_call = mod.get_global_var('func_7511')
func_7513_call = mutated_mod.get_global_var('func_7513')
call_13496 = relay.TupleGetItem(func_7511_call(), 0)
call_13497 = relay.TupleGetItem(func_7513_call(), 0)
func_10955_call = mod.get_global_var('func_10955')
func_10957_call = mutated_mod.get_global_var('func_10957')
call_13504 = func_10955_call()
call_13505 = func_10955_call()
output = relay.Tuple([call_13496,call_13504,])
output2 = relay.Tuple([call_13497,call_13505,])
func_13506 = relay.Function([], output)
mod['func_13506'] = func_13506
mod = relay.transform.InferType()(mod)
output = func_13506()
func_13507 = relay.Function([], output)
mutated_mod['func_13507'] = func_13507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3955_call = mod.get_global_var('func_3955')
func_3957_call = mutated_mod.get_global_var('func_3957')
call_13575 = relay.TupleGetItem(func_3955_call(), 0)
call_13576 = relay.TupleGetItem(func_3957_call(), 0)
output = relay.Tuple([call_13575,])
output2 = relay.Tuple([call_13576,])
func_13581 = relay.Function([], output)
mod['func_13581'] = func_13581
mod = relay.transform.InferType()(mod)
output = func_13581()
func_13582 = relay.Function([], output)
mutated_mod['func_13582'] = func_13582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9790_call = mod.get_global_var('func_9790')
func_9792_call = mutated_mod.get_global_var('func_9792')
call_13589 = func_9790_call()
call_13590 = func_9790_call()
output = relay.Tuple([call_13589,])
output2 = relay.Tuple([call_13590,])
func_13597 = relay.Function([], output)
mod['func_13597'] = func_13597
mod = relay.transform.InferType()(mod)
output = func_13597()
func_13598 = relay.Function([], output)
mutated_mod['func_13598'] = func_13598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7053_call = mod.get_global_var('func_7053')
func_7054_call = mutated_mod.get_global_var('func_7054')
call_13632 = relay.TupleGetItem(func_7053_call(), 5)
call_13633 = relay.TupleGetItem(func_7054_call(), 5)
func_6639_call = mod.get_global_var('func_6639')
func_6642_call = mutated_mod.get_global_var('func_6642')
var_13671 = relay.var("var_13671", dtype = "bool", shape = ())#candidate|13671|()|var|bool
var_13672 = relay.var("var_13672", dtype = "bool", shape = (156,))#candidate|13672|(156,)|var|bool
call_13670 = relay.TupleGetItem(func_6639_call(relay.reshape(var_13671.astype('bool'), []), relay.reshape(var_13672.astype('bool'), [1, 13, 12]), ), 2)
call_13673 = relay.TupleGetItem(func_6642_call(relay.reshape(var_13671.astype('bool'), []), relay.reshape(var_13672.astype('bool'), [1, 13, 12]), ), 2)
output = relay.Tuple([call_13632,call_13670,var_13671,var_13672,])
output2 = relay.Tuple([call_13633,call_13673,var_13671,var_13672,])
func_13678 = relay.Function([var_13671,var_13672,], output)
mod['func_13678'] = func_13678
mod = relay.transform.InferType()(mod)
mutated_mod['func_13678'] = func_13678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13678_call = mutated_mod.get_global_var('func_13678')
var_13680 = relay.var("var_13680", dtype = "bool", shape = ())#candidate|13680|()|var|bool
var_13681 = relay.var("var_13681", dtype = "bool", shape = (156,))#candidate|13681|(156,)|var|bool
call_13679 = func_13678_call(var_13680,var_13681,)
output = call_13679
func_13682 = relay.Function([var_13680,var_13681,], output)
mutated_mod['func_13682'] = func_13682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4838_call = mod.get_global_var('func_4838')
func_4839_call = mutated_mod.get_global_var('func_4839')
call_13689 = func_4838_call()
call_13690 = func_4838_call()
func_11962_call = mod.get_global_var('func_11962')
func_11964_call = mutated_mod.get_global_var('func_11964')
call_13695 = relay.TupleGetItem(func_11962_call(), 1)
call_13696 = relay.TupleGetItem(func_11964_call(), 1)
func_4811_call = mod.get_global_var('func_4811')
func_4812_call = mutated_mod.get_global_var('func_4812')
call_13707 = func_4811_call()
call_13708 = func_4811_call()
output = relay.Tuple([call_13689,call_13695,call_13707,])
output2 = relay.Tuple([call_13690,call_13696,call_13708,])
func_13713 = relay.Function([], output)
mod['func_13713'] = func_13713
mod = relay.transform.InferType()(mod)
mutated_mod['func_13713'] = func_13713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13713_call = mutated_mod.get_global_var('func_13713')
call_13714 = func_13713_call()
output = call_13714
func_13715 = relay.Function([], output)
mutated_mod['func_13715'] = func_13715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4144_call = mod.get_global_var('func_4144')
func_4145_call = mutated_mod.get_global_var('func_4145')
call_13727 = func_4144_call()
call_13728 = func_4144_call()
var_13733 = relay.var("var_13733", dtype = "float32", shape = (6, 7, 16))#candidate|13733|(6, 7, 16)|var|float32
bop_13734 = relay.bitwise_xor(call_13727.astype('uint8'), var_13733.astype('uint8')) # shape=(6, 7, 16)
bop_13737 = relay.bitwise_xor(call_13728.astype('uint8'), var_13733.astype('uint8')) # shape=(6, 7, 16)
output = bop_13734
output2 = bop_13737
func_13738 = relay.Function([var_13733,], output)
mod['func_13738'] = func_13738
mod = relay.transform.InferType()(mod)
mutated_mod['func_13738'] = func_13738
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13739 = relay.var("var_13739", dtype = "float32", shape = (6, 7, 16))#candidate|13739|(6, 7, 16)|var|float32
func_13738_call = mutated_mod.get_global_var('func_13738')
call_13740 = func_13738_call(var_13739)
output = call_13740
func_13741 = relay.Function([var_13739], output)
mutated_mod['func_13741'] = func_13741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9360_call = mod.get_global_var('func_9360')
func_9362_call = mutated_mod.get_global_var('func_9362')
call_13749 = relay.TupleGetItem(func_9360_call(), 0)
call_13750 = relay.TupleGetItem(func_9362_call(), 0)
func_9686_call = mod.get_global_var('func_9686')
func_9687_call = mutated_mod.get_global_var('func_9687')
call_13757 = func_9686_call()
call_13758 = func_9686_call()
func_12311_call = mod.get_global_var('func_12311')
func_12312_call = mutated_mod.get_global_var('func_12312')
call_13780 = relay.TupleGetItem(func_12311_call(), 2)
call_13781 = relay.TupleGetItem(func_12312_call(), 2)
output = relay.Tuple([call_13749,call_13757,call_13780,])
output2 = relay.Tuple([call_13750,call_13758,call_13781,])
func_13795 = relay.Function([], output)
mod['func_13795'] = func_13795
mod = relay.transform.InferType()(mod)
mutated_mod['func_13795'] = func_13795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13795_call = mutated_mod.get_global_var('func_13795')
call_13796 = func_13795_call()
output = call_13796
func_13797 = relay.Function([], output)
mutated_mod['func_13797'] = func_13797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10582_call = mod.get_global_var('func_10582')
func_10583_call = mutated_mod.get_global_var('func_10583')
call_13814 = relay.TupleGetItem(func_10582_call(), 2)
call_13815 = relay.TupleGetItem(func_10583_call(), 2)
output = relay.Tuple([call_13814,])
output2 = relay.Tuple([call_13815,])
func_13846 = relay.Function([], output)
mod['func_13846'] = func_13846
mod = relay.transform.InferType()(mod)
output = func_13846()
func_13847 = relay.Function([], output)
mutated_mod['func_13847'] = func_13847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5171_call = mod.get_global_var('func_5171')
func_5172_call = mutated_mod.get_global_var('func_5172')
call_13926 = relay.TupleGetItem(func_5171_call(), 2)
call_13927 = relay.TupleGetItem(func_5172_call(), 2)
output = call_13926
output2 = call_13927
func_13940 = relay.Function([], output)
mod['func_13940'] = func_13940
mod = relay.transform.InferType()(mod)
output = func_13940()
func_13941 = relay.Function([], output)
mutated_mod['func_13941'] = func_13941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10182_call = mod.get_global_var('func_10182')
func_10184_call = mutated_mod.get_global_var('func_10184')
call_13947 = relay.TupleGetItem(func_10182_call(), 0)
call_13948 = relay.TupleGetItem(func_10184_call(), 0)
func_6639_call = mod.get_global_var('func_6639')
func_6642_call = mutated_mod.get_global_var('func_6642')
const_13952 = relay.const(False, dtype = "bool")#candidate|13952|()|const|bool
const_13953 = relay.const([True,False,False,False,False,True,True,True,False,True,False,True,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,False,True,False,False,True,True,False,False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,True,False,False,False,True,False,True,True,False,False,False,False,True,True,True,True,True,False,False,False,False,False,True,True,True,True,True,True,True,False,True,False,True,False,True,False,False,False,False,False,False,False,True,True,True,False,False,True,False,False,True,True,False,False,False,False,True,True,True,False,True,True,True,False,True,False,True,True,False,True,True,False,True,False,True,False,False,True,True,True,False,False,False,False], dtype = "bool")#candidate|13953|(156,)|const|bool
call_13951 = relay.TupleGetItem(func_6639_call(relay.reshape(const_13952.astype('bool'), []), relay.reshape(const_13953.astype('bool'), [1, 13, 12]), ), 2)
call_13954 = relay.TupleGetItem(func_6642_call(relay.reshape(const_13952.astype('bool'), []), relay.reshape(const_13953.astype('bool'), [1, 13, 12]), ), 2)
output = relay.Tuple([call_13947,call_13951,const_13952,const_13953,])
output2 = relay.Tuple([call_13948,call_13954,const_13952,const_13953,])
func_13981 = relay.Function([], output)
mod['func_13981'] = func_13981
mod = relay.transform.InferType()(mod)
output = func_13981()
func_13982 = relay.Function([], output)
mutated_mod['func_13982'] = func_13982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13506_call = mod.get_global_var('func_13506')
func_13507_call = mutated_mod.get_global_var('func_13507')
call_13988 = relay.TupleGetItem(func_13506_call(), 1)
call_13989 = relay.TupleGetItem(func_13507_call(), 1)
func_7087_call = mod.get_global_var('func_7087')
func_7088_call = mutated_mod.get_global_var('func_7088')
call_13993 = relay.TupleGetItem(func_7087_call(), 0)
call_13994 = relay.TupleGetItem(func_7088_call(), 0)
var_14039 = relay.var("var_14039", dtype = "int8", shape = (6, 6, 8))#candidate|14039|(6, 6, 8)|var|int8
bop_14040 = relay.greater_equal(call_13988.astype('bool'), relay.reshape(var_14039.astype('bool'), relay.shape_of(call_13988))) # shape=(6, 6, 8)
bop_14043 = relay.greater_equal(call_13989.astype('bool'), relay.reshape(var_14039.astype('bool'), relay.shape_of(call_13989))) # shape=(6, 6, 8)
output = relay.Tuple([call_13993,bop_14040,])
output2 = relay.Tuple([call_13994,bop_14043,])
F = relay.Function([var_14039,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_14039,], output2)
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
