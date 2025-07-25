import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_4 = relay.var("var_4", dtype = "int32", shape = (3, 2, 10))#candidate|4|(3, 2, 10)|var|int32
var_5 = relay.var("var_5", dtype = "int32", shape = (3, 2, 10))#candidate|5|(3, 2, 10)|var|int32
bop_6 = relay.add(var_4.astype('int32'), relay.reshape(var_5.astype('int32'), relay.shape_of(var_4))) # shape=(3, 2, 10)
output = bop_6
output2 = bop_6
func_10 = relay.Function([var_4,var_5,], output)
mod['func_10'] = func_10
mod = relay.transform.InferType()(mod)
var_11 = relay.var("var_11", dtype = "int32", shape = (3, 2, 10))#candidate|11|(3, 2, 10)|var|int32
var_12 = relay.var("var_12", dtype = "int32", shape = (3, 2, 10))#candidate|12|(3, 2, 10)|var|int32
output = func_10(var_11,var_12,)
func_13 = relay.Function([var_11,var_12,], output)
mutated_mod['func_13'] = func_13
mutated_mod = relay.transform.InferType()(mutated_mod)
var_158 = relay.var("var_158", dtype = "uint8", shape = (3, 9, 14))#candidate|158|(3, 9, 14)|var|uint8
const_159 = relay.const([[[10,-8,-7,-1,8,-2,-1,3,7,-2,-8,-9,-9,10],[10,1,5,9,6,7,-9,7,7,10,6,6,9,6],[6,2,-7,-8,-6,6,-6,6,-5,-7,-2,6,-1,2],[10,7,-4,-4,4,5,6,10,6,9,-8,4,5,8],[4,5,-9,-2,1,-6,-5,-7,-2,-6,4,2,4,-1],[-7,7,2,7,-4,2,4,-4,-9,-1,7,-3,-3,-4],[2,9,8,-3,6,10,1,-7,2,-6,-2,3,-6,-4],[-3,7,-6,7,10,6,1,10,-10,9,-10,-4,-3,4],[5,-8,8,6,-4,10,4,-2,2,9,10,-5,-6,-3]],[[-7,-10,-6,-3,-6,10,3,-3,-8,3,8,-1,3,-9],[4,-8,2,5,6,4,-8,-1,-6,9,-1,3,6,8],[-1,-8,10,6,-4,1,9,-4,-2,8,-1,-2,-1,2],[1,5,-8,7,-9,-1,5,2,9,-1,-3,9,-7,-6],[7,4,-9,-10,-3,6,-9,6,-1,8,-6,-3,7,5],[-4,-2,1,9,-8,9,-3,5,4,-7,-10,6,-3,7],[10,6,2,-7,6,5,4,-5,-8,2,-2,8,-2,-9],[5,5,-7,1,10,4,-5,-10,-10,-7,-7,-4,-6,10],[9,4,-7,-1,-1,6,2,7,-7,-4,4,-9,10,8]],[[6,-5,9,-10,10,3,-4,1,10,-1,7,-6,-9,-9],[-8,7,7,2,-3,6,-4,3,9,3,-3,6,4,-10],[9,-5,8,-5,-6,-3,-7,-2,-8,-10,10,6,-2,5],[6,-10,-5,-4,-9,-8,-5,-3,7,-5,10,-2,1,-6],[-2,-10,8,-5,-6,-8,9,-9,-6,-7,8,10,9,8],[9,2,7,-2,-3,8,8,-4,1,-1,4,1,-2,-9],[2,3,-1,5,-9,3,-3,-9,8,-6,-7,-7,7,-2],[-9,-1,10,4,-9,1,5,-9,-8,7,-2,-6,-2,-1],[-3,9,5,4,-6,-7,5,-4,-4,7,1,-10,9,-3]]], dtype = "uint8")#candidate|159|(3, 9, 14)|const|uint8
bop_160 = relay.bitwise_and(var_158.astype('uint8'), relay.reshape(const_159.astype('uint8'), relay.shape_of(var_158))) # shape=(3, 9, 14)
func_10_call = mod.get_global_var('func_10')
func_13_call = mutated_mod.get_global_var('func_13')
const_174 = relay.const([-1,1,6,8,-6,5,-10,9,4,7,4,-8,-10,-3,8,6,-5,-1,-2,9,4,8,-6,3,2,-2,1,7,2,-10,8,-2,-3,-5,2,3,-1,1,9,7,-6,-6,-1,-8,-2,5,-6,-4,8,2,-7,-7,7,6,-3,-5,-6,-6,7,9], dtype = "int32")#candidate|174|(60,)|const|int32
call_173 = func_10_call(relay.reshape(const_174.astype('int32'), [3, 2, 10]), relay.reshape(const_174.astype('int32'), [3, 2, 10]), )
call_175 = func_10_call(relay.reshape(const_174.astype('int32'), [3, 2, 10]), relay.reshape(const_174.astype('int32'), [3, 2, 10]), )
var_179 = relay.var("var_179", dtype = "int32", shape = (3, 2, 10))#candidate|179|(3, 2, 10)|var|int32
bop_180 = relay.less(call_173.astype('bool'), relay.reshape(var_179.astype('bool'), relay.shape_of(call_173))) # shape=(3, 2, 10)
bop_183 = relay.less(call_175.astype('bool'), relay.reshape(var_179.astype('bool'), relay.shape_of(call_175))) # shape=(3, 2, 10)
func_10_call = mod.get_global_var('func_10')
func_13_call = mutated_mod.get_global_var('func_13')
call_186 = func_10_call(relay.reshape(const_174.astype('int32'), [3, 2, 10]), relay.reshape(var_179.astype('int32'), [3, 2, 10]), )
call_187 = func_10_call(relay.reshape(const_174.astype('int32'), [3, 2, 10]), relay.reshape(var_179.astype('int32'), [3, 2, 10]), )
uop_190 = relay.rsqrt(bop_160.astype('float64')) # shape=(3, 9, 14)
func_10_call = mod.get_global_var('func_10')
func_13_call = mutated_mod.get_global_var('func_13')
call_195 = func_10_call(relay.reshape(call_186.astype('int32'), [3, 2, 10]), relay.reshape(bop_180.astype('int32'), [3, 2, 10]), )
call_196 = func_10_call(relay.reshape(call_186.astype('int32'), [3, 2, 10]), relay.reshape(bop_180.astype('int32'), [3, 2, 10]), )
output = relay.Tuple([const_174,bop_180,call_186,uop_190,call_195,])
output2 = relay.Tuple([const_174,bop_183,call_187,uop_190,call_196,])
func_206 = relay.Function([var_158,var_179,], output)
mod['func_206'] = func_206
mod = relay.transform.InferType()(mod)
mutated_mod['func_206'] = func_206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_206_call = mutated_mod.get_global_var('func_206')
var_208 = relay.var("var_208", dtype = "uint8", shape = (3, 9, 14))#candidate|208|(3, 9, 14)|var|uint8
var_209 = relay.var("var_209", dtype = "int32", shape = (3, 2, 10))#candidate|209|(3, 2, 10)|var|int32
call_207 = func_206_call(var_208,var_209,)
output = call_207
func_210 = relay.Function([var_208,var_209,], output)
mutated_mod['func_210'] = func_210
mutated_mod = relay.transform.InferType()(mutated_mod)
var_823 = relay.var("var_823", dtype = "int16", shape = ())#candidate|823|()|var|int16
const_824 = relay.const([[[-1,1,10,-1,3],[5,7,-9,-2,6],[6,-10,-4,10,-2],[-3,-5,-10,-4,-2],[-4,4,-10,-4,6],[4,-4,7,-3,-9],[1,9,-6,1,-9],[7,-1,-5,-4,5],[2,5,4,-3,10],[-3,4,7,8,-2],[-2,-2,-1,-5,-7],[6,10,5,-5,10],[-10,8,-4,8,2]],[[10,-10,-10,9,-6],[6,10,-5,-7,-5],[8,9,-1,-1,-4],[10,9,-6,1,-2],[6,8,3,10,6],[8,-1,9,9,-3],[-3,9,-5,10,-2],[10,2,3,5,-7],[9,4,4,1,3],[8,-1,9,2,9],[-4,4,-10,3,-10],[-4,-8,8,4,-5],[5,5,10,1,5]],[[-10,10,-5,10,-4],[8,1,10,8,-9],[3,8,-2,-5,-4],[3,-7,9,3,-8],[2,-7,-4,2,-1],[6,-5,-5,7,-9],[8,7,5,7,-5],[-5,5,-10,8,-10],[3,6,-2,-4,-1],[-2,-7,6,2,9],[10,-6,7,1,-10],[-8,-9,-10,5,2],[10,-5,-10,8,4]],[[-1,3,-7,-5,-8],[1,9,-10,3,-4],[-1,6,1,5,-1],[-9,3,-2,-6,1],[6,-10,4,-4,5],[-1,-4,2,-6,-7],[8,-1,-9,1,4],[9,-8,2,1,8],[-4,4,-9,-3,3],[-1,-5,-2,-5,-2],[-9,-6,-2,-8,6],[2,-6,-10,-3,9],[5,9,-10,6,5]],[[6,-1,-10,3,-7],[-5,-1,-7,7,3],[8,-4,8,9,3],[4,-8,2,-7,6],[-5,4,4,-8,9],[-5,-9,-5,6,5],[-8,9,-1,3,-9],[3,-2,2,6,6],[-1,-4,3,9,1],[-9,2,-4,10,-2],[-8,2,10,7,4],[-1,6,5,-5,9],[10,-7,-5,-5,8]],[[-3,-2,10,9,-8],[-3,-5,-8,-8,-7],[-1,4,-9,-8,-5],[4,7,-3,10,4],[-6,-8,-6,3,1],[1,-7,9,6,-10],[6,-9,2,9,5],[-9,-10,1,-5,-2],[-4,-8,1,-7,-7],[-8,-5,-5,10,-8],[-9,7,5,-9,-4],[-9,-5,-1,4,-3],[-9,1,9,-10,4]],[[-5,6,-6,10,3],[6,4,9,-10,-7],[2,-6,-7,-3,-6],[-6,1,5,-5,3],[-10,-2,-4,4,-1],[-7,-5,6,-1,-3],[-5,10,-1,3,9],[-3,-7,-7,-5,-3],[10,-9,-4,-8,-5],[2,10,-6,-6,-6],[-5,7,-4,-2,-3],[-7,-6,9,3,-7],[-8,10,2,6,7]],[[4,-1,-3,-7,-7],[-10,3,-1,6,-10],[4,-1,-6,10,-10],[6,-8,-8,3,6],[6,-2,-3,-3,-9],[-3,1,-7,6,10],[2,-3,2,-1,-7],[-5,-6,1,-2,-8],[7,5,-5,8,-8],[1,-4,-10,6,-1],[2,-7,5,-8,4],[9,9,-1,4,8],[-8,4,3,-8,7]],[[3,7,8,8,8],[-1,-5,-1,-5,-8],[1,-1,-7,8,3],[-7,5,-8,6,8],[-10,-3,1,3,-2],[-8,6,5,6,-1],[9,7,3,-8,1],[-5,4,6,-3,-1],[10,8,-1,-9,8],[-5,-1,-2,8,-5],[5,2,7,5,8],[5,-7,4,-7,6],[7,2,-6,2,6]],[[6,9,-1,7,8],[-3,-5,-7,-10,-4],[-8,10,6,-8,-1],[-8,-6,-5,3,4],[-9,-4,7,1,-6],[8,3,5,5,10],[10,2,-4,2,1],[9,-2,2,6,1],[-10,5,-6,-5,-6],[8,6,1,-9,9],[8,1,5,-1,9],[-1,10,4,-6,8],[5,-9,6,-1,4]],[[6,-2,-4,-10,-5],[7,-8,2,5,-1],[4,-7,-7,3,-9],[-1,-9,-9,7,-7],[8,10,1,10,-2],[8,-6,-10,-9,4],[10,-10,6,3,1],[-8,4,-9,-2,2],[7,-1,-7,8,4],[2,7,4,-5,9],[-6,9,6,4,4],[-1,8,-5,-1,-10],[7,8,8,-7,10]],[[1,6,-4,5,-10],[8,1,5,10,1],[2,4,3,-3,-4],[-8,-7,-2,-9,-2],[7,2,5,-6,-5],[7,-6,-7,-2,9],[5,1,-4,-6,-2],[-1,8,7,-1,10],[-9,-3,-7,-3,-3],[5,10,2,8,6],[-4,-9,10,-8,8],[-7,5,1,10,-1],[8,3,-3,-3,-10]],[[-1,4,7,-5,-5],[2,-9,3,9,5],[8,-7,1,-3,10],[-1,-8,-2,-1,1],[-9,1,10,-5,-7],[8,-4,-4,4,9],[-1,-9,-9,5,8],[-9,8,3,2,-6],[10,6,-10,1,8],[-10,-2,9,7,-3],[-1,-10,-2,9,-2],[-5,-1,-6,-1,-3],[-9,-9,1,4,1]],[[3,-10,1,7,-6],[-4,-1,3,-4,-6],[-3,-1,8,2,9],[9,-5,6,-1,-7],[2,-1,8,2,-8],[2,-5,-6,4,5],[9,-5,5,4,4],[4,-5,-1,-8,-7],[-5,-8,2,3,9],[-9,-4,-5,-6,2],[10,-6,-2,10,-1],[-8,5,-7,9,-3],[10,7,6,10,2]],[[-2,1,-1,-6,-4],[-7,-3,6,9,2],[4,-6,5,-6,4],[6,-2,5,-9,-4],[9,-5,4,-4,9],[-7,-7,3,-4,6],[6,-3,10,-4,8],[4,-9,-10,2,-8],[-2,-3,9,-1,-4],[-1,3,-3,-4,4],[4,1,-8,-6,7],[-9,-10,-7,8,-2],[-9,7,10,4,6]],[[8,-5,5,4,-4],[-7,9,5,4,6],[-10,-10,-6,6,6],[8,-3,-5,-8,10],[-9,5,2,-3,-7],[-4,-5,-1,-7,-3],[-10,7,7,10,10],[-7,6,-6,-6,-7],[-2,-8,-7,10,-8],[5,5,1,-3,-7],[-10,-3,-8,5,1],[-5,-2,10,3,-3],[4,-1,1,8,1]]], dtype = "int16")#candidate|824|(16, 13, 5)|const|int16
bop_825 = relay.add(var_823.astype('int16'), const_824.astype('int16')) # shape=(16, 13, 5)
func_10_call = mod.get_global_var('func_10')
func_13_call = mutated_mod.get_global_var('func_13')
var_831 = relay.var("var_831", dtype = "int32", shape = (60,))#candidate|831|(60,)|var|int32
call_830 = func_10_call(relay.reshape(var_831.astype('int32'), [3, 2, 10]), relay.reshape(var_831.astype('int32'), [3, 2, 10]), )
call_832 = func_10_call(relay.reshape(var_831.astype('int32'), [3, 2, 10]), relay.reshape(var_831.astype('int32'), [3, 2, 10]), )
output = relay.Tuple([bop_825,call_830,var_831,])
output2 = relay.Tuple([bop_825,call_832,var_831,])
func_852 = relay.Function([var_823,var_831,], output)
mod['func_852'] = func_852
mod = relay.transform.InferType()(mod)
var_853 = relay.var("var_853", dtype = "int16", shape = ())#candidate|853|()|var|int16
var_854 = relay.var("var_854", dtype = "int32", shape = (60,))#candidate|854|(60,)|var|int32
output = func_852(var_853,var_854,)
func_855 = relay.Function([var_853,var_854,], output)
mutated_mod['func_855'] = func_855
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1141 = relay.var("var_1141", dtype = "float64", shape = (3, 4, 16))#candidate|1141|(3, 4, 16)|var|float64
uop_1142 = relay.asin(var_1141.astype('float64')) # shape=(3, 4, 16)
output = uop_1142
output2 = uop_1142
func_1144 = relay.Function([var_1141,], output)
mod['func_1144'] = func_1144
mod = relay.transform.InferType()(mod)
mutated_mod['func_1144'] = func_1144
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1145 = relay.var("var_1145", dtype = "float64", shape = (3, 4, 16))#candidate|1145|(3, 4, 16)|var|float64
func_1144_call = mutated_mod.get_global_var('func_1144')
call_1146 = func_1144_call(var_1145)
output = call_1146
func_1147 = relay.Function([var_1145], output)
mutated_mod['func_1147'] = func_1147
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1314 = relay.var("var_1314", dtype = "int8", shape = (11, 8, 16))#candidate|1314|(11, 8, 16)|var|int8
var_1315 = relay.var("var_1315", dtype = "int8", shape = (11, 8, 16))#candidate|1315|(11, 8, 16)|var|int8
bop_1316 = relay.bitwise_xor(var_1314.astype('int8'), relay.reshape(var_1315.astype('int8'), relay.shape_of(var_1314))) # shape=(11, 8, 16)
uop_1341 = relay.rsqrt(var_1314.astype('float64')) # shape=(11, 8, 16)
func_1144_call = mod.get_global_var('func_1144')
func_1147_call = mutated_mod.get_global_var('func_1147')
const_1345 = relay.const([[-1.096172,9.932238,-8.217633,-5.984092,-6.238151,-2.380251,-6.302353,-4.167715,-9.836646,3.061892,5.098353,-0.379978,7.387605,7.716133,0.911572,-0.040394,-7.441559,0.309167,0.803823,1.120663,1.132193,7.940286,-7.090284,-1.847316,6.219913,-8.440661,7.077152,3.154300,-5.501070,-1.427614,-4.840911,3.608274,-1.301811,2.612141,2.920864,-2.909856,8.874392,-0.130168,9.460208,-2.821434,-6.633244,-7.498855,7.365974,-3.592616,-7.725075,9.031722,6.854235,-8.844546,-1.622509,-6.107140,-7.090313,-5.944328,-4.961351,-7.932258,8.656645,-1.682700,7.670351,1.628961,-3.744104,-7.128493,2.653846,-4.095155,9.479432,-4.513245,-9.482054,2.569587,8.197330,-1.686839,-4.741369,-4.894036,-8.950761,6.203812,9.475138,-9.858963,-8.815344,-0.716162,3.499859,-8.977305,9.994615,-3.170248,9.430508,3.252990,7.627020,-9.364894,-8.067481,3.958834,-0.179956,-7.619536,9.787655,3.740410,2.642519,5.974419,-3.748324,1.866772,4.574637,-2.461698],[0.085844,9.265088,7.718958,-7.395073,-1.941288,-5.796875,-1.643141,-5.443133,-1.347830,1.786216,-6.180127,-5.323612,1.871550,-3.298719,3.154314,7.699513,-2.819393,8.942628,2.089684,9.142475,4.389852,-0.068623,-6.736725,6.858462,-8.901713,4.373431,-4.519921,-4.151789,4.244029,-9.673686,3.471066,-4.588246,-8.905956,1.794211,3.725006,-6.504622,0.399289,5.826405,8.551019,-6.184177,1.551403,-4.717391,3.099029,7.158717,-9.910766,1.404670,-2.349635,0.652903,7.119547,-9.410771,-1.806639,4.549103,6.132968,0.042657,9.579992,-4.088647,3.950801,-5.386216,4.118794,-0.051918,7.128949,3.033467,1.339182,4.852830,-7.429367,4.385147,-5.653264,-0.198965,0.677373,-0.616082,5.918731,-2.242497,-3.814515,1.245380,-1.094994,2.837585,7.524908,3.024661,2.888497,3.826847,-2.698174,-6.583798,6.965300,-5.884128,7.679993,6.600074,-0.042694,1.201037,8.436459,-9.855584,-5.101848,3.652896,6.731690,-2.615766,2.578634,-1.580033]], dtype = "float64")#candidate|1345|(2, 96)|const|float64
call_1344 = func_1144_call(relay.reshape(const_1345.astype('float64'), [3, 4, 16]))
call_1346 = func_1144_call(relay.reshape(const_1345.astype('float64'), [3, 4, 16]))
output = relay.Tuple([bop_1316,uop_1341,call_1344,const_1345,])
output2 = relay.Tuple([bop_1316,uop_1341,call_1346,const_1345,])
func_1356 = relay.Function([var_1314,var_1315,], output)
mod['func_1356'] = func_1356
mod = relay.transform.InferType()(mod)
mutated_mod['func_1356'] = func_1356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1356_call = mutated_mod.get_global_var('func_1356')
var_1358 = relay.var("var_1358", dtype = "int8", shape = (11, 8, 16))#candidate|1358|(11, 8, 16)|var|int8
var_1359 = relay.var("var_1359", dtype = "int8", shape = (11, 8, 16))#candidate|1359|(11, 8, 16)|var|int8
call_1357 = func_1356_call(var_1358,var_1359,)
output = call_1357
func_1360 = relay.Function([var_1358,var_1359,], output)
mutated_mod['func_1360'] = func_1360
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1382 = relay.const(False, dtype = "bool")#candidate|1382|()|const|bool
var_1383 = relay.var("var_1383", dtype = "bool", shape = (16, 7, 1))#candidate|1383|(16, 7, 1)|var|bool
bop_1384 = relay.logical_or(const_1382.astype('bool'), var_1383.astype('bool')) # shape=(16, 7, 1)
bop_1393 = relay.bitwise_xor(var_1383.astype('uint64'), relay.reshape(bop_1384.astype('uint64'), relay.shape_of(var_1383))) # shape=(16, 7, 1)
output = relay.Tuple([bop_1393,])
output2 = relay.Tuple([bop_1393,])
func_1396 = relay.Function([var_1383,], output)
mod['func_1396'] = func_1396
mod = relay.transform.InferType()(mod)
mutated_mod['func_1396'] = func_1396
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1397 = relay.var("var_1397", dtype = "bool", shape = (16, 7, 1))#candidate|1397|(16, 7, 1)|var|bool
func_1396_call = mutated_mod.get_global_var('func_1396')
call_1398 = func_1396_call(var_1397)
output = call_1398
func_1399 = relay.Function([var_1397], output)
mutated_mod['func_1399'] = func_1399
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1619 = relay.var("var_1619", dtype = "int8", shape = (6, 4, 12))#candidate|1619|(6, 4, 12)|var|int8
var_1620 = relay.var("var_1620", dtype = "int8", shape = (6, 4, 12))#candidate|1620|(6, 4, 12)|var|int8
bop_1621 = relay.subtract(var_1619.astype('int8'), relay.reshape(var_1620.astype('int8'), relay.shape_of(var_1619))) # shape=(6, 4, 12)
func_1396_call = mod.get_global_var('func_1396')
func_1399_call = mutated_mod.get_global_var('func_1399')
var_1628 = relay.var("var_1628", dtype = "bool", shape = (1, 112))#candidate|1628|(1, 112)|var|bool
call_1627 = relay.TupleGetItem(func_1396_call(relay.reshape(var_1628.astype('bool'), [16, 7, 1])), 0)
call_1629 = relay.TupleGetItem(func_1399_call(relay.reshape(var_1628.astype('bool'), [16, 7, 1])), 0)
func_206_call = mod.get_global_var('func_206')
func_210_call = mutated_mod.get_global_var('func_210')
const_1646 = relay.const([6,-3,-1,-4,7,-10,8,1,7,9,-9,-10,-10,6,8,5,-7,4,9,-8,7,3,8,-1,3,4,10,-6,6,4,5,7,-8,-1,-3,3,7,-7,9,1,7,7,-7,8,5,9,-1,-6,-1,6,-6,-6,-7,9,1,10,-3,-7,-10,-8,-7,8,5,-9,-9,-10,3,9,7,8,9,-7,-6,7,-1,2,-1,-8,-4,-1,-1,9,5,6,7,-3,3,-1,6,5,-10,-5,-9,9,9,6,1,6,5,-1,5,1,3,6,-9,-7,2,-1,-7,4,-10,-6,10,-10,-3,9,4,5,-3,7,6,2,5,8,-6,8,5,-1,-5,1,-10,5,2,1,4,1,3,-7,1,-10,10,-4,-3,1,6,5,2,-1,-3,4,-10,7,-10,-2,2,7,2,-8,-6,3,10,-9,-2,-1,-3,-2,1,6,8,10,2,1,-1,-8,-7,-1,1,-1,10,-5,6,6,1,-7,-2,6,-6,-9,-7,6,-8,-10,6,-1,1,7,-5,5,7,-4,2,-6,-8,-5,-1,-8,-7,9,10,-8,-4,-10,-2,-7,-8,-9,-1,-9,9,2,7,9,8,7,-6,1,-2,2,-8,2,-8,-6,-5,7,-3,3,9,-3,-10,7,7,-9,-10,2,10,4,6,-6,-7,6,2,-9,1,-1,4,8,-7,10,-8,3,-6,-5,-7,5,3,-3,1,7,-5,5,-8,1,-10,1,1,5,3,4,-2,-5,10,-10,-1,5,7,5,10,9,5,9,5,7,-7,-7,10,2,1,3,10,8,-5,-3,9,7,3,1,-4,-8,-9,-8,9,9,3,-10,7,2,-10,-8,-8,-2,3,-1,-4,-7,-5,2,-4,-4,2,-2,3,-2,9,-4,5,8,-1,-4,-7,10,6,8,4,9,-7,6,4,-4,7,8,4,-9,-6,-4,4,6,5,-1,5,4,10,-3,9,5,-5,-10,-10,6,4,8,-3,9,6,8,10,5,-3,2], dtype = "uint8")#candidate|1646|(378,)|const|uint8
var_1647 = relay.var("var_1647", dtype = "int32", shape = (60,))#candidate|1647|(60,)|var|int32
call_1645 = relay.TupleGetItem(func_206_call(relay.reshape(const_1646.astype('uint8'), [3, 9, 14]), relay.reshape(var_1647.astype('int32'), [3, 2, 10]), ), 4)
call_1648 = relay.TupleGetItem(func_210_call(relay.reshape(const_1646.astype('uint8'), [3, 9, 14]), relay.reshape(var_1647.astype('int32'), [3, 2, 10]), ), 4)
bop_1649 = relay.minimum(const_1646.astype('uint8'), call_1627.astype('uint8')) # shape=(16, 7, 378)
bop_1652 = relay.minimum(const_1646.astype('uint8'), call_1629.astype('uint8')) # shape=(16, 7, 378)
output = relay.Tuple([bop_1621,var_1628,call_1645,var_1647,bop_1649,])
output2 = relay.Tuple([bop_1621,var_1628,call_1648,var_1647,bop_1652,])
func_1668 = relay.Function([var_1619,var_1620,var_1628,var_1647,], output)
mod['func_1668'] = func_1668
mod = relay.transform.InferType()(mod)
mutated_mod['func_1668'] = func_1668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1668_call = mutated_mod.get_global_var('func_1668')
var_1670 = relay.var("var_1670", dtype = "int8", shape = (6, 4, 12))#candidate|1670|(6, 4, 12)|var|int8
var_1671 = relay.var("var_1671", dtype = "int8", shape = (6, 4, 12))#candidate|1671|(6, 4, 12)|var|int8
var_1672 = relay.var("var_1672", dtype = "bool", shape = (1, 112))#candidate|1672|(1, 112)|var|bool
var_1673 = relay.var("var_1673", dtype = "int32", shape = (60,))#candidate|1673|(60,)|var|int32
call_1669 = func_1668_call(var_1670,var_1671,var_1672,var_1673,)
output = call_1669
func_1674 = relay.Function([var_1670,var_1671,var_1672,var_1673,], output)
mutated_mod['func_1674'] = func_1674
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1768 = relay.var("var_1768", dtype = "int8", shape = (7, 12, 9))#candidate|1768|(7, 12, 9)|var|int8
var_1769 = relay.var("var_1769", dtype = "int8", shape = (7, 12, 9))#candidate|1769|(7, 12, 9)|var|int8
bop_1770 = relay.bitwise_xor(var_1768.astype('int8'), relay.reshape(var_1769.astype('int8'), relay.shape_of(var_1768))) # shape=(7, 12, 9)
func_206_call = mod.get_global_var('func_206')
func_210_call = mutated_mod.get_global_var('func_210')
const_1776 = relay.const([-7,-10,7,1,-3,3,-10,-8,10,-5,2,-7,-2,-2,-5,-6,10,-1,2,-6,1,-4,6,2,-4,5,10,4,8,10,-9,-4,-2,3,6,-9,-1,-8,7,-3,10,-6,1,10,-6,-1,-7,-1,1,-5,5,6,8,-3,7,-7,-5,5,1,-3,10,-1,10,-7,7,-2,5,10,-3,10,2,-4,10,-1,9,-7,10,5,9,-5,-4,-1,-2,-4,-6,4,4,5,9,7,1,-4,-4,-3,3,-1,2,7,5,-8,10,10,-9,-9,10,6,-10,4,-1,8,2,10,3,9,-9,-10,-10,2,-5,8,7,-7,-6,4,8,1,1,-6,-1,2,-4,10,3,3,-4,-3,7,-1,-3,-2,5,10,7,2,-3,-9,-9,10,2,9,-8,-9,2,-10,3,5,5,5,1,1,4,-10,-8,4,-8,6,-5,3,-4,-4,2,4,5,3,-9,-2,4,-3,-4,4,1,-8,-4,-4,1,-5,7,4,1,10,2,2,-3,8,-3,9,-2,-10,7,7,4,-5,-3,5,-6,3,-6,-4,1,6,6,-8,4,7,2,9,7,-6,-3,-6,7,-7,-4,2,4,-9,-5,9,3,-9,3,10,4,-2,-9,7,8,9,-4,-9,-8,9,3,1,3,2,9,-5,10,-1,-6,4,-10,-7,-5,5,5,7,1,6,1,9,2,5,3,-10,2,-2,9,1,6,-9,9,8,5,3,4,8,-7,-5,-8,-9,2,-5,3,-7,9,9,-2,-7,1,-5,-1,10,-5,-8,1,-3,9,4,-1,10,-6,9,5,7,5,2,4,-4,6,-3,-9,2,6,7,-8,9,-5,-2,-6,8,-10,1,-2,-4,-7,9,-7,4,-6,1,10,-8,10,-7,8,10,-6,1,-6,-8,5,-10,8,-4,-7,-8,2,-1,-5,-1,-4,8,-1,-9,5,-3,5,-3,-7,7,9,-10,1,-5,10,9,6,5,8,6,3,6,-3,1,3,4], dtype = "uint8")#candidate|1776|(378,)|const|uint8
const_1777 = relay.const([-4,5,-9,7,2,-5,1,-3,1,-8,-4,-3,1,-2,9,-10,6,-6,4,-4,5,5,7,4,-6,2,-3,4,2,-10,-9,-7,8,3,7,8,9,9,-3,-1,-7,-10,9,-6,-10,-3,9,-8,-3,8,-8,-1,4,-2,-5,8,7,2,-2,8], dtype = "int32")#candidate|1777|(60,)|const|int32
call_1775 = relay.TupleGetItem(func_206_call(relay.reshape(const_1776.astype('uint8'), [3, 9, 14]), relay.reshape(const_1777.astype('int32'), [3, 2, 10]), ), 4)
call_1778 = relay.TupleGetItem(func_210_call(relay.reshape(const_1776.astype('uint8'), [3, 9, 14]), relay.reshape(const_1777.astype('int32'), [3, 2, 10]), ), 4)
output = relay.Tuple([bop_1770,call_1775,const_1776,const_1777,])
output2 = relay.Tuple([bop_1770,call_1778,const_1776,const_1777,])
func_1789 = relay.Function([var_1768,var_1769,], output)
mod['func_1789'] = func_1789
mod = relay.transform.InferType()(mod)
var_1790 = relay.var("var_1790", dtype = "int8", shape = (7, 12, 9))#candidate|1790|(7, 12, 9)|var|int8
var_1791 = relay.var("var_1791", dtype = "int8", shape = (7, 12, 9))#candidate|1791|(7, 12, 9)|var|int8
output = func_1789(var_1790,var_1791,)
func_1792 = relay.Function([var_1790,var_1791,], output)
mutated_mod['func_1792'] = func_1792
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1938 = relay.var("var_1938", dtype = "float32", shape = (4, 5, 7))#candidate|1938|(4, 5, 7)|var|float32
var_1939 = relay.var("var_1939", dtype = "float32", shape = (4, 5, 7))#candidate|1939|(4, 5, 7)|var|float32
bop_1940 = relay.power(var_1938.astype('float32'), relay.reshape(var_1939.astype('float32'), relay.shape_of(var_1938))) # shape=(4, 5, 7)
bop_1946 = relay.floor_mod(var_1938.astype('float64'), relay.reshape(var_1939.astype('float64'), relay.shape_of(var_1938))) # shape=(4, 5, 7)
func_1356_call = mod.get_global_var('func_1356')
func_1360_call = mutated_mod.get_global_var('func_1360')
const_1952 = relay.const([8,3,-1,3,-8,3,4,1,-3,4,-10,-4,-1,-7,5,-6,-3,10,-3,-7,3,-10,7,8,10,5,9,6,-8,-6,-4,-5,-1,-2,-9,5,6,1,-9,-3,-1,8,-8,1,7,10,-10,-10,-9,5,-9,9,6,-1,9,5,-4,1,7,-1,-9,-8,5,10,-10,1,-3,-9,2,-5,5,2,-3,5,-3,6,7,-1,-6,8,3,-7,2,7,-7,-5,-4,-4,-10,-9,-7,-4,-3,-9,-5,-4,6,7,7,-2,-10,-7,-3,-3,3,-5,9,5,6,10,8,-2,-5,-2,4,-7,10,9,6,-6,4,-9,5,-4,7,2,7,-10,2,-5,6,1,5,-1,1,-1,-1,9,-4,6,-8,7,-2,-8,-8,3,2,-2,-3,9,10,-1,8,-8,-5,-4,-5,-8,5,-5,6,9,-9,6,-3,8,-3,-8,-8,-3,-3,6,5,8,10,5,1,-6,4,-4,7,2,-10,-10,7,3,-10,1,-5,-7,2,2,7,-6,2,-10,2,8,4,-8,9,4,-10,-7,4,1,6,-1,-5,-6,7,-5,-9,8,-9,6,-10,9,3,-7,10,5,3,-10,5,5,-3,-10,5,8,6,6,-4,8,-3,-8,-4,10,1,8,-10,-7,-5,-7,-4,-4,1,-6,5,6,-10,-2,7,4,3,-3,4,6,-4,-10,10,-9,-6,-7,1,-10,8,-7,-3,3,2,-9,-4,8,7,-6,-5,-7,-2,-3,-8,7,-6,-10,-7,5,9,-10,6,-10,-7,10,-5,-5,1,-3,-3,-6,-5,6,-1,3,-4,2,-10,-4,3,1,3,5,5,5,-6,-5,-9,-5,1,-10,-1,-6,7,2,-6,-5,10,-2,-8,1,10,-7,8,-1,9,5,-4,-5,-4,10,-9,-6,-7,-3,7,-8,-1,-6,-6,9,8,9,6,-4,8,-10,-1,5,-7,2,4,3,-5,-6,5,10,1,9,1,10,9,8,8,-7,-4,1,9,5,2,-6,-9,4,4,-9,-7,6,-1,-6,-8,6,-4,-1,-2,6,10,-2,-8,10,2,-1,-10,-6,3,-10,7,-4,4,3,-2,9,-2,-2,9,-6,-1,1,6,-2,9,2,9,-6,-1,-6,-9,4,8,-6,8,-10,-1,-2,-8,5,-6,3,5,8,-10,9,-9,-3,-9,-6,10,-5,8,-7,-2,4,-1,3,6,-10,-6,-6,-1,4,5,-6,7,-4,-1,-1,-3,-10,2,10,7,-4,10,9,-6,-3,6,-4,3,10,-10,6,6,10,3,5,2,4,7,7,-8,-4,2,-9,-7,10,2,1,-3,-7,10,6,-1,-8,-4,4,5,-8,8,-3,-8,2,-10,7,3,10,6,-7,-8,7,-2,-6,9,-6,-1,1,2,9,-6,7,-10,5,5,-3,1,-5,-1,7,-6,6,-2,7,10,-7,-2,-8,-3,8,-8,-3,3,9,-10,3,-1,-3,5,10,8,2,4,-4,-6,5,5,3,5,-9,2,10,10,8,-5,-1,-6,5,-4,6,-1,-1,8,-2,8,7,5,3,1,1,10,9,4,7,-10,7,4,8,4,7,3,-9,-1,4,-4,8,-8,1,10,1,2,1,-5,-10,-1,8,2,2,2,7,-2,1,3,-3,1,-3,1,-1,-5,5,7,-9,3,-4,9,2,-8,3,-6,-4,-10,1,3,8,-2,-5,8,-10,7,-7,-5,10,-3,-5,-3,7,-6,-7,-8,-8,-9,9,-8,8,1,2,6,9,8,8,5,-5,2,1,-8,-10,3,-2,-8,-4,8,7,1,3,4,-3,9,-9,1,-2,-2,-3,4,3,6,3,7,-9,-9,-10,-6,-1,2,-5,-1,-9,1,-7,-9,-9,10,-10,3,7,-2,5,1,-10,-6,-5,3,-2,-8,-9,9,-2,1,8,-1,-8,-6,-8,10,2,-6,7,-3,-4,-5,-7,-3,3,-1,8,8,5,-10,10,3,-10,-9,8,3,2,-5,2,8,-1,-8,2,-6,9,10,-10,3,1,4,-5,-9,6,-6,3,-6,4,3,2,-3,-7,-4,5,4,1,-5,-6,-1,-10,1,-2,8,-2,2,-2,7,-7,6,-8,7,-2,-4,-9,-1,4,4,8,2,5,-4,-6,-8,-1,4,-9,-1,-5,9,1,-5,-1,-1,-1,1,-4,2,-7,4,7,1,8,4,6,7,5,-2,-1,7,5,-7,-6,-10,1,3,9,1,6,3,3,9,4,-4,4,6,-3,8,-5,-2,-10,4,9,-9,5,4,3,-3,5,-1,-3,8,-1,-3,3,-5,-10,-2,-6,-3,4,8,1,2,3,4,-2,9,-7,2,-10,2,-7,1,7,6,-1,7,-10,-9,4,-6,-6,-2,9,-4,2,-1,10,4,-3,-9,7,-8,4,-7,-1,-7,-9,-1,-4,9,10,-4,-1,-10,-9,1,-4,10,-6,-8,-3,5,5,-2,2,-2,-3,-7,-5,9,7,-7,-10,-10,-7,5,-5,-3,8,-7,9,5,8,-4,-8,-6,-4,-7,-1,3,5,-9,10,-1,9,1,9,-10,9,-1,-1,-3,9,9,4,9,10,10,-10,-10,-10,9,-8,-8,4,-5,4,10,-5,3,-1,-1,-10,10,-3,-1,1,4,-10,6,2,9,-9,-9,-7,6,-7,-6,-1,9,7,8,-1,-9,5,-4,-9,2,9,-2,6,-4,-8,-1,9,2,-9,5,-5,10,-10,-4,7,-6,-9,-5,-8,-9,-1,5,10,7,-10,-1,7,-4,8,-7,-5,-3,1,1,-9,8,-1,-2,-4,2,1,10,7,-4,-3,-1,-4,-5,4,-8,8,-3,-1,-2,3,-1,-7,2,-5,10,9,-6,-8,2,7,-5,6,-4,2,-5,9,-9,7,2,-10,-9,6,2,4,-5,3,-6,7,-9,-7,4,-10,-4,-4,8,1,-3,-1,-2,-10,-8,9,6,-5,7,-9,7,5,6,-8,-5,10,-7,-4,5,-9,1,-6,-6,-1,-2,5,2,1,-1,-10,9,6,-10,6,-8,-8,-3,-5,-5,3,9,-7,7,-6,-8,-7,-6,-2,7,4,4,-4,6,7,6,-1,7,-5,-5,-5,9,9,-6,4,2,7,-9,3,10,9,10,-2,-7,1,8,-6,-7,6,7,-7,7,-2,-4,-4,-7,-10,-2,-5,-9,-2,4,8,2,-5,4,-7,-5,-9,-8,-3,5,-3,8,-7,-8,-6,6,4,-7,-8,-2,-2,-6,7,-6,-8,-6,2,-2,-2,8,3,-3,-6,9,-1,-9,-7,6,8,4,4,8,7,5,-2,-9,-10,3,3,8,-10,-9,-1,-3,-8,4,9,10,-3,5,-9,-8,9,3,-3,7,7,4,-2,8,4,-4,3,6,6,-1,10,-1,3,2,-6,-3,7,-2,2,9,-1,8,-4,2,-8,6,-4,-6,3,-5,6,-2,5,2,-2,-3,5,-9,-6,10,5,1,-2,-8,-2,2,3,3,-5,-5,-7,4,-10,10,5,1,5,-9,6,2,2,-9,7,5,8,-3,-10,6,9,5,7,3,-7,-1,-2,4,6,-1,5,6,-5,8,-3,5,-4,5,-8,5,1,-8,-10,8,-6,-10,-6,4,-5,-9,1,-2,6,-6,8,-10,1,3,-2,7,4,9,-6,-3,7,3,8,3,-5,-10,2,1,10,5,6,8,-1,-2,-1,-10,-9,-8,-8,-2,-10,3,2,3,9,2,10,-5,-8,-10,2,-9,4,-7,-6,7,-1,8,-6], dtype = "int8")#candidate|1952|(1408,)|const|int8
call_1951 = relay.TupleGetItem(func_1356_call(relay.reshape(const_1952.astype('int8'), [11, 8, 16]), relay.reshape(const_1952.astype('int8'), [11, 8, 16]), ), 3)
call_1953 = relay.TupleGetItem(func_1360_call(relay.reshape(const_1952.astype('int8'), [11, 8, 16]), relay.reshape(const_1952.astype('int8'), [11, 8, 16]), ), 3)
output = relay.Tuple([bop_1940,bop_1946,call_1951,const_1952,])
output2 = relay.Tuple([bop_1940,bop_1946,call_1953,const_1952,])
func_1954 = relay.Function([var_1938,var_1939,], output)
mod['func_1954'] = func_1954
mod = relay.transform.InferType()(mod)
mutated_mod['func_1954'] = func_1954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1954_call = mutated_mod.get_global_var('func_1954')
var_1956 = relay.var("var_1956", dtype = "float32", shape = (4, 5, 7))#candidate|1956|(4, 5, 7)|var|float32
var_1957 = relay.var("var_1957", dtype = "float32", shape = (4, 5, 7))#candidate|1957|(4, 5, 7)|var|float32
call_1955 = func_1954_call(var_1956,var_1957,)
output = call_1955
func_1958 = relay.Function([var_1956,var_1957,], output)
mutated_mod['func_1958'] = func_1958
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2060 = relay.var("var_2060", dtype = "float64", shape = (9, 4, 7))#candidate|2060|(9, 4, 7)|var|float64
uop_2061 = relay.acosh(var_2060.astype('float64')) # shape=(9, 4, 7)
func_1789_call = mod.get_global_var('func_1789')
func_1792_call = mutated_mod.get_global_var('func_1792')
var_2068 = relay.var("var_2068", dtype = "int8", shape = (756,))#candidate|2068|(756,)|var|int8
call_2067 = relay.TupleGetItem(func_1789_call(relay.reshape(var_2068.astype('int8'), [7, 12, 9]), relay.reshape(var_2068.astype('int8'), [7, 12, 9]), ), 3)
call_2069 = relay.TupleGetItem(func_1792_call(relay.reshape(var_2068.astype('int8'), [7, 12, 9]), relay.reshape(var_2068.astype('int8'), [7, 12, 9]), ), 3)
bop_2089 = relay.less(uop_2061.astype('bool'), relay.reshape(var_2060.astype('bool'), relay.shape_of(uop_2061))) # shape=(9, 4, 7)
output = relay.Tuple([call_2067,var_2068,bop_2089,])
output2 = relay.Tuple([call_2069,var_2068,bop_2089,])
func_2095 = relay.Function([var_2060,var_2068,], output)
mod['func_2095'] = func_2095
mod = relay.transform.InferType()(mod)
var_2096 = relay.var("var_2096", dtype = "float64", shape = (9, 4, 7))#candidate|2096|(9, 4, 7)|var|float64
var_2097 = relay.var("var_2097", dtype = "int8", shape = (756,))#candidate|2097|(756,)|var|int8
output = func_2095(var_2096,var_2097,)
func_2098 = relay.Function([var_2096,var_2097,], output)
mutated_mod['func_2098'] = func_2098
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2620 = relay.var("var_2620", dtype = "uint32", shape = (8, 7, 14))#candidate|2620|(8, 7, 14)|var|uint32
var_2621 = relay.var("var_2621", dtype = "uint32", shape = (8, 7, 14))#candidate|2621|(8, 7, 14)|var|uint32
bop_2622 = relay.less_equal(var_2620.astype('bool'), relay.reshape(var_2621.astype('bool'), relay.shape_of(var_2620))) # shape=(8, 7, 14)
func_1668_call = mod.get_global_var('func_1668')
func_1674_call = mutated_mod.get_global_var('func_1674')
const_2626 = relay.const([-9,1,6,2,1,-1,9,1,-6,8,-8,7,-4,-10,-2,-2,-7,-10,10,-10,-2,-2,-10,-3,-2,8,-3,-7,-9,-8,7,2,5,-8,6,6,1,-8,-2,7,3,-3,10,3,-8,-10,1,10,6,10,6,-1,-3,7,-2,-9,-10,1,-4,-1,3,9,3,-1,7,-10,-5,-1,-10,4,-5,-6,7,8,10,-6,-9,1,6,1,-1,-8,4,5,-2,-7,-1,-5,-10,2,10,-5,2,-5,7,-2,8,5,3,-7,8,-1,5,-1,-9,-5,10,-10,-7,1,-10,2,-4,2,-8,10,1,9,9,10,-1,-7,-8,-3,1,-1,-6,-10,2,8,9,8,-3,-5,-6,-10,-2,10,-5,7,7,-8,-2,7,-2,-6,5,10,-10,2,-2,5,-1,-7,7,6,-1,9,5,-7,-1,8,6,7,5,-6,-2,-4,-5,3,7,6,-6,-1,-2,-7,-3,2,5,9,-7,-10,5,5,-6,-2,8,1,4,4,-4,3,-8,-9,4,-4,5,1,-9,-10,7,-10,-1,-10,4,-4,-6,6,-2,8,6,-7,9,3,-6,-5,-6,-9,-5,-3,-4,-7,-4,6,-9,9,10,8,-6,9,3,-5,8,-5,5,-4,-5,-3,6,-4,-6,2,-1,-7,-1,-8,-8,-3,-1,3,-8,-6,10,5,-9,-4,-4,-4,9,1,-6,4,4,-4,8,10,6,3,7,3,7,-4,-4,-3,8,2,-2,9,6,2,3,-1,10,-5,2,-5,-7,-7], dtype = "int8")#candidate|2626|(288,)|const|int8
const_2627 = relay.const([True,False,False,True,True,True,False,False,False,False,True,False,False,False,False,True,True,True,True,False,False,False,False,True,False,False,True,False,False,True,False,False,True,False,True,False,True,True,False,True,True,False,True,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,False,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,False,False,True,True,True,False,False,False,False,False,False,True,False,True,False,True,True,False,True,False,False,True,False,True,True,False,False,False,False,True,False,False,True,False,True,True,False], dtype = "bool")#candidate|2627|(112,)|const|bool
var_2628 = relay.var("var_2628", dtype = "int32", shape = (60,))#candidate|2628|(60,)|var|int32
call_2625 = relay.TupleGetItem(func_1668_call(relay.reshape(const_2626.astype('int8'), [6, 4, 12]), relay.reshape(const_2626.astype('int8'), [6, 4, 12]), relay.reshape(const_2627.astype('bool'), [1, 112]), relay.reshape(var_2628.astype('int32'), [60,]), ), 3)
call_2629 = relay.TupleGetItem(func_1674_call(relay.reshape(const_2626.astype('int8'), [6, 4, 12]), relay.reshape(const_2626.astype('int8'), [6, 4, 12]), relay.reshape(const_2627.astype('bool'), [1, 112]), relay.reshape(var_2628.astype('int32'), [60,]), ), 3)
bop_2646 = relay.floor_mod(var_2620.astype('float64'), relay.reshape(bop_2622.astype('float64'), relay.shape_of(var_2620))) # shape=(8, 7, 14)
func_1789_call = mod.get_global_var('func_1789')
func_1792_call = mutated_mod.get_global_var('func_1792')
var_2653 = relay.var("var_2653", dtype = "int8", shape = (9, 84))#candidate|2653|(9, 84)|var|int8
call_2652 = relay.TupleGetItem(func_1789_call(relay.reshape(var_2653.astype('int8'), [7, 12, 9]), relay.reshape(var_2653.astype('int8'), [7, 12, 9]), ), 1)
call_2654 = relay.TupleGetItem(func_1792_call(relay.reshape(var_2653.astype('int8'), [7, 12, 9]), relay.reshape(var_2653.astype('int8'), [7, 12, 9]), ), 1)
func_1144_call = mod.get_global_var('func_1144')
func_1147_call = mutated_mod.get_global_var('func_1147')
var_2663 = relay.var("var_2663", dtype = "float64", shape = (24, 8))#candidate|2663|(24, 8)|var|float64
call_2662 = func_1144_call(relay.reshape(var_2663.astype('float64'), [3, 4, 16]))
call_2664 = func_1144_call(relay.reshape(var_2663.astype('float64'), [3, 4, 16]))
func_1144_call = mod.get_global_var('func_1144')
func_1147_call = mutated_mod.get_global_var('func_1147')
call_2668 = func_1144_call(relay.reshape(var_2663.astype('float64'), [3, 4, 16]))
call_2669 = func_1144_call(relay.reshape(var_2663.astype('float64'), [3, 4, 16]))
func_2095_call = mod.get_global_var('func_2095')
func_2098_call = mutated_mod.get_global_var('func_2098')
var_2680 = relay.var("var_2680", dtype = "float64", shape = (1, 252))#candidate|2680|(1, 252)|var|float64
call_2679 = relay.TupleGetItem(func_2095_call(relay.reshape(var_2680.astype('float64'), [9, 4, 7]), relay.reshape(var_2653.astype('int8'), [756,]), ), 0)
call_2681 = relay.TupleGetItem(func_2098_call(relay.reshape(var_2680.astype('float64'), [9, 4, 7]), relay.reshape(var_2653.astype('int8'), [756,]), ), 0)
func_206_call = mod.get_global_var('func_206')
func_210_call = mutated_mod.get_global_var('func_210')
var_2727 = relay.var("var_2727", dtype = "uint8", shape = (378,))#candidate|2727|(378,)|var|uint8
call_2726 = relay.TupleGetItem(func_206_call(relay.reshape(var_2727.astype('uint8'), [3, 9, 14]), relay.reshape(call_2625.astype('int32'), [3, 2, 10]), ), 4)
call_2728 = relay.TupleGetItem(func_210_call(relay.reshape(var_2727.astype('uint8'), [3, 9, 14]), relay.reshape(call_2625.astype('int32'), [3, 2, 10]), ), 4)
func_852_call = mod.get_global_var('func_852')
func_855_call = mutated_mod.get_global_var('func_855')
const_2730 = relay.const(-1, dtype = "int16")#candidate|2730|()|const|int16
call_2729 = relay.TupleGetItem(func_852_call(relay.reshape(const_2730.astype('int16'), []), relay.reshape(call_2625.astype('int32'), [60,]), ), 2)
call_2731 = relay.TupleGetItem(func_855_call(relay.reshape(const_2730.astype('int16'), []), relay.reshape(call_2625.astype('int32'), [60,]), ), 2)
func_1396_call = mod.get_global_var('func_1396')
func_1399_call = mutated_mod.get_global_var('func_1399')
call_2747 = relay.TupleGetItem(func_1396_call(relay.reshape(const_2627.astype('bool'), [16, 7, 1])), 0)
call_2748 = relay.TupleGetItem(func_1399_call(relay.reshape(const_2627.astype('bool'), [16, 7, 1])), 0)
func_1356_call = mod.get_global_var('func_1356')
func_1360_call = mutated_mod.get_global_var('func_1360')
const_2756 = relay.const([[5,-2,6,10,-1,8,1,-5,-8,-2,4,8,-7,9,-10,8,10,-4,8,-6,10,-7,4,9,4,2,7,3,8,7,-10,-3,-5,-5,-2,-1,4,5,-1,-9,-6,-5,2,8,-2,8,-9,2,-8,8,9,4,9,-9,-4,5,1,2,8,5,-4,-3,2,7,-2,1,6,5,3,-4,-4,6,9,-1,9,-10,-9,-7,6,-2,-1,-10,-8,-10,10,-9,-5,10,-4,-4,6,-7,-6,-5,-10,-1,-10,6,7,-1,2,-9,-5,-4,9,4,-3,-8,7,9,10,8,2,-10,-2,6,-10,-2,6,-8,5,2,-4,4,6,9,-5,8,3,-8,8,8,9,-5,-7,1,4,9,-6,1,8,7,-9,3,-2,4,3,8,-1,10,-7,-9,6,10,10,-3,-3,2,-5,3,-5,5,-8,-1,-7,8,-4,6,-4,-2,-10,-5,-5,-3,1,8,-3,-4,-10,-2,10,3,-7,-3,-5,-7,10,-8,-8,-7,-6,-7,-10,2,9,-6,-3,2,8,-3,10,10,2,9,6,1,3,-3,-10,-4,8,-8,9,-3,5,1,-5,-7,8,7,2,-8,-7,-7,-5,-9,-10,-5,7,9,-3,-9,-3,5,4,5,-1,2,-5,6,9,4,2,-2,9,-3,4,-1,10,-8,8,-10,-8,7,-1,-3,8,-4,7,1,9,-8,-6,2,7,-10,-3,3,3,3,5,-8,3,5,-8,-8,10,2,9,4,3,-8,-4,-8,-3,3,-6,2,3,-3,-4,9,-9,2,4,1,-7,4,3,10,-2,3,6,-9,-3,-1,3,2,3,-9,9,-4,2,2,9,-1,-7,-9,10,-3,2,9,-3,9,-7,3,-10,-6,5,6,-10,-5,1,-1,3,3,7,3,5,4,-10,-9,3,1,-3,-2,-3,-1,2,-3,-5,2,-10,-10,7,-6,2,-7,3,5,-4,9,5,-2,-2,-3,3,7,-4,-6,-2,8,-2,-10,-3,-10,-3,2,1,-6,9,9,9,-5,4,4,6,1,6,-2,6,6,3,9,4,-8,-7,6,5,-6,3,-5,1,6,7,8,1,5,2,9,-1,8,4,-3,5,7,1,-6,8,-2,1,-10,-2,8,1,1,-2,2,-4,4,8,5,3,-2,3,-8,3,-9,-5,10,-2,-9,-9,2,-10,3,6,-7,-1,-10,4,1,5,2,-6,-5,-3,-5,-9,-10,-1,-9,2,8,7,-8,-7,8,-10,4,-5,6,-5,-2,6,-5,4,-8,10,-10,7,7,8,7,-6,-5,10,-8,-10,3,-4,-7,-2,7,-2,-8,4,4,-1,-1,2,7,-5,8,9,3,2,4,-6,6,5,-6,9,10,-1,-6,-6,4,8,-9,5,-10,4,1,-2,-8,10,7,-6,-7,9,7,-6,9,4,3,-1,-8,-7,-5,-7,10,-8,5,4,-8,-5,10,-7,7,8,3,-3,4,-2,-10,3,6,-7,-3,5,5,8,3,-6,-9,10,-4,4,2,-9,5,-2,-3,-2,-9,-10,6,2,5,10,4,5,3,-8,-7,7,8,5,-10,8,5,-8,7,-2,9,6,2,-3,-3,9,-9,2,-8,1,-5,9,-10,-10,-8,7,2,3,5,8,9,7,-4,9,5,1,-10,9,7,7,2,3,7,10,3,1,-3,-4,-5,-10,3,-4,2,-5,3,-6,-5,-8,6,6,4,-3,-4,-8,10,-3,9,-7,9,2,1,-6,1,-9,-10,8,2,4,10,5,10,-4,5,2,3,-5,-3,3,5,-1,-8,-2,2,-6,-10,2,-1,8,8,-10,-5,-7,6,-10,-1,7,-2,10,6,6,-9,5,7,-5,-5,-7,-2,7,-4],[10,-2,7,-7,-5,4,-7,2,-2,7,-3,4,1,2,-3,-8,2,-3,1,-7,-3,2,2,1,-10,-5,1,2,-5,-3,-3,-3,-1,5,6,-2,10,8,5,-10,-10,-9,2,4,-6,-8,-9,3,9,4,9,-4,-8,-3,-2,10,-7,4,10,9,-8,-6,-9,-7,-8,-2,4,8,-8,7,-3,3,-5,1,8,3,6,3,8,-2,8,5,-1,6,-3,1,-9,8,-3,1,-1,-9,4,2,1,-2,1,-1,-8,2,-9,9,-7,-3,-6,-4,-9,-3,5,8,-3,-5,6,5,-4,-7,-9,-2,-3,-7,-9,7,-5,4,-8,-6,-3,-3,10,4,6,8,8,-2,-6,10,-3,5,9,-8,2,-8,-6,3,-3,-9,-8,4,8,7,-8,-9,-3,-9,-4,9,-10,10,-10,-1,1,1,8,5,5,1,-8,6,-5,-4,-1,-6,2,8,-10,-6,-10,10,6,7,-9,7,-9,1,-6,-2,9,-8,3,-4,5,-3,9,-5,1,6,-10,-9,6,2,4,10,1,6,-4,-8,10,-5,5,4,6,7,-5,-5,-6,-4,1,6,2,10,2,-8,-9,3,-7,-9,-9,6,-3,-6,8,-1,-5,-4,1,-4,2,-5,-7,3,7,4,10,-1,-3,-4,-10,1,-4,-4,-9,-7,-2,-9,3,10,6,8,-4,-3,-8,7,3,-5,4,-3,-8,1,-7,7,-4,1,-1,-8,-10,3,9,7,-9,-1,10,6,-6,-5,9,2,9,5,-2,6,-5,9,-8,-6,-9,-1,-10,-4,-6,-7,3,10,5,-1,-10,9,3,-9,-4,-1,1,1,-1,-8,-6,-3,6,-10,-1,-8,-7,6,6,-4,-2,3,-6,-5,-1,-3,-9,7,-2,-8,7,3,4,-5,-7,-1,3,2,-10,8,1,-8,10,10,4,4,-6,7,-8,-10,-3,-6,7,-8,7,8,-7,-10,4,8,8,1,-1,-5,3,8,8,-4,3,2,8,-8,6,4,10,8,-6,-3,9,9,-5,10,10,10,10,3,-2,4,3,-10,10,10,-8,4,-2,9,-10,3,-7,-3,-5,-4,9,6,4,2,5,9,-6,-9,5,-8,-9,3,3,2,2,8,-3,-3,2,10,-9,9,3,-6,7,3,4,-1,-4,9,-8,9,-1,8,-8,-1,1,-4,9,3,3,-2,-2,8,-6,3,-3,-7,5,-10,-6,-1,10,-1,5,-4,10,9,-9,-9,1,-10,6,-1,-5,-5,-1,-7,-10,-1,-2,5,-9,5,1,-4,8,9,3,5,10,-6,6,3,2,3,6,-6,-4,4,7,-8,-2,-10,-4,1,-7,-4,-2,1,10,8,3,3,-6,-1,-5,-9,3,-1,6,-2,9,-8,-2,5,-2,-7,6,10,-7,5,9,8,-3,10,1,4,7,-10,-10,10,7,-7,-7,5,10,-7,-3,-3,-4,-8,5,4,4,3,-1,6,-2,3,9,-3,-7,8,-5,-8,3,5,-8,4,-5,7,-3,7,7,-5,5,7,-10,4,7,-6,8,2,2,-1,4,6,3,3,1,-6,5,10,10,3,-6,10,4,-1,6,3,9,7,3,2,7,-2,-3,2,-8,3,-5,9,2,6,-1,-10,-10,-4,9,7,-4,-10,1,2,-6,3,-5,3,-4,7,-1,8,6,-4,-8,10,-10,-10,-4,-8,9,-4,-6,4,-9,7,-8,9,7,-6,4,8,8,-5,-2,3,-6,8,7,4,-2,5,-6,-3,-10,7,-9,-8,-2,-9,7,8,2,-7,-7,-6,10,1,6,8,-5,9,-9,-10,3,-5,-5,4,-8,-8,-10,6,-6,7,-10,-7,9,10,-7,8,2,-8,8,-4,-3,-1]], dtype = "int8")#candidate|2756|(2, 704)|const|int8
call_2755 = relay.TupleGetItem(func_1356_call(relay.reshape(const_2756.astype('int8'), [11, 8, 16]), relay.reshape(const_2756.astype('int8'), [11, 8, 16]), ), 0)
call_2757 = relay.TupleGetItem(func_1360_call(relay.reshape(const_2756.astype('int8'), [11, 8, 16]), relay.reshape(const_2756.astype('int8'), [11, 8, 16]), ), 0)
output = relay.Tuple([call_2625,const_2626,const_2627,var_2628,bop_2646,call_2652,var_2653,call_2662,var_2663,call_2668,call_2679,var_2680,call_2726,var_2727,call_2729,const_2730,call_2747,call_2755,const_2756,])
output2 = relay.Tuple([call_2629,const_2626,const_2627,var_2628,bop_2646,call_2654,var_2653,call_2664,var_2663,call_2669,call_2681,var_2680,call_2728,var_2727,call_2731,const_2730,call_2748,call_2757,const_2756,])
func_2765 = relay.Function([var_2620,var_2621,var_2628,var_2653,var_2663,var_2680,var_2727,], output)
mod['func_2765'] = func_2765
mod = relay.transform.InferType()(mod)
mutated_mod['func_2765'] = func_2765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2765_call = mutated_mod.get_global_var('func_2765')
var_2767 = relay.var("var_2767", dtype = "uint32", shape = (8, 7, 14))#candidate|2767|(8, 7, 14)|var|uint32
var_2768 = relay.var("var_2768", dtype = "uint32", shape = (8, 7, 14))#candidate|2768|(8, 7, 14)|var|uint32
var_2769 = relay.var("var_2769", dtype = "int32", shape = (60,))#candidate|2769|(60,)|var|int32
var_2770 = relay.var("var_2770", dtype = "int8", shape = (9, 84))#candidate|2770|(9, 84)|var|int8
var_2771 = relay.var("var_2771", dtype = "float64", shape = (24, 8))#candidate|2771|(24, 8)|var|float64
var_2772 = relay.var("var_2772", dtype = "float64", shape = (1, 252))#candidate|2772|(1, 252)|var|float64
var_2773 = relay.var("var_2773", dtype = "uint8", shape = (378,))#candidate|2773|(378,)|var|uint8
call_2766 = func_2765_call(var_2767,var_2768,var_2769,var_2770,var_2771,var_2772,var_2773,)
output = call_2766
func_2774 = relay.Function([var_2767,var_2768,var_2769,var_2770,var_2771,var_2772,var_2773,], output)
mutated_mod['func_2774'] = func_2774
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2927 = relay.var("var_2927", dtype = "int32", shape = (15, 6, 15))#candidate|2927|(15, 6, 15)|var|int32
var_2928 = relay.var("var_2928", dtype = "int32", shape = (15, 6, 15))#candidate|2928|(15, 6, 15)|var|int32
bop_2929 = relay.greater_equal(var_2927.astype('bool'), relay.reshape(var_2928.astype('bool'), relay.shape_of(var_2927))) # shape=(15, 6, 15)
bop_2933 = relay.power(bop_2929.astype('float32'), relay.reshape(var_2928.astype('float32'), relay.shape_of(bop_2929))) # shape=(15, 6, 15)
output = bop_2933
output2 = bop_2933
func_2936 = relay.Function([var_2927,var_2928,], output)
mod['func_2936'] = func_2936
mod = relay.transform.InferType()(mod)
mutated_mod['func_2936'] = func_2936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2936_call = mutated_mod.get_global_var('func_2936')
var_2938 = relay.var("var_2938", dtype = "int32", shape = (15, 6, 15))#candidate|2938|(15, 6, 15)|var|int32
var_2939 = relay.var("var_2939", dtype = "int32", shape = (15, 6, 15))#candidate|2939|(15, 6, 15)|var|int32
call_2937 = func_2936_call(var_2938,var_2939,)
output = call_2937
func_2940 = relay.Function([var_2938,var_2939,], output)
mutated_mod['func_2940'] = func_2940
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3042 = relay.const([[[-1.763787,7.401183,-2.371535,4.796172],[-5.431904,6.416156,-6.822899,-6.153563],[0.108728,1.965929,7.700115,-1.902208],[4.781393,5.544495,5.135085,9.655661],[-4.227722,5.062651,-8.008686,-9.790554],[4.660412,2.992398,-0.248710,-1.796416],[-7.088934,-1.877829,2.685024,-9.829626],[-4.321491,-9.184121,-4.378664,6.461757],[-7.142104,6.086777,2.072888,8.788787],[2.345578,-5.961367,0.305322,8.595475],[8.342565,3.891250,2.625700,0.627912],[-7.697186,9.287566,2.046345,4.755355]],[[2.296647,-8.355869,-6.654277,-2.439397],[-7.222875,4.080367,5.278605,2.738948],[-8.596983,0.582903,1.395730,2.392959],[-6.430267,-6.438733,6.123906,2.566564],[7.632365,7.234866,2.146444,0.262472],[4.727020,0.528653,-7.522688,7.125601],[-0.717440,-1.797689,6.436871,5.220811],[-3.267588,6.763026,3.077299,4.040908],[-0.077457,-5.784710,-6.488808,5.899843],[-6.904904,-4.881362,3.497264,3.228546],[-2.223932,7.285175,-3.006469,6.947473],[1.558382,-9.004711,2.816353,7.255238]],[[1.643007,9.477755,4.534241,7.028499],[-4.452412,-9.677392,3.155218,2.787983],[5.615729,7.024033,1.530966,9.586365],[0.496927,2.941975,9.624918,-1.169601],[-0.285356,-6.439780,-0.637452,1.857660],[7.230890,-7.471486,9.748885,-4.637291],[6.319444,-2.142942,-7.486259,9.958347],[-4.858538,-0.749149,5.883514,-2.221817],[-8.206711,8.611821,-2.561279,2.775344],[3.669374,-8.907218,8.986068,4.951275],[-3.209765,8.545144,2.731395,-5.542205],[5.936505,9.662323,6.991306,-2.272123]],[[-1.927333,-7.251137,-6.574752,-8.603342],[0.959275,3.354852,5.627680,0.928557],[-5.346910,-9.610865,3.777518,1.971263],[1.192188,6.163947,-3.562733,6.395318],[-6.973952,6.114517,8.189505,-3.319460],[-6.739377,-0.858889,-0.187060,4.416060],[-0.949069,8.441657,-2.778921,5.935059],[7.239264,-4.571169,-3.356462,6.801824],[1.023407,-4.143105,-8.945112,-3.632847],[-0.661251,5.081889,-5.798570,4.072590],[-2.949543,2.932028,-8.975927,9.632003],[6.931433,7.896417,9.806194,-9.670643]],[[-5.780814,0.513157,4.966600,1.357437],[-1.014702,8.312606,-9.757723,-1.202088],[2.173967,8.111061,-5.878471,3.363068],[4.403903,3.695853,2.394004,0.797687],[-1.514632,6.002036,-0.479949,9.004305],[5.555357,-2.632087,-6.236765,-9.544264],[-1.213690,5.124787,-0.153457,-3.758382],[1.163570,-6.370628,-0.052925,-2.282615],[2.057353,-4.164454,7.931064,-5.015038],[-2.492007,-6.287836,3.413036,-5.341814],[-0.559091,-8.750562,6.762266,-2.939703],[3.793477,8.150129,3.080420,-5.911096]],[[1.186879,-1.790539,6.851700,1.004240],[9.106691,-4.666642,4.806732,-8.145153],[-9.486818,-6.465688,-5.745572,-0.841360],[-3.710525,4.902399,-2.211338,-2.907194],[-7.801351,-5.833286,2.821210,-4.372425],[7.317615,-1.710970,4.150250,-2.375679],[2.633684,9.001961,-1.538982,3.841558],[-5.769797,-4.556218,7.553937,-7.267617],[1.107185,1.719135,0.446387,-0.470621],[-4.357327,8.679386,7.684678,2.709866],[-4.882979,-3.225170,-2.799674,2.302739],[-8.155016,4.142053,-2.410649,-8.039099]],[[-6.657055,0.227960,7.494160,-3.885856],[-5.436019,6.587374,-8.141330,-8.852716],[-8.127830,4.068686,3.625378,5.678124],[-9.345486,3.054575,-2.009541,-6.687727],[5.060243,-5.282327,3.660684,-3.657428],[-2.609674,-5.294545,-4.321246,-3.877980],[4.924785,4.582141,-1.723995,5.981182],[-2.468699,-2.459883,-9.630991,8.283190],[-7.937296,-9.131563,9.500385,2.872814],[-2.269161,-6.746994,-2.392006,6.474749],[-7.555556,-8.183393,3.113700,0.189062],[-2.696784,8.067439,-4.948658,-3.682372]],[[-7.005882,3.676780,4.227340,-2.115293],[-6.846398,-7.517299,7.562175,-5.615364],[2.780087,-0.890737,-1.443741,-5.469053],[0.792014,8.082203,-8.508366,-3.900423],[-6.595140,-8.519155,-4.538758,-5.045983],[3.700427,-6.070616,-7.824964,-4.317500],[2.807737,6.995378,-5.485863,7.933693],[1.420138,-5.258145,-9.388840,-6.041895],[-2.371431,0.987583,1.271526,8.796793],[-6.999806,1.515251,-9.865251,-5.631553],[9.339820,-7.692878,6.706323,9.060101],[-2.196431,8.030620,7.217796,-5.576157]],[[-0.662745,-3.451086,1.476017,4.891756],[7.799660,-9.487671,-2.307392,-0.711048],[-3.257882,-4.288999,-0.042340,-9.563899],[3.336636,2.116838,-0.346681,-8.283588],[1.211107,-0.305835,-7.885320,7.067338],[4.853813,6.061077,-1.660970,5.042358],[-1.824061,1.570110,8.079081,-5.308314],[6.905655,3.190413,3.609663,-2.116166],[1.481153,2.062263,-5.535593,7.132890],[-3.410305,-7.160787,-4.418154,-8.544870],[2.406543,3.345529,1.697922,5.662870],[-6.160826,-3.524254,-5.554782,-8.351840]],[[-5.301659,6.734729,-2.993057,-3.256739],[5.684487,-4.420431,-9.606111,4.804279],[-4.814840,-2.627999,-0.164584,-5.662698],[3.438092,-3.989631,3.163243,1.967928],[-2.043671,4.549286,3.663985,0.556108],[-2.572267,3.482789,-5.715281,-4.184219],[1.153204,4.148088,-3.904105,-4.215068],[-9.340393,1.407022,-0.590878,4.284274],[6.182379,2.438297,-5.261412,4.420792],[-6.644238,6.687029,8.675724,6.317205],[0.763464,-2.627874,-0.587807,6.904674],[2.823951,2.673360,5.793081,-5.317008]],[[5.295972,1.141609,1.980507,-3.929446],[2.919390,-8.565239,2.023568,-9.566073],[-8.824683,-7.052608,0.481646,-3.408601],[-7.873399,-6.429936,-4.419674,-5.130097],[6.483277,-7.730694,-3.751325,-8.555291],[-2.881467,8.160867,9.794463,-6.055820],[-9.580055,-1.043627,-2.027310,8.859653],[-8.349272,-1.525234,-4.341813,-6.552969],[6.818653,-3.172761,2.395119,4.030984],[-1.855082,6.612179,-9.321450,8.477703],[-7.299658,9.289460,-6.686616,0.066634],[-3.383722,-4.753995,-7.646639,-3.064316]],[[6.268886,-6.515354,-6.523519,-5.672662],[-5.552606,-6.364532,-6.287980,0.466689],[0.250850,4.126564,4.803697,9.031327],[7.861119,1.269162,-1.440949,2.025764],[-7.839462,1.345144,8.012151,5.425901],[8.978728,4.261297,-2.324729,4.376326],[9.599462,8.028262,9.704292,-6.597860],[-2.788744,7.274394,-7.913822,-8.890036],[-1.904281,7.389942,-7.711561,8.062031],[-5.197266,8.615489,7.136365,-8.675827],[9.640973,-7.282381,-0.232699,6.894485],[-8.552280,-7.462591,0.606202,0.248446]],[[-7.209984,-2.445527,-2.280954,-6.388803],[-0.387432,6.849648,-7.734500,-1.948934],[0.053650,0.539671,4.899863,7.253965],[9.312264,-1.489483,-3.583414,-7.905831],[-1.229493,0.888314,-1.909090,4.558979],[5.258011,-1.937426,5.422463,-0.056829],[2.063764,-3.964665,-8.758531,-1.918718],[1.271259,2.418803,1.051941,-6.748751],[-1.362714,-4.826358,-2.113137,8.580570],[-1.717248,7.697330,-7.497886,-1.333692],[7.491220,-1.498694,-1.251028,4.534472],[-8.006556,-0.339857,-5.629879,3.155766]],[[-7.304735,8.744522,-7.951722,7.274802],[4.846365,-2.128241,-9.778085,2.380184],[4.595104,1.478990,5.182448,-4.234523],[2.607485,3.452616,3.392057,-2.068173],[-8.687820,-7.448761,-0.547877,0.261999],[5.296506,5.920195,-1.166968,8.982067],[6.841693,-8.635752,-4.406502,-6.680286],[5.383984,7.188103,-5.743319,-1.728484],[-1.046720,2.269875,-4.270018,-3.643088],[-5.373387,4.987285,-0.673771,5.964763],[-6.775643,-6.120374,-5.021175,-6.132206],[-6.272917,-9.640930,-6.481103,4.232868]],[[-4.325583,4.853797,5.307208,-6.077433],[-4.906554,3.004407,-6.183350,-5.433633],[-5.772543,0.124436,9.759207,-6.310963],[-4.851053,-5.787924,5.189586,8.410266],[5.409978,7.868785,-6.960185,-8.362634],[9.845837,0.689778,-0.566810,-8.870733],[4.443317,5.426757,-1.784636,-3.766419],[9.745663,4.802463,0.949359,-6.382921],[2.487977,0.588923,1.728698,-0.992189],[6.504527,-3.295476,6.791972,-6.604585],[0.632521,6.582709,5.296289,-8.084537],[2.758282,-0.887907,-0.077904,3.442945]]], dtype = "float64")#candidate|3042|(15, 12, 4)|const|float64
var_3043 = relay.var("var_3043", dtype = "float64", shape = (15, 12, 4))#candidate|3043|(15, 12, 4)|var|float64
bop_3044 = relay.floor_divide(const_3042.astype('float64'), relay.reshape(var_3043.astype('float64'), relay.shape_of(const_3042))) # shape=(15, 12, 4)
uop_3054 = relay.sin(var_3043.astype('float32')) # shape=(15, 12, 4)
output = relay.Tuple([bop_3044,uop_3054,])
output2 = relay.Tuple([bop_3044,uop_3054,])
func_3057 = relay.Function([var_3043,], output)
mod['func_3057'] = func_3057
mod = relay.transform.InferType()(mod)
var_3058 = relay.var("var_3058", dtype = "float64", shape = (15, 12, 4))#candidate|3058|(15, 12, 4)|var|float64
output = func_3057(var_3058)
func_3059 = relay.Function([var_3058], output)
mutated_mod['func_3059'] = func_3059
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3909 = relay.var("var_3909", dtype = "float32", shape = (9, 3, 15))#candidate|3909|(9, 3, 15)|var|float32
uop_3910 = relay.erf(var_3909.astype('float32')) # shape=(9, 3, 15)
func_206_call = mod.get_global_var('func_206')
func_210_call = mutated_mod.get_global_var('func_210')
var_3920 = relay.var("var_3920", dtype = "uint8", shape = (378,))#candidate|3920|(378,)|var|uint8
var_3921 = relay.var("var_3921", dtype = "int32", shape = (60,))#candidate|3921|(60,)|var|int32
call_3919 = relay.TupleGetItem(func_206_call(relay.reshape(var_3920.astype('uint8'), [3, 9, 14]), relay.reshape(var_3921.astype('int32'), [3, 2, 10]), ), 0)
call_3922 = relay.TupleGetItem(func_210_call(relay.reshape(var_3920.astype('uint8'), [3, 9, 14]), relay.reshape(var_3921.astype('int32'), [3, 2, 10]), ), 0)
output = relay.Tuple([uop_3910,call_3919,var_3920,var_3921,])
output2 = relay.Tuple([uop_3910,call_3922,var_3920,var_3921,])
func_3923 = relay.Function([var_3909,var_3920,var_3921,], output)
mod['func_3923'] = func_3923
mod = relay.transform.InferType()(mod)
var_3924 = relay.var("var_3924", dtype = "float32", shape = (9, 3, 15))#candidate|3924|(9, 3, 15)|var|float32
var_3925 = relay.var("var_3925", dtype = "uint8", shape = (378,))#candidate|3925|(378,)|var|uint8
var_3926 = relay.var("var_3926", dtype = "int32", shape = (60,))#candidate|3926|(60,)|var|int32
output = func_3923(var_3924,var_3925,var_3926,)
func_3927 = relay.Function([var_3924,var_3925,var_3926,], output)
mutated_mod['func_3927'] = func_3927
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4041 = relay.var("var_4041", dtype = "float64", shape = (7, 16, 6))#candidate|4041|(7, 16, 6)|var|float64
uop_4042 = relay.atanh(var_4041.astype('float64')) # shape=(7, 16, 6)
bop_4049 = relay.power(var_4041.astype('float64'), relay.reshape(uop_4042.astype('float64'), relay.shape_of(var_4041))) # shape=(7, 16, 6)
output = bop_4049
output2 = bop_4049
func_4053 = relay.Function([var_4041,], output)
mod['func_4053'] = func_4053
mod = relay.transform.InferType()(mod)
mutated_mod['func_4053'] = func_4053
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4054 = relay.var("var_4054", dtype = "float64", shape = (7, 16, 6))#candidate|4054|(7, 16, 6)|var|float64
func_4053_call = mutated_mod.get_global_var('func_4053')
call_4055 = func_4053_call(var_4054)
output = call_4055
func_4056 = relay.Function([var_4054], output)
mutated_mod['func_4056'] = func_4056
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4662 = relay.const(-1, dtype = "uint16")#candidate|4662|()|const|uint16
var_4663 = relay.var("var_4663", dtype = "uint16", shape = (3, 2, 10))#candidate|4663|(3, 2, 10)|var|uint16
bop_4664 = relay.left_shift(const_4662.astype('uint16'), var_4663.astype('uint16')) # shape=(3, 2, 10)
output = relay.Tuple([bop_4664,])
output2 = relay.Tuple([bop_4664,])
func_4677 = relay.Function([var_4663,], output)
mod['func_4677'] = func_4677
mod = relay.transform.InferType()(mod)
mutated_mod['func_4677'] = func_4677
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4678 = relay.var("var_4678", dtype = "uint16", shape = (3, 2, 10))#candidate|4678|(3, 2, 10)|var|uint16
func_4677_call = mutated_mod.get_global_var('func_4677')
call_4679 = func_4677_call(var_4678)
output = call_4679
func_4680 = relay.Function([var_4678], output)
mutated_mod['func_4680'] = func_4680
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4761 = relay.var("var_4761", dtype = "float32", shape = (15, 2, 10))#candidate|4761|(15, 2, 10)|var|float32
uop_4762 = relay.atanh(var_4761.astype('float32')) # shape=(15, 2, 10)
func_1144_call = mod.get_global_var('func_1144')
func_1147_call = mutated_mod.get_global_var('func_1147')
var_4777 = relay.var("var_4777", dtype = "float64", shape = (48, 4))#candidate|4777|(48, 4)|var|float64
call_4776 = func_1144_call(relay.reshape(var_4777.astype('float64'), [3, 4, 16]))
call_4778 = func_1144_call(relay.reshape(var_4777.astype('float64'), [3, 4, 16]))
func_4677_call = mod.get_global_var('func_4677')
func_4680_call = mutated_mod.get_global_var('func_4680')
const_4781 = relay.const([2,-1,-1,-8,4,1,-7,9,3,-6,7,-3,2,2,8,-4,5,-3,-10,5,-10,-1,7,6,4,-8,-1,-7,9,-3,-3,9,4,-4,2,10,6,-7,-3,-2,7,9,-2,-3,8,-2,-2,-10,-3,-1,-6,7,2,4,8,-4,7,-5,2,4], dtype = "uint16")#candidate|4781|(60,)|const|uint16
call_4780 = relay.TupleGetItem(func_4677_call(relay.reshape(const_4781.astype('uint16'), [3, 2, 10])), 0)
call_4782 = relay.TupleGetItem(func_4680_call(relay.reshape(const_4781.astype('uint16'), [3, 2, 10])), 0)
func_206_call = mod.get_global_var('func_206')
func_210_call = mutated_mod.get_global_var('func_210')
var_4793 = relay.var("var_4793", dtype = "uint8", shape = (126, 3))#candidate|4793|(126, 3)|var|uint8
call_4792 = relay.TupleGetItem(func_206_call(relay.reshape(var_4793.astype('uint8'), [3, 9, 14]), relay.reshape(const_4781.astype('int32'), [3, 2, 10]), ), 2)
call_4794 = relay.TupleGetItem(func_210_call(relay.reshape(var_4793.astype('uint8'), [3, 9, 14]), relay.reshape(const_4781.astype('int32'), [3, 2, 10]), ), 2)
func_1356_call = mod.get_global_var('func_1356')
func_1360_call = mutated_mod.get_global_var('func_1360')
const_4796 = relay.const([-3,4,4,5,4,-2,-1,10,4,-7,9,-7,7,-7,2,-10,5,-8,10,8,-3,-1,-1,10,-5,4,-8,6,-4,6,1,8,1,-8,1,-5,6,9,-8,-5,-8,6,9,-1,-7,10,2,5,-5,-6,-8,-3,8,-4,-4,1,7,6,-1,10,4,7,7,1,6,-10,-8,-1,-8,-7,5,2,5,-7,-7,-4,6,-8,5,4,-7,-6,-9,5,3,8,8,-7,2,-1,2,9,-9,10,8,-5,-8,10,-9,5,-7,-7,4,1,-1,-4,-8,-10,2,2,4,5,-8,1,1,7,-8,-4,10,10,-8,4,-9,-2,6,3,1,4,-4,-9,1,-3,-2,-3,4,4,8,-7,-4,-10,-5,2,10,7,1,8,-4,10,10,8,7,-6,-4,3,-4,-10,-5,-4,8,-8,-7,-8,-7,-7,-2,-3,-1,-3,3,-2,-9,5,3,-9,-3,8,3,-3,6,1,6,-6,-4,1,7,6,4,-9,3,7,-7,9,3,-4,3,7,-1,6,2,-5,-1,-4,-4,-1,3,6,3,1,7,-4,-1,2,6,7,7,8,3,-10,-6,-6,9,8,7,-7,-5,7,-4,7,-8,9,-4,-1,8,6,4,-3,-5,-2,-2,-7,2,2,4,7,4,7,-10,7,-4,1,8,-9,-9,-3,2,8,7,-1,1,-3,1,-3,2,10,-6,2,-7,4,3,-6,9,-6,-8,-7,4,-4,-4,7,-10,2,10,-9,-6,-2,2,2,6,8,-7,-2,9,-8,-6,10,4,3,7,-10,5,-2,1,-8,5,8,-5,5,-10,-6,7,-4,8,-4,9,8,3,-9,-5,1,5,2,-2,3,-9,10,-4,9,-2,-7,-5,3,4,-4,2,-10,5,-6,-10,-10,-9,9,5,-5,10,-7,8,5,-5,2,-6,-4,-4,-9,1,-3,2,-6,-9,5,5,-6,-4,-5,-10,4,-7,7,1,6,-7,-4,1,7,3,1,6,10,-6,6,-2,-4,-9,10,10,3,5,8,7,7,-9,-7,4,2,-4,10,9,3,-6,9,1,5,9,-3,1,8,8,7,-5,-4,9,5,9,-7,2,-2,8,-8,-3,5,1,-5,1,1,-3,6,-10,-2,-10,-3,-7,-5,2,-3,-4,-10,4,-4,-9,4,1,-6,3,-7,8,-3,-4,-9,-4,3,1,-5,-9,1,-5,2,4,-6,-7,-10,-4,8,-3,-6,7,7,3,2,-2,-1,-7,4,4,-10,4,6,3,7,10,5,3,7,3,-9,6,3,-7,-7,-8,10,9,1,9,-7,9,10,3,9,9,-4,-10,-8,-5,-7,-6,-6,-4,-4,-3,6,5,6,-3,6,5,-7,-7,1,2,5,-7,-2,6,-6,8,-10,5,-9,-3,10,-2,-2,-4,1,4,-5,-6,4,2,10,-1,1,10,-6,-6,10,5,-9,8,-8,-7,-1,-9,-5,-4,-1,7,3,-3,-10,-7,-8,-4,-3,8,-3,2,6,-1,-4,-5,-2,-6,-2,3,-9,4,-5,4,-3,7,7,-3,3,-3,-1,-2,3,-7,1,8,-2,-7,3,5,6,-1,3,6,-8,-5,-9,1,6,-8,-9,7,1,10,-7,-9,5,6,3,-6,-2,9,7,-5,9,-10,-2,-2,8,4,-5,10,2,-9,-9,8,-3,3,9,5,-1,-6,9,-5,-10,-4,-3,-4,-2,2,8,-3,8,-3,3,-7,-10,-9,-1,-7,5,-5,-8,3,-3,-1,6,-4,-9,-1,4,9,1,4,-2,4,-6,6,-9,4,-4,5,-9,4,5,-10,-3,4,9,-7,-10,-10,1,10,3,-4,-1,8,-7,7,8,-2,8,-5,3,-10,3,1,4,-6,7,7,-8,-7,-7,-6,4,6,-3,9,-2,-10,8,3,-7,10,-8,4,-2,-10,7,-4,5,3,10,5,-2,1,10,-2,2,1,-9,-3,-5,-1,-2,-5,4,4,-1,-10,-5,1,-4,2,-6,-5,7,-7,-2,7,3,10,10,-5,-4,-2,-7,-6,-7,-6,-9,-10,-10,9,7,-5,-7,-10,-10,8,10,-7,-6,-8,9,-7,-7,-7,6,-9,3,3,-3,-9,-8,9,10,4,8,10,-8,-8,-6,1,10,-2,8,-4,-8,3,3,-3,7,8,1,-5,-7,-5,-7,-4,8,1,-1,6,10,-5,-1,-6,8,-6,-2,-10,-3,1,-3,8,-2,9,5,-5,5,8,10,8,9,-9,-6,-1,3,-10,8,-8,-6,4,-2,-6,8,-7,-7,-8,-1,-7,-5,-8,2,-7,-4,1,-3,1,3,-6,-9,-9,10,-5,2,9,-2,-10,-3,-5,5,8,10,-7,5,1,-8,2,-8,8,9,-9,-2,-5,9,3,5,-2,-9,5,-2,-9,9,-8,-8,-8,2,10,-8,1,5,9,-5,5,2,9,-10,-6,-10,7,9,-5,-3,-6,-9,8,1,6,-2,2,-2,-8,1,-1,-8,-9,2,-9,8,-5,2,-3,-3,-1,-9,-9,-5,-1,-2,-7,1,-7,-7,-7,4,6,-7,1,7,5,4,-6,2,5,-10,-4,6,5,10,2,5,-9,6,-4,-9,-8,-4,4,-2,10,1,4,-7,-5,-10,-10,5,-1,9,-4,6,-3,-4,8,8,-9,-2,-10,-1,-6,2,-8,-5,-9,-6,-5,5,-3,-7,-7,1,-5,7,1,-10,1,-3,10,9,4,-10,-8,-7,4,-3,10,-6,-6,10,-3,6,-2,-2,-7,-2,6,10,-7,-4,2,3,-3,6,-2,-7,-7,-8,2,-1,-10,-1,-5,10,-9,-6,-4,-2,-7,-6,-7,5,-8,2,2,-10,-6,-9,-6,-4,3,-6,10,6,10,-8,7,-8,-8,-4,6,3,8,5,-10,9,-1,-2,4,-8,-10,-1,4,9,-2,2,-8,9,6,-8,-5,10,1,-8,-10,1,-5,-6,-2,10,-9,-1,9,10,6,-2,6,-8,5,-4,-2,-4,7,-5,6,-2,-2,-1,3,-6,1,1,-1,-6,2,-1,7,1,-7,1,-6,8,6,-6,-3,9,2,3,6,10,-1,4,8,10,-4,1,-5,-5,-10,-1,5,9,9,-1,-1,-7,-1,10,4,5,4,7,4,-10,5,7,3,-7,6,-9,6,1,5,-7,5,9,7,-9,-8,-3,-2,10,6,8,-5,3,3,1,9,-8,-9,4,-3,-4,3,3,-2,3,-2,2,-7,9,10,9,7,2,6,-1,-10,-3,6,10,-1,-4,3,-2,-10,2,2,-9,-3,-6,-8,2,-4,3,-1,6,6,-8,-7,-1,3,8,7,6,-8,-10,1,-6,-5,3,-2,9,-10,-8,7,-5,-3,8,10,-1,-6,7,-1,2,-4,3,5,-7,-10,3,2,-10,3,-6,-9,3,8,-5,-5,-8,-4,-6,-4,8,-5,1,-3,6,-8,8,9,-5,1,7,-10,4,5,-7,-4,3,7,9,-7,-5,7,-2,-5,3,-8,-2,3,-4,-10,7,5,-3,6,-2,9,5,9,2,4,-9,-8,-3,-9,-9,-6,-10,8,3,7,6,1,4,9,-3,3,-9,5,2,-7,-2,9,5,-7,-1,2,-2,1,2,-2,-6,10,-6,7,8,8,8,4,-7,2,9,7,6,9,-1,6,8,3,1,-1,-4,1,-10,-7,-9,-5,2,10,-4,-9,-10,2,-1,1,5,-2,-4,-2,9,-1,8,-5,-10,10,3,-8,-4,-8,-5,8,-4,-8,-1,-1,10,9,8], dtype = "int8")#candidate|4796|(1408,)|const|int8
call_4795 = relay.TupleGetItem(func_1356_call(relay.reshape(const_4796.astype('int8'), [11, 8, 16]), relay.reshape(const_4796.astype('int8'), [11, 8, 16]), ), 1)
call_4797 = relay.TupleGetItem(func_1360_call(relay.reshape(const_4796.astype('int8'), [11, 8, 16]), relay.reshape(const_4796.astype('int8'), [11, 8, 16]), ), 1)
uop_4808 = relay.acosh(call_4780.astype('float32')) # shape=(3, 2, 10)
uop_4810 = relay.acosh(call_4782.astype('float32')) # shape=(3, 2, 10)
func_1789_call = mod.get_global_var('func_1789')
func_1792_call = mutated_mod.get_global_var('func_1792')
const_4817 = relay.const([-5,2,-9,6,-3,4,6,-6,3,-5,2,-3,8,7,3,6,-8,-3,-5,8,2,9,5,2,-9,9,2,-6,-8,-10,-6,-10,-9,1,4,1,-3,-3,-4,-8,-5,6,-3,-10,5,1,-8,-6,-5,-8,8,6,-10,10,5,-10,-9,8,9,2,-7,5,-5,2,-10,9,-2,9,-4,-9,-9,1,-5,9,-8,8,-3,3,-6,7,7,-3,-3,-10,-3,9,-8,-1,3,7,-10,-9,7,-2,6,8,9,2,-6,-2,3,-1,4,-4,-2,6,-5,5,-6,-5,-8,8,4,9,2,9,3,-6,1,-1,2,-5,4,-9,8,-7,-6,-4,-4,-10,-4,-2,8,3,-8,2,-6,9,6,-4,-3,-1,-5,1,7,6,2,-10,5,-10,2,5,7,-7,1,9,2,4,6,7,-7,-7,-10,-9,-4,8,-1,3,-4,-2,4,8,3,5,7,3,6,5,10,-9,-3,10,9,-1,-6,7,-6,5,-8,9,4,-9,3,-4,-8,-5,1,4,-9,-2,-9,6,-5,5,3,7,5,6,2,10,5,2,3,8,2,-8,9,8,-4,7,8,-5,-2,2,-2,-5,-8,-5,-4,2,2,-8,-3,-7,9,4,-2,2,-9,9,5,-8,-10,3,-7,1,-6,-4,-5,-5,7,-4,8,2,-10,-7,-6,9,2,-1,8,10,-10,10,7,2,5,-4,1,10,-8,6,4,9,7,6,-9,7,3,5,-5,6,2,-2,-6,4,-1,-8,-6,-2,-5,8,7,5,5,3,-6,9,-9,-3,-5,-8,7,-1,1,8,4,-3,-1,4,-10,-7,6,-6,-1,9,-4,-2,1,8,1,-1,1,-7,-2,-10,9,-9,-5,7,4,2,3,2,9,9,5,-6,-3,1,-5,-10,-10,9,-5,-9,-4,-8,-7,2,-8,8,10,10,-9,1,-1,10,1,7,10,7,-9,3,-5,3,-6,7,-5,9,7,7,10,-1,9,-9,4,-2,-10,8,-10,1,2,-1,-6,-10,-10,-2,8,-3,1,-5,9,7,-4,5,6,1,-5,-6,5,-5,-6,-7,-2,1,-2,6,6,1,8,8,-3,3,-3,8,-6,-5,9,5,2,-5,-2,6,-6,-2,6,-10,10,8,4,-3,8,-1,8,10,-1,4,8,5,-8,8,-6,-4,4,10,-7,-6,-1,-4,4,10,-1,-1,6,-10,-3,-10,-7,-3,-4,8,-8,-8,1,7,-8,-1,3,7,-9,4,7,1,8,-4,-9,-6,7,3,8,5,8,6,-9,-1,-1,-10,-10,-2,-5,3,-1,10,-4,9,-4,7,-10,3,7,-10,8,-5,-9,7,5,9,-8,5,-1,-4,-9,-8,4,-10,7,9,8,-4,-3,4,-2,6,-9,1,-5,6,6,3,-5,-10,3,-8,5,9,-6,6,5,7,2,7,-1,-3,6,6,1,4,7,-4,-7,-2,7,10,-9,9,2,-1,8,1,-10,-5,-5,4,2,-6,-4,-3,-6,6,-9,9,8,6,3,-9,-4,-5,-3,3,-8,8,7,4,4,1,2,5,-7,7,-10,-5,1,5,1,-3,9,3,-3,-1,7,-10,-9,1,8,8,-6,-4,4,-3,9,4,-5,4,-3,5,-7,1,2,6,1,1,10,4,-7,9,-1,4,1,6,-6,-6,-7,-1,-8,-2,2,6,-9,5,5,3,-8,-4,6,-3,-4,-5,5,-2,4,1,7,9,-6,-1,-8,-9,-1,3,6,10,-8,-10,5,-5,-6,-7,4,9,10,-2,-2,3,7,-1,-6,10,-9,7,2,3,10,3,7,3,9,6,-10,5,6,10,-8,-6,-1,-1,6,-5,5,10,7,1,-3,-9,3,10,-1,-3,-1,6,-3,6,-10,-8,6,-8,3,3,4,9,-8,-9,9,8,1,1,8,5,-8,-4,1,1,9,8,-6,3,5,-4,5,4,5,-2,-5,-2,10,-1,-8,-4,6,2,-8,7,8,10,3,-9], dtype = "int8")#candidate|4817|(756,)|const|int8
call_4816 = relay.TupleGetItem(func_1789_call(relay.reshape(const_4817.astype('int8'), [7, 12, 9]), relay.reshape(const_4817.astype('int8'), [7, 12, 9]), ), 1)
call_4818 = relay.TupleGetItem(func_1792_call(relay.reshape(const_4817.astype('int8'), [7, 12, 9]), relay.reshape(const_4817.astype('int8'), [7, 12, 9]), ), 1)
func_1954_call = mod.get_global_var('func_1954')
func_1958_call = mutated_mod.get_global_var('func_1958')
const_4824 = relay.const([0.279008,0.583075,-9.177667,9.304494,-1.135420,-4.739522,9.329094,7.115394,7.244867,-7.571038,7.589705,-2.880065,1.378470,-6.887476,6.400520,3.483544,-6.827372,5.782972,3.965885,-1.929055,-2.586090,2.886930,-2.159228,5.728028,-5.341024,8.432556,-2.049291,-0.306331,-7.147258,-0.970137,-1.592550,-0.191353,6.339370,-4.194416,-3.490349,-8.975445,5.350294,5.342228,-0.571332,1.477533,-2.220673,3.597357,9.292704,-8.920914,-1.516678,2.171749,-5.139506,6.442435,-8.424655,3.688678,-7.795872,4.665248,7.834097,3.441093,8.899169,-0.208780,1.951083,-2.416317,0.638618,4.193820,-9.876659,4.937937,-8.296589,-1.209656,-2.049432,-0.455795,1.161014,-4.464715,-7.368977,4.018487,9.986941,4.023120,5.483773,9.451577,1.972003,-5.673924,5.850212,-6.593608,-4.752476,-5.211050,-7.856644,1.247214,5.096410,-9.839634,-3.716105,1.730694,1.736530,-1.572482,6.663662,-7.964658,-1.736037,-4.602068,-5.590786,-9.355131,6.692479,7.298667,1.378512,7.992709,-7.475206,-9.272518,6.527520,-4.153473,-2.936519,5.685267,-8.469020,-3.485247,-0.256845,2.346165,-0.663699,3.109535,-0.095502,1.925272,-5.893606,-1.895004,6.193681,7.958177,8.767179,6.734907,-5.840575,0.420159,-3.569279,-9.774541,-2.063162,4.296690,1.241409,-3.396349,1.439895,3.938653,-7.615178,8.538165,-3.978079,8.317698,-6.455599,3.431217,8.404060,-1.692710,4.633760,8.152950,-7.270934,-8.419754], dtype = "float32")#candidate|4824|(140,)|const|float32
call_4823 = relay.TupleGetItem(func_1954_call(relay.reshape(const_4824.astype('float32'), [4, 5, 7]), relay.reshape(const_4824.astype('float32'), [4, 5, 7]), ), 3)
call_4825 = relay.TupleGetItem(func_1958_call(relay.reshape(const_4824.astype('float32'), [4, 5, 7]), relay.reshape(const_4824.astype('float32'), [4, 5, 7]), ), 3)
output = relay.Tuple([uop_4762,call_4776,var_4777,const_4781,call_4792,var_4793,call_4795,const_4796,uop_4808,call_4816,const_4817,call_4823,const_4824,])
output2 = relay.Tuple([uop_4762,call_4778,var_4777,const_4781,call_4794,var_4793,call_4797,const_4796,uop_4810,call_4818,const_4817,call_4825,const_4824,])
func_4826 = relay.Function([var_4761,var_4777,var_4793,], output)
mod['func_4826'] = func_4826
mod = relay.transform.InferType()(mod)
var_4827 = relay.var("var_4827", dtype = "float32", shape = (15, 2, 10))#candidate|4827|(15, 2, 10)|var|float32
var_4828 = relay.var("var_4828", dtype = "float64", shape = (48, 4))#candidate|4828|(48, 4)|var|float64
var_4829 = relay.var("var_4829", dtype = "uint8", shape = (126, 3))#candidate|4829|(126, 3)|var|uint8
output = func_4826(var_4827,var_4828,var_4829,)
func_4830 = relay.Function([var_4827,var_4828,var_4829,], output)
mutated_mod['func_4830'] = func_4830
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5050 = relay.var("var_5050", dtype = "float32", shape = (16, 1, 11))#candidate|5050|(16, 1, 11)|var|float32
uop_5051 = relay.acosh(var_5050.astype('float32')) # shape=(16, 1, 11)
output = relay.Tuple([uop_5051,])
output2 = relay.Tuple([uop_5051,])
func_5056 = relay.Function([var_5050,], output)
mod['func_5056'] = func_5056
mod = relay.transform.InferType()(mod)
mutated_mod['func_5056'] = func_5056
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5057 = relay.var("var_5057", dtype = "float32", shape = (16, 1, 11))#candidate|5057|(16, 1, 11)|var|float32
func_5056_call = mutated_mod.get_global_var('func_5056')
call_5058 = func_5056_call(var_5057)
output = call_5058
func_5059 = relay.Function([var_5057], output)
mutated_mod['func_5059'] = func_5059
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5338 = relay.var("var_5338", dtype = "bool", shape = (7, 9, 5))#candidate|5338|(7, 9, 5)|var|bool
var_5339 = relay.var("var_5339", dtype = "bool", shape = (7, 9, 5))#candidate|5339|(7, 9, 5)|var|bool
bop_5340 = relay.logical_and(var_5338.astype('bool'), relay.reshape(var_5339.astype('bool'), relay.shape_of(var_5338))) # shape=(7, 9, 5)
bop_5349 = relay.logical_or(var_5338.astype('bool'), relay.reshape(bop_5340.astype('bool'), relay.shape_of(var_5338))) # shape=(7, 9, 5)
func_1396_call = mod.get_global_var('func_1396')
func_1399_call = mutated_mod.get_global_var('func_1399')
var_5364 = relay.var("var_5364", dtype = "bool", shape = (56, 2))#candidate|5364|(56, 2)|var|bool
call_5363 = relay.TupleGetItem(func_1396_call(relay.reshape(var_5364.astype('bool'), [16, 7, 1])), 0)
call_5365 = relay.TupleGetItem(func_1399_call(relay.reshape(var_5364.astype('bool'), [16, 7, 1])), 0)
func_10_call = mod.get_global_var('func_10')
func_13_call = mutated_mod.get_global_var('func_13')
const_5374 = relay.const([-9,-8,-8,-2,3,2,4,-1,8,4,-3,3,7,5,-5,-6,3,-1,-8,-1,4,10,-7,-2,-3,2,1,-9,3,-2,2,-3,5,6,-6,2,-2,-7,5,4,8,-5,3,-7,-10,5,8,7,-3,-5,-1,8,-1,-4,6,6,6,-3,7,-5], dtype = "int32")#candidate|5374|(60,)|const|int32
call_5373 = func_10_call(relay.reshape(const_5374.astype('int32'), [3, 2, 10]), relay.reshape(const_5374.astype('int32'), [3, 2, 10]), )
call_5375 = func_10_call(relay.reshape(const_5374.astype('int32'), [3, 2, 10]), relay.reshape(const_5374.astype('int32'), [3, 2, 10]), )
func_2765_call = mod.get_global_var('func_2765')
func_2774_call = mutated_mod.get_global_var('func_2774')
const_5380 = relay.const([[3,5],[5,1],[9,-7],[9,6],[10,-6],[4,9],[-7,-3],[-3,7],[-10,-1],[8,-1],[9,7],[5,5],[-1,-8],[-1,8],[-5,4],[-8,5],[5,-5],[6,-10],[-3,-7],[2,-6],[5,10],[10,-3],[-9,-5],[9,-6],[-4,9],[-6,6],[-6,10],[5,1],[-9,-5],[10,-5],[6,-5],[10,1],[-2,-5],[-9,-10],[4,-5],[5,8],[-8,4],[-2,9],[1,-2],[5,4],[-4,-8],[9,-10],[-7,1],[-10,3],[-3,-9],[7,2],[-2,-8],[8,6],[10,8],[1,2],[2,7],[4,3],[-8,4],[-10,1],[9,-7],[-1,2],[9,1],[-8,8],[-8,-4],[-7,-2],[1,10],[10,-1],[3,9],[-3,5],[1,-1],[-1,-10],[4,-1],[-3,5],[9,-5],[-7,10],[-4,-5],[-10,-8],[8,-1],[-8,6],[-5,4],[10,-3],[-5,9],[-5,-3],[8,6],[8,-8],[-5,5],[-9,9],[8,3],[-1,8],[-7,9],[6,8],[9,1],[-2,-4],[-7,4],[10,10],[-5,9],[-1,3],[5,-9],[3,6],[-3,-1],[-9,4],[6,2],[1,5],[8,3],[2,-9],[-9,10],[6,-6],[-7,6],[2,2],[9,-3],[7,-6],[3,-4],[7,-3],[-2,10],[3,6],[3,-5],[-3,-6],[-10,-3],[-8,-4],[10,7],[3,-6],[5,10],[-4,-9],[10,5],[-1,-6],[-9,-10],[7,9],[3,-7],[-7,9],[10,1],[8,2],[-4,-3],[-5,5],[-7,-10],[-10,4],[-4,2],[-7,-3],[-2,1],[-4,10],[-10,-2],[2,-9],[-4,-5],[-10,2],[3,5],[-4,-7],[5,-8],[2,9],[-3,-7],[8,-5],[-6,1],[-1,-10],[-4,4],[-5,6],[-10,-1],[2,-2],[-10,-1],[-6,-3],[7,8],[4,4],[-5,7],[1,10],[-8,2],[10,7],[5,-8],[-2,-3],[2,9],[-1,5],[-3,-8],[4,6],[10,1],[3,9],[6,7],[8,-9],[3,-6],[2,2],[4,2],[1,-1],[5,2],[2,6],[-9,-7],[4,7],[5,2],[7,-5],[-6,-10],[-2,-10],[4,6],[3,5],[-4,-9],[10,6],[1,3],[1,-10],[4,6],[4,-4],[7,-6],[2,2],[-6,4],[7,1],[7,-8],[3,-7],[-2,2],[8,4],[-8,6],[4,5],[9,3],[-9,-5],[-8,5],[3,-8],[-5,-8],[-10,10],[3,-5],[-4,-6],[-10,-8],[-5,5],[6,-7],[-4,-3],[-7,1],[5,3],[-7,-6],[1,-3],[-1,1],[-4,9],[8,2],[-1,10],[7,-5],[-5,2],[-9,3],[10,-10],[-9,-7],[7,6],[10,-7],[2,-8],[9,5],[4,-5],[8,2],[6,-9],[2,9],[-9,-5],[10,1],[9,4],[7,-9],[-7,-3],[-4,10],[-4,8],[-4,7],[1,-4],[4,-4],[-9,9],[8,-6],[-6,-7],[-1,-4],[-8,2],[9,-5],[1,-1],[7,8],[-6,1],[-6,-6],[-3,3],[-1,-10],[7,-9],[1,-7],[5,5],[-5,-7],[9,4],[6,-10],[-4,4],[9,-2],[-6,-5],[7,9],[-1,-4],[-9,-7],[1,-6],[3,8],[8,-1],[-8,5],[8,-2],[3,-6],[6,-1],[1,5],[-1,-2],[6,2],[-4,3],[7,-5],[-2,-9],[8,9],[5,9],[8,-1],[5,-3],[-3,-7],[7,-8],[-9,-1],[-10,6],[-8,-2],[-3,-1],[6,-9],[-3,-2],[-5,-3],[8,-9],[4,10],[2,4],[10,-3],[8,3],[-3,-5],[-5,3],[5,-6],[-7,3],[-7,-5],[-8,-9],[6,1],[-3,8],[-9,4],[-1,5],[3,10],[-6,-1],[-6,2],[-7,10],[2,-9],[-8,-2],[-1,2],[-3,7],[-10,-6],[-10,1],[-5,-7],[3,-8],[-1,-9],[4,-7],[-6,-7],[7,7],[-1,-4],[-1,-6],[-8,-1],[-2,-6],[-5,-5],[6,6],[-2,5],[8,-7],[-4,-9],[-7,-1],[8,8],[2,5],[8,-10],[2,10],[-10,-3],[4,7],[-10,3],[3,-4],[8,3],[5,9],[9,-10],[5,5],[7,-4],[-6,1],[9,-5],[9,-7],[1,-9],[9,-10],[9,-9],[3,10],[2,1],[6,5],[-5,10],[-2,-1],[9,9],[-7,-8],[10,1],[-1,-3],[6,10],[5,7],[-8,4],[-4,-4],[4,-2],[-4,-9],[8,-10],[-2,4],[7,10],[-1,-2],[6,10],[-8,4],[6,2],[4,6],[3,3],[-9,3],[-10,7],[-2,10],[-6,9],[-5,-5],[8,-2],[-1,4],[-4,-9],[-3,10],[7,-7],[-8,-8],[-9,8],[1,4],[-5,2],[5,-1],[-5,4],[5,3]], dtype = "uint32")#candidate|5380|(392, 2)|const|uint32
const_5381 = relay.const([-7,4,2,-8,7,10,10,-9,-8,-6,1,10,3,-7,1,6,5,-4,3,-7,5,4,9,-10,4,-9,5,-8,-3,5,-7,4,2,-8,-1,7,2,1,7,-8,7,-7,-5,3,1,1,-8,1,-2,-4,2,7,7,5,1,-6,-9,3,9,3,3,-10,-9,-8,10,2,-5,7,-8,7,-8,-10,-7,2,-8,-8,8,-9,-8,6,10,9,-8,9,-1,-7,-3,-5,-9,-6,1,-7,3,6,4,-9,-1,-2,-7,6,1,-4,-10,5,-5,6,7,6,1,1,-7,2,1,6,-6,3,-6,2,-5,5,7,7,-7,4,-9,3,-7,4,10,-5,4,6,4,-6,-4,-10,-2,-5,-4,-9,5,-10,9,-10,8,5,-1,2,8,6,-6,-1,5,-9,6,-3,10,-3,9,-7,-7,7,-3,7,6,1,10,-4,1,-6,-1,-8,-2,9,-4,-6,-9,1,3,-1,-1,-3,-6,10,10,4,4,-2,3,-10,10,-6,-1,8,6,3,4,2,2,-9,7,4,5,10,9,-3,-7,7,9,-2,-7,-4,-2,2,8,8,3,9,-2,-6,-10,-10,-9,5,-4,-10,-1,-1,1,-10,-3,6,-2,5,-5,-7,-9,2,-5,3,3,8,10,-10,3,1,8,-1,2,6,-7,2,1,-6,-10,-6,4,8,5,4,8,1,3,-10,-10,-2,-1,-4,8,-9,-9,-3,8,7,-1,-1,-8,-9,-6,8,7,-4,-6,-1,10,-5,6,2,-3,-9,-1,5,5,-4,5,9,-4,10,-3,4,-2,10,9,4,-2,6,3,5,-7,9,1,-4,10,4,-7,-5,-1,9,-9,-2,3,-6,-1,-4,-10,-2,10,-7,-2,-2,-1,-1,3,2,2,7,-4,-4,4,5,1,-4,-5,-1,-1,-7,-1,-7,-8,-8,-5,-8,8,5,-9,7,-10,-3,3,4,-7,8,-9,4,-8,-8,9,-3,9,10,-10,10,-9,7,-8,-8,1,-5,-3,-8,1,-3,3,9,3,9,-8,5,3,1,-4,6,-5,8,8,-8,-3,1,-8,-9,2,6,9,9,-5,3,9,5,-10,1,-8,-9,3,-10,-4,2,6,-6,-1,-7,7,-4,-9,10,3,-9,2,3,-2,6,1,-10,8,-4,-4,5,-2,6,9,3,9,2,-2,9,-9,9,-5,-1,-6,-3,-5,-2,9,-8,-5,-2,-3,-6,-1,-10,-1,4,-8,8,9,4,10,-1,-5,-9,2,-3,-6,-1,-5,9,7,-2,10,9,-1,-3,1,10,-3,-4,-10,9,9,3,10,-10,9,2,-1,-9,5,3,-6,-10,2,3,3,8,-3,-6,6,9,-9,5,1,-2,3,-10,10,7,6,-6,3,2,8,8,7,9,8,8,7,-6,7,1,-10,1,-10,6,2,9,8,-4,-7,-3,-7,4,10,6,8,7,6,3,-5,-1,-8,7,-10,-3,3,9,6,6,3,-5,9,-8,-10,-3,9,3,4,5,8,8,5,-1,-3,9,9,9,-8,5,10,-2,-1,8,5,-9,3,-6,7,9,6,-7,4,5,5,-7,-7,3,5,3,-5,5,-10,-6,8,-6,-5,-9,9,10,-3,8,-9,-10,-2,-4,-7,-7,-10,5,-2,10,6,-6,-3,-10,5,-8,8,-9,-5,7,4,1,1,-9,9,-10,-1,1,-5,2,-8,4,-10,-6,8,7,9,3,5,3,-3,10,-1,8,3,-6,10,-9,-5,-5,8,2,-1,-9,6,2,-7,5,-3,-6,3,-9,3,5,-3,-10,4,10,6,-2,3,4,-6,10,2,-8,-7,1,-5,8,7,-8,-10,6,8,-10,10,3,-5,-5,-8,-5,2,-4,10,-4,2,8,10,9,2,1,7,9,-8,10,-9,-8,1,-7,-4,10,3,-9,3,-3,7,-6,1,-8,-2,-2,3,2,-3,-9,-8,-4,-8,-5,1,4,3,4,-7,-2,9,10,5,-10,-8,7,7,-8,4,-3], dtype = "int8")#candidate|5381|(756,)|const|int8
const_5382 = relay.const([[-6.332368,2.859799,-0.598842,-5.226355,2.916248,5.376581,-0.672102,7.726695,6.027534,-4.843700,-1.774555,-4.225348,0.859827,-1.811233,1.571697,-5.786677,8.065537,-6.530794,-4.099467,-1.776721,-6.503004,-6.050487,5.869419,7.185235,-5.212904,9.779524,2.926916,6.998476,-8.579211,6.147562,7.046627,0.218336,2.519401,3.832713,-3.632081,8.440560,9.924167,0.719150,2.700198,-8.260337,7.635559,-6.168917,6.239047,5.634737,6.002712,8.690461,-2.517945,-4.173652,-9.407338,6.846277,1.649725,5.894551,1.129586,6.866545,6.765258,-2.626681,-5.477996,8.339297,-4.738101,8.769802,9.130524,6.779247,8.294016,5.516870,3.253008,-4.114235,-2.564149,8.394236,4.032121,-6.933004,-7.681981,4.409953,-0.017610,-5.827069,1.906602,-4.938472,-8.260415,-7.255470,0.563199,3.785527,-0.225236,4.673421,0.652021,-8.850373,-6.739325,5.888392,0.184560,4.616435,-3.298830,8.224558,3.298753,-5.050323,7.948249,0.963276,2.733034,7.621761,-5.826004,-0.025910,5.203973,-2.262140,3.156364,0.819309,-9.751299,-9.468998,-5.223235,-1.512297,-5.962236,-3.941768,8.159222,-7.084823,-9.834765,5.922747,8.148447,6.762386,-9.445853,-4.002878,0.551011,7.209669,-3.875330,-2.463152,2.163895,-9.955779,-7.512133,7.996389,-6.336535,-3.826546,8.954338,0.283186,5.002160,0.705017,1.056277,3.672372,6.117624,-0.400315,9.691940,4.980972,-7.027981,-1.085463,-4.165299,-5.239145,8.769981,1.638857,-5.303400,9.196222,3.284158,-1.595384,-3.400788,-0.165692,-1.747622,5.608776,1.421844,-4.676354,-8.740144,-9.404208,-0.113878,5.864364,8.193638,-0.357323,-5.196162,3.028765,-4.433063,-4.636702,-1.456205,1.290680,9.736300,-0.614779,4.554636,-4.619554,5.946975,-5.333848,-9.258174,3.226780,-7.561701,0.492476,-9.037785,6.499526,-6.512877,4.842573,-0.178387,4.802459,-1.578756,-9.392450,-8.672485,4.295456,-6.049504,4.161218,-6.116348,-6.589036,-3.871998,4.872654,9.001802,-6.285514]], dtype = "float64")#candidate|5382|(1, 192)|const|float64
var_5383 = relay.var("var_5383", dtype = "float64", shape = (252,))#candidate|5383|(252,)|var|float64
var_5384 = relay.var("var_5384", dtype = "uint8", shape = (378,))#candidate|5384|(378,)|var|uint8
call_5379 = relay.TupleGetItem(func_2765_call(relay.reshape(const_5380.astype('uint32'), [8, 7, 14]), relay.reshape(const_5380.astype('uint32'), [8, 7, 14]), relay.reshape(const_5374.astype('int32'), [60,]), relay.reshape(const_5381.astype('int8'), [9, 84]), relay.reshape(const_5382.astype('float64'), [24, 8]), relay.reshape(var_5383.astype('float64'), [1, 252]), relay.reshape(var_5384.astype('uint8'), [378,]), ), 10)
call_5385 = relay.TupleGetItem(func_2774_call(relay.reshape(const_5380.astype('uint32'), [8, 7, 14]), relay.reshape(const_5380.astype('uint32'), [8, 7, 14]), relay.reshape(const_5374.astype('int32'), [60,]), relay.reshape(const_5381.astype('int8'), [9, 84]), relay.reshape(const_5382.astype('float64'), [24, 8]), relay.reshape(var_5383.astype('float64'), [1, 252]), relay.reshape(var_5384.astype('uint8'), [378,]), ), 10)
bop_5387 = relay.bitwise_or(var_5383.astype('int64'), call_5363.astype('int64')) # shape=(16, 7, 252)
bop_5390 = relay.bitwise_or(var_5383.astype('int64'), call_5365.astype('int64')) # shape=(16, 7, 252)
output = relay.Tuple([bop_5349,var_5364,call_5373,const_5374,call_5379,const_5380,const_5381,const_5382,var_5384,bop_5387,])
output2 = relay.Tuple([bop_5349,var_5364,call_5375,const_5374,call_5385,const_5380,const_5381,const_5382,var_5384,bop_5390,])
func_5392 = relay.Function([var_5338,var_5339,var_5364,var_5383,var_5384,], output)
mod['func_5392'] = func_5392
mod = relay.transform.InferType()(mod)
mutated_mod['func_5392'] = func_5392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5392_call = mutated_mod.get_global_var('func_5392')
var_5394 = relay.var("var_5394", dtype = "bool", shape = (7, 9, 5))#candidate|5394|(7, 9, 5)|var|bool
var_5395 = relay.var("var_5395", dtype = "bool", shape = (7, 9, 5))#candidate|5395|(7, 9, 5)|var|bool
var_5396 = relay.var("var_5396", dtype = "bool", shape = (56, 2))#candidate|5396|(56, 2)|var|bool
var_5397 = relay.var("var_5397", dtype = "float64", shape = (252,))#candidate|5397|(252,)|var|float64
var_5398 = relay.var("var_5398", dtype = "uint8", shape = (378,))#candidate|5398|(378,)|var|uint8
call_5393 = func_5392_call(var_5394,var_5395,var_5396,var_5397,var_5398,)
output = call_5393
func_5399 = relay.Function([var_5394,var_5395,var_5396,var_5397,var_5398,], output)
mutated_mod['func_5399'] = func_5399
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5448 = relay.var("var_5448", dtype = "int8", shape = ())#candidate|5448|()|var|int8
const_5449 = relay.const([[[4,9,2,-7,-2,-9,-7,-4,-3,-9,-8],[-6,4,-6,-8,8,-4,6,-2,4,-1,-10],[-6,-1,1,-6,2,4,4,8,-2,5,-3]]], dtype = "int8")#candidate|5449|(1, 3, 11)|const|int8
bop_5450 = relay.right_shift(var_5448.astype('int8'), const_5449.astype('int8')) # shape=(1, 3, 11)
output = bop_5450
output2 = bop_5450
func_5457 = relay.Function([var_5448,], output)
mod['func_5457'] = func_5457
mod = relay.transform.InferType()(mod)
var_5458 = relay.var("var_5458", dtype = "int8", shape = ())#candidate|5458|()|var|int8
output = func_5457(var_5458)
func_5459 = relay.Function([var_5458], output)
mutated_mod['func_5459'] = func_5459
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5504 = relay.const([[[5,1],[-8,-1],[-1,-3],[-8,7],[-6,-3],[-2,6],[-4,3],[-2,-3],[-3,-5],[5,6],[-8,9],[1,5]],[[4,2],[6,1],[1,-6],[-7,1],[3,-10],[9,-2],[-6,6],[8,5],[-9,7],[-5,5],[-4,-8],[-8,-10]],[[-7,9],[8,-5],[-4,-4],[-2,4],[7,7],[4,7],[-3,-1],[-6,-1],[-3,6],[-2,8],[2,8],[-2,-5]],[[8,1],[4,-9],[3,-7],[1,9],[-8,7],[-10,6],[8,7],[-8,1],[4,5],[-1,4],[-6,-4],[-9,-3]],[[10,9],[-5,-3],[8,-3],[2,-2],[7,4],[-4,4],[9,1],[1,-7],[3,2],[-10,1],[4,-8],[-9,5]],[[-8,3],[-9,-5],[5,8],[-7,-6],[2,10],[-4,4],[4,-6],[-10,8],[4,-1],[-10,-3],[10,10],[8,-2]]], dtype = "int32")#candidate|5504|(6, 12, 2)|const|int32
const_5505 = relay.const([[[-1,10],[7,-6],[-6,-7],[-9,1],[-8,3],[-9,5],[10,-10],[4,-5],[-7,8],[-4,-10],[5,9],[6,8]],[[-4,-6],[-9,-4],[-4,8],[-6,-4],[-7,7],[-7,2],[-8,7],[-8,8],[5,-5],[-6,7],[-5,7],[-9,-6]],[[-3,8],[2,3],[-8,2],[5,-1],[5,-7],[7,8],[-9,3],[7,-4],[2,2],[3,-4],[6,-8],[7,1]],[[7,10],[10,-6],[-6,-6],[-10,-7],[4,8],[5,-8],[-9,1],[-8,-9],[-10,9],[-8,6],[-5,9],[3,-2]],[[5,2],[-4,-2],[9,-3],[8,1],[1,-6],[6,5],[6,-1],[-9,-8],[2,6],[-2,-1],[4,5],[-5,9]],[[-8,-5],[9,-6],[-3,8],[9,-8],[-5,9],[1,-6],[5,6],[-10,6],[-10,-2],[2,-7],[-6,-10],[-10,8]]], dtype = "int32")#candidate|5505|(6, 12, 2)|const|int32
bop_5506 = relay.right_shift(const_5504.astype('int32'), relay.reshape(const_5505.astype('int32'), relay.shape_of(const_5504))) # shape=(6, 12, 2)
output = bop_5506
output2 = bop_5506
func_5512 = relay.Function([], output)
mod['func_5512'] = func_5512
mod = relay.transform.InferType()(mod)
output = func_5512()
func_5513 = relay.Function([], output)
mutated_mod['func_5513'] = func_5513
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5575 = relay.var("var_5575", dtype = "float64", shape = (4, 16, 16))#candidate|5575|(4, 16, 16)|var|float64
var_5576 = relay.var("var_5576", dtype = "float64", shape = (4, 16, 16))#candidate|5576|(4, 16, 16)|var|float64
bop_5577 = relay.floor_divide(var_5575.astype('float64'), relay.reshape(var_5576.astype('float64'), relay.shape_of(var_5575))) # shape=(4, 16, 16)
func_1396_call = mod.get_global_var('func_1396')
func_1399_call = mutated_mod.get_global_var('func_1399')
const_5583 = relay.const([True,False,True,True,True,False,False,False,True,False,False,False,False,False,True,True,True,False,True,False,False,False,True,False,False,True,False,True,True,True,False,False,True,True,True,True,False,False,True,True,False,False,True,True,False,True,False,True,True,True,True,False,False,True,False,False,False,False,False,True,True,False,False,True,True,True,False,True,True,True,False,False,True,False,True,True,True,True,False,False,True,False,False,True,True,False,True,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,True,False,True,False,False,False,False,False,False,True], dtype = "bool")#candidate|5583|(112,)|const|bool
call_5582 = relay.TupleGetItem(func_1396_call(relay.reshape(const_5583.astype('bool'), [16, 7, 1])), 0)
call_5584 = relay.TupleGetItem(func_1399_call(relay.reshape(const_5583.astype('bool'), [16, 7, 1])), 0)
func_2936_call = mod.get_global_var('func_2936')
func_2940_call = mutated_mod.get_global_var('func_2940')
var_5600 = relay.var("var_5600", dtype = "int32", shape = (1350,))#candidate|5600|(1350,)|var|int32
call_5599 = func_2936_call(relay.reshape(var_5600.astype('int32'), [15, 6, 15]), relay.reshape(var_5600.astype('int32'), [15, 6, 15]), )
call_5601 = func_2936_call(relay.reshape(var_5600.astype('int32'), [15, 6, 15]), relay.reshape(var_5600.astype('int32'), [15, 6, 15]), )
output = relay.Tuple([bop_5577,call_5582,const_5583,call_5599,var_5600,])
output2 = relay.Tuple([bop_5577,call_5584,const_5583,call_5601,var_5600,])
func_5604 = relay.Function([var_5575,var_5576,var_5600,], output)
mod['func_5604'] = func_5604
mod = relay.transform.InferType()(mod)
var_5605 = relay.var("var_5605", dtype = "float64", shape = (4, 16, 16))#candidate|5605|(4, 16, 16)|var|float64
var_5606 = relay.var("var_5606", dtype = "float64", shape = (4, 16, 16))#candidate|5606|(4, 16, 16)|var|float64
var_5607 = relay.var("var_5607", dtype = "int32", shape = (1350,))#candidate|5607|(1350,)|var|int32
output = func_5604(var_5605,var_5606,var_5607,)
func_5608 = relay.Function([var_5605,var_5606,var_5607,], output)
mutated_mod['func_5608'] = func_5608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5512_call = mod.get_global_var('func_5512')
func_5513_call = mutated_mod.get_global_var('func_5513')
call_5646 = func_5512_call()
call_5647 = func_5512_call()
output = call_5646
output2 = call_5647
func_5648 = relay.Function([], output)
mod['func_5648'] = func_5648
mod = relay.transform.InferType()(mod)
output = func_5648()
func_5649 = relay.Function([], output)
mutated_mod['func_5649'] = func_5649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5648_call = mod.get_global_var('func_5648')
func_5649_call = mutated_mod.get_global_var('func_5649')
call_5656 = func_5648_call()
call_5657 = func_5648_call()
output = relay.Tuple([call_5656,])
output2 = relay.Tuple([call_5657,])
func_5659 = relay.Function([], output)
mod['func_5659'] = func_5659
mod = relay.transform.InferType()(mod)
output = func_5659()
func_5660 = relay.Function([], output)
mutated_mod['func_5660'] = func_5660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5512_call = mod.get_global_var('func_5512')
func_5513_call = mutated_mod.get_global_var('func_5513')
call_5685 = func_5512_call()
call_5686 = func_5512_call()
func_1789_call = mod.get_global_var('func_1789')
func_1792_call = mutated_mod.get_global_var('func_1792')
var_5695 = relay.var("var_5695", dtype = "int8", shape = (756,))#candidate|5695|(756,)|var|int8
call_5694 = relay.TupleGetItem(func_1789_call(relay.reshape(var_5695.astype('int8'), [7, 12, 9]), relay.reshape(var_5695.astype('int8'), [7, 12, 9]), ), 0)
call_5696 = relay.TupleGetItem(func_1792_call(relay.reshape(var_5695.astype('int8'), [7, 12, 9]), relay.reshape(var_5695.astype('int8'), [7, 12, 9]), ), 0)
const_5704 = relay.const([[[2,-7],[5,-10],[9,9],[8,5],[6,3],[-10,8],[-7,4],[-10,-9],[10,7],[1,8],[-5,-3],[-10,-4]],[[-10,2],[5,-10],[4,-10],[-2,-7],[4,-6],[1,7],[10,-1],[-8,5],[-2,-8],[6,3],[-1,2],[-1,-6]],[[5,10],[-7,-4],[-4,-7],[9,-10],[10,2],[-5,-6],[8,-2],[9,4],[1,9],[-8,6],[9,-6],[-7,1]],[[-4,5],[-10,8],[9,6],[9,1],[3,-7],[-3,7],[-8,10],[9,5],[8,7],[-9,5],[6,-5],[3,-2]],[[-5,9],[3,10],[9,9],[3,5],[3,9],[-8,1],[6,-6],[3,-5],[-10,6],[10,-7],[8,-9],[1,2]],[[6,8],[-6,8],[7,8],[4,6],[-8,9],[10,7],[1,9],[-9,-6],[2,1],[-4,-9],[2,1],[-1,-2]]], dtype = "int32")#candidate|5704|(6, 12, 2)|const|int32
bop_5705 = relay.less(call_5685.astype('bool'), relay.reshape(const_5704.astype('bool'), relay.shape_of(call_5685))) # shape=(6, 12, 2)
bop_5708 = relay.less(call_5686.astype('bool'), relay.reshape(const_5704.astype('bool'), relay.shape_of(call_5686))) # shape=(6, 12, 2)
output = relay.Tuple([call_5694,var_5695,bop_5705,])
output2 = relay.Tuple([call_5696,var_5695,bop_5708,])
func_5733 = relay.Function([var_5695,], output)
mod['func_5733'] = func_5733
mod = relay.transform.InferType()(mod)
mutated_mod['func_5733'] = func_5733
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5734 = relay.var("var_5734", dtype = "int8", shape = (756,))#candidate|5734|(756,)|var|int8
func_5733_call = mutated_mod.get_global_var('func_5733')
call_5735 = func_5733_call(var_5734)
output = call_5735
func_5736 = relay.Function([var_5734], output)
mutated_mod['func_5736'] = func_5736
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5748 = relay.var("var_5748", dtype = "float32", shape = (5, 12, 8))#candidate|5748|(5, 12, 8)|var|float32
var_5749 = relay.var("var_5749", dtype = "float32", shape = (5, 12, 8))#candidate|5749|(5, 12, 8)|var|float32
bop_5750 = relay.maximum(var_5748.astype('float32'), relay.reshape(var_5749.astype('float32'), relay.shape_of(var_5748))) # shape=(5, 12, 8)
func_1144_call = mod.get_global_var('func_1144')
func_1147_call = mutated_mod.get_global_var('func_1147')
var_5775 = relay.var("var_5775", dtype = "float64", shape = (96, 2))#candidate|5775|(96, 2)|var|float64
call_5774 = func_1144_call(relay.reshape(var_5775.astype('float64'), [3, 4, 16]))
call_5776 = func_1144_call(relay.reshape(var_5775.astype('float64'), [3, 4, 16]))
func_5648_call = mod.get_global_var('func_5648')
func_5649_call = mutated_mod.get_global_var('func_5649')
call_5803 = func_5648_call()
call_5804 = func_5648_call()
func_5056_call = mod.get_global_var('func_5056')
func_5059_call = mutated_mod.get_global_var('func_5059')
var_5840 = relay.var("var_5840", dtype = "float32", shape = (4, 44))#candidate|5840|(4, 44)|var|float32
call_5839 = relay.TupleGetItem(func_5056_call(relay.reshape(var_5840.astype('float32'), [16, 1, 11])), 0)
call_5841 = relay.TupleGetItem(func_5059_call(relay.reshape(var_5840.astype('float32'), [16, 1, 11])), 0)
var_5847 = relay.var("var_5847", dtype = "float32", shape = (4, 44))#candidate|5847|(4, 44)|var|float32
bop_5848 = relay.bitwise_or(var_5840.astype('int64'), relay.reshape(var_5847.astype('int64'), relay.shape_of(var_5840))) # shape=(4, 44)
func_4826_call = mod.get_global_var('func_4826')
func_4830_call = mutated_mod.get_global_var('func_4830')
var_5859 = relay.var("var_5859", dtype = "float32", shape = (300,))#candidate|5859|(300,)|var|float32
const_5860 = relay.const([-1,-6,-10,-8,-5,-10,-6,5,-5,10,2,-8,6,-5,10,8,-1,-8,-1,8,9,-3,7,8,-10,9,-8,10,8,-7,-9,10,9,1,-6,-8,-8,-2,10,-10,-10,-2,-5,4,-10,-4,6,-7,3,7,-8,6,5,-3,-10,7,10,-10,-2,2,5,-10,-9,-10,-6,6,3,10,-10,4,3,-9,1,-10,4,-6,8,-2,3,-1,-10,-3,-9,-2,3,6,-9,9,-4,4,2,7,-4,-7,2,9,7,6,4,-2,3,-5,2,-2,-4,4,-6,4,-1,-10,10,-4,9,10,7,-2,-1,5,-2,2,3,2,7,1,8,1,-9,5,-7,3,9,6,-2,-7,-8,-10,7,2,9,-1,3,7,9,9,-8,-1,10,9,10,6,-7,1,-10,7,6,-8,-2,-10,6,-10,-6,3,10,-7,10,-10,-2,10,-6,3,8,1,-6,-2,4,9,5,-5,-6,7,8,4,10,3,-4,8,-10,2,1,10,-8,-5,-3,-9,-3,-8,6,10,-9,-4,1,-2,10,-9,-10,8,8,-2,-4,-1,-1,-7,-2,-5,-3,-1,-10,7,9,-2,-3,-10,4,5,4,6,-6,4,-1,6,-9,-10,1,8,-1,2,3,-6,-3,4,8,3,-4,-9,-8,-8,-3,-6,4,-6,-6,-1,-10,5,-10,1,10,2,-2,8,-8,-9,-5,-7,10,-5,2,7,-5,-5,3,4,1,5,9,-5,10,-9,-8,-5,2,9,6,-5,-8,7,-6,5,9,1,3,-6,-10,7,3,-8,-2,8,3,-10,-4,2,-9,7,9,5,-4,5,8,-3,6,4,10,-9,-5,-4,7,1,5,6,-8,5,2,5,6,10,1,3,8,-2,10,-4,-6,-4,4,6,-1,-1,3,-2,6,-2,-6,6,-6,6,8,4,6,-6,8,-2,5,1,-1,-10,4,4,6,3,10,-9,-1,2,-8,8,4,-4,-3,-8,9,3,-9,-3,-7,-10,-8,-5], dtype = "uint8")#candidate|5860|(378,)|const|uint8
call_5858 = relay.TupleGetItem(func_4826_call(relay.reshape(var_5859.astype('float32'), [15, 2, 10]), relay.reshape(call_5774.astype('float64'), [48, 4]), relay.reshape(const_5860.astype('uint8'), [126, 3]), ), 8)
call_5861 = relay.TupleGetItem(func_4830_call(relay.reshape(var_5859.astype('float32'), [15, 2, 10]), relay.reshape(call_5774.astype('float64'), [48, 4]), relay.reshape(const_5860.astype('uint8'), [126, 3]), ), 8)
uop_5866 = relay.sinh(call_5839.astype('float64')) # shape=(16, 1, 11)
uop_5868 = relay.sinh(call_5841.astype('float64')) # shape=(16, 1, 11)
uop_5877 = relay.tan(uop_5866.astype('float32')) # shape=(16, 1, 11)
uop_5879 = relay.tan(uop_5868.astype('float32')) # shape=(16, 1, 11)
output = relay.Tuple([bop_5750,call_5774,var_5775,call_5803,bop_5848,call_5858,var_5859,const_5860,uop_5877,])
output2 = relay.Tuple([bop_5750,call_5776,var_5775,call_5804,bop_5848,call_5861,var_5859,const_5860,uop_5879,])
func_5882 = relay.Function([var_5748,var_5749,var_5775,var_5840,var_5847,var_5859,], output)
mod['func_5882'] = func_5882
mod = relay.transform.InferType()(mod)
mutated_mod['func_5882'] = func_5882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5882_call = mutated_mod.get_global_var('func_5882')
var_5884 = relay.var("var_5884", dtype = "float32", shape = (5, 12, 8))#candidate|5884|(5, 12, 8)|var|float32
var_5885 = relay.var("var_5885", dtype = "float32", shape = (5, 12, 8))#candidate|5885|(5, 12, 8)|var|float32
var_5886 = relay.var("var_5886", dtype = "float64", shape = (96, 2))#candidate|5886|(96, 2)|var|float64
var_5887 = relay.var("var_5887", dtype = "float32", shape = (4, 44))#candidate|5887|(4, 44)|var|float32
var_5888 = relay.var("var_5888", dtype = "float32", shape = (4, 44))#candidate|5888|(4, 44)|var|float32
var_5889 = relay.var("var_5889", dtype = "float32", shape = (300,))#candidate|5889|(300,)|var|float32
call_5883 = func_5882_call(var_5884,var_5885,var_5886,var_5887,var_5888,var_5889,)
output = call_5883
func_5890 = relay.Function([var_5884,var_5885,var_5886,var_5887,var_5888,var_5889,], output)
mutated_mod['func_5890'] = func_5890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5512_call = mod.get_global_var('func_5512')
func_5513_call = mutated_mod.get_global_var('func_5513')
call_5897 = func_5512_call()
call_5898 = func_5512_call()
output = relay.Tuple([call_5897,])
output2 = relay.Tuple([call_5898,])
func_5899 = relay.Function([], output)
mod['func_5899'] = func_5899
mod = relay.transform.InferType()(mod)
mutated_mod['func_5899'] = func_5899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5899_call = mutated_mod.get_global_var('func_5899')
call_5900 = func_5899_call()
output = call_5900
func_5901 = relay.Function([], output)
mutated_mod['func_5901'] = func_5901
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5919 = relay.var("var_5919", dtype = "float32", shape = (2, 4, 8))#candidate|5919|(2, 4, 8)|var|float32
uop_5920 = relay.log10(var_5919.astype('float32')) # shape=(2, 4, 8)
bop_5922 = relay.bitwise_or(var_5919.astype('int32'), relay.reshape(uop_5920.astype('int32'), relay.shape_of(var_5919))) # shape=(2, 4, 8)
func_10_call = mod.get_global_var('func_10')
func_13_call = mutated_mod.get_global_var('func_13')
var_5930 = relay.var("var_5930", dtype = "int32", shape = (15, 4))#candidate|5930|(15, 4)|var|int32
call_5929 = func_10_call(relay.reshape(var_5930.astype('int32'), [3, 2, 10]), relay.reshape(var_5930.astype('int32'), [3, 2, 10]), )
call_5931 = func_10_call(relay.reshape(var_5930.astype('int32'), [3, 2, 10]), relay.reshape(var_5930.astype('int32'), [3, 2, 10]), )
func_2765_call = mod.get_global_var('func_2765')
func_2774_call = mutated_mod.get_global_var('func_2774')
const_5943 = relay.const([8,9,6,1,10,-8,-10,2,-10,10,8,2,-10,10,2,9,9,-2,-5,8,4,6,-7,-6,9,-10,7,-6,-4,-2,-10,-6,10,5,-2,-3,-3,10,7,-10,-3,5,4,-10,10,7,-2,-10,-1,-10,-1,1,9,-5,1,-3,6,6,-1,-10,-10,-10,8,-7,-8,3,-7,3,-8,-2,-4,3,5,1,8,7,-8,10,-9,-6,3,6,6,8,10,4,7,5,9,-9,7,4,-5,3,1,-8,-1,-6,6,2,6,-9,5,6,-9,-8,-3,4,-7,9,-6,-4,-3,-5,-6,4,-5,4,6,2,7,4,4,-7,4,-3,-6,9,-9,8,-3,7,5,8,3,9,-3,9,2,10,-3,6,10,-1,-10,-4,1,-1,-3,2,-10,-6,-5,-10,-3,10,-1,-7,4,10,5,6,-5,6,5,-6,8,-8,8,-7,6,7,8,8,10,-3,-2,-2,-6,-7,-6,-8,6,7,-3,3,6,9,-3,-3,9,-7,6,9,10,5,-10,10,8,-10,-2,2,-4,-1,2,-10,-3,-1,8,3,6,4,2,4,1,-2,-8,2,-7,-8,8,-1,7,-10,-2,3,-2,3,-10,3,-10,6,-1,-9,1,1,-7,8,2,1,10,1,-8,5,1,1,5,9,-6,-6,8,-4,-8,1,10,-6,-5,-6,1,-2,1,4,-1,-2,1,-1,3,-6,-8,3,-10,-2,-5,-7,-10,-9,-4,-5,-5,-1,-6,5,-10,2,-9,-7,5,-1,10,7,9,-10,-8,-6,-3,9,-1,-9,-9,-8,8,-7,-7,-3,8,-6,5,-8,1,6,-2,3,3,-2,-3,-1,6,-3,-8,-1,-6,3,-10,-4,6,-5,7,2,10,-2,-6,3,3,-6,-4,-5,-3,2,9,4,-6,-6,7,-2,-5,9,9,5,1,3,10,6,6,7,-5,-5,-2,-3,10,-5,4,-6,7,7,5,-3,-7,6,-8,3,6,4,6,4,-7,-10,-2,-5,8,-6,1,-7,8,-2,-6,10,10,7,-3,5,-1,-10,1,-3,9,-3,-7,-7,-2,1,-5,-2,-5,4,-4,-10,1,-10,-7,-5,-2,-7,7,-6,-4,-10,10,-3,-3,-4,3,3,-6,-10,6,9,2,-9,-9,-9,-1,-1,1,5,10,-2,-5,-9,-8,4,-2,3,9,2,-4,1,8,-8,6,4,5,9,10,1,-6,-5,-7,2,-8,-6,-5,-10,10,1,-3,2,-2,-10,-10,2,3,4,-6,8,1,8,10,9,8,-4,7,-9,-10,1,9,5,3,-3,-6,-2,-2,2,-8,10,1,7,3,-6,6,-10,-3,6,-6,4,10,8,-6,-2,1,2,-9,1,6,2,7,6,10,-7,-3,-8,-6,-2,9,7,-9,4,-8,9,-6,-8,4,-2,-10,-9,-9,3,-3,8,-3,4,3,-10,-4,-7,-10,3,2,8,-6,2,-4,-1,-4,-1,-3,8,4,7,7,-8,2,2,-7,-4,7,-8,-5,-2,-9,5,-9,-8,-3,10,-10,8,10,-5,-10,1,9,8,10,2,-4,-1,-1,5,3,-5,-2,4,5,-10,-10,-2,-10,-10,4,-8,-10,1,-8,-7,-10,4,9,5,-7,1,-5,4,-7,4,8,-8,-2,2,-5,-9,-1,-8,-10,4,-9,-5,-8,-8,5,6,5,-4,5,7,4,5,-10,4,10,-7,3,-3,-3,7,2,-3,-9,6,-4,-6,-8,4,5,-7,-7,4,-6,-2,8,9,5,9,-3,-2,5,-7,-8,-2,-8,8,3,7,6,10,-1,6,-1,3,-7,10,10,8,6,-1,-8,4,-10,1,-2,-2,10,-10,10,-2,8,-10,9,8,-7,-4,7,-6,-8,-5,-10,3,4,10,7,-2,3,-5,1,10,2,2,-1,-6,-9,-9,-5,-8,6,-2,1,-9,-7,9,-8,5,2,-9,10,-1,-4,8,3,-10,-6,-1,6,3,6,1,-10,6,-6,6,10,-4,8,-6,10,7,8,-4,9,10,-9,1,-9,-3,10,2,-9,-4,10,7,6,9,3,10,1,7,-5,1,-3,-1,-8,-5,-1,1,1,-3], dtype = "uint32")#candidate|5943|(784,)|const|uint32
var_5944 = relay.var("var_5944", dtype = "int8", shape = (756,))#candidate|5944|(756,)|var|int8
var_5945 = relay.var("var_5945", dtype = "float64", shape = (192,))#candidate|5945|(192,)|var|float64
const_5946 = relay.const([-9.429887,-6.796900,-8.437753,-9.101932,8.008495,8.922194,0.853152,3.864955,-2.150395,4.890251,6.708738,2.594807,-7.186957,6.052744,-8.490991,3.966555,-9.021035,-1.396691,2.534981,-2.915620,-1.900293,2.879828,1.246438,-6.297329,-0.264463,1.287010,-4.790657,3.526076,-5.626897,-0.350477,-3.552751,2.608720,2.429071,-1.120450,0.581272,3.386167,-1.474052,0.879721,-0.359052,8.301305,5.227117,-0.630317,1.122601,-0.204550,-0.908446,-0.652617,-8.065736,4.418746,8.670611,-4.163121,2.055026,-8.549344,1.381983,5.097278,0.058127,-9.551612,1.641704,-3.725924,2.104840,-5.991651,4.036058,-9.286861,6.663455,-0.779891,8.268834,4.612633,-4.222303,-0.092053,3.665652,7.571592,-3.383355,3.532855,-2.120268,-7.167464,-1.465053,5.396436,8.129287,-7.730442,-7.196072,7.120511,9.785402,-7.297413,-9.545504,9.738372,-6.394732,-5.320869,0.136741,9.871713,8.576574,8.616196,-6.072326,-1.270499,-9.130960,-0.498896,1.810863,6.001536,-9.750390,-0.833253,-5.584047,-8.722314,0.718898,-8.054855,-1.233126,-8.041855,2.213045,-2.499233,7.759693,-9.259218,3.637773,-3.983029,-2.790858,6.898308,0.556715,-4.889632,-0.974351,-6.826239,6.682216,-3.315540,-5.060997,-1.044190,-2.605375,-5.327162,7.162458,6.902384,0.382604,9.979364,1.772811,1.355936,-6.432685,0.251871,-0.636838,-7.346315,-7.591171,-0.230541,-4.434530,-8.959314,4.027699,-6.310480,5.269164,0.847437,5.855918,5.009498,7.396080,5.691002,-2.275240,-8.147053,-1.571346,-6.426145,0.953446,-0.757620,7.614306,-3.712000,1.072278,9.384682,4.865910,9.896719,2.781184,2.827215,6.864006,8.686413,4.772490,0.039876,-7.882346,-8.483368,-9.137239,7.191944,-5.298859,-3.528939,-1.408916,-1.870024,-9.755678,-6.842490,-3.944248,-6.639849,-7.250340,4.306985,-9.864971,-6.460120,0.147367,-3.336359,6.354680,4.303836,-8.205114,2.107867,-1.239239,-5.918587,1.842324,-5.514875,-3.819839,-7.294153,-5.498206,9.174130,-0.061999,-7.615534,-6.083468,4.205913,-4.839812,5.640383,-0.708101,-1.772234,5.203315,9.350792,4.408332,-9.265506,-1.175786,8.627157,8.687205,8.603378,-3.737166,1.728017,3.266519,-6.890478,6.510426,-8.818399,-9.854015,-5.271568,5.577082,-0.032675,-7.778905,-5.502582,8.259535,2.374713,-5.509193,-0.739065,-4.554181,-0.416244,-9.851284,-7.076025,-1.548916,3.393422,4.014813,-9.885344,8.154794,7.457078,-0.177044,3.743574,7.409420,-5.190231,3.679034,-4.599698,-4.994041,9.108127,0.151047,-2.020778,-5.761720,-1.654281,-0.435824,-0.393559,-8.971446,4.017318,-2.126874,-9.692084], dtype = "float64")#candidate|5946|(252,)|const|float64
const_5947 = relay.const([2,10,-8,-6,-1,-4,2,9,-2,3,10,4,2,9,9,-10,9,-4,2,7,9,-2,5,-10,2,6,-3,-1,4,-5,-2,-5,6,-2,-1,4,2,-3,-1,6,6,-3,-2,-6,-6,3,-7,-3,-10,-3,-3,3,5,4,10,-7,-4,5,-9,-4,1,7,6,3,4,-8,-5,4,-8,-5,-2,5,7,2,1,2,-3,-4,-8,6,-4,-1,-5,10,7,2,-10,-5,-8,-4,3,5,-7,-7,-5,-9,9,-10,6,10,5,-3,2,5,-5,1,7,3,2,-10,-5,5,-8,-10,3,10,-3,-7,10,-5,1,2,1,-3,-5,7,10,4,5,4,4,-9,6,-4,-8,-3,6,-10,-9,7,3,-4,7,3,-1,-1,-1,-6,6,7,-8,6,6,-10,-6,10,2,-2,-3,-3,2,-1,-6,-3,-6,8,-1,-9,-10,-3,-5,-8,9,6,-7,-6,2,-3,4,-1,-6,-4,7,5,10,6,3,2,3,5,6,-10,-9,-9,9,-1,10,2,-9,-7,-7,6,-6,-3,8,-1,-7,5,2,-9,3,-7,-7,2,-8,-9,-1,-4,-5,6,-2,10,-7,-5,8,-1,-4,-5,9,-9,4,9,-2,2,9,3,-8,1,7,-6,10,5,8,-6,-7,2,-10,-9,-6,-2,-1,-6,-5,4,-5,-6,-10,8,10,4,9,-9,1,-3,-10,-3,7,2,8,-5,-8,5,-3,7,9,3,7,6,9,-6,2,2,9,-3,-9,8,-9,-7,-8,-8,-6,-4,2,-3,-1,1,-6,-5,6,10,6,7,10,2,8,6,10,9,4,-4,-8,-8,-8,9,-3,-1,6,-8,2,4,-9,-6,-2,10,6,9,-9,-8,4,-2,6,-7,3,-7,-7,-9,-3,5,1,-1,1,10,-9,-8,-6,1,6,-2,-5,-6,-2,-1,1,2,3,-8,3,4,-6,6,-3,-4,7,9,-7,-6,-1,5,3,5,-1,10,-1,-8,5,9,-3,8], dtype = "uint8")#candidate|5947|(378,)|const|uint8
call_5942 = relay.TupleGetItem(func_2765_call(relay.reshape(const_5943.astype('uint32'), [8, 7, 14]), relay.reshape(const_5943.astype('uint32'), [8, 7, 14]), relay.reshape(call_5929.astype('int32'), [60,]), relay.reshape(var_5944.astype('int8'), [9, 84]), relay.reshape(var_5945.astype('float64'), [24, 8]), relay.reshape(const_5946.astype('float64'), [1, 252]), relay.reshape(const_5947.astype('uint8'), [378,]), ), 3)
call_5948 = relay.TupleGetItem(func_2774_call(relay.reshape(const_5943.astype('uint32'), [8, 7, 14]), relay.reshape(const_5943.astype('uint32'), [8, 7, 14]), relay.reshape(call_5929.astype('int32'), [60,]), relay.reshape(var_5944.astype('int8'), [9, 84]), relay.reshape(var_5945.astype('float64'), [24, 8]), relay.reshape(const_5946.astype('float64'), [1, 252]), relay.reshape(const_5947.astype('uint8'), [378,]), ), 3)
func_4053_call = mod.get_global_var('func_4053')
func_4056_call = mutated_mod.get_global_var('func_4056')
const_5965 = relay.const([[-2.218191,1.594156,0.491989,-0.004668,8.442802,3.039040,-7.487995,-9.517969,-9.146450,-4.087554,-7.502966,-6.917591,-0.716135,-3.228880,2.241222,1.568566,1.401376,1.964670,-2.615877,8.323389,-8.573589,-5.422747,-6.819622,-3.754330,6.073462,-5.759029,-9.949308,-6.742130,-9.360583,3.819826,0.634550,7.847521,4.076110,8.392087,-6.425273,9.545447,9.924128,7.269134,-4.771438,-1.021701,-4.487832,8.416082,-8.026080,7.374626,6.635066,-2.963387,-2.576163,2.262825,0.049645,2.143273,1.715131,-7.393086,-7.579609,-4.547395,-9.061093,7.666350,2.896431,6.469512,-2.423444,-6.068832,7.373063,4.500613,2.554347,8.909618,6.584818,-3.599786,8.530840,-0.596210,8.291994,6.972889,6.925412,-7.442206,8.442007,-5.648972,9.237215,5.658070,-4.557671,-3.378784,-4.783011,-2.224210,-0.209290,-7.722226,8.551153,-6.489611],[-2.194058,-0.825779,-1.128563,-0.065131,-4.141021,6.192518,-3.514456,-2.399503,6.214340,-0.460360,-0.181498,-6.524730,3.601731,1.072498,7.815950,5.967160,0.238719,6.826106,8.166163,2.278746,5.952733,9.285412,-1.759033,-4.701303,-2.369854,5.471877,3.375537,1.911378,-6.614799,6.675647,-4.248129,9.077478,9.201251,6.074176,8.877427,-4.141500,-5.931409,-2.539479,-1.557511,-2.762478,8.781089,8.582599,9.078225,8.682257,1.058808,7.757371,-1.776653,8.025775,-0.453250,-2.347680,-0.794699,-8.653988,-3.025391,0.145326,9.038011,5.546699,2.493707,3.617055,3.531944,-1.247367,3.919562,7.259257,3.073753,1.496483,7.688809,2.937215,8.410537,-9.229182,-5.470315,-5.259807,-4.147724,-6.204597,-9.138613,-5.339287,-7.099723,6.613113,6.866207,4.218040,9.301217,-9.602221,-1.224988,-4.592260,5.338769,0.447662],[-8.868484,3.081204,4.586934,-3.229046,0.361825,-5.530964,-2.120442,3.812564,-5.920050,-8.892496,-6.812145,-0.933175,-0.498046,-5.450691,-6.625802,8.448245,4.536645,8.483254,-2.224090,-9.786984,-3.219765,9.489974,-5.883930,-2.879456,-5.701021,7.123578,7.973057,7.053180,-4.014115,4.752774,-9.363914,-2.681027,8.357349,-1.216375,6.778166,1.184531,6.541370,-1.560442,-3.998064,-2.286664,9.532162,3.672180,-3.070921,-5.654761,-6.987618,0.414426,-5.278683,-1.089714,0.426020,3.137818,5.221498,-8.282218,-9.044666,5.887665,-4.147105,4.126481,4.044991,-1.074678,7.351674,-9.672333,1.093398,-8.205164,4.285716,5.552418,-5.878174,-6.326507,-3.753614,-0.487683,5.180135,0.284261,-1.277847,-3.082847,0.012643,6.775286,3.353631,-6.020285,2.811042,1.782066,7.622921,3.974218,6.213478,4.344326,-3.996123,-9.006485],[2.576727,7.144063,-2.422577,9.028807,2.295133,1.032435,3.881097,3.699450,-8.043903,2.300083,4.530158,0.656251,-5.014985,-2.150551,5.813551,6.330094,-3.688779,-2.295066,-5.337736,-9.332766,-3.615801,-4.711910,4.689919,-3.240167,-4.978307,5.002853,-2.714297,7.532678,-5.304920,7.112483,-1.200263,-0.212895,-1.994391,-2.596556,7.613905,-3.368095,-0.276505,0.035062,-9.967262,0.812022,4.032193,-7.094523,-8.155562,4.110033,-7.953046,-4.300651,1.864143,2.482349,3.489428,-3.069958,9.846380,-9.928821,4.477985,3.505056,7.362574,0.407115,-8.388813,-9.670390,4.701406,1.788245,-9.727069,-4.365057,-6.907893,0.746592,1.769050,-7.720464,-9.018446,-8.121984,-9.309425,0.871009,7.796627,4.593444,6.161144,-2.237562,8.902323,-1.384615,1.869245,2.407135,-4.895858,3.358150,-1.113566,-5.500375,-6.422903,-5.547867],[9.998494,-3.644271,-0.105561,-9.992677,0.241250,-1.167115,-8.530505,-2.606872,-9.389989,7.249833,0.288774,-0.577133,8.684972,-7.202002,-2.398070,-6.422100,0.314452,-1.927426,-0.797689,4.986543,7.198536,-2.060578,-1.839935,2.817611,-5.732880,2.599161,3.319263,0.330475,3.872321,-0.019430,9.105785,9.225430,9.833319,-1.247978,-6.677831,0.899719,-6.122116,9.610164,-1.774238,1.492908,2.770237,-9.651825,-0.976053,5.281553,-7.092048,7.006354,9.953166,-8.796934,-2.184628,-9.154618,-8.818867,-2.414726,-9.969671,0.778019,-7.881761,1.295444,0.222832,-8.150295,-0.107289,4.444631,4.085612,-4.602056,3.901108,7.530890,3.317943,-7.599052,3.392372,-1.123002,-2.682439,2.793270,-8.811396,4.464538,-6.805249,-2.871975,3.489485,9.448246,-4.752293,0.691069,-1.853300,-5.068477,4.664923,5.481385,8.475768,-6.020256],[3.900875,3.490457,-8.791595,-4.148063,-2.720780,1.207994,-3.814214,3.961541,-4.301833,6.989532,4.368593,5.910778,-3.429903,-8.826866,-6.596474,-9.352676,-9.270233,-9.420532,-4.493545,3.007060,7.673527,-5.400544,-8.186961,-9.537180,3.745945,1.275697,5.257557,8.641887,-8.350504,-6.329482,-8.475673,-4.807647,-4.268059,9.655875,1.553289,0.660041,-2.232151,5.032428,7.031650,7.746741,3.449816,-8.906642,6.706976,-5.018817,6.372994,8.455355,0.176191,-8.601654,-2.172054,-0.727125,-0.115493,-2.303974,-0.374471,7.466188,3.591893,-8.996809,-7.664129,-5.257959,-9.648495,6.873163,2.178962,3.637029,-1.983368,-4.968845,3.934611,2.413933,-0.041440,-1.442649,0.351959,3.670281,4.285147,7.930007,-1.592987,5.150106,-2.040231,-0.862047,8.830355,4.768387,0.792489,-1.080072,-3.185619,-3.069768,1.071881,2.752824],[3.368753,-4.136189,-0.648578,-7.305857,0.557305,5.473157,-4.954813,3.359358,3.304030,4.941621,-7.077806,-4.590422,6.619547,5.908439,7.847699,8.404098,0.697537,5.645116,1.517054,-5.721348,-3.933916,7.005257,2.813589,-0.815476,6.617854,4.456562,-8.170922,-6.770777,9.503383,-2.948078,1.414062,7.710987,3.114449,-2.442189,-1.016875,6.171686,4.267175,8.515786,4.529610,6.252445,4.186871,-4.310674,-6.377655,-3.007770,3.391296,7.044058,-3.277115,8.746921,8.355411,2.706284,9.761765,-1.631690,3.270762,1.101740,-3.416717,5.250495,-6.564510,7.873787,-3.900832,-4.044272,-9.155903,-2.251201,-6.856497,0.627467,-6.566616,7.761234,6.683020,-9.751321,6.406510,-1.358308,-9.315826,5.557549,9.274149,-9.953771,-7.194073,3.879662,-5.894307,-7.830381,-8.932884,-3.940142,-2.300272,-1.298797,-5.770272,-1.703346],[-6.171489,9.822373,-3.483014,6.849524,4.056142,1.558779,-8.066947,-5.741736,4.906799,6.904249,-2.603219,-8.250460,8.862912,4.335964,6.239125,2.561169,-8.761781,-8.204932,-5.764570,-3.233486,0.665308,6.580166,8.352181,-4.503745,-6.811585,-3.293231,-3.196304,3.997462,7.330926,0.067576,-2.396865,-0.970508,0.605569,9.286935,9.888187,5.496016,-0.242211,-2.096775,-5.549386,-3.689629,5.407295,-5.277495,6.032054,3.266484,-6.163644,3.409148,-7.935515,2.224273,-8.950899,4.261775,-0.492652,0.109938,0.974988,-6.136022,-3.738731,7.093968,2.610082,6.841142,8.966420,3.971685,5.790629,3.331757,3.976098,0.490361,2.374549,7.090963,9.836560,-8.528554,-1.784212,0.840849,8.801887,-2.803277,-3.477780,0.010050,3.494394,6.410098,2.353508,-9.818362,3.908453,5.528036,-4.554425,-2.296197,3.290056,-3.504159]], dtype = "float64")#candidate|5965|(8, 84)|const|float64
call_5964 = func_4053_call(relay.reshape(const_5965.astype('float64'), [7, 16, 6]))
call_5966 = func_4053_call(relay.reshape(const_5965.astype('float64'), [7, 16, 6]))
const_5976 = relay.const([[[-8.086809,-5.908555,-9.878128,9.549728,9.737757,9.337761,6.529513,-6.069806],[2.062873,-0.690184,-4.703304,-4.588232,-0.839203,0.575849,-6.501985,6.229997],[-8.545607,-9.378632,9.443902,8.045268,-9.835362,-7.516144,6.704798,-0.894635],[-4.735361,1.456592,8.690765,8.252708,4.872311,3.058934,0.712073,2.851933]],[[-7.262672,-0.981364,1.524824,-9.006900,-0.224220,1.749093,-5.009425,-1.691510],[-5.663366,7.898123,1.492893,9.708474,8.196402,-8.301387,0.238498,2.833177],[-1.484016,-0.487126,3.830688,5.696689,4.323931,0.640554,9.821060,-4.024006],[-7.212234,5.279603,-2.191398,-7.605872,8.913453,-4.205109,-0.201409,5.768697]]], dtype = "float32")#candidate|5976|(2, 4, 8)|const|float32
bop_5977 = relay.power(var_5919.astype('float64'), relay.reshape(const_5976.astype('float64'), relay.shape_of(var_5919))) # shape=(2, 4, 8)
func_3057_call = mod.get_global_var('func_3057')
func_3059_call = mutated_mod.get_global_var('func_3059')
var_5999 = relay.var("var_5999", dtype = "float64", shape = (720,))#candidate|5999|(720,)|var|float64
call_5998 = relay.TupleGetItem(func_3057_call(relay.reshape(var_5999.astype('float64'), [15, 12, 4])), 0)
call_6000 = relay.TupleGetItem(func_3059_call(relay.reshape(var_5999.astype('float64'), [15, 12, 4])), 0)
func_1668_call = mod.get_global_var('func_1668')
func_1674_call = mutated_mod.get_global_var('func_1674')
var_6026 = relay.var("var_6026", dtype = "int8", shape = (1, 288))#candidate|6026|(1, 288)|var|int8
var_6027 = relay.var("var_6027", dtype = "bool", shape = (112,))#candidate|6027|(112,)|var|bool
call_6025 = relay.TupleGetItem(func_1668_call(relay.reshape(var_6026.astype('int8'), [6, 4, 12]), relay.reshape(var_6026.astype('int8'), [6, 4, 12]), relay.reshape(var_6027.astype('bool'), [1, 112]), relay.reshape(call_5929.astype('int32'), [60,]), ), 3)
call_6028 = relay.TupleGetItem(func_1674_call(relay.reshape(var_6026.astype('int8'), [6, 4, 12]), relay.reshape(var_6026.astype('int8'), [6, 4, 12]), relay.reshape(var_6027.astype('bool'), [1, 112]), relay.reshape(call_5929.astype('int32'), [60,]), ), 3)
func_1396_call = mod.get_global_var('func_1396')
func_1399_call = mutated_mod.get_global_var('func_1399')
call_6043 = relay.TupleGetItem(func_1396_call(relay.reshape(var_6027.astype('bool'), [16, 7, 1])), 0)
call_6044 = relay.TupleGetItem(func_1399_call(relay.reshape(var_6027.astype('bool'), [16, 7, 1])), 0)
bop_6047 = relay.minimum(const_5965.astype('uint64'), relay.reshape(call_5964.astype('uint64'), relay.shape_of(const_5965))) # shape=(8, 84)
bop_6050 = relay.minimum(const_5965.astype('uint64'), relay.reshape(call_5966.astype('uint64'), relay.shape_of(const_5965))) # shape=(8, 84)
uop_6055 = relay.sigmoid(uop_5920.astype('float64')) # shape=(2, 4, 8)
output = relay.Tuple([bop_5922,call_5929,var_5930,call_5942,const_5943,var_5944,var_5945,const_5946,const_5947,bop_5977,call_5998,var_5999,call_6025,var_6026,var_6027,call_6043,bop_6047,uop_6055,])
output2 = relay.Tuple([bop_5922,call_5931,var_5930,call_5948,const_5943,var_5944,var_5945,const_5946,const_5947,bop_5977,call_6000,var_5999,call_6028,var_6026,var_6027,call_6044,bop_6050,uop_6055,])
func_6060 = relay.Function([var_5919,var_5930,var_5944,var_5945,var_5999,var_6026,var_6027,], output)
mod['func_6060'] = func_6060
mod = relay.transform.InferType()(mod)
mutated_mod['func_6060'] = func_6060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6060_call = mutated_mod.get_global_var('func_6060')
var_6062 = relay.var("var_6062", dtype = "float32", shape = (2, 4, 8))#candidate|6062|(2, 4, 8)|var|float32
var_6063 = relay.var("var_6063", dtype = "int32", shape = (15, 4))#candidate|6063|(15, 4)|var|int32
var_6064 = relay.var("var_6064", dtype = "int8", shape = (756,))#candidate|6064|(756,)|var|int8
var_6065 = relay.var("var_6065", dtype = "float64", shape = (192,))#candidate|6065|(192,)|var|float64
var_6066 = relay.var("var_6066", dtype = "float64", shape = (720,))#candidate|6066|(720,)|var|float64
var_6067 = relay.var("var_6067", dtype = "int8", shape = (1, 288))#candidate|6067|(1, 288)|var|int8
var_6068 = relay.var("var_6068", dtype = "bool", shape = (112,))#candidate|6068|(112,)|var|bool
call_6061 = func_6060_call(var_6062,var_6063,var_6064,var_6065,var_6066,var_6067,var_6068,)
output = call_6061
func_6069 = relay.Function([var_6062,var_6063,var_6064,var_6065,var_6066,var_6067,var_6068,], output)
mutated_mod['func_6069'] = func_6069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5512_call = mod.get_global_var('func_5512')
func_5513_call = mutated_mod.get_global_var('func_5513')
call_6131 = func_5512_call()
call_6132 = func_5512_call()
output = relay.Tuple([call_6131,])
output2 = relay.Tuple([call_6132,])
func_6154 = relay.Function([], output)
mod['func_6154'] = func_6154
mod = relay.transform.InferType()(mod)
mutated_mod['func_6154'] = func_6154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6154_call = mutated_mod.get_global_var('func_6154')
call_6155 = func_6154_call()
output = call_6155
func_6156 = relay.Function([], output)
mutated_mod['func_6156'] = func_6156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5899_call = mod.get_global_var('func_5899')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_6198 = relay.TupleGetItem(func_5899_call(), 0)
call_6199 = relay.TupleGetItem(func_5901_call(), 0)
uop_6206 = relay.log10(call_6198.astype('float64')) # shape=(6, 12, 2)
uop_6208 = relay.log10(call_6199.astype('float64')) # shape=(6, 12, 2)
func_4826_call = mod.get_global_var('func_4826')
func_4830_call = mutated_mod.get_global_var('func_4830')
const_6212 = relay.const([9.587890,0.439091,-3.953476,-8.522179,-7.722825,9.423721,6.061661,9.201988,8.659203,1.817678,-4.614062,6.740626,-2.307607,-7.219844,-3.963777,-0.732042,-8.471201,0.258853,-5.711626,5.866417,-4.328619,9.478998,6.473547,3.361210,-7.158205,3.817400,-6.423443,-6.184056,8.111813,1.565710,-8.408055,4.645966,4.609841,6.601054,2.045216,-3.933773,-5.568524,2.585184,0.358421,-3.147106,5.117171,-9.041122,2.957212,3.840883,5.929997,-6.437456,-8.083652,-2.328692,-8.421105,1.721964,-7.295368,-0.867269,3.300268,7.802066,-7.860193,8.326664,8.473756,-0.997526,-8.581404,9.732424,-1.494534,-3.749710,-7.315105,-5.926577,-2.524657,-1.736387,-6.507323,1.987412,-1.695255,-2.253774,4.936838,-2.280111,3.998910,4.994771,-3.742072,7.105549,-5.071613,4.715519,-6.805530,-3.021130,1.788161,1.985873,8.766028,-7.887371,1.532231,-1.921183,-9.965173,-1.766870,1.041844,1.561724,-4.974872,-0.813261,-2.759966,8.563454,-5.402170,-2.593139,-7.897660,5.777281,-5.214469,4.568497,-9.872159,-3.809808,8.645285,-1.608763,-1.978289,-6.077762,-3.882160,-1.406753,9.559796,8.672820,1.178026,5.802113,5.894708,9.551589,-5.519008,-6.613562,-6.753734,7.986701,7.823957,5.953789,-8.065937,-9.216748,-5.443828,9.482490,3.397133,7.353008,-9.891403,-3.804700,8.429977,-9.955276,5.031040,-8.469230,3.383958,4.291231,6.153825,9.566217,-1.969417,-2.207358,-9.751202,-6.714766,-5.359092,-9.139170,3.902558,5.265708,-6.656977,-7.910280,-3.817005,8.097197,7.004469,-7.147358,3.236061,-7.456207,1.432012,0.894083,-5.419744,2.464939,2.168343,-9.361502,2.779657,-5.022043,0.077838,3.672030,7.456076,6.482679,3.781216,-7.616581,5.529230,-4.526605,9.373553,-0.287395,-7.794678,1.527519,9.967467,-1.592519,8.450772,-3.608835,1.485319,-9.909398,7.605121,7.385890,4.325691,0.361707,-8.761523,1.570470,3.889989,-0.696703,-3.957430,-9.084545,3.434320,-0.792656,9.880310,7.968359,-1.931258,2.265396,5.246173,-4.043165,-9.195540,-0.226055,6.844607,6.085651,4.717251,-6.861888,2.633815,-5.464678,4.003355,6.083772,3.901628,-7.434967,-4.649414,8.921277,-5.277021,-6.999470,-4.687267,-2.767874,-3.512802,-3.762446,2.492540,9.510974,7.639604,0.501283,-3.311522,0.721220,1.639703,6.078021,-0.136350,2.658202,-6.652266,0.007674,-0.131646,7.134866,7.052388,4.416764,-4.304971,2.354465,-7.488217,6.866015,7.414699,-5.512131,-2.847855,-0.775860,3.660882,5.286270,9.281829,-3.643134,-3.831984,7.978149,6.313437,-6.750501,5.989717,-3.440561,-6.447495,4.684279,-8.033513,-1.284148,3.122791,7.671700,7.583675,7.572480,-2.143247,-7.506683,9.776142,-5.265943,-5.830570,-9.070548,9.134205,3.798625,-3.556876,1.527377,7.834676,4.171555,6.014219,7.383309,-8.968766,6.968716,-2.344879,9.351833,8.181818,-9.738174,5.781930,-1.246649,8.895484,-6.869648,-7.693937,8.861862,-4.606487,-1.133959,3.673427,-4.691123,-7.099957,-8.792868,3.807016,-8.939349,-1.019008,4.350017,-2.973909,-4.644533,9.193534,0.787595,-0.482629,0.822728], dtype = "float32")#candidate|6212|(300,)|const|float32
var_6213 = relay.var("var_6213", dtype = "float64", shape = (192,))#candidate|6213|(192,)|var|float64
const_6214 = relay.const([-3,3,4,-6,1,-8,3,-1,6,4,5,-10,-3,-2,7,2,2,8,7,9,-8,-4,-10,-9,-1,4,-10,6,-7,8,-6,2,10,-4,-7,-5,-9,5,-4,-8,9,2,-6,-5,-9,-5,-5,-2,10,-10,-10,2,-5,-9,-3,-5,10,-4,-6,-9,1,-9,-4,9,-9,-1,-7,-8,-1,-1,-5,7,-6,4,-9,8,-7,-6,9,5,8,7,-10,-8,-4,-3,7,-6,10,-4,1,9,-8,10,-4,-5,2,8,9,-3,4,3,8,4,-7,7,8,-9,4,-6,-6,-1,-5,10,-4,8,-1,-1,8,8,-2,5,-2,-8,6,5,5,10,-6,5,-3,9,-3,4,-6,9,7,9,10,10,-1,8,2,7,8,7,4,7,8,1,6,-3,-7,4,2,-5,-8,1,1,-7,10,2,10,3,3,-2,-7,-1,9,-4,-1,6,-2,-9,-4,3,10,8,-5,8,9,6,-8,10,2,8,3,-3,10,-9,10,-6,7,10,9,7,-9,3,10,5,-9,5,9,-8,-2,3,1,10,-5,8,-10,3,-10,9,2,-3,-8,-3,-8,6,-10,-2,8,8,4,-9,-3,-6,-1,-4,-8,3,5,3,-1,-3,-7,1,-7,-1,5,5,-4,-10,5,-7,-10,7,10,-7,8,-1,5,10,-1,4,3,-3,-2,4,-8,8,-3,1,8,4,8,-3,-9,6,6,-5,9,7,-4,9,-2,-8,-4,2,-9,-8,-4,-1,-3,-3,4,9,-8,5,7,-4,10,6,2,-8,6,7,8,-3,4,-4,-3,-2,-9,-3,-2,5,-8,8,9,-1,3,-5,6,5,-1,8,10,-7,8,5,-8,2,1,5,7,7,4,2,-9,9,6,5,9,4,5,-5,-10,-8,8,-3,9,-4,1,4,5,-1,3,8,10,-9,-3,-6,3,4,-9,-4,-8,-3,6,-8,-1,3,-4,5,-3,9,-9,9,-10,3,1,-8,-6,7,-8,-7], dtype = "uint8")#candidate|6214|(378,)|const|uint8
call_6211 = relay.TupleGetItem(func_4826_call(relay.reshape(const_6212.astype('float32'), [15, 2, 10]), relay.reshape(var_6213.astype('float64'), [48, 4]), relay.reshape(const_6214.astype('uint8'), [126, 3]), ), 4)
call_6215 = relay.TupleGetItem(func_4830_call(relay.reshape(const_6212.astype('float32'), [15, 2, 10]), relay.reshape(var_6213.astype('float64'), [48, 4]), relay.reshape(const_6214.astype('uint8'), [126, 3]), ), 4)
output = relay.Tuple([uop_6206,call_6211,const_6212,var_6213,const_6214,])
output2 = relay.Tuple([uop_6208,call_6215,const_6212,var_6213,const_6214,])
func_6218 = relay.Function([var_6213,], output)
mod['func_6218'] = func_6218
mod = relay.transform.InferType()(mod)
var_6219 = relay.var("var_6219", dtype = "float64", shape = (192,))#candidate|6219|(192,)|var|float64
output = func_6218(var_6219)
func_6220 = relay.Function([var_6219], output)
mutated_mod['func_6220'] = func_6220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5648_call = mod.get_global_var('func_5648')
func_5649_call = mutated_mod.get_global_var('func_5649')
call_6228 = func_5648_call()
call_6229 = func_5648_call()
func_1144_call = mod.get_global_var('func_1144')
func_1147_call = mutated_mod.get_global_var('func_1147')
const_6232 = relay.const([-8.676391,1.339623,8.318568,-4.528534,9.183970,-9.523272,8.522509,-8.321624,-4.844795,5.297406,2.358760,-5.732299,-9.270217,5.417022,-8.442848,6.430475,5.890023,8.277020,-3.790293,-9.511262,-5.174483,9.784365,3.542391,-7.592820,7.888267,1.813420,-7.647691,-0.450604,-9.252263,-0.712995,-3.805982,3.642906,-4.642257,-1.205032,-3.559438,-3.574681,-8.381363,-3.264865,4.388469,6.283205,-7.795170,-6.978175,-3.103327,1.971155,-0.543304,3.175317,-7.796837,-0.664990,9.888280,5.555246,1.668445,-9.741070,5.328211,-9.410722,1.872329,6.471044,-9.051275,-4.777075,6.007371,0.623353,5.553555,-0.545569,4.757463,-0.593343,2.291656,-9.564479,-9.747748,-7.460391,0.365618,-1.834868,-3.763628,-5.918313,1.969338,5.984954,8.086961,-3.702548,3.198203,-4.641331,-8.251184,3.397640,-0.467772,-8.127939,7.915937,9.273506,8.278985,4.466171,7.312635,-5.431232,2.472529,0.282244,-6.030425,1.159625,-9.259301,-2.160517,8.517879,7.737014,5.990486,-6.075337,-8.768186,9.592507,1.338270,-1.946422,1.096722,-9.034665,-5.226475,8.814441,7.583376,7.968772,-8.077893,-2.357034,0.375686,2.101262,-9.753935,5.594109,9.644868,-5.532324,-5.144331,-0.625423,-0.043231,-3.884131,-9.421253,3.092096,-4.956821,-8.437003,9.202762,-7.506870,-3.558002,2.404352,7.359135,6.046286,-1.959775,-0.737415,-9.621853,-5.220568,7.327712,-2.169231,-9.239688,3.810645,-0.959734,8.910283,4.296137,-5.618774,4.398269,-0.228623,2.845395,-7.148293,7.045621,-0.988382,0.456554,-3.899975,9.712790,-1.451626,6.111178,-0.036862,2.183326,4.337132,-1.835371,-5.374685,3.564572,-0.392433,1.910230,-5.270125,1.631754,-9.845788,9.364275,9.904097,8.747665,-2.908641,-4.380820,-9.397500,-0.575078,-8.657497,-0.077717,8.599923,9.872406,-2.364337,-4.709421,5.948670,4.918751,-4.153174,8.654200,9.196952,9.939992,4.825740,-5.362082,-9.936243,0.628768,4.310136,9.710790,6.454359,7.517586,0.621047], dtype = "float64")#candidate|6232|(192,)|const|float64
call_6231 = func_1144_call(relay.reshape(const_6232.astype('float64'), [3, 4, 16]))
call_6233 = func_1144_call(relay.reshape(const_6232.astype('float64'), [3, 4, 16]))
func_6060_call = mod.get_global_var('func_6060')
func_6069_call = mutated_mod.get_global_var('func_6069')
const_6266 = relay.const([1.840694,7.727334,0.995572,0.319806,2.006227,1.694479,2.643380,5.481953,-4.305535,3.725041,0.730965,-7.503309,6.705917,-7.710306,-4.468175,2.334445,4.097753,-9.028711,9.840132,2.752502,4.861087,-6.368404,-5.049059,4.461890,-3.652230,6.989320,-2.068352,-1.719759,-9.539988,4.934553,-8.623120,-0.727318,3.535128,0.903410,-5.699867,0.691997,3.520421,1.569650,6.847445,5.354752,7.002057,8.768092,-0.835529,-9.569279,-6.882978,2.195756,-2.586999,8.191884,3.487102,-8.939880,7.711002,6.256635,5.555945,-4.247722,3.939211,-5.446492,-4.670329,-4.159663,3.116608,4.383896,-3.810894,4.550676,4.698173,-3.767764], dtype = "float32")#candidate|6266|(64,)|const|float32
const_6267 = relay.const([[-5],[1],[-5],[-6],[7],[9],[-5],[7],[-10],[3],[-1],[-8],[-6],[2],[8],[-5],[-1],[7],[-3],[2],[-8],[-10],[-5],[-6],[-6],[-4],[8],[1],[-2],[3],[-9],[5],[5],[7],[-4],[-7],[-9],[5],[8],[10],[4],[10],[8],[3],[-4],[-10],[-5],[6],[-6],[9],[1],[4],[7],[-5],[-3],[-8],[1],[-7],[9],[8]], dtype = "int32")#candidate|6267|(60, 1)|const|int32
var_6268 = relay.var("var_6268", dtype = "int8", shape = (756,))#candidate|6268|(756,)|var|int8
var_6269 = relay.var("var_6269", dtype = "float64", shape = (720,))#candidate|6269|(720,)|var|float64
var_6270 = relay.var("var_6270", dtype = "int8", shape = (24, 12))#candidate|6270|(24, 12)|var|int8
const_6271 = relay.const([[True],[False],[False],[True],[False],[False],[False],[True],[False],[True],[False],[False],[True],[False],[False],[False],[True],[False],[False],[True],[False],[False],[False],[True],[False],[True],[True],[False],[False],[False],[True],[True],[False],[False],[False],[False],[False],[False],[True],[True],[False],[True],[True],[True],[False],[True],[False],[True],[True],[False],[False],[True],[False],[False],[True],[False],[False],[False],[True],[False],[False],[False],[True],[True],[False],[True],[True],[True],[False],[True],[False],[False],[False],[True],[True],[False],[False],[True],[True],[True],[True],[True],[True],[False],[False],[False],[False],[False],[False],[True],[False],[False],[False],[True],[True],[False],[False],[True],[True],[False],[False],[True],[False],[False],[False],[False],[True],[False],[True],[False],[False],[True]], dtype = "bool")#candidate|6271|(112, 1)|const|bool
call_6265 = relay.TupleGetItem(func_6060_call(relay.reshape(const_6266.astype('float32'), [2, 4, 8]), relay.reshape(const_6267.astype('int32'), [15, 4]), relay.reshape(var_6268.astype('int8'), [756,]), relay.reshape(call_6231.astype('float64'), [192,]), relay.reshape(var_6269.astype('float64'), [720,]), relay.reshape(var_6270.astype('int8'), [1, 288]), relay.reshape(const_6271.astype('bool'), [112,]), ), 3)
call_6272 = relay.TupleGetItem(func_6069_call(relay.reshape(const_6266.astype('float32'), [2, 4, 8]), relay.reshape(const_6267.astype('int32'), [15, 4]), relay.reshape(var_6268.astype('int8'), [756,]), relay.reshape(call_6231.astype('float64'), [192,]), relay.reshape(var_6269.astype('float64'), [720,]), relay.reshape(var_6270.astype('int8'), [1, 288]), relay.reshape(const_6271.astype('bool'), [112,]), ), 3)
func_206_call = mod.get_global_var('func_206')
func_210_call = mutated_mod.get_global_var('func_210')
const_6276 = relay.const([-10,-4,10,10,5,3,2,-6,9,-4,7,9,-4,9,7,-9,-10,10,2,-9,-7,-8,-6,-4,4,-1,4,2,-3,4,-6,9,-3,-5,-8,-3,-9,-4,3,-10,-5,-9,-1,7,-1,-5,1,2,2,2,-4,-5,-3,-9,-6,-5,-10,-10,-7,-4,-9,5,5,-7,-7,-7,1,5,2,4,3,-8,6,-3,-6,-1,-7,6,-4,-7,9,1,7,-8,9,6,3,-4,-4,4,-3,-5,-3,-2,-4,-9,4,-7,-5,-1,-6,6,-3,-8,7,-6,-9,3,-2,9,6,8,-8,-5,9,7,5,5,-8,-4,7,7,1,-7,7,-8,4,6,-3,4,7,9,9,-1,-9,1,-4,-3,2,-7,-8,3,3,3,-10,-7,-10,-10,-10,-5,-7,6,-9,-8,1,-2,-2,-10,-6,-8,9,3,2,8,6,1,-2,-5,-6,-1,-8,-3,-8,5,5,10,1,-3,7,-4,-7,-6,-2,7,2,4,-1,-2,1,2,-3,1,-6,-6,10,-7,7,-3,2,8,9,8,10,-8,-7,10,-3,-1,-7,-3,9,3,1,6,7,-9,-5,-4,-7,9,-5,2,-9,-8,-4,-5,-2,8,4,9,7,8,5,6,-6,-5,-3,10,4,2,10,-10,8,6,-3,5,-4,-1,-7,-10,1,4,4,9,4,5,-9,-6,2,-8,8,-4,-6,-1,1,6,9,-9,-5,-3,8,-3,-3,-3,-3,-2,6,-5,-3,7,-10,-10,-6,5,5,-10,-6,-1,4,-5,-7,-9,-5,9,-3,-3,-1,5,2,-9,-8,2,-4,4,-1,6,-8,-2,1,2,-10,-8,-8,10,-1,-8,10,4,7,1,-6,5,-3,-6,10,8,-3,-1,-7,4,2,8,4,-3,7,8,-2,-9,9,9,3,9,4,-10,5,-9,-6,6,-9,10,4,1,-8,-2,6,-8,9,-9,-1,1,5,-2,9,10,6,3,-5,-9,5,-3,1,3,3,10,-3,2,3,6], dtype = "uint8")#candidate|6276|(378,)|const|uint8
call_6275 = relay.TupleGetItem(func_206_call(relay.reshape(const_6276.astype('uint8'), [3, 9, 14]), relay.reshape(call_6265.astype('int32'), [3, 2, 10]), ), 3)
call_6277 = relay.TupleGetItem(func_210_call(relay.reshape(const_6276.astype('uint8'), [3, 9, 14]), relay.reshape(call_6265.astype('int32'), [3, 2, 10]), ), 3)
func_5648_call = mod.get_global_var('func_5648')
func_5649_call = mutated_mod.get_global_var('func_5649')
call_6285 = func_5648_call()
call_6286 = func_5648_call()
func_2095_call = mod.get_global_var('func_2095')
func_2098_call = mutated_mod.get_global_var('func_2098')
const_6294 = relay.const([-0.318123,-8.032368,7.127247,-3.369801,-3.644281,-3.378082,-7.297226,3.297280,6.562454,6.302290,6.011440,-6.300140,3.967147,-8.231574,-5.624691,2.534173,1.793253,-6.231620,0.887089,5.810660,8.191978,-5.981031,-8.000360,4.674127,0.818162,-0.304445,-5.176983,-7.050421,1.333009,-2.280956,-2.889882,-3.204179,3.579032,-5.224553,9.768222,-0.958762,3.457999,-9.751545,8.489456,-4.889011,-4.863169,6.195749,9.560757,1.537385,8.031710,-7.116139,9.580300,7.566257,2.331348,-9.668142,0.464190,9.013766,2.074018,-8.329755,-9.317882,7.804806,-3.613117,9.840914,-2.801556,-4.866678,-5.499218,4.441411,3.578856,7.408270,-5.342507,8.571146,-0.785446,8.318989,9.395989,-5.452881,-5.144461,-3.655544,8.869160,-2.769417,-4.736099,9.088375,7.180236,0.937366,6.651471,9.681127,-2.552341,7.399266,-2.241647,-8.315533,-9.883684,5.589353,8.832447,3.139482,6.844318,-3.317720,-1.991206,-3.827355,3.871985,-0.708216,-6.563341,-5.402942,1.420625,-3.379782,-1.366585,4.082414,8.087004,0.017288,-4.958813,5.517164,-6.473649,-6.488042,0.083795,-1.901296,-7.186656,5.766512,7.126475,5.028642,6.662116,-3.126582,-0.125702,9.227237,-5.318446,-6.756425,6.614904,-2.059679,-0.997875,8.863990,6.140116,-7.095217,-7.510927,4.637600,7.377689,-4.070756,-4.360062,7.492613,-4.497784,-7.295796,6.236019,-5.483739,3.631735,2.396711,3.889401,0.128561,-6.898131,-5.518540,-8.243733,-4.703740,-4.144501,-8.591990,6.068548,8.945196,-8.503503,-1.728145,0.253035,2.677799,7.555609,-1.277959,2.695525,-1.144245,8.778754,-0.167499,-0.855457,9.363218,-1.769232,5.274294,3.549136,3.731455,-4.967189,-2.858116,-4.108009,-5.112011,-0.192345,-8.890370,9.829243,4.338081,7.617611,-1.233881,0.332030,-4.834516,0.235522,8.439337,1.295982,7.637916,7.263312,8.047500,8.687833,1.384193,-3.822333,1.964056,-0.343276,-2.718410,-6.248635,4.054873,-3.838470,1.860077,8.581738,0.058375,-9.809028,6.879541,-7.498113,7.074102,-0.739472,2.107612,4.401364,-0.847897,5.554077,0.159375,2.971125,5.847811,6.188551,-1.977797,-4.430139,0.820693,-3.307120,-3.030439,8.405009,-2.016597,-5.967171,-3.945511,-5.443199,-1.514640,9.047095,9.216096,-8.486923,-1.049148,-2.626941,4.660843,-7.041128,4.528750,6.815396,3.431968,9.639015,-4.581016,9.778895,3.054693,-6.550973,-7.329615,-7.026589,-6.431753,-0.600592,-5.167584,0.192215,6.880207,-9.446966,-1.428866,-6.470460,-8.252187,4.542200,-3.856173,8.393478,-7.506083,0.081287,6.425854,5.049493,-8.279842,-4.319833,-6.238029], dtype = "float64")#candidate|6294|(252,)|const|float64
call_6293 = relay.TupleGetItem(func_2095_call(relay.reshape(const_6294.astype('float64'), [9, 4, 7]), relay.reshape(var_6268.astype('int8'), [756,]), ), 1)
call_6295 = relay.TupleGetItem(func_2098_call(relay.reshape(const_6294.astype('float64'), [9, 4, 7]), relay.reshape(var_6268.astype('int8'), [756,]), ), 1)
output = relay.Tuple([call_6228,call_6231,const_6232,call_6265,const_6266,const_6267,var_6268,var_6269,var_6270,const_6271,call_6275,const_6276,call_6285,call_6293,const_6294,])
output2 = relay.Tuple([call_6229,call_6233,const_6232,call_6272,const_6266,const_6267,var_6268,var_6269,var_6270,const_6271,call_6277,const_6276,call_6286,call_6295,const_6294,])
func_6303 = relay.Function([var_6268,var_6269,var_6270,], output)
mod['func_6303'] = func_6303
mod = relay.transform.InferType()(mod)
var_6304 = relay.var("var_6304", dtype = "int8", shape = (756,))#candidate|6304|(756,)|var|int8
var_6305 = relay.var("var_6305", dtype = "float64", shape = (720,))#candidate|6305|(720,)|var|float64
var_6306 = relay.var("var_6306", dtype = "int8", shape = (24, 12))#candidate|6306|(24, 12)|var|int8
output = func_6303(var_6304,var_6305,var_6306,)
func_6307 = relay.Function([var_6304,var_6305,var_6306,], output)
mutated_mod['func_6307'] = func_6307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5659_call = mod.get_global_var('func_5659')
func_5660_call = mutated_mod.get_global_var('func_5660')
call_6328 = relay.TupleGetItem(func_5659_call(), 0)
call_6329 = relay.TupleGetItem(func_5660_call(), 0)
func_10_call = mod.get_global_var('func_10')
func_13_call = mutated_mod.get_global_var('func_13')
const_6333 = relay.const([-6,-10,10,-10,-1,3,3,-4,3,-10,1,4,-1,-3,-6,-10,-9,-9,-6,-3,7,-6,-3,-3,10,-7,-1,6,6,10,-2,-6,-1,-1,3,-5,9,3,6,8,-9,4,10,3,1,-9,8,-3,10,7,7,6,-7,-10,4,6,5,-7,-10,-2], dtype = "int32")#candidate|6333|(60,)|const|int32
call_6332 = func_10_call(relay.reshape(const_6333.astype('int32'), [3, 2, 10]), relay.reshape(const_6333.astype('int32'), [3, 2, 10]), )
call_6334 = func_10_call(relay.reshape(const_6333.astype('int32'), [3, 2, 10]), relay.reshape(const_6333.astype('int32'), [3, 2, 10]), )
func_6303_call = mod.get_global_var('func_6303')
func_6307_call = mutated_mod.get_global_var('func_6307')
var_6366 = relay.var("var_6366", dtype = "int8", shape = (756,))#candidate|6366|(756,)|var|int8
const_6367 = relay.const([0.861955,-5.652337,4.097850,2.867461,6.994759,-5.064072,-4.729518,3.569635,-6.952810,3.776122,-5.033631,-4.428421,2.445117,-8.352096,-1.583002,-1.202060,-5.218242,6.852395,-8.278384,-3.214166,-6.760038,-0.214974,-0.881166,-2.674186,2.127344,-9.234112,0.448909,-9.064748,-7.320656,2.668279,6.265879,-3.027135,-5.932242,2.807155,0.468666,-6.133467,7.923133,-4.794722,7.453917,-0.775657,2.436464,-6.781053,6.013858,7.985100,-3.099139,-2.325894,-9.451719,0.133195,9.108418,-1.135262,-9.665448,-7.943298,3.300201,5.058360,1.235708,5.655722,9.808652,5.158612,0.434404,-2.380134,9.045503,6.443555,6.484650,-3.179558,-8.631013,0.405976,-4.604071,-0.618577,3.842277,-4.820809,5.592152,8.476476,4.514865,7.980935,4.154875,-3.004979,-4.939916,-5.834297,-0.058893,-7.004917,2.403574,-9.678235,-3.121309,-3.991107,-0.183058,-1.354369,-8.983725,-6.765508,5.007838,-7.343439,6.340044,8.116154,2.516721,-8.427458,9.870115,-2.517183,-3.475577,-8.166329,9.817399,-0.815982,7.519186,7.933871,-7.759538,1.538539,6.176376,-3.638683,0.623180,-6.958874,-6.227774,-9.603192,-1.081077,-2.843466,0.368380,0.242679,2.238448,9.678574,-5.227335,7.771980,-9.367020,-4.273279,-8.184019,7.054674,7.185602,-2.078758,-8.355664,0.715805,5.108599,6.291663,-0.565568,1.697084,4.889939,-3.720700,7.340385,-6.032168,-5.345765,4.695300,-3.684362,-3.190546,8.505459,5.207557,-7.940846,-9.389846,-5.167897,-3.884016,-9.816727,7.270007,-2.993881,2.808912,2.570560,-5.395418,0.008145,-5.027083,-0.543172,8.060601,-2.017301,3.469397,3.658062,-4.050348,8.517134,-2.919691,4.693495,8.458838,5.018579,6.796839,4.840385,-3.858830,-1.723370,-3.281783,-9.191190,-5.431404,-9.054462,4.508010,4.334000,3.897972,-4.847393,-6.564177,0.012480,-6.023672,-0.208225,6.064237,4.449839,-2.898769,4.231066,-6.777256,-2.143907,-9.784750,-0.313323,-8.245080,8.211006,-2.670130,1.370437,5.107389,7.923109,9.668901,-1.128421,5.624118,9.252697,4.673830,-2.415947,-7.034196,-4.188752,4.879362,-2.165223,-3.944803,2.550500,9.928253,7.526755,-8.841760,-9.917729,-9.731975,-0.933923,-5.068523,-9.524849,-7.363651,0.039849,7.836871,5.677531,-7.424163,0.728044,-4.884488,-9.385648,0.221581,-1.294666,-0.946151,-0.170730,4.763040,-0.249467,-7.138671,2.389876,5.045623,4.469250,-8.836058,8.145083,-2.411220,6.757953,2.876166,-9.532356,4.468578,-8.743951,-6.231485,0.819625,-6.638672,5.610175,-5.817700,1.062076,-5.913097,-6.836750,-9.098883,9.361736,-6.895925,5.220232,-5.838622,3.142531,-1.459773,4.640003,-0.594534,9.539569,-7.441386,1.053434,2.130194,-4.207549,5.703475,1.077666,-3.235910,-9.678592,2.630734,2.006244,9.066895,-5.213967,-5.824660,-9.461184,-7.777959,9.862843,3.480075,6.981473,-3.710627,-6.529684,-1.013884,0.802990,-6.441669,-4.270538,5.332082,-8.123172,-0.113452,-8.205738,-2.009630,1.726326,-4.540406,-3.571541,4.704115,2.492794,0.034287,5.574384,4.809690,0.195042,-3.110487,1.326494,0.284502,-8.895675,-5.059494,-3.523289,-3.017158,2.623822,2.079363,-5.494221,6.957590,-9.507773,2.475552,5.306276,-1.220538,-5.420245,-3.302489,-1.922940,0.696748,0.883107,3.095236,3.173642,2.074295,0.122191,-7.702666,6.134187,6.381223,-5.116790,7.136276,6.172206,-0.014767,-7.484011,2.030556,-1.839576,2.288043,7.891438,-7.059726,-8.800540,8.130432,-7.565460,6.411752,-1.592086,9.233936,5.867206,-0.720891,-6.502527,0.401257,0.376476,4.752619,8.542478,0.579216,9.291077,7.440684,1.907569,6.210176,-4.365805,7.144179,9.263962,-1.173423,4.520474,2.115508,8.735023,-4.809445,-5.486684,0.519935,-5.165598,-0.049399,-3.316217,-7.359092,-7.220725,6.232233,-0.190025,1.553919,2.723244,6.954221,-7.473736,-6.840648,9.070695,-3.833456,-9.297360,3.043695,-3.963974,-3.056888,-1.307674,-8.794200,0.337716,6.885206,-6.898739,9.845817,-4.927583,-6.123782,-3.873255,4.445281,8.299239,7.603626,4.270868,4.907581,-5.466422,-1.532499,-4.591620,8.415262,-6.635918,4.721800,-3.878416,-5.786592,5.949789,2.958411,8.438879,8.233190,0.772687,-1.923390,-8.821422,-7.735765,6.070065,1.170913,-3.439512,0.333654,1.106407,4.839216,-6.344129,2.426760,4.014016,4.865381,4.875981,3.643463,5.540029,2.789964,3.955694,-2.911260,-6.737335,-4.387858,-0.368284,8.662999,5.768169,3.552940,-9.769930,8.919801,-8.608453,-3.059476,-2.946722,-6.736758,1.346312,8.346095,8.799772,5.049128,0.044836,-7.479825,-7.602702,2.550549,0.441408,4.463032,3.021306,6.132904,3.648532,6.978465,9.895739,9.029845,8.757777,-9.005222,-1.762113,-2.416675,1.185609,5.309557,-1.784525,5.242659,-2.321396,0.066688,-3.560493,2.958235,-7.965798,6.752632,-7.183643,-9.632885,3.620081,-7.203835,8.104729,4.257529,-0.463774,-1.264846,8.965538,-2.353749,-2.163738,-4.074692,-7.306166,-4.490034,-6.412745,-0.698905,-4.285774,8.267256,1.584961,7.871684,-6.250694,-0.869563,2.137979,-8.152030,-3.148045,-5.975164,-0.190517,8.065536,-3.828987,-2.296914,5.732960,4.677310,2.713567,5.875502,9.242105,8.096580,2.253503,-6.620938,-7.085834,-7.563643,5.319529,5.923982,6.757433,-9.914419,-9.343271,-5.943679,6.603421,0.998723,-7.691576,-3.347811,9.299418,-7.797287,7.647578,-6.229480,5.971720,-9.849464,5.494149,-9.175841,5.655656,9.320655,4.479202,0.731088,2.444315,-9.601084,-3.447021,4.154289,-7.708543,-4.143734,-3.464903,-3.303245,4.444926,-8.042578,-6.260996,3.975888,1.990618,-0.979146,2.082923,-8.550878,-2.298171,-0.107002,4.922649,9.264371,8.549541,2.599675,-2.672070,7.366527,-0.634858,-2.252044,1.731905,-3.406081,-4.694329,9.165921,9.689780,6.574784,-2.807840,-4.787933,4.438244,-0.180484,5.281156,5.396175,0.627398,-0.822984,-5.636982,-4.689148,-4.388961,7.464925,8.644390,-1.007878,-8.446361,4.894716,-4.791496,-3.308076,9.588301,-6.030620,-9.842089,-1.931541,4.968045,3.811285,3.803387,7.983170,7.656073,9.100132,6.495566,6.633718,1.463145,5.677223,-9.888260,9.065429,-1.006325,-0.634764,0.112321,-2.233157,6.392200,0.460508,4.776177,6.159095,4.972326,-7.835348,-1.713680,-9.683182,-5.393553,4.526868,8.450881,-3.995708,7.447008,-7.163811,3.442838,5.355450,-3.907555,3.761393,2.805546,-6.455824,1.838264,2.427910,-7.594399,6.904214,3.037589,9.880205,-4.615562,-1.054343,3.134403,-8.538995,6.800708,7.687955,-4.240662,-1.790397,5.925114,-9.414551,0.350381,2.149147,0.616010,-5.336803,0.826534,9.587696,4.698897,6.665903,-5.062376,3.727828,0.410745,-6.342136,3.657347,1.917218,4.647598,-6.676813,-9.112720,4.392794,-4.308208,-3.320420,3.159355,1.482065,-5.062427,8.506826,5.101716,-6.207452,-6.818781,-9.073133,9.285621,-4.534896,-7.776464,4.953074,-3.887276,-8.778237,-4.466486,6.344722,2.610900,-4.410620,9.474840,-1.325724,-6.740724,-0.908853,2.276482,4.320139,-6.688000,-7.440071,-1.875709,6.717469,-6.850937,4.166398,5.932384,-0.529892,-4.099701,-9.607970,4.783823,-7.132607,1.810028,-5.096770,3.758581,-2.092214,0.845192,-8.307535,-7.712832,7.279760,-9.999051,-0.300842,4.925320,-4.086451,6.461638,9.483568,8.274033,6.225909,-3.779823,-2.296660,0.271770,-2.031694,8.796176,-6.114539,-0.979275,-0.806569,-6.651668,-6.728128,0.457662,9.852266,3.148457,9.744366], dtype = "float64")#candidate|6367|(720,)|const|float64
var_6368 = relay.var("var_6368", dtype = "int8", shape = (72, 4))#candidate|6368|(72, 4)|var|int8
call_6365 = relay.TupleGetItem(func_6303_call(relay.reshape(var_6366.astype('int8'), [756,]), relay.reshape(const_6367.astype('float64'), [720,]), relay.reshape(var_6368.astype('int8'), [24, 12]), ), 8)
call_6369 = relay.TupleGetItem(func_6307_call(relay.reshape(var_6366.astype('int8'), [756,]), relay.reshape(const_6367.astype('float64'), [720,]), relay.reshape(var_6368.astype('int8'), [24, 12]), ), 8)
func_5512_call = mod.get_global_var('func_5512')
func_5513_call = mutated_mod.get_global_var('func_5513')
call_6370 = func_5512_call()
call_6371 = func_5512_call()
func_5392_call = mod.get_global_var('func_5392')
func_5399_call = mutated_mod.get_global_var('func_5399')
const_6391 = relay.const([False,False,False,False,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True,False,False,True,False,False,False,True,False,True,False,False,False,False,False,False,False,False,True,True,True,False,True,True,False,True,True,True,True,False,True,True,False,True,False,False,True,False,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,True,False,True,False,True,True,False,False,True,False,False,True,False,True,True,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,False,True,False,False,False,True,False,False,False,True,True,False,True,False,True,False,False,True,True,True,True,False,False,True,False,False,True,True,False,False,False,False,True,False,False,True,True,True,False,False,False,True,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,False,True,True,True,True,True,True,False,False,True,True,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,False,False,False,True,False,True,True,True,True,False,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False,True,False,False,False,True,False,True,True,False,False,True,False,True,True,True,True,False,False,False,False,False,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,False,False,True,True,True,True,False,False,False,False,False,False,False,False,False,True,True,True,False,False,False,True,False,False,False,True,False,True,False,True,False,True,True,True,False,False,True,False,True,True,False,True,False,False,False,False,True,True,False,False,False,False,True,False,False,True,True,False,False], dtype = "bool")#candidate|6391|(315,)|const|bool
var_6392 = relay.var("var_6392", dtype = "bool", shape = (112,))#candidate|6392|(112,)|var|bool
const_6393 = relay.const([-3.134012,3.989433,7.296691,6.833495,-6.469212,-4.977710,0.052290,-7.799145,-1.666927,2.168021,7.968292,-9.593356,7.075207,-6.059338,8.663298,8.758894,-4.884715,5.378833,5.280508,8.136780,0.665256,5.763231,-8.740364,-7.407574,2.673393,-4.236502,-1.483998,-2.995518,-9.459489,-6.308933,-3.016345,-3.526068,5.686853,5.460787,-9.909357,-8.035308,-6.753017,-2.162513,6.248482,3.954870,-5.270496,4.067652,-8.336154,3.452907,1.561130,3.431993,5.861770,-4.157188,7.736373,-5.709838,3.182568,-5.965756,-6.724946,-5.352033,8.575192,8.980819,-5.743042,-0.819756,-5.883168,8.465821,-5.811741,-4.836104,-5.646339,-2.357730,-3.941440,-1.490746,8.469370,5.897354,1.721492,7.630554,-0.292115,5.214770,-7.093197,0.814021,5.782065,-5.959592,6.646156,7.693312,2.191270,-1.795121,-2.152488,0.821430,8.020023,-6.655150,7.365022,7.568446,-1.221247,-7.302215,4.965533,7.886877,-1.603479,-4.416314,-7.013210,-2.650894,2.783813,9.261128,1.191739,0.845504,-2.678901,4.621216,5.841506,5.926668,7.522132,-3.974667,9.273194,1.730832,1.916821,-0.988180,-9.135481,-7.471108,8.729148,7.812347,-9.488472,1.130105,-5.626354,-3.684370,5.029529,3.035574,1.132354,1.773899,-2.508775,9.426389,-9.969591,7.583679,-8.525587,-1.821430,-7.529646,-1.652410,-0.217368,2.788871,-9.675641,0.031628,1.735510,4.082263,-2.276885,0.573227,4.623364,3.220504,-1.127372,-7.050550,-1.887619,-6.152219,0.927028,2.131687,-7.747375,-0.646656,4.953814,4.308987,2.223356,5.510877,9.906772,-5.993638,3.992352,4.161244,-0.529786,-4.813577,-1.974161,3.418862,5.395994,-6.751079,0.900036,6.014166,-1.739779,2.977425,5.787912,4.841306,-2.335226,8.486823,8.352533,8.353552,1.101283,-2.431880,6.934474,4.635174,5.349296,-7.810823,-8.324095,6.937028,-8.145123,-8.539295,6.789453,3.247393,0.308670,-6.446597,5.231606,1.034160,2.772692,-1.447484,8.744766,-9.590517,0.112968,-3.902448,-1.400880,-4.336773,-4.673956,-2.865828,3.410539,7.340971,-5.264204,5.043688,-6.535344,-3.702949,9.672609,-4.266898,-3.171621,5.977437,8.515894,-4.331331,4.726499,0.921775,5.374241,4.204741,6.348608,-0.334726,-6.359883,9.705000,-8.391836,8.955483,-2.622767,-2.272709,-5.668158,3.307887,1.941039,6.588001,-4.808793,5.957107,-9.801194,-7.218925,5.581722,5.989063,2.391947,-4.074796,2.869425,0.718519,9.058821,-8.758412,0.828284,-1.974994,2.509042,8.095891,-3.454968,-2.157587,6.249112,-4.132593,3.033112,8.246579,-9.511695,-9.567687,2.820324,5.473268,2.099705,-8.441535], dtype = "float64")#candidate|6393|(252,)|const|float64
const_6394 = relay.const([[-5],[-9],[8],[-4],[-5],[6],[4],[-7],[-10],[1],[10],[10],[3],[-4],[9],[9],[8],[5],[-5],[-8],[-2],[2],[-2],[-3],[4],[4],[-5],[8],[8],[-10],[-7],[-5],[8],[-2],[-10],[5],[-7],[-6],[-10],[3],[4],[-7],[-2],[6],[6],[-10],[-6],[1],[4],[-8],[6],[-4],[2],[1],[-2],[5],[-4],[6],[9],[7],[-9],[-10],[2],[8],[-5],[-2],[-2],[3],[8],[-6],[-10],[8],[-3],[-9],[8],[10],[3],[-2],[-1],[4],[-9],[-8],[-3],[-4],[7],[-3],[1],[9],[8],[8],[6],[-5],[8],[-5],[-10],[-9],[-3],[9],[-10],[-7],[1],[1],[1],[-7],[10],[7],[3],[-4],[-1],[-2],[-9],[-9],[9],[-8],[-9],[3],[-7],[1],[8],[9],[3],[-3],[-7],[-7],[-7],[-9],[-9],[-1],[-6],[-5],[-6],[-6],[-7],[-2],[-5],[3],[6],[4],[5],[4],[-10],[10],[-3],[10],[-10],[6],[-5],[10],[9],[7],[3],[-4],[5],[6],[9],[2],[5],[1],[-3],[-9],[7],[-2],[6],[-6],[-5],[9],[-2],[9],[-10],[9],[-5],[1],[5],[7],[-6],[-2],[2],[5],[5],[2],[-4],[-8],[-3],[6],[-1],[5],[6],[-5],[-1],[-10],[1],[-9],[-7],[10],[6],[1],[-3],[8],[7],[-1],[9],[-6],[5],[7],[-8],[-2],[8],[-3],[-6],[6],[-4],[-1],[8],[-5],[1],[5],[4],[-4],[-5],[-5],[-7],[-1],[10],[1],[-6],[5],[-8],[1],[4],[-2],[3],[-7],[-1],[8],[-4],[-8],[-3],[10],[-4],[7],[-10],[3],[9],[-3],[-9],[-7],[2],[-3],[-7],[-8],[5],[-1],[-6],[10],[-2],[1],[-9],[9],[8],[10],[6],[-2],[-3],[1],[4],[-10],[7],[7],[-2],[3],[-6],[-7],[9],[-5],[-7],[4],[2],[2],[-9],[-7],[4],[3],[-9],[-7],[1],[-5],[4],[-4],[-8],[-2],[1],[8],[2],[-3],[5],[-5],[5],[2],[-10],[3],[7],[-10],[1],[-8],[10],[6],[5],[-7],[4],[-5],[9],[-7],[10],[6],[-6],[-3],[10],[8],[7],[2],[5],[9],[2],[7],[7],[6],[-4],[8],[-2],[-5],[-7],[5],[-4],[-9],[-10],[-6],[-1],[-5],[2],[-10],[5],[-7],[-8],[-2],[1],[-1],[8],[6],[-9],[-10],[-9],[4],[-3],[2],[2],[-6],[-5],[6],[8],[-4],[-7],[-9],[-10],[-8],[-1],[-8],[7],[10],[-10],[5],[4],[8],[6],[5],[-4],[-5],[5],[-8]], dtype = "uint8")#candidate|6394|(378, 1)|const|uint8
call_6390 = relay.TupleGetItem(func_5392_call(relay.reshape(const_6391.astype('bool'), [7, 9, 5]), relay.reshape(const_6391.astype('bool'), [7, 9, 5]), relay.reshape(var_6392.astype('bool'), [56, 2]), relay.reshape(const_6393.astype('float64'), [252,]), relay.reshape(const_6394.astype('uint8'), [378,]), ), 4)
call_6395 = relay.TupleGetItem(func_5399_call(relay.reshape(const_6391.astype('bool'), [7, 9, 5]), relay.reshape(const_6391.astype('bool'), [7, 9, 5]), relay.reshape(var_6392.astype('bool'), [56, 2]), relay.reshape(const_6393.astype('float64'), [252,]), relay.reshape(const_6394.astype('uint8'), [378,]), ), 4)
output = relay.Tuple([call_6328,call_6332,const_6333,call_6365,var_6366,const_6367,var_6368,call_6370,call_6390,const_6391,var_6392,const_6393,const_6394,])
output2 = relay.Tuple([call_6329,call_6334,const_6333,call_6369,var_6366,const_6367,var_6368,call_6371,call_6395,const_6391,var_6392,const_6393,const_6394,])
func_6396 = relay.Function([var_6366,var_6368,var_6392,], output)
mod['func_6396'] = func_6396
mod = relay.transform.InferType()(mod)
mutated_mod['func_6396'] = func_6396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6396_call = mutated_mod.get_global_var('func_6396')
var_6398 = relay.var("var_6398", dtype = "int8", shape = (756,))#candidate|6398|(756,)|var|int8
var_6399 = relay.var("var_6399", dtype = "int8", shape = (72, 4))#candidate|6399|(72, 4)|var|int8
var_6400 = relay.var("var_6400", dtype = "bool", shape = (112,))#candidate|6400|(112,)|var|bool
call_6397 = func_6396_call(var_6398,var_6399,var_6400,)
output = call_6397
func_6401 = relay.Function([var_6398,var_6399,var_6400,], output)
mutated_mod['func_6401'] = func_6401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5899_call = mod.get_global_var('func_5899')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_6450 = relay.TupleGetItem(func_5899_call(), 0)
call_6451 = relay.TupleGetItem(func_5901_call(), 0)
uop_6455 = relay.erf(call_6450.astype('float32')) # shape=(6, 12, 2)
uop_6457 = relay.erf(call_6451.astype('float32')) # shape=(6, 12, 2)
func_5512_call = mod.get_global_var('func_5512')
func_5513_call = mutated_mod.get_global_var('func_5513')
call_6478 = func_5512_call()
call_6479 = func_5512_call()
output = relay.Tuple([uop_6455,call_6478,])
output2 = relay.Tuple([uop_6457,call_6479,])
func_6480 = relay.Function([], output)
mod['func_6480'] = func_6480
mod = relay.transform.InferType()(mod)
mutated_mod['func_6480'] = func_6480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6480_call = mutated_mod.get_global_var('func_6480')
call_6481 = func_6480_call()
output = call_6481
func_6482 = relay.Function([], output)
mutated_mod['func_6482'] = func_6482
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6483 = relay.var("var_6483", dtype = "float32", shape = (5, 12, 6))#candidate|6483|(5, 12, 6)|var|float32
const_6484 = relay.const([[[-1.439825,-1.912776,5.875401,-4.315823,-5.582098,6.953644],[9.780832,-5.052762,7.128184,-1.484481,9.172767,-5.775341],[9.982461,3.895234,3.368688,5.192173,8.102133,-2.894050],[9.384822,1.543435,9.840255,-2.912517,2.679893,9.620145],[2.404737,-7.245289,6.893213,5.122455,5.659249,0.272573],[0.429987,-8.563494,5.035456,6.093639,2.316104,-3.631324],[0.145119,-3.501171,5.503109,-5.871791,8.347948,4.981506],[2.816563,5.752290,0.883793,7.173041,1.416538,7.364907],[-9.801754,4.475302,1.913172,-1.429479,2.002555,5.664964],[2.940513,8.592518,-8.974405,4.765322,4.648168,2.682370],[-8.964750,-5.153533,-7.190821,-2.062159,-6.330351,9.933921],[2.688356,5.857275,-2.044356,-3.674451,-4.780506,-3.155114]],[[-7.038790,-6.628357,0.890988,8.459075,-0.250543,0.676223],[4.262251,3.828371,-3.485968,-9.510696,0.141614,-3.852612],[-7.303405,6.410631,-5.407166,-7.573466,9.451874,5.789100],[-8.371903,-9.042502,-7.819038,7.095046,7.491478,2.326496],[3.371154,-9.087915,3.095654,-3.960322,7.474175,-8.656788],[-0.685449,-9.936897,7.151565,-9.653635,-7.283466,-0.318085],[-3.404796,5.741933,1.730876,4.736992,-8.860323,0.229820],[-6.605718,2.065723,6.797003,-4.501435,-8.023436,1.818135],[-5.178422,3.824198,7.670879,2.261466,-6.117725,6.494136],[3.364561,-3.874324,-6.124076,-7.931512,-2.144841,-7.971880],[9.911960,0.265244,-3.639819,-7.586090,-8.378333,1.924408],[2.771200,6.625229,6.949541,5.217706,-6.856764,-7.078246]],[[9.216917,2.577914,3.367058,3.825007,-5.697687,-6.032755],[-7.635826,3.745532,0.331182,-9.369551,6.245023,-3.339173],[-7.009363,-4.478786,9.789859,-9.218312,2.478626,-1.033442],[8.504797,5.354342,-7.770508,-0.909095,-7.986982,8.054515],[8.518363,0.303597,-5.346449,0.896241,8.172833,9.488119],[7.125187,-1.601802,3.920177,6.730829,-3.167209,8.846084],[-2.866497,6.439675,1.229682,-4.836078,-3.233178,-3.185526],[2.364447,-3.021419,9.269435,-4.873753,1.422279,5.502143],[4.845538,3.623869,8.846343,1.468954,1.115304,7.138279],[5.840124,3.833468,8.671326,-2.113192,4.974277,4.529113],[-2.293719,3.166279,-5.982388,3.121958,8.539307,-6.282685],[6.813588,7.446874,-1.905572,7.546462,-0.548498,-2.761016]],[[-9.642188,5.079767,4.490557,-3.152201,-7.052352,7.458569],[-4.854178,-3.065843,1.850149,9.175283,-7.413952,9.007060],[9.587838,6.434828,2.047301,2.262934,-3.302483,-4.591213],[2.469034,-2.782068,-7.976470,8.502249,-2.791788,4.615222],[-6.611584,-0.501010,6.813541,5.379330,-1.477243,-6.305199],[-3.637006,-8.531725,-2.205364,-3.808098,5.445250,2.991495],[-3.904546,2.956390,2.437838,6.732675,3.405996,-3.471378],[7.450656,8.074785,-6.025254,-5.787321,0.743796,-0.138214],[2.949652,9.617470,1.053679,-2.140052,1.364307,-9.491367],[-4.977425,-1.234611,8.381589,-6.704229,4.677545,-7.233582],[-3.010804,-5.549441,5.619896,2.608832,-7.083960,-1.914770],[-8.200409,7.300868,-2.397893,-4.384903,7.853995,-4.053063]],[[2.102344,-9.578114,-7.232395,5.839408,7.838856,-5.046858],[-3.419775,3.992446,-2.534079,-8.740815,-1.260773,6.118831],[0.220826,-1.186858,-1.650682,2.779119,4.141599,-2.615060],[-9.508562,-6.888844,-8.694458,3.850814,4.156801,0.588966],[-7.284340,-5.907438,1.570094,9.986578,8.280681,-5.364709],[-1.551654,1.652168,6.231027,2.234953,8.289708,7.062635],[-7.300285,-5.310067,4.648819,4.788036,0.814814,-5.757065],[5.393655,7.162593,1.154686,4.197148,3.397207,-5.914122],[-8.199545,6.428925,8.019316,5.801363,3.680875,4.171709],[7.701800,-2.329962,-8.024517,-5.817010,-8.411699,-2.510749],[2.960501,4.067878,9.742701,1.421004,7.138592,3.015375],[8.505608,-3.326895,2.218880,5.886384,-9.076130,7.789554]]], dtype = "float32")#candidate|6484|(5, 12, 6)|const|float32
bop_6485 = relay.mod(var_6483.astype('float32'), relay.reshape(const_6484.astype('float32'), relay.shape_of(var_6483))) # shape=(5, 12, 6)
func_1356_call = mod.get_global_var('func_1356')
func_1360_call = mutated_mod.get_global_var('func_1360')
var_6493 = relay.var("var_6493", dtype = "int8", shape = (352, 4))#candidate|6493|(352, 4)|var|int8
call_6492 = relay.TupleGetItem(func_1356_call(relay.reshape(var_6493.astype('int8'), [11, 8, 16]), relay.reshape(var_6493.astype('int8'), [11, 8, 16]), ), 1)
call_6494 = relay.TupleGetItem(func_1360_call(relay.reshape(var_6493.astype('int8'), [11, 8, 16]), relay.reshape(var_6493.astype('int8'), [11, 8, 16]), ), 1)
output = relay.Tuple([bop_6485,call_6492,var_6493,])
output2 = relay.Tuple([bop_6485,call_6494,var_6493,])
func_6498 = relay.Function([var_6483,var_6493,], output)
mod['func_6498'] = func_6498
mod = relay.transform.InferType()(mod)
mutated_mod['func_6498'] = func_6498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6498_call = mutated_mod.get_global_var('func_6498')
var_6500 = relay.var("var_6500", dtype = "float32", shape = (5, 12, 6))#candidate|6500|(5, 12, 6)|var|float32
var_6501 = relay.var("var_6501", dtype = "int8", shape = (352, 4))#candidate|6501|(352, 4)|var|int8
call_6499 = func_6498_call(var_6500,var_6501,)
output = call_6499
func_6502 = relay.Function([var_6500,var_6501,], output)
mutated_mod['func_6502'] = func_6502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5512_call = mod.get_global_var('func_5512')
func_5513_call = mutated_mod.get_global_var('func_5513')
call_6522 = func_5512_call()
call_6523 = func_5512_call()
output = relay.Tuple([call_6522,])
output2 = relay.Tuple([call_6523,])
func_6529 = relay.Function([], output)
mod['func_6529'] = func_6529
mod = relay.transform.InferType()(mod)
mutated_mod['func_6529'] = func_6529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6529_call = mutated_mod.get_global_var('func_6529')
call_6530 = func_6529_call()
output = call_6530
func_6531 = relay.Function([], output)
mutated_mod['func_6531'] = func_6531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5659_call = mod.get_global_var('func_5659')
func_5660_call = mutated_mod.get_global_var('func_5660')
call_6532 = relay.TupleGetItem(func_5659_call(), 0)
call_6533 = relay.TupleGetItem(func_5660_call(), 0)
func_5648_call = mod.get_global_var('func_5648')
func_5649_call = mutated_mod.get_global_var('func_5649')
call_6541 = func_5648_call()
call_6542 = func_5648_call()
output = relay.Tuple([call_6532,call_6541,])
output2 = relay.Tuple([call_6533,call_6542,])
func_6551 = relay.Function([], output)
mod['func_6551'] = func_6551
mod = relay.transform.InferType()(mod)
output = func_6551()
func_6552 = relay.Function([], output)
mutated_mod['func_6552'] = func_6552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6480_call = mod.get_global_var('func_6480')
func_6482_call = mutated_mod.get_global_var('func_6482')
call_6613 = relay.TupleGetItem(func_6480_call(), 0)
call_6614 = relay.TupleGetItem(func_6482_call(), 0)
func_1396_call = mod.get_global_var('func_1396')
func_1399_call = mutated_mod.get_global_var('func_1399')
const_6624 = relay.const([True,True,True,False,False,True,False,False,True,False,True,False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,True,False,False,True,True,True,True,False,True,True,True,False,True,False,False,False,True,False,False,True,False,False,False,False,False,False,False,True,False,True,True,True,True,False,True,False,True,False,False,True,True,False,True,False,False,True,True,True,True,True,False,True,True,True,False,False,True,False,True,False,True,True,True,False,True,False,True,False,False,True,True,True,True,False,False,False,True,True,True,False,False,False,False,True,True,False], dtype = "bool")#candidate|6624|(112,)|const|bool
call_6623 = relay.TupleGetItem(func_1396_call(relay.reshape(const_6624.astype('bool'), [16, 7, 1])), 0)
call_6625 = relay.TupleGetItem(func_1399_call(relay.reshape(const_6624.astype('bool'), [16, 7, 1])), 0)
output = relay.Tuple([call_6613,call_6623,const_6624,])
output2 = relay.Tuple([call_6614,call_6625,const_6624,])
func_6644 = relay.Function([], output)
mod['func_6644'] = func_6644
mod = relay.transform.InferType()(mod)
output = func_6644()
func_6645 = relay.Function([], output)
mutated_mod['func_6645'] = func_6645
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6697 = relay.var("var_6697", dtype = "float32", shape = (12, 1, 5))#candidate|6697|(12, 1, 5)|var|float32
var_6698 = relay.var("var_6698", dtype = "float32", shape = (12, 7, 5))#candidate|6698|(12, 7, 5)|var|float32
bop_6699 = relay.floor_mod(var_6697.astype('float32'), var_6698.astype('float32')) # shape=(12, 7, 5)
output = bop_6699
output2 = bop_6699
func_6706 = relay.Function([var_6697,var_6698,], output)
mod['func_6706'] = func_6706
mod = relay.transform.InferType()(mod)
var_6707 = relay.var("var_6707", dtype = "float32", shape = (12, 1, 5))#candidate|6707|(12, 1, 5)|var|float32
var_6708 = relay.var("var_6708", dtype = "float32", shape = (12, 7, 5))#candidate|6708|(12, 7, 5)|var|float32
output = func_6706(var_6707,var_6708,)
func_6709 = relay.Function([var_6707,var_6708,], output)
mutated_mod['func_6709'] = func_6709
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6738 = relay.var("var_6738", dtype = "float64", shape = (14, 15, 1))#candidate|6738|(14, 15, 1)|var|float64
uop_6739 = relay.sin(var_6738.astype('float64')) # shape=(14, 15, 1)
func_2765_call = mod.get_global_var('func_2765')
func_2774_call = mutated_mod.get_global_var('func_2774')
const_6751 = relay.const([[-5,8,-10,-5,1,9,-2,-9,3,4,3,7,6,1,3,-7,-8,10,-9,-5,3,-10,-6,1,-2,-3,-9,-3,8,-10,-1,1,-1,-5,6,-3,-6,3,9,9,-9,10,-3,-4,7,3,-2,-7,-5,-3,4,9,6,10,-8,-1,-3,6,4,-10,3,-10,8,-7,-10,4,-6,-4,9,-10,-4,5,-3,-5,10,-1,9,-9,9,-1,-8,-4,2,-9,-1,7,1,5,4,3,5,8,-5,4,6,-4,-2,9,6,4,-6,-3,2,2,-7,-1,-1,8,-7,10,10,8,-2,-6,4,6,-1,-8,4,-1,7,5,1,3,-8,1,-9,-9,-3,-9,-5,6,3,-8,-6,-10,-1,10,-10,1,-8,-7,-1,-9,-3,3,7,-3,5,-9,-2,-3,-6,6,8,8,-10,-4,-1,-5,-5,-2,8,-3,9,-4,-1,-8,10,6,1,-3,-7,2,-3,-4,-7,-9,4,-10,3,5,-10,4,-7,9,2,-9,-10,1,-9,-2,-1,-1,-2,-7,-4,-1,-5,4,3,10,-7,8,-1,1,-4,-6,3,-10,-6,-1,1,-5,-7,8,4,7,8,-9,4,1,-4,-3,-2,-3,9,-1,8,-7,-4,-4,5,-10,-1,-6,-10,3,3,2,-10,-6,-10,9,10,2,-3,4,2,-4,2,7,6,7,-7,-7,-5,8,-9,-5,5,4,-8,7,-2,-10,-1,-10,9,8,-8,5,-7,3,9,4,-7,-3,7,-2,3,7,1,2,-5,-7,7,-8,-4,8,-9,9,-3,1,-2,-2,7,10,-5,7,5,2,-8,6,-1,7,-9,6,-9,-3,-9,8,2,-3,10,-6,-6,7,-9,5,-7,10,7,9,2,-8,9,-5,2,10,8,9,6,-7,8,7,-4,-3,-4,8,-6,-4,-10,6,7,-8,-3,10,-2,6,-8,-7,-1,-5,7,-10,-8,8,5,4,1,8,6,3,6,-9,-2,9,1,8,-7,-10,5,5,-1,2,10,8,-10,5,10,-2,-4,-8,5,2,-8,-7,8,1,-2,5,-4,9,2,2,9,8,5,8,-6,1,1,-5,1,-2,10,6,-8,2,8,6,7,3,-2,1,-1,9,2,5,-1,-8,-4,-9,-7,4,4,-7,4,3,2,3,6,-7,8,-4,1,-2,-4,7,1,-1,3,-5,7,-4,-2,2,9,-8,3,5,-4,1,9,1,1,-8,9,3,1,-5,-4,-1,-8,9,-1,-7,5,-2,6,-6,-7,-3,-8,-2,-4,2,-2,1,1,3,-6,6,-6,6,4,-9,8,7,8,7,-4,8,-3,8,-10,-8,1,8,2,9,9,7,10,5,1,10,2,-5,-8,9,-4,-6,10,-2,1,-10,-1,-10,-9,9,-9,-7,-8,6,-5,-5,3,-6,7,-9,1,-7,-4,-3,3,3,4,5,-2,9,-9,10,6,-6,6,-1,5,-9,-6,10,-6,-3,4,-2,8,-8,6,10,-4,6,4,-4,5,5,-6,1,1,2,-2,6,4,9,-1,-3,-7,-2,-6,7,-2,3,1,-9,9,-10,4,1,7,9,10,3,-10,-8,3,-8,-10,-2,8,-3,-3,-8,-8,-8,-10,3,6,7,2,4,1,-10,-4,3,-6,-9,-9,9,-9,-2,-1,-10,2,-6,-3,10,10,-6,-2,8,-5,-10,-5,2,3,2,-9,-4,-10,-5,-9,-8,3,-5,2,7,-10,10,4,-9,5,5,-4,5,9,8,5,7,9,-4,-7,6,8,3,9,-2,-3,-8,-6,-2,3,1,5,7,-3,-5,-4,8,-9,7,-4,2,-6,6,-5,4,-10,7,6,9,5,-10,5,2,-2,3,5,-5,6,-2,-2,9,5,7,-10,-3,-10,-3,-4,10,1,1,-7,-9,-10,5,1,-5,-10,10,-9,-4,-7,-6,9,6,-7,9,5,-8,1,8,7,-2,6,-8,6,-5,-8,-5,-7,8,8,-6,5,8,7,-2,1,-1,6,3,-9,7,1,6,-3,-2,4,-5,-3,-7,-1,3,2,9,3,-2,-4,2,10,-3,-2,3,-2,5,1,6,-2,2,-2,4,4,-10]], dtype = "uint32")#candidate|6751|(1, 784)|const|uint32
const_6752 = relay.const([[-9,5,6,7],[6,5,-7,-9],[-9,5,-5,9],[-4,10,8,-9],[4,8,4,8],[-1,-1,-4,-7],[3,-4,-10,10],[9,-9,-5,-6],[6,9,-1,-2],[-1,-3,3,-6],[4,7,-3,8],[-8,-1,-7,3],[10,3,-10,8],[-10,-6,2,1],[4,-10,6,8]], dtype = "int32")#candidate|6752|(15, 4)|const|int32
var_6753 = relay.var("var_6753", dtype = "int8", shape = (9, 84))#candidate|6753|(9, 84)|var|int8
const_6754 = relay.const([3.169379,5.876489,5.500252,7.070888,7.006538,9.449897,0.512312,1.907596,-7.211021,5.313467,-6.725766,9.088296,-2.784550,1.540832,-9.553683,6.746525,-8.701671,2.768457,-8.949898,-1.385863,-2.448776,4.456034,-1.771542,-4.961036,-4.243353,-3.534850,6.215118,-1.025480,-9.448469,9.623273,-6.646803,-8.358130,2.981864,-1.733981,-0.321722,-0.285999,-7.079593,-0.471772,-2.148292,8.335209,-4.499993,6.427417,6.922202,-8.013871,2.726942,5.426733,-0.729516,-5.436605,9.220600,4.397178,-3.753436,-1.333443,8.525219,5.242826,1.337543,-2.359888,-1.290241,2.125780,3.467881,2.610688,-3.979197,9.066763,-1.257733,-0.482603,-5.679054,-9.797199,7.425678,-6.198241,8.866783,-2.806595,-0.222927,2.284078,-6.252567,3.414414,-2.284989,1.629256,9.583238,1.562672,-4.638828,7.695335,1.285916,3.063079,-5.028036,8.712561,9.098656,-5.567309,-8.282608,3.314408,-3.602801,6.949624,0.216823,0.282185,4.161675,1.371652,3.045628,-4.315932,-7.816877,2.205226,5.739506,-1.998300,7.027021,0.700055,-1.349803,-4.549779,2.983747,4.366715,-4.569157,9.574424,6.707434,-1.343887,7.526613,4.300187,-3.310277,-3.232476,7.341699,9.263436,7.345705,0.003222,5.037748,-5.585632,9.513810,6.098063,8.353530,5.366850,2.332465,1.056446,-6.246825,-7.567744,1.515753,7.083520,-5.064367,1.350378,1.340904,2.305925,3.851380,8.320525,-9.629813,-9.980873,7.749574,-2.079135,2.892480,3.808867,1.660308,1.853109,-1.806334,0.199284,1.827710,-8.522143,0.205077,4.767546,3.053932,4.310594,8.314826,7.765666,2.156722,-1.320497,4.430434,0.998088,3.268309,-1.356692,4.000935,-0.748983,-9.277874,8.309243,8.061102,-2.525940,9.708306,-0.312497,-9.707345,5.984180,9.307606,-6.610205,1.255172,6.689302,-3.928860,-7.607100,-9.116797,-7.232457,9.106191,-4.241529,-2.934182,3.787004,2.518822,9.082130,-1.687685,0.341819,-4.846039,-9.676702,6.509258,-4.553132,1.703786,0.228502], dtype = "float64")#candidate|6754|(192,)|const|float64
var_6755 = relay.var("var_6755", dtype = "float64", shape = (252,))#candidate|6755|(252,)|var|float64
const_6756 = relay.const([4,9,5,5,-8,6,-4,10,-5,-7,-3,1,-8,6,-10,6,-9,2,-10,4,7,-7,5,7,4,-10,-3,-1,-5,-10,5,7,-2,8,5,2,-1,3,8,-3,-7,7,6,-10,6,6,-7,-5,-3,1,-4,1,1,9,-5,-2,-7,-4,-9,-4,6,6,4,-4,-4,-6,-9,-4,-3,10,7,-2,-2,-7,-5,-6,2,6,-3,4,7,-8,7,7,-4,9,10,8,-10,-3,-6,7,8,6,4,-9,-8,-7,8,6,-2,5,-8,4,-8,4,5,-3,-3,-4,-7,-9,-1,-3,-10,-3,5,6,1,-1,8,-4,-7,6,6,-8,-5,9,5,7,10,-10,9,8,10,10,7,1,-3,-3,-10,-3,9,-3,3,-10,9,9,7,-10,9,5,6,-9,6,9,2,-1,3,5,-3,2,-4,9,-8,-10,-9,-2,-2,3,2,4,-1,5,8,-1,-5,-10,-3,4,-8,-10,-9,1,3,9,-3,1,7,-9,8,-5,-4,-3,6,10,-10,-10,-3,10,4,-5,-4,2,-2,6,2,2,6,2,-1,-5,-5,1,7,-7,-3,-9,-7,-10,-1,-1,-8,8,-6,-8,-7,1,-10,-9,6,-2,-8,-5,4,-6,-2,10,7,7,-10,-4,8,8,-10,6,3,-2,-9,-6,2,7,-8,-5,-5,-10,-7,-4,2,4,-9,5,-8,-2,5,1,-1,-3,-7,4,3,9,-10,3,-6,-3,7,8,-6,6,10,1,6,-10,4,-7,10,7,10,2,-6,1,-3,-1,-9,2,-4,3,-9,-5,9,-2,-7,-10,8,2,-7,9,2,-10,-9,-2,-7,5,2,-1,-1,1,-1,-6,5,4,1,-3,-5,3,7,-7,4,10,-3,6,-3,3,-10,-4,-8,-8,-2,-1,-5,-3,2,9,-3,2,2,-1,7,-1,-4,1,-5,-3,1,6,-10,10,-8,-8,10,6,-7,8,-10,2,-4,-7,3,6,4,10,10,6,1,-8,5,2], dtype = "uint8")#candidate|6756|(378,)|const|uint8
call_6750 = relay.TupleGetItem(func_2765_call(relay.reshape(const_6751.astype('uint32'), [8, 7, 14]), relay.reshape(const_6751.astype('uint32'), [8, 7, 14]), relay.reshape(const_6752.astype('int32'), [60,]), relay.reshape(var_6753.astype('int8'), [9, 84]), relay.reshape(const_6754.astype('float64'), [24, 8]), relay.reshape(var_6755.astype('float64'), [1, 252]), relay.reshape(const_6756.astype('uint8'), [378,]), ), 6)
call_6757 = relay.TupleGetItem(func_2774_call(relay.reshape(const_6751.astype('uint32'), [8, 7, 14]), relay.reshape(const_6751.astype('uint32'), [8, 7, 14]), relay.reshape(const_6752.astype('int32'), [60,]), relay.reshape(var_6753.astype('int8'), [9, 84]), relay.reshape(const_6754.astype('float64'), [24, 8]), relay.reshape(var_6755.astype('float64'), [1, 252]), relay.reshape(const_6756.astype('uint8'), [378,]), ), 6)
func_5659_call = mod.get_global_var('func_5659')
func_5660_call = mutated_mod.get_global_var('func_5660')
call_6762 = relay.TupleGetItem(func_5659_call(), 0)
call_6763 = relay.TupleGetItem(func_5660_call(), 0)
output = relay.Tuple([uop_6739,call_6750,const_6751,const_6752,var_6753,const_6754,var_6755,const_6756,call_6762,])
output2 = relay.Tuple([uop_6739,call_6757,const_6751,const_6752,var_6753,const_6754,var_6755,const_6756,call_6763,])
func_6765 = relay.Function([var_6738,var_6753,var_6755,], output)
mod['func_6765'] = func_6765
mod = relay.transform.InferType()(mod)
mutated_mod['func_6765'] = func_6765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6765_call = mutated_mod.get_global_var('func_6765')
var_6767 = relay.var("var_6767", dtype = "float64", shape = (14, 15, 1))#candidate|6767|(14, 15, 1)|var|float64
var_6768 = relay.var("var_6768", dtype = "int8", shape = (9, 84))#candidate|6768|(9, 84)|var|int8
var_6769 = relay.var("var_6769", dtype = "float64", shape = (252,))#candidate|6769|(252,)|var|float64
call_6766 = func_6765_call(var_6767,var_6768,var_6769,)
output = call_6766
func_6770 = relay.Function([var_6767,var_6768,var_6769,], output)
mutated_mod['func_6770'] = func_6770
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6794 = relay.const([[[True,True,False,False,True,False,False,False,False,True,False,False,True],[False,False,False,True,True,True,False,False,True,False,False,False,True],[True,False,True,True,False,True,True,True,True,False,True,False,True]],[[False,True,True,False,True,False,False,True,True,True,False,True,True],[False,False,False,False,True,True,True,True,True,True,False,False,False],[True,False,False,True,True,False,True,True,False,False,True,False,True]],[[False,True,True,False,False,True,False,False,False,True,False,True,False],[True,False,False,True,True,False,True,True,True,True,True,False,False],[True,False,True,True,True,True,False,True,True,False,False,True,True]],[[False,True,True,True,True,False,False,False,True,True,False,False,False],[True,True,True,False,True,False,False,False,True,False,False,True,True],[True,True,True,True,False,False,False,True,True,True,True,True,True]],[[False,False,True,True,False,True,False,True,True,False,True,True,False],[False,True,False,True,False,False,True,False,True,True,False,True,True],[True,False,False,True,False,True,True,True,False,False,False,False,True]],[[True,False,True,True,True,True,False,True,True,True,True,False,True],[False,True,True,True,False,False,False,True,True,False,False,True,True],[False,True,False,False,False,True,True,True,False,False,True,True,True]],[[False,False,True,False,True,True,True,False,True,False,False,True,True],[False,True,True,True,False,True,False,False,True,False,False,False,False],[False,False,True,True,False,True,True,True,True,False,False,False,False]],[[True,False,True,False,True,True,True,False,False,False,True,False,False],[True,False,False,True,False,True,False,True,False,False,False,False,True],[True,False,True,False,True,True,False,False,True,False,True,True,False]],[[True,True,False,True,True,True,True,False,False,False,True,False,True],[True,False,False,True,True,True,False,True,True,True,False,False,True],[True,False,False,False,False,True,True,False,False,True,True,True,True]]], dtype = "bool")#candidate|6794|(9, 3, 13)|const|bool
var_6795 = relay.var("var_6795", dtype = "bool", shape = (9, 3, 13))#candidate|6795|(9, 3, 13)|var|bool
bop_6796 = relay.logical_or(const_6794.astype('bool'), relay.reshape(var_6795.astype('bool'), relay.shape_of(const_6794))) # shape=(9, 3, 13)
func_1789_call = mod.get_global_var('func_1789')
func_1792_call = mutated_mod.get_global_var('func_1792')
var_6806 = relay.var("var_6806", dtype = "int8", shape = (756,))#candidate|6806|(756,)|var|int8
call_6805 = relay.TupleGetItem(func_1789_call(relay.reshape(var_6806.astype('int8'), [7, 12, 9]), relay.reshape(var_6806.astype('int8'), [7, 12, 9]), ), 1)
call_6807 = relay.TupleGetItem(func_1792_call(relay.reshape(var_6806.astype('int8'), [7, 12, 9]), relay.reshape(var_6806.astype('int8'), [7, 12, 9]), ), 1)
output = relay.Tuple([bop_6796,call_6805,var_6806,])
output2 = relay.Tuple([bop_6796,call_6807,var_6806,])
func_6808 = relay.Function([var_6795,var_6806,], output)
mod['func_6808'] = func_6808
mod = relay.transform.InferType()(mod)
var_6809 = relay.var("var_6809", dtype = "bool", shape = (9, 3, 13))#candidate|6809|(9, 3, 13)|var|bool
var_6810 = relay.var("var_6810", dtype = "int8", shape = (756,))#candidate|6810|(756,)|var|int8
output = func_6808(var_6809,var_6810,)
func_6811 = relay.Function([var_6809,var_6810,], output)
mutated_mod['func_6811'] = func_6811
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6480_call = mod.get_global_var('func_6480')
func_6482_call = mutated_mod.get_global_var('func_6482')
call_6901 = relay.TupleGetItem(func_6480_call(), 1)
call_6902 = relay.TupleGetItem(func_6482_call(), 1)
output = relay.Tuple([call_6901,])
output2 = relay.Tuple([call_6902,])
func_6910 = relay.Function([], output)
mod['func_6910'] = func_6910
mod = relay.transform.InferType()(mod)
output = func_6910()
func_6911 = relay.Function([], output)
mutated_mod['func_6911'] = func_6911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5899_call = mod.get_global_var('func_5899')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_6945 = relay.TupleGetItem(func_5899_call(), 0)
call_6946 = relay.TupleGetItem(func_5901_call(), 0)
func_1396_call = mod.get_global_var('func_1396')
func_1399_call = mutated_mod.get_global_var('func_1399')
const_6954 = relay.const([False,False,False,True,True,False,False,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,False,False,False,True,True,False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,True,False,False,False,True,False,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,False,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,True,True,False,False,False,False,False,False,True], dtype = "bool")#candidate|6954|(112,)|const|bool
call_6953 = relay.TupleGetItem(func_1396_call(relay.reshape(const_6954.astype('bool'), [16, 7, 1])), 0)
call_6955 = relay.TupleGetItem(func_1399_call(relay.reshape(const_6954.astype('bool'), [16, 7, 1])), 0)
func_6551_call = mod.get_global_var('func_6551')
func_6552_call = mutated_mod.get_global_var('func_6552')
call_6965 = relay.TupleGetItem(func_6551_call(), 0)
call_6966 = relay.TupleGetItem(func_6552_call(), 0)
func_852_call = mod.get_global_var('func_852')
func_855_call = mutated_mod.get_global_var('func_855')
const_6978 = relay.const(4, dtype = "int16")#candidate|6978|()|const|int16
var_6979 = relay.var("var_6979", dtype = "int32", shape = (60,))#candidate|6979|(60,)|var|int32
call_6977 = relay.TupleGetItem(func_852_call(relay.reshape(const_6978.astype('int16'), []), relay.reshape(var_6979.astype('int32'), [60,]), ), 0)
call_6980 = relay.TupleGetItem(func_855_call(relay.reshape(const_6978.astype('int16'), []), relay.reshape(var_6979.astype('int32'), [60,]), ), 0)
func_6529_call = mod.get_global_var('func_6529')
func_6531_call = mutated_mod.get_global_var('func_6531')
call_6984 = relay.TupleGetItem(func_6529_call(), 0)
call_6985 = relay.TupleGetItem(func_6531_call(), 0)
func_1668_call = mod.get_global_var('func_1668')
func_1674_call = mutated_mod.get_global_var('func_1674')
const_6993 = relay.const([2,9,3,8,-1,4,-4,-6,10,9,10,5,1,-6,-6,4,-6,-9,7,8,2,7,7,-10,9,-3,9,4,9,-10,7,-3,7,6,9,-1,6,-7,-3,9,6,-10,10,-5,-4,-4,-9,7,-10,1,5,-8,-1,-3,2,8,-4,1,2,2,2,-8,4,-8,-8,-6,2,5,1,-8,10,8,-4,-9,-6,-2,-9,-1,6,9,-8,-7,1,4,10,4,9,5,3,-8,4,-9,-10,8,-10,10,-4,-10,8,6,7,-9,1,10,7,7,7,4,6,1,-1,-8,7,1,-4,-3,-6,-9,-6,1,6,5,-3,1,3,9,-3,10,-7,-7,-7,-3,-3,-7,1,10,-5,-3,4,-2,-5,10,8,-10,-10,-5,7,9,10,9,-6,-1,6,1,-7,8,4,2,9,-6,-10,9,10,-9,3,-2,-1,-2,-6,-8,8,6,5,5,-1,6,-3,-1,2,-3,-10,-6,7,-7,-10,7,2,-9,9,-2,4,-4,-2,10,-6,10,8,-6,-1,10,-9,-1,-8,7,-4,-10,8,7,-10,5,2,2,9,-4,5,4,-1,-5,5,8,1,-8,-1,-9,4,7,-9,-5,-8,-1,-5,7,9,-4,-3,4,8,3,8,2,-7,-7,7,5,1,8,-10,-9,-6,3,-5,3,8,-7,-9,-8,6,-3,5,8,-3,-1,1,9,-5,7,1,7,8,-8,1,-5,1,-7,7,4,4,-10,5,2,-6,-2,-3,-6,3,9,-8,-8], dtype = "int8")#candidate|6993|(288,)|const|int8
call_6992 = relay.TupleGetItem(func_1668_call(relay.reshape(const_6993.astype('int8'), [6, 4, 12]), relay.reshape(const_6993.astype('int8'), [6, 4, 12]), relay.reshape(call_6953.astype('bool'), [1, 112]), relay.reshape(var_6979.astype('int32'), [60,]), ), 3)
call_6994 = relay.TupleGetItem(func_1674_call(relay.reshape(const_6993.astype('int8'), [6, 4, 12]), relay.reshape(const_6993.astype('int8'), [6, 4, 12]), relay.reshape(call_6953.astype('bool'), [1, 112]), relay.reshape(var_6979.astype('int32'), [60,]), ), 3)
func_5882_call = mod.get_global_var('func_5882')
func_5890_call = mutated_mod.get_global_var('func_5890')
var_7002 = relay.var("var_7002", dtype = "float32", shape = (8, 60))#candidate|7002|(8, 60)|var|float32
var_7003 = relay.var("var_7003", dtype = "float64", shape = (4, 48))#candidate|7003|(4, 48)|var|float64
const_7004 = relay.const([-9.843928,-3.273480,0.115451,7.748430,-2.348064,-3.239742,-6.112767,1.220119,-5.168865,-1.713045,5.684810,-9.995957,1.458366,-7.100559,-3.953439,-2.313094,6.751671,8.295172,2.270163,3.615967,-6.724515,-0.299246,-7.388320,-7.945037,-9.069348,-1.768516,3.728103,1.223607,-4.036020,9.668337,9.290874,-1.510870,-9.482322,5.466754,-5.083327,1.060241,-4.429751,-0.331946,-1.103709,2.991990,7.934013,-9.167949,7.743142,5.351621,3.211007,-8.792625,6.784811,6.248100,-2.047530,4.756481,1.021554,5.072211,6.270703,9.633764,-0.525833,-5.335456,-8.037277,3.957515,-7.234639,-8.603740,0.603371,-7.051848,8.404325,8.187846,9.595729,-9.614972,3.273120,-3.385878,3.997011,-1.752438,4.971342,-4.345883,1.332272,2.055439,-1.414461,-6.990733,-3.839260,-9.047054,-2.282275,2.537367,0.788725,7.080185,8.204355,4.237327,9.924601,9.042141,-6.348399,-4.327394,9.321615,7.165222,3.475493,0.492553,4.300055,2.778769,0.475852,1.305617,8.379136,-7.248999,-9.393927,5.149172,4.729717,-9.995106,-7.623966,-3.618589,-0.003281,-8.755643,3.296697,2.619149,6.643693,-6.665143,2.716466,6.376217,-8.543285,-2.691116,0.101205,-4.874064,-3.924086,-0.082649,-4.755343,-8.402006,1.823615,-0.733254,-6.929037,3.955290,2.950357,1.677874,2.862152,0.448998,-7.030784,-1.224353,8.359585,-1.827619,-8.020306,0.902650,3.493831,2.044469,-3.983162,6.042330,-9.423302,-8.323443,3.550612,-6.128640,1.285602,-2.741821,6.806744,6.690257,-7.348423,-8.326756,8.535097,4.359426,5.356556,5.793184,-3.015472,6.588486,2.371639,-4.582934,0.162270,8.291202,-2.600857,-7.923727,-6.270495,0.110387,3.536863,9.012429,6.084473,-6.062485,-8.705338,-4.660819,-5.497176,8.200805,6.473802,-6.451947,-1.435542,4.395638,-0.345563,1.510279], dtype = "float32")#candidate|7004|(176,)|const|float32
const_7005 = relay.const([-5.427111,5.305984,0.573557,-5.909429,-7.843664,9.903968,-2.761595,-0.615260,2.648612,-7.224293,1.476221,-8.384300,4.260630,6.639699,-9.294549,-1.423761,1.523111,9.125345,0.666626,-7.115225,6.776771,6.881506,4.249950,-1.956329,-6.756115,8.744381,9.056979,-8.169007,-1.230588,6.178565,-3.063267,3.923832,6.139870,-5.589823,-0.652542,2.213559,-0.214952,1.770872,-7.492498,-6.310676,-3.745915,-0.706231,9.528281,4.909431,5.464095,-2.932872,-6.759237,2.446180,5.135256,-6.779450,0.629683,2.568985,-1.876936,5.176159,-0.095903,1.308755,3.742409,9.512148,5.390655,1.305488,3.317632,-6.985003,2.289347,-2.849860,5.416020,0.927006,-8.983610,-6.372824,9.290487,3.610011,5.168625,7.261911,-8.990403,5.956067,9.184190,-7.458970,-9.210922,-7.605828,9.759744,-2.113809,1.548548,2.261899,-0.746074,-8.795670,3.533578,-7.448950,-6.850422,8.975146,-6.511078,-9.252546,2.596219,-4.544040,0.081490,-9.184163,4.965875,9.745621,-4.492436,-5.884482,-0.410514,-1.437805,-3.812351,-8.895686,-9.918261,-1.565944,-1.613704,-2.768194,4.190565,-0.127135,4.283921,4.755085,1.475637,2.992051,4.004284,0.519161,-1.659676,5.233426,-0.319130,-2.227097,-0.032462,4.426362,6.974063,-2.431546,-2.565418,-3.022950,2.935971,8.646554,-4.542667,-5.602066,-8.681024,-3.661409,-1.807500,-8.555083,5.844989,3.942481,8.156966,4.877988,1.915959,6.663318,-2.888132,4.101316,-6.992560,-4.633772,-8.877604,-6.824706,-8.745351,2.227140,5.179935,8.168570,-4.823613,-9.453872,9.854864,5.115517,0.182544,0.976542,-2.760983,-0.543087,9.710748,0.958635,0.603245,-7.704493,-9.626828,-1.803844,1.827805,0.201393,6.552641,6.298658,5.444566,3.448408,-1.535617,-7.049837,4.191540,5.955510,1.442367,-4.495848,-8.690194,2.594871,4.856117,-0.752607,9.432230,-0.056478,2.173665,-9.758526,-9.284748,-7.340109,-8.564254,7.313599,7.848268,-9.973673,-8.628436,5.089356,7.801024,4.502795,9.255865,-2.528420,7.578037,6.725150,-5.680751,7.018050,7.562240,4.666280,-6.586192,7.275763,9.246901,1.756617,0.928270,3.116875,5.423584,7.486522,-3.796885,8.777325,-1.900488,5.481580,-8.882644,-4.298873,-3.102705,4.515127,-3.472494,-2.273140,-5.373833,1.826557,-3.528844,1.510307,-5.479703,-2.794036,-2.143154,-3.702540,-2.355886,0.156261,7.930964,-9.018285,-3.590684,-0.358361,7.350273,-8.802437,-6.902059,2.611888,-2.382876,-3.762581,3.024892,-2.383066,2.001694,-5.196901,-2.296357,-7.711724,2.880427,4.440834,8.041768,4.266593,-8.652921,-8.732971,7.689990,7.333005,-0.050227,-6.668598,2.808254,8.745604,-4.952845,-5.933918,-7.491324,-5.067527,-7.163035,7.858006,0.785432,-3.915372,-9.522112,4.486851,-7.442005,-6.636306,-5.108031,-1.991602,7.402711,-5.866475,7.425893,-9.588142,-4.683255,-8.301083,-7.473451,-3.757983,-7.769193,6.197022,7.613306,-7.015396,4.810591,5.042517,-9.374343,2.626827,8.467659,1.448620,5.698983,-5.707773,-0.182749,-4.624437,-6.121907,-1.398074,4.364600,-5.828119,-6.882381,-0.299845,2.549345,-5.071452], dtype = "float32")#candidate|7005|(300,)|const|float32
call_7001 = relay.TupleGetItem(func_5882_call(relay.reshape(var_7002.astype('float32'), [5, 12, 8]), relay.reshape(var_7002.astype('float32'), [5, 12, 8]), relay.reshape(var_7003.astype('float64'), [96, 2]), relay.reshape(const_7004.astype('float32'), [4, 44]), relay.reshape(const_7004.astype('float32'), [4, 44]), relay.reshape(const_7005.astype('float32'), [300,]), ), 0)
call_7006 = relay.TupleGetItem(func_5890_call(relay.reshape(var_7002.astype('float32'), [5, 12, 8]), relay.reshape(var_7002.astype('float32'), [5, 12, 8]), relay.reshape(var_7003.astype('float64'), [96, 2]), relay.reshape(const_7004.astype('float32'), [4, 44]), relay.reshape(const_7004.astype('float32'), [4, 44]), relay.reshape(const_7005.astype('float32'), [300,]), ), 0)
func_6154_call = mod.get_global_var('func_6154')
func_6156_call = mutated_mod.get_global_var('func_6156')
call_7008 = relay.TupleGetItem(func_6154_call(), 0)
call_7009 = relay.TupleGetItem(func_6156_call(), 0)
output = relay.Tuple([call_6945,call_6953,const_6954,call_6965,call_6977,const_6978,var_6979,call_6984,call_6992,const_6993,call_7001,var_7002,var_7003,const_7004,const_7005,call_7008,])
output2 = relay.Tuple([call_6946,call_6955,const_6954,call_6966,call_6980,const_6978,var_6979,call_6985,call_6994,const_6993,call_7006,var_7002,var_7003,const_7004,const_7005,call_7009,])
func_7016 = relay.Function([var_6979,var_7002,var_7003,], output)
mod['func_7016'] = func_7016
mod = relay.transform.InferType()(mod)
mutated_mod['func_7016'] = func_7016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7016_call = mutated_mod.get_global_var('func_7016')
var_7018 = relay.var("var_7018", dtype = "int32", shape = (60,))#candidate|7018|(60,)|var|int32
var_7019 = relay.var("var_7019", dtype = "float32", shape = (8, 60))#candidate|7019|(8, 60)|var|float32
var_7020 = relay.var("var_7020", dtype = "float64", shape = (4, 48))#candidate|7020|(4, 48)|var|float64
call_7017 = func_7016_call(var_7018,var_7019,var_7020,)
output = call_7017
func_7021 = relay.Function([var_7018,var_7019,var_7020,], output)
mutated_mod['func_7021'] = func_7021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6529_call = mod.get_global_var('func_6529')
func_6531_call = mutated_mod.get_global_var('func_6531')
call_7063 = relay.TupleGetItem(func_6529_call(), 0)
call_7064 = relay.TupleGetItem(func_6531_call(), 0)
func_5899_call = mod.get_global_var('func_5899')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_7065 = relay.TupleGetItem(func_5899_call(), 0)
call_7066 = relay.TupleGetItem(func_5901_call(), 0)
output = relay.Tuple([call_7063,call_7065,])
output2 = relay.Tuple([call_7064,call_7066,])
func_7084 = relay.Function([], output)
mod['func_7084'] = func_7084
mod = relay.transform.InferType()(mod)
output = func_7084()
func_7085 = relay.Function([], output)
mutated_mod['func_7085'] = func_7085
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7093 = relay.var("var_7093", dtype = "float64", shape = (9, 12, 13))#candidate|7093|(9, 12, 13)|var|float64
uop_7094 = relay.atanh(var_7093.astype('float64')) # shape=(9, 12, 13)
uop_7103 = relay.cosh(uop_7094.astype('float32')) # shape=(9, 12, 13)
const_7111 = relay.const([[[6.929840,6.560177,3.312255,-4.629160,1.382237,9.300792,-7.543764,8.058329,-7.224165,4.183805,-9.517698,7.366770,8.530534],[6.927829,2.187243,-6.810436,-9.857432,9.387885,-9.325500,-9.186579,7.924374,-3.750583,5.462622,-5.978003,1.917430,9.589119],[-9.333135,-1.416042,4.155624,4.756528,-6.946451,2.578465,2.578909,-8.497424,5.704023,-6.544625,-9.975518,-9.895242,-8.253506],[9.394636,6.235094,1.673624,9.641430,5.797033,7.447162,5.424783,9.261585,-0.655891,5.783222,-9.191715,7.314095,-7.242253],[6.674645,0.533391,3.699653,6.298528,-9.003742,9.232149,-3.330658,-8.355714,6.224660,0.867967,-5.568344,-2.656571,-5.542853],[-1.116276,7.403108,9.696668,-1.783505,-7.093513,4.561896,-5.174847,-1.997538,2.794208,-4.531037,-8.519442,2.327354,-3.320263],[7.528028,2.046467,2.259031,0.082702,-5.002564,7.006849,3.383604,6.990760,1.475709,-0.491352,3.999732,-3.997548,8.269357],[9.782660,-9.630024,3.726852,-5.327014,2.102251,-4.732910,-9.632167,1.368359,7.827756,9.250920,9.671568,-8.019068,-4.580146],[3.885874,-6.412870,8.750618,4.296083,1.032334,8.345163,-8.488440,-6.163084,6.999019,0.856093,-1.181122,-7.919636,0.389249],[4.097250,2.017990,6.721782,-7.143494,-2.333040,-2.279658,-3.587299,-5.778098,1.647331,-8.963139,5.708907,3.270141,1.159725],[-3.206122,7.236605,7.560736,4.687929,5.164795,-8.806332,-7.341716,9.295539,-0.578605,7.635606,-9.921956,9.781615,-5.049477],[-5.528585,-5.265665,3.567254,5.294538,-1.559889,3.372351,-0.872986,6.985084,4.677587,7.483470,-0.404047,-8.633405,-8.768314]],[[-3.979879,8.062177,-1.194188,-3.090408,0.062695,9.898576,9.575957,-4.370763,-3.241370,9.046941,0.383593,4.726866,4.979685],[-8.676913,4.387747,-9.552571,5.879151,-8.263946,-6.048810,-3.433478,9.984027,-2.971489,8.873665,0.616192,4.925791,2.976867],[4.450338,6.030156,-1.032749,-2.509461,-8.903217,-5.171147,6.766571,-1.673997,9.353975,9.718337,-3.843127,3.401293,-8.834037],[5.810168,2.560462,-5.790318,-9.233233,-9.528332,-3.846283,-3.845866,8.926800,-0.852912,-7.328371,-4.599961,7.560068,-9.240314],[-5.646813,3.749898,-0.303595,-4.915271,-7.089681,1.542216,0.038519,9.480476,-8.738439,-2.328033,-6.017852,-0.489299,0.787404],[0.765114,4.595623,4.518456,1.040079,-8.894217,4.433285,-0.499820,-4.745493,-6.562245,6.435835,5.746346,-4.603454,8.657099],[-4.107212,8.963508,5.282572,-1.341045,-9.636212,-6.247738,-7.868879,7.651118,5.908876,9.428549,6.116033,3.469943,-6.050208],[3.973887,6.165542,1.029100,-0.718286,1.086009,9.785306,-1.907434,0.613422,-8.199433,-2.385582,-2.124042,4.947441,8.871814],[5.793382,2.024395,4.389887,-9.953647,9.390798,-2.365564,-3.026860,6.411454,5.382094,9.369574,-6.357110,-7.500605,-8.996492],[0.033747,2.956179,-0.892535,3.264927,-8.299437,-3.622757,3.913920,-7.701631,-6.577139,-7.142917,2.321729,0.315132,-5.990660],[-0.098805,-8.709343,7.808108,-0.022245,-6.271787,-4.773499,-8.256360,-2.166217,5.979404,-7.372837,9.284141,8.847369,3.370654],[6.381132,9.582687,-2.887720,1.973990,-3.950168,-5.131857,4.946263,-1.681315,6.670582,-6.176335,7.024759,4.147553,3.060677]],[[-0.260224,-9.665515,3.281968,7.909937,-5.264335,-0.944779,-3.687741,-9.634610,5.040783,-9.593388,7.159146,-5.775672,0.368217],[-0.003556,-2.365052,-2.629957,-2.410077,-1.055987,-0.759845,-2.813983,0.343592,-8.169434,-1.633597,8.672046,-8.393964,2.000244],[4.319439,5.825020,3.472820,4.494454,-2.279455,8.241090,6.009362,-8.291612,1.431297,-7.327217,-0.753562,-5.028478,4.667937],[-0.293724,9.283822,-1.340298,-6.934568,-8.776979,9.165154,5.602083,2.484873,-7.473736,-2.981250,-3.126375,0.625696,-8.700223],[-2.701529,-8.131468,-2.803062,1.223119,-2.119541,-4.193799,-7.718058,3.301914,8.437755,5.157264,4.874657,2.942209,-9.520278],[0.312744,-9.001358,6.075337,-9.483024,-8.854796,4.275439,3.253763,8.964457,-6.406173,-9.916707,0.300331,-7.282859,-1.593608],[-2.199917,9.692949,1.993774,0.841374,-6.359030,-0.272324,-2.786653,-5.286742,5.470026,-1.181391,0.868607,-4.659588,-3.681879],[6.442652,-3.946920,-6.473442,6.646529,1.195806,-4.016618,-2.429796,-2.163439,0.262506,-2.189571,-9.688157,0.772728,-3.517994],[5.614537,-1.282926,8.890279,-3.439787,9.099567,-9.213200,-8.882161,-2.715135,-2.589303,5.513476,0.108674,-6.387609,-0.032540],[0.641032,3.281953,9.203698,-4.363277,-6.334253,9.782369,5.076590,2.087362,-2.474016,-7.835860,-3.614227,8.177589,3.401516],[-4.958939,-3.823130,-5.807466,2.021890,-7.172535,-1.947998,-1.229201,-7.415860,7.214388,9.708701,8.278359,-6.262524,-3.207749],[5.995174,-6.661006,-3.641253,-4.203169,-4.032377,3.983744,-2.192106,-0.417816,-0.641130,6.147856,-4.261883,1.036348,8.055348]],[[6.038760,-8.132394,-7.222661,-8.444560,-5.204664,2.549869,3.111627,5.937581,2.215054,-9.036866,-1.585491,3.403746,5.893241],[-3.878201,7.457256,-1.631499,5.035659,-4.320087,-3.802099,-0.793404,1.268517,0.481084,7.844907,1.592302,-8.752321,-8.284666],[2.041795,-3.191591,-9.982673,3.847963,-5.911555,-4.057610,-6.534418,2.770350,5.255543,1.367829,5.768665,-5.508381,3.830649],[-6.775710,4.873264,-6.346345,-9.063167,-2.462332,8.572552,-3.086333,1.990407,1.313583,7.742888,-2.567529,-3.178895,2.498400],[-6.504935,1.683076,-4.521063,7.086130,-7.256257,-2.708746,-1.848829,7.541604,-4.435613,4.143132,2.818167,8.635032,2.256179],[1.654948,7.567014,4.492176,-5.634933,7.278726,-8.126989,9.506846,-5.944590,9.602106,-1.702693,-3.437042,-2.311339,-5.086348],[-5.448759,-2.096525,5.995826,1.483846,3.727019,-9.343104,1.826754,-3.204106,-4.082207,2.758161,0.425013,9.574548,0.075500],[-6.395303,0.667138,6.411442,-3.690507,0.042980,-6.800069,-3.086181,3.423288,5.456398,-7.715187,4.044120,0.120879,4.712283],[8.203804,-3.755602,-8.949649,5.101183,0.012513,0.533369,-1.842277,7.099541,2.344037,-5.459863,-4.212667,-1.588120,3.873772],[9.196900,-2.029010,6.285907,8.707615,-1.372128,-7.059219,5.769939,1.159729,7.031863,7.880171,-2.895100,-9.603687,-3.784097],[-8.431744,1.623739,-9.642281,4.747722,8.850431,-7.785651,-5.223724,-0.940287,-1.817731,7.076954,-0.007059,-9.278983,1.229775],[0.908591,1.218267,4.693267,-5.054504,-2.147105,1.063848,0.373715,-4.292524,-0.526736,-3.924629,-7.429398,-1.898958,-6.384446]],[[-2.279325,4.851503,9.118658,-2.639878,-4.353159,7.519408,-2.491864,0.606251,7.579856,3.820185,-4.309764,-0.264196,-5.715099],[-0.627868,-8.772582,-5.587875,4.532636,4.664528,-9.711049,2.481105,7.544502,1.837827,-8.166209,3.134252,6.386740,-6.570984],[-9.228155,-9.044024,2.662018,-4.205693,-1.375149,-1.735650,-6.509918,-8.020315,5.752987,9.803102,-1.615799,9.661145,9.361457],[-3.649599,5.137594,-3.794297,-6.793432,-1.180827,6.305589,0.442132,6.736460,6.494299,9.787619,-2.482052,-8.378917,5.581622],[-6.840728,5.555427,-0.192352,-5.421746,-2.630037,4.986560,-0.762315,-8.733282,-0.152601,3.000641,-5.400426,3.963320,-2.584033],[-2.739387,5.255056,-1.745383,-4.509687,2.851018,3.286121,-1.732110,7.793527,-4.313613,-5.066864,6.334127,1.034322,-8.854712],[-9.046531,3.012065,-5.947670,3.769760,-3.522090,3.592878,7.873366,8.817771,1.615399,8.850318,9.484435,-3.381414,-7.925294],[6.402825,-8.706970,5.165949,3.660244,5.472347,0.074962,-9.173687,-5.851182,-7.937348,-5.330114,5.087578,-0.050123,-4.913322],[-0.003679,5.195554,3.817989,-6.535799,-7.214584,-0.151671,5.083506,7.419934,-1.777719,-2.989751,-2.721837,-2.626590,-8.134860],[-3.831511,-2.884268,-9.239867,3.212051,-7.422691,-1.470603,-7.379924,-3.198535,4.369726,-1.441996,-2.631921,-2.745879,-2.412021],[-4.303881,9.956493,-7.970516,9.566229,3.203542,4.895511,4.551196,2.098453,9.850961,-4.655353,-4.569575,9.431882,0.120599],[5.826625,-6.200272,-7.782016,-0.441715,7.197350,4.615059,-9.378737,-4.249741,9.689020,4.197427,-0.791820,-1.346697,-1.591679]],[[-3.777023,3.817564,-3.335108,8.724808,-6.087400,9.348653,5.931659,8.947544,0.058926,4.059429,-7.756380,5.241590,7.721664],[-7.923597,-2.276003,-9.558420,-3.280334,-3.312622,-5.785650,5.718381,8.789072,-5.913678,0.564791,8.054592,4.584885,-7.040718],[5.185993,2.467842,7.414498,-6.980087,-9.958400,-4.753441,9.811109,1.030793,-1.251728,-3.252718,1.985643,3.252476,6.778058],[0.886891,7.950514,-3.120024,0.504075,-1.580386,6.304334,0.703319,7.690192,-9.587967,-1.435527,6.774487,-3.022351,5.004741],[-0.962417,-8.115647,6.719920,-6.877574,1.806554,-4.232487,-9.714319,-0.598871,0.997437,7.454106,2.890162,8.661780,-8.204595],[6.253960,0.489243,-6.861065,2.147981,9.274636,8.825381,9.277854,-5.429935,6.486090,-7.701305,-2.988747,1.007140,8.277051],[7.315920,4.464188,5.673717,-3.294017,2.084332,-9.475214,8.110301,0.246343,9.203098,2.042519,-7.325913,-6.171310,-9.896980],[7.001799,-2.297897,9.011017,9.967010,2.755272,9.695334,9.497492,8.909876,0.157625,9.465192,3.053535,5.613628,-7.827915],[7.258130,2.822785,5.770087,-6.254546,9.733957,4.507498,-3.852112,7.566523,-4.485134,-9.336357,-3.865460,-0.427340,-2.296939],[-1.436135,9.212260,-6.799066,2.337923,-1.588078,-0.823513,-9.898967,-3.372807,-0.967689,6.265770,-6.630631,6.246105,5.304629],[-3.642695,7.018048,1.818563,0.031252,9.314323,0.296145,4.615048,0.270861,-0.347553,9.534913,-9.443581,6.203867,2.979378],[0.230086,-8.743270,-5.257765,8.224836,-9.836653,6.867574,0.090964,1.703656,0.822736,-4.641246,-5.458776,-7.080594,-6.554034]],[[0.061245,-6.060853,1.862483,3.828950,-3.377735,8.337560,-2.716357,-4.664650,3.685217,-5.361288,4.794756,3.617928,-5.884056],[-9.094981,3.898925,6.374517,0.373623,6.194259,-6.883316,-9.711908,-3.263723,-9.050054,7.163381,-2.147870,-2.829590,9.577905],[-0.743593,4.074620,-4.881872,6.300703,-1.948806,4.413171,1.189304,9.458851,0.680898,-1.876960,6.078721,-9.428316,-7.460703],[9.176277,7.531745,-1.082410,0.497743,2.210102,8.147057,5.057065,1.334075,8.916222,3.222099,-0.995782,8.933676,-9.095735],[6.470339,3.835396,7.189679,-3.696992,-7.597348,-0.075598,1.715789,2.248061,-0.588266,-1.012339,6.385818,-8.181504,-2.722533],[-9.348932,-9.335779,-8.532989,4.238782,3.111961,-4.440525,-3.597976,-7.682651,-8.009784,-8.090667,-8.241507,-6.459471,-2.878224],[5.734512,-9.385810,-2.665967,6.804311,2.152610,-8.369295,5.085877,3.435014,-7.592858,-1.364900,-5.804626,-4.408214,6.648048],[-4.884447,8.351674,0.115533,8.570913,1.134147,-8.017552,-8.128049,-6.018101,7.666191,-7.037885,-3.588526,-9.419871,6.429147],[0.304348,3.015314,9.330259,4.758170,-7.995090,6.563183,-5.948692,1.054518,5.189927,1.313120,6.225514,2.709395,6.147417],[-4.160577,8.193313,9.573421,6.068352,5.147186,-0.850677,1.081984,5.251651,-5.901935,6.047381,5.597085,-3.711449,6.887442],[0.694719,9.720929,-0.153271,-6.136922,-9.354862,-0.782032,-6.193037,-4.174405,-8.109559,4.632752,-5.305557,-0.061932,-9.833844],[-0.301638,-5.530833,-7.566870,-9.442260,-1.900975,4.933792,-5.422031,-8.051446,3.057619,-7.632743,1.845110,5.422740,4.565941]],[[6.927158,-8.036553,7.783728,-5.790355,-9.261480,6.170872,-4.820974,8.075096,-6.731522,9.965418,-2.980871,3.242480,-7.431627],[-7.076806,4.635132,8.229929,8.809842,-3.684600,-2.782391,-3.195937,5.990282,-3.399451,5.700772,1.284979,0.242309,1.251439],[7.759169,4.240782,8.338692,-0.832312,0.547468,9.016121,9.423510,9.307147,-0.738872,-3.638863,3.500685,-2.003302,-9.322916],[-1.305280,-0.252997,3.801810,-6.469760,-8.665720,-4.862339,-6.416550,-6.234915,-0.661999,-5.633381,-0.794701,4.868866,-3.862360],[0.358243,-1.261755,0.922725,3.442516,-0.420765,9.535377,6.164047,-6.393612,-2.213105,1.493023,6.342348,-4.929037,4.362986],[-5.995938,5.452225,7.259855,4.625041,-9.724019,-2.065031,4.936182,9.155384,5.918346,-0.053155,-6.231581,4.395904,6.500173],[-4.870211,-9.084157,-1.703214,-3.843010,7.180905,-7.864681,1.842948,8.491644,2.544991,-0.318075,-0.189730,2.333796,-2.704510],[0.316094,-8.172258,-0.356237,6.270682,-7.323448,3.186818,8.692120,1.860601,-1.372371,3.822132,-1.250402,-5.220994,7.580818],[8.082465,3.480884,-6.770566,8.558335,4.104860,8.035180,-5.229355,6.428766,9.739244,-1.587965,-9.737802,6.090589,7.343436],[-6.723498,1.009879,-9.015645,7.535561,-3.716695,-7.048038,-5.724416,2.041860,-8.437260,1.588402,7.080454,4.250250,8.437650],[-2.941210,3.552216,0.168980,3.326009,9.609613,9.983920,9.351097,-0.785388,4.034700,-3.950107,9.858417,-7.394019,-7.573104],[2.403982,5.671545,1.894292,4.730305,9.201996,4.525722,6.715467,-9.479100,9.674396,-5.290117,-1.499675,-8.959317,-3.450610]],[[4.615550,-5.675997,4.457397,5.975687,6.632134,-3.022361,4.113747,5.774631,6.885468,0.765757,5.642153,3.945302,3.202691],[0.044996,-1.126109,2.201606,-8.698134,9.035627,5.201082,-6.360691,-8.536100,2.751386,4.531140,-8.748746,-5.556397,-4.522523],[-2.616856,8.210795,6.679580,3.127959,7.845178,-9.651091,-1.691429,5.624338,-4.032233,-2.361560,-4.088910,5.852433,-5.593138],[-6.820652,0.297453,-8.928761,0.667749,6.471039,-6.781635,-9.192123,9.119881,9.994088,3.838446,3.727200,0.965095,-5.184813],[-2.718893,4.066731,5.354325,3.532854,-5.500598,-0.690878,1.712348,9.057720,-4.379772,2.177147,-8.133549,2.297212,5.783231],[3.303821,2.674308,3.228405,1.190430,-5.620916,-4.676500,-6.159893,-8.700832,-1.365069,-8.056048,2.052353,-6.555954,5.295900],[-5.962806,-1.406629,2.915790,-4.217063,7.222463,-3.195004,-6.875510,1.203063,-3.002089,8.486266,-9.450589,3.843863,0.444916],[2.665202,2.371962,-4.823868,1.655473,-0.648525,5.002805,9.194787,-8.605470,6.767522,5.234420,7.490689,-8.328371,-3.938052],[1.546095,-6.772484,-2.452393,-2.450091,-9.973617,5.050595,6.149266,-1.276408,-1.520409,2.202985,-2.392680,9.260942,7.684739],[6.380048,-3.701844,-6.941508,2.574022,-6.480461,-9.758481,-5.920207,-3.045631,-1.609940,9.222364,-0.465088,9.479814,-9.454247],[-6.868835,0.070170,-7.084323,-6.709879,-3.376894,-6.762872,1.909613,9.364094,2.596917,-0.909031,-8.594336,3.601960,7.500990],[1.308475,9.469619,-3.183083,-8.633072,9.858961,3.361525,7.752156,-8.692668,6.519120,-9.578013,0.256856,-9.307771,5.428186]]], dtype = "float32")#candidate|7111|(9, 12, 13)|const|float32
bop_7112 = relay.mod(uop_7103.astype('float64'), relay.reshape(const_7111.astype('float64'), relay.shape_of(uop_7103))) # shape=(9, 12, 13)
bop_7115 = relay.floor_mod(uop_7103.astype('float32'), relay.reshape(const_7111.astype('float32'), relay.shape_of(uop_7103))) # shape=(9, 12, 13)
bop_7121 = relay.not_equal(bop_7115.astype('bool'), relay.reshape(uop_7094.astype('bool'), relay.shape_of(bop_7115))) # shape=(9, 12, 13)
output = relay.Tuple([bop_7112,bop_7121,])
output2 = relay.Tuple([bop_7112,bop_7121,])
func_7145 = relay.Function([var_7093,], output)
mod['func_7145'] = func_7145
mod = relay.transform.InferType()(mod)
var_7146 = relay.var("var_7146", dtype = "float64", shape = (9, 12, 13))#candidate|7146|(9, 12, 13)|var|float64
output = func_7145(var_7146)
func_7147 = relay.Function([var_7146], output)
mutated_mod['func_7147'] = func_7147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6154_call = mod.get_global_var('func_6154')
func_6156_call = mutated_mod.get_global_var('func_6156')
call_7151 = relay.TupleGetItem(func_6154_call(), 0)
call_7152 = relay.TupleGetItem(func_6156_call(), 0)
output = call_7151
output2 = call_7152
func_7162 = relay.Function([], output)
mod['func_7162'] = func_7162
mod = relay.transform.InferType()(mod)
output = func_7162()
func_7163 = relay.Function([], output)
mutated_mod['func_7163'] = func_7163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6480_call = mod.get_global_var('func_6480')
func_6482_call = mutated_mod.get_global_var('func_6482')
call_7192 = relay.TupleGetItem(func_6480_call(), 0)
call_7193 = relay.TupleGetItem(func_6482_call(), 0)
func_7145_call = mod.get_global_var('func_7145')
func_7147_call = mutated_mod.get_global_var('func_7147')
var_7217 = relay.var("var_7217", dtype = "float64", shape = (1404,))#candidate|7217|(1404,)|var|float64
call_7216 = relay.TupleGetItem(func_7145_call(relay.reshape(var_7217.astype('float64'), [9, 12, 13])), 1)
call_7218 = relay.TupleGetItem(func_7147_call(relay.reshape(var_7217.astype('float64'), [9, 12, 13])), 1)
func_2936_call = mod.get_global_var('func_2936')
func_2940_call = mutated_mod.get_global_var('func_2940')
const_7220 = relay.const([-1,6,2,9,6,-6,3,-9,10,-2,6,9,-8,-1,1,9,-6,-7,-6,6,4,-8,3,4,9,-6,9,-2,-10,-10,-8,-4,3,1,-10,5,2,1,-1,1,-2,-5,-2,-7,-2,3,5,-2,-1,-2,-3,4,-10,-1,1,-3,8,-5,-6,3,9,-10,5,7,-7,8,-3,5,7,-6,-9,3,-8,-10,-1,4,10,6,-6,-3,1,-4,4,-8,9,-9,-3,-8,1,7,10,1,5,-9,-2,5,6,6,9,10,9,6,4,-5,1,-6,-3,-5,6,-9,-6,10,2,-3,1,10,-5,-2,-2,3,-6,6,-5,8,-5,-8,1,-5,5,5,1,3,-4,4,-9,9,5,-7,-8,-4,1,-6,-1,7,-10,9,10,7,5,1,-10,1,8,8,4,1,-3,10,-1,-7,9,-2,7,4,5,-8,-6,10,1,-3,9,10,2,-5,7,2,9,-5,-7,2,4,5,-3,7,-5,6,-4,-8,-8,-7,-9,1,5,6,-6,-2,-10,-4,5,4,-10,6,9,-10,8,-2,-6,-5,-8,5,-1,6,-7,4,-10,2,1,5,3,-8,1,-8,-2,2,-5,-6,5,8,2,3,-10,-3,-4,-10,-4,-6,8,-3,-6,-2,3,7,-2,1,-9,-6,-1,8,7,-10,6,-5,-9,-9,-5,-8,-1,-10,2,-4,6,-9,-9,2,-7,-5,10,9,8,6,9,4,1,-2,5,-3,8,-10,9,10,-6,-10,7,-8,9,2,10,-7,-2,-3,7,-10,9,9,-3,5,8,-10,7,1,3,-4,-1,-5,2,-10,7,-3,9,6,4,5,-9,8,2,9,-5,10,4,7,-5,-6,-6,-9,-2,8,6,-8,8,-10,5,6,4,6,-3,-5,-1,-1,9,-3,-4,-7,-4,-7,10,1,-9,-7,-6,3,7,8,-9,6,-10,9,10,8,8,6,-5,3,-5,8,-3,-1,-9,10,-1,-5,7,-6,-7,-1,-10,-5,4,-10,8,10,-1,4,3,9,10,6,-10,-4,-7,-4,-2,3,-6,-4,-4,-6,9,-6,-3,6,-1,-3,-7,7,-2,2,-9,9,-9,-8,9,-8,5,3,-1,3,3,2,-3,-3,-10,-8,-9,2,1,-1,-5,3,4,-10,-4,8,7,7,-9,-4,5,-7,10,-2,-1,-5,3,8,3,2,-9,5,10,-5,-2,7,-2,2,4,-6,7,3,1,-5,9,10,-8,5,8,-7,10,8,8,3,1,7,3,6,-1,-6,10,10,2,-8,-5,1,-6,-5,-8,-6,-10,-9,-5,6,-7,6,-8,-9,-10,-3,9,10,6,2,6,4,-3,8,7,-3,6,-4,-6,9,10,-2,-7,-6,8,6,10,-9,-3,10,-2,-4,2,3,3,-5,3,1,10,4,7,-3,1,9,-10,4,2,10,-10,-4,-6,-5,8,10,3,-7,7,-7,-1,-2,5,-3,-6,1,-6,8,-7,1,-8,3,-9,2,-10,4,-3,-2,-4,5,8,9,-2,7,9,5,1,9,-8,-5,7,-10,8,1,7,-6,-2,10,-2,-5,7,10,-8,9,9,-8,5,-9,2,-7,-5,-5,-7,-3,1,2,10,5,9,5,10,-4,-1,-8,-4,1,7,6,-8,5,-9,-9,-8,-6,-10,7,-6,5,-6,10,7,9,5,9,8,-7,2,-7,-2,-9,6,2,-9,-9,9,4,9,9,-9,-1,6,-6,-4,1,6,8,-8,-3,-9,-9,-10,-6,6,-4,6,4,3,-10,-10,3,-1,-9,-5,-3,5,-5,-4,-5,-6,7,-6,2,10,-6,-1,8,2,-10,-8,-3,4,7,9,-10,2,-7,-8,-8,10,-9,-5,-4,4,5,-8,4,-6,-2,4,-10,-9,5,-5,-4,-8,-10,9,1,-10,5,5,-10,4,-8,3,-7,6,-8,6,7,-6,-9,3,-8,8,-10,5,-6,3,-9,3,-7,-7,-1,8,9,7,8,-7,4,10,-10,6,-5,-1,3,8,4,-6,2,-7,9,8,5,-4,3,-2,8,-9,7,7,6,2,3,-9,4,-6,9,10,1,4,9,-7,4,-2,-9,-2,4,-7,4,2,9,2,-3,-3,-8,8,-2,6,4,8,-5,-6,-6,8,8,-7,9,6,-4,4,-5,1,9,5,3,5,-6,9,-6,2,-6,-5,-8,4,-2,-6,-3,6,4,7,7,-7,5,-6,10,8,-5,-10,-4,7,-7,2,-1,3,-2,-3,4,-3,-4,3,7,2,4,6,-10,-3,7,-8,6,4,-4,8,-4,7,9,4,1,9,1,3,-10,8,-2,8,8,5,-8,9,3,2,6,-10,-3,4,6,-3,4,8,10,5,7,-9,2,-6,4,8,3,8,-9,-10,-10,3,-6,1,6,-3,5,-9,8,3,-5,-1,-1,6,1,-4,9,-6,-8,-1,2,-9,-6,3,6,-5,7,9,6,9,-1,10,-2,-5,3,7,1,-2,6,10,-3,3,4,-9,9,-10,1,-10,-6,3,2,7,-8,10,-6,8,-7,9,-6,2,4,-8,1,8,-5,-9,3,-2,-6,-8,5,10,-8,-3,-7,2,6,8,7,5,9,1,-1,-6,7,7,-10,4,-8,-4,4,6,-5,-9,10,-6,-9,2,2,-9,2,1,-5,-3,3,-5,3,-9,6,1,-2,-7,-6,3,9,-8,-7,4,-5,-4,4,7,1,-6,-4,4,-5,-8,-10,-10,-2,9,-9,-3,1,3,5,3,-8,4,7,9,-7,-3,-8,5,1,-3,-8,-5,2,-4,-9,-4,7,10,-3,6,-6,8,-1,-5,-6,3,5,-3,-3,3,-6,-1,-4,-7,-10,1,-1,9,2,4,-4,-2,-2,-5,1,-1,6,10,-2,9,1,5,8,5,2,8,6,-5,4,-5,8,2,7,6,-10,-9,-6,6,-10,6,10,-8,-3,-5,2,3,-6,-6,6,2,8,10,6,9,-5,-10,8,-3,10,1,-10,6,7,10,-5,-3,4,8,-7,7,-2,9,6,5,10,10,8,7,-9,1,9,-10,7,-4,4,8,-10,-8,-1,-2,8,-2,-9,6,-7,-5,-2,9,10,-4,5,-2,1,9,6,-4,5,-3,-4,-2,5,-7,-2,-6,2,-9,-2,-1,-5,-4,4,-5,3,-3,6,-9,-5,-8,5,-1,4,3,3,10,8,8,3,1,9,4,-1,8,9,3,2,2,-6,-3,-1,-8,8,-1,7,-6,7,-4,10,4,-10,5,3,-7,4,-9,-2,4,-10,10,8,-6,3,-3,3,-6,4,-4,-1,-5,2,10,10,-3,-8,2,8,-10,9,6,1,-7,-3,4,-4,9,-5,-10,-2,9,-6,7,-8,-5,-2,-1,2,10,10,9,2,-8,8,4,-10,3,2,10,-9,-9,5,-6,1,-2,9,-5,-3,8,2,3,-4,8,4,-8,-4,-6,8,-5,9,9,1,8,6,5,-9,10,3,-9,-7,-2,5,-9,1,1,-1,7,-4,-4,-3,8,7,5,-7,7,-3,-6,-8,-3,-9,10,-5,-10,3,1,4,10,-9,-1,1,-2,-6,3,3,2,10], dtype = "int32")#candidate|7220|(1350,)|const|int32
call_7219 = func_2936_call(relay.reshape(const_7220.astype('int32'), [15, 6, 15]), relay.reshape(const_7220.astype('int32'), [15, 6, 15]), )
call_7221 = func_2936_call(relay.reshape(const_7220.astype('int32'), [15, 6, 15]), relay.reshape(const_7220.astype('int32'), [15, 6, 15]), )
func_7016_call = mod.get_global_var('func_7016')
func_7021_call = mutated_mod.get_global_var('func_7021')
var_7236 = relay.var("var_7236", dtype = "int32", shape = (30, 2))#candidate|7236|(30, 2)|var|int32
var_7237 = relay.var("var_7237", dtype = "float32", shape = (8, 60))#candidate|7237|(8, 60)|var|float32
const_7238 = relay.const([[-1.739920,3.577255,-0.602021,-0.616126,3.822432,0.643513,1.746139,2.986312,0.512010,2.113103,2.965231,-8.073556,0.717928,1.711471,-0.041550,3.897760,-2.212490,7.802098,-4.934411,8.756828,-1.822406,-0.616211,-0.800599,9.018512],[1.116969,0.531304,-6.193585,-2.730584,-6.304201,-2.251696,6.363585,3.807165,-2.746499,-2.215460,-4.113721,-4.096318,0.341500,-1.858084,-4.731514,8.827699,-7.671481,-4.288940,-9.765971,3.459944,2.617859,3.012316,7.999702,-3.035588],[5.380322,9.427814,-2.546545,-9.535233,-3.324749,0.489946,-1.770387,-1.969393,-7.257544,-6.719966,1.221566,2.209902,2.415020,3.054133,8.297685,-3.640081,4.117272,-0.415748,0.980335,4.922619,5.702322,-0.923646,5.656405,-7.686198],[4.896480,-8.057190,-7.878540,2.221022,-9.311347,0.612160,7.319876,6.404995,6.591119,-7.590956,-1.153465,-0.095762,8.628906,-0.862125,8.918765,-0.396604,9.180233,0.601596,-1.754308,7.284799,3.477863,-4.901583,-9.359888,4.223981],[9.775006,-7.967214,9.898716,7.715919,9.120269,9.723516,-7.316977,7.663190,-2.977077,-7.905598,-2.438232,-5.744288,-2.530225,-1.094540,-8.623277,-4.264346,1.455169,3.880330,3.600874,3.651635,-1.037928,8.589540,-8.884432,-6.405962],[2.747664,4.648028,-2.976301,1.215686,-9.935762,5.402289,-3.685683,-2.845324,-4.425626,-3.014227,-1.722382,-1.022244,0.944991,-8.611109,6.121778,-2.867977,9.437227,-6.584429,8.919463,-0.089635,1.626208,-1.551382,2.434904,5.541467],[5.802012,2.198616,-7.333220,-6.371432,5.452827,6.276081,-4.228841,8.393531,-7.337010,4.686636,2.181525,8.314008,-7.712136,-2.159820,8.469941,8.454449,-0.725532,-2.356951,4.396339,-3.736615,3.166136,6.725784,4.326340,1.502564],[-5.926269,-5.389842,-1.222335,-3.418390,2.522017,-6.179162,-5.090670,7.762736,-1.340559,1.355081,2.647361,-2.824715,-6.689325,-9.680002,-9.822864,7.410105,-1.850554,9.314247,7.857025,7.728714,-0.797316,6.971219,-6.363993,0.911342]], dtype = "float64")#candidate|7238|(8, 24)|const|float64
call_7235 = relay.TupleGetItem(func_7016_call(relay.reshape(var_7236.astype('int32'), [60,]), relay.reshape(var_7237.astype('float32'), [8, 60]), relay.reshape(const_7238.astype('float64'), [4, 48]), ), 9)
call_7239 = relay.TupleGetItem(func_7021_call(relay.reshape(var_7236.astype('int32'), [60,]), relay.reshape(var_7237.astype('float32'), [8, 60]), relay.reshape(const_7238.astype('float64'), [4, 48]), ), 9)
uop_7252 = relay.sinh(call_7216.astype('float32')) # shape=(9, 12, 13)
uop_7254 = relay.sinh(call_7218.astype('float32')) # shape=(9, 12, 13)
func_2095_call = mod.get_global_var('func_2095')
func_2098_call = mutated_mod.get_global_var('func_2098')
var_7274 = relay.var("var_7274", dtype = "float64", shape = (252,))#candidate|7274|(252,)|var|float64
const_7275 = relay.const([[5,-10,2,8,-6,10,-10,2,-6,-8,-10,-9,10,1],[-5,5,-5,-1,-2,-9,-6,8,3,3,-6,8,7,3],[7,3,3,1,5,-4,-1,-5,1,-2,-5,6,8,-7],[1,10,-6,-1,-5,8,2,-6,3,7,-9,10,6,5],[-10,-6,-4,1,3,10,4,-5,10,-9,-7,8,-7,-7],[-6,4,-7,-9,1,3,-3,10,-1,-6,-8,-3,-3,-10],[3,3,2,-7,2,-1,7,-4,7,2,1,-6,-2,6],[1,-6,-3,-6,-8,5,-1,2,-10,-10,10,-4,9,10],[10,9,-1,-8,5,9,-6,-5,1,-5,-4,8,9,5],[-2,1,2,-5,-6,5,-8,-9,9,1,1,-2,3,9],[2,1,-10,9,-4,-4,9,6,-6,-2,-10,6,1,8],[-8,7,2,5,10,-7,8,9,-3,-5,-9,-5,-3,2],[-8,7,1,5,2,9,-4,8,-8,-9,1,1,4,1],[-8,9,-7,-2,-2,2,-7,-8,7,-2,5,5,9,8],[-3,-1,5,-7,-8,-1,-7,6,5,-6,-2,-5,-2,-2],[8,4,-10,2,-5,-6,-9,-5,9,2,-5,-6,7,-3],[6,1,7,5,2,-1,-6,2,-5,4,10,9,4,-2],[9,-9,-3,8,8,5,9,-7,-4,-4,7,2,4,5],[-9,9,4,-2,10,5,1,10,-8,9,-7,1,-1,-3],[6,-4,-5,-4,3,-6,-6,-5,-2,9,1,2,-2,-5],[-7,9,6,-10,-6,-2,10,4,-10,3,3,2,1,-3],[6,-6,-6,-8,-8,-5,-3,-3,-6,7,7,8,1,3],[1,-4,2,9,3,-10,6,-5,-4,-9,9,-6,5,6],[1,7,5,-10,1,5,-7,-7,10,-9,2,7,-4,-8],[7,7,3,-2,5,-5,1,2,-7,-10,-1,-3,9,-6],[3,3,8,-7,-2,-1,-3,5,8,-2,6,-2,-3,2],[5,4,-2,5,7,-2,3,7,-4,9,-4,9,-5,9],[-7,1,-8,9,3,1,8,-8,9,-8,-2,6,-10,-7],[5,-6,-6,-4,1,6,9,-4,1,1,-1,-4,8,8],[5,4,1,2,-4,-4,2,-10,5,10,-8,-7,-10,2],[3,7,-5,-9,10,4,10,10,7,-4,6,10,7,-4],[10,-6,-6,-2,1,-7,-3,-6,8,8,7,-10,6,-10],[-9,9,-10,4,-5,7,10,-8,5,-7,-1,10,6,5],[-10,-6,-9,10,-9,5,3,-3,-6,-7,6,-3,8,7],[3,-8,6,2,9,5,8,-4,-2,5,8,6,-5,-3],[4,9,-9,-10,10,-10,-6,7,-5,-7,9,-2,4,-3],[10,-4,-3,10,1,-8,-2,2,-3,1,1,4,8,7],[5,10,5,10,8,-1,-9,-2,7,-8,4,-8,-7,-6],[-10,6,-2,-1,-4,-6,-10,-3,-6,-2,8,3,1,-8],[-6,3,7,1,10,8,-4,6,1,-5,-4,-10,-8,6],[-6,8,-7,8,-2,5,3,-6,8,-3,9,8,6,8],[10,-7,-8,-10,8,1,9,4,9,-10,-9,-8,4,4],[3,-6,-5,1,10,8,-1,7,-5,3,10,5,-10,-10],[8,-4,5,5,-5,-1,10,-10,-10,-1,10,1,9,9],[-8,4,2,-8,-10,-5,1,-9,-9,4,-7,-4,-10,7],[2,1,-5,-5,-2,4,-8,-6,-8,2,3,-5,-10,7],[8,9,2,-8,-4,-5,-8,8,-7,6,9,-3,3,-3],[8,3,8,6,4,6,-8,6,-10,-3,1,2,-9,-4],[-4,-5,1,-10,2,6,9,3,2,3,-6,-1,-8,-8],[-10,9,-1,6,-4,10,2,1,-9,9,6,5,10,10],[9,-7,2,2,-2,-5,7,-4,1,-10,-2,2,-1,-1],[-1,1,8,-8,3,4,-8,-2,6,4,1,-10,3,2],[-8,-6,-3,10,2,4,8,1,-8,-3,-10,4,10,-8],[-5,-8,-3,-4,1,2,4,9,3,-9,6,9,-10,-9]], dtype = "int8")#candidate|7275|(54, 14)|const|int8
call_7273 = relay.TupleGetItem(func_2095_call(relay.reshape(var_7274.astype('float64'), [9, 4, 7]), relay.reshape(const_7275.astype('int8'), [756,]), ), 0)
call_7276 = relay.TupleGetItem(func_2098_call(relay.reshape(var_7274.astype('float64'), [9, 4, 7]), relay.reshape(const_7275.astype('int8'), [756,]), ), 0)
func_6303_call = mod.get_global_var('func_6303')
func_6307_call = mutated_mod.get_global_var('func_6307')
var_7280 = relay.var("var_7280", dtype = "float64", shape = (720,))#candidate|7280|(720,)|var|float64
call_7279 = relay.TupleGetItem(func_6303_call(relay.reshape(const_7275.astype('int8'), [756,]), relay.reshape(var_7280.astype('float64'), [720,]), relay.reshape(call_7235.astype('int8'), [24, 12]), ), 4)
call_7281 = relay.TupleGetItem(func_6307_call(relay.reshape(const_7275.astype('int8'), [756,]), relay.reshape(var_7280.astype('float64'), [720,]), relay.reshape(call_7235.astype('int8'), [24, 12]), ), 4)
output = relay.Tuple([call_7192,var_7217,call_7219,const_7220,call_7235,var_7236,var_7237,const_7238,uop_7252,call_7273,var_7274,const_7275,call_7279,var_7280,])
output2 = relay.Tuple([call_7193,var_7217,call_7221,const_7220,call_7239,var_7236,var_7237,const_7238,uop_7254,call_7276,var_7274,const_7275,call_7281,var_7280,])
func_7297 = relay.Function([var_7217,var_7236,var_7237,var_7274,var_7280,], output)
mod['func_7297'] = func_7297
mod = relay.transform.InferType()(mod)
mutated_mod['func_7297'] = func_7297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7297_call = mutated_mod.get_global_var('func_7297')
var_7299 = relay.var("var_7299", dtype = "float64", shape = (1404,))#candidate|7299|(1404,)|var|float64
var_7300 = relay.var("var_7300", dtype = "int32", shape = (30, 2))#candidate|7300|(30, 2)|var|int32
var_7301 = relay.var("var_7301", dtype = "float32", shape = (8, 60))#candidate|7301|(8, 60)|var|float32
var_7302 = relay.var("var_7302", dtype = "float64", shape = (252,))#candidate|7302|(252,)|var|float64
var_7303 = relay.var("var_7303", dtype = "float64", shape = (720,))#candidate|7303|(720,)|var|float64
call_7298 = func_7297_call(var_7299,var_7300,var_7301,var_7302,var_7303,)
output = call_7298
func_7304 = relay.Function([var_7299,var_7300,var_7301,var_7302,var_7303,], output)
mutated_mod['func_7304'] = func_7304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6154_call = mod.get_global_var('func_6154')
func_6156_call = mutated_mod.get_global_var('func_6156')
call_7311 = relay.TupleGetItem(func_6154_call(), 0)
call_7312 = relay.TupleGetItem(func_6156_call(), 0)
func_6808_call = mod.get_global_var('func_6808')
func_6811_call = mutated_mod.get_global_var('func_6811')
const_7321 = relay.const([True,False,True,True,False,False,True,True,False,False,False,False,True,False,False,False,True,True,False,False,True,True,True,True,True,False,False,False,True,False,False,False,True,False,False,True,False,True,True,False,True,True,False,False,True,False,False,False,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,False,False,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,False,False,False,False,False,False,True,False,True,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,False,True,False,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,True,True,False,True,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,True,False,True,True,True,False,True,True,True,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,False,True,False,False,False,True,True,False,True,True,True,False,False,False,True,True,True,False,False,False,True,True,False,False,True,True,True,True,False,True,True,False,False,False,False,False,True,True,True,True,False,False,True,False,False,False,False,True,False,False,True,True,True,False,True,False,True,True,True,True,False,True,True,False,True,True,False,False,False,True,True,True,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,False,False,False,False,False,True,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,True,True,False,True,False,True,True,True,False,False,True,False,True,True,False,False,True,False,True,False,True,False,True,True,False,False,False,True,False,False,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,False,False,True,False,True,True,True,False,True,True,True,True,True,True,False,True,False], dtype = "bool")#candidate|7321|(351,)|const|bool
var_7322 = relay.var("var_7322", dtype = "int8", shape = (18, 42))#candidate|7322|(18, 42)|var|int8
call_7320 = relay.TupleGetItem(func_6808_call(relay.reshape(const_7321.astype('bool'), [9, 3, 13]), relay.reshape(var_7322.astype('int8'), [756,]), ), 0)
call_7323 = relay.TupleGetItem(func_6811_call(relay.reshape(const_7321.astype('bool'), [9, 3, 13]), relay.reshape(var_7322.astype('int8'), [756,]), ), 0)
output = relay.Tuple([call_7311,call_7320,const_7321,var_7322,])
output2 = relay.Tuple([call_7312,call_7323,const_7321,var_7322,])
func_7364 = relay.Function([var_7322,], output)
mod['func_7364'] = func_7364
mod = relay.transform.InferType()(mod)
var_7365 = relay.var("var_7365", dtype = "int8", shape = (18, 42))#candidate|7365|(18, 42)|var|int8
output = func_7364(var_7365)
func_7366 = relay.Function([var_7365], output)
mutated_mod['func_7366'] = func_7366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6480_call = mod.get_global_var('func_6480')
func_6482_call = mutated_mod.get_global_var('func_6482')
call_7403 = relay.TupleGetItem(func_6480_call(), 1)
call_7404 = relay.TupleGetItem(func_6482_call(), 1)
output = call_7403
output2 = call_7404
func_7406 = relay.Function([], output)
mod['func_7406'] = func_7406
mod = relay.transform.InferType()(mod)
output = func_7406()
func_7407 = relay.Function([], output)
mutated_mod['func_7407'] = func_7407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7162_call = mod.get_global_var('func_7162')
func_7163_call = mutated_mod.get_global_var('func_7163')
call_7424 = func_7162_call()
call_7425 = func_7162_call()
output = relay.Tuple([call_7424,])
output2 = relay.Tuple([call_7425,])
func_7441 = relay.Function([], output)
mod['func_7441'] = func_7441
mod = relay.transform.InferType()(mod)
output = func_7441()
func_7442 = relay.Function([], output)
mutated_mod['func_7442'] = func_7442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7406_call = mod.get_global_var('func_7406')
func_7407_call = mutated_mod.get_global_var('func_7407')
call_7484 = func_7406_call()
call_7485 = func_7406_call()
const_7498 = relay.const([[[1,-2],[-9,8],[-10,-9],[8,1],[8,3],[-8,7],[-8,-7],[1,3],[-9,-2],[-1,-10],[-5,-3],[8,10]],[[6,5],[-8,-1],[7,-5],[3,-10],[-5,3],[-3,9],[1,3],[-10,3],[-6,-9],[5,1],[8,-10],[-6,-3]],[[3,8],[-6,3],[9,-5],[9,-2],[-10,-9],[10,7],[-6,7],[7,4],[4,5],[-7,9],[4,-4],[4,8]],[[-8,9],[7,-6],[-4,8],[4,3],[-1,10],[-7,-5],[-3,-4],[8,10],[-10,-4],[6,-3],[-2,2],[-2,4]],[[3,3],[-2,-3],[-7,1],[2,1],[-10,-1],[4,9],[-5,-4],[7,-10],[5,-2],[-2,-4],[-5,-6],[6,-1]],[[2,-7],[5,6],[6,-9],[-1,3],[2,5],[-4,3],[-3,8],[-6,-10],[-10,7],[-2,7],[7,10],[5,-6]]], dtype = "int32")#candidate|7498|(6, 12, 2)|const|int32
bop_7499 = relay.add(call_7484.astype('uint8'), relay.reshape(const_7498.astype('uint8'), relay.shape_of(call_7484))) # shape=(6, 12, 2)
bop_7502 = relay.add(call_7485.astype('uint8'), relay.reshape(const_7498.astype('uint8'), relay.shape_of(call_7485))) # shape=(6, 12, 2)
output = relay.Tuple([bop_7499,])
output2 = relay.Tuple([bop_7502,])
func_7507 = relay.Function([], output)
mod['func_7507'] = func_7507
mod = relay.transform.InferType()(mod)
mutated_mod['func_7507'] = func_7507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7507_call = mutated_mod.get_global_var('func_7507')
call_7508 = func_7507_call()
output = call_7508
func_7509 = relay.Function([], output)
mutated_mod['func_7509'] = func_7509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5512_call = mod.get_global_var('func_5512')
func_5513_call = mutated_mod.get_global_var('func_5513')
call_7545 = func_5512_call()
call_7546 = func_5512_call()
output = call_7545
output2 = call_7546
func_7551 = relay.Function([], output)
mod['func_7551'] = func_7551
mod = relay.transform.InferType()(mod)
output = func_7551()
func_7552 = relay.Function([], output)
mutated_mod['func_7552'] = func_7552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6644_call = mod.get_global_var('func_6644')
func_6645_call = mutated_mod.get_global_var('func_6645')
call_7582 = relay.TupleGetItem(func_6644_call(), 0)
call_7583 = relay.TupleGetItem(func_6645_call(), 0)
func_7364_call = mod.get_global_var('func_7364')
func_7366_call = mutated_mod.get_global_var('func_7366')
const_7588 = relay.const([6,-3,-7,9,-3,8,-8,4,-1,-10,8,9,-9,-4,-3,-2,8,-3,2,-9,-9,-4,5,7,-2,-3,7,6,8,-4,-10,7,4,3,3,3,-10,3,7,-1,4,-3,-9,-8,-6,7,1,-4,-5,-2,-10,4,-2,-5,-6,-1,-4,3,1,10,4,-5,-1,-9,-7,-9,-6,7,10,10,-10,-8,5,-10,5,-8,-7,-3,2,-7,4,6,-8,9,-4,-8,10,-1,-9,3,-10,4,-4,6,-10,-4,8,6,2,-8,4,1,1,-9,2,6,-3,-9,-9,2,7,-6,8,5,-7,4,-6,-7,8,9,10,-2,-6,-7,-6,-6,4,2,-6,-2,9,-6,3,-3,-9,-1,-8,1,5,-2,-6,-6,10,4,4,-9,-4,-7,8,9,2,8,4,7,7,10,8,6,5,-4,-6,3,9,8,-2,9,-7,-8,-6,10,-6,7,-8,2,2,4,10,-9,-9,-8,-2,-7,-4,9,1,3,10,1,-2,-3,8,4,5,9,-8,5,6,10,8,-1,-9,-6,6,-8,10,-5,-9,8,-4,-7,6,4,-5,-5,2,-2,2,-3,-7,1,2,-6,6,-4,3,-3,-3,-4,-1,-1,-4,-7,5,9,1,-7,-7,-6,9,5,3,-2,7,7,4,3,5,6,-10,-9,-6,-3,-1,10,-1,1,-5,4,-10,3,1,2,8,3,7,-8,-10,8,2,-1,-4,-8,-7,4,3,1,-3,-9,5,8,6,4,7,-7,-1,3,-1,6,-5,-9,-8,-2,5,4,5,-1,8,-9,9,-5,2,-10,10,5,6,4,4,7,-1,-9,-2,9,8,-6,-2,1,-10,-1,7,-8,9,9,1,-5,4,1,6,8,8,3,7,-7,3,9,-5,-4,-2,10,-6,6,-10,-8,6,2,-9,5,-7,5,10,1,-5,-10,6,10,6,4,2,-4,-9,4,1,6,-10,9,6,-5,-5,-8,4,4,4,8,3,8,-10,10,10,1,-8,1,-2,-7,-9,1,2,3,-7,-6,5,-10,4,6,7,-5,-10,1,1,3,2,5,-1,-2,9,7,-9,9,-9,9,-4,1,3,10,-1,-5,-6,6,9,4,-5,-2,-9,10,-5,4,-5,5,-8,-1,-7,1,-7,1,-7,3,-7,8,5,-2,9,2,-2,4,-4,-8,-1,4,-7,3,-1,6,1,-4,4,-1,-3,-8,1,-4,7,6,2,-8,-7,3,-9,-10,4,9,1,10,-4,-10,2,-2,7,-1,-1,5,1,-10,6,-3,3,8,-3,-9,-1,-3,-2,-4,-6,5,5,7,-10,8,-4,-6,-2,-2,-3,1,-9,-6,3,9,6,-9,6,9,-3,-1,10,6,10,-7,9,8,6,9,8,9,2,7,5,3,4,7,-9,-6,-2,-5,-2,-9,9,-8,-5,-10,-6,-6,-4,-9,1,2,10,3,2,-5,1,3,-1,8,7,-5,-5,-1,10,-7,5,-2,-9,7,3,6,-5,7,-7,3,2,-6,-1,-6,-9,1,-4,9,10,-3,-9,10,-7,1,1,-9,-4,-2,3,5,10,-6,-10,8,-2,-4,9,4,-10,-1,10,4,4,-8,-3,-1,-8,-9,-1,-8,-9,5,-4,-3,5,-5,-5,-9,-6,-8,-10,4,-5,6,-2,-2,-5,-9,7,3,-10,-6,-9,4,2,4,10,-1,3,-2,10,-7,2,-5,-10,10,9,2,1,-1,7,-6,-3,3,-4,2,2,10,5,-10,6,-6,-6,-2,4,3,-9,2,7,10,4,-5,3,-8,-3,-5,10,1,-10,4,-6,-9,5,-9,-9,-4,-4,9,6,-6,-8,5,4,4,1,-10,-7,4,-10,-6,5,-4,-1,-4,10,6,-5,-6,1,5,-1,8,5,10,6,-6,6,-8,1,-3,-6,-1,-2,-1,8,-4,10,7,-6,3,-2,1,-9,6,2,2,-10,10,9,-4,7,8,-2,5,3,-9,6,-5,-10,-4,-2,-2,-9,-4,-6,-7,-8,2], dtype = "int8")#candidate|7588|(756,)|const|int8
call_7587 = relay.TupleGetItem(func_7364_call(relay.reshape(const_7588.astype('int8'), [18, 42])), 1)
call_7589 = relay.TupleGetItem(func_7366_call(relay.reshape(const_7588.astype('int8'), [18, 42])), 1)
var_7606 = relay.var("var_7606", dtype = "int8", shape = (756,))#candidate|7606|(756,)|var|int8
bop_7607 = relay.add(const_7588.astype('float64'), relay.reshape(var_7606.astype('float64'), relay.shape_of(const_7588))) # shape=(756,)
output = relay.Tuple([call_7582,call_7587,bop_7607,])
output2 = relay.Tuple([call_7583,call_7589,bop_7607,])
func_7610 = relay.Function([var_7606,], output)
mod['func_7610'] = func_7610
mod = relay.transform.InferType()(mod)
var_7611 = relay.var("var_7611", dtype = "int8", shape = (756,))#candidate|7611|(756,)|var|int8
output = func_7610(var_7611)
func_7612 = relay.Function([var_7611], output)
mutated_mod['func_7612'] = func_7612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7507_call = mod.get_global_var('func_7507')
func_7509_call = mutated_mod.get_global_var('func_7509')
call_7627 = relay.TupleGetItem(func_7507_call(), 0)
call_7628 = relay.TupleGetItem(func_7509_call(), 0)
func_7162_call = mod.get_global_var('func_7162')
func_7163_call = mutated_mod.get_global_var('func_7163')
call_7634 = func_7162_call()
call_7635 = func_7162_call()
output = relay.Tuple([call_7627,call_7634,])
output2 = relay.Tuple([call_7628,call_7635,])
func_7637 = relay.Function([], output)
mod['func_7637'] = func_7637
mod = relay.transform.InferType()(mod)
mutated_mod['func_7637'] = func_7637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7637_call = mutated_mod.get_global_var('func_7637')
call_7638 = func_7637_call()
output = call_7638
func_7639 = relay.Function([], output)
mutated_mod['func_7639'] = func_7639
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7679 = relay.var("var_7679", dtype = "uint16", shape = (13, 10, 10))#candidate|7679|(13, 10, 10)|var|uint16
var_7680 = relay.var("var_7680", dtype = "uint16", shape = (13, 10, 10))#candidate|7680|(13, 10, 10)|var|uint16
bop_7681 = relay.bitwise_xor(var_7679.astype('uint16'), relay.reshape(var_7680.astype('uint16'), relay.shape_of(var_7679))) # shape=(13, 10, 10)
func_5457_call = mod.get_global_var('func_5457')
func_5459_call = mutated_mod.get_global_var('func_5459')
var_7685 = relay.var("var_7685", dtype = "int8", shape = ())#candidate|7685|()|var|int8
call_7684 = func_5457_call(relay.reshape(var_7685.astype('int8'), []))
call_7686 = func_5457_call(relay.reshape(var_7685.astype('int8'), []))
uop_7691 = relay.rsqrt(call_7684.astype('float64')) # shape=(1, 3, 11)
uop_7693 = relay.rsqrt(call_7686.astype('float64')) # shape=(1, 3, 11)
func_7406_call = mod.get_global_var('func_7406')
func_7407_call = mutated_mod.get_global_var('func_7407')
call_7696 = func_7406_call()
call_7697 = func_7406_call()
uop_7724 = relay.atanh(uop_7691.astype('float32')) # shape=(1, 3, 11)
uop_7726 = relay.atanh(uop_7693.astype('float32')) # shape=(1, 3, 11)
func_1954_call = mod.get_global_var('func_1954')
func_1958_call = mutated_mod.get_global_var('func_1958')
const_7739 = relay.const([[1.014763,-2.000730,4.754707,-6.176557,5.753680,1.140787,-2.167115,6.843718,-0.183792,-2.121187,7.616165,9.616979,4.717794,-1.277259,-4.023577,-7.498320,-2.858845,9.479574,7.028154,1.911897,-5.646601,-5.995883,-5.929030,8.457543,-3.153785,2.934591,4.501901,1.653978],[2.570877,-6.938599,-6.105635,4.782360,7.584745,-3.179545,2.614120,8.127061,-2.036409,-3.913435,4.605952,8.170275,8.990693,4.374019,3.593950,2.727899,0.384496,3.143599,4.098401,-7.803675,0.858912,5.011634,-3.431820,-0.191317,-5.105682,8.425838,-8.578504,1.216518],[0.163772,-3.847540,-8.612931,8.144088,4.124875,4.691157,-0.879851,-2.510727,-5.991530,-2.829807,-6.498563,2.824427,9.486952,8.670150,1.234070,4.033827,4.936876,-9.643994,4.535555,6.695466,-9.119379,8.988479,-7.575026,-6.572619,9.409508,6.429588,-0.339237,-0.848929],[7.930456,4.229107,3.915285,3.929338,8.905731,-2.458924,-7.243517,9.430026,-8.824336,3.467241,-9.485591,5.788590,-3.368889,-5.210620,1.793913,-5.540039,-3.762134,5.980462,-8.913667,-3.902599,-6.356394,-0.883006,8.293293,5.488716,6.639593,-8.563079,3.783163,0.116750],[2.059193,-8.787111,1.871408,0.292447,-5.727115,8.900256,-0.798687,-3.273353,-3.392749,8.863157,7.284358,9.574508,9.561503,-6.787465,8.553946,-7.869270,3.676664,8.277336,4.939299,-9.549077,9.374366,-9.215396,-3.963646,5.408486,8.599438,-1.340818,1.913588,8.513057]], dtype = "float32")#candidate|7739|(5, 28)|const|float32
call_7738 = relay.TupleGetItem(func_1954_call(relay.reshape(const_7739.astype('float32'), [4, 5, 7]), relay.reshape(const_7739.astype('float32'), [4, 5, 7]), ), 3)
call_7740 = relay.TupleGetItem(func_1958_call(relay.reshape(const_7739.astype('float32'), [4, 5, 7]), relay.reshape(const_7739.astype('float32'), [4, 5, 7]), ), 3)
output = relay.Tuple([bop_7681,var_7685,call_7696,uop_7724,call_7738,const_7739,])
output2 = relay.Tuple([bop_7681,var_7685,call_7697,uop_7726,call_7740,const_7739,])
func_7748 = relay.Function([var_7679,var_7680,var_7685,], output)
mod['func_7748'] = func_7748
mod = relay.transform.InferType()(mod)
mutated_mod['func_7748'] = func_7748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7748_call = mutated_mod.get_global_var('func_7748')
var_7750 = relay.var("var_7750", dtype = "uint16", shape = (13, 10, 10))#candidate|7750|(13, 10, 10)|var|uint16
var_7751 = relay.var("var_7751", dtype = "uint16", shape = (13, 10, 10))#candidate|7751|(13, 10, 10)|var|uint16
var_7752 = relay.var("var_7752", dtype = "int8", shape = ())#candidate|7752|()|var|int8
call_7749 = func_7748_call(var_7750,var_7751,var_7752,)
output = call_7749
func_7753 = relay.Function([var_7750,var_7751,var_7752,], output)
mutated_mod['func_7753'] = func_7753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7507_call = mod.get_global_var('func_7507')
func_7509_call = mutated_mod.get_global_var('func_7509')
call_7800 = relay.TupleGetItem(func_7507_call(), 0)
call_7801 = relay.TupleGetItem(func_7509_call(), 0)
output = relay.Tuple([call_7800,])
output2 = relay.Tuple([call_7801,])
func_7805 = relay.Function([], output)
mod['func_7805'] = func_7805
mod = relay.transform.InferType()(mod)
output = func_7805()
func_7806 = relay.Function([], output)
mutated_mod['func_7806'] = func_7806
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7819 = relay.var("var_7819", dtype = "float32", shape = (1, 3, 3))#candidate|7819|(1, 3, 3)|var|float32
uop_7820 = relay.sigmoid(var_7819.astype('float32')) # shape=(1, 3, 3)
uop_7828 = relay.erf(uop_7820.astype('float32')) # shape=(1, 3, 3)
output = uop_7828
output2 = uop_7828
func_7836 = relay.Function([var_7819,], output)
mod['func_7836'] = func_7836
mod = relay.transform.InferType()(mod)
var_7837 = relay.var("var_7837", dtype = "float32", shape = (1, 3, 3))#candidate|7837|(1, 3, 3)|var|float32
output = func_7836(var_7837)
func_7838 = relay.Function([var_7837], output)
mutated_mod['func_7838'] = func_7838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5512_call = mod.get_global_var('func_5512')
func_5513_call = mutated_mod.get_global_var('func_5513')
call_7844 = func_5512_call()
call_7845 = func_5512_call()
func_7162_call = mod.get_global_var('func_7162')
func_7163_call = mutated_mod.get_global_var('func_7163')
call_7868 = func_7162_call()
call_7869 = func_7162_call()
output = relay.Tuple([call_7844,call_7868,])
output2 = relay.Tuple([call_7845,call_7869,])
func_7870 = relay.Function([], output)
mod['func_7870'] = func_7870
mod = relay.transform.InferType()(mod)
output = func_7870()
func_7871 = relay.Function([], output)
mutated_mod['func_7871'] = func_7871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7805_call = mod.get_global_var('func_7805')
func_7806_call = mutated_mod.get_global_var('func_7806')
call_7900 = relay.TupleGetItem(func_7805_call(), 0)
call_7901 = relay.TupleGetItem(func_7806_call(), 0)
var_7902 = relay.var("var_7902", dtype = "uint8", shape = (6, 12, 2))#candidate|7902|(6, 12, 2)|var|uint8
bop_7903 = relay.power(call_7900.astype('float32'), relay.reshape(var_7902.astype('float32'), relay.shape_of(call_7900))) # shape=(6, 12, 2)
bop_7906 = relay.power(call_7901.astype('float32'), relay.reshape(var_7902.astype('float32'), relay.shape_of(call_7901))) # shape=(6, 12, 2)
uop_7908 = relay.sigmoid(call_7900.astype('float32')) # shape=(6, 12, 2)
uop_7910 = relay.sigmoid(call_7901.astype('float32')) # shape=(6, 12, 2)
output = relay.Tuple([bop_7903,uop_7908,])
output2 = relay.Tuple([bop_7906,uop_7910,])
func_7912 = relay.Function([var_7902,], output)
mod['func_7912'] = func_7912
mod = relay.transform.InferType()(mod)
var_7913 = relay.var("var_7913", dtype = "uint8", shape = (6, 12, 2))#candidate|7913|(6, 12, 2)|var|uint8
output = func_7912(var_7913)
func_7914 = relay.Function([var_7913], output)
mutated_mod['func_7914'] = func_7914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6551_call = mod.get_global_var('func_6551')
func_6552_call = mutated_mod.get_global_var('func_6552')
call_7921 = relay.TupleGetItem(func_6551_call(), 1)
call_7922 = relay.TupleGetItem(func_6552_call(), 1)
output = relay.Tuple([call_7921,])
output2 = relay.Tuple([call_7922,])
func_7941 = relay.Function([], output)
mod['func_7941'] = func_7941
mod = relay.transform.InferType()(mod)
output = func_7941()
func_7942 = relay.Function([], output)
mutated_mod['func_7942'] = func_7942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5512_call = mod.get_global_var('func_5512')
func_5513_call = mutated_mod.get_global_var('func_5513')
call_7945 = func_5512_call()
call_7946 = func_5512_call()
output = call_7945
output2 = call_7946
func_7952 = relay.Function([], output)
mod['func_7952'] = func_7952
mod = relay.transform.InferType()(mod)
output = func_7952()
func_7953 = relay.Function([], output)
mutated_mod['func_7953'] = func_7953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7441_call = mod.get_global_var('func_7441')
func_7442_call = mutated_mod.get_global_var('func_7442')
call_7979 = relay.TupleGetItem(func_7441_call(), 0)
call_7980 = relay.TupleGetItem(func_7442_call(), 0)
const_7992 = relay.const([[[-7,1],[3,-9],[5,-3],[-3,-8],[-1,-7],[-9,-5],[1,-3],[10,-8],[10,-10],[-7,7],[-7,2],[-3,4]],[[7,2],[-4,-6],[6,3],[-9,-2],[2,-1],[1,9],[-10,-9],[-3,-6],[-6,6],[-5,6],[-2,-7],[2,1]],[[3,1],[1,1],[2,4],[-3,-8],[1,1],[-8,9],[-6,10],[-10,-9],[2,9],[3,7],[-10,-3],[-5,3]],[[4,-4],[-1,-10],[-3,-2],[-3,8],[-3,1],[6,1],[10,10],[2,-1],[-9,9],[-2,-6],[1,-8],[9,2]],[[-2,9],[-2,4],[4,-7],[-1,-3],[5,-10],[-2,2],[4,-10],[5,-8],[4,2],[6,7],[-2,-6],[-3,3]],[[4,-7],[-10,10],[8,-9],[-1,-9],[-2,10],[-9,-10],[9,3],[-7,-4],[-10,7],[-1,-3],[8,-3],[9,-3]]], dtype = "int32")#candidate|7992|(6, 12, 2)|const|int32
bop_7993 = relay.logical_or(call_7979.astype('bool'), relay.reshape(const_7992.astype('bool'), relay.shape_of(call_7979))) # shape=(6, 12, 2)
bop_7996 = relay.logical_or(call_7980.astype('bool'), relay.reshape(const_7992.astype('bool'), relay.shape_of(call_7980))) # shape=(6, 12, 2)
func_6480_call = mod.get_global_var('func_6480')
func_6482_call = mutated_mod.get_global_var('func_6482')
call_8022 = relay.TupleGetItem(func_6480_call(), 0)
call_8023 = relay.TupleGetItem(func_6482_call(), 0)
func_7145_call = mod.get_global_var('func_7145')
func_7147_call = mutated_mod.get_global_var('func_7147')
var_8032 = relay.var("var_8032", dtype = "float64", shape = (1404,))#candidate|8032|(1404,)|var|float64
call_8031 = relay.TupleGetItem(func_7145_call(relay.reshape(var_8032.astype('float64'), [9, 12, 13])), 1)
call_8033 = relay.TupleGetItem(func_7147_call(relay.reshape(var_8032.astype('float64'), [9, 12, 13])), 1)
output = relay.Tuple([bop_7993,call_8022,call_8031,var_8032,])
output2 = relay.Tuple([bop_7996,call_8023,call_8033,var_8032,])
func_8036 = relay.Function([var_8032,], output)
mod['func_8036'] = func_8036
mod = relay.transform.InferType()(mod)
var_8037 = relay.var("var_8037", dtype = "float64", shape = (1404,))#candidate|8037|(1404,)|var|float64
output = func_8036(var_8037)
func_8038 = relay.Function([var_8037], output)
mutated_mod['func_8038'] = func_8038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6910_call = mod.get_global_var('func_6910')
func_6911_call = mutated_mod.get_global_var('func_6911')
call_8049 = relay.TupleGetItem(func_6910_call(), 0)
call_8050 = relay.TupleGetItem(func_6911_call(), 0)
output = relay.Tuple([call_8049,])
output2 = relay.Tuple([call_8050,])
func_8053 = relay.Function([], output)
mod['func_8053'] = func_8053
mod = relay.transform.InferType()(mod)
output = func_8053()
func_8054 = relay.Function([], output)
mutated_mod['func_8054'] = func_8054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7551_call = mod.get_global_var('func_7551')
func_7552_call = mutated_mod.get_global_var('func_7552')
call_8068 = func_7551_call()
call_8069 = func_7551_call()
func_6551_call = mod.get_global_var('func_6551')
func_6552_call = mutated_mod.get_global_var('func_6552')
call_8078 = relay.TupleGetItem(func_6551_call(), 1)
call_8079 = relay.TupleGetItem(func_6552_call(), 1)
func_6765_call = mod.get_global_var('func_6765')
func_6770_call = mutated_mod.get_global_var('func_6770')
const_8088 = relay.const([[7.217763,-8.811575,5.422777,7.269917,-8.091727,-3.257800,-6.657670,4.795582,-4.632540,-4.709817,7.788545,1.593267,1.395008,9.377526,-2.646432,-1.134585,-7.502119,2.424146,-7.002685,-8.112089,-3.619476,-5.202447,0.325919,-0.577402,0.294047,-4.272623,-3.062058,-1.036166,9.968745,-2.901897,-3.992924,0.966897,2.126498,-0.819961,3.649216,-9.584490,-5.830027,-7.091590,-3.794699,8.924307,6.786814,-2.726587],[1.081563,-7.126750,-3.246585,-7.476769,5.157454,6.625914,4.844080,-3.351332,-6.010600,-8.040054,-9.412888,-5.058168,3.221716,-5.223440,-8.349223,-3.380862,0.168812,-0.607074,4.267444,-9.082677,-5.109785,8.333709,-6.005859,5.408178,-1.070685,8.324651,-6.719596,4.724803,9.076880,1.536444,-1.518077,9.617744,-7.081197,3.211480,2.453449,-8.473334,4.021345,7.283631,-1.709843,2.180043,-4.942319,4.536960],[-2.435514,-1.634059,-4.203939,9.170410,5.733179,-3.469957,-8.166429,-5.367314,9.816425,-8.695906,-2.861526,-0.375331,-0.872435,-8.487774,-4.685397,5.984886,-4.579815,-3.878569,4.863266,-7.778437,7.564314,-3.045456,-4.508179,8.147453,-4.487037,2.718419,9.617407,1.410158,2.668146,-7.586941,6.101867,-5.189517,6.431469,-1.990816,7.091129,7.519978,6.815730,-1.371748,-9.328922,3.044790,0.104186,-9.822791],[4.047293,-8.342495,6.677152,-8.888532,7.541302,-7.270763,-3.118848,3.669377,1.779881,-9.569701,4.703310,5.562395,-7.622808,-6.399441,0.898861,-8.340325,-8.372529,4.511115,6.009821,-1.732088,-2.920920,8.800461,4.924707,-9.815827,6.428398,6.351988,-4.961876,5.776499,8.990606,-2.766714,-9.273854,0.495762,-0.577587,-1.247817,3.755155,-5.183383,2.445168,-7.509405,-6.392009,-2.374881,3.647636,-8.730058],[-8.325000,-6.079379,7.603667,-1.288924,1.127130,-9.852827,-2.861693,2.991809,8.934054,5.875350,8.123159,3.748852,3.460324,1.251335,7.506574,-5.338530,0.579872,-4.382656,3.751715,-3.525647,-4.421310,-3.376234,3.589083,-9.726776,7.424174,-1.418213,1.183855,9.580036,4.078318,3.049948,-1.875574,-6.765559,-6.458015,4.466389,3.797487,-4.078950,-4.353813,-6.782298,-2.717810,6.897698,-4.588877,-2.009188]], dtype = "float64")#candidate|8088|(5, 42)|const|float64
const_8089 = relay.const([[4,1],[8,2],[-3,-10],[-10,6],[9,6],[-9,-7],[7,8],[1,-7],[10,2],[-7,-7],[-9,-1],[5,-8],[-5,-6],[-9,1],[-6,3],[1,-6],[-10,-10],[-5,7],[-4,-2],[-6,-5],[7,7],[-6,-3],[-9,2],[6,4],[8,-3],[1,-8],[-8,5],[-1,7],[2,3],[2,2],[2,-5],[6,4],[-1,9],[-7,-6],[7,1],[2,5],[1,3],[4,9],[1,-4],[-3,-1],[5,8],[-6,9],[8,1],[-7,5],[4,3],[5,-6],[6,-5],[10,3],[7,9],[6,9],[7,5],[6,-4],[-1,-2],[1,-5],[10,5],[-8,-5],[-2,8],[-4,3],[9,-7],[-9,7],[10,-6],[-9,-7],[3,-9],[2,5],[10,-1],[2,-6],[-3,6],[-4,2],[2,6],[-3,10],[-4,-6],[-5,-10],[6,-7],[-5,-9],[-8,2],[8,7],[-4,-3],[5,-2],[2,-7],[8,-2],[-9,3],[4,4],[-7,-3],[10,6],[2,-10],[3,-5],[-9,2],[10,-2],[-4,2],[-6,-7],[3,-7],[9,-7],[-3,7],[-1,2],[5,-7],[-9,1],[-5,1],[-1,4],[10,9],[7,2],[2,-7],[-2,-3],[7,9],[1,1],[-4,7],[3,-1],[5,4],[-5,1],[4,2],[-8,-2],[-7,3],[2,5],[-8,-3],[-6,-4],[6,2],[-4,3],[-2,5],[-2,-7],[7,-10],[-5,5],[9,-2],[4,-5],[-6,4],[-1,-8],[-1,-3],[10,-1],[-1,8],[-8,-9],[2,-2],[-9,-7],[-6,-5],[-7,10],[-7,-1],[2,-6],[5,-8],[6,7],[-1,4],[-10,5],[1,2],[2,-6],[-4,6],[10,-8],[-7,-7],[-8,-10],[-5,-8],[-5,-10],[-2,6],[6,-5],[-10,-6],[-4,-5],[-5,-3],[-7,1],[-7,-9],[-4,1],[-5,2],[-1,-2],[9,-3],[-6,-5],[3,3],[2,5],[3,-4],[-5,2],[3,1],[-2,-9],[5,-5],[2,-2],[-9,6],[9,3],[-5,8],[3,10],[-4,2],[-8,-7],[4,-1],[-2,-1],[8,-4],[-1,10],[7,6],[7,-8],[10,7],[4,8],[7,-2],[4,2],[5,10],[7,1],[-7,-6],[4,-5],[7,-2],[-7,-6],[-2,5],[-6,-10],[5,4],[-10,-5],[-2,1],[-6,-4],[-10,3],[9,-4],[-10,8],[6,-4],[8,4],[-4,8],[2,4],[8,1],[4,-7],[-3,-3],[2,8],[9,-8],[1,8],[-10,1],[-6,10],[-5,-1],[-6,4],[-1,-4],[-10,10],[4,8],[-1,9],[1,-3],[-7,10],[-7,2],[1,-7],[-3,-5],[3,2],[-3,-1],[7,6],[-9,6],[6,-7],[8,8],[-5,2],[-6,-9],[-10,4],[-1,10],[6,5],[-6,3],[-6,-7],[-2,-4],[2,5],[2,-6],[-4,8],[9,5],[-5,-1],[3,5],[6,6],[8,5],[5,-7],[3,-9],[-6,-4],[8,-10],[-2,-4],[-7,-4],[10,1],[9,6],[-3,1],[8,4],[-9,-9],[-10,10],[2,-6],[-2,9],[10,9],[-5,1],[8,5],[4,-2],[-10,9],[-9,-1],[-2,7],[-7,5],[-6,7],[9,-9],[-2,5],[-4,8],[-7,3],[8,9],[2,6],[-4,-9],[5,-4],[-5,-5],[9,-2],[8,-8],[-9,-3],[6,-6],[9,8],[-5,6],[2,-6],[6,2],[3,10],[-6,-6],[-7,9],[-2,2],[9,7],[-6,3],[4,4],[3,5],[2,7],[2,-10],[-4,-4],[7,10],[-5,-9],[-9,-10],[-4,-2],[10,4],[3,-9],[-7,-7],[9,-9],[-7,-2],[5,5],[4,8],[-10,6],[8,-4],[-3,7],[4,-3],[5,-9],[3,7],[3,-4],[9,-8],[2,1],[-5,-2],[-7,-6],[-5,4],[-3,2],[-6,-5],[-3,7],[-3,-1],[8,5],[-6,-10],[8,-6],[7,2],[-4,-7],[5,9],[-1,10],[-9,8],[-2,1],[-2,2],[8,-4],[7,6],[-10,4],[-3,3],[-9,-9],[-3,-8],[-10,6],[-9,-3],[-6,4],[2,-7],[-3,8],[-3,-1],[4,-3],[-6,6],[1,9],[10,-8],[10,-2],[-4,-3],[-1,2],[-1,-8],[-2,6],[3,6],[-3,3],[1,-2],[5,-1],[4,-3],[-6,2],[-7,-6],[3,-9],[-3,-10],[3,10],[7,3],[5,-1],[2,7],[-1,7],[9,-9],[5,-9],[-6,-5],[-4,-3],[6,-5],[1,-1],[1,1],[4,2],[-3,-6],[-2,7],[5,8],[-6,4],[-6,10]], dtype = "int8")#candidate|8089|(378, 2)|const|int8
var_8090 = relay.var("var_8090", dtype = "float64", shape = (3, 84))#candidate|8090|(3, 84)|var|float64
call_8087 = relay.TupleGetItem(func_6765_call(relay.reshape(const_8088.astype('float64'), [14, 15, 1]), relay.reshape(const_8089.astype('int8'), [9, 84]), relay.reshape(var_8090.astype('float64'), [252,]), ), 5)
call_8091 = relay.TupleGetItem(func_6770_call(relay.reshape(const_8088.astype('float64'), [14, 15, 1]), relay.reshape(const_8089.astype('int8'), [9, 84]), relay.reshape(var_8090.astype('float64'), [252,]), ), 5)
output = relay.Tuple([call_8068,call_8078,call_8087,const_8088,const_8089,var_8090,])
output2 = relay.Tuple([call_8069,call_8079,call_8091,const_8088,const_8089,var_8090,])
func_8109 = relay.Function([var_8090,], output)
mod['func_8109'] = func_8109
mod = relay.transform.InferType()(mod)
mutated_mod['func_8109'] = func_8109
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8110 = relay.var("var_8110", dtype = "float64", shape = (3, 84))#candidate|8110|(3, 84)|var|float64
func_8109_call = mutated_mod.get_global_var('func_8109')
call_8111 = func_8109_call(var_8110)
output = call_8111
func_8112 = relay.Function([var_8110], output)
mutated_mod['func_8112'] = func_8112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7551_call = mod.get_global_var('func_7551')
func_7552_call = mutated_mod.get_global_var('func_7552')
call_8210 = func_7551_call()
call_8211 = func_7551_call()
func_1144_call = mod.get_global_var('func_1144')
func_1147_call = mutated_mod.get_global_var('func_1147')
const_8215 = relay.const([3.623343,6.005856,-9.305372,8.321798,0.187521,5.728735,7.727971,1.134092,3.877592,1.142028,-2.747727,-7.920573,1.971703,-0.175231,-6.343843,4.129499,9.997234,-9.283971,-5.008253,4.311846,-1.779097,-8.411840,2.422772,-4.850349,-6.385528,9.824160,2.882976,6.052418,0.179312,-5.934636,3.774062,6.689847,-7.448663,2.848847,2.676749,8.179596,7.623368,4.139903,4.429484,9.348666,4.395118,-3.544738,5.792568,-3.995048,4.133577,-7.548264,-9.425050,-0.239840,3.025864,1.257399,-1.086278,3.503226,-3.650871,-6.173691,-0.765547,2.107709,-4.853238,-5.152337,1.413825,-2.733204,4.700147,-9.493119,-0.075341,5.908475,-1.749552,-6.888369,2.215088,-4.952286,-3.648434,0.235636,8.913564,-4.500013,-3.477971,3.577168,0.317164,-5.877212,-7.013929,-5.403185,0.170879,3.956484,-1.829264,-2.544702,3.630292,1.461520,5.695024,-9.783758,-2.755828,-5.000402,2.512714,-3.937929,3.965971,-9.316413,7.038518,-7.415389,-1.357668,-7.160516,0.769562,-6.935159,-0.954821,-4.605335,-0.730818,-1.197656,-6.745110,5.865231,-2.459128,-8.438769,-5.174916,6.643665,-6.765906,6.525330,1.046133,1.610770,-1.877021,0.004368,-5.009867,0.671885,-9.559403,6.309210,-0.557303,2.593479,-8.412477,8.166980,-8.208081,2.305817,-8.382412,6.601067,-1.129377,5.627967,-4.015611,5.183374,-2.672461,0.529403,-0.695350,2.440462,1.119260,5.032631,2.386432,-0.777184,-5.801309,-5.643235,-6.043989,-0.143389,-3.783455,-4.060792,7.943615,0.250795,-7.314688,-0.772290,4.727516,8.844063,-0.822625,0.571359,9.713157,8.895888,2.253314,3.231228,2.477694,-3.715189,0.866590,-9.399279,0.664289,-1.457749,-7.725977,-3.885220,9.218507,-8.550616,7.008420,3.378262,-8.210435,-6.861602,-9.636408,0.825217,2.239095,5.902287,-6.490291,4.914522,-1.804657,5.508571,9.929133,-5.803454,-4.960864,-0.561084,-1.951403,-7.032015,8.076342,-9.803449,-0.043788,2.723316,-5.931066,-1.696717,0.840009,-6.098026], dtype = "float64")#candidate|8215|(192,)|const|float64
call_8214 = func_1144_call(relay.reshape(const_8215.astype('float64'), [3, 4, 16]))
call_8216 = func_1144_call(relay.reshape(const_8215.astype('float64'), [3, 4, 16]))
func_206_call = mod.get_global_var('func_206')
func_210_call = mutated_mod.get_global_var('func_210')
var_8227 = relay.var("var_8227", dtype = "uint8", shape = (378,))#candidate|8227|(378,)|var|uint8
var_8228 = relay.var("var_8228", dtype = "int32", shape = (60, 1))#candidate|8228|(60, 1)|var|int32
call_8226 = relay.TupleGetItem(func_206_call(relay.reshape(var_8227.astype('uint8'), [3, 9, 14]), relay.reshape(var_8228.astype('int32'), [3, 2, 10]), ), 3)
call_8229 = relay.TupleGetItem(func_210_call(relay.reshape(var_8227.astype('uint8'), [3, 9, 14]), relay.reshape(var_8228.astype('int32'), [3, 2, 10]), ), 3)
func_2936_call = mod.get_global_var('func_2936')
func_2940_call = mutated_mod.get_global_var('func_2940')
const_8232 = relay.const([9,2,-6,-2,-2,-10,-7,3,6,7,-10,-5,5,8,-9,8,-8,-7,-9,-5,6,-5,8,-5,9,6,-4,-4,6,6,9,-3,-6,-1,-1,-9,-6,10,-2,8,10,1,-4,-4,7,8,-5,2,1,-10,4,9,-4,3,5,-9,7,8,5,4,1,-7,-2,2,6,6,-1,-9,-6,-5,6,-6,4,-6,8,-10,-1,7,-7,7,-1,3,-9,-1,5,-6,9,-7,7,-9,-3,-4,-7,-8,-2,-8,-9,6,-1,1,-2,10,10,-4,1,2,4,10,10,8,4,-4,-4,9,9,5,8,3,-1,4,10,-5,5,8,5,7,9,-2,-4,-2,2,4,-3,9,4,5,1,-10,7,-2,-1,4,10,7,-9,-5,-6,-5,6,2,-7,-3,9,5,-1,-10,5,6,-2,-9,10,3,5,-7,-2,-2,-6,-7,10,2,-8,6,8,9,3,-10,4,-2,-3,-9,-6,4,-5,8,1,-9,-10,-2,-6,-8,-9,-5,6,-1,4,6,2,-3,-8,-4,-9,-10,7,1,3,2,10,6,-5,-6,8,1,1,8,-7,10,7,-6,2,-8,7,-8,9,4,10,5,4,-9,-1,6,-3,-3,6,5,-9,4,4,4,3,-7,9,-2,-7,-10,10,-6,10,-1,9,6,-10,-3,-10,6,-4,-8,-5,10,1,-10,-3,2,-6,-2,1,-2,-8,-3,-3,-4,4,-1,-2,2,-10,4,9,-9,-1,9,-8,-2,7,7,-6,8,-2,-10,-10,10,5,3,8,-8,-2,-10,1,9,9,7,-6,7,3,-4,2,-7,6,10,4,4,8,-8,-5,-6,-2,10,-9,6,6,9,6,4,5,-7,-5,-5,-4,-1,-10,3,-9,10,4,2,-9,-10,4,-6,-2,-8,-1,-10,-5,-6,-8,-9,-4,7,-8,-9,-7,-10,5,-9,-9,3,-9,-7,-6,1,1,-4,-10,4,9,5,-2,-8,10,-3,-6,1,3,-2,-10,-4,-5,-8,9,-1,5,4,-10,6,2,1,10,-3,-1,-2,10,-3,-6,7,5,4,5,-7,2,7,5,-2,-3,7,-10,6,-7,-4,-10,-6,1,4,10,3,9,6,1,8,-2,7,-4,-3,-9,-1,8,-5,9,-4,-5,1,-8,-7,-4,10,-9,-10,-7,-5,-8,9,-6,-6,8,-4,-7,-4,-3,-4,7,2,1,1,5,-8,2,2,4,3,-5,2,3,9,-10,-2,6,-2,-8,-5,-7,-9,-10,7,6,-3,-6,-5,4,4,6,8,-3,-7,3,5,6,-1,4,8,7,-3,10,-3,-3,-6,-6,-10,-7,2,-10,-10,-3,-3,-8,-7,4,-1,7,9,-4,8,1,8,5,-8,9,3,10,8,-7,-4,-6,-5,10,4,1,3,-10,-2,1,3,-9,-1,-10,-8,6,10,-8,5,-1,9,9,-5,-2,-7,6,-4,-4,-5,-6,5,-4,1,2,-9,5,4,-9,4,-6,6,-10,-7,5,-3,5,-2,3,-1,9,7,-8,-9,-9,-10,-3,7,7,10,-7,5,-2,-1,2,9,9,-5,-4,4,7,-8,-10,-6,10,3,2,1,4,-9,3,-8,-2,1,-9,-1,1,-9,-6,-10,-4,6,-10,9,1,2,4,8,5,1,-6,-10,-2,8,5,-6,10,4,3,5,1,-7,7,10,7,-6,4,10,7,5,7,-3,-7,8,-2,3,-10,8,-6,-7,-10,5,-9,3,4,-7,1,-1,-9,-8,2,2,-2,9,-1,-2,-1,6,-4,5,-6,1,4,-8,1,-4,7,-4,8,-6,10,-9,-5,-1,1,8,-2,-5,-1,1,-8,6,1,-6,-3,-8,-2,-6,-10,-5,4,-10,-2,-5,9,6,1,5,-2,-2,3,10,9,-2,2,1,1,-4,-8,8,7,5,4,3,-8,10,7,7,-5,-6,-6,-5,-10,-2,10,-4,-3,-6,-8,2,-5,7,4,9,-1,-8,-4,4,4,10,5,2,4,5,-8,-8,-1,7,7,7,-5,-4,10,10,-3,7,-8,-6,-6,6,7,-8,-7,8,-5,3,-1,-8,7,4,-10,-10,9,-3,-6,-10,-3,5,-5,5,9,-1,-6,-1,7,-5,-6,7,10,2,-1,10,1,3,8,8,-7,-8,-6,-8,-8,-9,-7,-2,8,-2,4,-2,-7,3,-6,-3,-1,-6,3,1,-6,-8,9,-9,-1,8,4,2,-7,-9,7,-6,6,-7,-7,-2,9,7,7,-6,8,4,6,-5,1,5,-5,-6,4,-10,2,-3,2,-10,5,-5,-2,7,7,10,-6,-5,6,4,5,-1,5,-9,-6,-6,-8,8,-2,-7,-8,6,-4,7,-2,-1,4,-5,8,8,4,-6,4,2,8,-4,8,10,-1,-1,-5,-10,-4,8,1,-7,7,-9,5,7,-1,-10,1,1,5,4,4,-9,-1,2,2,-8,3,1,9,1,-1,8,-1,5,-1,-5,3,5,10,9,-9,10,4,-7,-1,4,-1,5,1,7,-9,9,6,-9,5,8,-4,-3,-2,-1,3,7,8,-6,-2,-3,7,4,-9,-10,10,8,8,10,2,-5,9,-8,5,-7,1,9,-5,-1,-7,-1,-1,-9,-8,1,4,-6,-7,1,-10,-9,2,9,5,4,-3,7,1,4,-6,-1,8,-5,-4,9,5,-7,7,4,7,2,-2,3,8,3,10,-6,3,-5,6,-3,1,-9,5,10,3,2,-4,9,2,-6,5,-5,3,-5,4,-1,-7,7,8,-2,3,8,-8,-9,-8,5,9,4,-1,-1,9,2,-6,6,8,9,-3,-9,6,3,5,9,-9,-7,6,-5,-2,10,8,4,-5,7,9,-1,6,-9,4,-8,-5,-1,-1,-5,-5,-2,1,1,8,6,-6,4,-10,6,3,5,6,-10,-4,1,7,4,-9,6,5,-7,-8,4,6,-2,-3,-8,4,-6,-2,-2,2,9,-3,1,6,10,10,3,-5,4,3,6,9,-10,1,-2,-7,4,-5,-1,-6,-6,-6,-10,-6,-8,-8,6,8,-8,7,-2,10,-8,3,-7,-10,-5,4,7,2,8,-2,7,2,9,-5,6,8,-10,1,2,-2,8,-4,7,4,6,-2,8,-8,3,-7,-1,-3,8,10,-7,-4,-8,2,4,1,-6,3,-6,10,-8,-10,-1,-2,9,8,-2,-1,-3,-6,-10,7,9,-9,-4,-8,-5,-1,-3,7,5,-8,-10,-7,-3,-9,9,1,7,5,-9,4,-1,-4,8,-6,9,-9,-2,-3,1,-10,-8,-10,-10,-6,8,-7,-5,-3,4,-5,5,3,10,4,8,4,6,-10,-9,-7,6,-5,-7,-3,8,-6,-2,2,-7,-5,-10,-10,3,3,8,-10,-8,-9,-5,-5,-2,8,2,-6,-4,-5,-10,-3,6,-8,7,-3,2,9,-4,-10,9,-10,8,1,9,-8,-10,-3,-6,3,8,10,7,9,6,-8,9,-6,-4,-9,-3,-3,6,1,6,7,1,-5,-7,-2,4,-9,-7,-10,-4,-5,5,-3,-3,-5,10,4,9,10,4,2,1,2,8,3,10,2,6,-6,-10,10,3,1,-3,-10,4], dtype = "int32")#candidate|8232|(1350,)|const|int32
call_8231 = func_2936_call(relay.reshape(const_8232.astype('int32'), [15, 6, 15]), relay.reshape(const_8232.astype('int32'), [15, 6, 15]), )
call_8233 = func_2936_call(relay.reshape(const_8232.astype('int32'), [15, 6, 15]), relay.reshape(const_8232.astype('int32'), [15, 6, 15]), )
uop_8238 = relay.cosh(const_8232.astype('float32')) # shape=(1350,)
bop_8240 = relay.logical_and(uop_8238.astype('bool'), var_8228.astype('bool')) # shape=(60, 1350)
func_6218_call = mod.get_global_var('func_6218')
func_6220_call = mutated_mod.get_global_var('func_6220')
call_8243 = relay.TupleGetItem(func_6218_call(relay.reshape(call_8214.astype('float64'), [192,])), 1)
call_8244 = relay.TupleGetItem(func_6220_call(relay.reshape(call_8214.astype('float64'), [192,])), 1)
output = relay.Tuple([call_8210,call_8214,const_8215,call_8226,var_8227,call_8231,bop_8240,call_8243,])
output2 = relay.Tuple([call_8211,call_8216,const_8215,call_8229,var_8227,call_8233,bop_8240,call_8244,])
func_8245 = relay.Function([var_8227,var_8228,], output)
mod['func_8245'] = func_8245
mod = relay.transform.InferType()(mod)
mutated_mod['func_8245'] = func_8245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8245_call = mutated_mod.get_global_var('func_8245')
var_8247 = relay.var("var_8247", dtype = "uint8", shape = (378,))#candidate|8247|(378,)|var|uint8
var_8248 = relay.var("var_8248", dtype = "int32", shape = (60, 1))#candidate|8248|(60, 1)|var|int32
call_8246 = func_8245_call(var_8247,var_8248,)
output = call_8246
func_8249 = relay.Function([var_8247,var_8248,], output)
mutated_mod['func_8249'] = func_8249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7805_call = mod.get_global_var('func_7805')
func_7806_call = mutated_mod.get_global_var('func_7806')
call_8273 = relay.TupleGetItem(func_7805_call(), 0)
call_8274 = relay.TupleGetItem(func_7806_call(), 0)
output = relay.Tuple([call_8273,])
output2 = relay.Tuple([call_8274,])
func_8293 = relay.Function([], output)
mod['func_8293'] = func_8293
mod = relay.transform.InferType()(mod)
mutated_mod['func_8293'] = func_8293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8293_call = mutated_mod.get_global_var('func_8293')
call_8294 = func_8293_call()
output = call_8294
func_8295 = relay.Function([], output)
mutated_mod['func_8295'] = func_8295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7870_call = mod.get_global_var('func_7870')
func_7871_call = mutated_mod.get_global_var('func_7871')
call_8332 = relay.TupleGetItem(func_7870_call(), 0)
call_8333 = relay.TupleGetItem(func_7871_call(), 0)
output = relay.Tuple([call_8332,])
output2 = relay.Tuple([call_8333,])
func_8338 = relay.Function([], output)
mod['func_8338'] = func_8338
mod = relay.transform.InferType()(mod)
mutated_mod['func_8338'] = func_8338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8338_call = mutated_mod.get_global_var('func_8338')
call_8339 = func_8338_call()
output = call_8339
func_8340 = relay.Function([], output)
mutated_mod['func_8340'] = func_8340
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8457 = relay.var("var_8457", dtype = "float32", shape = (7, 4, 3))#candidate|8457|(7, 4, 3)|var|float32
uop_8458 = relay.cos(var_8457.astype('float32')) # shape=(7, 4, 3)
uop_8463 = relay.acosh(uop_8458.astype('float32')) # shape=(7, 4, 3)
output = relay.Tuple([uop_8463,])
output2 = relay.Tuple([uop_8463,])
func_8465 = relay.Function([var_8457,], output)
mod['func_8465'] = func_8465
mod = relay.transform.InferType()(mod)
var_8466 = relay.var("var_8466", dtype = "float32", shape = (7, 4, 3))#candidate|8466|(7, 4, 3)|var|float32
output = func_8465(var_8466)
func_8467 = relay.Function([var_8466], output)
mutated_mod['func_8467'] = func_8467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7941_call = mod.get_global_var('func_7941')
func_7942_call = mutated_mod.get_global_var('func_7942')
call_8506 = relay.TupleGetItem(func_7941_call(), 0)
call_8507 = relay.TupleGetItem(func_7942_call(), 0)
var_8508 = relay.var("var_8508", dtype = "int32", shape = (6, 12, 2))#candidate|8508|(6, 12, 2)|var|int32
bop_8509 = relay.floor_mod(call_8506.astype('float32'), relay.reshape(var_8508.astype('float32'), relay.shape_of(call_8506))) # shape=(6, 12, 2)
bop_8512 = relay.floor_mod(call_8507.astype('float32'), relay.reshape(var_8508.astype('float32'), relay.shape_of(call_8507))) # shape=(6, 12, 2)
func_2095_call = mod.get_global_var('func_2095')
func_2098_call = mutated_mod.get_global_var('func_2098')
var_8542 = relay.var("var_8542", dtype = "float64", shape = (252,))#candidate|8542|(252,)|var|float64
const_8543 = relay.const([[-10,-8,10,4,8,10,3,-10,2,6,-8,6,2,-8],[3,-2,6,1,-7,-4,9,1,-1,-4,6,5,-2,10],[4,-6,10,1,-7,4,5,8,-3,5,-1,8,-8,1],[-5,-1,-1,-7,-2,-6,1,2,-7,10,-1,-5,4,2],[-8,10,-6,-4,10,7,-10,-3,-3,6,7,-2,-3,-5],[-2,-8,1,-4,1,-3,1,-4,-3,1,4,-7,-5,1],[10,6,-4,2,4,-10,6,-7,3,8,-10,3,-8,5],[1,-5,2,3,-6,1,5,-7,7,9,-7,6,-8,1],[9,-3,-2,3,8,9,-3,5,4,-8,-8,-10,4,2],[5,1,-9,-6,1,-2,5,4,-4,5,-3,-8,2,5],[4,-9,1,6,-2,-9,-2,-5,-6,7,8,-7,-7,-1],[5,-4,-5,9,-4,-8,-7,-1,-1,8,-5,-7,-8,-5],[1,3,-4,-4,-3,7,-8,-4,-3,4,1,-9,-8,1],[-1,3,6,6,5,1,3,-5,-4,-5,-4,-8,2,5],[-6,-6,-5,-8,6,-1,6,-9,9,-9,3,-9,-3,-3],[-6,5,-7,10,-1,-4,-4,6,-8,-8,-8,-1,1,9],[-7,-6,-3,7,-1,3,-5,9,-2,9,1,-7,6,-2],[-6,-8,-5,7,7,-9,1,2,-9,-7,-5,10,-6,5],[-5,-9,-9,-5,3,-2,8,-1,-3,8,4,-2,-2,5],[9,9,8,-6,-7,1,7,-2,-5,5,-8,10,8,2],[-2,7,-8,7,4,-5,4,-3,-9,7,2,2,5,-5],[-3,3,6,9,6,-2,-7,5,2,4,5,-7,-3,8],[-10,1,7,-9,5,9,-1,-6,-9,-2,9,4,5,-10],[10,-6,-8,-4,-4,10,-2,-3,-9,3,-7,8,-1,9],[-4,6,-4,4,3,9,-2,7,7,7,8,-5,-5,1],[5,-3,9,-3,-4,-7,7,-4,-4,-5,2,8,-1,5],[3,-3,-5,7,8,5,7,8,-7,-2,-3,1,-8,5],[1,9,-3,-4,1,-10,-3,8,8,-3,8,5,4,-7],[6,-4,-2,-3,-7,3,10,4,2,-5,-10,5,-6,1],[10,-4,2,5,3,8,5,-6,9,-10,6,1,-4,5],[-9,-1,4,7,-5,9,10,-6,3,2,3,-2,7,-4],[10,-2,4,9,-1,6,-1,-2,6,-6,9,2,-9,-1],[-8,7,4,10,-3,8,7,9,-10,-7,-8,-7,2,-9],[4,9,-4,-1,-8,-6,9,-6,-7,4,-6,6,-7,-1],[2,2,-9,-9,1,-9,10,1,-9,-8,4,8,5,3],[8,-3,-1,8,7,-1,9,9,-7,-1,-1,-5,-2,-4],[6,1,9,-6,-10,-10,-4,-7,-5,2,-7,8,-3,3],[-3,-4,-4,5,-10,4,5,-7,9,2,8,-5,7,5],[4,7,6,-8,-8,-4,4,-8,-5,8,7,-7,-5,4],[-4,4,-10,7,2,-4,10,7,-7,-3,-10,-6,4,-5],[-6,3,-9,-9,-7,5,-6,10,-9,10,-3,-8,-5,-9],[-8,5,5,-3,4,3,10,1,-9,2,9,5,4,-3],[8,7,8,7,2,8,-1,9,3,9,-2,-1,2,3],[9,-6,-9,2,-5,-3,-8,4,5,3,5,9,3,-8],[-8,-1,-6,6,10,-5,7,-3,-10,-6,-10,3,3,5],[-4,8,-6,8,6,9,10,-10,-3,-3,9,8,-10,-5],[4,6,-4,7,7,-2,-9,-10,5,7,-2,1,-2,1],[3,-5,-7,-3,9,-9,-7,-9,1,7,-9,6,-7,-5],[7,2,-3,6,-10,-10,-1,5,-1,-8,4,-10,2,-4],[-2,-7,-4,-10,-6,8,-5,6,9,-8,8,7,-1,-4],[-3,-9,9,6,7,-2,-2,10,9,3,-1,-10,-7,10],[-4,-9,7,5,-6,-9,9,-5,-10,-8,2,8,-2,-2],[-7,-5,1,1,-3,-1,-7,3,2,7,-2,-10,6,-10],[8,7,6,-8,9,-2,4,-3,-4,9,2,-7,-2,-3]], dtype = "int8")#candidate|8543|(54, 14)|const|int8
call_8541 = relay.TupleGetItem(func_2095_call(relay.reshape(var_8542.astype('float64'), [9, 4, 7]), relay.reshape(const_8543.astype('int8'), [756,]), ), 0)
call_8544 = relay.TupleGetItem(func_2098_call(relay.reshape(var_8542.astype('float64'), [9, 4, 7]), relay.reshape(const_8543.astype('int8'), [756,]), ), 0)
func_5512_call = mod.get_global_var('func_5512')
func_5513_call = mutated_mod.get_global_var('func_5513')
call_8562 = func_5512_call()
call_8563 = func_5512_call()
func_3057_call = mod.get_global_var('func_3057')
func_3059_call = mutated_mod.get_global_var('func_3059')
var_8588 = relay.var("var_8588", dtype = "float64", shape = (720,))#candidate|8588|(720,)|var|float64
call_8587 = relay.TupleGetItem(func_3057_call(relay.reshape(var_8588.astype('float64'), [15, 12, 4])), 1)
call_8589 = relay.TupleGetItem(func_3059_call(relay.reshape(var_8588.astype('float64'), [15, 12, 4])), 1)
output = relay.Tuple([bop_8509,call_8541,var_8542,const_8543,call_8562,call_8587,var_8588,])
output2 = relay.Tuple([bop_8512,call_8544,var_8542,const_8543,call_8563,call_8589,var_8588,])
func_8593 = relay.Function([var_8508,var_8542,var_8588,], output)
mod['func_8593'] = func_8593
mod = relay.transform.InferType()(mod)
mutated_mod['func_8593'] = func_8593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8593_call = mutated_mod.get_global_var('func_8593')
var_8595 = relay.var("var_8595", dtype = "int32", shape = (6, 12, 2))#candidate|8595|(6, 12, 2)|var|int32
var_8596 = relay.var("var_8596", dtype = "float64", shape = (252,))#candidate|8596|(252,)|var|float64
var_8597 = relay.var("var_8597", dtype = "float64", shape = (720,))#candidate|8597|(720,)|var|float64
call_8594 = func_8593_call(var_8595,var_8596,var_8597,)
output = call_8594
func_8598 = relay.Function([var_8595,var_8596,var_8597,], output)
mutated_mod['func_8598'] = func_8598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7084_call = mod.get_global_var('func_7084')
func_7085_call = mutated_mod.get_global_var('func_7085')
call_8675 = relay.TupleGetItem(func_7084_call(), 1)
call_8676 = relay.TupleGetItem(func_7085_call(), 1)
output = relay.Tuple([call_8675,])
output2 = relay.Tuple([call_8676,])
func_8677 = relay.Function([], output)
mod['func_8677'] = func_8677
mod = relay.transform.InferType()(mod)
mutated_mod['func_8677'] = func_8677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8677_call = mutated_mod.get_global_var('func_8677')
call_8678 = func_8677_call()
output = call_8678
func_8679 = relay.Function([], output)
mutated_mod['func_8679'] = func_8679
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8845 = relay.var("var_8845", dtype = "float64", shape = (15, 4, 3))#candidate|8845|(15, 4, 3)|var|float64
uop_8846 = relay.sqrt(var_8845.astype('float64')) # shape=(15, 4, 3)
func_7406_call = mod.get_global_var('func_7406')
func_7407_call = mutated_mod.get_global_var('func_7407')
call_8849 = func_7406_call()
call_8850 = func_7406_call()
func_8338_call = mod.get_global_var('func_8338')
func_8340_call = mutated_mod.get_global_var('func_8340')
call_8858 = relay.TupleGetItem(func_8338_call(), 0)
call_8859 = relay.TupleGetItem(func_8340_call(), 0)
output = relay.Tuple([uop_8846,call_8849,call_8858,])
output2 = relay.Tuple([uop_8846,call_8850,call_8859,])
func_8862 = relay.Function([var_8845,], output)
mod['func_8862'] = func_8862
mod = relay.transform.InferType()(mod)
mutated_mod['func_8862'] = func_8862
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8863 = relay.var("var_8863", dtype = "float64", shape = (15, 4, 3))#candidate|8863|(15, 4, 3)|var|float64
func_8862_call = mutated_mod.get_global_var('func_8862')
call_8864 = func_8862_call(var_8863)
output = call_8864
func_8865 = relay.Function([var_8863], output)
mutated_mod['func_8865'] = func_8865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5512_call = mod.get_global_var('func_5512')
func_5513_call = mutated_mod.get_global_var('func_5513')
call_8938 = func_5512_call()
call_8939 = func_5512_call()
const_8951 = relay.const([[[5,7],[-7,-1],[5,6],[-6,-1],[-2,-6],[4,1],[1,-3],[-1,1],[8,2],[-3,10],[4,1],[-6,-7]],[[-1,-3],[-8,6],[-4,-10],[-4,3],[-1,7],[-7,-1],[4,-3],[6,-3],[4,-1],[2,-4],[8,3],[7,2]],[[-10,-1],[10,2],[-5,6],[-6,8],[5,-4],[9,-3],[-4,-7],[-2,-8],[-1,-1],[-2,-5],[-7,-8],[-2,-3]],[[-10,-5],[-7,-5],[5,-9],[-4,9],[-5,-6],[-5,-3],[6,7],[2,6],[-9,10],[-9,4],[-1,-3],[9,2]],[[-4,10],[-1,-4],[-6,4],[3,9],[-1,7],[-6,-6],[-5,1],[10,-9],[-2,-6],[3,8],[2,-9],[-2,-8]],[[-7,-2],[9,7],[-4,-9],[2,9],[-8,4],[4,5],[6,3],[-10,10],[10,-10],[2,5],[6,2],[-4,1]]], dtype = "int32")#candidate|8951|(6, 12, 2)|const|int32
bop_8952 = relay.logical_xor(call_8938.astype('uint32'), relay.reshape(const_8951.astype('uint32'), relay.shape_of(call_8938))) # shape=(6, 12, 2)
bop_8955 = relay.logical_xor(call_8939.astype('uint32'), relay.reshape(const_8951.astype('uint32'), relay.shape_of(call_8939))) # shape=(6, 12, 2)
func_1789_call = mod.get_global_var('func_1789')
func_1792_call = mutated_mod.get_global_var('func_1792')
var_8968 = relay.var("var_8968", dtype = "int8", shape = (9, 84))#candidate|8968|(9, 84)|var|int8
call_8967 = relay.TupleGetItem(func_1789_call(relay.reshape(var_8968.astype('int8'), [7, 12, 9]), relay.reshape(var_8968.astype('int8'), [7, 12, 9]), ), 0)
call_8969 = relay.TupleGetItem(func_1792_call(relay.reshape(var_8968.astype('int8'), [7, 12, 9]), relay.reshape(var_8968.astype('int8'), [7, 12, 9]), ), 0)
func_7364_call = mod.get_global_var('func_7364')
func_7366_call = mutated_mod.get_global_var('func_7366')
call_8977 = relay.TupleGetItem(func_7364_call(relay.reshape(var_8968.astype('int8'), [18, 42])), 3)
call_8978 = relay.TupleGetItem(func_7366_call(relay.reshape(var_8968.astype('int8'), [18, 42])), 3)
func_3057_call = mod.get_global_var('func_3057')
func_3059_call = mutated_mod.get_global_var('func_3059')
const_9001 = relay.const([9.093208,-0.225427,-8.970695,-4.895227,8.976699,5.403312,-5.388202,-0.733004,-2.464762,-1.104226,-6.580355,1.005344,-6.861892,-2.968879,-5.466356,-1.855421,2.153435,-0.690753,-2.323469,1.488550,0.535747,-4.899259,3.613218,5.784900,-4.958988,-4.806258,-0.131264,-6.957610,-7.502814,-4.442351,-5.155331,-8.564731,3.446413,0.254930,-9.106144,1.949429,-4.560735,7.254472,-3.602588,0.127327,-1.600949,7.991396,6.714302,-3.980619,-5.278635,-4.319751,1.713296,6.130241,-7.538262,-4.795567,0.575358,-9.824493,6.380287,5.858512,-6.087224,-6.936318,-9.615474,-7.232053,1.953850,9.347487,1.896704,-9.900052,8.757830,-9.404262,0.413052,-9.599050,-2.325291,-5.809648,-4.436380,-9.573712,-2.262526,6.670677,-8.718355,-8.440686,-8.486757,-6.949091,7.092876,-9.991087,-1.840141,-0.072463,6.068797,-0.806161,-1.512274,-8.187241,-2.713659,7.851855,8.557384,5.460951,-4.967847,-6.221847,-2.993345,7.351174,1.509027,-4.405673,-3.719933,5.310701,6.172727,3.547658,-3.645364,-1.758962,-5.666549,9.900766,-8.396306,-9.563211,-2.720573,-7.036266,5.064067,9.423758,0.039659,-2.676602,-7.086855,-2.419174,4.974232,3.437692,0.132660,-2.860133,-9.183453,3.788316,-0.539248,2.490889,-1.838292,0.853939,4.060134,3.055340,-4.808970,-4.271353,3.492414,-4.727164,0.223412,4.095245,0.365297,-9.474395,5.317875,5.775606,5.797195,9.959417,-6.041780,0.914375,2.834953,-2.952241,-4.797981,-4.637626,3.683966,-2.114189,1.298747,3.868340,0.172037,-3.835433,-4.658075,9.048889,-5.606565,8.143121,2.659994,4.977692,2.116280,3.816988,-4.425663,-3.243489,-7.273318,-3.152907,-3.265602,1.326889,-4.092224,-6.466719,7.997208,-9.888571,-5.289565,-2.471521,4.671385,-3.075115,5.229419,-9.178521,-0.445099,-2.456161,-7.796053,-5.508220,-7.094169,-1.637199,4.073402,8.829167,-2.708601,-7.908144,-6.743616,8.559723,-8.257153,-2.977633,7.579938,-3.732706,7.988967,-6.644358,2.912210,-5.450307,-0.083873,-9.897753,-8.527214,-9.854191,-2.502440,5.429406,1.056658,-6.438320,5.793257,-7.718444,5.041566,-2.014749,9.221164,-0.050935,4.565284,-9.356710,-2.176933,3.106133,1.157790,0.731748,-6.027231,-0.914895,6.853292,-0.460304,1.382811,6.749534,7.696922,-9.706577,9.577981,4.795000,5.286442,-3.884258,1.980394,-5.816137,-1.748679,-4.400035,3.468806,-4.635978,5.604016,1.326498,0.570092,4.407334,-8.418309,7.385422,9.251976,-5.950312,3.098329,-0.862063,-7.743472,3.028887,-1.209280,9.855701,-9.829827,9.821874,-5.752832,-7.569867,6.174325,-1.839969,4.047515,2.722915,0.221820,-6.855344,5.852733,2.727366,5.310278,-0.771205,-3.658781,0.576005,4.800716,-3.684579,7.851385,-2.069068,-8.057781,-7.695674,-8.247873,-4.866322,5.397356,-1.369070,1.428799,-1.667510,-9.617254,0.023286,2.275710,8.842649,6.177225,-7.789186,1.731373,8.962414,-1.234440,2.119283,-2.847839,-9.401182,-4.086386,-2.681917,-0.968295,5.824193,8.006881,3.124345,9.283625,3.369260,-6.400625,-3.050715,-5.036710,3.010475,1.199565,-3.318509,6.894402,-3.889283,6.428064,0.018374,6.951988,2.522778,6.352928,3.466729,2.281764,5.782398,4.206065,7.738215,-3.731648,-9.548216,-7.349979,7.996261,7.789549,1.738680,-8.546437,-2.969080,0.798839,-3.202717,-3.768184,-3.869277,-9.736016,1.932198,2.262525,-6.514784,3.060563,0.010171,4.281729,3.529785,-7.614969,1.883894,-9.502505,6.337362,2.082418,-2.873245,7.100058,-5.933366,0.520881,0.879338,-1.037528,-0.179014,-2.662410,2.635680,-6.036153,-2.649209,-2.091543,0.192174,5.086759,-9.662449,-1.566676,-1.978554,8.144176,3.125515,-2.296773,2.730080,-6.913442,1.075298,-5.250214,-7.137032,6.728331,8.084649,5.573129,-9.121419,1.467773,5.971794,-3.953133,-5.834670,-7.136955,-9.836143,-8.131284,-6.848271,5.155544,-5.313164,-5.261857,-0.369386,6.868753,9.576286,-1.536307,-2.553864,3.400233,8.891706,9.492109,1.894949,9.695625,3.713110,-3.668289,2.272328,9.401444,6.449024,-7.197599,9.506761,2.902731,-7.048338,4.681190,-6.330539,3.346387,-1.340057,2.817503,-3.150422,0.230334,-8.787421,0.111356,5.331184,1.070965,2.877445,-7.618563,-8.360551,1.657953,3.146696,5.430330,2.395459,8.230060,5.391937,-9.011332,7.540815,8.537157,1.324244,4.538164,0.990408,3.276701,1.032084,-2.069281,0.308553,-0.979563,-2.076827,-5.356856,-9.014996,7.031006,-6.493379,-7.698099,7.364495,-2.656066,-2.504794,3.637187,-2.153810,-9.191940,-9.208693,6.624338,4.972066,-8.170535,7.829368,3.205066,-6.457604,-1.580853,-3.488454,-0.473491,-6.829821,-1.653377,4.533728,4.399870,-1.532376,2.444301,-5.030949,7.989371,-6.824500,5.210009,-3.951007,-2.033284,6.349433,-8.121215,8.351757,7.297822,6.853640,-4.661251,1.129881,-1.909038,-1.773595,-3.234265,3.597855,-3.943324,7.215644,5.773894,-0.435678,-9.454117,-4.102376,-2.099839,0.713976,-8.232397,7.371208,5.291048,-6.555979,3.216798,7.834844,9.966718,5.669842,5.311295,0.786293,-8.516668,-2.873862,3.875907,7.480532,-2.226145,3.459320,3.153644,8.071314,2.208969,8.011315,-0.973261,-7.931910,3.522800,5.512528,-5.054042,0.997334,9.695420,5.921415,7.725935,-7.032875,9.346903,-7.659354,-9.733696,-2.690477,3.967625,-4.930837,-8.832142,5.627899,-5.089758,-4.097039,5.616784,-3.765536,9.443672,2.344496,-3.394584,-2.334013,3.001606,3.141663,5.054915,4.387035,6.492303,-7.831576,-7.777955,8.383681,6.951757,6.938581,7.784942,4.437936,0.669950,7.487388,-4.186864,5.844563,-0.688148,6.315593,-8.929770,-7.483303,5.761745,-7.756375,-9.556633,-2.395080,1.319899,-3.957856,3.922565,-0.586954,-0.296732,1.588318,6.047902,-8.405026,4.345670,9.270162,-2.300097,0.220420,4.145917,0.871659,2.985522,5.370687,6.361905,2.123523,0.627692,9.477676,-2.690115,-0.184805,-4.395229,9.178127,-0.539939,8.957013,8.528298,-5.285652,-2.640061,-7.636811,-5.636422,1.308482,-8.890556,-3.876132,-8.247123,3.434087,-2.147478,-7.328838,8.767870,-6.916556,8.638316,-0.391286,-6.502973,9.559204,3.714839,-7.565903,4.795522,6.214333,7.047586,8.831912,-0.484293,-0.889157,-2.711796,4.130157,-8.529557,5.780190,7.125668,-9.080609,2.997172,9.458093,-0.015828,-8.888039,5.983366,4.038046,0.661293,-3.545899,8.373973,0.471443,2.686059,3.672435,-5.382116,1.530565,7.887328,-8.144705,7.554397,1.358335,0.537980,2.780355,8.882754,0.953333,8.834965,-1.157537,-8.293476,-8.823732,-5.539556,-9.693969,8.872124,0.184220,7.138331,3.105816,3.727134,-2.844316,-5.544971,0.783846,-7.376312,-2.701191,-5.834845,3.367086,-6.431723,-7.414030,9.412875,-4.060323,2.192504,2.466134,6.559041,4.681483,4.457770,5.517388,-3.860279,-6.230606,-8.632011,-1.095100,9.795069,9.957054,-9.215236,3.736378,-8.634588,-3.619477,3.221534,0.313971,-3.567281,1.155559,-7.830746,7.423883,7.881693,-4.891830,-3.284676,-6.744082,-5.126271,-4.801051,6.245049,-8.530212,8.654285,0.483922,6.874616,8.714530,-8.454201,5.636201,8.827075,5.795964,-4.723095,-0.606885,-5.962150,3.279578,2.392523,5.812199,2.897515,-2.745994,-6.496652,8.233333,-0.567043,3.387885,1.775312,-7.132959,4.616579,5.766194,1.253072,9.194821,-1.056001,-7.242598,-5.953982,-4.144070,4.704050,-3.448584,4.471248,3.050734,-9.518559,-2.444727,-6.318111,-1.612097,-2.129443,1.994380], dtype = "float64")#candidate|9001|(720,)|const|float64
call_9000 = relay.TupleGetItem(func_3057_call(relay.reshape(const_9001.astype('float64'), [15, 12, 4])), 1)
call_9002 = relay.TupleGetItem(func_3059_call(relay.reshape(const_9001.astype('float64'), [15, 12, 4])), 1)
uop_9004 = relay.asinh(call_8977.astype('float64')) # shape=(18, 42)
uop_9006 = relay.asinh(call_8978.astype('float64')) # shape=(18, 42)
output = relay.Tuple([bop_8952,call_8967,var_8968,call_9000,const_9001,uop_9004,])
output2 = relay.Tuple([bop_8955,call_8969,var_8968,call_9002,const_9001,uop_9006,])
func_9010 = relay.Function([var_8968,], output)
mod['func_9010'] = func_9010
mod = relay.transform.InferType()(mod)
mutated_mod['func_9010'] = func_9010
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9011 = relay.var("var_9011", dtype = "int8", shape = (9, 84))#candidate|9011|(9, 84)|var|int8
func_9010_call = mutated_mod.get_global_var('func_9010')
call_9012 = func_9010_call(var_9011)
output = call_9012
func_9013 = relay.Function([var_9011], output)
mutated_mod['func_9013'] = func_9013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7551_call = mod.get_global_var('func_7551')
func_7552_call = mutated_mod.get_global_var('func_7552')
call_9015 = func_7551_call()
call_9016 = func_7551_call()
output = relay.Tuple([call_9015,])
output2 = relay.Tuple([call_9016,])
func_9033 = relay.Function([], output)
mod['func_9033'] = func_9033
mod = relay.transform.InferType()(mod)
output = func_9033()
func_9034 = relay.Function([], output)
mutated_mod['func_9034'] = func_9034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6551_call = mod.get_global_var('func_6551')
func_6552_call = mutated_mod.get_global_var('func_6552')
call_9138 = relay.TupleGetItem(func_6551_call(), 0)
call_9139 = relay.TupleGetItem(func_6552_call(), 0)
output = relay.Tuple([call_9138,])
output2 = relay.Tuple([call_9139,])
func_9147 = relay.Function([], output)
mod['func_9147'] = func_9147
mod = relay.transform.InferType()(mod)
mutated_mod['func_9147'] = func_9147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9147_call = mutated_mod.get_global_var('func_9147')
call_9148 = func_9147_call()
output = call_9148
func_9149 = relay.Function([], output)
mutated_mod['func_9149'] = func_9149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8338_call = mod.get_global_var('func_8338')
func_8340_call = mutated_mod.get_global_var('func_8340')
call_9161 = relay.TupleGetItem(func_8338_call(), 0)
call_9162 = relay.TupleGetItem(func_8340_call(), 0)
func_2765_call = mod.get_global_var('func_2765')
func_2774_call = mutated_mod.get_global_var('func_2774')
const_9164 = relay.const([-5,9,7,-7,3,9,9,-7,-4,10,-3,-10,-7,3,7,10,-2,-3,4,-9,1,-1,9,9,-10,-9,-9,1,2,-5,-5,10,-5,8,4,6,-7,-4,-4,2,-3,-5,7,-8,2,-9,-10,6,-3,5,-2,-1,-6,7,-9,4,-7,-4,-6,5,-8,7,-3,-3,7,-4,-9,-10,-1,6,4,-3,8,-7,-2,4,-7,7,-6,-8,8,-4,6,-1,10,6,7,7,7,-2,6,-10,-9,-3,-7,7,-3,-2,4,-6,1,2,-1,3,-3,-8,3,2,-3,6,-7,5,6,9,-1,8,-6,1,-9,5,1,3,-9,7,-9,4,-8,6,-6,-5,7,-10,2,-10,8,-5,1,5,2,-4,3,-8,8,-6,-6,-3,2,10,7,-7,7,5,1,-10,10,-3,-3,-5,-5,-7,-1,8,6,-9,7,-9,9,2,2,2,-7,6,-8,-1,3,7,-8,9,-10,8,-6,4,1,-7,10,-6,8,5,4,-10,3,2,2,-9,10,10,6,-1,-1,-9,-10,6,-6,4,6,-8,-3,4,2,8,3,-5,-3,4,-9,-3,-10,6,9,-8,8,-7,8,4,5,9,-9,6,3,6,-5,-10,7,10,10,10,-8,8,-8,-6,-6,2,-9,9,-8,-5,-1,7,3,-3,-9,-10,2,3,-2,-5,-3,-4,-5,6,8,-6,6,-7,5,1,-5,-9,9,-8,-10,-7,-2,-3,6,2,-1,-2,-6,-6,-1,2,-6,-4,2,5,-5,-3,5,-7,7,4,-10,7,-5,4,9,-3,-7,-1,-7,3,1,2,-3,-7,-8,2,-7,-3,-1,-10,3,7,-10,-2,-7,10,10,3,3,-8,3,7,9,4,-7,2,8,1,-8,-5,-8,2,-9,3,-7,2,-1,1,1,1,10,7,1,-5,2,3,-7,8,-9,9,-4,-7,-2,-4,-4,10,-8,-3,6,9,10,-8,8,6,-8,7,-5,-4,3,-9,-5,-4,-5,-2,-4,1,-5,-4,6,2,4,4,4,-8,10,-7,-6,7,-5,-4,-2,-7,-7,-3,1,-7,-7,-6,-10,9,2,4,6,-1,2,1,2,4,9,2,-3,4,-1,10,-5,-3,6,6,9,-2,-3,-7,-1,6,-8,-9,-9,-10,3,2,-10,6,-2,-7,-8,-6,-2,-7,3,2,-4,-10,-5,-5,-2,-8,-4,2,7,-9,-8,7,7,10,9,-1,4,8,-4,8,2,2,-2,-1,2,3,6,-10,6,-3,4,10,5,-7,-2,7,-1,-9,-3,-2,-2,-5,-7,-3,6,1,-2,-8,-10,-8,-10,-8,3,-5,-8,3,4,-10,4,-7,9,-8,9,-8,3,-3,10,-5,9,-1,-9,-8,-2,-7,2,-5,-1,2,3,1,7,-8,-9,1,-4,-6,-9,-7,3,-7,7,-7,-9,10,-10,-7,-9,5,-7,-4,1,4,-4,-10,5,3,-1,2,-1,1,5,8,2,-10,2,-10,5,4,6,-10,3,-7,-4,-4,1,-6,-3,10,10,4,7,-6,9,4,3,-10,-7,-1,-4,-6,2,5,8,1,-7,-1,-3,7,-8,9,2,8,-4,10,5,7,10,3,7,-8,-2,-1,8,7,8,7,-7,1,5,-1,9,-10,-10,-7,-8,5,3,-5,3,-7,9,-3,1,8,-7,-10,9,-7,2,9,-10,2,-2,6,-10,-8,-7,7,-7,5,6,-10,5,5,3,9,-10,-7,-9,-8,6,-10,-9,10,-4,7,2,6,-7,3,6,-3,3,1,-3,-1,-6,-9,-9,-8,7,2,7,5,8,-3,-1,3,6,-6,-4,7,9,5,-8,1,-8,-3,1,-8,7,5,10,10,5,-7,6,-9,2,4,-4,-3,10,-9,5,9,-3,-8,6,2,-5,-10,-5,-5,-2,-6,6,1,7,-4,-1,4,1,8,-3,1,-9,10,-10,8,-6,8,-6,-5,-3,7,5,-8,5,-6,-6,6,-7,-7,1,-9,-2,8,-8,-2,5,-4,1,7,-8,4,-1,9,-9,7,6,9,-4,7,-4,-2,-6,-7,8,5,-10,-2,-3,1,9,-4,-5,-2,-3,-1,-8,4], dtype = "uint32")#candidate|9164|(784,)|const|uint32
var_9165 = relay.var("var_9165", dtype = "int32", shape = (60,))#candidate|9165|(60,)|var|int32
const_9166 = relay.const([9,-8,-8,-3,10,-8,-10,2,7,8,1,6,-10,-7,4,-10,4,2,-8,2,-10,-4,5,4,8,-7,-8,6,4,10,9,-3,-8,5,-1,-2,5,1,4,2,-9,-10,-2,5,-10,-5,5,-2,-4,-8,1,-8,-10,6,6,7,-9,-4,-5,-8,-6,-4,1,-5,-10,-2,7,-9,8,-2,-5,10,5,-2,7,-5,-3,5,4,2,4,-7,3,7,-1,-6,7,-8,-1,3,2,-10,-9,-2,-4,-1,8,7,-3,-1,-5,-1,-4,-5,3,3,-7,2,-8,1,1,-10,9,8,-4,-8,-7,-3,10,-6,-7,-10,-3,-2,-9,5,-6,-6,-2,9,-5,-9,6,5,-8,-10,-9,-9,3,5,6,-1,-3,-9,5,-5,5,-5,3,-8,1,8,-8,-4,10,-4,-7,9,6,-9,4,-1,5,1,-8,-1,-6,-10,-5,7,2,-2,-8,3,8,5,3,2,-6,7,9,2,8,10,-6,9,-8,-9,3,-2,-3,3,-5,-5,8,-4,10,2,7,1,1,-3,4,-5,3,8,-4,-1,9,-9,-8,4,8,7,-10,-1,2,-9,-6,-3,-2,5,5,-7,4,1,-1,-1,3,-6,-6,-3,1,-5,8,5,3,10,-8,2,2,-3,8,-2,1,3,5,8,-2,4,-2,-2,9,-5,-8,10,-2,-3,-8,-3,-4,-6,6,6,8,-8,9,7,9,-8,1,-6,-2,5,-5,6,-7,-10,-8,-9,-8,-9,6,-4,10,-3,-9,-3,-10,-10,-7,6,-1,-6,-7,-7,1,-10,4,1,8,-4,-3,-8,7,1,4,-9,6,-8,-10,7,-3,-10,3,-2,5,9,-4,2,7,-9,-3,-8,6,1,10,-9,7,1,-1,2,-8,-4,8,-6,-1,5,-3,-2,-8,-7,3,3,-7,9,-7,4,1,-10,7,-5,-10,2,-7,4,-9,6,-9,1,5,-4,2,10,9,6,7,-4,-6,-2,-1,8,9,2,-5,6,7,-4,1,4,-5,3,6,9,-4,-4,-7,-4,6,-6,3,3,-3,8,-3,3,-3,-2,-4,10,1,-2,6,-9,-6,-3,9,6,3,8,-6,-5,-7,-9,-5,-10,3,-9,2,1,-2,-6,2,-5,-7,10,3,-4,2,1,2,-6,-5,-4,-4,4,9,7,3,-6,-2,-4,4,5,-9,3,-10,-6,7,-4,5,7,8,-5,3,-1,-10,1,-1,9,-3,-3,5,-9,-9,3,1,-10,-3,9,-6,2,5,1,-10,-6,-5,7,10,4,9,5,-7,-8,-10,6,-9,-2,-4,8,3,6,-5,-10,10,-6,1,-10,6,9,-7,2,7,-10,-8,4,4,-1,-4,-6,3,5,3,4,-7,5,-10,-10,2,-8,10,-2,-2,5,-4,-2,5,2,-5,9,-1,-6,1,8,9,4,7,-2,-8,5,-10,-10,-4,-4,9,3,-8,-1,-8,-2,6,-4,1,2,-5,-3,3,1,-6,-8,-8,6,-9,-5,-9,-4,3,8,6,-3,-6,-9,10,6,-4,-2,5,-10,-7,3,-10,-1,-7,-8,8,5,10,4,-3,-5,-7,1,6,-8,4,7,8,-8,-6,7,8,1,-5,7,7,5,10,6,7,9,5,7,5,-10,4,6,-1,-1,3,-2,-1,-4,5,10,-2,-3,-4,-10,-10,1,-10,-7,3,-7,5,7,-8,-10,1,-3,9,-1,8,4,-2,1,2,-2,5,3,9,-9,-3,10,-9,6,-10,-2,8,6,3,-3,5,-1,-5,10,4,-2,8,-10,4,-6,-5,-3,-6,-5,6,1,-5,10,7,-5,9,10,1,2,-8,-2,-9,-5,5,2,-10,-3,-7,7,4,9,-1,-9,-2,10,1,2,6,-5,-1,-4,-1,-6,-1,6,-6,9,5,2,2,7,5,-5,1,3,8,3,-4,2,3,-3,3,8,3,-7,-3,10,6,-8,7,10,-1,-7,-1,2,-4,-3,-10,-9,1,10,2,2,7,-6,-3,10,-7,-9], dtype = "int8")#candidate|9166|(756,)|const|int8
const_9167 = relay.const([-7.455072,-9.611919,-9.307327,-4.101823,-6.674166,3.943126,-5.103463,-8.745870,5.792787,-2.815598,-1.854706,-2.966536,-1.562729,-5.901280,-6.968091,1.377080,-0.850013,4.027866,-3.425862,-1.596582,-1.970130,-7.426253,1.275493,4.517701,1.385565,6.899419,-8.214165,8.204941,-9.289816,-4.009330,-9.042062,-9.812430,7.768472,2.306131,2.846284,-7.488131,-2.766056,-1.695342,2.703110,-6.483993,0.960818,9.813637,9.373023,9.786417,-1.198062,-2.646244,5.657563,4.210116,-8.806505,-8.433783,-6.143826,1.800605,-5.303011,-8.019025,7.459500,-8.445744,4.740839,-8.354489,-9.554620,-9.198074,8.399867,1.783116,1.916324,-0.360763,-9.767718,-0.977012,5.438496,4.369900,9.980322,-3.582097,-9.605656,-7.974314,-0.135494,-6.189515,-3.515875,1.092475,6.738166,-5.295004,4.153282,7.784330,-5.725963,0.232062,1.235845,4.568725,-1.309647,-7.722060,-1.189437,-6.426658,1.140379,1.063106,-5.623614,-3.929980,1.529010,-4.616750,5.028968,-6.660754,8.110474,8.533107,-6.666730,-1.340970,-0.103332,8.684334,8.738853,0.863518,-7.559012,-3.512408,9.425867,8.257157,7.571205,-9.464034,2.284293,-9.906453,-8.648256,7.156893,-6.204274,4.524500,-9.543348,3.482924,5.100475,6.837371,1.805701,-8.804749,-2.212150,-5.918541,7.885813,-1.021170,1.987477,-1.983752,-8.193154,1.224038,4.516479,-8.613625,2.084211,2.903358,-9.032575,6.913066,-4.730953,4.053386,8.003951,-3.083006,-2.912995,0.016765,-6.359876,2.252285,4.102727,9.259149,9.832181,2.907974,-8.335320,6.251482,9.594229,-5.032197,-9.756362,-1.737489,5.783887,7.529266,7.974402,-8.834664,-3.017050,-8.684293,-2.693984,-9.185818,3.571558,-4.644774,-2.106299,0.958110,-9.838045,8.630002,8.433471,-2.735779,-4.639543,-4.790652,-3.892003,1.043669,-7.540834,8.583959,-1.832586,-1.297203,6.797920,6.732134,2.656941,7.129732,-7.258444,-7.024176,-0.121702,6.706195,-9.581232,-4.459455,-7.376267,4.905387,2.418812,2.195635], dtype = "float64")#candidate|9167|(192,)|const|float64
var_9168 = relay.var("var_9168", dtype = "float64", shape = (42, 6))#candidate|9168|(42, 6)|var|float64
const_9169 = relay.const([8,4,1,1,6,4,-7,5,2,-10,4,3,7,-8,8,9,-9,6,-8,6,2,-6,-3,-6,4,-9,9,8,9,-7,5,-3,-9,-2,7,-1,-10,-9,-1,7,2,-2,1,6,-7,-6,-9,7,-7,4,-9,-4,-3,-3,9,-8,9,9,3,1,-10,-2,-6,-6,-8,-9,-3,-7,6,-1,-1,6,-10,-9,2,-10,-6,1,1,-9,8,-7,10,7,3,3,-8,3,5,8,-1,2,-3,1,10,5,7,9,6,-5,6,3,8,2,8,-1,-8,-8,5,5,9,-3,3,-4,-10,8,-9,-1,-6,10,-1,-3,-5,-10,-10,6,-6,-6,3,-8,10,-10,-8,8,4,-8,-1,5,-3,4,9,-5,-1,6,2,10,1,-1,-2,2,6,-2,2,1,-10,1,7,6,6,5,-5,9,4,4,-10,-2,6,-3,9,6,-3,1,-4,9,1,7,8,2,8,9,-10,-4,5,5,-5,5,9,-7,5,2,-3,-1,-4,4,9,-10,4,-5,3,-3,2,-6,8,-3,-1,-10,-5,5,4,-1,-3,-3,-5,6,-10,-6,-8,3,-6,-10,3,-1,-1,-8,-8,-7,10,-9,-8,-4,-3,1,5,-9,2,9,-9,4,9,-2,-10,1,1,-6,-3,7,3,9,-4,8,-8,-1,-7,7,-4,-6,-10,-4,-7,1,-1,7,-6,9,-7,-6,-3,-1,10,10,-7,-8,-5,9,3,1,-8,-5,5,6,2,-6,-9,-9,7,6,-8,-2,-9,3,10,-5,2,-3,-5,-8,1,3,-3,2,2,5,-2,-10,-7,-10,-7,-5,6,-6,7,7,-10,-9,-3,-4,-8,-2,3,9,5,6,6,-2,9,3,-2,5,1,6,6,-6,6,-5,9,10,5,7,9,-4,-7,-4,7,2,7,9,-7,-8,-4,1,-8,9,-9,5,-8,-6,-5,-6,2,-10,8,-2,6,-8,-4,-4,-10,-6,-9,-6,-9,4,5,-8,-9,-5,8,2], dtype = "uint8")#candidate|9169|(378,)|const|uint8
call_9163 = relay.TupleGetItem(func_2765_call(relay.reshape(const_9164.astype('uint32'), [8, 7, 14]), relay.reshape(const_9164.astype('uint32'), [8, 7, 14]), relay.reshape(var_9165.astype('int32'), [60,]), relay.reshape(const_9166.astype('int8'), [9, 84]), relay.reshape(const_9167.astype('float64'), [24, 8]), relay.reshape(var_9168.astype('float64'), [1, 252]), relay.reshape(const_9169.astype('uint8'), [378,]), ), 13)
call_9170 = relay.TupleGetItem(func_2774_call(relay.reshape(const_9164.astype('uint32'), [8, 7, 14]), relay.reshape(const_9164.astype('uint32'), [8, 7, 14]), relay.reshape(var_9165.astype('int32'), [60,]), relay.reshape(const_9166.astype('int8'), [9, 84]), relay.reshape(const_9167.astype('float64'), [24, 8]), relay.reshape(var_9168.astype('float64'), [1, 252]), relay.reshape(const_9169.astype('uint8'), [378,]), ), 13)
var_9173 = relay.var("var_9173", dtype = "int32", shape = (6, 12, 2))#candidate|9173|(6, 12, 2)|var|int32
bop_9174 = relay.bitwise_or(call_9161.astype('int8'), relay.reshape(var_9173.astype('int8'), relay.shape_of(call_9161))) # shape=(6, 12, 2)
bop_9177 = relay.bitwise_or(call_9162.astype('int8'), relay.reshape(var_9173.astype('int8'), relay.shape_of(call_9162))) # shape=(6, 12, 2)
output = relay.Tuple([call_9163,const_9164,var_9165,const_9166,const_9167,var_9168,const_9169,bop_9174,])
output2 = relay.Tuple([call_9170,const_9164,var_9165,const_9166,const_9167,var_9168,const_9169,bop_9177,])
func_9178 = relay.Function([var_9165,var_9168,var_9173,], output)
mod['func_9178'] = func_9178
mod = relay.transform.InferType()(mod)
mutated_mod['func_9178'] = func_9178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9178_call = mutated_mod.get_global_var('func_9178')
var_9180 = relay.var("var_9180", dtype = "int32", shape = (60,))#candidate|9180|(60,)|var|int32
var_9181 = relay.var("var_9181", dtype = "float64", shape = (42, 6))#candidate|9181|(42, 6)|var|float64
var_9182 = relay.var("var_9182", dtype = "int32", shape = (6, 12, 2))#candidate|9182|(6, 12, 2)|var|int32
call_9179 = func_9178_call(var_9180,var_9181,var_9182,)
output = call_9179
func_9183 = relay.Function([var_9180,var_9181,var_9182,], output)
mutated_mod['func_9183'] = func_9183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7941_call = mod.get_global_var('func_7941')
func_7942_call = mutated_mod.get_global_var('func_7942')
call_9264 = relay.TupleGetItem(func_7941_call(), 0)
call_9265 = relay.TupleGetItem(func_7942_call(), 0)
func_6529_call = mod.get_global_var('func_6529')
func_6531_call = mutated_mod.get_global_var('func_6531')
call_9296 = relay.TupleGetItem(func_6529_call(), 0)
call_9297 = relay.TupleGetItem(func_6531_call(), 0)
output = relay.Tuple([call_9264,call_9296,])
output2 = relay.Tuple([call_9265,call_9297,])
func_9298 = relay.Function([], output)
mod['func_9298'] = func_9298
mod = relay.transform.InferType()(mod)
output = func_9298()
func_9299 = relay.Function([], output)
mutated_mod['func_9299'] = func_9299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6154_call = mod.get_global_var('func_6154')
func_6156_call = mutated_mod.get_global_var('func_6156')
call_9304 = relay.TupleGetItem(func_6154_call(), 0)
call_9305 = relay.TupleGetItem(func_6156_call(), 0)
output = call_9304
output2 = call_9305
func_9335 = relay.Function([], output)
mod['func_9335'] = func_9335
mod = relay.transform.InferType()(mod)
output = func_9335()
func_9336 = relay.Function([], output)
mutated_mod['func_9336'] = func_9336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7805_call = mod.get_global_var('func_7805')
func_7806_call = mutated_mod.get_global_var('func_7806')
call_9395 = relay.TupleGetItem(func_7805_call(), 0)
call_9396 = relay.TupleGetItem(func_7806_call(), 0)
output = relay.Tuple([call_9395,])
output2 = relay.Tuple([call_9396,])
func_9400 = relay.Function([], output)
mod['func_9400'] = func_9400
mod = relay.transform.InferType()(mod)
mutated_mod['func_9400'] = func_9400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9400_call = mutated_mod.get_global_var('func_9400')
call_9401 = func_9400_call()
output = call_9401
func_9402 = relay.Function([], output)
mutated_mod['func_9402'] = func_9402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5659_call = mod.get_global_var('func_5659')
func_5660_call = mutated_mod.get_global_var('func_5660')
call_9456 = relay.TupleGetItem(func_5659_call(), 0)
call_9457 = relay.TupleGetItem(func_5660_call(), 0)
output = call_9456
output2 = call_9457
func_9461 = relay.Function([], output)
mod['func_9461'] = func_9461
mod = relay.transform.InferType()(mod)
mutated_mod['func_9461'] = func_9461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9461_call = mutated_mod.get_global_var('func_9461')
call_9462 = func_9461_call()
output = call_9462
func_9463 = relay.Function([], output)
mutated_mod['func_9463'] = func_9463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7162_call = mod.get_global_var('func_7162')
func_7163_call = mutated_mod.get_global_var('func_7163')
call_9576 = func_7162_call()
call_9577 = func_7162_call()
func_7637_call = mod.get_global_var('func_7637')
func_7639_call = mutated_mod.get_global_var('func_7639')
call_9595 = relay.TupleGetItem(func_7637_call(), 1)
call_9596 = relay.TupleGetItem(func_7639_call(), 1)
output = relay.Tuple([call_9576,call_9595,])
output2 = relay.Tuple([call_9577,call_9596,])
func_9610 = relay.Function([], output)
mod['func_9610'] = func_9610
mod = relay.transform.InferType()(mod)
mutated_mod['func_9610'] = func_9610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9610_call = mutated_mod.get_global_var('func_9610')
call_9611 = func_9610_call()
output = call_9611
func_9612 = relay.Function([], output)
mutated_mod['func_9612'] = func_9612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6551_call = mod.get_global_var('func_6551')
func_6552_call = mutated_mod.get_global_var('func_6552')
call_9634 = relay.TupleGetItem(func_6551_call(), 1)
call_9635 = relay.TupleGetItem(func_6552_call(), 1)
func_2765_call = mod.get_global_var('func_2765')
func_2774_call = mutated_mod.get_global_var('func_2774')
const_9649 = relay.const([9,-9,-7,10,4,-4,9,-3,-1,10,-8,7,2,6,-4,4,4,-8,-8,10,2,-9,7,2,1,-5,-10,-4,6,-2,-4,2,2,1,-2,-6,-5,5,-8,-2,-7,-9,-9,9,4,6,10,8,-9,3,-9,6,-3,6,10,-2,4,5,-6,-9,-6,10,2,-9,6,4,3,9,-3,-9,10,-1,5,-8,-8,3,1,-1,1,5,4,-5,3,4,9,-10,-9,5,-5,-4,1,9,1,6,2,1,5,4,2,-4,3,1,-5,5,1,-4,-7,4,-7,-1,-4,-4,8,6,5,-10,4,-10,8,-10,5,1,1,9,8,6,2,-2,7,2,-10,10,-4,4,4,-10,9,10,-7,-7,-8,-8,2,-3,-9,-1,-7,-2,9,-2,-1,-1,-4,-10,9,7,-2,-2,-6,-5,9,-2,7,9,2,-1,8,3,3,4,-3,-3,-7,-1,-9,-7,-4,-7,5,-9,1,-9,-3,10,6,-10,-4,-5,-8,-3,-5,-5,1,10,-10,-4,8,-10,8,9,-2,4,-3,-9,7,8,-4,1,-7,-5,9,-9,-5,-9,9,-6,8,8,-10,2,3,-1,5,4,2,-2,-9,9,-2,-6,6,-3,-3,-6,10,-4,8,-1,9,8,5,4,2,9,-10,6,-6,-10,2,3,4,6,-5,6,10,-5,3,-10,-3,-1,-5,-10,-6,1,-6,9,-4,-1,-9,2,10,-8,-9,10,-9,-6,7,-5,-6,-10,-3,-2,3,-5,-10,-6,6,-5,-4,6,7,-10,-10,7,1,8,-8,10,-4,8,4,4,9,3,-6,9,-3,-10,-3,-8,-6,-10,-9,-8,7,-6,-1,9,2,5,2,-1,-4,7,10,6,4,-10,6,3,-5,4,-9,-8,-8,-9,9,-7,-3,-2,2,8,-4,6,-8,5,7,-9,-6,-9,10,-7,10,-3,10,5,-3,-7,-1,9,1,-1,7,9,7,-8,-6,7,6,-6,-5,-8,3,-9,8,2,-4,-2,-4,-4,6,9,4,-7,-6,-9,-3,-1,-2,-1,-10,10,7,-5,-2,2,-1,-10,-9,-7,10,-9,-5,-1,3,-7,-6,-7,10,4,2,-10,10,-8,-8,7,-3,3,7,4,8,2,-10,-1,-10,-2,4,3,-3,5,10,-7,8,-2,6,6,-9,1,7,10,6,8,-4,-4,-6,8,2,-10,7,-5,9,-8,10,-6,1,4,7,-9,-5,-10,3,6,3,-6,-9,3,4,6,3,3,-7,-3,-9,9,-7,-4,5,6,7,8,4,-3,5,4,-1,-9,-4,-7,5,4,3,2,7,5,1,9,5,6,1,-7,7,-5,10,-1,-7,7,-2,-7,-1,10,-8,-9,-2,4,-5,10,-6,-4,-6,-1,9,-3,1,9,-6,5,-9,-8,9,6,2,-7,-10,7,5,1,10,-6,-5,4,-7,7,1,-9,-7,6,3,-10,-6,1,6,7,5,6,2,3,-7,5,6,-2,-1,4,2,8,-10,-1,-2,-2,-4,9,8,-5,-4,7,-6,-5,-5,-2,-3,-7,3,9,8,2,-10,8,-7,-5,5,3,10,8,-6,-4,-5,10,-3,-1,2,3,-8,-2,-5,-6,-10,2,6,5,4,-9,-4,-5,9,8,-3,5,-3,4,5,-10,8,5,4,6,-3,5,5,4,9,-7,-2,-4,9,-5,-10,9,7,-2,6,-10,-4,-6,-6,4,4,-8,4,-1,9,-9,-1,7,-4,10,8,1,-5,-10,9,6,5,-10,-3,-2,-9,1,1,7,-6,5,4,-7,-5,10,1,7,-10,-3,-10,-7,-7,-6,-6,-2,-7,-8,5,10,10,-3,-5,-5,7,-10,-4,-5,-3,9,-3,2,10,-3,-3,4,-4,-4,-9,-4,8,3,-8,5,9,-3,-5,-2,-4,1,-7,-3,-3,-10,8,9,7,-10,-10,10,-6,-2,7,7,9,1,2,9,-10,8,-2,-4,8,-5,8,2,10,7,9,1,10,6,-5,-7,-1,-3,-1,3,2,2,5,3,7,3,2,4,5,5,-4,-6,-9,-9,9,-2,9,-10,7,10,-3,-9,-6,-8,4,2,8,-4], dtype = "uint32")#candidate|9649|(784,)|const|uint32
var_9650 = relay.var("var_9650", dtype = "int32", shape = (60,))#candidate|9650|(60,)|var|int32
const_9651 = relay.const([10,-7,-10,-2,-1,-7,-7,-1,-2,-4,-5,3,-8,5,-7,-7,8,4,6,-3,3,3,4,10,6,-10,-7,-6,4,-6,-8,9,-10,5,1,4,-1,5,-10,1,9,6,-6,2,4,10,5,-9,4,-9,-4,-10,-2,10,8,-6,3,-4,2,9,-3,7,8,-1,10,9,6,8,-4,8,2,-10,7,5,9,-5,-1,-10,-10,5,-4,-3,6,8,4,6,1,-10,-2,-8,-7,3,9,10,8,-9,-2,3,-6,9,-7,5,-3,-6,9,3,-9,5,4,7,-1,-4,-9,-10,-10,-6,-6,-6,-7,1,8,-2,-4,5,4,-2,8,-9,-5,-3,-10,3,-1,4,-3,4,10,-8,-4,-4,7,-3,-2,-2,-1,-3,8,-6,8,9,-4,-3,-8,3,-8,-10,3,-7,-8,-5,6,2,5,-4,-6,4,-5,-6,-10,7,-6,-2,-2,7,10,1,-9,1,-8,6,-10,-6,9,-8,-1,-8,1,9,1,-3,5,8,-4,-9,-7,-8,7,-10,8,-7,2,-7,7,6,1,10,3,1,10,2,6,2,6,10,-1,-2,-4,4,6,-9,9,-6,-9,2,8,7,-3,-7,-3,4,4,5,-6,9,-10,10,10,-4,2,10,-7,4,-6,-3,-8,10,-1,-9,-5,1,-1,-7,-9,-1,4,-3,-6,2,-7,-10,-10,-6,5,-1,8,-6,-7,9,1,-8,-1,7,-9,-1,4,1,10,-8,-5,-5,-3,1,3,5,-9,-10,-6,-8,-6,1,-8,5,-10,-5,3,9,1,3,7,2,1,-6,9,-1,-5,-8,-3,-3,7,1,5,4,-7,2,7,1,5,6,-5,2,9,3,2,-6,-1,9,-4,-4,1,6,1,9,-9,2,2,-2,-4,3,-8,-3,8,6,6,-5,-7,7,2,-6,1,-3,-1,-3,9,-1,9,-7,-7,-8,-3,9,8,10,10,-1,3,3,10,-1,6,-5,5,1,-4,-4,-4,9,-7,-1,4,-9,5,-2,-9,-3,4,-1,9,2,3,-2,-7,10,-9,-2,-3,9,4,-5,6,-10,-6,-1,3,10,-9,2,3,-1,-2,-5,-3,-5,8,10,7,-8,10,-10,5,8,2,10,-1,6,-4,-10,-5,-4,4,1,-5,-4,8,-2,4,7,-2,-1,-9,-8,-10,-2,3,2,-1,9,-9,4,7,-10,-6,8,5,-2,-10,7,-1,7,-4,-1,1,4,-1,9,2,10,6,5,7,4,-10,-7,10,2,4,-1,-3,5,3,3,-3,3,-9,1,-8,5,-7,-6,8,-1,5,-9,8,4,10,-7,10,-2,-10,7,9,-5,-4,-1,3,9,7,6,-2,7,6,4,-5,5,9,-3,-3,5,1,4,-10,-2,10,2,-8,3,4,2,-6,-3,10,-5,6,2,6,3,-8,-4,-3,-10,7,7,-3,-9,5,-3,-9,7,8,5,5,1,3,2,4,-8,-5,10,-1,6,10,10,10,5,7,4,-7,5,-2,5,9,5,-8,4,2,5,3,-3,3,1,-7,-1,-1,4,5,7,5,-10,7,-2,7,-2,5,3,3,-7,10,5,-6,5,2,-5,-6,-10,2,1,-1,10,-8,3,9,-2,-8,4,-9,7,-3,-8,9,9,2,-1,-4,-7,5,4,10,7,-6,-5,-10,-4,-5,1,10,5,1,-5,8,9,-3,-7,2,4,5,-1,-10,-7,7,8,9,3,1,8,1,-3,2,-9,6,-2,-3,-5,8,-7,-3,6,10,3,-7,-9,8,-3,1,-5,-7,7,10,2,-7,4,-6,9,8,-5,3,-3,5,-1,2,-5,-5,-9,-4,2,2,1,-6,3,-4,-1,2,8,-4,6,-7,4,-3,8,4,1,5,5,4,-9,4,-5,-6,6,4,-5,-4,4,2,5,1,3,7,1,-5,10,-2,8,8,9,9,-6,1,-8,-3,8,-10,3,-10,-9,-5,-4,3,-7,9,4,8,-1,-1,1,-4,7], dtype = "int8")#candidate|9651|(756,)|const|int8
const_9652 = relay.const([[-3.907038,7.957099,0.446276,9.243239,8.194213,-3.094959,4.331310,-6.225438],[3.419239,1.545449,-3.018898,-7.793841,-8.844423,1.250945,-6.577904,-7.535815],[-9.159029,-9.090672,-0.890561,6.286386,1.391294,-6.971406,4.024223,7.402716],[4.133568,-2.660870,-3.232045,6.852717,-6.353563,1.623022,-4.373846,2.733948],[6.426896,-6.687275,0.757816,1.982907,-2.269612,2.095743,-7.988827,-2.630662],[-7.773764,-0.263402,0.630475,7.539599,-1.494361,-4.253140,-5.224160,0.959018],[-9.728043,-2.298418,6.333793,-8.291479,0.389653,8.563432,-9.209621,3.176073],[-3.926698,6.348635,9.291609,1.816383,9.431038,-7.042245,3.988947,6.906836],[-5.663140,2.952665,6.115812,1.228351,-4.647500,3.751886,-8.820199,9.829278],[-9.402361,-7.516767,8.941217,3.240455,-2.747375,-2.932697,8.061599,9.067649],[8.324146,2.256473,-6.846438,4.390572,3.046741,2.462417,5.368063,-3.781050],[-4.332338,-6.199715,-8.684877,-4.312106,2.890679,-7.302543,3.883850,-4.255894],[-0.023040,8.323996,-9.270901,6.458106,0.820765,2.210801,1.787921,-3.783491],[6.793013,6.634834,-0.980060,-5.118104,2.090343,-1.299728,-9.563262,2.996432],[-9.082781,6.425003,-6.356419,-4.179880,1.369067,-4.501801,6.332205,-1.162745],[0.992614,-9.563776,-3.711748,-5.545885,9.203490,-8.801224,6.638968,0.498874],[-7.354730,2.197147,6.224466,7.286654,9.079840,-8.665803,-3.489555,2.401894],[-1.956640,-3.232189,-8.738595,-3.894031,6.797482,7.468451,2.841870,3.049487],[1.155848,-7.357209,-3.600438,-3.695141,3.362395,4.028186,6.053292,-6.503617],[-5.699823,-7.818696,0.051773,0.929572,9.783231,7.673493,4.419093,5.852026],[1.359169,2.347982,2.692656,-2.630576,-7.286724,-5.629850,-4.822594,-0.777006],[5.846785,-6.883194,5.875786,-8.972923,-8.051517,5.549835,-5.712946,3.601854],[-6.273884,7.263894,-2.013368,4.409730,2.261294,-1.469762,-9.534723,0.246526],[-6.736932,-8.773258,8.757935,-8.499167,-9.767450,4.766495,-0.432802,8.662715]], dtype = "float64")#candidate|9652|(24, 8)|const|float64
const_9653 = relay.const([[6.836472,-4.753765,6.596000,-8.338471,-5.948961,-6.484592,-1.538625,6.347401,-8.380810,2.917432,-5.229081,-4.450505,-9.187110,8.179768,5.640144,-0.990895,5.018740,-3.156221,4.396279,9.528378,4.532844,-7.797771,3.596117,5.002878,-3.281990,7.094915,-1.817901,-6.861978,-6.681768,-5.586438,0.849577,-6.565764,1.746293,1.161282,2.269605,-0.361478,7.193183,-1.916669,9.252908,-0.042128,-8.658093,-6.942646,0.839549,-7.440949,-0.068652,3.939921,4.447024,6.602324,-6.691115,-3.621614,1.248416,9.734456,0.237098,-2.001576,8.758459,-3.435939,-6.400714,-1.747306,0.683340,6.084845,9.636066,8.784938,-2.001325,1.001513,-4.795027,-5.200364,8.192674,-7.393046,-1.635957,7.335125,9.021842,7.254599,-5.663140,2.820249,-9.597526,-5.142032,3.867227,0.425479,-2.031716,-3.580005,-0.073379,-5.971793,-0.060217,-4.405998],[5.723491,-3.773125,-5.608689,3.177999,-6.444529,-9.518325,4.597602,-2.477182,9.291185,0.172000,2.432202,-8.027496,-4.312050,2.672156,1.505239,0.151292,1.350847,4.508949,-1.244942,-1.338888,8.235254,7.083286,5.083062,5.044473,2.647535,-6.709034,-1.346801,-2.013725,-1.202385,-4.517689,-7.022979,-4.598093,5.394616,2.322090,-9.305902,-8.921416,-4.903206,0.233509,-9.871114,-5.603318,0.536315,-5.056529,6.743669,-7.992587,-1.859395,5.963136,1.690246,-3.314424,3.645157,-6.445222,3.035475,2.349787,-2.267975,-7.351046,6.255023,6.152535,6.142175,8.878268,-2.719085,-0.252688,-5.428657,0.827601,-1.711786,-7.647684,7.655691,2.976693,-4.227937,9.989345,7.126144,5.875451,-4.186037,0.209038,-1.540355,9.870461,9.890647,9.675420,4.359584,6.874891,-8.624192,-2.549424,-4.299308,-1.331519,-2.580664,4.589749],[2.782622,1.678296,1.392963,-9.581166,3.954765,9.685170,7.116184,-1.677574,3.854037,-5.195555,1.707491,-5.972200,1.199964,-7.308020,-7.762135,2.226671,-4.662612,4.289439,-8.787436,8.075742,3.522428,-7.310072,1.036775,-7.421374,-3.386820,-2.196120,8.897306,9.767026,-7.619126,-9.256766,2.257877,-1.544152,-2.995215,-1.481457,6.094828,-5.691512,-1.088665,-5.416513,8.359885,-1.493200,2.532730,-0.505084,5.821404,7.301679,6.712222,-0.938204,-0.984585,1.776242,3.780426,4.878220,1.523015,9.667709,-9.510477,-3.402482,-5.412037,0.773458,4.981518,-8.153684,9.321552,-3.939825,-7.265158,0.465424,-4.471142,5.035412,-2.355604,-7.907840,2.131386,1.223313,8.309171,9.828134,4.183328,-2.565847,-9.970132,2.217601,-0.123441,2.071347,5.915775,6.275517,8.703052,9.085833,7.667442,7.136577,3.814054,-0.752906]], dtype = "float64")#candidate|9653|(3, 84)|const|float64
var_9654 = relay.var("var_9654", dtype = "uint8", shape = (378,))#candidate|9654|(378,)|var|uint8
call_9648 = relay.TupleGetItem(func_2765_call(relay.reshape(const_9649.astype('uint32'), [8, 7, 14]), relay.reshape(const_9649.astype('uint32'), [8, 7, 14]), relay.reshape(var_9650.astype('int32'), [60,]), relay.reshape(const_9651.astype('int8'), [9, 84]), relay.reshape(const_9652.astype('float64'), [24, 8]), relay.reshape(const_9653.astype('float64'), [1, 252]), relay.reshape(var_9654.astype('uint8'), [378,]), ), 12)
call_9655 = relay.TupleGetItem(func_2774_call(relay.reshape(const_9649.astype('uint32'), [8, 7, 14]), relay.reshape(const_9649.astype('uint32'), [8, 7, 14]), relay.reshape(var_9650.astype('int32'), [60,]), relay.reshape(const_9651.astype('int8'), [9, 84]), relay.reshape(const_9652.astype('float64'), [24, 8]), relay.reshape(const_9653.astype('float64'), [1, 252]), relay.reshape(var_9654.astype('uint8'), [378,]), ), 12)
uop_9662 = relay.acos(const_9653.astype('float32')) # shape=(3, 84)
output = relay.Tuple([call_9634,call_9648,const_9649,var_9650,const_9651,const_9652,var_9654,uop_9662,])
output2 = relay.Tuple([call_9635,call_9655,const_9649,var_9650,const_9651,const_9652,var_9654,uop_9662,])
func_9666 = relay.Function([var_9650,var_9654,], output)
mod['func_9666'] = func_9666
mod = relay.transform.InferType()(mod)
var_9667 = relay.var("var_9667", dtype = "int32", shape = (60,))#candidate|9667|(60,)|var|int32
var_9668 = relay.var("var_9668", dtype = "uint8", shape = (378,))#candidate|9668|(378,)|var|uint8
output = func_9666(var_9667,var_9668,)
func_9669 = relay.Function([var_9667,var_9668,], output)
mutated_mod['func_9669'] = func_9669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7551_call = mod.get_global_var('func_7551')
func_7552_call = mutated_mod.get_global_var('func_7552')
call_9706 = func_7551_call()
call_9707 = func_7551_call()
output = call_9706
output2 = call_9707
func_9727 = relay.Function([], output)
mod['func_9727'] = func_9727
mod = relay.transform.InferType()(mod)
output = func_9727()
func_9728 = relay.Function([], output)
mutated_mod['func_9728'] = func_9728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7162_call = mod.get_global_var('func_7162')
func_7163_call = mutated_mod.get_global_var('func_7163')
call_9771 = func_7162_call()
call_9772 = func_7162_call()
const_9784 = relay.const([[[7,9],[10,2],[9,2],[-8,4],[-6,5],[-5,-2],[-1,7],[6,-5],[-4,9],[-2,5],[-2,5],[3,10]],[[-10,-7],[7,-3],[10,8],[6,9],[8,3],[10,-1],[-9,2],[8,1],[-10,2],[-8,8],[4,6],[-7,-9]],[[4,7],[2,-8],[-6,2],[4,-9],[-2,2],[5,1],[-5,-9],[-3,-7],[4,3],[-4,6],[-1,2],[-2,2]],[[4,-7],[3,10],[5,10],[10,5],[3,-10],[8,5],[-6,7],[-1,-5],[2,-6],[8,-2],[-5,-10],[-2,-9]],[[-4,-2],[-6,-4],[-5,2],[1,-3],[-9,-7],[-4,9],[3,-4],[-6,-2],[1,5],[-10,-2],[1,4],[-3,-2]],[[-3,1],[-1,-7],[-2,1],[-4,-10],[-6,4],[3,4],[-2,-3],[-3,-9],[-7,-6],[-1,-3],[1,-2],[-7,-2]]], dtype = "int32")#candidate|9784|(6, 12, 2)|const|int32
bop_9785 = relay.bitwise_and(call_9771.astype('uint16'), relay.reshape(const_9784.astype('uint16'), relay.shape_of(call_9771))) # shape=(6, 12, 2)
bop_9788 = relay.bitwise_and(call_9772.astype('uint16'), relay.reshape(const_9784.astype('uint16'), relay.shape_of(call_9772))) # shape=(6, 12, 2)
func_4053_call = mod.get_global_var('func_4053')
func_4056_call = mutated_mod.get_global_var('func_4056')
var_9798 = relay.var("var_9798", dtype = "float64", shape = (672,))#candidate|9798|(672,)|var|float64
call_9797 = func_4053_call(relay.reshape(var_9798.astype('float64'), [7, 16, 6]))
call_9799 = func_4053_call(relay.reshape(var_9798.astype('float64'), [7, 16, 6]))
output = relay.Tuple([bop_9785,call_9797,var_9798,])
output2 = relay.Tuple([bop_9788,call_9799,var_9798,])
func_9802 = relay.Function([var_9798,], output)
mod['func_9802'] = func_9802
mod = relay.transform.InferType()(mod)
var_9803 = relay.var("var_9803", dtype = "float64", shape = (672,))#candidate|9803|(672,)|var|float64
output = func_9802(var_9803)
func_9804 = relay.Function([var_9803], output)
mutated_mod['func_9804'] = func_9804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5648_call = mod.get_global_var('func_5648')
func_5649_call = mutated_mod.get_global_var('func_5649')
call_9816 = func_5648_call()
call_9817 = func_5648_call()
output = call_9816
output2 = call_9817
func_9818 = relay.Function([], output)
mod['func_9818'] = func_9818
mod = relay.transform.InferType()(mod)
output = func_9818()
func_9819 = relay.Function([], output)
mutated_mod['func_9819'] = func_9819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7441_call = mod.get_global_var('func_7441')
func_7442_call = mutated_mod.get_global_var('func_7442')
call_9820 = relay.TupleGetItem(func_7441_call(), 0)
call_9821 = relay.TupleGetItem(func_7442_call(), 0)
func_6706_call = mod.get_global_var('func_6706')
func_6709_call = mutated_mod.get_global_var('func_6709')
const_9832 = relay.const([-0.063552,4.047388,-3.610121,-6.474411,-2.785706,-2.792044,9.594480,1.153090,-4.659873,-3.065176,-2.895449,3.580113,7.513959,4.307877,2.396901,8.382202,3.543766,3.917115,1.118082,6.210955,4.920036,-1.778907,-5.461408,-1.630958,-2.782873,-5.642941,-8.183027,6.065031,0.571235,-6.102979,1.075965,-2.927161,6.015901,-4.591354,-7.889467,-7.905619,3.305252,-7.174409,-0.638015,-3.674496,5.339945,-7.894153,-2.841361,3.021839,-2.611812,-0.516030,5.240637,-3.629344,1.646144,3.336400,-5.399801,5.629702,9.105321,1.528088,-3.171894,-1.013701,-6.975581,0.348904,-1.139935,7.477764], dtype = "float32")#candidate|9832|(60,)|const|float32
const_9833 = relay.const([[2.363746,9.818775,2.919276,-4.910564,-7.252904,-6.911087,7.969165,2.215745,-5.632676,-2.996779,7.853782,-9.410897,4.706954,-3.244704,5.671133,-8.629008,-0.070827,4.942734,-4.487895,-8.465111,4.902280,-4.289352,-0.044734,6.161093,-0.423845,-9.120861,-9.975776,-6.764848,-4.731965,-3.988999,2.120632,-8.322890,-3.531106,-6.124788,8.866466,4.996234,4.813584,-6.308561,-6.109965,0.927686,3.380387,-2.067837,-0.641137,-3.669330,3.675129,-3.370280,5.735337,4.802406,5.964813,-1.600929,-2.624829,9.839620,-4.315535,6.177936,6.457201,2.940873,0.633792,1.661713,-8.110732,-9.531827,-9.555208,-9.178280,-1.950428,9.001100,0.750922,-3.697436,-4.120125,-8.083670,4.247561,7.438741,-7.400322,-7.133877,-7.448081,6.909907,6.276035,-7.121037,9.655265,1.006197,-5.159383,9.083745,7.461742,-5.082976,8.537204,-0.737919],[-1.144124,-9.806628,-9.278781,-6.065268,-0.384575,9.326943,-4.339915,3.239336,-1.094340,6.804036,9.011752,5.690507,-4.701837,-5.450846,-3.911373,1.133256,-4.636301,6.471306,-2.316312,9.089446,5.022378,-9.920275,7.291538,4.509605,-5.564012,-3.376092,8.402464,-2.134166,4.354044,-5.182784,4.520036,8.646228,0.466265,-5.100211,-8.554943,-5.257625,-3.141663,8.190425,-8.369200,-7.469848,6.160024,-2.898472,-7.869081,7.479060,-9.638011,8.220116,0.433998,8.737756,0.951146,-7.589237,-9.129529,9.721219,9.157370,-1.216809,-7.619718,-5.543303,3.789089,-5.792560,-8.212971,-0.692635,2.946697,-7.838511,-7.872783,1.707465,-7.434686,3.000781,-7.205456,4.072270,-0.179384,4.276795,-8.586846,-4.329409,4.126505,6.461450,-0.819951,-7.959910,1.127551,-3.599342,-7.284202,8.949715,7.718628,7.469769,-0.564759,7.137188],[-5.022494,4.152602,1.782580,0.930040,-3.828417,-9.259491,-4.680932,6.515593,9.820160,6.384418,9.565845,-0.428109,3.756417,5.253256,5.136199,-3.350496,7.530424,-9.869207,-4.256885,7.436301,3.813117,7.332612,-1.626145,2.922659,7.383018,-3.132319,-2.605683,4.314508,-9.433779,3.851508,-4.944861,-0.102174,6.495340,-3.790525,-8.076823,-4.427085,5.137478,5.318253,-3.774017,2.622975,2.582437,0.799661,0.865191,2.565950,5.842595,0.358771,7.429958,8.512847,-7.899446,-7.425888,-9.558769,-8.901605,-8.467769,6.920336,2.403893,-4.478453,-1.023057,-8.282244,0.967973,-7.166540,-1.676997,-7.673502,4.710845,-5.595300,7.753193,-4.163667,2.992760,0.479978,-6.023836,6.828763,3.813435,-7.410789,1.455332,8.808169,-6.281036,1.601119,1.338058,-2.975940,3.048506,5.572064,6.403088,-1.734079,-5.915239,6.063318],[9.239080,-2.485903,-3.904152,-0.126704,1.043369,-4.846889,5.029979,-4.428288,5.667559,3.281967,4.746217,4.202576,-4.269559,-5.778373,5.926239,6.721557,-7.006254,-0.668598,-6.147786,-6.102203,-1.264899,-5.982870,-4.172857,6.766769,9.519219,-2.481420,7.477218,-5.938413,-8.278460,-9.024098,-4.626078,-0.084829,-3.698065,2.914728,9.772126,-1.326323,6.461377,-7.455743,-6.232950,8.500774,-1.762607,-5.005501,-8.375564,-5.781596,6.211973,-8.106967,-0.342663,-0.399711,0.565703,-3.095462,5.217570,0.314100,0.361871,-0.403450,3.049934,1.257940,-1.500185,3.827187,-4.649841,8.015008,-5.623803,8.260683,-8.793897,0.811859,-9.719038,-1.017443,4.420774,-5.465395,7.668207,-6.186498,-4.421186,6.008707,3.391240,3.955858,-3.369557,-2.709624,2.017968,8.312094,3.143841,2.215012,-2.637341,-1.092919,5.301680,-2.879832],[1.361870,0.701354,2.292377,-2.313106,0.133681,-8.188408,-4.669694,7.575178,1.183361,0.257169,2.496833,-2.208155,4.164512,2.008252,7.283299,3.801383,-9.759176,-6.804995,6.978885,3.666636,3.714239,-6.187524,-4.863685,1.804545,8.826614,-1.533374,3.245748,-3.294212,2.126240,-6.149096,-6.380307,-5.801380,-9.053086,-9.425339,7.920363,5.664036,4.110711,7.285604,1.289846,5.726500,3.564478,3.675559,-0.610000,1.476811,-4.018866,-2.849861,-7.446281,4.486871,-6.855943,-9.407964,2.995816,-6.814940,-1.329675,-0.414959,-1.131166,-6.474207,-5.619050,-9.351438,4.272193,-8.933607,7.790805,-9.776676,8.163938,9.253161,1.386122,-6.081879,6.011637,-6.659431,-9.646901,9.957680,-5.138794,-1.903033,8.472620,-2.395399,2.544874,-6.941174,8.423944,-8.620257,7.412118,-6.311961,5.072670,4.655144,5.103613,-7.715045]], dtype = "float32")#candidate|9833|(5, 84)|const|float32
call_9831 = func_6706_call(relay.reshape(const_9832.astype('float32'), [12, 1, 5]), relay.reshape(const_9833.astype('float32'), [12, 7, 5]), )
call_9834 = func_6706_call(relay.reshape(const_9832.astype('float32'), [12, 1, 5]), relay.reshape(const_9833.astype('float32'), [12, 7, 5]), )
output = relay.Tuple([call_9820,call_9831,const_9832,const_9833,])
output2 = relay.Tuple([call_9821,call_9834,const_9832,const_9833,])
func_9837 = relay.Function([], output)
mod['func_9837'] = func_9837
mod = relay.transform.InferType()(mod)
output = func_9837()
func_9838 = relay.Function([], output)
mutated_mod['func_9838'] = func_9838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7805_call = mod.get_global_var('func_7805')
func_7806_call = mutated_mod.get_global_var('func_7806')
call_9861 = relay.TupleGetItem(func_7805_call(), 0)
call_9862 = relay.TupleGetItem(func_7806_call(), 0)
func_6218_call = mod.get_global_var('func_6218')
func_6220_call = mutated_mod.get_global_var('func_6220')
var_9868 = relay.var("var_9868", dtype = "float64", shape = (192,))#candidate|9868|(192,)|var|float64
call_9867 = relay.TupleGetItem(func_6218_call(relay.reshape(var_9868.astype('float64'), [192,])), 4)
call_9869 = relay.TupleGetItem(func_6220_call(relay.reshape(var_9868.astype('float64'), [192,])), 4)
func_8677_call = mod.get_global_var('func_8677')
func_8679_call = mutated_mod.get_global_var('func_8679')
call_9878 = relay.TupleGetItem(func_8677_call(), 0)
call_9879 = relay.TupleGetItem(func_8679_call(), 0)
func_6154_call = mod.get_global_var('func_6154')
func_6156_call = mutated_mod.get_global_var('func_6156')
call_9889 = relay.TupleGetItem(func_6154_call(), 0)
call_9890 = relay.TupleGetItem(func_6156_call(), 0)
func_6480_call = mod.get_global_var('func_6480')
func_6482_call = mutated_mod.get_global_var('func_6482')
call_9904 = relay.TupleGetItem(func_6480_call(), 1)
call_9905 = relay.TupleGetItem(func_6482_call(), 1)
output = relay.Tuple([call_9861,call_9867,var_9868,call_9878,call_9889,call_9904,])
output2 = relay.Tuple([call_9862,call_9869,var_9868,call_9879,call_9890,call_9905,])
func_9906 = relay.Function([var_9868,], output)
mod['func_9906'] = func_9906
mod = relay.transform.InferType()(mod)
var_9907 = relay.var("var_9907", dtype = "float64", shape = (192,))#candidate|9907|(192,)|var|float64
output = func_9906(var_9907)
func_9908 = relay.Function([var_9907], output)
mutated_mod['func_9908'] = func_9908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7406_call = mod.get_global_var('func_7406')
func_7407_call = mutated_mod.get_global_var('func_7407')
call_10062 = func_7406_call()
call_10063 = func_7406_call()
func_7610_call = mod.get_global_var('func_7610')
func_7612_call = mutated_mod.get_global_var('func_7612')
const_10065 = relay.const([6,1,1,-7,-4,9,7,3,-5,9,2,9,-2,-5,9,-4,-9,2,-10,3,4,-1,-9,2,-5,-10,-5,-4,-3,6,10,7,-2,1,10,7,5,-8,4,-6,2,-5,5,6,8,-10,-1,-8,-7,-6,-3,4,2,-4,-1,5,-8,-2,10,3,-9,6,1,2,5,7,-10,-7,3,1,4,9,8,7,9,-6,4,-8,-8,-4,-8,-2,-4,-3,2,2,1,8,-5,7,-6,2,-7,-4,1,-7,-9,-7,7,9,-5,-7,-2,-4,-1,-3,-6,-4,5,7,6,-3,4,-7,2,-2,8,-3,-4,9,10,2,-7,8,-4,8,-10,4,-2,8,-8,-1,10,9,1,-1,10,-6,10,8,10,4,8,-5,-9,-4,-5,-5,1,1,2,4,5,-10,5,-9,-4,6,-10,-4,-5,-8,-5,3,7,-7,-8,-2,10,-8,-9,-9,-1,-7,-5,-2,9,-9,2,-10,8,9,-6,-10,2,1,-6,-4,-5,-8,2,-9,1,-5,1,-4,-1,-8,-4,3,-6,-7,5,1,-2,10,-10,-3,8,4,3,2,-2,3,7,-4,-2,-9,-10,-9,-9,4,-8,10,7,7,1,6,-8,-1,-6,-1,-4,9,1,6,-7,-9,1,2,3,-2,9,-10,-8,5,8,6,8,-7,3,1,8,-6,-9,-9,-10,-9,-8,7,3,-1,9,2,3,8,-3,-8,9,9,2,2,-6,2,-1,-1,-2,3,10,-1,-5,10,6,-8,-10,2,-5,-6,3,-7,7,-1,10,10,-9,4,-10,3,-4,8,8,-8,2,5,1,4,-8,7,-8,10,10,3,-10,-5,-9,-10,2,-1,-1,-4,6,10,-2,4,6,9,-7,5,1,4,4,7,2,-4,2,-5,7,-4,4,9,1,-5,2,-10,1,-1,7,-1,-5,2,-3,8,2,-9,2,-6,7,3,-1,-10,-4,7,10,10,3,5,-9,-5,6,9,3,-1,5,10,5,-10,3,-2,-5,8,-4,-3,-5,6,-2,1,8,-6,6,-3,-5,3,2,1,-8,7,-2,-7,-9,-8,7,6,1,-2,-7,-1,-10,10,-10,9,-2,1,7,10,-2,6,-10,-7,-4,10,-4,4,5,-5,-7,-2,3,2,1,5,-2,5,5,1,-10,3,-1,-7,-2,-1,7,9,-5,9,5,-1,6,7,7,5,10,-1,-4,7,-1,7,2,-7,9,4,9,-10,-3,-8,-4,8,-10,5,9,2,-2,7,8,-10,-7,10,-2,-3,-7,7,-4,5,6,-8,4,3,2,10,4,-7,-8,9,9,-5,2,8,-9,-8,3,-9,7,-2,4,8,-6,8,-4,-4,-8,-1,-2,-4,2,-3,-9,1,-4,6,-7,-5,9,-6,10,-8,-8,-9,-8,1,-5,2,-9,-2,5,3,2,6,-1,6,2,-2,-3,-3,3,10,10,-4,4,-4,-3,1,-4,9,-9,9,-9,2,-1,4,8,-6,3,-7,-7,5,5,7,3,5,1,3,-6,-3,-9,2,8,-6,-9,9,2,-6,-2,-8,-9,8,8,9,6,10,-8,3,-2,8,-1,-5,-2,2,6,-10,-5,-4,-2,7,-4,5,1,7,-8,5,5,-2,1,-3,-6,-1,-3,-5,7,-3,1,2,-8,7,7,3,2,-10,-1,-1,8,-9,-8,-6,-6,-5,-8,3,9,2,-2,9,-2,8,-4,2,10,2,4,2,-6,-9,7,10,3,-1,9,-8,10,4,-2,3,8,1,-3,3,1,4,5,-1,6,-1,3,5,5,7,-6,1,-8,-5,5,-8,2,-4,6,3,-9,-6,-6,-8,-10,10,5,-1,6,-2,6,9,4,4,9,3,-4,2,7,2,-5,3,-8,5,-2,6,8,5,1,3,7,-9,4,2,3,9,8,10,-6,-9,1,-6,3,3,1,3,4,8,5,-9,3,6,10,5,-10,-6,-10,-10,-6,-6,-10,2,2,2,-9,8,9,-3,-2,6,-3,-3], dtype = "int8")#candidate|10065|(756,)|const|int8
call_10064 = relay.TupleGetItem(func_7610_call(relay.reshape(const_10065.astype('int8'), [756,])), 1)
call_10066 = relay.TupleGetItem(func_7612_call(relay.reshape(const_10065.astype('int8'), [756,])), 1)
func_9335_call = mod.get_global_var('func_9335')
func_9336_call = mutated_mod.get_global_var('func_9336')
call_10085 = func_9335_call()
call_10086 = func_9335_call()
uop_10118 = relay.cosh(call_10064.astype('float32')) # shape=(9, 3, 13)
uop_10120 = relay.cosh(call_10066.astype('float32')) # shape=(9, 3, 13)
func_9461_call = mod.get_global_var('func_9461')
func_9463_call = mutated_mod.get_global_var('func_9463')
call_10129 = func_9461_call()
call_10130 = func_9461_call()
output = relay.Tuple([call_10062,const_10065,call_10085,uop_10118,call_10129,])
output2 = relay.Tuple([call_10063,const_10065,call_10086,uop_10120,call_10130,])
func_10131 = relay.Function([], output)
mod['func_10131'] = func_10131
mod = relay.transform.InferType()(mod)
output = func_10131()
func_10132 = relay.Function([], output)
mutated_mod['func_10132'] = func_10132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10131_call = mod.get_global_var('func_10131')
func_10132_call = mutated_mod.get_global_var('func_10132')
call_10168 = relay.TupleGetItem(func_10131_call(), 1)
call_10169 = relay.TupleGetItem(func_10132_call(), 1)
output = relay.Tuple([call_10168,])
output2 = relay.Tuple([call_10169,])
func_10174 = relay.Function([], output)
mod['func_10174'] = func_10174
mod = relay.transform.InferType()(mod)
mutated_mod['func_10174'] = func_10174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10174_call = mutated_mod.get_global_var('func_10174')
call_10175 = func_10174_call()
output = call_10175
func_10176 = relay.Function([], output)
mutated_mod['func_10176'] = func_10176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9818_call = mod.get_global_var('func_9818')
func_9819_call = mutated_mod.get_global_var('func_9819')
call_10199 = func_9818_call()
call_10200 = func_9818_call()
func_7406_call = mod.get_global_var('func_7406')
func_7407_call = mutated_mod.get_global_var('func_7407')
call_10201 = func_7406_call()
call_10202 = func_7406_call()
output = relay.Tuple([call_10199,call_10201,])
output2 = relay.Tuple([call_10200,call_10202,])
func_10209 = relay.Function([], output)
mod['func_10209'] = func_10209
mod = relay.transform.InferType()(mod)
output = func_10209()
func_10210 = relay.Function([], output)
mutated_mod['func_10210'] = func_10210
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10263 = relay.var("var_10263", dtype = "int64", shape = ())#candidate|10263|()|var|int64
var_10264 = relay.var("var_10264", dtype = "int64", shape = (1, 10, 12))#candidate|10264|(1, 10, 12)|var|int64
bop_10265 = relay.maximum(var_10263.astype('int64'), var_10264.astype('int64')) # shape=(1, 10, 12)
bop_10269 = relay.divide(var_10264.astype('float64'), var_10263.astype('float64')) # shape=(1, 10, 12)
bop_10273 = relay.logical_or(var_10264.astype('bool'), relay.reshape(bop_10269.astype('bool'), relay.shape_of(var_10264))) # shape=(1, 10, 12)
func_1356_call = mod.get_global_var('func_1356')
func_1360_call = mutated_mod.get_global_var('func_1360')
var_10280 = relay.var("var_10280", dtype = "int8", shape = (1408,))#candidate|10280|(1408,)|var|int8
call_10279 = relay.TupleGetItem(func_1356_call(relay.reshape(var_10280.astype('int8'), [11, 8, 16]), relay.reshape(var_10280.astype('int8'), [11, 8, 16]), ), 1)
call_10281 = relay.TupleGetItem(func_1360_call(relay.reshape(var_10280.astype('int8'), [11, 8, 16]), relay.reshape(var_10280.astype('int8'), [11, 8, 16]), ), 1)
output = relay.Tuple([bop_10265,bop_10273,call_10279,var_10280,])
output2 = relay.Tuple([bop_10265,bop_10273,call_10281,var_10280,])
func_10295 = relay.Function([var_10263,var_10264,var_10280,], output)
mod['func_10295'] = func_10295
mod = relay.transform.InferType()(mod)
mutated_mod['func_10295'] = func_10295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10295_call = mutated_mod.get_global_var('func_10295')
var_10297 = relay.var("var_10297", dtype = "int64", shape = ())#candidate|10297|()|var|int64
var_10298 = relay.var("var_10298", dtype = "int64", shape = (1, 10, 12))#candidate|10298|(1, 10, 12)|var|int64
var_10299 = relay.var("var_10299", dtype = "int8", shape = (1408,))#candidate|10299|(1408,)|var|int8
call_10296 = func_10295_call(var_10297,var_10298,var_10299,)
output = call_10296
func_10300 = relay.Function([var_10297,var_10298,var_10299,], output)
mutated_mod['func_10300'] = func_10300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9461_call = mod.get_global_var('func_9461')
func_9463_call = mutated_mod.get_global_var('func_9463')
call_10374 = func_9461_call()
call_10375 = func_9461_call()
output = relay.Tuple([call_10374,])
output2 = relay.Tuple([call_10375,])
func_10387 = relay.Function([], output)
mod['func_10387'] = func_10387
mod = relay.transform.InferType()(mod)
output = func_10387()
func_10388 = relay.Function([], output)
mutated_mod['func_10388'] = func_10388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5899_call = mod.get_global_var('func_5899')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_10430 = relay.TupleGetItem(func_5899_call(), 0)
call_10431 = relay.TupleGetItem(func_5901_call(), 0)
output = call_10430
output2 = call_10431
func_10445 = relay.Function([], output)
mod['func_10445'] = func_10445
mod = relay.transform.InferType()(mod)
mutated_mod['func_10445'] = func_10445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10445_call = mutated_mod.get_global_var('func_10445')
call_10446 = func_10445_call()
output = call_10446
func_10447 = relay.Function([], output)
mutated_mod['func_10447'] = func_10447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7406_call = mod.get_global_var('func_7406')
func_7407_call = mutated_mod.get_global_var('func_7407')
call_10503 = func_7406_call()
call_10504 = func_7406_call()
uop_10514 = relay.cos(call_10503.astype('float64')) # shape=(6, 12, 2)
uop_10516 = relay.cos(call_10504.astype('float64')) # shape=(6, 12, 2)
output = relay.Tuple([uop_10514,])
output2 = relay.Tuple([uop_10516,])
func_10539 = relay.Function([], output)
mod['func_10539'] = func_10539
mod = relay.transform.InferType()(mod)
output = func_10539()
func_10540 = relay.Function([], output)
mutated_mod['func_10540'] = func_10540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7870_call = mod.get_global_var('func_7870')
func_7871_call = mutated_mod.get_global_var('func_7871')
call_10586 = relay.TupleGetItem(func_7870_call(), 1)
call_10587 = relay.TupleGetItem(func_7871_call(), 1)
func_5457_call = mod.get_global_var('func_5457')
func_5459_call = mutated_mod.get_global_var('func_5459')
const_10592 = relay.const(-5, dtype = "int8")#candidate|10592|()|const|int8
call_10591 = func_5457_call(relay.reshape(const_10592.astype('int8'), []))
call_10593 = func_5457_call(relay.reshape(const_10592.astype('int8'), []))
func_7941_call = mod.get_global_var('func_7941')
func_7942_call = mutated_mod.get_global_var('func_7942')
call_10618 = relay.TupleGetItem(func_7941_call(), 0)
call_10619 = relay.TupleGetItem(func_7942_call(), 0)
func_6808_call = mod.get_global_var('func_6808')
func_6811_call = mutated_mod.get_global_var('func_6811')
const_10626 = relay.const([[True,True,False],[False,True,True],[True,True,False],[False,False,False],[False,True,True],[True,True,True],[True,True,False],[True,True,True],[True,False,False],[True,False,True],[False,True,True],[True,True,False],[False,False,True],[False,False,True],[False,False,True],[False,False,False],[True,True,True],[True,False,False],[False,True,False],[True,True,True],[False,True,False],[True,False,False],[True,False,False],[True,False,True],[False,True,True],[True,True,True],[False,False,False],[True,True,False],[False,False,False],[False,True,True],[True,True,False],[False,True,True],[False,False,True],[False,True,False],[True,False,True],[True,True,False],[False,True,False],[True,True,True],[True,True,True],[True,True,False],[False,True,False],[True,True,True],[False,True,True],[True,True,True],[True,True,True],[False,False,False],[False,False,False],[False,True,True],[False,True,False],[True,False,True],[False,True,False],[False,False,True],[True,False,False],[False,True,False],[True,True,True],[False,True,True],[True,False,True],[True,False,True],[False,False,False],[False,False,False],[True,False,True],[False,False,True],[True,True,True],[False,True,True],[False,True,False],[True,True,True],[False,False,True],[True,True,False],[False,True,False],[False,True,False],[True,True,False],[False,True,False],[False,False,True],[True,False,True],[False,False,False],[False,True,True],[False,True,False],[True,True,True],[True,True,True],[False,False,False],[False,True,True],[True,True,False],[True,True,True],[True,True,True],[False,True,False],[False,False,True],[True,False,True],[True,True,False],[True,True,True],[False,True,True],[False,True,False],[False,False,False],[False,False,True],[True,True,False],[True,True,False],[True,True,False],[False,False,False],[True,False,True],[True,True,False],[True,True,True],[False,True,True],[True,True,True],[True,False,True],[False,True,False],[True,False,True],[True,True,False],[True,False,True],[True,True,True],[False,True,False],[True,False,True],[False,False,False],[True,True,False],[True,False,False],[False,True,True],[True,False,False],[False,True,True],[True,False,True]], dtype = "bool")#candidate|10626|(117, 3)|const|bool
const_10627 = relay.const([-8,4,6,3,10,5,7,6,3,10,-4,-5,-3,9,4,10,-6,3,2,1,-7,2,2,4,9,-5,7,2,-6,6,5,-1,2,-3,3,-8,10,-6,10,-8,-4,-6,4,4,6,-10,-8,4,-7,6,-2,-10,-6,5,-6,7,-7,-2,-10,10,6,9,-1,4,9,-7,6,-3,2,8,-2,-8,9,-9,6,-5,9,8,6,-7,-4,7,-10,2,-10,-1,-9,-1,-1,-7,8,-3,7,-7,5,-1,-8,1,-9,-1,-3,-1,-1,1,3,-1,2,-7,5,-4,-10,1,3,8,-3,3,3,-10,-8,-8,-9,-1,-1,1,-4,8,2,-4,9,9,4,10,7,2,9,4,7,10,-6,7,6,6,3,2,-3,-4,4,4,3,7,-4,-1,-8,2,-2,4,2,-7,-9,7,-2,10,-6,-5,8,1,5,-4,3,-5,-5,-6,-6,-4,-1,-8,3,-9,2,-9,8,-4,-2,-3,6,-3,-6,10,1,10,6,-7,6,1,1,-10,-10,1,-5,-8,-4,-4,9,6,-1,-1,4,9,3,-10,7,-5,-6,-8,3,-4,8,-1,5,4,4,2,-5,-10,10,-5,1,4,8,-10,2,10,-3,5,-10,1,-6,4,3,-10,-3,10,4,-3,9,-5,-9,-9,8,8,4,-4,4,2,1,2,8,9,-9,-6,8,-9,6,7,1,4,7,-8,5,10,-3,-1,6,2,-4,4,-10,9,1,4,5,9,-7,3,-6,-7,7,9,7,9,-4,5,5,1,-2,-8,-4,-9,4,2,-6,1,8,7,3,-9,10,-10,6,1,-10,-4,-7,-5,4,-1,8,-4,-3,-2,-6,3,2,10,-9,-7,1,-1,-6,-9,4,1,-3,-8,3,-3,10,-6,3,2,9,1,3,-8,10,9,9,-6,2,-9,4,5,-9,-6,-9,2,-10,-9,5,-1,-7,9,-8,-8,-10,5,-8,10,1,8,6,7,-5,10,6,-6,-2,8,-3,10,3,9,-8,-9,-7,-1,8,-3,-6,4,-4,4,-7,-6,1,4,-5,-7,2,-4,-2,-5,4,-5,1,-10,-10,-1,-9,7,-6,3,-4,6,6,-6,-4,-1,9,9,-5,-2,-5,4,-1,1,-2,9,-7,-9,-3,-3,5,7,2,-3,5,2,8,4,-6,7,1,1,8,-3,6,2,-2,7,-5,8,4,1,-7,3,10,-1,-5,9,4,-6,9,-4,-9,2,-1,-5,2,1,9,-5,4,-9,10,-4,-3,-9,-10,-1,5,-2,-4,3,3,7,8,2,-2,2,-3,10,-7,-6,3,-6,3,-7,5,4,2,1,-7,-1,-5,1,-9,4,10,-3,-9,1,8,-8,-8,10,-4,-1,3,-10,-6,6,1,-1,2,-4,-4,-3,-5,-5,3,-4,-8,10,8,2,10,-9,-10,2,6,-4,-4,-3,8,-3,-5,10,3,-7,-1,-7,6,1,-6,-7,2,-5,8,5,-7,-9,-7,-8,-10,-1,1,-9,6,5,5,-6,-5,1,-8,9,7,10,8,2,10,-6,-3,-9,7,3,-6,-8,8,4,8,-1,-3,8,-8,7,8,-2,10,-2,-5,-8,-1,-2,8,5,1,-2,9,-4,-2,7,-6,-1,-10,3,5,6,10,5,6,-5,-7,9,-8,-5,6,10,-2,-10,3,10,7,-6,-6,6,-2,-6,1,-7,10,1,5,-10,2,1,-3,5,-7,-10,1,-4,10,-2,-7,10,-2,-5,-2,-3,-5,10,-7,2,4,-8,8,10,4,-9,-2,10,9,8,-2,-6,9,-7,-10,10,-10,1,-10,8,-2,7,-3,5,-2,-5,-5,-1,4,-1,-10,-8,-1,10,9,-7,2,-2,-1,-9,9,-7,-5,-1,10,-5,4,1,-4,7,9,-2,-8,-8,-1,-3,-2,-5,3,-8,-7,-3,6,-6,-5,4,7,-6,10,7,10,-2,-2,-1,-4,-8,-2,1,5,10,10,-5,-10,5,5,-1,-4,9,-1,-1,-7,-5], dtype = "int8")#candidate|10627|(756,)|const|int8
call_10625 = relay.TupleGetItem(func_6808_call(relay.reshape(const_10626.astype('bool'), [9, 3, 13]), relay.reshape(const_10627.astype('int8'), [756,]), ), 0)
call_10628 = relay.TupleGetItem(func_6811_call(relay.reshape(const_10626.astype('bool'), [9, 3, 13]), relay.reshape(const_10627.astype('int8'), [756,]), ), 0)
output = relay.Tuple([call_10586,call_10591,const_10592,call_10618,call_10625,const_10626,const_10627,])
output2 = relay.Tuple([call_10587,call_10593,const_10592,call_10619,call_10628,const_10626,const_10627,])
func_10641 = relay.Function([], output)
mod['func_10641'] = func_10641
mod = relay.transform.InferType()(mod)
output = func_10641()
func_10642 = relay.Function([], output)
mutated_mod['func_10642'] = func_10642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7084_call = mod.get_global_var('func_7084')
func_7085_call = mutated_mod.get_global_var('func_7085')
call_10677 = relay.TupleGetItem(func_7084_call(), 1)
call_10678 = relay.TupleGetItem(func_7085_call(), 1)
output = relay.Tuple([call_10677,])
output2 = relay.Tuple([call_10678,])
func_10682 = relay.Function([], output)
mod['func_10682'] = func_10682
mod = relay.transform.InferType()(mod)
output = func_10682()
func_10683 = relay.Function([], output)
mutated_mod['func_10683'] = func_10683
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10719 = relay.var("var_10719", dtype = "uint16", shape = ())#candidate|10719|()|var|uint16
var_10720 = relay.var("var_10720", dtype = "uint16", shape = (8, 7, 1))#candidate|10720|(8, 7, 1)|var|uint16
bop_10721 = relay.left_shift(var_10719.astype('uint16'), var_10720.astype('uint16')) # shape=(8, 7, 1)
bop_10724 = relay.floor_mod(var_10719.astype('float64'), bop_10721.astype('float64')) # shape=(8, 7, 1)
output = bop_10724
output2 = bop_10724
func_10732 = relay.Function([var_10719,var_10720,], output)
mod['func_10732'] = func_10732
mod = relay.transform.InferType()(mod)
var_10733 = relay.var("var_10733", dtype = "uint16", shape = ())#candidate|10733|()|var|uint16
var_10734 = relay.var("var_10734", dtype = "uint16", shape = (8, 7, 1))#candidate|10734|(8, 7, 1)|var|uint16
output = func_10732(var_10733,var_10734,)
func_10735 = relay.Function([var_10733,var_10734,], output)
mutated_mod['func_10735'] = func_10735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10209_call = mod.get_global_var('func_10209')
func_10210_call = mutated_mod.get_global_var('func_10210')
call_10768 = relay.TupleGetItem(func_10209_call(), 1)
call_10769 = relay.TupleGetItem(func_10210_call(), 1)
output = call_10768
output2 = call_10769
func_10775 = relay.Function([], output)
mod['func_10775'] = func_10775
mod = relay.transform.InferType()(mod)
output = func_10775()
func_10776 = relay.Function([], output)
mutated_mod['func_10776'] = func_10776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7084_call = mod.get_global_var('func_7084')
func_7085_call = mutated_mod.get_global_var('func_7085')
call_10797 = relay.TupleGetItem(func_7084_call(), 0)
call_10798 = relay.TupleGetItem(func_7085_call(), 0)
func_7637_call = mod.get_global_var('func_7637')
func_7639_call = mutated_mod.get_global_var('func_7639')
call_10804 = relay.TupleGetItem(func_7637_call(), 1)
call_10805 = relay.TupleGetItem(func_7639_call(), 1)
output = relay.Tuple([call_10797,call_10804,])
output2 = relay.Tuple([call_10798,call_10805,])
func_10807 = relay.Function([], output)
mod['func_10807'] = func_10807
mod = relay.transform.InferType()(mod)
mutated_mod['func_10807'] = func_10807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10807_call = mutated_mod.get_global_var('func_10807')
call_10808 = func_10807_call()
output = call_10808
func_10809 = relay.Function([], output)
mutated_mod['func_10809'] = func_10809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6529_call = mod.get_global_var('func_6529')
func_6531_call = mutated_mod.get_global_var('func_6531')
call_10835 = relay.TupleGetItem(func_6529_call(), 0)
call_10836 = relay.TupleGetItem(func_6531_call(), 0)
output = relay.Tuple([call_10835,])
output2 = relay.Tuple([call_10836,])
func_10846 = relay.Function([], output)
mod['func_10846'] = func_10846
mod = relay.transform.InferType()(mod)
mutated_mod['func_10846'] = func_10846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10846_call = mutated_mod.get_global_var('func_10846')
call_10847 = func_10846_call()
output = call_10847
func_10848 = relay.Function([], output)
mutated_mod['func_10848'] = func_10848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10387_call = mod.get_global_var('func_10387')
func_10388_call = mutated_mod.get_global_var('func_10388')
call_10853 = relay.TupleGetItem(func_10387_call(), 0)
call_10854 = relay.TupleGetItem(func_10388_call(), 0)
output = relay.Tuple([call_10853,])
output2 = relay.Tuple([call_10854,])
func_10863 = relay.Function([], output)
mod['func_10863'] = func_10863
mod = relay.transform.InferType()(mod)
output = func_10863()
func_10864 = relay.Function([], output)
mutated_mod['func_10864'] = func_10864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10863_call = mod.get_global_var('func_10863')
func_10864_call = mutated_mod.get_global_var('func_10864')
call_10910 = relay.TupleGetItem(func_10863_call(), 0)
call_10911 = relay.TupleGetItem(func_10864_call(), 0)
func_7364_call = mod.get_global_var('func_7364')
func_7366_call = mutated_mod.get_global_var('func_7366')
const_10922 = relay.const([10,10,3,-4,-2,-10,-4,10,-7,-9,9,8,-5,8,-3,-3,4,5,-1,-2,7,-6,6,-4,-2,1,10,7,-10,5,-1,6,-6,-5,-1,2,2,8,-1,10,-5,9,10,-9,3,4,4,9,5,9,-2,4,6,-1,-2,4,-2,3,9,2,5,7,-10,-3,10,-10,10,8,6,7,-10,7,4,-2,1,-6,-2,8,-7,6,3,-4,10,1,1,5,-8,3,-10,4,1,-8,1,6,8,-9,-9,-6,-5,6,4,7,-2,4,5,3,-6,-8,10,-6,5,-1,-8,-3,3,-9,9,-9,-6,2,8,7,8,-2,-9,-7,6,1,5,1,3,3,7,4,-4,5,4,8,7,-10,-10,3,5,4,-7,-7,4,-6,-3,-4,-9,-9,-1,6,-6,-6,-5,2,4,1,-10,6,10,5,-2,-8,-6,-7,1,6,-2,-4,3,1,4,1,-2,-6,-8,-6,9,-3,-1,3,4,9,-2,-6,-1,-4,-1,-6,1,5,-4,10,-5,8,3,-9,-1,-2,-3,9,5,6,-10,1,6,-1,-9,2,3,-1,1,1,8,6,4,-3,1,-7,4,2,-3,8,3,-7,2,-3,8,7,-1,-7,-10,-6,-2,4,10,-5,1,9,5,-2,-4,10,-1,7,-1,9,-5,-4,7,-2,-8,-3,2,4,-8,4,5,3,2,10,-2,-5,-1,5,-1,-8,-6,7,-3,-5,9,-10,-3,10,2,-1,6,-5,-6,-6,9,-3,5,5,1,6,9,-4,-2,2,-4,-10,8,9,4,-1,1,10,-6,-1,-6,6,-6,2,5,-2,4,9,-5,-5,4,-6,2,1,2,4,1,-5,-2,-7,-8,6,-2,3,-1,-8,4,2,-1,-3,-4,-3,7,-4,-5,-6,1,-7,4,2,-10,-2,6,2,4,-2,-2,-5,-3,8,1,2,-5,-7,-3,-6,-9,9,4,-3,-9,-9,10,-10,3,10,3,8,-5,8,-3,-10,5,-8,-5,7,7,-2,10,-9,-3,6,3,5,6,3,-8,-2,6,-9,-2,-2,-4,4,-8,6,-2,-7,-4,-2,-6,2,9,4,-5,-6,-1,5,-3,-9,2,4,8,8,4,4,6,-1,-3,10,-9,-4,5,6,-8,10,-10,3,-8,10,2,1,4,-5,-8,-5,-3,7,-10,-5,8,8,2,6,4,-1,1,-6,-5,-2,-6,-9,-9,7,9,-8,1,-5,-7,2,-8,-10,6,-4,9,-3,-6,-5,1,2,6,-9,6,-2,6,6,9,-4,6,-8,-5,-9,5,4,8,10,-8,2,4,8,-10,-5,-4,5,-7,4,-4,-3,-7,-9,-6,8,7,-7,4,10,-2,2,-3,8,10,2,-5,6,-3,-8,3,3,7,-10,7,-4,6,7,-5,-7,-6,-10,5,2,1,7,7,-6,1,-5,8,9,5,3,-2,-6,9,-9,2,-2,-3,-10,10,5,4,10,-7,-7,-7,-4,-9,7,-6,4,-2,-2,-5,7,10,7,-10,-5,-5,1,3,1,8,1,6,4,2,-5,10,-4,-2,4,5,-10,4,-2,-9,-10,-1,-4,6,7,6,7,-1,-6,-2,-4,-2,7,6,-2,2,-5,-2,-10,-7,-8,-8,-8,-8,2,7,-6,10,4,5,-2,-9,-10,4,-1,8,1,-8,2,5,5,10,10,7,8,1,8,5,-3,7,-9,7,10,-10,1,-6,7,10,-10,3,-10,5,8,-8,-8,-7,10,8,-9,-2,-6,-7,-8,2,7,-3,-4,6,8,-3,9,-5,5,-8,-4,5,1,-2,-10,-7,4,3,-8,-7,1,5,3,-8,3,-1,8,-6,-7,-8,-5,-1,4,-6,-2,-1,5,4,7,-4,-10,9,2,-7,-6,-5,9,-9,-1,7,7,8,-5,-10,6,3,3,-4,-7,-2,-7,3,5,8,6,9,3,-7,-2,1,5,4,5,-10,10,-5,-1,4,10,-1,-9,-2,-10,1,8,-9,-5,10,2,4,6], dtype = "int8")#candidate|10922|(756,)|const|int8
call_10921 = relay.TupleGetItem(func_7364_call(relay.reshape(const_10922.astype('int8'), [18, 42])), 1)
call_10923 = relay.TupleGetItem(func_7366_call(relay.reshape(const_10922.astype('int8'), [18, 42])), 1)
output = relay.Tuple([call_10910,call_10921,const_10922,])
output2 = relay.Tuple([call_10911,call_10923,const_10922,])
func_10947 = relay.Function([], output)
mod['func_10947'] = func_10947
mod = relay.transform.InferType()(mod)
output = func_10947()
func_10948 = relay.Function([], output)
mutated_mod['func_10948'] = func_10948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10863_call = mod.get_global_var('func_10863')
func_10864_call = mutated_mod.get_global_var('func_10864')
call_10973 = relay.TupleGetItem(func_10863_call(), 0)
call_10974 = relay.TupleGetItem(func_10864_call(), 0)
output = call_10973
output2 = call_10974
func_10980 = relay.Function([], output)
mod['func_10980'] = func_10980
mod = relay.transform.InferType()(mod)
output = func_10980()
func_10981 = relay.Function([], output)
mutated_mod['func_10981'] = func_10981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10209_call = mod.get_global_var('func_10209')
func_10210_call = mutated_mod.get_global_var('func_10210')
call_10984 = relay.TupleGetItem(func_10209_call(), 0)
call_10985 = relay.TupleGetItem(func_10210_call(), 0)
output = call_10984
output2 = call_10985
func_10997 = relay.Function([], output)
mod['func_10997'] = func_10997
mod = relay.transform.InferType()(mod)
mutated_mod['func_10997'] = func_10997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10997_call = mutated_mod.get_global_var('func_10997')
call_10998 = func_10997_call()
output = call_10998
func_10999 = relay.Function([], output)
mutated_mod['func_10999'] = func_10999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8338_call = mod.get_global_var('func_8338')
func_8340_call = mutated_mod.get_global_var('func_8340')
call_11123 = relay.TupleGetItem(func_8338_call(), 0)
call_11124 = relay.TupleGetItem(func_8340_call(), 0)
output = call_11123
output2 = call_11124
func_11167 = relay.Function([], output)
mod['func_11167'] = func_11167
mod = relay.transform.InferType()(mod)
output = func_11167()
func_11168 = relay.Function([], output)
mutated_mod['func_11168'] = func_11168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10174_call = mod.get_global_var('func_10174')
func_10176_call = mutated_mod.get_global_var('func_10176')
call_11187 = relay.TupleGetItem(func_10174_call(), 0)
call_11188 = relay.TupleGetItem(func_10176_call(), 0)
func_5882_call = mod.get_global_var('func_5882')
func_5890_call = mutated_mod.get_global_var('func_5890')
const_11205 = relay.const([1.429372,-0.443686,1.286640,0.903399,-6.788568,-7.371824,9.807555,7.229393,0.155522,-3.208739,3.987672,-0.351407,-0.485879,3.658567,5.048791,-5.541130,-5.285118,1.620895,0.734188,-5.179822,3.826492,-3.132237,9.564833,-9.305517,6.983305,-1.297670,7.621515,-5.477334,6.002654,0.571801,-9.415650,8.687442,5.832553,9.252600,4.538139,-4.757704,-6.138308,-4.736164,-1.615699,-6.135492,2.118709,-6.044151,9.858575,-5.275833,7.948928,-8.460267,-8.764382,-7.448878,-8.440469,-4.186359,4.336525,9.514815,-1.842846,-2.425742,-1.626755,-7.503453,2.019699,7.184685,-3.921796,8.829416,1.769741,9.141098,-3.173467,8.073477,5.420860,-7.387155,-4.331904,-4.325330,6.068513,8.953482,-6.873408,-7.612221,2.659455,-2.343036,1.772786,3.485880,5.448075,-8.309087,-7.889315,3.374989,-9.017524,3.529670,0.734553,9.104569,-3.902293,-2.384124,-9.067383,-9.571732,-5.194330,1.414422,4.827528,6.369283,-3.840545,-0.601821,6.816967,-3.629077,2.113664,7.741317,-4.464629,-5.240274,0.720927,9.460744,2.020266,3.904482,-5.017264,3.126964,9.383847,1.270522,2.467186,1.670587,3.625955,-7.876602,3.635098,8.903184,-6.650778,-8.786482,-7.354935,7.818011,7.119562,-2.025972,-6.035385,6.978871,-1.696329,3.621958,-5.450343,-5.602948,-3.695237,2.591810,-1.531902,4.618617,-4.800913,9.779283,5.385120,-9.510426,7.994997,1.351779,-2.908006,-0.777052,3.896589,-4.391235,-6.243926,2.918162,6.669207,-5.802584,4.810751,-1.808256,3.371204,-6.361072,2.703601,6.025221,0.164453,-4.698158,-7.554082,-0.809347,-3.130431,6.673255,-2.522056,4.394378,5.450314,6.781748,-0.384300,-8.116855,5.863376,-0.569875,0.730543,-3.909806,-6.812727,1.899024,6.930564,-9.913885,-5.009626,-6.223612,-3.699292,8.969366,9.092164,-4.856902,-1.131818,5.447922,-9.828346,-5.400684,4.376597,-9.204926,9.594984,-5.523879,-0.807388,-5.977726,5.298520,1.363061,8.959152,5.372418,9.063460,-3.857667,3.691931,-2.812824,8.682387,6.800442,1.207128,0.213907,2.662723,1.641913,-1.885286,5.936781,-8.687246,-9.008676,1.117715,-9.484117,1.253492,-3.082548,-8.009582,-2.077179,-3.790668,-6.545417,-7.141239,-3.230201,-9.462981,9.420020,-5.261738,-6.308200,1.415045,-6.807891,-6.146342,0.138550,5.508570,-5.275249,-6.621536,9.901841,2.828554,-0.588950,5.878932,0.845579,-1.969660,9.263859,6.899483,0.305929,-0.277855,5.954196,-1.295008,-8.194958,7.127752,0.467231,-5.808688,-4.043250,2.130798,6.739179,0.248059,-8.245529,8.503191,-4.601394,4.398614,2.002982,6.763124,-8.833478,1.754887,9.989689,-4.656140,4.549654,-2.559997,-1.922387,-8.309155,-1.910351,-1.884262,-7.100929,-2.718439,8.124270,-3.025506,8.128489,4.222103,-7.204381,8.732318,2.066015,-8.558882,-7.316851,-9.127234,-2.571718,-7.580349,7.003232,8.378168,-8.229051,-1.956671,3.287445,-7.843979,8.153225,2.874779,-7.113662,8.092899,-4.327809,-8.794992,-3.864906,0.419663,-9.600026,-0.983856,-4.096887,4.306119,6.406728,-3.903684,-3.923701,-7.260885,5.194023,3.108072,-0.089299,2.360084,6.267438,7.503047,1.138540,-4.144884,-8.934102,5.704306,9.611912,5.743053,-4.595627,3.679835,-2.909168,-3.286857,9.565489,8.940085,9.662108,-9.395251,9.952435,-3.944438,-3.382511,-8.008584,4.715320,-5.722242,-7.880558,-4.471033,8.338139,1.846025,4.383252,8.138674,-4.155585,-1.854870,-0.524891,-7.543042,-4.289132,-1.814728,3.670239,4.945050,-3.936045,1.372083,2.751287,2.055390,-8.375079,-4.483804,6.751940,-8.669326,-9.032587,4.760203,-8.725423,-3.714981,-7.715223,8.386425,5.089999,8.666156,-1.929862,-0.712071,-5.458022,3.552767,8.842322,-7.788789,4.823493,-1.432556,2.778724,-7.407923,6.931400,-9.841820,9.822467,1.116202,-4.932236,-1.515912,-9.829802,-7.923511,0.924773,9.900266,1.537870,2.401948,-2.519570,-8.542312,8.261502,0.441282,-6.536540,-3.936841,-8.030938,-7.742531,-1.403963,3.863865,-7.701283,7.778631,9.358323,-9.829277,-9.127412,-6.909886,4.186898,-8.273754,2.048247,9.431506,4.887521,-1.824231,5.172504,-5.244578,8.292744,-6.227685,3.307790,0.847421,-2.603793,4.583849,7.743656,-3.814088,0.799843,4.347745,-0.450427,-3.045369,3.381303,3.899645,1.100229,-1.508349,-5.571199,-2.355581,8.717111,-6.217659,9.087593,-4.488029,9.631574,3.314954,-2.245525,-0.939654,2.498722,-2.031566,3.119062,-4.216336,-8.972168,1.676076,4.757545,-5.395231,-6.364229,9.549227,6.978551,-4.888086,-3.146995,7.895350,9.609402,7.071750,-0.765548,8.803012,-3.470404,-6.633096,-5.465921,5.015853,-1.067365,-7.573319,-5.560776,-6.868673,-8.290768,5.717845,2.711737,5.789342,-3.035226,3.210974,-6.593389,-6.989541,-0.926086,5.022240,-4.820891,3.946074,8.571082,2.298798,8.369788,2.560287,8.147530,-0.090554,5.339001,1.433874,-3.249794,-6.708564,4.683593,4.684598,4.305935,-5.367150,8.512354,-1.763534,-9.888417], dtype = "float32")#candidate|11205|(480,)|const|float32
var_11206 = relay.var("var_11206", dtype = "float64", shape = (192,))#candidate|11206|(192,)|var|float64
const_11207 = relay.const([[-7.505472,-1.773449,-3.958102,2.007242,-7.713329,4.591870,-2.124096,-3.412890,6.328490,7.444743,-8.407521,4.117947,2.938710,3.706746,8.996107,5.702068,-3.110437,-2.331482,4.271705,0.310457,-7.492476,-1.343406,1.972983,-4.280236,7.259584,1.584810,3.874094,3.732850,5.735780,-3.682700,3.255355,-2.852756,4.431525,8.017560,-7.252110,-1.403458,4.286255,-1.392620,1.498070,3.234037,-3.717166,-5.472848,0.606647,-5.179161,-9.907009,6.106702,-1.379653,-2.230185,-5.215451,-5.361200,-4.203745,8.903856,1.054541,-0.118054,-3.372624,-0.476155,1.971200,-7.268226,-0.506049,2.820030,0.568173,9.855063,5.846288,-2.423800,9.664653,-1.874933,5.064119,8.650961,3.460947,-2.814044,1.818274,-0.411283,1.881659,1.095534,3.958195,8.453029,0.757424,-6.904216,-2.001357,-2.458120,4.275211,7.993750,-9.510783,-4.280421,-8.546387,-2.413620,6.645318,-1.054381,3.309688,-1.554315,8.497817,-5.397276,-3.368947,6.000994,6.267563,-3.501252,-8.955673,1.122196,-5.058662,6.848660,-2.288271,-3.105303,-2.000685,8.587406,-2.449036,4.653049,8.903832,-1.309132,-0.751271,-8.211712,6.234803,2.481654,-7.954726,2.452152,-0.894259,8.781988,-7.092822,-8.901470,2.112463,-1.981252,6.466271,3.672110,4.318696,3.322278,0.306721,1.515360,-2.137072,-1.274566,-4.991165,-3.324706,-5.297175,1.631251,4.162217,-1.525272,1.976634,9.831671,-6.342997,5.589299,-7.320988,3.677585,-8.166487,7.245780,6.650140,3.282100,5.674770,-2.857796,-7.956148,-6.135265,0.310642,-7.451920,3.290768,-2.613625,-4.475093,-9.151263,-6.039068,-8.629996,-7.619738,2.120272,7.130559,0.615067,-5.192987,2.486781,-3.115134,1.844590,-7.240883,-9.084340,7.315928,6.775266,7.056062,-3.616223,8.124000,-9.378838,-0.746124,-4.634330,4.088405,-2.386476]], dtype = "float32")#candidate|11207|(1, 176)|const|float32
var_11208 = relay.var("var_11208", dtype = "float32", shape = (300,))#candidate|11208|(300,)|var|float32
call_11204 = relay.TupleGetItem(func_5882_call(relay.reshape(const_11205.astype('float32'), [5, 12, 8]), relay.reshape(const_11205.astype('float32'), [5, 12, 8]), relay.reshape(var_11206.astype('float64'), [96, 2]), relay.reshape(const_11207.astype('float32'), [4, 44]), relay.reshape(const_11207.astype('float32'), [4, 44]), relay.reshape(var_11208.astype('float32'), [300,]), ), 3)
call_11209 = relay.TupleGetItem(func_5890_call(relay.reshape(const_11205.astype('float32'), [5, 12, 8]), relay.reshape(const_11205.astype('float32'), [5, 12, 8]), relay.reshape(var_11206.astype('float64'), [96, 2]), relay.reshape(const_11207.astype('float32'), [4, 44]), relay.reshape(const_11207.astype('float32'), [4, 44]), relay.reshape(var_11208.astype('float32'), [300,]), ), 3)
output = relay.Tuple([call_11187,call_11204,const_11205,var_11206,const_11207,var_11208,])
output2 = relay.Tuple([call_11188,call_11209,const_11205,var_11206,const_11207,var_11208,])
func_11211 = relay.Function([var_11206,var_11208,], output)
mod['func_11211'] = func_11211
mod = relay.transform.InferType()(mod)
mutated_mod['func_11211'] = func_11211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11211_call = mutated_mod.get_global_var('func_11211')
var_11213 = relay.var("var_11213", dtype = "float64", shape = (192,))#candidate|11213|(192,)|var|float64
var_11214 = relay.var("var_11214", dtype = "float32", shape = (300,))#candidate|11214|(300,)|var|float32
call_11212 = func_11211_call(var_11213,var_11214,)
output = call_11212
func_11215 = relay.Function([var_11213,var_11214,], output)
mutated_mod['func_11215'] = func_11215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5512_call = mod.get_global_var('func_5512')
func_5513_call = mutated_mod.get_global_var('func_5513')
call_11217 = func_5512_call()
call_11218 = func_5512_call()
output = call_11217
output2 = call_11218
func_11220 = relay.Function([], output)
mod['func_11220'] = func_11220
mod = relay.transform.InferType()(mod)
output = func_11220()
func_11221 = relay.Function([], output)
mutated_mod['func_11221'] = func_11221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6551_call = mod.get_global_var('func_6551')
func_6552_call = mutated_mod.get_global_var('func_6552')
call_11241 = relay.TupleGetItem(func_6551_call(), 1)
call_11242 = relay.TupleGetItem(func_6552_call(), 1)
func_7748_call = mod.get_global_var('func_7748')
func_7753_call = mutated_mod.get_global_var('func_7753')
const_11244 = relay.const([-7,-3,10,-2,3,6,-3,2,-9,10,-7,7,-7,4,-8,-3,1,8,10,-10,2,-4,8,-2,2,-10,-10,4,8,5,1,3,-6,5,-10,8,2,-8,10,9,3,1,-8,3,3,2,-8,9,-3,-7,-9,7,-6,6,-9,10,-6,-7,7,8,8,5,-4,-9,9,2,-10,1,-7,4,2,8,-4,-2,-5,-1,10,-10,-10,-3,-2,7,7,-9,-7,-10,6,6,-3,3,9,-2,9,5,-10,8,-5,-5,5,5,-9,-10,5,9,6,-5,-3,6,-8,3,9,-9,8,-5,9,4,6,-5,4,6,-5,5,-9,-1,-1,-4,-6,3,8,7,-7,-7,7,-2,5,10,-1,7,-7,-7,-5,-7,6,4,-9,3,-4,-8,4,3,-2,-1,-10,-4,-9,5,2,4,1,3,-1,-5,7,-7,7,-2,6,3,4,-3,6,6,10,-7,-9,3,5,6,-5,-6,-4,-3,-4,6,-2,10,9,-8,-7,1,5,8,6,-3,7,-5,-10,1,3,-9,-8,-4,6,-5,-7,8,2,2,-10,-1,6,7,-2,-7,8,1,6,1,7,4,-4,-8,10,6,-6,-6,3,-10,4,2,-5,5,8,5,4,1,-2,6,-10,-2,1,1,-1,-9,-10,6,3,9,1,-9,3,-3,-3,-9,-3,-1,8,8,-5,-6,-9,-2,-6,-6,-7,2,-8,-7,7,-2,-8,5,-5,5,10,-4,-6,1,-7,10,3,6,-8,10,10,6,-7,3,-1,-3,-4,10,-3,-1,-8,-6,3,-2,-6,8,6,-5,-2,6,-1,-4,6,-4,-3,-1,5,1,1,1,-6,3,-3,-7,-7,6,-2,2,4,-8,10,-9,-1,5,6,7,-6,-5,9,2,5,-5,-10,-6,2,3,-5,6,-5,-6,-6,-4,-5,1,-9,9,3,-10,10,1,-1,-3,9,2,8,-6,3,9,8,-2,-5,10,7,-2,7,-1,10,-5,-3,4,7,8,-9,-7,-10,-4,2,-2,-8,-7,10,5,4,-8,7,8,1,3,4,-4,1,-9,4,5,8,6,2,7,-1,10,-4,-3,4,-4,10,-3,8,5,3,-3,-1,-8,-2,8,-9,-3,-9,-7,-4,1,1,-4,-6,-10,-8,2,3,2,-5,9,1,7,8,-4,5,6,-1,-4,9,8,6,-9,-9,2,-3,8,-3,-7,8,-5,7,8,2,-7,-5,-10,-6,-10,2,-9,-5,3,1,-10,9,2,9,-4,-4,-3,7,-2,4,5,5,3,2,-9,5,-10,7,10,5,-6,-6,-10,6,-3,-5,8,-6,-2,-8,9,-10,-8,2,2,4,6,9,-3,9,5,8,-6,6,-1,8,-6,1,-9,1,-2,-1,7,8,7,7,3,-7,8,-8,-8,2,-9,7,8,9,-7,2,-4,-3,8,-5,5,-2,7,-5,6,-8,-10,3,7,2,2,-7,4,7,1,-7,-8,-1,-6,-10,4,9,7,2,2,7,9,2,5,7,5,-4,2,-8,4,3,7,1,-4,5,8,1,7,1,7,2,2,5,-3,-4,-10,-6,9,-9,2,-10,-8,-6,-6,-1,-6,7,10,2,4,2,-3,10,-6,6,5,-8,6,-9,2,-7,4,-6,5,-10,6,-2,-10,10,3,6,1,-10,8,9,-3,8,-10,2,4,4,-3,8,1,3,-5,2,3,-1,3,-10,-6,-4,3,-2,7,7,-4,-7,-5,9,-9,4,-10,2,-6,-10,1,1,-9,4,-10,-9,-6,-7,7,10,6,-8,10,-10,2,-3,5,10,-8,1,5,-2,8,-3,7,3,-7,10,2,-6,-1,9,2,9,4,-9,1,2,-3,4,-6,3,-9,3,-2,-4,-7,-8,-4,10,-10,7,-2,-3,-3,5,6,-5,9,-4,4,-6,3,-9,-3,-5,9,4,-2,-4,-4,6,-7,4,-6,8,6,-10,-8,-6,-1,-3,6,2,6,4,-7,1,9,9,-2,7,1,-7,-8,1,5,-10,3,10,7,9,-2,7,4,7,3,3,3,4,-4,-1,-8,1,-2,-1,3,-3,2,8,-6,-3,-9,4,6,-5,10,9,-8,1,1,1,2,1,-5,-10,-4,-1,-9,6,2,8,-7,2,-9,-7,5,-6,-3,-10,6,1,-5,4,9,3,-1,-3,-10,-4,-10,-9,9,1,-2,2,5,7,-8,-5,-1,8,9,-8,10,8,-3,4,-2,-7,8,-2,5,-4,-10,-1,7,-1,-3,-5,-3,1,-10,9,2,6,-7,4,8,6,6,7,7,2,-6,-2,-10,6,-8,1,1,1,-6,10,2,1,5,3,-5,3,4,2,-8,5,1,7,5,-2,2,4,9,-4,-3,-8,4,10,7,-3,8,3,3,-3,-8,9,8,4,9,2,4,10,1,7,2,3,5,-9,-7,-7,1,7,-9,7,-10,10,10,4,-10,1,9,1,-1,-4,-5,5,5,5,2,4,2,-8,3,-4,-2,-4,9,7,-6,-10,10,-8,7,2,5,1,-9,-10,10,-7,10,-5,7,-1,-3,-5,-6,1,-6,3,7,1,-5,-8,8,9,-7,7,6,-6,-10,-3,1,8,-5,1,4,-7,4,6,-3,9,9,3,-5,6,9,10,1,9,10,9,-3,-5,-4,-8,7,-6,-3,-4,7,4,9,-5,-3,-8,6,6,-4,6,-3,-4,10,-9,-8,-3,-4,10,-2,-6,1,7,9,-7,-6,8,5,-2,-3,-2,-5,-7,-4,2,6,-1,2,-6,-3,2,6,-1,-6,-10,5,2,-6,8,-8,6,-10,2,-4,3,-3,-7,6,2,10,-1,-3,-4,3,-1,-4,-6,-3,-8,-7,2,-5,9,-4,5,2,-10,10,3,6,4,-10,-6,-9,10,3,-5,9,-2,-4,9,-5,-10,3,-10,-1,10,-7,4,1,3,6,-4,4,7,5,6,7,6,-1,-8,3,4,6,-7,4,9,-5,-2,-9,7,-9,3,-8,5,-7,2,2,-1,5,-3,5,-6,7,1,9,9,2,-3,2,2,10,1,-1,10,8,5,-7,6,-1,1,5,-9,3,7,-9,-7,2,-2,-8,-9,8,-2,6,-1,2,-8,-4,-4,-8,-6,-10,5,1,-5,10,7,-9,-4,-4,-10,9,-5,-5,-3,2,10,-2,-3,2,6,-3,1,4,5,-10,-6,2,-3,-10,2,6,3,-6,-3,-6,4,1,-9,1,-3,-10,-2,-2,-1,-1,-4,4,-7,4,3,-8,-9,-10,-6,-4,-2,9,7,8,4,3,-8,-7,-9,4,1,7,-3,-8,-10,7,7,7,-9,-1,6,-3,1,9,1,2,-5,1,9,-6,-4,-10,-1,4,-4,3,9,6,5,9,-9,7,-1,-2,10,9,1,6,8,1,4,-4,1,-2,5,2,4,8,8,8,-5,5,-8,-7,-10,8], dtype = "uint16")#candidate|11244|(1300,)|const|uint16
const_11245 = relay.const(7, dtype = "int8")#candidate|11245|()|const|int8
call_11243 = relay.TupleGetItem(func_7748_call(relay.reshape(const_11244.astype('uint16'), [13, 10, 10]), relay.reshape(const_11244.astype('uint16'), [13, 10, 10]), relay.reshape(const_11245.astype('int8'), []), ), 0)
call_11246 = relay.TupleGetItem(func_7753_call(relay.reshape(const_11244.astype('uint16'), [13, 10, 10]), relay.reshape(const_11244.astype('uint16'), [13, 10, 10]), relay.reshape(const_11245.astype('int8'), []), ), 0)
func_5056_call = mod.get_global_var('func_5056')
func_5059_call = mutated_mod.get_global_var('func_5059')
const_11252 = relay.const([-9.961882,-6.450661,-1.994808,9.814040,-2.093285,3.835211,7.242330,-9.856201,-8.099042,-9.083774,1.304732,1.865052,-6.747294,2.881005,8.677184,4.094578,-0.141651,-9.981020,-8.665197,6.654011,4.554088,-0.238099,7.272664,9.914220,2.875659,-5.467136,6.244344,-7.595713,3.764758,8.902563,-0.535724,-9.782192,6.764724,-2.784390,-3.205248,-2.123532,-8.953477,-4.434572,0.547057,4.704381,-0.533467,0.210477,7.780602,2.734438,3.820992,-0.534683,7.152732,-3.296973,6.602322,-8.084939,2.971412,-2.445726,8.115733,0.389279,-8.651117,7.334683,-7.343587,-9.205985,0.008716,-6.648684,-4.196353,-1.803409,-9.127958,-8.249260,6.210437,7.958062,5.886485,-7.685888,8.267394,8.541566,-5.743720,-2.514989,3.327534,0.103185,-8.909629,-7.155278,-7.376701,-0.333382,1.685162,-0.463508,2.789529,5.147961,0.429456,2.476555,3.862365,-5.599303,2.510786,3.136084,1.991162,2.609387,-5.903381,1.185042,8.531916,5.076415,-7.256795,1.737685,-9.557862,5.464100,7.379490,-9.693613,8.998424,-5.753307,9.789518,-7.591203,-4.083885,-8.872576,6.533894,3.238902,8.964441,3.044630,5.112929,0.217665,-3.238511,5.263883,4.520573,-1.615260,4.554934,1.187496,-2.506874,4.655491,-3.791842,-2.752089,6.631313,-3.150699,-0.998113,9.162916,-3.650281,5.437541,9.630710,-3.361761,-5.675785,3.212973,-1.920055,-0.485470,-7.922438,0.059232,6.053604,-6.336847,-6.290668,3.253301,0.712587,-4.258596,4.786673,-2.919420,-0.719193,5.083554,4.817386,-5.361302,-3.164700,3.606335,5.755402,3.766858,-4.795191,2.261094,-2.253470,2.490202,1.658400,2.847289,-3.817425,7.313764,8.106595,2.922810,-9.899643,-8.625307,0.959775,0.070628,-6.444184,0.339567,3.064193,7.729813,-5.802232,3.944188,-7.197509,-1.413548,-7.850656,-9.337216], dtype = "float32")#candidate|11252|(176,)|const|float32
call_11251 = relay.TupleGetItem(func_5056_call(relay.reshape(const_11252.astype('float32'), [16, 1, 11])), 0)
call_11253 = relay.TupleGetItem(func_5059_call(relay.reshape(const_11252.astype('float32'), [16, 1, 11])), 0)
uop_11254 = relay.cosh(call_11243.astype('float32')) # shape=(13, 10, 10)
uop_11256 = relay.cosh(call_11246.astype('float32')) # shape=(13, 10, 10)
output = relay.Tuple([call_11241,const_11244,const_11245,call_11251,const_11252,uop_11254,])
output2 = relay.Tuple([call_11242,const_11244,const_11245,call_11253,const_11252,uop_11256,])
func_11271 = relay.Function([], output)
mod['func_11271'] = func_11271
mod = relay.transform.InferType()(mod)
mutated_mod['func_11271'] = func_11271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11271_call = mutated_mod.get_global_var('func_11271')
call_11272 = func_11271_call()
output = call_11272
func_11273 = relay.Function([], output)
mutated_mod['func_11273'] = func_11273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7084_call = mod.get_global_var('func_7084')
func_7085_call = mutated_mod.get_global_var('func_7085')
call_11286 = relay.TupleGetItem(func_7084_call(), 1)
call_11287 = relay.TupleGetItem(func_7085_call(), 1)
func_10846_call = mod.get_global_var('func_10846')
func_10848_call = mutated_mod.get_global_var('func_10848')
call_11306 = relay.TupleGetItem(func_10846_call(), 0)
call_11307 = relay.TupleGetItem(func_10848_call(), 0)
uop_11310 = relay.cosh(call_11306.astype('float32')) # shape=(6, 12, 2)
uop_11312 = relay.cosh(call_11307.astype('float32')) # shape=(6, 12, 2)
output = relay.Tuple([call_11286,uop_11310,])
output2 = relay.Tuple([call_11287,uop_11312,])
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
func_5648_call = mod.get_global_var('func_5648')
func_5649_call = mutated_mod.get_global_var('func_5649')
call_11345 = func_5648_call()
call_11346 = func_5648_call()
output = call_11345
output2 = call_11346
func_11348 = relay.Function([], output)
mod['func_11348'] = func_11348
mod = relay.transform.InferType()(mod)
output = func_11348()
func_11349 = relay.Function([], output)
mutated_mod['func_11349'] = func_11349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10807_call = mod.get_global_var('func_10807')
func_10809_call = mutated_mod.get_global_var('func_10809')
call_11448 = relay.TupleGetItem(func_10807_call(), 1)
call_11449 = relay.TupleGetItem(func_10809_call(), 1)
func_9033_call = mod.get_global_var('func_9033')
func_9034_call = mutated_mod.get_global_var('func_9034')
call_11457 = relay.TupleGetItem(func_9033_call(), 0)
call_11458 = relay.TupleGetItem(func_9034_call(), 0)
output = relay.Tuple([call_11448,call_11457,])
output2 = relay.Tuple([call_11449,call_11458,])
func_11461 = relay.Function([], output)
mod['func_11461'] = func_11461
mod = relay.transform.InferType()(mod)
output = func_11461()
func_11462 = relay.Function([], output)
mutated_mod['func_11462'] = func_11462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6154_call = mod.get_global_var('func_6154')
func_6156_call = mutated_mod.get_global_var('func_6156')
call_11572 = relay.TupleGetItem(func_6154_call(), 0)
call_11573 = relay.TupleGetItem(func_6156_call(), 0)
output = call_11572
output2 = call_11573
func_11578 = relay.Function([], output)
mod['func_11578'] = func_11578
mod = relay.transform.InferType()(mod)
output = func_11578()
func_11579 = relay.Function([], output)
mutated_mod['func_11579'] = func_11579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9298_call = mod.get_global_var('func_9298')
func_9299_call = mutated_mod.get_global_var('func_9299')
call_11619 = relay.TupleGetItem(func_9298_call(), 1)
call_11620 = relay.TupleGetItem(func_9299_call(), 1)
output = relay.Tuple([call_11619,])
output2 = relay.Tuple([call_11620,])
func_11631 = relay.Function([], output)
mod['func_11631'] = func_11631
mod = relay.transform.InferType()(mod)
mutated_mod['func_11631'] = func_11631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11631_call = mutated_mod.get_global_var('func_11631')
call_11632 = func_11631_call()
output = call_11632
func_11633 = relay.Function([], output)
mutated_mod['func_11633'] = func_11633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10641_call = mod.get_global_var('func_10641')
func_10642_call = mutated_mod.get_global_var('func_10642')
call_11657 = relay.TupleGetItem(func_10641_call(), 3)
call_11658 = relay.TupleGetItem(func_10642_call(), 3)
func_206_call = mod.get_global_var('func_206')
func_210_call = mutated_mod.get_global_var('func_210')
const_11674 = relay.const([-3,2,-10,-7,-2,9,7,4,-3,-8,7,1,-1,3,7,1,-8,6,-9,-7,7,10,-9,1,-1,6,-2,2,-1,-9,4,-8,2,-10,-6,-3,-5,10,-9,6,1,6,1,7,2,10,-5,-8,-2,-9,7,3,4,6,4,3,-3,7,10,4,1,8,2,-2,-6,3,2,9,-9,1,-6,7,5,3,-1,7,-3,-5,-5,-9,9,-6,8,-8,10,-10,-6,-8,-4,-8,10,-4,-2,-9,-9,8,2,10,-1,9,-10,2,8,8,-10,7,-2,4,2,-1,-2,9,-6,6,-9,-1,-3,-6,-2,3,1,-6,10,8,-1,-1,1,9,-10,5,9,10,-10,1,1,7,-3,-6,1,5,5,9,7,-1,2,-6,-3,-10,-3,8,8,-7,-8,-4,-6,-3,6,-7,9,-7,6,-1,-10,-4,6,6,-7,5,-7,-4,-9,-6,-10,-5,10,1,7,-7,-5,-9,-6,2,-1,9,-5,1,-2,8,-9,-1,7,7,4,-1,8,7,-9,7,8,-8,-1,-7,-3,2,-8,-2,-7,-8,-4,9,3,6,-6,3,-1,7,7,2,8,3,9,2,-4,-6,-1,2,10,7,-5,2,-9,-7,-2,8,4,-8,7,-8,10,3,8,5,-5,8,3,5,8,10,-8,-9,-2,-7,5,-1,-1,6,10,-1,-6,-5,8,4,-10,3,-5,-4,1,7,7,3,-2,9,-2,9,9,10,-3,-3,-9,3,-1,10,-8,-10,-4,-3,1,10,-4,1,2,3,6,-8,-2,-8,8,7,-6,3,7,10,-9,1,-9,9,4,5,-5,4,4,2,-3,-9,5,2,-7,-2,-3,2,-5,-1,10,-10,9,-4,-7,6,-7,-2,-7,6,7,2,1,9,-4,7,-6,-1,-1,7,-1,-2,8,-1,-8,-10,-5,4,8,-3,4,6,-9,5,2,-9,-5,-1,7,-9,-9,10,3,3,5,-4,6,-1,9,-4,-9,5,-8,-8,-8,-7], dtype = "uint8")#candidate|11674|(378,)|const|uint8
var_11675 = relay.var("var_11675", dtype = "int32", shape = (30, 2))#candidate|11675|(30, 2)|var|int32
call_11673 = relay.TupleGetItem(func_206_call(relay.reshape(const_11674.astype('uint8'), [3, 9, 14]), relay.reshape(var_11675.astype('int32'), [3, 2, 10]), ), 3)
call_11676 = relay.TupleGetItem(func_210_call(relay.reshape(const_11674.astype('uint8'), [3, 9, 14]), relay.reshape(var_11675.astype('int32'), [3, 2, 10]), ), 3)
output = relay.Tuple([call_11657,call_11673,const_11674,var_11675,])
output2 = relay.Tuple([call_11658,call_11676,const_11674,var_11675,])
func_11681 = relay.Function([var_11675,], output)
mod['func_11681'] = func_11681
mod = relay.transform.InferType()(mod)
mutated_mod['func_11681'] = func_11681
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11682 = relay.var("var_11682", dtype = "int32", shape = (30, 2))#candidate|11682|(30, 2)|var|int32
func_11681_call = mutated_mod.get_global_var('func_11681')
call_11683 = func_11681_call(var_11682)
output = call_11683
func_11684 = relay.Function([var_11682], output)
mutated_mod['func_11684'] = func_11684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10641_call = mod.get_global_var('func_10641')
func_10642_call = mutated_mod.get_global_var('func_10642')
call_11699 = relay.TupleGetItem(func_10641_call(), 0)
call_11700 = relay.TupleGetItem(func_10642_call(), 0)
output = relay.Tuple([call_11699,])
output2 = relay.Tuple([call_11700,])
func_11742 = relay.Function([], output)
mod['func_11742'] = func_11742
mod = relay.transform.InferType()(mod)
mutated_mod['func_11742'] = func_11742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11742_call = mutated_mod.get_global_var('func_11742')
call_11743 = func_11742_call()
output = call_11743
func_11744 = relay.Function([], output)
mutated_mod['func_11744'] = func_11744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7952_call = mod.get_global_var('func_7952')
func_7953_call = mutated_mod.get_global_var('func_7953')
call_11768 = func_7952_call()
call_11769 = func_7952_call()
output = relay.Tuple([call_11768,])
output2 = relay.Tuple([call_11769,])
func_11786 = relay.Function([], output)
mod['func_11786'] = func_11786
mod = relay.transform.InferType()(mod)
output = func_11786()
func_11787 = relay.Function([], output)
mutated_mod['func_11787'] = func_11787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9298_call = mod.get_global_var('func_9298')
func_9299_call = mutated_mod.get_global_var('func_9299')
call_11832 = relay.TupleGetItem(func_9298_call(), 1)
call_11833 = relay.TupleGetItem(func_9299_call(), 1)
func_6303_call = mod.get_global_var('func_6303')
func_6307_call = mutated_mod.get_global_var('func_6307')
var_11843 = relay.var("var_11843", dtype = "int8", shape = (756,))#candidate|11843|(756,)|var|int8
var_11844 = relay.var("var_11844", dtype = "float64", shape = (720,))#candidate|11844|(720,)|var|float64
const_11845 = relay.const([-4,-1,-7,-3,6,3,-9,-4,-4,-4,6,-6,9,-4,-10,-3,1,-7,-7,-7,-2,-9,-1,5,-1,-4,8,-8,9,7,10,-6,-2,-9,-3,-1,9,7,2,3,-10,2,8,4,-3,-1,-1,-4,-9,-3,3,9,-6,2,-8,-3,4,4,-7,-1,1,5,-8,6,-4,-10,-5,-9,-5,10,5,-2,1,1,6,10,4,1,6,9,-6,-7,10,-5,4,-10,1,8,-10,9,10,5,-9,-8,-2,5,6,1,5,-10,-1,9,-2,3,-5,8,-6,-9,-9,-7,4,1,3,3,-7,-8,3,2,4,5,-8,5,6,-8,-1,-8,-7,4,-10,-8,1,-9,5,8,-5,-9,8,8,7,10,10,-4,6,7,-6,5,2,2,5,7,6,6,9,9,9,6,7,6,-10,1,9,3,-2,-9,6,-9,-1,6,7,5,-5,7,1,-5,-8,6,4,1,6,-3,7,7,-4,-9,10,-1,7,7,1,8,10,-9,5,8,-3,6,-2,-9,7,9,3,2,-8,-7,-3,-8,-1,7,8,-9,-8,-10,-1,-9,8,6,10,1,-9,6,-3,4,3,2,-1,-4,-10,-1,5,7,-10,5,3,7,-2,1,-7,-1,-10,-4,6,10,-2,6,1,-9,8,-10,-9,2,-9,-7,10,7,-3,-3,-6,-8,5,4,-9,8,8,-8,-4,8,-5,-8,-5,7,5,-10,2,-9,-1,-5,-7,-8,9,-2,8,6,7,8,-8,-1,-4,6], dtype = "int8")#candidate|11845|(288,)|const|int8
call_11842 = relay.TupleGetItem(func_6303_call(relay.reshape(var_11843.astype('int8'), [756,]), relay.reshape(var_11844.astype('float64'), [720,]), relay.reshape(const_11845.astype('int8'), [24, 12]), ), 3)
call_11846 = relay.TupleGetItem(func_6307_call(relay.reshape(var_11843.astype('int8'), [756,]), relay.reshape(var_11844.astype('float64'), [720,]), relay.reshape(const_11845.astype('int8'), [24, 12]), ), 3)
output = relay.Tuple([call_11832,call_11842,var_11843,var_11844,const_11845,])
output2 = relay.Tuple([call_11833,call_11846,var_11843,var_11844,const_11845,])
func_11847 = relay.Function([var_11843,var_11844,], output)
mod['func_11847'] = func_11847
mod = relay.transform.InferType()(mod)
var_11848 = relay.var("var_11848", dtype = "int8", shape = (756,))#candidate|11848|(756,)|var|int8
var_11849 = relay.var("var_11849", dtype = "float64", shape = (720,))#candidate|11849|(720,)|var|float64
output = func_11847(var_11848,var_11849,)
func_11850 = relay.Function([var_11848,var_11849,], output)
mutated_mod['func_11850'] = func_11850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7637_call = mod.get_global_var('func_7637')
func_7639_call = mutated_mod.get_global_var('func_7639')
call_11915 = relay.TupleGetItem(func_7637_call(), 0)
call_11916 = relay.TupleGetItem(func_7639_call(), 0)
func_7805_call = mod.get_global_var('func_7805')
func_7806_call = mutated_mod.get_global_var('func_7806')
call_11917 = relay.TupleGetItem(func_7805_call(), 0)
call_11918 = relay.TupleGetItem(func_7806_call(), 0)
func_4826_call = mod.get_global_var('func_4826')
func_4830_call = mutated_mod.get_global_var('func_4830')
const_11927 = relay.const([-9.270392,0.690690,2.294235,9.557879,3.308631,3.012726,9.196426,1.576654,0.334246,5.341284,3.237557,-8.449769,-2.109571,-7.117824,7.185269,-9.103152,-1.629756,6.979562,8.153761,5.895839,-3.927363,0.988417,9.280099,-0.569085,0.950337,-5.757365,-9.606252,9.859680,-5.561523,1.827109,3.090691,4.323983,2.665968,6.107562,-7.709299,4.980029,9.489908,-6.168980,-1.371181,0.601276,6.167822,-7.679152,-1.084263,-2.401100,5.447479,-4.671974,-3.496870,4.682538,-7.264375,-1.407497,3.342838,-6.518976,-2.655324,-7.483185,5.056770,-0.428099,3.577135,9.686902,-0.236888,8.466375,4.002991,-7.939330,9.362171,3.362556,2.313614,-5.613418,6.877921,6.105994,-4.447653,-8.525582,-5.428334,-8.816568,7.343773,3.081754,9.652320,-5.028326,7.586500,-0.274127,-5.273029,-9.164993,0.198947,-2.095338,5.697097,-0.408091,7.134940,-7.597216,2.330052,-6.279061,-0.278675,-7.452731,-3.431615,-8.243891,-9.767012,-0.294939,-9.574865,-1.395648,-3.447478,-2.995651,-3.100830,9.421711,-1.583756,1.551993,-4.070151,-7.182316,-0.771107,-0.638376,8.869327,-7.774919,-9.659793,-9.048410,9.767861,-5.366498,-0.162670,-0.200438,-0.176062,-7.598510,4.951309,-1.377888,1.674566,-6.787588,-2.036334,-7.211128,2.101128,9.590156,-2.063663,-0.833920,-3.693239,2.026780,3.788621,6.609926,7.084551,-4.373764,-6.373920,-0.018285,-9.964683,7.116949,4.604405,-1.534842,-6.733681,-0.801722,-2.182132,-0.299094,-8.938444,2.838648,8.115712,1.441161,-8.695329,1.515442,-5.474881,8.343220,-6.992612,8.093092,-8.047413,-4.633396,7.046570,4.563061,6.229116,-6.607362,8.741430,-9.356479,0.865731,9.502903,6.075040,-1.522554,-4.576306,-1.178817,-6.405917,0.102095,-5.143614,1.479893,-2.129066,4.425983,-7.041904,9.945477,4.830827,4.340687,1.598688,-9.005504,3.596424,5.986720,-8.623844,3.116461,4.457265,-8.338487,-5.574303,-7.955764,-3.442159,1.626854,2.173260,5.489189,-7.066498,1.974516,5.288613,-5.259449,-2.010689,1.698319,-0.326948,1.602326,1.717062,5.340513,3.102530,-4.449515,0.511884,6.377339,8.256627,6.133473,2.251642,4.956651,-6.625278,1.787259,2.791830,-2.664221,7.084393,-1.192877,9.503699,9.701035,3.370045,-5.439375,3.222657,4.047275,-5.498303,-8.344205,-4.503416,9.964345,3.173853,9.818757,1.599255,-1.821487,-4.331844,5.577984,-1.864324,-0.091645,-0.856618,-2.134777,-2.416653,-3.325310,-1.422201,-6.118619,8.630239,-2.339826,5.096067,8.101714,9.084242,2.289196,-3.892161,0.856180,0.028991,-7.346309,-1.098041,7.423073,0.037809,-3.278433,-0.435327,-3.355293,-9.983569,1.584833,-9.302121,-1.331114,-1.407039,7.871612,-9.395913,-2.557132,2.208398,8.523548,1.955913,-8.375409,0.386024,8.933944,-7.319285,3.583175,-3.657784,-3.322366,3.591901,-3.570787,-1.800295,6.797556,-0.546341,3.691425,-0.360429,5.096032,9.211909,-7.859365,-5.762119,1.842241,8.960030,6.231437,4.204043,7.089651,-0.981990,-2.548234,6.114766,0.364257,2.797224,6.344298,-5.721335,-0.896544,3.367585,-0.103504,-5.047112,-5.228738], dtype = "float32")#candidate|11927|(300,)|const|float32
var_11928 = relay.var("var_11928", dtype = "float64", shape = (192,))#candidate|11928|(192,)|var|float64
const_11929 = relay.const([-8,2,-6,5,7,-9,7,10,-10,7,-9,2,3,-6,-5,-2,9,4,-4,5,4,10,3,-1,8,-10,9,2,9,7,-4,8,4,-1,1,-2,1,8,-3,-6,-9,10,10,1,2,5,6,-9,5,9,-7,1,-2,-9,10,-5,-2,6,-9,-1,-3,-6,10,-9,7,-1,8,10,10,6,5,-6,8,-8,9,7,8,2,1,2,-9,2,-2,-9,2,-2,-9,-7,-2,-4,-6,6,-4,-1,10,-3,-6,-6,7,-3,-3,7,5,8,1,-2,-1,-1,5,-10,-5,3,5,-10,-7,3,-7,-9,-6,-4,9,2,-2,-4,4,1,-6,9,-6,-6,-1,10,-9,4,7,10,2,5,4,-3,7,8,-10,7,-7,8,1,-7,8,6,9,-3,-10,7,10,-4,5,10,-10,-1,9,-6,9,3,-7,5,4,9,8,8,7,5,-4,7,-4,-3,-10,-5,4,-8,-6,-9,1,-4,3,9,6,1,-10,5,9,-9,9,-7,4,4,-8,-10,-10,-10,-6,4,-2,1,-5,8,-6,-2,2,8,7,-6,6,6,10,-10,4,8,2,9,-8,1,5,9,-5,5,-10,6,7,-3,-7,-3,8,10,3,-7,-8,8,-2,-3,5,-6,7,10,-4,-10,5,-4,7,5,5,2,10,9,9,6,9,9,-4,1,4,-8,5,4,-8,-1,-10,-10,-4,-10,-2,7,10,9,-4,1,2,-7,-3,-10,-1,-8,5,-9,7,-4,-8,2,4,2,-4,8,-2,4,9,10,6,-8,6,-1,-7,-3,3,-2,9,-9,-7,-10,3,6,-9,-1,-4,5,6,-4,9,9,5,1,5,6,8,-3,-1,4,-5,4,-1,1,4,-2,3,7,3,1,-7,-10,-4,-7,-1,-4,5,8,-8,5,4,-5,7,4,-9,9,-1,-2,-1,-9,-9,1,-2,9,-7,2,-2,-8,-6,-10,-9,-2,8,-5,-2,-1,9,4,-10,3,-9,-9], dtype = "uint8")#candidate|11929|(378,)|const|uint8
call_11926 = relay.TupleGetItem(func_4826_call(relay.reshape(const_11927.astype('float32'), [15, 2, 10]), relay.reshape(var_11928.astype('float64'), [48, 4]), relay.reshape(const_11929.astype('uint8'), [126, 3]), ), 0)
call_11930 = relay.TupleGetItem(func_4830_call(relay.reshape(const_11927.astype('float32'), [15, 2, 10]), relay.reshape(var_11928.astype('float64'), [48, 4]), relay.reshape(const_11929.astype('uint8'), [126, 3]), ), 0)
output = relay.Tuple([call_11915,call_11917,call_11926,const_11927,var_11928,const_11929,])
output2 = relay.Tuple([call_11916,call_11918,call_11930,const_11927,var_11928,const_11929,])
func_11938 = relay.Function([var_11928,], output)
mod['func_11938'] = func_11938
mod = relay.transform.InferType()(mod)
mutated_mod['func_11938'] = func_11938
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11939 = relay.var("var_11939", dtype = "float64", shape = (192,))#candidate|11939|(192,)|var|float64
func_11938_call = mutated_mod.get_global_var('func_11938')
call_11940 = func_11938_call(var_11939)
output = call_11940
func_11941 = relay.Function([var_11939], output)
mutated_mod['func_11941'] = func_11941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11786_call = mod.get_global_var('func_11786')
func_11787_call = mutated_mod.get_global_var('func_11787')
call_11980 = relay.TupleGetItem(func_11786_call(), 0)
call_11981 = relay.TupleGetItem(func_11787_call(), 0)
func_11742_call = mod.get_global_var('func_11742')
func_11744_call = mutated_mod.get_global_var('func_11744')
call_11982 = relay.TupleGetItem(func_11742_call(), 0)
call_11983 = relay.TupleGetItem(func_11744_call(), 0)
func_7952_call = mod.get_global_var('func_7952')
func_7953_call = mutated_mod.get_global_var('func_7953')
call_11986 = func_7952_call()
call_11987 = func_7952_call()
func_6060_call = mod.get_global_var('func_6060')
func_6069_call = mutated_mod.get_global_var('func_6069')
var_11997 = relay.var("var_11997", dtype = "float32", shape = (64,))#candidate|11997|(64,)|var|float32
const_11998 = relay.const([10,9,-1,5,-9,-7,-5,-10,2,-1,5,10,5,-4,-1,-7,4,10,9,3,10,6,10,6,-5,1,-9,8,1,4,7,-4,7,8,-1,5,-9,-7,-8,-1,9,5,-4,-1,4,-8,7,4,6,-2,-3,10,-2,10,-7,-5,4,-6,4,3], dtype = "int32")#candidate|11998|(60,)|const|int32
const_11999 = relay.const([9,-1,-5,-4,-6,6,10,-1,7,3,6,-3,-4,-2,-5,6,6,-6,6,8,9,-6,-1,1,-6,-2,-10,7,-2,-2,-3,-10,8,7,-9,4,8,-9,8,9,-2,8,-5,-7,3,5,-8,4,2,9,-8,-9,6,7,8,8,6,4,-3,8,2,2,8,-7,-7,4,-1,4,-1,-1,-7,-8,9,2,-3,-5,-6,7,3,6,2,5,-3,1,10,-2,5,7,2,-3,4,1,5,5,4,7,-1,9,3,-9,-4,-9,-3,-2,-8,1,2,-1,4,6,7,-1,-6,-4,2,2,-6,-4,7,-3,10,-6,-10,3,3,1,1,-8,-4,-7,-6,10,-10,-1,2,-2,2,7,7,7,7,9,9,8,10,10,4,9,6,-1,-6,1,2,-9,7,-8,3,4,-5,-7,-8,2,-7,-6,-3,-1,1,-6,-9,-10,2,-3,-5,8,9,-6,2,-1,-1,4,-5,2,7,6,2,4,-6,-10,4,-1,-5,2,-7,8,1,1,-9,1,-10,3,5,-7,-4,3,6,3,-3,9,-7,7,1,3,10,5,10,-3,7,7,-6,1,4,-3,8,-6,-1,4,-10,1,8,-9,5,-5,-3,-6,-3,-1,3,-6,8,-10,3,-10,-9,-3,10,-7,-6,-9,-5,8,-4,-6,4,9,-2,-10,1,9,2,8,4,9,10,-8,5,-2,6,-7,10,2,-5,8,-2,-9,-9,-8,-4,4,9,8,10,4,-8,6,-8,-1,-9,-10,-5,7,8,6,4,-6,4,6,4,1,2,-1,6,-3,8,-7,-4,5,-10,4,3,-9,-3,-2,-7,-8,-10,1,-8,10,10,1,2,6,8,-9,9,7,-3,9,-10,10,8,6,6,4,-5,-1,-10,10,8,-9,7,1,5,-3,8,6,7,-2,8,-10,-10,2,10,7,1,-5,4,-10,5,-3,-9,7,-1,-8,4,3,-8,3,7,6,-10,8,-6,-10,-2,-1,3,6,6,2,1,-3,10,-9,-8,5,-3,-1,-1,-9,5,5,-8,10,4,-4,-7,4,-5,-6,-5,2,-4,-8,-3,2,-6,3,-8,10,7,5,-2,-3,1,1,-10,5,-5,1,-1,-5,-9,-3,-5,9,8,8,-2,-7,2,-10,-1,8,-1,6,-3,-10,-3,-1,5,-2,3,-3,3,-9,-7,7,7,6,6,9,4,4,-2,8,3,2,-8,-1,4,5,-1,9,-10,6,-8,-7,-4,-2,6,-8,7,-6,-5,-7,-1,8,7,-9,-4,-6,10,5,-6,2,6,-4,-10,-10,-9,1,1,3,-9,-8,-7,-5,8,3,-8,8,5,-7,-4,7,3,-5,-9,4,-1,3,7,-5,10,8,2,-10,-10,1,3,9,-8,-2,-3,7,9,9,7,-10,1,3,-6,10,1,1,-1,-1,7,6,-2,-1,2,-6,8,-4,-5,-4,-3,10,6,-7,4,-6,1,-10,-6,3,-2,6,6,1,-8,-6,-9,-4,-10,4,9,4,3,-3,4,6,7,-8,-4,6,-3,-5,-9,-7,-10,-10,2,-10,-7,-5,-9,8,5,-8,-6,10,-7,2,-6,2,2,6,7,1,7,6,9,1,-2,2,5,9,-9,-5,-2,10,10,-9,1,2,8,-5,4,2,7,5,-7,2,-5,-2,6,10,7,-5,-1,-6,7,-7,-7,8,-2,4,7,-7,4,7,1,-8,-7,9,-1,7,6,10,3,-7,-3,4,10,-10,9,6,7,10,-8,3,2,9,6,-3,-9,3,3,10,9,10,1,9,10,1,-6,7,-6,8,-8,-8,1,-7,-1,2,10,7,5,-9,-5,3,7,-9,-6,3,-10,-1,4,-7,-8,4,-10,9,-9,10,-9,3,-3,-8,-1,-5,6,2,-5,-5,-10,10,2,-5,8,-2,10,-6,10,-6,-7,-2,8,-4,-6,7,-10,6,-8,2,10,-4,1,-5,-6,-4,1,-7,-1,-1,10,3,-7,-1,-1,3,-6,2], dtype = "int8")#candidate|11999|(756,)|const|int8
const_12000 = relay.const([-2.443427,-0.486680,-6.546657,0.908252,2.142064,-9.241258,7.534115,5.832519,-4.607489,9.484014,-0.334225,-8.991316,3.132329,6.721179,9.540988,6.370933,8.591596,6.892722,-8.367994,0.908906,-5.510586,-7.089462,-5.793106,-7.324409,-1.598189,-1.639235,-4.539180,3.350160,-0.618993,-7.181072,9.312643,9.517781,4.963131,-1.070845,-6.433496,0.505194,8.362863,-6.934946,0.781071,-6.543803,7.287066,-4.907641,-7.916850,3.109192,8.852414,-2.626401,3.669272,1.650868,-4.508040,-9.429886,-9.284277,6.244356,7.904222,4.161336,9.484545,5.746868,-5.110870,-3.197559,4.866217,0.008092,8.736798,5.967650,-6.104516,6.567801,-3.127734,2.847592,7.364114,9.442024,-6.548772,8.669348,-2.961680,-1.307045,-0.711143,1.156189,-5.336096,-6.762141,-7.306674,-5.762473,8.924292,6.212864,7.757005,-4.545108,-4.100846,-1.589379,-3.833750,-2.897944,-2.386302,-4.117584,3.888320,-4.485299,-3.707276,1.875723,2.672857,6.038654,2.245723,-4.976218,7.974503,3.908087,-6.836978,4.913956,5.251048,-8.069678,-8.378986,-3.559512,-1.098057,-0.545691,-0.094391,-6.569002,1.405858,-8.653091,-1.512746,-4.598160,8.901320,4.313786,6.399489,-6.617627,-6.949625,-9.876397,4.836609,-4.992522,7.771478,3.468653,-9.218160,5.144674,1.926698,-3.421230,5.982741,-2.108295,-3.283316,-7.544738,-6.026661,-8.187021,0.636009,9.855884,-6.205522,8.120032,-8.388349,5.319969,-3.435567,5.597798,-3.304337,7.111975,-1.446730,-5.859920,-9.729258,-5.833032,0.290639,5.425311,5.331333,-4.807732,0.494089,6.256055,-6.422349,-8.684063,-7.184493,-4.429947,-8.589660,-7.450164,3.793595,6.827101,0.193318,-7.501586,5.249810,-4.588939,5.678245,-1.759247,-8.535180,-0.132439,-7.088926,6.041392,-1.082750,8.056249,4.860046,7.373013,-7.265373,-3.844912,-4.241586,-5.620689,7.527603,-6.146859,9.845955,4.718095,8.403975,-0.782466,-2.849123,-4.320336,-5.373429,9.001336,4.774516,-5.459133,-1.319823,0.415122], dtype = "float64")#candidate|12000|(192,)|const|float64
var_12001 = relay.var("var_12001", dtype = "float64", shape = (720,))#candidate|12001|(720,)|var|float64
var_12002 = relay.var("var_12002", dtype = "int8", shape = (4, 72))#candidate|12002|(4, 72)|var|int8
const_12003 = relay.const([True,False,False,True,True,False,False,False,False,True,False,True,False,False,True,True,False,False,False,False,False,False,True,True,True,False,False,False,False,True,False,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,True,True,True,True,False,True,False,True,True,True,True,False,False,True,False,False,True,False,False,True,False,True,True,False,False,True,False,False,False,True,False,True,False,False,False,False,True,False,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False], dtype = "bool")#candidate|12003|(112,)|const|bool
call_11996 = relay.TupleGetItem(func_6060_call(relay.reshape(var_11997.astype('float32'), [2, 4, 8]), relay.reshape(const_11998.astype('int32'), [15, 4]), relay.reshape(const_11999.astype('int8'), [756,]), relay.reshape(const_12000.astype('float64'), [192,]), relay.reshape(var_12001.astype('float64'), [720,]), relay.reshape(var_12002.astype('int8'), [1, 288]), relay.reshape(const_12003.astype('bool'), [112,]), ), 11)
call_12004 = relay.TupleGetItem(func_6069_call(relay.reshape(var_11997.astype('float32'), [2, 4, 8]), relay.reshape(const_11998.astype('int32'), [15, 4]), relay.reshape(const_11999.astype('int8'), [756,]), relay.reshape(const_12000.astype('float64'), [192,]), relay.reshape(var_12001.astype('float64'), [720,]), relay.reshape(var_12002.astype('int8'), [1, 288]), relay.reshape(const_12003.astype('bool'), [112,]), ), 11)
output = relay.Tuple([call_11980,call_11982,call_11986,call_11996,var_11997,const_11998,const_11999,const_12000,var_12001,var_12002,const_12003,])
output2 = relay.Tuple([call_11981,call_11983,call_11987,call_12004,var_11997,const_11998,const_11999,const_12000,var_12001,var_12002,const_12003,])
func_12013 = relay.Function([var_11997,var_12001,var_12002,], output)
mod['func_12013'] = func_12013
mod = relay.transform.InferType()(mod)
var_12014 = relay.var("var_12014", dtype = "float32", shape = (64,))#candidate|12014|(64,)|var|float32
var_12015 = relay.var("var_12015", dtype = "float64", shape = (720,))#candidate|12015|(720,)|var|float64
var_12016 = relay.var("var_12016", dtype = "int8", shape = (4, 72))#candidate|12016|(4, 72)|var|int8
output = func_12013(var_12014,var_12015,var_12016,)
func_12017 = relay.Function([var_12014,var_12015,var_12016,], output)
mutated_mod['func_12017'] = func_12017
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12022 = relay.var("var_12022", dtype = "bool", shape = (13, 14, 16))#candidate|12022|(13, 14, 16)|var|bool
var_12023 = relay.var("var_12023", dtype = "bool", shape = (13, 14, 16))#candidate|12023|(13, 14, 16)|var|bool
bop_12024 = relay.logical_or(var_12022.astype('bool'), relay.reshape(var_12023.astype('bool'), relay.shape_of(var_12022))) # shape=(13, 14, 16)
output = relay.Tuple([bop_12024,])
output2 = relay.Tuple([bop_12024,])
func_12029 = relay.Function([var_12022,var_12023,], output)
mod['func_12029'] = func_12029
mod = relay.transform.InferType()(mod)
var_12030 = relay.var("var_12030", dtype = "bool", shape = (13, 14, 16))#candidate|12030|(13, 14, 16)|var|bool
var_12031 = relay.var("var_12031", dtype = "bool", shape = (13, 14, 16))#candidate|12031|(13, 14, 16)|var|bool
output = func_12029(var_12030,var_12031,)
func_12032 = relay.Function([var_12030,var_12031,], output)
mutated_mod['func_12032'] = func_12032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5648_call = mod.get_global_var('func_5648')
func_5649_call = mutated_mod.get_global_var('func_5649')
call_12150 = func_5648_call()
call_12151 = func_5648_call()
output = relay.Tuple([call_12150,])
output2 = relay.Tuple([call_12151,])
func_12166 = relay.Function([], output)
mod['func_12166'] = func_12166
mod = relay.transform.InferType()(mod)
output = func_12166()
func_12167 = relay.Function([], output)
mutated_mod['func_12167'] = func_12167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9147_call = mod.get_global_var('func_9147')
func_9149_call = mutated_mod.get_global_var('func_9149')
call_12185 = relay.TupleGetItem(func_9147_call(), 0)
call_12186 = relay.TupleGetItem(func_9149_call(), 0)
output = call_12185
output2 = call_12186
func_12193 = relay.Function([], output)
mod['func_12193'] = func_12193
mod = relay.transform.InferType()(mod)
mutated_mod['func_12193'] = func_12193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12193_call = mutated_mod.get_global_var('func_12193')
call_12194 = func_12193_call()
output = call_12194
func_12195 = relay.Function([], output)
mutated_mod['func_12195'] = func_12195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9298_call = mod.get_global_var('func_9298')
func_9299_call = mutated_mod.get_global_var('func_9299')
call_12202 = relay.TupleGetItem(func_9298_call(), 1)
call_12203 = relay.TupleGetItem(func_9299_call(), 1)
output = relay.Tuple([call_12202,])
output2 = relay.Tuple([call_12203,])
func_12224 = relay.Function([], output)
mod['func_12224'] = func_12224
mod = relay.transform.InferType()(mod)
output = func_12224()
func_12225 = relay.Function([], output)
mutated_mod['func_12225'] = func_12225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6644_call = mod.get_global_var('func_6644')
func_6645_call = mutated_mod.get_global_var('func_6645')
call_12260 = relay.TupleGetItem(func_6644_call(), 2)
call_12261 = relay.TupleGetItem(func_6645_call(), 2)
output = call_12260
output2 = call_12261
func_12262 = relay.Function([], output)
mod['func_12262'] = func_12262
mod = relay.transform.InferType()(mod)
mutated_mod['func_12262'] = func_12262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12262_call = mutated_mod.get_global_var('func_12262')
call_12263 = func_12262_call()
output = call_12263
func_12264 = relay.Function([], output)
mutated_mod['func_12264'] = func_12264
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12342 = relay.var("var_12342", dtype = "float32", shape = (12, 16, 14))#candidate|12342|(12, 16, 14)|var|float32
uop_12343 = relay.sigmoid(var_12342.astype('float32')) # shape=(12, 16, 14)
func_10387_call = mod.get_global_var('func_10387')
func_10388_call = mutated_mod.get_global_var('func_10388')
call_12347 = relay.TupleGetItem(func_10387_call(), 0)
call_12348 = relay.TupleGetItem(func_10388_call(), 0)
uop_12365 = relay.acosh(uop_12343.astype('float64')) # shape=(12, 16, 14)
output = relay.Tuple([call_12347,uop_12365,])
output2 = relay.Tuple([call_12348,uop_12365,])
func_12376 = relay.Function([var_12342,], output)
mod['func_12376'] = func_12376
mod = relay.transform.InferType()(mod)
mutated_mod['func_12376'] = func_12376
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12377 = relay.var("var_12377", dtype = "float32", shape = (12, 16, 14))#candidate|12377|(12, 16, 14)|var|float32
func_12376_call = mutated_mod.get_global_var('func_12376')
call_12378 = func_12376_call(var_12377)
output = call_12378
func_12379 = relay.Function([var_12377], output)
mutated_mod['func_12379'] = func_12379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10863_call = mod.get_global_var('func_10863')
func_10864_call = mutated_mod.get_global_var('func_10864')
call_12384 = relay.TupleGetItem(func_10863_call(), 0)
call_12385 = relay.TupleGetItem(func_10864_call(), 0)
func_8053_call = mod.get_global_var('func_8053')
func_8054_call = mutated_mod.get_global_var('func_8054')
call_12406 = relay.TupleGetItem(func_8053_call(), 0)
call_12407 = relay.TupleGetItem(func_8054_call(), 0)
output = relay.Tuple([call_12384,call_12406,])
output2 = relay.Tuple([call_12385,call_12407,])
func_12411 = relay.Function([], output)
mod['func_12411'] = func_12411
mod = relay.transform.InferType()(mod)
mutated_mod['func_12411'] = func_12411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12411_call = mutated_mod.get_global_var('func_12411')
call_12412 = func_12411_call()
output = call_12412
func_12413 = relay.Function([], output)
mutated_mod['func_12413'] = func_12413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11786_call = mod.get_global_var('func_11786')
func_11787_call = mutated_mod.get_global_var('func_11787')
call_12489 = relay.TupleGetItem(func_11786_call(), 0)
call_12490 = relay.TupleGetItem(func_11787_call(), 0)
uop_12498 = relay.atan(call_12489.astype('float32')) # shape=(6, 12, 2)
uop_12500 = relay.atan(call_12490.astype('float32')) # shape=(6, 12, 2)
output = uop_12498
output2 = uop_12500
func_12506 = relay.Function([], output)
mod['func_12506'] = func_12506
mod = relay.transform.InferType()(mod)
output = func_12506()
func_12507 = relay.Function([], output)
mutated_mod['func_12507'] = func_12507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6529_call = mod.get_global_var('func_6529')
func_6531_call = mutated_mod.get_global_var('func_6531')
call_12584 = relay.TupleGetItem(func_6529_call(), 0)
call_12585 = relay.TupleGetItem(func_6531_call(), 0)
func_9837_call = mod.get_global_var('func_9837')
func_9838_call = mutated_mod.get_global_var('func_9838')
call_12598 = relay.TupleGetItem(func_9837_call(), 1)
call_12599 = relay.TupleGetItem(func_9838_call(), 1)
uop_12621 = relay.acosh(call_12598.astype('float32')) # shape=(12, 7, 5)
uop_12623 = relay.acosh(call_12599.astype('float32')) # shape=(12, 7, 5)
func_1144_call = mod.get_global_var('func_1144')
func_1147_call = mutated_mod.get_global_var('func_1147')
const_12626 = relay.const([8.459563,-2.662982,-1.677014,-7.795011,4.982718,1.436736,-6.611565,0.112000,-7.890687,8.946275,-5.007829,6.484280,-1.850059,7.120812,-9.988304,-8.351845,-5.527872,-5.248392,6.847084,-4.118112,-9.104771,-3.498739,-7.246365,-6.638694,4.950046,2.992774,8.004212,7.376036,4.894430,4.377379,-8.786098,-4.079621,-4.444631,6.946477,6.671176,-2.089118,8.922232,-7.258096,-4.559365,-6.969105,-1.845989,9.331414,-7.842657,2.429505,3.222742,-6.551301,-9.014893,5.277390,6.066097,6.777198,-6.916134,7.896835,-1.424532,7.304584,-3.300612,0.226077,-0.605524,-6.820326,7.464335,-0.389246,-7.136258,-6.012747,7.807613,7.222554,-2.948256,1.187771,-6.886686,-1.431032,-6.266574,7.029267,7.499590,-8.489233,9.169437,5.355128,-0.505980,-3.693235,-6.387929,-6.603024,-5.734185,-4.857113,-8.473251,5.753046,-6.430757,8.524019,2.628295,-5.790123,5.428025,-2.425066,5.454580,-9.920717,-3.263998,7.744535,1.033821,-3.333233,0.404845,7.414442,4.860224,0.185452,-6.392701,-0.444629,9.226020,8.478898,4.692835,-3.595936,3.941397,4.361914,4.094466,-8.078398,-6.059690,-3.578542,5.022491,7.182396,-3.656902,5.327699,3.589009,-1.912728,-2.668086,-3.709972,-8.461340,-2.929699,5.782708,2.761117,-2.660646,5.045715,-5.796259,5.407061,5.810353,-3.282620,9.819554,9.997223,-9.666642,2.812152,4.556354,-9.574836,-3.519029,5.142156,-6.020877,-6.649995,-0.145717,5.368559,7.121953,-5.985428,7.395340,-1.508817,-1.051419,-4.919406,-4.102733,1.739234,5.228750,3.522358,1.717702,3.960130,3.132475,-6.652024,9.297198,-8.125673,-4.843269,-1.827419,-5.740915,-9.533449,-0.805768,1.004136,0.102308,-2.146235,-1.264475,-6.687760,-9.745592,-7.969449,-8.980321,2.888912,-2.628232,-8.453472,-4.173525,1.043710,-4.159772,-5.842120,-6.652295,1.530910,-0.424756,-7.217741,6.623099,-8.071238,-4.677737,1.303463,-8.222543,-5.444864,-9.191936,1.045828,7.363590,0.313074,2.880409,-5.293729], dtype = "float64")#candidate|12626|(192,)|const|float64
call_12625 = func_1144_call(relay.reshape(const_12626.astype('float64'), [3, 4, 16]))
call_12627 = func_1144_call(relay.reshape(const_12626.astype('float64'), [3, 4, 16]))
func_11348_call = mod.get_global_var('func_11348')
func_11349_call = mutated_mod.get_global_var('func_11349')
call_12641 = func_11348_call()
call_12642 = func_11348_call()
func_7941_call = mod.get_global_var('func_7941')
func_7942_call = mutated_mod.get_global_var('func_7942')
call_12659 = relay.TupleGetItem(func_7941_call(), 0)
call_12660 = relay.TupleGetItem(func_7942_call(), 0)
func_2936_call = mod.get_global_var('func_2936')
func_2940_call = mutated_mod.get_global_var('func_2940')
var_12683 = relay.var("var_12683", dtype = "int32", shape = (1350,))#candidate|12683|(1350,)|var|int32
call_12682 = func_2936_call(relay.reshape(var_12683.astype('int32'), [15, 6, 15]), relay.reshape(var_12683.astype('int32'), [15, 6, 15]), )
call_12684 = func_2936_call(relay.reshape(var_12683.astype('int32'), [15, 6, 15]), relay.reshape(var_12683.astype('int32'), [15, 6, 15]), )
func_1954_call = mod.get_global_var('func_1954')
func_1958_call = mutated_mod.get_global_var('func_1958')
var_12697 = relay.var("var_12697", dtype = "float32", shape = (140,))#candidate|12697|(140,)|var|float32
call_12696 = relay.TupleGetItem(func_1954_call(relay.reshape(var_12697.astype('float32'), [4, 5, 7]), relay.reshape(var_12697.astype('float32'), [4, 5, 7]), ), 0)
call_12698 = relay.TupleGetItem(func_1958_call(relay.reshape(var_12697.astype('float32'), [4, 5, 7]), relay.reshape(var_12697.astype('float32'), [4, 5, 7]), ), 0)
output = relay.Tuple([call_12584,uop_12621,call_12625,const_12626,call_12641,call_12659,call_12682,var_12683,call_12696,var_12697,])
output2 = relay.Tuple([call_12585,uop_12623,call_12627,const_12626,call_12642,call_12660,call_12684,var_12683,call_12698,var_12697,])
func_12712 = relay.Function([var_12683,var_12697,], output)
mod['func_12712'] = func_12712
mod = relay.transform.InferType()(mod)
mutated_mod['func_12712'] = func_12712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12712_call = mutated_mod.get_global_var('func_12712')
var_12714 = relay.var("var_12714", dtype = "int32", shape = (1350,))#candidate|12714|(1350,)|var|int32
var_12715 = relay.var("var_12715", dtype = "float32", shape = (140,))#candidate|12715|(140,)|var|float32
call_12713 = func_12712_call(var_12714,var_12715,)
output = call_12713
func_12716 = relay.Function([var_12714,var_12715,], output)
mutated_mod['func_12716'] = func_12716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11220_call = mod.get_global_var('func_11220')
func_11221_call = mutated_mod.get_global_var('func_11221')
call_12731 = func_11220_call()
call_12732 = func_11220_call()
output = call_12731
output2 = call_12732
func_12742 = relay.Function([], output)
mod['func_12742'] = func_12742
mod = relay.transform.InferType()(mod)
mutated_mod['func_12742'] = func_12742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12742_call = mutated_mod.get_global_var('func_12742')
call_12743 = func_12742_call()
output = call_12743
func_12744 = relay.Function([], output)
mutated_mod['func_12744'] = func_12744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9335_call = mod.get_global_var('func_9335')
func_9336_call = mutated_mod.get_global_var('func_9336')
call_12781 = func_9335_call()
call_12782 = func_9335_call()
output = call_12781
output2 = call_12782
func_12812 = relay.Function([], output)
mod['func_12812'] = func_12812
mod = relay.transform.InferType()(mod)
mutated_mod['func_12812'] = func_12812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12812_call = mutated_mod.get_global_var('func_12812')
call_12813 = func_12812_call()
output = call_12813
func_12814 = relay.Function([], output)
mutated_mod['func_12814'] = func_12814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9298_call = mod.get_global_var('func_9298')
func_9299_call = mutated_mod.get_global_var('func_9299')
call_12838 = relay.TupleGetItem(func_9298_call(), 0)
call_12839 = relay.TupleGetItem(func_9299_call(), 0)
func_11271_call = mod.get_global_var('func_11271')
func_11273_call = mutated_mod.get_global_var('func_11273')
call_12847 = relay.TupleGetItem(func_11271_call(), 0)
call_12848 = relay.TupleGetItem(func_11273_call(), 0)
func_11578_call = mod.get_global_var('func_11578')
func_11579_call = mutated_mod.get_global_var('func_11579')
call_12852 = func_11578_call()
call_12853 = func_11578_call()
output = relay.Tuple([call_12838,call_12847,call_12852,])
output2 = relay.Tuple([call_12839,call_12848,call_12853,])
func_12858 = relay.Function([], output)
mod['func_12858'] = func_12858
mod = relay.transform.InferType()(mod)
mutated_mod['func_12858'] = func_12858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12858_call = mutated_mod.get_global_var('func_12858')
call_12859 = func_12858_call()
output = call_12859
func_12860 = relay.Function([], output)
mutated_mod['func_12860'] = func_12860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10131_call = mod.get_global_var('func_10131')
func_10132_call = mutated_mod.get_global_var('func_10132')
call_12885 = relay.TupleGetItem(func_10131_call(), 2)
call_12886 = relay.TupleGetItem(func_10132_call(), 2)
func_5392_call = mod.get_global_var('func_5392')
func_5399_call = mutated_mod.get_global_var('func_5399')
const_12888 = relay.const([True,True,False,True,False,False,False,True,True,False,True,True,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,True,False,True,True,True,True,True,False,True,False,True,False,True,True,True,False,True,True,False,True,True,True,False,False,False,True,False,False,False,False,False,True,False,True,False,False,False,False,False,True,False,True,True,True,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,True,True,True,False,True,True,True,True,True,True,False,True,True,True,False,False,False,True,True,False,False,True,True,True,False,False,True,True,True,False,False,False,True,False,True,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,True,True,False,False,False,False,True,False,True,False,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,True,True,True,False,False,False,False,True,True,False,False,True,True,False,True,False,False,True,True,True,True,True,False,False,True,False,True,False,True,False,True,False,True,False,True,True,False,True,True,True,True,True,True,True,True,False,True,True,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,True,True,True,True,True,False,False,True,False,True,False,True,False,False,False,True,True,False,True,True,True,True,True,True,False,False,True,False,False,False,False,False,True,False,True,False,False,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,False,False,False,False,True,True,True,True,True,False,True,False,False,False,True,True,False,False,False,False,True,True,True,False,False,True,True], dtype = "bool")#candidate|12888|(315,)|const|bool
var_12889 = relay.var("var_12889", dtype = "bool", shape = (112,))#candidate|12889|(112,)|var|bool
const_12890 = relay.const([[5.675577,-4.624688,-4.982841,-3.396882,5.745944,3.137510],[8.367380,-0.857645,0.395020,-7.714317,-5.397538,5.568286],[2.871315,2.054427,-2.375033,6.033693,9.134453,-9.945372],[-6.700043,8.628453,4.652357,-3.470100,9.790474,-6.756734],[-6.370391,3.358338,9.717675,7.826020,8.851614,-6.086147],[-3.238138,7.795682,-9.903003,4.652024,3.233200,-7.274163],[-1.563281,8.613211,7.715573,-4.992971,-8.909293,-1.430358],[-5.497761,-7.070527,1.888423,6.774954,1.098736,6.188278],[-8.047470,-3.866451,0.256914,2.274318,-4.321474,7.074007],[-4.699564,0.881621,-3.179913,2.795028,0.258710,-3.839906],[-8.370199,-4.545640,6.314657,4.671481,1.363780,0.099076],[1.518618,-4.981127,7.544089,7.097282,0.265702,7.469787],[3.193599,-5.094948,-6.546439,2.717783,3.294110,-1.391033],[2.231418,-2.489539,-6.729243,-9.538188,-5.324772,9.946541],[-2.373753,-9.421092,3.390468,1.146864,-8.596315,2.227624],[3.906479,9.181277,-9.956371,7.491590,-4.512402,-7.543769],[1.394847,-4.279964,5.930047,4.717233,-2.353524,1.632685],[1.717937,-5.766768,8.985722,0.623160,-5.442433,8.941201],[-3.205663,8.755696,-0.345192,9.610361,-9.332731,-3.492255],[0.705688,6.188390,5.814815,7.512573,-5.632942,-2.124614],[1.387027,-8.332666,-2.834676,0.484643,-6.669412,7.790623],[-0.686178,-7.372933,-3.553321,3.674208,-0.662948,-6.297854],[3.078671,2.068595,5.512870,7.698703,1.496416,3.008203],[4.249325,-7.154368,3.618288,5.953329,1.666469,-3.015319],[-0.749856,0.795933,-6.772343,-6.990564,-5.186570,3.780062],[4.747531,-8.919146,-4.227598,-0.919767,-2.170165,2.336070],[4.208126,-8.625169,-9.876652,-0.145069,-6.740371,-8.382450],[6.298428,-5.042331,-9.046545,-0.343688,9.002007,-3.263168],[-9.823826,6.359149,0.729910,-8.249658,8.509418,0.928668],[3.975953,-6.165344,-6.238190,-9.364511,8.438429,4.370672],[6.016849,1.871955,-8.693178,-2.512296,0.036907,-7.373038],[8.618668,4.037799,0.421764,-1.422149,-0.323978,-8.300038],[2.817884,7.949738,8.470536,-3.855677,-9.677300,7.092975],[6.904196,1.829312,-4.024822,-7.687996,-6.662250,-2.056548],[-2.656031,-8.789707,-7.570041,7.953817,4.300179,-9.831104],[0.171874,3.647397,8.415916,9.874824,2.908778,9.246892],[-1.064302,2.217343,0.676738,-5.041533,-3.579491,-3.536270],[7.732959,5.694733,-2.070975,2.668581,-9.678111,0.508886],[-6.756037,3.045836,8.088479,5.036226,-3.348702,-1.624692],[-1.329144,7.631550,4.928751,9.678345,-0.657563,-2.350003],[8.405391,-3.767035,-1.090832,9.038818,-1.326594,-7.409338],[2.170844,8.426503,-9.648573,8.463242,-6.052043,-8.454076]], dtype = "float64")#candidate|12890|(42, 6)|const|float64
var_12891 = relay.var("var_12891", dtype = "uint8", shape = (378,))#candidate|12891|(378,)|var|uint8
call_12887 = relay.TupleGetItem(func_5392_call(relay.reshape(const_12888.astype('bool'), [7, 9, 5]), relay.reshape(const_12888.astype('bool'), [7, 9, 5]), relay.reshape(var_12889.astype('bool'), [56, 2]), relay.reshape(const_12890.astype('float64'), [252,]), relay.reshape(var_12891.astype('uint8'), [378,]), ), 7)
call_12892 = relay.TupleGetItem(func_5399_call(relay.reshape(const_12888.astype('bool'), [7, 9, 5]), relay.reshape(const_12888.astype('bool'), [7, 9, 5]), relay.reshape(var_12889.astype('bool'), [56, 2]), relay.reshape(const_12890.astype('float64'), [252,]), relay.reshape(var_12891.astype('uint8'), [378,]), ), 7)
const_12895 = relay.const([[1.983161,-4.637157,-1.011448,-9.946079,-0.181091,3.027805,9.332910,-6.255150,4.869257,9.524564,-6.402399,5.756021,-8.633469,-7.568870,0.415185,5.655965,2.521827,-9.503863,-3.331413,-2.913804,-2.325652,2.960819,-9.956896,6.610376,0.528567,-3.582888,-7.456623,9.123891,1.206743,5.707122,5.137136,3.464205,-6.335326,-7.714157,-4.122288,3.141156,-9.687578,3.820664,-6.326071,-5.418342,3.598188,9.456156,5.182489,-1.597950,-9.736812,9.123740,3.523410,-9.574076,-4.038033,-3.429349,-9.293455,-8.205353,-1.341529,0.490661,-6.580957,2.789525,-8.119903,-2.407202,9.634567,-0.353535,-0.096321,6.267312,5.185020,8.699786,-7.180027,-8.975990,7.527449,5.984602,-4.258505,-8.372451,5.068530,-8.531761,-6.162121,9.976657,-0.745539,9.662831,0.477622,-5.117793,-7.478948,-9.861884,3.294327,4.547843,9.689946,3.268418,1.618187,7.885073,7.241862,-6.275803,-4.826625,1.257309,-8.882637,9.050744,3.831305,-9.121137,3.416770,-0.234198,2.620125,4.285004,-3.650505,2.650040,-0.553003,-3.239448,-5.875905,7.560923,-7.738704,0.950870,2.501157,-3.953346,-4.895684,-5.630971,-3.304600,9.888827,3.585744,-0.946041,1.322611,1.622852,-8.865007,3.109047,6.913044,8.638672,2.476141,-8.998445,3.273825,9.849521,3.651353,4.264688,-4.387566,0.105033,4.818685,6.959090,1.302887,-9.917576,2.167876,6.161711,-4.795724,-0.308017,7.066989,-2.871422,-7.117519,8.541082,-9.979600,3.844774,2.588448,-0.790738,-1.043769,2.181886,-9.118967,-1.079194,2.165116,-0.442137,-1.357165,6.011302,1.003578,9.832487,8.391347,3.632161,0.461180,-6.812125,-0.703154,-8.081274,-2.501651,-5.775618,4.711506,-8.457196,-2.018299,9.012770,-9.209434,0.849134,-5.789804,0.108903,9.965747,7.905291,7.159572,1.361580,-0.409907,-3.510864,8.923417,-8.181286,7.213919,5.565874,8.953233,5.969089,3.179553,-1.062757,0.538937,6.745809,-4.725464,1.675601,-7.846931,7.297644,-8.392010,5.199540],[0.525972,1.476795,7.378817,-1.003252,0.296339,-0.172637,-6.101346,-1.546459,-1.999111,-5.231963,0.571808,-5.734160,-2.792722,-6.341252,7.714171,-7.334375,1.024381,-3.585410,-6.145872,-7.895001,-6.896715,-0.792548,7.260850,-9.410050,-5.804923,-1.059553,-0.170873,7.214889,2.538686,-5.681310,-0.115503,9.618855,-3.537212,-6.143360,-8.299066,-0.973284,0.367101,-5.171522,0.707077,-6.968500,8.522505,7.992144,8.374251,0.336330,3.099155,5.193853,-3.614975,7.961110,-8.254192,-0.834257,-6.028892,0.984568,0.128321,-3.395852,-4.041257,2.062419,-7.918955,-9.330710,5.083579,-3.326638,6.767114,-9.742352,-6.385281,-8.225932,8.325738,8.772627,6.689758,3.680312,-7.718176,6.980632,-7.050659,9.991866,-3.647461,-7.094857,5.567578,-9.976586,2.312573,-1.171568,-8.570141,-0.988939,6.449574,-9.268540,7.523246,-8.372525,4.923226,-2.139079,-5.516835,-9.447936,7.235685,-9.376886,8.829196,1.707311,-9.995050,-4.387306,-9.961635,-9.939127,1.978448,-6.149575,2.898680,-6.078158,9.232121,-6.685610,-8.760070,-4.813401,-0.509316,-0.821914,1.041083,-9.108749,-0.321735,-9.172271,0.315054,-2.874201,4.589206,8.379042,9.807837,-3.189610,9.960003,-3.074791,1.268647,5.976848,-4.129956,-9.462349,-3.604593,2.747648,9.348234,7.100850,-2.913192,6.746855,2.017459,-3.220254,4.240950,6.453334,-2.806068,-9.910757,-5.622157,6.975126,-4.678082,-1.359376,-7.562523,1.763917,2.953601,-4.433392,-0.746912,-2.002388,3.047835,4.033912,3.886052,6.043619,-3.271503,3.983297,0.101028,6.879642,-2.442884,-1.894627,4.449760,8.006658,6.924366,7.545569,5.030394,6.818983,-2.231698,8.581421,0.541883,3.083499,4.974099,-8.374047,4.383788,-2.805825,2.999191,-3.168763,-7.466461,1.200233,-5.865130,7.225308,-3.576252,-3.930118,7.257674,-2.174940,-9.351373,2.968254,2.371144,-2.831606,8.085973,-5.764072,-6.118905,-5.198928,-9.273108,-4.900264,-1.377602,8.806154,-2.400686,3.292713],[3.515066,-0.786287,-4.772523,7.398702,3.742725,-2.703898,-8.406827,5.402643,-5.353094,6.456263,8.360037,8.416411,-5.312787,3.801387,-1.694869,-6.207306,-1.121082,6.395823,-0.494345,-7.272338,-1.838234,0.809157,-4.115747,7.634076,-5.474344,6.914065,-2.252151,4.780678,4.941250,0.822511,8.294312,-5.107502,-2.448509,-9.338842,-5.654715,-9.993743,-9.235292,-1.420244,-0.409475,3.281582,-1.448907,8.820280,6.930927,9.912175,0.844181,-6.810627,9.823343,-2.469976,-4.163704,-2.066764,-7.222602,8.219928,-8.597527,1.677799,-1.663930,8.451047,0.099167,7.624451,0.803474,-4.490993,-0.701581,-2.026325,7.720705,3.749700,2.152275,-3.887348,1.271350,-2.664373,1.233187,-5.537373,-1.531004,4.826688,-2.434213,-1.434227,7.345818,-1.542435,2.512930,0.252481,-1.044733,-2.111495,8.638282,0.543234,9.708323,-2.003640,8.068208,-3.218599,1.621769,7.696393,-6.232491,1.002194,-1.531909,7.732098,-2.946666,-4.681928,-8.795386,6.527628,-4.992782,-9.177181,-5.185894,-3.339628,9.222881,-7.372323,-8.123268,7.324152,9.460518,3.405109,-0.885496,-4.919069,7.611975,9.649870,9.049763,0.350743,5.941163,0.405410,4.732923,3.493318,-5.232348,0.787688,-5.320338,-3.354413,0.292499,4.587645,-9.276980,5.856140,7.769202,7.838005,6.848433,-9.246134,-0.526884,-7.291343,7.957848,6.127517,6.505876,2.471463,8.111200,-2.863947,0.538098,-5.743447,9.483015,3.629155,6.759071,2.569922,-3.847998,9.709174,-8.046953,-4.293290,-4.163815,9.374097,-2.571633,9.607593,-2.578914,-4.384727,7.465967,-3.427567,-6.408417,0.577986,-5.831947,-1.209267,-3.774167,-4.852045,-9.095097,5.021101,-7.006817,-4.415011,2.644257,-3.035043,1.680316,8.244056,9.279853,1.807967,3.658279,7.413342,-1.480193,-1.034883,-4.659490,7.297699,8.946529,7.568851,7.449770,-4.989750,8.548373,7.757014,-6.964308,5.214048,-4.974073,7.882527,-5.393680,2.468532,5.443740,3.736886,-5.385114,-6.712135],[7.468760,3.651892,7.598094,7.298174,-1.023977,-2.832106,2.161573,1.069110,-1.281973,-6.888148,0.391646,9.194174,5.987793,-2.125811,3.526623,-1.431337,-8.440590,-3.695239,0.362913,-0.908594,-4.529786,-2.728621,4.976212,1.543591,0.762800,-8.672531,4.633555,3.336445,-1.398543,9.608779,-9.778114,4.381253,8.299833,-0.624822,1.589544,3.575057,6.378288,-6.799856,8.442848,5.934393,4.940498,1.295463,2.936933,1.492395,8.411368,-0.412710,-9.692692,-4.978093,8.616270,1.058723,-5.377557,-3.962952,-1.030170,-2.530048,-0.234128,-4.283466,4.185960,-9.814009,-6.403724,-4.042126,-3.224653,8.482311,-5.410187,1.627481,2.889999,1.613449,4.428979,8.641889,-8.753658,0.264149,1.607429,-0.878934,8.332538,-3.571179,-8.030344,4.610549,1.632833,-5.532969,6.497601,0.884117,-8.014249,-5.944173,-3.190934,6.832330,0.194533,9.233959,3.161233,4.511967,-4.843377,-2.083009,-9.637351,-2.018748,3.113231,-8.655705,-9.808800,0.398805,-7.704616,-2.382129,8.050132,2.515533,-9.601174,-5.509903,-8.355846,-3.638990,0.300638,2.764654,6.740794,2.058010,-2.993696,8.868031,8.742851,1.667414,-5.484679,-8.690731,-7.869445,-5.257697,-5.797934,-5.799047,-0.582234,2.935268,2.405111,8.315909,-2.942603,4.083726,-4.653656,1.142662,9.936892,6.021494,-2.798096,-9.536655,7.472933,5.134458,0.260842,-5.673025,0.092436,1.595800,6.389144,4.374315,2.092139,-5.480683,2.020754,7.206024,5.610336,-2.032595,-3.767823,-5.471129,8.446507,9.853175,6.986666,-1.371000,5.837444,6.438968,-6.455694,6.218398,-5.672408,-1.394590,8.408193,-7.157424,-2.073750,0.510039,2.876270,4.711694,2.573511,1.782251,-2.973214,4.524015,0.247057,-6.705642,8.422737,7.448367,-2.758273,8.438260,1.521268,-4.216273,-8.732191,-6.880683,2.530525,-6.478488,-3.254684,9.685242,2.389464,6.750973,2.815892,9.304843,2.927881,-8.038790,-4.581072,8.176508,-8.623111,7.131298,4.635421,-4.749671],[9.155539,-2.826899,5.187774,0.996608,-1.209239,7.152060,-4.683994,9.459946,-5.936342,6.319040,2.938464,-2.214804,-7.790867,5.402770,-7.583345,-9.656822,-3.836082,2.967444,-1.078187,2.556392,2.945698,8.860910,3.759334,4.991176,-5.178385,-0.387329,-3.034147,5.588622,-0.654839,-5.808221,3.457552,3.667676,9.089039,7.676915,3.869266,3.007191,8.401568,-4.475660,8.835720,-9.138703,3.614824,4.296693,-0.676221,-3.416312,1.023398,4.089939,-7.875448,7.613788,9.033835,1.651188,8.425651,-7.675180,1.756281,4.746272,-7.104706,5.827659,-5.246381,4.278059,0.403766,7.939617,4.590123,1.346907,9.972631,7.897980,5.894346,6.991257,5.021472,-8.986567,9.175239,2.623358,8.346997,4.319134,-2.362588,-9.825302,-1.193193,-0.542117,-0.161215,1.098636,-9.113708,2.331985,-3.615710,-5.837916,-4.652019,-8.356057,-8.196925,9.012430,-8.588884,9.429843,-3.874247,6.247544,-8.233988,-2.135357,1.670242,-1.360397,-0.624703,-4.883347,8.602723,1.722586,7.896429,6.473203,7.272484,3.745721,2.034773,-9.372211,0.926902,-5.970992,-7.457333,-4.505080,2.999043,6.933658,-9.936998,-9.543927,3.285612,4.845348,8.172197,-3.603007,-3.679661,9.801579,1.899849,5.967823,8.817811,-1.977886,-9.046384,0.502524,8.799269,1.352877,-8.004616,2.026111,4.576837,-5.329812,2.305509,-3.101980,7.413827,6.586885,1.857494,7.677211,6.338031,-1.123975,-6.619183,7.509410,0.559411,-3.602299,-4.208127,7.436234,-6.724777,-4.483338,-3.417135,9.199173,-2.590054,-3.761726,1.406279,-2.616919,1.492030,-6.523273,5.043264,-0.037436,0.895609,-8.015557,-5.625985,9.902482,-6.024576,2.141957,-8.593489,-5.076621,1.790063,9.638970,-4.522423,6.424699,-7.385995,0.825559,0.011586,-0.076424,-4.321675,-5.240920,-9.446584,-2.072176,-5.875680,-7.274831,-4.767649,3.703331,0.832614,7.346637,1.010093,-3.987687,-2.061990,2.365806,7.354261,-8.992922,-6.321639,-1.617985,2.582130,3.652803],[-8.638755,-6.581377,-9.254422,1.069564,-7.698922,4.142363,7.313726,-0.434804,-8.241761,-8.767189,2.304242,0.499006,8.861885,7.901834,-7.022840,-2.037125,-3.323400,-1.973055,3.460674,-3.011090,-0.586113,6.374222,0.130936,2.776358,3.063487,1.703551,2.473409,-2.174381,0.345788,7.730188,7.239097,-5.032763,-5.415820,-4.551173,-9.535780,-5.736876,4.145650,5.213317,4.599432,-1.192253,-2.633039,5.501869,-8.245609,-4.785278,5.206483,-2.826928,-0.270710,-3.686742,3.001952,-7.517921,-4.482181,-4.813599,-5.021795,-8.313002,-0.437562,-5.455150,7.271422,-7.221281,8.662660,3.353473,-9.290722,7.350244,-0.762764,-5.857157,4.663111,-0.087637,3.850666,1.119220,-5.471380,9.148178,-2.161845,3.124467,6.933655,0.193643,-3.089272,-2.934223,-8.849697,0.446095,8.536025,-4.769248,-6.388327,-0.683359,9.505313,4.520460,-8.886702,5.857160,-8.961339,-1.043090,-5.696970,0.807960,-2.241980,-5.856493,0.637622,4.974849,6.850318,9.802384,-7.026136,3.558639,9.187072,4.631612,8.249731,-3.640103,5.695957,4.445445,7.991421,7.561640,-8.983682,-5.770302,9.934448,1.958944,-5.734380,6.004237,-2.134293,-2.932808,5.814856,0.563441,-7.778309,0.513202,-0.548324,-4.982240,8.837705,9.832469,9.168673,4.428806,-6.041378,1.925945,-9.969279,1.016298,6.417736,-1.418313,-3.442999,6.209983,-1.263059,-2.024368,9.241002,-9.586757,-6.822108,8.514441,8.209736,8.231733,9.230552,-9.070895,0.855719,-4.227106,-3.111417,9.810882,9.844639,1.312561,3.863803,-8.127692,-9.865512,4.436672,5.735373,-6.230106,-4.414024,-8.073180,-9.162975,5.576682,-5.944705,-7.416303,-5.394782,4.072925,-2.898256,3.217566,9.871649,5.332629,-6.927309,-0.613361,2.194004,9.727755,-4.843202,8.905118,-1.092771,-5.803068,-7.277019,0.917402,4.501608,-5.197691,-8.328663,7.970738,-8.718290,1.559544,-9.924888,-2.910750,6.855549,3.379094,0.175233,-0.930161,6.391731,-1.507378,-2.565962,-0.258495],[3.744616,2.926193,9.591772,0.792092,1.302360,-8.259162,-1.645236,8.721033,-7.924510,-4.051586,6.673825,-7.840445,9.937534,9.035585,-1.237228,9.749924,-7.204275,9.062698,-0.066948,3.639711,-3.359259,7.871360,-7.001994,-4.091564,2.217296,-6.195695,9.726294,9.778071,-0.333635,-0.533289,-0.404408,-3.299241,3.704608,-2.561639,-8.617967,0.583100,-3.437017,1.208827,-3.339514,6.632142,-4.587938,-6.125825,-9.193799,0.590863,-0.051882,-7.220770,7.122344,-9.207037,-4.492472,-5.460072,-3.629882,6.137306,-9.733901,-9.935752,-8.929978,-9.549972,3.847288,3.066253,-5.793031,-7.445297,-6.299764,-8.365401,3.182392,-3.699125,6.234931,-8.990163,4.908458,-7.426632,8.173386,-1.226333,1.524488,-2.632924,1.144302,-3.518765,-5.390025,4.418407,4.967547,9.658105,-5.548444,0.487811,-1.322745,5.762569,0.717568,-9.436743,-6.160071,4.326524,4.098940,4.341813,8.439906,0.176813,-7.823351,-5.804027,-9.755205,1.924199,-3.179519,-5.209912,-6.245698,-4.274760,-0.108199,-8.324801,6.075018,-5.949858,-8.029629,6.066000,9.543207,9.052104,6.540889,-9.207724,9.279139,-4.071313,-8.762911,5.235997,9.961968,-7.050864,-6.633801,-0.120357,-8.186508,-7.330999,-4.864886,-6.356449,-9.414677,-8.244323,-4.211547,1.590993,-6.319069,9.776775,7.386942,9.166208,-2.501907,-1.348229,1.506571,-7.425438,8.024460,-7.682803,-7.897552,0.582369,-9.355612,7.333243,-2.544242,0.992140,-8.059619,4.144981,8.252231,-0.611109,1.222836,-8.925846,-3.880621,-1.174060,2.067504,6.886380,-1.117120,1.662768,-7.877913,2.327880,7.030300,3.760837,8.925490,3.589415,-6.128608,-7.084775,-2.293976,-3.228252,1.021124,-0.739099,3.541770,-6.200504,2.979176,-3.723469,-2.837887,-2.086639,-1.780214,-9.895977,6.374384,-9.212020,0.049304,8.186966,7.933078,-2.237526,-1.064842,-4.240646,6.237578,2.366977,-4.128720,-8.793949,7.095257,-9.928607,4.563567,0.883405,4.427831,-7.089396,-1.222572,-6.393253]], dtype = "float64")#candidate|12895|(7, 192)|const|float64
bop_12896 = relay.bitwise_or(call_12887.astype('int32'), const_12895.astype('int32')) # shape=(7, 192)
bop_12899 = relay.bitwise_or(call_12892.astype('int32'), const_12895.astype('int32')) # shape=(7, 192)
func_6060_call = mod.get_global_var('func_6060')
func_6069_call = mutated_mod.get_global_var('func_6069')
var_12905 = relay.var("var_12905", dtype = "float32", shape = (8, 8))#candidate|12905|(8, 8)|var|float32
var_12906 = relay.var("var_12906", dtype = "int32", shape = (60,))#candidate|12906|(60,)|var|int32
const_12907 = relay.const([-4,7,8,4,-8,4,4,-3,-3,-1,3,4,4,7,-3,-5,-3,6,8,5,10,-7,9,7,7,1,-5,-7,4,-1,6,3,-10,-9,10,-4,3,7,3,6,-4,-9,3,-6,-2,3,4,-7,6,3,-10,-10,-2,7,-3,-5,-9,5,-4,8,-9,6,-8,8,-7,-1,1,1,10,-9,2,-1,-10,-4,7,-2,2,10,1,5,-10,-8,-10,2,-9,-3,7,-4,10,3,10,6,5,4,-5,-5,-5,-5,2,-5,10,-5,-1,6,-7,-1,-8,2,6,-1,-7,5,1,-7,1,7,-9,10,1,3,7,-6,-4,10,8,-10,-10,-5,7,4,-3,1,3,-3,-7,2,-2,-3,-9,-6,-4,10,-1,3,-8,-6,-9,-6,-8,5,-7,3,5,6,9,-3,-8,5,9,-7,-8,-1,-2,9,5,-5,-3,2,6,-4,-1,6,-9,9,2,6,-1,-6,3,2,1,10,8,4,3,-7,-4,-4,-5,-10,2,-6,4,-5,9,-6,-5,-6,10,6,-7,-8,7,3,-8,8,10,3,6,-2,-3,5,5,-2,-1,-10,3,-9,-1,-4,-7,7,6,3,7,-7,4,-10,-5,-5,1,5,3,-6,-6,3,3,-3,1,-3,9,-1,-3,-1,-3,3,4,-10,1,3,-6,-3,10,8,-9,-2,-10,-1,-3,-1,1,-2,1,-3,-10,2,-5,-7,-10,-8,5,-7,-2,9,-3,4,4,10,-10,2,9,5,8,9,-6,-6,7,-9,-4,-6,9,-2,6,2,4,5,5,-7,2,2,-5,3,2,2,-10,-2,8,4,7,-9,8,-4,4,8,9,5,8,7,10,5,-10,7,-2,-4,-6,10,7,-7,-5,-8,-6,-8,1,-6,5,-10,-10,-2,9,3,-9,9,9,8,2,-10,-8,-5,-6,-1,4,-7,-8,9,5,3,7,3,-8,1,6,10,-10,5,8,8,-7,8,-3,5,1,5,9,-5,8,7,-7,-8,-4,6,8,5,8,3,2,-9,-5,2,-2,-9,7,6,4,3,-8,-1,-3,-4,-2,2,4,-9,-8,10,-2,-2,-8,-2,-2,-10,6,-7,-2,1,7,-9,5,-9,-1,-2,-2,9,-1,-10,-8,3,6,2,-2,-5,6,-9,4,-3,1,-5,10,-10,-6,5,-5,-7,-10,-10,-2,1,-8,9,2,-6,-7,-3,6,-7,-6,-6,1,-3,-2,3,-7,-4,-7,-9,-6,10,-6,10,8,4,-2,-6,-4,5,-3,2,3,7,2,8,8,1,5,-8,9,-9,-4,5,6,-6,8,-9,5,-2,-9,-4,2,-5,-5,10,-4,-6,-5,-8,10,-10,-1,1,4,-4,-6,1,2,-5,-8,-4,3,3,-2,9,-5,2,7,-4,9,-3,4,4,-10,6,3,2,-1,-2,-6,-9,-9,6,6,-6,-6,1,4,10,6,4,6,-5,-1,-2,-9,7,-1,5,-3,-4,1,2,3,-1,-8,8,3,4,10,2,-6,9,-3,7,-9,-8,-6,-8,-4,10,6,-7,1,2,9,3,4,-5,10,7,-2,-10,5,1,-8,1,-7,2,2,-1,9,-6,-8,4,-2,-5,-3,-7,4,-8,-7,6,-9,-3,-4,2,10,8,9,-6,-10,7,8,4,2,-2,-10,6,-7,-10,5,6,-2,-3,-6,-1,-2,2,4,1,7,-6,4,-6,-1,3,10,1,-4,2,7,-10,4,10,7,4,7,-1,-2,-3,7,10,7,-9,10,-3,-5,-6,5,6,7,8,-10,6,-7,-6,7,4,-9,-5,4,-6,10,-9,7,-7,-7,-8,-5,10,3,6,6,-4,-3,-4,6,10,-1,1,6,2,-2,-2,-7,8,-10,2,6,-1,-4,8,6,-5,6,-4,-3,-6,9,1,2,-7,-6,8,-6,1,-5,-9,-6,7,10,6,2,-10,2,8,-3,-6,-6,10,-5,-2,-9,-3,-7,7,-6,3,-5,-8,6,-10,-4,7,1,2,10,8,6,6], dtype = "int8")#candidate|12907|(756,)|const|int8
var_12908 = relay.var("var_12908", dtype = "float64", shape = (720,))#candidate|12908|(720,)|var|float64
const_12909 = relay.const([7,-4,4,-6,10,5,-2,-9,-9,1,5,10,-9,-10,-10,-1,-4,8,4,-10,9,-4,2,-3,-10,-4,6,-3,-1,-8,-4,8,4,8,1,4,-5,-3,2,9,-2,-8,-9,3,-6,2,2,9,-7,3,7,2,-6,1,2,-9,-5,3,10,3,-9,-5,5,6,-3,2,6,3,10,1,4,-4,-9,-2,-3,2,-9,2,4,-8,8,-6,3,-8,3,-4,-9,7,-5,6,3,-1,-8,-6,2,-7,3,5,-5,8,-2,5,1,1,1,6,-5,4,-2,6,-4,4,-8,-3,2,9,4,-5,-7,2,4,-2,7,-4,6,-4,-3,-8,-7,-4,-2,3,10,-2,-8,7,-2,-3,-4,-9,9,3,-2,-2,1,8,-10,9,2,-7,6,2,-2,9,4,-10,-1,-4,5,-2,4,10,-2,4,-10,4,-4,6,-3,-3,2,9,-8,6,1,-10,7,-8,10,-5,-2,8,9,-3,-8,-1,-2,6,3,3,-2,-8,-2,-10,-6,-5,-7,-4,7,-9,4,7,-10,5,-5,-7,1,7,-2,8,-5,-6,-7,9,6,9,9,7,9,5,10,2,-9,-5,-8,-9,-7,5,5,-8,-3,-2,-4,-4,-1,-8,2,2,-1,-2,-9,3,-8,-10,4,6,6,2,7,3,-6,8,-5,1,7,-6,-8,4,7,9,-1,-1,-10,-7,2,6,-4,-7,-5,4,4,10,-1,8,-6,1,9,-8,-6,10,6,-5,-10,-9,3,-9,-5,10], dtype = "int8")#candidate|12909|(288,)|const|int8
call_12904 = relay.TupleGetItem(func_6060_call(relay.reshape(var_12905.astype('float32'), [2, 4, 8]), relay.reshape(var_12906.astype('int32'), [15, 4]), relay.reshape(const_12907.astype('int8'), [756,]), relay.reshape(call_12887.astype('float64'), [192,]), relay.reshape(var_12908.astype('float64'), [720,]), relay.reshape(const_12909.astype('int8'), [1, 288]), relay.reshape(var_12889.astype('bool'), [112,]), ), 12)
call_12910 = relay.TupleGetItem(func_6069_call(relay.reshape(var_12905.astype('float32'), [2, 4, 8]), relay.reshape(var_12906.astype('int32'), [15, 4]), relay.reshape(const_12907.astype('int8'), [756,]), relay.reshape(call_12887.astype('float64'), [192,]), relay.reshape(var_12908.astype('float64'), [720,]), relay.reshape(const_12909.astype('int8'), [1, 288]), relay.reshape(var_12889.astype('bool'), [112,]), ), 12)
output = relay.Tuple([call_12885,const_12888,var_12889,const_12890,var_12891,bop_12896,call_12904,var_12905,var_12906,const_12907,var_12908,const_12909,])
output2 = relay.Tuple([call_12886,const_12888,var_12889,const_12890,var_12891,bop_12899,call_12910,var_12905,var_12906,const_12907,var_12908,const_12909,])
func_12921 = relay.Function([var_12889,var_12891,var_12905,var_12906,var_12908,], output)
mod['func_12921'] = func_12921
mod = relay.transform.InferType()(mod)
mutated_mod['func_12921'] = func_12921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12921_call = mutated_mod.get_global_var('func_12921')
var_12923 = relay.var("var_12923", dtype = "bool", shape = (112,))#candidate|12923|(112,)|var|bool
var_12924 = relay.var("var_12924", dtype = "uint8", shape = (378,))#candidate|12924|(378,)|var|uint8
var_12925 = relay.var("var_12925", dtype = "float32", shape = (8, 8))#candidate|12925|(8, 8)|var|float32
var_12926 = relay.var("var_12926", dtype = "int32", shape = (60,))#candidate|12926|(60,)|var|int32
var_12927 = relay.var("var_12927", dtype = "float64", shape = (720,))#candidate|12927|(720,)|var|float64
call_12922 = func_12921_call(var_12923,var_12924,var_12925,var_12926,var_12927,)
output = call_12922
func_12928 = relay.Function([var_12923,var_12924,var_12925,var_12926,var_12927,], output)
mutated_mod['func_12928'] = func_12928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9298_call = mod.get_global_var('func_9298')
func_9299_call = mutated_mod.get_global_var('func_9299')
call_12998 = relay.TupleGetItem(func_9298_call(), 1)
call_12999 = relay.TupleGetItem(func_9299_call(), 1)
func_10997_call = mod.get_global_var('func_10997')
func_10999_call = mutated_mod.get_global_var('func_10999')
call_13000 = func_10997_call()
call_13001 = func_10997_call()
func_7805_call = mod.get_global_var('func_7805')
func_7806_call = mutated_mod.get_global_var('func_7806')
call_13004 = relay.TupleGetItem(func_7805_call(), 0)
call_13005 = relay.TupleGetItem(func_7806_call(), 0)
output = relay.Tuple([call_12998,call_13000,call_13004,])
output2 = relay.Tuple([call_12999,call_13001,call_13005,])
func_13017 = relay.Function([], output)
mod['func_13017'] = func_13017
mod = relay.transform.InferType()(mod)
mutated_mod['func_13017'] = func_13017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13017_call = mutated_mod.get_global_var('func_13017')
call_13018 = func_13017_call()
output = call_13018
func_13019 = relay.Function([], output)
mutated_mod['func_13019'] = func_13019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5512_call = mod.get_global_var('func_5512')
func_5513_call = mutated_mod.get_global_var('func_5513')
call_13094 = func_5512_call()
call_13095 = func_5512_call()
func_10775_call = mod.get_global_var('func_10775')
func_10776_call = mutated_mod.get_global_var('func_10776')
call_13100 = func_10775_call()
call_13101 = func_10775_call()
func_5733_call = mod.get_global_var('func_5733')
func_5736_call = mutated_mod.get_global_var('func_5736')
var_13113 = relay.var("var_13113", dtype = "int8", shape = (756,))#candidate|13113|(756,)|var|int8
call_13112 = relay.TupleGetItem(func_5733_call(relay.reshape(var_13113.astype('int8'), [756,])), 2)
call_13114 = relay.TupleGetItem(func_5736_call(relay.reshape(var_13113.astype('int8'), [756,])), 2)
output = relay.Tuple([call_13094,call_13100,call_13112,var_13113,])
output2 = relay.Tuple([call_13095,call_13101,call_13114,var_13113,])
func_13124 = relay.Function([var_13113,], output)
mod['func_13124'] = func_13124
mod = relay.transform.InferType()(mod)
mutated_mod['func_13124'] = func_13124
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13125 = relay.var("var_13125", dtype = "int8", shape = (756,))#candidate|13125|(756,)|var|int8
func_13124_call = mutated_mod.get_global_var('func_13124')
call_13126 = func_13124_call(var_13125)
output = call_13126
func_13127 = relay.Function([var_13125], output)
mutated_mod['func_13127'] = func_13127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11461_call = mod.get_global_var('func_11461')
func_11462_call = mutated_mod.get_global_var('func_11462')
call_13155 = relay.TupleGetItem(func_11461_call(), 1)
call_13156 = relay.TupleGetItem(func_11462_call(), 1)
output = call_13155
output2 = call_13156
func_13158 = relay.Function([], output)
mod['func_13158'] = func_13158
mod = relay.transform.InferType()(mod)
output = func_13158()
func_13159 = relay.Function([], output)
mutated_mod['func_13159'] = func_13159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7441_call = mod.get_global_var('func_7441')
func_7442_call = mutated_mod.get_global_var('func_7442')
call_13162 = relay.TupleGetItem(func_7441_call(), 0)
call_13163 = relay.TupleGetItem(func_7442_call(), 0)
output = call_13162
output2 = call_13163
func_13167 = relay.Function([], output)
mod['func_13167'] = func_13167
mod = relay.transform.InferType()(mod)
output = func_13167()
func_13168 = relay.Function([], output)
mutated_mod['func_13168'] = func_13168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11461_call = mod.get_global_var('func_11461')
func_11462_call = mutated_mod.get_global_var('func_11462')
call_13180 = relay.TupleGetItem(func_11461_call(), 1)
call_13181 = relay.TupleGetItem(func_11462_call(), 1)
func_8245_call = mod.get_global_var('func_8245')
func_8249_call = mutated_mod.get_global_var('func_8249')
const_13193 = relay.const([-8,7,-4,-6,-5,-2,-7,3,8,-9,-10,5,1,-5,5,9,10,-1,-8,-7,-3,10,-3,10,-6,10,-7,2,-7,6,-4,-7,-3,-3,7,-8,8,8,10,7,-8,-1,-10,-4,-1,2,7,2,-8,-5,-2,5,10,5,3,5,7,-8,-1,7,-3,9,-8,2,-5,-5,9,-1,3,-8,-8,-10,8,-3,10,-1,10,-5,-1,8,-3,5,1,10,1,-4,8,3,2,5,7,7,7,8,10,-6,-7,6,6,-5,3,-6,-3,-6,-5,1,8,1,-1,-5,-3,3,-3,-1,4,-8,3,-7,-2,-5,6,9,3,3,-9,4,-1,-3,5,-3,-9,-5,4,-1,5,-1,2,-8,2,-9,-10,-2,-2,-3,-10,-8,-7,1,5,6,-8,2,1,-4,-1,-3,-6,2,-1,-6,3,-9,-5,2,10,1,-6,-7,4,9,4,10,6,-7,9,9,-7,2,7,-3,5,7,8,-8,5,10,9,9,-2,-4,2,-2,-10,-1,10,5,6,7,-6,-6,6,2,6,3,-10,8,2,8,-4,-10,1,-10,-7,-2,-5,6,6,7,9,-9,-8,-10,-7,-4,-7,5,-10,-6,-5,-2,9,-2,-5,-7,2,5,3,2,-6,-10,1,-3,-2,9,-9,10,6,5,2,10,-7,3,2,9,2,-3,5,-5,6,6,3,-5,7,-4,9,-2,1,-8,3,-3,9,9,1,-2,-7,2,4,3,-5,-2,-1,3,-4,-6,-10,-3,6,-2,-7,4,3,-8,-5,-10,-7,7,1,-3,2,-1,8,-1,7,1,-6,-1,-5,5,1,-10,-10,-10,8,-5,1,-5,1,5,-7,-5,3,3,-7,8,6,8,-5,-6,-10,-7,8,-1,-8,-10,-5,10,-2,-6,3,-7,-1,4,1,-3,2,3,-10,8,3,4,2,-7,-7,3,8,1,-5,7,7,-7,10,9,-6,-9,-5,-8,7,1,-10,-5,4,-8,-1,5,5,-4,-3,6], dtype = "uint8")#candidate|13193|(378,)|const|uint8
var_13194 = relay.var("var_13194", dtype = "int32", shape = (60,))#candidate|13194|(60,)|var|int32
call_13192 = relay.TupleGetItem(func_8245_call(relay.reshape(const_13193.astype('uint8'), [378,]), relay.reshape(var_13194.astype('int32'), [60, 1]), ), 0)
call_13195 = relay.TupleGetItem(func_8249_call(relay.reshape(const_13193.astype('uint8'), [378,]), relay.reshape(var_13194.astype('int32'), [60, 1]), ), 0)
output = relay.Tuple([call_13180,call_13192,const_13193,var_13194,])
output2 = relay.Tuple([call_13181,call_13195,const_13193,var_13194,])
func_13219 = relay.Function([var_13194,], output)
mod['func_13219'] = func_13219
mod = relay.transform.InferType()(mod)
var_13220 = relay.var("var_13220", dtype = "int32", shape = (60,))#candidate|13220|(60,)|var|int32
output = func_13219(var_13220)
func_13221 = relay.Function([var_13220], output)
mutated_mod['func_13221'] = func_13221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11167_call = mod.get_global_var('func_11167')
func_11168_call = mutated_mod.get_global_var('func_11168')
call_13262 = func_11167_call()
call_13263 = func_11167_call()
func_8109_call = mod.get_global_var('func_8109')
func_8112_call = mutated_mod.get_global_var('func_8112')
var_13267 = relay.var("var_13267", dtype = "float64", shape = (252,))#candidate|13267|(252,)|var|float64
call_13266 = relay.TupleGetItem(func_8109_call(relay.reshape(var_13267.astype('float64'), [3, 84])), 5)
call_13268 = relay.TupleGetItem(func_8112_call(relay.reshape(var_13267.astype('float64'), [3, 84])), 5)
output = relay.Tuple([call_13262,call_13266,var_13267,])
output2 = relay.Tuple([call_13263,call_13268,var_13267,])
func_13277 = relay.Function([var_13267,], output)
mod['func_13277'] = func_13277
mod = relay.transform.InferType()(mod)
var_13278 = relay.var("var_13278", dtype = "float64", shape = (252,))#candidate|13278|(252,)|var|float64
output = func_13277(var_13278)
func_13279 = relay.Function([var_13278], output)
mutated_mod['func_13279'] = func_13279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6551_call = mod.get_global_var('func_6551')
func_6552_call = mutated_mod.get_global_var('func_6552')
call_13305 = relay.TupleGetItem(func_6551_call(), 1)
call_13306 = relay.TupleGetItem(func_6552_call(), 1)
func_7805_call = mod.get_global_var('func_7805')
func_7806_call = mutated_mod.get_global_var('func_7806')
call_13363 = relay.TupleGetItem(func_7805_call(), 0)
call_13364 = relay.TupleGetItem(func_7806_call(), 0)
func_6154_call = mod.get_global_var('func_6154')
func_6156_call = mutated_mod.get_global_var('func_6156')
call_13366 = relay.TupleGetItem(func_6154_call(), 0)
call_13367 = relay.TupleGetItem(func_6156_call(), 0)
func_7912_call = mod.get_global_var('func_7912')
func_7914_call = mutated_mod.get_global_var('func_7914')
call_13386 = relay.TupleGetItem(func_7912_call(relay.reshape(call_13366.astype('uint8'), [6, 12, 2])), 1)
call_13387 = relay.TupleGetItem(func_7914_call(relay.reshape(call_13366.astype('uint8'), [6, 12, 2])), 1)
func_13167_call = mod.get_global_var('func_13167')
func_13168_call = mutated_mod.get_global_var('func_13168')
call_13388 = func_13167_call()
call_13389 = func_13167_call()
output = relay.Tuple([call_13305,call_13363,call_13366,call_13386,call_13388,])
output2 = relay.Tuple([call_13306,call_13364,call_13367,call_13387,call_13389,])
func_13394 = relay.Function([], output)
mod['func_13394'] = func_13394
mod = relay.transform.InferType()(mod)
mutated_mod['func_13394'] = func_13394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13394_call = mutated_mod.get_global_var('func_13394')
call_13395 = func_13394_call()
output = call_13395
func_13396 = relay.Function([], output)
mutated_mod['func_13396'] = func_13396
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13424 = relay.var("var_13424", dtype = "float64", shape = (7, 4, 5))#candidate|13424|(7, 4, 5)|var|float64
uop_13425 = relay.erf(var_13424.astype('float64')) # shape=(7, 4, 5)
func_12193_call = mod.get_global_var('func_12193')
func_12195_call = mutated_mod.get_global_var('func_12195')
call_13430 = func_12193_call()
call_13431 = func_12193_call()
output = relay.Tuple([uop_13425,call_13430,])
output2 = relay.Tuple([uop_13425,call_13431,])
func_13445 = relay.Function([var_13424,], output)
mod['func_13445'] = func_13445
mod = relay.transform.InferType()(mod)
var_13446 = relay.var("var_13446", dtype = "float64", shape = (7, 4, 5))#candidate|13446|(7, 4, 5)|var|float64
output = func_13445(var_13446)
func_13447 = relay.Function([var_13446], output)
mutated_mod['func_13447'] = func_13447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10209_call = mod.get_global_var('func_10209')
func_10210_call = mutated_mod.get_global_var('func_10210')
call_13461 = relay.TupleGetItem(func_10209_call(), 0)
call_13462 = relay.TupleGetItem(func_10210_call(), 0)
func_206_call = mod.get_global_var('func_206')
func_210_call = mutated_mod.get_global_var('func_210')
var_13464 = relay.var("var_13464", dtype = "uint8", shape = (378,))#candidate|13464|(378,)|var|uint8
var_13465 = relay.var("var_13465", dtype = "int32", shape = (60,))#candidate|13465|(60,)|var|int32
call_13463 = relay.TupleGetItem(func_206_call(relay.reshape(var_13464.astype('uint8'), [3, 9, 14]), relay.reshape(var_13465.astype('int32'), [3, 2, 10]), ), 0)
call_13466 = relay.TupleGetItem(func_210_call(relay.reshape(var_13464.astype('uint8'), [3, 9, 14]), relay.reshape(var_13465.astype('int32'), [3, 2, 10]), ), 0)
func_8338_call = mod.get_global_var('func_8338')
func_8340_call = mutated_mod.get_global_var('func_8340')
call_13470 = relay.TupleGetItem(func_8338_call(), 0)
call_13471 = relay.TupleGetItem(func_8340_call(), 0)
func_9335_call = mod.get_global_var('func_9335')
func_9336_call = mutated_mod.get_global_var('func_9336')
call_13497 = func_9335_call()
call_13498 = func_9335_call()
func_6154_call = mod.get_global_var('func_6154')
func_6156_call = mutated_mod.get_global_var('func_6156')
call_13499 = relay.TupleGetItem(func_6154_call(), 0)
call_13500 = relay.TupleGetItem(func_6156_call(), 0)
output = relay.Tuple([call_13461,call_13463,var_13464,var_13465,call_13470,call_13497,call_13499,])
output2 = relay.Tuple([call_13462,call_13466,var_13464,var_13465,call_13471,call_13498,call_13500,])
func_13505 = relay.Function([var_13464,var_13465,], output)
mod['func_13505'] = func_13505
mod = relay.transform.InferType()(mod)
var_13506 = relay.var("var_13506", dtype = "uint8", shape = (378,))#candidate|13506|(378,)|var|uint8
var_13507 = relay.var("var_13507", dtype = "int32", shape = (60,))#candidate|13507|(60,)|var|int32
output = func_13505(var_13506,var_13507,)
func_13508 = relay.Function([var_13506,var_13507,], output)
mutated_mod['func_13508'] = func_13508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5512_call = mod.get_global_var('func_5512')
func_5513_call = mutated_mod.get_global_var('func_5513')
call_13550 = func_5512_call()
call_13551 = func_5512_call()
output = call_13550
output2 = call_13551
func_13572 = relay.Function([], output)
mod['func_13572'] = func_13572
mod = relay.transform.InferType()(mod)
mutated_mod['func_13572'] = func_13572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13572_call = mutated_mod.get_global_var('func_13572')
call_13573 = func_13572_call()
output = call_13573
func_13574 = relay.Function([], output)
mutated_mod['func_13574'] = func_13574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12224_call = mod.get_global_var('func_12224')
func_12225_call = mutated_mod.get_global_var('func_12225')
call_13594 = relay.TupleGetItem(func_12224_call(), 0)
call_13595 = relay.TupleGetItem(func_12225_call(), 0)
func_7805_call = mod.get_global_var('func_7805')
func_7806_call = mutated_mod.get_global_var('func_7806')
call_13602 = relay.TupleGetItem(func_7805_call(), 0)
call_13603 = relay.TupleGetItem(func_7806_call(), 0)
func_13017_call = mod.get_global_var('func_13017')
func_13019_call = mutated_mod.get_global_var('func_13019')
call_13609 = relay.TupleGetItem(func_13017_call(), 2)
call_13610 = relay.TupleGetItem(func_13019_call(), 2)
func_10807_call = mod.get_global_var('func_10807')
func_10809_call = mutated_mod.get_global_var('func_10809')
call_13619 = relay.TupleGetItem(func_10807_call(), 1)
call_13620 = relay.TupleGetItem(func_10809_call(), 1)
func_13445_call = mod.get_global_var('func_13445')
func_13447_call = mutated_mod.get_global_var('func_13447')
var_13630 = relay.var("var_13630", dtype = "float64", shape = (140,))#candidate|13630|(140,)|var|float64
call_13629 = relay.TupleGetItem(func_13445_call(relay.reshape(var_13630.astype('float64'), [7, 4, 5])), 0)
call_13631 = relay.TupleGetItem(func_13447_call(relay.reshape(var_13630.astype('float64'), [7, 4, 5])), 0)
output = relay.Tuple([call_13594,call_13602,call_13609,call_13619,call_13629,var_13630,])
output2 = relay.Tuple([call_13595,call_13603,call_13610,call_13620,call_13631,var_13630,])
func_13671 = relay.Function([var_13630,], output)
mod['func_13671'] = func_13671
mod = relay.transform.InferType()(mod)
var_13672 = relay.var("var_13672", dtype = "float64", shape = (140,))#candidate|13672|(140,)|var|float64
output = func_13671(var_13672)
func_13673 = relay.Function([var_13672], output)
mutated_mod['func_13673'] = func_13673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8677_call = mod.get_global_var('func_8677')
func_8679_call = mutated_mod.get_global_var('func_8679')
call_13689 = relay.TupleGetItem(func_8677_call(), 0)
call_13690 = relay.TupleGetItem(func_8679_call(), 0)
output = relay.Tuple([call_13689,])
output2 = relay.Tuple([call_13690,])
func_13701 = relay.Function([], output)
mod['func_13701'] = func_13701
mod = relay.transform.InferType()(mod)
mutated_mod['func_13701'] = func_13701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13701_call = mutated_mod.get_global_var('func_13701')
call_13702 = func_13701_call()
output = call_13702
func_13703 = relay.Function([], output)
mutated_mod['func_13703'] = func_13703
mutated_mod = relay.transform.InferType()(mutated_mod)
const_13714 = relay.const([[[6,1,-6,5,7,-2,-3],[-5,-9,3,-3,10,-7,-5],[3,-6,-3,-2,-7,-9,-7],[1,9,8,8,7,-8,1],[6,-10,-2,-9,-5,-4,-9],[9,7,5,7,-4,-9,-8],[8,2,-7,-4,-1,6,3],[10,-6,-8,-10,-6,10,-2],[1,-4,3,-4,8,-1,-10],[-7,-8,6,8,4,-1,-3],[-2,-8,6,1,-7,10,-4],[6,-10,8,-2,4,2,-7],[10,-2,6,-5,-3,4,3],[7,8,1,8,8,6,3],[-9,1,-2,-4,-4,-3,-7]],[[-8,4,6,-1,-10,8,3],[9,2,-6,-1,-7,-7,4],[-7,-10,1,-10,-5,-6,10],[-2,-8,8,-1,2,-1,7],[-9,9,-3,-10,-2,-1,-3],[-2,1,-5,7,8,8,-1],[10,-8,-10,6,7,-6,-8],[7,-6,-4,3,5,-5,-7],[6,3,-6,4,9,9,-7],[6,-4,7,-2,-8,-4,-2],[-7,-3,6,8,6,-8,-3],[2,2,5,3,-7,-7,-7],[-9,2,-7,-8,3,-7,-9],[6,1,-1,-8,-10,-2,-5],[3,2,10,-7,-10,-1,2]],[[-4,2,4,9,-6,-4,9],[7,-5,-3,-2,10,1,-8],[-5,-2,-3,8,-8,3,-6],[-2,4,-9,10,5,-7,5],[7,2,-4,-8,9,-2,-4],[2,-3,5,6,6,7,1],[-8,-2,8,6,10,-8,-3],[5,7,-7,4,8,7,-5],[9,8,2,4,-6,1,8],[5,10,-7,9,-7,-8,-10],[-3,9,3,-9,7,-5,6],[9,5,-5,5,-4,-8,5],[6,-2,2,-10,1,10,-7],[-1,10,8,5,2,5,-4],[5,-10,-7,-1,-6,-6,4]],[[-4,-8,5,6,-3,7,3],[-9,7,-6,-8,-1,-4,2],[5,5,-9,6,-10,7,5],[9,8,-7,-4,3,-8,1],[-3,-3,2,-10,2,5,8],[7,8,5,6,2,-5,-1],[1,-6,-8,-5,-8,3,8],[-3,-2,4,-6,9,-1,3],[-5,-10,10,-1,6,9,10],[7,10,8,10,-5,1,10],[4,-7,-8,5,2,6,-3],[-5,9,-1,-9,2,-1,8],[10,3,3,-2,6,9,-5],[-7,4,-9,3,3,-9,3],[-3,-1,1,6,5,-5,7]],[[-10,-10,1,8,-6,-4,-4],[3,4,-8,-10,10,-3,6],[-3,-3,-7,9,-9,-10,1],[-4,-8,2,-5,-6,9,1],[-8,-1,1,-5,7,6,2],[-10,1,-7,1,8,10,-10],[-9,-3,9,-9,8,-7,-7],[-10,1,3,-2,-1,-8,2],[5,8,-5,3,5,-4,-4],[-5,-6,-2,-4,8,-5,-10],[8,-2,-6,-6,-1,6,-1],[-6,-3,-7,-7,5,6,-7],[2,6,1,-2,-10,7,9],[5,4,-6,4,6,-4,1],[4,-3,-5,-6,-8,-3,-1]],[[10,-4,2,6,-4,1,2],[-9,-5,2,9,6,-4,-8],[-5,-7,-10,9,6,-10,-8],[8,-6,4,2,-1,3,-8],[6,-4,-4,-5,10,6,1],[-8,-7,-2,7,-6,4,-10],[7,-4,2,3,8,10,-1],[-8,2,-5,4,4,5,-8],[9,6,6,8,-9,-5,8],[7,-4,6,-2,-7,-8,8],[2,2,6,7,9,1,8],[-5,5,-6,8,7,2,-6],[6,6,10,1,-6,-7,6],[3,5,-10,9,-1,9,6],[-3,-2,6,9,5,-1,10]],[[8,-9,-2,8,-5,10,-5],[-4,-10,5,8,-9,-7,-10],[-7,-10,8,7,-2,-4,1],[4,4,-9,9,-6,5,-5],[-2,-3,-5,6,-10,5,-8],[-10,-2,-7,6,-1,-1,-1],[2,9,3,3,-2,-3,-3],[-6,-7,2,-3,-6,-6,-6],[-3,1,5,9,1,7,-2],[8,9,6,10,-5,-6,4],[9,-9,8,-8,-2,-2,9],[-8,10,-6,-8,2,8,-3],[-10,8,-6,2,9,-7,-6],[-3,8,4,5,-4,-2,-1],[6,7,-2,5,-2,-3,6]],[[-1,9,-7,-7,-5,-3,-7],[9,-5,3,-1,9,-2,5],[-3,5,5,-9,-3,3,9],[8,1,6,-2,-10,-2,1],[9,9,-8,5,8,-6,-10],[-8,-5,7,-4,3,-1,-9],[9,9,7,-1,2,-10,2],[1,5,5,6,7,4,-5],[3,10,-5,4,-4,-1,-1],[-7,7,6,-1,-5,2,8],[1,1,-7,-8,9,-6,-6],[-1,6,-1,8,-6,-8,-6],[2,-6,-7,-9,-9,7,-10],[1,10,3,10,10,1,8],[8,10,10,-4,-5,1,1]],[[-2,-3,-5,6,8,1,-5],[7,-2,9,-4,7,4,-1],[8,5,3,4,8,7,8],[-7,10,8,6,1,-6,9],[2,7,4,-9,-7,-6,-5],[-2,-2,-5,10,4,3,-9],[6,1,8,8,-9,8,10],[-10,10,7,2,6,-7,9],[8,9,5,-1,-7,4,6],[1,-9,-2,-4,1,-2,7],[9,-1,5,10,9,3,-2],[1,9,5,-2,7,7,3],[6,1,7,2,-2,-4,-4],[7,1,4,-10,10,-6,-10],[-4,2,-3,7,5,-4,10]],[[7,4,-1,-4,9,-4,7],[-3,-2,-10,-8,7,4,3],[-6,7,-10,-9,-10,-6,6],[5,9,-8,4,5,-4,-9],[4,-8,6,6,-10,7,-8],[6,-2,-5,8,3,-5,8],[-3,-8,9,-9,-5,3,2],[5,4,5,-2,-8,-8,-6],[9,2,9,7,8,-4,-3],[-10,6,6,-7,-5,-3,-1],[4,-2,1,3,6,7,7],[8,-8,-8,4,-4,5,1],[-4,7,-2,-9,6,3,5],[5,1,4,2,4,6,-6],[-9,8,-1,-9,7,6,-3]],[[5,-10,10,4,3,-7,-1],[-6,3,3,-7,10,7,-8],[-3,1,9,-8,5,4,-5],[4,4,-2,5,10,-10,-2],[10,-10,-2,-10,-2,-9,-8],[6,6,1,10,-6,-9,-9],[-7,-3,-10,1,-4,3,9],[7,-7,-3,3,-10,7,7],[2,-4,6,9,2,6,-1],[4,-10,-9,3,9,-6,-8],[7,-9,-1,10,-2,-3,-1],[10,7,3,-6,4,4,5],[4,-3,1,2,6,-1,-2],[-3,-3,-6,1,-8,2,8],[9,6,-9,6,4,3,-1]],[[10,-9,6,-8,-2,2,7],[6,-1,-1,8,-7,-9,2],[1,-6,-7,-6,7,-7,-4],[-1,-4,8,-9,2,8,-2],[2,-1,-7,6,4,-9,7],[-1,7,-3,8,6,-8,-7],[-10,5,6,5,-5,-7,4],[-1,2,-1,4,9,5,1],[6,2,-10,-9,5,10,-6],[10,-5,-10,-10,7,7,8],[-3,-3,-9,-8,4,-5,-3],[8,4,-1,8,7,4,-4],[1,-1,10,-5,1,-10,-9],[3,-2,3,-8,6,-6,3],[-8,-1,10,-3,-7,1,-10]],[[-4,-6,2,7,-3,-8,2],[3,-5,4,-9,-9,-5,9],[-4,-7,-7,-5,-10,-4,9],[5,7,-7,-8,-10,5,7],[4,4,-4,-8,5,-2,6],[-9,10,-4,-1,-1,4,-3],[-9,-7,-8,-2,-3,7,-4],[2,-5,-4,-6,-1,-1,-5],[4,-4,-10,-7,-3,5,1],[-5,-1,6,-1,-10,-9,3],[5,-5,-7,3,1,8,-1],[1,2,-1,-6,-8,5,3],[1,6,-5,7,1,9,-10],[-5,9,6,-3,-6,-4,-5],[4,-5,-5,3,1,1,-9]],[[-3,7,-3,5,10,6,6],[-8,-9,10,-9,2,-6,-1],[-6,-7,-1,-6,-1,-2,8],[4,-8,-6,7,8,2,8],[-4,4,9,-8,6,-3,-4],[5,-2,5,-3,6,6,6],[7,-5,-2,2,10,10,-3],[-2,-7,-10,-6,-1,-7,-1],[-5,4,-2,5,-10,5,-7],[6,7,1,-5,-7,8,-1],[8,-2,2,7,5,-8,-8],[-2,10,-5,8,-3,6,3],[9,-1,-8,10,-6,-6,8],[3,8,9,7,-5,1,-5],[9,1,4,4,4,3,-10]]], dtype = "int8")#candidate|13714|(14, 15, 7)|const|int8
const_13715 = relay.const([[[-7,-5,10,-2,-10,2,-8],[10,-10,-7,1,2,-4,6],[6,-7,7,-7,-6,7,7],[-1,-2,-3,8,-9,-2,3],[-6,3,4,-6,4,1,-2],[9,10,8,-9,-4,3,-7],[4,10,10,-1,3,-9,-1],[-8,-1,-4,-7,10,-3,4],[-8,8,-3,-2,-4,-1,-2],[-4,3,6,9,4,2,1],[-8,1,7,8,2,5,6],[-2,6,-1,-10,-4,9,-6],[-2,8,3,6,3,-10,-7],[-8,10,-1,-6,5,1,4],[7,-3,-6,-9,-4,-8,10]],[[-1,-2,-7,-9,-9,1,2],[3,-4,-7,-9,9,3,-2],[10,1,-8,10,-5,4,-7],[-8,-8,6,-3,-8,7,8],[-3,-3,2,-4,-4,6,7],[-3,-6,3,2,-6,2,5],[3,9,6,1,-5,8,3],[-9,5,-5,3,-7,-7,7],[-8,1,8,1,4,-3,9],[8,-5,-4,-1,3,7,6],[-2,-7,9,-4,-10,2,7],[4,-7,9,1,4,2,-3],[-5,5,4,-10,8,10,10],[-3,-7,4,9,-8,7,-10],[7,-6,-2,4,10,9,-9]],[[-9,2,6,9,5,-1,8],[-3,7,-4,6,3,-4,-3],[5,5,-9,-6,-8,4,4],[-6,-3,3,-1,-2,-4,7],[2,-2,-2,-10,4,7,-10],[-5,6,9,10,-1,10,8],[-2,2,4,10,-1,-10,-6],[-6,10,3,3,-7,-5,-4],[4,8,6,10,4,-10,10],[-1,-9,-5,10,-4,1,8],[10,10,3,-9,-8,2,7],[-6,-2,-3,3,9,-5,8],[2,3,-7,5,-1,-2,-3],[10,8,9,2,-2,-10,-8],[-2,5,2,8,-1,1,9]],[[-2,10,2,-7,-8,3,-3],[1,-9,8,8,2,-1,-1],[6,8,2,-9,5,-7,4],[-3,4,8,6,7,-8,-2],[-3,-5,-4,-6,-2,3,4],[10,-2,5,-6,9,-3,-8],[7,-1,-2,9,1,4,-2],[-1,-9,-6,-8,6,6,-8],[4,-9,5,-9,-8,4,-4],[3,7,4,-8,6,-1,-10],[8,7,5,2,8,8,10],[5,2,3,3,5,10,-7],[-2,10,-6,-1,-1,-2,4],[4,4,1,-9,-7,-4,4],[-2,4,2,5,9,1,-8]],[[-10,3,-10,5,-4,6,5],[-4,3,-3,-9,9,3,9],[-1,-8,-1,6,9,1,-4],[-7,-8,-1,6,-5,9,8],[-5,7,-3,-6,-6,-4,-2],[10,-3,-6,-7,-1,10,-7],[-4,-2,-9,-5,-2,7,-1],[-2,-7,8,9,-2,-2,-7],[-10,3,9,-3,4,3,8],[5,10,-2,-10,-6,6,-3],[-10,5,7,6,-5,4,-8],[7,-4,5,10,10,8,6],[5,-6,-2,-7,-1,4,-5],[-7,-5,8,7,-5,1,-6],[3,-4,-1,-3,3,3,6]],[[-2,-6,-3,5,10,5,10],[3,6,8,-4,2,4,-1],[1,-4,8,4,-1,-3,3],[-8,-5,-1,-9,-10,-7,-4],[10,-8,3,-4,2,-10,-8],[-3,10,-8,-4,-5,5,6],[10,3,-5,10,2,9,-3],[4,2,6,3,-9,2,-10],[1,-9,7,-10,-2,2,-6],[8,10,1,-3,7,1,-3],[-2,-10,-2,-4,2,3,6],[-7,-6,10,-9,1,-1,8],[-4,5,-5,-7,-5,-7,-8],[-10,-8,5,-4,-4,-9,6],[1,2,-6,-1,5,1,-10]],[[-6,1,-3,6,4,4,-4],[-3,4,8,-9,-6,-9,-8],[-10,9,9,3,8,1,-9],[2,-9,-8,8,1,-10,8],[8,10,-6,-6,-8,8,-10],[9,-3,7,-3,9,10,-9],[-6,10,4,-4,8,9,10],[-3,6,4,-5,5,5,-1],[3,5,-8,-3,-6,5,8],[-1,1,1,-8,-9,3,2],[6,-2,3,8,2,-4,-10],[-2,2,7,7,-1,2,-9],[3,-2,5,10,1,9,-9],[2,3,8,-7,-1,2,1],[-3,8,2,-7,-5,-2,4]],[[10,6,5,-5,-5,7,-7],[7,10,8,5,9,6,-6],[-10,2,6,-1,-5,3,9],[5,6,5,3,-5,3,8],[-5,8,9,-5,-7,-3,7],[6,5,-3,5,-10,-1,-5],[-8,-4,1,8,3,2,-4],[-6,-2,-8,-4,-1,-10,5],[5,-6,5,6,3,6,1],[-9,5,-7,-6,8,-7,6],[8,-7,-3,6,4,-4,7],[-4,-9,3,-8,3,-5,-3],[7,-8,-3,2,1,-4,9],[3,-1,4,9,4,-8,-1],[-7,5,-4,-3,-1,4,2]],[[-6,-7,6,-5,-8,8,2],[-10,-8,7,-4,-8,9,3],[-1,1,-5,6,8,4,6],[9,-7,-10,7,10,-10,10],[8,-3,8,8,-6,-9,-4],[2,4,-7,-4,5,4,-5],[-4,6,-10,-2,-4,-4,-3],[-7,-5,-6,-2,-9,1,8],[-1,-2,9,6,-6,10,9],[10,-6,-8,8,9,10,-6],[3,-6,10,9,7,-9,-6],[-3,-2,6,2,8,-9,-1],[4,-9,3,1,-5,-3,6],[5,2,6,3,-1,-5,6],[-7,-2,-4,9,-8,3,1]],[[-8,-1,-10,3,6,-7,2],[7,5,-6,-6,-1,10,-5],[3,-2,-4,3,3,-1,1],[-7,9,2,-7,-2,9,-7],[-3,3,-8,-8,-7,8,7],[10,-5,-1,-10,-10,-1,9],[6,-10,-6,-6,7,9,-4],[-5,-6,9,9,-8,4,5],[10,7,10,6,10,2,-7],[3,-8,4,-1,-7,-2,-1],[-3,-4,-10,1,-6,-6,3],[6,-9,-3,5,-2,10,-7],[6,-1,-4,-4,-3,6,5],[8,10,-10,-2,7,-2,-4],[-10,-5,8,-7,-10,-1,-9]],[[-4,9,-4,7,9,9,-7],[-6,-3,1,-3,5,-5,3],[8,1,6,-8,-10,-6,-4],[-6,8,-1,8,-9,3,3],[9,-4,-9,2,6,8,5],[-6,1,-10,-3,9,5,6],[-4,-7,-6,3,-7,-1,-5],[10,4,-8,7,-3,-3,4],[2,7,9,-10,-7,10,-8],[-9,-1,2,7,2,10,-4],[10,10,-6,-10,2,-9,3],[-5,2,1,-4,-1,-2,5],[-10,6,5,-2,4,-7,1],[5,5,4,-3,1,7,8],[-6,-3,2,-6,5,1,9]],[[-6,-1,-6,-3,4,-5,-5],[6,4,-8,8,-6,8,-2],[1,-4,4,1,4,10,10],[-2,8,10,-9,10,-10,-10],[8,-7,3,-9,1,-7,-2],[10,2,8,-9,3,9,-5],[-10,9,-9,8,-10,-1,6],[5,-4,-1,6,-6,10,-2],[3,-9,-4,-10,7,-7,6],[7,5,-10,-6,7,10,6],[5,8,5,2,8,-4,-1],[-1,8,-8,1,-4,-9,-8],[6,-7,-9,-10,6,6,3],[8,-1,-2,-8,-2,8,-5],[-8,-4,-6,5,9,2,7]],[[-9,7,4,-8,-7,-7,-7],[-6,2,5,6,8,-7,-9],[10,6,-6,-7,-3,9,3],[-8,10,1,5,9,-7,5],[2,4,9,3,5,6,-7],[7,-10,8,-8,-4,-7,8],[-8,10,6,3,-6,-1,-8],[-10,-1,-5,-3,-2,2,-5],[7,-4,6,-6,-10,2,-7],[6,1,2,-2,-4,8,5],[2,-2,5,3,-2,6,9],[-9,-2,-4,10,4,3,-8],[-5,-2,4,3,1,-3,-6],[6,-8,4,9,-10,3,10],[3,6,10,-5,3,-6,-6]],[[7,7,-7,-8,4,8,4],[-9,9,4,-1,7,-1,-4],[7,5,1,-7,8,1,3],[-7,3,3,9,9,-2,-8],[9,9,3,9,-7,-4,4],[-8,-7,3,-10,-3,-4,10],[1,8,-1,5,10,-2,2],[3,-3,4,5,-9,-6,3],[-7,7,-5,9,3,-2,1],[1,1,-1,4,-4,3,-3],[10,-8,-2,-6,-1,3,-2],[-10,-8,-6,6,5,1,10],[-7,-10,10,3,-6,-7,7],[-2,2,9,2,2,1,9],[-9,5,-1,-2,-4,10,-7]]], dtype = "int8")#candidate|13715|(14, 15, 7)|const|int8
bop_13716 = relay.minimum(const_13714.astype('int8'), relay.reshape(const_13715.astype('int8'), relay.shape_of(const_13714))) # shape=(14, 15, 7)
uop_13736 = relay.exp(const_13714.astype('float32')) # shape=(14, 15, 7)
func_10641_call = mod.get_global_var('func_10641')
func_10642_call = mutated_mod.get_global_var('func_10642')
call_13740 = relay.TupleGetItem(func_10641_call(), 4)
call_13741 = relay.TupleGetItem(func_10642_call(), 4)
func_11271_call = mod.get_global_var('func_11271')
func_11273_call = mutated_mod.get_global_var('func_11273')
call_13746 = relay.TupleGetItem(func_11271_call(), 4)
call_13747 = relay.TupleGetItem(func_11273_call(), 4)
output = relay.Tuple([bop_13716,uop_13736,call_13740,call_13746,])
output2 = relay.Tuple([bop_13716,uop_13736,call_13741,call_13747,])
func_13752 = relay.Function([], output)
mod['func_13752'] = func_13752
mod = relay.transform.InferType()(mod)
mutated_mod['func_13752'] = func_13752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13752_call = mutated_mod.get_global_var('func_13752')
call_13753 = func_13752_call()
output = call_13753
func_13754 = relay.Function([], output)
mutated_mod['func_13754'] = func_13754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8677_call = mod.get_global_var('func_8677')
func_8679_call = mutated_mod.get_global_var('func_8679')
call_13760 = relay.TupleGetItem(func_8677_call(), 0)
call_13761 = relay.TupleGetItem(func_8679_call(), 0)
func_9906_call = mod.get_global_var('func_9906')
func_9908_call = mutated_mod.get_global_var('func_9908')
var_13788 = relay.var("var_13788", dtype = "float64", shape = (192,))#candidate|13788|(192,)|var|float64
call_13787 = relay.TupleGetItem(func_9906_call(relay.reshape(var_13788.astype('float64'), [192,])), 3)
call_13789 = relay.TupleGetItem(func_9908_call(relay.reshape(var_13788.astype('float64'), [192,])), 3)
output = relay.Tuple([call_13760,call_13787,var_13788,])
output2 = relay.Tuple([call_13761,call_13789,var_13788,])
func_13827 = relay.Function([var_13788,], output)
mod['func_13827'] = func_13827
mod = relay.transform.InferType()(mod)
var_13828 = relay.var("var_13828", dtype = "float64", shape = (192,))#candidate|13828|(192,)|var|float64
output = func_13827(var_13828)
func_13829 = relay.Function([var_13828], output)
mutated_mod['func_13829'] = func_13829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7952_call = mod.get_global_var('func_7952')
func_7953_call = mutated_mod.get_global_var('func_7953')
call_13902 = func_7952_call()
call_13903 = func_7952_call()
output = relay.Tuple([call_13902,])
output2 = relay.Tuple([call_13903,])
func_13916 = relay.Function([], output)
mod['func_13916'] = func_13916
mod = relay.transform.InferType()(mod)
output = func_13916()
func_13917 = relay.Function([], output)
mutated_mod['func_13917'] = func_13917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7406_call = mod.get_global_var('func_7406')
func_7407_call = mutated_mod.get_global_var('func_7407')
call_13986 = func_7406_call()
call_13987 = func_7406_call()
func_5899_call = mod.get_global_var('func_5899')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_14008 = relay.TupleGetItem(func_5899_call(), 0)
call_14009 = relay.TupleGetItem(func_5901_call(), 0)
output = relay.Tuple([call_13986,call_14008,])
output2 = relay.Tuple([call_13987,call_14009,])
func_14013 = relay.Function([], output)
mod['func_14013'] = func_14013
mod = relay.transform.InferType()(mod)
output = func_14013()
func_14014 = relay.Function([], output)
mutated_mod['func_14014'] = func_14014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8338_call = mod.get_global_var('func_8338')
func_8340_call = mutated_mod.get_global_var('func_8340')
call_14015 = relay.TupleGetItem(func_8338_call(), 0)
call_14016 = relay.TupleGetItem(func_8340_call(), 0)
var_14018 = relay.var("var_14018", dtype = "int32", shape = (6, 12, 2))#candidate|14018|(6, 12, 2)|var|int32
bop_14019 = relay.maximum(call_14015.astype('uint32'), relay.reshape(var_14018.astype('uint32'), relay.shape_of(call_14015))) # shape=(6, 12, 2)
bop_14022 = relay.maximum(call_14016.astype('uint32'), relay.reshape(var_14018.astype('uint32'), relay.shape_of(call_14016))) # shape=(6, 12, 2)
output = relay.Tuple([bop_14019,])
output2 = relay.Tuple([bop_14022,])
func_14039 = relay.Function([var_14018,], output)
mod['func_14039'] = func_14039
mod = relay.transform.InferType()(mod)
mutated_mod['func_14039'] = func_14039
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14040 = relay.var("var_14040", dtype = "int32", shape = (6, 12, 2))#candidate|14040|(6, 12, 2)|var|int32
func_14039_call = mutated_mod.get_global_var('func_14039')
call_14041 = func_14039_call(var_14040)
output = call_14041
func_14042 = relay.Function([var_14040], output)
mutated_mod['func_14042'] = func_14042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10947_call = mod.get_global_var('func_10947')
func_10948_call = mutated_mod.get_global_var('func_10948')
call_14052 = relay.TupleGetItem(func_10947_call(), 1)
call_14053 = relay.TupleGetItem(func_10948_call(), 1)
output = relay.Tuple([call_14052,])
output2 = relay.Tuple([call_14053,])
func_14056 = relay.Function([], output)
mod['func_14056'] = func_14056
mod = relay.transform.InferType()(mod)
output = func_14056()
func_14057 = relay.Function([], output)
mutated_mod['func_14057'] = func_14057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12411_call = mod.get_global_var('func_12411')
func_12413_call = mutated_mod.get_global_var('func_12413')
call_14061 = relay.TupleGetItem(func_12411_call(), 1)
call_14062 = relay.TupleGetItem(func_12413_call(), 1)
output = call_14061
output2 = call_14062
func_14078 = relay.Function([], output)
mod['func_14078'] = func_14078
mod = relay.transform.InferType()(mod)
mutated_mod['func_14078'] = func_14078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14078_call = mutated_mod.get_global_var('func_14078')
call_14079 = func_14078_call()
output = call_14079
func_14080 = relay.Function([], output)
mutated_mod['func_14080'] = func_14080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11271_call = mod.get_global_var('func_11271')
func_11273_call = mutated_mod.get_global_var('func_11273')
call_14088 = relay.TupleGetItem(func_11271_call(), 5)
call_14089 = relay.TupleGetItem(func_11273_call(), 5)
func_12812_call = mod.get_global_var('func_12812')
func_12814_call = mutated_mod.get_global_var('func_12814')
call_14096 = func_12812_call()
call_14097 = func_12812_call()
func_9298_call = mod.get_global_var('func_9298')
func_9299_call = mutated_mod.get_global_var('func_9299')
call_14100 = relay.TupleGetItem(func_9298_call(), 1)
call_14101 = relay.TupleGetItem(func_9299_call(), 1)
func_13445_call = mod.get_global_var('func_13445')
func_13447_call = mutated_mod.get_global_var('func_13447')
const_14106 = relay.const([-7.716593,-4.570171,1.204992,5.748900,5.385915,-6.347039,-9.878738,1.465633,-3.124176,-4.133094,-2.192994,-4.801773,7.817285,-1.027031,8.943499,-4.793057,-1.869375,3.711189,-5.322759,-6.099306,2.637674,5.167478,-2.342143,0.008759,5.845707,-5.149197,0.564338,-2.303676,-2.446357,7.523404,-4.549928,0.232439,5.773641,4.339230,7.049822,1.375531,-4.387664,5.612128,-3.687257,-7.891044,-5.773894,2.132465,5.669323,1.991433,-6.807612,9.311179,-7.863110,-0.165728,5.686666,9.977594,3.704497,7.036530,8.738284,-7.276769,2.371358,-0.074130,-7.333039,-3.996357,0.354294,4.342546,-6.418754,-0.039310,3.854382,-1.388743,-3.251359,5.667285,2.634130,-6.458633,4.110394,-6.498225,8.342076,2.266278,-1.544042,5.858046,6.955229,0.667132,4.680092,-8.381202,-2.874659,1.440968,9.015623,-4.682610,2.307233,9.114304,-3.952462,0.130746,-3.459052,1.190889,-1.124191,-6.914895,9.874911,-8.298920,-1.859751,6.327370,4.993835,8.841644,1.829066,7.570727,-7.628861,-5.343295,-8.444873,-5.407637,-8.365352,5.588014,-5.795172,-6.776241,-1.271045,-0.657219,0.599473,7.454317,-4.805304,7.860418,6.455002,-2.325879,-2.201111,-7.726825,6.941913,3.564702,-7.586666,-5.125364,6.840289,-7.887274,7.901134,-7.783454,-2.467828,-7.978325,-1.704662,-6.209041,-7.798579,-0.853130,8.293516,-9.613722,7.341261,-5.024605,-0.009358,0.242947,0.815836,7.740099,-5.876232,-0.083785], dtype = "float64")#candidate|14106|(140,)|const|float64
call_14105 = relay.TupleGetItem(func_13445_call(relay.reshape(const_14106.astype('float64'), [7, 4, 5])), 1)
call_14107 = relay.TupleGetItem(func_13447_call(relay.reshape(const_14106.astype('float64'), [7, 4, 5])), 1)
func_13394_call = mod.get_global_var('func_13394')
func_13396_call = mutated_mod.get_global_var('func_13396')
call_14118 = relay.TupleGetItem(func_13394_call(), 4)
call_14119 = relay.TupleGetItem(func_13396_call(), 4)
func_11847_call = mod.get_global_var('func_11847')
func_11850_call = mutated_mod.get_global_var('func_11850')
const_14122 = relay.const([[6,-4],[4,8],[-8,-7],[5,3],[1,1],[-2,-8],[9,10],[-7,1],[8,10],[5,-1],[4,-1],[1,6],[-10,2],[5,5],[-7,5],[-1,-7],[10,-2],[-3,7],[1,8],[-3,-4],[3,-7],[5,2],[6,7],[-2,6],[-2,-8],[-1,4],[-2,-4],[7,10],[-5,8],[-6,1],[6,9],[2,1],[-6,-1],[-1,-9],[-9,9],[-2,-6],[3,-6],[-2,3],[4,-7],[9,-2],[-6,-2],[-10,-1],[-5,-7],[-9,-3],[-6,-3],[5,-10],[8,-5],[5,2],[2,10],[4,-5],[4,-3],[4,5],[-4,-2],[-2,7],[-10,-9],[-2,8],[-4,10],[-4,4],[-4,8],[4,9],[2,6],[-4,6],[-7,-10],[-5,-7],[-9,-6],[9,-8],[10,2],[-3,-3],[-4,9],[-3,-1],[9,3],[10,-10],[4,-1],[-7,-7],[-6,10],[-2,4],[-3,4],[-7,8],[6,7],[-1,4],[-4,-10],[3,5],[-8,1],[-7,8],[8,-8],[8,-9],[7,-10],[-5,-6],[9,-8],[-5,6],[-10,-5],[-1,-9],[-4,-4],[-2,7],[-10,-10],[3,-4],[1,-9],[-8,2],[-9,7],[2,1],[-2,8],[-9,-3],[-4,-6],[8,1],[3,-8],[2,-7],[8,3],[9,-4],[10,-4],[9,-7],[-10,-9],[-2,-8],[10,-4],[-5,-5],[6,-3],[-3,-7],[-10,-1],[-8,-1],[-1,7],[-1,-8],[10,-3],[-4,9],[8,6],[-8,-6],[2,9],[-8,-8],[-3,4],[-9,-4],[4,-3],[-10,10],[-4,-1],[9,-5],[7,-3],[-4,-5],[8,-10],[-2,4],[-6,6],[-1,5],[-3,2],[-6,-5],[8,-9],[10,1],[3,-3],[-8,1],[-5,-9],[3,6],[10,10],[-2,10],[-2,6],[5,8],[-9,-3],[9,2],[-2,4],[6,-3],[-5,-4],[-7,-9],[-5,3],[-2,-8],[-1,9],[-4,5],[1,1],[-9,-4],[9,-3],[4,7],[9,-9],[-10,-2],[-7,-2],[2,-7],[9,10],[6,2],[2,2],[-7,3],[-1,-7],[-9,-2],[9,-9],[5,6],[6,2],[8,7],[-9,-5],[-10,-10],[-3,9],[-5,-10],[9,9],[-5,-10],[9,-3],[5,-6],[-9,-1],[-1,9],[10,-6],[3,3],[-5,-7],[-5,1],[8,2],[6,-8],[-1,5],[1,-4],[3,8],[-7,-7],[-3,-3],[1,4],[-10,1],[-4,-4],[-9,7],[-4,-1],[-4,-3],[9,-3],[6,1],[-10,5],[1,9],[-8,-2],[-1,-6],[-3,-3],[7,-8],[-8,1],[7,-9],[6,8],[-3,-5],[-1,5],[8,-8],[-2,8],[7,-8],[-6,-8],[2,1],[-5,-7],[7,7],[-9,-9],[-6,9],[-8,-9],[-2,-1],[-7,-3],[-8,7],[3,-2],[-6,-8],[1,-5],[6,5],[9,-10],[-1,1],[-2,7],[9,3],[-7,-2],[-4,-1],[10,2],[-8,-10],[2,-9],[-3,-3],[7,4],[3,9],[6,5],[4,5],[-2,9],[-5,-8],[-3,10],[-1,2],[2,-5],[-7,4],[-8,1],[7,-7],[2,-10],[7,4],[8,7],[-8,7],[-4,4],[9,-3],[1,8],[-2,8],[10,-1],[-7,-8],[-2,4],[3,1],[-4,-1],[4,-9],[-9,-2],[1,-5],[7,2],[2,1],[-7,3],[6,1],[6,4],[-5,-5],[-1,5],[5,7],[-5,-8],[-8,-8],[-1,5],[2,9],[8,-10],[-6,7],[-1,1],[4,10],[6,-6],[-6,-7],[5,6],[10,7],[-9,-10],[3,-6],[4,2],[5,5],[1,-6],[-6,-8],[9,-10],[3,8],[6,9],[-7,-4],[2,7],[10,-1],[-5,-2],[3,4],[7,-10],[1,2],[-6,-9],[-6,4],[-10,9],[4,3],[-8,4],[6,-3],[2,-1],[9,-2],[-4,10],[3,10],[-4,3],[9,-1],[10,8],[1,-9],[5,8],[3,1],[-3,9],[-4,9],[-8,-7],[-8,-5],[4,-8],[-5,10],[9,5],[9,1],[-8,10],[-9,-9],[-1,3],[-5,-2],[2,-3],[-5,10],[-2,5],[-3,-5],[-7,3],[4,-3],[6,-6],[6,9],[-6,-6],[7,4],[-3,1],[7,6],[-3,-2],[-9,-1],[2,-8],[-3,-6],[-3,-9],[-10,-10],[-4,-8],[-8,-7],[-3,5],[-3,-9],[-2,-3],[7,-4],[-2,1],[-6,5],[-3,-2],[-9,-2],[-9,4],[-5,-9],[1,-4],[9,-1],[10,5],[2,-5],[4,5],[-6,6],[6,-9],[3,8],[8,-4],[-9,-2],[-6,5]], dtype = "int8")#candidate|14122|(378, 2)|const|int8
var_14123 = relay.var("var_14123", dtype = "float64", shape = (720,))#candidate|14123|(720,)|var|float64
call_14121 = relay.TupleGetItem(func_11847_call(relay.reshape(const_14122.astype('int8'), [756,]), relay.reshape(var_14123.astype('float64'), [720,]), ), 2)
call_14124 = relay.TupleGetItem(func_11850_call(relay.reshape(const_14122.astype('int8'), [756,]), relay.reshape(var_14123.astype('float64'), [720,]), ), 2)
func_7912_call = mod.get_global_var('func_7912')
func_7914_call = mutated_mod.get_global_var('func_7914')
call_14129 = relay.TupleGetItem(func_7912_call(relay.reshape(call_14100.astype('uint8'), [6, 12, 2])), 0)
call_14130 = relay.TupleGetItem(func_7914_call(relay.reshape(call_14100.astype('uint8'), [6, 12, 2])), 0)
func_11742_call = mod.get_global_var('func_11742')
func_11744_call = mutated_mod.get_global_var('func_11744')
call_14133 = relay.TupleGetItem(func_11742_call(), 0)
call_14134 = relay.TupleGetItem(func_11744_call(), 0)
func_10295_call = mod.get_global_var('func_10295')
func_10300_call = mutated_mod.get_global_var('func_10300')
var_14152 = relay.var("var_14152", dtype = "int64", shape = ())#candidate|14152|()|var|int64
const_14153 = relay.const([[-10,6,-7,-6,-4,9,-8,-9,4,-3,-3,3,4,4,1,-6,-8,-8,5,-7,-10,-6,-7,-9,9,10,-1,-10,6,-10,10,2,2,-3,4,6,6,-4,-7,4],[5,9,-8,-2,3,-3,-9,10,-5,-10,3,-6,-8,-4,1,2,-3,-9,-10,-7,-4,7,-7,7,-10,-4,-3,-1,-9,7,-4,-6,-9,-10,-8,1,9,-5,3,-10],[-9,5,5,2,-3,-5,-7,4,8,3,10,7,-2,-6,4,-9,2,-4,1,4,4,-9,-2,7,6,5,-3,-5,-9,-1,9,-6,3,-2,8,8,-5,5,9,-7]], dtype = "int64")#candidate|14153|(3, 40)|const|int64
const_14154 = relay.const([1,9,1,7,10,2,-10,8,9,8,-1,4,10,9,10,-2,-6,-9,8,8,3,-4,5,5,-9,3,5,8,-5,-3,-7,-8,-9,-1,-2,-4,9,9,1,1,-6,2,4,-7,6,-3,-6,-7,7,-1,-9,5,-5,3,8,-10,10,6,-3,-4,2,4,-8,4,-3,8,9,9,10,4,7,2,7,3,10,10,5,-9,-9,2,-7,-3,4,4,5,1,1,1,-1,9,4,-3,-5,1,5,-5,4,1,-9,9,3,8,-3,-2,-5,-8,-10,7,-5,-9,-4,5,4,3,2,-9,-1,-9,-8,-3,-1,2,-3,-7,9,-1,2,-10,-5,-10,-6,2,-8,4,-1,8,7,3,1,8,-8,3,-4,-6,6,6,9,-9,-6,-2,9,8,2,-4,3,-2,-1,-1,-8,6,7,5,-9,-10,7,-3,-3,-2,4,7,8,-8,-6,3,-8,-1,-10,-10,3,5,3,8,-9,-1,4,2,-9,10,1,-3,-2,-3,-1,3,-4,-3,4,-1,10,8,9,-8,10,6,-3,2,1,10,-10,-5,-9,9,10,8,3,-5,-8,1,-5,1,5,-5,-1,-8,10,-3,-2,4,-6,1,2,4,-1,10,-3,5,-4,-4,-5,-6,-8,4,5,9,4,-1,-7,6,9,5,-7,-9,9,6,8,1,-10,3,4,-7,3,3,-4,-8,-3,4,-3,10,8,8,-7,9,1,-5,5,3,3,-8,5,9,-10,9,-7,5,-7,1,-9,5,4,7,3,7,-6,-10,-10,-2,-3,-4,-1,8,-10,-2,-1,9,7,3,5,-8,3,-5,-9,5,-7,-4,8,4,1,6,-5,5,2,5,-8,-10,1,7,-2,1,1,-8,7,6,-10,-2,-7,8,-7,-9,-6,-9,6,-4,-8,10,10,8,-9,-7,-9,5,-6,-7,8,9,5,-10,1,1,-10,-1,-8,10,-5,10,6,10,-10,4,-3,1,-8,-2,4,-10,-6,-5,-10,-4,1,-1,-9,6,7,7,-4,9,9,3,-5,-10,-6,5,-9,2,-3,5,-3,-1,-5,-10,9,1,3,3,-10,8,7,1,2,-6,-6,9,3,2,8,-7,3,7,3,-3,3,9,5,-8,5,6,-4,-3,-4,-7,6,9,1,7,-6,-8,-2,-10,7,7,-1,-3,7,4,-10,-4,-4,-10,-9,-10,7,-5,-7,7,-3,5,-9,-1,-6,-8,7,-7,-4,-7,-3,-7,6,-9,-7,6,5,5,4,10,2,-8,-7,1,3,-4,4,-5,3,3,2,-1,-3,-1,-4,-6,-7,7,-3,-7,6,-1,3,1,1,10,-3,2,-9,2,-4,-2,-5,6,7,4,-5,4,-2,7,-6,9,-8,-7,4,10,2,-10,1,6,-9,3,-5,3,-9,1,7,-9,10,2,7,-3,-4,-7,1,6,2,-6,-4,4,-1,-3,6,-3,-7,-2,9,-5,-10,-9,-6,1,-4,-6,-5,-6,-7,5,8,-10,7,3,-7,10,-1,-6,-5,4,3,-10,10,5,4,1,-1,8,10,3,-2,-7,-1,-9,-2,-6,4,-3,1,-4,-9,-6,3,-8,7,-4,-6,1,4,6,4,-8,9,5,-9,-4,1,9,-5,-10,-2,-3,-3,-6,4,-2,-5,9,2,-1,-2,-1,6,-8,9,-5,-2,9,-3,-4,-8,-7,7,-4,-1,-3,-1,-7,-4,-10,-5,-4,-5,2,-10,7,3,1,-10,-2,-2,-4,-7,10,6,-4,6,7,5,-9,8,-2,-10,2,10,2,6,2,9,-7,-3,7,1,1,5,-10,6,5,-7,-7,-10,-6,5,4,-2,-8,-1,6,-8,7,-7,-6,9,10,-10,-2,5,9,-7,-3,-1,4,5,4,-7,9,-6,-10,8,-2,6,-9,1,1,10,-5,-5,2,10,-7,5,-2,3,-7,-1,-9,2,-8,-7,-8,-2,-7,3,1,5,2,-4,-2,-6,9,-9,-6,8,1,2,-2,4,3,1,3,-2,8,9,4,-3,7,-5,1,7,-1,-3,7,-4,-5,6,1,-4,5,-10,-3,6,-3,10,-4,-7,-8,-8,8,-5,7,4,1,-8,3,7,-1,3,2,9,2,1,-8,7,10,-10,5,-6,2,-1,10,-9,1,-4,-5,8,-10,-9,7,4,-8,-6,-8,7,4,3,8,-6,5,-3,-4,-8,-2,-5,-1,-8,-5,1,-7,-3,8,5,-1,-4,-3,-5,-10,1,9,10,-5,10,3,3,-10,10,-4,4,8,-2,-5,-7,-1,6,4,-2,4,-1,5,-6,-2,-3,-1,-4,4,-9,-10,-3,-5,-2,5,-10,-8,-6,4,-6,-6,5,-5,-6,2,10,-10,-4,4,-3,-10,5,-3,8,3,-4,-4,-6,-7,-8,8,10,2,4,-9,-2,2,-6,-10,-4,10,-2,8,-3,-10,1,-10,-9,-8,6,-2,8,-8,2,-1,-1,-6,-5,-10,-9,-3,10,3,6,4,9,-2,1,3,8,-10,5,3,-10,2,5,10,-7,-7,-4,-4,-7,2,-6,3,-9,6,-1,-5,2,-10,1,6,-7,-2,4,-6,4,-2,2,-8,-8,-4,1,-2,5,2,4,-7,-1,-1,-4,-9,-6,-1,-4,-7,3,-3,-1,9,-7,-5,1,1,8,10,-1,-4,-7,5,-6,-8,-6,-3,-6,-6,-7,3,2,1,-9,3,7,-9,4,8,8,7,6,4,6,4,-10,9,-2,9,-1,-3,2,3,-6,4,-8,10,4,-4,4,2,-7,-4,-3,-10,7,-3,7,-5,-8,9,-1,-9,-4,5,-3,2,8,-8,-10,7,4,-8,-7,-4,-3,2,3,-1,4,-5,-1,-8,-2,3,-7,-9,8,3,-2,10,-1,9,4,3,4,-7,-6,7,1,1,-8,-10,10,4,10,5,-6,7,4,10,-9,-6,-3,-6,3,-4,-10,1,-6,1,-9,-9,-3,-7,-8,7,-5,4,-6,-4,-8,3,-1,-5,9,6,4,-7,4,4,-2,-9,5,-4,-4,1,-7,7,7,8,1,6,-9,-2,6,5,8,4,9,-4,8,-4,-10,-4,6,2,6,-1,-10,8,-3,-3,-8,4,-7,-10,-6,10,5,2,6,9,2,6,4,-8,-10,-8,6,-6,4,9,-10,3,-5,-7,9,-4,7,-4,6,8,3,-4,9,3,4,1,-1,9,1,8,3,4,-1,-1,-10,-3,-4,-1,5,-6,6,-2,6,-4,9,-9,-5,2,-1,1,1,-6,10,-8,3,-3,3,-7,-9,8,-6,-2,-9,-5,7,-6,1,-3,-1,-6,-7,3,-8,-1,-5,7,-5,10,-5,-8,2,-3,8,-6,9,1,-2,-7,7,9,8,-3,7,9,-8,-6,-3,-5,-5,7,-4,-9,5,9,6,3,-4,-7,10,4,-2,-2,1,3,-10,-9,1,3,6,7,7,-5,8,3,7,10,2,-6,1,9,2,-6,-8,6,-8,-5,6,-8,-4,-6,10,4,-8,-5,10,10,1,-2,4,2,-2,9,-9,-4,-9,5,6,3,8,3,-1,-9,-7,-1,8,5,8,-1,4,-1,-6,4,6,6,-5,-3,9,9,10,1,1,1,1,-10,7,-7,8,7,-9,9,1,2,-1,-8,-1,2,-6,-3,6,1,5,-8,-1,6,-7,4,6,-10,7,1,-8,9,-7,-10,-8,-6,-2,3,-1,-3,-5,-8,5,9,7,-9,2,-10,2,9,2,-2,-4,-8,-5,3,8,-2,-1,-4], dtype = "int8")#candidate|14154|(1408,)|const|int8
call_14151 = relay.TupleGetItem(func_10295_call(relay.reshape(var_14152.astype('int64'), []), relay.reshape(const_14153.astype('int64'), [1, 10, 12]), relay.reshape(const_14154.astype('int8'), [1408,]), ), 1)
call_14155 = relay.TupleGetItem(func_10300_call(relay.reshape(var_14152.astype('int64'), []), relay.reshape(const_14153.astype('int64'), [1, 10, 12]), relay.reshape(const_14154.astype('int8'), [1408,]), ), 1)
func_13916_call = mod.get_global_var('func_13916')
func_13917_call = mutated_mod.get_global_var('func_13917')
call_14159 = relay.TupleGetItem(func_13916_call(), 0)
call_14160 = relay.TupleGetItem(func_13917_call(), 0)
func_6303_call = mod.get_global_var('func_6303')
func_6307_call = mutated_mod.get_global_var('func_6307')
var_14174 = relay.var("var_14174", dtype = "int8", shape = (288,))#candidate|14174|(288,)|var|int8
call_14173 = relay.TupleGetItem(func_6303_call(relay.reshape(const_14122.astype('int8'), [756,]), relay.reshape(var_14123.astype('float64'), [720,]), relay.reshape(var_14174.astype('int8'), [24, 12]), ), 11)
call_14175 = relay.TupleGetItem(func_6307_call(relay.reshape(const_14122.astype('int8'), [756,]), relay.reshape(var_14123.astype('float64'), [720,]), relay.reshape(var_14174.astype('int8'), [24, 12]), ), 11)
output = relay.Tuple([call_14088,call_14096,call_14100,call_14105,const_14106,call_14118,call_14121,const_14122,var_14123,call_14129,call_14133,call_14151,var_14152,const_14153,const_14154,call_14159,call_14173,var_14174,])
output2 = relay.Tuple([call_14089,call_14097,call_14101,call_14107,const_14106,call_14119,call_14124,const_14122,var_14123,call_14130,call_14134,call_14155,var_14152,const_14153,const_14154,call_14160,call_14175,var_14174,])
func_14187 = relay.Function([var_14123,var_14152,var_14174,], output)
mod['func_14187'] = func_14187
mod = relay.transform.InferType()(mod)
mutated_mod['func_14187'] = func_14187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14187_call = mutated_mod.get_global_var('func_14187')
var_14189 = relay.var("var_14189", dtype = "float64", shape = (720,))#candidate|14189|(720,)|var|float64
var_14190 = relay.var("var_14190", dtype = "int64", shape = ())#candidate|14190|()|var|int64
var_14191 = relay.var("var_14191", dtype = "int8", shape = (288,))#candidate|14191|(288,)|var|int8
call_14188 = func_14187_call(var_14189,var_14190,var_14191,)
output = call_14188
func_14192 = relay.Function([var_14189,var_14190,var_14191,], output)
mutated_mod['func_14192'] = func_14192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13394_call = mod.get_global_var('func_13394')
func_13396_call = mutated_mod.get_global_var('func_13396')
call_14367 = relay.TupleGetItem(func_13394_call(), 3)
call_14368 = relay.TupleGetItem(func_13396_call(), 3)
func_11681_call = mod.get_global_var('func_11681')
func_11684_call = mutated_mod.get_global_var('func_11684')
var_14376 = relay.var("var_14376", dtype = "int32", shape = (60,))#candidate|14376|(60,)|var|int32
call_14375 = relay.TupleGetItem(func_11681_call(relay.reshape(var_14376.astype('int32'), [30, 2])), 1)
call_14377 = relay.TupleGetItem(func_11684_call(relay.reshape(var_14376.astype('int32'), [30, 2])), 1)
func_10_call = mod.get_global_var('func_10')
func_13_call = mutated_mod.get_global_var('func_13')
call_14387 = func_10_call(relay.reshape(var_14376.astype('int32'), [3, 2, 10]), relay.reshape(var_14376.astype('int32'), [3, 2, 10]), )
call_14388 = func_10_call(relay.reshape(var_14376.astype('int32'), [3, 2, 10]), relay.reshape(var_14376.astype('int32'), [3, 2, 10]), )
output = relay.Tuple([call_14367,call_14375,var_14376,call_14387,])
output2 = relay.Tuple([call_14368,call_14377,var_14376,call_14388,])
func_14417 = relay.Function([var_14376,], output)
mod['func_14417'] = func_14417
mod = relay.transform.InferType()(mod)
var_14418 = relay.var("var_14418", dtype = "int32", shape = (60,))#candidate|14418|(60,)|var|int32
output = func_14417(var_14418)
func_14419 = relay.Function([var_14418], output)
mutated_mod['func_14419'] = func_14419
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14425 = relay.var("var_14425", dtype = "float32", shape = (14, 11, 7))#candidate|14425|(14, 11, 7)|var|float32
uop_14426 = relay.log10(var_14425.astype('float32')) # shape=(14, 11, 7)
func_10732_call = mod.get_global_var('func_10732')
func_10735_call = mutated_mod.get_global_var('func_10735')
var_14435 = relay.var("var_14435", dtype = "uint16", shape = ())#candidate|14435|()|var|uint16
var_14436 = relay.var("var_14436", dtype = "uint16", shape = (56,))#candidate|14436|(56,)|var|uint16
call_14434 = func_10732_call(relay.reshape(var_14435.astype('uint16'), []), relay.reshape(var_14436.astype('uint16'), [8, 7, 1]), )
call_14437 = func_10732_call(relay.reshape(var_14435.astype('uint16'), []), relay.reshape(var_14436.astype('uint16'), [8, 7, 1]), )
output = relay.Tuple([uop_14426,call_14434,var_14435,var_14436,])
output2 = relay.Tuple([uop_14426,call_14437,var_14435,var_14436,])
func_14440 = relay.Function([var_14425,var_14435,var_14436,], output)
mod['func_14440'] = func_14440
mod = relay.transform.InferType()(mod)
mutated_mod['func_14440'] = func_14440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14440_call = mutated_mod.get_global_var('func_14440')
var_14442 = relay.var("var_14442", dtype = "float32", shape = (14, 11, 7))#candidate|14442|(14, 11, 7)|var|float32
var_14443 = relay.var("var_14443", dtype = "uint16", shape = ())#candidate|14443|()|var|uint16
var_14444 = relay.var("var_14444", dtype = "uint16", shape = (56,))#candidate|14444|(56,)|var|uint16
call_14441 = func_14440_call(var_14442,var_14443,var_14444,)
output = call_14441
func_14445 = relay.Function([var_14442,var_14443,var_14444,], output)
mutated_mod['func_14445'] = func_14445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10387_call = mod.get_global_var('func_10387')
func_10388_call = mutated_mod.get_global_var('func_10388')
call_14476 = relay.TupleGetItem(func_10387_call(), 0)
call_14477 = relay.TupleGetItem(func_10388_call(), 0)
func_13505_call = mod.get_global_var('func_13505')
func_13508_call = mutated_mod.get_global_var('func_13508')
var_14497 = relay.var("var_14497", dtype = "uint8", shape = (378,))#candidate|14497|(378,)|var|uint8
const_14498 = relay.const([-8,-3,8,-10,-6,5,10,7,4,3,1,5,3,-7,-8,7,7,-8,4,7,8,7,4,7,5,-9,-9,8,-6,1,9,-7,-9,-9,-6,2,-10,9,-3,1,-6,4,7,-9,7,5,7,-10,1,-1,10,9,2,-4,-4,-5,-7,8,-1,5], dtype = "int32")#candidate|14498|(60,)|const|int32
call_14496 = relay.TupleGetItem(func_13505_call(relay.reshape(var_14497.astype('uint8'), [378,]), relay.reshape(const_14498.astype('int32'), [60,]), ), 2)
call_14499 = relay.TupleGetItem(func_13508_call(relay.reshape(var_14497.astype('uint8'), [378,]), relay.reshape(const_14498.astype('int32'), [60,]), ), 2)
func_5899_call = mod.get_global_var('func_5899')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_14529 = relay.TupleGetItem(func_5899_call(), 0)
call_14530 = relay.TupleGetItem(func_5901_call(), 0)
output = relay.Tuple([call_14476,call_14496,var_14497,const_14498,call_14529,])
output2 = relay.Tuple([call_14477,call_14499,var_14497,const_14498,call_14530,])
func_14533 = relay.Function([var_14497,], output)
mod['func_14533'] = func_14533
mod = relay.transform.InferType()(mod)
var_14534 = relay.var("var_14534", dtype = "uint8", shape = (378,))#candidate|14534|(378,)|var|uint8
output = func_14533(var_14534)
func_14535 = relay.Function([var_14534], output)
mutated_mod['func_14535'] = func_14535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10682_call = mod.get_global_var('func_10682')
func_10683_call = mutated_mod.get_global_var('func_10683')
call_14548 = relay.TupleGetItem(func_10682_call(), 0)
call_14549 = relay.TupleGetItem(func_10683_call(), 0)
func_8109_call = mod.get_global_var('func_8109')
func_8112_call = mutated_mod.get_global_var('func_8112')
const_14566 = relay.const([1.073779,-9.500502,2.757941,1.879370,-4.820614,-2.028438,-0.525555,-3.154819,-7.548743,6.248259,-5.721425,-2.399548,-0.285454,2.518461,-4.122548,1.019487,-9.684139,-8.938026,3.570417,9.086529,7.542182,-3.349098,-6.460718,0.509467,-0.636107,5.607251,8.391056,-6.178809,-6.704774,8.021057,8.862502,-9.524221,-8.838904,3.974805,-0.181799,0.931865,-1.668324,3.097354,6.845110,6.587027,1.652461,-5.594863,6.751561,1.809761,-1.001749,-8.290103,5.572033,1.979446,5.594899,-0.037212,-1.993960,4.734439,3.014615,3.833926,-8.018189,-4.461412,-6.051105,-1.534222,-1.706404,1.440653,0.201074,-2.712150,-6.636286,-1.206470,0.149552,2.090529,2.811189,-1.798658,-9.859903,1.070891,9.051732,-0.204222,-6.134471,7.558453,-2.879095,6.183026,-4.361993,0.212289,9.478560,9.592469,-5.952321,-3.840765,1.165915,-1.624824,4.127842,-7.670782,-8.846295,-4.819171,-2.984808,7.869186,-1.610172,-1.457874,-6.970841,5.008212,6.967915,-8.716041,8.723491,6.139683,-9.649985,-6.347587,1.842830,-4.636936,-7.322093,-1.049529,-7.294872,2.011695,-4.288468,6.232975,5.198814,4.646949,9.896675,-5.990271,-4.458931,-4.339937,-5.262444,-2.065941,7.612286,8.912329,1.046974,-0.344296,6.362982,-0.078336,3.315294,-9.176587,-3.856733,-8.107961,-9.414177,5.654963,-1.652897,7.641367,-7.933442,6.488589,-3.641192,8.434991,-5.176484,1.796729,-1.185588,-4.656284,9.304752,-2.654722,-7.846895,-1.914258,-3.623949,2.432036,7.029589,6.053676,4.789843,9.064566,3.875706,5.303398,1.501163,7.524489,9.104194,2.865961,-3.549853,-2.022753,-2.464594,7.416812,-1.500108,-0.915273,5.462366,-8.063445,-0.137238,-4.347837,-5.610599,4.845983,-7.849162,9.292163,-0.872461,8.424865,6.729652,6.863234,-7.917900,-5.940758,-3.514688,-6.500664,-3.265450,-6.691612,-0.799622,-3.536198,-0.166991,-1.960149,-5.798464,-5.985818,3.918441,6.978023,-6.941191,-3.168561,-6.784252,7.623961,4.406177,-2.673975,-1.899080,-2.710544,-4.890572,-8.795410,1.911133,7.528752,-2.128786,-6.675231,6.519666,-7.886874,0.140647,-7.143059,4.571702,-9.369036,7.879150,-6.356345,6.753661,4.393093,7.927431,-4.210752,-1.007171,-1.434688,-2.881664,-6.788150,2.127624,6.483368,-1.344019,-6.752998,0.233778,-0.784090,8.288143,8.409008,-9.550701,-6.600819,-1.682389,-7.637726,1.805462,7.261943,6.762052,8.916017,3.712168,8.784377,3.943801,4.481613,-8.405132,9.604086,6.560512,-0.229083,7.705147,5.188859,-3.277634,0.844941,5.280163,3.826430,-5.716088,5.961415,0.916278,5.037136,-8.292391,1.897688], dtype = "float64")#candidate|14566|(252,)|const|float64
call_14565 = relay.TupleGetItem(func_8109_call(relay.reshape(const_14566.astype('float64'), [3, 84])), 2)
call_14567 = relay.TupleGetItem(func_8112_call(relay.reshape(const_14566.astype('float64'), [3, 84])), 2)
func_13394_call = mod.get_global_var('func_13394')
func_13396_call = mutated_mod.get_global_var('func_13396')
call_14573 = relay.TupleGetItem(func_13394_call(), 4)
call_14574 = relay.TupleGetItem(func_13396_call(), 4)
output = relay.Tuple([call_14548,call_14565,const_14566,call_14573,])
output2 = relay.Tuple([call_14549,call_14567,const_14566,call_14574,])
func_14583 = relay.Function([], output)
mod['func_14583'] = func_14583
mod = relay.transform.InferType()(mod)
output = func_14583()
func_14584 = relay.Function([], output)
mutated_mod['func_14584'] = func_14584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10539_call = mod.get_global_var('func_10539')
func_10540_call = mutated_mod.get_global_var('func_10540')
call_14674 = relay.TupleGetItem(func_10539_call(), 0)
call_14675 = relay.TupleGetItem(func_10540_call(), 0)
output = call_14674
output2 = call_14675
func_14676 = relay.Function([], output)
mod['func_14676'] = func_14676
mod = relay.transform.InferType()(mod)
output = func_14676()
func_14677 = relay.Function([], output)
mutated_mod['func_14677'] = func_14677
mutated_mod = relay.transform.InferType()(mutated_mod)
const_14711 = relay.const([[[3,-1,-8,-4,-7,-1,-8,-5,1,-6,3,-8,9,-1],[-1,-9,8,-1,-8,5,1,4,-3,8,8,-2,7,1],[10,-1,7,-5,1,3,10,3,-6,-1,-7,-4,2,-8],[-5,-4,-1,6,-4,4,9,-5,7,-8,-6,-3,-7,-7],[-2,5,4,-2,4,-4,1,4,-5,-8,-6,5,-5,-4],[-7,1,-6,9,-6,6,1,10,7,-1,-4,3,5,-3],[-8,5,8,5,2,5,-4,-10,10,-8,-4,7,8,-10],[-2,7,10,5,8,9,3,10,6,4,-9,-2,1,-3],[-3,-6,-5,-3,3,-10,-8,-2,4,10,-1,-5,7,3],[9,7,-8,7,5,8,-9,-10,-9,10,4,3,-4,-4],[-8,-7,5,-8,-8,-8,-4,3,-5,10,7,5,-10,5],[-9,-3,9,5,-7,-9,-10,9,3,9,7,10,-1,-5],[5,5,2,4,-9,5,4,10,-1,9,-3,10,10,-3],[-6,2,-10,-7,4,-2,-2,6,1,1,-6,-5,-1,-10],[4,-1,-4,2,-9,-4,2,-3,-5,10,6,-7,2,-3]],[[9,-3,9,-3,-9,4,-6,9,8,-2,-1,-8,-4,1],[-1,8,-10,-10,6,-1,-8,1,7,2,1,6,-6,1],[3,3,-10,1,5,10,-7,-6,-8,-1,-8,8,-6,-5],[3,10,10,10,-8,2,4,-5,-3,-8,-10,5,3,-1],[-10,-1,2,8,7,-2,1,-8,-5,8,6,10,6,-7],[-9,-5,-5,-9,-8,-9,-7,1,8,-2,6,3,-5,-9],[-8,-7,-5,3,1,-6,-1,7,9,-5,-9,10,-9,7],[-5,5,3,8,8,-7,-5,9,10,-5,6,-4,9,10],[6,-1,6,-4,-2,6,-6,-9,5,-9,6,4,6,-6],[-3,-2,-8,1,9,-10,8,10,-8,-4,-9,-8,9,-6],[3,1,-10,6,-3,1,-2,4,-6,1,3,7,-10,-6],[10,-5,6,8,8,6,-2,-5,8,4,4,-8,-3,-9],[-9,-2,-9,-1,-3,-2,6,4,7,-2,-9,-6,2,-1],[8,-7,-7,7,6,-4,8,1,6,-2,5,7,-10,8],[-9,-8,1,6,-2,7,-1,-8,6,5,-3,4,-2,-1]]], dtype = "uint8")#candidate|14711|(2, 15, 14)|const|uint8
var_14712 = relay.var("var_14712", dtype = "uint8", shape = (2, 15, 14))#candidate|14712|(2, 15, 14)|var|uint8
bop_14713 = relay.add(const_14711.astype('uint8'), relay.reshape(var_14712.astype('uint8'), relay.shape_of(const_14711))) # shape=(2, 15, 14)
output = relay.Tuple([bop_14713,])
output2 = relay.Tuple([bop_14713,])
F = relay.Function([var_14712,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_14712,], output2)
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
