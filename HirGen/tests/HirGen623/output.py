import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_28 = relay.const([[-2],[2],[9],[-7],[7],[3],[1],[6],[-7],[5],[-7],[10],[4],[-10],[-1]], dtype = "int16")#candidate|28|(15, 1)|const|int16
var_29 = relay.var("var_29", dtype = "int16", shape = (15, 1))#candidate|29|(15, 1)|var|int16
bop_30 = relay.bitwise_or(const_28.astype('int16'), relay.reshape(var_29.astype('int16'), relay.shape_of(const_28))) # shape=(15, 1)
output = relay.Tuple([bop_30,])
output2 = relay.Tuple([bop_30,])
func_34 = relay.Function([var_29,], output)
mod['func_34'] = func_34
mod = relay.transform.InferType()(mod)
mutated_mod['func_34'] = func_34
mutated_mod = relay.transform.InferType()(mutated_mod)
var_35 = relay.var("var_35", dtype = "int16", shape = (15, 1))#candidate|35|(15, 1)|var|int16
func_34_call = mutated_mod.get_global_var('func_34')
call_36 = func_34_call(var_35)
output = call_36
func_37 = relay.Function([var_35], output)
mutated_mod['func_37'] = func_37
mutated_mod = relay.transform.InferType()(mutated_mod)
const_119 = relay.const([[[-10,-3,-8],[-10,-5,-5],[-8,-7,-7],[5,3,-10],[9,-6,-5],[-2,2,6],[10,-8,10],[-7,6,-3],[7,3,-7],[-2,2,-7],[-1,-4,6],[4,7,2],[3,10,-3],[6,-10,-1],[9,-3,3]],[[10,3,-6],[5,7,-4],[-3,-8,8],[-5,-3,-1],[-2,-2,-3],[-9,9,-8],[-8,-9,-7],[4,9,3],[5,-4,-3],[-5,-7,-1],[1,5,9],[7,8,-4],[8,-7,2],[-6,7,5],[5,6,8]],[[4,7,-1],[5,-6,5],[-8,-2,2],[2,-10,8],[-1,-7,6],[-4,5,2],[-10,4,-7],[-7,-2,7],[-2,-1,-2],[-10,-1,7],[4,-10,3],[-5,-8,-10],[-9,-2,-6],[6,2,10],[6,4,-9]],[[-7,-4,-2],[-10,1,-7],[4,8,7],[-7,-1,10],[-10,3,6],[-6,-7,-9],[-9,-5,6],[3,-7,8],[-4,9,-3],[-9,7,-8],[8,-3,6],[3,2,10],[-9,8,2],[4,-10,-3],[1,-5,-6]],[[1,-8,-6],[-10,-2,6],[-10,2,4],[3,-2,-8],[7,7,-2],[-6,-4,9],[9,-10,2],[10,4,10],[-8,4,8],[-4,-5,-7],[-1,-10,-7],[8,10,6],[5,-2,10],[7,-6,7],[-4,9,2]],[[-8,10,10],[9,-5,6],[-1,-9,-8],[-6,6,-5],[-6,-6,10],[-2,10,8],[-3,-8,8],[-10,-4,3],[-8,6,-2],[9,-4,6],[2,4,-2],[-2,9,-3],[-3,-7,2],[9,-10,-3],[10,4,-4]],[[7,8,8],[4,-7,1],[10,-3,-10],[-7,-4,-8],[3,7,-1],[8,9,-9],[-10,-8,-8],[8,-2,4],[-7,-5,-10],[-8,-10,-2],[7,10,8],[2,4,6],[8,9,7],[4,-4,5],[-1,-9,-7]],[[3,-1,-10],[2,-8,2],[8,7,10],[9,-10,-2],[-9,7,5],[6,-7,-2],[-5,-9,-1],[-6,10,6],[-9,-1,-10],[-3,7,8],[3,-1,3],[9,8,-3],[-8,-9,2],[8,4,10],[4,4,3]],[[-5,-6,-9],[2,8,-6],[10,-10,4],[-8,-5,2],[6,-1,9],[-4,2,-3],[-10,-1,-4],[9,-2,-4],[-3,9,-5],[-7,8,3],[4,2,-9],[1,1,-10],[-10,10,10],[-8,-6,-2],[9,4,-9]]], dtype = "uint16")#candidate|119|(9, 15, 3)|const|uint16
const_120 = relay.const([[[-4,6,5],[3,1,-6],[4,-5,6],[6,7,-3],[4,-9,3],[4,2,-9],[1,4,9],[-10,-6,9],[-4,-10,-1],[-8,-6,-3],[-6,-6,-8],[-7,8,-2],[1,-9,-6],[7,-5,1],[-1,-8,-5]],[[7,1,-2],[-8,-5,-10],[3,-8,8],[-3,4,-5],[4,3,4],[7,1,-5],[-5,2,1],[-9,-3,9],[3,-8,1],[-3,1,9],[5,-9,5],[9,-8,2],[-3,4,-9],[9,6,-10],[-3,2,-10]],[[1,10,-2],[-3,3,-4],[-9,-7,2],[7,-10,9],[7,-5,-5],[-1,-2,6],[4,-7,-1],[3,5,-4],[-7,-8,-3],[9,8,9],[10,-10,3],[-8,-7,5],[5,9,-9],[9,-5,5],[4,8,-9]],[[-5,-10,-3],[3,9,8],[10,-3,5],[4,-8,-3],[-9,-6,-8],[7,-5,-8],[-10,-2,3],[-3,3,-1],[-6,6,-6],[-6,5,3],[6,-7,-6],[9,-8,-5],[1,3,3],[-6,-1,-4],[1,-3,1]],[[-2,-7,-10],[-5,-9,2],[-3,1,10],[-2,-5,-9],[1,1,8],[3,1,-8],[2,-1,-8],[6,-7,9],[-1,4,-3],[6,-4,-9],[9,2,-9],[2,-8,4],[-6,-7,-7],[2,7,-5],[10,-6,8]],[[-7,-5,-8],[1,-8,3],[-5,4,3],[10,1,-1],[10,10,4],[-9,-7,-1],[-1,-5,1],[2,-6,-10],[10,-4,9],[-9,-5,-5],[9,3,10],[-8,-6,1],[10,5,-10],[5,-5,10],[2,-3,8]],[[-9,5,2],[-4,8,3],[9,-3,-9],[1,2,3],[-10,-3,6],[-4,-10,-7],[-4,-3,2],[10,-1,-6],[-5,-6,-3],[-2,6,9],[-9,-6,-9],[9,3,4],[8,-7,-8],[-9,9,1],[-6,6,-8]],[[-3,7,-6],[-2,8,7],[-9,7,-5],[-8,-9,2],[3,-4,-10],[-6,-1,-2],[-7,-2,-10],[-10,-5,6],[3,4,4],[-1,4,6],[8,-6,-2],[6,5,-6],[-6,-7,-5],[-8,-8,10],[8,7,-7]],[[-3,4,5],[-10,-7,6],[1,2,-2],[-10,5,3],[-9,9,1],[10,10,-5],[-2,-4,9],[4,4,7],[-3,6,-4],[7,2,-1],[9,-8,7],[-4,10,8],[1,-1,-8],[-3,-7,2],[10,7,3]]], dtype = "uint16")#candidate|120|(9, 15, 3)|const|uint16
bop_121 = relay.logical_xor(const_119.astype('uint16'), relay.reshape(const_120.astype('uint16'), relay.shape_of(const_119))) # shape=(9, 15, 3)
uop_127 = relay.log(const_119.astype('float32')) # shape=(9, 15, 3)
uop_129 = relay.asinh(const_120.astype('float32')) # shape=(9, 15, 3)
func_34_call = mod.get_global_var('func_34')
func_37_call = mutated_mod.get_global_var('func_37')
var_132 = relay.var("var_132", dtype = "int16", shape = (15,))#candidate|132|(15,)|var|int16
call_131 = relay.TupleGetItem(func_34_call(relay.reshape(var_132.astype('int16'), [15, 1])), 0)
call_133 = relay.TupleGetItem(func_37_call(relay.reshape(var_132.astype('int16'), [15, 1])), 0)
func_34_call = mod.get_global_var('func_34')
func_37_call = mutated_mod.get_global_var('func_37')
call_139 = relay.TupleGetItem(func_34_call(relay.reshape(var_132.astype('int16'), [15, 1])), 0)
call_140 = relay.TupleGetItem(func_37_call(relay.reshape(var_132.astype('int16'), [15, 1])), 0)
output = relay.Tuple([bop_121,uop_127,uop_129,call_131,var_132,call_139,])
output2 = relay.Tuple([bop_121,uop_127,uop_129,call_133,var_132,call_140,])
func_141 = relay.Function([var_132,], output)
mod['func_141'] = func_141
mod = relay.transform.InferType()(mod)
mutated_mod['func_141'] = func_141
mutated_mod = relay.transform.InferType()(mutated_mod)
var_142 = relay.var("var_142", dtype = "int16", shape = (15,))#candidate|142|(15,)|var|int16
func_141_call = mutated_mod.get_global_var('func_141')
call_143 = func_141_call(var_142)
output = call_143
func_144 = relay.Function([var_142], output)
mutated_mod['func_144'] = func_144
mutated_mod = relay.transform.InferType()(mutated_mod)
const_316 = relay.const([[[5],[-3],[10],[-2],[9],[5],[9],[10],[4],[9]],[[7],[1],[-9],[-8],[2],[-6],[-3],[-10],[10],[1]],[[-4],[-1],[8],[4],[-5],[5],[6],[-6],[7],[-1]],[[9],[-5],[-8],[-7],[-5],[-10],[-5],[-3],[-2],[-7]],[[9],[-9],[-6],[-2],[-8],[3],[2],[-10],[-3],[9]],[[-5],[8],[-1],[3],[5],[10],[-9],[-10],[1],[9]],[[7],[-7],[-10],[-9],[3],[-10],[8],[8],[-6],[-5]],[[-10],[6],[4],[-6],[8],[-6],[-5],[-3],[-7],[-5]],[[-10],[-1],[-2],[10],[-2],[2],[9],[-3],[6],[10]],[[3],[10],[-7],[3],[5],[6],[-5],[-8],[6],[7]],[[-2],[-9],[-7],[-6],[10],[-8],[1],[2],[-10],[4]],[[5],[3],[-7],[-6],[-8],[10],[-2],[-2],[1],[-3]],[[-5],[-5],[6],[6],[4],[-1],[2],[-8],[-4],[3]],[[-7],[-3],[1],[-7],[5],[-5],[-10],[1],[-10],[10]]], dtype = "uint64")#candidate|316|(14, 10, 1)|const|uint64
var_317 = relay.var("var_317", dtype = "uint64", shape = (14, 10, 15))#candidate|317|(14, 10, 15)|var|uint64
bop_318 = relay.less_equal(const_316.astype('bool'), var_317.astype('bool')) # shape=(14, 10, 15)
output = bop_318
output2 = bop_318
func_322 = relay.Function([var_317,], output)
mod['func_322'] = func_322
mod = relay.transform.InferType()(mod)
mutated_mod['func_322'] = func_322
mutated_mod = relay.transform.InferType()(mutated_mod)
var_323 = relay.var("var_323", dtype = "uint64", shape = (14, 10, 15))#candidate|323|(14, 10, 15)|var|uint64
func_322_call = mutated_mod.get_global_var('func_322')
call_324 = func_322_call(var_323)
output = call_324
func_325 = relay.Function([var_323], output)
mutated_mod['func_325'] = func_325
mutated_mod = relay.transform.InferType()(mutated_mod)
var_403 = relay.var("var_403", dtype = "float32", shape = (10, 5, 1))#candidate|403|(10, 5, 1)|var|float32
var_404 = relay.var("var_404", dtype = "float32", shape = (10, 5, 8))#candidate|404|(10, 5, 8)|var|float32
bop_405 = relay.subtract(var_403.astype('float32'), var_404.astype('float32')) # shape=(10, 5, 8)
output = relay.Tuple([bop_405,])
output2 = relay.Tuple([bop_405,])
func_417 = relay.Function([var_403,var_404,], output)
mod['func_417'] = func_417
mod = relay.transform.InferType()(mod)
mutated_mod['func_417'] = func_417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_417_call = mutated_mod.get_global_var('func_417')
var_419 = relay.var("var_419", dtype = "float32", shape = (10, 5, 1))#candidate|419|(10, 5, 1)|var|float32
var_420 = relay.var("var_420", dtype = "float32", shape = (10, 5, 8))#candidate|420|(10, 5, 8)|var|float32
call_418 = func_417_call(var_419,var_420,)
output = call_418
func_421 = relay.Function([var_419,var_420,], output)
mutated_mod['func_421'] = func_421
mutated_mod = relay.transform.InferType()(mutated_mod)
var_872 = relay.var("var_872", dtype = "bool", shape = (9, 10, 4))#candidate|872|(9, 10, 4)|var|bool
const_873 = relay.const([[[False,True,False,True],[False,True,False,True],[False,False,True,False],[False,False,False,True],[True,True,True,False],[False,False,True,True],[True,False,True,False],[True,True,False,False],[False,True,True,True],[False,True,False,True]],[[True,True,True,False],[True,False,True,False],[True,False,False,False],[False,True,True,False],[True,False,False,False],[True,True,False,False],[False,False,True,False],[True,True,True,True],[False,True,True,True],[True,False,True,False]],[[False,True,False,True],[False,True,True,True],[True,True,True,True],[False,False,True,False],[False,False,True,True],[True,False,False,True],[True,True,False,False],[True,True,True,False],[False,True,True,False],[True,False,True,False]],[[True,False,True,False],[False,False,False,False],[False,True,False,True],[False,False,False,True],[False,False,False,True],[True,True,True,True],[False,False,True,True],[False,False,False,False],[True,True,False,True],[False,False,False,False]],[[False,False,False,False],[False,False,True,False],[True,True,False,False],[False,True,False,True],[False,True,False,False],[False,False,False,True],[False,False,False,False],[True,False,False,True],[False,False,True,True],[True,False,True,False]],[[False,True,False,False],[True,False,True,True],[False,False,True,False],[False,False,True,False],[False,True,False,True],[False,True,False,False],[True,True,True,False],[False,True,False,False],[False,True,False,True],[True,False,False,True]],[[False,False,True,False],[False,False,True,False],[False,True,False,False],[False,False,False,False],[False,False,False,False],[True,True,False,True],[False,False,True,True],[False,True,True,False],[True,False,True,True],[True,False,False,True]],[[True,False,True,False],[False,True,False,False],[True,False,False,False],[True,False,False,True],[True,True,True,True],[False,False,False,False],[False,True,True,True],[True,True,False,False],[True,True,False,False],[True,False,False,False]],[[True,True,True,False],[True,True,False,False],[False,True,False,False],[True,False,False,True],[True,False,True,False],[True,True,False,True],[True,True,True,False],[True,True,False,False],[False,True,True,False],[False,True,False,False]]], dtype = "bool")#candidate|873|(9, 10, 4)|const|bool
bop_874 = relay.logical_or(var_872.astype('bool'), relay.reshape(const_873.astype('bool'), relay.shape_of(var_872))) # shape=(9, 10, 4)
func_34_call = mod.get_global_var('func_34')
func_37_call = mutated_mod.get_global_var('func_37')
var_911 = relay.var("var_911", dtype = "int16", shape = (15, 1))#candidate|911|(15, 1)|var|int16
call_910 = relay.TupleGetItem(func_34_call(relay.reshape(var_911.astype('int16'), [15, 1])), 0)
call_912 = relay.TupleGetItem(func_37_call(relay.reshape(var_911.astype('int16'), [15, 1])), 0)
output = relay.Tuple([bop_874,call_910,var_911,])
output2 = relay.Tuple([bop_874,call_912,var_911,])
func_934 = relay.Function([var_872,var_911,], output)
mod['func_934'] = func_934
mod = relay.transform.InferType()(mod)
var_935 = relay.var("var_935", dtype = "bool", shape = (9, 10, 4))#candidate|935|(9, 10, 4)|var|bool
var_936 = relay.var("var_936", dtype = "int16", shape = (15, 1))#candidate|936|(15, 1)|var|int16
output = func_934(var_935,var_936,)
func_937 = relay.Function([var_935,var_936,], output)
mutated_mod['func_937'] = func_937
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1159 = relay.var("var_1159", dtype = "bool", shape = (6, 1, 8))#candidate|1159|(6, 1, 8)|var|bool
var_1160 = relay.var("var_1160", dtype = "bool", shape = (6, 10, 8))#candidate|1160|(6, 10, 8)|var|bool
bop_1161 = relay.logical_or(var_1159.astype('bool'), var_1160.astype('bool')) # shape=(6, 10, 8)
bop_1169 = relay.power(var_1160.astype('float32'), relay.reshape(bop_1161.astype('float32'), relay.shape_of(var_1160))) # shape=(6, 10, 8)
output = bop_1169
output2 = bop_1169
func_1177 = relay.Function([var_1159,var_1160,], output)
mod['func_1177'] = func_1177
mod = relay.transform.InferType()(mod)
var_1178 = relay.var("var_1178", dtype = "bool", shape = (6, 1, 8))#candidate|1178|(6, 1, 8)|var|bool
var_1179 = relay.var("var_1179", dtype = "bool", shape = (6, 10, 8))#candidate|1179|(6, 10, 8)|var|bool
output = func_1177(var_1178,var_1179,)
func_1180 = relay.Function([var_1178,var_1179,], output)
mutated_mod['func_1180'] = func_1180
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1283 = relay.var("var_1283", dtype = "float32", shape = (6, 10, 13))#candidate|1283|(6, 10, 13)|var|float32
uop_1284 = relay.log2(var_1283.astype('float32')) # shape=(6, 10, 13)
bop_1300 = relay.right_shift(uop_1284.astype('int8'), relay.reshape(var_1283.astype('int8'), relay.shape_of(uop_1284))) # shape=(6, 10, 13)
func_934_call = mod.get_global_var('func_934')
func_937_call = mutated_mod.get_global_var('func_937')
const_1304 = relay.const([False,False,False,False,False,False,True,True,True,False,False,False,True,True,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,False,False,False,True,True,False,True,True,True,True,False,True,False,True,True,False,True,True,False,False,True,False,True,True,False,True,True,True,False,True,True,True,True,False,False,True,False,True,False,True,True,False,False,True,True,True,False,False,False,False,False,False,False,False,True,False,True,False,True,True,True,True,False,True,True,True,False,True,False,False,True,True,False,True,True,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False,False,True,False,True,False,True,False,False,False,True,False,False,True,False,False,False,True,True,False,True,False,True,False,True,True,False,True,False,True,False,True,True,False,True,False,False,False,False,False,False,True,False,False,True,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,True,True,False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,True,True,False,False,False,False,False,True,False,True,True,True,True,False,True,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,False,False,False,False,False,True,True,False,True,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,True,True,False,False,False,True,False,False,False,True,False,False,False,True,False,True,False,False,False,True,False,False,False,False,True,False,True,False,True,True,False,False,False,False,False,False,True,False,False,True,True,True,False,True,False,False,True,False,False,True,False,False,False,False,True,True,True,False,True,False,True,True,False,False,True,False,False], dtype = "bool")#candidate|1304|(360,)|const|bool
const_1305 = relay.const([4,3,-3,5,-9,8,-4,-1,-9,-5,1,-3,7,9,4], dtype = "int16")#candidate|1305|(15,)|const|int16
call_1303 = relay.TupleGetItem(func_934_call(relay.reshape(const_1304.astype('bool'), [9, 10, 4]), relay.reshape(const_1305.astype('int16'), [15, 1]), ), 0)
call_1306 = relay.TupleGetItem(func_937_call(relay.reshape(const_1304.astype('bool'), [9, 10, 4]), relay.reshape(const_1305.astype('int16'), [15, 1]), ), 0)
uop_1312 = relay.rsqrt(bop_1300.astype('float64')) # shape=(6, 10, 13)
func_141_call = mod.get_global_var('func_141')
func_144_call = mutated_mod.get_global_var('func_144')
call_1318 = relay.TupleGetItem(func_141_call(relay.reshape(const_1305.astype('int16'), [15,])), 1)
call_1319 = relay.TupleGetItem(func_144_call(relay.reshape(const_1305.astype('int16'), [15,])), 1)
output = relay.Tuple([call_1303,const_1304,const_1305,uop_1312,call_1318,])
output2 = relay.Tuple([call_1306,const_1304,const_1305,uop_1312,call_1319,])
func_1324 = relay.Function([var_1283,], output)
mod['func_1324'] = func_1324
mod = relay.transform.InferType()(mod)
var_1325 = relay.var("var_1325", dtype = "float32", shape = (6, 10, 13))#candidate|1325|(6, 10, 13)|var|float32
output = func_1324(var_1325)
func_1326 = relay.Function([var_1325], output)
mutated_mod['func_1326'] = func_1326
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1354 = relay.const([[[-9.482387,-6.903724,2.228743,6.043628,6.798205,1.833068],[3.418779,-9.662571,8.620158,8.627444,-2.364891,-1.496484],[4.052987,9.050169,3.004885,-5.585367,-6.080560,-8.452126],[-7.118862,3.568100,6.382026,1.541780,3.101448,-9.078084],[6.297302,-1.730506,0.330991,3.902160,0.356335,-9.185790]],[[7.981921,-9.069373,3.341741,6.007726,-1.874253,6.999810],[-3.428479,-2.120087,5.897203,-4.622498,-1.846059,-3.240074],[-2.994457,-2.586120,-6.539965,-6.445118,-2.332408,-0.883429],[5.787077,0.440381,-8.861172,9.597850,-3.782658,-4.251486],[-4.665681,-0.939375,-9.225993,-0.665036,1.135886,-2.007095]],[[6.039528,3.366889,2.568751,1.100443,-0.275293,-1.602527],[-3.334861,7.631480,3.983861,-7.639815,-1.883997,4.564494],[1.579936,1.035555,-0.232551,6.157667,1.365656,6.747333],[-5.386479,5.863926,-0.451282,7.321718,-6.681634,9.428724],[4.703316,6.584487,-4.740919,-0.416347,6.639572,-6.876981]],[[8.914208,6.932484,9.642756,1.916511,-9.777587,-4.163619],[-1.368376,6.128209,-8.894276,-9.111836,-5.197910,7.507923],[-1.692237,-0.437137,-7.541614,-6.933429,-2.782871,-1.689268],[-4.085857,5.171085,-7.738110,3.415207,-2.949965,0.678142],[4.937939,-4.237426,-3.267059,2.587599,8.154509,-0.321168]],[[-7.060132,8.569556,-8.063212,-2.301397,5.857639,4.272144],[7.580074,-4.042144,2.676671,-7.274260,3.010765,-1.520989],[4.982287,4.001927,-4.592772,-9.546842,-6.933597,5.008104],[7.251865,8.926294,-3.833502,-2.777459,-2.000597,1.368709],[3.513871,-0.388542,-5.137299,-2.534791,-1.443883,-3.362558]],[[4.491701,-1.462815,-5.622031,-6.570094,0.732111,-7.063922],[4.244558,-9.115863,2.056515,1.499633,3.343794,0.737561],[3.637690,6.597858,6.588972,-3.733194,-5.408441,-3.568830],[-4.491799,-7.128338,6.134209,5.332034,-9.151536,-0.207433],[0.704278,-0.155589,8.498874,-9.503515,4.444316,1.514102]],[[3.879581,9.240857,-8.633383,-6.668161,-9.124637,-6.451975],[0.748732,-3.087191,6.143725,4.156892,0.491976,-7.022363],[-9.407380,2.231374,-8.765943,-3.743211,-6.567606,-9.002228],[-2.933730,9.579104,1.951114,-7.949931,-7.503696,-1.594989],[6.390176,-6.926102,0.230046,1.347768,-4.393477,4.178640]],[[3.797453,-1.529198,1.456322,-5.096020,-3.744996,9.311665],[-9.092749,-2.252477,-3.870947,-3.203078,7.416149,-1.998127],[7.323136,-5.128797,-2.212183,4.007059,8.908168,8.986728],[-0.604670,-9.797343,-0.616829,-8.952635,5.325940,9.658372],[-5.639955,7.632086,-9.395168,-5.214447,-9.697955,6.653442]],[[2.284638,-0.628592,8.619198,5.564461,-6.638063,-0.332460],[1.539877,3.135494,7.595476,3.785185,-5.244234,0.582796],[-2.755684,6.152385,-9.220925,-8.298111,6.538961,4.684836],[-1.999849,-8.725459,-6.405255,6.375219,9.089257,3.004041],[2.547544,-6.545952,2.023578,0.657666,-7.956066,-2.186584]],[[3.414098,-3.289414,-5.271876,8.768131,-6.843069,3.135589],[-5.618140,3.729839,3.391755,3.092184,6.753637,-4.107191],[1.829946,-9.732593,-9.287217,3.760867,6.144043,-5.754746],[7.957516,7.473529,2.181859,-9.787876,2.406049,-3.930881],[-6.933644,-5.268473,3.228667,6.580238,-8.826371,-8.886918]],[[-5.310555,-7.309011,5.393664,1.717057,4.318585,5.298564],[3.546733,-5.945333,2.976413,5.427571,-5.663831,3.533835],[2.682912,1.217178,-6.544757,-5.325555,8.978121,5.218821],[-5.778185,5.498809,1.115832,-5.644226,-2.902066,5.647562],[5.144251,-9.538412,-2.724938,-1.894407,-0.339815,6.527764]],[[1.345348,2.569264,2.279480,-9.134268,-1.228590,1.217688],[-9.022581,-2.608482,-9.091561,-1.329318,6.699657,-7.048528],[-6.802048,6.237148,-2.622173,1.788737,-6.176232,-4.237201],[1.296429,2.300559,-7.504817,7.419455,1.962297,2.296117],[-1.738636,5.101191,-1.129653,7.457912,-4.004620,2.379457]],[[-7.537564,9.301203,-0.442375,-4.363409,-4.762742,2.239333],[-4.300094,8.765114,-2.727821,5.756256,-6.054207,-9.329023],[-4.835566,9.807611,-5.112920,6.594193,6.078039,-3.676093],[-3.275726,-0.472828,-1.271063,5.658933,-6.577482,-5.403164],[-0.750103,6.635607,6.966112,4.026582,-2.745063,-7.643286]],[[-6.682922,1.813424,-2.326794,0.712536,-8.902929,0.562728],[2.675277,3.607681,7.292988,-3.867981,2.289546,-4.694541],[-2.297762,8.606237,-9.649422,5.703594,5.949656,4.752582],[-1.516982,5.785405,-1.832320,-9.843893,5.045972,8.315803],[9.889299,-6.505160,-2.629080,3.574413,8.931207,4.621198]],[[1.525331,-6.830813,2.759787,-9.090849,-3.713270,-8.811388],[1.536187,-4.530409,-8.921515,6.882155,9.472545,-4.133719],[6.207719,-9.614808,-4.360049,-1.542676,0.013457,0.664928],[-6.012997,-2.927449,1.382363,0.107701,4.237111,7.559500],[-2.553780,-2.439737,0.536824,6.817510,-6.580613,9.327942]]], dtype = "float32")#candidate|1354|(15, 5, 6)|const|float32
uop_1355 = relay.erf(const_1354.astype('float32')) # shape=(15, 5, 6)
func_141_call = mod.get_global_var('func_141')
func_144_call = mutated_mod.get_global_var('func_144')
var_1360 = relay.var("var_1360", dtype = "int16", shape = (15, 1))#candidate|1360|(15, 1)|var|int16
call_1359 = relay.TupleGetItem(func_141_call(relay.reshape(var_1360.astype('int16'), [15,])), 5)
call_1361 = relay.TupleGetItem(func_144_call(relay.reshape(var_1360.astype('int16'), [15,])), 5)
func_934_call = mod.get_global_var('func_934')
func_937_call = mutated_mod.get_global_var('func_937')
const_1375 = relay.const([[False,False,True,False,True,False,True,False,False,True,False,True,False,False,True,True,True,True,True,False,True,True,True,False,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,False,False,False,True,False,False,True,True,False,False,False,False,True,True,True,False,True,False,True,True,False],[True,True,True,True,True,True,True,True,False,True,False,False,True,True,False,False,False,True,False,False,True,False,False,True,True,False,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,False,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,True],[False,True,True,True,True,True,False,False,False,False,True,False,False,True,False,True,False,False,True,False,False,False,True,False,False,False,False,True,True,True,False,True,True,False,True,False,True,True,False,True,True,True,True,True,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,True],[True,False,True,False,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,False,True,False,True,True,True,False,False,True,False,True,True,True,True,False,True,True,False,True,False,True,True,False,True,False,False,False,True,True,True,False,True,True,True,False,False,False,True,False,True,True],[False,False,False,True,False,True,True,False,False,True,True,True,False,False,True,False,False,False,True,False,True,True,True,False,True,True,False,False,False,True,True,False,False,True,True,False,False,False,True,False,False,False,True,False,True,True,False,True,True,True,True,False,False,False,False,False,False,False,False,False],[False,False,False,False,True,True,False,False,False,True,False,False,False,False,False,True,True,False,False,False,True,False,True,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,True,False,True,True,True,True,False,False,True,False,False]], dtype = "bool")#candidate|1375|(6, 60)|const|bool
call_1374 = relay.TupleGetItem(func_934_call(relay.reshape(const_1375.astype('bool'), [9, 10, 4]), relay.reshape(var_1360.astype('int16'), [15, 1]), ), 2)
call_1376 = relay.TupleGetItem(func_937_call(relay.reshape(const_1375.astype('bool'), [9, 10, 4]), relay.reshape(var_1360.astype('int16'), [15, 1]), ), 2)
output = relay.Tuple([uop_1355,call_1359,var_1360,call_1374,const_1375,])
output2 = relay.Tuple([uop_1355,call_1361,var_1360,call_1376,const_1375,])
func_1381 = relay.Function([var_1360,], output)
mod['func_1381'] = func_1381
mod = relay.transform.InferType()(mod)
var_1382 = relay.var("var_1382", dtype = "int16", shape = (15, 1))#candidate|1382|(15, 1)|var|int16
output = func_1381(var_1382)
func_1383 = relay.Function([var_1382], output)
mutated_mod['func_1383'] = func_1383
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1395 = relay.var("var_1395", dtype = "float64", shape = (6, 3, 1))#candidate|1395|(6, 3, 1)|var|float64
uop_1396 = relay.cos(var_1395.astype('float64')) # shape=(6, 3, 1)
output = uop_1396
output2 = uop_1396
func_1409 = relay.Function([var_1395,], output)
mod['func_1409'] = func_1409
mod = relay.transform.InferType()(mod)
mutated_mod['func_1409'] = func_1409
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1410 = relay.var("var_1410", dtype = "float64", shape = (6, 3, 1))#candidate|1410|(6, 3, 1)|var|float64
func_1409_call = mutated_mod.get_global_var('func_1409')
call_1411 = func_1409_call(var_1410)
output = call_1411
func_1412 = relay.Function([var_1410], output)
mutated_mod['func_1412'] = func_1412
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1802 = relay.var("var_1802", dtype = "bool", shape = ())#candidate|1802|()|var|bool
const_1803 = relay.const([[[True,False,True,False,False,False,True,True,True,True,True,True,False],[False,True,True,False,True,True,True,True,True,False,True,True,True],[False,False,False,True,False,False,True,True,False,True,True,True,False],[False,False,False,False,True,False,True,False,False,True,True,True,False],[False,True,True,True,False,False,True,True,True,False,True,False,True],[True,False,True,True,False,True,True,False,True,False,False,True,False],[False,False,True,True,False,True,True,False,True,True,False,False,False],[True,False,True,True,False,True,True,True,False,False,False,True,False],[False,False,True,True,False,True,True,False,True,True,True,False,True],[False,True,True,True,False,False,True,True,False,True,False,True,False]],[[False,True,True,False,False,True,False,True,False,False,False,True,False],[True,False,False,True,False,False,True,True,True,True,False,True,False],[False,False,True,True,True,True,True,False,True,True,True,True,False],[True,False,False,False,False,False,False,False,True,False,True,False,False],[False,True,False,True,False,False,False,True,True,True,False,False,True],[False,True,False,True,True,True,True,False,True,False,False,True,False],[True,False,True,False,False,False,True,False,True,True,False,True,False],[True,False,True,False,True,True,True,True,False,True,False,False,True],[True,False,True,True,False,False,True,False,False,True,False,False,True],[True,True,True,True,False,False,True,True,False,True,False,False,False]],[[False,True,True,False,False,False,False,True,True,True,True,False,True],[False,True,True,False,False,False,True,True,True,True,False,True,False],[False,False,False,False,False,True,True,True,True,True,False,False,False],[True,True,False,False,False,False,True,True,False,False,True,True,True],[True,True,True,False,True,False,False,False,False,False,True,False,False],[False,True,False,False,False,True,True,False,True,True,False,True,False],[False,True,False,True,False,True,False,False,True,False,False,True,False],[False,True,True,False,True,True,False,True,False,False,True,True,False],[False,True,False,True,True,False,False,True,True,True,False,False,True],[True,False,True,False,False,True,False,True,False,True,False,False,True]],[[False,False,False,False,False,False,True,False,False,False,False,False,False],[True,True,False,True,False,False,True,True,False,True,True,False,False],[True,False,True,True,True,True,True,True,True,True,True,False,True],[True,True,True,False,True,False,True,True,False,False,True,True,True],[False,True,False,False,True,True,False,False,False,True,False,True,False],[True,False,False,False,True,True,True,False,True,False,True,True,True],[True,True,True,False,False,True,True,True,True,True,False,False,True],[True,True,True,False,False,True,True,False,True,False,True,False,True],[True,False,False,False,True,True,True,False,True,True,True,True,False],[True,False,True,True,True,False,False,True,False,False,False,True,False]],[[True,False,False,True,True,True,True,True,True,False,False,False,True],[True,True,False,False,False,True,False,True,False,False,True,True,True],[True,True,True,True,False,False,True,False,True,False,True,False,True],[False,False,True,False,True,False,True,False,True,True,True,True,False],[False,True,True,True,False,True,False,True,False,False,True,True,False],[False,True,True,False,False,True,True,True,True,False,True,True,False],[False,False,False,False,True,False,True,False,True,False,True,True,True],[True,False,True,False,False,True,True,False,False,True,True,True,False],[True,True,False,False,False,False,False,False,False,True,False,False,False],[True,False,True,False,True,True,False,False,True,True,False,True,True]],[[False,False,False,True,True,True,False,True,True,False,True,False,False],[False,True,False,False,True,True,False,True,False,True,False,False,False],[True,True,False,False,False,False,True,True,True,False,False,True,True],[False,False,False,False,False,False,True,True,False,True,False,False,False],[False,False,False,True,False,True,False,False,False,True,False,True,False],[True,True,False,False,False,False,False,False,False,True,True,False,False],[True,True,False,False,True,True,False,True,False,False,False,False,False],[False,True,False,True,True,True,False,False,True,False,False,False,True],[True,True,False,True,True,True,False,True,True,True,False,True,False],[False,True,False,True,True,True,False,True,False,False,False,True,False]],[[False,True,False,False,False,True,True,False,False,False,False,False,True],[True,True,False,True,True,False,False,False,True,False,True,False,True],[True,False,False,False,False,False,False,False,False,False,False,True,True],[False,True,True,True,False,False,False,False,True,False,True,False,False],[False,False,True,False,True,False,False,True,True,False,True,True,True],[True,True,True,False,False,True,True,True,False,False,False,True,False],[True,True,True,True,True,False,True,False,False,True,False,True,False],[True,True,False,False,False,True,False,True,False,False,True,True,False],[True,True,False,False,False,True,True,True,True,False,True,False,False],[False,True,True,True,False,False,False,False,True,True,True,True,False]],[[True,True,True,True,True,True,False,True,True,False,True,True,False],[False,True,True,False,False,True,False,True,False,False,True,True,False],[False,False,True,True,False,True,True,False,False,False,True,False,False],[False,True,True,True,True,True,True,False,True,True,False,True,False],[False,True,True,True,True,False,True,True,True,False,False,False,False],[False,True,True,False,True,True,True,False,True,False,True,False,True],[False,True,True,False,True,True,True,False,True,True,False,False,False],[False,False,False,False,False,False,True,True,False,False,True,False,False],[False,False,True,False,True,False,True,False,False,False,False,True,False],[True,False,True,True,False,True,False,False,True,False,False,True,False]],[[True,True,True,True,False,True,True,True,True,True,True,False,True],[True,False,True,True,False,False,True,True,False,False,False,False,False],[False,False,True,True,False,False,False,True,True,False,False,False,False],[True,True,True,True,True,True,True,False,False,False,True,True,True],[True,True,False,True,False,False,True,True,True,False,True,True,True],[False,False,False,False,False,True,False,True,True,True,False,False,True],[False,False,False,False,False,True,True,False,False,True,False,False,False],[True,False,True,False,True,True,False,True,False,False,True,False,False],[False,True,False,False,False,True,True,True,True,True,False,False,True],[True,False,True,True,False,False,True,False,False,False,True,True,False]]], dtype = "bool")#candidate|1803|(9, 10, 13)|const|bool
bop_1804 = relay.logical_and(var_1802.astype('bool'), const_1803.astype('bool')) # shape=(9, 10, 13)
uop_1807 = relay.atan(bop_1804.astype('float32')) # shape=(9, 10, 13)
output = uop_1807
output2 = uop_1807
func_1815 = relay.Function([var_1802,], output)
mod['func_1815'] = func_1815
mod = relay.transform.InferType()(mod)
var_1816 = relay.var("var_1816", dtype = "bool", shape = ())#candidate|1816|()|var|bool
output = func_1815(var_1816)
func_1817 = relay.Function([var_1816], output)
mutated_mod['func_1817'] = func_1817
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2671 = relay.var("var_2671", dtype = "float64", shape = (10, 9, 12))#candidate|2671|(10, 9, 12)|var|float64
var_2672 = relay.var("var_2672", dtype = "float64", shape = (10, 9, 12))#candidate|2672|(10, 9, 12)|var|float64
bop_2673 = relay.mod(var_2671.astype('float64'), relay.reshape(var_2672.astype('float64'), relay.shape_of(var_2671))) # shape=(10, 9, 12)
func_1409_call = mod.get_global_var('func_1409')
func_1412_call = mutated_mod.get_global_var('func_1412')
const_2690 = relay.const([-0.330088,-6.969178,-3.446035,0.220925,4.361249,8.341566,5.754202,0.166439,9.186037,5.401341,-6.333825,-2.613096,0.318955,1.163844,-6.579705,6.502045,4.806956,2.068670], dtype = "float64")#candidate|2690|(18,)|const|float64
call_2689 = func_1409_call(relay.reshape(const_2690.astype('float64'), [6, 3, 1]))
call_2691 = func_1409_call(relay.reshape(const_2690.astype('float64'), [6, 3, 1]))
func_417_call = mod.get_global_var('func_417')
func_421_call = mutated_mod.get_global_var('func_421')
var_2696 = relay.var("var_2696", dtype = "float32", shape = (50,))#candidate|2696|(50,)|var|float32
const_2697 = relay.const([[3.751385,-4.878472,8.234598,9.031579,0.419386,9.671467,3.963725,4.810765,6.904542,0.916638,3.439605,-8.400832,2.932467,-9.727243,8.133218,9.564750,8.226398,1.161429,5.550181,-0.555875,-0.920608,2.921042,-4.231353,-9.444203,0.603397,-8.454906,3.461094,4.214550,-3.484212,-6.229059,4.210351,-8.406639,-4.569439,0.657855,-0.548233,-0.133555,3.474973,-9.222232,-8.142203,-4.483491,-8.960439,1.650467,5.087461,-8.135691,-6.130780,-0.016923,9.486177,-9.648372,-4.631368,1.053058,-8.010465,-7.064199,-5.143532,5.683621,9.644616,-2.657648,-1.635756,0.564633,-6.258903,8.703464,-9.397954,-9.364102,3.435100,7.261226,-0.180044,-9.630332,1.265056,-7.504182,-3.586776,-4.433743,8.222814,9.232807,-3.990896,-7.764882,0.395187,-1.603913,2.266682,7.133658,5.323978,-4.585080,9.848786,-8.267620,6.041472,-9.808123,4.039380,5.322988,4.233205,-4.960348,2.375963,-3.796054,8.321080,3.530938,8.337710,1.865422,0.343592,-5.183644,-4.959966,7.975113,-3.192639,3.331750,8.333996,-7.858482,-1.923430,-2.994873,3.923667,-2.879486,8.826756,5.861951,-6.258902,-1.965745,7.506724,-4.182700,0.260348,3.640431,-5.889524,7.919624,-0.856800,-1.726909,6.945180,-5.501001,-4.800501,5.761147,-8.413423,-5.249196,4.336383,7.304813,-0.234274,-5.710529,1.784342,9.462390,5.221276,6.845254,-5.048877,-7.644834,2.008947,6.605094,8.765467,9.541106,6.097773,-5.487293,-5.877192,0.368826,5.346449,6.956370,-1.761846,-8.783442,7.810917,0.644076,-7.761550,8.888298,-5.994300,6.659277,6.374734,-8.695056,-8.815773,9.977659,-1.288712,1.353441,0.627412,-3.887180,0.890389,4.778829,4.768967,1.461641,-4.659086,9.436738,9.512396,-2.747378,8.734432,6.581439,8.629276,3.152303,-0.788315,0.302292,5.971524,7.411467,1.852894,7.613392,4.258220,-1.872015,-1.117516,-7.586735,-1.696291,-0.724584,9.658908,1.495147,2.222432,-4.015903,-5.883839,1.992739,-8.413197,-7.608110,1.082959,-9.987331,-9.261518,-1.237206,-5.489133,-1.081148,4.279896,-2.466803],[5.082042,1.875495,-8.282481,-6.350374,0.287837,-0.969688,-2.808970,4.437933,1.941642,-5.617952,-2.237179,-4.902354,9.200389,1.059259,7.647447,-5.615873,-9.216234,8.496861,4.353110,2.426637,2.964661,-8.237301,-2.085674,1.831472,4.732216,-4.352101,-4.317132,-2.684816,1.724861,-8.143124,-2.333505,1.124367,-7.606756,6.164907,-0.045128,6.940815,9.874588,4.527189,4.070992,0.998669,-3.229456,1.699296,-4.363164,1.204147,9.825119,-2.279640,-4.223406,-9.941471,6.603966,-8.496000,-0.188461,5.416827,-1.502901,-8.567116,-5.827942,-4.295667,3.692056,5.069380,-2.841800,3.215701,5.133944,2.837873,-4.470031,-4.359134,1.331206,7.054877,-4.575148,2.705861,-8.633916,2.262081,3.011141,9.125435,2.368810,-0.982174,8.545183,7.346614,-9.652717,-9.626148,2.222304,-8.233882,-6.563766,-1.603972,-6.476829,1.225823,5.014664,3.591412,-6.287786,9.713718,-0.273011,4.087878,-7.903475,-4.600596,0.250698,1.565308,5.460583,-2.386179,7.253946,8.086273,-2.101387,-8.224434,6.127243,0.526907,4.727335,1.666596,-2.302444,7.446799,6.476186,6.717827,0.183237,0.757738,-8.534937,-2.170546,2.666101,-0.133539,-3.863465,9.421975,-0.466193,0.357346,-7.502005,2.763481,-2.296242,1.724415,-8.105031,-9.807763,0.442861,4.836112,5.608436,7.789085,1.235071,9.546737,7.132923,5.683066,0.983135,4.310189,9.046114,-6.026852,6.005379,9.679027,8.142997,4.806987,-2.969441,-0.521337,-2.488626,-7.065664,6.080977,5.604905,-7.747344,3.750500,-7.156959,3.893726,2.518728,2.739398,3.856183,9.535691,-8.822419,1.038756,9.329538,8.976477,-6.381301,1.147593,6.884232,-3.744635,9.778184,5.283050,-3.888328,7.416238,-5.026753,-5.756953,7.467975,-4.205050,8.177456,-5.846756,-9.200609,-6.518595,5.086294,-1.297873,6.284952,1.424513,-8.738011,-9.613016,7.899971,5.479074,-2.565358,-7.710181,5.894511,2.581485,-6.812493,0.601757,0.396027,3.702161,6.041501,0.666701,-7.286432,3.405948,3.016899,7.384430,9.386179,5.026473,6.119943,6.636338]], dtype = "float32")#candidate|2697|(2, 200)|const|float32
call_2695 = relay.TupleGetItem(func_417_call(relay.reshape(var_2696.astype('float32'), [10, 5, 1]), relay.reshape(const_2697.astype('float32'), [10, 5, 8]), ), 0)
call_2698 = relay.TupleGetItem(func_421_call(relay.reshape(var_2696.astype('float32'), [10, 5, 1]), relay.reshape(const_2697.astype('float32'), [10, 5, 8]), ), 0)
bop_2707 = relay.floor_mod(const_2690.astype('float32'), relay.reshape(call_2689.astype('float32'), relay.shape_of(const_2690))) # shape=(18,)
bop_2710 = relay.floor_mod(const_2690.astype('float32'), relay.reshape(call_2691.astype('float32'), relay.shape_of(const_2690))) # shape=(18,)
func_1177_call = mod.get_global_var('func_1177')
func_1180_call = mutated_mod.get_global_var('func_1180')
var_2721 = relay.var("var_2721", dtype = "bool", shape = (48,))#candidate|2721|(48,)|var|bool
const_2722 = relay.const([True,True,True,False,False,False,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,True,False,True,False,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,True,True,True,True,False,True,False,True,False,False,False,False,True,False,True,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,False,True,True,True,False,True,True,False,False,True,True,False,True,False,True,True,False,False,False,True,True,False,True,True,True,True,True,False,True,True,False,True,False,True,True,True,False,False,True,False,True,False,True,False,True,False,True,True,False,False,False,False,False,True,True,True,False,False,True,True,False,True,False,False,False,True,True,False,True,True,False,False,True,True,True,False,True,False,True,False,False,True,False,False,False,True,True,False,True,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,True,False,False,True,True,False,True,True,True,True,False,False,False,True,False,True,False,False,True,True,False,True,True,True,False,False,False,True,False,False,True,False,False,True,True,True,True,False,True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,True,True,True,True,True,False,False,True,True,False,False,False,True,True,False,True,False,True,False,True,False,True,False,True,True,False,True,True,False,False,True,True,True,False,True,True,False,True,False,True,True,False,False,False,False,False,True,False,True,True,False,True,False,False,False,True,False,True,False,True,False,False,False,True,False,True,False,True,False,True,False,True,True,False,True,True,False,False,False,True,True,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,True,False,True,False,True,True,True,True,False,True,False,False,True,False,False,True,False,False,False,False,True,True,True,False,True,False,False,False,False,False,False,False,True,True,False,False,True,True,True,True,False,False,True,False,False,True,True,True,False,True,True,True,True,False,True,False,True,False,False,True,False,True,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,False,True,True,False,False,True,True,True,False,True,False,False,True,True,True,False,True,False,True,False,False,False,True,False,True,True,True,True,False,True,False,True,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,False,True,False,False,False,False,True,True,True,False,False,True,True,True,True,True,False,False,False,False,False,True,True,False,True,True,False,False,False,False,False], dtype = "bool")#candidate|2722|(480,)|const|bool
call_2720 = func_1177_call(relay.reshape(var_2721.astype('bool'), [6, 1, 8]), relay.reshape(const_2722.astype('bool'), [6, 10, 8]), )
call_2723 = func_1177_call(relay.reshape(var_2721.astype('bool'), [6, 1, 8]), relay.reshape(const_2722.astype('bool'), [6, 10, 8]), )
uop_2726 = relay.sinh(call_2695.astype('float32')) # shape=(10, 5, 8)
uop_2728 = relay.sinh(call_2698.astype('float32')) # shape=(10, 5, 8)
output = relay.Tuple([bop_2673,var_2696,const_2697,bop_2707,call_2720,var_2721,const_2722,uop_2726,])
output2 = relay.Tuple([bop_2673,var_2696,const_2697,bop_2710,call_2723,var_2721,const_2722,uop_2728,])
func_2733 = relay.Function([var_2671,var_2672,var_2696,var_2721,], output)
mod['func_2733'] = func_2733
mod = relay.transform.InferType()(mod)
mutated_mod['func_2733'] = func_2733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2733_call = mutated_mod.get_global_var('func_2733')
var_2735 = relay.var("var_2735", dtype = "float64", shape = (10, 9, 12))#candidate|2735|(10, 9, 12)|var|float64
var_2736 = relay.var("var_2736", dtype = "float64", shape = (10, 9, 12))#candidate|2736|(10, 9, 12)|var|float64
var_2737 = relay.var("var_2737", dtype = "float32", shape = (50,))#candidate|2737|(50,)|var|float32
var_2738 = relay.var("var_2738", dtype = "bool", shape = (48,))#candidate|2738|(48,)|var|bool
call_2734 = func_2733_call(var_2735,var_2736,var_2737,var_2738,)
output = call_2734
func_2739 = relay.Function([var_2735,var_2736,var_2737,var_2738,], output)
mutated_mod['func_2739'] = func_2739
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3027 = relay.var("var_3027", dtype = "uint16", shape = ())#candidate|3027|()|var|uint16
var_3028 = relay.var("var_3028", dtype = "uint16", shape = (13, 10, 15))#candidate|3028|(13, 10, 15)|var|uint16
bop_3029 = relay.equal(var_3027.astype('bool'), var_3028.astype('bool')) # shape=(13, 10, 15)
func_34_call = mod.get_global_var('func_34')
func_37_call = mutated_mod.get_global_var('func_37')
const_3033 = relay.const([[6,2,-4,-1,6,-8,-10,7,3,5,-9,-1,2,-5,-3]], dtype = "int16")#candidate|3033|(1, 15)|const|int16
call_3032 = relay.TupleGetItem(func_34_call(relay.reshape(const_3033.astype('int16'), [15, 1])), 0)
call_3034 = relay.TupleGetItem(func_37_call(relay.reshape(const_3033.astype('int16'), [15, 1])), 0)
func_34_call = mod.get_global_var('func_34')
func_37_call = mutated_mod.get_global_var('func_37')
call_3036 = relay.TupleGetItem(func_34_call(relay.reshape(const_3033.astype('int16'), [15, 1])), 0)
call_3037 = relay.TupleGetItem(func_37_call(relay.reshape(const_3033.astype('int16'), [15, 1])), 0)
output = relay.Tuple([bop_3029,call_3032,const_3033,call_3036,])
output2 = relay.Tuple([bop_3029,call_3034,const_3033,call_3037,])
func_3038 = relay.Function([var_3027,var_3028,], output)
mod['func_3038'] = func_3038
mod = relay.transform.InferType()(mod)
var_3039 = relay.var("var_3039", dtype = "uint16", shape = ())#candidate|3039|()|var|uint16
var_3040 = relay.var("var_3040", dtype = "uint16", shape = (13, 10, 15))#candidate|3040|(13, 10, 15)|var|uint16
output = func_3038(var_3039,var_3040,)
func_3041 = relay.Function([var_3039,var_3040,], output)
mutated_mod['func_3041'] = func_3041
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4168 = relay.var("var_4168", dtype = "float64", shape = ())#candidate|4168|()|var|float64
var_4169 = relay.var("var_4169", dtype = "float64", shape = (16, 5, 16))#candidate|4169|(16, 5, 16)|var|float64
bop_4170 = relay.floor_mod(var_4168.astype('float64'), var_4169.astype('float64')) # shape=(16, 5, 16)
output = bop_4170
output2 = bop_4170
func_4181 = relay.Function([var_4168,var_4169,], output)
mod['func_4181'] = func_4181
mod = relay.transform.InferType()(mod)
mutated_mod['func_4181'] = func_4181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4181_call = mutated_mod.get_global_var('func_4181')
var_4183 = relay.var("var_4183", dtype = "float64", shape = ())#candidate|4183|()|var|float64
var_4184 = relay.var("var_4184", dtype = "float64", shape = (16, 5, 16))#candidate|4184|(16, 5, 16)|var|float64
call_4182 = func_4181_call(var_4183,var_4184,)
output = call_4182
func_4185 = relay.Function([var_4183,var_4184,], output)
mutated_mod['func_4185'] = func_4185
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4292 = relay.var("var_4292", dtype = "float64", shape = (7, 13, 4))#candidate|4292|(7, 13, 4)|var|float64
uop_4293 = relay.log10(var_4292.astype('float64')) # shape=(7, 13, 4)
func_1324_call = mod.get_global_var('func_1324')
func_1326_call = mutated_mod.get_global_var('func_1326')
const_4304 = relay.const([2.339459,-2.026159,3.789537,7.547664,-0.453175,0.449250,1.850614,-6.070969,-8.411988,-2.611766,7.392644,5.477497,-3.749972,4.129188,-6.067533,1.296068,-4.893785,-0.156601,3.528271,-8.736569,8.650494,2.770553,-9.226044,-2.633285,-6.851612,0.098743,3.964281,0.619906,-5.349729,2.810695,2.229655,-8.123320,-3.671087,8.289390,-5.014993,-3.508887,-2.955042,-4.701542,7.663177,1.283571,8.274668,4.940623,-5.262233,-7.356778,9.092661,8.052009,4.344739,-3.038622,-3.251761,5.758415,-5.833739,7.816095,-2.198632,2.973564,-5.595771,6.049057,3.328062,-6.679439,3.220387,-3.498746,3.482804,1.477506,6.341395,-7.741479,-8.193114,-7.375047,4.431989,7.396204,3.015923,-1.760541,3.192629,-3.392081,-0.886084,-9.364667,5.088594,4.239009,6.778514,6.192703,-4.338819,-4.133538,-6.492273,0.400100,-3.223851,5.643129,6.880252,-1.394184,7.250578,-7.569143,9.487116,4.414889,5.784890,3.639929,6.881986,-0.498740,0.627312,-5.490754,2.571666,2.469836,-2.959808,-3.792391,-4.771009,4.167967,2.899756,-8.523290,-2.385112,0.577407,-4.460743,-1.651578,-7.805535,0.454790,-2.664699,2.165195,-3.735043,4.894079,3.993421,-0.373925,-5.298814,8.906644,4.216364,4.910784,6.900592,-6.237147,5.334849,2.642205,0.231928,9.404871,5.687289,9.997046,-2.248064,-2.175432,-1.768744,9.727220,-3.418873,-4.482505,-2.734941,-1.559208,4.208698,5.117561,9.490607,-7.510163,-8.843278,-5.823562,-2.752561,5.804934,7.892655,-9.795431,-3.083997,-3.670959,-2.368589,5.383982,-5.324194,-0.540838,-5.864501,4.913962,-6.891243,-2.282846,1.995086,-7.139388,-9.683267,-0.181403,-8.567277,-8.932412,7.518518,1.363643,9.574104,-5.485608,-7.382337,2.748811,4.642548,1.293332,-7.605950,-3.003748,-6.386930,9.478997,-2.828237,-3.856633,-7.739012,6.040194,-9.252066,7.166637,6.449510,3.931048,-5.478208,-9.643835,5.563808,-4.335477,4.863046,-4.776372,4.545343,6.649711,4.531210,-3.557991,-2.844375,6.071599,0.470918,-7.160451,0.702328,-1.493230,7.907355,2.121836,-4.512046,-9.534926,-0.044353,-8.959558,7.404306,4.335652,4.442667,-9.276460,5.730700,-9.564683,5.083678,-8.618566,2.303091,-5.779115,2.133128,9.190481,4.027582,-3.931614,-1.102957,-4.492144,-8.698380,5.358216,0.212269,9.686851,5.208809,0.217370,-6.570067,7.492461,0.823993,-5.086115,3.422330,-9.295276,-8.977570,-9.293582,0.953266,-0.152583,-8.195390,-2.191792,2.946318,0.844607,2.057574,2.333513,-7.243191,9.080234,7.837321,-2.398555,-3.131581,2.772602,3.051489,4.858084,-2.619350,-5.356439,1.524133,1.173179,-6.217693,-8.534216,2.415053,-9.967191,-8.366062,1.895031,0.920215,9.549568,9.130163,-0.092031,-8.218291,9.703897,1.856248,-0.645859,-4.208630,-2.306766,-8.861401,0.919340,-0.584677,7.997852,9.170757,-2.539474,-3.490934,-3.589860,6.858286,4.804187,3.947298,-1.782042,-9.959483,8.759031,-6.886865,-0.236009,-9.623231,5.673762,3.197116,-6.945920,2.987244,0.492812,-9.789453,5.171924,9.477599,1.870435,-0.286887,3.945562,-1.402500,7.720235,-0.673462,9.811927,1.837835,-1.696546,9.316992,-1.632504,4.355225,4.351392,8.366725,6.668920,7.565768,0.867633,0.027513,-7.604574,-2.777708,-0.688388,6.482479,5.522231,-0.760672,7.833022,-6.566592,2.978123,-4.244757,8.927208,5.439319,-4.797123,-5.790296,-0.733206,-6.544184,2.398462,8.513154,-7.467050,-4.816416,1.939918,1.607475,-9.664698,-0.951737,0.363885,-6.940504,5.497048,-5.079734,-7.146133,8.688285,-4.240864,-9.499223,-8.732561,6.381869,-7.348552,2.469726,8.099559,1.971915,-2.400099,3.502920,-2.517265,6.421657,5.640008,1.956530,-0.622756,3.816535,-3.848379,-1.835756,3.996816,0.221697,3.188944,6.715559,5.305623,9.548717,4.974698,-5.194400,-7.407906,5.887027,3.352344,-4.440647,2.486024,-6.264640,3.895606,1.528343,-1.245372,-1.641795,4.717067,-7.154797,-6.608080,-0.194633,-0.332567,5.601720,-5.501215,8.783988,9.485853,7.615147,9.820500,8.507824,3.448274,0.470189,0.009526,4.018244,8.268258,-1.495181,6.700874,2.700681,3.006156,3.360696,0.781503,8.749417,-0.977277,-6.922040,-4.298636,-5.590596,-4.804320,4.799020,6.937976,-0.721233,6.930319,2.333231,7.094092,-8.992075,2.277139,6.776318,-0.635385,-0.376598,3.758574,-9.053132,-4.309471,3.993220,-4.703908,-1.945812,-2.806375,8.475545,0.986040,-4.003620,7.704609,2.752237,-3.786167,-2.506743,3.353191,8.694345,5.334633,-4.504404,-3.285560,-7.611661,5.537410,2.405538,6.345573,3.147087,9.346026,2.335180,-1.889737,4.994373,1.767031,-9.527628,-8.559478,-5.259174,6.500309,6.357887,-4.940675,8.835976,3.921409,1.763504,2.968461,8.663802,9.337040,8.792591,-1.959042,-4.556056,-3.943460,-5.961879,9.836025,-2.866377,-2.471431,-4.794079,5.223514,-9.764259,-6.384281,9.235009,-5.840655,-7.331142,-2.677198,5.609344,5.415451,-6.528804,-4.126437,-7.647031,9.210371,9.221058,7.989290,8.892276,7.213819,8.212972,4.673359,9.597777,8.202588,4.078730,6.480132,-1.502609,9.977752,4.771148,-0.692969,2.349057,-1.443997,6.322719,-7.236745,4.374461,-8.598812,-9.801395,2.595645,6.047638,9.275752,-5.754494,1.577862,1.576300,-5.422461,4.476633,8.471513,-0.522559,5.621138,8.870931,-9.883368,4.768197,0.025105,7.075230,8.911594,2.797380,3.785386,2.938334,6.802504,5.866734,9.800398,-4.036984,2.481270,7.571533,-9.181007,3.190396,0.382962,5.493191,-9.897128,3.563427,9.380922,-3.104503,6.889865,7.310386,6.888559,-3.996437,1.094601,7.589682,7.520284,3.913686,1.189263,9.159830,3.150130,8.647018,7.869542,7.111962,0.604564,7.319344,-6.395502,1.803959,-5.023089,-6.473847,-2.742218,-5.713263,-9.328996,1.478158,-5.204719,-5.346948,5.419571,7.693185,1.439446,5.357408,1.644434,3.558679,-5.468512,4.431503,-1.069323,-7.403544,1.188601,-2.263598,8.592337,6.403829,-4.491676,9.683671,8.325566,-9.391007,-0.266560,5.821252,0.372976,6.486475,-8.078869,-2.429236,-6.820705,9.631005,6.070463,-9.603198,-7.184078,9.495408,4.888615,-4.658635,5.179939,0.879430,3.415594,2.253480,0.685873,-2.026098,7.043540,-7.648222,1.027873,3.444616,-3.056024,4.049213,9.152577,5.981548,-3.759889,5.832879,2.552851,6.148847,-7.273115,4.119144,5.360819,4.744797,-7.707218,-2.730547,8.162561,-1.236415,0.096579,-9.041794,-9.665253,-3.819371,-8.796048,8.689535,-4.828892,-9.722549,9.633074,4.311824,9.980707,-1.787746,-1.204278,6.417100,-9.699941,4.886052,-0.700290,1.482806,-7.061424,2.502124,8.195915,-0.559222,1.830001,-3.277079,-0.181121,2.310885,-1.551365,7.040146,-2.095092,6.949725,-0.472962,7.811725,-6.744729,-3.165065,-8.795248,8.078311,-3.030417,2.827207,-6.492398,-7.397797,8.633895,-6.176410,8.082430,1.237872,5.522004,5.782731,5.762879,-2.182845,4.097157,-5.673453,-4.361885,6.163285,5.227790,-0.095701,9.245555,-2.402623,-3.319938,-5.721012,-6.468475,1.447504,-1.166821,-1.116800,1.950666,-3.071165,9.695720,-1.246070,-2.837948,-4.360695,1.982526,-3.135631,9.846543,3.271432,7.192171,-9.653650,1.707166,8.881642,-1.912009,-4.181836,-6.226753,-1.757285,4.939244,2.282438,-8.901609,-1.740147,-2.908980,-4.305613,4.565914,1.564378,-9.636616,4.843877,-2.555207,8.186902,-7.183711,-3.556650,-9.530937,-2.898787,-1.514442,-0.850720,3.737399,-4.373882,1.374480,0.436192,-8.796137,3.297473,-0.362496,9.673241,-0.933388,2.444346,-8.157178,5.003314,-8.014233,-1.040771,-7.298298,-7.514217,4.558230,1.645891,6.705156,-6.831456,-2.416094,-2.026810,-5.191304,3.476118,8.819887,6.419429,-6.963204,-8.672230,-5.723688,7.039001,4.841654,-4.775869,-8.994496,3.145966,-5.047167,-9.653612,-6.473786,-9.951526,-3.242147,7.967646,-9.358005,7.988973,5.705577,-4.230591,-0.328752,-9.128672,6.589426,6.901509,4.742080,6.529118,-7.153195,-4.767730,1.177593,6.996912,-9.312217,0.860299,8.626131,9.155787,-3.481890,-6.861265,-4.241091], dtype = "float32")#candidate|4304|(780,)|const|float32
call_4303 = relay.TupleGetItem(func_1324_call(relay.reshape(const_4304.astype('float32'), [6, 10, 13])), 4)
call_4305 = relay.TupleGetItem(func_1326_call(relay.reshape(const_4304.astype('float32'), [6, 10, 13])), 4)
var_4325 = relay.var("var_4325", dtype = "float64", shape = (7, 13, 4))#candidate|4325|(7, 13, 4)|var|float64
bop_4326 = relay.less(uop_4293.astype('bool'), relay.reshape(var_4325.astype('bool'), relay.shape_of(uop_4293))) # shape=(7, 13, 4)
output = relay.Tuple([call_4303,const_4304,bop_4326,])
output2 = relay.Tuple([call_4305,const_4304,bop_4326,])
func_4339 = relay.Function([var_4292,var_4325,], output)
mod['func_4339'] = func_4339
mod = relay.transform.InferType()(mod)
var_4340 = relay.var("var_4340", dtype = "float64", shape = (7, 13, 4))#candidate|4340|(7, 13, 4)|var|float64
var_4341 = relay.var("var_4341", dtype = "float64", shape = (7, 13, 4))#candidate|4341|(7, 13, 4)|var|float64
output = func_4339(var_4340,var_4341,)
func_4342 = relay.Function([var_4340,var_4341,], output)
mutated_mod['func_4342'] = func_4342
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4496 = relay.var("var_4496", dtype = "float32", shape = (1, 15, 16))#candidate|4496|(1, 15, 16)|var|float32
uop_4497 = relay.log2(var_4496.astype('float32')) # shape=(1, 15, 16)
bop_4505 = relay.logical_and(var_4496.astype('bool'), relay.reshape(uop_4497.astype('bool'), relay.shape_of(var_4496))) # shape=(1, 15, 16)
func_417_call = mod.get_global_var('func_417')
func_421_call = mutated_mod.get_global_var('func_421')
const_4510 = relay.const([[-1.526628,-1.199820,6.886221,-6.156503,5.182940,5.220441,-4.999776,-3.728382,-6.365001,5.924714,6.241912,-3.279769,-8.876436,4.548577,5.881987,0.939816,8.668815,9.479033,5.439161,-9.735689,9.947252,-2.759152,4.627419,-9.704696,0.975215,6.671216,-1.644029,5.052357,5.271216,5.793289,2.425868,3.468896,-7.921730,9.808607,-5.240330,0.392066,8.273165,-1.171848,-8.619737,1.768903,-2.507319,-7.010594,-2.858644,5.268609,3.363258,-6.241547,-9.426048,6.285499,-8.420096,-4.229727]], dtype = "float32")#candidate|4510|(1, 50)|const|float32
var_4511 = relay.var("var_4511", dtype = "float32", shape = (400,))#candidate|4511|(400,)|var|float32
call_4509 = relay.TupleGetItem(func_417_call(relay.reshape(const_4510.astype('float32'), [10, 5, 1]), relay.reshape(var_4511.astype('float32'), [10, 5, 8]), ), 0)
call_4512 = relay.TupleGetItem(func_421_call(relay.reshape(const_4510.astype('float32'), [10, 5, 1]), relay.reshape(var_4511.astype('float32'), [10, 5, 8]), ), 0)
func_4181_call = mod.get_global_var('func_4181')
func_4185_call = mutated_mod.get_global_var('func_4185')
var_4515 = relay.var("var_4515", dtype = "float64", shape = ())#candidate|4515|()|var|float64
const_4516 = relay.const([-0.265941,9.526944,-3.576934,-1.354324,-7.318307,6.635288,-0.722947,4.712561,1.552021,-4.163135,5.582099,7.177393,9.899495,-7.951886,1.315182,6.053468,-6.538495,-9.378712,-7.949658,8.343525,-8.116102,8.735196,-3.419922,-7.280673,5.734162,7.561656,-0.610908,2.742686,-1.024994,7.161591,2.595539,8.543612,3.909919,-2.521006,-3.528150,-8.059626,4.918801,-3.753980,-2.417908,7.055708,0.094482,-6.508607,1.534499,6.319201,-5.382284,4.208640,1.240541,2.835369,-0.499022,4.020441,1.475377,5.119490,7.083640,-8.037330,-5.619214,-8.705512,-3.893703,-8.010669,-7.487392,0.187228,-2.054861,-6.167448,9.019761,-7.120376,-5.292074,-2.373748,6.206247,-4.778841,9.822579,-4.157284,-8.081970,2.616158,8.598597,-1.079921,-9.597673,-7.294352,-3.143382,-6.418232,-7.314329,0.375418,-6.529606,-2.638443,-5.244425,5.397896,4.841100,5.064149,-7.811128,-7.274173,-0.755300,9.899935,-8.142241,9.014618,8.576232,-1.117069,-5.097140,-3.716579,-4.755311,-4.510688,0.234153,-1.349087,3.371058,-8.473344,8.672820,-7.120811,8.636850,-8.945699,6.520004,-8.144645,9.437125,5.268780,-2.941051,8.119092,-6.478821,6.056847,2.288797,0.418812,-7.350538,-2.582541,-3.079871,5.946769,-0.242078,-9.607652,-9.185284,-5.349918,8.632748,2.826525,1.289771,-0.706146,6.031379,8.539703,-0.537906,0.010190,-3.677028,-0.842941,-8.134875,-2.908551,2.245928,2.771228,8.610424,1.099143,0.044711,7.070770,8.608211,-5.579412,3.374698,3.730592,-5.653406,-2.033234,-7.893400,-0.347108,1.401518,-2.852086,7.100317,-9.040849,2.548079,4.202233,-5.343037,-2.774115,2.321777,-6.568552,-8.380390,-8.735188,0.795706,-7.187998,7.135541,-5.263176,6.146919,4.926667,-3.038354,-3.628492,1.085441,-8.108106,-6.534300,-3.249743,-9.628918,-9.813436,-3.312372,7.748265,-8.665007,-0.021038,-1.793886,-4.872084,7.679926,-7.563931,1.615747,0.792507,6.127053,-3.961333,-1.058430,1.380702,-2.777190,-3.415393,-6.018583,-3.939991,7.817299,-1.242114,5.260017,0.831647,-6.488221,2.743543,-6.500480,-4.655088,-1.217211,7.067519,0.811901,3.952577,6.730826,3.383223,-3.229250,-9.505303,-9.466612,6.072151,5.427017,-0.220338,6.314049,7.920036,-2.498987,4.988816,-3.666856,-6.922443,6.627918,4.459386,0.865754,-5.676247,-1.149337,1.633622,0.319720,6.279734,2.795860,-0.455060,0.622685,6.098013,7.392343,-4.945136,3.564118,-0.815571,2.638290,8.369576,-0.274676,-9.879701,-1.455843,4.077649,-8.967036,-0.207143,-0.296194,-8.676532,-0.403670,8.623662,-4.821957,-2.717339,-2.363216,-1.088854,-9.120567,-9.103737,9.584698,-6.740691,-1.163813,1.045479,-9.209684,4.124901,-9.027713,-7.244237,7.288466,8.883882,5.064200,3.898307,-2.807444,7.858521,-7.833188,7.965360,-9.696898,0.312315,1.610876,-2.365902,6.691844,-8.396960,0.739988,-1.247157,-1.393352,5.770553,5.151930,-3.827140,-7.926217,9.341650,5.005340,8.998152,-1.526414,9.770798,9.379945,3.404115,5.209746,1.910466,-1.715978,5.449987,8.685634,-8.860242,1.900598,-8.958662,8.620047,-9.931915,-2.275587,-9.424736,4.885255,-7.549968,0.479426,7.835094,6.603895,-1.658719,-4.445773,-6.993519,-6.094294,6.470322,9.853674,2.301570,2.319743,-1.185549,0.307927,-1.587688,-9.410338,-6.078063,-3.905136,-9.842550,-0.744186,8.793984,-2.549850,-7.130232,-5.937714,-8.599891,9.560153,-7.051470,-4.886554,-9.254696,-6.741006,-1.730097,0.686758,-5.255008,-7.195112,2.485708,6.317453,6.696867,-6.576520,-4.027625,2.709110,7.249406,3.678869,5.205697,-9.080042,2.779482,-9.866282,6.912805,-8.699860,9.795552,-4.478954,6.880109,3.673897,1.628026,-9.479746,8.877381,-5.095959,-0.976069,-0.756555,2.585192,3.816319,3.858185,-8.106692,0.780241,7.722680,0.437268,2.358373,3.915453,-7.527266,4.626066,5.473590,-1.981261,8.034521,4.788741,7.583792,-1.763533,9.300619,-8.352880,-8.299100,2.001078,1.288838,2.012613,3.162424,3.586777,6.909756,7.719045,7.699380,-6.005988,-3.207683,4.702616,3.504569,0.233780,6.692295,-5.660017,7.507832,5.569992,4.906256,-3.745843,-0.472235,-7.344230,-6.216678,-4.231629,0.107320,-0.411936,-8.600764,0.048935,2.858506,-1.104057,7.213053,-1.173781,-9.315598,7.878411,-4.414589,4.730854,9.949367,-4.168537,5.619785,-9.597217,4.516887,-6.618032,-4.352261,6.064273,-0.982297,-8.407850,1.169457,7.813774,1.090681,1.300921,-2.798004,-4.556938,-0.426629,6.210767,6.573806,-7.795482,-7.255296,-2.624038,9.281112,-1.369020,1.980566,2.137956,7.122028,7.091055,9.565152,-6.187196,5.241776,0.258015,3.907261,0.119209,-3.652335,5.317115,-7.693504,1.891756,-2.695495,-9.325857,6.755431,-3.244615,-2.516859,0.035219,-2.672686,3.971272,-6.055097,3.373621,9.789875,-9.049295,-5.768682,-6.916138,2.395813,-2.880410,0.431915,6.935258,-3.356650,4.425352,2.199101,-9.010520,-3.192703,0.453803,3.483296,-0.207947,5.205518,-2.596384,-1.400964,5.373069,0.016949,6.768520,-2.591359,9.017147,-5.697209,2.187174,5.382363,8.844930,5.328486,-1.639786,0.661347,6.886990,6.814076,1.532447,-6.722054,5.139021,-7.805800,-0.059014,1.557146,-0.341010,-8.447822,-3.623737,3.710259,2.171811,-8.772539,9.277771,-0.755227,9.925992,2.671915,6.333962,3.914727,8.625555,-5.962003,-0.877755,3.415426,9.605667,-5.543748,6.841330,-3.214020,-0.238708,-5.365201,-1.679392,-7.969892,-1.302986,-2.002902,2.346497,-3.309493,-9.092315,-5.311684,-1.646789,2.666179,5.930278,5.010155,6.399913,1.769770,2.277205,-5.052581,-2.373137,1.436321,-3.798517,-9.956578,5.571596,-6.175833,7.004531,-7.476969,-8.129889,-4.038676,8.632681,-9.454564,1.749772,-5.471274,6.369630,-5.839804,9.118117,-0.684588,-6.734455,2.435467,4.875767,7.344160,-5.449670,-6.531849,5.853796,-6.756816,4.607472,2.252088,-0.577368,3.390968,-2.971831,1.538772,9.037528,4.327744,-5.220491,8.356587,-3.104985,1.245952,-7.098465,9.071684,-7.364366,-3.780415,-9.117156,-7.556932,4.710153,-8.145374,9.711887,0.723202,4.523638,-0.554261,8.489818,7.460590,-9.126666,-4.989157,2.586946,-9.668753,0.110627,5.430583,0.259841,-6.399335,6.140340,-0.779373,-9.927454,6.928859,8.893340,4.863997,8.953118,-6.505910,0.232468,-8.056161,1.395274,-4.519029,1.136814,-9.786709,4.861789,7.646166,-1.635164,-7.365102,3.039468,-2.124259,5.264024,3.969448,5.822304,0.045714,-4.791558,7.884043,-1.029884,-7.068312,0.630986,-4.765898,0.524172,7.844721,-7.378556,-0.456312,7.568118,-5.990681,-6.793004,2.221807,6.353188,6.036577,-7.528917,8.758654,-0.202710,-1.131014,1.298035,2.730338,-2.237644,-9.684563,-6.819448,-8.712400,5.337155,-7.732021,-6.895497,3.880498,-5.600465,0.515526,4.205628,-8.364577,-8.299976,9.402535,6.355454,-0.786304,8.136300,-1.821893,4.558636,7.802712,5.812706,-9.661970,7.857328,-7.571917,-2.931966,-8.062335,-3.144783,-1.494495,1.096583,-6.545834,-8.182829,-3.657182,8.240025,8.848028,1.996232,-2.128463,-5.721496,-6.804237,-4.111715,-9.342399,-3.766430,1.753638,3.872184,8.862946,3.864328,8.811779,-6.056473,-7.635562,2.777530,-0.900584,-0.979226,9.560286,-6.129242,4.580599,-0.601194,7.547751,-6.012630,-5.804679,-2.538488,2.774463,9.649465,9.173805,-7.388763,-1.998635,5.637184,3.963131,4.193491,6.339532,-6.989479,-6.018123,-4.539355,-6.416638,-2.818813,-5.295157,-7.470049,2.769349,-8.501022,-3.934111,-4.732642,-3.058140,7.575097,1.088915,8.198880,-2.143989,3.172781,-2.572838,3.671631,4.822358,1.787405,-1.842291,9.425943,-8.064661,9.545322,-5.316385,0.111413,4.329351,-9.228034,8.390154,7.915794,-7.782015,-5.945459,-9.398231,0.409804,-3.157585,0.587387,-2.751844,-7.593980,0.241689,8.360636,5.095511,-8.198986,-9.901068,8.720753,-2.136342,5.226255,-3.074647,-6.253793,5.504305,-7.783339,-2.539914,7.669728,-0.734789,8.021697,8.973102,7.869496,6.471957,1.393461,4.898670,4.962542,-2.229677,-0.560453,5.227329,8.515696,-5.716623,-4.603177,-8.132505,0.554182,2.984183,-1.973296,-2.781450,2.753330,4.968564,4.027404,7.684127,3.546601,8.707842,-1.450758,-5.423370,-8.834347,1.042977,2.859526,-1.036370,-2.896861,-0.221851,-2.003748,9.119651,-5.280937,-4.360684,0.673434,7.583999,8.675579,-2.724673,2.211004,-7.885734,0.555099,-5.262102,9.994769,9.836843,-5.671078,-1.826898,-9.763086,-4.345092,-9.524103,-5.659232,-8.433199,-0.943835,3.849577,-2.149371,3.135527,-0.417913,-1.136309,-0.726372,8.617813,-7.247846,1.575006,-9.951875,-6.873958,-2.040030,0.948175,-4.982616,-0.784672,-2.122746,7.417633,-3.017770,0.709943,2.432477,6.768590,0.038144,6.846114,-3.700081,-9.193623,2.805582,7.205231,3.451253,-9.942084,9.065431,6.877174,-2.630780,-0.654213,5.493512,3.458378,3.575441,-3.719973,2.723156,-9.929361,-4.397871,-6.710716,6.769411,-2.936663,4.309128,-8.178995,0.006759,-2.882323,-9.839817,8.422374,-0.383862,-9.226443,1.863039,-1.650333,1.465606,6.058828,5.553711,7.722087,1.499461,4.834664,-1.921699,9.401090,7.882970,-1.223848,-5.266025,-8.877972,-4.347781,6.733398,7.936505,7.083768,-8.028777,1.599495,-7.112895,2.964605,-7.821459,-9.367046,-7.544503,-3.723621,0.936620,-4.344286,-6.105757,-2.779847,8.585494,5.995510,5.396189,7.451064,6.439532,5.881477,5.269573,2.007106,-3.425191,5.886544,-2.813031,-6.783762,-7.426928,2.912931,2.865137,4.604816,2.420646,-0.254162,8.804981,4.517699,-5.190339,7.971503,6.376234,3.515235,-2.447762,-7.322516,-3.239451,6.728647,7.323206,-6.629702,-2.944910,-3.583384,-9.763975,2.671820,-7.592453,-2.137819,0.287262,2.197395,-6.594621,-3.882047,8.906098,2.322364,-1.712257,-7.531716,-9.728370,-7.757873,-7.242735,-2.940197,3.246834,8.757393,-1.846046,-4.118211,3.754916,-2.074395,-5.240017,-4.491103,-7.261498,-6.102098,-6.275237,-6.535179,6.600906,-1.383383,2.716021,-2.267661,-3.899639,5.885390,7.609803,-0.694077,3.754726,-4.306339,-9.058720,8.716369,4.148417,4.828704,-6.946837,-6.189833,-7.667114,4.192232,4.620580,0.125870,0.087195,5.257059,-4.843547,8.182191,-8.629083,-1.278033,5.071128,7.798038,4.353837,-1.230630,2.978106,4.452804,8.013946,5.117883,-8.768582,-6.942861,6.018801,-5.301473,-6.367610,1.955125,6.737823,8.249215,1.418753,7.163344,4.678782,-1.214533,-2.906768,-9.779083,5.341704,1.698762,-8.538647,5.627642,7.025541,-7.173070,-4.936071,-2.286390,3.831933,-9.357115,6.519552,8.140886,5.185391,5.170993,4.137470,-3.837901,5.707920,-6.596845,9.761655,-1.855274,2.274491,-7.735893,-1.075405,3.188120,-3.802167,4.452742,-7.936687,-8.300931,-7.143686,7.405361,-7.135329,-7.151031,2.488640,9.908595,0.269554,4.807912,-9.241324,-7.862968,4.913495,-9.384518,2.512378,7.217492,-4.778349,8.638722,1.867782,-0.847888,-1.828993,9.619193,1.447629,1.931849,-8.698606,1.747377,-4.486466,-0.769863,-8.387469,-9.024588,-2.062518,5.045529,5.062851,2.282128,2.323972,-9.751644,4.979243,-0.104442,9.364543,7.108480,-6.085425,-9.795332,-9.304628,-2.896297,-4.316191,-0.265893,-3.652049,1.858985,-4.278652,-8.342795,5.673455,-2.719532,2.179988,2.082663,-7.294917,-3.587324,-4.329104,6.047281,3.337439,2.569463,-1.672255,-0.428973,6.575231,1.168539,8.546116,8.392794,-9.916201,8.504885,-9.367120,-2.602386,4.121369,-7.967008,-2.665982,-0.829521,9.453312,0.880685,2.110181,9.284312,1.121873,-4.823362,-8.985464,6.178760,9.297522,-8.434541,-8.124412,-3.697553,-8.664302,4.130096,4.692739,-1.025815,2.531268,-3.921651,-5.366881,5.278364,-1.809498,-2.875475,0.234943,-2.438480,-9.940915,8.173535,5.963252,-1.767344,-0.840822,-8.648273,5.305767,-4.510350,-9.029545,7.773329,-4.081589,3.727327,-1.101536,-4.861320,7.994233,0.614992,6.079613,-0.789372,-1.760927,-3.984737,-9.233039,-7.042194,-2.830240,-3.974380,-4.931494,4.848356,-8.582422,0.235316,-3.897399,0.084104,-5.525230,6.608054,5.248573,2.574797,-0.541164,-5.907129,-5.497077,-5.874091,1.226031,-0.123273,-1.502291,7.485908,-8.424177,6.861397,-1.392012,-5.257933,9.782797,-3.039588,-3.129676,3.286405,-1.786556,7.117344,-0.850407,0.870329,4.336319,2.571471,7.108407,-6.486512,-3.452876,-0.623681,-4.226008,9.929584,-2.661445,-6.527777,8.138628,9.895388,7.863547,6.566603,-4.166252,-0.056054,-5.056092,2.945450,-7.340174,5.629619,9.178809,8.319852,-2.641276,-0.273446,-9.299879,9.941260,-9.709864,2.120773,-4.907359,2.757120,5.028177,-9.504642,-8.936939,0.273974,7.767647,3.505226,-8.745374,2.489698,3.445487,0.666222,-4.066160,-2.341394,5.263337,1.279279,-8.012757,-2.363303,-6.605741,0.175802,-0.927096,0.724248,9.285245,8.783515,7.952725,-4.932107,-2.659563,-9.565897,8.284746,0.604584,6.014991,-3.104641,5.599152,2.380057,7.593801,-7.338800,-1.361085,4.117829,-2.907478,4.134630,5.507483,7.178266,-5.412217,9.733735,-2.779520,-5.774248,5.468571,2.813339,-9.575344,-2.016383,6.415813,1.500026,-1.508455,0.277565,0.610562,-9.247043,-4.635505,-2.736067,5.720655,-6.448376,-2.421263,8.112375], dtype = "float64")#candidate|4516|(1280,)|const|float64
call_4514 = func_4181_call(relay.reshape(var_4515.astype('float64'), []), relay.reshape(const_4516.astype('float64'), [16, 5, 16]), )
call_4517 = func_4181_call(relay.reshape(var_4515.astype('float64'), []), relay.reshape(const_4516.astype('float64'), [16, 5, 16]), )
output = relay.Tuple([bop_4505,call_4509,const_4510,var_4511,call_4514,var_4515,const_4516,])
output2 = relay.Tuple([bop_4505,call_4512,const_4510,var_4511,call_4517,var_4515,const_4516,])
func_4518 = relay.Function([var_4496,var_4511,var_4515,], output)
mod['func_4518'] = func_4518
mod = relay.transform.InferType()(mod)
mutated_mod['func_4518'] = func_4518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4518_call = mutated_mod.get_global_var('func_4518')
var_4520 = relay.var("var_4520", dtype = "float32", shape = (1, 15, 16))#candidate|4520|(1, 15, 16)|var|float32
var_4521 = relay.var("var_4521", dtype = "float32", shape = (400,))#candidate|4521|(400,)|var|float32
var_4522 = relay.var("var_4522", dtype = "float64", shape = ())#candidate|4522|()|var|float64
call_4519 = func_4518_call(var_4520,var_4521,var_4522,)
output = call_4519
func_4523 = relay.Function([var_4520,var_4521,var_4522,], output)
mutated_mod['func_4523'] = func_4523
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4739 = relay.const([[[-2.798283,5.976979,1.412042,6.766254],[-0.460837,9.514680,5.596498,-9.054903],[4.318242,3.464860,-2.581670,5.404144],[-2.882340,-8.818062,2.750596,-4.181018],[7.238314,-4.506804,6.917288,7.885391],[-0.244364,3.825347,2.135754,7.643834],[-8.220755,7.474055,-1.324526,4.227266],[-1.888379,7.642425,3.332435,6.333545],[-0.508927,9.871887,3.860117,7.465852],[-5.203231,-7.676018,6.063854,-2.429265]],[[-5.392784,-4.167131,-3.531893,6.430112],[1.645477,-7.353646,-4.482239,-8.301719],[8.809369,9.762474,-8.511636,6.859467],[2.397592,-9.176614,4.500644,-9.396538],[-0.303243,-5.482739,-1.679929,-1.021780],[7.676723,-7.367904,-4.178164,-8.073638],[1.807533,1.256297,-9.387311,-0.958026],[-8.854505,-0.930365,7.323548,4.653440],[-0.714161,-7.831516,4.104440,-4.320977],[3.412864,2.433695,1.707161,4.247307]],[[4.836341,-7.054810,8.682325,9.282658],[-0.522617,6.714572,9.769337,5.847445],[4.122693,-4.827728,-4.733485,4.628843],[-3.689264,-7.570283,-6.346020,-2.730649],[-3.201754,1.947986,2.499253,8.965567],[5.267620,2.283365,9.593200,-4.686558],[-5.936227,3.722461,0.447338,-6.375759],[5.510281,-7.445751,-6.039839,4.825328],[7.257235,0.516842,-5.608251,-8.017151],[7.161047,-7.774507,3.272496,1.751386]],[[3.176598,-9.059058,1.875937,-0.454168],[6.981873,-8.466918,8.378670,-1.443402],[9.846560,6.235711,-0.630989,2.614685],[0.184276,-9.099941,-4.979544,-9.871734],[8.932180,-9.098083,1.362770,6.210816],[0.190735,8.970140,-2.219799,-8.060032],[2.493311,6.893363,4.071944,3.639929],[-2.788931,7.791950,-9.743021,-5.074007],[9.089682,-7.166486,-2.350634,1.012811],[-2.762945,-1.604569,0.628839,-1.653413]],[[6.031534,-6.310543,-2.889492,5.023810],[-8.139534,6.101133,4.210401,-3.068459],[-4.401506,4.723855,-7.307122,5.949478],[1.056730,2.856363,-1.351650,3.344101],[3.052198,-1.570964,-4.671289,-6.984632],[0.181967,9.402837,-3.911642,7.630327],[-4.218606,7.908543,3.367040,3.687016],[-7.435875,7.318047,-7.069709,-3.010053],[0.410909,7.289591,0.669701,-5.398045],[6.428951,9.421598,0.513531,9.376220]],[[7.151169,-0.904702,2.240605,-8.097139],[9.261460,-7.596301,-6.489057,8.266214],[4.123280,9.501357,1.888823,6.188581],[3.242641,-5.527223,1.964931,6.215626],[-4.695985,-7.284866,9.984547,5.601752],[-4.490727,9.176543,1.717562,-4.202870],[5.049317,3.681591,9.383383,-1.842222],[7.930671,4.851698,-7.795122,9.174623],[2.583883,-5.583570,-0.299093,0.924944],[6.413882,-6.774492,2.619418,3.291290]]], dtype = "float32")#candidate|4739|(6, 10, 4)|const|float32
uop_4740 = relay.acosh(const_4739.astype('float32')) # shape=(6, 10, 4)
bop_4743 = relay.greater(uop_4740.astype('bool'), relay.reshape(const_4739.astype('bool'), relay.shape_of(uop_4740))) # shape=(6, 10, 4)
uop_4746 = relay.sin(const_4739.astype('float32')) # shape=(6, 10, 4)
func_1815_call = mod.get_global_var('func_1815')
func_1817_call = mutated_mod.get_global_var('func_1817')
var_4750 = relay.var("var_4750", dtype = "bool", shape = ())#candidate|4750|()|var|bool
call_4749 = func_1815_call(relay.reshape(var_4750.astype('bool'), []))
call_4751 = func_1815_call(relay.reshape(var_4750.astype('bool'), []))
func_322_call = mod.get_global_var('func_322')
func_325_call = mutated_mod.get_global_var('func_325')
const_4753 = relay.const([-3,-10,-4,-8,-6,7,2,-6,6,-8,-2,-1,7,7,9,-6,-2,-9,-3,-9,10,5,-2,8,1,-1,5,9,8,-7,7,7,-2,-8,-3,-3,3,-9,-1,10,-1,8,3,-7,7,-5,-1,-6,1,9,-10,-9,2,-7,4,-6,-10,-2,-2,-3,-5,3,-3,1,2,-9,2,-5,-5,7,2,6,-8,5,7,10,8,-10,-4,-4,8,-9,1,-5,6,8,5,-10,-2,2,-4,-3,-6,3,3,6,-1,4,-1,-10,2,7,-2,10,-3,-3,-7,-9,-1,-4,-2,-6,7,4,-8,5,2,7,8,-8,-4,-9,-9,-3,-3,-3,-7,-7,-8,2,-7,7,-8,3,-4,8,2,-8,-6,-1,9,-5,6,3,-4,1,-2,9,5,-8,3,-8,1,-7,-6,-9,6,-1,5,6,9,-1,6,-2,3,9,-4,-10,2,6,-8,2,7,4,-9,3,8,10,-5,-4,-2,4,-1,-3,-4,10,1,3,9,-4,-8,8,-1,9,-3,-6,-7,3,7,-10,6,-10,-3,-9,-2,1,-9,5,9,8,8,-9,4,-4,1,-1,-5,-3,6,3,4,8,-4,3,-7,-7,5,-10,9,4,-8,-6,8,3,3,1,-9,1,10,-7,5,1,-2,-2,5,-3,-9,-5,-10,10,-4,3,8,7,7,6,-9,-3,8,-2,-9,7,3,6,2,-9,7,-2,-5,4,4,-4,-8,4,2,10,-10,-1,9,-8,-3,9,-2,-8,9,-9,-3,4,1,7,3,-5,2,-5,5,-4,-4,-10,-4,-3,10,4,8,5,7,5,7,2,-7,-2,4,-1,-1,-5,9,7,-2,3,8,-9,7,-4,5,-6,5,-3,8,-7,4,3,10,3,1,-3,-3,6,8,4,8,-6,-2,1,-2,8,-10,1,2,-5,-9,4,1,-2,1,-2,8,1,-6,9,-3,-8,-9,-5,3,4,8,-4,7,10,1,-7,2,10,-4,-10,7,8,-6,-7,-2,-1,-10,-9,-10,-4,-3,-2,3,-4,3,2,9,8,-6,4,-5,-8,9,-1,-8,-10,10,-7,5,9,-3,-8,2,8,10,-6,7,1,5,5,-10,6,6,-2,3,9,-2,-10,4,4,2,-10,-8,-4,-6,4,-1,-4,4,-8,-7,2,-3,-6,10,10,4,10,-4,2,-3,-3,-9,-5,-3,9,-9,1,-3,8,1,-5,1,-6,2,-4,6,-3,-6,-9,1,-1,1,2,-1,9,-10,4,4,8,-7,2,2,2,6,-1,3,5,5,8,-10,5,-5,-3,10,2,-6,5,-4,7,10,4,9,-7,-9,-10,4,-10,4,-6,7,-4,-6,10,-3,7,5,7,3,10,-9,-4,6,1,-7,4,7,-4,6,1,1,3,1,1,3,9,-2,6,5,7,4,-6,1,4,-6,-7,6,4,-1,3,-8,10,3,7,-3,2,10,-10,1,-8,-2,-5,-6,-6,-6,5,-9,-4,-10,2,7,-3,-5,-8,9,-1,-3,-1,-5,-8,-6,-5,-7,-9,1,-2,-7,-5,-10,-9,1,1,-8,2,1,-4,-4,-2,-9,-10,2,9,9,-2,-9,9,2,-3,-4,4,7,-10,7,2,1,-6,-5,4,1,2,-8,-1,1,-1,-10,-8,-2,-8,2,-7,-3,8,8,-2,10,8,-3,8,-4,6,-3,1,-7,-4,-8,-2,2,8,1,-10,4,-9,-8,8,6,-3,2,-4,-2,6,7,-2,-5,2,2,7,9,-10,4,10,6,1,-9,5,-1,-3,8,-1,8,10,-5,-6,6,-3,6,2,-7,9,6,-7,-4,9,-6,6,-4,-3,-7,3,-5,-4,2,-4,-7,-4,7,-3,-2,5,-5,-1,1,-7,-1,2,9,-8,9,9,-4,-10,6,2,-8,-5,1,-9,8,-9,-8,-6,6,-7,5,-1,-9,-10,8,3,10,-6,-2,1,3,-10,10,8,-9,1,1,2,6,-4,-3,-8,-5,-4,-1,8,7,-7,-5,5,9,9,-9,-9,3,7,10,-1,-2,-1,-1,9,8,-7,8,-6,-5,7,6,-8,9,6,-3,-2,3,-7,2,-2,-1,-3,10,-8,-4,10,-2,10,-4,-1,-3,-3,8,-1,-8,-3,2,8,5,9,-2,1,7,-5,8,-9,9,-7,4,9,3,-8,6,-8,-3,-10,4,-7,3,-4,-8,-1,-7,-5,-8,-2,6,5,8,-3,-10,4,-6,-7,-4,9,-5,10,9,-2,10,8,-4,8,-8,-2,7,4,-8,-4,1,-4,-6,-8,-2,3,-2,9,-6,7,1,-2,-5,4,7,-6,3,-7,-6,5,-5,9,-1,-3,-5,-1,-10,-5,-1,-8,6,1,6,8,2,8,-2,-7,3,-10,-2,5,5,-7,-6,7,1,-1,5,-6,3,-8,-1,9,-5,-4,-1,-9,6,5,2,-6,-1,9,8,-6,-1,7,-7,8,5,-9,9,-3,3,-1,-9,8,-3,7,-4,4,5,-9,-8,-6,-9,9,2,-6,-9,10,3,-9,4,-10,7,8,-5,-6,-6,-6,-9,6,7,4,9,4,-1,8,7,8,2,-7,4,10,10,-6,8,-8,-4,-1,-8,4,-7,7,-10,1,-2,9,-4,8,2,2,-8,7,5,-4,4,-2,-10,-7,5,-2,-8,1,-7,-5,2,1,8,-1,-7,-5,3,-3,6,3,10,6,-4,10,-7,10,-4,9,-8,-6,7,7,-9,-3,10,8,-1,8,3,-7,-4,-2,-8,2,-3,-3,10,-2,-8,-5,3,10,8,-7,9,3,-9,-4,6,-4,-6,1,5,-8,8,-3,7,-3,5,-7,-4,-8,5,-1,-1,10,-10,-5,4,-9,-7,3,8,-10,-8,7,-9,-8,-8,3,-5,-7,4,1,-5,10,3,-7,-1,-3,-6,-4,5,9,-10,5,7,-10,3,-1,-2,-2,4,5,8,6,-8,1,2,-9,2,8,5,2,-1,-8,-4,9,10,5,2,4,-4,5,2,-8,7,8,6,-10,5,-2,-10,8,7,-10,9,-10,8,8,-9,-8,2,8,8,-5,-8,3,-7,10,6,-2,-3,-7,8,-2,-2,3,4,2,-1,-4,-5,7,-10,8,8,-3,4,1,-7,-9,1,5,-1,-9,5,1,2,1,-6,10,-1,-4,-2,7,8,-8,-5,-8,9,1,3,-3,-4,7,-7,6,9,-3,5,-10,-3,5,3,-8,-1,8,3,-8,-8,-8,1,3,2,-1,-3,3,9,-7,1,7,-6,-3,6,7,6,1,7,-7,7,9,9,9,10,-2,-3,3,4,10,7,6,-5,3,8,-5,10,-8,-6,8,-4,8,-9,-1,-7,5,-10,-7,7,-7,2,1,-5,-10,7,-10,-8,2,-9,2,-4,8,-7,9,7,-10,-9,10,1,9,-5,1,-5,-3,-6,8,2,-5,5,5,-3,2,8,-8,-9,7,3,-9,4,5,-5,-1,-1,9,10,9,-9,-5,-10,-5,9,-4,3,3,5,7,-10,-8,5,-8,-1,8,7,-8,8,9,7,-2,-9,8,-4,4,5,7,-9,-5,-4,-2,-8,-2,-4,-6,6,-3,-4,9,-8,-1,6,3,5,-10,2,-3,-4,1,-8,1,4,9,5,-5,2,7,6,-7,-9,1,9,-4,-1,-1,1,-10,-5,4,-8,4,6,2,-1,-4,-4,-2,1,5,2,-8,7,-9,-1,-4,-1,-1,-10,-9,-1,-3,-10,-9,-2,10,2,6,-7,4,7,7,6,7,10,-1,10,8,-9,-8,1,7,-7,-3,-10,-2,-4,-7,8,8,-1,-1,-3,1,-5,-4,-1,10,-6,4,-9,-4,-7,3,4,-5,10,-8,-6,8,-9,8,5,-8,10,-6,-8,1,-1,3,6,2,6,1,-10,5,-3,-1,-2,7,1,-2,4,-6,-8,2,-7,-9,6,-6,1,6,-4,-2,6,-8,-5,-7,4,5,10,-5,4,1,6,-6,9,-2,-1,-9,6,-5,10,3,5,7,5,-4,5,-9,-5,9,7,6,6,4,-3,-4,-10,8,-4,3,-4,-10,-4,-10,-4,-10,-10,8,2,-9,-2,9,-1,9,3,-7,-1,-7,-6,2,8,10,10,6,-1,-8,-10,-6,5,6,-7,6,10,3,-10,5,-8,-6,6,-2,-6,1,-7,-7,-4,2,-6,9,10,1,8,-8,2,7,-7,-4,-9,-1,3,1,-2,1,1,-5,4,1,-3,-10,-4,-4,8,-5,4,5,5,7,1,7,-7,-3,10,3,-4,8,-10,10,-10,-6,1,4,-9,5,-8,-2,-7,-6,-10,8,-1,-1,-1,-10,-5,7,-10,-4,-3,-1,-3,6,9,-7,-8,-10,-5,2,3,7,8,4,9,9,8,3,-2,-3,10,9,-7,6,1,8,-10,1,-10,-8,-6,-1,4,8,-4,6,-3,1,-5,1,-5,-1,3,4,1,-4,-6,1,-10,7,-2,-5,9,4,-3,3,4,-4,8,-10,-10,3,-9,10,-5,-3,-2,-3,-6,-7,2,8,4,10,-2,10,-5,1,-9,-5,-8,3,-9,-10,-3,-4,9,-10,-6,6,1,1,8,1,-3,-4,-5,10,5,-8,9,3,6,10,4,-1,1,-2,-3,8,9,4,1,7,4,-6,5,-10,3,-2,-7,1,-4,6,-7,-1,8,-10,1,-9,-1,7,-4,-9,-8,-3,6,2,-8,7,-7,-2,6,-8,-9,2,-9,6,-10,2,7,-5,-9,5,9,5,-10,1,-8,5,-3,7,-9,-9,9,-9,5,1,2,5,8,5,4,-6,-4,-10,-9,3,10,-7,1,7,-9,-4,-4,10,7,-2,3,5,-10,-4,-4,6,-9,4,10,-8,2,2,8,-10,9,-8,-9,-10,2,5,-1,9,-8,1,-6,1,-10,-4,4,3,-5,6,8,10,-9,3,9,-3,-8,-7,3,2,10,2,-1,9,-8,7,-2,5,3,-5,-1,-1,3,3,7,-9,-3,-3,6,10,9,-1,6,4,3,4,-10,-4,5,6,5,9,6,4,-5,7,2,7,-3,9,-2,3,10,-4,-7,6,-6,3,8,4,-2,9,9,3,-7,-10,-7,-3,-10,-1,7,-10,2,-7,-1,-6,-3,6,-9,4,3,-8,-6,-9,-8,-3,8,10,-7,2,9,10,3,6,8,9,-3,-4,-8,5,-5,-2,4,-5,-10,-10,7,3,-9,-1,8,-8,6,1,-7,1,5,-7,7,9,-8,-8,-10,-2,-9,-5,2,-9,-9,4,7,10,-1,10,-6,5,9,-9,-4,9,6,2,9,-8,-2,-4,8,-10,8,6,10,-10,-5,-9,3,-6,-1,-9,-10,9,-9,-2,7,-7,3,-1,-5,3,1,2,-1,3,9,-4,-8,2,6,-6,5,1,7,2,-4,-5,-6,-1,7,10,-7,-4,7,-4,-9,9,-6,-3,-2,-8,-9,-3,1,-3,9,4,-6,-3,-6,10,-9,-1,-7,9,-1,-6,-9,-5,-1,1,-2,6,-5,2,7,-7,1,3,-6,7,-7,-8,-10,-9,3,-2,4,2,-8,9,8,-4,-7,7,7,-9,-7,-5,1,-1,-1,-7,1,-2,-6,6], dtype = "uint64")#candidate|4753|(2100,)|const|uint64
call_4752 = func_322_call(relay.reshape(const_4753.astype('uint64'), [14, 10, 15]))
call_4754 = func_322_call(relay.reshape(const_4753.astype('uint64'), [14, 10, 15]))
bop_4760 = relay.not_equal(uop_4746.astype('bool'), var_4750.astype('bool')) # shape=(6, 10, 4)
output = relay.Tuple([bop_4743,call_4749,call_4752,const_4753,bop_4760,])
output2 = relay.Tuple([bop_4743,call_4751,call_4754,const_4753,bop_4760,])
func_4769 = relay.Function([var_4750,], output)
mod['func_4769'] = func_4769
mod = relay.transform.InferType()(mod)
mutated_mod['func_4769'] = func_4769
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4770 = relay.var("var_4770", dtype = "bool", shape = ())#candidate|4770|()|var|bool
func_4769_call = mutated_mod.get_global_var('func_4769')
call_4771 = func_4769_call(var_4770)
output = call_4771
func_4772 = relay.Function([var_4770], output)
mutated_mod['func_4772'] = func_4772
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5036 = relay.var("var_5036", dtype = "float64", shape = (15, 9, 10))#candidate|5036|(15, 9, 10)|var|float64
var_5037 = relay.var("var_5037", dtype = "float64", shape = (15, 9, 10))#candidate|5037|(15, 9, 10)|var|float64
bop_5038 = relay.floor_divide(var_5036.astype('float64'), relay.reshape(var_5037.astype('float64'), relay.shape_of(var_5036))) # shape=(15, 9, 10)
output = relay.Tuple([bop_5038,])
output2 = relay.Tuple([bop_5038,])
func_5041 = relay.Function([var_5036,var_5037,], output)
mod['func_5041'] = func_5041
mod = relay.transform.InferType()(mod)
mutated_mod['func_5041'] = func_5041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5041_call = mutated_mod.get_global_var('func_5041')
var_5043 = relay.var("var_5043", dtype = "float64", shape = (15, 9, 10))#candidate|5043|(15, 9, 10)|var|float64
var_5044 = relay.var("var_5044", dtype = "float64", shape = (15, 9, 10))#candidate|5044|(15, 9, 10)|var|float64
call_5042 = func_5041_call(var_5043,var_5044,)
output = call_5042
func_5045 = relay.Function([var_5043,var_5044,], output)
mutated_mod['func_5045'] = func_5045
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5177 = relay.var("var_5177", dtype = "float64", shape = (11, 11, 15))#candidate|5177|(11, 11, 15)|var|float64
uop_5178 = relay.asinh(var_5177.astype('float64')) # shape=(11, 11, 15)
output = relay.Tuple([uop_5178,])
output2 = relay.Tuple([uop_5178,])
func_5182 = relay.Function([var_5177,], output)
mod['func_5182'] = func_5182
mod = relay.transform.InferType()(mod)
mutated_mod['func_5182'] = func_5182
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5183 = relay.var("var_5183", dtype = "float64", shape = (11, 11, 15))#candidate|5183|(11, 11, 15)|var|float64
func_5182_call = mutated_mod.get_global_var('func_5182')
call_5184 = func_5182_call(var_5183)
output = call_5184
func_5185 = relay.Function([var_5183], output)
mutated_mod['func_5185'] = func_5185
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5194 = relay.const([[[4.328906,8.813930,7.926681,8.417695,6.363215,8.192935,4.722447,-5.371287,-0.043223,2.963278,-7.317013,1.328216,-4.801005],[1.983163,5.700617,7.657503,-3.727770,-7.165185,5.533786,9.759408,-0.321278,1.410075,-2.476887,4.431139,-0.687737,-1.838628],[9.679743,-2.856435,4.175548,9.062315,6.790825,4.458541,-5.817201,9.415771,4.387597,-2.218041,4.917158,0.098073,8.140505],[-6.496265,-9.444087,-8.118298,-7.952941,9.474368,-6.498411,2.680121,-5.929909,-5.313836,-8.682048,-5.693093,-3.116390,-8.536764],[-5.671083,8.994686,-3.087117,5.133373,8.575631,-9.706370,3.052936,8.409520,6.926746,7.462650,4.689140,-7.104778,4.662286],[5.134223,2.543230,4.300709,7.987284,4.049478,-2.818098,-3.289892,-2.874892,0.743106,3.901358,4.313007,6.531464,-4.261856],[-9.726363,0.756736,0.627607,-1.846035,-0.010753,-8.618288,-4.004861,6.886814,7.362253,-5.210149,1.759339,6.764125,-6.169350]],[[3.199003,0.982502,-1.314330,-9.325660,3.595838,-2.709350,-2.602869,9.418104,8.161569,-7.392261,-2.165647,-8.559999,9.844403],[-5.550514,-3.174035,2.458640,1.028645,0.674486,9.764240,9.600502,9.101808,-0.180274,-7.249020,0.793775,4.433592,-3.840461],[4.777046,8.337775,-8.855428,5.446478,-6.234482,-3.206242,6.339480,-7.518162,5.296983,9.344655,7.363549,-1.033027,7.753650],[4.963366,3.661852,-0.196143,3.672120,1.774001,2.252724,-3.572183,-1.209527,1.129862,6.636905,-4.590137,6.504121,2.278098],[7.262980,-3.789297,9.115703,6.423049,-2.182495,9.574654,9.564081,7.076774,4.004608,8.373563,0.839621,4.900739,-7.370898],[2.388448,0.583777,-9.313036,0.918833,0.572902,9.902720,9.728357,-6.373256,7.877530,-9.466830,7.009833,-8.518723,6.641846],[7.469100,-2.715185,-4.007010,-5.387823,8.094918,-4.561278,9.429630,6.329658,-7.155740,-2.773374,-8.046530,8.960910,2.262352]],[[-1.312860,6.972219,9.571615,4.716540,-2.844879,1.100992,8.834678,2.021451,6.669556,-6.683243,1.479104,-5.577503,9.054440],[4.348077,6.733318,3.866676,3.555104,3.961736,-1.963796,-2.662790,-5.288689,5.732427,-6.618021,7.815668,9.596544,2.981436],[-6.399850,1.678601,-0.790619,-6.084044,2.823974,4.028876,-0.266227,9.678731,7.756957,1.339739,2.934800,-6.318213,-4.341008],[-0.424582,0.303567,-1.667199,1.367917,9.423056,3.428040,2.153411,-0.382349,0.718273,4.706488,7.798052,-5.470980,-4.796747],[8.526048,-8.595784,-6.128526,9.680939,-4.729002,8.508095,7.489713,2.685420,9.896997,8.560219,4.516865,-7.082695,7.245912],[-4.351228,9.202527,-0.939166,4.338072,-9.281198,7.708587,9.979692,5.638603,2.745720,3.344320,1.417679,4.445155,-3.485431],[4.733563,1.628063,-8.942908,3.146799,-6.420808,-9.671196,-1.923381,6.197936,1.006655,4.875291,6.041762,7.617726,3.172216]],[[9.243843,-3.340439,9.830430,7.945123,-9.834564,-7.869963,4.589160,7.450394,-2.064518,-7.099670,9.634972,-3.378319,-7.761058],[0.380376,7.690789,6.063939,1.142505,-1.569964,1.451662,9.414097,-8.912067,8.233513,-8.353406,1.645868,-1.048299,-3.318346],[4.442431,-8.307991,7.341657,-3.455816,-4.174705,1.573909,3.656598,2.410063,3.047381,-5.754148,-3.643661,8.123521,6.037553],[-5.244169,-1.436993,6.957646,0.418489,-0.775012,-5.795619,9.251023,-4.598097,-4.550113,2.921846,-8.417227,4.429330,-4.549035],[0.397567,-5.288041,-9.156888,-2.153346,-7.942226,0.924578,-5.565443,-3.316378,-4.696228,5.179154,-6.867696,-9.490662,0.087377],[0.263424,5.340113,9.147536,1.490500,2.103509,-0.507507,0.691124,-6.491405,-4.492732,-5.140473,9.882167,6.520732,4.185375],[-6.429182,6.307605,-1.541085,-2.227247,-2.209551,-9.383652,-4.748038,1.112029,-9.156686,7.231902,4.376930,4.764042,-9.529659]],[[-2.114738,9.988940,0.584721,2.987121,-0.306274,3.838754,-6.962154,-4.053894,-0.761568,-3.522919,2.715755,-3.610758,7.749988],[-5.365632,4.588084,2.348474,-2.846819,6.637798,9.554874,-0.496577,-0.561421,-6.989443,0.670210,-6.676710,1.077986,-5.572747],[2.543060,2.357473,-7.005597,7.785550,-4.865613,-2.982302,1.735834,8.199996,-6.632753,-5.805683,2.212480,6.340380,8.293932],[-2.388828,0.867318,6.176547,6.620916,2.059716,0.165830,0.371550,-7.105579,-0.473822,2.691330,-3.720127,-3.319096,7.851007],[3.404494,-0.359351,-0.746677,-9.655746,3.918169,-5.401889,-2.568587,0.931453,-2.941248,-3.656495,-3.948205,-2.060406,-6.739423],[1.354758,-2.160325,-8.661663,-5.545737,-2.770447,-7.248154,-0.569540,5.167789,-6.714968,-7.824123,9.661736,0.881451,5.098454],[-0.757961,8.624727,-4.169324,4.711882,0.897374,5.822452,1.442904,-6.768113,-2.952140,5.539654,5.247896,2.410543,6.837640]],[[-4.812626,-2.385742,-6.729762,-4.647921,5.626165,8.507192,0.470185,3.977974,-5.728204,-4.359474,-3.809629,6.719779,-9.899823],[9.298678,-6.549122,-9.350290,0.822458,8.066458,-6.726411,-9.325196,-5.661930,-6.667981,-7.975726,-2.927822,-7.967465,-9.811009],[2.028395,8.856090,-1.536660,-1.119989,4.190801,-9.840376,4.559232,5.608375,3.496277,-1.531596,4.330580,1.767077,-4.199077],[-7.455908,-5.197629,7.535040,-9.371580,-6.673644,7.690790,4.263623,6.206561,-9.081344,1.151228,-4.629256,9.969519,5.531126],[-0.629237,-0.045948,-9.675801,1.033145,0.923125,7.173273,6.639644,6.856918,-5.654144,-4.529533,-4.475711,-6.255304,-3.995738],[-4.465492,3.275869,-6.637815,-5.534967,-9.984647,9.993639,8.641702,-6.329678,-0.269214,-2.774936,1.984058,-3.936533,1.534130],[-0.198652,4.236046,-2.329197,-7.067590,5.929256,5.183371,3.412503,-8.249205,-5.250493,-2.971684,-0.734573,-3.635267,-3.718967]],[[8.306856,5.406710,5.213466,1.429781,-7.800310,-5.810379,7.307762,9.932782,0.180648,3.656726,9.442134,5.562806,-4.838828],[-3.319983,5.762551,-0.944631,-8.245966,9.347239,8.441632,-4.488534,-5.613869,-9.260584,-0.484521,2.137851,6.013464,6.778756],[-3.112759,-9.009832,8.788559,5.055640,5.243966,9.523015,-9.375435,1.199960,7.334154,0.652389,-3.244886,-5.904520,-0.467956],[-5.407128,-5.234794,-5.139738,-6.538609,5.928015,-7.776870,-9.291486,7.352108,4.752522,-7.542436,1.561815,-0.917331,-0.249305],[7.046970,1.952218,-9.863781,4.471312,2.473653,1.969069,-0.792585,1.086397,8.356767,-2.907486,-5.928856,-9.249100,-1.369448],[-2.497516,8.928684,9.352509,6.915689,-7.907949,-4.003482,-1.177115,4.800028,8.027819,2.038766,-9.656381,4.413126,8.600998],[-8.205124,-5.322189,9.487097,8.832041,6.103901,6.948406,6.910801,-1.252415,4.402984,-0.358733,-1.498988,-3.500632,-0.440730]],[[5.549348,6.230903,5.267984,-3.079506,-0.052856,9.163650,-1.653545,-6.317578,5.633756,7.862861,2.567778,3.174592,-8.884917],[-9.293706,3.342150,6.290177,-9.957480,8.362567,6.891816,6.571399,1.891294,6.166934,-0.512463,-7.461382,-1.164210,9.761002],[-2.900365,8.253563,1.894540,-9.967217,-1.417280,8.683809,-3.871296,6.475314,-0.944387,-8.449986,1.113768,-7.830164,0.027735],[0.774218,-6.648374,-9.855301,2.731342,7.582045,7.107112,0.261928,-4.253718,-9.974766,8.871600,-2.391747,-0.685079,-8.549508],[-6.436108,7.778528,6.038512,8.880625,-3.330581,-6.039776,0.653995,-0.443223,0.500044,2.342124,-6.320835,0.384657,5.629363],[6.032622,-4.727853,7.650370,-6.894417,-9.237254,0.492924,-0.021449,3.638732,-6.184259,-4.049724,2.943864,-8.024314,8.958029],[-0.484584,2.600371,-4.237885,-9.644572,-2.078899,-2.568957,-9.700396,-7.391627,-1.811204,6.932485,6.651054,5.689228,-4.764257]],[[-2.014069,2.434581,5.946768,-4.960618,1.952748,-1.847268,8.816789,2.241279,5.008005,-5.383794,4.382212,-7.455319,9.923714],[-2.988288,-3.267473,6.448819,-7.341162,-1.171944,9.991974,-5.221268,-9.006278,-9.729467,7.295338,6.499018,2.115478,-0.212443],[-7.264981,-4.431748,-2.745294,-2.372502,0.660453,4.023112,-6.998924,-3.928092,-2.490571,-8.972786,3.372568,-2.875460,-8.824914],[5.290866,-2.078868,5.959978,7.246110,-0.174952,-6.153489,-9.603227,-2.171188,0.035839,8.652626,-4.209022,-4.799637,-9.965949],[6.521109,-9.661660,-2.484524,-6.819226,9.673234,-0.770350,3.543491,9.444524,5.554298,8.260126,4.817327,2.254054,-0.510238],[5.585898,-7.713149,-6.471440,-9.163759,-5.915869,7.500669,2.029013,-4.624990,3.106319,-4.742525,9.989294,-8.724287,-2.090431],[-2.333798,-2.681962,4.990510,1.657383,-1.276800,-6.816625,2.973196,3.431008,0.421317,7.329210,-5.020709,1.265218,9.672594]]], dtype = "float64")#candidate|5194|(9, 7, 13)|const|float64
var_5195 = relay.var("var_5195", dtype = "float64", shape = (9, 7, 13))#candidate|5195|(9, 7, 13)|var|float64
bop_5196 = relay.floor_mod(const_5194.astype('float64'), relay.reshape(var_5195.astype('float64'), relay.shape_of(const_5194))) # shape=(9, 7, 13)
func_34_call = mod.get_global_var('func_34')
func_37_call = mutated_mod.get_global_var('func_37')
const_5219 = relay.const([-8,3,-10,-8,-6,-9,8,-5,-9,-8,-2,-8,1,-7,-8], dtype = "int16")#candidate|5219|(15,)|const|int16
call_5218 = relay.TupleGetItem(func_34_call(relay.reshape(const_5219.astype('int16'), [15, 1])), 0)
call_5220 = relay.TupleGetItem(func_37_call(relay.reshape(const_5219.astype('int16'), [15, 1])), 0)
output = relay.Tuple([bop_5196,call_5218,const_5219,])
output2 = relay.Tuple([bop_5196,call_5220,const_5219,])
func_5231 = relay.Function([var_5195,], output)
mod['func_5231'] = func_5231
mod = relay.transform.InferType()(mod)
var_5232 = relay.var("var_5232", dtype = "float64", shape = (9, 7, 13))#candidate|5232|(9, 7, 13)|var|float64
output = func_5231(var_5232)
func_5233 = relay.Function([var_5232], output)
mutated_mod['func_5233'] = func_5233
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5310 = relay.var("var_5310", dtype = "int32", shape = (2, 1, 16))#candidate|5310|(2, 1, 16)|var|int32
var_5311 = relay.var("var_5311", dtype = "int32", shape = (2, 1, 16))#candidate|5311|(2, 1, 16)|var|int32
bop_5312 = relay.multiply(var_5310.astype('int32'), relay.reshape(var_5311.astype('int32'), relay.shape_of(var_5310))) # shape=(2, 1, 16)
func_4181_call = mod.get_global_var('func_4181')
func_4185_call = mutated_mod.get_global_var('func_4185')
const_5319 = relay.const(4.263305, dtype = "float64")#candidate|5319|()|const|float64
const_5320 = relay.const([[-5.093107],[4.941211],[6.438604],[1.509796],[-0.972453],[8.446436],[1.995560],[-8.835757],[-0.167661],[-6.866406],[-0.375234],[3.385724],[-9.017846],[-5.956436],[7.614824],[-7.932229],[-2.286769],[5.024520],[-0.160849],[-2.733155],[8.931554],[-5.515680],[1.471466],[1.679399],[3.112913],[4.670943],[7.197078],[2.062115],[2.589287],[-8.456145],[4.339616],[-6.491917],[3.468270],[0.331490],[-8.792966],[-5.054850],[0.328336],[5.065307],[5.091297],[-2.038924],[-3.947417],[2.797632],[-0.233827],[-3.752866],[-4.089146],[-3.537866],[9.562217],[1.210790],[4.672961],[-6.827093],[-0.304149],[6.849313],[-2.260747],[-3.538343],[1.482657],[-7.777598],[6.332007],[1.649388],[4.220961],[4.664401],[-7.567969],[3.372959],[8.389017],[-5.478218],[2.698334],[-0.117971],[-6.047296],[9.538794],[-7.888638],[-6.321175],[-4.707878],[-9.350920],[-7.235912],[-3.635889],[5.160217],[-8.524132],[5.484338],[4.479717],[-1.151029],[3.328578],[3.035908],[-8.312446],[6.743250],[-0.229335],[7.997227],[7.311078],[0.635693],[9.444245],[7.193132],[1.253147],[-6.782788],[4.118061],[0.248942],[-1.221821],[-7.668743],[8.675236],[4.382265],[4.734396],[8.326622],[4.699961],[2.076034],[3.172286],[-8.474652],[-7.298435],[-7.426352],[-7.061627],[7.802138],[-6.979302],[-8.845167],[0.155683],[0.080752],[-3.179302],[-8.975032],[2.221096],[5.613617],[-7.267239],[-9.512927],[-5.163148],[8.970561],[-8.727005],[-0.084041],[-7.434956],[-3.060661],[7.915144],[3.149546],[-5.425278],[3.112309],[8.843040],[-0.091632],[-1.369974],[9.498558],[-8.489973],[-4.270820],[-2.251412],[-8.267895],[6.362827],[3.731529],[-6.309780],[-7.322017],[0.540216],[-1.883440],[-9.141179],[-1.085089],[7.296316],[6.594066],[1.453037],[7.921669],[-6.296243],[-7.862578],[3.103135],[6.103839],[0.489983],[-4.771122],[0.383867],[4.552273],[-2.470536],[-8.406169],[-8.516172],[-2.388062],[9.902557],[8.489848],[0.775011],[7.168925],[-9.945820],[-7.563346],[-1.132637],[-9.589242],[5.969432],[3.763185],[6.178009],[9.534836],[6.642813],[2.059906],[-7.904374],[5.882561],[5.654755],[-9.215006],[0.495339],[-5.686024],[6.339667],[4.559510],[-8.235814],[-8.712409],[-1.873943],[-2.426369],[-2.279220],[2.424893],[9.540696],[5.977694],[1.080848],[-4.982445],[4.968223],[9.688766],[-0.043221],[-9.549408],[-7.364064],[6.250090],[3.644697],[-0.131080],[1.300543],[-6.803924],[-0.675907],[4.552464],[-0.814237],[-1.497166],[-4.588993],[-6.848471],[4.611604],[-5.173082],[1.825764],[-4.117288],[9.904352],[-1.171420],[1.885539],[-1.811768],[-1.249400],[-1.021817],[1.701080],[-7.951320],[7.017136],[4.554096],[7.618062],[6.721837],[6.543984],[-7.429296],[3.920078],[-6.738506],[-4.062813],[0.381060],[-5.061884],[7.261841],[-1.935021],[8.186675],[3.801126],[7.875612],[-7.158467],[-1.766161],[-7.037140],[5.385224],[-9.679754],[-4.544336],[-8.800852],[-3.733860],[-4.127452],[-6.937705],[6.920143],[6.920155],[1.861710],[0.975083],[-8.330951],[0.333562],[8.312003],[6.034644],[-7.763212],[4.222575],[-5.734767],[-2.254728],[6.360445],[-2.948818],[-4.864356],[-4.037866],[-9.871552],[-0.352884],[-3.432540],[-3.236297],[-0.221541],[-3.167270],[-9.717944],[-0.490316],[-2.666377],[4.481888],[5.769444],[3.359506],[-3.531884],[-5.759915],[-6.417805],[-7.963829],[-7.251815],[-6.678686],[6.138487],[-5.194939],[5.039969],[6.275861],[-7.187690],[-2.875268],[-4.759312],[4.207627],[9.233843],[-9.193246],[-0.397428],[-2.215850],[0.716723],[1.030771],[3.149872],[-2.779412],[5.200886],[7.135802],[6.087187],[-1.751571],[-6.623362],[-1.326261],[-0.100648],[-3.587339],[-2.958615],[9.498023],[-5.830539],[2.778254],[-6.427326],[1.033902],[9.157913],[-2.069044],[-8.373177],[3.044457],[7.376274],[2.313307],[-1.834386],[-2.344626],[-9.598533],[-3.314989],[8.013611],[9.781359],[0.083864],[8.690282],[-5.715057],[-6.099003],[-2.276011],[-6.195740],[-2.470080],[8.939764],[0.177296],[7.074281],[-0.712586],[-1.685300],[-6.165531],[-2.177785],[-1.862804],[0.033786],[-1.747497],[7.082414],[-9.315196],[-8.279254],[5.970301],[7.696064],[-0.654172],[9.009150],[-5.569154],[8.475506],[-4.201985],[4.635980],[-3.224580],[-0.313504],[2.058978],[2.084027],[-8.087625],[-2.353201],[-6.703297],[9.266435],[5.342681],[6.575659],[6.134153],[8.631068],[4.163075],[4.292026],[-7.834803],[-9.932764],[-0.996925],[1.669127],[7.903012],[5.937645],[-3.505652],[-6.794404],[7.642204],[-8.490238],[-1.428887],[-8.288060],[-5.507107],[2.857792],[5.255469],[5.528417],[7.502805],[-5.509876],[-7.247624],[-2.234917],[-8.293933],[0.963106],[1.115635],[7.420452],[1.232546],[-4.288607],[6.144552],[-8.823381],[-4.265941],[9.960526],[-7.315591],[-4.051550],[6.028367],[0.602520],[-0.862439],[1.203253],[6.119493],[6.987978],[-1.602906],[7.493843],[-8.412552],[4.814499],[8.633952],[8.652288],[-2.590296],[6.773829],[8.859529],[-1.107762],[-3.678777],[-6.140565],[2.590833],[-7.722316],[-7.992441],[-3.122226],[-6.693173],[9.920129],[4.067957],[3.314021],[-1.377816],[-0.303768],[6.155958],[3.339909],[7.549210],[5.375530],[3.303242],[2.719802],[8.483117],[4.925840],[4.579708],[-0.616577],[-4.004401],[1.414329],[9.361599],[-3.971480],[8.859250],[-7.572556],[-6.323936],[-1.422101],[9.306278],[4.356252],[4.930960],[-3.221822],[-8.922095],[5.619558],[6.025995],[-8.138377],[8.031568],[3.471162],[-4.642078],[-6.662760],[-9.838393],[-9.319056],[-2.299582],[6.244981],[4.833832],[-6.245755],[2.851533],[1.718189],[-4.119079],[9.362488],[9.131156],[8.917173],[2.816742],[2.012892],[-4.648513],[-4.674572],[-9.743931],[1.472285],[7.286233],[-9.685025],[-2.224140],[8.034603],[3.886147],[5.041110],[8.467306],[4.114633],[-8.310391],[4.168013],[2.914003],[9.209022],[-5.008150],[8.633431],[4.459985],[4.912352],[2.541536],[4.757181],[-6.073677],[8.543837],[2.368387],[-6.816500],[1.202917],[0.532751],[-7.065606],[-7.804011],[3.736927],[-1.582722],[3.507470],[-0.211460],[-5.790778],[4.404121],[-5.814030],[6.334469],[7.358482],[-9.535687],[-8.902615],[-0.682701],[6.188567],[9.488527],[-6.510565],[5.408438],[-3.842633],[-5.599558],[2.943205],[-3.432885],[-1.580039],[2.363506],[-4.019320],[-6.650668],[2.462663],[-3.343399],[8.012397],[-7.644093],[1.878034],[-9.864886],[0.905289],[4.764931],[5.860388],[5.283042],[9.948232],[4.093949],[1.029618],[-9.583118],[4.335574],[8.279704],[5.359983],[-8.387260],[-3.141772],[7.954896],[2.601216],[-7.609418],[-6.896510],[-0.119703],[8.526311],[-2.804498],[9.992454],[-4.331198],[8.633942],[-4.499257],[8.191012],[1.253512],[9.873521],[9.269033],[-4.036927],[7.509086],[6.029183],[-7.862631],[-7.592331],[4.018657],[-3.143006],[-3.140949],[7.232709],[-2.064392],[7.943402],[-6.740106],[5.081208],[3.448594],[4.409866],[-0.495634],[-3.078274],[4.155342],[8.214025],[4.221428],[-4.723103],[5.982551],[-8.691639],[-9.398475],[2.549165],[-3.449169],[2.911053],[5.092969],[1.517042],[-9.914826],[-3.746525],[-6.412175],[-0.622471],[-9.632075],[-4.202501],[0.074800],[-9.641948],[6.456232],[-8.411533],[6.679331],[5.027660],[-2.809790],[-0.810963],[8.736816],[4.595382],[-3.101882],[-5.055392],[-6.981712],[4.045824],[6.740583],[-7.084044],[-5.514416],[7.095855],[3.748546],[-2.903373],[7.359474],[2.519280],[-1.942476],[-2.757578],[5.273903],[2.356680],[5.354198],[-4.181720],[0.469574],[-1.102950],[4.193897],[2.121490],[2.310739],[-1.980569],[5.455809],[8.069909],[-0.126758],[-8.526950],[-9.643212],[-4.254436],[-0.651793],[-3.004002],[4.114308],[6.564935],[-5.207459],[5.611220],[-9.901870],[0.424208],[-2.676034],[4.694511],[-6.635127],[-6.206025],[1.006558],[-5.134080],[9.264427],[6.167477],[-0.702868],[7.986390],[-7.183540],[-6.308201],[-8.865066],[7.303912],[8.952747],[1.592999],[-1.382846],[1.918534],[9.140350],[0.240018],[-4.877301],[1.622331],[-1.133014],[-7.891034],[-3.835197],[-8.268277],[-8.961406],[3.095571],[4.545822],[-2.520753],[8.094617],[-1.707347],[-1.310087],[6.456510],[6.066482],[-8.270573],[-0.011742],[-2.322802],[-5.982966],[2.484234],[-2.733107],[7.234753],[2.349550],[-8.180567],[8.766842],[7.193450],[-6.678629],[-7.057978],[9.448807],[-3.025435],[-2.001534],[-2.688608],[-7.752713],[1.128924],[8.642937],[0.416363],[2.421499],[6.442472],[8.403735],[4.441159],[-2.924065],[-8.351149],[-7.959246],[4.791188],[-8.479691],[-3.946040],[-7.973439],[5.844409],[6.521837],[2.488200],[4.632718],[2.005688],[8.932342],[2.939403],[-6.268336],[-5.267036],[0.894381],[3.991084],[5.364478],[5.939504],[-6.715075],[9.683727],[9.164252],[-9.514183],[1.558628],[0.373916],[-0.233457],[4.386105],[7.935670],[5.304988],[2.898960],[-2.253793],[-5.886592],[-0.928326],[-2.948922],[5.811148],[-9.102345],[3.549231],[5.688018],[-0.496874],[3.861718],[6.188757],[-9.372372],[-3.442777],[-6.476659],[9.522594],[3.570493],[-6.720522],[0.656597],[9.492417],[6.790716],[2.123451],[8.182389],[8.827942],[-7.064582],[-4.556160],[2.924733],[9.778477],[-3.235124],[-1.426036],[6.859402],[6.401004],[3.412056],[-3.559702],[-9.278451],[9.284636],[-4.975545],[3.510470],[4.780966],[-4.446065],[3.283044],[-6.274404],[8.465476],[-0.541010],[9.341056],[-4.912189],[6.333191],[7.840500],[5.822673],[3.620920],[6.956772],[8.846713],[2.813776],[-4.700814],[4.782659],[-5.368808],[9.358562],[-4.942386],[9.357835],[-5.856538],[0.888278],[6.135567],[-0.353183],[8.791268],[2.536989],[-7.349474],[8.464936],[-2.554680],[-2.054469],[-7.410122],[-0.634332],[-2.889021],[2.056720],[-8.430134],[-4.337414],[6.187214],[5.704510],[-0.551836],[1.260039],[5.434398],[-0.716957],[8.187300],[-6.771727],[3.694925],[-2.330844],[-3.692750],[-9.286305],[-7.893317],[7.192477],[-2.024869],[-8.484335],[0.536357],[3.949651],[8.369463],[-3.002881],[0.180668],[-0.278420],[-9.025184],[-4.791421],[-8.569005],[8.426942],[1.343004],[7.080350],[6.918664],[-9.465134],[-9.301095],[4.173272],[-4.762003],[6.597705],[2.879041],[1.321038],[8.103737],[-6.887867],[-1.157812],[7.081620],[2.200197],[1.111025],[-5.715625],[8.200314],[-1.193640],[-4.318060],[-6.335519],[-5.712284],[-1.616886],[-8.962606],[8.047484],[-8.107058],[-9.831269],[3.143312],[4.903355],[0.335255],[3.428269],[-6.011947],[2.381506],[-8.154076],[9.808798],[9.467715],[-8.950949],[5.452442],[6.412321],[0.519441],[1.314798],[1.110890],[-9.162968],[-4.833028],[5.263258],[-3.043949],[-3.561755],[9.311083],[-7.241158],[8.266475],[-5.655996],[0.076247],[8.286122],[5.136702],[3.949615],[5.426412],[-5.600699],[-5.569403],[5.541434],[-4.515251],[-7.979062],[-3.881119],[4.396149],[-2.989204],[3.246553],[-9.362819],[-7.481706],[-3.576161],[-2.036780],[1.976686],[-5.862817],[-4.087417],[5.804070],[4.599200],[0.040484],[-0.083332],[9.089929],[-5.127293],[-3.840917],[-8.737871],[4.708009],[9.839924],[3.294111],[9.380569],[7.111470],[4.572186],[3.405404],[-0.125645],[-4.661797],[-6.661008],[6.761226],[1.792916],[9.204091],[-2.930631],[-5.748210],[7.887872],[0.224786],[-4.617302],[-8.819082],[-2.316301],[-9.845762],[-0.459411],[7.140055],[-4.061730],[-9.966977],[4.467345],[4.463472],[-5.575040],[-0.571100],[-6.916083],[-5.520658],[-9.853396],[-6.322524],[-1.113873],[-7.230955],[-3.816725],[-0.977297],[1.296927],[5.959623],[2.772055],[-1.242975],[-5.802948],[8.302732],[-2.639227],[7.194087],[-7.979240],[-8.916453],[1.031265],[2.706004],[0.738348],[-9.929927],[-2.084162],[-0.991076],[-6.776100],[-4.615621],[-5.429624],[-0.454592],[-8.498305],[5.485654],[8.334560],[-2.256047],[-0.751099],[3.591074],[2.094426],[7.623186],[-4.107120],[7.198821],[-9.685013],[-4.571897],[2.595737],[-1.011586],[2.621787],[-9.355190],[-7.538782],[-9.806096],[-4.088333],[-3.446071],[6.730154],[-9.280767],[-9.128410],[-8.901308],[9.785434],[-1.571478],[8.391313],[-7.213610],[3.964009],[-7.984526],[8.660291],[-0.796096],[4.025868],[-6.811308],[0.065266],[-0.540177],[-2.520665],[-6.077439],[2.948490],[7.898990],[-8.590317],[-2.898112],[7.490128],[-3.437483],[-4.081448],[0.248777],[-3.521738],[9.068176],[5.943038],[1.489937],[-3.350763],[5.137580],[1.027250],[-2.838725],[-5.968685],[0.553193],[1.194756],[2.138452],[7.672228],[9.694016],[-5.095490],[5.977233],[-6.078447],[-8.104930],[-3.791571],[3.246725],[-6.398878],[6.636512],[-9.197382],[-0.639746],[-2.437169],[9.470519],[2.870909],[-3.676214],[-5.578851],[-8.779903],[-8.946030],[6.071402],[8.676199],[-9.633555],[-5.218177],[-4.302154],[5.750999],[-1.979757],[3.836154],[-1.927451],[-5.419280],[2.728803],[-0.091694],[-8.579182],[3.536584],[-1.704482],[0.116771],[8.244980],[0.700187],[-5.745475],[8.044795],[-1.808108],[4.888949],[-2.303964],[4.158022],[-3.286588],[-5.613396],[-6.783108],[7.083015],[7.056397],[7.306299],[-4.308372],[-8.506276],[3.524016],[-6.926649],[3.232454],[6.782765],[-6.654788],[-0.329572],[4.990919],[4.008776],[6.535880],[-4.746220],[5.988148],[8.405293],[-9.527212],[-8.486437],[0.006399],[-0.145512],[-0.674905],[-3.150599],[-3.877725],[-2.210505],[-2.145590],[8.448909],[-6.213311],[1.259574],[-4.664899],[3.967370],[9.795415],[0.911503],[-9.517555],[0.630939],[-9.123806],[-4.230951],[-2.836048],[-0.239177],[-8.650527],[3.707958],[6.943864],[1.122465],[5.893848],[8.998324],[-9.250678],[8.512668],[0.741055],[1.719128],[-4.983457],[6.411267],[6.344032],[-2.786310],[1.161414],[-0.975093],[0.079076],[-7.501799],[6.572488],[-2.340911],[8.466224],[-6.695306],[0.771868],[6.621594],[-4.913612],[-1.480960],[9.827662],[5.085891],[5.034651],[-7.424544],[-5.343464],[0.218563],[-1.888610],[-4.850111],[1.456727],[9.187950],[2.072642],[-9.793023],[5.732098],[6.017774],[-8.877874],[1.781328],[-2.360716],[-3.673678],[-8.155845],[-9.254003],[-8.696201],[-2.519169],[9.476567],[-9.254961],[8.498828],[2.921181],[4.498150],[0.182941],[-5.591667],[4.646110],[-0.833651],[-7.098187],[7.845813],[9.463981],[-5.244188],[5.607930],[9.164927],[0.557715],[-3.086408],[8.651882],[5.990386],[-9.096695],[-5.182446],[-1.934176],[2.665067],[2.895829],[-0.714591],[-3.836753],[0.091995],[0.340467],[4.185666],[-7.146576],[-0.424271],[9.894438],[4.815146],[-3.577376],[-8.349009],[2.090354],[4.614284],[1.116911],[1.561104],[-4.952015],[-1.901809],[-8.199760],[-0.800602],[6.411594],[-0.737975],[-4.855064],[-5.463738],[0.165791],[-5.173536],[-9.142647],[6.675701],[8.943955],[0.765521],[8.643303],[-5.065210],[-9.769623],[-6.466987],[-2.990396],[-0.243876],[-0.323654],[7.335362],[4.954346],[-9.913686],[2.213039],[0.393857],[9.451781],[6.736613],[9.296946],[7.016378],[-6.063751],[-4.172771],[1.473036],[0.115841],[-7.122905],[6.376576],[-8.782297],[3.603848],[-0.561541],[-7.492280],[8.934284],[-8.030370],[-2.261218],[6.180843],[-0.126679],[-9.579586],[-6.863966],[-8.463504],[3.475963],[9.484235],[5.007797],[-1.360864],[0.205607],[-4.391308],[-2.859222],[3.132884],[-6.578011],[-8.795525],[-1.282472],[-8.548397],[2.611306],[9.137832],[9.808567],[5.797525],[3.165294],[-3.819440],[8.363779],[-7.017250],[1.358586],[8.132029],[3.730971],[3.480030],[-4.556973],[4.745278],[6.599084],[4.018664],[-1.816492],[4.277006],[-3.839139],[7.163657],[1.757605],[0.951980],[-1.334031],[-2.281431]], dtype = "float64")#candidate|5320|(1280, 1)|const|float64
call_5318 = func_4181_call(relay.reshape(const_5319.astype('float64'), []), relay.reshape(const_5320.astype('float64'), [16, 5, 16]), )
call_5321 = func_4181_call(relay.reshape(const_5319.astype('float64'), []), relay.reshape(const_5320.astype('float64'), [16, 5, 16]), )
output = relay.Tuple([bop_5312,call_5318,const_5319,const_5320,])
output2 = relay.Tuple([bop_5312,call_5321,const_5319,const_5320,])
func_5322 = relay.Function([var_5310,var_5311,], output)
mod['func_5322'] = func_5322
mod = relay.transform.InferType()(mod)
mutated_mod['func_5322'] = func_5322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5322_call = mutated_mod.get_global_var('func_5322')
var_5324 = relay.var("var_5324", dtype = "int32", shape = (2, 1, 16))#candidate|5324|(2, 1, 16)|var|int32
var_5325 = relay.var("var_5325", dtype = "int32", shape = (2, 1, 16))#candidate|5325|(2, 1, 16)|var|int32
call_5323 = func_5322_call(var_5324,var_5325,)
output = call_5323
func_5326 = relay.Function([var_5324,var_5325,], output)
mutated_mod['func_5326'] = func_5326
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5711 = relay.const([[[6.906773,-7.397021,3.900785,-1.477302,-7.260623,9.811281,-4.769279,0.317441,-3.812075,-7.068589,-6.864031],[-8.826591,-4.403283,-5.497016,6.741769,0.326173,3.112814,-7.889951,-1.907580,6.261253,-5.781853,3.087062],[0.651676,5.461374,4.726277,-1.936674,-0.028186,-6.964631,-9.234603,1.177785,-2.962065,6.180956,-6.682203],[-5.537515,-6.053373,-0.948812,-6.306856,0.555280,-4.508782,5.812868,-7.529973,8.560157,-6.123235,9.287491],[-5.610993,2.604637,1.541024,8.531818,-0.174938,1.289937,1.208545,2.946333,3.205379,-3.871556,4.602798],[7.416935,3.083060,-1.545108,-7.050156,5.986164,-8.866075,3.404832,0.192864,-3.523097,-5.696420,-4.205465],[1.848086,2.150093,-2.588305,-1.520494,-6.581726,-1.821828,-7.416558,4.371009,-8.159892,5.455133,2.722519],[2.323124,0.227772,-9.181752,0.554090,-1.576878,-6.006036,4.880473,1.178617,-5.595796,7.216243,3.123024],[-6.138883,-0.865694,9.830965,8.577567,-9.215211,3.325725,-6.322517,9.482129,-2.393221,-2.488391,5.032393]],[[-1.363766,2.954224,-2.258972,4.693299,-4.237381,3.107102,-8.544586,9.825504,6.542337,-3.643056,9.233117],[8.126577,-9.211606,-0.155744,-5.475442,-3.303420,-1.880316,-3.674527,-8.516455,5.639509,8.844867,4.221964],[0.027253,6.762419,-9.350923,-7.107936,2.298871,-5.799164,6.433427,-3.724875,1.458146,-9.340271,2.645653],[-7.126636,-6.164065,-6.187743,-6.274447,-5.533534,-4.963984,0.499736,4.785969,4.451683,7.573874,4.542413],[-2.439074,-1.738370,-4.089253,-3.447403,1.534306,-4.601983,-0.508427,0.640176,-1.429669,-5.237388,-5.222673],[-5.874643,9.766126,-9.545822,7.427707,-5.015589,1.569328,8.368175,3.126926,1.372247,9.407933,0.095852],[3.443324,-7.809501,-4.339885,-5.680047,-3.691851,-0.697878,-4.732217,-2.010282,-8.815313,-3.466713,-2.086548],[-8.299654,8.957596,-7.603381,9.844078,-3.808941,5.219723,-2.092740,9.140704,-3.938439,2.046221,-6.943476],[7.042616,-7.114525,7.262953,5.849716,-7.013122,3.947598,-0.862184,-9.962024,7.989562,-9.968154,-4.350066]],[[-5.928540,7.343974,2.153825,-4.590200,9.118977,3.661962,6.263072,-0.393704,-6.990218,-9.861206,-5.088115],[0.899252,-4.955585,5.609346,7.989012,-5.128668,3.899468,-7.649832,-1.467364,-2.031170,-4.998157,4.273247],[-5.369596,2.501542,4.064983,8.062480,-6.713310,-6.024588,0.018526,9.217614,3.649902,7.683542,3.111579],[-8.475616,-8.600760,7.984845,-0.436660,-3.621387,-3.647561,9.233728,-4.590720,6.722835,9.804354,7.307008],[7.717822,-8.782598,-0.283061,-1.665236,5.346698,-6.214933,5.843378,6.847037,-0.620960,0.293854,7.031215],[-3.634174,0.981309,-0.062520,-8.663931,0.141781,-2.523697,-2.759728,1.157982,-3.096834,6.915991,-0.016161],[6.729028,-2.897395,-2.483214,-0.624117,-9.261936,5.219996,4.024671,5.299286,8.925144,1.287582,-1.679324],[1.515319,-7.355248,-6.015953,-2.093612,8.378655,-3.274855,5.212811,0.070342,-1.026471,8.968644,9.295536],[9.555882,-3.326934,0.521442,-4.736168,4.439955,-1.498689,-5.717148,-4.827732,4.323639,-8.151129,3.713599]],[[-9.820561,0.627229,7.979228,-6.151078,5.824973,0.656052,7.308964,-9.719199,-2.852766,6.534771,7.936740],[3.377138,-5.080165,1.921424,0.461535,-3.533394,7.895641,-4.280937,-6.434681,9.164699,4.227212,8.710648],[-0.353024,-0.620319,-3.187607,4.859809,8.277455,7.384834,7.888096,-5.631892,3.940041,8.594773,8.215896],[5.157610,-4.777965,7.369927,5.532381,-7.807497,-0.563418,-2.660436,-1.783070,6.580963,6.651461,6.341234],[8.700230,2.857431,8.876844,-7.625777,-9.952821,-3.050778,-2.140282,-6.814129,0.085157,0.662972,-7.441213],[-7.034567,2.224939,-1.742656,-8.141304,-1.920641,-2.883580,-1.929883,-7.797229,-2.842730,7.939793,8.439663],[-2.699379,1.603400,6.124109,-2.765121,0.918198,-2.303214,-6.252893,8.036128,0.683071,-3.978537,8.862064],[0.820652,8.816693,-8.297023,-5.807696,6.948580,-2.708875,-0.322210,1.040694,6.402358,6.018855,-5.140739],[-1.917240,-9.809846,5.944087,9.968586,-2.181116,-3.473586,-5.973720,-7.324914,-1.516387,-6.016365,-7.362351]],[[-0.065433,8.774255,-1.354281,-2.587276,-0.191166,-4.058360,-6.031473,9.125565,-0.443972,-3.183664,-5.360388],[-9.424157,7.334886,-2.152970,7.386006,2.127103,-3.465087,4.167906,7.491252,5.309043,-1.909310,6.054653],[2.433766,8.953748,-7.722117,-3.333440,-9.026390,8.321255,-9.777936,5.879877,-2.880136,6.325761,8.288084],[-1.614910,-5.944418,-6.790040,8.710283,6.260116,5.319601,9.756260,-5.273394,-7.261065,-8.161849,1.484442],[2.174909,-3.600034,7.178628,-7.521786,-5.773228,2.698391,0.892959,9.103895,8.351286,6.124814,1.393532],[-4.310538,3.881582,0.595877,-5.926224,-2.824126,6.706651,-5.601977,-9.726216,-8.095385,5.904147,-8.082360],[2.041624,3.106473,-8.167871,0.314313,7.885108,-7.377346,-5.097852,-8.243781,-5.256803,-8.891501,7.849239],[-8.921351,-8.795929,-6.691915,-9.511335,-7.271140,8.347992,1.681499,-7.987635,9.820097,-3.974772,-4.867225],[3.199101,-6.274061,8.703791,-2.814494,0.627914,2.928673,6.019114,3.417036,-8.004068,3.103871,7.280606]],[[7.903518,-4.081538,-4.721717,-1.232335,7.936052,1.462521,9.930759,2.065073,-6.412863,-3.859976,-1.118953],[6.060288,-1.491668,4.733288,6.881745,-9.268123,-4.003117,-2.927108,9.089386,-2.802264,-1.277287,-3.786290],[-9.909628,1.949178,-6.906297,-5.733616,8.315614,-7.401422,5.204345,-6.310445,6.452645,-9.228081,8.555047],[-2.968285,3.554626,9.182098,-9.755915,-9.808253,1.661522,8.863547,7.753535,-1.906470,-6.068387,-2.746819],[-9.317279,-2.417659,6.614801,-6.214281,3.063604,-5.123965,4.135828,4.748242,6.561077,-9.183616,2.432989],[3.812294,-7.198577,-5.527180,-7.905057,-8.885640,9.556375,-2.941328,8.342859,4.755682,0.366489,-9.041934],[5.727489,7.897849,4.816742,-9.308836,3.729650,5.567506,7.406915,-0.425763,9.847109,6.368135,-3.300871],[6.807274,-9.701304,-5.031350,-7.785512,-1.607227,-6.343071,3.574191,7.072409,8.448862,2.912177,-3.134423],[-6.307089,-7.459039,-8.419718,-0.686888,-8.492343,-8.481631,-2.854962,-2.586598,4.337302,-8.718882,-4.287410]],[[2.734433,5.695715,6.357526,-0.407581,-1.986125,-6.639425,-0.457403,-4.314742,8.879466,-4.349045,9.837541],[9.915731,-5.770793,-3.116676,-9.540463,-2.303679,-0.356145,-5.201198,-0.628519,-9.337980,6.729705,7.614503],[5.141842,-6.235577,-7.388156,-2.912861,8.971411,-2.481288,5.963462,1.931077,6.118144,2.456084,6.714450],[0.576059,-6.495945,-4.772916,1.872724,9.782275,4.051587,3.241124,7.114063,9.466590,9.813952,-7.513097],[-8.006585,5.596097,6.552414,-2.713802,-9.906167,-5.007540,6.363412,9.542353,-2.594175,1.425560,-2.364301],[-0.273965,-0.514448,7.783041,4.778479,-2.912909,1.820052,8.782130,4.118071,2.525993,-2.100793,-1.875987],[5.093655,-3.819916,0.869601,9.689819,-6.472405,6.266366,-4.561082,3.872801,-7.253360,6.549753,4.832216],[-1.515005,-0.673204,-2.741759,0.948689,-0.864055,-8.844639,-6.257205,-2.147993,-5.231299,0.218385,-5.509427],[-5.076939,9.204061,5.220055,-8.763649,-9.026479,3.979986,-1.897559,3.002879,2.580917,-0.880667,-6.397945]],[[9.541643,3.424505,8.854777,7.576914,-8.524728,1.751460,-2.058254,-9.046338,0.783080,1.559202,-4.133322],[5.648867,6.477579,9.917258,-0.033669,-9.435666,1.143391,3.058187,0.241437,-3.720367,-4.522494,2.370024],[-7.763256,2.738679,-1.353314,9.682356,8.930077,-2.965558,6.865352,-9.699198,8.441881,3.666700,-8.313577],[-1.152127,7.201749,3.675437,-5.621595,-8.116051,9.701518,5.039098,-9.513632,-5.665094,9.971668,-2.815278],[-2.348468,-4.702899,5.357444,-0.701425,6.037253,0.698725,4.408362,-5.172808,-5.590978,4.493168,8.077442],[3.049525,5.449933,1.521191,9.807281,9.761110,-6.548316,1.617291,0.088224,-2.848068,-8.573088,2.356876],[-2.652148,-3.451813,-2.242798,-4.875981,-3.301631,6.789127,5.535932,-7.962610,-2.442709,3.301163,1.159228],[-9.408027,-3.352069,4.056076,1.011575,6.482085,4.697545,-7.512490,8.274682,9.435600,-3.305989,0.144728],[9.158582,-0.478552,6.624471,-4.120395,3.343304,8.520948,9.386907,-2.520300,6.241948,8.979992,1.721842]],[[-8.754215,-8.242526,-3.156188,-5.322860,5.643258,8.965973,6.530640,5.521475,-3.046445,-2.460618,-3.422693],[-9.766611,-8.227205,-6.288375,-7.321226,6.352386,-1.653545,-0.068209,8.857331,-5.419795,-0.982203,-3.563005],[-4.527473,-4.641767,-6.017970,-2.688114,-5.460213,-9.073484,-7.292291,-2.919194,-0.077216,4.181369,-4.242753],[-4.846862,-6.252994,-7.702622,-2.821628,-9.879415,-9.699903,9.345490,-1.223877,7.016600,2.620888,1.729263],[2.971774,-7.697097,-1.758759,-6.651025,-3.995201,-5.703454,-3.781766,0.357350,7.473400,8.931679,-9.558309],[4.596527,0.485861,-9.724979,-5.425891,-4.866374,4.286351,1.325452,4.955520,-5.102879,-1.319631,-5.706264],[7.945020,-7.795037,-9.027905,-9.133164,-6.590655,4.306032,8.502384,-4.492375,3.614924,7.829222,-8.276740],[-1.853937,-7.597555,7.809886,1.811393,4.396071,2.923750,-2.580956,-7.008709,6.494740,-5.644194,-1.275652],[-5.167282,8.506244,0.266926,-7.768400,1.678499,8.297500,-4.814144,3.227437,0.732530,-5.903712,-1.089113]],[[-9.547586,-8.630808,8.221072,-4.745941,-8.689708,0.262089,-3.837509,-0.105989,-3.051295,-2.314162,5.239414],[-5.944427,-8.212271,-0.170744,-2.694183,7.087553,9.704136,-3.836932,-4.923872,-2.577115,4.003318,-9.032127],[-4.883218,2.711864,0.155189,1.970573,-9.102278,9.860597,3.681725,7.191565,-0.474864,-1.804294,-0.579103],[-6.645991,8.515167,6.667830,-2.883912,-8.349842,-4.200211,7.471583,2.132741,9.351060,-2.299561,1.701591],[-0.860232,-9.986692,5.746532,-6.578356,1.392997,5.817924,8.662772,-7.393822,-4.181198,-6.634409,-8.201904],[-4.255399,-0.965811,5.383244,-4.427335,-2.609485,7.925210,8.602592,7.392988,9.892056,3.086833,9.085332],[6.974218,-3.841509,0.892309,6.130979,2.036640,7.459400,1.802967,-9.775311,3.365688,-1.565924,1.578596],[-8.887898,7.995352,-8.123408,-2.015770,3.677088,7.221664,8.665611,-8.121724,-5.341498,1.308993,-2.368701],[-4.356004,-1.484894,6.447080,-4.847991,2.067249,-4.794412,-8.986372,8.172268,-1.117351,0.122025,-8.992457]],[[-2.033077,8.695071,-8.602989,1.060623,9.474818,-9.749327,3.470990,-5.075230,-7.473475,-9.830737,-4.722202],[8.845662,5.833024,-7.413431,2.633667,-0.285758,3.937636,-8.337901,-5.786140,-5.126585,5.551587,9.200173],[3.992150,0.941086,2.137655,-1.217355,-3.186279,7.396346,1.195121,-7.535692,4.588610,7.683236,-4.953535],[-7.605406,4.580544,-0.611216,7.582718,7.944093,6.766525,8.771381,0.514190,-6.022905,5.398814,2.431655],[6.535381,-0.476185,-1.550420,-9.831933,2.584550,6.234952,3.228569,-0.804805,-3.671107,1.926710,-7.750853],[-9.130901,-9.575159,2.236335,1.008996,6.168312,9.023865,3.720450,1.196771,-2.767764,-3.880132,9.733020],[-4.180175,0.561224,7.962712,-9.242523,6.929359,7.736557,-0.265455,2.450869,-1.699286,-2.410187,-2.177335],[7.447754,9.423281,5.139038,-8.888398,-4.867583,-1.428759,6.439448,-7.927677,1.522195,-8.975205,-8.744380],[5.013435,-6.533913,-7.309488,2.449844,-2.196118,-9.260682,3.825961,-4.847071,-3.337326,-3.458318,-4.775877]],[[-7.171729,2.259247,-4.993215,5.732855,-3.872144,-3.633265,-2.635921,-7.720803,-5.016929,-2.090021,-7.696090],[-3.830246,7.303774,4.925198,3.957141,0.514535,0.315225,0.131897,0.208796,-0.312886,1.029359,-8.711813],[3.437239,-2.042963,-4.991829,-2.272893,-3.556046,1.172844,2.184431,1.121702,-4.899225,-6.044476,0.871479],[8.337758,-5.394100,2.879203,-3.024733,2.370433,-6.146472,3.011014,0.229987,8.123119,-1.888831,8.395472],[-9.122447,-4.968996,-4.872865,-9.892363,-5.214062,-3.531588,7.075497,1.871817,2.614674,4.563802,-4.871416],[-5.836132,-7.863558,9.326484,-6.997935,-4.306381,4.099626,4.269493,3.912067,3.323157,7.038576,6.454217],[1.768670,9.796616,5.154337,-0.582321,0.464174,8.134037,2.467135,0.409019,-4.915295,-9.206606,-4.351596],[6.137964,0.304606,-1.385273,-4.012541,7.240997,-1.452693,-6.375943,4.763457,3.673644,-4.300092,-9.503956],[8.402088,9.444376,3.939497,1.457843,-4.166139,2.318400,3.237493,-9.645925,0.031445,-1.968469,-4.005661]],[[-4.941448,0.329229,0.011999,-8.090875,3.494003,6.820815,5.112613,-2.555033,-8.720258,0.062248,-1.276279],[0.637762,-3.831399,-7.747341,-7.180073,-2.476219,-3.987719,-5.143768,4.355408,9.993414,-7.344046,3.749282],[6.158714,-5.446359,-4.272518,-8.096334,2.411904,-0.824764,-6.045955,-7.048209,2.688065,3.472159,-8.538087],[1.723409,7.282378,3.139519,3.932024,5.247722,-2.763242,4.257953,-6.578598,-0.260064,7.918291,7.267612],[7.515710,7.488812,-6.785853,1.267100,-9.928072,-2.205438,9.617953,-4.095398,3.815383,-1.854265,6.469315],[-8.758799,9.565144,5.214191,9.157237,-9.205201,-0.098570,-0.458681,3.434916,-6.549897,-2.758787,8.769555],[-4.704428,8.473513,8.665172,0.309719,8.618288,-2.392834,-5.966529,7.880535,6.452618,2.112687,5.330003],[-5.064935,3.101400,1.977845,-1.457509,8.507557,-5.906384,-5.586367,-3.404060,-2.556554,9.658112,-1.485643],[0.761066,-3.670198,-7.519669,-8.848445,9.683723,-7.172358,2.321860,-5.954630,-1.993556,-8.031062,-8.209928]],[[-3.053549,5.619896,-4.173725,-5.718445,-7.172132,8.698897,-4.446227,-3.229266,1.344248,4.703549,-2.376998],[4.079191,-2.609595,5.742536,-6.752042,3.496285,-1.945191,-3.981391,-8.162626,-9.598450,-3.663216,6.987051],[4.716109,0.645317,4.459784,-5.106578,-3.693141,-1.426129,0.456861,6.230715,-9.627433,-1.162979,4.723035],[2.197369,2.809632,1.347841,2.515361,-0.428234,-3.225015,-7.498788,7.234619,-8.396315,-4.085694,-2.354441],[-9.645872,-4.877504,8.576892,7.989999,8.933379,-0.916340,-3.987208,-6.815523,-4.999702,-4.932984,-6.500217],[-5.183867,9.064982,8.134013,1.546832,7.652230,-1.803182,-4.015318,2.971243,-4.665742,0.501779,7.041730],[-6.304173,7.446330,9.424278,-5.800335,-7.422579,3.269799,1.634093,-2.740103,-3.237163,-9.151578,8.184302],[-2.227698,-4.832715,2.257639,4.874938,-4.444292,-2.966037,-9.913474,0.605366,0.437126,5.472112,-3.394319],[-1.000836,-3.984853,-0.771216,0.644314,1.808245,-3.726590,-1.604743,8.801874,7.111225,-3.707971,-9.605460]],[[5.487963,6.767142,3.204589,0.416987,4.211874,-6.055032,-2.349500,-7.314027,-9.235013,-5.587228,3.777921],[-2.358600,-4.506721,-7.358050,5.935344,-9.860472,9.024885,-0.707719,-5.955235,-1.241001,3.983947,8.567218],[8.738775,3.291973,-6.983468,1.058925,-4.622833,-5.688718,8.645576,2.059215,1.942074,3.769224,1.561826],[-8.755303,6.730092,3.647974,0.712798,-6.988654,-2.006111,3.414089,8.663951,9.746637,-4.444546,6.164979],[-1.649899,3.008440,-9.435289,-3.669902,-8.765062,8.674408,2.109985,-1.979104,-3.583441,-1.110532,-6.485219],[8.081658,-9.995511,6.550397,-7.898181,-5.159470,-0.320700,6.315671,-9.737423,-8.193652,-4.388606,-9.730678],[7.762566,-1.020508,8.091689,-2.757576,-2.414277,-5.186890,-5.546722,-1.933873,-2.048394,-6.734895,-5.127267],[3.067692,0.881942,1.376182,3.280184,-1.743314,-7.977645,-3.900394,8.104416,7.428397,-7.088998,-7.144771],[9.310982,-1.105342,3.110148,-5.516535,-3.451623,-8.702792,-9.202333,9.149287,9.282415,-1.496614,-4.187363]],[[2.618110,4.941571,-2.237224,-9.697717,7.507359,7.760480,9.207278,-1.468084,-7.631664,6.738355,-2.752490],[-2.124477,-8.583450,9.940911,1.518470,2.910651,1.931161,5.905514,6.852811,-0.623806,8.226066,-7.201770],[-9.504294,3.839540,6.646158,3.697381,-9.848170,3.824878,0.294769,7.746365,-1.576790,-5.656578,8.120755],[9.432353,4.869652,9.300898,2.289013,-9.520062,-5.792660,-6.094835,-2.561270,-1.315070,4.258525,7.130877],[-0.987190,3.804632,-2.737665,5.933783,9.619877,-2.859603,-6.221388,-5.247420,9.349978,-5.145237,-1.846781],[7.621310,-7.089565,3.954169,8.261917,3.748329,4.826218,-6.707934,-8.701007,1.963912,4.977167,-7.223017],[-3.406580,5.929293,3.104834,5.906447,9.706938,2.374659,-9.490415,6.647697,3.741056,-5.314364,-2.239184],[-4.121551,-3.004252,-0.472150,3.103220,0.295064,2.252268,0.007821,-9.378343,-5.747797,3.108091,-9.417922],[-4.353397,4.783081,-5.085961,-3.738893,3.223347,5.849106,1.353060,1.432825,-8.142951,-9.406087,3.717849]]], dtype = "float32")#candidate|5711|(16, 9, 11)|const|float32
uop_5712 = relay.cosh(const_5711.astype('float32')) # shape=(16, 9, 11)
func_4518_call = mod.get_global_var('func_4518')
func_4523_call = mutated_mod.get_global_var('func_4523')
const_5717 = relay.const([-0.219685,-1.666066,-1.337132,5.074918,-5.116969,1.500341,-6.520392,4.064943,6.116046,-6.847161,2.261986,7.952543,5.151465,-8.823821,3.455281,1.991568,-2.755430,-0.686183,5.610832,8.223876,5.586787,-2.634436,9.581602,2.745305,-7.720261,-9.140261,-7.506054,-3.460849,6.163057,-6.900306,8.311429,-1.141174,-3.995105,1.424952,-8.472104,9.427311,8.195513,0.978478,1.016052,4.784779,-9.944961,-8.468931,3.455709,9.129223,7.891583,6.344674,7.767079,-1.245297,-8.359213,-2.923905,-8.477877,-5.313067,8.519241,-2.981713,-4.390850,-0.781953,9.786145,-6.271273,8.812456,-0.961366,1.432895,-9.136248,3.349722,-9.817760,-5.294752,8.192042,-7.009071,-6.746818,3.342589,9.521077,-5.065796,3.567554,-9.826096,-0.393589,4.418901,-0.064290,-2.449704,1.797904,-4.211364,-9.950969,-8.615279,1.898858,6.430586,-2.061171,1.006416,2.183188,0.818677,8.742544,-1.909395,-3.733309,-3.952384,-9.800830,2.271720,9.197633,-6.444014,-5.268234,8.798211,4.712976,4.709154,3.202487,4.090173,-0.041751,0.766502,-8.185977,0.457842,6.079710,-5.559844,-5.801179,-6.968462,4.272422,1.314091,7.100981,6.597275,-8.057164,5.084490,1.056732,-9.191504,9.739376,-5.137689,8.083195,-1.614193,6.324983,-3.837099,-3.662194,0.592481,1.428721,4.798592,4.548449,-8.357461,5.005697,-3.372906,-8.383539,-3.072418,-2.006689,-9.638225,-9.797553,2.946847,5.543983,-9.265906,-7.997360,1.387300,-8.026984,-1.336938,5.116731,3.090941,-7.419732,-3.187323,-0.735725,8.825444,9.065199,-7.827103,-9.512823,7.311468,-6.364840,-2.085787,-3.349121,-1.030384,-5.871103,-4.000730,1.331064,4.640074,8.403365,2.972844,-8.852660,4.865891,-5.535342,-7.302132,4.829123,-4.497709,2.418432,-7.118497,-9.158590,-0.088305,3.623176,-6.503090,8.045370,7.670944,2.804750,-4.440287,2.293624,1.646362,-0.922955,-9.761480,-2.829434,9.521606,2.525629,8.436056,-5.306612,7.010604,-5.348090,6.631657,6.354065,1.067673,0.240212,-6.240046,5.275112,-3.934084,9.242893,6.859592,5.748907,2.523666,-1.315050,-7.110318,0.915550,-9.206217,6.600352,4.763741,-8.308402,-6.535616,-3.062194,-8.795397,-9.156594,1.636233,-2.702398,1.560671,0.464620,-9.573938,0.259782,6.722076,-7.921630,4.513160,5.146201,-8.195917,8.640192,4.166878,-1.858515,6.932160,-4.327112,-3.239677,3.104309,-8.308020,0.743664,-4.097279,0.224925,6.944115,5.455189,8.116799,2.472789,1.164864,-9.896738], dtype = "float32")#candidate|5717|(240,)|const|float32
var_5718 = relay.var("var_5718", dtype = "float32", shape = (40, 10))#candidate|5718|(40, 10)|var|float32
const_5719 = relay.const(7.335771, dtype = "float64")#candidate|5719|()|const|float64
call_5716 = relay.TupleGetItem(func_4518_call(relay.reshape(const_5717.astype('float32'), [1, 15, 16]), relay.reshape(var_5718.astype('float32'), [400,]), relay.reshape(const_5719.astype('float64'), []), ), 6)
call_5720 = relay.TupleGetItem(func_4523_call(relay.reshape(const_5717.astype('float32'), [1, 15, 16]), relay.reshape(var_5718.astype('float32'), [400,]), relay.reshape(const_5719.astype('float64'), []), ), 6)
func_417_call = mod.get_global_var('func_417')
func_421_call = mutated_mod.get_global_var('func_421')
var_5740 = relay.var("var_5740", dtype = "float32", shape = (50,))#candidate|5740|(50,)|var|float32
call_5739 = relay.TupleGetItem(func_417_call(relay.reshape(var_5740.astype('float32'), [10, 5, 1]), relay.reshape(var_5718.astype('float32'), [10, 5, 8]), ), 0)
call_5741 = relay.TupleGetItem(func_421_call(relay.reshape(var_5740.astype('float32'), [10, 5, 1]), relay.reshape(var_5718.astype('float32'), [10, 5, 8]), ), 0)
uop_5744 = relay.log2(uop_5712.astype('float64')) # shape=(16, 9, 11)
output = relay.Tuple([call_5716,const_5717,var_5718,const_5719,call_5739,var_5740,uop_5744,])
output2 = relay.Tuple([call_5720,const_5717,var_5718,const_5719,call_5741,var_5740,uop_5744,])
func_5765 = relay.Function([var_5718,var_5740,], output)
mod['func_5765'] = func_5765
mod = relay.transform.InferType()(mod)
var_5766 = relay.var("var_5766", dtype = "float32", shape = (40, 10))#candidate|5766|(40, 10)|var|float32
var_5767 = relay.var("var_5767", dtype = "float32", shape = (50,))#candidate|5767|(50,)|var|float32
output = func_5765(var_5766,var_5767,)
func_5768 = relay.Function([var_5766,var_5767,], output)
mutated_mod['func_5768'] = func_5768
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6057 = relay.var("var_6057", dtype = "bool", shape = (15, 3, 7))#candidate|6057|(15, 3, 7)|var|bool
var_6058 = relay.var("var_6058", dtype = "bool", shape = (15, 3, 7))#candidate|6058|(15, 3, 7)|var|bool
bop_6059 = relay.logical_and(var_6057.astype('bool'), relay.reshape(var_6058.astype('bool'), relay.shape_of(var_6057))) # shape=(15, 3, 7)
func_1324_call = mod.get_global_var('func_1324')
func_1326_call = mutated_mod.get_global_var('func_1326')
var_6089 = relay.var("var_6089", dtype = "float32", shape = (780, 1))#candidate|6089|(780, 1)|var|float32
call_6088 = relay.TupleGetItem(func_1324_call(relay.reshape(var_6089.astype('float32'), [6, 10, 13])), 3)
call_6090 = relay.TupleGetItem(func_1326_call(relay.reshape(var_6089.astype('float32'), [6, 10, 13])), 3)
uop_6091 = relay.atan(var_6057.astype('float64')) # shape=(15, 3, 7)
func_1409_call = mod.get_global_var('func_1409')
func_1412_call = mutated_mod.get_global_var('func_1412')
var_6094 = relay.var("var_6094", dtype = "float64", shape = (18,))#candidate|6094|(18,)|var|float64
call_6093 = func_1409_call(relay.reshape(var_6094.astype('float64'), [6, 3, 1]))
call_6095 = func_1409_call(relay.reshape(var_6094.astype('float64'), [6, 3, 1]))
func_4181_call = mod.get_global_var('func_4181')
func_4185_call = mutated_mod.get_global_var('func_4185')
var_6108 = relay.var("var_6108", dtype = "float64", shape = ())#candidate|6108|()|var|float64
var_6109 = relay.var("var_6109", dtype = "float64", shape = (1280,))#candidate|6109|(1280,)|var|float64
call_6107 = func_4181_call(relay.reshape(var_6108.astype('float64'), []), relay.reshape(var_6109.astype('float64'), [16, 5, 16]), )
call_6110 = func_4181_call(relay.reshape(var_6108.astype('float64'), []), relay.reshape(var_6109.astype('float64'), [16, 5, 16]), )
func_4339_call = mod.get_global_var('func_4339')
func_4342_call = mutated_mod.get_global_var('func_4342')
var_6112 = relay.var("var_6112", dtype = "float64", shape = (364,))#candidate|6112|(364,)|var|float64
call_6111 = relay.TupleGetItem(func_4339_call(relay.reshape(var_6112.astype('float64'), [7, 13, 4]), relay.reshape(var_6112.astype('float64'), [7, 13, 4]), ), 1)
call_6113 = relay.TupleGetItem(func_4342_call(relay.reshape(var_6112.astype('float64'), [7, 13, 4]), relay.reshape(var_6112.astype('float64'), [7, 13, 4]), ), 1)
func_1815_call = mod.get_global_var('func_1815')
func_1817_call = mutated_mod.get_global_var('func_1817')
call_6115 = func_1815_call(relay.reshape(var_6108.astype('bool'), []))
call_6116 = func_1815_call(relay.reshape(var_6108.astype('bool'), []))
func_4181_call = mod.get_global_var('func_4181')
func_4185_call = mutated_mod.get_global_var('func_4185')
call_6118 = func_4181_call(relay.reshape(var_6108.astype('float64'), []), relay.reshape(call_6107.astype('float64'), [16, 5, 16]), )
call_6119 = func_4181_call(relay.reshape(var_6108.astype('float64'), []), relay.reshape(call_6107.astype('float64'), [16, 5, 16]), )
func_2733_call = mod.get_global_var('func_2733')
func_2739_call = mutated_mod.get_global_var('func_2739')
const_6125 = relay.const([7.375956,-9.817736,-3.859879,7.101333,-1.472258,-4.639189,-8.720454,8.971540,-6.711385,-3.132695,-1.421041,6.169181,-3.973015,3.386439,-0.861897,-2.321765,9.473549,3.324216,0.717388,-3.671442,1.950484,-2.462392,4.606159,-9.836857,6.329168,4.540351,-1.582514,2.792137,-7.843630,2.263252,8.498618,-7.470320,-6.066664,3.297944,-5.218691,-4.211817,-2.277713,-5.043895,-4.121127,1.775036,3.552686,3.762933,-3.769718,1.612311,8.654368,2.133503,-0.744528,2.764702,-6.849042,-7.131161,-8.496816,-6.104582,9.144397,-9.066568,-3.099463,2.782192,8.792740,8.655911,6.415342,-4.466617,1.393642,4.048732,4.353088,4.673549,1.798101,-7.782508,-4.869667,4.719020,0.586838,3.829028,9.176650,-2.695074,-9.387863,-3.404303,-4.115868,-3.600750,9.589522,3.017535,6.472582,-3.718416,-9.897396,-7.492992,2.887774,-2.402203,-9.565518,-7.999161,-3.082136,-2.614452,3.800265,-5.750765,5.795553,7.720827,-0.287985,1.652953,9.116262,4.985090,-9.332635,-1.882777,1.913861,9.989497,1.927488,0.566090,-4.359591,-0.717001,9.424231,3.566319,3.998810,1.497868,0.713890,0.067324,-1.195949,-3.653222,7.401426,-5.247908,3.619856,-9.912058,-7.626506,-5.391220,7.992085,-7.921783,0.235615,2.023326,-9.296309,-9.771892,3.500099,9.840582,-6.945413,-2.960269,-1.042463,-6.194263,-6.933758,-5.840995,8.152633,8.758568,7.551672,1.360574,1.744301,-4.541532,8.662637,1.389734,-7.545398,-9.299104,-6.811102,-2.677686,6.220140,-8.951978,1.941297,-5.106304,8.284250,5.581386,3.673318,1.225621,8.379716,4.760816,3.378274,9.283566,1.887810,-4.939042,8.141538,-9.353073,-9.564004,-8.489251,-3.400507,-9.407296,1.680217,-2.850848,-9.379256,3.704201,8.641875,-9.450979,-7.883727,8.783736,5.901493,8.011499,-8.325202,5.252895,8.385291,7.105374,9.532205,1.201981,8.090195,4.440314,-6.977359,-9.261471,4.166276,-2.459384,-3.880860,8.013853,8.158246,-2.195348,7.894732,-4.847783,-8.280912,-2.692940,1.983738,-3.272657,5.738473,-3.872754,-8.194075,-2.551470,7.363355,0.724506,-5.707088,7.107976,-6.396452,5.130967,-4.695446,-0.325244,0.033404,-1.457637,-8.163246,-0.980698,-8.021907,4.689314,0.097625,9.792891,-9.026706,-3.290742,7.963570,9.102206,-0.630650,5.317959,-9.555044,6.344985,-8.283233,2.006298,-6.348512,5.729355,-7.566886,7.107719,-2.294468,8.920992,-5.332376,1.666942,5.414727,0.754097,5.990167,-8.132675,-4.315598,-4.806995,7.280805,9.781337,2.781148,7.473101,-1.237275,5.201210,0.350178,8.794540,-6.798128,9.066803,2.913688,4.886367,-5.522305,4.898879,3.749145,1.021117,8.252598,-1.772264,6.557116,-1.808772,7.733278,-4.874138,-9.299362,-9.312474,-9.167642,2.405046,-7.958109,8.100854,-0.125399,1.411898,-6.924002,3.335489,1.142242,-2.665043,2.679303,-8.437320,-9.693982,6.300060,1.919685,0.241052,4.630255,6.334399,-9.329289,-9.781825,5.644838,-9.131214,3.351570,7.660557,-9.966723,5.177626,3.762839,-2.600694,5.660910,-1.636815,2.107320,-9.352645,-6.409711,-2.425104,-2.408937,-2.768387,-1.049507,0.400411,-0.100832,-6.880751,-4.983659,-1.190793,-0.498113,0.049879,-0.907344,-5.248184,-3.789441,-1.677219,-9.311349,6.978885,-7.976525,9.621579,-0.968984,-2.043046,9.154871,4.025264,-7.472948,5.017946,-8.615138,-4.836853,8.168247,-7.311911,-8.229604,-8.403457,3.882849,4.289379,2.917506,-9.240077,-0.863438,-6.782656,-6.579955,4.834664,1.023994,8.505223,-6.982231,-5.324103,-8.469349,4.951649,-2.203620,2.275586,0.870329,2.021763,4.005586,-6.293814,-7.657171,-7.690365,9.710127,0.976714,-0.567178,-9.310666,6.115925,-1.410349,-8.283786,-5.015652,-7.769446,-6.610446,-8.208242,-2.855472,-0.100024,3.712081,-2.424387,8.518986,-2.435312,-6.492026,6.165312,7.609996,-0.791891,-8.677191,3.638239,0.943871,-1.317326,3.327460,8.687759,7.818318,-8.707163,-2.023825,-0.721997,-7.164368,-7.874105,9.616347,-4.635246,-5.385632,7.378337,1.696916,1.134017,-7.506403,-9.129830,4.834105,0.836850,1.532205,0.986415,-6.604348,4.024002,-4.550878,-2.973764,9.062370,-5.106833,8.945489,-1.496051,-8.190756,6.177099,-9.271827,-6.611312,3.705801,-2.547125,-0.509756,-6.776011,5.566697,4.061193,1.291434,5.560186,-3.664007,3.035497,2.770730,-0.541604,0.558128,-5.731880,-5.540807,1.693012,5.620446,-9.920759,-8.505642,-7.886667,3.755855,4.994340,6.183393,1.203524,5.512291,4.082122,1.296918,-8.695589,5.948682,-3.039435,-5.080281,7.484679,7.446772,0.538714,-0.728839,9.857996,4.842599,5.050709,2.702195,4.713064,4.285103,-3.242843,-3.862740,7.465117,2.106054,6.465624,-0.251725,2.628259,1.356623,3.671193,6.522723,9.355755,3.668376,3.828854,9.195124,5.850137,-8.495036,3.862660,5.882552,-5.198736,-8.688856,-5.904516,1.011761,-7.334650,-5.432656,-0.809561,-7.494440,-0.523365,-2.558431,0.678550,-6.582785,-8.983283,-5.360292,-6.478830,6.476312,-3.390492,-5.108447,-6.417303,7.757832,-3.122239,-1.496553,4.365722,-6.158415,-0.694611,0.397655,0.330172,7.915604,-4.447855,7.312559,3.785209,-9.620170,6.672554,-4.612840,-3.677907,-4.544659,7.991290,3.084428,-6.168282,-8.105076,4.917706,-0.443988,-8.173154,-6.460643,8.292662,9.878123,-3.613768,-9.992304,-6.832520,9.685601,-6.712988,-1.793091,-6.925779,-7.193160,7.503782,-6.256135,1.748318,4.958687,-0.363145,-7.407715,-5.843775,-0.283443,1.787805,-3.548437,2.763090,-8.481902,6.444406,9.560707,9.759227,-3.169511,-9.482503,8.348398,0.725392,8.427183,-6.236408,5.694988,7.001583,-4.840486,9.598504,5.083861,-3.049487,-0.905019,-8.159887,-6.761788,-7.463910,-4.057557,7.199237,-9.181530,5.824995,-5.654567,6.957072,-9.092956,2.108159,-2.092710,4.156462,0.622498,5.266434,8.066921,2.963304,1.969798,2.229395,-9.500498,8.844142,5.748206,1.217112,1.529833,-8.018419,1.868230,-3.067050,-8.663738,3.999617,9.426789,4.017453,-1.124588,-1.112348,-8.706677,-0.980427,-4.666603,2.812758,-5.654523,8.147996,-2.281212,2.244991,1.687871,1.853628,4.498667,1.053241,4.355501,1.611961,5.530363,-1.037278,6.044210,2.740346,-0.851070,-0.888108,2.165300,-2.816298,7.977210,4.257679,1.031278,-1.786110,-0.034238,-8.466127,-8.275073,3.358662,3.609388,-8.865683,-7.928798,9.542399,-1.598550,1.752601,1.378617,5.987179,8.561401,-1.347546,4.775565,8.668785,-7.477827,-4.773909,-5.099888,0.694109,6.212552,-7.529227,5.942441,-1.748499,7.264302,9.211223,-0.002830,7.367825,6.560768,-8.618364,-4.798486,-2.091474,5.495757,-1.967132,2.724145,-4.462134,9.123287,-7.937843,-7.048911,-9.512186,7.631251,-5.086392,6.976789,6.075471,4.455819,2.344666,-4.084903,9.264744,-6.285099,1.132617,0.433870,-2.048126,-4.765171,1.866063,-8.269212,7.603390,8.336907,9.369442,1.024361,2.428235,-1.694358,9.229151,0.204935,7.690074,-5.879532,3.886410,-1.957230,-5.518973,-9.765541,0.623037,6.620288,-7.793535,-0.453939,1.884557,6.201507,2.952283,-0.597010,-0.808789,5.391857,5.044614,-5.166565,6.865753,3.560324,5.505251,9.051472,-6.597395,9.682715,2.853530,-8.497846,-0.191911,1.898543,9.248116,-2.336615,7.269056,9.446999,7.282224,2.789239,-7.511508,-1.058662,5.264695,-9.603423,-8.198126,-5.576445,-8.159209,9.395238,-5.591240,-5.099836,-9.730796,1.585265,-6.915389,-7.518605,-8.376835,-8.958235,-5.826598,9.725818,-2.861727,3.090143,8.042039,-1.289766,-1.575350,-3.188349,-5.819504,6.538974,8.157378,8.302166,9.177377,1.346028,6.686865,9.260946,-5.646114,9.164495,-5.177814,-4.595222,2.753038,4.844405,-7.081389,-0.942248,-7.665002,9.452738,5.740591,8.384776,-9.563464,-6.408511,-8.227047,-9.209583,-9.906983,8.934965,-3.504713,2.652430,-2.227841,-2.451182,-9.127909,-6.043643,-1.887391,0.230520,-6.060188,-1.890782,9.156138,-9.953209,-1.872237,6.549999,4.433501,-9.121263,-3.599987,1.721459,-6.423767,0.903308,-4.717707,-9.857368,1.074375,-3.028059,-5.774239,-8.443297,-5.594072,-8.400853,5.814101,9.564971,-0.262668,3.623363,6.176905,-1.621499,-8.998392,2.190938,4.145470,5.509213,1.254976,-2.267789,-0.961065,8.653898,9.604200,-9.538314,5.699144,2.900020,2.340413,-5.827423,3.139569,-9.057983,-8.787732,4.324749,5.273893,-8.874093,-9.802539,6.560534,-3.346760,9.015399,-7.142486,-0.459504,-0.711439,5.380279,-0.381706,-5.914111,-2.621270,8.292303,-4.115063,-5.938522,4.924852,-5.721882,1.933808,6.068569,7.558867,-3.567949,-7.941631,4.448694,-1.399403,-7.986977,2.487332,8.703177,6.381740,-7.067885,4.263818,-3.005415,-2.773920,-5.724955,-9.496644,1.195476,9.165450,3.277027,-0.550020,-2.941258,5.936296,-4.246281,0.717609,7.907719,-0.841369,2.612112,-8.368283,8.409909,-2.140789,2.589591,3.904586,-1.538509,-3.834677,-6.551270,3.193063,9.595832,5.588168,8.022952,5.916106,1.293192,-7.083890,6.133756,-9.017331,1.823330,4.263140,4.246647,9.564226,8.429659,2.879607,2.911708,-4.904813,-5.639801,-4.675380,-5.432301,-8.968917,3.885818,-6.192533,5.160019,5.459290,-8.426630,4.507767,3.751264,4.490119,-2.658923,-0.670420,4.954016,7.367918,-7.189425,6.290918,3.628438,0.759749,4.724648,-8.816894,-5.604474,4.921072,-3.487948,0.802386,-7.839327,-5.161097,7.581340,-4.547028,0.687857,-3.626569,4.808310,-6.590924,2.189393,0.961169,-7.169066,-7.093776,-3.269690,3.788891,-0.090173,-0.957423,0.456504,-8.192208,-6.994219,-1.646436,-8.432394,9.741114,-6.461664,-3.347146,1.058776,-8.140085,1.398544,7.901075,8.806227,-8.457765,1.360475,-6.767575,6.148668,4.069124,4.152706,5.470751,3.458096,9.857610,8.900539,8.078730,5.307799,-5.429370,-5.750970,-2.223706,-0.181897,-8.931420,-3.156359,-7.500259,3.724930,8.822794,9.797612,-1.389851,1.891451,7.806282,2.254845,-8.278916,-2.984228,-4.142634,-0.930107,-5.536539,8.127375,-4.808027,7.472621,-0.108128,-3.975285,0.912497,-3.562995,-6.037623,4.102351,-4.854825,5.700614,-1.230213,8.245327,-8.999980,1.788515,-5.591711,7.792659,-9.680511,-3.354773,5.852326,-8.704527,-2.277105,-6.190016,2.959972,-8.565908,5.381881,-6.481467,-2.787452,-4.227291,4.250958,7.598355,-9.524550,-6.504831,-9.771818,9.812560,1.102287,-0.935460,2.947640,4.421287,4.522631,-7.058149,0.034286,-3.332740,3.257752,-7.564775,-4.452367,-0.511500,3.938727,-1.804214,2.072586,2.324951,4.417806,5.589392,7.891027,1.255209,-7.228802,2.212894,-6.784647,0.125018,-4.686219,-7.054733,-1.051931,2.133591,5.502927,7.948525,-6.635821,-6.754465,-1.503489,-4.855702,-6.032059,-9.206256,6.258083,-6.029376,0.806688,5.985859,8.399202,1.998984,9.209269,7.014584,-5.694032,9.074793,-1.299471,-2.740171,9.916713,-8.057809,1.164240,4.456087,-3.561720,-7.749497,1.883983,5.780582,-3.952616,-2.455252,4.920159,-0.752934,-4.057672,-5.443755,4.220668,-9.350007,7.850956,-3.895954,9.307758,-7.699488,6.850045,-4.062852,-4.247804,-1.964351,-8.519331,-7.258398,-3.293335,2.988222,2.869189,5.858941,-0.814818,3.353321,-5.108555,-3.611111], dtype = "float64")#candidate|6125|(1080,)|const|float64
const_6126 = relay.const([[6.274594],[6.668540],[0.353897],[-6.233451],[-7.844743],[8.235147],[3.874680],[2.362154],[-9.106847],[-8.252334],[-9.500515],[-8.605717],[4.214838],[6.940852],[1.671145],[-3.362364],[-4.379681],[-1.680456],[-8.962030],[0.093674],[-9.501782],[-7.723996],[-8.838648],[-6.500208],[-2.815368],[4.847479],[7.193983],[6.936976],[-7.222977],[-5.445645],[-8.012564],[-5.419891],[-1.384888],[-9.711795],[3.898255],[-5.933752],[-8.211433],[-5.628660],[-7.006762],[3.701001],[7.576755],[5.739576],[4.449049],[3.138601],[2.085826],[0.559935],[-8.614878],[-4.937503],[0.193640],[7.508106]], dtype = "float32")#candidate|6126|(50, 1)|const|float32
const_6127 = relay.const([[True],[False],[True],[True],[True],[True],[False],[False],[False],[False],[False],[True],[False],[True],[True],[True],[False],[True],[True],[False],[True],[True],[True],[False],[True],[False],[False],[True],[False],[True],[True],[True],[False],[False],[True],[True],[True],[True],[True],[True],[True],[True],[False],[False],[False],[True],[True],[False]], dtype = "bool")#candidate|6127|(48, 1)|const|bool
call_6124 = relay.TupleGetItem(func_2733_call(relay.reshape(const_6125.astype('float64'), [10, 9, 12]), relay.reshape(const_6125.astype('float64'), [10, 9, 12]), relay.reshape(const_6126.astype('float32'), [50,]), relay.reshape(const_6127.astype('bool'), [48,]), ), 4)
call_6128 = relay.TupleGetItem(func_2739_call(relay.reshape(const_6125.astype('float64'), [10, 9, 12]), relay.reshape(const_6125.astype('float64'), [10, 9, 12]), relay.reshape(const_6126.astype('float32'), [50,]), relay.reshape(const_6127.astype('bool'), [48,]), ), 4)
output = relay.Tuple([bop_6059,call_6088,var_6089,uop_6091,call_6093,var_6094,call_6107,var_6108,var_6109,call_6111,var_6112,call_6115,call_6118,call_6124,const_6125,const_6126,const_6127,])
output2 = relay.Tuple([bop_6059,call_6090,var_6089,uop_6091,call_6095,var_6094,call_6110,var_6108,var_6109,call_6113,var_6112,call_6116,call_6119,call_6128,const_6125,const_6126,const_6127,])
func_6131 = relay.Function([var_6057,var_6058,var_6089,var_6094,var_6108,var_6109,var_6112,], output)
mod['func_6131'] = func_6131
mod = relay.transform.InferType()(mod)
mutated_mod['func_6131'] = func_6131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6131_call = mutated_mod.get_global_var('func_6131')
var_6133 = relay.var("var_6133", dtype = "bool", shape = (15, 3, 7))#candidate|6133|(15, 3, 7)|var|bool
var_6134 = relay.var("var_6134", dtype = "bool", shape = (15, 3, 7))#candidate|6134|(15, 3, 7)|var|bool
var_6135 = relay.var("var_6135", dtype = "float32", shape = (780, 1))#candidate|6135|(780, 1)|var|float32
var_6136 = relay.var("var_6136", dtype = "float64", shape = (18,))#candidate|6136|(18,)|var|float64
var_6137 = relay.var("var_6137", dtype = "float64", shape = ())#candidate|6137|()|var|float64
var_6138 = relay.var("var_6138", dtype = "float64", shape = (1280,))#candidate|6138|(1280,)|var|float64
var_6139 = relay.var("var_6139", dtype = "float64", shape = (364,))#candidate|6139|(364,)|var|float64
call_6132 = func_6131_call(var_6133,var_6134,var_6135,var_6136,var_6137,var_6138,var_6139,)
output = call_6132
func_6140 = relay.Function([var_6133,var_6134,var_6135,var_6136,var_6137,var_6138,var_6139,], output)
mutated_mod['func_6140'] = func_6140
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6398 = relay.const([[[9.129056,-9.812961],[8.494989,-4.795598],[2.572338,-2.585034],[-4.873273,-1.691677],[-5.215547,-4.371919],[8.996689,-3.625294],[0.230106,5.548865],[3.900592,-8.527595],[-5.507976,-6.372286],[3.080352,-7.917306],[-3.420420,-7.381210]],[[1.557590,4.267714],[-0.822788,-3.904876],[7.270610,-8.000246],[5.711266,-1.089944],[-3.297693,8.596480],[2.507118,-1.922254],[-9.718998,-9.204841],[-2.779348,1.207385],[2.713404,3.282940],[0.236958,-5.441077],[-2.364314,8.448825]],[[-9.630221,-2.147424],[-7.997663,7.970948],[-5.254815,5.084854],[2.027945,6.628067],[-6.530898,2.669393],[-0.052817,7.410806],[5.871209,-7.466503],[-8.256164,2.288639],[0.852427,-5.278653],[0.379298,-6.029100],[9.111694,6.572471]]], dtype = "float32")#candidate|6398|(3, 11, 2)|const|float32
const_6399 = relay.const([[[-4.050842,9.752200],[8.466486,-8.678055],[9.022287,-3.965121],[9.164135,-5.521778],[-4.316179,0.110699],[8.970487,-0.527061],[-3.579685,1.344202],[-4.313912,-6.557627],[-3.843899,0.360247],[9.278049,-0.588065],[5.667938,-8.415914]],[[-0.150352,4.962032],[2.074903,8.586345],[6.976608,-1.163743],[9.862630,7.327101],[-1.868312,8.406528],[-9.480281,-9.144458],[-0.114420,-0.614626],[-5.307730,1.958706],[9.462728,3.456818],[3.196218,-8.653598],[-8.010931,-7.822324]],[[-0.571644,-9.299465],[7.968859,-9.226537],[-0.590094,-4.369576],[6.452472,-5.883410],[1.884646,-9.732892],[-3.268089,6.209741],[-8.773048,-1.533855],[-6.633059,8.986173],[4.841864,6.574071],[6.721207,-7.741145],[3.903930,-8.799559]]], dtype = "float32")#candidate|6399|(3, 11, 2)|const|float32
bop_6400 = relay.floor_divide(const_6398.astype('float32'), relay.reshape(const_6399.astype('float32'), relay.shape_of(const_6398))) # shape=(3, 11, 2)
output = relay.Tuple([bop_6400,])
output2 = relay.Tuple([bop_6400,])
func_6412 = relay.Function([], output)
mod['func_6412'] = func_6412
mod = relay.transform.InferType()(mod)
mutated_mod['func_6412'] = func_6412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6412_call = mutated_mod.get_global_var('func_6412')
call_6413 = func_6412_call()
output = call_6413
func_6414 = relay.Function([], output)
mutated_mod['func_6414'] = func_6414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6412_call = mod.get_global_var('func_6412')
func_6414_call = mutated_mod.get_global_var('func_6414')
call_6465 = relay.TupleGetItem(func_6412_call(), 0)
call_6466 = relay.TupleGetItem(func_6414_call(), 0)
output = call_6465
output2 = call_6466
func_6489 = relay.Function([], output)
mod['func_6489'] = func_6489
mod = relay.transform.InferType()(mod)
output = func_6489()
func_6490 = relay.Function([], output)
mutated_mod['func_6490'] = func_6490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6412_call = mod.get_global_var('func_6412')
func_6414_call = mutated_mod.get_global_var('func_6414')
call_6585 = relay.TupleGetItem(func_6412_call(), 0)
call_6586 = relay.TupleGetItem(func_6414_call(), 0)
func_1409_call = mod.get_global_var('func_1409')
func_1412_call = mutated_mod.get_global_var('func_1412')
var_6598 = relay.var("var_6598", dtype = "float64", shape = (3, 6))#candidate|6598|(3, 6)|var|float64
call_6597 = func_1409_call(relay.reshape(var_6598.astype('float64'), [6, 3, 1]))
call_6599 = func_1409_call(relay.reshape(var_6598.astype('float64'), [6, 3, 1]))
func_3038_call = mod.get_global_var('func_3038')
func_3041_call = mutated_mod.get_global_var('func_3041')
const_6613 = relay.const(-2, dtype = "uint16")#candidate|6613|()|const|uint16
const_6614 = relay.const([-5,-6,-4,9,7,10,4,-2,-6,2,6,-7,-10,-9,7,-7,-6,1,7,-6,9,8,-9,8,-7,-7,6,-7,6,7,7,8,-7,5,-8,10,-9,3,-7,5,-1,4,-6,-2,-9,8,4,-1,-4,7,-9,9,3,8,-1,3,-5,1,-10,-8,5,8,9,-10,-8,-4,4,-7,-5,7,9,-10,-9,-8,6,-1,-1,8,-8,4,7,-5,9,-8,-8,-2,6,-1,-5,-7,6,-9,7,-8,10,-1,8,-8,9,-3,2,1,-9,5,5,2,2,-10,-1,-3,10,7,-3,7,2,6,7,-2,-4,-8,-2,2,-4,-2,1,-7,3,-1,1,-6,-9,-7,-2,3,-9,-4,-3,-5,-9,5,4,2,-8,-4,10,1,4,6,-8,-9,1,-8,-10,-5,-1,8,2,5,-1,-8,10,-10,9,10,4,6,5,-2,-8,3,-7,5,10,-7,8,4,7,10,-2,3,10,-3,-3,9,2,-1,2,8,3,-7,-3,8,-6,5,-9,-4,-8,-5,2,4,-5,-4,-10,-2,-2,-5,1,6,-4,-7,-9,-3,8,10,3,7,-1,-6,7,-8,-7,5,-8,5,-10,-4,-3,-6,4,-4,-9,4,4,-1,-8,-2,-1,2,8,9,2,-6,10,-10,9,-1,7,-8,-5,-3,-9,-7,2,10,-1,-7,-4,-9,-7,1,3,4,-9,-2,-3,-9,-2,3,-8,-3,5,1,4,-4,-9,9,-6,3,-7,-10,-1,-3,5,-8,-2,-1,2,-6,2,-9,4,-10,-1,8,9,10,-6,3,-2,6,4,9,-9,-2,5,-9,-9,1,-3,10,6,-2,-5,-4,7,-1,7,-7,-4,-5,-10,10,-5,-1,-10,10,1,8,6,2,-4,-2,-2,-7,-8,9,-9,9,-2,2,-1,9,4,-9,1,-2,4,-6,-5,-5,5,2,3,-8,2,-6,-2,-5,2,7,-5,8,6,-6,-7,3,4,-4,7,-9,-1,1,2,2,-10,-9,9,-2,1,6,-8,-10,6,-7,-7,1,-5,-3,-10,1,5,3,-7,-7,-3,-8,1,3,-3,10,1,8,-8,3,8,-6,-3,-5,5,1,-6,-1,7,6,-6,-10,2,3,10,7,-1,1,3,-6,-1,-6,-8,-7,1,-6,2,4,-5,3,4,-7,3,10,-5,2,-5,-4,7,9,5,-5,-3,-10,-9,-6,-2,-7,-3,1,-5,-6,3,-3,-3,8,-8,-4,3,9,-6,-4,-10,-5,10,-10,1,5,-8,-4,-3,-9,-7,-3,-7,-2,-9,-3,-9,-9,2,-6,-5,-7,-3,4,-5,-8,3,3,-4,-3,3,-2,-4,-5,-2,9,4,-2,1,5,-6,8,-6,1,8,-5,-2,7,-9,2,3,-1,-1,6,-9,-6,5,6,7,-1,3,-7,-4,1,-7,7,8,9,-10,-9,-7,6,3,3,-1,-4,-2,-9,7,10,-5,-6,-4,2,3,3,-8,-3,-10,10,3,-6,-7,3,-7,10,1,-4,-4,-9,10,8,-2,1,-9,3,-5,9,4,-7,-7,2,2,3,4,2,5,-2,-1,6,3,4,-8,9,-4,-4,3,9,4,3,3,2,5,2,8,-8,9,9,4,1,6,3,3,-5,1,7,-3,-1,-6,8,10,4,-7,-9,5,-3,9,-8,-7,1,3,3,10,6,-6,9,10,7,10,-2,-10,-4,2,-9,-9,6,-10,-7,4,6,10,6,-1,-9,1,-6,8,-7,-5,9,1,-5,-6,-9,10,10,1,9,-1,4,2,4,-1,-2,1,10,9,-1,2,9,7,9,7,3,10,3,-7,-4,10,-7,-1,3,4,7,7,-5,5,-4,6,2,5,8,2,2,-1,-3,8,2,-9,8,-7,10,-1,-6,-2,-2,2,10,-5,-6,-3,-9,-2,-3,-4,-8,-7,2,-5,-6,-7,-5,-2,2,7,-6,-4,1,7,-8,-8,1,7,5,2,-10,-4,7,-9,-3,-7,-9,3,-9,-8,1,-5,1,-6,5,-2,8,-9,-1,-3,7,3,-3,9,-9,8,3,4,7,-2,1,-7,-7,-3,-5,5,8,-1,6,-10,-7,9,-4,-3,5,5,-9,-5,9,7,6,-7,9,3,7,2,-4,3,-6,-2,4,-8,-10,-1,3,-10,-1,-3,-6,-8,10,7,1,-3,-10,9,-2,7,10,-10,8,-1,-8,9,-1,-7,7,6,-5,6,-5,9,1,-9,6,3,-9,2,1,1,10,-4,1,-8,10,-4,-8,2,9,-10,3,8,10,-1,-3,2,10,10,-5,-2,4,-9,8,-4,5,1,-9,-1,-9,9,-5,-5,6,-10,6,5,-5,2,6,-2,2,-10,-2,-2,-3,3,2,7,-5,-9,7,9,-8,7,9,-4,3,-3,-5,8,-6,6,-10,7,9,4,-10,10,-6,-2,8,-7,10,-6,5,-10,6,6,-10,9,9,-5,-8,8,4,10,-6,3,-9,8,4,2,8,5,-2,-7,-8,1,9,-10,9,-5,9,10,8,9,-8,1,8,1,-8,1,3,2,1,-5,1,5,9,-5,3,-6,-2,4,2,-10,-8,-10,2,2,-3,-4,-8,-4,6,3,-3,10,-7,5,-4,4,5,2,4,-9,-3,-1,3,8,-5,9,-10,-3,-5,-8,3,-10,6,4,-6,-6,7,9,-3,1,10,5,-1,10,-7,7,-10,8,1,-5,6,-5,1,5,5,-3,6,-8,6,-6,-6,-5,-2,-2,5,-9,9,4,-1,5,4,4,5,8,-10,6,-7,-2,-4,-1,2,-9,-5,-10,-1,4,-2,-5,8,10,-8,-4,7,-4,-10,1,-5,2,3,-8,-6,10,-1,-5,-8,9,-3,-1,-8,-3,-9,10,-5,6,6,-4,6,-10,-9,-6,-4,-5,7,-9,-10,-5,9,5,-10,1,4,-8,-9,7,-5,-7,7,6,-7,-9,9,9,7,-1,-4,-3,-10,-1,9,-9,1,5,-9,2,-8,-4,-2,3,7,-8,-6,3,4,-5,2,-9,-1,2,5,-5,-4,-10,-1,6,6,-1,7,-8,-8,3,-6,-6,7,4,-2,7,-7,-10,9,-8,-2,-7,5,-7,8,-4,2,-1,7,-3,6,5,-8,-6,3,-1,-5,1,4,4,9,6,7,2,-7,-3,6,8,2,-8,8,-7,8,2,9,-1,5,2,7,5,9,-6,-3,9,-8,10,6,8,9,-5,-7,9,-6,-1,-4,-8,4,10,-10,-5,-5,2,-4,5,-10,2,-9,-9,-9,-9,-9,-8,2,-2,-4,-1,-2,10,3,9,-8,-3,9,1,4,-5,-8,6,10,4,-7,-4,-8,-6,2,6,-6,4,-1,-7,8,8,2,5,3,7,4,10,-6,3,-10,5,-10,-3,-7,-5,-10,-10,-10,6,6,-3,7,-2,-10,10,-8,5,-5,8,-9,-6,10,3,10,-3,-5,7,-2,4,8,9,8,-3,-4,-6,5,-4,-7,-3,8,-5,4,6,5,-5,3,-8,-10,5,-1,9,-4,-1,9,2,-9,10,-1,7,-6,8,8,2,6,-6,-10,-2,-7,7,-6,3,6,-9,2,2,10,-7,7,-8,9,-9,-8,-5,-4,3,3,-5,1,-7,-2,1,10,-2,-9,1,6,-9,1,-1,8,4,2,-2,3,-6,-10,-9,-4,9,-5,1,10,-8,-6,7,5,-9,3,9,-1,-1,1,3,-2,9,5,-9,-2,8,-5,5,-8,-4,6,-7,10,9,-9,-5,7,8,-5,-6,3,-6,1,-6,-6,2,-8,8,-8,-7,1,7,5,-9,2,7,1,4,5,-5,-2,2,7,-8,-8,1,7,7,-5,4,4,-5,-5,9,8,-2,2,-2,3,-3,5,10,3,-5,4,6,-1,2,-9,-9,-6,1,2,-8,-5,5,4,1,-1,-6,6,-2,2,-6,-7,-9,-3,-3,-4,-1,2,9,9,5,-6,6,2,2,4,-4,2,-3,4,1,7,-6,-8,-4,5,-9,-10,-7,-3,-8,-7,-7,8,6,-8,-1,-1,-1,-2,-5,6,-9,9,1,-3,8,-1,-2,6,2,-7,6,-8,6,-6,6,-7,10,-1,7,-10,-5,-1,-2,5,1,-5,-1,-8,4,7,5,6,-9,8,2,-2,-1,-6,-10,-6,-4,-9,-7,-9,10,4,-2,-3,-9,9,-9,8,6,2,6,8,-1,2,-4,1,-1,-9,7,-5,1,8,7,-9,-2,8,10,-6,4,1,1,10,-8,6,-1,2,5,3,5,-4,2,5,-7,-3,8,-9,-5,-4,9,8,1,3,9,-7,-7,-3,2,-3,8,-9,1,7,6,10,-1,5,-10,7,2,6,-4,2,-7,-6,10,-1,-3,8,-10,-5,7,-1,6,-6,4,2,1,6,7,-2,7,-10,2,10,-6,-2,-2,-10,3,-1,-8,-6,4,-6,6,-2,1,-3,-9,4,-9,10,9,2,-8,8,-5,-4,8,2,9,-7,5,5,5,3,4,-7,-5,-7,-1,8,9,7,-5,-1,2,-7,10,-4,1,-10,1,10,-6,9,-1,-3,1,8,-10,2,-9,-10,-3,5,-4,-9,-10,-10,-7,4,-8,-8,9,-6,-7,1,-9,4,-9,-6,-3,7,5,2,10,9,2,-8,-3,2,-5,7,-5,-6,1,-7,-6,-10,4,2,-5,-2,8,10,6,-3,-4,-5,-1,-7,-2,7,-9,-10,6,-6,4,-9,-8,6,-2,5,9,-9,4,5,10,-5,-8,3,8,8,-9,-6,10,1,1,10,-9,-10,-4,-10,-8,7,-9,-1,-2,-2,-8,8,-10,-9,-8,-3,-7,1,-10,10,-3,4,-7,-2,6,10,2,-1,8,5,9,2,-1,-1,-3,8,6,-1,-7,-2,8,-8,-9,-5,10,-10,10,-9,6,-3,-9,-6,-3,7,-1,-6,10,-9,2,3,-6,3,8,8,-1,4,3,4,8,-7,-2,-6,-6,1,-9,-2,-9,10,8,-3,2,-9,-9,1,6,-6,3,-1,7,7,-6,10,7,-5,9,-3,7,-5,7,-4,8,-1,2,-9,4,4,6,-7,3,9,-2,-4,-6,-7,-7,-6,-3,-5,9,-5,-10,4,10,-1,5,-4,4,-10,-6,-3,-10,-9,6,-9,6,1,-2,3,8,4,6,4,7,-10,1,-8,-10,5,1,-4,-7,-4,-10,10,3,-1,3,8,-9,2], dtype = "uint16")#candidate|6614|(1950,)|const|uint16
call_6612 = relay.TupleGetItem(func_3038_call(relay.reshape(const_6613.astype('uint16'), []), relay.reshape(const_6614.astype('uint16'), [13, 10, 15]), ), 1)
call_6615 = relay.TupleGetItem(func_3041_call(relay.reshape(const_6613.astype('uint16'), []), relay.reshape(const_6614.astype('uint16'), [13, 10, 15]), ), 1)
func_34_call = mod.get_global_var('func_34')
func_37_call = mutated_mod.get_global_var('func_37')
call_6619 = relay.TupleGetItem(func_34_call(relay.reshape(call_6612.astype('int16'), [15, 1])), 0)
call_6620 = relay.TupleGetItem(func_37_call(relay.reshape(call_6612.astype('int16'), [15, 1])), 0)
uop_6623 = relay.log2(call_6585.astype('float64')) # shape=(3, 11, 2)
uop_6625 = relay.log2(call_6586.astype('float64')) # shape=(3, 11, 2)
func_5182_call = mod.get_global_var('func_5182')
func_5185_call = mutated_mod.get_global_var('func_5185')
var_6627 = relay.var("var_6627", dtype = "float64", shape = (1815,))#candidate|6627|(1815,)|var|float64
call_6626 = relay.TupleGetItem(func_5182_call(relay.reshape(var_6627.astype('float64'), [11, 11, 15])), 0)
call_6628 = relay.TupleGetItem(func_5185_call(relay.reshape(var_6627.astype('float64'), [11, 11, 15])), 0)
output = relay.Tuple([call_6597,var_6598,call_6612,const_6613,const_6614,call_6619,uop_6623,call_6626,var_6627,])
output2 = relay.Tuple([call_6599,var_6598,call_6615,const_6613,const_6614,call_6620,uop_6625,call_6628,var_6627,])
func_6637 = relay.Function([var_6598,var_6627,], output)
mod['func_6637'] = func_6637
mod = relay.transform.InferType()(mod)
var_6638 = relay.var("var_6638", dtype = "float64", shape = (3, 6))#candidate|6638|(3, 6)|var|float64
var_6639 = relay.var("var_6639", dtype = "float64", shape = (1815,))#candidate|6639|(1815,)|var|float64
output = func_6637(var_6638,var_6639,)
func_6640 = relay.Function([var_6638,var_6639,], output)
mutated_mod['func_6640'] = func_6640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6489_call = mod.get_global_var('func_6489')
func_6490_call = mutated_mod.get_global_var('func_6490')
call_6693 = func_6489_call()
call_6694 = func_6489_call()
output = relay.Tuple([call_6693,])
output2 = relay.Tuple([call_6694,])
func_6695 = relay.Function([], output)
mod['func_6695'] = func_6695
mod = relay.transform.InferType()(mod)
output = func_6695()
func_6696 = relay.Function([], output)
mutated_mod['func_6696'] = func_6696
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6412_call = mod.get_global_var('func_6412')
func_6414_call = mutated_mod.get_global_var('func_6414')
call_6810 = relay.TupleGetItem(func_6412_call(), 0)
call_6811 = relay.TupleGetItem(func_6414_call(), 0)
func_1324_call = mod.get_global_var('func_1324')
func_1326_call = mutated_mod.get_global_var('func_1326')
var_6824 = relay.var("var_6824", dtype = "float32", shape = (780,))#candidate|6824|(780,)|var|float32
call_6823 = relay.TupleGetItem(func_1324_call(relay.reshape(var_6824.astype('float32'), [6, 10, 13])), 3)
call_6825 = relay.TupleGetItem(func_1326_call(relay.reshape(var_6824.astype('float32'), [6, 10, 13])), 3)
bop_6830 = relay.less(var_6824.astype('bool'), relay.reshape(call_6823.astype('bool'), relay.shape_of(var_6824))) # shape=(780,)
bop_6833 = relay.less(var_6824.astype('bool'), relay.reshape(call_6825.astype('bool'), relay.shape_of(var_6824))) # shape=(780,)
uop_6854 = relay.atan(call_6823.astype('float64')) # shape=(6, 10, 13)
uop_6856 = relay.atan(call_6825.astype('float64')) # shape=(6, 10, 13)
output = relay.Tuple([call_6810,bop_6830,uop_6854,])
output2 = relay.Tuple([call_6811,bop_6833,uop_6856,])
func_6872 = relay.Function([var_6824,], output)
mod['func_6872'] = func_6872
mod = relay.transform.InferType()(mod)
var_6873 = relay.var("var_6873", dtype = "float32", shape = (780,))#candidate|6873|(780,)|var|float32
output = func_6872(var_6873)
func_6874 = relay.Function([var_6873], output)
mutated_mod['func_6874'] = func_6874
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6913 = relay.const([[[4.494876,-8.732914,3.855546,-9.857496,2.688572,-9.077413,-7.335453,4.444287,6.290977,-9.119903,0.445753,-6.090938,9.124517,-6.435230],[7.123132,8.068918,-5.715607,-2.529561,-0.687318,1.976138,-7.951514,8.558929,-8.020094,1.113646,2.054624,-6.974578,-0.304785,-7.014417],[0.748056,0.773938,-3.754801,3.242146,-7.067681,-4.459848,-2.892790,-9.098345,7.958618,-0.351668,6.511526,-5.750747,1.868390,9.103566],[9.552730,3.082696,-0.377892,0.363596,-8.589972,1.738062,-7.749450,8.949812,-3.730379,-8.724820,6.967113,6.301941,-6.842859,-1.332471],[-2.232880,9.118371,6.143174,-2.468042,6.365190,3.325355,-2.334296,-4.489649,-7.808441,-8.160877,-7.504089,0.380357,5.821633,-1.533771],[-6.299292,1.263399,-6.882934,-9.283649,3.197559,0.034273,-1.565058,-0.200550,-1.718449,5.509608,4.794294,3.122429,-1.256496,7.434768],[5.977727,2.714346,-9.847822,-7.316521,7.355731,7.774955,-8.276004,2.287499,7.422113,6.566405,5.429762,-4.380298,-3.629382,-1.897900],[-7.078947,-9.448312,7.305316,6.912925,-0.922025,-9.932682,-3.912334,6.211784,-4.703682,7.378598,-7.088385,8.727138,-9.538573,-8.077552],[9.005019,3.445138,6.513306,4.558348,-5.317925,-9.286061,3.471854,-5.749748,-6.645040,-3.827460,5.670952,-5.393331,-0.783565,5.020597],[-7.943837,-5.463884,-5.689239,4.914508,0.364538,-0.648961,-9.922220,2.680403,4.369154,0.398707,9.536836,-2.715171,-3.066764,-6.581268],[1.852378,5.674616,-6.498950,9.561505,2.922368,-1.643848,-7.229196,-0.589870,4.827945,-9.468715,-2.051794,9.429103,5.755525,-0.285872]],[[-4.926682,-2.960685,-4.312902,3.858955,1.645923,7.140187,-7.944799,-0.068812,-4.958884,1.336642,-6.763092,-3.801229,8.316211,-9.969681],[9.816825,-5.902549,4.261580,6.255981,-4.645483,-2.083582,-1.769085,1.891555,5.584068,8.809943,-1.336216,-5.920083,-4.852278,1.382742],[-1.227080,-7.553833,-4.297666,2.590039,6.657723,2.348636,-1.405640,-8.139760,5.149979,8.827384,4.822342,-0.981515,4.973545,-7.707850],[1.241843,6.342758,8.274192,-6.755119,1.265805,8.750608,-4.361679,-9.993761,5.418629,6.707124,-7.497012,1.536133,8.613459,-1.324513],[-3.313289,-9.460455,-9.691404,5.667410,2.425059,-8.005323,-7.184926,-6.396970,-2.367856,7.680321,8.412673,3.508013,2.528035,8.759667],[-5.223079,0.073357,-8.700887,6.865521,1.332333,-1.852996,-3.638047,6.443415,-1.254845,9.324033,7.007501,-4.600317,-2.187154,-5.027673],[4.347572,-0.866275,9.276625,-8.659665,-2.940967,6.220354,0.326181,-4.364996,-7.607630,-9.984491,1.848337,5.934087,-9.875761,3.024065],[9.954812,-0.573824,7.927085,2.616248,-7.920713,-4.736626,2.501563,-4.889345,3.091927,-4.954894,0.174414,3.348334,-7.100487,9.136422],[-2.907530,7.386989,-7.304388,-1.200513,9.478804,9.300637,-3.385568,-7.471531,7.691767,-6.887991,9.835915,-7.425394,5.239475,-8.124451],[-4.113419,-7.782917,-3.963303,5.296285,4.256506,6.267125,6.885825,-7.054688,-1.379873,0.254969,3.139779,2.429237,-7.771961,2.633193],[1.042994,9.514238,1.281768,-0.430529,-6.158443,4.840673,-2.548436,-0.552021,9.749046,7.529601,1.385511,6.925309,-2.498575,7.541669]],[[-6.434456,-2.049061,-8.084980,8.171486,3.791299,-0.309392,5.516871,7.278095,-4.558523,9.294785,-6.741697,4.390031,5.023432,-7.407225],[3.133462,-1.589383,5.346336,5.730740,5.306711,6.729811,6.452906,-0.878243,5.632382,-6.474001,2.166350,4.885878,-5.694523,3.947929],[4.026695,6.275647,3.103936,-8.415332,-2.507692,0.901021,5.385803,-4.680647,-2.171538,9.430820,-4.695667,8.007489,-1.562636,5.986239],[3.379638,-8.637223,-8.801419,-8.414976,-2.491303,-6.575662,-2.948847,-4.674120,2.520606,-0.753691,4.200968,0.964572,5.443076,2.957575],[-4.177489,-4.159411,5.062982,-2.079567,-1.717510,0.267106,-8.306143,0.149445,9.430941,-3.332849,-4.699910,-4.103312,-5.605261,3.545379],[-6.340919,2.807964,8.068337,8.040349,0.489659,1.117710,-9.182065,-7.404878,-4.152499,0.681688,7.348756,-1.899867,8.556724,5.636927],[6.117795,0.171659,6.386726,-5.468298,5.098378,1.251685,4.389119,-5.518287,1.087781,-7.930209,2.508985,-8.518527,8.770781,-5.913704],[7.079628,2.955183,7.869016,0.127830,8.505169,4.174857,5.278927,9.083207,3.573056,-2.194390,-0.907570,3.023001,-4.010732,-4.864627],[-7.705969,-1.740012,-3.142596,-6.088682,1.753535,-1.019246,3.144469,4.106439,-9.287396,-3.660532,-8.276103,4.171975,5.039684,-4.996160],[-0.925165,-5.746730,-7.801978,-4.686898,-7.324678,-5.976361,-2.548153,-1.369996,-4.417417,-7.560274,8.388780,0.909460,0.133805,-4.495858],[1.780706,0.102164,-2.584465,-8.684105,-5.387537,1.101972,-2.945930,-1.980634,9.075962,-2.863104,-8.988723,-9.644946,9.155261,-8.911058]],[[-5.226636,-2.617110,3.442441,9.266075,6.822206,-4.311282,6.107989,-7.564603,8.483959,-5.592428,7.384616,3.393715,-2.322795,9.703677],[4.171395,-8.280497,7.695801,4.039356,-8.860784,-6.773995,-3.883548,-5.302734,-2.138485,3.138445,8.475820,-1.894729,7.000720,3.262648],[-8.790943,8.583716,-2.186767,3.219948,-5.156044,-6.253834,-0.904811,-0.268954,-8.759562,-6.127639,4.208540,-4.864001,2.432360,-9.970260],[-6.172112,-1.680457,-9.555869,-0.422020,-8.966442,-8.997372,-1.448149,9.101513,2.352569,-3.320071,-1.939753,7.060331,-0.584093,2.959165],[-7.063231,-5.153277,9.164657,9.198835,9.171528,-3.661706,-5.746733,-5.135328,1.396869,0.771790,-1.787379,-7.004765,-0.429282,-2.967631],[-1.326767,-5.437106,6.802274,1.290786,-4.111337,3.068505,9.785991,6.852356,-3.281200,-8.446893,2.404533,1.743113,5.799384,5.794638],[2.996577,2.126086,2.880116,-4.959346,-8.081550,5.260140,5.406153,-7.102292,-9.068774,-2.012244,-4.749543,-5.208219,-5.457805,1.203306],[-6.641248,0.982690,-7.886165,1.799933,-7.605653,3.613877,4.102197,9.971858,7.005372,6.226280,4.116415,-5.534125,3.830191,-9.973278],[-1.254110,1.294614,-7.711471,-7.301515,3.571169,-6.253734,-8.237849,2.922512,-9.477275,-1.095598,-4.409717,0.888973,1.014158,4.635851],[-4.361509,-5.849128,4.849118,1.777284,-5.831514,8.965565,4.797240,9.723985,2.766425,-7.897885,-7.868802,5.399883,-7.727772,-2.254816],[-6.133034,-8.502756,3.037819,-4.601813,5.070952,-7.910594,9.966219,1.343716,9.946572,-0.093231,2.300091,-6.886271,7.699066,0.316998]],[[-5.730262,9.765778,7.028174,-9.681414,-9.429662,-2.201484,-3.354083,4.989705,-0.742264,5.547029,-9.771667,-6.027425,-4.227417,2.299685],[-8.700117,3.641648,-3.155849,0.337716,7.445912,7.503703,-7.040422,0.075213,-1.150259,4.286631,8.233857,2.625130,-3.876157,-9.364139],[-2.162334,9.575217,-9.956877,-7.839995,8.977832,-9.410968,4.260079,3.647873,4.758848,-1.048603,4.293786,-7.271695,-6.440942,-3.833348],[2.209991,9.811298,-6.506132,-0.373742,-3.192127,-8.709246,7.132685,-8.249288,-6.898945,-5.105814,-1.575773,7.432256,-5.133900,-5.483142],[8.045418,-2.548931,6.819071,7.728492,-3.852898,-9.765218,-2.350255,-8.665641,-9.834321,-5.563471,-7.722841,-1.637619,2.175062,7.834331],[-1.670269,3.082072,-7.677586,-9.908886,0.921570,-3.535152,-2.531537,-1.285190,7.879701,-2.616309,3.118710,-1.838340,2.055175,-0.187596],[-6.494268,5.302311,-2.429407,8.536654,-8.290355,-7.638449,1.668481,0.400016,-7.566627,-9.721609,-5.672466,2.071999,1.812082,-3.788402],[-4.624683,0.733385,-8.589520,1.834896,9.223655,7.047982,5.808776,-2.768074,-1.011489,-9.171512,5.636620,-9.739506,2.570876,-0.515409],[1.398379,6.412655,1.802004,2.869451,9.305870,-1.738741,9.031294,-1.692585,-7.097716,2.106557,-8.001866,5.995992,-4.169644,-7.800777],[6.120096,-2.240781,7.110574,-8.550116,-5.743645,-0.381454,8.722470,4.758632,-6.333780,4.397090,-4.527951,-2.046512,-4.805053,-5.358241],[9.558185,-6.478435,5.266332,-7.952530,-1.705715,-1.811792,-8.543556,0.462957,3.971923,-0.481577,-8.662791,-9.718012,-1.170249,-4.160008]],[[-9.041712,3.562344,0.211683,-9.795908,-9.312050,9.068127,-3.484829,1.048594,-1.041276,-8.958756,3.347184,3.620652,-9.920550,-6.121424],[-9.105111,3.446510,-6.919850,3.166810,-9.691696,-1.557440,-1.256008,2.040374,5.360629,2.693373,9.191475,-1.114545,-8.755003,8.858450],[9.780398,5.601326,-4.897714,1.239849,2.526095,-3.894208,-3.026460,-4.678640,-3.776451,0.802076,-6.195152,0.126438,-5.556212,3.794938],[0.239644,2.103205,-7.414991,6.862851,8.217849,2.848949,4.326921,-2.162771,4.520065,-0.774970,5.394183,6.026603,-8.314568,7.107844],[-5.699458,4.604832,2.881728,8.515586,7.873386,-7.406761,7.487235,5.203222,3.480153,-6.668973,-9.217190,-2.155006,4.487821,4.513182],[-3.984129,-5.734737,8.418112,1.444380,6.397360,4.571726,3.031688,2.434139,3.814627,6.894387,3.101032,7.804382,-1.566017,1.642346],[-4.252680,9.837202,6.377620,8.643113,4.346790,-4.575110,0.337790,7.040167,9.654396,0.183750,1.971184,-3.547922,7.590361,-6.971383],[1.556601,0.134536,-1.893414,1.035179,-6.531500,5.242940,6.767828,-6.437846,6.725453,4.978115,3.111009,5.521099,3.244231,1.872755],[-9.372182,-6.251344,7.421014,8.054853,-5.191699,7.001228,6.851484,-7.578059,-5.721522,-2.448741,-0.149771,8.836459,-6.694198,-3.051602],[-0.039777,-6.469070,2.578369,-9.466690,-2.975523,-2.017056,-4.681123,-8.430811,-8.956513,-8.895501,4.253288,-3.236298,-0.930985,0.873022],[0.795156,-4.746789,0.633762,-8.448401,2.619662,2.266171,-4.238083,-5.069069,-6.315473,-2.152307,5.291586,7.201775,2.401267,-4.719690]],[[0.465977,2.759163,8.869100,-1.868275,-9.095247,2.796874,-6.769884,-9.812655,6.632993,6.440019,7.116738,-2.802941,7.174936,6.580225],[-7.208359,-7.067315,-6.607559,-3.910019,-7.252989,-0.873201,1.320903,-2.092276,5.500409,-9.729692,-2.223078,-6.042181,4.324270,-7.641885],[-4.044569,-1.100000,-3.029940,0.054252,-5.369892,-5.199383,-9.520930,4.279040,6.776248,6.437020,-3.544757,5.747491,-8.322636,-4.239069],[-7.275785,-6.529181,2.260850,2.110888,2.571251,-4.992084,-0.664590,-1.137472,2.619838,-1.343604,-1.211158,5.515128,8.148581,4.278921],[-1.777997,-2.401214,-9.395566,-8.696539,0.391356,4.535832,-0.954901,-6.737642,6.265277,0.124385,-7.827696,5.425725,-6.224949,-5.475482],[9.173914,4.898840,4.956737,-7.077008,-7.462999,2.498913,3.120398,-1.267521,-6.558088,-0.985466,-1.304926,7.044188,-8.186984,4.847969],[9.617969,-0.487929,1.205691,6.572276,8.360010,-7.837637,-0.044750,7.630632,6.193148,2.112518,-2.463883,2.253121,9.751987,-3.522665],[9.685994,-2.766496,8.252592,8.332284,-6.205014,7.030992,-7.809862,5.175940,-7.691812,-2.428193,4.530940,0.129146,-1.062736,-1.594935],[7.736374,0.148987,-0.145446,-8.783579,-8.653547,-2.394404,-4.358743,0.119401,0.668517,3.253379,7.152784,2.506338,6.898104,3.661203],[7.792599,9.948891,-8.064353,9.596200,6.527808,-7.720298,5.365005,-5.649520,-1.464372,8.414914,3.288301,2.138161,-2.123487,8.486015],[-9.819090,8.992522,-2.337711,-4.241421,6.473210,8.870210,8.887390,3.495662,-0.001589,-5.153735,8.832122,-8.271158,-0.091947,4.236924]],[[4.214262,-9.532991,9.254180,3.943932,4.416256,-4.661549,-4.362501,7.894210,3.771210,-6.017649,-6.939151,7.013722,-5.717325,-7.833140],[5.402994,-9.681796,-5.349783,-0.991035,-5.992056,6.891106,-1.904478,9.669060,2.112098,-9.484373,2.383196,-7.543664,-3.685957,6.983161],[-7.161351,4.593644,5.622696,-6.555817,8.551133,-6.818782,-4.535686,9.265574,3.893967,9.773494,1.597370,-4.218994,5.187251,-4.324171],[-8.775967,-7.525302,-8.967930,-1.066359,9.564198,0.286154,-1.933845,4.758764,-6.779292,7.449300,5.978977,-3.183817,-9.575249,7.217554],[-5.808216,7.769558,7.355239,9.817929,-9.966621,1.831105,-5.021825,-1.336757,-5.728768,4.909358,-8.942375,7.383059,-7.532303,-7.518623],[-2.240392,-1.333706,4.197792,7.358143,5.925426,-3.341141,-3.052179,-2.702091,2.172523,7.978779,-3.953138,-6.669599,7.742290,-9.927275],[1.360407,6.902806,-6.464764,-7.075663,1.392557,-0.616849,-2.391331,-1.213941,-2.564304,5.424380,3.071933,-3.253884,-3.337373,-5.029828],[-7.759201,0.648013,9.887353,9.571175,-7.719322,-6.469180,5.320628,-2.874543,7.701444,-9.760611,3.792394,4.469614,0.376777,-1.503130],[-6.933256,2.813555,5.503176,8.472061,6.984867,-1.155645,-9.157566,-4.049609,4.399078,-9.497201,9.410998,0.542279,-7.627806,-7.467284],[-7.474710,9.430536,9.685321,3.334605,8.757178,-9.441718,6.291471,-7.549236,9.209364,1.077759,-4.506524,2.489789,-6.760755,-6.659773],[-1.422840,-9.706062,-8.535724,9.680319,4.324791,-7.971834,9.015288,2.977519,-8.071889,3.998022,-4.328906,-5.773807,-7.145920,7.822439]],[[-1.149738,0.583916,-5.364193,2.165319,-3.150466,-4.841260,0.643033,-7.309735,0.126497,1.594411,-7.442468,9.704283,8.148026,3.252310],[-4.658562,2.518805,-9.468386,6.673130,-0.918070,0.550635,4.611882,-1.039611,6.928229,-0.044828,4.492415,-9.249148,-1.371810,-3.655978],[6.246448,5.045296,-2.928269,8.044045,7.739916,3.379696,8.612052,-1.776092,5.809915,-8.946125,-2.878830,8.452527,-5.085336,7.161850],[-5.115970,5.254779,7.156245,5.451293,2.330787,-7.170553,9.156359,-8.771296,8.423722,8.694263,-7.882714,6.120659,-1.497727,-2.695963],[-9.670971,0.396349,5.267991,-0.264476,7.870348,0.988688,-7.114364,-1.925305,3.168558,3.454518,9.138685,4.649485,-5.438324,-4.683356],[-8.733639,0.703923,-3.810493,6.217001,4.655247,-4.995002,1.008619,0.786755,-1.518692,9.322595,9.423457,-1.904605,8.560678,-4.538567],[-4.539478,1.067974,1.968840,7.254435,6.690103,5.452596,-9.152390,-9.066423,0.812261,-3.252669,8.198488,-4.616642,-9.187246,7.695659],[-2.699399,4.410514,1.427217,0.662559,4.001336,-7.888689,0.070642,-2.252827,-6.091701,7.591523,-5.385877,6.690354,1.995618,-3.617527],[-8.259150,-1.818249,8.911476,9.391699,-8.466015,7.100981,2.872875,-4.268569,-4.301217,-9.009836,5.300883,-0.566469,4.901849,7.875724],[7.627139,-8.336346,-2.788276,6.495972,-0.372863,-9.473040,0.969518,0.655911,6.106550,-6.751682,-6.758407,-6.875705,-9.831292,7.308290],[-4.698047,8.479401,0.092196,5.444344,-0.851649,0.453630,9.753562,6.653708,-9.598206,8.915822,-8.195732,1.973476,5.712370,9.987526]],[[-4.928227,0.950114,4.876218,8.629102,2.578692,-7.883885,1.997711,-6.384895,1.739105,4.665211,-2.187399,-1.066767,-0.538543,1.778557],[2.572420,-8.887901,-4.129952,4.026790,-8.142265,-0.062187,7.850909,9.481084,-7.751527,-8.938214,6.963893,9.081324,-4.981220,-4.388195],[6.722170,-5.053390,-3.473221,9.153990,1.114193,8.721833,7.408500,2.768967,-6.258892,1.054550,-9.246877,6.152896,7.158980,-5.435383],[-8.486204,4.396910,-3.155414,-2.659964,-1.501376,4.113221,-6.091577,8.107167,-7.194311,7.307263,9.834957,-7.071635,-2.779247,9.491443],[-5.478554,2.761443,-9.655759,9.584576,6.963855,-2.660411,5.011768,0.016576,-2.568609,1.254616,0.159455,9.506527,8.774136,-1.352084],[6.512179,1.301240,7.884054,-8.232795,5.003197,7.939865,-6.946600,-6.682386,9.229144,9.660901,-9.003377,2.330371,4.538894,-8.119794],[-7.383424,-5.173055,-6.358430,3.768372,9.619735,-7.623069,1.899105,5.030937,5.096645,4.706853,2.373315,-4.054194,0.940326,8.543062],[-9.135029,5.007388,-6.640881,4.329319,-6.897607,9.609640,-1.653396,-4.883527,0.710570,3.536212,-2.600227,3.708764,-2.284542,2.280934],[4.028071,-4.077572,5.778251,-0.627785,-7.319918,-0.247921,5.838237,-1.179037,2.368597,6.797428,-5.529432,3.764541,-9.019983,-4.541373],[-6.319407,-5.624803,-5.027487,-3.330673,0.587773,9.153634,-8.860624,-4.836302,6.704448,4.511330,0.788327,9.327384,-3.838354,-5.028270],[-1.110387,4.788772,6.338273,-2.429499,-6.881338,7.343408,-9.404942,7.325373,-3.369816,-2.182164,-5.490465,8.022368,-6.843277,6.009586]],[[2.556059,0.380635,-5.617130,4.179292,2.557493,3.670832,-3.036820,8.284628,-6.963150,2.982789,-9.230756,-2.001237,3.051504,-9.249993],[6.399055,-0.968699,-4.735123,-2.641083,-2.484756,-0.999684,3.269059,-2.797082,-6.681101,-0.599161,-9.195583,9.872137,9.378317,-1.745330],[9.666427,6.880146,-0.275001,-8.794899,0.190542,-8.918652,-4.969519,2.509473,-5.174267,2.413777,3.915183,4.122274,0.116657,-3.706221],[2.025166,1.977945,-0.564880,2.553256,7.907902,3.065210,-9.629132,-1.457021,-3.312690,-1.687851,1.629997,0.734694,-3.459821,8.556712],[0.821312,-2.174447,-8.844690,-1.918817,-8.659660,8.922572,9.503150,2.123413,-2.707342,-3.960609,5.479005,-1.853884,-8.198627,-7.356070],[-5.008621,-9.051445,1.393720,-3.683062,-5.703275,-7.084369,-0.661363,-8.290273,-6.189033,9.409992,-2.662297,8.068350,3.847690,-4.728809],[0.414177,-0.328473,-4.225515,-1.609201,7.782645,3.556272,5.670001,6.584139,-6.450975,7.315721,5.566193,2.256294,-8.534752,0.301196],[-7.126183,8.485526,-4.379134,-5.193551,-3.281206,1.194093,2.039462,0.772542,-7.123072,0.586638,0.586283,-5.965506,4.063626,-3.021385],[-7.124354,4.619411,1.050353,3.733842,-9.414158,7.763937,-3.739006,1.610335,2.279773,-3.115467,3.944552,-7.615479,-4.779478,8.811883],[4.356404,5.001474,2.463525,-6.446779,7.264918,5.838866,7.716424,-3.788251,4.364084,-5.634420,-3.339610,-8.844531,-8.224053,-1.088524],[2.084605,-9.503070,9.700671,3.857640,0.504897,-4.056219,9.111311,-5.129206,-0.938134,-7.091539,-2.226835,-7.574310,3.986324,-5.993076]],[[-9.381525,-2.038851,-3.387785,-7.025949,-5.905495,4.859665,8.856694,-7.949994,8.192221,-2.369010,3.219995,2.812046,3.504420,-8.694115],[-6.344757,-2.253300,-1.468875,4.141894,2.635368,-1.344643,2.680705,9.824303,1.200866,6.517247,8.353249,-8.346673,-2.031653,-1.374626],[-2.827845,-5.754218,-2.607156,1.775058,1.321440,2.026019,-4.159081,-0.316312,4.888337,-4.879167,9.909180,6.765753,6.577723,7.260768],[2.420076,1.891334,-9.125316,0.375191,-3.370432,9.732210,9.918759,7.498932,6.995567,0.865435,5.493891,5.754678,9.558792,8.141173],[8.778976,-1.217960,8.768695,-9.151721,6.163539,-4.834917,-7.174082,7.361072,-6.691117,2.206037,-5.724628,5.355273,-0.280012,-0.246505],[0.121127,7.576012,-9.286143,-2.192185,8.674414,7.529755,-7.945500,2.720353,-6.975378,-4.219032,2.638926,-2.112170,-2.680982,9.616185],[-4.311583,-8.116889,-8.223108,-3.676918,6.801429,-2.861635,8.696328,7.118414,5.042908,-9.282315,7.924545,-1.049862,-8.741956,-7.841810],[-7.519871,-0.494859,6.654857,6.632512,-0.404203,-9.738102,-7.931638,-0.655232,-2.151668,8.387428,-5.676732,7.028246,-6.500744,-7.366440],[-5.927344,0.856226,0.238507,-7.894030,-3.079559,-8.983586,4.862245,-0.850204,1.210189,-7.124049,-1.888446,9.938970,6.479748,-9.503431],[-3.063667,6.810992,0.624837,-2.928220,-5.363568,0.250492,-1.809591,5.953614,-9.577759,0.462246,-5.543873,3.019188,7.426726,-0.751138],[-4.614766,-8.232746,5.015610,6.637550,-5.483330,7.685879,-5.062408,2.236130,-2.278071,9.414139,-5.048793,-0.123294,-5.100619,4.229721]],[[-1.283714,-0.519773,-8.997853,-3.109980,-8.947482,-9.133952,0.280782,0.306450,-4.571880,-8.059819,8.356803,3.635276,-1.541734,4.255854],[8.211314,-0.497929,-4.873493,-7.734721,4.782053,-3.185384,3.307438,-6.638728,3.644339,-6.415127,-4.145153,-9.105180,-7.879115,2.306618],[-8.912837,4.080259,2.344684,6.024345,5.189852,-9.348404,-3.254735,-9.757154,8.788400,-2.231027,7.494027,-8.060168,5.516821,4.255113],[-4.343705,-1.965690,6.569497,-4.101039,2.940267,-5.094282,-1.872117,4.611913,-4.485044,-4.097690,-5.397199,-7.214879,2.092135,4.393047],[3.460573,9.832229,4.154761,-9.220279,9.981241,1.501937,9.498610,1.822531,-4.064776,-9.116876,4.532422,-1.051708,-6.873701,8.223949],[3.550267,-5.093725,7.155007,-4.922452,-0.375033,-3.880962,-2.629660,-5.389339,9.486566,3.256021,8.831944,-6.134522,-6.722517,-1.042009],[8.705298,-9.710536,6.710715,-4.022771,-8.731831,5.681565,4.790156,4.495451,-1.521650,0.463392,3.293004,5.962351,1.729081,8.394580],[4.651334,-8.354499,5.012591,6.702867,1.399267,-7.161599,9.887665,-1.945260,5.084678,-9.236663,-0.825288,1.160375,-5.169561,-6.421166],[9.945798,6.309215,3.183810,9.583955,-1.832840,2.175879,-5.186585,-2.939138,-3.763115,8.370611,-2.093105,2.167586,6.650801,-4.345588],[7.923607,4.805995,1.594674,6.594993,-2.619644,1.824162,-8.493138,4.074354,-9.988384,-7.368207,-9.625891,-0.170252,1.581198,9.403176],[6.407934,-4.328605,-8.310066,4.157077,-1.146524,3.702886,5.680108,5.240207,7.149040,8.554684,-7.647284,-2.984380,9.912913,2.008510]],[[-8.943150,3.591687,9.011518,6.680412,-6.840732,1.439280,4.916324,1.679632,3.526200,-3.312330,1.325508,4.119483,7.395998,1.980079],[-4.252238,1.492564,2.389526,-6.350430,-6.040174,6.919522,-4.200152,2.215746,2.858662,2.949883,-9.820440,6.935342,6.827714,1.593051],[3.615070,5.918855,-0.846958,-3.240137,9.905846,-2.796844,-7.034595,-1.285032,-1.605771,6.614102,7.672549,-1.592832,-8.398689,8.846904],[-9.572907,2.423383,7.131382,-3.328684,4.247163,-6.163619,4.687874,6.185869,-1.134530,8.607882,8.229339,-3.338369,8.197943,-0.178705],[-5.243126,1.557778,3.495243,-9.807626,0.014687,-4.528834,-0.839362,0.782641,7.151403,3.420185,5.911520,-4.694162,9.685010,3.033523],[2.202259,5.486072,5.743823,2.804126,1.368158,-7.134310,-0.322922,3.450456,2.123594,-0.208207,5.555677,-6.771816,-7.754816,-3.401112],[5.667090,-7.620849,8.834355,-9.703074,-5.452477,5.763175,-8.325268,-0.738923,-6.282654,5.211178,3.897478,-2.163881,0.252909,9.133505],[6.479513,-1.107051,4.987339,-5.674050,-5.587247,8.786345,-4.045023,-5.175672,-4.650211,4.991022,-9.281453,-4.953991,-5.636812,4.805895],[2.774764,-3.840671,-3.236238,0.037122,1.200070,-0.128069,6.892855,1.960424,0.409336,-6.607300,-5.061992,-6.757104,-2.567541,-8.128651],[-9.385415,-2.915744,-1.982253,-6.502886,5.384661,-9.221737,4.477247,-9.575891,9.643928,-8.027933,1.975583,-1.541326,-1.436475,3.384428],[-2.127285,-7.048100,7.151230,-9.531261,6.608507,-4.909312,4.073676,9.865613,5.537615,1.834317,3.444240,0.139626,-6.555140,2.176554]],[[4.854134,9.187696,-0.287354,-9.705920,-3.575666,-8.042813,9.868590,0.325299,2.826229,-9.520945,-9.259912,5.944420,7.413327,9.292702],[8.471609,2.509815,3.021621,-0.332632,-2.039330,6.472259,6.359169,-0.155268,-3.215642,3.130824,-9.238711,-8.920265,6.709736,0.934836],[6.858474,-1.619427,1.393784,0.066309,-7.753868,-4.850092,-2.587544,-2.530732,4.964145,-2.985078,-6.829371,-9.337801,3.238918,2.812527],[-2.960816,-7.973701,9.296379,-9.254362,-8.268312,1.357776,6.056561,5.813148,7.016475,-7.351969,-6.084956,-8.968976,-0.050822,8.523334],[-8.772686,8.129265,4.151805,-0.473658,-5.230605,9.862095,-4.550801,-2.971283,6.032919,4.267733,1.673965,1.031679,-0.492725,-2.166227],[-0.061942,0.317565,-5.920675,-7.286804,-7.621882,2.641590,6.695710,6.328256,3.043291,-0.192809,6.327796,-6.121839,4.835216,-1.417926],[8.091701,-4.421086,-5.605868,-4.583573,-7.966702,6.163023,2.532156,-5.069386,0.706015,-9.182377,1.880877,9.948332,-1.392122,5.500246],[-2.886736,-7.411915,-8.319429,6.174020,-6.128669,7.397378,-1.425097,1.365427,6.454694,6.226134,4.520559,-9.287844,-1.865765,9.278987],[3.087234,-3.323379,-6.522836,7.227967,3.180098,4.437600,8.292676,6.022050,9.112591,9.816032,-7.419194,-9.484622,3.046174,-5.182800],[-5.132521,-6.657478,-4.329187,2.729590,2.228449,5.185751,-8.839953,-9.656518,1.124500,2.497745,-4.600383,-8.470469,9.229150,-2.811656],[4.548241,-3.528244,-8.762246,5.498251,2.391905,2.890977,4.912960,-2.402826,-1.947224,8.231953,-4.741628,-3.978290,-4.070189,2.325789]],[[9.558271,-7.451123,-6.854011,9.681605,3.763018,5.029730,0.468844,-4.475932,9.764339,-3.722807,9.432508,2.604089,3.962882,5.604149],[-9.857887,1.578476,-5.412923,-2.210241,9.348763,-7.033157,-8.193946,6.252651,-4.852120,5.042100,-2.019931,4.713559,5.121994,3.626368],[8.804904,-0.388000,4.171327,2.260043,4.759568,-4.472288,7.060024,-8.686258,-0.858714,-7.681612,1.574137,-5.717234,8.341907,6.049962],[3.881441,2.867587,8.311879,-1.556176,-7.481277,3.014151,-6.580227,-1.507279,-7.763978,4.709659,-1.842759,7.269124,4.033896,-0.101406],[-2.567483,-0.366429,-7.283017,-0.313427,0.669008,0.050428,-9.877996,-0.208864,-2.412353,9.466587,0.420758,-7.776968,-0.244276,3.101898],[0.669878,-7.906991,2.932384,2.454749,8.239949,-8.800758,8.985339,-8.963278,-2.469454,-9.232351,3.634423,7.670484,-6.140943,-5.008594],[2.183341,6.815738,5.809282,-4.275453,-3.162226,3.869196,0.996308,-3.118169,9.360414,3.259845,5.669743,-2.552971,4.814917,1.490996],[3.025700,-2.509520,8.468401,-0.878274,5.182734,-7.053658,-2.770278,2.470477,9.431422,-7.963696,-5.936018,-7.101907,7.954401,-6.590950],[-4.206701,9.970245,-7.818759,-6.718007,7.888090,-8.867847,-0.760984,-2.660864,-9.417804,-2.345854,4.609754,-9.718903,-9.704595,-3.468987],[-5.619739,-0.197961,-0.596292,-1.833865,5.835934,6.871955,2.868934,-8.534740,-0.396840,0.069090,-8.539857,-1.670834,-6.222929,-7.465932],[0.956939,4.582879,1.362491,-0.613159,0.209218,-5.332526,8.135208,9.214302,-2.368292,-5.071484,-4.441283,1.517185,-1.894292,-0.491504]]], dtype = "float64")#candidate|6913|(16, 11, 14)|const|float64
uop_6914 = relay.atanh(const_6913.astype('float64')) # shape=(16, 11, 14)
func_5182_call = mod.get_global_var('func_5182')
func_5185_call = mutated_mod.get_global_var('func_5185')
const_6917 = relay.const([2.803059,1.037494,6.324673,-8.179216,-2.400625,-4.245631,-2.550255,-2.746723,3.457477,9.104578,2.189447,4.612148,4.450200,5.526484,-7.812371,4.897154,1.308435,-0.746784,5.818610,-5.608765,-9.005717,-1.863219,-7.259747,8.606047,-3.524640,-7.927586,4.203199,-7.030769,1.641000,7.544063,-9.123396,-8.934118,-6.357148,-8.652252,5.413352,5.154094,0.308314,-4.209176,-2.908850,2.507040,-5.424815,-5.360948,6.383747,1.023453,6.743921,-1.720406,6.411619,0.152215,-9.187997,-4.797365,-9.065129,3.186660,1.742748,7.201683,8.284874,-4.542754,0.305413,0.153471,-4.849454,7.124351,-5.020418,6.140864,-2.376756,9.659447,4.485012,-1.588898,7.634872,4.444162,1.124493,2.370223,-0.859610,3.623139,-1.084191,-1.263959,4.640523,-0.799182,-8.181996,9.020975,-4.248686,9.883302,-8.752475,7.483227,2.049267,9.658311,-4.297870,0.612054,-7.085167,-4.678083,0.819221,0.080800,-9.847699,-4.992128,-1.129636,-9.374994,-5.028174,-3.550821,7.824929,1.678834,-2.879392,-0.800878,3.450923,4.264933,-8.903953,-7.432118,7.854699,-9.418584,-1.953813,-5.647839,-2.313028,1.274839,-4.432659,-0.556796,-0.707155,-2.839758,-2.073862,0.275540,-7.869987,3.262241,-4.098941,-0.053928,-3.339634,9.472545,-7.608490,4.415077,-8.021368,7.766227,-8.446770,0.118558,5.724968,9.216435,-5.730866,7.690095,-1.937201,9.511163,1.082767,-9.279619,-7.738242,-5.042034,4.778666,5.934194,-5.536363,-8.830443,-8.299389,9.128786,0.748477,5.065724,7.646527,-6.424427,-3.258334,-7.738101,6.550812,5.351335,9.793003,-6.940124,7.987834,-2.575210,4.991901,-7.066329,-8.529650,2.013203,-3.976805,5.702119,-3.724526,6.809973,9.823426,-6.880597,-7.165624,-0.640266,1.962988,-9.296390,7.589632,-0.180728,8.083442,-1.079834,2.125859,8.609031,1.971979,7.696493,-5.410235,-5.389929,7.834936,8.377069,-8.117121,4.670200,-8.088887,-3.528841,-9.946987,-4.994105,4.354583,-9.606809,1.934351,-9.255277,-7.348565,-1.178715,0.348305,4.143110,9.574777,-0.831774,-1.669321,2.467815,-0.462060,-1.066969,-3.413475,-5.835110,-2.753701,-8.780955,7.985809,-5.657425,4.865112,-4.124179,4.605125,9.888817,-1.411646,-0.435964,8.767588,-1.242980,0.845591,-3.494603,7.666141,7.606234,5.311185,9.512647,-7.198014,2.956060,-1.584374,-6.936047,9.744138,-9.775310,-2.142869,-7.559828,-1.906929,5.452878,-7.470543,-3.936943,-3.962781,2.925079,2.366994,-2.642588,-7.389379,6.901532,-2.810967,-9.907703,4.225863,0.176506,4.869309,7.311176,-7.531408,6.813174,1.824523,6.426122,1.829622,5.834408,4.139377,-4.688793,0.200350,4.953461,-9.018098,5.958638,-7.224902,5.057358,7.693473,-1.302738,0.853564,-7.596313,5.949422,-9.535336,-8.636034,7.271995,-2.859816,9.682469,-4.058613,9.770937,-1.552690,-4.030554,9.145392,-7.768911,8.185669,6.949873,-6.520691,6.038023,9.445172,-9.434466,3.583572,9.341709,4.752895,-7.599904,2.415480,-3.921830,-5.075412,7.538635,-1.873859,-4.276542,-0.569020,-8.437578,0.380567,-1.279770,-6.405661,-6.425081,-4.334094,6.417577,-4.799469,5.234432,4.762416,0.308932,6.577588,9.948716,-1.023111,4.027443,7.880507,6.924117,1.535652,9.479838,-3.228508,8.748021,-1.607106,7.111548,-2.574286,-7.363222,-3.635638,-6.743717,-8.088427,-3.130404,0.064227,2.001431,8.660424,-6.207718,-6.408161,-9.910799,0.028444,-8.669397,-0.270858,8.012458,-5.839095,-7.067825,0.786866,-7.518660,6.863552,8.384521,-0.420250,7.653316,9.337113,-3.468870,-5.427624,9.717514,1.940720,5.941643,3.513296,-7.790451,-3.073142,-0.134463,2.646938,-1.825501,7.718055,-6.147546,-9.090060,-6.359653,5.879177,-5.957035,5.770484,7.999890,2.766412,6.893255,8.820889,-9.581669,-1.810409,-8.258346,-8.859620,-8.640648,-2.651780,0.927945,7.988880,-3.302646,2.027513,-3.242889,-3.418587,5.548880,-9.945094,-3.304454,-1.349184,8.312892,-2.574910,0.696196,-8.399526,-2.110773,-3.601845,-4.637776,7.635035,-5.628265,0.677997,-5.555578,-6.425645,5.708600,-8.632146,5.286457,-9.336018,2.899412,-8.789328,9.114574,4.945891,6.818262,-9.469061,5.341079,-9.378820,-1.701462,-9.763146,-1.679581,-0.202509,7.017340,6.924477,5.882002,2.841064,-6.280078,3.420312,0.093037,-4.831890,-3.622088,-0.093353,-1.962469,7.635027,-6.075603,7.033245,2.414557,-5.086455,-0.155765,2.039531,5.852591,3.181804,-8.667642,-0.338760,8.826087,-3.533769,3.467310,4.902717,4.480633,-7.231221,-8.458842,-0.677606,9.046451,-7.402212,3.102464,4.724061,-8.619649,-6.789745,-4.529386,-8.156766,5.139646,9.193522,0.532202,9.556342,-1.976519,-1.934320,1.478489,-1.840501,3.931185,0.480849,-0.653030,-5.578814,9.872535,3.815880,9.274330,4.868860,-8.774901,6.636326,7.739480,-4.325251,-5.763732,-6.980208,-9.561308,-5.811310,1.606371,-1.173016,-6.636274,-1.568640,0.453355,1.784073,-7.946536,-0.770465,-1.572050,-6.265669,-0.391956,1.185090,-6.055260,-1.107426,-9.279220,-8.401197,-5.168350,9.163342,3.081880,-6.346601,3.188153,2.181619,-0.404709,-8.597407,6.978398,-5.396483,7.266903,-9.325354,5.958545,-9.190866,9.136384,8.869088,0.777988,7.736097,8.190744,-7.155441,6.568783,-4.517062,5.784867,-0.820049,7.657131,-2.413226,-9.112842,-3.375226,1.600110,7.557578,-7.974569,7.079639,6.311641,-7.096812,-2.859657,7.375104,0.085777,-3.428354,-6.779760,7.373563,3.936812,3.844447,5.234419,-2.201409,-3.235349,5.814926,-7.770184,7.309917,9.660797,-9.681544,-0.009094,-4.914795,2.251685,-8.882894,3.490595,-5.750630,2.187644,1.137555,2.577999,9.535347,3.861797,-1.186601,6.927637,-3.710036,-8.199589,3.141136,-1.884760,-1.442539,-0.993081,-1.410683,-0.180287,-4.522658,-7.217750,-2.837330,0.400194,6.944344,3.487900,8.946778,9.768499,4.946203,-4.232565,-1.160173,-1.107007,2.445204,3.553672,7.140735,-1.297604,1.611661,0.122550,-0.962119,-2.652834,7.557248,-5.613205,-3.768937,-5.429201,9.970763,-2.272764,-0.234251,-3.765230,5.986268,4.596010,3.454767,5.983706,-8.620049,5.444044,5.997977,-5.674770,6.264729,6.048369,5.405803,1.514944,6.012256,-6.934312,5.712605,7.905318,5.398090,1.200975,-4.061334,4.019639,7.106227,2.541142,-9.979123,4.415429,-3.345004,-1.993145,8.616605,-7.290447,2.123954,-8.363790,2.645100,-0.029377,-5.321966,-7.332892,-6.829652,2.022138,-6.201101,-4.319425,-5.500727,-9.906848,7.797956,-6.718477,-8.939910,4.696158,-5.436402,-0.930139,7.215155,-5.595166,-4.413891,-4.255451,-8.310695,-0.097115,-4.562225,-3.933587,4.486132,-3.831780,3.633628,4.773379,6.865017,6.356146,-6.525938,-8.572143,-1.505506,8.876263,9.512485,5.858359,2.220138,-1.378481,3.150773,-3.365735,7.203214,8.031922,-9.746151,-5.330060,0.809983,9.613673,-0.435010,3.295136,-8.460217,7.602927,-4.102681,3.933812,6.385442,0.331403,-9.701533,3.953324,-8.407988,-7.868952,3.743513,7.358452,6.518057,-4.816039,-7.425730,-8.361615,-3.393971,-9.393973,8.378939,-7.542411,9.063342,1.146372,0.930684,3.688564,1.996726,-6.162561,-1.004794,8.479039,-6.741472,4.549004,5.571575,4.385775,-3.556615,-0.624190,-2.541481,-5.728414,-5.656138,9.904813,-9.771149,-5.156909,6.470010,-2.480270,-6.128119,0.896099,6.322167,9.080459,-0.897407,-0.416027,-8.924830,-6.289434,5.581775,-9.039042,-3.872073,8.815414,-0.071220,-9.497102,0.462569,5.494152,-9.948460,-2.006372,-4.250228,-4.607599,5.018452,0.358124,3.077262,-7.447543,-0.902020,2.227206,-3.049240,6.785210,-5.942357,-9.235534,-4.707836,5.044275,-4.333363,-5.444528,5.508704,-9.640185,4.291820,-5.727146,9.816197,8.287520,3.189207,7.634288,4.407757,-1.826223,-2.191688,4.870949,-4.886698,-8.605636,2.833000,6.346974,9.783752,8.145868,5.256773,-6.348230,-4.423582,-1.730870,-7.227930,1.129854,-8.270436,6.077695,1.815322,7.340804,0.710941,-2.687720,-2.884818,0.199897,6.566957,-1.116356,-9.655088,-5.535865,-0.486126,-3.686920,-1.089878,7.755074,8.993373,1.868507,6.389454,-4.899497,-8.067688,9.203682,6.453400,2.318278,3.872478,2.020297,-4.820710,-1.381398,3.821483,6.772600,4.541626,-8.617856,5.127747,2.903790,3.530711,7.641598,-7.154398,-4.835157,9.002031,8.189335,-5.395600,-6.140122,-7.309529,0.958113,9.410766,5.465077,8.484027,1.768088,9.717337,-1.807334,-4.098190,1.149495,-1.871495,-5.189401,5.162120,9.808265,3.850668,-3.324422,-5.391182,8.850751,-0.649074,-8.702076,-9.206527,-6.446943,-7.819456,-1.428294,-3.296719,-5.673735,-8.514934,-9.200602,-2.540198,2.209338,6.821177,1.974046,0.208180,7.281504,7.403024,-9.187587,1.964526,1.776984,5.393380,-7.710708,7.679332,-7.542804,-9.452379,1.192220,-7.703122,-1.508524,-3.892397,-3.002478,-5.710037,0.076138,5.956259,4.408299,-0.223539,5.607614,4.952199,2.663857,-1.845027,-6.551632,-9.476778,8.970558,-1.410820,-6.511234,1.291544,-3.601686,-2.014324,0.042367,0.771892,-8.498617,4.588474,8.115551,-3.255873,-2.406146,4.590677,1.574477,-7.589639,-5.115749,-7.050426,-9.239574,7.008822,0.848850,-5.296607,-5.021422,7.222634,-1.929993,-8.667308,1.921660,-8.985372,1.833625,-2.376261,-7.602686,9.641559,8.402956,7.996847,8.233737,5.224892,6.719425,2.063430,2.983923,-7.805672,8.319086,-1.584224,2.392559,-3.381847,-2.722073,6.115071,-2.157444,0.232444,-8.529563,3.726786,-6.517243,-4.434935,-4.164895,6.885365,9.268831,3.939255,-5.024261,2.437133,2.124874,-2.323411,2.793240,-4.725069,-1.930502,0.295498,-5.640820,-3.337058,3.068526,-3.011311,-3.842727,-2.654162,-1.736290,-5.540643,1.315441,-7.259873,-4.473657,-9.178485,3.885549,0.010227,-2.542332,-6.655699,3.218965,6.725267,-4.459793,-6.343639,8.908573,-2.475694,7.163820,-0.004259,-7.240994,9.341068,7.740968,-3.158797,-5.262226,-6.212262,2.644345,5.797932,0.731756,4.727932,3.928026,-0.793231,-8.519739,-2.259831,-8.462603,-5.959210,1.519350,7.582169,0.117706,2.070293,3.381228,7.396232,9.241013,2.027985,1.247402,-9.161759,-5.627169,-8.566907,4.566404,-5.045960,4.677989,-9.505660,-0.397101,-7.356409,-5.287383,2.165033,2.547484,-2.710110,-5.839353,-5.570835,-2.291008,-5.258215,9.917027,-9.677872,1.628185,-5.012787,8.576968,9.602146,-9.486399,-0.009995,-0.240656,-2.981690,-7.446008,-3.611229,-8.283674,-9.688607,6.376700,-6.919368,4.571982,4.936098,1.603571,-6.206262,-2.644715,8.402989,6.424457,6.306145,2.133833,5.050900,-6.241614,-2.849099,-5.351607,-1.938535,7.607917,2.506273,0.058011,3.246315,-1.478241,4.537013,-3.712978,-3.493616,-1.922734,6.392915,5.048633,2.564888,-1.404855,3.724548,5.977102,-6.443395,-9.652318,4.620017,-4.713182,-7.346187,-0.903636,5.200149,-8.448906,-9.994540,-6.054704,5.618839,2.010441,7.019451,-1.056168,-1.958147,-6.057342,1.070178,-3.062849,-2.694758,3.297639,-0.361105,4.258277,-2.380812,1.930896,-2.488602,-8.940168,9.194306,2.845156,3.782733,7.340216,3.340456,-7.217434,-7.894662,6.030583,3.497126,-7.799354,6.314307,-6.318354,4.614267,-4.203322,1.373697,0.728074,-3.691447,6.506424,5.036460,-5.167332,5.002747,8.273042,4.750071,-8.754642,2.394704,-8.906967,-8.210813,1.172764,-6.725118,-2.462243,-6.974101,7.101927,-5.003546,8.281579,5.267218,-6.690141,-1.421515,0.804251,-2.244489,2.028480,-8.539819,-7.454617,-9.370214,-2.594002,-4.840996,-1.731899,0.026750,2.367862,-4.571048,1.423073,-5.956335,-8.225327,7.106382,2.462338,-1.794109,2.286266,-5.375668,1.032007,7.228868,-0.115577,-1.924336,8.005103,-0.145493,2.749565,9.301127,-5.114550,-1.125865,-7.098290,-2.132098,-9.620035,-8.221770,6.146179,9.369474,6.167082,0.795287,-6.888235,-0.770415,6.752501,5.664236,-4.652082,2.498195,-2.218648,3.723913,7.591667,-3.909896,-8.873572,1.770468,-7.069715,5.200954,-2.180047,2.154614,-9.994171,-2.788735,-0.365530,3.134182,-9.851941,3.921207,-7.992902,0.941144,2.461883,1.387630,2.151347,8.748233,-1.865258,2.597918,2.937806,9.050552,4.137733,8.009952,6.203620,-4.639178,2.000841,4.809478,-9.102505,9.083088,-5.321571,-6.844210,-4.915037,7.780022,-5.949603,8.318583,0.368584,8.881619,-0.617337,-9.021854,0.903879,9.688339,3.655823,7.897632,8.041253,2.110511,3.801610,2.984335,7.829611,-1.683690,-1.659942,-8.239370,0.267675,-4.194029,-1.600087,7.317979,7.207547,7.323309,7.154851,-9.931034,4.880290,3.172754,5.957823,-3.777778,8.985553,-3.589403,-1.580318,-9.998316,1.818559,0.485561,5.267091,4.369617,0.968273,9.342306,4.924325,-7.570348,8.210442,-4.316832,-7.395847,-9.504386,4.423215,8.357590,7.197353,6.211088,-4.881448,-4.700728,-3.793845,-1.774043,-5.680911,-2.511805,-0.846293,5.222208,-4.417368,-4.017331,-4.158445,4.216891,-9.149623,-8.996098,-7.060669,-9.344720,-1.525294,-2.868628,-4.388783,7.818313,0.758313,5.661046,-8.244394,5.746029,-8.939598,7.045425,-9.830119,-8.026841,-8.376548,-8.715462,7.547620,4.518458,-3.512502,-7.258320,9.142728,0.450397,4.296692,-3.639686,8.193443,1.962988,2.953769,5.231052,7.488745,-6.312745,-6.168718,-8.351595,6.607044,6.200989,8.202860,1.255881,0.605706,8.058646,7.049359,-1.336334,-9.358438,-8.512664,6.252080,6.625450,7.078748,-2.938071,3.195290,9.883053,-5.324214,-9.151085,-7.177330,-6.389762,-2.941458,7.009494,2.505356,3.339136,1.715307,-7.664771,7.984036,1.846102,8.533075,-4.265706,-8.529854,-3.618444,-6.887663,-6.861500,-0.628756,0.913878,5.356151,-8.425309,-3.945262,-9.576028,1.364972,-2.972967,-1.118905,7.623262,8.282060,-6.356844,-5.742276,4.699611,9.134569,3.987496,-9.465273,5.412273,3.746641,2.663301,5.858560,5.785160,-4.292331,5.752022,4.731991,-5.398363,-9.545146,-5.135938,4.603987,7.303520,-9.972354,-1.706173,6.513127,-1.970255,2.011616,1.770360,6.385203,3.876676,-3.139274,-1.773255,-9.947351,6.295218,-9.711462,2.054594,5.927732,-9.590260,6.479077,-8.035789,-4.937285,-1.341179,-3.476427,-6.530150,-1.088828,2.851473,-6.267488,6.795027,7.782154,9.322476,-8.140644,3.370283,-8.201147,3.736998,0.188154,-7.942575,-5.398485,1.865980,-2.275562,-9.177400,-5.102986,-6.018101,-2.375753,2.283475,-4.770438,6.612142,1.356363,-9.181969,-9.280915,1.862787,4.493611,-8.170548,-5.837069,0.613672,0.419698,-9.527615,1.953438,2.778700,-6.602913,9.771769,8.065947,8.186684,-4.268593,-8.391543,-7.164938,-0.800536,-0.124281,8.315696,-3.661915,6.062866,9.889076,2.281090,-6.643022,-2.425753,3.533279,3.495141,-1.270726,7.897706,-2.934372,0.795152,-4.120918,4.022130,-4.793267,0.608724,3.092955,3.788963,-9.590800,1.812994,9.594870,3.086954,-4.791391,0.689232,-7.877482,6.362474,6.841713,0.347340,-4.247299,-8.268875,4.231787,6.167071,-9.089832,5.112283,-7.116655,-5.562880,-0.660877,-8.235252,-8.003007,8.159157,8.686067,-2.161044,-7.601905,-0.624279,-9.578158,3.539931,-2.046289,-2.975168,2.675555,-3.558975,-0.500950,0.403608,-2.808077,3.374373,-1.144525,2.842009,5.018405,-8.095735,2.151033,-2.426883,4.299564,-6.384430,0.511841,-4.458175,-4.872078,-8.313083,6.720751,-4.020460,3.758774,2.167460,-2.313756,9.407893,-1.709789,2.211235,-2.131122,1.589036,-5.996150,-6.088473,-6.005691,-4.275792,0.141282,5.973201,3.896242,-0.925588,-0.566705,-7.919995,8.319002,-4.155818,8.230259,1.051324,-1.983799,7.747208,-7.582578,-3.706681,-4.335290,-1.664200,8.114784,6.927557,8.003009,0.688177,8.201818,-0.835192,-9.116346,-2.292749,3.547303,3.657760,-5.102398,-9.843701,-7.367480,7.034543,7.478144,-3.342728,2.008872,6.139582,-2.983958,-1.596354,-4.142929,-2.030245,-8.664042,-2.355256,-4.769444,4.287154,-9.351982,-3.705949,-6.612952,-7.693336,5.683525,-2.774198,-5.921885,7.864329,-3.734647,-9.442992,-2.103585,8.547730,5.476357,-0.237811,-7.088931,-9.528095,0.706263,5.924282,-9.610010,-0.130352,2.632602,-4.561155,-8.788865,-0.272983,-7.130515,-4.756152,5.496103,3.732114,1.766901,-2.746152,1.296244,5.396389,2.744570,-0.682988,-5.865716,7.895552,3.846265,4.345369,5.503174,-2.868253,-3.308719,6.618491,1.585098,-8.146356,-4.772298,-2.940125,2.341570,4.131207,-1.818285,-0.849691,-4.370405,-4.923240,5.097313,1.467453,6.264023,-9.424071,-7.121877,7.660341,-5.088147,5.793976,5.195037,-1.380863,7.816107,1.847147,3.435078,-5.423166,-6.371398,0.822397,-6.682706,-6.234162,6.525153,4.657730,-4.625128,2.165491,-1.260296,-5.699833,-3.613474,-7.727302,-2.985347,6.671215,1.761686,5.889864,9.429421,5.425952,1.159149,2.029987,0.329788,2.703106,-8.731628,-2.899698,9.784149,-4.427178,-9.464448,5.466094,-7.376626,-3.196518,-6.616581,8.554169,1.162792,7.398523,7.021603,8.861043,4.501720,-3.799850,5.665843,-6.179289,6.858450,-3.156219,2.512572,-3.791527,-9.650839,1.170720,-9.745526,-9.752040,6.605135,9.153378,8.727300,3.099578,8.032224,-9.786521,2.088490,1.453069,1.181313,-6.779385,9.485617,-0.285937,0.300119,-0.706963,9.410764,8.049027,-2.615498,1.714419,3.118181,-3.037038,-0.055388,7.218152,9.602659,5.673781,-5.850373,7.248426,-0.680024,-8.964427,5.447032,-1.253669,5.440755,0.500236,-6.584921,3.818869,-2.985100,-2.709845,-2.207065,-8.363683,-9.980397,-9.415215,5.490010,-4.547047,-2.004605,7.222552,7.926988,-4.282613,-6.731406,-8.815182,-1.153165,-1.491214,4.606907,7.111559,7.957642,7.888155,9.475464,-5.206860,6.507768,6.361751,3.232974,6.874143,-0.520369,-6.191562,8.921640,2.828748,-9.956906,-6.170179,-6.590388,-4.306966,2.239057,1.610752,5.521756,3.686073,-3.413325,-6.367495,-1.926076,-4.344390,0.437549,3.778077,2.281374,-4.267176,-2.151799,3.771385,3.783324,-9.228024,8.052300,5.302594,-1.898220,6.445857,2.212065,-6.720374,9.489715,-0.723053,0.665429,6.780499,-3.486392,1.477061,3.774386,9.261399,-6.737080,4.548576,0.221417,-8.472563,-2.077054,-9.763148,-5.763322,9.865889,7.938131,-9.741133,0.007715,3.689546,-9.347898,-0.483788,4.268191,-8.591880,-4.810935,8.276272,-4.018506,2.098367,8.034614,8.525108,-7.627913,5.343201,-6.170565,5.429013,-9.780242,-6.642937,3.345819,-6.323746,-6.508611,-2.537490,-6.558871,0.157691,7.432247,1.391676,-4.794487,-5.855026,9.253093,2.976868,-0.295197,6.644951,2.843521,0.151962,4.085437,-4.490051,-5.805715,-0.967618,-7.413484,9.671367,-7.204079,0.673865,9.049297,8.653427,3.151036,6.352409,0.762216,-6.212908,-5.659871,1.442765,3.707186,8.151111,-3.879996,4.958997,5.877693,6.239888,3.960869,0.695604,-6.147290,-0.540756,3.804444,9.086780], dtype = "float64")#candidate|6917|(1815,)|const|float64
call_6916 = relay.TupleGetItem(func_5182_call(relay.reshape(const_6917.astype('float64'), [11, 11, 15])), 0)
call_6918 = relay.TupleGetItem(func_5185_call(relay.reshape(const_6917.astype('float64'), [11, 11, 15])), 0)
output = relay.Tuple([uop_6914,call_6916,const_6917,])
output2 = relay.Tuple([uop_6914,call_6918,const_6917,])
func_6922 = relay.Function([], output)
mod['func_6922'] = func_6922
mod = relay.transform.InferType()(mod)
output = func_6922()
func_6923 = relay.Function([], output)
mutated_mod['func_6923'] = func_6923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6695_call = mod.get_global_var('func_6695')
func_6696_call = mutated_mod.get_global_var('func_6696')
call_6924 = relay.TupleGetItem(func_6695_call(), 0)
call_6925 = relay.TupleGetItem(func_6696_call(), 0)
var_6935 = relay.var("var_6935", dtype = "float32", shape = (3, 11, 2))#candidate|6935|(3, 11, 2)|var|float32
bop_6936 = relay.not_equal(call_6924.astype('bool'), relay.reshape(var_6935.astype('bool'), relay.shape_of(call_6924))) # shape=(3, 11, 2)
bop_6939 = relay.not_equal(call_6925.astype('bool'), relay.reshape(var_6935.astype('bool'), relay.shape_of(call_6925))) # shape=(3, 11, 2)
output = relay.Tuple([bop_6936,])
output2 = relay.Tuple([bop_6939,])
func_6946 = relay.Function([var_6935,], output)
mod['func_6946'] = func_6946
mod = relay.transform.InferType()(mod)
var_6947 = relay.var("var_6947", dtype = "float32", shape = (3, 11, 2))#candidate|6947|(3, 11, 2)|var|float32
output = func_6946(var_6947)
func_6948 = relay.Function([var_6947], output)
mutated_mod['func_6948'] = func_6948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6695_call = mod.get_global_var('func_6695')
func_6696_call = mutated_mod.get_global_var('func_6696')
call_6958 = relay.TupleGetItem(func_6695_call(), 0)
call_6959 = relay.TupleGetItem(func_6696_call(), 0)
func_6872_call = mod.get_global_var('func_6872')
func_6874_call = mutated_mod.get_global_var('func_6874')
var_6966 = relay.var("var_6966", dtype = "float32", shape = (780,))#candidate|6966|(780,)|var|float32
call_6965 = relay.TupleGetItem(func_6872_call(relay.reshape(var_6966.astype('float32'), [780,])), 0)
call_6967 = relay.TupleGetItem(func_6874_call(relay.reshape(var_6966.astype('float32'), [780,])), 0)
func_322_call = mod.get_global_var('func_322')
func_325_call = mutated_mod.get_global_var('func_325')
const_6970 = relay.const([-7,5,-1,-9,9,-1,10,4,-9,-1,-3,-5,6,-4,-3,8,-5,4,-6,-10,-8,3,-10,-7,9,9,9,-8,9,6,2,-1,-1,-2,9,-1,4,5,3,4,-10,-4,8,-3,-4,10,3,3,-8,10,-1,-4,-4,-3,-1,-1,-2,9,6,1,-9,8,-2,-9,-7,8,9,-7,3,2,-6,4,-7,-2,-4,-5,-1,8,-3,4,3,2,-7,7,-6,5,-3,2,3,4,-6,-2,-1,2,7,-8,1,-4,-6,8,1,5,-4,5,2,7,-8,5,-9,-5,-5,9,-2,4,-4,-1,-8,1,5,1,5,5,7,3,1,6,-3,-3,6,3,2,8,-2,3,-5,7,2,-5,6,-9,-8,-2,-8,3,4,7,-2,5,-4,-1,3,-8,2,6,-1,-4,1,-9,-10,-4,-10,10,6,4,-4,-8,7,-3,-1,-6,7,-3,-3,-7,7,-9,2,9,-3,-9,-1,7,3,4,1,6,9,4,2,-7,3,-7,5,5,10,6,-1,7,3,7,3,-3,5,-6,-1,7,1,10,-10,4,1,1,-3,5,10,-1,7,5,3,10,-6,-5,3,-3,-2,-4,6,-2,-2,8,-3,6,3,4,5,-8,-3,8,-10,-10,5,-3,7,-2,6,-2,-9,9,-10,-9,-6,-3,-4,4,1,6,6,-9,-9,-2,2,-4,-2,4,5,-4,4,8,10,2,4,7,1,2,8,-5,-8,3,1,2,3,-4,5,5,-6,7,4,9,-4,5,7,-2,10,-6,3,6,-6,-2,-6,6,-3,1,9,-5,5,4,-2,8,4,-3,-4,4,1,10,-5,9,-1,7,2,-2,-4,8,7,-9,2,9,-3,7,-10,-3,-3,-5,5,-4,-8,4,7,9,8,2,-10,-9,3,-6,2,10,-4,-2,8,3,-6,-7,9,-4,4,10,-8,-6,4,6,3,-5,-2,5,-5,-6,-5,6,9,-2,8,8,10,9,-5,-10,-10,7,-4,-1,-1,1,-2,-2,7,-5,-8,2,-6,-10,5,-1,-6,8,3,10,8,1,-8,-2,-1,-1,9,-6,4,8,-7,4,-9,5,2,7,-9,-2,3,6,-1,4,-10,-5,-6,6,3,-9,4,6,1,8,2,-1,-1,3,-3,2,-5,10,1,5,5,6,-1,-5,-6,4,-2,4,-9,-5,-2,-6,5,8,-1,10,10,5,-10,4,3,3,3,1,4,6,5,5,-9,8,10,8,-5,9,-3,-1,-1,4,-4,9,10,-8,-1,-7,-7,-2,2,-7,1,4,9,10,2,7,8,-5,-3,-3,7,-5,-4,1,7,5,-6,-1,4,6,-5,1,-10,2,-1,-8,-7,-3,1,7,4,5,-10,-2,6,-8,2,6,8,-7,-3,5,9,-2,-2,10,10,-3,-10,3,-6,8,-2,1,-2,-9,3,-6,-2,7,-7,9,10,8,-8,7,3,1,2,7,8,1,-10,8,-7,-5,1,2,5,-1,-2,-6,-8,4,8,-5,7,-2,5,6,-4,-6,4,-4,9,-1,-8,10,5,7,3,-10,8,-7,1,-4,-4,-7,10,9,-1,-2,9,-4,-4,-6,2,9,-7,4,-10,2,-1,-2,2,-10,-2,-1,-4,5,-7,7,10,-3,10,6,8,-4,7,-1,9,-2,-4,6,-2,-6,-4,10,8,-1,-9,-10,5,7,2,-10,9,-6,9,-3,-2,7,1,-10,-9,7,5,8,-1,-1,2,6,5,6,-1,-4,7,9,-9,5,9,9,-9,-6,-1,-5,-8,6,-2,-9,1,-8,-7,6,-5,5,5,7,-10,-6,10,3,2,-5,-2,-1,-10,-1,7,2,-10,-5,-10,9,-7,-8,-6,-7,10,5,6,5,7,4,5,6,-2,10,-7,-3,-4,3,4,10,-2,6,-3,6,8,3,-6,1,-2,-2,-10,5,-6,3,6,3,-8,-6,9,8,1,-5,10,7,-6,3,3,-7,-4,-8,4,10,8,1,-7,-9,10,-7,9,-6,-4,9,7,-6,-8,5,4,2,-9,-3,1,9,5,6,2,9,1,3,7,2,2,7,-1,1,-1,-8,-6,8,7,-7,7,4,5,-7,7,-8,-5,6,-6,-7,9,3,-4,-9,6,1,4,-1,-3,3,-10,-8,8,2,-10,10,4,-7,4,-1,-3,-4,-6,-8,-7,-2,4,1,-3,-5,-10,2,-8,-2,6,5,-4,10,5,-2,1,-7,-3,4,-1,-10,-3,5,-3,6,-2,3,-9,7,-3,6,4,-6,4,-4,-10,-6,-9,6,9,5,4,-9,-3,9,-7,7,-2,10,-4,1,-1,6,-1,3,-4,-3,-8,-3,9,6,-9,-9,5,-7,6,-10,-6,-8,-9,-8,3,3,-2,-2,-6,-8,1,-6,-9,-3,10,3,-10,-4,3,-3,-3,-6,1,-5,8,4,1,4,-2,4,-10,9,-7,8,4,6,8,-10,2,7,-1,9,-10,1,-10,3,3,2,2,-1,3,-4,9,-9,-1,1,5,3,3,-7,-10,-6,10,-4,8,-1,-1,2,-10,1,5,-5,-3,8,-4,-10,-5,9,4,10,-9,3,-7,-9,5,-2,3,-1,-8,2,-3,-8,1,-6,9,9,10,-7,8,-7,8,-3,7,-5,2,8,-2,-8,2,-9,3,-10,-9,-9,4,10,-5,1,7,-10,-5,-8,5,-1,-1,9,-6,6,-7,-2,3,3,5,2,1,-10,-10,-5,-4,1,5,-9,10,-8,-10,-2,-4,-1,-10,-10,-4,-7,-1,-7,-9,10,10,-6,-5,-9,-9,-6,-5,-4,9,-6,-6,-7,-7,2,5,-9,3,5,-4,-1,-5,-5,-5,5,-3,-6,4,-6,10,-7,1,-9,-3,-10,-9,9,-7,4,3,5,10,7,-7,-7,2,-1,1,-5,4,-3,-6,7,-7,7,-2,-10,-6,-8,-9,-9,2,3,-1,8,-6,8,-3,7,-10,2,7,-4,-10,-5,1,1,5,7,-2,1,5,-2,-8,10,5,10,5,-4,-10,3,4,-5,8,5,6,-2,7,1,2,3,-5,-9,9,-5,-4,-10,-4,7,8,4,8,-7,9,-4,9,-8,2,-5,1,-2,10,-3,-9,-4,2,1,5,7,-5,-5,-10,-1,8,-5,-5,4,-9,8,5,6,-4,-7,4,3,9,-4,-8,-1,-10,-5,-3,10,6,-1,4,10,4,-6,-5,6,4,-1,6,9,10,10,-3,-7,-10,1,8,1,1,8,4,-8,-5,-3,4,-6,-5,8,-7,-8,5,-1,3,3,-9,9,-7,6,-9,5,-8,-6,7,3,-10,1,2,-6,-7,-8,10,-2,6,10,-6,7,-6,-6,-8,5,10,3,1,7,-6,4,4,-4,-5,-6,-9,-2,-7,-8,-9,-4,2,-3,5,-10,-4,-9,-2,9,-9,-6,-7,5,-1,10,5,-1,3,9,1,-1,6,5,4,5,6,-2,-2,-8,10,-2,-4,-2,-4,-5,2,4,-7,-4,-1,-6,10,2,5,-4,-8,9,-9,8,-2,2,10,-2,3,10,6,-2,4,-10,-4,3,3,3,-1,-7,6,10,7,5,-9,5,10,2,3,-2,-6,-10,-5,1,4,2,9,-7,4,-6,6,-6,1,10,-2,3,-7,5,6,9,-3,-3,3,-9,-10,9,10,-2,-7,-7,3,5,4,2,-5,1,4,-4,-2,5,10,9,1,-1,2,-7,9,-6,1,3,1,-8,8,1,5,-5,1,-6,-3,-3,4,-1,2,-6,-5,3,-10,8,-2,-1,6,3,8,-2,-6,-6,-6,5,-2,5,7,1,8,7,-10,-9,2,8,1,1,-6,10,-3,2,-4,-3,4,10,5,1,8,4,4,-10,-1,-4,9,10,1,-7,6,7,2,-1,-5,-2,4,2,7,5,-6,-6,-5,7,6,-10,-2,4,4,-2,-10,3,2,4,-9,1,7,10,-4,7,-9,-4,-6,6,6,1,4,-3,-9,-8,-5,-6,6,6,3,10,2,4,6,8,-9,9,-2,10,9,-10,6,-7,-1,4,8,-7,-2,10,2,10,-8,-3,-3,-2,10,9,7,2,-10,-4,-2,1,-4,2,1,-5,4,1,-2,2,-4,-2,6,1,-10,-4,-5,-8,8,-3,3,9,-10,5,-3,6,7,-10,-1,10,-7,-6,9,-1,6,-7,-4,6,-9,7,-9,1,8,10,-4,3,-5,4,-6,3,9,-9,-8,-8,-6,-1,6,1,-5,5,1,3,-10,-10,-1,6,-4,-4,2,1,5,-2,-4,-6,4,-2,-3,9,-3,-10,3,-6,-3,-9,-10,-2,2,7,7,-7,-7,5,6,-3,-4,-3,1,4,-10,10,3,5,7,1,5,6,9,-4,-9,3,-2,-2,6,10,1,5,3,1,-2,-6,2,-3,-5,-5,-3,-8,3,-9,-8,-6,-8,-4,1,-3,-10,1,4,3,10,6,6,-8,5,-9,-4,-1,6,-5,3,-1,8,-6,-8,2,9,-9,3,6,-5,-1,2,3,-9,4,-6,-6,-6,7,-1,2,-8,-7,-10,-8,-7,-6,-1,6,7,2,4,-10,-10,6,7,-3,9,-7,-10,4,4,-6,-10,4,2,-3,-6,9,-1,7,-3,4,-10,-10,7,-10,5,5,8,-1,9,-9,8,-1,2,-6,8,-6,-2,-1,-2,10,-6,-1,8,7,7,-10,-3,-1,-9,-2,8,7,6,-8,6,-4,-5,-9,8,-8,-1,9,1,2,8,9,4,5,-4,8,3,2,-8,10,-6,-10,-9,2,-10,4,-8,3,10,2,3,4,2,3,-7,-8,1,10,9,-4,6,-9,2,4,10,-6,6,6,-5,9,-1,-7,-5,4,10,-4,-7,-1,-5,-1,-1,-7,-6,-4,-3,5,10,-8,-10,10,2,6,-9,8,-2,-10,-5,-1,-9,2,-7,-5,8,1,-6,7,7,7,2,1,-4,8,-7,10,3,-7,6,5,-5,-1,-9,9,4,3,3,10,6,-7,-7,6,-7,-10,7,9,4,-3,10,9,1,-8,8,10,-5,7,-3,4,6,-7,9,-4,-7,6,-10,1,-8,6,6,2,-4,-5,-1,-7,3,9,9,5,-2,-3,-7,-6,3,1,-7,-3,1,7,9,9,7,5,3,4,-2,-10,3,-2,-7,8,-7,4,-10,-9,5,10,6,-2,5,6,4,4,9,6,2,-9,-4,8,4,-3,-7,-2,8,4,9,9,-4,-3,-1,-1,2,4,3,-1,1,-7,-7,-1,-5,8,-5,-9,2,-3,2,7,-4,-3,-5,5,10,-2,2,-2,10,-3,7,-3,-6,3,8,6,-1,8,-3,9,6,-2,9,-9,6,-4,-6,1,3,1,-3,5,6,-7,-10,-4,-2,-7,10,9,-8,8,-10,-5,2,8,5,-9,-9,-9,5,-5,10,7,10,6,9,-1,3,-3,1,2,7,6,10,-6,1,-3,5,-10,5,2,-10,-2,6,7,7,5,3,-1,-9,9,8,2,3,8,-10,10,3,10,-7,1,8,-9,9,7,7,-9,-9,8,-5,-10,9,2,1,-3,10,-2,10,-3,-1,7], dtype = "uint64")#candidate|6970|(2100,)|const|uint64
call_6969 = func_322_call(relay.reshape(const_6970.astype('uint64'), [14, 10, 15]))
call_6971 = func_322_call(relay.reshape(const_6970.astype('uint64'), [14, 10, 15]))
output = relay.Tuple([call_6958,call_6965,var_6966,call_6969,const_6970,])
output2 = relay.Tuple([call_6959,call_6967,var_6966,call_6971,const_6970,])
func_6974 = relay.Function([var_6966,], output)
mod['func_6974'] = func_6974
mod = relay.transform.InferType()(mod)
var_6975 = relay.var("var_6975", dtype = "float32", shape = (780,))#candidate|6975|(780,)|var|float32
output = func_6974(var_6975)
func_6976 = relay.Function([var_6975], output)
mutated_mod['func_6976'] = func_6976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6922_call = mod.get_global_var('func_6922')
func_6923_call = mutated_mod.get_global_var('func_6923')
call_6992 = relay.TupleGetItem(func_6922_call(), 2)
call_6993 = relay.TupleGetItem(func_6923_call(), 2)
uop_6994 = relay.cos(call_6992.astype('float32')) # shape=(1815,)
uop_6996 = relay.cos(call_6993.astype('float32')) # shape=(1815,)
func_6131_call = mod.get_global_var('func_6131')
func_6140_call = mutated_mod.get_global_var('func_6140')
const_6998 = relay.const([True,True,True,False,True,True,True,True,True,True,True,True,True,True,False,False,True,False,True,True,True,False,False,False,True,False,True,False,True,True,True,False,False,True,True,False,False,False,True,True,False,True,False,True,False,True,True,True,True,False,False,False,False,True,True,False,True,False,False,True,False,False,True,False,True,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,False,True,True,False,False,False,False,True,True,True,False,True,True,False,True,False,False,False,True,True,False,True,False,True,False,False,False,False,False,False,True,False,True,True,False,True,True,True,True,False,False,True,True,True,True,True,True,False,True,False,True,True,True,False,False,False,False,False,False,False,False,False,False,False,True,True,True,False,False,False,True,False,False,False,True,True,True,False,True,False,False,True,True,True,True,True,True,True,True,False,False,False,False,False,False,True,True,True,True,True,False,False,True,False,True,False,True,False,False,True,True,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,False,False,True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,True,True,True,False,True,False,True,True,False,True,False,True,False,False,False,True,True,False,True,False,False,False,True,False,False,True,False,True,True,True,False,False,False,True,True,False,True,False,True,True,True,True,True,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,False,False,False,False,False,True,True,True,True,False,True,False,False,True,True,True,True,True,False,False,True,True,False,False,False,False,True,False,True,False,True,True,False,False], dtype = "bool")#candidate|6998|(315,)|const|bool
var_6999 = relay.var("var_6999", dtype = "float32", shape = (390, 2))#candidate|6999|(390, 2)|var|float32
const_7000 = relay.const([-8.730045,4.849331,5.483992,-6.132148,-7.576831,-5.530269,3.185286,9.309412,6.253849,4.262574,9.568328,6.812925,-0.976712,7.556968,3.761233,-5.423773,4.216920,-9.234402], dtype = "float64")#candidate|7000|(18,)|const|float64
var_7001 = relay.var("var_7001", dtype = "float64", shape = ())#candidate|7001|()|var|float64
const_7002 = relay.const([-8.400870,-6.474866,4.865640,-3.400644,-4.847213,-9.680998,2.058555,-1.682170,4.975508,4.484833,3.896245,8.476573,9.844056,-6.495336,-9.487505,-9.803838,-4.147087,-4.112073,1.255427,-2.209817,-3.682897,9.722387,3.462447,-7.055637,2.804959,7.271384,-8.048317,-6.339729,-0.456998,-4.950743,-9.048519,4.510837,-6.046512,9.649614,-1.786481,9.758813,-9.805966,-2.726747,-2.471868,-9.752493,-7.716962,9.691831,-2.791571,-6.507846,-2.104071,0.396003,-3.484794,-9.771183,-0.647014,-1.055969,3.028592,0.183632,-9.514301,-7.009408,-8.437251,-6.881872,-3.837243,-7.481160,8.578129,0.817796,7.797913,2.789033,-1.277560,-9.836028,7.700406,0.946733,-7.821590,-6.044418,1.538934,-9.366461,-4.444859,-0.643169,-2.573115,3.525762,-0.072455,2.665709,-6.037902,0.183617,-3.825610,4.090831,-0.366973,9.946922,-9.086036,3.081651,-1.943826,6.858392,-5.989668,8.519366,-5.257320,-4.743907,2.672563,3.566277,-9.736180,-9.430910,-1.017725,-7.234709,3.135984,-6.679723,-0.008568,0.102969,9.049110,1.925146,-5.326655,-1.311144,4.142238,7.301765,-0.543874,-9.908662,2.717751,-6.497921,0.464124,-8.007042,-4.060665,-1.654174,-7.925259,5.909425,-3.337151,6.564075,1.380833,-6.633931,8.475215,0.261420,-6.039419,-4.804050,0.283625,2.950123,-8.137367,4.774417,-7.401496,1.732963,0.440156,-0.520240,4.075113,-8.167697,8.914784,4.581459,7.123420,9.858654,5.858456,6.702058,-6.457402,4.029883,1.193073,7.569843,-5.494306,-4.007809,8.571378,8.768122,0.415390,7.026406,-4.579814,9.848676,2.689915,1.138159,-2.419909,2.793300,-3.441690,4.670952,2.947948,7.362034,9.050949,1.883103,3.730838,6.388739,9.456962,4.834908,-5.663264,3.972419,4.496581,-4.536711,3.315542,-3.334646,-1.011276,0.701053,-6.476340,0.495933,0.170268,-7.627272,2.558061,7.035154,-5.888268,0.396153,4.554440,9.045495,1.364292,-1.723691,1.171615,-4.298100,9.975129,-3.094023,9.828126,5.645736,-2.647468,4.092749,-3.493605,-9.583853,0.696859,7.501513,-5.546154,-4.705563,-6.869116,5.340234,9.528455,4.587082,1.206380,5.886421,7.315705,2.978072,-7.822035,3.197421,0.449829,-1.821910,1.684278,4.689588,-9.635209,-0.276303,8.849843,-5.753307,0.884742,3.372596,4.811457,7.414660,9.843059,8.266982,2.905601,-9.559868,-2.338259,-0.271113,-8.503836,-4.231577,2.184948,6.817111,-7.700144,4.034841,2.184065,-2.700956,3.386891,5.333946,9.690533,1.216752,-2.937696,3.279527,-8.181618,-7.413548,-0.126803,7.086586,6.812402,-6.347622,-9.202799,-0.924703,-6.635017,3.160033,-5.718956,-4.228241,3.418561,6.269440,-5.430843,-9.593560,-8.005867,7.961181,3.287444,-3.594668,-0.062394,-0.430286,-8.682513,-8.273407,-6.006746,5.452902,1.698568,-2.395979,1.762984,-2.550495,-3.567881,-5.243975,8.757288,7.383942,-4.178542,-7.852637,-3.846856,1.653121,0.052845,6.381256,1.940470,-7.853373,5.046205,1.489220,-1.057246,-7.401656,6.898522,4.419729,-8.754753,5.233664,-5.929334,9.562647,5.214631,-7.389173,5.350775,-1.017773,-1.010837,2.280311,4.379706,-9.469931,-8.912210,-3.538992,3.300314,-2.581161,6.068219,-1.007404,3.149920,-8.416250,-8.450345,8.385633,1.057202,0.272477,5.703726,5.913132,5.179154,-9.801703,-3.485230,8.893593,2.294315,4.294164,-5.493277,-4.811203,-1.744389,-1.758625,7.655568,-8.215035,7.393313,-8.514607,-9.004283,3.179338,6.644175,3.987600,-6.763070,1.894466,-2.812498,-3.788981,-4.936180,0.390035,-1.139901,-0.292194,3.612789,-2.442672,-3.251310,2.755294,-9.648179,-8.038887,1.305511,5.529005,3.546785,5.841047,8.214074,-0.173064,-9.027278,-1.892662,1.279263,9.588863,9.162155,8.153168,-0.111969,-2.191886,0.863051,1.672769,-9.757644,-1.976996,3.094050,-6.221271,-0.521285,8.452173,-5.615561,2.636543,-8.230532,-0.739975,-3.323515,1.520496,9.097642,1.424255,-6.331069,1.145707,0.934422,-2.723916,3.890073,2.819762,4.914420,-3.903705,0.929685,9.843754,-7.119285,0.354780,8.115522,-3.862765,2.790152,2.859959,-3.681563,-3.332864,2.774099,-8.259680,3.844469,-7.299352,-9.092855,-6.304985,-6.860539,3.220323,-1.760112,2.853569,5.346406,-4.901733,9.290178,1.101303,-4.071136,2.517453,-7.412585,-4.517677,6.729213,8.049114,0.284652,6.833002,7.890684,0.575732,-5.179432,-4.209445,-7.390916,-0.474504,-7.560714,4.206376,7.659377,-3.152516,-0.571328,-0.245102,4.344371,-3.759910,7.654756,-0.980533,-6.539948,-2.600715,-7.534606,7.022013,8.529046,-6.899492,1.636669,-4.038280,-0.777466,-8.024660,0.469179,8.261902,-4.712191,-0.148213,2.173518,9.069728,-3.640174,-2.148150,-9.999209,5.739254,3.229661,9.809932,9.451995,-6.149648,9.007761,-2.474514,7.816448,9.454673,3.283195,4.305860,5.939958,3.045507,2.963935,-5.346611,4.010141,5.324787,-8.220961,9.458788,5.971296,0.150132,-9.066107,4.748774,6.401495,-5.864689,-4.214326,-9.335428,-9.601458,8.336141,3.931752,0.312498,4.556790,-6.875400,3.892865,4.034702,2.591450,0.362810,9.026343,8.262442,-0.998827,2.143120,3.260536,-7.522648,3.496463,6.931083,5.640912,4.699708,-2.770469,-0.127598,4.296741,-0.746192,4.339609,8.478240,-6.642621,1.732105,-0.888535,-3.175066,-3.151121,2.261829,-1.212728,6.275645,5.785014,4.057479,-9.008331,6.652183,9.452549,-6.708484,-5.117458,0.012941,-4.363983,0.314460,-7.909814,-8.807323,-2.097991,-5.911669,3.936875,-7.868574,8.122543,-6.819063,-5.399951,4.796543,7.844206,-4.595609,7.347191,-7.942235,-7.751693,-5.942439,2.209118,-6.509415,-4.437154,4.593756,-0.481221,-2.741454,9.828931,0.497935,5.914470,3.205974,-4.718954,-4.431895,-5.268240,1.147192,-0.563649,6.354261,-9.869396,7.837197,-9.985263,-6.321403,-5.610989,-4.208447,1.529564,6.182141,9.669778,3.173813,-7.588801,5.285668,5.368147,-6.950694,2.807587,6.737960,6.248194,-9.496108,8.956850,-4.759581,-5.794744,5.664935,-9.236762,-1.996137,-4.959811,9.447663,9.003747,8.841422,4.519668,-5.213859,6.354701,-9.439904,-4.555959,-0.721807,-9.470078,0.735892,-3.949968,-6.300978,-2.997081,-3.361560,4.343012,1.831198,-9.100951,5.873433,-5.514941,-4.304008,6.737597,-0.055952,-0.194752,-5.699077,7.359598,1.188286,-1.716843,-2.969773,-0.664929,8.908569,-1.806783,-9.563085,9.958255,-7.362346,4.138225,8.240688,-4.810938,-1.747543,6.266022,9.358567,-8.977495,-7.787416,-8.327079,6.359457,5.836494,-1.504144,-5.065728,-0.849902,-6.267862,8.432416,-8.201780,8.778088,5.673150,6.634213,-5.873003,2.835765,5.019586,0.460619,1.834792,-8.071795,-9.718806,-9.626858,5.636755,-3.968593,-2.858989,9.167896,6.584494,3.646710,-1.111174,4.794086,7.565328,5.570177,-4.771101,-8.805597,-0.828972,-3.447951,-1.620180,3.885676,6.591715,8.710214,8.991940,-3.390718,8.315717,5.541346,-8.057591,-7.604629,-4.153600,-5.909790,7.630214,-4.862429,9.284913,-6.878401,1.247025,1.122478,6.565571,-7.927794,5.997114,0.344603,-8.093182,-0.286320,5.760346,-8.419618,4.892291,-6.870804,-6.900325,-0.942970,2.387717,7.364164,-0.886417,-1.213062,7.324470,-3.894787,1.755740,-1.302045,4.608668,9.570867,9.969979,-9.140146,-3.376785,6.858478,3.343147,4.900469,-4.145244,7.050997,5.962883,1.157373,8.485518,-4.948159,9.496458,-7.871981,0.330838,-6.601440,-9.594778,2.570777,3.424212,6.364661,-7.867204,-0.800013,7.325721,3.408176,8.202630,5.156865,1.169899,6.819447,-0.469035,1.063888,9.248545,5.822397,-9.988678,6.154913,8.780674,-6.496053,0.495921,1.195103,-5.388939,0.143246,4.424340,-8.365855,-0.168599,3.527537,-0.252839,6.285916,-0.573125,4.874547,2.360279,3.979141,6.375386,4.211188,-6.101485,1.852314,1.872021,-3.180617,2.245875,4.859296,-9.063660,0.866959,2.269722,6.856551,2.992261,-1.707572,7.535732,3.459290,5.076385,6.011650,2.307607,9.435146,1.297137,5.856156,-8.516155,1.216814,-5.800605,8.010618,2.226021,4.894927,9.297801,9.317823,9.471872,9.618481,9.462532,-8.127540,8.247045,-6.232027,0.033595,-7.833913,-2.413600,4.944244,-2.770704,1.044487,4.530842,-5.078267,-8.880617,5.419013,-2.419061,4.283521,7.525022,0.062952,2.426897,5.392949,8.389965,-1.055358,5.356444,-9.870259,2.619999,0.874319,5.077707,8.340118,-4.809794,4.093974,-4.163738,-3.758338,8.400185,-4.335212,9.873140,1.097767,8.311035,5.820199,4.189715,-9.576003,3.087102,9.023248,2.938107,-6.759751,0.935416,6.285985,-0.804087,5.423540,1.899787,-7.491963,-5.641798,4.279218,-2.931618,-4.217973,1.560740,-2.437936,6.722897,1.174374,-5.266780,-2.043525,4.885737,8.745050,3.448444,1.100334,9.434866,-0.303591,-2.232038,6.155932,-7.513396,-9.077442,0.713577,-1.420664,8.969098,2.354153,6.793142,0.369149,2.839635,2.016254,-2.157333,0.995034,-6.624051,0.325832,-6.617691,2.636542,-8.114095,-1.086348,-2.648767,-8.224934,-8.077198,-5.331012,0.426085,-9.929047,-3.441264,-8.929403,6.647417,-7.729594,2.314957,-1.404990,8.776840,-9.341789,1.622894,4.391859,1.658071,4.674176,7.481691,6.479118,-4.159134,-4.487330,4.533330,6.635825,-9.020871,1.439291,5.937984,6.554995,4.224244,-7.159815,-3.553169,2.399241,-5.579981,9.676943,-7.770644,-2.329441,2.651594,5.730888,4.757065,1.208529,4.628805,1.773144,-7.915023,4.099566,-9.232216,-3.626410,4.633249,-7.166254,6.359711,4.300778,8.996790,-3.873356,-6.100307,1.764331,-8.062559,-7.262048,3.576679,-0.280722,-0.713836,-0.208774,1.058328,-2.167421,-1.792502,-2.978416,-8.643506,4.911248,-3.699454,-6.562202,2.166491,-3.495656,-4.050404,8.788187,6.592911,4.356549,6.674948,-8.690749,6.668025,0.831155,-8.709554,1.631556,-2.589921,-8.354414,-0.918985,5.336507,-6.426838,7.727041,-3.105666,9.158960,-8.729721,-4.317409,-4.846969,-0.272954,3.403806,5.004563,-7.925819,-7.554311,3.865130,1.749984,-6.039804,0.207652,-9.630822,6.636752,-2.114299,-3.243167,-6.579126,-3.959781,-2.178863,-9.089522,0.707670,9.967793,-4.794765,-9.234754,-8.278240,3.275137,-9.713347,7.994137,5.798344,-4.984254,8.985662,-3.057322,8.775705,-2.091121,1.566256,2.555102,-7.177207,-4.074814,-5.415487,-9.040456,-9.077566,8.119675,0.515794,-2.732003,-1.088743,-6.907006,4.988129,0.604801,3.060239,-2.969797,-8.272878,2.709553,-5.974720,8.345920,-6.961077,6.150262,4.270044,-4.010482,-3.985335,9.783621,4.589625,-6.399817,-2.254694,0.143569,-5.026794,-4.619140,2.531677,8.618315,-7.182487,-5.276136,3.384960,1.724873,1.189443,7.585978,-4.463350,-0.945041,-9.635585,9.556743,-6.692357,-4.024066,-7.192275,0.902614,5.267005,-4.520347,2.428726,-2.157375,-0.644804,1.950793,1.133551,2.916740,3.316534,1.920729,1.094551,-7.051370,2.456879,-9.289139,1.213167,8.695211,-4.794466,-6.512847,2.622895,-9.985932,3.239415,7.189668,-0.966968,-8.139796,-1.801126,7.989590,-3.371605,7.894897,3.250287,-0.779972,2.874516,5.881005,8.458935,1.645384,-8.731166,-7.482655,1.310892,0.008171,5.983130,5.645818,9.019153,6.765384,-9.366189,-5.239143,-7.853219,-6.564527,-9.319666,9.609818,-1.275900,-6.733481,7.019655,-1.079365,-7.132331,-2.286076,5.614728,2.256144,0.585609,3.412790,0.187695,3.265918,-3.085842,4.315772,7.538630,-2.098889,1.498770,-5.146921,2.187871,0.525028,-9.676743,6.363899,8.075100,3.315646,7.864468,-6.196254,-1.793399,-5.273728,-4.562085,7.089497,8.958344,9.417513,1.755672,3.683000,-7.314708,-0.865610,-2.867871,-6.980237,2.452856,-0.491308,-7.454036,3.057299,-2.419208,5.495487,-6.252819,-7.291213,-6.850094,-7.985475,-1.291851,5.448845,1.619105,9.842540,3.387237,4.886495,8.108120,-4.353662,6.494279,-8.463392,0.028500,-6.456288,1.763402,0.844433,-0.962968,4.967441,4.154937,3.893889,-7.959314,5.565975,-1.951995,-5.101026,-2.896562,-8.269420,2.887848,-4.471394,-5.673536,-9.154799,1.358111,-3.701109,6.212373,-2.596665,-5.433172,2.028461,2.831673,-0.723729,-6.650869,8.514243,4.353229,-2.964039,1.975822,-9.388382,5.554984,5.087836,-1.066661,-4.308626,0.787123,9.195001,-3.478291,-9.621616,9.279807,5.805715,-6.764225,-8.770471,-8.773638,-5.346522,8.444351,-9.583122,2.282048,-8.591428,7.188673,7.792280,3.135258,-4.989355,-4.428887,8.391749,6.051710,2.247972,-0.877340,-6.036093,-2.396081,-1.977112,7.729851,-8.654505,-5.535621,-2.504037,8.293321,-8.905651,-7.174244,-8.897748,1.732422,-0.744714,-2.643104,-3.087609,-2.293674,-3.636058,0.941478,-7.254284,9.963035,8.750522,2.866528,5.269523,-0.949941,-7.823833,-9.025829,0.385412,-1.946595,-3.706411,4.381590,9.639897,4.883399,-8.653499,-0.348237,7.584014,4.003319,0.158062,1.128065,8.674796,-5.727547,-4.019936,-6.837789,4.231854,-7.216166,4.191680,-3.420219,5.425135,-3.514846,0.121502,-7.959208,-2.365556,3.233599,5.876488,-4.782895,-7.763226,-4.368669,5.039419,-2.454783,2.794961,2.592018,-8.792167,-6.818075,5.988262,5.019722,5.017998,-0.904321,4.112966,-7.271057,-9.848540,5.914059,9.955298,7.447825,-9.683232,8.707650,-0.315145,8.221683,3.638617,-8.689542,-9.869044], dtype = "float64")#candidate|7002|(1280,)|const|float64
const_7003 = relay.const([-1.039493,9.587660,-9.924772,9.145991,1.332970,5.457291,-1.943239,-0.077490,8.834256,-7.227021,-9.222215,-2.903616,-0.185110,-3.971237,2.354621,3.709319,9.375882,-3.269108,-3.026287,1.465186,-0.856180,3.338695,9.527297,4.549478,-6.409364,8.495264,3.531062,-4.219783,-6.685504,0.734695,4.275277,7.893834,8.497353,-8.761509,-3.074726,6.481976,-7.609268,6.617427,9.828147,-4.991164,-1.810707,-2.227939,-5.628419,7.987516,7.419360,-1.205474,-5.038717,2.128076,7.009872,5.838300,-7.123674,-6.900657,3.518183,-5.084596,-5.140513,6.859638,-4.245743,-0.760085,-6.408540,3.250042,-7.971661,-5.146245,-9.898882,4.111867,0.994223,0.949826,6.030597,-8.484429,0.438802,1.349710,9.944790,-4.029688,-6.559542,-2.757088,-4.448638,5.479475,6.688782,2.547749,4.105026,7.007806,-9.445245,-9.732347,6.509161,-3.671514,8.395547,-6.177719,-7.862949,-5.426608,-7.751223,7.573489,6.727119,8.374987,-6.185979,-5.454590,8.856069,-2.676425,-2.460309,-7.189060,3.986316,-6.915658,-4.769887,-4.976005,1.774905,-4.250455,6.443144,-4.086408,-4.558607,-2.161210,2.075262,-6.753617,-9.259872,-8.164238,-6.111782,-3.458559,9.824199,-9.460428,-9.197189,1.432737,-1.314948,7.942437,9.759782,-8.362739,7.095921,6.401956,5.851010,-3.754931,-7.247405,-9.120268,7.406029,1.813329,6.699289,-5.149712,-8.197029,6.899191,0.342706,-0.481870,-1.756784,-6.970103,1.936588,-2.068579,-2.285914,0.331766,1.852981,3.306188,-7.426580,-6.663593,-3.105394,3.306038,-1.280836,6.376922,0.198864,-8.717263,-6.377172,-8.379382,-3.226817,-0.258275,7.105622,-7.957375,7.402352,3.597197,-7.230025,0.147488,-3.309074,1.744809,0.165092,8.532033,-1.629132,1.012481,-0.726726,7.378457,-5.667884,1.777571,0.574684,6.497278,2.588847,-7.154857,-1.159149,0.469023,7.168627,1.959892,0.547709,1.380814,-4.834679,3.339299,-4.272027,-0.102113,-5.346888,-9.122219,6.282579,7.891733,-0.615929,-1.391279,5.640114,-1.772426,-1.763085,-4.883096,-1.847735,9.146249,-5.632619,3.894089,5.120841,2.969485,-6.969418,8.425529,1.233146,-9.828004,9.735372,-7.320927,-6.760875,6.981838,-7.669129,5.138513,4.313695,-4.639658,2.770716,3.036333,6.289669,-4.492710,-7.827877,7.370185,-8.714102,-1.055217,-2.109352,2.448775,6.475434,4.903267,-2.023670,-8.461324,8.669625,3.559321,-0.184706,-5.184423,1.021718,8.337784,-8.692917,-8.796290,9.305425,-7.343879,7.668518,-4.889270,-2.823623,0.447829,-2.872652,2.374062,-4.310744,-9.124235,9.063382,-4.846116,-6.176616,-0.913514,-1.604364,5.308494,0.339952,3.768096,4.457735,0.096811,8.322473,-2.097956,-9.175607,1.764898,-4.787150,-0.833381,-3.809622,8.052773,-2.452023,-4.142195,-7.565451,-7.091525,5.887840,-1.012396,-4.925605,3.711243,-2.458287,7.087441,5.967676,2.339332,3.946003,4.056143,-8.648845,-8.153862,-7.781281,1.383279,-9.626164,7.391858,8.207489,7.687155,1.342200,5.103435,-7.833372,8.935108,-8.592899,-1.774538,-2.188113,7.656185,-8.074663,3.637358,-3.882213,0.760184,9.641763,3.386801,-1.238691,-5.590007,7.207432,-1.295128,-2.664441,5.606146,-7.235877,-6.363322,9.347217,-0.628452,0.431908,-1.518786,-0.039961,1.843845,-1.259745,6.637944,4.559192,4.110671,4.668054,-0.110437,8.992697,-9.984495,9.197549,-6.379026,2.558452,-7.310513,-6.221730,-5.540921,-6.056673,-5.046836,-6.819944,-6.505377,1.138276,-3.049110,0.578802,0.453781,-9.558145,-9.922985,-9.279194,-5.694839,0.325610,6.933773,-4.405808,5.844160,4.545949,5.042194,4.681910,7.944083,9.381484,3.671951,-4.439068,8.778662,4.667575,0.732161,-3.896634,0.154370,-2.426479,-8.969086,-4.133995,-2.410284,4.197447,-0.767102,8.800565,-9.498502], dtype = "float64")#candidate|7003|(364,)|const|float64
call_6997 = relay.TupleGetItem(func_6131_call(relay.reshape(const_6998.astype('bool'), [15, 3, 7]), relay.reshape(const_6998.astype('bool'), [15, 3, 7]), relay.reshape(var_6999.astype('float32'), [780, 1]), relay.reshape(const_7000.astype('float64'), [18,]), relay.reshape(var_7001.astype('float64'), []), relay.reshape(const_7002.astype('float64'), [1280,]), relay.reshape(const_7003.astype('float64'), [364,]), ), 15)
call_7004 = relay.TupleGetItem(func_6140_call(relay.reshape(const_6998.astype('bool'), [15, 3, 7]), relay.reshape(const_6998.astype('bool'), [15, 3, 7]), relay.reshape(var_6999.astype('float32'), [780, 1]), relay.reshape(const_7000.astype('float64'), [18,]), relay.reshape(var_7001.astype('float64'), []), relay.reshape(const_7002.astype('float64'), [1280,]), relay.reshape(const_7003.astype('float64'), [364,]), ), 15)
output = relay.Tuple([uop_6994,call_6997,const_6998,var_6999,const_7000,var_7001,const_7002,const_7003,])
output2 = relay.Tuple([uop_6996,call_7004,const_6998,var_6999,const_7000,var_7001,const_7002,const_7003,])
func_7019 = relay.Function([var_6999,var_7001,], output)
mod['func_7019'] = func_7019
mod = relay.transform.InferType()(mod)
var_7020 = relay.var("var_7020", dtype = "float32", shape = (390, 2))#candidate|7020|(390, 2)|var|float32
var_7021 = relay.var("var_7021", dtype = "float64", shape = ())#candidate|7021|()|var|float64
output = func_7019(var_7020,var_7021,)
func_7022 = relay.Function([var_7020,var_7021,], output)
mutated_mod['func_7022'] = func_7022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6695_call = mod.get_global_var('func_6695')
func_6696_call = mutated_mod.get_global_var('func_6696')
call_7041 = relay.TupleGetItem(func_6695_call(), 0)
call_7042 = relay.TupleGetItem(func_6696_call(), 0)
output = call_7041
output2 = call_7042
func_7077 = relay.Function([], output)
mod['func_7077'] = func_7077
mod = relay.transform.InferType()(mod)
output = func_7077()
func_7078 = relay.Function([], output)
mutated_mod['func_7078'] = func_7078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6489_call = mod.get_global_var('func_6489')
func_6490_call = mutated_mod.get_global_var('func_6490')
call_7116 = func_6489_call()
call_7117 = func_6489_call()
output = call_7116
output2 = call_7117
func_7124 = relay.Function([], output)
mod['func_7124'] = func_7124
mod = relay.transform.InferType()(mod)
output = func_7124()
func_7125 = relay.Function([], output)
mutated_mod['func_7125'] = func_7125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6695_call = mod.get_global_var('func_6695')
func_6696_call = mutated_mod.get_global_var('func_6696')
call_7128 = relay.TupleGetItem(func_6695_call(), 0)
call_7129 = relay.TupleGetItem(func_6696_call(), 0)
func_4769_call = mod.get_global_var('func_4769')
func_4772_call = mutated_mod.get_global_var('func_4772')
var_7160 = relay.var("var_7160", dtype = "bool", shape = ())#candidate|7160|()|var|bool
call_7159 = relay.TupleGetItem(func_4769_call(relay.reshape(var_7160.astype('bool'), [])), 2)
call_7161 = relay.TupleGetItem(func_4772_call(relay.reshape(var_7160.astype('bool'), [])), 2)
output = relay.Tuple([call_7128,call_7159,var_7160,])
output2 = relay.Tuple([call_7129,call_7161,var_7160,])
func_7168 = relay.Function([var_7160,], output)
mod['func_7168'] = func_7168
mod = relay.transform.InferType()(mod)
var_7169 = relay.var("var_7169", dtype = "bool", shape = ())#candidate|7169|()|var|bool
output = func_7168(var_7169)
func_7170 = relay.Function([var_7169], output)
mutated_mod['func_7170'] = func_7170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6695_call = mod.get_global_var('func_6695')
func_6696_call = mutated_mod.get_global_var('func_6696')
call_7197 = relay.TupleGetItem(func_6695_call(), 0)
call_7198 = relay.TupleGetItem(func_6696_call(), 0)
func_7168_call = mod.get_global_var('func_7168')
func_7170_call = mutated_mod.get_global_var('func_7170')
const_7200 = relay.const(False, dtype = "bool")#candidate|7200|()|const|bool
call_7199 = relay.TupleGetItem(func_7168_call(relay.reshape(const_7200.astype('bool'), [])), 0)
call_7201 = relay.TupleGetItem(func_7170_call(relay.reshape(const_7200.astype('bool'), [])), 0)
output = relay.Tuple([call_7197,call_7199,const_7200,])
output2 = relay.Tuple([call_7198,call_7201,const_7200,])
func_7228 = relay.Function([], output)
mod['func_7228'] = func_7228
mod = relay.transform.InferType()(mod)
output = func_7228()
func_7229 = relay.Function([], output)
mutated_mod['func_7229'] = func_7229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7228_call = mod.get_global_var('func_7228')
func_7229_call = mutated_mod.get_global_var('func_7229')
call_7242 = relay.TupleGetItem(func_7228_call(), 0)
call_7243 = relay.TupleGetItem(func_7229_call(), 0)
var_7248 = relay.var("var_7248", dtype = "float32", shape = (3, 11, 2))#candidate|7248|(3, 11, 2)|var|float32
bop_7249 = relay.right_shift(call_7242.astype('int8'), relay.reshape(var_7248.astype('int8'), relay.shape_of(call_7242))) # shape=(3, 11, 2)
bop_7252 = relay.right_shift(call_7243.astype('int8'), relay.reshape(var_7248.astype('int8'), relay.shape_of(call_7243))) # shape=(3, 11, 2)
output = relay.Tuple([bop_7249,])
output2 = relay.Tuple([bop_7252,])
func_7255 = relay.Function([var_7248,], output)
mod['func_7255'] = func_7255
mod = relay.transform.InferType()(mod)
var_7256 = relay.var("var_7256", dtype = "float32", shape = (3, 11, 2))#candidate|7256|(3, 11, 2)|var|float32
output = func_7255(var_7256)
func_7257 = relay.Function([var_7256], output)
mutated_mod['func_7257'] = func_7257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6489_call = mod.get_global_var('func_6489')
func_6490_call = mutated_mod.get_global_var('func_6490')
call_7259 = func_6489_call()
call_7260 = func_6489_call()
output = call_7259
output2 = call_7260
func_7290 = relay.Function([], output)
mod['func_7290'] = func_7290
mod = relay.transform.InferType()(mod)
mutated_mod['func_7290'] = func_7290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7290_call = mutated_mod.get_global_var('func_7290')
call_7291 = func_7290_call()
output = call_7291
func_7292 = relay.Function([], output)
mutated_mod['func_7292'] = func_7292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6922_call = mod.get_global_var('func_6922')
func_6923_call = mutated_mod.get_global_var('func_6923')
call_7300 = relay.TupleGetItem(func_6922_call(), 0)
call_7301 = relay.TupleGetItem(func_6923_call(), 0)
func_5041_call = mod.get_global_var('func_5041')
func_5045_call = mutated_mod.get_global_var('func_5045')
var_7326 = relay.var("var_7326", dtype = "float64", shape = (1350,))#candidate|7326|(1350,)|var|float64
call_7325 = relay.TupleGetItem(func_5041_call(relay.reshape(var_7326.astype('float64'), [15, 9, 10]), relay.reshape(var_7326.astype('float64'), [15, 9, 10]), ), 0)
call_7327 = relay.TupleGetItem(func_5045_call(relay.reshape(var_7326.astype('float64'), [15, 9, 10]), relay.reshape(var_7326.astype('float64'), [15, 9, 10]), ), 0)
output = relay.Tuple([call_7300,call_7325,var_7326,])
output2 = relay.Tuple([call_7301,call_7327,var_7326,])
func_7338 = relay.Function([var_7326,], output)
mod['func_7338'] = func_7338
mod = relay.transform.InferType()(mod)
var_7339 = relay.var("var_7339", dtype = "float64", shape = (1350,))#candidate|7339|(1350,)|var|float64
output = func_7338(var_7339)
func_7340 = relay.Function([var_7339], output)
mutated_mod['func_7340'] = func_7340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7290_call = mod.get_global_var('func_7290')
func_7292_call = mutated_mod.get_global_var('func_7292')
call_7378 = func_7290_call()
call_7379 = func_7290_call()
var_7398 = relay.var("var_7398", dtype = "float32", shape = (3, 11, 2))#candidate|7398|(3, 11, 2)|var|float32
bop_7399 = relay.multiply(call_7378.astype('uint16'), relay.reshape(var_7398.astype('uint16'), relay.shape_of(call_7378))) # shape=(3, 11, 2)
bop_7402 = relay.multiply(call_7379.astype('uint16'), relay.reshape(var_7398.astype('uint16'), relay.shape_of(call_7379))) # shape=(3, 11, 2)
output = bop_7399
output2 = bop_7402
func_7403 = relay.Function([var_7398,], output)
mod['func_7403'] = func_7403
mod = relay.transform.InferType()(mod)
var_7404 = relay.var("var_7404", dtype = "float32", shape = (3, 11, 2))#candidate|7404|(3, 11, 2)|var|float32
output = func_7403(var_7404)
func_7405 = relay.Function([var_7404], output)
mutated_mod['func_7405'] = func_7405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7228_call = mod.get_global_var('func_7228')
func_7229_call = mutated_mod.get_global_var('func_7229')
call_7456 = relay.TupleGetItem(func_7228_call(), 1)
call_7457 = relay.TupleGetItem(func_7229_call(), 1)
output = call_7456
output2 = call_7457
func_7459 = relay.Function([], output)
mod['func_7459'] = func_7459
mod = relay.transform.InferType()(mod)
mutated_mod['func_7459'] = func_7459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7459_call = mutated_mod.get_global_var('func_7459')
call_7460 = func_7459_call()
output = call_7460
func_7461 = relay.Function([], output)
mutated_mod['func_7461'] = func_7461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6922_call = mod.get_global_var('func_6922')
func_6923_call = mutated_mod.get_global_var('func_6923')
call_7469 = relay.TupleGetItem(func_6922_call(), 0)
call_7470 = relay.TupleGetItem(func_6923_call(), 0)
func_1381_call = mod.get_global_var('func_1381')
func_1383_call = mutated_mod.get_global_var('func_1383')
var_7480 = relay.var("var_7480", dtype = "int16", shape = (15,))#candidate|7480|(15,)|var|int16
call_7479 = relay.TupleGetItem(func_1381_call(relay.reshape(var_7480.astype('int16'), [15, 1])), 3)
call_7481 = relay.TupleGetItem(func_1383_call(relay.reshape(var_7480.astype('int16'), [15, 1])), 3)
output = relay.Tuple([call_7469,call_7479,var_7480,])
output2 = relay.Tuple([call_7470,call_7481,var_7480,])
func_7482 = relay.Function([var_7480,], output)
mod['func_7482'] = func_7482
mod = relay.transform.InferType()(mod)
var_7483 = relay.var("var_7483", dtype = "int16", shape = (15,))#candidate|7483|(15,)|var|int16
output = func_7482(var_7483)
func_7484 = relay.Function([var_7483], output)
mutated_mod['func_7484'] = func_7484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7290_call = mod.get_global_var('func_7290')
func_7292_call = mutated_mod.get_global_var('func_7292')
call_7499 = func_7290_call()
call_7500 = func_7290_call()
var_7503 = relay.var("var_7503", dtype = "float32", shape = (3, 11, 2))#candidate|7503|(3, 11, 2)|var|float32
bop_7504 = relay.mod(call_7499.astype('float32'), relay.reshape(var_7503.astype('float32'), relay.shape_of(call_7499))) # shape=(3, 11, 2)
bop_7507 = relay.mod(call_7500.astype('float32'), relay.reshape(var_7503.astype('float32'), relay.shape_of(call_7500))) # shape=(3, 11, 2)
func_5041_call = mod.get_global_var('func_5041')
func_5045_call = mutated_mod.get_global_var('func_5045')
var_7511 = relay.var("var_7511", dtype = "float64", shape = (1350,))#candidate|7511|(1350,)|var|float64
call_7510 = relay.TupleGetItem(func_5041_call(relay.reshape(var_7511.astype('float64'), [15, 9, 10]), relay.reshape(var_7511.astype('float64'), [15, 9, 10]), ), 0)
call_7512 = relay.TupleGetItem(func_5045_call(relay.reshape(var_7511.astype('float64'), [15, 9, 10]), relay.reshape(var_7511.astype('float64'), [15, 9, 10]), ), 0)
output = relay.Tuple([bop_7504,call_7510,var_7511,])
output2 = relay.Tuple([bop_7507,call_7512,var_7511,])
func_7521 = relay.Function([var_7503,var_7511,], output)
mod['func_7521'] = func_7521
mod = relay.transform.InferType()(mod)
mutated_mod['func_7521'] = func_7521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7521_call = mutated_mod.get_global_var('func_7521')
var_7523 = relay.var("var_7523", dtype = "float32", shape = (3, 11, 2))#candidate|7523|(3, 11, 2)|var|float32
var_7524 = relay.var("var_7524", dtype = "float64", shape = (1350,))#candidate|7524|(1350,)|var|float64
call_7522 = func_7521_call(var_7523,var_7524,)
output = call_7522
func_7525 = relay.Function([var_7523,var_7524,], output)
mutated_mod['func_7525'] = func_7525
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7552 = relay.const([[[5,7,5,-3,2,10,-8,-7,4],[2,2,7,3,10,4,-9,5,5],[8,4,-7,1,-9,-10,10,-5,3],[6,-5,-7,10,-10,-10,7,-4,-9],[5,-6,10,-7,2,-3,-5,-3,5],[-9,-6,4,-5,-5,1,-10,5,3],[6,6,-4,-2,-9,-7,-7,-3,-7]],[[-10,-7,-9,-10,-7,9,-10,9,-2],[8,2,-3,4,-7,-4,6,-5,8],[1,7,2,-7,-2,2,-9,-9,8],[2,-1,-2,3,10,9,4,-5,8],[-8,2,1,-3,4,5,-4,-5,6],[-2,5,9,-10,-6,5,-4,8,2],[-10,4,-4,8,-4,5,-2,2,-8]],[[3,-5,5,-10,-4,7,-2,10,-2],[2,4,-5,-7,5,4,2,5,4],[-9,1,7,-9,6,2,4,8,-2],[-7,9,10,-7,-3,-10,-2,-5,2],[10,10,3,-4,8,4,-4,-10,-3],[10,-3,-4,-2,-1,9,9,-7,5],[-1,-6,10,8,1,1,-10,-5,4]],[[5,-4,-10,-2,-4,6,-8,8,-5],[-3,4,-2,-7,-4,5,-2,3,-9],[-10,-2,1,-4,8,-4,-10,-7,-1],[7,-9,-2,10,-5,9,6,8,-4],[9,-9,-9,9,1,4,-4,10,4],[8,-6,-9,-8,4,6,-4,-7,-1],[7,6,5,-10,2,2,3,-2,-2]],[[2,7,-5,-8,-5,3,1,-5,2],[8,-8,-3,8,10,-5,-10,-2,4],[9,8,7,1,5,-7,-7,8,-7],[8,7,7,8,-10,6,10,8,-9],[-9,-2,-8,9,8,-3,-8,-4,6],[-8,9,-7,-2,8,4,4,10,6],[-9,-3,4,-3,4,-9,7,7,5]],[[-10,-2,6,8,7,-6,-3,-2,3],[10,-10,3,7,7,7,1,-9,-6],[6,5,-1,10,7,10,-8,5,-7],[7,8,1,6,-3,-4,9,4,-5],[6,-6,-9,-4,7,7,8,9,8],[1,1,-8,-4,4,3,-10,-9,6],[3,7,9,-5,7,-3,3,8,10]],[[8,5,10,3,8,8,-8,-4,-10],[-8,-10,-8,-2,6,4,8,-10,4],[-2,1,7,-6,8,-1,-2,5,5],[-4,-6,-7,-8,4,7,-9,-3,10],[8,6,-5,8,7,9,9,-7,6],[7,8,-2,-7,5,-9,-3,-1,5],[-7,5,-8,-6,-10,4,-8,9,-2]],[[10,-2,-3,-9,2,-5,-8,-1,8],[9,-6,8,4,1,-9,-6,4,1],[-1,-4,-10,9,3,3,7,5,1],[-5,9,-10,-9,-7,-4,-4,9,-5],[9,9,4,-5,-5,6,6,-3,-7],[3,-7,3,-9,6,5,8,-7,-5],[-10,4,3,-1,3,-1,-7,10,-5]],[[5,10,-9,-5,8,-4,3,-5,7],[-8,4,2,-6,2,-5,7,-8,-3],[3,-5,-10,-3,-3,9,-6,-10,-2],[10,3,2,-8,8,-9,6,-7,-10],[-2,-9,3,6,-8,-4,3,8,7],[-4,2,-4,2,-10,2,7,7,10],[-5,1,-5,6,8,-3,-6,1,-8]],[[-1,-4,-9,-3,10,-2,9,-7,3],[-5,1,2,2,3,-8,-8,-9,-1],[9,-7,-3,-1,6,-5,3,7,7],[10,-7,-1,-3,-5,-3,3,2,3],[8,-8,-4,-3,-4,1,-10,-9,3],[6,-10,8,-9,5,10,-7,-2,3],[9,-2,-6,2,-3,5,-2,-10,1]],[[-6,-1,-2,-9,-9,3,8,10,4],[-3,4,-9,2,7,6,1,8,2],[-1,8,-5,-4,2,-3,9,-5,1],[-1,9,-6,8,6,-7,8,3,-10],[7,-1,7,7,1,-1,10,-7,4],[4,9,9,-10,6,3,4,-1,10],[1,7,3,-4,2,2,5,9,5]],[[9,-7,1,-2,-1,-1,2,10,4],[7,-6,9,6,-1,-7,-3,6,-3],[9,3,10,-2,-4,4,-6,5,-2],[10,-10,5,9,-6,-7,3,6,-9],[-8,9,-3,-1,3,-3,-4,-5,3],[-4,7,9,-10,-3,6,3,2,9],[4,-6,-8,4,-9,-8,8,-7,3]],[[2,-6,-10,-6,8,4,3,9,-6],[8,1,-8,10,-3,4,10,-9,-10],[1,-3,-2,-8,6,-4,-6,-2,-10],[8,-10,-8,6,10,-6,-6,4,6],[8,-3,-3,9,-1,-10,5,2,8],[-10,8,2,10,-9,-9,2,-10,4],[-6,-5,-7,-8,3,-8,8,5,-5]],[[9,5,10,2,-1,-1,-6,-1,-1],[-5,1,-9,-9,4,-4,-3,6,1],[-3,-10,-5,-3,-5,1,-3,7,4],[-10,4,1,4,-10,-5,8,4,-4],[8,-10,-2,-3,9,6,7,-10,-3],[-8,8,-9,1,-1,-5,3,-4,8],[-6,-10,10,-10,-5,7,-3,5,5]],[[2,-9,-8,-2,8,6,2,7,-8],[-10,-4,-9,1,4,-3,7,-4,10],[1,-4,8,6,-3,1,-10,2,-4],[-4,2,10,-8,3,-3,3,5,-4],[-7,-4,-5,-4,6,10,-6,4,2],[-5,10,2,1,9,3,10,6,-4],[6,6,3,-1,-10,-9,10,-5,-10]]], dtype = "int8")#candidate|7552|(15, 7, 9)|const|int8
var_7553 = relay.var("var_7553", dtype = "int8", shape = (15, 7, 9))#candidate|7553|(15, 7, 9)|var|int8
bop_7554 = relay.logical_xor(const_7552.astype('int8'), relay.reshape(var_7553.astype('int8'), relay.shape_of(const_7552))) # shape=(15, 7, 9)
var_7564 = relay.var("var_7564", dtype = "int8", shape = (15, 7, 9))#candidate|7564|(15, 7, 9)|var|int8
bop_7565 = relay.greater_equal(const_7552.astype('bool'), relay.reshape(var_7564.astype('bool'), relay.shape_of(const_7552))) # shape=(15, 7, 9)
output = relay.Tuple([bop_7554,bop_7565,])
output2 = relay.Tuple([bop_7554,bop_7565,])
func_7568 = relay.Function([var_7553,var_7564,], output)
mod['func_7568'] = func_7568
mod = relay.transform.InferType()(mod)
var_7569 = relay.var("var_7569", dtype = "int8", shape = (15, 7, 9))#candidate|7569|(15, 7, 9)|var|int8
var_7570 = relay.var("var_7570", dtype = "int8", shape = (15, 7, 9))#candidate|7570|(15, 7, 9)|var|int8
output = func_7568(var_7569,var_7570,)
func_7571 = relay.Function([var_7569,var_7570,], output)
mutated_mod['func_7571'] = func_7571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6412_call = mod.get_global_var('func_6412')
func_6414_call = mutated_mod.get_global_var('func_6414')
call_7577 = relay.TupleGetItem(func_6412_call(), 0)
call_7578 = relay.TupleGetItem(func_6414_call(), 0)
var_7583 = relay.var("var_7583", dtype = "float32", shape = (3, 11, 2))#candidate|7583|(3, 11, 2)|var|float32
bop_7584 = relay.power(call_7577.astype('float64'), relay.reshape(var_7583.astype('float64'), relay.shape_of(call_7577))) # shape=(3, 11, 2)
bop_7587 = relay.power(call_7578.astype('float64'), relay.reshape(var_7583.astype('float64'), relay.shape_of(call_7578))) # shape=(3, 11, 2)
output = bop_7584
output2 = bop_7587
func_7600 = relay.Function([var_7583,], output)
mod['func_7600'] = func_7600
mod = relay.transform.InferType()(mod)
var_7601 = relay.var("var_7601", dtype = "float32", shape = (3, 11, 2))#candidate|7601|(3, 11, 2)|var|float32
output = func_7600(var_7601)
func_7602 = relay.Function([var_7601], output)
mutated_mod['func_7602'] = func_7602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7124_call = mod.get_global_var('func_7124')
func_7125_call = mutated_mod.get_global_var('func_7125')
call_7646 = func_7124_call()
call_7647 = func_7124_call()
const_7651 = relay.const([[[-1.877796,6.029127],[1.165491,9.905708],[0.610609,-3.056143],[8.440470,-0.436885],[-2.239337,-1.126701],[-3.259766,-8.115320],[-1.304230,-8.212277],[-1.581784,6.149418],[1.148594,-2.518600],[9.756964,-2.831369],[-4.036891,-5.036704]],[[-9.481821,6.924695],[-8.234256,-6.465950],[-3.871268,6.656270],[9.863295,-9.138236],[3.234493,-5.867822],[-1.900605,6.979563],[-4.421870,0.110738],[-2.247622,6.060122],[-4.164547,5.467381],[-5.378025,7.609476],[-8.402823,8.195678]],[[-4.830736,-6.924140],[6.779132,-2.267348],[8.220133,-7.443485],[-1.560038,-7.359594],[9.020200,1.750966],[4.327288,9.398865],[-2.488319,-1.014532],[0.947621,2.173806],[-7.697679,6.513552],[-2.050918,2.309780],[2.331805,-5.093595]]], dtype = "float32")#candidate|7651|(3, 11, 2)|const|float32
bop_7652 = relay.greater(call_7646.astype('bool'), relay.reshape(const_7651.astype('bool'), relay.shape_of(call_7646))) # shape=(3, 11, 2)
bop_7655 = relay.greater(call_7647.astype('bool'), relay.reshape(const_7651.astype('bool'), relay.shape_of(call_7647))) # shape=(3, 11, 2)
func_6946_call = mod.get_global_var('func_6946')
func_6948_call = mutated_mod.get_global_var('func_6948')
call_7658 = relay.TupleGetItem(func_6946_call(relay.reshape(bop_7652.astype('float32'), [3, 11, 2])), 0)
call_7659 = relay.TupleGetItem(func_6948_call(relay.reshape(bop_7652.astype('float32'), [3, 11, 2])), 0)
uop_7660 = relay.sinh(call_7658.astype('float32')) # shape=(3, 11, 2)
uop_7662 = relay.sinh(call_7659.astype('float32')) # shape=(3, 11, 2)
output = relay.Tuple([bop_7652,uop_7660,])
output2 = relay.Tuple([bop_7655,uop_7662,])
func_7667 = relay.Function([], output)
mod['func_7667'] = func_7667
mod = relay.transform.InferType()(mod)
mutated_mod['func_7667'] = func_7667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7667_call = mutated_mod.get_global_var('func_7667')
call_7668 = func_7667_call()
output = call_7668
func_7669 = relay.Function([], output)
mutated_mod['func_7669'] = func_7669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7077_call = mod.get_global_var('func_7077')
func_7078_call = mutated_mod.get_global_var('func_7078')
call_7726 = func_7077_call()
call_7727 = func_7077_call()
output = call_7726
output2 = call_7727
func_7788 = relay.Function([], output)
mod['func_7788'] = func_7788
mod = relay.transform.InferType()(mod)
output = func_7788()
func_7789 = relay.Function([], output)
mutated_mod['func_7789'] = func_7789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6412_call = mod.get_global_var('func_6412')
func_6414_call = mutated_mod.get_global_var('func_6414')
call_7801 = relay.TupleGetItem(func_6412_call(), 0)
call_7802 = relay.TupleGetItem(func_6414_call(), 0)
func_6922_call = mod.get_global_var('func_6922')
func_6923_call = mutated_mod.get_global_var('func_6923')
call_7822 = relay.TupleGetItem(func_6922_call(), 1)
call_7823 = relay.TupleGetItem(func_6923_call(), 1)
output = relay.Tuple([call_7801,call_7822,])
output2 = relay.Tuple([call_7802,call_7823,])
func_7836 = relay.Function([], output)
mod['func_7836'] = func_7836
mod = relay.transform.InferType()(mod)
output = func_7836()
func_7837 = relay.Function([], output)
mutated_mod['func_7837'] = func_7837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7077_call = mod.get_global_var('func_7077')
func_7078_call = mutated_mod.get_global_var('func_7078')
call_7867 = func_7077_call()
call_7868 = func_7077_call()
uop_7888 = relay.asin(call_7867.astype('float32')) # shape=(3, 11, 2)
uop_7890 = relay.asin(call_7868.astype('float32')) # shape=(3, 11, 2)
uop_7891 = relay.cos(call_7867.astype('float64')) # shape=(3, 11, 2)
uop_7893 = relay.cos(call_7868.astype('float64')) # shape=(3, 11, 2)
output = relay.Tuple([uop_7888,uop_7891,])
output2 = relay.Tuple([uop_7890,uop_7893,])
func_7906 = relay.Function([], output)
mod['func_7906'] = func_7906
mod = relay.transform.InferType()(mod)
mutated_mod['func_7906'] = func_7906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7906_call = mutated_mod.get_global_var('func_7906')
call_7907 = func_7906_call()
output = call_7907
func_7908 = relay.Function([], output)
mutated_mod['func_7908'] = func_7908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7788_call = mod.get_global_var('func_7788')
func_7789_call = mutated_mod.get_global_var('func_7789')
call_7939 = func_7788_call()
call_7940 = func_7788_call()
func_7788_call = mod.get_global_var('func_7788')
func_7789_call = mutated_mod.get_global_var('func_7789')
call_7945 = func_7788_call()
call_7946 = func_7788_call()
uop_7950 = relay.exp(call_7945.astype('float64')) # shape=(3, 11, 2)
uop_7952 = relay.exp(call_7946.astype('float64')) # shape=(3, 11, 2)
output = relay.Tuple([call_7939,uop_7950,])
output2 = relay.Tuple([call_7940,uop_7952,])
func_7955 = relay.Function([], output)
mod['func_7955'] = func_7955
mod = relay.transform.InferType()(mod)
mutated_mod['func_7955'] = func_7955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7955_call = mutated_mod.get_global_var('func_7955')
call_7956 = func_7955_call()
output = call_7956
func_7957 = relay.Function([], output)
mutated_mod['func_7957'] = func_7957
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7977 = relay.const([[[-10,7,-9],[-1,-9,6],[8,3,7],[3,4,-7],[2,-9,-2],[3,5,-7],[-10,1,-7],[-7,6,-4]],[[-7,7,8],[4,9,-4],[-10,-10,6],[-3,8,-8],[-3,-9,-4],[4,-9,-3],[-4,-8,2],[3,-1,-9]],[[2,3,-6],[-4,-5,7],[-3,3,3],[-10,4,-9],[2,-8,-7],[-9,-7,-1],[-5,-1,6],[-2,-1,3]],[[-4,1,3],[-4,-4,-9],[9,1,10],[10,-5,-6],[1,9,6],[3,7,7],[4,6,-6],[-10,-10,-3]],[[-3,8,6],[-8,-3,-8],[-9,8,-7],[-5,-8,10],[3,-9,8],[-5,-6,8],[6,-8,3],[9,-9,7]],[[2,6,4],[-4,-3,-1],[-6,2,9],[4,6,-8],[8,-2,-4],[10,2,8],[1,2,-4],[4,1,-9]],[[-8,8,5],[-6,3,9],[-8,5,-4],[-7,-4,6],[3,-7,-10],[5,-1,3],[-8,8,-8],[9,5,-7]],[[5,-3,-4],[-7,1,-1],[2,10,-8],[-9,3,-10],[-6,6,-10],[-2,6,6],[-4,-6,8],[-7,-3,4]],[[-1,2,2],[-4,8,10],[4,7,-7],[9,7,-8],[5,5,-4],[3,-2,1],[4,4,7],[2,-8,-1]],[[-1,6,-8],[-2,4,10],[4,5,-8],[-2,4,-6],[2,4,8],[-2,-8,6],[-7,-8,6],[10,1,10]],[[4,2,7],[-10,-8,8],[-10,5,-1],[3,-1,-10],[10,1,-7],[-3,-2,-10],[-4,10,7],[-8,-8,-4]],[[-5,-8,9],[-5,8,-2],[-6,8,9],[1,-10,-7],[-8,-3,-7],[-5,7,1],[3,-7,-4],[8,4,-2]],[[-5,8,1],[-2,10,5],[-4,10,-6],[-9,8,10],[5,-4,3],[3,6,-3],[7,-7,-1],[-4,3,-6]]], dtype = "int16")#candidate|7977|(13, 8, 3)|const|int16
var_7978 = relay.var("var_7978", dtype = "int16", shape = (13, 8, 3))#candidate|7978|(13, 8, 3)|var|int16
bop_7979 = relay.less(const_7977.astype('bool'), relay.reshape(var_7978.astype('bool'), relay.shape_of(const_7977))) # shape=(13, 8, 3)
bop_7985 = relay.bitwise_and(const_7977.astype('uint16'), relay.reshape(var_7978.astype('uint16'), relay.shape_of(const_7977))) # shape=(13, 8, 3)
uop_7994 = relay.log2(bop_7985.astype('float32')) # shape=(13, 8, 3)
func_6131_call = mod.get_global_var('func_6131')
func_6140_call = mutated_mod.get_global_var('func_6140')
var_7998 = relay.var("var_7998", dtype = "bool", shape = (315,))#candidate|7998|(315,)|var|bool
var_7999 = relay.var("var_7999", dtype = "float32", shape = (780,))#candidate|7999|(780,)|var|float32
const_8000 = relay.const([-0.615477,3.645069,0.300226,6.307987,5.784193,5.014800,1.818249,-0.320472,-8.766138,-6.907155,-5.981527,-8.542115,8.524740,5.377897,9.160906,5.608074,-7.132652,3.471072], dtype = "float64")#candidate|8000|(18,)|const|float64
const_8001 = relay.const(2.579204, dtype = "float64")#candidate|8001|()|const|float64
const_8002 = relay.const([9.337272,4.889945,7.855895,2.788704,0.623173,7.157551,4.677844,6.193072,3.041955,7.215677,-0.984179,-8.172424,0.969696,-0.591021,-7.957832,3.559223,4.147911,2.555852,-3.428146,-0.130488,-4.794312,8.715025,-9.231269,0.498443,3.504707,5.675638,6.965065,9.521942,9.631976,4.617781,9.261932,6.027580,9.374986,5.953175,-2.364165,7.112867,2.972228,-0.872229,-2.112046,-4.166638,-8.420219,1.309397,6.405460,-5.118840,-2.431247,-8.010816,6.086222,-7.060425,-1.919836,-1.880622,1.040599,5.624515,-6.895173,0.725259,5.134021,-5.746253,0.671858,3.568513,7.198393,-7.516838,5.929737,6.551316,-0.909460,1.679586,1.957404,0.230292,-9.739315,-1.398812,2.777649,9.673607,2.529304,-0.503115,6.363298,9.685953,-7.533301,-4.028991,-5.827814,-8.437084,2.837127,7.154761,1.333332,8.244981,7.404755,9.200782,4.744300,-0.498579,-8.428775,-8.585617,-7.323759,-6.922813,4.827354,4.917156,-1.148505,-6.724601,1.201338,7.714265,9.186781,-1.282294,-8.244115,3.863867,-5.614402,-8.912381,-2.039666,-1.159504,-5.829547,9.446030,9.155174,3.212792,-6.328729,8.803601,1.028659,2.889430,-9.474791,7.119319,0.283333,-1.180919,-5.035308,-4.795533,0.301303,-5.689299,-6.916386,3.981618,-3.913504,8.640388,9.459741,-1.949445,8.242750,2.237807,-8.319296,-0.946988,9.481070,4.810156,0.645111,-8.509530,7.801568,-6.155489,3.837709,8.610491,-1.391710,-7.826423,-7.848011,-5.855408,-5.833859,3.752444,2.850684,-1.460482,-1.367038,-5.359594,-4.179169,4.378714,0.733875,8.173556,4.655681,-6.436988,1.764563,4.785335,-8.888917,-8.813038,6.608685,3.660932,7.541563,5.459441,5.452977,-3.388186,6.824975,2.956945,2.738619,4.907925,-1.976826,9.527677,-6.653567,1.898436,-4.189029,-2.398406,4.772751,-8.521830,5.703298,-4.641988,-6.679192,-0.438931,-8.038371,-6.397330,-7.444383,9.173942,-8.173777,8.990480,9.388807,8.748002,-9.165626,-5.928761,4.387675,-4.626521,-6.218289,6.097304,2.058999,-4.980190,-5.937458,-4.818249,-5.888941,7.396466,-4.060327,-8.415970,5.435883,6.420065,6.658199,6.889844,2.503164,1.908844,-5.592574,-6.191282,5.688091,-1.474253,2.687929,-1.655171,-8.728660,-4.231120,-0.974727,-9.079976,-1.507618,0.535286,7.622145,-7.934787,1.388300,6.280930,5.940244,0.840989,-6.386926,-3.701703,-7.855735,-3.264053,-5.327492,2.719489,8.966278,-0.043712,-0.447855,7.190124,-9.255968,-6.654204,1.564316,9.617860,6.656274,4.552405,-4.071178,6.589199,3.391185,2.326936,7.889243,-4.483429,8.474502,-6.216902,5.352344,6.317351,-9.404143,0.751395,5.511110,-3.480899,1.572892,3.791343,7.238369,2.525366,-6.714163,-1.482579,8.339782,-3.867761,2.373482,-9.078428,-7.133738,-7.381946,7.328633,-1.934793,-9.181559,3.135465,5.279888,-1.163774,-1.283643,7.397765,-9.776539,-6.267556,-5.920561,-4.875927,5.126526,-3.859215,2.505602,-4.086770,-7.188869,6.787794,2.218057,5.404100,1.189608,8.784084,3.378835,-0.699201,-0.017566,8.948985,8.966205,-9.379379,6.521300,-3.334920,5.435362,4.148629,-6.075092,9.433361,-0.409538,-7.634649,-3.543309,7.227059,-0.178970,1.861664,-2.462618,7.028915,8.914571,-7.472448,0.753639,0.256600,-0.635594,-3.111369,9.657490,-4.508299,-1.852617,-8.234830,9.761562,-0.031161,1.499815,-7.906303,7.430111,-0.968041,-3.627694,7.960624,0.185840,-1.867506,1.942491,-1.760959,-8.470192,-4.890809,4.849963,6.424660,-7.422544,-5.077385,-7.446438,3.423726,4.373211,-0.835549,0.674351,4.187582,-3.674516,-5.703856,-2.831022,-5.753954,9.613413,-5.080729,4.750519,5.979752,2.155203,-8.263420,5.095331,4.312277,1.340599,-4.744939,1.309912,1.940910,6.094746,-3.350357,7.169805,6.663586,7.464671,5.588760,4.423309,3.108308,5.562153,-7.591131,2.057885,5.398956,6.228412,5.630709,5.068598,-7.785321,-3.312574,-5.623076,-3.751444,4.915428,3.141210,-0.091666,9.173845,-9.655480,9.990702,3.709706,-6.253227,1.894091,-1.319785,2.471600,-1.667593,4.593983,-6.595322,-6.179277,9.022171,-3.266315,-1.315358,5.145574,-5.251389,-1.728922,6.428197,7.344443,-6.534665,6.836185,0.699670,-4.249254,3.643699,4.404568,-0.805674,-5.103525,5.588259,-8.413096,6.317783,3.924007,1.611556,-2.329174,-3.096772,7.118164,-5.841980,5.519132,6.859593,6.398338,1.411963,-3.242674,-8.855310,7.878844,0.522239,-8.762531,-0.107561,9.941129,3.791986,-5.851041,3.587464,1.944357,-7.923057,2.990384,-1.548360,-8.892033,9.264281,6.725641,4.680199,4.257348,2.851746,-5.440874,-4.875276,9.066014,6.370510,0.066910,0.792403,-9.967692,3.176965,2.461639,5.436523,-0.804595,-7.682252,-6.264791,-2.842055,2.604564,5.146303,5.682021,8.645907,-7.583470,-9.244547,8.937129,-1.241180,-0.977809,5.736091,3.835813,7.094319,-6.493897,-1.522978,-5.166666,-5.774916,-2.686493,8.472151,2.835297,-3.546435,5.441251,3.592006,5.512766,-7.085724,-9.280757,7.568338,-1.779250,7.145360,9.963568,-0.153360,-5.608577,2.060982,-8.293090,2.242737,3.446358,0.019749,-1.143937,8.937730,-9.043521,0.563831,2.039289,8.871573,-6.564442,-4.958508,-8.673355,9.674859,-7.670336,8.305007,2.913120,-3.813467,-7.156809,2.073723,7.920505,-4.702064,-2.321546,-6.381954,0.171181,-7.814489,-6.633997,1.986194,1.884580,1.744163,5.945610,-1.034851,5.386504,3.944942,2.458633,9.416694,3.510677,-6.158019,0.667120,7.379547,-9.444643,-9.314906,9.107586,7.157287,-8.920002,-9.384055,7.917256,-3.002768,8.848102,0.268770,-1.870202,8.687730,-6.630240,-8.576183,-1.069131,-7.630958,8.834986,2.113694,-9.094106,5.628542,-3.118321,-3.129251,-5.120952,-4.637047,-2.178644,-4.290039,-5.554236,-6.306110,-1.422070,8.822355,7.295952,3.344757,-9.338775,6.717850,-6.707488,-5.915354,-4.767618,-9.849596,6.473007,-6.627298,-0.903750,7.472202,9.393789,-6.060365,-3.358511,-0.908986,4.136189,-6.287499,8.161963,5.740315,-9.334028,-1.534625,-0.419547,5.246731,1.685421,-6.062911,6.150438,6.218264,6.415368,-2.700920,6.333894,3.169644,-4.570984,-6.194672,8.405264,3.642971,3.181951,-7.763411,5.204462,-1.027036,-1.699619,-5.971397,-7.771505,-9.723862,9.668674,4.355221,4.222945,-8.616912,-5.074296,4.650718,-8.489083,5.129532,-5.366317,8.292369,0.960073,5.679462,-5.249117,0.305879,9.405725,5.463010,-6.336256,0.031721,7.080567,-9.315690,-1.852598,-1.264793,-9.336566,3.983519,1.615474,-7.013714,-8.602521,-1.656052,-6.091805,0.981557,3.156188,-3.564432,3.818371,-0.982189,0.976835,-8.493177,-8.165570,-5.247939,-9.079901,-8.217065,1.417529,-0.930535,-2.514150,-3.254892,6.627511,-7.733930,-1.395862,-2.642496,-3.661045,2.067736,7.169162,1.151940,-3.893435,6.456334,7.495046,-0.004087,-3.322797,-8.580389,-4.181157,9.369345,-7.259348,-4.009883,7.177461,-2.253924,9.978857,0.468960,6.417534,7.256477,4.250183,-4.176607,-5.937225,9.075563,-4.225005,2.064244,-9.256680,-2.544495,-8.372200,-7.229564,6.939885,2.158125,-0.502292,-0.676752,4.556091,5.869763,-5.453722,-1.774734,-2.517277,2.103524,2.522500,7.716083,-1.796045,4.971701,0.878595,-7.872633,-1.987134,3.020819,-1.819354,3.562409,0.989060,-7.220970,-9.119984,-2.145360,-9.776567,0.524942,-3.095309,-3.538711,-3.849114,4.595999,3.319172,6.812915,5.183190,-1.936594,-3.985217,-7.599973,-5.801799,8.002493,1.494646,7.790531,2.174600,2.904422,-6.695693,-2.316802,5.591381,-9.082543,6.271838,2.043663,-6.583420,7.640123,4.058428,4.695853,-4.366722,-9.004378,-2.484181,-2.005926,5.990579,-7.515694,5.618564,-9.797218,-6.735940,0.551078,-3.866229,2.766233,-4.472814,5.880023,-8.666928,7.750476,2.207904,-2.002768,4.025208,-5.681750,-0.874177,-8.425631,3.374848,8.312549,8.482146,-0.386848,0.453916,4.127166,-6.392932,4.861104,6.308403,1.383564,-9.366125,-3.268590,-3.736861,-0.812297,3.882551,-6.864073,-7.656473,8.703898,-5.807027,1.378394,0.313469,8.778391,-9.152301,-2.533117,6.784728,-9.874960,6.477107,-3.434564,1.935340,-4.144226,4.146077,-2.348962,-5.473966,-1.557926,0.659728,-5.120489,-1.460049,-4.476686,-6.449414,-9.355656,-8.476322,-6.619781,3.920498,-3.885375,5.883387,-1.197656,8.739454,-8.718036,-3.814218,4.142927,4.490568,-2.971021,4.692370,-7.800095,2.420323,-6.035275,6.800774,2.357479,0.469760,-2.139348,-2.483026,4.906713,6.528942,-9.259764,-5.416278,4.954932,0.596631,0.956448,-4.191013,0.580978,-3.578587,4.258280,-5.656648,2.156331,-2.999854,-7.606970,-5.342503,0.109818,-5.092346,2.772299,1.957874,-4.495499,-1.832069,6.829680,9.670257,-1.249281,-1.201839,5.022214,-2.561669,-7.592173,-9.860427,4.799391,6.031940,-8.690675,-4.071026,-6.655956,-3.190915,3.751261,1.447614,3.176476,9.852337,-9.831235,-1.948338,-7.294339,-7.153087,7.586855,6.591150,5.431478,8.461854,-8.174052,2.347489,9.198081,7.881498,-4.306850,-1.682988,7.555079,1.711048,6.730923,-3.824151,-1.519795,2.205570,3.954048,7.885525,3.169586,7.290490,-1.854484,-5.577380,-5.405526,-6.943107,-8.309355,7.144393,-8.896808,-8.920753,-6.639754,2.940652,2.557456,-2.706748,-3.504173,-5.085183,8.444141,0.887748,-8.833526,5.242524,-0.138971,-7.961869,-7.727467,-5.015655,-2.031544,9.429163,8.438372,-9.654487,8.499889,-1.736172,-7.637849,9.183809,-5.437621,9.350109,-8.833478,8.886690,5.785020,-2.264986,3.016438,-8.912289,1.296470,-0.813806,5.371913,5.232913,-2.555046,-2.465927,-2.818793,-6.859981,-4.399393,-9.318027,-5.134894,6.560442,5.304837,-6.085251,0.773316,-7.177223,-2.079535,9.042356,8.228593,-7.343995,-9.991676,-1.805894,-5.877852,3.968331,1.180653,2.308831,-1.055574,7.851879,-7.517947,-4.042344,-7.296182,-2.169846,-7.955842,-6.295775,2.646745,7.813652,8.660099,-6.372593,-7.437134,7.884391,6.683918,8.503126,9.662687,5.681292,-7.740102,2.638507,7.378344,8.012760,-3.575341,7.130266,-5.690755,2.632239,9.415483,0.784928,-3.937365,5.385060,-2.085405,3.871798,3.773244,4.014337,-1.828426,-6.065242,2.331180,2.395658,-0.861233,6.628334,2.364361,-6.605745,-7.243805,-1.977348,-7.374719,9.387746,8.950546,2.424990,2.277512,-4.090107,5.111345,5.635977,9.095110,-6.551745,-5.816319,-0.709716,4.926728,-3.845303,9.391187,-7.729078,-3.159846,-8.209616,-3.986218,-3.555679,-2.328937,2.177277,3.071164,-1.987414,-5.117468,-8.090314,-3.471139,-9.946808,-6.603949,-8.615638,-7.833211,2.989971,-7.792196,-8.593336,9.570902,-7.464785,0.427815,-1.069732,5.728415,6.394157,0.595389,-0.020144,0.334702,7.018988,0.134299,8.419303,-9.040230,-7.918446,-5.467029,7.514986,2.289567,1.021589,-9.344872,4.884700,9.735282,2.517292,2.959672,-8.017610,-0.285324,-7.799289,0.371854,9.233185,-6.614611,-1.690605,-1.975248,5.682710,-3.141237,5.355687,-4.692285,-9.501204,0.426630,-9.043291,0.524053,7.346626,7.940263,0.231048,2.467694,-2.940416,-7.602246,-7.480742,3.921741,-0.802444,6.761495,-5.657799,-4.695891,1.546066,-0.228168,-5.411690,-8.822946,2.752394,1.275355,6.040393,-6.907124,3.037397,-8.617162,8.327558,3.415671,3.744118,3.346710,-2.060173,-1.701745,-6.643634,4.537498,-4.588598,-1.194759,1.555026,-2.718754,3.913913,6.246190,7.990280,-4.787041,5.310113,-1.183089,-8.985868,-6.769124,-9.130307,-8.884760,9.329167,3.697952,-4.018219,5.014225,-2.881953,-5.128657,-4.708013,-8.585178,3.781271,5.306590,-6.438737,-3.188816,4.853250,6.178132,1.305948,-0.703768,4.752223,4.084368,-9.661137,-7.191292,-7.841727,-9.132352,-8.967795,3.918329,6.735823,-3.297687,-0.913660,2.947083,1.795237,6.103269,-7.259933,2.353444,-4.309041,5.287420,6.418605,5.058956,-7.306491,0.255926,-2.081318,8.791696,1.035002,5.000480,-0.419100,8.468551,4.678315,-4.493827,5.603644,7.796058,-5.001019,-5.536391,-1.122220,-0.857585,3.897525,0.230686,-7.081089,7.360828,-7.720350,5.630548,4.877579,-2.307148,-9.320027,7.601348,-6.044844,8.112901,2.008299,3.232969,4.785614,9.154557,9.768864,-5.248925,7.039834,8.975327,-2.352900,-5.721428,2.581290,-6.825400,1.392595,2.799201,-7.852317,6.699353,-1.532812,-9.288264,-8.592878,-3.939284,-9.701389,6.796038,3.711791,-5.912773,0.919903,4.208798,2.544019,-0.554144,4.701841,2.066959,-5.603697,-4.180659,2.624234,-4.110593,-1.984774,2.444047,7.336440,-6.206781,8.986473,-9.168456,6.541843,8.645517,6.834305,0.597610,-1.746304,9.435189,5.718129,2.498144,-8.982652,-7.928593,7.200426,3.713112,-0.931080,7.249211,-1.395669,8.930725,9.321855,4.935777,-7.524012,-4.548451,2.731811,-2.191159,9.242685,7.556148,4.062746,-2.819082,2.660373,-6.935682,6.655128,9.945565,2.620891,6.143657,9.286679,-5.045627,6.394099,-7.015223,-5.771769,-0.897872,0.588744,9.425136,1.830055,2.415472,3.358564,3.596265,7.438093,7.536598,1.713535,2.525870,9.994397,-1.406655,-4.284101,1.035195,2.079285,-5.526917,5.549619,-8.512937,4.683448,8.967444,2.461479,5.827248,1.057050,1.179587,9.375669,2.760501,-2.386820,-7.295183,6.856475,3.903469,7.718542,7.688514,1.824697], dtype = "float64")#candidate|8002|(1280,)|const|float64
const_8003 = relay.const([-5.066560,2.135988,3.692842,-2.334288,9.727195,8.716500,-9.438659,1.756111,3.598919,-2.596344,3.664903,-5.100657,-6.001426,-2.084172,7.185437,-2.545380,-2.881485,1.870214,-6.450949,0.820518,-6.442772,-6.241237,-4.771166,0.127106,-3.161919,9.674414,6.686651,-9.507039,0.238543,1.312718,-0.547747,-9.615941,-4.829686,-1.819316,1.174512,-6.719972,5.043341,-0.419093,-1.887459,3.769726,4.798687,9.270431,-9.822045,-7.706823,-1.792906,-1.561195,3.047546,-3.152255,0.443493,-9.509033,-9.233834,-0.960425,-6.665669,4.098317,-3.528051,9.644715,1.424247,-3.789964,7.065091,-6.555220,-3.622336,-1.181245,9.109605,4.417424,-4.052820,-0.936997,6.711376,-9.242953,0.164310,-0.118958,-8.744197,-3.133972,-6.095044,6.326111,8.580227,-8.626460,7.154326,-0.618895,2.933286,1.692795,7.523049,-5.508638,-5.249603,-7.916441,-6.935253,1.967070,8.441338,3.042241,-5.432659,4.762785,-6.547833,9.317790,-8.096677,-7.284805,-4.155250,4.638515,1.657821,-8.481155,-2.244944,-0.603473,0.556292,8.292986,1.210351,1.899278,-1.870692,1.382568,-6.568509,-6.317152,-6.235115,-7.232983,-8.160370,3.201255,5.280403,3.647055,-3.317325,-6.446794,0.769838,-5.779759,-1.340455,-3.803640,-1.918678,3.221365,-8.530103,-9.538674,8.875517,6.185274,-1.652019,1.904312,-1.217413,-7.753310,-4.911044,8.639171,-8.924336,-9.100972,8.874099,0.799685,7.611627,-1.878277,-0.998902,-7.162299,4.611931,2.657416,-7.679402,0.424931,9.416540,-0.406840,-7.009322,6.680421,4.371829,-5.201722,-8.157961,8.307269,-1.731900,-5.763243,-1.341497,-4.220428,-6.509924,5.268195,1.278865,-4.342533,-6.700367,-2.335052,-1.586487,-0.048956,-3.964839,-8.809335,-3.729755,-1.944303,1.278787,-4.368524,9.360569,2.510020,-8.940950,2.255988,8.792700,8.314280,-2.405134,-8.384624,5.360663,-2.934515,9.282228,4.540446,-6.022656,9.302955,-9.729344,9.020972,-5.725726,8.964918,-6.143553,-1.606828,-8.276878,6.738219,-3.719809,6.313063,-3.039122,1.076538,-4.313646,-2.217626,-2.448955,-8.392355,3.524637,-1.495906,-9.463279,-8.423880,-5.421636,-9.893892,-7.078497,7.104408,-1.509564,0.237357,4.397878,-3.193901,0.302768,-3.101282,-2.339092,-8.930011,8.494136,-1.419468,-9.124523,-5.563651,1.891613,-4.133385,-9.301218,-2.543688,-9.484841,-8.206565,-0.960429,-3.688144,5.260878,3.890976,9.466757,0.073511,0.952881,4.761708,-9.290456,-9.508065,-5.531728,-1.589745,8.657403,2.971163,-3.947072,2.014050,4.772921,-4.858795,-9.768560,-4.884777,1.938643,-9.517266,2.637290,-2.365102,6.668602,-1.653017,6.186208,1.879968,2.328456,9.223439,-2.034384,7.468744,-4.810496,-8.438616,7.994732,-6.633544,-2.520634,5.180203,-1.626036,0.887270,7.508313,-5.758892,-4.739821,6.297580,-5.245404,8.971035,5.244400,-2.237366,-5.320679,-2.007773,-7.402133,-7.143781,-3.431784,-0.857243,-1.045388,-5.047176,5.459178,-1.169419,-8.814123,-9.810001,-9.913993,4.243494,-7.978328,7.711050,-6.285005,-0.061776,8.590349,8.132442,0.138796,-0.432838,-6.075922,9.117397,0.791235,5.504939,2.283442,3.564046,-8.375629,5.656936,-8.754695,9.854999,-3.599616,9.856744,3.513826,0.083840,8.784590,-6.827887,2.610234,1.534973,0.784605,-9.679693,-3.773843,3.907508,2.841801,3.111439,1.944198,-2.302040,6.668988,5.807005,3.946167,4.755270,3.307979,-6.101212,5.454495,5.131677,-1.098397,6.866287,4.452603,2.410979,8.233472,4.948837,-7.331151,-1.728553,6.310805,-2.018489,0.382402,8.508731,1.459063,3.030834,-6.636372,5.111428,-3.142580,4.796902,8.355497,-8.947128,-1.523558,-5.561127,-4.168005,-7.211156,-0.747305,-8.835769,-0.811758,-5.831354,2.454444,-0.004751,4.515585,-0.875050,-5.635354,9.667291], dtype = "float64")#candidate|8003|(364,)|const|float64
call_7997 = relay.TupleGetItem(func_6131_call(relay.reshape(var_7998.astype('bool'), [15, 3, 7]), relay.reshape(var_7998.astype('bool'), [15, 3, 7]), relay.reshape(var_7999.astype('float32'), [780, 1]), relay.reshape(const_8000.astype('float64'), [18,]), relay.reshape(const_8001.astype('float64'), []), relay.reshape(const_8002.astype('float64'), [1280,]), relay.reshape(const_8003.astype('float64'), [364,]), ), 15)
call_8004 = relay.TupleGetItem(func_6140_call(relay.reshape(var_7998.astype('bool'), [15, 3, 7]), relay.reshape(var_7998.astype('bool'), [15, 3, 7]), relay.reshape(var_7999.astype('float32'), [780, 1]), relay.reshape(const_8000.astype('float64'), [18,]), relay.reshape(const_8001.astype('float64'), []), relay.reshape(const_8002.astype('float64'), [1280,]), relay.reshape(const_8003.astype('float64'), [364,]), ), 15)
output = relay.Tuple([bop_7979,uop_7994,call_7997,var_7998,var_7999,const_8000,const_8001,const_8002,const_8003,])
output2 = relay.Tuple([bop_7979,uop_7994,call_8004,var_7998,var_7999,const_8000,const_8001,const_8002,const_8003,])
func_8005 = relay.Function([var_7978,var_7998,var_7999,], output)
mod['func_8005'] = func_8005
mod = relay.transform.InferType()(mod)
var_8006 = relay.var("var_8006", dtype = "int16", shape = (13, 8, 3))#candidate|8006|(13, 8, 3)|var|int16
var_8007 = relay.var("var_8007", dtype = "bool", shape = (315,))#candidate|8007|(315,)|var|bool
var_8008 = relay.var("var_8008", dtype = "float32", shape = (780,))#candidate|8008|(780,)|var|float32
output = func_8005(var_8006,var_8007,var_8008,)
func_8009 = relay.Function([var_8006,var_8007,var_8008,], output)
mutated_mod['func_8009'] = func_8009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7124_call = mod.get_global_var('func_7124')
func_7125_call = mutated_mod.get_global_var('func_7125')
call_8059 = func_7124_call()
call_8060 = func_7124_call()
func_3038_call = mod.get_global_var('func_3038')
func_3041_call = mutated_mod.get_global_var('func_3041')
const_8072 = relay.const(-4, dtype = "uint16")#candidate|8072|()|const|uint16
const_8073 = relay.const([9,1,8,8,1,10,-6,-10,10,-5,3,-5,5,-2,-10,6,2,7,-3,7,2,3,2,5,5,3,2,-4,-1,-5,9,10,-1,3,-9,-7,8,9,3,1,3,-6,1,1,-8,3,-8,-1,10,-2,-4,2,-10,1,-4,-1,-8,4,-9,-1,1,-4,-7,-9,-1,-5,-1,9,7,-5,4,-10,3,2,-10,8,-9,2,9,10,-6,5,2,-1,5,10,1,4,5,-5,10,-8,-6,-2,4,5,9,-9,5,9,-5,-9,-10,-10,8,-2,9,-5,10,1,1,6,-7,2,5,2,-2,-6,-2,9,-2,-8,1,-7,3,9,-4,-6,9,3,-9,2,5,-6,-4,9,-8,-6,-2,-1,1,-3,-4,7,6,5,-6,7,-7,-10,-7,-5,-8,3,-6,-9,6,-3,10,6,-2,3,10,-3,2,5,4,6,5,-6,-6,7,6,4,9,-1,-3,-3,4,-9,9,10,6,-9,-5,-1,9,-7,-5,2,1,7,8,6,-5,-2,8,10,-6,-6,-4,-4,-2,-10,1,3,5,-7,-1,9,-7,10,1,-1,9,-7,-4,-7,-1,-5,1,6,7,1,4,4,8,-9,4,-5,-9,7,5,-10,-5,1,-1,1,10,-8,1,8,-5,-10,6,5,10,-9,-10,-5,3,8,-3,-4,1,9,-5,3,3,1,1,-5,10,7,-2,-4,8,-1,-10,-6,-8,-5,10,-2,-3,4,-1,-4,4,10,6,3,5,-9,-6,8,-9,-6,2,4,1,9,7,-2,7,-7,5,10,-1,-6,3,-2,6,-1,-5,4,-1,7,-6,-8,-2,-7,2,-8,-4,1,-8,-10,-10,5,-6,-3,-1,4,1,10,7,-2,-3,-4,-7,-6,10,3,7,-7,-6,9,-1,7,-4,-5,4,-2,10,-6,10,3,-8,-2,-4,-7,9,10,-8,2,-3,5,-6,4,2,4,4,2,6,6,-2,10,8,1,-6,9,2,7,-10,4,3,-4,5,-8,7,-1,-8,10,3,-1,4,10,-6,4,8,-8,5,-7,-5,1,2,2,-7,5,4,10,-7,-4,5,-9,-5,3,8,-10,8,6,5,9,10,1,1,-2,2,-3,3,10,-8,7,7,-8,1,5,4,10,-8,-8,4,9,-5,3,-4,-5,7,8,-9,9,2,8,5,-10,8,-4,-7,8,-7,9,5,-4,7,-8,-10,-8,10,10,3,2,9,4,1,5,5,9,-9,-6,-7,-3,-3,3,7,1,-5,-1,-1,8,9,9,-9,-7,3,5,10,-9,10,-8,-7,-9,4,-7,-7,6,-2,3,7,-10,-3,-2,-4,8,5,3,9,-4,-3,9,-8,9,1,-1,-2,-9,-9,-10,2,-7,5,8,-3,6,-3,-8,-9,-3,7,-9,7,3,-6,9,10,4,-7,7,5,7,-6,9,10,-6,-7,5,10,10,-1,-6,8,-6,2,-6,-5,-5,6,6,7,2,-6,8,6,-4,8,8,9,10,7,8,-8,5,-6,-9,-5,-5,-9,7,-2,10,8,-7,-4,-10,-4,1,9,6,-8,-8,-8,-2,-7,-10,-7,-10,-2,5,5,-5,2,-3,-3,-8,-3,-2,1,-8,4,-9,2,-7,8,8,-5,-4,-8,-10,5,-2,2,1,-9,-4,-9,-3,2,-3,3,-6,4,-7,-7,3,-3,-10,10,-10,10,-1,7,-8,-7,-1,-4,-9,7,1,3,5,3,-10,-7,-2,-4,-6,1,10,-6,-8,-10,-7,3,2,-5,9,-2,-1,-1,6,9,6,5,-8,1,-1,1,9,-7,-9,7,10,-8,10,5,-7,-9,2,3,7,6,-4,-6,-2,-3,7,10,3,8,9,3,-8,3,8,-2,9,-1,-4,7,1,-8,3,-6,5,-2,-9,-4,-7,7,-2,-10,-6,5,1,-7,-5,-9,-2,-5,-8,5,3,-4,-4,-8,9,-7,-1,4,-6,4,-7,-8,-9,8,-3,5,-10,-6,10,-1,2,-6,2,-6,-3,8,5,-9,-2,-2,-9,8,-7,-6,-8,8,6,-4,-3,5,-3,6,-10,10,3,6,10,3,-8,-4,7,6,-7,-4,-3,6,3,-5,10,-6,9,7,5,5,-1,2,5,3,-10,-10,-5,10,2,-4,3,5,1,-1,4,-2,7,2,1,1,2,6,-2,7,4,-6,1,-8,5,-1,-5,3,6,-3,-1,-10,-10,10,5,-5,9,7,-7,2,-4,3,5,-3,-9,10,3,-3,-6,-4,-10,-1,4,-7,-3,-3,2,-6,9,-8,6,-10,-7,3,-6,4,7,3,1,10,-10,1,-8,9,-6,10,6,-2,-3,-6,-3,-6,-8,-2,10,-5,7,-2,-2,-6,9,-2,-6,-10,1,-9,-8,5,-4,7,10,-6,-7,-6,1,-1,6,9,-10,-2,-5,-7,5,-1,10,-7,-9,9,-1,-6,7,-7,3,-4,5,5,-6,-4,-6,-2,-2,-9,1,-8,-5,9,4,-4,1,9,3,-5,8,-9,-4,-1,1,-9,9,7,2,5,-3,2,-4,-10,-6,-5,-4,-1,7,-5,3,5,1,-8,-9,10,10,3,-4,-3,10,7,4,2,-1,2,-1,7,-8,-7,-6,8,-1,-1,6,7,2,9,3,7,-10,-9,-7,-5,9,-3,-8,-2,4,6,-9,-7,9,7,9,8,-5,4,-3,-9,2,-9,5,-1,-7,2,-8,-5,8,10,7,9,-5,8,-2,10,10,-4,1,7,-2,3,9,8,-1,-5,6,-4,8,9,-8,-4,10,-5,-5,8,3,-7,9,-8,-6,1,-8,3,7,-6,2,-3,-9,-3,3,2,-3,8,6,4,-10,2,-2,-6,8,1,-3,10,7,6,5,5,7,-3,9,3,-4,1,-1,-2,10,-8,-2,-7,-4,-8,-1,8,-6,10,-8,-7,9,8,-7,-8,-8,10,-7,-6,1,9,-6,-9,7,8,-2,10,4,-1,10,8,6,-7,-6,-3,6,-9,8,-5,-7,10,9,-1,8,4,1,-6,-1,-1,6,3,7,-4,-8,-10,1,4,-10,3,-7,5,-8,-9,6,5,6,-5,8,10,10,2,-9,-1,3,6,10,2,-4,6,-10,3,-9,-1,-10,6,10,-1,-6,8,8,-1,-5,8,-3,7,-7,1,1,-6,2,2,10,1,-8,7,-2,6,-3,-5,1,10,-6,-6,5,-9,4,1,5,-1,-2,2,-9,1,5,8,10,5,-1,3,5,-2,-1,4,-4,2,-5,10,-5,8,7,-5,6,-4,-3,10,9,8,5,-10,6,5,-6,-7,-7,10,-3,-2,-7,5,-5,9,-8,-4,8,4,-5,7,-5,4,-1,6,1,2,-6,7,3,5,-2,6,4,8,-8,-3,-1,-5,-1,-6,-10,-10,7,-10,-3,2,6,9,-8,9,4,-9,9,9,6,4,-6,-4,2,-3,-1,-4,5,-6,10,8,-7,9,2,8,3,-4,6,2,-4,-3,-10,-1,-10,-9,-2,6,-6,5,-1,8,3,-3,-1,-5,9,-9,6,-7,7,-1,-3,-6,10,-8,4,-6,-7,-6,-5,-3,-10,7,-2,-6,-10,-6,2,1,5,4,5,-6,3,3,2,6,8,-2,8,7,-5,-1,9,10,1,-5,7,3,3,8,1,9,-7,-8,-9,5,10,-2,5,-4,7,7,1,4,7,9,-7,-7,-9,1,4,1,-1,-4,6,-7,5,7,-5,10,-4,-9,-7,-7,-3,-4,6,10,10,-4,-2,-9,6,-5,-8,10,-5,-5,7,-1,-2,-9,2,-8,5,-1,4,6,-8,8,7,8,-10,4,-6,-10,-10,9,-10,8,-10,4,9,-1,-2,-2,8,1,-4,-5,-10,1,6,5,6,3,2,-9,7,9,10,8,-5,5,-4,2,-7,-7,4,9,5,7,9,-10,5,-8,5,2,-5,-1,-1,-4,-7,-3,10,10,-6,-3,-2,-3,-6,-3,-7,9,6,-2,3,5,-4,1,-2,9,10,3,9,-1,9,4,-9,-9,-4,-1,-6,7,7,-3,-8,5,8,-10,-5,2,4,-1,10,9,-10,3,9,5,-9,-4,-5,-7,-6,10,9,-7,-9,-10,-8,-4,-1,6,6,-5,2,-4,-8,-9,-9,8,-10,-2,1,7,1,10,8,-10,-9,-3,-4,-7,-7,9,-5,5,1,-6,9,4,7,-10,7,-1,-8,-7,-1,-7,3,6,2,-7,1,5,-9,10,2,10,1,-8,-8,-1,1,9,3,-6,-9,8,-6,-9,-2,10,-8,-5,-4,8,-8,-10,9,5,-7,5,-3,7,7,-4,-3,-5,5,-10,1,-10,8,-7,3,7,2,7,6,-5,-8,-2,-1,1,-6,-4,8,-5,-6,-1,6,-9,1,-6,-10,2,7,-10,-10,6,-2,3,4,8,10,-1,9,-7,-7,-9,-1,8,4,8,-1,-10,-5,-4,-10,-3,2,-9,5,3,-8,-3,-3,8,-1,1,-3,4,3,8,-10,4,-6,-5,8,5,10,6,10,-9,2,-10,1,2,-4,7,-3,8,-3,-10,-10,-8,4,-4,-6,3,4,-3,-7,-9,9,-5,-9,2,5,-3,-7,-7,-5,-5,-3,10,-2,-2,-10,-10,-9,1,-9,9,5,10,3,2,6,10,6,7,-3,-6,10,-1,-2,-6,-5,4,-9,1,4,1,-3,-1,8,-8,5,-3,-2,5,-7,5,-9,10,-5,-9,6,-9,10,-7,-8,-9,-9,-9,9,4,-8,-9,-8,-3,2,4,-4,5,4,2,7,4,-8,-6,8,4,-9,-3,2,3,-7,-9,9,5,-8,-5,10,2,2,-4,9,6,-9,-6,4,4,-6,4,-9,-1,6,1,-5,4,2,-10,4,-9,-7,-3,-6,-4,-9,10,-7,-6,-6,9,-9,-1,-10,2,-6,-6,-9,4,7,-10,6,6,-10,6,-9,-9,9,1,-10,-3,5,-1,-10,10,5,-4,9,-2,-2,6,5,-2,-7,2,-6,-8,-6,-5,-6,-4,2,-9,9,1,2,-3,-7,1,-7,-3,-10,4,-10,2,4,4,-5,-9,8,6,-9,9,5,10,-3,-3,-2,8,-7,-5,-8,7,3,10,5,-3,6,-10,10,-2,-3,-5,-3,-6,-1,1,1,5,-3,-7,-10,5,-2,8,5,4,-5,2,2,-8,10,-4,-7,-6,3,-3,6,2,2,-10,10], dtype = "uint16")#candidate|8073|(1950,)|const|uint16
call_8071 = relay.TupleGetItem(func_3038_call(relay.reshape(const_8072.astype('uint16'), []), relay.reshape(const_8073.astype('uint16'), [13, 10, 15]), ), 2)
call_8074 = relay.TupleGetItem(func_3041_call(relay.reshape(const_8072.astype('uint16'), []), relay.reshape(const_8073.astype('uint16'), [13, 10, 15]), ), 2)
uop_8081 = relay.log(call_8059.astype('float32')) # shape=(3, 11, 2)
uop_8083 = relay.log(call_8060.astype('float32')) # shape=(3, 11, 2)
output = relay.Tuple([call_8071,const_8072,const_8073,uop_8081,])
output2 = relay.Tuple([call_8074,const_8072,const_8073,uop_8083,])
func_8097 = relay.Function([], output)
mod['func_8097'] = func_8097
mod = relay.transform.InferType()(mod)
output = func_8097()
func_8098 = relay.Function([], output)
mutated_mod['func_8098'] = func_8098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6922_call = mod.get_global_var('func_6922')
func_6923_call = mutated_mod.get_global_var('func_6923')
call_8114 = relay.TupleGetItem(func_6922_call(), 1)
call_8115 = relay.TupleGetItem(func_6923_call(), 1)
var_8126 = relay.var("var_8126", dtype = "float64", shape = (11, 11, 15))#candidate|8126|(11, 11, 15)|var|float64
bop_8127 = relay.mod(call_8114.astype('float32'), relay.reshape(var_8126.astype('float32'), relay.shape_of(call_8114))) # shape=(11, 11, 15)
bop_8130 = relay.mod(call_8115.astype('float32'), relay.reshape(var_8126.astype('float32'), relay.shape_of(call_8115))) # shape=(11, 11, 15)
uop_8137 = relay.asin(var_8126.astype('float32')) # shape=(11, 11, 15)
uop_8144 = relay.sin(uop_8137.astype('float32')) # shape=(11, 11, 15)
func_1409_call = mod.get_global_var('func_1409')
func_1412_call = mutated_mod.get_global_var('func_1412')
const_8149 = relay.const([5.453237,-1.055856,6.367029,-0.806162,2.327999,-2.312289,-2.502342,5.548412,5.800230,9.988925,-8.566309,4.191168,7.410218,-0.262915,5.983175,-4.859954,6.933831,9.177446], dtype = "float64")#candidate|8149|(18,)|const|float64
call_8148 = func_1409_call(relay.reshape(const_8149.astype('float64'), [6, 3, 1]))
call_8150 = func_1409_call(relay.reshape(const_8149.astype('float64'), [6, 3, 1]))
func_1324_call = mod.get_global_var('func_1324')
func_1326_call = mutated_mod.get_global_var('func_1326')
var_8152 = relay.var("var_8152", dtype = "float32", shape = (780,))#candidate|8152|(780,)|var|float32
call_8151 = relay.TupleGetItem(func_1324_call(relay.reshape(var_8152.astype('float32'), [6, 10, 13])), 4)
call_8153 = relay.TupleGetItem(func_1326_call(relay.reshape(var_8152.astype('float32'), [6, 10, 13])), 4)
output = relay.Tuple([bop_8127,uop_8144,call_8148,const_8149,call_8151,var_8152,])
output2 = relay.Tuple([bop_8130,uop_8144,call_8150,const_8149,call_8153,var_8152,])
func_8171 = relay.Function([var_8126,var_8152,], output)
mod['func_8171'] = func_8171
mod = relay.transform.InferType()(mod)
mutated_mod['func_8171'] = func_8171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8171_call = mutated_mod.get_global_var('func_8171')
var_8173 = relay.var("var_8173", dtype = "float64", shape = (11, 11, 15))#candidate|8173|(11, 11, 15)|var|float64
var_8174 = relay.var("var_8174", dtype = "float32", shape = (780,))#candidate|8174|(780,)|var|float32
call_8172 = func_8171_call(var_8173,var_8174,)
output = call_8172
func_8175 = relay.Function([var_8173,var_8174,], output)
mutated_mod['func_8175'] = func_8175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7124_call = mod.get_global_var('func_7124')
func_7125_call = mutated_mod.get_global_var('func_7125')
call_8252 = func_7124_call()
call_8253 = func_7124_call()
func_7482_call = mod.get_global_var('func_7482')
func_7484_call = mutated_mod.get_global_var('func_7484')
const_8262 = relay.const([-5,1,-4,7,-10,1,4,-6,-8,-9,4,-9,-1,7,3], dtype = "int16")#candidate|8262|(15,)|const|int16
call_8261 = relay.TupleGetItem(func_7482_call(relay.reshape(const_8262.astype('int16'), [15,])), 2)
call_8263 = relay.TupleGetItem(func_7484_call(relay.reshape(const_8262.astype('int16'), [15,])), 2)
output = relay.Tuple([call_8252,call_8261,const_8262,])
output2 = relay.Tuple([call_8253,call_8263,const_8262,])
func_8283 = relay.Function([], output)
mod['func_8283'] = func_8283
mod = relay.transform.InferType()(mod)
output = func_8283()
func_8284 = relay.Function([], output)
mutated_mod['func_8284'] = func_8284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7228_call = mod.get_global_var('func_7228')
func_7229_call = mutated_mod.get_global_var('func_7229')
call_8329 = relay.TupleGetItem(func_7228_call(), 1)
call_8330 = relay.TupleGetItem(func_7229_call(), 1)
output = relay.Tuple([call_8329,])
output2 = relay.Tuple([call_8330,])
func_8348 = relay.Function([], output)
mod['func_8348'] = func_8348
mod = relay.transform.InferType()(mod)
mutated_mod['func_8348'] = func_8348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8348_call = mutated_mod.get_global_var('func_8348')
call_8349 = func_8348_call()
output = call_8349
func_8350 = relay.Function([], output)
mutated_mod['func_8350'] = func_8350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8283_call = mod.get_global_var('func_8283')
func_8284_call = mutated_mod.get_global_var('func_8284')
call_8383 = relay.TupleGetItem(func_8283_call(), 2)
call_8384 = relay.TupleGetItem(func_8284_call(), 2)
output = relay.Tuple([call_8383,])
output2 = relay.Tuple([call_8384,])
func_8413 = relay.Function([], output)
mod['func_8413'] = func_8413
mod = relay.transform.InferType()(mod)
mutated_mod['func_8413'] = func_8413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8413_call = mutated_mod.get_global_var('func_8413')
call_8414 = func_8413_call()
output = call_8414
func_8415 = relay.Function([], output)
mutated_mod['func_8415'] = func_8415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6695_call = mod.get_global_var('func_6695')
func_6696_call = mutated_mod.get_global_var('func_6696')
call_8497 = relay.TupleGetItem(func_6695_call(), 0)
call_8498 = relay.TupleGetItem(func_6696_call(), 0)
func_6872_call = mod.get_global_var('func_6872')
func_6874_call = mutated_mod.get_global_var('func_6874')
var_8507 = relay.var("var_8507", dtype = "float32", shape = (780,))#candidate|8507|(780,)|var|float32
call_8506 = relay.TupleGetItem(func_6872_call(relay.reshape(var_8507.astype('float32'), [780,])), 2)
call_8508 = relay.TupleGetItem(func_6874_call(relay.reshape(var_8507.astype('float32'), [780,])), 2)
func_417_call = mod.get_global_var('func_417')
func_421_call = mutated_mod.get_global_var('func_421')
const_8526 = relay.const([5.451554,2.872617,4.563780,5.775282,-4.325598,-4.303380,5.810372,-8.733522,-9.314433,-2.177609,-1.903436,4.249250,9.037085,-5.532823,-8.308041,-3.659305,-0.559084,4.808749,0.118456,9.575726,-1.316606,1.881307,-0.574248,-2.017818,3.586080,6.293234,-0.909540,-8.100589,2.634790,-4.214452,-0.658458,-7.329588,-7.857053,7.005744,-7.743185,2.868300,-9.737310,-6.165363,-7.625318,4.093691,6.949155,3.176225,4.223448,7.839889,1.408449,-1.132059,4.304250,-1.903776,9.016441,0.172188], dtype = "float32")#candidate|8526|(50,)|const|float32
var_8527 = relay.var("var_8527", dtype = "float32", shape = (400,))#candidate|8527|(400,)|var|float32
call_8525 = relay.TupleGetItem(func_417_call(relay.reshape(const_8526.astype('float32'), [10, 5, 1]), relay.reshape(var_8527.astype('float32'), [10, 5, 8]), ), 0)
call_8528 = relay.TupleGetItem(func_421_call(relay.reshape(const_8526.astype('float32'), [10, 5, 1]), relay.reshape(var_8527.astype('float32'), [10, 5, 8]), ), 0)
func_7403_call = mod.get_global_var('func_7403')
func_7405_call = mutated_mod.get_global_var('func_7405')
call_8531 = func_7403_call(relay.reshape(call_8497.astype('float32'), [3, 11, 2]))
call_8532 = func_7403_call(relay.reshape(call_8497.astype('float32'), [3, 11, 2]))
output = relay.Tuple([call_8497,call_8506,var_8507,call_8525,const_8526,var_8527,call_8531,])
output2 = relay.Tuple([call_8498,call_8508,var_8507,call_8528,const_8526,var_8527,call_8532,])
func_8533 = relay.Function([var_8507,var_8527,], output)
mod['func_8533'] = func_8533
mod = relay.transform.InferType()(mod)
mutated_mod['func_8533'] = func_8533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8533_call = mutated_mod.get_global_var('func_8533')
var_8535 = relay.var("var_8535", dtype = "float32", shape = (780,))#candidate|8535|(780,)|var|float32
var_8536 = relay.var("var_8536", dtype = "float32", shape = (400,))#candidate|8536|(400,)|var|float32
call_8534 = func_8533_call(var_8535,var_8536,)
output = call_8534
func_8537 = relay.Function([var_8535,var_8536,], output)
mutated_mod['func_8537'] = func_8537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8413_call = mod.get_global_var('func_8413')
func_8415_call = mutated_mod.get_global_var('func_8415')
call_8564 = relay.TupleGetItem(func_8413_call(), 0)
call_8565 = relay.TupleGetItem(func_8415_call(), 0)
func_8005_call = mod.get_global_var('func_8005')
func_8009_call = mutated_mod.get_global_var('func_8009')
var_8568 = relay.var("var_8568", dtype = "int16", shape = (312,))#candidate|8568|(312,)|var|int16
var_8569 = relay.var("var_8569", dtype = "bool", shape = (315,))#candidate|8569|(315,)|var|bool
const_8570 = relay.const([[9.693742],[-2.416397],[2.987498],[8.870864],[-2.470828],[6.872202],[0.965315],[-2.488750],[-9.590066],[-6.952393],[8.578478],[4.014954],[-4.776699],[1.361045],[-1.700290],[2.689467],[-4.845428],[6.306829],[-0.872019],[6.303101],[-0.611805],[-8.269824],[-8.637607],[-2.502607],[2.341301],[-0.164328],[-7.760690],[2.352333],[-8.054174],[0.679223],[-4.281433],[3.331904],[-2.822995],[0.610994],[5.587261],[2.322734],[7.625566],[2.222097],[-9.551711],[-3.211219],[-8.774203],[-8.865540],[-5.662151],[8.158013],[-7.175192],[-0.612422],[8.589898],[6.336764],[-7.260129],[8.065353],[0.423915],[4.626617],[-1.935716],[-0.888459],[2.153944],[0.912160],[0.895518],[-4.363694],[1.936507],[6.786955],[-8.567914],[1.376342],[2.837893],[-6.203699],[2.847569],[2.391644],[-1.240615],[1.724309],[-3.943175],[-4.062076],[2.677206],[1.173085],[9.217286],[-7.601860],[-3.802840],[2.487171],[2.189259],[-2.593419],[6.805387],[-6.437544],[-1.820548],[-7.139268],[6.581251],[-2.534734],[1.445470],[7.527066],[-5.897937],[-1.284871],[-1.888362],[-6.484982],[-1.151003],[7.974119],[-2.205799],[-9.865693],[-2.571736],[-5.761748],[-2.290976],[-6.061330],[5.066303],[5.156090],[1.921084],[9.284061],[-5.485437],[2.772988],[-8.317692],[1.439472],[9.313061],[5.568207],[-3.096132],[-1.081152],[-0.870587],[-9.476267],[2.618629],[-1.566072],[7.585181],[7.266454],[-9.105407],[-3.217260],[-1.989250],[8.185101],[0.567965],[9.371325],[-4.363466],[3.474469],[-1.707367],[9.538064],[-8.833810],[-9.172663],[-5.854642],[-0.450544],[-2.714086],[-7.634124],[-8.686790],[5.614142],[3.671033],[-3.506942],[4.778569],[5.328395],[-9.668832],[9.059321],[-8.783423],[2.985273],[-6.813625],[-3.791687],[4.502322],[-0.021129],[1.145127],[-2.660088],[4.880608],[-6.617093],[2.408772],[0.441078],[5.538176],[-3.935562],[2.950376],[-4.701084],[-5.338142],[0.509850],[9.124269],[-8.605864],[-8.437376],[6.602641],[1.437893],[-3.258558],[7.617054],[7.882045],[6.723509],[-8.897447],[-0.294607],[-8.343236],[-6.307205],[1.496031],[-4.999144],[2.377398],[5.395283],[-3.446567],[-6.145253],[1.581203],[-0.310437],[-8.519744],[-4.218435],[-6.576727],[-7.618960],[-2.875878],[0.170648],[2.447910],[-5.315359],[-6.132306],[7.174472],[-7.364785],[7.780514],[-4.446941],[-7.911743],[-3.116819],[3.708601],[5.209903],[-8.589491],[3.610364],[-4.736409],[0.617407],[-7.649185],[1.491261],[-8.185602],[-8.147280],[3.014528],[-9.465052],[5.161607],[-9.843332],[-5.166710],[-4.947535],[9.654528],[4.238611],[0.856671],[-1.679799],[5.044218],[0.247482],[-1.871972],[-8.405277],[0.478242],[-6.367137],[2.090736],[9.454371],[-6.857667],[1.175196],[-5.263726],[-1.483167],[0.889707],[-3.237766],[6.909552],[-7.589138],[-2.877902],[-3.755276],[-1.867381],[3.116294],[7.381890],[-5.444206],[-2.051688],[-2.626244],[4.009311],[4.194370],[1.414255],[7.125229],[-6.940165],[-6.523642],[-0.457954],[-8.491332],[-5.945825],[-2.113324],[5.863246],[-7.985036],[3.769160],[1.054362],[3.304242],[-0.398370],[4.811939],[-6.285975],[-6.241584],[3.495265],[2.070648],[-3.217155],[-6.139927],[9.368428],[8.256558],[6.988402],[9.934341],[-1.873589],[-5.946440],[9.873068],[4.309338],[-3.869958],[5.826165],[0.200770],[-7.599858],[-9.988585],[-3.426644],[-2.484368],[6.531449],[-7.109087],[9.200877],[9.853165],[5.783250],[9.202666],[-3.776953],[6.791246],[2.448852],[-0.434321],[5.331381],[-8.655090],[1.912522],[6.972856],[4.410988],[-0.590370],[0.634649],[5.104920],[6.108953],[-0.002412],[-5.467625],[-3.575079],[-3.118248],[-2.029041],[-3.940210],[-2.067987],[5.215817],[1.203076],[-4.185018],[-1.332762],[-7.492077],[-3.625238],[9.433261],[-6.120094],[4.952776],[-5.435723],[8.333568],[-8.938758],[-0.172876],[5.504328],[9.464350],[-2.908232],[-9.887633],[4.956109],[1.776162],[-0.323392],[7.889201],[7.244239],[-8.631264],[5.233406],[-4.104295],[-0.317275],[-7.902322],[7.936838],[7.053669],[5.900821],[2.014045],[8.210821],[-6.292723],[-5.808904],[6.797198],[8.288346],[6.193753],[7.957839],[7.104840],[2.571507],[-4.725203],[3.452693],[-1.658222],[-1.643442],[2.059963],[4.399393],[0.120796],[-5.920752],[3.707164],[0.741170],[7.775875],[3.119880],[-7.128631],[-4.757783],[0.741802],[7.464717],[6.562278],[8.245984],[-1.547072],[-9.654569],[3.733717],[-2.619060],[-0.627219],[-7.289231],[7.287187],[-2.423058],[4.489731],[1.447394],[1.939108],[6.616658],[-9.450367],[-8.059043],[0.033618],[5.648308],[5.577762],[7.769169],[6.058058],[-0.798446],[-4.634364],[-4.261524],[-7.822059],[-8.462112],[-0.324366],[8.517534],[1.324352],[8.710322],[-7.490876],[-6.734412],[9.653917],[3.385819],[1.916409],[6.267416],[-3.155412],[-0.779158],[6.374838],[-1.380077],[-0.674970],[1.211161],[-2.187178],[-3.702597],[0.557249],[3.248621],[1.728354],[8.104021],[-5.592346],[-6.958367],[7.126364],[-9.930462],[2.326314],[-2.368929],[7.219361],[-8.003542],[1.665022],[6.490741],[4.079092],[7.169591],[0.401309],[-9.466596],[-9.104907],[5.800995],[-5.830203],[-6.899888],[8.134119],[5.620252],[-8.998913],[0.134169],[-4.398452],[8.732204],[0.798425],[4.350282],[-7.173916],[9.623557],[-7.026857],[-5.683885],[2.738720],[6.961342],[6.893810],[9.420351],[-9.867161],[7.236107],[-0.161222],[8.741059],[9.209630],[-3.606942],[5.449903],[8.233574],[7.313394],[8.827976],[-1.504363],[-9.998254],[8.579294],[4.971474],[-8.249415],[9.749521],[3.320081],[9.019652],[-3.248335],[-0.025180],[4.320130],[-0.217799],[-4.179781],[-7.524011],[1.928524],[7.737826],[3.978479],[8.511900],[8.946443],[-5.514474],[-3.367253],[7.356186],[-1.314172],[1.906180],[7.890622],[-0.393499],[8.313871],[6.003280],[-1.933799],[6.893345],[8.543084],[2.778835],[-2.927337],[8.034132],[5.552097],[5.621254],[2.574240],[6.807134],[5.945843],[-6.624314],[-9.659737],[7.863977],[-2.526980],[-2.882939],[-1.908665],[-4.317433],[-8.663279],[2.867408],[-2.235170],[5.679892],[-0.123979],[8.689761],[1.624553],[2.551866],[-7.777629],[1.450754],[3.941080],[-2.569003],[3.478589],[-0.590900],[-8.763271],[4.346185],[9.504793],[2.617116],[1.023845],[2.374938],[-5.118298],[1.478741],[-2.177203],[-2.387091],[2.069157],[8.682958],[2.043482],[-5.624780],[-3.896175],[-9.115008],[0.482104],[-2.315291],[-8.471764],[-8.343803],[-5.725136],[6.691884],[8.989592],[-6.533385],[-4.454189],[-7.348328],[-0.226036],[-4.204639],[3.206032],[-0.664349],[6.278944],[-0.761120],[-8.752347],[6.448755],[-0.573087],[-3.497691],[-1.848746],[9.442583],[-6.793162],[4.217471],[2.273954],[-0.713330],[6.891915],[0.330324],[4.869018],[3.022472],[-0.846318],[5.693738],[-4.078565],[-1.574497],[3.064386],[9.276589],[-1.108040],[8.411345],[-1.975505],[4.102325],[-3.861543],[9.977651],[-1.599864],[-4.437862],[-4.598000],[2.346871],[3.341995],[1.525552],[6.727227],[-9.266039],[-4.855532],[-0.815814],[2.509705],[1.490955],[-5.767826],[8.079218],[2.222314],[2.430979],[3.873419],[4.425925],[3.977245],[-0.900337],[-1.116165],[-5.588960],[0.243227],[-0.106736],[-3.024518],[8.327018],[-8.276801],[4.741753],[6.606656],[5.097903],[1.048382],[0.664712],[-0.660713],[-3.218685],[3.413342],[-9.403349],[-3.296484],[6.512254],[8.535158],[2.759369],[3.091573],[7.168506],[9.851833],[-8.197051],[0.359160],[4.979173],[-5.146812],[8.824546],[-3.998467],[-2.336840],[2.098661],[5.957246],[5.256709],[9.322336],[-0.762488],[-0.004046],[2.202701],[9.269427],[-7.227758],[-3.902258],[2.623963],[-4.468727],[-8.542187],[-8.248059],[7.259930],[-7.099018],[9.245276],[-6.722223],[-9.566107],[4.657990],[-1.410655],[-3.356738],[-0.910487],[9.171017],[-8.859610],[-6.461582],[2.602915],[9.612614],[7.831075],[-4.359069],[6.971546],[1.025602],[-9.767456],[7.982840],[3.173575],[9.355719],[9.447139],[-8.393935],[2.680882],[-4.026442],[8.770252],[7.108497],[-6.200547],[-6.813728],[-5.678393],[-5.601899],[1.683470],[-2.241502],[-1.133816],[-6.029059],[9.360012],[8.999612],[-8.929193],[-4.632632],[0.482415],[9.996350],[3.274393],[-7.782246],[1.008616],[7.411302],[8.859149],[7.579693],[3.186734],[6.983733],[-5.369479],[-4.524997],[5.019687],[-6.346517],[8.586377],[-9.255883],[1.748558],[9.698591],[-5.593055],[-7.038509],[-8.414184],[-8.805991],[-5.137687],[-1.141866],[9.464597],[2.532933],[4.850212],[7.684778],[7.134310],[-2.633830],[-5.059404],[-0.570201],[-3.440456],[1.912602],[2.329153],[7.861706],[6.443154],[9.534640],[6.322790],[-2.412724],[8.420957],[-1.576476],[1.717271],[-6.039070],[9.102980],[3.350939],[7.784152],[-4.810613],[0.958589],[-9.279395],[1.804639],[-6.375094],[8.827720],[-4.923401],[5.885512],[-6.507789],[-7.818234],[8.340929],[-5.202713],[3.427948],[0.272598],[-7.143154],[-7.827789],[-6.525304],[-5.215790],[-6.604705],[-9.144372],[-2.830824],[-2.297143],[5.491222],[1.339988],[5.679553],[-0.631623],[2.798479],[-6.555961],[8.312162],[6.951134],[-9.007045],[-5.646690],[8.708202],[6.622361],[-5.941955],[-1.194961],[-6.685596],[-7.936688],[-6.666934],[2.294123],[1.519489],[5.760501],[-7.361273],[4.875594],[1.774491],[3.391456],[-6.560571],[-6.630735],[-9.014228],[0.176025],[-8.310579],[-6.034398],[9.250957],[-4.603617],[-8.319691],[2.093313],[6.472199],[6.872311],[-9.215544],[1.502291],[1.747246]], dtype = "float32")#candidate|8570|(780, 1)|const|float32
call_8567 = relay.TupleGetItem(func_8005_call(relay.reshape(var_8568.astype('int16'), [13, 8, 3]), relay.reshape(var_8569.astype('bool'), [315,]), relay.reshape(const_8570.astype('float32'), [780,]), ), 4)
call_8571 = relay.TupleGetItem(func_8009_call(relay.reshape(var_8568.astype('int16'), [13, 8, 3]), relay.reshape(var_8569.astype('bool'), [315,]), relay.reshape(const_8570.astype('float32'), [780,]), ), 4)
func_6922_call = mod.get_global_var('func_6922')
func_6923_call = mutated_mod.get_global_var('func_6923')
call_8581 = relay.TupleGetItem(func_6922_call(), 2)
call_8582 = relay.TupleGetItem(func_6923_call(), 2)
func_7255_call = mod.get_global_var('func_7255')
func_7257_call = mutated_mod.get_global_var('func_7257')
var_8598 = relay.var("var_8598", dtype = "float32", shape = (66,))#candidate|8598|(66,)|var|float32
call_8597 = relay.TupleGetItem(func_7255_call(relay.reshape(var_8598.astype('float32'), [3, 11, 2])), 0)
call_8599 = relay.TupleGetItem(func_7257_call(relay.reshape(var_8598.astype('float32'), [3, 11, 2])), 0)
output = relay.Tuple([call_8564,call_8567,var_8568,var_8569,const_8570,call_8581,call_8597,var_8598,])
output2 = relay.Tuple([call_8565,call_8571,var_8568,var_8569,const_8570,call_8582,call_8599,var_8598,])
func_8600 = relay.Function([var_8568,var_8569,var_8598,], output)
mod['func_8600'] = func_8600
mod = relay.transform.InferType()(mod)
mutated_mod['func_8600'] = func_8600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8600_call = mutated_mod.get_global_var('func_8600')
var_8602 = relay.var("var_8602", dtype = "int16", shape = (312,))#candidate|8602|(312,)|var|int16
var_8603 = relay.var("var_8603", dtype = "bool", shape = (315,))#candidate|8603|(315,)|var|bool
var_8604 = relay.var("var_8604", dtype = "float32", shape = (66,))#candidate|8604|(66,)|var|float32
call_8601 = func_8600_call(var_8602,var_8603,var_8604,)
output = call_8601
func_8605 = relay.Function([var_8602,var_8603,var_8604,], output)
mutated_mod['func_8605'] = func_8605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7077_call = mod.get_global_var('func_7077')
func_7078_call = mutated_mod.get_global_var('func_7078')
call_8623 = func_7077_call()
call_8624 = func_7077_call()
output = call_8623
output2 = call_8624
func_8678 = relay.Function([], output)
mod['func_8678'] = func_8678
mod = relay.transform.InferType()(mod)
output = func_8678()
func_8679 = relay.Function([], output)
mutated_mod['func_8679'] = func_8679
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8733 = relay.var("var_8733", dtype = "float32", shape = (4, 16, 1))#candidate|8733|(4, 16, 1)|var|float32
uop_8734 = relay.log(var_8733.astype('float32')) # shape=(4, 16, 1)
func_4518_call = mod.get_global_var('func_4518')
func_4523_call = mutated_mod.get_global_var('func_4523')
const_8741 = relay.const([4.400738,8.401619,-7.146905,-9.501060,1.181240,5.701313,-4.025135,-0.112358,-0.916266,2.318996,-1.274354,2.176098,-1.173683,0.664555,-5.159151,-8.273744,-1.381665,8.637986,5.885035,8.634783,-6.576394,-4.404173,-2.321076,-8.051712,9.876091,3.462052,-4.721079,0.273127,-6.673308,-8.616512,-6.174219,-6.059533,-7.368756,-6.813613,-8.491146,2.451315,-3.667706,9.721760,-5.109887,1.080460,2.890377,7.389657,-5.688900,-3.379688,4.323116,5.133161,3.297836,5.120265,8.479515,8.766312,9.692247,6.891580,-6.504930,6.296920,-1.150473,1.629688,4.089422,9.779197,1.899675,-7.631974,3.554991,0.872172,-5.183701,-4.538169,-9.624980,4.195829,-0.475993,3.108268,9.181178,8.598397,3.840008,8.619168,2.052479,-5.285031,-1.503348,-5.466905,-5.781396,-7.498122,-0.036165,2.455251,-9.509004,-8.693535,7.446060,1.435699,-7.303038,-9.878210,1.304353,4.852759,8.734971,-5.821481,-7.501361,5.289730,-4.634586,7.166380,-8.558760,0.514635,9.661163,-1.590590,2.380884,7.439968,-8.795551,6.577600,3.197016,4.800408,5.471330,-7.147759,-1.716005,-2.830494,3.555578,7.175661,-2.792639,-6.296726,-4.376972,-0.634318,5.199479,-8.282555,-0.071902,4.571245,-5.549164,-1.103622,-7.888460,1.530564,-7.176737,8.048283,-2.740902,3.025935,8.633594,-1.763569,-2.015450,1.050232,8.223362,-2.856094,-0.557641,3.528806,-4.929768,-4.873185,1.891014,8.385207,0.573438,7.949010,0.638343,0.028413,9.291621,-5.398974,-4.241769,1.419045,9.301326,8.724711,9.435952,-7.124462,-0.797929,4.496385,5.879613,1.514356,9.548722,-9.038267,-0.039326,-1.657207,5.123205,8.789113,-8.620780,2.542226,-3.940953,6.311257,-8.972909,9.060807,-7.756621,-5.244321,8.291248,4.895955,-2.856621,6.888522,7.016559,-8.309955,4.730503,-2.459284,-8.377360,3.191919,2.430500,8.898882,0.299001,-5.202099,5.622210,0.841269,7.256490,7.741120,-0.493402,-5.794012,-0.014203,-7.279049,-3.123380,-3.815219,5.980476,-0.153569,-7.123864,-6.630952,-6.123536,-0.778565,7.722639,7.257920,-0.070631,-6.128744,9.835480,-4.821609,-9.346590,7.512180,7.667904,9.775561,-2.822946,9.758567,4.714019,-4.925645,9.885275,9.859878,-7.378083,0.269014,-4.545435,6.741733,-4.622058,1.864013,-0.743143,7.769844,-9.879518,-5.811464,-2.053622,-1.425368,3.525249,-5.254898,5.585696,0.633397,-9.807126,-8.887250,9.185922,-9.857731,8.621406,-4.249836,5.520363,9.805152,-9.255982,-1.493782], dtype = "float32")#candidate|8741|(240,)|const|float32
var_8742 = relay.var("var_8742", dtype = "float32", shape = (400,))#candidate|8742|(400,)|var|float32
const_8743 = relay.const(-5.950452, dtype = "float64")#candidate|8743|()|const|float64
call_8740 = relay.TupleGetItem(func_4518_call(relay.reshape(const_8741.astype('float32'), [1, 15, 16]), relay.reshape(var_8742.astype('float32'), [400,]), relay.reshape(const_8743.astype('float64'), []), ), 3)
call_8744 = relay.TupleGetItem(func_4523_call(relay.reshape(const_8741.astype('float32'), [1, 15, 16]), relay.reshape(var_8742.astype('float32'), [400,]), relay.reshape(const_8743.astype('float64'), []), ), 3)
output = relay.Tuple([uop_8734,call_8740,const_8741,var_8742,const_8743,])
output2 = relay.Tuple([uop_8734,call_8744,const_8741,var_8742,const_8743,])
func_8745 = relay.Function([var_8733,var_8742,], output)
mod['func_8745'] = func_8745
mod = relay.transform.InferType()(mod)
var_8746 = relay.var("var_8746", dtype = "float32", shape = (4, 16, 1))#candidate|8746|(4, 16, 1)|var|float32
var_8747 = relay.var("var_8747", dtype = "float32", shape = (400,))#candidate|8747|(400,)|var|float32
output = func_8745(var_8746,var_8747,)
func_8748 = relay.Function([var_8746,var_8747,], output)
mutated_mod['func_8748'] = func_8748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8413_call = mod.get_global_var('func_8413')
func_8415_call = mutated_mod.get_global_var('func_8415')
call_8865 = relay.TupleGetItem(func_8413_call(), 0)
call_8866 = relay.TupleGetItem(func_8415_call(), 0)
output = call_8865
output2 = call_8866
func_8870 = relay.Function([], output)
mod['func_8870'] = func_8870
mod = relay.transform.InferType()(mod)
mutated_mod['func_8870'] = func_8870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8870_call = mutated_mod.get_global_var('func_8870')
call_8871 = func_8870_call()
output = call_8871
func_8872 = relay.Function([], output)
mutated_mod['func_8872'] = func_8872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7836_call = mod.get_global_var('func_7836')
func_7837_call = mutated_mod.get_global_var('func_7837')
call_8885 = relay.TupleGetItem(func_7836_call(), 1)
call_8886 = relay.TupleGetItem(func_7837_call(), 1)
func_6131_call = mod.get_global_var('func_6131')
func_6140_call = mutated_mod.get_global_var('func_6140')
var_8910 = relay.var("var_8910", dtype = "bool", shape = (315,))#candidate|8910|(315,)|var|bool
var_8911 = relay.var("var_8911", dtype = "float32", shape = (10, 78))#candidate|8911|(10, 78)|var|float32
var_8912 = relay.var("var_8912", dtype = "float64", shape = (18,))#candidate|8912|(18,)|var|float64
var_8913 = relay.var("var_8913", dtype = "float64", shape = ())#candidate|8913|()|var|float64
var_8914 = relay.var("var_8914", dtype = "float64", shape = (1280,))#candidate|8914|(1280,)|var|float64
const_8915 = relay.const([6.281802,8.140098,-2.915476,5.122338,-3.174818,-3.487267,2.282380,4.464216,5.750556,1.755266,-3.819630,9.149735,-5.909835,8.859471,4.173529,7.248265,-9.233150,-6.813428,-8.710613,-4.446018,6.848465,7.164017,3.197210,-7.124820,2.465387,-2.450055,7.822419,-0.037294,3.102202,9.495071,-5.287751,2.748022,6.081889,2.181383,-6.159682,6.674776,-4.197987,-4.967825,3.857573,-9.530916,-7.791520,-2.589501,-3.332843,-9.469152,-3.815896,7.741906,-0.756580,5.639851,-6.173449,1.641805,5.466694,-6.978217,-0.363426,2.604476,4.396823,-6.997531,1.588225,9.817091,4.371625,9.798833,7.528799,-2.350716,3.307891,-2.174506,1.697095,-5.028187,-5.990403,-1.722331,-8.608243,-1.433506,-4.163378,3.442323,-3.312825,5.679379,-5.766563,0.869698,9.200836,2.870164,-9.791965,-9.241472,-3.806299,-9.109788,-5.181549,5.143013,-0.686014,-2.459030,-9.987346,-9.259392,6.111974,-6.458147,-0.936369,0.354844,0.295821,5.316774,-1.766214,6.369963,-2.013864,9.479353,2.750279,8.133870,8.283075,-6.191597,-0.628661,-0.419263,-4.463026,6.180789,-7.261749,5.737643,-6.737806,1.586740,-6.144616,9.251054,-0.650886,9.057208,3.786317,-6.568268,6.955052,-9.511455,3.531436,7.200631,4.336463,1.686642,2.209180,2.620288,3.775097,7.653450,-4.774002,-8.094547,6.451113,-0.714914,3.150169,3.885874,7.642821,-3.966593,-4.769905,-3.172485,-8.008461,-8.128308,-3.388516,1.783379,-5.378464,-3.757115,7.720591,-2.557994,-3.555357,0.007525,1.166503,-6.846802,-0.113235,0.987576,-2.716758,-8.657653,5.569600,2.970254,2.393904,8.444839,3.108553,-3.551930,9.493482,2.313830,4.282753,2.655290,-3.502394,5.861340,-0.860006,3.581922,-6.692234,0.131049,-3.744733,-4.502965,-6.948427,-8.611422,5.073807,-1.269024,0.017560,-0.846272,7.574470,6.649142,-8.016520,-0.200100,5.009201,6.100010,-6.822608,-2.524223,3.828907,-8.696101,-9.687278,6.328483,4.925595,-8.308843,-0.532885,0.041486,-0.369968,3.076946,0.014458,3.494068,1.281380,-3.503898,-1.292688,6.679556,0.765354,0.496833,-5.187711,2.081310,-2.607843,-4.836335,9.047656,-2.217494,-3.252810,-2.271007,-9.477698,-0.014929,-7.866260,7.979766,8.389987,8.536600,-9.595001,5.683025,3.355250,-8.416247,-0.365847,-2.486362,-4.530200,-3.935036,-3.697657,-3.782448,-7.119408,8.089140,3.029090,9.948429,3.570584,-0.905235,3.378037,-3.346781,-7.615238,7.364453,8.017655,-6.061926,-9.266385,-2.691585,0.304870,7.193569,7.464154,4.558706,6.830292,-7.089389,3.890815,-2.702135,-6.701527,4.440523,1.192856,6.551662,3.353158,-1.708915,-0.008150,-9.089169,8.372053,-1.103217,-2.559287,-4.851295,-5.983861,-8.805297,0.098324,8.754937,0.838526,-6.278229,2.046335,3.195295,-5.762669,-5.733126,-7.953539,-1.814994,6.202834,4.795867,-2.666750,1.816334,-4.252162,-0.912631,3.517898,9.484124,0.613658,7.228906,3.308420,1.587157,4.331492,8.626521,-6.281626,9.800789,-9.210018,-6.934602,-6.399549,5.788626,5.713107,-8.265766,6.615675,-8.166354,-3.877663,5.848457,-6.912320,4.174074,6.489015,-6.259306,-1.253304,5.602437,-6.140788,-7.169736,8.326790,2.105823,6.964896,7.154620,0.461884,3.750619,-0.828538,0.841254,4.605198,-0.160352,9.047755,8.814136,-4.608644,-4.769018,-4.699049,-1.653811,4.451425,-4.314688,7.534618,4.827900,6.834328,-6.368412,-4.890368,8.736962,-4.866442,-4.668563,-7.667181,-3.353280,-6.726191,0.561704,7.336415,-1.611658,5.080564,7.900281,2.682609,9.153494,-3.314750,-9.413791,7.665275,-7.485173,2.149370,-0.649777,-2.261916,-2.446804,0.755203,7.527155,7.920876,9.290044,8.741924,-4.973463,-5.492403,2.000060,8.467544,5.735210,1.989869,8.862029,-2.509201,-8.356488], dtype = "float64")#candidate|8915|(364,)|const|float64
call_8909 = relay.TupleGetItem(func_6131_call(relay.reshape(var_8910.astype('bool'), [15, 3, 7]), relay.reshape(var_8910.astype('bool'), [15, 3, 7]), relay.reshape(var_8911.astype('float32'), [780, 1]), relay.reshape(var_8912.astype('float64'), [18,]), relay.reshape(var_8913.astype('float64'), []), relay.reshape(var_8914.astype('float64'), [1280,]), relay.reshape(const_8915.astype('float64'), [364,]), ), 11)
call_8916 = relay.TupleGetItem(func_6140_call(relay.reshape(var_8910.astype('bool'), [15, 3, 7]), relay.reshape(var_8910.astype('bool'), [15, 3, 7]), relay.reshape(var_8911.astype('float32'), [780, 1]), relay.reshape(var_8912.astype('float64'), [18,]), relay.reshape(var_8913.astype('float64'), []), relay.reshape(var_8914.astype('float64'), [1280,]), relay.reshape(const_8915.astype('float64'), [364,]), ), 11)
func_934_call = mod.get_global_var('func_934')
func_937_call = mutated_mod.get_global_var('func_937')
var_8937 = relay.var("var_8937", dtype = "bool", shape = (360, 1))#candidate|8937|(360, 1)|var|bool
const_8938 = relay.const([-6,-7,9,5,-6,-6,-7,10,3,4,7,6,-3,-2,-7], dtype = "int16")#candidate|8938|(15,)|const|int16
call_8936 = relay.TupleGetItem(func_934_call(relay.reshape(var_8937.astype('bool'), [9, 10, 4]), relay.reshape(const_8938.astype('int16'), [15, 1]), ), 1)
call_8939 = relay.TupleGetItem(func_937_call(relay.reshape(var_8937.astype('bool'), [9, 10, 4]), relay.reshape(const_8938.astype('int16'), [15, 1]), ), 1)
bop_8942 = relay.floor_divide(call_8885.astype('float64'), const_8938.astype('float64')) # shape=(11, 11, 15)
bop_8945 = relay.floor_divide(call_8886.astype('float64'), const_8938.astype('float64')) # shape=(11, 11, 15)
bop_8962 = relay.mod(var_8912.astype('float64'), var_8937.astype('float64')) # shape=(360, 18)
output = relay.Tuple([call_8909,var_8910,var_8911,var_8913,var_8914,const_8915,call_8936,bop_8942,bop_8962,])
output2 = relay.Tuple([call_8916,var_8910,var_8911,var_8913,var_8914,const_8915,call_8939,bop_8945,bop_8962,])
func_8966 = relay.Function([var_8910,var_8911,var_8912,var_8913,var_8914,var_8937,], output)
mod['func_8966'] = func_8966
mod = relay.transform.InferType()(mod)
mutated_mod['func_8966'] = func_8966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8966_call = mutated_mod.get_global_var('func_8966')
var_8968 = relay.var("var_8968", dtype = "bool", shape = (315,))#candidate|8968|(315,)|var|bool
var_8969 = relay.var("var_8969", dtype = "float32", shape = (10, 78))#candidate|8969|(10, 78)|var|float32
var_8970 = relay.var("var_8970", dtype = "float64", shape = (18,))#candidate|8970|(18,)|var|float64
var_8971 = relay.var("var_8971", dtype = "float64", shape = ())#candidate|8971|()|var|float64
var_8972 = relay.var("var_8972", dtype = "float64", shape = (1280,))#candidate|8972|(1280,)|var|float64
var_8973 = relay.var("var_8973", dtype = "bool", shape = (360, 1))#candidate|8973|(360, 1)|var|bool
call_8967 = func_8966_call(var_8968,var_8969,var_8970,var_8971,var_8972,var_8973,)
output = call_8967
func_8974 = relay.Function([var_8968,var_8969,var_8970,var_8971,var_8972,var_8973,], output)
mutated_mod['func_8974'] = func_8974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8678_call = mod.get_global_var('func_8678')
func_8679_call = mutated_mod.get_global_var('func_8679')
call_8976 = func_8678_call()
call_8977 = func_8678_call()
func_6872_call = mod.get_global_var('func_6872')
func_6874_call = mutated_mod.get_global_var('func_6874')
const_8980 = relay.const([[5.429220,-0.748470,-3.687609,9.153524,-0.346514,-0.381677,4.000435,8.096284,2.879451,-0.595400,-2.562730,4.598634,9.691997,5.259391,-4.292119,8.459131,7.752763,2.624292,7.567550,-1.463281,2.915263,-3.375792,8.499411,-0.808917,-8.459911,5.995979,-2.410793,-7.726829,1.803205,0.995191,-1.777115,-2.733916,-0.846532,1.027150,-1.550042,9.468190,8.716553,-7.273304,-8.445101,1.760648,7.851699,2.099985,3.571993,5.313981,-0.098457,7.122628,-6.286373,-1.604379,7.273737,-1.488145,-8.768784,3.187766,9.010509,-6.291903,-2.804570,5.461286,-3.478044,2.318287,-3.979133,6.241709,0.717262,3.929707,-1.384973,-7.575652,-8.969846,1.034762,4.945307,-8.656907,-5.180780,-5.156164,-8.991383,6.942151,-4.717655,9.419861,6.899405,5.581031,4.200978,-4.558956,8.047574,8.024599,-3.943636,-4.819750,8.083079,-1.211349,3.090379,5.900623,-3.091708,-9.779494,7.012566,-5.679306,-2.074829,-9.504075,-9.198675,9.432373,2.298839,0.428729,4.110670,5.596681,-7.282521,3.825175,-7.299869,-4.076028,6.804884,-1.826823,-2.797576,1.015302,-9.318620,-7.501016,7.875915,-8.416004,-0.658598,-7.736690,4.919114,-3.926016,5.489900,3.974028,-2.767081,7.287424,9.941709,8.428630,-9.690043,-5.307990,-8.975899,5.612235,0.797556,-5.817948,-9.253267,5.028428,9.452892,4.552709,8.467865,-8.045945,-5.240384,0.174932,7.467379,2.642734,-9.852136,6.128088,-2.033498,-9.603645,-0.240793,7.725914,4.637186,7.143584,7.376883,3.665032,0.436899,-4.799372,2.454038,1.324954,-8.634974,-0.254614,7.293703,0.962757,5.002247,6.073428],[9.542524,-4.789864,2.572024,1.893916,-9.226029,-5.778395,-7.669336,-7.788939,-3.065717,4.260045,-8.237385,5.750805,9.843998,-5.352998,-7.864507,-2.561921,-7.039839,-6.885465,-8.183348,-8.662647,6.821241,9.036244,-0.279679,4.026561,0.957576,5.695442,8.307059,4.289669,-7.080720,5.057866,6.071220,-0.972420,-9.192257,-4.966764,-5.509137,0.719004,5.925333,6.008951,-7.873814,-9.972592,0.792424,-5.989533,4.630471,7.040424,1.658245,-5.756878,6.664193,-5.707733,-2.869504,-3.194943,-6.065529,-6.798949,-3.561435,5.628944,-8.624094,4.351654,0.305385,-6.293619,7.949127,-9.150770,-5.789148,-6.683894,1.782394,1.226610,6.753225,-3.513601,-2.055077,1.028196,3.964411,3.402189,-2.390858,5.334820,-4.381236,-3.463559,-1.956089,-6.677929,-4.393281,-4.534701,-3.211343,2.685329,7.516318,1.670389,-3.962855,2.603706,1.659785,8.121160,2.448662,6.050863,9.358904,7.413976,3.685349,-8.683430,-4.903529,3.994817,3.833710,-3.090795,7.943801,-6.691735,-9.299707,9.586484,-7.410294,-6.949008,3.812539,-2.168684,7.220074,-0.045389,0.529429,-7.053097,5.630911,-7.593256,-9.727162,-7.621356,-0.186202,4.898811,-5.135831,-8.945742,-9.507237,-7.727568,3.883404,-3.229826,-0.846954,8.572785,9.355412,-4.197160,3.828095,9.905157,4.789252,5.004517,-0.691000,5.434462,6.881200,-7.086649,-5.214002,-5.286617,1.237647,-7.605127,0.544761,7.652000,-3.245813,-4.948837,6.155756,0.982899,0.858569,-5.009262,-7.715388,-4.064580,-3.222529,9.211898,8.546853,-5.495617,-8.144986,-3.391063,-1.656310,-7.738260,1.351585,-5.497144],[4.874020,-9.032951,9.560878,-7.178841,-0.540719,8.390374,2.252212,6.663386,-0.538601,0.240930,-3.235546,0.650186,-6.696050,0.115804,-7.436652,-1.982194,-4.723441,-0.046693,1.978631,1.927528,1.915601,-8.961723,8.659392,3.124509,3.204748,-2.425223,-6.045900,-0.317512,3.047543,5.702440,-1.827059,1.381591,-6.221271,-5.320296,7.624431,2.017923,-1.869456,2.798862,1.644498,-7.719527,-1.258921,-0.583211,-0.083432,7.536392,5.655531,2.363439,-2.259090,-5.572445,-0.869707,-7.843826,-1.430114,-4.861349,-2.953111,-6.115424,-8.013780,-4.266002,4.391531,1.252036,-0.470810,7.540747,2.179291,0.449218,-4.813586,-9.067692,-3.783060,-6.543585,-8.146412,7.753507,-0.899103,-9.768494,-2.384833,0.109442,-3.273334,8.482375,5.695980,-3.303612,0.396714,-4.815822,8.519222,-2.625974,-0.081701,-5.122617,5.677274,2.828498,9.298827,-9.514832,-8.481833,3.265313,4.772132,7.383219,5.084423,7.894866,4.804034,-8.262127,6.849438,-7.281159,7.583392,-1.906951,0.629640,9.800494,-7.785371,-0.731217,4.873194,3.900372,5.760336,-2.546677,-5.540087,8.187161,6.715549,-4.370859,5.226379,-6.091939,3.268104,7.464121,-4.991340,4.806435,0.635892,-6.643734,6.648308,1.806848,-8.340648,7.996684,0.653662,2.622265,5.315578,7.122636,-8.884995,0.327684,3.251508,-9.924744,3.799293,-1.811491,-8.687451,-6.065634,-9.181168,-1.745873,7.586851,6.896624,-2.670504,7.082484,-7.890936,-6.607824,3.035363,-1.965912,2.507521,-9.971341,-0.238327,9.763932,8.520516,-4.953558,1.509890,4.131872,-8.066804,5.478016,8.448194,-6.505436],[-5.407565,-6.854082,7.224447,-3.384290,-0.745047,9.780666,8.438812,1.018379,-1.709616,-9.382132,-7.171179,-4.405141,-5.240833,1.776088,8.664385,6.517074,3.231377,1.242707,-4.762100,4.885123,-6.978417,4.036812,6.333874,4.795105,-2.399212,6.876573,7.013183,2.392154,1.002601,4.343078,0.631177,-2.193348,-9.231685,5.102663,2.611383,1.943333,6.933589,4.249676,8.454232,8.540976,-5.516098,-7.058310,-8.544770,6.168066,6.360320,-1.426029,8.115692,1.927822,-0.331321,-7.765049,0.391798,-3.541704,-8.197789,2.400768,-2.232918,9.603922,1.344810,-1.663041,-9.588904,0.966892,-6.038653,-4.046709,3.381066,1.799426,-3.030824,6.951084,-2.631213,-5.817726,-8.685311,-7.595669,-8.396406,5.457906,-0.292849,-1.495217,-0.547489,-7.400222,8.130457,-3.363567,-0.737497,8.708996,-5.009641,-8.845589,-5.009709,1.076072,-6.958342,6.246019,-1.107653,-2.496363,-2.524336,9.025322,-0.942434,1.818953,-7.372771,-0.771740,9.964363,2.855587,3.973456,-0.259128,-7.849776,-5.728515,-2.559509,-8.856200,-4.485239,7.190910,5.649144,2.996165,-5.066646,2.435373,1.380564,8.025052,8.476982,-4.487070,-5.114093,-2.323455,-2.797411,6.128782,-7.808500,0.831311,-6.283022,1.252451,2.010799,2.740814,1.834658,-3.118573,1.339131,-7.964858,-5.051617,6.297879,7.206577,-1.620526,-8.882981,-3.376295,0.091694,9.432780,-8.843463,1.829517,-2.036509,9.554996,7.258426,-7.422045,0.007021,-1.300885,2.287827,-9.355695,9.307486,-7.440353,-4.761109,6.299468,6.104751,0.731490,9.892164,8.729947,-9.915634,-2.291230,5.808210,-8.628833],[5.752049,-1.892396,-4.247598,8.798266,7.540871,1.006520,2.436570,7.698397,0.980273,-1.567470,1.864089,-4.201689,7.684823,-9.195485,9.630488,0.028969,4.002315,1.141865,6.778231,7.299558,7.415900,-4.356721,2.317195,9.787668,2.208302,-9.028883,8.724370,-2.059038,4.661552,4.396879,6.757051,7.517988,1.439563,-8.108184,0.931730,5.946205,-1.938163,8.900929,-2.971572,-0.814187,8.608291,-5.844179,-8.469395,3.849897,0.346242,-3.774361,8.275753,6.971919,7.492818,8.269166,-2.082251,4.642633,9.742907,-6.468609,1.607886,6.428962,2.002169,7.434496,-3.578053,1.597397,-5.322479,-6.230447,2.352180,-6.390859,9.502892,-7.018087,-4.649688,-8.631146,-3.328620,9.307662,5.956274,-0.514213,5.265539,-4.160668,-7.756994,9.164793,-3.611257,5.602200,-6.672417,-2.935524,0.317701,6.280989,-0.546130,0.187386,-0.672917,-8.857437,7.405769,0.015985,-9.855150,-4.228013,3.164441,1.494630,0.745858,-5.414145,-2.979444,2.200900,3.073544,-1.234943,-9.579204,-0.958503,-4.254752,5.141384,-8.569292,-2.507122,-0.820708,1.289556,3.864381,1.146937,8.919292,-3.832557,-9.753320,-6.284185,-7.808752,5.150089,-5.135342,4.233329,-9.852047,0.742838,6.022108,-3.208889,-9.107692,-6.290094,-6.358757,0.272522,5.778926,-9.850396,8.078609,2.974335,1.314844,6.827896,-9.198989,-5.594096,4.406996,2.785900,-4.383901,-6.707256,-7.259414,-5.613289,3.976087,-4.629890,1.794779,-5.526635,8.272502,-3.105546,0.672962,1.009438,-5.639734,-0.838146,2.192544,3.338031,1.634862,-4.165732,-5.732670,6.332623,-0.543029,-5.891776]], dtype = "float32")#candidate|8980|(5, 156)|const|float32
call_8979 = relay.TupleGetItem(func_6872_call(relay.reshape(const_8980.astype('float32'), [780,])), 1)
call_8981 = relay.TupleGetItem(func_6874_call(relay.reshape(const_8980.astype('float32'), [780,])), 1)
output = relay.Tuple([call_8976,call_8979,const_8980,])
output2 = relay.Tuple([call_8977,call_8981,const_8980,])
func_8982 = relay.Function([], output)
mod['func_8982'] = func_8982
mod = relay.transform.InferType()(mod)
mutated_mod['func_8982'] = func_8982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8982_call = mutated_mod.get_global_var('func_8982')
call_8983 = func_8982_call()
output = call_8983
func_8984 = relay.Function([], output)
mutated_mod['func_8984'] = func_8984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7836_call = mod.get_global_var('func_7836')
func_7837_call = mutated_mod.get_global_var('func_7837')
call_8994 = relay.TupleGetItem(func_7836_call(), 1)
call_8995 = relay.TupleGetItem(func_7837_call(), 1)
func_417_call = mod.get_global_var('func_417')
func_421_call = mutated_mod.get_global_var('func_421')
var_9001 = relay.var("var_9001", dtype = "float32", shape = (50,))#candidate|9001|(50,)|var|float32
var_9002 = relay.var("var_9002", dtype = "float32", shape = (400,))#candidate|9002|(400,)|var|float32
call_9000 = relay.TupleGetItem(func_417_call(relay.reshape(var_9001.astype('float32'), [10, 5, 1]), relay.reshape(var_9002.astype('float32'), [10, 5, 8]), ), 0)
call_9003 = relay.TupleGetItem(func_421_call(relay.reshape(var_9001.astype('float32'), [10, 5, 1]), relay.reshape(var_9002.astype('float32'), [10, 5, 8]), ), 0)
var_9007 = relay.var("var_9007", dtype = "float32", shape = (50,))#candidate|9007|(50,)|var|float32
bop_9008 = relay.bitwise_xor(var_9001.astype('int32'), relay.reshape(var_9007.astype('int32'), relay.shape_of(var_9001))) # shape=(50,)
output = relay.Tuple([call_8994,call_9000,var_9002,bop_9008,])
output2 = relay.Tuple([call_8995,call_9003,var_9002,bop_9008,])
func_9012 = relay.Function([var_9001,var_9002,var_9007,], output)
mod['func_9012'] = func_9012
mod = relay.transform.InferType()(mod)
var_9013 = relay.var("var_9013", dtype = "float32", shape = (50,))#candidate|9013|(50,)|var|float32
var_9014 = relay.var("var_9014", dtype = "float32", shape = (400,))#candidate|9014|(400,)|var|float32
var_9015 = relay.var("var_9015", dtype = "float32", shape = (50,))#candidate|9015|(50,)|var|float32
output = func_9012(var_9013,var_9014,var_9015,)
func_9016 = relay.Function([var_9013,var_9014,var_9015,], output)
mutated_mod['func_9016'] = func_9016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7836_call = mod.get_global_var('func_7836')
func_7837_call = mutated_mod.get_global_var('func_7837')
call_9023 = relay.TupleGetItem(func_7836_call(), 0)
call_9024 = relay.TupleGetItem(func_7837_call(), 0)
func_417_call = mod.get_global_var('func_417')
func_421_call = mutated_mod.get_global_var('func_421')
const_9037 = relay.const([[1.273385],[-2.345613],[-8.619869],[-8.195181],[-8.906423],[-5.225042],[-5.132449],[2.411379],[9.345602],[7.716942],[-1.557907],[4.504284],[-1.882818],[-2.631747],[4.778536],[-7.994097],[7.938049],[7.440811],[-1.822846],[9.285517],[-5.260630],[1.282209],[7.457686],[4.105871],[-1.070182],[-7.524010],[-2.508393],[-5.196270],[-9.921282],[1.379908],[1.817931],[-5.635697],[6.289417],[-2.764879],[6.266748],[-8.290293],[4.813883],[2.175691],[7.933728],[6.449559],[0.257173],[-8.253261],[6.390279],[2.775204],[5.787935],[-8.541275],[-8.016849],[-5.540804],[-7.852884],[5.861882]], dtype = "float32")#candidate|9037|(50, 1)|const|float32
var_9038 = relay.var("var_9038", dtype = "float32", shape = (400,))#candidate|9038|(400,)|var|float32
call_9036 = relay.TupleGetItem(func_417_call(relay.reshape(const_9037.astype('float32'), [10, 5, 1]), relay.reshape(var_9038.astype('float32'), [10, 5, 8]), ), 0)
call_9039 = relay.TupleGetItem(func_421_call(relay.reshape(const_9037.astype('float32'), [10, 5, 1]), relay.reshape(var_9038.astype('float32'), [10, 5, 8]), ), 0)
uop_9042 = relay.cosh(const_9037.astype('float64')) # shape=(50, 1)
uop_9046 = relay.acos(uop_9042.astype('float32')) # shape=(50, 1)
func_1409_call = mod.get_global_var('func_1409')
func_1412_call = mutated_mod.get_global_var('func_1412')
const_9051 = relay.const([1.507360,-8.736438,4.468949,9.617967,-7.428145,4.691053,-8.569072,8.273303,0.909127,-0.028625,6.953710,-8.748657,6.046572,3.781670,-0.133243,-7.149089,-4.432093,-5.614242], dtype = "float64")#candidate|9051|(18,)|const|float64
call_9050 = func_1409_call(relay.reshape(const_9051.astype('float64'), [6, 3, 1]))
call_9052 = func_1409_call(relay.reshape(const_9051.astype('float64'), [6, 3, 1]))
func_7482_call = mod.get_global_var('func_7482')
func_7484_call = mutated_mod.get_global_var('func_7484')
var_9059 = relay.var("var_9059", dtype = "int16", shape = (15,))#candidate|9059|(15,)|var|int16
call_9058 = relay.TupleGetItem(func_7482_call(relay.reshape(var_9059.astype('int16'), [15,])), 1)
call_9060 = relay.TupleGetItem(func_7484_call(relay.reshape(var_9059.astype('int16'), [15,])), 1)
func_1177_call = mod.get_global_var('func_1177')
func_1180_call = mutated_mod.get_global_var('func_1180')
const_9062 = relay.const([True,False,True,False,True,False,False,False,False,True,False,True,True,True,False,False,True,True,False,True,False,False,True,False,True,False,True,True,False,True,False,True,True,False,False,False,False,False,False,True,True,False,False,False,True,False,False,True], dtype = "bool")#candidate|9062|(48,)|const|bool
var_9063 = relay.var("var_9063", dtype = "bool", shape = (480,))#candidate|9063|(480,)|var|bool
call_9061 = func_1177_call(relay.reshape(const_9062.astype('bool'), [6, 1, 8]), relay.reshape(var_9063.astype('bool'), [6, 10, 8]), )
call_9064 = func_1177_call(relay.reshape(const_9062.astype('bool'), [6, 1, 8]), relay.reshape(var_9063.astype('bool'), [6, 10, 8]), )
bop_9067 = relay.add(uop_9046.astype('uint32'), relay.reshape(uop_9042.astype('uint32'), relay.shape_of(uop_9046))) # shape=(50, 1)
func_8348_call = mod.get_global_var('func_8348')
func_8350_call = mutated_mod.get_global_var('func_8350')
call_9071 = relay.TupleGetItem(func_8348_call(), 0)
call_9072 = relay.TupleGetItem(func_8350_call(), 0)
func_6695_call = mod.get_global_var('func_6695')
func_6696_call = mutated_mod.get_global_var('func_6696')
call_9074 = relay.TupleGetItem(func_6695_call(), 0)
call_9075 = relay.TupleGetItem(func_6696_call(), 0)
func_7482_call = mod.get_global_var('func_7482')
func_7484_call = mutated_mod.get_global_var('func_7484')
call_9079 = relay.TupleGetItem(func_7482_call(relay.reshape(var_9059.astype('int16'), [15,])), 1)
call_9080 = relay.TupleGetItem(func_7484_call(relay.reshape(var_9059.astype('int16'), [15,])), 1)
bop_9084 = relay.power(uop_9042.astype('float64'), var_9038.astype('float64')) # shape=(50, 400)
bop_9088 = relay.logical_or(bop_9067.astype('bool'), relay.reshape(uop_9046.astype('bool'), relay.shape_of(bop_9067))) # shape=(50, 1)
var_9092 = relay.var("var_9092", dtype = "bool", shape = (50, 1))#candidate|9092|(50, 1)|var|bool
bop_9093 = relay.power(bop_9088.astype('float32'), relay.reshape(var_9092.astype('float32'), relay.shape_of(bop_9088))) # shape=(50, 1)
bop_9106 = relay.multiply(bop_9067.astype('int64'), const_9051.astype('int64')) # shape=(50, 18)
output = relay.Tuple([call_9023,call_9036,call_9050,call_9058,var_9059,call_9061,const_9062,var_9063,call_9071,call_9074,call_9079,bop_9084,bop_9093,bop_9106,])
output2 = relay.Tuple([call_9024,call_9039,call_9052,call_9060,var_9059,call_9064,const_9062,var_9063,call_9072,call_9075,call_9080,bop_9084,bop_9093,bop_9106,])
func_9110 = relay.Function([var_9038,var_9059,var_9063,var_9092,], output)
mod['func_9110'] = func_9110
mod = relay.transform.InferType()(mod)
mutated_mod['func_9110'] = func_9110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9110_call = mutated_mod.get_global_var('func_9110')
var_9112 = relay.var("var_9112", dtype = "float32", shape = (400,))#candidate|9112|(400,)|var|float32
var_9113 = relay.var("var_9113", dtype = "int16", shape = (15,))#candidate|9113|(15,)|var|int16
var_9114 = relay.var("var_9114", dtype = "bool", shape = (480,))#candidate|9114|(480,)|var|bool
var_9115 = relay.var("var_9115", dtype = "bool", shape = (50, 1))#candidate|9115|(50, 1)|var|bool
call_9111 = func_9110_call(var_9112,var_9113,var_9114,var_9115,)
output = call_9111
func_9116 = relay.Function([var_9112,var_9113,var_9114,var_9115,], output)
mutated_mod['func_9116'] = func_9116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6412_call = mod.get_global_var('func_6412')
func_6414_call = mutated_mod.get_global_var('func_6414')
call_9187 = relay.TupleGetItem(func_6412_call(), 0)
call_9188 = relay.TupleGetItem(func_6414_call(), 0)
uop_9191 = relay.sqrt(call_9187.astype('float64')) # shape=(3, 11, 2)
uop_9193 = relay.sqrt(call_9188.astype('float64')) # shape=(3, 11, 2)
func_2733_call = mod.get_global_var('func_2733')
func_2739_call = mutated_mod.get_global_var('func_2739')
var_9203 = relay.var("var_9203", dtype = "float64", shape = (1080,))#candidate|9203|(1080,)|var|float64
const_9204 = relay.const([-2.376440,-1.702020,-1.489585,-5.564003,-8.626035,5.823749,-8.902582,-0.510553,-8.268965,3.146897,-5.397212,4.033155,-0.964716,5.105049,-1.970697,3.936420,7.587120,-6.617676,-4.219263,0.843752,5.969294,9.266743,-3.803064,-9.245971,7.703315,-1.920446,4.658421,8.780685,-6.095209,-4.889983,4.318848,-1.052591,9.028612,-2.916353,9.782143,8.041478,-3.496376,-5.986011,-9.092873,-4.637531,-0.103776,-2.016129,-7.148494,9.017980,-0.684817,0.284979,-8.784013,-9.489773,3.062314,6.722403], dtype = "float32")#candidate|9204|(50,)|const|float32
var_9205 = relay.var("var_9205", dtype = "bool", shape = (48,))#candidate|9205|(48,)|var|bool
call_9202 = relay.TupleGetItem(func_2733_call(relay.reshape(var_9203.astype('float64'), [10, 9, 12]), relay.reshape(var_9203.astype('float64'), [10, 9, 12]), relay.reshape(const_9204.astype('float32'), [50,]), relay.reshape(var_9205.astype('bool'), [48,]), ), 2)
call_9206 = relay.TupleGetItem(func_2739_call(relay.reshape(var_9203.astype('float64'), [10, 9, 12]), relay.reshape(var_9203.astype('float64'), [10, 9, 12]), relay.reshape(const_9204.astype('float32'), [50,]), relay.reshape(var_9205.astype('bool'), [48,]), ), 2)
output = relay.Tuple([uop_9191,call_9202,var_9203,const_9204,var_9205,])
output2 = relay.Tuple([uop_9193,call_9206,var_9203,const_9204,var_9205,])
func_9207 = relay.Function([var_9203,var_9205,], output)
mod['func_9207'] = func_9207
mod = relay.transform.InferType()(mod)
mutated_mod['func_9207'] = func_9207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9207_call = mutated_mod.get_global_var('func_9207')
var_9209 = relay.var("var_9209", dtype = "float64", shape = (1080,))#candidate|9209|(1080,)|var|float64
var_9210 = relay.var("var_9210", dtype = "bool", shape = (48,))#candidate|9210|(48,)|var|bool
call_9208 = func_9207_call(var_9209,var_9210,)
output = call_9208
func_9211 = relay.Function([var_9209,var_9210,], output)
mutated_mod['func_9211'] = func_9211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7955_call = mod.get_global_var('func_7955')
func_7957_call = mutated_mod.get_global_var('func_7957')
call_9216 = relay.TupleGetItem(func_7955_call(), 0)
call_9217 = relay.TupleGetItem(func_7957_call(), 0)
uop_9222 = relay.cosh(call_9216.astype('float64')) # shape=(3, 11, 2)
uop_9224 = relay.cosh(call_9217.astype('float64')) # shape=(3, 11, 2)
func_7459_call = mod.get_global_var('func_7459')
func_7461_call = mutated_mod.get_global_var('func_7461')
call_9225 = func_7459_call()
call_9226 = func_7459_call()
output = relay.Tuple([uop_9222,call_9225,])
output2 = relay.Tuple([uop_9224,call_9226,])
func_9236 = relay.Function([], output)
mod['func_9236'] = func_9236
mod = relay.transform.InferType()(mod)
mutated_mod['func_9236'] = func_9236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9236_call = mutated_mod.get_global_var('func_9236')
call_9237 = func_9236_call()
output = call_9237
func_9238 = relay.Function([], output)
mutated_mod['func_9238'] = func_9238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8678_call = mod.get_global_var('func_8678')
func_8679_call = mutated_mod.get_global_var('func_8679')
call_9272 = func_8678_call()
call_9273 = func_8678_call()
output = relay.Tuple([call_9272,])
output2 = relay.Tuple([call_9273,])
func_9279 = relay.Function([], output)
mod['func_9279'] = func_9279
mod = relay.transform.InferType()(mod)
mutated_mod['func_9279'] = func_9279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9279_call = mutated_mod.get_global_var('func_9279')
call_9280 = func_9279_call()
output = call_9280
func_9281 = relay.Function([], output)
mutated_mod['func_9281'] = func_9281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6922_call = mod.get_global_var('func_6922')
func_6923_call = mutated_mod.get_global_var('func_6923')
call_9299 = relay.TupleGetItem(func_6922_call(), 2)
call_9300 = relay.TupleGetItem(func_6923_call(), 2)
var_9310 = relay.var("var_9310", dtype = "float64", shape = (1815,))#candidate|9310|(1815,)|var|float64
bop_9311 = relay.power(call_9299.astype('float64'), relay.reshape(var_9310.astype('float64'), relay.shape_of(call_9299))) # shape=(1815,)
bop_9314 = relay.power(call_9300.astype('float64'), relay.reshape(var_9310.astype('float64'), relay.shape_of(call_9300))) # shape=(1815,)
output = bop_9311
output2 = bop_9314
func_9316 = relay.Function([var_9310,], output)
mod['func_9316'] = func_9316
mod = relay.transform.InferType()(mod)
mutated_mod['func_9316'] = func_9316
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9317 = relay.var("var_9317", dtype = "float64", shape = (1815,))#candidate|9317|(1815,)|var|float64
func_9316_call = mutated_mod.get_global_var('func_9316')
call_9318 = func_9316_call(var_9317)
output = call_9318
func_9319 = relay.Function([var_9317], output)
mutated_mod['func_9319'] = func_9319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8283_call = mod.get_global_var('func_8283')
func_8284_call = mutated_mod.get_global_var('func_8284')
call_9375 = relay.TupleGetItem(func_8283_call(), 2)
call_9376 = relay.TupleGetItem(func_8284_call(), 2)
output = call_9375
output2 = call_9376
func_9387 = relay.Function([], output)
mod['func_9387'] = func_9387
mod = relay.transform.InferType()(mod)
mutated_mod['func_9387'] = func_9387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9387_call = mutated_mod.get_global_var('func_9387')
call_9388 = func_9387_call()
output = call_9388
func_9389 = relay.Function([], output)
mutated_mod['func_9389'] = func_9389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7290_call = mod.get_global_var('func_7290')
func_7292_call = mutated_mod.get_global_var('func_7292')
call_9390 = func_7290_call()
call_9391 = func_7290_call()
output = relay.Tuple([call_9390,])
output2 = relay.Tuple([call_9391,])
func_9394 = relay.Function([], output)
mod['func_9394'] = func_9394
mod = relay.transform.InferType()(mod)
mutated_mod['func_9394'] = func_9394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9394_call = mutated_mod.get_global_var('func_9394')
call_9395 = func_9394_call()
output = call_9395
func_9396 = relay.Function([], output)
mutated_mod['func_9396'] = func_9396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7955_call = mod.get_global_var('func_7955')
func_7957_call = mutated_mod.get_global_var('func_7957')
call_9458 = relay.TupleGetItem(func_7955_call(), 1)
call_9459 = relay.TupleGetItem(func_7957_call(), 1)
func_8745_call = mod.get_global_var('func_8745')
func_8748_call = mutated_mod.get_global_var('func_8748')
const_9461 = relay.const([-7.825050,2.630822,0.972407,1.069578,9.722585,-0.098668,-0.188758,5.832505,-3.123094,4.611556,8.748650,0.845320,8.195701,-7.354682,-1.076891,9.194031,-2.227097,0.226831,-2.196568,-0.238990,-6.940534,0.559798,-4.794743,4.872463,3.954931,8.605793,0.566171,4.820318,-5.084442,4.726573,2.582805,2.833358,6.946762,6.658914,-8.656285,0.703745,-6.382282,1.425414,4.855308,-0.375348,-2.078397,-4.821447,-4.051293,-1.128954,6.285742,-2.591981,2.002403,5.723602,-5.933797,-7.029469,-9.983160,7.558775,-3.213171,4.861123,5.601339,-2.687983,7.403921,0.816763,-6.266569,7.158373,7.134293,0.726412,1.695938,2.516381], dtype = "float32")#candidate|9461|(64,)|const|float32
const_9462 = relay.const([9.499833,8.045741,6.718478,-7.023497,-0.908735,-1.562909,8.195873,3.692077,5.919747,4.508461,-1.689914,8.813222,1.679712,4.251684,7.547525,-2.248037,2.599400,-2.784961,-6.254036,6.618220,-8.106447,5.670209,2.008427,8.331567,5.651449,9.551335,0.852666,5.705758,5.591774,-5.977118,8.013093,-7.306553,-1.946663,3.543271,0.544169,7.244155,-0.123042,5.114116,8.355910,-8.685089,6.447848,1.213539,1.507635,-2.737903,4.926293,9.330076,5.725895,-6.051771,-1.729005,8.350221,-6.241479,6.293559,0.157665,1.360613,-5.143234,4.339648,6.751598,-5.120238,6.135524,-4.279529,3.622773,5.911785,0.539317,-3.918433,8.393487,8.395069,-1.818091,-8.856442,8.192812,7.031708,-0.320743,0.373862,9.312800,-9.647204,-4.269178,6.535346,-7.766119,4.894038,-5.844133,2.303257,8.328659,-9.719259,-6.670616,1.029070,-8.647812,4.904302,8.650547,-4.052342,-1.808029,6.538633,1.516919,0.964899,-7.426601,4.776810,-1.081940,-6.207988,9.282870,-3.754312,-1.777146,7.822657,-2.010733,1.373317,-3.263815,-7.404708,-4.039991,7.462437,-4.480306,9.224632,7.956156,-4.836543,7.715234,2.054985,2.611489,-7.058342,9.322587,-3.425681,-7.783770,1.637735,9.781519,-1.195163,-6.950342,-4.642232,-1.465506,3.591843,-8.281732,2.375890,-1.923931,7.843056,-8.976456,4.006646,6.808292,3.508894,2.656743,-0.298903,-8.791293,-4.393133,9.737699,-7.515969,-4.625077,9.902530,1.191157,7.401980,-7.025230,8.714439,-4.243835,-7.934757,-7.673836,-6.969815,2.545825,-9.153339,7.422829,-0.908872,7.516298,-5.598075,-4.083766,5.889665,-3.643512,1.411924,4.994780,-2.871792,-7.505578,2.280900,-2.324547,-1.860432,7.861137,-9.985064,-0.484537,8.267346,3.768866,3.731222,1.358863,3.335788,9.584069,-4.062430,6.912598,6.060264,-9.098258,-8.715185,-4.967788,-9.578532,7.821882,-4.633298,1.761404,-9.636219,4.797827,-1.251455,-9.360904,-5.217406,-3.998560,-4.796343,4.612958,2.190774,-1.258041,7.819607,0.981642,-2.022637,-1.564109,-1.189989,-7.017605,-3.049757,-4.727045,4.744085,-8.229371,6.806307,-2.760871,-3.750664,4.456437,5.455072,3.572687,-0.755336,-8.319109,1.507229,3.747023,-7.825164,-9.563781,9.056319,3.816720,6.883708,-9.907940,0.138550,-3.851769,8.091139,6.402834,-3.999845,3.031877,1.872833,7.054854,-2.288377,-1.516307,8.295705,9.287189,-7.872095,0.298497,-9.018282,-5.801418,-7.893702,1.667072,-5.109747,9.498268,4.898547,9.254264,-3.779498,4.441087,5.886392,-8.102197,0.066528,4.807563,-6.762899,5.308099,-1.116491,-0.859453,4.198361,-9.470874,8.873214,-2.638421,-3.647060,3.636681,-7.846170,0.607823,0.434463,-7.697925,9.974477,-3.287012,-4.722095,-3.921859,5.466467,-7.976468,-9.992206,-2.365904,-1.781997,-1.855389,-4.441191,4.910593,9.375426,-3.122126,-7.555217,3.329728,-7.307886,-8.515628,4.141445,6.821214,6.357820,7.758335,9.480148,1.371001,-2.148997,-8.180321,-9.711926,-5.499055,2.970295,-4.937144,7.054748,3.140068,8.762374,3.583159,6.400085,9.872462,-5.660613,-6.980605,-3.720834,2.094144,-4.120639,2.493750,7.076467,-5.197889,-3.141873,6.768212,-3.099123,4.817060,-5.311628,-5.545225,5.109245,-3.740183,7.395785,6.165610,6.231581,-1.431207,3.222908,-1.052984,6.379615,5.419061,7.309779,-7.216324,3.816004,7.424427,-9.243401,2.600889,6.886718,2.792027,4.767446,-5.399232,7.905157,-3.582470,-9.053023,1.829959,6.779521,3.783332,0.985002,-8.770716,0.227141,-0.232555,4.712555,9.337486,-2.284971,6.904417,-5.540121,-2.482273,0.206795,-2.560422,2.549884,2.616635,-5.120644,3.054222,-8.609215,-9.517232,6.600533,2.061229,0.325424,8.153954,7.079625,7.527719,-1.225052,7.730919,-9.671077,7.370427,-7.044328,-7.448548,8.517102,-4.344496,5.768674,8.430749,-6.466920,9.901200,3.262521,2.492909,-1.584675,-6.840528,-3.249227,-1.036532,1.229168,-2.486430,-2.316366,-6.537261,-8.627207,-5.551070,-2.099891,-7.181169,-3.313306,-3.886880,-3.241751,8.883847,-6.301503,9.581355,7.090778,8.428973,1.643832,-4.471432,-4.362630,0.222326,-2.949488], dtype = "float32")#candidate|9462|(400,)|const|float32
call_9460 = relay.TupleGetItem(func_8745_call(relay.reshape(const_9461.astype('float32'), [4, 16, 1]), relay.reshape(const_9462.astype('float32'), [400,]), ), 4)
call_9463 = relay.TupleGetItem(func_8748_call(relay.reshape(const_9461.astype('float32'), [4, 16, 1]), relay.reshape(const_9462.astype('float32'), [400,]), ), 4)
output = relay.Tuple([call_9458,call_9460,const_9461,const_9462,])
output2 = relay.Tuple([call_9459,call_9463,const_9461,const_9462,])
func_9464 = relay.Function([], output)
mod['func_9464'] = func_9464
mod = relay.transform.InferType()(mod)
mutated_mod['func_9464'] = func_9464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9464_call = mutated_mod.get_global_var('func_9464')
call_9465 = func_9464_call()
output = call_9465
func_9466 = relay.Function([], output)
mutated_mod['func_9466'] = func_9466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9279_call = mod.get_global_var('func_9279')
func_9281_call = mutated_mod.get_global_var('func_9281')
call_9702 = relay.TupleGetItem(func_9279_call(), 0)
call_9703 = relay.TupleGetItem(func_9281_call(), 0)
func_8600_call = mod.get_global_var('func_8600')
func_8605_call = mutated_mod.get_global_var('func_8605')
const_9708 = relay.const([-1,-10,1,-8,-6,2,6,-9,-9,6,-10,9,3,2,-7,9,-10,-10,-3,-1,-5,-8,-2,-5,3,6,6,-7,-1,2,-4,9,2,-6,-6,-5,-1,-3,-3,3,2,7,9,6,-7,-9,1,-6,5,-9,8,-5,-10,-3,7,-7,7,8,10,-5,4,7,-2,-10,4,10,-7,2,-3,10,-10,10,3,-1,-2,1,10,3,2,1,-5,9,-5,-1,5,-10,-8,-2,8,5,2,8,-3,-6,-4,-10,-7,5,9,10,-5,9,-1,-6,4,1,-5,-10,7,3,10,-4,-2,8,-3,5,9,3,3,-10,-1,5,-7,-6,8,10,5,-6,3,8,2,-5,-7,2,-8,-9,1,-6,-8,7,-2,-7,-10,-3,4,-6,7,9,10,6,-2,-8,10,3,4,7,6,-2,4,9,1,8,9,-3,-7,-8,5,-3,-9,4,-8,-1,4,1,1,8,5,1,3,2,3,8,7,-3,-10,2,-8,2,-8,-2,3,2,-7,-4,5,10,-8,-5,2,1,-5,-9,6,6,4,-5,-9,-5,-10,-7,-6,2,-5,-9,5,10,5,-6,1,-6,-10,-2,-8,5,7,-2,9,7,10,-3,-7,6,2,-4,-4,8,3,-4,6,-8,3,3,1,8,-7,-8,-5,8,-6,10,5,5,7,-9,-1,5,-5,8,10,9,10,-2,4,2,-4,-2,-2,7,8,-4,2,-5,-10,5,2,7,-3,-6,-1,-9,-3,-4,-7,6,-6,4,-2,7,5,-9,-7,-8,-5,1,5,1,-10,4,-5,-3,-3,-2,-8,-4,-2,10,9,-2,-4,-2,-3,-6], dtype = "int16")#candidate|9708|(312,)|const|int16
const_9709 = relay.const([[False,False,True,True,False,True,True,True,False],[False,False,True,False,True,False,False,False,True],[True,True,False,False,False,False,False,False,True],[False,False,False,True,True,False,True,False,False],[False,True,True,False,False,True,True,False,True],[False,False,True,True,True,False,True,True,False],[True,False,False,True,False,True,True,True,False],[False,False,False,False,False,False,False,False,False],[True,False,False,False,False,False,True,True,True],[True,False,False,False,False,False,False,True,False],[True,False,False,True,False,False,False,True,True],[False,True,True,False,False,True,False,True,True],[False,False,False,True,False,True,True,False,True],[False,False,False,False,False,False,False,True,True],[True,True,False,False,True,True,True,True,True],[True,True,False,False,True,True,True,False,True],[False,False,True,True,False,True,True,False,True],[True,True,True,False,False,False,False,False,False],[True,True,True,True,False,True,True,True,False],[False,False,True,True,False,True,False,True,True],[False,False,True,True,True,False,False,False,False],[True,False,False,True,False,False,False,True,False],[True,False,True,False,True,True,True,False,True],[False,True,False,True,True,False,False,False,False],[True,True,False,True,False,False,False,True,False],[False,True,True,False,True,False,False,True,True],[True,False,True,True,False,False,True,True,True],[False,True,False,False,False,True,False,False,True],[False,False,False,True,False,True,False,False,False],[False,False,True,True,False,True,True,True,True],[True,False,False,True,False,False,True,False,False],[False,False,False,True,True,False,True,False,False],[False,False,True,True,True,True,False,False,True],[False,True,False,True,True,True,False,False,True],[False,True,False,False,True,False,True,False,True]], dtype = "bool")#candidate|9709|(35, 9)|const|bool
call_9707 = relay.TupleGetItem(func_8600_call(relay.reshape(const_9708.astype('int16'), [312,]), relay.reshape(const_9709.astype('bool'), [315,]), relay.reshape(call_9702.astype('float32'), [66,]), ), 0)
call_9710 = relay.TupleGetItem(func_8605_call(relay.reshape(const_9708.astype('int16'), [312,]), relay.reshape(const_9709.astype('bool'), [315,]), relay.reshape(call_9702.astype('float32'), [66,]), ), 0)
func_6695_call = mod.get_global_var('func_6695')
func_6696_call = mutated_mod.get_global_var('func_6696')
call_9711 = relay.TupleGetItem(func_6695_call(), 0)
call_9712 = relay.TupleGetItem(func_6696_call(), 0)
output = relay.Tuple([call_9702,call_9707,const_9708,const_9709,call_9711,])
output2 = relay.Tuple([call_9703,call_9710,const_9708,const_9709,call_9712,])
func_9726 = relay.Function([], output)
mod['func_9726'] = func_9726
mod = relay.transform.InferType()(mod)
output = func_9726()
func_9727 = relay.Function([], output)
mutated_mod['func_9727'] = func_9727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9279_call = mod.get_global_var('func_9279')
func_9281_call = mutated_mod.get_global_var('func_9281')
call_9744 = relay.TupleGetItem(func_9279_call(), 0)
call_9745 = relay.TupleGetItem(func_9281_call(), 0)
func_7019_call = mod.get_global_var('func_7019')
func_7022_call = mutated_mod.get_global_var('func_7022')
var_9757 = relay.var("var_9757", dtype = "float32", shape = (780,))#candidate|9757|(780,)|var|float32
var_9758 = relay.var("var_9758", dtype = "float64", shape = ())#candidate|9758|()|var|float64
call_9756 = relay.TupleGetItem(func_7019_call(relay.reshape(var_9757.astype('float32'), [390, 2]), relay.reshape(var_9758.astype('float64'), []), ), 1)
call_9759 = relay.TupleGetItem(func_7022_call(relay.reshape(var_9757.astype('float32'), [390, 2]), relay.reshape(var_9758.astype('float64'), []), ), 1)
func_5041_call = mod.get_global_var('func_5041')
func_5045_call = mutated_mod.get_global_var('func_5045')
var_9774 = relay.var("var_9774", dtype = "float64", shape = (1350,))#candidate|9774|(1350,)|var|float64
call_9773 = relay.TupleGetItem(func_5041_call(relay.reshape(var_9774.astype('float64'), [15, 9, 10]), relay.reshape(var_9774.astype('float64'), [15, 9, 10]), ), 0)
call_9775 = relay.TupleGetItem(func_5045_call(relay.reshape(var_9774.astype('float64'), [15, 9, 10]), relay.reshape(var_9774.astype('float64'), [15, 9, 10]), ), 0)
var_9781 = relay.var("var_9781", dtype = "float32", shape = (50, 15))#candidate|9781|(50, 15)|var|float32
bop_9782 = relay.mod(call_9756.astype('float64'), var_9781.astype('float64')) # shape=(50, 15)
bop_9785 = relay.mod(call_9759.astype('float64'), var_9781.astype('float64')) # shape=(50, 15)
output = relay.Tuple([call_9744,var_9757,var_9758,call_9773,var_9774,bop_9782,])
output2 = relay.Tuple([call_9745,var_9757,var_9758,call_9775,var_9774,bop_9785,])
func_9797 = relay.Function([var_9757,var_9758,var_9774,var_9781,], output)
mod['func_9797'] = func_9797
mod = relay.transform.InferType()(mod)
var_9798 = relay.var("var_9798", dtype = "float32", shape = (780,))#candidate|9798|(780,)|var|float32
var_9799 = relay.var("var_9799", dtype = "float64", shape = ())#candidate|9799|()|var|float64
var_9800 = relay.var("var_9800", dtype = "float64", shape = (1350,))#candidate|9800|(1350,)|var|float64
var_9801 = relay.var("var_9801", dtype = "float32", shape = (50, 15))#candidate|9801|(50, 15)|var|float32
output = func_9797(var_9798,var_9799,var_9800,var_9801,)
func_9802 = relay.Function([var_9798,var_9799,var_9800,var_9801,], output)
mutated_mod['func_9802'] = func_9802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8678_call = mod.get_global_var('func_8678')
func_8679_call = mutated_mod.get_global_var('func_8679')
call_9843 = func_8678_call()
call_9844 = func_8678_call()
func_6872_call = mod.get_global_var('func_6872')
func_6874_call = mutated_mod.get_global_var('func_6874')
var_9850 = relay.var("var_9850", dtype = "float32", shape = (780,))#candidate|9850|(780,)|var|float32
call_9849 = relay.TupleGetItem(func_6872_call(relay.reshape(var_9850.astype('float32'), [780,])), 2)
call_9851 = relay.TupleGetItem(func_6874_call(relay.reshape(var_9850.astype('float32'), [780,])), 2)
output = relay.Tuple([call_9843,call_9849,var_9850,])
output2 = relay.Tuple([call_9844,call_9851,var_9850,])
func_9860 = relay.Function([var_9850,], output)
mod['func_9860'] = func_9860
mod = relay.transform.InferType()(mod)
mutated_mod['func_9860'] = func_9860
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9861 = relay.var("var_9861", dtype = "float32", shape = (780,))#candidate|9861|(780,)|var|float32
func_9860_call = mutated_mod.get_global_var('func_9860')
call_9862 = func_9860_call(var_9861)
output = call_9862
func_9863 = relay.Function([var_9861], output)
mutated_mod['func_9863'] = func_9863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9279_call = mod.get_global_var('func_9279')
func_9281_call = mutated_mod.get_global_var('func_9281')
call_9914 = relay.TupleGetItem(func_9279_call(), 0)
call_9915 = relay.TupleGetItem(func_9281_call(), 0)
func_4181_call = mod.get_global_var('func_4181')
func_4185_call = mutated_mod.get_global_var('func_4185')
var_9921 = relay.var("var_9921", dtype = "float64", shape = ())#candidate|9921|()|var|float64
const_9922 = relay.const([9.538627,4.429468,0.722292,-8.326939,-7.176367,-4.495835,-7.344292,9.653227,-3.501857,-1.885356,-0.256781,-6.527449,-7.095982,-7.958323,0.603423,3.660365,0.008387,9.982958,9.216237,4.911361,1.420140,-7.168189,4.697157,-6.008261,-6.267645,8.883854,-2.039841,-1.928160,-7.512409,-4.251846,-7.754245,-2.199837,-7.593364,3.573291,8.799965,0.107186,-6.259483,3.466415,9.208792,-2.885900,-1.702954,5.812813,9.342354,6.402124,-8.989582,1.609324,2.294792,-3.779142,6.654925,0.231005,-2.336478,-1.185813,5.349574,-5.367133,1.629204,-7.651327,-3.315178,-8.913924,2.385652,-7.707944,7.185220,9.298947,9.137100,-8.185722,9.130334,-9.883024,6.346485,-4.470137,-7.802691,7.670539,2.492510,9.358605,3.657365,3.071807,7.365581,-0.083234,8.517864,9.432150,7.154049,-4.793867,4.628901,-2.009911,2.696928,5.366676,-5.957071,5.373817,-4.381380,0.188844,-8.040985,9.096140,-4.308732,-9.025558,3.771811,7.267670,6.166680,8.075763,-3.494442,8.719381,-7.267518,7.178800,-3.946196,0.112592,8.887728,-3.731611,8.188924,3.459597,-7.705479,-1.723433,4.930273,-4.087878,5.853827,7.649446,-4.053088,6.462570,-6.047305,8.640736,9.224050,3.261997,6.140733,-5.708249,3.926009,0.641345,4.751200,8.194467,8.560145,0.418780,7.847190,-3.533032,-9.602750,6.580313,-8.463955,0.799545,6.374414,-7.932860,-6.291408,6.956872,-2.994666,2.696971,-3.691140,-0.906216,9.766488,-8.279862,-5.220764,-9.231285,-0.913673,4.724172,-6.619451,-7.897763,-7.468064,-1.303100,1.327401,-1.929226,-9.124511,8.949362,9.706961,-8.209750,-9.864505,7.136949,4.087484,6.215762,8.864694,-9.120847,9.493205,6.167080,0.437721,-3.427066,-1.169389,-6.877938,0.082265,0.101689,4.369096,6.920169,8.093602,9.021075,-2.291800,-2.321525,3.411458,4.284504,-9.841125,-4.873467,-5.691341,-4.024909,-9.106536,-4.547425,1.959102,-1.042552,9.191938,-8.484216,-1.844002,-5.686626,-7.169399,6.169967,4.549813,-7.650826,9.337103,-4.365783,6.119537,-6.767186,4.357438,3.671106,9.465521,-5.847940,4.722359,8.386200,-5.354794,-6.804038,-2.009680,-8.122106,-0.982795,7.011066,-4.066380,-0.182507,8.951220,2.374820,8.874159,1.766194,-4.909766,5.881656,-1.143052,1.018389,-4.288361,7.444888,8.755119,7.431867,-6.941828,-0.329265,-2.783291,-4.904910,9.782699,-1.712685,8.023332,3.440759,4.813938,0.947731,5.716581,-2.918491,7.367343,3.516383,-3.174464,-6.736280,3.720645,5.897106,7.318368,4.713705,2.480936,9.290230,9.305774,-0.373153,-2.066215,-7.599785,-0.835010,7.338263,-6.422577,9.983976,6.584430,7.187297,-1.434885,-6.098224,2.574793,-5.489557,-2.132969,6.761443,7.458510,-1.097903,0.826768,2.536978,-5.874184,7.559053,8.259871,7.304735,3.796901,-7.244732,5.742960,1.549522,-3.405449,2.657362,-8.905207,9.766722,-6.318944,7.527058,-8.713312,6.577059,8.484810,-2.422717,2.057797,-8.466151,-2.788756,-7.117764,6.461944,-9.702650,-2.498895,-7.343237,-5.165311,-1.652818,-7.150639,5.472106,-7.744400,1.669328,1.057218,3.330711,3.552366,7.519456,-4.711155,1.824242,-5.376274,0.906734,4.012936,5.904759,5.496840,-8.995162,9.445905,3.361361,-7.813410,7.392329,-2.015700,4.750748,-2.150206,0.292655,-5.807051,6.786901,5.411872,5.171795,-4.675120,-0.412743,-0.554149,5.387740,-3.304065,-3.855788,5.244135,7.181629,-6.549733,3.113666,3.590307,2.089858,0.080155,-3.785152,3.302233,9.247391,-0.963526,-2.542180,-1.420813,-1.990153,-9.739185,-3.327862,9.040744,9.200910,-7.540035,-7.519615,9.622491,7.498245,-2.235709,1.159960,-4.467022,-1.256163,6.585925,9.562242,-7.920086,-5.069048,-5.288371,5.618594,-5.307600,6.555176,8.344627,2.554726,1.034245,-0.889743,-5.260507,-5.917429,-8.296680,-5.639600,8.507351,-8.993837,5.624118,-3.754276,5.859373,5.157767,-1.715287,-6.705311,3.263228,-2.398406,-7.329314,-7.224708,4.045101,2.986431,3.805484,9.215935,-3.204971,6.737823,-7.925221,3.609545,5.664307,-6.751369,-4.064566,9.956068,-6.394055,-5.448347,-5.958351,6.627723,5.729774,-9.156208,-3.644967,1.551743,0.467980,8.754048,-6.408767,2.065861,1.432874,6.331228,-6.035759,2.969994,7.641674,7.319227,9.165579,4.031188,-1.400470,0.245354,4.318298,4.740576,4.237705,-0.720408,9.824848,8.266158,5.329949,-0.915230,-2.476733,-9.733852,-5.959158,0.565485,8.295484,-7.350381,-2.535332,-4.206287,6.021540,-4.386503,-2.556443,-8.872288,-4.681599,2.809672,7.622999,5.605853,5.176428,5.256841,-3.563525,1.993303,1.005341,8.636339,-9.083246,2.765991,6.564241,-0.513012,-1.007442,9.699769,2.979510,1.257701,5.609055,-3.309021,-5.004523,-6.128908,-9.210218,-3.892621,9.318475,-3.375905,-1.420765,0.757451,6.069670,8.562377,0.915814,7.380009,7.836269,7.089251,2.186678,-4.083244,0.054132,-8.208907,-9.505606,2.110861,-6.531366,2.112254,0.236945,-3.212111,5.118082,-7.651770,5.372622,5.631072,-0.046341,9.696890,-3.123506,-1.082780,-8.490883,8.915517,9.194449,-8.888671,-8.413869,-3.647592,3.082418,5.082693,8.755631,9.151030,4.487907,7.518686,1.835736,4.786875,-5.089659,3.643232,4.987331,-6.680454,8.983410,-4.247281,-2.369607,7.001293,-8.095742,-1.839433,-7.382844,-1.177542,-8.352824,-7.510734,-5.300336,2.163231,1.528901,1.525801,-4.062373,3.227611,-4.451653,3.646981,0.182921,-2.431129,9.051504,6.547531,-7.698736,6.228918,0.121773,-8.630526,-7.733054,7.223171,-4.613640,-6.983313,-3.058069,-3.250282,6.944382,8.569042,-5.740702,-1.932909,7.347353,-8.935540,7.535671,-1.746707,2.082984,-6.029638,7.783658,3.424947,-9.883131,-1.419253,0.771406,-3.552243,-0.111704,9.325380,5.226444,2.937913,9.409232,2.436743,0.257018,-4.702830,-3.423394,-8.284626,-9.732287,-7.778950,9.405486,3.160673,7.142767,-2.375344,5.760638,6.777089,5.181541,3.790470,-6.592926,-7.335765,3.294409,-8.851911,4.817574,8.325614,-0.185883,0.052766,-2.956977,-2.576095,-6.571187,4.878596,7.856014,-8.898733,2.284773,2.096795,-6.725290,-2.390670,-9.920197,-1.944901,2.361390,4.459031,7.685953,-2.674679,2.048949,4.674782,9.471388,-6.072518,6.283920,3.483221,-6.827973,-4.977922,-9.062328,-4.255861,5.726027,5.078652,-3.347541,-3.511688,1.920863,1.977262,-9.587208,-5.261375,-3.560492,-8.403155,2.231762,-6.476005,-6.076645,1.883542,9.946361,-0.446716,-4.737195,-8.552742,-3.722410,-2.449490,9.255668,7.107816,-7.486356,8.074590,-7.390058,9.678928,2.844580,1.423337,-6.503145,4.823460,8.197760,1.591368,1.361006,-8.735791,-6.419658,6.964493,2.775327,4.097233,-0.943356,-8.350122,-4.620760,-3.265638,2.605221,-3.945302,-1.707710,-2.878567,0.869230,9.221474,2.174520,-6.994493,-8.335898,1.609126,-1.109253,-1.445447,0.135011,1.917438,-9.174450,2.231545,-0.250387,1.757758,8.799274,-1.272789,6.557713,5.616486,6.523122,5.872519,0.336047,0.285277,4.702999,-9.326326,-2.110538,2.113739,-8.608571,3.071690,-1.815174,0.413538,-8.597982,-9.491907,-2.706701,-9.337801,7.010410,7.237507,-3.519939,8.689996,-3.531775,-2.284496,1.852951,2.517394,-4.993938,-5.120703,-2.226713,8.775964,0.931689,-6.630444,1.082458,-7.634070,-2.237027,-6.873955,-8.117399,9.306297,1.870086,-4.760765,8.132304,-5.174156,-4.288702,-0.901012,8.257755,3.359527,6.024711,-3.388856,-6.147595,4.597490,-8.718676,8.017161,5.052003,-3.238940,-6.236493,-1.440355,-9.895643,5.440507,9.023186,2.282007,2.534564,-5.690156,9.285872,-9.951305,9.031272,-1.902146,3.655935,-6.961117,-6.417313,0.572035,6.757366,-9.712788,7.493447,-5.482804,9.395604,0.936415,-9.434970,1.667200,-4.462343,0.754070,-6.433921,6.482607,0.852019,-5.300450,-4.956128,-5.628851,4.245715,-5.677260,4.858271,-2.783240,-8.039657,1.505948,1.436097,-1.865548,-5.005715,4.346236,-2.855015,-5.612488,-4.075937,7.632616,5.181517,9.001083,5.796031,9.488916,-6.787241,4.400803,9.532048,-0.444951,-8.106690,-6.222771,-2.059433,2.797264,-3.155719,9.868266,-1.439550,-9.115002,-8.968898,8.499670,9.551333,-0.680565,-8.541272,-1.006460,9.022335,-1.487682,-6.298381,-1.595635,-0.897659,9.955042,-1.847784,1.646960,4.124462,-0.839590,3.291682,8.640657,-2.861605,7.143918,-5.703666,-9.425043,-5.779087,0.957184,5.504752,4.542688,6.929460,-8.737629,2.810918,-7.887119,7.393465,7.424811,-2.808593,0.584443,-7.413946,3.125239,6.555200,-8.946082,-1.167640,-8.873698,-6.648899,5.328976,-9.412238,7.234116,-0.684050,-5.936183,-0.097932,-1.736656,3.589821,6.913141,-6.420894,-0.526733,-2.474499,9.262912,-0.692837,-5.711512,-6.225673,-7.715980,7.402265,-3.360590,5.363372,-8.259847,-6.193125,1.267952,-1.096691,-8.109357,1.179589,-2.426114,8.132648,4.457858,1.343237,-5.868400,3.692169,-3.430079,-8.023348,-6.272726,-2.641496,9.551012,-7.885342,-6.760386,6.066416,0.082237,0.995437,-2.362733,-6.486256,-6.076007,3.847342,2.466367,2.518247,-4.301778,-4.468870,1.695314,4.417244,-0.472978,5.022079,-5.775925,8.818306,-5.653083,-7.121670,4.672360,-4.015173,-7.362572,1.295018,-2.540304,-0.486269,-9.786604,-7.902869,8.462394,8.271630,9.853230,-1.134819,2.682719,6.392185,-7.513130,1.560773,-1.436301,5.023113,0.738438,-1.561423,0.642299,-0.317805,-1.507867,4.051329,-3.332145,8.354748,-8.926825,-3.611082,2.757745,9.585916,3.547768,3.508114,-0.985594,-2.188875,2.429577,6.893337,2.772977,4.158519,-1.013600,0.385445,6.194281,-9.640039,-3.468035,7.364550,8.868107,5.004757,0.337132,-1.962917,2.039434,-9.152791,-4.723986,8.177820,9.714183,4.461561,-0.167967,4.591196,2.170965,1.223467,-7.945298,1.997311,1.678894,-6.667651,6.960093,-9.857053,7.241345,-9.611455,-9.877599,-7.452200,-8.739917,-9.876579,-1.683354,-8.651694,1.254831,-0.553160,-3.680083,7.230070,-0.862179,2.353192,1.621824,6.731816,-5.278203,-7.468336,9.468901,-4.414030,-4.408434,-3.110786,-7.300542,-7.654962,-5.616070,0.691695,-7.810528,-5.698313,-1.490041,-2.496919,2.831934,7.607248,4.113391,9.496710,-1.671608,-3.177486,-6.400203,7.925306,4.894840,-4.494735,-2.551684,2.849983,5.369439,-1.199983,7.858038,3.293760,-6.641981,-7.912979,-2.021346,-5.491714,9.270285,5.731029,-8.549722,6.904795,-3.267661,8.437743,5.522386,4.141181,7.815045,5.753125,-4.373790,9.650442,4.139690,5.258366,4.537042,-2.134224,-3.020855,-5.057357,-8.123017,7.583754,-1.655263,-0.075030,2.070942,-3.380003,8.237694,9.158110,-5.371727,-3.595230,-3.432701,9.604368,5.724363,-4.966579,3.996725,-9.757701,-4.413659,-7.520347,7.554975,8.374105,-2.567510,7.614073,8.756291,2.422088,2.703814,5.212053,5.433089,-4.581981,-3.087966,4.341244,0.593608,2.278135,3.704951,-4.036294,-3.792657,3.769921,6.635744,-6.179622,1.282765,-1.998602,0.575983,-7.370864,-6.684674,-2.509341,7.945060,-2.594437,8.863728,7.662857,2.608699,4.048628,4.318465,-2.621326,1.811269,2.391118,9.824634,-4.237749,2.836284,3.256771,2.479193,-0.749390,9.271827,8.864688,-6.667346,7.312395,1.527799,-0.416990,9.915197,0.166788,1.043428,9.015270,2.095129,-4.800532,-4.912470,-0.368894,0.706517,8.803477,-6.931624,5.063088,6.627290,-8.525676,-7.668807,3.492123,-8.758861,-6.135955,8.069823,-0.830391,9.402277,4.574547,-2.062621,6.893910,-1.308782,9.480890,-2.969912,0.475913,7.901949,-2.907861,-9.235807,-9.492632,-4.063498,5.073660,-7.229949,-2.463801,-6.207672,-7.081780,-5.191460,-9.955466,-2.758202,5.724162,-8.830313,-9.457660,-5.158769,1.124961,-9.849420,3.868302,1.042519,-8.109447,-9.447055,5.173129,-1.086790,-9.843070,-4.562028,8.583415,-8.514855,7.905235,8.017353,-2.547713,-5.416363,2.206939,1.934673,8.658992,2.279990,4.799792,3.792081,-5.544360,-1.484798,-8.050245,4.411409,3.938176,-3.487359,-0.307220,-7.944469,9.700104,4.484844,9.535597,-8.547297,5.235251,-5.036304,1.296128,1.024136,3.533120,-0.804075,-5.399547,3.374285,1.573249,-0.700513,7.655653,1.920424,4.625417,1.981305,1.541435,-9.875722,7.728331,9.960718,-5.472178,-5.151994,-6.931544,7.396099,-8.741790,-2.244700,-3.104064,-7.049992,7.175265,-3.763941,-3.107383,0.727503,0.669193,-6.130683,-0.765279,-9.670420,-0.575304,-2.939646,8.690869,-2.558804,-4.652182,-5.028216,2.685922,9.435274,-3.955553,-1.223839,3.744193,-3.400547,1.980466,-6.618301,8.876799,-4.619865,8.480898,-9.850956,-6.204146,7.498573,-8.670566,8.955327,-2.962111,-8.766271,-2.997639,7.604964,4.395868,6.987507,-4.440781,-4.099335,-2.112225,6.513517,-9.021197,-3.563631,-5.754110,5.956773,1.258571,1.002529,6.858522,-1.597439,-9.839890,-6.492725,-3.184017,-8.448453,0.036855,-3.508239,4.865549,8.450766,9.598364,-9.120618,5.756957,-3.094412,-0.323664,-6.546427,-7.769993,0.201807,-1.154945,-6.964116,8.227563,8.832771,6.186457,-0.642680,-1.602288,-1.203464,-7.919700,6.090366,4.126005,-3.891703,6.702374,3.020888,-0.125103,-8.510642,-6.366868,7.252665,1.892138,-2.056042,-7.242171,8.441996,2.269113,-3.092301,-7.773099,7.110223,-8.510765,1.104587], dtype = "float64")#candidate|9922|(1280,)|const|float64
call_9920 = func_4181_call(relay.reshape(var_9921.astype('float64'), []), relay.reshape(const_9922.astype('float64'), [16, 5, 16]), )
call_9923 = func_4181_call(relay.reshape(var_9921.astype('float64'), []), relay.reshape(const_9922.astype('float64'), [16, 5, 16]), )
func_8870_call = mod.get_global_var('func_8870')
func_8872_call = mutated_mod.get_global_var('func_8872')
call_9933 = func_8870_call()
call_9934 = func_8870_call()
func_7338_call = mod.get_global_var('func_7338')
func_7340_call = mutated_mod.get_global_var('func_7340')
var_9940 = relay.var("var_9940", dtype = "float64", shape = (135, 10))#candidate|9940|(135, 10)|var|float64
call_9939 = relay.TupleGetItem(func_7338_call(relay.reshape(var_9940.astype('float64'), [1350,])), 1)
call_9941 = relay.TupleGetItem(func_7340_call(relay.reshape(var_9940.astype('float64'), [1350,])), 1)
func_6974_call = mod.get_global_var('func_6974')
func_6976_call = mutated_mod.get_global_var('func_6976')
var_9943 = relay.var("var_9943", dtype = "float32", shape = (10, 78))#candidate|9943|(10, 78)|var|float32
call_9942 = relay.TupleGetItem(func_6974_call(relay.reshape(var_9943.astype('float32'), [780,])), 2)
call_9944 = relay.TupleGetItem(func_6976_call(relay.reshape(var_9943.astype('float32'), [780,])), 2)
output = relay.Tuple([call_9914,call_9920,var_9921,const_9922,call_9933,call_9939,var_9940,call_9942,var_9943,])
output2 = relay.Tuple([call_9915,call_9923,var_9921,const_9922,call_9934,call_9941,var_9940,call_9944,var_9943,])
func_9968 = relay.Function([var_9921,var_9940,var_9943,], output)
mod['func_9968'] = func_9968
mod = relay.transform.InferType()(mod)
mutated_mod['func_9968'] = func_9968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9968_call = mutated_mod.get_global_var('func_9968')
var_9970 = relay.var("var_9970", dtype = "float64", shape = ())#candidate|9970|()|var|float64
var_9971 = relay.var("var_9971", dtype = "float64", shape = (135, 10))#candidate|9971|(135, 10)|var|float64
var_9972 = relay.var("var_9972", dtype = "float32", shape = (10, 78))#candidate|9972|(10, 78)|var|float32
call_9969 = func_9968_call(var_9970,var_9971,var_9972,)
output = call_9969
func_9973 = relay.Function([var_9970,var_9971,var_9972,], output)
mutated_mod['func_9973'] = func_9973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8413_call = mod.get_global_var('func_8413')
func_8415_call = mutated_mod.get_global_var('func_8415')
call_9975 = relay.TupleGetItem(func_8413_call(), 0)
call_9976 = relay.TupleGetItem(func_8415_call(), 0)
output = call_9975
output2 = call_9976
func_9993 = relay.Function([], output)
mod['func_9993'] = func_9993
mod = relay.transform.InferType()(mod)
output = func_9993()
func_9994 = relay.Function([], output)
mutated_mod['func_9994'] = func_9994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7228_call = mod.get_global_var('func_7228')
func_7229_call = mutated_mod.get_global_var('func_7229')
call_10020 = relay.TupleGetItem(func_7228_call(), 2)
call_10021 = relay.TupleGetItem(func_7229_call(), 2)
func_8413_call = mod.get_global_var('func_8413')
func_8415_call = mutated_mod.get_global_var('func_8415')
call_10022 = relay.TupleGetItem(func_8413_call(), 0)
call_10023 = relay.TupleGetItem(func_8415_call(), 0)
output = relay.Tuple([call_10020,call_10022,])
output2 = relay.Tuple([call_10021,call_10023,])
func_10041 = relay.Function([], output)
mod['func_10041'] = func_10041
mod = relay.transform.InferType()(mod)
output = func_10041()
func_10042 = relay.Function([], output)
mutated_mod['func_10042'] = func_10042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9394_call = mod.get_global_var('func_9394')
func_9396_call = mutated_mod.get_global_var('func_9396')
call_10121 = relay.TupleGetItem(func_9394_call(), 0)
call_10122 = relay.TupleGetItem(func_9396_call(), 0)
output = relay.Tuple([call_10121,])
output2 = relay.Tuple([call_10122,])
func_10129 = relay.Function([], output)
mod['func_10129'] = func_10129
mod = relay.transform.InferType()(mod)
mutated_mod['func_10129'] = func_10129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10129_call = mutated_mod.get_global_var('func_10129')
call_10130 = func_10129_call()
output = call_10130
func_10131 = relay.Function([], output)
mutated_mod['func_10131'] = func_10131
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10191 = relay.var("var_10191", dtype = "float32", shape = (13, 2, 12))#candidate|10191|(13, 2, 12)|var|float32
uop_10192 = relay.sigmoid(var_10191.astype('float32')) # shape=(13, 2, 12)
output = relay.Tuple([uop_10192,])
output2 = relay.Tuple([uop_10192,])
func_10196 = relay.Function([var_10191,], output)
mod['func_10196'] = func_10196
mod = relay.transform.InferType()(mod)
mutated_mod['func_10196'] = func_10196
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10197 = relay.var("var_10197", dtype = "float32", shape = (13, 2, 12))#candidate|10197|(13, 2, 12)|var|float32
func_10196_call = mutated_mod.get_global_var('func_10196')
call_10198 = func_10196_call(var_10197)
output = call_10198
func_10199 = relay.Function([var_10197], output)
mutated_mod['func_10199'] = func_10199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10129_call = mod.get_global_var('func_10129')
func_10131_call = mutated_mod.get_global_var('func_10131')
call_10275 = relay.TupleGetItem(func_10129_call(), 0)
call_10276 = relay.TupleGetItem(func_10131_call(), 0)
output = call_10275
output2 = call_10276
func_10288 = relay.Function([], output)
mod['func_10288'] = func_10288
mod = relay.transform.InferType()(mod)
output = func_10288()
func_10289 = relay.Function([], output)
mutated_mod['func_10289'] = func_10289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6412_call = mod.get_global_var('func_6412')
func_6414_call = mutated_mod.get_global_var('func_6414')
call_10320 = relay.TupleGetItem(func_6412_call(), 0)
call_10321 = relay.TupleGetItem(func_6414_call(), 0)
output = relay.Tuple([call_10320,])
output2 = relay.Tuple([call_10321,])
func_10336 = relay.Function([], output)
mod['func_10336'] = func_10336
mod = relay.transform.InferType()(mod)
output = func_10336()
func_10337 = relay.Function([], output)
mutated_mod['func_10337'] = func_10337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6922_call = mod.get_global_var('func_6922')
func_6923_call = mutated_mod.get_global_var('func_6923')
call_10412 = relay.TupleGetItem(func_6922_call(), 0)
call_10413 = relay.TupleGetItem(func_6923_call(), 0)
func_5322_call = mod.get_global_var('func_5322')
func_5326_call = mutated_mod.get_global_var('func_5326')
const_10417 = relay.const([2,-2,9,-5,-9,-1,8,7,3,-2,-3,-9,-3,-7,1,-3,-5,5,-5,6,-9,6,-7,5,-8,-4,-1,4,-7,2,-8,-4], dtype = "int32")#candidate|10417|(32,)|const|int32
call_10416 = relay.TupleGetItem(func_5322_call(relay.reshape(const_10417.astype('int32'), [2, 1, 16]), relay.reshape(const_10417.astype('int32'), [2, 1, 16]), ), 2)
call_10418 = relay.TupleGetItem(func_5326_call(relay.reshape(const_10417.astype('int32'), [2, 1, 16]), relay.reshape(const_10417.astype('int32'), [2, 1, 16]), ), 2)
func_6695_call = mod.get_global_var('func_6695')
func_6696_call = mutated_mod.get_global_var('func_6696')
call_10419 = relay.TupleGetItem(func_6695_call(), 0)
call_10420 = relay.TupleGetItem(func_6696_call(), 0)
output = relay.Tuple([call_10412,call_10416,const_10417,call_10419,])
output2 = relay.Tuple([call_10413,call_10418,const_10417,call_10420,])
func_10422 = relay.Function([], output)
mod['func_10422'] = func_10422
mod = relay.transform.InferType()(mod)
mutated_mod['func_10422'] = func_10422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10422_call = mutated_mod.get_global_var('func_10422')
call_10423 = func_10422_call()
output = call_10423
func_10424 = relay.Function([], output)
mutated_mod['func_10424'] = func_10424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7788_call = mod.get_global_var('func_7788')
func_7789_call = mutated_mod.get_global_var('func_7789')
call_10501 = func_7788_call()
call_10502 = func_7788_call()
const_10512 = relay.const([[[-0.653000,8.461753],[-0.787163,5.932763],[-0.398367,5.029494],[6.461600,-3.328770],[8.219571,-8.338603],[0.173551,-2.323610],[-5.200575,5.923082],[6.743599,9.457264],[-1.281384,-9.024611],[-6.854953,-2.150228],[-7.820524,9.267028]],[[0.884893,-6.118689],[0.086744,-0.465014],[-0.974502,8.590145],[-5.288732,-5.344227],[8.133151,-5.644193],[-1.376673,-0.050947],[-7.193982,3.069324],[-1.796258,0.229274],[-7.263131,-9.627745],[-6.538077,-4.097741],[2.273199,-7.083702]],[[-8.480343,-3.980903],[-5.137566,-7.030243],[7.451550,6.705013],[1.763147,-9.157507],[2.409464,6.323870],[8.906790,-7.215596],[-1.251060,2.329969],[-4.363235,-1.841146],[-8.486664,3.122087],[5.808713,6.553978],[-2.380629,-9.766115]]], dtype = "float32")#candidate|10512|(3, 11, 2)|const|float32
bop_10513 = relay.bitwise_xor(call_10501.astype('int32'), relay.reshape(const_10512.astype('int32'), relay.shape_of(call_10501))) # shape=(3, 11, 2)
bop_10516 = relay.bitwise_xor(call_10502.astype('int32'), relay.reshape(const_10512.astype('int32'), relay.shape_of(call_10502))) # shape=(3, 11, 2)
output = relay.Tuple([bop_10513,])
output2 = relay.Tuple([bop_10516,])
func_10519 = relay.Function([], output)
mod['func_10519'] = func_10519
mod = relay.transform.InferType()(mod)
mutated_mod['func_10519'] = func_10519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10519_call = mutated_mod.get_global_var('func_10519')
call_10520 = func_10519_call()
output = call_10520
func_10521 = relay.Function([], output)
mutated_mod['func_10521'] = func_10521
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10535 = relay.var("var_10535", dtype = "float32", shape = (9, 1, 6))#candidate|10535|(9, 1, 6)|var|float32
uop_10536 = relay.asinh(var_10535.astype('float32')) # shape=(9, 1, 6)
func_7568_call = mod.get_global_var('func_7568')
func_7571_call = mutated_mod.get_global_var('func_7571')
var_10540 = relay.var("var_10540", dtype = "int8", shape = (945,))#candidate|10540|(945,)|var|int8
call_10539 = relay.TupleGetItem(func_7568_call(relay.reshape(var_10540.astype('int8'), [15, 7, 9]), relay.reshape(var_10540.astype('int8'), [15, 7, 9]), ), 0)
call_10541 = relay.TupleGetItem(func_7571_call(relay.reshape(var_10540.astype('int8'), [15, 7, 9]), relay.reshape(var_10540.astype('int8'), [15, 7, 9]), ), 0)
output = relay.Tuple([uop_10536,call_10539,var_10540,])
output2 = relay.Tuple([uop_10536,call_10541,var_10540,])
func_10551 = relay.Function([var_10535,var_10540,], output)
mod['func_10551'] = func_10551
mod = relay.transform.InferType()(mod)
var_10552 = relay.var("var_10552", dtype = "float32", shape = (9, 1, 6))#candidate|10552|(9, 1, 6)|var|float32
var_10553 = relay.var("var_10553", dtype = "int8", shape = (945,))#candidate|10553|(945,)|var|int8
output = func_10551(var_10552,var_10553,)
func_10554 = relay.Function([var_10552,var_10553,], output)
mutated_mod['func_10554'] = func_10554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10129_call = mod.get_global_var('func_10129')
func_10131_call = mutated_mod.get_global_var('func_10131')
call_10630 = relay.TupleGetItem(func_10129_call(), 0)
call_10631 = relay.TupleGetItem(func_10131_call(), 0)
output = call_10630
output2 = call_10631
func_10632 = relay.Function([], output)
mod['func_10632'] = func_10632
mod = relay.transform.InferType()(mod)
mutated_mod['func_10632'] = func_10632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10632_call = mutated_mod.get_global_var('func_10632')
call_10633 = func_10632_call()
output = call_10633
func_10634 = relay.Function([], output)
mutated_mod['func_10634'] = func_10634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9279_call = mod.get_global_var('func_9279')
func_9281_call = mutated_mod.get_global_var('func_9281')
call_10643 = relay.TupleGetItem(func_9279_call(), 0)
call_10644 = relay.TupleGetItem(func_9281_call(), 0)
func_9279_call = mod.get_global_var('func_9279')
func_9281_call = mutated_mod.get_global_var('func_9281')
call_10645 = relay.TupleGetItem(func_9279_call(), 0)
call_10646 = relay.TupleGetItem(func_9281_call(), 0)
func_8600_call = mod.get_global_var('func_8600')
func_8605_call = mutated_mod.get_global_var('func_8605')
const_10673 = relay.const([1,-7,-5,3,7,-3,10,-10,-4,10,-1,10,-9,5,8,-10,-3,-5,-4,-10,-6,-5,-9,-3,2,-9,-2,-4,-4,7,-1,2,6,2,6,10,-7,6,1,-8,-5,-7,6,6,-2,-1,-9,-9,-10,2,5,6,8,9,-3,2,4,3,-3,-9,3,10,-2,-7,-1,8,5,-1,10,-2,-9,-1,4,-4,-6,-3,-4,10,-3,-10,-10,-10,4,7,3,7,4,4,3,-6,-2,5,-4,-4,6,9,4,-2,-5,2,-8,10,8,-9,-4,7,6,2,9,-6,1,2,7,4,10,-9,-7,-10,5,-4,-6,4,3,1,5,-8,3,2,1,-3,1,1,5,3,-1,-8,9,1,10,-5,-9,1,-2,-3,8,6,-2,-9,8,-4,2,8,-5,-5,-8,2,-3,1,-6,10,2,3,-3,-8,6,-10,7,-10,-6,7,-5,-3,-2,6,9,-9,-2,-5,-7,-5,-9,1,-4,8,6,-4,-6,1,-1,5,-5,-3,7,3,4,-6,5,-1,-8,7,-4,-9,7,-8,9,8,-8,-2,-10,-10,4,-7,3,6,-7,-9,3,3,8,-8,-7,-2,7,1,-10,2,-6,3,-7,3,3,6,8,5,3,4,8,-6,-1,-4,7,-6,-5,4,-7,5,-9,-5,-10,-4,2,4,3,6,-6,-6,6,-8,9,2,-7,8,-10,4,3,-5,-5,6,-9,-1,-5,-8,6,-2,7,5,-3,-1,-5,-4,-10,-5,10,-2,-8,-1,-1,3,-4,6,-9,5,-3,-4,9,9,9,-4,-7,-5,1,-7,-5,-2,5,8,7,3,-10,-8,-7,8], dtype = "int16")#candidate|10673|(312,)|const|int16
const_10674 = relay.const([True,False,False,True,False,False,True,False,True,True,True,False,True,False,True,False,False,True,False,True,True,True,False,True,True,False,False,False,False,False,True,True,True,True,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,True,False,True,True,True,False,False,True,True,False,False,True,False,True,False,True,False,True,True,False,True,True,True,False,True,False,True,False,True,False,False,False,True,True,True,False,False,True,True,True,False,True,False,False,True,True,True,True,False,True,True,True,False,False,True,True,False,False,True,True,True,True,False,False,False,True,False,False,True,True,True,True,True,False,True,False,True,False,True,True,True,False,True,True,False,False,False,True,True,True,False,False,False,False,False,True,False,False,True,True,True,True,False,False,True,True,False,False,True,True,True,True,True,False,False,False,True,True,True,False,False,True,False,True,False,False,False,False,False,True,True,True,False,True,False,True,False,False,True,True,False,True,False,True,True,True,True,False,False,False,False,False,False,False,True,False,False,True,False,False,True,True,False,True,False,False,True,False,False,False,True,False,True,False,False,True,True,True,True,True,False,False,True,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,False,False,False,False,False,False,False,True,True,False,False,False,False,False,False,False,True,True,False,False,True,False,True,True,True,True,False,False,False,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,False,True,True,True,True,True,False,True,True,True,False,False,True,False,False,True,True,True,False,True,False,False], dtype = "bool")#candidate|10674|(315,)|const|bool
call_10672 = relay.TupleGetItem(func_8600_call(relay.reshape(const_10673.astype('int16'), [312,]), relay.reshape(const_10674.astype('bool'), [315,]), relay.reshape(call_10645.astype('float32'), [66,]), ), 3)
call_10675 = relay.TupleGetItem(func_8605_call(relay.reshape(const_10673.astype('int16'), [312,]), relay.reshape(const_10674.astype('bool'), [315,]), relay.reshape(call_10645.astype('float32'), [66,]), ), 3)
func_9207_call = mod.get_global_var('func_9207')
func_9211_call = mutated_mod.get_global_var('func_9211')
const_10686 = relay.const([[-0.463024,-9.859328,2.245901,-7.638670,3.610631,-7.703546,-3.427839,-4.436198,-6.709600,6.204969,-1.008745,1.317016],[-5.652776,-5.147944,-3.793643,6.448743,7.954174,4.379439,4.706519,-3.478921,-2.265075,-9.218771,0.513479,7.799304],[5.809297,-3.591899,1.574352,6.054448,-6.498916,-0.406610,-0.980532,-4.467073,3.170995,-4.169567,1.031349,3.563387],[8.231333,-5.917158,-3.775873,-9.627998,-8.468296,0.075748,-2.941161,8.119565,-1.449900,1.810285,-0.375002,7.870630],[9.553383,-5.222690,-3.070295,-1.114383,9.746543,-4.739927,8.140430,4.403601,0.911180,1.125701,-4.856343,-5.464788],[-4.619210,8.670447,0.974098,-3.898635,-3.824645,6.152756,4.753624,-8.910020,-7.333147,-5.374441,1.323574,-4.018268],[3.782046,8.581636,-7.486972,-4.162287,2.784485,5.069769,-9.599260,-1.422960,4.878545,8.713895,7.228535,5.091551],[-2.181399,0.684078,-8.699191,-7.708274,0.842626,6.050017,-5.135681,-5.755152,3.349643,-0.290040,-1.917870,-4.759235],[6.441492,-4.525490,3.595657,-9.694525,2.556709,6.947582,7.656498,1.856217,1.116618,9.732948,7.030422,-9.452373],[3.062709,-3.244219,4.937515,9.405721,2.899282,8.607390,-9.988548,-6.802112,-9.766860,7.247691,-8.185409,-6.146212],[7.536975,4.092517,-6.045445,7.018714,-6.316720,3.611909,-4.436255,-8.857292,-9.530213,-8.985884,-1.111013,-1.831539],[-1.625100,-7.289647,4.387620,3.102958,-0.208775,8.652743,-2.987062,6.603745,-7.643768,-5.555672,0.216802,-0.826401],[-4.944062,-2.488789,-7.052002,0.855808,-8.205344,7.880905,1.862885,-3.985247,9.877580,-5.505803,-6.417944,-1.298038],[-6.027931,4.844184,-4.436756,2.909760,-8.487146,8.219643,-9.639135,-5.987225,-7.857387,-9.488189,-7.652331,-7.248378],[-8.865412,8.729622,-3.743798,-7.285658,-3.243852,-3.492783,3.089539,6.532481,-3.363761,-5.508552,-6.312912,6.974688],[-6.422240,-5.812783,9.423838,-2.551671,6.803865,-6.139496,-6.437689,-1.795766,9.316687,8.291474,-2.749696,-7.685597],[0.073231,5.481376,9.391359,-1.719410,5.546688,-0.489750,9.644853,-4.609541,-9.294684,-8.949084,4.188921,7.215727],[-5.185224,-3.825334,-3.424670,9.693383,5.178560,5.676984,4.349993,2.387193,-4.700576,5.072970,-7.286313,-8.191170],[6.752778,7.782226,9.936231,9.407250,3.752077,-0.941851,-0.051615,5.959321,-5.319068,7.843798,3.047388,-8.952942],[-1.834452,9.733972,-6.225539,-9.769386,8.818686,-4.627858,-8.202793,-8.625128,5.355877,3.462823,-6.036136,-4.239041],[1.233485,-7.379314,-9.923058,-3.186316,3.099320,8.641535,6.383493,3.945891,-2.251923,1.155904,7.710043,-8.339450],[-1.138240,-1.699071,3.104730,-0.564426,-2.284357,0.740249,8.012102,-2.759340,7.950041,-7.810067,9.353579,2.220981],[-9.352223,-4.604187,-5.098101,-8.208749,0.986835,8.838762,2.028783,6.176251,0.266599,-4.660209,8.661942,8.021907],[9.947455,6.665667,5.996460,-1.888794,-4.277216,1.275516,8.067918,1.758942,-8.771972,2.632990,-3.462296,-7.329208],[7.697286,2.272371,6.127980,-8.921360,-3.559484,6.502769,-0.648889,6.392176,-6.127268,-0.191852,5.328378,-2.993265],[-3.203020,0.713905,0.829811,-7.534076,4.393058,2.451559,-2.576101,4.537623,4.934506,-7.763536,-9.292844,-7.130596],[-0.567113,-8.115309,7.529225,-8.239106,0.329085,-8.849158,6.522092,1.951740,-5.634202,6.215761,-9.247175,-3.167128],[8.000292,-9.498446,-9.356829,-6.544589,1.370709,-1.738574,-4.496763,-9.462513,1.856620,-9.729684,-8.747239,5.880573],[-3.344992,5.997565,0.383121,-2.210975,4.281372,-7.718631,-4.918764,-2.897317,8.196718,-8.488688,3.119838,9.852923],[6.477385,4.512769,-3.261474,8.387503,6.852134,4.870095,-8.681653,9.895446,-4.747327,6.073391,7.989791,-6.006560],[6.507893,-2.508270,-9.085810,7.580690,1.832626,7.478630,3.209153,-3.901492,6.149751,5.269688,1.486049,9.314804],[-6.496819,-4.223376,8.875659,-9.218028,7.936258,5.079765,2.502591,-2.655536,-3.633539,-2.198844,-9.061290,-9.482525],[-6.632178,9.775313,6.920465,-4.668997,9.762144,9.895256,1.683308,4.389868,-4.999878,-4.179111,4.880499,-4.742942],[-8.931062,3.314438,6.803302,1.148605,5.389357,4.203840,8.462244,-4.789435,0.482942,5.758672,-2.486697,6.213452],[-1.832484,-6.106941,-8.325179,5.064964,9.614794,7.187472,-9.200762,-2.777154,2.832711,-5.940276,3.115407,-9.916814],[-3.510407,-8.793368,-2.992544,8.176516,5.517643,5.702827,-1.270826,3.203272,1.301002,-4.312319,7.698930,-3.670019],[9.203970,3.227064,7.733493,4.319578,-8.161664,-5.317143,3.317544,7.145490,9.079049,1.709716,4.621223,9.402565],[1.595902,-3.218968,5.570928,-2.340379,-3.280554,5.905667,4.610409,1.745646,-8.204747,-1.556022,-3.924322,4.771404],[-2.553773,9.357298,6.770924,2.415117,4.390255,1.955290,-8.602587,2.251880,5.608258,-6.094552,8.116610,-2.949838],[-9.781680,2.966648,-2.574935,-7.376481,5.353658,-0.564098,0.291374,-5.322416,-3.725895,4.267484,7.424889,4.594202],[8.039946,5.054736,5.712605,2.227383,-2.581400,-0.044237,3.134087,-4.353818,9.181194,1.348840,-2.449950,5.308219],[1.061376,6.613810,4.236318,4.971666,-1.997875,5.245212,8.783561,5.593481,9.731199,-7.859193,3.718668,-7.590796],[-0.722691,5.529928,4.054539,9.196516,9.954841,3.003722,7.930204,7.724423,4.149483,4.414296,8.182682,-4.855874],[6.145302,8.648729,9.605959,2.988071,1.314719,-4.562600,0.256746,5.659377,-5.697866,1.175734,-0.642390,-4.650911],[5.986284,-1.144767,-3.297266,3.768034,3.309170,-6.685974,-2.411841,-1.518944,-3.255182,-9.905295,-6.599947,-8.261278],[-8.560681,-9.515101,6.394498,-8.899061,5.080712,0.962679,-4.089173,9.762664,-9.625395,-7.747614,0.695465,-9.680300],[-6.486529,6.392694,2.186734,0.407594,7.422508,-0.434942,-9.280960,4.416779,8.061072,-9.425120,5.472499,5.416143],[2.686505,4.098317,4.543444,4.822139,-0.742123,-8.744568,-0.890377,-1.374663,-0.374915,-8.336515,5.665979,-4.623554],[4.233099,-6.738600,-0.997107,-0.573838,-3.135340,-9.040964,9.310673,6.488818,-3.019320,3.891239,0.239886,-5.681319],[-5.168840,7.441641,-4.995548,-0.153200,-2.884853,-3.932862,2.846700,-6.786342,-6.297843,3.892756,-3.700306,-8.418972],[-1.202570,-8.533714,9.331984,3.575594,2.825684,7.333115,-0.343331,2.531458,7.935559,3.037654,-8.278526,-5.797596],[-2.403737,7.616431,-8.834908,7.311271,3.997212,-8.845158,-0.086901,9.689535,-1.165305,7.098985,-9.210606,2.516669],[6.903631,-0.189841,8.359961,-9.107552,-4.197276,-9.813716,6.723853,-8.285816,4.573137,5.597821,-5.416832,-4.205975],[-6.041605,-6.124674,-0.418419,-7.182104,-5.654043,-7.998832,1.986295,-4.274014,-8.085131,-5.908378,-9.050171,-5.123791],[0.696038,-9.610196,-9.602621,1.108379,-3.728240,-6.554326,0.899510,-8.990723,3.440792,2.148885,-2.267089,4.153608],[2.212008,-6.711065,-5.864763,7.920744,0.622460,3.191501,-3.761572,-7.701942,-5.916849,-8.229608,2.837055,-0.070865],[0.234751,5.747599,6.678303,-7.363220,-2.121578,-6.534227,9.508346,-8.716864,2.109719,1.374481,-6.874944,0.277330],[-9.468814,7.232245,-5.589528,-6.687869,3.209231,2.449272,-9.023967,8.728376,3.845323,3.296997,-7.528209,6.878418],[-8.030682,4.274828,-0.668264,2.438450,-6.791517,-8.233021,-1.329954,-7.025113,-4.315225,-3.804148,2.436514,5.130937],[-0.369091,-4.789419,-0.900071,-0.994268,-9.977622,-1.887959,-0.058032,7.974075,-2.512965,-0.194584,-9.202445,-7.742973],[-0.794643,-5.401758,0.990336,-7.874760,-9.829353,-5.627123,-1.920650,2.143209,-3.531066,1.835236,-0.062673,-5.786525],[-0.039809,0.466969,0.452625,4.278474,6.366900,-3.552519,2.069820,-5.359497,9.415314,9.748315,7.717280,-8.088068],[-4.388539,9.192670,-2.423813,2.861933,-5.761540,3.347508,-4.842297,5.228566,-1.149116,-2.464048,6.496661,-2.253999],[9.501993,-1.989699,-4.109991,6.362054,0.119424,7.787769,-6.328949,-9.976730,-3.373772,-4.484121,3.770476,-3.058300],[7.281592,4.120102,6.075260,4.358655,2.160070,6.234189,-2.564256,-6.161446,8.408405,8.037481,-7.280367,-8.810119],[-5.888085,-3.552363,2.940106,3.700511,5.339425,3.196220,-2.874677,-2.723498,-0.012324,-9.285654,-9.241672,-8.684857],[-7.333583,7.615664,-5.509749,9.913747,-0.275606,-8.136679,-3.174265,2.517968,-9.218050,-8.982113,0.963331,3.603523],[7.707177,9.919009,-5.047193,8.453199,1.230829,-2.817666,9.970730,-3.386692,6.731951,0.472617,5.973245,0.775530],[9.941259,-0.902310,-0.043129,-2.768438,0.246515,0.359537,-7.729135,8.831735,9.941503,9.665821,6.450248,9.962326],[-1.564286,3.801554,5.084439,2.144083,-3.714224,8.491798,0.788995,-9.248309,6.139358,5.407002,6.899593,-3.425647],[-2.292759,4.226030,1.580570,-8.286043,0.876193,0.920962,-6.778373,0.428716,0.186472,-4.737094,-1.795650,4.111781],[-3.679749,5.520437,4.379012,8.620867,9.069686,-7.562798,0.347029,-9.827070,-6.879395,9.673664,0.033684,4.321159],[1.806962,0.960170,9.916488,-8.210171,0.717483,5.455804,4.753656,-0.930376,1.451861,4.486346,0.367419,3.103059],[-6.190327,5.125194,0.621056,-2.303457,-4.899503,-5.983591,-3.981418,0.126698,6.611020,2.733483,7.904435,6.290404],[-7.687839,0.738942,4.528562,2.438959,1.930606,2.200549,0.739751,-4.270271,1.831374,8.636283,3.673509,-8.561668],[8.799590,2.188732,1.354372,5.314502,3.903578,-3.549429,4.567593,-9.111968,-9.573748,2.323234,8.046465,4.454821],[6.956234,3.599909,0.269287,0.324383,2.052753,-6.195600,3.569316,-9.443738,-2.984648,5.149542,-8.520253,8.088828],[5.948820,-5.982196,-2.103220,-3.595663,0.276542,-7.521319,9.156233,1.718183,-3.884395,9.300946,-3.308943,-8.247078],[-9.038602,-3.606068,-4.968647,2.107274,8.987043,-9.365996,9.838470,0.034122,-7.211245,-6.613048,4.678913,-4.504810],[0.730955,5.928395,2.738063,-5.848187,-4.838646,-4.939002,-2.071841,-1.242414,-6.842073,7.609894,0.126235,-2.060050],[-4.029333,4.776210,-5.473663,1.044060,-7.696982,0.636608,0.265317,4.938294,9.984782,-2.495122,-3.421754,5.990712],[1.378046,-7.017179,6.396284,8.297048,5.559743,8.281998,-0.741674,5.345846,4.803548,4.373780,6.408782,-7.589249],[-4.173267,-9.244885,-2.155723,3.724380,8.297890,-8.541647,-2.398457,-2.207246,3.809279,-2.218636,0.376551,-3.182270],[-5.893588,9.296673,-7.650906,-3.314484,-5.264166,8.270945,-8.785018,-6.240299,5.652638,-9.231976,-0.103430,1.648696],[-1.817799,-0.087532,-1.557995,2.260200,-0.902597,-2.421339,-5.995496,3.396070,2.219978,6.915564,-9.309454,4.787200],[5.931095,2.817123,8.074364,3.277996,-0.870255,2.219725,-2.962940,-2.067533,9.224704,0.389466,7.670980,-1.421000],[-5.138341,2.868976,7.065972,-0.649641,-6.808510,1.253595,-8.695181,-3.988477,-8.061451,1.580171,-6.709060,2.299527],[-9.881954,7.039586,9.001065,3.344023,-0.467810,-6.162217,4.858844,-7.649037,6.617715,6.091211,-5.759244,-0.705541],[2.795305,6.214694,5.265798,1.759442,6.853868,-1.504376,-1.423285,-5.588950,-4.400521,5.431938,7.034244,0.830757],[8.173018,8.465709,-9.513130,-3.528818,8.050501,4.605582,-7.611077,7.094955,-0.287297,-5.226459,7.509459,6.054053]], dtype = "float64")#candidate|10686|(90, 12)|const|float64
var_10687 = relay.var("var_10687", dtype = "bool", shape = (48,))#candidate|10687|(48,)|var|bool
call_10685 = relay.TupleGetItem(func_9207_call(relay.reshape(const_10686.astype('float64'), [1080,]), relay.reshape(var_10687.astype('bool'), [48,]), ), 1)
call_10688 = relay.TupleGetItem(func_9211_call(relay.reshape(const_10686.astype('float64'), [1080,]), relay.reshape(var_10687.astype('bool'), [48,]), ), 1)
func_4518_call = mod.get_global_var('func_4518')
func_4523_call = mutated_mod.get_global_var('func_4523')
var_10704 = relay.var("var_10704", dtype = "float32", shape = (240,))#candidate|10704|(240,)|var|float32
const_10705 = relay.const(-2.505906, dtype = "float64")#candidate|10705|()|const|float64
call_10703 = relay.TupleGetItem(func_4518_call(relay.reshape(var_10704.astype('float32'), [1, 15, 16]), relay.reshape(call_10685.astype('float32'), [400,]), relay.reshape(const_10705.astype('float64'), []), ), 6)
call_10706 = relay.TupleGetItem(func_4523_call(relay.reshape(var_10704.astype('float32'), [1, 15, 16]), relay.reshape(call_10685.astype('float32'), [400,]), relay.reshape(const_10705.astype('float64'), []), ), 6)
func_6946_call = mod.get_global_var('func_6946')
func_6948_call = mutated_mod.get_global_var('func_6948')
call_10713 = relay.TupleGetItem(func_6946_call(relay.reshape(call_10645.astype('float32'), [3, 11, 2])), 0)
call_10714 = relay.TupleGetItem(func_6948_call(relay.reshape(call_10645.astype('float32'), [3, 11, 2])), 0)
func_8097_call = mod.get_global_var('func_8097')
func_8098_call = mutated_mod.get_global_var('func_8098')
call_10720 = relay.TupleGetItem(func_8097_call(), 0)
call_10721 = relay.TupleGetItem(func_8098_call(), 0)
func_4518_call = mod.get_global_var('func_4518')
func_4523_call = mutated_mod.get_global_var('func_4523')
call_10735 = relay.TupleGetItem(func_4518_call(relay.reshape(var_10704.astype('float32'), [1, 15, 16]), relay.reshape(call_10685.astype('float32'), [400,]), relay.reshape(const_10705.astype('float64'), []), ), 4)
call_10736 = relay.TupleGetItem(func_4523_call(relay.reshape(var_10704.astype('float32'), [1, 15, 16]), relay.reshape(call_10685.astype('float32'), [400,]), relay.reshape(const_10705.astype('float64'), []), ), 4)
func_7521_call = mod.get_global_var('func_7521')
func_7525_call = mutated_mod.get_global_var('func_7525')
var_10753 = relay.var("var_10753", dtype = "float64", shape = (1350,))#candidate|10753|(1350,)|var|float64
call_10752 = relay.TupleGetItem(func_7521_call(relay.reshape(call_10713.astype('float32'), [3, 11, 2]), relay.reshape(var_10753.astype('float64'), [1350,]), ), 0)
call_10754 = relay.TupleGetItem(func_7525_call(relay.reshape(call_10713.astype('float32'), [3, 11, 2]), relay.reshape(var_10753.astype('float64'), [1350,]), ), 0)
func_9236_call = mod.get_global_var('func_9236')
func_9238_call = mutated_mod.get_global_var('func_9238')
call_10786 = relay.TupleGetItem(func_9236_call(), 0)
call_10787 = relay.TupleGetItem(func_9238_call(), 0)
func_7600_call = mod.get_global_var('func_7600')
func_7602_call = mutated_mod.get_global_var('func_7602')
call_10799 = func_7600_call(relay.reshape(call_10645.astype('float32'), [3, 11, 2]))
call_10800 = func_7600_call(relay.reshape(call_10645.astype('float32'), [3, 11, 2]))
output = relay.Tuple([call_10643,call_10645,call_10672,const_10673,const_10674,call_10685,const_10686,var_10687,call_10703,var_10704,const_10705,call_10713,call_10720,call_10735,call_10752,var_10753,call_10786,call_10799,])
output2 = relay.Tuple([call_10644,call_10646,call_10675,const_10673,const_10674,call_10688,const_10686,var_10687,call_10706,var_10704,const_10705,call_10714,call_10721,call_10736,call_10754,var_10753,call_10787,call_10800,])
func_10804 = relay.Function([var_10687,var_10704,var_10753,], output)
mod['func_10804'] = func_10804
mod = relay.transform.InferType()(mod)
mutated_mod['func_10804'] = func_10804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10804_call = mutated_mod.get_global_var('func_10804')
var_10806 = relay.var("var_10806", dtype = "bool", shape = (48,))#candidate|10806|(48,)|var|bool
var_10807 = relay.var("var_10807", dtype = "float32", shape = (240,))#candidate|10807|(240,)|var|float32
var_10808 = relay.var("var_10808", dtype = "float64", shape = (1350,))#candidate|10808|(1350,)|var|float64
call_10805 = func_10804_call(var_10806,var_10807,var_10808,)
output = call_10805
func_10809 = relay.Function([var_10806,var_10807,var_10808,], output)
mutated_mod['func_10809'] = func_10809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6412_call = mod.get_global_var('func_6412')
func_6414_call = mutated_mod.get_global_var('func_6414')
call_10833 = relay.TupleGetItem(func_6412_call(), 0)
call_10834 = relay.TupleGetItem(func_6414_call(), 0)
output = relay.Tuple([call_10833,])
output2 = relay.Tuple([call_10834,])
func_10838 = relay.Function([], output)
mod['func_10838'] = func_10838
mod = relay.transform.InferType()(mod)
output = func_10838()
func_10839 = relay.Function([], output)
mutated_mod['func_10839'] = func_10839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9464_call = mod.get_global_var('func_9464')
func_9466_call = mutated_mod.get_global_var('func_9466')
call_10852 = relay.TupleGetItem(func_9464_call(), 2)
call_10853 = relay.TupleGetItem(func_9466_call(), 2)
output = call_10852
output2 = call_10853
func_10861 = relay.Function([], output)
mod['func_10861'] = func_10861
mod = relay.transform.InferType()(mod)
mutated_mod['func_10861'] = func_10861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10861_call = mutated_mod.get_global_var('func_10861')
call_10862 = func_10861_call()
output = call_10862
func_10863 = relay.Function([], output)
mutated_mod['func_10863'] = func_10863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9394_call = mod.get_global_var('func_9394')
func_9396_call = mutated_mod.get_global_var('func_9396')
call_10884 = relay.TupleGetItem(func_9394_call(), 0)
call_10885 = relay.TupleGetItem(func_9396_call(), 0)
func_9207_call = mod.get_global_var('func_9207')
func_9211_call = mutated_mod.get_global_var('func_9211')
var_10916 = relay.var("var_10916", dtype = "float64", shape = (1080,))#candidate|10916|(1080,)|var|float64
const_10917 = relay.const([True,True,True,True,True,True,False,False,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,True,False,False,False,False,True,False,True,True,False,True,False,False,True,False,False,True,True,True], dtype = "bool")#candidate|10917|(48,)|const|bool
call_10915 = relay.TupleGetItem(func_9207_call(relay.reshape(var_10916.astype('float64'), [1080,]), relay.reshape(const_10917.astype('bool'), [48,]), ), 4)
call_10918 = relay.TupleGetItem(func_9211_call(relay.reshape(var_10916.astype('float64'), [1080,]), relay.reshape(const_10917.astype('bool'), [48,]), ), 4)
func_4769_call = mod.get_global_var('func_4769')
func_4772_call = mutated_mod.get_global_var('func_4772')
const_10920 = relay.const(True, dtype = "bool")#candidate|10920|()|const|bool
call_10919 = relay.TupleGetItem(func_4769_call(relay.reshape(const_10920.astype('bool'), [])), 4)
call_10921 = relay.TupleGetItem(func_4772_call(relay.reshape(const_10920.astype('bool'), [])), 4)
func_7290_call = mod.get_global_var('func_7290')
func_7292_call = mutated_mod.get_global_var('func_7292')
call_10924 = func_7290_call()
call_10925 = func_7290_call()
var_10929 = relay.var("var_10929", dtype = "bool", shape = (6, 10, 4))#candidate|10929|(6, 10, 4)|var|bool
bop_10930 = relay.logical_or(call_10919.astype('bool'), relay.reshape(var_10929.astype('bool'), relay.shape_of(call_10919))) # shape=(6, 10, 4)
bop_10933 = relay.logical_or(call_10921.astype('bool'), relay.reshape(var_10929.astype('bool'), relay.shape_of(call_10921))) # shape=(6, 10, 4)
func_7338_call = mod.get_global_var('func_7338')
func_7340_call = mutated_mod.get_global_var('func_7340')
var_10941 = relay.var("var_10941", dtype = "float64", shape = (1350,))#candidate|10941|(1350,)|var|float64
call_10940 = relay.TupleGetItem(func_7338_call(relay.reshape(var_10941.astype('float64'), [1350,])), 0)
call_10942 = relay.TupleGetItem(func_7340_call(relay.reshape(var_10941.astype('float64'), [1350,])), 0)
func_9464_call = mod.get_global_var('func_9464')
func_9466_call = mutated_mod.get_global_var('func_9466')
call_10948 = relay.TupleGetItem(func_9464_call(), 0)
call_10949 = relay.TupleGetItem(func_9466_call(), 0)
output = relay.Tuple([call_10884,call_10915,var_10916,const_10917,const_10920,call_10924,bop_10930,call_10940,var_10941,call_10948,])
output2 = relay.Tuple([call_10885,call_10918,var_10916,const_10917,const_10920,call_10925,bop_10933,call_10942,var_10941,call_10949,])
func_10957 = relay.Function([var_10916,var_10929,var_10941,], output)
mod['func_10957'] = func_10957
mod = relay.transform.InferType()(mod)
var_10958 = relay.var("var_10958", dtype = "float64", shape = (1080,))#candidate|10958|(1080,)|var|float64
var_10959 = relay.var("var_10959", dtype = "bool", shape = (6, 10, 4))#candidate|10959|(6, 10, 4)|var|bool
var_10960 = relay.var("var_10960", dtype = "float64", shape = (1350,))#candidate|10960|(1350,)|var|float64
output = func_10957(var_10958,var_10959,var_10960,)
func_10961 = relay.Function([var_10958,var_10959,var_10960,], output)
mutated_mod['func_10961'] = func_10961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7906_call = mod.get_global_var('func_7906')
func_7908_call = mutated_mod.get_global_var('func_7908')
call_11045 = relay.TupleGetItem(func_7906_call(), 0)
call_11046 = relay.TupleGetItem(func_7908_call(), 0)
output = call_11045
output2 = call_11046
func_11053 = relay.Function([], output)
mod['func_11053'] = func_11053
mod = relay.transform.InferType()(mod)
output = func_11053()
func_11054 = relay.Function([], output)
mutated_mod['func_11054'] = func_11054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8348_call = mod.get_global_var('func_8348')
func_8350_call = mutated_mod.get_global_var('func_8350')
call_11136 = relay.TupleGetItem(func_8348_call(), 0)
call_11137 = relay.TupleGetItem(func_8350_call(), 0)
output = relay.Tuple([call_11136,])
output2 = relay.Tuple([call_11137,])
func_11158 = relay.Function([], output)
mod['func_11158'] = func_11158
mod = relay.transform.InferType()(mod)
mutated_mod['func_11158'] = func_11158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11158_call = mutated_mod.get_global_var('func_11158')
call_11159 = func_11158_call()
output = call_11159
func_11160 = relay.Function([], output)
mutated_mod['func_11160'] = func_11160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10861_call = mod.get_global_var('func_10861')
func_10863_call = mutated_mod.get_global_var('func_10863')
call_11161 = func_10861_call()
call_11162 = func_10861_call()
const_11163 = relay.const([-7.314560,-0.530153,-1.260745,2.402515,-1.033327,-0.828276,1.669739,-1.342500,-4.735707,-1.566585,4.382821,-3.738732,-8.144103,-8.995571,0.212553,-1.837869,3.694700,1.533604,-3.361583,6.424692,-4.811375,-6.551301,-8.472883,-8.277435,1.000955,-6.688465,-9.493772,-5.497575,-4.777669,-0.770126,0.250095,-2.698404,-9.906552,-0.665842,-2.592136,6.396662,0.742547,-0.691484,-6.169437,-4.296743,0.050851,0.224014,-6.665147,-9.076036,-5.843925,-9.406396,-4.990710,-8.172404,-0.394381,9.884925,4.944261,0.703776,-8.935535,-7.710517,-0.710829,-0.339963,1.216548,0.812223,-9.643712,3.506514,0.604174,-0.393557,-5.070026,-5.680835], dtype = "float32")#candidate|11163|(64,)|const|float32
bop_11164 = relay.bitwise_or(call_11161.astype('int64'), relay.reshape(const_11163.astype('int64'), relay.shape_of(call_11161))) # shape=(64,)
bop_11167 = relay.bitwise_or(call_11162.astype('int64'), relay.reshape(const_11163.astype('int64'), relay.shape_of(call_11162))) # shape=(64,)
func_8171_call = mod.get_global_var('func_8171')
func_8175_call = mutated_mod.get_global_var('func_8175')
var_11185 = relay.var("var_11185", dtype = "float64", shape = (1815,))#candidate|11185|(1815,)|var|float64
const_11186 = relay.const([-8.783088,-6.089402,7.668331,6.413115,4.518498,-1.116869,-9.844385,-7.569039,-0.778388,-9.912330,-9.806938,-1.465667,-8.601948,-5.308452,9.562346,4.434784,-9.289704,9.583904,5.654435,-6.977634,0.423887,2.052462,0.103594,1.591826,4.369964,-6.261731,3.800148,-8.440439,5.429542,4.746402,8.820124,-7.238363,1.790045,5.865609,8.628700,6.904861,-7.777693,-6.557747,6.899914,-8.245666,4.904353,-1.551202,4.650125,7.146264,6.979529,9.894934,9.587449,-2.973196,-9.249001,6.987407,5.018904,-5.916306,-3.890122,-0.177097,-6.653658,-1.385654,9.751668,5.520429,0.783890,-6.754412,5.717390,1.640576,6.946641,5.595673,2.469984,7.329635,-7.941631,5.875907,1.158716,-6.367333,-5.104006,5.156601,3.389383,-0.687636,6.843010,-8.577952,-8.876783,-6.073151,8.405658,2.616157,-0.972446,-4.276199,2.909265,4.227650,9.581781,-9.531588,-8.347638,5.205753,-3.028166,5.169184,-6.298168,5.221898,6.023210,5.298981,0.163979,-9.511494,3.685039,-7.550889,-1.585364,6.005678,3.924033,9.118936,-3.861067,-2.314027,-5.639562,-4.250582,4.986449,7.910348,7.251024,2.561056,-0.418824,4.383695,-8.425502,-6.326552,5.463746,-2.243229,3.283860,6.668696,9.891541,2.653759,5.072495,-5.314549,4.474331,5.069990,-0.818900,7.597520,-1.969598,5.815043,0.287908,0.947178,2.622054,8.238763,4.665324,-4.099452,-8.119143,-7.539826,-3.370412,-7.563689,9.760847,-9.938903,2.719697,-3.399268,-2.070740,-6.162282,6.879272,2.680708,-8.686506,7.711175,6.720776,-6.466254,5.159149,7.247543,5.140874,9.388920,7.995561,2.244345,-1.206988,1.364750,4.609140,-8.036089,1.721218,5.177496,-1.796967,-8.956484,0.372640,-1.041648,9.844617,-7.683656,4.965713,8.387091,3.369217,4.852891,-0.583134,2.398990,8.760077,-9.659140,8.907855,-1.035867,4.591636,7.499198,3.154795,6.232118,8.637516,6.886101,-7.069398,3.956758,5.276557,2.649667,9.580609,6.634582,-0.971852,-6.305076,-6.731576,0.754628,3.163120,-6.097468,-4.845740,3.006540,6.731319,0.883276,-1.394886,6.629027,0.546816,1.401276,1.609213,7.813468,4.437624,2.241845,-4.162952,8.526481,3.241638,-4.025953,1.763808,8.316481,7.193933,-0.938622,-7.890167,4.628866,-9.504946,-5.684439,-4.370913,8.390184,3.448246,6.433126,-8.154111,7.674946,-3.612819,4.498987,-8.071904,-2.497866,8.162085,2.429322,-8.571394,-1.432498,7.227944,2.531162,-2.158848,9.551211,6.265171,-2.425952,9.294296,-5.035287,1.955975,-4.739966,-6.178869,1.120295,4.806418,5.041775,-1.082129,3.004572,2.961281,3.638964,7.211928,5.266999,2.366054,-1.837653,-0.557185,-5.867054,4.850724,1.560159,0.076228,7.794125,8.326432,-3.093168,-9.316277,5.687456,-9.109915,-6.768018,-9.924895,1.563486,0.255582,-0.675876,-2.787028,1.563448,1.318847,2.088833,-4.308063,-3.537089,-5.996358,2.858737,-1.211447,-2.230444,4.247275,-9.035192,-8.284577,2.236560,-1.418862,4.806724,-0.336616,-1.876247,1.170083,-2.873726,-1.456573,8.937149,2.410790,-3.473337,-7.569674,1.584805,5.824855,4.870861,4.798371,3.854117,-0.804871,-2.469986,4.530032,4.659519,-5.445541,-0.116674,-2.176036,0.922732,-0.325280,4.891754,-7.597714,-0.802062,-1.326526,-6.444636,-7.251402,0.524843,-2.728988,9.312084,-5.855910,3.291941,-6.675186,-0.059305,5.130824,1.341738,7.979943,-9.464928,6.689527,0.984691,-8.892992,6.456861,3.549344,-3.782011,-2.503588,1.556996,-1.737737,7.041136,8.120711,3.747307,-9.054261,-8.034050,1.868348,4.002470,-0.285452,-4.832299,-0.938656,7.285961,2.396560,-6.940782,-6.578696,-7.665908,-3.715014,6.191485,1.386261,-5.197843,3.390107,8.905195,-6.260749,8.646769,9.287262,5.716878,1.516226,3.952314,-6.745759,-9.818060,-1.800396,7.649763,8.242975,-1.697743,4.787209,-0.993578,6.344605,3.041854,-4.617875,-1.479077,3.894399,-7.875447,6.823695,2.283442,1.226209,-8.671981,-0.807172,-1.942636,-0.532141,6.338936,7.226224,0.689960,2.208106,-2.723941,3.820057,-3.342607,6.803580,-3.895400,-5.489091,-3.462200,0.370415,4.556284,5.632423,0.370179,-8.422706,6.020015,-3.245354,8.873996,-3.133477,-0.786104,-1.041938,-7.717280,3.214795,-6.068384,-1.487834,2.600132,5.704831,9.397595,-9.307342,3.109900,2.622695,-5.494877,8.394999,-8.988528,-3.968275,4.304709,9.184577,-5.163300,-3.205480,-4.212366,6.714972,1.704934,8.169619,5.430923,3.669691,-8.256158,-4.805610,0.366364,-4.295603,4.528932,-8.949290,-7.724292,-5.785232,-7.155421,0.759076,3.046551,-0.349191,-9.546617,5.600541,8.299926,-2.386631,-7.110760,-0.445687,-1.167227,1.222810,9.788428,-7.962957,2.876520,-8.099316,-4.003090,-0.387127,2.783574,-7.566393,-7.648989,6.142255,-2.909679,-3.051641,-7.076955,-3.942660,3.588717,-6.588079,0.529021,-3.856870,1.155540,-1.343231,9.523720,4.821943,8.629394,-9.566514,-3.862330,1.289812,4.987220,2.209048,0.180123,-1.899781,6.433280,5.670414,4.680250,3.630254,0.767551,-9.846546,-6.625977,9.991452,6.112314,-2.984217,0.912799,0.857884,5.458638,8.945550,-9.117409,3.313914,-6.864605,5.891188,1.426720,5.946981,-2.383613,4.842915,5.257331,5.884516,-9.312203,-5.993450,1.262518,-2.005204,-5.145937,1.264655,4.406591,-7.879021,-0.278108,2.883603,-8.320940,-3.360731,9.747643,-6.636216,-9.218250,4.413133,0.069641,-5.556171,5.729799,2.594106,-2.987120,2.335383,0.993263,-2.623593,0.489807,0.088350,-5.643399,-3.214179,3.892033,-6.504165,-0.707961,-0.183495,-5.112228,6.725735,1.368624,5.713353,8.751043,5.416525,2.531806,-9.964171,-6.302549,-8.255793,6.433836,-6.695759,6.079500,-0.267198,-3.447885,9.711321,-4.388000,3.050308,9.757298,3.498225,7.295664,-4.282027,-3.377322,0.028910,-4.679066,7.435142,-3.135448,5.948625,7.243824,-2.717058,-4.548600,-2.939662,-1.877082,1.633821,-1.678055,-8.782156,3.355325,-9.095093,-1.249066,-4.910383,-6.540746,-6.569819,1.966132,-6.473278,-3.910069,8.442256,1.431717,3.532522,6.125676,1.354021,4.371366,1.807246,-5.150687,3.952309,4.635245,-2.549582,8.335254,-4.902931,-0.003843,3.143229,1.518318,9.264443,-6.147470,-6.071731,8.371927,-1.840652,-1.907959,-1.561175,3.670901,7.260109,3.222277,-8.454425,-8.885558,-0.111387,-8.677138,4.051040,-5.106998,-1.433071,7.998827,-6.838084,-3.900272,-4.821348,-7.400930,-0.156446,-6.043705,-9.842435,6.820582,-4.929380,8.918593,-0.821047,8.814246,-1.883507,-2.792985,-0.904358,4.159496,1.887684,6.689845,-1.911615,-7.509083,-8.218717,-1.859088,-7.921096,1.298156,-7.612802,7.122930,-8.258627,-4.830756,-5.024847,5.319069,4.279872,6.452064,4.112984,-8.758118,-4.518288,-8.932754,7.697977,4.505421,-1.919213,-0.747099,-0.654108,2.506028,-6.330370,1.878937,-8.353193,-9.153514,5.953912,-9.132631,-3.615904,0.154722,4.927610,0.149659,-6.997958,6.967377,-0.756423,0.328262,9.721169,5.988134,2.645625,4.122646,-8.385847,6.747761,3.288283,-0.053921,-0.068711,4.672772,2.173944,-3.181883,1.174304,-0.700240,0.190943,-1.645810,-1.175389,0.624667,-1.518899,6.417568,-5.806425,4.895647,1.307779,9.959547,7.905098,7.015204,-1.080062,-4.627885,6.395162,2.105785,7.155996,-9.022155,0.062685,2.425461,-1.601721,-6.507086,5.487444,-2.386113,0.560623,-4.601207,-5.162461,6.478318,6.440842,6.599020,-1.362328,0.850503,-5.464315,9.484921,9.465672,-1.834755,-8.958743,-2.798791,-4.633608,-9.305276,8.058236,-4.108463,-4.882185,-3.457220,2.993924,9.641311,-6.720142,6.180320,-5.400521,-9.306689,2.662233,6.329725,-7.619174,1.991342,-9.929272,-1.827711,-3.206550,-7.875222,3.870821,-2.575977,-2.613270,-2.510488,2.434910,0.502699,0.667144,4.551622,-1.502012,-7.836948,9.773113,1.054654,8.482945,6.953542,-6.412800,-0.715083,-1.190557,4.814439,-3.915166,7.408488,6.018089,3.182222,-0.362362,-0.427412,0.090927,9.808316,-3.082191,1.009520,7.636744,-3.952738,-7.004302,9.152816,8.472212,5.837350,-0.612858,7.529903], dtype = "float32")#candidate|11186|(780,)|const|float32
call_11184 = relay.TupleGetItem(func_8171_call(relay.reshape(var_11185.astype('float64'), [11, 11, 15]), relay.reshape(const_11186.astype('float32'), [780,]), ), 2)
call_11187 = relay.TupleGetItem(func_8175_call(relay.reshape(var_11185.astype('float64'), [11, 11, 15]), relay.reshape(const_11186.astype('float32'), [780,]), ), 2)
output = relay.Tuple([bop_11164,call_11184,var_11185,const_11186,])
output2 = relay.Tuple([bop_11167,call_11187,var_11185,const_11186,])
func_11188 = relay.Function([var_11185,], output)
mod['func_11188'] = func_11188
mod = relay.transform.InferType()(mod)
var_11189 = relay.var("var_11189", dtype = "float64", shape = (1815,))#candidate|11189|(1815,)|var|float64
output = func_11188(var_11189)
func_11190 = relay.Function([var_11189], output)
mutated_mod['func_11190'] = func_11190
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11229 = relay.var("var_11229", dtype = "int8", shape = (2, 12, 1))#candidate|11229|(2, 12, 1)|var|int8
var_11230 = relay.var("var_11230", dtype = "int8", shape = (2, 12, 11))#candidate|11230|(2, 12, 11)|var|int8
bop_11231 = relay.less_equal(var_11229.astype('bool'), var_11230.astype('bool')) # shape=(2, 12, 11)
output = bop_11231
output2 = bop_11231
func_11243 = relay.Function([var_11229,var_11230,], output)
mod['func_11243'] = func_11243
mod = relay.transform.InferType()(mod)
var_11244 = relay.var("var_11244", dtype = "int8", shape = (2, 12, 1))#candidate|11244|(2, 12, 1)|var|int8
var_11245 = relay.var("var_11245", dtype = "int8", shape = (2, 12, 11))#candidate|11245|(2, 12, 11)|var|int8
output = func_11243(var_11244,var_11245,)
func_11246 = relay.Function([var_11244,var_11245,], output)
mutated_mod['func_11246'] = func_11246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10838_call = mod.get_global_var('func_10838')
func_10839_call = mutated_mod.get_global_var('func_10839')
call_11294 = relay.TupleGetItem(func_10838_call(), 0)
call_11295 = relay.TupleGetItem(func_10839_call(), 0)
func_10861_call = mod.get_global_var('func_10861')
func_10863_call = mutated_mod.get_global_var('func_10863')
call_11297 = func_10861_call()
call_11298 = func_10861_call()
func_7667_call = mod.get_global_var('func_7667')
func_7669_call = mutated_mod.get_global_var('func_7669')
call_11318 = relay.TupleGetItem(func_7667_call(), 1)
call_11319 = relay.TupleGetItem(func_7669_call(), 1)
output = relay.Tuple([call_11294,call_11297,call_11318,])
output2 = relay.Tuple([call_11295,call_11298,call_11319,])
func_11328 = relay.Function([], output)
mod['func_11328'] = func_11328
mod = relay.transform.InferType()(mod)
mutated_mod['func_11328'] = func_11328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11328_call = mutated_mod.get_global_var('func_11328')
call_11329 = func_11328_call()
output = call_11329
func_11330 = relay.Function([], output)
mutated_mod['func_11330'] = func_11330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7459_call = mod.get_global_var('func_7459')
func_7461_call = mutated_mod.get_global_var('func_7461')
call_11358 = func_7459_call()
call_11359 = func_7459_call()
func_1815_call = mod.get_global_var('func_1815')
func_1817_call = mutated_mod.get_global_var('func_1817')
var_11361 = relay.var("var_11361", dtype = "bool", shape = ())#candidate|11361|()|var|bool
call_11360 = func_1815_call(relay.reshape(var_11361.astype('bool'), []))
call_11362 = func_1815_call(relay.reshape(var_11361.astype('bool'), []))
output = relay.Tuple([call_11358,call_11360,var_11361,])
output2 = relay.Tuple([call_11359,call_11362,var_11361,])
func_11375 = relay.Function([var_11361,], output)
mod['func_11375'] = func_11375
mod = relay.transform.InferType()(mod)
mutated_mod['func_11375'] = func_11375
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11376 = relay.var("var_11376", dtype = "bool", shape = ())#candidate|11376|()|var|bool
func_11375_call = mutated_mod.get_global_var('func_11375')
call_11377 = func_11375_call(var_11376)
output = call_11377
func_11378 = relay.Function([var_11376], output)
mutated_mod['func_11378'] = func_11378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6695_call = mod.get_global_var('func_6695')
func_6696_call = mutated_mod.get_global_var('func_6696')
call_11404 = relay.TupleGetItem(func_6695_call(), 0)
call_11405 = relay.TupleGetItem(func_6696_call(), 0)
uop_11414 = relay.asinh(call_11404.astype('float64')) # shape=(3, 11, 2)
uop_11416 = relay.asinh(call_11405.astype('float64')) # shape=(3, 11, 2)
output = relay.Tuple([uop_11414,])
output2 = relay.Tuple([uop_11416,])
func_11419 = relay.Function([], output)
mod['func_11419'] = func_11419
mod = relay.transform.InferType()(mod)
output = func_11419()
func_11420 = relay.Function([], output)
mutated_mod['func_11420'] = func_11420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7077_call = mod.get_global_var('func_7077')
func_7078_call = mutated_mod.get_global_var('func_7078')
call_11448 = func_7077_call()
call_11449 = func_7077_call()
func_34_call = mod.get_global_var('func_34')
func_37_call = mutated_mod.get_global_var('func_37')
var_11469 = relay.var("var_11469", dtype = "int16", shape = (15,))#candidate|11469|(15,)|var|int16
call_11468 = relay.TupleGetItem(func_34_call(relay.reshape(var_11469.astype('int16'), [15, 1])), 0)
call_11470 = relay.TupleGetItem(func_37_call(relay.reshape(var_11469.astype('int16'), [15, 1])), 0)
func_10336_call = mod.get_global_var('func_10336')
func_10337_call = mutated_mod.get_global_var('func_10337')
call_11471 = relay.TupleGetItem(func_10336_call(), 0)
call_11472 = relay.TupleGetItem(func_10337_call(), 0)
output = relay.Tuple([call_11448,call_11468,var_11469,call_11471,])
output2 = relay.Tuple([call_11449,call_11470,var_11469,call_11472,])
func_11493 = relay.Function([var_11469,], output)
mod['func_11493'] = func_11493
mod = relay.transform.InferType()(mod)
var_11494 = relay.var("var_11494", dtype = "int16", shape = (15,))#candidate|11494|(15,)|var|int16
output = func_11493(var_11494)
func_11495 = relay.Function([var_11494], output)
mutated_mod['func_11495'] = func_11495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8283_call = mod.get_global_var('func_8283')
func_8284_call = mutated_mod.get_global_var('func_8284')
call_11497 = relay.TupleGetItem(func_8283_call(), 2)
call_11498 = relay.TupleGetItem(func_8284_call(), 2)
output = call_11497
output2 = call_11498
func_11503 = relay.Function([], output)
mod['func_11503'] = func_11503
mod = relay.transform.InferType()(mod)
output = func_11503()
func_11504 = relay.Function([], output)
mutated_mod['func_11504'] = func_11504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11503_call = mod.get_global_var('func_11503')
func_11504_call = mutated_mod.get_global_var('func_11504')
call_11519 = func_11503_call()
call_11520 = func_11503_call()
func_8966_call = mod.get_global_var('func_8966')
func_8974_call = mutated_mod.get_global_var('func_8974')
const_11529 = relay.const([False,False,True,True,False,True,True,False,True,False,False,False,False,True,False,False,False,False,True,True,False,False,True,False,False,False,False,False,True,False,False,True,False,False,True,False,True,False,False,False,False,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,True,False,True,False,False,True,True,True,True,False,True,False,False,False,False,False,False,True,True,False,True,False,True,False,False,False,True,True,True,False,True,False,False,False,False,True,False,False,False,True,False,True,False,True,True,False,True,False,True,False,False,True,False,True,True,True,False,False,False,True,False,True,False,True,False,False,False,False,False,False,True,True,True,True,False,True,False,True,True,True,False,True,False,False,True,True,True,True,True,True,False,False,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,False,False,True,False,False,False,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,False,True,False,True,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,True,True,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,True,True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False,False,True,False,True,False,False,False,True,True,True,False,False,True,False,True,False,True,True,False,True,True,False,True,True,True,False,True,False,False,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,True,True,False,False,False,False,True,True,False,False,False,False,False,False,False,False,True,True,True,True,True,True,False,False,True,True,True,False,True,True,False,False,False], dtype = "bool")#candidate|11529|(315,)|const|bool
const_11530 = relay.const([[2.997647,5.708664,-1.903082,1.467185,-0.856031,-7.413508,9.323508,-9.200003,-0.599313,-0.395258,0.419006,0.335526,3.750410,-0.247433,8.256238,-7.948095,8.810164,0.738195,-2.637694,-3.187301,-5.201701,-3.405151,-7.892433,-1.808053,1.737419,-4.105890,-0.078529,4.437552,-2.690104,0.070007,6.829962,-0.648612,-9.828363,-2.236072,-8.509855,6.867667,0.376314,4.284126,-9.520792,4.344977,-8.551383,-0.407547,1.047335,-3.750239,1.806425,5.190343,1.503674,8.326038,-4.097140,1.937072,-7.962651,7.227500,-1.438517,0.207460,-0.725173,-4.190864,-3.917012,-6.035158,-7.142383,4.320753,-5.992222,-0.903380,-3.991885,2.476433,5.297188,-2.309361,5.736393,5.516162,-9.174392,7.120763,0.043323,2.314106,-9.873944,-3.728435,-2.772799,0.247014,-5.074350,-3.162323,6.383572,1.053477,-7.879480,1.714280,-0.714871,9.185994,5.367352,8.118467,-5.049490,6.940326,-8.880862,3.469291,4.995050,-0.332414,-0.945729,8.069740,-6.542387,-1.028625,-4.896905,1.336322,2.035294,6.408864,9.121115,9.295341,7.820352,-0.492386,-9.408213,-7.843165,-8.786192,-4.603906,8.990032,9.373976,-5.359429,4.339233,3.633841,6.802012,8.151612,9.182652,-4.186216,4.273799,7.013078,0.380652,1.111702,-0.513060,-5.243598,4.100729,-0.246240,-2.043554,-1.214622,6.088526,-1.423726,-1.326016,4.550447,-0.374934,0.704747,7.123758,8.218663,-5.826210,-6.141026,1.695610,2.549455,-2.275865,4.810931,7.363336,-3.746852,5.558734,2.523451,5.668427,4.400859,-0.264661,5.944239,-8.947095,1.587704,3.245185,7.773700,-0.805700,3.795139,-6.110051,4.231719,8.499637,-0.956537,-5.007580,-0.519158,-8.019747,2.581484,-5.320340,-2.970768,-4.980608,-4.970896,6.766686,-9.523764,-4.926338,-6.159026,-8.649676,-6.026434,-7.672071,-2.550004,4.052947,-3.196364,-0.872171,-1.241910,-2.741556,6.674219,-5.847523,-6.930624,9.123732,-6.875349,6.709416,-5.061074,-7.083043,7.643965,3.495683,-2.059480,-2.052378,-4.979425,-6.480166,-2.778962,5.146392,6.004495,6.923062,3.767213,-0.066430,-4.413746,9.625798,7.355583,-9.484659,-6.537480,-3.201390,-6.784917,4.069422,-4.107474,3.552081,-1.375990,-9.276229,3.134579,1.882020,9.321934,-5.660131,2.388529,-1.760068,1.996675,7.390184,0.615919,-6.564021,2.275054,-6.887919,-3.698339,-0.124247,2.790409,-0.509866,-4.737401,5.562134,-7.734610,8.242827,8.883602,-6.997366,-3.446235,-8.479328,-0.682536,5.485384,-7.659488,9.315407,-5.103216,1.258669,-6.066559,-7.980461,-3.115500,-4.238138,4.101380,-4.247550,-1.397962,3.099516,5.709553,-6.339037,4.062066,7.214085,3.377384,-8.058909,-4.059201,7.175927,0.622580,9.151516,-4.008765,-9.673643,7.936463,-7.789580,-3.522299,2.935463,-2.700629,7.423091,7.623249,2.786238,4.465633,-5.110716,-5.329012,-8.730950,5.607766,0.333282,-1.740528,8.280740,-9.809642,6.063932,-2.473285,-0.901868,-5.424076,-2.564966,-8.782217,-4.899094,1.024455,3.435287,0.850248,2.541700,6.115878,-7.461091,6.819587,-1.066924,1.745745,-6.141410,-8.984185,-8.079522,-1.748897,-0.749710,2.239304,-8.032257,-7.772904,-5.630540,0.081193,-2.553180,-8.865981,-0.627816,7.140980,7.284789,-1.737192,-0.347606,2.732275,5.199590,6.510055,-4.013638,6.498823,2.524134,5.155104,9.517123,2.982181,9.006412,-7.767398,4.340934,-7.218544,-3.612952,-9.674700,3.361303,-9.509829,8.223248,7.943072,-4.090803,-9.865403,-4.462634,8.851058,8.658655,3.477413,-8.899138,-2.114395,1.603081,-4.593967,-9.256574,-8.730987,-0.695872,-8.018243,-7.969585,-1.493266,-1.464931,-0.931260,-3.068806,-0.542158,9.415605,-7.038130,6.648870,0.152632,-9.595218,8.389233,1.108960,-9.784178,-0.097003,4.154781,-8.635179,4.402852,0.131517,6.530187,8.690775,0.832758,-4.501720,-1.638432,-5.274506,-1.953985,0.507195,5.564185,-2.732823,3.133404,3.119089,3.011971,-0.151826,-2.510945,1.765924,0.530349,-1.330785,4.316369,-4.950397,-0.576060,6.188131,1.303379,-3.136996,9.233007,1.917426,3.687770,-3.416439,-8.482520,8.949309,-6.796272,1.297135,9.561360,-4.779498,-9.051957,-0.312753,4.075407,1.029251,1.639652,-4.728627,-8.379205,7.741120,-4.947276,1.813085,-2.327019,2.470753,4.717838,-4.589355,-3.303794,9.731031,7.292869,-3.395987,2.610006,-8.850999,8.272961,-6.164030,-1.204077,-3.313063,4.057921,0.675213,-7.628967,-0.013641,1.740598,9.429849,2.849780,-1.326706,-9.809360,4.189741,8.649262,-1.196998,-3.650777,-7.098505,-2.742419,6.553270,-0.223145,9.851181,-5.439603,-4.351272,-0.071438,7.028314,-8.399501,9.581011,-6.161178,1.744388,-4.822297,8.640756,-5.784455,5.654617,-2.641940,-4.950702,8.659276,4.183434,3.989537,-2.901232,5.147893,4.571091,1.273593,0.184643,0.829745,6.760149,-2.928075,5.061384,3.683784,-6.026935,5.191669,-4.515249,-3.632055,-8.189386,-9.379404,-4.772271,6.051878,6.161361,-3.644482,-2.726765,2.742992,2.038764,-4.978768,-6.750866,5.453890,3.715902,5.700018,1.961348,-1.682984,7.249093,-9.070139,-3.625852,6.091232,7.717550,-5.290963,-7.094462,9.212675,-5.841197,-6.580629,6.290274,1.446367,-6.813438,2.024697,-9.861384,-4.579237,-5.671640,4.762155,-1.134204,-2.201171,-7.749606,9.540154,5.111902,-5.281042,1.831674,-7.833459,-7.570760,2.081668,0.558575,5.595573,-9.818310,7.030431,-5.252051,-2.964067,-9.311313,-0.277253,1.365458,5.919103,0.743852,-4.889662,-5.145615,4.441461,-1.391044,3.915545,7.352980,-2.418342,-7.788726,-0.991992,-0.624027,4.668488,-7.517946,-1.523270,-2.950903,-1.029253,5.842916,-2.971980,1.136067,8.442460,-8.136828,0.217871,8.278988,-8.669798,-4.784213,-9.184443,2.664088,6.076656,-6.278729,1.701570,5.584616,-1.015951,3.934682,-4.530766,-1.474569,-8.079011,-8.913031,5.525149,7.757001,-5.347552,-7.318612,3.119218,-2.246614,1.700222,-3.183254,5.837450,-9.388169,-1.609452,-4.092363,1.626703,-6.064636,-7.796406,3.768910,-7.057294,1.072018,-9.740024,-2.718216,5.171915,-3.234105,4.008081,8.168387,-5.751317,-3.072472,0.910280,0.619370,7.640984,3.639896,1.888256,2.180917,6.753671,-9.792397,7.528964,8.030301,4.415576,1.672757,-7.012259,-9.314236,3.939983,-3.480680,4.094639,2.029325,2.244368,-5.299349,7.007336,3.902700,-2.163596,3.353491,-3.016983,-2.687626,-4.351228,-4.291840,3.993717,-2.299604,3.262707,6.609416,-2.539499,1.405523,9.328915,-5.209587,-1.228079,-5.043273,6.313918,-4.863336,-8.479208,-3.428692,-2.450915,-8.681189,2.445058,-6.020061,9.130146,3.337928,-3.790693,4.033991,7.701513,6.818206,3.467730,-3.823468,5.611409,-3.620101,-6.982797,-8.908803,9.287558,-3.332722,1.494168,8.068276,-3.144672,3.978853,-2.162101,9.491688,-0.830727,3.762986,-7.367025,6.298289,-0.520858,7.126871,-6.135663,9.097517,-7.507579,-3.759876,5.661348,-3.136819,-4.128871,-4.621269,8.463551,-7.281948,-9.432595,0.858613,-0.101344,-3.063218,7.329506,0.321890,-7.700155,5.795524,-4.444613,-2.408006,-8.335363,4.503959,-9.655853,3.199631,9.263638,-4.786185,1.168453,-8.136240,-0.796400,-1.701492,1.399474,4.908025,-8.003418,-2.875255,-5.072914,-2.491094,-9.323526,9.326345,-4.763148,-9.101182,2.562064,6.948653,-0.719815,-8.551040,2.370341,-6.309977,-1.304830,-0.835106,4.249503,5.782480,0.289877,-7.017945,1.503422,6.686008,-4.342651,-0.436921,-8.225834,-1.535492,5.767202,7.301577,2.060482,1.610902,3.441242,-6.362955,7.913653,-1.237282,-2.063943,-7.006359,-3.681850,3.467726,5.574532,-8.530394,5.182041,-0.956667,5.295116,0.020138,-4.545868,-0.305023,-4.074493,-0.709154,-6.655769,4.347226,6.168548,7.576198,6.405056,-9.178729,-1.413395,-6.999145,6.496102,-7.429772,-8.506155,4.167954,4.955968,-5.065879,-2.739875,9.980556,8.952535,1.674967,-6.492418,-6.447493,8.795007,-6.611572,-4.097366,-5.000634,1.837354,-3.707197,-4.077023,-0.471639,-2.819199,-3.107540,7.695604,3.745476,-4.294019,1.057843,9.854629,-1.056563,-6.591644,-0.453156,9.301166,-7.069144]], dtype = "float32")#candidate|11530|(1, 780)|const|float32
var_11531 = relay.var("var_11531", dtype = "float64", shape = (18,))#candidate|11531|(18,)|var|float64
var_11532 = relay.var("var_11532", dtype = "float64", shape = ())#candidate|11532|()|var|float64
var_11533 = relay.var("var_11533", dtype = "float64", shape = (1280,))#candidate|11533|(1280,)|var|float64
var_11534 = relay.var("var_11534", dtype = "bool", shape = (12, 30))#candidate|11534|(12, 30)|var|bool
call_11528 = relay.TupleGetItem(func_8966_call(relay.reshape(const_11529.astype('bool'), [315,]), relay.reshape(const_11530.astype('float32'), [10, 78]), relay.reshape(var_11531.astype('float64'), [18,]), relay.reshape(var_11532.astype('float64'), []), relay.reshape(var_11533.astype('float64'), [1280,]), relay.reshape(var_11534.astype('bool'), [360, 1]), ), 8)
call_11535 = relay.TupleGetItem(func_8974_call(relay.reshape(const_11529.astype('bool'), [315,]), relay.reshape(const_11530.astype('float32'), [10, 78]), relay.reshape(var_11531.astype('float64'), [18,]), relay.reshape(var_11532.astype('float64'), []), relay.reshape(var_11533.astype('float64'), [1280,]), relay.reshape(var_11534.astype('bool'), [360, 1]), ), 8)
output = relay.Tuple([call_11519,call_11528,const_11529,const_11530,var_11531,var_11532,var_11533,var_11534,])
output2 = relay.Tuple([call_11520,call_11535,const_11529,const_11530,var_11531,var_11532,var_11533,var_11534,])
func_11538 = relay.Function([var_11531,var_11532,var_11533,var_11534,], output)
mod['func_11538'] = func_11538
mod = relay.transform.InferType()(mod)
var_11539 = relay.var("var_11539", dtype = "float64", shape = (18,))#candidate|11539|(18,)|var|float64
var_11540 = relay.var("var_11540", dtype = "float64", shape = ())#candidate|11540|()|var|float64
var_11541 = relay.var("var_11541", dtype = "float64", shape = (1280,))#candidate|11541|(1280,)|var|float64
var_11542 = relay.var("var_11542", dtype = "bool", shape = (12, 30))#candidate|11542|(12, 30)|var|bool
output = func_11538(var_11539,var_11540,var_11541,var_11542,)
func_11543 = relay.Function([var_11539,var_11540,var_11541,var_11542,], output)
mutated_mod['func_11543'] = func_11543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7836_call = mod.get_global_var('func_7836')
func_7837_call = mutated_mod.get_global_var('func_7837')
call_11561 = relay.TupleGetItem(func_7836_call(), 1)
call_11562 = relay.TupleGetItem(func_7837_call(), 1)
func_2733_call = mod.get_global_var('func_2733')
func_2739_call = mutated_mod.get_global_var('func_2739')
const_11564 = relay.const([7.138826,-8.508946,1.024939,3.220604,6.516925,-7.003685,1.578545,-0.795311,-3.461822,4.536180,-2.174966,8.133925,6.629879,6.145589,4.801266,-9.094416,-1.764079,-9.359574,-4.598150,5.101415,-3.380453,-6.262017,-7.434673,-9.705137,7.850852,2.251386,2.504595,-0.992573,-7.787976,5.401910,6.638356,-5.235025,-1.224093,3.125382,4.228685,0.051098,0.171550,8.430865,-2.051738,-0.086761,9.091090,4.529664,-5.931055,9.325154,-3.734613,8.608216,-7.187667,0.521152,-8.986836,-4.935796,8.667942,1.460087,2.473667,-6.271884,-4.037991,6.329947,1.520282,-3.944313,-1.011245,-5.794076,3.348001,-7.338947,1.842386,-3.198788,8.851203,2.088428,-8.150663,0.821606,2.307720,9.896807,-5.246875,-2.594698,-0.688763,5.506196,-8.910249,2.365748,1.800467,-0.408937,1.005434,9.863284,5.578824,5.699804,9.304058,0.950117,-5.127831,6.956212,8.669446,-6.064087,-7.371786,2.970178,6.977204,-0.339831,-3.210425,-2.676323,-0.492715,-2.767604,-3.014484,6.291844,-4.057647,7.779352,-6.886061,3.837338,-8.883410,2.101003,-2.451520,9.244666,0.040536,-3.490921,-4.105188,9.117513,-6.898448,-8.865623,8.895528,8.838053,-2.900819,-0.264847,1.170932,9.840245,-4.260684,-8.635942,4.497670,-8.231579,-8.814974,-1.908025,3.137424,2.310185,-1.477635,0.797933,6.932776,2.888804,5.349789,-1.775037,-1.085133,-9.130326,-2.878270,8.611380,-6.512580,-2.362519,-8.614468,-9.240124,-2.069709,-0.501239,9.791432,-6.626130,-9.331734,0.093114,-3.839336,-6.632436,5.222501,1.348039,9.787924,1.150256,-7.403014,-4.441009,-9.601302,9.009374,-7.439867,6.090076,2.410738,3.669105,-5.542355,9.096955,-1.461532,8.174920,-3.627913,-2.656444,6.503283,2.273516,5.891020,-8.345732,-8.484354,3.134617,8.334255,2.185481,-2.952358,-7.173754,8.733993,0.417771,8.908242,3.542950,8.198649,-9.838154,5.658131,3.154796,9.818032,-4.521475,5.374849,7.173205,4.554317,5.853156,5.485985,-1.519587,4.688066,-2.230116,-8.707775,-0.320745,9.491594,-9.420747,-2.255270,-7.386745,0.676021,-6.223859,-1.347658,-0.299822,-6.480529,6.270238,4.696358,-0.187576,-2.439917,-5.530720,-4.114644,-6.998047,7.036008,-6.150705,-0.128102,5.234459,1.510522,-1.412733,8.598499,2.408341,-7.420533,9.341504,-1.661276,-1.987678,0.341712,9.286410,5.036586,2.119805,-9.734379,4.790677,-7.129722,9.515973,-1.966542,6.994766,-5.070584,8.947566,-5.349859,-4.129104,-9.346951,9.371684,2.587170,4.120279,-1.934542,6.341747,-4.617540,-9.714873,-1.717975,-7.056372,3.351061,-0.218565,3.740232,0.233819,6.244383,-8.267317,-2.438777,2.055490,2.624447,3.939683,2.935563,-1.343766,5.691086,6.044406,-0.521730,-0.214839,6.976232,6.281247,-6.820824,-0.020776,6.542320,4.603682,-6.545437,0.307005,9.690363,-1.328826,-4.286986,-3.021986,6.923520,4.071596,7.381550,8.107150,-7.809041,2.965572,4.627845,-5.185889,5.622709,7.760856,-1.046933,2.856057,9.598087,6.583898,-3.653826,9.704596,0.687323,-6.520310,-7.145169,9.771363,-9.280924,4.796999,2.371775,-4.693505,8.736402,-1.608446,0.292729,1.757108,0.145890,-2.522899,-3.531556,9.248444,-1.842477,-9.521618,-0.355412,2.989415,4.833708,-4.524583,3.290504,4.066732,-0.531298,-4.451583,5.057776,-5.480201,-4.611759,-6.573713,-2.408010,-1.755212,9.233106,4.700320,5.662007,1.498184,2.940175,1.682741,-0.069992,8.501712,-0.480697,-9.200655,1.998673,8.834784,1.623257,-2.949396,4.785421,-6.414147,-0.733265,-0.936892,1.114656,-2.342784,-1.741109,4.925656,-8.464668,4.361087,-3.743971,-1.261533,2.495903,-4.207532,8.969578,-9.765826,2.101710,-4.744418,8.095564,5.357724,-0.148733,3.129103,0.252949,6.161021,-4.319511,7.724823,7.774933,-0.108193,7.496486,4.521204,-3.658274,3.203795,6.037423,7.686508,8.072161,5.364108,-7.830320,-3.068844,6.293782,4.045309,-0.455162,-5.929678,-2.785980,-4.930573,7.287186,-7.313127,-9.302525,-9.412244,3.991251,-1.516095,-9.522797,-3.592722,-8.817816,8.024194,0.848183,5.293140,1.460161,4.822560,3.167684,6.532032,5.747377,-0.702120,9.310269,2.216795,-2.650818,1.471121,1.107909,2.601977,-2.014683,1.417597,9.976814,-3.753618,5.338583,-0.016820,5.835472,3.076959,0.540348,-6.897290,-8.573088,-4.059891,8.133577,-3.240482,8.214570,9.529476,-2.841660,7.662835,0.682650,-2.451600,3.990418,8.657889,-0.034384,-7.483855,-0.572519,-0.365753,-7.097657,6.617776,7.143974,1.181234,2.550071,-7.952298,5.695067,4.111603,4.405718,7.836862,-5.959886,-5.331008,-0.173154,2.907062,5.973007,7.498206,-4.998890,-6.891851,-6.591825,-7.022606,-7.488008,9.407748,6.181769,-7.868008,-4.929352,2.627267,8.860625,3.485785,-2.209186,-1.727138,2.472443,-7.472888,6.671719,4.420767,-9.799459,8.506174,-1.877110,-8.156913,-6.837144,0.771778,3.277674,6.812333,-1.220205,-2.595798,8.023911,-6.819142,-7.514698,-1.217843,5.802044,-4.102958,-1.765421,-8.838678,-6.321695,-7.813729,-8.854433,-7.281595,-1.058385,-9.047216,-5.331058,-1.211710,7.882855,-8.333599,4.849345,3.931718,-8.054961,-0.928723,-8.034483,-3.391254,8.410973,0.555601,-1.054058,1.386331,1.317633,3.591271,-1.743810,-5.897768,-8.166081,-6.376004,9.402001,2.245868,9.912898,-2.336460,-6.179366,-4.533024,6.007573,6.026184,8.816666,3.323283,-2.931482,8.683732,-1.477420,9.696653,-4.674816,-7.771689,5.962291,-9.855094,0.466070,-7.108338,7.293704,6.375258,-5.333277,-9.506716,-8.719124,6.075376,-5.438800,3.983740,-5.395493,3.139718,-5.968855,-3.994030,9.489908,-1.910396,-1.210170,3.700409,-1.252216,-0.516175,8.302984,-4.400699,-4.255475,9.667137,-2.756584,4.216315,8.207990,-3.479784,-8.139454,3.956118,4.580301,-5.690958,6.224757,0.893899,7.343413,-3.725670,-7.617023,-2.856957,-8.182491,2.641529,-3.149767,5.283846,2.223091,-2.401429,5.105276,-7.869623,4.916365,-3.975398,-2.290515,-4.101215,9.136259,-8.736855,-3.750473,4.689240,-6.910815,8.243875,8.241860,-5.051637,-8.785375,2.913391,6.052565,-4.520737,-4.701791,8.552593,-5.553443,-5.687072,-3.697301,6.948804,8.124861,-5.001556,2.516264,8.416803,-6.106285,-4.631337,-2.535376,-9.061954,5.719405,-6.600223,5.300774,-6.384792,-9.729402,-8.713267,7.224565,6.372128,-4.659170,9.693555,2.632456,-5.128960,-8.137827,1.643085,-2.389699,-9.875491,-0.706997,-0.954813,-5.459396,-4.760125,3.504969,-1.435877,-1.801200,-7.765723,4.202363,1.458368,-7.139555,-7.342770,-5.014826,1.567243,-6.193535,-7.432501,-6.921897,-2.193368,6.870550,6.254701,5.687948,3.264148,7.997630,-0.697950,3.214345,-6.902049,-7.044506,2.525598,-0.479973,7.548590,-0.072234,1.835923,-2.557281,-4.296558,-7.889040,3.142595,2.296130,-0.487532,-8.889327,4.633289,-6.711111,4.886634,-8.693709,3.956223,8.893766,2.383108,-1.413455,-9.407945,0.420844,-6.527851,3.240182,9.839480,-5.422528,9.099815,4.441908,2.695100,-6.013774,-3.966458,5.124286,3.870729,-4.231502,-5.037528,-5.580316,-6.802186,4.817382,8.980985,-5.316932,5.789345,-8.117642,2.456184,6.687381,1.590167,1.684638,3.584625,5.350910,2.886893,7.352037,-6.273049,-9.079858,4.773993,3.994742,-0.961925,-2.191731,6.116265,1.074058,-1.950652,7.799634,-0.160764,0.035511,2.341372,7.189887,-7.896140,-1.181818,-2.542771,3.772294,8.342771,-6.615133,-9.931754,0.997421,-7.840888,-8.707068,-9.021492,-7.772157,-1.911988,-3.494205,1.238325,-0.711809,-9.844350,-4.061941,-9.635575,2.253244,2.861129,8.042556,-1.597465,2.529377,8.798134,0.761895,1.859991,7.035289,1.554691,5.335190,3.038851,-7.221380,-0.680132,-9.420067,5.857210,-1.985013,7.687196,-5.748747,8.195498,-5.483914,-7.312691,-3.182412,-3.184795,0.779033,9.000455,-4.844048,8.070944,-3.455360,4.597902,-8.373665,-5.711302,6.116648,-0.413826,7.412224,0.143434,8.064973,3.179066,9.355042,2.336590,6.814705,8.997764,8.879579,0.777475,8.248747,-3.242439,0.021535,-7.898735,-6.251872,-9.136441,-8.241325,-4.176356,0.209088,9.336481,0.594510,-4.752479,3.182831,-5.201495,-9.219952,9.343232,-3.982444,9.618920,-1.650303,1.742933,-4.651333,8.314669,8.244395,-3.721946,0.273806,-5.069040,-8.007507,-1.548086,-1.945442,-1.823229,-6.214046,-2.749709,3.884356,-7.751445,-5.580059,7.865771,4.235000,6.155075,-2.803474,-0.430026,-6.433438,-8.926896,7.609772,-8.977168,4.033330,-3.658553,-6.868450,-3.472882,-4.703805,-9.497447,-4.092710,6.730065,-9.561001,5.277861,7.641571,-8.243325,-7.025095,-2.888294,1.638176,5.912387,-3.813167,-5.532021,0.897133,-4.642492,5.224246,-9.956896,-6.714441,-1.003399,-1.300703,6.224728,0.251907,7.159881,-8.545414,3.018735,8.658143,-2.934253,-0.351602,-3.881055,-1.177257,5.247376,2.514249,8.166498,3.783267,-8.663087,5.144114,6.149459,-0.181836,-7.712832,8.660131,-3.709527,6.725676,-5.734819,-6.674704,1.484347,6.093948,-6.476892,-1.523079,3.115744,8.118627,8.515125,2.562547,0.789286,-5.589684,1.949707,0.411707,-4.495305,-2.059188,-1.065959,1.027720,3.573796,-1.812878,-5.043549,-2.302347,1.524909,8.942120,-3.763379,1.741171,-3.907155,-2.679332,9.855151,-0.593428,-9.497999,-6.560031,2.245704,-7.491232,8.917145,-0.894858,5.788896,6.642992,0.685049,6.477385,4.003558,9.442655,-9.561476,2.539787,-6.906243,9.988954,3.331219,2.339101,-9.823742,8.446730,4.620850,3.735134,-2.338020,5.752577,4.013115,-8.075267,1.643652,7.033487,7.416745,-6.658798,-2.944634,-1.093408,5.933791,-4.872867,0.030732,9.853391,2.379682,1.676949,7.516596,0.632471,3.518321,-7.254547,-1.181726,4.570691,-3.383826,2.175775,4.322641,-6.831555,8.604605,-7.895460,2.121550,8.252601,-4.790119,-4.342646,1.217490,7.879843,8.800730,-3.603432,5.198303,1.015087,9.334215,-3.739113,-1.501536,6.187692,4.218857,-5.807950,-1.091918,1.084399,-2.199597,-7.679957,-2.786731,7.108443,6.933374,6.336911,6.711118,0.188326,0.375226,1.862862,-7.013797,7.662827,3.104356,-2.272462,-4.838708,-1.315584,-6.032029,-0.299348,-7.100733,-8.959432,5.860963,-9.614392,8.829042,6.676047,5.262238,-9.741099,-1.019952,4.294480,-7.650241,5.059385,-4.095153,3.537504,-5.805065,4.697392,7.473583,4.549849,0.257662,7.086139,5.507712,8.575269,-1.466283,-0.961621,1.187954,-9.714597,-6.237213,-2.593191,6.463367,6.552939,-4.483473,6.940083,-1.092483,-0.335633,-4.766026,-4.570835,2.661902,6.314997,-1.877797,-7.557883,5.354969,4.680243,-0.378164,-9.192945,5.702596,9.036487,-7.902651,-0.104664,0.132335,-2.879546,-6.862118,1.924848,-5.767833,2.635192,5.393747,5.755614,-3.749262,-9.749711,-0.122865,4.873898,-9.770725,7.309810,2.445809,4.023612,9.211472,-5.540131,5.530523,2.187751,-3.930002,-4.586547,-4.660069,1.272905,-7.791682,0.229123,-9.756687,-2.916459,3.727284,-1.666282,9.247471,-7.223201,6.857484,3.784292,-0.819910,8.514319,9.626100,-7.000372,1.930190,3.694014,1.605704,-6.784120,5.818669,-9.405867,0.519873,4.711287,7.183826,7.133046,-6.303202,6.215543,4.981252], dtype = "float64")#candidate|11564|(1080,)|const|float64
var_11565 = relay.var("var_11565", dtype = "float32", shape = (5, 10))#candidate|11565|(5, 10)|var|float32
const_11566 = relay.const([False,True,True,True,False,False,False,False,False,False,False,True,False,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,False,False,True,False,False,True,False,False,True,False,False,True,False,False,True,False,True,True,True,True], dtype = "bool")#candidate|11566|(48,)|const|bool
call_11563 = relay.TupleGetItem(func_2733_call(relay.reshape(const_11564.astype('float64'), [10, 9, 12]), relay.reshape(const_11564.astype('float64'), [10, 9, 12]), relay.reshape(var_11565.astype('float32'), [50,]), relay.reshape(const_11566.astype('bool'), [48,]), ), 6)
call_11567 = relay.TupleGetItem(func_2739_call(relay.reshape(const_11564.astype('float64'), [10, 9, 12]), relay.reshape(const_11564.astype('float64'), [10, 9, 12]), relay.reshape(var_11565.astype('float32'), [50,]), relay.reshape(const_11566.astype('bool'), [48,]), ), 6)
func_6922_call = mod.get_global_var('func_6922')
func_6923_call = mutated_mod.get_global_var('func_6923')
call_11595 = relay.TupleGetItem(func_6922_call(), 0)
call_11596 = relay.TupleGetItem(func_6923_call(), 0)
output = relay.Tuple([call_11561,call_11563,const_11564,var_11565,const_11566,call_11595,])
output2 = relay.Tuple([call_11562,call_11567,const_11564,var_11565,const_11566,call_11596,])
func_11637 = relay.Function([var_11565,], output)
mod['func_11637'] = func_11637
mod = relay.transform.InferType()(mod)
var_11638 = relay.var("var_11638", dtype = "float32", shape = (5, 10))#candidate|11638|(5, 10)|var|float32
output = func_11637(var_11638)
func_11639 = relay.Function([var_11638], output)
mutated_mod['func_11639'] = func_11639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9387_call = mod.get_global_var('func_9387')
func_9389_call = mutated_mod.get_global_var('func_9389')
call_11641 = func_9387_call()
call_11642 = func_9387_call()
output = call_11641
output2 = call_11642
func_11649 = relay.Function([], output)
mod['func_11649'] = func_11649
mod = relay.transform.InferType()(mod)
mutated_mod['func_11649'] = func_11649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11649_call = mutated_mod.get_global_var('func_11649')
call_11650 = func_11649_call()
output = call_11650
func_11651 = relay.Function([], output)
mutated_mod['func_11651'] = func_11651
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11691 = relay.var("var_11691", dtype = "uint32", shape = (9, 11, 5))#candidate|11691|(9, 11, 5)|var|uint32
var_11692 = relay.var("var_11692", dtype = "uint32", shape = (9, 11, 5))#candidate|11692|(9, 11, 5)|var|uint32
bop_11693 = relay.left_shift(var_11691.astype('uint32'), relay.reshape(var_11692.astype('uint32'), relay.shape_of(var_11691))) # shape=(9, 11, 5)
func_7077_call = mod.get_global_var('func_7077')
func_7078_call = mutated_mod.get_global_var('func_7078')
call_11702 = func_7077_call()
call_11703 = func_7077_call()
output = relay.Tuple([bop_11693,call_11702,])
output2 = relay.Tuple([bop_11693,call_11703,])
func_11717 = relay.Function([var_11691,var_11692,], output)
mod['func_11717'] = func_11717
mod = relay.transform.InferType()(mod)
mutated_mod['func_11717'] = func_11717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11717_call = mutated_mod.get_global_var('func_11717')
var_11719 = relay.var("var_11719", dtype = "uint32", shape = (9, 11, 5))#candidate|11719|(9, 11, 5)|var|uint32
var_11720 = relay.var("var_11720", dtype = "uint32", shape = (9, 11, 5))#candidate|11720|(9, 11, 5)|var|uint32
call_11718 = func_11717_call(var_11719,var_11720,)
output = call_11718
func_11721 = relay.Function([var_11719,var_11720,], output)
mutated_mod['func_11721'] = func_11721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10838_call = mod.get_global_var('func_10838')
func_10839_call = mutated_mod.get_global_var('func_10839')
call_11729 = relay.TupleGetItem(func_10838_call(), 0)
call_11730 = relay.TupleGetItem(func_10839_call(), 0)
output = call_11729
output2 = call_11730
func_11738 = relay.Function([], output)
mod['func_11738'] = func_11738
mod = relay.transform.InferType()(mod)
output = func_11738()
func_11739 = relay.Function([], output)
mutated_mod['func_11739'] = func_11739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8413_call = mod.get_global_var('func_8413')
func_8415_call = mutated_mod.get_global_var('func_8415')
call_11762 = relay.TupleGetItem(func_8413_call(), 0)
call_11763 = relay.TupleGetItem(func_8415_call(), 0)
output = call_11762
output2 = call_11763
func_11777 = relay.Function([], output)
mod['func_11777'] = func_11777
mod = relay.transform.InferType()(mod)
mutated_mod['func_11777'] = func_11777
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11777_call = mutated_mod.get_global_var('func_11777')
call_11778 = func_11777_call()
output = call_11778
func_11779 = relay.Function([], output)
mutated_mod['func_11779'] = func_11779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8097_call = mod.get_global_var('func_8097')
func_8098_call = mutated_mod.get_global_var('func_8098')
call_11800 = relay.TupleGetItem(func_8097_call(), 1)
call_11801 = relay.TupleGetItem(func_8098_call(), 1)
output = relay.Tuple([call_11800,])
output2 = relay.Tuple([call_11801,])
func_11810 = relay.Function([], output)
mod['func_11810'] = func_11810
mod = relay.transform.InferType()(mod)
mutated_mod['func_11810'] = func_11810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11810_call = mutated_mod.get_global_var('func_11810')
call_11811 = func_11810_call()
output = call_11811
func_11812 = relay.Function([], output)
mutated_mod['func_11812'] = func_11812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7290_call = mod.get_global_var('func_7290')
func_7292_call = mutated_mod.get_global_var('func_7292')
call_11813 = func_7290_call()
call_11814 = func_7290_call()
output = relay.Tuple([call_11813,])
output2 = relay.Tuple([call_11814,])
func_11815 = relay.Function([], output)
mod['func_11815'] = func_11815
mod = relay.transform.InferType()(mod)
mutated_mod['func_11815'] = func_11815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11815_call = mutated_mod.get_global_var('func_11815')
call_11816 = func_11815_call()
output = call_11816
func_11817 = relay.Function([], output)
mutated_mod['func_11817'] = func_11817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9279_call = mod.get_global_var('func_9279')
func_9281_call = mutated_mod.get_global_var('func_9281')
call_11878 = relay.TupleGetItem(func_9279_call(), 0)
call_11879 = relay.TupleGetItem(func_9281_call(), 0)
func_7077_call = mod.get_global_var('func_7077')
func_7078_call = mutated_mod.get_global_var('func_7078')
call_11882 = func_7077_call()
call_11883 = func_7077_call()
func_4769_call = mod.get_global_var('func_4769')
func_4772_call = mutated_mod.get_global_var('func_4772')
const_11930 = relay.const(False, dtype = "bool")#candidate|11930|()|const|bool
call_11929 = relay.TupleGetItem(func_4769_call(relay.reshape(const_11930.astype('bool'), [])), 2)
call_11931 = relay.TupleGetItem(func_4772_call(relay.reshape(const_11930.astype('bool'), [])), 2)
output = relay.Tuple([call_11878,call_11882,call_11929,const_11930,])
output2 = relay.Tuple([call_11879,call_11883,call_11931,const_11930,])
func_11947 = relay.Function([], output)
mod['func_11947'] = func_11947
mod = relay.transform.InferType()(mod)
output = func_11947()
func_11948 = relay.Function([], output)
mutated_mod['func_11948'] = func_11948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11815_call = mod.get_global_var('func_11815')
func_11817_call = mutated_mod.get_global_var('func_11817')
call_11952 = relay.TupleGetItem(func_11815_call(), 0)
call_11953 = relay.TupleGetItem(func_11817_call(), 0)
func_8870_call = mod.get_global_var('func_8870')
func_8872_call = mutated_mod.get_global_var('func_8872')
call_11966 = func_8870_call()
call_11967 = func_8870_call()
output = relay.Tuple([call_11952,call_11966,])
output2 = relay.Tuple([call_11953,call_11967,])
func_11980 = relay.Function([], output)
mod['func_11980'] = func_11980
mod = relay.transform.InferType()(mod)
output = func_11980()
func_11981 = relay.Function([], output)
mutated_mod['func_11981'] = func_11981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7955_call = mod.get_global_var('func_7955')
func_7957_call = mutated_mod.get_global_var('func_7957')
call_11982 = relay.TupleGetItem(func_7955_call(), 1)
call_11983 = relay.TupleGetItem(func_7957_call(), 1)
output = relay.Tuple([call_11982,])
output2 = relay.Tuple([call_11983,])
func_11986 = relay.Function([], output)
mod['func_11986'] = func_11986
mod = relay.transform.InferType()(mod)
output = func_11986()
func_11987 = relay.Function([], output)
mutated_mod['func_11987'] = func_11987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7459_call = mod.get_global_var('func_7459')
func_7461_call = mutated_mod.get_global_var('func_7461')
call_11993 = func_7459_call()
call_11994 = func_7459_call()
func_2733_call = mod.get_global_var('func_2733')
func_2739_call = mutated_mod.get_global_var('func_2739')
const_12002 = relay.const([-2.451170,-8.250738,0.928028,-1.395302,5.631000,-4.227074,9.337552,-3.741096,6.448563,-4.701580,-9.919990,0.235824,1.857159,9.074405,5.803832,4.426637,-2.367289,0.358215,-2.004015,9.406655,8.074199,6.155852,4.808872,0.641539,9.764910,2.442805,-9.473931,-6.164926,-6.702499,8.750673,-2.338972,-4.206418,-0.682737,-5.981101,3.855713,-6.323031,0.860238,4.426160,-6.476208,-5.737230,-5.804389,4.160823,-7.737217,9.352430,9.398985,-8.350632,9.866320,-8.120407,6.517328,7.897248,-3.370240,1.017135,0.529483,-8.469914,3.511312,4.616468,1.600720,8.700036,2.136709,-4.444411,6.182232,-3.158288,9.146231,-1.723302,5.970169,0.717847,9.004035,-4.091233,-8.367085,-7.717483,0.646663,8.506009,-4.056897,-9.440542,9.828316,-5.162367,5.242687,-4.644166,5.435252,6.662438,-6.486855,0.604279,-7.768389,-4.693693,-6.467807,-5.177775,-9.206848,-1.728072,-3.782750,-3.605757,-9.466140,-6.325809,7.587055,-8.055497,6.032574,-4.151052,4.492798,-1.581708,8.254427,-5.216504,7.300851,0.191759,-5.202565,6.590964,-9.992858,9.757199,-8.062100,-8.038813,-0.560926,6.238809,1.523601,3.284797,8.972035,-2.990936,-7.430881,-8.436998,0.706895,3.586574,-7.005953,1.861595,1.367432,6.569499,-3.177170,9.013868,-8.175014,4.543470,-7.687245,-7.681480,-8.734331,-4.230436,0.207865,-9.753625,-8.996663,2.712871,-0.099929,5.297443,3.298166,-2.138238,5.708451,-1.127510,-9.040509,3.709446,-9.377996,-6.840311,-3.756295,9.222190,3.274791,-7.733586,7.176848,-0.345798,-5.827662,6.056119,-3.043977,-6.703630,-6.094175,-3.306347,-9.416981,5.273509,8.451099,6.449441,6.308311,-8.588005,-2.820721,-6.391629,-7.275478,-8.785818,5.403053,-0.756301,0.676072,2.138832,8.151776,-3.947650,0.871695,-8.250971,9.998731,-8.134443,-1.275792,7.816591,7.377852,-4.423427,8.530728,9.248842,3.968574,-4.083923,-1.580376,-0.668228,7.148719,4.530314,-8.150117,-6.086234,9.641562,-3.580573,7.589365,-4.882771,-1.199850,-8.329717,4.870034,-6.752424,8.355675,5.865882,-5.401875,0.496299,-5.175277,-5.609256,-3.306474,-5.834207,5.906934,1.997405,3.463234,3.915398,-3.604531,9.242518,9.548478,-8.334466,-1.073889,-8.798522,7.762323,8.462959,-5.628879,0.733532,-8.308080,-4.679375,-8.488848,-7.728306,-5.171326,5.738520,5.347097,-0.912049,-1.093756,3.734277,2.199763,2.455314,1.433509,-7.362151,-9.215787,-4.219402,-0.610073,-8.020928,-7.507107,-7.999196,1.149845,1.694336,-2.001551,0.794472,6.528201,5.304659,6.993503,9.550919,6.569891,-5.739652,7.814249,-8.573159,-5.206593,0.378224,4.516525,3.600083,6.843220,5.322447,-5.441105,1.801788,3.189853,-2.932986,7.514607,1.748245,-1.894857,0.995720,-6.903621,5.346265,-3.176352,9.323790,-8.516689,-2.737080,-5.917203,2.683966,5.937929,-4.865001,2.488087,8.873054,-1.048355,-8.955869,-5.541733,2.219861,9.839029,1.890731,4.738409,-3.726093,2.007720,5.300936,-0.349061,2.189699,9.305514,1.140879,-4.361739,-1.438027,1.295947,5.322294,-7.748613,4.847423,7.129620,5.941798,1.444754,-3.498658,5.571025,-1.252528,-3.582711,0.577613,0.237397,4.093124,7.389965,2.064762,-3.178567,-3.749045,7.972688,-6.496633,5.007492,0.131134,8.814189,6.714904,7.354947,3.360239,6.505229,-8.644969,4.846824,3.462409,7.000562,7.275353,4.899767,-4.840937,0.313477,-6.604237,-8.602154,-8.962450,0.863129,-0.228891,2.613323,8.184850,-5.333652,-0.417851,0.682315,-3.990908,-9.208995,-9.503768,-8.130390,-9.821276,2.005484,-6.149151,-4.280200,-6.739052,-9.456128,-4.442273,-9.781205,9.547730,3.376458,-9.085886,6.315857,1.535147,-5.995678,3.006113,-3.663681,3.875625,-0.400723,-8.763542,-7.730794,9.177677,8.492954,-9.572746,1.920975,8.965855,1.828255,7.776149,-1.592642,-9.598219,-0.129464,5.366299,0.680819,-1.932894,-6.274012,-2.803410,0.320216,-8.775762,-3.402528,-8.516375,-1.445978,-4.995146,9.740320,-1.264547,8.136250,9.599123,-3.611625,-1.622291,4.613199,-8.611398,9.679736,-5.734899,-4.878163,-4.495931,1.081324,-9.754150,-5.260523,-1.072216,-1.990880,7.077090,0.042342,6.876168,-5.464878,-9.185726,-9.796561,2.420741,4.877067,0.849743,-9.985427,-8.257183,-2.111654,6.566422,-7.524793,2.986958,-3.504175,-2.553184,0.374290,-1.416203,1.930422,9.439873,4.650603,-0.551397,-1.916245,-2.975144,3.341948,-7.397707,0.315008,-9.414584,9.438837,-6.033890,-8.669209,-2.278422,-4.613145,6.983538,8.660355,4.704471,-0.518014,1.965029,7.044050,2.808911,0.684200,4.994471,-3.503298,-8.166265,7.988522,7.085853,9.659544,0.783832,-3.936848,1.775425,1.025349,-6.754658,-1.665533,-2.832942,5.720500,-7.643029,4.711453,3.301166,1.624055,-5.942728,-0.918622,6.090223,7.299508,0.234136,6.850351,2.259897,-8.472106,-2.365395,0.195634,-1.463474,0.104846,6.291734,-0.531113,-7.471671,-5.765271,-4.389401,-6.534752,-1.830645,-6.480277,-7.672537,7.331974,-2.411701,9.826089,-7.029398,2.797672,-0.020867,-7.413449,-5.403996,-1.410038,-2.094715,5.389059,-8.226868,-2.449075,0.237562,-1.607695,5.007466,0.453069,7.184629,-6.118859,3.005139,6.391521,-2.835682,-7.832157,-9.346338,2.728349,9.090755,-5.059945,5.483488,3.729290,2.908869,-4.006163,5.089562,1.357695,-0.503094,-2.671573,6.401398,2.090379,3.399383,-8.869293,1.397282,6.094845,-9.818483,-2.953553,-0.733905,-3.034424,2.127923,-8.757679,-8.562127,-4.073333,-2.403835,6.319879,-3.668723,3.510139,-6.904940,4.631246,-0.607902,-3.292704,-8.916391,-0.836473,-1.579981,4.067268,2.057187,-9.308090,2.697151,-6.410384,-1.388568,5.417893,7.803175,-6.307763,7.123021,8.141749,-6.026230,-0.761945,-4.591424,-3.616887,-2.303685,-5.081302,2.857067,6.662403,6.853900,-6.446549,1.659480,-2.935102,9.829292,-5.781719,6.920928,-1.448786,-4.099149,-1.255084,9.260333,1.235216,-6.239931,9.800208,6.368943,-9.776619,-9.433382,-9.704936,0.427648,-7.723744,0.915328,2.139797,-7.219044,8.621431,-2.518695,4.867020,-1.340428,7.284320,2.870750,-9.082657,-2.608405,8.977391,-1.803772,-1.081820,6.772527,-2.336743,-8.865812,9.826992,8.101416,7.430652,-3.660893,3.376656,6.653263,-3.729521,7.789446,7.280697,1.555286,-2.609833,-1.758301,2.968104,-2.024055,4.736552,5.530446,0.211206,9.132181,4.799460,-0.592618,-5.110470,4.868262,-0.678994,2.692263,-2.466020,-1.243702,-2.572712,-7.130851,-7.280813,0.705904,3.937469,-8.970800,7.065109,0.467365,-2.092536,9.038099,5.476080,7.645493,0.755945,-0.097359,1.713982,8.779688,1.459681,-1.671989,-6.768311,3.919018,-6.379986,-2.770261,3.337897,-6.224897,7.873367,-4.849656,4.641283,-2.019803,3.144867,-7.018294,-3.328851,-0.237949,5.128486,4.319605,8.197214,3.108602,2.535489,0.720337,0.158806,-0.694312,-6.455014,-2.397429,-9.414104,-6.894768,5.228149,-1.484196,-0.164741,6.235022,7.319795,3.774728,-5.711829,4.609242,3.691441,-0.374776,-7.942677,2.065353,-9.890088,-1.970529,4.046370,-3.266912,-7.306363,-5.695696,9.808261,-0.903055,-8.228098,0.360223,5.512788,-8.971150,-7.382727,2.245073,0.763726,1.946370,-4.473190,-0.226745,-8.474271,-3.116094,-0.878168,-5.868610,0.940872,-4.215381,-9.755032,-1.921016,-0.258997,-4.755561,5.676708,-0.471411,7.221176,-6.149250,9.275070,3.239392,4.363971,-1.273699,-2.434387,-0.714129,-6.355421,5.351074,-1.897921,-4.114303,4.042912,4.861275,-6.078934,0.952148,7.619076,-9.459563,1.493839,9.689280,8.789576,-2.942061,-4.567633,2.731186,0.862370,8.813899,-7.088365,4.328396,2.385116,2.685729,-7.358708,3.010785,-9.071013,-9.699585,7.187470,0.965517,-8.836521,-3.150346,-9.111847,4.474717,-6.300841,3.727914,-6.574745,-6.558902,-5.655450,9.686247,7.730714,-4.347414,-2.996323,8.572001,-2.602974,1.407083,-9.527448,5.140362,2.662308,-3.723511,-1.864415,6.026111,-3.416842,-9.081781,9.272808,3.120311,-8.317491,-7.707440,7.969059,-0.243270,-0.832625,-6.592444,1.632604,1.171128,-5.546146,-6.514799,-0.698734,2.664133,-4.194806,4.956596,6.951195,-6.690536,-6.381649,7.963547,-9.936332,-8.106163,4.148962,3.618662,-8.729659,0.265215,-4.731398,0.819791,3.724850,-3.959662,-0.108290,7.386767,-4.293102,2.514294,4.135268,-3.579505,-8.314084,-9.447184,9.827690,-3.002899,9.350378,-5.398228,-8.180150,-2.784866,-3.049771,6.039920,-5.670325,9.181401,-2.144396,3.567205,4.149916,2.348743,-2.326508,5.127997,2.154475,-2.190435,5.318319,-6.835974,-3.595802,-3.941797,2.700801,-2.693736,-9.237911,4.555833,-0.451316,-6.871959,-2.988280,-1.259472,-6.034632,9.313197,1.399036,-4.312979,-5.335348,-9.886691,5.836446,-1.516861,-5.801932,-3.000908,-6.265018,8.409029,-5.194462,-6.708162,5.834922,-1.508453,-7.471291,0.264708,3.989417,-8.863904,7.785425,-4.905542,3.716045,6.089383,8.288416,8.342013,2.500728,0.831324,-2.580868,5.279953,-7.374094,5.147924,5.874682,-4.718537,-2.436240,-5.542219,-9.635257,-4.705064,4.822554,9.108569,6.922659,-6.529262,-7.885290,4.411628,1.226267,-0.374031,-8.098988,-4.721459,8.885694,-7.075930,-3.788133,4.150257,2.848079,-0.594709,3.709586,-4.148078,-7.161003,-7.839314,-0.615352,-3.906734,-6.761191,9.290805,-9.939945,-1.712347,-3.874158,-9.660448,8.613143,2.816567,6.681946,-1.692747,-6.773540,-0.957502,3.959607,3.899228,-5.893519,-1.955473,-4.577425,9.537463,5.138127,-0.622620,-7.774121,-8.910327,-0.950856,-4.179268,-0.879087,4.590158,3.662331,9.183147,-5.098654,-7.745455,-0.648018,3.647033,-0.941361,-8.246521,-3.291728,-7.337899,9.145350,-5.436221,-9.132821,5.027923,1.295462,1.294607,-1.690325,-3.805592,2.836242,2.685245,6.932149,6.136411,8.349227,3.335460,-6.595159,-3.362902,1.617512,-5.702454,-3.333489,-8.301139,-8.867841,-4.423274,-6.242357,4.771804,-5.982753,-9.232623,6.458042,5.684990,9.653484,-1.868165,-3.513999,5.718578,5.173512,-0.780316,5.303093,-0.756370,-7.791325,3.000072,9.976762,6.399094,8.267733,5.259265,1.591911,-8.107971,9.585682,-9.632734,1.257620,5.088570,8.990182,-6.108825,-2.886366,-8.727134,-1.031514,-1.142302,-5.337870,2.592286,0.572070,-6.108538,3.977982,0.892858,5.918462,2.535158,5.402938,-9.874175,-4.014693,8.889728,2.386236,8.586066,1.158926,2.648375,2.790153,-2.076980,2.719880,7.745766,3.863331,1.890631,4.698718,7.416858,-9.823557,5.603891,0.386536,7.307120,6.098273,-7.201205,-4.481451,-2.308414,-5.331607,-7.041938,-2.813249,-2.689763,-5.412275,-1.321818,-4.115040,-5.871686,0.345459,3.947527,6.978883,7.655717,-5.304810,5.948760,5.320211,-2.385226,-5.585186,5.141315,0.371823,-5.190320,-5.876170,4.279934,8.677347,3.154368,8.297722,8.002076,3.764989,3.231792,-1.963945,8.844501,2.855176,9.443797,-1.117996,-6.899888,-1.857175,-3.917044,5.569687,-6.721866,7.187629,-1.242136,-1.460227,7.805935,-0.630556,4.567171,-8.873678,4.172872,4.707424,3.866829,1.397666,5.473016,5.114824,-2.533033,8.401255,3.687247,-9.729061,0.273902,0.342997,5.391885,-9.425437,-5.912070], dtype = "float64")#candidate|12002|(1080,)|const|float64
var_12003 = relay.var("var_12003", dtype = "float32", shape = (5, 10))#candidate|12003|(5, 10)|var|float32
const_12004 = relay.const([False,False,True,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True,True,False,False,True,False,True,False,False,False,True,False,False,True,False,False,True,True,False,False,True,True,True,True,False,True,False,True,False,True,False], dtype = "bool")#candidate|12004|(48,)|const|bool
call_12001 = relay.TupleGetItem(func_2733_call(relay.reshape(const_12002.astype('float64'), [10, 9, 12]), relay.reshape(const_12002.astype('float64'), [10, 9, 12]), relay.reshape(var_12003.astype('float32'), [50,]), relay.reshape(const_12004.astype('bool'), [48,]), ), 1)
call_12005 = relay.TupleGetItem(func_2739_call(relay.reshape(const_12002.astype('float64'), [10, 9, 12]), relay.reshape(const_12002.astype('float64'), [10, 9, 12]), relay.reshape(var_12003.astype('float32'), [50,]), relay.reshape(const_12004.astype('bool'), [48,]), ), 1)
func_7521_call = mod.get_global_var('func_7521')
func_7525_call = mutated_mod.get_global_var('func_7525')
const_12008 = relay.const([-7.330494,6.264287,0.973223,-8.837518,-2.551274,4.584607,-7.919892,-5.023024,-4.786401,8.264893,7.628302,8.118591,6.661002,-0.770325,-2.560367,7.217274,6.765667,6.001248,7.348736,1.050239,-8.019699,-6.026065,5.699346,7.437660,-3.405884,-7.263861,1.190718,-1.649292,3.197710,5.913338,-5.526690,-6.870688,2.490394,-0.331403,1.391035,-5.481599,-0.842446,8.391680,2.760304,4.886650,1.155190,-5.150744,-1.335268,-1.030250,0.470545,8.103133,-7.435514,8.004385,8.015838,-9.219291,5.866471,-1.984610,-3.305321,5.772620,2.591986,0.065102,-7.090655,9.772038,-4.404754,-9.480435,0.393352,8.692958,1.272011,-6.081157,-9.450151,-4.196114,5.875078,-4.498963,-5.946909,-2.394345,-7.799803,-6.009262,4.139795,8.818812,5.043896,1.606129,4.242728,-4.023135,-4.514937,-1.953996,-8.718195,-5.960982,9.417436,2.403185,9.367601,5.601976,6.463884,-0.550434,9.877470,-4.960489,-9.943753,-4.512762,-9.297404,-4.514877,1.794117,5.443435,8.070586,8.696752,-4.635372,-3.632143,-2.673779,-8.409921,-2.820687,-4.668370,-5.079008,-3.189042,5.368572,1.203985,-3.825588,-1.259191,-7.496469,3.789402,0.153727,-9.258663,3.353641,9.779890,3.848425,6.926151,5.546080,5.919898,-1.095432,-6.208386,-8.975827,4.527447,2.181059,-9.197569,9.482437,-6.629496,9.298363,7.207653,2.963500,-8.759192,-1.149127,-6.500405,-6.533259,6.651150,-0.023500,-7.978230,8.738739,1.709427,3.484978,-8.994766,5.687420,8.893331,-9.807913,8.593154,-1.443710,-8.756885,4.013498,-9.388566,-0.897573,-1.719444,8.677832,-5.769345,-2.614151,8.443532,8.854972,-7.215735,-3.051939,4.527110,-3.645925,1.393875,5.301751,5.500744,-0.071882,-0.095183,-1.562201,4.398625,4.349896,-1.784777,8.589588,7.683890,-9.762536,2.840743,1.775565,6.769739,6.298245,-6.831619,-2.361281,7.264714,9.086131,4.795774,-8.421652,3.234078,-1.669560,9.161531,-6.341820,4.589099,2.725569,5.665657,4.810956,-5.567094,3.481571,2.286409,0.372203,0.048984,-0.790204,-7.776111,6.359260,-7.922128,3.535837,-1.180845,-8.185930,-1.163983,-3.133610,2.315911,-0.076644,5.922541,-0.003115,1.218785,0.904388,0.473860,-1.653304,2.817816,8.121013,0.614759,9.957167,-5.679589,6.503265,5.016265,5.926548,-0.242527,1.435184,6.812243,-0.149213,2.855862,6.654799,-2.252811,-3.126115,-1.468674,3.830903,-1.316277,9.604229,5.460272,-3.211544,-6.511798,4.351537,6.659625,-7.746949,-3.632479,-7.488469,4.030954,-0.397576,6.536967,2.530471,8.329908,8.782627,9.016044,-6.136881,-2.953492,-3.026954,-0.373892,8.712876,-6.853996,9.867453,-7.067005,-0.514942,5.614862,8.539831,1.965440,-9.085853,-2.313071,-5.013052,-3.694461,-1.583485,4.483945,-6.837171,-8.504933,-5.319603,2.704590,5.868266,9.218678,7.524206,6.446485,7.179266,4.548665,7.892140,3.611302,-6.859994,-3.774087,-3.080175,0.459836,-4.360774,-6.658986,-4.786752,-9.859094,-7.797968,3.174850,-2.957861,-4.033965,2.994638,-3.438296,8.602983,-3.522834,9.933823,-5.972242,3.989240,-6.951603,6.927627,-3.021176,0.117053,-4.315822,-2.358450,3.417581,-4.571461,-2.842039,-9.916841,-8.843471,-3.379206,8.231723,1.840858,-9.296673,2.969510,-7.087073,7.362856,-8.970766,5.033501,-6.135886,-3.699432,6.380075,-9.765130,-9.681601,-4.332920,-3.232863,7.550553,-2.108952,-6.179660,8.331190,-1.620130,-5.607869,-5.700908,-1.447119,9.734156,9.033141,-0.599856,-4.384539,-1.918868,4.396256,7.315977,-6.195428,7.412029,-4.054461,3.748293,6.597039,1.020986,5.388745,-1.200275,-0.661057,5.810734,1.650314,-3.776551,-4.800149,-2.002648,2.708427,7.310237,4.149262,-4.138086,-4.370782,6.353541,7.114170,-7.386099,0.820698,-1.203104,-1.890020,2.947292,-9.695946,-4.044236,2.694186,-6.325483,-7.882204,-1.241665,1.344709,9.188540,-6.784598,0.922885,-4.973028,-5.343837,7.528579,1.592359,-3.928985,7.426942,-4.717354,2.988072,8.459148,-4.221338,-2.750157,4.839550,4.409750,5.067733,9.980085,-7.103873,-9.030325,3.070459,8.310084,-6.068657,-8.832823,-8.685731,9.517026,-8.394767,-0.493738,-7.604120,3.588520,-5.022669,2.742577,-7.103650,-2.725657,-5.624580,3.878445,-3.667227,-9.487795,6.556255,1.287155,8.593980,3.486638,7.974764,-7.728566,-9.354632,1.403662,-2.383372,1.145055,5.459827,0.474005,-6.240756,-1.347583,-5.094773,3.277370,7.147366,7.798045,4.377131,-7.832368,-3.998935,8.365883,-6.695688,3.820746,6.497835,5.993072,2.463432,-3.282204,7.180260,-6.724514,5.772917,3.651672,-0.219023,0.434744,-9.056933,-9.419044,-6.180321,8.769454,-4.477871,3.279851,4.899831,0.843838,-4.768214,7.731264,-7.853183,6.351593,5.592664,-0.007072,1.600332,-9.469426,1.148030,4.461178,-8.501737,-2.091825,0.589534,-4.697294,-6.383243,8.374373,5.967030,-0.251678,2.951278,8.894432,1.178996,-2.573174,1.980596,-0.425769,-2.631864,-1.219223,-9.949137,8.679325,-3.468283,0.772510,5.877959,5.689993,5.312992,-8.817522,1.111116,4.693409,2.326247,-0.832819,-8.176840,6.928956,-1.420177,4.338850,-8.955949,-5.141036,-4.069256,8.161223,4.471959,-9.923401,3.982676,3.877878,-7.423199,6.763161,-5.502404,-0.548642,-3.428889,3.052085,4.410540,6.217494,-9.985480,6.348755,9.430403,-6.670419,1.289416,8.650940,-9.155252,-8.544743,-4.285648,-0.367552,1.212036,2.195955,5.326838,-6.458703,-2.202559,-5.669404,4.688437,3.366923,7.980676,8.444158,4.499329,4.029906,4.828978,-8.744498,6.632747,3.650285,-9.421127,-4.936795,4.065687,-4.846724,-7.746229,-6.437485,-4.108808,2.423372,-8.968300,4.539448,8.607483,6.762193,-9.990919,-0.484866,-6.642502,-5.407398,8.761117,-5.135989,3.869965,-7.778852,-9.247068,1.408135,-5.464129,-2.514387,-9.956811,-4.347068,-4.254346,-6.224638,-9.884336,-8.104671,-7.424711,8.084008,8.413095,5.485909,-1.596238,-5.729303,-5.574902,-8.626000,-0.238460,6.820101,-1.262179,1.991574,7.964784,8.563372,-3.110369,0.401572,-7.123774,-1.668448,-9.368975,-4.519394,2.066068,2.075007,-8.564192,4.277440,-1.253623,3.497836,-6.985987,8.503518,0.459575,6.353750,-6.353093,-2.424680,6.790150,-7.135209,-0.946233,0.782118,-1.239542,-7.573232,-1.155718,8.745064,-0.312398,1.696335,8.405267,9.242216,8.012809,9.510848,5.755435,-6.744420,-6.206604,-7.918808,5.116444,9.482855,9.613934,-4.373258,2.702452,-4.490315,6.396529,-3.840969,5.049738,0.546761,7.665925,-1.104191,-7.998190,4.819441,-5.809071,-0.851346,8.458458,1.428718,6.069811,-3.645381,6.721515,-3.433121,-4.165581,-7.372788,-3.673184,-2.288414,-8.630018,-6.942378,2.424722,1.547929,-2.875150,2.774183,8.976781,-1.060348,7.796942,2.210372,0.433209,9.877840,8.028244,9.243870,2.000262,7.629507,7.076672,-4.937821,7.460294,-0.689497,2.999720,-3.845792,-2.556186,9.524143,8.078786,-7.028246,5.491186,3.118140,0.675904,-6.348666,-4.709851,-4.374849,-5.491102,7.428154,0.794435,6.442243,2.628787,7.084740,-4.035164,1.377854,-8.527826,-2.509265,9.397863,-1.666385,7.608225,8.778883,-0.498818,8.777090,7.084932,-9.701036,-3.598592,4.765434,1.443490,0.275031,-0.948210,-5.766139,-8.160748,-1.713066,-5.645943,9.088596,9.730174,2.137051,-2.576176,-4.876985,0.601921,-3.577395,-2.990511,-3.917982,9.485905,5.851285,-4.923284,-9.103804,3.214851,1.536299,2.845111,1.144753,4.289731,-6.368970,4.496821,8.195894,9.654815,-3.896548,-8.555525,-2.801954,-9.911490,1.654381,1.418400,2.404621,-4.767662,-3.080620,0.232345,-2.013978,-5.435520,8.999448,-5.932369,6.150294,-7.210245,5.149234,-5.356463,-8.620638,-5.494833,4.655768,5.152353,-1.949872,9.429704,9.681399,-0.327599,-4.315944,-2.258729,-6.623886,-5.000990,5.020841,9.560869,5.570199,-2.307989,-9.988384,2.011625,-2.674729,-8.538705,-8.339437,7.365480,4.865202,-6.324820,-9.374582,1.683922,8.991322,-3.599187,-1.196678,2.326925,2.714082,-0.967119,-8.967365,-2.168784,-9.067307,2.666501,-2.827471,8.731298,-1.733503,4.501820,-0.910415,6.461351,7.822816,-3.869325,2.621970,9.230029,5.985229,-4.079737,-0.695728,-4.248236,-0.425441,8.689416,-7.603478,-0.334310,-0.118078,-2.098188,-4.499920,-4.759293,3.109892,8.082883,4.341081,-4.361638,-7.220958,-6.365535,6.404618,-2.461491,4.941468,-3.651416,-0.691886,-2.047278,0.363773,9.227773,4.745710,7.116730,5.645013,9.506500,4.633382,3.352982,7.112518,-6.099703,4.265838,-3.621671,6.722114,-2.797667,1.922141,-4.874942,2.323776,-0.182434,-0.055426,-9.045745,-0.389057,-8.246250,6.413560,-0.747181,6.889172,7.945358,7.968838,1.949240,-3.846518,-1.883092,5.357217,-8.330326,-0.586163,2.967175,-3.501219,-8.090835,1.056453,4.260307,3.206447,9.719705,-7.229387,7.850925,-1.167435,-1.344258,-3.472549,-4.944584,-4.645544,5.394807,4.714201,8.625817,-4.204507,6.386181,-6.592361,-9.267257,-5.490216,-5.037059,-9.168163,-0.152713,2.078614,3.550206,9.577488,5.364808,6.535930,-6.184492,1.699195,-7.981908,-9.823212,3.821586,-2.780145,-1.239766,-0.540247,-2.025999,-1.598417,6.565344,4.150399,6.592718,3.551002,-2.067362,6.110408,3.381719,-7.866179,-8.581815,2.030342,5.712531,9.040756,-3.840618,4.302435,-0.634964,3.220948,8.516483,1.666208,1.281741,3.542121,3.619869,3.253877,2.965051,-7.963677,-8.104085,7.945838,-3.258035,6.957899,-7.282157,5.108386,-5.957497,8.139903,8.606465,-7.430779,3.271455,2.198787,6.613925,6.085369,-4.325008,-3.108914,-9.975925,0.315234,8.278020,4.181233,6.242958,-8.429188,-1.958407,3.666962,-8.197370,-3.316628,3.171730,-6.922909,-5.631250,4.375160,-8.625480,5.637892,4.455484,3.135155,3.720041,6.086001,3.104867,-2.813156,2.697889,8.196592,-6.121222,4.787974,3.027382,-5.202182,0.713369,6.218396,5.043470,-7.905288,5.616922,5.576869,6.009024,8.942433,5.612471,-8.378011,3.414124,-5.290588,2.954486,6.087376,-2.535585,1.830965,5.613386,1.032621,9.813442,6.661945,8.256171,-9.898801,0.822300,8.087340,5.451004,0.973775,9.574021,-6.682373,6.137328,-9.455208,7.906111,-5.580478,-9.339014,-2.619020,2.105159,-3.642807,-1.222168,1.474459,-7.647155,-1.376884,-2.063721,-7.828790,-5.732881,1.306398,-3.592087,4.460417,0.732858,-6.774882,6.819036,4.951613,-9.262152,5.708496,-5.396362,4.200938,3.728783,9.584894,2.935599,7.631482,-7.870288,-9.292933,-1.927320,5.892117,8.927397,8.052735,-6.729198,0.361715,-4.017705,1.826426,-5.100385,3.844920,0.694162,4.585759,-5.033462,-2.554938,3.136570,4.955846,-0.954722,8.126236,-7.931374,-2.146667,-8.535673,-3.409810,-2.326496,4.741389,-5.229443,-2.709964,0.255370,-3.588308,-5.032291,2.160863,3.925422,-8.395057,6.428080,8.564173,-6.297910,-3.111049,-8.520032,-6.429738,-0.574028,5.934777,-5.784014,-7.965956,0.780851,-4.629355,1.851469,-3.849482,-4.634589,-8.448284,-0.116769,-4.342805,7.509734,4.209284,3.036574,-3.679805,-5.531192,-4.090634,5.940721,-7.518483,7.192195,0.836863,-9.345155,-8.667144,-9.424163,-3.974233,-1.327410,3.997462,7.562633,1.038198,-3.998626,0.799031,8.675452,-0.911934,-0.551933,-5.107286,4.714851,8.404752,9.753033,-3.366895,-2.698330,-4.438143,2.065404,5.677230,3.650165,4.636814,-8.384228,-6.854707,-0.948045,4.640620,2.276378,7.680125,0.198756,1.071158,-7.165948,-9.385254,-4.717596,7.404628,-2.691266,8.066738,-3.084781,-3.393876,6.371714,-0.029807,4.102841,-9.501058,8.837385,1.896744,-3.146297,3.830129,-5.762725,-4.633202,8.447540,1.055391,-4.008092,8.162622,5.193053,0.525409,-9.543006,4.793845,8.408097,-0.637203,9.317461,4.314820,-4.698549,-3.732522,-4.538001,-7.462105,-9.953809,-0.954498,-0.305031,2.502511,2.895656,-8.757346,6.001710,5.345779,4.529582,1.518829,5.072834,9.809723,-5.065769,-8.281372,-7.000889,-3.869022,-4.443264,8.711554,-7.517358,2.913321,9.017549,7.096597,2.386558,-7.205067,-2.211385,0.473548,-1.721643,-6.247192,-6.773498,-2.432149,3.304248,6.886220,4.751222,-6.991595,-9.448460,0.642848,1.445147,-7.721594,8.870314,9.893299,-4.645543,8.461812,3.607853,8.199871,-9.101142,-5.032163,-9.977909,-4.681442,-6.702019,7.193010,-1.857009,0.603500,7.103694,-6.163192,-3.870737,0.943418,-1.697765,1.136038,-0.004165,9.021079,-2.689242,-1.436189,4.641230,-4.115813,6.633287,-8.181516,-6.976517,3.329289,5.069609,-7.835561,3.555428,5.848345,-3.823429,-9.803300,3.846534,-0.644716,7.070439,7.027259,5.724057,3.370373,0.659219,-7.684652,2.191379,-9.346180,8.998804,-7.529275,-4.745379,-7.382734,-5.625401,7.645456,-6.087543,-8.980151,-1.154936,-5.238478,3.604742,-2.452212,-2.713606,5.663651,-1.596849,-0.600000,-1.449840,-8.974714,-7.531611,-7.834147,3.365310,1.473581,1.169795,-9.541485,2.254713,6.616251,-5.589969,9.707981,-1.398605,-0.406993,-7.289929,-6.731289,4.433433,7.410729,5.223698,-3.896354,6.140752,-0.896151,7.983599,-8.948010,4.662523,-0.217615,4.103715,-4.512052,-4.944649,-5.659625,-0.665185,9.481280,-2.384584,1.938693,-1.446657,-5.204540,3.861271,-4.094923,1.679732,1.744636,-0.224068,-7.512075,-8.912571,8.941546,7.281449,3.519170,-7.909363,9.720426,-2.385087,-0.517485,3.460273,-7.438965,0.396884,0.593716,-0.415523,-0.313418,-8.266125,-5.893758,2.500894,2.655101,-6.931154,-0.723306,-2.878190,4.125276,5.626050,4.341439,-4.901840,0.492024,2.361380,4.371649,-0.226327,-7.513888,-4.370122,6.320738,9.796019,4.262813,0.268719,-0.019265,5.573122,-1.265990,-7.326124,0.931256,-5.947849,-5.970535,-9.737744,5.037346,9.776154,2.578379,-0.361570,-7.193155,-7.462106,0.663908,5.906940,6.575898,6.651780,7.988573,9.706923,6.620574,-6.030566,1.652260,5.044138,6.922329,7.756490,-6.940711,0.469404,5.367451,-8.711236,0.570298,-1.751306,4.115354,3.684217,9.784976], dtype = "float64")#candidate|12008|(1350,)|const|float64
call_12007 = relay.TupleGetItem(func_7521_call(relay.reshape(call_11993.astype('float32'), [3, 11, 2]), relay.reshape(const_12008.astype('float64'), [1350,]), ), 0)
call_12009 = relay.TupleGetItem(func_7525_call(relay.reshape(call_11993.astype('float32'), [3, 11, 2]), relay.reshape(const_12008.astype('float64'), [1350,]), ), 0)
output = relay.Tuple([call_11993,call_12001,const_12002,var_12003,const_12004,call_12007,const_12008,])
output2 = relay.Tuple([call_11994,call_12005,const_12002,var_12003,const_12004,call_12009,const_12008,])
func_12039 = relay.Function([var_12003,], output)
mod['func_12039'] = func_12039
mod = relay.transform.InferType()(mod)
mutated_mod['func_12039'] = func_12039
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12040 = relay.var("var_12040", dtype = "float32", shape = (5, 10))#candidate|12040|(5, 10)|var|float32
func_12039_call = mutated_mod.get_global_var('func_12039')
call_12041 = func_12039_call(var_12040)
output = call_12041
func_12042 = relay.Function([var_12040], output)
mutated_mod['func_12042'] = func_12042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8982_call = mod.get_global_var('func_8982')
func_8984_call = mutated_mod.get_global_var('func_8984')
call_12048 = relay.TupleGetItem(func_8982_call(), 0)
call_12049 = relay.TupleGetItem(func_8984_call(), 0)
func_9236_call = mod.get_global_var('func_9236')
func_9238_call = mutated_mod.get_global_var('func_9238')
call_12063 = relay.TupleGetItem(func_9236_call(), 0)
call_12064 = relay.TupleGetItem(func_9238_call(), 0)
output = relay.Tuple([call_12048,call_12063,])
output2 = relay.Tuple([call_12049,call_12064,])
func_12077 = relay.Function([], output)
mod['func_12077'] = func_12077
mod = relay.transform.InferType()(mod)
output = func_12077()
func_12078 = relay.Function([], output)
mutated_mod['func_12078'] = func_12078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11503_call = mod.get_global_var('func_11503')
func_11504_call = mutated_mod.get_global_var('func_11504')
call_12128 = func_11503_call()
call_12129 = func_11503_call()
func_10041_call = mod.get_global_var('func_10041')
func_10042_call = mutated_mod.get_global_var('func_10042')
call_12161 = relay.TupleGetItem(func_10041_call(), 0)
call_12162 = relay.TupleGetItem(func_10042_call(), 0)
func_8966_call = mod.get_global_var('func_8966')
func_8974_call = mutated_mod.get_global_var('func_8974')
var_12167 = relay.var("var_12167", dtype = "bool", shape = (315,))#candidate|12167|(315,)|var|bool
var_12168 = relay.var("var_12168", dtype = "float32", shape = (780,))#candidate|12168|(780,)|var|float32
var_12169 = relay.var("var_12169", dtype = "float64", shape = (18, 1))#candidate|12169|(18, 1)|var|float64
const_12170 = relay.const([5.439093,4.445061,-0.177185,2.214057,-1.143392,-8.263307,-7.041148,-7.826373,-1.934756,-5.313556,-4.303472,6.185862,-8.097255,-3.157505,-0.002954,6.593661,6.551217,5.340608,-3.839479,2.031233,1.352313,0.057271,3.852190,-8.643541,-4.863405,-5.129744,-3.892206,2.378298,2.860758,-7.668020,-4.490364,1.726875,0.640829,1.822244,1.159621,-5.230954,2.975092,-8.107443,6.014019,-4.826174,8.520720,8.869048,-2.927870,-0.936804,-5.225674,8.956744,-8.730228,-6.134114,-9.699514,3.683033,-1.777101,-7.097373,-2.023608,0.520434,-0.756913,5.386187,-8.684013,1.076607,0.803342,-0.450482,-1.155259,-3.165509,-8.959353,-0.636216,0.324443,1.298486,-1.346022,7.001822,-1.754940,-5.946642,-7.788469,7.303803,-2.599469,1.360888,-0.583185,9.812293,4.745255,-9.511401,3.160747,-4.910689,-9.592216,-1.529635,-9.828826,9.183991,-1.844558,7.755854,5.904167,-5.558418,2.035550,-1.241042,9.109934,-4.874620,6.620064,4.378960,-3.892585,7.592274,0.262340,7.234825,1.088727,-0.694033,-0.394142,-5.719410,-3.254359,-6.181772,-8.872549,-2.530381,-7.261251,1.039630,2.605841,-0.728753,-7.679392,-5.904918,-4.839482,2.257838,7.821191,7.433182,4.930584,9.543013,-9.781047,9.848289,-9.926447,6.908187,2.413512,0.053950,7.603947,-3.214914,4.152431,6.405618,-1.688928,-3.870683,-6.165484,1.711272,2.883596,-3.220513,-2.438267,9.950840,4.087202,-1.988120,4.716593,4.452543,9.536866,-6.953330,-5.299055,-1.014079,4.085978,-4.869432,0.156125,4.032767,9.239962,-6.355240,-1.393368,-2.904792,-1.293636,-2.081902,-0.981545,-5.109637,1.919993,1.271452,-2.564675,-6.743756,-5.170341,-5.169898,-7.597476,-4.538536,4.250086,-0.462614,-4.372688,5.676481,3.959616,-8.898923,1.668793,2.038320,-6.506551,-0.819631,1.464250,-6.056746,-1.394125,4.100095,-8.597381,-1.317561,-7.685623,2.805957,6.404359,-7.831961,-8.771668,2.735763,8.940624,-0.756574,3.993460,8.266276,1.308027,-9.309403,-9.547491,3.934252,1.186736,-1.584199,-8.614256,6.664097,-7.516197,-9.449116,-3.634637,-4.963022,-3.254222,6.765299,5.517091,-8.965604,-8.943705,-1.271327,-3.971598,-0.719939,4.914443,-6.120089,-1.580928,-7.531359,4.263322,-4.871074,-5.122988,6.318751,6.269192,-0.547174,5.523790,-7.431999,7.207186,-2.284180,-9.372386,0.182654,6.318820,5.236855,2.976945,-5.014849,-5.449121,6.292549,4.028826,6.818219,3.757611,-7.204735,8.196725,8.435645,9.149354,-1.778858,-7.598405,-6.221447,6.888411,4.065497,4.842705,1.135404,-5.664776,-2.938005,-8.926558,4.909244,8.651718,-9.509922,-5.438319,4.325736,-2.313664,5.883991,6.147063,-4.246234,2.711326,-6.914279,-4.914670,-4.921086,-9.685653,-3.027632,-1.389870,-5.129719,9.435835,-6.601018,-0.185437,-5.012224,-1.014813,2.958740,5.677360,-0.579102,-8.512791,6.469284,2.252283,5.850755,-8.644160,-3.073235,4.031043,-9.682678,7.514719,-3.094342,-1.419436,-1.239584,-6.733690,-5.665169,-6.717459,-0.221074,2.156293,6.382724,2.344149,-4.508770,-3.826077,4.242913,-9.890845,3.701783,-6.357250,1.704804,-7.912431,3.604386,-8.250868,-4.705225,2.338460,4.872778,-8.947253,5.020704,1.571084,1.498637,-8.111119,-0.587515,-1.471621,-9.836837,9.030126,1.352388,-3.958708,0.200456,-8.182972,6.457248,-3.204803,7.671686,4.989065,0.468981,-5.640018,-3.297506,4.759275,5.324715,-0.405646,-1.214345,-2.629607,3.019816,7.780690,3.912332,-9.164464,6.177463,1.536104,6.139610,9.128829,9.820627,6.392079,-0.218204,-5.761616,-2.882717,7.841116,6.211253,-2.514465,-8.063574,7.696960,-5.296167,-2.072136,-1.633388,-8.820191,-4.018234,-3.302092,9.854592,-5.454959,-1.555251,-0.531869,0.116248,-2.768490,2.899772,-7.193116,-7.968415,3.673342,4.826403,-8.064562,9.085243,-8.376605,-7.335547,6.094526,-4.614702,5.297281,4.298919,-9.252469,6.477627,1.145645,0.220535,3.877255,3.799112,-1.047655,-1.739813,-5.949002,8.166622,-1.428548,-4.828231,-2.715971,1.326913,9.058277,7.312043,6.739184,-7.860320,7.436161,-2.699262,1.477645,5.529687,3.061417,-5.271195,8.089909,-2.292782,9.048231,5.769348,6.681939,2.017946,3.823773,-2.834130,-2.178536,5.548802,6.709350,-2.252230,1.567293,-6.847063,5.182770,5.768238,2.225989,-7.779343,-6.026681,-4.657545,-8.209130,-2.250902,-5.555098,8.602110,-9.562013,-6.195612,-5.011489,-9.545000,-0.791760,-6.186270,-7.240013,-3.741262,6.112740,-2.813934,-9.241479,-0.690339,6.728669,4.385917,9.599898,-5.634235,5.026963,9.157324,6.683048,-0.243609,6.919913,1.871029,-0.153011,9.242978,5.472406,6.935874,-3.046620,-5.728351,-9.787803,2.421063,-7.348838,2.973565,-1.157687,-5.514184,8.836085,8.146333,4.758738,-2.042543,-8.399582,-5.681045,8.175078,5.393842,3.067184,8.997176,6.568288,2.231536,-1.575656,-1.166473,-4.710384,-9.071298,1.393275,-7.686463,3.964847,-7.405002,-6.508085,8.020043,-3.821640,8.104258,-5.746763,1.771264,8.880637,-0.327841,-6.187688,-2.191138,7.758404,-6.364059,-0.130735,3.281170,1.490897,9.859398,-0.174504,1.965732,1.498845,-5.427553,-9.126406,-8.124851,4.192513,9.119392,1.959345,-8.320641,6.748890,7.487858,2.546316,1.617279,-6.860744,-5.117494,8.711085,9.190274,-4.546897,-7.401043,9.463135,-0.079576,8.420512,-1.137291,3.073349,6.235094,4.485759,-1.775919,-1.678621,4.482797,-1.461235,1.069899,-8.221586,-8.327637,4.893023,7.419767,8.606582,3.733784,6.782780,5.235872,-0.055830,2.936107,4.768125,-3.574356,7.577710,-0.117599,7.588344,7.382153,-2.489191,-5.848079,7.494005,2.333032,9.707087,9.910825,-6.180539,9.822589,-5.311723,9.572440,-9.899926,5.093906,1.197839,7.976471,0.617083,-0.082460,-4.139663,6.236143,-5.971969,3.792008,8.382177,4.653181,2.025513,-2.197673,8.635969,-4.735203,3.377882,-7.891636,3.927387,8.219127,-6.167074,1.539503,-8.326520,-0.087137,9.376332,-8.243432,6.541458,-9.305435,-1.651591,-8.712993,-2.945540,3.156841,-7.181498,5.233288,2.956048,-4.001928,-0.414343,3.714732,4.833597,-4.245282,7.441077,4.238029,-5.397725,4.869836,6.761402,-1.135344,-2.813383,3.592429,4.046324,0.241989,-2.448601,2.232580,0.424894,9.072890,-4.236803,4.472242,7.057206,-1.615472,-8.671990,-6.464459,8.927355,-1.258343,0.177178,-0.766364,-7.299203,5.969818,-7.668415,0.457902,3.133030,-5.884549,-7.204067,6.866095,-4.043170,7.648467,-4.219304,-3.757028,2.142025,5.044138,0.681840,6.163851,0.838663,-7.127821,9.034948,4.747808,-0.528188,0.855921,3.691968,-5.466820,-7.616024,0.357575,-1.908736,7.304920,-7.184307,-9.158089,-2.305331,0.082254,-6.245749,2.447659,0.716375,9.666529,-0.747776,1.081389,2.836513,-9.232411,5.245698,-5.768851,5.836870,9.897878,9.156588,2.807330,-1.745865,6.921761,-3.570389,-1.429471,-1.099642,-0.191558,-7.418712,-3.506563,8.997179,-9.985434,-9.373303,-8.597372,-1.042910,0.629256,5.253451,0.940200,2.733949,0.643110,-5.098185,-1.522609,0.418574,9.228527,-5.982398,2.506575,-3.302121,-5.235103,0.625984,1.995988,0.533536,6.600773,2.813094,-1.390705,5.520052,8.431930,3.972169,-6.488275,-7.374514,4.153696,-7.474665,-0.816733,-2.430833,3.161787,-4.386999,7.944779,-3.918041,-4.246944,4.552268,-7.260230,-6.958435,-7.466267,0.259633,-4.302903,9.393548,-1.200967,2.295225,-6.599256,-5.922212,4.780780,-5.784367,-7.268984,7.364615,0.410169,2.822963,7.416011,3.033314,8.424807,9.412989,-7.474590,1.985089,-6.397183,1.198349,-8.293134,-6.880980,-5.159995,-5.367189,6.051446,-1.889992,0.880145,5.544809,3.046907,-6.667434,3.152043,9.617300,-6.067718,8.540414,1.330395,-3.210940,-7.006423,8.216445,3.094576,4.605406,5.500888,0.565678,4.650286,4.571644,2.131864,7.827742,0.583208,-5.476717,-4.031261,-2.924937,4.598078,2.205719,-8.043448,-5.183292,2.951589,-0.794789,9.861976,3.270676,-1.829951,-1.918687,-1.716553,7.579888,-6.991003,-5.126027,3.329837,-6.724605,3.496741,-8.925914,-8.461629,5.635243,-2.382277,-6.805766,-6.523151,-0.010075,-8.478163,-1.857191,-9.919849,1.926994,-4.636855,7.787822,-4.053575,-0.171244,-8.368581,7.516660,0.133781,-3.843716,3.578280,-5.325328,-7.120513,-7.324643,1.074971,6.029876,-0.334871,-6.833355,-1.588119,-4.179025,2.686691,-0.189342,9.685590,-1.842746,5.584484,-1.010386,9.074243,-0.404069,0.070257,-1.511431,1.404044,1.194402,-0.191945,-6.826989,8.643659,-7.331447,4.037660,-1.044312,-3.509575,-3.738172,2.767487,-1.563998,3.620050,-4.208055,-7.556889,3.476829,1.731100,9.996632,-6.244362,-7.053758,8.576048,-2.219587,-0.821636,9.933202,4.786766,-1.787024,0.962807,6.959840,8.465235,7.958304,-8.475265,0.065883,6.513369,-1.615158,7.102768,-9.239484,4.706401,6.719854,5.181332,-5.014952,-1.680104,-2.503022,-4.648214,-5.530803,3.547778,8.550464,-1.389063,3.710278,9.263634,7.141848,1.433729,2.167585,-8.613658,-2.350063,-4.226369,-7.078788,4.007620,-5.053535,-7.272333,1.599612,-3.432651,-5.259210,4.681437,1.484043,5.477809,0.107531,-6.200108,1.654975,-3.948651,-9.866468,-0.387591,9.498615,3.633331,3.485315,6.614119,-8.793196,1.855149,-6.362542,-5.503111,-4.365550,4.604895,-4.337000,-6.780056,-5.424815,3.047494,1.961735,-7.071427,1.052577,-0.287516,8.221884,2.725187,-0.990305,-6.134712,-5.688768,-3.628295,-1.561389,-8.082307,6.446604,-4.684291,4.217102,-8.769904,-3.212402,-6.935685,8.516551,-2.311302,-4.561156,-0.250360,9.782548,3.759832,8.743757,-3.549558,8.454642,1.927591,7.303337,1.660951,6.705523,-2.823579,-9.624075,-7.473950,7.675783,-4.935592,-5.641133,-0.134382,-1.862051,2.591413,5.907208,1.537931,3.866723,0.727319,2.133801,1.013819,4.835407,-1.899182,-5.352906,5.734806,0.465274,1.166737,-2.886421,4.537171,-0.751091,-2.192755,-8.549110,-0.131114,-2.152945,3.294775,-3.234865,6.304560,-2.691613,7.221019,-8.335690,-3.921585,2.515889,6.948905,-4.159527,-4.832080,-2.093298,-4.063770,-2.747475,-0.399113,8.550707,-2.812390,-9.871997,9.370627,2.560176,-8.439721,0.241603,-8.538978,-3.388243,-4.258000,-6.595024,7.893337,7.153462,-8.489647,2.503515,8.816085,-4.231636,-4.396113,3.230891,1.292140,4.082532,-8.757857,-3.686896,2.872254,-8.638037,1.472312,-7.687728,3.419429,8.593628,7.585115,-6.337013,6.435369,6.936795,-2.527162,0.169402,4.788099,3.929686,3.379590,-5.542776,-9.841918,-6.822733,-2.768420,3.321190,-8.619024,1.334733,9.133115,-6.679746,-9.414982,-5.448485,-8.585744,-4.188390,-8.308845,6.535616,2.915529,-1.007951,0.085288,-7.833491,1.195958,1.371645,-7.512239,-4.601741,1.787791,-9.071927,-9.311121,-7.353749,-9.976980,-0.118604,-8.202768,-1.730816,-6.119816,6.407676,1.975049,7.609954,3.602536,-2.393556,5.241130,6.869859,-4.125387,-8.287629,6.157726,4.500077,7.117050,-2.437145,-4.254395,0.204455,-8.140647,-3.257815,-3.374098,-0.867776,-4.329218,3.545043,5.566233,-8.061108,-9.412416,-1.719675,9.752932,2.522559,-9.290340,-3.305786,-8.086810,8.286387,5.775780,-7.472411,7.540350,4.964488,-9.588341,1.340787,-4.911384,0.196087,-2.217980,-0.583489,0.118721,-8.088531,9.983822,-5.313493,-8.795486,-9.031428,2.202501,-3.777108,-8.020458,1.982813,-2.051256,-6.747565,-3.734510,-9.253656,-6.459743,1.874002,-9.759761,6.416949,-5.878872,-4.377325,2.701390,-0.895608,7.414200,4.534110,9.882313,-5.671504,8.837283,-3.985720,-4.074790,-6.617038,5.807266,0.737220,0.578266,6.877640,-3.524573,-2.381879,0.215244,1.492608,8.451996,-9.372481,5.868647,3.258802,3.620049,-4.250247,-4.888386,-6.487198,-2.509872,4.127479,-2.952914,-3.695538,-4.550443,-2.959691,5.115363,3.755109,-1.232866,8.679703,-6.619206,-2.900287,-1.375460,-3.425898,4.519748,-5.757492,-7.774647,8.214664,5.984825,6.562201,6.220172,9.397503,2.319607,1.970042,-2.423710,9.156018,5.571479,-0.173108,6.147392,-3.924670,-7.260168,-9.436202,3.060580,0.155921,0.325966,-7.458430,6.135739,-4.655286,-6.763459,-3.656672,-1.128445,-5.206389,-6.635018,-1.287725,2.305319,-4.684990,4.502474,-2.380102,4.321832,5.884289,-2.887046,2.314828,5.423091,7.392839,9.902873,-4.998981,6.366063,-4.372668,-6.405413,3.989766,2.167655,0.061181,4.146254,1.239148,6.733299,1.470975,7.349683,3.269519,-8.733660,-4.728626,2.023391,-8.618163,9.957478,-6.694275,7.590693,0.434969,9.458912,3.133629,-2.557088,2.461568,-8.461988,-0.668111,1.095127,-3.127363,-3.390767,-6.189243,-2.753996,-0.267540,3.761925,4.598711,9.370519,3.292984,6.228118,6.691986,-4.436782,4.595482,0.131461,-6.506629,-4.371520,4.782153,4.420736,-7.189111,-8.008651,-3.608067,4.660019,-5.426073,-5.516780,8.686966,-9.498007,-4.534365,-3.896350,7.772415,5.224299,-1.309947,7.698612,-5.540005,5.213532,-1.360106,1.717446,5.021368,-0.295561,8.438464,-1.394207,-3.551728,1.480529,2.421412,-8.315049,-2.930081,-9.188810,2.454709,-3.693700,-1.723298,-3.059058,5.246077,6.527720,-0.795316,-4.947029,6.400001,9.121278,4.435988,-3.097389,-0.240092,-2.507900,-4.438996,7.083339,-6.987801,0.345335], dtype = "float64")#candidate|12170|(1280,)|const|float64
var_12171 = relay.var("var_12171", dtype = "bool", shape = (360,))#candidate|12171|(360,)|var|bool
call_12166 = relay.TupleGetItem(func_8966_call(relay.reshape(var_12167.astype('bool'), [315,]), relay.reshape(var_12168.astype('float32'), [10, 78]), relay.reshape(var_12169.astype('float64'), [18,]), relay.reshape(call_12161.astype('float64'), []), relay.reshape(const_12170.astype('float64'), [1280,]), relay.reshape(var_12171.astype('bool'), [360, 1]), ), 2)
call_12172 = relay.TupleGetItem(func_8974_call(relay.reshape(var_12167.astype('bool'), [315,]), relay.reshape(var_12168.astype('float32'), [10, 78]), relay.reshape(var_12169.astype('float64'), [18,]), relay.reshape(call_12161.astype('float64'), []), relay.reshape(const_12170.astype('float64'), [1280,]), relay.reshape(var_12171.astype('bool'), [360, 1]), ), 2)
output = relay.Tuple([call_12128,call_12161,call_12166,var_12167,var_12168,var_12169,const_12170,var_12171,])
output2 = relay.Tuple([call_12129,call_12162,call_12172,var_12167,var_12168,var_12169,const_12170,var_12171,])
func_12174 = relay.Function([var_12167,var_12168,var_12169,var_12171,], output)
mod['func_12174'] = func_12174
mod = relay.transform.InferType()(mod)
mutated_mod['func_12174'] = func_12174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12174_call = mutated_mod.get_global_var('func_12174')
var_12176 = relay.var("var_12176", dtype = "bool", shape = (315,))#candidate|12176|(315,)|var|bool
var_12177 = relay.var("var_12177", dtype = "float32", shape = (780,))#candidate|12177|(780,)|var|float32
var_12178 = relay.var("var_12178", dtype = "float64", shape = (18, 1))#candidate|12178|(18, 1)|var|float64
var_12179 = relay.var("var_12179", dtype = "bool", shape = (360,))#candidate|12179|(360,)|var|bool
call_12175 = func_12174_call(var_12176,var_12177,var_12178,var_12179,)
output = call_12175
func_12180 = relay.Function([var_12176,var_12177,var_12178,var_12179,], output)
mutated_mod['func_12180'] = func_12180
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12222 = relay.var("var_12222", dtype = "float64", shape = (2, 11, 4))#candidate|12222|(2, 11, 4)|var|float64
uop_12223 = relay.sin(var_12222.astype('float64')) # shape=(2, 11, 4)
output = uop_12223
output2 = uop_12223
func_12230 = relay.Function([var_12222,], output)
mod['func_12230'] = func_12230
mod = relay.transform.InferType()(mod)
var_12231 = relay.var("var_12231", dtype = "float64", shape = (2, 11, 4))#candidate|12231|(2, 11, 4)|var|float64
output = func_12230(var_12231)
func_12232 = relay.Function([var_12231], output)
mutated_mod['func_12232'] = func_12232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7836_call = mod.get_global_var('func_7836')
func_7837_call = mutated_mod.get_global_var('func_7837')
call_12289 = relay.TupleGetItem(func_7836_call(), 1)
call_12290 = relay.TupleGetItem(func_7837_call(), 1)
output = relay.Tuple([call_12289,])
output2 = relay.Tuple([call_12290,])
func_12309 = relay.Function([], output)
mod['func_12309'] = func_12309
mod = relay.transform.InferType()(mod)
mutated_mod['func_12309'] = func_12309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12309_call = mutated_mod.get_global_var('func_12309')
call_12310 = func_12309_call()
output = call_12310
func_12311 = relay.Function([], output)
mutated_mod['func_12311'] = func_12311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8413_call = mod.get_global_var('func_8413')
func_8415_call = mutated_mod.get_global_var('func_8415')
call_12317 = relay.TupleGetItem(func_8413_call(), 0)
call_12318 = relay.TupleGetItem(func_8415_call(), 0)
func_1409_call = mod.get_global_var('func_1409')
func_1412_call = mutated_mod.get_global_var('func_1412')
var_12327 = relay.var("var_12327", dtype = "float64", shape = (18,))#candidate|12327|(18,)|var|float64
call_12326 = func_1409_call(relay.reshape(var_12327.astype('float64'), [6, 3, 1]))
call_12328 = func_1409_call(relay.reshape(var_12327.astype('float64'), [6, 3, 1]))
output = relay.Tuple([call_12317,call_12326,var_12327,])
output2 = relay.Tuple([call_12318,call_12328,var_12327,])
func_12334 = relay.Function([var_12327,], output)
mod['func_12334'] = func_12334
mod = relay.transform.InferType()(mod)
var_12335 = relay.var("var_12335", dtype = "float64", shape = (18,))#candidate|12335|(18,)|var|float64
output = func_12334(var_12335)
func_12336 = relay.Function([var_12335], output)
mutated_mod['func_12336'] = func_12336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9394_call = mod.get_global_var('func_9394')
func_9396_call = mutated_mod.get_global_var('func_9396')
call_12437 = relay.TupleGetItem(func_9394_call(), 0)
call_12438 = relay.TupleGetItem(func_9396_call(), 0)
func_8171_call = mod.get_global_var('func_8171')
func_8175_call = mutated_mod.get_global_var('func_8175')
const_12507 = relay.const([9.407142,-3.467495,-8.617878,2.306954,-0.245987,9.114658,-9.038040,0.807139,6.526302,-0.508614,5.888912,-1.532977,-5.290842,-3.075839,-3.862123,-3.502085,-2.444085,2.099202,-8.175548,-6.582106,9.565805,9.708472,1.362853,0.108200,-0.442555,3.544927,-8.429747,-6.982512,0.604295,-3.440012,-8.477926,6.202329,7.391087,8.313519,9.001319,-6.289599,-8.907475,-3.704647,-8.269186,-2.993059,-4.323590,-9.319116,7.578320,1.786355,-3.272291,5.028253,-7.220522,3.434814,0.144822,-1.390240,-0.223653,7.626716,-5.350904,8.618726,4.942195,6.215505,1.888288,3.472507,5.910024,8.814342,-8.597980,-5.337427,0.049905,8.325845,9.645670,6.619324,-9.378236,-0.151326,3.554512,-6.855083,8.978129,-6.677796,3.958451,-3.038858,-2.806381,-5.167500,-8.457152,8.000968,3.201178,-6.419021,-6.664578,-0.399884,-3.568181,4.278183,-8.515144,-6.244920,-0.753413,5.176930,-2.671386,-9.235072,0.753139,-7.224511,5.539333,-1.890078,-0.687686,5.672397,-1.949041,1.683803,-0.024056,-7.323271,-1.821370,4.633952,7.862024,7.678448,-7.258391,-8.961623,-9.676872,9.189538,3.166941,-4.148508,-4.677897,-7.326412,-1.212990,7.390202,0.614109,9.416459,-0.865338,-1.104300,0.942304,-7.164318,0.343254,-2.974648,7.244312,6.514157,7.808393,-8.441679,-2.037658,-1.147945,-0.841687,3.993462,-7.616889,-5.377673,0.955917,-5.378511,-9.752608,-1.819814,-3.611151,8.686995,-5.442001,-1.460964,2.434861,8.823546,0.008244,-7.652624,9.414190,4.908739,-6.673723,0.501644,-2.548368,9.941688,-0.093159,-4.769199,-0.137500,-4.187681,6.288898,-1.332672,1.505162,-8.956881,4.802545,-7.140521,-1.321143,-5.136942,4.306528,3.665234,-1.585512,-2.591760,-9.133661,3.318597,5.644826,-4.013356,-0.679415,6.438426,-3.020266,-8.481085,-4.808493,4.624881,6.244270,9.155002,3.529745,-8.888014,3.542872,-8.440724,-1.834665,-1.087273,8.472965,-9.180877,9.262534,0.024249,7.529026,-0.876181,-5.757945,-4.994020,7.493300,3.576801,-5.788961,-3.799030,-6.810854,-2.114655,-8.392002,-4.478484,7.558330,2.617564,-0.564606,-3.419836,8.771643,2.168187,-6.065406,9.951237,-8.561111,-0.263231,-9.535798,-9.377393,6.735050,2.134052,-5.802375,7.685505,-4.862190,-1.711569,3.401615,-0.183053,3.857906,4.992786,-3.526513,-2.149785,5.112037,5.974910,9.198223,-4.849727,-6.819677,8.824805,-3.384746,-1.159246,6.010293,8.194303,-6.163763,9.783059,-5.265984,6.060736,7.008954,6.421164,6.326137,3.151352,-4.735886,5.340674,5.730333,5.315917,-5.278030,7.034701,6.009741,-0.436991,-6.025757,4.507053,-1.170283,7.196629,-6.400761,-6.070470,-0.454949,9.557475,-6.264338,3.471601,1.392716,6.193119,7.679005,2.101800,1.622405,-5.860647,-2.109483,-6.278283,-4.134240,-2.175865,-9.771873,-1.849155,-3.468463,-0.658660,4.578059,3.064019,-8.260620,-4.550960,7.250353,-2.900583,0.282179,-2.046940,7.377247,3.643478,9.251421,-4.422647,-5.713174,-8.554264,-7.268157,1.182452,-8.693524,-9.967758,2.229901,-1.962591,5.021128,-6.117008,8.802416,-6.093877,5.551844,4.766880,4.880889,4.475280,-9.789478,6.682815,-6.398235,-5.543942,1.581852,7.932908,4.820389,6.087879,1.138276,-7.929052,-2.902106,2.349720,-0.931109,-0.412514,-1.913181,2.312353,2.327181,-9.914101,-5.436156,8.142057,9.510550,-8.183366,-5.082831,8.255681,2.592161,1.000611,-4.647292,-1.072195,7.910797,7.792432,-2.285784,-9.338475,8.446656,2.597385,-4.996778,5.731132,9.308808,-0.791656,2.187853,2.306853,3.573837,-1.093921,2.980400,-7.777116,-9.949723,2.059301,1.528725,-6.819588,-7.636605,-2.347801,-4.152806,-1.501233,6.607702,-9.608718,6.121726,-3.047097,-2.522180,-6.956333,0.066268,-4.813031,-3.475177,-2.177362,9.800421,-8.743060,-8.451905,-5.442152,-8.369848,-2.860122,-6.591348,-5.854510,7.517350,-3.096941,-2.661583,4.444120,-7.541582,6.214046,2.468063,-4.283954,-5.089665,-0.383634,2.909683,-9.919610,-7.686117,4.093599,9.333777,-6.100080,-5.515039,-7.041287,8.005290,-0.614020,1.557184,2.208007,1.689167,0.998976,-1.465537,-5.450791,4.335373,-8.685216,-9.819260,-8.634303,7.056794,-3.793104,7.160538,-1.142596,-8.217166,-4.501979,-6.626361,6.577517,5.394149,-8.010094,-5.837475,9.981982,6.796651,7.073023,-2.428565,8.575241,-0.229508,7.152454,-7.539575,1.812569,8.812895,-2.020508,6.005768,5.608914,-5.504312,-6.660916,3.934468,-5.792062,6.644753,-8.499347,2.049122,-9.619734,6.160104,-0.692951,3.348065,-8.215866,5.116283,1.254839,-7.962121,-0.288304,-7.587951,-9.543000,-7.186523,-1.143726,-6.484980,3.015467,-2.629281,-7.776245,-7.527374,8.529024,-7.630281,-8.011447,-7.407048,-7.816737,-2.539177,3.825487,8.865740,-3.892085,1.331434,-7.667454,9.045488,2.862520,7.049555,7.113822,-7.026910,7.178275,9.155450,0.587532,5.158663,-5.185791,-0.957386,-5.083033,6.356595,9.706170,4.810397,6.901341,-2.110300,-8.862675,-2.533189,0.703127,-0.007735,0.668172,-8.384855,3.734901,-8.987465,9.588169,-0.567327,-4.843003,7.070238,-1.077718,7.378916,3.958090,-9.600701,3.008672,-7.234810,-2.691856,-5.807313,-6.748602,-0.264477,-5.016979,5.074506,5.453418,-0.470137,-7.140003,5.475385,-1.989263,-5.540686,-9.836641,-0.574130,3.877941,-8.463248,1.117999,1.059205,9.453159,-3.820600,-4.873186,-7.369150,2.775130,2.580366,-0.357762,-6.911350,-8.454804,-5.061275,9.718605,-2.297386,9.042978,-9.436836,1.867277,-8.687872,9.725803,3.857622,7.460272,4.446341,-8.665105,-6.525999,-1.316541,8.065431,6.802499,7.444035,-3.857863,7.966001,2.191937,1.772323,8.977034,5.100549,-2.888525,-0.269569,-1.431037,-4.532240,-1.576093,6.810555,2.601974,2.011606,9.165378,4.046503,2.057136,9.255311,1.349043,4.763130,6.069602,4.231232,4.851895,6.902312,-3.383091,-7.924602,-3.487823,0.790172,5.554433,-6.202772,9.575694,-5.450248,-6.457542,2.440441,-3.327933,-9.816611,-7.006649,3.041380,2.210626,7.669371,-2.097573,-5.487060,-9.048634,-9.511122,6.911353,-2.072726,9.375183,1.136009,-8.236317,6.933334,1.238285,-8.158927,0.309647,-4.821322,-7.116617,-9.574244,9.107030,2.231014,-3.326755,7.942602,-0.301819,7.140679,2.882359,3.620020,1.377673,-9.575703,-7.632544,-9.203671,7.473154,-3.033952,9.759101,-6.955947,-9.762969,-5.673507,-8.179334,-9.444767,9.954423,-2.970370,-2.354589,-5.115238,-6.200368,-9.824679,-3.076357,-6.835681,4.775527,2.705611,-8.911715,-9.656473,-0.221754,1.264378,-0.894315,4.536491,4.687688,-5.529892,-9.605020,-3.890063,-2.959680,9.114163,0.246599,-5.687026,6.881912,1.062679,4.762598,-3.184584,-3.756194,-4.336092,1.319555,-8.131346,4.761942,-5.162774,-3.580237,-0.577392,3.526423,9.716890,-1.307737,-5.610246,2.471840,3.326336,1.244800,-0.624720,0.471395,-5.424928,0.427381,-8.638539,-6.731173,-5.198653,6.639125,6.311674,-9.548117,2.067729,-3.324427,-8.512914,-4.882374,-8.283194,0.924048,3.291513,-3.311065,4.298478,3.979317,-7.729383,-5.653434,-2.971559,-3.772661,8.150037,-0.304144,2.806898,-6.864056,-5.936935,8.093686,-3.366780,-6.783937,6.615153,5.645419,-3.209238,-9.820527,-3.659346,3.200103,-8.601166,-9.689437,-3.041059,6.088975,6.581045,-4.617121,-4.482214,1.631854,-5.768052,-9.513961,-9.356374,4.780116,-2.046949,8.668606,-1.131053,8.460708,-8.263118,-0.753749,-0.059633,-7.298279,9.059265,-8.539883,-2.471535,-6.581293,5.536458,6.084945,2.464874,-1.362015,-6.237087,-7.791939,-4.043387,-4.842032,-3.193985,4.312343,-0.283781,-3.310207,-9.891961,8.345250,-0.566190,-6.751769,-2.932944,5.183131,-2.242811,-4.456724,-8.605521,4.513422,-6.927198,8.566148,8.779255,-2.192404,0.332409,9.079834,4.070492,-7.859636,6.572123,5.671104,-2.733674,7.201406,-7.635130,-8.882796,-3.319802,3.576881,2.316376,9.491880,3.994426,-6.956690,9.340955,3.264978,-2.711776,-3.270780,-1.009832,0.780448,6.454447,1.959160,-5.994250,-0.608218,9.571141,-6.184853,-8.805459,9.130949,9.386170,-1.201671,-9.648234,9.191144,-3.721235,-8.665260,1.883942,4.830789,-6.750511,-5.347085,-2.548710,5.832229,-0.947808,-2.336472,-5.879850,-5.205740,7.354320,-8.859529,-0.901968,-7.566604,9.709777,1.563589,5.271693,1.799148,1.074393,-8.107395,-4.268987,-1.522612,8.316214,-0.064131,-8.881634,1.361097,7.080423,0.263136,6.522404,-0.724778,-7.651624,4.592814,3.929133,6.443437,-8.856270,-7.304079,-7.046291,6.097785,-8.325794,4.240591,6.728527,-0.351458,-4.229527,-1.506392,-0.067319,-4.512900,9.215405,-6.510693,7.487315,6.138267,4.399546,-2.171596,-7.527395,-5.186463,5.545757,-1.329131,-8.874030,-1.221408,-9.567025,0.899957,7.202337,-8.165903,5.500115,4.651595,-7.450381,4.480982,5.538748,9.299294,6.817326,-2.077600,6.752583,2.969825,8.619492,-0.477206,8.333776,-2.861696,-1.457321,2.862978,4.226214,-0.938782,4.076037,-1.972053,8.878867,2.041637,6.201878,-2.995674,-2.498725,-4.291194,1.994121,4.750706,-4.410183,6.812277,-1.676528,1.132474,-1.718856,-0.140655,6.446213,-0.270290,-4.898656,5.670432,6.520424,3.336650,-0.262696,5.179787,-8.310133,-0.842065,0.513053,8.178848,-5.553909,6.960708,-9.524579,-0.515550,-4.486004,7.937457,-9.681179,-4.788745,-6.580079,3.747072,-9.814778,-5.492709,-6.655911,6.693107,-1.937987,9.593254,2.206512,2.378760,-3.555953,9.735047,-0.179434,-6.622815,-5.807689,-4.867376,-1.291233,0.950922,5.942121,7.480381,-6.683436,0.680690,-1.457873,8.659117,5.436470,9.877825,-2.721074,1.103328,3.311824,-7.197470,-4.826606,-1.103577,-1.442442,1.237868,1.855421,5.424098,-6.739868,3.990411,-3.755752,-2.110872,3.313330,4.809637,7.406740,3.579156,-1.051488,-1.962939,-0.177422,9.667879,-8.076958,-2.269642,-1.443753,4.330254,-5.862322,5.400671,1.051589,2.757347,9.115578,-1.138049,2.613113,-3.269086,8.320849,-1.463618,9.695314,8.630020,9.544705,-4.797322,2.553098,-6.005079,-8.092294,-9.426382,4.099511,-1.078268,3.225351,8.794426,-8.563888,-4.107275,-9.397783,-6.222821,3.643160,7.310429,2.488656,-8.728359,7.311774,8.888054,-3.050878,9.446413,3.539019,-1.708606,7.830723,1.722002,8.365271,9.148734,-0.600005,-0.153497,1.579256,-4.822477,4.358614,-8.117990,1.947353,-3.251730,8.815411,-0.080702,9.423727,2.633185,-5.557350,2.046618,3.136346,-5.014429,-0.981916,3.101793,-9.919049,-1.716118,-2.849807,6.993110,-7.716460,3.669345,7.229928,-6.027395,-8.518238,8.947616,-8.902166,8.192082,-7.148769,-6.911650,-0.785459,-5.774699,0.881722,-1.533725,9.286334,-7.437516,2.589387,-4.851597,0.183660,2.660861,-5.854590,-2.659453,3.279795,-6.975574,2.786182,-5.216155,-5.690178,5.118842,-6.458239,7.166709,2.359854,6.636036,0.876657,1.326126,4.404787,5.655951,-8.539351,-2.459777,3.521782,6.772365,0.423213,-1.203025,-8.921819,-8.623603,7.443965,8.910927,0.521594,3.128774,-4.361656,2.842306,6.588708,0.880226,-6.448468,-0.904146,4.112950,5.073720,7.054776,-9.315537,6.802912,-3.487233,7.602003,0.929262,1.789055,0.112996,5.759176,3.234679,2.026551,-5.797578,-8.914170,1.853981,-4.089515,0.194963,-1.255591,-4.862820,-3.874612,-7.154616,-5.606356,-2.072601,-9.468757,5.162944,-2.862562,8.612206,3.200400,2.642248,-2.746540,8.921311,7.074512,-0.463047,4.716594,0.119446,-5.376383,9.397776,8.810983,-6.475802,0.508151,-9.548830,-8.421188,-2.766471,0.016443,4.843053,-8.215270,2.544894,9.637250,-5.054750,-5.765568,-9.229429,2.830176,5.486209,1.607260,1.424656,3.055973,-3.637648,9.757035,1.698929,9.861222,-3.748972,-2.582101,7.660543,2.312344,-6.251642,-2.622814,-8.439577,-9.662255,-1.831868,9.988255,-1.871338,2.582026,-3.407198,7.033305,-2.921710,8.762227,3.385593,-3.062769,7.915945,-0.858179,5.211651,4.507717,-7.237668,6.206725,2.477628,-5.001947,4.113793,3.822302,-1.054194,4.200264,8.015863,0.968098,-5.702480,1.486555,-9.862631,6.048893,-2.495996,0.271934,-6.483220,-0.815830,-7.859095,-6.964225,-1.494929,7.013586,-7.118186,0.684249,6.552618,-7.038151,-1.407109,-0.538544,7.788657,-1.363246,-5.519205,4.109514,-2.028082,-6.209242,-9.651934,-9.726764,-3.775328,-9.199424,3.071116,-9.129640,-5.201582,-1.471768,9.827024,7.830846,0.501149,-1.540607,-4.431537,-4.741862,0.043993,3.986511,6.257639,2.607162,2.025135,8.161370,3.057671,-8.492965,-5.640400,2.422260,0.062115,4.308264,-6.806018,-2.204199,1.703397,-7.058168,8.387759,-3.350515,4.447179,4.194772,8.143334,3.775810,-8.022167,6.285821,5.524176,-2.557474,8.380043,5.747555,-7.028052,-3.018722,-9.636576,-1.294546,-4.430211,4.435878,-6.102670,6.275328,2.172225,9.693555,-9.104199,-2.329569,0.366515,-0.445944,-9.360393,-3.971669,2.119426,-4.452495,6.230415,9.293000,-5.140342,-3.802203,3.391217,-0.684194,-3.364799,5.755596,-0.359146,-0.593342,-2.301104,7.213841,-4.469189,5.365997,-0.219424,-4.723555,6.730831,-9.260691,-3.126964,-3.466069,-6.332629,-0.082628,-7.886169,3.346827,7.714382,-2.880394,-8.063067,5.589102,-4.633144,-2.646441,-0.521460,-3.663248,-8.926358,8.753147,0.420783,1.979868,8.647475,2.601394,9.375311,-3.166955,-3.855724,-4.084561,-1.585968,-7.387892,1.643575,-4.963597,4.847928,6.070886,2.440052,-8.097015,-6.000930,-6.243980,9.083217,-1.935113,-4.537273,1.774557,7.783839,3.090096,6.487382,-1.678623,-7.902936,0.379831,-1.823068,2.131459,7.280450,-9.243079,9.960879,3.493690,-0.949065,6.654933,2.767299,-0.069000,7.826384,-1.405759,8.009837,1.067350,6.195755,8.881021,4.225684,8.414625,-3.109634,-9.494157,-6.062954,-3.197632,7.445099,4.759531,-0.338411,-1.751466,6.031179,4.305675,3.891550,-3.934752,0.887553,-9.136056,6.689780,8.365588,-1.722158,4.830833,-0.225899,9.117168,-5.512500,-7.217480,-7.373619,-5.523912,8.525121,-2.470463,-0.450824,-5.049918,-7.407694,-6.197858,-6.975923,9.017855,3.670351,-1.743493,-2.367487,-4.016011,-3.408231,-5.880636,3.876033,2.499676,-0.348138,9.682623,-6.889264,-3.324266,5.774868,-0.573581,-1.876453,-0.612644,3.750839,2.466937,-1.352963,-8.431596,-0.877691,-0.298150,4.690058,2.339137,1.479197,-2.471202,-9.779101,7.012511,8.216890,6.371804,1.555848,9.664916,-3.038347,3.005597,-9.324801,-1.695843,-0.374857,-5.432418,-6.179302,4.261541,2.067795,0.527222,-2.952956,7.398862,6.311097,7.123858,-6.047294,9.890254,-4.325957,6.332836,-3.406753,4.530695,-7.609547,-1.297054,1.171105,7.168613,9.516593,-9.178000,3.123763,1.899243,1.317862,0.766826,0.411330,-5.336150,9.278339,0.690594,5.890062,-2.825672,-9.514459,-4.362078,-1.517632,-0.433736,0.119701,9.695432,-5.178414,9.695651,-0.457209,4.462773,9.527267,8.418745,-8.406830,-4.546800,6.903352,5.151506,1.150300,-4.279208,7.593939,9.003613,2.054664,9.390297,0.139071,9.367389,-6.149621,8.375285,8.713062,-1.155277,4.253955,0.226801,-9.362234,9.278546,8.213320,6.818376,-1.774064,9.645438,-0.757046,-9.021048,7.541447,3.873932,-5.775677,4.176916,8.155152,4.916527,-9.655032,6.863720,-1.092308,-8.018598,-4.154137,-8.147931,-4.030886,8.681647,5.472226,-3.522813,3.008105,-2.293873,-9.402572,1.959384,3.489325,7.263988,-2.999760,-2.652738,6.823280,-6.430863,5.270751,-1.390309,-0.320083,-5.102518,2.350616,-2.338145,-4.633586,3.944663,-8.459410,-4.947409,3.113942,3.757163,-8.072784,-1.302273,-1.983913,-4.178793,-4.380805,6.358204,-7.713454,-2.264689,-4.738032,-0.233095,4.125022,8.681895,2.365202,8.373810,2.996058,-3.276340,2.810174,4.508190,2.124373,6.862197,0.318136,-4.553462,-0.332696,2.774470,7.992979,3.338829,5.805748,-3.182919,-5.941703,-9.644307,-9.797008,7.866136,0.496461,5.581585,-1.721414,-3.447702,6.250275,8.124590,7.609897,-4.287084,5.807542,2.106561,-0.370049,5.632207,-3.196877,6.251677,-7.503089,-5.534544,6.349375,-1.824650,-3.799779,2.538427,5.415224,4.596963,-8.284688,5.266014,1.985779,-7.588220,-3.360868,-8.901468,8.068799,9.672094,-6.320568,-2.119476,6.626553,-6.279021,8.607101,0.692290,-0.795319,-6.066023,-3.778501,-7.508930,-9.744611,0.383247,-7.844474,2.660962,3.214266,2.376809,-2.630506,-9.728506,-1.769876,1.670535,-5.191690,-3.774727,8.364629,9.994174,-7.665086,0.517802,0.669622,2.775317,-6.698144,4.792215,8.607016,-8.209716,-3.781766,4.433705,6.479444,8.200231,8.679710,-7.009944,-6.216168,-6.903095,-4.446108,9.767145,0.690600,0.555688,-0.354267,3.499970,-6.956354,4.757661,-8.991153,1.970858,-4.037272,-3.682538,3.392450,-1.744023,-9.164537,-3.274709,5.746003,-6.176309,6.654181,-4.927952,8.105200,6.388058,7.211390,-2.265169,-9.019591,6.930049,-3.423839,-3.623875,6.969086,3.290903,-6.415941,-1.057245,-3.534036,-7.269661,-3.265553,9.061020,-5.658087,7.626642,9.092765,-8.142453,-6.017548,-3.310875,5.121718,-7.042926,-6.075888,-1.442200,7.135500,-5.200955,-5.238865,3.637299,6.364784,-0.774092,-9.696008,-3.845382,6.220319,0.006933,-3.521173,1.890127,-3.167973,-6.151366,9.753897,2.786943,5.393333,-4.289370,-8.954710,5.705522,-8.505311,-2.365855,6.400599,5.484083,8.295201,-0.155695,-8.816025,3.639557,1.611251,5.072880,-5.306399,-2.077970,-2.641963,4.769487,-9.628484,2.668599,-4.178855,4.605146,-1.477993,5.936603,0.932004,3.968778,1.416735,5.483847,2.576282,1.981113,4.195565,4.837111,5.748565,0.829588,3.747180,-8.678958,-7.909517,-2.302067,-7.196232,-5.629678,7.757166,-1.331941,-6.009850,-8.301159,-9.697858,1.033392,6.893305,-0.607811,-4.828435,-4.498964,-2.755534,2.699313,2.713172,6.971559,3.303267,3.761668,8.425799,5.415797,5.022347,4.839050,-0.817407,-8.325906,-2.893447,-1.861324,-4.752634,-6.830110,7.685280,4.149963,3.303766,2.988315,-6.146511,-0.438518,-8.520908,5.945997,8.600661,2.182407,8.086934,1.469885,-8.925236,-5.760431,-7.449543,9.104976,4.076701,-3.452869,6.348694,8.529541,5.827666,-1.916790,-9.636311,9.939849,-6.315434,0.641589,-9.094233,8.546590,-2.575629,6.288071,8.049504,-9.275717,1.404263,8.856058,-2.634490,-7.235269,-8.986585,7.296903,-4.759502,-9.357266,-9.790505,9.155015,-5.982159,2.127498,-0.808184,-9.662531,-3.362101,-4.403142,1.272149,-5.920706,9.827251,2.629666,6.172939,-3.085137,-7.500826,8.238787,-7.346819,4.179154,9.111417,8.765239,-0.637524,0.962765,-3.815809,-7.074972,-9.343519,-2.527298,-6.584416,5.121115,-9.322594,6.049860,8.879672,7.426470,9.561259,-3.543393,-9.979385,0.807870,2.779685,8.147860,-5.737953,-0.052918,-3.599952,-7.902687,-9.735395,5.598590], dtype = "float64")#candidate|12507|(1815,)|const|float64
const_12508 = relay.const([6.426337,-2.569913,-5.930160,6.239576,-1.562769,4.685291,-1.709741,-2.074536,-0.317321,5.571228,1.044852,1.084591,5.380586,-4.058449,-7.015895,1.480883,2.370298,-1.231414,0.302961,-8.799590,-9.596265,1.456346,-5.046950,-6.282749,-5.659857,4.741367,1.770892,-5.783811,1.611336,-9.796520,-8.640627,6.942478,6.322662,4.706735,-5.950720,9.034765,0.041666,1.014302,-6.202932,9.798180,8.274910,-6.076393,1.171516,0.955977,5.637304,-9.892191,-7.653663,1.491008,-4.139828,-1.982684,-8.430255,9.545699,-7.345199,7.846123,-8.032965,-8.769966,-0.614846,2.673082,1.355638,-1.087130,-2.154861,-6.557433,2.367389,-4.760954,8.665169,-2.316158,-9.011736,5.370411,-2.575841,0.813219,8.761826,-5.877274,-9.656203,-5.792159,-5.041865,0.610314,7.658831,3.293359,6.076039,-3.768211,-5.787881,0.958943,7.196251,-0.633565,6.665034,-9.704936,5.506217,-6.786443,-6.110177,0.302127,-9.052907,7.277267,-1.433996,-8.762750,1.923699,-3.743420,0.447925,-7.814099,6.375007,-3.599836,4.832865,0.923071,6.960238,-9.522188,-6.418630,-7.590485,-3.243836,1.822815,8.037018,1.230980,-8.667246,-2.761223,6.134083,-6.558624,1.763862,8.043104,-3.622574,6.636510,7.131829,0.227246,7.790974,-5.384328,-7.474217,3.481590,6.364506,-1.200854,-1.339467,7.634896,2.131006,-6.912114,-8.977335,9.839259,4.771430,-7.998353,9.523290,-6.268528,6.186585,-1.272129,-3.612987,6.421248,-3.864419,-0.948847,3.003851,-4.488250,5.955017,4.611054,7.056599,-4.980628,-7.811285,5.272919,1.059934,-4.704594,-4.264683,-3.952695,-1.412690,-8.308186,2.880372,-5.712055,-0.984931,3.598500,6.191995,9.997241,-7.369563,1.703646,-1.663293,-9.397432,9.544684,-8.139743,6.116265,-0.598524,2.982464,1.187662,6.304089,2.271851,-5.880205,-4.505638,0.890913,-1.016285,6.671236,-9.036292,-1.366651,6.889022,-1.744453,2.128604,-5.898876,8.687463,-6.276899,-1.846930,-8.044500,0.642530,8.060429,1.114916,2.229283,-7.660902,3.855666,-5.349440,1.769872,6.821086,-1.221887,7.504839,1.114745,-0.723640,8.854289,3.585502,-4.238252,5.694280,-0.932774,-5.328970,-3.069792,4.527365,-1.093340,-7.707302,6.523411,7.402444,-8.573306,7.157206,3.249877,-4.308799,-3.974399,3.539957,-4.856680,-4.156091,0.952737,5.657018,4.310781,3.912297,-8.880926,4.397775,-6.818274,3.289016,-5.720311,-7.337030,-3.011825,-6.884995,-8.581593,1.136495,-0.410281,-5.485190,6.413393,-6.440445,-4.212767,-4.601676,5.327604,-6.758014,-6.071850,-5.014759,-2.731558,-4.831431,6.924781,-9.470104,-6.720942,3.191401,2.572439,-6.418469,7.538582,-7.505916,8.479006,-2.510507,-6.124974,-0.907920,6.619497,1.194320,4.178821,-1.824930,2.823410,-0.506494,8.698932,-6.820589,4.912771,4.759647,6.460707,-2.653642,-0.233354,5.761652,-5.243430,8.504706,1.029515,5.800195,-9.190891,9.502410,-7.452483,-4.957716,1.971680,1.164339,5.787773,0.008236,-5.669946,5.542534,7.961249,6.435313,-9.069132,0.322388,-1.822408,-6.168574,-0.775798,-4.690830,-7.667217,-7.888424,3.054615,-9.881829,-0.247446,-1.629781,-6.421199,6.338727,-2.428349,8.573340,7.323856,-9.700135,6.833520,2.823186,0.518267,2.331064,-9.244878,7.171664,8.237093,-9.198691,-3.002757,-5.708864,4.457659,-5.259216,-3.729535,-8.612053,-2.069905,7.288188,-9.898772,9.936291,-8.300566,4.310880,7.057430,2.956681,-3.214355,-5.015039,-9.214529,1.816127,4.877319,1.082689,5.471575,0.570133,1.806685,-4.406149,7.924478,2.605686,-5.165767,-8.447770,9.779692,-3.080974,-5.954823,-6.304463,2.669282,-2.464981,6.499914,-8.320637,2.487776,-9.732592,7.291333,-1.053272,5.514146,-2.869293,-6.426592,6.316799,-5.143952,-5.498280,-9.171149,2.101744,-0.723586,-1.038185,-0.311888,9.023751,8.291236,-6.299431,-0.046222,2.136137,-1.420195,6.140468,8.296063,-1.654119,-0.398673,-7.822475,-0.306066,-0.458284,1.357326,-3.604529,6.867283,0.613158,-9.384078,3.710401,8.086049,-6.426980,8.526237,-1.016026,-4.590801,-7.258957,5.410674,8.942510,6.661419,2.855195,2.190746,-2.596338,2.209951,7.760068,7.232287,-6.073143,0.008210,-5.664708,-4.028253,1.624575,5.404849,3.558023,-9.953702,-1.406287,-5.206929,-5.588104,-5.462493,-8.055483,2.651911,0.863156,7.852270,8.175870,-8.771762,0.162245,-7.679629,3.668124,-8.937591,0.376845,4.317132,-2.287187,9.473305,8.868842,2.657694,5.518295,8.123974,0.458213,-5.467635,-7.689026,-5.383143,2.318125,-5.990690,0.511430,3.972771,-8.865543,-8.152500,-8.889810,4.261760,0.784248,8.704018,4.624774,5.990871,9.070377,8.754315,-9.303614,0.171060,1.695866,-1.542722,2.405617,0.425821,5.274848,-8.509849,2.970787,1.131120,0.648134,2.976923,-6.782083,5.252532,-5.426764,4.579112,6.558160,-6.759599,-0.058147,1.502786,-8.815295,8.943728,-7.746730,5.999834,-7.717632,2.905270,2.135387,-7.884091,9.224574,-0.947569,3.735832,1.374547,-1.783004,4.392777,-4.525299,-5.881832,9.125946,-3.940690,-1.315987,9.085185,7.545986,-8.589198,5.517020,-2.968057,-5.095888,-3.801050,-2.443782,-5.061596,5.169540,0.354432,-2.019984,-6.983440,-6.993302,-9.765484,-1.619393,9.763758,-2.049986,-3.940643,-8.704830,-9.192491,0.866947,-3.333636,-8.455618,4.526193,-1.566080,-1.063842,-4.407703,-2.397907,9.201322,1.997024,-1.402144,3.312530,-5.797686,-9.539470,-6.313742,-7.312490,2.819151,7.055440,4.768469,6.578211,-2.485613,1.878198,-9.844200,8.443289,-8.704661,1.778252,0.923247,8.159433,3.423646,-6.474897,-8.003505,2.752390,-3.783596,-8.747026,7.757462,9.592877,2.401201,3.029866,3.837359,9.999095,5.652029,-8.789915,-1.038781,6.468885,-5.809553,4.735389,-5.892949,-2.957106,-8.021785,-3.292235,5.784307,7.224935,-6.704385,-2.154914,4.426787,6.032283,5.354352,2.220273,7.223961,6.519230,-3.111153,9.922479,2.375135,3.963052,-1.554674,-7.680950,-9.763867,-3.117454,-9.460540,-0.495130,-0.376031,-3.082433,5.630567,1.484837,-6.933950,-9.390629,-8.715317,0.010046,-5.692954,4.731399,0.480807,-6.131129,8.074510,-8.753339,4.539705,2.395894,1.904595,0.517297,1.452719,0.109889,9.332270,-2.643320,6.719012,-3.439557,8.057248,-5.599234,6.954917,-9.292478,3.833277,-9.748280,1.498478,6.187272,9.845451,1.793717,8.335312,3.151796,7.912557,-0.312950,0.346658,-3.487599,-3.189614,1.499218,1.453791,-9.799346,4.168651,0.349725,-1.664788,5.585398,-1.227140,-9.264656,0.832104,-8.944179,-8.029937,-5.450220,3.437417,-2.979521,3.780051,2.315445,9.137599,-7.661556,-8.230663,6.324316,-4.054393,6.875905,4.318446,-3.775020,9.395080,1.966924,-4.916391,9.288303,-7.151806,1.568353,-7.878039,-0.823207,2.335945,-6.719221,8.137703,-9.879827,-1.962644,-4.852042,-4.483264,-4.106559,6.187726,1.263036,7.873413,-2.831870,-2.016410,-6.775341,-9.387031,-4.525134,0.942037,-5.155295,-5.617493,-7.754449,-3.808952,-0.195799,1.530025,-0.724432,5.371009,-3.121100,-7.126262,-9.668319,0.347338,1.423781,-1.495944,7.137438,-6.125562,-5.633497,-7.802062,8.532581,9.222126,9.212576,5.447861,1.789134,5.800558,6.591118,-0.482849,-1.777266,-4.031248,-1.945779,4.154937,-5.951379,6.105064,-6.161247,7.198565,-2.346846,-4.146369,-0.253503,7.071715,-3.015063,4.438054,-3.707516,2.502381,0.899355,4.787985,-0.168525,5.730429,-1.501678,8.282799,2.551398,8.138598,3.720579,3.531364,1.343411,-0.063466,-1.622682,7.386551,6.243571,2.553950,2.624753,-5.074372,-1.524610,-9.987026,-2.076550,5.573574,5.023137,9.287258,-7.016653,-8.966970,9.227894,9.870125,-8.987344,7.120351,-9.391269,7.528608,6.136517,6.387241,1.112011,-0.202313,-6.381146,5.956287,-2.457418,-7.913815,-3.904525,-9.372917,7.136957,8.241433,8.923542,-8.652048,4.048185,3.033552,5.792535,-1.618237,-4.649909,5.883108,0.785515,-5.225103,8.649868,-0.903621,9.054296,-6.713316,8.216701,6.748000,-8.640874,-2.612702,2.389472,-4.969783,-6.167051,5.676243,9.145217,2.566554], dtype = "float32")#candidate|12508|(780,)|const|float32
call_12506 = relay.TupleGetItem(func_8171_call(relay.reshape(const_12507.astype('float64'), [11, 11, 15]), relay.reshape(const_12508.astype('float32'), [780,]), ), 1)
call_12509 = relay.TupleGetItem(func_8175_call(relay.reshape(const_12507.astype('float64'), [11, 11, 15]), relay.reshape(const_12508.astype('float32'), [780,]), ), 1)
func_5182_call = mod.get_global_var('func_5182')
func_5185_call = mutated_mod.get_global_var('func_5185')
call_12532 = relay.TupleGetItem(func_5182_call(relay.reshape(call_12506.astype('float64'), [11, 11, 15])), 0)
call_12533 = relay.TupleGetItem(func_5185_call(relay.reshape(call_12506.astype('float64'), [11, 11, 15])), 0)
func_5182_call = mod.get_global_var('func_5182')
func_5185_call = mutated_mod.get_global_var('func_5185')
call_12534 = relay.TupleGetItem(func_5182_call(relay.reshape(call_12532.astype('float64'), [11, 11, 15])), 0)
call_12535 = relay.TupleGetItem(func_5185_call(relay.reshape(call_12532.astype('float64'), [11, 11, 15])), 0)
var_12544 = relay.var("var_12544", dtype = "float64", shape = (1815,))#candidate|12544|(1815,)|var|float64
bop_12545 = relay.minimum(const_12507.astype('uint64'), relay.reshape(var_12544.astype('uint64'), relay.shape_of(const_12507))) # shape=(1815,)
output = relay.Tuple([call_12437,call_12506,const_12508,call_12532,call_12534,bop_12545,])
output2 = relay.Tuple([call_12438,call_12509,const_12508,call_12533,call_12535,bop_12545,])
func_12549 = relay.Function([var_12544,], output)
mod['func_12549'] = func_12549
mod = relay.transform.InferType()(mod)
var_12550 = relay.var("var_12550", dtype = "float64", shape = (1815,))#candidate|12550|(1815,)|var|float64
output = func_12549(var_12550)
func_12551 = relay.Function([var_12550], output)
mutated_mod['func_12551'] = func_12551
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11815_call = mod.get_global_var('func_11815')
func_11817_call = mutated_mod.get_global_var('func_11817')
call_12582 = relay.TupleGetItem(func_11815_call(), 0)
call_12583 = relay.TupleGetItem(func_11817_call(), 0)
output = relay.Tuple([call_12582,])
output2 = relay.Tuple([call_12583,])
func_12584 = relay.Function([], output)
mod['func_12584'] = func_12584
mod = relay.transform.InferType()(mod)
output = func_12584()
func_12585 = relay.Function([], output)
mutated_mod['func_12585'] = func_12585
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12586 = relay.var("var_12586", dtype = "int64", shape = (2, 14, 16))#candidate|12586|(2, 14, 16)|var|int64
const_12587 = relay.const([[[-7,-9,6,7,-10,9,-8,6,1,-1,-6,8,2,4,10,-4],[-4,1,-10,3,-5,-5,-7,6,-7,-7,-10,4,-4,-6,6,1],[-2,4,-9,4,-9,8,2,-6,-2,3,-7,-2,3,-5,-9,-1],[-9,2,1,-1,-5,-6,4,7,4,-6,6,2,-9,10,-5,8],[7,-1,6,-9,-2,9,1,-10,5,-6,7,10,-8,3,-3,-5],[-10,9,10,-8,-6,-8,6,-10,7,4,7,-9,6,6,4,-10],[-10,2,-8,2,-9,9,-10,8,8,-1,-6,7,4,-1,-7,-3],[-9,-8,-5,-1,3,-2,10,2,10,2,-4,7,-4,-6,-9,-1],[4,-7,2,-3,-7,-9,5,-4,5,-10,-5,-8,-5,-4,-5,-3],[4,10,-6,-2,10,-10,5,9,-10,-10,3,-7,-6,3,6,2],[5,-8,5,-6,3,9,1,-7,-6,-9,-9,-9,7,-8,-9,-5],[-2,-7,-4,3,10,5,-1,-4,1,8,-10,-7,-9,2,-3,2],[3,-4,2,-2,9,-4,2,-7,-1,-5,10,-10,4,8,-10,-5],[-10,7,6,4,9,-6,-8,-5,6,2,1,6,3,-5,4,3]],[[10,-6,3,2,10,4,10,8,9,-3,-1,8,-5,-4,-4,1],[-1,2,6,6,1,3,7,-9,-1,-7,-1,6,-9,-5,9,8],[-2,2,4,6,-5,-9,10,1,10,4,4,-9,10,7,-9,-9],[-7,3,-10,9,5,2,-5,9,-2,9,2,-8,-2,-4,-1,-6],[-8,2,-5,5,-8,-7,7,-10,-10,-4,7,-7,-8,3,-5,-8],[5,9,10,2,-9,10,-7,-7,-9,9,3,-6,6,10,8,2],[-9,-5,-7,8,-10,-5,9,5,-3,6,2,-6,-3,10,8,5],[7,8,-1,-1,7,9,6,-5,-8,-4,5,1,-8,-9,2,-8],[8,-2,-4,-9,9,-6,1,3,-4,-2,-8,-7,1,-7,-2,4],[10,-8,-9,5,4,-4,-5,-4,5,-8,-8,-3,2,6,4,-5],[-7,1,9,-5,-7,8,5,3,-2,5,7,-1,-6,3,6,-6],[-1,9,1,3,-3,4,-6,8,-5,8,-8,10,-3,-6,3,1],[7,5,4,-9,-10,-2,9,4,2,-7,10,-8,2,-1,-6,-10],[2,4,-3,10,-8,-2,4,-1,10,9,-7,3,1,-4,-6,-1]]], dtype = "int64")#candidate|12587|(2, 14, 16)|const|int64
bop_12588 = relay.minimum(var_12586.astype('int64'), relay.reshape(const_12587.astype('int64'), relay.shape_of(var_12586))) # shape=(2, 14, 16)
output = relay.Tuple([bop_12588,])
output2 = relay.Tuple([bop_12588,])
func_12597 = relay.Function([var_12586,], output)
mod['func_12597'] = func_12597
mod = relay.transform.InferType()(mod)
var_12598 = relay.var("var_12598", dtype = "int64", shape = (2, 14, 16))#candidate|12598|(2, 14, 16)|var|int64
output = func_12597(var_12598)
func_12599 = relay.Function([var_12598], output)
mutated_mod['func_12599'] = func_12599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6412_call = mod.get_global_var('func_6412')
func_6414_call = mutated_mod.get_global_var('func_6414')
call_12667 = relay.TupleGetItem(func_6412_call(), 0)
call_12668 = relay.TupleGetItem(func_6414_call(), 0)
output = call_12667
output2 = call_12668
func_12680 = relay.Function([], output)
mod['func_12680'] = func_12680
mod = relay.transform.InferType()(mod)
output = func_12680()
func_12681 = relay.Function([], output)
mutated_mod['func_12681'] = func_12681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7788_call = mod.get_global_var('func_7788')
func_7789_call = mutated_mod.get_global_var('func_7789')
call_12696 = func_7788_call()
call_12697 = func_7788_call()
output = call_12696
output2 = call_12697
func_12699 = relay.Function([], output)
mod['func_12699'] = func_12699
mod = relay.transform.InferType()(mod)
output = func_12699()
func_12700 = relay.Function([], output)
mutated_mod['func_12700'] = func_12700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9387_call = mod.get_global_var('func_9387')
func_9389_call = mutated_mod.get_global_var('func_9389')
call_12727 = func_9387_call()
call_12728 = func_9387_call()
func_7403_call = mod.get_global_var('func_7403')
func_7405_call = mutated_mod.get_global_var('func_7405')
var_12757 = relay.var("var_12757", dtype = "float32", shape = (66,))#candidate|12757|(66,)|var|float32
call_12756 = func_7403_call(relay.reshape(var_12757.astype('float32'), [3, 11, 2]))
call_12758 = func_7403_call(relay.reshape(var_12757.astype('float32'), [3, 11, 2]))
output = relay.Tuple([call_12727,call_12756,var_12757,])
output2 = relay.Tuple([call_12728,call_12758,var_12757,])
func_12762 = relay.Function([var_12757,], output)
mod['func_12762'] = func_12762
mod = relay.transform.InferType()(mod)
mutated_mod['func_12762'] = func_12762
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12763 = relay.var("var_12763", dtype = "float32", shape = (66,))#candidate|12763|(66,)|var|float32
func_12762_call = mutated_mod.get_global_var('func_12762')
call_12764 = func_12762_call(var_12763)
output = call_12764
func_12765 = relay.Function([var_12763], output)
mutated_mod['func_12765'] = func_12765
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12767 = relay.var("var_12767", dtype = "float32", shape = (13, 6, 15))#candidate|12767|(13, 6, 15)|var|float32
uop_12768 = relay.atanh(var_12767.astype('float32')) # shape=(13, 6, 15)
output = uop_12768
output2 = uop_12768
func_12774 = relay.Function([var_12767,], output)
mod['func_12774'] = func_12774
mod = relay.transform.InferType()(mod)
mutated_mod['func_12774'] = func_12774
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12775 = relay.var("var_12775", dtype = "float32", shape = (13, 6, 15))#candidate|12775|(13, 6, 15)|var|float32
func_12774_call = mutated_mod.get_global_var('func_12774')
call_12776 = func_12774_call(var_12775)
output = call_12776
func_12777 = relay.Function([var_12775], output)
mutated_mod['func_12777'] = func_12777
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7788_call = mod.get_global_var('func_7788')
func_7789_call = mutated_mod.get_global_var('func_7789')
call_12799 = func_7788_call()
call_12800 = func_7788_call()
func_9968_call = mod.get_global_var('func_9968')
func_9973_call = mutated_mod.get_global_var('func_9973')
var_12844 = relay.var("var_12844", dtype = "float64", shape = ())#candidate|12844|()|var|float64
var_12845 = relay.var("var_12845", dtype = "float64", shape = (1350,))#candidate|12845|(1350,)|var|float64
const_12846 = relay.const([7.171956,-1.589060,3.458509,-2.040455,-3.971997,-2.670709,6.335296,-8.175782,-5.322152,3.294530,-9.384775,-1.389160,3.586589,-9.735610,8.910953,1.212072,1.020340,1.764001,6.771416,3.500122,7.374631,-4.011059,8.198735,7.074488,9.533774,-7.486674,-0.521094,-3.778569,8.544215,4.604282,0.711398,5.885955,-1.285433,2.101474,-8.788245,6.278758,-3.408400,-9.463245,3.494075,4.292752,-1.744596,-7.801192,-6.614418,-6.018005,3.424752,-7.332381,-6.784415,5.611878,4.965759,7.552043,-1.604335,2.975225,-9.912255,-8.108626,-0.416899,-8.903198,7.753625,9.909944,2.659964,-2.716833,2.953007,7.997366,-2.977071,-8.289857,9.907979,-1.462043,1.137497,-7.732902,2.656549,7.505305,-7.074587,9.254890,-7.277217,-2.754857,-8.452746,-6.197102,6.329894,-9.865770,8.385055,5.152082,-0.227422,-0.471806,-7.174934,2.610019,8.647136,5.701216,6.355134,-7.231026,2.796105,6.518433,6.514923,-1.405930,-9.776185,-7.315021,6.917835,-6.488867,1.076888,3.053689,-8.591296,-3.080866,1.679456,2.367001,-6.597392,-9.812902,-5.261124,3.241335,-1.695404,4.725947,-9.401128,-9.437262,7.760046,0.952456,7.155987,-5.982650,-9.137137,7.760267,-9.106316,-6.374379,-6.442588,6.804657,-6.800973,-6.678103,-5.485859,2.100891,-2.588043,-8.747693,6.464037,-6.876162,4.261263,-5.455213,3.993603,9.857028,-4.534442,-8.147308,3.221204,-2.385755,9.529523,-2.371738,-7.642171,-4.957076,5.800374,-0.499718,2.464202,4.232947,-7.145532,-6.849921,8.999272,6.136234,7.140411,4.989936,8.682462,-0.515197,-7.264309,-1.182149,9.715368,5.615238,-9.355428,3.603938,0.583578,-0.796439,-5.457320,6.663097,-6.756058,9.906034,8.573638,-5.819455,-4.649775,9.102630,9.671954,5.349164,-9.174344,7.975680,5.110868,-7.944563,6.070497,-2.478291,8.167192,-4.838271,-0.857480,6.294412,-3.344414,3.967232,7.715613,0.691167,-3.330037,3.278020,-2.036842,5.077387,3.027079,-7.643667,-4.717147,-5.434434,-8.520822,-5.623934,-6.249729,-3.215102,2.471277,-2.667455,-6.914355,-4.092260,-0.899307,-7.000259,-8.312372,-6.655779,4.317986,3.600183,4.636744,-7.747133,-0.810554,6.701391,-1.536059,0.485345,4.450478,-5.614222,2.492950,-4.440875,-4.941231,-7.300115,7.934496,-3.718722,2.246861,-3.369602,7.766560,4.093043,6.784549,2.686386,-0.513038,-4.433350,-7.072418,-2.333290,8.168173,0.272715,5.496436,-8.864290,8.755722,0.657941,-6.545595,1.962316,-6.882878,5.083767,7.288559,-4.915802,4.540113,2.429746,5.940500,-1.429310,4.092659,7.561245,9.228732,2.372281,-2.350540,-6.110846,-2.316701,4.383926,-1.941818,6.358475,6.435368,8.715355,-3.296669,-4.128812,-0.935463,-5.370755,-7.422964,-3.086267,1.510788,-5.358097,7.286850,5.463659,3.406405,-8.946887,1.927371,9.851791,0.767336,-7.910786,-5.451501,-5.382315,6.099843,-8.921642,-0.518510,8.173190,-9.697505,3.175587,-9.530325,5.233600,5.590111,6.150445,6.113237,0.596338,-7.126835,-7.959704,-5.002474,3.865707,9.649798,-7.121981,4.655990,-7.022429,7.042415,0.160751,-9.753010,2.387089,-0.074356,-9.989431,-2.769148,4.748201,6.439112,4.050103,-6.451745,8.055589,-1.569213,4.704648,-8.472535,5.811990,7.972237,1.160881,5.966097,-5.798444,-9.003041,-2.089506,-0.273826,7.593593,6.233061,-7.736265,7.372908,-9.992193,7.143409,9.831129,2.120838,8.525247,2.340483,-2.107839,-6.319248,6.101004,3.668746,4.126944,6.496300,-4.110949,4.635264,-6.404042,-9.546390,-4.832798,-7.080369,9.286716,-9.429427,-9.973214,-9.286789,-5.735562,1.960156,8.639472,0.565568,1.417980,9.808845,-3.812547,-1.166064,8.092077,7.208054,-9.215917,-3.955017,3.991448,-0.422360,-1.275909,-8.020427,0.237478,-1.012473,-3.564347,9.036755,-4.569571,0.685077,5.228219,2.309365,3.587925,-6.940293,-5.067600,1.092916,6.821197,-4.175953,-8.212345,8.339657,-1.778423,-3.292331,6.874572,-2.144319,-3.487188,-3.766557,3.423827,3.244384,-7.483580,-8.317591,-9.288573,-8.852819,-4.252894,7.417096,6.556406,-3.779366,6.163909,5.105465,2.127523,-5.284570,2.278021,2.685531,6.763118,9.817709,7.984721,-1.317959,-3.223797,7.787808,1.374979,3.205826,9.632520,3.524298,9.642589,-9.500119,-7.083035,-7.442822,2.441588,5.675424,-6.752225,7.065714,-9.385134,0.816562,-9.136053,3.571871,-5.645311,8.844254,0.831415,-0.842884,5.298445,6.901286,7.220037,4.278221,8.656040,1.090252,-7.321479,6.058216,7.063828,5.867354,-2.187814,7.432476,8.845304,-3.245697,5.631599,0.380183,6.157781,4.329415,0.925571,-4.308036,1.088281,-4.278182,-5.071862,-1.495074,5.412232,5.680948,3.116149,-7.203752,5.666031,9.208301,8.858470,7.946470,6.280176,9.474965,-8.623364,2.087560,-0.230252,5.334992,-4.583511,-0.314651,5.030957,3.977455,-6.118738,1.713681,-9.219850,1.091909,-6.479991,9.204059,3.806506,-9.886381,-0.545345,8.835191,9.743086,6.949677,-3.193479,6.020944,3.673091,-2.777321,-1.733188,-2.315592,-4.700697,-6.572322,-7.808540,-2.380407,4.112149,7.967668,7.267282,-6.345418,6.765927,-5.281155,8.711850,0.539105,-6.435815,-2.275436,-8.329272,7.992783,-4.502881,4.405910,5.402090,-8.001411,-7.858485,-6.850856,-7.710660,-9.670578,-8.687458,-2.361660,9.427942,5.208432,6.456464,-0.689510,-9.411181,8.939899,-1.130724,6.582111,-9.821769,-7.236982,-7.609771,-9.131340,0.862643,-8.804439,5.347970,8.929792,9.669960,-7.503939,-2.204814,-2.453968,5.624572,-0.897225,-8.068372,7.801033,7.083646,0.165780,9.368940,6.142663,-8.771652,-5.926365,-3.726914,-7.608583,-2.038242,-1.744050,-1.422945,9.243058,-0.862132,3.466824,-4.081429,-6.440034,-6.561417,1.817610,2.121944,-6.460877,-9.000911,-2.716927,-7.538788,-3.974342,2.392484,1.720814,9.290227,5.979963,-8.979146,-1.118365,-6.022339,0.760792,-1.109570,-2.039709,2.101389,-4.343111,7.947024,-4.778578,6.609901,0.315347,2.872659,-1.708690,3.130936,8.480408,-3.888042,-6.104510,-8.118460,6.943805,-9.497628,-6.213609,-9.492447,-8.158032,9.638982,3.869419,2.211261,-1.470819,-4.372710,-5.815554,-9.126031,9.391296,4.111059,9.954495,5.633673,5.505919,-6.361084,6.158264,-7.602168,8.675886,-9.421084,-8.075760,7.022412,8.005892,-3.270571,5.849051,4.376380,2.851356,3.611530,-1.319604,-8.715601,-6.253262,0.293047,7.772981,5.353078,-2.147635,-9.960239,-8.282116,2.712052,0.342102,5.675882,-6.847126,8.662594,7.006305,9.338918,-6.112430,8.000712,-1.202272,-6.038988,-4.589254,-0.165555,-3.028292,-2.874496,-2.408128,-8.197794,9.440635,4.975911,-2.139445,0.826108,9.092148,2.655169,-3.352535,-9.153637,5.444423,9.293586,1.507353,-5.531658,-0.632248,-5.915768,-0.554662,-4.545461,-8.623476,-2.084846,-6.820939,-7.336604,-9.598120,5.703866,8.481543,7.513578,9.763235,-3.632165,0.596491,-6.099107,6.731249,-7.477663,2.111516,9.079042,-1.342009,-4.579908,-3.484226,-3.877931,-7.114562,8.562684,-9.829695,-0.620813,0.198372,-5.330201,-0.626684,-0.099528,6.827753,2.154960,4.104632,-0.579729,-3.861109,8.961120,7.691956,3.714128,7.061627,4.425408,-1.844333,6.630837,3.364935,-4.663981,-8.940843,8.436809,0.148269,-0.594328,-1.241742,4.781775,7.195899,5.614160,-9.441209,-5.857874,9.161339,5.251348,-5.124932,-1.474223,-9.791317,2.021394,4.434711,-9.511904,3.830771,-2.068674,8.251611,9.598225,-8.350832,-9.195594,0.851867,-9.218729,-2.443328,-9.775144,8.665378,-7.724907,8.794252,-0.259266,4.195678,-7.215666,-5.126794,-4.399804,-5.090560,-8.827181,-7.218700,8.664267,-7.302202,-4.744692,-1.704630,7.283838,4.413800,1.119749,5.499881,-6.997101,8.129482,8.732778,4.763800,0.803129,7.598394,-1.630116,-0.338741,-1.640357,4.572352,-1.622232,9.127753,1.335460,9.310485,-0.834647,7.664373,0.517106,7.298076,-5.546144,-1.880445,-9.473948,5.369950,2.485687,-6.308633,-4.817798,6.496326,9.390515,-5.598461,0.989918,-6.969531,-0.139159,-5.266730,-9.062080,7.756941,-7.096419,-7.483661,8.381775], dtype = "float32")#candidate|12846|(780,)|const|float32
call_12843 = relay.TupleGetItem(func_9968_call(relay.reshape(var_12844.astype('float64'), []), relay.reshape(var_12845.astype('float64'), [135, 10]), relay.reshape(const_12846.astype('float32'), [10, 78]), ), 1)
call_12847 = relay.TupleGetItem(func_9973_call(relay.reshape(var_12844.astype('float64'), []), relay.reshape(var_12845.astype('float64'), [135, 10]), relay.reshape(const_12846.astype('float32'), [10, 78]), ), 1)
func_12549_call = mod.get_global_var('func_12549')
func_12551_call = mutated_mod.get_global_var('func_12551')
const_12851 = relay.const([-0.919872,-2.759823,-1.609631,2.476642,-1.135110,9.058008,1.328804,-9.650729,-0.974596,-3.325099,-6.327818,1.500749,-2.046247,0.566280,-5.792160,5.390046,-7.803647,5.515437,-5.579669,3.977279,4.976441,-8.429383,-1.703590,-4.846879,7.709164,-1.390566,8.890510,-8.326125,-6.672413,4.876188,-1.270176,1.087324,-0.401929,-1.595785,-1.393524,7.465350,-4.396010,-7.911587,3.118197,9.303648,5.630082,-5.644993,2.411924,9.842481,-8.812963,-6.799583,7.030626,5.380082,9.898780,-1.982085,4.967510,2.100320,-7.273182,7.361566,-5.898177,-5.039734,-2.146434,-1.117761,-5.520432,4.533396,5.531371,7.131698,-0.782462,-7.459751,-5.714194,4.400248,0.636144,0.994979,-7.450954,1.943009,5.385563,-2.925798,-1.943788,7.482690,-6.439060,2.628438,4.644559,-3.654836,-6.457376,3.628389,-0.640972,-8.041907,9.926451,4.083809,-8.772596,2.230698,-3.493859,9.703341,-3.509582,6.574843,-9.746081,-6.447526,-8.639237,5.591451,-5.495533,6.414071,2.241851,-9.543936,-2.238108,-6.251388,-0.954376,-3.786055,6.066393,0.475597,5.871395,8.495832,1.980455,4.838946,-0.287249,-0.975871,5.377774,7.431283,-4.664876,7.377482,8.677527,2.069250,6.388732,4.100489,-5.462186,7.913794,0.849166,1.004908,-8.947385,-5.639957,2.220135,2.038128,2.607440,1.318030,-2.217133,-7.552211,-6.483635,7.908636,0.795399,-4.840770,1.870310,9.214493,-0.255157,-7.077010,5.364930,-5.683525,0.935980,2.874225,-1.726913,-5.318537,-7.784987,3.795414,8.896174,-5.284985,5.678936,-5.006509,-4.178590,0.736908,-1.247556,-3.371609,0.862537,-4.550031,-8.199469,9.177895,-9.090346,-5.597545,-8.745798,3.774762,-9.248992,-6.476739,-6.037517,7.425505,2.179981,-5.873000,-6.863826,7.266793,6.163758,-1.549247,-6.423075,-3.382097,-7.832845,0.194725,-6.097409,-9.151577,-9.684443,-4.761018,8.313226,-7.182890,9.353280,-6.246165,3.064493,0.805635,3.357110,-6.428466,6.372739,-4.726792,9.135282,-0.954870,-2.221051,4.215578,8.764159,7.374452,2.425200,4.069672,-7.134824,-6.929898,-5.701846,-5.941425,8.072933,6.596057,-5.146280,-2.705596,0.316421,5.696612,6.121793,-6.263152,2.565609,6.062735,2.601377,9.105521,-1.066035,1.911486,0.749875,-9.933515,4.753377,9.416443,6.265603,7.103786,-2.256560,-5.082645,8.622839,-8.881229,1.790204,7.918266,4.546531,-8.743416,-5.208346,-7.874118,-5.525977,4.217692,-6.200624,7.699827,-0.749683,-0.165226,1.064482,3.747534,1.574191,8.019226,3.607670,-8.156575,0.775664,4.658450,-4.530641,7.017983,-4.200721,-1.304571,4.496800,2.262840,1.018354,-5.244403,-0.520575,2.678804,-5.095903,-1.325579,-8.316192,-6.264719,-3.109692,9.151082,4.301108,1.249638,3.026690,-9.251363,5.012645,6.991506,7.369032,6.731697,3.538321,7.281364,-2.994327,5.748361,-9.210633,-9.297229,9.175047,-4.353467,7.327169,5.344615,1.094668,3.037217,9.955827,9.359408,9.676245,-0.646199,-7.786998,-6.593175,-2.975232,3.573879,8.503359,6.719454,1.220586,6.946810,7.749569,-0.807168,-5.147376,6.137252,-3.272848,-4.863559,7.424119,-6.326066,-5.856414,-6.472292,-6.236407,-6.384289,-5.249907,2.096736,1.205570,-6.582439,5.168952,3.612738,-5.445882,1.101345,-0.902771,-5.694860,-5.331366,2.735492,0.226038,6.858303,2.849812,1.538652,0.140782,1.125065,1.643750,4.976415,-4.521876,-1.609776,8.902781,1.553227,9.164235,-9.531661,-7.513109,6.318119,1.729566,-9.960411,-2.336614,-3.069318,-0.148411,-0.732072,1.086523,-0.511965,-8.101113,6.925127,-2.585819,1.674597,-1.113477,2.808925,9.213512,9.900115,-3.900830,6.383511,1.981695,-9.229306,-0.939436,-9.995770,5.240095,0.917787,5.274363,4.525081,-6.100296,-7.942621,-2.147067,9.648948,-1.516141,9.445041,-7.969602,4.869963,-1.647684,6.520390,-7.139523,0.468453,-3.827650,2.374008,4.312692,7.562122,-4.153372,-9.373243,-7.820468,-5.425440,-3.654840,2.336060,6.100482,8.542348,-2.026182,-1.211295,-3.145100,-3.384102,-1.188086,-6.618326,3.553384,1.244826,9.946340,-0.055340,-8.502443,-1.085866,-7.257079,6.017355,-9.753940,-1.179286,-9.999643,6.595842,-6.378560,8.169531,-9.849373,-1.277060,-1.943754,8.935958,3.879604,8.549828,-2.920457,4.192509,8.755737,-8.207588,6.760825,-4.957903,1.294780,-8.616149,-5.158297,9.136680,0.359860,-2.044523,7.934214,-7.237698,9.015651,-2.297106,1.149029,1.177401,7.840307,3.104559,-8.822327,-0.910223,4.235661,8.151711,-7.682937,-9.134297,-5.934441,2.297365,-8.515765,-6.636088,5.941589,-3.910425,-2.403690,2.621626,8.448970,-3.986616,3.662860,-7.847628,1.508357,-1.229960,-9.681040,-7.803551,0.661528,-7.581159,2.174757,0.073168,-7.692586,2.169529,6.630293,-6.823683,8.244611,-4.572564,8.368605,-1.093958,-0.932409,-5.009099,6.356199,8.846337,2.268025,3.548318,5.113100,6.140489,-5.978538,-5.863463,-7.438544,-0.796972,-6.559223,-2.208244,4.863083,-1.743973,8.574132,-3.728953,8.463113,3.242104,-1.530155,7.657752,3.197330,1.200551,-5.809684,-6.173859,-7.696286,-3.972663,9.568967,-8.599745,8.767105,5.247236,9.380485,-9.709432,4.038620,9.402064,-1.699961,0.143642,-9.624241,1.012884,1.804455,6.765372,-7.705514,-5.737585,-7.156835,8.377461,1.479919,-6.905343,-1.544916,-8.221144,-9.364860,6.077708,-0.318383,-3.907692,5.662384,1.324635,5.170704,-0.779901,8.640168,-5.592498,3.328204,5.528266,-6.611264,-5.970789,-4.743610,-0.586130,-1.080565,5.562614,0.044131,1.460314,5.928402,4.969910,2.961887,7.792993,-9.150949,-5.649787,0.905454,-1.643834,2.534532,-4.131018,7.832918,-4.649086,6.183751,3.250051,-3.159169,9.220461,5.074768,-5.179637,4.607500,5.484384,1.223070,4.486144,-2.765692,-4.390422,-7.187179,3.826123,-3.606761,-7.435394,-8.523615,-9.362339,-9.273398,-7.159357,-6.699966,9.189298,-2.286421,7.806252,-3.480140,-2.936522,-9.195669,4.288357,-2.873028,5.341400,-3.783834,-5.541489,5.622165,7.974677,-3.560278,9.662691,2.050314,-2.027073,-5.303839,9.069037,1.314929,9.639745,9.354534,-6.983640,2.973589,-8.249558,5.298907,-4.258379,2.349901,1.757129,-8.013871,-5.119544,5.654382,6.997432,-5.450194,-2.894811,5.874898,8.723583,-7.803767,-7.300759,0.812278,-9.401031,6.576247,1.112033,-5.353311,-5.490768,-0.010816,-0.024248,-5.942528,9.866607,1.937578,-2.573508,9.107980,4.730289,8.701032,8.770945,-9.887219,-6.811889,6.186023,-7.784197,-8.183988,-3.531343,6.778627,-1.885770,-8.513176,-7.023700,7.431129,-7.582753,-4.656916,9.354577,0.492933,9.766554,-7.674802,7.527788,3.840427,7.485315,2.495168,-4.669060,5.066544,-2.056728,-3.175858,1.634750,8.300201,-2.637804,8.997047,5.355267,2.942214,-2.127009,-1.421206,7.653786,4.239690,6.335966,-1.230453,7.596454,-6.977193,6.679255,-1.822482,8.733063,1.463787,9.927910,3.804461,0.881973,1.086449,-3.669018,-7.681396,-3.563137,-1.868899,-7.097930,5.273891,-6.646355,3.015203,0.852813,-3.934260,3.676650,-9.675124,-8.966312,9.838820,-6.358820,9.443639,5.688804,-9.825752,4.439490,3.749860,7.527515,4.368311,0.064751,-2.230857,-3.771922,2.048469,-9.456958,9.950488,2.053713,-7.258277,7.939410,-0.481537,6.858534,-6.062220,2.145707,-0.992395,8.537443,4.735319,-1.771164,4.610889,-3.080251,-6.252394,-2.277705,-5.356027,1.723738,-2.268125,-8.692237,5.733479,6.194182,1.443213,9.591919,-7.473172,8.079144,9.221595,7.982643,3.418058,4.621782,-8.814161,1.153473,4.757429,3.747207,9.555335,-7.003940,-3.538807,5.041763,8.708456,4.512296,2.405369,3.439626,0.612750,5.008025,-9.235645,-6.365657,-2.550656,7.334147,-2.352410,0.246768,2.738664,-5.088794,-5.145538,3.385417,2.226149,3.006175,0.695726,6.848150,7.229124,1.169229,-7.113412,-3.707686,5.131045,-6.223546,-6.551053,-8.847632,-0.094668,5.985058,-9.521690,-1.383746,-2.743834,-5.026586,-9.451391,-3.591824,-4.968312,4.253116,2.082107,3.537476,-6.750283,0.165896,-2.020709,-2.945370,-9.269262,6.959188,-5.123622,-9.282443,6.268284,-8.374412,5.235028,4.194196,3.808341,-7.703087,-1.186523,8.226217,1.670321,2.255078,-9.673517,-5.174915,-4.762135,4.223951,6.405656,5.439098,-6.321666,-1.913092,-2.964904,6.841654,7.397548,-4.715056,-8.269817,-1.750735,-6.547381,8.888129,7.323357,-2.004258,3.919010,-3.380429,0.148173,6.492676,1.388478,0.410701,5.768405,5.322148,-5.190377,-1.311714,-7.873793,9.618034,-2.662934,2.793509,-1.680659,9.436820,-7.970628,9.065894,6.204397,8.659054,-4.760483,-2.470598,-4.699489,-9.163565,-4.705676,5.355172,1.544546,5.226725,0.709192,9.295443,-5.354660,4.132467,-2.628766,8.494812,3.898134,4.490254,6.399952,8.387974,0.172132,5.405995,-3.166099,-9.582502,9.725279,8.970426,3.088001,-9.793905,-9.461994,-8.435599,-6.050867,-9.103128,-6.775038,-1.475596,-1.748877,4.141243,9.656313,5.077244,1.426566,-1.077922,0.276132,9.700773,-8.960370,4.430444,5.051904,-4.810565,3.865921,3.265631,-2.049679,8.806766,8.695675,-3.556060,1.382024,-7.057316,-9.150463,3.893231,9.161039,-1.312777,6.677166,-9.218584,6.379124,-2.956248,3.801123,-7.787957,5.820680,-0.658444,4.103278,-3.900465,-5.176970,6.245946,8.731099,8.416543,-6.376693,-8.032191,5.405407,-5.726209,7.957483,9.693248,4.215108,-2.570024,9.144943,6.291438,-5.215153,-8.957597,1.539103,2.085636,-8.369745,5.881900,-4.065504,-7.049304,-2.775828,-0.662669,-6.702968,-9.773681,0.617438,-0.369040,-3.206510,6.574575,1.095759,9.214765,-2.347092,0.368715,5.599913,3.338250,6.350953,5.071922,-1.670964,5.853747,0.340237,-1.929849,4.495816,-7.162635,0.098652,-9.156095,9.612293,4.131334,-8.526081,-7.722724,1.718465,9.444419,-2.645465,-2.798946,-4.527269,7.510433,7.013456,-6.203849,-1.168372,-7.571743,7.829745,6.709022,0.260288,-9.616064,3.700741,9.581176,-1.908153,4.679344,-7.039820,8.070962,-8.905212,-2.395643,8.288439,-0.565322,1.440591,9.761024,1.414933,4.066526,1.948178,-5.454938,5.079631,0.822374,-8.698229,-5.648721,-5.946248,3.869634,-5.194495,-9.280075,-7.304408,7.439310,-0.573622,-4.517259,2.642713,-5.659553,1.936503,-2.797664,-1.930668,-2.948713,-1.709363,1.756489,9.905468,4.223301,3.470582,3.619952,-6.062954,0.869322,5.456347,-2.101535,-1.206647,6.410629,7.158109,-7.703999,0.404278,-6.101331,8.694392,-0.869998,-2.151270,-9.999090,1.949967,-4.700530,-9.473874,-7.110251,5.011701,9.185171,2.316899,-4.109791,-4.740936,7.498901,5.165277,9.135611,2.420851,3.332380,-8.999666,2.650362,5.451765,1.624278,-4.219496,3.092005,5.986863,6.073549,4.273995,5.327428,-8.415983,6.313367,1.979516,-6.428522,-4.467895,-0.727612,0.961074,5.160623,0.742112,-0.068816,-9.178323,-8.884302,-4.083427,3.002364,7.177168,3.327201,5.541018,0.888322,-6.068307,5.254940,-3.597179,1.693751,-9.221284,-7.808039,2.124116,7.216171,9.951496,0.651272,1.070905,6.658770,-8.365127,-2.957729,-4.115780,-9.506899,4.307670,7.176963,0.263166,7.190925,3.129962,-8.096179,-0.362765,3.072191,6.711724,-9.238162,4.128500,1.593156,-8.294197,0.813794,1.341450,2.439521,6.650171,-5.660038,3.687547,-1.666068,-6.467475,-7.879076,-9.177802,-3.834158,-8.927461,-5.260515,-9.567045,1.090130,3.570156,1.403054,-2.844955,0.575820,-3.324282,5.564613,9.681766,-0.740516,-8.386780,9.856753,-6.642239,-8.827592,-1.092465,-6.771503,-8.091878,0.238604,-2.514804,-7.960068,-9.509496,2.345062,-0.680599,-6.057548,-5.679103,3.751729,2.358706,-1.884345,-4.312232,7.825204,6.296255,4.895192,4.664112,-1.959036,-9.471230,2.184468,-4.795486,7.923065,8.080020,3.223807,-9.673019,-9.052469,3.468058,-2.526600,0.047961,-3.397239,6.703749,-6.860703,-0.338303,9.258011,7.495712,6.326727,8.571035,-6.494526,9.582488,-9.311461,-4.917210,4.380169,4.782200,0.153678,5.063686,-9.900538,-8.736129,-1.185361,3.775121,1.607334,-4.548011,-9.721710,3.603851,-1.471811,-8.599800,-4.345186,2.690358,-2.083409,2.776052,6.933319,0.508862,-8.483736,-2.395660,5.959375,-7.034799,-4.799643,5.312837,-0.797933,-3.359130,0.444355,4.629018,4.054649,-0.456425,-1.548445,-2.732697,-2.652929,5.062470,2.663129,0.721301,2.262662,0.610208,-4.153413,-6.845337,9.508451,0.582697,-1.631956,-7.710087,3.916128,9.126485,6.841521,4.498672,-1.493569,-8.916469,-2.479156,-7.545603,7.043547,-9.473919,-1.747916,-7.990981,6.652947,3.334029,-3.230642,2.894169,-0.862861,3.778395,-4.605732,8.428803,6.048468,-2.401429,-6.081755,4.547755,-6.432578,9.236218,3.706441,-0.306520,-8.654378,-7.470750,-7.803109,-5.665691,-0.290304,-2.791130,0.413262,4.655416,5.884482,-2.422750,-2.019681,8.417910,4.522683,-4.049481,-3.579958,5.082487,-8.756106,0.126129,-6.037686,1.939555,-6.429415,7.500518,7.906569,-0.240527,4.770264,-1.479212,8.369166,-7.674195,3.008612,1.328066,-5.428789,-7.300104,-9.157477,0.129890,4.099881,9.225896,-9.050564,2.823703,-1.113819,-7.409916,8.178261,8.477551,-1.379562,1.471085,-0.486791,8.344464,-2.635609,9.564376,0.780593,6.011387,3.398780,-7.951107,5.282538,-2.103550,-8.270746,9.843798,4.825846,-1.137666,9.561461,5.071226,-5.462026,-0.657053,-2.383047,6.547663,-8.356356,6.603217,7.437799,2.641726,6.890781,-3.921594,-9.629066,5.292854,5.545916,8.252913,-4.505994,-0.693072,0.801075,5.634032,0.795577,5.890804,0.507435,2.134036,2.907589,4.136601,-0.889798,-6.987953,-8.840435,1.352968,8.256641,-0.813034,6.521506,-5.847778,8.785836,1.278378,-1.825528,-7.547882,5.404259,-5.808951,-0.859306,6.204082,-5.904833,8.525851,-1.882413,-7.863830,6.956420,9.952640,6.830145,5.447202,0.928003,6.171611,3.992408,8.867546,-8.570748,8.844497,6.864192,2.482705,-3.200111,-9.697196,2.094214,-6.825887,8.194447,-4.786854,2.159689,9.462020,-1.468457,-1.630601,-4.771406,-1.590197,-6.813004,0.567486,-8.279562,3.310717,4.284706,3.641655,-0.432066,9.392084,6.147244,-3.402706,4.660554,8.422605,6.321439,-0.913022,8.830640,-2.041592,-4.796836,-0.656002,-7.103391,-7.843820,7.007762,3.052812,3.320154,-5.391222,-0.957791,-9.113770,-4.250302,5.345016,4.553704,-9.097270,-1.473303,-8.986717,-8.164474,4.668466,-3.501023,7.615599,-0.555802,7.900309,5.183983,-3.528335,9.962025,-6.473885,9.366772,3.929630,5.118870,0.254899,-0.842937,-8.964153,-3.642480,4.219137,4.503490,1.240266,6.332068,-7.681192,-7.198242,-0.025508,5.210460,9.910546,-1.898302,0.591544,-6.349452,2.806842,6.952798,-7.185894,-8.412725,-8.197664,-7.553378,5.121574,4.183368,-1.263005,-4.589063,9.499786,8.397942,-8.114117,4.883628,2.641824,1.128733,-4.887046,9.346530,-0.144810,-7.222216,9.474631,-8.341825,6.916457,-9.081822,2.302966,-7.864709,-4.381616,-4.324943,-7.564395,2.706003,5.377420,-0.073984,0.823553,-2.091557,9.397683,-0.929855,1.132005,0.117112,-4.706875,0.651367,3.962104,-6.782648,4.355729,-0.129610,-5.326327,-7.547618,-1.615833,0.669053,-6.488785,-6.298237,3.794955,-1.289730,6.817008,8.307574,-9.760658,-0.066365,-5.269755,0.778427,9.848535,0.855831,2.331536,8.588210,5.980334,8.477709,1.842132,9.137879,9.810608,0.498335,-5.811698,-4.379183,1.600688,-3.260683,-7.139273,-7.710890,5.788298,7.027155,1.025846,6.120831,-9.405299,-2.367173,-5.650240,-5.482485,1.376951,-8.131669,-4.446326,-1.187856,1.123866,4.897745,6.395428,5.963481,-6.311678,0.174294,-8.739147,-0.558777,-8.013701,-2.624251,-5.341017,-5.662120,-1.910181,9.513335,6.656483,3.949204,-8.162724,-8.099245,-1.405564,5.216590,4.713619,-8.441987,5.561925,-8.438608,5.200145,-9.977674,8.382706,3.053706,3.751120,-0.469871,0.234533,-0.947546,-5.132945,1.627724,-2.411031,7.630143,5.540161,6.948916,-6.213990,-5.844987,-7.274303,-4.242827,4.342105,-9.114349,-3.342042,-9.206044,-9.601445,-8.911765,5.777585,3.188757,-6.749736,9.945902,-1.535113,-8.455950,-7.678885,-3.909166,5.022034,-7.099648,-2.704757,9.853361,9.077520,-0.672232,-4.362058,0.978670,-0.703882,-9.526599,6.244544,5.986947,-0.458560,3.088305,-1.550543,-6.098277,-4.577605,6.419985,8.302221,2.479648,-8.840832,-2.579008,-6.105382,-2.646907,-4.874748,1.935094,4.956323,6.239751,-9.724912,-0.762197,-3.207698,-6.519441,-9.859127,2.196541,8.390822,-9.095413,9.062387,-4.477134,-4.520078,-0.183760,6.656406,3.924358,-6.102658,8.310730,6.711847,-6.386596,-2.693106,-9.636199,-3.682351,-5.483979,-7.844982,6.629236,2.244114,-5.122049,-8.139377,-8.871227,-3.973529,-7.232964,-3.619916,-1.517249,-8.387090,6.406107,7.188571,4.936800,0.177829,8.654033,-8.804028,9.210175,6.515996,-0.695765,9.016686,0.933230,-1.514535,-4.350999,1.242551,-4.662832,8.316179,-0.163879,0.270326,-1.553273,0.570902,-1.608333,-3.326603,5.998189,4.477462,-9.913713,-5.312805,0.764711,0.269124,6.496351,-5.490366,-2.730180,4.228627,-5.179531,-8.203322,-4.515678,3.798191,-7.921935,-3.020895,3.157657,6.850961,-1.141784,5.011412,-4.309811,-5.396876,-7.173322,6.931750,-0.350341,7.308857,3.091674,-6.186546,-9.027639,-5.750943,1.583212,-5.793547,2.266213,-5.764491,-8.760579,6.151337,4.646663,-6.001398,-3.256812,-8.802142,8.264677,1.524703,-6.669056,-1.289061,2.074519,3.812399,4.095213,7.362526,3.251112,9.306706,-9.738764,-7.688669,-6.071878,2.069576,-9.827463,2.905084,6.143378,-7.053649,-7.602379,-7.883362,2.311829,8.726422,-2.735732,0.520732,-1.693267,8.353426,2.193729,-2.892813,-2.785347,-8.096628,-4.982685,-6.781766,3.007082,2.424723,8.505452,3.560984,2.743471,-8.168909,-2.653309,0.911783,-1.721178,3.345877,-3.454393,3.045653,7.635398,8.895763,0.046117,4.014196,-6.711818,2.360204,7.240265,-4.810950,2.375590,-0.952607,1.541650,-2.663403,-7.844647,7.465274,-5.810733,1.389103,7.010036,3.859120,3.565705,8.131896,9.455491,1.385808,1.528841,7.822886,-1.973789,-0.394716,6.849011,8.540095,-6.490683,-4.724323,0.588023,-1.136622,-7.454752,-6.400242,7.899740,7.845774,-7.924217,4.652892,-4.384355,-3.172494,-4.390923,-4.115337,0.148146,9.530265,9.968640,-7.193451,0.678157,0.327620,-2.240943,9.428385,7.108017,-8.610469,-0.427152,7.548433,-1.778459,0.542669,5.726009,-1.234523,-6.987101,-3.014985,6.707156,-7.105532,-3.805536,-2.244922,9.045891,-9.767832,-4.535663,-0.986279,-9.291506,-5.803660,9.830976,8.920293,0.875843,-8.448340,4.536242,4.914369,2.109575,5.971751,1.779848,3.709581,-6.505095,7.982495,-0.821901,6.805420,-7.361993,-8.828241,5.427819,-2.963438], dtype = "float64")#candidate|12851|(1815,)|const|float64
call_12850 = relay.TupleGetItem(func_12549_call(relay.reshape(const_12851.astype('float64'), [1815,])), 0)
call_12852 = relay.TupleGetItem(func_12551_call(relay.reshape(const_12851.astype('float64'), [1815,])), 0)
func_7521_call = mod.get_global_var('func_7521')
func_7525_call = mutated_mod.get_global_var('func_7525')
call_12857 = relay.TupleGetItem(func_7521_call(relay.reshape(call_12799.astype('float32'), [3, 11, 2]), relay.reshape(var_12845.astype('float64'), [1350,]), ), 0)
call_12858 = relay.TupleGetItem(func_7525_call(relay.reshape(call_12799.astype('float32'), [3, 11, 2]), relay.reshape(var_12845.astype('float64'), [1350,]), ), 0)
output = relay.Tuple([call_12799,call_12843,var_12844,var_12845,const_12846,call_12850,const_12851,call_12857,])
output2 = relay.Tuple([call_12800,call_12847,var_12844,var_12845,const_12846,call_12852,const_12851,call_12858,])
func_12864 = relay.Function([var_12844,var_12845,], output)
mod['func_12864'] = func_12864
mod = relay.transform.InferType()(mod)
var_12865 = relay.var("var_12865", dtype = "float64", shape = ())#candidate|12865|()|var|float64
var_12866 = relay.var("var_12866", dtype = "float64", shape = (1350,))#candidate|12866|(1350,)|var|float64
output = func_12864(var_12865,var_12866,)
func_12867 = relay.Function([var_12865,var_12866,], output)
mutated_mod['func_12867'] = func_12867
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12893 = relay.const([[[True,True,False,True,False,False,False,True,True,False,True,False,False,False],[True,True,False,True,True,False,False,True,False,False,True,True,False,False],[True,True,True,True,False,True,False,False,True,False,True,False,True,True]],[[True,True,True,False,False,False,True,False,False,False,True,False,False,False],[True,False,True,False,False,False,True,False,True,True,True,False,False,False],[False,True,True,True,False,True,True,False,True,True,False,True,True,False]],[[True,True,False,False,False,True,False,False,True,False,False,False,True,True],[False,True,False,True,False,True,False,False,False,False,True,True,True,True],[False,False,True,True,True,False,True,True,True,False,True,True,False,False]],[[True,True,True,False,True,True,True,True,True,True,False,True,True,True],[True,False,False,True,False,False,True,False,False,False,True,True,False,True],[False,False,True,False,False,False,False,True,False,True,False,True,False,False]],[[False,False,True,True,False,False,True,True,False,False,True,False,False,False],[True,True,True,False,True,False,False,True,True,False,False,True,True,True],[False,True,True,False,True,True,False,False,True,True,True,True,True,False]],[[True,True,False,False,False,False,False,False,False,False,True,True,False,False],[False,True,True,False,True,False,True,False,True,True,False,False,False,True],[True,True,True,False,False,False,True,True,False,True,True,False,False,False]]], dtype = "bool")#candidate|12893|(6, 3, 14)|const|bool
const_12894 = relay.const([[[False,False,False,False,True,True,True,False,False,True,True,True,False,False],[True,True,True,False,True,False,False,True,True,True,True,False,False,True],[False,True,True,True,True,False,True,True,True,False,True,True,True,False]],[[False,True,False,True,True,False,True,False,False,True,True,True,True,False],[True,True,True,False,False,True,True,False,True,False,True,False,False,False],[True,True,False,True,True,True,False,False,True,True,False,True,False,True]],[[False,True,True,True,True,False,True,True,True,False,True,False,False,False],[False,False,False,True,False,True,False,True,False,False,True,True,True,True],[False,False,False,False,True,True,True,False,True,True,False,True,True,True]],[[True,False,False,False,False,False,True,False,True,False,True,True,False,False],[False,False,True,False,False,True,False,True,False,False,False,False,True,False],[True,False,True,False,False,True,False,True,False,False,True,True,False,True]],[[True,False,True,True,False,True,False,False,False,False,False,True,False,False],[True,True,False,False,False,True,False,False,True,True,True,True,True,True],[False,True,False,True,True,True,True,False,False,True,False,True,True,False]],[[False,False,False,True,True,False,True,True,False,True,False,True,False,True],[False,True,False,False,False,False,False,False,False,True,False,False,False,False],[True,True,True,True,True,True,False,True,False,True,False,False,True,False]]], dtype = "bool")#candidate|12894|(6, 3, 14)|const|bool
bop_12895 = relay.logical_or(const_12893.astype('bool'), relay.reshape(const_12894.astype('bool'), relay.shape_of(const_12893))) # shape=(6, 3, 14)
output = relay.Tuple([bop_12895,])
output2 = relay.Tuple([bop_12895,])
func_12900 = relay.Function([], output)
mod['func_12900'] = func_12900
mod = relay.transform.InferType()(mod)
output = func_12900()
func_12901 = relay.Function([], output)
mutated_mod['func_12901'] = func_12901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11328_call = mod.get_global_var('func_11328')
func_11330_call = mutated_mod.get_global_var('func_11330')
call_12907 = relay.TupleGetItem(func_11328_call(), 2)
call_12908 = relay.TupleGetItem(func_11330_call(), 2)
func_8870_call = mod.get_global_var('func_8870')
func_8872_call = mutated_mod.get_global_var('func_8872')
call_12930 = func_8870_call()
call_12931 = func_8870_call()
output = relay.Tuple([call_12907,call_12930,])
output2 = relay.Tuple([call_12908,call_12931,])
func_12949 = relay.Function([], output)
mod['func_12949'] = func_12949
mod = relay.transform.InferType()(mod)
output = func_12949()
func_12950 = relay.Function([], output)
mutated_mod['func_12950'] = func_12950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7290_call = mod.get_global_var('func_7290')
func_7292_call = mutated_mod.get_global_var('func_7292')
call_13003 = func_7290_call()
call_13004 = func_7290_call()
output = call_13003
output2 = call_13004
func_13016 = relay.Function([], output)
mod['func_13016'] = func_13016
mod = relay.transform.InferType()(mod)
mutated_mod['func_13016'] = func_13016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13016_call = mutated_mod.get_global_var('func_13016')
call_13017 = func_13016_call()
output = call_13017
func_13018 = relay.Function([], output)
mutated_mod['func_13018'] = func_13018
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13095 = relay.var("var_13095", dtype = "float32", shape = (15, 16, 6))#candidate|13095|(15, 16, 6)|var|float32
uop_13096 = relay.log(var_13095.astype('float32')) # shape=(15, 16, 6)
func_7403_call = mod.get_global_var('func_7403')
func_7405_call = mutated_mod.get_global_var('func_7405')
var_13100 = relay.var("var_13100", dtype = "float32", shape = (11, 6))#candidate|13100|(11, 6)|var|float32
call_13099 = func_7403_call(relay.reshape(var_13100.astype('float32'), [3, 11, 2]))
call_13101 = func_7403_call(relay.reshape(var_13100.astype('float32'), [3, 11, 2]))
func_7521_call = mod.get_global_var('func_7521')
func_7525_call = mutated_mod.get_global_var('func_7525')
var_13105 = relay.var("var_13105", dtype = "float64", shape = (1350,))#candidate|13105|(1350,)|var|float64
call_13104 = relay.TupleGetItem(func_7521_call(relay.reshape(var_13100.astype('float32'), [3, 11, 2]), relay.reshape(var_13105.astype('float64'), [1350,]), ), 0)
call_13106 = relay.TupleGetItem(func_7525_call(relay.reshape(var_13100.astype('float32'), [3, 11, 2]), relay.reshape(var_13105.astype('float64'), [1350,]), ), 0)
output = relay.Tuple([uop_13096,call_13099,var_13100,call_13104,var_13105,])
output2 = relay.Tuple([uop_13096,call_13101,var_13100,call_13106,var_13105,])
func_13114 = relay.Function([var_13095,var_13100,var_13105,], output)
mod['func_13114'] = func_13114
mod = relay.transform.InferType()(mod)
var_13115 = relay.var("var_13115", dtype = "float32", shape = (15, 16, 6))#candidate|13115|(15, 16, 6)|var|float32
var_13116 = relay.var("var_13116", dtype = "float32", shape = (11, 6))#candidate|13116|(11, 6)|var|float32
var_13117 = relay.var("var_13117", dtype = "float64", shape = (1350,))#candidate|13117|(1350,)|var|float64
output = func_13114(var_13115,var_13116,var_13117,)
func_13118 = relay.Function([var_13115,var_13116,var_13117,], output)
mutated_mod['func_13118'] = func_13118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11419_call = mod.get_global_var('func_11419')
func_11420_call = mutated_mod.get_global_var('func_11420')
call_13144 = relay.TupleGetItem(func_11419_call(), 0)
call_13145 = relay.TupleGetItem(func_11420_call(), 0)
output = relay.Tuple([call_13144,])
output2 = relay.Tuple([call_13145,])
func_13171 = relay.Function([], output)
mod['func_13171'] = func_13171
mod = relay.transform.InferType()(mod)
mutated_mod['func_13171'] = func_13171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13171_call = mutated_mod.get_global_var('func_13171')
call_13172 = func_13171_call()
output = call_13172
func_13173 = relay.Function([], output)
mutated_mod['func_13173'] = func_13173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12680_call = mod.get_global_var('func_12680')
func_12681_call = mutated_mod.get_global_var('func_12681')
call_13206 = func_12680_call()
call_13207 = func_12680_call()
func_11738_call = mod.get_global_var('func_11738')
func_11739_call = mutated_mod.get_global_var('func_11739')
call_13219 = func_11738_call()
call_13220 = func_11738_call()
output = relay.Tuple([call_13206,call_13219,])
output2 = relay.Tuple([call_13207,call_13220,])
func_13236 = relay.Function([], output)
mod['func_13236'] = func_13236
mod = relay.transform.InferType()(mod)
output = func_13236()
func_13237 = relay.Function([], output)
mutated_mod['func_13237'] = func_13237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10632_call = mod.get_global_var('func_10632')
func_10634_call = mutated_mod.get_global_var('func_10634')
call_13254 = func_10632_call()
call_13255 = func_10632_call()
output = relay.Tuple([call_13254,])
output2 = relay.Tuple([call_13255,])
func_13300 = relay.Function([], output)
mod['func_13300'] = func_13300
mod = relay.transform.InferType()(mod)
mutated_mod['func_13300'] = func_13300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13300_call = mutated_mod.get_global_var('func_13300')
call_13301 = func_13300_call()
output = call_13301
func_13302 = relay.Function([], output)
mutated_mod['func_13302'] = func_13302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8283_call = mod.get_global_var('func_8283')
func_8284_call = mutated_mod.get_global_var('func_8284')
call_13321 = relay.TupleGetItem(func_8283_call(), 2)
call_13322 = relay.TupleGetItem(func_8284_call(), 2)
func_1177_call = mod.get_global_var('func_1177')
func_1180_call = mutated_mod.get_global_var('func_1180')
const_13359 = relay.const([True,False,True,True,True,False,True,True,True,True,False,False,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,True,True,False,False,False,True,False,False,False,False,True,True,True,True,False,False,True,True,False,True,False], dtype = "bool")#candidate|13359|(48,)|const|bool
var_13360 = relay.var("var_13360", dtype = "bool", shape = (4, 120))#candidate|13360|(4, 120)|var|bool
call_13358 = func_1177_call(relay.reshape(const_13359.astype('bool'), [6, 1, 8]), relay.reshape(var_13360.astype('bool'), [6, 10, 8]), )
call_13361 = func_1177_call(relay.reshape(const_13359.astype('bool'), [6, 1, 8]), relay.reshape(var_13360.astype('bool'), [6, 10, 8]), )
output = relay.Tuple([call_13321,call_13358,const_13359,var_13360,])
output2 = relay.Tuple([call_13322,call_13361,const_13359,var_13360,])
func_13364 = relay.Function([var_13360,], output)
mod['func_13364'] = func_13364
mod = relay.transform.InferType()(mod)
var_13365 = relay.var("var_13365", dtype = "bool", shape = (4, 120))#candidate|13365|(4, 120)|var|bool
output = func_13364(var_13365)
func_13366 = relay.Function([var_13365], output)
mutated_mod['func_13366'] = func_13366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11053_call = mod.get_global_var('func_11053')
func_11054_call = mutated_mod.get_global_var('func_11054')
call_13405 = func_11053_call()
call_13406 = func_11053_call()
func_13364_call = mod.get_global_var('func_13364')
func_13366_call = mutated_mod.get_global_var('func_13366')
const_13413 = relay.const([False,True,False,True,True,True,True,True,True,False,True,True,True,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,False,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,True,False,False,True,False,True,False,False,True,False,False,False,True,False,True,True,True,True,True,False,False,True,False,False,False,True,False,False,True,True,True,False,True,False,True,True,True,True,True,True,True,False,True,True,False,True,False,False,False,True,False,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,False,False,False,True,True,False,True,True,True,False,False,True,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,False,False,False,False,False,False,False,False,False,False,True,True,True,True,True,True,True,True,False,True,True,True,True,False,False,True,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,True,False,False,False,True,False,True,False,True,True,True,False,False,True,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,True,False,False,True,False,True,True,False,True,False,False,False,False,False,True,True,False,False,True,True,False,True,False,True,False,False,False,False,True,False,False,False,True,False,False,True,True,True,True,True,True,False,True,True,False,False,False,False,False,True,True,False,True,True,True,True,False,True,True,True,False,True,True,True,False,True,False,True,False,True,False,False,True,True,True,True,True,False,True,True,True,True,True,False,False,False,True,False,False,False,True,False,False,True,True,False,False,True,True,True,False,False,True,False,True,False,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,True,False,False,False,False,True,True,False,False,True,True,False,False,False,True,True,True,True,True,True,True,False,True,True,True,False,False,True,False,False,True,False,True,True,False,True,False,True,True,False,False,False,False,True,True,True,False,False,False,False,True,False,False,False,True,True,False,True,False,True,False,True,True,True,False,True,False,False,True,True,False,True,True,True,False,False,False,True,False,True,True,True,True,True,False,False,False,False,False,False,True,False,False,False,True,False,False,True,True,True,False,True,False,True,False,True,False,True,False,False,False,True,False,True,False,False,True,False,False,True,False,False,True,False], dtype = "bool")#candidate|13413|(480,)|const|bool
call_13412 = relay.TupleGetItem(func_13364_call(relay.reshape(const_13413.astype('bool'), [4, 120])), 1)
call_13414 = relay.TupleGetItem(func_13366_call(relay.reshape(const_13413.astype('bool'), [4, 120])), 1)
func_6131_call = mod.get_global_var('func_6131')
func_6140_call = mutated_mod.get_global_var('func_6140')
const_13433 = relay.const([False,True,False,False,False,False,False,True,True,True,True,False,True,True,False,False,True,False,True,True,False,False,False,True,False,False,True,True,True,True,False,False,False,False,False,False,False,False,True,True,False,True,True,True,False,False,False,False,False,True,True,False,False,True,True,False,True,False,True,True,True,True,True,False,True,True,False,True,False,False,True,False,True,False,True,True,False,True,True,True,True,False,True,True,True,True,True,True,True,False,False,True,True,True,True,False,False,True,True,False,True,False,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,False,False,False,False,False,True,True,True,False,True,False,False,True,False,True,True,True,False,False,True,False,False,False,True,False,True,True,False,False,True,True,True,True,False,True,False,True,True,True,False,False,True,False,True,False,True,True,True,True,True,False,True,True,False,True,False,True,False,False,False,True,False,True,True,False,False,True,True,True,False,True,False,False,True,True,False,True,False,True,False,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,False,False,True,True,False,True,True,False,True,False,True,True,True,False,False,False,False,True,False,True,True,True,True,False,False,True,True,True,True,True,True,True,True,False,False,True,False,True,True,True,False,True,True,True,True,True,True,True,True,True,False,False,False,True,False,True,False,True,False,True,False,False,False,True,False,True,True,False,False,False,False,False,True,True,False,False,False,True,True,True,True,False,True,True,True,True,False,False,False,True,True,False,True,False,False,True,True,True,False,True,True,False,False], dtype = "bool")#candidate|13433|(315,)|const|bool
var_13434 = relay.var("var_13434", dtype = "float32", shape = (780,))#candidate|13434|(780,)|var|float32
var_13435 = relay.var("var_13435", dtype = "float64", shape = (18,))#candidate|13435|(18,)|var|float64
var_13436 = relay.var("var_13436", dtype = "float64", shape = ())#candidate|13436|()|var|float64
var_13437 = relay.var("var_13437", dtype = "float64", shape = (1280,))#candidate|13437|(1280,)|var|float64
const_13438 = relay.const([6.633785,7.359218,2.770235,5.535618,6.971584,3.417520,7.212737,-6.948167,3.608028,-9.839567,6.136010,7.572493,-8.510633,3.275640,-1.155166,5.668756,4.831553,5.612992,-3.521968,6.196297,4.303292,0.376466,-8.999267,6.885717,8.962429,8.911412,0.705469,-0.907095,-2.106392,1.112687,1.445926,4.065110,9.014504,5.073269,2.284575,-9.299812,-0.231565,4.654666,1.876331,-6.348238,-9.093549,-8.902859,-5.492826,2.467475,-3.405332,4.759534,7.388946,-0.574354,0.501622,5.190840,-5.684584,-2.462988,9.844865,7.887839,-1.432094,9.972101,9.711976,-0.017305,-6.847777,0.641798,5.651519,-4.404940,2.856734,5.445245,6.913798,9.098736,-9.228521,-9.750544,4.918170,2.632848,1.738442,7.452375,-6.267098,-6.149811,1.173767,0.748840,-5.597812,-2.074850,-2.341524,-3.939501,-9.089226,5.712040,9.630450,-7.915329,5.727435,5.470943,0.589477,7.817347,-6.184165,-8.793728,4.174236,-4.835913,-4.076909,9.878150,7.435069,-2.904141,8.903985,-0.397940,5.584390,-5.643482,-5.041474,9.438881,-5.636880,5.466572,-1.816197,-2.829728,6.371596,1.187694,2.225344,-3.917060,-3.038161,-1.756207,-9.307567,0.280080,-3.309356,-1.475995,1.159223,-3.285496,7.680192,-8.197928,2.682669,0.793130,-0.774959,-4.548554,-5.266877,-7.606157,8.798804,-5.168249,5.391022,7.314907,7.669216,1.951030,4.121815,-9.093892,0.105980,-6.176805,-1.471294,-6.925729,-8.573469,-6.589648,1.347668,-5.038390,-9.267195,9.935514,-2.421881,1.599552,-5.688114,-5.934761,-6.507805,-5.760191,7.497892,-7.490080,2.231662,-7.915120,-2.080059,-3.199437,2.476681,-4.994491,9.700259,-5.716109,6.324752,-7.534669,-7.882665,3.875022,8.892085,-8.701193,6.099380,-8.007582,9.139951,-3.208153,-7.024832,-2.891023,2.411091,3.513891,-2.098843,-4.977068,4.131401,3.294571,6.330231,-5.860304,3.302012,-0.364349,7.457030,0.784216,2.351553,-8.260211,-6.009993,-3.380894,-1.745147,-1.144121,1.115909,-4.841024,4.900281,-9.427460,-0.122089,-2.939150,7.336052,-0.523308,8.460215,-8.709766,-8.166703,-4.688252,0.990636,-7.747903,-8.810623,-0.118033,-7.267560,-1.704532,-6.269359,-2.744479,8.595424,-9.726351,7.760550,-2.085527,-9.838523,-2.045709,2.198038,4.672443,4.574639,-6.533233,5.439373,1.320262,4.968049,1.075671,-5.688184,8.471294,-5.911030,-6.349552,-4.388393,4.377313,6.674321,1.770343,-4.284381,1.500260,3.388237,-3.197873,-5.064355,-4.766831,2.945713,-6.380016,3.600879,-7.165065,3.403734,-7.746534,0.913215,6.355330,2.689039,0.510517,6.528885,9.770469,0.846136,1.194713,1.107860,2.255711,-0.930500,-6.683843,5.493163,1.257071,1.520919,4.225661,2.400034,-4.430007,8.955997,9.611216,-0.589045,2.929606,-3.023977,-8.798025,-9.779917,-2.310208,6.985924,9.114089,7.177444,0.752265,-4.850995,7.883900,0.975946,-6.484497,-6.302955,-2.308058,-4.608818,-2.456137,-7.918670,-6.726518,-6.381472,7.379160,6.766681,4.396917,-5.256436,0.144257,9.783570,-2.816987,-7.988798,4.896181,-6.069075,-9.374515,-3.650698,3.277775,8.401180,5.631599,4.850623,7.153213,8.148061,0.865796,7.075450,-6.176338,-1.183455,-9.996188,2.875815,6.094087,1.799411,-8.586924,-0.583921,-8.067969,9.783294,5.457295,7.701932,4.115400,3.158806,-6.396989,-1.994353,3.113179,9.868982,2.727639,-1.884653,6.907431,-4.916446,0.958258,8.766874,-5.068606,8.757148,6.670262,-8.862183,-8.506743,-5.378305,8.119928,9.109097,2.809281,-3.186061,-6.930106,4.672254,-4.402619,7.979378,-1.877473,9.147605,-4.457897,-0.384068,9.075088,-9.904525,3.182187,-8.298191,6.332218,3.554933,0.363250,-0.374417,-3.736303,3.177267,4.535241,-9.379757,0.466925,5.522811,1.934703,-2.623078,-8.736641], dtype = "float64")#candidate|13438|(364,)|const|float64
call_13432 = relay.TupleGetItem(func_6131_call(relay.reshape(const_13433.astype('bool'), [15, 3, 7]), relay.reshape(const_13433.astype('bool'), [15, 3, 7]), relay.reshape(var_13434.astype('float32'), [780, 1]), relay.reshape(var_13435.astype('float64'), [18,]), relay.reshape(var_13436.astype('float64'), []), relay.reshape(var_13437.astype('float64'), [1280,]), relay.reshape(const_13438.astype('float64'), [364,]), ), 10)
call_13439 = relay.TupleGetItem(func_6140_call(relay.reshape(const_13433.astype('bool'), [15, 3, 7]), relay.reshape(const_13433.astype('bool'), [15, 3, 7]), relay.reshape(var_13434.astype('float32'), [780, 1]), relay.reshape(var_13435.astype('float64'), [18,]), relay.reshape(var_13436.astype('float64'), []), relay.reshape(var_13437.astype('float64'), [1280,]), relay.reshape(const_13438.astype('float64'), [364,]), ), 10)
output = relay.Tuple([call_13405,call_13412,const_13413,call_13432,const_13433,var_13434,var_13435,var_13436,var_13437,const_13438,])
output2 = relay.Tuple([call_13406,call_13414,const_13413,call_13439,const_13433,var_13434,var_13435,var_13436,var_13437,const_13438,])
func_13441 = relay.Function([var_13434,var_13435,var_13436,var_13437,], output)
mod['func_13441'] = func_13441
mod = relay.transform.InferType()(mod)
mutated_mod['func_13441'] = func_13441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13441_call = mutated_mod.get_global_var('func_13441')
var_13443 = relay.var("var_13443", dtype = "float32", shape = (780,))#candidate|13443|(780,)|var|float32
var_13444 = relay.var("var_13444", dtype = "float64", shape = (18,))#candidate|13444|(18,)|var|float64
var_13445 = relay.var("var_13445", dtype = "float64", shape = ())#candidate|13445|()|var|float64
var_13446 = relay.var("var_13446", dtype = "float64", shape = (1280,))#candidate|13446|(1280,)|var|float64
call_13442 = func_13441_call(var_13443,var_13444,var_13445,var_13446,)
output = call_13442
func_13447 = relay.Function([var_13443,var_13444,var_13445,var_13446,], output)
mutated_mod['func_13447'] = func_13447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11649_call = mod.get_global_var('func_11649')
func_11651_call = mutated_mod.get_global_var('func_11651')
call_13454 = func_11649_call()
call_13455 = func_11649_call()
func_8966_call = mod.get_global_var('func_8966')
func_8974_call = mutated_mod.get_global_var('func_8974')
var_13483 = relay.var("var_13483", dtype = "bool", shape = (315, 1))#candidate|13483|(315, 1)|var|bool
const_13484 = relay.const([-8.349897,-5.408300,3.738746,-0.114867,-9.074854,-7.592406,8.811614,7.057000,-3.275579,-8.613280,9.374639,-3.864847,-9.794051,2.344904,4.466504,0.919558,1.714466,2.233502,-3.437406,-3.899235,5.573842,-3.679345,2.598238,-6.919676,-0.391796,7.318686,-7.549360,3.918912,6.853400,-0.137761,-5.731867,-3.044519,-7.702634,-8.210171,8.195440,6.247856,1.684878,7.197395,8.803390,-3.381829,6.211736,5.692426,9.669430,-8.672185,-9.679662,-4.191281,-0.656490,-9.950374,-5.809742,-5.757281,6.504014,-6.501868,4.877395,-8.050133,-2.832118,3.712068,-2.985276,4.884596,5.372851,-6.295900,-9.497938,0.042322,6.383351,1.294618,-5.676743,8.154924,4.917702,3.716151,-4.217284,6.131935,-6.874519,-7.260118,-3.312975,7.394776,7.657685,1.065138,-3.076535,5.407463,-7.694880,0.899279,-2.886963,-7.900845,-4.898291,-2.745331,8.623750,3.991397,-2.458438,-4.075234,6.252440,4.067840,3.376274,2.119736,6.938264,0.181706,9.742910,-6.027929,-9.880440,-3.992764,-8.241400,2.260814,-4.775553,-1.099222,-8.783955,5.640302,-4.076609,-1.037546,6.508542,1.608944,-2.251853,-0.253182,1.996316,2.168794,-6.490712,-0.319957,8.875678,-7.494473,6.409551,-5.361609,-6.714535,4.455878,-9.715915,-1.081625,4.680097,-5.386039,9.420020,-1.113240,-3.147783,-7.207838,9.863599,9.949559,-6.607844,-1.260285,-1.977091,2.647277,2.275683,3.305493,-9.488596,5.704004,7.726996,-6.321603,6.684428,9.707831,-3.159201,-2.265818,7.156652,-7.600101,1.577735,1.392871,-3.582306,-7.739145,9.709784,2.244853,-5.279272,-2.051785,8.669468,-2.623744,1.849883,-2.697436,1.348338,2.791415,-2.107637,-1.338873,-2.323496,-9.805760,-0.078121,-7.716963,-2.504734,3.543792,8.793438,8.594868,-1.267155,6.638345,8.182426,-4.658956,-1.301283,7.268857,9.267417,-3.420101,3.507734,-6.966978,-9.953115,-1.466275,5.852623,8.668086,6.381467,4.991857,-7.076176,3.907409,-2.187167,-9.103841,3.284477,3.514314,1.226924,-2.974394,-3.893742,-5.046242,-6.537766,-2.512443,-0.584956,-9.768044,-6.977540,-2.930101,-0.398156,-8.054785,8.443763,9.978857,5.441307,1.409052,-2.817300,9.988425,8.255142,4.853458,-9.759514,6.854164,6.027145,-2.177473,9.859948,-5.605792,-3.693149,-3.288534,6.336103,-4.437998,-4.402669,6.599440,-1.132481,-5.769689,-9.141071,2.628146,0.184955,-7.703188,-1.360165,-4.487388,3.061274,1.680377,3.175284,3.211334,6.475568,7.837984,4.122148,-6.500849,-3.848872,8.807029,7.493431,4.667544,0.231013,0.562056,6.417611,9.851835,9.598671,-7.944912,-7.828986,4.411123,-1.481954,-9.850017,-9.559850,5.050856,5.350309,0.795242,9.622174,2.098700,-7.333190,-7.528487,-8.267560,-2.372709,-3.050438,-1.273090,-1.695864,-5.570009,1.719450,8.252480,7.649724,-0.203447,1.748024,2.048760,-2.136458,-4.663797,-6.328582,-8.767770,-9.241779,-2.988946,-4.183325,-8.808131,-6.258267,4.233284,7.393009,3.145833,7.049019,7.557822,-5.080717,7.038627,0.945784,5.716232,-9.703426,-9.015967,5.523336,4.514231,0.737624,-6.820703,-6.157837,4.724254,-5.007321,-9.632783,-8.922160,1.120558,8.853726,-7.935346,-3.116412,-1.572974,8.571637,2.536657,8.242822,-9.070861,-9.983788,-3.174863,-0.987219,-4.464345,9.377685,-7.913854,-7.148805,-2.975499,-4.799704,-9.649080,-5.148319,9.409868,4.669659,-0.189380,9.433527,-6.183394,-2.261536,-7.508469,-1.865304,9.348339,-5.575988,-5.994013,6.690485,-7.575189,5.330002,-7.182833,7.394023,1.399907,7.980951,6.179519,3.978829,-0.893196,-2.477768,-4.197025,-0.323206,-0.874260,-0.401540,3.926660,5.588826,1.608553,1.611231,5.108144,-4.811030,0.781000,-0.197434,-9.737414,-4.831552,9.965623,-5.683223,-4.312583,-5.858084,8.483808,4.756705,-3.158853,-9.459408,6.872287,-0.048906,-9.036099,2.322202,-6.738820,-3.107806,4.205406,4.921821,9.428614,6.795782,-4.384671,5.929936,-5.218692,1.972920,2.682278,-5.156642,6.145372,4.181005,5.872670,3.544473,0.937818,8.673413,9.509051,3.577721,-5.848998,-2.106116,-4.973855,-4.826997,-9.914199,-9.443294,3.590545,-9.463393,1.570071,-3.077017,-4.759486,-3.772377,3.257177,3.513796,-4.840697,9.906443,5.879720,-1.492500,8.632323,-0.591068,-8.181700,-2.482181,7.764707,-0.753454,-8.992565,-3.433917,-6.780631,-9.205585,-0.358182,-3.713901,2.903331,7.473674,3.630730,-2.397912,-3.898731,-1.487829,1.181354,-3.225422,3.452855,4.581570,0.291221,1.821229,-6.956649,9.664383,1.723568,-9.917681,7.410034,0.980567,0.762452,-0.498945,-3.923766,-9.008243,9.372449,-9.025267,4.950713,-8.349563,1.327286,-4.358215,-8.817989,-3.243185,-3.863667,-1.792528,-3.753885,-5.184433,9.208154,6.314321,-6.618554,-1.781333,-4.631349,-1.447695,-8.280266,-3.130056,-7.788278,-0.790005,-3.193365,-4.261259,2.644289,6.730295,-0.702567,5.864388,-3.159464,3.010505,-2.642872,-4.018096,7.405173,-2.350326,5.213761,3.228174,2.151812,-3.925763,9.769116,-6.455784,5.591832,-8.785355,-0.269091,-6.839844,5.976773,9.755555,7.055415,-8.118646,-4.975126,-5.303214,-0.130334,-9.605982,5.082420,6.717422,1.283640,3.034999,6.151833,5.542107,0.366587,-8.301768,4.473008,-6.641732,2.922922,1.731753,1.723237,-4.293254,-4.376176,-0.549947,3.709842,-6.924199,1.129775,-6.393166,2.702151,-4.495151,3.533910,6.470815,-5.969449,4.887983,6.515367,-0.552175,-0.239534,-1.156746,3.192634,8.355517,-7.933457,3.661690,3.694354,9.272466,8.684323,-8.290489,-0.365916,-2.826711,7.072331,1.395797,-9.309342,-0.034439,-6.844402,7.329272,6.110242,-3.351273,-0.625513,8.568658,4.362679,1.553453,4.155720,7.178375,3.464689,-3.994961,6.172532,4.717688,9.050367,0.837863,-2.777718,0.043690,4.208763,-0.419774,-2.559010,9.949325,-9.007068,-1.522802,-4.557675,2.213545,5.392814,9.615690,6.642832,7.411028,-3.570505,-0.998329,7.132641,-7.325398,-7.624384,2.829283,-6.958723,-0.532721,5.057976,-8.398180,2.432463,9.818899,-5.769382,4.646950,-3.489503,-8.927547,5.363144,7.971104,0.111265,7.057345,-1.415846,-8.007077,-1.981262,6.208007,8.044671,8.633842,-9.025649,-4.042287,0.849572,-8.438691,-4.145047,-5.483447,-4.338818,-2.612442,8.480061,6.364312,-6.241692,5.156877,-7.402134,-2.012374,-8.722521,-8.109058,5.202945,1.732335,0.936302,-7.653413,1.100894,9.381391,-1.757072,5.906673,-1.289089,-2.672812,-6.615980,8.807489,-3.349774,-9.692357,9.346870,9.028576,3.195309,-9.683016,4.203358,-0.863990,3.020814,-4.392847,-7.052382,-7.164168,-1.567515,0.392565,-2.307562,6.467082,7.192329,4.822540,2.863708,9.947755,-5.362284,4.755563,-1.282782,-2.958240,8.726126,9.722457,-0.506146,-8.366613,-4.264742,0.009711,-9.375787,-1.065329,-4.932207,4.955116,-2.854283,5.408496,-1.568573,-4.879242,-5.536098,-3.355625,8.873345,6.906127,9.004118,-2.607365,-8.659145,-7.327093,0.615725,-6.062285,6.830783,2.130645,-9.104165,-0.626358,3.448255,2.822609,0.388664,1.596891,2.712020,-8.341520,4.259389,3.124016,-2.920673,-8.953086,-4.492527,1.808574,-0.490214,8.690903,5.508721,9.486249,1.771434,3.445037,2.017056,1.296137,1.392744,8.994466,1.227473,-7.193869,1.545696,2.058596,6.630294,6.052589,2.948131,-5.963665,-3.388667,4.322282,-0.695985,-7.931777,1.937131,4.380324,9.472775,3.006337,9.985960,-9.767360,3.841454,-6.935918,-9.651385,-7.368571,-9.375676,8.304018,2.170214,-8.642769,5.317014,7.025785,7.843341,7.503773,4.702827,4.038567,1.879548,2.428113,4.662700,2.207686,6.023576,7.342604,9.092791,-8.859663,9.236329,-6.433310,6.118222,5.701679,-8.092947,2.481972,-2.574188,-0.913066,-6.180245,-4.321556,5.158092,-7.281691,7.844138,8.215943,-7.318881,5.645520,-7.110867,-0.208708,1.973097,-9.173600,-0.715151,-2.359780,-7.160907,-6.295437,-0.644288,-7.931355,6.852994,9.181529,-0.021391,0.972945,-5.318052,-6.623555,-8.170592,3.237522,8.766142,-0.911403,7.830680,-2.267951,3.887254,8.652745,7.842552,-2.989414,-6.063900], dtype = "float32")#candidate|13484|(780,)|const|float32
const_13485 = relay.const([1.878583,-6.073107,5.115899,-2.818396,-4.881919,5.092807,8.316288,1.654688,-1.183633,2.746138,7.067246,-8.151026,3.274691,2.677870,8.615297,9.744812,-7.344195,0.385958], dtype = "float64")#candidate|13485|(18,)|const|float64
var_13486 = relay.var("var_13486", dtype = "float64", shape = ())#candidate|13486|()|var|float64
var_13487 = relay.var("var_13487", dtype = "float64", shape = (1280,))#candidate|13487|(1280,)|var|float64
const_13488 = relay.const([True,True,False,True,False,True,True,True,True,False,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,False,False,False,True,False,False,True,False,True,False,True,False,False,True,False,True,False,True,True,False,True,True,True,False,False,True,True,True,False,False,True,True,False,True,False,False,True,False,True,True,False,False,True,False,True,False,True,True,True,True,True,False,False,True,False,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True,True,False,True,False,False,True,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,True,False,True,True,True,True,True,False,False,True,False,True,True,True,True,True,True,True,False,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,True,False,False,False,False,False,True,False,True,False,True,True,False,True,False,False,False,True,False,True,False,False,False,False,False,True,True,True,True,False,False,False,False,False,False,False,False,True,True,False,False,False,True,False,True,True,False,False,False,True,True,False,True,True,True,False,True,False,True,False,False,True,True,False,True,True,False,False,True,True,False,True,False,True,True,True,False,True,True,False,False,False,False,False,False,True,False,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,False,True,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,True,False,False,True,False,False,False,True,False,True,False,True,True,False,True,True,False,True,True,False,True,False,False,True,True,False,False,True,False,False,False,True,False,False,True,False,True,True,True,True,False,True,False], dtype = "bool")#candidate|13488|(360,)|const|bool
call_13482 = relay.TupleGetItem(func_8966_call(relay.reshape(var_13483.astype('bool'), [315,]), relay.reshape(const_13484.astype('float32'), [10, 78]), relay.reshape(const_13485.astype('float64'), [18,]), relay.reshape(var_13486.astype('float64'), []), relay.reshape(var_13487.astype('float64'), [1280,]), relay.reshape(const_13488.astype('bool'), [360, 1]), ), 7)
call_13489 = relay.TupleGetItem(func_8974_call(relay.reshape(var_13483.astype('bool'), [315,]), relay.reshape(const_13484.astype('float32'), [10, 78]), relay.reshape(const_13485.astype('float64'), [18,]), relay.reshape(var_13486.astype('float64'), []), relay.reshape(var_13487.astype('float64'), [1280,]), relay.reshape(const_13488.astype('bool'), [360, 1]), ), 7)
uop_13525 = relay.cos(const_13485.astype('float64')) # shape=(18,)
output = relay.Tuple([call_13454,call_13482,var_13483,const_13484,var_13486,var_13487,const_13488,uop_13525,])
output2 = relay.Tuple([call_13455,call_13489,var_13483,const_13484,var_13486,var_13487,const_13488,uop_13525,])
func_13527 = relay.Function([var_13483,var_13486,var_13487,], output)
mod['func_13527'] = func_13527
mod = relay.transform.InferType()(mod)
var_13528 = relay.var("var_13528", dtype = "bool", shape = (315, 1))#candidate|13528|(315, 1)|var|bool
var_13529 = relay.var("var_13529", dtype = "float64", shape = ())#candidate|13529|()|var|float64
var_13530 = relay.var("var_13530", dtype = "float64", shape = (1280,))#candidate|13530|(1280,)|var|float64
output = func_13527(var_13528,var_13529,var_13530,)
func_13531 = relay.Function([var_13528,var_13529,var_13530,], output)
mutated_mod['func_13531'] = func_13531
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13559 = relay.var("var_13559", dtype = "float64", shape = (11, 6, 13))#candidate|13559|(11, 6, 13)|var|float64
var_13560 = relay.var("var_13560", dtype = "float64", shape = (11, 6, 13))#candidate|13560|(11, 6, 13)|var|float64
bop_13561 = relay.power(var_13559.astype('float64'), relay.reshape(var_13560.astype('float64'), relay.shape_of(var_13559))) # shape=(11, 6, 13)
func_11243_call = mod.get_global_var('func_11243')
func_11246_call = mutated_mod.get_global_var('func_11246')
var_13591 = relay.var("var_13591", dtype = "int8", shape = (24,))#candidate|13591|(24,)|var|int8
var_13592 = relay.var("var_13592", dtype = "int8", shape = (1, 264))#candidate|13592|(1, 264)|var|int8
call_13590 = func_11243_call(relay.reshape(var_13591.astype('int8'), [2, 12, 1]), relay.reshape(var_13592.astype('int8'), [2, 12, 11]), )
call_13593 = func_11243_call(relay.reshape(var_13591.astype('int8'), [2, 12, 1]), relay.reshape(var_13592.astype('int8'), [2, 12, 11]), )
output = relay.Tuple([bop_13561,call_13590,var_13591,var_13592,])
output2 = relay.Tuple([bop_13561,call_13593,var_13591,var_13592,])
func_13595 = relay.Function([var_13559,var_13560,var_13591,var_13592,], output)
mod['func_13595'] = func_13595
mod = relay.transform.InferType()(mod)
mutated_mod['func_13595'] = func_13595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13595_call = mutated_mod.get_global_var('func_13595')
var_13597 = relay.var("var_13597", dtype = "float64", shape = (11, 6, 13))#candidate|13597|(11, 6, 13)|var|float64
var_13598 = relay.var("var_13598", dtype = "float64", shape = (11, 6, 13))#candidate|13598|(11, 6, 13)|var|float64
var_13599 = relay.var("var_13599", dtype = "int8", shape = (24,))#candidate|13599|(24,)|var|int8
var_13600 = relay.var("var_13600", dtype = "int8", shape = (1, 264))#candidate|13600|(1, 264)|var|int8
call_13596 = func_13595_call(var_13597,var_13598,var_13599,var_13600,)
output = call_13596
func_13601 = relay.Function([var_13597,var_13598,var_13599,var_13600,], output)
mutated_mod['func_13601'] = func_13601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10422_call = mod.get_global_var('func_10422')
func_10424_call = mutated_mod.get_global_var('func_10424')
call_13620 = relay.TupleGetItem(func_10422_call(), 1)
call_13621 = relay.TupleGetItem(func_10424_call(), 1)
output = call_13620
output2 = call_13621
func_13645 = relay.Function([], output)
mod['func_13645'] = func_13645
mod = relay.transform.InferType()(mod)
mutated_mod['func_13645'] = func_13645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13645_call = mutated_mod.get_global_var('func_13645')
call_13646 = func_13645_call()
output = call_13646
func_13647 = relay.Function([], output)
mutated_mod['func_13647'] = func_13647
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6412_call = mod.get_global_var('func_6412')
func_6414_call = mutated_mod.get_global_var('func_6414')
call_13651 = relay.TupleGetItem(func_6412_call(), 0)
call_13652 = relay.TupleGetItem(func_6414_call(), 0)
func_11637_call = mod.get_global_var('func_11637')
func_11639_call = mutated_mod.get_global_var('func_11639')
const_13682 = relay.const([6.312881,-7.959210,8.403970,-1.036642,-3.384105,-3.377788,6.941079,7.240610,8.103515,-9.390036,-3.389790,-9.593371,1.940514,3.559341,6.399884,2.007257,1.762066,-7.843000,1.343858,1.419637,7.359598,-5.655079,-5.186241,7.921680,-8.081126,9.809586,8.383842,-6.179203,4.452981,3.857345,7.133938,1.405777,6.236859,4.776883,-1.587280,-7.897127,-5.572471,-5.094524,-3.492484,-1.081912,9.357715,8.509140,-0.327658,3.548407,-6.097265,-0.028785,-2.489852,-7.111787,7.739355,-7.726734], dtype = "float32")#candidate|13682|(50,)|const|float32
call_13681 = relay.TupleGetItem(func_11637_call(relay.reshape(const_13682.astype('float32'), [5, 10])), 4)
call_13683 = relay.TupleGetItem(func_11639_call(relay.reshape(const_13682.astype('float32'), [5, 10])), 4)
func_7788_call = mod.get_global_var('func_7788')
func_7789_call = mutated_mod.get_global_var('func_7789')
call_13684 = func_7788_call()
call_13685 = func_7788_call()
func_12230_call = mod.get_global_var('func_12230')
func_12232_call = mutated_mod.get_global_var('func_12232')
var_13729 = relay.var("var_13729", dtype = "float64", shape = (88,))#candidate|13729|(88,)|var|float64
call_13728 = func_12230_call(relay.reshape(var_13729.astype('float64'), [2, 11, 4]))
call_13730 = func_12230_call(relay.reshape(var_13729.astype('float64'), [2, 11, 4]))
func_1815_call = mod.get_global_var('func_1815')
func_1817_call = mutated_mod.get_global_var('func_1817')
const_13736 = relay.const(False, dtype = "bool")#candidate|13736|()|const|bool
call_13735 = func_1815_call(relay.reshape(const_13736.astype('bool'), []))
call_13737 = func_1815_call(relay.reshape(const_13736.astype('bool'), []))
output = relay.Tuple([call_13651,call_13681,const_13682,call_13684,call_13728,var_13729,call_13735,const_13736,])
output2 = relay.Tuple([call_13652,call_13683,const_13682,call_13685,call_13730,var_13729,call_13737,const_13736,])
func_13739 = relay.Function([var_13729,], output)
mod['func_13739'] = func_13739
mod = relay.transform.InferType()(mod)
mutated_mod['func_13739'] = func_13739
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13740 = relay.var("var_13740", dtype = "float64", shape = (88,))#candidate|13740|(88,)|var|float64
func_13739_call = mutated_mod.get_global_var('func_13739')
call_13741 = func_13739_call(var_13740)
output = call_13741
func_13742 = relay.Function([var_13740], output)
mutated_mod['func_13742'] = func_13742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8283_call = mod.get_global_var('func_8283')
func_8284_call = mutated_mod.get_global_var('func_8284')
call_13771 = relay.TupleGetItem(func_8283_call(), 1)
call_13772 = relay.TupleGetItem(func_8284_call(), 1)
func_12762_call = mod.get_global_var('func_12762')
func_12765_call = mutated_mod.get_global_var('func_12765')
var_13780 = relay.var("var_13780", dtype = "float32", shape = (66,))#candidate|13780|(66,)|var|float32
call_13779 = relay.TupleGetItem(func_12762_call(relay.reshape(var_13780.astype('float32'), [66,])), 2)
call_13781 = relay.TupleGetItem(func_12765_call(relay.reshape(var_13780.astype('float32'), [66,])), 2)
func_5322_call = mod.get_global_var('func_5322')
func_5326_call = mutated_mod.get_global_var('func_5326')
const_13785 = relay.const([-9,-10,9,3,10,-8,-2,-9,2,5,7,-4,10,1,-9,-1,7,5,9,-2,8,7,-4,4,-10,-3,1,-10,-9,4,9,8], dtype = "int32")#candidate|13785|(32,)|const|int32
call_13784 = relay.TupleGetItem(func_5322_call(relay.reshape(const_13785.astype('int32'), [2, 1, 16]), relay.reshape(const_13785.astype('int32'), [2, 1, 16]), ), 2)
call_13786 = relay.TupleGetItem(func_5326_call(relay.reshape(const_13785.astype('int32'), [2, 1, 16]), relay.reshape(const_13785.astype('int32'), [2, 1, 16]), ), 2)
output = relay.Tuple([call_13771,call_13779,var_13780,call_13784,const_13785,])
output2 = relay.Tuple([call_13772,call_13781,var_13780,call_13786,const_13785,])
func_13790 = relay.Function([var_13780,], output)
mod['func_13790'] = func_13790
mod = relay.transform.InferType()(mod)
var_13791 = relay.var("var_13791", dtype = "float32", shape = (66,))#candidate|13791|(66,)|var|float32
output = func_13790(var_13791)
func_13792 = relay.Function([var_13791], output)
mutated_mod['func_13792'] = func_13792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11649_call = mod.get_global_var('func_11649')
func_11651_call = mutated_mod.get_global_var('func_11651')
call_13798 = func_11649_call()
call_13799 = func_11649_call()
func_8097_call = mod.get_global_var('func_8097')
func_8098_call = mutated_mod.get_global_var('func_8098')
call_13808 = relay.TupleGetItem(func_8097_call(), 3)
call_13809 = relay.TupleGetItem(func_8098_call(), 3)
output = relay.Tuple([call_13798,call_13808,])
output2 = relay.Tuple([call_13799,call_13809,])
func_13820 = relay.Function([], output)
mod['func_13820'] = func_13820
mod = relay.transform.InferType()(mod)
output = func_13820()
func_13821 = relay.Function([], output)
mutated_mod['func_13821'] = func_13821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11986_call = mod.get_global_var('func_11986')
func_11987_call = mutated_mod.get_global_var('func_11987')
call_13859 = relay.TupleGetItem(func_11986_call(), 0)
call_13860 = relay.TupleGetItem(func_11987_call(), 0)
func_6489_call = mod.get_global_var('func_6489')
func_6490_call = mutated_mod.get_global_var('func_6490')
call_13864 = func_6489_call()
call_13865 = func_6489_call()
func_9394_call = mod.get_global_var('func_9394')
func_9396_call = mutated_mod.get_global_var('func_9396')
call_13876 = relay.TupleGetItem(func_9394_call(), 0)
call_13877 = relay.TupleGetItem(func_9396_call(), 0)
output = relay.Tuple([call_13859,call_13864,call_13876,])
output2 = relay.Tuple([call_13860,call_13865,call_13877,])
func_13893 = relay.Function([], output)
mod['func_13893'] = func_13893
mod = relay.transform.InferType()(mod)
output = func_13893()
func_13894 = relay.Function([], output)
mutated_mod['func_13894'] = func_13894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10422_call = mod.get_global_var('func_10422')
func_10424_call = mutated_mod.get_global_var('func_10424')
call_13919 = relay.TupleGetItem(func_10422_call(), 3)
call_13920 = relay.TupleGetItem(func_10424_call(), 3)
output = relay.Tuple([call_13919,])
output2 = relay.Tuple([call_13920,])
func_13938 = relay.Function([], output)
mod['func_13938'] = func_13938
mod = relay.transform.InferType()(mod)
output = func_13938()
func_13939 = relay.Function([], output)
mutated_mod['func_13939'] = func_13939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10422_call = mod.get_global_var('func_10422')
func_10424_call = mutated_mod.get_global_var('func_10424')
call_14009 = relay.TupleGetItem(func_10422_call(), 3)
call_14010 = relay.TupleGetItem(func_10424_call(), 3)
output = relay.Tuple([call_14009,])
output2 = relay.Tuple([call_14010,])
func_14014 = relay.Function([], output)
mod['func_14014'] = func_14014
mod = relay.transform.InferType()(mod)
mutated_mod['func_14014'] = func_14014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14014_call = mutated_mod.get_global_var('func_14014')
call_14015 = func_14014_call()
output = call_14015
func_14016 = relay.Function([], output)
mutated_mod['func_14016'] = func_14016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7228_call = mod.get_global_var('func_7228')
func_7229_call = mutated_mod.get_global_var('func_7229')
call_14028 = relay.TupleGetItem(func_7228_call(), 2)
call_14029 = relay.TupleGetItem(func_7229_call(), 2)
output = call_14028
output2 = call_14029
func_14032 = relay.Function([], output)
mod['func_14032'] = func_14032
mod = relay.transform.InferType()(mod)
output = func_14032()
func_14033 = relay.Function([], output)
mutated_mod['func_14033'] = func_14033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10129_call = mod.get_global_var('func_10129')
func_10131_call = mutated_mod.get_global_var('func_10131')
call_14055 = relay.TupleGetItem(func_10129_call(), 0)
call_14056 = relay.TupleGetItem(func_10131_call(), 0)
output = call_14055
output2 = call_14056
func_14064 = relay.Function([], output)
mod['func_14064'] = func_14064
mod = relay.transform.InferType()(mod)
mutated_mod['func_14064'] = func_14064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14064_call = mutated_mod.get_global_var('func_14064')
call_14065 = func_14064_call()
output = call_14065
func_14066 = relay.Function([], output)
mutated_mod['func_14066'] = func_14066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14014_call = mod.get_global_var('func_14014')
func_14016_call = mutated_mod.get_global_var('func_14016')
call_14079 = relay.TupleGetItem(func_14014_call(), 0)
call_14080 = relay.TupleGetItem(func_14016_call(), 0)
func_7836_call = mod.get_global_var('func_7836')
func_7837_call = mutated_mod.get_global_var('func_7837')
call_14081 = relay.TupleGetItem(func_7836_call(), 0)
call_14082 = relay.TupleGetItem(func_7837_call(), 0)
func_322_call = mod.get_global_var('func_322')
func_325_call = mutated_mod.get_global_var('func_325')
var_14084 = relay.var("var_14084", dtype = "uint64", shape = (2100,))#candidate|14084|(2100,)|var|uint64
call_14083 = func_322_call(relay.reshape(var_14084.astype('uint64'), [14, 10, 15]))
call_14085 = func_322_call(relay.reshape(var_14084.astype('uint64'), [14, 10, 15]))
func_2733_call = mod.get_global_var('func_2733')
func_2739_call = mutated_mod.get_global_var('func_2739')
const_14092 = relay.const([-5.214197,-1.821628,-5.539674,7.093826,5.481560,-0.335650,-6.660894,-7.583984,-5.235589,9.672386,-7.744646,3.805741,4.460431,5.449662,-8.501854,9.546773,4.421734,-7.221034,-5.493468,-9.322684,-4.863385,-2.178957,-7.189937,3.062007,-5.401087,7.484268,8.104522,-1.163834,-1.002356,0.559664,-7.018526,2.636502,-6.157052,9.093475,8.305898,-1.485866,-7.822512,5.728941,-7.528342,3.480078,6.641265,8.276179,9.845315,0.814317,3.107723,-7.078759,1.519303,1.458141,1.846463,-2.112665,-0.490132,-8.221671,0.994731,-3.092743,6.575541,-1.588601,-1.544319,5.557653,-3.554398,3.185406,-4.210464,9.933264,-6.662876,4.470310,1.644143,-5.743621,6.280843,-0.273709,-6.546513,-6.520420,-7.082593,-4.615796,-0.829879,-2.111306,-5.025008,-4.976835,-8.246050,3.131750,1.551448,-1.402758,-5.890600,-8.026750,-3.544738,5.021320,4.483155,-5.875643,-1.996642,-7.519723,-4.291427,7.846940,5.221606,7.937513,8.576641,-4.689991,-9.412443,3.653821,9.787892,-0.477952,-8.458099,1.611013,0.628344,4.940206,-9.472406,-8.330840,2.483899,-8.137939,3.289125,-7.831002,-6.836153,1.243042,9.038918,7.906318,2.388865,-4.459016,1.084283,2.162505,8.709723,2.766864,2.913206,0.947825,6.375838,7.064568,7.659834,-6.551856,-7.473801,-5.660221,-8.298629,-5.446034,0.069959,-8.528495,-7.364177,2.753253,-7.539205,-4.828022,-5.706043,-3.202483,4.351584,9.302736,6.485588,-7.752350,2.668251,-0.729211,-6.381596,8.949630,8.361419,7.987580,-1.505711,-5.292262,9.483332,-0.019026,-9.792858,8.258961,-9.808674,-1.679529,-0.420475,7.428084,-6.812707,-9.022046,-0.351599,-4.438752,1.036075,-8.713831,9.015945,-0.258335,8.159262,-6.153424,-1.720250,9.499381,-3.015585,-7.153322,-5.008334,3.044258,7.272639,8.399799,3.056170,-0.234627,0.341590,-6.070186,1.306358,0.270846,1.741670,-3.704393,-7.245598,-3.001898,7.234065,9.801648,-2.687728,-6.111775,-6.325554,-0.143824,-8.747532,-8.026690,5.661477,-5.102003,-2.652964,3.525556,1.002674,9.057642,6.596941,6.948288,-0.654549,-2.784727,9.194810,6.963446,-8.932464,0.687943,-7.919808,5.215273,7.397772,-2.095344,8.584359,8.343127,2.425780,-7.124857,6.438772,8.073851,1.535442,-5.201507,6.680863,-4.043819,3.397378,-4.701805,-8.996919,5.573707,6.355064,9.540433,6.760583,6.530237,9.735136,7.618337,9.580955,-3.032207,-2.804118,2.511063,-1.537978,-1.093599,-2.470437,3.699072,-6.950129,-0.707614,-4.680242,-5.352765,-1.529853,-5.899288,-3.163073,-8.154797,7.929782,-4.701309,-0.644292,7.225291,0.131964,-2.627573,-0.592256,-4.875281,1.795321,-9.689662,-8.359445,5.482456,-9.131064,-2.860165,-4.821505,3.682452,-0.145492,2.649131,0.685413,3.902541,-7.882706,-2.421354,-2.234006,6.164168,0.443246,8.118691,6.714823,4.216307,4.032723,-5.323650,-9.849611,9.743396,5.021013,4.525289,8.836610,5.075879,7.364269,-4.619966,5.896641,4.220337,6.364379,-7.990004,8.362515,-3.477774,-4.910106,-4.938677,-4.170913,4.155426,7.288080,3.763400,2.804475,-0.523944,-1.190374,-7.747763,3.606906,2.275703,6.516209,5.006530,1.076397,3.679904,-2.210395,-2.624984,3.890952,-3.036874,9.402314,6.777016,-2.652522,1.811723,-4.027713,-1.257345,8.337664,-3.915078,-0.185237,6.203999,2.597880,7.974940,5.950809,9.896863,9.338700,3.674046,4.993950,2.060338,-8.589033,-8.128520,6.106743,-3.608995,-1.028625,2.355142,-2.152014,-5.156599,7.003604,5.076953,-5.723233,9.555807,-8.266333,-4.957645,4.357233,-2.593019,-7.843962,-2.702239,4.497762,-9.497647,3.663367,-7.568197,-3.842319,3.448483,-2.964307,-8.405629,3.983168,-9.355926,-5.053687,8.483662,6.311801,-6.714301,2.758466,5.619352,7.188741,-3.731927,3.944257,5.561327,-4.710555,9.519715,9.890713,8.599947,3.882086,7.572885,-7.587408,6.071256,-0.138231,8.201882,-2.557850,-4.870459,-0.271765,-8.467211,-8.484553,9.943054,-1.016833,0.229196,4.132958,3.279775,1.314734,-2.800597,4.549191,9.492930,0.410319,5.517183,7.610841,-1.433914,7.536643,7.833364,-9.285691,-2.189784,3.792447,-8.327575,-9.621773,4.039265,-5.613649,8.946760,3.551519,0.477812,7.371705,-0.891448,1.154344,-8.207655,1.241866,-7.408806,-0.231233,-2.634685,-1.464855,-8.341181,-0.979014,-3.364034,-9.444142,8.076188,-8.984919,-1.827402,6.230317,-5.509250,2.770493,1.599727,-0.587108,-5.257498,-7.390010,-7.838695,-2.726839,9.243475,-7.555422,7.881715,3.915200,-9.601704,-8.822979,6.619564,0.450189,-1.970899,-5.934056,1.865093,0.491866,-7.920879,4.866000,-9.743130,9.250446,-7.153991,-8.450943,-3.774173,-7.867029,5.046838,-4.052070,0.288712,2.568303,-0.989388,5.153244,-3.661458,-9.251335,8.146738,-4.397166,7.902856,4.720239,1.698021,0.429200,-5.087842,6.896877,-4.767324,-4.194125,1.104139,5.423392,-7.604860,-2.828756,3.899032,9.761674,-6.269480,5.406312,5.111148,9.714138,-1.946242,9.494275,4.206103,-4.926386,-4.197598,4.148884,-8.496384,9.854858,5.060194,-7.069290,-9.428407,8.236906,9.397802,-3.266111,-9.002381,3.953866,2.953692,2.481738,0.669807,-8.252399,-6.608574,-8.610881,5.863264,2.396548,9.291930,4.498915,7.947632,-7.566442,6.656735,-4.645719,-6.163213,-9.552528,-2.779212,-0.431521,-2.947202,5.383679,-5.901115,6.788019,0.189431,6.611842,-4.897015,1.622076,9.108205,-3.161888,-5.323033,-2.031917,7.953149,-8.976162,-8.379002,6.797384,-7.395236,-6.122233,-1.417764,-8.247916,-3.937824,-3.759135,-6.648380,8.393815,9.987688,1.754531,-0.954606,8.976427,-6.202286,5.715725,-1.185967,1.061145,9.807063,-1.450255,-3.363791,2.303882,-6.464743,9.014964,4.806656,-1.590225,3.026545,3.793860,-7.652832,9.486141,-8.782737,4.768446,6.964238,7.711170,-8.112764,9.240449,-0.121932,-1.517379,-7.563856,-0.676026,-2.949806,9.664111,-4.125847,4.671377,0.070070,7.068464,2.424486,-7.100654,-9.168363,7.744678,9.471636,0.728825,0.998175,-0.298575,3.147468,-0.691251,-0.988549,8.063154,-0.043819,8.026522,8.939341,2.262384,9.210138,-1.763944,-4.328009,9.783890,-6.252531,2.478172,-9.475941,4.982691,-4.732588,4.970741,6.708003,8.788551,8.607542,8.378562,-2.219039,3.297769,6.434517,8.905746,1.527550,1.048205,1.435869,7.308253,4.969510,1.437909,-8.746069,-6.256562,-8.480980,6.980585,-9.786547,-0.661506,-0.574560,-1.103808,3.146212,3.599047,-1.288972,-2.046007,7.047276,9.919187,9.737891,7.122765,9.792311,8.192085,3.816008,3.331959,-6.406996,-1.723168,7.261472,-7.572810,-0.291780,5.213474,-6.004009,-5.383206,-9.930554,-2.754499,8.445133,5.593518,1.717799,-8.458050,-0.844396,-1.219661,3.595594,9.044840,-9.479195,-2.623265,9.312759,1.712776,6.845662,9.414514,-2.039624,9.124094,2.950501,-6.377160,-6.069159,-3.153613,7.575130,3.888498,3.976474,3.936765,-9.756466,3.333105,-5.356627,1.656683,-9.410702,1.541258,9.509970,-8.372459,4.674612,4.519026,2.699535,-3.845715,0.571353,-3.244486,-4.969304,-8.949850,6.457649,-9.304833,-9.387500,3.961395,4.406260,5.559632,-4.681669,5.261336,9.119801,6.570641,-3.865110,8.864832,6.365227,5.837476,7.742661,-4.693622,6.383241,-7.962864,-2.819756,-9.972118,-8.947606,-2.577675,-1.119554,0.578033,0.027968,-5.512987,-7.137019,9.383587,2.143313,-2.061405,-1.745415,4.217252,0.828672,2.724617,-2.943889,6.345432,-2.752300,4.339188,-0.818681,-9.259903,5.702972,1.971824,-6.432156,9.346201,4.482831,-3.824223,-2.161837,6.759206,-6.459722,9.733132,5.914640,4.556763,4.298363,-9.967637,6.893530,9.240361,5.452500,4.054689,2.063305,-9.311478,-8.347503,-8.289295,-4.683470,-3.930701,-5.326603,9.934797,3.280988,9.038607,1.024263,-5.637794,-5.438169,6.533414,-6.663326,1.158679,8.336218,7.621020,8.985135,-7.927869,6.606928,-3.927066,1.176693,4.929349,-0.201241,5.758287,-8.539962,5.537132,3.784166,0.473549,3.549008,5.992146,-6.666761,-7.530682,-9.756106,6.435518,8.587495,2.327134,-0.426343,6.498811,-8.195231,-2.956267,-0.353586,5.270687,8.757130,-7.289719,-4.163126,1.177379,-1.509744,-0.181237,4.823573,-1.206732,0.828150,3.994715,5.685750,-7.240120,6.195372,-5.172538,-9.169622,4.768449,-3.973517,-8.785074,6.648189,5.510209,1.300189,-1.471267,-8.800970,-8.666497,-6.108756,0.256448,-9.050063,0.392086,-3.943564,-2.985048,-5.295352,-1.072964,4.105790,1.015856,0.688331,-6.150224,-2.206942,8.588502,8.484814,-8.058513,7.698190,0.648766,3.985418,5.413146,3.816094,7.572106,8.337470,-9.423552,-5.098662,6.040908,6.885920,2.583190,-5.684886,-4.085070,-4.333148,5.699441,-0.741559,5.831018,-4.894640,7.883351,-2.746198,7.910306,9.741060,-9.358084,3.553932,4.654376,9.749108,-7.927951,8.295293,-0.844160,5.861739,7.571014,-2.246215,0.009338,4.748152,-6.529734,0.898214,5.712125,-6.527876,0.273471,0.984050,-4.448592,9.419163,-3.687526,9.163307,-1.731058,-3.417152,-8.414371,-1.437231,9.492101,-2.851727,-9.919612,2.498112,-9.843106,4.867145,3.034840,-9.758158,-7.580152,-2.139713,-2.099344,7.474970,-7.343758,-4.847014,-0.061247,6.603137,-2.100792,-2.305177,6.663818,-6.144256,1.573882,0.970966,-4.086386,-5.484005,0.566611,9.966589,-0.090289,-5.791412,9.106331,7.301140,-8.479189,4.433802,-3.025981,0.501037,-0.796414,-2.058578,0.857337,-9.861710,1.885397,-0.472843,-0.171042,9.896409,-8.586284,5.863435,-5.119357,-1.861476,0.540959,-5.803996,5.409470,-3.378877,5.819345,6.048985,-7.077625,1.223738,-0.335503,2.214440,8.821414,2.698093,-2.034967,7.034597,9.192504,9.557254,-0.201717,-4.657137,1.876331,1.198193,8.535212,-7.957013,-4.999299,-8.132135,6.678200,0.030844,-4.105252,5.152744,-9.028866,1.457180,-3.675947,-9.546569,-2.613811,-3.594004,0.031652,8.777291,-3.871787,8.676970,9.601030,8.817406,9.587072,0.951660,2.864839,-9.848205,-0.023604,5.028151,0.072634,5.635157,-0.536881,7.133442,7.308964,6.331942,-6.812328,-3.448323,-3.430671,4.839047,2.598373,9.131722,8.696378,-6.989767,7.681700,-5.884314,6.277289,8.433637,2.420181,-0.047620,2.681800,-5.788356,-1.560186,7.703233,-7.500066,-2.938125,7.704226,-0.852803,3.958218,-5.949865,-2.178090,3.334054,-2.046711,3.315990,-9.144364,-5.159977,8.271857,8.399854,-8.064590,-8.999025,3.521268,-4.705162,-5.986614,8.504241,9.789577,6.721209,-8.233394,1.700912,2.019585,-2.289049,-6.583673,9.824359,0.815535,0.293088,8.057394,-6.272878,-7.470697,8.743399,8.670310,8.304379,8.220722,-0.014552,7.092058,-1.578991,0.585682,-0.372935,-0.830105,2.426791,5.593507,4.332612,6.032379,5.037856,-1.775639,-3.493022,-9.146764,-5.852718,-6.697597,5.516899,-7.420112,-4.084006,0.037514,-6.752366,-5.689973,3.266285,-8.297770,-4.501785,6.316441,-3.774722,2.660445,7.016238,-5.302559,7.116718,1.343325,-8.804985,-9.324718,5.434025,-8.477114,7.102187,2.005565,-4.063725,8.776096,8.879413,-1.285313,-9.117768,4.871473,9.240131,5.316368,-8.419034,-3.717018,3.398292,-0.920378,-8.013034,-5.771183,8.295183], dtype = "float64")#candidate|14092|(1080,)|const|float64
const_14093 = relay.const([-2.115702,-6.650995,2.657734,8.720493,1.582228,5.683050,9.869033,5.738627,-7.063223,5.456687,-6.201302,5.712246,2.852615,5.569674,0.138812,-3.429037,-0.733572,4.966449,-3.116100,1.157604,8.668442,6.198392,-8.064416,9.715344,-3.608618,6.720146,-9.337169,3.853792,-2.514754,9.869090,1.519971,-3.099895,-8.061139,4.452378,-2.037761,0.648295,0.986751,-9.287424,9.846271,-2.304181,-8.115825,-5.718974,-0.874235,-3.973629,-2.219203,5.898680,1.201583,1.375416,4.738157,-3.147818], dtype = "float32")#candidate|14093|(50,)|const|float32
const_14094 = relay.const([False,True,True,True,True,False,True,True,False,True,False,False,True,True,False,True,False,False,True,True,True,False,False,False,False,True,False,False,False,True,True,False,False,False,False,False,False,True,True,True,True,True,True,False,False,True,False,False], dtype = "bool")#candidate|14094|(48,)|const|bool
call_14091 = relay.TupleGetItem(func_2733_call(relay.reshape(const_14092.astype('float64'), [10, 9, 12]), relay.reshape(const_14092.astype('float64'), [10, 9, 12]), relay.reshape(const_14093.astype('float32'), [50,]), relay.reshape(const_14094.astype('bool'), [48,]), ), 3)
call_14095 = relay.TupleGetItem(func_2739_call(relay.reshape(const_14092.astype('float64'), [10, 9, 12]), relay.reshape(const_14092.astype('float64'), [10, 9, 12]), relay.reshape(const_14093.astype('float32'), [50,]), relay.reshape(const_14094.astype('bool'), [48,]), ), 3)
bop_14096 = relay.bitwise_and(var_14084.astype('uint8'), relay.reshape(call_14083.astype('uint8'), relay.shape_of(var_14084))) # shape=(2100,)
bop_14099 = relay.bitwise_and(var_14084.astype('uint8'), relay.reshape(call_14085.astype('uint8'), relay.shape_of(var_14084))) # shape=(2100,)
func_7521_call = mod.get_global_var('func_7521')
func_7525_call = mutated_mod.get_global_var('func_7525')
var_14117 = relay.var("var_14117", dtype = "float64", shape = (1350,))#candidate|14117|(1350,)|var|float64
call_14116 = relay.TupleGetItem(func_7521_call(relay.reshape(call_14081.astype('float32'), [3, 11, 2]), relay.reshape(var_14117.astype('float64'), [1350,]), ), 0)
call_14118 = relay.TupleGetItem(func_7525_call(relay.reshape(call_14081.astype('float32'), [3, 11, 2]), relay.reshape(var_14117.astype('float64'), [1350,]), ), 0)
func_8283_call = mod.get_global_var('func_8283')
func_8284_call = mutated_mod.get_global_var('func_8284')
call_14150 = relay.TupleGetItem(func_8283_call(), 2)
call_14151 = relay.TupleGetItem(func_8284_call(), 2)
output = relay.Tuple([call_14079,call_14081,call_14091,const_14092,const_14093,const_14094,bop_14096,call_14116,var_14117,call_14150,])
output2 = relay.Tuple([call_14080,call_14082,call_14095,const_14092,const_14093,const_14094,bop_14099,call_14118,var_14117,call_14151,])
func_14155 = relay.Function([var_14084,var_14117,], output)
mod['func_14155'] = func_14155
mod = relay.transform.InferType()(mod)
var_14156 = relay.var("var_14156", dtype = "uint64", shape = (2100,))#candidate|14156|(2100,)|var|uint64
var_14157 = relay.var("var_14157", dtype = "float64", shape = (1350,))#candidate|14157|(1350,)|var|float64
output = func_14155(var_14156,var_14157,)
func_14158 = relay.Function([var_14156,var_14157,], output)
mutated_mod['func_14158'] = func_14158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7459_call = mod.get_global_var('func_7459')
func_7461_call = mutated_mod.get_global_var('func_7461')
call_14160 = func_7459_call()
call_14161 = func_7459_call()
func_7955_call = mod.get_global_var('func_7955')
func_7957_call = mutated_mod.get_global_var('func_7957')
call_14168 = relay.TupleGetItem(func_7955_call(), 1)
call_14169 = relay.TupleGetItem(func_7957_call(), 1)
output = relay.Tuple([call_14160,call_14168,])
output2 = relay.Tuple([call_14161,call_14169,])
func_14173 = relay.Function([], output)
mod['func_14173'] = func_14173
mod = relay.transform.InferType()(mod)
output = func_14173()
func_14174 = relay.Function([], output)
mutated_mod['func_14174'] = func_14174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12699_call = mod.get_global_var('func_12699')
func_12700_call = mutated_mod.get_global_var('func_12700')
call_14188 = func_12699_call()
call_14189 = func_12699_call()
output = relay.Tuple([call_14188,])
output2 = relay.Tuple([call_14189,])
func_14191 = relay.Function([], output)
mod['func_14191'] = func_14191
mod = relay.transform.InferType()(mod)
mutated_mod['func_14191'] = func_14191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14191_call = mutated_mod.get_global_var('func_14191')
call_14192 = func_14191_call()
output = call_14192
func_14193 = relay.Function([], output)
mutated_mod['func_14193'] = func_14193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12584_call = mod.get_global_var('func_12584')
func_12585_call = mutated_mod.get_global_var('func_12585')
call_14215 = relay.TupleGetItem(func_12584_call(), 0)
call_14216 = relay.TupleGetItem(func_12585_call(), 0)
func_12039_call = mod.get_global_var('func_12039')
func_12042_call = mutated_mod.get_global_var('func_12042')
const_14233 = relay.const([1.442595,-3.391090,4.467521,-1.886175,-6.209714,8.005670,-4.162135,-0.416828,-8.032453,-8.280441,4.918437,6.802051,-5.263675,-7.648768,6.959174,-8.154269,0.164061,3.046739,-3.768236,-5.666325,3.176847,-7.372006,7.489830,-6.952612,5.064353,-7.747711,-6.003629,-7.258929,-9.526074,-2.647178,-1.366801,9.430078,4.747415,-5.757728,-8.722344,-3.813529,-4.471444,6.789917,9.498056,3.773487,-1.946129,-9.171604,-1.313732,0.813318,4.131146,-1.892934,-8.483547,9.581128,-2.377523,-5.429228], dtype = "float32")#candidate|14233|(50,)|const|float32
call_14232 = relay.TupleGetItem(func_12039_call(relay.reshape(const_14233.astype('float32'), [5, 10])), 2)
call_14234 = relay.TupleGetItem(func_12042_call(relay.reshape(const_14233.astype('float32'), [5, 10])), 2)
func_8745_call = mod.get_global_var('func_8745')
func_8748_call = mutated_mod.get_global_var('func_8748')
var_14253 = relay.var("var_14253", dtype = "float32", shape = (64, 1))#candidate|14253|(64, 1)|var|float32
const_14254 = relay.const([[1.584110,9.076586,8.223858,8.480640,-4.304512,6.633631,-8.206390,2.704509,1.609951,5.608321,-9.596730,-4.750053,0.216739,4.548374,-4.967301,-5.325197,-8.639689,-7.335336,4.190329,-9.075779,9.001205,-2.844823,1.230360,-5.015044,-6.528404,-2.380755,1.259284,-8.777979,-3.016440,-5.643666,6.023894,-7.047796,0.174718,0.372319,-3.441309,-0.269133,3.677856,9.248210,-2.595022,-7.216756,-0.872191,8.142090,1.741705,-8.494121,7.944364,-4.392355,-8.470176,2.226295,1.896173,-1.003789,-9.133173,5.234186,-2.036313,-3.574891,-9.222409,3.648872,1.878165,-1.978898,-3.781492,3.916313,-6.747843,1.756452,-0.074477,-9.923028,3.164152,-0.084235,1.151373,-5.751469,-1.235235,7.536792,0.187286,2.700627,9.324561,6.224194,2.951653,-3.496664,-0.215745,-9.134460,-7.930313,-5.684357,1.975127,5.361466,-0.685046,-4.939678,-1.648950,-0.030759,-0.117272,-3.215442,6.687453,-7.468498,-0.011264,-4.232501,-2.347496,-1.181860,0.190833,-0.072697,1.724653,-2.433883,1.087864,-0.413393],[-3.212843,0.611703,3.830786,-8.112365,9.369946,1.209704,3.870014,-9.205243,-6.920720,-6.871773,2.149477,-6.195364,-9.095293,4.864297,-6.602929,2.620917,-2.193954,4.134573,5.644491,-2.002952,-7.160836,-5.019713,-9.864714,9.471176,0.093059,-2.440696,0.177444,2.924363,9.207499,6.284023,2.956688,-5.194334,-4.846842,6.081214,-3.699358,-1.156446,2.793317,-3.582167,-8.364239,-2.215547,-2.758865,-0.452517,4.536821,0.636920,-2.560071,-8.736431,-0.474333,4.155377,4.858309,-4.709935,5.540827,-9.938484,1.340640,-3.411898,5.734462,-4.220379,7.016777,9.753058,-6.729030,-0.282444,2.291749,-3.682618,6.402096,-4.635964,-1.088914,-4.840563,-5.940718,-0.446741,-3.687954,6.997554,1.719593,7.227835,-0.116201,-1.977892,3.504950,-9.759877,7.142473,-0.296653,-1.032556,9.859819,1.952219,-6.637260,2.398324,-7.380094,4.778522,5.051096,1.792062,-9.120294,4.200219,-8.550685,8.203113,4.902374,-0.629181,9.281758,7.822724,4.367616,9.647415,-9.987344,6.976614,-1.394534],[-4.500055,2.313285,-2.265470,6.722181,-5.088477,-4.565422,-3.421138,0.920133,-5.959413,-2.823547,0.708886,-5.340489,8.797167,8.039110,8.674172,-2.403418,6.490211,1.932388,2.859676,8.559892,9.209701,1.311726,-7.440184,-8.136516,9.176417,-4.576530,-3.780103,3.180008,1.368908,-9.369515,-5.528835,-2.550022,0.123404,9.264622,-3.770562,-5.183057,0.784600,-4.474963,-9.538795,-7.725876,0.578145,5.241008,4.505488,7.419784,6.289704,-5.920799,-9.179049,-6.258302,-8.046122,-7.667289,-0.070569,-9.985281,-9.752251,0.395039,3.038432,4.939355,-9.470180,5.467214,5.654024,-6.874752,-3.773231,4.864226,4.457552,-1.469764,3.380721,2.958214,-1.178119,3.536067,-4.236055,5.400429,-7.670238,-3.977813,6.237369,0.703239,-5.541690,-9.926308,-8.536435,-5.676727,3.088204,5.253649,1.459067,-8.877188,9.858339,4.188219,1.509021,0.088996,4.032241,-0.042023,4.253211,4.589979,-5.138521,3.216613,7.139982,-7.058518,-0.855949,-6.562439,-2.126434,7.707612,-3.570176,9.433832],[-7.227855,-7.898038,-2.749570,-2.748931,-1.498495,-5.949081,7.970777,4.881332,9.615690,4.349262,9.937928,0.033824,0.598751,7.467351,3.038756,5.879916,-6.504986,8.018808,-2.074762,-5.132435,-5.495516,9.644893,-0.590668,-1.760067,2.962115,-3.024283,8.686845,-8.955242,-2.367442,2.090273,5.751486,5.254701,-0.058093,-4.758997,6.315180,8.009228,2.984080,3.053522,7.463524,8.508156,-0.011751,1.819873,-1.644150,-5.227178,-5.336004,-2.633544,-7.539797,4.840742,3.886875,8.469830,-2.870423,-7.928434,-2.772339,-1.851647,4.890600,-8.025634,7.088018,-0.162652,8.630134,-7.109049,-6.626423,1.917815,5.194298,4.055846,6.816295,0.878179,1.818534,2.938091,5.120270,3.982990,-8.353471,-4.096408,9.900367,1.402371,5.248132,-7.488893,-1.995024,-5.155728,-1.943561,-4.041099,5.918582,-7.142589,7.333083,-7.835169,2.831626,-8.265194,9.178530,5.177758,7.078593,3.275015,-1.536321,-0.699504,-0.037335,-9.368127,-2.246794,-1.566450,-9.041207,-0.694340,-0.438602,3.825744]], dtype = "float32")#candidate|14254|(4, 100)|const|float32
call_14252 = relay.TupleGetItem(func_8745_call(relay.reshape(var_14253.astype('float32'), [4, 16, 1]), relay.reshape(const_14254.astype('float32'), [400,]), ), 0)
call_14255 = relay.TupleGetItem(func_8748_call(relay.reshape(var_14253.astype('float32'), [4, 16, 1]), relay.reshape(const_14254.astype('float32'), [400,]), ), 0)
func_9207_call = mod.get_global_var('func_9207')
func_9211_call = mutated_mod.get_global_var('func_9211')
const_14267 = relay.const([False,False,True,False,True,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,True,False,True,False,True,True,False], dtype = "bool")#candidate|14267|(48,)|const|bool
call_14266 = relay.TupleGetItem(func_9207_call(relay.reshape(call_14232.astype('float64'), [1080,]), relay.reshape(const_14267.astype('bool'), [48,]), ), 0)
call_14268 = relay.TupleGetItem(func_9211_call(relay.reshape(call_14232.astype('float64'), [1080,]), relay.reshape(const_14267.astype('bool'), [48,]), ), 0)
uop_14282 = relay.atanh(const_14254.astype('float64')) # shape=(4, 100)
func_11188_call = mod.get_global_var('func_11188')
func_11190_call = mutated_mod.get_global_var('func_11190')
var_14286 = relay.var("var_14286", dtype = "float64", shape = (1815,))#candidate|14286|(1815,)|var|float64
call_14285 = relay.TupleGetItem(func_11188_call(relay.reshape(var_14286.astype('float64'), [1815,])), 3)
call_14287 = relay.TupleGetItem(func_11190_call(relay.reshape(var_14286.astype('float64'), [1815,])), 3)
uop_14300 = relay.atan(uop_14282.astype('float64')) # shape=(4, 100)
uop_14302 = relay.erf(uop_14300.astype('float64')) # shape=(4, 100)
bop_14311 = relay.less(uop_14302.astype('bool'), relay.reshape(uop_14282.astype('bool'), relay.shape_of(uop_14302))) # shape=(4, 100)
output = relay.Tuple([call_14215,call_14232,const_14233,call_14252,var_14253,call_14266,const_14267,call_14285,var_14286,bop_14311,])
output2 = relay.Tuple([call_14216,call_14234,const_14233,call_14255,var_14253,call_14268,const_14267,call_14287,var_14286,bop_14311,])
func_14322 = relay.Function([var_14253,var_14286,], output)
mod['func_14322'] = func_14322
mod = relay.transform.InferType()(mod)
var_14323 = relay.var("var_14323", dtype = "float32", shape = (64, 1))#candidate|14323|(64, 1)|var|float32
var_14324 = relay.var("var_14324", dtype = "float64", shape = (1815,))#candidate|14324|(1815,)|var|float64
output = func_14322(var_14323,var_14324,)
func_14325 = relay.Function([var_14323,var_14324,], output)
mutated_mod['func_14325'] = func_14325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10288_call = mod.get_global_var('func_10288')
func_10289_call = mutated_mod.get_global_var('func_10289')
call_14345 = func_10288_call()
call_14346 = func_10288_call()
func_6946_call = mod.get_global_var('func_6946')
func_6948_call = mutated_mod.get_global_var('func_6948')
call_14348 = relay.TupleGetItem(func_6946_call(relay.reshape(call_14345.astype('float32'), [3, 11, 2])), 0)
call_14349 = relay.TupleGetItem(func_6948_call(relay.reshape(call_14345.astype('float32'), [3, 11, 2])), 0)
output = relay.Tuple([call_14345,call_14348,])
output2 = relay.Tuple([call_14346,call_14349,])
func_14355 = relay.Function([], output)
mod['func_14355'] = func_14355
mod = relay.transform.InferType()(mod)
output = func_14355()
func_14356 = relay.Function([], output)
mutated_mod['func_14356'] = func_14356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14032_call = mod.get_global_var('func_14032')
func_14033_call = mutated_mod.get_global_var('func_14033')
call_14389 = func_14032_call()
call_14390 = func_14032_call()
func_8005_call = mod.get_global_var('func_8005')
func_8009_call = mutated_mod.get_global_var('func_8009')
var_14411 = relay.var("var_14411", dtype = "int16", shape = (1, 312))#candidate|14411|(1, 312)|var|int16
var_14412 = relay.var("var_14412", dtype = "bool", shape = (315,))#candidate|14412|(315,)|var|bool
var_14413 = relay.var("var_14413", dtype = "float32", shape = (5, 156))#candidate|14413|(5, 156)|var|float32
call_14410 = relay.TupleGetItem(func_8005_call(relay.reshape(var_14411.astype('int16'), [13, 8, 3]), relay.reshape(var_14412.astype('bool'), [315,]), relay.reshape(var_14413.astype('float32'), [780,]), ), 3)
call_14414 = relay.TupleGetItem(func_8009_call(relay.reshape(var_14411.astype('int16'), [13, 8, 3]), relay.reshape(var_14412.astype('bool'), [315,]), relay.reshape(var_14413.astype('float32'), [780,]), ), 3)
func_10957_call = mod.get_global_var('func_10957')
func_10961_call = mutated_mod.get_global_var('func_10961')
const_14421 = relay.const([7.614239,8.236215,1.661884,5.402409,-4.143254,7.000918,1.413763,1.505899,4.158829,-2.956266,3.497296,3.749519,-2.012558,-9.792277,-2.617676,-9.316687,6.129945,9.837725,-0.149411,8.538959,-6.852818,9.192111,3.319677,-7.792639,-2.022627,8.583195,7.269086,-4.664392,5.907519,1.162235,-7.555382,8.635743,-6.604592,-6.839690,-1.153347,9.701706,-8.218622,-2.733266,-3.155034,-2.030555,0.538510,-4.622005,-7.223015,-5.413009,5.743825,6.050609,8.023880,2.235748,-8.725141,-5.436997,-1.613818,1.446880,-5.091352,-1.779557,-1.228700,-0.883325,-1.305170,-0.759973,4.229892,-7.773422,4.435981,-5.758885,5.530720,-3.115656,-3.573814,-2.381583,-6.439327,0.452013,5.236799,5.652193,5.498839,5.675753,2.156000,-0.379399,8.817405,1.551483,7.359799,8.309699,-1.271101,-5.689423,3.469634,9.871101,-0.808020,-8.338188,-5.392027,8.090229,9.919741,8.820094,6.948658,-9.700662,2.989294,7.679439,1.372333,6.051327,-8.666630,-5.546810,-5.577164,3.916630,9.491077,-7.597521,-8.524308,3.652938,-6.839259,-3.850140,-6.803977,-2.898876,-5.719246,-1.307713,4.259471,0.242983,5.740604,6.072774,1.230626,-2.521720,-4.247963,-6.034421,8.467874,4.144932,3.646744,3.381345,-4.740316,5.571624,9.575631,-0.808175,1.011773,-0.016195,-0.801123,-6.219491,-2.544428,-8.041197,4.692046,0.836534,-1.206493,-7.081918,-8.519680,8.504995,-1.199239,-3.899506,3.358835,-3.998088,-3.900067,2.650220,-8.360032,2.385156,9.545922,1.021101,-1.821402,9.994116,9.957445,-4.038315,6.978499,-9.543508,-9.988128,3.162347,-4.203695,-0.921072,-0.435186,7.262913,9.853051,6.705974,-5.533728,6.537333,-7.507940,9.652199,3.677265,6.434583,9.719792,-5.549276,-7.516744,6.790946,0.672050,-5.711986,-1.482066,-6.349554,-6.501830,-7.254217,-8.395270,1.404472,-5.485229,3.305750,4.848135,-8.202712,-1.817349,-0.562806,-3.427098,2.172776,-7.219414,8.076506,9.672065,-3.781713,8.071744,-5.212353,0.573172,-7.015057,-7.843132,3.833853,5.347162,6.080545,-2.801468,-5.769018,6.216048,-8.866267,6.177322,-2.080359,6.255760,-8.017926,7.023264,-4.651348,5.498720,-3.047017,-0.478837,5.169004,6.393168,-2.688824,-2.329830,-0.459632,-8.468420,3.276765,-9.874426,5.297154,7.496138,6.580312,-0.761680,0.920715,-8.167954,-9.294454,0.991707,-4.577005,-5.593360,-8.850773,-4.004168,-4.086130,0.848077,-9.864705,-3.597172,6.422847,-9.319136,-1.156809,-2.693455,-4.422701,-7.557697,-5.490596,-8.989485,-4.922927,5.518013,5.029552,-2.710471,-7.076288,-7.688285,1.497319,-2.012086,-3.473581,7.781114,-6.649182,-5.634926,7.239917,5.152043,-8.934144,-3.121469,-1.771049,4.910423,6.192251,8.368286,8.228810,9.808954,-2.060361,6.961540,-6.354961,-0.551570,-6.545511,3.463976,6.128597,8.271067,-2.966092,-6.400633,0.209863,-6.553393,7.833162,1.457066,8.218551,-2.547720,-6.516486,-0.673920,-8.742886,5.777860,5.165077,-9.401474,3.189652,-7.040822,-6.919540,-3.684541,-9.440936,-5.530659,3.819343,-4.139789,-9.714616,-9.430468,-1.750858,2.029890,7.778177,-7.106948,2.577498,7.200279,-4.834299,-5.612016,8.127169,7.911748,-4.803840,5.274481,2.976893,-3.646034,-2.728157,-8.119536,-9.078821,-9.890341,0.681534,-1.207478,4.013955,5.884009,-3.917445,-0.110058,4.369236,2.189671,-7.147778,6.712248,5.474462,4.418509,-8.870267,-3.967786,-3.643144,9.143749,7.107636,-2.697697,7.708401,8.003981,-7.663066,0.260333,7.871029,8.960292,-5.651727,1.857207,-7.698856,8.040794,-1.383166,8.743755,-7.537574,-9.581116,1.941375,7.109630,1.619611,-0.098055,-2.748986,7.576089,-6.433214,4.555474,2.169042,-7.147416,-4.473043,-8.515300,-8.215398,2.773853,-1.467679,-6.795442,-5.222364,7.983957,-4.402794,6.956964,0.061302,-2.794953,7.698880,-1.706373,-3.134353,3.432940,4.776033,-6.707286,8.071953,-2.271194,3.975161,9.637044,-8.737173,8.499010,-4.171279,-4.166998,0.402937,-0.290088,-5.734073,8.548444,0.664499,1.662270,6.675127,-8.866468,0.074536,-1.083418,-2.833991,3.641427,-7.820635,4.252076,1.224627,0.601185,1.730031,-1.442058,-3.556902,-0.046794,-1.591043,-1.755454,1.429510,-7.638197,-8.661334,-8.619648,6.543895,5.095832,-4.677102,-6.965983,-8.222707,7.537424,5.908371,-0.228950,7.363272,-5.711198,-5.904750,5.840817,5.080026,6.094706,7.789667,-7.785049,9.232859,-2.285365,1.787966,2.449179,-0.412756,0.180379,-1.182239,-9.288829,-3.395557,3.088376,1.762310,7.135946,8.615666,-3.152993,-9.881210,1.534102,4.600690,8.384418,-7.316839,-6.641388,3.163618,0.719113,5.191185,-9.381898,-5.325875,5.840337,-2.096701,-1.159706,3.475656,-0.328300,-2.575365,0.704786,-5.054834,-0.418165,4.852380,3.185026,-9.114061,0.844026,-2.600332,1.241884,6.945668,0.198171,3.453597,4.857670,-0.392854,-8.862142,8.419743,-3.538209,3.361009,8.182473,-1.580999,6.083478,9.923190,-8.897541,-6.764317,-0.624404,-3.220513,-8.665207,0.600601,-2.970272,5.845306,-2.498054,-1.968690,-6.317952,5.448053,9.404415,1.082218,-7.547841,0.626614,-9.957433,5.188534,5.257633,-4.117915,6.975833,-7.564736,-5.685197,2.387036,-0.844406,6.109645,7.274549,-6.677206,-9.081590,3.798508,-8.661113,-6.638906,7.764723,3.310610,5.251674,-4.350698,-3.517584,0.696906,-1.053470,3.110591,-5.797805,-1.820471,-7.209194,-4.244817,-5.326720,0.593157,-6.584323,0.225612,2.826563,4.319577,0.450362,-7.814442,-1.678491,-2.157877,-6.770364,9.688037,-0.824596,-8.092075,7.126069,-1.828441,-7.299306,-7.784921,4.643223,-5.022557,5.005322,5.832940,1.939361,-8.755547,8.745007,6.324328,-3.401605,0.676655,-1.288871,4.600226,-3.884473,2.886729,-4.921357,-1.580413,7.945912,-7.086545,-1.790176,9.563695,7.348664,9.381413,-2.882611,-6.156139,9.727577,-5.097928,1.710990,4.117259,4.379893,5.121631,9.686901,8.308966,-3.119371,7.901578,9.764673,9.454068,-7.250983,-1.444364,5.162657,5.583695,-1.737397,-3.950348,-4.677334,3.816881,-8.066173,5.825516,-6.695525,-2.456536,-7.717827,8.811413,5.275134,6.254093,2.559819,-5.548399,-6.997657,-6.277736,3.085659,1.242754,-8.101928,4.243503,7.502366,-5.185375,3.106766,-8.097767,-0.499567,-8.007138,-8.964878,6.369496,7.676056,-4.100288,-7.236094,-2.306532,8.905350,0.244308,-3.698707,-4.955602,0.439787,-7.076205,-6.547006,-1.797241,-3.408383,-7.885263,-7.625258,2.480686,0.444942,-0.909763,-8.664043,-9.451228,-2.783972,8.146608,-5.202248,-4.710915,6.835613,0.223235,0.923413,-2.594932,-5.106625,1.444516,3.897559,-7.789376,-6.473463,-7.945202,4.944438,3.668781,-7.457904,-4.489265,-1.669742,-4.438826,4.514652,9.899846,3.270750,6.972096,-1.865478,7.083708,4.756715,7.415151,-4.357222,-2.022449,-0.388304,5.987012,-1.953558,3.318295,-7.614627,-7.121364,8.453103,-6.943305,-2.350129,-2.642815,-9.509535,-6.273830,8.355035,-6.550783,5.911467,1.505856,-5.344882,-2.959776,2.461904,0.607841,9.658779,3.349393,-9.127306,9.049946,5.799604,8.685100,5.462970,7.096756,5.392883,-9.642564,-7.276304,-1.165910,-1.776641,-2.685391,1.127362,9.533105,7.998532,5.981285,7.080609,-1.568071,5.992493,-1.899617,8.961534,5.461746,8.373707,9.760268,-6.818456,-0.582495,-1.777254,-1.504545,7.469111,-9.484830,-8.916711,-9.917669,7.011869,6.116583,-6.724125,9.974400,9.634460,6.405895,9.644338,5.770428,-8.433106,-5.797369,-6.396869,-4.953734,0.170102,-5.400716,0.640179,6.882990,-3.792976,4.352034,-5.485119,-7.824027,1.827156,4.145958,9.360397,-7.867069,-3.071601,-9.932323,0.762665,-0.847790,-9.029705,7.188414,6.751234,-3.098537,9.633997,3.144782,-4.997629,8.612050,9.669763,-8.836850,3.417629,-3.021531,-2.442710,-9.017149,-2.377250,-0.178704,-7.214012,-3.652900,-9.643515,2.175298,-9.475599,5.224154,-5.734575,-0.796328,6.456921,-4.991726,-9.513661,0.227612,-2.830332,-1.400686,-9.860733,3.276982,-8.266318,2.933015,-2.930003,-4.585553,7.581561,0.936793,4.250694,3.185322,6.116078,0.903583,-9.543176,-8.089338,4.607478,4.392296,4.745801,-9.308857,-1.542951,-1.617933,-8.632542,7.845331,-0.380408,2.278477,2.932240,7.010066,2.004849,-3.411191,7.668860,-5.415940,9.546376,-7.306161,-2.643883,5.816937,-6.178601,8.572477,-0.329319,-9.633833,8.134466,-4.919302,-2.969585,0.229138,8.320758,-0.026478,-3.455267,3.791529,-3.193154,-2.662295,-8.457268,-5.662441,2.156053,3.199543,-5.006400,2.937559,4.745555,-5.417189,2.066620,5.167362,5.936220,3.148535,-8.432925,-4.239815,-9.848845,7.667568,-2.409067,-8.541309,1.035666,2.147576,9.963019,-5.567467,7.449214,7.008175,-2.658710,5.795559,-4.331848,-1.060354,6.714716,0.722088,3.107258,-4.232246,-9.751505,-9.402881,-0.854961,-8.706427,-1.587028,-7.946282,7.784447,-7.887997,7.701236,-7.584325,-5.660182,-9.357190,4.231965,8.162045,7.887657,-1.159048,-1.991259,8.613736,-3.361329,4.772684,-7.440892,-4.799405,4.122063,-5.852589,-6.783760,-1.147567,2.810672,-4.642759,-7.992152,3.382289,5.015151,-8.819223,-6.601350,-1.604335,0.945973,5.714001,-1.013089,7.008215,-4.504932,-3.301253,-3.257507,1.593512,1.104787,-9.294459,-8.289782,6.170633,5.595112,7.447918,-8.888497,1.933877,7.342615,6.262712,-9.345058,0.539733,-3.014826,-4.546993,-3.461660,-5.816000,7.553686,-7.173828,6.152543,-2.750597,2.225709,-3.603942,8.553891,9.888225,5.929812,-1.771873,1.585703,-6.621746,6.075671,0.413424,6.400361,-9.294324,-1.420175,-9.141106,-0.855427,0.819280,-6.002850,8.126712,3.971529,2.549076,-3.602735,-5.199669,7.068330,7.526434,4.888874,9.995106,2.935991,-5.397160,-3.897711,4.996090,5.847773,-4.176308,-8.936277,5.549541,-4.814604,-6.293565,1.017958,-5.501007,-9.501471,5.831086,-3.574140,-1.531766,-9.706820,-1.995266,1.162838,-0.803389,-3.176270,-3.184394,-2.422949,-1.887468,-8.085682,8.466700,3.121916,4.919905,-5.183843,-9.741885,1.373249,-5.788992,9.018967,-7.855465,-7.809010,9.854963,3.932156,1.544085,7.588533,-4.588440,2.432937,7.547724,8.517180,-6.941557,-6.966486,1.463671,9.463559,0.780173,-5.293671,7.013537,-5.920071,9.601535,-2.015318,-4.936911,-6.459831,-0.286564,-6.165040,-6.900745,-3.859850,6.109085,2.575579,-7.950657,-4.257129,9.186833,8.807651,7.772226,1.679297,0.087201,-6.815246,-9.660162,-5.135525,-4.967890,-1.927335,-1.562006,6.043585,5.173880,-6.539345,1.042373,-7.750099,9.179661,1.129055,4.985821,7.286697,-2.441207,-3.149512,-2.681468,7.937974,-9.860650,-8.613247,-1.925943,-7.856826,-4.369096,4.759361,-4.950929,7.386939,9.631873,-6.524743,2.118024,2.495235,5.774667,-6.482908,-7.504696,-7.900777,-4.266550,-6.843240,-6.012470,-5.679639,0.424216,-7.376426,5.119304,-3.763027,-1.275349,-9.125146,-4.047133,-9.505238,5.780267,-2.468355,-4.407799,-9.789166,7.680131,-7.173434,-7.710193,-1.507785,-9.337107,6.350063,-1.498102,6.886428,-2.876750,5.913429,0.998668,8.094486,-5.726970,2.704043,-0.657554,4.850044,-8.554329,-0.335218,4.602014,-3.945811,6.479811,1.053445,2.596299], dtype = "float64")#candidate|14421|(1080,)|const|float64
const_14422 = relay.const([False,True,False,True,False,True,True,True,False,False,True,False,False,True,False,False,True,False,True,True,True,False,False,False,False,False,True,False,False,True,False,False,False,False,True,False,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,False,False,True,False,False,True,True,True,False,False,True,False,False,True,False,True,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,False,False,False,False,True,True,False,False,True,False,True,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True,False,False,True,False,True,True,False,True,False,True,False,False,True,False,False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,False,True,True,True,True,True,False,False,True,True,False,True,True,False,False,True,True,True,True,False,True,True,False,False,False,False,False,False,False,False,True,False,False,False,True,True,True,True,True,True,False,False,False,False,False,False,True,True,True,True,False,True,False,False,True,False,False,False,True,False,False,False,True,False,True,False,True,False,False,True,True,False,True,True,False,True,False,False,True,True,True,True,False,True,True,False,False,True,False,True,False,False,True,True,True,False,True,False,True,True,True,False,False], dtype = "bool")#candidate|14422|(240,)|const|bool
const_14423 = relay.const([7.805597,0.257980,9.463100,2.433889,-7.074275,-5.103667,-1.001619,1.376101,0.005744,-4.837468,-6.845404,5.929697,-2.517154,7.576917,0.655985,0.971032,2.404295,7.755049,-2.922036,-3.765279,-1.390928,9.045354,-7.848643,9.901633,-1.712696,6.675297,-2.116930,-1.151022,4.086858,6.805477,-3.937807,-7.812651,6.091228,-1.277935,-9.175072,-5.678376,-4.160594,-6.209872,-2.700275,-7.235457,9.944770,3.493125,-3.244225,-3.592920,7.411110,-7.887889,-1.893372,-7.281137,-6.910961,8.462911,8.983712,-2.220317,5.984409,-7.063097,-7.855879,-0.624534,7.863647,7.172950,-3.955783,0.285026,9.825828,6.659799,-4.875607,0.486660,4.918687,-7.281069,-7.401441,-1.337536,5.846337,5.847980,9.139195,1.444854,4.254578,-8.320908,-9.397039,-1.853967,8.005366,1.503149,9.936669,-9.136364,2.089440,9.664820,5.858594,-2.642685,7.965344,-9.438419,4.233686,8.978092,0.395745,-7.636822,6.733750,8.422239,1.023095,4.200323,-8.915211,5.046170,-9.780395,5.705622,-5.905559,-3.911219,-4.051939,-2.688156,-5.220019,-4.084693,9.485534,9.751421,4.696793,8.031417,8.645994,5.609254,-1.676673,0.353249,-0.050297,0.724564,-0.679077,-9.247258,-3.837541,4.869369,-2.903235,-3.035651,-3.612587,-0.264073,2.656080,-0.922447,-2.663842,-0.736021,-3.685731,0.074690,-0.271876,1.298157,-7.349716,8.810402,-5.865344,7.939707,4.147167,-8.079134,1.812173,8.334306,-5.402590,0.967937,-0.712966,-8.626749,-8.766741,8.697899,-1.936274,4.760218,-2.948037,3.070483,5.294068,0.904499,3.095104,7.084990,-9.131097,6.749068,-7.223011,-0.024865,-5.007790,-7.253804,-5.652054,9.595013,-9.394032,-1.020931,-6.318090,-2.722188,-9.387768,-6.979348,8.587583,2.264871,-9.347919,5.388347,9.597198,3.799037,-8.717627,-2.170492,4.074947,2.799805,1.173170,-3.472167,2.404580,0.538220,-5.254974,0.791243,5.811528,-8.925074,3.946088,6.030085,2.975658,-9.873678,-2.569861,-8.437656,1.865300,5.658794,3.368572,-3.112516,-5.338170,7.783956,4.434186,4.686664,5.055807,-3.271239,4.639710,3.926193,0.298873,-5.275336,1.761079,0.614065,-0.741475,6.209903,9.658976,-9.576016,3.697582,-9.418972,8.006620,-4.556390,7.053306,1.871245,-0.481416,4.435476,2.537425,3.359976,1.523163,5.907859,6.041011,4.807570,-9.238413,2.210557,5.157158,-3.930467,0.755752,2.543665,4.250509,2.840575,-9.760927,0.221803,-2.049694,-9.110920,-0.197657,2.803675,-2.359814,-7.705355,-6.159229,-3.798129,2.054439,-4.161087,9.910317,-7.732277,7.404280,-2.207216,-8.316641,0.131517,-0.401350,-7.347054,0.789225,3.283895,5.846823,-9.152623,4.532755,4.836303,9.698827,2.469934,-5.876247,0.698140,5.292573,9.301928,-0.011800,-1.806952,-2.803222,3.971832,-2.762882,3.738931,-0.571946,3.365328,-9.988374,-4.503301,7.914201,1.571107,4.847984,5.478222,-9.008136,6.727699,1.087628,-7.878152,-4.552002,5.180969,-8.551061,-7.905631,-1.250335,-6.749148,7.382501,-0.685788,-2.944772,-4.916369,-2.528501,-6.627121,-1.396684,9.374383,4.780190,0.908133,2.096930,-0.796202,0.148739,-7.956039,-8.359072,-8.769554,-2.473125,-5.774987,-6.367501,-4.782054,-8.797862,-8.316254,-8.203740,-0.874419,4.039838,-2.045385,-0.363937,-7.271131,7.951343,3.193880,8.324881,9.825978,-2.293636,-1.555620,-3.600208,-8.698839,6.816344,4.394016,-6.914635,8.550692,6.854101,7.936428,-0.056048,3.067707,-4.131358,5.899625,3.357517,6.539183,9.313544,-2.809790,9.226823,-5.850579,8.797514,-8.937246,-9.955878,0.519281,1.142936,3.756029,-1.811048,-5.963566,-4.812370,-1.644661,-4.093657,6.489191,8.388765,-0.642077,-1.398905,4.934168,-9.884598,-2.757833,2.707309,0.291500,-2.713646,-7.836270,6.237445,5.662871,6.032128,2.794861,-6.706074,2.934982,9.232839,-3.547458,-9.189579,8.786828,3.515696,3.414966,-3.287723,-2.668450,-6.415927,9.530384,5.861690,9.860467,8.219574,-7.165323,7.349553,9.937555,9.300179,8.768091,-7.487725,0.961256,-3.099130,-4.998278,5.352947,8.740881,-4.525735,6.654645,8.972646,-8.643984,-9.269391,-2.426296,-8.822316,-4.975148,8.424592,8.660814,-4.916233,-9.262660,-9.414182,8.956694,3.455967,2.321139,-3.714904,4.169684,4.218039,-2.582143,-2.768480,5.211994,-0.584058,9.299966,9.855270,4.034974,2.156537,-5.529911,5.631950,5.178680,-6.121014,-9.422621,0.182020,3.297213,2.492159,-4.826925,-7.866179,-2.697736,7.078322,6.201681,-8.343525,0.109844,-9.358134,8.984171,2.396633,-7.257381,0.496064,-1.407246,-0.945923,3.449980,0.455746,4.718528,-7.410374,3.502900,9.997665,-9.811446,0.557807,0.769803,-6.984862,1.441445,0.230728,5.366108,-9.924314,-6.852319,6.421522,-4.059931,0.628321,1.138266,8.629962,-9.553306,5.511785,6.446537,-8.656003,-4.730438,9.916953,-2.828612,3.439524,-9.193880,-2.714551,-0.374974,-1.087964,-7.278455,-1.821592,2.803059,-6.963110,7.274713,7.493122,4.195920,5.276339,-7.088552,1.075400,-3.642344,-8.769099,2.954187,7.470650,1.052254,-7.013800,9.790852,9.498161,2.379324,-8.565390,6.179004,4.347876,1.185328,-8.422167,9.447833,3.504875,-1.447560,-9.772565,-8.571965,5.740179,-3.919889,4.464839,-9.058067,-2.330623,4.296670,-5.767898,-4.729051,4.822080,5.308494,5.334928,0.580495,-5.684426,7.319525,6.833310,-9.485022,0.398746,3.320722,-1.518920,0.242572,7.656844,-1.675008,0.551296,5.780040,-3.635988,-7.693392,1.489438,-1.427043,5.668796,0.032130,8.217969,3.238035,-9.408235,-3.559739,-0.129120,5.413823,-4.580028,-8.726978,9.432736,-6.300818,-1.539644,0.875818,-2.970117,8.067131,5.546070,0.435982,-5.762017,4.774408,6.987511,5.693858,3.574087,7.554887,-7.264660,4.519236,7.920217,-1.086111,-4.716085,7.610052,5.123590,-5.702168,4.856411,-8.870430,-6.415352,-6.242085,1.206320,-4.071827,2.445691,-4.157071,8.187510,7.376200,8.679206,-4.733227,9.073343,-1.158622,-9.605858,-3.543504,-7.750845,3.178834,-4.493272,-3.679174,6.566187,1.283928,-8.004433,8.637588,9.993938,-3.174551,-3.994832,8.612254,3.236192,-4.253179,-3.120707,2.416616,2.719435,-4.355745,2.020294,1.581139,6.130496,6.520296,-4.649159,8.750646,0.152797,-6.494457,-4.273663,8.508387,-4.282174,9.365718,-2.880337,3.649177,0.326926,-0.992928,2.952168,0.980082,-5.676485,-5.709630,8.512894,-8.034666,-3.349315,-7.113272,-8.612887,-6.638057,-1.982620,-3.115879,-8.823199,-5.683527,9.964490,-7.985791,2.279718,6.718708,-6.190964,-0.249414,3.175651,-2.435586,-0.390288,-8.646532,9.244757,9.641332,-2.984461,-3.397531,5.688165,-0.699335,6.007267,5.596016,-7.445814,-5.101358,7.780644,1.462529,-0.832919,-4.386500,-8.032717,6.268880,8.923347,8.760039,-8.033950,-5.222197,3.347832,-8.997953,-3.321789,6.676695,-5.438299,7.178255,-0.966663,-6.028991,6.814760,5.330915,2.678870,4.995291,1.366986,-5.881840,-2.905752,-9.415444,3.987963,7.414158,-6.362990,3.836830,-1.664677,-9.170418,3.195687,6.132664,9.491381,-5.471476,-2.895206,3.188443,9.872119,0.499002,9.984033,5.711509,9.591935,-8.198357,2.176119,-8.212572,-6.233485,-9.164782,-1.713534,-9.370854,8.975117,-3.319538,-9.122889,2.069396,-4.272781,-3.230790,-5.132000,-6.939468,-9.114368,-6.493400,-8.942916,9.264754,5.991208,-2.021800,-3.360873,-8.039418,-6.979956,9.409299,-3.350276,-5.523283,6.804199,-7.806495,-0.731763,0.085269,8.077511,-0.287926,8.128378,9.061637,3.404845,-4.464273,-4.024698,8.216276,7.762606,-3.121480,-0.837565,-8.283074,9.547824,0.525684,-6.769447,-5.403285,-5.584043,8.290749,-9.084909,4.816505,7.767685,7.706110,-0.993992,-2.480264,7.236337,8.870563,5.053167,-0.030704,3.663069,-6.039912,-5.063558,3.886080,1.085561,-1.292705,1.188461,9.215644,8.447536,8.466210,-7.730527,-6.986756,-0.587013,8.329394,4.984499,-3.745105,6.308951,-7.047806,3.786964,5.543254,0.389648,-7.112795,2.738329,9.222296,0.196554,-7.246501,-8.500696,0.126061,-0.145919,-0.682017,-1.297686,-2.670220,0.066272,-9.020631,1.758451,3.045433,7.705894,2.455396,5.639826,-4.649142,2.042495,-9.259871,7.884574,-6.677812,-8.476112,3.176667,2.935193,9.848395,1.020200,1.896252,0.462826,1.642093,6.426726,7.675806,9.871120,4.377229,-2.597772,-2.548191,4.428553,5.651014,8.861863,6.611535,8.380168,0.820848,-5.574707,3.648949,3.746755,-3.254158,8.987881,1.041990,1.330056,-7.038594,4.011178,6.021977,0.370731,-5.488430,-9.561849,-3.284788,-5.496996,-1.214438,-8.847429,-5.272223,-2.156241,-9.269076,-9.278276,-4.163156,-3.394471,8.076914,6.810345,1.727833,-5.659974,5.417000,1.354098,-1.054001,9.047075,-8.038697,-0.179372,0.586965,2.198671,-6.457730,0.484541,-6.780375,3.273788,9.369132,-3.613847,-8.156449,5.080678,5.406062,3.358115,-4.616173,-1.021165,-2.698367,-9.750025,5.176820,-5.190042,6.372611,-4.565003,2.495788,-7.793566,-5.527556,0.073568,4.348377,-0.532439,0.199438,-5.777048,-4.460556,-0.259679,1.662009,-0.465614,5.043721,-5.270470,6.048308,-6.360740,9.413226,8.077247,6.275672,-3.886812,4.665840,-3.968280,-3.901144,9.299327,1.283538,8.003339,-5.206778,-7.933351,-2.936396,-6.286421,7.183814,5.442586,3.210730,8.660237,2.947481,0.683334,-7.527120,-6.029339,-9.296636,-8.606091,6.278765,-0.024613,3.048745,4.433370,-1.688020,4.729377,-3.325791,-6.087784,-1.709530,5.728949,7.052188,-9.170925,-8.832521,-0.638855,-9.851506,-4.588959,-8.827425,6.591190,8.564518,-0.394882,7.627145,-5.035407,-3.690105,9.318041,-3.249602,-8.414491,-4.298425,0.672411,4.078203,3.383816,-5.095855,-8.874385,1.823978,4.450353,-4.545331,-3.414787,2.573043,-5.252543,4.750891,-9.669237,-8.471261,4.597008,-6.875824,5.038568,-3.723901,8.863747,-9.274804,7.837243,-7.947648,9.915466,-3.478710,-7.639698,-6.298811,4.113949,-0.605345,7.400588,8.044124,9.948053,8.673586,7.135288,-7.077226,7.524604,-4.008379,-1.495839,0.198697,-6.085277,8.407985,3.231997,4.668467,6.950584,5.986749,-7.819854,7.990405,-7.904392,-7.850193,-8.058207,-5.992230,5.125415,-6.469153,2.545766,2.758209,-0.884437,-1.876028,-0.444366,-5.298864,-0.464082,-7.035676,-8.187495,-1.308216,2.892676,1.260966,0.469675,2.079644,-7.502470,-5.827409,4.916825,3.411137,-3.748693,4.241419,4.842930,-0.060237,8.037403,-8.703703,-2.119664,-2.325654,3.941771,7.778273,-5.703269,-7.125749,8.586208,-3.084484,-1.332709,-7.676082,-1.576788,-1.913741,6.823058,4.393043,6.007904,5.067773,-3.883625,3.603998,1.034124,3.269770,9.786946,-7.723018,-1.158133,7.319064,9.388913,-9.226073,-5.621255,6.731342,6.885107,-2.426342,2.009250,3.104098,-6.041359,2.357165,8.104982,0.571418,-2.786089,9.004877,-0.893143,-8.327345,-4.716087,7.329693,7.131005,3.011294,7.420974,4.055560,1.883820,1.828232,-4.787529,0.462938,3.373777,-1.747478,-5.099539,-9.187367,6.254427,-0.504851,0.125092,-6.419332,1.389839,-9.859537,0.939948,3.086729,-1.031340,-3.686172,1.333911,-6.704136,-4.140786,4.565930,2.647971,-1.703396,-9.016508,-6.775899,-4.674328,-6.464928,-6.493554,4.937427,-6.694889,-9.501650,2.169368,7.041348,-0.142052,2.146619,7.902351,-0.559807,-2.992319,8.753716,2.529771,6.785194,-9.955776,9.658269,-3.041992,-4.735354,8.061055,4.644901,-2.074365,-5.960348,-7.960576,7.084801,-3.114052,-9.961229,-7.168088,9.759314,-1.514294,-0.118351,-6.970724,9.529025,-1.228305,8.412486,5.101891,-2.538039,-0.032712,-8.198420,-0.530441,-7.323874,3.764971,0.116032,-2.148145,-7.179814,6.737572,2.305231,-7.263008,-8.637662,-1.650603,8.975703,-6.927066,9.019386,-2.018284,-1.464751,-5.056037,0.293093,9.759732,2.918030,7.761396,-3.126441,-6.462713,-5.474906,8.940131,7.061588,-3.027210,9.354680,-1.810712,9.799746,-7.997658,3.143784,-0.686556,1.480972,-2.291090,7.195250,-5.320881,-4.277653,0.235852,4.093693,-9.398103,3.163497,5.853363,0.307748,5.012069,-5.340948,-3.293227,-7.953567,-4.276401,6.631586,9.040531,-3.233581,-3.140702,-3.931084,0.945850,-8.264806,3.685981,7.675923,-3.668909,-8.348142,5.155132,-3.697984,6.349397,0.297722,-5.474092,-2.319770,2.367819,9.266460,8.094205,-4.342059,1.104359,-2.098635,-0.127870,-3.026890,2.512602,-7.812666,6.952124,-9.653970,-5.963147,2.387380,-2.000515,-7.248702,-2.053144,-8.567254,8.735669,2.362318,0.224764,0.127456,0.977520,9.947869,7.898094,3.645740,-4.517050,7.309604,0.182074,5.503626,-6.776110,-0.373452,2.152875,-0.818439,9.533822,9.926419,-4.931124,-3.963823,-0.750761,-1.885916,7.008608,3.247101,9.738375,-8.383450,1.035694,3.892128,2.085376,-2.643658,-4.371776,-2.633753,-9.134386,-3.998893,-9.703317,-8.553610,-5.733578,-0.362790,6.904278,7.006747,-6.913616,5.429805,5.448224,5.762926,-7.183917,5.718241,9.317835,-3.528334,-4.090697,-2.430523,7.020690,4.005489,1.435320,-0.184996,3.588613,5.868366,7.025324,2.535810,6.676191,-0.447381,6.036740,-6.697454,3.641777,-5.025478,-1.807000,-4.056794,-2.332674,2.669586,-8.904182,-5.730869,-4.423882,8.410322,-9.415212,-9.329510,-3.122668,-1.176991,7.902023,-2.380765,2.429776,-4.133570,3.701133,-3.384759,-9.861564,0.399413,0.341208,9.848516,1.037817,6.612114,0.088693,-8.916710,-7.642711,0.469321,4.005386,-9.788718,3.110084,-3.801953,-0.452191,-4.527200,7.087494,0.483418,7.813386,-4.068101,4.999466,-1.717477,2.297740,-6.197424,4.966660,2.743654,1.254144,-6.138984,-6.091617,7.177062,7.201529,-7.211289,6.577614,5.808771,-0.194344,-4.517901,2.314625,-1.697244,3.417767,5.121020,5.759667,8.659219,-3.783145,8.325844,9.771004,7.496266,-6.238532,0.492550,6.209407,-0.299068,-5.993107,-3.796829,8.687246,-1.177373,1.477826,-5.615630,4.393933,-8.091194,4.293127,-6.320068,-1.205185,6.439545,1.997791,8.684962], dtype = "float64")#candidate|14423|(1350,)|const|float64
call_14420 = relay.TupleGetItem(func_10957_call(relay.reshape(const_14421.astype('float64'), [1080,]), relay.reshape(const_14422.astype('bool'), [6, 10, 4]), relay.reshape(const_14423.astype('float64'), [1350,]), ), 1)
call_14424 = relay.TupleGetItem(func_10961_call(relay.reshape(const_14421.astype('float64'), [1080,]), relay.reshape(const_14422.astype('bool'), [6, 10, 4]), relay.reshape(const_14423.astype('float64'), [1350,]), ), 1)
output = relay.Tuple([call_14389,call_14410,var_14411,var_14412,var_14413,call_14420,const_14421,const_14422,const_14423,])
output2 = relay.Tuple([call_14390,call_14414,var_14411,var_14412,var_14413,call_14424,const_14421,const_14422,const_14423,])
func_14425 = relay.Function([var_14411,var_14412,var_14413,], output)
mod['func_14425'] = func_14425
mod = relay.transform.InferType()(mod)
var_14426 = relay.var("var_14426", dtype = "int16", shape = (1, 312))#candidate|14426|(1, 312)|var|int16
var_14427 = relay.var("var_14427", dtype = "bool", shape = (315,))#candidate|14427|(315,)|var|bool
var_14428 = relay.var("var_14428", dtype = "float32", shape = (5, 156))#candidate|14428|(5, 156)|var|float32
output = func_14425(var_14426,var_14427,var_14428,)
func_14429 = relay.Function([var_14426,var_14427,var_14428,], output)
mutated_mod['func_14429'] = func_14429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9394_call = mod.get_global_var('func_9394')
func_9396_call = mutated_mod.get_global_var('func_9396')
call_14483 = relay.TupleGetItem(func_9394_call(), 0)
call_14484 = relay.TupleGetItem(func_9396_call(), 0)
output = relay.Tuple([call_14483,])
output2 = relay.Tuple([call_14484,])
func_14501 = relay.Function([], output)
mod['func_14501'] = func_14501
mod = relay.transform.InferType()(mod)
output = func_14501()
func_14502 = relay.Function([], output)
mutated_mod['func_14502'] = func_14502
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14514 = relay.var("var_14514", dtype = "float32", shape = (10, 5, 1))#candidate|14514|(10, 5, 1)|var|float32
const_14515 = relay.const([[[-5.219054,4.738449,-3.832909,-9.546109,7.241278,-9.606250,9.015787],[-9.569384,-4.973731,-8.169894,5.832866,3.173672,0.674780,1.796762],[-4.128320,-5.461795,-8.337999,-3.738661,-8.976101,3.960191,8.694780],[-0.178036,1.307621,-2.187092,6.239078,-5.677417,-7.149466,6.423989],[-3.909336,-6.168914,0.665630,9.618277,-2.086269,2.260225,2.096306]],[[-2.995886,-7.485491,0.639632,-6.954030,8.198783,8.844720,-8.155363],[3.993743,0.740698,6.420646,-7.064152,-0.102110,-9.343875,-8.447768],[3.167365,-4.953128,-0.864583,-8.244569,-5.524290,9.379951,-6.748887],[8.807508,-0.038476,6.737997,-9.069188,2.577413,5.314615,5.918911],[-2.475541,5.830323,8.202700,-9.926983,5.876256,9.576467,8.772997]],[[4.734519,2.349838,-1.685802,-2.984622,7.914238,-4.267235,8.779070],[-9.122124,4.978907,-7.075210,3.156612,-6.740068,0.468490,-4.493040],[6.691145,3.248427,-2.936609,4.431801,-7.268528,-5.597084,4.404806],[-0.255553,-5.383539,7.807674,-0.567076,3.249686,7.390869,9.778630],[3.599763,7.520590,8.496222,8.885856,-6.456020,-2.858088,-7.771574]],[[-9.027616,-2.661729,0.235078,-9.059856,-6.194234,-9.156089,-9.175268],[-1.086417,7.278673,3.662498,-6.581844,4.060765,-9.508000,0.227469],[4.550239,3.857536,0.369322,-8.583037,0.670613,4.970390,4.420678],[4.544039,6.410310,8.674996,4.320767,3.102994,1.200474,2.123070],[-8.767520,2.883998,3.134998,-9.980735,-5.254102,2.672130,9.969557]],[[5.324379,-8.690217,-5.739909,-8.338569,-1.325006,-0.358490,-4.917067],[2.037936,-9.443865,-7.300973,5.647834,-4.717734,-9.836666,-8.218945],[-3.239646,-7.855982,0.184910,-8.031182,-1.506532,0.142757,-4.411771],[-6.467059,-0.200246,0.368074,-6.591325,-6.595350,0.367317,4.074722],[5.543001,5.606490,9.489229,0.169759,-2.366055,-4.294397,3.385507]],[[-7.028935,8.535553,-0.437611,-1.068852,-4.075584,1.000442,-2.798790],[-6.192374,-7.396352,7.593865,8.903499,5.302564,1.363965,9.346397],[-7.944198,-6.241440,-2.819037,9.187692,0.958844,-9.589639,-8.058558],[-4.188013,-1.128193,-6.448916,-9.766952,-7.625195,-7.900477,-8.917712],[-7.464175,3.109643,-5.553678,7.859139,-7.743524,0.241816,-2.636516]],[[6.058671,5.364505,5.990079,-5.245990,-4.455392,3.119349,3.770941],[-5.784620,-5.005432,7.253724,8.689343,8.732802,-3.614156,-2.816467],[6.216445,-2.758625,1.117554,-0.149881,5.959626,6.127722,4.855178],[8.210632,-4.806027,-2.883760,-1.326584,0.353322,-4.929282,-1.385791],[-3.385694,-8.133362,7.318322,-0.486518,6.566579,5.487677,-4.292151]],[[-3.264320,4.495287,-5.927459,-8.891565,-8.186719,-6.334660,-1.173574],[-1.424029,7.708689,5.181206,-5.566853,-2.306823,-9.802289,7.649331],[6.756006,-1.305556,0.788813,8.436592,8.362546,1.229760,-4.314474],[8.815892,-2.169667,6.775138,-7.364518,6.873115,1.903664,-1.259697],[6.418763,1.001436,3.044572,1.807740,1.195504,-6.532205,-4.650745]],[[1.439193,5.384366,7.781640,-4.378179,7.445198,-3.355930,-3.614544],[0.463100,2.183088,-7.670129,1.082992,-6.154006,5.676245,3.941712],[-1.412253,7.255709,-6.942877,5.383648,-7.356912,-8.243271,-9.130944],[-1.745474,-3.893406,1.815071,9.341569,-4.512289,7.196862,2.692117],[-3.583204,-9.165350,-9.993174,-6.616934,-0.890531,-1.807193,-0.501882]],[[5.726559,8.312048,5.404040,4.340956,9.030630,-9.802110,6.483850],[-3.359624,-9.310388,8.524254,-3.021149,-7.168625,-9.426829,-0.443222],[0.306821,8.815044,0.019657,7.133926,-7.481879,-5.967902,8.897445],[8.266648,-6.250613,0.124992,-2.207081,-7.508211,-2.906764,-2.873779],[0.637775,4.078212,6.682072,1.978501,-5.979588,1.010514,4.725895]]], dtype = "float32")#candidate|14515|(10, 5, 7)|const|float32
bop_14516 = relay.add(var_14514.astype('float32'), const_14515.astype('float32')) # shape=(10, 5, 7)
func_8413_call = mod.get_global_var('func_8413')
func_8415_call = mutated_mod.get_global_var('func_8415')
call_14524 = relay.TupleGetItem(func_8413_call(), 0)
call_14525 = relay.TupleGetItem(func_8415_call(), 0)
func_1815_call = mod.get_global_var('func_1815')
func_1817_call = mutated_mod.get_global_var('func_1817')
const_14529 = relay.const(False, dtype = "bool")#candidate|14529|()|const|bool
call_14528 = func_1815_call(relay.reshape(const_14529.astype('bool'), []))
call_14530 = func_1815_call(relay.reshape(const_14529.astype('bool'), []))
output = relay.Tuple([bop_14516,call_14524,call_14528,const_14529,])
output2 = relay.Tuple([bop_14516,call_14525,call_14530,const_14529,])
func_14541 = relay.Function([var_14514,], output)
mod['func_14541'] = func_14541
mod = relay.transform.InferType()(mod)
var_14542 = relay.var("var_14542", dtype = "float32", shape = (10, 5, 1))#candidate|14542|(10, 5, 1)|var|float32
output = func_14541(var_14542)
func_14543 = relay.Function([var_14542], output)
mutated_mod['func_14543'] = func_14543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9394_call = mod.get_global_var('func_9394')
func_9396_call = mutated_mod.get_global_var('func_9396')
call_14563 = relay.TupleGetItem(func_9394_call(), 0)
call_14564 = relay.TupleGetItem(func_9396_call(), 0)
output = call_14563
output2 = call_14564
func_14569 = relay.Function([], output)
mod['func_14569'] = func_14569
mod = relay.transform.InferType()(mod)
mutated_mod['func_14569'] = func_14569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14569_call = mutated_mod.get_global_var('func_14569')
call_14570 = func_14569_call()
output = call_14570
func_14571 = relay.Function([], output)
mutated_mod['func_14571'] = func_14571
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14621 = relay.var("var_14621", dtype = "float64", shape = ())#candidate|14621|()|var|float64
var_14622 = relay.var("var_14622", dtype = "float64", shape = (6, 7, 16))#candidate|14622|(6, 7, 16)|var|float64
bop_14623 = relay.mod(var_14621.astype('float64'), var_14622.astype('float64')) # shape=(6, 7, 16)
output = bop_14623
output2 = bop_14623
F = relay.Function([var_14621,var_14622,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_14621,var_14622,], output2)
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
