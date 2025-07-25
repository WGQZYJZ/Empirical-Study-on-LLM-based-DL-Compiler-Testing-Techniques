import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_160 = relay.var("var_160", dtype = "float32", shape = (5, 6, 15))#candidate|160|(5, 6, 15)|var|float32
uop_161 = relay.acosh(var_160.astype('float32')) # shape=(5, 6, 15)
output = uop_161
output2 = uop_161
func_166 = relay.Function([var_160,], output)
mod['func_166'] = func_166
mod = relay.transform.InferType()(mod)
mutated_mod['func_166'] = func_166
mutated_mod = relay.transform.InferType()(mutated_mod)
var_167 = relay.var("var_167", dtype = "float32", shape = (5, 6, 15))#candidate|167|(5, 6, 15)|var|float32
func_166_call = mutated_mod.get_global_var('func_166')
call_168 = func_166_call(var_167)
output = call_168
func_169 = relay.Function([var_167], output)
mutated_mod['func_169'] = func_169
mutated_mod = relay.transform.InferType()(mutated_mod)
var_644 = relay.var("var_644", dtype = "int16", shape = (7, 15, 15))#candidate|644|(7, 15, 15)|var|int16
const_645 = relay.const([[[9,10,-10,-2,-4,8,-9,6,8,7,-8,-2,-9,1,-4],[-6,3,-4,-10,7,9,9,-2,-9,-10,-2,-1,7,7,-4],[1,6,7,6,-10,-1,-8,-7,9,3,-2,6,-9,3,-3],[7,-8,9,-6,-5,7,5,8,10,-8,5,-5,-5,-7,10],[-5,5,1,1,8,4,-1,3,-1,-7,3,10,2,-4,-2],[-9,1,-4,-8,10,10,1,10,-1,6,-1,9,-1,-5,-1],[9,-7,6,3,-4,-9,-6,6,-6,-9,6,-3,1,7,1],[4,8,10,-1,-9,5,-1,-10,-7,5,-1,5,-5,10,-4],[-10,10,-10,-3,5,-7,-1,1,5,-8,-5,-3,-4,9,-2],[4,-1,-1,7,3,-7,-2,9,10,5,-6,8,3,10,6],[4,4,-6,-10,9,5,-4,-2,2,4,-1,-8,-2,1,-2],[3,-8,-5,2,-7,7,-6,-1,-1,-2,2,9,-4,-10,2],[3,10,-4,4,-8,-8,-3,7,3,-8,-7,10,-8,-7,-9],[-10,6,-4,5,-6,-8,-10,-9,6,-7,6,-3,-9,1,1],[5,-2,3,1,3,3,-2,-4,-9,2,7,1,-6,-4,6]],[[-7,-9,4,-3,2,-2,7,7,6,4,-6,-6,2,7,9],[1,8,4,-6,7,-3,4,-7,-3,-10,1,-9,-3,10,-7],[3,4,-10,3,5,5,-3,8,-9,-10,-10,-5,7,10,-5],[-6,-8,2,-9,5,5,2,6,-7,-10,4,-8,-9,-6,-4],[-7,-1,-5,3,8,-9,-8,10,-10,-1,-5,-8,-5,-10,5],[1,-8,-9,3,-8,1,-3,-8,-5,1,-7,-2,-1,-4,-5],[7,-3,8,10,7,4,5,9,2,10,-9,-2,-3,-5,4],[-8,-7,7,-6,-9,-7,10,-10,-5,-4,-10,3,-3,4,7],[-1,-10,5,-6,-8,-3,7,7,4,-4,9,1,-7,-10,2],[1,-2,2,2,-10,4,-5,9,-2,6,-1,-9,6,-7,-7],[6,4,10,-7,5,-3,1,10,10,2,8,-10,6,-3,2],[3,9,-6,-3,-1,10,-7,-4,10,-9,-1,-4,3,6,-4],[-7,8,2,7,7,-6,-4,8,10,-3,10,5,4,5,-6],[-8,-4,1,10,-5,-5,-6,2,8,-3,10,-4,7,-2,8],[1,-9,4,-5,7,3,-9,-3,-4,4,4,9,8,8,8]],[[6,-3,6,-6,-2,-1,6,-6,2,2,5,9,-5,-10,6],[2,9,8,3,-8,-8,-1,-8,5,-7,5,2,6,4,-2],[-5,-4,-10,-2,8,-1,7,-3,1,7,3,-9,-8,4,-2],[2,-3,-4,1,-7,7,7,1,1,6,-9,-9,-7,5,1],[-10,-5,-9,5,8,-9,1,9,6,6,-7,4,-5,-5,2],[6,-8,2,-3,-7,10,-3,4,3,-3,3,-3,-8,-5,7],[-6,9,7,3,-10,-10,-8,9,7,1,10,10,8,2,-10],[1,3,1,-1,9,-5,-2,-3,5,5,-2,10,8,1,-1],[8,-6,-4,-2,-9,8,1,-5,5,6,5,-4,-9,3,4],[-8,10,5,1,10,-10,2,-2,-8,8,-6,-2,-10,-7,-1],[-8,5,-5,3,8,5,-4,1,-7,-3,-5,-10,1,7,2],[9,1,10,-4,1,6,4,-7,8,-6,-9,-1,-7,8,2],[-4,-9,-5,-2,-2,3,-10,-10,1,-1,10,-7,8,5,8],[5,10,-10,5,-6,-4,4,7,3,1,-7,1,-2,-8,4],[-8,-9,-2,-5,-10,3,1,9,1,-10,-3,3,-10,4,6]],[[5,4,-2,2,5,-8,5,-6,-9,-6,9,-5,5,9,-5],[-5,9,-4,-10,-6,-8,3,-4,-10,8,-2,-7,-1,-4,2],[-7,8,10,5,-8,-5,3,-4,7,-10,9,-3,-10,-9,-7],[4,9,10,-3,7,3,-10,10,-5,-7,3,8,-4,-10,-5],[-5,-3,-2,-4,-5,8,3,-6,3,1,8,-8,7,7,7],[6,-2,8,9,8,-3,4,8,8,-3,1,-2,-10,-3,8],[-10,3,3,-5,-3,10,1,1,-4,-1,9,-10,3,10,6],[9,4,7,5,-2,5,4,8,5,8,10,-10,-8,10,-2],[-8,2,2,9,-1,6,5,-4,-7,4,7,-3,-4,-1,-1],[-1,-3,-8,6,10,10,-3,-6,-7,-6,-8,-5,-1,4,-3],[4,-3,-1,-1,8,-2,7,-3,-4,8,1,4,-9,-7,8],[7,6,-10,10,-1,3,9,3,-7,-2,9,-10,-1,10,1],[8,10,7,10,-1,8,-4,-6,-8,-4,-7,-8,-9,-8,-7],[-9,-9,10,10,5,-8,-5,-1,1,-3,4,9,-9,-10,-9],[5,5,-6,-2,-2,-8,-2,-5,6,-4,3,1,1,10,6]],[[-10,7,5,-10,-2,5,-7,2,4,9,9,8,-4,1,-10],[-5,-7,8,8,10,2,-9,-6,10,1,10,1,-1,6,-1],[8,-7,-10,9,-2,-9,8,-3,1,4,3,3,1,1,7],[-4,-7,1,7,-5,-1,-5,-4,-1,2,-6,-1,-2,-4,-2],[2,7,-8,-7,8,-5,-8,-8,-9,-7,6,7,-2,-2,10],[9,-9,-3,7,-1,4,4,6,-4,2,-3,3,-6,1,-5],[-3,4,3,8,-7,-6,6,-3,-3,5,-6,-2,10,-6,-9],[1,7,3,-3,9,1,-3,5,-7,-10,-4,3,-7,-5,4],[-6,-5,2,-3,8,-7,7,-5,-5,-3,-7,3,-2,-2,3],[-2,-1,-2,-4,8,-6,4,-6,-8,-3,5,-7,-7,9,5],[-5,3,-3,-9,-1,-2,3,-4,4,9,4,-5,-2,-9,4],[-3,10,-5,2,-1,-2,-3,6,-3,9,6,-5,4,7,-8],[-7,10,-8,2,8,4,4,-6,-5,3,-10,-7,1,-4,-5],[9,-3,1,3,-1,7,-2,5,5,8,3,-6,5,-10,-8],[-9,-10,8,-4,-7,6,2,-6,8,8,7,4,-10,5,-7]],[[-6,1,-9,-7,2,9,7,7,-2,-5,1,-10,7,3,9],[-4,8,-2,6,1,-5,-7,-4,8,-9,6,4,4,-3,5],[9,-10,-7,-6,-4,-3,7,-1,-4,9,-1,5,9,9,10],[-6,5,6,8,5,8,1,7,8,-1,7,2,-9,3,4],[4,-2,6,3,1,8,-7,5,-10,-7,2,7,8,-2,6],[6,-6,10,-8,9,-4,-9,5,7,8,10,-2,3,-3,-2],[-3,-8,9,-4,-5,-8,-10,-2,-2,-4,-4,2,1,5,2],[-2,6,-5,-2,-3,10,5,-10,-6,-5,5,-5,3,-4,-8],[6,3,-2,10,-5,-10,-4,-6,-2,-7,3,6,2,-1,-10],[5,1,-9,-6,6,1,8,-2,2,-9,1,-2,9,10,10],[-1,5,5,-6,4,4,-9,-1,-9,5,3,-7,6,-8,-5],[6,3,9,-7,1,-10,-7,7,10,-2,-3,4,7,-7,-6],[-3,-10,6,-6,-8,-4,-2,-7,-8,7,3,-4,-10,-9,-8],[-1,9,-9,3,-6,4,7,-1,-7,3,-1,-3,-5,8,2],[-1,8,4,-5,-5,-8,-2,-5,1,-2,-7,3,9,-5,-4]],[[-4,-1,4,-10,-4,9,3,9,4,3,6,-10,10,-7,-8],[-1,5,-7,-9,8,-1,5,10,-6,-6,2,-7,-1,4,1],[8,-6,-3,-1,-9,4,-10,6,5,-2,-10,-4,-7,-5,2],[4,-5,-2,5,-1,-6,4,7,4,5,4,-2,-4,3,1],[3,-7,10,-9,5,-7,6,-5,-5,-7,-8,-6,1,-1,-7],[-4,-10,1,8,-4,9,-4,-5,1,1,-10,1,7,-6,-8],[1,-3,3,-2,3,6,7,10,10,-2,9,7,-8,2,5],[6,4,-8,5,-7,-5,-2,-2,2,4,-10,8,1,-4,-9],[-4,4,4,4,3,8,4,-8,-4,6,-6,1,6,9,8],[8,3,-10,7,8,7,5,8,8,6,2,-2,6,-8,9],[-5,5,-10,-6,-3,4,2,1,-5,-4,3,-10,10,5,3],[1,1,-7,-5,8,7,7,-3,9,-7,6,-10,7,4,-7],[7,6,-6,-1,-6,-10,-10,2,5,-1,4,-2,-6,6,4],[9,-1,-1,8,1,-10,-8,-8,-6,-2,3,4,2,-8,-10],[-10,-4,-3,-2,-7,-6,-2,7,-5,-2,10,2,-3,-6,3]]], dtype = "int16")#candidate|645|(7, 15, 15)|const|int16
bop_646 = relay.right_shift(var_644.astype('int16'), relay.reshape(const_645.astype('int16'), relay.shape_of(var_644))) # shape=(7, 15, 15)
func_166_call = mod.get_global_var('func_166')
func_169_call = mutated_mod.get_global_var('func_169')
var_656 = relay.var("var_656", dtype = "float32", shape = (1, 450))#candidate|656|(1, 450)|var|float32
call_655 = func_166_call(relay.reshape(var_656.astype('float32'), [5, 6, 15]))
call_657 = func_166_call(relay.reshape(var_656.astype('float32'), [5, 6, 15]))
uop_670 = relay.acos(var_656.astype('float32')) # shape=(1, 450)
func_166_call = mod.get_global_var('func_166')
func_169_call = mutated_mod.get_global_var('func_169')
call_688 = func_166_call(relay.reshape(uop_670.astype('float32'), [5, 6, 15]))
call_689 = func_166_call(relay.reshape(uop_670.astype('float32'), [5, 6, 15]))
uop_692 = relay.sin(uop_670.astype('float32')) # shape=(1, 450)
uop_703 = relay.asin(uop_692.astype('float64')) # shape=(1, 450)
bop_707 = relay.add(uop_703.astype('uint64'), relay.reshape(call_688.astype('uint64'), relay.shape_of(uop_703))) # shape=(1, 450)
bop_710 = relay.add(uop_703.astype('uint64'), relay.reshape(call_689.astype('uint64'), relay.shape_of(uop_703))) # shape=(1, 450)
uop_716 = relay.atanh(uop_703.astype('float64')) # shape=(1, 450)
func_166_call = mod.get_global_var('func_166')
func_169_call = mutated_mod.get_global_var('func_169')
call_720 = func_166_call(relay.reshape(call_655.astype('float32'), [5, 6, 15]))
call_721 = func_166_call(relay.reshape(call_655.astype('float32'), [5, 6, 15]))
bop_723 = relay.bitwise_and(uop_716.astype('int16'), relay.reshape(uop_692.astype('int16'), relay.shape_of(uop_716))) # shape=(1, 450)
output = relay.Tuple([bop_646,call_655,bop_707,call_720,bop_723,])
output2 = relay.Tuple([bop_646,call_657,bop_710,call_721,bop_723,])
func_728 = relay.Function([var_644,var_656,], output)
mod['func_728'] = func_728
mod = relay.transform.InferType()(mod)
mutated_mod['func_728'] = func_728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_728_call = mutated_mod.get_global_var('func_728')
var_730 = relay.var("var_730", dtype = "int16", shape = (7, 15, 15))#candidate|730|(7, 15, 15)|var|int16
var_731 = relay.var("var_731", dtype = "float32", shape = (1, 450))#candidate|731|(1, 450)|var|float32
call_729 = func_728_call(var_730,var_731,)
output = call_729
func_732 = relay.Function([var_730,var_731,], output)
mutated_mod['func_732'] = func_732
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1115 = relay.var("var_1115", dtype = "bool", shape = (10, 15, 16))#candidate|1115|(10, 15, 16)|var|bool
var_1116 = relay.var("var_1116", dtype = "bool", shape = (10, 15, 16))#candidate|1116|(10, 15, 16)|var|bool
bop_1117 = relay.logical_or(var_1115.astype('bool'), relay.reshape(var_1116.astype('bool'), relay.shape_of(var_1115))) # shape=(10, 15, 16)
uop_1122 = relay.acosh(bop_1117.astype('float64')) # shape=(10, 15, 16)
func_166_call = mod.get_global_var('func_166')
func_169_call = mutated_mod.get_global_var('func_169')
var_1127 = relay.var("var_1127", dtype = "float32", shape = (450,))#candidate|1127|(450,)|var|float32
call_1126 = func_166_call(relay.reshape(var_1127.astype('float32'), [5, 6, 15]))
call_1128 = func_166_call(relay.reshape(var_1127.astype('float32'), [5, 6, 15]))
bop_1136 = relay.less_equal(uop_1122.astype('bool'), relay.reshape(bop_1117.astype('bool'), relay.shape_of(uop_1122))) # shape=(10, 15, 16)
func_166_call = mod.get_global_var('func_166')
func_169_call = mutated_mod.get_global_var('func_169')
call_1141 = func_166_call(relay.reshape(var_1127.astype('float32'), [5, 6, 15]))
call_1142 = func_166_call(relay.reshape(var_1127.astype('float32'), [5, 6, 15]))
output = relay.Tuple([call_1126,var_1127,bop_1136,call_1141,])
output2 = relay.Tuple([call_1128,var_1127,bop_1136,call_1142,])
func_1144 = relay.Function([var_1115,var_1116,var_1127,], output)
mod['func_1144'] = func_1144
mod = relay.transform.InferType()(mod)
mutated_mod['func_1144'] = func_1144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1144_call = mutated_mod.get_global_var('func_1144')
var_1146 = relay.var("var_1146", dtype = "bool", shape = (10, 15, 16))#candidate|1146|(10, 15, 16)|var|bool
var_1147 = relay.var("var_1147", dtype = "bool", shape = (10, 15, 16))#candidate|1147|(10, 15, 16)|var|bool
var_1148 = relay.var("var_1148", dtype = "float32", shape = (450,))#candidate|1148|(450,)|var|float32
call_1145 = func_1144_call(var_1146,var_1147,var_1148,)
output = call_1145
func_1149 = relay.Function([var_1146,var_1147,var_1148,], output)
mutated_mod['func_1149'] = func_1149
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1387 = relay.var("var_1387", dtype = "float32", shape = (6, 13, 3))#candidate|1387|(6, 13, 3)|var|float32
uop_1388 = relay.cosh(var_1387.astype('float32')) # shape=(6, 13, 3)
output = relay.Tuple([uop_1388,])
output2 = relay.Tuple([uop_1388,])
func_1401 = relay.Function([var_1387,], output)
mod['func_1401'] = func_1401
mod = relay.transform.InferType()(mod)
var_1402 = relay.var("var_1402", dtype = "float32", shape = (6, 13, 3))#candidate|1402|(6, 13, 3)|var|float32
output = func_1401(var_1402)
func_1403 = relay.Function([var_1402], output)
mutated_mod['func_1403'] = func_1403
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1626 = relay.const([[[-5,-9,-3,-6,-6,-6,7,-10,-6,-3,3,8,6],[7,6,-1,-2,-3,3,-5,-8,6,4,-8,-9,3],[-2,-10,-1,-6,8,5,-8,-4,-10,10,1,5,-1],[6,-5,4,9,10,10,6,3,-7,-2,2,9,9],[-5,5,-9,-8,1,-4,3,-2,-9,-2,-10,3,-1],[3,6,-1,-8,9,-9,-2,6,-1,-9,5,-1,-10],[9,2,-8,-1,9,-5,10,4,10,10,-1,8,-5]],[[-8,1,9,1,9,8,-4,-4,4,5,-3,-4,-5],[-5,-7,-6,-1,2,9,1,5,-2,6,9,9,-8],[3,5,-6,-8,5,7,5,5,-7,5,-8,10,-10],[6,7,2,-7,-5,-1,6,-1,1,-6,-1,5,-2],[3,-8,5,4,9,1,5,9,-10,-2,-9,8,-1],[8,-7,8,-6,-4,-10,2,-6,-5,8,-7,-8,9],[3,-5,-8,-10,-3,4,-7,-10,-9,-8,5,6,-5]],[[4,-3,1,2,-8,-8,3,9,1,-8,-2,-5,-3],[-2,-6,3,10,-4,-2,8,-7,10,-8,-7,-2,-1],[-3,-5,-1,-5,-5,8,6,8,-8,-10,3,-5,9],[-9,9,9,10,-8,2,7,-6,3,-7,-2,7,2],[-3,10,-10,-7,1,-3,-2,2,-6,1,6,-6,7],[1,-1,4,9,10,-3,10,-4,6,4,8,-9,-4],[5,9,9,3,-3,5,-1,3,3,9,-8,5,-5]],[[6,4,-2,-9,8,-10,-9,10,-7,1,6,-7,5],[-1,9,-3,-1,-2,-3,-3,2,-4,8,-5,6,7],[3,-8,-7,-7,5,1,7,9,6,-3,-7,9,4],[10,-1,-3,-9,3,7,4,1,8,-9,-10,-10,5],[-3,-3,-8,6,-10,-6,-1,6,-2,-10,6,-1,-8],[1,-5,7,1,-2,5,-10,10,-5,-6,8,3,-1],[7,-5,-4,-5,5,4,6,-4,-7,-7,10,-5,-2]],[[6,-1,6,10,5,2,-2,3,-10,3,9,8,-6],[-7,9,-6,-7,-4,8,-8,10,4,6,10,-8,10],[5,-5,-8,-4,4,-4,8,7,3,-1,-5,5,-4],[-7,-7,4,-7,-3,-3,-4,8,9,-3,3,2,-9],[9,-8,8,-9,-4,-7,2,-8,8,2,-7,1,7],[-7,10,-8,1,-3,-3,4,-3,-10,2,10,9,3],[2,9,-1,-2,2,9,-8,-2,5,8,-8,5,-8]],[[7,6,5,-7,-1,1,-9,-3,-8,-1,2,6,-5],[10,-2,4,6,-1,-2,-3,7,6,7,-2,-10,5],[8,2,6,3,8,9,-9,-3,1,4,10,-3,7],[3,-10,-9,-10,4,-1,-5,-6,1,7,8,1,-5],[2,-9,-5,8,1,-6,6,-6,-8,-6,-7,2,2],[-3,2,6,-8,-4,-7,8,10,8,5,1,-5,6],[5,-8,-9,-9,-1,-6,-2,-1,3,-9,-5,-8,-1]],[[2,5,7,-9,6,8,-9,-2,5,5,5,9,-10],[-10,-7,-7,-6,8,-4,-10,4,-8,6,-6,-4,-9],[1,-10,4,-1,-1,-9,-5,-4,-3,1,-4,-10,9],[-1,9,1,-8,4,2,-3,6,-2,9,9,-10,-1],[9,5,7,10,-6,9,1,7,9,-8,10,-5,6],[2,6,2,-3,5,3,-10,-8,4,-2,-5,-1,-5],[3,-9,-6,6,-4,-9,-5,9,-10,8,9,9,3]],[[10,5,4,-7,-6,5,5,2,8,-8,5,7,-6],[-5,8,9,3,-5,-1,-1,-5,10,-8,4,10,-5],[10,10,10,2,-5,-6,-4,-5,-3,-3,7,-8,8],[2,-2,4,-1,-9,-2,-7,-10,3,-3,-9,9,3],[-7,-10,3,-4,-1,8,-3,-10,-7,-9,-1,-3,5],[9,5,-9,-4,-9,10,-1,-10,-2,-5,-7,1,-1],[2,-7,5,-10,-9,-5,7,8,-5,-8,-8,-9,5]]], dtype = "uint8")#candidate|1626|(8, 7, 13)|const|uint8
var_1627 = relay.var("var_1627", dtype = "uint8", shape = (8, 7, 13))#candidate|1627|(8, 7, 13)|var|uint8
bop_1628 = relay.left_shift(const_1626.astype('uint8'), relay.reshape(var_1627.astype('uint8'), relay.shape_of(const_1626))) # shape=(8, 7, 13)
func_728_call = mod.get_global_var('func_728')
func_732_call = mutated_mod.get_global_var('func_732')
var_1638 = relay.var("var_1638", dtype = "int16", shape = (1575,))#candidate|1638|(1575,)|var|int16
var_1639 = relay.var("var_1639", dtype = "float32", shape = (450,))#candidate|1639|(450,)|var|float32
call_1637 = relay.TupleGetItem(func_728_call(relay.reshape(var_1638.astype('int16'), [7, 15, 15]), relay.reshape(var_1639.astype('float32'), [1, 450]), ), 4)
call_1640 = relay.TupleGetItem(func_732_call(relay.reshape(var_1638.astype('int16'), [7, 15, 15]), relay.reshape(var_1639.astype('float32'), [1, 450]), ), 4)
func_728_call = mod.get_global_var('func_728')
func_732_call = mutated_mod.get_global_var('func_732')
call_1654 = relay.TupleGetItem(func_728_call(relay.reshape(var_1638.astype('int16'), [7, 15, 15]), relay.reshape(call_1637.astype('float32'), [1, 450]), ), 2)
call_1655 = relay.TupleGetItem(func_732_call(relay.reshape(var_1638.astype('int16'), [7, 15, 15]), relay.reshape(call_1637.astype('float32'), [1, 450]), ), 2)
func_728_call = mod.get_global_var('func_728')
func_732_call = mutated_mod.get_global_var('func_732')
call_1656 = relay.TupleGetItem(func_728_call(relay.reshape(var_1638.astype('int16'), [7, 15, 15]), relay.reshape(call_1637.astype('float32'), [1, 450]), ), 2)
call_1657 = relay.TupleGetItem(func_732_call(relay.reshape(var_1638.astype('int16'), [7, 15, 15]), relay.reshape(call_1637.astype('float32'), [1, 450]), ), 2)
output = relay.Tuple([bop_1628,call_1637,var_1638,var_1639,call_1654,call_1656,])
output2 = relay.Tuple([bop_1628,call_1640,var_1638,var_1639,call_1655,call_1657,])
func_1666 = relay.Function([var_1627,var_1638,var_1639,], output)
mod['func_1666'] = func_1666
mod = relay.transform.InferType()(mod)
mutated_mod['func_1666'] = func_1666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1666_call = mutated_mod.get_global_var('func_1666')
var_1668 = relay.var("var_1668", dtype = "uint8", shape = (8, 7, 13))#candidate|1668|(8, 7, 13)|var|uint8
var_1669 = relay.var("var_1669", dtype = "int16", shape = (1575,))#candidate|1669|(1575,)|var|int16
var_1670 = relay.var("var_1670", dtype = "float32", shape = (450,))#candidate|1670|(450,)|var|float32
call_1667 = func_1666_call(var_1668,var_1669,var_1670,)
output = call_1667
func_1671 = relay.Function([var_1668,var_1669,var_1670,], output)
mutated_mod['func_1671'] = func_1671
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1908 = relay.var("var_1908", dtype = "bool", shape = (10, 9, 12))#candidate|1908|(10, 9, 12)|var|bool
const_1909 = relay.const([[[True,True,True,False,True,False,True,True,True,True,False,True],[False,False,False,False,True,True,True,True,False,True,False,False],[True,True,False,True,True,True,True,False,False,False,True,False],[False,False,True,True,False,True,True,False,True,True,False,False],[True,True,False,True,True,False,False,False,True,False,True,False],[True,False,True,False,False,False,False,False,False,True,False,False],[False,True,False,True,False,True,False,True,False,False,True,True],[False,True,True,True,True,False,False,False,False,True,False,False],[True,False,True,True,True,True,False,True,False,False,True,False]],[[True,True,False,False,True,True,True,True,False,True,False,True],[True,False,True,False,True,False,False,False,False,True,False,False],[False,False,True,False,False,False,True,False,True,True,False,False],[False,True,True,False,False,False,True,False,False,False,False,False],[False,False,False,True,False,False,True,False,False,False,True,True],[True,False,True,False,True,True,True,True,False,False,True,True],[False,False,True,True,False,True,True,True,True,True,False,True],[False,True,False,False,True,True,True,False,True,False,True,False],[True,False,True,False,False,False,True,True,False,False,False,False]],[[True,True,True,False,False,True,False,False,False,False,True,False],[True,False,False,False,True,True,False,False,True,True,False,False],[True,True,True,True,True,True,True,False,False,True,True,False],[False,True,True,True,True,False,True,False,False,True,False,True],[True,False,False,False,True,False,False,False,False,True,True,True],[False,False,False,False,True,True,True,False,False,False,True,True],[False,False,True,False,True,True,False,False,True,False,True,False],[False,True,False,False,True,True,False,True,True,False,False,True],[True,True,True,True,True,False,False,True,False,True,True,True]],[[False,True,False,True,True,True,True,False,False,True,False,True],[False,False,True,True,False,True,False,True,False,True,False,True],[True,False,False,True,True,True,True,True,True,True,False,False],[False,True,False,False,False,True,False,False,True,True,False,False],[False,False,True,False,False,False,True,True,False,True,True,False],[False,False,True,True,True,False,False,True,True,False,True,False],[True,True,False,True,False,False,True,False,True,False,False,True],[False,True,False,True,False,True,True,True,True,False,False,False],[False,False,True,False,True,True,False,False,False,False,True,True]],[[True,False,True,False,True,False,True,True,True,True,False,False],[True,True,True,False,False,True,True,False,False,False,False,True],[True,False,True,False,True,True,True,False,True,False,False,False],[False,True,False,False,False,False,False,True,False,True,False,False],[False,True,False,False,True,True,True,True,True,True,True,False],[False,False,False,True,False,False,False,True,True,False,True,False],[False,True,True,False,False,True,False,False,False,True,True,False],[False,False,True,True,True,False,False,True,False,False,True,False],[True,True,True,False,True,False,False,True,True,False,False,True]],[[True,False,False,False,True,True,False,True,True,True,True,True],[True,True,False,True,True,True,True,False,False,True,True,True],[True,True,True,True,True,True,False,True,True,False,True,True],[True,True,False,True,False,True,False,True,False,False,False,False],[False,True,False,False,False,True,False,False,True,True,True,False],[False,True,True,True,False,False,False,True,True,True,False,True],[False,False,False,True,True,False,True,True,False,True,True,False],[True,True,False,False,False,True,False,False,True,False,False,True],[False,False,False,False,True,True,True,False,True,False,True,False]],[[False,False,True,False,True,True,True,False,False,True,False,True],[True,True,True,False,True,True,True,True,False,True,True,True],[False,True,True,False,True,False,False,True,False,False,False,False],[True,True,False,True,False,True,False,True,False,False,True,True],[True,False,False,True,False,False,True,False,True,False,False,False],[True,True,True,True,True,True,True,False,False,False,True,True],[True,False,False,True,False,False,False,True,False,False,True,False],[False,False,True,True,False,True,True,True,False,True,True,True],[False,False,True,True,False,True,False,True,True,False,False,True]],[[False,False,False,True,True,True,True,True,True,False,True,False],[False,False,True,False,True,False,False,False,True,True,True,True],[False,True,True,True,True,True,False,False,False,True,True,True],[False,False,False,False,True,True,False,True,False,True,True,True],[False,True,True,True,True,False,False,True,True,True,True,True],[True,True,True,True,False,False,False,True,False,False,True,True],[False,True,False,False,False,False,True,False,True,True,True,False],[True,False,False,True,True,True,False,False,False,True,True,True],[True,True,False,True,False,True,True,False,False,True,False,False]],[[True,True,True,True,False,False,True,False,False,True,True,False],[False,True,False,True,False,False,False,True,True,False,False,True],[True,True,True,True,True,True,True,False,True,False,True,True],[True,True,True,True,False,False,True,True,True,False,False,True],[False,False,False,True,False,True,True,True,False,False,False,True],[False,True,False,True,False,True,False,True,False,False,False,True],[False,False,False,False,False,False,True,False,False,False,True,False],[True,False,True,True,True,True,True,True,False,True,False,False],[False,False,True,True,False,False,False,True,False,False,True,False]],[[False,False,False,False,False,True,False,True,False,True,True,True],[False,False,False,False,True,False,True,True,False,False,False,True],[False,False,False,False,False,True,False,False,True,False,False,False],[False,False,True,False,True,False,True,True,False,True,False,True],[True,True,True,True,True,True,False,False,False,False,False,False],[True,True,True,True,True,True,True,True,False,False,True,True],[True,False,True,True,True,True,True,False,False,False,False,True],[True,False,True,True,True,False,False,False,True,True,True,False],[False,False,False,False,True,True,False,False,False,True,True,True]]], dtype = "bool")#candidate|1909|(10, 9, 12)|const|bool
bop_1910 = relay.logical_and(var_1908.astype('bool'), relay.reshape(const_1909.astype('bool'), relay.shape_of(var_1908))) # shape=(10, 9, 12)
func_728_call = mod.get_global_var('func_728')
func_732_call = mutated_mod.get_global_var('func_732')
var_1915 = relay.var("var_1915", dtype = "int16", shape = (105, 15))#candidate|1915|(105, 15)|var|int16
const_1916 = relay.const([1.065933,-3.264930,6.594325,-8.933569,4.209411,1.092777,-2.396942,-9.955586,0.229757,-2.399689,-1.786582,8.970834,1.174589,7.998963,-3.574575,6.315107,-6.547267,-3.125470,1.774075,-0.738025,-4.289774,6.566775,-5.527652,0.575936,-6.426861,-6.440552,-4.815876,8.698608,2.832580,-1.373490,3.826980,-8.195942,-1.240762,2.155377,1.292664,-8.696581,-8.004377,-5.043549,6.616683,-4.407552,-8.752410,-8.288200,-8.944073,-0.047710,-8.076393,9.595805,0.771563,2.048501,9.420415,5.510910,2.268211,-4.337812,5.142257,-5.018231,-7.211140,-9.170255,9.117291,-9.950716,-2.589758,-9.265264,6.307433,-4.988093,9.341913,-9.539739,1.392082,7.763462,6.312774,-6.313589,-5.955712,3.793910,6.310760,1.447642,-6.647265,-0.174337,7.262905,-1.704660,-3.782918,8.412861,-4.542820,-6.346464,3.047156,-8.004569,-1.959432,-2.611848,-3.643397,1.103544,6.165109,-6.098244,-7.980025,7.569018,1.705157,7.832192,-6.335116,7.874856,-6.657905,-5.581080,2.496254,8.512247,7.489058,4.755563,7.294528,8.476478,6.598312,6.746233,-1.043797,3.093084,-9.869192,-0.027519,4.459121,0.494183,2.013313,-9.666593,3.130511,-1.647808,2.030549,-5.174757,1.807622,7.003170,1.420516,-6.590302,6.246602,-0.284224,-4.598792,8.131576,-9.315013,-5.343256,-3.295098,0.748824,-6.698688,6.726097,4.684337,-5.406497,2.825166,9.906375,-6.380301,7.703607,-2.760812,6.974416,-2.436574,-4.871829,-1.385922,-0.907845,6.175684,-3.224358,-2.165704,8.587469,4.255075,-5.493350,-4.357061,1.297029,6.965383,-2.979447,-5.895255,4.164778,-2.152344,-5.357480,-2.990482,-2.089369,-1.452825,8.581504,-9.522579,-5.477968,-4.264678,-2.238657,-7.738727,-5.827993,-1.737910,2.025661,-6.657164,0.907054,1.140227,1.177754,4.778686,8.605225,-4.496660,-5.593621,-0.101196,-2.979471,2.211624,6.376939,9.733469,9.177901,-0.023111,-6.792145,8.537689,-9.235253,6.586415,-5.678164,1.322873,-8.860211,-0.877777,-1.168212,4.246887,-3.122404,6.247903,8.841326,3.446931,0.796682,4.927082,-7.881281,7.808767,4.414204,3.505834,8.046999,-9.670723,-3.890905,-3.147853,0.179235,-5.082458,-2.397428,2.073750,-6.699944,9.330093,-3.585558,4.320226,0.322648,8.120532,-8.299905,3.417908,6.837621,8.722287,-9.066391,-0.751355,-3.331040,3.981569,2.538275,-3.308516,9.565548,2.646772,-9.323958,1.063962,5.113431,7.808850,4.088251,-4.271118,-0.293960,-5.185910,9.449896,-5.963973,1.111916,1.667777,-7.092478,-9.469862,7.460386,2.527055,3.075914,7.389558,-4.096449,-8.979724,0.734542,-4.948294,-1.880266,6.773557,-9.109377,4.412917,6.519364,-3.133317,-9.834401,-3.812093,-7.419602,-7.446143,-2.385096,-5.924335,-0.377741,-8.037287,0.304063,3.007781,4.151373,-4.338526,-0.967771,-1.158138,-2.775861,9.708192,7.320140,-5.264185,2.182536,9.279699,-0.247940,-6.729182,-3.088587,0.093273,-2.048527,-3.640022,5.375216,4.188757,-2.230735,9.709113,-4.335466,-1.465952,-8.727210,0.158224,0.754501,8.874430,-6.523900,-4.930939,-9.394125,5.776609,-6.283237,4.835354,-5.544902,6.627106,-3.686071,5.549246,1.570143,-2.726996,-5.076094,6.889297,9.344059,0.963749,2.366597,-7.849227,2.771996,-7.718160,1.672861,6.066791,-9.369864,3.493244,-8.643883,4.652180,-3.421928,1.975370,2.610647,-6.499117,-3.422370,-8.939364,9.849685,4.459552,-7.288686,-5.852735,4.698179,5.829280,-4.446193,-9.858559,0.988864,-5.028880,-1.168234,-0.474485,-0.548559,-1.920688,1.079357,-7.119490,0.391016,6.722975,1.888705,-1.931647,-3.341737,-4.387317,-3.856645,9.926470,-5.935408,3.633403,9.959828,-2.432397,-2.359186,-9.605578,-1.880474,-6.024118,8.158957,7.665386,4.984027,8.840465,-8.497886,-9.889106,1.397920,-2.448542,1.756262,-8.757396,-0.420502,-5.387717,0.836608,-4.977343,-4.980100,3.267629,-3.325435,-4.831484,-5.944722,6.965933,-8.634894,2.932712,6.617320,1.070875,8.567026,-7.512492,9.598155,-1.166518,5.652136,-9.315033,3.247234,4.344608,-4.432964,0.684432,-5.608207,5.077910,-5.333994,-8.764234,9.964865,-4.480630,9.014502,-3.687066,-2.852315,6.803006,2.429101,6.827356,6.043093,-7.619166,-0.770897,0.798933,9.479960,8.204064,2.496825,6.431981,-9.843263,-1.073664,-1.723603,-9.304891,3.382061,9.461916,1.635891,-1.965890,4.762991,-8.668007,-4.398177,-0.220756,9.376123,-8.565684,5.468942,2.387106,7.923425,1.777191,-0.831451,-5.724353,6.538530,-0.163704,-6.175711,-8.417049,9.378474,-8.335870,-8.637674,7.035302,-1.434474,-2.145090,-0.605556,9.587125,2.688135,7.666512,-0.902588,-2.676966,0.296044,-1.814829,7.917891], dtype = "float32")#candidate|1916|(450,)|const|float32
call_1914 = relay.TupleGetItem(func_728_call(relay.reshape(var_1915.astype('int16'), [7, 15, 15]), relay.reshape(const_1916.astype('float32'), [1, 450]), ), 1)
call_1917 = relay.TupleGetItem(func_732_call(relay.reshape(var_1915.astype('int16'), [7, 15, 15]), relay.reshape(const_1916.astype('float32'), [1, 450]), ), 1)
output = relay.Tuple([bop_1910,call_1914,var_1915,const_1916,])
output2 = relay.Tuple([bop_1910,call_1917,var_1915,const_1916,])
func_1928 = relay.Function([var_1908,var_1915,], output)
mod['func_1928'] = func_1928
mod = relay.transform.InferType()(mod)
var_1929 = relay.var("var_1929", dtype = "bool", shape = (10, 9, 12))#candidate|1929|(10, 9, 12)|var|bool
var_1930 = relay.var("var_1930", dtype = "int16", shape = (105, 15))#candidate|1930|(105, 15)|var|int16
output = func_1928(var_1929,var_1930,)
func_1931 = relay.Function([var_1929,var_1930,], output)
mutated_mod['func_1931'] = func_1931
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1977 = relay.var("var_1977", dtype = "float32", shape = (12, 11, 2))#candidate|1977|(12, 11, 2)|var|float32
uop_1978 = relay.sinh(var_1977.astype('float32')) # shape=(12, 11, 2)
uop_1980 = relay.exp(uop_1978.astype('float64')) # shape=(12, 11, 2)
output = uop_1980
output2 = uop_1980
func_1983 = relay.Function([var_1977,], output)
mod['func_1983'] = func_1983
mod = relay.transform.InferType()(mod)
mutated_mod['func_1983'] = func_1983
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1984 = relay.var("var_1984", dtype = "float32", shape = (12, 11, 2))#candidate|1984|(12, 11, 2)|var|float32
func_1983_call = mutated_mod.get_global_var('func_1983')
call_1985 = func_1983_call(var_1984)
output = call_1985
func_1986 = relay.Function([var_1984], output)
mutated_mod['func_1986'] = func_1986
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2043 = relay.var("var_2043", dtype = "uint8", shape = (6, 1, 13))#candidate|2043|(6, 1, 13)|var|uint8
const_2044 = relay.const([[[5,-2,-6,10,-8,-2,10,5,-8,-5,-4,10,-5],[1,-3,5,8,9,-2,1,-3,-3,4,-1,4,3],[-8,-5,-1,-5,1,2,-9,-5,-1,3,9,7,3],[-6,-3,8,-3,-4,-9,-9,-1,10,-2,-5,3,-9]],[[5,8,3,6,4,-7,6,1,10,-6,1,-5,2],[9,7,10,3,1,-1,-2,-2,3,-10,-3,-6,-5],[6,-1,-9,6,8,7,5,7,-4,2,-8,4,-3],[10,8,6,5,-2,8,2,5,7,-7,5,-1,-9]],[[-2,-7,-4,4,-4,3,10,6,3,-5,-7,-6,5],[10,-8,5,4,7,-2,-9,3,-8,7,-2,1,-9],[-8,-5,-6,-8,-5,-6,-8,-8,-6,-9,-9,2,2],[-6,-9,-3,10,1,4,4,-4,-8,-5,-7,3,10]],[[2,6,5,-6,7,-3,-7,6,-4,1,-1,2,-5],[-7,-4,8,8,-9,8,-7,-5,5,-3,-5,9,4],[-5,8,-7,6,-1,-7,-2,1,-4,-6,-9,4,2],[-8,5,3,-10,8,7,1,10,-8,-6,4,-9,10]],[[-1,-9,-4,-4,-1,-9,-9,10,-2,-5,-9,-7,-1],[-5,-1,-8,1,-5,-6,-6,-5,10,3,-9,9,9],[6,4,-7,8,6,-8,5,2,2,8,4,-3,-8],[-1,-8,-6,6,-2,9,-9,-7,-1,-2,-4,2,2]],[[-2,2,9,8,4,10,5,3,3,10,10,-2,6],[-5,-10,6,-3,-1,-2,8,4,-7,1,7,-3,3],[8,-4,-3,-7,-7,4,-1,-10,5,-2,7,2,-1],[-3,-3,6,4,-10,-2,-10,9,-8,-1,5,8,9]]], dtype = "uint8")#candidate|2044|(6, 4, 13)|const|uint8
bop_2045 = relay.greater(var_2043.astype('bool'), const_2044.astype('bool')) # shape=(6, 4, 13)
func_166_call = mod.get_global_var('func_166')
func_169_call = mutated_mod.get_global_var('func_169')
const_2053 = relay.const([-5.825647,4.065346,3.447318,1.772551,2.813708,6.831251,8.185983,6.110874,-7.189836,-0.252993,-2.835432,-1.131142,7.823545,5.345108,6.051566,5.144375,-0.600390,1.127690,-8.667302,-8.183715,3.917703,-4.849323,-9.934702,5.445170,-8.812956,-1.935910,-9.027738,-9.109319,-3.413419,-0.247973,-9.376739,6.385927,3.041966,-0.989207,-0.806047,0.311829,6.336350,-1.399913,-9.261266,-4.934858,9.844575,3.105498,-5.653962,0.838552,5.631476,-2.099849,7.550494,-7.289900,-5.352121,-6.240920,-5.524023,-0.322435,-7.594174,2.399786,7.024939,1.111290,-0.138305,-5.157104,-4.470942,-2.733768,-2.596754,7.364843,-1.335106,-1.818271,-4.508440,0.218912,-6.287371,-6.681097,4.754547,2.321985,-0.191450,7.414381,0.472059,7.366135,-3.499677,-8.007818,-0.187189,-4.874947,5.731875,0.079009,-3.482231,-9.399295,9.416435,6.362225,-3.459180,2.252895,4.957404,-8.810979,-0.376157,-3.729690,1.393933,3.919511,-6.773266,-5.643914,-6.421871,8.390275,3.127367,-9.293534,9.360275,3.101418,-2.381780,-4.234303,5.270596,9.410018,-0.737989,-5.469642,-0.719781,7.684501,-8.781805,-0.603585,1.850678,4.386249,-5.936633,5.855305,8.484044,7.185544,7.321863,0.296522,-9.707138,5.506901,-0.499523,-7.309311,8.672214,9.886417,-0.542951,7.675985,7.361388,-7.182692,-3.745485,3.327883,-6.653389,0.122305,-7.476146,-7.581807,0.163968,9.533334,-4.270021,-2.900911,6.371894,9.522843,-4.997682,-8.935424,9.488998,0.906235,-2.606752,7.068885,3.727914,5.874871,3.525121,9.029547,4.539784,-5.720147,-1.334297,0.156574,-2.383553,5.300247,3.479757,-6.142159,-8.503914,-9.836127,9.731324,8.521365,6.457106,-0.475413,7.949249,1.616731,0.964289,-5.687083,0.339872,0.734674,-9.669058,-6.381192,-6.170230,-8.781788,-8.887805,-2.337745,-4.154804,-8.783516,-6.184305,-6.328066,-1.130962,-0.390624,2.225264,-8.817438,-5.256639,-6.662299,-6.635952,4.119724,1.381527,-3.287276,-3.230949,6.825832,-0.995870,-0.823525,8.485339,-1.419517,4.056096,3.096970,4.688449,7.094889,8.555985,-0.924938,-3.912723,4.254353,3.193352,9.775823,-4.500778,-7.488827,-4.715985,3.065067,5.779478,-4.147926,-5.511595,9.866313,1.078604,2.457635,-0.183076,-4.056363,3.622253,5.499302,8.749996,9.977322,2.629915,4.816550,-4.245062,6.574141,-5.334610,-6.437385,6.364819,1.866637,-0.049154,-3.471661,-4.313810,9.515652,-4.174155,0.562901,8.607635,5.512523,-2.505839,3.887828,7.778264,7.482544,-6.258035,-0.454717,8.593845,-1.485189,-6.542545,6.515869,7.322098,0.649759,4.653045,-1.009872,6.907816,8.118481,-4.759752,-1.328174,-9.672033,1.095558,-2.109010,-1.321924,9.255694,6.020157,8.754435,3.770155,-6.731182,-5.343616,0.158527,-8.988913,-9.221450,-1.472774,-9.913969,-9.926559,-8.829302,7.418104,0.498123,6.189912,-5.220568,7.522544,3.600534,8.856985,5.729903,2.174175,-8.336967,0.486306,9.690768,2.175459,-7.008883,-4.554125,7.832362,9.026936,-4.530741,-0.615986,-9.453827,-4.416760,-9.185101,0.649124,-9.181221,-3.340899,-2.893816,1.239420,6.164520,-3.676116,1.688752,0.103596,-2.447095,3.726604,2.847592,-8.567439,6.235254,3.061892,-0.967494,1.728858,4.621793,0.695982,0.165237,4.601403,8.059053,8.240672,3.282624,5.920062,2.622665,-3.557643,-5.547576,-0.051003,0.668663,4.344025,-6.689754,-4.290543,-1.142814,-0.114260,5.028481,1.848112,0.855572,3.958340,7.460602,-6.143854,0.953410,0.097363,0.616515,-3.306215,5.382898,-5.778731,-0.571281,7.016056,-9.571370,0.164386,3.221565,-3.847833,4.603064,4.658307,5.778703,2.971579,-3.568928,-9.626009,3.643889,8.798278,5.918215,-4.545047,-3.857708,-9.308601,8.446027,-7.870701,-8.072428,1.375198,-2.415748,-7.825848,8.259780,6.911087,-9.441942,4.482592,-9.758431,-0.622333,3.399842,3.349152,-3.052266,-4.624218,8.414668,6.969805,-9.868532,3.971795,1.329079,-5.594353,-8.677485,3.974526,3.217408,-5.114061,6.054158,8.397606,5.799488,-8.796109,0.348664,-2.006162,-1.927776,-8.814317,-0.874454,7.811005,-5.190129,-7.517987,7.659143,5.547106,9.227658,-5.693777,1.748104,1.796883,2.137539,-5.469146,-0.443196,5.856896,-2.841984,6.929624,-5.413968,8.106866,-1.999223,5.078824,1.325917,5.112246,-8.856103,5.119660,2.530055,-8.541509,-9.306114,3.736970,2.302623,5.920217,0.767360,4.313921,-7.719200,-2.273704,-1.490993,-2.700246,-2.252351,-0.847832,-2.109213,-8.308825,-0.394424,-9.115489,-9.112686,-5.985945,-7.001438,2.857332,-6.666232,8.264432,2.312890,-7.030705,7.629508,6.759631,-5.550702,-9.378779,0.124235,-1.838383], dtype = "float32")#candidate|2053|(450,)|const|float32
call_2052 = func_166_call(relay.reshape(const_2053.astype('float32'), [5, 6, 15]))
call_2054 = func_166_call(relay.reshape(const_2053.astype('float32'), [5, 6, 15]))
func_1928_call = mod.get_global_var('func_1928')
func_1931_call = mutated_mod.get_global_var('func_1931')
const_2058 = relay.const([False,True,False,False,False,True,False,False,False,False,True,False,True,True,True,True,True,False,False,False,False,True,False,False,True,False,True,False,False,True,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,True,True,False,True,True,False,True,True,False,False,False,True,False,False,False,False,False,False,True,False,True,False,False,False,False,True,False,True,True,True,True,False,False,True,False,True,True,True,True,True,True,True,False,True,True,False,True,True,True,True,True,False,True,True,False,True,False,False,True,True,True,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,False,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,False,False,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,False,False,True,False,True,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,False,False,False,True,True,True,False,False,True,True,True,True,True,False,False,False,False,False,True,False,True,False,False,False,True,False,False,False,True,False,False,True,True,False,False,False,True,False,False,True,True,True,False,False,True,False,False,True,True,False,True,False,False,True,False,True,False,False,True,True,True,True,True,False,False,True,False,True,False,False,False,True,True,True,False,False,True,False,False,False,False,True,False,True,True,True,False,True,True,False,False,False,True,True,False,True,True,False,True,True,False,True,False,True,False,False,False,False,True,False,False,True,True,True,False,False,False,True,True,True,True,False,False,False,True,False,False,False,True,True,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,False,False,True,False,False,False,False,False,False,False,True,True,False,True,True,False,False,False,False,True,True,False,False,True,True,False,True,False,True,False,True,False,False,False,False,False,False,False,False,False,True,False,True,True,True,True,True,True,True,True,False,True,True,False,False,False,False,True,True,False,True,False,False,True,False,False,True,True,True,False,True,False,False,True,True,True,False,False,False,True,True,False,False,True,False,False,True,False,False,False,False,True,False,False,True,True,True,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,True,False,True,True,True,True,False,True,True,False,False,False,True,True,True,False,False,True,False,False,False,False,True,True,True,False,True,False,False,True,False,True,False,False,True,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,False,True,False,True,False,True,False,True,True,False,True,False,True,True,False,False,False,True,True,False,True,True,False,False,True,False,True,False,False,False,False,True,True,True,False,True,False,False,False,False,False,True,False,False,False,False,False,False,True,False,False,False,True,True,False,False,True,False,False,False,False,True,True,True,False,True,False,False,False,False,False,False,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,False,False,True,False,False,False,True,True,False,False,True,False,False,False,True,True,False,True,True,False,False,False,True,True,True,True,True,True,True,False,False,True,False,True,True,True,True,False,False,True,True,False,True,True,False,False,False,False,False,False,False,False,False,False,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,True,False,True,True,False,False,True,False,True,True,False,True,True,False,True,True,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,True,True,True,False,True,False,True,True,True,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,True,True,True,False,True,False,False,False,True,False,False,False,False,True,True,True,True,True,True,False,False,False,True,False,True,True,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,True,False,True,False,False,False,True,True,True,False,True,False,True,False,True,False,False,True,False,True,True,True,False,False,False,True,False,True,True,False,True,False,True,False,True,True,True,False,False,False,False,False,False,False,False,False,False,False,True,False,True,False,True,True,False,True,True,False,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,False,False,True,False,True,True,True,True,True,True,True,False,False,False,True,False,True,True,True,True,False,True,False,True,False,True,True,False,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,True,True,True,True,False,True,True,False,True,False,False,True,False,False,False,True,False,False,True,True,False,False,True,False,False,True,True,False,True,False,True,True,True,False,False,False,False,True,False,True,False,False,False,False,False,False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,False,False,False,False,False,True,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,False,True,False,True,False,True,False,True,True,True,True,False,False,False,True,True,True,False,False,False,True,True,False,True,False,True,False,True,True,True,True,True,True,True,True,True,False,True,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,False,True,False,False,False,True,False,False,True,True,False,True,False,False,True,True,True,False,False,True,True,False,False,False,True,False,True,True,True,False], dtype = "bool")#candidate|2058|(1080,)|const|bool
var_2059 = relay.var("var_2059", dtype = "int16", shape = (1575,))#candidate|2059|(1575,)|var|int16
call_2057 = relay.TupleGetItem(func_1928_call(relay.reshape(const_2058.astype('bool'), [10, 9, 12]), relay.reshape(var_2059.astype('int16'), [105, 15]), ), 1)
call_2060 = relay.TupleGetItem(func_1931_call(relay.reshape(const_2058.astype('bool'), [10, 9, 12]), relay.reshape(var_2059.astype('int16'), [105, 15]), ), 1)
const_2061 = relay.const([[[-2,-1,6,-1,-8,6,-1,10,-6,6,-1,4,-4]],[[-3,2,-6,-6,-3,1,-7,-8,-1,-8,2,3,-7]],[[-1,-2,-5,7,-8,2,-9,6,-10,-9,8,5,2]],[[-7,9,1,-6,4,-9,-9,-3,-3,-5,-2,-4,1]],[[-10,7,8,-7,9,-7,-3,6,-2,-1,5,7,10]],[[5,10,-5,6,4,-9,1,9,5,-10,3,8,-9]]], dtype = "uint8")#candidate|2061|(6, 1, 13)|const|uint8
bop_2062 = relay.maximum(var_2043.astype('float32'), relay.reshape(const_2061.astype('float32'), relay.shape_of(var_2043))) # shape=(6, 1, 13)
output = relay.Tuple([bop_2045,call_2052,const_2053,call_2057,const_2058,var_2059,bop_2062,])
output2 = relay.Tuple([bop_2045,call_2054,const_2053,call_2060,const_2058,var_2059,bop_2062,])
func_2073 = relay.Function([var_2043,var_2059,], output)
mod['func_2073'] = func_2073
mod = relay.transform.InferType()(mod)
var_2074 = relay.var("var_2074", dtype = "uint8", shape = (6, 1, 13))#candidate|2074|(6, 1, 13)|var|uint8
var_2075 = relay.var("var_2075", dtype = "int16", shape = (1575,))#candidate|2075|(1575,)|var|int16
output = func_2073(var_2074,var_2075,)
func_2076 = relay.Function([var_2074,var_2075,], output)
mutated_mod['func_2076'] = func_2076
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2192 = relay.const([[[-5.764022,7.013433,-2.138989,4.143717,7.066548,6.309833,-9.699311],[-1.714281,-5.718741,-3.235719,-1.790719,-3.950513,-8.787402,-5.161908],[9.092959,-2.765161,-0.203062,-9.910430,-7.750897,-6.244708,-1.202606],[4.617681,-2.785822,-9.294231,2.339692,-7.086411,1.898773,2.270825],[2.660266,1.789407,4.479551,-8.488979,-3.796499,-0.829368,-4.533566],[-4.620503,6.623308,-2.888056,1.735588,-2.259516,6.450214,3.490820],[5.736598,6.205445,-6.845173,3.276798,-2.014742,8.623344,0.209147],[4.468000,-8.634714,-7.680794,-3.903227,-3.054262,5.652487,-0.390181],[7.343205,6.162289,-2.160054,1.573711,2.818978,-3.668299,3.877930],[-7.677407,-6.726949,-8.631935,9.130293,-0.711833,9.546540,-1.734178],[0.407405,-1.941777,-4.012195,3.064747,-5.259050,8.742710,-2.478235],[4.856327,9.951160,-5.893276,5.791388,-3.567943,1.786275,-9.037950],[6.937232,2.203940,7.618404,-2.209216,1.491367,-0.775181,-4.018826]],[[1.826309,-7.495845,-1.652322,8.582206,2.940383,-6.386369,0.021739],[-8.794410,-8.272770,-7.910146,-8.053381,1.905243,0.092769,-2.419014],[-7.002206,6.623724,0.070021,-9.041486,4.560826,-8.785564,1.819216],[4.955423,-3.075067,-6.558378,1.535559,-4.345595,3.798126,-7.824227],[-7.608840,-6.790023,-1.256045,1.580371,8.597204,6.006546,9.312547],[4.232670,-1.830822,4.338167,-4.318860,-3.662242,9.019202,9.421852],[-0.217527,6.979390,8.405045,-5.549542,-1.950671,8.566283,5.920217],[-3.687630,4.338731,1.790499,-0.293439,-8.624666,9.836611,9.259967],[-3.745549,3.373670,-0.449582,9.482869,-9.098111,4.064614,6.539600],[8.476893,-0.758393,4.911732,0.200386,2.190924,-5.030329,0.683925],[-5.037274,-8.951972,1.554507,-5.654369,-8.158179,0.917323,1.313332],[4.331585,-3.584857,3.057966,0.637723,-8.573985,-0.289590,-5.087426],[5.278837,-8.001041,-8.368196,-0.256766,-5.557530,-3.176891,9.584296]],[[5.643523,-6.649212,2.442309,6.217140,4.899822,-0.424303,-1.266142],[-5.199936,8.098702,-8.876719,2.194225,-9.381478,-7.291046,-8.532076],[1.232276,2.132348,-3.275110,-5.780665,-7.032211,6.694880,-4.307168],[0.823300,-7.292796,3.380823,6.506113,3.340976,0.960210,8.803913],[-3.476429,-5.869336,4.788307,-2.390987,1.946299,1.153071,6.640609],[-6.896784,-0.924600,-6.417278,9.649324,-6.707105,0.531738,9.174142],[9.158007,-5.381910,3.108755,-1.162226,-7.938100,-4.527118,5.873274],[0.470616,-0.211588,-7.114213,4.547789,4.904635,-4.218248,-3.443447],[9.796287,-8.180666,-7.842174,-3.225929,5.218061,-2.473455,-2.737301],[-7.542030,-7.407350,-4.565434,6.174741,-1.277492,4.755715,4.438414],[5.602151,9.070291,7.270655,-2.460717,-3.822008,9.811482,8.998230],[-1.154526,1.290475,7.039471,-2.904772,-1.565478,-1.558380,0.291345],[9.171741,5.154078,-9.642733,5.244540,8.870792,0.915571,7.164398]],[[0.965043,-8.401042,-6.660454,-1.056163,7.936597,3.416992,-3.483471],[-2.074165,7.267349,-8.133801,9.918378,6.010321,4.695326,-3.220933],[-3.283030,2.152144,-3.230152,0.290561,6.833329,-6.404254,3.006884],[1.898230,2.949167,9.574415,3.050709,0.335046,-7.788580,0.147890],[0.411982,-2.866210,4.479893,-2.161299,4.320598,-7.295363,8.990820],[7.706169,-9.190571,5.573074,7.564893,-7.223425,-6.767726,2.237350],[-1.195483,-1.203489,-7.966038,-6.777176,3.103465,1.362981,-6.752839],[2.826207,-1.056358,-6.869191,2.383807,-2.289177,-2.065738,3.968646],[-5.383700,6.863795,-8.343140,5.009621,-6.643955,-1.416532,-3.706280],[-4.962296,-6.312698,-2.595441,2.143447,7.613985,-0.426510,0.947747],[8.348101,-3.282217,4.538542,-4.684052,4.687832,-8.421486,1.365169],[6.881701,-9.579932,2.372051,-4.019773,2.989507,-9.842841,-7.796731],[-4.157346,-9.180617,1.408111,9.976935,-7.743065,-2.572143,7.323242]],[[-2.146280,0.200142,-9.820619,9.154875,-8.545289,-5.974289,2.665902],[3.149647,5.967996,0.435150,6.805870,-8.210123,8.586086,-6.856573],[8.464442,-5.518804,3.052836,7.627760,7.391023,5.954544,-0.790380],[1.346843,-4.903827,-4.674494,-3.479098,5.389109,-4.940346,0.320252],[2.877429,3.953128,4.303203,-2.677641,5.725734,5.807119,-1.744747],[3.769500,-2.914940,5.994464,2.812692,-1.130986,4.051232,7.577223],[-7.742310,-2.937185,-0.522028,-0.321437,5.080197,-1.081925,-6.447432],[-8.568937,-0.771286,-1.001802,-9.021673,-6.276410,1.183649,-1.218148],[-8.007048,-7.119743,-5.075884,-8.543967,-7.263122,-6.290997,8.673565],[-5.107127,-8.331118,3.870103,-8.382074,0.143441,8.693800,-0.700442],[7.245545,6.505461,-0.151175,-0.224599,-0.165078,-3.408194,4.133007],[6.196191,5.112284,-4.624959,-5.842362,8.295176,3.050313,6.842209],[-2.833727,6.001552,-6.700007,7.706573,-3.618637,6.124893,9.829739]],[[7.349557,2.703286,7.333548,6.735440,-4.171888,7.215508,-6.324838],[4.024589,8.844039,-8.796802,0.336943,-8.360919,7.387102,-1.461544],[6.939347,-7.859754,-2.839727,6.116673,2.219976,8.947028,-3.731295],[9.626932,-3.600246,1.963686,-5.098696,-6.704156,-8.018304,-5.008131],[-3.443867,4.242943,-9.878031,-3.294995,7.484666,9.981965,-5.470538],[-9.770246,6.513643,-1.758814,-7.782487,-3.444032,1.586980,-1.933670],[2.600695,5.642180,9.475542,2.124191,8.995712,-8.727796,-7.746022],[4.769889,0.030260,6.991718,8.093030,-9.952121,9.573120,-2.418000],[7.028871,3.567252,4.088299,-3.353508,4.257398,2.502387,-9.923202],[9.699593,8.436932,7.121479,-2.274085,5.903894,-1.511378,-5.436122],[-1.889003,-9.339466,9.122954,-4.856269,4.418100,-1.254009,9.121466],[0.518486,1.549942,-9.449692,6.650070,5.041283,-2.524810,3.817475],[-5.815425,9.201381,-6.300215,4.532269,7.677157,-4.784918,-7.643508]],[[6.361397,-4.351733,8.392837,4.066198,-1.567869,-5.889710,-3.248294],[8.092943,3.922608,3.424872,-0.413211,8.481882,-5.547777,-6.814808],[5.921607,7.977824,-3.013175,4.086564,5.030827,6.750984,6.400641],[-6.191217,-1.883153,1.236284,9.709428,-6.250038,-5.828277,4.383696],[-8.952525,9.988018,7.431565,-5.420312,3.509909,6.375571,-8.875973],[-8.083416,-4.583949,-9.549078,-2.857114,0.011100,-2.139540,-3.753565],[3.598830,9.579779,9.149892,5.999558,9.173216,-9.521510,7.765639],[-0.574242,-5.473166,6.461124,9.518531,0.001350,1.414597,9.940590],[2.461463,-1.360187,-8.511058,-8.802367,-2.523341,-2.425955,-3.117087],[-4.689216,-1.426567,6.635134,-4.182728,-0.459750,-1.096605,1.821883],[-4.677174,-5.212750,-6.539622,-8.378444,-6.715008,-5.813186,-7.735715],[8.270979,6.365880,-2.037890,-4.902013,-4.149556,-8.913977,-9.275147],[3.282061,-2.513640,-9.410103,5.956139,3.057071,7.681203,-8.689601]]], dtype = "float64")#candidate|2192|(7, 13, 7)|const|float64
uop_2193 = relay.asin(const_2192.astype('float64')) # shape=(7, 13, 7)
output = relay.Tuple([uop_2193,])
output2 = relay.Tuple([uop_2193,])
func_2198 = relay.Function([], output)
mod['func_2198'] = func_2198
mod = relay.transform.InferType()(mod)
output = func_2198()
func_2199 = relay.Function([], output)
mutated_mod['func_2199'] = func_2199
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2243 = relay.const(-2, dtype = "int8")#candidate|2243|()|const|int8
var_2244 = relay.var("var_2244", dtype = "int8", shape = (15, 1, 5))#candidate|2244|(15, 1, 5)|var|int8
bop_2245 = relay.bitwise_and(const_2243.astype('int8'), var_2244.astype('int8')) # shape=(15, 1, 5)
func_166_call = mod.get_global_var('func_166')
func_169_call = mutated_mod.get_global_var('func_169')
const_2251 = relay.const([-0.884519,2.771420,-0.803645,-4.539510,-9.626633,-1.323914,7.263803,-5.167224,3.170459,-0.740194,-0.858234,-1.039712,6.769210,-9.457449,3.564756,-4.880054,4.475577,6.945784,-3.676078,-8.138652,2.722234,-5.979013,2.147505,-4.282201,-4.583434,5.520717,4.287740,-9.109985,-7.290766,8.979118,9.854241,2.954370,0.794296,-2.869127,6.505517,7.083882,-7.204172,9.229857,-8.689505,-0.531753,-9.881293,9.245603,0.680457,-0.653833,8.862033,3.593986,-7.876605,6.424494,5.962594,6.366262,1.763886,5.039333,-4.862844,1.254644,-6.053623,5.231144,3.177736,-8.875190,1.415064,5.034251,-2.349120,5.403496,9.908075,3.873097,5.464098,3.761538,6.677643,-8.736837,3.930944,-4.527419,8.583244,9.197603,5.215188,-7.021451,-7.758052,9.349851,-7.393488,3.587733,5.855403,7.275432,4.058236,5.225466,5.220348,-2.985269,-9.437100,3.950990,0.905238,-6.749358,-3.466637,1.131582,-8.972914,-4.096495,3.923849,8.495234,-9.215716,4.979901,4.518029,-6.301032,-6.609786,-8.896190,4.513152,4.565823,-0.330791,6.226559,-1.240437,2.094972,8.788941,9.641121,-1.322869,-4.457335,3.269673,-1.759585,-0.977236,-8.467910,-1.497380,3.781631,-1.536521,-5.209906,2.099090,3.601653,-4.006096,-3.021270,-8.772454,-7.800269,-9.151884,4.890777,4.187170,6.746562,-5.667068,-0.074335,-2.216752,0.312837,-7.349185,1.805531,0.712831,4.153744,9.767580,-8.843363,-3.303944,-0.552123,1.512077,-9.913457,-6.264685,-5.227929,1.064735,7.618693,5.148146,-4.580158,-3.206351,8.509728,2.580479,2.103956,-8.371147,-8.464997,-4.842532,-6.198555,5.663213,-2.710847,-2.506138,-9.337302,-9.291023,1.789178,-7.613646,5.963146,7.980757,6.007250,-6.582746,9.418872,-0.757548,1.856749,0.146114,-2.272917,-0.680596,-1.342428,0.035320,5.001063,-2.627367,6.260667,-5.836903,7.660271,5.815134,-8.013769,6.752129,8.586908,-4.633320,-7.114382,-2.508367,-2.120311,-3.084338,0.264107,6.340793,4.401117,5.566361,3.579832,1.565636,7.533490,6.420397,-6.422530,8.797540,-7.417297,-3.311426,9.624362,3.551283,-5.043761,-0.538673,9.172761,-9.133213,1.544781,-4.759954,4.436269,4.512300,-8.807881,4.820157,4.625072,-2.943848,-0.480895,0.031223,4.448484,9.797227,-6.493087,6.647149,8.233364,-8.475258,1.448322,3.053577,-1.407446,0.537566,4.683620,-9.642443,-6.692082,-9.832805,1.381163,-3.967512,-9.297086,-7.646640,-4.582431,3.374827,0.987942,-3.834642,-0.277344,-0.876730,4.025176,3.931044,-2.819793,5.483313,6.049559,1.151388,1.955052,2.688065,5.669824,-8.950404,-3.253374,6.001087,0.191147,-0.916412,-1.524958,6.410543,9.934247,-0.023549,-0.520991,-4.691598,-3.519533,-6.012879,2.717048,6.078026,-8.938664,-5.441614,4.689750,-7.942601,-0.722294,-2.484365,6.882740,-8.417439,1.212089,-0.385800,-0.157121,0.153246,-7.015812,5.211083,4.325873,-7.812495,-0.405214,-3.913552,1.239464,5.959545,-6.817320,-3.726744,5.255726,-5.322528,5.147741,-2.014083,1.708967,-8.312018,4.268921,5.624875,9.120556,-9.044042,6.192446,1.477475,-6.127790,-9.227977,3.287397,-2.355826,3.640230,4.292559,-7.564403,-1.311767,6.387639,1.571509,-8.281862,1.341755,9.070469,-3.895853,4.612586,4.082134,-6.062734,-0.774049,-9.513744,-1.119231,7.495123,-9.588638,5.255307,7.076865,-5.767546,3.057078,9.979390,-4.926736,4.949594,2.653049,-7.360841,-2.194016,-5.958654,-9.285293,2.516816,-7.905657,-3.099706,-4.218718,-7.510623,-6.158113,7.704499,5.310924,5.124893,0.376917,-7.707365,5.391774,0.588008,2.847693,-5.673716,-8.835499,-1.572056,-8.305240,9.193972,-3.279167,-8.961862,-7.609205,2.944044,-4.593954,6.762188,6.817814,4.238628,5.304506,-5.593131,-2.681023,-1.656184,-6.506658,-3.543144,-0.374232,-0.942956,4.668853,6.713728,-1.897512,8.545540,7.981018,-7.969963,6.693913,7.557552,-4.954120,6.025650,-9.591336,1.683604,5.268459,0.257903,3.963084,-6.143852,-8.939175,1.043282,-9.673675,-9.833080,6.369801,-8.294980,-4.626696,2.081508,0.553419,0.133240,5.537948,3.344242,-7.980466,-4.254731,-1.215381,-6.807097,-8.320931,1.924900,5.603260,8.905512,-5.685390,4.432562,9.701703,9.206124,2.441623,4.025207,0.620923,5.122551,8.917860,5.316075,5.058558,9.655812,6.822064,-1.002364,-4.045847,-1.956632,-6.352308,2.437318,-0.152673,-7.052276,2.562550,-6.070848,-4.446372,6.060935,8.299777,9.939348,-9.006728,9.069166,5.478297,-9.463968,6.998099,-8.913783,-1.715343,3.017577,-6.094058,9.668999,6.847594,-5.664899,5.668633,-0.941198,9.522386,4.671723,-9.896674,9.046426,5.044627,7.173587], dtype = "float32")#candidate|2251|(450,)|const|float32
call_2250 = func_166_call(relay.reshape(const_2251.astype('float32'), [5, 6, 15]))
call_2252 = func_166_call(relay.reshape(const_2251.astype('float32'), [5, 6, 15]))
func_1666_call = mod.get_global_var('func_1666')
func_1671_call = mutated_mod.get_global_var('func_1671')
var_2268 = relay.var("var_2268", dtype = "uint8", shape = (728,))#candidate|2268|(728,)|var|uint8
const_2269 = relay.const([10,4,-2,9,2,-9,-10,2,-10,1,-6,1,10,4,-3,-7,-10,9,8,7,3,2,-8,-9,9,4,-4,-7,-2,-4,9,-8,-2,8,4,9,5,1,8,-4,1,4,2,10,2,7,-3,8,-1,-7,-4,-2,-10,2,4,6,-3,-1,-4,9,4,5,2,-5,10,7,8,2,-4,-7,2,6,-6,10,-9,-5,-4,10,-2,8,7,-7,-7,-5,7,3,-7,-5,-5,4,6,7,-8,8,2,-5,3,3,2,3,2,-9,5,4,10,4,-9,-8,7,-8,-3,-7,-4,-6,-10,6,-5,1,-10,1,-6,10,5,-2,-5,3,-3,4,-1,-4,1,3,8,7,-2,1,-1,-3,8,-3,6,-3,-4,-6,7,-8,-3,-4,6,8,10,-5,-10,-9,4,5,8,8,-5,9,-6,2,-9,-10,-10,4,-10,10,7,-2,3,-2,-5,5,7,-4,2,-4,-2,5,-5,-1,7,-8,-3,7,8,-7,10,-5,-5,-9,4,-7,8,-8,10,-1,-1,3,-1,-9,10,2,-7,4,-5,-10,-6,7,10,10,-7,9,2,-1,2,2,8,-1,-2,-1,-8,7,-10,2,10,-2,-5,-4,-2,-9,-8,8,6,3,2,4,4,6,8,4,1,6,6,2,6,4,-2,-2,-10,6,-8,4,4,6,9,1,-5,-6,6,8,-9,7,-3,-10,3,-4,8,1,-9,5,8,-8,2,3,-1,-3,-5,4,9,-10,-1,3,4,5,-2,3,-8,-4,-6,10,10,-10,4,-3,-9,7,-1,1,-6,-1,7,-10,-7,-5,3,-2,1,-10,-5,9,-7,-6,-9,-4,-3,3,8,-5,8,-10,9,6,4,-4,8,-5,-2,-5,-7,-5,-7,2,-4,2,1,4,2,10,3,-6,-7,-10,-3,-9,-8,-3,-3,-10,-2,-10,2,2,2,-3,6,-10,2,2,-4,8,-7,7,-5,-8,7,1,10,5,-5,-8,8,4,5,7,-8,3,5,-7,5,9,-3,-3,-4,-6,-9,-10,2,10,9,-1,2,2,4,-10,-5,2,1,-3,-8,-4,3,7,-7,5,4,-2,-9,-4,4,-3,4,10,-5,-10,2,-1,9,10,-4,-9,10,3,-6,2,2,2,3,1,3,-10,-5,-9,6,10,6,-8,-3,-8,1,-10,7,1,3,7,-1,-2,5,-1,-5,-3,-10,-9,-4,-1,-9,8,-4,8,-10,3,10,-8,-9,8,-1,4,3,-4,2,-4,6,-9,-2,8,-9,-3,-6,-6,1,-6,-6,-4,4,8,3,9,5,-2,4,-6,10,-4,2,3,3,-6,2,9,-7,-3,10,-4,9,-1,7,-6,9,-5,-7,4,10,10,-1,-7,8,3,-10,-5,2,-2,5,5,-5,5,-1,-5,-3,10,-5,-6,-4,5,5,-5,-5,-7,-2,-4,-5,2,-2,-6,1,10,-2,1,5,-4,-5,9,-5,-10,-9,5,-5,-9,-3,3,2,9,2,-1,-7,7,-3,4,1,6,-10,3,7,6,8,3,-5,-3,6,3,-1,7,-5,2,7,-7,9,6,-3,-6,-2,-2,-5,3,10,-7,4,-5,-7,8,-4,-2,-2,-1,-3,-7,-7,-1,3,4,-1,4,-6,-6,-7,6,-7,4,-1,6,3,-8,-2,5,-4,-9,-1,-10,-2,-10,1,2,-6,-1,3,-10,3,-7,6,8,-10,-5,-10,7,-1,2,-3,-4,-1,6,4,-8,-4,10,6,10,-5,-6,9,-6,10,-6,10,-2,5,-5,-5,-6,10,9,-3,2,3,2,3,2,-6,4,8,-9,5,-4,8,7,5,4,4,-6,5,-9,-4,10,1,7,2,-4,1,5,-5,7,-10,-8,6,1,1,-8,1,6,3,-1,1,-10,-3,-10,-9,10,8,4,-3,-5,-5,1,2,7,-3,10,4,-4,7,7,3,-7,-5,-4,6,-3,2,-6,-1,8,3,-6,10,-6,-6,-4,8,7,-2,4,-10,-10,10,7,-1,5,-4,1,-3,-10,-9,7,8,3,-6,-10,1,-1,8,-4,6,2,-10,-4,9,-3,2,6,-3,2,5,6,-3,-8,-6,1,10,1,-6,7,3,-6,8,-5,-2,-10,8,-2,4,4,-10,3,-8,-4,-3,2,10,1,9,-1,-2,7,-9,-2,6,-7,1,-8,6,3,-4,-3,2,-4,-9,-3,6,-2,-6,-9,2,-1,-8,4,-3,-3,-4,3,2,9,2,4,-2,4,3,-2,-1,-8,4,-3,8,7,-2,-8,-6,8,10,8,10,-10,5,-8,7,-5,7,-9,6,7,-6,4,1,-2,6,3,-1,-1,-6,-5,4,-5,10,7,10,3,8,-8,1,-2,-9,5,9,-6,-6,10,-1,-2,-9,-6,-1,-4,10,10,1,10,-6,-10,2,9,-7,7,-4,-10,8,-3,-6,-9,-1,10,8,4,7,-8,9,7,6,3,-5,-4,-8,-1,4,-5,-9,-6,4,-3,-3,-10,-8,-10,10,-8,-8,-7,9,-5,10,-9,2,7,7,-7,-1,-5,-3,-7,10,-8,-6,-7,5,-2,-9,-5,8,10,-4,-6,-3,5,-7,1,-8,6,-5,10,4,-6,-3,-5,-3,-6,2,-3,6,3,10,1,-4,-1,1,-9,-5,7,6,-9,-6,5,1,-5,5,2,-3,-5,-1,5,10,-6,-1,-1,6,-5,8,-10,-9,8,2,-1,-3,1,-3,-8,10,-5,9,-7,9,7,3,8,2,-6,-6,-1,-1,4,9,-6,8,-2,-1,-1,-1,10,6,6,4,4,6,10,8,-3,8,7,-3,6,-8,-4,5,-4,2,9,-1,5,-8,9,10,4,1,7,-2,8,10,-10,-6,8,-6,3,1,9,4,7,9,-4,-5,-6,4,7,-8,8,3,1,2,1,3,-3,7,10,3,6,-5,-7,6,4,10,7,10,5,3,5,5,2,-2,-7,8,-5,8,3,-3,-10,-9,-8,-9,10,8,-8,7,-4,2,-4,-7,-3,-10,-10,3,7,1,2,-8,-9,-10,-9,7,-6,5,9,-8,6,1,8,-10,-10,10,-8,-6,5,6,-5,-7,1,-10,1,-5,3,-5,-1,-7,3,-3,-8,-9,-9,8,7,-4,5,-9,1,3,9,4,-2,-9,10,9,-4,-2,-3,-4,6,-9,3,7,-1,5,-10,-7,4,1,-1,4,1,6,-8,4,-10,7,2,-5,-4,-2,3,-1,7,-1,-2,-4,4,-7,-2,-8,-6,4,-9,-1,-1,-1,4,1,4,2,8,-9,7,7,-8,2,2,-4,-6,5,-9,4,-6,7,-7,-6,-4,-1,2,2,5,-6,9,9,8,-5,-10,-10,-3,8,5,-7,10,2,6,-2,8,-7,9,-4,-1,3,9,-10,2,2,-2,10,7,-6,6,3,7,4,-7,4,-9,-7,-4,-9,-5,-6,10,-2,8,7,5,1,-9,7,-3,-1,-8,9,7,8,8,2,-10,4,-2,5,10,-7,-8,4,5,-2,-8,-5,-10,1,-9,-8,9,8,-1,-7,6,2,10,5,-5,-8,-9,-10,-6,-9,-5,-5,-6,-6,-5,-2,8,-6,1,-4,10,9,-5,-10,-1,-7,5,1,-4,-2,9,-9,-7,-5,-8,-3,3,10,3,10,-1,10,-8,9,7,10,-5,-3,3,9,9,10,5,9,-9,4,5,-6,-5,6,8,8,-4,-4,-10,-10,6,-10,-9,-1,-7,10,8,-6,3,-7,-5,-4,5,-8,2,6,10,-9,7,9,6,6,5,9,4,-1,-10,-10,3,-1,-9,-3,5,8,-3,-5,-4,2,-3,-9,4,7,-3,8,6,10,-8,-2,4,-4,7,-5,10,-2,10,-1,-1,8,-5,3,10,7,-6,-3,-1,9,-8,-10,-4,5,-4,-8,-5,3,7,-1,9,6,-1,6,-8,9,-1,-6,1,-1,-8,-2,-7,2,10,10,-5,5,-7,-5,7,-1,-3,5,10,9,-5,2,-7,-6,10,-4,-4,1,9,-6,-10,-7,6,8,-8,-6,9,4,2,1,-8,9,6,-3,3,-3,6,9,2,8,6,4,1,1,8,7,9,-7,-3,-1,-8,1,-8,6,10,1,-9,9,-1,-5,-2,-4,-6,7,-1,-6,-7,-5,-9,-5,8,-5,1,6,6,-2,4,1,-8,9,-1,10,-6,-2,-9,-6,-5,3], dtype = "int16")#candidate|2269|(1575,)|const|int16
call_2267 = relay.TupleGetItem(func_1666_call(relay.reshape(var_2268.astype('uint8'), [8, 7, 13]), relay.reshape(const_2269.astype('int16'), [1575,]), relay.reshape(call_2250.astype('float32'), [450,]), ), 0)
call_2270 = relay.TupleGetItem(func_1671_call(relay.reshape(var_2268.astype('uint8'), [8, 7, 13]), relay.reshape(const_2269.astype('int16'), [1575,]), relay.reshape(call_2250.astype('float32'), [450,]), ), 0)
output = relay.Tuple([bop_2245,call_2250,const_2251,call_2267,var_2268,const_2269,])
output2 = relay.Tuple([bop_2245,call_2252,const_2251,call_2270,var_2268,const_2269,])
func_2279 = relay.Function([var_2244,var_2268,], output)
mod['func_2279'] = func_2279
mod = relay.transform.InferType()(mod)
var_2280 = relay.var("var_2280", dtype = "int8", shape = (15, 1, 5))#candidate|2280|(15, 1, 5)|var|int8
var_2281 = relay.var("var_2281", dtype = "uint8", shape = (728,))#candidate|2281|(728,)|var|uint8
output = func_2279(var_2280,var_2281,)
func_2282 = relay.Function([var_2280,var_2281,], output)
mutated_mod['func_2282'] = func_2282
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2294 = relay.const(2.650877, dtype = "float32")#candidate|2294|()|const|float32
var_2295 = relay.var("var_2295", dtype = "float32", shape = (6, 10, 13))#candidate|2295|(6, 10, 13)|var|float32
bop_2296 = relay.divide(const_2294.astype('float32'), var_2295.astype('float32')) # shape=(6, 10, 13)
output = relay.Tuple([bop_2296,])
output2 = relay.Tuple([bop_2296,])
func_2302 = relay.Function([var_2295,], output)
mod['func_2302'] = func_2302
mod = relay.transform.InferType()(mod)
var_2303 = relay.var("var_2303", dtype = "float32", shape = (6, 10, 13))#candidate|2303|(6, 10, 13)|var|float32
output = func_2302(var_2303)
func_2304 = relay.Function([var_2303], output)
mutated_mod['func_2304'] = func_2304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2198_call = mod.get_global_var('func_2198')
func_2199_call = mutated_mod.get_global_var('func_2199')
call_2387 = relay.TupleGetItem(func_2198_call(), 0)
call_2388 = relay.TupleGetItem(func_2199_call(), 0)
func_1983_call = mod.get_global_var('func_1983')
func_1986_call = mutated_mod.get_global_var('func_1986')
const_2397 = relay.const([[9.239278,-3.127470],[-4.378304,-1.197328],[1.243823,5.260182],[-1.674101,-1.187654],[6.481820,0.147922],[9.793662,-6.892856],[-9.647637,-1.525974],[3.326923,3.022226],[7.785882,-0.881034],[-7.863288,-1.392953],[-9.925444,-0.975326],[-9.138300,-9.615694],[-6.020532,-1.683280],[5.730386,0.395709],[-1.542190,-5.048750],[-1.202550,-9.395019],[3.617992,2.734858],[4.718400,8.216416],[1.646906,9.172087],[-5.255051,7.505097],[0.289306,3.238570],[6.395828,-2.180398],[-3.565165,1.808447],[-2.999281,-0.964161],[-3.744608,5.429791],[6.482025,3.146331],[-9.111117,2.584400],[-0.761543,2.037875],[-7.848717,-9.467571],[-8.356894,0.201677],[-0.319114,0.217045],[-1.389621,-7.316027],[4.240025,-4.705418],[2.340864,1.964004],[-6.283503,-2.845017],[-8.937325,8.125127],[-0.298087,-4.757405],[-2.747816,0.233137],[-2.503993,-6.082835],[7.360416,3.166550],[-4.483628,1.925019],[8.609128,-5.167820],[4.987968,5.611945],[-0.755202,-6.511617],[-7.146920,6.702746],[-4.159150,2.391947],[1.086520,8.365536],[8.743270,7.887896],[0.371791,0.897803],[-2.887522,-0.586141],[-0.393745,3.116367],[-5.132995,-0.581454],[-2.186466,-1.398918],[-9.247824,0.445300],[1.658305,-9.247195],[4.727726,-9.467804],[5.976374,0.500307],[8.588388,0.970105],[7.720850,0.349268],[1.360433,2.038231],[4.847555,-6.495168],[9.419003,-2.451346],[5.017031,8.833506],[-0.139973,6.412383],[2.718139,0.855090],[-2.657458,3.174573],[3.220004,-8.269295],[-6.095350,-8.459940],[3.984443,1.573153],[-3.421647,9.697411],[8.614518,-6.734107],[-0.664037,8.013605],[0.961494,2.591109],[1.333464,4.349396],[6.448267,0.962339],[3.582402,6.251589],[5.732738,-5.145829],[-4.813197,0.605224],[-3.732863,-9.552696],[2.138206,2.771056],[-0.879080,-4.787464],[5.941085,1.445813],[7.364190,-1.773884],[-7.771897,0.563993],[-2.485280,-4.147956],[5.638700,-3.725643],[8.119019,7.075381],[-5.949857,9.492321],[4.192542,2.087472],[-9.090749,7.785592],[2.784215,-0.647268],[9.478729,9.801756],[0.821602,6.014639],[0.736074,7.258697],[-4.795130,5.585378],[8.889514,5.527763],[5.760517,3.324813],[1.420460,0.817528],[-0.737517,7.221004],[-6.866471,7.731173],[-7.637168,-4.329832],[1.617613,-5.042718],[-1.444603,-8.622238],[4.171471,-1.339271],[-3.536881,-6.820930],[-0.227834,9.505211],[8.874643,2.387400],[3.431018,-5.478413],[5.702431,-7.302843],[-8.158805,-7.688938],[-4.243968,-2.710365],[-2.144540,-3.822024],[-8.689796,5.790651],[4.948514,2.699098],[3.237283,-8.069537],[2.808366,-2.133500],[3.617320,8.516945],[9.891917,7.849054],[9.751041,4.587306],[-5.725582,-7.139437],[-0.961353,-7.582840],[-4.237086,3.007389],[-1.911569,9.232085],[-8.403126,-1.952068],[-2.574409,3.389255],[2.604295,8.830387],[-3.360151,-9.988825],[5.615417,1.853218],[-7.203905,9.874803],[5.390595,-6.987129],[-4.789686,9.370961],[4.178701,-1.227370]], dtype = "float32")#candidate|2397|(132, 2)|const|float32
call_2396 = func_1983_call(relay.reshape(const_2397.astype('float32'), [12, 11, 2]))
call_2398 = func_1983_call(relay.reshape(const_2397.astype('float32'), [12, 11, 2]))
output = relay.Tuple([call_2387,call_2396,const_2397,])
output2 = relay.Tuple([call_2388,call_2398,const_2397,])
func_2399 = relay.Function([], output)
mod['func_2399'] = func_2399
mod = relay.transform.InferType()(mod)
output = func_2399()
func_2400 = relay.Function([], output)
mutated_mod['func_2400'] = func_2400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2399_call = mod.get_global_var('func_2399')
func_2400_call = mutated_mod.get_global_var('func_2400')
call_2408 = relay.TupleGetItem(func_2399_call(), 0)
call_2409 = relay.TupleGetItem(func_2400_call(), 0)
output = relay.Tuple([call_2408,])
output2 = relay.Tuple([call_2409,])
func_2410 = relay.Function([], output)
mod['func_2410'] = func_2410
mod = relay.transform.InferType()(mod)
output = func_2410()
func_2411 = relay.Function([], output)
mutated_mod['func_2411'] = func_2411
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2512 = relay.var("var_2512", dtype = "float32", shape = (5, 4, 11))#candidate|2512|(5, 4, 11)|var|float32
var_2513 = relay.var("var_2513", dtype = "float32", shape = (5, 4, 11))#candidate|2513|(5, 4, 11)|var|float32
bop_2514 = relay.subtract(var_2512.astype('float32'), relay.reshape(var_2513.astype('float32'), relay.shape_of(var_2512))) # shape=(5, 4, 11)
func_2073_call = mod.get_global_var('func_2073')
func_2076_call = mutated_mod.get_global_var('func_2076')
const_2520 = relay.const([7,-8,9,-3,-2,8,10,2,10,5,-6,8,-4,9,-3,-3,6,-3,5,4,8,9,7,-10,-1,7,-1,-7,7,2,10,-2,-7,1,-2,1,-7,8,4,-3,6,-4,-2,-10,5,-8,-7,1,-5,6,-7,7,-7,-8,-4,6,10,5,-1,10,8,2,10,9,-6,-3,4,-9,-5,-2,7,-7,9,8,8,7,7,1], dtype = "uint8")#candidate|2520|(78,)|const|uint8
const_2521 = relay.const([[10,7,4,-1,-1,7,6,9,5,-2,-10,-4,-9,7,-10,1,10,-4,-5,-9,4,8,-3,4,6,6,-7,10,-7,5,9,7,-5,2,-8,6,8,-1,-10,10,-1,3,9,5,2,5,-7,3,-5,-3,7,-4,5,5,-2,-1,-3,4,-10,10,-10,-5,1,-10,2,-1,3,1,3,-3,-3,2,1,-8,5,-2,6,4,5,6,-9,6,2,-2,-7,4,1,6,1,2,-5,-3,-4,-10,4,8,-3,-7,-6,-4,4,-3,-1,9,-4,-8,-7,-1,9,-2,7,6,8,9,-2,7,8,-5,10,10,6,4,-2,-6,6,6,2,5,5,4,-4,5,2,2,-3,5,-2,-5,-3,5,-3,-3,3,4,2,7,-10,10,2,5,6,-5,10,3,2,-1,1,9,1,-5,-3,1,-7,-9,-4,-4,-4,-9,10,-6,-1,5,-2,-9,-10,-6,-9,8,9,-4,-2,1,9,10,1,-2,-4,8,3,-9,-4,-8,3,8,3,-2,2,1,-3,-1,-7,-1,-1,-7,8,9,-2,-6,3,6,8,1,3,-1,2,-5,8,10,-6,-8,-6,10,-6,-4,10,6,-1,-10,-10,-3,5,-1,-5,-4,1,-7,9,-4,4,3,-1,-6,8,7,6,-10,9,6,2,4,4,-10,-1,-7,4,10,10,6,-9,6,4,-8,7,6,6,5,-3,2,-9,8,-10,9,-6,6,9,-3,-7,-5,-7,-6,-2,4,5,-9,6,10,-10,3,-5,1,2,6,-7,6,3,-10,4,-10,1,-5,-1,-10,-3,6,4,1,-3,5,-7,5,-4,5,-10,-7,6,-7,-7,7,2,10,-1,1,-8,-4,-7,5,6,9,6,-7,6,-9,-1,-4,10,-8,-5,-4,5,-7,1,-6,-3,2,-9,-2,-3,1,-9,-4,9,1,10,6,-7,8,7,4,-6,-7,-5,1,2,-1,-7,10,-8,-1,-8,2,1,3,3,-6,-4,-6,-2,7,9,4,3,-3,7,-9,-2,-10,2,-1,-9,-4,1,-1,6,-8,-8,-2,-6,-1,-10,8,3,7,1,10,6,-4,3,10,5,-4,-8,-3,-3,7,-7,7,3,5,3,-6,9,-4,5,-10,1,3,-10,4,-3,7,8,-1,-10,-4,2,-2,10,-3,-1,7,-9,-1,-9,4,-10,1,7,-8,10,1,-4,5,10,-10,1,3,8,-10,-1,-8,-7,6,2,-2,7,-4,-6,-6,-7,7,2,1,-4,-8,5,-3,-6,8,-4,-2,-4,6,7,8,6,3,7,-1,-5,5,4,4,-10,10,5,-7,-8,2,-4,-9,-8,-2,8,-8,-10,-5,-3,-6,3,7,6,6,-8,9,-9,-4,-5,-3,-10,6,-4,-6,-1,-1,6,10,-3,-10,-7,7,-9,4,-9,-7,-10,9,-3,2,-7,6,-3,9,-7,9,8,-9,-8,1,1,-6,-10,-4,2,-4,-1,4,1,9,2,1,5,9,4,-1,-7,-6,4,9,-8,-4,-7,2,-4,5,9,6,-7,-7,4,-8,7,-1,5,-6,6,3,-10,1,-6,-10,4,10,2,2,7,10,-5,-4,10,7,-2,9,-7,-8,9,-1,7,-4,-9,6,8,2,6,4,-10,3,-3,-5,-3,3,-2,-6,-6,-7,-7,-4,10,8,4,1,-5,5,7,8,5,-5,-8,6,-1,10,8,5,-10,4,-9,9,1,3,5,1,5,-9,-7,8,1,-6,-1,-9,-5,8,-9,-7,-2,10,2,-9,9,1,-4,2,6,-4,-10,-2,5,-9,7,-5,-8,6,8,10,-5,3,-9,-7,-4,2,6,-1,3,5,9,9,-7,-1,4,4,2,1,4,-4,8,6,-1,-5,10,4,-2,-9,2,7,1,5,1,-5,-3,5,7,5,8,-2,-2,8,-1,-2,-6,9,10,-3,10,-6,-6,-6,2,-1,-3,-1,-1,-8,5,-5,1,-10,-10,4,10,-4,-10,-1,2,-5,7,10,2,-10,2,-9,3,-3,-4,-2,-6,-3,5,-1,6,-3,-1,-10,-3,-1,10,-7,1,6,9,-2,-4,-3,8,7,-1,6,-3,4,-1,-10,-7,5,-9,3,-1,-2,9,6,-3,-1,3,-6,-6,-4,-7,7,3,10,-3,7,10,-8,9,8,9,8,-9,-2,-5,1,3,6,1,8,-10,9,8,-3,-3,1,-10,-6,3,3,4,-10,3,-3,-1,-10,5,5,9,10,-8,-6,10,-7,-9,1,-4,10,-8,-6,3,-1,7,4,3,10,7,-10,-5,9,7,7,2,3,-2,8,4,8,7,-9,-7,2,2,-10,8,3,9,7,1,1,8,1,-1,3,-10,-10,9,9,-5,10,-8,9,7,7,7,-1,9,6,10,10,2,-7,4,-4,-4,-2,-1,10,-6,-6,-6,7,1,-5,-3,-3,5,-5,7,-7,4,-5,-10,-3,-3,1,-7,5,2,-1,5,9,7,10,-1,-6,8,-2,-8,7,5,1,8,10,-7,6,-6,-5,-9,6,2,9,-3,8,-5,3,5,-1,-1,7,-1,-4,-10,-1,-2,10,-9,3,9,5,8,-5,-1,10,-7,-2,3,-9,-4,3,9,9,-4,4,-8,1,-5,3,-3,10,1,2,9,-9,2,-9,9,1,-2,9,3,6,-6,-6,3,3,-9,9,6,2,-4,-1,9,-8,-8,-3,-7,-9,-9,6,-10,-3,3,10,2,7,3,8,-1,-4,-3,10,-5,7,-3,-3,1,3,-10,1,-6,-7,-8,10,-1,-8,1,-6,-6,-8,5,1,9,-10,-10,-2,-1,3,6,-9,-10,-5,7,-7,6,10,-1,7,-9,-1,-10,-3,-4,2,-4,8,10,-6,7,-7,-1,2,2,-1,10,7,-5,-3,-1,-8,8,8,1,4,-7,9,-2,9,-2,-4,-2,-2,-3,3,-10,8,9,5,-10,-6,-1,-5,7,6,6,-2,3,3,-1,-2,7,10,-8,4,5,6,-6,-1,-7,-4,9,9,-2,-9,-9,5,-3,-2,1,10,7,-3,9,5,3,8,5,-5,2,-1,7,6,2,-2,3,10,9,4,7,1,1,3,9,-5,2,-1,-4,10,5,1,-5,10,4,2,-5,3,-4,-2,-2,1,4,4,9,6,-7,3,-7,8,7,3,2,-6,10,-7,-4,6,-10,-8,4,4,10,-5,-8,-6,-10,-7,-3,-9,2,5,4,-5,-4,7,6,9,-7,-1,-7,10,-6,-4,-1,-1,-8,-8,-10,9,4,1,-7,6,-7,9,-5,-5,-7,1,-9,10,1,-10,-10,6,-6,6,7,7,10,-2,-4,-8,-6,-8,3,4,7,6,6,-3,-9,6,-2,2,9,-9,-10,4,5,-3,-2,-10,-3,-8,8,-1,-2,-3,-2,-10,-10,3,-5,-10,-9,-7,-9,9,5,3,1,-2,-3,-1,3,-5,10,5,-3,4,-7,2,-9,-10,-10,-2,6,-6,-1,3,6,-7,6,-2,6,-10,8,-8,4,-5,-2,-5,-1,7,-6,5,8,10,3,-2,9,-1,5,8,-1,2,-10,-2,-6,4,-9,5,1,3,9,-5,7,-9,-7,-2,2,2,10,6,2,9,-8,-1,4,-5,9,-3,-5,-1,-1,-3,-6,6,8,4,-1,3,1,-8,-8,-8,-4,7,5,-4,-2,9,9,-6,7,-6,6,8,3,-2,1,-2,-1,6,9,-4,6,-1,-1,3,8,6,1,1,2,-7,-3,9,9,2,5,1,9,8,8,10,3,9,-2,7,6,-8,-6,5,-2,5,4,1,-5,-3,-2,-8,1,-6,8,6,9,2,-2,-3,5,6,-4,-3,5,4,1,2,-9,-4,4,-10,-7,-10,-1,-5,-9,-6,-5,-3,-6,-10,7,10,2,3,-7,9,-7,-1,2,-5,-5,5,9,-4,5,4,8,9,10,-4,-7,1,3,-2,-9,9,7,6,4,-5,-6,2,-4,1,-7,3,1,-9,5,1,-8,8,4,5,5,-6,10,-4,1,2,-2,1,8,-8,-1,7,-9,9,2,-1,6,8,5,4,-9,3,1,5,-4,-4,-3,-6,-9,-6,-9,-8,4,2,-7,-5,-5,8,-2,5,9,1,-2,4,10,-10,9,-5,-3,-4,5,9,-8,6,-3,8,-2,-1,3,-8,9,3,6,-1,-9,3,4]], dtype = "int16")#candidate|2521|(1, 1575)|const|int16
call_2519 = relay.TupleGetItem(func_2073_call(relay.reshape(const_2520.astype('uint8'), [6, 1, 13]), relay.reshape(const_2521.astype('int16'), [1575,]), ), 5)
call_2522 = relay.TupleGetItem(func_2076_call(relay.reshape(const_2520.astype('uint8'), [6, 1, 13]), relay.reshape(const_2521.astype('int16'), [1575,]), ), 5)
var_2524 = relay.var("var_2524", dtype = "int16", shape = (14, 1575))#candidate|2524|(14, 1575)|var|int16
bop_2525 = relay.minimum(const_2521.astype('uint64'), var_2524.astype('uint64')) # shape=(14, 1575)
func_2399_call = mod.get_global_var('func_2399')
func_2400_call = mutated_mod.get_global_var('func_2400')
call_2529 = relay.TupleGetItem(func_2399_call(), 2)
call_2530 = relay.TupleGetItem(func_2400_call(), 2)
var_2533 = relay.var("var_2533", dtype = "uint64", shape = (14, 1575))#candidate|2533|(14, 1575)|var|uint64
bop_2534 = relay.floor_mod(bop_2525.astype('float32'), relay.reshape(var_2533.astype('float32'), relay.shape_of(bop_2525))) # shape=(14, 1575)
output = relay.Tuple([bop_2514,call_2519,const_2520,call_2529,bop_2534,])
output2 = relay.Tuple([bop_2514,call_2522,const_2520,call_2530,bop_2534,])
func_2540 = relay.Function([var_2512,var_2513,var_2524,var_2533,], output)
mod['func_2540'] = func_2540
mod = relay.transform.InferType()(mod)
var_2541 = relay.var("var_2541", dtype = "float32", shape = (5, 4, 11))#candidate|2541|(5, 4, 11)|var|float32
var_2542 = relay.var("var_2542", dtype = "float32", shape = (5, 4, 11))#candidate|2542|(5, 4, 11)|var|float32
var_2543 = relay.var("var_2543", dtype = "int16", shape = (14, 1575))#candidate|2543|(14, 1575)|var|int16
var_2544 = relay.var("var_2544", dtype = "uint64", shape = (14, 1575))#candidate|2544|(14, 1575)|var|uint64
output = func_2540(var_2541,var_2542,var_2543,var_2544,)
func_2545 = relay.Function([var_2541,var_2542,var_2543,var_2544,], output)
mutated_mod['func_2545'] = func_2545
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2570 = relay.var("var_2570", dtype = "uint32", shape = (16, 2, 12))#candidate|2570|(16, 2, 12)|var|uint32
const_2571 = relay.const([[[4,-7,6,3,-2,5,-3,-6,4,3,-4,-4],[-3,-3,-7,6,-5,-8,-7,-9,2,-8,4,4]],[[-6,5,9,6,-8,-5,-2,-10,-6,-7,9,-3],[-1,-8,4,4,10,-1,-9,-10,-6,3,8,6]],[[-4,-6,-9,6,9,-7,-7,-3,8,-5,-3,-5],[-2,6,4,3,-4,-4,9,5,5,8,-2,-10]],[[-7,1,-10,6,5,-1,5,-8,6,-6,-2,-10],[4,3,-1,10,8,5,-6,-9,4,-1,-7,-1]],[[-10,5,-7,-1,4,-9,-4,2,-10,9,9,-8],[-1,3,-5,10,-1,-7,3,1,1,2,-9,-7]],[[-1,-7,-8,3,-2,-9,3,4,8,4,1,-9],[-5,8,-3,-5,5,5,6,5,6,-7,-7,3]],[[-4,7,2,6,4,3,10,4,-9,9,8,-5],[7,-3,5,-10,-3,-2,10,4,1,5,-5,-5]],[[1,2,-7,4,-9,8,1,2,-4,10,-2,10],[-4,-7,6,-5,-5,6,6,-7,5,10,3,1]],[[-6,-3,-7,-4,-10,2,-2,-4,-6,2,-8,-8],[4,10,-9,5,4,-6,3,-6,10,10,4,2]],[[4,-3,-10,-7,10,2,-10,5,-6,-9,-10,3],[-10,3,-7,-8,-8,5,-4,10,2,5,10,-8]],[[-2,7,-9,-3,3,6,10,3,5,-6,4,4],[10,10,9,10,6,-3,-8,-5,-2,-5,3,2]],[[7,8,6,9,-3,-9,6,4,-5,-6,-3,7],[2,-2,9,-4,2,10,-7,-5,6,1,-1,6]],[[3,-2,3,-4,9,-1,-9,-7,-8,-10,-3,-3],[1,3,-2,2,10,-2,1,-9,9,1,4,9]],[[-4,-7,6,-8,-8,10,1,-5,-6,-6,-10,-9],[5,-9,7,-3,8,10,1,-4,-10,-1,6,1]],[[-1,-9,2,-4,-8,-7,2,8,9,-8,7,-1],[6,-7,8,-4,-5,-1,-9,-3,9,-3,-10,-5]],[[-2,-1,-4,-7,4,5,-2,-10,10,-3,10,7],[7,-2,-5,-8,-1,8,-9,8,-9,-5,1,-7]]], dtype = "uint32")#candidate|2571|(16, 2, 12)|const|uint32
bop_2572 = relay.logical_xor(var_2570.astype('uint32'), relay.reshape(const_2571.astype('uint32'), relay.shape_of(var_2570))) # shape=(16, 2, 12)
output = bop_2572
output2 = bop_2572
func_2580 = relay.Function([var_2570,], output)
mod['func_2580'] = func_2580
mod = relay.transform.InferType()(mod)
var_2581 = relay.var("var_2581", dtype = "uint32", shape = (16, 2, 12))#candidate|2581|(16, 2, 12)|var|uint32
output = func_2580(var_2581)
func_2582 = relay.Function([var_2581], output)
mutated_mod['func_2582'] = func_2582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2399_call = mod.get_global_var('func_2399')
func_2400_call = mutated_mod.get_global_var('func_2400')
call_2598 = relay.TupleGetItem(func_2399_call(), 2)
call_2599 = relay.TupleGetItem(func_2400_call(), 2)
uop_2609 = relay.tan(call_2598.astype('float32')) # shape=(132, 2)
uop_2611 = relay.tan(call_2599.astype('float32')) # shape=(132, 2)
func_2410_call = mod.get_global_var('func_2410')
func_2411_call = mutated_mod.get_global_var('func_2411')
call_2622 = relay.TupleGetItem(func_2410_call(), 0)
call_2623 = relay.TupleGetItem(func_2411_call(), 0)
func_1928_call = mod.get_global_var('func_1928')
func_1931_call = mutated_mod.get_global_var('func_1931')
var_2627 = relay.var("var_2627", dtype = "bool", shape = (1080,))#candidate|2627|(1080,)|var|bool
var_2628 = relay.var("var_2628", dtype = "int16", shape = (15, 105))#candidate|2628|(15, 105)|var|int16
call_2626 = relay.TupleGetItem(func_1928_call(relay.reshape(var_2627.astype('bool'), [10, 9, 12]), relay.reshape(var_2628.astype('int16'), [105, 15]), ), 1)
call_2629 = relay.TupleGetItem(func_1931_call(relay.reshape(var_2627.astype('bool'), [10, 9, 12]), relay.reshape(var_2628.astype('int16'), [105, 15]), ), 1)
output = relay.Tuple([uop_2609,call_2622,call_2626,var_2627,var_2628,])
output2 = relay.Tuple([uop_2611,call_2623,call_2629,var_2627,var_2628,])
func_2632 = relay.Function([var_2627,var_2628,], output)
mod['func_2632'] = func_2632
mod = relay.transform.InferType()(mod)
var_2633 = relay.var("var_2633", dtype = "bool", shape = (1080,))#candidate|2633|(1080,)|var|bool
var_2634 = relay.var("var_2634", dtype = "int16", shape = (15, 105))#candidate|2634|(15, 105)|var|int16
output = func_2632(var_2633,var_2634,)
func_2635 = relay.Function([var_2633,var_2634,], output)
mutated_mod['func_2635'] = func_2635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2198_call = mod.get_global_var('func_2198')
func_2199_call = mutated_mod.get_global_var('func_2199')
call_2662 = relay.TupleGetItem(func_2198_call(), 0)
call_2663 = relay.TupleGetItem(func_2199_call(), 0)
func_166_call = mod.get_global_var('func_166')
func_169_call = mutated_mod.get_global_var('func_169')
const_2669 = relay.const([-4.518631,1.131807,1.672025,-2.320397,-2.217707,-4.615874,-8.523856,6.567312,0.514519,-1.107576,-8.941673,7.599930,-3.156647,-9.189320,-7.092986,-2.198367,-4.926757,-4.293798,8.768885,9.289709,6.713654,2.547905,-6.647767,-4.092330,-2.637704,9.476987,-5.188912,-7.761945,3.945850,1.144846,-9.735949,6.428786,0.798744,0.833428,-0.685341,-4.386142,-8.770086,6.465007,-4.481594,7.432303,-3.817027,4.160942,8.378873,-3.692198,2.928866,-0.346553,3.181109,-6.051547,1.029001,-8.434393,-2.984492,4.340617,-0.690408,5.123336,-4.398681,6.642474,0.015252,-2.824328,-9.772352,8.379070,-5.135002,4.171939,3.677065,-3.434310,0.985404,-1.541453,9.260419,3.551567,0.333250,-3.795413,3.684808,-7.335630,-6.615652,1.063158,7.154174,-5.692032,-7.772011,-5.385278,1.277674,4.730696,4.102834,-1.386779,9.925459,-7.811052,-1.062418,3.651838,-5.883199,-4.224949,-4.996001,3.943814,9.124637,2.922168,9.841655,7.379660,-6.427191,-0.189067,1.353668,-4.600084,-9.756505,7.393802,7.067065,-6.994354,-6.901860,-5.201318,-5.819886,0.068489,-4.462290,4.559264,-9.673962,-8.715344,3.745697,-3.296598,-6.712115,-9.548201,7.226278,7.804609,-2.920629,-9.203687,9.516172,1.674558,-3.636697,3.900693,4.952839,-6.012015,1.069587,-4.933184,1.845389,6.613515,9.422403,-7.841985,0.951120,7.352448,7.103564,1.323951,-3.373516,-4.890731,2.609484,7.754254,2.568924,-5.318811,9.106897,3.590779,1.002114,-3.187584,-0.357325,0.858593,-6.931256,5.522759,-0.340346,-2.572638,4.605149,8.449717,-6.237908,4.893597,-9.075576,5.473965,-1.593994,8.930514,7.749603,-1.611906,-4.148327,-7.003596,-0.919879,3.429489,-4.251619,-3.827576,-4.375105,-6.540632,-7.015827,-5.348018,1.348178,-4.462420,4.555008,1.720327,2.407184,-5.572583,7.890446,4.061723,0.454984,-9.215528,-8.442999,3.070529,-3.924225,-9.459338,-4.181998,9.910640,-6.202856,2.416000,6.811710,-5.681141,4.150808,0.488191,4.671700,-8.611282,1.590210,-2.167543,7.830789,-6.210507,6.813206,8.582599,-0.560200,7.862089,-3.487864,-3.378330,1.600709,9.745464,4.193577,8.480246,9.520599,4.510044,-2.104839,-6.703412,-7.701793,8.355585,5.678533,2.941655,-8.622874,-3.555918,0.331810,-0.425290,-3.512990,8.184786,-8.310552,-9.713822,7.316146,-1.182417,-1.763888,1.345161,-1.399972,-9.441186,6.886843,5.132228,4.091228,9.761044,-8.120427,7.998039,3.139981,-7.352208,-9.546560,0.100757,8.418782,7.930750,-6.090791,-9.668914,-6.751071,4.571126,-7.013056,3.658168,-2.911999,-7.545964,-2.421088,2.668078,2.459593,-9.872053,1.255511,8.467027,2.272973,-6.603801,1.213558,-5.390770,8.429924,-3.840710,-7.711537,1.068592,-7.324577,0.232122,-1.855894,-4.051703,4.045702,7.494989,-2.815851,3.404860,3.971449,4.874586,-7.274108,-7.824219,5.364223,5.317840,-7.050855,8.825144,-4.037061,-0.791959,7.653071,-9.639975,0.483359,2.026655,-6.030071,9.537043,-0.231843,0.171201,3.691425,6.598735,-2.436040,-2.782514,0.209134,0.480796,6.307115,-9.690258,-5.788785,8.955435,-9.273856,9.953043,4.690180,7.292925,1.724788,-9.916162,-3.441305,-6.062802,-4.393821,-8.063819,-8.735669,0.209207,1.239751,-6.015015,0.025240,6.513395,6.070573,-2.680143,4.697119,-4.228027,-0.333280,5.566719,-4.845995,5.858961,4.413121,9.859580,5.465325,8.298635,-7.743885,-8.748640,7.621262,-3.361076,-7.503086,3.438895,-5.101960,6.413192,-1.128425,7.763275,-0.143147,9.394330,-2.441416,0.849726,4.773863,-9.374264,-0.252393,7.081431,-6.090086,-4.969458,3.858217,7.394653,-5.108915,-3.369668,9.735468,2.771248,2.580795,6.103922,9.641641,0.634276,2.657748,4.537404,8.794589,5.701682,-8.859251,-7.119327,6.482582,5.952096,-7.564207,-5.096461,3.024994,7.442575,-4.611091,9.613534,8.504237,5.941846,-8.208403,6.095872,6.169604,-2.074743,-5.258001,5.087073,-1.014186,5.263816,6.198355,-8.735240,-5.537143,2.128850,2.654245,-3.765506,0.436141,8.550967,-3.206689,5.750934,-0.241261,7.750802,8.475124,-8.560504,4.777536,-5.782589,-2.403697,-9.662982,1.141692,9.162083,-0.779206,0.940277,5.266593,3.158904,2.559620,-3.801629,-3.973805,1.166109,-9.738413,2.496814,0.900762,-6.932040,0.977662,-2.728563,-5.936074,3.839680,-2.077934,7.211783,0.031184,6.772071,5.847565,-7.482873,-8.976459,3.784015,-1.641996,-3.549832,8.749827,8.917485,4.819297,5.462407,4.036771,-7.338951,2.433323,-7.760538,5.069469,-5.497992,7.378240,-6.035667,-4.691995,-4.040848,1.710617,-3.708431,-4.868037,0.438247,-1.176506,0.482114,1.039029,7.636425], dtype = "float32")#candidate|2669|(450,)|const|float32
call_2668 = func_166_call(relay.reshape(const_2669.astype('float32'), [5, 6, 15]))
call_2670 = func_166_call(relay.reshape(const_2669.astype('float32'), [5, 6, 15]))
bop_2674 = relay.subtract(const_2669.astype('int8'), relay.reshape(call_2668.astype('int8'), relay.shape_of(const_2669))) # shape=(450,)
bop_2677 = relay.subtract(const_2669.astype('int8'), relay.reshape(call_2670.astype('int8'), relay.shape_of(const_2669))) # shape=(450,)
output = relay.Tuple([call_2662,bop_2674,])
output2 = relay.Tuple([call_2663,bop_2677,])
func_2683 = relay.Function([], output)
mod['func_2683'] = func_2683
mod = relay.transform.InferType()(mod)
mutated_mod['func_2683'] = func_2683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2683_call = mutated_mod.get_global_var('func_2683')
call_2684 = func_2683_call()
output = call_2684
func_2685 = relay.Function([], output)
mutated_mod['func_2685'] = func_2685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2683_call = mod.get_global_var('func_2683')
func_2685_call = mutated_mod.get_global_var('func_2685')
call_2753 = relay.TupleGetItem(func_2683_call(), 0)
call_2754 = relay.TupleGetItem(func_2685_call(), 0)
func_2302_call = mod.get_global_var('func_2302')
func_2304_call = mutated_mod.get_global_var('func_2304')
const_2759 = relay.const([-2.340292,-7.319826,7.882558,7.231324,-5.863884,6.300863,-8.500246,-0.333685,7.573084,8.015729,9.089586,-4.654276,4.700817,8.577254,-1.623278,1.687479,5.840947,-9.483723,-8.033505,-8.084509,-1.900673,1.383509,-2.799430,-3.792244,2.465233,-6.750550,-5.037763,-9.648753,-5.872632,9.163554,0.505929,6.473685,-1.442535,7.594926,7.145004,8.820963,1.033706,-4.462284,7.327826,-2.111374,9.966801,7.547855,6.044415,5.239909,2.934888,-7.162378,0.209028,5.682482,8.218042,1.876815,-0.188774,4.287480,5.923808,-5.267918,-7.485174,3.413831,1.834675,-2.723530,8.604282,-7.180732,-2.201737,8.492083,2.510803,3.524397,7.322896,1.084459,6.144408,-7.756864,2.358827,9.909255,0.605426,4.261953,1.071646,7.895798,9.642546,-0.510504,-4.591946,3.047080,-6.869408,-1.756639,5.680344,-8.307455,-9.168512,6.868004,5.925479,-5.094866,-4.567230,5.915072,6.806316,-0.544516,5.650780,-6.182282,-5.444477,6.426705,-4.534964,-8.603345,8.469108,-4.428783,1.205278,5.789388,4.084447,3.718662,8.679724,7.273590,6.736610,4.389390,-7.434336,-9.789513,-9.089400,-7.564947,-2.760853,-9.337117,2.869600,8.781747,2.521162,0.531399,-7.301690,-2.077403,8.111770,-8.509424,8.409198,8.621368,0.744842,-9.303376,1.695112,-8.787279,6.371418,-9.552835,-2.224157,-5.577109,-5.188393,-0.546992,-4.303000,8.386360,-2.720670,9.840308,2.212192,-3.017275,-1.081087,-3.933929,3.061954,2.703566,-3.933177,7.462870,-7.477951,-6.993483,6.516459,1.720239,7.197142,9.904620,6.973776,6.674902,-4.830761,8.533067,-8.871508,-7.162802,9.759383,-9.953103,3.737794,-3.667734,4.560202,5.715431,7.376176,6.149808,2.216947,-5.283188,0.300995,1.043310,2.244369,-8.552129,3.974971,7.372938,9.481748,-0.589555,9.860438,-9.640795,2.026264,1.386238,-5.160413,2.321797,-7.553689,-9.362894,8.488663,8.985451,2.707921,-5.452931,-6.345141,6.457511,3.293596,8.525307,-1.655650,-0.141002,6.130121,-6.698075,-7.390914,3.959586,5.329538,-5.280848,5.071887,-5.344422,1.987242,9.732501,-9.375536,3.077615,-6.713112,8.328017,-7.556366,-4.419245,0.464273,-3.263918,-4.146706,-7.014658,3.020073,-3.339740,-8.049868,4.723683,1.815273,-1.769790,5.983404,-3.321424,-3.368707,-6.648491,8.847723,-1.386163,3.115045,-1.303697,-9.399280,-4.555734,6.193100,-2.564474,7.456177,4.937005,9.345254,-1.531158,-9.870559,-5.654152,-6.101474,4.581293,-5.347992,9.526681,-4.986585,6.566812,-9.236338,1.862940,5.013154,-2.036523,5.598413,4.886855,6.353031,-0.332648,-2.574263,-2.544175,7.022277,-3.232002,9.964744,-5.855701,0.580360,-1.613619,7.395878,1.835559,0.421757,7.222598,-9.627721,0.216159,-3.897489,6.007148,0.269344,-6.386302,3.102940,-0.553953,-5.938465,6.059630,-5.340132,9.064875,9.572040,-3.165389,-5.663253,7.101866,7.277743,-4.520007,-3.583524,-0.945747,4.402510,3.383466,-6.575185,8.647484,-2.113357,-3.049679,-0.409845,-4.223464,0.996017,7.554923,-0.120890,-9.250155,3.364155,0.420117,-6.756176,1.402797,-4.905138,-2.979865,-0.888580,5.335571,-0.258244,-6.273085,-1.457953,-3.094618,4.083942,9.076941,9.174713,0.945534,1.007316,-8.783769,1.504284,3.908343,-8.752547,-3.873227,-7.851799,5.813052,9.609058,1.929675,-7.164885,9.761830,4.574754,1.065931,-7.714114,-3.341251,-2.872287,6.358422,-9.660921,3.875636,5.112782,-7.705114,-8.592419,-6.683454,9.428831,6.050546,-1.979475,3.876937,5.688063,-5.170052,-8.522363,8.767127,2.162446,-5.135562,-8.673568,9.950177,2.162693,4.843157,0.633516,0.785000,8.967177,7.943759,-4.034277,-7.742886,3.262283,8.464675,0.279870,-5.253232,-5.307986,-3.582216,9.315705,-9.074060,0.327630,-8.522654,8.638568,4.557949,-2.755842,-7.017178,-0.702692,-0.918077,1.960290,3.602813,9.106711,-5.886107,-6.851718,-3.777806,-3.062308,-0.551195,-0.964439,-9.692579,-3.162366,-2.804598,-0.196997,0.835766,3.214210,1.669169,-8.468624,9.689915,-8.845767,2.880963,1.675474,-4.406012,-5.880007,8.058216,3.534953,-2.329573,-4.741823,-5.708299,-7.334886,2.691891,-1.241175,-5.994502,8.017055,-4.162270,3.008263,-3.289802,2.442570,-3.463613,4.050156,-2.547904,-6.500841,-7.990642,5.193465,1.596933,5.187817,-7.952259,6.012229,-2.935142,-9.631752,1.399699,-2.797518,-9.324187,-8.183074,3.195388,5.227712,3.357202,-0.868503,-9.070372,-9.105570,3.171084,-1.947842,6.329422,5.083589,-9.427291,-5.495241,5.665130,9.603436,-1.740741,7.244991,0.378979,8.869473,-3.549017,-9.349625,-7.769737,-2.172552,-4.521503,8.522653,4.929332,3.045006,-2.773517,2.803596,-1.188155,-1.857026,-5.086757,-6.359405,-2.715586,-2.536936,-4.018530,7.492441,-2.583676,-1.581860,-5.205289,-7.603881,-2.749361,0.327746,-6.463293,9.474934,9.314083,1.952896,7.558745,4.397891,-6.443245,-8.514453,-0.159598,1.706242,6.899639,-3.625397,5.781989,2.806258,-1.658748,-0.386662,3.414507,-8.527514,4.914798,1.554415,3.038180,-7.291408,-4.557131,-1.719815,-8.841493,1.532329,-8.070438,1.386110,3.878906,2.335924,0.049768,-3.324474,6.390993,6.956674,-6.613329,4.206728,9.331799,4.006405,-8.182960,1.165617,9.771329,3.720936,-7.906311,3.983660,7.181354,7.387617,9.586896,-7.150830,-2.148935,3.841502,-7.673425,2.450865,1.357977,9.302415,-1.486088,-0.693591,-0.232502,6.576998,7.563367,-5.979573,-8.378432,7.043653,8.503175,-2.402487,-4.687657,-6.564535,3.914299,-2.162366,7.453426,-0.183586,-8.852060,6.870073,-9.012937,1.601144,-6.382401,9.433892,-5.485888,-9.487135,-7.427470,7.893036,-7.359849,7.077769,4.821868,-2.085445,0.176054,8.499710,-5.914536,-9.306803,3.721673,-0.132414,5.271296,-1.215496,-4.980179,2.866317,-9.979645,0.472099,9.009080,-3.004036,6.592275,8.327721,2.008821,-1.031433,6.515169,5.353423,6.082993,-5.751670,4.927543,-0.437770,3.484955,-7.920005,-0.251449,4.111889,-0.638814,6.960861,-1.420933,-1.947394,8.934302,0.305478,-0.299227,0.377676,-6.483363,-9.033718,2.887552,-2.552708,3.287796,-6.684872,-9.710388,7.552812,4.545710,-6.058358,5.176492,3.599913,-2.472168,1.057130,7.231102,-7.679874,4.435701,4.100842,8.676922,4.034248,-1.908689,-4.685868,6.877497,3.632110,-0.550395,4.362763,1.410231,-9.412201,8.542472,-4.432752,4.789467,5.124050,8.276298,2.446985,-8.226064,2.883984,-3.235256,9.342872,7.260233,-2.810916,3.001133,2.094346,-2.072461,-3.349297,-3.175693,3.563467,7.133260,-7.499924,7.596527,2.920820,-8.064788,5.363487,-7.766457,7.456574,4.155789,-6.570119,2.929223,5.191185,3.511507,1.530245,-1.421209,3.230830,9.551775,8.074271,9.419290,-7.200936,7.389654,-5.978878,1.494407,-0.094609,7.436971,3.474123,-0.005121,9.523007,-5.577213,9.905339,4.102020,-1.048195,-3.229251,7.686255,-5.596543,-6.972541,3.015723,2.097340,-4.384923,-9.062083,-8.099324,-9.781472,-8.594543,1.754151,-3.028290,-3.404448,0.414727,0.155048,-0.437523,-9.499227,-3.285144,-9.399456,8.893324,-2.375446,1.127408,-5.053351,-6.724620,9.247935,-6.121231,7.103902,7.043745,-8.912487,-2.994425,2.014064,-2.128978,7.544844,-1.445137,0.098764,-1.982405,3.473121,-2.932693,8.071689,-7.772123,3.137932,0.122994,9.031434,-8.720377,-2.956915,5.702499,7.087262,1.786207,3.893424,8.100236,5.572454,-7.357796,1.924494,-4.967659,-8.870228,9.273652,9.954414,-1.882666,-6.589062,-9.748437,-5.444381,-6.640653,-8.464980,-7.392798,9.586867,-8.199429,8.429790,3.110634,2.722490,-6.262624,-6.723602,6.864202,-9.966943,-7.073996,0.412734,0.608678,5.612575,9.738929,5.279887,5.248120,8.962182,-8.538856,-5.458405,-5.947975,3.241477,2.336516,-0.805085,-7.510892,3.517978,5.861342,9.209930,-3.938418,-8.321241,-9.028853,7.259489,-9.927372,7.036829,-5.497377,-8.772070,5.694497,4.255907,5.954016,-9.027713,-2.160598,1.662755,-2.864725,9.633538,3.282687,-0.847303,8.342377,9.404734,7.683296,-2.496552,-6.203731,-7.369401,4.040381], dtype = "float32")#candidate|2759|(780,)|const|float32
call_2758 = relay.TupleGetItem(func_2302_call(relay.reshape(const_2759.astype('float32'), [6, 10, 13])), 0)
call_2760 = relay.TupleGetItem(func_2304_call(relay.reshape(const_2759.astype('float32'), [6, 10, 13])), 0)
output = relay.Tuple([call_2753,call_2758,const_2759,])
output2 = relay.Tuple([call_2754,call_2760,const_2759,])
func_2765 = relay.Function([], output)
mod['func_2765'] = func_2765
mod = relay.transform.InferType()(mod)
mutated_mod['func_2765'] = func_2765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2765_call = mutated_mod.get_global_var('func_2765')
call_2766 = func_2765_call()
output = call_2766
func_2767 = relay.Function([], output)
mutated_mod['func_2767'] = func_2767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2683_call = mod.get_global_var('func_2683')
func_2685_call = mutated_mod.get_global_var('func_2685')
call_2772 = relay.TupleGetItem(func_2683_call(), 1)
call_2773 = relay.TupleGetItem(func_2685_call(), 1)
output = relay.Tuple([call_2772,])
output2 = relay.Tuple([call_2773,])
func_2791 = relay.Function([], output)
mod['func_2791'] = func_2791
mod = relay.transform.InferType()(mod)
mutated_mod['func_2791'] = func_2791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2791_call = mutated_mod.get_global_var('func_2791')
call_2792 = func_2791_call()
output = call_2792
func_2793 = relay.Function([], output)
mutated_mod['func_2793'] = func_2793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2791_call = mod.get_global_var('func_2791')
func_2793_call = mutated_mod.get_global_var('func_2793')
call_2817 = relay.TupleGetItem(func_2791_call(), 0)
call_2818 = relay.TupleGetItem(func_2793_call(), 0)
uop_2824 = relay.sigmoid(call_2817.astype('float64')) # shape=(450,)
uop_2826 = relay.sigmoid(call_2818.astype('float64')) # shape=(450,)
bop_2854 = relay.not_equal(call_2817.astype('bool'), relay.reshape(uop_2824.astype('bool'), relay.shape_of(call_2817))) # shape=(450,)
bop_2857 = relay.not_equal(call_2818.astype('bool'), relay.reshape(uop_2826.astype('bool'), relay.shape_of(call_2818))) # shape=(450,)
output = bop_2854
output2 = bop_2857
func_2858 = relay.Function([], output)
mod['func_2858'] = func_2858
mod = relay.transform.InferType()(mod)
output = func_2858()
func_2859 = relay.Function([], output)
mutated_mod['func_2859'] = func_2859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2858_call = mod.get_global_var('func_2858')
func_2859_call = mutated_mod.get_global_var('func_2859')
call_2896 = func_2858_call()
call_2897 = func_2858_call()
output = call_2896
output2 = call_2897
func_2909 = relay.Function([], output)
mod['func_2909'] = func_2909
mod = relay.transform.InferType()(mod)
output = func_2909()
func_2910 = relay.Function([], output)
mutated_mod['func_2910'] = func_2910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2399_call = mod.get_global_var('func_2399')
func_2400_call = mutated_mod.get_global_var('func_2400')
call_2947 = relay.TupleGetItem(func_2399_call(), 1)
call_2948 = relay.TupleGetItem(func_2400_call(), 1)
func_2632_call = mod.get_global_var('func_2632')
func_2635_call = mutated_mod.get_global_var('func_2635')
const_2953 = relay.const([True,True,True,False,False,True,False,True,True,True,True,False,True,True,True,True,False,True,True,False,False,False,False,True,False,True,False,True,True,False,True,True,False,True,True,False,False,True,False,True,True,True,True,False,False,True,True,False,False,False,True,False,False,True,True,False,True,True,False,False,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,False,False,True,False,False,True,False,False,True,True,True,False,True,True,False,True,True,False,True,False,False,False,True,True,True,False,True,False,True,False,False,True,False,False,True,False,True,False,True,False,True,False,True,True,True,True,False,False,True,True,False,True,False,True,False,True,True,False,True,True,False,False,False,False,False,False,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,False,True,False,False,False,True,True,False,False,False,False,False,True,False,False,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,True,False,True,False,True,True,True,False,False,False,True,False,False,False,True,True,True,False,False,True,True,True,False,True,False,True,False,True,False,True,False,True,False,False,True,True,True,True,False,True,True,True,True,True,True,False,False,False,False,True,True,False,False,False,True,True,True,True,False,True,False,True,False,False,True,False,False,False,True,False,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,True,True,False,True,False,False,False,False,True,True,False,True,True,True,True,True,False,False,False,False,False,True,False,False,True,False,False,True,False,False,False,True,True,False,False,True,True,True,False,False,False,False,True,False,False,False,True,False,False,True,False,False,False,False,False,False,False,True,True,False,True,False,True,True,False,False,False,True,True,False,True,True,True,False,True,True,False,False,True,False,True,True,False,False,True,True,False,False,False,True,False,True,True,False,False,False,False,True,True,True,True,True,False,False,True,False,True,False,False,False,False,False,True,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,True,False,False,False,True,True,True,True,True,False,True,True,True,True,True,False,False,True,True,False,True,False,False,True,False,False,False,True,False,True,True,True,True,True,True,True,False,False,False,True,True,True,True,False,False,False,False,True,False,False,True,True,False,False,False,False,False,False,False,False,True,True,True,True,False,False,False,True,True,False,False,False,True,True,False,True,False,False,False,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,True,True,True,True,False,False,True,False,False,False,False,False,True,False,True,False,False,True,False,True,False,False,True,False,False,False,True,False,False,False,True,True,True,False,False,True,True,True,True,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,True,False,False,False,False,False,False,True,True,True,False,True,False,True,False,False,False,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,False,False,False,False,True,True,False,False,False,False,False,True,True,False,True,True,False,False,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,True,True,True,False,True,True,False,True,True,True,False,False,False,False,False,True,False,False,False,True,False,False,True,False,False,True,True,True,False,False,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,False,True,True,True,True,False,False,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,True,True,False,False,False,True,True,True,True,True,False,False,True,True,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,True,True,False,False,True,False,True,False,True,False,True,False,False,True,True,True,False,False,False,False,False,False,True,False,True,True,True,True,False,False,False,True,True,False,False,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,False,False,False,True,False,True,True,False,False,True,False,False,True,True,False,True,False,False,False,False,True,True,True,True,False,True,False,False,False,True,False,False,True,True,False,False,False,True,False,True,False,False,True,True,True,False,False,False,False,False,False,False,True,True,True,True,False,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,True,False,True,True,False,False,False,True,False,True,False,True,True,True,True,False,True,False,True,True,False,True,True,False,False,True,False,False,False,False,False,False,True,True,True,True,False,False,True,False,True,True,True,False,False,True,True,True,True,False,False,True,False,True,False,False,False,False,False,True,True,False,True,False,False,False,True,False,False,False,False,True,False,True,False,False,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,False,True,True,True,True,True,False,False,True,False,True,False,True,True,False,True,False,False,True,False,False,False,False,False,True,False,True,True,False,True,False,False,False,True,True,True,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,True,True,False,True,False,False,True,True,False,False,False,False,False,True,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True,False,False,False,True,False,True,True], dtype = "bool")#candidate|2953|(1080,)|const|bool
const_2954 = relay.const([6,-5,5,-5,-8,-3,-7,-1,7,6,5,3,9,9,6,5,-3,2,8,-8,10,-3,6,-9,7,10,7,-5,5,-2,-1,7,-7,3,8,10,-5,-6,9,5,5,8,-1,6,7,8,-5,4,-6,7,-10,-6,2,-7,-1,6,8,-6,7,6,2,-5,-1,-8,6,2,2,3,2,-6,-2,9,-8,-10,8,10,10,-4,-4,7,-8,6,-9,-4,8,-5,2,-2,-8,-5,8,6,-1,-6,-3,-5,-6,-10,1,-7,6,9,8,10,4,4,-3,10,1,8,-1,-4,5,1,2,7,3,-7,9,-9,-3,7,-3,9,-4,-7,-2,-3,7,-7,5,-8,-1,-1,2,-7,3,10,-2,-10,-6,3,-8,-8,-2,5,-8,8,-7,2,-7,4,-3,-5,-3,-1,-2,8,-5,-4,-1,6,1,9,-1,7,7,9,6,-5,1,-10,4,-10,6,6,2,-7,6,-10,6,-6,-9,-5,2,-3,-7,3,-1,-10,8,2,-10,4,-6,4,10,-7,6,3,1,9,9,1,7,-4,-9,-7,-9,6,5,-7,9,-5,5,1,4,-4,-3,2,10,9,4,10,-6,7,4,8,8,-8,-1,-9,-10,7,-9,5,5,-9,-1,10,-5,9,-3,-3,-10,3,10,6,6,5,-2,-5,6,6,4,5,7,9,2,-2,-4,4,9,-6,-5,10,-3,6,8,-5,2,-2,-5,-10,4,9,-8,-6,5,2,4,7,5,-7,9,-5,-1,9,-7,-2,10,-1,-6,-5,-8,9,7,9,3,-8,7,3,-2,7,1,2,-3,-10,-9,-8,-2,-1,6,2,8,-2,-3,7,5,-5,-3,8,10,-3,-2,10,-9,-2,2,4,4,-9,9,4,-7,-10,8,6,-5,8,1,1,8,-7,-7,-4,-7,2,8,9,7,-8,9,-2,5,2,-10,10,-4,2,-7,6,9,7,-4,-3,-8,-5,-6,-1,-10,9,-8,8,5,5,6,4,-7,-3,9,-1,8,4,-4,-7,2,4,6,-1,-2,2,8,-5,7,10,-5,-5,-9,-9,5,-7,5,-6,5,-1,-6,7,9,2,10,-3,3,2,-6,4,8,-2,-5,3,8,9,6,-9,-7,-2,1,6,3,5,-6,5,-2,-8,-5,-9,4,6,-1,7,-6,-7,-4,2,-8,9,3,1,-10,4,-7,-10,-8,-2,-3,-9,6,7,-8,9,3,-3,3,4,2,-1,-1,-1,-9,-10,-10,1,-4,7,-7,-1,6,9,-9,-7,2,-9,8,4,2,10,-2,1,-9,-1,7,-9,7,4,-4,4,-8,-1,-4,6,8,2,-6,7,1,4,-9,1,-2,1,-8,1,9,-4,6,2,5,5,5,7,-1,4,-5,-7,1,-2,-4,-3,-5,-7,7,9,3,3,8,-4,2,-1,4,-3,-8,2,-8,-5,3,7,1,-4,-2,2,9,-8,-7,-8,-9,-4,6,6,-2,-8,-5,9,-3,-10,-1,4,2,3,-3,10,1,-8,3,-10,5,2,-7,5,5,4,2,8,-1,5,1,5,-1,-9,-7,9,-1,1,3,7,-5,-6,8,-3,4,-3,3,-8,-1,9,10,-1,9,6,-1,-10,3,-3,9,-9,4,-1,-2,-9,8,2,-6,-6,6,-6,6,-3,-3,1,2,6,-2,3,8,6,10,3,-10,2,4,2,6,-10,-4,3,-8,4,-8,5,-8,9,8,5,-2,7,7,-5,-7,-3,3,-8,5,-5,6,-8,-9,-4,10,9,6,-7,5,5,-4,-4,-4,-9,2,-3,-2,-5,-9,-1,8,-10,-6,-7,-6,5,-1,-8,9,6,-1,-2,-10,-7,-5,8,10,10,-5,-9,1,5,-2,9,-10,5,-3,-8,3,2,6,3,-9,2,-10,-7,4,3,4,-7,8,-8,10,-4,3,-3,5,5,-9,-8,-7,-1,6,6,7,-4,9,4,10,-2,-5,2,-1,3,-3,10,-7,-10,5,5,-3,-5,-5,-10,10,-7,-7,4,-5,7,-2,-7,-7,4,-7,2,-1,2,9,-10,4,-3,-4,10,-5,-7,-3,6,1,2,2,-8,2,-9,-2,9,6,-8,8,-2,-6,-8,3,-10,5,-4,5,-9,2,9,7,-1,-1,-5,-8,2,4,-2,5,3,4,-6,-9,-8,-3,4,-5,2,5,-5,-2,6,6,-7,2,2,5,-6,2,-5,1,4,-6,1,4,6,-10,6,-2,10,10,1,9,2,-1,6,-8,-7,-7,-8,2,-8,6,-2,-6,-4,2,6,3,3,-8,-6,-7,3,-1,6,-2,-8,10,-9,-10,-5,-8,-6,-10,7,-7,-4,-7,-10,-5,2,5,-8,-7,1,7,4,8,8,-10,-8,9,-1,9,3,-2,-3,-2,-1,-7,-10,10,-2,5,-10,7,10,-10,-10,-6,4,9,-4,10,4,8,4,8,-8,-7,8,6,2,10,-4,-7,6,-6,9,-6,3,-4,1,4,7,-10,7,-2,2,3,2,-4,5,9,-8,-4,-8,-10,4,-2,7,-5,-8,5,1,-7,7,-1,5,-6,-6,6,3,-7,-1,-8,-1,-5,10,-10,-10,-7,-10,9,10,-6,10,-2,-7,-9,-8,-7,10,7,-3,-2,-3,10,-7,9,-6,6,9,10,7,-4,-6,5,6,5,-10,-2,8,-8,-1,-4,2,-5,-10,-6,-4,-3,3,6,9,-9,-10,1,3,5,-4,10,-1,-6,-10,9,3,4,-9,7,2,4,-9,4,-4,-5,-9,6,-2,4,-5,5,4,-5,-2,10,8,-7,-1,-8,-1,-7,8,2,-6,-1,9,10,-7,-6,-5,2,10,-2,-2,8,-3,-4,8,10,-4,6,9,7,-1,7,-9,1,10,-2,6,-6,7,-8,9,1,-1,9,5,7,10,1,-3,-3,-10,5,-7,2,4,10,-10,-9,2,-2,-5,-2,-3,6,-9,-8,6,-2,-6,-6,6,6,-9,-8,4,-7,-1,3,3,-7,-8,1,10,-6,10,9,-10,-4,1,-1,4,-1,10,-6,-5,7,-1,9,4,8,-9,-9,-3,9,7,-8,-1,-5,-4,4,-5,5,1,-7,-7,-8,3,7,-2,-9,-10,1,7,2,8,-3,9,9,9,-3,-3,7,10,-10,-10,-3,-8,-2,2,-6,-2,-3,6,10,-10,-6,-6,6,4,-8,7,-7,-8,9,6,8,8,-10,-5,-2,3,-7,8,7,-3,10,-8,6,9,6,3,-3,5,-5,-4,-5,-4,8,-8,-6,9,1,-5,3,-2,-9,-3,8,-6,10,2,8,10,8,10,8,-1,9,6,10,-3,7,-1,-5,9,-6,-3,-5,-10,-8,8,-4,-5,-5,-6,-10,-3,-6,3,-9,9,3,10,2,2,2,7,1,8,-2,-2,-7,1,-7,-7,7,4,7,-8,5,10,-4,-3,9,-10,10,-7,-6,10,-3,4,2,-1,-3,9,-1,-5,-8,-9,-2,9,-2,8,-5,3,-3,9,4,-6,9,5,6,4,-2,10,3,-5,4,-2,2,-6,-2,-10,-4,-3,4,4,2,2,2,-8,-1,-7,8,3,-5,-3,-3,3,-3,-2,-8,7,-4,-2,2,1,-4,-8,10,-10,-10,1,-10,-3,-3,-10,-1,9,-5,-4,-2,10,-5,-6,-8,7,-1,-3,5,4,1,8,-10,-7,-9,-1,6,-9,-8,4,-3,-7,-1,5,-6,-3,4,9,8,6,7,-10,-9,-1,-6,-6,-8,-3,-3,5,9,6,-1,5,9,9,-1,8,-10,10,4,4,8,10,-6,-1,-5,8,2,-7,7,6,7,-9,-2,4,6,5,5,-7,2,-8,7,-7,9,7,-10,-3,8,7,-2,4,-10,2,-8,-8,9,9,2,-2,-10,7,3,-10,-6,10,7,-6,5,-2,-8,-3,-6,2,10,9,4,-3,-9,-9,9,3,-3,5,-10,1,9,7,-8,-3,5,-10,9,-10,-6,5,8,1,8,1,3,6,-8,7,-3,6,-4,7,-2,4,-5,3,-9,-9,2,-5,-4,9,5,9,8,-6,-6,8,9,5,-2,-9,7,-8,-10,6,-7,7,2,-9,-5,-3,-7,8,2,2,-6,-5,-9,-1,-9,4,-1,7,10,4,-9,6,-7,-4,10,4,-4,-8,-3,5,-6,-5,1,2,8,-7,-4,-4,9,-1,1,6,6,2,3], dtype = "int16")#candidate|2954|(1575,)|const|int16
call_2952 = relay.TupleGetItem(func_2632_call(relay.reshape(const_2953.astype('bool'), [1080,]), relay.reshape(const_2954.astype('int16'), [15, 105]), ), 1)
call_2955 = relay.TupleGetItem(func_2635_call(relay.reshape(const_2953.astype('bool'), [1080,]), relay.reshape(const_2954.astype('int16'), [15, 105]), ), 1)
var_2969 = relay.var("var_2969", dtype = "float64", shape = (12, 11, 2))#candidate|2969|(12, 11, 2)|var|float64
bop_2970 = relay.logical_and(call_2947.astype('bool'), relay.reshape(var_2969.astype('bool'), relay.shape_of(call_2947))) # shape=(12, 11, 2)
bop_2973 = relay.logical_and(call_2948.astype('bool'), relay.reshape(var_2969.astype('bool'), relay.shape_of(call_2948))) # shape=(12, 11, 2)
uop_2979 = relay.log10(const_2953.astype('float64')) # shape=(1080,)
func_1928_call = mod.get_global_var('func_1928')
func_1931_call = mutated_mod.get_global_var('func_1931')
call_2989 = relay.TupleGetItem(func_1928_call(relay.reshape(const_2953.astype('bool'), [10, 9, 12]), relay.reshape(const_2954.astype('int16'), [105, 15]), ), 1)
call_2990 = relay.TupleGetItem(func_1931_call(relay.reshape(const_2953.astype('bool'), [10, 9, 12]), relay.reshape(const_2954.astype('int16'), [105, 15]), ), 1)
func_728_call = mod.get_global_var('func_728')
func_732_call = mutated_mod.get_global_var('func_732')
call_2995 = relay.TupleGetItem(func_728_call(relay.reshape(const_2954.astype('int16'), [7, 15, 15]), relay.reshape(call_2989.astype('float32'), [1, 450]), ), 4)
call_2996 = relay.TupleGetItem(func_732_call(relay.reshape(const_2954.astype('int16'), [7, 15, 15]), relay.reshape(call_2989.astype('float32'), [1, 450]), ), 4)
uop_3013 = relay.log2(var_2969.astype('float64')) # shape=(12, 11, 2)
bop_3015 = relay.left_shift(uop_3013.astype('int32'), relay.reshape(call_2947.astype('int32'), relay.shape_of(uop_3013))) # shape=(12, 11, 2)
bop_3018 = relay.left_shift(uop_3013.astype('int32'), relay.reshape(call_2948.astype('int32'), relay.shape_of(uop_3013))) # shape=(12, 11, 2)
output = relay.Tuple([call_2952,const_2954,bop_2970,uop_2979,call_2989,call_2995,bop_3015,])
output2 = relay.Tuple([call_2955,const_2954,bop_2973,uop_2979,call_2990,call_2996,bop_3018,])
func_3021 = relay.Function([var_2969,], output)
mod['func_3021'] = func_3021
mod = relay.transform.InferType()(mod)
var_3022 = relay.var("var_3022", dtype = "float64", shape = (12, 11, 2))#candidate|3022|(12, 11, 2)|var|float64
output = func_3021(var_3022)
func_3023 = relay.Function([var_3022], output)
mutated_mod['func_3023'] = func_3023
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3025 = relay.var("var_3025", dtype = "int16", shape = ())#candidate|3025|()|var|int16
var_3026 = relay.var("var_3026", dtype = "int16", shape = (7, 14, 12))#candidate|3026|(7, 14, 12)|var|int16
bop_3027 = relay.add(var_3025.astype('int16'), var_3026.astype('int16')) # shape=(7, 14, 12)
func_1983_call = mod.get_global_var('func_1983')
func_1986_call = mutated_mod.get_global_var('func_1986')
const_3039 = relay.const([[-9.778862],[-2.342142],[-8.127903],[8.057581],[-0.763074],[5.197055],[-0.286987],[-2.934146],[9.840296],[-3.782558],[5.180774],[-7.356527],[5.989316],[-4.238354],[1.274835],[-2.199362],[2.821754],[1.654206],[5.460286],[6.147505],[-6.139625],[-5.679643],[5.979754],[-5.851534],[-3.634006],[3.879867],[1.803073],[2.775852],[8.158610],[-9.331520],[-7.659645],[4.626279],[6.223477],[4.315686],[8.033851],[9.426137],[-8.812368],[-0.488273],[-7.574816],[-9.090578],[9.074983],[-2.218747],[-1.793600],[0.519724],[-5.578883],[-0.543114],[-0.828117],[-2.546072],[-8.233654],[3.895729],[-9.699464],[9.849803],[-2.023538],[-9.612921],[6.863106],[4.783904],[9.084719],[8.869681],[4.550226],[7.771371],[-0.735394],[8.141507],[3.250813],[-7.964128],[9.911890],[7.204595],[-2.117350],[-6.419202],[-4.028671],[-3.201861],[-0.208910],[-7.702556],[8.521459],[3.867161],[-0.702286],[-6.841511],[-0.620999],[-5.171961],[-3.077334],[-9.897630],[-9.603333],[9.350068],[-9.993867],[6.430182],[4.606656],[-4.447812],[0.861562],[9.192653],[-0.852661],[-1.372222],[0.538000],[7.064707],[-1.486961],[-2.271167],[3.820466],[-1.256113],[-4.852103],[-2.650495],[-5.687610],[-2.826292],[4.085955],[3.594122],[4.547034],[-1.458153],[4.965158],[6.732129],[0.102561],[-7.321795],[-5.161082],[-7.498127],[5.990507],[9.891668],[7.367557],[5.434143],[9.865876],[4.864761],[-3.739832],[7.837285],[5.632648],[-2.702205],[-2.638885],[8.171077],[-2.158238],[3.744123],[-3.180950],[-2.964916],[4.685349],[-5.518985],[-0.970523],[-4.912081],[2.865114],[-5.646245],[-2.300287],[3.815350],[2.386755],[-1.845125],[1.557615],[-7.944067],[9.544588],[-1.451448],[7.703353],[-2.037052],[-3.794890],[6.727932],[-4.962890],[-4.270023],[1.602849],[1.060117],[6.509183],[7.776934],[-0.691544],[-6.986062],[-2.374202],[-7.025675],[6.770716],[7.555394],[3.575804],[7.802694],[-9.813873],[-2.971302],[-5.017060],[-3.029590],[-2.965031],[2.194285],[3.262247],[-9.920470],[-7.371173],[8.418866],[7.988621],[-3.799453],[4.947684],[-0.224405],[1.726797],[-3.619809],[-2.703485],[-3.582444],[-2.029318],[8.724865],[2.183988],[-7.623984],[6.245758],[-2.347260],[5.858813],[-4.010068],[5.450506],[5.706297],[8.071567],[-9.962213],[5.326259],[-8.999750],[2.635662],[-5.400909],[-4.622110],[-4.362276],[-2.757236],[-6.446753],[-8.937391],[1.883521],[-8.904025],[-7.954239],[6.144173],[-0.192117],[0.692285],[0.075709],[-9.132362],[8.816580],[2.712916],[5.105286],[5.223149],[4.228357],[-6.802569],[3.847946],[-0.954058],[-6.082555],[6.609477],[0.220848],[0.340313],[4.721438],[-9.262612],[9.589338],[-8.813345],[-0.544813],[9.103295],[3.117842],[-6.445536],[-2.338891],[-8.447168],[5.686786],[5.963932],[-8.781729],[-0.420178],[1.066176],[2.090654],[0.315876],[7.500034],[-1.137051],[2.429058],[5.797355],[-3.623572],[6.787004],[3.387903],[1.740330],[9.559047],[6.848073],[2.894985],[9.558404],[0.820033],[2.502209],[9.641220],[-5.436879],[7.512820],[5.971351],[8.222729],[2.864564],[7.746223],[-7.518665],[5.853360],[1.101353],[-2.770761],[2.143677],[-8.666661],[-4.820252],[7.488697],[-6.838499]], dtype = "float32")#candidate|3039|(264, 1)|const|float32
call_3038 = func_1983_call(relay.reshape(const_3039.astype('float32'), [12, 11, 2]))
call_3040 = func_1983_call(relay.reshape(const_3039.astype('float32'), [12, 11, 2]))
func_3021_call = mod.get_global_var('func_3021')
func_3023_call = mutated_mod.get_global_var('func_3023')
call_3048 = relay.TupleGetItem(func_3021_call(relay.reshape(call_3038.astype('float64'), [12, 11, 2])), 0)
call_3049 = relay.TupleGetItem(func_3023_call(relay.reshape(call_3038.astype('float64'), [12, 11, 2])), 0)
func_2198_call = mod.get_global_var('func_2198')
func_2199_call = mutated_mod.get_global_var('func_2199')
call_3051 = relay.TupleGetItem(func_2198_call(), 0)
call_3052 = relay.TupleGetItem(func_2199_call(), 0)
bop_3054 = relay.bitwise_xor(const_3039.astype('uint64'), var_3025.astype('uint64')) # shape=(264, 1)
output = relay.Tuple([bop_3027,call_3038,call_3048,call_3051,bop_3054,])
output2 = relay.Tuple([bop_3027,call_3040,call_3049,call_3052,bop_3054,])
func_3061 = relay.Function([var_3025,var_3026,], output)
mod['func_3061'] = func_3061
mod = relay.transform.InferType()(mod)
mutated_mod['func_3061'] = func_3061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3061_call = mutated_mod.get_global_var('func_3061')
var_3063 = relay.var("var_3063", dtype = "int16", shape = ())#candidate|3063|()|var|int16
var_3064 = relay.var("var_3064", dtype = "int16", shape = (7, 14, 12))#candidate|3064|(7, 14, 12)|var|int16
call_3062 = func_3061_call(var_3063,var_3064,)
output = call_3062
func_3065 = relay.Function([var_3063,var_3064,], output)
mutated_mod['func_3065'] = func_3065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2791_call = mod.get_global_var('func_2791')
func_2793_call = mutated_mod.get_global_var('func_2793')
call_3069 = relay.TupleGetItem(func_2791_call(), 0)
call_3070 = relay.TupleGetItem(func_2793_call(), 0)
var_3073 = relay.var("var_3073", dtype = "int8", shape = (450,))#candidate|3073|(450,)|var|int8
bop_3074 = relay.floor_divide(call_3069.astype('float32'), relay.reshape(var_3073.astype('float32'), relay.shape_of(call_3069))) # shape=(450,)
bop_3077 = relay.floor_divide(call_3070.astype('float32'), relay.reshape(var_3073.astype('float32'), relay.shape_of(call_3070))) # shape=(450,)
func_2858_call = mod.get_global_var('func_2858')
func_2859_call = mutated_mod.get_global_var('func_2859')
call_3088 = func_2858_call()
call_3089 = func_2858_call()
output = relay.Tuple([bop_3074,call_3088,])
output2 = relay.Tuple([bop_3077,call_3089,])
func_3092 = relay.Function([var_3073,], output)
mod['func_3092'] = func_3092
mod = relay.transform.InferType()(mod)
mutated_mod['func_3092'] = func_3092
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3093 = relay.var("var_3093", dtype = "int8", shape = (450,))#candidate|3093|(450,)|var|int8
func_3092_call = mutated_mod.get_global_var('func_3092')
call_3094 = func_3092_call(var_3093)
output = call_3094
func_3095 = relay.Function([var_3093], output)
mutated_mod['func_3095'] = func_3095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2858_call = mod.get_global_var('func_2858')
func_2859_call = mutated_mod.get_global_var('func_2859')
call_3099 = func_2858_call()
call_3100 = func_2858_call()
func_2399_call = mod.get_global_var('func_2399')
func_2400_call = mutated_mod.get_global_var('func_2400')
call_3102 = relay.TupleGetItem(func_2399_call(), 2)
call_3103 = relay.TupleGetItem(func_2400_call(), 2)
func_2683_call = mod.get_global_var('func_2683')
func_2685_call = mutated_mod.get_global_var('func_2685')
call_3104 = relay.TupleGetItem(func_2683_call(), 0)
call_3105 = relay.TupleGetItem(func_2685_call(), 0)
uop_3111 = relay.asin(call_3102.astype('float32')) # shape=(132, 2)
uop_3113 = relay.asin(call_3103.astype('float32')) # shape=(132, 2)
uop_3133 = relay.atan(uop_3111.astype('float64')) # shape=(132, 2)
uop_3135 = relay.atan(uop_3113.astype('float64')) # shape=(132, 2)
const_3138 = relay.const([[6.971912,9.136872],[-6.746379,-2.137417],[3.191367,-7.076209],[4.134646,-6.120194],[-7.294363,-7.756230],[-3.821580,3.584568],[5.641466,-1.006282],[5.108689,1.911798],[7.066641,-5.901426],[-3.347431,1.666591],[-8.741912,-0.161801],[-2.572949,7.584492],[2.168426,2.124043],[5.941948,9.278485],[-7.420753,4.781037],[7.230917,-3.727032],[7.828679,-1.869988],[6.786920,8.169843],[-6.914880,4.622831],[0.719419,0.275608],[9.097303,-4.701178],[4.824448,6.966051],[1.098368,-5.842024],[-4.356920,3.994820],[1.436229,7.087242],[8.842142,-9.265767],[-6.373441,4.815862],[-4.334018,-4.610627],[1.014528,3.424874],[-0.538405,4.287964],[7.167006,-4.539335],[-7.197009,1.614262],[4.865206,1.351631],[-8.887976,-9.688625],[3.905474,-4.028984],[0.328540,9.962087],[0.630856,6.694307],[-1.246703,2.111992],[-5.899353,2.674105],[-7.568986,-3.473688],[5.736321,-5.992325],[-0.504350,-6.610289],[-9.814967,2.670123],[0.292784,5.882882],[3.666404,-4.237766],[3.588914,5.902558],[2.551975,-9.360563],[-6.444792,5.547966],[-3.674335,5.893713],[4.149142,3.946292],[-6.305827,7.150954],[6.713011,-2.241544],[2.874871,-9.285628],[-9.410225,0.185843],[-8.955570,6.778693],[-0.033208,-1.281560],[2.050412,8.759770],[3.489736,-6.557806],[-2.326232,8.676186],[-4.360391,-1.366375],[-5.264691,-4.237153],[4.816954,-7.554824],[-9.540135,-7.557108],[9.385967,0.115804],[-9.890412,9.007249],[2.878868,9.750442],[4.467925,-4.181406],[-7.864775,1.429363],[4.647402,8.745841],[6.835122,6.715407],[-8.766421,8.742003],[-3.149724,-1.438278],[5.284522,8.518666],[8.835143,-7.144732],[8.415858,4.528841],[-2.946425,0.181991],[-3.196136,-7.153663],[-0.495379,7.216881],[1.995867,-5.543687],[-2.917410,-8.244973],[-5.999372,-0.340347],[-7.777098,-8.037203],[1.151426,6.748669],[3.850925,-5.165554],[3.373079,8.822508],[-4.876108,-8.151936],[8.165291,7.432803],[8.793510,-8.700690],[0.500650,-8.720697],[4.232845,-2.536617],[-8.144309,-3.884753],[-4.638736,7.455032],[9.828640,3.462154],[-6.820664,2.103876],[9.438091,5.002773],[-6.578225,-7.142245],[-8.410411,4.369727],[-1.028522,0.503066],[9.612340,-5.059291],[-5.187503,-3.118558],[-4.611468,6.953609],[7.023364,7.245498],[6.961594,-8.984340],[-0.900025,-8.524291],[0.299874,-7.202644],[9.473392,-8.816147],[-9.553512,-5.826196],[-2.295053,-4.482415],[-5.939100,6.862738],[1.347030,-8.496434],[7.295642,-0.590178],[-0.760710,8.454163],[3.545404,5.706494],[9.273905,3.170350],[-3.703552,-7.274501],[-7.299085,6.155407],[-0.606417,1.973414],[6.234721,-7.960119],[-6.573724,-0.406643],[6.750773,-4.309621],[-9.642550,7.860017],[6.452612,9.888230],[-2.973862,-4.717146],[-2.077511,-3.721149],[0.851964,-1.638620],[0.951456,7.525939],[-2.648617,-0.895451],[0.318417,-4.554146],[-0.905844,0.545462],[-8.248113,9.699583],[-0.563513,-1.105864],[-5.951117,3.209712]], dtype = "float32")#candidate|3138|(132, 2)|const|float32
bop_3139 = relay.mod(uop_3111.astype('float64'), relay.reshape(const_3138.astype('float64'), relay.shape_of(uop_3111))) # shape=(132, 2)
bop_3142 = relay.mod(uop_3113.astype('float64'), relay.reshape(const_3138.astype('float64'), relay.shape_of(uop_3113))) # shape=(132, 2)
func_2198_call = mod.get_global_var('func_2198')
func_2199_call = mutated_mod.get_global_var('func_2199')
call_3143 = relay.TupleGetItem(func_2198_call(), 0)
call_3144 = relay.TupleGetItem(func_2199_call(), 0)
output = relay.Tuple([call_3099,call_3104,uop_3133,bop_3139,call_3143,])
output2 = relay.Tuple([call_3100,call_3105,uop_3135,bop_3142,call_3144,])
func_3148 = relay.Function([], output)
mod['func_3148'] = func_3148
mod = relay.transform.InferType()(mod)
mutated_mod['func_3148'] = func_3148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3148_call = mutated_mod.get_global_var('func_3148')
call_3149 = func_3148_call()
output = call_3149
func_3150 = relay.Function([], output)
mutated_mod['func_3150'] = func_3150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2909_call = mod.get_global_var('func_2909')
func_2910_call = mutated_mod.get_global_var('func_2910')
call_3175 = func_2909_call()
call_3176 = func_2909_call()
output = relay.Tuple([call_3175,])
output2 = relay.Tuple([call_3176,])
func_3181 = relay.Function([], output)
mod['func_3181'] = func_3181
mod = relay.transform.InferType()(mod)
output = func_3181()
func_3182 = relay.Function([], output)
mutated_mod['func_3182'] = func_3182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2765_call = mod.get_global_var('func_2765')
func_2767_call = mutated_mod.get_global_var('func_2767')
call_3189 = relay.TupleGetItem(func_2765_call(), 2)
call_3190 = relay.TupleGetItem(func_2767_call(), 2)
output = relay.Tuple([call_3189,])
output2 = relay.Tuple([call_3190,])
func_3193 = relay.Function([], output)
mod['func_3193'] = func_3193
mod = relay.transform.InferType()(mod)
output = func_3193()
func_3194 = relay.Function([], output)
mutated_mod['func_3194'] = func_3194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3148_call = mod.get_global_var('func_3148')
func_3150_call = mutated_mod.get_global_var('func_3150')
call_3237 = relay.TupleGetItem(func_3148_call(), 4)
call_3238 = relay.TupleGetItem(func_3150_call(), 4)
func_3148_call = mod.get_global_var('func_3148')
func_3150_call = mutated_mod.get_global_var('func_3150')
call_3249 = relay.TupleGetItem(func_3148_call(), 4)
call_3250 = relay.TupleGetItem(func_3150_call(), 4)
output = relay.Tuple([call_3237,call_3249,])
output2 = relay.Tuple([call_3238,call_3250,])
func_3258 = relay.Function([], output)
mod['func_3258'] = func_3258
mod = relay.transform.InferType()(mod)
output = func_3258()
func_3259 = relay.Function([], output)
mutated_mod['func_3259'] = func_3259
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3266 = relay.var("var_3266", dtype = "int32", shape = ())#candidate|3266|()|var|int32
var_3267 = relay.var("var_3267", dtype = "int32", shape = (1, 2, 4))#candidate|3267|(1, 2, 4)|var|int32
bop_3268 = relay.left_shift(var_3266.astype('int32'), var_3267.astype('int32')) # shape=(1, 2, 4)
bop_3277 = relay.right_shift(var_3266.astype('uint32'), var_3267.astype('uint32')) # shape=(1, 2, 4)
uop_3280 = relay.atanh(bop_3268.astype('float32')) # shape=(1, 2, 4)
output = relay.Tuple([bop_3277,uop_3280,])
output2 = relay.Tuple([bop_3277,uop_3280,])
func_3287 = relay.Function([var_3266,var_3267,], output)
mod['func_3287'] = func_3287
mod = relay.transform.InferType()(mod)
mutated_mod['func_3287'] = func_3287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3287_call = mutated_mod.get_global_var('func_3287')
var_3289 = relay.var("var_3289", dtype = "int32", shape = ())#candidate|3289|()|var|int32
var_3290 = relay.var("var_3290", dtype = "int32", shape = (1, 2, 4))#candidate|3290|(1, 2, 4)|var|int32
call_3288 = func_3287_call(var_3289,var_3290,)
output = call_3288
func_3291 = relay.Function([var_3289,var_3290,], output)
mutated_mod['func_3291'] = func_3291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2399_call = mod.get_global_var('func_2399')
func_2400_call = mutated_mod.get_global_var('func_2400')
call_3333 = relay.TupleGetItem(func_2399_call(), 0)
call_3334 = relay.TupleGetItem(func_2400_call(), 0)
func_3193_call = mod.get_global_var('func_3193')
func_3194_call = mutated_mod.get_global_var('func_3194')
call_3351 = relay.TupleGetItem(func_3193_call(), 0)
call_3352 = relay.TupleGetItem(func_3194_call(), 0)
output = relay.Tuple([call_3333,call_3351,])
output2 = relay.Tuple([call_3334,call_3352,])
func_3359 = relay.Function([], output)
mod['func_3359'] = func_3359
mod = relay.transform.InferType()(mod)
output = func_3359()
func_3360 = relay.Function([], output)
mutated_mod['func_3360'] = func_3360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3258_call = mod.get_global_var('func_3258')
func_3259_call = mutated_mod.get_global_var('func_3259')
call_3428 = relay.TupleGetItem(func_3258_call(), 0)
call_3429 = relay.TupleGetItem(func_3259_call(), 0)
output = call_3428
output2 = call_3429
func_3430 = relay.Function([], output)
mod['func_3430'] = func_3430
mod = relay.transform.InferType()(mod)
output = func_3430()
func_3431 = relay.Function([], output)
mutated_mod['func_3431'] = func_3431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3181_call = mod.get_global_var('func_3181')
func_3182_call = mutated_mod.get_global_var('func_3182')
call_3498 = relay.TupleGetItem(func_3181_call(), 0)
call_3499 = relay.TupleGetItem(func_3182_call(), 0)
output = call_3498
output2 = call_3499
func_3506 = relay.Function([], output)
mod['func_3506'] = func_3506
mod = relay.transform.InferType()(mod)
mutated_mod['func_3506'] = func_3506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3506_call = mutated_mod.get_global_var('func_3506')
call_3507 = func_3506_call()
output = call_3507
func_3508 = relay.Function([], output)
mutated_mod['func_3508'] = func_3508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3258_call = mod.get_global_var('func_3258')
func_3259_call = mutated_mod.get_global_var('func_3259')
call_3540 = relay.TupleGetItem(func_3258_call(), 1)
call_3541 = relay.TupleGetItem(func_3259_call(), 1)
func_3181_call = mod.get_global_var('func_3181')
func_3182_call = mutated_mod.get_global_var('func_3182')
call_3542 = relay.TupleGetItem(func_3181_call(), 0)
call_3543 = relay.TupleGetItem(func_3182_call(), 0)
output = relay.Tuple([call_3540,call_3542,])
output2 = relay.Tuple([call_3541,call_3543,])
func_3553 = relay.Function([], output)
mod['func_3553'] = func_3553
mod = relay.transform.InferType()(mod)
mutated_mod['func_3553'] = func_3553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3553_call = mutated_mod.get_global_var('func_3553')
call_3554 = func_3553_call()
output = call_3554
func_3555 = relay.Function([], output)
mutated_mod['func_3555'] = func_3555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2683_call = mod.get_global_var('func_2683')
func_2685_call = mutated_mod.get_global_var('func_2685')
call_3556 = relay.TupleGetItem(func_2683_call(), 1)
call_3557 = relay.TupleGetItem(func_2685_call(), 1)
output = call_3556
output2 = call_3557
func_3558 = relay.Function([], output)
mod['func_3558'] = func_3558
mod = relay.transform.InferType()(mod)
output = func_3558()
func_3559 = relay.Function([], output)
mutated_mod['func_3559'] = func_3559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3181_call = mod.get_global_var('func_3181')
func_3182_call = mutated_mod.get_global_var('func_3182')
call_3585 = relay.TupleGetItem(func_3181_call(), 0)
call_3586 = relay.TupleGetItem(func_3182_call(), 0)
output = relay.Tuple([call_3585,])
output2 = relay.Tuple([call_3586,])
func_3589 = relay.Function([], output)
mod['func_3589'] = func_3589
mod = relay.transform.InferType()(mod)
output = func_3589()
func_3590 = relay.Function([], output)
mutated_mod['func_3590'] = func_3590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3193_call = mod.get_global_var('func_3193')
func_3194_call = mutated_mod.get_global_var('func_3194')
call_3599 = relay.TupleGetItem(func_3193_call(), 0)
call_3600 = relay.TupleGetItem(func_3194_call(), 0)
func_2683_call = mod.get_global_var('func_2683')
func_2685_call = mutated_mod.get_global_var('func_2685')
call_3624 = relay.TupleGetItem(func_2683_call(), 1)
call_3625 = relay.TupleGetItem(func_2685_call(), 1)
output = relay.Tuple([call_3599,call_3624,])
output2 = relay.Tuple([call_3600,call_3625,])
func_3628 = relay.Function([], output)
mod['func_3628'] = func_3628
mod = relay.transform.InferType()(mod)
output = func_3628()
func_3629 = relay.Function([], output)
mutated_mod['func_3629'] = func_3629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2683_call = mod.get_global_var('func_2683')
func_2685_call = mutated_mod.get_global_var('func_2685')
call_3694 = relay.TupleGetItem(func_2683_call(), 0)
call_3695 = relay.TupleGetItem(func_2685_call(), 0)
func_3558_call = mod.get_global_var('func_3558')
func_3559_call = mutated_mod.get_global_var('func_3559')
call_3696 = func_3558_call()
call_3697 = func_3558_call()
uop_3703 = relay.cosh(call_3694.astype('float32')) # shape=(7, 13, 7)
uop_3705 = relay.cosh(call_3695.astype('float32')) # shape=(7, 13, 7)
output = relay.Tuple([call_3696,uop_3703,])
output2 = relay.Tuple([call_3697,uop_3705,])
func_3718 = relay.Function([], output)
mod['func_3718'] = func_3718
mod = relay.transform.InferType()(mod)
output = func_3718()
func_3719 = relay.Function([], output)
mutated_mod['func_3719'] = func_3719
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3738 = relay.var("var_3738", dtype = "float32", shape = (10, 4, 1))#candidate|3738|(10, 4, 1)|var|float32
uop_3739 = relay.cosh(var_3738.astype('float32')) # shape=(10, 4, 1)
var_3745 = relay.var("var_3745", dtype = "float32", shape = (10, 4, 12))#candidate|3745|(10, 4, 12)|var|float32
bop_3746 = relay.not_equal(uop_3739.astype('bool'), var_3745.astype('bool')) # shape=(10, 4, 12)
output = relay.Tuple([bop_3746,])
output2 = relay.Tuple([bop_3746,])
func_3753 = relay.Function([var_3738,var_3745,], output)
mod['func_3753'] = func_3753
mod = relay.transform.InferType()(mod)
mutated_mod['func_3753'] = func_3753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3753_call = mutated_mod.get_global_var('func_3753')
var_3755 = relay.var("var_3755", dtype = "float32", shape = (10, 4, 1))#candidate|3755|(10, 4, 1)|var|float32
var_3756 = relay.var("var_3756", dtype = "float32", shape = (10, 4, 12))#candidate|3756|(10, 4, 12)|var|float32
call_3754 = func_3753_call(var_3755,var_3756,)
output = call_3754
func_3757 = relay.Function([var_3755,var_3756,], output)
mutated_mod['func_3757'] = func_3757
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3763 = relay.var("var_3763", dtype = "float32", shape = (6, 5, 7))#candidate|3763|(6, 5, 7)|var|float32
uop_3764 = relay.log10(var_3763.astype('float32')) # shape=(6, 5, 7)
uop_3771 = relay.asin(uop_3764.astype('float64')) # shape=(6, 5, 7)
output = relay.Tuple([uop_3771,])
output2 = relay.Tuple([uop_3771,])
func_3790 = relay.Function([var_3763,], output)
mod['func_3790'] = func_3790
mod = relay.transform.InferType()(mod)
mutated_mod['func_3790'] = func_3790
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3791 = relay.var("var_3791", dtype = "float32", shape = (6, 5, 7))#candidate|3791|(6, 5, 7)|var|float32
func_3790_call = mutated_mod.get_global_var('func_3790')
call_3792 = func_3790_call(var_3791)
output = call_3792
func_3793 = relay.Function([var_3791], output)
mutated_mod['func_3793'] = func_3793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2198_call = mod.get_global_var('func_2198')
func_2199_call = mutated_mod.get_global_var('func_2199')
call_3799 = relay.TupleGetItem(func_2198_call(), 0)
call_3800 = relay.TupleGetItem(func_2199_call(), 0)
uop_3818 = relay.atan(call_3799.astype('float32')) # shape=(7, 13, 7)
uop_3820 = relay.atan(call_3800.astype('float32')) # shape=(7, 13, 7)
bop_3821 = relay.floor_divide(call_3799.astype('float64'), relay.reshape(uop_3818.astype('float64'), relay.shape_of(call_3799))) # shape=(7, 13, 7)
bop_3824 = relay.floor_divide(call_3800.astype('float64'), relay.reshape(uop_3820.astype('float64'), relay.shape_of(call_3800))) # shape=(7, 13, 7)
output = bop_3821
output2 = bop_3824
func_3825 = relay.Function([], output)
mod['func_3825'] = func_3825
mod = relay.transform.InferType()(mod)
output = func_3825()
func_3826 = relay.Function([], output)
mutated_mod['func_3826'] = func_3826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2909_call = mod.get_global_var('func_2909')
func_2910_call = mutated_mod.get_global_var('func_2910')
call_3906 = func_2909_call()
call_3907 = func_2909_call()
func_3181_call = mod.get_global_var('func_3181')
func_3182_call = mutated_mod.get_global_var('func_3182')
call_3924 = relay.TupleGetItem(func_3181_call(), 0)
call_3925 = relay.TupleGetItem(func_3182_call(), 0)
output = relay.Tuple([call_3906,call_3924,])
output2 = relay.Tuple([call_3907,call_3925,])
func_3941 = relay.Function([], output)
mod['func_3941'] = func_3941
mod = relay.transform.InferType()(mod)
output = func_3941()
func_3942 = relay.Function([], output)
mutated_mod['func_3942'] = func_3942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2765_call = mod.get_global_var('func_2765')
func_2767_call = mutated_mod.get_global_var('func_2767')
call_3972 = relay.TupleGetItem(func_2765_call(), 2)
call_3973 = relay.TupleGetItem(func_2767_call(), 2)
func_2765_call = mod.get_global_var('func_2765')
func_2767_call = mutated_mod.get_global_var('func_2767')
call_3992 = relay.TupleGetItem(func_2765_call(), 0)
call_3993 = relay.TupleGetItem(func_2767_call(), 0)
func_3628_call = mod.get_global_var('func_3628')
func_3629_call = mutated_mod.get_global_var('func_3629')
call_4000 = relay.TupleGetItem(func_3628_call(), 0)
call_4001 = relay.TupleGetItem(func_3629_call(), 0)
output = relay.Tuple([call_3972,call_3992,call_4000,])
output2 = relay.Tuple([call_3973,call_3993,call_4001,])
func_4002 = relay.Function([], output)
mod['func_4002'] = func_4002
mod = relay.transform.InferType()(mod)
output = func_4002()
func_4003 = relay.Function([], output)
mutated_mod['func_4003'] = func_4003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2410_call = mod.get_global_var('func_2410')
func_2411_call = mutated_mod.get_global_var('func_2411')
call_4012 = relay.TupleGetItem(func_2410_call(), 0)
call_4013 = relay.TupleGetItem(func_2411_call(), 0)
func_2279_call = mod.get_global_var('func_2279')
func_2282_call = mutated_mod.get_global_var('func_2282')
var_4026 = relay.var("var_4026", dtype = "int8", shape = (75,))#candidate|4026|(75,)|var|int8
const_4027 = relay.const([[-5],[-8],[1],[-3],[9],[5],[-8],[8],[8],[8],[1],[-10],[4],[-2],[1],[1],[-10],[1],[8],[-6],[-10],[8],[7],[-3],[-1],[10],[9],[-3],[-8],[-3],[8],[5],[4],[9],[-1],[-1],[-5],[8],[7],[7],[-2],[-2],[-7],[-6],[-1],[-5],[3],[-4],[7],[-1],[8],[9],[2],[-3],[9],[-7],[-7],[4],[3],[10],[-8],[-10],[5],[10],[-9],[8],[4],[1],[5],[5],[6],[-6],[10],[-8],[1],[6],[2],[-2],[1],[-7],[-4],[8],[-4],[-6],[-4],[4],[-2],[4],[2],[4],[9],[3],[-5],[8],[-7],[-8],[2],[1],[-8],[-5],[-7],[-4],[-1],[10],[10],[9],[3],[1],[-6],[-7],[4],[6],[-3],[1],[5],[4],[7],[2],[6],[-3],[5],[6],[-5],[7],[5],[-6],[9],[-6],[8],[-4],[3],[6],[5],[10],[-9],[8],[9],[1],[8],[-5],[4],[-4],[5],[5],[-5],[-8],[-8],[2],[10],[5],[-9],[3],[-4],[1],[-6],[6],[10],[-1],[10],[-8],[-7],[-7],[9],[-10],[-1],[10],[7],[-7],[-10],[6],[-7],[-4],[-4],[9],[4],[-9],[4],[-8],[5],[-5],[3],[8],[9],[-5],[-6],[-4],[3],[7],[6],[-1],[7],[-3],[-8],[-5],[-9],[1],[8],[-3],[7],[-5],[-7],[3],[1],[-9],[-9],[-9],[-2],[7],[-1],[5],[5],[-1],[-5],[9],[2],[-4],[-4],[-1],[8],[4],[-2],[-2],[-3],[-8],[-3],[6],[9],[10],[-2],[8],[2],[-3],[7],[-3],[-5],[2],[10],[-6],[5],[9],[7],[4],[1],[-1],[-3],[-6],[-9],[5],[-2],[2],[-7],[-7],[-10],[-2],[-6],[-1],[-4],[-8],[10],[-1],[8],[-2],[-4],[-2],[-5],[-6],[-1],[-9],[-3],[-4],[-2],[2],[1],[-3],[9],[6],[1],[4],[-2],[4],[3],[10],[-2],[-6],[10],[5],[-4],[-7],[7],[6],[8],[-5],[9],[-4],[8],[-10],[9],[-6],[1],[-7],[-2],[4],[-9],[3],[-5],[-6],[-2],[-9],[10],[5],[5],[-10],[7],[7],[-10],[2],[9],[9],[9],[6],[2],[6],[-10],[-6],[2],[10],[-7],[4],[-10],[4],[9],[1],[-2],[-6],[4],[-4],[1],[-10],[-4],[-5],[8],[-4],[8],[8],[10],[8],[-8],[5],[-1],[10],[2],[-2],[3],[-6],[-10],[5],[-6],[10],[-8],[-2],[2],[8],[-8],[1],[-6],[7],[-6],[-1],[-4],[-10],[-7],[10],[-4],[9],[-1],[-10],[10],[-3],[1],[-10],[-7],[-4],[-9],[-4],[1],[-5],[8],[4],[-8],[-4],[4],[3],[10],[-2],[2],[-7],[-10],[-1],[-6],[-10],[-8],[-9],[-10],[6],[6],[8],[4],[1],[9],[-6],[-7],[9],[-5],[-6],[5],[10],[-1],[-8],[4],[3],[-4],[9],[4],[3],[-5],[-4],[3],[2],[4],[-9],[-4],[-10],[1],[-7],[4],[2],[-3],[-7],[3],[8],[-8],[-2],[6],[8],[-10],[8],[-9],[-8],[-8],[3],[7],[9],[10],[-6],[-5],[-1],[-9],[-7],[7],[-4],[4],[2],[10],[-6],[-8],[-10],[6],[-4],[-5],[-9],[5],[7],[-5],[8],[10],[10],[3],[9],[-3],[-4],[4],[6],[5],[-8],[10],[-3],[9],[10],[4],[7],[-1],[-10],[-10],[-10],[4],[4],[9],[-9],[7],[5],[5],[6],[-9],[2],[-6],[7],[-8],[4],[6],[1],[-9],[7],[2],[-2],[-3],[8],[-6],[6],[3],[-7],[6],[8],[3],[-10],[-7],[8],[-5],[-4],[2],[7],[5],[-7],[-2],[-4],[-10],[-7],[7],[10],[9],[-10],[2],[-2],[4],[5],[-4],[-5],[-8],[7],[7],[6],[-2],[-6],[8],[10],[6],[4],[7],[-7],[2],[9],[4],[2],[-8],[3],[-10],[-3],[-2],[5],[4],[9],[-5],[-10],[-7],[-5],[10],[-2],[10],[6],[2],[-3],[8],[9],[4],[-2],[-9],[-8],[2],[-7],[8],[-7],[-6],[5],[-4],[3],[-2],[-2],[-2],[-2],[5],[5],[-5],[-8],[-5],[-7],[7],[-1],[4],[6],[-9],[-5],[5],[1],[8],[-2],[-7],[5],[-1],[8],[-8],[-9],[8],[7],[-8],[-9],[-3],[-7],[-2],[4],[2],[-1],[4],[-1],[-2],[1],[4],[6],[-1],[-4],[-5],[-5],[-9],[-7],[-3],[-3],[8],[5],[1],[-8],[-5],[-3],[-8],[10],[2],[-8],[1],[7],[8],[-3],[6],[7],[9],[9],[10],[-4],[-6],[-5],[-8],[2],[1],[8],[3],[-1],[1],[3],[9],[5],[-4],[9],[2],[10],[-2],[10],[9],[1],[4],[-1],[-7],[10],[-6],[9],[-3],[-5],[-9],[-2],[10],[8],[-8],[-4],[-2],[7],[4],[-5],[-8],[-1],[9],[2],[-4],[-10],[3],[-5],[5],[-7],[-2],[10],[-5],[2],[-2],[-10],[-3],[7],[-1],[-4],[5],[-8],[-8],[-3],[4],[8]], dtype = "uint8")#candidate|4027|(728, 1)|const|uint8
call_4025 = relay.TupleGetItem(func_2279_call(relay.reshape(var_4026.astype('int8'), [15, 1, 5]), relay.reshape(const_4027.astype('uint8'), [728,]), ), 1)
call_4028 = relay.TupleGetItem(func_2282_call(relay.reshape(var_4026.astype('int8'), [15, 1, 5]), relay.reshape(const_4027.astype('uint8'), [728,]), ), 1)
output = relay.Tuple([call_4012,call_4025,var_4026,const_4027,])
output2 = relay.Tuple([call_4013,call_4028,var_4026,const_4027,])
func_4034 = relay.Function([var_4026,], output)
mod['func_4034'] = func_4034
mod = relay.transform.InferType()(mod)
var_4035 = relay.var("var_4035", dtype = "int8", shape = (75,))#candidate|4035|(75,)|var|int8
output = func_4034(var_4035)
func_4036 = relay.Function([var_4035], output)
mutated_mod['func_4036'] = func_4036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2791_call = mod.get_global_var('func_2791')
func_2793_call = mutated_mod.get_global_var('func_2793')
call_4051 = relay.TupleGetItem(func_2791_call(), 0)
call_4052 = relay.TupleGetItem(func_2793_call(), 0)
output = relay.Tuple([call_4051,])
output2 = relay.Tuple([call_4052,])
func_4063 = relay.Function([], output)
mod['func_4063'] = func_4063
mod = relay.transform.InferType()(mod)
mutated_mod['func_4063'] = func_4063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4063_call = mutated_mod.get_global_var('func_4063')
call_4064 = func_4063_call()
output = call_4064
func_4065 = relay.Function([], output)
mutated_mod['func_4065'] = func_4065
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4087 = relay.const([[[2.359272,3.771915,-4.987641,8.529424],[-4.870410,8.992444,6.079852,-0.694490],[-7.758552,-7.590065,5.866464,-9.065822],[2.754467,-7.998351,4.545391,-9.933785],[1.929528,-3.931573,0.027004,0.746651],[2.700176,-9.489575,-7.386772,-9.910919],[-2.402543,-0.939134,8.131694,2.145252],[4.761737,-3.100199,3.219996,-7.526941]],[[-2.367050,-2.057478,-7.791308,2.985214],[-4.848116,-5.453871,-6.194630,-4.418460],[-6.589934,-9.327238,8.169769,-8.958501],[1.672782,-3.791942,7.266385,-8.508826],[3.923401,0.085215,-6.168562,-3.069677],[-7.666331,5.580019,8.045458,4.166216],[-0.446173,8.816325,0.790849,6.002268],[-0.917963,7.388235,-4.615108,2.455374]],[[-2.999823,5.757662,2.077824,-3.033142],[-3.476167,6.009083,6.454377,2.119414],[-7.975238,4.227891,9.415571,9.647006],[-1.286330,0.861955,-8.067850,6.867646],[-2.581394,3.420726,-9.419715,3.483563],[8.924544,-1.611017,-6.175926,4.983989],[-9.544193,-8.577396,6.585119,8.855543],[1.535234,-2.250566,6.039825,-4.317679]],[[-2.704124,5.407658,8.180464,8.894881],[1.420241,2.792464,-6.673344,3.808182],[-9.070848,-8.489289,3.075016,4.836181],[-9.248840,-1.884518,1.421556,1.964900],[-8.776455,-0.055975,-0.519402,-6.652537],[3.405408,1.553403,-4.565973,-5.856888],[-7.199263,-8.497620,-6.592350,-1.852097],[0.821862,-4.207886,-6.015580,-9.596882]],[[1.927147,-2.737223,6.920653,5.482978],[1.414678,-3.385430,7.451032,-3.882226],[7.847172,3.071391,-0.654643,-4.975574],[-7.661935,1.197259,2.705132,1.970027],[-0.512496,-5.298098,8.530654,1.589317],[-1.230118,-4.343368,-4.679268,0.668116],[-7.164362,-0.071264,0.284857,-1.654257],[9.686642,-2.030326,-4.610580,5.943719]],[[7.765329,-5.516844,-3.999596,4.684032],[3.448666,-8.274453,-8.621810,8.842430],[9.519061,-8.480614,-3.087257,-1.248356],[-1.354290,-5.887404,6.396723,2.040381],[9.275947,4.303999,7.625467,-1.496923],[-5.855596,7.811096,6.984942,6.324267],[-7.018112,4.137352,8.796675,-1.834778],[-6.639923,-2.447050,1.503561,-1.743769]],[[2.847414,-3.588182,3.784700,1.195821],[3.101224,-0.010948,3.263530,2.382865],[7.580720,-6.366611,8.737741,-4.339181],[-2.710578,9.714126,6.874822,-7.828064],[8.660335,2.464104,-4.589973,-1.630537],[4.489502,-5.258336,6.659533,-1.906946],[-8.167597,8.974440,-8.461012,9.045615],[-6.214928,-9.286602,-6.732097,-2.579426]],[[8.717918,-6.303810,-4.872578,3.398946],[-9.493407,-1.884373,-7.064944,-2.647592],[0.877260,-4.662556,-2.537638,-7.357571],[-1.160639,-6.992255,-3.272113,-4.903001],[-3.456021,3.581201,4.551935,1.610700],[-1.038371,6.319492,-5.285603,9.190490],[3.280020,2.601665,2.365920,-3.266749],[-6.993977,-6.582335,0.003455,-7.605968]]], dtype = "float32")#candidate|4087|(8, 8, 4)|const|float32
uop_4088 = relay.sin(const_4087.astype('float32')) # shape=(8, 8, 4)
uop_4091 = relay.sigmoid(uop_4088.astype('float32')) # shape=(8, 8, 4)
func_3553_call = mod.get_global_var('func_3553')
func_3555_call = mutated_mod.get_global_var('func_3555')
call_4101 = relay.TupleGetItem(func_3553_call(), 1)
call_4102 = relay.TupleGetItem(func_3555_call(), 1)
uop_4103 = relay.atanh(uop_4091.astype('float64')) # shape=(8, 8, 4)
output = relay.Tuple([call_4101,uop_4103,])
output2 = relay.Tuple([call_4102,uop_4103,])
func_4114 = relay.Function([], output)
mod['func_4114'] = func_4114
mod = relay.transform.InferType()(mod)
mutated_mod['func_4114'] = func_4114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4114_call = mutated_mod.get_global_var('func_4114')
call_4115 = func_4114_call()
output = call_4115
func_4116 = relay.Function([], output)
mutated_mod['func_4116'] = func_4116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3558_call = mod.get_global_var('func_3558')
func_3559_call = mutated_mod.get_global_var('func_3559')
call_4124 = func_3558_call()
call_4125 = func_3558_call()
output = call_4124
output2 = call_4125
func_4128 = relay.Function([], output)
mod['func_4128'] = func_4128
mod = relay.transform.InferType()(mod)
mutated_mod['func_4128'] = func_4128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4128_call = mutated_mod.get_global_var('func_4128')
call_4129 = func_4128_call()
output = call_4129
func_4130 = relay.Function([], output)
mutated_mod['func_4130'] = func_4130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2909_call = mod.get_global_var('func_2909')
func_2910_call = mutated_mod.get_global_var('func_2910')
call_4142 = func_2909_call()
call_4143 = func_2909_call()
output = relay.Tuple([call_4142,])
output2 = relay.Tuple([call_4143,])
func_4144 = relay.Function([], output)
mod['func_4144'] = func_4144
mod = relay.transform.InferType()(mod)
mutated_mod['func_4144'] = func_4144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4144_call = mutated_mod.get_global_var('func_4144')
call_4145 = func_4144_call()
output = call_4145
func_4146 = relay.Function([], output)
mutated_mod['func_4146'] = func_4146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2909_call = mod.get_global_var('func_2909')
func_2910_call = mutated_mod.get_global_var('func_2910')
call_4175 = func_2909_call()
call_4176 = func_2909_call()
output = call_4175
output2 = call_4176
func_4183 = relay.Function([], output)
mod['func_4183'] = func_4183
mod = relay.transform.InferType()(mod)
output = func_4183()
func_4184 = relay.Function([], output)
mutated_mod['func_4184'] = func_4184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4183_call = mod.get_global_var('func_4183')
func_4184_call = mutated_mod.get_global_var('func_4184')
call_4215 = func_4183_call()
call_4216 = func_4183_call()
output = call_4215
output2 = call_4216
func_4219 = relay.Function([], output)
mod['func_4219'] = func_4219
mod = relay.transform.InferType()(mod)
output = func_4219()
func_4220 = relay.Function([], output)
mutated_mod['func_4220'] = func_4220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3628_call = mod.get_global_var('func_3628')
func_3629_call = mutated_mod.get_global_var('func_3629')
call_4221 = relay.TupleGetItem(func_3628_call(), 0)
call_4222 = relay.TupleGetItem(func_3629_call(), 0)
output = call_4221
output2 = call_4222
func_4237 = relay.Function([], output)
mod['func_4237'] = func_4237
mod = relay.transform.InferType()(mod)
output = func_4237()
func_4238 = relay.Function([], output)
mutated_mod['func_4238'] = func_4238
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4239 = relay.var("var_4239", dtype = "float32", shape = (6, 9, 7))#candidate|4239|(6, 9, 7)|var|float32
uop_4240 = relay.rsqrt(var_4239.astype('float32')) # shape=(6, 9, 7)
uop_4242 = relay.asin(uop_4240.astype('float32')) # shape=(6, 9, 7)
bop_4249 = relay.not_equal(uop_4240.astype('bool'), relay.reshape(uop_4242.astype('bool'), relay.shape_of(uop_4240))) # shape=(6, 9, 7)
output = bop_4249
output2 = bop_4249
func_4275 = relay.Function([var_4239,], output)
mod['func_4275'] = func_4275
mod = relay.transform.InferType()(mod)
var_4276 = relay.var("var_4276", dtype = "float32", shape = (6, 9, 7))#candidate|4276|(6, 9, 7)|var|float32
output = func_4275(var_4276)
func_4277 = relay.Function([var_4276], output)
mutated_mod['func_4277'] = func_4277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3558_call = mod.get_global_var('func_3558')
func_3559_call = mutated_mod.get_global_var('func_3559')
call_4320 = func_3558_call()
call_4321 = func_3558_call()
func_2580_call = mod.get_global_var('func_2580')
func_2582_call = mutated_mod.get_global_var('func_2582')
const_4332 = relay.const([7,-10,9,-5,-2,-4,-3,2,2,8,6,-1,-4,9,2,-5,9,-1,7,-1,1,10,10,3,5,-9,1,-2,-10,7,5,3,9,-2,10,-5,-3,-6,-9,6,-10,5,-4,6,-1,6,-9,10,10,6,7,10,10,-4,5,-5,2,6,-8,-10,9,5,-2,8,6,2,7,5,6,-8,-9,5,2,7,-8,-1,2,5,-10,6,8,1,-7,-5,-8,-5,-4,10,4,6,-6,-8,-2,10,5,9,-3,-9,1,-5,-6,7,3,-6,7,-8,8,9,1,5,7,-9,6,-1,3,9,-6,-9,-4,-5,-6,3,-1,7,6,-9,-8,1,8,3,8,1,8,5,7,-4,5,1,2,9,2,10,6,-3,3,-8,-10,7,10,-2,3,2,-3,-5,10,2,-2,1,-4,-4,2,2,-10,-8,10,-9,-5,-1,3,5,10,7,-2,1,3,-4,9,5,-4,2,-4,-9,4,-9,-7,-2,4,10,6,-1,-9,3,3,-7,-2,3,2,7,3,2,-10,9,-4,9,10,-10,-7,9,3,-8,-5,-3,4,-4,5,9,10,7,-8,-5,-6,-9,8,-4,-4,-5,3,7,-7,-8,-6,-6,-6,-2,9,3,10,10,-10,8,7,4,-1,-9,3,-1,-4,-5,1,-5,3,-8,9,-3,-2,-4,4,1,10,-6,-7,10,-3,2,-4,-6,4,-4,-2,4,5,5,6,7,-5,-7,-9,2,5,7,2,8,7,-8,6,5,10,3,5,1,2,-10,4,2,-7,-9,-2,4,-7,-8,-4,6,-2,-9,-2,7,-8,-6,1,4,-7,-7,-1,8,-3,3,-1,3,-10,2,-5,-6,10,-9,-10,-8,-7,-7,8,-6,-6,-2,8,10,-2,-9,-5,-1,-7,-5,3,-7,2,9,-1,-3,-2,4,2,7,10,2,3,10,4,-8,-9,-9,8,1,3,-6,10,-4,-6,8,-8,-1,4,10,5,8,10,-6,-7,10,4,-4,8,7,-10,-9,-5,-7], dtype = "uint32")#candidate|4332|(384,)|const|uint32
call_4331 = func_2580_call(relay.reshape(const_4332.astype('uint32'), [16, 2, 12]))
call_4333 = func_2580_call(relay.reshape(const_4332.astype('uint32'), [16, 2, 12]))
output = relay.Tuple([call_4320,call_4331,const_4332,])
output2 = relay.Tuple([call_4321,call_4333,const_4332,])
func_4335 = relay.Function([], output)
mod['func_4335'] = func_4335
mod = relay.transform.InferType()(mod)
output = func_4335()
func_4336 = relay.Function([], output)
mutated_mod['func_4336'] = func_4336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3558_call = mod.get_global_var('func_3558')
func_3559_call = mutated_mod.get_global_var('func_3559')
call_4365 = func_3558_call()
call_4366 = func_3558_call()
output = call_4365
output2 = call_4366
func_4384 = relay.Function([], output)
mod['func_4384'] = func_4384
mod = relay.transform.InferType()(mod)
mutated_mod['func_4384'] = func_4384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4384_call = mutated_mod.get_global_var('func_4384')
call_4385 = func_4384_call()
output = call_4385
func_4386 = relay.Function([], output)
mutated_mod['func_4386'] = func_4386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4237_call = mod.get_global_var('func_4237')
func_4238_call = mutated_mod.get_global_var('func_4238')
call_4409 = func_4237_call()
call_4410 = func_4237_call()
output = call_4409
output2 = call_4410
func_4415 = relay.Function([], output)
mod['func_4415'] = func_4415
mod = relay.transform.InferType()(mod)
output = func_4415()
func_4416 = relay.Function([], output)
mutated_mod['func_4416'] = func_4416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2791_call = mod.get_global_var('func_2791')
func_2793_call = mutated_mod.get_global_var('func_2793')
call_4420 = relay.TupleGetItem(func_2791_call(), 0)
call_4421 = relay.TupleGetItem(func_2793_call(), 0)
const_4422 = relay.const([-4,-8,7,-4,-7,4,8,6,7,6,-7,9,-9,-9,2,8,2,-4,-1,2,3,9,-6,-5,-5,10,-9,-1,5,7,-5,-5,4,-6,10,-4,5,-4,-10,-7,2,-6,-6,1,1,1,4,5,-7,-2,-10,-8,2,10,-3,-7,-4,-5,-2,-4,-4,-10,-2,6,-5,-4,9,-2,6,-2,-8,-1,2,3,-4,-8,3,-7,-3,2,-5,1,-10,4,-4,2,-5,-4,-1,-2,5,3,10,-3,-5,8,-3,4,3,-7,4,9,-4,-8,-2,-10,-2,7,3,2,-6,9,-1,-1,3,-1,9,8,-3,-6,7,-1,9,3,-7,1,7,-3,7,3,1,-8,-4,-4,1,1,6,-10,-10,-8,-8,-2,-8,-3,6,6,-2,10,9,2,-3,-1,-4,5,-4,3,-1,6,8,6,-9,-5,-5,6,10,5,10,-4,6,10,-4,1,8,5,-1,1,-3,9,-3,3,3,-9,-3,9,4,-9,-4,4,-10,-9,-1,-8,-9,4,4,-9,5,-1,-1,-8,-2,3,-7,-10,-5,-5,1,1,-2,4,-2,2,1,6,6,6,8,5,-8,2,4,-10,-5,-5,-9,3,-1,9,-8,3,6,1,-1,-1,9,-2,5,6,-6,6,-1,7,2,6,-8,4,-10,-9,-9,-10,6,-1,-8,10,9,1,3,-2,1,-6,6,-4,3,7,-4,10,3,-2,8,6,7,7,-3,-6,-6,-5,10,-9,5,-5,-7,10,4,-2,5,2,-5,-4,8,5,2,-6,-1,7,3,6,7,-9,-9,5,-6,8,8,10,-3,9,6,8,-10,-5,7,10,-7,-4,9,2,8,9,-3,-1,-5,-2,8,10,6,-1,-7,8,-2,-2,-4,8,-8,10,-5,10,5,-1,-3,-1,6,-4,6,9,-6,1,-7,4,6,-9,-6,1,10,-2,-10,-3,-8,-9,1,-2,-9,7,-2,5,4,8,-2,1,10,-4,8,-9,4,-1,-8,-2,-8,6,9,-9,-3,2,6,9,9,-8,-1,-5,7,-2,1,-3,-10,-8,-10,1,-3,-1,8,-7,-3,6,-4,-1,-7,5,6,6,8,-6,-10,-2,-1,4,-2,6,5,-9,3,9,2,1,-3,5,-2,10,9,-4,6,10,8,3,-10,-2,4,-6,-7,-6,3,-4,4,6,7,-4,10,10,1,-1,8,5], dtype = "int8")#candidate|4422|(450,)|const|int8
bop_4423 = relay.mod(call_4420.astype('float64'), relay.reshape(const_4422.astype('float64'), relay.shape_of(call_4420))) # shape=(450,)
bop_4426 = relay.mod(call_4421.astype('float64'), relay.reshape(const_4422.astype('float64'), relay.shape_of(call_4421))) # shape=(450,)
output = relay.Tuple([bop_4423,])
output2 = relay.Tuple([bop_4426,])
func_4438 = relay.Function([], output)
mod['func_4438'] = func_4438
mod = relay.transform.InferType()(mod)
output = func_4438()
func_4439 = relay.Function([], output)
mutated_mod['func_4439'] = func_4439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2791_call = mod.get_global_var('func_2791')
func_2793_call = mutated_mod.get_global_var('func_2793')
call_4475 = relay.TupleGetItem(func_2791_call(), 0)
call_4476 = relay.TupleGetItem(func_2793_call(), 0)
output = relay.Tuple([call_4475,])
output2 = relay.Tuple([call_4476,])
func_4499 = relay.Function([], output)
mod['func_4499'] = func_4499
mod = relay.transform.InferType()(mod)
output = func_4499()
func_4500 = relay.Function([], output)
mutated_mod['func_4500'] = func_4500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3589_call = mod.get_global_var('func_3589')
func_3590_call = mutated_mod.get_global_var('func_3590')
call_4514 = relay.TupleGetItem(func_3589_call(), 0)
call_4515 = relay.TupleGetItem(func_3590_call(), 0)
func_1144_call = mod.get_global_var('func_1144')
func_1149_call = mutated_mod.get_global_var('func_1149')
const_4525 = relay.const([False,False,True,True,True,True,False,True,False,False,True,True,True,False,False,True,True,False,False,True,False,False,False,False,True,False,False,True,True,False,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,False,False,True,False,False,False,False,False,False,False,True,False,False,False,False,True,False,True,False,True,False,False,True,False,True,True,True,False,True,False,False,False,False,True,False,True,True,True,True,True,True,True,False,False,True,False,True,True,True,True,False,False,True,True,False,False,True,True,True,False,False,True,False,False,False,True,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True,True,False,False,True,False,True,False,True,False,False,True,True,True,False,True,False,True,False,False,False,False,True,False,True,True,False,True,True,True,True,True,False,True,True,True,True,False,True,True,False,False,False,True,True,False,False,True,False,False,True,False,True,False,True,False,True,True,True,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,False,True,False,True,False,False,False,True,True,False,False,False,True,True,False,False,True,True,True,True,True,True,True,False,False,True,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,False,True,False,True,True,True,False,False,False,True,True,True,True,False,True,False,False,True,False,False,True,True,True,False,True,False,True,True,True,True,True,True,True,True,False,False,True,False,False,True,True,True,False,False,True,True,True,True,True,True,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,False,True,False,True,False,False,True,False,False,False,False,True,False,True,False,True,True,True,False,True,True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,True,False,False,False,False,False,False,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,True,False,True,False,True,False,False,True,False,True,True,False,False,True,False,False,True,False,True,True,False,True,True,True,False,True,True,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,True,False,False,False,False,True,False,True,False,False,False,True,True,True,True,False,False,False,True,False,False,True,True,True,True,True,True,True,False,True,True,False,True,True,False,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,True,True,False,True,True,False,True,False,False,True,True,True,True,True,True,True,True,False,True,False,True,False,False,False,False,False,True,False,True,True,True,True,False,False,False,True,False,False,False,False,True,True,True,True,False,False,False,False,False,True,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,False,False,True,False,False,False,True,True,True,False,False,False,False,False,False,True,False,False,False,False,False,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,False,False,True,True,False,True,False,True,False,False,False,False,True,True,True,True,True,False,False,True,False,True,True,False,False,False,True,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,True,False,False,False,True,False,True,True,True,True,False,True,True,False,True,False,True,True,False,False,False,True,True,True,True,False,False,False,True,True,True,False,True,False,False,True,False,True,False,True,False,True,False,True,True,True,False,True,True,False,True,True,True,False,False,False,False,False,False,True,True,False,True,True,False,False,False,False,True,False,True,False,True,False,True,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,True,True,False,False,False,True,False,True,True,False,False,True,True,False,True,True,True,True,False,True,False,True,True,True,True,False,True,True,True,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,False,True,True,True,True,True,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,True,True,False,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,False,False,True,False,True,False,False,True,False,True,False,False,False,False,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,False,True,True,False,True,True,False,True,False,True,False,False,True,True,False,False,False,False,False,False,True,False,False,False,False,False,False,True,False,True,False,True,False,False,True,False,True,True,True,True,False,False,False,False,True,False,False,True,True,False,True,False,True,True,False,True,True,False,True,True,False,True,False,False,True,True,False,False,True,False,False,True,False,False,True,True,False,True,False,True,False,True,True,True,False,True,False,True,False,True,False,False,True,True,False,False,False,True,True,True,True,True,True,True,True,False,False,True,False,False,True,False,True,False,True,True,False,True,False,False,True,False,False,False,True,False,False,False,True,True,True,False,False,False,True,True,True,True,True,True,True,False,True,False,False,False,True,False,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,True,False,False,False,False,True,True,True,True,False,False,False,False,True,False,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,False,False,False,True,False,True,False,False,True,True,False,True,True,True,True,True,False,False,False,True,False,True,False,False,True,False,True,True,True,True,True,True,False,True,False,False,False,True,False,True,False,False,False,True,False,False,True,False,False,True,False,False,False,False,True,True,False,False,False,True,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,True,True,False,False,True,True,False,False,True,False,True,False,False,True,True,True,True,False,True,True,True,False,False,False,False,True,False,False,False,True,False,False,False,False,False,False,False,False,False,True,False,True,False,False,False,True,True,False,True,False,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,False,True,False,True,False,False,False,False,False,True,True,True,True,True,False,False,True,True,True,True,False,False,True,True,True,False,False,False,False,True,False,False,False,False,True,False,True,True,False,True,False,False,False,False,True,False,False,False,True,True,True,True,True,False,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,False,True,True,False,True,True,True,False,False,True,True,True,False,True,True,False,True,True,True,False,False,True,True,False,False,True,True,True,False,True,False,False,False,False,False,False,True,True,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,True,False,True,False,True,True,True,True,True,True,True,True,False,True,True,True,True,False,False,True,True,False,True,True,True,True,True,True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,False,False,False,True,True,True,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,False,False,False,True,False,False,True,False,False,True,True,False,True,True,False,False,True,False,True,False,False,True,True,True,False,True,True,True,False,False,False,False,False,False,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,True,False,True,False,False,True,False,True,False,False,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,False,True,True,True,True,False,False,False,False,False,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,False,True,True,True,False,True,True,True,False,False,True,False,False,True,False,False,True,True,False,True,True,True,False,False,True,False,False,False,True,False,False,True,True,True,True,False,False,False,True,False,True,False,False,True,True,True,False,True,False,False,False,True,True,False,False,False,False,False,False,True,False,False,True,False,True,False,False,True,False,True,True,True,False,False,True,True,True,True,False,True,True,True,True,True,True,True,True,False,True,False,True,False,False,False,False,False,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True,False,False,False,True,False,True,False,False,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,False,False,True,True,False,False,False,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,True,False,True,False,False,False,False,False,False,False,False,False,True,True,False,False,True,False,True,True,True,False,True,False,True,False,False,True,False,True,False,True,True,True,True,False,True,False,False,False,False,False,False,False,True,False,False,False,False,True,False,True,True,True,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,True,False,False,True,False,False,True,False,False,True,False,True,True,True,False,True,False,False,True,False,True,True,False,True,True,True,True,True,False,True,False,True,True,False,False,True,False,True,True,False,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,True,False,True,False,False,False,True,True,False,False,True,False,True,True,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,True,True,False,True,True,True,False,False,False,True,False,True,True,True,True,True,False,False,True,False,True,True,False,False,True,False,True,True,False,True,True,True,False,True,False,False,True,True,False,True,False,False,False,True,True,True,True,False,False,False,False,True,True,True,True,False,True,False,False,True,True,True,True,False,True,True,False,False,False,False,True,True,False,True,False,True,False,True,True,False,False,False,False,True,True,True,False,False,False,False,True,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,True,True,True,False,True,True,False,True,True,True,True,True,True,True,True,True,False,False,True,False,True,True,True,True,False,True,True,True,False,True,True,True,False,True,False,False,False,False,True,True,False,False,False,True,True,True,False,False,False,False,False,True,True,True,False,True,False,True,True,True,True,False,False,True,True,False,True,False,True,True,True,True,True,False,False,True,True,True,True,True,True,True,False,False,False,True,False,True,False,True,False,True,True,False,True,True,True,False,True,False,True,False,True,True,False,True,False,False,False,True,True,True,False,False,False,False,True,False,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True,False,True,True,True,True,True,False,False,True,True,False,True,True,False,False,True,False,True,False,True,False,True,True,False,False,False,True,True,True,True,False,True,False,True,True,True,True,True,True,False,False,True,True,False,True,True,True,True,False,False,True,True,True,False,True,True,True,False,False,False,True,False,False,True,False,True,False,True,False,True,True,False,False,False,False,False,True,False,True,True,False,False,False,True,True,False,False,False,False,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,True,True,False,False,True,True,True,True,True,False,False,False,False,True,False,False,True,False,False,True,False,True,True,False,False,False,True,False,False,True,False,False,False,True,False,True,False,True,True,True,True,True,True,True,False,False,False,True,False,False,False,False,True,False,False,True,False,True,True,False,True,False,False,True,True,False,True,True,True,False,False,True,True,True,False,True,True,False,True,True,False,True,True,False,True,True,True,True,True,True,False,False,True,False,True,False,True,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,True,False,True,True,False,False,True,True,False,False,False,False,True,True,False,False,True,False,False,False,True,False,True,False,True,False,True,True,True,False,False,True,True,True,False,True,True,True,True,True,True,True], dtype = "bool")#candidate|4525|(2400,)|const|bool
call_4524 = relay.TupleGetItem(func_1144_call(relay.reshape(const_4525.astype('bool'), [10, 15, 16]), relay.reshape(const_4525.astype('bool'), [10, 15, 16]), relay.reshape(call_4514.astype('float32'), [450,]), ), 3)
call_4526 = relay.TupleGetItem(func_1149_call(relay.reshape(const_4525.astype('bool'), [10, 15, 16]), relay.reshape(const_4525.astype('bool'), [10, 15, 16]), relay.reshape(call_4514.astype('float32'), [450,]), ), 3)
func_4034_call = mod.get_global_var('func_4034')
func_4036_call = mutated_mod.get_global_var('func_4036')
var_4538 = relay.var("var_4538", dtype = "int8", shape = (75,))#candidate|4538|(75,)|var|int8
call_4537 = relay.TupleGetItem(func_4034_call(relay.reshape(var_4538.astype('int8'), [75,])), 3)
call_4539 = relay.TupleGetItem(func_4036_call(relay.reshape(var_4538.astype('int8'), [75,])), 3)
uop_4547 = relay.atan(call_4537.astype('float32')) # shape=(728, 1)
uop_4549 = relay.atan(call_4539.astype('float32')) # shape=(728, 1)
const_4561 = relay.const([[-9.920023,-4.360635,3.334734,-5.933591,6.379326,1.696606,7.471216,5.933854,-2.186427],[1.879715,-0.533474,7.947583,-8.375643,-5.038218,-2.845402,-3.802868,-8.232005,6.231349],[-9.455853,9.569875,-9.298457,-8.741762,1.174047,2.011373,-3.974180,9.491416,2.489295],[8.015001,2.638796,-6.159893,5.299839,-4.198142,5.961421,-4.730107,8.711261,-8.168327],[-5.956137,7.356199,-6.001389,3.822460,3.221020,8.621929,-6.614810,-2.024735,4.179602],[6.932919,0.545519,-4.951853,3.023730,0.914752,8.605738,-7.794752,-4.931575,4.389117],[7.351598,-3.638027,8.918777,0.575208,-8.633995,3.824021,-3.917081,-9.078250,-7.813063],[1.196436,0.869629,-8.191287,-4.597953,-8.888420,9.393215,1.621717,4.155143,0.303270],[9.014716,-5.389400,4.433137,0.601020,-4.223379,9.826748,2.074972,2.193112,8.061652],[1.323556,-5.616197,5.418999,6.654408,-5.845503,-2.745944,-0.631383,3.776966,7.347586],[-3.794133,-4.291885,-5.959163,-9.183848,-0.575251,5.326397,6.879451,8.229170,-7.590435],[8.561386,7.490501,-6.705053,-7.470016,-1.033386,2.930390,-8.304691,-5.567246,9.987606],[-0.352256,-1.982069,0.096696,3.784248,-4.457817,-7.750275,7.131118,4.894610,-6.497595],[-0.867749,-8.169579,-3.635657,-1.666974,3.659737,4.367805,0.565040,-9.185261,4.379391],[7.066916,9.089003,0.006517,3.899155,7.109341,-5.332630,-8.790970,-6.111449,5.410690],[9.603184,5.627098,-6.624356,2.253861,4.972592,-4.228279,5.553094,0.568749,7.127632],[-5.139404,8.865613,7.009575,3.038312,-8.194596,-7.696370,-0.688630,3.622769,3.800030],[1.368180,0.814805,-6.174572,0.179737,-0.347341,-2.609882,2.477238,-8.984216,4.468237],[-5.885848,1.455881,-9.157690,-0.868761,0.179589,5.207999,-5.664718,8.979949,6.151562],[8.693511,0.690523,6.967347,9.282337,7.248818,0.678052,-4.801686,9.979376,-2.785358],[5.112499,4.145656,-2.673603,3.833862,2.284641,-4.779207,9.323053,4.183064,6.063568],[-2.822220,3.175310,-1.720709,-2.050827,8.322562,3.677257,-2.510629,-7.268759,0.913291],[-4.888768,7.144486,-3.942303,-3.124324,4.451472,-9.250633,-4.703327,-5.223348,-3.745032],[-8.856522,5.763685,8.213637,1.571438,2.614555,6.723589,-0.555258,-7.369658,3.562313],[2.135036,-8.490343,1.104158,-6.997950,6.510942,5.935824,0.746924,2.496828,1.908341],[4.772222,-9.635960,2.679780,-1.164204,8.257389,9.238014,0.316301,-0.076723,-4.311596],[-8.216160,7.919549,4.299549,-5.542425,-7.186285,2.138088,-4.327435,-6.383096,4.426468],[-9.172528,1.695203,-3.024608,-6.652968,9.885416,3.997344,-5.356991,-9.584040,-4.138244],[-8.369115,4.215843,-2.109890,2.935771,8.451453,6.437171,8.616316,-4.330946,0.907008],[1.738491,-3.388201,-4.218378,-1.249064,-9.081611,-7.099077,-7.675078,6.462438,1.068897],[-2.489098,-1.537234,-7.600163,3.256779,7.218804,-2.525826,-4.839797,-9.082200,-4.397977],[9.193897,8.463127,-9.516921,-0.239896,-4.043972,-4.421917,1.880603,-9.975584,-6.878545],[0.046018,-5.330115,-1.920250,3.968208,3.546120,6.199622,-5.557173,-1.769979,-6.405749],[6.741788,-2.439017,-1.757060,8.422447,0.304407,6.724419,-9.762751,3.386895,0.438686],[6.459855,0.402109,-9.362723,-5.694816,1.873454,-7.095055,1.020286,-8.898253,-3.594216],[-2.936285,-4.426436,8.790622,-8.367454,-1.730893,1.651637,3.854879,-4.318856,2.171254],[8.372532,0.848610,-7.571850,4.227462,3.083057,8.407641,-8.349722,0.059434,-4.109112],[7.569581,-2.705430,-4.643704,3.441853,-7.728061,-3.898897,7.013580,9.406890,-0.939583],[-6.846320,-1.384044,8.903573,7.083514,8.166298,-6.865409,-9.920232,-7.672555,7.721969],[-1.295149,-4.141835,-6.848284,-7.493492,2.363545,-9.694129,4.968744,7.794738,-3.020965],[-1.046354,-8.336012,-7.406982,0.722887,-2.203785,0.354321,-4.207678,2.355375,-8.024267],[-7.838199,7.696582,5.937529,0.268791,-0.949453,-3.071506,-9.176841,7.843887,-3.580372],[7.403178,-7.201180,-0.606874,-7.981248,4.553373,8.256337,2.150633,-1.188248,1.847742],[8.477463,-5.062691,2.644323,-9.874056,9.453917,3.221217,-8.718003,5.373510,-5.260087],[-7.426936,7.645468,-2.984377,-3.358049,-8.864986,-1.048994,-2.313623,-0.387151,-8.295778],[2.655971,6.734569,-7.198041,-8.181443,-4.905979,2.007096,0.737366,5.434125,8.576893],[-4.302824,6.773067,-4.316833,-4.881140,2.673785,3.347846,3.977470,0.580292,-9.984257],[2.421036,-6.994470,-9.157149,-9.181050,3.031668,-5.942051,-5.055087,-8.293836,1.428973],[8.115130,2.368016,3.335763,-9.205916,9.464811,0.621266,6.387753,5.580786,-0.025494],[7.781522,2.913245,-0.496894,6.919457,-4.714448,3.011580,-5.641818,-2.481744,2.674045],[0.663272,-0.305124,9.958329,-8.666195,-1.249930,-5.019639,3.891150,7.381501,9.758528],[5.508847,-1.905812,-0.913272,0.244510,2.227780,5.675128,2.445152,-2.655662,4.169226],[-3.825632,8.120411,8.175012,4.933595,0.270823,-7.684374,6.846013,-8.153943,4.382126],[1.119768,1.884427,-7.547764,3.518843,8.914382,5.954204,-9.368174,-0.426179,-8.903286],[4.340517,2.824678,5.152912,6.398221,1.842975,-7.042891,2.114406,9.056989,-9.876679],[9.586280,-3.876333,-0.776230,3.521825,0.460919,-7.762798,-4.656328,1.338487,-7.076346],[3.611700,9.984972,9.574200,0.256534,7.270518,-8.296688,1.277481,-9.106569,-2.887673],[7.214315,7.130789,-8.063156,4.326783,0.857957,-8.528968,3.229036,-4.999821,-9.954498],[-7.141297,-9.526745,-5.060866,-7.610752,-5.107361,3.571218,8.391721,-4.702837,9.135920],[-2.098076,0.965854,-7.780167,3.811797,5.467275,-8.855974,-2.210063,-7.328409,8.693424],[5.945173,-1.551480,-8.532984,-6.541789,-3.768063,-1.138079,7.569153,-7.624991,-5.354447],[-1.755243,-8.262286,4.947406,6.587612,-5.754934,-9.558157,9.925931,5.878417,0.499112],[6.605227,3.523396,1.774607,-7.646389,-0.871059,6.411439,4.613328,-5.667562,-9.814442],[-5.152302,5.541423,4.774379,-4.337063,1.357437,-8.135708,6.615734,1.101061,0.697576],[-5.611721,5.059182,6.109937,-8.030813,1.278639,-1.739320,-7.785804,2.181229,0.725960],[-6.590707,1.342955,6.583295,-7.735901,-9.738012,4.664245,-9.619234,8.280371,-6.621229],[4.025457,9.249570,-9.352880,-5.198164,-2.215601,-5.724180,-5.008954,-3.211177,4.975312],[0.664938,-1.773920,8.845525,3.121821,-8.839730,0.004771,1.991011,4.621502,7.440528],[6.064453,-6.277621,-2.611838,7.075442,7.050079,-7.208559,-7.138084,8.873059,9.580750],[-2.155717,-8.040965,5.088975,-0.930918,-9.413558,0.585148,7.439193,9.770643,7.360527],[-8.040958,-1.079525,-7.565362,-0.996178,-0.273536,0.326687,-5.927893,8.913199,-1.153793],[7.644392,0.646677,-4.487036,6.513584,9.979315,-2.441523,-9.800749,-9.637030,-3.796959],[-5.013989,8.296499,-7.668384,-5.564722,-7.978758,-2.742725,0.176398,2.953093,3.899930],[5.945539,1.579223,-1.904770,0.378320,6.085222,6.257188,-3.789448,-4.571657,2.561479],[7.070487,-0.085027,2.020078,-8.833004,-5.589998,9.346719,-9.016820,-6.317016,-7.502848],[1.767501,-2.680891,4.645874,-3.872965,3.341176,5.055880,-4.084804,-0.815848,-3.184695],[3.387060,-6.911696,5.813431,5.612129,1.694386,1.663058,-9.683638,2.836795,4.957326],[6.051372,4.067945,4.494238,2.860685,3.438157,-8.037764,1.183762,-6.488944,3.590694],[1.188645,6.753065,-6.436549,-9.381451,7.193324,7.514223,-3.622211,3.455966,0.130161],[-1.190660,-8.101169,9.574827,-8.851107,-7.178203,-7.182830,-7.091574,-9.694805,-7.056391],[-1.291786,-3.247562,6.415916,9.578291,-0.443861,8.825631,9.556372,-5.998459,9.147232],[-9.448503,-9.837296,-1.896450,-2.503172,-4.317063,2.218900,0.907212,-7.215127,0.049847],[-9.392610,8.928317,0.867812,-3.458018,6.660116,-8.538170,-0.979137,-9.098316,2.263137],[-8.784027,2.896861,4.762834,2.608224,-4.592215,-6.670965,3.157859,-7.543557,8.536734],[6.952437,-3.978170,-7.050656,7.811262,5.502424,9.093720,5.720303,-3.230724,-6.861620],[5.941375,7.051849,0.154812,3.768330,-5.474700,-2.274285,-4.117988,2.811370,-6.132128],[4.448899,2.675692,0.561103,-4.265571,-8.359080,9.231898,-6.480870,-4.545007,-5.645896],[8.197309,4.411010,-0.392267,2.419403,9.518985,4.841587,-0.223756,-4.648569,-3.035674],[-8.080482,-8.382247,6.570112,9.090359,-2.522519,7.437252,-5.316367,-5.566218,-6.015472],[1.690915,3.949154,3.278921,-2.873819,-2.801425,1.989559,-0.415706,2.748747,-5.174681],[-8.487757,-9.587695,4.603463,1.018739,-1.504197,0.845169,-6.039037,-2.256949,-6.075000],[5.081882,0.638603,3.131240,-0.817705,-0.527876,-6.435356,-9.072345,-3.907346,4.276694],[5.912644,3.217948,-4.830438,-2.899762,1.517555,6.322497,-5.265212,-3.848079,-3.494485],[-5.504635,1.892249,-0.523234,0.253810,-3.171789,8.398715,-6.525640,5.217144,-7.495322],[-8.403456,-3.391243,7.089375,7.217809,-4.130008,0.556659,9.976328,6.423982,-3.936670],[-6.202742,6.854477,7.483409,-1.686811,7.397315,-4.979966,-3.167072,-9.226879,-5.878937],[-2.924346,-6.809270,-9.875540,5.130104,1.035286,-5.496732,-0.633032,-8.498414,-0.295322],[-0.913097,6.328303,-0.804572,6.702657,-9.439405,4.073723,8.086010,8.094633,0.420537],[6.263244,6.534932,6.923269,-7.273404,6.403564,6.571633,-8.793863,-2.972980,0.335804],[6.009655,6.256937,5.991214,2.164870,-5.335181,-6.544732,-7.435806,-5.982153,-1.713826],[0.867705,8.362570,6.213325,-6.809978,-7.248492,5.803850,1.656026,-9.825653,2.734379],[-3.428676,-2.761058,5.978157,-6.532111,-3.779865,7.003946,-2.038068,8.442664,9.028439],[0.920125,7.343243,6.497900,8.117001,5.070934,4.300625,6.712578,6.590938,8.856025],[-3.647261,-6.495597,-1.283748,-1.413740,4.269406,6.645020,-4.527197,-8.546756,-7.984375],[3.865260,9.520913,-1.781499,8.183834,-2.276269,1.811061,6.013063,6.566494,7.907743],[4.173310,-1.595665,5.413554,-1.671797,-9.716756,1.612943,-8.328348,1.248818,-4.926194],[-9.295401,9.093979,-2.469675,-8.702818,0.176073,-7.228822,-9.813945,-3.845246,-0.182621],[-1.763788,4.992810,8.847452,5.448981,0.675896,2.136801,-6.229332,9.979634,-3.998569],[2.574070,7.188237,-4.719200,8.467451,-3.751871,-7.798271,8.479432,1.404432,6.118751],[-4.032654,-6.987746,8.428961,5.338223,2.787551,-4.758047,-9.422308,5.096777,-5.388665],[8.316707,-8.406694,9.096371,-6.530395,1.765000,9.116701,9.339510,7.570919,-2.682272],[0.778853,0.779582,-0.332065,7.535957,1.623396,5.040926,-4.429302,6.958821,-5.346290],[9.237502,7.527347,-1.267328,-7.009975,-8.282708,6.971722,-0.653732,-8.785024,1.771722],[2.337413,-7.317359,1.822886,-5.076053,-5.950471,-5.700743,-2.416161,-7.379012,-7.107026],[5.444342,-0.357602,2.190308,-8.375783,-1.577469,1.325402,9.267369,-4.998017,7.514281],[8.435794,-8.735416,0.550944,-2.995097,-6.586914,9.036846,8.412106,6.594598,1.824597],[6.954243,9.271892,-3.283173,-4.926101,3.184465,9.482425,-9.468626,0.216393,5.625479],[-1.216991,-7.171189,-3.839556,1.229107,-5.848459,7.872084,3.227999,6.894110,-3.596768],[4.092591,-5.137177,-7.589032,2.450338,-3.600152,2.833114,0.616497,-5.038307,-9.363046],[-2.825703,-3.012974,5.397432,-7.781529,6.787792,7.886901,4.055349,-2.295902,1.586200],[-0.155674,5.165915,4.231792,-3.297735,-2.444974,7.301016,1.347992,8.378071,-1.478936],[7.970028,5.870643,3.060321,-2.362932,-1.496711,-8.830381,5.987113,-6.323567,5.103158],[0.419975,3.263886,-4.586671,0.109652,-3.217928,-7.287587,1.430927,6.102704,-0.376713],[2.338211,1.730779,5.137957,4.419061,-6.169462,7.401881,-9.394394,4.078271,6.834491],[-5.371961,7.516165,4.882554,6.426707,0.701283,3.610018,4.209781,4.144664,-9.047657],[-7.148775,7.451221,-9.595736,4.732749,-9.739032,-5.273739,-2.111953,-3.046601,8.210002],[9.298942,-9.696939,5.828094,-7.510432,-2.528940,4.147647,-8.498573,-9.072759,6.205315],[9.681293,6.488841,5.033172,9.256049,-7.878041,-8.761655,1.802041,8.102570,-7.261801],[1.272357,7.442396,-8.349510,3.367648,2.349314,0.276485,-6.684371,9.798233,-6.247172],[9.371337,-1.503901,6.971984,4.737020,7.841438,-8.060105,6.335842,-4.684585,3.426169],[9.307002,-7.873747,-8.319648,2.894896,-3.110655,2.787196,-3.682384,-5.615484,-5.727782],[9.156496,-2.163898,-9.854665,-5.673144,-5.698301,7.040413,-1.763489,-4.694497,0.701392],[-4.154447,2.142722,6.839375,7.848839,0.087068,-7.678595,9.322351,9.277806,-6.168883],[-0.006525,6.000473,-1.296687,-2.746985,-4.842317,2.469615,6.438001,-6.692920,-5.675711],[6.351142,7.505935,1.107976,2.992378,5.348043,-2.675354,-6.565631,7.935537,8.796390],[-2.472668,-1.880240,5.127108,-8.383496,4.176031,6.856387,-0.559511,5.682626,-7.721431],[-8.525001,1.187590,-9.629089,0.634710,-8.741137,5.596777,-4.264808,9.037255,-5.784661],[-4.258456,8.826410,5.547982,7.285409,-9.572969,-7.108906,9.289580,-8.106173,-0.162775],[-2.272929,2.694902,-9.353951,2.404802,3.194991,0.397610,8.147436,-8.877143,0.253583],[1.521363,-4.699134,2.714381,-8.166179,8.111557,5.063816,-6.138866,2.257360,-8.771556],[-4.625846,7.066549,-1.414920,5.934056,-0.341255,2.056354,4.072884,5.039027,-5.197047],[-0.532048,3.959253,2.469200,-2.038895,2.332521,3.521925,4.271961,2.433886,6.644497],[-9.596240,5.693612,0.701778,-3.624079,4.609662,-5.990134,9.098285,6.565170,-1.139435],[0.801842,-5.586295,-6.589550,4.186198,9.909560,-9.948285,-5.265330,4.619686,-0.194640],[-3.323024,2.290340,-1.445677,4.410498,8.472124,-0.368842,7.836690,-8.823077,-5.731782],[-6.668296,-0.163525,-8.983313,-9.279786,0.838888,-4.073635,-1.719924,0.752736,7.550612],[7.779491,7.681775,6.051854,-6.702140,0.011760,-5.242074,-9.547296,5.583547,-9.908097],[7.245892,2.944429,-3.737216,-3.892934,-1.531300,-9.761101,9.783555,9.876111,-3.650625],[5.542348,5.644882,3.712104,-3.640521,-7.242834,7.848902,-0.403413,-9.930702,9.931086],[7.594896,3.698490,7.567409,2.717571,-8.892971,1.764974,8.663847,1.121579,-4.009705],[-4.107784,-6.248351,-8.395310,0.970169,2.435336,-5.877867,-6.285965,-4.316548,-2.303838],[-3.197955,6.462509,-1.964730,9.595393,3.861548,-7.191155,-0.203457,-5.227758,-2.514576],[-4.664319,5.171346,8.859980,-3.068433,-8.413048,3.409320,9.295712,-2.639065,-1.954503],[3.965040,5.215844,6.704037,-8.539564,-3.522991,-7.671186,-7.763820,7.788516,-0.257113],[7.306324,-4.664492,-0.811385,-8.082110,7.034448,-5.373653,5.933250,-3.566128,-2.600363],[7.221882,6.370793,5.245456,-2.917832,-7.852628,-1.038723,-5.504149,1.318268,6.651857],[-0.375876,5.441075,-8.146601,-7.920992,-3.585019,-1.880919,-1.957881,5.091204,-5.093786],[1.096252,-2.926619,-4.387502,8.955799,0.667816,7.418796,-1.445017,-1.656777,-8.337063],[1.087328,8.754773,6.211695,-8.152679,4.604090,9.465416,-4.394938,-4.760762,-6.982202],[8.300690,5.958540,-2.998188,4.728421,-1.981464,6.289204,3.758735,0.810280,-3.400765],[-5.628872,-2.397502,-9.084305,9.795983,3.337199,-6.773898,-9.979666,6.069644,-6.103681],[4.340301,-7.554705,0.469659,-9.866253,-9.660834,3.888544,-6.466120,7.986432,6.934502],[-2.500540,-7.050101,-5.389845,7.963568,8.484793,-4.650263,-6.270410,0.108115,-6.056232],[-3.692605,4.416169,-0.709403,7.751704,7.140129,-3.110794,4.413454,8.782065,-6.018399],[-8.114035,8.885153,-7.566529,5.029698,3.866986,2.218131,2.821538,-8.269957,-7.125684],[-4.804986,7.104870,-4.014388,-2.456456,-2.885890,0.748115,-0.743788,-0.837677,0.970029],[8.444120,7.396183,-1.548716,-1.829830,1.913927,-1.316435,-2.616237,2.066910,-6.140286],[9.744904,0.141827,5.918264,-3.359761,-6.627527,8.589985,8.852144,-3.920424,6.961924],[5.599854,9.746682,-1.772585,-9.973331,-4.683411,-9.731802,0.426397,1.633713,4.498722],[8.518361,-0.087407,-9.457421,-9.817181,6.323710,-1.077604,7.863987,-6.798406,-3.834587],[-4.156422,7.370378,1.313665,-0.466261,0.862386,9.548991,-1.124487,-8.149188,8.901887],[-1.236338,-0.247898,-3.042874,-4.241877,-6.556182,-9.054174,5.771429,0.879195,2.060543],[-3.281453,1.586512,-7.712040,-9.278078,-7.238736,8.785743,0.918065,7.497499,3.241301],[-6.345541,3.056146,9.510207,-9.267770,-9.330537,6.644595,-6.206550,4.708269,-4.182899],[-8.537190,-1.963464,1.592484,-0.940488,2.033426,7.289847,-1.667291,-7.429087,-0.164934],[3.827390,-6.183440,9.008819,-0.367086,2.622377,2.228608,9.790428,-6.446366,-2.371259],[9.637926,-9.619896,-8.142814,-9.258655,-6.989645,-3.330820,-5.925051,9.303260,-3.947934],[-8.234806,-1.651499,-1.643870,8.703221,5.761769,-8.396081,-2.595498,2.194390,-1.578767],[-9.191970,-5.132122,-2.026517,2.059222,-4.262619,8.794548,2.855511,1.778827,-4.249867],[-7.837837,1.864052,5.775688,9.179119,-2.046724,2.012034,6.765620,6.139724,-6.045302],[-3.458127,-5.425500,-6.307353,9.939663,6.964552,5.600314,0.708967,-7.027059,1.194843],[-5.336714,5.360321,1.405747,0.475074,-3.600384,-2.628017,-8.300469,-4.244418,-4.741586],[6.042758,5.967876,-8.696134,-3.400474,-0.223153,4.194629,-1.457449,-3.660271,-6.050143],[-4.606696,-4.092833,-9.764133,5.623717,-0.420791,6.651269,-3.942404,-9.227055,3.815898],[-2.234213,-9.428401,-7.750261,3.561062,6.979358,-2.178018,6.399431,-0.066725,6.137126],[3.239925,5.638130,2.657011,-0.543473,6.822208,5.238040,3.952121,-1.701396,-7.462471],[4.522909,-9.986903,2.243916,-1.216718,1.644967,5.867463,9.352976,-8.810619,-3.285687],[7.988765,8.896821,4.519953,-7.960205,8.815801,1.330080,7.906328,8.233042,7.627759],[3.586771,6.151617,-8.467409,0.851283,3.767193,9.538489,7.248216,-4.449918,8.071636],[7.530045,6.386217,8.535619,-6.252025,2.311726,-2.300719,2.835254,9.830398,-1.661001],[1.299385,5.467779,6.661989,-3.091503,-2.387320,-1.512661,-8.816942,7.672610,-1.584789],[-6.383431,9.551505,-1.568767,0.476511,7.692586,-5.188546,-6.267566,-3.949303,6.329734],[-9.232691,-1.384771,-7.496469,3.774249,6.917460,-4.152760,8.628930,-1.233669,1.483980],[-5.145147,-7.395420,5.115775,5.651133,-2.251917,9.345201,-0.043299,1.717864,-7.081010],[3.062214,4.089076,-7.880618,-4.094128,-4.026139,0.918139,8.736140,-6.330031,1.539932],[-0.644566,-0.711565,-7.659225,-5.423483,1.472396,-7.691335,-6.102136,4.734378,-8.936641],[1.006668,5.154871,9.226777,8.800195,-2.574568,9.799717,6.152785,8.125737,-1.532286],[-6.101518,-4.482813,8.390293,0.992578,-1.180373,0.575031,2.585569,0.671705,-1.827605],[3.487215,6.184883,-5.804075,1.300787,-7.532181,6.141120,5.861427,-2.860160,8.619045],[-1.188126,9.477247,-7.399160,9.527349,1.686386,-7.319922,4.386599,-1.458016,-0.220510],[0.578067,-6.626489,-6.927204,9.457307,5.058946,4.207302,3.141247,-6.158287,-4.541288],[9.632018,-2.835219,-6.557173,-2.667213,-9.319794,-5.787574,8.151664,-2.152488,2.418797],[2.037820,-8.441781,-8.881008,-5.092065,7.419708,-8.141306,7.113874,6.819451,5.833688],[-2.881641,-5.598704,-0.404304,3.192999,-7.598806,2.723171,-7.471052,-6.140102,-4.769934],[-7.916250,-8.356090,4.538293,3.967656,-6.215438,-5.078962,-2.677004,-8.676730,2.895416],[0.562979,-2.012394,-3.483623,-1.185030,2.596486,-0.033235,3.631731,-9.183899,-2.393589],[5.026097,-2.873862,7.984775,6.654483,6.526835,-0.896575,-5.790568,-5.406353,7.964581],[-9.082016,8.153073,1.489474,7.660988,9.675330,-3.021670,7.680181,8.092359,-4.803416],[-8.938926,5.718978,2.177006,-3.308528,1.409261,-6.266747,-7.382663,-0.436007,-0.476736],[4.676944,6.220272,6.449766,-1.147657,1.624936,-2.556268,-0.450284,8.490691,4.949752],[2.025624,-2.595002,-4.531911,-6.853343,2.586841,-3.626130,-0.646065,-1.116363,-3.743767],[8.251143,-2.348614,8.071444,-8.772960,-5.612428,9.239161,-0.787372,2.740627,3.356903],[-4.589268,-5.964217,2.714738,6.956578,-0.423029,1.306086,-0.898113,-5.166317,9.992664],[7.742881,1.778358,7.611304,1.939198,-4.466795,-1.145046,-5.516844,4.626960,-4.218730],[-5.969050,-4.407620,7.550903,9.821064,-6.829480,3.633238,3.134791,-7.765145,-3.348833],[1.915946,3.359706,-6.112169,-4.640350,-1.369129,-1.646209,-4.605375,0.015721,1.470286],[-8.196202,-7.112843,-4.007970,-6.232269,-0.138416,8.505718,-6.495439,9.024468,-1.361276],[8.352588,-1.651888,-8.066405,-0.100568,4.023387,1.558555,4.259552,-5.886326,-5.981121],[5.293225,-4.663118,0.300242,-9.923113,4.618519,-4.885028,2.492902,-1.469326,0.112309],[-4.814302,2.609157,8.709475,2.794616,-4.682545,-8.084307,-9.301700,5.678659,-3.004994],[-8.122771,-5.874076,-3.488954,4.811652,-1.100446,0.909986,-6.359045,7.268613,-4.308905],[-4.473828,7.422712,1.375102,-5.259608,3.191706,-9.336413,-9.867206,-5.221515,-0.958696],[5.299480,4.173620,8.352697,-8.647770,-6.294584,9.993480,-2.719894,-8.175651,-1.715754],[-8.804696,-8.382438,-5.256681,4.460249,7.906521,8.967786,-6.606994,-8.839373,-3.346230],[-6.081576,8.899423,7.015698,5.801597,0.270622,5.768864,7.858243,-5.621970,-6.253911],[0.127813,1.416018,5.174234,-8.630473,-2.773078,5.861343,8.588626,4.142125,7.381947],[3.339809,-3.088119,-7.421553,6.243503,4.230729,4.818178,-2.030692,5.695868,-0.044488],[4.798444,-3.715315,4.184387,-5.441847,-3.029163,0.436522,-7.617577,-7.440761,4.619703],[0.670297,8.256535,-5.583841,-9.884969,5.401098,8.677228,-7.826857,-6.045753,-2.554834],[2.738324,-8.302705,-0.151262,9.577518,5.688670,3.964829,-3.221525,9.368689,-2.312128],[8.630614,-7.253622,-8.773719,-7.030261,-0.159284,-2.292086,-5.402180,-3.477790,4.076391],[-4.627382,8.887845,-6.199189,3.645278,4.968384,-9.577506,-3.277905,-0.380342,-7.197394],[-6.031207,-1.298551,-2.465265,2.113650,-1.498163,2.103538,-3.884330,-3.502062,1.426670],[1.471876,8.399903,3.680420,-2.545248,1.469429,7.562291,5.892860,-6.371542,-3.947315],[-5.193043,7.060924,4.871626,-2.122948,8.652442,-3.038400,-3.452421,5.367185,-6.843008],[4.172058,-8.870573,-5.058015,1.337654,-6.833471,1.346841,-7.241942,-8.123392,-5.661696],[-8.311956,-2.861408,5.228991,0.547199,-8.203171,4.530066,2.190217,5.928498,-6.545727],[5.555019,2.091707,4.944087,1.355184,6.519305,-7.416699,9.243200,-1.719742,-3.541021],[-7.865880,0.583162,-2.823605,-9.142829,-5.953606,2.209281,6.456820,-0.741337,-0.964275],[4.133523,3.040968,-9.897189,-7.713070,-5.064358,9.610150,-0.336156,-8.840233,-2.444207],[-0.734799,4.384158,-2.098063,8.577365,6.961285,-8.433825,-9.265637,9.407222,-8.247868],[4.600574,-4.237706,-2.633467,-2.287535,9.772485,-8.068824,8.995155,-4.453285,7.773600],[3.349718,-5.301073,-5.392961,5.596164,-6.741244,-9.486629,-9.540538,9.574807,-0.838016],[-0.634253,-9.574308,8.393520,7.252057,-9.121944,4.043340,-7.495880,-9.852661,-5.907750],[1.593109,1.243704,-6.914255,6.951499,3.928556,1.070404,-8.614912,-2.697007,-3.310275],[7.356821,-7.059003,7.469827,-2.585381,6.032595,7.562162,7.473617,0.760841,-4.203093],[1.490172,-5.623630,2.925478,-5.302423,2.667377,-9.060454,-6.990383,3.516141,5.665595],[5.355955,-1.822052,5.888366,-7.670033,-2.059175,4.958757,5.798817,-1.135461,-2.223086],[-9.230778,9.548658,7.753160,7.145515,-6.426067,0.621374,5.575610,2.853112,4.667080],[7.922975,9.822578,9.493069,2.314653,0.361488,-1.426878,2.821958,-1.577338,-9.438796],[-4.864815,-0.395497,-4.439488,4.426256,-4.420982,7.954175,1.487487,2.075336,-7.435023],[3.188637,7.535392,-8.428427,-8.155001,-2.481476,-0.958393,5.457102,-5.138462,0.237132],[0.238722,6.371520,5.046169,6.388320,4.092511,-3.601350,8.504602,9.840476,-8.658577],[-2.841777,7.473925,-3.966985,1.014143,7.681174,4.094701,-7.297905,9.450794,-3.827006],[-7.918283,2.273879,-5.516915,0.164221,0.211947,-6.636046,-9.801569,7.004261,-5.016597],[-1.734938,7.453925,3.411733,-2.346261,8.983450,2.807579,2.217386,0.548300,-5.421446],[-0.679405,2.830313,-5.954165,7.549267,-8.595162,7.713977,-4.683171,-4.139919,3.553123],[-6.225426,2.138098,2.674667,0.415450,-4.224599,0.924121,-4.693624,-0.816855,5.344518],[-8.044997,-7.389896,3.398457,5.795378,3.812141,5.247320,6.316058,-8.527536,8.412986],[-6.275774,-5.015488,3.925739,0.100436,5.762388,5.727090,-1.226141,-1.025173,-0.502814],[-3.166691,0.211621,3.111899,-7.566524,6.489746,0.012918,-1.781402,9.171215,-9.547788],[-6.313480,0.719649,-2.842990,6.220645,-2.033759,8.973664,8.082717,-5.639254,3.296507],[-9.717787,-2.543606,-4.516901,-6.106679,1.093337,-7.578262,7.181151,6.962682,-7.532918],[2.762104,8.892934,3.507644,1.552359,-6.756451,-0.476706,0.862929,-6.664313,-2.154615],[-5.709630,8.724119,-0.207095,8.698333,8.945375,-5.526819,-5.388876,7.108532,6.756829],[-8.493595,8.560013,-0.537951,-2.260347,-6.445643,-7.997467,-3.205091,-0.679725,-0.645109],[0.629150,-2.596171,8.148259,-6.860819,-9.438239,9.758388,9.515163,-8.443849,-4.101390],[-6.031084,7.088648,2.647524,2.762009,-0.521903,-9.548647,-9.427148,-9.701140,-6.836301],[-3.161791,-9.820791,-0.543847,-9.790330,3.986940,-6.491703,-6.709007,9.232404,-4.720904],[9.789890,-2.306583,5.838354,-6.746576,-9.410037,-4.502239,-9.115604,5.380989,2.926598],[-6.230120,0.365907,5.856090,-7.464121,-1.968940,1.830734,-2.236870,-8.883097,-6.086399],[6.591157,-5.443693,4.328365,-4.928072,8.306952,-1.457807,1.534962,-4.189690,6.533557],[9.958719,3.492494,0.921250,-0.024034,6.931438,-0.204344,-2.206328,3.138675,6.082641],[1.929159,-3.147463,3.011937,3.989793,-2.165383,-7.396618,1.140809,6.322335,4.419957],[7.613996,-8.030573,5.606599,-4.712096,2.050707,-6.522473,2.271976,-6.143491,-3.575152],[-7.968639,2.274535,1.984046,-2.977454,7.527476,-1.692614,-8.721877,-0.353324,-5.280894],[6.997069,1.028252,-3.718507,8.471839,4.014279,-9.515130,-3.863926,7.107442,7.058287],[3.992815,-9.075449,1.894234,0.351065,-3.954360,-8.495125,6.208025,-2.638632,-8.496850],[-0.341518,-9.324158,-7.805345,6.208971,7.484003,-3.264362,-5.585493,7.743397,-2.829670],[2.036794,-0.675978,7.894831,-1.432820,2.071189,6.040045,-9.356261,1.848931,8.743705],[5.150246,-6.244989,7.676483,1.242587,-0.442617,-5.392957,6.680150,4.507461,-1.144584],[-6.792677,9.514800,3.052587,-0.235181,1.117429,-5.232081,8.972684,1.464362,-6.133988],[-1.073521,-5.292940,-7.315371,7.044432,-2.737777,-6.355263,6.604220,-6.021572,-1.018848],[0.607152,8.885247,-9.994950,7.560769,2.820042,-8.095968,8.332363,5.369389,5.089983],[7.454271,0.051188,3.403923,-7.848505,-1.515724,-9.857681,-5.978497,3.276792,-8.855104],[4.170561,0.270385,-7.609719,-3.038708,-5.183931,-9.337533,-6.887224,-3.722689,7.643047],[2.488059,-5.848010,-0.526509,-5.606745,-1.294965,-8.806920,4.805133,-9.896349,-0.916166],[-1.813473,8.050937,-5.861405,8.866916,3.946453,-5.367080,4.936451,-3.188516,-5.632073],[-6.136785,8.823838,-0.541058,1.647355,3.352303,5.354135,4.392625,-8.940095,-4.907753],[-7.771584,5.903319,-6.145632,-8.188568,8.345875,6.710623,-4.601848,-7.825087,6.870435],[8.512217,8.892868,-5.724998,5.570555,-3.385400,-6.608021,-6.879017,-4.346413,-2.973739],[-6.237125,5.318594,9.135699,2.533489,-1.898447,1.657806,-9.036864,7.967996,0.542146],[-7.082273,6.050324,0.870826,-7.369769,-2.564661,7.709474,6.984355,3.304633,-1.557703],[8.336276,-8.072843,2.428116,6.659677,2.392084,9.411575,9.351218,2.432092,2.698633],[-5.707584,-4.391706,-0.367764,-6.444966,8.195305,-7.652582,-2.380187,1.513379,-7.554788],[7.819365,6.649250,-6.430808,4.780793,-6.519013,-9.836023,4.931575,0.304710,6.492427],[-9.131495,8.371474,0.382137,1.122607,-8.166488,6.395896,3.335974,-8.158761,7.788835],[-0.876554,-8.680521,7.131738,-8.130237,-3.206148,-4.299947,5.390743,8.950658,3.378267],[6.700529,-5.002115,7.062587,-9.708102,-6.859959,2.223738,0.741543,6.288796,1.926951],[-4.850059,2.138241,1.171220,-0.334278,-1.613646,-2.910941,-9.511921,-8.481067,9.779068],[-6.488605,2.676728,-9.578407,-3.397276,-1.102809,-8.507072,-9.254740,8.270104,8.666409],[-6.929487,2.888878,6.038017,-8.119931,6.278052,-2.773757,-2.618607,-4.677702,-7.273403],[0.221062,-9.363373,-6.366442,2.181510,9.816717,-3.340378,5.259921,-7.600944,-0.427977],[-5.729321,-1.185548,4.931368,-3.019173,6.988053,0.795009,-5.890616,6.099010,-8.850281],[6.070953,-8.919594,-2.661757,7.207209,2.989665,8.478293,8.418469,-7.512783,7.267075],[-6.781512,-1.644106,1.294754,7.315195,-2.864665,-7.101537,-8.516981,-6.345694,7.710304],[-3.783465,-2.974714,-7.431598,4.005501,-5.261461,8.914169,4.502556,9.614128,-3.969886],[-6.141165,-4.183492,-8.169507,8.672642,-3.312273,1.414951,2.754843,-0.332559,-6.854087],[2.591355,-1.519646,0.216605,7.604140,-8.238550,-7.969969,0.005276,-1.842396,5.448848],[9.530172,-4.540117,-4.621835,4.894298,3.588163,-5.103793,-0.687365,0.401301,8.022363],[4.271403,4.607389,4.283150,-2.827219,-7.559362,4.254075,7.336891,3.619174,-1.765080],[6.126402,8.558128,-9.262493,-8.864008,7.350835,8.625865,6.856742,3.650788,-8.832893],[-2.096866,-0.861713,-9.683734,8.146659,-9.132171,4.457600,-7.836301,-5.953580,0.832231],[7.900911,1.653147,7.113636,7.830499,3.603450,3.298797,-2.192057,-9.406149,8.411441],[-2.675770,-2.531414,7.086668,9.947022,9.577284,1.833751,-6.789359,-6.586952,1.804133],[1.858982,-1.651652,8.473796,-9.482343,-9.342552,-2.227683,9.033049,-7.340476,0.401944],[9.671885,6.628619,-9.856264,9.734471,-2.866989,7.302868,7.002635,-8.362361,4.883292],[-8.869120,9.772034,9.736858,-1.431211,-7.845880,-1.462846,-8.380192,2.364483,-9.419553],[-9.977629,-3.836107,-0.210256,-2.211599,-3.274826,8.228939,-9.209250,-4.027242,-1.957001],[-8.250796,-4.399612,0.634502,-5.197026,7.448164,-5.598801,-2.177232,5.555181,9.014460],[-5.438632,-6.546330,-0.437069,-3.372193,9.186012,4.395392,-1.270346,-1.295416,-3.284996],[-4.440722,2.436355,-3.877001,8.490983,-3.745595,-0.739134,-0.555100,8.393631,5.724492],[4.857780,-6.964458,-8.649084,-1.403509,1.854053,-6.712752,1.244113,1.026166,-0.736921],[-3.729874,-4.816214,-3.016005,-1.567452,7.355592,0.652662,4.796249,-7.461676,3.276067],[6.783010,-0.487535,-8.671641,3.499045,8.771539,-5.117037,-4.671027,6.081373,5.793115],[0.841087,7.892045,5.018530,-8.001608,9.604065,4.380738,4.231632,-8.129217,5.476793],[-0.736864,-6.976970,4.746329,7.093048,1.441864,-7.073497,1.856033,-6.358734,-6.586562],[5.598972,2.887528,-8.385578,-5.744142,1.897325,6.660139,7.103161,5.787957,9.902035],[3.372087,2.873740,6.487517,1.278435,0.127324,3.302881,-1.648332,-8.335921,6.603752],[-0.890140,4.467739,0.300071,-9.887732,-2.337255,-7.791210,5.637799,2.394046,4.789275],[-4.561931,0.538192,-6.484734,-1.215444,9.493247,-5.427112,6.275340,-6.896207,4.096946],[2.825199,3.209701,4.552556,7.394120,3.017264,8.044079,8.505352,0.800528,-1.125896],[-2.409238,-9.215836,6.791774,-9.554078,2.128013,5.229656,-1.500753,6.779050,5.587899],[-5.725331,8.786435,9.137702,-4.148888,-4.911396,5.676475,4.241875,5.755533,8.657413],[2.130345,5.765730,6.586321,2.128926,6.942271,9.908994,4.050892,9.490538,3.962367],[-8.475132,-5.829579,1.308396,7.286884,9.520811,8.031383,7.201659,-8.480426,0.325967],[-0.505033,-6.196757,7.413254,-6.503147,1.030975,1.009312,-9.516446,-4.317128,7.003356],[-7.695189,-4.669302,0.303404,-7.524434,-7.491418,-1.026805,-5.948820,-3.658604,-4.018723],[-1.748958,4.308891,3.011986,-1.048073,-6.765386,-4.214493,4.537022,-9.884282,-4.739517],[7.878986,-1.050341,0.900873,4.420610,5.465866,-9.271926,-9.529979,-2.354372,-6.988036],[-3.484988,6.761700,3.972411,-2.648225,-8.439307,9.488766,6.275748,-4.868077,-1.818893],[-7.250553,4.811420,-5.104259,2.050236,5.738948,-6.296058,4.407713,-0.575813,5.419472],[-2.495861,-1.504313,-3.638924,3.251708,-4.896744,8.292628,-5.852563,8.518358,-6.442078],[8.141421,-7.544211,5.048094,1.082468,1.466728,-6.468582,7.400398,1.277048,4.826610],[8.807238,1.686551,-4.886612,4.399867,-7.488921,7.368830,-2.514456,-6.834028,6.757533],[6.802867,5.750756,-7.805566,2.330601,-3.495503,-5.694570,-8.697730,1.305816,2.053899],[-4.173256,-0.006122,9.400719,7.625732,-3.892168,-3.958117,-1.401513,-9.851325,6.003496],[6.646332,5.787606,4.912494,3.519506,0.334722,4.520045,3.726698,8.803867,-5.722437],[5.008834,-6.297956,6.392837,9.645270,-9.725588,8.029109,-0.734530,-6.513400,1.694162],[4.302097,3.215191,8.721903,-7.141493,8.090086,-3.153096,-0.952492,0.652243,3.947553],[-2.034632,-7.090392,0.700215,-1.328078,-6.547562,8.354308,-3.871375,3.100495,5.745351],[-7.061563,0.668187,-7.411571,1.516262,7.803933,5.913180,8.609244,9.286916,9.386927],[-0.046684,-2.135003,-6.196086,-4.094227,4.779603,0.402169,-4.293285,-6.508326,4.771486],[1.328620,2.201324,1.520546,1.829209,-4.958865,4.546459,7.042701,1.965207,-7.876114],[6.402681,-5.164956,-6.943082,-5.317657,6.123469,-3.018973,9.356259,0.764587,-0.244775],[9.960061,-2.074408,-6.062704,1.851052,3.542031,-8.246636,4.452110,-5.463126,-9.422907],[9.768581,6.635963,2.043589,6.585820,8.524469,2.993948,8.491021,3.908808,7.123333],[4.283614,-0.361037,0.935823,8.618187,-5.057644,9.218876,-9.298771,5.139487,6.250954],[-1.847030,3.429211,-3.512810,2.933461,-2.404650,6.557957,2.929392,-0.324941,0.603295],[-7.586315,-4.062818,-6.086119,6.538093,-7.918023,-1.117747,2.659424,-1.469704,-7.401711],[0.170882,1.107052,-6.953587,3.743061,7.668759,0.884966,-4.450564,2.994429,9.071079],[-3.337778,4.455923,9.156823,-1.550450,-6.887892,-7.442637,2.583455,-5.544427,8.570024],[5.965468,-8.240857,-1.417138,4.128532,9.221324,-1.095767,-9.328989,5.690043,0.270081],[3.800279,2.950045,3.507482,-4.058984,-5.854072,4.828252,-1.413631,-4.343994,2.319869],[-4.562784,3.333374,-0.961983,-2.063656,-6.841877,-5.314492,9.078103,-0.178603,4.977083],[-1.641926,-7.711582,-0.909755,-5.428055,7.306582,-9.899519,1.768319,0.468349,-9.059506],[-6.804648,4.627454,3.244852,9.148344,4.159843,6.908836,2.857006,0.675156,-8.335244],[4.879956,-3.710328,-7.485497,5.256296,9.287861,-9.916342,-9.804206,6.634773,-6.465853],[7.341842,9.966671,5.833934,9.985239,-1.845319,-4.793366,9.378655,5.574588,-9.693315],[-6.660761,6.239407,9.708943,8.977376,6.008717,2.434966,8.911154,6.726980,0.219595],[-1.030544,2.671945,6.053251,2.497109,0.874135,-9.340868,-2.542221,8.692476,9.371279],[-8.923017,4.429703,2.930905,0.323803,2.017696,2.396559,6.448690,-4.758137,-9.054934],[-1.233667,-0.308488,-7.926702,-9.086398,8.119890,-5.338486,-3.849358,3.509702,-8.451513],[-9.041369,-3.535655,-4.813249,-9.669595,1.038113,-3.534731,0.225525,3.254746,-2.618061],[-7.650193,9.875306,2.003545,-9.701154,-6.985610,4.837787,-9.301664,-4.937825,2.185210],[-5.510541,-6.723123,-7.281048,5.276585,5.259606,9.717609,-4.454706,-4.045051,5.493600],[-4.155195,5.556865,-4.147729,2.290841,-9.396201,3.364010,5.575042,-5.675213,5.874909],[-0.272911,-2.767783,7.951023,-1.522258,9.428142,6.587752,-1.720694,0.724435,-8.580228],[-6.995355,-0.257227,2.368085,-9.327253,-7.873820,-2.531870,-1.771457,-6.312355,0.594695],[-6.139573,-3.396653,-2.981541,1.975615,2.729472,0.450033,-7.929723,2.312900,-0.748486],[-8.495402,8.181863,3.220860,-8.555258,4.509788,-8.263556,-9.848838,-0.260597,2.102257],[5.138635,5.789969,2.892187,-7.380166,-9.800814,-6.379418,4.756391,8.066877,5.248828],[-9.669320,-4.557929,3.307669,-0.527746,-6.166118,-9.533052,-8.928555,-6.015929,-1.032397],[-5.011067,9.341935,-1.208259,0.114556,-0.346406,4.209018,-4.639173,3.918313,6.891654],[6.322311,-8.586976,-0.206565,1.444051,-9.500191,-9.556577,1.964742,-0.416710,9.191168],[8.441591,-1.212475,6.584308,5.437900,7.070411,5.376130,0.738531,1.377441,-3.240307],[-7.168796,-4.798541,4.646670,3.875504,0.931321,3.413430,8.533081,2.973084,-4.611424],[0.008189,-3.414248,-3.806489,4.293480,1.534035,3.173011,-4.060297,8.229170,4.909455],[0.195179,-0.570981,-6.598728,4.986115,-1.590479,2.645601,9.334808,-1.600286,3.807497],[1.312733,1.159483,6.877978,-1.676705,-7.948057,-9.923220,-6.530557,2.099887,-1.114585],[-4.392119,3.244585,3.302843,8.824946,4.332062,-5.250492,-6.237257,8.564158,-5.009019],[0.933869,-8.726072,0.396227,8.954226,-4.590189,-6.968622,-6.124342,-6.432325,6.672867],[-4.116576,-9.242625,-8.130522,-1.563974,0.341917,-6.885675,4.682304,-6.406091,-4.814182],[-4.902990,-2.162331,-2.497777,-3.884356,0.671383,-3.466147,-3.749102,-2.905780,-8.707253],[4.955455,1.278502,-7.280767,2.607139,4.085293,4.841146,9.898755,9.512637,-8.880299],[-2.761599,-2.721084,1.501225,-7.337128,6.763269,-9.733334,5.703970,5.994530,-9.234775],[2.265444,7.827426,-4.613216,-5.306365,-4.837206,1.019634,2.617570,5.603485,5.838290],[-9.881925,-1.186049,-8.243891,2.901450,1.971453,0.047091,-7.634818,8.793250,2.195082],[-2.851644,2.066732,-6.234819,2.036257,-1.633686,8.460395,1.326695,9.234412,-4.347112],[-2.792203,0.137650,-4.070160,-0.855817,7.371479,-2.053415,0.690955,-4.404576,4.457479],[5.641682,-9.817555,-0.657410,3.720268,2.998397,4.649128,0.274066,8.851747,9.473820],[2.774803,-2.928411,3.784236,8.328227,1.119669,1.316345,-7.349831,2.374897,-7.734729],[5.506838,3.276810,-2.937525,-1.544019,1.430370,3.129866,4.383908,-9.609502,8.357834],[-6.622400,-5.708324,4.375461,-6.883079,-7.820757,-5.892463,9.462171,-4.710277,9.302962],[-5.701885,-6.367953,2.314745,-4.953758,-7.990105,0.569270,3.385771,1.213963,7.487091],[2.770894,-0.375755,-6.987981,9.973926,-8.186191,-1.503553,-0.662732,0.306763,-5.074239],[-4.275610,6.438360,0.362161,9.092119,-7.271546,-1.765649,4.023417,-5.314033,9.571792],[-8.961605,-0.248544,5.792752,-2.257226,3.895548,-0.365383,8.736313,3.073285,-5.388140],[6.848127,7.209989,-5.369311,7.666691,2.564747,7.074970,-1.970013,5.392851,0.541379],[-8.221571,0.795509,7.859813,5.865106,-9.482222,-5.886705,-8.210657,-3.709731,4.246741],[4.549979,-1.675251,-5.385904,-7.344415,-7.196343,-8.809868,-7.274265,4.609256,-1.470871],[7.175083,4.610033,-9.908421,-2.008717,9.264780,-0.569028,3.191571,-8.541851,6.488273],[-0.959475,1.257809,0.416561,-4.317745,-0.696988,9.931637,-7.240680,7.937889,5.759883],[8.531293,-8.970537,-1.274886,-3.152456,-1.124982,-6.464064,7.787158,4.573131,1.427469],[-5.464744,-1.820448,6.314231,-3.283815,9.687965,-5.070280,4.955709,-0.617823,-1.931735],[2.639203,2.360861,1.328761,1.702685,-4.625372,-8.008031,7.812597,5.490198,9.314856],[-9.433348,-1.080646,9.212024,-5.644092,0.887717,-1.023486,5.879225,-4.282444,-1.597149],[-2.201835,-1.706249,-6.555735,-6.750658,-1.005016,-9.737854,8.892488,2.606202,-6.207639],[-8.032214,8.653589,1.652391,1.802783,4.991015,0.161022,-9.418935,8.450703,-3.651887],[5.312678,-9.053386,-1.640310,5.750021,0.344661,-2.920979,-7.527857,-4.726139,-6.542672],[4.116806,-1.470669,5.179770,-6.139695,-9.655238,-2.951143,-8.461834,4.674242,0.525048],[6.433363,9.106515,5.524206,-8.675366,-9.728843,-5.444204,-5.848230,7.742688,-6.498728],[4.687996,-5.051352,9.727620,-0.928906,-9.727569,-0.713255,-5.053841,-1.778565,-4.291590],[1.589683,2.162162,2.367868,-9.343375,-1.223228,-4.789249,-3.968914,4.061332,7.668906],[4.844357,-2.168314,-6.534384,-1.287267,-5.790402,-3.197128,-5.851205,6.038953,-7.776781],[3.962212,9.311915,-6.178177,8.226966,7.059046,1.782518,6.090127,-1.447291,-2.706222],[-4.137199,1.497439,1.979147,8.936773,0.276337,-2.122227,0.910770,-5.086871,8.245681],[-0.751374,1.119776,1.578169,0.387891,-4.492302,4.320278,-4.421641,3.038591,-9.699082],[6.971130,-1.911681,2.441916,-5.781439,1.631520,4.851661,2.654721,2.330385,2.417619],[2.381612,1.911799,-3.900178,-6.651315,-1.433007,8.249034,7.243202,-6.840150,8.142745],[-7.604999,-1.462358,2.117870,-5.422729,7.142061,5.221550,-0.116549,7.609201,-3.167225],[-8.066646,-3.640716,-3.389400,-1.084946,8.475023,-0.816631,-9.192869,-1.555004,-2.610882],[-7.275413,0.629005,-7.814410,-1.076986,8.261030,-3.050371,2.340646,1.231631,4.799172],[7.400179,8.378514,-2.711468,-3.546149,-8.508382,4.153818,-5.015538,3.293421,6.602456],[-9.089266,-7.620409,-1.866677,-0.464293,-6.964993,1.636435,8.882815,2.939240,8.731890],[-5.840792,-6.432291,4.526959,4.057835,7.045405,7.243821,-0.300933,-6.228218,3.682456],[9.764290,-7.318732,6.223789,9.939484,6.786560,2.397819,-6.505869,-9.593323,-7.626062],[-8.580875,7.556068,-1.438704,3.115157,-7.482658,-6.205903,-2.837638,4.087773,8.349035],[-3.026466,-5.388702,9.795621,0.830643,3.836728,-4.090631,0.882414,-9.052130,-6.688129],[3.844394,4.851015,9.687910,0.835498,-3.728020,-5.394553,-4.864910,-9.414067,-9.222071],[-1.713914,-5.442081,4.324326,-6.915208,5.359741,7.169442,6.537147,8.018425,1.586939],[-4.001054,-0.682522,3.694696,-7.175043,-9.174710,-0.232121,-2.989363,-4.710982,1.647357],[1.049758,-7.547591,-3.732880,-5.631886,-8.842983,-3.657039,-4.018766,-3.151541,1.139788],[-9.707044,9.429616,0.327514,4.470299,2.879338,-1.083000,-4.661308,-1.599986,-2.118798],[-1.820348,-9.589478,1.427323,-0.125238,-6.198172,-0.228481,7.278729,5.043501,8.356629],[-2.796880,9.300511,-9.366023,-6.446589,7.234442,7.848643,3.515957,6.078751,-1.708003],[1.096038,-7.047261,-5.376552,5.966683,7.287974,-6.956128,1.206858,-1.508626,-4.853335],[-4.102999,1.939805,7.062146,-9.497193,-3.896521,1.436057,-4.749608,-7.290221,-9.414326],[4.965864,-7.892554,-5.342358,-1.834669,2.341683,-0.295682,2.273278,2.891993,1.825310],[-9.365671,4.556726,3.075263,0.637377,1.272929,-6.981873,-9.995361,-5.824089,3.642161],[-9.327054,-4.371351,-9.058837,6.584300,-7.786271,-7.873284,-8.610224,4.445254,3.148524],[-1.033441,-7.738195,-3.294713,7.729976,-5.813870,0.658265,-6.318116,7.555881,-0.095776],[-0.415809,-6.861215,-3.985809,-5.671394,1.469062,-4.816234,-6.080175,0.166692,9.755737],[6.332849,5.733811,-6.059987,8.964439,-0.514131,5.493181,-3.798136,-1.002277,-4.732193],[7.196540,1.321338,-4.681360,-5.066954,-4.264109,1.376645,2.143766,-4.260327,9.549012],[-4.699735,-0.745625,0.625311,2.770047,4.623055,-9.575076,-1.416732,-5.586318,-7.319356],[8.596523,1.365718,9.813195,7.827163,0.451228,8.831116,-8.869238,-6.345039,-2.035576],[2.433653,9.652077,9.863312,-1.660445,-3.599641,-7.405909,-5.837094,8.625621,2.333107],[-4.657075,0.802810,6.443049,-2.855382,-8.352099,-4.832201,9.431603,-8.045551,-3.202271],[-5.349937,9.807178,9.496221,-4.465721,-8.650653,0.304130,-5.715878,-6.658125,0.730891],[-3.596623,-5.584553,-1.854569,2.736073,-3.592340,7.531651,1.071900,0.056400,-4.699811],[-7.842772,-6.617297,-3.376944,6.197844,-7.570461,-3.375649,8.065544,1.275325,-8.798596],[-9.387239,3.885405,0.043917,3.443283,3.968209,-0.503013,1.412892,-9.222428,1.545608],[1.696018,8.237750,-2.059310,4.327759,-9.170497,2.469381,4.348842,-0.258663,-4.035550],[0.731847,-7.345385,4.442242,-3.080115,-8.560971,-9.306137,4.237709,-4.223464,4.083342],[-2.921962,-1.582667,-3.983129,1.600694,1.377327,-9.846800,-2.642971,4.562774,-6.077480],[7.529273,9.206242,5.557928,2.317573,5.813486,7.435354,-4.765697,7.220502,-9.728420],[3.599557,8.367715,0.987560,-7.711135,6.342497,5.382527,-0.329037,-8.260103,-4.133224],[-1.132532,-7.434578,7.234873,-0.191073,-5.721384,-6.710950,6.775771,-6.458873,-5.240715],[5.753540,9.559339,-2.843146,-1.472229,4.745357,-4.345731,2.306993,6.096898,-8.815017],[2.863619,3.925028,-3.617893,5.319545,7.068399,8.539976,7.661603,-7.838148,6.051912],[8.570898,-4.932121,1.691830,-3.859570,5.385005,-5.555818,-8.367359,-6.941831,5.367607],[8.295487,7.396150,0.737003,-4.853068,8.441270,0.655141,9.055200,-3.013141,-1.675593],[-8.351636,-5.035304,-2.749064,1.385019,5.473061,-4.706806,7.047149,6.092773,-9.521632],[6.371491,4.845449,-0.676114,3.355308,-0.190039,1.491103,5.288311,5.956898,2.445406],[2.163181,0.530510,-4.391776,5.718449,0.577135,-0.568818,8.746217,0.467005,-7.593841],[-7.881193,6.320069,-0.207626,4.919600,2.455074,7.309257,-8.083187,7.010034,9.406695],[-1.863291,5.023113,4.292667,8.421941,0.425709,-1.063332,-3.037560,-2.829216,3.608366],[-7.125131,-7.092967,5.583575,-1.080467,-4.033338,0.895914,-3.379561,7.841738,-0.295516],[9.430183,6.784798,-5.094066,2.611479,-3.330042,-4.200594,-6.288432,-9.173394,-9.399902],[-9.940162,-5.133807,8.621346,2.744999,6.585737,1.921244,5.780064,1.776947,-0.458979],[-9.215243,3.591888,0.976312,-0.312326,-4.128892,-4.818613,0.448375,-6.474747,-2.575015],[5.288658,8.576259,-7.530234,-9.394256,0.418006,-1.720564,3.786601,1.583730,-2.498102],[9.528110,-4.868939,8.429604,-8.148995,-7.047172,-6.120705,-1.558388,-2.619926,-1.368968],[1.246712,-6.399403,5.364849,-4.238569,-4.348117,6.510411,-8.976138,1.118708,-3.690989],[6.478456,6.162707,4.084008,-7.043098,-5.812746,6.071331,7.399896,3.049580,-2.975712],[1.756513,-9.747028,-9.912858,-1.237166,-0.894082,-1.553021,-1.688064,7.441128,7.081743],[-1.902725,8.073087,-9.462230,2.635166,9.081240,0.321635,4.837742,-8.650506,-5.058955],[9.804280,5.592805,4.640408,1.736541,6.226418,6.200744,1.384497,2.484633,-4.698310],[-5.606521,6.986775,7.842214,4.459571,5.922697,-1.268628,-4.309268,-8.776734,8.637776],[3.507998,-6.129591,4.436813,7.630721,1.172832,7.758175,-8.274392,5.626142,3.672813],[4.094983,-7.440873,-9.045360,-9.869589,-0.212427,-4.069674,-9.989459,-3.682814,2.458615],[6.757046,6.417896,2.576624,-3.362905,-3.197659,2.416719,-0.182998,-2.277795,-1.464112],[4.911591,0.144096,1.014662,8.774891,-1.972972,-3.831210,-6.210443,-4.146455,-4.136691],[-6.588346,-1.072036,7.543879,5.867097,-5.669261,-2.039949,-2.822706,3.307784,3.671034],[-6.952874,9.849871,4.202819,-6.521876,9.170720,3.615454,-4.717532,-0.075673,-9.298434],[-6.719669,-9.768503,5.307749,6.343321,-5.503069,1.087039,-0.183718,5.948658,-6.782888],[6.546099,-3.223966,-1.065508,3.437914,4.295492,3.306631,2.578815,4.028519,-1.239754],[-3.426852,9.056513,-6.869669,-7.210721,-4.620294,-9.762263,-0.786250,2.229577,-4.942489],[-6.627770,-6.867933,-7.215511,3.907169,4.172654,8.449886,0.140763,-8.332162,-9.324960],[-7.587314,9.343434,-8.103708,9.934610,3.689795,7.970752,-2.035109,7.295030,-4.792853],[-6.562387,3.540741,-3.000047,8.838444,-2.264422,-2.772594,1.418496,-1.862380,1.451623],[-6.455956,6.204723,3.612426,-0.898663,3.520838,-8.723486,2.179965,8.924985,2.716220],[2.833609,-2.436866,-5.714293,-0.919087,9.516771,-4.814895,-1.172081,6.978662,-2.727209],[-0.197674,0.104946,2.541489,7.973062,-2.071936,2.133594,2.728906,5.488859,2.751502],[-5.837775,1.233294,-5.926320,6.171630,-2.215280,-5.502374,8.060409,6.366088,-9.656006],[9.522924,8.359587,8.995865,7.539402,1.278662,-1.703359,-5.510299,4.671731,-6.391763],[8.486651,-6.100681,-7.312499,-7.813905,5.509241,-3.080864,-2.401645,-1.986285,-8.476139],[1.381415,-5.571334,-6.030887,9.086851,2.161375,-8.696645,-8.355403,5.021469,2.270390],[5.512639,-1.516064,-4.312440,2.451721,-3.387032,-3.144071,8.616796,-0.056611,7.191568],[-9.702281,6.336629,6.788692,3.614397,6.442298,-2.237308,-3.480090,-4.780518,-4.269544],[-1.139220,-9.833611,3.095368,3.589482,-4.903291,-5.477120,-1.839929,-9.469073,1.523335],[6.196578,8.264376,6.207637,3.735532,2.528927,-9.676419,-9.235510,5.739597,0.606100],[-2.155617,3.819757,-5.450861,-5.412174,-9.888815,-7.740259,-6.885048,-6.462748,-9.130574],[5.898477,-1.719306,-3.173718,-0.619451,4.402728,5.812739,4.804168,9.656205,-3.149782],[-8.815478,-7.573595,6.727031,-9.468264,-7.402375,4.715737,2.318768,-4.188696,5.253597],[-9.993076,-0.385796,-5.072609,6.842377,4.884848,-0.751237,-9.566621,-9.914179,-4.101368],[-6.022163,3.526734,7.992908,9.504920,5.117890,-3.130067,-5.258164,-4.248415,-2.587579],[-9.776163,-1.916965,-8.062961,2.266056,-1.116702,6.679051,0.282253,3.509471,-5.198939],[3.391980,4.279517,-8.009476,-1.441751,0.406376,9.733265,4.873580,9.484027,0.833958],[-4.683931,-8.598109,-2.888076,5.282242,9.931052,-9.208221,-3.594664,-3.426669,-6.167896],[9.632336,7.208619,4.777360,6.689001,0.741417,1.968120,-4.045874,2.182850,-1.165641],[9.958422,-4.174301,-2.839072,-4.314031,-8.851794,5.199803,7.280196,6.981595,1.963652],[5.850994,0.581004,0.478602,0.646253,9.878668,-9.304302,-1.858799,6.565765,0.024592],[9.607144,-5.299233,-9.467883,-6.504403,6.019386,-8.528358,8.408901,0.687212,-5.957152],[2.031058,-3.383052,2.514004,-9.905306,-8.540054,-9.663988,6.843920,-6.432204,6.724964],[3.110958,-3.802223,-1.382020,5.505987,9.429839,-2.980628,2.990184,0.516878,-6.506494],[0.157751,5.992976,3.216561,2.766557,6.938597,-2.619597,-6.644609,6.117987,-6.188153],[6.128693,6.863455,-2.045323,0.292562,1.418778,-6.508456,9.281754,-9.563472,4.086269],[-7.866916,-3.859423,-6.097020,-8.694701,1.308856,-8.161515,3.847633,0.688549,-8.436867],[2.617403,-5.936484,-2.681975,-8.895764,-5.763307,-1.891035,-1.391154,-6.324225,4.218116],[-2.879015,0.170330,0.739043,8.794589,8.187320,5.915271,3.346867,2.769433,9.819114],[-4.822238,1.451873,-3.284786,-2.280720,-2.679887,9.590170,-3.883976,-2.765658,6.217022],[5.264961,-6.058321,-0.440055,-7.709770,-1.718211,6.593580,8.152148,-3.907650,-1.275988],[7.250630,5.133949,6.342578,2.847798,-1.920197,3.014547,4.712338,9.137526,7.514781],[1.163477,0.013323,-3.609247,1.257393,-3.861130,-0.691130,-2.559985,5.044851,-0.911748],[-9.313600,-3.564793,4.752705,9.728404,-3.125341,-2.518962,-5.256751,1.423595,-6.247008],[-3.436713,-1.133746,4.796472,2.256602,-8.506356,3.568978,6.714273,-5.616556,5.319126],[8.227234,-9.926753,4.872971,0.926097,-6.614589,6.937142,-9.152711,-1.658740,-3.542106],[-8.361974,3.795136,-4.615216,8.597948,-2.444888,-6.041302,8.598135,-6.750019,3.453076],[-8.764465,2.954932,-3.662128,9.944270,-5.636614,4.262057,1.576643,-9.346594,-6.751889],[-4.427146,-6.823896,1.103250,-7.529013,-4.626487,-1.433455,-7.802149,6.331253,2.546510],[-1.199473,-5.663119,-6.798943,1.342797,7.071000,-6.694382,-4.732309,8.712163,4.060251],[4.604388,4.269327,6.072770,-1.012862,9.929965,5.786096,6.810391,0.045582,1.862903],[5.889016,-3.239304,-0.589958,-3.293105,0.095631,-9.136193,-2.547415,-0.224618,2.448088],[4.503891,3.100110,9.344878,3.902620,-2.936727,3.432531,-3.583703,-9.246038,4.638191],[9.331210,4.406552,-3.059094,5.500400,-9.802967,-1.427884,3.420403,4.434933,-4.499500],[-9.434465,3.072301,4.923565,-4.968609,5.349327,-6.073738,9.145876,-4.385654,-9.340292],[-7.657307,7.635618,8.068324,0.262463,4.480654,0.425023,4.556183,9.241430,-9.316078],[1.560500,-6.649564,5.256700,-7.997593,-5.203477,2.645859,7.804662,-6.427770,-8.545388],[-3.208396,9.520503,-5.507728,-7.799976,-7.576978,-0.824330,-1.354483,7.507347,-3.123752],[0.054550,1.685887,7.266839,-7.252394,7.262994,3.351167,-9.047806,2.622748,6.283895],[-2.186330,4.278384,4.279078,4.201807,-3.802748,-7.634979,0.935477,4.972307,3.514192],[7.206078,3.742406,2.711287,0.637887,-9.339947,0.708235,-1.792323,4.192599,-3.024510],[-6.266938,-7.569548,-4.120197,3.202685,-8.788662,-9.713884,-3.667780,2.955828,-6.617573],[-7.501232,-9.117161,-4.500291,3.610651,4.326872,0.773745,4.736356,0.556851,-4.315970],[2.210673,5.536574,-6.737395,3.031600,-8.148073,-3.322023,9.617167,-0.311797,0.938626],[7.269840,2.132524,-6.681450,-2.544925,-8.745849,6.016692,0.985141,1.333700,6.346950],[8.612022,-9.590633,3.503330,-0.773482,2.720163,3.242052,-5.640078,6.623062,5.014966],[-5.947968,-3.117292,-1.326036,7.156050,-6.647194,-8.643949,-5.958524,-9.596884,0.470993],[7.394096,8.522252,-3.308417,1.934760,5.801347,0.110346,-0.913892,8.851490,-5.624763],[3.996450,1.011873,-2.654084,3.864140,9.085201,2.547239,2.129876,8.836431,-0.980961],[3.483789,-5.396686,-0.982327,-0.414279,8.139077,5.990713,1.341453,4.101617,-2.268712],[-2.970072,-5.054409,-7.874137,1.547523,-4.366306,-1.178408,-2.876492,-9.995601,-0.497391],[-7.778117,-4.687572,-2.607292,-8.348579,-6.300276,5.357768,8.568872,-9.546138,4.716908],[-1.231803,-3.976429,2.675953,9.303957,1.431275,-6.780662,-2.064914,-2.327465,-8.029630],[5.831234,-0.690735,-3.881246,-5.872646,6.035632,5.788760,2.021812,6.344026,-3.136929],[-6.717145,3.400269,-2.156173,-5.384510,-2.266347,8.305067,9.010375,7.340300,-1.140280],[2.209188,-9.190034,0.341142,-8.315712,1.393886,-1.924514,-1.353193,5.636749,-5.057257],[-4.846781,-6.429000,9.093530,6.188366,-7.981119,-3.123731,5.203497,-7.047426,3.608293],[3.510144,-5.126365,0.034727,7.022015,-3.267146,3.914795,-8.090882,3.821207,7.140563],[-3.185861,9.108659,1.353264,3.181589,-4.118962,-0.586947,2.716318,0.815307,-8.302025],[-6.277892,-0.198839,-4.962188,-1.637574,6.869449,-7.840929,-4.481639,-2.434497,5.936389],[-4.803326,-8.607183,-7.690404,-5.346927,-3.307561,-3.324388,-1.429375,-8.817098,8.516910],[2.042989,2.628430,6.869893,2.291804,-7.530015,2.456795,8.655235,-2.210251,-0.502101],[4.528045,-5.120923,-2.370714,-7.426680,-0.286082,-2.590132,-7.682023,0.371310,-6.834410],[3.410094,-2.219917,0.555838,9.585503,9.113002,-8.437830,8.020882,-0.298835,-3.008187],[-4.148205,-0.417366,0.098990,-9.855868,-8.870751,-4.752382,-7.783680,-0.745205,1.839770],[-0.308572,-1.503913,5.015656,-2.418760,-5.525549,-0.922811,1.545085,-5.221915,0.498910],[-4.571453,5.717471,8.022066,-6.010801,7.384175,4.293536,-6.883195,0.648335,3.802454],[-0.732825,4.161776,7.692301,6.491962,-8.943356,-9.304471,7.885016,6.126823,0.694706],[-4.353716,-7.838229,-5.639552,7.093353,-7.078805,4.058219,4.346329,7.470752,7.586334],[-0.974869,9.221507,-4.121839,3.429784,6.615047,-9.303091,7.454701,-3.867885,-0.379823],[5.301130,6.938440,-1.967625,-0.046590,-6.078814,0.778888,-8.230764,-2.804264,-0.418517],[7.001361,9.964956,5.447730,0.955692,-1.408204,-4.671519,-2.858677,-0.531749,7.864785],[-6.989731,-9.536189,7.227781,-8.057575,-0.823328,-1.402532,5.126279,-5.155870,-2.453761],[-7.560573,-0.511555,0.069925,8.495670,5.916755,8.554112,2.823787,-1.950096,9.315165],[8.400786,2.007651,-8.824480,-6.747271,5.288689,-3.631125,-4.621176,6.165015,-4.721214],[-8.517708,-2.578749,5.240575,-7.741000,5.424922,9.612008,7.664887,0.865989,-8.524960],[-1.655833,2.496058,6.852142,1.720738,2.189683,-3.753041,3.745030,8.234751,-3.433279],[9.815590,3.369333,1.550924,4.636365,6.004802,1.699195,9.165698,4.201140,7.343351],[-6.625878,-9.347590,2.198341,8.722724,6.969082,-4.696747,-3.031846,6.522969,4.291922],[-9.900180,7.428598,6.526040,0.428540,-3.425897,0.714407,9.727858,-2.491429,6.360721],[-7.413596,-9.766107,-5.354009,-5.586286,-8.331379,-3.903805,-9.139872,1.005989,1.269450],[7.394225,4.311890,6.809278,8.704175,-0.387400,-5.538869,-5.178117,5.509659,7.273647],[8.516302,-5.007138,9.233408,1.264647,4.043486,0.459681,7.102817,1.983005,-8.789287],[-1.917269,3.774561,3.901324,-9.384310,-0.614456,-9.393474,9.763945,4.027482,3.641169],[3.622070,6.833415,8.591086,9.201534,4.648378,1.730821,3.264954,1.678039,9.890762],[-1.590433,-4.407693,7.748603,-0.612319,9.262005,-0.525372,-1.117410,8.798944,-7.668368],[-1.137746,-9.443364,-2.086011,5.839481,1.729780,-4.460790,1.769690,-0.327765,5.666178],[-1.096937,3.793705,-0.078307,5.044311,2.935994,-2.254100,1.568206,3.450076,-1.652754],[-8.287724,6.679964,-9.158049,-5.430168,-7.153951,-0.718599,-4.049979,-9.518479,-9.185488],[9.218415,6.221917,-7.854683,-7.861989,6.898824,4.692515,7.806512,2.768843,0.867951],[-4.233421,-6.951960,9.302746,-8.547093,0.827319,3.157070,7.091034,2.799287,7.167868],[-6.142459,-5.164898,8.300409,8.090597,3.759655,1.939840,9.938142,-6.458845,-1.850688],[-2.635656,4.657995,7.987541,1.269624,0.780591,-4.384664,-3.718411,-8.096082,-3.243445],[2.918073,-6.532017,-2.139602,0.781874,4.238133,4.949266,0.523047,-6.017711,-5.119595],[2.860884,0.515335,-5.990683,1.850168,-6.640749,1.731503,8.638634,1.671409,5.170485],[2.332459,4.937770,-5.768076,8.322909,-5.819524,-6.535043,7.554737,-0.420873,-9.559438],[-0.189835,6.702497,0.381699,7.465197,8.054106,-5.372695,3.743054,-9.683282,-0.600933],[3.556152,-8.464781,-3.279259,-4.596231,5.464930,-8.421188,-9.712382,8.169301,2.754338],[-3.152798,-0.719646,1.133934,8.826604,-7.079327,9.513856,-3.307909,-1.875778,-6.319581],[-6.744011,8.254371,9.821334,6.013424,-2.726719,-6.425631,-1.764492,6.905069,-1.548451],[7.356570,0.762585,3.029290,5.858320,2.494009,9.944871,-8.922146,1.535432,9.325821],[7.154781,-6.982941,3.560214,1.683311,9.594568,-2.446161,-1.748443,6.052850,-6.445593],[-3.021653,2.587672,8.031729,-0.700989,-2.650059,5.842567,-5.018341,-1.964845,2.728953],[3.090680,5.912860,8.631742,5.257398,-8.670738,1.707777,1.331822,-8.053899,5.255422],[4.233963,1.889950,9.673633,2.399663,8.494020,-1.195248,-7.165319,8.567072,6.245380],[4.776077,-1.073107,4.260182,-4.813667,-4.251707,6.042967,7.450748,2.620272,-7.011710],[6.948363,-4.561920,-2.313323,2.817137,6.910222,-2.835638,5.901627,3.447260,5.637528],[4.652123,0.732120,-6.587160,-9.597780,-8.275396,-5.956748,-7.002274,-3.647807,-5.716094],[-3.242193,5.451722,6.985627,-8.550750,-9.231610,-9.179996,-3.343913,4.839879,1.147744],[2.388003,0.323596,3.865485,-8.191369,-0.428010,2.628957,2.151954,-4.265939,6.152725],[7.224573,1.197975,8.301692,6.839013,6.764827,1.821866,1.499996,-5.616368,-9.884077],[-4.937751,-6.404227,-0.849721,-8.964929,7.581503,-0.912860,-4.422032,-0.046643,8.783449],[6.806183,5.975660,-8.778109,-3.129254,1.337301,-0.869503,-3.832196,5.265282,5.619533],[-2.090230,9.463040,5.583063,-1.463204,2.493270,1.116161,-7.969446,-9.013554,2.859247],[2.412137,-3.732476,7.779681,-9.393013,8.690391,-7.889492,1.525830,-7.186764,-0.909040],[8.515759,8.343044,1.646209,6.361966,-8.951477,8.638294,-8.700230,5.998398,-3.408642],[-0.990079,-2.082888,-6.355413,-1.985236,-7.418588,-0.548510,-7.598612,8.186534,5.275386],[-1.972447,0.831117,-5.384395,2.113187,3.667651,3.957907,0.938864,-3.499630,1.393387],[-3.985925,7.397134,1.735908,2.094315,1.914698,3.929141,5.281285,7.623074,-1.393367],[6.538592,6.168012,-0.107680,-6.014962,-1.957392,-8.408257,3.350357,7.332483,6.814746],[6.517209,8.780451,0.241694,8.090221,-5.543957,6.842390,-6.419428,-7.580895,1.590800],[-1.914723,-9.662197,1.101260,-0.209870,1.434301,1.926811,-5.629829,2.951912,5.467794],[5.287536,9.734617,0.474223,-6.578443,-9.965399,4.558383,-2.192096,5.699147,-2.442357],[2.055089,-8.890725,9.297025,1.881540,-5.565120,6.181698,0.185019,-8.643706,-4.524488],[-0.598624,4.732311,-6.469606,-5.131450,-5.456538,9.007708,-3.804309,8.272123,-8.847347],[-9.615919,9.184079,-8.457289,-1.483975,6.018516,8.447927,7.765012,-8.652967,-2.822775],[4.563133,1.319112,-9.799740,8.721627,4.212564,7.917844,0.241758,8.226769,-0.340050],[3.910868,-9.683049,6.737575,-5.572332,4.250384,3.606793,5.038054,-5.376743,-4.576945],[-5.351349,-0.991307,2.670409,6.338081,5.347859,9.325702,-8.347759,1.774666,4.153347],[-2.846037,4.477079,-0.371945,7.631636,9.145158,5.738801,4.199034,8.054762,3.817533],[0.803632,1.971254,-1.474787,0.600820,3.965020,5.587005,0.182865,3.586590,9.043679],[-9.705031,3.825096,-6.988211,7.764328,-4.905957,6.347978,5.087386,-8.905141,-9.461777],[1.465517,-5.362263,-7.752556,9.513554,5.864386,-2.498567,3.694275,-8.041353,-0.683557],[9.869296,-9.317897,4.943096,3.479643,-1.963743,7.019009,-2.808080,-4.049567,-2.699797],[-8.849812,1.187859,-3.603264,-5.673233,-6.720665,-8.473236,-8.119184,-0.031503,-5.317306],[-2.580473,4.413850,3.451359,2.207395,6.359098,-9.627319,-4.883244,-9.854003,2.899536],[1.789099,-0.752073,-3.283427,1.510413,-7.921203,7.225728,5.306450,-5.087653,-0.811096],[5.161399,-6.475408,-2.258168,-7.159917,4.104003,-3.739780,9.874018,4.987352,5.352306],[4.052467,-5.349873,-0.238018,-2.777838,1.661377,-3.619608,-3.043685,-4.267187,1.040312],[-8.497778,3.979849,-8.891036,-5.592324,-7.428947,2.084632,7.229500,-0.836295,-6.370866],[2.089350,-4.745230,7.714786,-0.580608,-5.521990,-3.312171,9.320839,-5.452640,6.465966],[-0.665869,-0.997113,4.582342,-3.595390,-1.173287,-3.116951,-6.783265,0.072115,-8.788227],[4.049629,7.314008,2.136816,1.322050,-8.195472,-3.650989,-6.805184,8.658422,9.017093],[-0.180034,3.520772,-1.359909,8.231527,0.694896,1.002659,-8.002787,-4.533846,-1.387809],[5.427824,7.524660,9.482189,4.062726,-4.017541,6.820121,3.211633,-6.355282,-4.900726],[-5.587776,3.771171,8.090431,-9.713217,6.150777,7.369578,-3.751308,-4.781814,-2.401087],[8.299888,0.558395,-5.975419,1.003341,0.603077,-8.913671,-0.760693,6.979238,-0.840908],[-8.931800,-6.314767,7.996363,-9.131209,2.457911,3.255455,-9.996768,0.807913,3.382416],[-4.106287,-0.831475,-3.120301,-0.850229,8.283865,-8.196197,-5.352321,-0.464176,-9.523009],[-5.605317,-9.830952,9.753447,2.221214,-3.234067,-1.390483,-3.343390,3.583464,-8.616015],[3.676847,-7.301133,-4.758661,-0.788946,-3.556113,-5.804253,-0.249114,0.072583,-8.758045],[1.409052,-1.539556,-7.776517,9.345708,-0.590178,0.003882,-3.059842,5.408037,-1.989311],[0.701310,-2.317985,5.971783,-9.320366,7.504553,-1.514421,2.286514,8.522806,-8.753648],[-4.970518,-3.721068,-1.223658,2.304460,-5.033286,6.586756,-3.060581,3.639613,-3.612526],[3.002145,-9.879555,-9.528385,-4.289087,-1.181834,-3.154359,-1.637331,-2.217014,6.568530],[-7.183578,5.265985,4.744474,9.434158,6.868251,-2.678158,-7.290227,1.135078,-2.720030],[1.088792,0.446805,-0.008966,-0.371238,-0.407210,1.745521,6.109886,-1.328875,-9.986269],[-0.727776,5.908714,-2.132177,0.488546,-2.677705,0.833263,2.726027,7.696958,9.937721],[-1.846778,-7.276152,-1.902967,-6.683771,-9.635512,6.051032,-8.702560,-4.097263,4.803665],[2.900142,2.601039,2.112533,-1.931954,-0.473107,1.524729,5.039467,5.191575,-3.116058],[9.991306,-6.341887,3.981765,-0.139991,5.002809,-6.879324,4.451351,9.196800,8.607144],[1.983856,0.222496,9.918375,1.691049,-5.592705,7.753281,6.558869,4.206658,-1.398529],[0.578467,-8.799260,6.712171,6.310570,-9.292485,-7.352508,-4.072851,8.201955,5.491836],[-5.651579,3.466705,3.423237,-7.787724,4.490778,-1.345224,-0.891621,-4.166236,-6.967439],[8.429946,-9.772104,3.029857,1.904131,8.509429,8.422836,-4.883797,9.555216,5.838919],[-3.529483,0.064685,9.376990,2.630991,4.854713,4.491596,9.062089,-4.884049,-1.338803],[-6.035728,4.906802,8.290699,-8.169990,-2.926045,5.156412,7.022295,0.350798,-2.928236],[-7.949539,2.987793,7.264352,-7.361496,1.389253,5.854129,-9.131637,-9.193374,9.781861],[-8.625388,5.915922,7.098688,-3.386198,-2.187371,-1.949124,8.136234,-4.891326,-5.421642],[2.489991,-0.533030,2.563256,-6.653053,-5.851956,5.463938,-6.839978,0.968397,5.945029],[9.814431,7.933047,3.236250,-6.781023,6.971558,8.933991,-1.553684,-3.672160,-9.243841],[-8.438904,5.380067,3.810469,-1.615775,-9.855443,1.512922,0.375057,-7.434527,-9.926679],[-7.915835,-2.795028,1.356763,5.774127,-9.722332,-7.983796,-6.555138,5.401733,4.724365],[-4.589910,2.573570,-5.648549,-8.506506,4.255651,-0.107776,9.536807,-7.875538,-1.271487],[8.323632,0.470909,2.523694,-9.376306,8.324077,9.581691,-0.432901,-5.555783,3.997402],[-2.175532,-3.516023,-6.241008,6.708263,1.907977,6.497652,6.794187,-6.890228,-7.806062],[2.256237,9.937399,-3.484772,5.434361,-9.922641,-6.901247,-3.887912,-6.473656,-5.051741],[-4.278272,-1.378153,0.276556,0.553449,-1.653536,-9.332978,-4.007973,-1.142739,-6.084256],[-3.430430,3.937277,7.841727,-1.866089,4.019192,8.751788,7.847262,1.374905,7.739639],[8.808250,-0.238184,-8.474076,-4.473241,-9.096250,-0.609202,-3.779351,-5.738581,-8.172088],[2.975524,-4.908425,4.866997,4.530805,6.695257,-4.318436,1.059713,3.032824,8.089045],[-4.515105,-6.967466,-7.086265,6.788915,-5.269391,4.965712,-1.935158,9.982084,7.008148],[-1.526001,-2.109172,2.178792,-6.019608,-3.873313,-3.101984,-2.155855,-0.121946,9.578752],[0.575406,3.811649,9.449498,-2.655203,4.065638,-6.695901,-9.561042,9.447621,-4.868853],[3.086670,-1.265591,-1.793824,-3.051353,6.890511,-0.956988,8.039703,-1.776646,7.674626],[8.039218,4.571419,8.225423,9.637759,-3.849973,-8.210685,-4.554631,1.499564,-4.795424],[6.371836,-9.213363,2.083972,-6.060519,9.205547,6.781189,-9.934943,-4.612692,4.777711],[5.733727,-9.479812,-4.556978,-9.790402,-7.530638,3.090717,9.350917,0.373542,1.520501],[-4.053838,-4.561485,-6.416825,-4.076648,-5.139783,-4.887417,7.684769,3.104234,2.221999],[-8.818909,-3.132787,-7.264641,6.089775,-8.405246,4.864653,0.036634,3.527583,8.333992],[0.094215,-3.510528,6.177406,-6.534637,-6.105389,-9.562096,7.876049,0.181004,2.758528],[4.961415,-3.401903,-9.009792,4.294536,7.428325,3.294398,8.062993,9.221477,-3.206808],[-2.784645,2.246900,-8.722485,5.819849,-2.340406,7.054995,-9.020386,2.537051,5.611192],[-2.764947,1.774163,0.201260,1.809208,-3.361535,5.493348,7.902823,9.499845,-9.388351],[-7.393661,9.964935,6.485236,-7.003428,9.678206,-4.583375,0.955206,4.793570,-2.962790],[4.476377,5.348786,-7.495048,9.854934,4.908021,-1.313871,-5.453407,3.573674,-4.583200],[9.922180,-3.053444,-9.090500,4.957146,1.610639,-8.862916,2.997470,4.638825,1.921089],[7.586247,5.203067,0.701007,1.444269,-0.203393,6.125493,6.047179,-8.639997,3.780732],[-0.528042,-7.858535,-3.298673,8.072296,2.863146,-0.816312,1.036511,9.455375,-9.789867],[-0.696781,-1.257340,-2.890161,4.327124,-3.299187,4.408081,-3.927898,-3.779371,-6.395683],[-3.396355,8.518627,-8.799963,-9.474567,2.399573,7.212415,4.381398,2.054982,-4.643364],[1.003159,6.026826,2.666858,-3.303816,-3.664975,9.695407,7.811726,4.742811,2.132013],[-8.808777,3.501582,3.143553,-3.718945,-5.639720,-9.132603,8.484450,8.838097,-5.165406],[-3.850535,-8.743366,8.447093,0.114735,9.204524,9.779813,-8.446415,4.757214,-6.241184],[-7.173676,5.259708,-2.120750,-0.367360,6.867286,0.490711,-3.965572,-5.731510,-1.146620],[-5.186511,-0.641595,-9.841918,-4.117737,-7.015448,-1.274115,-5.029742,0.992739,-0.014607],[-6.230982,5.444760,-1.079048,8.974188,-4.506622,4.670710,9.915532,-9.405141,-5.652690],[-6.144115,-6.389165,-4.369205,7.287457,7.811035,-2.595410,-4.156505,-2.484370,-8.077126],[-2.794034,-9.125409,-2.961726,-8.869888,0.663335,8.994171,4.795180,8.270781,-2.598911],[2.232402,-6.739039,-8.456495,-5.664951,7.334432,0.324925,0.392606,4.883000,-9.079074],[8.020455,-7.549827,-1.988702,-8.760458,1.182325,0.039542,4.428483,1.757898,4.177095],[-5.100357,-6.089098,7.698864,-3.122560,-7.310292,-2.184870,8.248977,0.799973,-0.715568],[1.952944,7.775164,-3.927738,7.978387,9.683856,-7.952003,-8.271583,-1.936247,-5.413955],[-4.490631,-7.829562,3.338124,-5.514037,4.490863,-2.405046,6.307771,-6.667112,-8.494168],[1.263303,8.558857,-8.723113,3.041740,-7.729210,6.682335,2.058020,3.289422,-1.448143]], dtype = "float32")#candidate|4561|(728, 9)|const|float32
bop_4562 = relay.not_equal(uop_4547.astype('bool'), const_4561.astype('bool')) # shape=(728, 9)
bop_4565 = relay.not_equal(uop_4549.astype('bool'), const_4561.astype('bool')) # shape=(728, 9)
uop_4569 = relay.acos(const_4561.astype('float32')) # shape=(728, 9)
uop_4575 = relay.atanh(uop_4569.astype('float64')) # shape=(728, 9)
bop_4577 = relay.equal(uop_4575.astype('bool'), relay.reshape(bop_4562.astype('bool'), relay.shape_of(uop_4575))) # shape=(728, 9)
bop_4580 = relay.equal(uop_4575.astype('bool'), relay.reshape(bop_4565.astype('bool'), relay.shape_of(uop_4575))) # shape=(728, 9)
uop_4587 = relay.exp(uop_4575.astype('float32')) # shape=(728, 9)
func_3941_call = mod.get_global_var('func_3941')
func_3942_call = mutated_mod.get_global_var('func_3942')
call_4589 = relay.TupleGetItem(func_3941_call(), 0)
call_4590 = relay.TupleGetItem(func_3942_call(), 0)
func_4128_call = mod.get_global_var('func_4128')
func_4130_call = mutated_mod.get_global_var('func_4130')
call_4593 = func_4128_call()
call_4594 = func_4128_call()
func_4384_call = mod.get_global_var('func_4384')
func_4386_call = mutated_mod.get_global_var('func_4386')
call_4596 = func_4384_call()
call_4597 = func_4384_call()
output = relay.Tuple([call_4514,call_4524,const_4525,var_4538,bop_4577,uop_4587,call_4589,call_4593,call_4596,])
output2 = relay.Tuple([call_4515,call_4526,const_4525,var_4538,bop_4580,uop_4587,call_4590,call_4594,call_4597,])
func_4602 = relay.Function([var_4538,], output)
mod['func_4602'] = func_4602
mod = relay.transform.InferType()(mod)
mutated_mod['func_4602'] = func_4602
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4603 = relay.var("var_4603", dtype = "int8", shape = (75,))#candidate|4603|(75,)|var|int8
func_4602_call = mutated_mod.get_global_var('func_4602')
call_4604 = func_4602_call(var_4603)
output = call_4604
func_4605 = relay.Function([var_4603], output)
mutated_mod['func_4605'] = func_4605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3359_call = mod.get_global_var('func_3359')
func_3360_call = mutated_mod.get_global_var('func_3360')
call_4618 = relay.TupleGetItem(func_3359_call(), 0)
call_4619 = relay.TupleGetItem(func_3360_call(), 0)
output = relay.Tuple([call_4618,])
output2 = relay.Tuple([call_4619,])
func_4624 = relay.Function([], output)
mod['func_4624'] = func_4624
mod = relay.transform.InferType()(mod)
output = func_4624()
func_4625 = relay.Function([], output)
mutated_mod['func_4625'] = func_4625
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4654 = relay.const([[[9.440464,-7.459628,-6.017301],[1.833107,0.134263,-0.307302],[9.959400,4.245859,-1.076984],[-2.890203,5.117117,-6.514411],[5.102724,7.196299,-8.884856],[-3.303713,1.603230,-4.341474],[-8.057478,-1.016032,-0.735550],[3.581271,-6.417411,-7.118726],[-3.017340,6.160337,8.326773],[-4.785981,-5.312635,8.089943]],[[9.160877,5.494157,3.926666],[-7.427632,3.388813,7.054921],[1.977273,4.528676,8.566112],[-0.403544,2.013542,1.898308],[-9.608713,6.166566,2.360936],[9.026114,-9.906162,-2.350672],[-8.829197,5.727366,5.966634],[-4.158095,0.146109,1.329030],[4.347190,-1.582568,0.002902],[8.333831,-4.784322,-4.952289]],[[1.425012,-4.473073,-3.942765],[4.504599,2.718657,4.798681],[-0.716983,-8.222653,0.963354],[-3.000591,0.897566,0.763244],[6.786539,-6.721306,0.121744],[1.248601,4.172144,-7.684952],[-7.732889,-3.765834,-2.777316],[9.381715,5.253825,-4.729468],[9.384655,1.041955,-4.719328],[0.792810,6.158634,0.095586]],[[-1.866758,-3.025992,-1.178770],[-7.217513,-3.095931,-8.392822],[-5.333080,7.949311,5.553708],[-5.424866,4.067701,-9.331102],[2.111658,7.791009,1.241329],[1.723392,1.386180,1.335366],[8.477961,0.829202,3.415339],[-3.528840,6.524728,9.946303],[-3.848335,5.859712,-1.188429],[9.184975,0.018150,-3.013366]],[[8.261834,-6.988034,0.520913],[-5.906074,5.501135,9.539639],[0.066406,-3.156001,7.039141],[-6.326105,-5.355528,1.540421],[9.768844,-9.873751,3.049327],[1.000759,-4.589301,-8.348476],[-7.135080,-5.777341,-3.761968],[-3.068237,-7.900570,-0.188746],[-4.533144,8.639205,-5.518819],[2.231936,3.319322,-2.876984]],[[2.765871,9.789972,4.854401],[7.835629,-6.898973,-8.491729],[6.247357,-0.480069,6.115986],[-3.808374,1.146211,-4.055128],[-7.406381,9.941808,6.689691],[0.993381,-0.085612,3.939810],[-1.816684,1.389661,-2.922871],[4.773445,-2.060300,8.125372],[-4.420958,4.457483,7.263756],[9.647852,-5.067243,2.476513]],[[-5.685866,-5.238511,5.495273],[-8.532691,-5.165462,-2.789926],[9.157243,9.558067,-0.269986],[-8.611526,-2.897385,-7.871784],[8.107802,0.911757,4.654917],[-6.904581,7.568162,-0.920434],[-7.272380,-4.128050,-7.130418],[9.077902,-4.142358,4.146190],[-1.151293,1.722740,4.269740],[-5.913809,3.322156,-7.331373]],[[3.802703,-0.496329,9.897108],[1.727314,-5.903210,6.495146],[2.790735,-5.077263,9.452609],[-3.028740,3.209839,-8.506208],[8.596816,-8.857100,-4.868693],[4.408806,7.189892,0.210970],[-7.355021,-2.018904,-0.681536],[7.623019,-2.155879,-9.300897],[6.708729,4.087590,-4.454859],[-8.920467,2.686602,7.631671]],[[7.287408,4.700735,-3.152658],[-2.301831,0.676455,0.279966],[-7.624290,2.658492,0.366874],[-9.574574,-2.143417,4.160683],[9.346113,4.225169,-6.729583],[-7.854564,6.149822,-1.959716],[-3.403003,9.262488,2.875580],[-9.540354,1.749547,0.719968],[9.326334,-7.339836,6.159747],[-3.258023,6.987115,1.609832]],[[-6.239086,0.544804,8.805243],[-3.185263,-2.543911,-5.301466],[-6.144800,2.954469,-5.095879],[-7.447414,-6.348042,-0.171757],[9.430136,-0.723971,-9.256591],[-1.452306,-2.980035,-7.870119],[-7.119601,6.333609,-3.984118],[-5.087608,-1.328783,0.639792],[-7.159277,-8.233857,-9.839515],[6.546600,-7.348844,-3.652750]],[[6.614572,5.347622,-5.456125],[-7.237431,-2.917645,-3.052637],[0.469901,-0.764993,-9.186399],[-6.658670,1.181512,-0.123502],[4.680729,0.385847,1.814844],[-3.303618,1.405541,-3.211502],[-6.454405,-5.602873,7.548926],[6.468766,6.677974,-2.632890],[1.120722,8.856401,-4.679813],[-3.770097,2.516933,4.844046]],[[2.773474,3.343624,3.401898],[5.056097,-6.242960,3.497754],[-3.903589,-4.588341,-0.473902],[3.937927,-6.294420,-5.565399],[-2.284800,-5.925188,2.866754],[7.520477,-6.033675,0.883430],[-5.513856,9.584427,-7.380008],[-4.696070,1.175870,-5.245698],[-8.829897,-6.547951,-0.296123],[2.328670,8.099711,-7.907551]],[[3.250078,-4.085446,7.149882],[7.746043,-1.420534,-1.455188],[1.053441,0.506626,-9.933878],[-4.241178,0.009353,0.368144],[-0.615475,8.423929,-5.664540],[-2.508769,4.295379,1.502930],[-1.350822,-9.846488,2.923976],[8.866817,-9.100108,-8.689812],[-4.310325,8.026371,7.194317],[-5.037352,3.630450,9.507599]],[[1.851996,0.244024,-3.123291],[7.642987,7.361902,1.196847],[9.459052,-2.163015,0.727218],[-0.756902,2.155876,-9.714098],[-4.413626,-0.238103,-4.492552],[4.725563,1.753445,-3.835428],[-3.138604,-6.663668,5.674888],[-4.355916,-4.035662,-0.885178],[4.636376,-2.417488,-7.072453],[3.921606,1.515310,-7.959372]],[[-5.601217,0.341507,-2.963181],[6.563524,-9.702603,8.406188],[-0.424045,-7.111752,-8.553251],[-2.806328,8.961547,-2.288457],[7.205479,-0.706856,-6.874177],[-7.702386,-2.593089,-8.784194],[1.179679,0.685380,-4.779897],[-9.280373,2.493056,9.865188],[8.407263,5.616516,-8.913449],[5.779164,-4.770141,-1.228665]]], dtype = "float64")#candidate|4654|(15, 10, 3)|const|float64
var_4655 = relay.var("var_4655", dtype = "float64", shape = (15, 10, 3))#candidate|4655|(15, 10, 3)|var|float64
bop_4656 = relay.divide(const_4654.astype('float64'), relay.reshape(var_4655.astype('float64'), relay.shape_of(const_4654))) # shape=(15, 10, 3)
func_2399_call = mod.get_global_var('func_2399')
func_2400_call = mutated_mod.get_global_var('func_2400')
call_4659 = relay.TupleGetItem(func_2399_call(), 1)
call_4660 = relay.TupleGetItem(func_2400_call(), 1)
uop_4662 = relay.asinh(call_4659.astype('float64')) # shape=(12, 11, 2)
uop_4664 = relay.asinh(call_4660.astype('float64')) # shape=(12, 11, 2)
func_3628_call = mod.get_global_var('func_3628')
func_3629_call = mutated_mod.get_global_var('func_3629')
call_4673 = relay.TupleGetItem(func_3628_call(), 0)
call_4674 = relay.TupleGetItem(func_3629_call(), 0)
output = relay.Tuple([bop_4656,uop_4662,call_4673,])
output2 = relay.Tuple([bop_4656,uop_4664,call_4674,])
func_4675 = relay.Function([var_4655,], output)
mod['func_4675'] = func_4675
mod = relay.transform.InferType()(mod)
mutated_mod['func_4675'] = func_4675
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4676 = relay.var("var_4676", dtype = "float64", shape = (15, 10, 3))#candidate|4676|(15, 10, 3)|var|float64
func_4675_call = mutated_mod.get_global_var('func_4675')
call_4677 = func_4675_call(var_4676)
output = call_4677
func_4678 = relay.Function([var_4676], output)
mutated_mod['func_4678'] = func_4678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4335_call = mod.get_global_var('func_4335')
func_4336_call = mutated_mod.get_global_var('func_4336')
call_4689 = relay.TupleGetItem(func_4335_call(), 1)
call_4690 = relay.TupleGetItem(func_4336_call(), 1)
var_4704 = relay.var("var_4704", dtype = "uint32", shape = (16, 2, 12))#candidate|4704|(16, 2, 12)|var|uint32
bop_4705 = relay.power(call_4689.astype('float64'), relay.reshape(var_4704.astype('float64'), relay.shape_of(call_4689))) # shape=(16, 2, 12)
bop_4708 = relay.power(call_4690.astype('float64'), relay.reshape(var_4704.astype('float64'), relay.shape_of(call_4690))) # shape=(16, 2, 12)
bop_4713 = relay.divide(call_4689.astype('float64'), relay.reshape(var_4704.astype('float64'), relay.shape_of(call_4689))) # shape=(16, 2, 12)
bop_4716 = relay.divide(call_4690.astype('float64'), relay.reshape(var_4704.astype('float64'), relay.shape_of(call_4690))) # shape=(16, 2, 12)
output = relay.Tuple([bop_4705,bop_4713,])
output2 = relay.Tuple([bop_4708,bop_4716,])
func_4739 = relay.Function([var_4704,], output)
mod['func_4739'] = func_4739
mod = relay.transform.InferType()(mod)
mutated_mod['func_4739'] = func_4739
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4740 = relay.var("var_4740", dtype = "uint32", shape = (16, 2, 12))#candidate|4740|(16, 2, 12)|var|uint32
func_4739_call = mutated_mod.get_global_var('func_4739')
call_4741 = func_4739_call(var_4740)
output = call_4741
func_4742 = relay.Function([var_4740], output)
mutated_mod['func_4742'] = func_4742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2399_call = mod.get_global_var('func_2399')
func_2400_call = mutated_mod.get_global_var('func_2400')
call_4841 = relay.TupleGetItem(func_2399_call(), 0)
call_4842 = relay.TupleGetItem(func_2400_call(), 0)
output = relay.Tuple([call_4841,])
output2 = relay.Tuple([call_4842,])
func_4852 = relay.Function([], output)
mod['func_4852'] = func_4852
mod = relay.transform.InferType()(mod)
mutated_mod['func_4852'] = func_4852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4852_call = mutated_mod.get_global_var('func_4852')
call_4853 = func_4852_call()
output = call_4853
func_4854 = relay.Function([], output)
mutated_mod['func_4854'] = func_4854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3359_call = mod.get_global_var('func_3359')
func_3360_call = mutated_mod.get_global_var('func_3360')
call_4858 = relay.TupleGetItem(func_3359_call(), 1)
call_4859 = relay.TupleGetItem(func_3360_call(), 1)
output = call_4858
output2 = call_4859
func_4863 = relay.Function([], output)
mod['func_4863'] = func_4863
mod = relay.transform.InferType()(mod)
output = func_4863()
func_4864 = relay.Function([], output)
mutated_mod['func_4864'] = func_4864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4499_call = mod.get_global_var('func_4499')
func_4500_call = mutated_mod.get_global_var('func_4500')
call_4946 = relay.TupleGetItem(func_4499_call(), 0)
call_4947 = relay.TupleGetItem(func_4500_call(), 0)
output = relay.Tuple([call_4946,])
output2 = relay.Tuple([call_4947,])
func_4958 = relay.Function([], output)
mod['func_4958'] = func_4958
mod = relay.transform.InferType()(mod)
mutated_mod['func_4958'] = func_4958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4958_call = mutated_mod.get_global_var('func_4958')
call_4959 = func_4958_call()
output = call_4959
func_4960 = relay.Function([], output)
mutated_mod['func_4960'] = func_4960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3181_call = mod.get_global_var('func_3181')
func_3182_call = mutated_mod.get_global_var('func_3182')
call_4978 = relay.TupleGetItem(func_3181_call(), 0)
call_4979 = relay.TupleGetItem(func_3182_call(), 0)
func_1401_call = mod.get_global_var('func_1401')
func_1403_call = mutated_mod.get_global_var('func_1403')
var_4990 = relay.var("var_4990", dtype = "float32", shape = (234,))#candidate|4990|(234,)|var|float32
call_4989 = relay.TupleGetItem(func_1401_call(relay.reshape(var_4990.astype('float32'), [6, 13, 3])), 0)
call_4991 = relay.TupleGetItem(func_1403_call(relay.reshape(var_4990.astype('float32'), [6, 13, 3])), 0)
output = relay.Tuple([call_4978,call_4989,var_4990,])
output2 = relay.Tuple([call_4979,call_4991,var_4990,])
func_5003 = relay.Function([var_4990,], output)
mod['func_5003'] = func_5003
mod = relay.transform.InferType()(mod)
var_5004 = relay.var("var_5004", dtype = "float32", shape = (234,))#candidate|5004|(234,)|var|float32
output = func_5003(var_5004)
func_5005 = relay.Function([var_5004], output)
mutated_mod['func_5005'] = func_5005
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5036 = relay.var("var_5036", dtype = "float64", shape = (8, 9, 7))#candidate|5036|(8, 9, 7)|var|float64
var_5037 = relay.var("var_5037", dtype = "float64", shape = (8, 9, 7))#candidate|5037|(8, 9, 7)|var|float64
bop_5038 = relay.floor_divide(var_5036.astype('float64'), relay.reshape(var_5037.astype('float64'), relay.shape_of(var_5036))) # shape=(8, 9, 7)
output = relay.Tuple([bop_5038,])
output2 = relay.Tuple([bop_5038,])
func_5041 = relay.Function([var_5036,var_5037,], output)
mod['func_5041'] = func_5041
mod = relay.transform.InferType()(mod)
mutated_mod['func_5041'] = func_5041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5041_call = mutated_mod.get_global_var('func_5041')
var_5043 = relay.var("var_5043", dtype = "float64", shape = (8, 9, 7))#candidate|5043|(8, 9, 7)|var|float64
var_5044 = relay.var("var_5044", dtype = "float64", shape = (8, 9, 7))#candidate|5044|(8, 9, 7)|var|float64
call_5042 = func_5041_call(var_5043,var_5044,)
output = call_5042
func_5045 = relay.Function([var_5043,var_5044,], output)
mutated_mod['func_5045'] = func_5045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3258_call = mod.get_global_var('func_3258')
func_3259_call = mutated_mod.get_global_var('func_3259')
call_5124 = relay.TupleGetItem(func_3258_call(), 1)
call_5125 = relay.TupleGetItem(func_3259_call(), 1)
output = relay.Tuple([call_5124,])
output2 = relay.Tuple([call_5125,])
func_5131 = relay.Function([], output)
mod['func_5131'] = func_5131
mod = relay.transform.InferType()(mod)
output = func_5131()
func_5132 = relay.Function([], output)
mutated_mod['func_5132'] = func_5132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5131_call = mod.get_global_var('func_5131')
func_5132_call = mutated_mod.get_global_var('func_5132')
call_5169 = relay.TupleGetItem(func_5131_call(), 0)
call_5170 = relay.TupleGetItem(func_5132_call(), 0)
func_2540_call = mod.get_global_var('func_2540')
func_2545_call = mutated_mod.get_global_var('func_2545')
var_5174 = relay.var("var_5174", dtype = "float32", shape = (220,))#candidate|5174|(220,)|var|float32
const_5175 = relay.const([-10,2,9,-4,8,7,3,7,-8,-3,5,1,-4,-2,-7,-2,5,-8,-9,5,-10,-3,4,6,-8,-4,-4,-9,-9,9,-4,-2,-7,3,-5,-3,3,-10,5,8,7,-8,-8,1,8,5,3,2,2,-7,-4,-3,-4,3,-9,5,-4,6,10,1,-7,1,-6,1,-8,4,-7,-10,-2,-4,-5,-6,2,3,1,-1,2,10,4,-7,-10,-6,-10,9,9,-2,2,7,1,-5,4,5,-5,6,-8,4,4,4,4,3,-9,-2,-4,-5,7,-9,4,-10,9,-10,9,-5,-2,6,-6,-1,-5,-6,-10,-3,-8,1,-6,-5,-7,2,-9,-8,7,10,4,-8,4,7,2,-4,-2,-6,-6,-3,-6,-8,3,-7,-1,-4,8,-3,6,10,-9,10,-9,-2,-7,-9,-2,-7,4,-7,-1,-9,5,-3,3,-8,-8,-6,7,2,-4,7,8,3,10,-7,1,3,-10,-6,10,7,-4,-4,2,-9,9,-2,-1,-10,-5,3,-7,-9,-3,-1,-8,-2,1,7,4,-10,1,-1,-9,5,-2,-7,7,5,2,4,2,6,3,-9,-9,-1,4,-5,7,-6,-8,-7,10,4,5,4,3,-5,3,-5,-4,5,10,-1,-7,5,10,10,-1,-4,2,8,-9,-2,-8,7,3,9,9,2,7,-3,9,-10,8,9,-3,-5,-1,-7,6,-10,-5,4,-1,1,-4,-6,8,1,2,-5,-10,-7,9,-7,-7,6,8,-7,-6,8,3,-1,1,-6,-4,6,-3,-5,7,1,-1,-8,-7,-7,-1,3,10,-4,5,-2,3,5,10,-2,3,5,-10,-4,-5,-10,-7,-2,-6,-6,8,-2,-5,-1,-8,-4,-8,-5,-1,5,-10,-2,-9,-2,3,-8,5,4,-10,4,9,8,-8,-6,-2,3,-8,-10,3,4,1,7,-3,-5,7,10,7,3,-1,-4,-10,8,4,-6,2,-3,3,9,4,-8,3,-8,6,-8,2,3,-9,-1,10,1,9,-5,5,-10,-9,-1,6,5,-3,-10,-2,-9,5,5,-1,-7,10,5,-7,-8,3,9,9,3,6,10,-8,9,1,9,10,-2,-10,-8,2,-5,5,6,9,-9,3,-3,8,-6,-5,1,-5,-6,2,5,-1,-10,-8,2,6,-2,-1,-1,8,8,-6,-9,-3,-7,-10,-2,-3,-7,1,-8,-3,5,7,2,7,1,10,4,4,2,-4,-4,9,7,1,6,-8,-9,-8,2,-1,-1,-2,6,-8,9,5,10,7,3,-5,-3,1,-1,10,-6,-8,-6,2,8,10,-2,3,8,-9,7,9,8,9,-1,-5,-4,2,5,1,3,-1,8,-5,3,9,-10,9,10,-9,8,6,9,1,-3,5,8,9,9,4,9,-1,2,7,7,5,-2,-9,-10,-2,5,-6,-3,-8,-10,6,6,6,-7,-1,1,-10,-6,1,-1,8,-10,10,-1,8,1,-1,-1,-6,-2,-3,-3,-7,1,-5,-2,-10,-9,-6,1,4,-9,-10,1,-1,10,-7,6,-4,-3,1,3,-8,4,-5,-9,6,1,10,-9,-7,4,6,10,-7,6,-8,1,-3,1,9,-6,-10,10,-1,1,-2,5,-5,7,-10,3,-3,-6,-1,-4,-7,-7,9,6,-10,1,-4,-1,1,-2,-10,9,-1,-10,9,3,6,2,-7,7,-7,-9,-3,1,-6,-5,10,-10,8,-1,3,5,-4,-5,7,-8,10,-5,-8,7,9,-2,5,-10,-1,-9,5,-4,-1,9,10,-4,5,-1,8,-8,-9,8,10,6,8,-6,9,1,-8,10,8,-6,3,-5,-9,-8,3,2,-3,-5,-4,-6,-10,3,-9,-5,8,9,3,2,9,10,-7,5,3,-3,-10,7,7,-7,-4,-3,-6,-4,8,-10,-10,-9,5,9,4,2,-2,-6,-1,-3,-7,-9,-9,-1,3,-6,-4,-1,10,4,5,-10,6,-6,-8,6,-7,8,2,-7,-3,-7,9,-3,-10,-5,-4,2,10,7,-8,5,7,-5,5,3,4,-4,-10,2,-5,-4,3,-8,-5,4,7,-1,3,5,-8,7,-10,5,-9,1,7,4,3,-4,7,2,-5,10,10,7,6,2,-6,-10,-5,10,6,1,-6,-8,2,6,-4,7,-4,4,2,-9,-4,-5,10,2,-1,-5,-9,-9,2,8,4,2,4,9,3,-4,7,-7,-5,2,1,3,2,-8,-9,-2,6,10,-1,5,1,2,-1,4,5,3,5,5,8,-2,4,10,10,-9,3,7,-5,1,-10,-1,-2,1,10,7,-1,-7,-4,4,-8,-7,7,4,-4,6,-1,9,3,3,7,-5,8,5,10,-8,-10,-1,10,7,-2,8,-1,-7,8,-10,-9,-5,-7,-2,10,5,-4,5,2,8,6,-7,2,5,-5,6,10,-2,-4,3,-4,-1,5,-2,1,-2,5,-6,-5,-8,-6,6,-8,2,-5,-5,5,7,4,-8,-9,-2,4,-1,10,1,4,1,-6,-3,10,-9,-3,-5,-8,-2,7,-3,-3,-10,-6,9,8,1,3,-6,1,7,4,3,-9,10,8,-7,-8,5,7,5,4,-1,1,9,5,-7,10,-10,4,4,-3,-6,5,-6,-5,-10,-8,-5,8,-2,10,1,-1,10,1,1,3,5,-9,2,4,1,3,-1,-10,6,-4,1,-8,-3,4,-2,-1,5,-2,4,-9,7,10,4,3,-1,7,-4,-4,-5,-5,3,6,8,7,3,8,9,-8,-10,-5,9,5,-8,-4,-7,-9,-7,-10,-4,-6,4,-7,-3,-8,-7,6,-6,3,9,-6,-6,-7,-4,7,-6,5,6,3,-6,-2,3,-10,6,2,1,-2,-4,10,-7,-6,-8,3,10,3,8,-10,1,1,-3,7,-2,1,-9,6,7,-1,10,1,9,-9,-1,-9,8,2,-2,7,9,9,-10,3,6,6,-7,9,3,4,-4,-6,2,6,-8,-7,-3,-4,3,10,-3,-7,-5,8,-4,-2,7,3,-8,3,-3,5,-9,7,-8,3,-5,-4,9,-8,8,3,8,5,6,5,10,-5,9,-1,1,2,6,-8,-10,10,-6,3,1,-1,-6,8,4,-5,7,2,1,6,10,6,10,-9,-1,10,10,10,-6,10,-4,-7,-10,-1,-4,10,-2,-5,-4,-9,-7,-6,-10,3,-9,-10,-9,-5,5,-1,2,-3,10,7,4,-9,-2,-8,-3,10,3,6,4,-10,-5,8,-4,2,-10,-8,-2,3,-1,-8,-3,8,-8,-7,-4,-1,-2,8,9,10,8,4,-4,-6,10,-1,4,-9,4,5,7,-8,-7,4,8,-7,-1,-8,8,2,-2,10,-4,8,-7,7,1,2,4,5,-10,-2,-1,-8,6,6,-4,-6,5,6,7,5,-9,-7,3,-6,-2,3,-9,-4,-2,-5,-9,5,-4,-8,-2,-10,-2,-5,7,-7,2,-4,-3,-7,1,9,4,-3,-5,-9,6,2,-6,-2,-10,6,10,-2,10,-6,-3,10,1,6,-6,4,6,-9,-3,-9,-1,5,-5,-2,6,4,5,9,-9,1,-1,7,-3,4,-9,-8,-6,-2,10,5,-4,-7,5,4,-2,7,-1,3,-1,9,9,-10,10,7,-6,6,-3,8,1,-10,-6,-6,-3,3,5,-6,1,9,-8,1,-9,3,-2,-8,2,3,8,6,-8,5,-3,6,-7,-5,-1,10,-5,-2,5,-9,-9,-4,4,8,9,5,-6,-5,-8,-9,-7,9,-3,9,2,-4,10,7,10,-6,-1,-2,-4,2,-7,2,-10,-10,-3,-3,-6,-5,-5,-10,10,-5,-9,-7,-5,-6,10,10,9,4,-6,-7,4,-9,-6,5,5,6,8,-6,2,7,7,3,5,10,-6,6,-10,-8,-3,2,-4,3,-4,5,10,10,-7,-7,-2,-6,5,8,-6,-4,9,1,6,5,5,-6,2,-4,10,-3,-10,1,-2,3,-5,-9,2,-8,-5,6,3,-5,-9,5,-2,-4,-1,10,-5,-1,9,-5,-1,-9,7,4,-9,-6,8,8,4,-4,8,-6,4,-3,9,-4,-10,5,-10,9,8,8,1,-7,9,-9,3,7,-5,2,8,-4,-3,-8,-8,2,6,-1,5,1,-7,-10,8,-2,10,6,-2,-8,9,-7,7,-10,-7,-10,-1,8,-3,-10,10,3,6,7,10,-4,-5,4,10,5,-9,2,5,-7,2,7,-9,-1,-10,6,6,-8,1,-3,10,-10,10,-6,-4,3,-10,8,-3,-6,-7,-4,2,-4,-6,6,2,6,8,8,4,-1,-4,-6,8,-9,-4,-10,6,1,-2,9,-3,-7,-6,-4,-6,7,-4,8,-4,-8,1,7,3,-1,-3,8,-5,8,2,4,-8,10,5,-5,5,7,3,-1,-2,-3,3,2,8,1,-1,-8,7,3,5,1,3,-4,-4,5,9,10,1,2,-9,9,-2,-10,-4,3,3,7,-3,-2,-8,-2,7,1,-3,7,-9,-5,3,2,-10,-9,8,-9,-9,-8,10,-5,2,-6,2,9,10,-2,9,4,-8,2,-9,7,-2,6,-4,10,9,-3,9,-2,-5,-6,8,-4,1,2,-7,-7,-3,2,3,7,7,-3,-3,-7,-9,5,-1,6,6,-3,7,3,-4,-9,-8,9,8,2,-6,2,-2,-7,-5,-8,-10,-6,-2,7,6,2,-4,-9,-2,-4,2,8,-2,-6,7,-9,-4,2,-4,1,-8,-3,-4,5,-5,-6,6,8,10,-6,-9,-2,10,10,-6,5,6,6,-2,5,3,-4,-9,8,10,4,1,-4,-1,-6,-9,-9,-10,-2,8,-2,1,2,10,-9,6,-10,9,-7,-2,5,3,-4,-1,-7,-6,-1,-5,-8,1,-5,-1,3,9,-8,2,-2,-1,9,-5,-2,5,1,-4,-5,6,-5,5,7,-7,-4,-2,5,-3,5,1,10,-1,-8,-9,4,-2,-4,-7,2,-8,5,5,1,-6,-7,-6,-5,-7,3,-7,-3,6,-8,8,6,-6,-4,-1,-10,-3,-4,-5,5,-1,10,-5,-6,10,-1,6,4,6,-5,-7,4,4,-7,8,-3,-10,6,5,4,10,6,3,-7,2,-8,7,-8,-9,-9,9,-5,-6,2,-6,9,-4,-9,-8,5,-6,-8,-4,-5,-3,1,8,-9,-8,-6,-9,-8,1,-7,-4,9,-7,5,5,-4,4,-10,-1,7,-2,-4,7,4,-1,-6,-7,-7,4,-4,3,9,5,-2,-10,8,1,5,-5,-5,-3,-3,6,3,-3,-10,8,4,3,-2,4,-7,3,10,-4,-4,3,-5,9,-10,-8,-7,-2,-10,8,7,1,4,7,-9,6,-8,-3,10,5,-4,-2,7,-3,-8,6,-2,3,-8,7,-3,-5,6,6,-1,7,1,-8,3,5,4,-1,10,-10,4,8,-2,8,2,-3,-2,6,-10,-4,-8,4,-2,-8,-9,-1,-6,2,-3,-8,-4,-5,1,-10,8,4,2,-9,5,7,4,8,-8,-9,-1,-3,8,-1,-1,-10,6,-6,3,5,1,-1,9,-8,-2,-5,6,7,-7,-4,3,9,7,-10,-1,8,4,-8,9,-9,4,5,3,3,2,10,1,-5,-5,1,-9,-7,-8,-5,10,9,9,4,-6,3,4,5,3,4,-6,-3,3,5,4,8,7,9,-9,-9,-10,5,8,-7,-2,8,-7,-1,10,10,10,-9,3,-3,1,-9,6,2,6,4,2,5,4,10,6,9,5,-2,-6,-3,7,-9,-8,7,-2,-1,3,-4,4,3,3,5,-10,8,-4,-4,-7,-3,3,10,-1,2,8,2,-1,3,7,-1,7,-4,4,-1,10,-5,-6,-10,5,2,9,7,-1,3,-6,-4,6,3,5,-1,10,1,1,2,5,-1,-9,4,7,-5,-2,8,-8,-9,7,-9,-8,-4,2,-8,1,9,8,-10,-1,-9,-6,4,-2,-7,5,-7,-6,5,-6,-5,2,8,9,6,3,-6,6,2,-3,6,-5,-4,-3,-9,1,9,9,-5,3,10,-9,-4,-6,-1,-5,8,2,-1,10,6,-5,7,2,2,-3,1,9,-5,2,-4,4,7,6,1,-7,9,3,5,6,-1,2,-1,9,-5,-3,-10,-5,-5,4,-8,6,-4,-1,-4,-8,8,-9,10,6,-1,-8,-7,7,-3,7,-1,-9,2,5,7,-3,3,5,-1,3,-9,4,-4,-6,-9,10,-8,8,7,5,7,2,-1,-5,7,6,-7,-1,-1,-9,2,2,-8,-9,4,-10,4,-2,8,-9,3,10,8,-4,10,9,5,-3,4,8,6,8,10,4,7,-5,-9,-4,-6,-5,-2,-10,6,7,-5,-7,-3,-8,-6,2,-6,-4,2,3,6,6,-2,4,10,-7,6,-4,10,-1,6,10,10,8,-1,10,1,-5,10,1,3,-5,-6,8,-2,-2,4,-2,-5,-6,3,6,-2,7,4,-4,-7,-4,5,-9,-2,-7,3,3,-10,-8,5,-9,9,-8,5,8,10,-5,5,-2,-6,-5,8,1,-7,5,5,8,9,6,8,7,7,3,-7,3,5,6,-6,-3,6,-6,1,6,9,-5,-8,-7,4,1,8,-7,-1,-8,10,3,-9,-10,10,2,9,-8,-10,4,-6,7,8,-5,-9,-10,-4,6,2,6,3,3,7,-9,-6,-3,9,-4,-4,-7,-4,1,-2,3,-6,-7,-9,10,-2,3,1,10,-3,-6,7,-1,4,1,2,9,-5,6,-7,-9,3,-6,-5,-4,-5,9,-6,3,4,-6,-9,2,-3,9,-3,8,-8,2,-5,6,-9,-9,5,4,9,-6,5,4,6,-8,2,7,-4,-7,-7,6,10,-10,-1,-4,4,-1,-8,9,-8,5,4,-2,-2,7,4,3,3,8,-8,4,-2,1,10,4,-8,10,10,2,2,9,-5,9,8,1,8,5,2,10,5,-2,2,7,-5,-3,-8,-3,7,-2,9,-10,-1,-9,-3,7,-2,3,10,-5,8,-9,2,-9,6,-5,-5,2,-2,-10,-9,-4,-5,-6,-6,-7,-10,-1,10,3,-1,1,-5,-5,5,1,4,6,4,-4,4,5,10,8,5,-8,-2,-6,3,4,-7,-3,-2,-10,-2,9,6,1,9,7,-1,-2,-3,9,-10,-3,10,9,4,10,-6,3,-2,-9,4,-7,-1,7,9,-2,-9,-7,-3,-2,-8,5,3,5,10,8,-1,8,-6,-6,1,4,-4,-10,7,-6,-8,8,-6,-9,-8,2,-10,1,-7,10,8,-9,-5,9,-5,-7,-5,4,-10,2,8,9,-6,5,-9,1,-9,10,-9,7,4,-7,-1,-2,4,8,8,3,8,-7,-2,-4,7,6,3,-10,-7,7,7,-8,-3,-6,-6,7,6,-2,-2,-9,10,-5,-7,1,-3,4,8,-5,-2,6,-8,3,6,-2,2,7,5,7,10,-7,-8,5,5,-9,-8,3,7,-2,1,-1,-3,7,2,-1,-1,3,1,5,7,1,10,-3,-9,-10,-9,5,9,2,-7,-2,-3,-10,-5,10,-1,-7,-4,8,5,6,-6,8,5,7,-6,2,3,6,7,10,-5,-8,9,-2,3,10,1,7,9,9,10,-7,-3,3,-6,-7,9,-10,3,-5,-4,-10,-3,2,-10,9,4,4,-6,-7,-1,-5,-2,-1,9,-3,-8,-7,-9,-5,3,10,-8,3,3,-8,4,5,10,-1,9,-1,9,10,-10,7,-8,9,3,-2,3,1,3,3,1,2,10,-8,3,8,-4,-5,2,-8,7,1,10,-7,-7,6,-6,7,4,-6,-3,10,-9,-10,10,-8,-8,7,1,4,-4,-4,-1,-6,-6,1,7,9,-8,-1,-6,5,7,5,6,6,10,-8,-2,-3,9,10,-7,3,7,-2,-2,1,9,-9,-3,-4,-6,-3,9,9,-2,-5,9,2,4,10,-3,7,-7,8,1,3,4,-6,-4,2,-3,4,-7,-9,-4,-8,2,-8,10,-8,-8,8,1,-7,-8,-10,10,-4,-4,-9,-4,3,10,4,9,-3,-7,1,5,-2,10,4,7,6,-1,-8,-2,10,6,4,-7,4,-9,1,-6,-7,-6,6,-6,-7,-7,-1,-7,1,-6,1,-3,9,-4,6,-5,6,-1,-7,5,6,-8,-1,10,10,-6,-9,-10,10,1,3,8,-9,4,-8,1,-2,-10,6,4,6,-9,-10,-3,2,-8,-2,-6,5,-1,10,-8,-1,-7,8,6,-1,9,5,-2,8,2,6,2,-10,6,-5,4,3,-4,3,5,7,5,-7,-9,-9,-6,-10,6,-3,10,7,3,-7,10,-9,6,-2,7,2,-6,-6,-5,5,6,4,-6,-2,-2,8,-1,-1,-4,-9,-2,-7,-9,-3,9,6,5,-1,-4,10,4,-7,8,1,1,-4,-1,3,4,-6,5,-6,3,-1,-10,10,10,8,-7,1,9,1,6,1,10,-3,-7,-5,-6,-7,9,10,-9,9,-7,4,-6,7,-6,2,-6,-3,3,5,-6,8,2,-5,8,6,4,3,-4,-2,1,-8,-8,-9,-1,-2,9,-10,-10,3,-1,-5,-9,-5,-1,3,10,8,-2,-10,-3,10,6,2,-7,6,-4,-2,-1,5,-3,-3,-10,10,-8,-5,-5,-3,-6,-9,-2,2,-5,-10,-3,-8,1,-7,2,5,10,-3,6,7,2,7,-10,1,-5,-2,4,-5,1,8,-1,-3,2,9,-1,9,2,-9,-7,10,9,-2,-1,-10,9,6,-10,3,7,1,8,-3,-6,-5,-3,6,-8,-7,-3,1,-6,4,-10,-9,10,-6,9,-3,2,-1,4,6,-6,-10,9,-3,-2,2,-7,-8,-2,7,2,8,9,-10,7,-6,-9,3,10,5,-4,-4,10,8,-4,5,7,1,-3,1,-7,2,-3,-5,3,-5,-9,-8,8,-2,4,-10,1,9,4,-5,-8,10,3,4,-7,5,-7,6,-2,10,8,-7,3,4,-9,-2,-9,8,-10,-8,-3,-3,-7,-6,9,-2,-7,-7,-8,-2,1,4,6,2,4,3,4,-8,6,9,-1,6,2,8,6,9,-4,7,-4,-8,-2,6,8,6,-9,1,6,7,9,-9,7,-2,10,-3,-2,-3,-3,-10,-4,-2,1,-2,-1,6,4,6,-3,2,-2,8,-7,6,-9,-8,-3,5,-6,-3,-3,8,4,9,-4,3,-6,-10,9,3,-2,-2,-5,-9,3,9,-10,-5,3,-4,-5,-5,-5,5,2,-3,-1,1,1,7,3,1,-5,10,10,-6,-8,-5,-9,8,-8,-8,-7,5,1,3,9,7,-2,-3,10,9,-2,2,7,-3,-2,-6,-9,4,-4,-4,-3,-9,8,9,-1,6,5,7,8,6,2,-7,-4,1,-2,-3,5,-1,-3,-1,-1,10,-4,7,-6,4,-7,-8,-3,-3,5,-1,-9,5,3,6,4,-9,2,2,10,-3,8,10,-10,8,8,-6,-2,-8,-9,-8,-2,-1,4,2,1,1,-7,-3,-3,-6,10,7,-5,6,3,4,2,10,9,8,-7,9,9,5,-1,-2,-3,3,-5,-9,-7,-2,8,-5,-5,-7,1,8,-8,-1,-4,-1,3,4,-5,4,7,10,-9,-4,-7,7,-9,-9,10,5,6,-2,2,-5,-2,-10,7,6,-5,2,-3,4,-8,8,-7,-1,-1,-10,-10,1,-3,2,-10,-8,1,1,-1,-8,7,6,-1,7,-1,-4,-1,4,3,-4,6,-10,-3,5,-5,2,8,-8,-4,-10,1,7,-6,-5,-9,-4,2,6,-4,-9,1,-2,9,10,4,-8,4,6,6,-9,-2,-2,6,2,-6,-8,4,9,-10,5,-9,-9,-8,-2,-8,-1,-3,-7,-10,8,1,4,8,7,4,-1,6,-5,7,-1,10,5,5,-2,-2,1,-8,1,10,-5,-1,-7,-8,-3,4,10,-4,-5,9,-3,10,8,-1,-6,-6,-5,-9,4,-9,-4,9,-4,1,5,9,-4,-4,-6,9,5,-5,10,7,3,3,6,5,6,-1,7,8,6,-4,-6,4,-6,-4,-3,4,-6,7,-8,3,-10,6,-4,-1,-8,-5,-5,6,10,-2,10,10,3,-7,2,7,-6,-9,9,3,2,2,6,3,-9,-8,-10,-4,-8,4,-2,-1,-3,-9,2,-8,9,-4,-9,3,-1,-6,3,-6,2,2,10,-4,-6,5,-4,-4,2,-2,-6,-8,9,-10,3,-3,5,-1,-3,-7,-8,8,-5,7,-10,-10,-5,5,-10,6,2,-10,-7,1,-6,8,3,5,8,-7,4,-7,6,3,-1,-1,10,-10,-2,8,1,1,-4,2,-2,-2,-4,5,5,6,-9,-6,10,-8,9,2,4,4,4,1,2,-2,6,-8,7,4,-3,-9,-8,-9,4,7,-7,-7,-6,6,-4,6,-8,-1,-8,-5,9,8,-2,6,-8,-6,-3,-5,3,-7,-4,9,5,8,-6,8,8,3,-1,-6,2,-4,-4,4,-4,6,-3,-7,4,-6,10,-4,-8,-8,5,-9,-3,4,4,5,-10,-4,-6,3,-8,-10,3,-9,-2,1,9,6,1,-9,9,-10,7,-2,-7,-4,-6,-5,10,-9,9,2,9,1,-10,-6,-8,-6,2,-9,4,2,-10,8,-1,2,6,9,4,5,4,-10,8,7,-5,7,-2,1,7,1,4,-1,9,-6,-2,6,-2,8,4,10,-2,1,9,5,1,8,-1,-8,9,-3,6,-6,-8,10,10,5,10,-7,10,-7,-9,-8,1,3,1,10,-7,-8,1,-1,2,4,-4,1,4,-4,-10,-5,8,1,-6,-9,-9,10,-6,2,6,10,-8,1,6,7,8,8,-2,7,2,-10,4,-3,-10,-10,3,-4,8,5,3,-3,7,-8,2,6,-1,7,4,-6,6,-1,-4,2,-4,-10,-10,-9,4,-6,5,2,-8,-1,-8,-9,3,-5,-6,-2,3,-9,-5,-2,10,-7,9,10,6,-2,-8,-1,10,9,5,10,1,3,-10,7,2,-6,1,8,7,4,-10,8,4,-8,7,7,7,-6,-2,10,6,4,-10,-7,-2,-6,-9,-4,2,-10,-2,-8,6,10,6,-1,-4,2,-7,4,-1,6,3,-10,4,3,-8,6,5,-3,6,7,-9,5,-7,9,-7,5,5,-6,-9,4,10,-3,-6,9,-10,-9,5,-9,2,8,1,1,1,4,8,9,-7,-4,9,-4,-10,-2,-8,-7,8,-10,-1,6,8,-3,-7,-4,-3,7,4,4,4,-10,6,-3,-3,3,3,7,9,-8,10,-1,2,8,-9,9,8,-6,-7,9,1,5,1,-5,-1,5,5,-8,-3,-3,9,-6,1,1,10,-9,2,-4,7,-1,2,-2,3,-4,-6,-9,-8,4,-6,9,-7,-8,4,1,-1,10,10,2,1,4,-2,-6,7,-4,-7,10,3,2,-9,-7,-5,6,8,-3,-4,8,-9,8,4,-10,5,4,9,3,9,10,6,1,4,3,-8,-5,5,2,5,2,-1,8,-2,-10,3,-5,6,7,8,9,2,3,-7,-9,-7,4,7,10,5,2,-1,-10,-3,-8,-6,-6,-1,6,-6,-10,-7,-10,6,-4,1,-10,-3,9,7,6,4,-4,3,-1,-6,-1,-5,5,-5,2,-7,8,5,5,-7,-7,-4,-6,-10,7,9,-9,1,6,7,3,4,-3,1,3,8,8,3,-1,10,1,6,-4,7,4,-9,5,8,-2,-7,-6,-7,9,10,-4,-7,-2,6,1,-5,5,-4,7,10,3,-4,-2,-3,10,-10,4,9,10,1,9,10,1,-6,-6,-8,4,7,-3,-7,-6,9,-4,-7,4,-8,5,6,-4,4,9,-8,-4,-10,-7,-1,-6,4,-7,-6,8,-5,-4,9,-5,9,-5,-10,-3,-5,1,-5,6,-9,-2,-5,1,-3,5,4,-5,6,9,8,-8,4,10,-6,-1,-9,-2,-1,-6,-9,-8,-3,-5,4,6,-5,8,-4,9,3,9,-2,8,-1,10,7,2,-3,-8,-10,-1,-1,-6,-5,8,-4,-4,5,10,8,7,-9,5,5,-7,10,-2,6,7,-3,-1,-2,-5,-7,-5,6,10,1,5,1,-5,-1,3,2,-1,6,4,-9,5,4,10,-1,3,-6,-10,-2,9,1,-1,5,-10,5,9,2,9,3,6,-10,8,7,6,-2,-3,8,-5,-7,3,10,-6,-5,8,6,4,3,5,-9,-1,5,-3,1,5,-5,-2,10,7,4,-5,-1,8,2,-6,-4,3,3,2,6,-2,6,7,-3,-1,-2,-7,9,7,-1,-2,1,6,-1,-10,8,9,-5,9,-1,-4,9,3,1,9,4,8,-9,1,-3,-7,2,-4,-10,-6,-3,3,-4,-2,-8,-6,4,-10,-8,-3,2,1,-5,1,-10,-8,9,-7,-8,7,-1,2,9,-8,-3,-10,-10,10,-8,1,-10,-10,-10,2,-7,-6,4,-6,10,-9,-5,-1,-10,10,-2,7,-2,10,6,-10,1,-3,-3,-5,3,9,5,-4,-9,-4,-7,-2,7,-1,-2,-6,-8,-7,10,-6,-7,2,3,6,2,2,10,10,-3,-10,3,-9,5,-2,7,-7,-2,-6,-6,-6,2,-10,1,-10,3,3,-6,-9,-6,7,10,10,4,7,-8,-10,1,5,-2,-8,6,2,-4,4,-3,-5,-6,5,1,-2,4,-1,2,9,-2,-10,10,10,-5,4,-5,1,6,-1,-5,-7,-5,-6,-6,-2,3,7,-5,7,-3,-8,-4,2,-2,-8,-8,-9,-3,1,-1,-8,-6,-10,-3,-1,-10,7,-7,-3,-3,-7,5,-3,1,6,8,6,10,-7,3,-9,8,-8,-8,3,3,2,5,4,1,8,5,-5,2,-8,-1,-9,-5,-1,7,4,-3,-7,4,-4,3,-6,6,5,-5,-2,-10,-5,-7,9,10,3,2,2,3,-4,-8,7,4,-3,-3,-5,-7,9,7,-7,3,-2,3,-2,-2,3,7,-7,9,9,-6,-6,-5,6,-5,8,-4,-5,-6,3,5,7,3,-2,3,-6,-8,-1,-7,4,9,-10,-4,-2,-1,-8,1,6,-9,-6,-4,3,-5,4,9,-2,3,3,-4,-8,10,-1,3,-2,-8,7,3,3,-2,7,-6,-10,-2,6,8,1,2,-6,9,-9,8,-10,-6,6,9,-1,-4,-6,6,2,-8,1,-7,6,6,-5,-1,-5,10,-7,7,-6,9,-9,5,-8,-6,-4,-5,-9,4,-5,-2,2,-4,-1,-6,-5,-10,-1,-6,8,7,5,10,5,1,-1,-10,3,1,-6,2,2,-6,6,2,-3,6,3,1,4,-5,5,7,1,1,-2,1,-6,7,-6,-6,7,7,1,-5,-10,-9,8,-2,-3,8,-7,-1,5,-4,4,2,-5,-9,-6,1,-7,-2,8,5,10,-7,2,9,6,10,7,-1,-10,-9,5,6,-2,-8,-4,-2,-6,-1,-8,8,6,-4,-8,7,5,6,-8,3,-1,-2,2,7,-4,-6,9,-6,2,1,-5,9,6,2,-8,-6,4,1,-4,3,9,2,-5,-4,-10,-8,5,5,-5,-5,-1,-9,1,-10,10,-4,-7,6,5,-1,-7,10,-8,-3,-3,5,1,9,-6,8,-4,-3,-7,3,1,6,2,-9,-2,-5,-1,7,6,4,6,-8,-4,-9,9,2,-5,7,-6,-10,-1,1,9,3,-5,7,-1,-2,-5,-4,5,6,8,-9,-2,-1,6,-4,-2,-10,6,-8,2,1,-3,2,3,-7,-1,-5,5,-7,-8,8,10,8,-7,4,-8,-7,-10,-8,8,5,-4,-4,6,2,2,5,9,-9,-10,6,-10,9,-3,-4,-6,2,-1,9,-10,1,-2,-6,-10,5,-2,7,5,1,-7,-9,-5,-3,9,-4,-2,5,-3,-2,7,-2,10,10,-7,3,7,-7,7,9,-9,-7,7,-4,2,-3,5,10,5,3,3,4,-2,-4,-10,-4,-3,-9,-2,3,8,3,-9,1,6,-4,1,-1,-10,9,6,-8,-4,-1,1,-10,-10,-4,-9,3,-10,4,-8,4,8,9,-9,-4,5,1,1,-4,-6,10,-3,9,-1,-7,-6,8,-6,-9,-3,10,-8,3,-4,-10,5,-4,-4,-4,-5,-5,-1,6,-9,4,6,1,7,-5,1,1,-7,8,7,-8,2,3,6,3,-4,9,-3,6,-4,-2,8,5,-8,9,-5,-6,-2,-2,-10,-6,-4,-6,7,10,5,-8,-5,10,-6,-9,-8,7,5,8,6,2,9,8,10,-9,10,-9,10,2,-8,8,7,-6,7,-10,8,-5,-9,-2,1,-5,-9,-7,4,9,-10,8,4,-2,7,-4,-3,1,1,3,7,2,2,6,-1,-8,2,10,1,7,-3,3,1,2,-9,4,4,-1,9,2,4,5,-7,4,-9,6,-1,10,4,5,-6,7,-7,6,-8,8,-10,10,7,7,-4,-8,3,8,-1,-9,2,-8,-6,4,5,-8,4,4,3,-7,-4,1,-4,-3,3,-1,9,3,4,-1,-9,3,8,-7,9,-7,1,-10,-10,10,-8,6,10,3,9,4,5,-3,7,4,-6,-8,-1,-3,-5,2,-6,9,10,-2,7,6,3,5,-1,-5,9,3,-6,-1,-9,-4,-3,-3,-6,3,2,5,1,7,-8,9,10,9,6,6,-5,4,-3,3,3,5,9,5,10,2,-6,9,-10,-1,8,-6,6,-3,7,10,-3,-7,3,-2,4,4,4,-6,-2,5,-4,3,10,-9,-1,7,4,-4,-6,1,-10,-9,-8,1,4,10,-4,8,-8,-1,7,-2,-3,-7,5,-8,5,-9,4,3,-3,-4,5,-3,8,-1,-3,6,-1,3,-1,1,8,-8,-10,-10,3,4,-5,-10,-10,-10,8,-8,-8,-7,2,2,-9,-4,-1,-4,10,2,-4,10,7,-6,5,4,-5,-2,-10,-10,-5,6,9,-8,-7,-4,-3,4,6,5,-5,7,-1,-10,-1,9,-3,2,6,-2,-10,-3,-1,-5,8,10,-10,-7,4,-3,6,-3,-7,-4,4,-6,-2,-9,6,2,5,-1,-9,-7,6,7,10,-2,4,-9,-1,5,4,10,8,-5,-4,-8,-5,-5,5,-2,4,3,1,8,-7,-7,7,-10,-9,-7,-3,5,2,-10,2,1,7,5,5,10,-6,-2,6,9,-9,8,3,-2,5,-1,6,-4,7,-1,-3,-4,-9,2,-8,-3,-7,-1,-6,5,-4,10,-10,3,2,-10,4,-3,-10,-10,-6,-5,4,5,-8,-3,9,-4,-6,8,10,4,-2,9,-2,10,2,10,3,9,-8,-8,6,7,9,-1,-3,-5,9,-7,-2,8,-6,3,-6,5,-3,-2,-4,-10,-6,4,-3,6,-2,3,-2,10,-1,-9,3,2,4,-6,5,-3,-6,-2,-3,-3,1,-1,-8,3,3,-8,-6,6,-4,-2,8,-10,10,7,10,10,-7,6,-1,-9,-3,-3,-7,2,-9,8,8,4,-2,3,3,3,2,7,8,-8,-3,1,9,-9,8,8,9,-3,-4,-1,8,7,3,5,-10,-6,5,-2,1,-5,-1,4,-6,9,1,-7,5,-1,7,-4,1,1,5,10,-5,6,7,-5,5,3,7,-7,5,3,-5,1,4,2,5,9,9,5,-3,9,6,8,-3,8,-2,-1,7,-5,-4,-2,10,-9,7,5,6,-10,7,8,2,7,6,-2,-2,3,3,4,-7,10,-9,-5,-8,-9,-2,4,-2,9,1,-8,8,8,9,5,-7,9,10,10,9,-3,-4,-5,10,-4,-5,5,-6,-5,4,-10,-4,6,-4,-4,-4,6,-5,-6,-6,9,5,-5,6,-5,-9,-1,5,-7,-4,4,1,7,2,3,4,-7,6,9,1,4,10,-3,3,-5,-2,-4,-8,8,-6,8,-5,-10,-9,4,-2,10,-4,-8,2,3,-2,-6,1,2,7,7,5,4,6,-3,-4,2,-5,-4,-2,10,7,-6,-2,-4,-8,-2,8,-8,3,5,-4,7,5,-4,-10,3,-2,6,5,4,2,-8,-1,-5,6,4,-6,9,2,-8,-2,2,10,-10,9,-10,-10,-3,3,-7,-9,10,2,7,-7,-10,8,2,1,2,-6,3,1,8,6,-4,8,8,-5,6,10,10,-8,-5,-4,1,9,5,1,-3,-1,-2,3,9,-5,-10,8,4,-4,-5,7,-6,1,8,7,9,-8,-8,-10,-9,-1,1,-10,-7,5,-1,-9,1,-10,-2,-10,-6,-1,-9,1,-8,-8,-4,-6,-3,5,5,4,-4,5,-3,8,-1,-4,-1,-8,-1,-10,5,6,-10,5,-4,1,3,-5,-9,6,1,-10,-8,3,-7,4,2,-1,2,-6,-2,6,1,2,2,1,7,-10,-2,-4,-10,10,-2,-2,6,3,-7,5,-8,-7,2,-8,1,-6,2,1,-2,-4,3,-9,6,-7,10,-10,-7,-3,-6,2,10,10,1,6,2,8,-5,-4,-8,3,-3,10,-9,2,3,-3,-3,-7,-4,-8,2,-2,2,8,-9,1,4,-3,-2,10,-9,10,-6,8,1,-6,3,-10,6,-8,8,6,-1,-5,-1,10,-8,6,1,-3,2,-5,-9,-2,2,-9,-1,2,-3,-5,-2,6,9,-3,8,3,7,-6,3,-3,-10,-5,7,-3,4,5,-4,5,7,-6,-4,-4,6,-7,-8,4,-3,8,-6,-10,-8,-6,10,-8,7,-9,-2,2,-2,7,-9,9,9,10,6,-6,7,-9,-3,-3,2,1,-6,3,4,-10,-2,3,-6,-9,-2,-9,8,7,8,2,-3,-5,8,9,-10,2,-9,5,7,10,-10,-10,10,10,7,-7,6,9,9,-5,8,1,2,3,-10,9,-3,-2,8,10,-5,8,-8,-3,-7,-6,-6,4,-2,7,1,6,7,-6,10,-2,2,4,9,9,-8,2,-3,-3,-7,-1,-8,-4,-4,2,8,-9,-6,-10,-2,4,5,7,-4,3,1,-10,10,4,4,-10,-1,-3,-1,3,-4,-7,-3,-5,5,10,3,-4,4,8,5,-2,-4,3,-10,1,3,10,-2,-7,-4,-10,-5,-9,4,8,-5,4,-5,-5,5,-8,-5,6,-5,2,-10,-8,9,-5,-7,10,3,-1,3,7,3,-8,-4,-4,9,-10,-10,-3,8,-2,1,6,10,-6,3,-10,-9,-5,-5,3,6,-3,4,7,-4,-4,5,-10,-7,-7,-10,-7,7,3,2,6,-9,-8,2,2,6,-2,-8,-5,1,-3,9,1,3,-8,7,-3,-10,9,6,-8,1,-5,-2,-2,-2,-5,7,7,-7,-5,6,3,10,-7,-7,-9,7,-5,-4,-4,-6,-7,5,4,-6,8,-8,-7,-5,3,3,10,7,1,-6,10,-3,6,-1,-2,9,1,3,6,-4,1,2,-7,7,-4,2,7,-1,5,-3,-8,-7,2,9,-7,6,2,9,10,-7,1,8,-9,10,2,-3,8,1,1,7,-5,-7,-4,6,4,-8,-5,4,-7,9,8,2,-3,7,5,3,-8,6,-9,-5,6,-10,2,-6,-8,10,9,3,5,8,-5,-1,-1,6,9,-3,-7,-7,-6,-7,8,-10,1,8,5,-7,7,5,5,10,-3,9,5,-8,-7,-5,4,3,-1,3,-9,6,8,-5,-3,7,9,5,-9,5,7,4,-5,9,10,-2,4,-4,-9,5,8,-7,5,-9,4,4,-3,-7,3,-6,9,1,-6,-6,-8,9,3,10,-8,4,-4,5,5,10,7,-3,4,10,1,-8,-6,-4,3,-7,-5,-4,9,10,1,-4,-6,7,-2,-1,-10,1,-6,-3,1,9,-2,8,-2,5,-8,4,-5,5,5,-10,7,-2,-8,-1,6,-6,-4,-8,-3,-4,4,-7,6,-8,-10,-9,-2,1,6,9,-5,-10,9,7,-3,-3,8,7,1,-6,-4,1,6,5,5,5,9,9,7,8,-9,-8,10,-1,-1,-4,-4,10,-9,5,7,2,-7,-1,-8,-6,-1,-2,-10,-2,3,-5,-2,-8,-7,5,-5,9,-7,-8,-1,-2,9,-3,-10,-9,2,-10,8,-7,5,9,8,-3,10,2,8,-6,-1,-7,6,3,-1,-4,5,3,3,9,10,8,5,-3,-5,9,10,4,5,3,2,-4,9,6,-1,-3,7,3,9,-5,7,-10,-2,-2,-4,3,-2,-5,-6,3,8,-10,-5,-8,-1,1,-9,-6,7,-7,2,-9,9,-7,4,4,-6,-6,-7,9,7,3,-3,6,6,-1,5,7,5,-9,-4,1,-7,-4,3,-10,5,8,-4,-8,-8,-3,2,-9,3,-3,2,8,-5,2,6,-10,-7,9,-1,-4,-9,-3,4,-5,1,6,4,-1,-6,6,-6,3,3,7,-2,-6,-7,-9,3,9,-3,-7,7,-5,2,-7,10,-6,-3,-8,3,5,2,-2,-7,9,6,-7,4,7,5,-8,5,7,-4,-2,-8,-10,10,-9,5,-7,6,5,5,-7,8,-7,-7,1,-1,2,-10,2,-4,-9,1,-7,9,6,-6,6,6,4,-10,-9,-8,10,3,9,5,4,3,10,5,-6,8,-4,-7,-2,-3,-8,9,-2,2,-10,1,-4,9,-6,1,-5,6,-3,-8,-10,5,-4,7,-7,-7,-9,-2,3,-6,-6,-1,-4,-2,9,-4,-3,-10,3,2,8,8,-10,-8,-4,3,1,-4,-10,4,8,-10,-6,9,8,1,3,-3,2,7,8,-7,-6,6,7,7,9,-6,8,4,7,3,-5,-4,-10,2,-2,6,7,-4,-1,10,8,5,-3,5,-4,-3,-7,-5,-9,6,5,-1,-4,-7,-6,7,4,2,-2,-1,-7,5,-1,-2,7,-4,-10,5,10,10,-10,1,-2,-5,-2,-1,9,3,-8,10,1,-10,-9,-6,6,8,-7,-1,-4,1,1,6,-8,1,4,-3,-7,7,-5,-6,10,-8,5,-4,-8,-4,7,-10,-9,-2,2,7,6,7,8,6,-9,3,-8,2,1,4,6,-2,-4,-9,10,8,-1,-1,10,4,-6,3,3,-7,-1,-10,-4,3,9,-6,7,6,1,-6,-7,-10,7,-6,-7,3,-3,-5,9,6,-10,-6,-8,-5,-4,-10,1,-5,-3,7,3,10,-4,4,2,1,2,-1,4,7,-6,10,-9,6,-3,4,4,1,-8,3,-4,-4,-4,5,10,5,-3,3,-9,3,-1,-9,10,5,4,10,2,4,-8,3,3,3,-2,-7,5,-4,-7,-1,2,7,-4,6,10,10,-1,7,3,-1,6,8,9,10,-5,-5,9,-7,-10,8,6,-9,3,2,-5,10,10,5,-10,-7,7,5,3,-8,-8,-4,-6,-9,8,4,-4,-5,2,6,-4,-10,5,7,-9,3,-1,10,-10,6,-10,-1,5,-3,-5,-1,-1,2,-6,6,-3,-1,-5,-4,9,3,2,-8,-2,-4,-9,8,5,6,8,-5,10,-7,-8,-10,-3,-8,8,2,6,-9,-10,-3,-8,4,-2,6,8,6,6,-5,-8,-4,1,-8,-1,-10,-3,-5,3,-6,-2,-6,10,6,-8,7,-4,-4,-8,-1,-9,-9,3,3,3,2,6,6,2,9,3,-7,8,3,4,-2,-3,7,-5,4,2,5,-6,1,3,9,8,2,-9,-2,6,-8,-7,7,-5,-1,-8,6,-5,5,9,-3,-2,-4,9,4,2,-6,-8,2,-5,2,-7,-1,-7,2,10,6,-8,3,-8,5,-10,10,6,-1,3,6,4,-4,-6,9,-10,10,-5,7,1,-5,5,-10,5,3,9,-10,9,-5,10,10,9,10,-2,-9,-3,7,10,-10,-1,7,-2,-2,-10,-3,1,2,3,5,-1,10,1,-1,-5,7,3,5,-10,-6,5,3,-5,7,-7,3,7,9,1,8,-10,-9,1,-8,-2,-1,4,-5,7,6,6,-1,3,10,1,-7,7,3,1,-8,6,1,3,8,10,3,3,9,-5,9,1,6,3,5,-3,-8,2,8,7,-5,-9,-3,4,10,10,-5,7,-8,-3,8,-6,4,8,-3,-7,4,-9,-2,-8,2,4,-9,-1,3,10,9,-10,3,-6,-6,5,10,-6,6,-5,-2,-8,-1,-7,-4,-8,2,7,-7,-2,-7,-3,-10,1,3,-6,6,3,2,2,7,-10,-5,2,1,4,-10,5,6,-6,2,1,6,5,-5,6,4,-9,-5,2,-5,-4,-3,-5,-4,7,2,6,-3,-8,6,8,-1,1,-8,-2,9,-9,4,1,-4,-6,8,4,2,10,5,-10,-5,-4,1,-9,1,-5,2,7,-6,-10,-6,4,8,8,1,2,8,-10,-10,-1,7,-10,-2,4,-1,-10,1,-8,9,-2,3,-8,-8,10,-9,2,7,-4,-10,-6,-5,9,4,4,-3,-6,8,7,-4,5,2,-1,1,9,-6,-4,3,6,1,5,-4,-2,6,-10,10,4,-5,10,-2,7,4,-8,7,6,-2,3,1,10,-7,-8,8,-7,-8,-2,4,10,-3,4,-2,7,3,-2,5,10,2,7,9,-6,-2,7,8,-5,6,10,-2,-2,4,9,-5,9,6,-9,1,4,-6,9,-10,6,6,4,10,2,9,3,-10,-3,-10,5,-10,5,2,1,-10,8,2,3,9,5,-5,-3,-1,-3,-9,-2,-7,-6,-3,-1,-5,-9,10,-8,-5,8,-3,7,5,5,-10,4,6,-6,-10,-1,7,-1,-2,-7,-6,-9,4,-3,9,5,-8,7,-3,-2,2,-8,-5,-6,-10,4,-8,4,-10,-2,-6,-6,-10,-8,-8,3,-6,-10,10,6,9,-5,-4,8,8,10,-9,-10,-3,-1,9,-2,-5,-3,-6,-6,-10,1,-1,-7,1,3,-8,-10,-1,2,4,-4,6,-5,-10,-9,-1,-6,1,1,3,-3,-7,1,-3,10,9,-8,3,7,-6,6,9,10,-7,4,-5,2,2,-1,-8,-4,-7,2,-8,5,-5,3,-5,4,4,-4,4,2,-1,1,-4,-8,9,-10,9,3,8,-8,9,-5,-1,-1,-6,1,5,-1,-8,1,1,6,-9,-5,-7,10,-6,-8,-5,-2,-3,10,-6,1,2,-1,3,2,-8,-9,-10,10,5,5,-8,-10,-1,-3,3,-10,3,-5,-9,-10,-4,2,9,1,10,1,4,-3,4,-1,7,2,-3,8,-4,10,9,-3,4,10,10,5,7,-9,1,9,-1,10,10,7,8,1,9,-6,7,-8,1,3,1,-10,1,-10,2,8,10,5,3,7,-9,-5,-1,5,8,10,1,-2,1,7,-4,5,-10,-3,-6,5,3,4,-4,-6,9,2,9,-2,-7,-6,-6,6,1,1,8,-5,-5,-5,-7,1,-10,-6,10,9,-1,-8,-4,-4,-4,4,-8,-4,-9,-4,-1,-2,10,8,-10,-9,2,7,-4,2,-6,9,-9,-9,-2,-5,-7,-4,7,-9,10,7,5,-9,4,6,-2,-6,-8,7,7,2,1,3,9,4,-1,-3,-4,7,6,10,8,6,2,-3,7,6,-3,-5,-2,6,-9,-2,-1,-5,-10,-4,-2,2,4,-4,3,9,9,-10,3,6,5,9,5,-5,-8,3,9,-3,-5,6,-6,-5,8,-8,1,5,10,-6,-7,-9,-1,-2,-2,-7,-3,-2,-9,4,4,10,-3,-3,-10,-9,-1,-1,-3,-5,9,1,-5,1,-1,3,6,-1,10,-4,-5,7,-3,8,-3,-2,-5,4,-5,-5,-9,-10,-4,6,6,-4,2,7,-2,-3,8,-9,6,6,-10,8,1,-6,8,9,-1,3,6,1,4,5,9,8,7,7,-5,9,-2,9,7,3,4,-5,7,10,-2,-7,9,8,-7,5,9,-6,-9,2,6,7,-3,-10,-10,4,-5,5,-4,2,-8,-3,-1,10,5,-7,9,-9,-6,-5,-9,-10,-9,8,8,7,7,4,1,9,8,-7,9,9,6,4,2,2,3,-7,2,-8,5,8,-8,10,-10,-10,4,6,3,7,-6,-9,9,-9,-9,1,-8,8,5,-1,6,5,3,3,-3,-5,9,7,9,8,-4,-2,9,10,1,-10,5,8,-7,7,-1,-9,4,8,-6,1,-7,-2,-6,-10,-6,-5,-6,-10,-6,-4,-7,7,3,-5,2,-6,-3,-7,5,-8,-8,1,-6,10,5,-8,9,4,-1,-10,8,-3,-6,-2,6,1,2,1,-10,9,6,-10,5,8,4,8,-4,5,-9,-3,8,10,-6,8,-1,3,-6,-4,-6,6,10,4,-3,6,-7,-9,-2,4,2,-4,-1,-2,-10,10,9,-6,10,-1,-10,-6,-5,-1,-4,3,-7,8,-5,-4,7,1,-8,2,-10,2,1,6,-1,-3,1,2,4,-3,10,-6,-9,-2,-7,-6,9,-6,4,-8,-8,-3,-6,5,2,-1,-3,-1,5,3,10,-8,7,-1,5,-7,10,-1,2,-8,-4,-1,7,1,-5,-3,-4,-6,-4,-2,-8,-1,-1,-5,-8,9,4,-9,2,-3,4,4,7,-9,-6,-2,-1,3,5,5,10,3,6,7,4,6,5,8,-9,5,-7,2,-9,-2,-2,8,-2,8,-7,-9,6,-8,7,-5,2,-4,8,-1,-2,3,-9,-7,-6,-1,1,-3,-7,-8,-7,-1,-4,10,-4,8,3,9,6,2,-1,4,-5,9,-8,-6,-9,-5,-3,-4,7,10,-5,1,5,3,8,-9,4,7,-6,-8,8,-9,-2,8,7,9,-7,3,-4,9,6,7,6,4,4,9,7,5,-1,9,10,-9,-8,10,-1,-6,-5,-8,6,4,-4,-4,-9,2,-1,-7,9,-8,8,-9,-5,7,7,-2,5,-4,9,2,6,-9,5,6,1,10,-1,8,3,5,-9,2,-7,5,-4,-5,10,-7,-1,8,-6,9,7,-3,-5,10,-7,9,1,-9,2,-7,-9,7,5,2,-6,-9,10,-3,10,8,8,-3,-1,5,-8,6,-5,9,-10,3,2,9,6,7,-5,-5,-10,3,-3,-7,-1,10,7,7,-2,3,6,8,-2,-8,-9,10,-3,3,1,7,-2,-7,-10,-6,7,-10,1,-3,-4,10,5,-5,4,4,-9,-7,-2,1,9,6,-7,8,-4,-3,-3,-2,-6,9,-4,-7,-8,3,1,3,1,7,-4,8,-8,-6,5,-1,2,10,7,-8,-2,-8,-5,2,-8,6,5,-2,8,-4,-6,1,-9,6,8,4,7,2,10,-7,-4,2,10,2,4,8,-5,9,-4,1,-1,4,6,9,2,6,-1,-9,4,9,-9,7,-10,7,5,5,-4,3,7,-4,10,-6,8,-3,7,10,3,-10,-6,-6,-7,-9,2,-9,-6,7,-4,-8,-8,-7,-5,3,-6,2,9,5,10,7,5,-2,-10,6,2,8,-7,9,2,1,-4,-10,-10,9,8,-4,1,-6,5,-6,-8,-10,-9,-6,-10,9,-7,-7,5,-8,3,7,-10,-6,5,-5,-6,7,-4,8,-9,8,-9,4,2,-8,8,8,8,-4,-5,7,5,-9,-6,-5,-6,-2,9,-9,-2,3,-4,-7,-4,-7,-1,10,-10,-5,6,3,2,-6,-5,-9,4,4,-2,2,3,4,-6,10,-3,-4,4,10,-7,8,-3,-7,-10,7,-4,-9,-8,5,-7,-2,1,-9,7,4,8,-4,-8,8,-5,-1,3,10,-2,7,-9,2,-7,6,2,8,9,-9,-4,-4,-3,10,6,7,-4,-9,-5,2,4,8,5,6,-7,-2,5,3,-2,1,-2,5,-5,6,5,-4,5,7,-9,5,-1,8,-2,1,4,9,-2,-4,9,7,-8,-5,6,-5,8,-10,7,-4,-10,3,6,-2,6,-5,5,-1,6,8,-9,-4,4,-5,-3,2,-3,-7,-8,-9,-4,1,10,-2,7,8,-4,-4,-8,1,-9,5,7,3,1,-2,-8,-2,-3,5,-6,-8,7,3,3,7,7,4,-3,1,-10,-9,-4,-5,7,10,2,6,-2,-5,2,-8,5,5,10,-2,-9,-7,1,-3,-3,-4,1,-4,-10,9,-2,-3,9,-7,-5,7,9,10,-7,10,6,-5,-3,-9,10,5,4,-9,9,2,-4,-10,3,6,-5,-10,-10,7,5,-8,-5,-7,2,-2,1,-5,-2,-1,-8,-9,-1,1,5,7,-5,5,10,9,-7,3,6,4,-6,7,9,-5,4,-6,-6,-8,-9,-1,4,-1,2,8,3,-7,8,4,-1,-10,7,-5,10,-3,8,-6,-3,-3,2,-4,5,5,-7,-3,-8,-5,-10,9,4,8,6,-2,10,8,9,8,-5,-9,2,3,6,4,-6,5,4,2,9,3,-1,3,2,4,-4,10,-7,-5,-10,-1,1,6,1,-7,2,-10,-10,-3,-4,-10,1,2,4,3,8,2,-9,-7,8,1,-6,3,3,8,4,-4,9,-7,5,9,-3,5,9,4,-7,-7,5,-9,-9,-6,7,10,-7,-1,6,-8,-10,2,-4,-9,9,-4,-10,-3,-1,2,10,-6,-10,1,-6,4,3,-9,2,10,6,8,-10,-2,1,-9,-5,-7,-1,-10,1,-4,2,3,-1,-7,-10,10,-7,1,6,8,4,-8,-6,-1,-4,1,-8,10,-1,4,-2,-1,7,-7,-1,-4,-10,9,1,-3,7,-1,-8,4,-9,-1,3,2,-4,-2,-5,2,-1,3,3,6,-10,6,-1,-7,9,3,-2,3,-7,-2,3,2,-7,5,1,-1,-10,10,9,4,-7,-3,4,-6,-1,5,-2,-6,-2,-10,-4,-5,-2,-8,2,1,8,8,-8,-5,3,-2,7,-8,1,-3,1,-1,-10,-1,10,-4,6,4,-6,-4,1,8,6,-8,-1,3,-6,4,5,10,9,-6,6,10,1,3,-10,9,-6,-4,-5,-9,-3,-8,-10,4,4,4,-1,2,-10,3,7,-7,-8,-9,10,-5,3,-1,-4,2,-6,10,5,-9,-8,-3,4,-7,3,-5,-6,-5,-6,1,3,9,-4,-7,10,1,8,-4,-6,-3,9,-1,10,3,6,5,-9,-7,1,1,-9,1,10,10,-8,-6,-2,-9,5,-6,6,-10,-6,-10,-2,10,3,9,-9,-9,1,-4,-4,-5,5,-10,5,-7,-7,-7,8,-10,-1,6,9,6,1,-5,3,4,3,10,-5,8,4,3,-5,4,-4,-5,-6,-5,1,3,-1,-1,-2,4,-9,-1,8,-6,-9,-10,-1,-7,5,3,9,-1,5,-5,-4,6,1,-6,-1,5,-3,4,9,-10,-1,-2,2,-3,5,4,8,3,-5,-10,3,10,-10,1,-4,-4,7,9,1,-4,1,8,-8,-1,-1,-1,8,-10,6,8,4,6,9,-1,-7,-9,-5,-10,-7,7,-1,10,-10,8,4,7,-7,1,10,8,-1,8,1,8,-8,-4,5,-6,6,2,-9,10,-4,2,7,1,-5,3,-6,4,7,-3,-3,7,3,1,-8,8,4,-6,-1,8,-8,4,3,10,-9,4,1,1,-1,-8,3,-1,-7,9,-3,-6,7,5,-1,2,7,9,-7,4,5,9,9,7,8,-5,-1,2,-4,-10,3,2,7,-7,-4,-4,-2,-6,-2,6,9,1,-4,-9,-1,3,2,3,9,-6,9,-3,-3,-2,4,-5,1,2,-8,-6,-2,4,-6,-5,-6,-9,1,8,3,-6,-9,-7,-6,10,1,-4,4,-7,6,-5,-1,9,-6,-5,-8,5,2,10,2,4,3,-6,-8,9,-3,8,9,-7,4,-4,-2,10,1,-4,9,8,-7,-10,5,1,-4,-5,6,-7,-3,5,-2,-9,-4,-7,10,4,8,-4,-5,-5,6,1,-2,-2,-1,-10,3,-7,-4,-9,-8,6,1,10,-5,-5,5,-2,-6,3,3,-2,7,-1,-2,9,-7,7,-3,4,-4,-8,6,-9,6,2,7,4,-5,-5,9,-8,-9,6,4,1,-10,-8,-10,-1,-8,6,8,9,4,10,-10,-10,5,-2,-6,8,3,-4,-4,-1,-7,8,-4,-9,-3,-4,1,-1,-9,-5,7,5,-1,4,2,-10,2,-6,-4,-7,-6,-1,6,-3,-6,-2,-4,-4,-5,-10,4,8,7,4,-9,-2,3,-3,-5,4,5,-6,-4,-3,9,-8,5,-2,-9,6,7,-4,9,-9,-6,-10,10,9,6,-3,-7,-1,6,-7,-10,-5,-10,9,-8,6,1,4,-1,5,7,4,8,8,-9,-9,7,7,-2,-7,-5,4,-10,-5,-3,8,-8,-6,10,-2,-1,7,6,-5,10,-1,-6,9,5,-7,-6,-8,7,-5,-8,-5,10,6,8,4,-5,3,2,-7,9,3,1,4,-5,-5,5,-9,6,9,-7,3,10,5,-1,-8,8,-6,5,7,8,-1,3,-8,-7,4,1,-8,-5,-4,-5,7,-6,-10,-4,8,-8,4,3,2,-10,6,4,-4,-6,5,3,-5,-4,7,-4,9,6,-5,7,8,4,9,-9,8,3,7,7,2,-8,1,-8,4,-6,-4,8,10,-8,-1,2,-2,-5,1,-2,-3,-6,4,7,-7,-9,-5,2,9,4,7,-1,3,10,8,-8,4,-7,5,6,-6,2,-2,-9,-4,-2,1,10,9,-9,-1,10,-3,4,1,-2,5,-10,-8,-9,-2,-3,-4,8,-2,2,3,1,-9,4,4,-8,-9,5,1,-8,-7,-7,-4,6,-9,-3,8,-8,8,-8,-9,-1,-9,4,2,-3,2,10,3,6,-4,-6,-3,-9,8,3,-6,-6,1,-2,-1,-2,5,1,-9,1,3,6,-4,9,6,9,-6,-6,-4,-10,5,8,-5,7,-3,9,-6,4,-4,1,-4,-2,7,7,-6,6,10,-1,-10,-1,7,-1,-5,-2,-5,-8,5,-9,-6,4,5,5,-4,10,-9,7,1,10,2,-4,6,7,-2,4,5,1,-7,-5,7,5,6,-1,-1,-2,2,9,10,7,-2,-9,10,9,8,-10,-1,10,-8,-4,-1,-9,6,9,2,7,9,-5,8,8,-7,-3,-1,6,6,-8,10,-10,-3,-4,6,-3,9,-6,1,5,10,6,4,3,-4,7,-8,10,-3,-8,-6,-6,8,-4,-7,7,-8,1,7,-2,-6,-6,-3,8,1,-8,7,-3,-7,-6,-5,-2,-7,7,-8,6,-9,10,9,9,-4,-8,-1,7,-8,-10,7,-8,-6,10,-5,10,7,5,10,5,-10,-6,-5,-1,-8,-8,5,-1,2,-5,-6,-2,-6,8,-2,9,-7,5,10,5,-8,-4,8,2,-5,-8,1,-5,-6,3,5,9,9,-3,1,10,10,10,1,7,-10,-8,-2,10,-5,5,-6,-3,-10,7,-6,-1,-1,4,5,-10,6,-6,9,8,8,4,-8,1,5,7,5,10,9,9,-5,8,5,2,9,-9,-1,-1,2,-7,9,10,4,-9,-2,-8,7,10,10,-5,-2,-6,-7,-4,-6,-8,4,9,6,2,6,8,-6,5,-2,2,7,7,-4,5,-1,-7,8,5,-3,5,7,-3,2,8,8,-8,-8,9,7,2,-6,4,-4,-10,-8,-6,-10,7,-7,-8,4,10,-2,-6,4,6,8,3,-9,-6,-2,1,1,4,4,5,-7,-2,5,-5,-7,-10,-10,-4,8,5,4,1,-3,-7,6,-5,-6,-9,4,-3,-6,-5,-6,5,-10,-5,4,4,-1,-4,-3,-10,-7,-2,-5,-3,6,7,-6,-7,3,-5,-9,6,-9,7,-1,-1,-5,3,-7,-3,4,-6,-2,-1,6,4,4,-5,2,5,10,4,-8,-7,5,10,10,2,-9,-9,-10,2,4,-8,-1,10,10,7,4,5,-2,9,-10,-5,5,-8,8,-8,7,-9,-1,-10,-4,3,10,7,4,5,-6,-5,-4,-5,-2,5,1,10,2,6,-6,5,-8,10,-6,-6,-5,3,-5,-2,-1,6,10,7,5,-9,2,-9,-6,-2,5,-7,10,-10,8,10,8,3,-2,-9,4,2,-1,6,-1,2,-6,-4,8,-1,-5,-6,-9,-2,-9,-9,-10,9,-3,1,-1,10,1,-4,-10,-5,-6,-10,2,-7,3,-6,-9,6,-1,-6,9,2,1,-1,10,6,9,-2,-7,3,-9,5,-5,-9,-8,-9,-2,9,6,2,7,4,5,-8,7,4,-2,1,10,6,-9,-4,-7,-2,-4,8,4,7,8,-2,7,-8,-3,-8,2,-10,10,-2,9,-9,10,-4,1,-4,7,3,-1,4,-3,8,8,-8,4,-7,-4,5,6,-8,1,6,-9,-3,-4,-4,-1,4,-2,10,-2,10,5,-10,5,8,2,-5,6,1,4,9,-10,7,-7,10,5,-5,-5,1,-5,-7,4,-9,-1,2,-8,1,6,-3,-6,-2,3,3,-4,-10,-5,7,-1,4,7,-7,9,-6,-7,-9,10,-8,-1,-2,7,-6,-1,4,9,5,-3,2,2,6,7,-6,7,1,-5,4,5,4,1,7,5,-8,4,-2,-8,-8,6,-1,6,-2,4,-2,-4,-4,-4,6,3,-10,4,3,-2,8,-3,-10,10,1,-6,5,-9,6,8,-5,-6,7,-6,-3,-1,6,-9,-4,-8,4,-10,-5,-8,2,-3,-6,-1,8,-3,-10,1,8,-4,-10,9,-8,3,-10,4,-8,9,7,-8,1,-7,6,7,-9,-10,5,3,10,9,-8,2,-2,-9,-2,4,-8,4,-9,2,2,-5,1,2,-5,-1,-4,8,-3,2,5,9,-7,1,-4,1,5,4,-5,1,-7,-4,3,-8,-10,2,-6,-1,3,-8,7,6,-7,-1,-9,2,-3,9,-10,-4,7,8,-8,8,-2,-10,-8,-10,9,7,2,-5,8,2,-1,8,2,-5,6,-2,2,7,8,-4,9,-4,1,-5,-3,6,-5,4,-2,-8,2,7,1,3,1,8,-9,10,-4,-10,4,-5,-10,-6,9,1,3,-7,-1,-8,10,-2,-10,10,9,-3,7,2,6,-10,-4,-6,10,-3,-4,5,7,-2,10,-3,3,2,3,-7,-3,-3,9,-4,-3,-2,-8,-10,4,5,5,5,-3,9,-2,-6,5,-4,1,5,-4,10,6,8,1,6,-1,-5,9,-2,-10,9,-10,-10,-8,-4,2,6,-5,7,-8,-1,5,5,9,6,8,3,-6,-10,7,-9,-9,8,9,-9,10,8,-7,1,2,5,3,-9,-10,7,4,-8,-1,8,-2,9,-8,-7,-9,3,6,-1,-6,1,-9,5,4,-8,-10,9,3,5,-4,-8,-3,-4,9,-9,6,-10,8,-10,-1,-1,5,4,-7,-1,3,4,10,-4,-5,-3,3,-6,1,5,-4,-2,4,7,6,4,7,5,8,-6,2,-2,5,6,-5,7,-7,6,-6,5,-1,3,-7,-5,8,7,-3,5,-8,3,3,-1,-8,4,-2,-5,-7,2,7,-10,1,4,-6,-3,9,-8,-5,-3,-7,-6,-7,1,9,10,3,10,-5,9,3,-6,7,7,2,-4,8,-8,-2,10,4,-9,10,-10,-6,-6,10,-3,7,-10,1,-8,3,7,6,-9,7,-5,9,-2,2,-4,-2,-1,9,10,5,-3,5,-6,-7,-9,-2,1,-8,6,1,-6,9,3,-9,9,2,-2,4,-6,-4,-7,-9,-8,9,9,-2,-2,2,-10,-8,-3,-3,-7,-7,-9,-8,-7,-3,4,-7,-2,7,1,-1,8,-9,2,-10,-10,10,7,-6,-4,7,10,10,4,-10,-9,-7,-2,10,2,-1,-8,-2,10,7,-6,4,2,-2,3,3,-2,-9,-9,-8,-10,3,-1,-10,4,7,-6,10,4,4,3,-9,10,-9,6,1,-6,3,1,10,-5,-7,-7,8,-8,-1,4,6,-8,4,-4,-10,-9,-10,8,-8,-9,3,2,1,6,1,-2,3,-5,1,-3,-2,6,5,-3,5,9,-10,-1,-1,3,-6,-2,-2,-7,-6,6,5,9,-5,2,-6,10,-2,-7,8,6,6,7,4,-2,6,-6,1,-10,10,8,3,-2,-9,-9,-10,4,-2,3,-7,-4,-5,4,10,6,-6,-5,-2,-3,5,-9,6,10,-2,-3,10,-2,10,4,-9,-9,3,-1,1,8,-7,-5,-8,-2,10,1,-5,-6,10,6,-10,-2,10,-10,9,-1,4,-3,10,7,3,9,-3,-4,7,-10,-6,10,8,-9,9,-5,-3,-9,4,-3,6,-4,9,1,9,-10,6,2,-1,2,2,-7,8,8,-2,10,4,-6,-3,6,-10,10,8,1,5,-1,3,-2,4,4,2,5,-9,7,-9,7,-9,7,-8,-7,4,-10,8,1,-3,-9,10,-2,-4,-4,-4,-4,7,-2,-2,8,9,-6,-1,8,-1,-10,10,9,-1,-6,-3,9,2,4,10,-3,-3,7,-5,9,-1,-6,-1,4,-9,6,-1,-1,-4,-10,-9,5,-1,6,-7,-1,-4,-1,1,4,6,-1,4,-1,-8,-5,3,9,-10,9,9,-8,-6,-5,-4,6,-10,-8,-8,3,1,3,7,7,6,-7,-5,-8,-1,7,-4,7,9,-8,-6,3,10,1,-7,-5,4,7,-4,-2,10,2,10,9,5,-6,-8,-8,4,-6,-8,3,-2,5,7,-2,-5,-2,6,-6,-9,-3,3,7,-1,-8,5,-2,2,-2,-5,8,1,-6,-3,9,9,3,3,1,5,4,-1,-5,-6,-5,-3,10,5,2,-2,-4,-5,5,6,-4,5,3,4,10,6,10,10,-5,8,5,-10,-3,3,-5,-1,-4,-6,-4,-4,2,-2,1,-2,7,6,2,-8,-3,2,-3,-4,1,3,-2,-2,7,5,-5,2,1,-1,-6,-7,-3,-4,3,-3,-9,10,3,4,-5,6,9,10,-8,2,-2,-2,7,-3,-5,5,-5,7,-4,-6,1,-8,3,-10,-9,-6,9,-9,-3,9,9,6,-6,9,-6,-10,10,9,4,-6,-10,-7,10,7,6,-3,-9,-10,4,4,6,-6,2,2,3,-2,-8,-3,-4,-2,-8,7,8,10,-7,-9,-10,3,-2,-9,-1,-7,-7,7,-3,-2,-8,8,-8,-5,5,-2,-10,-9,10,-7,-9,9,-9,9,-9,-2,-2,10,-1,7,-10,-2,-3,-5,1,3,-8,-5,-1,8,-7,-7,-5,1,2,1,-6,-4,-6,-10,-1,-6,-5,8,5,-8,-10,-1,9,-10,-9,-5,-6,4,8,-10,6,9,-8,1,-5,-6,-1,-10,1,3,1,-5,-7,-2,4,1,9,-3,-7,10,1,-6,5,5,6,-9,6,-5,-4,7,10,-8,-9,3,5,-9,1,3,1,-3,-5,-5,6,-5,8,8,9,-4,7,6,3,10,-1,10,-10,9,7,8,4,4,5,-10,8,-5,-5,6,-8,-2,1,1,6,7,-5,-7,-8,3,-4,10,-8,6,-7,1,-1,4,-6,-3,8,6,-5,-4,-7,-8,1,5,-4,5,3,9,-3,-6,-10,1,-9,3,3,8,-6,3,2,-1,8,10,-5,7,-3,-7,4,-3,9,8,5,2,-10,-3,2,1,-1,1,-1,4,-3,-9,10,-1,-9,-1,-3,-8,-9,-7,4,-2,10,-10,4,-5,4,-6,-5,3,4,-8,8,-1,-6,7,10,-4,-5,-3,10,-5,-3,1,8,4,8,2,-8,3,3,6,1,4,-6,-4,7,1,2,8,5,-3,-3,-9,8,-7,-1,-6,2,-6,-9,5,2,3,-9,6,-2,7,4,8,-5,4,-9,6,-10,-2,-7,-4,4,-4,8,-6,-9,-8,8,-4,1,9,-8,-1,-9,7,1,-4,-9,-9,8,-7,-10,-1,-1,1,5,-1,-7,1,-7,-4,10,-5,-6,-5,-10,3,-9,8,9,1,-9,7,7,4,6,4,5,6,2,8,-6,-1,5,-5,1,10,-10,-8,5,-3,-7,9,-6,3,-8,1,-2,-1,6,-5,5,6,2,-4,-3,10,-6,2,-7,2,-6,1,7,-6,1,-9,9,-2,9,-10,3,-4,10,-10,1,-2,5,4,9,-5,3,7,-9,-3,-4,-1,-2,5,1,8,-5,6,4,-2,-3,-3,10,8,-8,-8,-3,-9,-3,6,-10,-3,-3,-5,-2,1,-5,-2,6,-6,1,9,4,7,-4,1,-7,9,7,10,2,-5,-8,3,4,-8,-5,7,7,-7,10,5,4,7,7,-1,1,-7,2,2,-9,-1,9,6,-5,-7,2,-10,5,10,-7,10,-6,6,6,3,10,2,3,5,2,1,-3,10,2,-9,-10,8,5,3,-4,7,-2,5,-6,3,4,1,9,-7,-1,2,7,-7,-6,4,-1,-3,-9,-10,1,-4,-9,4,6,1,-10,-9,2,9,-8,-5,-3,2,9,8,5,-6,-9,-6,-4,4,-9,2,1,-9,-4,10,5,9,3,-7,-3,7,-3,-9,-10,-2,-8,-10,6,9,-4,-7,-10,6,-8,-4,-3,-5,3,-7,8,4,4,6,3,-9,-2,-7,-5,-6,5,-5,2,-7,3,10,3,-9,7,-6,1,-9,-4,-7,-9,-5,4,3,10,-3,-5,-6,8,-7,3,7,-1,-6,3,7,8,-6,-1,-8,-2,4,7,-6,-7,2,-6,-3,7,5,5,-4,3,-5,1,-5,-8,8,1,10,9,-10,-3,4,-4,-10,3,4,-3,10,4,-5,-6,-6,1,5,-8,-4,7,10,7,2,5,-5,5,-2,-3,-1,-4,-6,-5,-2,5,5,-4,-7,7,10,-7,10,-2,-3,3,-4,1,9,-10,-10,-7,-8,9,1,-7,8,7,6,-2,4,2,-2,9,-10,4,-5,2,3,1,9,-6,1,-7,-3,-5,6,-9,10,-2,7,10,-9,5,6,-8,3,-2,-7,1,-9,1,4,6,7,4,-3,6,-7,-6,9,5,-5,-8,7,-4,-6,2,2,3,5,5,-10,-2,4,-9,1,6,-3,8,-6,6,7,1,5,1,9,-10,5,-5,1,3,-8,-7,5,-10,-8,-10,-4,4,-5,3,-1,3,6,-6,-4,8,7,-4,1,-3,10,-3,6,-6,-4,-5,4,10,5,-7,-4,2,10,-6,-10,9,-4,-4,2,1,1,-1,-3,-4,-7,-7,8,6,5,-9,3,-3,-2,7,-1,10,-2,8,1,4,-7,-1,-2,4,-1,2,-3,-8,4,-9,-4,10,7,1,-1,6,-10,2,-5,1,9,9,8,7,3,-10,4,-2,9,-6,2,8,-10,8,-7,3,-2,-10,-10,-6,-4,9,-8,6,8,-8,6,4,8,-3,-1,-3,-9,-5,9,-1,8,8,2,-3,-7,-3,-7,-3,1,2,-2,-4,7,9,1,-8,1,6,3,6,-2,-5,7,6,3,1,10,-8,7,2,9,-10,7,4,7,1,10,-10,3,-7,3,-4,5,9,-1,-1,-2,-1,-9,2,4,5,7,-2,-1,-9,-9,7,-8,8,-1,10,-4,-6,-5,-8,10,-4,1,9,7,6,4,-3,-2,-2,4,6,-10,-8,1,-5,-9,7,-4,-2,8,-8,1,-5,-4,8,8,3,-8,-2,-7,7,-5,-8,3,-2,7,-5,3,5,-6,3,-9,-1,-9,6,-1,6,9,5,-3,5,6,2,2,5,2,-2,-8,8,8,-3,-6,5,2,-9,6,9,-6,1,10,-5,-6,3,-2,1,-4,-8,-3,6,-2,4,-3,-10,-6,8,-7,-10,2,6,6,-5,-2,-1,-6,2,-3,6,1,-6,6,-5,-9,-5,2,-6,-7,-7,3,-3,4,-7,-4,-5,-10,4,-7,9,7,6,5,6,-2,-10,10,4,-3,-2,-5,-3,-8,-2,-7,-10,5,2,9,-2,10,3,-7,5,-7,6,4,8,-8,6,9,10,3,4,1,-10,-5,-4,-2,-4,-5,-3,-2,10,9,-7,-3,4,10,-5,-1,-5,-10,1,-7,-2,-5,-9,6,-9,7,-5,3,-6,7,-8,-8,7,2,-1,4,1,-8,8,-2,-1,3,9,5,-10,7,-1,3,-5,7,-3,-1,10,-5,-7,5,7,-2,-5,2,-1,5,5,9,2,10,-5,-10,-4,3,-3,7,-6,4,8,-9,6,1,2,5,-8,-7,-6,7,-1,1,-1,-4,7,-8,-4,8,-1,-5,-10,6,3,-10,10,1,2,-7,-10,7,9,-6,4,-4,2,-7,10,-10,-7,-4,-2,2,8,-4,-10,-8,8,-3,8,5,-9,-4,-8,-1,-7,-3,3,2,5,-2,6,-6,-7,-7,10,-7,-6,7,-7,8,5,-2,9,2,9,10,7,2,-9,-9,10,-6,-6,2,-3,-7,4,-9,-5,-6,6,-2,4,-4,-4,9,-8,-2,-10,-8,-5,-1,6,1,-2,8,4,2,-5,-2,1,2,-8,6,1,1,10,-6,-4,8,5,-6,7,7,-6,10,2,-9,-10,-8,-8,6,3,-4,10,-4,7,4,-10,5,-1,5,9,-4,8,8,3,4,10,6,10,-5,-2,1,1,1,-1,5,-10,-8,3,6,2,5,-8,3,2,4,-8,-7,-3,3,5,-3,-1,5,9,-1,1,-4,-8,6,-5,-4,-9,4,-9,5,8,-1,1,2,-7,-10,10,5,10,-6,4,-10,2,5,4,7,10,-9,-4,-10,4,9,-5,-2,8,4,9,-4,-1,-4,1,-4,-9,-1,-4,6,-2,-3,-9,-5,-6,-8,-4,-6,3,7,1,-2,-6,5,-3,-1,-6,-3,-1,2,7,2,4,6,10,-1,7,-3,-8,3,3,-8,8,4,10,-7,-5,10,-9,-7,2,-1,-3,9,7,3,-6,7,-4,5,8,-3,-3,2,-1,-10,-7,9,-7,1,2,2,-7,-4,-1,-7,3,1,4,7,-2,-8,9,-9,6,10,6,-8,4,-3,2,-5,-9,2,-10,9,-9,-3,2,7,-3,-10,3,-9,-1,-2,-2,2,3,-5,5,5,8,-2,-9,2,6,-9,1,5,-2,-7,-4,-6,-2,-8,-4,9,-10,-6,-10,10,-2,4,-9,-5,6,5,-2,-6,3,-9,8,3,-1,-8,-9,8,7,5,2,7,4,9,5,10,1,7,9,9,8,2,6,-7,1,1,3,-1,-1,3,-8,-4,-2,8,10,3,7,-5,3,-7,5,-8,-5,-5,1,-10,1,-8,6,6,5,6,-3,2,3,10,7,-6,7,7,-1,7,-3,-7,-10,7,-2,-5,3,3,-9,6,9,6,-5,-5,10,-2,-6,-3,4,10,-2,3,4,-3,-6,-9,-5,4,10,8,-1,4,-9,-4,7,-1,10,-6,7,-9,10,-2,5,-5,-7,-6,5,-8,8,-7,7,-4,1,3,-1,5,-2,-8,-4,3,-10,-10,8,-9,-9,1,-6,4,7,7,2,1,8,-3,4,2,5,-9,9,9,-4,-3,-5,8,-4,2,-5,-2,-4,-5,-2,-4,-8,-10,-1,-2,-9,-7,-2,8,2,-4,5,-1,-4,9,1,3,-8,-4,-3,-6,-3,-7,-2,3,-7,10,-4,2,5,-3,7,-8,8,6,10,4,-6,10,-9,1,-1,-7,10,-4,3,3,-5,6,5,-7,-5,10,-3,1,-5,-8,-1,-3,6,-8,-7,8,-4,-7,6,3,4,-5,6,-9,-8,7,-3,2,10,-8,-3,-8,1,-5,9,2,-3,-10,-3,-10,-7,-10,-9,-8,4,-7,2,-5,3,4,10,-5,3,2,6,8,-10,2,1,-10,7,4,-5,4,7,-9,-6,-9,-10,6,4,-9,-2,-8,2,10,7,1,-10,-9,-5,-5,-3,-1,-9,8,2,-10,8,-9,-5,-2,-2,-6,9,3,-4,-6,-5,9,-7,7,-4,-4,-4,3,-2,4,7,8,5,-10,10,-7,5,8,3,-1,-4,-9,6,10,6,-1,5,-9,-1,-1,-8,-5,-6,-7,10,-6,-1,-5,-7,-8,-8,-8,-10,-5,-7,-9,7,-10,-9,-2,2,-3,2,-3,-2,2,10,3,6,-1,4,-9,-6,-2,5,1,-1,-2,2,-2,4,4,-3,-4,-7,-5,4,2,5,4,9,7,2,4,3,-10,-9,3,-5,4,-3,-3,-5,9,-10,-9,-10,10,6,-10,8,-9,6,1,-8,-1,4,-10,-10,8,-1,8,7,-5,-2,3,-5,-6,-4,-10,4,5,-7,6,3,-7,4,8,-5,-2,6,-6,-8,1,1,-4,3,2,4,9,-3,4,4,-7,-2,8,6,10,8,8,3,6,-3,9,-8,7,-5,-9,10,1,-6,-2,5,-10,5,4,-2,-5,-3,-2,-3,4,-9,-8,-8,-1,-10,-1,-6,7,9,-9,-6,-5,9,9,8,9,-6,-6,-7,-1,1,9,-2,-1,10,3,-6,-4,-10,6,-8,-7,1,-9,2,5,-3,-3,3,-8,-5,10,1,-6,-8,-1,7,-9,3,9,1,1,8,-10,1,3,-3,5,8,-7,4,-3,7,-1,3,8,-4,7,-4,-3,9,10,1,-7,9,-7,1,-3,-1,9,-6,7,7,-2,-5,5,-2,-7,2,-6,-8,-3,-1,9,3,-6,-6,-9,-9,3,7,-9,5,-6,9,-8,-2,-8,-9,5,-7,-1,5,6,-2,-9,7,7,-1,-10,4,-7,-1,9,2,-2,-6,1,-4,5,-6,-4,-10,6,6,4,-4,-6,6,4,9,6,-8,5,4,9,-6,-2,4,2,3,-9,4,1,9,7,-1,1,10,3,-10,3,-3,-6,4,-6,1,6,-1,9,-4,7,-9,-5,8,4,-10,6,3,-4,-10,-6,8,-10,2,-8,-6,-10,-7,6,4,-5,-9,2,5,-9,-6,9,10,2,9,-8,9,3,-4,-1,-1,3,-7,9,10,-8,6,2,-7,10,8,-4,-6,3,6,-6,-10,4,-5,1,5,-4,7,9,-10,-3,-6,5,1,-10,2,5,-7,9,-4,-9,-2,-1,9,-4,-10,-7,-3,6,10,3,4,-2,-7,-4,3,-3,6,-5,-6,4,-5,2,-5,4,-6,7,-4,-4,-2,-5,4,2,-2,5,-6,-3,3,-1,-6,4,-1,-6,2,8,-8,2,1,-2,-1,-2,-9,9,2,10,2,-2,9,-10,7,6,2,-9,-10,-7,-1,9,4,4,6,4,10,-3,-7,9,-10,1,-10,7,5,-4,-3,-8,9,-2,6,4,-5,4,-9,-6,-9,-3,1,-1,-5,3,-8,-4,-3,-1,-4,4,4,-9,-2,-4,-4,-9,8,-1,7,-1,-7,1,1,10,8,3,1,-5,-9,-5,7,-1,-6,-9,8,-7,5,6,9,-9,9,1,6,-6,-6,-9,5,-7,2,-3,6,-7,7,4,1,-6,-5,-2,-2,7,9,10,-6,2,-5,-2,6,-9,-7,10,-6,8,-3,4,1,5,7,-2,6,-5,-1,-9,8,-2,1,-1,-10,10,-3,1,8,-2,5,10,-7,10,1,9,-7,4,-2,-9,-6,-6,-5,-3,-4,8,8,-9,-2,-5,10,4,-4,7,5,-8,5,2,-2,-3,-9,-6,-8,1,5,6,-9,-5,1,9,-10,-9,-3,-6,-7,9,-1,-2,-1,-10,-9,4,-9,1,2,7,8,-6,-8,-4,-3,-10,10,-3,5,7,-10,-3,9,10,-5,1,5,-4,2,-10,5,-7,-2,-5,-4,2,-3,-6,9,4,-2,-7,4,2,3,1,1,-4,10,1,-2,-1,-6,-9,-2,-8,10,3,-9,2,-4,2,2,-8,5,-10,10,4,-8,-10,-8,5,4,-3,-1,-8,7,10,-6,-4,8,10,5,6,10,4,-4,7,-8,-2,-3,-6,10,4,4,1,-3,-2,6,4,1,4,-8,3,9,-7,-8,7,-8,-6,-8,-6,7,-9,-5,-8,10,4,-1,6,-4,6,-5,-10,3,-7,4,-2,-3,-3,-4,5,-3,4,5,5,2,-1,-4,9,-6,8,2,-10,-9,-3,6,-8,6,2,-3,-1,10,-3,-3,-2,3,-9,-10,-9,-4,3,-2,-8,5,10,-8,-5,2,-5,-2,-4,-8,9,-5,-6,-3,-10,10,-3,-9,2,-3,10,-5,-2,3,-4,-2,1,-3,8,-6,1,8,10,9,9,-7,9,5,10,9,10,-7,1,-10,8,-9,3,-4,-9,4,-5,6,-4,-7,-8,10,-2,-1,-1,-1,-8,-9,-10,-5,-6,-6,2,6,2,4,-4,9,3,8,-2,2,-1,-2,-4,1,-8,2,8,7,5,-1,-6,-4,2,-3,-1,6,-8,3,9,-3,-1,-6,6,1,3,-10,-4,-7,6,-1,-9,-9,9,-10,-7,3,9,-9,1,6,-1,4,-3,-2,-3,8,-1,-8,10,-7,10,-5,9,3,1,7,-8,-9,-2,-1,-5,-6,5,-7,3,-2,-5,-1,8,-6,5,-2,4,3,-4,8,3,-6,-9,5,-6,-4,-3,-7,1,1,9,-9,7,-7,-8,8,1,2,-6,4,6,-5,5,10,-5,3,4,-7,8,2,10,-9,-6,3,-2,6,-4,-6,2,6,7,-3,5,-4,3,1,7,-4,-3,-5,-3,10,9,-8,-2,-10,6,-3,-3,-6,-2,2,4,-2,-3,9,-7,3,7,-9,-8,9,2,4,9,-4,6,-4,-1,7,-3,-2,-9,6,-8,4,-4,9,7,1,-5,10,-2,2,-1,9,-9,-4,-8,4,-5,-10,-3,5,2,7,3,-9,-4,-8,1,-8,-10,9,-7,2,1,-3,2,-6,5,4,-3,-3,-5,1,-10,-8,-5,8,2,-4,-3,7,4,-10,7,7,8,-8,-2,-8,-9,-3,-5,-6,3,10,-6,1,-2,-9,6,10,5,-6,-8,1,3,2,5,7,-8,3,-5,6,-5,8,-2,-5,10,-5,-6,-4,10,-8,-3,-4,1,-9,-2,-6,1,-10,6,-3,7,-3,-4,-3,-4,-3,4,-2,-5,-3,-5,5,5,-10,-3,7,2,-6,-6,3,9,-9,-3,10,-1,6,2,-3,-1,9,-7,-7,-4,-5,1,4,-4,-3,-5,5,-7,-1,4,-7,-6,-8,-1,-10,-7,7,5,-8,-4,5,5,5,-3,-1,10,-4,2,-7,-7,10,-4,-2,8,-7,2,-4,-6,-6,-7,7,-3,-2,-3,10,10,5,-6,-4,-8,9,-4,4,-3,-10,7,8,8,-7,-10,4,4,5,-10,-4,-9,8,-7,-5,7,3,-5,-4,-10,8,5,-2,-3,8,-6,-2,7,-10,6,-7,3,5,-10,2,9,3,-2,-2,2,8,4,4,-10,8,-2,-9,4,4,4,-5,8,6,3,-4,-7,6,2,3,-4,10,-5,-2,4,4,-6,8,6,-3,-1,7,-9,1,3,-3,-6,-5,-9,-1,-7,-10,3,4,-3,2,3,-2,-2,-2,-9,-4,-8,-8,-7,2,2,-6,10,-6,-8,7,-8,4,3,5,-2,9,-7,9,-3,-10,2,10,10,5,4,9,-2,-2,-10,-7,3,2,-10,-5,-1,8,3,-5,5,10,1,-3,-10,-8,-9,3,-10,3,-6,-2,3,10,9,-10,-5,-6,-8,1,-4,-10,-3,-5,10,2,-6,4,-6,7,10,-2,6,3,-6,1,3,-3,6,9,7,1,6,3,10,7,-7,-6,6,-6,4,-4,-1,-5,-6,3,6,5,1,-3,-7,-4,-1,7,10,2,3,2,3,-2,-2,10,-1,9,2,5,-4,6,-7,-5,-6,-4,-10,-2,-6,10,9,3,5,-2,-5,8,3,-7,7,-1,8,2,2,1,-10,5,2,-1,-1,6,9,-7,8,-5,7,-7,-1,-3,7,-10,-6,8,2,-5,-2,9,4,4,-2,-6,6,4,-4,-2,-10,8,7,5,5,4,-2,-9,-1,-10,-1,-3,-2,6,-3,-9,-1,2,4,9,7,9,8,-8,10,-5,-4,1,5,-4,-4,-5,9,-4,5,4,-9,-3,-2,10,-9,-6,3,-9,-3,-1,5,3,-5,8,-2,-6,-9,10,10,-3,4,1,7,8,-2,-8,-6,2,-9,3,-5,2,8,5,-1,6,-10,-5,-7,-6,3,-8,4,-2,2,-4,-6,3,8,1,-8,5,4,-4,4,-1,-5,-7,1,-4,7,-2,-4,-7,2,-2,-5,-8,-6,9,4,8,-1,8,6,-8,10,8,-6,-6,2,-1,-2,5,1,1,-4,-5,-6,8,7,-7,-6,2,-1,-2,-4,-10,-10,-8,9,-8,-8,9,-10,-8,-4,5,-3,4,5,6,7,-8,1,9,5,2,-2,9,-9,-8,-3,3,-10,-9,10,-4,3,3,-6,-3,-10,6,7,4,4,9,7,-3,-8,1,8,-5,7,-3,10,6,5,4,9,10,-3,1,2,6,6,7,3,3,10,3,-5,2,2,4,5,7,4,8,3,5,1,3,4,6,-3,-5,-9,-10,4,-2,-9,-9,-6,10,-10,9,7,-7,-8,-6,-3,1,8,3,-9,-3,6,3,10,1,8,-3,-2,7,-5,-2,4,10,-7,5,8,4,1,-5,-3,-3,6,8,-8,7,8,2,3,3,5,-7,8,-8,-1,2,-9,4,8,-3,-7,-10,2,-6,-3,6,-8,10,4,-5,-1,10,-1,-7,-8,-5,-3,-9,-8,9,-3,9,7,7,9,8,-8,-2,-3,-8,-9,4,-2,6,-8,-1,-9,-2,4,-8,1,5,-2,-8,5,-4,1,-8,-2,2,9,-3,-6,5,-6,2,-6,-9,-3,-3,-5,5,-8,-10,7,-2,-7,-5,4,2,-2,9,3,-8,7,9,2,-9,-4,1,-2,8,-2,4,-2,5,-5,3,2,-6,-5,-10,-8,-7,7,6,3,-1,-6,10,-3,3,7,6,9,8,-9,-1,7,-1,-8,-6,-10,7,-3,-3,9,-4,4,-8,6,-9,4,3,-9,-6,1,7,10,-5,-10,9,8,8,5,-5,3,5,-3,7,-3,9,4,3,-2,6,1,-3,-9,1,8,7,1,9,10,-7,8,7,4,7,-10,-7,-8,-10,-3,3,6,-3,1,10,-7,-4,-1,-8,-1,-10,-7,2,9,-2,-10,4,-4,2,8,-7,-6,-1,-10,-3,-5,3,-2,-5,6,5,-4,-3,-5,-4,-6,-7,9,-1,-8,-1,-9,-5,9,4,-1,3,-8,-2,3,6,-6,-4,-5,-6,-1,-8,-3,-3,-4,10,-8,9,-3,-8,8,6,1,8,4,8,3,6,-8,-2,6,10,-9,1,-1,-8,5,10,5,1,-4,-5,-5,-4,-9,-7,-8,-2,-7,9,-2,-6,1,4,-4,5,5,4,2,5,4,-10,-9,9,3,-4,5,5,-6,1,-7,-9,-8,-2,-2,-4,1,9,6,5,-6,-8,1,-8,-4,8,-7,4,1,-8,5,7,7,5,6,3,-1,4,4,-10,10,10,4,-5,-1,5,-6,-9,2,6,-6,-1,-2,10,8,-6,7,-8,-9,-5,7,-6,4,-5,1,-4,2,7,-2,-2,8,-9,-4,-5,1,5,10,10,-9,10,-8,-9,10,6,5,-2,-6,8,-9,6,3,-9,-3,6,-6,1,1,-6,-10,-2,-2,7,-7,-9,8,-8,7,1,-6,1,3,6,6,4,-4,-8,-3,6,2,6,-1,10,-10,9,9,-8,3,-8,-3,2,1,6,7,-3,7,8,2,7,10,-9,-5,-3,10,7,6,-3,-9,2,-10,8,2,7,-5,-9,-2,2,-7,6,-6,3,2,10,6,1,7,-5,-5,-7,9,-3,-6,8,2,3,9,-2,1,-2,4,-2,1,9,2,-6,2,3,6,3,7,6,3,7,-9,-10,-2,-1,-2,1,-6,6,-6,-8,-10,10,9,5,5,-6,3,-7,-2,10,-9,-9,-7,5,-4,8,5,3,-8,-6,2,-7,-9,10,3,7,-10,-10,-1,-2,7,-1,2,6,4,-2,3,-1,-6,-6,-10,4,1,-7,-9,9,1,-8,-6,10,6,8,3,-4,10,-9,-4,10,-5,8,-6,-9,7,-7,-2,2,-10,7,-10,2,2,-2,-4,-4,9,-4,10,-9,3,-1,4,-10,4,8,10,-7,3,3,-2,-10,-10,6,-10,-9,3,-7,-3,-1,-6,-2,1,1,7,-1,8,1,-8,9,4,-10,-8,-3,-3,8,5,6,-9,10,-8,6,4,7,4,7,-6,4,3,-4,4,-8,4,-7,-10,1,-7,7,6,-1,-9,-8,-7,-8,-2,1,-6,8,-2,5,9,-1,4,-10,-1,3,-1,-5,-5,-3,5,4,-10,3,5,-5,3,5,-5,10,-5,-7,3,-7,5,5,1,-5,-10,-4,-6,3,4,-9,-2,4,-9,4,-3,10,8,-1,-3,-1,-5,-1,-3,-10,-4,-7,-7,6,3,10,10,5,-5,8,-3,2,5,8,-2,6,-5,-4,3,8,9,-4,-8,-10,7,1,-8,-7,8,10,4,-8,8,-1,2,-9,-9,-4,1,-10,-2,8,5,5,-1,-5,-3,-3,-5,-4,-6,-1,-3,4,9,-10,-6,-4,-4,-6,6,-1,4,-9,-8,9,-5,3,-5,2,10,8,-2,6,-3,-2,-4,7,-7,-7,1,-3,6,6,10,9,2,7,-2,-10,5,-2,-7,7,9,-10,-1,7,-6,1,1,-7,7,-6,7,2,2,-1,6,2,1,4,-3,-9,5,7,8,-8,-10,-4,2,8,-3,-2,4,-2,4,-7,8,9,4,9,2,8,2,8,1,8,5,-1,-4,4,-1,-8,-6,2,3,-3,7,-8,7,-4,3,10,-2,7,-6,-3,-1,-5,7,7,7,6,3,-4,1,-7,-10,2,-2,9,1,4,-4,-9,6,-1,-7,-8,3,1,10,10,-8,5,3,-7,-7,-6,-2,1,2,1,-1,2,-1,-1,2,2,-6,-8,-10,-3,8,7,6,-7,10,-10,9,6,-4,10,8,5,-8,5,10,6,-9,9,8,4,6,-8,5,-2,3,-6,-5,-7,4,2,1,-3,8,6,7,-6,5,7,-10,-10,2,-3,6,7,-3,-5,6,7,-7,-4,4,-7,-3,-10,3,5,-7,-10,2,5,8,-2,-8,-2,3,-9,-5,-9,-1,3,-8,-9,1,-7,7,-10,2,3,4,-2,1,-5,8,-7,2,2,2,-4,1,8,3,-6,2,2,-5,3,8,4,-4,6,5,-6,9,10,1,-9,5,-9,5,3,6,7,3,-9,-4,-3,-2,4,10,3,-1,6,-10,-5,4,6,-1,3,4,-5,6,-5,-8,2,-4,-7,-9,-3,8,5,-3,4,-4,1,1,-6,3,-5,-2,-7,2,-1,9,-2,-1,10,8,9,-3,1,6,2,1,-10,-6,9,-3,9,-4,10,7,-7,-6,-10,7,-4,1,2,-3,6,1,7,6,7,-8,5,-7,-2,-1,1,-6,-2,-10,2,9,3,5,-6,-8,1,10,-3,8,-9,10,8,-6,4,5,1,5,-5,-8,9,4,3,-8,2,-2,5,-2,7,-3,7,-8,-3,-4,3,-1,-7,-4,2,5,-8,-4,8,-7,-7,-7,-10,1,-9,-6,-7,5,-4,4,-1,-10,5,-3,2,-9,10,-1,2,6,9,2,-8,1,5,10,4,6,-3,-4,9,-4,-9,1,-9,3,-8,-3,3,2,9,6,1,-3,-9,1,-10,8,2,-3,8,-8,-2,-5,-6,2,9,9,10,-6,8,-8,4,2,-7,6,2,4,-6,-10,7,8,-2,8,8,10,3,8,7,-5,6,2,7,5,-4,-8,7,-7,-2,10,10,9,1,3,7,2,9,-3,-9,-2,3,4,-5,-10,7,-8,-1,10,-4,8,1,7,4,-6,8,6,7,3,4,-10,1,-9,7,-4,4,-4,-4,5,-3,-2,9,4,9,-8,9,3,-6,-4,-2,3,2,1,10,-7,6,-6,9,-3,-7,1,-10,8,7,-8,2,-4,-1,-4,10,-6,3,3,1,-8,10,-6,4,-6,-6,9,-8,-4,-10,1,-2,-8,6,4,-1,8,4,10,8,8,-10,3,3,-8,8,5,-6,-2,6,2,10,9,-1,-1,-6,-2,7,-6,-5,-3,4,2,1,-2,9,6,-3,-3,-5,3,3,-8,3,1,8,2,2,-4,7,1,10,-5,-2,7,-3,1,-6,-6,-4,-8,1,-6,3,3,6,7,-1,8,1,5,6,9,4,4,2,-10,-3,3,6,7,2,-7,6,-8,-3,-2,8,2,9,-10,7,4,-6,-7,5,-4,7,1,9,10,-4,-10,6,-6,9,7,-6,7,8,-6,-7,3,2,-5,5,4,10,4,7,2,-6,3,10,5,3,2,-2,1,-8,6,4,5,-3,3,-8,5,3,-5,-7,10,2,7,8,-9,-6,2,-4,-5,5,-6,-2,5,10,-10,-10,4,-4,-9,10,-9,-2,6,7,4,1,2,-4,1,-9,-10,1,3,6,-6,-10,3,-5,10,2,3,-6,7,4,-4,8,1,8,3,-6,2,-5,9,-8,1,5,-3,10,10,9,6,6,7,1,-1,2,-6,10,6,-6,-8,-2,1,3,8,5,-9,9,-6,9,-9,1,-5,-1,-9,-9,-10,-9,5,-2,2,-4,10,-1,6,-4,-9,10,-7,7,10,4,9,10,-3,-6,4,10,-3,-10,10,-6,10,5,1,-5,9,2,3,1,-6,3,-7,4,3,-3,-10,4,-6,-7,-4,-7,-10,-3,1,-8,-1,9,-3,1,6,1,-2,-6,-7,-3,-3,-3,9,5,10,-7,6,2,-8,7,7,-10,6,-5,-6,1,-1,2,2,10,-3,-4,2,8,9,3,-5,4,8,-2,10,-6,2,10,7,6,8,1,-6,-9,-4,10,7,1,-3,-4,8,5,7,-4,7,8,-1,-5,-6,3,-9,1,7,3,-5,-5,6,7,-5,-2,2,-8,-7,-4,-7,4,10,-2,-7,8,-4,9,1,3,-6,10,5,4,9,6,5,-2,7,-3,-10,10,-4,-4,-4,2,-2,-9,10,-8,1,7,-3,-10,-4,5,-4,10,4,2,10,10,-6,-8,2,5,9,-9,2,3,4,4,2,5,-7,-6,3,-9,-4,-5,-5,10,-4,-6,-2,-4,8,-4,1,8,8,-5,7,10,-4,-8,5,5,-10,-8,10,9,-10,-10,-4,-1,2,5,-1,-3,-10,-6,-10,6,1,-4,-8,1,-6,10,-9,4,8,-1,4,6,4,9,-2,-5,1,-4,-2,8,5,-10,1,-4,-3,10,8,1,7,-5,9,1,-9,10,1,-9,-7,1,-5,7,-1,-9,-2,-10,-2,-9,4,10,5,7,7,-2,-7,2,-9,3,-9,-8,3,-1,2,-6,10,-2,-8,-10,-4,-1,7,-6,6,6,-10,-6,10,-7,-9,-1,-3,-3,1,-7,-8,-8,4,1,3,-3,10,7,-9,4,-9,7,7,2,5,-3,-8,10,-6,9,-8,4,6,-10,6,-2,-1,9,-9,6,-10,9,-9,-9,-9,4,-3,-5,-10,3,-3,4,-4,-1,-4,6,-5,4,-3,-1,-1,10,-5,-2,-4,-4,-2,10,-1,-8,10,-1,-1,3,7,-6,2,4,-1,-4,-3,-1,-5,2,3,-3,6,-2,-10,-2,-8,9,6,-9,2,-3,2,-2,4,4,-4,4,2,8,10,3,10,-10,-5,-3,-2,2,10,-10,-7,-6,3,2,6,7,10,6,2,-6,6,-4,6,2,-1,10,9,1,-6,7,-5,-9,-4,4,-2,-3,-2,7,-4,-3,3,6,-9,-4,-2,-8,7,1,-2,-9,7,-5,10,6,10,10,-5,7,-3,-1,-4,-1,8,-4,9,7,5,7,-3,-9,4,-8,6,-5,8,6,-6,-5,-1,7,10,7,5,1,9,-10,-9,-4,-4,6,6,8,-2,-8,-1,4,8,-9,7,8,-9,-9,-7,-5,-1,-4,4,-10,-4,9,3,7,7,4,-5,8,-1,2,1,8,10,-10,4,1,8,3,5,3,-5,6,7,4,4,-7,-5,8,7,-10,-7,8,2,7,3,-1,-4,8,2,3,-10,-10,3,10,5,-2,-2,-8,-6,-2,-4,7,10,3,-9,-8,5,6,6,-2,8,3,-8,2,5,-1,9,-7,3,-2,6,-3,-10,1,-7,-6,8,-4,-10,10,-2,-2,-9,1,9,-6,3,-6,-8,-10,-1,-9,6,7,2,9,8,-7,2,-1,-1,-8,8,-9,2,-3,-6,3,-8,7,-8,5,2,3,10,-7,-10,-9,-8,5,10,4,-2,9,7,-9,-6,1,6,2,-7,-1,3,-7,10,10,2,7,2,2,-2,4,-7,6,6,-3,6,-2,-4,9,-1,-6,-6,6,9,-5,1,10,4,-1,-5,-5,-8,9,6,-10,10,9,-10,-4,-3,1,10,-3,-9,-7,9,-5,-9,-3,-6,-3,8,4,6,-7,9,-4,3,-3,2,-9,4,-1,10,-9,6,5,-3,-2,-9,10,8,6,3,-6,-1,-7,-8,-9,2,-7,9,2,4,-3,-2,-10,-10,4,6,-8,2,4,-4,10,-1,4,-10,-4,-8,-7,1,-1,-6,4,-4,10,6,9,5,5,6,-7,-4,3,9,2,-9,-3,-9,-6,-7,-2,10,-2,9,-10,7,-5,8,4,-10,-9,1,-6,7,7,10,-7,-9,5,8,-4,5,-9,9,-2,10,-2,1,5,-1,2,-2,-4,-1,8,6,-6,3,-6,9,-3,-7,-3,-2,8,3,-7,-10,3,-9,1,-6,6,4,-2,-10,-5,-10,5,7,7,3,4,-4,3,9,-1,-2,-4,1,-9,-1,-7,-3,2,8,-1,-3,4,-1,5,10,-4,-4,-9,6,-7,-2,-9,9,-4,-1,7,9,5,8,-9,5,3,4,6,9,9,8,-6,-9,1,7,-8,-9,4,1,8,-9,-5,2,-4,-5,-4,-3,7,5,4,5,-8,-2,-2,8,-9,10,3,-7,6,-2,-4,-5,6,8,1,1,10,4,8,-3,-10,-5,8,1,-2,4,-7,7,-8,3,-2,9,-10,5,4,9,2,6,-3,-4,10,-3,7,-2,6,-4,-2,2,5,-3,7,4,3,-1,-7,-3,3,5,5,4,-3,-2,1,-10,-1,-7,5,10,-1,4,6,-6,5,-6,9,4,8,8,1,-8,-10,-3,-6,3,-3,-7,8,5,-5,4,1,-5,-7,10,2,10,-3,-9,3,-8,10,-5,-9,2,1,7,5,3,-8,9,9,3,10,2,-7,2,-8,-6,5,-4,-5,10,-4,3,4,-1,1,6,10,-7,-2,4,3,-10,9,7,-4,7,10,9,4,-8,8,6,-5,4,-9,-7,10,3,9,5,-8,1,-4,3,-2,1,-8,5,10,-9,8,3,3,-9,-9,6,-9,-7,-9,1,3,9,-10,5,6,9,9,-5,-10,-5,-1,6,7,-4,-6,-8,-6,-2,-3,-6,-10,6,7,-2,-6,-5,7,8,5,-2,7,-1,7,1,8,-3,-2,-10,2,7,-6,-4,4,-8,-4,-1,8,-3,-5,7,2,4,10,-3,5,-10,-2,3,-8,6,-1,10,1,4,-8,1,-2,-1,10,-7,-4,5,1,2,1,1,7,1,5,-3,-8,-2,-1,5,9,-6,8,8,1,9,10,-4,-1,4,-10,-10,3,-9,5,6,7,-6,3,-4,-4,6,5,10,3,-4,10,1,4,-8,5,2,5,-7,-1,-1,-4,-10,7,6,3,2,2,7,-5,-6,8,-2,-5,1,10,3,-9,6,3,5,-2,9,2,1,-10,8,4,-9,1,-4,-2,-8,10,-8,-5,-10,3,10,-5,3,-7,-3,2,-9,2,5,-10,6,8,4,-10,-10,-6,-8,-3,-6,3,1,-1,-8,4,8,10,-6,9,-2,6,4,4,3,-5,8,-8,1,9,-2,-7,-9,-4,5,-4,-4,9,-2,-2,-10,4,4,9,1,7,3,6,10,6,3,2,-2,-7,-8,9,-5,8,-9,5,6,-5,-7,-2,1,4,-10,3,-1,-6,1,-7,-2,-6,-1,-1,2,-8,9,7,10,3,-8,-3,1,8,-9,-8,7,2,-4,6,10,-6,8,8,3,-7,2,-1,-1,4,-1,1,-6,-9,5,-8,-3,-6,6,-6,-7,-1,5,1,1,6,-8,2,-9,4,-8,10,7,-10,-10,-3,3,8,-5,6,2,8,8,-6,10,-10,4,-10,6,3,6,4,9,-9,-1,-2,6,5,-1,8,2,-2,8,7,-1,1,-8,7,9,4,1,-4,-6,-1,-1,10,7,-10,-3,-10,-1,2,-7,7,-6,-7,6,4,-2,1,-3,7,-3,6,7,-8,6,8,-10,-1,-5,-3,-2,7,1,-5,8,-4,-10,5,-6,-6,5,-8,-6,-9,-9,-5,9,-5,9,3,-4,6,-9,3,-8,-10,10,7,-8,10,9,10,-7,-6,-7,-2,10,-6,3,-6,6,-3,3,4,-6,-1,-10,-1,-6,-1,-10,5,-3,8,-10,-6,-8,7,-8,-5,5,-7,4,10,-9,-4,-4,-6,2,4,6,-10,-8,8,-8,-8,6,8,7,2,8,4,5,-10,4,8,-3,-6,7,-5,-8,8,2,6,3,-5,3,5,-9,-4,-9,5,-3,3,7,-7,-4,-9,-2,-6,-2,-5,10,3,-7,2,-1,7,8,-6,-1,9,1,-2,2,7,8,-9,2,-8,8,4,-7,-5,-5,1,5,9,-8,6,-8,-4,-5,-7,-4,7,-6,-1,-3,9,9,-4,-10,10,-6,9,-1,2,-7,-6,-7,3,3,-8,2,6,5,-6,3,-2,4,2,-6,3,7,-2,-2,8,3,-4,3,-6,10,-5,2,1,-1,-3,-7,-10,-8,9,-9,7,-4,7,-1,-10,-9,-3,4,-6,6,6,8,8,-8,5,-5,-1,3,6,3,4,-3,-2,2,-6,9,-10,5,2,6,-5,10,-9,6,-7,-3,2,10,3,-3,-10,10,-9,9,-10,-7,-7,-3,-9,2,-9,-9,-1,8,-2,-4,5,-2,10,-6,-8,7,1,2,10,-6,-8,-1,-5,-4,10,-9,3,9,-5,-6,-9,10,5,-10,3,4,-2,-2,-4,5,-6,10,8,-5,-6,7,5,3,-7,-5,-8,4,3,-8,4,-2,-8,2,-4,8,-9,5,-2,4,-3,2,5,3,1,7,-5,-8,3,-8,6,-9,2,-8,4,4,10,-1,1,3,7,9,-8,6,4,8,-3,6,-1,-10,8,-4,-1,3,1,5,-7,2,9,9,-4,-5,6,-2,8,3,9,6,4,-1,-9,-5,-1,6,-6,5,-3,-9,-4,7,-5,9,10,4,-7,9,3,4,2,6,-4,8,-1,-6,9,8,6,8,5,1,6,9,5,-5,-3,5,-10,-5,-1,8,8,2,3,1,-1,-1,-4,10,6,-6,-6,8,-3,9,-8,4,10,10,-7,3,-5,8,-9,-1,-4,5,10,-6,-10,9,-9,-4,8,-6,8,4,6,-5,10,1,6,4,1,1,4,-9,-4,5,10,-8,1,-4,-5,3,6,1,-7,-8,-4,2,-2,2,6,7,-9,6,8,-6,-8,10,10,-6,8,-9,-6,2,-2,1,4,-7,4,10,1,8,-6,3,-2,6,4,4,-6,7,5,-7,-9,-9,-8,-6,-8,10,3,-9,-4,-6,-10,-10,9,4,7,-2,-6,9,1,-4,-10,-10,-8,9,-5,10,-7,2,8,-9,-9,-1,-1,10,-6,10,7,-10,-10,6,-5,-1,-7,-8,10,9,-8,4,-1,-3,9,2,3,2,4,-9,6,-1,6,7,-9,-5,9,6,6,-6,3,2,1,-9,1,3,-1,-10,6,-3,6,-1,7,-4,9,7,-9,7,-2,4,-8,3,-5,-6,-2,5,-7,4,4,-7,7,4,-1,-5,-9,8,-10,-9,-6,4,-6,-6,7,-6,-10,-5,-7,5,2,-2,-1,-10,-3,-5,-6,7,-10,-6,4,8,-5,1,2,1,-5,6,-5,-8,7,-9,2,8,10,-9,-8,-8,-9,-6,-4,4,-9,-9,9,5,1,-3,-10,5,5,-2,-10,-5,-1,10,7,7,6,-10,-5,3,9,-9,6,-6,-7,-1,1,5,-6,-7,1,-9,-2,-4,-6,-3,2,3,-5,9,1,10,-8,4,-2,-9,9,-1,-10,7,1,-10,-9,3,6,-5,-3,-9,-2,7,7,6,-7,-4,2,-1,-1,-10,-8,4,4,-8,-6,10,-3,-1,-4,-4,-4,7,2,-2,1,-5,4,10,3,-5,-9,5,3,-10,-3,-7,5,-6,2,-1,-10,1,-8,-2,-10,-7,3,1,-10,-2,-5,1,-4,6,6,10,-4,10,3,10,-10,-4,-3,-6,6,-5,6,1,-6,6,6,8,9,3,-9,-7,2,-1,-6,7,4,3,1,-1,-4,-8,5,2,3,7,-8,2,-8,4,-7,-8,-2,-2,6,9,10,-10,-1,-10,6,8,-4,4,1,-7,-9,-3,3,-4,-9,-9,-8,8,1,-6,7,-3,-4,2,4,-8,-4,2,4,-8,-8,-4,8,-6,9,-6,-5,7,5,-7,-1,-10,3,2,-9,-2,7,-5,-9,-4,2,7,8,-9,5,1,-8,-1,-6,-10,-3,-4,-10,7,-10,10,-10,1,2,2,5,-7,8,-6,1,1,-8,-8,4,10,4,-7,-8,4,-10,9,-2,8,4,-4,8,3,-10,6,6,-7,-5,-7,-5,-3,7,-10,-10,-9,-2,3,6,-8,9,-10,8,-5,4,-6,-3,5,2,-1,2,9,2,-4,10,-7,-3,-3,-6,6,10,-10,10,5,9,-6,-5,-6,9,-7,1,-9,1,-7,-2,-7,-4,5,2,-6,3,3,9,5,9,-8,-6,-5,10,-3,7,-3,9,-5,-8,-6,-4,-1,8,10,9,-8,-6,-3,-6,-7,10,-6,-1,-2,3,-2,-6,-10,8,-4,8,6,-6,10,-7,7,-8,8,3,8,9,2,2,2,4,9,-7,-7,3,-4,-4,-10,3,4,10,-3,2,6,1,-4,-3,8,9,2,-3,-4,9,-1,-4,10,7,-4,-3,2,8,7,-10,-9,10,-3,-10,-10,-1,-3,4,-10,9,9,-6,-5,9,-4,-9,-8,-8,2,7,7,10,4,5,6,-10,5,-6,-10,4,-3,-1,-10,3,-7,3,-8,-3,-9,-8,2,10,4,10,2,-10,-5,-8,-9,8,-9,9,-3,2,9,-7,-6,10,6,5,-6,-4,7,-7,-3,4,5,1,-4,-2,-1,-7,7,-10,-9,-2,2,-5,6,-7,6,-2,3,-1,-6,-3,1,5,-7,-2,10,1,-7,-2,8,-3,1,7,9,-4,-10,-2,-6,2,10,10,-7,-1,-7,9,-2,-10,-10,-8,5,-5,-8,-10,4,10,6,-3,10,7,-8,-3,-1,-3,1,1,5,3,-3,-10,6,10,-9,-3,8,8,-6,-6,5,-5,3,2,-2,-3,-9,1,-10,-7,5,-8,10,10,-7,1,8,-8,-4,10,7,-2,-6,-4,-5,5,-3,-6,9,8,-2,9,7,-2,-10,-8,8,5,-4,-10,4,-2,8,-7,-3,4,6,-7,1,-3,-4,9,-2,5,7,-6,1,-5,5,6,9,-3,-3,7,10,8,2,5,4,-9,-7,4,-4,-9,-3,6,6,8,-10,5,4,5,3,-9,1,-9,-4,6,-2,-6,3,8,1,-9,10,2,-9,1,4,8,7,-4,2,6,9,10,3,-9,3,-5,6,-8,-2,-7,-8,-4,6,-5,-9,2,-4,8,-8,2,-9,-8,-4,-9,5,7,-3,-8,8,-7,4,-5,-10,6,1,1,4,-4,6,-7,9,6,-4,1,8,2,-5,-10,1,-5,3,4,-5,-6,-2,-4,8,3,4,7,-1,-6,6,-3,4,-3,4,-4,8,2,2,2,-7,3,10,5,-9,-10,-9,-3,-3,-9,6,5,-3,5,-4,7,-4,3,2,-7,-1,5,-2,-4,-7,-1,6,10,-3,-7,3,-6,-6,-1,9,9,-5,-9,-3,1,3,4,7,1,10,-7,-5,10,-6,-2,-8,-2,-3,1,1,7,-3,-7,6,10,-9,-9,-4,6,1,-2,8,4,-4,-1,-5,10,1,8,-7,-5,7,-1,-4,-10,6,6,7,-7,-2,-7,7,7,-9,7,-3,-2,-6,-1,9,-5,-5,-1,8,-5,-6,-9,4,-3,1,8,-10,-2,3,-7,7,1,3,-6,10,1,-6,9,8,-4,1,1,-2,10,-8,-2,-8,-9,-5,-2,-6,10,-5,3,-2,10,-9,-7,-6,8,3,-1,5,4,2,-4,8,2,7,-9,-4,-4,-10,4,9,1,6,-5,-1,10,4,4,1,9,5,7,-7,-10,2,-4,-10,3,7,6,6,3,-1,5,-5,8,-10,-7,5,-3,-5,-6,-2,-8,6,8,9,3,8,-2,10,-3,6,-7,-9,-6,7,-7,10,1,1,-9,3,-10,9,4,-5,-2,-6,4,9,-8,-3,-9,-2,10,-2,-4,8,-5,-10,-8,3,8,1,5,-1,10,9,8,2,5,-4,8,-4,2,-10,-1,-2,-4,-10,-3,-3,-6,2,4,-1,-7,-1,-10,8,1,2,-4,-10,7,9,-2,5,-5,-3,3,9,2,7,-6,-3,4,8,10,-6,7,-9,8,-8,-10,-1,8,5,3,-1,-8,4,10,9,10,-8,-1,-8,10,-1,9,-5,5,9,1,-4,4,2,2,7,7,8,4,-8,-4,-5,2,-9,10,-4,8,2,10,10,-3,3,-4,-9,-7,-3,5,-3,7,-5,-2,10,1,-5,-5,-10,-4,10,3,6,-8,2,-6,2,1,-2,8,-4,-3,-9,-4,7,-3,-5,8,-8,-2,-10,9,2,9,2,6,-8,3,-7,6,6,-3,-6,4,-7,-6,5,-9,7,10,7,5,5,1,-6,6,-6,3,-9,-6,3,1,1,-4,-10,-6,-2,-2,-9,-1,-2,9,5,10,8,10,1,-9,3,-9,-10,2,7,1,9,-3,8,-10,3,-8,-9,-4,4,-3,1,-2,10,-4,-9,5,6,10,-9,8,-2,4,-9,-2,-6,-9,-8,7,-6,4,-6,3,6,-8,6,10,-4,-1,-5,-5,-9,-7,7,6,-6,9,9,4,7,-2,-7,3,7,6,9,2,-6,-7,-4,6,-3,-2,9,6,7,9,10,-7,3,8,5,-2,-10,7,1,-6,10,-5,-3,3,10,-5,-1,9,8,-8,9,7,8,-5,-7,3,8,-6,-8,-2,10,-1,4,9,-7,-8,-8,6,-8,4,2,5,-5,3,-10,6,-6,3,6,3,-8,10,5,1,-6,3,4,10,-8,5,-9,8,-7,-3,-2,6,7,-7,3,8,-4,-9,-10,8,-1,-6,3,4,-6,2,-5,-9,6,5,-3,-1,7,-5,-9,2,7,10,1,-1,5,4,-4,10,-10,-1,1,2,-10,-4,-2,-10,-6,1,6,-6,-5,-9,-5,1,8,-8,4,9,-7,-4,1,9,4,-5,-2,-1,3,-8,-3,-6,10,1,4,-9,-5,3,7,-1,2,5,-1,10,8,-4,6,-5,-4,10,8,-2,-2,-7,6,2,-6,-1,3,10,-1,6,4,4,8,9,-3,7,3,6,3,-7,-7,5,2,-5,4,2,3,-8,-2,-4,-8,-2,-6,2,8,-8,10,7,3,-6,-1,6,6,4,-1,-3,-1,9,5,9,-1,-8,-4,-2,7,3,8,-2,3,2,-4,4,2,-7,5,2,-4,-6,5,5,-7,10,10,-10,7,9,-7,-1,6,-7,5,-4,10,-5,-7,-9,-1,-10,2,-5,3,4,-9,-8,2,-6,5,-6,-2,-9,3,5,-6,6,6,7,-7,9,6,3,-3,7,-10,2,-5,-1,7,-4,-3,-1,4,-6,10,1,3,4,-2,5,-5,4,-5,8,-2,-7,5,-4,7,-1,5,3,-5,-5,9,9,-6,3,9,-7,6,-8,3,1,1,-7,4,-4,8,-4,-3,2,-7,3,8,8,4,-6,-7,-5,9,-3,-3,-1,-10,7,-9,3,3,3,5,-7,9,-4,-10,-3,4,-3,-4,-7,3,-8,-2,-10,6,-6,7,10,7,-10,-6,8,-8,-6,-9,-9,-6,5,-7,-2,-10,-3,-10,-5,-10,3,-8,7,-4,-2,-5,-5,5,8,-7,-4,9,-8,-4,-3,7,-2,9,-3,-2,5,-6,-10,-2,-3,-1,8,6,-6,-8,-5,-6,-10,-6,-7,-9,-6,5,-6,-6,-6,5,4,1,-4,-10,-3,-7,1,-7,-2,5,1,-5,6,7,-8,-9,6,2,-8,10,-9,4,10,2,-10,-3,-6,-2,-2,8,1,-4,-5,6,1,7,-3,-3,4,9,2,-9,-2,3,-7,-8,6,5,8,-9,7,10,6,-7,7,-8,-7,9,5,-5,-5,-3,5,-6,-1,-4,8,-10,-5,7,-2,3,2,-1,6,-3,1,3,4,-10,2,-5,8,-7,2,-7,10,6,-3,-1,2,-1,-10,10,-4,10,6,8,-1,-9,2,-1,-7,6,-1,1,3,-10,-8,8,1,-8,3,1,1,-1,7,5,7,3,10,-5,8,7,-4,-6,3,3,9,4,-5,3,4,-3,-9,1,10,4,1,-4,6,-1,-3,7,-8,2,-5,-3,-2,10,-5,-5,-8,3,-10,-4,8,-5,10,2,4,-1,-10,-10,3,8,-2,4,-1,9,5,-8,-9,-3,9,-8,1,4,6,-8,3,-8,8,-6,9,2,9,5,5,8,3,-6,7,-10,5,1,-3,-4,-1,1,6,-3,3,4,6,-1,9,-7,-9,-9,-4,-2,-1,9,-5,-3,-2,-5,-4,1,2,-3,1,-7,-7,-5,-9,10,-1,4,-7,-6,-3,4,-9,-9,8,2,-10,-10,-7,9,-1,-6,6,-10,-4,4,9,-5,4,1,-6,3,-4,-4,-9,-7,-2,3,-2,2,9,-5,3,-7,6,3,3,-9,-1,7,5,-8,-8,4,-6,-8,-2,3,5,-4,-10,-4,-1,9,5,1,2,7,-2,4,9,3,6,-5,-10,3,-6,-4,-7,8,-10,2,-8,-6,1,-8,-9,-10,-9,-8,-5,-8,6,-7,-6,5,-4,10,5,2,-3,4,1,8,10,8,5,-6,9,-3,8,9,-4,-4,4,-5,-8,8,7,-9,2,-2,-5,-7,2,7,8,10,6,1,1,6,8,-9,10,10,7,-8,-2,5,4,2,2,4,-7,10,4,7,10,5,-4,-3,-10,-1,5,-6,2,3,-1,3,-5,-8,-7,-8,-1,-6,-1,5,-9,4,6,6,-10,-1,-7,1,-7,10,-5,10,3,-10,6,-8,2,2,-1,-6,-7,-4,-1,-8,-7,2,-9,6,10,-8,1,-5,7,-1,-4,-1,-1,-9,3,3,-6,-10,7,6,-1,-6,-10,5,8,8,-10,7,6,-8,-1,-7,-3,-1,4,-10,2,9,-8,-7,-10,-10,-4,4,3,8,-2,-3,3,-7,-9,-2,-6,-3,3,3,-7,-6,2,-2,1,-10,-7,9,-5,5,-5,7,5,-8,-9,4,7,-6,9,5,10,-4,-8,-4,-1,-9,5,-10,5,1,-10,-10,6,-8,-8,6,10,-2,4,3,5,2,7,2,-9,-8,1,-7,-7,-3,-2,10,10,-10,10,-10,5,-6,-1,6,3,-10,-1,-1,-4,3,3,7,5,-8,3,1,9,10,-6,-1,-2,3,-9,-2,-9,10,8,7,-7,8,4,-7,7,-4,-6,3,-5,-1,-1,9,10,1,-7,1,7,3,1,6,-9,-4,-5,-3,1,7,9,-1,-5,6,3,7,1,3,2,-1,-8,-4,-9,-3,10,-4,6,-7,8,-5,3,2,4,5,3,-6,10,-3,-8,-1,8,7,-9,-7,10,-9,-5,-6,-4,-6,-6,9,-2,-4,1,-9,1,5,4,8,-5,8,5,1,-4,8,9,7,10,-4,-9,3,10,-1,-9,8,-5,4,-8,-3,3,-4,9,-6,3,1,2,3,2,-4,-4,-3,-9,-10,3,1,5,10,7,2,-7,-1,8,1,-7,-1,7,9,-2,-3,4,-10,-9,2,8,5,8,-2,-1,8,-8,-8,-2,3,6,8,-1,-9,-3,-8,5,-4,-1,-1,1,-10,-8,-8,-5,-6,-6,-3,5,7,2,-8,-9,2,-3,2,-10,-5,-1,1,-3,-7,1,5,-1,-5,8,-10,8,-8,-4,-4,-5,5,3,1,10,4,7,9,-2,1,-10,10,4,8,10,-4,-3,8,6,-2,7,-10,-5,-2,-5,-8,7,-10,6,3,-2,-9,-8,10,6,10,8,-10,1,10,9,1,-8,9,1,-9,8,7,-7,-2,1,-8,2,-3,-10,-10,-3,-4,-2,-4,-6,-3,1,2,8,-2,-6,9,-8,2,5,8,-3,-8,7,7,5,8,1,-3,-2,8,-5,5,-1,-3,8,-6,-4,-5,6,-2,3,6,-10,3,-4,-9,1,-2,2,9,-7,-3,9,9,2,-8,-1,-9,1,-2,-6,-4,6,9,3,10,-3,8,2,1,1,9,2,-3,-1,-10,10,3,-1,-6,10,-2,-10,9,8,-6,-9,-10,-4,-6,2,1,9,7,-8,-2,-8,3,7,-10,2,-5,-2,2,2,10,-1,5,6,-9,5,-3,10,-3,-6,1,10,8,10,9,-7,5,1,-9,-4,-1,4,5,8,10,-2,3,-6,5,3,10,-2,-8,-7,-10,-7,-3,5,-4,6,8,-4,10,-3,10,9,-6,6,-6,2,7,8,-10,-6,7,-8,-7,-7,-2,4,-6,1,7,-7,2,10,-9,-9,-1,-3,6,3,-2,2,1,-8,-10,1,8,-10,-7,2,-1,3,6,2,7,-7,6,-5,-5,5,1,5,-4,-4,7,5,6,2,5,-6,-9,-1,10,1,-8,3,2,1,-2,5,10,9,-1,10,3,8,6,-7,5,4,-4,-3,6,2,-10,9,-8,-5,-9,5,-10,-6,-2,5,-10,-1,7,-1,-9,-2,2,8,-4,-1,10,7,-8,-6,-3,-10,-9,7,6,-10,-1,-5,-8,4,-5,-4,-10,-5,-1,9,-2,-9,9,-9,-4,-1,5,-7,-6,-6,-6,8,-1,-4,-3,-8,-3,8,-1,-6,-7,-1,10,7,10,9,-4,-10,9,7,7,9,-4,-2,3,1,7,-4,9,7,3,-5,-4,-1,-9,6,-6,7,-9,5,9,4,8,-4,-7,6,6,8,6,-2,-10,2,3,-5,10,-6,8,6,-6,-2,-3,7,-10,1,6,3,-4,-1,-6,-9,10,7,5,-3,6,-6,-6,2,7,1,7,-9,-1,-9,-9,-3,-6,-7,6,2,7,-4,-10,-8,8,-10,5,9,10,-3,6,9,8,3,-8,-7,2,8,6,6,-5,-2,-6,6,-6,-4,-5,-6,-9,-1,3,-1,-9,-4,-3,2,9,-10,-4,-10,5,5,-8,-5,8,-5,-3,-6,5,1,2,-8,7,5,-4,2,-10,-9,5,-7,-1,-6,1,9,1,6,3,-4,3,2,4,-7,8,-5,4,-8,6,-9,5,3,-8,-9,2,-3,-1,-2,-6,1,7,-9,-10,5,-2,-7,2,2,8,3,5,6,-1,-10,9,1,9,-6,10,9,6,10,5,-2,-5,4,10,-3,8,8,-9,3,2,1,3,-3,-5,8,4,4,6,-9,-7,9,-8,-3,7,-4,-5,8,-4,-6,-3,10,6,-7,3,-9,8,4,-5,2,-2,9,-3,5,8,-10,-8,8,-6,4,-1,-8,3,7,-10,7,7,-9,-5,-2,6,3,2,-7,6,-8,6,-8,-9,-6,5,-10,1,7,-2,8,10,-3,5,-1,-1,2,4,-8,-6,-1,-8,-5,8,7,-10,-9,8,-1,2,-6,10,2,-7,-6,-5,-5,-5,3,2,-5,-7,-1,6,8,5,-3,-3,10,5,4,-4,-4,9,4,7,2,-4,9,-8,-10,-4,-9,-7,-6,6,4,-6,10,-6,-7,-2,9,5,-7,-6,5,7,-4,4,7,-9,-1,-9,-10,-3,-10,-7,2,6,4,-6,3,-2,8,-8,-5,7,-1,5,1,-2,5,-9,-3,8,-10,-4,-8,9,-2,2,-3,-1,5,-10,6,-9,-1,-9,5,10,10,8,2,-5,-6,10,-7,-6,9,-3,7,-7,2,1,-3,-5,-4,-2,-2,-1,-5,-10,5,9,3,10,-3,6,-1,5,7,7,-2,-10,-8,-3,-3,7,2,-4,7,-4,-9,8,-7,-3,10,8,1,-6,-8,-1,-3,-10,6,9,6,-6,4,-6,-6,7,-1,9,2,10,-4,4,-1,10,8,3,-3,-10,2,9,-7,5,3,1,-9,7,3,-9,-6,4,-10,-10,5,-7,-8,-8,-5,2,-8,3,-3,1,2,2,2,-3,-4,-3,-5,-9,-9,5,-3,9,-1,9,3,-1,3,-4,-1,5,-2,-8,1,7,8,5,2,-1,8,-6,-3,7,-10,8,10,1,-4,-8,-8,-8,-8,6,-8,-10,8,-9,-2,-6,9,-4,-9,-2,3,9,-4,8,9,3,-10,4,-10,-2,9,-3,-1,-9,3,5,-3,7,-1,-1,-8,10,9,9,-8,10,-6,8,-3,2,-10,1,-1,-3,5,7,-10,1,-2,9,-1,9,-5,7,-6,3,5,-1,4,3,8,1,6,9,4,9,-6,-5,7,-8,-2,-1,7,-5,4,10,-7,-1,-5,-2,8,-6,-10,-7,2,2,-10,-1,2,10,4,-9,-3,4,3,-8], dtype = "int16")#candidate|5175|(22050,)|const|int16
call_5173 = relay.TupleGetItem(func_2540_call(relay.reshape(var_5174.astype('float32'), [5, 4, 11]), relay.reshape(var_5174.astype('float32'), [5, 4, 11]), relay.reshape(const_5175.astype('int16'), [14, 1575]), relay.reshape(const_5175.astype('uint64'), [14, 1575]), ), 0)
call_5176 = relay.TupleGetItem(func_2545_call(relay.reshape(var_5174.astype('float32'), [5, 4, 11]), relay.reshape(var_5174.astype('float32'), [5, 4, 11]), relay.reshape(const_5175.astype('int16'), [14, 1575]), relay.reshape(const_5175.astype('uint64'), [14, 1575]), ), 0)
output = relay.Tuple([call_5169,call_5173,var_5174,const_5175,])
output2 = relay.Tuple([call_5170,call_5176,var_5174,const_5175,])
func_5182 = relay.Function([var_5174,], output)
mod['func_5182'] = func_5182
mod = relay.transform.InferType()(mod)
mutated_mod['func_5182'] = func_5182
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5183 = relay.var("var_5183", dtype = "float32", shape = (220,))#candidate|5183|(220,)|var|float32
func_5182_call = mutated_mod.get_global_var('func_5182')
call_5184 = func_5182_call(var_5183)
output = call_5184
func_5185 = relay.Function([var_5183], output)
mutated_mod['func_5185'] = func_5185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3553_call = mod.get_global_var('func_3553')
func_3555_call = mutated_mod.get_global_var('func_3555')
call_5214 = relay.TupleGetItem(func_3553_call(), 0)
call_5215 = relay.TupleGetItem(func_3555_call(), 0)
func_3628_call = mod.get_global_var('func_3628')
func_3629_call = mutated_mod.get_global_var('func_3629')
call_5216 = relay.TupleGetItem(func_3628_call(), 1)
call_5217 = relay.TupleGetItem(func_3629_call(), 1)
func_4499_call = mod.get_global_var('func_4499')
func_4500_call = mutated_mod.get_global_var('func_4500')
call_5228 = relay.TupleGetItem(func_4499_call(), 0)
call_5229 = relay.TupleGetItem(func_4500_call(), 0)
output = relay.Tuple([call_5214,call_5216,call_5228,])
output2 = relay.Tuple([call_5215,call_5217,call_5229,])
func_5230 = relay.Function([], output)
mod['func_5230'] = func_5230
mod = relay.transform.InferType()(mod)
mutated_mod['func_5230'] = func_5230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5230_call = mutated_mod.get_global_var('func_5230')
call_5231 = func_5230_call()
output = call_5231
func_5232 = relay.Function([], output)
mutated_mod['func_5232'] = func_5232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5131_call = mod.get_global_var('func_5131')
func_5132_call = mutated_mod.get_global_var('func_5132')
call_5247 = relay.TupleGetItem(func_5131_call(), 0)
call_5248 = relay.TupleGetItem(func_5132_call(), 0)
output = call_5247
output2 = call_5248
func_5268 = relay.Function([], output)
mod['func_5268'] = func_5268
mod = relay.transform.InferType()(mod)
mutated_mod['func_5268'] = func_5268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5268_call = mutated_mod.get_global_var('func_5268')
call_5269 = func_5268_call()
output = call_5269
func_5270 = relay.Function([], output)
mutated_mod['func_5270'] = func_5270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4219_call = mod.get_global_var('func_4219')
func_4220_call = mutated_mod.get_global_var('func_4220')
call_5274 = func_4219_call()
call_5275 = func_4219_call()
func_5268_call = mod.get_global_var('func_5268')
func_5270_call = mutated_mod.get_global_var('func_5270')
call_5284 = func_5268_call()
call_5285 = func_5268_call()
output = relay.Tuple([call_5274,call_5284,])
output2 = relay.Tuple([call_5275,call_5285,])
func_5294 = relay.Function([], output)
mod['func_5294'] = func_5294
mod = relay.transform.InferType()(mod)
output = func_5294()
func_5295 = relay.Function([], output)
mutated_mod['func_5295'] = func_5295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2858_call = mod.get_global_var('func_2858')
func_2859_call = mutated_mod.get_global_var('func_2859')
call_5300 = func_2858_call()
call_5301 = func_2858_call()
func_2073_call = mod.get_global_var('func_2073')
func_2076_call = mutated_mod.get_global_var('func_2076')
const_5309 = relay.const([-10,-4,-3,-3,3,4,4,-7,-9,4,7,6,5,-1,7,-9,-4,-4,-1,2,8,-5,5,-5,6,8,-5,7,10,-3,8,4,6,-7,-6,-1,6,-7,10,7,1,9,-8,6,-4,7,-8,2,-10,2,-9,-10,-1,-7,-9,6,8,6,2,7,8,6,6,3,-8,-2,8,-3,9,1,-2,9,-4,7,-8,10,10,-5], dtype = "uint8")#candidate|5309|(78,)|const|uint8
const_5310 = relay.const([-10,1,-9,6,-9,1,4,-8,-5,-2,8,9,-6,-5,3,7,2,-7,-8,-4,9,-6,9,8,6,-6,-9,-2,4,-6,-7,4,2,10,-4,8,10,-8,7,2,-5,-6,5,-9,-5,-8,9,-4,3,2,8,3,-3,-6,-7,4,7,4,9,-3,-8,9,-4,8,-6,-7,10,2,-2,-4,5,1,-7,5,10,-2,-2,-6,3,4,-6,-2,2,2,2,-3,5,10,8,-9,7,5,-10,4,6,-3,-10,9,-10,-7,6,-7,1,4,-5,6,-2,-9,-3,-8,-4,9,5,-7,-8,5,-2,6,4,-3,-1,-10,9,7,-4,-8,5,4,7,7,6,9,6,3,3,8,-2,-9,8,2,-1,2,-10,-8,-10,10,6,-5,-7,4,-2,-4,-1,-7,8,-4,-2,9,-5,-6,-3,-10,-10,-3,3,6,2,-2,-4,-3,-10,3,3,1,8,-2,6,10,-7,2,2,5,-8,6,-8,4,6,-10,-1,7,-10,2,9,1,-7,-5,-1,-3,-9,-10,-8,7,-4,-2,-5,6,-8,-1,-10,-2,-7,8,-9,-6,-1,-7,1,-4,-8,9,7,-1,4,1,-8,5,-2,-3,5,9,-4,-9,-10,-9,1,-4,-5,-3,-8,-5,7,-2,-4,-10,-2,4,-7,2,-6,-6,1,7,-4,7,5,10,3,-3,-5,-3,-3,-7,-2,6,10,-8,1,-6,-8,-10,-6,-6,-10,-3,3,-4,-7,-7,-9,-10,6,-9,3,-5,-10,-5,3,5,-10,8,6,-10,-4,3,-9,-2,1,3,9,-7,10,5,-3,7,-9,-7,-9,-10,-3,6,-6,-6,-8,-4,-6,5,-5,9,1,1,1,6,6,-2,-9,-10,5,-5,-4,1,10,-6,-10,-2,9,2,-3,9,-4,-6,-9,7,4,-8,-1,-8,9,-7,-9,2,2,9,2,-3,-10,7,-9,5,6,-2,6,-7,6,-6,3,-4,-9,10,-4,6,-6,-5,-9,8,8,2,10,1,-5,2,2,-5,-10,2,2,9,-3,4,-7,-7,10,10,-1,5,-5,-6,-4,10,7,-9,-2,-8,-3,6,5,-6,3,5,7,9,-9,-1,-7,-7,4,5,4,-10,-8,-8,2,-7,2,-8,-6,-2,-6,-9,3,7,-2,5,8,3,-4,10,-7,-10,1,-9,-8,3,2,-5,6,4,8,5,7,-1,-1,6,8,-8,-5,-7,7,-7,9,-6,5,4,1,9,-9,8,3,-9,-9,3,5,-9,9,-3,-9,5,1,7,-1,2,1,2,-6,-7,2,-1,10,-1,-5,7,-3,7,-6,-10,5,8,3,-9,3,-4,-8,1,-6,-6,9,4,-8,8,9,10,1,9,-8,-3,-6,5,1,-1,2,-9,-3,-1,-5,-6,8,-10,5,-2,-10,5,1,10,-10,10,-10,-1,1,-5,-2,3,-8,8,4,8,5,10,5,-8,2,-5,7,7,-7,-4,-5,8,2,9,-5,10,10,6,9,-8,-1,5,-8,-6,7,3,-9,-5,4,8,1,-9,-5,6,-8,7,9,7,-4,-10,3,3,4,-4,4,-10,-10,-7,6,1,8,-5,-9,2,-5,6,-8,1,-1,-10,9,-1,1,-3,9,-10,1,-6,10,-8,2,5,7,2,5,2,-4,-2,-10,1,-1,8,8,4,2,3,10,-6,5,2,3,-3,-10,1,2,-1,3,-4,-3,-7,4,3,-9,8,8,-4,-7,-8,-2,5,1,6,7,-2,-10,-7,10,-8,-10,3,-6,1,-3,-10,-7,10,3,1,8,10,4,-4,-9,3,9,-9,10,10,-10,10,-7,5,-8,10,10,6,9,-8,4,-10,-5,8,9,-1,-10,6,3,7,-10,7,-7,3,5,-6,1,2,5,1,9,4,-3,7,4,7,-3,3,9,7,7,5,-1,4,-8,-9,9,8,-4,9,-3,3,1,7,1,-8,-1,-6,1,-6,7,9,1,-7,6,-4,-2,-4,-4,-7,-9,5,9,10,-3,10,-4,-5,8,-1,-10,3,3,-7,10,-1,-8,-7,-10,-6,5,-5,6,-3,4,1,8,-7,3,5,-9,-2,-5,-3,-8,-7,6,-10,-2,9,5,-3,3,-4,-6,-10,7,4,-3,-6,6,3,-7,-4,-8,-6,-2,5,-9,-2,10,-1,-5,9,-10,8,10,7,6,6,-4,-6,3,10,2,8,5,7,2,6,10,-9,-7,8,10,5,10,8,5,-5,3,7,1,-8,1,-9,9,-3,-6,8,-7,-10,4,-8,10,-4,-7,1,-8,-2,-2,-9,-9,-5,-3,3,-6,9,-2,9,-2,-5,7,-6,-4,1,9,6,4,5,4,9,2,2,-7,-6,-5,6,8,4,-2,7,-8,-1,4,-2,-5,-8,9,1,-10,-4,9,-6,4,10,-8,-7,-9,9,-4,4,1,6,-4,7,5,9,-1,-10,7,-1,6,1,6,-1,-2,2,6,5,-7,4,-4,-6,9,10,-8,1,8,-1,4,7,-6,-1,-6,-4,1,-3,-10,1,-6,5,1,10,-8,6,-3,-1,-1,-3,1,8,-5,6,-1,-5,10,-3,-6,2,3,7,10,-9,10,-8,1,-2,8,-2,-7,-9,6,7,6,7,9,7,2,2,10,-5,-5,-5,-7,3,-5,10,-6,-5,-6,2,-4,5,-5,-2,-7,5,-3,5,9,-3,-2,-8,-10,9,-3,1,9,7,-5,10,5,-3,6,-6,10,1,-2,10,-2,-8,-9,-6,9,4,-2,7,10,6,10,2,1,1,4,3,-10,5,-2,-10,4,-6,-10,4,10,7,1,-9,-5,-6,-2,7,2,1,-2,-4,7,-3,-10,7,4,-2,-5,7,-3,-1,2,5,1,-7,-7,7,2,10,-6,3,-3,5,10,-8,-5,-6,-6,-10,-6,-9,-9,-6,-8,-2,-3,4,-4,4,5,4,8,6,10,-2,-4,-1,9,1,-4,-2,9,-5,-7,6,-10,1,-10,-3,-4,9,5,-10,-7,-2,5,10,-1,7,-3,-9,3,10,-8,4,-7,1,-2,8,1,10,5,-10,-4,-4,9,-7,-5,6,9,7,-4,2,1,-5,4,-8,5,5,4,6,3,6,2,3,-1,-1,-1,2,5,-4,-3,7,-10,-1,10,-10,3,-2,5,8,6,-2,4,-8,-1,7,-5,-6,-7,-1,-4,-1,-6,-4,8,8,1,2,-4,-4,5,1,-6,-6,3,9,8,-4,4,-7,10,-10,-5,-8,-5,8,-6,1,-5,4,-4,-5,4,9,9,-2,-1,-4,5,7,-6,1,3,1,-6,-8,-9,-7,6,1,-9,-6,5,7,2,1,1,8,-3,6,6,-2,-8,-8,-4,-2,3,-3,8,10,8,-9,-3,-4,8,6,5,10,8,10,10,4,9,-2,9,-8,3,-7,4,3,-1,-7,8,10,9,7,-1,3,-10,7,-8,8,10,-8,-7,6,1,-6,3,4,-7,1,1,6,-10,-3,-7,10,6,-4,8,-3,-5,7,-7,10,-3,10,7,-7,10,-5,-9,-6,2,10,-10,-10,-3,5,-9,4,7,6,-1,-3,3,7,3,-8,3,-7,-2,10,-6,-7,-9,9,-4,-10,-9,7,-10,-3,8,-10,-3,6,5,-3,8,-6,-9,-2,9,10,-4,-10,-1,-9,-6,2,5,-5,3,-1,-7,7,-1,9,-3,-10,7,-3,-4,-9,-1,-2,-10,-7,6,-5,7,7,3,10,8,-2,1,-3,-8,-5,-3,7,5,-6,4,-4,-3,8,10,9,9,10,9,-5,6,-7,-9,2,-2,5,-10,-6,-1,-9,2,6,3,1,1,-8,6,-6,4,10,-6,10,5,9,10,-4,9,-4,-8,-2,-1,-8,8,5,-1,7,-10,-3,3,-9,-1,-5,-5,-1,-6,-5,-5,-7,6,4,4,5,8,-9,2,-4,-2,-3,2,1,-9,6,-9,5,-4,3,10,-4,-5,-1,-2,10,-6,1,9,5,-10,9,5,-5,5,-8,5,5,-6,7,-3,-10,-1,6,-4,-5,-3,4,-2,-8,-6,-4,-10,-10,-7,-2,5,-1,4,-4,10,3,-6,5,7,-5,-10,3,-1,-4,-2,-9,10,-1,9,1,7,-7,2,-2,-5,-9,7,-5,-6,7,7,5,9,-10,-3,8,-6,4,-6,4,-7,-6,-6,5,10,-10,-9,4,10], dtype = "int16")#candidate|5310|(1575,)|const|int16
call_5308 = relay.TupleGetItem(func_2073_call(relay.reshape(const_5309.astype('uint8'), [6, 1, 13]), relay.reshape(const_5310.astype('int16'), [1575,]), ), 1)
call_5311 = relay.TupleGetItem(func_2076_call(relay.reshape(const_5309.astype('uint8'), [6, 1, 13]), relay.reshape(const_5310.astype('int16'), [1575,]), ), 1)
output = relay.Tuple([call_5300,call_5308,const_5309,const_5310,])
output2 = relay.Tuple([call_5301,call_5311,const_5309,const_5310,])
func_5337 = relay.Function([], output)
mod['func_5337'] = func_5337
mod = relay.transform.InferType()(mod)
output = func_5337()
func_5338 = relay.Function([], output)
mutated_mod['func_5338'] = func_5338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4438_call = mod.get_global_var('func_4438')
func_4439_call = mutated_mod.get_global_var('func_4439')
call_5396 = relay.TupleGetItem(func_4438_call(), 0)
call_5397 = relay.TupleGetItem(func_4439_call(), 0)
func_3430_call = mod.get_global_var('func_3430')
func_3431_call = mutated_mod.get_global_var('func_3431')
call_5401 = func_3430_call()
call_5402 = func_3430_call()
uop_5410 = relay.erf(call_5401.astype('float64')) # shape=(7, 13, 7)
uop_5412 = relay.erf(call_5402.astype('float64')) # shape=(7, 13, 7)
bop_5422 = relay.bitwise_and(call_5401.astype('int32'), relay.reshape(uop_5410.astype('int32'), relay.shape_of(call_5401))) # shape=(7, 13, 7)
bop_5425 = relay.bitwise_and(call_5402.astype('int32'), relay.reshape(uop_5412.astype('int32'), relay.shape_of(call_5402))) # shape=(7, 13, 7)
func_728_call = mod.get_global_var('func_728')
func_732_call = mutated_mod.get_global_var('func_732')
const_5427 = relay.const([-10,2,-1,-10,-4,2,-9,-10,5,-5,7,-4,6,-8,-1,9,-10,-9,7,3,-6,-7,-4,-5,10,-3,-9,-8,9,1,1,-3,-3,3,2,9,1,-2,-5,-7,6,-4,7,3,9,7,-4,-2,-1,-6,1,10,3,10,-8,3,-6,-10,-10,-10,6,9,-6,-8,-6,-1,-2,-10,2,3,6,5,-6,5,-7,-4,-2,5,-2,6,-7,-6,7,-4,-7,-10,-4,4,-9,5,-6,1,2,6,8,3,-1,4,4,-9,-6,3,-6,-9,8,3,5,-1,-9,-10,-3,4,-9,-3,8,-5,3,-6,6,3,1,1,-9,2,1,7,-2,-7,-3,5,2,-8,9,3,-9,-3,-2,8,-7,1,2,-2,-1,9,-1,7,-6,8,9,3,8,10,-10,-3,-9,-5,-2,-7,-9,-1,1,-4,5,2,-3,-3,3,-5,4,-10,-2,-5,-5,9,9,2,8,-6,-8,-8,-7,4,-4,5,-6,-10,1,5,8,-7,6,6,5,-8,4,6,4,-3,10,8,-2,-6,-4,6,7,-8,5,8,7,5,-1,-5,10,5,4,9,2,7,-8,-7,-8,-7,-10,-3,10,-8,-8,8,-1,-9,6,10,-3,5,2,6,6,3,2,-3,-5,-3,-6,-10,-4,1,-6,10,-8,1,-5,-1,4,-1,9,9,6,6,5,-10,-4,-8,2,10,-3,1,1,10,-6,-10,-4,-9,-2,-6,-1,-5,7,-5,-1,10,-7,-1,1,-4,4,-3,4,3,-9,3,3,-6,1,-1,8,8,2,-6,5,-1,-5,-9,6,-6,-1,4,-7,6,2,4,-9,-9,-6,-4,-6,-1,-9,9,4,-10,-6,-1,-5,-5,-4,-10,3,-4,4,-9,-4,1,-3,-7,-8,2,-1,9,7,4,-2,6,4,6,9,8,6,-5,2,3,-10,5,7,-9,7,8,8,9,-4,-9,8,6,-9,-4,4,-10,-4,8,-1,4,10,9,5,-9,-3,-4,8,-7,-1,-7,-8,-3,-3,2,8,4,-1,8,-1,7,-9,-6,-8,-3,4,6,-8,4,10,5,-5,7,-2,-2,-6,-8,9,-2,-7,-6,5,-2,-10,4,6,7,-10,9,-3,-6,1,2,8,-5,-8,-3,-4,8,5,4,-3,5,7,-5,7,9,-3,-8,-6,-5,5,-9,-7,2,9,3,7,5,-2,-6,2,-6,8,-8,-8,-1,3,1,7,9,-7,1,-10,2,7,-10,-3,5,-10,-6,-8,-1,-6,-8,-4,-2,1,7,-10,-3,6,7,10,3,-5,-8,7,-3,-10,8,9,-6,-1,-4,-3,7,8,1,6,-8,2,-3,5,-1,-6,-10,-9,7,-3,-1,8,8,-2,4,2,8,-7,-4,-6,7,4,-8,8,-2,-8,9,-3,-2,5,-4,5,2,2,4,1,-1,-1,-7,-8,-9,-4,-2,3,-5,-9,7,10,8,7,3,1,4,-2,-10,4,7,-6,-6,-5,9,-9,-8,10,-2,-5,-7,-8,10,-6,2,-10,7,-10,-6,3,6,4,2,1,-2,-8,7,-4,7,9,-7,10,6,-8,-2,-8,4,4,7,-9,-2,-2,6,-5,-5,4,-5,7,-4,-2,7,-5,-3,6,-6,2,5,-6,9,3,8,-7,2,4,8,-2,-7,3,-10,3,5,4,9,-8,3,-2,1,-6,1,10,-4,-4,3,-3,8,9,-1,-3,2,7,-5,8,6,2,2,9,-6,10,-4,-2,-9,8,-3,10,-4,-3,-6,6,7,-3,2,8,9,-7,1,7,-2,9,8,3,6,3,-8,-8,-9,-5,-5,8,1,6,7,-1,10,6,-9,2,-4,-9,-5,9,-8,-4,-7,6,8,-9,7,5,10,-5,-10,-4,3,-7,2,10,-10,2,7,-7,-2,-9,6,4,7,3,-8,10,-2,-10,4,-4,-6,-4,-6,7,7,7,-2,-7,4,-4,1,-4,4,-9,5,3,-2,2,9,-8,-5,-8,-7,6,7,4,6,10,3,8,-5,-7,1,-6,9,5,-8,3,-9,5,-10,3,6,-8,5,6,9,4,3,8,-4,7,5,-9,10,-10,2,6,9,8,-10,-1,-8,-8,-6,6,-9,-6,-3,-1,-9,-3,6,-1,-1,-8,-5,-1,5,7,-4,-5,-6,-1,6,-1,-5,-7,4,-4,9,8,-3,9,8,1,-7,-7,9,-1,10,-9,-8,5,-4,-9,-3,9,7,3,-3,7,3,4,-2,7,1,-8,-2,-3,2,-1,10,-10,-7,-2,9,4,-3,-4,-5,10,6,-3,1,-7,7,-9,-8,-3,1,-7,5,2,8,-5,-8,-7,3,3,7,8,-7,-2,-5,10,-10,-8,-6,3,8,-9,2,-1,7,6,5,1,-10,-7,-7,1,-3,4,-1,3,6,-8,-9,1,2,-1,3,10,-4,6,-3,-1,-10,-6,-4,2,3,8,8,8,-7,8,-1,-3,5,-8,-10,7,-8,1,-1,1,5,-6,9,5,-2,-7,-3,-2,10,9,1,-10,-8,-8,-5,5,-2,-3,6,8,10,5,-4,2,-4,-5,-8,1,-5,-6,-2,10,-5,-5,-2,-9,8,6,10,7,-10,9,5,-5,-3,-3,-4,-8,-8,10,-8,10,4,8,-5,-7,7,-4,-8,-5,10,5,-10,2,8,6,2,1,-4,-9,-6,-6,2,9,7,-8,-3,2,8,1,-8,3,7,-8,-5,-1,-5,7,-7,7,10,2,10,9,9,-3,9,9,-2,-6,-7,-9,6,-10,-10,-10,4,-6,-7,2,6,-3,3,-10,10,-1,5,-7,-6,5,-4,10,6,-2,-2,-8,-4,-1,10,2,-9,7,5,-6,-3,-8,-5,-6,-4,-5,5,-3,4,-5,-7,-6,-2,-10,-7,9,-7,-6,7,5,-10,-8,-6,3,-8,4,-5,-10,3,7,6,9,-7,6,-7,-5,-3,-2,-7,9,-3,-9,-5,-9,-10,-8,4,-10,10,-5,8,4,5,2,-2,7,6,-6,-6,-9,3,7,-5,-8,-4,2,3,5,3,-9,-10,10,4,-7,1,9,3,1,2,3,-2,-9,-4,-10,4,1,8,8,-7,2,-2,2,-8,3,4,-7,-4,9,3,-4,1,-10,7,10,-4,-2,5,2,-8,-3,-3,-7,9,5,-7,10,4,-8,-8,3,-1,8,10,7,-5,10,-3,2,-5,5,-6,10,4,1,6,-6,8,1,2,-7,2,-4,6,-10,-3,-3,-1,8,-10,-7,-10,3,7,-9,-4,7,-4,3,-4,-1,8,-5,8,4,10,-4,6,-2,1,-3,6,3,8,-9,8,1,-5,-7,-10,3,-4,-4,-4,3,-6,2,-6,-3,10,-9,6,-6,-8,6,-4,2,5,8,10,5,-10,9,2,10,-6,2,-1,-2,3,-9,-6,5,-4,-9,6,10,10,10,3,-4,9,10,-6,8,-2,-6,-5,10,-6,6,2,8,7,-6,9,9,7,7,4,5,-2,4,4,9,-2,3,-2,8,8,10,-5,5,-2,7,10,2,5,-1,2,10,-6,-10,2,10,1,9,-10,-7,-7,-8,8,-10,8,1,-3,3,-4,10,2,-7,-9,-8,1,3,2,6,3,-3,7,-2,7,-4,10,-8,-5,5,3,6,1,-3,-1,4,-7,5,-3,8,4,-2,7,5,4,7,5,3,-1,2,-9,5,3,2,9,-9,-2,-5,8,-1,2,-4,-1,5,-5,-5,-3,-8,10,-6,10,2,-4,-8,-9,-9,-9,1,9,-2,-3,9,-7,6,-9,-8,6,10,7,6,-9,8,-7,-5,-5,3,4,-7,10,-8,-4,9,-6,-3,7,10,4,1,9,10,-5,-3,6,9,3,-7,4,8,5,5,-1,-7,3,8,5,7,10,8,9,-4,-5,-9,8,-10,-1,4,-10,-8,-10,6,-4,-7,2,-2,3,3,-8,-8,2,-9,3,-6,6,-9,-4,-4,-7,-5,-8,-9,-3,-8,5,-7,-6,-9,-2,3,2,-6,6,-5,3,-1,8,-2,10,-2,-8,1,5,-4,-8,-5,-10,9,3,8,-5,-6,6,-4,10,1,-6,3,-4,-10,-5,-5,8,-8,7,8,4,4,4,8,5,1,4,5,-10,-2,-4,9,-8,-4,2,6,-7,-7,8,4,-5,-7,10,8,-8,6,-5,3,-1,-6,-10,2,3,-8,-5,6], dtype = "int16")#candidate|5427|(1575,)|const|int16
call_5426 = relay.TupleGetItem(func_728_call(relay.reshape(const_5427.astype('int16'), [7, 15, 15]), relay.reshape(call_5396.astype('float32'), [1, 450]), ), 0)
call_5428 = relay.TupleGetItem(func_732_call(relay.reshape(const_5427.astype('int16'), [7, 15, 15]), relay.reshape(call_5396.astype('float32'), [1, 450]), ), 0)
output = relay.Tuple([call_5396,bop_5422,call_5426,const_5427,])
output2 = relay.Tuple([call_5397,bop_5425,call_5428,const_5427,])
func_5438 = relay.Function([], output)
mod['func_5438'] = func_5438
mod = relay.transform.InferType()(mod)
output = func_5438()
func_5439 = relay.Function([], output)
mutated_mod['func_5439'] = func_5439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4114_call = mod.get_global_var('func_4114')
func_4116_call = mutated_mod.get_global_var('func_4116')
call_5544 = relay.TupleGetItem(func_4114_call(), 1)
call_5545 = relay.TupleGetItem(func_4116_call(), 1)
var_5554 = relay.var("var_5554", dtype = "float64", shape = (8, 8, 4))#candidate|5554|(8, 8, 4)|var|float64
bop_5555 = relay.divide(call_5544.astype('float64'), relay.reshape(var_5554.astype('float64'), relay.shape_of(call_5544))) # shape=(8, 8, 4)
bop_5558 = relay.divide(call_5545.astype('float64'), relay.reshape(var_5554.astype('float64'), relay.shape_of(call_5545))) # shape=(8, 8, 4)
func_5182_call = mod.get_global_var('func_5182')
func_5185_call = mutated_mod.get_global_var('func_5185')
const_5562 = relay.const([-9.561929,-9.688674,1.981617,6.826731,2.103429,5.063762,-7.694854,-4.071203,0.472836,5.181085,-4.616040,-0.778681,9.748482,-3.723364,-5.952745,-0.913665,-8.786560,-1.786455,8.243001,-4.900062,-9.166772,2.204056,6.928566,-4.992012,6.765882,1.457301,-2.426107,8.630772,-8.483197,-5.643182,8.885184,9.949162,0.072159,-8.045528,-7.626492,9.633110,-9.461160,6.762517,-8.474645,-0.598867,0.010951,-1.573552,-7.738020,4.662327,2.248035,0.620632,-7.333027,-3.384381,-8.924654,1.810070,4.704367,4.843220,2.078029,-9.528744,-9.739976,6.310611,-9.644803,2.289581,-3.214532,-1.478575,-1.367080,-3.532725,-0.192226,1.888949,9.707898,0.020086,0.548379,-9.133026,9.403557,7.456537,-1.177990,0.528975,-3.816312,3.391810,-6.308416,-3.783594,3.160249,4.861016,9.437671,-8.272218,0.813287,2.644358,2.147441,-4.181764,-3.019392,-7.514230,-1.543765,-2.788781,9.891091,3.646879,9.380171,-5.342553,9.454095,-4.428174,-3.150584,8.857738,4.098014,8.345879,4.594335,4.051957,9.414312,-8.159655,-1.488695,-8.562290,-1.974512,2.516041,5.762139,-0.082129,5.251145,8.587283,3.392070,-9.780662,1.983644,6.731794,3.618151,2.955046,4.120383,-9.135333,-7.976598,1.501764,6.791990,-5.756599,-2.823574,8.405150,1.493490,-2.134791,2.651102,4.036815,-6.235086,6.310460,-3.432531,-2.598078,-5.179923,5.449524,5.827505,9.947924,5.670482,3.289858,-3.996145,8.461151,1.591824,4.721136,-7.175077,2.195172,5.026235,-1.165645,1.001020,0.405972,-2.196812,-7.726182,1.782230,-2.586617,3.091142,5.812081,-6.717133,-5.887115,-4.787675,-7.133517,-2.670164,8.899477,3.593967,1.874899,-7.957878,-5.328804,6.539369,-9.019912,7.450420,5.601921,-6.604172,-7.284372,-1.620019,-5.718030,-3.762002,9.275151,-8.647385,1.179682,1.467409,6.331943,1.394545,-6.218353,-5.312241,-8.287896,5.366238,5.742485,-8.782481,-7.254585,-6.587629,5.722683,5.052922,5.254463,8.873978,7.837464,-6.408621,-1.847027,0.430446,-1.529529,4.570072,4.188256,4.840172,-4.528925,-9.332427,-3.604861,5.419138,-5.399898,-7.541857,-0.494620,-4.947163,-0.330765,-1.217937,-5.010619,5.078860,-9.488974,8.577957,8.406560,-5.053135,-3.594463,-9.998470,3.408188,-4.887919,9.190442], dtype = "float32")#candidate|5562|(220,)|const|float32
call_5561 = relay.TupleGetItem(func_5182_call(relay.reshape(const_5562.astype('float32'), [220,])), 3)
call_5563 = relay.TupleGetItem(func_5185_call(relay.reshape(const_5562.astype('float32'), [220,])), 3)
uop_5576 = relay.rsqrt(var_5554.astype('float64')) # shape=(8, 8, 4)
output = relay.Tuple([bop_5555,call_5561,const_5562,uop_5576,])
output2 = relay.Tuple([bop_5558,call_5563,const_5562,uop_5576,])
func_5578 = relay.Function([var_5554,], output)
mod['func_5578'] = func_5578
mod = relay.transform.InferType()(mod)
var_5579 = relay.var("var_5579", dtype = "float64", shape = (8, 8, 4))#candidate|5579|(8, 8, 4)|var|float64
output = func_5578(var_5579)
func_5580 = relay.Function([var_5579], output)
mutated_mod['func_5580'] = func_5580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3825_call = mod.get_global_var('func_3825')
func_3826_call = mutated_mod.get_global_var('func_3826')
call_5636 = func_3825_call()
call_5637 = func_3825_call()
uop_5638 = relay.log(call_5636.astype('float64')) # shape=(7, 13, 7)
uop_5640 = relay.log(call_5637.astype('float64')) # shape=(7, 13, 7)
func_728_call = mod.get_global_var('func_728')
func_732_call = mutated_mod.get_global_var('func_732')
var_5644 = relay.var("var_5644", dtype = "int16", shape = (5, 315))#candidate|5644|(5, 315)|var|int16
const_5645 = relay.const([-6.520162,-6.899796,7.219487,-0.527179,-2.942048,5.661467,-4.267523,-0.117775,0.639907,7.805084,-5.311130,-1.217628,-4.873251,-4.509813,-3.419065,1.778011,6.227416,-5.180315,3.456934,-7.931672,1.385192,-2.605558,8.585933,-7.577092,-1.837511,7.852867,4.380963,4.356513,-3.465369,-2.833799,0.356468,5.460874,8.119713,6.715111,5.202031,3.813035,4.319504,-9.568021,-6.678570,-6.601978,-9.421206,4.398701,3.413669,3.279646,-1.711474,4.860630,0.219667,-5.606844,-5.694833,8.695481,5.797365,-6.628382,-1.181172,9.969126,3.253714,2.294583,6.049116,-1.674709,-9.206560,5.855683,5.900802,-2.709707,9.417915,9.113115,-5.969241,5.655078,9.571494,5.163751,-4.362789,-7.156108,-8.580312,-6.408417,-4.328512,-3.986014,-2.991482,-2.355138,-1.298895,2.316444,6.189172,-0.906489,8.279529,-9.607997,4.910556,4.960143,-4.843670,-3.165592,6.717361,8.173555,6.009690,-8.213856,5.134845,7.743314,2.926599,1.935874,5.067418,3.660580,-3.806306,-6.169323,2.900929,7.741844,2.602899,-9.751411,-2.174981,1.941410,3.654816,-7.476931,-4.788869,1.808860,-2.234770,-5.256550,-5.278615,-9.586441,5.427947,-4.052326,-4.410449,5.798088,4.045876,3.873016,9.381236,4.394036,-6.839181,6.324681,9.890131,8.937668,4.201254,-2.819334,3.031874,-8.423890,3.195849,7.204974,8.442501,1.069103,-1.974210,-6.448267,5.553272,-7.164718,8.304406,-6.448329,-6.226512,-2.570234,-6.880231,0.812568,-1.009168,-7.109663,8.363835,1.804744,-1.873531,5.839427,1.635424,-0.560199,-2.106701,2.474690,-5.175658,-4.644116,7.835911,4.455677,0.869326,0.834615,-6.300409,9.024716,7.598948,-4.086919,-3.930574,-4.656286,-4.653792,-7.814612,9.011737,-1.033059,-2.613353,3.196841,-1.076375,1.960760,8.534994,8.319880,-3.962516,7.410998,3.359666,-5.182941,-9.949166,-6.784264,3.847626,4.207088,-8.686095,1.562930,-9.751235,-1.712000,9.112765,6.571679,-8.474070,-6.361690,1.743766,-5.634538,-2.693503,-4.922707,6.930377,8.987098,-7.468524,5.144222,-4.233325,7.308882,6.755474,8.112894,1.935657,-5.065347,8.728782,-5.230490,-5.951563,-8.300386,3.560720,1.504394,5.933052,-5.345408,8.010497,-0.402375,-9.286777,3.797459,9.426823,-5.209534,1.321589,-7.742020,4.604759,6.082504,8.830784,-6.379627,1.057585,7.850322,-8.095080,-2.484126,2.788667,-2.283115,-1.733292,-7.164704,-9.865124,-8.499028,2.754606,0.655790,3.844346,-3.581317,-2.018559,-4.529936,4.395327,-8.257458,5.746597,8.454149,7.774066,-5.497668,9.847789,6.790190,5.609178,6.889418,-9.751289,8.147890,-9.018083,-8.633247,1.562289,-6.903804,-3.952698,-9.851780,1.807756,-4.028062,4.477804,-0.957553,9.191447,9.931164,2.913187,0.739637,8.413061,1.476721,7.293234,-8.314843,-9.047979,3.380400,0.342653,-9.370885,3.581832,0.875521,1.561135,-1.623221,7.656067,2.016841,-3.634878,-9.729786,-4.250016,9.731094,9.119896,-7.111274,-1.073506,-2.382848,4.683597,-9.059678,9.410547,-4.196231,8.879701,-0.371198,-9.917397,3.940503,-0.101468,-2.928263,-9.784753,-4.826176,5.225772,6.383610,-3.828868,3.632982,5.986652,6.432833,5.486639,4.416675,-4.115171,2.154004,-5.525848,8.118929,-6.774607,8.902563,-4.701572,-6.808736,-0.963803,9.737090,2.351377,-9.655854,9.331361,9.547049,6.865427,3.066083,-0.006630,-0.742954,-2.341738,-1.656574,1.407252,7.882735,8.959099,2.680882,4.546651,2.156460,7.936038,7.477212,8.130392,4.211810,-7.079848,-8.322070,8.147782,0.009514,-5.358647,-9.431320,9.198436,4.690581,2.058278,-3.961646,-1.459242,2.029449,9.225794,-8.000523,-2.817107,-6.888801,-9.067057,8.150667,6.615342,8.406932,-9.504592,-8.888427,6.667586,3.486498,-8.308982,-7.464316,4.716801,1.718109,-7.214278,5.209306,6.558955,8.892992,-7.124413,-5.070030,5.171834,0.001968,1.984868,4.681126,-4.227382,-7.347324,-9.974074,8.426046,-0.302477,0.625931,-0.939220,8.793314,-9.912996,9.917133,-6.081044,-1.621167,-5.701157,4.834317,6.598487,-3.934960,0.607535,4.544207,1.172498,5.669956,0.624481,2.590232,9.872068,5.722431,5.599307,-9.157524,-3.423518,-1.939677,8.605995,5.334933,-5.014429,-2.001652,-5.237395,-4.598416,-0.213363,7.460655,-3.190997,7.661801,-4.916775,8.554065,1.663573,5.137542,-2.699560,-6.539928,2.545205,5.432068,-9.952230,-5.800401,9.794911,-6.455414,-6.706267,3.746203,-6.353725,9.377344,2.441820,5.721154,-7.146860,8.187097,-0.941707,-2.288366,8.320732,0.551083,1.882878,-1.249697,-4.379216,-8.956733,-7.095813,4.313989,-5.016756,7.229346,9.517393,3.756354,9.989271,4.258046], dtype = "float32")#candidate|5645|(450,)|const|float32
call_5643 = relay.TupleGetItem(func_728_call(relay.reshape(var_5644.astype('int16'), [7, 15, 15]), relay.reshape(const_5645.astype('float32'), [1, 450]), ), 4)
call_5646 = relay.TupleGetItem(func_732_call(relay.reshape(var_5644.astype('int16'), [7, 15, 15]), relay.reshape(const_5645.astype('float32'), [1, 450]), ), 4)
bop_5655 = relay.logical_and(uop_5638.astype('bool'), relay.reshape(call_5636.astype('bool'), relay.shape_of(uop_5638))) # shape=(7, 13, 7)
bop_5658 = relay.logical_and(uop_5640.astype('bool'), relay.reshape(call_5637.astype('bool'), relay.shape_of(uop_5640))) # shape=(7, 13, 7)
output = relay.Tuple([call_5643,var_5644,const_5645,bop_5655,])
output2 = relay.Tuple([call_5646,var_5644,const_5645,bop_5658,])
func_5664 = relay.Function([var_5644,], output)
mod['func_5664'] = func_5664
mod = relay.transform.InferType()(mod)
var_5665 = relay.var("var_5665", dtype = "int16", shape = (5, 315))#candidate|5665|(5, 315)|var|int16
output = func_5664(var_5665)
func_5666 = relay.Function([var_5665], output)
mutated_mod['func_5666'] = func_5666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4863_call = mod.get_global_var('func_4863')
func_4864_call = mutated_mod.get_global_var('func_4864')
call_5672 = func_4863_call()
call_5673 = func_4863_call()
func_4415_call = mod.get_global_var('func_4415')
func_4416_call = mutated_mod.get_global_var('func_4416')
call_5703 = func_4415_call()
call_5704 = func_4415_call()
bop_5711 = relay.greater_equal(call_5703.astype('bool'), relay.reshape(call_5672.astype('bool'), relay.shape_of(call_5703))) # shape=(780,)
bop_5714 = relay.greater_equal(call_5704.astype('bool'), relay.reshape(call_5673.astype('bool'), relay.shape_of(call_5704))) # shape=(780,)
output = bop_5711
output2 = bop_5714
func_5719 = relay.Function([], output)
mod['func_5719'] = func_5719
mod = relay.transform.InferType()(mod)
mutated_mod['func_5719'] = func_5719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5719_call = mutated_mod.get_global_var('func_5719')
call_5720 = func_5719_call()
output = call_5720
func_5721 = relay.Function([], output)
mutated_mod['func_5721'] = func_5721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3193_call = mod.get_global_var('func_3193')
func_3194_call = mutated_mod.get_global_var('func_3194')
call_5722 = relay.TupleGetItem(func_3193_call(), 0)
call_5723 = relay.TupleGetItem(func_3194_call(), 0)
uop_5726 = relay.atanh(call_5722.astype('float64')) # shape=(780,)
uop_5728 = relay.atanh(call_5723.astype('float64')) # shape=(780,)
func_728_call = mod.get_global_var('func_728')
func_732_call = mutated_mod.get_global_var('func_732')
var_5734 = relay.var("var_5734", dtype = "int16", shape = (1575,))#candidate|5734|(1575,)|var|int16
var_5735 = relay.var("var_5735", dtype = "float32", shape = (450,))#candidate|5735|(450,)|var|float32
call_5733 = relay.TupleGetItem(func_728_call(relay.reshape(var_5734.astype('int16'), [7, 15, 15]), relay.reshape(var_5735.astype('float32'), [1, 450]), ), 3)
call_5736 = relay.TupleGetItem(func_732_call(relay.reshape(var_5734.astype('int16'), [7, 15, 15]), relay.reshape(var_5735.astype('float32'), [1, 450]), ), 3)
output = relay.Tuple([uop_5726,call_5733,var_5734,var_5735,])
output2 = relay.Tuple([uop_5728,call_5736,var_5734,var_5735,])
func_5748 = relay.Function([var_5734,var_5735,], output)
mod['func_5748'] = func_5748
mod = relay.transform.InferType()(mod)
var_5749 = relay.var("var_5749", dtype = "int16", shape = (1575,))#candidate|5749|(1575,)|var|int16
var_5750 = relay.var("var_5750", dtype = "float32", shape = (450,))#candidate|5750|(450,)|var|float32
output = func_5748(var_5749,var_5750,)
func_5751 = relay.Function([var_5749,var_5750,], output)
mutated_mod['func_5751'] = func_5751
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5758 = relay.var("var_5758", dtype = "float32", shape = (15, 8, 9))#candidate|5758|(15, 8, 9)|var|float32
uop_5759 = relay.sqrt(var_5758.astype('float32')) # shape=(15, 8, 9)
output = relay.Tuple([uop_5759,])
output2 = relay.Tuple([uop_5759,])
func_5761 = relay.Function([var_5758,], output)
mod['func_5761'] = func_5761
mod = relay.transform.InferType()(mod)
var_5762 = relay.var("var_5762", dtype = "float32", shape = (15, 8, 9))#candidate|5762|(15, 8, 9)|var|float32
output = func_5761(var_5762)
func_5763 = relay.Function([var_5762], output)
mutated_mod['func_5763'] = func_5763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4958_call = mod.get_global_var('func_4958')
func_4960_call = mutated_mod.get_global_var('func_4960')
call_5768 = relay.TupleGetItem(func_4958_call(), 0)
call_5769 = relay.TupleGetItem(func_4960_call(), 0)
output = relay.Tuple([call_5768,])
output2 = relay.Tuple([call_5769,])
func_5776 = relay.Function([], output)
mod['func_5776'] = func_5776
mod = relay.transform.InferType()(mod)
output = func_5776()
func_5777 = relay.Function([], output)
mutated_mod['func_5777'] = func_5777
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5877 = relay.var("var_5877", dtype = "int8", shape = (16, 13, 1))#candidate|5877|(16, 13, 1)|var|int8
const_5878 = relay.const([[[-10,-10,-3,-2,5,2,-10,-2,-1,-10],[6,-1,8,-9,-10,-1,-6,-7,-7,-9],[-10,-6,5,-1,-7,-5,-6,9,2,5],[1,-4,-6,-7,10,9,8,2,-3,2],[-3,-2,3,-5,1,9,-7,-8,-6,7],[-2,-5,10,-8,2,3,-6,4,-8,6],[-10,-1,10,9,-4,-9,1,-1,-3,5],[8,1,-5,-3,8,4,2,5,5,-5],[10,-9,2,-3,-8,2,-6,-8,-10,6],[10,-5,5,4,2,1,7,-3,10,4],[4,-4,9,-1,-4,-6,-7,9,-1,-4],[-4,4,-4,10,5,-6,10,-7,-3,-7],[-5,3,5,4,5,-8,-4,2,-1,4]],[[8,7,9,8,-4,2,9,-1,-7,8],[-4,5,-1,6,1,10,-1,7,10,-3],[-2,4,-2,6,10,5,2,-2,7,5],[-9,7,-1,-9,2,5,-10,-5,-2,2],[-9,-7,-7,6,-6,-1,-5,4,-3,-6],[6,-8,10,9,-6,-7,-9,8,3,9],[-4,-4,-1,4,3,10,5,8,-1,9],[-9,6,1,4,-5,-3,7,7,-10,-1],[-5,4,9,7,-10,-9,3,7,-9,-9],[-5,-5,-4,10,7,6,-2,-4,-2,-1],[7,1,7,-5,-8,3,9,-8,10,4],[9,1,-10,-2,-6,-5,3,5,2,6],[-4,-5,-7,-5,-3,6,9,-5,2,1]],[[10,-1,10,5,-5,3,-2,-4,3,5],[10,-8,-9,-10,-8,-1,9,-1,9,2],[-9,-5,3,-7,1,-2,5,2,3,-9],[4,-9,-3,9,-10,-7,-6,-7,4,-5],[8,-5,-7,9,8,-1,7,3,-4,-3],[5,-1,-2,2,-4,10,4,7,4,-3],[3,5,6,9,4,4,9,2,6,9],[1,-6,-5,-10,10,-3,7,-2,-8,3],[-2,-1,4,4,7,4,3,5,-2,8],[8,4,9,-8,-6,7,10,10,-1,-6],[8,-6,-7,-8,8,2,7,-1,1,-3],[2,6,8,-8,8,7,3,6,6,2],[2,-10,-9,7,-2,-8,10,8,9,7]],[[1,3,9,5,-5,-9,-10,-10,-2,10],[7,8,-3,-5,4,10,-8,-9,-4,4],[3,8,4,2,-7,2,10,1,-8,-6],[10,8,-8,-7,-5,-4,6,-10,2,-6],[6,-2,8,2,10,10,3,-10,-7,3],[-9,10,1,-4,6,1,-10,8,6,5],[7,8,3,9,6,-6,1,8,10,2],[-6,5,5,5,3,-9,-7,-10,-6,2],[3,7,-4,5,-9,-9,1,2,-9,-9],[-8,3,-5,6,2,-5,6,10,-9,5],[1,4,7,-7,-2,9,5,5,-6,3],[-9,-4,10,-8,-6,-6,6,-6,5,-1],[10,-9,3,6,7,7,10,2,3,1]],[[-2,6,-9,4,8,5,5,-6,7,6],[-3,-1,-4,7,2,1,-6,-5,1,-3],[3,10,9,8,8,-2,-9,-8,-8,2],[-4,6,-10,-7,10,-2,7,5,-8,3],[-7,10,2,8,-4,9,-3,-8,-8,4],[6,-3,9,-8,-10,-4,-10,10,-2,-9],[9,4,5,-3,-8,2,-4,-4,4,-2],[3,-9,10,-4,-8,-1,-10,-6,-7,-9],[7,-7,-8,-6,3,5,1,8,5,-6],[-4,1,9,3,8,1,3,6,6,-4],[-9,-4,4,4,5,-4,6,-7,3,-3],[1,-6,-1,-6,6,8,8,8,6,-3],[3,-4,-5,5,2,-8,-3,7,-7,-3]],[[-2,8,2,4,-9,3,-8,-10,7,-8],[-7,-1,-1,4,-3,2,-7,7,-8,9],[2,9,6,-1,-7,3,-7,4,-3,7],[5,-3,-2,2,-3,-7,-1,-3,6,-4],[-4,6,-1,1,-1,2,-8,10,5,-9],[-3,3,3,-2,1,3,-3,9,1,10],[10,10,6,9,-2,-2,-7,8,3,10],[-8,-1,1,-8,4,4,1,2,-4,1],[-1,10,7,9,-9,-4,-1,-1,7,-7],[-7,-4,7,-10,-9,4,3,2,-3,10],[2,-1,8,-7,1,-7,7,9,-7,4],[9,8,3,3,-10,7,6,-7,10,-1],[-10,-1,8,-10,8,-3,-3,10,2,1]],[[6,-6,-6,7,6,6,4,4,7,9],[9,6,-4,7,10,9,-4,8,-7,5],[-5,-1,8,3,1,-3,-5,-2,5,-6],[-7,-5,-10,-2,-10,-2,10,3,1,5],[1,4,-9,6,8,-1,7,-8,10,5],[7,-6,3,4,7,-7,9,4,-10,2],[-2,-2,10,7,-10,-2,10,-3,-7,-8],[-6,3,-6,3,-9,3,7,-2,5,-7],[-2,9,6,6,1,-8,-6,-2,9,-8],[10,10,7,4,-3,-7,1,8,10,-9],[-5,7,7,6,7,-4,7,4,-8,-8],[-9,-6,10,8,-8,-10,3,6,9,7],[8,-10,-9,-1,-3,10,1,-2,9,-1]],[[-6,-10,8,-2,10,2,-3,2,-9,1],[-1,3,6,-3,7,4,6,-4,-9,-9],[6,-6,-6,-2,-3,-4,-3,-6,-4,6],[4,-5,-5,3,5,-3,-5,-9,9,-5],[-4,7,-6,8,4,1,5,8,-5,4],[-5,1,9,-3,3,3,7,-7,-2,2],[1,4,1,6,3,6,-10,-1,8,7],[2,-1,7,1,-2,-7,-8,9,-5,5],[-8,7,9,4,2,1,9,-2,-1,-10],[-5,8,-10,-3,3,-2,-9,8,6,5],[3,-1,-9,1,-5,-3,-9,-6,-9,5],[-6,-4,7,5,1,-1,-8,-7,3,-7],[10,-9,-2,-10,-5,-4,4,-8,-9,6]],[[2,6,-8,-7,2,1,5,-3,-6,-9],[-9,-2,10,-6,4,10,-9,-8,-9,10],[-10,-3,3,-1,10,8,4,4,1,-4],[4,-10,10,10,2,1,2,-6,-2,4],[10,1,3,7,-7,-10,3,-6,8,2],[-7,-4,7,-4,1,-10,9,3,9,7],[-9,9,-6,4,-10,-6,9,7,-9,6],[-10,-9,8,-2,-1,6,-5,1,9,-5],[-2,-7,-10,9,-9,9,1,-8,-1,-7],[1,-2,8,10,-9,-8,8,5,2,-7],[-9,10,-6,9,9,10,9,8,5,7],[-3,-6,10,6,5,5,-2,2,-3,5],[-6,4,7,5,8,-6,6,-9,-5,-10]],[[-10,4,10,-2,-8,-7,-2,-4,-10,2],[2,8,-4,-4,-6,1,9,-10,3,4],[-8,8,9,-2,-10,9,-4,9,8,5],[8,-1,-1,-8,2,-6,2,-4,-5,-1],[1,-8,-1,-1,10,2,-3,-7,-6,9],[-8,10,-10,-10,-1,3,-3,4,-5,2],[2,3,10,8,-6,4,5,-3,-8,-1],[6,-10,-4,-4,9,6,3,-7,-1,7],[-3,3,-4,-4,-1,-3,10,9,-8,-4],[-10,-2,-10,-4,-3,10,3,-5,-10,-1],[-3,-2,-10,8,-4,8,-3,-5,-7,-5],[1,8,9,-10,2,3,-8,8,-4,7],[-9,1,3,-6,-4,-3,-6,-6,-6,-7]],[[-10,4,5,-5,8,-8,6,8,5,4],[-5,-4,-9,10,-9,-4,9,-6,-1,5],[4,6,-5,3,-10,-1,5,-8,10,-10],[4,9,-3,10,-9,-3,10,-4,6,9],[6,1,-7,-4,6,7,1,3,-2,-7],[-8,5,10,7,9,-1,7,-4,10,3],[-5,6,-8,-9,-4,3,-7,-1,8,-4],[-5,-9,9,-7,3,-5,-10,-4,3,-1],[10,-8,10,3,-9,-4,1,7,9,9],[5,10,-8,-6,-6,6,8,-2,-5,-8],[-1,9,6,-2,-1,6,-6,1,-9,-4],[3,2,4,-2,8,-3,2,2,9,2],[-4,8,-3,5,8,-8,9,-4,3,-2]],[[-6,3,-9,6,9,-10,4,-3,8,10],[7,-7,-7,9,-7,-4,-6,-2,2,-4],[6,3,3,9,-4,-7,9,7,-5,10],[7,-6,1,-1,6,3,9,-3,4,4],[-3,10,7,7,-4,-5,-1,8,-8,8],[-2,5,-8,6,2,-9,10,-6,7,-10],[-2,-3,-7,8,10,1,-6,-5,-7,-6],[10,-4,3,9,7,10,-6,6,-6,1],[10,-7,-8,-3,-5,4,2,-6,-1,-4],[6,-10,9,-8,-10,-10,-10,-9,1,-3],[-10,-10,4,9,4,-6,9,5,-1,2],[1,-6,-1,9,-8,8,7,10,5,9],[-3,10,-10,-2,9,4,6,-10,4,8]],[[-10,-10,6,2,-1,3,-5,-8,9,10],[3,-7,-4,7,6,2,4,7,-3,-3],[10,-10,10,-4,9,-6,-5,-3,-10,1],[-10,4,-6,-5,-9,-5,6,-6,7,-5],[1,1,6,7,6,4,2,9,-10,-6],[3,-10,9,7,-3,2,-6,1,9,-10],[7,-1,3,-6,-6,-3,-4,-10,-8,-10],[-9,-6,7,7,-5,-1,2,-1,3,9],[8,8,7,-8,3,8,2,7,9,-5],[2,7,7,-10,-3,-10,2,-6,6,-6],[2,4,-7,-1,-6,1,2,3,-5,-2],[1,1,9,-6,1,-7,5,-7,2,-9],[6,-8,7,8,6,2,1,3,-3,9]],[[1,9,9,10,-7,2,8,-2,3,7],[-1,7,4,-5,8,-1,2,-7,-9,2],[6,9,-6,-9,2,-6,-6,-8,2,-7],[7,-1,9,10,5,-2,-8,4,-2,2],[-10,-9,-3,7,10,8,-2,-6,7,9],[-10,2,1,-3,-1,-9,5,-7,6,-4],[10,4,10,-2,-6,8,1,-5,10,-9],[2,1,-7,6,4,2,9,-5,3,-6],[8,6,-8,6,-10,-8,-3,2,7,5],[-7,5,-2,6,8,6,-10,7,-5,5],[-6,-10,3,-10,9,2,-2,-3,-9,-10],[3,-3,10,10,-1,-3,-9,7,-4,-2],[4,-8,-3,1,-1,9,8,-6,9,6]],[[-2,-10,-9,-5,-6,5,-1,6,-3,7],[7,10,5,-6,4,8,-8,-9,5,-9],[10,-9,-6,-6,2,-4,7,-6,10,9],[-1,-9,5,-5,9,1,7,-2,-7,-3],[2,-9,1,-5,7,-4,1,9,-1,-6],[10,2,7,2,2,2,3,7,9,5],[-6,-6,4,2,-4,10,4,-1,5,7],[-9,5,2,-5,2,7,-1,-4,2,2],[2,10,-3,-9,6,-10,-4,-6,5,-7],[1,6,9,-1,-5,7,-5,5,7,8],[1,8,-3,2,-6,-6,5,3,1,6],[-6,-3,-1,-1,-4,2,7,1,-6,9],[-3,1,8,-3,7,-6,6,2,-10,6]],[[1,1,9,1,8,7,6,1,-3,6],[-6,1,-4,9,-7,1,-2,8,-6,-9],[1,-6,-6,-3,-3,-9,1,-1,2,-2],[7,-6,6,2,-7,4,9,-4,-7,3],[6,-9,1,-6,1,1,9,-7,-5,7],[-2,-7,9,5,10,5,10,-5,-5,-2],[-8,4,-2,2,-2,9,-10,-2,-10,6],[-4,8,-5,3,-3,-6,-1,8,-1,-3],[1,-4,2,1,-2,-4,8,-10,-2,-2],[-1,-7,7,8,-8,-9,-4,-2,-9,-8],[10,7,1,-10,2,9,-8,-8,2,3],[6,2,4,-4,-9,-6,-4,6,4,-10],[7,2,8,10,-3,-1,-6,-8,-9,5]]], dtype = "int8")#candidate|5878|(16, 13, 10)|const|int8
bop_5879 = relay.maximum(var_5877.astype('int8'), const_5878.astype('int8')) # shape=(16, 13, 10)
output = bop_5879
output2 = bop_5879
func_5884 = relay.Function([var_5877,], output)
mod['func_5884'] = func_5884
mod = relay.transform.InferType()(mod)
mutated_mod['func_5884'] = func_5884
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5885 = relay.var("var_5885", dtype = "int8", shape = (16, 13, 1))#candidate|5885|(16, 13, 1)|var|int8
func_5884_call = mutated_mod.get_global_var('func_5884')
call_5886 = func_5884_call(var_5885)
output = call_5886
func_5887 = relay.Function([var_5885], output)
mutated_mod['func_5887'] = func_5887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4438_call = mod.get_global_var('func_4438')
func_4439_call = mutated_mod.get_global_var('func_4439')
call_5960 = relay.TupleGetItem(func_4438_call(), 0)
call_5961 = relay.TupleGetItem(func_4439_call(), 0)
uop_5965 = relay.log(call_5960.astype('float64')) # shape=(450,)
uop_5967 = relay.log(call_5961.astype('float64')) # shape=(450,)
output = uop_5965
output2 = uop_5967
func_5973 = relay.Function([], output)
mod['func_5973'] = func_5973
mod = relay.transform.InferType()(mod)
output = func_5973()
func_5974 = relay.Function([], output)
mutated_mod['func_5974'] = func_5974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4438_call = mod.get_global_var('func_4438')
func_4439_call = mutated_mod.get_global_var('func_4439')
call_5988 = relay.TupleGetItem(func_4438_call(), 0)
call_5989 = relay.TupleGetItem(func_4439_call(), 0)
func_166_call = mod.get_global_var('func_166')
func_169_call = mutated_mod.get_global_var('func_169')
call_6019 = func_166_call(relay.reshape(call_5988.astype('float32'), [5, 6, 15]))
call_6020 = func_166_call(relay.reshape(call_5988.astype('float32'), [5, 6, 15]))
func_4624_call = mod.get_global_var('func_4624')
func_4625_call = mutated_mod.get_global_var('func_4625')
call_6021 = relay.TupleGetItem(func_4624_call(), 0)
call_6022 = relay.TupleGetItem(func_4625_call(), 0)
func_2909_call = mod.get_global_var('func_2909')
func_2910_call = mutated_mod.get_global_var('func_2910')
call_6023 = func_2909_call()
call_6024 = func_2909_call()
uop_6034 = relay.acos(call_6019.astype('float64')) # shape=(5, 6, 15)
uop_6036 = relay.acos(call_6020.astype('float64')) # shape=(5, 6, 15)
output = relay.Tuple([call_5988,call_6021,call_6023,uop_6034,])
output2 = relay.Tuple([call_5989,call_6022,call_6024,uop_6036,])
func_6038 = relay.Function([], output)
mod['func_6038'] = func_6038
mod = relay.transform.InferType()(mod)
mutated_mod['func_6038'] = func_6038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6038_call = mutated_mod.get_global_var('func_6038')
call_6039 = func_6038_call()
output = call_6039
func_6040 = relay.Function([], output)
mutated_mod['func_6040'] = func_6040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4335_call = mod.get_global_var('func_4335')
func_4336_call = mutated_mod.get_global_var('func_4336')
call_6051 = relay.TupleGetItem(func_4335_call(), 1)
call_6052 = relay.TupleGetItem(func_4336_call(), 1)
uop_6056 = relay.exp(call_6051.astype('float64')) # shape=(16, 2, 12)
uop_6058 = relay.exp(call_6052.astype('float64')) # shape=(16, 2, 12)
output = uop_6056
output2 = uop_6058
func_6063 = relay.Function([], output)
mod['func_6063'] = func_6063
mod = relay.transform.InferType()(mod)
output = func_6063()
func_6064 = relay.Function([], output)
mutated_mod['func_6064'] = func_6064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6063_call = mod.get_global_var('func_6063')
func_6064_call = mutated_mod.get_global_var('func_6064')
call_6067 = func_6063_call()
call_6068 = func_6063_call()
uop_6087 = relay.atanh(call_6067.astype('float64')) # shape=(16, 2, 12)
uop_6089 = relay.atanh(call_6068.astype('float64')) # shape=(16, 2, 12)
output = uop_6087
output2 = uop_6089
func_6091 = relay.Function([], output)
mod['func_6091'] = func_6091
mod = relay.transform.InferType()(mod)
output = func_6091()
func_6092 = relay.Function([], output)
mutated_mod['func_6092'] = func_6092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3941_call = mod.get_global_var('func_3941')
func_3942_call = mutated_mod.get_global_var('func_3942')
call_6113 = relay.TupleGetItem(func_3941_call(), 1)
call_6114 = relay.TupleGetItem(func_3942_call(), 1)
func_3589_call = mod.get_global_var('func_3589')
func_3590_call = mutated_mod.get_global_var('func_3590')
call_6120 = relay.TupleGetItem(func_3589_call(), 0)
call_6121 = relay.TupleGetItem(func_3590_call(), 0)
output = relay.Tuple([call_6113,call_6120,])
output2 = relay.Tuple([call_6114,call_6121,])
func_6126 = relay.Function([], output)
mod['func_6126'] = func_6126
mod = relay.transform.InferType()(mod)
output = func_6126()
func_6127 = relay.Function([], output)
mutated_mod['func_6127'] = func_6127
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6151 = relay.var("var_6151", dtype = "uint32", shape = ())#candidate|6151|()|var|uint32
var_6152 = relay.var("var_6152", dtype = "uint32", shape = (6, 5, 7))#candidate|6152|(6, 5, 7)|var|uint32
bop_6153 = relay.maximum(var_6151.astype('uint32'), var_6152.astype('uint32')) # shape=(6, 5, 7)
func_3753_call = mod.get_global_var('func_3753')
func_3757_call = mutated_mod.get_global_var('func_3757')
var_6158 = relay.var("var_6158", dtype = "float32", shape = (40,))#candidate|6158|(40,)|var|float32
const_6159 = relay.const([5.244743,-8.060456,-4.502431,-1.958815,9.666049,2.029981,-5.281993,-5.690125,6.124557,-0.920115,-0.351093,8.551277,-6.345127,3.143252,0.793778,-4.883864,4.029478,9.353991,4.948304,9.330434,4.085752,-5.927845,3.825333,2.485842,-4.521095,-4.878710,9.023875,3.201277,-8.609262,-9.179642,9.135762,1.195106,6.404274,-0.083212,-0.536806,1.607585,4.379540,5.431327,-1.167973,3.311744,-0.309533,-0.544508,-0.082462,-5.576576,-3.492330,-5.277088,0.476365,-4.792288,-3.201803,9.240580,-6.795846,2.072028,1.456130,9.389382,6.205700,-3.703726,-2.302341,6.542214,-9.920397,-6.599731,-5.875848,6.579902,-4.205869,-2.595452,-1.030020,0.553428,4.317534,-3.404457,-8.156388,-5.730547,9.981936,7.099896,0.339901,-0.175467,-4.333674,-4.626768,1.616834,-4.236114,-4.724100,-2.065121,7.548389,1.055372,-1.124281,3.229232,6.710531,-1.442270,-0.440001,6.760839,6.874415,8.742703,-7.768399,-2.127574,8.224653,3.033497,-9.530507,1.977876,7.473576,-8.571290,-1.251336,-0.136294,2.962254,-2.439127,1.513667,-3.920293,9.653389,-5.226925,7.878493,1.612480,-9.769295,-7.212893,5.655664,-5.069031,1.935971,-0.599688,-0.252743,1.178647,-3.592665,6.615684,3.209408,-6.695815,0.361257,-6.953025,5.569574,-5.390763,-8.420850,-2.695378,-7.230483,6.044256,3.047174,5.065404,-8.329901,-0.484576,3.829685,-3.173807,3.982462,7.241595,-6.918365,1.017746,-0.097540,8.717958,1.426762,-7.321655,-4.128548,1.308589,0.602041,4.845505,7.084077,-9.062780,2.769852,-8.176322,7.196280,9.495847,4.432071,-4.659190,-5.881930,7.851358,5.530731,5.518430,3.744888,-3.387142,-1.080388,-3.925847,9.632896,-2.195758,-8.347381,1.846715,-3.122846,4.912321,7.012041,2.868964,2.161720,3.035518,-2.370024,-0.022659,2.445329,9.347872,-4.760660,-8.481012,-2.357193,-1.405608,4.355469,7.626933,-5.638997,3.284550,-0.460801,-4.497256,1.039133,-4.632460,-5.594831,0.037685,2.409785,4.720285,4.477766,0.255116,-6.170338,-9.598672,8.364155,-2.746967,-8.348376,-9.750875,-7.996870,-3.973579,-9.443396,-0.933896,5.546718,3.031379,-6.205975,-7.608424,-1.186165,4.118606,9.628777,-7.010910,1.203927,-2.331133,-6.653916,-1.895883,6.224913,3.572293,-3.369212,3.785559,7.730893,-5.196772,5.138892,4.947576,4.988243,0.078277,-1.407041,3.239294,-4.388682,6.515418,-3.273623,0.301171,-1.628266,-3.296923,-1.283897,-7.304988,-1.776257,4.625888,4.998760,4.326496,-7.026370,4.211705,-9.376885,-3.546686,3.697579,7.184943,-2.839855,7.116346,5.416368,0.802027,8.409135,-9.874189,-7.735922,-4.994368,-9.102410,-1.032630,-1.495094,-7.197646,9.984615,6.146643,-4.650704,-8.567820,1.680216,-6.893051,5.102826,4.433395,4.160891,-7.428413,2.395433,-0.565737,-0.222412,-6.619988,-4.061438,3.549473,-2.204571,-8.139209,-0.368239,4.560730,3.203470,-0.572917,6.217434,2.345823,9.048157,-2.360015,-8.154237,7.926219,-2.800047,3.564293,-4.948803,-5.678974,8.331547,6.925594,8.399700,-9.704808,-6.963507,-2.725559,-4.787106,0.978239,1.043015,-5.955230,-6.631754,7.352223,-3.514407,5.076000,7.198488,3.950955,0.304755,-6.408247,2.833087,7.311068,-1.843037,3.194932,7.831313,-4.045111,-0.598519,8.609860,-9.537415,6.096131,7.339805,3.089462,-2.634387,-8.032115,-4.473621,5.885236,2.876039,5.476192,-7.465560,-4.448369,3.544303,-8.318998,2.471066,-3.338034,-1.944048,-2.845129,0.573905,9.869744,-4.170074,1.956716,-8.593893,-6.143053,3.679710,6.532226,-4.496042,8.522716,4.449014,-1.871183,6.029647,-9.267178,-0.143841,-3.514599,0.208354,-7.934650,5.051657,-8.812404,-6.730185,8.626474,-6.620411,8.901638,-7.895461,6.795414,-1.610285,-1.036902,-4.966393,-8.588566,-2.084933,-4.375819,-5.615523,3.872044,-3.938091,1.542091,8.357091,-7.867144,-2.785828,-3.781422,0.988202,-2.804183,0.288914,3.709707,5.315491,4.390273,-1.129842,9.876642,-2.816624,-5.246931,-0.022566,7.274872,-2.704365,-7.684523,1.027433,9.283118,-9.451443,-0.732967,6.408643,4.202893,6.161124,-3.065888,3.609951,-2.821234,-8.866908,-7.308620,2.499608,-0.977863,-4.190124,-9.428078,-7.249172,-9.595126,9.790858,-6.814990,-7.183173,7.862305,-8.872404,-0.709481,-8.560108,6.539803,6.432769,6.477774,2.341410,0.517814,-1.192214,1.700872,2.099792,2.598573,7.472616,6.922490,-8.980631,0.316125,-5.755965,-2.758195,0.189054,-8.946917,1.242411,0.505537,9.950848,-6.229219,-0.387413,-7.735967,0.493372,-1.600777,-8.192136,8.040083,-1.863363,1.193078,-4.342631,9.838329,-3.471583,-6.356079,-1.027342,-2.360730,-6.503756,2.238285,1.234007,3.393393,-8.620146,3.657478,5.159195,1.121852,9.308778,2.297224,-8.434218,3.835894,-9.564134,-2.951484,4.817894,-4.653957,-2.531155,-4.862964,-7.950517,-4.908583,7.431082,6.333006,-0.258968,7.897553,5.423104,1.014951,0.357627,-2.037742,7.305456,-6.901896,-9.044139,-9.871301], dtype = "float32")#candidate|6159|(480,)|const|float32
call_6157 = relay.TupleGetItem(func_3753_call(relay.reshape(var_6158.astype('float32'), [10, 4, 1]), relay.reshape(const_6159.astype('float32'), [10, 4, 12]), ), 0)
call_6160 = relay.TupleGetItem(func_3757_call(relay.reshape(var_6158.astype('float32'), [10, 4, 1]), relay.reshape(const_6159.astype('float32'), [10, 4, 12]), ), 0)
output = relay.Tuple([bop_6153,call_6157,var_6158,const_6159,])
output2 = relay.Tuple([bop_6153,call_6160,var_6158,const_6159,])
func_6165 = relay.Function([var_6151,var_6152,var_6158,], output)
mod['func_6165'] = func_6165
mod = relay.transform.InferType()(mod)
mutated_mod['func_6165'] = func_6165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6165_call = mutated_mod.get_global_var('func_6165')
var_6167 = relay.var("var_6167", dtype = "uint32", shape = ())#candidate|6167|()|var|uint32
var_6168 = relay.var("var_6168", dtype = "uint32", shape = (6, 5, 7))#candidate|6168|(6, 5, 7)|var|uint32
var_6169 = relay.var("var_6169", dtype = "float32", shape = (40,))#candidate|6169|(40,)|var|float32
call_6166 = func_6165_call(var_6167,var_6168,var_6169,)
output = call_6166
func_6170 = relay.Function([var_6167,var_6168,var_6169,], output)
mutated_mod['func_6170'] = func_6170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3506_call = mod.get_global_var('func_3506')
func_3508_call = mutated_mod.get_global_var('func_3508')
call_6183 = func_3506_call()
call_6184 = func_3506_call()
output = relay.Tuple([call_6183,])
output2 = relay.Tuple([call_6184,])
func_6196 = relay.Function([], output)
mod['func_6196'] = func_6196
mod = relay.transform.InferType()(mod)
output = func_6196()
func_6197 = relay.Function([], output)
mutated_mod['func_6197'] = func_6197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4624_call = mod.get_global_var('func_4624')
func_4625_call = mutated_mod.get_global_var('func_4625')
call_6198 = relay.TupleGetItem(func_4624_call(), 0)
call_6199 = relay.TupleGetItem(func_4625_call(), 0)
var_6205 = relay.var("var_6205", dtype = "float64", shape = (7, 13, 7))#candidate|6205|(7, 13, 7)|var|float64
bop_6206 = relay.subtract(call_6198.astype('int32'), relay.reshape(var_6205.astype('int32'), relay.shape_of(call_6198))) # shape=(7, 13, 7)
bop_6209 = relay.subtract(call_6199.astype('int32'), relay.reshape(var_6205.astype('int32'), relay.shape_of(call_6199))) # shape=(7, 13, 7)
output = bop_6206
output2 = bop_6209
func_6210 = relay.Function([var_6205,], output)
mod['func_6210'] = func_6210
mod = relay.transform.InferType()(mod)
var_6211 = relay.var("var_6211", dtype = "float64", shape = (7, 13, 7))#candidate|6211|(7, 13, 7)|var|float64
output = func_6210(var_6211)
func_6212 = relay.Function([var_6211], output)
mutated_mod['func_6212'] = func_6212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2909_call = mod.get_global_var('func_2909')
func_2910_call = mutated_mod.get_global_var('func_2910')
call_6240 = func_2909_call()
call_6241 = func_2909_call()
output = relay.Tuple([call_6240,])
output2 = relay.Tuple([call_6241,])
func_6255 = relay.Function([], output)
mod['func_6255'] = func_6255
mod = relay.transform.InferType()(mod)
output = func_6255()
func_6256 = relay.Function([], output)
mutated_mod['func_6256'] = func_6256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4415_call = mod.get_global_var('func_4415')
func_4416_call = mutated_mod.get_global_var('func_4416')
call_6262 = func_4415_call()
call_6263 = func_4415_call()
func_6091_call = mod.get_global_var('func_6091')
func_6092_call = mutated_mod.get_global_var('func_6092')
call_6283 = func_6091_call()
call_6284 = func_6091_call()
uop_6289 = relay.log2(call_6283.astype('float32')) # shape=(16, 2, 12)
uop_6291 = relay.log2(call_6284.astype('float32')) # shape=(16, 2, 12)
output = relay.Tuple([call_6262,uop_6289,])
output2 = relay.Tuple([call_6263,uop_6291,])
func_6317 = relay.Function([], output)
mod['func_6317'] = func_6317
mod = relay.transform.InferType()(mod)
output = func_6317()
func_6318 = relay.Function([], output)
mutated_mod['func_6318'] = func_6318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3628_call = mod.get_global_var('func_3628')
func_3629_call = mutated_mod.get_global_var('func_3629')
call_6361 = relay.TupleGetItem(func_3628_call(), 1)
call_6362 = relay.TupleGetItem(func_3629_call(), 1)
var_6363 = relay.var("var_6363", dtype = "int8", shape = (450,))#candidate|6363|(450,)|var|int8
bop_6364 = relay.floor_mod(call_6361.astype('float64'), relay.reshape(var_6363.astype('float64'), relay.shape_of(call_6361))) # shape=(450,)
bop_6367 = relay.floor_mod(call_6362.astype('float64'), relay.reshape(var_6363.astype('float64'), relay.shape_of(call_6362))) # shape=(450,)
output = relay.Tuple([bop_6364,])
output2 = relay.Tuple([bop_6367,])
func_6381 = relay.Function([var_6363,], output)
mod['func_6381'] = func_6381
mod = relay.transform.InferType()(mod)
mutated_mod['func_6381'] = func_6381
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6382 = relay.var("var_6382", dtype = "int8", shape = (450,))#candidate|6382|(450,)|var|int8
func_6381_call = mutated_mod.get_global_var('func_6381')
call_6383 = func_6381_call(var_6382)
output = call_6383
func_6384 = relay.Function([var_6382], output)
mutated_mod['func_6384'] = func_6384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4063_call = mod.get_global_var('func_4063')
func_4065_call = mutated_mod.get_global_var('func_4065')
call_6419 = relay.TupleGetItem(func_4063_call(), 0)
call_6420 = relay.TupleGetItem(func_4065_call(), 0)
output = relay.Tuple([call_6419,])
output2 = relay.Tuple([call_6420,])
func_6426 = relay.Function([], output)
mod['func_6426'] = func_6426
mod = relay.transform.InferType()(mod)
output = func_6426()
func_6427 = relay.Function([], output)
mutated_mod['func_6427'] = func_6427
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6477 = relay.var("var_6477", dtype = "float64", shape = (6, 10, 16))#candidate|6477|(6, 10, 16)|var|float64
uop_6478 = relay.sin(var_6477.astype('float64')) # shape=(6, 10, 16)
func_2683_call = mod.get_global_var('func_2683')
func_2685_call = mutated_mod.get_global_var('func_2685')
call_6482 = relay.TupleGetItem(func_2683_call(), 0)
call_6483 = relay.TupleGetItem(func_2685_call(), 0)
func_6038_call = mod.get_global_var('func_6038')
func_6040_call = mutated_mod.get_global_var('func_6040')
call_6484 = relay.TupleGetItem(func_6038_call(), 1)
call_6485 = relay.TupleGetItem(func_6040_call(), 1)
output = relay.Tuple([uop_6478,call_6482,call_6484,])
output2 = relay.Tuple([uop_6478,call_6483,call_6485,])
func_6486 = relay.Function([var_6477,], output)
mod['func_6486'] = func_6486
mod = relay.transform.InferType()(mod)
mutated_mod['func_6486'] = func_6486
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6487 = relay.var("var_6487", dtype = "float64", shape = (6, 10, 16))#candidate|6487|(6, 10, 16)|var|float64
func_6486_call = mutated_mod.get_global_var('func_6486')
call_6488 = func_6486_call(var_6487)
output = call_6488
func_6489 = relay.Function([var_6487], output)
mutated_mod['func_6489'] = func_6489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4335_call = mod.get_global_var('func_4335')
func_4336_call = mutated_mod.get_global_var('func_4336')
call_6537 = relay.TupleGetItem(func_4335_call(), 1)
call_6538 = relay.TupleGetItem(func_4336_call(), 1)
output = relay.Tuple([call_6537,])
output2 = relay.Tuple([call_6538,])
func_6561 = relay.Function([], output)
mod['func_6561'] = func_6561
mod = relay.transform.InferType()(mod)
mutated_mod['func_6561'] = func_6561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6561_call = mutated_mod.get_global_var('func_6561')
call_6562 = func_6561_call()
output = call_6562
func_6563 = relay.Function([], output)
mutated_mod['func_6563'] = func_6563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5719_call = mod.get_global_var('func_5719')
func_5721_call = mutated_mod.get_global_var('func_5721')
call_6578 = func_5719_call()
call_6579 = func_5719_call()
output = call_6578
output2 = call_6579
func_6589 = relay.Function([], output)
mod['func_6589'] = func_6589
mod = relay.transform.InferType()(mod)
mutated_mod['func_6589'] = func_6589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6589_call = mutated_mod.get_global_var('func_6589')
call_6590 = func_6589_call()
output = call_6590
func_6591 = relay.Function([], output)
mutated_mod['func_6591'] = func_6591
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6592 = relay.var("var_6592", dtype = "float32", shape = (6, 1, 2))#candidate|6592|(6, 1, 2)|var|float32
uop_6593 = relay.tan(var_6592.astype('float32')) # shape=(6, 1, 2)
func_1401_call = mod.get_global_var('func_1401')
func_1403_call = mutated_mod.get_global_var('func_1403')
var_6597 = relay.var("var_6597", dtype = "float32", shape = (234,))#candidate|6597|(234,)|var|float32
call_6596 = relay.TupleGetItem(func_1401_call(relay.reshape(var_6597.astype('float32'), [6, 13, 3])), 0)
call_6598 = relay.TupleGetItem(func_1403_call(relay.reshape(var_6597.astype('float32'), [6, 13, 3])), 0)
func_5973_call = mod.get_global_var('func_5973')
func_5974_call = mutated_mod.get_global_var('func_5974')
call_6599 = func_5973_call()
call_6600 = func_5973_call()
bop_6601 = relay.logical_or(uop_6593.astype('bool'), relay.reshape(var_6592.astype('bool'), relay.shape_of(uop_6593))) # shape=(6, 1, 2)
func_4063_call = mod.get_global_var('func_4063')
func_4065_call = mutated_mod.get_global_var('func_4065')
call_6605 = relay.TupleGetItem(func_4063_call(), 0)
call_6606 = relay.TupleGetItem(func_4065_call(), 0)
func_6165_call = mod.get_global_var('func_6165')
func_6170_call = mutated_mod.get_global_var('func_6170')
const_6608 = relay.const(8, dtype = "uint32")#candidate|6608|()|const|uint32
const_6609 = relay.const([-5,-8,6,-2,8,-6,2,-4,-2,-4,4,-6,4,2,-3,9,-3,8,6,-2,9,-9,3,-5,-10,9,5,-4,1,8,10,1,-4,-5,-8,-7,2,-7,-1,1,-1,7,6,-4,-7,10,-10,3,7,-8,-2,1,1,10,-10,3,-1,-7,4,-3,-4,10,-1,9,8,4,-10,-5,-3,-5,6,-6,10,4,-3,-7,-8,-10,-8,9,-6,-8,-8,-1,6,5,6,10,5,2,-1,-6,5,-9,6,-1,-3,-1,1,-1,8,10,-7,9,-4,-9,-9,-3,-10,-7,2,-1,6,5,3,-4,-2,-6,5,-1,6,4,-5,-8,-1,3,5,-10,7,-10,-3,-3,1,6,-3,-4,6,-4,5,10,-1,1,9,8,-7,6,5,5,-9,3,-7,-2,-7,8,10,-9,-10,-6,-4,-5,-5,10,-10,-7,7,10,-8,-9,-9,-8,4,10,10,5,10,-4,8,-4,-1,7,10,-4,-2,-5,1,-9,-1,-10,-5,-2,4,-10,9,1,5,-10,5,-5,-6,-7,-2,-5,-7,3,-10,5,-2,-6,-8,-1], dtype = "uint32")#candidate|6609|(210,)|const|uint32
const_6610 = relay.const([-3.261349,1.433034,-4.375454,-8.715498,1.613929,1.515125,0.963434,4.741266,-5.834137,-0.464433,-3.850585,-4.131290,1.204078,2.884438,1.658989,6.702206,2.106363,-9.511132,-0.866190,3.427727,9.090435,3.570969,-9.698834,-4.347726,9.424192,-6.677312,-4.360513,5.253449,1.997539,-6.954979,-9.435083,-4.177645,-0.959647,6.732091,-3.897797,-4.926842,4.150845,-7.506212,1.499984,-8.803463], dtype = "float32")#candidate|6610|(40,)|const|float32
call_6607 = relay.TupleGetItem(func_6165_call(relay.reshape(const_6608.astype('uint32'), []), relay.reshape(const_6609.astype('uint32'), [6, 5, 7]), relay.reshape(const_6610.astype('float32'), [40,]), ), 2)
call_6611 = relay.TupleGetItem(func_6170_call(relay.reshape(const_6608.astype('uint32'), []), relay.reshape(const_6609.astype('uint32'), [6, 5, 7]), relay.reshape(const_6610.astype('float32'), [40,]), ), 2)
output = relay.Tuple([call_6596,var_6597,call_6599,bop_6601,call_6605,call_6607,const_6608,const_6609,const_6610,])
output2 = relay.Tuple([call_6598,var_6597,call_6600,bop_6601,call_6606,call_6611,const_6608,const_6609,const_6610,])
func_6633 = relay.Function([var_6592,var_6597,], output)
mod['func_6633'] = func_6633
mod = relay.transform.InferType()(mod)
mutated_mod['func_6633'] = func_6633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6633_call = mutated_mod.get_global_var('func_6633')
var_6635 = relay.var("var_6635", dtype = "float32", shape = (6, 1, 2))#candidate|6635|(6, 1, 2)|var|float32
var_6636 = relay.var("var_6636", dtype = "float32", shape = (234,))#candidate|6636|(234,)|var|float32
call_6634 = func_6633_call(var_6635,var_6636,)
output = call_6634
func_6637 = relay.Function([var_6635,var_6636,], output)
mutated_mod['func_6637'] = func_6637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2909_call = mod.get_global_var('func_2909')
func_2910_call = mutated_mod.get_global_var('func_2910')
call_6703 = func_2909_call()
call_6704 = func_2909_call()
func_6165_call = mod.get_global_var('func_6165')
func_6170_call = mutated_mod.get_global_var('func_6170')
var_6729 = relay.var("var_6729", dtype = "uint32", shape = ())#candidate|6729|()|var|uint32
var_6730 = relay.var("var_6730", dtype = "uint32", shape = (210,))#candidate|6730|(210,)|var|uint32
var_6731 = relay.var("var_6731", dtype = "float32", shape = (20, 2))#candidate|6731|(20, 2)|var|float32
call_6728 = relay.TupleGetItem(func_6165_call(relay.reshape(var_6729.astype('uint32'), []), relay.reshape(var_6730.astype('uint32'), [6, 5, 7]), relay.reshape(var_6731.astype('float32'), [40,]), ), 3)
call_6732 = relay.TupleGetItem(func_6170_call(relay.reshape(var_6729.astype('uint32'), []), relay.reshape(var_6730.astype('uint32'), [6, 5, 7]), relay.reshape(var_6731.astype('float32'), [40,]), ), 3)
func_4219_call = mod.get_global_var('func_4219')
func_4220_call = mutated_mod.get_global_var('func_4220')
call_6745 = func_4219_call()
call_6746 = func_4219_call()
output = relay.Tuple([call_6703,call_6728,var_6729,var_6730,var_6731,call_6745,])
output2 = relay.Tuple([call_6704,call_6732,var_6729,var_6730,var_6731,call_6746,])
func_6748 = relay.Function([var_6729,var_6730,var_6731,], output)
mod['func_6748'] = func_6748
mod = relay.transform.InferType()(mod)
var_6749 = relay.var("var_6749", dtype = "uint32", shape = ())#candidate|6749|()|var|uint32
var_6750 = relay.var("var_6750", dtype = "uint32", shape = (210,))#candidate|6750|(210,)|var|uint32
var_6751 = relay.var("var_6751", dtype = "float32", shape = (20, 2))#candidate|6751|(20, 2)|var|float32
output = func_6748(var_6749,var_6750,var_6751,)
func_6752 = relay.Function([var_6749,var_6750,var_6751,], output)
mutated_mod['func_6752'] = func_6752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2198_call = mod.get_global_var('func_2198')
func_2199_call = mutated_mod.get_global_var('func_2199')
call_6754 = relay.TupleGetItem(func_2198_call(), 0)
call_6755 = relay.TupleGetItem(func_2199_call(), 0)
output = call_6754
output2 = call_6755
func_6761 = relay.Function([], output)
mod['func_6761'] = func_6761
mod = relay.transform.InferType()(mod)
output = func_6761()
func_6762 = relay.Function([], output)
mutated_mod['func_6762'] = func_6762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3506_call = mod.get_global_var('func_3506')
func_3508_call = mutated_mod.get_global_var('func_3508')
call_6814 = func_3506_call()
call_6815 = func_3506_call()
func_4602_call = mod.get_global_var('func_4602')
func_4605_call = mutated_mod.get_global_var('func_4605')
var_6855 = relay.var("var_6855", dtype = "int8", shape = (75,))#candidate|6855|(75,)|var|int8
call_6854 = relay.TupleGetItem(func_4602_call(relay.reshape(var_6855.astype('int8'), [75,])), 7)
call_6856 = relay.TupleGetItem(func_4605_call(relay.reshape(var_6855.astype('int8'), [75,])), 7)
output = relay.Tuple([call_6814,call_6854,var_6855,])
output2 = relay.Tuple([call_6815,call_6856,var_6855,])
func_6859 = relay.Function([var_6855,], output)
mod['func_6859'] = func_6859
mod = relay.transform.InferType()(mod)
var_6860 = relay.var("var_6860", dtype = "int8", shape = (75,))#candidate|6860|(75,)|var|int8
output = func_6859(var_6860)
func_6861 = relay.Function([var_6860], output)
mutated_mod['func_6861'] = func_6861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3718_call = mod.get_global_var('func_3718')
func_3719_call = mutated_mod.get_global_var('func_3719')
call_6875 = relay.TupleGetItem(func_3718_call(), 0)
call_6876 = relay.TupleGetItem(func_3719_call(), 0)
func_6426_call = mod.get_global_var('func_6426')
func_6427_call = mutated_mod.get_global_var('func_6427')
call_6877 = relay.TupleGetItem(func_6426_call(), 0)
call_6878 = relay.TupleGetItem(func_6427_call(), 0)
func_2765_call = mod.get_global_var('func_2765')
func_2767_call = mutated_mod.get_global_var('func_2767')
call_6882 = relay.TupleGetItem(func_2765_call(), 0)
call_6883 = relay.TupleGetItem(func_2767_call(), 0)
output = relay.Tuple([call_6875,call_6877,call_6882,])
output2 = relay.Tuple([call_6876,call_6878,call_6883,])
func_6893 = relay.Function([], output)
mod['func_6893'] = func_6893
mod = relay.transform.InferType()(mod)
output = func_6893()
func_6894 = relay.Function([], output)
mutated_mod['func_6894'] = func_6894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3193_call = mod.get_global_var('func_3193')
func_3194_call = mutated_mod.get_global_var('func_3194')
call_6992 = relay.TupleGetItem(func_3193_call(), 0)
call_6993 = relay.TupleGetItem(func_3194_call(), 0)
output = call_6992
output2 = call_6993
func_7004 = relay.Function([], output)
mod['func_7004'] = func_7004
mod = relay.transform.InferType()(mod)
output = func_7004()
func_7005 = relay.Function([], output)
mutated_mod['func_7005'] = func_7005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3148_call = mod.get_global_var('func_3148')
func_3150_call = mutated_mod.get_global_var('func_3150')
call_7020 = relay.TupleGetItem(func_3148_call(), 3)
call_7021 = relay.TupleGetItem(func_3150_call(), 3)
output = relay.Tuple([call_7020,])
output2 = relay.Tuple([call_7021,])
func_7023 = relay.Function([], output)
mod['func_7023'] = func_7023
mod = relay.transform.InferType()(mod)
output = func_7023()
func_7024 = relay.Function([], output)
mutated_mod['func_7024'] = func_7024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3589_call = mod.get_global_var('func_3589')
func_3590_call = mutated_mod.get_global_var('func_3590')
call_7049 = relay.TupleGetItem(func_3589_call(), 0)
call_7050 = relay.TupleGetItem(func_3590_call(), 0)
func_3790_call = mod.get_global_var('func_3790')
func_3793_call = mutated_mod.get_global_var('func_3793')
const_7056 = relay.const([-5.151912,6.511512,4.654565,1.521468,-3.414264,8.536718,-5.169152,4.805387,8.981339,-5.582657,3.196227,-6.884913,-6.524271,-7.645313,2.441132,-0.972118,8.681843,2.466843,-8.866180,2.922550,-8.094524,5.335962,0.921968,7.648819,-4.939547,0.693956,-3.011763,-4.502787,7.068465,-8.734404,3.414796,-5.749232,-6.891757,8.257821,-7.933807,2.589847,0.163245,-9.651769,-7.119627,0.487722,7.659796,-2.465031,-5.005949,-4.812537,5.717313,-1.819920,2.395411,1.523713,8.565702,-1.436536,-1.351323,-6.649028,2.222591,-6.466143,-8.810840,-5.100518,-3.210533,1.661654,2.505029,-3.823008,-3.206816,7.767028,-7.328709,1.242957,5.446946,4.193547,-7.924731,4.632907,-5.258184,5.673013,6.512112,-3.029082,-1.262302,-0.840795,-7.046334,-5.811741,-8.292518,-8.219224,0.017612,-0.299640,-1.421109,-5.708500,7.938983,-8.538119,4.400435,-9.328480,8.008519,-9.754359,4.054159,7.700862,-6.342283,-2.880382,-0.503584,1.121170,6.542387,-0.419865,2.398168,-1.875193,5.290995,1.521180,-1.774382,9.495475,-2.292574,3.638080,0.401777,3.017365,-2.031232,-9.144386,9.483433,-9.409870,2.305792,-9.725499,0.305491,4.432014,9.029221,7.441298,-6.917316,0.732923,3.144516,-0.769477,1.117145,-0.602727,-9.656384,-5.704435,-3.163708,-0.668438,-6.879278,-6.423548,5.192799,-8.483919,-0.121844,-8.783062,-7.292213,-1.948852,-0.636356,-0.828413,-5.324150,1.098506,7.731113,-1.461051,5.644288,0.996412,3.818236,8.231346,4.332840,8.588823,-2.478375,7.547519,9.333287,-8.750535,-3.296103,-3.597306,0.161085,8.549987,8.860240,-8.371666,-9.505702,-4.915495,6.794557,-3.851688,7.203919,1.537425,6.581431,4.407795,-8.900804,-8.379012,-6.354031,2.902197,5.222965,6.677990,5.595820,6.336972,6.972874,5.755236,4.846165,-0.937830,-3.577578,-5.212265,-9.974952,-8.933099,2.630439,4.306069,2.726210,3.513640,-6.906081,-5.681026,-9.734427,8.873588,6.545413,3.745644,7.357436,-9.092662,5.951317,3.238080,-5.925629,-9.785772,4.786616,4.230433,-4.353979,8.472449,8.506561,-3.348232,3.372402,-8.807735,3.369634,6.519841,0.044205,-2.688399,3.578405,-1.209671], dtype = "float32")#candidate|7056|(210,)|const|float32
call_7055 = relay.TupleGetItem(func_3790_call(relay.reshape(const_7056.astype('float32'), [6, 5, 7])), 0)
call_7057 = relay.TupleGetItem(func_3793_call(relay.reshape(const_7056.astype('float32'), [6, 5, 7])), 0)
uop_7060 = relay.rsqrt(call_7055.astype('float32')) # shape=(6, 5, 7)
uop_7062 = relay.rsqrt(call_7057.astype('float32')) # shape=(6, 5, 7)
bop_7073 = relay.left_shift(uop_7060.astype('int16'), relay.reshape(call_7055.astype('int16'), relay.shape_of(uop_7060))) # shape=(6, 5, 7)
bop_7076 = relay.left_shift(uop_7062.astype('int16'), relay.reshape(call_7057.astype('int16'), relay.shape_of(uop_7062))) # shape=(6, 5, 7)
output = relay.Tuple([call_7049,const_7056,bop_7073,])
output2 = relay.Tuple([call_7050,const_7056,bop_7076,])
func_7077 = relay.Function([], output)
mod['func_7077'] = func_7077
mod = relay.transform.InferType()(mod)
output = func_7077()
func_7078 = relay.Function([], output)
mutated_mod['func_7078'] = func_7078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5230_call = mod.get_global_var('func_5230')
func_5232_call = mutated_mod.get_global_var('func_5232')
call_7094 = relay.TupleGetItem(func_5230_call(), 2)
call_7095 = relay.TupleGetItem(func_5232_call(), 2)
output = relay.Tuple([call_7094,])
output2 = relay.Tuple([call_7095,])
func_7098 = relay.Function([], output)
mod['func_7098'] = func_7098
mod = relay.transform.InferType()(mod)
output = func_7098()
func_7099 = relay.Function([], output)
mutated_mod['func_7099'] = func_7099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4852_call = mod.get_global_var('func_4852')
func_4854_call = mutated_mod.get_global_var('func_4854')
call_7153 = relay.TupleGetItem(func_4852_call(), 0)
call_7154 = relay.TupleGetItem(func_4854_call(), 0)
var_7164 = relay.var("var_7164", dtype = "float64", shape = (7, 13, 7))#candidate|7164|(7, 13, 7)|var|float64
bop_7165 = relay.floor_mod(call_7153.astype('float64'), relay.reshape(var_7164.astype('float64'), relay.shape_of(call_7153))) # shape=(7, 13, 7)
bop_7168 = relay.floor_mod(call_7154.astype('float64'), relay.reshape(var_7164.astype('float64'), relay.shape_of(call_7154))) # shape=(7, 13, 7)
uop_7169 = relay.cos(bop_7165.astype('float32')) # shape=(7, 13, 7)
uop_7171 = relay.cos(bop_7168.astype('float32')) # shape=(7, 13, 7)
func_4275_call = mod.get_global_var('func_4275')
func_4277_call = mutated_mod.get_global_var('func_4277')
var_7174 = relay.var("var_7174", dtype = "float32", shape = (1, 378))#candidate|7174|(1, 378)|var|float32
call_7173 = func_4275_call(relay.reshape(var_7174.astype('float32'), [6, 9, 7]))
call_7175 = func_4275_call(relay.reshape(var_7174.astype('float32'), [6, 9, 7]))
func_1666_call = mod.get_global_var('func_1666')
func_1671_call = mutated_mod.get_global_var('func_1671')
var_7180 = relay.var("var_7180", dtype = "uint8", shape = (728,))#candidate|7180|(728,)|var|uint8
const_7181 = relay.const([4,7,1,8,1,6,5,-2,10,-5,1,-10,10,2,-6,9,9,7,8,-1,-1,-9,-8,1,-5,1,-8,5,-3,-7,-3,8,-2,3,2,1,2,2,-10,-10,-1,-3,5,8,6,-6,2,3,1,-4,-10,10,4,4,7,1,8,-9,-3,-1,-2,9,3,8,6,10,-6,9,-2,-5,10,9,9,9,4,-2,6,-4,3,-4,-5,-6,3,-2,10,-4,-3,-6,-10,6,-4,-2,-2,-1,8,2,8,-6,-3,5,-6,-4,1,-1,9,-7,-8,5,-5,2,2,9,-4,-10,-3,-2,6,-8,-8,-10,-10,1,-5,-7,3,-8,-7,-4,3,-2,8,5,-2,3,-6,6,-9,4,-3,8,4,10,2,4,5,2,-10,9,2,1,-4,-3,-5,-9,-10,4,-1,-5,8,10,5,-1,1,-6,-2,2,-5,-1,2,9,-4,-3,-9,10,8,-1,4,-8,1,-9,-1,1,5,-6,-9,-8,10,-8,10,6,-9,-2,10,9,2,-6,-8,8,-8,-10,-9,-2,2,6,9,1,-1,-3,1,-10,-10,7,-5,1,9,-2,2,5,-5,7,5,4,-10,-4,-8,7,3,6,-9,3,10,6,1,-7,4,-2,1,4,-4,-4,5,2,5,7,-7,-4,8,-3,1,5,4,-4,-5,6,-9,4,2,-3,8,-1,-2,3,4,1,6,3,-3,-6,-7,10,3,-9,1,-9,4,3,-4,-8,-4,4,-4,1,5,-8,10,-6,1,7,7,-9,8,9,-10,-10,5,-4,2,6,3,-8,1,5,9,-2,-9,-9,4,-7,-4,-1,-3,-8,2,-10,8,-7,2,-1,-5,-9,-7,-1,6,-7,7,9,-3,-2,-1,-10,-10,9,3,5,6,-4,4,-4,-1,3,1,7,1,8,2,2,-9,6,-3,-1,6,-2,9,5,8,-10,-3,4,-6,5,-2,-4,8,-4,10,9,-1,10,-6,-1,-4,5,8,9,-4,6,1,-9,-9,-1,-8,-6,-1,8,3,6,-10,3,2,4,8,2,-9,10,5,6,2,-4,-10,2,2,9,9,-2,7,5,-7,7,-9,3,-8,7,2,-3,-4,4,-1,1,-6,-8,-2,-10,-3,6,-4,6,-9,10,-6,4,5,9,-2,5,3,2,-10,6,-9,-5,-3,-5,-8,6,9,6,-9,-2,-5,-2,2,-6,6,6,-4,10,-4,10,1,7,-7,6,10,-8,4,-5,-3,1,-3,-9,-9,-2,4,-6,9,7,-6,3,-10,9,2,2,-5,9,9,-2,-6,1,10,7,1,-9,-6,3,7,9,7,7,6,9,3,-6,-8,9,4,-9,-9,-2,-3,10,-6,-9,2,-5,1,6,5,-1,8,-3,5,9,-2,-8,5,-5,8,-6,-10,-9,-4,7,6,4,-9,6,1,-9,-8,10,-6,6,8,4,-4,-1,9,-10,5,9,-3,7,2,-10,2,4,4,-3,4,4,-2,10,4,-8,-6,-4,-4,6,8,6,4,9,-10,4,-10,5,5,3,5,-10,-8,3,-7,6,3,-5,-2,8,-7,-9,3,8,9,-9,3,-9,-6,-1,-9,8,10,10,-10,-5,1,3,-8,-3,-2,-5,-2,6,-5,10,-7,-8,2,9,6,-8,-10,2,1,8,6,8,6,-7,-4,-6,3,-8,-4,6,4,1,-2,3,8,7,-3,-3,3,-1,-7,6,3,-5,-2,10,-5,-10,-4,10,-4,-6,-4,-5,9,1,-5,5,2,8,1,2,7,-2,-4,-2,1,-5,-7,1,-8,-3,1,2,8,-9,-8,-6,2,-7,-2,5,5,6,2,-9,10,-5,9,-6,9,-9,-8,-3,3,-9,7,6,-3,7,2,6,-9,4,-10,7,8,4,1,8,-7,8,-10,7,9,-1,-1,4,7,10,-8,7,-2,-2,10,6,-7,-1,-1,10,-4,10,9,-5,-1,6,-1,5,-3,8,-9,9,1,4,-10,-1,-7,-10,-4,-3,-2,-4,9,8,-8,-5,3,4,-6,5,3,2,4,6,-9,-2,-7,7,6,8,-4,-1,-9,-10,-3,2,-8,8,6,-1,-3,9,-1,-6,2,3,10,-2,10,5,8,3,-2,9,5,3,4,1,-8,4,-2,-5,-10,-3,-10,6,-6,3,10,-3,3,6,-10,7,-4,6,-8,10,10,10,10,8,-5,-3,5,9,-2,9,1,-9,-7,-1,-8,2,-4,7,-8,-1,8,-7,8,2,10,5,5,6,-1,-6,-8,8,-3,-8,-10,6,-1,-2,9,-2,-5,-2,-2,-4,-5,-1,-1,5,-4,8,1,3,-7,2,8,6,-2,-4,7,7,-10,-3,7,-6,-10,-6,-8,-3,-3,10,-3,-5,-5,9,-8,-3,5,9,5,-3,-2,8,-10,-5,-7,4,-3,5,9,1,-10,-4,-2,7,10,6,10,2,-6,3,-3,-5,6,-8,4,10,6,9,9,-9,5,-9,-9,5,9,1,4,8,-8,5,-6,7,3,1,-1,8,-6,-3,9,2,-3,-10,1,-7,6,10,-10,-5,-3,2,-9,-2,-9,-1,2,-8,8,-3,8,7,-3,8,-6,-4,-1,4,9,6,2,8,-5,-10,4,4,-3,-6,10,10,8,6,2,-1,8,3,-7,8,9,6,1,-7,-3,-5,-8,-8,10,-6,-5,-7,4,-7,-1,2,-10,5,-8,-10,-7,3,-9,-2,6,3,-4,-6,-8,-9,5,9,10,1,-6,9,5,1,-5,-2,10,2,-4,2,1,-1,1,-4,-5,10,-7,7,3,5,-10,8,-2,5,1,10,-7,10,4,-2,10,-2,-3,8,-8,3,-10,1,-3,2,2,-8,4,10,4,8,-1,1,-1,1,2,9,-7,5,-7,-6,8,1,-1,-1,10,-1,10,-7,10,10,2,-5,-2,-8,9,9,7,-1,-8,5,2,8,-7,2,-5,-9,-4,3,-7,4,-5,3,-2,10,9,-7,-1,-2,2,-6,-8,3,1,7,-8,-6,-3,-5,-5,4,-2,4,6,4,10,6,-6,10,-4,7,-8,-7,2,-6,8,-1,-1,-6,1,-6,9,-10,10,2,9,-7,4,9,-7,5,7,8,10,-6,5,3,5,-10,-5,10,-4,2,1,6,-8,-5,-8,2,10,-1,9,10,-9,-8,3,-10,-5,4,4,5,-2,5,-3,10,-7,8,-6,10,9,4,6,-8,6,6,-4,2,-1,-8,5,10,10,8,6,-3,-5,-6,1,-3,-6,7,-10,-7,-5,7,-4,10,5,-10,-5,6,10,-3,8,5,7,-5,8,-7,-9,-3,-1,5,-10,-7,-7,-6,-6,5,-7,7,2,-10,-6,-5,3,-5,10,10,-6,6,-1,10,1,3,-10,1,-4,4,8,-4,7,5,1,9,4,1,-8,-5,10,9,2,-4,3,-6,-7,-1,-10,-6,-6,8,-2,5,4,1,2,6,3,10,-5,-6,9,-1,-6,9,3,1,-8,7,8,6,1,-4,9,8,-2,-10,-4,9,-9,-1,8,10,-10,-6,7,10,5,2,-10,1,7,-5,4,10,-4,8,2,-8,6,-1,-7,3,-5,-7,5,8,-9,2,9,-7,-2,-7,-6,7,8,-7,8,-8,-4,7,2,3,8,-3,7,10,-6,4,-9,-3,8,5,-9,7,7,-5,9,8,-5,-4,10,4,10,-5,-10,9,8,3,4,-5,6,-10,9,-4,-9,-1,-2,-5,4,3,-10,-1,4,-10,-4,1,-6,-6,-9,1,9,-8,-6,3,-5,-1,9,-7,-6,1,-1,-1,-3,2,-7,1,5,-7,2,-1,6,-6,-6,8,-10,-3,1,-10,10,8,8,-3,7,-6,-2,10,10,5,-8,9,1,-3,-7,7,-8,5,4,-9,-10,2,1,-1,7,-9,8,5,2,-2,-2,6,-3,3,1,-8,6,-6,-3,10,-3,-5,8,10,9,-9,-8,8,-8,-1,-5,-1,-1,10,5,4,-8,9,-10,-6,-9,-9,-1,-10,-9,7,2,-9,-6,6,8,9,10,3,-7,10,-7,-4,-5,-5,-7,-10,-2,-1,7,-10,-7,4,9,1,10,3,-2,4,-3,-4,3,9,-5,6,8,-1,-6,-4,2,-2,-9,-10,2,-10,4,5,-10,-3,-7,-8,-4,9,4,5,-3,10,2,2,-3,10,8,3,2], dtype = "int16")#candidate|7181|(1575,)|const|int16
var_7182 = relay.var("var_7182", dtype = "float32", shape = (50, 9))#candidate|7182|(50, 9)|var|float32
call_7179 = relay.TupleGetItem(func_1666_call(relay.reshape(var_7180.astype('uint8'), [8, 7, 13]), relay.reshape(const_7181.astype('int16'), [1575,]), relay.reshape(var_7182.astype('float32'), [450,]), ), 5)
call_7183 = relay.TupleGetItem(func_1671_call(relay.reshape(var_7180.astype('uint8'), [8, 7, 13]), relay.reshape(const_7181.astype('int16'), [1575,]), relay.reshape(var_7182.astype('float32'), [450,]), ), 5)
output = relay.Tuple([uop_7169,call_7173,var_7174,call_7179,var_7180,const_7181,var_7182,])
output2 = relay.Tuple([uop_7171,call_7175,var_7174,call_7183,var_7180,const_7181,var_7182,])
func_7184 = relay.Function([var_7164,var_7174,var_7180,var_7182,], output)
mod['func_7184'] = func_7184
mod = relay.transform.InferType()(mod)
mutated_mod['func_7184'] = func_7184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7184_call = mutated_mod.get_global_var('func_7184')
var_7186 = relay.var("var_7186", dtype = "float64", shape = (7, 13, 7))#candidate|7186|(7, 13, 7)|var|float64
var_7187 = relay.var("var_7187", dtype = "float32", shape = (1, 378))#candidate|7187|(1, 378)|var|float32
var_7188 = relay.var("var_7188", dtype = "uint8", shape = (728,))#candidate|7188|(728,)|var|uint8
var_7189 = relay.var("var_7189", dtype = "float32", shape = (50, 9))#candidate|7189|(50, 9)|var|float32
call_7185 = func_7184_call(var_7186,var_7187,var_7188,var_7189,)
output = call_7185
func_7190 = relay.Function([var_7186,var_7187,var_7188,var_7189,], output)
mutated_mod['func_7190'] = func_7190
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7195 = relay.const([[[-2.300167,3.014966],[4.246521,8.857430],[5.776080,7.945786],[-8.975182,-8.388302],[8.888011,4.114656],[8.122226,-2.094739],[-7.307291,5.357974],[-8.308107,4.326577],[-1.775765,6.356332],[-0.106257,-5.980142],[0.084135,-9.315319],[4.578918,7.572357],[-6.619506,9.593756],[-6.409492,-9.280166],[5.088200,5.354713]],[[-0.329739,-6.785589],[-8.778131,3.877745],[0.282745,-3.677697],[0.118932,-5.092207],[-2.759231,-8.261742],[-5.928957,-8.290194],[9.581049,-5.238909],[2.592481,1.352914],[-1.371888,-8.316802],[0.452490,3.610047],[9.012425,9.598942],[1.805677,7.329142],[-8.393057,-7.999119],[-4.689808,1.133163],[2.889874,-2.256291]],[[-0.512357,-1.326323],[-1.929836,8.410460],[-7.541777,-3.822734],[-2.015920,5.552919],[8.032768,5.343069],[-7.675086,-5.285062],[5.996863,-8.516181],[7.607818,8.770744],[-7.883827,-2.096049],[-8.040658,-6.927891],[2.018056,-7.628501],[2.160228,4.789684],[2.883346,-1.100085],[-5.793226,-1.720358],[-3.235223,-8.477655]],[[0.590832,3.240073],[8.555729,-8.397564],[4.709940,8.482420],[6.808925,4.650791],[2.197845,8.375720],[6.772056,-3.445160],[6.785959,9.785291],[7.420479,7.277107],[9.808256,4.016235],[4.427289,-2.785865],[-0.159822,4.075733],[-0.266670,-2.897332],[5.341231,-4.995420],[1.743854,-9.824860],[0.932334,7.879878]],[[3.454582,2.828456],[6.995822,5.377714],[9.584055,-8.823049],[5.790299,8.693712],[-2.651860,1.860895],[-5.968416,-4.340640],[-4.442470,-7.958654],[7.113860,4.256730],[-8.089982,1.226163],[7.356640,-9.899996],[2.537150,-9.641212],[-4.011625,-8.091468],[-7.458107,-7.368914],[7.998545,-5.813719],[6.552706,3.841174]],[[-0.180112,2.524050],[2.698115,3.439029],[-5.390615,4.525560],[-8.934225,-8.197156],[-5.025888,6.622163],[6.295247,0.359059],[-8.496374,-1.403747],[-8.230011,-5.899227],[-9.057949,1.290696],[2.680640,-8.543432],[7.541804,6.260735],[-2.501229,-2.411109],[-8.869375,4.619853],[-5.509856,-2.863773],[-1.408914,-6.047303]],[[-6.794083,-9.018179],[1.495138,-0.051207],[-9.889738,-1.751078],[1.471989,9.202029],[3.964640,-7.967715],[1.801683,5.933268],[-7.189138,-6.477937],[1.724086,0.339755],[-9.975736,-6.803280],[3.434346,-2.896295],[-4.974670,4.526505],[-3.078192,9.205637],[6.077813,2.124556],[3.408427,-1.051281],[-0.189777,-6.703017]],[[1.406086,4.371643],[4.055218,0.649653],[-7.890574,-4.584566],[-4.535330,-3.419110],[-1.914136,3.803898],[1.217921,-4.379913],[1.628195,-9.440391],[-1.630501,7.514343],[-2.373784,6.847179],[5.100728,4.070629],[-5.589787,-3.712420],[7.020468,3.927542],[-3.404302,0.539714],[8.847709,-3.892992],[-0.257062,-4.012102]],[[8.196506,0.996459],[-3.028214,-8.328088],[1.931577,2.283781],[9.272383,3.552318],[5.459429,8.677338],[0.868178,9.042574],[-7.373273,2.934397],[4.743743,4.497768],[-2.977477,-9.124552],[0.140860,-7.278833],[-6.979228,-8.883321],[3.143572,9.852834],[-2.215044,-3.459976],[5.489714,-1.917345],[6.690159,4.389448]],[[3.011921,8.985502],[8.004407,-1.388161],[-3.628081,0.337728],[8.613318,4.605114],[9.323647,9.741741],[4.022585,8.325732],[2.408968,-1.425328],[-8.790500,0.586155],[7.174577,2.627754],[1.466842,8.068536],[-0.734933,-8.290774],[8.687220,-2.020553],[-7.446081,-3.908663],[7.336600,9.617512],[-1.736565,3.319795]],[[6.721927,-2.409338],[3.509173,7.091403],[-4.428032,0.479468],[5.673688,-4.520812],[7.014665,-7.021691],[-8.179153,5.014312],[-8.796701,-8.311504],[-1.109900,7.890961],[0.386336,-1.151858],[2.977028,1.221043],[5.784746,-0.253399],[-2.729569,4.323043],[0.114391,-0.986246],[-5.678375,0.140271],[-1.071572,5.469277]]], dtype = "float64")#candidate|7195|(11, 15, 2)|const|float64
uop_7196 = relay.sqrt(const_7195.astype('float64')) # shape=(11, 15, 2)
output = uop_7196
output2 = uop_7196
func_7200 = relay.Function([], output)
mod['func_7200'] = func_7200
mod = relay.transform.InferType()(mod)
mutated_mod['func_7200'] = func_7200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7200_call = mutated_mod.get_global_var('func_7200')
call_7201 = func_7200_call()
output = call_7201
func_7202 = relay.Function([], output)
mutated_mod['func_7202'] = func_7202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6426_call = mod.get_global_var('func_6426')
func_6427_call = mutated_mod.get_global_var('func_6427')
call_7226 = relay.TupleGetItem(func_6426_call(), 0)
call_7227 = relay.TupleGetItem(func_6427_call(), 0)
output = call_7226
output2 = call_7227
func_7231 = relay.Function([], output)
mod['func_7231'] = func_7231
mod = relay.transform.InferType()(mod)
output = func_7231()
func_7232 = relay.Function([], output)
mutated_mod['func_7232'] = func_7232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3430_call = mod.get_global_var('func_3430')
func_3431_call = mutated_mod.get_global_var('func_3431')
call_7255 = func_3430_call()
call_7256 = func_3430_call()
output = relay.Tuple([call_7255,])
output2 = relay.Tuple([call_7256,])
func_7281 = relay.Function([], output)
mod['func_7281'] = func_7281
mod = relay.transform.InferType()(mod)
mutated_mod['func_7281'] = func_7281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7281_call = mutated_mod.get_global_var('func_7281')
call_7282 = func_7281_call()
output = call_7282
func_7283 = relay.Function([], output)
mutated_mod['func_7283'] = func_7283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6317_call = mod.get_global_var('func_6317')
func_6318_call = mutated_mod.get_global_var('func_6318')
call_7287 = relay.TupleGetItem(func_6317_call(), 0)
call_7288 = relay.TupleGetItem(func_6318_call(), 0)
func_3021_call = mod.get_global_var('func_3021')
func_3023_call = mutated_mod.get_global_var('func_3023')
const_7321 = relay.const([-9.847952,5.023303,6.791462,9.649308,-1.189603,-6.448090,-2.697193,-2.664798,-1.206386,8.974184,-6.578058,2.722580,-9.741528,7.132727,1.212968,-0.659203,5.378178,0.610860,2.767487,-8.180649,6.742983,-1.217145,3.842687,-1.789849,-2.402078,8.207010,-4.881662,7.023511,-1.911048,-3.572381,-5.849544,1.030054,-7.272022,-3.376945,1.563092,5.675409,2.945693,-6.451873,-7.159554,-0.439840,-4.515426,-9.030934,-2.911333,8.510540,-5.124560,-2.828555,-4.482069,9.606226,-2.318943,1.017997,-2.086291,-4.094923,-2.370403,-6.900016,7.088487,-0.142747,-5.502422,8.249975,-7.285646,9.987125,-2.431560,4.329654,7.233252,-5.459287,0.005268,-2.774022,-9.997926,2.131220,2.832879,-3.991755,2.224142,6.012282,0.058412,-2.737115,7.830882,-2.896080,-5.300502,4.920847,-8.247389,0.389575,1.814211,0.916984,5.842060,-3.672186,4.185563,1.877059,4.642307,-7.279613,3.349465,-7.189381,1.169237,0.578255,6.912333,5.350540,-3.508369,3.758508,-1.634673,0.538130,9.240407,7.790171,-1.467184,7.824103,2.407768,-9.388967,9.701644,1.901137,-9.415501,-6.753029,3.665800,3.568883,-6.368509,9.593332,-4.056489,-1.380537,6.227774,-4.659144,5.910866,8.855576,7.368513,1.630973,6.386310,6.744112,4.471253,6.071105,-7.429126,-8.565601,4.249278,4.579476,7.865474,6.957501,3.561225,-2.223185,-8.713170,9.468867,-4.657514,-9.565408,-7.974416,7.791348,9.754761,-4.759623,5.596423,-0.991604,1.585805,-5.940644,-6.413883,7.237809,0.709151,-2.050215,3.231823,-8.572683,-7.493729,9.608744,-5.388912,1.039412,0.970898,0.782344,-4.925400,2.459064,-7.786434,-1.340491,-4.495813,-5.208192,-8.417284,2.614267,7.935455,0.144966,-3.876533,-7.924455,9.130512,-3.821928,7.784979,9.418519,3.808895,9.010799,1.486904,-7.304599,7.458194,3.067062,7.189995,-6.381629,-4.893613,3.684020,-0.555613,-8.957162,0.219621,6.724506,-4.858371,-8.192474,5.611419,3.185367,-9.959144,-7.572273,9.568618,9.381677,-7.766660,5.753424,2.981746,0.402163,-5.338431,2.193323,-0.995816,-9.437453,2.270655,2.969101,1.636140,0.829414,-4.158780,0.306320,-9.016005,7.992368,-3.913350,5.711907,9.610856,-9.171167,-0.551517,2.921540,-8.059741,-8.665364,-2.808545,-2.026943,-2.359452,9.423465,-1.577277,-8.725230,7.323137,7.289325,-5.497631,4.915140,-6.160969,2.900467,6.964962,2.623189,1.516018,-6.827368,0.518581,8.314526,-7.196362,3.203535,8.849032,1.152627,3.103424,5.095932,-4.461094,3.614890,-8.357654,6.593403,1.559342,3.224968,-1.948732,-8.925816,-4.378768,-6.888846,7.338102,2.755791,6.559583,6.752505,-2.064378,6.515829,-5.205083,8.545761,8.573954,-2.307710,4.637459,5.460738], dtype = "float64")#candidate|7321|(264,)|const|float64
call_7320 = relay.TupleGetItem(func_3021_call(relay.reshape(const_7321.astype('float64'), [12, 11, 2])), 5)
call_7322 = relay.TupleGetItem(func_3023_call(relay.reshape(const_7321.astype('float64'), [12, 11, 2])), 5)
output = relay.Tuple([call_7287,call_7320,const_7321,])
output2 = relay.Tuple([call_7288,call_7322,const_7321,])
func_7325 = relay.Function([], output)
mod['func_7325'] = func_7325
mod = relay.transform.InferType()(mod)
output = func_7325()
func_7326 = relay.Function([], output)
mutated_mod['func_7326'] = func_7326
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7401 = relay.var("var_7401", dtype = "int32", shape = (1, 15, 12))#candidate|7401|(1, 15, 12)|var|int32
const_7402 = relay.const([[[1,-2,-8,-3,-10,-10,-9,-1,7,10,7,7],[-4,7,-8,-6,10,-5,4,-5,6,5,2,8],[-10,-3,-6,6,-9,-10,5,7,3,6,-10,2],[-8,-3,10,4,-2,8,5,9,-8,2,-4,9],[-1,-7,-5,8,3,-4,5,-7,-4,4,-3,-3],[4,4,-6,-7,9,-9,2,-8,1,2,-1,-10],[5,4,10,9,-3,-2,-8,-6,-5,-3,-4,-4],[4,-8,6,-2,5,7,3,9,-10,5,-2,-7],[7,5,-3,-4,-6,4,4,3,1,-7,5,-10],[-9,-3,5,-9,9,4,7,-9,-2,-7,10,-8],[-7,5,10,-6,-2,1,8,2,6,-9,3,5],[2,4,9,3,8,9,5,9,2,-7,-10,8],[-4,-8,-5,-4,5,9,1,-2,-1,-9,4,-6],[-7,-9,-3,-4,5,3,5,7,5,-5,-7,7],[6,8,3,-10,-8,-1,7,-5,-7,2,-8,-3]],[[-4,-1,-3,-3,-4,3,-5,-2,-4,-4,-8,3],[9,-9,-4,-10,-1,1,9,7,5,5,-4,2],[7,9,5,1,9,1,-4,-2,-1,-9,9,8],[-7,-3,-7,9,1,9,3,-1,2,6,2,9],[2,-6,5,6,-6,-2,-6,-6,2,6,-5,-6],[9,-3,9,-4,1,4,5,-9,-1,-3,4,7],[-5,1,-9,7,8,-9,-3,10,7,3,5,3],[4,4,-5,6,-3,-8,-4,2,-8,-1,-6,-6],[-6,-4,-10,7,-5,4,2,-8,4,9,4,2],[-2,2,5,-10,-8,1,3,3,-9,-6,4,-5],[-1,-8,4,4,2,-4,5,-5,-10,2,-4,-1],[-10,1,-2,-4,-1,-5,-10,-2,6,-9,-2,5],[-3,-5,-10,8,-5,5,7,10,2,4,-6,-6],[4,5,-2,-6,-7,-9,-9,-10,10,-2,7,-7],[-9,4,-9,10,-6,7,-7,-2,-6,-5,10,1]]], dtype = "int32")#candidate|7402|(2, 15, 12)|const|int32
bop_7403 = relay.bitwise_or(var_7401.astype('int32'), const_7402.astype('int32')) # shape=(2, 15, 12)
output = relay.Tuple([bop_7403,])
output2 = relay.Tuple([bop_7403,])
func_7409 = relay.Function([var_7401,], output)
mod['func_7409'] = func_7409
mod = relay.transform.InferType()(mod)
mutated_mod['func_7409'] = func_7409
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7410 = relay.var("var_7410", dtype = "int32", shape = (1, 15, 12))#candidate|7410|(1, 15, 12)|var|int32
func_7409_call = mutated_mod.get_global_var('func_7409')
call_7411 = func_7409_call(var_7410)
output = call_7411
func_7412 = relay.Function([var_7410], output)
mutated_mod['func_7412'] = func_7412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4128_call = mod.get_global_var('func_4128')
func_4130_call = mutated_mod.get_global_var('func_4130')
call_7437 = func_4128_call()
call_7438 = func_4128_call()
func_7077_call = mod.get_global_var('func_7077')
func_7078_call = mutated_mod.get_global_var('func_7078')
call_7439 = relay.TupleGetItem(func_7077_call(), 1)
call_7440 = relay.TupleGetItem(func_7078_call(), 1)
func_2858_call = mod.get_global_var('func_2858')
func_2859_call = mutated_mod.get_global_var('func_2859')
call_7447 = func_2858_call()
call_7448 = func_2858_call()
func_1928_call = mod.get_global_var('func_1928')
func_1931_call = mutated_mod.get_global_var('func_1931')
var_7450 = relay.var("var_7450", dtype = "bool", shape = (1080,))#candidate|7450|(1080,)|var|bool
var_7451 = relay.var("var_7451", dtype = "int16", shape = (1575, 1))#candidate|7451|(1575, 1)|var|int16
call_7449 = relay.TupleGetItem(func_1928_call(relay.reshape(var_7450.astype('bool'), [10, 9, 12]), relay.reshape(var_7451.astype('int16'), [105, 15]), ), 3)
call_7452 = relay.TupleGetItem(func_1931_call(relay.reshape(var_7450.astype('bool'), [10, 9, 12]), relay.reshape(var_7451.astype('int16'), [105, 15]), ), 3)
uop_7457 = relay.sqrt(var_7451.astype('float32')) # shape=(1575, 1)
bop_7472 = relay.bitwise_and(uop_7457.astype('int64'), call_7447.astype('int64')) # shape=(1575, 450)
bop_7475 = relay.bitwise_and(uop_7457.astype('int64'), call_7448.astype('int64')) # shape=(1575, 450)
bop_7486 = relay.left_shift(var_7450.astype('uint64'), uop_7457.astype('uint64')) # shape=(1575, 1080)
output = relay.Tuple([call_7437,call_7439,call_7449,bop_7472,bop_7486,])
output2 = relay.Tuple([call_7438,call_7440,call_7452,bop_7475,bop_7486,])
func_7495 = relay.Function([var_7450,var_7451,], output)
mod['func_7495'] = func_7495
mod = relay.transform.InferType()(mod)
var_7496 = relay.var("var_7496", dtype = "bool", shape = (1080,))#candidate|7496|(1080,)|var|bool
var_7497 = relay.var("var_7497", dtype = "int16", shape = (1575, 1))#candidate|7497|(1575, 1)|var|int16
output = func_7495(var_7496,var_7497,)
func_7498 = relay.Function([var_7496,var_7497,], output)
mutated_mod['func_7498'] = func_7498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2410_call = mod.get_global_var('func_2410')
func_2411_call = mutated_mod.get_global_var('func_2411')
call_7532 = relay.TupleGetItem(func_2410_call(), 0)
call_7533 = relay.TupleGetItem(func_2411_call(), 0)
output = call_7532
output2 = call_7533
func_7540 = relay.Function([], output)
mod['func_7540'] = func_7540
mod = relay.transform.InferType()(mod)
output = func_7540()
func_7541 = relay.Function([], output)
mutated_mod['func_7541'] = func_7541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6126_call = mod.get_global_var('func_6126')
func_6127_call = mutated_mod.get_global_var('func_6127')
call_7612 = relay.TupleGetItem(func_6126_call(), 0)
call_7613 = relay.TupleGetItem(func_6127_call(), 0)
output = call_7612
output2 = call_7613
func_7624 = relay.Function([], output)
mod['func_7624'] = func_7624
mod = relay.transform.InferType()(mod)
output = func_7624()
func_7625 = relay.Function([], output)
mutated_mod['func_7625'] = func_7625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2765_call = mod.get_global_var('func_2765')
func_2767_call = mutated_mod.get_global_var('func_2767')
call_7638 = relay.TupleGetItem(func_2765_call(), 1)
call_7639 = relay.TupleGetItem(func_2767_call(), 1)
func_5578_call = mod.get_global_var('func_5578')
func_5580_call = mutated_mod.get_global_var('func_5580')
var_7646 = relay.var("var_7646", dtype = "float64", shape = (256,))#candidate|7646|(256,)|var|float64
call_7645 = relay.TupleGetItem(func_5578_call(relay.reshape(var_7646.astype('float64'), [8, 8, 4])), 2)
call_7647 = relay.TupleGetItem(func_5580_call(relay.reshape(var_7646.astype('float64'), [8, 8, 4])), 2)
output = relay.Tuple([call_7638,call_7645,var_7646,])
output2 = relay.Tuple([call_7639,call_7647,var_7646,])
func_7650 = relay.Function([var_7646,], output)
mod['func_7650'] = func_7650
mod = relay.transform.InferType()(mod)
mutated_mod['func_7650'] = func_7650
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7651 = relay.var("var_7651", dtype = "float64", shape = (256,))#candidate|7651|(256,)|var|float64
func_7650_call = mutated_mod.get_global_var('func_7650')
call_7652 = func_7650_call(var_7651)
output = call_7652
func_7653 = relay.Function([var_7651], output)
mutated_mod['func_7653'] = func_7653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2198_call = mod.get_global_var('func_2198')
func_2199_call = mutated_mod.get_global_var('func_2199')
call_7671 = relay.TupleGetItem(func_2198_call(), 0)
call_7672 = relay.TupleGetItem(func_2199_call(), 0)
output = call_7671
output2 = call_7672
func_7679 = relay.Function([], output)
mod['func_7679'] = func_7679
mod = relay.transform.InferType()(mod)
output = func_7679()
func_7680 = relay.Function([], output)
mutated_mod['func_7680'] = func_7680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5268_call = mod.get_global_var('func_5268')
func_5270_call = mutated_mod.get_global_var('func_5270')
call_7847 = func_5268_call()
call_7848 = func_5268_call()
var_7850 = relay.var("var_7850", dtype = "float64", shape = (7, 13, 7))#candidate|7850|(7, 13, 7)|var|float64
bop_7851 = relay.logical_or(call_7847.astype('bool'), relay.reshape(var_7850.astype('bool'), relay.shape_of(call_7847))) # shape=(7, 13, 7)
bop_7854 = relay.logical_or(call_7848.astype('bool'), relay.reshape(var_7850.astype('bool'), relay.shape_of(call_7848))) # shape=(7, 13, 7)
func_5973_call = mod.get_global_var('func_5973')
func_5974_call = mutated_mod.get_global_var('func_5974')
call_7856 = func_5973_call()
call_7857 = func_5973_call()
output = relay.Tuple([bop_7851,call_7856,])
output2 = relay.Tuple([bop_7854,call_7857,])
func_7868 = relay.Function([var_7850,], output)
mod['func_7868'] = func_7868
mod = relay.transform.InferType()(mod)
mutated_mod['func_7868'] = func_7868
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7869 = relay.var("var_7869", dtype = "float64", shape = (7, 13, 7))#candidate|7869|(7, 13, 7)|var|float64
func_7868_call = mutated_mod.get_global_var('func_7868')
call_7870 = func_7868_call(var_7869)
output = call_7870
func_7871 = relay.Function([var_7869], output)
mutated_mod['func_7871'] = func_7871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4852_call = mod.get_global_var('func_4852')
func_4854_call = mutated_mod.get_global_var('func_4854')
call_7875 = relay.TupleGetItem(func_4852_call(), 0)
call_7876 = relay.TupleGetItem(func_4854_call(), 0)
output = call_7875
output2 = call_7876
func_7887 = relay.Function([], output)
mod['func_7887'] = func_7887
mod = relay.transform.InferType()(mod)
mutated_mod['func_7887'] = func_7887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7887_call = mutated_mod.get_global_var('func_7887')
call_7888 = func_7887_call()
output = call_7888
func_7889 = relay.Function([], output)
mutated_mod['func_7889'] = func_7889
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7890 = relay.var("var_7890", dtype = "float32", shape = (9, 14, 7))#candidate|7890|(9, 14, 7)|var|float32
var_7891 = relay.var("var_7891", dtype = "float32", shape = (9, 14, 7))#candidate|7891|(9, 14, 7)|var|float32
bop_7892 = relay.power(var_7890.astype('float32'), relay.reshape(var_7891.astype('float32'), relay.shape_of(var_7890))) # shape=(9, 14, 7)
uop_7896 = relay.tan(var_7891.astype('float64')) # shape=(9, 14, 7)
output = relay.Tuple([bop_7892,uop_7896,])
output2 = relay.Tuple([bop_7892,uop_7896,])
F = relay.Function([var_7890,var_7891,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7890,var_7891,], output2)
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
