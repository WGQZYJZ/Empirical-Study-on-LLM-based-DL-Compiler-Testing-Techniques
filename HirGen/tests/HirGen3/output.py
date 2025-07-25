import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_53 = relay.var("var_53", dtype = "int16", shape = (2, 11, 7))#candidate|53|(2, 11, 7)|var|int16
const_54 = relay.const([[[-1,-6,-8,-1,-3,-6,7],[-9,-6,5,-2,-7,-2,1],[4,-7,2,-8,-4,-1,-1],[-3,-5,-5,1,-10,4,-9],[-10,-10,-4,-1,-10,9,10],[-10,6,-9,8,-1,4,3],[3,-4,10,-7,-3,-3,9],[-7,-1,-10,-2,8,-3,-8],[-2,-6,-1,-6,-6,-7,3],[-4,-1,1,-9,9,-8,-1],[5,7,-10,-10,5,4,-1]],[[2,3,6,8,8,-8,1],[5,6,-3,7,8,-2,5],[4,-1,2,4,-9,-5,4],[-5,9,8,2,-10,3,-8],[1,-5,1,-3,9,3,2],[5,1,-2,4,8,3,6],[-6,-3,10,-1,-3,6,-4],[9,6,3,-6,10,6,5],[-3,-5,5,-5,-7,8,1],[-3,-2,2,-6,7,-1,-1],[2,6,9,4,3,-1,-6]]], dtype = "int16")#candidate|54|(2, 11, 7)|const|int16
bop_55 = relay.logical_xor(var_53.astype('int16'), relay.reshape(const_54.astype('int16'), relay.shape_of(var_53))) # shape=(2, 11, 7)
output = bop_55
output2 = bop_55
func_61 = relay.Function([var_53,], output)
mod['func_61'] = func_61
mod = relay.transform.InferType()(mod)
var_62 = relay.var("var_62", dtype = "int16", shape = (2, 11, 7))#candidate|62|(2, 11, 7)|var|int16
output = func_61(var_62)
func_63 = relay.Function([var_62], output)
mutated_mod['func_63'] = func_63
mutated_mod = relay.transform.InferType()(mutated_mod)
const_81 = relay.const(8, dtype = "int8")#candidate|81|()|const|int8
const_82 = relay.const([[[-9,10,6,1,-2,8,9,8,7,-3,-1],[10,-1,-4,-6,-2,1,-4,2,8,2,-1],[7,-4,3,5,-2,-1,-10,7,6,-10,1],[-4,9,8,8,-6,-1,9,10,7,9,-6],[-4,4,4,7,-9,-10,-10,2,10,-3,10],[6,-8,-3,-2,7,-2,6,-6,-3,3,-5],[-4,3,7,-6,9,-9,4,5,9,-1,-4],[8,1,7,5,-9,1,4,7,8,-1,-5],[7,2,-2,8,4,-8,-9,9,10,-4,9],[10,-5,3,5,4,10,7,-3,-9,-3,1],[5,6,7,6,-6,-3,-7,1,-6,2,-3],[9,-4,-2,-9,-8,3,8,2,6,-2,-2],[-7,9,-8,-1,-1,-8,1,1,2,-2,3],[-5,-8,6,-9,-9,9,-10,-10,-9,-1,6],[-6,-2,8,3,6,10,-8,3,3,6,9],[-1,8,2,9,-1,-6,-3,-7,-10,6,-8]],[[-4,-4,5,9,5,-5,-3,2,4,7,6],[-8,10,-9,-8,1,-10,-9,2,-8,-9,9],[9,-4,-7,-5,-4,-8,-1,-9,6,10,-2],[8,6,-2,-9,7,-6,-1,3,-8,10,-1],[4,9,9,-3,-8,-6,7,9,1,-3,10],[-10,1,10,-3,-2,1,5,3,-3,-1,5],[-9,3,4,-8,2,-7,-7,6,-10,-7,2],[-4,-1,7,-8,-9,1,-8,8,9,-6,-4],[-5,-3,9,-9,3,7,10,8,-6,-6,9],[-2,-2,8,9,-10,-10,-3,-4,-9,6,5],[-8,6,9,3,-6,6,7,-7,-6,3,2],[5,8,7,8,4,4,-3,1,-3,-2,6],[-5,-8,-10,6,-6,-9,5,-2,7,-2,-5],[-6,-1,-5,1,4,4,6,-2,-7,-5,7],[-4,4,5,4,1,8,10,6,-5,-5,4],[-5,8,-9,10,-5,-4,-6,5,1,-8,9]],[[-2,-9,-7,8,-8,10,-6,-8,-4,9,-2],[-9,4,4,-8,-2,-7,-7,-5,-6,9,10],[-4,2,-3,-7,5,-3,-7,3,-9,-6,-5],[-3,-10,-7,6,4,10,-9,6,-10,-2,-2],[-2,-4,9,9,5,-4,10,1,1,-7,1],[3,-10,8,8,10,-4,-2,6,-7,-1,5],[-2,-9,-4,-3,-10,10,-9,-1,8,-6,-8],[3,8,-5,3,-2,6,10,-8,3,-7,-10],[-1,1,4,2,-6,8,-7,4,-2,-4,2],[8,-7,9,-6,-10,2,8,1,-8,9,2],[8,5,-6,8,-5,7,-9,-5,7,-4,7],[5,-4,-6,10,8,-5,7,5,9,-6,-3],[-5,2,4,-1,9,-10,8,5,-3,5,9],[-1,-9,-8,9,10,10,7,7,6,3,-9],[1,8,-1,5,-7,8,-9,1,-6,3,4],[-1,-10,-8,-4,-4,5,10,-5,7,3,7]],[[2,9,2,5,6,8,-2,8,5,2,4],[-5,-8,10,-8,1,-7,-7,6,5,-7,-5],[1,-6,5,-6,1,-7,-6,8,4,-5,2],[9,3,10,-1,2,8,10,-7,2,2,6],[-8,3,6,4,9,5,-9,5,-2,4,6],[-5,4,10,9,-3,10,9,-1,3,-6,3],[5,-7,-4,9,7,-4,1,7,2,7,4],[-8,-8,-7,3,-2,-10,7,2,-6,8,-1],[6,1,6,9,-3,-6,-2,-5,-7,-3,-6],[2,6,8,-8,5,5,-1,3,2,9,-8],[3,3,-2,6,9,-5,-8,1,2,-1,3],[9,-1,3,-8,-8,6,-2,2,-8,8,7],[8,3,5,6,-5,5,3,4,1,-6,-5],[-7,8,7,-9,-3,4,7,-7,1,-6,-8],[6,-4,-5,-4,-1,-7,-6,-7,3,-4,-4],[-8,3,-5,-6,10,6,-9,-4,-1,-7,4]],[[-7,10,10,6,-4,9,6,6,8,5,2],[4,8,1,-6,-1,-7,-2,5,-3,4,6],[-7,-5,-10,8,6,-8,-5,-2,-7,5,-3],[2,-5,-7,-8,-3,9,9,-10,-1,-7,1],[-1,5,5,1,7,6,-10,-2,-9,-3,-5],[-8,-9,9,8,-10,-4,-7,6,-9,-3,4],[-9,2,-3,6,7,-1,1,-10,2,9,6],[-9,6,-5,4,-2,10,-2,-9,3,10,-10],[-5,-1,-2,-7,8,3,5,-1,-1,-5,-7],[6,-5,9,2,-8,2,6,-2,6,-10,-4],[-9,5,7,1,-6,9,-5,-9,-10,5,-10],[7,7,-4,2,-1,2,-3,7,3,2,-7],[10,5,6,-1,-5,8,2,9,9,-9,8],[-8,-7,-10,-2,-7,6,-10,5,9,-10,2],[-1,7,2,9,-7,7,-9,-2,-4,5,2],[2,-9,-7,-10,-2,-9,10,-5,1,7,6]],[[5,-1,9,-8,-3,6,3,-10,2,5,1],[3,6,9,-4,-1,5,9,-8,-2,-9,-3],[-4,7,-7,9,10,5,10,9,-9,4,-2],[7,-9,-3,1,-3,10,-3,4,4,-8,8],[-5,1,-7,7,7,3,4,6,-3,2,-9],[-2,-9,-7,-9,4,-1,-5,1,10,-9,5],[9,1,-10,-9,8,-4,-10,-3,-5,1,1],[6,2,-9,1,6,-5,3,-10,4,4,2],[-6,-4,-1,1,-5,-1,7,9,5,-7,2],[4,2,9,-4,3,7,5,4,-7,4,-7],[-1,-8,-2,5,-5,-6,-6,7,6,-4,-7],[1,6,2,10,-3,-4,5,6,-1,-10,-1],[4,8,8,-4,-10,10,-5,-8,-10,3,-1],[-1,10,-7,-1,-7,-6,6,7,-3,-7,5],[-3,-6,-3,8,-9,1,1,2,-8,-6,3],[2,-1,9,8,-9,-6,-6,4,-4,-1,4]],[[7,-3,-2,1,10,-7,8,1,9,-7,-3],[-3,4,-9,4,-8,-9,6,-9,-9,2,-4],[-2,-4,-4,-4,-3,5,-8,-6,-10,-5,-5],[-10,-10,7,-7,-10,-5,7,-7,-8,2,2],[10,2,2,8,-8,4,-9,10,4,-2,6],[10,-4,6,4,6,5,3,-5,7,-1,-3],[-5,-6,-5,-10,10,6,10,10,1,-7,3],[-6,-3,4,-7,4,-4,-1,-9,-9,10,-4],[7,-4,7,-7,-3,9,-7,8,1,-3,2],[-3,-4,-1,8,-5,-9,-5,10,7,4,-7],[-10,-4,1,-8,-1,4,-3,-10,-2,10,-3],[8,-7,-7,10,2,3,2,3,-6,9,10],[7,-7,-6,-10,9,2,-4,9,-5,3,6],[1,-3,4,7,8,-5,-4,-9,9,4,-8],[-2,-2,7,-6,-1,2,4,-8,1,4,10],[-8,4,-8,3,-7,-2,-4,4,-10,7,-1]],[[-10,-3,-6,9,-6,-6,6,-1,10,4,6],[-1,-7,7,4,8,-8,5,7,1,-10,-4],[-1,-5,-2,4,-8,2,5,1,7,3,8],[1,-1,1,-9,2,-1,-2,-8,2,-9,-1],[-4,-4,-2,10,5,7,6,-1,-4,-5,-10],[9,1,-3,-8,7,-5,-4,-7,6,8,2],[-1,6,-6,10,6,-5,1,-9,10,-10,6],[1,10,9,-3,1,6,1,8,9,3,3],[9,4,10,6,9,1,-7,9,-3,-7,-6],[10,-2,-10,-2,10,6,5,-7,4,-8,-7],[-7,-8,7,-9,4,8,2,-10,2,-8,-3],[6,3,7,-7,8,-3,4,2,2,7,-1],[-8,3,-2,-10,-5,-8,-8,-2,1,9,-8],[3,-8,-7,7,-4,-10,6,-10,-10,7,-3],[-3,10,-5,-10,-3,3,10,-6,10,3,-7],[-4,7,1,-2,-1,-9,10,1,7,3,-7]],[[1,-1,5,1,-2,10,10,7,6,-8,-8],[-7,6,-5,3,3,7,-5,5,4,-2,1],[6,6,4,6,-10,-3,6,-7,-1,-7,2],[1,-7,-9,1,-4,7,-10,-4,5,9,2],[7,8,-10,8,-6,-3,6,-5,1,-6,7],[-1,2,7,-5,1,-10,2,6,4,-9,-5],[1,1,-9,-2,5,-9,1,-2,-7,-8,4],[7,-10,-9,9,3,6,-4,3,3,-1,-8],[-10,-9,-5,-4,-7,-8,3,3,3,-4,1],[6,-7,-5,3,1,4,-10,6,-8,4,-9],[5,-1,-9,-9,-6,-6,8,-1,7,-4,-5],[1,-8,-4,7,1,5,-10,8,5,-8,7],[4,-7,-4,-3,-7,10,-3,10,-8,-2,3],[-7,5,7,7,-1,5,-4,-1,10,9,-5],[-4,4,6,-5,10,-1,6,-10,5,-3,-9],[1,-4,-8,-1,-7,8,7,9,-2,-1,-4]],[[5,9,-5,-2,9,-4,4,-4,-7,-10,-4],[8,8,-2,6,-8,-2,-1,-7,-1,6,-7],[-7,7,-6,8,5,-3,9,4,3,-6,-6],[2,-2,2,-6,2,2,9,10,7,-5,-10],[6,-10,5,4,5,-9,-6,-8,-9,-8,-10],[10,6,5,10,8,9,-2,5,10,-1,8],[-9,2,7,-3,-8,-6,4,8,7,7,3],[4,5,-10,4,-6,6,-3,9,-9,10,-3],[-7,6,4,-3,5,5,-1,8,2,-8,-1],[1,-8,-9,6,-5,-3,-8,-6,-4,-6,3],[-3,-5,-7,7,-8,10,-9,-6,-2,-9,-4],[2,5,3,6,-3,8,-7,-2,5,-3,8],[5,-6,-5,-2,1,10,-1,-1,8,-7,3],[3,8,-5,-2,-2,7,4,4,-2,1,3],[5,-10,-8,-1,-2,-6,10,-3,4,-9,-5],[4,8,-4,-8,-10,1,-5,-6,-9,1,-1]],[[7,-5,-9,-6,5,4,8,10,-7,8,-10],[-6,-1,7,10,-5,3,-10,2,1,-5,-1],[-4,-8,3,10,3,2,-3,-8,-10,-10,2],[-9,5,6,-4,-3,-9,-3,7,8,1,3],[-10,7,-5,4,8,-4,3,4,-6,-10,-8],[-9,-6,6,-8,1,10,-7,6,4,7,8],[-7,-9,-1,-10,-2,3,-8,5,-8,4,-6],[-4,-4,-8,-6,3,1,8,3,-1,9,-4],[3,-2,8,2,7,-8,-6,-2,-3,8,6],[-7,6,-3,2,-3,-7,-9,-1,10,-6,-8],[3,5,-4,-3,10,9,-8,2,-10,-6,-2],[-3,-3,-10,1,9,6,1,8,-10,4,4],[-2,1,-3,-2,-9,7,-7,-2,3,-4,7],[10,-9,-2,10,4,-4,5,-1,4,1,3],[10,-8,-7,3,8,-9,-4,10,9,-5,1],[2,-6,-4,-10,6,-4,-3,9,-5,1,-3]],[[-7,8,-9,8,-4,3,-7,-8,-6,6,-1],[1,7,6,-1,3,-2,-3,4,4,-4,-8],[4,7,-10,-9,4,-10,5,-8,-5,-6,10],[9,-5,-1,-9,-9,3,-4,10,6,1,-6],[-4,-7,-5,-7,4,-10,10,-5,8,-4,1],[6,9,-9,9,-1,8,-3,10,-10,5,-1],[-1,6,2,4,5,-9,3,-7,1,-7,-5],[-4,8,9,-5,-2,9,-8,5,-4,-4,-7],[1,1,-3,1,-7,-2,2,-2,-2,-3,-2],[1,5,-10,-10,-7,-4,-1,5,6,10,10],[-1,-6,7,-3,-2,-6,2,9,-6,1,3],[6,5,-1,-2,-4,3,6,-1,9,-5,-4],[3,-7,8,-9,-9,2,-7,-8,3,-1,-5],[-8,-8,-2,4,-8,-9,-7,4,-1,-1,8],[3,-8,-1,7,-8,10,4,8,10,-6,-4],[8,-1,10,10,-3,-5,1,1,-10,3,-6]],[[-4,6,4,-2,6,-4,-9,-10,-2,1,-3],[-1,-2,-7,3,-3,-2,2,10,-4,-6,-3],[3,-1,6,4,6,-8,-8,-5,-10,1,-5],[8,9,-2,-10,-7,10,-2,1,8,3,6],[-2,-4,9,-6,8,-10,6,1,8,-1,-7],[-5,-8,4,10,3,-10,6,-2,-4,6,9],[-5,-8,-10,9,3,-4,8,2,-7,-10,4],[8,8,-8,5,6,10,3,4,-7,-10,10],[8,-6,9,-6,3,8,-6,-8,6,1,8],[7,-9,-1,-5,7,-2,-2,8,-3,2,4],[10,8,-6,3,4,5,6,4,-6,-7,-1],[-1,-5,-4,8,4,2,5,1,-9,1,2],[-2,9,5,-8,4,-9,-6,7,-1,-1,3],[10,-7,2,-4,3,1,6,9,6,7,-4],[8,-6,-4,-3,-4,-2,-3,9,1,5,-6],[-9,7,8,-1,-7,-6,10,-2,7,-6,-9]],[[5,6,7,-7,-4,-8,2,-7,2,3,-6],[10,-6,4,-5,-2,-10,-6,2,2,2,9],[7,6,-9,-9,-2,5,-5,-1,-3,-3,-3],[-9,-4,1,10,9,-5,1,4,10,-9,3],[5,6,-6,10,10,4,-10,-2,-6,-2,-6],[8,-2,-5,5,-7,-3,-8,-4,10,-8,9],[-3,10,2,2,-4,-9,1,9,3,6,-9],[-4,-5,-6,-9,10,-8,1,4,-9,6,-7],[1,2,-2,-7,-3,3,-7,10,5,-10,-2],[-4,-6,5,10,-8,-7,-4,-9,9,4,-9],[-2,9,-8,-2,-9,9,1,7,5,2,-8],[-1,1,-8,-2,8,-7,-1,3,7,2,-7],[-9,4,-2,8,-7,4,8,3,-10,-6,-5],[1,-10,9,-4,5,-1,-9,-7,2,5,10],[-9,-5,-3,7,8,7,8,-10,-4,-8,-5],[-9,-4,-4,8,-2,8,-7,6,10,-2,2]],[[5,-2,10,-6,-7,-7,6,7,7,1,7],[-4,-2,1,-1,3,6,5,-7,2,5,-4],[1,3,3,1,1,-6,-10,-8,9,-9,9],[2,-4,-10,2,-10,-5,10,6,-9,7,-2],[2,1,3,8,-3,-8,5,-6,1,-1,-8],[6,2,-2,1,-9,-4,-6,-8,9,-5,10],[6,-8,-3,-3,9,4,-7,4,10,2,-4],[3,1,5,10,5,-1,-10,1,7,7,5],[10,1,-3,-6,-1,8,10,9,7,3,-6],[-4,8,-1,3,-8,-5,2,10,-2,-4,3],[4,-1,6,10,-9,-3,8,-4,9,-3,-9],[-2,-3,-1,7,-3,8,3,-10,-7,9,-7],[-3,-9,3,9,-9,2,-5,10,-7,-2,-9],[-8,-8,-9,7,6,-7,6,-7,1,-4,-9],[-5,3,-4,-6,10,5,3,8,9,1,9],[5,2,3,8,7,2,5,6,10,-9,5]],[[8,1,-7,3,-4,3,4,-4,-9,6,-2],[9,4,4,-6,-5,-4,10,-3,-9,-1,2],[10,8,6,1,4,-6,1,6,-10,-2,9],[8,-4,10,-1,3,-6,-1,4,2,3,-8],[9,4,5,6,5,-10,2,8,-10,-5,9],[-1,-9,1,-3,10,5,1,-7,7,-2,-5],[-5,-10,-2,-3,4,-6,-9,6,-9,1,-10],[5,-1,9,9,2,7,-9,8,1,-6,-6],[5,-6,-10,-8,9,-8,-6,-6,1,9,9],[-8,-9,-10,8,-1,-5,9,4,-6,1,-3],[-10,-3,6,-10,1,-1,-9,-7,-6,9,-7],[-9,-6,-4,-6,7,8,9,-4,-9,9,7],[-3,-4,-5,10,-3,-3,-3,-7,3,-7,4],[7,6,-4,7,2,6,-1,-1,2,-10,-3],[9,-2,-6,5,8,9,-7,-1,-2,6,-1],[8,-8,7,3,-10,2,9,4,7,8,-6]]], dtype = "int8")#candidate|82|(16, 16, 11)|const|int8
bop_83 = relay.minimum(const_81.astype('int8'), const_82.astype('int8')) # shape=(16, 16, 11)
func_61_call = mod.get_global_var('func_61')
func_63_call = mutated_mod.get_global_var('func_63')
const_89 = relay.const([-7,1,2,6,-5,1,1,-1,-1,5,-3,-10,6,4,4,-4,-10,1,-8,4,-2,-5,3,1,5,5,-2,10,-3,-8,4,8,-10,-3,-5,-4,-4,-9,6,-2,6,9,-2,-6,5,-10,9,-2,6,-5,-6,10,-7,8,-1,-4,-8,4,2,-3,-3,8,2,9,7,2,5,5,3,7,4,10,4,9,4,-5,-6,1,4,9,5,7,3,6,-5,-1,-6,-10,7,-8,-3,9,9,9,-9,-5,10,-6,5,-9,5,-1,3,3,1,10,-6,3,-1,9,1,-4,-7,3,2,-2,4,-10,-3,8,4,-9,-8,-6,-7,9,-8,-10,-3,6,-7,-4,2,-9,-5,-10,-4,1,-1,1,1,-5,-2,5,8,-1,-8,7,9,4,2,4,4,7], dtype = "int16")#candidate|89|(154,)|const|int16
call_88 = func_61_call(relay.reshape(const_89.astype('int16'), [2, 11, 7]))
call_90 = func_61_call(relay.reshape(const_89.astype('int16'), [2, 11, 7]))
bop_93 = relay.maximum(const_82.astype('uint64'), relay.reshape(bop_83.astype('uint64'), relay.shape_of(const_82))) # shape=(16, 16, 11)
func_61_call = mod.get_global_var('func_61')
func_63_call = mutated_mod.get_global_var('func_63')
call_97 = func_61_call(relay.reshape(call_88.astype('int16'), [2, 11, 7]))
call_98 = func_61_call(relay.reshape(call_88.astype('int16'), [2, 11, 7]))
var_102 = relay.var("var_102", dtype = "int16", shape = (2, 11, 7))#candidate|102|(2, 11, 7)|var|int16
bop_103 = relay.less_equal(call_88.astype('bool'), relay.reshape(var_102.astype('bool'), relay.shape_of(call_88))) # shape=(2, 11, 7)
bop_106 = relay.less_equal(call_90.astype('bool'), relay.reshape(var_102.astype('bool'), relay.shape_of(call_90))) # shape=(2, 11, 7)
var_116 = relay.var("var_116", dtype = "uint64", shape = (16, 16, 11))#candidate|116|(16, 16, 11)|var|uint64
bop_117 = relay.logical_xor(bop_93.astype('uint64'), relay.reshape(var_116.astype('uint64'), relay.shape_of(bop_93))) # shape=(16, 16, 11)
func_61_call = mod.get_global_var('func_61')
func_63_call = mutated_mod.get_global_var('func_63')
call_122 = func_61_call(relay.reshape(var_102.astype('int16'), [2, 11, 7]))
call_123 = func_61_call(relay.reshape(var_102.astype('int16'), [2, 11, 7]))
bop_124 = relay.logical_and(var_102.astype('bool'), relay.reshape(bop_103.astype('bool'), relay.shape_of(var_102))) # shape=(2, 11, 7)
bop_127 = relay.logical_and(var_102.astype('bool'), relay.reshape(bop_106.astype('bool'), relay.shape_of(var_102))) # shape=(2, 11, 7)
output = relay.Tuple([const_89,call_97,bop_117,call_122,bop_124,])
output2 = relay.Tuple([const_89,call_98,bop_117,call_123,bop_127,])
func_128 = relay.Function([var_102,var_116,], output)
mod['func_128'] = func_128
mod = relay.transform.InferType()(mod)
var_129 = relay.var("var_129", dtype = "int16", shape = (2, 11, 7))#candidate|129|(2, 11, 7)|var|int16
var_130 = relay.var("var_130", dtype = "uint64", shape = (16, 16, 11))#candidate|130|(16, 16, 11)|var|uint64
output = func_128(var_129,var_130,)
func_131 = relay.Function([var_129,var_130,], output)
mutated_mod['func_131'] = func_131
mutated_mod = relay.transform.InferType()(mutated_mod)
const_159 = relay.const([[[1.401832,4.651218,-2.027999,-1.911331,-2.412229,-7.887293,-5.735480,2.826063],[8.845701,-9.713774,5.065881,8.480397,-0.856748,-4.921902,4.059468,-7.461641]],[[-6.931157,-1.967015,-3.187372,-1.104737,-1.991102,6.606479,4.296832,2.736073],[3.574896,1.905240,3.865148,-7.190557,-3.345992,-2.160323,-8.423513,-9.445317]],[[3.556415,2.566917,9.586210,-5.970499,-9.112358,4.184029,-9.129314,-1.328934],[-4.366517,-5.878326,9.139590,2.294375,-6.341186,8.292331,6.979285,9.426229]],[[-8.981092,-7.651174,-0.044979,5.712191,-7.165199,-4.982998,-0.228229,-0.988471],[-7.614796,-6.477663,3.655142,-9.529784,9.351719,-4.225126,8.718489,9.628677]],[[-8.669958,-3.244105,2.162556,-2.039579,-0.303715,-9.164485,4.954633,6.948979],[-6.960643,5.734977,5.004224,3.982101,5.923766,9.325410,8.616183,-2.744069]],[[6.714627,-7.389764,8.410573,-6.001458,-0.863233,-8.717439,-1.300101,4.643153],[8.841263,-6.903158,-6.363151,9.555406,-3.967155,9.043162,-7.309208,9.745354]],[[-3.815125,-3.013057,-0.868775,6.967310,1.061032,8.219338,0.037583,-8.504765],[5.700471,2.259168,-9.587641,-5.167861,-3.045743,-0.331434,4.439135,-8.489462]],[[-4.705253,1.743730,7.498180,9.297928,-5.653416,-3.238318,5.806154,-4.580859],[-8.296536,6.761878,7.256957,6.103151,2.523119,-6.616615,2.000525,-9.497000]],[[2.256162,6.796758,-1.394863,9.432964,0.633447,-0.702053,4.761584,6.447415],[-0.172383,-4.981918,-5.268620,4.790439,-8.558687,9.425375,-1.125907,5.271464]],[[6.532802,4.332494,5.283379,9.132600,-8.686332,1.450419,-1.088078,1.045880],[5.376444,-6.894963,5.036987,3.457670,3.083376,-5.687712,-9.307480,8.411671]],[[-0.469379,8.623068,-3.287368,-0.210027,-7.149216,-5.255224,-4.637935,-6.601226],[2.974393,-2.064088,-4.026054,-8.210451,-0.088559,-8.257928,-9.478022,-0.312495]],[[-6.383587,-7.423580,-1.192440,1.284501,6.081165,-0.905460,-9.757798,9.249661],[4.456622,-0.628014,-1.803914,-6.259162,8.865719,6.858409,-1.539822,-3.660992]],[[-5.371186,2.227616,9.210899,5.593643,-8.085561,4.593053,-1.876635,6.388169],[-9.565000,-0.864144,-4.892225,9.412505,6.328717,-8.809382,-8.858682,-5.936884]],[[9.449297,-2.710941,-9.068586,6.540951,8.610854,7.577996,-7.561813,7.154898],[7.457978,8.609533,-8.407855,8.578545,6.116025,-8.006566,4.882913,-4.308653]]], dtype = "float64")#candidate|159|(14, 2, 8)|const|float64
uop_160 = relay.log(const_159.astype('float64')) # shape=(14, 2, 8)
func_61_call = mod.get_global_var('func_61')
func_63_call = mutated_mod.get_global_var('func_63')
const_166 = relay.const([10,-6,3,-9,-3,7,-6,-2,3,-10,7,-7,2,4,-6,3,-10,-1,2,-5,-2,-7,-5,-5,-4,-3,2,-5,-4,4,-9,9,6,4,9,3,4,-10,-8,9,1,3,2,10,7,7,1,-7,6,-4,-3,-4,6,5,-8,6,-6,5,-8,-3,8,-5,8,7,5,6,-8,-4,6,-10,4,6,-8,-8,-7,-3,3,-8,-10,-2,6,-5,-2,-1,-8,3,-9,-4,3,3,-2,-8,4,3,-1,-1,5,-1,4,-5,3,4,8,-8,9,2,-8,4,6,-6,-4,-4,-4,8,-7,10,-1,-3,-2,4,4,3,-8,-6,4,-3,-10,9,-2,-9,10,-8,-4,3,-1,9,3,-9,-7,-7,-6,3,-7,-9,-1,-7,-10,3,-3,-1,-3,2,-2,-9], dtype = "int16")#candidate|166|(154,)|const|int16
call_165 = func_61_call(relay.reshape(const_166.astype('int16'), [2, 11, 7]))
call_167 = func_61_call(relay.reshape(const_166.astype('int16'), [2, 11, 7]))
output = relay.Tuple([uop_160,call_165,const_166,])
output2 = relay.Tuple([uop_160,call_167,const_166,])
func_171 = relay.Function([], output)
mod['func_171'] = func_171
mod = relay.transform.InferType()(mod)
mutated_mod['func_171'] = func_171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_171_call = mutated_mod.get_global_var('func_171')
call_172 = func_171_call()
output = call_172
func_173 = relay.Function([], output)
mutated_mod['func_173'] = func_173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_171_call = mod.get_global_var('func_171')
func_173_call = mutated_mod.get_global_var('func_173')
call_177 = relay.TupleGetItem(func_171_call(), 0)
call_178 = relay.TupleGetItem(func_173_call(), 0)
var_179 = relay.var("var_179", dtype = "float64", shape = (14, 2, 8))#candidate|179|(14, 2, 8)|var|float64
bop_180 = relay.less_equal(call_177.astype('bool'), relay.reshape(var_179.astype('bool'), relay.shape_of(call_177))) # shape=(14, 2, 8)
bop_183 = relay.less_equal(call_178.astype('bool'), relay.reshape(var_179.astype('bool'), relay.shape_of(call_178))) # shape=(14, 2, 8)
uop_184 = relay.log10(var_179.astype('float32')) # shape=(14, 2, 8)
output = relay.Tuple([bop_180,uop_184,])
output2 = relay.Tuple([bop_183,uop_184,])
func_201 = relay.Function([var_179,], output)
mod['func_201'] = func_201
mod = relay.transform.InferType()(mod)
var_202 = relay.var("var_202", dtype = "float64", shape = (14, 2, 8))#candidate|202|(14, 2, 8)|var|float64
output = func_201(var_202)
func_203 = relay.Function([var_202], output)
mutated_mod['func_203'] = func_203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_171_call = mod.get_global_var('func_171')
func_173_call = mutated_mod.get_global_var('func_173')
call_229 = relay.TupleGetItem(func_171_call(), 0)
call_230 = relay.TupleGetItem(func_173_call(), 0)
var_241 = relay.var("var_241", dtype = "float64", shape = (14, 2, 8))#candidate|241|(14, 2, 8)|var|float64
bop_242 = relay.logical_xor(call_229.astype('int8'), relay.reshape(var_241.astype('int8'), relay.shape_of(call_229))) # shape=(14, 2, 8)
bop_245 = relay.logical_xor(call_230.astype('int8'), relay.reshape(var_241.astype('int8'), relay.shape_of(call_230))) # shape=(14, 2, 8)
output = relay.Tuple([bop_242,])
output2 = relay.Tuple([bop_245,])
func_264 = relay.Function([var_241,], output)
mod['func_264'] = func_264
mod = relay.transform.InferType()(mod)
var_265 = relay.var("var_265", dtype = "float64", shape = (14, 2, 8))#candidate|265|(14, 2, 8)|var|float64
output = func_264(var_265)
func_266 = relay.Function([var_265], output)
mutated_mod['func_266'] = func_266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_171_call = mod.get_global_var('func_171')
func_173_call = mutated_mod.get_global_var('func_173')
call_324 = relay.TupleGetItem(func_171_call(), 1)
call_325 = relay.TupleGetItem(func_173_call(), 1)
func_128_call = mod.get_global_var('func_128')
func_131_call = mutated_mod.get_global_var('func_131')
var_327 = relay.var("var_327", dtype = "uint64", shape = (1408, 2))#candidate|327|(1408, 2)|var|uint64
call_326 = relay.TupleGetItem(func_128_call(relay.reshape(call_324.astype('int16'), [2, 11, 7]), relay.reshape(var_327.astype('uint64'), [16, 16, 11]), ), 2)
call_328 = relay.TupleGetItem(func_131_call(relay.reshape(call_324.astype('int16'), [2, 11, 7]), relay.reshape(var_327.astype('uint64'), [16, 16, 11]), ), 2)
output = relay.Tuple([call_324,call_326,var_327,])
output2 = relay.Tuple([call_325,call_328,var_327,])
func_329 = relay.Function([var_327,], output)
mod['func_329'] = func_329
mod = relay.transform.InferType()(mod)
var_330 = relay.var("var_330", dtype = "uint64", shape = (1408, 2))#candidate|330|(1408, 2)|var|uint64
output = func_329(var_330)
func_331 = relay.Function([var_330], output)
mutated_mod['func_331'] = func_331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_171_call = mod.get_global_var('func_171')
func_173_call = mutated_mod.get_global_var('func_173')
call_342 = relay.TupleGetItem(func_171_call(), 2)
call_343 = relay.TupleGetItem(func_173_call(), 2)
func_201_call = mod.get_global_var('func_201')
func_203_call = mutated_mod.get_global_var('func_203')
var_363 = relay.var("var_363", dtype = "float64", shape = (224,))#candidate|363|(224,)|var|float64
call_362 = relay.TupleGetItem(func_201_call(relay.reshape(var_363.astype('float64'), [14, 2, 8])), 0)
call_364 = relay.TupleGetItem(func_203_call(relay.reshape(var_363.astype('float64'), [14, 2, 8])), 0)
output = relay.Tuple([call_342,call_362,var_363,])
output2 = relay.Tuple([call_343,call_364,var_363,])
func_366 = relay.Function([var_363,], output)
mod['func_366'] = func_366
mod = relay.transform.InferType()(mod)
var_367 = relay.var("var_367", dtype = "float64", shape = (224,))#candidate|367|(224,)|var|float64
output = func_366(var_367)
func_368 = relay.Function([var_367], output)
mutated_mod['func_368'] = func_368
mutated_mod = relay.transform.InferType()(mutated_mod)
var_397 = relay.var("var_397", dtype = "float64", shape = (16, 8, 8))#candidate|397|(16, 8, 8)|var|float64
uop_398 = relay.sigmoid(var_397.astype('float64')) # shape=(16, 8, 8)
uop_408 = relay.log2(uop_398.astype('float32')) # shape=(16, 8, 8)
output = uop_408
output2 = uop_408
func_414 = relay.Function([var_397,], output)
mod['func_414'] = func_414
mod = relay.transform.InferType()(mod)
var_415 = relay.var("var_415", dtype = "float64", shape = (16, 8, 8))#candidate|415|(16, 8, 8)|var|float64
output = func_414(var_415)
func_416 = relay.Function([var_415], output)
mutated_mod['func_416'] = func_416
mutated_mod = relay.transform.InferType()(mutated_mod)
var_424 = relay.var("var_424", dtype = "float32", shape = (15, 1, 8))#candidate|424|(15, 1, 8)|var|float32
uop_425 = relay.sin(var_424.astype('float32')) # shape=(15, 1, 8)
func_128_call = mod.get_global_var('func_128')
func_131_call = mutated_mod.get_global_var('func_131')
var_440 = relay.var("var_440", dtype = "int16", shape = (154,))#candidate|440|(154,)|var|int16
var_441 = relay.var("var_441", dtype = "uint64", shape = (2816,))#candidate|441|(2816,)|var|uint64
call_439 = relay.TupleGetItem(func_128_call(relay.reshape(var_440.astype('int16'), [2, 11, 7]), relay.reshape(var_441.astype('uint64'), [16, 16, 11]), ), 3)
call_442 = relay.TupleGetItem(func_131_call(relay.reshape(var_440.astype('int16'), [2, 11, 7]), relay.reshape(var_441.astype('uint64'), [16, 16, 11]), ), 3)
uop_448 = relay.atanh(uop_425.astype('float32')) # shape=(15, 1, 8)
bop_451 = relay.bitwise_and(var_424.astype('int64'), relay.reshape(uop_425.astype('int64'), relay.shape_of(var_424))) # shape=(15, 1, 8)
bop_454 = relay.less_equal(uop_448.astype('bool'), relay.reshape(bop_451.astype('bool'), relay.shape_of(uop_448))) # shape=(15, 1, 8)
bop_461 = relay.equal(uop_425.astype('bool'), relay.reshape(bop_454.astype('bool'), relay.shape_of(uop_425))) # shape=(15, 1, 8)
output = relay.Tuple([call_439,var_440,var_441,bop_461,])
output2 = relay.Tuple([call_442,var_440,var_441,bop_461,])
func_464 = relay.Function([var_424,var_440,var_441,], output)
mod['func_464'] = func_464
mod = relay.transform.InferType()(mod)
mutated_mod['func_464'] = func_464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_464_call = mutated_mod.get_global_var('func_464')
var_466 = relay.var("var_466", dtype = "float32", shape = (15, 1, 8))#candidate|466|(15, 1, 8)|var|float32
var_467 = relay.var("var_467", dtype = "int16", shape = (154,))#candidate|467|(154,)|var|int16
var_468 = relay.var("var_468", dtype = "uint64", shape = (2816,))#candidate|468|(2816,)|var|uint64
call_465 = func_464_call(var_466,var_467,var_468,)
output = call_465
func_469 = relay.Function([var_466,var_467,var_468,], output)
mutated_mod['func_469'] = func_469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_171_call = mod.get_global_var('func_171')
func_173_call = mutated_mod.get_global_var('func_173')
call_474 = relay.TupleGetItem(func_171_call(), 0)
call_475 = relay.TupleGetItem(func_173_call(), 0)
output = relay.Tuple([call_474,])
output2 = relay.Tuple([call_475,])
func_479 = relay.Function([], output)
mod['func_479'] = func_479
mod = relay.transform.InferType()(mod)
mutated_mod['func_479'] = func_479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_479_call = mutated_mod.get_global_var('func_479')
call_480 = func_479_call()
output = call_480
func_481 = relay.Function([], output)
mutated_mod['func_481'] = func_481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_479_call = mod.get_global_var('func_479')
func_481_call = mutated_mod.get_global_var('func_481')
call_498 = relay.TupleGetItem(func_479_call(), 0)
call_499 = relay.TupleGetItem(func_481_call(), 0)
uop_503 = relay.sqrt(call_498.astype('float32')) # shape=(14, 2, 8)
uop_505 = relay.sqrt(call_499.astype('float32')) # shape=(14, 2, 8)
func_171_call = mod.get_global_var('func_171')
func_173_call = mutated_mod.get_global_var('func_173')
call_508 = relay.TupleGetItem(func_171_call(), 0)
call_509 = relay.TupleGetItem(func_173_call(), 0)
bop_510 = relay.multiply(call_508.astype('uint32'), relay.reshape(uop_503.astype('uint32'), relay.shape_of(call_508))) # shape=(14, 2, 8)
bop_513 = relay.multiply(call_509.astype('uint32'), relay.reshape(uop_505.astype('uint32'), relay.shape_of(call_509))) # shape=(14, 2, 8)
uop_538 = relay.sinh(bop_510.astype('float32')) # shape=(14, 2, 8)
uop_540 = relay.sinh(bop_513.astype('float32')) # shape=(14, 2, 8)
output = uop_538
output2 = uop_540
func_543 = relay.Function([], output)
mod['func_543'] = func_543
mod = relay.transform.InferType()(mod)
mutated_mod['func_543'] = func_543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_543_call = mutated_mod.get_global_var('func_543')
call_544 = func_543_call()
output = call_544
func_545 = relay.Function([], output)
mutated_mod['func_545'] = func_545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_479_call = mod.get_global_var('func_479')
func_481_call = mutated_mod.get_global_var('func_481')
call_549 = relay.TupleGetItem(func_479_call(), 0)
call_550 = relay.TupleGetItem(func_481_call(), 0)
output = call_549
output2 = call_550
func_561 = relay.Function([], output)
mod['func_561'] = func_561
mod = relay.transform.InferType()(mod)
mutated_mod['func_561'] = func_561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_561_call = mutated_mod.get_global_var('func_561')
call_562 = func_561_call()
output = call_562
func_563 = relay.Function([], output)
mutated_mod['func_563'] = func_563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_171_call = mod.get_global_var('func_171')
func_173_call = mutated_mod.get_global_var('func_173')
call_585 = relay.TupleGetItem(func_171_call(), 0)
call_586 = relay.TupleGetItem(func_173_call(), 0)
output = call_585
output2 = call_586
func_590 = relay.Function([], output)
mod['func_590'] = func_590
mod = relay.transform.InferType()(mod)
output = func_590()
func_591 = relay.Function([], output)
mutated_mod['func_591'] = func_591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_561_call = mod.get_global_var('func_561')
func_563_call = mutated_mod.get_global_var('func_563')
call_606 = func_561_call()
call_607 = func_561_call()
var_620 = relay.var("var_620", dtype = "float64", shape = (14, 2, 8))#candidate|620|(14, 2, 8)|var|float64
bop_621 = relay.floor_mod(call_606.astype('float32'), relay.reshape(var_620.astype('float32'), relay.shape_of(call_606))) # shape=(14, 2, 8)
bop_624 = relay.floor_mod(call_607.astype('float32'), relay.reshape(var_620.astype('float32'), relay.shape_of(call_607))) # shape=(14, 2, 8)
output = relay.Tuple([bop_621,])
output2 = relay.Tuple([bop_624,])
func_627 = relay.Function([var_620,], output)
mod['func_627'] = func_627
mod = relay.transform.InferType()(mod)
mutated_mod['func_627'] = func_627
mutated_mod = relay.transform.InferType()(mutated_mod)
var_628 = relay.var("var_628", dtype = "float64", shape = (14, 2, 8))#candidate|628|(14, 2, 8)|var|float64
func_627_call = mutated_mod.get_global_var('func_627')
call_629 = func_627_call(var_628)
output = call_629
func_630 = relay.Function([var_628], output)
mutated_mod['func_630'] = func_630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_171_call = mod.get_global_var('func_171')
func_173_call = mutated_mod.get_global_var('func_173')
call_648 = relay.TupleGetItem(func_171_call(), 1)
call_649 = relay.TupleGetItem(func_173_call(), 1)
output = call_648
output2 = call_649
func_657 = relay.Function([], output)
mod['func_657'] = func_657
mod = relay.transform.InferType()(mod)
output = func_657()
func_658 = relay.Function([], output)
mutated_mod['func_658'] = func_658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_171_call = mod.get_global_var('func_171')
func_173_call = mutated_mod.get_global_var('func_173')
call_686 = relay.TupleGetItem(func_171_call(), 2)
call_687 = relay.TupleGetItem(func_173_call(), 2)
func_171_call = mod.get_global_var('func_171')
func_173_call = mutated_mod.get_global_var('func_173')
call_689 = relay.TupleGetItem(func_171_call(), 0)
call_690 = relay.TupleGetItem(func_173_call(), 0)
func_264_call = mod.get_global_var('func_264')
func_266_call = mutated_mod.get_global_var('func_266')
call_694 = relay.TupleGetItem(func_264_call(relay.reshape(call_689.astype('float64'), [14, 2, 8])), 0)
call_695 = relay.TupleGetItem(func_266_call(relay.reshape(call_689.astype('float64'), [14, 2, 8])), 0)
func_201_call = mod.get_global_var('func_201')
func_203_call = mutated_mod.get_global_var('func_203')
call_697 = relay.TupleGetItem(func_201_call(relay.reshape(call_689.astype('float64'), [14, 2, 8])), 0)
call_698 = relay.TupleGetItem(func_203_call(relay.reshape(call_689.astype('float64'), [14, 2, 8])), 0)
func_479_call = mod.get_global_var('func_479')
func_481_call = mutated_mod.get_global_var('func_481')
call_708 = relay.TupleGetItem(func_479_call(), 0)
call_709 = relay.TupleGetItem(func_481_call(), 0)
func_657_call = mod.get_global_var('func_657')
func_658_call = mutated_mod.get_global_var('func_658')
call_710 = func_657_call()
call_711 = func_657_call()
func_657_call = mod.get_global_var('func_657')
func_658_call = mutated_mod.get_global_var('func_658')
call_715 = func_657_call()
call_716 = func_657_call()
output = relay.Tuple([call_686,call_689,call_694,call_697,call_708,call_710,call_715,])
output2 = relay.Tuple([call_687,call_690,call_695,call_698,call_709,call_711,call_716,])
func_721 = relay.Function([], output)
mod['func_721'] = func_721
mod = relay.transform.InferType()(mod)
output = func_721()
func_722 = relay.Function([], output)
mutated_mod['func_722'] = func_722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_721_call = mod.get_global_var('func_721')
func_722_call = mutated_mod.get_global_var('func_722')
call_771 = relay.TupleGetItem(func_721_call(), 0)
call_772 = relay.TupleGetItem(func_722_call(), 0)
func_543_call = mod.get_global_var('func_543')
func_545_call = mutated_mod.get_global_var('func_545')
call_795 = func_543_call()
call_796 = func_543_call()
output = relay.Tuple([call_771,call_795,])
output2 = relay.Tuple([call_772,call_796,])
func_813 = relay.Function([], output)
mod['func_813'] = func_813
mod = relay.transform.InferType()(mod)
output = func_813()
func_814 = relay.Function([], output)
mutated_mod['func_814'] = func_814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_479_call = mod.get_global_var('func_479')
func_481_call = mutated_mod.get_global_var('func_481')
call_874 = relay.TupleGetItem(func_479_call(), 0)
call_875 = relay.TupleGetItem(func_481_call(), 0)
func_479_call = mod.get_global_var('func_479')
func_481_call = mutated_mod.get_global_var('func_481')
call_882 = relay.TupleGetItem(func_479_call(), 0)
call_883 = relay.TupleGetItem(func_481_call(), 0)
func_366_call = mod.get_global_var('func_366')
func_368_call = mutated_mod.get_global_var('func_368')
call_885 = relay.TupleGetItem(func_366_call(relay.reshape(call_882.astype('float64'), [224,])), 2)
call_886 = relay.TupleGetItem(func_368_call(relay.reshape(call_882.astype('float64'), [224,])), 2)
output = relay.Tuple([call_874,call_882,call_885,])
output2 = relay.Tuple([call_875,call_883,call_886,])
func_895 = relay.Function([], output)
mod['func_895'] = func_895
mod = relay.transform.InferType()(mod)
output = func_895()
func_896 = relay.Function([], output)
mutated_mod['func_896'] = func_896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_590_call = mod.get_global_var('func_590')
func_591_call = mutated_mod.get_global_var('func_591')
call_900 = func_590_call()
call_901 = func_590_call()
output = call_900
output2 = call_901
func_918 = relay.Function([], output)
mod['func_918'] = func_918
mod = relay.transform.InferType()(mod)
output = func_918()
func_919 = relay.Function([], output)
mutated_mod['func_919'] = func_919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_895_call = mod.get_global_var('func_895')
func_896_call = mutated_mod.get_global_var('func_896')
call_929 = relay.TupleGetItem(func_895_call(), 2)
call_930 = relay.TupleGetItem(func_896_call(), 2)
output = relay.Tuple([call_929,])
output2 = relay.Tuple([call_930,])
func_937 = relay.Function([], output)
mod['func_937'] = func_937
mod = relay.transform.InferType()(mod)
mutated_mod['func_937'] = func_937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_937_call = mutated_mod.get_global_var('func_937')
call_938 = func_937_call()
output = call_938
func_939 = relay.Function([], output)
mutated_mod['func_939'] = func_939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_543_call = mod.get_global_var('func_543')
func_545_call = mutated_mod.get_global_var('func_545')
call_946 = func_543_call()
call_947 = func_543_call()
var_959 = relay.var("var_959", dtype = "float32", shape = (14, 2, 8))#candidate|959|(14, 2, 8)|var|float32
bop_960 = relay.logical_and(call_946.astype('bool'), relay.reshape(var_959.astype('bool'), relay.shape_of(call_946))) # shape=(14, 2, 8)
bop_963 = relay.logical_and(call_947.astype('bool'), relay.reshape(var_959.astype('bool'), relay.shape_of(call_947))) # shape=(14, 2, 8)
func_479_call = mod.get_global_var('func_479')
func_481_call = mutated_mod.get_global_var('func_481')
call_975 = relay.TupleGetItem(func_479_call(), 0)
call_976 = relay.TupleGetItem(func_481_call(), 0)
output = relay.Tuple([bop_960,call_975,])
output2 = relay.Tuple([bop_963,call_976,])
func_1009 = relay.Function([var_959,], output)
mod['func_1009'] = func_1009
mod = relay.transform.InferType()(mod)
var_1010 = relay.var("var_1010", dtype = "float32", shape = (14, 2, 8))#candidate|1010|(14, 2, 8)|var|float32
output = func_1009(var_1010)
func_1011 = relay.Function([var_1010], output)
mutated_mod['func_1011'] = func_1011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_561_call = mod.get_global_var('func_561')
func_563_call = mutated_mod.get_global_var('func_563')
call_1035 = func_561_call()
call_1036 = func_561_call()
output = call_1035
output2 = call_1036
func_1037 = relay.Function([], output)
mod['func_1037'] = func_1037
mod = relay.transform.InferType()(mod)
mutated_mod['func_1037'] = func_1037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1037_call = mutated_mod.get_global_var('func_1037')
call_1038 = func_1037_call()
output = call_1038
func_1039 = relay.Function([], output)
mutated_mod['func_1039'] = func_1039
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1046 = relay.var("var_1046", dtype = "float64", shape = (14, 1, 8))#candidate|1046|(14, 1, 8)|var|float64
uop_1047 = relay.rsqrt(var_1046.astype('float64')) # shape=(14, 1, 8)
func_264_call = mod.get_global_var('func_264')
func_266_call = mutated_mod.get_global_var('func_266')
var_1051 = relay.var("var_1051", dtype = "float64", shape = (224,))#candidate|1051|(224,)|var|float64
call_1050 = relay.TupleGetItem(func_264_call(relay.reshape(var_1051.astype('float64'), [14, 2, 8])), 0)
call_1052 = relay.TupleGetItem(func_266_call(relay.reshape(var_1051.astype('float64'), [14, 2, 8])), 0)
func_414_call = mod.get_global_var('func_414')
func_416_call = mutated_mod.get_global_var('func_416')
var_1054 = relay.var("var_1054", dtype = "float64", shape = (1024,))#candidate|1054|(1024,)|var|float64
call_1053 = func_414_call(relay.reshape(var_1054.astype('float64'), [16, 8, 8]))
call_1055 = func_414_call(relay.reshape(var_1054.astype('float64'), [16, 8, 8]))
output = relay.Tuple([uop_1047,call_1050,var_1051,call_1053,var_1054,])
output2 = relay.Tuple([uop_1047,call_1052,var_1051,call_1055,var_1054,])
func_1059 = relay.Function([var_1046,var_1051,var_1054,], output)
mod['func_1059'] = func_1059
mod = relay.transform.InferType()(mod)
var_1060 = relay.var("var_1060", dtype = "float64", shape = (14, 1, 8))#candidate|1060|(14, 1, 8)|var|float64
var_1061 = relay.var("var_1061", dtype = "float64", shape = (224,))#candidate|1061|(224,)|var|float64
var_1062 = relay.var("var_1062", dtype = "float64", shape = (1024,))#candidate|1062|(1024,)|var|float64
output = func_1059(var_1060,var_1061,var_1062,)
func_1063 = relay.Function([var_1060,var_1061,var_1062,], output)
mutated_mod['func_1063'] = func_1063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_479_call = mod.get_global_var('func_479')
func_481_call = mutated_mod.get_global_var('func_481')
call_1070 = relay.TupleGetItem(func_479_call(), 0)
call_1071 = relay.TupleGetItem(func_481_call(), 0)
output = relay.Tuple([call_1070,])
output2 = relay.Tuple([call_1071,])
func_1085 = relay.Function([], output)
mod['func_1085'] = func_1085
mod = relay.transform.InferType()(mod)
mutated_mod['func_1085'] = func_1085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1085_call = mutated_mod.get_global_var('func_1085')
call_1086 = func_1085_call()
output = call_1086
func_1087 = relay.Function([], output)
mutated_mod['func_1087'] = func_1087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_561_call = mod.get_global_var('func_561')
func_563_call = mutated_mod.get_global_var('func_563')
call_1090 = func_561_call()
call_1091 = func_561_call()
uop_1098 = relay.atan(call_1090.astype('float64')) # shape=(14, 2, 8)
uop_1100 = relay.atan(call_1091.astype('float64')) # shape=(14, 2, 8)
func_464_call = mod.get_global_var('func_464')
func_469_call = mutated_mod.get_global_var('func_469')
const_1107 = relay.const([[9.821331,-1.691437],[9.629926,4.411636],[-2.523400,9.499595],[-7.980175,8.485517],[-8.975297,3.351014],[7.284469,7.037308],[9.062354,9.125316],[8.888104,0.610605],[-6.397491,-3.015653],[7.713668,1.344778],[-9.989392,-3.236181],[4.471719,2.427341],[8.938417,-7.248813],[-6.184535,-9.671489],[-8.015497,5.214632],[-8.193075,-0.765560],[1.828239,-0.209586],[-9.830523,-4.300434],[-3.385085,3.594608],[-4.662502,4.673874],[3.342554,-6.887525],[0.655225,-6.181824],[1.634610,7.129709],[-1.089754,-4.792782],[3.122030,-5.629283],[-4.222663,-1.092354],[1.948725,-7.141650],[-9.080202,-3.012579],[3.508170,6.404806],[2.526820,-2.219948],[-1.946754,-9.683338],[7.721547,-5.536961],[6.704610,-0.617271],[2.953598,6.436508],[-2.845942,-3.699006],[8.838561,1.855527],[-5.377797,-2.780289],[-3.385306,-4.782545],[-8.321836,1.025071],[7.946430,-3.610375],[-5.356400,0.631088],[5.275789,-3.166296],[-4.056595,5.540973],[8.936814,6.224847],[9.931180,1.662215],[-1.307927,-8.718712],[-0.581872,3.816647],[2.367796,0.603089],[-7.172574,5.347019],[8.665936,-5.035118],[3.135658,9.650734],[-8.846528,-0.627568],[-9.121375,5.420104],[2.642838,-6.375013],[7.639577,0.329489],[6.064152,-4.801240],[6.130032,-0.788053],[7.687546,4.414095],[-0.177946,-7.723870],[9.522574,-2.985175]], dtype = "float32")#candidate|1107|(60, 2)|const|float32
var_1108 = relay.var("var_1108", dtype = "int16", shape = (154,))#candidate|1108|(154,)|var|int16
var_1109 = relay.var("var_1109", dtype = "uint64", shape = (2816,))#candidate|1109|(2816,)|var|uint64
call_1106 = relay.TupleGetItem(func_464_call(relay.reshape(const_1107.astype('float32'), [15, 1, 8]), relay.reshape(var_1108.astype('int16'), [154,]), relay.reshape(var_1109.astype('uint64'), [2816,]), ), 0)
call_1110 = relay.TupleGetItem(func_469_call(relay.reshape(const_1107.astype('float32'), [15, 1, 8]), relay.reshape(var_1108.astype('int16'), [154,]), relay.reshape(var_1109.astype('uint64'), [2816,]), ), 0)
output = relay.Tuple([uop_1098,call_1106,const_1107,var_1108,var_1109,])
output2 = relay.Tuple([uop_1100,call_1110,const_1107,var_1108,var_1109,])
func_1112 = relay.Function([var_1108,var_1109,], output)
mod['func_1112'] = func_1112
mod = relay.transform.InferType()(mod)
var_1113 = relay.var("var_1113", dtype = "int16", shape = (154,))#candidate|1113|(154,)|var|int16
var_1114 = relay.var("var_1114", dtype = "uint64", shape = (2816,))#candidate|1114|(2816,)|var|uint64
output = func_1112(var_1113,var_1114,)
func_1115 = relay.Function([var_1113,var_1114,], output)
mutated_mod['func_1115'] = func_1115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_171_call = mod.get_global_var('func_171')
func_173_call = mutated_mod.get_global_var('func_173')
call_1135 = relay.TupleGetItem(func_171_call(), 1)
call_1136 = relay.TupleGetItem(func_173_call(), 1)
func_264_call = mod.get_global_var('func_264')
func_266_call = mutated_mod.get_global_var('func_266')
const_1160 = relay.const([-6.942215,-2.542633,9.414011,3.220988,-9.437975,2.449202,7.556187,9.382341,2.251284,5.373804,-1.445560,2.591975,0.935811,-4.080340,6.793190,0.701845,5.878419,-8.171495,-2.165270,4.753601,-3.985881,0.160729,-9.087200,4.829187,-7.951437,-5.834017,6.893824,-5.878068,2.565165,8.680422,8.307246,-6.614954,-3.451462,8.966674,9.057833,5.827289,7.200893,6.481387,8.433226,-0.035268,0.297912,9.035581,-5.705875,2.006735,-9.774511,9.756975,-3.566885,-3.397784,-3.644228,2.930745,0.662303,1.638210,3.700396,-1.042723,-0.801465,3.982405,-5.481406,-6.796970,-3.559118,-0.610352,-1.044659,9.420191,-2.846824,3.779949,1.913407,-4.133260,5.610714,-0.721188,-9.227878,4.772363,9.470563,2.282171,6.160206,-6.119109,5.206915,-3.246985,-0.046349,-0.710616,-1.022582,-9.216468,7.414572,-1.540591,-7.355004,3.906813,0.142614,2.318001,0.830467,-6.094394,-0.352260,0.682794,-2.054553,2.054764,0.569096,1.281724,1.652451,4.883847,-7.186016,2.368850,-8.210559,5.786557,-3.192636,-3.736221,2.266417,-6.733867,-2.019016,-6.981687,-8.942509,5.852579,0.297292,9.961503,-5.625516,8.190350,-0.844861,-2.546950,-5.720161,-8.743001,-0.641542,-6.805595,-4.183470,-2.619772,-1.722097,9.490903,-0.717025,-6.701032,7.633164,6.532443,7.849572,-9.395999,0.907067,-3.038586,-2.989460,-5.577765,-3.146619,0.351049,-4.444854,5.706715,-3.205954,0.190934,5.677288,-0.080096,0.225995,8.136792,1.621526,-4.350551,-6.266969,-7.690879,2.951656,9.378222,5.394151,-2.893803,-7.931240,5.692415,-5.364479,-0.247686,-1.099691,-1.356136,-0.638496,-4.116039,9.902925,-1.069937,-2.171028,1.744051,-8.097924,2.891330,6.791889,2.378284,3.109043,-4.103221,3.530490,9.543735,1.679445,9.771827,2.187045,2.496276,-5.206165,-3.628037,-2.319708,-8.987922,0.338306,4.741058,-5.287963,-4.662350,5.080377,7.694524,7.711674,-7.735703,8.382727,-3.441607,-4.981833,4.173341,-2.841330,0.155653,5.078718,6.243978,1.958429,8.243713,9.463528,1.329711,-0.357665,6.862819,5.582008,6.214435,8.523858,-9.588092,7.285945,-6.945418,2.569011,9.928190,8.836561,5.309179,6.685224,-3.763331,3.243244,8.235297,7.241045,1.045076,-2.129464,2.253969,5.823895,6.575687,4.304492,-6.421470,2.330982,-9.171300], dtype = "float64")#candidate|1160|(224,)|const|float64
call_1159 = relay.TupleGetItem(func_264_call(relay.reshape(const_1160.astype('float64'), [14, 2, 8])), 0)
call_1161 = relay.TupleGetItem(func_266_call(relay.reshape(const_1160.astype('float64'), [14, 2, 8])), 0)
func_1085_call = mod.get_global_var('func_1085')
func_1087_call = mutated_mod.get_global_var('func_1087')
call_1173 = relay.TupleGetItem(func_1085_call(), 0)
call_1174 = relay.TupleGetItem(func_1087_call(), 0)
func_918_call = mod.get_global_var('func_918')
func_919_call = mutated_mod.get_global_var('func_919')
call_1180 = func_918_call()
call_1181 = func_918_call()
output = relay.Tuple([call_1135,call_1159,const_1160,call_1173,call_1180,])
output2 = relay.Tuple([call_1136,call_1161,const_1160,call_1174,call_1181,])
func_1196 = relay.Function([], output)
mod['func_1196'] = func_1196
mod = relay.transform.InferType()(mod)
output = func_1196()
func_1197 = relay.Function([], output)
mutated_mod['func_1197'] = func_1197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1037_call = mod.get_global_var('func_1037')
func_1039_call = mutated_mod.get_global_var('func_1039')
call_1226 = func_1037_call()
call_1227 = func_1037_call()
func_721_call = mod.get_global_var('func_721')
func_722_call = mutated_mod.get_global_var('func_722')
call_1242 = relay.TupleGetItem(func_721_call(), 0)
call_1243 = relay.TupleGetItem(func_722_call(), 0)
output = relay.Tuple([call_1226,call_1242,])
output2 = relay.Tuple([call_1227,call_1243,])
func_1259 = relay.Function([], output)
mod['func_1259'] = func_1259
mod = relay.transform.InferType()(mod)
output = func_1259()
func_1260 = relay.Function([], output)
mutated_mod['func_1260'] = func_1260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_721_call = mod.get_global_var('func_721')
func_722_call = mutated_mod.get_global_var('func_722')
call_1332 = relay.TupleGetItem(func_721_call(), 4)
call_1333 = relay.TupleGetItem(func_722_call(), 4)
func_264_call = mod.get_global_var('func_264')
func_266_call = mutated_mod.get_global_var('func_266')
call_1351 = relay.TupleGetItem(func_264_call(relay.reshape(call_1332.astype('float64'), [14, 2, 8])), 0)
call_1352 = relay.TupleGetItem(func_266_call(relay.reshape(call_1332.astype('float64'), [14, 2, 8])), 0)
output = relay.Tuple([call_1332,call_1351,])
output2 = relay.Tuple([call_1333,call_1352,])
func_1385 = relay.Function([], output)
mod['func_1385'] = func_1385
mod = relay.transform.InferType()(mod)
mutated_mod['func_1385'] = func_1385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1385_call = mutated_mod.get_global_var('func_1385')
call_1386 = func_1385_call()
output = call_1386
func_1387 = relay.Function([], output)
mutated_mod['func_1387'] = func_1387
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1399 = relay.var("var_1399", dtype = "float32", shape = (12, 1, 5))#candidate|1399|(12, 1, 5)|var|float32
uop_1400 = relay.acos(var_1399.astype('float32')) # shape=(12, 1, 5)
func_171_call = mod.get_global_var('func_171')
func_173_call = mutated_mod.get_global_var('func_173')
call_1402 = relay.TupleGetItem(func_171_call(), 0)
call_1403 = relay.TupleGetItem(func_173_call(), 0)
output = relay.Tuple([uop_1400,call_1402,])
output2 = relay.Tuple([uop_1400,call_1403,])
func_1406 = relay.Function([var_1399,], output)
mod['func_1406'] = func_1406
mod = relay.transform.InferType()(mod)
var_1407 = relay.var("var_1407", dtype = "float32", shape = (12, 1, 5))#candidate|1407|(12, 1, 5)|var|float32
output = func_1406(var_1407)
func_1408 = relay.Function([var_1407], output)
mutated_mod['func_1408'] = func_1408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_590_call = mod.get_global_var('func_590')
func_591_call = mutated_mod.get_global_var('func_591')
call_1413 = func_590_call()
call_1414 = func_590_call()
uop_1416 = relay.cos(call_1413.astype('float64')) # shape=(14, 2, 8)
uop_1418 = relay.cos(call_1414.astype('float64')) # shape=(14, 2, 8)
output = uop_1416
output2 = uop_1418
func_1431 = relay.Function([], output)
mod['func_1431'] = func_1431
mod = relay.transform.InferType()(mod)
mutated_mod['func_1431'] = func_1431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1431_call = mutated_mod.get_global_var('func_1431')
call_1432 = func_1431_call()
output = call_1432
func_1433 = relay.Function([], output)
mutated_mod['func_1433'] = func_1433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mod.get_global_var('func_918')
func_919_call = mutated_mod.get_global_var('func_919')
call_1578 = func_918_call()
call_1579 = func_918_call()
func_128_call = mod.get_global_var('func_128')
func_131_call = mutated_mod.get_global_var('func_131')
var_1588 = relay.var("var_1588", dtype = "int16", shape = (154,))#candidate|1588|(154,)|var|int16
const_1589 = relay.const([-3,-5,3,3,10,-10,-6,-5,-7,-6,4,-4,6,8,-1,8,9,-6,9,-10,5,-6,-9,9,-1,-4,6,10,3,2,5,7,5,10,3,3,-8,-10,-1,-6,4,7,-7,10,5,6,-1,-5,6,-10,-5,-8,5,-3,-7,-9,6,-10,7,5,-3,-3,1,1,-5,-6,-8,-5,-2,-9,5,1,8,-6,-3,-6,-1,-9,6,2,4,2,-4,-7,3,-7,-6,4,2,-8,1,9,2,6,1,9,-8,9,8,-8,10,3,-4,1,-7,10,4,1,7,-5,-5,-6,-5,-3,-9,-6,-8,6,-6,-7,7,-10,-7,8,-8,4,7,-6,-3,7,-2,2,4,2,-6,-2,6,-5,-2,-7,-5,-4,1,7,9,-7,-9,-10,4,4,1,-2,-7,-2,-9,1,-1,10,-5,5,3,6,10,6,10,-5,-5,9,-3,4,9,-10,10,-10,7,2,9,1,-6,5,-8,-6,-7,-4,4,-4,3,3,6,-2,-3,2,-2,3,-1,-1,-7,9,-2,4,-2,10,6,3,-9,2,7,5,-6,-7,-7,5,5,-7,10,-4,-4,10,-10,-10,5,-4,-6,4,-7,3,9,-9,-4,1,10,6,2,3,-10,4,7,-10,4,6,-2,7,-7,-6,-3,-4,-6,8,-10,-1,-4,-6,10,-3,-7,-8,-10,-2,1,7,-9,-8,3,3,7,-2,9,-3,1,5,-6,10,-10,-10,-2,-7,-8,-6,-1,4,2,-8,-5,10,-6,5,8,6,10,8,-5,-5,-10,-5,9,-6,7,-2,6,10,6,3,-3,-9,9,6,-2,8,-1,10,4,3,-3,-6,8,2,1,6,-6,-6,-6,-10,3,-10,-1,-6,-10,8,5,-2,-2,-5,-10,9,-9,3,-9,-4,1,9,-4,-8,-6,-8,4,4,-4,9,3,2,-2,7,-7,6,-5,-1,1,-5,-8,10,3,-6,-6,-3,-4,10,9,9,-8,-6,-9,-4,-6,1,-10,-6,8,1,8,10,-6,-7,-10,3,-1,-3,-5,5,5,-5,-9,-9,-4,1,-2,-3,-3,-5,9,3,4,4,-4,-1,7,4,-9,-4,-3,5,8,-6,-8,-6,-7,-9,-6,2,-2,-8,3,6,7,2,-5,-7,-5,-3,-4,-2,-9,-3,5,-6,-2,-7,-8,-4,-3,7,5,2,-9,-3,-6,-5,7,10,5,1,10,-2,-3,5,5,5,-10,-8,-1,-3,9,2,7,-9,9,2,10,-8,-10,-10,-5,-3,-5,3,5,5,-5,9,10,-6,10,8,2,4,9,7,2,-10,-2,-2,-10,-10,-3,-8,-8,2,4,7,-6,-10,-6,10,8,6,-2,8,5,-10,6,1,-4,-2,-3,-6,2,1,-4,10,10,3,-2,7,-8,8,-4,-10,2,-7,-2,1,9,-4,4,5,7,5,1,-1,-8,7,-7,-8,-8,3,8,-6,5,-9,3,2,-6,-3,10,5,2,10,8,8,5,-8,3,-9,5,1,4,1,-2,-6,-10,-2,3,-2,10,-9,-1,-7,4,-5,5,-8,-9,10,3,6,7,6,10,2,-7,-6,-9,-5,8,-3,-5,-4,10,-10,10,-8,3,-6,3,-4,1,1,10,5,5,5,-9,-6,2,1,3,-8,5,-9,6,-9,1,8,-5,3,1,1,6,-8,-5,-2,-10,5,8,4,-7,-8,-4,-2,-9,10,-5,-1,-10,1,2,4,-6,7,-2,8,5,-10,2,9,-10,-5,-4,6,-7,-9,-2,1,3,4,1,7,-7,5,10,3,7,-3,-6,2,5,2,-6,7,-3,5,2,7,8,9,8,-5,9,5,-6,9,-10,-3,6,-8,-1,-2,-6,2,-3,-3,2,9,6,9,10,-7,10,1,-10,-6,5,-7,1,6,-10,-6,-6,8,-8,8,-6,2,-7,-4,3,9,10,-10,5,4,6,-2,6,6,8,5,9,9,-10,2,-5,-5,8,7,-3,3,-2,2,6,5,2,-5,7,8,9,3,4,10,-5,-7,9,-8,6,10,-7,-3,4,1,-4,-9,8,8,3,-4,-4,-5,-3,-3,-2,-1,9,-10,-4,4,-10,2,8,10,7,-8,-8,-5,7,-10,-2,-9,-6,3,10,7,-4,-9,-10,-4,4,-9,6,-3,-1,-3,5,1,-3,-9,-4,4,-9,10,2,6,7,-10,9,-7,8,1,-4,-3,9,-3,-2,4,-1,-9,-10,1,-2,10,6,-2,-9,-6,-7,1,2,-2,-2,4,-3,-6,-9,10,-10,5,-8,-10,1,-10,-6,-6,-7,-3,-7,2,-1,2,-7,-3,1,-5,-4,7,-1,-4,2,-5,2,-9,4,-10,-2,-7,3,8,-10,6,-5,9,-2,3,7,-2,-4,10,2,5,2,-5,-1,-2,3,5,1,-6,-1,6,6,8,10,-10,-10,8,-6,-1,-5,8,-1,8,8,-6,4,8,-3,-2,6,7,6,10,-8,8,1,1,-10,-5,-6,9,4,-10,4,8,-5,-6,10,-2,4,-4,-8,9,6,6,7,-2,3,-8,5,6,10,-10,7,-3,-1,-8,-1,-7,-2,-1,-8,-10,6,-9,3,-8,5,-7,1,3,-4,3,9,4,-2,-2,9,-5,-9,3,-8,-7,10,-7,-2,5,3,-5,5,-6,6,1,-10,-10,9,-1,8,-3,-1,-9,3,3,1,2,7,5,6,1,-2,-6,-6,-1,-6,3,7,4,-8,-9,5,5,7,-9,7,2,-1,-4,7,9,2,-5,-4,10,-8,-10,-10,6,6,2,-5,5,-3,3,6,7,6,10,1,-1,-1,-3,-6,8,-6,5,5,9,1,-9,-6,9,-8,-1,1,9,2,10,-1,-8,-9,10,3,3,1,-2,-10,-8,-10,-1,-10,-10,2,-8,10,-2,9,6,-9,-7,-3,-9,8,3,-6,-8,5,-7,-9,2,3,2,-3,-5,5,5,8,3,9,5,-2,-2,-2,4,7,3,-9,1,1,-4,-5,8,-3,1,-7,-9,-9,6,3,-3,7,8,10,7,5,-10,2,-4,-9,9,1,-6,1,4,-5,4,-6,9,-2,-9,-2,5,-9,9,4,-5,-7,9,-5,4,3,-4,-8,5,1,-7,3,7,3,-9,5,3,-4,-2,5,-3,-3,7,1,-1,4,-5,2,-10,-9,1,2,10,6,9,7,2,-8,-1,-1,-1,-4,3,-10,8,-3,-5,-3,-2,-6,-4,2,5,5,1,2,-2,-10,-10,-9,2,-9,6,4,3,-9,-5,3,3,7,5,-7,6,1,10,8,1,-10,1,4,-4,-3,6,-8,-3,2,-6,4,-6,2,6,-7,9,-5,-9,-6,-4,1,-4,-10,6,8,2,-8,8,4,1,-4,-9,3,-10,3,8,7,-5,-3,-10,4,3,-10,-1,-7,-8,-5,2,6,-6,7,5,10,-10,8,3,9,4,-9,6,1,6,2,3,9,9,5,-9,-1,-7,-8,2,8,-9,-5,2,-8,2,-8,9,4,3,-9,4,3,8,-2,1,6,-7,-4,7,-9,3,1,3,8,-5,-10,7,-8,5,5,2,-5,-4,-7,-2,-7,-2,-6,6,-2,-3,9,8,-4,9,-10,-5,-9,-3,-10,-3,-9,-7,-3,-1,5,-9,-3,-2,-1,-10,-2,-5,4,7,2,-2,6,-8,-4,4,-2,-2,2,-3,6,6,-8,9,1,-5,6,6,7,-1,-4,10,9,-2,-7,6,8,-1,2,-10,6,8,3,5,9,-10,-10,8,4,10,4,-7,7,1,-10,4,4,-7,5,6,-8,6,9,-7,1,8,-3,-10,-5,-2,1,10,-8,-4,-8,9,-9,4,-9,4,-8,7,-7,2,7,-6,9,-4,2,-2,-10,-6,5,10,-1,-6,-7,10,2,-8,3,-7,-10,1,-3,-4,-3,-4,2,-6,8,-4,7,-1,-6,-7,-4,5,-9,8,9,-3,-4,-5,-10,-3,-3,3,3,-6,-2,-1,-9,-2,1,8,-4,2,-9,8,6,-8,-8,-8,5,-1,-8,5,7,6,9,-7,9,5,-6,7,-4,-2,4,-5,-5,7,-7,1,-10,-3,4,-6,-9,9,3,9,1,-2,-1,-5,1,10,-4,3,1,-7,-6,-6,-1,2,10,-3,-3,7,10,-2,6,1,4,-6,-2,10,3,4,-10,1,-8,-3,7,-4,-6,10,-8,-1,-8,9,-9,9,2,9,-2,6,-3,8,10,9,-8,-7,-1,-1,7,-1,7,-2,5,-5,-2,-4,9,-6,-6,7,5,10,-6,7,1,4,7,-8,-7,-9,1,7,7,-1,10,7,-3,3,10,-3,-7,-8,2,1,7,2,5,-8,-3,-7,6,-10,3,-8,-5,-3,-7,9,6,-1,-9,-1,-10,-9,9,-8,10,-3,1,-7,4,9,10,1,7,9,4,-10,-10,-9,-5,-3,5,9,9,2,-7,-5,8,-10,-1,-1,-8,1,-2,-6,-9,3,7,2,9,1,5,-2,5,10,-3,-1,3,-1,-4,1,6,-7,-7,2,3,1,-1,-10,5,10,-10,8,-3,-6,6,10,3,-8,8,-6,3,-8,-2,-1,-10,-4,-4,-4,3,-5,1,-10,7,-5,-10,-8,10,-9,6,-9,5,-9,-6,-7,4,8,9,10,-8,1,-5,10,4,-8,-1,9,10,4,-2,7,-3,1,-4,8,-7,-9,5,-8,3,1,4,-10,7,-10,-7,5,3,1,-9,9,-7,8,10,-3,5,6,2,-4,4,-8,-3,2,-10,-1,-2,-5,-9,-3,1,1,-7,-5,-3,-10,3,7,-2,9,-1,-1,1,4,-10,-10,-10,-9,5,10,3,4,-9,-1,1,-2,-4,-7,-2,-6,5,-7,4,6,2,-9,5,10,-6,6,4,-10,-5,-3,6,-1,-5,10,4,9,3,10,3,3,-4,-7,-10,-5,5,-2,-7,-4,1,2,-1,1,10,3,3,5,6,6,-10,-1,-10,6,7,-10,7,4,-6,3,8,9,1,-9,-7,-2,-5,-2,5,-2,9,1,-7,-3,1,9,1,1,4,-6,4,-8,1,5,7,10,-3,-1,7,-3,1,6,-10,3,-6,4,8,-2,-9,7,-6,1,10,-8,-5,5,-3,-9,7,-8,10,-6,4,-7,5,-1,1,-10,6,-7,-1,9,3,-8,8,7,9,-8,1,10,-9,9,-4,2,1,1,10,-7,-5,-5,-2,-3,-4,-6,6,3,6,7,2,-10,-9,-4,-10,-3,-5,-10,-1,-8,3,1,7,-9,7,2,7,4,-2,6,9,-7,-8,-3,-9,3,2,-5,10,-1,10,-10,-7,3,-5,1,10,10,4,-6,-2,-9,7,-3,-8,7,2,-6,-2,-8,10,10,-7,8,4,6,-7,2,1,-10,-2,6,4,2,-1,-10,-10,-10,3,-10,-4,-4,-3,2,4,2,10,-1,-2,-10,-3,-3,-3,10,3,-4,8,5,-6,5,2,5,7,-6,-9,1,9,5,-9,9,-8,-6,-10,-8,-9,-6,2,2,-9,8,7,2,-3,7,3,-3,-10,7,-1,8,-10,10,-8,-1,3,7,-1,5,5,8,-1,-8,10,-10,-10,1,-5,-2,-5,9,6,-9,4,-1,-9,6,-9,-8,-2,10,-9,2,1,-6,-10,-4,3,-3,9,-6,2,8,-6,10,9,10,10,1,-9,-8,3,5,-9,-3,-4,-7,-10,-8,3,4,10,9,7,3,-8,5,5,9,2,-2,-10,-3,-6,-7,-2,3,5,4,-4,10,-8,-3,-6,-6,-4,-5,9,-7,8,6,-4,-2,2,3,-2,8,-7,-4,-5,3,1,6,-5,-7,-6,5,-3,-9,4,1,-4,-8,9,-5,-2,-6,6,3,6,4,-4,-1,7,-1,3,-9,-8,7,-10,-6,9,-7,7,-6,-9,-6,-1,-9,-9,1,10,-1,10,-10,10,-3,9,6,10,-8,4,4,-10,-6,-3,3,9,-4,1,9,1,10,2,5,-8,2,6,7,-1,7,10,-9,-1,9,-8,-3,10,8,-1,-5,5,-1,5,7,3,-2,-3,5,6,5,-10,-3,-2,-2,6,-2,-5,4,-4,-8,4,-3,10,10,-10,10,-5,-2,-7,-2,2,-6,10,6,10,3,5,10,4,1,-6,5,5,-10,10,5,-5,-8,10,1,10,-5,-9,-2,6,-6,4,4,7,-4,-6,-10,10,8,-3,-2,-2,-10,2,4,5,10,3,3,-10,8,3,-8,5,-5,-4,3,-3,-9,-5,3,-4,3,9,-7,10,4,1,-8,-8,5,1,-10,-3,9,3,-9,-9,4,8,-8,7,2,5,-6,-5,7,-1,10,7,1,5,4,-4,-3,-2,-1,-4,6,-4,-2,-5,5,-7,1,6,1,2,5,-8,8,-9,8,1,3,-8,4,-6,-3,-6,7,4,3,-7,-4,9,4,9,1,6,5,1,-9,-10,1,5,-8,-10,-7,-1,2,2,-10,-6,3,7,7,-1,6,-9,9,-5,-4,-10,-1,-3,1,-9,-8,-1,8,-1,7,-1,3,-8,-5,9,-9,2,10,-5,5,-3,8,6,-4,-8,8,2,1,-6,-6,-6,6,6,-7,8,-2,5,-6,5,7,-1,-5,10,4,2,3,-4,10,-6,1,-9,6,5,6,-2,-5,9,5,-8,7,8,10,8,1,8,-9,-7,10,7,-1,-8,3,8,1,6,8,8,5,9,-2,-10,-2,6,-10,-10,5,9,7,7,-5,-6,8,-10,-1,-10,6,4,8,1,-6,-9,1,10,-7,-8,9,-5,7,9,-6,3,-1,-1,-8,5,5,6,3,-6,2,-1,7,7,3,3,4,-1,-2,4,-5,7,-2,-4,8,5,3,8,-2,-5,10,-4,6,9,-6,-10,-1,-10,10,10,-5,8,1,-9,1,-9,4,7,-9,-9,-9,-7,-8,5,-1,7,-2,-4,-1,5,9,-4,9,4,-10,-4,-4,1,-6,-1,3,-2,3,7,1,7,-8,-2,4,7,-10,3,2,5,2,4,4,-10,4,-10,-9,-4,7,6,-3,-7,3,-7,4,10,10,1,4,2,9,4,8,-7,-7,8,5,4,-5,-1,-5,-5,9,-10,7,2,3,-4,-5,7,3,1,-3,3,6,-9,7,7,-1,-8,10,-6,5,5,2,-3,9,2,10,2,-3,8,-8,-5,-5,-9,2,-9,9,8,-8,-8,-4,-1,-8,-2,-7,-1,7,-3,-9,-7,-10,-10,10,2,-9,-7,1,-9,2,-9,4,-1,6,-3,-8,5,-9,-9,-1,9,9,4,3,-8,7,-3,7,-1,-9,7,-7,5,5,6,-5,9,8,-6,9,7,1,-6,-5,-1,-1,2,-1,5,3,6,-4,-3,-8,-7,-1,2,4,2,3,6,2,-6,-6,-8,10,-6,7,-1,6,-2,2,-3,-2,-8,6,2,1,-10,-7,-6,2,-3,1,6,4,8,-3,-2,4,1,3,10,9,1,-8,-5,10,1,-4,3,-4], dtype = "uint64")#candidate|1589|(2816,)|const|uint64
call_1587 = relay.TupleGetItem(func_128_call(relay.reshape(var_1588.astype('int16'), [2, 11, 7]), relay.reshape(const_1589.astype('uint64'), [16, 16, 11]), ), 2)
call_1590 = relay.TupleGetItem(func_131_call(relay.reshape(var_1588.astype('int16'), [2, 11, 7]), relay.reshape(const_1589.astype('uint64'), [16, 16, 11]), ), 2)
output = relay.Tuple([call_1578,call_1587,var_1588,const_1589,])
output2 = relay.Tuple([call_1579,call_1590,var_1588,const_1589,])
func_1592 = relay.Function([var_1588,], output)
mod['func_1592'] = func_1592
mod = relay.transform.InferType()(mod)
mutated_mod['func_1592'] = func_1592
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1593 = relay.var("var_1593", dtype = "int16", shape = (154,))#candidate|1593|(154,)|var|int16
func_1592_call = mutated_mod.get_global_var('func_1592')
call_1594 = func_1592_call(var_1593)
output = call_1594
func_1595 = relay.Function([var_1593], output)
mutated_mod['func_1595'] = func_1595
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1600 = relay.var("var_1600", dtype = "float64", shape = (16, 14, 1))#candidate|1600|(16, 14, 1)|var|float64
uop_1601 = relay.sin(var_1600.astype('float64')) # shape=(16, 14, 1)
output = uop_1601
output2 = uop_1601
func_1613 = relay.Function([var_1600,], output)
mod['func_1613'] = func_1613
mod = relay.transform.InferType()(mod)
mutated_mod['func_1613'] = func_1613
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1614 = relay.var("var_1614", dtype = "float64", shape = (16, 14, 1))#candidate|1614|(16, 14, 1)|var|float64
func_1613_call = mutated_mod.get_global_var('func_1613')
call_1615 = func_1613_call(var_1614)
output = call_1615
func_1616 = relay.Function([var_1614], output)
mutated_mod['func_1616'] = func_1616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_479_call = mod.get_global_var('func_479')
func_481_call = mutated_mod.get_global_var('func_481')
call_1630 = relay.TupleGetItem(func_479_call(), 0)
call_1631 = relay.TupleGetItem(func_481_call(), 0)
func_464_call = mod.get_global_var('func_464')
func_469_call = mutated_mod.get_global_var('func_469')
const_1645 = relay.const([-1.565210,4.050712,9.407542,-2.508100,-4.296139,3.400789,-5.667793,-2.121288,-2.004675,0.966208,-9.461112,9.877117,2.752791,6.684120,-3.300097,3.605914,5.862999,3.060325,6.701708,-3.815318,4.819517,0.756226,6.257601,-0.173825,1.383579,6.226158,0.419914,5.682762,3.368910,7.263721,4.220290,1.768418,-7.057633,-0.387386,-1.375886,5.150462,-7.193755,5.270293,9.656312,5.760474,6.128317,-6.520590,-7.222228,7.768465,-9.117474,6.696228,1.201475,-5.264287,-2.855968,-3.239749,-3.555219,-6.197838,-8.945612,-6.264937,3.337050,-9.542125,9.288823,7.392457,4.954348,0.272275,-3.585549,9.437728,6.376049,9.716730,-5.265255,-5.017041,5.586472,-4.818010,-1.516049,0.097784,-1.960085,-0.698804,-3.400220,0.802380,-0.175005,-8.010339,-9.918708,1.443508,0.346996,8.216027,-4.512050,-1.768183,-8.885871,0.559428,-7.996087,-0.875157,-8.733029,-7.127868,7.738337,-0.552049,-0.004672,-6.268907,7.577093,7.551255,-0.522054,-6.034940,-9.292444,-6.980894,4.580157,-0.866154,5.872129,5.532257,0.731659,-5.627120,2.571451,3.914574,2.204225,-1.996165,4.715274,-1.215857,-6.987505,-3.339957,4.001692,9.213427,-5.351475,-9.467746,4.031298,6.992866,7.416593,8.694210], dtype = "float32")#candidate|1645|(120,)|const|float32
const_1646 = relay.const([6,9,-8,2,-3,-9,2,-10,-7,-1,-9,-5,7,-2,-1,-2,-8,-4,1,-2,-3,-3,-2,-3,-9,10,-3,4,10,-6,5,-7,-10,9,-8,-4,-1,5,-9,2,3,7,-8,7,6,-8,-3,4,-9,3,-4,-8,5,10,-2,-3,6,-2,-8,2,-4,7,-7,-1,5,-4,2,-6,5,-2,-2,-3,-4,3,-4,7,5,-5,6,9,-1,-2,2,3,-8,6,9,-6,-2,6,4,-4,-9,3,7,9,-2,-5,1,-4,1,8,-7,5,-5,-5,-4,10,-10,-1,5,-6,-2,-1,-9,1,3,1,6,-9,-9,-2,5,-6,-6,-3,8,-8,-2,-1,-2,-10,4,6,9,10,10,-1,-5,2,-6,2,4,-2,7,-7,8,7,-1,1,-8,8,-5,5], dtype = "int16")#candidate|1646|(154,)|const|int16
const_1647 = relay.const([[10,1],[7,-8],[-7,-2],[-1,4],[-2,5],[7,-10],[1,2],[1,10],[-1,9],[-2,2],[-10,-8],[-7,5],[3,3],[-5,6],[8,-6],[7,-4],[-8,6],[-10,1],[3,10],[-6,-1],[5,8],[-4,10],[2,5],[-3,-8],[2,10],[2,-3],[-3,-7],[10,-5],[-2,8],[7,2],[-3,3],[-5,-4],[-4,-2],[-6,-3],[10,7],[10,6],[6,1],[-2,-7],[9,-1],[-8,3],[1,-10],[8,7],[3,-9],[-5,6],[1,-7],[8,1],[1,-2],[-7,2],[-10,-9],[6,-8],[10,-2],[4,-8],[-5,1],[-8,-3],[-2,-7],[1,1],[4,10],[5,-8],[7,2],[10,-8],[5,-8],[-2,2],[-5,-5],[8,8],[5,1],[7,-5],[-9,-6],[6,-4],[3,-2],[3,1],[2,-6],[3,4],[3,-7],[5,7],[-8,-5],[-8,5],[-2,-8],[-2,-5],[-4,-7],[-7,4],[8,-4],[-5,9],[5,10],[-2,7],[-4,1],[6,10],[-6,-9],[-10,7],[-6,1],[2,-9],[-3,-2],[-3,-10],[-6,3],[-4,-1],[4,7],[3,-1],[5,-2],[-1,3],[9,-10],[-4,1],[9,1],[-1,-8],[-10,-8],[-7,4],[3,8],[-9,10],[8,-2],[10,2],[9,5],[-6,4],[7,1],[-3,7],[-2,-3],[-6,9],[-3,-6],[-6,4],[-4,5],[3,-7],[1,4],[4,-3],[-6,7],[9,8],[9,-7],[-6,10],[10,-9],[-5,1],[4,-2],[-9,-5],[1,-1],[-10,-4],[-4,-3],[10,10],[7,10],[6,7],[-1,10],[-8,-8],[-7,-1],[7,5],[4,2],[9,3],[3,-9],[-9,1],[-7,-1],[-6,-4],[-8,-9],[8,-8],[1,-8],[4,-8],[9,6],[-4,-9],[5,-6],[10,3],[6,-5],[-7,-9],[-7,-1],[-2,-7],[-6,8],[-9,-3],[-6,-7],[-10,4],[-4,10],[-4,-2],[-8,1],[1,1],[-1,7],[4,6],[8,6],[-4,4],[1,-1],[-5,-7],[3,-4],[-6,-2],[-4,6],[-7,-9],[6,5],[-8,-7],[-4,-6],[-1,-3],[1,-9],[-4,3],[-7,7],[-3,-3],[4,6],[6,2],[4,-1],[1,9],[1,10],[-8,3],[-1,-3],[7,-3],[3,-2],[7,-1],[4,-7],[-3,-8],[4,-2],[-10,-10],[-7,7],[-7,6],[10,-9],[4,7],[1,4],[10,-10],[9,-9],[-1,9],[-1,4],[5,-10],[-10,1],[10,-3],[-9,4],[-8,-6],[-8,-3],[3,7],[-8,-2],[10,7],[2,3],[5,-10],[2,6],[8,-6],[-4,-5],[1,-10],[2,-2],[-5,-2],[7,8],[5,8],[2,9],[5,-8],[4,-7],[5,6],[3,-2],[8,-5],[3,-9],[-1,-6],[-1,3],[-10,-7],[6,1],[-3,-1],[-4,-5],[8,9],[1,-2],[7,5],[4,-5],[1,-9],[8,-10],[-7,-7],[3,5],[-2,-7],[-4,-7],[-6,10],[4,-4],[-9,-2],[3,10],[-3,2],[1,-1],[2,9],[-6,9],[-1,-4],[4,10],[1,10],[5,3],[-9,6],[-2,2],[-5,-2],[-9,3],[-7,5],[-4,-7],[-10,-8],[-9,3],[-6,7],[-5,2],[1,-1],[4,-10],[-10,4],[-1,-9],[-10,-6],[-8,4],[-7,3],[-9,2],[-8,10],[-8,5],[-5,-3],[2,7],[-9,-8],[1,2],[-4,-10],[10,2],[-6,4],[-3,3],[9,-6],[8,-10],[8,7],[-1,-7],[-3,-9],[2,5],[-6,-3],[5,8],[-4,5],[-10,2],[-5,7],[-7,3],[5,5],[5,-5],[-6,-9],[6,6],[-10,3],[-8,-7],[-3,2],[-1,2],[-9,3],[-6,3],[9,-6],[9,-7],[5,-10],[7,7],[-4,-10],[4,-10],[8,6],[-2,-7],[-1,5],[4,-9],[-4,-3],[6,10],[1,-6],[-3,-9],[-10,6],[-4,-4],[-5,6],[-3,-2],[6,7],[-7,4],[9,4],[-6,5],[-10,9],[-6,-10],[4,-4],[-3,-3],[2,-2],[8,-9],[-6,1],[6,10],[-10,9],[-4,1],[-6,-4],[-1,-9],[10,4],[-7,-7],[5,-7],[-7,-6],[-7,-5],[5,8],[2,2],[10,8],[1,8],[-4,3],[4,-10],[-8,-7],[3,-6],[9,2],[6,5],[-5,8],[5,-6],[-2,6],[-10,8],[-3,2],[9,6],[2,7],[2,-7],[-5,3],[-2,8],[-7,-3],[-1,6],[4,-1],[6,10],[5,-5],[9,2],[-7,-3],[3,7],[6,-8],[9,-2],[-9,-7],[-10,2],[-4,2],[1,9],[-10,-8],[-4,4],[5,10],[3,-8],[-4,-1],[1,2],[2,-1],[8,10],[-4,1],[-7,9],[-7,5],[-10,-6],[9,-3],[-1,-8],[-8,6],[10,-4],[-8,2],[1,5],[-10,-8],[7,-7],[1,9],[-4,5],[-7,-8],[6,-1],[8,-10],[-5,-7],[-7,-7],[8,1],[5,-1],[6,-1],[-6,-1],[-2,9],[-6,-8],[-3,-7],[-7,7],[10,7],[7,-6],[-6,7],[7,-6],[-10,6],[-5,-6],[7,-1],[10,4],[-5,7],[10,6],[-2,8],[10,-6],[-3,4],[-7,6],[-4,2],[6,-5],[-6,-2],[6,10],[10,-7],[6,-9],[-8,-4],[-5,-10],[-9,2],[6,-6],[-10,9],[-6,-5],[-9,-5],[6,3],[-6,8],[9,-10],[-10,-6],[2,1],[10,-9],[8,-3],[4,1],[3,-3],[-3,2],[-9,-2],[7,-7],[10,2],[-5,8],[-2,-10],[8,-10],[7,10],[4,-4],[4,-4],[-4,1],[-7,5],[3,5],[2,-4],[9,1],[-7,6],[3,-6],[5,-10],[-9,2],[4,-7],[-9,-2],[10,-3],[-2,-4],[7,2],[-9,-9],[-8,-3],[1,-4],[3,2],[6,6],[4,4],[4,-6],[-10,-3],[9,-3],[-2,-4],[2,-10],[9,-10],[7,-2],[3,-6],[-6,10],[-3,4],[8,8],[2,4],[10,-2],[5,-6],[5,-3],[4,7],[-4,-3],[-3,-10],[4,10],[-2,1],[-8,10],[2,6],[-2,8],[-8,5],[6,-10],[4,-10],[8,4],[4,-1],[-8,-6],[7,-2],[10,-6],[-6,10],[-8,1],[-10,10],[-10,-9],[2,7],[-1,2],[4,8],[3,10],[-4,3],[3,-3],[4,-3],[10,9],[2,-1],[10,4],[5,-7],[7,-10],[-10,-2],[-7,-7],[10,7],[2,9],[-3,-10],[4,-6],[5,9],[-1,-4],[2,-5],[2,-1],[-10,2],[6,9],[-4,2],[-2,-8],[2,-10],[6,5],[9,-8],[9,-3],[10,2],[-9,-7],[9,-2],[2,7],[-7,6],[-10,-5],[10,-10],[-5,-8],[10,-4],[5,3],[-5,-5],[7,8],[1,-1],[-6,10],[2,-4],[4,-3],[-6,-5],[-10,-4],[-5,1],[-1,8],[-4,2],[7,-7],[1,5],[3,-8],[-7,-9],[3,-4],[-2,-2],[4,6],[-1,10],[-8,7],[6,5],[-2,-10],[7,-7],[-5,-9],[-4,10],[1,5],[-4,-1],[10,4],[-10,7],[1,10],[-9,6],[-8,8],[6,-9],[6,10],[-9,-4],[7,-4],[4,-8],[1,3],[-8,1],[-4,9],[1,-8],[4,-8],[-8,-3],[-10,-3],[-10,-1],[10,-8],[-3,-4],[2,-10],[3,-9],[-5,-9],[9,8],[-1,-4],[-2,10],[9,10],[-1,-2],[10,-5],[9,2],[-2,4],[5,1],[-3,-4],[9,6],[-6,-1],[-3,-9],[4,-9],[-9,-4],[-2,-2],[-2,-10],[7,-7],[10,6],[2,-2],[-10,-1],[8,-7],[1,-9],[2,9],[-4,9],[2,10],[3,-7],[-1,1],[1,-8],[-2,-5],[-8,3],[6,8],[-10,5],[-6,6],[-9,4],[4,-5],[-5,-6],[-10,9],[7,-2],[3,-7],[6,7],[-7,1],[5,-7],[-9,8],[7,-3],[6,5],[-4,-8],[-6,2],[-7,5],[-3,1],[2,-9],[-10,6],[-2,4],[-1,-1],[7,-3],[-6,-6],[7,8],[-6,8],[-7,-8],[5,-6],[-3,4],[1,-10],[-9,-1],[10,-10],[9,-7],[-9,4],[3,4],[-5,6],[1,3],[-7,10],[6,3],[-1,4],[-2,-6],[5,6],[-1,7],[-1,6],[-5,5],[4,10],[-1,7],[-5,-3],[-2,-8],[6,-7],[6,-4],[9,10],[1,-7],[-5,4],[-7,7],[3,-9],[-8,4],[-10,-10],[6,-3],[4,-10],[1,9],[-2,1],[5,3],[7,-5],[-8,-8],[9,-5],[3,-2],[3,3],[7,9],[6,-3],[7,1],[8,8],[6,-6],[-5,-1],[-1,9],[-3,8],[-6,-1],[7,7],[10,10],[5,-3],[6,-5],[-10,-1],[-9,5],[-3,-4],[-9,3],[-9,-2],[8,4],[-9,-4],[6,-6],[-8,-7],[7,1],[-4,9],[9,1],[-2,-4],[6,4],[7,-2],[9,-1],[-7,6],[-2,-6],[-1,2],[-8,-6],[8,1],[-10,-3],[2,3],[-5,2],[5,-10],[4,-3],[-10,5],[-8,8],[-4,1],[-3,2],[2,-9],[-10,-1],[-1,-3],[-8,2],[-9,-7],[9,-2],[4,7],[-10,3],[4,10],[-4,-2],[3,-10],[10,-8],[8,-8],[1,-9],[5,-10],[-5,-8],[-6,-7],[-9,-5],[-4,3],[8,5],[-7,2],[2,10],[-9,6],[-3,7],[3,10],[-2,-6],[2,2],[-1,6],[9,3],[-3,-3],[-5,-6],[-3,8],[6,-10],[4,7],[-3,8],[6,-1],[3,-8],[-9,9],[-10,-2],[8,1],[-9,4],[-6,1],[-10,5],[-4,4],[-10,-6],[-3,-3],[-7,-8],[-7,1],[-1,-9],[-6,8],[1,3],[-10,5],[-9,-1],[3,7],[-10,-7],[7,3],[2,5],[-6,3],[6,3],[3,6],[-8,-6],[10,10],[-10,9],[6,-5],[7,4],[3,-1],[5,3],[-3,-2],[5,-1],[-3,6],[-10,1],[8,4],[-6,-9],[10,-7],[3,3],[-8,-6],[-2,9],[7,-9],[10,-5],[-7,-4],[-9,-3],[-10,-4],[-2,-10],[1,-5],[-4,-8],[-8,10],[-6,6],[3,-6],[10,3],[-10,4],[3,2],[1,-7],[-2,6],[10,7],[2,-1],[3,9],[-7,-3],[1,-10],[-3,-10],[-2,1],[-10,1],[4,7],[-1,-1],[8,-8],[-4,3],[-8,2],[7,-8],[-9,-10],[-6,10],[-1,4],[-7,-6],[4,-1],[5,-8],[7,6],[1,3],[-3,-10],[6,-8],[9,8],[-8,-3],[8,-3],[-8,-8],[2,-10],[-10,-5],[-8,1],[-5,2],[3,-1],[6,-3],[6,9],[-8,10],[3,-3],[3,-5],[2,-6],[4,-2],[9,8],[-7,-10],[-9,-8],[8,-7],[8,-3],[9,-3],[-3,-2],[8,-6],[9,-10],[6,-3],[3,-4],[-1,-1],[4,-1],[3,7],[-2,4],[5,5],[-5,2],[7,10],[9,10],[-6,9],[8,-2],[4,6],[8,-6],[-10,-7],[-7,10],[-4,-7],[-4,-3],[9,-10],[-1,-7],[-4,3],[-1,-7],[1,9],[2,-6],[-8,1],[10,-4],[-5,-8],[-9,-3],[6,-8],[-2,-1],[8,-3],[-7,-9],[9,-9],[-4,-10],[7,5],[-10,2],[-2,-4],[-3,9],[5,4],[-10,7],[4,8],[10,7],[5,5],[2,-1],[6,-1],[2,-2],[4,7],[2,-3],[1,-6],[-1,-10],[7,-10],[-3,-5],[8,-1],[10,7],[1,7],[-9,2],[4,-3],[-1,1],[-8,-8],[6,1],[-3,-6],[6,-6],[9,-2],[4,8],[-10,-4],[4,10],[8,3],[3,-8],[6,7],[7,-9],[-7,-5],[-5,-10],[6,9],[-9,3],[8,1],[-8,8],[-3,6],[-10,-8],[-7,9],[-8,10],[-3,5],[7,9],[-4,7],[-9,7],[-1,4],[9,-8],[7,-10],[-6,-10],[-1,-9],[4,6],[-8,9],[-7,9],[-9,-9],[7,5],[-7,-8],[7,-2],[-4,9],[-10,-6],[-7,4],[-1,-3],[-6,-7],[2,-8],[6,1],[-5,-2],[-3,8],[3,10],[9,5],[8,8],[-10,8],[6,-10],[1,6],[4,4],[-8,-1],[-6,-10],[-6,5],[-2,-10],[8,4],[-2,-6],[6,7],[-9,-9],[5,7],[-2,8],[-3,4],[6,8],[9,-7],[6,4],[-5,-4],[-5,-1],[-3,-4],[7,-5],[-5,-6],[2,-4],[-3,4],[2,3],[-10,-4],[-10,-5],[-5,-9],[3,3],[-2,8],[10,-7],[-10,-4],[8,2],[6,2],[2,10],[6,-10],[-3,8],[1,-9],[7,5],[6,2],[7,-3],[1,-9],[-1,-10],[8,8],[2,-7],[2,-1],[-6,6],[6,-8],[-3,5],[4,-9],[-5,-4],[9,-4],[-9,-2],[-1,-10],[1,-8],[4,-9],[-7,-3],[10,-8],[10,-8],[5,8],[7,5],[-4,6],[10,2],[2,-3],[6,1],[-5,-3],[-2,-2],[6,-3],[1,-2],[4,10],[-4,10],[-4,6],[-6,-9],[6,5],[-2,-7],[8,-1],[9,-6],[1,-8],[8,10],[10,5],[-1,-8],[4,-8],[-10,-5],[6,-9],[-1,-9],[1,-7],[7,3],[1,5],[10,-2],[-7,-3],[5,5],[-7,-6],[9,9],[5,9],[3,-9],[-9,8],[-8,-8],[-9,1],[-10,-5],[3,3],[9,10],[-10,-3],[-2,-7],[9,-2],[4,-1],[10,8],[10,-9],[5,5],[-6,7],[5,-10],[2,-9],[1,-9],[3,9],[-2,5],[10,-5],[8,10],[-4,-1],[-7,-7],[8,-2],[-9,-7],[1,-6],[-5,-4],[-9,-2],[8,10],[-1,2],[-5,6],[5,4],[9,4],[9,2],[5,9],[-5,-8],[6,-7],[-2,-2],[-6,-10],[-8,-2],[-8,-8],[8,-1],[8,-6],[2,7],[5,-3],[-3,-4],[5,9],[-2,4],[-7,7],[2,10],[-9,-4],[2,8],[-7,4],[8,-6],[-4,8],[-6,-6],[-5,-2],[-4,-9],[-9,-3],[-6,8],[-2,3],[10,4],[-6,2],[5,9],[-4,8],[-3,8],[-2,5],[-1,-3],[-5,2],[-8,3],[-9,10],[-2,3],[-7,-3],[-8,4],[-1,-7],[-4,-3],[9,-8],[2,-4],[4,-4],[-10,4],[7,-10],[8,6],[5,-2],[-6,-9],[2,3],[-9,-6],[1,-3],[8,10],[7,-4],[-6,-4],[4,1],[3,-6],[-9,3],[-5,5],[1,-7],[-5,8],[-9,-7],[-1,-5],[1,6],[7,-10],[-10,-8],[-2,-1],[1,3],[6,-10],[-4,-9],[9,9],[-1,-5],[6,7],[-8,10],[-8,-4],[10,-4],[9,-1],[-10,7],[4,1],[-2,4],[-4,1],[-7,-4],[2,3],[7,10],[1,8],[-2,3],[2,3],[-4,1],[1,-10],[5,-1],[-3,-8],[-2,-6],[-10,6],[-1,1],[-5,-9],[-3,-7],[-2,-1],[2,-3],[8,3],[2,5],[-6,-5],[10,-2],[10,5],[10,6],[-8,1],[2,-5],[5,-2],[-9,-8],[-8,2],[9,-4],[-5,-2],[1,-9],[6,-1],[1,-9],[-3,-5],[8,7],[-8,-3],[-5,8],[7,5],[10,1],[1,4],[-5,2],[4,10],[3,-7],[8,-2],[10,-5],[9,-7],[3,5],[-7,7],[6,9],[7,3],[7,-4],[1,-10],[-5,-5],[4,-3],[9,10],[-1,-9],[-8,-6],[-8,-8],[-6,-9],[-6,5],[3,-6],[-6,-3],[-1,3],[4,6],[8,9],[-8,2],[9,2],[-2,9],[-10,2],[5,1],[2,7],[-5,8],[-4,1],[5,-9],[-5,-10],[-9,4],[-5,5],[4,8],[-1,-2],[8,10],[-8,-4],[-4,-7],[-4,-8],[7,4],[8,4],[7,-8],[6,5],[-1,-4],[5,1],[-2,10],[7,-1],[-10,8],[4,2],[5,2],[-1,3],[-1,2],[-6,-7],[3,-6],[-9,-7],[-2,9],[-1,9],[-2,-5],[-7,6],[7,4],[-8,4],[2,4],[-7,-2],[-7,4],[1,-4],[-6,5],[-7,-9],[-6,-8],[8,8],[1,1],[2,-4],[-4,7],[-4,8],[9,-3],[-4,-3],[-7,-7],[-4,-3],[8,3],[-9,8],[-9,-9],[-7,-3],[10,-7],[8,7],[2,8],[-10,2],[-9,5],[-4,-3],[10,-6],[-9,-7],[6,-5],[3,-2],[5,-2],[-5,10],[-1,-3],[-10,10],[8,-8],[8,8],[-7,-10],[5,7],[4,-3],[-6,-2],[-8,4],[1,7],[-1,-8],[10,2],[-9,10],[-6,3],[8,8],[9,-1],[-7,4],[-10,-9],[5,9],[-5,5],[-3,9],[-1,9],[8,-3],[9,3],[-10,6],[-7,-2],[-4,10],[-10,-5],[-1,4],[7,-3],[-3,2],[-2,-10],[10,-4],[-2,-9],[-5,-8],[-5,10],[7,8],[-9,1],[-7,2],[7,-2],[9,-4],[-4,7],[-6,-6],[8,-5],[-2,-3],[3,-1],[-6,-10],[6,-2],[1,5],[-10,5],[-9,-7],[9,-6],[-6,-3],[2,1],[-10,2],[6,2],[1,1],[10,-9]], dtype = "uint64")#candidate|1647|(1408, 2)|const|uint64
call_1644 = relay.TupleGetItem(func_464_call(relay.reshape(const_1645.astype('float32'), [15, 1, 8]), relay.reshape(const_1646.astype('int16'), [154,]), relay.reshape(const_1647.astype('uint64'), [2816,]), ), 2)
call_1648 = relay.TupleGetItem(func_469_call(relay.reshape(const_1645.astype('float32'), [15, 1, 8]), relay.reshape(const_1646.astype('int16'), [154,]), relay.reshape(const_1647.astype('uint64'), [2816,]), ), 2)
var_1649 = relay.var("var_1649", dtype = "float64", shape = (14, 2, 8))#candidate|1649|(14, 2, 8)|var|float64
bop_1650 = relay.greater(call_1630.astype('bool'), relay.reshape(var_1649.astype('bool'), relay.shape_of(call_1630))) # shape=(14, 2, 8)
bop_1653 = relay.greater(call_1631.astype('bool'), relay.reshape(var_1649.astype('bool'), relay.shape_of(call_1631))) # shape=(14, 2, 8)
var_1663 = relay.var("var_1663", dtype = "uint64", shape = (2816,))#candidate|1663|(2816,)|var|uint64
bop_1664 = relay.power(call_1644.astype('float64'), relay.reshape(var_1663.astype('float64'), relay.shape_of(call_1644))) # shape=(2816,)
bop_1667 = relay.power(call_1648.astype('float64'), relay.reshape(var_1663.astype('float64'), relay.shape_of(call_1648))) # shape=(2816,)
bop_1679 = relay.greater(const_1647.astype('bool'), relay.reshape(var_1663.astype('bool'), relay.shape_of(const_1647))) # shape=(1408, 2)
bop_1683 = relay.greater_equal(bop_1650.astype('bool'), relay.reshape(var_1649.astype('bool'), relay.shape_of(bop_1650))) # shape=(14, 2, 8)
bop_1686 = relay.greater_equal(bop_1653.astype('bool'), relay.reshape(var_1649.astype('bool'), relay.shape_of(bop_1653))) # shape=(14, 2, 8)
output = relay.Tuple([const_1645,const_1646,bop_1664,bop_1679,bop_1683,])
output2 = relay.Tuple([const_1645,const_1646,bop_1667,bop_1679,bop_1686,])
func_1689 = relay.Function([var_1649,var_1663,], output)
mod['func_1689'] = func_1689
mod = relay.transform.InferType()(mod)
mutated_mod['func_1689'] = func_1689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1689_call = mutated_mod.get_global_var('func_1689')
var_1691 = relay.var("var_1691", dtype = "float64", shape = (14, 2, 8))#candidate|1691|(14, 2, 8)|var|float64
var_1692 = relay.var("var_1692", dtype = "uint64", shape = (2816,))#candidate|1692|(2816,)|var|uint64
call_1690 = func_1689_call(var_1691,var_1692,)
output = call_1690
func_1693 = relay.Function([var_1691,var_1692,], output)
mutated_mod['func_1693'] = func_1693
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1698 = relay.var("var_1698", dtype = "float32", shape = (9, 2, 4))#candidate|1698|(9, 2, 4)|var|float32
uop_1699 = relay.cosh(var_1698.astype('float32')) # shape=(9, 2, 4)
bop_1710 = relay.greater_equal(uop_1699.astype('bool'), relay.reshape(var_1698.astype('bool'), relay.shape_of(uop_1699))) # shape=(9, 2, 4)
output = bop_1710
output2 = bop_1710
func_1723 = relay.Function([var_1698,], output)
mod['func_1723'] = func_1723
mod = relay.transform.InferType()(mod)
mutated_mod['func_1723'] = func_1723
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1724 = relay.var("var_1724", dtype = "float32", shape = (9, 2, 4))#candidate|1724|(9, 2, 4)|var|float32
func_1723_call = mutated_mod.get_global_var('func_1723')
call_1725 = func_1723_call(var_1724)
output = call_1725
func_1726 = relay.Function([var_1724], output)
mutated_mod['func_1726'] = func_1726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mod.get_global_var('func_918')
func_919_call = mutated_mod.get_global_var('func_919')
call_1800 = func_918_call()
call_1801 = func_918_call()
uop_1803 = relay.acos(call_1800.astype('float64')) # shape=(14, 2, 8)
uop_1805 = relay.acos(call_1801.astype('float64')) # shape=(14, 2, 8)
func_657_call = mod.get_global_var('func_657')
func_658_call = mutated_mod.get_global_var('func_658')
call_1810 = func_657_call()
call_1811 = func_657_call()
output = relay.Tuple([uop_1803,call_1810,])
output2 = relay.Tuple([uop_1805,call_1811,])
func_1816 = relay.Function([], output)
mod['func_1816'] = func_1816
mod = relay.transform.InferType()(mod)
output = func_1816()
func_1817 = relay.Function([], output)
mutated_mod['func_1817'] = func_1817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1385_call = mod.get_global_var('func_1385')
func_1387_call = mutated_mod.get_global_var('func_1387')
call_1822 = relay.TupleGetItem(func_1385_call(), 0)
call_1823 = relay.TupleGetItem(func_1387_call(), 0)
var_1834 = relay.var("var_1834", dtype = "float64", shape = (14, 2, 8))#candidate|1834|(14, 2, 8)|var|float64
bop_1835 = relay.bitwise_and(call_1822.astype('int32'), relay.reshape(var_1834.astype('int32'), relay.shape_of(call_1822))) # shape=(14, 2, 8)
bop_1838 = relay.bitwise_and(call_1823.astype('int32'), relay.reshape(var_1834.astype('int32'), relay.shape_of(call_1823))) # shape=(14, 2, 8)
func_1689_call = mod.get_global_var('func_1689')
func_1693_call = mutated_mod.get_global_var('func_1693')
const_1840 = relay.const([-5,3,-7,1,-9,-10,-1,-4,-1,3,6,-10,3,-9,7,9,4,8,-3,9,-3,-1,-4,-7,5,-6,-3,-4,-4,-9,9,-7,-10,-4,-3,-6,-4,3,1,-4,9,-9,-8,9,6,-5,7,-7,6,-1,8,7,6,1,-1,-6,-7,-3,10,7,3,4,-3,-7,4,-7,-7,4,6,1,-2,-8,-5,-6,-4,-4,6,-6,-9,-7,1,5,10,-3,5,-4,2,8,4,4,-6,4,6,-10,-3,8,-10,-3,-2,-9,-10,-6,6,4,5,-7,-8,-2,2,-9,-8,10,2,8,-2,3,-1,-8,2,-6,-10,7,-7,4,10,6,-2,5,2,8,-2,9,9,-2,-9,-7,5,-9,-4,2,6,-3,6,4,3,5,-2,-3,-2,-3,3,-4,-5,-3,-5,6,-4,-2,7,8,8,9,8,3,5,2,6,-8,-8,2,5,5,-7,10,10,5,-3,-8,-4,-10,-8,9,-10,-7,-10,-2,-6,-6,3,-6,4,-3,-6,8,3,-9,4,-5,6,3,-10,3,-1,1,-3,-8,-8,5,-3,4,-5,-9,2,3,5,-6,-10,-4,-7,6,-2,10,7,-6,10,-8,-4,6,-2,-7,-5,-5,3,-10,2,2,-2,6,8,2,1,-5,-9,-4,-9,10,-6,-1,-2,-1,8,-10,6,10,5,1,1,4,6,3,-9,-9,5,3,-2,-4,6,1,-8,-5,2,-3,-2,5,5,1,-8,-6,-2,-2,1,-5,10,10,-6,2,-3,-10,-4,-2,4,10,8,7,-4,4,-5,-4,-4,4,1,5,3,-8,-4,-3,-8,10,-8,5,6,-7,8,-7,-8,-10,6,-3,-5,-5,3,-5,10,8,2,10,-1,-2,-2,9,9,9,9,6,4,2,9,10,-5,-7,-2,-9,-6,1,-10,-8,-2,-8,-2,6,6,-5,7,2,6,1,8,8,-10,4,1,-3,-2,5,-7,-9,-7,8,10,8,-1,3,-10,3,-9,-2,-10,3,-7,-3,-7,7,-7,-2,7,4,-8,7,-7,7,-9,6,7,-1,-10,-9,9,5,-3,4,6,5,-4,-3,3,6,-1,1,-4,2,-9,10,-9,3,-1,-1,6,10,-10,-8,5,7,6,3,2,-3,8,-8,-10,10,-9,-10,-1,-2,5,4,-6,3,-10,-2,-4,3,2,-1,-2,6,4,-6,-6,5,-10,1,-1,8,3,-4,-6,-10,-8,-3,-2,4,2,-2,-10,-2,-6,-6,7,8,5,8,-9,-2,-7,-9,-3,-6,5,-5,-5,-7,10,-7,9,-9,-9,8,3,-7,6,-1,1,3,-7,2,5,-2,3,2,-7,8,5,-6,-7,-1,10,-1,-3,-8,-3,10,-8,-1,-4,-4,-3,8,8,8,-8,-8,3,1,4,-6,-8,2,-1,-8,7,5,-4,-8,7,-10,5,3,-7,-3,2,7,8,-7,-4,3,8,-1,-8,-5,-3,10,-2,7,7,-2,1,-10,-1,-7,3,6,7,4,-4,-10,5,-8,-3,8,-7,9,-10,-9,8,-5,8,-4,7,-10,-8,-2,2,-10,3,5,8,7,2,10,4,3,-5,4,-5,-6,5,-6,6,-2,-3,10,-10,1,5,-4,-7,8,1,5,-8,-9,-7,-10,2,-3,-10,8,3,1,-3,6,9,-1,10,8,-4,-1,-3,-5,4,2,4,3,1,5,9,3,9,-2,-9,7,7,-6,10,5,-1,9,7,1,5,4,-1,-6,3,9,8,7,5,-4,-5,8,-6,-9,8,2,10,-9,-7,1,-5,-1,-8,6,2,-6,-1,-2,1,1,-3,-5,1,4,-1,7,7,6,-8,9,-4,-6,-1,-1,10,-6,-5,8,4,-5,6,10,-1,9,9,-9,4,8,-6,2,3,10,6,5,9,5,-1,1,3,3,-9,-7,-10,10,5,3,-7,-5,1,5,9,7,6,6,-9,1,3,-1,-4,8,-1,5,-4,-1,2,6,5,-3,-3,-10,8,-8,-1,4,10,-5,5,-8,-2,-5,-6,-6,-4,4,8,2,7,-4,1,-2,-10,-9,-6,-3,8,3,-8,-7,-5,-2,4,8,-3,8,10,2,-8,6,-10,4,-6,-1,3,-9,-8,-3,4,-4,4,1,-5,-6,6,6,-1,-3,7,-3,2,3,10,4,9,-1,1,9,-6,8,-6,-7,7,6,-6,6,-1,-7,7,7,9,-1,1,-6,-2,1,1,9,-10,1,5,1,10,-9,1,-5,5,1,-3,-4,-1,6,-3,-9,-9,-8,-2,2,-8,1,6,-2,-1,8,-1,-10,9,6,1,6,10,6,-2,-3,9,4,9,8,-10,-3,-1,7,1,4,1,-1,4,2,-6,-8,1,10,-7,-2,-5,10,-10,-7,-10,-2,-3,-3,-2,2,-2,-3,-4,4,1,8,1,-3,-5,-5,-1,8,-1,10,-6,1,5,-10,5,10,-10,-2,-8,-5,3,-10,6,-8,-8,10,1,1,-3,4,-7,-6,5,-9,2,8,5,-2,7,-7,10,-9,9,6,-3,2,7,8,-5,-8,4,-2,5,7,6,7,1,7,-7,2,7,3,-1,7,9,-2,-3,-1,10,10,-4,-10,-4,5,-1,-3,-10,-4,7,-8,9,1,-4,-8,-2,8,7,1,8,3,2,10,2,4,5,8,-1,4,1,10,2,9,10,3,5,-7,-3,2,1,7,-9,-2,5,-6,9,2,-5,-3,3,3,3,9,-9,1,7,7,-6,4,6,10,7,-9,4,-7,9,7,2,-7,-6,-10,-8,-7,-6,8,5,7,1,-6,9,4,-5,-1,-8,5,-9,-7,2,3,-6,-9,-8,-5,-4,4,4,5,-10,6,5,3,8,2,3,9,-4,-2,-7,-9,-8,4,2,3,8,-3,-5,-8,4,5,3,9,-2,-10,-8,8,4,9,-3,-10,-4,-3,-7,3,1,1,10,1,-8,1,-2,3,-2,1,-5,-8,4,-7,4,-4,-8,9,2,-9,3,-10,10,-10,-4,-10,10,7,9,4,-5,-10,-1,10,1,8,1,10,1,-4,8,3,1,-1,7,-6,4,-7,7,2,9,3,-8,-3,-2,4,-2,10,-1,8,8,2,9,9,-7,3,3,-9,-10,1,-3,2,4,-1,-2,-2,-2,-4,-2,-7,6,-8,-8,1,9,-10,9,-8,-3,-5,-7,-7,9,-9,6,1,-10,4,-6,-5,-9,9,-8,-8,-7,8,-1,-4,10,-3,-3,-10,-5,-10,1,8,-2,-7,-6,-1,-9,-1,-6,1,10,2,-2,6,-7,8,2,8,-5,-4,10,-5,4,1,3,-6,8,6,-10,-7,9,-7,-3,6,-9,-10,4,2,-3,8,5,-9,-1,4,9,2,-7,2,-3,-8,9,-5,-3,-2,10,-2,-5,-9,-8,-10,2,-7,-1,1,-7,8,6,10,-10,8,2,4,-3,-4,4,9,3,7,7,8,6,2,1,3,-2,-1,1,10,10,4,-7,2,-1,6,8,1,-1,-7,-5,-6,-1,1,-4,-5,-6,-8,2,-5,-2,2,-6,-5,-8,-3,-3,9,-6,6,-1,6,-10,2,-6,-6,9,-8,10,6,-6,-10,8,4,10,-5,3,-10,-8,6,1,-2,-1,-9,-6,1,-4,4,10,5,10,-1,-1,-5,-5,-3,-6,-9,9,-9,5,-8,3,-2,-8,3,6,10,-6,8,-9,-8,-8,-1,6,-10,4,-9,-8,1,7,5,-9,3,-3,7,-2,6,-3,-6,8,10,-6,8,2,-3,3,-2,-4,-10,-8,6,5,3,-8,8,7,-10,9,-6,-9,-9,8,7,-8,6,5,9,5,-7,-1,10,3,8,2,-2,-4,5,2,-3,-8,-10,2,-2,-1,1,-2,-9,-5,-6,2,7,-8,-9,4,-5,-2,7,6,2,-8,1,-6,-6,7,7,1,9,-8,-2,-2,-7,3,10,-3,9,7,-1,8,3,9,-7,6,10,6,-6,-10,-3,-7,4,-5,-3,-1,-5,-2,-6,-10,1,-1,-2,2,3,1,7,-9,1,-2,-8,7,-3,4,9,-4,-2,1,10,-1,5,1,3,-1,-7,9,7,9,-4,-9,6,3,-8,3,-8,-3,10,5,7,8,-10,-7,4,6,10,-2,1,-6,2,7,6,2,-3,9,-6,3,-7,-2,-8,-6,-6,-5,-6,3,2,7,-9,4,-10,3,-4,-10,7,-10,2,5,8,2,1,-1,5,-3,-9,-6,3,-4,6,-8,8,9,-7,6,4,-7,-3,-10,-8,-1,-1,5,8,1,-3,-6,8,-9,-2,8,2,1,-6,4,-5,1,3,7,5,-5,6,9,1,-9,-4,-8,-6,2,1,8,-2,-3,-6,6,10,-2,-5,2,-1,-8,10,1,-5,8,10,4,-4,9,-7,1,-8,-4,4,-10,7,-1,-4,-2,7,8,5,-1,1,9,7,-5,-5,-8,7,5,8,2,10,2,6,-7,2,-2,-10,-10,4,-1,-8,-7,9,-10,10,8,8,7,7,-6,4,1,2,-10,-1,-3,-10,-4,6,5,-8,8,-10,-9,-1,-10,-5,-8,4,-3,-8,4,1,-6,-3,-5,-3,-6,-9,2,2,-4,4,-5,-1,5,-5,7,6,10,-4,10,-7,-10,1,-6,-7,1,-4,10,-3,5,4,3,-7,9,10,-9,-4,-5,5,10,-4,1,-7,3,8,7,4,-3,-3,-2,-2,9,-2,-2,6,6,5,7,-2,2,-10,1,-7,5,-7,-4,-6,6,7,-4,2,-4,7,8,4,9,-7,10,-7,7,-9,-4,3,-4,9,-5,8,-9,3,-6,5,10,8,-9,4,2,4,10,-7,10,-2,9,6,-7,-3,-5,8,4,5,2,9,3,-9,3,-9,2,-7,3,8,2,3,-2,3,7,-1,-7,3,6,-5,10,1,7,-4,3,2,-3,-3,6,-3,3,-3,4,2,-10,10,-3,1,-3,2,-4,1,9,-4,-7,-7,-1,-1,-6,7,-10,-5,10,-4,-10,-8,1,4,3,-5,3,1,2,-10,-4,6,4,8,-7,8,9,4,5,-1,3,9,10,1,3,-2,-8,1,-10,-7,-9,4,3,9,-5,-6,-8,8,6,-10,1,-6,-8,3,3,-5,-5,4,9,5,6,4,-10,-10,2,-7,-1,1,7,-9,4,-7,-5,6,-4,7,4,-4,4,3,3,8,-1,3,-3,-2,-6,-5,-10,6,5,4,7,-6,-1,6,6,-7,-10,-9,-5,-1,10,4,8,3,-5,3,-2,-2,7,-6,9,2,-6,-4,1,-3,-1,2,9,3,2,-4,4,-9,4,-3,-1,-6,-7,-7,6,-1,9,8,-9,-1,-8,5,-3,-2,10,-1,2,5,8,10,-5,2,-4,-1,-3,2,-9,3,1,-8,3,-9,7,-6,9,-10,7,-8,6,4,4,-3,2,3,-3,4,2,-3,-7,-7,-5,1,-1,-4,8,8,-5,5,7,1,-10,-4,-8,3,-5,2,-7,3,1,7,-7,-1,4,-10,-3,10,7,6,-10,1,-9,-7,-5,6,-10,-5,-8,7,-2,4,9,-9,-8,2,-5,-3,-7,3,-1,-9,-4,7,-1,-7,-3,-2,-4,9,-7,-10,-5,9,5,5,10,8,8,-7,10,-6,2,-5,9,10,6,-10,-7,6,-8,-10,5,-4,3,-4,3,4,-9,4,5,-6,6,-4,5,-6,1,5,4,-10,1,10,5,-1,-4,-2,1,-10,6,-1,-5,5,-3,-3,10,-3,-9,-4,8,-1,-2,-1,-3,-1,8,1,1,9,-6,10,-6,-6,-8,1,8,10,5,3,6,-8,-8,-6,-6,-2,7,-10,-8,8,-9,-4,1,4,-5,7,-3,-6,5,-9,-8,5,4,8,4,-8,7,9,-5,-5,2,-4,8,-5,1,-3,-6,4,-4,3,-2,-10,-4,8,-3,-4,6,9,7,6,9,-6,-10,6,5,-3,-2,-8,3,8,1,-1,9,3,-4,-3,-10,10,1,3,5,5,-8,-4,8,-5,3,8,-7,-7,9,6,10,7,-1,-9,6,-2,6,-5,9,7,-7,-3,5,-5,-9,-2,-6,10,1,2,3,2,-1,8,-9,1,10,-10,3,7,-6,-2,-10,-8,2,-8,5,6,9,7,1,-3,3,5,-7,-9,-3,-5,-3,-6,2,-10,4,-6,-2,-10,-2,-3,4,-10,-2,4,-10,-10,2,8,10,5,-3,-6,4,9,6,-1,-10,3,-2,7,8,4,3,-5,7,-6,1,-9,-7,2,-8,6,-6,10,-8,9,-2,5,5,8,-2,-4,4,9,-2,7,-6,8,3,-1,2,-4,-2,-2,9,-1,-4,-3,10,2,-2,2,3,1,9,-7,-1,7,-10,-2,-1,-9,8,5,-5,-2,7,7,5,6,-10,-4,3,-4,-2,-3,9,-10,-5,7,-2,-9,2,-1,-3,-10,1,4,5,9,4,2,4,-2,-9,-1,9,-1,7,9,-10,-3,-1,5,4,-7,5,-6,3,10,-9,4,2,-9,9,8,-7,8,-9,5,-6,6,4,-10,9,9,-2,8,-10,4,-4,-7,-7,-10,10,2,10,5,9,8,-7,8,4,7,2,3,8,-9,-7,-1,-6,2,2,-7,5,1,-6,5,-4,4,-6,3,9,8,3,-2,4,-5,3,7,9,2,-6,5,-1,-5,-4,-10,-2,-8,10,4,-5,-2,10,6,7,7,7,1,-9,-5,-7,-7,-5,-2,6,-3,-4,9,4,7,5,5,4,-10,-4,-7,9,-8,8,3,7,-4,1,-8,3,6,-7,-10,7,-5,4,-2,3,-9,-1,6,-8,-2,6,-2,5,-6,9,5,-5,-10,10,4,-3,6,-5,3,-5,-2,7,9,-4,-4,1,10,8,9,-2,-3,5,-1,4,-6,1,9,2,7,2,-8,1,-3,7,-8,4,-4,-5,-1,-8,-7,7,-6,5,-6,7,2,-3,8,4,1,-1,8,9,-4,-8,-8,8,-5,-9,2,6,-7,-8,9,3,1,-4,-10,8,-3,-5,-3,-7,8,1,4,-1,-4,-6,-2,-2,4,1,10,6,-6,-4,-5,-9,-7,-10,-6,1,-1,-3,-7,5,-1,-5,-4,4,-1,-2,7,7,10,6,10,7,6,4,7,7,6,8,-1,3,-9,10,4,2,7,-3,-7,10,-10,-9,4,4,-5,1,5,10,6,-1,-7,8,3,3,-2,3,7,-1,-5,-2,-9,10,6,-9,-10,-5,-5,3,6,8,-6,2,-3,6,-7,-10,-3,10,10,2,-10,-9,3,3,-7,-7,-1,8,-9,-4,3,3,-6,-5,-4,8,-7,-9,10,-10,-4,-10,4,-9,-2,-1,8,-3,9,-3,-7,7,10,4,9,-5,-9,-7,2,-7,-10,-3,4,-7,4,-8,-10,4,-2,-8,-4,-5,9,-7,-10,7,-5,-10,-6,6,6,-2,-8,6,7,-2,-8,-6,-8,10,-9,8,9,5,-7,-7,2,9,8], dtype = "uint64")#candidate|1840|(2816,)|const|uint64
call_1839 = relay.TupleGetItem(func_1689_call(relay.reshape(var_1834.astype('float64'), [14, 2, 8]), relay.reshape(const_1840.astype('uint64'), [2816,]), ), 1)
call_1841 = relay.TupleGetItem(func_1693_call(relay.reshape(var_1834.astype('float64'), [14, 2, 8]), relay.reshape(const_1840.astype('uint64'), [2816,]), ), 1)
output = relay.Tuple([bop_1835,call_1839,const_1840,])
output2 = relay.Tuple([bop_1838,call_1841,const_1840,])
func_1853 = relay.Function([var_1834,], output)
mod['func_1853'] = func_1853
mod = relay.transform.InferType()(mod)
mutated_mod['func_1853'] = func_1853
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1854 = relay.var("var_1854", dtype = "float64", shape = (14, 2, 8))#candidate|1854|(14, 2, 8)|var|float64
func_1853_call = mutated_mod.get_global_var('func_1853')
call_1855 = func_1853_call(var_1854)
output = call_1855
func_1856 = relay.Function([var_1854], output)
mutated_mod['func_1856'] = func_1856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_590_call = mod.get_global_var('func_590')
func_591_call = mutated_mod.get_global_var('func_591')
call_1905 = func_590_call()
call_1906 = func_590_call()
uop_1909 = relay.cosh(call_1905.astype('float64')) # shape=(14, 2, 8)
uop_1911 = relay.cosh(call_1906.astype('float64')) # shape=(14, 2, 8)
func_895_call = mod.get_global_var('func_895')
func_896_call = mutated_mod.get_global_var('func_896')
call_1913 = relay.TupleGetItem(func_895_call(), 2)
call_1914 = relay.TupleGetItem(func_896_call(), 2)
output = relay.Tuple([uop_1909,call_1913,])
output2 = relay.Tuple([uop_1911,call_1914,])
func_1946 = relay.Function([], output)
mod['func_1946'] = func_1946
mod = relay.transform.InferType()(mod)
mutated_mod['func_1946'] = func_1946
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1946_call = mutated_mod.get_global_var('func_1946')
call_1947 = func_1946_call()
output = call_1947
func_1948 = relay.Function([], output)
mutated_mod['func_1948'] = func_1948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_937_call = mod.get_global_var('func_937')
func_939_call = mutated_mod.get_global_var('func_939')
call_1980 = relay.TupleGetItem(func_937_call(), 0)
call_1981 = relay.TupleGetItem(func_939_call(), 0)
output = call_1980
output2 = call_1981
func_2000 = relay.Function([], output)
mod['func_2000'] = func_2000
mod = relay.transform.InferType()(mod)
mutated_mod['func_2000'] = func_2000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2000_call = mutated_mod.get_global_var('func_2000')
call_2001 = func_2000_call()
output = call_2001
func_2002 = relay.Function([], output)
mutated_mod['func_2002'] = func_2002
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2012 = relay.const([[[-9.292903,-4.952045,-3.730827,-6.800789,-4.985505],[7.599756,-7.159375,7.596948,-5.979019,9.879475],[7.854694,-3.321453,0.163611,-7.768970,-7.284590],[1.675780,2.600646,1.089395,-7.726340,9.992722],[8.365616,4.171742,-1.313954,9.472338,-2.745791],[-8.143856,-2.206648,0.107692,-1.697944,-1.504712],[-4.878471,-4.743521,3.941429,9.609413,6.413203]],[[-7.058763,1.218140,-2.903819,-3.149538,3.610568],[-2.972321,-6.791089,-5.826938,3.728596,-2.432047],[-9.560689,7.773939,-3.066608,-1.745379,9.835175],[-4.306620,8.971567,3.775402,9.568110,6.204834],[-1.655696,-1.227288,-8.748233,-7.713742,-6.624996],[6.934528,3.666534,6.092117,7.477611,-8.282870],[0.158680,7.439020,-5.952034,-5.641752,-7.342657]],[[-2.840255,2.573733,-9.171193,-1.850781,2.836266],[0.250188,3.872603,-6.075385,-7.145717,-5.398821],[-8.777451,9.936647,-1.261149,-1.803001,7.239673],[-7.670324,8.168265,-7.521683,3.193016,-8.650508],[5.799895,4.751538,1.054273,1.274548,-2.532640],[-4.464075,3.116079,-2.057283,0.396885,-9.943116],[8.912771,4.157571,8.498143,-5.207604,-9.293948]],[[0.608834,-1.819526,-4.511088,-8.913435,1.047024],[6.355271,0.528719,4.498307,8.191370,-0.764717],[7.848564,-7.396531,-3.531446,2.459215,7.976411],[-8.609356,1.190895,2.233978,-8.408136,-0.142390],[-6.302611,5.195075,-8.156323,8.056169,3.929324],[-2.591892,-0.047920,2.182415,-9.396334,1.454250],[-5.333060,-4.301892,8.109222,2.596233,-7.049377]]], dtype = "float64")#candidate|2012|(4, 7, 5)|const|float64
const_2013 = relay.const([[[-7.284218,-7.094394,-2.291036,-3.959324,-9.597259],[-0.281694,1.121111,5.623538,-7.052741,2.412490],[-5.245212,9.907363,-5.409917,4.595177,-8.464514],[0.884621,7.854322,6.889751,-4.918192,-4.407247],[-7.639134,2.772655,-7.426370,0.409301,7.758813],[-0.999795,5.083241,6.447332,-4.107290,-7.262515],[-8.019726,9.833800,6.747454,8.265914,-7.027970]],[[-6.922917,-2.609121,1.254684,7.157399,-5.272600],[2.947126,-5.017118,-4.304466,-3.081920,0.955139],[6.906266,3.002899,5.299145,0.233347,-7.720448],[-1.524572,0.069092,-0.770802,-6.321960,5.846355],[-4.902741,1.719396,6.484077,8.014426,-3.009148],[-6.473867,-9.581228,9.652227,2.915860,-4.516099],[-9.717769,-5.914823,0.716337,-7.578791,-7.721436]],[[-7.613939,4.563951,-6.490244,6.620719,-5.305033],[-5.841234,2.033138,-3.101968,-0.898884,-8.177741],[2.458111,-9.401731,-1.656807,-2.862988,5.148278],[-8.428324,-2.185057,2.166123,9.034437,-6.513769],[-4.247383,-5.965973,5.095552,-4.289743,-3.642443],[-3.338761,-6.892297,-8.684400,-3.493415,9.396259],[5.111330,-6.205801,5.421594,-5.411781,-1.608476]],[[2.132040,8.560205,8.978047,-6.767037,7.932352],[-2.531365,9.088440,-1.660145,1.815029,-6.905892],[-5.091999,-3.858596,6.431914,-1.746232,-5.419334],[-5.705781,8.132119,-9.345386,-1.409509,5.724354],[2.672578,6.128722,-1.191883,-3.724863,6.165739],[-0.181550,1.683355,-0.604775,7.197290,-4.193164],[2.554796,2.327114,7.080769,4.720654,-1.527031]]], dtype = "float64")#candidate|2013|(4, 7, 5)|const|float64
bop_2014 = relay.maximum(const_2012.astype('float64'), relay.reshape(const_2013.astype('float64'), relay.shape_of(const_2012))) # shape=(4, 7, 5)
func_1385_call = mod.get_global_var('func_1385')
func_1387_call = mutated_mod.get_global_var('func_1387')
call_2035 = relay.TupleGetItem(func_1385_call(), 0)
call_2036 = relay.TupleGetItem(func_1387_call(), 0)
var_2050 = relay.var("var_2050", dtype = "float64", shape = (4, 7, 5))#candidate|2050|(4, 7, 5)|var|float64
bop_2051 = relay.bitwise_and(const_2013.astype('int16'), relay.reshape(var_2050.astype('int16'), relay.shape_of(const_2013))) # shape=(4, 7, 5)
bop_2059 = relay.greater(const_2013.astype('bool'), relay.reshape(var_2050.astype('bool'), relay.shape_of(const_2013))) # shape=(4, 7, 5)
func_561_call = mod.get_global_var('func_561')
func_563_call = mutated_mod.get_global_var('func_563')
call_2062 = func_561_call()
call_2063 = func_561_call()
func_264_call = mod.get_global_var('func_264')
func_266_call = mutated_mod.get_global_var('func_266')
call_2067 = relay.TupleGetItem(func_264_call(relay.reshape(call_2035.astype('float64'), [14, 2, 8])), 0)
call_2068 = relay.TupleGetItem(func_266_call(relay.reshape(call_2035.astype('float64'), [14, 2, 8])), 0)
func_1816_call = mod.get_global_var('func_1816')
func_1817_call = mutated_mod.get_global_var('func_1817')
call_2070 = relay.TupleGetItem(func_1816_call(), 1)
call_2071 = relay.TupleGetItem(func_1817_call(), 1)
uop_2072 = relay.cosh(bop_2051.astype('float32')) # shape=(4, 7, 5)
output = relay.Tuple([bop_2014,call_2035,bop_2059,call_2062,call_2067,call_2070,uop_2072,])
output2 = relay.Tuple([bop_2014,call_2036,bop_2059,call_2063,call_2068,call_2071,uop_2072,])
func_2079 = relay.Function([var_2050,], output)
mod['func_2079'] = func_2079
mod = relay.transform.InferType()(mod)
mutated_mod['func_2079'] = func_2079
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2080 = relay.var("var_2080", dtype = "float64", shape = (4, 7, 5))#candidate|2080|(4, 7, 5)|var|float64
func_2079_call = mutated_mod.get_global_var('func_2079')
call_2081 = func_2079_call(var_2080)
output = call_2081
func_2082 = relay.Function([var_2080], output)
mutated_mod['func_2082'] = func_2082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1385_call = mod.get_global_var('func_1385')
func_1387_call = mutated_mod.get_global_var('func_1387')
call_2088 = relay.TupleGetItem(func_1385_call(), 0)
call_2089 = relay.TupleGetItem(func_1387_call(), 0)
output = call_2088
output2 = call_2089
func_2092 = relay.Function([], output)
mod['func_2092'] = func_2092
mod = relay.transform.InferType()(mod)
output = func_2092()
func_2093 = relay.Function([], output)
mutated_mod['func_2093'] = func_2093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1259_call = mod.get_global_var('func_1259')
func_1260_call = mutated_mod.get_global_var('func_1260')
call_2114 = relay.TupleGetItem(func_1259_call(), 0)
call_2115 = relay.TupleGetItem(func_1260_call(), 0)
func_1112_call = mod.get_global_var('func_1112')
func_1115_call = mutated_mod.get_global_var('func_1115')
var_2138 = relay.var("var_2138", dtype = "int16", shape = (154,))#candidate|2138|(154,)|var|int16
var_2139 = relay.var("var_2139", dtype = "uint64", shape = (2816,))#candidate|2139|(2816,)|var|uint64
call_2137 = relay.TupleGetItem(func_1112_call(relay.reshape(var_2138.astype('int16'), [154,]), relay.reshape(var_2139.astype('uint64'), [2816,]), ), 3)
call_2140 = relay.TupleGetItem(func_1115_call(relay.reshape(var_2138.astype('int16'), [154,]), relay.reshape(var_2139.astype('uint64'), [2816,]), ), 3)
func_1431_call = mod.get_global_var('func_1431')
func_1433_call = mutated_mod.get_global_var('func_1433')
call_2143 = func_1431_call()
call_2144 = func_1431_call()
func_1431_call = mod.get_global_var('func_1431')
func_1433_call = mutated_mod.get_global_var('func_1433')
call_2151 = func_1431_call()
call_2152 = func_1431_call()
output = relay.Tuple([call_2114,call_2137,var_2138,var_2139,call_2143,call_2151,])
output2 = relay.Tuple([call_2115,call_2140,var_2138,var_2139,call_2144,call_2152,])
func_2154 = relay.Function([var_2138,var_2139,], output)
mod['func_2154'] = func_2154
mod = relay.transform.InferType()(mod)
mutated_mod['func_2154'] = func_2154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2154_call = mutated_mod.get_global_var('func_2154')
var_2156 = relay.var("var_2156", dtype = "int16", shape = (154,))#candidate|2156|(154,)|var|int16
var_2157 = relay.var("var_2157", dtype = "uint64", shape = (2816,))#candidate|2157|(2816,)|var|uint64
call_2155 = func_2154_call(var_2156,var_2157,)
output = call_2155
func_2158 = relay.Function([var_2156,var_2157,], output)
mutated_mod['func_2158'] = func_2158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1085_call = mod.get_global_var('func_1085')
func_1087_call = mutated_mod.get_global_var('func_1087')
call_2200 = relay.TupleGetItem(func_1085_call(), 0)
call_2201 = relay.TupleGetItem(func_1087_call(), 0)
output = call_2200
output2 = call_2201
func_2205 = relay.Function([], output)
mod['func_2205'] = func_2205
mod = relay.transform.InferType()(mod)
output = func_2205()
func_2206 = relay.Function([], output)
mutated_mod['func_2206'] = func_2206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1946_call = mod.get_global_var('func_1946')
func_1948_call = mutated_mod.get_global_var('func_1948')
call_2239 = relay.TupleGetItem(func_1946_call(), 1)
call_2240 = relay.TupleGetItem(func_1948_call(), 1)
output = call_2239
output2 = call_2240
func_2241 = relay.Function([], output)
mod['func_2241'] = func_2241
mod = relay.transform.InferType()(mod)
output = func_2241()
func_2242 = relay.Function([], output)
mutated_mod['func_2242'] = func_2242
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2250 = relay.var("var_2250", dtype = "float64", shape = (14, 1, 14))#candidate|2250|(14, 1, 14)|var|float64
uop_2251 = relay.log10(var_2250.astype('float64')) # shape=(14, 1, 14)
output = relay.Tuple([uop_2251,])
output2 = relay.Tuple([uop_2251,])
func_2253 = relay.Function([var_2250,], output)
mod['func_2253'] = func_2253
mod = relay.transform.InferType()(mod)
mutated_mod['func_2253'] = func_2253
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2254 = relay.var("var_2254", dtype = "float64", shape = (14, 1, 14))#candidate|2254|(14, 1, 14)|var|float64
func_2253_call = mutated_mod.get_global_var('func_2253')
call_2255 = func_2253_call(var_2254)
output = call_2255
func_2256 = relay.Function([var_2254], output)
mutated_mod['func_2256'] = func_2256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_171_call = mod.get_global_var('func_171')
func_173_call = mutated_mod.get_global_var('func_173')
call_2277 = relay.TupleGetItem(func_171_call(), 1)
call_2278 = relay.TupleGetItem(func_173_call(), 1)
var_2284 = relay.var("var_2284", dtype = "int16", shape = (2, 11, 7))#candidate|2284|(2, 11, 7)|var|int16
bop_2285 = relay.left_shift(call_2277.astype('int16'), relay.reshape(var_2284.astype('int16'), relay.shape_of(call_2277))) # shape=(2, 11, 7)
bop_2288 = relay.left_shift(call_2278.astype('int16'), relay.reshape(var_2284.astype('int16'), relay.shape_of(call_2278))) # shape=(2, 11, 7)
output = bop_2285
output2 = bop_2288
func_2290 = relay.Function([var_2284,], output)
mod['func_2290'] = func_2290
mod = relay.transform.InferType()(mod)
var_2291 = relay.var("var_2291", dtype = "int16", shape = (2, 11, 7))#candidate|2291|(2, 11, 7)|var|int16
output = func_2290(var_2291)
func_2292 = relay.Function([var_2291], output)
mutated_mod['func_2292'] = func_2292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_543_call = mod.get_global_var('func_543')
func_545_call = mutated_mod.get_global_var('func_545')
call_2296 = func_543_call()
call_2297 = func_543_call()
uop_2298 = relay.exp(call_2296.astype('float64')) # shape=(14, 2, 8)
uop_2300 = relay.exp(call_2297.astype('float64')) # shape=(14, 2, 8)
bop_2308 = relay.less(uop_2298.astype('bool'), relay.reshape(call_2296.astype('bool'), relay.shape_of(uop_2298))) # shape=(14, 2, 8)
bop_2311 = relay.less(uop_2300.astype('bool'), relay.reshape(call_2297.astype('bool'), relay.shape_of(uop_2300))) # shape=(14, 2, 8)
output = bop_2308
output2 = bop_2311
func_2314 = relay.Function([], output)
mod['func_2314'] = func_2314
mod = relay.transform.InferType()(mod)
mutated_mod['func_2314'] = func_2314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2314_call = mutated_mod.get_global_var('func_2314')
call_2315 = func_2314_call()
output = call_2315
func_2316 = relay.Function([], output)
mutated_mod['func_2316'] = func_2316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1085_call = mod.get_global_var('func_1085')
func_1087_call = mutated_mod.get_global_var('func_1087')
call_2339 = relay.TupleGetItem(func_1085_call(), 0)
call_2340 = relay.TupleGetItem(func_1087_call(), 0)
output = relay.Tuple([call_2339,])
output2 = relay.Tuple([call_2340,])
func_2342 = relay.Function([], output)
mod['func_2342'] = func_2342
mod = relay.transform.InferType()(mod)
output = func_2342()
func_2343 = relay.Function([], output)
mutated_mod['func_2343'] = func_2343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2314_call = mod.get_global_var('func_2314')
func_2316_call = mutated_mod.get_global_var('func_2316')
call_2361 = func_2314_call()
call_2362 = func_2314_call()
func_2314_call = mod.get_global_var('func_2314')
func_2316_call = mutated_mod.get_global_var('func_2316')
call_2363 = func_2314_call()
call_2364 = func_2314_call()
func_590_call = mod.get_global_var('func_590')
func_591_call = mutated_mod.get_global_var('func_591')
call_2372 = func_590_call()
call_2373 = func_590_call()
output = relay.Tuple([call_2361,call_2363,call_2372,])
output2 = relay.Tuple([call_2362,call_2364,call_2373,])
func_2374 = relay.Function([], output)
mod['func_2374'] = func_2374
mod = relay.transform.InferType()(mod)
mutated_mod['func_2374'] = func_2374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2374_call = mutated_mod.get_global_var('func_2374')
call_2375 = func_2374_call()
output = call_2375
func_2376 = relay.Function([], output)
mutated_mod['func_2376'] = func_2376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1085_call = mod.get_global_var('func_1085')
func_1087_call = mutated_mod.get_global_var('func_1087')
call_2410 = relay.TupleGetItem(func_1085_call(), 0)
call_2411 = relay.TupleGetItem(func_1087_call(), 0)
var_2415 = relay.var("var_2415", dtype = "float64", shape = (14, 2, 8))#candidate|2415|(14, 2, 8)|var|float64
bop_2416 = relay.bitwise_or(call_2410.astype('uint16'), relay.reshape(var_2415.astype('uint16'), relay.shape_of(call_2410))) # shape=(14, 2, 8)
bop_2419 = relay.bitwise_or(call_2411.astype('uint16'), relay.reshape(var_2415.astype('uint16'), relay.shape_of(call_2411))) # shape=(14, 2, 8)
output = relay.Tuple([bop_2416,])
output2 = relay.Tuple([bop_2419,])
func_2439 = relay.Function([var_2415,], output)
mod['func_2439'] = func_2439
mod = relay.transform.InferType()(mod)
mutated_mod['func_2439'] = func_2439
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2440 = relay.var("var_2440", dtype = "float64", shape = (14, 2, 8))#candidate|2440|(14, 2, 8)|var|float64
func_2439_call = mutated_mod.get_global_var('func_2439')
call_2441 = func_2439_call(var_2440)
output = call_2441
func_2442 = relay.Function([var_2440], output)
mutated_mod['func_2442'] = func_2442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1816_call = mod.get_global_var('func_1816')
func_1817_call = mutated_mod.get_global_var('func_1817')
call_2480 = relay.TupleGetItem(func_1816_call(), 0)
call_2481 = relay.TupleGetItem(func_1817_call(), 0)
func_2154_call = mod.get_global_var('func_2154')
func_2158_call = mutated_mod.get_global_var('func_2158')
var_2487 = relay.var("var_2487", dtype = "int16", shape = (154,))#candidate|2487|(154,)|var|int16
var_2488 = relay.var("var_2488", dtype = "uint64", shape = (1, 2816))#candidate|2488|(1, 2816)|var|uint64
call_2486 = relay.TupleGetItem(func_2154_call(relay.reshape(var_2487.astype('int16'), [154,]), relay.reshape(var_2488.astype('uint64'), [2816,]), ), 1)
call_2489 = relay.TupleGetItem(func_2158_call(relay.reshape(var_2487.astype('int16'), [154,]), relay.reshape(var_2488.astype('uint64'), [2816,]), ), 1)
uop_2496 = relay.sinh(var_2488.astype('float32')) # shape=(1, 2816)
func_561_call = mod.get_global_var('func_561')
func_563_call = mutated_mod.get_global_var('func_563')
call_2498 = func_561_call()
call_2499 = func_561_call()
uop_2504 = relay.sqrt(uop_2496.astype('float32')) # shape=(1, 2816)
output = relay.Tuple([call_2480,call_2486,var_2487,call_2498,uop_2504,])
output2 = relay.Tuple([call_2481,call_2489,var_2487,call_2499,uop_2504,])
func_2528 = relay.Function([var_2487,var_2488,], output)
mod['func_2528'] = func_2528
mod = relay.transform.InferType()(mod)
mutated_mod['func_2528'] = func_2528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2528_call = mutated_mod.get_global_var('func_2528')
var_2530 = relay.var("var_2530", dtype = "int16", shape = (154,))#candidate|2530|(154,)|var|int16
var_2531 = relay.var("var_2531", dtype = "uint64", shape = (1, 2816))#candidate|2531|(1, 2816)|var|uint64
call_2529 = func_2528_call(var_2530,var_2531,)
output = call_2529
func_2532 = relay.Function([var_2530,var_2531,], output)
mutated_mod['func_2532'] = func_2532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_657_call = mod.get_global_var('func_657')
func_658_call = mutated_mod.get_global_var('func_658')
call_2570 = func_657_call()
call_2571 = func_657_call()
func_543_call = mod.get_global_var('func_543')
func_545_call = mutated_mod.get_global_var('func_545')
call_2588 = func_543_call()
call_2589 = func_543_call()
output = relay.Tuple([call_2570,call_2588,])
output2 = relay.Tuple([call_2571,call_2589,])
func_2592 = relay.Function([], output)
mod['func_2592'] = func_2592
mod = relay.transform.InferType()(mod)
output = func_2592()
func_2593 = relay.Function([], output)
mutated_mod['func_2593'] = func_2593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2592_call = mod.get_global_var('func_2592')
func_2593_call = mutated_mod.get_global_var('func_2593')
call_2635 = relay.TupleGetItem(func_2592_call(), 1)
call_2636 = relay.TupleGetItem(func_2593_call(), 1)
output = relay.Tuple([call_2635,])
output2 = relay.Tuple([call_2636,])
func_2651 = relay.Function([], output)
mod['func_2651'] = func_2651
mod = relay.transform.InferType()(mod)
output = func_2651()
func_2652 = relay.Function([], output)
mutated_mod['func_2652'] = func_2652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_813_call = mod.get_global_var('func_813')
func_814_call = mutated_mod.get_global_var('func_814')
call_2660 = relay.TupleGetItem(func_813_call(), 0)
call_2661 = relay.TupleGetItem(func_814_call(), 0)
func_1431_call = mod.get_global_var('func_1431')
func_1433_call = mutated_mod.get_global_var('func_1433')
call_2669 = func_1431_call()
call_2670 = func_1431_call()
func_543_call = mod.get_global_var('func_543')
func_545_call = mutated_mod.get_global_var('func_545')
call_2689 = func_543_call()
call_2690 = func_543_call()
output = relay.Tuple([call_2660,call_2669,call_2689,])
output2 = relay.Tuple([call_2661,call_2670,call_2690,])
func_2729 = relay.Function([], output)
mod['func_2729'] = func_2729
mod = relay.transform.InferType()(mod)
mutated_mod['func_2729'] = func_2729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2729_call = mutated_mod.get_global_var('func_2729')
call_2730 = func_2729_call()
output = call_2730
func_2731 = relay.Function([], output)
mutated_mod['func_2731'] = func_2731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1946_call = mod.get_global_var('func_1946')
func_1948_call = mutated_mod.get_global_var('func_1948')
call_2732 = relay.TupleGetItem(func_1946_call(), 0)
call_2733 = relay.TupleGetItem(func_1948_call(), 0)
output = relay.Tuple([call_2732,])
output2 = relay.Tuple([call_2733,])
func_2741 = relay.Function([], output)
mod['func_2741'] = func_2741
mod = relay.transform.InferType()(mod)
output = func_2741()
func_2742 = relay.Function([], output)
mutated_mod['func_2742'] = func_2742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1431_call = mod.get_global_var('func_1431')
func_1433_call = mutated_mod.get_global_var('func_1433')
call_2765 = func_1431_call()
call_2766 = func_1431_call()
output = relay.Tuple([call_2765,])
output2 = relay.Tuple([call_2766,])
func_2769 = relay.Function([], output)
mod['func_2769'] = func_2769
mod = relay.transform.InferType()(mod)
mutated_mod['func_2769'] = func_2769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2769_call = mutated_mod.get_global_var('func_2769')
call_2770 = func_2769_call()
output = call_2770
func_2771 = relay.Function([], output)
mutated_mod['func_2771'] = func_2771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2592_call = mod.get_global_var('func_2592')
func_2593_call = mutated_mod.get_global_var('func_2593')
call_2797 = relay.TupleGetItem(func_2592_call(), 0)
call_2798 = relay.TupleGetItem(func_2593_call(), 0)
func_561_call = mod.get_global_var('func_561')
func_563_call = mutated_mod.get_global_var('func_563')
call_2817 = func_561_call()
call_2818 = func_561_call()
func_171_call = mod.get_global_var('func_171')
func_173_call = mutated_mod.get_global_var('func_173')
call_2823 = relay.TupleGetItem(func_171_call(), 2)
call_2824 = relay.TupleGetItem(func_173_call(), 2)
bop_2849 = relay.divide(call_2797.astype('float32'), relay.reshape(call_2823.astype('float32'), relay.shape_of(call_2797))) # shape=(2, 11, 7)
bop_2852 = relay.divide(call_2798.astype('float32'), relay.reshape(call_2824.astype('float32'), relay.shape_of(call_2798))) # shape=(2, 11, 7)
output = relay.Tuple([call_2817,bop_2849,])
output2 = relay.Tuple([call_2818,bop_2852,])
func_2854 = relay.Function([], output)
mod['func_2854'] = func_2854
mod = relay.transform.InferType()(mod)
output = func_2854()
func_2855 = relay.Function([], output)
mutated_mod['func_2855'] = func_2855
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2887 = relay.var("var_2887", dtype = "float64", shape = (7, 1, 6))#candidate|2887|(7, 1, 6)|var|float64
uop_2888 = relay.cos(var_2887.astype('float64')) # shape=(7, 1, 6)
uop_2891 = relay.log10(var_2887.astype('float64')) # shape=(7, 1, 6)
func_1723_call = mod.get_global_var('func_1723')
func_1726_call = mutated_mod.get_global_var('func_1726')
var_2895 = relay.var("var_2895", dtype = "float32", shape = (72, 1))#candidate|2895|(72, 1)|var|float32
call_2894 = func_1723_call(relay.reshape(var_2895.astype('float32'), [9, 2, 4]))
call_2896 = func_1723_call(relay.reshape(var_2895.astype('float32'), [9, 2, 4]))
uop_2903 = relay.atan(uop_2891.astype('float32')) # shape=(7, 1, 6)
uop_2905 = relay.acosh(uop_2903.astype('float64')) # shape=(7, 1, 6)
output = relay.Tuple([uop_2888,call_2894,var_2895,uop_2905,])
output2 = relay.Tuple([uop_2888,call_2896,var_2895,uop_2905,])
func_2916 = relay.Function([var_2887,var_2895,], output)
mod['func_2916'] = func_2916
mod = relay.transform.InferType()(mod)
mutated_mod['func_2916'] = func_2916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2916_call = mutated_mod.get_global_var('func_2916')
var_2918 = relay.var("var_2918", dtype = "float64", shape = (7, 1, 6))#candidate|2918|(7, 1, 6)|var|float64
var_2919 = relay.var("var_2919", dtype = "float32", shape = (72, 1))#candidate|2919|(72, 1)|var|float32
call_2917 = func_2916_call(var_2918,var_2919,)
output = call_2917
func_2920 = relay.Function([var_2918,var_2919,], output)
mutated_mod['func_2920'] = func_2920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1037_call = mod.get_global_var('func_1037')
func_1039_call = mutated_mod.get_global_var('func_1039')
call_2969 = func_1037_call()
call_2970 = func_1037_call()
func_2651_call = mod.get_global_var('func_2651')
func_2652_call = mutated_mod.get_global_var('func_2652')
call_2976 = relay.TupleGetItem(func_2651_call(), 0)
call_2977 = relay.TupleGetItem(func_2652_call(), 0)
output = relay.Tuple([call_2969,call_2976,])
output2 = relay.Tuple([call_2970,call_2977,])
func_3000 = relay.Function([], output)
mod['func_3000'] = func_3000
mod = relay.transform.InferType()(mod)
mutated_mod['func_3000'] = func_3000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3000_call = mutated_mod.get_global_var('func_3000')
call_3001 = func_3000_call()
output = call_3001
func_3002 = relay.Function([], output)
mutated_mod['func_3002'] = func_3002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_895_call = mod.get_global_var('func_895')
func_896_call = mutated_mod.get_global_var('func_896')
call_3017 = relay.TupleGetItem(func_895_call(), 0)
call_3018 = relay.TupleGetItem(func_896_call(), 0)
func_561_call = mod.get_global_var('func_561')
func_563_call = mutated_mod.get_global_var('func_563')
call_3050 = func_561_call()
call_3051 = func_561_call()
output = relay.Tuple([call_3017,call_3050,])
output2 = relay.Tuple([call_3018,call_3051,])
func_3065 = relay.Function([], output)
mod['func_3065'] = func_3065
mod = relay.transform.InferType()(mod)
mutated_mod['func_3065'] = func_3065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3065_call = mutated_mod.get_global_var('func_3065')
call_3066 = func_3065_call()
output = call_3066
func_3067 = relay.Function([], output)
mutated_mod['func_3067'] = func_3067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_561_call = mod.get_global_var('func_561')
func_563_call = mutated_mod.get_global_var('func_563')
call_3076 = func_561_call()
call_3077 = func_561_call()
var_3080 = relay.var("var_3080", dtype = "float64", shape = (14, 2, 8))#candidate|3080|(14, 2, 8)|var|float64
bop_3081 = relay.mod(call_3076.astype('float32'), relay.reshape(var_3080.astype('float32'), relay.shape_of(call_3076))) # shape=(14, 2, 8)
bop_3084 = relay.mod(call_3077.astype('float32'), relay.reshape(var_3080.astype('float32'), relay.shape_of(call_3077))) # shape=(14, 2, 8)
func_2154_call = mod.get_global_var('func_2154')
func_2158_call = mutated_mod.get_global_var('func_2158')
const_3105 = relay.const([5,5,-4,1,-9,1,7,-9,-8,2,-10,1,10,-8,-4,6,-4,3,8,-7,6,2,9,6,-2,9,7,-10,1,5,-7,-7,2,9,4,6,6,-5,9,-4,-2,-3,-4,3,-2,-3,9,-10,-9,-10,8,3,4,-1,-7,-4,-8,7,-1,-1,1,4,5,-1,-6,5,7,-8,-4,-3,-1,-2,-5,3,1,1,-10,-4,-10,7,-5,7,-10,2,1,-7,-2,3,7,-1,2,2,6,6,8,1,-6,7,3,-10,-3,-9,5,10,2,10,-5,7,-6,-1,-6,2,-1,8,6,-10,-2,-4,3,-8,-9,-10,-1,-10,-1,3,-1,9,-4,8,2,1,-9,2,-2,8,9,6,8,-6,6,4,6,1,-10,-2,-9,6,-7,-3,-9,10,10,7], dtype = "int16")#candidate|3105|(154,)|const|int16
const_3106 = relay.const([6,-4,-7,4,10,1,6,-4,-9,3,2,2,9,10,-1,-8,-4,-7,-3,-1,7,-5,-3,7,2,3,-1,5,-10,-5,10,7,-6,-7,7,1,1,9,7,-5,6,-10,-4,7,2,2,-7,-7,5,-3,-1,8,-2,-5,3,-7,-7,-5,4,2,6,-9,5,8,-10,-4,-5,5,9,6,2,-10,2,10,7,-1,8,-6,6,2,-4,6,-7,7,-3,-10,8,-3,-5,-6,5,-5,-9,-3,-4,-10,-9,8,-1,4,9,8,3,-8,2,-9,3,-7,7,-7,5,9,-8,-4,1,-3,-1,8,2,-10,-9,-1,-5,5,10,-2,3,-3,-8,10,-4,-2,3,10,-3,10,-1,4,-1,9,1,10,-3,-5,-9,-4,9,9,3,7,-10,-10,10,-9,3,4,-9,9,9,-7,-10,-1,-5,1,10,8,9,-2,-1,1,9,9,-2,-2,-4,-9,-9,1,3,-6,4,-4,1,1,9,8,-9,-7,-7,2,-9,-4,-3,4,9,-10,3,5,2,-8,7,-8,-4,7,-8,-3,-2,-7,3,1,-3,-4,-5,-2,4,7,-7,8,-3,-3,6,8,-2,-2,-6,7,-6,-8,2,7,10,-7,-10,-6,-10,2,4,3,-4,-3,10,2,4,6,-7,-4,-8,4,8,10,3,-5,1,5,4,8,9,-1,-9,9,-1,-7,-3,-6,-2,-8,-8,4,-2,-9,-6,-2,8,-7,2,6,-8,4,-3,2,-9,-2,3,8,-4,2,3,-6,7,9,1,3,-8,1,-7,7,-1,-3,-7,-2,10,-3,-7,-6,-6,4,-2,-5,3,-10,-8,6,-9,6,2,7,1,4,10,-2,7,-4,-2,7,-6,6,7,-3,-3,-10,-8,-6,6,-7,-2,-5,-7,-7,-9,-4,5,-10,4,-7,-4,-9,-4,1,6,8,-9,8,3,4,-2,-10,-8,9,2,6,-3,-8,1,8,-7,7,3,-1,1,-10,-4,1,-1,-6,6,-10,-9,7,8,-1,-4,-3,4,-5,1,-9,8,-9,-2,-1,-6,-1,-1,-9,6,6,-8,8,4,6,-9,-10,-9,-5,3,3,-8,8,-3,-8,7,-2,4,-7,-5,4,10,-10,-5,1,-2,-1,9,10,6,-2,6,8,-3,-8,7,-2,-8,-7,-9,4,5,4,5,-7,-3,-4,2,-9,-6,-5,1,-10,-4,-3,-9,6,4,-9,3,-10,4,5,5,-5,1,3,-9,-2,-2,-6,3,7,10,-6,2,7,-9,4,-8,-4,6,2,10,8,8,5,4,9,-5,-6,3,3,-8,8,5,-5,-1,8,-1,-5,8,10,-9,-7,8,-3,7,-2,6,-2,-2,-2,6,-6,6,-5,1,-8,8,9,9,4,-10,2,6,7,-3,-3,-8,-5,10,9,-9,4,-2,-3,4,8,6,2,-6,-2,-7,-7,5,9,3,-9,-7,-10,-5,-4,2,5,-2,2,5,6,-2,-6,4,-4,-7,9,-7,5,-2,3,10,4,2,-9,-9,-8,7,-9,3,-10,-8,4,-8,7,9,5,-5,-1,-4,-5,-7,-5,-1,7,-6,4,-6,9,-1,-5,6,10,-9,-2,3,-6,-4,-9,3,-9,-5,-5,5,-6,-2,-7,-2,-2,9,-6,3,7,4,2,-3,8,-8,-8,9,-1,6,-9,-6,3,-7,2,-10,-7,4,-4,4,5,-7,7,9,-6,8,5,-8,-1,-7,5,1,-4,3,4,-9,9,3,1,4,9,5,-5,-4,8,-1,-9,-4,9,-8,-3,5,-5,8,2,-5,3,7,-5,-4,2,-7,-8,-3,-6,-4,-10,-1,-7,2,10,-10,-9,10,-8,10,-2,1,6,10,7,-3,3,3,-4,9,2,8,8,9,4,4,-6,7,10,-4,-9,3,10,4,-3,-7,-4,-8,4,-8,7,-4,8,-5,-7,5,-5,-10,6,-8,-6,-4,1,-3,-9,3,5,-9,9,1,-4,-5,-5,-3,-8,-10,7,7,5,-2,2,-2,-3,10,-6,1,5,8,-1,-1,-1,5,6,-7,3,7,7,4,2,-3,3,10,-9,8,-9,-9,1,-10,6,-7,-9,6,-6,5,4,-8,-3,5,-7,10,-1,8,-2,8,-8,-9,-1,-2,-7,5,-6,-8,-3,10,3,8,10,-5,-6,10,-10,-10,6,-6,-8,6,-5,-2,-5,-8,4,-4,4,5,-4,6,6,3,-8,8,-9,10,7,2,-6,-4,-8,3,8,4,4,4,-5,-3,5,1,-4,-9,2,-6,-4,7,7,-6,7,-6,1,1,8,-1,5,-10,2,1,3,-4,-6,-8,2,-9,-5,2,-9,-6,-8,2,8,4,1,7,3,-2,-4,-3,6,7,-8,-1,-5,6,1,-7,-9,-2,6,-6,-1,-7,9,-1,-3,8,9,-10,4,8,-3,-8,-7,3,-10,-2,9,5,-1,-5,-7,6,4,-2,2,-6,6,5,6,9,-1,6,2,8,-8,-6,7,2,-9,-10,4,-4,-1,6,-1,5,5,9,-3,-9,-1,-7,-8,-8,3,6,5,10,2,-3,-10,-4,10,-2,-2,5,7,-2,10,10,9,3,-9,-9,-8,6,1,-2,-5,3,5,-3,-9,-7,-6,-4,-6,-8,-7,-8,9,4,-3,-2,-1,6,-4,-8,5,-2,4,-5,-3,3,-9,-7,-4,10,-7,6,7,4,2,-2,9,9,2,-2,-8,-4,-6,7,2,-9,-10,-7,-10,6,-2,10,-6,5,-2,10,-1,-9,7,-9,5,-8,-5,-2,3,-7,-8,-8,-6,2,-9,-2,-9,7,8,3,-6,-8,5,7,10,4,-3,-2,-7,-10,9,5,2,-3,2,6,8,-10,-6,10,-3,3,1,8,2,-4,-8,10,-3,-10,1,-2,10,2,10,-9,10,-2,9,-9,-8,3,-2,-5,6,-9,-9,-5,-4,4,-1,-1,-9,2,-3,-1,1,-6,-9,-7,4,1,6,4,-5,6,-5,8,9,2,-10,2,8,-6,7,-1,9,6,-10,-7,-3,2,7,-2,2,10,-8,5,10,-3,7,10,6,3,-8,-4,3,-9,-5,-9,-6,9,1,9,7,8,6,2,-6,1,-7,-5,10,-5,4,4,-2,3,8,5,-6,1,-1,-5,2,-10,-10,1,8,4,9,3,2,-5,10,8,-4,-7,4,3,9,-6,8,-8,3,-10,2,6,-9,-4,2,4,-1,-1,4,-2,7,1,-5,-2,3,-5,-3,-8,-1,-1,4,-8,-6,-1,-3,3,-3,3,-7,8,-7,6,-3,2,9,-8,-9,-10,-7,5,-8,-8,-5,8,-8,-2,1,-4,-4,-2,-10,-6,9,3,-8,6,7,4,-6,5,-1,8,-7,-10,-9,-2,3,7,3,-7,-6,-7,-8,-6,5,8,-10,-10,9,6,2,-6,-5,8,10,-10,-10,-1,8,-1,-1,-1,-5,6,2,-1,-9,9,9,3,-3,-6,-2,1,6,-4,-3,6,5,4,-3,2,-4,-7,8,-2,6,6,-5,-7,9,8,4,1,-5,7,-10,1,9,6,-1,-10,6,-3,1,4,1,3,5,7,9,-9,4,-4,9,10,-8,-4,-6,-7,-9,8,-2,-7,5,8,-9,-2,6,-6,7,4,-6,-2,-7,1,4,8,-10,-5,-9,10,10,1,-9,-3,-2,-2,9,-3,6,4,1,6,-7,8,-3,-5,10,9,2,-6,2,5,5,-8,9,-1,-6,-4,7,10,-2,-3,3,-4,7,-1,9,10,5,-6,-2,9,-5,2,6,-4,-10,-1,-10,-10,-4,-5,9,10,3,-10,-3,4,1,2,1,8,-2,4,5,-10,-5,3,-10,9,8,-8,-8,1,-10,1,-8,3,-7,3,-9,2,-7,9,7,-1,-7,10,-3,9,3,-7,8,-10,-6,-8,3,10,-4,-7,7,7,-7,3,7,5,1,-8,1,5,-10,-4,-2,5,5,6,10,-10,-10,8,5,9,3,-7,7,2,5,-10,-2,1,-7,-1,-2,-5,-2,-2,-6,4,-8,4,3,3,-3,4,-8,-5,2,3,7,-6,10,-7,-9,-6,2,-4,-7,2,10,7,1,-2,-10,-6,-2,7,4,-8,4,2,3,10,3,-2,-8,-8,3,-1,-4,9,3,9,9,-10,9,-1,-8,-2,7,-1,-3,3,10,8,-2,1,2,-3,-7,-7,5,-9,-1,5,7,2,-6,7,-10,1,3,-9,3,-7,5,7,4,-4,-10,-4,4,8,-2,5,3,7,-9,2,-8,-10,-5,-2,4,-3,-4,1,2,7,6,9,7,7,10,-6,8,-1,5,-1,9,3,-10,3,-6,7,10,3,-2,5,-10,10,9,1,5,4,6,1,-4,10,-3,-3,-3,-2,7,-6,-8,-4,-10,-2,-9,-10,6,2,6,-1,9,1,10,-8,3,-3,2,10,2,-6,-10,5,10,9,9,4,-4,3,-10,-3,7,-6,3,1,-9,8,7,-9,-3,2,10,2,-1,-10,-6,-6,10,1,7,1,-1,9,-2,-5,-7,-7,-3,1,-3,-4,5,-9,-1,10,-2,-8,-8,1,5,5,2,-1,10,-8,-4,-10,-2,5,9,3,-6,4,-6,-6,-10,-5,2,7,7,-4,8,3,5,3,-5,5,5,-5,-2,-2,-1,-5,2,-4,-7,-1,4,-5,1,-1,2,8,-5,10,6,-2,-8,2,10,10,-6,-4,-4,9,7,-4,8,-8,-8,2,10,-3,-2,-10,-4,-10,1,3,3,1,-6,8,-10,8,-5,-2,-4,-3,3,-9,-4,-7,4,-8,-4,8,-7,-5,-3,3,-5,2,3,8,-9,-2,7,-5,1,-10,6,6,-4,-10,-8,-6,-1,4,4,-9,10,-3,5,8,3,3,-5,3,-2,8,-8,-2,-3,-1,8,-7,5,5,-9,-6,-4,4,-7,-1,-9,-6,-3,6,-5,-10,-10,3,-6,5,-3,10,7,-7,10,-3,6,8,10,-3,10,9,-10,-5,-1,4,1,-1,7,-5,7,7,-9,-1,8,5,-7,10,-7,6,5,-1,-5,5,2,2,-9,-3,6,9,-7,-4,9,4,8,3,9,10,-8,-7,-8,-10,-7,-5,-6,-9,-9,9,-6,3,2,-9,-1,6,-5,-10,3,-10,-4,5,9,4,6,7,6,-8,-7,-1,8,-8,4,6,9,-10,-10,4,9,-9,-1,1,-8,8,-5,-6,10,-6,3,2,9,-6,6,-10,7,-4,-8,8,3,3,-8,-3,-2,-1,-2,-8,4,9,5,-7,-1,-3,-3,4,10,3,6,-6,-4,3,1,-6,7,-7,5,7,4,-6,2,2,-9,9,3,-2,-4,5,-8,2,-6,-8,-2,10,6,2,6,-9,1,10,7,2,-9,-7,-10,2,8,1,-8,4,5,-1,10,-7,2,-6,9,8,-7,-5,-6,4,-1,-1,-4,-3,1,-3,4,1,-7,-2,-6,-4,-7,-9,10,-6,8,9,4,-10,-6,7,3,5,-6,-8,-1,-5,-3,-3,8,5,-9,-8,6,8,-3,1,5,-7,5,1,-8,-4,1,-6,-7,6,5,6,2,-1,-1,2,-10,-6,2,9,-6,-3,-10,-9,-9,-10,-9,-6,-4,-7,-1,2,-5,4,-10,9,8,4,-2,5,-9,6,5,8,-8,6,-1,-1,-9,-6,-2,4,7,-7,2,-10,1,9,-9,5,4,-9,10,-3,-6,7,-4,-7,-10,1,10,-4,-1,-7,4,8,-3,-4,6,3,6,10,-10,2,3,3,9,4,-2,8,3,3,2,9,5,-10,2,1,-8,2,-10,-7,-2,-9,-2,-8,5,-10,-9,7,-3,-4,-8,6,10,9,3,-9,9,-9,6,-5,-1,10,-6,-3,-3,-3,-10,8,9,1,5,6,9,4,-3,8,4,3,4,-10,-10,9,3,3,-7,3,4,6,5,3,-1,-3,1,-6,1,-4,-10,-3,10,-3,10,-9,-7,10,-6,-1,5,1,-9,3,-4,1,1,5,1,10,-5,-6,5,6,10,-10,1,-3,10,-10,-4,-8,-6,8,-2,9,-7,-2,10,8,5,-4,-1,5,-4,6,8,5,-7,-3,1,-10,4,3,-2,-3,8,1,6,-1,-5,-10,-2,-6,8,-10,9,9,4,9,-2,-2,2,2,-1,10,-1,-8,-7,-2,6,-6,-3,-10,5,-2,-2,1,-8,-3,9,7,-6,-5,-1,-10,10,-4,8,-10,3,-4,-6,10,2,-5,9,-1,10,9,-2,10,6,-6,8,-9,-8,8,10,10,-1,2,-8,6,10,1,8,-5,3,-9,5,-4,3,-9,-9,-6,5,-2,-3,-2,8,5,3,8,-9,-9,-5,9,4,-10,8,-5,3,5,8,7,9,9,9,-9,2,-5,10,4,4,7,9,-3,7,-6,-5,10,2,7,-5,-2,-4,-6,2,8,-4,-8,-5,3,10,9,-2,-1,-6,-10,7,-2,10,5,9,-8,6,-8,-6,5,10,-3,-10,-9,-5,9,-2,4,10,3,-3,-2,8,2,-1,-10,-10,7,9,8,6,7,8,-9,-3,8,5,6,2,-7,-8,5,-2,-8,10,-7,3,4,7,10,6,-5,9,-4,1,3,-8,7,-3,-1,1,9,3,-5,-7,-8,4,5,5,4,9,-7,-8,-7,9,3,-7,6,-8,-8,-10,1,10,-7,3,4,9,-9,6,-7,5,7,-6,9,7,-10,-4,1,7,10,1,2,-5,-8,-8,-8,-9,-2,-9,9,-8,3,2,-7,-3,-8,3,4,-2,1,-9,4,5,1,9,-1,10,3,9,-10,-9,7,-10,-3,5,-4,-4,-2,-6,-4,6,-4,-3,-8,-6,-7,9,-10,6,1,7,8,6,2,-5,-9,-4,-7,9,-9,6,-4,1,1,-5,-9,-10,6,8,-7,4,4,-8,-5,6,6,2,-6,1,-8,-2,1,-5,5,4,-6,8,6,-9,-7,-7,-9,-10,-1,4,9,10,9,8,-9,-8,3,-5,3,2,-2,-10,7,8,5,9,10,-6,5,3,-6,-10,-6,-8,10,-9,-8,-5,-3,4,5,-1,-3,5,9,-1,-8,6,6,5,5,-10,6,-9,-8,-6,8,-1,-2,-6,-4,-8,8,6,-9,1,6,-6,-9,-1,9,4,-5,-8,-1,10,1,-6,3,4,5,-3,-9,3,-5,6,2,-1,5,3,-4,-9,-2,-6,9,6,-5,4,7,1,4,6,-7,10,-8,8,-6,9,-6,-3,-6,8,8,-7,-1,-9,-6,-10,1,7,-5,-3,3,-10,-10,-3,-2,10,-5,4,-5,-1,-7,-4,-3,10,-5,8,7,-7,1,-3,-1,2,10,-1,9,4,5,6,6,-3,-9,8,-10,-10,5,5,-6,9,5,1,-4,-9,2,6,-1,10,3,-5,3,6,-1,-3,2,-5,3,-10,-10,7,-6,1,-3,7,-10,-9,-10,-2,-9,-9,8,5,-9,-10,6,2,-2,9,-5,1,1,-10,-6,1,7,4,4,-7,-6,2], dtype = "uint64")#candidate|3106|(2816,)|const|uint64
call_3104 = relay.TupleGetItem(func_2154_call(relay.reshape(const_3105.astype('int16'), [154,]), relay.reshape(const_3106.astype('uint64'), [2816,]), ), 1)
call_3107 = relay.TupleGetItem(func_2158_call(relay.reshape(const_3105.astype('int16'), [154,]), relay.reshape(const_3106.astype('uint64'), [2816,]), ), 1)
output = relay.Tuple([bop_3081,call_3104,const_3105,const_3106,])
output2 = relay.Tuple([bop_3084,call_3107,const_3105,const_3106,])
func_3109 = relay.Function([var_3080,], output)
mod['func_3109'] = func_3109
mod = relay.transform.InferType()(mod)
var_3110 = relay.var("var_3110", dtype = "float64", shape = (14, 2, 8))#candidate|3110|(14, 2, 8)|var|float64
output = func_3109(var_3110)
func_3111 = relay.Function([var_3110], output)
mutated_mod['func_3111'] = func_3111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3065_call = mod.get_global_var('func_3065')
func_3067_call = mutated_mod.get_global_var('func_3067')
call_3127 = relay.TupleGetItem(func_3065_call(), 1)
call_3128 = relay.TupleGetItem(func_3067_call(), 1)
output = call_3127
output2 = call_3128
func_3144 = relay.Function([], output)
mod['func_3144'] = func_3144
mod = relay.transform.InferType()(mod)
mutated_mod['func_3144'] = func_3144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3144_call = mutated_mod.get_global_var('func_3144')
call_3145 = func_3144_call()
output = call_3145
func_3146 = relay.Function([], output)
mutated_mod['func_3146'] = func_3146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2374_call = mod.get_global_var('func_2374')
func_2376_call = mutated_mod.get_global_var('func_2376')
call_3160 = relay.TupleGetItem(func_2374_call(), 0)
call_3161 = relay.TupleGetItem(func_2376_call(), 0)
var_3178 = relay.var("var_3178", dtype = "bool", shape = (14, 2, 8))#candidate|3178|(14, 2, 8)|var|bool
bop_3179 = relay.subtract(call_3160.astype('float32'), relay.reshape(var_3178.astype('float32'), relay.shape_of(call_3160))) # shape=(14, 2, 8)
bop_3182 = relay.subtract(call_3161.astype('float32'), relay.reshape(var_3178.astype('float32'), relay.shape_of(call_3161))) # shape=(14, 2, 8)
func_937_call = mod.get_global_var('func_937')
func_939_call = mutated_mod.get_global_var('func_939')
call_3186 = relay.TupleGetItem(func_937_call(), 0)
call_3187 = relay.TupleGetItem(func_939_call(), 0)
func_1689_call = mod.get_global_var('func_1689')
func_1693_call = mutated_mod.get_global_var('func_1693')
var_3190 = relay.var("var_3190", dtype = "uint64", shape = (2816,))#candidate|3190|(2816,)|var|uint64
call_3189 = relay.TupleGetItem(func_1689_call(relay.reshape(call_3186.astype('float64'), [14, 2, 8]), relay.reshape(var_3190.astype('uint64'), [2816,]), ), 2)
call_3191 = relay.TupleGetItem(func_1693_call(relay.reshape(call_3186.astype('float64'), [14, 2, 8]), relay.reshape(var_3190.astype('uint64'), [2816,]), ), 2)
bop_3214 = relay.maximum(call_3189.astype('float64'), relay.reshape(var_3190.astype('float64'), relay.shape_of(call_3189))) # shape=(2816,)
bop_3217 = relay.maximum(call_3191.astype('float64'), relay.reshape(var_3190.astype('float64'), relay.shape_of(call_3191))) # shape=(2816,)
func_366_call = mod.get_global_var('func_366')
func_368_call = mutated_mod.get_global_var('func_368')
call_3218 = relay.TupleGetItem(func_366_call(relay.reshape(bop_3179.astype('float64'), [224,])), 2)
call_3219 = relay.TupleGetItem(func_368_call(relay.reshape(bop_3179.astype('float64'), [224,])), 2)
var_3232 = relay.var("var_3232", dtype = "float32", shape = (14, 2, 8))#candidate|3232|(14, 2, 8)|var|float32
bop_3233 = relay.floor_divide(bop_3179.astype('float32'), relay.reshape(var_3232.astype('float32'), relay.shape_of(bop_3179))) # shape=(14, 2, 8)
bop_3236 = relay.floor_divide(bop_3182.astype('float32'), relay.reshape(var_3232.astype('float32'), relay.shape_of(bop_3182))) # shape=(14, 2, 8)
output = relay.Tuple([call_3186,bop_3214,call_3218,bop_3233,])
output2 = relay.Tuple([call_3187,bop_3217,call_3219,bop_3236,])
func_3240 = relay.Function([var_3178,var_3190,var_3232,], output)
mod['func_3240'] = func_3240
mod = relay.transform.InferType()(mod)
mutated_mod['func_3240'] = func_3240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3240_call = mutated_mod.get_global_var('func_3240')
var_3242 = relay.var("var_3242", dtype = "bool", shape = (14, 2, 8))#candidate|3242|(14, 2, 8)|var|bool
var_3243 = relay.var("var_3243", dtype = "uint64", shape = (2816,))#candidate|3243|(2816,)|var|uint64
var_3244 = relay.var("var_3244", dtype = "float32", shape = (14, 2, 8))#candidate|3244|(14, 2, 8)|var|float32
call_3241 = func_3240_call(var_3242,var_3243,var_3244,)
output = call_3241
func_3245 = relay.Function([var_3242,var_3243,var_3244,], output)
mutated_mod['func_3245'] = func_3245
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3314 = relay.const([[[False,False,True,True,True,False,False,True,False,True,False,False,False,False],[False,False,False,False,False,False,True,False,False,False,True,True,True,False],[False,False,False,False,False,True,True,True,False,True,False,False,False,False]],[[False,False,True,False,True,True,False,True,True,True,True,True,True,False],[True,False,True,True,True,True,True,True,True,False,True,True,False,True],[True,False,False,True,True,True,True,False,False,False,True,True,True,False]],[[True,True,False,False,True,True,True,False,True,False,False,False,False,True],[True,False,False,False,True,False,True,False,True,False,False,True,False,True],[True,False,True,False,True,True,False,False,True,True,True,False,True,True]],[[False,True,False,True,False,False,True,True,True,False,True,False,False,True],[False,True,False,True,True,True,True,False,False,True,False,True,False,True],[True,True,False,True,False,False,False,False,True,True,True,False,True,False]],[[False,False,True,False,True,True,True,False,False,False,False,True,True,False],[False,True,False,False,False,False,True,True,True,False,True,False,True,True],[False,True,True,False,True,True,True,False,False,False,False,True,True,False]],[[False,False,False,False,False,False,False,False,True,False,True,False,False,True],[False,True,False,False,False,True,False,True,False,True,True,True,False,True],[False,True,True,False,True,False,False,True,False,True,False,True,True,True]]], dtype = "bool")#candidate|3314|(6, 3, 14)|const|bool
var_3315 = relay.var("var_3315", dtype = "bool", shape = (6, 3, 14))#candidate|3315|(6, 3, 14)|var|bool
bop_3316 = relay.logical_and(const_3314.astype('bool'), relay.reshape(var_3315.astype('bool'), relay.shape_of(const_3314))) # shape=(6, 3, 14)
func_2000_call = mod.get_global_var('func_2000')
func_2002_call = mutated_mod.get_global_var('func_2002')
call_3323 = func_2000_call()
call_3324 = func_2000_call()
output = relay.Tuple([bop_3316,call_3323,])
output2 = relay.Tuple([bop_3316,call_3324,])
func_3335 = relay.Function([var_3315,], output)
mod['func_3335'] = func_3335
mod = relay.transform.InferType()(mod)
mutated_mod['func_3335'] = func_3335
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3336 = relay.var("var_3336", dtype = "bool", shape = (6, 3, 14))#candidate|3336|(6, 3, 14)|var|bool
func_3335_call = mutated_mod.get_global_var('func_3335')
call_3337 = func_3335_call(var_3336)
output = call_3337
func_3338 = relay.Function([var_3336], output)
mutated_mod['func_3338'] = func_3338
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3347 = relay.var("var_3347", dtype = "int32", shape = (6, 7))#candidate|3347|(6, 7)|var|int32
const_3348 = relay.const([[6,-4,9,4,1,3,-9],[2,6,-10,-2,8,-10,4],[8,5,-3,2,4,-9,1],[2,5,-10,7,-3,-4,2],[3,-7,5,-6,4,2,6],[-4,3,9,-9,7,8,4]], dtype = "int32")#candidate|3348|(6, 7)|const|int32
bop_3349 = relay.bitwise_or(var_3347.astype('int32'), relay.reshape(const_3348.astype('int32'), relay.shape_of(var_3347))) # shape=(6, 7)
output = relay.Tuple([bop_3349,])
output2 = relay.Tuple([bop_3349,])
func_3364 = relay.Function([var_3347,], output)
mod['func_3364'] = func_3364
mod = relay.transform.InferType()(mod)
mutated_mod['func_3364'] = func_3364
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3365 = relay.var("var_3365", dtype = "int32", shape = (6, 7))#candidate|3365|(6, 7)|var|int32
func_3364_call = mutated_mod.get_global_var('func_3364')
call_3366 = func_3364_call(var_3365)
output = call_3366
func_3367 = relay.Function([var_3365], output)
mutated_mod['func_3367'] = func_3367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3065_call = mod.get_global_var('func_3065')
func_3067_call = mutated_mod.get_global_var('func_3067')
call_3419 = relay.TupleGetItem(func_3065_call(), 0)
call_3420 = relay.TupleGetItem(func_3067_call(), 0)
func_2528_call = mod.get_global_var('func_2528')
func_2532_call = mutated_mod.get_global_var('func_2532')
var_3422 = relay.var("var_3422", dtype = "int16", shape = (154,))#candidate|3422|(154,)|var|int16
const_3423 = relay.const([2,1,7,-5,4,2,-8,-6,-8,-2,10,10,-1,-2,-3,-4,8,6,5,-4,7,-2,7,-1,5,-6,3,6,-10,-3,-5,9,2,1,-7,10,-10,-8,-10,-4,4,2,3,3,8,10,3,-9,5,6,-4,5,-9,-5,-1,8,8,-5,7,8,-4,-1,8,-5,9,-4,-10,-10,-1,1,-3,-9,8,4,10,3,10,4,-3,8,2,6,10,-10,1,5,10,-7,-6,4,-4,-3,-2,-10,-5,4,2,-9,5,7,1,-2,-4,9,-1,-7,3,-9,4,-7,-10,8,2,8,7,3,-5,-10,5,8,-6,1,2,4,9,-7,-4,-3,-2,-4,-6,10,-4,-10,-4,7,3,1,9,-5,7,-9,9,-7,-5,-2,2,10,-4,6,-1,8,-2,1,-4,-2,-8,-2,-7,10,2,2,-5,1,-5,7,-10,9,-6,5,-7,-1,-2,-4,3,-10,5,10,-4,-1,-8,4,5,-1,-4,-1,5,-7,-4,-3,-4,-4,5,-1,5,-8,10,2,-5,-8,-7,-1,-10,9,-1,3,-7,8,-2,-3,-1,-1,-2,10,-4,-8,7,5,-10,-3,7,6,-2,-8,-3,3,-3,-9,-5,-4,-7,-10,-2,4,-9,2,-1,-2,5,9,-2,-4,-5,9,3,-9,-6,5,-5,-9,-5,2,1,1,5,-4,2,-1,-2,-9,2,5,8,-5,10,7,6,1,5,-1,-4,7,-2,7,7,-9,3,-8,-4,3,-10,7,-2,-3,-2,9,-9,6,-5,7,6,-4,8,9,6,3,-6,1,-1,-7,9,1,-2,-1,-9,-10,2,3,5,-3,-7,8,9,1,6,-4,-4,2,3,5,-2,6,-1,6,-2,9,-5,3,8,5,4,6,-8,3,4,3,5,3,-8,-1,8,-4,-7,-1,2,7,-7,3,-5,-5,6,-8,9,6,10,10,7,3,2,9,9,-8,-10,2,-9,6,-6,8,-4,3,-2,-4,-8,5,2,-3,-1,-9,-4,-8,-7,10,-1,-1,3,-10,8,7,2,7,7,5,5,-9,-5,3,3,7,4,-10,-1,-5,4,-8,-4,-8,-7,9,7,2,-6,5,-10,5,2,10,-6,4,-7,-4,-7,1,7,7,-7,7,-4,7,7,-8,9,-2,-5,5,-9,2,-3,-2,-3,4,10,7,6,-7,-8,-3,5,2,-2,-9,-5,-6,5,9,-1,-2,-8,4,-3,-8,8,-9,-7,-10,-9,-7,-1,5,5,6,8,-6,4,-10,-2,9,-2,-2,1,-5,2,-5,8,-1,-1,-8,2,5,3,5,6,7,4,4,-3,4,-4,10,-8,-5,-7,-7,-7,5,8,9,-5,1,-6,-7,-5,-8,-1,-8,-1,-7,6,-7,6,4,5,-9,10,2,-6,-6,-1,9,5,10,-2,4,10,-2,-5,-2,10,1,-5,5,-1,4,7,3,-3,-6,9,-5,-1,-5,5,-5,3,4,-10,-9,4,-4,-7,3,-9,8,-10,4,2,-8,-9,4,10,9,-9,-10,2,-5,10,-10,8,-6,3,-10,1,1,-2,1,-5,1,-9,-8,-4,1,-1,-2,10,-7,-9,-7,-4,2,5,5,6,-3,-6,7,4,-3,-10,5,-4,3,7,6,2,7,-3,-7,-8,-3,1,-4,7,-1,-4,-7,9,2,1,7,-5,-1,7,-5,-10,1,8,8,5,-10,-6,-5,-8,10,4,3,4,-8,-5,9,-3,7,-8,-7,-4,1,-4,4,-5,1,4,9,-1,-2,-1,-2,-1,-4,-3,1,-7,-7,1,5,8,5,4,-3,-2,3,-3,-8,1,-3,-4,-2,-9,4,-4,5,-8,5,4,-9,2,2,5,10,-1,-2,9,5,-5,-5,-1,3,1,-1,6,3,-2,-3,-4,-4,-8,-9,-10,-5,7,-6,-2,-8,-6,10,-1,-2,-8,1,-10,7,1,4,-10,8,1,-6,10,-6,4,-8,8,9,5,-8,-7,4,10,-3,9,8,7,2,9,-4,3,10,-4,-9,-1,5,-1,9,-8,-2,6,-4,-7,10,6,10,8,1,9,4,-7,1,9,-1,-4,2,4,-1,-4,-8,-5,-10,-6,-8,2,-8,-2,-9,9,-5,-3,-1,5,-10,4,-1,-6,-5,-3,9,4,4,-6,-6,3,8,-8,-4,2,4,-4,5,4,-2,3,-2,-7,-3,-1,8,10,-1,4,3,-1,-1,10,3,-8,-2,-4,-9,1,6,3,-8,-9,-3,-4,10,-1,-8,-1,-6,-6,1,1,5,-4,-7,-4,-9,-4,9,-9,3,3,3,-4,2,-7,2,-3,-1,-7,-3,3,-7,6,-5,6,-7,9,1,-8,5,-8,-5,-3,7,5,2,-3,5,4,4,-7,-7,2,-4,-2,8,-8,-10,-9,3,-6,4,-6,9,-10,-10,-6,7,-6,10,10,8,1,8,-3,-4,8,10,-8,1,-4,6,9,-7,4,3,-5,1,6,-6,10,2,7,-1,-3,-2,5,-6,-1,9,10,9,-2,-3,-10,1,-6,-10,-7,7,-3,-4,9,3,2,-7,-4,10,-7,-8,10,10,2,-1,1,6,1,2,-9,1,-7,-6,7,8,-10,4,6,8,-2,-7,-8,-6,-5,10,5,7,-2,-4,-10,-4,9,-2,9,-4,-10,-5,6,-9,2,-6,1,-9,-6,-9,-5,9,-10,-10,-1,-2,-7,-9,-2,3,6,-1,1,-9,2,7,2,1,7,10,8,-8,3,-6,-6,9,6,-8,-9,-8,-4,8,1,7,-3,-5,-3,3,-10,10,-10,9,-8,-5,-5,-8,7,6,-5,5,2,-6,5,-2,2,3,1,-8,-1,6,5,5,-7,-10,-6,10,-7,4,10,8,-9,2,5,9,-2,-1,8,-6,1,-9,3,4,8,3,-5,7,-4,-4,-8,6,-7,-6,-7,1,-8,-2,2,10,-7,7,6,5,-5,-10,1,5,-4,-4,3,8,8,4,-9,1,9,-7,-3,6,1,-5,3,10,-10,10,-2,7,-2,1,7,-7,-1,3,7,4,-7,-10,-8,10,5,-1,10,-6,-1,4,-10,-6,5,4,1,10,8,8,10,-4,-8,1,-3,10,5,-1,7,3,9,6,9,7,5,3,-1,-10,2,-9,-10,10,-5,10,10,-5,-3,10,4,7,-3,5,-7,-5,6,-5,-2,-2,6,10,5,7,-4,-10,-6,-10,-9,-3,9,5,-1,-4,5,-10,7,-7,5,2,2,-2,1,7,6,-8,7,10,6,-1,-9,-10,-2,9,-2,9,-5,4,2,5,1,-2,-9,-6,-6,3,-7,4,-3,-7,5,1,-8,5,-6,7,-6,-6,1,9,9,5,-9,3,1,7,9,-6,-6,-10,-1,-2,6,-1,1,6,-4,-4,-1,4,-1,8,2,-9,-4,1,-6,4,10,-10,-7,-9,-1,-3,1,4,10,-2,-7,1,9,-1,-2,8,-10,2,-9,8,5,-2,-3,-10,8,5,4,9,7,-10,-4,-10,-1,2,3,-9,3,7,-6,9,9,-1,2,-6,-1,8,7,10,10,7,3,-4,-7,-4,-7,1,9,-9,-4,-9,-3,10,5,-7,3,-10,2,-3,-4,4,-10,-7,6,1,1,7,-9,4,-9,8,-9,-6,-4,-9,-6,10,-9,4,-5,7,4,-9,-3,6,-6,-1,5,-3,6,7,-9,7,-6,-5,-7,6,-10,-6,-8,2,9,6,-1,-4,4,-1,10,3,9,8,2,-7,9,-5,8,-8,3,2,6,2,-7,3,1,5,5,5,-7,10,-8,2,4,-2,5,-10,-9,-1,3,6,-1,3,-6,3,-5,-1,10,8,5,-9,-3,3,1,-8,9,10,9,-6,-4,-10,4,1,-7,7,8,-4,5,10,-3,-2,-4,-4,6,8,1,-8,-1,8,-5,-2,3,3,-3,-5,3,9,-10,2,3,5,-10,-8,9,1,-2,-8,-6,6,3,-6,-1,-6,7,4,-10,3,-9,2,-6,-5,-3,5,3,1,-5,4,1,4,2,8,-8,-3,-2,6,-6,-8,3,10,-7,3,7,7,-1,-6,10,4,-6,6,2,4,2,-6,-5,2,-7,-3,6,4,2,2,-5,9,-3,-9,-6,2,-5,4,7,4,-5,-10,-9,-10,-6,3,9,5,7,-9,-5,3,-1,3,-3,6,6,-8,-2,-5,1,10,-2,-3,6,-1,3,4,1,6,4,3,-7,4,9,8,7,-9,-2,7,-4,-3,-4,-3,-2,-8,-10,-6,-4,-6,10,-5,3,-8,-6,-7,5,7,4,-2,-8,5,-3,-7,-9,-2,-9,6,10,-9,8,7,3,-3,-4,5,7,-2,-9,7,-1,7,-5,2,-8,10,-4,-1,10,5,-7,6,10,-4,6,-7,10,7,-8,9,-9,-1,-7,-9,4,-1,-4,-7,-4,3,4,-6,-3,-10,-1,6,1,2,-8,4,-5,-7,1,-3,-4,-8,-6,3,-9,-2,-5,10,-4,3,-5,7,4,-1,7,2,2,-10,-4,2,9,4,10,9,8,9,-10,3,10,9,-2,9,-10,-4,3,10,10,5,9,8,-7,-1,3,9,10,3,10,7,10,-6,9,-6,-1,-9,-6,-6,-3,-9,10,2,-9,-3,-6,9,-4,-2,3,10,-2,4,7,2,-6,-8,3,10,6,9,4,9,-6,-10,10,5,-2,-1,-9,-1,-6,-5,1,-8,-9,-9,8,-2,1,-5,4,5,9,5,9,-4,6,-1,-7,4,-10,10,2,-2,5,-6,-5,7,4,-3,1,-7,9,2,7,-1,-8,4,-6,-3,-4,-4,-9,-5,4,-8,-5,9,-3,1,8,8,6,6,-10,3,-9,5,7,-2,7,-5,5,10,7,-7,-5,1,-8,-1,7,10,-2,-1,-6,1,3,8,2,-3,9,-5,6,6,-4,-2,-3,-4,-9,4,-8,-9,-1,-8,-6,3,2,2,6,3,6,-9,-8,-4,10,2,-4,-8,9,9,6,3,-2,9,2,7,7,-9,-1,-2,2,8,5,1,1,-9,2,8,-6,1,8,8,-8,-10,9,-9,-6,-6,-4,-6,9,-3,-9,6,-5,-7,-6,8,-3,2,-10,4,-9,-10,-9,7,6,-8,10,-2,2,-8,8,2,-6,-3,7,-4,-8,-1,-3,-3,-8,-3,7,-3,-7,-7,9,-6,6,-1,7,-1,-2,-9,1,-3,5,7,-3,10,3,7,-7,-9,10,-5,-7,-1,-9,5,2,-8,6,-10,-8,-9,6,-5,6,-7,3,-5,-10,-3,-7,-8,-6,8,4,9,8,2,-3,-8,-10,9,-7,-6,-1,6,7,6,10,5,4,3,3,8,4,-9,9,10,2,-2,4,8,-10,7,2,4,-8,-8,4,-1,1,3,-7,5,10,10,-5,-7,5,-7,-6,3,-9,8,-6,-6,-8,7,3,-5,-1,-6,5,1,7,-7,10,10,-2,7,-7,4,-1,1,5,4,10,2,3,-5,3,5,5,-5,4,-4,-4,-6,-3,10,4,-4,5,-2,-9,-9,1,4,-9,-3,-2,4,9,-10,7,-10,5,5,-8,-6,-4,-9,-1,2,-3,-5,-6,-10,6,-7,1,6,-1,-4,8,6,-9,10,8,-1,9,-6,4,-9,-6,-7,-4,-1,-4,4,6,-5,-6,4,6,-5,-3,1,-6,10,-9,-9,8,9,-6,5,4,-7,-4,4,-8,9,1,9,-2,-9,5,-5,-9,-6,-1,7,10,8,8,-6,-3,10,-4,-3,-9,9,-2,9,-1,6,-4,9,-10,-8,9,7,-10,9,-9,10,7,-1,6,-2,-5,-10,3,2,6,-4,-3,-10,9,7,-2,-5,8,7,8,-10,-10,-1,-10,8,3,3,-4,-1,10,10,-6,-2,5,-10,-1,-5,3,-3,8,-10,-1,7,4,10,-7,-8,7,9,1,4,-2,-2,4,-9,-5,1,10,3,7,9,-6,-7,9,7,-7,-4,10,3,1,4,9,-4,-7,-4,-2,8,-2,-3,3,2,10,9,2,-4,4,-9,-7,-3,-1,9,-9,-3,4,-1,5,6,-1,-5,-7,-8,-9,3,1,10,-10,-9,-6,10,-10,4,8,1,5,4,9,2,-8,-3,10,3,2,10,4,-5,-3,-10,-1,10,-10,-9,-4,-6,7,-3,5,-8,10,3,10,-8,9,3,10,-5,6,9,4,-6,7,7,-7,-6,-4,1,-9,4,9,-9,1,-1,-7,-8,-8,-3,6,-4,4,8,-1,2,7,1,3,7,3,2,-8,2,-7,-8,4,3,-4,-7,-1,-8,-5,6,-6,-4,1,-8,8,-5,-4,5,-7,-7,1,-7,-3,3,-1,-7,-2,-7,-7,-9,6,8,-9,9,5,-6,-9,1,7,7,-10,6,-5,4,7,-7,-9,2,-9,-1,-6,-1,9,5,5,-3,-8,7,-1,5,6,8,8,1,-10,2,-1,-9,6,-6,7,5,10,9,5,-7,8,6,7,5,-2,-3,1,-3,9,-9,-1,-2,-10,-2,8,8,9,2,-1,-5,-6,-6,-2,6,-8,-8,3,2,2,10,5,6,2,-2,-6,8,5,1,-10,-9,-3,-9,-6,10,5,9,-6,6,4,-2,4,4,-3,7,1,-4,-4,1,-4,-9,8,10,3,-3,5,9,7,-1,8,4,5,-4,-8,8,-5,-10,-4,-9,8,8,-9,-5,2,-7,-3,10,6,4,10,-8,8,9,8,-1,-10,-2,-5,5,2,-8,2,2,5,-4,7,-9,7,6,-6,4,5,-4,2,8,3,8,5,3,-5,4,-8,6,10,3,-9,1,4,4,7,1,-7,5,-10,-1,-5,6,7,9,3,5,-2,8,2,-1,4,-8,4,5,2,-8,1,10,-7,7,-4,4,1,-1,3,-3,-5,-8,-6,2,8,-5,-5,9,8,4,10,-8,-9,3,3,9,-7,-9,-9,-1,3,8,-4,2,2,-6,5,3,-4,-7,2,-7,2,-4,-6,-10,4,7,-4,2,6,-8,3,-4,-8,6,-9,-9,-10,6,7,-5,3,-8,2,4,-7,6,4,9,-4,-1,9,-6,10,-2,-7,7,10,8,5,-7,-4,2,-6,-1,-5,3,-10,-2,-10,-9,-1,8,2,-3,-8,9,7,4,-4,6,-5,5,10,8,-2,-7,-3,-6,1,-4,-2,-4,6,-2,3,2,-9,-5,-6,8,-10,-1,-10,-2,8,3,-8,-9,-5,9,-1,5,-9,8,3,-3,1,-10,1,-3,7,-9,2,-1,10,-6,2,10,2,-7,4,-2,4,-7,3,3,5,-4,9,6,7,2,-3,-1,2,4,9,-2,-7,9,-8,-7,-6,2,8,7,-9,-5,1,1,-5,1,2,-1,2,-8,-4,-5,-6,6,-4,9,9,-10,-9,6,-8,2,-2,-7,-2,-5,10,5,-9,-1,-3,8,4,4,1,-1,-9,-6,-5,5,10,2,-2,-9,9,3,2,-5,1,2,-9,10,-6,-1,3,-6,6,2,-8,-10,-1,-8], dtype = "uint64")#candidate|3423|(2816,)|const|uint64
call_3421 = relay.TupleGetItem(func_2528_call(relay.reshape(var_3422.astype('int16'), [154,]), relay.reshape(const_3423.astype('uint64'), [1, 2816]), ), 4)
call_3424 = relay.TupleGetItem(func_2532_call(relay.reshape(var_3422.astype('int16'), [154,]), relay.reshape(const_3423.astype('uint64'), [1, 2816]), ), 4)
output = relay.Tuple([call_3419,call_3421,var_3422,const_3423,])
output2 = relay.Tuple([call_3420,call_3424,var_3422,const_3423,])
func_3431 = relay.Function([var_3422,], output)
mod['func_3431'] = func_3431
mod = relay.transform.InferType()(mod)
mutated_mod['func_3431'] = func_3431
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3432 = relay.var("var_3432", dtype = "int16", shape = (154,))#candidate|3432|(154,)|var|int16
func_3431_call = mutated_mod.get_global_var('func_3431')
call_3433 = func_3431_call(var_3432)
output = call_3433
func_3434 = relay.Function([var_3432], output)
mutated_mod['func_3434'] = func_3434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_479_call = mod.get_global_var('func_479')
func_481_call = mutated_mod.get_global_var('func_481')
call_3444 = relay.TupleGetItem(func_479_call(), 0)
call_3445 = relay.TupleGetItem(func_481_call(), 0)
func_543_call = mod.get_global_var('func_543')
func_545_call = mutated_mod.get_global_var('func_545')
call_3453 = func_543_call()
call_3454 = func_543_call()
output = relay.Tuple([call_3444,call_3453,])
output2 = relay.Tuple([call_3445,call_3454,])
func_3457 = relay.Function([], output)
mod['func_3457'] = func_3457
mod = relay.transform.InferType()(mod)
output = func_3457()
func_3458 = relay.Function([], output)
mutated_mod['func_3458'] = func_3458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_895_call = mod.get_global_var('func_895')
func_896_call = mutated_mod.get_global_var('func_896')
call_3479 = relay.TupleGetItem(func_895_call(), 2)
call_3480 = relay.TupleGetItem(func_896_call(), 2)
output = relay.Tuple([call_3479,])
output2 = relay.Tuple([call_3480,])
func_3486 = relay.Function([], output)
mod['func_3486'] = func_3486
mod = relay.transform.InferType()(mod)
output = func_3486()
func_3487 = relay.Function([], output)
mutated_mod['func_3487'] = func_3487
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3563 = relay.var("var_3563", dtype = "uint8", shape = (11, 13, 8))#candidate|3563|(11, 13, 8)|var|uint8
var_3564 = relay.var("var_3564", dtype = "uint8", shape = (11, 13, 8))#candidate|3564|(11, 13, 8)|var|uint8
bop_3565 = relay.add(var_3563.astype('uint8'), relay.reshape(var_3564.astype('uint8'), relay.shape_of(var_3563))) # shape=(11, 13, 8)
uop_3568 = relay.cos(bop_3565.astype('float32')) # shape=(11, 13, 8)
func_479_call = mod.get_global_var('func_479')
func_481_call = mutated_mod.get_global_var('func_481')
call_3574 = relay.TupleGetItem(func_479_call(), 0)
call_3575 = relay.TupleGetItem(func_481_call(), 0)
func_937_call = mod.get_global_var('func_937')
func_939_call = mutated_mod.get_global_var('func_939')
call_3577 = relay.TupleGetItem(func_937_call(), 0)
call_3578 = relay.TupleGetItem(func_939_call(), 0)
func_3335_call = mod.get_global_var('func_3335')
func_3338_call = mutated_mod.get_global_var('func_3338')
var_3585 = relay.var("var_3585", dtype = "bool", shape = (42, 6))#candidate|3585|(42, 6)|var|bool
call_3584 = relay.TupleGetItem(func_3335_call(relay.reshape(var_3585.astype('bool'), [6, 3, 14])), 0)
call_3586 = relay.TupleGetItem(func_3338_call(relay.reshape(var_3585.astype('bool'), [6, 3, 14])), 0)
output = relay.Tuple([uop_3568,call_3574,call_3577,call_3584,var_3585,])
output2 = relay.Tuple([uop_3568,call_3575,call_3578,call_3586,var_3585,])
func_3587 = relay.Function([var_3563,var_3564,var_3585,], output)
mod['func_3587'] = func_3587
mod = relay.transform.InferType()(mod)
var_3588 = relay.var("var_3588", dtype = "uint8", shape = (11, 13, 8))#candidate|3588|(11, 13, 8)|var|uint8
var_3589 = relay.var("var_3589", dtype = "uint8", shape = (11, 13, 8))#candidate|3589|(11, 13, 8)|var|uint8
var_3590 = relay.var("var_3590", dtype = "bool", shape = (42, 6))#candidate|3590|(42, 6)|var|bool
output = func_3587(var_3588,var_3589,var_3590,)
func_3591 = relay.Function([var_3588,var_3589,var_3590,], output)
mutated_mod['func_3591'] = func_3591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_813_call = mod.get_global_var('func_813')
func_814_call = mutated_mod.get_global_var('func_814')
call_3602 = relay.TupleGetItem(func_813_call(), 0)
call_3603 = relay.TupleGetItem(func_814_call(), 0)
output = call_3602
output2 = call_3603
func_3617 = relay.Function([], output)
mod['func_3617'] = func_3617
mod = relay.transform.InferType()(mod)
output = func_3617()
func_3618 = relay.Function([], output)
mutated_mod['func_3618'] = func_3618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2342_call = mod.get_global_var('func_2342')
func_2343_call = mutated_mod.get_global_var('func_2343')
call_3625 = relay.TupleGetItem(func_2342_call(), 0)
call_3626 = relay.TupleGetItem(func_2343_call(), 0)
output = call_3625
output2 = call_3626
func_3657 = relay.Function([], output)
mod['func_3657'] = func_3657
mod = relay.transform.InferType()(mod)
output = func_3657()
func_3658 = relay.Function([], output)
mutated_mod['func_3658'] = func_3658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2000_call = mod.get_global_var('func_2000')
func_2002_call = mutated_mod.get_global_var('func_2002')
call_3706 = func_2000_call()
call_3707 = func_2000_call()
output = call_3706
output2 = call_3707
func_3718 = relay.Function([], output)
mod['func_3718'] = func_3718
mod = relay.transform.InferType()(mod)
output = func_3718()
func_3719 = relay.Function([], output)
mutated_mod['func_3719'] = func_3719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1431_call = mod.get_global_var('func_1431')
func_1433_call = mutated_mod.get_global_var('func_1433')
call_3750 = func_1431_call()
call_3751 = func_1431_call()
const_3779 = relay.const([[[-1.729963,5.797868,5.040815,2.920536,-8.127262,-2.605982,4.469896,0.121542],[-6.861136,-7.973040,-5.965356,6.605223,8.805707,3.676639,-8.351948,-9.545018]],[[8.029753,6.926788,5.712894,4.211393,-2.910876,2.071853,-5.075833,-1.307350],[2.926362,-6.083662,-1.995771,-3.163196,-5.948851,-1.832839,-8.172075,2.135227]],[[-3.297594,-1.577751,-1.137825,6.369339,8.125493,-0.824263,-3.024833,-9.161512],[5.509853,5.062691,-2.006088,5.357037,4.515042,-6.381891,3.494154,7.974334]],[[-3.081668,6.849263,-0.580858,-7.839143,-8.786115,1.884282,5.071402,-1.492480],[-5.640087,-0.286156,5.701051,-6.252999,1.771734,-0.624445,-1.462026,-4.442538]],[[-4.751111,3.800674,3.900587,-8.062022,-3.805003,-6.851543,-1.639558,5.777510],[-7.533634,2.334424,2.755866,-7.540868,-7.016594,6.952159,-5.669608,-7.000859]],[[-3.411027,3.744932,5.220819,7.168401,-7.311325,7.665406,-2.260824,6.467571],[-5.596997,-6.115681,-9.609362,-2.279255,7.835675,-1.088278,7.584350,-1.178688]],[[-3.119148,5.550993,-7.273337,-5.398680,-3.853081,2.995781,-3.899535,5.863344],[1.139518,-8.332786,-2.981031,0.173107,7.030073,-5.155407,-4.834652,-0.623302]],[[-0.348102,-6.182659,-9.496104,8.283353,-0.610617,0.205612,-1.346757,8.701521],[-4.399452,3.646679,-0.608874,-5.129076,-5.153915,-5.009683,-0.165131,-3.272235]],[[8.138135,1.728641,9.310243,-5.401477,2.338217,-0.430077,7.734681,5.758353],[4.452298,-7.283486,6.701591,3.122224,4.448988,-2.042897,-3.504720,9.339749]],[[3.423188,7.606199,7.770050,-5.224636,6.905292,-2.529048,-3.357746,-5.253929],[3.300470,7.867843,-2.103184,-1.075254,6.930795,8.625396,7.315714,2.532938]],[[7.504775,1.897442,-1.615880,7.787539,-6.280687,-4.532667,5.461192,1.199395],[-6.718099,-8.708999,6.567385,-7.036911,6.728974,4.886133,-1.017711,-6.676706]],[[3.345036,2.193409,1.601991,-5.859647,-9.062002,5.136257,5.274363,-0.113635],[6.051918,-4.142741,-7.744012,6.717818,-6.707505,-0.244830,4.507693,-6.295516]],[[5.289848,1.693718,-7.963426,-6.970694,-4.287956,8.003533,-3.895916,3.267049],[-9.264075,4.464428,2.404458,-9.874926,7.316009,-1.401445,8.236162,1.056770]],[[-1.470221,-7.875117,-7.709320,-0.722847,-8.628511,3.507578,0.624202,-7.711162],[-7.036391,-0.479036,0.500606,-7.075400,-5.025755,3.572080,8.413432,-3.763457]]], dtype = "float64")#candidate|3779|(14, 2, 8)|const|float64
bop_3780 = relay.equal(call_3750.astype('bool'), relay.reshape(const_3779.astype('bool'), relay.shape_of(call_3750))) # shape=(14, 2, 8)
bop_3783 = relay.equal(call_3751.astype('bool'), relay.reshape(const_3779.astype('bool'), relay.shape_of(call_3751))) # shape=(14, 2, 8)
bop_3785 = relay.divide(call_3750.astype('float64'), relay.reshape(bop_3780.astype('float64'), relay.shape_of(call_3750))) # shape=(14, 2, 8)
bop_3788 = relay.divide(call_3751.astype('float64'), relay.reshape(bop_3783.astype('float64'), relay.shape_of(call_3751))) # shape=(14, 2, 8)
output = relay.Tuple([bop_3785,])
output2 = relay.Tuple([bop_3788,])
func_3791 = relay.Function([], output)
mod['func_3791'] = func_3791
mod = relay.transform.InferType()(mod)
mutated_mod['func_3791'] = func_3791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3791_call = mutated_mod.get_global_var('func_3791')
call_3792 = func_3791_call()
output = call_3792
func_3793 = relay.Function([], output)
mutated_mod['func_3793'] = func_3793
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3835 = relay.var("var_3835", dtype = "uint32", shape = ())#candidate|3835|()|var|uint32
const_3836 = relay.const([[[4,-4,8,-9,6,9,8],[1,7,-7,-3,-10,8,-3],[-4,-6,6,-7,9,-7,3],[1,3,5,4,-4,6,9],[-2,8,5,-8,-3,-7,2],[7,9,9,2,3,-5,-2],[-3,-6,-5,2,-6,3,5],[4,-4,-3,1,-5,5,10],[5,2,4,4,10,-1,8],[10,2,3,4,-8,-9,7]],[[-1,3,-8,-7,-2,-2,-8],[-3,-7,-4,-4,6,2,-3],[7,4,-9,-5,3,-9,-2],[9,6,-8,4,3,-8,8],[-10,-2,10,-6,-4,-6,-4],[2,-8,8,5,-8,-10,9],[-7,-10,7,-6,10,8,5],[-1,-10,5,-5,3,-10,9],[9,8,2,-5,-1,-5,-2],[-7,8,-4,-2,-6,3,-5]],[[10,3,-1,-7,10,-3,10],[-6,-3,-7,-10,7,1,6],[-5,-7,6,-6,10,1,3],[4,4,-6,-2,5,-8,-3],[8,-3,4,-9,9,-1,-7],[10,8,5,-6,6,8,2],[-8,4,-6,-10,-6,-3,4],[-3,-6,-3,9,-6,-3,-2],[8,6,9,-1,-7,-7,9],[10,-6,6,-8,-8,-1,1]],[[-7,-2,7,10,-7,2,3],[1,-1,-7,1,-1,-4,-5],[3,6,1,4,7,-7,-4],[-10,-10,9,9,-10,-1,1],[-10,-8,-4,-3,-4,4,-3],[-6,10,4,-7,1,10,8],[2,7,-8,3,9,9,-4],[-5,-6,4,6,-5,-4,9],[-8,5,8,10,-7,8,-2],[1,1,-3,-6,-2,8,5]],[[6,5,-3,-3,-4,-7,-7],[-9,3,5,6,3,-6,4],[4,5,3,3,-4,-5,9],[-1,8,-5,2,6,-9,-9],[4,2,-1,8,-9,-10,-5],[-3,-8,1,6,6,10,-7],[-1,-8,10,-2,7,6,9],[10,2,8,-8,3,-7,-6],[-1,7,-9,-6,3,3,6],[-7,-7,10,-10,7,-7,4]],[[1,2,2,3,-4,-2,7],[-8,-5,9,-10,1,-7,-10],[3,10,-3,-6,-4,6,-10],[-5,-4,-9,8,2,8,7],[-6,-10,10,-10,4,10,9],[-8,-6,5,7,-2,-3,-10],[10,6,6,-4,8,1,-2],[-2,9,-9,2,-7,-9,4],[3,-4,-3,10,6,8,-8],[6,2,-10,-7,-5,6,-9]],[[-1,8,7,9,-2,-1,-1],[-2,10,8,5,4,-8,2],[1,10,4,-5,1,3,3],[4,5,-10,6,-10,7,-5],[-10,-10,10,-4,7,7,3],[1,-4,-9,-3,-7,-8,-9],[10,1,-3,-3,-8,-7,-6],[3,4,7,-9,8,-9,10],[-3,-4,5,3,4,-10,4],[-9,2,2,-4,-4,7,-6]],[[9,6,6,-3,3,8,-3],[-2,-8,7,-1,-5,-10,-1],[-1,5,-4,1,1,3,-3],[3,-1,-3,6,-8,1,-5],[2,-7,-4,6,3,9,3],[-8,-5,2,-8,7,-5,2],[-10,-6,-2,9,7,-5,3],[6,8,-2,-7,-2,-9,8],[6,1,-6,2,10,-5,7],[9,5,-7,9,7,2,-8]],[[8,7,7,-2,3,-2,-7],[3,-8,5,-8,-6,10,1],[-1,-4,-9,5,-7,7,-2],[6,-8,5,-9,-7,1,-4],[-5,6,7,6,-1,10,-9],[9,-7,-1,3,-1,6,-9],[-1,1,-9,-5,7,10,2],[7,10,5,4,-2,-3,9],[-1,8,3,-10,-6,-9,-6],[-2,-3,-2,-8,10,-4,-7]],[[5,6,-8,8,4,6,-2],[-5,-5,7,-8,1,-5,-8],[-3,-3,2,-6,6,2,1],[1,2,-10,-3,-9,5,6],[2,8,-10,-6,2,5,-4],[-9,-6,8,6,-6,-6,-1],[4,-10,3,2,9,-10,-9],[-9,3,-10,8,-6,10,5],[-7,-5,-6,-9,-1,4,8],[10,-10,-2,7,-1,-2,1]],[[-1,5,5,-10,5,9,10],[-7,-9,8,6,-2,10,9],[-2,-3,1,10,-8,-6,-2],[2,-10,2,5,-9,-8,3],[-4,-1,5,9,1,-1,-2],[5,-1,7,5,-3,9,-1],[-10,-8,-9,3,4,9,9],[-8,8,-6,10,2,-3,6],[-6,-1,-1,3,10,3,5],[-1,5,-7,3,-4,9,8]],[[1,-3,3,3,5,-4,-1],[-8,3,3,9,1,-5,4],[-10,-5,-8,-8,-4,-5,-7],[5,7,4,-5,10,-9,7],[-5,-10,-7,8,3,6,-6],[-8,1,-3,-7,2,6,-7],[2,-8,6,2,3,9,-5],[-5,8,-4,-9,1,5,-9],[5,5,1,-4,1,10,-7],[2,-4,3,-4,-4,5,8]],[[-1,9,4,-3,9,-2,5],[-6,1,-4,-7,-10,3,4],[1,8,-1,-10,-2,2,2],[2,7,10,6,-4,1,5],[-8,-4,3,3,-8,10,7],[1,-7,-7,-1,-2,-4,-1],[10,1,-5,7,4,1,-4],[-5,-5,10,-1,8,-5,10],[-9,-4,-7,7,7,-9,5],[-6,2,-9,8,-1,-6,1]],[[-1,3,-2,-9,2,-2,-9],[2,2,4,-9,-3,4,-8],[-4,4,-9,-5,3,-1,-7],[6,5,-3,-7,-3,2,5],[-1,-6,1,-10,6,3,-7],[-4,7,-4,9,-9,4,5],[9,10,3,5,-6,6,10],[1,4,-6,7,-5,-5,5],[6,5,-1,5,1,-10,7],[-8,5,-6,7,2,-10,-2]],[[-1,4,8,5,4,-3,-2],[-3,9,3,3,5,-1,-5],[5,-6,6,-4,-9,2,-10],[2,8,-8,9,10,-3,3],[3,-5,-5,5,-2,6,9],[-7,-2,1,-6,-6,-2,-8],[-3,-1,9,5,8,7,-10],[-3,2,-7,1,-6,-9,-2],[1,8,-1,10,-6,5,-4],[5,-5,2,2,-4,9,2]],[[4,-9,-3,9,-5,-3,-4],[6,-1,4,3,5,-7,-10],[1,-2,-7,-10,-7,4,7],[-4,6,-1,-3,4,2,3],[8,-6,7,-6,9,5,-4],[-8,10,4,-4,-4,-1,-4],[8,2,3,7,-6,-4,-10],[2,2,6,4,10,6,-4],[10,8,7,6,-10,10,7],[-2,7,-4,4,10,2,5]]], dtype = "uint32")#candidate|3836|(16, 10, 7)|const|uint32
bop_3837 = relay.logical_xor(var_3835.astype('uint32'), const_3836.astype('uint32')) # shape=(16, 10, 7)
func_3486_call = mod.get_global_var('func_3486')
func_3487_call = mutated_mod.get_global_var('func_3487')
call_3840 = relay.TupleGetItem(func_3486_call(), 0)
call_3841 = relay.TupleGetItem(func_3487_call(), 0)
func_201_call = mod.get_global_var('func_201')
func_203_call = mutated_mod.get_global_var('func_203')
call_3862 = relay.TupleGetItem(func_201_call(relay.reshape(call_3840.astype('float64'), [14, 2, 8])), 1)
call_3863 = relay.TupleGetItem(func_203_call(relay.reshape(call_3840.astype('float64'), [14, 2, 8])), 1)
func_2205_call = mod.get_global_var('func_2205')
func_2206_call = mutated_mod.get_global_var('func_2206')
call_3864 = func_2205_call()
call_3865 = func_2205_call()
output = relay.Tuple([bop_3837,call_3840,call_3862,call_3864,])
output2 = relay.Tuple([bop_3837,call_3841,call_3863,call_3865,])
func_3872 = relay.Function([var_3835,], output)
mod['func_3872'] = func_3872
mod = relay.transform.InferType()(mod)
mutated_mod['func_3872'] = func_3872
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3873 = relay.var("var_3873", dtype = "uint32", shape = ())#candidate|3873|()|var|uint32
func_3872_call = mutated_mod.get_global_var('func_3872')
call_3874 = func_3872_call(var_3873)
output = call_3874
func_3875 = relay.Function([var_3873], output)
mutated_mod['func_3875'] = func_3875
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2741_call = mod.get_global_var('func_2741')
func_2742_call = mutated_mod.get_global_var('func_2742')
call_3935 = relay.TupleGetItem(func_2741_call(), 0)
call_3936 = relay.TupleGetItem(func_2742_call(), 0)
output = relay.Tuple([call_3935,])
output2 = relay.Tuple([call_3936,])
func_3952 = relay.Function([], output)
mod['func_3952'] = func_3952
mod = relay.transform.InferType()(mod)
output = func_3952()
func_3953 = relay.Function([], output)
mutated_mod['func_3953'] = func_3953
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3966 = relay.var("var_3966", dtype = "float64", shape = (8, 10, 15))#candidate|3966|(8, 10, 15)|var|float64
uop_3967 = relay.atanh(var_3966.astype('float64')) # shape=(8, 10, 15)
bop_3978 = relay.greater_equal(uop_3967.astype('bool'), relay.reshape(var_3966.astype('bool'), relay.shape_of(uop_3967))) # shape=(8, 10, 15)
output = bop_3978
output2 = bop_3978
func_3993 = relay.Function([var_3966,], output)
mod['func_3993'] = func_3993
mod = relay.transform.InferType()(mod)
var_3994 = relay.var("var_3994", dtype = "float64", shape = (8, 10, 15))#candidate|3994|(8, 10, 15)|var|float64
output = func_3993(var_3994)
func_3995 = relay.Function([var_3994], output)
mutated_mod['func_3995'] = func_3995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3486_call = mod.get_global_var('func_3486')
func_3487_call = mutated_mod.get_global_var('func_3487')
call_4038 = relay.TupleGetItem(func_3486_call(), 0)
call_4039 = relay.TupleGetItem(func_3487_call(), 0)
var_4052 = relay.var("var_4052", dtype = "float64", shape = (224,))#candidate|4052|(224,)|var|float64
bop_4053 = relay.bitwise_and(call_4038.astype('int64'), relay.reshape(var_4052.astype('int64'), relay.shape_of(call_4038))) # shape=(224,)
bop_4056 = relay.bitwise_and(call_4039.astype('int64'), relay.reshape(var_4052.astype('int64'), relay.shape_of(call_4039))) # shape=(224,)
func_1816_call = mod.get_global_var('func_1816')
func_1817_call = mutated_mod.get_global_var('func_1817')
call_4066 = relay.TupleGetItem(func_1816_call(), 1)
call_4067 = relay.TupleGetItem(func_1817_call(), 1)
func_3486_call = mod.get_global_var('func_3486')
func_3487_call = mutated_mod.get_global_var('func_3487')
call_4070 = relay.TupleGetItem(func_3486_call(), 0)
call_4071 = relay.TupleGetItem(func_3487_call(), 0)
func_329_call = mod.get_global_var('func_329')
func_331_call = mutated_mod.get_global_var('func_331')
var_4077 = relay.var("var_4077", dtype = "uint64", shape = (2816,))#candidate|4077|(2816,)|var|uint64
call_4076 = relay.TupleGetItem(func_329_call(relay.reshape(var_4077.astype('uint64'), [1408, 2])), 0)
call_4078 = relay.TupleGetItem(func_331_call(relay.reshape(var_4077.astype('uint64'), [1408, 2])), 0)
func_590_call = mod.get_global_var('func_590')
func_591_call = mutated_mod.get_global_var('func_591')
call_4079 = func_590_call()
call_4080 = func_590_call()
output = relay.Tuple([bop_4053,call_4066,call_4070,call_4076,var_4077,call_4079,])
output2 = relay.Tuple([bop_4056,call_4067,call_4071,call_4078,var_4077,call_4080,])
func_4081 = relay.Function([var_4052,var_4077,], output)
mod['func_4081'] = func_4081
mod = relay.transform.InferType()(mod)
var_4082 = relay.var("var_4082", dtype = "float64", shape = (224,))#candidate|4082|(224,)|var|float64
var_4083 = relay.var("var_4083", dtype = "uint64", shape = (2816,))#candidate|4083|(2816,)|var|uint64
output = func_4081(var_4082,var_4083,)
func_4084 = relay.Function([var_4082,var_4083,], output)
mutated_mod['func_4084'] = func_4084
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4165 = relay.var("var_4165", dtype = "float32", shape = (4, 15, 4))#candidate|4165|(4, 15, 4)|var|float32
var_4166 = relay.var("var_4166", dtype = "float32", shape = (4, 15, 4))#candidate|4166|(4, 15, 4)|var|float32
bop_4167 = relay.floor_divide(var_4165.astype('float32'), relay.reshape(var_4166.astype('float32'), relay.shape_of(var_4165))) # shape=(4, 15, 4)
func_2592_call = mod.get_global_var('func_2592')
func_2593_call = mutated_mod.get_global_var('func_2593')
call_4180 = relay.TupleGetItem(func_2592_call(), 0)
call_4181 = relay.TupleGetItem(func_2593_call(), 0)
func_3065_call = mod.get_global_var('func_3065')
func_3067_call = mutated_mod.get_global_var('func_3067')
call_4183 = relay.TupleGetItem(func_3065_call(), 0)
call_4184 = relay.TupleGetItem(func_3067_call(), 0)
output = relay.Tuple([bop_4167,call_4180,call_4183,])
output2 = relay.Tuple([bop_4167,call_4181,call_4184,])
func_4187 = relay.Function([var_4165,var_4166,], output)
mod['func_4187'] = func_4187
mod = relay.transform.InferType()(mod)
var_4188 = relay.var("var_4188", dtype = "float32", shape = (4, 15, 4))#candidate|4188|(4, 15, 4)|var|float32
var_4189 = relay.var("var_4189", dtype = "float32", shape = (4, 15, 4))#candidate|4189|(4, 15, 4)|var|float32
output = func_4187(var_4188,var_4189,)
func_4190 = relay.Function([var_4188,var_4189,], output)
mutated_mod['func_4190'] = func_4190
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4199 = relay.const(5.726922, dtype = "float32")#candidate|4199|()|const|float32
var_4200 = relay.var("var_4200", dtype = "float32", shape = (14, 5, 11))#candidate|4200|(14, 5, 11)|var|float32
bop_4201 = relay.floor_divide(const_4199.astype('float32'), var_4200.astype('float32')) # shape=(14, 5, 11)
var_4207 = relay.var("var_4207", dtype = "float32", shape = (4, 9, 13))#candidate|4207|(4, 9, 13)|var|float32
bop_4208 = relay.greater_equal(const_4199.astype('bool'), var_4207.astype('bool')) # shape=(4, 9, 13)
bop_4214 = relay.logical_and(bop_4208.astype('bool'), relay.reshape(var_4207.astype('bool'), relay.shape_of(bop_4208))) # shape=(4, 9, 13)
output = relay.Tuple([bop_4201,bop_4214,])
output2 = relay.Tuple([bop_4201,bop_4214,])
func_4218 = relay.Function([var_4200,var_4207,], output)
mod['func_4218'] = func_4218
mod = relay.transform.InferType()(mod)
mutated_mod['func_4218'] = func_4218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4218_call = mutated_mod.get_global_var('func_4218')
var_4220 = relay.var("var_4220", dtype = "float32", shape = (14, 5, 11))#candidate|4220|(14, 5, 11)|var|float32
var_4221 = relay.var("var_4221", dtype = "float32", shape = (4, 9, 13))#candidate|4221|(4, 9, 13)|var|float32
call_4219 = func_4218_call(var_4220,var_4221,)
output = call_4219
func_4222 = relay.Function([var_4220,var_4221,], output)
mutated_mod['func_4222'] = func_4222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1431_call = mod.get_global_var('func_1431')
func_1433_call = mutated_mod.get_global_var('func_1433')
call_4296 = func_1431_call()
call_4297 = func_1431_call()
output = call_4296
output2 = call_4297
func_4300 = relay.Function([], output)
mod['func_4300'] = func_4300
mod = relay.transform.InferType()(mod)
output = func_4300()
func_4301 = relay.Function([], output)
mutated_mod['func_4301'] = func_4301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1385_call = mod.get_global_var('func_1385')
func_1387_call = mutated_mod.get_global_var('func_1387')
call_4388 = relay.TupleGetItem(func_1385_call(), 1)
call_4389 = relay.TupleGetItem(func_1387_call(), 1)
output = call_4388
output2 = call_4389
func_4395 = relay.Function([], output)
mod['func_4395'] = func_4395
mod = relay.transform.InferType()(mod)
output = func_4395()
func_4396 = relay.Function([], output)
mutated_mod['func_4396'] = func_4396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2241_call = mod.get_global_var('func_2241')
func_2242_call = mutated_mod.get_global_var('func_2242')
call_4443 = func_2241_call()
call_4444 = func_2241_call()
func_201_call = mod.get_global_var('func_201')
func_203_call = mutated_mod.get_global_var('func_203')
call_4459 = relay.TupleGetItem(func_201_call(relay.reshape(call_4443.astype('float64'), [14, 2, 8])), 1)
call_4460 = relay.TupleGetItem(func_203_call(relay.reshape(call_4443.astype('float64'), [14, 2, 8])), 1)
func_3457_call = mod.get_global_var('func_3457')
func_3458_call = mutated_mod.get_global_var('func_3458')
call_4467 = relay.TupleGetItem(func_3457_call(), 0)
call_4468 = relay.TupleGetItem(func_3458_call(), 0)
func_2314_call = mod.get_global_var('func_2314')
func_2316_call = mutated_mod.get_global_var('func_2316')
call_4508 = func_2314_call()
call_4509 = func_2314_call()
output = relay.Tuple([call_4443,call_4459,call_4467,call_4508,])
output2 = relay.Tuple([call_4444,call_4460,call_4468,call_4509,])
func_4527 = relay.Function([], output)
mod['func_4527'] = func_4527
mod = relay.transform.InferType()(mod)
output = func_4527()
func_4528 = relay.Function([], output)
mutated_mod['func_4528'] = func_4528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1196_call = mod.get_global_var('func_1196')
func_1197_call = mutated_mod.get_global_var('func_1197')
call_4537 = relay.TupleGetItem(func_1196_call(), 3)
call_4538 = relay.TupleGetItem(func_1197_call(), 3)
output = relay.Tuple([call_4537,])
output2 = relay.Tuple([call_4538,])
func_4541 = relay.Function([], output)
mod['func_4541'] = func_4541
mod = relay.transform.InferType()(mod)
mutated_mod['func_4541'] = func_4541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4541_call = mutated_mod.get_global_var('func_4541')
call_4542 = func_4541_call()
output = call_4542
func_4543 = relay.Function([], output)
mutated_mod['func_4543'] = func_4543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mod.get_global_var('func_918')
func_919_call = mutated_mod.get_global_var('func_919')
call_4547 = func_918_call()
call_4548 = func_918_call()
uop_4554 = relay.asin(call_4547.astype('float64')) # shape=(14, 2, 8)
uop_4556 = relay.asin(call_4548.astype('float64')) # shape=(14, 2, 8)
uop_4562 = relay.sin(uop_4554.astype('float64')) # shape=(14, 2, 8)
uop_4564 = relay.sin(uop_4556.astype('float64')) # shape=(14, 2, 8)
func_4187_call = mod.get_global_var('func_4187')
func_4190_call = mutated_mod.get_global_var('func_4190')
const_4567 = relay.const([[7.797382,4.527714,9.091986,6.380991,-6.427594,5.671278,-6.450756,-0.822958,7.794708,4.391411,-5.446655,-3.743375,4.049956,-2.070424,3.073975,-5.828433,7.195182,-4.821509,-9.132545,-6.266817,-1.614508,1.409066,-5.382447,-8.384430,-2.941532,-8.685267,-2.133618,-3.166494,5.733005,-4.156253,9.910953,5.010362,-4.798848,8.784121,1.435156,-1.417914,3.017532,-2.196495,2.351294,0.305550,3.765519,0.261470,-8.566956,9.132165,-8.264989,7.665511,-3.658574,-4.506282,-5.210510,7.107253,-8.688128,7.619211,-6.144837,7.029115,1.818887,0.339592,-7.999978,-4.855528,-9.808764,-6.545764],[9.895785,-1.474407,0.849540,3.785469,-3.678056,2.355094,-7.795848,2.276903,1.020549,-1.137940,7.148930,9.740032,-3.069653,0.783843,6.898141,1.679985,9.976383,9.688182,3.228724,-5.360873,2.677011,-2.977437,-4.608260,-4.958297,-0.123177,-0.413419,-7.470190,1.555118,-0.150746,-6.896072,9.491723,-0.395081,1.587313,5.851284,-8.579225,2.641106,5.326559,1.948487,4.101541,5.057464,2.188465,0.344762,3.369630,-6.380881,0.733204,-4.865638,0.384171,1.637610,-5.740013,4.096133,-0.209130,-4.067576,-9.620550,-0.923566,-0.440857,9.744139,1.987520,9.144407,9.538241,-0.784937],[-4.466191,1.191045,-2.432057,8.839882,5.454770,2.786759,7.722432,-1.185015,-0.953750,0.316879,-9.221804,-4.354832,3.398154,1.130277,0.887245,-7.943200,-5.937898,0.643744,-7.803312,6.960924,7.494191,-5.414523,-6.532743,-1.520631,6.259710,0.947883,-0.144342,6.449916,-8.033856,5.797010,4.288833,0.116241,3.110840,-9.952172,1.724206,-5.507592,-9.765276,5.057058,8.250684,2.729088,3.099021,-9.567956,-1.337532,-5.443333,-7.837529,6.704816,3.729296,8.041585,7.131927,-1.025117,5.338531,-0.032308,3.533106,6.668282,2.117709,2.850024,6.054553,3.866219,-4.603524,-7.190210],[9.503127,-1.777991,8.174155,4.377899,8.777404,7.706921,-5.830156,-9.465966,-3.886761,-0.738564,2.864401,-9.773853,-2.739421,-3.426985,2.991718,6.404776,-2.512611,2.630726,-6.652105,0.739419,7.818334,-3.275375,-1.996850,6.827980,-5.049903,-1.893229,-5.950304,2.356258,-3.768369,0.802239,-6.488478,-5.680975,-1.851457,-1.224499,2.865834,-4.166252,3.075806,-4.136790,6.186175,-1.967728,-0.131677,7.206055,4.033708,4.149799,2.764540,-3.278810,3.881100,-1.644199,-4.143898,-0.687662,-9.850763,-7.626340,-0.666394,8.842461,0.295493,4.961630,4.442769,-3.605808,0.922624,-0.334879]], dtype = "float32")#candidate|4567|(4, 60)|const|float32
call_4566 = relay.TupleGetItem(func_4187_call(relay.reshape(const_4567.astype('float32'), [4, 15, 4]), relay.reshape(const_4567.astype('float32'), [4, 15, 4]), ), 2)
call_4568 = relay.TupleGetItem(func_4190_call(relay.reshape(const_4567.astype('float32'), [4, 15, 4]), relay.reshape(const_4567.astype('float32'), [4, 15, 4]), ), 2)
func_2205_call = mod.get_global_var('func_2205')
func_2206_call = mutated_mod.get_global_var('func_2206')
call_4573 = func_2205_call()
call_4574 = func_2205_call()
func_264_call = mod.get_global_var('func_264')
func_266_call = mutated_mod.get_global_var('func_266')
call_4588 = relay.TupleGetItem(func_264_call(relay.reshape(uop_4554.astype('float64'), [14, 2, 8])), 0)
call_4589 = relay.TupleGetItem(func_266_call(relay.reshape(uop_4554.astype('float64'), [14, 2, 8])), 0)
func_1112_call = mod.get_global_var('func_1112')
func_1115_call = mutated_mod.get_global_var('func_1115')
var_4591 = relay.var("var_4591", dtype = "int16", shape = (154,))#candidate|4591|(154,)|var|int16
var_4592 = relay.var("var_4592", dtype = "uint64", shape = (2816,))#candidate|4592|(2816,)|var|uint64
call_4590 = relay.TupleGetItem(func_1112_call(relay.reshape(var_4591.astype('int16'), [154,]), relay.reshape(var_4592.astype('uint64'), [2816,]), ), 4)
call_4593 = relay.TupleGetItem(func_1115_call(relay.reshape(var_4591.astype('int16'), [154,]), relay.reshape(var_4592.astype('uint64'), [2816,]), ), 4)
func_3109_call = mod.get_global_var('func_3109')
func_3111_call = mutated_mod.get_global_var('func_3111')
call_4613 = relay.TupleGetItem(func_3109_call(relay.reshape(uop_4554.astype('float64'), [14, 2, 8])), 3)
call_4614 = relay.TupleGetItem(func_3111_call(relay.reshape(uop_4554.astype('float64'), [14, 2, 8])), 3)
output = relay.Tuple([uop_4562,call_4566,const_4567,call_4573,call_4588,call_4590,var_4591,var_4592,call_4613,])
output2 = relay.Tuple([uop_4564,call_4568,const_4567,call_4574,call_4589,call_4593,var_4591,var_4592,call_4614,])
func_4618 = relay.Function([var_4591,var_4592,], output)
mod['func_4618'] = func_4618
mod = relay.transform.InferType()(mod)
var_4619 = relay.var("var_4619", dtype = "int16", shape = (154,))#candidate|4619|(154,)|var|int16
var_4620 = relay.var("var_4620", dtype = "uint64", shape = (2816,))#candidate|4620|(2816,)|var|uint64
output = func_4618(var_4619,var_4620,)
func_4621 = relay.Function([var_4619,var_4620,], output)
mutated_mod['func_4621'] = func_4621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_657_call = mod.get_global_var('func_657')
func_658_call = mutated_mod.get_global_var('func_658')
call_4626 = func_657_call()
call_4627 = func_657_call()
output = relay.Tuple([call_4626,])
output2 = relay.Tuple([call_4627,])
func_4629 = relay.Function([], output)
mod['func_4629'] = func_4629
mod = relay.transform.InferType()(mod)
mutated_mod['func_4629'] = func_4629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4629_call = mutated_mod.get_global_var('func_4629')
call_4630 = func_4629_call()
output = call_4630
func_4631 = relay.Function([], output)
mutated_mod['func_4631'] = func_4631
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4639 = relay.var("var_4639", dtype = "float64", shape = (11, 1))#candidate|4639|(11, 1)|var|float64
uop_4640 = relay.sigmoid(var_4639.astype('float64')) # shape=(11, 1)
output = relay.Tuple([uop_4640,])
output2 = relay.Tuple([uop_4640,])
func_4650 = relay.Function([var_4639,], output)
mod['func_4650'] = func_4650
mod = relay.transform.InferType()(mod)
mutated_mod['func_4650'] = func_4650
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4651 = relay.var("var_4651", dtype = "float64", shape = (11, 1))#candidate|4651|(11, 1)|var|float64
func_4650_call = mutated_mod.get_global_var('func_4650')
call_4652 = func_4650_call(var_4651)
output = call_4652
func_4653 = relay.Function([var_4651], output)
mutated_mod['func_4653'] = func_4653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4395_call = mod.get_global_var('func_4395')
func_4396_call = mutated_mod.get_global_var('func_4396')
call_4717 = func_4395_call()
call_4718 = func_4395_call()
output = call_4717
output2 = call_4718
func_4724 = relay.Function([], output)
mod['func_4724'] = func_4724
mod = relay.transform.InferType()(mod)
output = func_4724()
func_4725 = relay.Function([], output)
mutated_mod['func_4725'] = func_4725
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4775 = relay.var("var_4775", dtype = "bool", shape = (7, 10, 4))#candidate|4775|(7, 10, 4)|var|bool
var_4776 = relay.var("var_4776", dtype = "bool", shape = (7, 10, 4))#candidate|4776|(7, 10, 4)|var|bool
bop_4777 = relay.logical_and(var_4775.astype('bool'), relay.reshape(var_4776.astype('bool'), relay.shape_of(var_4775))) # shape=(7, 10, 4)
func_895_call = mod.get_global_var('func_895')
func_896_call = mutated_mod.get_global_var('func_896')
call_4785 = relay.TupleGetItem(func_895_call(), 0)
call_4786 = relay.TupleGetItem(func_896_call(), 0)
const_4799 = relay.const([[[True,True,False,True],[False,False,True,True],[False,True,False,True],[False,True,True,True],[True,True,False,True],[True,True,True,False],[True,True,True,True],[False,False,False,True],[False,False,False,False],[False,False,True,True]],[[True,True,False,True],[True,True,True,False],[False,True,True,False],[True,False,False,False],[False,True,False,False],[False,False,True,False],[False,False,False,True],[False,False,False,True],[True,False,False,False],[True,True,False,True]],[[True,False,True,False],[False,True,False,False],[True,False,False,True],[False,False,True,True],[False,True,False,False],[True,False,True,True],[False,True,True,True],[True,False,False,False],[False,False,False,False],[True,False,True,False]],[[True,True,True,True],[True,False,False,True],[False,False,True,True],[False,False,False,False],[False,False,True,True],[False,False,True,False],[False,True,False,True],[True,True,False,False],[True,True,False,False],[False,False,False,False]],[[True,True,True,True],[False,False,False,False],[False,True,True,False],[True,False,False,True],[True,False,True,False],[False,True,True,True],[False,True,True,False],[True,True,False,False],[True,False,False,True],[False,False,True,False]],[[True,False,False,True],[False,False,False,True],[False,True,True,False],[False,False,True,True],[True,True,True,True],[False,False,True,True],[False,True,False,False],[True,True,False,True],[True,False,False,True],[False,False,False,False]],[[False,False,True,False],[False,False,True,False],[True,True,True,False],[True,False,True,True],[False,False,True,True],[True,True,False,True],[True,False,False,True],[True,True,True,True],[True,False,True,True],[True,True,True,False]]], dtype = "bool")#candidate|4799|(7, 10, 4)|const|bool
bop_4800 = relay.left_shift(bop_4777.astype('uint16'), relay.reshape(const_4799.astype('uint16'), relay.shape_of(bop_4777))) # shape=(7, 10, 4)
func_2000_call = mod.get_global_var('func_2000')
func_2002_call = mutated_mod.get_global_var('func_2002')
call_4807 = func_2000_call()
call_4808 = func_2000_call()
uop_4815 = relay.asinh(bop_4800.astype('float64')) # shape=(7, 10, 4)
func_2439_call = mod.get_global_var('func_2439')
func_2442_call = mutated_mod.get_global_var('func_2442')
call_4825 = relay.TupleGetItem(func_2439_call(relay.reshape(call_4807.astype('float64'), [14, 2, 8])), 0)
call_4826 = relay.TupleGetItem(func_2442_call(relay.reshape(call_4807.astype('float64'), [14, 2, 8])), 0)
func_2079_call = mod.get_global_var('func_2079')
func_2082_call = mutated_mod.get_global_var('func_2082')
const_4829 = relay.const([[-2.959249,-5.969446,-8.049300,-1.577152],[0.217797,-7.387681,1.296503,9.216414],[2.377217,3.993060,7.522806,5.352788],[-8.978109,-3.008004,6.652352,6.125262],[-0.420564,0.968020,1.735395,8.457245],[7.043015,6.501735,-6.809470,-2.096493],[6.843922,0.078425,-7.381275,2.351443],[2.913470,7.020076,5.932946,-4.452442],[6.648807,-2.944903,7.938461,4.241205],[6.076423,4.727167,9.231290,-9.087960],[3.133311,9.585776,-4.929281,-2.006619],[5.520675,9.266715,-1.745192,-6.443580],[0.733746,6.075334,-7.586742,8.747743],[8.212749,0.451570,-9.338728,6.446653],[1.239104,0.946345,0.458747,1.007251],[-4.925137,5.218190,-0.472438,-5.598698],[-0.447628,-5.202701,-9.586790,5.131173],[-4.090671,-5.085156,-2.340261,-9.376922],[-6.243203,2.194011,7.928071,-9.834308],[2.160951,3.504786,8.488908,-5.064885],[6.173780,-8.065888,-0.388282,1.237533],[7.627763,-1.826672,6.840761,7.861502],[-9.686851,6.786147,-2.590771,1.038129],[-2.581261,2.093851,-6.429577,3.248802],[9.476504,0.143174,4.540630,-9.338384],[-4.932504,-5.565984,-3.051510,-4.065396],[0.517259,-5.031172,5.283472,8.251440],[-8.600463,-6.134829,-2.214892,-4.147625],[1.526206,-4.666186,-1.699709,4.377030],[1.756692,-8.585948,-6.599896,-5.283250],[3.153031,3.546685,2.243109,-0.930753],[6.849223,-9.045917,-6.100977,8.033938],[8.330437,5.370087,4.051715,-1.059570],[-6.392759,-9.753980,8.313225,-7.219144],[6.256058,-6.157211,0.123080,0.133646]], dtype = "float64")#candidate|4829|(35, 4)|const|float64
call_4828 = relay.TupleGetItem(func_2079_call(relay.reshape(const_4829.astype('float64'), [4, 7, 5])), 2)
call_4830 = relay.TupleGetItem(func_2082_call(relay.reshape(const_4829.astype('float64'), [4, 7, 5])), 2)
output = relay.Tuple([call_4785,call_4807,uop_4815,call_4825,call_4828,const_4829,])
output2 = relay.Tuple([call_4786,call_4808,uop_4815,call_4826,call_4830,const_4829,])
func_4832 = relay.Function([var_4775,var_4776,], output)
mod['func_4832'] = func_4832
mod = relay.transform.InferType()(mod)
var_4833 = relay.var("var_4833", dtype = "bool", shape = (7, 10, 4))#candidate|4833|(7, 10, 4)|var|bool
var_4834 = relay.var("var_4834", dtype = "bool", shape = (7, 10, 4))#candidate|4834|(7, 10, 4)|var|bool
output = func_4832(var_4833,var_4834,)
func_4835 = relay.Function([var_4833,var_4834,], output)
mutated_mod['func_4835'] = func_4835
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4844 = relay.var("var_4844", dtype = "float64", shape = (11, 11, 5))#candidate|4844|(11, 11, 5)|var|float64
const_4845 = relay.const([[[-3.074066,4.001640,6.190730,7.021580,-6.718251],[-6.834437,-7.349166,2.354053,4.119996,8.221317],[0.286129,2.672944,1.890919,-3.085285,7.017081],[5.250655,-2.940424,-5.003222,-0.365043,-7.300569],[4.497283,-0.091934,9.445251,8.936337,3.375615],[7.807983,8.976042,8.559974,7.052755,0.547604],[-8.455328,-1.703725,5.058425,-4.454080,3.543202],[2.185423,3.636458,-0.068398,1.143589,-3.839457],[-5.854189,-4.713096,-7.569615,-4.145828,7.819456],[-9.703995,-4.319239,-4.061445,6.213483,-5.692190],[-8.427702,4.711937,1.198710,-1.010216,1.284833]],[[4.400629,-0.596957,7.178421,-1.503463,-9.078319],[8.480234,4.273043,-7.196654,-3.660249,-1.223157],[-3.029275,-1.226308,-7.323391,0.399413,-0.304789],[1.365437,5.640792,1.776986,-8.599654,-9.083621],[1.271797,-7.880331,-9.921314,5.842028,-4.100824],[8.447738,-7.901921,9.681654,7.935435,8.458391],[3.898498,-3.920251,4.808346,-4.283484,9.156823],[-0.749664,-5.921410,9.756404,9.511476,4.327628],[-4.039783,-7.589308,-1.017977,7.465731,8.256023],[-1.016375,-2.027289,1.425494,-1.151737,8.207273],[-3.265828,0.613659,-4.347563,4.452648,8.606542]],[[-4.723518,2.772387,-9.083371,-8.012330,-4.307365],[-1.722443,-6.541807,5.248520,-5.091278,3.582684],[6.795505,-9.634787,8.657192,5.889901,-6.033091],[0.207871,-8.640078,-3.359474,1.962517,-2.334643],[-8.314769,-3.681776,8.361692,-9.485303,3.757370],[-9.303515,9.824740,9.760822,6.659103,-8.811298],[5.246518,-7.345818,-7.974610,-8.113891,7.366270],[4.262961,-8.046598,4.546879,7.823651,1.746611],[8.110799,3.895227,-0.876626,3.309998,6.301591],[-5.723371,-5.063590,-6.980953,5.158164,-1.560971],[-5.586153,-2.296916,0.143197,-2.249523,1.309267]],[[0.667436,4.513881,4.067774,-7.353283,-1.671329],[-6.893919,-1.466508,6.449043,-0.598836,-7.467150],[-7.330337,-5.298156,1.966757,-6.294613,2.422355],[2.616528,-8.999585,5.955228,1.264198,1.553892],[-9.676454,-9.665390,-2.587225,4.806595,-5.787008],[5.045647,-4.423549,6.469481,1.759579,-9.593669],[3.049600,9.208383,-3.552215,9.392405,-3.495672],[4.551602,8.581182,-6.259752,-9.058067,-5.600830],[1.042904,5.005128,9.313993,0.908191,-8.176676],[2.223204,6.040107,1.313798,-7.000279,3.219600],[2.986042,5.053791,-5.480072,-2.522221,4.564422]],[[2.992243,-2.390869,4.312755,7.915293,-4.280007],[-4.241445,3.193858,2.081553,7.688375,-6.562650],[-4.303675,-6.162508,-2.977708,0.753689,9.487668],[0.671903,2.610418,3.906883,3.797170,5.666445],[-3.860884,-0.189882,-0.239370,-7.494868,7.903167],[-4.445706,6.305701,5.316179,-1.225459,-6.654980],[7.637826,-5.519733,-2.264163,0.766068,2.751065],[0.304092,-8.748834,9.111881,4.398101,7.371797],[-8.752719,3.046945,-8.458017,6.658231,2.568942],[-3.505894,2.051861,-6.173599,-3.447708,-9.800898],[-4.219090,7.818036,3.171568,2.783747,-6.430370]],[[5.104239,3.137398,-8.760524,3.264907,-9.821029],[-9.307303,1.090144,1.784898,6.145018,-4.859441],[4.297567,8.330278,7.847967,-8.072568,-2.831294],[0.301033,3.809607,-0.508692,-1.604937,-8.103151],[-7.755729,7.441757,-9.727487,7.270649,-6.666261],[5.781839,6.148589,-6.519688,1.452527,8.684331],[-9.300503,7.420246,9.818775,5.539850,9.690676],[-8.068672,-4.445784,-0.315832,8.079258,-2.764275],[2.133019,3.372529,7.825181,6.217141,-0.276246],[-8.459953,-2.760814,1.773053,5.619832,0.199214],[-7.328171,-0.692034,-2.365501,6.300963,7.530179]],[[8.896868,-2.050111,0.192004,7.615912,-7.376011],[9.796400,-7.445751,8.140429,-2.200645,-8.317634],[3.695951,8.205147,-6.371978,-9.919397,2.282452],[5.413411,-8.783927,-5.530450,9.965395,3.553408],[0.982783,-1.292736,-3.418976,1.669552,-6.904238],[-6.736407,-0.163255,-2.985050,6.270522,5.597584],[-4.597803,-2.626972,-9.680961,-7.146003,-2.028347],[8.964984,-5.240919,4.924088,3.804412,4.278986],[-6.731368,-3.939364,-0.240759,3.163403,4.085800],[-4.520018,-0.889909,6.167826,6.830258,-0.881243],[2.998750,-8.882434,-7.160275,-1.432504,-6.567834]],[[6.432079,0.905128,-8.284893,-5.277521,-2.765153],[-7.619367,7.370243,5.984127,5.991746,-1.396151],[-6.656638,3.178244,-2.800213,-6.976935,-3.019943],[-6.227353,2.629343,7.065598,0.383797,-7.570786],[3.494166,9.963330,6.540874,3.815590,4.578920],[-0.016967,8.540245,-7.968373,2.019959,-0.641178],[-2.224727,-4.760164,0.464547,0.841698,9.827065],[-6.361292,-2.384127,-9.020333,-8.205919,-8.141317],[5.269125,3.307547,-0.166344,-5.786991,-6.001287],[6.566052,-7.303414,-4.659712,0.089814,-9.484933],[0.923553,-5.152268,-0.388730,3.146001,-3.199102]],[[3.608552,6.436629,6.441627,-3.094154,1.229497],[-6.171542,6.081205,-6.094220,-0.498755,3.402980],[4.379956,1.022378,-3.446503,-2.353011,-4.170406],[7.698306,-8.233124,-8.159011,8.309397,-2.263099],[5.235941,6.212946,6.951842,9.584063,-3.369564],[-5.358751,0.134060,1.593403,-6.076425,-6.747745],[-2.709866,-1.720733,-1.959029,-0.012208,8.559238],[-6.713603,-0.345673,-1.130273,-4.112374,4.235614],[-8.560465,-0.427367,-4.077352,-5.253590,1.858218],[3.831957,-9.623512,-3.757423,6.903846,-3.763907],[1.283918,6.026239,1.844206,5.069054,4.750196]],[[-7.010038,9.510861,-1.237086,-4.385265,-0.424171],[1.365916,6.610928,1.879810,-3.638469,2.365721],[3.351877,2.797615,-6.267625,-1.724522,-9.141708],[-6.456532,-8.376945,9.815924,4.539084,3.406795],[8.121946,-5.104938,-4.642259,4.011457,-6.238348],[-7.650053,9.729830,-8.315652,-4.561376,-6.025673],[0.300355,8.941140,-4.861165,-1.202387,-7.202169],[4.968969,-2.530008,-3.641965,4.767448,9.566532],[-5.637658,4.436428,7.861514,1.040757,9.441219],[6.705013,5.879314,-3.342470,8.991371,5.181948],[-0.878254,-3.877394,-5.279993,1.635450,-4.570542]],[[2.254780,-7.626614,-2.872384,6.160356,4.342316],[5.977868,3.324711,2.122396,-7.443374,-6.573667],[-6.921823,-3.753400,6.720705,-2.833388,-5.784140],[9.405548,9.501846,7.826750,3.804370,-6.590948],[1.811683,8.776172,-1.294856,-4.246844,-0.220572],[-7.239273,2.304006,2.104335,-2.623717,0.625813],[-6.506425,-2.598934,1.860970,6.619763,-8.701454],[8.169574,-2.257190,-7.610294,-5.186707,8.915490],[4.698083,8.167184,3.491969,0.736591,-3.488749],[-1.075615,2.821120,5.050852,-5.043859,-2.754602],[-1.678397,-9.186237,-7.507246,1.967827,7.628249]]], dtype = "float64")#candidate|4845|(11, 11, 5)|const|float64
bop_4846 = relay.floor_divide(var_4844.astype('float64'), relay.reshape(const_4845.astype('float64'), relay.shape_of(var_4844))) # shape=(11, 11, 5)
bop_4851 = relay.less_equal(bop_4846.astype('bool'), relay.reshape(const_4845.astype('bool'), relay.shape_of(bop_4846))) # shape=(11, 11, 5)
uop_4854 = relay.sin(bop_4851.astype('float32')) # shape=(11, 11, 5)
output = relay.Tuple([uop_4854,])
output2 = relay.Tuple([uop_4854,])
func_4859 = relay.Function([var_4844,], output)
mod['func_4859'] = func_4859
mod = relay.transform.InferType()(mod)
mutated_mod['func_4859'] = func_4859
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4860 = relay.var("var_4860", dtype = "float64", shape = (11, 11, 5))#candidate|4860|(11, 11, 5)|var|float64
func_4859_call = mutated_mod.get_global_var('func_4859')
call_4861 = func_4859_call(var_4860)
output = call_4861
func_4862 = relay.Function([var_4860], output)
mutated_mod['func_4862'] = func_4862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3791_call = mod.get_global_var('func_3791')
func_3793_call = mutated_mod.get_global_var('func_3793')
call_4890 = relay.TupleGetItem(func_3791_call(), 0)
call_4891 = relay.TupleGetItem(func_3793_call(), 0)
output = call_4890
output2 = call_4891
func_4916 = relay.Function([], output)
mod['func_4916'] = func_4916
mod = relay.transform.InferType()(mod)
mutated_mod['func_4916'] = func_4916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4916_call = mutated_mod.get_global_var('func_4916')
call_4917 = func_4916_call()
output = call_4917
func_4918 = relay.Function([], output)
mutated_mod['func_4918'] = func_4918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3144_call = mod.get_global_var('func_3144')
func_3146_call = mutated_mod.get_global_var('func_3146')
call_4949 = func_3144_call()
call_4950 = func_3144_call()
output = call_4949
output2 = call_4950
func_4966 = relay.Function([], output)
mod['func_4966'] = func_4966
mod = relay.transform.InferType()(mod)
mutated_mod['func_4966'] = func_4966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4966_call = mutated_mod.get_global_var('func_4966')
call_4967 = func_4966_call()
output = call_4967
func_4968 = relay.Function([], output)
mutated_mod['func_4968'] = func_4968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1385_call = mod.get_global_var('func_1385')
func_1387_call = mutated_mod.get_global_var('func_1387')
call_4977 = relay.TupleGetItem(func_1385_call(), 0)
call_4978 = relay.TupleGetItem(func_1387_call(), 0)
output = call_4977
output2 = call_4978
func_4981 = relay.Function([], output)
mod['func_4981'] = func_4981
mod = relay.transform.InferType()(mod)
output = func_4981()
func_4982 = relay.Function([], output)
mutated_mod['func_4982'] = func_4982
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4989 = relay.var("var_4989", dtype = "float32", shape = (11, 12, 12))#candidate|4989|(11, 12, 12)|var|float32
uop_4990 = relay.log(var_4989.astype('float32')) # shape=(11, 12, 12)
output = relay.Tuple([uop_4990,])
output2 = relay.Tuple([uop_4990,])
func_4993 = relay.Function([var_4989,], output)
mod['func_4993'] = func_4993
mod = relay.transform.InferType()(mod)
mutated_mod['func_4993'] = func_4993
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4994 = relay.var("var_4994", dtype = "float32", shape = (11, 12, 12))#candidate|4994|(11, 12, 12)|var|float32
func_4993_call = mutated_mod.get_global_var('func_4993')
call_4995 = func_4993_call(var_4994)
output = call_4995
func_4996 = relay.Function([var_4994], output)
mutated_mod['func_4996'] = func_4996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3144_call = mod.get_global_var('func_3144')
func_3146_call = mutated_mod.get_global_var('func_3146')
call_5004 = func_3144_call()
call_5005 = func_3144_call()
func_2079_call = mod.get_global_var('func_2079')
func_2082_call = mutated_mod.get_global_var('func_2082')
const_5029 = relay.const([-3.264808,-2.856462,-6.895358,3.150722,-2.469564,7.035080,2.738078,-6.603660,-6.169587,-0.284657,1.502553,6.411645,-7.224200,-7.328976,9.679476,-3.013472,7.304746,9.964812,6.194485,-5.984839,-5.153567,5.779812,-6.498062,9.050900,2.957047,-5.638720,5.085151,4.577318,-2.126459,8.205294,-0.741588,9.423584,-6.370210,6.047933,-0.178745,1.479741,-9.683556,-0.366989,-4.066920,9.849599,1.275028,-1.907421,9.898556,-8.773425,-9.792260,2.187022,-3.796788,-1.208723,9.327015,-8.824366,-7.488052,9.236309,-7.395146,4.378694,6.568298,8.020831,-8.139219,1.665639,6.231195,5.315359,8.285792,-7.383191,-6.586158,-8.587026,1.057844,1.267621,2.148856,-3.107228,-6.919593,-4.627387,-1.372533,8.799233,-1.247155,-5.826521,-5.043409,8.274848,-8.036787,0.564161,-8.035735,-1.812484,1.699854,8.625741,-4.040546,-8.135724,-9.562911,9.595656,-3.095669,5.421875,4.543399,2.631518,-7.143102,-5.760485,-4.077613,1.073263,1.961785,-6.925621,5.345806,6.132516,3.565715,-0.976957,1.537247,-0.174656,-4.739326,-4.148150,8.375549,-7.385107,-4.491492,-9.392773,-6.268707,2.565504,-3.907855,-6.197720,-7.703830,9.547050,-8.890291,7.828364,9.812364,3.745956,3.876678,-7.070831,6.820550,-7.212948,6.077351,8.637244,-7.868088,0.543208,-3.602537,-8.136916,-9.053924,3.960198,-0.362941,-0.629116,-1.766103,4.891107,1.185108,4.424879,-7.447914,-2.318796,-4.097178,-9.981905], dtype = "float64")#candidate|5029|(140,)|const|float64
call_5028 = relay.TupleGetItem(func_2079_call(relay.reshape(const_5029.astype('float64'), [4, 7, 5])), 3)
call_5030 = relay.TupleGetItem(func_2082_call(relay.reshape(const_5029.astype('float64'), [4, 7, 5])), 3)
output = relay.Tuple([call_5004,call_5028,const_5029,])
output2 = relay.Tuple([call_5005,call_5030,const_5029,])
func_5034 = relay.Function([], output)
mod['func_5034'] = func_5034
mod = relay.transform.InferType()(mod)
mutated_mod['func_5034'] = func_5034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5034_call = mutated_mod.get_global_var('func_5034')
call_5035 = func_5034_call()
output = call_5035
func_5036 = relay.Function([], output)
mutated_mod['func_5036'] = func_5036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_561_call = mod.get_global_var('func_561')
func_563_call = mutated_mod.get_global_var('func_563')
call_5082 = func_561_call()
call_5083 = func_561_call()
var_5089 = relay.var("var_5089", dtype = "float64", shape = (14, 2, 8))#candidate|5089|(14, 2, 8)|var|float64
bop_5090 = relay.left_shift(call_5082.astype('uint32'), relay.reshape(var_5089.astype('uint32'), relay.shape_of(call_5082))) # shape=(14, 2, 8)
bop_5093 = relay.left_shift(call_5083.astype('uint32'), relay.reshape(var_5089.astype('uint32'), relay.shape_of(call_5083))) # shape=(14, 2, 8)
func_2729_call = mod.get_global_var('func_2729')
func_2731_call = mutated_mod.get_global_var('func_2731')
call_5099 = relay.TupleGetItem(func_2729_call(), 2)
call_5100 = relay.TupleGetItem(func_2731_call(), 2)
output = relay.Tuple([bop_5090,call_5099,])
output2 = relay.Tuple([bop_5093,call_5100,])
func_5105 = relay.Function([var_5089,], output)
mod['func_5105'] = func_5105
mod = relay.transform.InferType()(mod)
mutated_mod['func_5105'] = func_5105
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5106 = relay.var("var_5106", dtype = "float64", shape = (14, 2, 8))#candidate|5106|(14, 2, 8)|var|float64
func_5105_call = mutated_mod.get_global_var('func_5105')
call_5107 = func_5105_call(var_5106)
output = call_5107
func_5108 = relay.Function([var_5106], output)
mutated_mod['func_5108'] = func_5108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4724_call = mod.get_global_var('func_4724')
func_4725_call = mutated_mod.get_global_var('func_4725')
call_5113 = func_4724_call()
call_5114 = func_4724_call()
output = relay.Tuple([call_5113,])
output2 = relay.Tuple([call_5114,])
func_5115 = relay.Function([], output)
mod['func_5115'] = func_5115
mod = relay.transform.InferType()(mod)
output = func_5115()
func_5116 = relay.Function([], output)
mutated_mod['func_5116'] = func_5116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_721_call = mod.get_global_var('func_721')
func_722_call = mutated_mod.get_global_var('func_722')
call_5147 = relay.TupleGetItem(func_721_call(), 0)
call_5148 = relay.TupleGetItem(func_722_call(), 0)
func_1059_call = mod.get_global_var('func_1059')
func_1063_call = mutated_mod.get_global_var('func_1063')
var_5151 = relay.var("var_5151", dtype = "float64", shape = (112,))#candidate|5151|(112,)|var|float64
var_5152 = relay.var("var_5152", dtype = "float64", shape = (224,))#candidate|5152|(224,)|var|float64
var_5153 = relay.var("var_5153", dtype = "float64", shape = (4, 256))#candidate|5153|(4, 256)|var|float64
call_5150 = relay.TupleGetItem(func_1059_call(relay.reshape(var_5151.astype('float64'), [14, 1, 8]), relay.reshape(var_5152.astype('float64'), [224,]), relay.reshape(var_5153.astype('float64'), [1024,]), ), 1)
call_5154 = relay.TupleGetItem(func_1063_call(relay.reshape(var_5151.astype('float64'), [14, 1, 8]), relay.reshape(var_5152.astype('float64'), [224,]), relay.reshape(var_5153.astype('float64'), [1024,]), ), 1)
output = relay.Tuple([call_5147,call_5150,var_5151,var_5152,var_5153,])
output2 = relay.Tuple([call_5148,call_5154,var_5151,var_5152,var_5153,])
func_5158 = relay.Function([var_5151,var_5152,var_5153,], output)
mod['func_5158'] = func_5158
mod = relay.transform.InferType()(mod)
mutated_mod['func_5158'] = func_5158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5158_call = mutated_mod.get_global_var('func_5158')
var_5160 = relay.var("var_5160", dtype = "float64", shape = (112,))#candidate|5160|(112,)|var|float64
var_5161 = relay.var("var_5161", dtype = "float64", shape = (224,))#candidate|5161|(224,)|var|float64
var_5162 = relay.var("var_5162", dtype = "float64", shape = (4, 256))#candidate|5162|(4, 256)|var|float64
call_5159 = func_5158_call(var_5160,var_5161,var_5162,)
output = call_5159
func_5163 = relay.Function([var_5160,var_5161,var_5162,], output)
mutated_mod['func_5163'] = func_5163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mod.get_global_var('func_918')
func_919_call = mutated_mod.get_global_var('func_919')
call_5170 = func_918_call()
call_5171 = func_918_call()
output = relay.Tuple([call_5170,])
output2 = relay.Tuple([call_5171,])
func_5176 = relay.Function([], output)
mod['func_5176'] = func_5176
mod = relay.transform.InferType()(mod)
output = func_5176()
func_5177 = relay.Function([], output)
mutated_mod['func_5177'] = func_5177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3952_call = mod.get_global_var('func_3952')
func_3953_call = mutated_mod.get_global_var('func_3953')
call_5198 = relay.TupleGetItem(func_3952_call(), 0)
call_5199 = relay.TupleGetItem(func_3953_call(), 0)
output = call_5198
output2 = call_5199
func_5205 = relay.Function([], output)
mod['func_5205'] = func_5205
mod = relay.transform.InferType()(mod)
mutated_mod['func_5205'] = func_5205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5205_call = mutated_mod.get_global_var('func_5205')
call_5206 = func_5205_call()
output = call_5206
func_5207 = relay.Function([], output)
mutated_mod['func_5207'] = func_5207
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5221 = relay.var("var_5221", dtype = "float32", shape = (14, 1, 7))#candidate|5221|(14, 1, 7)|var|float32
uop_5222 = relay.atanh(var_5221.astype('float32')) # shape=(14, 1, 7)
func_5205_call = mod.get_global_var('func_5205')
func_5207_call = mutated_mod.get_global_var('func_5207')
call_5230 = func_5205_call()
call_5231 = func_5205_call()
uop_5239 = relay.acos(uop_5222.astype('float64')) # shape=(14, 1, 7)
func_918_call = mod.get_global_var('func_918')
func_919_call = mutated_mod.get_global_var('func_919')
call_5241 = func_918_call()
call_5242 = func_918_call()
output = relay.Tuple([call_5230,uop_5239,call_5241,])
output2 = relay.Tuple([call_5231,uop_5239,call_5242,])
func_5255 = relay.Function([var_5221,], output)
mod['func_5255'] = func_5255
mod = relay.transform.InferType()(mod)
var_5256 = relay.var("var_5256", dtype = "float32", shape = (14, 1, 7))#candidate|5256|(14, 1, 7)|var|float32
output = func_5255(var_5256)
func_5257 = relay.Function([var_5256], output)
mutated_mod['func_5257'] = func_5257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mod.get_global_var('func_918')
func_919_call = mutated_mod.get_global_var('func_919')
call_5311 = func_918_call()
call_5312 = func_918_call()
func_2528_call = mod.get_global_var('func_2528')
func_2532_call = mutated_mod.get_global_var('func_2532')
const_5324 = relay.const([4,3,-9,2,6,-7,-5,1,4,-9,-2,-10,7,-8,2,9,5,8,4,4,-7,5,4,9,-3,-2,-7,7,8,9,5,3,-9,-5,-4,-5,2,3,3,5,-2,-5,3,-5,5,10,1,1,-8,-2,-5,-1,6,-4,-6,9,10,-9,5,-4,9,10,7,9,-8,-8,-10,2,3,-7,7,-10,-1,9,-4,-6,-5,2,-10,9,-4,10,6,-1,8,-1,-5,1,10,2,3,9,-6,1,-4,3,7,-5,7,-3,6,-9,5,-7,-2,-10,-8,-4,-2,10,7,-7,9,9,-7,-9,8,-6,-2,9,3,-10,10,5,8,9,9,4,-7,-1,7,9,-10,8,1,7,-7,-7,8,9,5,5,-4,-1,-10,-5,-4,2,-3,-7,8,-8,-8,1], dtype = "int16")#candidate|5324|(154,)|const|int16
const_5325 = relay.const([6,-10,10,-8,2,3,6,-4,-3,-9,-1,4,-3,6,-10,6,9,-5,-9,-9,-2,8,2,-6,-1,5,3,3,4,2,6,-10,-3,3,-9,-2,-7,-10,-6,-3,-3,-1,10,2,5,9,-3,8,5,9,6,-6,-4,3,3,7,6,2,-3,-1,-10,2,1,-9,-3,-2,-10,3,5,3,2,1,9,-6,-10,3,-9,-1,-4,7,-9,-6,7,2,-5,-7,-7,7,-4,10,-1,-1,-7,1,3,9,-6,10,4,3,-8,-10,-1,-5,-1,-8,-8,-3,3,6,-1,-7,-10,10,8,-5,4,-3,2,1,-3,-6,-9,-7,2,-6,6,1,2,-10,-5,-9,10,-7,2,-4,6,-5,8,5,5,6,-9,-9,-10,-1,6,5,4,8,9,-10,-3,-10,-6,2,8,-5,5,-8,-3,-10,-1,-2,-9,10,4,3,-4,8,-7,3,8,-4,10,-8,3,1,-4,-8,5,3,9,-7,-8,-6,7,10,-7,-8,8,-1,3,4,5,4,-3,9,2,6,-3,5,-4,-5,1,2,-9,-10,-5,4,8,1,-5,-3,8,-7,2,1,8,8,9,-1,-3,3,-5,9,4,-5,10,-8,-7,-9,8,6,-8,-9,4,-5,1,6,-6,-1,5,-1,-4,-5,-3,-10,6,9,10,-9,8,-3,6,8,4,-2,7,-4,-2,10,3,10,-7,3,9,-4,-8,7,-6,-5,4,9,-1,-10,4,-2,-3,-8,1,8,3,-6,-8,-6,8,5,9,1,1,-6,-5,-3,9,7,-3,2,6,9,-1,-8,-6,-10,1,6,-5,8,-1,6,-2,-1,-9,-1,3,9,-4,-2,2,-7,3,4,8,-8,2,-8,-9,7,4,-5,9,10,10,6,-5,-4,8,6,9,2,10,-6,-1,-8,-3,1,-6,-5,-4,-10,-4,7,4,8,9,-5,-2,-9,5,7,2,-2,-10,5,-8,2,9,5,-5,7,5,-5,4,-9,3,9,-5,-4,-7,-6,5,-8,9,8,-8,-10,-10,9,2,4,-3,1,-3,-10,5,5,6,-4,9,-1,-8,10,-9,-3,7,6,-10,8,3,4,-8,8,6,-10,-4,4,3,2,-4,-3,-2,-1,-6,-6,10,5,-2,-1,4,3,-4,4,2,-1,2,-7,3,-7,-10,-7,4,6,4,-4,9,-8,4,-10,9,3,5,4,-10,6,5,-8,-7,4,-2,-2,6,5,4,-8,-9,2,1,-4,10,-10,-5,-5,5,-4,10,9,7,-7,9,2,6,-4,4,9,9,-1,8,-7,-5,-9,6,-2,1,-4,5,-2,3,-10,-3,-3,10,9,7,-2,-6,9,10,6,1,6,5,-6,4,-7,7,-1,1,-7,-5,-5,2,6,-5,5,-2,1,9,-8,-5,9,-5,3,10,6,-8,8,-5,2,-5,-6,-8,-6,6,9,9,7,8,-9,9,2,6,-7,-4,-3,-6,6,7,2,-8,-9,6,-2,-6,-1,-8,-4,4,-5,2,7,-8,3,-9,-9,3,5,-3,-6,-7,6,3,-2,-1,5,-7,-3,-7,8,-1,-2,-6,8,5,-2,10,-10,10,-9,-8,-6,9,8,6,-4,5,-3,-5,4,-4,4,4,6,3,5,-2,-6,10,8,10,-5,10,-7,9,-6,-8,7,-2,6,-8,9,-3,10,-7,-9,10,5,2,-8,-5,-3,5,-5,-3,-6,-3,1,-10,-9,-9,5,4,3,1,-8,6,-9,3,9,6,-7,10,7,8,6,-8,-7,2,8,-9,-2,-8,-7,-5,-7,4,2,-1,-6,6,-4,-7,-5,-1,2,9,-9,5,10,-4,10,2,-4,10,-1,3,9,8,-9,-8,3,5,6,7,9,-4,1,-1,-8,6,5,5,-9,9,4,-9,5,-8,-5,7,-6,2,-7,-4,-4,-4,-2,-5,2,1,9,2,5,5,2,-3,-4,-10,10,6,6,4,-9,-3,3,6,5,8,-5,-9,6,9,-10,1,-3,-3,6,-1,6,-5,-7,5,-8,-1,5,-2,-5,-10,-10,-3,9,3,3,2,7,2,-8,-7,7,9,-1,4,-2,1,9,-4,-1,-6,1,6,7,6,-3,4,-3,6,6,10,-8,7,-4,-6,7,9,-1,-8,3,6,8,-9,-4,5,-7,-7,5,-2,4,1,-3,-9,-7,5,-2,-7,-2,1,1,8,-10,-5,-9,-1,-7,2,5,4,-10,-2,-9,-1,7,-1,-8,8,-3,3,8,-5,-8,-4,-8,-5,-5,-1,7,-9,5,-3,-8,3,2,5,9,6,7,-2,-8,3,5,-10,-7,-9,1,-5,4,2,3,-7,-5,2,5,-7,3,6,6,-2,-9,5,-6,-8,-8,6,8,-6,8,-5,3,8,3,-4,4,-4,-1,-2,9,5,10,9,-7,-1,4,-10,9,3,-3,-3,-4,-7,-5,-2,-9,-2,-8,-7,7,-2,3,9,1,5,10,-9,6,1,-7,6,2,4,-8,-7,-10,-9,10,-6,2,4,-1,10,3,1,-6,7,-4,8,-4,8,-1,-7,-4,5,-4,10,4,-5,1,8,-2,5,-5,-7,-7,1,1,-2,-10,-3,-6,10,-4,8,10,3,2,-5,3,6,-6,-8,6,3,5,-10,10,-10,6,10,-7,-5,4,-5,-3,-5,-9,-7,-2,-3,-10,-7,-7,-5,-8,-9,1,-1,-6,-2,-7,-10,-9,-5,9,8,-3,10,-6,2,-3,7,5,-10,4,9,-8,-10,-6,-8,3,6,4,5,-4,-2,-8,-10,-6,-1,2,-4,9,-7,-8,-1,2,-8,-5,4,10,6,-4,-10,-9,-3,-10,-1,-8,5,-5,9,-6,-4,10,2,-6,9,-7,2,-9,-8,1,-8,-8,-7,1,-10,2,2,4,3,4,-3,2,-6,-2,10,4,2,-2,6,-6,-4,2,2,2,9,-9,7,-8,2,9,-1,1,6,-4,-1,-3,-9,-3,-3,6,8,-2,7,-10,-8,-1,2,4,-7,4,-9,3,2,-8,-10,4,-2,-5,-8,7,1,-5,-2,-3,-7,9,2,5,9,-6,10,6,-10,-10,-5,-2,-9,-9,8,-3,7,-5,5,2,3,-2,-9,6,1,-8,7,1,9,-8,-2,-5,1,7,-10,-10,6,-8,10,4,2,-8,-4,-4,8,1,2,-8,-8,9,-3,-2,10,-4,6,2,2,8,8,8,-5,-6,6,10,-1,1,7,-1,-3,-5,-2,10,6,9,-1,2,5,3,-3,5,-1,6,-10,-2,1,-6,8,-9,4,-10,5,1,9,-1,-6,-8,5,-4,2,-9,-5,10,-9,-8,8,-9,10,-5,5,-5,4,-7,-9,3,-7,4,7,7,-4,-10,5,-5,9,-5,-6,5,-6,-1,5,4,-6,4,-4,-1,6,-1,1,5,6,6,2,3,6,-3,-10,3,-9,1,-9,-4,-4,-7,8,6,-4,7,-4,6,-6,10,-7,-2,-1,-2,3,-5,-10,1,4,4,-8,8,1,3,-4,-3,-10,-9,-6,-1,-6,6,-1,-6,4,5,-10,5,6,1,5,-10,7,-5,-10,-1,-3,4,6,10,-9,2,-7,-3,9,2,-7,10,-2,6,1,10,-8,9,6,4,2,5,4,-4,-1,8,9,-2,3,4,-9,8,-1,-1,-6,-4,-10,-10,8,-9,10,-9,-7,9,10,6,10,-9,2,-9,7,-7,-2,-3,-10,-1,4,-9,-2,-3,-2,4,-4,2,-6,-2,-4,-10,-7,1,5,-8,-2,2,-3,-6,3,-6,6,-2,-1,-3,-5,-3,6,-8,6,2,2,3,8,-2,-1,9,-8,-10,-5,-4,-6,1,-3,-2,6,8,-7,-5,10,7,8,9,-7,5,-3,-10,-9,10,-1,-2,8,5,1,-10,9,-2,-5,3,1,-4,8,-3,5,9,-6,5,1,9,1,-10,-9,5,7,-6,5,-5,3,2,-1,-6,-1,3,10,-3,1,9,-8,-6,4,5,1,4,8,-4,8,8,-2,1,-2,2,10,5,-8,4,4,-3,9,-1,-5,8,6,3,6,9,-10,1,-2,7,9,4,-1,2,-6,7,-9,-7,10,2,-5,5,-2,7,-5,6,8,-9,8,-8,-4,6,-1,-10,-2,-8,3,-6,10,-3,-8,10,10,4,1,-10,9,10,-8,1,-3,1,-2,5,8,6,-6,1,-6,-1,7,5,9,5,8,-9,5,-8,-7,-9,-8,3,3,-9,-1,7,-4,-5,10,2,6,-8,3,9,9,-5,5,3,3,7,4,3,10,1,-10,9,-6,6,-3,9,5,8,-3,-9,3,-2,4,3,7,-4,-8,-2,10,-4,-5,4,9,9,3,10,-6,10,-10,-1,-10,-2,10,5,-2,-4,1,8,-1,2,6,9,4,9,-6,-1,-7,-7,8,8,10,-8,1,-1,-4,-8,4,-10,1,-2,-2,-5,9,8,3,-9,10,-4,-5,5,7,-8,3,9,9,-2,8,2,9,-5,5,-5,-3,-6,-3,6,6,-1,5,-2,-3,5,-2,-9,6,3,-7,-6,7,-7,-5,-10,-10,-10,1,9,-8,7,3,3,1,-1,-6,7,9,4,8,4,5,2,8,1,-8,-6,-8,10,-4,-6,-8,-6,8,10,3,3,-8,3,-10,1,-7,-9,-5,2,10,2,10,4,7,3,9,-6,-5,-4,5,3,4,5,-4,1,-5,-3,-2,-5,2,8,8,-10,-3,9,10,8,-5,3,9,5,-8,3,5,8,-9,-9,-10,-1,-3,-1,-10,9,3,7,8,8,-10,8,2,-3,2,-8,-2,5,7,2,-6,-7,5,-1,-5,8,1,-1,2,1,-7,-6,8,-4,-9,4,-7,2,-4,4,-1,7,10,2,3,6,4,6,-5,-7,-7,10,2,6,7,7,2,-10,1,4,7,3,4,-1,2,-5,-9,-4,9,6,10,3,-5,-4,-7,2,8,3,-5,-3,2,-5,-3,1,7,-9,1,10,-7,4,-3,-5,-2,-5,5,-1,7,8,-4,-3,8,-9,4,-7,-4,-4,-9,-9,9,7,5,-9,-5,2,7,2,7,-6,-3,-1,-4,-5,4,-4,-2,-7,9,9,4,-5,9,8,-1,9,7,-2,-5,-2,2,3,6,-1,5,-1,3,2,5,10,-6,1,-8,-2,9,3,-1,5,6,4,-8,-10,5,5,-2,8,-3,-1,2,-4,-9,-2,3,10,5,-1,-3,4,-3,-7,-3,4,6,4,9,8,-5,8,10,-9,4,-8,9,2,-10,-8,6,8,7,9,-2,-4,9,-6,2,4,3,10,3,-5,-2,5,-7,7,4,2,3,2,-9,-1,-4,-4,6,-1,7,1,3,5,-8,5,-8,-8,4,5,8,4,-2,9,4,8,-7,9,4,9,-8,-3,-3,9,1,-9,-9,-1,3,10,1,9,6,10,-1,3,-3,-6,-5,4,-9,5,7,-1,-7,8,-1,-7,-4,-1,6,-4,8,7,-5,1,3,-3,1,1,-9,7,-5,-8,-1,-3,3,-8,-7,6,4,-7,-3,-9,6,-2,10,-4,-4,-5,-3,2,10,-9,-2,1,2,7,10,-10,8,1,3,-5,10,-2,2,1,3,-1,6,-5,9,4,7,-6,-7,-5,4,9,-3,1,6,-9,3,-6,-9,-7,-4,-10,4,8,-4,-6,-4,-6,-8,4,10,-7,-1,-10,-5,-1,-8,9,-8,7,-9,-4,-8,2,7,3,7,-10,2,-1,9,-5,-4,10,1,-7,8,5,-2,-3,-3,8,-6,-10,-10,-5,-2,5,3,7,-3,-6,6,9,10,-8,-10,-3,-5,-5,2,4,-10,-2,-4,-9,-3,-10,-8,-8,-2,-1,3,1,7,-2,5,4,7,-10,-5,10,6,9,-8,2,3,4,-7,3,10,2,-3,1,-2,-1,-2,7,2,3,2,1,9,1,-10,-10,2,-4,-10,-5,9,-1,8,10,5,1,9,5,7,5,-2,8,1,-9,8,-5,-1,-8,6,2,-1,1,4,1,-3,1,-3,1,10,5,5,6,8,-8,4,-6,-10,-9,4,-8,-6,2,7,-5,3,-6,2,6,-8,4,2,-8,-8,1,-7,-1,-9,4,8,4,9,-2,3,-1,-2,-4,-7,-1,9,9,2,-9,-2,-8,2,2,5,4,-3,1,-2,-4,-7,-3,8,4,-9,10,8,2,3,5,1,5,6,1,-9,6,9,-6,-9,-6,5,-10,7,5,9,5,-1,3,-4,-5,9,-3,-1,7,7,-8,1,-7,1,6,4,-1,-2,4,9,1,1,10,10,1,1,4,-7,-2,-3,-10,10,3,6,-9,7,4,-3,1,2,-5,-9,-6,-9,5,-7,-10,6,10,-9,8,-9,3,9,-9,3,-5,-10,1,1,1,2,-6,5,2,-5,9,5,9,-5,8,-10,-2,-5,-2,-10,-4,-6,-1,-4,-4,-3,4,2,-5,-2,7,-5,-4,6,7,-3,-6,-1,10,10,-6,-5,-5,6,8,-3,1,7,-2,-3,7,-2,-5,-10,10,-8,-4,-9,-4,9,4,-6,-3,10,4,-4,1,3,-9,-10,-2,-5,3,-5,10,6,7,-1,-7,-4,6,1,6,-3,7,-5,-2,-5,-6,-10,4,2,-2,-2,4,9,5,-9,-3,7,-4,1,5,-10,8,-7,10,4,2,10,-1,10,-6,-1,9,-1,2,-10,-7,6,-10,8,4,-1,-7,4,9,-7,3,6,-6,7,-8,-5,-5,2,5,7,-1,6,1,-9,-4,-5,-4,10,-9,-8,-2,-6,5,6,8,-7,-6,-9,5,-7,-4,-7,-5,-6,4,5,-8,-6,-9,-3,6,7,5,8,4,10,-10,-4,-3,-1,-8,-2,-7,9,1,-4,4,-10,5,-10,3,-7,-6,-8,-5,6,7,-10,-8,-2,-3,-7,-8,-9,-5,4,-8,1,-5,-4,9,-2,10,5,-2,-7,5,-3,1,8,10,3,4,-3,4,9,-7,-2,-4,-5,5,-3,-7,5,-10,-5,-4,8,4,-7,9,2,9,-3,2,-1,-9,1,-3,-8,-7,3,1,9,5,4,4,-1,3,-9,-1,3,-7,8,1,2,8,9,-9,7,-6,9,10,-4,4,-7,4,-5,-4,-10,10,3,9,1,2,-1,2,10,-10,2,-10,8,-9,-6,9,-10,-9,-1,4,-6,10,5,-9,-4,1,-4,-5,6,9,-8,9,-9,10,-7,-2,3,2,5,-4,10,-5,8,-1,5,-8,8,3,-6,-9,-7,5,2,7,9,-6,-9,-5,2,-3,4,2,-9,-3,-7,-7,1,4,9,1,-3,7,10,10,6,9,-7,5,-5,10,-1,4,-10,7,10,-7,7,-6,6,6,-1,5,5,1,-10,-10,9,3,2,9,10,-8,2,1,-2,-3,2,-9,9,5,-5,2,-10,-3,7,-6,-10,1,10,1,8,5,3,7,5,5,8,4,-4,-2,-1,-7,3,-4,-1,5,8,-9], dtype = "uint64")#candidate|5325|(2816,)|const|uint64
call_5323 = relay.TupleGetItem(func_2528_call(relay.reshape(const_5324.astype('int16'), [154,]), relay.reshape(const_5325.astype('uint64'), [1, 2816]), ), 2)
call_5326 = relay.TupleGetItem(func_2532_call(relay.reshape(const_5324.astype('int16'), [154,]), relay.reshape(const_5325.astype('uint64'), [1, 2816]), ), 2)
output = relay.Tuple([call_5311,call_5323,const_5324,const_5325,])
output2 = relay.Tuple([call_5312,call_5326,const_5324,const_5325,])
func_5333 = relay.Function([], output)
mod['func_5333'] = func_5333
mod = relay.transform.InferType()(mod)
output = func_5333()
func_5334 = relay.Function([], output)
mutated_mod['func_5334'] = func_5334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1816_call = mod.get_global_var('func_1816')
func_1817_call = mutated_mod.get_global_var('func_1817')
call_5404 = relay.TupleGetItem(func_1816_call(), 0)
call_5405 = relay.TupleGetItem(func_1817_call(), 0)
output = relay.Tuple([call_5404,])
output2 = relay.Tuple([call_5405,])
func_5406 = relay.Function([], output)
mod['func_5406'] = func_5406
mod = relay.transform.InferType()(mod)
mutated_mod['func_5406'] = func_5406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5406_call = mutated_mod.get_global_var('func_5406')
call_5407 = func_5406_call()
output = call_5407
func_5408 = relay.Function([], output)
mutated_mod['func_5408'] = func_5408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_479_call = mod.get_global_var('func_479')
func_481_call = mutated_mod.get_global_var('func_481')
call_5411 = relay.TupleGetItem(func_479_call(), 0)
call_5412 = relay.TupleGetItem(func_481_call(), 0)
const_5414 = relay.const([[[1.334734,-2.374380,7.293868,-4.569332,2.563687,-8.016197,8.159455,-2.159189],[-9.398254,-1.711211,-2.912220,-4.957185,-7.552803,9.059687,4.226133,7.341268]],[[8.156889,-2.344056,-6.105894,5.665672,-3.164271,3.946682,-9.371422,2.730222],[9.627119,-6.547350,-5.561614,9.568831,5.183912,7.342369,-9.788955,8.845754]],[[-7.463629,-5.477640,-9.369267,-0.435094,2.520492,8.877938,-1.921380,-2.653514],[-6.316735,1.570182,2.823304,5.244103,2.156653,-7.390978,8.251954,-2.014051]],[[4.368577,6.939010,-1.962978,-3.493380,4.948333,9.252188,-3.844441,6.696198],[-2.937226,-5.874446,0.292500,-7.262546,-3.334286,-5.575080,4.788392,6.048814]],[[0.846651,-4.423622,-9.693618,3.223077,-3.718695,3.935534,-4.881067,5.245725],[2.947854,3.910852,-8.451930,-2.759059,-0.883136,-5.758426,4.755740,-0.222873]],[[-1.599074,-4.289834,5.204109,-5.732468,-9.095281,-9.757319,-2.526304,2.504451],[0.969157,7.438242,3.073799,-7.740601,-7.050400,5.830051,-3.871696,2.583051]],[[-0.337999,-1.061683,5.561971,-6.435419,-6.796188,2.366567,-9.237657,2.481317],[8.529823,0.732276,-3.220866,-7.669817,5.250475,-9.600034,1.195360,-8.384446]],[[0.816081,9.887141,-9.147744,-8.952353,-6.860963,1.503578,-2.130177,5.584097],[9.813125,-1.048613,-4.766737,5.150288,-4.558891,-0.372438,4.339213,-0.976710]],[[4.929355,6.521911,1.792101,-6.065789,5.452721,-9.134428,-3.984276,0.873660],[7.884662,3.275540,-7.715915,9.289644,-1.909043,-6.583060,-3.925745,-4.800446]],[[-4.236112,4.226541,6.394614,-5.351276,-5.340227,3.948751,-8.822394,-7.640223],[-1.026116,1.959773,-0.981644,-0.546956,-7.643623,-2.363743,7.526444,-1.493462]],[[8.412963,9.102500,-9.596590,4.926021,-7.210532,2.433380,-8.831962,-5.800116],[-0.638402,0.583599,-6.548767,4.868496,5.773555,-2.779414,5.038138,-3.968119]],[[-6.622687,9.613558,5.215988,1.294895,0.616222,-9.377084,5.426055,7.298476],[7.818620,-2.954701,-2.609829,-2.474947,-0.926659,-5.548312,-1.984383,-0.322434]],[[-4.455832,3.075172,-3.449475,3.576591,3.143283,1.251195,0.152676,-2.200059],[-5.944897,-8.236757,9.217629,-8.508866,4.938272,7.975672,8.360929,0.780728]],[[4.058416,-0.395752,6.494414,-5.114412,1.698188,1.958761,-4.822134,4.853213],[8.746173,7.618829,4.147105,-8.389051,-7.005032,-4.478961,2.199794,2.466371]]], dtype = "float64")#candidate|5414|(14, 2, 8)|const|float64
bop_5415 = relay.bitwise_xor(call_5411.astype('uint32'), relay.reshape(const_5414.astype('uint32'), relay.shape_of(call_5411))) # shape=(14, 2, 8)
bop_5418 = relay.bitwise_xor(call_5412.astype('uint32'), relay.reshape(const_5414.astype('uint32'), relay.shape_of(call_5412))) # shape=(14, 2, 8)
func_2154_call = mod.get_global_var('func_2154')
func_2158_call = mutated_mod.get_global_var('func_2158')
const_5423 = relay.const([-8,-9,2,1,6,7,-5,5,-6,-2,-9,-7,2,-5,-6,-4,-9,3,-9,-1,-10,-7,7,-6,10,-10,-8,-9,2,-3,-2,5,1,3,2,-5,4,-7,3,-4,3,3,2,4,-9,4,-3,1,7,-4,-1,1,-8,-8,2,-3,7,-8,7,3,-6,-7,6,-5,-3,-9,-7,-10,9,-5,10,-7,5,6,-7,9,-5,-4,-4,1,-9,2,3,2,-1,-4,-6,-10,8,2,4,-9,-6,10,-6,-9,-5,1,-4,1,-2,10,10,7,-5,-3,10,10,9,-8,-2,9,8,7,-5,-1,7,-4,-1,-5,2,7,-4,-10,6,-7,6,8,-10,-10,-5,-3,-10,9,8,8,-4,1,-2,10,-2,-8,6,4,1,2,-3,-6,2,6,1,-1,9,-2], dtype = "int16")#candidate|5423|(154,)|const|int16
const_5424 = relay.const([-8,-2,-5,4,-4,-1,1,-3,-9,-4,6,-9,10,-9,10,6,-2,6,-7,-5,5,1,-4,-5,-9,7,4,-4,-5,-7,-8,-5,-3,8,-1,-5,10,2,-10,8,8,7,-3,-6,-4,5,8,-2,1,5,2,-10,-5,8,-1,-7,2,-1,-2,7,-2,8,4,-2,-10,9,-8,8,-1,-1,3,-3,9,-1,-1,-7,-3,-2,6,2,-3,-2,7,-6,-8,-3,4,-7,-10,-6,-9,3,-9,-6,10,-5,-8,4,6,-6,-7,-5,-6,6,1,8,-4,-3,-7,9,9,-10,10,-2,4,-1,10,-3,-8,-4,-10,2,-5,-6,4,-10,9,7,4,8,-1,10,-4,-10,4,5,8,8,10,8,1,-4,7,-2,5,10,8,9,-7,-6,5,-2,9,-6,6,-1,-3,-7,-8,-1,8,9,5,10,7,10,-9,4,-4,5,6,7,2,-10,-5,-3,4,3,-2,-1,8,2,6,3,8,-4,-5,4,6,-8,-4,-6,-5,-10,-1,-7,-4,8,4,-4,3,-5,-6,4,2,3,-2,-8,9,3,9,-2,-8,-5,-4,-5,4,5,-10,3,10,-9,6,-9,-5,8,-4,-9,1,-5,10,3,-9,-5,7,10,-4,2,-6,7,-5,5,5,4,-7,-2,8,-2,-2,-7,-5,-8,7,10,-1,5,2,-7,-4,-3,-9,-10,8,5,1,1,-8,4,9,9,1,-5,-3,-9,3,-10,7,-1,-1,7,8,-7,-8,-4,-5,8,6,-8,-8,-8,9,3,-7,10,-1,-10,-8,-7,-8,-7,3,-8,9,-2,2,-7,-7,6,-7,1,-7,6,10,4,-4,2,6,-10,5,-1,-1,8,9,1,-10,3,-7,-3,-2,-6,9,8,7,10,10,-9,-8,-9,10,-4,-6,10,-5,8,-3,6,2,7,3,-3,7,-6,-10,-3,-6,-3,-3,4,7,5,-8,-1,-6,2,-4,-2,7,-7,4,-7,8,-3,-2,-6,10,-10,2,-1,-8,8,7,4,-10,1,10,4,-8,6,3,1,-5,4,-2,8,9,3,-7,-2,-7,-9,-10,4,10,-10,-4,-6,3,6,6,-7,-9,-3,-7,-1,7,-1,5,-5,-5,-7,5,8,5,3,-8,-8,-1,3,-7,2,8,-3,9,5,-4,-3,-6,-8,6,4,-4,-3,5,-4,-2,-10,-2,-3,-2,4,-3,-4,-9,1,4,9,8,-2,10,9,4,4,2,-6,-6,-8,-9,-9,7,-2,-3,-8,5,-6,-7,8,-4,-9,10,9,-8,-6,-1,5,-2,10,2,-8,9,-3,-9,-10,-5,-9,6,2,7,3,2,-8,7,-2,6,-7,4,-3,-2,5,-4,4,-2,-4,-4,-7,-6,-1,-10,3,2,1,1,8,7,-1,-10,10,1,9,2,-2,-10,1,-5,-8,-6,3,-4,-9,6,3,6,6,-9,3,-4,2,-7,5,-9,8,-5,1,2,4,3,-4,3,6,-8,7,-3,5,2,-1,7,6,-10,3,8,-2,7,10,5,-5,-7,4,-1,-2,-8,-6,2,-7,9,-6,7,10,1,5,-5,10,1,4,10,-7,-8,-5,2,-5,-4,-2,9,7,9,8,10,-8,2,5,7,-4,4,5,3,-9,-3,8,-2,-1,-6,-4,9,-9,3,4,-7,-3,10,-9,2,-10,8,4,-2,10,6,-6,8,-5,-1,-9,9,-3,3,-2,9,-7,-1,-6,8,10,-2,6,-2,-8,-1,-5,-2,1,-8,8,6,-4,-8,9,8,7,-6,9,5,-2,6,-9,6,4,5,-3,9,6,-10,3,-4,10,-5,-7,8,-1,9,-3,-9,10,8,3,-1,-7,3,2,2,7,-1,-10,-6,-5,10,-9,-6,-3,4,-4,-6,-7,10,-8,1,10,10,3,10,10,-8,10,-1,8,8,10,2,-5,-9,5,-8,2,-6,5,-4,7,-7,-6,8,2,8,4,-3,4,-1,2,5,-9,-10,6,-9,-6,8,5,-5,-5,-10,5,-7,-3,-10,-10,-10,4,1,-4,3,-9,1,10,-10,9,4,-3,-2,9,-3,7,-8,-3,-2,-1,6,-7,-1,-1,2,3,3,-6,6,9,4,5,8,1,5,-7,2,-6,-1,-6,-8,-8,8,-7,9,4,-1,-7,6,-9,10,2,9,6,4,4,2,-2,-8,-3,-5,2,9,-7,9,-8,1,2,-7,-4,10,-4,10,1,6,-6,-4,-9,10,-9,-3,10,4,-5,-10,-1,-7,-3,10,-6,1,-9,2,9,5,3,-3,-1,-6,-10,-3,9,6,6,7,4,4,4,-3,-10,-10,-4,7,-2,10,-3,4,5,-3,8,5,-1,-7,-6,7,7,-10,-4,6,4,-9,1,9,3,-8,-4,-5,3,10,-2,-7,8,-10,6,8,4,-5,9,2,5,-5,3,6,1,7,-4,-2,10,5,-2,6,-8,-10,4,-1,3,2,5,4,-5,-1,3,-3,9,-1,-1,-6,7,-8,-7,-3,-6,-6,4,-8,9,10,-5,7,1,3,-4,-10,5,3,8,4,-1,-6,-10,-4,6,-5,8,-2,-9,-2,-6,-3,2,-6,-1,6,-1,-9,-9,-4,-8,5,-10,-9,-6,1,5,4,1,10,10,-6,-10,-4,7,-5,8,2,-9,-6,-2,-8,2,-4,1,4,2,2,4,-5,5,-5,2,-10,10,7,-2,1,-6,-6,-1,-8,-10,-6,-8,5,-1,-8,-10,3,4,-4,-4,2,-9,6,-1,-10,-7,-7,-7,10,-3,-10,-9,-4,4,3,10,7,6,-9,8,-9,-6,-1,9,3,-2,-6,8,7,-8,2,-8,7,-4,2,-6,6,9,6,-9,-1,-2,5,9,-3,-4,2,6,7,-6,2,2,-5,-5,9,2,8,-9,5,5,-4,3,-1,7,-8,7,-8,-8,-7,6,1,-8,-3,2,-6,5,5,7,-8,-4,-9,6,7,2,9,10,7,8,8,9,-6,3,6,-9,-6,1,-1,5,-1,2,7,9,-3,-6,-9,-4,-3,8,8,-4,-8,2,-3,9,-5,5,4,-8,3,7,-10,6,-9,3,-10,4,3,1,-4,-10,-1,3,-9,4,4,3,-4,9,3,-1,-10,-5,2,9,-4,6,-3,3,-9,-7,10,-1,1,8,-4,9,5,-7,9,2,4,-1,7,1,2,-1,8,-7,-1,-4,-3,9,6,4,3,-1,3,5,7,-8,-6,3,10,-4,6,-6,-1,-6,4,-4,-7,-5,6,-2,10,6,-10,1,-1,-1,-4,-8,3,-4,6,-3,1,-3,9,-4,7,6,-10,-7,3,10,6,-4,3,-5,4,-10,-7,-5,-10,7,10,-5,2,3,-2,5,-10,7,7,-2,2,-7,5,-9,-3,-2,-2,5,-1,-1,1,10,-5,7,-9,-2,-1,1,-2,-2,-9,-10,-1,4,3,-4,-1,8,-1,7,-3,2,9,3,6,-8,10,-7,-5,5,-6,2,5,-5,-6,6,-3,-5,-4,6,4,6,-4,-8,-3,6,-4,-9,10,-5,6,8,-2,2,3,-5,-3,-2,-3,5,3,-7,10,8,-2,8,4,7,-1,9,8,1,-6,-10,3,-5,7,-7,-10,8,-6,9,-2,-6,-7,7,1,-9,-2,6,-2,-6,-4,7,8,5,-2,5,-1,9,8,-3,7,-9,-9,-4,7,2,-5,-7,-4,6,-7,2,-4,3,-10,-4,-8,-3,8,-10,1,8,10,-6,10,-10,5,-4,-6,2,5,2,8,2,7,3,-5,4,8,2,6,-4,8,1,-7,2,10,7,1,6,-3,-6,1,8,1,-9,3,-7,3,5,-2,10,-10,2,6,9,-6,-2,8,6,9,6,9,3,5,10,6,1,-8,-7,-8,8,5,1,-9,3,-4,-1,6,7,-5,-9,8,7,1,-2,2,5,9,9,6,-7,-2,-3,4,10,-6,8,-6,-4,1,-8,-6,-10,-2,5,2,-8,10,-5,-3,2,3,-7,-7,8,7,-10,-2,9,9,1,6,8,-5,8,7,9,-2,-8,7,6,3,-6,4,8,1,-7,-1,3,-9,3,-3,-5,-9,5,-9,10,4,-7,-3,-6,-4,-5,9,10,1,5,8,-2,-4,-2,5,-5,10,-9,-6,-1,-9,5,4,-9,1,-10,3,5,-6,-2,-1,-2,-10,-3,-8,-7,9,-7,9,8,10,-10,-10,10,-2,-9,-9,3,1,-6,-10,-8,-8,4,10,9,1,-1,-4,9,5,-10,-8,-6,9,-10,6,2,2,1,-9,10,-10,3,5,-10,9,-7,-3,5,-4,2,2,5,-9,6,7,-8,-8,-10,2,-3,2,-7,10,6,9,-5,-10,-7,-7,7,-8,10,5,-6,2,7,9,8,5,5,-1,-7,3,2,-6,5,-5,7,-6,8,-4,3,-8,-5,6,9,4,-10,7,-6,-2,-6,-7,8,7,3,-10,9,1,1,5,7,-5,4,-9,-6,5,-10,4,-6,-4,6,-9,-2,-8,8,-2,-1,-1,8,9,-1,-5,-7,-10,1,3,-8,2,-3,-4,2,-7,2,7,-8,-5,1,3,-8,-10,-5,-6,-5,4,7,-10,-3,-9,7,-4,-6,-7,6,4,10,-2,-7,9,-5,10,10,-10,-9,7,-8,-2,-9,-1,6,10,-9,3,1,10,7,-9,-1,2,-7,-7,-10,-9,-7,-8,4,-1,2,-1,-7,2,-2,-3,-9,3,3,-1,9,4,10,9,1,9,3,10,-2,4,-3,-6,-9,8,-1,7,-9,-5,4,-3,5,2,-3,-6,5,6,6,-8,-3,6,-5,3,5,-3,6,-6,9,7,-10,-6,4,1,-5,4,5,-9,5,6,-2,1,-8,-8,-6,-8,9,-1,7,-2,3,10,8,-10,-3,-4,-7,4,-1,2,-7,-4,-6,1,5,6,1,-7,7,-3,4,-7,2,8,-4,-1,-3,-9,-7,2,6,-1,-8,-8,-6,7,-10,-2,-8,6,-5,2,9,6,-2,8,-10,6,7,-3,9,-2,-6,1,-7,5,3,9,-1,-6,7,2,4,5,6,-2,-10,3,-1,2,-1,-9,6,-6,4,3,-7,9,5,-3,-2,7,9,9,-4,7,8,2,5,5,2,-3,3,10,-5,-2,-6,-10,8,-7,10,10,4,-6,-1,-10,-8,-2,4,2,3,-6,-10,-5,6,1,-8,8,6,-2,-4,10,7,5,-1,1,-9,-2,5,-9,3,-9,-4,4,-10,5,-1,5,6,-1,5,3,-1,6,4,7,5,8,-2,9,1,3,10,1,-8,-5,8,-8,4,-5,7,-8,7,-4,-10,-10,-9,-4,2,7,10,2,1,-7,2,-3,-3,5,-7,-2,2,-10,6,9,9,-8,9,9,10,3,7,2,7,3,-6,10,6,10,4,-1,-7,-4,-3,-4,-6,-6,3,4,-5,3,-1,-3,5,-10,-7,3,-4,-10,-7,-9,-3,7,-4,7,7,3,7,6,3,2,-1,-4,10,-3,2,2,-8,3,-10,-1,4,-9,-4,-2,3,5,-7,-10,-4,-5,-6,2,-6,5,-9,6,-2,4,-2,-3,2,-10,6,7,-4,6,9,-1,5,4,-4,-9,7,-2,-10,3,-2,3,4,8,2,5,4,-8,-4,4,5,4,-7,-1,1,10,-9,-3,-3,-9,7,-8,-2,1,-1,3,8,-7,6,-3,2,-2,6,-3,8,-4,8,5,8,-7,1,-4,9,-6,-1,-4,4,-5,-3,1,-2,6,7,-9,5,6,8,-5,-3,-2,1,9,-5,-8,-5,-10,4,-5,7,-5,-2,8,-3,4,5,-2,5,-2,8,-9,-6,9,6,10,10,6,8,-9,-7,7,-3,8,2,6,-9,4,3,7,7,-3,-5,-8,-10,-6,-2,-1,-3,10,-9,7,1,-5,-5,6,-2,-1,-5,-1,-6,4,-9,-2,3,10,-8,2,-8,-8,9,-7,10,-9,-6,3,-9,-1,-3,-5,-5,-8,1,4,7,4,-5,-9,10,-1,-2,10,3,-4,-4,-1,-1,4,1,3,10,-5,10,-2,-4,1,-7,-1,-4,-7,3,9,-8,-8,-1,-8,8,-7,-7,-3,2,-1,6,-1,7,1,5,4,5,4,-10,-8,-6,-9,4,8,-7,-6,10,-5,5,-5,-10,-6,10,8,4,10,-2,7,-2,-3,3,-4,-9,10,-9,-6,5,-1,-4,6,-6,2,-7,6,-3,10,2,-10,5,5,-8,-2,-3,-9,1,-8,2,-6,8,-8,-3,-8,-4,-6,-2,-2,1,3,-6,-2,-8,5,10,-8,-3,1,7,-3,-2,10,9,4,8,8,10,1,2,-9,-7,-3,3,8,-5,-1,-9,9,-2,2,10,4,-9,1,10,4,-7,8,10,2,-5,2,-3,-4,6,5,-3,8,-3,-5,-9,10,7,7,-2,-3,-9,4,8,7,3,9,-2,-10,-6,-7,6,-10,-5,-2,-6,-5,10,9,7,-1,9,-8,9,-5,5,-1,-9,-5,9,-3,-2,10,-10,-9,6,-9,2,-3,3,5,9,-8,8,-5,1,-2,8,5,2,7,6,10,-1,-8,-10,-2,-8,7,6,-2,10,7,7,-6,-6,4,6,9,-6,2,9,-3,8,4,2,10,2,-7,-9,-8,5,8,-8,9,-3,10,-6,-10,4,8,-4,7,-6,-4,9,-4,6,6,-9,7,-5,-6,9,3,4,1,-10,3,-3,2,1,-6,8,-10,-4,-10,4,-10,-4,8,6,5,6,-3,4,-2,-1,-3,-8,-7,8,3,-3,-6,-8,6,-4,10,-6,-10,8,7,-10,-10,1,-5,5,2,-3,-7,-3,-4,4,6,9,-10,9,8,-8,-10,-6,-2,2,-10,-4,-5,10,5,-5,3,8,3,-3,-9,-1,-3,-1,-9,1,-6,-4,4,-2,7,-10,3,4,-7,1,9,4,-1,7,8,7,2,6,-7,-5,-8,-7,-4,9,9,9,1,7,8,2,-1,9,4,9,4,8,-8,-4,-5,6,-4,1,6,-9,-4,-10,2,8,7,-7,-3,4,1,6,1,-9,6,-10,10,9,-10,8,-8,-6,-6,-7,-10,-2,9,7,9,2,-8,10,-2,9,-7,2,5,-2,2,10,10,-1,2,-8,-5,-8,3,-8,-6,8,6,-1,-7,2,4,-1,5,-3,1,-10,2,-1,6,3,-8,7,1,5,-3,-9,-10,-3,-4,4,10,4,-1,-10,-6,-1,3,10,-8,-4,-3,-9,-3,10,9,-5,-7,2,5,7,4,-8,7,-3,-3,5,-7,-9,-7,10,-2,-6,5,8,-1,-1,-4,3,5,6,10,5,6,-2,4,10,6,-6,-5,10,1,2,-10,-7,-1,-4,2,10,3,2,3,-3,9,9,6,-9,-1,-2,-6,-8,2,7,3,-4,9,-4,-10,-3,-10,1,4,-3,-1,-7,-4,3,9,9,-7,-8,1,-1,3,-7,10,9,10,-10,8,7,4,-7,-7,-7,-3,3,1,2], dtype = "uint64")#candidate|5424|(2816,)|const|uint64
call_5422 = relay.TupleGetItem(func_2154_call(relay.reshape(const_5423.astype('int16'), [154,]), relay.reshape(const_5424.astype('uint64'), [2816,]), ), 3)
call_5425 = relay.TupleGetItem(func_2158_call(relay.reshape(const_5423.astype('int16'), [154,]), relay.reshape(const_5424.astype('uint64'), [2816,]), ), 3)
output = relay.Tuple([bop_5415,call_5422,const_5423,const_5424,])
output2 = relay.Tuple([bop_5418,call_5425,const_5423,const_5424,])
func_5428 = relay.Function([], output)
mod['func_5428'] = func_5428
mod = relay.transform.InferType()(mod)
mutated_mod['func_5428'] = func_5428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5428_call = mutated_mod.get_global_var('func_5428')
call_5429 = func_5428_call()
output = call_5429
func_5430 = relay.Function([], output)
mutated_mod['func_5430'] = func_5430
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5442 = relay.const([[[False,False,False,True,False,True,False,False,True,False,False,False,True,False,True,False],[True,True,True,False,True,False,False,False,True,False,False,True,False,True,True,False],[True,True,True,True,False,False,False,False,False,False,False,True,False,False,True,True],[True,True,False,False,True,False,True,False,False,True,True,False,False,False,False,True],[True,False,True,True,False,True,True,False,True,False,False,False,False,True,True,True],[False,True,True,True,True,False,True,True,True,False,True,True,False,False,True,True],[False,False,True,False,True,False,False,False,False,False,False,False,False,False,True,False]],[[True,True,False,True,True,True,False,True,False,False,False,False,False,True,False,False],[True,True,False,False,True,False,True,False,True,True,False,True,True,False,True,True],[True,True,False,False,True,False,True,True,False,False,True,False,True,True,False,True],[False,False,True,False,True,False,False,False,False,False,True,True,False,False,False,True],[False,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True],[True,True,True,False,False,True,False,False,False,True,True,False,True,False,False,True],[False,False,False,True,True,False,True,True,False,True,False,True,True,False,False,False]],[[True,False,False,True,True,False,True,True,True,True,False,True,True,False,False,True],[False,True,True,True,True,False,False,True,True,False,False,False,False,True,True,False],[True,True,True,False,False,True,False,True,False,False,False,True,False,True,False,False],[False,True,True,True,True,False,True,False,False,True,True,True,False,False,True,True],[True,False,False,True,True,False,True,True,False,True,False,False,False,True,False,False],[False,True,False,False,True,True,False,False,False,True,True,True,True,False,False,True],[False,False,False,False,False,True,True,False,True,False,False,True,True,False,False,True]],[[False,False,True,True,True,False,True,True,True,False,False,True,False,True,False,True],[True,False,True,False,False,False,False,True,False,True,False,True,True,False,True,True],[False,False,True,True,False,False,True,False,True,True,True,True,False,True,False,False],[True,True,False,True,False,False,False,False,True,True,False,True,True,True,False,False],[True,True,True,False,False,False,False,True,False,True,False,False,False,True,False,True],[False,False,True,False,True,True,True,False,False,True,True,False,False,False,False,True],[True,True,True,True,False,True,False,False,False,True,False,False,False,True,False,False]],[[True,True,True,False,False,False,True,True,True,False,True,True,False,True,False,False],[False,False,True,False,True,False,False,False,True,True,False,True,False,False,True,True],[True,False,False,False,False,True,True,True,True,False,False,False,True,True,False,True],[True,True,False,False,True,False,False,False,True,True,True,True,True,True,True,True],[True,True,True,False,False,False,True,True,False,False,True,True,True,True,False,False],[True,False,False,False,True,True,True,False,False,False,False,True,True,True,False,True],[False,True,True,False,True,False,True,True,False,True,False,True,False,True,True,True]]], dtype = "bool")#candidate|5442|(5, 7, 16)|const|bool
var_5443 = relay.var("var_5443", dtype = "bool", shape = (5, 7, 16))#candidate|5443|(5, 7, 16)|var|bool
bop_5444 = relay.logical_and(const_5442.astype('bool'), relay.reshape(var_5443.astype('bool'), relay.shape_of(const_5442))) # shape=(5, 7, 16)
func_627_call = mod.get_global_var('func_627')
func_630_call = mutated_mod.get_global_var('func_630')
var_5456 = relay.var("var_5456", dtype = "float64", shape = (224,))#candidate|5456|(224,)|var|float64
call_5455 = relay.TupleGetItem(func_627_call(relay.reshape(var_5456.astype('float64'), [14, 2, 8])), 0)
call_5457 = relay.TupleGetItem(func_630_call(relay.reshape(var_5456.astype('float64'), [14, 2, 8])), 0)
func_721_call = mod.get_global_var('func_721')
func_722_call = mutated_mod.get_global_var('func_722')
call_5464 = relay.TupleGetItem(func_721_call(), 2)
call_5465 = relay.TupleGetItem(func_722_call(), 2)
uop_5492 = relay.cosh(const_5442.astype('float32')) # shape=(5, 7, 16)
func_4527_call = mod.get_global_var('func_4527')
func_4528_call = mutated_mod.get_global_var('func_4528')
call_5495 = relay.TupleGetItem(func_4527_call(), 3)
call_5496 = relay.TupleGetItem(func_4528_call(), 3)
func_171_call = mod.get_global_var('func_171')
func_173_call = mutated_mod.get_global_var('func_173')
call_5502 = relay.TupleGetItem(func_171_call(), 2)
call_5503 = relay.TupleGetItem(func_173_call(), 2)
uop_5505 = relay.log(uop_5492.astype('float32')) # shape=(5, 7, 16)
bop_5513 = relay.less(uop_5505.astype('bool'), relay.reshape(bop_5444.astype('bool'), relay.shape_of(uop_5505))) # shape=(5, 7, 16)
output = relay.Tuple([call_5455,var_5456,call_5464,call_5495,call_5502,bop_5513,])
output2 = relay.Tuple([call_5457,var_5456,call_5465,call_5496,call_5503,bop_5513,])
func_5522 = relay.Function([var_5443,var_5456,], output)
mod['func_5522'] = func_5522
mod = relay.transform.InferType()(mod)
var_5523 = relay.var("var_5523", dtype = "bool", shape = (5, 7, 16))#candidate|5523|(5, 7, 16)|var|bool
var_5524 = relay.var("var_5524", dtype = "float64", shape = (224,))#candidate|5524|(224,)|var|float64
output = func_5522(var_5523,var_5524,)
func_5525 = relay.Function([var_5523,var_5524,], output)
mutated_mod['func_5525'] = func_5525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2342_call = mod.get_global_var('func_2342')
func_2343_call = mutated_mod.get_global_var('func_2343')
call_5539 = relay.TupleGetItem(func_2342_call(), 0)
call_5540 = relay.TupleGetItem(func_2343_call(), 0)
func_2854_call = mod.get_global_var('func_2854')
func_2855_call = mutated_mod.get_global_var('func_2855')
call_5550 = relay.TupleGetItem(func_2854_call(), 1)
call_5551 = relay.TupleGetItem(func_2855_call(), 1)
output = relay.Tuple([call_5539,call_5550,])
output2 = relay.Tuple([call_5540,call_5551,])
func_5560 = relay.Function([], output)
mod['func_5560'] = func_5560
mod = relay.transform.InferType()(mod)
mutated_mod['func_5560'] = func_5560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5560_call = mutated_mod.get_global_var('func_5560')
call_5561 = func_5560_call()
output = call_5561
func_5562 = relay.Function([], output)
mutated_mod['func_5562'] = func_5562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1037_call = mod.get_global_var('func_1037')
func_1039_call = mutated_mod.get_global_var('func_1039')
call_5597 = func_1037_call()
call_5598 = func_1037_call()
output = relay.Tuple([call_5597,])
output2 = relay.Tuple([call_5598,])
func_5611 = relay.Function([], output)
mod['func_5611'] = func_5611
mod = relay.transform.InferType()(mod)
output = func_5611()
func_5612 = relay.Function([], output)
mutated_mod['func_5612'] = func_5612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3065_call = mod.get_global_var('func_3065')
func_3067_call = mutated_mod.get_global_var('func_3067')
call_5636 = relay.TupleGetItem(func_3065_call(), 0)
call_5637 = relay.TupleGetItem(func_3067_call(), 0)
func_4832_call = mod.get_global_var('func_4832')
func_4835_call = mutated_mod.get_global_var('func_4835')
var_5659 = relay.var("var_5659", dtype = "bool", shape = (1, 280))#candidate|5659|(1, 280)|var|bool
call_5658 = relay.TupleGetItem(func_4832_call(relay.reshape(var_5659.astype('bool'), [7, 10, 4]), relay.reshape(var_5659.astype('bool'), [7, 10, 4]), ), 3)
call_5660 = relay.TupleGetItem(func_4835_call(relay.reshape(var_5659.astype('bool'), [7, 10, 4]), relay.reshape(var_5659.astype('bool'), [7, 10, 4]), ), 3)
output = relay.Tuple([call_5636,call_5658,var_5659,])
output2 = relay.Tuple([call_5637,call_5660,var_5659,])
func_5667 = relay.Function([var_5659,], output)
mod['func_5667'] = func_5667
mod = relay.transform.InferType()(mod)
var_5668 = relay.var("var_5668", dtype = "bool", shape = (1, 280))#candidate|5668|(1, 280)|var|bool
output = func_5667(var_5668)
func_5669 = relay.Function([var_5668], output)
mutated_mod['func_5669'] = func_5669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2092_call = mod.get_global_var('func_2092')
func_2093_call = mutated_mod.get_global_var('func_2093')
call_5752 = func_2092_call()
call_5753 = func_2092_call()
const_5754 = relay.const([[[7.366823,-1.555488,-8.794311,-8.936758,4.732578,4.152313,2.754037,-1.446995],[9.840066,9.555689,-2.084700,-3.338899,6.267728,-6.265819,1.902639,-5.910035]],[[7.151958,9.008241,-0.115358,-4.649835,-1.666530,-5.026609,1.959478,-0.345944],[-0.800274,0.006264,0.480383,9.856944,2.221476,-4.371055,4.669057,7.159600]],[[9.252591,8.285822,-2.343676,-6.130420,7.136229,3.860751,3.743708,3.950577],[2.648557,8.988322,-3.851739,-0.820172,-8.760717,-5.223527,7.515578,7.000432]],[[9.332027,-6.388340,-8.862236,-3.355562,-4.041564,-3.015579,8.022442,4.192077],[5.709918,7.985002,-1.454556,4.645011,2.814602,-5.379848,2.145886,7.660191]],[[-3.656640,-5.513596,-2.959245,-9.713122,-4.565724,5.960950,0.804518,7.932836],[6.607300,-9.148119,-1.151957,-9.495832,-2.804142,-2.232021,-3.056465,-7.391774]],[[-6.190417,0.746832,4.915672,5.183700,1.945551,-8.272751,8.442629,0.665731],[-4.612773,-1.907041,8.873042,-4.380492,-2.169143,8.878785,7.135019,6.834339]],[[-5.389141,-2.588231,0.239584,-5.402817,-2.392351,6.274726,-7.944479,-8.087690],[-9.484501,3.769620,-1.555813,2.246053,-2.118292,6.045014,-8.855051,8.442451]],[[-5.775381,0.501685,8.914066,-9.835175,-0.507308,-7.507352,-9.248468,7.636690],[4.101860,-3.903744,1.530602,-9.692589,-7.623786,7.089086,6.579646,3.263373]],[[-1.478978,5.847188,-0.670960,-0.347944,7.826121,1.477321,4.281338,-6.666350],[8.671087,-8.885746,6.488046,8.032007,6.845444,-7.017031,7.583408,-3.959900]],[[-5.086377,-2.037069,3.323857,6.545446,1.653853,-7.027527,-3.557181,1.519921],[6.760573,-6.409426,1.903211,-8.558115,-7.944254,0.904199,-1.454702,0.858941]],[[6.123818,-1.708588,-8.937820,5.769350,-4.796052,9.839294,-6.699968,2.393057],[-0.184533,-9.471443,7.615637,-5.237323,-1.926336,2.290055,8.497881,5.177336]],[[-0.808967,2.320982,-6.702715,-5.796272,-5.894946,9.974747,9.957431,-2.253890],[-2.173923,2.014137,4.342052,6.123922,5.756165,8.613032,4.991343,6.015630]],[[-2.987538,8.103590,1.682972,7.979182,5.135378,-3.667111,6.449845,-7.280281],[-0.290201,6.079097,-9.474360,1.782534,-1.549054,-9.513666,4.797397,6.780860]],[[3.116693,-0.070650,8.917429,-5.530674,-9.373857,0.698185,-2.009716,7.547560],[8.314118,-6.789538,0.935805,4.041603,-9.806598,-8.326047,8.573171,8.656999]]], dtype = "float64")#candidate|5754|(14, 2, 8)|const|float64
bop_5755 = relay.power(call_5752.astype('float32'), relay.reshape(const_5754.astype('float32'), relay.shape_of(call_5752))) # shape=(14, 2, 8)
bop_5758 = relay.power(call_5753.astype('float32'), relay.reshape(const_5754.astype('float32'), relay.shape_of(call_5753))) # shape=(14, 2, 8)
output = relay.Tuple([bop_5755,])
output2 = relay.Tuple([bop_5758,])
func_5759 = relay.Function([], output)
mod['func_5759'] = func_5759
mod = relay.transform.InferType()(mod)
output = func_5759()
func_5760 = relay.Function([], output)
mutated_mod['func_5760'] = func_5760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3065_call = mod.get_global_var('func_3065')
func_3067_call = mutated_mod.get_global_var('func_3067')
call_5823 = relay.TupleGetItem(func_3065_call(), 1)
call_5824 = relay.TupleGetItem(func_3067_call(), 1)
func_2528_call = mod.get_global_var('func_2528')
func_2532_call = mutated_mod.get_global_var('func_2532')
const_5826 = relay.const([-6,-3,8,-1,-4,4,-6,10,10,-8,-9,5,-1,-4,4,10,-2,8,2,-8,-4,2,1,-9,-3,1,5,5,9,-1,-9,-5,-4,2,-6,4,5,1,-9,7,5,-6,-4,-8,-10,-7,10,1,9,-1,6,-7,1,-6,-8,2,1,-6,9,-7,5,-8,-6,-10,-2,9,6,8,-4,6,7,5,-8,-4,-7,3,-5,-8,10,7,10,-10,2,4,4,5,-9,-1,1,1,-4,-9,-7,-1,6,-1,-4,3,-10,-9,6,-6,-6,2,-2,-5,-9,-7,-3,5,6,6,-8,-5,5,-3,-2,7,-7,5,-4,-8,-7,1,-3,7,-10,-1,-1,7,2,8,2,-10,-4,8,7,3,1,2,-10,-5,-4,-1,3,-1,-9,-7,-2,-9,3,-8,-5,4], dtype = "int16")#candidate|5826|(154,)|const|int16
const_5827 = relay.const([-2,-7,-7,3,5,7,3,3,-8,8,-5,7,3,4,-8,5,6,-8,4,3,9,5,6,1,-7,1,4,-3,10,6,8,1,-5,1,10,3,1,-1,-8,-1,5,-6,10,6,7,-1,5,-3,8,-2,-5,8,-2,5,1,-6,-7,-5,-2,-8,-5,5,10,-10,1,9,-8,-4,-5,-2,-4,-5,1,-2,1,3,1,-5,6,-3,7,3,-8,6,5,-10,-8,-3,-4,-3,5,2,6,8,3,8,-3,5,-9,3,-1,-4,9,-10,-10,-10,1,-10,-9,8,10,-2,-1,2,-10,-2,1,9,-3,3,-4,-8,-6,3,-9,-7,-10,-1,8,9,-2,8,-8,3,8,3,-10,-10,-9,2,-5,-8,2,4,-5,-9,-5,-2,5,-2,-1,8,6,-10,10,-7,-4,10,4,-7,8,-8,2,5,5,-2,-4,10,6,-9,1,-3,-8,-1,8,3,-2,2,3,3,7,-4,6,3,3,10,5,-7,8,-9,-5,-4,-5,3,6,-8,3,-3,8,-1,-7,3,6,-7,9,1,-10,1,3,-5,-1,-1,-7,-3,2,3,9,-1,7,9,6,10,-7,3,-6,-1,3,3,-8,-4,4,-2,-5,-8,-3,-10,9,8,2,7,2,-9,2,9,-10,-2,10,7,-7,10,4,-2,10,8,-1,-4,-3,-10,-4,-6,-1,1,4,-9,-5,-2,8,1,-2,-2,3,6,8,2,-6,-10,-1,-10,-1,6,7,6,-10,5,-5,6,4,6,1,-6,8,-6,9,4,5,7,-7,-9,-9,2,-1,1,-2,7,-5,-10,1,4,2,-1,7,10,2,-3,-4,-6,-3,10,4,-7,-2,-5,-5,-6,-6,-3,-4,9,2,6,6,3,-9,-5,10,-5,10,-9,9,-1,10,-10,-9,-2,-2,9,2,-9,4,-5,7,9,2,-4,3,7,-1,10,7,-3,4,-9,3,-7,-2,-1,6,6,-10,-8,6,-6,2,9,2,10,-5,2,7,-6,4,7,9,-8,4,2,1,8,-6,7,-2,-3,6,-8,-5,-1,4,-10,9,-2,6,-4,-3,-2,-3,6,6,4,-5,4,-9,-10,2,5,-8,6,-4,2,-5,4,-5,-3,2,-4,2,-8,2,-1,7,-8,7,-10,-4,-6,-7,7,5,-3,-7,-3,-3,-7,8,-3,-8,-2,5,-5,2,-8,-6,-9,4,7,6,-10,2,8,-9,-4,2,-3,-6,7,-4,7,1,8,-5,-7,-6,2,8,7,-8,4,7,-8,8,2,-2,1,-4,-9,3,-10,4,-6,-9,-10,3,1,-3,-4,-4,-4,-5,8,-3,8,4,4,9,2,2,7,8,-5,6,-2,6,-5,-9,10,-3,-10,6,6,-6,3,2,1,-9,1,-6,4,-8,-2,-5,1,-1,-6,6,2,2,-8,-7,-4,-7,-2,7,4,-6,-4,-1,10,7,10,-7,5,-2,-4,6,-7,-3,8,4,7,8,-4,10,2,-9,-3,7,-6,3,-9,-9,1,-3,4,-1,-1,4,-10,9,-2,-4,-5,-10,-1,-4,-3,-7,9,-3,9,-3,5,-6,-2,6,-3,6,3,-10,1,5,9,8,1,-10,-7,3,-2,8,-3,-5,-5,6,-9,2,-4,-5,8,10,7,10,-5,-10,1,9,10,-2,-7,5,-9,-9,4,6,9,9,-8,-4,3,9,9,8,4,-6,-2,-10,-8,4,2,3,-7,-9,-3,-7,-4,10,6,5,-10,2,4,3,-2,-5,8,-6,-2,10,-8,4,7,7,2,3,7,-1,9,4,-10,6,8,-3,-10,6,3,-10,-3,-4,-1,4,4,8,1,7,-2,1,8,10,8,6,5,-2,2,-3,2,-10,5,4,-3,-9,-5,-7,-4,-10,3,4,1,8,1,-8,-9,1,-10,1,-5,10,-1,-2,-2,-7,-8,4,-8,-3,-2,-4,-1,4,-10,-5,-5,5,-10,3,9,8,5,-7,4,2,2,8,10,7,9,7,6,4,-8,9,-8,-9,1,-6,7,-3,-3,-6,-7,7,2,-3,-5,-4,3,4,-10,-2,8,-8,-5,8,3,5,5,-7,-3,5,7,-2,-5,-10,9,6,2,-4,4,-7,6,-9,1,7,-8,3,-6,-6,1,-3,-9,-8,4,10,-6,5,8,-2,-1,6,-3,-5,-5,-7,-8,-9,-1,10,10,3,8,7,-5,-6,8,-8,-2,-2,-5,-3,1,-1,-10,-10,-2,6,5,7,-2,6,6,3,-6,-5,5,-5,-10,3,-7,10,-9,9,-2,2,9,6,-2,3,5,1,6,8,-10,7,5,-7,4,8,2,9,-8,7,5,9,8,10,6,1,1,5,7,-2,-10,6,8,5,2,7,-4,7,-6,7,5,8,-9,-3,7,-7,4,8,1,-10,-5,-2,1,2,-4,-9,-10,8,2,-4,-7,-5,-6,-6,8,2,3,2,-1,3,-5,8,-9,-3,-8,-9,9,7,-9,-2,9,10,-8,-7,-9,6,-3,1,1,-5,2,3,10,-5,-4,-7,1,-6,2,-7,6,-6,8,-2,-1,7,5,-5,1,-5,6,-10,9,-5,-1,-1,8,5,5,6,-8,-9,4,-7,3,1,-4,-8,7,4,-8,5,2,-1,-1,3,1,-10,6,-9,9,-10,-3,8,2,9,6,-5,8,-5,4,-8,-10,9,8,-4,-1,2,3,-3,-9,-4,-6,5,-6,3,-10,6,-1,-7,6,-6,8,-9,7,5,-4,-2,1,-6,-10,8,2,-2,-10,4,10,10,-7,6,-3,-1,-3,7,2,8,4,2,9,-1,-2,-4,-4,-8,-3,4,-7,-3,7,4,-5,1,-10,7,8,-8,-2,1,-7,6,5,-8,-6,3,-2,5,1,9,1,-3,-6,9,3,4,1,2,2,8,-2,3,10,-3,6,-4,-10,5,-8,-3,-4,-3,-7,-1,-4,6,10,9,-9,-2,-4,9,-1,-1,-1,-2,-1,2,-7,-8,-1,-8,-6,-2,-9,8,-1,9,-5,3,-5,1,-9,6,7,8,8,1,-4,7,-9,9,5,-4,-10,-6,-3,3,-1,7,-2,-4,-10,4,-7,-7,9,-6,8,5,-8,-5,10,-10,-10,9,-1,-2,-7,5,7,-2,-2,1,10,-7,8,9,3,-9,8,5,-10,-10,-3,-4,-9,-7,7,-10,-7,-7,-3,3,8,9,1,-5,10,1,-2,-4,-3,1,-2,-7,10,-1,10,10,-9,4,-2,-2,-4,-6,8,-7,-2,1,1,-10,-1,5,9,9,-2,-10,2,9,-5,-10,4,3,6,-9,-1,-10,-3,6,-8,-2,10,7,1,7,10,10,5,-9,7,-9,-10,-3,-4,5,-3,-4,-8,-4,6,7,-9,9,10,6,-7,-6,-4,10,-5,9,3,-3,-2,-9,8,-4,3,-10,1,-10,1,-5,-2,-2,-1,9,4,-4,8,-7,-1,3,4,9,-1,6,-5,-8,8,-6,-1,-3,-8,1,10,4,1,-5,3,2,3,6,1,-4,6,-9,6,1,-1,-10,2,-2,9,10,3,8,2,-3,9,-5,7,1,-8,-5,-7,-9,9,4,1,2,7,-10,-3,3,10,7,2,1,10,-8,-1,8,10,-7,-7,5,-8,-5,9,7,8,5,1,1,-1,2,7,3,-5,8,-1,8,-7,-4,-2,6,-4,1,6,-1,-10,1,5,5,-6,2,6,-9,-2,1,-4,6,-7,-5,7,-10,-1,8,-6,-5,-6,10,-6,6,1,-4,4,5,4,-4,8,-2,6,-6,-3,-5,-8,2,3,4,5,9,9,-3,-3,-6,5,-1,-9,5,8,10,4,-9,-2,-9,2,-8,-1,4,2,-7,9,7,-5,-10,2,-8,-4,1,10,2,-7,3,-5,-2,-8,-1,-6,-6,1,-5,-8,9,-2,9,-8,5,3,-3,-4,5,-5,10,-7,6,2,10,6,3,10,1,-3,5,-4,-6,5,-4,-8,-2,9,-2,9,3,3,-5,-6,-1,3,-6,-4,7,4,10,6,-6,1,-7,9,-8,-4,5,9,10,2,9,8,7,-7,-3,-10,7,-4,4,4,8,-4,9,-7,-5,5,-6,8,-5,10,-10,-5,-4,3,6,1,-5,-5,10,3,2,7,-3,3,4,5,6,10,3,-7,1,1,4,-2,9,-10,-7,10,4,7,-9,-1,-6,-2,-6,-6,-8,5,-4,-8,6,5,-5,-1,-10,-8,-3,-1,-1,8,5,-4,-2,7,-8,8,-3,5,-9,8,7,8,4,-8,4,10,-9,-4,-5,-6,8,-5,6,8,8,-3,-1,-6,-10,-7,10,6,4,-10,-3,-10,-10,-1,-8,-10,-6,-3,5,1,4,4,7,-5,9,10,4,2,-6,10,1,-10,6,3,3,-1,-4,-2,4,-4,7,-5,-3,-6,-10,-4,-8,-10,-8,-8,-9,-9,-3,-7,-10,-9,4,-9,3,-9,4,5,-8,8,10,-10,-6,-3,9,3,-1,-6,6,-6,-1,-3,-8,6,-3,-5,-2,-3,3,-7,-6,-2,3,-3,-3,10,-6,10,-1,-2,-3,-9,-2,-3,-6,7,-1,10,9,4,4,8,7,4,4,-2,4,4,-2,1,9,2,9,5,7,9,-3,9,-5,-6,10,-8,9,-10,-2,9,-1,1,-4,7,6,-1,5,9,-5,-10,2,7,3,2,-10,-5,3,10,-4,9,5,1,1,1,-2,3,1,7,9,9,10,10,-4,3,9,10,-3,3,8,4,-7,7,-6,1,-2,5,-6,7,5,-8,1,10,8,10,9,7,10,3,-6,3,7,-2,-5,5,-9,4,-10,6,10,-5,1,-3,5,6,10,-1,-9,2,-2,-4,9,-10,4,8,-3,1,6,-2,-9,4,10,-6,10,3,-4,-2,-4,-5,-8,2,-7,-5,8,4,8,9,-5,10,-5,-7,9,6,-2,2,4,-3,-9,-6,8,4,-9,-7,-8,-2,-8,-3,-8,2,10,4,-10,-6,9,-7,1,-4,-4,7,-8,8,7,4,-10,9,-10,3,2,-10,1,-8,9,-5,5,-9,-2,-10,8,-6,10,-6,8,2,-9,3,-8,-4,-4,-1,2,1,-7,-5,-5,-3,4,-5,9,6,-10,7,1,6,-2,-8,9,2,-10,-2,6,10,-5,6,-4,1,1,-1,-3,2,8,-2,9,4,1,-6,1,6,-3,-9,5,1,10,-10,3,-8,4,-7,-6,-2,-8,3,-4,-7,-1,6,-6,4,8,-1,-8,1,1,-4,-10,-3,5,-10,-6,10,3,5,-10,7,5,-1,7,6,10,6,-6,-8,6,4,5,9,-7,-7,-5,6,-2,-2,9,-6,8,6,-10,7,-4,-8,-2,-7,1,-7,-8,-6,-10,-1,6,7,-1,6,-9,9,-3,-2,-2,-5,3,-1,6,3,-6,6,-4,-6,6,-6,4,-8,-2,5,9,9,3,-3,9,-7,-10,7,-4,9,-4,6,-2,-8,-7,8,-2,-8,-1,3,6,-5,3,-10,-6,8,6,9,-10,-10,-9,-3,-9,5,3,-8,-10,-7,6,7,-8,1,8,-2,6,-3,2,3,8,-9,-7,-2,-1,-7,6,-8,-10,-10,8,5,4,8,-8,7,-10,9,-7,-4,7,5,7,10,4,-6,-10,8,-10,1,-7,6,-7,7,-3,2,2,5,-3,-7,-5,-1,3,-10,-4,-3,-1,2,-3,4,8,5,-5,9,5,9,6,-6,7,-2,-9,6,3,10,5,-1,1,-4,8,8,-9,5,5,6,7,7,-2,-6,10,-2,-1,9,9,-8,-7,2,3,3,9,2,-7,4,1,-6,-5,10,-1,7,4,-9,-4,-9,10,-5,-3,-7,-5,10,8,-8,6,10,-9,-9,6,6,-1,-7,8,2,-8,-2,7,-8,9,9,-6,-3,7,9,-2,-3,1,7,-1,-1,-5,1,-6,-6,-7,-10,-5,-9,7,-6,-3,5,9,3,9,9,8,6,9,9,-7,10,-2,-6,6,-9,3,3,5,1,2,10,10,-6,-7,4,3,-10,2,7,8,-7,1,-2,-3,-2,5,-7,-7,-5,-7,2,4,9,6,3,2,-6,7,-9,2,-7,5,-1,6,-9,-6,5,3,-7,-9,-4,8,6,-7,-8,-8,6,-9,-6,-5,-10,-5,5,10,-8,10,-2,3,6,4,-9,-8,-6,3,4,6,-3,8,1,-7,6,1,6,5,4,-5,-2,7,10,1,-2,-7,-9,2,-4,7,6,10,-9,-5,6,5,3,-7,6,8,-6,2,3,-3,2,-8,7,-4,7,-1,-9,3,10,6,10,3,-2,-9,-10,-1,2,3,-9,10,-6,9,7,7,1,-5,-9,7,5,6,8,-8,-9,4,7,4,-2,7,6,-9,9,-10,-4,10,2,-3,-3,3,-1,10,8,9,8,1,2,-2,6,9,-6,-7,5,9,2,-10,8,9,3,-7,-8,6,10,10,8,8,-10,-4,-7,-3,-4,2,-10,-9,-10,5,-5,-7,8,3,-9,-10,7,4,-7,-3,-7,-5,5,-3,10,-5,10,2,-3,2,7,1,-7,10,-1,7,7,8,-5,10,-8,2,1,3,-2,-6,-8,5,-3,9,7,5,-7,-9,-3,-10,6,-8,-8,10,8,9,4,-5,-10,-2,-10,2,-1,2,9,-4,5,-9,5,-5,5,2,9,-8,-2,5,-9,-1,-7,2,-6,1,10,-8,-9,-9,6,-6,7,-3,4,10,6,-4,6,-9,4,-6,1,-9,-7,-7,-8,-10,-6,-3,-1,-4,6,-10,-3,7,-10,-4,-8,-1,1,-10,10,-5,10,-7,-3,-10,8,-3,10,10,2,-8,7,7,-7,9,4,-6,-2,-7,-3,-5,-8,3,8,-5,9,3,5,6,-7,-1,-8,7,-9,6,3,2,2,9,-9,2,-10,-6,7,8,8,4,4,8,6,-5,5,-10,1,9,-4,1,-10,-10,10,10,5,6,5,-5,7,-2,7,1,1,-9,-3,-10,9,7,-8,-9,-2,4,-10,2,1,2,-6,-6,-3,4,9,-6,-6,8,-1,-8,-6,4,-5,5,-10,4,8,-3,-8,6,4,4,4,-5,2,9,8,-6,-10,9,-6,6,-4,6,7,-9,-1,-3,6,-3,3,-8,7,-6,-3,-7,-7,-4,3,2,1,2,-4,-8,-5,1,-2,1,-1,6,-1,4,7,10,7,9,5,9,-8,-2,-7,-1,1,10,-8,-7,-1,-8,10,-8,1,-4,-1,-6,1,10,-2,-1,-2,5,7,-6,5,-9,-1,2,4,-8,3,2,3,-4,-4,6,-5,-3,-4,-3,4,-4,8,-6,-1,7,-10,8,2,6,8,-9,4,-5,2,7,-9,2,-6,2,-3,-3,-10,6,-4,8,-4,-5,3,-5,10,-3,-3,-8,3,8,1,-9,-2,-2,7,8,-9,8,-7,-6,-6,-7,2,-10,7,1,7,8,-6,6,10,-3,-9,10,-5,-2,-7,-2,6], dtype = "uint64")#candidate|5827|(2816,)|const|uint64
call_5825 = relay.TupleGetItem(func_2528_call(relay.reshape(const_5826.astype('int16'), [154,]), relay.reshape(const_5827.astype('uint64'), [1, 2816]), ), 0)
call_5828 = relay.TupleGetItem(func_2532_call(relay.reshape(const_5826.astype('int16'), [154,]), relay.reshape(const_5827.astype('uint64'), [1, 2816]), ), 0)
output = relay.Tuple([call_5823,call_5825,const_5826,const_5827,])
output2 = relay.Tuple([call_5824,call_5828,const_5826,const_5827,])
func_5833 = relay.Function([], output)
mod['func_5833'] = func_5833
mod = relay.transform.InferType()(mod)
output = func_5833()
func_5834 = relay.Function([], output)
mutated_mod['func_5834'] = func_5834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3617_call = mod.get_global_var('func_3617')
func_3618_call = mutated_mod.get_global_var('func_3618')
call_5853 = func_3617_call()
call_5854 = func_3617_call()
func_128_call = mod.get_global_var('func_128')
func_131_call = mutated_mod.get_global_var('func_131')
const_5877 = relay.const([4,10,-8,-3,-8,-3,-6,6,-5,-1,-4,-10,-1,-9,6,2,3,9,-8,8,-3,-2,10,-5,6,-7,-8,-7,7,-5,8,-1,9,6,-2,-3,7,-4,-3,3,-4,2,-7,-4,-4,5,8,5,-8,5,5,-5,-5,-9,-7,-8,5,4,8,6,8,-6,-1,-4,-3,-1,6,3,6,-10,8,-3,-9,-5,-6,10,4,10,8,4,-2,-2,-10,10,8,-8,-9,9,9,-4,7,-1,-10,6,-5,-9,-5,3,-7,1,6,-4,-10,2,7,8,-10,4,-10,-9,-1,9,-1,-1,-9,4,10,2,-10,-3,10,4,-2,1,-1,6,9,7,-2,-8,1,-8,-1,2,5,-2,-9,-7,5,3,-8,-7,6,7,-2,-1,-9,5,9,3,5,7,2,-4,-3,2,-6,8,-2,-2,-4,-9,-9,-4,2,-2,-5,-2,4,3,-5,-9,-3,-4,4,1,-8,10,5,-8,1,7,-9,-2,-6,-8,-9,3,4,7,5,7,-10,-1,-10,5,8,-7,2,-10,6,1,-7,-7,4,-10,-4,2,-3,-3,1,4,10,6,3,-2,4,-4,8,1,-5,-10,-9,7,5,-4,-7,-8,2,-9,-10,1,2,4,-7,1,7,5,4,-7,-1,5,-9,-5,7,-3,-4,-10,2,-10,10,-2,-3,-2,-10,-5,-9,-9,5,7,-7,-10,9,-1,5,-1,-3,1,-2,4,-1,-3,1,-9,5,8,-8,-4,8,9,7,8,5,-5,-2,10,-7,-4,-4,-3,-8,-10,-9,5,-2,-3,-4,-10,-8,-7,3,6,10,-8,-2,3,4,-8,2,2,-8,4,4,3,8,-6,9,2,-1,-4,-1,-5,-2,10,6,7,-7,-4,-4,6,-8,4,-4,5,-7,8,-7,5,-6,1,-8,-4,9,7,6,7,8,1,10,-5,6,6,-6,3,7,4,2,2,7,-9,7,-6,9,-4,3,7,3,-3,6,3,-9,1,-6,-5,6,-3,-9,-5,6,9,-9,1,2,4,-9,3,5,-9,9,-1,9,-8,-5,-9,2,-2,-6,4,-8,-8,-7,-5,5,1,-2,-10,8,-9,3,-8,10,8,5,-6,2,10,-4,-10,-10,6,-5,3,6,-8,4,4,6,-1,-3,3,-10,-3,-7,5,5,-9,8,6,6,1,-10,3,6,-6,-3,-2,-4,-7,-9,-8,4,7,-3,-3,6,8,-10,3,-5,5,-10,10,2,-4,-2,5,4,-5,6,-6,6,10,5,4,-4,9,-3,-7,8,6,-8,5,7,-6,10,5,6,-1,-9,-2,-3,-7,1,3,-7,-1,-4,-6,-6,1,-6,1,-10,-4,9,-1,10,9,2,-3,3,-6,10,-5,6,-2,2,8,-8,-10,10,-1,9,-2,-4,-2,10,-3,1,7,-5,2,6,9,2,-3,1,5,-4,1,-3,-4,-2,-3,6,-2,1,-8,6,1,9,2,-7,-1,3,6,6,7,8,1,-10,-5,-9,-7,10,-2,-3,-10,9,-9,3,8,-7,5,3,-9,9,5,7,-2,2,-8,8,5,-9,-2,2,-10,-3,6,3,10,-9,9,-8,5,-4,-5,2,2,6,2,1,9,-6,-1,-10,10,-7,5,3,5,4,-10,2,8,5,10,-1,-10,-5,6,6,-5,9,8,4,9,-5,-6,10,-7,-3,1,-7,1,-3,-7,4,-4,4,3,7,-7,1,-9,7,-8,-4,-2,-1,3,9,7,-4,6,-2,7,1,10,-7,-4,9,-5,-4,-4,-10,-1,10,2,-8,3,7,7,-6,-1,10,-9,1,1,-1,-10,-3,9,8,7,-2,-6,-2,9,4,3,7,-2,-8,-4,10,-9,5,-8,3,-1,-8,6,-1,-8,-6,8,4,4,5,-10,-9,7,1,9,3,-1,-6,-8,5,-2,8,-6,2,-6,-7,-9,7,2,-3,4,-10,4,-3,3,-2,-8,-6,5,-6,2,-7,-4,9,4,9,-10,2,-5,8,-2,-4,1,7,-6,4,10,1,6,2,-3,-8,9,7,-5,-3,-5,9,7,-1,3,-2,-9,-7,-4,4,1,2,-2,-6,-4,-5,-8,-7,4,-9,-5,10,-8,8,-7,1,4,9,-2,4,8,9,8,2,-5,-9,-3,-6,-7,3,7,-3,9,7,-1,-9,2,4,3,-10,-6,-1,-7,2,-1,9,2,7,5,1,6,-2,8,-6,1,-1,6,-10,9,8,-8,6,-8,9,10,9,2,4,-7,-2,8,-9,-5,9,10,4,4,-8,-6,6,-1,-3,4,2,10,4,-7,-4,2,6,1,-10,3,-7,-6,-6,6,9,-7,-5,-7,4,-2,6,-4,-5,-6,9,-4,-8,-9,-9,-4,-7,1,7,-1,-2,1,-8,-4,-9,-2,10,5,8,4,9,6,-8,-9,5,-6,-4,6,-2,-7,-9,-9,4,-8,-8,-10,8,-4,-2,-1,-3,-3,8,1,10,-10,8,9,-3,-6,7,1,-3,4,-10,-2,4,1,7,-1,-3,-5,10,5,-8,8,1,3,-6,9,1,-8,9,8,-3,-2,-2,9,2,9,7,7,7,-1,-6,9,-4,-4,-8,10,1,-10,-2,7,3,3,-3,9,10,-5,4,4,2,-4,10,6,7,-6,-4,-2,9,10,-6,4,-1,-4,4,5,-6,10,3,7,1,1,-6,-4,-8,9,-3,2,3,-3,4,4,-6,-5,-10,1,6,9,-4,-9,7,-6,2,-8,-6,3,-8,-1,3,5,8,7,7,6,-8,4,4,8,10,10,-7,-7,3,-9,-3,2,-10,7,-4,9,-9,-9,-2,8,5,5,2,8,9,-2,2,8,-2,9,2,-9,-10,-6,7,4,2,5,3,-1,-1,-7,-8,4,1,-7,-3,4,7,8,3,-8,-3,-1,8,-9,9,-3,10,-9,5,2,4,-3,-5,5,-5,3,9,2,-9,8,6,7,1,5,-1,5,-4,-6,-9,8,-5,-2,6,2,5,-5,1,7,7,-9,-10,6,3,4,5,8,5,-2,3,8,4,-1,5,-1,9,-5,-4,-2,2,-9,-9,7,-6,-5,-3,-9,8,3,7,10,-4,4,3,-5,3,4,-2,6,-9,10,-5,10,10,-1,-9,-10,3,1,9,2,1,-4,8,2,2,-1,1,-4,-9,8,3,1,4,-3,9,5,-5,2,10,1,5,10,-7,9,-9,-4,-4,10,8,-1,1,6,8,7,3,1,-4,-8,-5,-5,-3,-9,-5,-5,2,-1,-5,-9,6,-2,-8,10,5,-10,-2,-7,7,2,-4,-4,-6,-1,3,-7,-8,9,1,7,-7,8,-4,-6,8,-3,-8,9,4,-6,-10,8,-1,5,6,2,8,5,-3,-3,9,-5,4,1,-6,7,-2,-5,1,9,-1,-1,10,-3,6,-6,-3,-4,-7,-7,3,-10,-8,-2,-6,-6,-3,-7,4,-4,7,7,-10,-9,5,-1,-9,-7,-5,-5,1,9,-8,-7,-8,3,2,7,1,1,1,6,1,6,4,1,1,-1,10,-1,8,4,-4,-2,-7,10,-2,-6,2,3,3,5,-5,3,4,-4,6,10,10,-4,4,-5,-10,3,4,2,-9,-1,3,2,8,8,5,-5,-2,2,-2,-6,7,-8,5,-8,7,1,-5,-7,-8,-8,-5,-5,-9,6,-3,6,10,-5,-4,-9,4,10,2,2,-2,-10,3,-5,4,6,4,1,5,-8,9,-9,9,2,-7,-3,5,6,-1,-2,2,2,9,-9,9,3,-9,1,-2,-1,-9,7,-8,-4,4,3,4,-4,-1,7,-4,-8,-5,-1,3,-7,6,8,7,-2,8,8,3,4,7,-5,-2,-4,-3,-3,6,-1,-3,8,-1,-2,-8,-2,4,-6,-5,-4,4,-3,2,5,7,-2,-5,4,-1,-6,9,-1,-3,-4,7,-5,-5,-10,-8,4,-1,8,7,3,-8,-8,-6,-10,7,7,-3,9,-3,-4,5,8,6,-1,8,2,2,5,-10,-9,10,-3,10,-10,2,-6,5,3,10,6,-10,5,8,-2,-6,7,6,-8,3,-9,-5,-2,-9,-2,10,6,-6,-4,5,-3,6,7,-2,-8,5,2,4,-8,8,1,-8,10,10,-8,-9,-5,3,-4,-9,3,-10,1,8,7,1,-6,7,-3,-1,3,4,-2,2,-5,10,2,-1,-6,-4,7,-2,-4,-10,-5,8,8,6,10,-9,8,10,-1,-4,-2,-1,4,1,-2,5,-1,-5,-6,10,-8,10,8,5,3,-8,8,3,7,-9,4,-6,8,3,-2,-9,-1,6,9,3,-3,-6,-2,-2,-4,8,7,-4,-7,9,1,2,7,5,3,7,-9,-6,3,-2,1,6,5,-2,-8,-2,1,2,5,-1,3,2,-10,-5,-6,-9,-6,-6,-8,1,-1,6,8,9,5,-10,7,-2,-10,-9,3,-5,6,10,-4,-9,-6,9,3,7,-8,-8,-3,-10,-1,-1,-9,-5,-2,9,6,10,-3,5,-5,-5,3,7,-8,-9,8,-3,-8,3,1,-3,10,-6,2,-10,-6,-1,-8,3,5,-3,1,1,-4,7,-6,2,-4,8,2,3,3,-6,-2,7,10,2,7,1,8,7,-10,10,7,-10,-8,-6,-6,-1,1,6,7,-5,1,-6,-5,5,-3,-9,-6,1,1,2,8,-6,1,-2,-9,-5,-2,9,7,3,10,-2,1,10,-9,-9,-8,-7,4,1,8,-4,-8,-10,-9,-7,-6,-7,10,-9,2,7,-1,-8,6,10,5,4,9,2,-8,-10,6,1,5,-5,8,-6,10,5,5,-2,1,8,2,9,7,-4,7,10,-5,-8,9,-3,-7,-5,-6,-5,-2,7,10,-4,5,1,3,-1,-8,-3,-2,6,-5,-2,-7,-7,9,-5,-10,-8,-6,7,2,-8,-7,-7,-7,8,3,4,6,-1,9,-4,4,6,-10,-7,-8,-3,8,-4,3,9,-2,8,-6,3,-4,4,8,5,-10,-2,-9,-7,-5,2,-3,-3,-3,6,-9,-5,-7,-10,9,-5,-10,-1,-2,-6,7,4,-6,-8,-10,-8,-5,-2,2,-7,7,-1,-1,-6,9,9,-9,-10,9,-5,4,8,6,2,-3,-8,3,9,-2,-6,-8,-8,5,3,-6,5,-10,9,-2,-4,10,-7,-3,-8,3,5,8,-8,9,-10,-10,5,5,-7,-5,-6,-3,9,-1,-1,2,8,7,-6,9,-1,9,8,10,-5,-4,-9,3,-5,6,1,-9,-9,-6,3,8,-2,-2,3,6,6,-8,-1,4,9,1,9,10,-6,-2,10,5,-9,4,10,1,-2,-2,3,-8,-9,2,-8,-5,-7,-5,6,-10,-8,8,-6,3,-9,-4,2,-3,-10,-8,-7,5,1,2,-2,4,-9,-6,-1,-7,-6,1,3,-1,-10,3,4,-1,10,2,-6,-9,-7,1,6,6,-7,9,2,-2,9,-10,-5,-7,4,6,4,-6,10,6,-7,7,-1,3,8,-8,5,1,-8,-5,-6,4,-6,-10,10,-4,2,1,8,9,-3,5,4,6,-4,4,-1,1,-9,-4,9,-3,7,-4,-10,-5,1,-9,-5,7,-5,1,-9,3,-3,6,5,5,-5,-9,4,-8,-3,10,-1,9,-7,-3,-3,4,-5,2,-4,-2,-5,-6,4,-4,10,-6,8,-8,-6,-1,9,-8,10,2,4,4,4,8,3,-6,-5,-3,-8,8,-2,-6,8,5,4,1,1,9,5,-5,9,-1,-2,7,-7,-5,-8,2,-4,2,-4,6,-10,3,2,6,-9,-8,-5,-2,-4,1,-7,5,-10,7,-4,1,8,1,-4,-3,-6,-6,8,3,-5,1,5,-1,-7,-9,3,-4,8,3,4,6,9,-3,10,-8,-10,6,8,-10,-8,-5,3,-2,-7,-2,4,-5,10,9,-5,4,7,1,-5,-10,4,-4,7,7,-4,8,-8,1,10,7,-9,1,9,3,4,1,-9,4,-2,3,-1,3,4,9,-4,-9,7,10,1,4,-7,1,9,-5,6,8,-8,7,5,-8,-2,3,-7,9,-6,-3,-9,8,-10,10,10,-5,9,10,8,4,-5,1,-1,1,-5,-10,-9,-2,-3,6,2,-2,3,-4,2,-3,6,10,-6,5,-5,6,5,-4,-4,-2,4,-5,9,-10,-1,9,-6,-5,2,-4,6,1,-9,10,7,-8,-7,8,6,9,8,5,1,-6,3,-1,9,-10,7,2,3,3,-4,-10,-10,8,-10,-3,6,-5,-7,-7,6,-5,-9,-7,6,6,4,2,4,-1,2,7,-1,-6,7,-5,1,8,-8,4,-6,5,4,-3,5,7,5,-7,4,-5,7,6,3,-7,10,4,-2,7,4,8,-3,1,7,-4,-3,6,10,-7,-7,-1,-8,6,-4,7,4,-9,10,-2,-8,-2,5,1,9,8,4,4,6,3,-4,10,-8,4,9,-9,-4,9,8,-5,-10,4,6,-8,-9,-4,3,-2,3,3,3,10,-4,7,1,-10,6,-6,5,7,-7,8,3,3,5,7,-7,-5,9,2,5,2,-7,6,-4,-5,-1,1,4,-1,9,8,6,4,7,-5,7,4,6,5,10,-1,6,7,5,10,6,9,-3,-9,-10,-1,-2,2,-4,7,8,6,-9,3,-1,-9,2,2,4,6,-6,2,1,-7,2,8,4,-3,9,9,10,-8,10,10,9,-8,2,-4,-4,7,-5,-6,-2,-1,9,-10,10,3,-6,-3,-6,10,9,-10,-5,8,3,8,-5,6,-1,-2,2,2,-8,-3,-6,-2,-8,-7,-1,-4,9,10,1,7,-2,-6,4,-2,-4,7,-1,4,-1,-4,-10,-7,-8,-4,-4,-4,9,1,-9,6,-10,-5,1,-10,-4,5,1,-2,10,2,4,10,-8,-7,-4,2,5,4,-9,-8,-7,5,-4,8,3,-10,6,10,-1,-2,-1,10,2,-4,6,-3,5,-2,-5,5,-2,4,-6,-3,5,-3,-10,4,7,-2,-10,-8,3,5,4,-7,-6,-6,9,-9,-3,-1,-7,4,5,-9,-10,-9,10,-2,-6,1,-2,-4,4,-5,8,-1,-3,1,10,-4,-8,5,8,10,-10,6,8,3,5,-1,4,-8,-7,-8,8,9,-6,3,4,8,4,6,-5,-6,-6,3,-8,-8,9,-2,-7,-2,7,-7,-9,-5,-2,-7,-1,-7,-9,-7,-3,-10,1,1,4,3,1,4,-6,4,-1,6,5,9,6,-1,-10,-1,-4,3,6,-1,5,-6,6,10,3,1,9,-2,-5,2,-5,-10,-3,-8,8,-5,-9,-5,-3,2,1,3,-3,-3,-1,6,9,-4,-9,-3,-6,-2,-1,9,2,-9,-7,2,-1,-10,1,-8,-6,-5,9,-3,-6,9,2,3,-1,8,7,10,7,2,-10,10,-5,10,-3,-8,-8,8,6,5,-6,-7,-4,-2,-9,-1,-7,4,8,-5,-8,9,1,-7,1,-6,6,-1], dtype = "uint64")#candidate|5877|(2816,)|const|uint64
call_5876 = relay.TupleGetItem(func_128_call(relay.reshape(call_5853.astype('int16'), [2, 11, 7]), relay.reshape(const_5877.astype('uint64'), [16, 16, 11]), ), 1)
call_5878 = relay.TupleGetItem(func_131_call(relay.reshape(call_5853.astype('int16'), [2, 11, 7]), relay.reshape(const_5877.astype('uint64'), [16, 16, 11]), ), 1)
func_5115_call = mod.get_global_var('func_5115')
func_5116_call = mutated_mod.get_global_var('func_5116')
call_5886 = relay.TupleGetItem(func_5115_call(), 0)
call_5887 = relay.TupleGetItem(func_5116_call(), 0)
output = relay.Tuple([call_5853,call_5876,const_5877,call_5886,])
output2 = relay.Tuple([call_5854,call_5878,const_5877,call_5887,])
func_5893 = relay.Function([], output)
mod['func_5893'] = func_5893
mod = relay.transform.InferType()(mod)
output = func_5893()
func_5894 = relay.Function([], output)
mutated_mod['func_5894'] = func_5894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5428_call = mod.get_global_var('func_5428')
func_5430_call = mutated_mod.get_global_var('func_5430')
call_5903 = relay.TupleGetItem(func_5428_call(), 3)
call_5904 = relay.TupleGetItem(func_5430_call(), 3)
output = call_5903
output2 = call_5904
func_5910 = relay.Function([], output)
mod['func_5910'] = func_5910
mod = relay.transform.InferType()(mod)
output = func_5910()
func_5911 = relay.Function([], output)
mutated_mod['func_5911'] = func_5911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3000_call = mod.get_global_var('func_3000')
func_3002_call = mutated_mod.get_global_var('func_3002')
call_5947 = relay.TupleGetItem(func_3000_call(), 0)
call_5948 = relay.TupleGetItem(func_3002_call(), 0)
func_3993_call = mod.get_global_var('func_3993')
func_3995_call = mutated_mod.get_global_var('func_3995')
var_5965 = relay.var("var_5965", dtype = "float64", shape = (1200,))#candidate|5965|(1200,)|var|float64
call_5964 = func_3993_call(relay.reshape(var_5965.astype('float64'), [8, 10, 15]))
call_5966 = func_3993_call(relay.reshape(var_5965.astype('float64'), [8, 10, 15]))
output = relay.Tuple([call_5947,call_5964,var_5965,])
output2 = relay.Tuple([call_5948,call_5966,var_5965,])
func_5970 = relay.Function([var_5965,], output)
mod['func_5970'] = func_5970
mod = relay.transform.InferType()(mod)
mutated_mod['func_5970'] = func_5970
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5971 = relay.var("var_5971", dtype = "float64", shape = (1200,))#candidate|5971|(1200,)|var|float64
func_5970_call = mutated_mod.get_global_var('func_5970')
call_5972 = func_5970_call(var_5971)
output = call_5972
func_5973 = relay.Function([var_5971], output)
mutated_mod['func_5973'] = func_5973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4916_call = mod.get_global_var('func_4916')
func_4918_call = mutated_mod.get_global_var('func_4918')
call_5985 = func_4916_call()
call_5986 = func_4916_call()
func_2528_call = mod.get_global_var('func_2528')
func_2532_call = mutated_mod.get_global_var('func_2532')
var_6005 = relay.var("var_6005", dtype = "int16", shape = (154,))#candidate|6005|(154,)|var|int16
var_6006 = relay.var("var_6006", dtype = "uint64", shape = (2816,))#candidate|6006|(2816,)|var|uint64
call_6004 = relay.TupleGetItem(func_2528_call(relay.reshape(var_6005.astype('int16'), [154,]), relay.reshape(var_6006.astype('uint64'), [1, 2816]), ), 1)
call_6007 = relay.TupleGetItem(func_2532_call(relay.reshape(var_6005.astype('int16'), [154,]), relay.reshape(var_6006.astype('uint64'), [1, 2816]), ), 1)
uop_6009 = relay.atan(call_6004.astype('float32')) # shape=(154,)
uop_6011 = relay.atan(call_6007.astype('float32')) # shape=(154,)
func_5522_call = mod.get_global_var('func_5522')
func_5525_call = mutated_mod.get_global_var('func_5525')
var_6025 = relay.var("var_6025", dtype = "bool", shape = (560,))#candidate|6025|(560,)|var|bool
call_6024 = relay.TupleGetItem(func_5522_call(relay.reshape(var_6025.astype('bool'), [5, 7, 16]), relay.reshape(call_5985.astype('float64'), [224,]), ), 0)
call_6026 = relay.TupleGetItem(func_5525_call(relay.reshape(var_6025.astype('bool'), [5, 7, 16]), relay.reshape(call_5985.astype('float64'), [224,]), ), 0)
var_6037 = relay.var("var_6037", dtype = "uint64", shape = (2816,))#candidate|6037|(2816,)|var|uint64
bop_6038 = relay.logical_and(var_6006.astype('bool'), relay.reshape(var_6037.astype('bool'), relay.shape_of(var_6006))) # shape=(2816,)
output = relay.Tuple([call_5985,var_6005,uop_6009,call_6024,var_6025,bop_6038,])
output2 = relay.Tuple([call_5986,var_6005,uop_6011,call_6026,var_6025,bop_6038,])
func_6044 = relay.Function([var_6005,var_6006,var_6025,var_6037,], output)
mod['func_6044'] = func_6044
mod = relay.transform.InferType()(mod)
var_6045 = relay.var("var_6045", dtype = "int16", shape = (154,))#candidate|6045|(154,)|var|int16
var_6046 = relay.var("var_6046", dtype = "uint64", shape = (2816,))#candidate|6046|(2816,)|var|uint64
var_6047 = relay.var("var_6047", dtype = "bool", shape = (560,))#candidate|6047|(560,)|var|bool
var_6048 = relay.var("var_6048", dtype = "uint64", shape = (2816,))#candidate|6048|(2816,)|var|uint64
output = func_6044(var_6045,var_6046,var_6047,var_6048,)
func_6049 = relay.Function([var_6045,var_6046,var_6047,var_6048,], output)
mutated_mod['func_6049'] = func_6049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5893_call = mod.get_global_var('func_5893')
func_5894_call = mutated_mod.get_global_var('func_5894')
call_6059 = relay.TupleGetItem(func_5893_call(), 3)
call_6060 = relay.TupleGetItem(func_5894_call(), 3)
func_1259_call = mod.get_global_var('func_1259')
func_1260_call = mutated_mod.get_global_var('func_1260')
call_6061 = relay.TupleGetItem(func_1259_call(), 0)
call_6062 = relay.TupleGetItem(func_1260_call(), 0)
func_201_call = mod.get_global_var('func_201')
func_203_call = mutated_mod.get_global_var('func_203')
call_6094 = relay.TupleGetItem(func_201_call(relay.reshape(call_6059.astype('float64'), [14, 2, 8])), 0)
call_6095 = relay.TupleGetItem(func_203_call(relay.reshape(call_6059.astype('float64'), [14, 2, 8])), 0)
output = relay.Tuple([call_6059,call_6061,call_6094,])
output2 = relay.Tuple([call_6060,call_6062,call_6095,])
func_6098 = relay.Function([], output)
mod['func_6098'] = func_6098
mod = relay.transform.InferType()(mod)
output = func_6098()
func_6099 = relay.Function([], output)
mutated_mod['func_6099'] = func_6099
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6138 = relay.var("var_6138", dtype = "uint16", shape = (15, 1, 1))#candidate|6138|(15, 1, 1)|var|uint16
const_6139 = relay.const([[[3,-9,-10,9],[2,-6,-9,4]],[[10,-5,4,-1],[-9,-8,1,6]],[[6,3,4,3],[5,6,10,-8]],[[-3,5,6,8],[2,-8,-6,7]],[[4,9,3,3],[-1,1,-9,6]],[[-1,3,-6,-5],[-7,-3,9,-6]],[[-1,10,-6,1],[-10,-3,-1,-2]],[[9,-2,-6,-5],[-9,-5,-10,1]],[[5,5,-2,1],[9,2,-4,-2]],[[2,7,-10,1],[5,-6,-7,6]],[[8,-5,8,-2],[-1,-6,-3,-7]],[[-4,-4,-9,4],[3,8,-6,-3]],[[-6,5,-6,10],[3,2,8,-2]],[[-2,-9,-3,4],[4,7,-6,4]],[[-1,-5,-8,-4],[-3,-9,-4,7]]], dtype = "uint16")#candidate|6139|(15, 2, 4)|const|uint16
bop_6140 = relay.equal(var_6138.astype('bool'), const_6139.astype('bool')) # shape=(15, 2, 4)
uop_6160 = relay.asinh(var_6138.astype('float32')) # shape=(15, 1, 1)
output = relay.Tuple([bop_6140,uop_6160,])
output2 = relay.Tuple([bop_6140,uop_6160,])
func_6162 = relay.Function([var_6138,], output)
mod['func_6162'] = func_6162
mod = relay.transform.InferType()(mod)
var_6163 = relay.var("var_6163", dtype = "uint16", shape = (15, 1, 1))#candidate|6163|(15, 1, 1)|var|uint16
output = func_6162(var_6163)
func_6164 = relay.Function([var_6163], output)
mutated_mod['func_6164'] = func_6164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4724_call = mod.get_global_var('func_4724')
func_4725_call = mutated_mod.get_global_var('func_4725')
call_6166 = func_4724_call()
call_6167 = func_4724_call()
output = relay.Tuple([call_6166,])
output2 = relay.Tuple([call_6167,])
func_6198 = relay.Function([], output)
mod['func_6198'] = func_6198
mod = relay.transform.InferType()(mod)
output = func_6198()
func_6199 = relay.Function([], output)
mutated_mod['func_6199'] = func_6199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1196_call = mod.get_global_var('func_1196')
func_1197_call = mutated_mod.get_global_var('func_1197')
call_6212 = relay.TupleGetItem(func_1196_call(), 1)
call_6213 = relay.TupleGetItem(func_1197_call(), 1)
func_3457_call = mod.get_global_var('func_3457')
func_3458_call = mutated_mod.get_global_var('func_3458')
call_6215 = relay.TupleGetItem(func_3457_call(), 0)
call_6216 = relay.TupleGetItem(func_3458_call(), 0)
output = relay.Tuple([call_6212,call_6215,])
output2 = relay.Tuple([call_6213,call_6216,])
func_6237 = relay.Function([], output)
mod['func_6237'] = func_6237
mod = relay.transform.InferType()(mod)
output = func_6237()
func_6238 = relay.Function([], output)
mutated_mod['func_6238'] = func_6238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3952_call = mod.get_global_var('func_3952')
func_3953_call = mutated_mod.get_global_var('func_3953')
call_6239 = relay.TupleGetItem(func_3952_call(), 0)
call_6240 = relay.TupleGetItem(func_3953_call(), 0)
uop_6266 = relay.sigmoid(call_6239.astype('float32')) # shape=(14, 2, 8)
uop_6268 = relay.sigmoid(call_6240.astype('float32')) # shape=(14, 2, 8)
func_1946_call = mod.get_global_var('func_1946')
func_1948_call = mutated_mod.get_global_var('func_1948')
call_6275 = relay.TupleGetItem(func_1946_call(), 1)
call_6276 = relay.TupleGetItem(func_1948_call(), 1)
func_3065_call = mod.get_global_var('func_3065')
func_3067_call = mutated_mod.get_global_var('func_3067')
call_6286 = relay.TupleGetItem(func_3065_call(), 1)
call_6287 = relay.TupleGetItem(func_3067_call(), 1)
output = relay.Tuple([uop_6266,call_6275,call_6286,])
output2 = relay.Tuple([uop_6268,call_6276,call_6287,])
func_6295 = relay.Function([], output)
mod['func_6295'] = func_6295
mod = relay.transform.InferType()(mod)
output = func_6295()
func_6296 = relay.Function([], output)
mutated_mod['func_6296'] = func_6296
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6337 = relay.var("var_6337", dtype = "bool", shape = (10, 16, 7))#candidate|6337|(10, 16, 7)|var|bool
var_6338 = relay.var("var_6338", dtype = "bool", shape = (10, 16, 7))#candidate|6338|(10, 16, 7)|var|bool
bop_6339 = relay.logical_and(var_6337.astype('bool'), relay.reshape(var_6338.astype('bool'), relay.shape_of(var_6337))) # shape=(10, 16, 7)
uop_6343 = relay.asin(var_6338.astype('float64')) # shape=(10, 16, 7)
output = relay.Tuple([bop_6339,uop_6343,])
output2 = relay.Tuple([bop_6339,uop_6343,])
func_6354 = relay.Function([var_6337,var_6338,], output)
mod['func_6354'] = func_6354
mod = relay.transform.InferType()(mod)
var_6355 = relay.var("var_6355", dtype = "bool", shape = (10, 16, 7))#candidate|6355|(10, 16, 7)|var|bool
var_6356 = relay.var("var_6356", dtype = "bool", shape = (10, 16, 7))#candidate|6356|(10, 16, 7)|var|bool
output = func_6354(var_6355,var_6356,)
func_6357 = relay.Function([var_6355,var_6356,], output)
mutated_mod['func_6357'] = func_6357
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6367 = relay.var("var_6367", dtype = "uint64", shape = ())#candidate|6367|()|var|uint64
const_6368 = relay.const([[[-7,-10,8,-3,-3,10,7,3,3,10,-9,-3,4],[1,-8,-3,-5,-8,-4,4,5,9,-3,10,8,5],[-10,2,2,2,-10,-3,-2,9,-3,3,-9,1,-5],[-10,-2,10,-1,6,6,3,4,2,-8,-2,-6,-8],[5,8,10,-3,-1,4,5,-7,-9,6,8,-1,-3],[-9,8,-5,-7,-5,9,9,2,5,-5,-8,-5,-10],[-4,-1,-6,5,8,-10,-3,3,-4,-3,8,-4,2],[-9,-8,-10,-4,9,-1,-5,-6,-5,-2,10,-3,-4],[3,-5,-2,10,5,-2,10,10,-8,2,2,3,-8],[-9,8,-1,1,-3,-10,3,-4,-6,-6,8,3,-8],[-9,-8,5,-7,1,3,-4,7,3,1,2,-4,6],[-2,1,-4,2,7,-1,10,2,6,-4,-10,-10,4],[10,10,-9,-7,-2,-3,4,10,6,-7,-7,-4,3]],[[-10,7,-7,-2,-3,9,3,10,4,10,9,-7,-6],[-7,-7,-6,-5,1,-8,-9,5,-10,9,-4,5,-10],[10,9,4,-8,-10,8,-5,-9,1,5,-8,-4,-6],[2,4,6,-9,-2,2,-2,4,10,-8,-4,7,-6],[-8,-1,-9,-8,5,9,-10,7,-10,-6,10,4,3],[8,1,4,-4,-6,10,-8,-7,-10,-9,-2,-7,-3],[-4,-6,7,8,2,7,-1,-1,-6,-7,-9,3,8],[-4,4,4,4,-7,-8,1,1,5,1,-4,-8,-4],[-9,-4,-10,2,6,4,-7,-3,7,4,1,1,-9],[1,-5,-4,-1,3,-7,-5,-4,4,-9,-8,-10,6],[4,-3,2,2,-10,4,-7,3,6,8,7,1,9],[-2,-2,10,6,8,-1,5,-7,3,8,7,-3,3],[-6,-6,2,4,8,9,-7,-2,-7,10,-8,7,8]],[[-1,8,-3,-8,9,-6,-5,7,8,1,4,9,-2],[-6,4,-3,-9,10,-3,-10,2,5,10,-9,6,10],[-8,4,7,-10,-8,-7,2,-6,10,9,-1,7,-4],[2,8,10,3,7,5,-3,10,9,-9,-9,2,9],[2,-7,-2,-8,2,-8,3,-5,3,-1,-7,-5,5],[3,1,1,8,10,6,2,-8,-3,6,-9,-5,1],[1,8,1,-5,5,-6,5,-5,-3,-1,5,-2,-3],[9,-1,1,8,2,-3,2,7,1,5,5,2,9],[-1,8,1,-1,2,8,3,9,-9,4,-10,-7,10],[3,9,1,2,-1,9,-9,6,-10,7,5,-2,-3],[-3,-9,4,6,5,-1,-7,2,-6,6,8,3,7],[3,-6,-4,-7,-3,-7,6,6,-9,-2,10,1,2],[-4,-5,4,2,4,-8,-1,4,9,9,7,-2,-8]],[[9,-10,9,7,-7,-9,10,7,6,8,-5,10,-4],[-10,8,-9,-7,9,3,7,-6,8,-4,3,-2,-10],[7,9,-8,10,-8,2,-7,1,-6,9,9,-7,10],[-2,10,9,1,9,-10,-7,7,6,-10,-4,-7,8],[10,-10,-5,3,4,1,2,7,10,-10,3,2,3],[8,9,-10,1,-9,2,-10,-6,2,-4,9,4,2],[7,9,-2,-4,4,1,-3,2,4,2,6,9,-4],[3,-10,-3,2,9,-2,-6,6,-2,8,4,9,-4],[-9,-2,-3,-1,3,-4,-8,9,-5,-6,10,1,5],[4,1,-6,2,5,6,-10,2,2,-6,-1,5,3],[-9,-7,-10,-8,-8,-3,-4,-6,6,9,-2,1,-3],[-1,2,-6,-10,5,2,3,8,2,6,-4,6,4],[6,7,6,10,2,10,8,2,-9,-2,2,-10,-4]],[[5,-8,9,2,3,-2,7,8,-7,-3,6,5,8],[4,8,-10,7,1,2,-9,-3,-10,6,10,-4,-4],[4,10,9,-9,1,1,9,-1,-5,-10,3,1,-7],[5,-3,-4,10,-10,-8,-9,10,7,2,-4,10,7],[1,-5,8,-10,10,-7,-7,-3,-8,6,-2,9,2],[-5,9,-6,-2,1,-2,1,6,-4,7,-10,10,2],[10,10,-7,4,6,6,-2,10,-9,-6,10,-8,7],[-1,5,-1,-7,8,-5,-1,2,-1,-6,8,1,-8],[4,-8,-3,10,-4,-4,-3,6,3,-10,-7,-1,9],[8,-3,-1,-4,10,9,7,2,-6,-2,-2,10,-3],[-3,9,6,-2,-6,6,3,9,-5,-7,8,1,-4],[6,-6,-2,-7,-3,-10,2,9,6,-3,5,-9,-4],[-4,6,9,-5,-5,6,-7,3,-7,1,-2,-9,2]],[[-2,6,10,10,-1,10,-5,-10,6,-1,5,5,-3],[5,-3,-8,9,-8,4,-5,-6,1,-1,-2,8,-10],[-3,-1,6,-10,2,-2,2,10,-10,10,-1,7,4],[10,5,7,7,-6,-3,-9,-4,7,-5,-1,3,8],[6,5,5,10,-5,1,4,-4,6,1,8,-6,-7],[5,2,-2,-9,6,2,5,4,1,3,-4,-3,-9],[-5,2,-5,1,-10,-6,2,4,-10,3,-7,2,4],[-1,3,5,-8,-1,4,10,5,-3,-10,2,6,-5],[-2,4,-5,2,-4,7,6,5,-9,3,1,-2,-3],[-2,-10,1,-6,-9,-10,2,-1,-6,-6,-4,5,1],[-3,8,7,-4,-9,-8,-10,9,-1,-3,-9,-7,9],[-1,1,10,-5,10,10,-9,-1,-7,6,-10,-6,-9],[-2,-9,-10,-5,2,-6,4,1,2,-5,8,5,-8]],[[3,9,-9,10,4,-8,-2,-4,9,8,4,-9,4],[-2,3,3,-6,-10,3,-10,-10,4,9,2,-8,8],[-10,-2,6,3,-6,7,-7,6,5,-7,-6,-8,-10],[3,-1,-9,-9,5,-7,-5,5,8,7,3,1,8],[10,-4,-6,-8,9,-8,-10,-2,-3,3,-6,-1,-4],[6,2,-5,-8,5,-8,-1,-2,-3,-3,-1,-3,6],[3,4,-10,3,2,8,-6,6,-6,1,7,10,1],[6,-4,-5,10,6,-8,3,8,-4,6,10,-8,-10],[7,6,-1,-3,-5,-4,8,6,-9,-7,-2,-3,2],[10,4,-6,-10,-8,5,6,10,6,9,3,10,-5],[1,-1,-1,3,-3,-6,-9,3,-8,5,-10,5,10],[-5,7,5,10,-1,8,-8,-2,3,-9,-5,-7,4],[-1,5,6,-6,-4,3,8,6,-7,-7,9,2,8]],[[4,8,-3,6,2,1,-6,-8,10,-4,-2,-1,2],[8,-9,-1,-2,-2,10,4,-1,-10,10,10,4,6],[-5,-4,8,-10,8,1,-10,4,2,-2,3,-4,3],[-2,-5,4,7,8,-10,4,8,8,10,-8,10,-7],[-5,7,-4,7,-7,-1,9,-8,6,6,9,3,-8],[2,-2,-2,-10,7,5,-3,-2,-5,-4,9,6,7],[1,-5,-3,-6,3,-4,-6,7,2,4,-6,7,5],[-3,3,-8,-10,-3,9,-7,-7,7,1,-5,-6,9],[1,6,-5,-8,-9,-5,9,-1,7,-3,9,8,-6],[5,3,7,-1,9,-2,-6,-5,-9,9,5,9,8],[9,-8,-8,-8,6,-6,-8,6,-4,-8,-3,5,8],[6,9,-5,-10,5,5,-1,-9,-1,4,7,-10,-6],[4,5,-3,-7,-6,1,5,-6,-1,5,-5,-7,6]],[[4,-8,8,-4,-4,-5,9,3,-7,-8,-1,1,-9],[4,3,1,-5,10,3,-8,10,7,-3,1,-9,5],[6,-9,10,2,-3,-3,-1,4,8,8,3,9,-6],[-8,-7,-8,-8,-9,-10,4,-3,-4,1,-8,-9,-6],[4,10,6,-8,8,-10,-2,-5,-2,-10,5,1,3],[4,10,4,-7,-5,-2,-8,8,9,6,6,4,-3],[9,6,5,-6,9,-8,-6,-1,-7,-1,6,-7,-3],[-10,-9,7,-1,4,10,-1,-9,9,-4,-4,-9,6],[-4,-8,9,3,3,8,10,9,1,2,9,-7,-2],[-1,-5,-4,3,-5,10,-10,7,-8,-9,8,-7,2],[-2,6,-10,-4,-6,-4,-10,1,7,6,9,-9,-3],[10,9,-5,-3,-6,-7,-7,-1,-4,-10,-5,-4,8],[-7,4,8,-9,8,-10,4,-1,8,-6,1,-10,-4]],[[-7,-5,4,6,1,1,-2,3,-9,8,10,10,-5],[-9,-1,9,1,-6,8,-2,7,9,4,1,-1,-3],[-7,10,-1,6,-1,-3,10,9,1,-7,7,-8,-9],[2,10,-2,6,8,10,3,-10,4,-6,-10,-6,-7],[-4,-4,6,1,-1,2,7,-9,3,-8,8,6,7],[-1,4,8,3,-9,7,-4,6,-8,-5,8,10,-2],[10,-2,-8,1,-9,10,-10,10,2,6,7,9,-2],[9,-4,10,-2,2,3,2,4,-5,-2,10,8,-3],[1,-8,-10,-6,-1,10,-9,3,-10,6,-8,6,8],[5,-3,3,-2,-10,-10,-7,-3,4,3,-5,-4,-5],[-4,4,1,1,10,10,7,-2,-6,-9,10,-2,3],[-4,-8,9,1,7,-5,-8,4,-4,-9,7,-9,-8],[-2,-10,8,1,-2,-10,-6,-7,-7,5,-4,-10,7]],[[-2,-6,3,-9,-2,-6,4,5,-3,3,1,8,1],[3,6,-1,-6,7,4,2,-4,10,6,-2,-4,2],[6,9,1,9,4,6,-8,1,10,9,-10,1,-2],[-7,-9,4,-9,3,9,-7,-1,-4,5,-2,-7,-8],[9,6,-4,10,4,-9,8,-2,3,9,2,4,9],[10,-4,-6,10,6,7,-5,9,1,-7,4,2,-5],[-9,10,4,5,-2,3,-4,-4,-3,9,5,1,3],[-4,-1,9,-8,7,3,-10,-6,5,-9,1,9,8],[-10,-8,4,-1,-2,4,-1,2,4,7,4,-10,-10],[-9,-10,5,-5,6,4,4,-8,-6,9,1,1,-5],[-9,-1,7,9,6,9,6,3,-3,-8,3,-7,3],[6,-5,10,-8,-6,3,-2,9,2,-7,7,-10,-10],[-8,-7,-7,8,6,8,1,6,-1,-2,-2,-6,-9]],[[-8,8,6,-6,-1,-6,5,-7,5,-8,9,-1,-10],[7,-1,-10,9,-8,-8,-6,5,5,5,4,-9,10],[2,9,6,9,-4,6,-1,-8,9,7,7,8,6],[-1,4,1,7,-7,9,8,-9,9,-1,8,-3,5],[-8,4,-5,-7,8,-3,1,8,10,-3,2,-10,1],[2,2,5,-10,-2,-4,4,-8,-9,-8,8,2,-6],[5,5,3,-9,-7,-7,-3,-2,9,-1,2,5,-4],[8,4,10,2,-7,-5,2,-1,10,9,1,7,-6],[-1,-1,-3,2,-6,1,10,-5,-4,-10,7,1,2],[-5,-3,10,-1,10,1,-5,4,5,2,2,6,-1],[10,10,-5,10,3,3,-2,-9,-4,-10,-8,4,-4],[6,-8,4,10,-9,6,-4,-1,4,-9,-6,7,1],[10,7,-2,3,-1,-8,-10,7,-10,6,7,5,-3]],[[9,7,-7,-3,-1,5,-7,-3,-9,-3,9,-5,-5],[3,10,-10,-7,-7,4,-7,7,8,-10,10,-4,-6],[-6,-7,5,10,-9,-2,-9,-9,1,7,9,3,-8],[1,-5,6,7,-10,-5,-8,3,1,1,5,7,3],[9,7,10,-1,4,6,-3,6,9,2,-5,1,4],[-1,8,-7,1,-6,4,6,7,9,-10,-9,10,8],[6,-3,-3,-9,10,8,2,2,1,3,-2,7,-9],[9,-10,7,6,6,6,-10,5,-6,2,-4,8,1],[2,-1,6,2,-7,-4,1,-2,-7,-3,-2,1,9],[-7,3,-6,-7,7,7,1,-10,-8,-5,8,-7,-6],[10,-3,3,5,-9,2,-9,9,-8,-1,5,1,-10],[-4,10,5,9,10,-9,9,-7,6,-8,10,-7,-8],[10,2,8,8,10,-9,-3,-3,3,2,1,-6,5]],[[6,-8,-4,-4,10,-6,2,-2,-7,10,-9,1,5],[-3,10,-6,10,3,-2,-2,-8,1,-4,-1,-9,-10],[7,4,-3,2,3,-2,-4,6,-3,-10,-7,-3,5],[-10,6,-5,-1,-7,-3,8,9,-10,-8,-10,-7,1],[1,-2,7,-3,4,-10,-6,-7,-7,7,-8,10,-3],[4,9,3,9,-8,-9,-1,-8,6,-7,-3,2,10],[-4,4,9,9,-5,-1,10,-1,8,-10,3,10,-2],[4,-10,-4,3,6,-7,-1,9,-7,1,8,1,8],[7,-4,1,-3,-2,-9,-4,-6,-2,-3,1,2,7],[-3,-9,2,9,4,-4,4,3,-1,-8,8,-8,-5],[-1,2,8,-6,-6,-4,4,6,-5,6,-2,5,-5],[-2,-3,1,3,-2,9,-9,-6,-10,2,-10,6,7],[4,2,4,-2,10,-3,-9,7,2,-2,10,1,-10]]], dtype = "uint64")#candidate|6368|(14, 13, 13)|const|uint64
bop_6369 = relay.bitwise_and(var_6367.astype('uint64'), const_6368.astype('uint64')) # shape=(14, 13, 13)
func_6044_call = mod.get_global_var('func_6044')
func_6049_call = mutated_mod.get_global_var('func_6049')
var_6374 = relay.var("var_6374", dtype = "int16", shape = (154,))#candidate|6374|(154,)|var|int16
var_6375 = relay.var("var_6375", dtype = "uint64", shape = (2816,))#candidate|6375|(2816,)|var|uint64
const_6376 = relay.const([True,True,False,True,True,False,False,False,True,True,False,True,False,True,True,False,True,True,True,True,True,True,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,False,True,False,False,True,False,True,False,False,True,False,False,False,True,True,False,False,True,False,True,True,False,False,False,False,True,False,False,True,True,True,True,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,False,False,False,False,True,True,False,True,False,False,True,False,True,True,True,False,False,True,True,False,False,True,False,False,True,False,False,True,True,False,False,False,True,True,False,False,False,False,True,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,True,False,False,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,False,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,False,True,True,False,False,False,True,False,False,False,True,False,False,True,False,False,True,True,False,True,True,True,True,False,True,True,False,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,False,True,False,False,True,True,True,True,True,False,False,False,True,True,True,True,True,False,False,True,True,True,True,False,False,False,True,True,False,True,True,False,False,True,False,False,True,False,True,False,False,False,False,True,True,True,False,True,True,True,False,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,True,True,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,False,False,True,False,True,True,False,True,True,True,False,True,False,False,False,True,False,True,False,False,True,False,True,False,False,False,False,False,True,False,False,True,False,True,True,False,True,False,True,False,True,True,True,False,False,False,True,False,True,True,False,True,True,True,True,False,True,True,False,False,True,False,True,True,True,False,True,False,False,False,True,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,False,False,True,False,False,False,False,True,True,False,True,True,False,False,True,True,False,True,False,False,True,False,True,True,False,False,True,True,True,False,True,True,False,False,False,False,False,False,True,False,False,True,True,True,True,False,False,True,False,False,True,True,True,False,True,True,True,False,True,False,True,False,True,True,True,True,False,True,False,True,True,False,False,False,True,True,True,False,False,True,False,True,False,True,False,True,True,True,False,False,True,True,False,False,False,True,False,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,False,True,False,False,True,True,True,True,True,False,False,True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,True,True,False,False,True,False,False,True,False,True,False,True,False,True,True,False,True,True,False,False,False,True,False,False,False,False,True,False,False,False], dtype = "bool")#candidate|6376|(560,)|const|bool
call_6373 = relay.TupleGetItem(func_6044_call(relay.reshape(var_6374.astype('int16'), [154,]), relay.reshape(var_6375.astype('uint64'), [2816,]), relay.reshape(const_6376.astype('bool'), [560,]), relay.reshape(var_6375.astype('uint64'), [2816,]), ), 0)
call_6377 = relay.TupleGetItem(func_6049_call(relay.reshape(var_6374.astype('int16'), [154,]), relay.reshape(var_6375.astype('uint64'), [2816,]), relay.reshape(const_6376.astype('bool'), [560,]), relay.reshape(var_6375.astype('uint64'), [2816,]), ), 0)
uop_6379 = relay.acosh(const_6368.astype('float64')) # shape=(14, 13, 13)
func_4966_call = mod.get_global_var('func_4966')
func_4968_call = mutated_mod.get_global_var('func_4968')
call_6385 = func_4966_call()
call_6386 = func_4966_call()
func_128_call = mod.get_global_var('func_128')
func_131_call = mutated_mod.get_global_var('func_131')
call_6389 = relay.TupleGetItem(func_128_call(relay.reshape(var_6374.astype('int16'), [2, 11, 7]), relay.reshape(var_6375.astype('uint64'), [16, 16, 11]), ), 0)
call_6390 = relay.TupleGetItem(func_131_call(relay.reshape(var_6374.astype('int16'), [2, 11, 7]), relay.reshape(var_6375.astype('uint64'), [16, 16, 11]), ), 0)
output = relay.Tuple([bop_6369,call_6373,var_6374,var_6375,const_6376,uop_6379,call_6385,call_6389,])
output2 = relay.Tuple([bop_6369,call_6377,var_6374,var_6375,const_6376,uop_6379,call_6386,call_6390,])
func_6393 = relay.Function([var_6367,var_6374,var_6375,], output)
mod['func_6393'] = func_6393
mod = relay.transform.InferType()(mod)
var_6394 = relay.var("var_6394", dtype = "uint64", shape = ())#candidate|6394|()|var|uint64
var_6395 = relay.var("var_6395", dtype = "int16", shape = (154,))#candidate|6395|(154,)|var|int16
var_6396 = relay.var("var_6396", dtype = "uint64", shape = (2816,))#candidate|6396|(2816,)|var|uint64
output = func_6393(var_6394,var_6395,var_6396,)
func_6397 = relay.Function([var_6394,var_6395,var_6396,], output)
mutated_mod['func_6397'] = func_6397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2741_call = mod.get_global_var('func_2741')
func_2742_call = mutated_mod.get_global_var('func_2742')
call_6418 = relay.TupleGetItem(func_2741_call(), 0)
call_6419 = relay.TupleGetItem(func_2742_call(), 0)
func_5522_call = mod.get_global_var('func_5522')
func_5525_call = mutated_mod.get_global_var('func_5525')
const_6432 = relay.const([False,True,True,True,True,False,False,False,True,False,True,False,True,True,False,False,False,True,True,False,False,False,False,False,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,True,False,True,True,False,False,True,False,False,True,True,False,True,False,True,True,True,False,False,True,False,True,True,False,False,True,False,True,True,False,True,False,False,True,True,False,True,False,False,False,True,False,False,False,False,True,False,True,False,False,True,False,False,False,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,False,False,False,True,False,False,True,False,True,False,False,True,True,False,True,False,False,True,True,True,False,False,True,True,False,False,True,True,False,True,True,False,True,False,True,True,False,True,True,True,True,False,False,False,False,True,False,False,True,True,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False,False,True,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,False,False,True,False,False,True,False,True,False,False,False,True,True,False,False,False,True,True,True,False,False,False,False,True,False,True,False,False,False,False,False,False,True,False,False,True,True,False,True,True,True,True,False,False,False,True,False,True,False,True,True,True,False,True,False,False,False,False,False,False,False,True,False,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,True,True,True,True,False,True,True,True,True,False,True,True,True,False,True,False,True,False,False,False,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,False,True,False,True,True,False,True,False,False,False,False,True,False,False,True,False,True,False,True,False,False,False,False,False,False,True,False,True,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,True,False,True,True,False,True,False,False,True,True,True,False,True,True,True,False,False,False,True,False,True,False,False,False,False,False,False,True,False,True,True,False,True,False,True,False,True,True,False,True,False,True,True,False,False,False,False,False,False,True,False,True,False,False,True,False,False,True,True,True,True,False,True,False,False,False,False,False,False,True,True,False,False,False,False,True,True,True,True,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,False,False,False,False,False,True,True,False,True,True,True,True,False,True,False,False,True,True,True,False,True,True,True,False,False,False,True,True,False,False,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,False,False,True,True,True,True,True,True,False,True,True,False,False], dtype = "bool")#candidate|6432|(560,)|const|bool
call_6431 = relay.TupleGetItem(func_5522_call(relay.reshape(const_6432.astype('bool'), [5, 7, 16]), relay.reshape(call_6418.astype('float64'), [224,]), ), 0)
call_6433 = relay.TupleGetItem(func_5525_call(relay.reshape(const_6432.astype('bool'), [5, 7, 16]), relay.reshape(call_6418.astype('float64'), [224,]), ), 0)
output = relay.Tuple([call_6418,call_6431,const_6432,])
output2 = relay.Tuple([call_6419,call_6433,const_6432,])
func_6440 = relay.Function([], output)
mod['func_6440'] = func_6440
mod = relay.transform.InferType()(mod)
mutated_mod['func_6440'] = func_6440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6440_call = mutated_mod.get_global_var('func_6440')
call_6441 = func_6440_call()
output = call_6441
func_6442 = relay.Function([], output)
mutated_mod['func_6442'] = func_6442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1037_call = mod.get_global_var('func_1037')
func_1039_call = mutated_mod.get_global_var('func_1039')
call_6443 = func_1037_call()
call_6444 = func_1037_call()
func_5428_call = mod.get_global_var('func_5428')
func_5430_call = mutated_mod.get_global_var('func_5430')
call_6452 = relay.TupleGetItem(func_5428_call(), 0)
call_6453 = relay.TupleGetItem(func_5430_call(), 0)
func_4981_call = mod.get_global_var('func_4981')
func_4982_call = mutated_mod.get_global_var('func_4982')
call_6462 = func_4981_call()
call_6463 = func_4981_call()
output = relay.Tuple([call_6443,call_6452,call_6462,])
output2 = relay.Tuple([call_6444,call_6453,call_6463,])
func_6469 = relay.Function([], output)
mod['func_6469'] = func_6469
mod = relay.transform.InferType()(mod)
output = func_6469()
func_6470 = relay.Function([], output)
mutated_mod['func_6470'] = func_6470
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6493 = relay.var("var_6493", dtype = "float32", shape = (6, 8, 5))#candidate|6493|(6, 8, 5)|var|float32
uop_6494 = relay.erf(var_6493.astype('float32')) # shape=(6, 8, 5)
uop_6496 = relay.exp(uop_6494.astype('float32')) # shape=(6, 8, 5)
output = uop_6496
output2 = uop_6496
F = relay.Function([var_6493,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6493,], output2)
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
	relay.transform.SimplifyExpr(),
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
