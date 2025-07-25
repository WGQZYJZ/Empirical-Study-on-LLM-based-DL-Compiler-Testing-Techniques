import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_1122 = relay.const([[[2,10,-5,-9,-5,2,2,-8],[-6,3,2,-3,-9,-3,6,7],[-7,5,-2,-4,3,-10,1,9],[9,-7,9,8,-2,-3,4,-6],[6,3,-6,-5,-3,3,3,3]],[[5,4,9,3,1,-2,7,6],[-7,-1,5,1,3,4,-7,7],[-9,7,-1,3,-10,8,1,1],[2,3,8,-5,-2,-6,-8,-1],[3,6,2,-9,2,-10,-3,3]],[[2,5,3,-2,9,-2,-2,5],[-4,-1,-2,-9,-10,-9,9,-10],[-1,-3,-5,7,-5,-2,-5,2],[9,6,-6,8,-3,10,-1,4],[-3,6,2,-1,-4,3,1,-9]],[[-1,-4,7,4,8,-3,-2,1],[-2,3,-10,-2,-9,-4,-2,-3],[-7,1,-8,5,9,-3,2,6],[10,-1,-8,-7,-8,9,5,3],[8,7,9,10,-9,-8,-8,9]],[[6,10,-3,-10,7,10,-1,3],[7,5,-3,5,-1,-5,7,-9],[-3,8,-6,-6,-10,-5,9,2],[10,-3,6,9,1,6,-7,5],[-4,6,3,-2,-8,6,7,-3]],[[-7,1,4,-1,-3,5,4,4],[2,7,-3,10,6,-7,4,-1],[8,-6,-2,-9,6,9,-3,7],[2,-3,-4,4,-9,-4,-3,-7],[7,-3,-10,5,6,5,4,9]],[[7,1,-4,-3,8,-9,-10,-1],[-8,5,-9,-6,-4,-8,-3,6],[-8,-3,-4,7,-2,2,-1,-9],[1,8,6,-7,-5,1,-2,1],[-8,2,9,-3,-4,-4,-9,-5]],[[-9,-10,-9,7,4,3,9,-3],[6,-6,-5,-7,3,3,6,-2],[-2,-2,-3,-4,-7,10,1,-10],[1,4,-4,-4,-6,-10,-8,7],[-9,1,-8,-7,-2,-10,2,-9]],[[-7,-8,8,9,-10,6,3,8],[-2,2,-1,-4,7,5,-7,2],[-1,-6,-4,-3,-6,-2,2,-1],[-8,4,-3,4,6,9,8,-7],[2,6,-8,10,-7,5,4,-4]],[[10,-6,10,-2,3,-10,-1,-8],[10,-8,-4,-4,-1,-10,4,1],[-4,6,-9,2,10,-1,-1,-3],[-6,1,9,10,-6,-5,4,6],[-3,6,1,-3,2,-3,4,3]]], dtype = "uint8")#candidate|1122|(10, 5, 8)|const|uint8
var_1123 = relay.var("var_1123", dtype = "uint8", shape = (10, 5, 8))#candidate|1123|(10, 5, 8)|var|uint8
bop_1124 = relay.multiply(const_1122.astype('uint8'), relay.reshape(var_1123.astype('uint8'), relay.shape_of(const_1122))) # shape=(10, 5, 8)
output = bop_1124
output2 = bop_1124
func_1128 = relay.Function([var_1123,], output)
mod['func_1128'] = func_1128
mod = relay.transform.InferType()(mod)
var_1129 = relay.var("var_1129", dtype = "uint8", shape = (10, 5, 8))#candidate|1129|(10, 5, 8)|var|uint8
output = func_1128(var_1129)
func_1130 = relay.Function([var_1129], output)
mutated_mod['func_1130'] = func_1130
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1210 = relay.var("var_1210", dtype = "float32", shape = (13, 5, 15))#candidate|1210|(13, 5, 15)|var|float32
uop_1211 = relay.log2(var_1210.astype('float32')) # shape=(13, 5, 15)
output = relay.Tuple([uop_1211,])
output2 = relay.Tuple([uop_1211,])
func_1225 = relay.Function([var_1210,], output)
mod['func_1225'] = func_1225
mod = relay.transform.InferType()(mod)
mutated_mod['func_1225'] = func_1225
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1226 = relay.var("var_1226", dtype = "float32", shape = (13, 5, 15))#candidate|1226|(13, 5, 15)|var|float32
func_1225_call = mutated_mod.get_global_var('func_1225')
call_1227 = func_1225_call(var_1226)
output = call_1227
func_1228 = relay.Function([var_1226], output)
mutated_mod['func_1228'] = func_1228
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1275 = relay.var("var_1275", dtype = "int8", shape = (9, 7, 10))#candidate|1275|(9, 7, 10)|var|int8
var_1276 = relay.var("var_1276", dtype = "int8", shape = (9, 7, 10))#candidate|1276|(9, 7, 10)|var|int8
bop_1277 = relay.subtract(var_1275.astype('int8'), relay.reshape(var_1276.astype('int8'), relay.shape_of(var_1275))) # shape=(9, 7, 10)
output = relay.Tuple([bop_1277,])
output2 = relay.Tuple([bop_1277,])
func_1283 = relay.Function([var_1275,var_1276,], output)
mod['func_1283'] = func_1283
mod = relay.transform.InferType()(mod)
var_1284 = relay.var("var_1284", dtype = "int8", shape = (9, 7, 10))#candidate|1284|(9, 7, 10)|var|int8
var_1285 = relay.var("var_1285", dtype = "int8", shape = (9, 7, 10))#candidate|1285|(9, 7, 10)|var|int8
output = func_1283(var_1284,var_1285,)
func_1286 = relay.Function([var_1284,var_1285,], output)
mutated_mod['func_1286'] = func_1286
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2004 = relay.const([[[9,-6,9,4,9,1,-6,-4,-5,-9,2,5,8,3,-8,6],[10,8,9,9,-7,-1,5,1,10,-5,8,6,-1,-5,-5,8],[4,-5,9,8,4,-9,9,-9,4,1,3,7,6,4,-3,-7],[10,8,5,7,9,6,-8,7,8,-3,5,4,-1,5,3,-1],[-3,6,8,5,9,-5,8,-6,-10,-7,10,6,-2,-5,2,-1],[6,-3,1,2,-1,5,-9,-6,-2,1,4,3,-8,-2,6,-5],[3,9,-6,-1,7,8,9,-2,7,-4,3,-7,-6,1,-6,-6],[-4,10,7,-9,-7,10,-1,8,-8,-8,-10,1,-6,9,7,-1]],[[-2,1,4,4,8,-9,8,6,-8,8,9,-3,2,-9,9,1],[2,-9,-3,8,-8,-10,-2,6,-9,9,6,5,6,-8,-5,-6],[-3,1,-9,9,4,6,6,-10,-6,4,-3,-9,-4,-5,6,-4],[-6,6,4,5,-5,-5,-4,-7,-6,-2,2,9,10,5,-3,6],[-3,-7,8,-4,4,3,6,8,-2,10,-4,10,-1,10,3,7],[10,3,-7,-10,-6,-9,-4,-2,-7,-10,9,5,-6,-8,-2,-3],[9,10,-2,-7,5,9,-10,8,5,-8,-10,6,9,3,9,4],[3,-3,4,3,5,9,-5,5,-4,4,-8,-10,-6,-6,10,-2]],[[4,9,-5,-5,6,-6,-10,-3,-5,-10,9,10,2,10,-6,6],[8,-7,-6,1,-8,-5,9,-5,-4,7,-3,-9,-3,-7,-1,-10],[-6,10,-1,6,-10,-8,-8,3,-7,5,9,7,3,4,6,-3],[-1,8,5,-1,-6,6,-1,-6,-3,-10,-5,6,-10,-3,4,-1],[-10,9,5,-2,9,7,-9,8,-5,4,-5,9,-1,-4,-8,-10],[-5,4,8,-5,6,-7,-6,-8,-5,-1,3,8,10,-8,8,-7],[-8,-5,6,3,3,-8,-7,9,9,6,8,5,-7,-8,-3,-8],[-5,7,-6,-5,2,-5,10,-5,-4,10,-5,3,7,7,-8,1]],[[9,-7,8,-1,7,-1,3,-5,-5,10,9,-1,5,-8,-2,-8],[-7,-5,9,7,-5,-3,4,-5,3,10,9,8,-9,6,-5,4],[1,7,7,-6,-4,-3,8,-7,1,3,-7,3,5,-9,6,-2],[-3,7,-7,-4,-3,-7,-3,4,-10,-6,-7,-4,2,5,-7,5],[8,-9,6,-3,-10,-1,-5,-9,-1,-5,-5,1,4,-5,2,10],[3,-6,3,-7,-10,-6,-5,-3,1,7,6,-3,-5,-9,10,9],[-9,2,4,4,10,-2,-6,-3,10,-3,7,7,6,-1,5,2],[4,-7,3,-6,-3,10,-1,8,-1,10,-1,-2,-2,5,-2,1]],[[-1,8,-2,-9,-1,8,-1,7,-9,2,3,9,8,3,3,7],[4,9,10,-1,-8,4,5,-1,-8,6,-8,5,1,7,-1,7],[2,1,6,2,3,5,-7,4,-1,7,7,7,-9,9,1,-7],[-2,2,2,-5,-9,-3,-9,4,-9,-1,-4,-4,5,6,9,-8],[4,2,5,1,8,-2,2,6,8,10,8,-6,-7,-10,6,9],[9,5,1,-7,1,3,-7,7,-8,9,10,2,10,6,-1,5],[8,-3,-6,-5,2,-10,-1,-8,3,7,-5,-1,-1,10,-1,4],[-6,8,1,-9,-5,6,6,-3,3,10,-8,-4,7,-3,-10,-10]],[[5,-8,-3,-1,-8,4,-9,2,-8,-2,5,-5,10,3,-6,8],[-4,10,-5,-8,6,-6,-1,-8,1,5,-6,10,-2,-7,9,2],[2,-3,-4,10,2,-6,-4,-4,-6,3,-1,7,-8,-2,8,10],[-7,-6,3,1,-4,10,5,5,3,1,-4,5,-1,-9,-10,-10],[2,-10,-4,4,-1,-7,8,-6,-3,5,5,7,9,-8,7,-8],[6,7,10,-7,6,5,-8,-5,10,-8,1,3,-3,1,-9,-2],[8,2,-9,-8,6,8,-8,5,-4,3,10,7,4,-5,8,7],[-7,7,9,10,1,-9,1,-7,1,-2,3,-6,7,2,-1,5]]], dtype = "int8")#candidate|2004|(6, 8, 16)|const|int8
var_2005 = relay.var("var_2005", dtype = "int8", shape = (6, 8, 16))#candidate|2005|(6, 8, 16)|var|int8
bop_2006 = relay.logical_xor(const_2004.astype('int8'), relay.reshape(var_2005.astype('int8'), relay.shape_of(const_2004))) # shape=(6, 8, 16)
func_1225_call = mod.get_global_var('func_1225')
func_1228_call = mutated_mod.get_global_var('func_1228')
var_2010 = relay.var("var_2010", dtype = "float32", shape = (975, 1))#candidate|2010|(975, 1)|var|float32
call_2009 = relay.TupleGetItem(func_1225_call(relay.reshape(var_2010.astype('float32'), [13, 5, 15])), 0)
call_2011 = relay.TupleGetItem(func_1228_call(relay.reshape(var_2010.astype('float32'), [13, 5, 15])), 0)
func_1128_call = mod.get_global_var('func_1128')
func_1130_call = mutated_mod.get_global_var('func_1130')
const_2015 = relay.const([7,6,-6,-8,8,-8,6,-8,8,7,9,-8,-10,-7,-9,10,-2,3,-5,8,-1,-10,-6,-9,-6,-4,6,8,-7,7,-9,3,-3,-7,9,4,4,5,10,-6,-10,-5,-4,-4,-8,-6,6,-8,6,-9,-5,-5,5,-10,-5,5,-9,-2,3,-4,7,-10,1,-3,-5,6,-5,8,-10,-9,7,10,4,8,10,-10,6,-1,8,-8,10,3,-2,7,9,10,-10,1,4,3,3,-4,-5,-6,3,-6,-7,-8,9,-2,1,-6,2,-9,7,4,-7,-9,-5,5,-10,-9,-9,-5,-2,9,-10,-8,-4,-3,-9,3,7,-10,10,10,-6,8,-8,6,-1,-5,1,7,10,-8,-9,7,-6,8,-2,-7,-7,-6,7,5,6,-3,3,4,-10,-2,-5,4,-8,9,-1,10,1,-3,7,-10,-7,-2,3,-4,10,3,-7,-9,9,6,-4,8,-4,6,10,-4,9,9,-2,4,-9,7,3,-10,4,4,4,-5,-6,8,7,5,8,7,-7,9,-9,9,-2,6,-6,-6,-4,-7,-2,-6,-8,6,-5,5,-5,7,1,-9,6,1,-8,2,-7,-2,-5,9,-1,9,-9,7,9,9,-1,-4,-6,9,-1,-5,10,-9,-8,-10,3,-5,6,-6,10,-4,6,10,-5,5,1,-6,9,-8,4,-6,-7,-1,6,7,-5,-7,-1,2,-5,3,6,9,-5,-4,4,7,-2,-6,8,-4,-6,-5,-7,4,3,-10,-7,6,-7,-8,-10,-4,-3,-1,-6,5,8,-1,-6,-9,-2,-10,9,10,6,-6,-5,9,3,-1,6,10,-4,9,6,1,-8,-9,-6,-4,7,9,2,-9,9,-3,6,1,4,3,7,-8,-4,-3,-5,3,6,-3,-3,5,-4,8,-2,3,-8,-6,10,-1,10,-5,10,-7,1,7,4,-5,-2,10,2,2,10,7,3,-4,-2,9,6,-10,-6,2,-3,-10,-2,1,-8,3,4,-9,8,1,2,-3,6,7,4,-3,6,2,-8,1,-9,-3,6,9,5,5,-7,-4,-6,6,10,-7,-5,-4], dtype = "uint8")#candidate|2015|(400,)|const|uint8
call_2014 = func_1128_call(relay.reshape(const_2015.astype('uint8'), [10, 5, 8]))
call_2016 = func_1128_call(relay.reshape(const_2015.astype('uint8'), [10, 5, 8]))
uop_2020 = relay.atanh(var_2005.astype('float32')) # shape=(6, 8, 16)
func_1225_call = mod.get_global_var('func_1225')
func_1228_call = mutated_mod.get_global_var('func_1228')
call_2024 = relay.TupleGetItem(func_1225_call(relay.reshape(var_2010.astype('float32'), [13, 5, 15])), 0)
call_2025 = relay.TupleGetItem(func_1228_call(relay.reshape(var_2010.astype('float32'), [13, 5, 15])), 0)
output = relay.Tuple([bop_2006,call_2009,var_2010,call_2014,const_2015,uop_2020,call_2024,])
output2 = relay.Tuple([bop_2006,call_2011,var_2010,call_2016,const_2015,uop_2020,call_2025,])
func_2034 = relay.Function([var_2005,var_2010,], output)
mod['func_2034'] = func_2034
mod = relay.transform.InferType()(mod)
mutated_mod['func_2034'] = func_2034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2034_call = mutated_mod.get_global_var('func_2034')
var_2036 = relay.var("var_2036", dtype = "int8", shape = (6, 8, 16))#candidate|2036|(6, 8, 16)|var|int8
var_2037 = relay.var("var_2037", dtype = "float32", shape = (975, 1))#candidate|2037|(975, 1)|var|float32
call_2035 = func_2034_call(var_2036,var_2037,)
output = call_2035
func_2038 = relay.Function([var_2036,var_2037,], output)
mutated_mod['func_2038'] = func_2038
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2091 = relay.var("var_2091", dtype = "float32", shape = (3, 16, 4))#candidate|2091|(3, 16, 4)|var|float32
uop_2092 = relay.asinh(var_2091.astype('float32')) # shape=(3, 16, 4)
func_2034_call = mod.get_global_var('func_2034')
func_2038_call = mutated_mod.get_global_var('func_2038')
const_2096 = relay.const([-1,4,5,7,-5,-3,5,-5,2,-10,-7,9,3,-6,-10,-7,-10,-9,2,-2,-10,5,10,-4,3,-5,7,6,10,2,-7,-10,-2,3,-4,-3,4,2,8,-8,-10,-9,-1,-10,7,10,3,-10,-9,-10,-1,-9,-9,-9,-9,-7,-2,-7,-1,5,-8,-3,-6,-7,9,-10,-8,-3,2,-5,-1,-1,9,7,6,10,-6,7,8,-9,-9,7,-7,-8,4,-1,6,-9,3,-6,9,-5,1,-7,3,-7,-4,-4,5,-2,-5,-4,-9,5,1,1,9,5,5,10,9,-2,2,-5,-8,-7,-2,-4,-6,-2,-2,8,-8,-1,6,-3,-9,-9,-3,-9,1,-5,-7,-5,10,1,-2,-3,-2,5,8,-3,3,9,6,8,-3,2,2,4,-9,-5,-6,3,-5,-5,6,-7,2,6,3,5,5,-8,9,10,-9,-10,3,4,-10,8,-9,-7,-2,-10,5,3,-5,8,2,-3,-2,7,-6,3,10,-4,-10,-1,-1,9,6,-7,-10,-6,-6,-5,-2,6,-1,-6,2,-1,8,-7,5,-5,6,4,1,-10,1,-5,-8,-2,10,2,-7,-4,-7,4,-7,-4,2,-10,-10,-8,-8,5,-4,4,7,5,9,9,-10,-9,-1,-9,9,-6,2,9,8,3,-2,-3,-5,3,8,9,4,-5,10,-5,-3,-7,6,-4,-3,4,6,-6,-6,4,-2,9,2,8,10,-1,6,-10,8,-5,-3,-8,-6,1,-5,3,-9,-1,10,2,-3,-3,-3,-1,8,-1,5,-9,4,-5,6,-4,4,-5,5,2,-2,-6,1,5,-3,8,6,1,9,10,-3,10,10,-10,5,-10,1,2,-3,-9,3,-4,-7,2,-10,1,5,-1,-7,9,-4,-8,6,7,7,6,5,1,-5,-8,-5,8,-10,-4,-7,10,-3,8,-8,-7,-3,5,2,-10,10,10,8,-5,7,7,4,7,4,5,2,-9,4,3,-3,-3,-2,8,2,-8,5,-3,3,-8,-7,10,-6,2,-4,-8,-9,-10,5,-3,-3,6,-6,-9,-10,7,2,5,-6,-8,6,-5,-6,-8,-5,9,-1,6,-3,10,3,-1,3,-3,-6,1,-8,7,-3,6,-7,4,8,-9,8,-6,-5,8,-4,-8,3,-2,-8,-6,5,9,-6,10,-4,7,-6,-4,2,10,-4,-6,-10,9,-9,-8,-4,-8,9,-4,-7,-6,-6,8,6,-3,6,9,-10,-3,1,5,8,8,3,2,-5,-7,-1,-8,-10,-7,-2,4,3,3,9,-1,-3,-4,-3,8,-5,8,7,2,6,-8,4,-10,-1,4,3,9,-4,-2,-9,4,3,-1,7,2,1,-2,1,-5,-5,2,-4,-3,4,-7,6,-9,1,-3,-3,2,2,2,-5,6,6,7,-1,-10,8,9,7,4,8,-8,10,-7,-3,-8,6,8,3,1,6,6,9,7,-3,-3,8,-4,-1,-1,-9,-3,-2,-8,6,9,-3,7,2,5,5,-8,1,-1,4,9,2,8,-2,-1,6,-2,4,-10,-3,4,4,1,6,2,-6,3,4,4,-8,6,-4,4,6,-6,8,7,4,1,-1,-9,-5,-7,-2,5,-5,-5,-9,-10,-2,4,-8,3,-8,-1,-9,-8,-1,-3,5,4,-9,10,9,-3,-6,-10,-7,-6,9,-5,-8,-3,7,5,-4,-3,-9,2,-3,-6,3,5,8,6,1,-6,-4,9,4,1,-2,-2,-7,6,3,-1,7,-6,-7,4,4,6,-6,-7,-8,8,-5,8,9,4,-7,8,-10,3,-9,-5,5,-10,6,-1,10,-2,-2,-8,8,2,-6,-3,5,4,-1,8,10,-10,7,-1,-3,-3,7,5,-3,1,7,4,10,-7,-6,-8,1,3,1,7,6,8,-1,-9,4,-2,5,-3,5,-5,-3,9,3,5,5,8,2,-7,3,-9,-7,7,8,-5,10,-8,-5,8,-9,3,-7,-9,9,3,-3,8,-3,2,-3,-6,8,-7,-1,2,9,5,-4,-4,10,4,10,-3,-5,6,-3,2], dtype = "int8")#candidate|2096|(768,)|const|int8
var_2097 = relay.var("var_2097", dtype = "float32", shape = (975,))#candidate|2097|(975,)|var|float32
call_2095 = relay.TupleGetItem(func_2034_call(relay.reshape(const_2096.astype('int8'), [6, 8, 16]), relay.reshape(var_2097.astype('float32'), [975, 1]), ), 4)
call_2098 = relay.TupleGetItem(func_2038_call(relay.reshape(const_2096.astype('int8'), [6, 8, 16]), relay.reshape(var_2097.astype('float32'), [975, 1]), ), 4)
output = relay.Tuple([uop_2092,call_2095,const_2096,var_2097,])
output2 = relay.Tuple([uop_2092,call_2098,const_2096,var_2097,])
func_2115 = relay.Function([var_2091,var_2097,], output)
mod['func_2115'] = func_2115
mod = relay.transform.InferType()(mod)
var_2116 = relay.var("var_2116", dtype = "float32", shape = (3, 16, 4))#candidate|2116|(3, 16, 4)|var|float32
var_2117 = relay.var("var_2117", dtype = "float32", shape = (975,))#candidate|2117|(975,)|var|float32
output = func_2115(var_2116,var_2117,)
func_2118 = relay.Function([var_2116,var_2117,], output)
mutated_mod['func_2118'] = func_2118
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2357 = relay.var("var_2357", dtype = "bool", shape = ())#candidate|2357|()|var|bool
var_2358 = relay.var("var_2358", dtype = "bool", shape = (2, 11, 1))#candidate|2358|(2, 11, 1)|var|bool
bop_2359 = relay.logical_and(var_2357.astype('bool'), var_2358.astype('bool')) # shape=(2, 11, 1)
output = relay.Tuple([bop_2359,])
output2 = relay.Tuple([bop_2359,])
func_2363 = relay.Function([var_2357,var_2358,], output)
mod['func_2363'] = func_2363
mod = relay.transform.InferType()(mod)
mutated_mod['func_2363'] = func_2363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2363_call = mutated_mod.get_global_var('func_2363')
var_2365 = relay.var("var_2365", dtype = "bool", shape = ())#candidate|2365|()|var|bool
var_2366 = relay.var("var_2366", dtype = "bool", shape = (2, 11, 1))#candidate|2366|(2, 11, 1)|var|bool
call_2364 = func_2363_call(var_2365,var_2366,)
output = call_2364
func_2367 = relay.Function([var_2365,var_2366,], output)
mutated_mod['func_2367'] = func_2367
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2431 = relay.var("var_2431", dtype = "int8", shape = (12, 1, 10))#candidate|2431|(12, 1, 10)|var|int8
var_2432 = relay.var("var_2432", dtype = "int8", shape = (12, 12, 10))#candidate|2432|(12, 12, 10)|var|int8
bop_2433 = relay.add(var_2431.astype('int8'), var_2432.astype('int8')) # shape=(12, 12, 10)
output = relay.Tuple([bop_2433,])
output2 = relay.Tuple([bop_2433,])
func_2444 = relay.Function([var_2431,var_2432,], output)
mod['func_2444'] = func_2444
mod = relay.transform.InferType()(mod)
var_2445 = relay.var("var_2445", dtype = "int8", shape = (12, 1, 10))#candidate|2445|(12, 1, 10)|var|int8
var_2446 = relay.var("var_2446", dtype = "int8", shape = (12, 12, 10))#candidate|2446|(12, 12, 10)|var|int8
output = func_2444(var_2445,var_2446,)
func_2447 = relay.Function([var_2445,var_2446,], output)
mutated_mod['func_2447'] = func_2447
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2647 = relay.var("var_2647", dtype = "float64", shape = (7, 10, 4))#candidate|2647|(7, 10, 4)|var|float64
var_2648 = relay.var("var_2648", dtype = "float64", shape = (7, 10, 4))#candidate|2648|(7, 10, 4)|var|float64
bop_2649 = relay.mod(var_2647.astype('float64'), relay.reshape(var_2648.astype('float64'), relay.shape_of(var_2647))) # shape=(7, 10, 4)
func_1128_call = mod.get_global_var('func_1128')
func_1130_call = mutated_mod.get_global_var('func_1130')
var_2653 = relay.var("var_2653", dtype = "uint8", shape = (400,))#candidate|2653|(400,)|var|uint8
call_2652 = func_1128_call(relay.reshape(var_2653.astype('uint8'), [10, 5, 8]))
call_2654 = func_1128_call(relay.reshape(var_2653.astype('uint8'), [10, 5, 8]))
func_1283_call = mod.get_global_var('func_1283')
func_1286_call = mutated_mod.get_global_var('func_1286')
const_2661 = relay.const([3,-3,-6,10,10,8,1,1,6,9,-9,-10,9,9,10,-6,-3,-6,1,-7,-9,4,2,6,-3,1,-1,2,-2,4,2,8,1,4,-2,-3,-7,-9,-2,-6,-9,6,7,-2,10,-2,-7,10,4,10,-7,7,1,1,-2,-8,-4,-2,4,-2,1,-9,-6,-6,2,-8,-8,1,10,3,-10,2,-5,5,-10,6,-2,-10,3,-9,-10,2,-2,9,6,4,3,8,-2,-1,-1,-2,1,1,7,-9,-9,-9,5,-4,10,-4,6,2,6,-8,10,10,-5,-7,5,1,6,-6,6,9,8,10,7,1,5,2,1,-9,5,9,2,5,-10,1,10,3,-5,-1,-6,8,2,-9,2,-1,5,-10,-10,7,5,-5,7,-3,2,7,-4,9,4,1,7,-6,2,9,10,-9,3,-10,-3,-5,4,-2,6,6,-3,-8,9,-3,2,2,-8,-7,-6,-1,7,-7,-7,-3,2,3,-8,-6,-8,7,-10,2,-1,-9,5,9,8,-4,5,-6,-9,-4,3,-4,-8,-1,-2,-8,-1,2,-9,-7,-5,1,-10,-8,-7,6,2,-3,2,3,-8,-9,-10,-6,-1,7,7,5,5,6,4,6,-1,10,-4,9,4,2,8,4,-2,-5,-8,-6,-4,7,-4,5,1,-1,8,6,8,7,-7,-7,-1,9,5,-2,-8,6,-1,7,8,-4,8,10,7,5,-6,4,7,7,-7,-10,8,-6,6,-1,-3,-3,-3,8,8,-6,6,-4,-1,6,1,-4,-9,-10,-6,-3,3,10,7,-10,1,-9,-5,-1,-3,-6,-2,-5,-1,-10,-3,-7,-7,4,7,8,9,-7,10,1,-5,-10,-7,10,10,-6,10,-1,2,-10,-1,-7,6,7,1,1,-6,3,-8,1,2,10,3,-9,-9,4,-7,-2,-2,-1,8,-9,5,-8,-6,10,8,-9,3,6,7,4,8,9,5,-4,-3,5,-6,2,2,9,-4,-1,-6,-1,-4,9,10,-3,-7,6,-10,10,4,6,-4,7,3,8,-4,2,-3,1,8,-8,1,-5,-5,-6,6,6,-7,9,1,-9,6,5,2,-5,-2,-5,7,5,-6,-4,3,2,2,-1,-1,-10,-2,8,-2,4,8,-6,-9,8,2,-8,1,-6,-3,8,7,-3,-4,5,-6,8,6,8,5,-1,-7,1,-8,2,3,-9,7,-1,5,-7,-3,-4,10,-6,-7,3,7,3,-10,9,5,4,-2,-5,1,7,-8,4,-4,-5,9,-8,-2,2,-3,7,-10,2,-8,-10,-8,2,9,-3,8,5,-6,4,3,-1,-10,6,1,-4,4,7,-1,7,-7,-3,8,4,3,3,-5,-2,-5,5,-6,-7,10,-2,5,1,10,10,-5,4,-2,2,1,4,-2,-4,-7,9,-6,-10,-10,6,-6,2,1,-7,-10,4,-5,-9,-5,-7,7,10,5,-6,-1,-9,-1,8,4,6,-6,-9,-7,10,-3,-4,1,4,6,-4,-4,-5,1,-6,-7,-1,3,4,10,1,10,-4,3,-8,-9,7,-3,-8,-4,-1,7,5,-4,9,4,-7,-9,-5,8,1,-6,-1,-1,-7,-3,7,2,7,3,-2,-8,-3,-2,9,-4,7,1,10,7,6,-8,10,-6,-8,5,-10,-10,9,-1,-2,-9,6,-9,1], dtype = "int8")#candidate|2661|(630,)|const|int8
call_2660 = relay.TupleGetItem(func_1283_call(relay.reshape(const_2661.astype('int8'), [9, 7, 10]), relay.reshape(const_2661.astype('int8'), [9, 7, 10]), ), 0)
call_2662 = relay.TupleGetItem(func_1286_call(relay.reshape(const_2661.astype('int8'), [9, 7, 10]), relay.reshape(const_2661.astype('int8'), [9, 7, 10]), ), 0)
output = relay.Tuple([bop_2649,call_2652,var_2653,call_2660,const_2661,])
output2 = relay.Tuple([bop_2649,call_2654,var_2653,call_2662,const_2661,])
func_2670 = relay.Function([var_2647,var_2648,var_2653,], output)
mod['func_2670'] = func_2670
mod = relay.transform.InferType()(mod)
var_2671 = relay.var("var_2671", dtype = "float64", shape = (7, 10, 4))#candidate|2671|(7, 10, 4)|var|float64
var_2672 = relay.var("var_2672", dtype = "float64", shape = (7, 10, 4))#candidate|2672|(7, 10, 4)|var|float64
var_2673 = relay.var("var_2673", dtype = "uint8", shape = (400,))#candidate|2673|(400,)|var|uint8
output = func_2670(var_2671,var_2672,var_2673,)
func_2674 = relay.Function([var_2671,var_2672,var_2673,], output)
mutated_mod['func_2674'] = func_2674
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3512 = relay.var("var_3512", dtype = "uint8", shape = ())#candidate|3512|()|var|uint8
var_3513 = relay.var("var_3513", dtype = "uint8", shape = (11, 1, 7))#candidate|3513|(11, 1, 7)|var|uint8
bop_3514 = relay.less(var_3512.astype('bool'), var_3513.astype('bool')) # shape=(11, 1, 7)
func_1283_call = mod.get_global_var('func_1283')
func_1286_call = mutated_mod.get_global_var('func_1286')
const_3529 = relay.const([5,-5,-9,-4,1,-9,-3,8,1,1,-8,-3,-6,-1,10,-7,2,-5,-6,-5,-1,6,3,1,-1,2,-9,-6,3,1,5,-2,1,6,-8,-6,9,-3,3,-6,10,-8,6,5,-1,-5,-4,3,-6,-5,-4,-3,1,5,4,10,1,3,2,-7,4,-9,-8,-4,-5,-9,7,2,-2,4,8,9,2,5,2,6,3,-4,2,-7,6,4,2,3,-10,-9,3,-8,-2,10,6,-9,3,-1,-1,10,6,3,1,-1,5,1,-8,4,1,-5,9,-7,-5,-9,-9,-6,-4,-3,8,-8,-4,2,6,-5,9,-6,-1,-3,1,7,-1,-7,3,-4,3,-4,10,2,-2,-5,-4,9,3,-6,-4,-6,-5,3,-2,6,8,-6,-10,4,-3,4,1,-7,-5,-1,-5,5,-10,5,-5,9,5,-10,4,-8,5,6,-5,-10,-5,1,-8,9,5,9,-9,3,-6,10,9,6,-9,-7,7,-5,8,4,4,-3,-1,1,3,-5,-9,6,2,1,6,6,-7,10,8,-1,-9,-1,7,10,6,-8,2,-4,-7,8,6,9,-8,1,2,10,6,-2,3,-4,1,7,-7,-10,7,8,-5,-7,5,-8,-9,10,10,-10,-6,-6,-8,10,4,-10,9,4,-4,-4,-10,7,3,-7,-9,-7,-3,2,6,7,-4,-10,-4,7,-9,10,-5,1,4,8,6,10,8,3,6,3,8,2,-2,-1,-10,-10,-7,1,-8,-7,-6,-4,-9,-10,8,4,9,-7,3,-1,8,-7,2,-8,-1,-5,-4,-3,7,-7,-7,10,-6,-8,-6,3,-10,-2,-10,-3,7,-10,-6,-3,6,-7,-2,-2,5,-1,-7,-8,9,-9,2,10,9,-10,4,-7,5,7,10,-10,-7,7,-7,3,7,-5,-4,-6,-6,8,-2,-2,9,-8,7,6,-9,10,-10,-2,-4,3,3,-1,-8,10,-1,10,-10,-1,-6,-10,9,-3,-10,-3,-3,2,-8,6,1,-7,-6,4,-5,2,-9,-6,-2,-5,-5,9,-7,-5,-4,-10,-7,-7,3,-1,-4,8,5,2,-5,2,-9,10,-9,-8,4,-8,-4,5,6,-4,9,6,9,3,-6,6,3,-1,8,7,-7,4,10,9,-5,8,8,-10,-1,1,-8,-5,10,7,-5,-2,1,-6,-7,-1,-9,-8,1,3,3,-1,10,5,-2,-10,1,1,-9,-5,3,1,-4,-8,9,9,5,6,-6,7,-5,2,8,8,-10,4,-10,5,3,9,7,5,-7,-1,-4,-8,-5,5,-6,1,-7,-1,-9,10,-4,-8,-6,6,6,6,-6,-6,-7,-2,-5,10,9,8,-10,2,9,6,2,9,-9,-7,9,4,6,8,-1,3,10,8,2,-5,-1,-6,-2,1,2,-6,1,7,-8,-9,5,-8,3,-6,-7,4,3,3,7,-9,-3,-1,7,-4,-5,5,-2,5,-1,10,2,-8,-4,-10,-6,-1,6,-3,-10,-7,9,4,-6,-7,-8,7,-1,-6,-7,-9,5,-1,-3,-3,1,-9,3,4,-10,6,-7,9,9,4,-2,-8,2,10,-6,-8,5,9,-1,-9,3,-1,8,10,-5,-3,7,6,3,-7,-2,-7,-4,-7,9,-6,-9,3,-6,7,7,-10,3,6,-3,6,9,2,-2,-6,5,3], dtype = "int8")#candidate|3529|(630,)|const|int8
call_3528 = relay.TupleGetItem(func_1283_call(relay.reshape(const_3529.astype('int8'), [9, 7, 10]), relay.reshape(const_3529.astype('int8'), [9, 7, 10]), ), 0)
call_3530 = relay.TupleGetItem(func_1286_call(relay.reshape(const_3529.astype('int8'), [9, 7, 10]), relay.reshape(const_3529.astype('int8'), [9, 7, 10]), ), 0)
output = relay.Tuple([bop_3514,call_3528,const_3529,])
output2 = relay.Tuple([bop_3514,call_3530,const_3529,])
func_3544 = relay.Function([var_3512,var_3513,], output)
mod['func_3544'] = func_3544
mod = relay.transform.InferType()(mod)
mutated_mod['func_3544'] = func_3544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3544_call = mutated_mod.get_global_var('func_3544')
var_3546 = relay.var("var_3546", dtype = "uint8", shape = ())#candidate|3546|()|var|uint8
var_3547 = relay.var("var_3547", dtype = "uint8", shape = (11, 1, 7))#candidate|3547|(11, 1, 7)|var|uint8
call_3545 = func_3544_call(var_3546,var_3547,)
output = call_3545
func_3548 = relay.Function([var_3546,var_3547,], output)
mutated_mod['func_3548'] = func_3548
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4458 = relay.var("var_4458", dtype = "int16", shape = (5, 8, 4))#candidate|4458|(5, 8, 4)|var|int16
const_4459 = relay.const([[[-6,2,-10,7],[10,6,-6,3],[3,5,5,9],[-9,6,8,1],[-8,-9,9,-8],[3,7,5,3],[3,-9,-7,-6],[5,-8,-1,6]],[[-4,-10,2,4],[-6,-5,2,10],[-7,8,9,-8],[8,-7,7,-10],[10,-3,-10,6],[-7,6,10,-7],[-6,8,-10,8],[-6,-7,-10,-1]],[[-7,-1,-9,-4],[9,-8,-7,-7],[-9,-6,5,7],[1,-2,10,-1],[8,-5,-8,-5],[-8,-7,7,8],[1,7,2,-5],[9,-5,-3,-8]],[[-8,-7,-2,5],[-5,-7,-8,-8],[-2,5,8,-8],[9,6,10,10],[6,4,2,-8],[-2,9,1,-9],[2,-7,-3,-7],[-8,2,-6,-6]],[[2,10,1,-10],[6,-3,7,-10],[-5,9,-1,8],[-1,9,-7,-2],[7,4,4,9],[3,7,-3,9],[5,5,6,7],[-6,-9,-1,1]]], dtype = "int16")#candidate|4459|(5, 8, 4)|const|int16
bop_4460 = relay.bitwise_and(var_4458.astype('int16'), relay.reshape(const_4459.astype('int16'), relay.shape_of(var_4458))) # shape=(5, 8, 4)
output = bop_4460
output2 = bop_4460
func_4470 = relay.Function([var_4458,], output)
mod['func_4470'] = func_4470
mod = relay.transform.InferType()(mod)
var_4471 = relay.var("var_4471", dtype = "int16", shape = (5, 8, 4))#candidate|4471|(5, 8, 4)|var|int16
output = func_4470(var_4471)
func_4472 = relay.Function([var_4471], output)
mutated_mod['func_4472'] = func_4472
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4643 = relay.var("var_4643", dtype = "float32", shape = (1, 11, 6))#candidate|4643|(1, 11, 6)|var|float32
uop_4644 = relay.acosh(var_4643.astype('float32')) # shape=(1, 11, 6)
bop_4646 = relay.minimum(var_4643.astype('uint64'), relay.reshape(uop_4644.astype('uint64'), relay.shape_of(var_4643))) # shape=(1, 11, 6)
output = bop_4646
output2 = bop_4646
func_4654 = relay.Function([var_4643,], output)
mod['func_4654'] = func_4654
mod = relay.transform.InferType()(mod)
var_4655 = relay.var("var_4655", dtype = "float32", shape = (1, 11, 6))#candidate|4655|(1, 11, 6)|var|float32
output = func_4654(var_4655)
func_4656 = relay.Function([var_4655], output)
mutated_mod['func_4656'] = func_4656
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4815 = relay.var("var_4815", dtype = "int8", shape = (1, 6, 14))#candidate|4815|(1, 6, 14)|var|int8
var_4816 = relay.var("var_4816", dtype = "int8", shape = (2, 6, 14))#candidate|4816|(2, 6, 14)|var|int8
bop_4817 = relay.bitwise_and(var_4815.astype('int8'), var_4816.astype('int8')) # shape=(2, 6, 14)
output = bop_4817
output2 = bop_4817
func_4833 = relay.Function([var_4815,var_4816,], output)
mod['func_4833'] = func_4833
mod = relay.transform.InferType()(mod)
mutated_mod['func_4833'] = func_4833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4833_call = mutated_mod.get_global_var('func_4833')
var_4835 = relay.var("var_4835", dtype = "int8", shape = (1, 6, 14))#candidate|4835|(1, 6, 14)|var|int8
var_4836 = relay.var("var_4836", dtype = "int8", shape = (2, 6, 14))#candidate|4836|(2, 6, 14)|var|int8
call_4834 = func_4833_call(var_4835,var_4836,)
output = call_4834
func_4837 = relay.Function([var_4835,var_4836,], output)
mutated_mod['func_4837'] = func_4837
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5122 = relay.var("var_5122", dtype = "int64", shape = (12, 10, 1))#candidate|5122|(12, 10, 1)|var|int64
var_5123 = relay.var("var_5123", dtype = "int64", shape = (12, 10, 6))#candidate|5123|(12, 10, 6)|var|int64
bop_5124 = relay.subtract(var_5122.astype('int64'), var_5123.astype('int64')) # shape=(12, 10, 6)
func_2444_call = mod.get_global_var('func_2444')
func_2447_call = mutated_mod.get_global_var('func_2447')
var_5131 = relay.var("var_5131", dtype = "int8", shape = (1440,))#candidate|5131|(1440,)|var|int8
call_5130 = relay.TupleGetItem(func_2444_call(relay.reshape(var_5122.astype('int8'), [12, 1, 10]), relay.reshape(var_5131.astype('int8'), [12, 12, 10]), ), 0)
call_5132 = relay.TupleGetItem(func_2447_call(relay.reshape(var_5122.astype('int8'), [12, 1, 10]), relay.reshape(var_5131.astype('int8'), [12, 12, 10]), ), 0)
output = relay.Tuple([bop_5124,call_5130,var_5131,])
output2 = relay.Tuple([bop_5124,call_5132,var_5131,])
func_5136 = relay.Function([var_5122,var_5123,var_5131,], output)
mod['func_5136'] = func_5136
mod = relay.transform.InferType()(mod)
var_5137 = relay.var("var_5137", dtype = "int64", shape = (12, 10, 1))#candidate|5137|(12, 10, 1)|var|int64
var_5138 = relay.var("var_5138", dtype = "int64", shape = (12, 10, 6))#candidate|5138|(12, 10, 6)|var|int64
var_5139 = relay.var("var_5139", dtype = "int8", shape = (1440,))#candidate|5139|(1440,)|var|int8
output = func_5136(var_5137,var_5138,var_5139,)
func_5140 = relay.Function([var_5137,var_5138,var_5139,], output)
mutated_mod['func_5140'] = func_5140
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5407 = relay.var("var_5407", dtype = "uint16", shape = (14, 3, 14))#candidate|5407|(14, 3, 14)|var|uint16
var_5408 = relay.var("var_5408", dtype = "uint16", shape = (14, 3, 14))#candidate|5408|(14, 3, 14)|var|uint16
bop_5409 = relay.maximum(var_5407.astype('uint16'), relay.reshape(var_5408.astype('uint16'), relay.shape_of(var_5407))) # shape=(14, 3, 14)
output = bop_5409
output2 = bop_5409
func_5414 = relay.Function([var_5407,var_5408,], output)
mod['func_5414'] = func_5414
mod = relay.transform.InferType()(mod)
mutated_mod['func_5414'] = func_5414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5414_call = mutated_mod.get_global_var('func_5414')
var_5416 = relay.var("var_5416", dtype = "uint16", shape = (14, 3, 14))#candidate|5416|(14, 3, 14)|var|uint16
var_5417 = relay.var("var_5417", dtype = "uint16", shape = (14, 3, 14))#candidate|5417|(14, 3, 14)|var|uint16
call_5415 = func_5414_call(var_5416,var_5417,)
output = call_5415
func_5418 = relay.Function([var_5416,var_5417,], output)
mutated_mod['func_5418'] = func_5418
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5697 = relay.var("var_5697", dtype = "float32", shape = (8, 16, 15))#candidate|5697|(8, 16, 15)|var|float32
uop_5698 = relay.log(var_5697.astype('float32')) # shape=(8, 16, 15)
bop_5723 = relay.power(var_5697.astype('float64'), relay.reshape(uop_5698.astype('float64'), relay.shape_of(var_5697))) # shape=(8, 16, 15)
output = bop_5723
output2 = bop_5723
func_5735 = relay.Function([var_5697,], output)
mod['func_5735'] = func_5735
mod = relay.transform.InferType()(mod)
mutated_mod['func_5735'] = func_5735
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5736 = relay.var("var_5736", dtype = "float32", shape = (8, 16, 15))#candidate|5736|(8, 16, 15)|var|float32
func_5735_call = mutated_mod.get_global_var('func_5735')
call_5737 = func_5735_call(var_5736)
output = call_5737
func_5738 = relay.Function([var_5736], output)
mutated_mod['func_5738'] = func_5738
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6175 = relay.var("var_6175", dtype = "uint8", shape = (14, 8, 3))#candidate|6175|(14, 8, 3)|var|uint8
var_6176 = relay.var("var_6176", dtype = "uint8", shape = (14, 8, 3))#candidate|6176|(14, 8, 3)|var|uint8
bop_6177 = relay.add(var_6175.astype('uint8'), relay.reshape(var_6176.astype('uint8'), relay.shape_of(var_6175))) # shape=(14, 8, 3)
uop_6180 = relay.sigmoid(var_6176.astype('float64')) # shape=(14, 8, 3)
output = relay.Tuple([bop_6177,uop_6180,])
output2 = relay.Tuple([bop_6177,uop_6180,])
func_6191 = relay.Function([var_6175,var_6176,], output)
mod['func_6191'] = func_6191
mod = relay.transform.InferType()(mod)
var_6192 = relay.var("var_6192", dtype = "uint8", shape = (14, 8, 3))#candidate|6192|(14, 8, 3)|var|uint8
var_6193 = relay.var("var_6193", dtype = "uint8", shape = (14, 8, 3))#candidate|6193|(14, 8, 3)|var|uint8
output = func_6191(var_6192,var_6193,)
func_6194 = relay.Function([var_6192,var_6193,], output)
mutated_mod['func_6194'] = func_6194
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7317 = relay.var("var_7317", dtype = "int64", shape = (4, 1, 2))#candidate|7317|(4, 1, 2)|var|int64
const_7318 = relay.const([[[5,7],[10,-1],[-10,-4],[-6,-5],[-3,-9],[-6,-5],[-1,10],[2,-9],[5,-4],[-9,8],[8,8],[10,-8],[-10,9]],[[-8,-4],[-5,-4],[10,-2],[9,-1],[-3,-8],[10,6],[3,-4],[1,-8],[-2,-5],[7,-2],[5,3],[1,4],[3,-6]],[[2,-7],[-4,-8],[8,1],[8,-5],[-9,3],[2,-10],[2,-7],[-6,9],[3,-2],[7,-1],[6,5],[1,-3],[6,4]],[[4,10],[-8,10],[-10,-3],[-5,1],[5,-8],[-7,6],[-2,8],[-5,-5],[8,4],[2,3],[4,-6],[-1,10],[-10,-8]]], dtype = "int64")#candidate|7318|(4, 13, 2)|const|int64
bop_7319 = relay.less(var_7317.astype('bool'), const_7318.astype('bool')) # shape=(4, 13, 2)
func_1283_call = mod.get_global_var('func_1283')
func_1286_call = mutated_mod.get_global_var('func_1286')
const_7323 = relay.const([[9,-6,-9,3,5,-8,-2,-5,4,-1,-4,-7,-1,6,4,-5,-10,-3,5,-4,5,-9,7,-5,-7,2,-7,4,9,-3,-9,-9,1,-7,7,7,3,9,1,-1,-2,2,1,-9,-3,5,-3,3,6,2,-1,-5,4,4,-8,6,7,-9,-1,9,5,9,8],[-3,2,-8,-2,-7,9,-4,8,8,5,4,-8,-1,6,-10,-2,1,-8,-6,5,9,-7,-2,-10,-10,10,2,-6,-2,4,1,6,-7,2,-5,9,1,-6,8,-3,-2,2,-2,8,3,7,8,-5,-6,-10,-1,4,4,-5,7,-1,-5,-4,1,3,5,-7,3],[-8,8,1,-7,-3,6,-3,8,-1,-7,1,8,4,-6,-4,5,-10,-10,-2,10,7,-3,-1,2,-7,-9,-7,-4,8,-3,9,-4,9,-3,-10,6,3,6,4,7,9,10,3,-8,-2,-3,7,3,9,8,-1,7,-8,9,2,-1,-10,-8,3,-3,-7,9,2],[-1,-9,2,-7,-5,5,5,8,10,-9,2,-4,-8,-1,-6,-8,-8,10,-9,1,2,-8,3,6,-5,-2,4,3,-1,-10,9,-6,7,7,4,9,-5,-4,-2,-4,3,5,-5,3,5,3,-1,1,6,1,-9,8,7,4,2,6,7,-7,10,-8,-3,-8,-3],[-10,8,-9,-4,-3,-8,-10,-7,8,-8,6,-4,2,7,-2,1,-9,5,-8,-6,-2,5,7,-6,6,1,-1,-8,2,5,8,-8,-4,7,-4,10,9,5,9,-2,-9,-9,-10,5,4,6,5,9,6,9,8,5,-7,7,6,-3,4,5,-8,-6,10,2,-7],[-5,6,-5,5,6,-4,10,-2,-5,2,10,2,-2,-9,10,-7,1,10,2,7,9,-8,-1,1,-9,-8,5,-5,6,3,-2,-2,-6,10,-8,-5,-8,10,-5,5,-6,-1,7,-9,-1,-9,-5,-7,-1,-10,-4,10,7,-1,-10,4,-3,10,2,3,4,-8,10],[1,-4,4,5,4,-5,2,-3,-5,1,8,-5,-7,-10,-9,4,-6,10,-10,8,-4,-9,10,1,10,-1,5,7,4,-9,-2,2,1,9,-6,5,2,6,-6,7,1,4,5,-10,-1,-3,-1,-2,-6,4,-10,4,1,-1,-1,2,-10,9,-8,-4,7,-3,-2],[-1,-5,-2,5,4,10,-4,-8,4,-3,-1,4,-9,3,-1,6,-3,6,6,3,-9,7,-5,-8,-3,4,1,1,2,1,-9,5,7,-7,-5,1,5,-5,-5,9,-3,1,-4,-3,6,-10,-2,7,6,-10,-6,3,1,2,-1,3,6,10,-8,-8,9,-7,3],[-8,-10,10,-1,7,-2,-9,2,9,-8,9,1,10,7,9,-3,-9,-7,-7,3,-2,5,-10,-5,-6,-7,1,-6,6,-10,1,5,-4,-10,-3,-7,10,8,2,8,-8,-4,-2,2,4,-4,3,5,-4,-10,-8,1,10,9,-5,-9,1,-4,6,1,-7,-4,-6],[10,4,4,9,-1,5,1,6,-4,7,-9,3,-2,-5,-5,-5,-1,-6,-2,-10,-2,-2,6,-4,4,8,4,-3,6,-5,1,5,-1,-6,-4,6,5,10,6,2,7,5,-3,-10,-8,-9,4,-2,-5,-8,7,6,3,-5,-3,-1,9,2,4,-1,6,3,4]], dtype = "int8")#candidate|7323|(10, 63)|const|int8
call_7322 = relay.TupleGetItem(func_1283_call(relay.reshape(const_7323.astype('int8'), [9, 7, 10]), relay.reshape(const_7323.astype('int8'), [9, 7, 10]), ), 0)
call_7324 = relay.TupleGetItem(func_1286_call(relay.reshape(const_7323.astype('int8'), [9, 7, 10]), relay.reshape(const_7323.astype('int8'), [9, 7, 10]), ), 0)
output = relay.Tuple([bop_7319,call_7322,const_7323,])
output2 = relay.Tuple([bop_7319,call_7324,const_7323,])
func_7327 = relay.Function([var_7317,], output)
mod['func_7327'] = func_7327
mod = relay.transform.InferType()(mod)
var_7328 = relay.var("var_7328", dtype = "int64", shape = (4, 1, 2))#candidate|7328|(4, 1, 2)|var|int64
output = func_7327(var_7328)
func_7329 = relay.Function([var_7328], output)
mutated_mod['func_7329'] = func_7329
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7420 = relay.var("var_7420", dtype = "uint16", shape = (12, 1, 16))#candidate|7420|(12, 1, 16)|var|uint16
var_7421 = relay.var("var_7421", dtype = "uint16", shape = (12, 9, 16))#candidate|7421|(12, 9, 16)|var|uint16
bop_7422 = relay.greater_equal(var_7420.astype('bool'), var_7421.astype('bool')) # shape=(12, 9, 16)
output = relay.Tuple([bop_7422,])
output2 = relay.Tuple([bop_7422,])
func_7434 = relay.Function([var_7420,var_7421,], output)
mod['func_7434'] = func_7434
mod = relay.transform.InferType()(mod)
mutated_mod['func_7434'] = func_7434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7434_call = mutated_mod.get_global_var('func_7434')
var_7436 = relay.var("var_7436", dtype = "uint16", shape = (12, 1, 16))#candidate|7436|(12, 1, 16)|var|uint16
var_7437 = relay.var("var_7437", dtype = "uint16", shape = (12, 9, 16))#candidate|7437|(12, 9, 16)|var|uint16
call_7435 = func_7434_call(var_7436,var_7437,)
output = call_7435
func_7438 = relay.Function([var_7436,var_7437,], output)
mutated_mod['func_7438'] = func_7438
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7561 = relay.var("var_7561", dtype = "uint8", shape = (2, 9, 10))#candidate|7561|(2, 9, 10)|var|uint8
const_7562 = relay.const([[[3,7,10,-4,8,9,-4,7,-8,-5],[7,4,6,6,6,-1,-10,1,-6,3],[2,2,-3,-9,4,-10,2,6,5,-1],[-7,-3,9,-5,6,8,1,4,-1,-5],[-7,-3,-8,-6,2,-7,8,-6,-2,3],[-8,-6,3,3,4,-8,-4,9,3,-6],[-5,-3,-10,1,9,-2,6,-8,-9,-4],[10,4,-4,-7,-10,-1,-7,-9,5,-1],[-3,3,-10,-10,-3,-1,-6,-8,-10,7]],[[-9,5,7,3,4,-8,6,8,-4,4],[-5,-10,-2,1,-5,-1,9,10,-10,7],[6,2,-9,-7,-3,10,-8,6,1,1],[8,-10,-10,4,-3,5,-8,-1,-1,2],[1,-9,4,-8,-7,-1,-3,-3,-3,-2],[-1,6,-5,-6,5,-10,10,5,9,1],[4,-10,-4,9,-1,4,9,-1,6,3],[-5,-10,-6,-1,8,-8,5,-1,-10,-6],[1,-3,1,7,1,-1,-4,-5,3,5]]], dtype = "uint8")#candidate|7562|(2, 9, 10)|const|uint8
bop_7563 = relay.subtract(var_7561.astype('uint8'), relay.reshape(const_7562.astype('uint8'), relay.shape_of(var_7561))) # shape=(2, 9, 10)
func_1128_call = mod.get_global_var('func_1128')
func_1130_call = mutated_mod.get_global_var('func_1130')
const_7568 = relay.const([-10,8,8,3,7,3,-1,-10,7,5,6,-2,-4,2,-8,-8,4,2,-5,7,-5,9,-3,5,9,-4,7,-5,-2,-10,8,1,-3,5,-5,1,3,6,-7,8,2,-2,-7,-9,-7,-1,9,6,4,10,-4,-1,-1,6,9,-5,-3,9,5,9,9,7,-2,9,-4,7,-2,-6,-5,-10,-6,5,-5,9,4,-3,8,10,1,-7,-10,5,-5,4,5,4,10,-9,6,6,8,3,-9,7,4,-7,10,-6,-2,7,-4,-9,2,1,5,-6,-7,8,-3,8,-1,-2,6,10,-6,-5,7,7,1,-5,-5,1,1,-8,6,-10,10,10,9,3,-6,-8,-4,2,4,4,-10,1,-4,-6,6,7,-9,1,-8,7,-3,-7,-1,4,8,-5,3,-2,7,-5,-5,9,3,3,-2,-5,5,-4,5,-2,-6,-3,-2,-5,-2,-10,-5,10,8,-9,-2,-7,-10,-3,-9,-6,-1,3,6,10,8,-7,-10,-1,10,9,6,-1,5,9,-9,8,-6,3,6,-9,3,7,3,-2,-8,9,4,-8,3,4,2,4,-2,-1,-10,3,8,-9,-6,6,-1,-5,4,-8,1,-1,-4,5,3,6,-6,-7,9,-7,-6,-8,-5,-5,-10,-6,-5,-6,-3,6,-6,-7,1,9,9,-4,7,5,-9,-3,-3,10,7,8,-6,5,-7,4,-8,8,9,6,6,-9,10,-1,-2,-1,-6,8,5,4,8,2,3,5,3,-9,1,-3,-2,3,5,1,-5,3,-4,2,7,8,-3,1,2,-3,9,-3,-2,3,2,-1,6,-5,-3,10,10,-1,9,-6,-3,4,-7,-1,3,8,-1,-2,-5,5,5,-9,3,7,1,5,-4,-5,5,-2,1,6,7,7,7,1,9,-9,7,6,-9,3,9,-6,6,-7,-8,-9,10,-8,-7,-1,8,-9,-5,-4,-6,-10,4,3,6,7,10,-2,1,1,8,6,-3,-10,2,3,-2,6,2,6,-7,3,-10,-10,-4,10,-5,9,-5,-6,-4,6,-3,2,2,-3,-4,6,1,4], dtype = "uint8")#candidate|7568|(400,)|const|uint8
call_7567 = func_1128_call(relay.reshape(const_7568.astype('uint8'), [10, 5, 8]))
call_7569 = func_1128_call(relay.reshape(const_7568.astype('uint8'), [10, 5, 8]))
func_2670_call = mod.get_global_var('func_2670')
func_2674_call = mutated_mod.get_global_var('func_2674')
var_7574 = relay.var("var_7574", dtype = "float64", shape = (280,))#candidate|7574|(280,)|var|float64
call_7573 = relay.TupleGetItem(func_2670_call(relay.reshape(var_7574.astype('float64'), [7, 10, 4]), relay.reshape(var_7574.astype('float64'), [7, 10, 4]), relay.reshape(const_7568.astype('uint8'), [400,]), ), 4)
call_7575 = relay.TupleGetItem(func_2674_call(relay.reshape(var_7574.astype('float64'), [7, 10, 4]), relay.reshape(var_7574.astype('float64'), [7, 10, 4]), relay.reshape(const_7568.astype('uint8'), [400,]), ), 4)
output = relay.Tuple([bop_7563,call_7567,const_7568,call_7573,var_7574,])
output2 = relay.Tuple([bop_7563,call_7569,const_7568,call_7575,var_7574,])
func_7592 = relay.Function([var_7561,var_7574,], output)
mod['func_7592'] = func_7592
mod = relay.transform.InferType()(mod)
mutated_mod['func_7592'] = func_7592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7592_call = mutated_mod.get_global_var('func_7592')
var_7594 = relay.var("var_7594", dtype = "uint8", shape = (2, 9, 10))#candidate|7594|(2, 9, 10)|var|uint8
var_7595 = relay.var("var_7595", dtype = "float64", shape = (280,))#candidate|7595|(280,)|var|float64
call_7593 = func_7592_call(var_7594,var_7595,)
output = call_7593
func_7596 = relay.Function([var_7594,var_7595,], output)
mutated_mod['func_7596'] = func_7596
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7788 = relay.var("var_7788", dtype = "float64", shape = (7, 13, 3))#candidate|7788|(7, 13, 3)|var|float64
uop_7789 = relay.sin(var_7788.astype('float64')) # shape=(7, 13, 3)
func_4654_call = mod.get_global_var('func_4654')
func_4656_call = mutated_mod.get_global_var('func_4656')
const_7805 = relay.const([-0.730646,4.193536,-0.479264,8.905239,7.856753,5.858973,-0.737761,1.450619,8.566363,1.113218,5.687228,6.219786,8.412044,2.253912,6.150083,-4.026847,4.014877,1.103117,3.405924,-0.275514,4.723293,-1.285701,-8.104486,-7.825023,-1.017907,-3.772774,-3.411260,5.234859,8.117446,-9.681073,5.727058,8.692742,-3.606345,-0.686921,8.099708,-8.143350,-0.790626,9.427166,1.011972,-0.747628,4.435271,5.753608,2.439655,1.630462,6.119826,6.962876,-9.329114,-2.512017,-2.245752,-2.057667,4.358330,-7.746287,1.154478,-5.074870,1.301759,8.356760,-7.714985,-7.956585,5.625546,-6.293226,-5.122777,6.041497,-5.941612,1.456375,-9.122031,1.853490], dtype = "float32")#candidate|7805|(66,)|const|float32
call_7804 = func_4654_call(relay.reshape(const_7805.astype('float32'), [1, 11, 6]))
call_7806 = func_4654_call(relay.reshape(const_7805.astype('float32'), [1, 11, 6]))
output = relay.Tuple([uop_7789,call_7804,const_7805,])
output2 = relay.Tuple([uop_7789,call_7806,const_7805,])
func_7809 = relay.Function([var_7788,], output)
mod['func_7809'] = func_7809
mod = relay.transform.InferType()(mod)
var_7810 = relay.var("var_7810", dtype = "float64", shape = (7, 13, 3))#candidate|7810|(7, 13, 3)|var|float64
output = func_7809(var_7810)
func_7811 = relay.Function([var_7810], output)
mutated_mod['func_7811'] = func_7811
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8721 = relay.var("var_8721", dtype = "int32", shape = (16, 12, 6))#candidate|8721|(16, 12, 6)|var|int32
var_8722 = relay.var("var_8722", dtype = "int32", shape = (16, 12, 6))#candidate|8722|(16, 12, 6)|var|int32
bop_8723 = relay.less(var_8721.astype('bool'), relay.reshape(var_8722.astype('bool'), relay.shape_of(var_8721))) # shape=(16, 12, 6)
func_4833_call = mod.get_global_var('func_4833')
func_4837_call = mutated_mod.get_global_var('func_4837')
const_8741 = relay.const([-9,10,7,-3,-9,2,6,1,-9,-5,9,-10,-6,2,-9,4,7,1,-7,4,5,-5,-9,-8,-3,5,2,-4,10,-6,-10,-8,-6,2,3,9,-1,-1,-5,9,2,7,-9,-4,-7,-9,-1,-6,6,-10,4,-7,6,-5,8,8,-10,-6,7,8,-10,-3,-4,8,6,8,-7,-5,6,-7,-6,6,1,-4,4,4,-1,-5,-5,8,8,9,3,-2], dtype = "int8")#candidate|8741|(84,)|const|int8
var_8742 = relay.var("var_8742", dtype = "int8", shape = (168,))#candidate|8742|(168,)|var|int8
call_8740 = func_4833_call(relay.reshape(const_8741.astype('int8'), [1, 6, 14]), relay.reshape(var_8742.astype('int8'), [2, 6, 14]), )
call_8743 = func_4833_call(relay.reshape(const_8741.astype('int8'), [1, 6, 14]), relay.reshape(var_8742.astype('int8'), [2, 6, 14]), )
output = relay.Tuple([bop_8723,call_8740,const_8741,var_8742,])
output2 = relay.Tuple([bop_8723,call_8743,const_8741,var_8742,])
func_8750 = relay.Function([var_8721,var_8722,var_8742,], output)
mod['func_8750'] = func_8750
mod = relay.transform.InferType()(mod)
mutated_mod['func_8750'] = func_8750
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8750_call = mutated_mod.get_global_var('func_8750')
var_8752 = relay.var("var_8752", dtype = "int32", shape = (16, 12, 6))#candidate|8752|(16, 12, 6)|var|int32
var_8753 = relay.var("var_8753", dtype = "int32", shape = (16, 12, 6))#candidate|8753|(16, 12, 6)|var|int32
var_8754 = relay.var("var_8754", dtype = "int8", shape = (168,))#candidate|8754|(168,)|var|int8
call_8751 = func_8750_call(var_8752,var_8753,var_8754,)
output = call_8751
func_8755 = relay.Function([var_8752,var_8753,var_8754,], output)
mutated_mod['func_8755'] = func_8755
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8828 = relay.const([[[1],[-7]],[[8],[7]],[[-9],[3]],[[8],[3]],[[-9],[4]],[[-4],[6]],[[3],[4]],[[-3],[1]],[[10],[4]],[[-8],[-2]],[[-3],[1]],[[3],[3]],[[-9],[-5]],[[3],[10]],[[1],[7]]], dtype = "uint64")#candidate|8828|(15, 2, 1)|const|uint64
var_8829 = relay.var("var_8829", dtype = "uint64", shape = (15, 2, 16))#candidate|8829|(15, 2, 16)|var|uint64
bop_8830 = relay.greater(const_8828.astype('bool'), var_8829.astype('bool')) # shape=(15, 2, 16)
func_5735_call = mod.get_global_var('func_5735')
func_5738_call = mutated_mod.get_global_var('func_5738')
const_8835 = relay.const([6.193498,7.961610,4.920597,9.124924,9.757960,2.803587,2.373185,9.423696,-7.977755,6.395380,-4.221004,-6.058790,9.723523,7.805591,-5.219227,-0.268986,0.450125,-9.142064,-4.576308,5.085875,6.849620,3.235663,-1.886807,1.621106,2.781147,2.125061,7.386334,-3.438247,-5.177566,5.238844,-1.346377,-3.459229,9.245123,-2.955202,-3.776722,-5.691020,-9.506573,-0.493985,-2.618943,0.199604,-7.884801,-9.069459,-5.037271,4.118758,-7.419964,2.181876,-4.854041,1.454863,6.882694,1.880329,0.625724,2.961801,9.472977,-1.638053,0.657082,3.035561,-3.833240,-4.498146,9.310500,5.669866,-1.915855,-2.938312,-5.642113,6.433984,-0.062708,4.535384,-2.999898,4.507277,-4.090812,8.847706,-2.965271,-5.116153,-3.329958,6.943174,-2.474526,-5.391746,-6.384157,7.969352,-5.768986,-0.753526,1.909801,-8.769350,-6.054691,-0.377052,9.114987,0.550818,-2.136377,-0.965708,-5.814567,-3.678188,4.291423,4.213166,-2.610422,-5.685290,8.108378,9.683602,8.811714,-6.308127,4.388665,-5.543595,1.306067,-4.925476,2.249164,-6.035681,3.664184,-2.377236,6.911975,-8.538960,-4.750250,-6.991251,3.346450,5.158944,0.902569,-3.071189,-2.040924,5.309255,-7.075530,7.953326,4.380258,9.209959,4.522012,2.477926,-3.571277,-2.105703,-6.757609,-1.945438,-0.303517,-2.319409,-8.597440,-1.015916,-0.185956,-0.424574,-5.275850,-5.251435,0.857932,-7.756441,-1.120492,-8.708079,6.569644,9.621147,1.166561,4.642356,5.739611,-0.491936,-7.799672,-6.745573,-6.343489,-6.841155,3.151229,-2.249868,-3.877099,3.623559,-9.612886,0.084505,-9.794052,-7.896042,6.677196,4.960339,7.588174,-4.091154,-3.728871,-7.691815,2.654711,9.609195,-2.457420,6.514122,-8.654158,2.394479,-2.582881,-8.927492,0.447095,6.535657,-0.763386,-7.434205,-1.850377,-7.943080,8.057479,4.834562,5.257605,3.257749,3.617924,-7.432547,1.168566,-6.971054,2.736815,-7.179100,7.388657,0.574145,-1.729825,-6.882024,-4.400151,-3.493114,6.344419,-2.807287,-8.689085,-0.377639,-3.797822,-4.212925,-4.768135,-6.403814,0.621292,7.575028,-8.616266,6.289605,-0.191974,0.637411,-2.351810,-0.546861,2.036961,-4.017782,4.107452,0.630383,1.025917,8.345993,5.408656,2.156759,6.598984,8.370866,2.155123,-6.706572,-9.772782,-6.941347,6.821026,5.875059,0.886282,4.471288,-0.473765,1.775348,-1.888830,-0.652752,-4.237979,-3.240976,-4.586126,5.655683,-9.143631,5.093040,7.357279,9.740317,-5.163062,2.337805,-3.709487,-0.878119,-3.527939,1.810936,4.844041,-4.111617,4.295025,3.135338,-5.118817,-2.582694,-3.696139,-5.931325,4.898270,8.642598,-6.078318,-5.570618,7.508775,8.334921,-6.299077,-4.055972,-9.837191,2.943322,2.092990,9.844275,2.197772,4.250119,5.721138,7.506076,6.197368,6.253101,3.448812,8.751635,-5.090401,-3.219121,4.359497,-0.984036,0.117974,9.126699,-1.763745,9.703978,-5.878371,-6.346830,-3.382468,5.985979,-5.138803,2.505269,-1.265217,-3.015086,3.733166,4.210255,3.365976,3.443313,9.627477,4.736225,3.076343,8.719299,2.014622,-9.940442,4.857727,-7.080195,-3.386063,9.212594,-6.603189,6.859966,3.411971,-7.463680,6.871983,2.363561,-6.775137,-0.663560,3.647883,-5.244976,6.602261,-2.291441,-0.057931,-4.060869,-6.987932,7.334885,6.733196,1.897553,5.997844,9.637967,7.935132,6.434952,-9.387039,6.346548,8.849107,-6.277798,-2.826997,0.154020,3.493208,7.630637,1.181255,-9.155936,-5.638234,5.325504,9.240716,-6.263848,-7.136327,4.168241,8.625881,-3.439111,-1.031302,-3.377928,-0.536705,8.130999,3.288833,5.577158,6.055113,-2.850317,0.631456,7.523785,-6.369877,7.068738,1.150210,8.592064,-3.657572,2.765617,1.876652,9.664290,0.382275,5.341662,-0.187567,4.122318,3.130430,5.524935,-2.058659,7.567972,-4.960266,3.241617,8.064253,-0.859734,-7.698929,-7.388913,0.892214,8.504744,-9.624556,-7.502295,-5.001871,-1.583590,9.791810,-3.871290,-5.075267,-2.315973,1.395389,-6.778449,2.643709,-8.726822,-7.990182,9.572940,-4.898272,-7.839081,9.482402,3.537079,3.437233,5.909381,4.629990,-8.060262,-4.829309,-5.441349,-1.375577,-2.218064,-8.896510,3.847135,-2.744883,-3.123329,-5.094236,1.767939,4.684974,9.749233,4.903786,5.494901,-4.940728,-9.770080,4.937526,-0.559604,-9.027482,6.052740,4.981666,1.860887,7.849888,0.381981,7.682360,1.047953,8.982248,6.492112,-8.254404,-7.703843,-3.176592,4.861335,8.467128,0.174331,-3.664575,-4.753085,0.325202,7.689672,-8.737462,-0.645595,-1.781016,-3.811213,-6.615826,-4.815188,2.915650,-0.912284,9.626767,6.743188,5.078001,-7.670994,7.986588,-0.876912,9.730465,8.737930,-7.337781,1.796905,2.344251,-3.674427,9.562530,-2.850036,6.084985,-0.255286,-8.206497,-1.429842,-4.292373,-8.472915,0.627888,-8.953759,-3.076120,-2.386300,-2.951393,4.940878,-5.010479,7.706963,-2.320836,-7.518971,-7.210841,3.346813,-2.487794,3.544916,-1.855539,-7.933131,-2.263546,-4.409883,-7.305549,9.371485,-9.989997,-4.885999,-4.684589,-9.928242,-9.807244,9.930015,7.548532,7.441604,-8.299842,-9.433469,-6.048873,-2.120497,-5.014674,-0.483068,-9.463246,3.267386,-8.659010,2.839627,6.918788,-4.482312,-4.732618,8.396031,-3.867227,4.915545,5.022588,3.011330,-8.663013,-8.986714,3.117589,6.794460,-1.677424,-0.583537,-2.204057,5.812982,-3.569603,0.456975,8.928322,-2.857530,-9.454933,-9.523482,-4.638049,4.719995,-6.173140,4.887130,-4.327599,3.569601,7.032615,-1.268461,2.127891,0.232621,2.954393,-4.365374,0.663757,-8.907888,-0.639727,9.269702,-2.562642,3.200186,-2.681239,-1.060464,4.090066,5.072787,-7.994362,-1.529143,-9.354575,4.882690,0.021945,-4.902188,-0.506381,-0.691236,-9.208157,8.520180,-2.495721,4.780337,9.211803,-9.546550,4.272222,0.739824,1.788350,9.398633,-9.172154,2.180272,-1.682102,-3.154564,-9.790709,5.183617,2.040830,1.978835,4.615814,-1.855319,7.080213,6.426803,6.906621,-9.209896,-6.837520,-1.688792,-9.101845,-2.395832,6.777954,2.517932,1.594100,-3.773195,-4.574263,6.355470,-2.824552,-6.315647,-0.812026,-9.258057,7.999215,-2.992680,-5.403960,-2.580227,-3.000074,6.023187,0.450206,0.677671,7.323434,3.483636,0.452916,1.603060,2.325065,8.167721,6.186252,3.545776,-3.362432,9.955808,-0.705814,2.708588,-1.182801,-0.179311,-2.189319,2.273958,-3.351252,9.962278,7.229876,9.375334,-8.967995,-1.219624,6.573874,-2.117119,6.219094,-5.240770,0.116575,-5.061159,5.225657,-3.096246,-6.313159,2.929767,-5.153744,-7.974335,-0.411560,-2.549285,5.342688,-3.529998,-0.342731,-3.660480,-6.569050,2.398131,6.304632,-9.755946,1.604167,-2.770430,-8.062679,-2.728804,-5.812529,-7.060335,-2.693742,4.952917,5.750944,-2.833370,7.847885,3.153536,-7.781815,2.552477,-7.573771,-5.823389,-3.414005,2.645818,-1.761215,-7.044887,-3.499089,8.966133,2.762834,-7.468772,8.581838,3.195012,-3.990581,-8.255458,8.254401,-9.284048,5.601835,8.213212,6.401287,-1.080728,-8.929348,-4.441938,9.565289,-9.887539,-2.090158,7.465800,5.766822,-8.753017,7.327173,-8.500853,7.251774,-7.350512,1.370465,-7.037806,-5.818169,0.782647,1.825854,-9.797169,5.165993,-5.715418,9.029641,2.758802,-3.770874,-5.370457,7.027365,-5.303587,8.440926,1.128861,3.067815,4.039003,6.618180,-9.926996,-1.324314,2.890335,8.759968,-1.331917,-7.756113,-7.227358,9.328265,-5.403618,7.935968,0.702673,-7.452379,-5.900321,8.815619,8.673611,-5.476269,6.438066,-4.266998,-0.706094,-9.501467,4.654932,3.100595,4.663992,-6.640162,9.652643,4.476139,8.707246,3.118924,5.578865,1.857917,1.101507,-3.620231,2.124241,-8.792524,5.288599,-0.936707,2.121156,-7.880589,-8.789278,-4.377093,-4.297766,5.373888,4.201764,0.524959,7.445796,-8.669963,-7.306991,5.551138,0.474073,-4.309529,8.525363,4.573131,-7.768520,7.657075,0.687197,-7.914443,6.827699,8.022839,-5.667815,1.037218,2.594072,4.042489,6.147522,3.028846,-2.955589,9.310008,-3.634346,-2.999561,-2.554409,-9.193902,0.477859,9.223861,-3.903587,-4.683886,-5.502018,-5.295685,9.537072,6.710059,-2.716331,5.869179,-8.546582,-8.530293,-6.216695,1.932593,7.036631,-4.818531,-6.629263,9.882128,-3.394026,-0.906386,-2.226444,-5.758190,-1.301614,-8.403810,2.969911,8.214339,-8.995802,-7.378357,-9.704856,5.668001,3.071406,-7.950753,4.159071,-3.477365,1.368436,-8.823798,7.221495,1.297353,4.712137,0.595726,-3.925383,-7.951338,-8.539302,7.254863,0.837150,-5.575332,-1.156876,-8.197715,1.677956,5.207057,3.772330,-9.791226,-0.644096,-5.616362,1.928083,-8.278946,-2.137694,-9.427653,-1.051253,9.292165,-2.450643,-0.676016,3.791788,-4.788315,-1.629164,4.684682,-3.873397,-2.464736,-2.949485,-4.793614,-5.192853,3.455949,2.755388,-1.094174,7.885146,8.482352,6.156786,-8.397034,7.979993,9.921217,-6.881879,9.871986,-0.024513,2.629834,9.109893,-8.282046,9.024877,-0.618522,8.669735,-3.845802,4.404443,-4.178560,9.473400,7.329594,-1.081597,-6.255693,8.332977,6.738532,-3.101751,-3.982042,-5.631640,6.338983,-3.075782,-7.794721,-7.356140,-7.515232,1.331672,7.175974,8.910418,3.734913,2.175793,-3.862290,5.494796,3.489527,4.189686,7.138934,-2.727272,3.950614,7.145243,1.692992,-0.108941,3.478233,-1.727973,-4.536135,9.901854,1.197920,-6.903461,1.650493,7.817605,0.682218,4.578350,-3.499438,3.393256,-9.246855,-8.104954,5.451531,-6.393251,-1.482158,7.173714,-4.245102,-9.675089,5.321825,-1.588811,-4.514709,8.772025,-6.820883,6.224466,6.782412,-9.433975,8.315823,5.139369,8.181694,4.347024,-7.651422,-7.296341,9.886749,0.520649,2.572793,2.824659,7.912305,5.284029,8.826262,1.795846,-2.670084,0.099708,-5.484240,-3.390504,-4.415731,5.067782,-5.593159,5.170933,-4.857295,-9.075944,-7.434926,4.475496,7.669801,5.496766,3.472835,7.565254,-5.235305,5.218840,1.363829,-4.124236,5.076021,-9.818891,-2.303680,3.118085,-8.576608,-8.550147,-3.915731,6.835207,3.972100,-1.665225,4.376257,-9.309844,-0.285508,-0.933479,7.664033,0.399483,-4.827354,-8.163576,-8.935212,1.899149,9.458832,7.840861,9.357148,7.468455,-0.600329,-9.318006,3.465522,9.836480,-6.665920,5.522470,5.350210,8.955659,1.540459,-6.398503,7.948665,-2.725571,8.875689,-9.819827,-3.414061,9.697217,-4.995428,-2.227441,-4.987519,5.118253,6.369154,-8.624564,-0.633469,-4.496351,2.118309,2.131268,-3.301700,-7.249963,3.870752,4.295344,-6.741083,-3.371256,-9.784234,8.308143,1.160979,6.451765,5.000321,0.235811,3.762715,9.621332,-8.729179,-4.163330,1.833053,-9.833465,2.190510,-5.607517,9.826536,-8.964229,-9.650816,-8.570898,7.954103,-7.605855,-8.314614,-5.631765,-5.356419,-4.535361,-5.758590,9.757689,5.991079,-1.655638,9.033652,8.592859,-2.964084,-9.992786,6.000588,-6.587721,7.790773,0.352120,-8.564488,7.591310,-9.202644,7.282740,-1.174959,-5.850565,-6.630582,7.727390,3.240647,-5.104981,-1.141498,-0.648692,-3.884812,-3.484459,-5.999679,8.643271,2.863796,3.608527,-5.004334,-6.644579,9.184321,3.654662,-1.471914,-9.211053,1.632520,6.767091,0.841531,7.916479,-8.307615,2.239135,9.909146,3.528822,-7.490487,-1.575350,1.155378,4.507222,6.582319,-5.549908,4.706297,-1.835609,-2.164713,5.828269,8.459684,0.472668,-7.324106,-0.935046,6.853990,3.930767,-8.063551,-0.120164,-5.134329,0.819815,-7.289250,0.374197,-6.504600,-6.471968,8.765511,-3.037783,-7.426844,-5.761610,4.299022,9.224640,-8.229884,-1.921225,-0.891023,-5.058899,-1.436739,5.284185,-9.680443,6.866283,-1.258665,7.061417,4.666176,-5.184125,4.431985,-4.247237,-8.485492,8.372194,-3.148127,8.664642,-9.214844,-1.377828,7.496483,-0.352290,-9.986572,-4.830007,6.352240,6.052224,-9.624732,4.601016,-2.322568,-6.530369,2.947448,-8.120560,0.473729,-6.992965,8.139930,-6.342819,-3.903213,-5.304620,-5.404541,0.705456,-9.751438,-2.762714,6.142820,-5.442689,-8.340096,-5.020563,-9.111038,9.183607,-8.029080,-7.716629,-1.470719,0.550255,7.888691,-2.477333,-1.966963,5.478114,-1.575749,3.744862,9.193990,9.185457,-5.277070,6.864065,-4.837138,-8.569714,1.477292,4.320182,-6.645226,-3.190248,-3.691788,8.740726,1.271218,-1.013649,4.175465,2.940177,4.900205,-3.761664,-4.236424,8.143951,-7.476359,1.935415,-7.646759,-3.762219,9.641890,-6.061392,8.255515,5.414031,-1.699198,-4.106796,3.019203,4.887827,-3.420686,1.148209,0.452600,-8.448603,-1.641311,4.120319,-0.231535,2.005048,3.052888,5.146459,-0.144201,5.600567,-1.901181,-7.302869,4.620326,3.367730,7.188202,-8.845617,1.695995,-9.218276,-0.582612,-2.702456,6.650366,3.835059,1.968904,3.410011,7.686492,-6.465898,-7.736698,0.605764,-4.757427,-7.431490,0.812451,4.957449,7.206920,8.824516,8.910325,-7.313883,3.615892,7.895985,-2.995275,-9.835803,5.692080,-2.922035,2.961516,5.851290,-4.051793,8.588460,-4.131865,-6.696846,0.593532,-5.074095,3.694436,0.746852,-9.379390,0.996365,-8.858300,-3.573897,-5.043058,4.346900,-5.747635,-9.999950,-2.824389,7.727370,-9.597904,-4.364459,4.952890,-6.353736,3.599752,3.502060,6.658648,3.929359,7.763725,7.983340,-3.107114,6.957966,-3.835487,7.142110,-2.944383,8.586102,-8.704512,-9.972292,-0.534233,-7.409900,-2.154644,6.436563,-3.484505,6.216171,-3.546519,7.611102,-5.113886,-2.929421,-7.809303,5.956464,-8.645367,2.446977,0.744142,-9.807782,9.638147,6.309718,-6.205851,6.616720,2.062129,-9.530507,1.569889,-0.140228,6.942874,-3.975466,-9.064601,-7.570675,5.812069,3.534554,8.921688,-0.293613,-1.270029,-1.624505,4.554125,2.567563,8.291316,-1.855895,-1.044866,-0.598760,4.142246,2.411108,-6.597757,-8.613602,-6.145926,-2.146286,0.096498,-3.394364,1.957288,0.147513,-1.258867,7.414818,-1.127315,-1.111726,6.456958,-6.193742,-3.877752,-3.037868,8.206132,-9.837362,5.128760,0.639567,3.132241,-5.085867,3.300042,3.079879,7.392833,0.395309,0.332953,-8.248312,-7.635240,4.262751,-6.975087,5.609840,2.319322,7.080148,1.176621,6.220839,-2.460094,4.818707,1.010841,4.962005,4.032458,6.659314,9.878584,0.453711,-7.531965,-3.226564,5.355796,7.083307,3.148930,3.507802,3.010324,4.767487,-2.003665,9.465367,-0.306897,-3.425882,8.045158,-1.777235,1.232958,-1.792401,-1.366724,7.690208,0.975772,-1.157501,9.743959,6.630340,6.740831,4.690487,0.851895,0.975766,3.132421,2.750000,9.814647,5.866770,-9.190994,0.389946,-4.508637,-3.148529,1.727112,-4.217930,-4.846030,2.029075,9.471892,3.737396,-9.105432,-6.549930,6.161545,-4.791128,9.047706,2.348612,-3.707737,-9.609574,1.228969,-4.101584,-8.165812,-6.097404,-1.457944,-4.966409,-3.842582,-5.275204,-5.820746,-5.691153,-6.121104,0.775598,3.030160,8.481443,0.223087,-8.910946,-3.566521,8.525088,-2.387572,6.148076,6.781022,-9.835397,-0.779304,-6.214605,8.720752,-5.964977,-8.500820,2.982948,-0.103911,1.418494,-1.705822,6.513879,-0.805144,2.429724,-9.185790,4.894779,-9.877694,2.843304,-4.564815,-9.765385,-1.675909,7.844620,-3.862420,-7.878095,-0.162634,-6.535246,-9.537768,2.119074,-7.274857,5.564544,-8.131077,-3.597482,-1.833373,7.041409,-4.479797,-3.218135,-7.692285,3.935633,-7.856043,9.543529,3.913130,0.893066,9.827511,-3.174846,-9.874543,-2.520201,-6.709819,5.769812,-8.734732,9.190222,-8.888067,-7.064169,1.485093,2.591228,7.540792,-8.183938,-4.053712,-8.979186,7.189870,3.240604,-0.878815,-4.124203,4.574052,7.100978,-2.139706,-7.947454,-3.506599,9.734777,-2.814773,1.079791,0.707078,-8.261609,-4.880575,-9.970307,1.326686,1.522356,4.911975,-3.754257,2.201140,6.499459,-0.396623,8.956987,-1.481678,-7.209577,7.184203,-5.341773,-0.319703,0.225438,-3.358882,-8.440134,7.436455,3.216839,2.969835,7.680588,-6.215413,-4.284402,-0.535885,3.173260,-4.851125,1.703687,-7.438025,-8.389564,-4.821116,2.952707,9.769229,-4.567197,5.977137,-9.985563,8.613423,9.189383,-1.655036,-0.350241,1.036602,8.481402,-3.418403,-1.978445,-7.218008,0.043426,-5.984890,9.974831,-5.288575,-6.697134,-2.229962,-0.499721,5.471764,8.253084,7.169500,-5.734197,7.202956,-3.998087,9.377717,-2.268981,1.750489,-2.345164,-3.125229,-3.664012,-1.772835,-5.482947,7.195282,-3.075009,3.724681,-0.373562,-0.786359,4.177096,-5.861884,9.513744,-8.922652,7.650832,4.129813,1.671295,-6.554419,-3.938710,8.337669,8.907984,9.390577,3.802196,2.150386,2.298395,-9.773876,7.324022,-8.985418,-5.786510,3.172524,-9.445693,-0.184325,-8.185815,3.918772,5.404234,-6.428843,0.882427,-2.240900,-9.711593,-5.778001,7.310611,-0.800550,8.542542,5.694251,-0.918778,-6.584173,3.501038,-4.322829,7.279015,-4.699175,-6.875948,3.296471,-1.193473,-6.298571,5.799703,-5.100568,-9.417404,3.181823,7.691207,5.835469,5.007938,6.210229,-6.376838,0.790847,0.831643,-3.363695,-3.231695,-3.258279,-7.542050,1.795620,0.908278,-0.292261,-3.968949,-3.439479,6.792977,0.994439,0.584999,1.414661,0.652398,2.874122,0.967371,-0.992554,5.692527,-2.641978,-1.032061,0.614762,-6.273811,4.978618,9.957389,-8.154265,4.730281,-4.638757,-2.198843,7.249795,-2.693805,7.396165,-4.682604,5.395646,-5.054792,9.182441,0.063191,-8.737385,1.761290,-9.895755,2.049194,9.339538,8.399369,6.240388,8.884418,2.289062,6.226737,7.085933,-1.085107,2.620148,4.162954,9.308576,4.891926,-8.775675,4.492559,-2.387924,6.629592,-1.554853,6.898959,2.221882,-4.197988,-9.763137,1.922131,2.383075,-4.427071,-6.568045,-6.057580,-7.771143,9.936237,-5.002447,1.891850,-9.692561,-0.629801,0.980277,-9.376270,-6.236229,5.216553,3.973378,8.310081,0.618824,0.504449,3.806475,9.158944,-5.608492,-0.868217,-3.536889,5.869280,-6.593707,3.660285,9.202566,-9.402117,-3.593998,-6.054633,-0.310215,-5.563017,4.431454,9.603790,8.462346,-6.902381,-7.297818,-3.813803,-6.615292,1.308766,4.811453,3.222786,-9.717304,0.275629,1.837311,-0.682663,4.062788,2.001371,4.170626,9.120910,-0.626516,-1.260844,-9.320989,9.171971,-4.014007,4.326854,1.577788,-1.191792,1.820662,-5.678357,0.787409,-0.100022,5.010287,2.086387,9.397521,-6.711605,-6.247627,-0.128794,5.507182,8.153136,-1.831666,-2.201233,9.613016,4.151762,-5.859112,-5.048784,3.971099,-8.185626,-5.570129,3.180335,-4.038733,0.575907,-1.506942,7.334351,6.130461,8.429853,3.000420,3.550942,-8.399036,0.555966,-9.473173,-3.097415,2.683889,3.281192,-6.857090,1.709235,-5.012461,6.132755,-9.270733,-3.366811,8.475881,3.633041,6.577746,-1.119123,6.398249,-5.556319,0.556005,1.758362,6.449519,-9.704249,0.410016,-6.303117,2.773008,-6.456422,-6.140513,8.481977,-2.623488,5.727795,-1.873691,6.041895,1.971562,5.158671,-8.657375,3.774792,4.945591,2.567679,2.863319,-7.702764,6.651114,-1.891832,-0.567544,-8.244119,-0.445759,-3.877689,9.580034,8.953796,-9.917167,2.115968,5.364466,-2.536022,-3.634709,-0.306050,-6.340957,-5.670798,7.539692,4.696912,9.911580,0.881032,8.548285,-4.885022,6.135619,-5.392965,-9.324496,8.127533,-0.678135,8.051201,4.897097,3.487831,-5.380829,-5.318551,-7.960900,4.962659,2.635206,-2.866009,8.295802,9.729543,-7.948139,-1.205467,3.203066,-6.001647,7.324404,-8.655425,5.495530,-0.011538,-2.393058,-3.394462,7.302984,-3.586491,-5.801248,3.719512,8.979411,-3.163293,-5.289585,-4.105738,-2.521521,-8.475439,-5.160095,1.488561,-5.933240,-5.544177,-4.324290,9.020508,-5.202732,-8.872051,-6.198593,-8.228874,-7.064610,6.626870,4.796784,-8.424391,7.876094,-9.863157,4.319964,8.512802,6.217602,-3.551886,-2.545344,0.175696,1.251085,7.560648,-5.732304,1.041789,0.161305,4.936688,3.265308,-9.512205,-8.442877,-0.009847], dtype = "float32")#candidate|8835|(1920,)|const|float32
call_8834 = func_5735_call(relay.reshape(const_8835.astype('float32'), [8, 16, 15]))
call_8836 = func_5735_call(relay.reshape(const_8835.astype('float32'), [8, 16, 15]))
func_2363_call = mod.get_global_var('func_2363')
func_2367_call = mutated_mod.get_global_var('func_2367')
var_8842 = relay.var("var_8842", dtype = "bool", shape = ())#candidate|8842|()|var|bool
var_8843 = relay.var("var_8843", dtype = "bool", shape = (22,))#candidate|8843|(22,)|var|bool
call_8841 = relay.TupleGetItem(func_2363_call(relay.reshape(var_8842.astype('bool'), []), relay.reshape(var_8843.astype('bool'), [2, 11, 1]), ), 0)
call_8844 = relay.TupleGetItem(func_2367_call(relay.reshape(var_8842.astype('bool'), []), relay.reshape(var_8843.astype('bool'), [2, 11, 1]), ), 0)
func_7327_call = mod.get_global_var('func_7327')
func_7329_call = mutated_mod.get_global_var('func_7329')
var_8852 = relay.var("var_8852", dtype = "int64", shape = (8,))#candidate|8852|(8,)|var|int64
call_8851 = relay.TupleGetItem(func_7327_call(relay.reshape(var_8852.astype('int64'), [4, 1, 2])), 2)
call_8853 = relay.TupleGetItem(func_7329_call(relay.reshape(var_8852.astype('int64'), [4, 1, 2])), 2)
output = relay.Tuple([bop_8830,call_8834,const_8835,call_8841,var_8842,var_8843,call_8851,var_8852,])
output2 = relay.Tuple([bop_8830,call_8836,const_8835,call_8844,var_8842,var_8843,call_8853,var_8852,])
func_8857 = relay.Function([var_8829,var_8842,var_8843,var_8852,], output)
mod['func_8857'] = func_8857
mod = relay.transform.InferType()(mod)
var_8858 = relay.var("var_8858", dtype = "uint64", shape = (15, 2, 16))#candidate|8858|(15, 2, 16)|var|uint64
var_8859 = relay.var("var_8859", dtype = "bool", shape = ())#candidate|8859|()|var|bool
var_8860 = relay.var("var_8860", dtype = "bool", shape = (22,))#candidate|8860|(22,)|var|bool
var_8861 = relay.var("var_8861", dtype = "int64", shape = (8,))#candidate|8861|(8,)|var|int64
output = func_8857(var_8858,var_8859,var_8860,var_8861,)
func_8862 = relay.Function([var_8858,var_8859,var_8860,var_8861,], output)
mutated_mod['func_8862'] = func_8862
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8885 = relay.const([[[-5.126495],[0.383067],[7.408903],[-9.229407],[4.222104],[-8.379629]],[[3.296061],[-3.811730],[-8.037505],[-3.213596],[-1.201079],[-3.029214]],[[-4.762065],[-4.496299],[5.934757],[3.473963],[-3.384519],[-7.437004]],[[8.136935],[2.028045],[-4.934518],[6.352862],[-5.525108],[-1.508911]],[[2.389692],[9.338291],[1.960955],[6.912944],[8.251557],[9.839241]]], dtype = "float32")#candidate|8885|(5, 6, 1)|const|float32
uop_8886 = relay.asin(const_8885.astype('float32')) # shape=(5, 6, 1)
func_5735_call = mod.get_global_var('func_5735')
func_5738_call = mutated_mod.get_global_var('func_5738')
var_8889 = relay.var("var_8889", dtype = "float32", shape = (1920,))#candidate|8889|(1920,)|var|float32
call_8888 = func_5735_call(relay.reshape(var_8889.astype('float32'), [8, 16, 15]))
call_8890 = func_5735_call(relay.reshape(var_8889.astype('float32'), [8, 16, 15]))
output = relay.Tuple([uop_8886,call_8888,var_8889,])
output2 = relay.Tuple([uop_8886,call_8890,var_8889,])
func_8904 = relay.Function([var_8889,], output)
mod['func_8904'] = func_8904
mod = relay.transform.InferType()(mod)
var_8905 = relay.var("var_8905", dtype = "float32", shape = (1920,))#candidate|8905|(1920,)|var|float32
output = func_8904(var_8905)
func_8906 = relay.Function([var_8905], output)
mutated_mod['func_8906'] = func_8906
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8976 = relay.var("var_8976", dtype = "float32", shape = ())#candidate|8976|()|var|float32
const_8977 = relay.const([[[-5.232413,-8.289019,3.137581,2.514921,1.232888,-0.530723,-0.926768,-4.742327,-4.579594,-2.657174,-8.472097,6.619529,0.088962,-4.279418,-0.655444,8.174654],[7.561918,-4.548762,-6.627008,-8.855674,-7.729740,-4.341075,8.379003,-2.918722,5.705023,-0.575916,6.372400,-7.361376,9.529300,5.826025,-0.246367,3.251323],[-3.129068,-0.597523,8.073523,5.390317,-9.984313,3.128580,-5.682827,7.186774,-2.529607,6.899245,0.547930,-8.497299,-8.542619,-8.704111,3.463633,-0.840019],[-6.191338,-2.750594,2.212270,6.803866,-2.951703,7.540691,-0.381527,-7.010979,-4.821567,9.005141,6.084924,9.133491,7.244155,-7.195185,0.571207,-7.719892],[2.985503,8.959026,-4.436449,-8.982113,9.528772,4.081921,3.019711,5.116187,2.186277,7.314984,-6.274516,-7.674013,3.213656,-8.251697,1.968635,-5.991880],[-0.158120,7.044866,-1.360063,3.779742,-6.835458,-2.479556,-5.442973,2.369344,-7.973748,-2.266375,8.922912,-5.489044,3.943893,9.723149,6.459168,6.121455],[-9.974846,7.448980,8.046110,-6.384337,1.344619,2.259722,-2.360204,-7.706186,8.586392,-7.950082,4.875868,0.660929,3.751350,-8.167903,-5.126759,-1.118639],[-8.487666,-1.637158,-7.283079,4.458073,0.933764,0.657927,-6.106919,-3.951018,-0.897094,-0.288498,7.467303,-6.615278,6.822189,7.450561,6.868658,-8.364828],[0.720532,4.623042,7.491082,-6.346920,4.646064,8.047094,9.373188,2.744892,-9.759407,2.979776,-6.831984,-0.465293,-7.586429,5.235730,-6.915259,-9.725242],[-6.621224,1.311557,-9.151992,-3.235121,-6.069182,0.476598,7.945835,6.460639,2.927137,1.860205,8.662034,1.429484,-7.507920,3.120032,-5.229060,-7.066065],[0.206078,-4.264078,3.654921,3.818174,-2.397002,0.326475,4.994423,6.568670,-6.848788,-1.976823,7.374310,6.138435,5.451257,-5.642151,-5.565873,-0.806787],[-5.520998,-4.615943,-8.756563,4.483644,-1.312906,-3.622084,-8.463365,-6.830116,9.242752,-6.979598,-5.757712,-2.133344,-1.128483,1.637823,8.416618,-5.063487],[4.940670,-0.553133,-2.072294,-0.683425,-0.233214,-1.107348,6.965293,9.932802,-5.352267,1.963179,-7.109985,-5.984615,-0.334682,9.815180,5.726352,0.129076],[-4.052315,-1.850114,-7.093312,-4.604647,-1.418739,2.437087,9.449199,-2.761097,-2.159133,3.404600,2.804103,2.934177,7.045048,3.478674,-1.488498,0.464727]],[[-8.013018,9.351931,3.629204,-4.379621,-3.571384,7.229758,-6.114246,2.703912,3.683510,7.428226,-8.756617,-9.539856,-0.647306,3.064215,-7.022540,5.804454],[-1.937553,7.773505,-6.742901,9.264536,8.592477,7.045149,-9.121069,-0.490746,3.419312,-3.890912,-0.660617,4.304404,6.621192,9.538857,-0.738780,-2.648030],[6.189289,-4.492660,7.976171,6.319078,-6.862501,0.328915,0.507745,-1.734541,6.104364,3.100638,4.945026,-2.742212,9.820799,-6.673998,7.864911,-6.101725],[5.537656,-7.069109,8.908157,5.504835,-3.786113,-8.521730,5.345779,-0.826688,-5.105229,-5.682156,0.827706,-4.719021,9.906636,-3.939817,3.087443,6.897658],[7.008079,-3.900726,2.112313,-5.849172,-9.377463,-4.025672,2.545921,-3.878014,-0.165332,2.431184,-7.467944,-4.560250,-9.124179,-2.713550,4.160323,-5.040303],[2.799903,9.835192,1.136582,7.816862,4.405705,5.360428,-2.484066,-4.549428,-7.314214,-0.479059,0.222779,-6.204615,4.953841,3.923766,0.149587,1.676917],[-7.120640,2.166467,-8.484053,5.282326,-1.921629,-0.231355,3.324081,1.924222,-4.478202,-8.950127,-7.235726,-8.409780,0.062588,8.993746,3.010021,5.233048],[0.626435,1.922270,5.066797,0.089584,1.832414,7.328567,-2.915843,4.759608,-5.859265,-4.055563,-5.097943,1.099374,5.791930,-0.638497,8.548427,-3.642550],[0.334499,8.019766,6.654164,-9.602945,-1.928528,2.932515,4.161618,-4.288104,-2.280669,-5.928726,5.676306,-9.040085,-9.522745,6.321922,-4.561909,0.867401],[-9.833075,5.125736,7.858294,-0.836366,4.240683,6.981519,-6.590189,-8.068548,-4.427159,-5.826201,-9.986435,-0.913966,9.451974,3.632344,-6.891003,3.638258],[0.616929,-5.777301,9.651132,-1.490425,-0.056210,2.363999,0.139789,1.762712,-5.854346,2.300041,-2.365950,-8.919754,-9.079463,2.542727,-3.846233,6.279866],[6.752164,-0.507878,-3.686799,5.744280,-2.587953,-2.278133,5.475016,-6.299429,0.001412,-9.409092,2.991342,2.455003,-9.030331,-2.894346,-3.718496,-6.026521],[2.623440,-7.810802,-8.640816,-5.438724,-7.998252,-5.048004,-8.065134,7.948967,2.241121,0.154343,-2.445371,-6.162323,-1.242013,7.149231,-9.074497,-0.262200],[3.587126,5.924502,0.927283,-6.842880,-5.087549,8.537541,3.611720,-2.823817,-6.387165,-8.151370,1.509627,-5.647369,3.875399,-8.516651,3.636785,-6.433765]]], dtype = "float32")#candidate|8977|(2, 14, 16)|const|float32
bop_8978 = relay.not_equal(var_8976.astype('bool'), const_8977.astype('bool')) # shape=(2, 14, 16)
output = bop_8978
output2 = bop_8978
func_8993 = relay.Function([var_8976,], output)
mod['func_8993'] = func_8993
mod = relay.transform.InferType()(mod)
var_8994 = relay.var("var_8994", dtype = "float32", shape = ())#candidate|8994|()|var|float32
output = func_8993(var_8994)
func_8995 = relay.Function([var_8994], output)
mutated_mod['func_8995'] = func_8995
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9242 = relay.var("var_9242", dtype = "float32", shape = (13, 13, 10))#candidate|9242|(13, 13, 10)|var|float32
uop_9243 = relay.atanh(var_9242.astype('float32')) # shape=(13, 13, 10)
func_5735_call = mod.get_global_var('func_5735')
func_5738_call = mutated_mod.get_global_var('func_5738')
const_9255 = relay.const([[-1.739134],[9.457474],[-6.392961],[-8.734020],[-5.527287],[2.658980],[2.461649],[-0.214264],[-7.465608],[-9.539022],[3.893555],[3.178214],[7.382035],[-6.598310],[8.446724],[2.550415],[0.456905],[9.014542],[-6.049272],[-4.217968],[7.222169],[-9.989640],[-6.036190],[2.757843],[-1.738774],[9.098052],[6.021124],[-2.547251],[6.914745],[-7.297637],[-6.352253],[-8.095367],[-3.454638],[2.964403],[7.820226],[-1.443527],[1.640549],[9.095167],[3.741701],[2.783080],[-1.631034],[9.383671],[2.405268],[-6.228214],[-5.952524],[8.623307],[-0.068678],[9.743206],[7.856248],[8.685103],[-3.395154],[5.321436],[-7.538648],[-0.443106],[1.254345],[0.341319],[-9.724278],[2.859471],[4.457411],[-7.499955],[-8.296299],[-7.530210],[5.792255],[-7.415256],[-9.795409],[-8.404981],[1.746237],[-6.185932],[-4.862331],[3.041890],[-7.166601],[-5.945852],[9.307156],[-4.504472],[1.664484],[-6.238376],[-6.892535],[1.889635],[-2.825715],[-6.731036],[8.020789],[-2.943618],[-4.153256],[4.602466],[2.809660],[7.741921],[2.970244],[-2.487306],[8.609861],[5.890534],[3.328011],[5.842169],[-6.676821],[0.622212],[-8.506763],[0.065524],[-6.622522],[-1.878574],[5.123557],[-2.557379],[-4.407590],[-7.884209],[7.261683],[-3.103587],[-0.766552],[1.447460],[1.884728],[3.907879],[6.726545],[4.481423],[3.652916],[-6.683239],[-4.817465],[-7.113946],[-1.749387],[-6.597658],[-5.833827],[-8.190770],[7.180040],[7.249672],[3.550532],[8.822867],[2.361532],[-5.697602],[1.864319],[-4.267387],[2.981196],[0.524299],[5.548406],[0.718190],[-9.844880],[-5.145973],[-2.895730],[-8.291869],[3.689128],[1.859148],[-1.235833],[6.740300],[-7.026126],[3.433602],[7.297126],[-0.014131],[-5.310019],[-3.544485],[0.371807],[2.605527],[4.928668],[8.396340],[-1.761315],[0.686395],[9.949740],[-3.230268],[7.128017],[9.836050],[-9.700164],[-4.522318],[-9.888843],[-1.189029],[-0.622719],[-9.067514],[-6.529034],[7.331914],[3.677652],[4.883618],[-1.571872],[4.448660],[-5.948743],[9.964402],[7.358496],[0.714004],[2.039630],[-8.877615],[-0.707180],[-8.730528],[2.570314],[-5.443935],[-6.159261],[-6.680423],[-2.433156],[-6.361783],[-5.747710],[-4.469760],[7.379611],[1.471860],[-5.570176],[-3.768632],[-0.854032],[4.189497],[7.025823],[7.821539],[-8.460644],[-0.150551],[8.264270],[-2.913049],[6.264179],[-3.912683],[-7.302233],[-9.058535],[-6.563220],[8.086885],[-6.260546],[4.921453],[-5.198367],[2.430309],[-9.831410],[-1.169325],[-5.907588],[-6.323809],[5.542445],[-7.835602],[8.843672],[6.841486],[1.455212],[4.295258],[4.434823],[2.650970],[4.681428],[-5.128866],[7.761439],[5.290977],[-9.012708],[0.333189],[5.673242],[-9.504739],[-5.892339],[0.069479],[3.506953],[-9.794744],[-7.024533],[-2.545745],[-1.273303],[8.823833],[-1.286600],[3.951749],[7.298111],[-4.376143],[-8.249341],[-8.076956],[3.999658],[1.480878],[5.807793],[6.297982],[7.207741],[-9.615420],[6.876066],[2.182047],[-6.879207],[4.695370],[-4.483302],[-5.617608],[-6.207186],[8.881744],[-2.545082],[-9.733815],[-7.080379],[-6.235028],[-7.309618],[-1.676898],[5.744064],[1.253726],[8.879150],[-4.023125],[5.509989],[7.340944],[-5.995217],[0.832144],[-4.149764],[3.233670],[-6.776887],[-0.887188],[7.179992],[7.083325],[-0.649440],[2.522981],[-7.252829],[-6.142271],[7.702253],[9.009947],[7.862117],[-6.780626],[-3.372844],[-0.729433],[-8.930335],[-0.493725],[0.466399],[0.512162],[7.362924],[-9.173660],[-1.867198],[3.979395],[-3.725542],[4.788663],[-6.586716],[-7.587374],[0.120510],[3.719289],[-2.268651],[-5.301098],[6.274768],[7.879564],[0.840997],[-1.225629],[7.170747],[-1.562649],[-7.080771],[-7.366890],[4.364054],[0.560460],[-0.078612],[5.173992],[-7.390234],[-6.069827],[-0.745442],[-7.784299],[9.194211],[-2.663478],[-5.925666],[5.663851],[4.688067],[-9.303809],[1.213953],[-8.564533],[-4.520733],[-1.651028],[6.699000],[-4.259651],[-0.853928],[-2.478026],[8.034299],[-5.975500],[8.905827],[2.497530],[2.337383],[4.193190],[-8.110122],[5.590042],[3.579795],[-0.436719],[3.237560],[-5.498748],[7.857408],[-2.163078],[6.972217],[-8.775660],[5.391725],[9.129288],[-2.781685],[1.281403],[9.949215],[-6.481338],[-7.084278],[8.208560],[-2.593961],[7.538495],[-7.079638],[-5.284127],[-4.389357],[6.228480],[-8.509469],[-6.586216],[4.304468],[-2.431921],[-7.495277],[8.059936],[-0.348872],[4.298405],[4.264022],[-2.461752],[-4.495676],[8.630723],[-8.204395],[-6.106859],[2.039781],[-0.950736],[-5.344377],[0.667715],[3.897705],[1.746792],[7.722683],[8.397201],[-1.357952],[-4.523731],[-4.429889],[3.164700],[-0.299657],[2.007975],[5.789048],[2.788428],[-1.635499],[-8.492017],[-0.619994],[-4.942399],[6.629261],[1.101479],[-3.716274],[-7.379213],[9.259599],[1.874789],[-5.254006],[5.855407],[1.304725],[7.734728],[-3.454374],[8.892786],[-9.956948],[4.082924],[-5.753825],[-7.784286],[4.516717],[-0.647708],[6.380356],[8.496052],[-1.657035],[-6.077705],[7.690224],[8.131861],[-3.129077],[7.407640],[-8.775077],[0.629954],[-3.104881],[7.219866],[-1.237288],[-5.177781],[-1.801124],[-5.481938],[-5.976375],[-9.647872],[-9.879896],[8.388295],[-6.481179],[-2.250385],[7.566371],[-0.262548],[7.839749],[-8.092309],[-7.502724],[-3.840661],[-7.590133],[1.696908],[6.894500],[-2.569965],[8.741079],[-0.056454],[0.231307],[7.694621],[2.725298],[-0.389764],[-7.712790],[-7.516259],[6.977040],[7.646124],[-5.630617],[-1.028923],[6.423620],[8.464997],[1.312023],[-3.193482],[6.022746],[-1.766385],[-1.350851],[-1.110514],[-2.036400],[-9.155514],[4.829580],[-4.363852],[2.169229],[4.427534],[9.577093],[-2.508360],[6.365742],[5.990058],[3.230977],[2.432912],[4.424120],[4.683386],[3.506551],[5.326305],[1.574533],[-2.912388],[-9.052058],[1.539519],[7.633803],[9.658848],[-7.436986],[4.661360],[-0.270639],[3.160926],[-6.818684],[-4.423134],[-4.918408],[3.191158],[3.619088],[0.536893],[-3.066761],[-9.572513],[-0.491082],[-0.357134],[-7.328878],[-2.301156],[-9.156944],[-1.237809],[1.608975],[-1.139449],[-7.162841],[7.650062],[7.851795],[-5.355193],[5.760460],[0.684517],[-6.466169],[-2.833408],[0.881647],[-5.266582],[-9.726589],[-2.601259],[-9.333599],[1.375448],[-2.465053],[2.714161],[-5.720379],[-1.875157],[1.727398],[1.580425],[-9.225063],[-9.018192],[-5.015096],[-2.421734],[2.698570],[2.402313],[5.283984],[-6.216811],[-4.996782],[7.148796],[-5.142150],[1.966365],[3.711352],[-5.406792],[-4.713733],[0.552656],[-3.242390],[5.030729],[-6.634770],[-2.399919],[-9.634842],[-7.639720],[1.150336],[3.410609],[-9.303475],[9.605905],[7.892574],[-6.746395],[-5.533566],[9.061901],[-2.547295],[4.420264],[-2.321847],[5.709798],[-4.561684],[2.361233],[7.441210],[3.173639],[-0.390862],[-0.954668],[8.066464],[0.386386],[-3.784252],[-4.117394],[-1.446228],[1.219392],[-2.978118],[3.474026],[-8.813590],[-6.799542],[-1.454080],[0.435322],[5.887946],[1.520097],[-9.964401],[-0.343561],[7.689635],[-4.147738],[3.688460],[-4.908708],[1.438147],[-7.192346],[-9.780046],[-7.145395],[-2.533079],[-4.743327],[-8.210359],[-8.226604],[-5.629686],[-7.964650],[2.094483],[-4.827457],[-6.633309],[-5.301003],[6.635859],[-0.869332],[3.996508],[9.654180],[-8.125669],[-3.315989],[-5.469986],[-3.354224],[-8.811402],[-3.320446],[-8.174756],[4.405644],[3.543634],[-6.490411],[3.562292],[-8.815163],[3.982537],[3.536042],[5.658326],[-5.392150],[-4.823616],[8.832808],[6.390992],[-4.450595],[-1.514670],[-6.511348],[2.715329],[4.319308],[-5.561031],[-1.443819],[-9.680451],[-5.620815],[4.562000],[-9.669217],[-9.574121],[7.212946],[1.499728],[2.367742],[-2.653254],[6.499273],[-9.003583],[4.183481],[2.721444],[7.613884],[-2.493250],[4.390240],[-5.492621],[-1.671903],[7.683539],[-1.049380],[5.003216],[6.383883],[-2.401285],[-8.078810],[-6.363405],[-4.372191],[6.254126],[-8.452022],[-2.225031],[-6.208497],[3.307318],[1.872332],[-7.521530],[-4.502489],[1.633043],[6.479107],[-7.241182],[1.990365],[-9.636906],[0.976012],[0.148268],[4.569940],[8.322340],[-3.437732],[7.607754],[-5.922137],[-7.386988],[-4.433427],[2.754665],[5.703968],[-5.826153],[0.310562],[2.520929],[3.559307],[-4.674777],[-9.679763],[-5.498031],[0.604975],[8.264585],[2.219319],[-3.907287],[7.209567],[-0.459573],[0.014509],[-0.332951],[-3.903785],[-7.223939],[9.928760],[-4.276010],[8.847726],[5.952530],[4.555591],[5.647836],[5.979401],[-3.192003],[-8.824428],[-8.723254],[4.108667],[0.209165],[-0.750636],[5.479375],[-5.430428],[9.890144],[1.980851],[9.314127],[-6.417717],[-0.434241],[-3.526915],[-2.795562],[-8.905131],[9.464413],[-6.324640],[2.764179],[-8.833419],[-3.479948],[-5.215563],[2.049973],[2.364848],[4.423494],[-2.486735],[0.957541],[4.816260],[-4.527857],[-6.056449],[-6.452436],[8.120622],[7.457404],[2.207081],[-1.854610],[7.374196],[0.029761],[-6.479289],[6.871348],[6.009471],[2.322868],[2.856885],[-7.752663],[-2.283396],[-2.387939],[-6.729686],[-5.401703],[-8.730452],[4.281954],[-8.011095],[1.605308],[-7.214555],[0.224812],[1.344940],[2.655159],[5.553242],[1.664057],[2.333249],[-1.578520],[-2.297481],[-0.221368],[7.810941],[5.293975],[-8.383607],[3.666883],[-8.339882],[7.606055],[3.033102],[1.893082],[0.579642],[8.949402],[5.544893],[6.809614],[1.827718],[8.673358],[-9.587973],[-6.251927],[-3.485078],[-1.610032],[-6.612582],[0.875305],[-1.202129],[3.440236],[2.921874],[4.414214],[7.255083],[-5.537139],[0.758905],[-4.751021],[7.935875],[-0.714846],[9.015322],[5.184595],[-8.928307],[9.471052],[4.238456],[1.639221],[5.454684],[-4.186759],[-5.607556],[8.236507],[-0.638670],[-5.199061],[0.699958],[-4.997700],[-8.118099],[-6.164032],[4.665437],[4.446644],[6.451814],[-9.583368],[9.706198],[1.715907],[2.856407],[-6.375863],[5.680133],[8.759758],[8.616837],[6.139007],[-4.283462],[0.318813],[-8.858017],[2.828444],[6.103800],[-9.602577],[6.478144],[9.574135],[-9.953296],[3.343096],[-8.327863],[6.895665],[2.690569],[-9.234653],[4.339993],[3.156366],[4.315945],[-1.457283],[-7.125559],[-0.644551],[0.515338],[6.647981],[3.341695],[9.967824],[1.797320],[1.154853],[-0.471838],[8.679270],[-8.250584],[-5.977816],[4.463066],[2.370053],[-9.922257],[-5.142596],[3.015149],[-6.203627],[0.964578],[5.975265],[4.703368],[5.155588],[7.465449],[-1.272833],[1.714043],[7.126805],[2.580336],[5.614432],[0.126579],[-5.670850],[4.667038],[2.249313],[0.996103],[8.027144],[9.267954],[3.468979],[0.303361],[2.725648],[-1.808554],[7.938364],[8.986113],[9.845105],[-3.191622],[5.029790],[5.615023],[-6.592488],[-6.386430],[-7.685461],[4.258790],[0.809847],[-6.287150],[5.303983],[0.198516],[9.665648],[0.864835],[3.454492],[1.844057],[1.164754],[-7.824658],[-3.763952],[-7.893608],[-9.435104],[-6.860500],[-8.757033],[-6.155904],[-8.273316],[6.665760],[-8.093425],[-0.641475],[-1.238355],[-7.343791],[-0.276297],[-0.750463],[-1.296700],[-5.876439],[-5.892574],[3.271279],[4.311288],[1.127440],[4.420506],[9.784003],[7.909488],[-4.852574],[2.008884],[1.420958],[-6.772950],[-1.524791],[0.685660],[-5.203267],[1.181956],[-0.704329],[-2.819902],[-8.408866],[3.137401],[9.850159],[3.051725],[-8.109117],[8.950018],[-2.270924],[1.911504],[-1.192118],[-3.249709],[-8.788448],[8.497088],[0.953424],[8.856087],[2.364839],[8.863023],[-1.690503],[3.049405],[7.856116],[-8.402485],[6.400462],[-5.358424],[0.189815],[3.768557],[1.791346],[-9.964941],[-6.659180],[4.238972],[-4.570166],[7.500241],[-3.741634],[6.566432],[-8.805346],[-8.334821],[9.458292],[9.891009],[8.040735],[-8.202190],[-3.404649],[-9.688541],[2.475153],[0.033965],[1.037699],[6.499654],[-4.936984],[5.709725],[0.406813],[8.854572],[7.774045],[-9.228997],[-8.185141],[-9.093554],[7.709887],[-8.590926],[-2.736661],[-5.959993],[0.399487],[6.798538],[-2.841137],[-9.930979],[-0.490457],[4.400556],[-0.406179],[7.897085],[-4.289022],[-4.505850],[6.206165],[-2.014887],[-9.910879],[-9.620205],[-4.940294],[-7.874487],[3.047304],[-4.907929],[8.244314],[-5.955795],[-2.407579],[6.657772],[-8.660857],[-5.386281],[-4.808417],[9.494256],[5.164568],[2.715350],[6.300710],[4.448446],[-2.920324],[2.117627],[4.853574],[1.726971],[4.595466],[-6.289786],[4.617001],[-4.717651],[-6.889861],[-3.101955],[-7.195670],[7.586317],[-5.080883],[9.243415],[-4.505950],[7.129385],[-7.132530],[-0.983866],[-6.498491],[-2.462336],[1.851096],[8.648013],[2.994401],[-4.519897],[-5.861974],[-5.848050],[7.136437],[9.884441],[-1.166477],[5.618542],[2.223241],[8.387021],[7.128841],[1.724981],[7.944961],[3.250218],[7.574465],[9.663117],[6.273741],[-8.473208],[1.221095],[-9.290430],[-1.109427],[-4.285727],[-9.829550],[-3.238508],[-0.930208],[9.479573],[8.393394],[4.312951],[7.521006],[-4.944081],[9.654922],[4.171194],[4.295184],[-5.489773],[-3.491814],[8.691781],[-7.729003],[-3.921744],[2.105755],[-1.781301],[-7.081619],[-1.190087],[0.429727],[9.316192],[-0.457535],[0.304277],[4.194084],[-4.727181],[-7.527433],[3.566930],[8.095578],[-6.815324],[-6.257086],[-9.715585],[8.974302],[9.038111],[0.893837],[7.701660],[3.249582],[1.757761],[-2.082334],[5.461995],[1.350748],[1.070506],[1.038737],[-2.631719],[6.307083],[-4.741053],[9.756935],[-4.781238],[-8.468308],[7.655450],[1.317757],[-4.420747],[6.095936],[-8.271967],[-6.595534],[7.553520],[-9.801391],[9.359541],[-7.178131],[-4.593785],[-2.468371],[3.619817],[-8.438494],[-8.510467],[-6.186520],[-7.905707],[0.987456],[-9.854428],[-3.118989],[-9.522576],[7.448318],[-8.528746],[-0.642038],[8.004103],[7.396679],[2.758009],[-4.517985],[-0.641465],[-7.895277],[0.901639],[-0.830388],[-8.366761],[-0.498005],[-2.609631],[0.626565],[0.378939],[-4.752920],[-5.964938],[-8.796884],[9.076616],[-6.600450],[4.235104],[-5.347166],[9.334189],[2.346123],[4.160251],[-5.578819],[0.877653],[-8.574249],[4.921596],[-0.435687],[-1.422435],[-9.927720],[-0.712170],[-0.734665],[-9.110273],[-8.463974],[-5.028988],[0.858569],[7.702659],[-9.552216],[-2.240167],[-7.873182],[-5.507487],[7.190277],[-2.331770],[-7.698320],[2.053220],[-8.462787],[4.451128],[5.784480],[8.278076],[-5.325616],[-3.355264],[3.796087],[-7.498345],[-9.067695],[-8.918259],[-3.224670],[-5.397861],[-0.273735],[6.508728],[2.220171],[3.552691],[-7.950226],[4.139828],[-4.419128],[2.949451],[-1.829190],[5.442378],[6.144960],[9.051152],[-2.191709],[-7.589445],[-5.952556],[1.546630],[-1.961020],[-8.926866],[3.998487],[4.467468],[-3.318331],[1.639436],[9.583347],[6.601800],[5.837762],[8.270262],[-4.308523],[-7.970229],[-2.347937],[0.631405],[1.407901],[6.657017],[-4.137575],[-1.486377],[9.394607],[8.568604],[-5.648043],[-4.765396],[-1.789489],[3.355415],[-6.087037],[-6.073886],[6.674975],[-7.978580],[-3.368993],[3.365670],[-5.944328],[8.793292],[-4.360053],[-6.213670],[3.904132],[6.887821],[-9.246620],[6.643088],[-1.104923],[-5.458798],[1.529250],[5.433000],[-4.965354],[-9.265015],[-0.203910],[-0.486672],[-2.373097],[2.445284],[6.318030],[-7.259532],[6.130569],[-3.124423],[1.968017],[-9.435633],[-2.195289],[9.087902],[-8.892568],[7.931212],[-2.662464],[0.629220],[0.815516],[2.270535],[1.354399],[-4.712109],[-6.617904],[7.789690],[-3.127882],[9.990202],[6.179895],[4.502836],[1.729683],[7.164046],[-6.042173],[-7.767547],[-4.072470],[6.992223],[9.409967],[1.929731],[0.577591],[-3.821797],[-1.199070],[2.566100],[1.228805],[-9.350946],[7.749775],[7.476628],[-7.505789],[-3.384718],[6.038584],[1.897012],[-6.622300],[8.341617],[3.328887],[-0.366514],[-3.650552],[-3.595979],[-4.052170],[0.073909],[8.820902],[-3.818556],[-9.993532],[7.068900],[-4.206074],[0.342595],[-2.127898],[0.585930],[3.603442],[-9.180495],[0.868064],[6.693228],[8.409934],[-8.719174],[0.828225],[-5.737028],[5.057739],[3.512897],[-5.507866],[3.084232],[-8.771373],[-4.681785],[3.567428],[0.057960],[-5.835608],[-7.575309],[-4.552650],[3.912774],[9.060911],[9.395433],[7.583488],[7.306989],[-0.525015],[-6.975436],[0.727929],[1.829591],[-3.943838],[-1.488271],[6.266467],[-3.032675],[-2.879933],[4.188921],[-6.442699],[-6.497647],[-4.366749],[5.135368],[2.056234],[8.910401],[4.020245],[-1.230466],[4.730803],[8.747137],[3.894307],[7.994341],[6.795512],[-3.849637],[-0.861784],[1.522222],[-3.490271],[2.663892],[4.330958],[3.037603],[4.286254],[3.339618],[-5.356255],[-3.170368],[3.242026],[-3.258294],[6.665784],[-6.870070],[6.272467],[-0.409165],[-5.312935],[7.113971],[-3.801266],[-0.450152],[9.169505],[-9.715824],[-0.216093],[1.639654],[-2.309096],[-5.521186],[7.589555],[-8.597015],[-0.494323],[-1.271996],[-4.475056],[-6.805527],[-4.865574],[9.280718],[-8.390348],[-5.142427],[3.669498],[-1.304575],[-2.694466],[4.141625],[2.763334],[3.819043],[-0.513978],[-8.930320],[-4.704832],[-6.552658],[6.411023],[6.030496],[-3.043256],[-7.024900],[-5.094770],[-7.369832],[-2.642856],[6.816735],[8.992289],[4.370741],[-6.276343],[0.927740],[-9.308649],[-5.180711],[-7.188448],[8.961212],[8.721223],[1.970692],[-2.945452],[-3.807314],[8.983557],[-9.886175],[3.957159],[-1.697336],[-8.323140],[-0.521457],[-5.983362],[4.011434],[1.186364],[9.400175],[5.675936],[6.355450],[-5.807966],[-0.533707],[6.830618],[2.263236],[-7.065526],[-9.422497],[-7.591449],[-2.797935],[-5.823256],[5.645000],[-8.906489],[8.947462],[-0.420122],[-0.228164],[-1.051104],[-8.800937],[-4.176650],[6.545806],[5.779287],[-9.431122],[-1.137870],[-4.943110],[-3.266785],[-7.033889],[5.517130],[8.352978],[-2.855567],[1.030268],[-8.248846],[-2.958610],[1.500314],[4.297924],[-1.042669],[4.791379],[4.590370],[3.378983],[-9.882474],[-7.059596],[-2.921767],[0.928098],[6.269256],[6.372990],[-4.181502],[-2.245386],[-0.803441],[6.011951],[-7.999508],[-6.895492],[4.147052],[-6.213202],[3.496373],[-4.889656],[2.791704],[-6.707816],[7.788859],[8.469535],[0.856407],[7.977456],[0.174350],[-2.755626],[-8.511719],[-0.039651],[-2.795556],[9.049019],[-7.999521],[-8.462968],[8.326905],[-1.264916],[-1.622291],[-2.524958],[-8.277019],[-9.136646],[5.363873],[6.100749],[9.833841],[-0.946913],[4.120068],[-3.999332],[8.826738],[8.883989],[-9.154333],[-9.380790],[0.731549],[-8.022358],[0.100068],[5.185285],[1.049400],[5.400061],[8.046041],[9.833475],[-2.902698],[9.201220],[-7.482844],[2.547039],[6.400987],[-3.412202],[6.203530],[-7.349850],[7.991419],[-2.960476],[2.740317],[-6.381561],[3.580877],[5.295961],[8.903977],[5.216683],[4.532031],[2.983015],[2.647207],[9.122120],[-3.659621],[-3.566017],[-3.895222],[-6.239217],[9.664625],[3.750508],[-3.566194],[4.277798],[0.011851],[1.968904],[-5.668926],[2.425546],[8.038642],[7.579354],[1.473644],[6.170114],[-2.849208],[8.416749],[-1.059349],[-2.184836],[-1.874210],[1.847812],[-5.000914],[-0.781073],[5.142503],[-2.765480],[6.499306],[8.556296],[-4.307316],[0.925348],[-3.228165],[5.513501],[-8.361885],[0.841671],[-5.397132],[-8.677990],[4.375590],[-6.209185],[9.720996],[-0.924336],[-2.481314],[-5.827139],[-4.496810],[-8.332756],[-5.838975],[-9.871137],[-4.127459],[-6.388378],[4.897102],[-4.156780],[2.877875],[-4.329326],[-5.874338],[-8.304483],[-3.371784],[-3.816525],[0.492142],[-0.989152],[3.905841],[0.112647],[-0.801802],[-0.261172],[8.008237],[1.790177],[-2.894915],[0.493652],[-6.755072],[7.244842],[-8.579362],[-4.034707],[-0.232522],[8.337835],[7.201148],[2.094081],[-2.177517],[8.400948],[-7.527661],[5.835813],[-8.330197],[-9.192034],[-6.756537],[-5.950266],[-2.477826],[0.331829],[-2.941413],[4.285206],[5.508001],[-3.062190],[-0.397106],[0.572393],[-6.815671],[8.730994],[-6.680986],[5.953288],[0.363512],[4.669331],[0.733470],[-4.475697],[2.371451],[-8.541432],[-5.774630],[-6.667561],[-1.120173],[-7.390872],[-2.095831],[0.373276],[-3.631160],[-2.097154],[2.751510],[8.822693],[4.897551],[2.935196],[4.151391],[-5.218956],[1.028462],[-5.191003],[-3.410358],[2.980517],[2.077068],[2.339134],[4.379630],[4.513704],[6.429544],[-4.748853],[2.178675],[6.514345],[7.472836],[6.115922],[1.898991],[6.963815],[-0.413428],[-7.320564],[4.269983],[7.217500],[3.704158],[-8.789969],[7.160977],[0.881243],[2.716004],[3.739688],[5.221969],[-3.225632],[6.931519],[5.044328],[9.500799],[-9.046641],[-8.589842],[6.149283],[-2.807031],[5.560021],[9.072589],[8.782735],[0.681221],[-9.940972],[-3.938584],[7.238240],[-1.837759],[-5.726845],[9.381576],[-5.911225],[8.852651],[-2.725974],[4.781184],[9.677890],[-8.693184],[-7.165264],[-0.228409],[-6.420001],[-9.422637],[8.910585],[-5.218445],[-2.178710],[-0.287389],[1.266600],[1.902194],[-2.049971],[-3.278490],[-9.253783],[-0.417507],[9.007604],[-5.111076],[2.231313],[7.757395],[-4.897322],[-3.570516],[0.303861],[-6.035430],[0.002818],[-7.581473],[-5.227862],[2.106062],[-1.444018],[8.989181],[0.686183],[-1.060700],[-5.072269],[-1.041628],[-6.399514],[1.595656],[8.359403],[-4.907197],[7.949687],[1.828735],[1.772904],[8.175468],[1.888607],[-5.803850],[-7.309694],[-9.049718],[-8.460152],[-3.441550],[-5.559255],[-5.206540],[5.902949],[4.473893],[2.191132],[0.248904],[4.337675],[1.347851],[-6.284287],[-4.155559],[8.409299],[-5.569724],[1.251241],[-4.352014],[5.913765],[-6.113007],[8.809896],[-6.013235],[1.925590],[-4.133516],[5.857192],[9.718031],[-2.688603],[0.458147],[3.063880],[-4.237662],[0.444113],[-8.078168],[5.089822],[-7.488793],[5.999369],[-6.470706],[8.916245],[6.153306],[6.299933],[9.557197],[7.556010],[6.793833],[2.448500],[1.817419],[-3.720033],[-3.108033],[-1.217847],[-1.398567],[3.908621],[-3.217920],[-9.649081],[8.148504],[-1.523640],[-7.509454],[-7.251194],[-7.308158],[-6.488226],[3.240173],[3.667398],[-6.248555],[-1.334238],[0.405523],[7.735414],[4.048366],[-2.047364],[9.704311],[-3.713784],[-4.595322],[-5.384581],[-2.772121],[-4.544921],[-3.542367],[-3.206609],[-1.513744],[-2.291363],[-5.598294],[9.562728],[4.418317],[1.097270],[6.374019],[5.103151],[-2.027955],[-2.668232],[-1.154465],[7.266837],[3.156498],[6.973120],[-8.529315],[-2.815629],[0.593441],[4.233604],[2.698621],[5.260655],[1.574534],[4.350900],[-6.120254],[-9.236919],[3.391327],[1.590231],[9.776461],[-3.584181],[-3.612369],[-9.768489],[-7.882650],[-5.053430],[-2.195645],[9.343479],[-6.483351],[-9.354326],[7.575254],[9.369809],[-0.550301],[4.209330],[-3.707778],[9.625547],[4.571443],[-4.916775],[-5.668402],[3.602867],[0.606317],[-3.479431],[1.933927],[-1.089891],[6.385555],[-5.999153],[-2.877628],[-0.406649],[3.838252],[-9.559385],[5.907247],[4.066229],[-3.086920],[-2.183867],[-4.621181],[3.782583],[4.800265],[3.129515],[6.179602],[9.157428],[0.110597],[0.575959],[3.130427],[-7.354596],[3.007466],[-2.439334],[4.105834],[-8.530742],[1.805858],[-5.742823],[-4.942942],[-2.859938],[1.886943],[-4.907906],[8.660154],[5.310496],[4.240977],[-6.163225],[1.601064],[3.373853],[-5.021383],[0.803206],[1.586153],[0.610790],[-7.329034]], dtype = "float32")#candidate|9255|(1920, 1)|const|float32
call_9254 = func_5735_call(relay.reshape(const_9255.astype('float32'), [8, 16, 15]))
call_9256 = func_5735_call(relay.reshape(const_9255.astype('float32'), [8, 16, 15]))
output = relay.Tuple([uop_9243,call_9254,const_9255,])
output2 = relay.Tuple([uop_9243,call_9256,const_9255,])
func_9294 = relay.Function([var_9242,], output)
mod['func_9294'] = func_9294
mod = relay.transform.InferType()(mod)
mutated_mod['func_9294'] = func_9294
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9295 = relay.var("var_9295", dtype = "float32", shape = (13, 13, 10))#candidate|9295|(13, 13, 10)|var|float32
func_9294_call = mutated_mod.get_global_var('func_9294')
call_9296 = func_9294_call(var_9295)
output = call_9296
func_9297 = relay.Function([var_9295], output)
mutated_mod['func_9297'] = func_9297
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10153 = relay.var("var_10153", dtype = "float64", shape = (6, 12, 16))#candidate|10153|(6, 12, 16)|var|float64
var_10154 = relay.var("var_10154", dtype = "float64", shape = (6, 12, 16))#candidate|10154|(6, 12, 16)|var|float64
bop_10155 = relay.floor_mod(var_10153.astype('float64'), relay.reshape(var_10154.astype('float64'), relay.shape_of(var_10153))) # shape=(6, 12, 16)
output = relay.Tuple([bop_10155,])
output2 = relay.Tuple([bop_10155,])
func_10161 = relay.Function([var_10153,var_10154,], output)
mod['func_10161'] = func_10161
mod = relay.transform.InferType()(mod)
var_10162 = relay.var("var_10162", dtype = "float64", shape = (6, 12, 16))#candidate|10162|(6, 12, 16)|var|float64
var_10163 = relay.var("var_10163", dtype = "float64", shape = (6, 12, 16))#candidate|10163|(6, 12, 16)|var|float64
output = func_10161(var_10162,var_10163,)
func_10164 = relay.Function([var_10162,var_10163,], output)
mutated_mod['func_10164'] = func_10164
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10521 = relay.var("var_10521", dtype = "int16", shape = (7, 16, 3))#candidate|10521|(7, 16, 3)|var|int16
var_10522 = relay.var("var_10522", dtype = "int16", shape = (7, 16, 3))#candidate|10522|(7, 16, 3)|var|int16
bop_10523 = relay.logical_xor(var_10521.astype('int16'), relay.reshape(var_10522.astype('int16'), relay.shape_of(var_10521))) # shape=(7, 16, 3)
const_10534 = relay.const([[[-4,2,9],[1,-6,-2],[4,9,8],[7,10,-8],[-4,-10,6],[2,5,9],[7,3,3],[-10,-9,-2],[-6,6,8],[3,-1,-10],[3,8,8],[-1,-5,8],[-4,-4,9],[10,8,-1],[2,-8,-9],[1,-4,1]],[[6,7,-8],[9,5,-5],[-3,10,-10],[8,7,6],[-6,-7,8],[2,-9,3],[-6,-1,10],[-7,-10,-4],[10,-6,-8],[2,-1,-6],[-8,-1,9],[-6,8,8],[-5,1,-2],[10,7,-8],[8,8,-10],[8,-3,6]],[[-5,-7,-2],[-3,7,-6],[10,-2,2],[9,1,-1],[2,-10,-8],[-6,-1,-6],[-7,-1,2],[5,5,-9],[7,-9,7],[-1,9,5],[10,-10,6],[3,6,8],[-3,-10,-10],[7,8,10],[-6,-4,4],[6,-3,-4]],[[-4,-2,3],[8,5,-6],[8,-6,9],[-2,7,-2],[5,7,-4],[-7,-10,-9],[-1,10,-5],[-10,-2,-9],[-2,-8,7],[2,-9,2],[-1,-4,-7],[3,9,3],[4,7,2],[8,7,5],[-5,-7,-7],[10,7,-9]],[[8,-4,9],[-1,3,-8],[-5,10,-10],[5,-3,4],[9,-10,-7],[-1,-2,1],[2,-4,-1],[-1,9,-8],[6,8,6],[-9,-3,1],[7,8,9],[-3,-3,-8],[-9,1,-2],[-9,-2,6],[-7,5,6],[-4,10,-2]],[[-3,-1,-2],[-1,2,9],[2,-10,4],[-4,-3,-5],[-5,-1,10],[5,10,10],[-9,-5,4],[2,-3,-2],[-10,-10,-5],[3,-3,-6],[-10,8,1],[4,-8,8],[2,-8,2],[-1,-6,7],[-5,1,5],[-3,-10,-4]],[[7,-10,4],[7,-10,10],[4,-6,2],[10,-4,-5],[10,-1,-7],[3,1,-8],[-3,-1,-1],[5,-2,-4],[4,2,-6],[-4,-5,1],[10,-7,-7],[-7,4,-5],[1,-8,3],[-7,-9,5],[-8,-4,-6],[6,-8,10]]], dtype = "int16")#candidate|10534|(7, 16, 3)|const|int16
bop_10535 = relay.equal(var_10522.astype('bool'), relay.reshape(const_10534.astype('bool'), relay.shape_of(var_10522))) # shape=(7, 16, 3)
func_1128_call = mod.get_global_var('func_1128')
func_1130_call = mutated_mod.get_global_var('func_1130')
var_10543 = relay.var("var_10543", dtype = "uint8", shape = (400,))#candidate|10543|(400,)|var|uint8
call_10542 = func_1128_call(relay.reshape(var_10543.astype('uint8'), [10, 5, 8]))
call_10544 = func_1128_call(relay.reshape(var_10543.astype('uint8'), [10, 5, 8]))
uop_10562 = relay.sin(var_10522.astype('float32')) # shape=(7, 16, 3)
output = relay.Tuple([bop_10523,bop_10535,call_10542,var_10543,uop_10562,])
output2 = relay.Tuple([bop_10523,bop_10535,call_10544,var_10543,uop_10562,])
func_10565 = relay.Function([var_10521,var_10522,var_10543,], output)
mod['func_10565'] = func_10565
mod = relay.transform.InferType()(mod)
mutated_mod['func_10565'] = func_10565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10565_call = mutated_mod.get_global_var('func_10565')
var_10567 = relay.var("var_10567", dtype = "int16", shape = (7, 16, 3))#candidate|10567|(7, 16, 3)|var|int16
var_10568 = relay.var("var_10568", dtype = "int16", shape = (7, 16, 3))#candidate|10568|(7, 16, 3)|var|int16
var_10569 = relay.var("var_10569", dtype = "uint8", shape = (400,))#candidate|10569|(400,)|var|uint8
call_10566 = func_10565_call(var_10567,var_10568,var_10569,)
output = call_10566
func_10570 = relay.Function([var_10567,var_10568,var_10569,], output)
mutated_mod['func_10570'] = func_10570
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10668 = relay.var("var_10668", dtype = "int64", shape = (7, 6, 13))#candidate|10668|(7, 6, 13)|var|int64
var_10669 = relay.var("var_10669", dtype = "int64", shape = (7, 6, 13))#candidate|10669|(7, 6, 13)|var|int64
bop_10670 = relay.right_shift(var_10668.astype('int64'), relay.reshape(var_10669.astype('int64'), relay.shape_of(var_10668))) # shape=(7, 6, 13)
output = relay.Tuple([bop_10670,])
output2 = relay.Tuple([bop_10670,])
func_10673 = relay.Function([var_10668,var_10669,], output)
mod['func_10673'] = func_10673
mod = relay.transform.InferType()(mod)
var_10674 = relay.var("var_10674", dtype = "int64", shape = (7, 6, 13))#candidate|10674|(7, 6, 13)|var|int64
var_10675 = relay.var("var_10675", dtype = "int64", shape = (7, 6, 13))#candidate|10675|(7, 6, 13)|var|int64
output = func_10673(var_10674,var_10675,)
func_10676 = relay.Function([var_10674,var_10675,], output)
mutated_mod['func_10676'] = func_10676
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11084 = relay.var("var_11084", dtype = "uint32", shape = (5, 7, 4))#candidate|11084|(5, 7, 4)|var|uint32
var_11085 = relay.var("var_11085", dtype = "uint32", shape = (5, 7, 4))#candidate|11085|(5, 7, 4)|var|uint32
bop_11086 = relay.bitwise_or(var_11084.astype('uint32'), relay.reshape(var_11085.astype('uint32'), relay.shape_of(var_11084))) # shape=(5, 7, 4)
uop_11093 = relay.exp(bop_11086.astype('float32')) # shape=(5, 7, 4)
output = relay.Tuple([uop_11093,])
output2 = relay.Tuple([uop_11093,])
func_11108 = relay.Function([var_11084,var_11085,], output)
mod['func_11108'] = func_11108
mod = relay.transform.InferType()(mod)
var_11109 = relay.var("var_11109", dtype = "uint32", shape = (5, 7, 4))#candidate|11109|(5, 7, 4)|var|uint32
var_11110 = relay.var("var_11110", dtype = "uint32", shape = (5, 7, 4))#candidate|11110|(5, 7, 4)|var|uint32
output = func_11108(var_11109,var_11110,)
func_11111 = relay.Function([var_11109,var_11110,], output)
mutated_mod['func_11111'] = func_11111
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11186 = relay.var("var_11186", dtype = "int8", shape = (14, 10, 14))#candidate|11186|(14, 10, 14)|var|int8
const_11187 = relay.const([[[5,3,7,-5,6,10,-1,3,-7,-6,10,-1,-9,-8],[7,9,2,-3,-4,7,8,-1,2,-6,2,7,3,5],[-4,-5,10,4,-5,-1,3,-8,9,-2,3,9,10,-5],[3,-5,4,-9,-5,6,-2,-9,-7,8,8,7,7,-5],[4,-2,-2,4,-8,-2,-10,2,-7,6,10,10,-3,-7],[4,9,-6,5,-9,-5,5,-1,8,-6,-6,9,-8,4],[-5,-2,-5,-9,2,-10,-2,-8,-4,2,2,-5,2,-4],[2,-2,9,9,4,8,9,-7,-2,-10,1,8,-1,2],[8,2,4,-8,7,-10,5,-5,3,-7,-6,-3,10,10],[6,-3,-8,6,-8,-6,2,-3,1,3,-1,-10,7,6]],[[5,-9,10,7,6,9,-8,8,-10,-8,3,4,2,-3],[-5,8,-4,3,8,3,3,-9,-8,2,-2,-6,10,10],[-4,-10,-3,1,3,3,-5,-7,-10,-1,7,-6,-2,5],[2,3,-10,7,1,-1,3,8,-2,-10,5,-1,-3,-3],[-9,8,-6,7,3,-9,3,1,-6,6,7,-10,-7,5],[6,-6,6,6,6,8,-9,-6,-9,-8,7,2,-4,-4],[-1,-3,-7,-2,5,-7,-1,-10,3,5,-2,-6,-1,-1],[-1,5,4,-1,-7,5,10,2,-6,6,-6,-1,3,7],[8,-6,3,-2,-7,9,7,7,6,3,-2,1,-7,8],[2,2,1,8,9,-10,-5,4,3,-1,1,-10,2,-10]],[[-6,9,-4,-7,-8,9,-6,-8,10,-5,1,3,-2,4],[-6,3,3,-1,4,1,2,-1,-3,-1,1,7,6,6],[2,-3,4,-10,9,-5,-9,7,8,-10,-7,3,1,-9],[-9,6,-5,-8,7,8,-9,-1,9,10,5,8,4,-9],[-1,-9,-5,2,4,-1,-9,-8,-9,-9,-8,6,2,5],[-5,-9,7,9,-3,-2,-2,-9,-1,1,10,10,10,9],[-2,-8,-1,5,4,-9,-6,5,5,1,5,-8,6,2],[6,8,8,-4,2,8,-5,5,10,-3,6,-3,-8,5],[-10,9,-8,5,4,8,1,2,-3,-9,-6,9,8,4],[-4,-9,-6,4,7,4,9,9,-6,-5,-7,3,9,-7]],[[6,3,10,8,-2,4,2,-5,9,-10,-3,5,1,5],[-2,7,2,1,3,10,2,9,1,4,5,5,10,10],[-10,1,7,-3,1,-3,-3,-2,-8,-10,2,-8,-7,7],[-5,-9,1,-8,-10,-7,4,5,-4,6,-5,-10,-10,6],[-5,5,7,6,5,-8,6,-6,-7,2,8,-3,4,-2],[4,-2,-8,-1,-2,-4,-1,-2,8,-9,-6,6,9,-7],[-3,-7,-6,7,7,-8,5,6,4,4,3,-9,-4,-5],[4,-6,-2,5,-2,-9,-10,-8,10,-10,-1,10,-8,6],[-4,7,-4,7,7,-3,4,-8,10,-9,1,7,-4,7],[-8,3,4,1,4,6,-2,10,3,-2,5,5,3,-9]],[[3,-8,-9,-2,-3,-4,1,-8,-9,10,-8,6,6,-1],[-7,3,-6,-8,3,1,3,1,-5,8,9,7,2,1],[9,6,-4,-6,1,-7,-4,-8,-6,-4,10,-5,1,6],[-7,3,9,-2,10,3,-1,-6,3,-5,-7,-7,10,5],[6,-9,8,-1,-1,2,-10,-5,-9,8,-6,-8,2,1],[-9,-5,10,2,-6,-7,-5,-10,-3,-7,-7,4,-10,8],[2,-5,-6,8,6,3,2,-1,-6,1,6,-4,5,-8],[-2,8,-4,5,-5,3,4,3,6,10,-5,-3,-10,-5],[9,-1,-10,5,4,-3,6,2,1,-3,-9,1,5,-4],[3,2,-3,-2,-6,6,-10,10,-4,-3,6,-4,-2,-9]],[[-8,-4,2,-2,-10,9,-5,5,3,-9,-8,4,2,-8],[-2,1,-10,3,-10,-1,1,-6,5,2,-7,-7,-7,10],[8,4,-7,-1,10,10,-1,10,-3,10,8,-5,5,1],[-2,1,-10,-1,-2,5,8,-1,8,-3,-10,8,5,6],[-7,3,-9,-1,-1,-6,-9,-6,6,-6,-1,-5,1,10],[5,9,-2,-1,-9,9,-7,5,-8,2,10,-8,6,3],[-5,7,-10,3,-1,4,9,9,10,1,-7,-2,1,-8],[-1,8,6,7,-4,-8,7,4,-7,1,7,5,-6,-10],[5,8,1,-4,-3,-4,3,1,-6,-3,6,-10,7,10],[10,-10,10,-3,-4,-9,-9,-4,-7,-10,10,7,7,-2]],[[1,-8,9,-10,-8,1,1,10,5,2,-9,-6,-6,-6],[8,-9,-7,4,7,-7,6,-8,8,-6,-2,-6,1,-1],[-2,-3,-4,-3,-1,10,-8,2,7,-10,-6,9,-3,10],[-6,2,-7,-10,7,-3,-10,-4,-2,-4,-6,5,1,1],[-8,9,-1,1,5,-10,-7,-9,-8,9,3,10,-8,-3],[-10,2,-7,-1,1,6,-5,8,-1,-1,2,-10,3,-6],[6,1,-6,-1,5,1,4,-4,6,-3,9,-8,5,-7],[8,1,-3,-10,-7,-1,-3,-8,10,9,4,-4,5,-7],[10,9,9,3,-4,10,6,-4,4,7,4,1,-8,-2],[-9,-5,2,8,-6,3,6,1,-5,-10,-7,-4,-4,8]],[[1,7,8,10,6,1,-3,-3,-8,-2,9,3,-10,6],[3,10,-3,-8,8,3,8,-7,-8,1,-7,10,-4,10],[3,1,-10,-2,7,6,-7,-1,-2,-7,1,10,-10,1],[-5,-1,-9,-4,3,-3,-7,-8,-7,1,-7,4,8,-5],[-4,4,9,8,10,-4,10,-5,-6,3,-2,-7,-3,-7],[2,-1,10,6,3,-5,7,-7,-9,-6,-5,-2,-1,8],[-7,7,8,-6,3,8,-7,8,4,-3,-8,-2,5,-2],[1,4,-6,9,-1,4,8,-2,5,-1,7,-6,2,-10],[9,5,3,-10,-2,-6,-8,9,-2,-3,2,10,7,-4],[1,5,-7,2,2,10,-2,9,7,-8,-10,10,4,-3]],[[5,9,3,-5,-8,2,-10,-6,-1,4,4,10,2,9],[-9,6,-2,-9,-1,-7,5,1,-6,-10,1,-6,8,10],[-8,-6,1,-3,9,10,-8,10,-10,9,-5,2,6,2],[6,6,1,10,-5,7,-5,-3,7,8,-4,3,9,7],[3,-9,-3,4,-8,8,-7,7,-3,7,-6,7,-4,-9],[-4,-6,8,-8,4,-5,-6,6,-7,7,5,-9,-1,-1],[5,-7,8,7,-3,-7,9,-9,-2,-10,10,-8,-5,6],[-3,10,6,-8,3,10,-2,-10,8,8,4,10,9,-9],[-7,10,-3,-10,10,-5,5,6,2,-10,5,10,-8,-5],[10,-1,10,-7,-2,4,-6,2,4,-1,-5,-7,-1,-2]],[[-7,7,-3,-4,-10,8,1,3,-2,-1,6,-5,4,-1],[-10,5,-10,-5,-3,-7,-4,-4,-8,-2,-5,-7,4,-9],[-3,-3,-3,-10,-3,7,-8,8,9,4,-10,-8,-7,7],[8,-10,-8,3,3,6,10,1,-8,-9,10,6,10,-6],[-10,10,1,-8,3,10,-7,-2,-2,7,10,8,-1,-2],[8,-10,3,6,-2,-2,-8,-2,1,-1,5,-2,4,-6],[2,-8,8,-3,-9,-4,5,-7,8,-5,-3,1,-4,4],[-1,-5,-10,7,2,-10,9,4,-10,5,10,9,8,-1],[1,4,-8,6,1,-8,3,4,2,4,-8,-1,10,-4],[-8,-1,-2,2,4,-10,3,-10,5,-6,1,-10,10,-1]],[[-9,-7,10,7,-4,2,9,5,-9,8,-8,-3,-6,-1],[-2,5,7,-10,3,-9,-4,-7,4,-5,-6,6,-7,6],[-2,8,-1,-9,8,-5,5,-7,8,4,-5,-4,-9,-6],[1,-10,9,9,2,8,7,10,-1,3,-9,1,3,5],[-6,-10,3,10,-1,-3,8,2,7,7,9,7,-6,-3],[2,3,-9,4,7,5,4,-1,-1,10,-7,6,-9,-5],[3,-4,-6,-4,-3,6,-4,-8,-8,5,-3,7,-1,5],[8,-5,-6,8,7,6,2,-10,2,7,6,-9,-6,-9],[9,-7,4,10,2,-3,-9,10,10,8,-7,-9,-6,4],[-5,8,-6,3,-8,9,2,-10,-10,4,2,9,-8,4]],[[9,5,8,-9,10,-4,6,10,-7,3,-3,-5,-1,-4],[-5,3,6,-9,3,9,-10,4,8,8,-6,-3,7,6],[4,-7,10,-6,-9,-1,1,-6,4,-8,3,10,-6,10],[2,-3,8,7,9,-4,-8,-1,-4,-9,4,-3,-5,8],[-5,-9,6,3,-2,-4,6,1,3,-3,6,5,3,-9],[-10,-2,-7,4,-2,7,-9,-7,9,9,8,8,3,-8],[-5,5,-5,-2,9,-6,-3,7,6,-9,1,-8,9,5],[-3,-8,-1,4,3,8,2,-5,9,-8,-5,1,-4,-7],[6,5,-6,-8,10,-2,-9,-5,6,-9,9,9,6,-1],[8,-3,1,-6,3,-3,7,5,6,9,9,7,7,5]],[[-4,2,-4,8,3,2,7,10,-1,-2,-7,10,-10,6],[-1,-9,-7,10,-7,9,-2,9,-4,-5,-6,-1,9,10],[8,-7,9,7,10,-9,4,9,7,-5,-7,-8,-7,-5],[-10,-6,-3,9,-10,7,-2,4,-6,-1,-1,6,7,10],[-2,-8,9,3,6,3,-8,3,9,-5,-2,-8,5,10],[7,-3,6,1,7,9,-6,1,-5,4,-4,8,5,1],[-9,1,-3,-3,8,-6,8,2,10,-7,-8,10,10,-7],[4,-7,1,9,2,4,-7,-9,-8,10,4,4,10,3],[-1,-7,10,-10,-1,4,-10,-5,9,-6,7,-8,7,3],[7,7,10,-5,-5,-3,3,-10,-8,-1,-3,5,-5,10]],[[-4,-7,-1,-10,-8,3,-7,2,4,2,8,-10,-2,-10],[-7,-9,3,1,-2,-5,6,-6,4,5,-9,-1,-2,-8],[5,1,8,2,-8,5,6,2,10,4,-3,4,-6,9],[-6,-4,6,-3,-7,-8,-10,9,-5,-5,-7,10,10,4],[-1,-5,1,-9,7,1,-7,-1,2,-10,-10,-3,-7,-9],[-7,2,5,4,-9,10,5,9,2,8,9,2,-6,-6],[-8,-8,7,2,1,7,8,-5,-1,-6,6,7,-3,-5],[-6,2,8,-8,1,-9,7,-4,3,10,6,9,2,-7],[6,6,7,-5,-9,9,6,-4,-4,-8,8,3,5,-5],[-7,-4,8,-5,9,9,-5,-9,6,4,2,7,1,5]]], dtype = "int8")#candidate|11187|(14, 10, 14)|const|int8
bop_11188 = relay.less(var_11186.astype('bool'), relay.reshape(const_11187.astype('bool'), relay.shape_of(var_11186))) # shape=(14, 10, 14)
output = relay.Tuple([bop_11188,])
output2 = relay.Tuple([bop_11188,])
func_11196 = relay.Function([var_11186,], output)
mod['func_11196'] = func_11196
mod = relay.transform.InferType()(mod)
var_11197 = relay.var("var_11197", dtype = "int8", shape = (14, 10, 14))#candidate|11197|(14, 10, 14)|var|int8
output = func_11196(var_11197)
func_11198 = relay.Function([var_11197], output)
mutated_mod['func_11198'] = func_11198
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11568 = relay.var("var_11568", dtype = "float32", shape = (3, 4, 11))#candidate|11568|(3, 4, 11)|var|float32
var_11569 = relay.var("var_11569", dtype = "float32", shape = (3, 4, 11))#candidate|11569|(3, 4, 11)|var|float32
bop_11570 = relay.power(var_11568.astype('float32'), relay.reshape(var_11569.astype('float32'), relay.shape_of(var_11568))) # shape=(3, 4, 11)
bop_11575 = relay.floor_mod(var_11569.astype('float64'), relay.reshape(bop_11570.astype('float64'), relay.shape_of(var_11569))) # shape=(3, 4, 11)
uop_11578 = relay.log2(bop_11570.astype('float64')) # shape=(3, 4, 11)
func_2670_call = mod.get_global_var('func_2670')
func_2674_call = mutated_mod.get_global_var('func_2674')
const_11609 = relay.const([-1.981060,-7.583129,-2.108085,-5.353419,2.699538,-8.600181,-3.099731,-1.824778,5.652349,-2.015191,2.534982,5.792162,-1.983611,2.160767,-3.580820,-6.811684,-4.440095,-3.349932,-6.683754,7.731676,-6.256131,-8.440476,0.731360,8.697014,8.486315,7.636787,-9.150038,-3.068695,5.665558,-8.798896,9.483061,4.011543,9.107167,-8.437038,-1.442606,0.424601,1.168042,-9.638511,5.195604,-0.242630,3.935425,2.776009,-1.695768,-1.621345,0.986349,-9.590092,4.613643,4.153446,5.357410,4.006381,8.840056,-3.346875,-3.284070,-2.017475,-7.228859,8.728393,-5.171960,9.535610,-4.414647,-0.270329,-6.257919,-7.572159,-8.144272,4.881171,1.718576,-3.612662,9.843244,-9.900546,8.133758,6.673439,1.358119,2.933284,-0.123445,-8.654096,-5.102479,-3.651903,6.031916,9.862482,-4.720570,-8.255830,4.477308,4.778931,1.811429,-7.419321,-1.175406,3.646869,-5.242017,3.758868,7.926833,-7.836233,-0.420777,4.721727,1.317146,-8.438929,8.959464,-0.385705,3.771910,6.890288,9.600097,3.215794,-3.711069,1.434915,4.883467,4.631249,-7.968439,-4.760973,-5.665794,3.389573,-3.075482,-5.552312,-8.774049,-8.833527,-1.400243,-8.455483,-5.779669,8.649998,-7.778207,2.407056,5.225752,3.168855,-4.208028,-5.671034,7.563906,6.732400,8.377890,4.050798,-0.948162,5.436410,6.535003,-7.843366,1.868963,-5.068366,-0.629011,7.351829,-2.117861,8.534987,3.334551,-8.765297,6.923463,-6.435937,9.315231,-8.675906,-9.164752,-6.532909,-4.454515,7.972050,-5.807924,3.538577,7.194420,-9.027580,6.304026,0.640402,4.994656,0.792662,8.471961,-3.118875,5.375146,-1.403562,-1.382338,-6.327747,4.365885,2.555945,9.451279,-7.424853,7.224756,9.032108,-3.573846,3.212589,-5.632898,5.388665,4.733330,-9.442460,-4.039196,-9.965759,5.476049,2.933325,-8.978560,-2.687903,-7.113260,-9.120667,3.390949,-0.534444,-4.781482,7.823813,4.344078,-9.800348,-7.481837,4.867986,9.128004,-5.655977,-1.291128,7.992794,-6.164017,5.924115,-8.314365,-3.840866,5.817755,-9.240277,5.055279,-9.206963,-1.214479,5.006056,6.788145,8.747808,-9.817709,7.632516,-4.625081,6.316727,-1.366855,4.227816,-8.151089,-9.635965,-6.041557,-8.387511,-5.612303,-1.586890,0.598409,-3.398828,9.286633,-3.851537,3.110050,-9.659748,-1.859740,-0.055632,-4.513300,-4.917972,6.520278,-7.217890,1.664705,9.670256,9.925820,-0.544554,5.406601,9.116210,-3.039911,-7.017748,6.090478,6.256658,-4.415708,-1.050945,5.720516,-2.799810,8.619339,3.219363,1.715916,5.342116,-9.902551,4.783891,-9.164282,-1.380947,-5.643488,-8.165954,-4.979457,-9.368056,5.518039,7.910390,7.660989,5.847708,4.312051,6.513309,-4.465835,3.949291,-5.219130,-0.832141,-7.352083,1.810842,-7.073384,-9.542127,-7.577003,0.658314,-1.586041,-4.442359,-6.848634,-0.195704,-9.026156,-3.814079,-5.629793,-3.950980,9.237846,3.360337], dtype = "float64")#candidate|11609|(280,)|const|float64
var_11610 = relay.var("var_11610", dtype = "uint8", shape = (4, 100))#candidate|11610|(4, 100)|var|uint8
call_11608 = relay.TupleGetItem(func_2670_call(relay.reshape(const_11609.astype('float64'), [7, 10, 4]), relay.reshape(const_11609.astype('float64'), [7, 10, 4]), relay.reshape(var_11610.astype('uint8'), [400,]), ), 3)
call_11611 = relay.TupleGetItem(func_2674_call(relay.reshape(const_11609.astype('float64'), [7, 10, 4]), relay.reshape(const_11609.astype('float64'), [7, 10, 4]), relay.reshape(var_11610.astype('uint8'), [400,]), ), 3)
output = relay.Tuple([bop_11575,uop_11578,call_11608,const_11609,var_11610,])
output2 = relay.Tuple([bop_11575,uop_11578,call_11611,const_11609,var_11610,])
func_11612 = relay.Function([var_11568,var_11569,var_11610,], output)
mod['func_11612'] = func_11612
mod = relay.transform.InferType()(mod)
var_11613 = relay.var("var_11613", dtype = "float32", shape = (3, 4, 11))#candidate|11613|(3, 4, 11)|var|float32
var_11614 = relay.var("var_11614", dtype = "float32", shape = (3, 4, 11))#candidate|11614|(3, 4, 11)|var|float32
var_11615 = relay.var("var_11615", dtype = "uint8", shape = (4, 100))#candidate|11615|(4, 100)|var|uint8
output = func_11612(var_11613,var_11614,var_11615,)
func_11616 = relay.Function([var_11613,var_11614,var_11615,], output)
mutated_mod['func_11616'] = func_11616
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11919 = relay.var("var_11919", dtype = "float64", shape = (10, 10, 8))#candidate|11919|(10, 10, 8)|var|float64
uop_11920 = relay.sin(var_11919.astype('float64')) # shape=(10, 10, 8)
bop_11938 = relay.minimum(uop_11920.astype('float64'), relay.reshape(var_11919.astype('float64'), relay.shape_of(uop_11920))) # shape=(10, 10, 8)
bop_11941 = relay.logical_xor(bop_11938.astype('int32'), relay.reshape(var_11919.astype('int32'), relay.shape_of(bop_11938))) # shape=(10, 10, 8)
func_8904_call = mod.get_global_var('func_8904')
func_8906_call = mutated_mod.get_global_var('func_8906')
var_11955 = relay.var("var_11955", dtype = "float32", shape = (1920,))#candidate|11955|(1920,)|var|float32
call_11954 = relay.TupleGetItem(func_8904_call(relay.reshape(var_11955.astype('float32'), [1920,])), 0)
call_11956 = relay.TupleGetItem(func_8906_call(relay.reshape(var_11955.astype('float32'), [1920,])), 0)
output = relay.Tuple([bop_11941,call_11954,var_11955,])
output2 = relay.Tuple([bop_11941,call_11956,var_11955,])
func_11960 = relay.Function([var_11919,var_11955,], output)
mod['func_11960'] = func_11960
mod = relay.transform.InferType()(mod)
mutated_mod['func_11960'] = func_11960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11960_call = mutated_mod.get_global_var('func_11960')
var_11962 = relay.var("var_11962", dtype = "float64", shape = (10, 10, 8))#candidate|11962|(10, 10, 8)|var|float64
var_11963 = relay.var("var_11963", dtype = "float32", shape = (1920,))#candidate|11963|(1920,)|var|float32
call_11961 = func_11960_call(var_11962,var_11963,)
output = call_11961
func_11964 = relay.Function([var_11962,var_11963,], output)
mutated_mod['func_11964'] = func_11964
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11975 = relay.var("var_11975", dtype = "float32", shape = (4, 9, 13))#candidate|11975|(4, 9, 13)|var|float32
uop_11976 = relay.log2(var_11975.astype('float32')) # shape=(4, 9, 13)
const_12000 = relay.const([[[0.290918,-1.447370,-0.350887,-5.411609,-6.342053,-5.657957,-3.848990,-8.966641,-0.119355,5.337253,-9.631397,-3.819650,-4.232135],[-7.138878,8.197859,0.756696,9.718601,-8.928512,0.640973,3.912933,3.687606,5.527949,-9.854519,-3.356191,-5.130902,-0.017625],[-9.006464,5.497982,2.397062,-9.627350,6.229111,-8.576951,6.437961,-9.356626,6.575230,-6.842793,-1.208804,-2.563031,-3.757466],[7.562587,-6.322214,3.736978,1.173842,1.083214,-0.178612,2.497611,-8.786770,-1.484830,-9.186296,-6.238096,-8.116062,6.416734],[-9.181682,-7.708075,-6.090543,9.014871,8.765417,1.037815,2.542610,-1.213761,-8.722751,-9.961937,3.574472,-9.299979,8.953334],[3.263993,4.331577,-2.656749,0.310072,-6.610200,5.864953,-6.816937,-5.975303,7.369201,1.359566,-5.115541,7.819308,-2.579112],[1.995031,8.086378,2.666021,5.117398,3.758136,-9.281554,-8.426440,-5.575768,-4.044018,-7.448373,-8.134010,-4.456950,3.676821],[6.608345,5.346027,9.238638,-7.708267,-5.579965,-9.978518,-7.247894,6.498920,-4.773224,-9.614639,0.232266,7.898072,5.570064],[8.659515,7.040380,-1.195033,-7.521332,-7.794931,9.782789,-1.599083,-6.534027,1.778092,-8.028862,1.351062,-2.700829,6.223531]],[[-8.710391,7.860220,-6.028014,-0.402741,-9.852086,-4.410444,-2.159295,-4.724848,1.808387,9.439021,7.492919,-7.433210,-0.236015],[-2.567969,0.098812,-0.081704,7.969357,-0.729557,9.407410,3.887515,2.975253,-0.503668,6.548261,0.833519,3.151392,-9.241269],[5.878248,-2.184003,9.176988,-0.063875,-5.604229,-4.709127,9.342658,7.430790,5.613545,-7.707990,-9.150880,2.426932,1.211862],[-5.333972,0.423538,-5.653369,7.119933,-2.782875,8.305196,-2.458729,-5.566825,3.596947,1.284815,-6.309214,-2.051726,7.787219],[2.151202,-5.660389,-5.989558,3.973291,5.757181,-6.801244,-0.656285,3.191606,-1.710242,4.321885,3.564772,-8.891406,7.684111],[5.590060,3.017246,-6.218034,8.248880,3.064422,1.094808,-3.762209,-6.318642,2.268731,0.845375,1.641781,-6.610261,-9.746259],[2.052917,-5.939880,8.960816,-8.201783,0.769507,9.369858,9.079309,-2.314920,7.107125,-5.300096,0.220396,-8.118187,-2.003864],[-2.760002,-5.019828,-6.685984,7.299820,-0.524691,8.305791,6.406596,8.154720,6.326472,-1.626963,8.748110,-9.248345,2.651812],[-3.921624,1.136154,0.820027,9.318832,-6.133107,-3.903419,9.622985,4.977430,4.142588,3.493808,5.237185,-4.457427,-3.104283]],[[-4.370967,8.550807,-3.178537,4.118947,-1.176535,-2.805243,3.405784,-5.484711,-2.441943,-1.988408,-1.409634,0.685320,6.529363],[-6.834061,-8.067264,9.563800,-5.299628,-8.578240,-0.896296,-9.531668,1.505552,1.379346,5.066630,-4.743140,8.857269,3.045429],[-1.288058,5.170940,-8.119651,0.652067,-8.167005,9.410975,1.034117,6.084804,5.236263,9.182141,-1.844138,9.966855,-3.997685],[-1.931243,9.734735,3.879834,-4.774933,4.503764,-4.008226,3.170142,2.321173,8.932331,-4.693162,6.606649,-6.335489,-8.265737],[3.779846,9.088749,4.514164,7.607067,9.518634,6.059732,1.342008,-3.267387,2.082493,-8.338316,-5.688571,-0.320883,-9.453019],[9.843233,-0.457040,-4.849025,3.796439,0.725722,4.872355,9.178019,2.923292,-2.334282,2.814985,-0.031020,-8.120518,-8.708802],[6.402946,1.717879,-8.625566,-9.109793,9.973364,-4.607483,-1.419051,3.359643,-5.635419,3.114408,1.049012,-1.471122,-5.447968],[-6.556572,1.643725,-0.409529,9.440878,-7.404906,-5.109997,-3.459421,1.009745,-8.047671,-9.564066,1.981232,1.822292,-8.565632],[-1.636685,8.087617,5.523036,0.576067,-9.521169,0.658960,-3.152302,1.123950,2.654945,-8.772683,-3.873185,-3.816068,-5.818617]],[[6.535090,-0.127492,6.720385,-5.028576,-4.650486,-2.190673,-4.834371,8.283221,-0.875686,-2.389195,-4.641179,8.292316,-6.858117],[0.770015,-1.268083,6.144792,7.420510,4.033438,-0.686531,-9.647908,5.256219,9.642082,6.841862,-4.990617,-1.812523,-7.289258],[-9.661935,9.241634,9.697053,0.752756,-5.311080,-3.291413,9.013256,-1.115519,6.784990,-8.848600,7.604446,3.079388,-5.968287],[-4.886528,-6.874017,5.681026,-1.074741,6.325474,4.708154,9.711886,0.615943,-9.509056,8.941859,4.134418,2.420415,-5.735028],[1.468038,3.379050,5.809120,-2.522941,-8.146737,-4.215423,-4.899284,0.026928,-1.783752,0.797787,-4.210108,-2.351958,4.909972],[-9.965430,7.668774,6.992680,-6.563434,-2.691717,9.021493,9.287922,-5.300411,-7.483426,-2.877744,0.925917,7.305513,-2.437424],[-5.044613,6.294167,-5.547898,-1.645379,-5.587708,-8.273085,-8.568635,-7.065529,8.888266,-2.025544,7.894657,-7.523819,-9.996336],[3.160457,9.762654,5.781213,-5.387761,4.885141,-6.719121,8.369711,1.398683,-9.612943,-6.728382,8.468820,-5.491732,-3.244410],[8.929650,8.850235,-3.943106,2.179916,4.281488,4.241566,5.737579,-3.351408,-7.589133,1.995093,-8.200743,9.348612,-4.900725]]], dtype = "float32")#candidate|12000|(4, 9, 13)|const|float32
bop_12001 = relay.right_shift(uop_11976.astype('int8'), relay.reshape(const_12000.astype('int8'), relay.shape_of(uop_11976))) # shape=(4, 9, 13)
output = relay.Tuple([bop_12001,])
output2 = relay.Tuple([bop_12001,])
func_12009 = relay.Function([var_11975,], output)
mod['func_12009'] = func_12009
mod = relay.transform.InferType()(mod)
mutated_mod['func_12009'] = func_12009
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12010 = relay.var("var_12010", dtype = "float32", shape = (4, 9, 13))#candidate|12010|(4, 9, 13)|var|float32
func_12009_call = mutated_mod.get_global_var('func_12009')
call_12011 = func_12009_call(var_12010)
output = call_12011
func_12012 = relay.Function([var_12010], output)
mutated_mod['func_12012'] = func_12012
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12975 = relay.const([[[-0.712423,2.864529,8.974246,-0.227631,5.604014,-8.151674,4.830418,-3.829140,-8.985954,-3.534970,4.612724],[-1.822913,2.149426,5.358663,5.084187,5.843717,5.874133,0.502198,-3.982630,-6.031035,7.199479,-3.079614],[7.561938,-8.638165,1.519630,-0.013579,1.763454,-8.499977,5.088235,1.133347,2.494458,-4.584137,-5.860286],[7.812822,3.335898,-3.651920,-4.377332,6.987929,-3.204559,-1.552447,-0.726483,-2.257408,8.542854,1.972541],[-2.570468,-9.867224,5.006722,-6.357505,-1.562566,-6.546617,-8.535661,-9.587889,2.841415,-0.621791,0.987069],[5.254869,1.910800,-2.186351,7.643414,5.192471,-8.304847,7.786731,-8.612440,0.662667,5.098236,8.843121]],[[6.168331,3.587264,3.277732,-8.787305,-3.232616,8.436526,6.095141,-7.400928,1.819106,-5.093350,4.302418],[4.732938,2.393905,-9.297070,-8.390479,-6.923333,0.788414,7.947265,-1.000328,-9.165812,0.749720,-2.099602],[9.058602,4.887288,7.002079,-2.905454,0.854878,-1.442595,0.705538,-5.307274,-4.950931,1.641369,-0.067981],[5.964364,-6.538585,0.997872,4.684535,-3.264759,-1.362407,7.470122,6.552646,8.828800,0.780479,2.241853],[-3.873828,-5.118143,7.450687,7.552526,-4.295071,-4.123936,-2.522136,4.350100,7.477878,-2.218393,9.636411],[0.096575,1.090768,-9.091292,5.982175,0.318829,8.887596,-1.880139,7.197137,-0.231903,-2.115414,-7.584945]],[[-6.695446,-8.644314,8.761459,6.354761,-9.846584,5.642779,0.561060,-6.580298,-1.079529,8.088264,-7.199222],[-1.625450,8.542995,5.328525,3.608266,-1.014759,0.775601,7.522754,4.527483,-7.032974,-3.999317,5.008021],[0.117210,-2.198334,-9.462197,1.904602,2.416324,-3.646852,-2.764268,3.552033,-1.423419,0.783075,-7.883695],[-3.681214,7.098455,-8.642567,9.739631,-0.880228,7.508109,-0.167306,-6.925084,-0.362254,5.557575,-0.358641],[1.664174,3.426328,9.399325,9.663669,9.639186,5.285567,-3.942027,-9.164316,1.890965,-1.490446,7.263989],[-2.393456,-6.164643,-9.119119,-3.739206,3.131727,-9.280407,3.416784,5.804574,3.162765,-4.102495,-0.575150]],[[-2.116124,-2.043786,7.485747,7.328610,0.035426,-3.069749,-4.683234,5.014091,3.368284,-5.908076,4.331344],[6.948371,5.024271,-2.735486,4.293353,-2.435064,2.015584,4.512279,-6.337253,-3.321213,7.696122,4.959792],[6.664587,-6.539978,-1.829431,-1.242488,-0.888973,-7.192880,-7.247971,8.201760,7.176866,-7.413322,9.021604],[4.941808,-0.561311,9.444650,-5.501767,2.211937,-5.109754,-6.601444,6.685452,-3.043935,-8.903044,3.137353],[3.914646,-9.559309,-5.595964,-5.735343,1.651294,2.314917,1.506623,3.833134,-2.400383,2.191843,-3.826352],[0.853687,-6.631677,0.667521,-1.530094,2.529258,6.619607,4.946136,-6.564123,4.198102,0.853781,1.880727]],[[-7.353583,2.804419,-8.166095,5.734486,-1.196228,-7.840642,-8.359643,-6.421629,-0.040457,5.057998,9.290958],[0.954302,-7.714341,6.520317,-2.973811,-0.647347,6.241454,8.605158,-5.247418,-5.379446,9.121581,4.256149],[-4.894445,-3.778110,4.594914,3.522162,-5.687100,6.353624,6.287304,1.398607,7.326479,-8.472839,9.548966],[-1.255343,-4.149275,-2.186865,6.203199,-2.905498,2.316637,-3.649389,-2.394191,-8.738303,6.184629,1.335855],[-0.735629,-4.270158,-0.828417,3.936914,-8.703742,1.062558,-6.340500,-6.446367,1.721234,-4.385539,0.464565],[3.210082,-6.431978,5.036337,0.543763,-2.992064,5.702855,-1.284267,-4.564344,5.127730,9.749747,8.656734]],[[-5.272697,-8.385380,-5.613073,1.257165,8.995938,5.562837,-5.020658,1.047759,3.285130,1.599589,-6.984163],[-1.887076,9.468174,2.296728,-8.994280,7.065487,-4.699766,-3.932038,-0.640772,3.046641,6.904460,7.836481],[3.929553,0.219630,-8.906677,1.422975,-0.999469,3.164663,9.404286,9.889035,-3.001467,-1.240446,-1.517312],[4.074807,-5.329261,-5.896258,-3.266039,3.590443,4.916718,-2.735921,-4.247852,-1.413251,-2.579730,-5.347525],[6.945714,7.552175,-9.182100,-2.712767,2.212355,8.721759,-6.594198,6.371730,4.352954,-7.056423,4.413114],[5.811405,-9.515158,0.667265,6.678820,-3.061278,1.562922,-8.003901,-2.344163,-0.224374,3.554946,7.046291]],[[7.712607,-7.956135,-7.397015,0.923232,6.204011,7.544420,7.279678,-6.238215,-0.538066,0.686482,3.795161],[-9.423239,-7.357719,4.332794,-5.024386,-4.400535,8.066106,7.422788,6.842565,1.069519,7.432802,9.137953],[7.164542,1.285240,-4.139369,6.186331,1.106766,5.497163,-6.148507,6.298105,-6.453971,6.634189,-5.007799],[3.377901,1.549113,-5.914004,6.201649,0.600398,-4.753084,-6.771631,9.899946,-8.429083,4.081740,7.639533],[-4.286974,2.265571,-0.426798,-6.949398,4.759472,-9.634162,-2.593959,7.230055,-7.122610,7.949925,5.678285],[-2.872822,3.983959,7.607683,-8.236451,1.084234,5.557582,0.975311,1.914989,-6.257644,2.126089,6.629711]],[[-1.171695,7.348790,-5.581234,5.995296,5.945513,-0.445910,-4.963996,1.473427,-7.166885,4.972036,0.929947],[0.500585,-9.359918,9.291728,9.788832,1.123702,6.510615,-8.307058,5.115620,-5.189321,8.824523,-0.906312],[-8.424941,4.264990,-8.786976,4.587374,6.117674,-4.908353,-7.245959,-8.752713,-4.989177,2.363875,-4.722350],[9.773004,9.668145,-0.363609,5.547681,-9.195630,2.371004,-0.212863,-2.266246,0.125348,8.661612,2.883086],[-8.857928,1.502026,-3.685073,-6.437287,-6.358638,-6.288261,4.747695,0.617106,8.276301,5.539843,9.067986],[-8.168443,2.438225,6.481442,0.223871,-7.395031,-5.511669,1.379497,0.996334,-1.485242,1.160950,4.653414]],[[5.966045,1.013061,8.013373,8.649023,1.350196,-7.560639,-9.440261,0.325540,0.907824,6.838090,9.187883],[-3.745622,-4.654126,-3.703402,0.495037,0.077207,-3.353233,-1.611664,5.549522,-5.602010,2.152938,1.892194],[3.416929,-7.952033,-1.576078,-0.017500,-5.762596,-6.852236,2.743498,-6.730230,8.898873,-5.102295,0.453295],[8.538293,-0.347517,7.165277,-8.855217,6.525046,3.316848,-3.557852,3.487111,2.257630,2.307561,0.912698],[-1.743838,-9.176627,2.369625,-7.848328,1.331587,1.173547,3.567140,6.452572,1.105529,1.040449,-1.723575],[-8.296209,3.646101,2.967970,-3.240765,6.123687,0.171509,-9.178935,-6.880768,8.972441,-4.279259,-2.256128]],[[8.794683,3.177546,-9.666510,1.385229,8.270777,7.795640,2.590182,9.147471,9.727341,-9.823334,-0.327490],[1.427476,3.833702,-9.598652,3.280480,-0.082693,3.018973,6.352343,-7.203282,-9.623356,-0.184285,-1.115185],[6.193797,6.986645,2.858293,0.792969,-2.078715,-3.979278,4.570163,7.522386,8.883804,9.784230,-2.363385],[3.977889,3.974212,-6.350338,0.812818,1.917285,-0.061900,7.907894,-6.369476,-5.496257,2.471580,7.410394],[7.133840,1.094208,-3.281964,7.625049,7.031842,7.863403,9.304061,-5.181846,3.922294,6.997718,4.306100],[4.684557,1.020688,-6.055473,-0.002873,9.927776,0.898841,8.121359,6.309845,-7.448403,7.182858,8.794243]],[[6.593644,4.807331,8.332062,-0.340294,2.951603,-7.909256,9.574764,0.974345,-9.237865,-9.474644,4.377016],[3.281219,-4.633971,1.236184,-6.554397,-9.043599,-4.896918,-6.386980,-8.884668,-3.315371,-9.324384,-0.394490],[-5.337706,9.719786,-5.232559,-7.534910,0.808879,-2.098561,8.874088,9.728131,-6.346641,8.213330,8.591272],[-4.489273,-9.330238,9.837926,-9.966555,9.566530,0.859766,9.037433,-0.590301,5.539783,-0.577668,7.047053],[4.214854,3.438794,0.069791,5.163998,-0.321771,-3.799425,-3.037325,0.328715,-9.916585,4.848474,4.908452],[3.921634,-2.213169,-8.817237,9.479314,-5.809361,-4.652828,-0.262144,-5.052012,8.902397,-3.750665,-3.158362]],[[1.000889,5.858632,-9.850536,-5.711165,8.687199,2.003287,-6.850405,-9.167210,2.565382,5.103942,-1.866177],[7.245261,0.663385,3.686092,4.019746,-7.542078,8.133652,-3.716877,3.772635,-0.196592,-0.372133,-5.767342],[2.321202,-1.797953,-9.872696,-5.656642,-3.208831,1.238281,-7.275778,6.239199,-5.469205,0.481927,7.433370],[2.199768,-6.481307,1.638332,6.712948,8.427715,3.083520,-8.748741,9.714702,-6.912470,-7.924680,4.651050],[3.824906,-9.788882,7.784846,5.384754,2.600666,9.156096,-6.989832,1.170229,-2.235940,-3.145733,-1.643446],[3.960142,-8.093340,2.556226,-0.121529,5.231765,2.841443,5.096687,2.077210,6.249144,-4.371564,-8.887077]]], dtype = "float64")#candidate|12975|(12, 6, 11)|const|float64
uop_12976 = relay.asin(const_12975.astype('float64')) # shape=(12, 6, 11)
func_1225_call = mod.get_global_var('func_1225')
func_1228_call = mutated_mod.get_global_var('func_1228')
const_12983 = relay.const([4.199070,-5.242206,-9.713213,-4.691058,5.238036,-4.848842,-4.501751,-5.284993,-2.565877,7.841984,-4.436011,-0.040969,-3.643291,2.977092,-1.100704,5.315024,-9.426496,-7.884061,-6.045862,-7.192419,-9.773813,-7.112180,-0.318234,7.259490,2.553860,7.381551,1.860495,6.759672,2.450543,-0.193582,-9.400463,5.752357,9.751617,2.167708,-0.498688,2.780736,-6.696267,-6.663469,-1.830637,-3.285496,-2.515506,4.724805,2.360788,3.873533,6.556064,-7.776831,7.756585,-5.894243,9.868618,-9.798533,-4.411357,-0.821381,6.721773,1.077158,4.087765,-6.236695,-8.905999,8.312975,-6.136788,-1.192450,-5.611343,5.275257,-7.813270,-5.016741,-0.044199,6.312200,-8.987637,1.982373,-7.903341,2.843825,-0.904941,4.627310,-7.509311,1.750632,1.167536,-8.561015,-8.799046,0.400435,-9.452497,8.264514,-3.451365,4.070350,-7.629756,4.601508,7.689579,-0.029177,-2.849497,-8.789396,5.000907,6.757990,7.258370,-8.607685,-0.156584,-1.606807,-1.761638,3.572510,4.878816,2.148867,3.156541,-3.270848,-3.159791,8.266045,1.925579,6.030675,7.410364,3.313257,-2.280692,-8.391534,-0.254622,6.558319,-2.523217,8.722617,5.975019,-4.143185,5.522541,-6.345532,9.191922,-9.228827,0.456298,7.325735,2.278647,-5.449031,2.626050,-5.266962,6.496808,-5.557924,-4.685012,5.937084,-7.874577,-2.294053,2.636154,6.913188,-5.566361,4.459160,8.999327,-0.115667,0.221638,4.740275,-6.577984,-5.709248,6.872511,3.249976,2.705345,-9.389760,-7.167246,4.330220,4.624288,0.599499,3.782870,0.108182,2.618085,3.504148,-6.814588,0.317284,-6.974331,9.381924,-0.929831,9.764418,9.974470,-5.417150,-7.940734,7.728537,-3.068718,-8.926513,5.612451,7.583446,0.224887,-3.773810,2.752602,-9.192597,6.495077,9.838856,1.054003,4.375615,-2.081018,-1.280185,-6.678837,-7.205494,-5.854686,-1.916096,6.515021,5.895508,-5.886424,-3.862066,9.800740,7.678915,-7.379331,9.097598,2.794229,0.883055,-4.008825,-5.658831,5.676345,7.996352,7.179701,-4.486015,3.126347,-8.885044,6.118262,8.224982,9.626484,8.510246,-3.800918,3.860962,-9.111441,1.337229,1.602486,2.210956,0.656531,-5.179396,-3.890517,7.539894,-6.026351,6.464118,-9.775497,2.389189,3.436856,-4.817049,0.440251,7.682115,-4.512431,-6.317039,-0.356542,-5.165891,-8.891789,1.649504,5.105155,5.717796,-9.783436,4.252351,7.660899,-9.894752,-2.353652,-7.098464,7.794571,4.313590,2.769668,5.874015,1.601217,9.155021,-1.595133,-6.011193,7.790375,-6.019570,-1.066498,-7.229119,-4.713660,-2.161130,3.124007,-8.599490,-5.657131,-4.019422,1.590401,6.167444,-3.070148,-3.695410,2.415231,-9.463357,-3.500416,-9.700672,8.750080,0.024860,-8.228735,-7.257487,-7.556914,-9.740694,-0.786608,-6.997076,-4.488138,-1.023947,-9.832327,4.545342,3.493118,-3.020064,-4.431375,-0.445633,-9.785682,7.993559,0.941999,-4.977419,-8.446023,-3.713955,-2.903831,-9.956601,-7.025090,9.444481,-8.748333,6.876181,-7.062234,6.414080,-7.649319,-9.177208,4.931139,4.747409,2.990202,7.343451,-6.895420,-7.122779,-7.229246,3.904715,7.493947,-8.313948,-2.499088,2.884508,7.346278,8.937883,-0.013295,-8.239600,-5.053607,-3.503079,-1.505357,3.865318,1.540192,2.511348,1.938977,3.389078,2.004905,-1.296301,8.583098,-9.215140,-0.016337,-6.758576,-6.288539,3.473428,0.952477,-8.978946,7.705015,-0.482996,-2.037229,-5.148411,1.217025,-1.308043,1.722869,-4.967468,2.410889,-7.969686,-1.821280,-3.952681,1.193864,9.044946,-3.219022,-4.403211,-7.214137,-0.723354,-9.981491,-4.407916,-8.397373,-2.316531,2.992319,-7.173031,-8.317316,-7.840410,-5.479470,3.505038,-0.078152,-3.316446,-8.278320,-5.824553,5.067987,3.742691,-3.294366,3.428399,0.945913,-0.718084,-6.667171,1.435797,3.513024,-0.011940,-3.880878,-5.123691,-5.252098,1.856801,4.823476,3.191282,3.479427,5.407961,-7.504093,-0.071977,-8.829118,-5.011726,-0.484358,3.262666,-9.623399,1.843443,0.726001,4.124446,-1.506989,5.319425,1.375922,-3.442943,6.318431,-5.898979,3.078398,1.792812,5.654168,-7.377792,0.349106,-6.286259,1.174519,1.607704,3.935918,6.848685,8.528779,4.896913,0.902350,7.950049,1.953940,0.931577,3.402759,3.987643,-7.940442,-4.880376,9.242389,6.883707,-7.448511,-4.857232,-0.330627,7.410266,-5.256784,-0.499995,-2.659673,-2.802951,4.968414,-2.153420,8.216032,5.281116,-6.383064,3.533847,-3.934020,-2.117541,5.627058,-7.145480,-1.780213,-9.225982,3.588248,1.078204,-7.301556,9.196233,6.276843,-2.117900,9.091140,-7.919295,2.459477,-0.530296,5.197026,-7.293718,2.644326,-8.767469,-9.299631,-4.719325,6.946469,-9.028885,6.906730,0.789911,5.537298,2.708964,7.271749,-6.673093,-8.448853,8.167038,-2.034931,-2.624091,-7.946102,3.274147,8.867924,-0.346567,2.969984,3.881860,7.985266,4.868792,-3.059570,4.969492,8.332324,7.987521,-7.888639,6.387784,-8.611601,-8.828048,-8.019555,-2.159433,1.467982,-4.185064,9.335875,-1.367814,-0.279174,8.159325,-9.122213,-8.898175,4.398790,0.389923,-5.759566,-3.295440,4.857555,-1.312386,-8.307006,2.711714,5.081889,9.163635,0.041681,7.814406,7.692189,1.264058,-8.005478,1.032734,8.557067,8.277290,2.304652,-7.869717,2.943862,-9.236099,1.188674,6.886117,8.403867,0.428240,-0.033644,-5.704087,-2.120211,-5.764619,-3.530925,-8.409837,-9.773339,4.177470,5.921820,-4.110996,-9.797748,-8.451834,3.000053,6.685019,-4.809993,7.730170,3.564531,9.632427,8.224458,-7.858015,3.546483,1.473930,6.114246,-6.480266,4.217105,3.414812,7.507433,4.578617,3.884461,-5.908787,-0.131240,9.998079,6.387858,6.259677,-0.411110,-5.508423,-8.498251,2.556350,3.663344,-4.287591,8.672510,-7.797668,0.143125,8.792170,-8.681760,5.249707,9.285606,0.840154,5.134544,-6.224088,-6.712657,0.721453,-9.965215,-2.726637,-3.649590,-3.815170,-2.014230,8.424017,6.737567,7.831614,-8.665187,-8.190834,5.405334,-8.358347,-6.661336,-9.995876,-2.827535,8.313743,-0.895670,-6.635971,-7.970023,-7.379847,8.447117,-9.594694,-4.367290,8.914212,-5.455420,7.041893,1.436920,-7.426005,-8.861242,-9.236570,9.529788,2.361193,-1.388546,-9.509644,8.322880,0.317046,-7.966234,9.396176,1.653049,0.158325,-1.774831,1.648603,5.544278,7.146287,-7.118582,-0.612318,9.616289,-0.963263,3.114145,-7.907647,5.288893,7.090787,5.261251,4.866113,5.988322,0.607059,6.642024,1.509349,-2.514092,-8.389415,3.839325,-3.483806,-4.571784,-1.390017,-2.487034,-1.738848,-5.243822,1.751707,-8.992857,3.874110,-6.523929,0.724753,7.936147,-3.615401,4.797613,7.074831,8.390407,0.378930,-1.207325,8.920120,-5.985099,-3.908324,2.023254,6.098667,-1.948997,-3.799069,1.432812,-0.578048,-4.476743,-6.697731,6.529984,-0.143424,-5.821885,6.857114,2.470345,8.040589,-6.701485,0.226356,1.072761,-1.349453,1.544009,-6.174932,-3.895326,5.725354,8.624910,7.102578,3.703484,5.476601,1.453117,-1.632197,6.502628,8.053696,-6.447506,-5.389582,3.313762,1.446190,2.491417,9.013135,5.876981,-7.555486,-0.824274,5.864230,-5.030607,0.268645,2.748028,-0.472798,8.789855,5.666087,-7.678909,-3.010309,-5.280106,-6.188504,8.270241,7.167656,2.615382,-7.387509,6.571248,6.252777,-8.118018,-1.637593,0.124295,2.109325,-0.408058,-5.205515,-0.263904,-8.313966,-2.592824,-2.201142,-8.853255,-1.159017,6.808057,7.258603,4.358468,-4.386397,-4.899029,7.736395,-8.295122,-5.235714,2.500513,2.566049,8.612365,-7.002097,5.579703,-7.712942,8.785048,1.415198,2.395303,0.897913,9.203583,-5.236999,-2.889436,7.698385,-6.010965,2.452338,-4.703427,8.065976,-6.603720,-4.875050,-6.458004,5.392682,9.940848,5.354052,-2.182070,8.514065,-0.477020,5.101294,-3.447145,1.365722,-9.145959,-8.062209,-3.607603,8.809102,-7.957919,-0.352278,-1.738326,-9.288379,-0.732886,-4.180721,-1.211247,-6.843034,6.570407,-0.221978,7.515658,5.740293,-4.072460,-4.413804,6.167663,-9.029520,6.637727,2.415218,-1.929155,-0.596148,6.740461,0.909638,-7.543287,-6.236910,9.073828,2.619921,4.812241,5.843419,8.141710,-8.628359,8.500807,-3.214475,5.930096,-6.597165,9.750464,-6.553934,4.068221,-6.596391,8.917444,0.547404,9.708864,6.664225,4.893476,8.367095,7.057203,-8.790490,-2.594122,6.309355,-2.376728,6.083275,-1.714076,-4.434911,-0.586208,-2.070944,0.469360,-0.450257,-0.434748,3.322851,-3.846085,-8.757990,-6.439647,-8.315937,2.544869,-7.395354,0.560638,3.122009,0.138618,4.713029,2.643642,-9.389936,-4.182195,0.331505,-0.847442,-4.016990,2.262520,-3.190016,1.747907,-6.463266,6.000344,-6.393537,6.301774,-6.270874,0.350404,-9.125321,2.501100,-4.976075,2.241943,6.831278,-5.319268,0.894126,-4.425828,-7.713957,-9.070996,8.948284,3.817996,9.103537,1.580719,-1.626004,4.208271,4.705488,5.977750,-0.123992,-6.422033,-1.515834,-2.631884,-2.071787,-7.207381,-2.374143,-7.777652,-3.261380,-0.007789,-3.967000,5.460955,-3.214674,9.341057,-7.753711,6.624736,8.633078,-8.300430,0.029932,2.467188,9.968050,-7.443968,5.680240,3.513467,-6.390463,5.516105,-0.123556,4.661803,6.549174,-7.290139,1.548355,4.111738,0.176120,1.050451,-4.194667,3.823962,-5.133550,5.173888,-5.083895,3.720952,-5.535745,4.878771,5.286587,-6.018274,7.444329,-8.216387,-5.352593,9.362014,1.732706,-8.162692,-7.346890,-0.559166,6.147340,-9.764986,-4.588890,6.082592,-8.192428,8.400552,2.325266,-9.133207,1.397237,-5.059764,-7.786630,5.536216,-1.049632,8.179563,0.801150,9.500020,-3.288385,-9.233926,0.648567,6.176239,-2.705208,7.218857,-5.127543,-7.534980,2.113713,-6.964831,2.387299,2.703062,7.172301,-8.592649,-9.833112,-5.650990,7.558484,-6.191299,-2.406518,-6.852185,-2.408547,-8.946124,1.960505,-2.106475,4.626837,7.323240,9.511129,-2.150835,5.862143,8.890817,-1.740079,-8.527184,3.315525,-9.814102,3.848451,-2.091248,8.051097,-3.748254,-5.657101,4.031690,3.288969,-6.720880,0.881825,-5.025951,1.785037,4.347229,2.432437,8.918918], dtype = "float32")#candidate|12983|(975,)|const|float32
call_12982 = relay.TupleGetItem(func_1225_call(relay.reshape(const_12983.astype('float32'), [13, 5, 15])), 0)
call_12984 = relay.TupleGetItem(func_1228_call(relay.reshape(const_12983.astype('float32'), [13, 5, 15])), 0)
output = relay.Tuple([uop_12976,call_12982,const_12983,])
output2 = relay.Tuple([uop_12976,call_12984,const_12983,])
func_12987 = relay.Function([], output)
mod['func_12987'] = func_12987
mod = relay.transform.InferType()(mod)
output = func_12987()
func_12988 = relay.Function([], output)
mutated_mod['func_12988'] = func_12988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12987_call = mod.get_global_var('func_12987')
func_12988_call = mutated_mod.get_global_var('func_12988')
call_13003 = relay.TupleGetItem(func_12987_call(), 0)
call_13004 = relay.TupleGetItem(func_12988_call(), 0)
output = call_13003
output2 = call_13004
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
func_12987_call = mod.get_global_var('func_12987')
func_12988_call = mutated_mod.get_global_var('func_12988')
call_13023 = relay.TupleGetItem(func_12987_call(), 1)
call_13024 = relay.TupleGetItem(func_12988_call(), 1)
var_13025 = relay.var("var_13025", dtype = "float32", shape = (13, 5, 15))#candidate|13025|(13, 5, 15)|var|float32
bop_13026 = relay.add(call_13023.astype('uint8'), relay.reshape(var_13025.astype('uint8'), relay.shape_of(call_13023))) # shape=(13, 5, 15)
bop_13029 = relay.add(call_13024.astype('uint8'), relay.reshape(var_13025.astype('uint8'), relay.shape_of(call_13024))) # shape=(13, 5, 15)
func_5735_call = mod.get_global_var('func_5735')
func_5738_call = mutated_mod.get_global_var('func_5738')
const_13035 = relay.const([[3.939405],[3.956669],[3.616929],[-1.015374],[-7.459154],[-0.877211],[-6.998312],[5.996111],[-2.188344],[6.999205],[-2.598280],[-9.736380],[-9.730734],[-4.085250],[8.280908],[-2.736852],[9.764020],[2.079569],[-3.002398],[5.845470],[-4.085292],[8.182906],[-2.791238],[-9.804001],[-7.125982],[0.729781],[1.529555],[9.091194],[2.486057],[-2.992039],[-1.753829],[4.630052],[4.434086],[-7.236929],[-8.974766],[-4.147240],[-9.474028],[1.280454],[-0.336255],[8.454319],[-2.793936],[-0.968853],[7.239544],[9.283608],[9.133857],[3.724849],[-8.326259],[0.518717],[7.025795],[-8.414845],[2.668023],[-0.720670],[-4.389463],[-6.995945],[-2.806393],[1.464757],[-7.915196],[-4.078123],[2.764435],[-8.810249],[2.868200],[1.741537],[-6.048369],[5.219595],[-9.301561],[-5.302785],[7.005139],[0.192660],[-7.118311],[-6.382433],[-1.304954],[6.184265],[1.312140],[-0.960674],[0.131336],[4.667927],[-6.020352],[4.635458],[-9.842996],[-7.704753],[-1.643311],[-6.982253],[-5.451027],[7.221972],[-0.233364],[9.190081],[8.450383],[4.650491],[-3.363320],[4.314506],[6.583184],[-2.321137],[8.296378],[-7.532992],[6.907129],[8.129194],[8.129029],[1.249189],[6.981628],[5.680157],[-7.143522],[-6.635950],[4.220451],[8.552123],[9.031093],[-3.352990],[5.044510],[-2.787311],[-6.165107],[-6.170064],[-5.185366],[1.288661],[-4.530579],[8.502967],[3.625016],[4.046158],[7.069953],[6.654666],[1.441968],[-4.233484],[0.362742],[4.441348],[6.836287],[-3.845840],[0.573061],[1.621779],[-4.691825],[6.468872],[7.690069],[-3.293842],[9.097038],[9.649422],[-9.838587],[-5.510918],[4.193615],[-1.598547],[5.336837],[5.077564],[-7.549929],[-7.254744],[7.866186],[7.241377],[-8.815147],[-2.419029],[4.513594],[-9.957470],[-3.258244],[9.980065],[-6.902324],[-3.609023],[-5.671591],[-0.533587],[3.284357],[-4.959751],[3.368338],[5.528077],[2.566395],[-2.998029],[0.796432],[0.329283],[-4.860615],[-0.857532],[0.046962],[9.525446],[6.464736],[5.415484],[-8.541253],[2.181363],[-6.093745],[3.022061],[-0.523659],[-7.517337],[7.284976],[2.684046],[9.978304],[4.261282],[-6.012717],[-7.718894],[0.129477],[5.908183],[7.630787],[-6.989658],[-4.903830],[2.089740],[-6.725309],[2.056160],[0.608132],[-4.843330],[-1.271386],[-1.970649],[-8.629274],[2.586595],[7.039052],[7.982509],[9.545633],[9.367231],[4.343848],[2.019963],[3.426927],[-6.307491],[7.851691],[-9.226062],[8.012817],[-2.577309],[-9.913812],[4.281862],[-4.411208],[5.755245],[-9.370956],[3.596957],[5.305823],[6.351433],[-7.019866],[-3.352278],[1.083191],[0.300023],[-4.917636],[-6.853565],[-4.671326],[-5.685350],[2.133768],[-0.109736],[-6.011669],[0.430405],[-3.130155],[0.250792],[4.736837],[-8.393112],[8.189366],[2.673854],[-6.503890],[6.285717],[-4.544939],[-9.104631],[-6.168165],[7.550260],[3.173548],[-8.449243],[1.733066],[-3.652886],[-8.031162],[5.933771],[-9.527036],[7.717509],[-7.177390],[8.921774],[-9.888359],[-9.999038],[-8.017133],[4.322578],[6.117363],[-7.865813],[-0.856853],[-0.954228],[-6.985505],[6.701983],[-3.311619],[-6.679954],[6.333634],[-5.336133],[-7.507257],[-7.216238],[0.872403],[2.879241],[1.896992],[-1.130682],[5.913847],[4.800324],[3.727573],[0.011289],[1.394373],[-8.994567],[3.915476],[-6.045186],[7.576829],[-4.849144],[-5.490872],[-6.769408],[1.119912],[8.808717],[-2.364047],[4.058195],[-8.229675],[-5.705287],[1.338151],[4.248893],[-0.666752],[-0.479615],[-0.156585],[-1.717210],[-2.291910],[7.112302],[0.092942],[-7.726650],[1.183603],[-6.632858],[0.124923],[4.340198],[-9.608091],[-1.356693],[6.237399],[-7.664931],[4.920309],[5.177438],[-5.515240],[5.762452],[1.973150],[5.898467],[-5.487454],[3.866823],[-3.778879],[-0.845056],[-9.131980],[9.151430],[2.807827],[-3.331074],[-3.165257],[-7.865274],[4.388186],[5.545808],[-6.082812],[-9.014716],[-0.212155],[-2.873553],[6.564131],[-6.504432],[3.296882],[-5.341731],[3.791475],[8.957507],[8.632239],[7.577049],[-3.735647],[5.993187],[-7.795000],[5.259646],[-5.884962],[-4.002723],[-0.568806],[2.422223],[-0.844691],[9.585769],[-7.863341],[4.386221],[4.349500],[-7.616225],[-1.613813],[-1.541071],[-9.465015],[6.806110],[7.889304],[6.185818],[-0.373896],[-3.974075],[-8.566096],[8.440039],[0.221643],[2.027592],[-5.414425],[1.951035],[5.173752],[-3.828132],[-4.169164],[-0.817671],[-8.037274],[9.480902],[8.582574],[8.327501],[-0.616362],[-9.552921],[-5.658961],[7.428228],[-8.202107],[9.583212],[-2.094114],[-9.836625],[5.242043],[4.486080],[-6.975785],[-5.480244],[9.012582],[-0.528606],[-7.628726],[5.111334],[8.508877],[6.679353],[6.944206],[0.806655],[0.439872],[-0.861109],[-3.060037],[2.471377],[1.460705],[8.458514],[4.149935],[-1.219455],[9.320248],[2.293307],[6.864180],[-8.916091],[-7.676833],[-5.430763],[-4.796220],[9.248633],[-2.639108],[9.464474],[-2.216099],[-2.104125],[-3.014119],[9.032538],[3.178841],[-1.422758],[-1.114705],[-4.946134],[-6.371035],[-9.709650],[3.907946],[-0.092719],[5.743665],[8.069488],[3.222349],[-2.636557],[-8.436587],[9.247798],[-7.834885],[-9.692518],[6.824947],[-1.745627],[-4.912738],[3.099579],[7.989247],[1.175642],[-5.264598],[-8.981019],[4.283143],[6.064937],[7.687658],[-1.700808],[7.618338],[-5.052359],[2.171287],[8.389633],[2.870951],[-2.533752],[0.208494],[2.150437],[-8.758543],[1.613319],[-2.632636],[-0.981116],[1.320100],[2.774508],[9.656981],[-1.277554],[3.148216],[-9.589902],[3.050398],[0.052956],[3.610052],[-0.219415],[2.059925],[1.618655],[-8.774204],[-9.361211],[-3.369375],[-4.355303],[3.849902],[-5.646994],[-3.497517],[3.558099],[5.021892],[-8.757603],[3.000509],[-8.652944],[0.561997],[6.307418],[-8.415518],[-2.796081],[3.020413],[6.477417],[8.752035],[-3.016732],[4.842098],[7.357299],[0.973563],[-9.318423],[-2.770938],[-3.131437],[-2.971082],[-2.045340],[9.381071],[0.416700],[-3.355255],[2.895197],[-6.596912],[-5.393716],[-9.972976],[-2.271027],[2.514576],[3.665896],[-3.414595],[-7.207633],[-7.983219],[1.141137],[0.035069],[5.693626],[7.040179],[-7.883499],[-2.022775],[-5.851037],[-7.696274],[1.615005],[5.429036],[4.442236],[0.175433],[8.667844],[-5.296779],[8.401714],[-4.023613],[8.629289],[-7.001691],[0.079861],[3.464376],[-2.752614],[2.539850],[2.705268],[4.127762],[-5.334304],[-2.343797],[6.376711],[9.238183],[-7.270228],[-3.561733],[-0.459844],[-8.307296],[-6.162501],[-4.438997],[-6.226335],[3.600622],[-6.590932],[5.366875],[8.829337],[-7.900394],[6.712653],[0.648358],[-5.527986],[-5.433423],[-3.026737],[-9.506560],[9.528020],[-7.283075],[-9.103120],[6.184591],[9.568650],[0.796489],[4.129577],[5.097104],[9.697702],[6.660681],[-8.672633],[4.691639],[6.787600],[3.236270],[9.422897],[-3.068409],[-0.602439],[-3.225026],[-6.054968],[-0.824148],[7.870317],[2.920482],[-9.450785],[0.011051],[-6.465695],[0.142313],[0.457357],[8.547407],[-4.430406],[-7.840095],[3.462239],[-2.484366],[5.106952],[-7.383545],[2.517602],[0.027109],[-4.301743],[6.710502],[8.213916],[-5.548767],[8.332017],[2.676516],[-2.371444],[7.922241],[8.733076],[-6.360360],[5.248414],[3.888354],[-4.617364],[-1.256210],[-3.432853],[-1.429819],[-6.917592],[2.207818],[-5.715135],[3.160798],[8.998361],[-1.337426],[1.219422],[-7.256554],[9.118902],[0.563541],[-1.560962],[3.885109],[-0.202780],[-9.706522],[-0.058394],[1.228689],[-7.068788],[-9.918745],[-0.631214],[5.149897],[-2.774065],[-4.817451],[7.102849],[3.226292],[3.868505],[2.870876],[7.982468],[-5.913850],[-2.119677],[-6.411717],[2.199724],[7.174090],[-4.733186],[-1.622354],[9.119289],[8.775467],[6.210218],[-5.658532],[-6.359583],[7.727046],[-6.531331],[6.486864],[-1.124462],[-9.832271],[-0.797216],[9.015599],[-4.663935],[-0.148422],[-7.781538],[-4.129379],[-4.964893],[-9.401195],[5.347948],[-2.617341],[-9.157825],[5.219799],[7.762198],[-9.442351],[1.742596],[-9.328382],[2.090616],[3.276781],[0.473543],[-9.135897],[0.655189],[5.109671],[-4.034730],[1.719371],[-8.743320],[-9.980684],[-8.949366],[-8.715056],[-4.955871],[8.077538],[8.232088],[-4.937676],[7.552590],[-1.122463],[4.678170],[-7.244542],[9.156255],[-0.400272],[5.650409],[5.440882],[8.999526],[-4.079242],[-8.188632],[4.596587],[1.204246],[-2.459381],[4.802445],[4.236289],[-6.192865],[1.987557],[7.999858],[-5.973353],[8.015822],[-4.224375],[4.841981],[2.705987],[0.042355],[-6.403197],[-4.575103],[6.525723],[-0.776464],[-2.323792],[-1.086956],[-2.181412],[2.976471],[-7.937396],[1.071814],[-4.517602],[6.435296],[-6.483617],[-7.727766],[9.110531],[8.126421],[5.903464],[-9.474414],[-7.755837],[-4.655213],[-9.319075],[-6.655747],[-8.213901],[-3.133647],[-9.536972],[9.551748],[-8.548593],[-5.931213],[9.460447],[-1.447346],[-6.986522],[-6.753739],[6.537565],[-4.490953],[7.998218],[-7.899402],[7.485374],[-7.965505],[1.593242],[-1.714400],[8.881711],[-3.355446],[-7.573668],[-1.427367],[5.323826],[7.501412],[-0.654988],[-7.425684],[-8.960641],[2.169747],[9.666562],[4.411840],[3.013701],[-4.741077],[-8.744735],[-2.061134],[5.812244],[7.119115],[7.209087],[8.226329],[2.081590],[2.959034],[4.479582],[2.486862],[-2.445798],[4.240817],[9.937954],[1.045949],[5.059923],[4.119044],[-9.285941],[6.320440],[-7.750322],[-6.207697],[-1.849195],[-6.973106],[-0.513519],[3.686573],[1.781334],[7.454673],[-7.290167],[-4.110318],[3.161644],[-7.510714],[1.451340],[-5.108994],[6.434735],[8.577588],[-1.595947],[-3.134831],[-8.530805],[-0.301321],[-3.416021],[-6.161383],[9.969402],[2.373600],[-3.258520],[2.483284],[2.100759],[-2.806520],[2.091421],[9.020739],[-5.893249],[-6.395364],[-0.764024],[1.820188],[8.619512],[7.053080],[-6.856860],[-0.148563],[0.296844],[2.630709],[8.196420],[9.831929],[-8.303731],[5.384655],[-5.626820],[-8.910368],[-8.614104],[0.267975],[7.102012],[5.095871],[6.783384],[-8.794754],[-1.477961],[7.140772],[2.760518],[2.544512],[2.587372],[3.564477],[6.707807],[0.821575],[4.286648],[-7.913428],[-5.925880],[-1.513460],[6.126655],[-4.686733],[-7.663975],[-2.607885],[9.339783],[-5.933825],[-5.544046],[1.987977],[-6.140220],[5.875982],[-6.927714],[8.128045],[-0.511356],[6.275842],[-9.380654],[6.871471],[8.827504],[-6.751829],[-9.646786],[-2.041536],[-5.043017],[-2.879233],[-9.137683],[-8.561338],[0.195821],[-5.967087],[-7.221982],[2.383468],[-9.834427],[4.595281],[5.483524],[-1.499105],[-7.699711],[-0.595277],[6.424828],[2.449263],[-1.106820],[-3.022002],[1.489930],[9.793479],[-2.313440],[-2.860401],[-7.449124],[9.905260],[-2.477975],[4.527414],[1.509078],[-4.596828],[-2.205884],[6.171299],[8.197200],[6.996129],[-4.556903],[9.374281],[-6.443966],[-6.793812],[-6.085789],[3.751958],[3.291316],[5.544855],[3.391563],[6.856628],[-6.115828],[-2.154021],[-7.694065],[-0.547280],[-9.822512],[7.202778],[1.721461],[1.387635],[-7.314712],[-9.499071],[-5.457078],[2.561497],[2.743140],[-1.901018],[9.740268],[5.801097],[6.445758],[-1.460671],[7.422494],[-9.275623],[-9.507309],[9.420315],[-9.454764],[8.497840],[-4.814594],[2.938978],[0.566793],[-8.873731],[-2.324059],[7.480133],[-0.635466],[2.305850],[-2.807431],[-3.993436],[4.819972],[-0.196917],[-3.139268],[8.916802],[-8.259411],[9.476874],[6.210989],[7.552968],[5.030328],[5.866819],[-2.201814],[5.067590],[4.695069],[8.710838],[-0.315914],[-9.817156],[-5.663036],[5.901456],[-5.391909],[9.792083],[8.820792],[8.197598],[0.492511],[1.734164],[6.364424],[-0.659393],[2.800633],[-9.527946],[0.291775],[8.161009],[6.994484],[3.060157],[-6.358791],[2.215374],[4.962070],[0.158586],[6.764536],[7.292943],[5.038759],[-2.191600],[7.752424],[0.218731],[-2.162578],[-1.796112],[8.030339],[-5.947915],[5.866102],[-1.851328],[-2.334933],[-5.443302],[-3.511831],[4.101831],[-0.276184],[-0.576834],[5.823941],[-3.459147],[-8.635457],[-6.833967],[-7.868442],[-9.790004],[-2.883628],[-1.330376],[-1.854458],[8.028433],[-5.987525],[-1.684989],[0.333799],[0.280140],[4.984114],[5.205347],[-5.490376],[3.052888],[6.031269],[6.427845],[-0.599488],[6.056077],[-9.639491],[-1.944917],[-6.077237],[-3.910272],[8.121904],[2.939468],[-8.180389],[5.029751],[1.336570],[-0.639579],[-6.521355],[-8.998541],[2.753371],[6.499184],[9.845207],[-9.398828],[1.307801],[-8.259548],[-5.497354],[-4.414706],[4.877993],[-0.721370],[-8.616589],[8.374076],[9.707290],[4.689327],[-9.463742],[7.897261],[-8.218376],[3.765369],[-7.063599],[8.722098],[4.423401],[2.455565],[-0.604448],[6.117408],[-8.854677],[3.220495],[3.738659],[-5.597882],[8.228494],[2.922103],[4.054455],[0.895119],[8.287522],[0.429898],[8.986218],[3.862690],[-5.010114],[-5.020723],[7.613240],[-5.067313],[-6.500193],[-8.482009],[2.706007],[-4.186780],[2.118019],[-6.023352],[-0.296790],[-1.901376],[-7.089304],[7.352873],[-9.085758],[-5.087639],[-3.448262],[-4.916235],[2.073959],[8.185871],[-9.333196],[1.197072],[-0.993569],[-8.794043],[9.450407],[-3.082444],[2.000981],[-2.660367],[-4.492988],[7.434904],[-2.436510],[9.826836],[-2.371145],[-9.816450],[-8.274279],[1.800856],[-5.067159],[-8.084921],[-2.020868],[-4.274232],[4.243687],[-6.850873],[7.822797],[3.865649],[-1.307724],[-1.640980],[-6.755847],[1.421579],[0.468768],[-1.200191],[6.675067],[2.266792],[3.268831],[-7.429977],[-3.646715],[0.869507],[8.898621],[-0.110722],[-6.878189],[-2.199011],[-5.733330],[-0.503432],[-6.465166],[-1.240730],[5.766359],[-0.668985],[-9.165864],[-2.050709],[2.153306],[-4.419409],[1.766038],[-1.835815],[1.414636],[5.295967],[-2.371686],[-1.522759],[3.571510],[6.421380],[4.885640],[2.980863],[3.902070],[3.583329],[9.670677],[7.070915],[3.418815],[8.451404],[7.413442],[7.873493],[-0.975263],[4.479468],[3.253864],[-3.678423],[-7.749153],[-8.494624],[6.630712],[-8.692531],[4.791904],[-1.831435],[-9.658791],[-0.507660],[4.413286],[-8.769276],[3.350890],[2.877895],[3.708136],[-7.364910],[4.570797],[7.847806],[-0.669047],[5.172431],[5.303275],[-2.962445],[9.218532],[-6.216380],[-4.942564],[7.801022],[-1.152104],[3.024081],[-9.540267],[7.297723],[0.509273],[-1.324185],[-4.188215],[-2.084948],[3.217043],[-0.173014],[4.152957],[-7.314613],[-4.654621],[-2.366643],[3.231809],[-7.316014],[-0.863955],[9.900892],[7.629471],[-5.322326],[-9.409960],[4.338285],[-4.409076],[1.755293],[1.201390],[-3.400526],[9.491017],[5.805711],[1.948704],[-2.297290],[-3.354405],[-4.054079],[-6.500058],[3.319170],[1.573235],[-0.624742],[-8.292431],[-8.235825],[3.659136],[-5.769414],[-3.272655],[-1.332166],[8.024617],[6.048809],[1.972088],[2.102672],[-8.490538],[-8.609058],[4.629436],[-0.570453],[7.106125],[-3.180029],[-3.439506],[-5.976770],[3.128452],[-2.946046],[-7.681623],[2.825942],[9.620813],[-4.244084],[-9.398540],[-6.868266],[-7.358206],[-3.104783],[-2.704582],[-5.086696],[4.962671],[1.578130],[8.043299],[-2.785873],[-9.569953],[-9.594689],[9.010041],[6.192382],[-9.376215],[5.205963],[2.091590],[-2.821719],[2.273890],[-8.638721],[4.995545],[9.720311],[1.310230],[4.336351],[4.866992],[2.547122],[-7.937706],[-5.651798],[1.758102],[-4.841954],[7.216388],[9.343266],[3.475815],[-9.727941],[-8.133402],[-9.088210],[1.905376],[-3.766360],[-6.242796],[-5.437643],[7.436256],[-2.605461],[3.368083],[2.325233],[-7.822889],[5.212259],[-6.092818],[-1.028083],[-0.320018],[-3.419204],[1.511971],[-3.369223],[-3.043347],[-5.909758],[-4.970063],[-8.656633],[-0.290246],[-7.602011],[3.716551],[0.461295],[3.119323],[-1.977581],[0.767972],[-6.114985],[1.595912],[-6.884773],[7.965786],[-9.204910],[0.160930],[7.919085],[9.054883],[-9.494573],[-6.651718],[1.998755],[-3.450244],[9.238308],[8.639578],[3.157703],[-1.850195],[-6.494993],[-3.285764],[0.379244],[-9.447537],[-3.236198],[-5.173784],[7.200324],[2.206102],[9.670832],[-3.940001],[-0.886360],[1.227205],[2.704233],[7.387741],[3.619985],[-1.456437],[2.545343],[-4.667963],[-7.595967],[-4.903614],[4.565093],[-8.531075],[-0.811823],[-0.850543],[5.348804],[7.573123],[2.589687],[9.096988],[3.612948],[-8.677531],[1.414978],[4.097940],[3.739200],[3.620008],[-5.742687],[-4.828536],[-1.384054],[-5.204012],[2.948530],[-9.933930],[-7.709343],[-2.006884],[8.516412],[-9.190873],[-9.119856],[9.190770],[1.535609],[-7.381018],[2.503754],[-3.195700],[-0.712767],[7.841811],[-1.487951],[8.393304],[-3.332336],[-9.709452],[4.418031],[-5.620100],[2.628276],[-2.256867],[8.689368],[1.688736],[-2.859806],[-9.052109],[1.282233],[9.507640],[4.280406],[-4.919742],[-2.911601],[9.415625],[7.367610],[9.183217],[-6.640290],[9.454826],[-2.690543],[6.466842],[-1.093868],[-0.197211],[6.874166],[-5.571460],[-8.017463],[-7.978419],[-3.149433],[1.979994],[-0.972074],[7.099610],[-1.376294],[6.129027],[-7.802815],[-7.362644],[-0.011696],[4.590577],[-2.623781],[9.913890],[-5.157053],[-4.662924],[3.789091],[-1.139331],[1.189254],[-7.565525],[7.936414],[-1.917878],[0.501755],[-0.791360],[-2.674305],[-4.960604],[2.930878],[5.681464],[-4.070598],[6.096499],[-9.819482],[2.883594],[-2.958104],[7.482296],[6.235170],[9.245225],[7.358760],[-9.201174],[0.410290],[0.624426],[-5.450506],[-3.108094],[9.683127],[3.813453],[-9.425594],[-1.922270],[1.998426],[-4.870413],[2.679722],[1.440407],[-1.113216],[8.554970],[-7.948368],[-8.019553],[5.876367],[-0.531595],[7.355760],[0.976306],[-0.740138],[-3.771001],[6.974841],[-9.326919],[-3.030379],[-8.060925],[-5.563003],[-7.757432],[-5.826126],[9.779012],[-0.392274],[9.951310],[9.852701],[6.605973],[-1.176493],[7.784033],[0.235644],[-8.975595],[-0.201968],[4.426179],[5.382238],[-2.013483],[-0.458141],[-6.569599],[5.129117],[8.077495],[6.344719],[2.223704],[-8.543137],[-3.457156],[6.875279],[-4.145042],[8.727654],[7.945978],[3.009036],[5.663663],[-4.495997],[-3.244938],[-5.591892],[1.476647],[-5.048072],[4.465096],[9.277457],[-8.114289],[5.373025],[0.436268],[-3.125617],[-2.991939],[-2.926762],[1.425342],[-7.909084],[-6.672691],[1.796346],[3.425823],[-3.483346],[5.950094],[-2.868318],[-4.064285],[9.916305],[9.427525],[0.635298],[8.037062],[-5.568659],[-6.352514],[1.668510],[-6.067467],[-3.681910],[-8.106990],[-3.983153],[0.025546],[-7.312644],[6.802221],[-0.379566],[0.312170],[7.425850],[-8.635142],[9.060163],[-9.442060],[8.269609],[-8.720905],[0.683773],[4.832810],[4.172295],[3.611164],[8.874580],[-1.305920],[1.240605],[-8.713114],[-9.900262],[6.831222],[2.939156],[-4.597985],[6.667067],[-4.084754],[4.890633],[6.695042],[-6.902675],[-3.465114],[-8.382777],[4.147782],[8.444986],[1.324029],[7.271828],[-6.047378],[3.396288],[1.287638],[3.190461],[3.264307],[7.012595],[-9.646274],[-8.447565],[5.431714],[-8.723314],[3.150385],[1.824862],[-2.199679],[-2.694631],[4.206944],[-6.393830],[0.506442],[5.372322],[-9.517597],[1.045847],[5.753330],[2.605162],[3.497362],[8.685821],[-7.147612],[9.250522],[-6.487655],[-7.798759],[8.488846],[-0.372219],[7.390417],[-6.760407],[0.256801],[8.451952],[-6.208392],[7.845202],[1.455458],[8.760672],[8.907313],[9.206770],[-5.705858],[0.494769],[5.019107],[-3.876690],[-7.969859],[3.584307],[9.651003],[1.381567],[2.874965],[-7.824553],[1.276090],[8.764931],[-6.815557],[7.886608],[0.805688],[-0.805392],[9.713896],[-2.517405],[9.784901],[3.886078],[-7.957237],[6.488589],[-3.849353],[-6.776128],[-7.647950],[-9.841731],[-1.950328],[-4.414058],[-3.893742],[-2.008628],[6.085231],[-3.719191],[-0.613129],[6.068094],[7.046796],[-8.469876],[-4.991323],[6.806295],[-3.050084],[-6.920262],[-8.145198],[-9.386914],[8.150201],[0.603846],[-3.284603],[1.366033],[-4.846710],[1.905889],[1.930571],[4.111840],[2.539780],[-7.135208],[4.497403],[5.556974],[8.016995],[-8.595272],[-6.048463],[-1.806354],[-2.967892],[4.070579],[-5.771788],[-3.858590],[-8.051459],[3.668475],[-1.934406],[-9.380947],[-0.207066],[0.557995],[-5.788812],[8.083530],[4.664607],[1.407898],[-8.973250],[2.671838],[-7.284422],[-2.457107],[7.612371],[1.846461],[-8.754210],[2.472030],[0.545172],[-7.571011],[-0.644024],[-9.188369],[-7.424564],[-2.238222],[1.055012],[3.897372],[-3.289757],[-9.853019],[-3.951466],[3.669095],[5.395574],[2.043339],[5.194605],[6.014123],[1.124351],[0.785946],[3.810667],[-4.017806],[9.458417],[4.013634],[5.139558],[4.381970],[3.114388],[-8.564599],[-4.011839],[-6.838458],[-4.478353],[9.642735],[-4.563441],[2.334099],[-0.321725],[-4.585785],[-8.451116],[-7.683206],[9.801876],[-9.516030],[-5.562305],[-0.298103],[-9.286681],[2.893570],[-8.654633],[-0.259785],[-8.068794],[4.266764],[-1.347085],[-7.987961],[6.513978],[8.612304],[8.544285],[2.102278],[6.541518],[8.905075],[2.285852],[-4.144216],[-7.469040],[-3.274050],[7.256672],[-1.011811],[-2.585804],[-7.407142],[-2.191100],[-9.985928],[8.476935],[4.166398],[8.523741],[-0.706661],[-3.403929],[-2.326027],[4.190945],[5.847469],[1.463028],[6.168588],[3.543514],[-4.751694],[7.153133],[-2.603717],[2.600024],[2.404948],[-6.767714],[5.016362],[4.752878],[5.449960],[-8.410716],[-0.782965],[-4.791442],[0.576080],[2.327129],[-5.549460],[-7.214790],[8.412305],[6.917006],[7.211667],[-4.862904],[-3.553848],[1.522805],[-3.123967],[2.563971],[8.691238],[5.423762],[9.553128],[4.166229],[0.320141],[5.756431],[2.492875],[-6.132055],[4.292171],[2.429638],[-7.952034],[8.126914],[-5.619807],[5.425781],[-2.000177],[-4.244104],[-9.466964],[6.322702],[7.167253],[-6.406186],[4.533182],[-3.311180],[-1.650718],[0.802393],[3.997072],[-2.229628],[-8.040020],[-5.489524],[5.714272],[7.689936],[-5.771621],[8.140573],[-7.758627],[-6.246548],[9.664803],[-3.916708],[7.518031],[-2.637710],[-7.302949],[8.712296],[-3.418146],[6.241034],[-5.427460],[4.742483],[5.289717],[1.829628],[5.227523],[-7.685347],[5.702004],[0.229550],[-5.507446],[3.983479],[4.430826],[8.692944],[-7.723902],[8.537387],[-7.073142],[9.590133],[-3.403160],[-2.053338],[-7.828821],[1.526898],[-4.680906],[9.659526],[-2.690350],[9.041782],[-4.533918],[-3.594635],[-4.304303],[4.559997],[4.725570],[8.356937],[-2.443734],[-3.282034],[3.352527],[-7.015893],[-5.785877],[6.989944],[-7.461591],[-4.658503],[-8.119935],[4.583802],[-3.261933],[-2.135793],[4.392423],[3.989472],[-2.512530],[-8.329522],[-5.576163],[1.558233],[-3.267563],[2.520343],[1.460550],[7.585586],[6.546195],[-0.919881],[2.762162],[-8.566157],[-0.519641],[-5.786543],[8.443485],[-6.626692],[-4.662956],[-7.168836],[8.452142],[0.290460],[7.319017],[-5.276835],[9.231452],[-7.120853],[8.617779],[-2.686343],[-9.164728],[-9.785679],[5.246473],[-0.677890],[1.613971],[-9.485335],[-9.289989],[-1.780058],[-1.509828],[1.592219],[-8.900814],[-0.110081],[4.156049],[-3.627570],[-3.418959],[-7.302706],[8.066238],[0.675505],[8.771812],[7.670561],[-4.525881],[9.855002],[-2.711791],[-6.216226],[5.219177],[3.619755],[1.886987],[6.452504],[-8.212483],[4.451243],[1.933570],[-6.455722],[-3.288485],[3.330111],[6.833633]], dtype = "float32")#candidate|13035|(1920, 1)|const|float32
call_13034 = func_5735_call(relay.reshape(const_13035.astype('float32'), [8, 16, 15]))
call_13036 = func_5735_call(relay.reshape(const_13035.astype('float32'), [8, 16, 15]))
const_13038 = relay.const([[[8.203769,-3.348320,-4.341619,1.511114,-2.137839,-0.900014,-5.312636,-3.008506,-0.434470,7.429045,-1.475174,-8.909341,2.593950,6.189545,1.398780],[9.105989,2.083691,-8.236576,-5.656966,5.089153,1.807576,-6.835753,5.058059,-5.311563,-3.820088,0.401087,-6.760186,-9.708250,-7.158039,-1.563670],[-2.725811,-2.635925,1.115038,4.928641,-9.894329,-5.849733,8.719869,6.539297,-6.320619,-9.169595,6.389678,9.902421,4.508357,3.465944,9.148136],[0.113098,8.220581,9.267908,7.296021,-8.343466,-9.917551,8.317543,0.856108,-3.537705,-2.877138,8.526229,-9.583314,2.078016,-9.128965,2.161910],[-1.434450,5.318308,-7.421197,-2.542568,-4.935717,9.335040,-3.581159,-0.579971,3.008280,2.631226,7.385014,3.827235,7.596884,0.907846,0.264169]],[[-0.223217,2.432697,4.907038,-6.887166,9.744234,3.251777,9.031303,8.595866,2.018980,1.498544,1.723130,5.261708,-8.067685,2.652742,-1.304871],[8.177304,3.377366,2.081243,-7.750728,-8.332985,-6.609754,4.891977,8.664774,7.585030,8.180032,4.462873,5.881114,-4.582886,-8.011254,7.712220],[-0.379739,6.721805,3.128185,2.852780,-4.365803,-1.110454,8.448550,3.504751,-4.789981,7.295838,1.606448,-7.634892,-5.050218,-7.180146,8.369489],[3.301073,-4.500679,3.226922,2.939241,-6.487113,-1.658184,-8.192559,-0.425591,2.199310,-9.575088,-5.996055,6.120272,-1.135123,4.122261,-5.197286],[-4.843527,7.986788,-1.466055,5.615890,3.113950,-6.490603,-4.015386,1.033983,-6.769102,2.617798,4.499664,-5.758534,4.794826,-3.125617,9.233280]],[[7.218242,4.900617,4.109873,8.713846,6.169733,-3.265582,-1.646228,8.015699,6.847726,-0.236886,-0.681334,-6.670730,9.618662,-2.522061,7.163411],[-7.834471,7.956190,8.100199,-0.240402,5.508662,9.179901,1.363296,-5.902209,7.810980,-7.482255,6.713170,0.870715,0.741600,7.199072,6.563278],[8.116599,0.185542,2.297606,7.026638,1.785720,2.714974,-4.598773,-8.433563,1.507345,-0.285837,-4.945683,7.081965,-4.505273,-0.980824,-5.789547],[-8.341555,9.653562,-5.657711,-3.694724,-5.257571,6.143438,-9.090968,-4.220633,-2.124589,-1.977177,2.711968,-3.640292,-0.935202,0.404659,-7.667862],[-0.795539,-4.345906,-9.485026,-5.482719,-0.112862,-9.109128,6.420772,-9.229798,-6.999160,8.992193,1.661072,6.977491,9.165114,-3.071641,-9.794852]],[[-7.381582,4.040824,-5.382385,-4.254263,-3.366086,-5.429745,-6.194243,8.548273,0.001217,2.124555,-6.571460,-1.460660,6.178696,-7.303000,-5.725948],[-1.985155,9.548661,5.466514,-6.468115,0.475581,4.078862,2.676259,1.275456,-9.086771,-0.761516,2.383591,-9.853776,-1.131195,-6.532220,-8.717413],[3.321640,1.262932,-9.074601,0.474164,-1.881960,-5.255327,-0.399625,1.309684,-2.272945,-2.937586,-8.859285,-5.079684,5.694637,-7.847611,4.682568],[6.314075,5.468722,9.921708,3.818858,-5.339724,2.173466,5.502353,5.317988,9.929654,-8.745220,-4.249444,-7.524553,-4.539240,-3.457423,0.218419],[3.489870,-2.760457,6.339735,-4.056747,-7.970627,5.097925,7.607025,2.119231,4.309207,6.139226,0.978043,-7.584360,-3.499500,4.950311,8.410420]],[[-1.197956,5.150465,-8.493318,-6.455694,-8.321349,7.104240,3.594565,-2.242794,1.219271,9.366745,-0.122602,7.312674,-0.289542,4.089248,-0.645838],[-5.764926,7.545039,1.999048,6.739224,-0.785661,3.536897,5.782270,5.221054,0.392875,5.585596,0.785190,4.920438,2.342421,-9.665802,-3.504025],[4.969179,7.772524,-4.280858,-8.136626,-1.647512,6.113389,0.800439,-6.007973,1.008027,9.647817,7.076436,-0.717950,2.201561,-9.562022,-8.642388],[-1.480242,-2.582389,-5.110003,2.147974,-2.539712,9.183106,2.905530,-0.714122,5.089085,6.203092,-8.266238,4.581205,-3.882801,-4.341171,-9.955988],[0.458484,9.551020,-4.259797,-2.623829,-9.658355,-4.371956,3.208377,-8.658914,1.527461,9.578476,2.653244,7.374157,-8.846171,2.376816,5.782190]],[[3.624912,5.944077,-2.969767,-7.980444,3.041021,0.167896,-4.396806,0.216238,-1.939670,8.670902,3.614306,4.818864,9.448631,-5.902483,6.574547],[3.456786,-7.333013,9.124043,-1.457023,-0.008496,-0.048507,4.129985,-8.752859,-1.891900,-9.468612,-5.279006,-3.282718,-9.312853,7.921730,-7.627078],[-1.282409,5.414823,-0.982063,9.173909,-4.721631,-5.378331,0.185102,7.823403,-4.206871,-7.076466,8.248493,2.907820,5.256085,-3.632143,-3.991757],[5.778514,-1.940552,-3.178646,8.631955,4.453211,8.102505,-7.035593,-0.196305,-4.774197,0.140326,4.804163,0.489793,-7.072523,-3.388667,5.370646],[-0.982413,-2.812401,4.514087,6.989678,-0.834300,-6.177607,6.249135,9.442649,-5.338586,-8.937177,-2.874757,2.094011,-8.951426,-4.525867,-6.477643]],[[-5.090158,-5.246324,9.929656,9.270264,-1.254774,8.079363,4.909288,-6.567579,-9.219885,-5.689384,-7.311517,-2.273036,-7.473635,-1.671371,-5.177119],[-6.120111,7.887845,2.271216,-1.515989,2.880192,-1.473847,3.945123,5.610685,-1.867589,-3.082827,2.890801,-0.826668,-1.270016,-8.791749,7.063020],[9.012623,6.123613,9.622972,8.422238,7.327795,-8.235889,-8.600582,2.274561,9.577880,0.376340,-1.089730,4.306994,2.577575,9.723745,-8.831571],[-9.293112,-6.614343,-3.064556,-7.749589,2.690686,-5.480599,0.148378,1.857893,8.710545,4.994228,5.460238,9.686099,-8.009443,-9.481773,-3.409149],[-1.281465,6.009501,0.851132,-1.004515,5.300142,1.695007,-1.116889,-0.985272,-9.849400,-2.719216,7.854735,0.233285,-0.871231,6.490595,-8.246455]],[[1.241531,-0.654876,2.281268,-4.787436,5.131590,-1.604434,-7.884162,5.907280,-5.053282,-6.227144,7.280013,-6.614006,-8.215232,-4.721675,-8.529028],[1.317564,-6.369250,-4.032076,5.956886,1.971289,-8.896681,-6.699610,-7.839617,-2.412712,0.891305,-2.692906,-3.837809,2.894117,3.552649,-1.098232],[-3.542255,-0.056288,6.147772,7.993232,6.076490,5.085237,-7.167731,-4.398919,4.992398,7.843272,0.912366,-9.041669,1.557536,-3.816938,1.253083],[-5.942701,3.138950,-7.396097,9.506698,5.311774,1.593930,-5.343898,-7.460906,-2.876205,3.772432,-9.660922,1.338320,-3.430865,5.196073,-7.974994],[5.492850,-4.008063,2.248282,0.348688,-2.462290,9.898739,2.705735,7.278716,0.454399,-3.274815,-8.880099,9.581457,8.078824,-2.848890,5.399572]],[[7.674161,2.951449,6.073506,0.339932,8.546636,2.083829,1.040289,-2.622314,7.323112,-9.436889,8.974132,-8.236880,7.881219,-1.637895,-8.517999],[-6.962205,5.434224,-7.493804,-7.843499,9.102823,2.124489,-5.555325,-7.109573,-6.478843,-7.284955,1.632448,3.040133,0.306105,7.405420,-9.931376],[8.590244,5.848714,-3.273396,5.944098,8.119217,-7.592194,9.295949,7.300617,5.053937,0.187823,6.920880,3.060895,7.178383,4.519087,8.192927],[-3.473769,-5.831229,9.943042,4.133161,9.769176,4.029074,-1.994647,-3.785141,-8.141147,9.825458,-0.112904,-2.126099,6.152213,-6.184826,-2.337224],[-6.272894,-9.366248,3.569147,2.041298,-5.932301,4.156498,-5.480325,-0.660526,-0.718166,-8.214518,7.910276,-5.753741,8.390838,9.449721,-8.868605]],[[2.125869,-5.766473,9.871084,5.591904,8.108716,1.440452,0.810820,-8.658018,-1.123336,0.816850,-5.193729,1.398325,-5.498466,-9.826463,-6.429969],[-9.648003,5.403708,3.441898,-8.597067,5.467264,-7.669236,-6.882838,-0.809561,-4.399621,2.886982,1.526606,-8.867541,-2.462535,3.297954,-5.271355],[3.299802,4.413015,3.435464,9.374548,9.906721,1.888424,6.983620,-0.006470,-5.860851,9.504702,-1.974008,5.475088,9.932578,0.162235,-7.384013],[7.590439,-7.914783,-1.510727,5.446535,3.805695,-7.447937,4.021793,1.334294,2.430478,-9.805371,7.344677,-2.192785,7.757605,4.769648,-1.628654],[-2.170063,5.196761,3.787942,-6.544296,-0.249758,8.991824,4.700148,-9.936660,-9.385088,-8.341963,-1.917378,3.800505,3.127654,1.952964,-9.011150]],[[-9.651913,5.599262,3.962460,-7.623750,2.952880,-3.526727,8.173772,4.147243,-5.291472,-3.566181,-5.496218,-3.806925,0.950222,-0.238736,-1.785210],[-3.142644,4.765594,1.825639,-7.670045,5.713342,-6.652367,1.715983,6.427721,9.531513,-1.886987,-3.770320,2.990233,6.930522,-1.737985,4.699445],[-3.546638,-2.470480,1.357717,-6.655080,2.044140,6.739838,1.135781,5.467995,-9.622376,-2.125767,-2.030367,8.416891,-2.872032,-0.037718,2.293323],[2.530133,-8.073952,1.142352,4.262149,7.621366,7.040458,-6.889412,9.696457,3.431010,8.310059,0.956291,5.632804,6.446680,7.712980,-6.066466],[7.889628,-9.682384,8.533796,9.862524,9.889012,2.337286,2.546361,-0.410117,-7.985060,-0.448327,3.193445,7.831038,3.851588,-2.997358,1.765570]],[[7.073485,0.263328,-1.814042,3.550293,7.057017,-4.302567,-9.752032,0.995232,6.180244,-8.716429,1.456210,3.831016,-1.430744,9.594512,2.297949],[-7.580602,1.408378,-9.612521,-8.860869,3.095032,-0.893682,2.333192,8.503176,3.972702,-8.205425,0.093240,-0.145966,-2.264935,2.514692,1.257899],[-5.659949,3.035765,7.080078,4.191798,8.758054,-4.048219,2.336810,-6.356864,-0.977073,9.045196,-6.912021,-4.043126,1.861177,3.316358,-5.396416],[6.125345,-2.398636,-5.628152,-9.798755,-0.267256,-8.324377,2.943801,-5.047584,-5.438569,-3.761025,2.655298,-4.462586,2.389043,-1.922059,-8.393446],[1.343704,-8.673124,-8.889231,-1.632812,-4.657283,3.967785,0.563529,-4.006127,-8.555659,-1.449515,-2.288970,0.760855,6.795209,-8.488800,-6.840426]],[[-3.594015,-7.870975,4.322880,4.094964,0.662456,-6.180514,-0.785928,-5.676767,2.577570,5.042463,3.468011,0.271782,9.820034,0.614268,4.089893],[-6.197152,2.759893,-4.474333,-8.510558,-0.918102,4.667242,-0.030130,-2.169997,1.458404,4.017636,8.426178,-7.611751,-1.084430,3.349040,-4.909057],[2.191236,-0.868178,7.817616,6.903538,-7.900948,-6.601512,9.275988,1.430562,0.898356,6.628346,-9.305574,5.508070,-8.601060,-0.468932,7.353741],[-6.962067,9.564952,6.028961,3.974414,-8.609395,9.783575,3.710297,4.782599,-8.125037,1.766772,-3.367409,1.499700,2.425980,7.694320,2.246913],[-1.177378,0.353132,3.374260,-5.069752,2.889904,-6.930513,2.812816,1.761596,5.512110,9.206158,-2.719731,-2.520533,7.755846,1.193837,7.445831]]], dtype = "float32")#candidate|13038|(13, 5, 15)|const|float32
bop_13039 = relay.power(call_13023.astype('float32'), relay.reshape(const_13038.astype('float32'), relay.shape_of(call_13023))) # shape=(13, 5, 15)
bop_13042 = relay.power(call_13024.astype('float32'), relay.reshape(const_13038.astype('float32'), relay.shape_of(call_13024))) # shape=(13, 5, 15)
uop_13048 = relay.rsqrt(const_13038.astype('float32')) # shape=(13, 5, 15)
func_5414_call = mod.get_global_var('func_5414')
func_5418_call = mutated_mod.get_global_var('func_5418')
const_13071 = relay.const([-8,7,3,-4,-10,-3,-4,-6,-4,-9,-6,4,8,1,1,10,-3,9,6,-4,2,1,-8,10,8,2,8,4,-10,-7,-9,10,5,7,-5,-8,-8,4,-6,7,-4,9,-7,-5,8,-7,10,-8,-7,4,5,10,3,-9,-8,2,-7,1,4,2,9,-8,7,2,10,-7,-2,-8,10,-3,-8,-10,7,-1,-7,-4,2,-7,-7,-4,-9,-2,9,5,1,-10,4,-4,-9,-4,9,7,10,-2,-3,4,9,-2,-7,-2,4,7,-9,-2,7,-9,6,10,9,2,10,5,-1,-10,1,-9,3,6,-1,4,-4,6,8,5,10,1,-3,-9,-1,-7,2,-1,3,7,-6,2,4,10,-6,1,-2,3,-7,2,-5,2,4,-2,-1,-1,-2,8,4,9,-3,-3,-3,2,3,9,2,7,7,3,10,6,10,9,-2,-2,-9,3,5,3,9,8,-3,9,4,-9,-7,-10,1,-1,-8,-1,9,-2,-7,-2,4,10,-5,-1,-1,5,7,7,5,-2,-10,-3,-5,3,7,-10,7,2,1,1,4,-1,1,1,-7,-10,-6,-8,-7,6,-10,7,-8,-7,2,10,6,-7,3,-5,-10,9,-8,-8,-2,9,1,-9,-6,-10,6,2,-3,-1,8,-9,10,4,-9,-3,7,4,9,-8,2,1,8,-2,-6,-9,8,1,-8,-6,-9,9,-10,-7,6,3,-5,-6,2,6,-10,10,-5,-5,-8,-3,1,-5,6,-1,-7,-10,1,-5,-5,-10,-8,-4,3,-9,2,2,-3,-6,8,1,4,-10,-1,-7,-8,3,9,-2,-1,-7,-2,-8,-5,3,-4,1,-8,-10,-7,-5,-5,-4,10,-9,6,3,3,2,8,1,10,7,-2,6,7,8,-2,6,-8,-10,-1,2,-6,1,-2,5,6,-1,-10,-10,8,9,-10,-1,-4,-3,-6,8,-3,-8,-3,6,-7,-8,4,6,-7,2,-1,-6,-6,9,-7,-7,-10,-5,2,-4,8,7,-1,-6,7,-6,2,5,-4,-3,-5,-9,-7,-10,6,7,-6,-10,5,-7,-5,-3,8,9,4,1,2,4,6,10,8,10,10,-4,5,9,6,-8,-4,6,-9,-7,7,-2,-7,-7,-10,2,-4,-6,10,10,1,-2,-5,3,3,4,-3,-5,1,-7,6,2,8,10,5,-3,7,3,2,-3,6,-7,6,-1,-3,-9,-10,2,8,3,1,2,-1,-8,-1,-10,-10,7,-10,-4,-9,-5,-1,4,-6,-5,-6,4,1,2,5,-10,10,3,-8,-6,-2,-3,-5,-4,-7,-9,5,-10,-7,10,-6,-9,10,10,-10,2,-5,-7,-5,1,-10,-4,-6,-1,9,-7,4,1,7,-9,-8,-9,9,3,-6,5,-7,-1,5,5,3,-7,7,10,-1,-3,1,2,-9,-3,9,1,9,8,3,-6,-7,-3,4,10,-2,4,4,-5,-3,8,-8,-10,10,-1,-5,-1,-3,-7,-8,2,-8,7,-4,-5,-1,-1,-3,-6,-10,5,-5,6,-1,-2,-1,-2,3,-3,10,-6,-2,-1,-7,-7,5,10], dtype = "uint16")#candidate|13071|(588,)|const|uint16
call_13070 = func_5414_call(relay.reshape(const_13071.astype('uint16'), [14, 3, 14]), relay.reshape(const_13071.astype('uint16'), [14, 3, 14]), )
call_13072 = func_5414_call(relay.reshape(const_13071.astype('uint16'), [14, 3, 14]), relay.reshape(const_13071.astype('uint16'), [14, 3, 14]), )
uop_13075 = relay.log(call_13070.astype('float64')) # shape=(14, 3, 14)
uop_13077 = relay.log(call_13072.astype('float64')) # shape=(14, 3, 14)
output = relay.Tuple([bop_13026,call_13034,const_13035,bop_13039,uop_13048,const_13071,uop_13075,])
output2 = relay.Tuple([bop_13029,call_13036,const_13035,bop_13042,uop_13048,const_13071,uop_13077,])
func_13081 = relay.Function([var_13025,], output)
mod['func_13081'] = func_13081
mod = relay.transform.InferType()(mod)
mutated_mod['func_13081'] = func_13081
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13082 = relay.var("var_13082", dtype = "float32", shape = (13, 5, 15))#candidate|13082|(13, 5, 15)|var|float32
func_13081_call = mutated_mod.get_global_var('func_13081')
call_13083 = func_13081_call(var_13082)
output = call_13083
func_13084 = relay.Function([var_13082], output)
mutated_mod['func_13084'] = func_13084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12987_call = mod.get_global_var('func_12987')
func_12988_call = mutated_mod.get_global_var('func_12988')
call_13352 = relay.TupleGetItem(func_12987_call(), 0)
call_13353 = relay.TupleGetItem(func_12988_call(), 0)
func_13081_call = mod.get_global_var('func_13081')
func_13084_call = mutated_mod.get_global_var('func_13084')
const_13355 = relay.const([4.803727,-6.722127,-4.088351,-8.441682,-0.777065,-7.514692,-4.826109,1.724817,-0.060336,-4.712701,8.676789,9.221767,-8.122712,0.150241,9.934237,3.234802,4.243353,8.297459,7.819935,-5.643111,-4.491209,1.580209,-7.077660,6.140254,7.355751,4.501466,-8.274247,5.468616,3.781112,8.849114,1.163101,0.825373,-5.860002,4.905372,2.684846,3.386006,-3.550082,-3.436104,-2.768525,9.464723,0.499260,-1.190878,0.599857,-6.705933,-4.195816,-4.551829,-4.616992,-6.796106,-1.728740,5.670678,4.704124,-5.608448,8.667696,-9.956660,-4.981924,4.497354,-1.618908,8.413417,7.419121,-7.777167,0.899987,-6.990542,0.788560,9.036607,-2.811559,7.489506,5.155360,5.844987,-8.272311,-9.797850,3.258272,-4.050411,9.676437,8.325067,5.863695,-3.505275,-3.222723,-4.506695,8.509018,-3.491691,-2.054081,3.263856,5.087279,-4.174638,3.425549,-8.793703,0.995234,-0.846401,-6.477658,2.039607,-9.193234,8.411366,-3.263818,-0.046562,6.673566,4.355887,-2.623071,0.390846,3.288958,9.529142,6.124327,0.275422,-4.593714,6.596192,-1.592562,-8.062115,2.895122,5.103759,1.373668,4.526525,-9.833951,3.285912,-8.048221,-5.568640,-2.006553,-2.763341,8.907597,-8.262286,8.541429,4.499453,2.224944,-9.354204,2.927848,-5.059941,1.297878,9.807540,8.637983,-8.095419,3.433553,7.325952,-2.033703,2.689489,-5.668302,2.997798,-9.072153,3.835889,-8.369178,-9.329265,5.967782,2.638061,-8.512289,8.188151,5.294416,5.837859,-7.041989,-7.806105,-0.434814,8.900697,-8.156311,4.193880,7.952431,-1.445000,-2.278322,9.234175,3.353111,5.462028,8.762108,5.617252,-2.677896,1.175132,-6.314182,-1.532568,-2.089421,0.980931,-7.020417,3.321564,3.359078,-8.680430,-6.541985,9.082361,-5.733181,6.708512,8.738495,-3.663286,-4.063027,8.722194,1.004576,7.496595,1.889788,-6.347218,5.500831,6.924702,9.521361,2.097949,4.299800,-7.765361,5.529595,6.578613,-9.162807,-0.837130,7.046049,4.996524,1.429081,-4.511350,8.609903,2.538095,-1.630059,8.030899,-7.760074,3.996986,-6.912165,1.640468,-0.935448,-6.020196,-9.627382,1.941643,-0.263412,-9.571910,1.028829,-4.404253,-9.797368,-2.577594,-3.503061,-1.784459,-1.211503,-3.282189,8.652109,-5.139084,-8.847373,9.644023,6.361080,4.751171,8.736636,-8.832797,-0.023660,-9.075096,-4.740802,-5.087671,-9.918641,5.748473,-8.800771,4.854801,0.136657,4.097471,4.202205,-9.853380,8.267571,-6.682758,2.264032,-7.941064,-7.110937,-1.739660,1.182879,5.478061,-1.333666,-1.706534,1.173914,-2.050506,8.447042,-4.570652,-3.712953,8.338240,-7.375199,1.289860,-7.650965,-6.882998,-6.050453,2.925940,2.419634,8.161627,0.623625,-2.352382,-9.216569,7.601941,3.391168,-3.741239,-9.767159,4.393492,7.610303,4.190288,-9.693458,-5.262055,-9.192493,-2.546301,0.015637,9.500169,9.749438,9.715877,1.989712,0.479886,-7.915978,-9.367909,-1.849278,-0.864932,-1.983421,1.596769,8.274922,4.478396,-0.412638,3.888899,-9.669276,-1.335088,-9.369050,7.330916,4.317519,-2.802578,-0.489489,-5.067244,2.370626,-1.319674,-5.313067,-6.036336,-0.603039,-8.392231,-5.284902,-2.927574,-3.785212,-5.196416,-4.122897,-2.867923,7.712091,5.124276,-8.866273,-4.158803,-5.886789,6.934104,-4.095716,-5.979955,-7.951861,8.161437,-3.061924,7.654484,5.297905,-8.589907,7.411276,7.410670,9.931011,-6.180949,-5.143154,9.573029,5.318092,-4.552639,5.915652,-3.838510,2.440936,-7.744642,8.608927,-8.301822,1.245068,-0.598773,-1.772032,9.831369,2.394396,1.351735,-3.952349,-2.241060,7.291883,-3.733924,-8.752138,-0.726247,-3.006187,1.312089,-1.778063,-3.658132,-9.533684,-0.998660,-7.359459,7.665526,9.509928,-0.948166,5.811719,-7.975515,3.440773,5.381191,1.164010,9.297525,-3.627187,-9.417004,-5.381040,0.508210,5.806882,6.197581,8.137747,9.011022,3.616089,0.346495,2.003038,-8.581002,-8.029861,-9.063052,6.762478,8.375700,-2.866466,2.121460,8.309775,-0.626561,-7.941939,-8.300941,-8.375807,2.132631,7.824058,-7.248161,-8.738546,6.518017,2.138285,-4.815116,0.214019,-6.926720,1.291160,1.169092,-5.377261,-8.762056,6.689664,5.714649,-0.352360,-9.942710,3.823350,-7.337446,2.045551,-5.440198,1.601933,7.847937,-0.094232,6.425950,2.460558,-3.808793,-6.294811,6.144983,-6.583482,4.667801,2.837364,-4.871396,-4.384062,-9.086267,6.217483,-9.139113,5.418993,9.980870,-4.625894,-1.873534,1.469322,8.326781,0.195944,-9.100521,6.444590,-9.996933,6.984607,8.846555,-4.019842,3.852105,-0.625380,-0.759346,7.393119,-1.804707,-1.352597,-5.947060,4.400380,9.351553,-4.839967,-9.823952,4.825510,-9.035306,-9.419760,0.574581,6.317667,-6.626611,-0.930825,2.993189,-7.739964,9.842219,-4.044369,9.964495,-3.582187,-3.777461,-1.935074,-4.235269,-3.822458,-1.343952,2.176515,4.817932,-8.253709,-3.963267,-2.052998,-7.631059,2.093118,-4.457993,2.436093,-3.017537,-9.230348,-6.434984,0.915332,5.041147,8.404846,-4.763737,6.154625,4.544728,0.055077,-1.438265,-3.028368,8.112301,1.091819,3.874668,9.857340,-8.627094,9.720238,-5.053717,4.323655,-4.329964,8.922397,5.080369,-6.311628,-7.460169,4.630694,1.552591,7.440912,5.367228,-0.365956,-6.686526,-3.765852,-8.607188,2.178754,7.448879,-4.621249,-9.101341,-6.680641,-0.413915,-7.998052,0.480693,9.723363,0.220798,6.994086,9.155149,-5.629795,6.713421,-2.864567,-0.620412,-7.556607,2.646507,0.136943,-2.766983,5.100614,-2.170808,9.111442,0.151253,-8.435912,2.936242,-7.376821,-1.068313,-9.046087,0.106713,0.094744,1.160883,6.993396,-0.656092,-5.865597,8.241194,4.579625,1.299028,0.791972,9.816397,-3.059770,8.253130,-0.689908,1.550782,2.434227,0.627284,-4.432062,-3.266556,7.320451,-3.627653,1.817915,-2.894521,0.642745,5.099285,-3.627888,-9.120381,0.056822,8.732892,9.400634,8.463228,-5.522821,3.275942,3.373268,-8.653095,-1.529207,-3.985439,-7.189013,-6.225824,-8.036529,-3.379098,4.582592,9.765288,-6.121405,-8.872488,7.921832,-4.727593,-7.129375,-1.716737,2.855728,2.362325,7.319329,7.445204,-9.199493,1.933426,0.029737,5.657953,1.640613,-3.017186,-3.487232,7.375132,-9.424172,4.344102,-7.030611,-7.271678,-2.456386,3.317251,7.018333,-4.569067,1.309189,-3.273827,0.985114,1.312254,6.322934,8.782793,-7.511073,1.985590,-5.555120,3.897589,8.671881,9.636984,4.208657,4.428364,1.747303,-2.719028,-0.106351,-8.494741,2.440034,-0.933371,3.476331,-7.680184,-4.013388,-2.447621,-1.652901,8.123227,5.219508,1.526409,-1.940093,5.154126,-1.985824,-8.706049,-5.211700,5.479800,-4.504304,-0.537420,4.646052,5.846307,5.936991,-8.786894,7.924596,6.516603,-9.529637,-1.636457,9.209557,5.524461,8.847529,-7.120875,-3.561794,4.338802,4.861966,-6.723761,-2.104686,2.139855,7.157937,8.448242,5.554608,6.565424,-2.545665,-4.838305,4.907275,0.380830,7.277087,-2.993595,0.451065,-7.662085,-6.453896,4.250276,-7.109633,-1.455346,6.501125,4.480760,-2.466590,-0.229611,-1.160062,-7.211617,-2.871474,-9.901230,-2.367321,1.048815,2.228347,-2.881140,-5.624091,-0.903180,-4.104808,-6.703652,4.841388,4.475435,-2.149663,-3.960506,-6.620898,-7.225699,-4.097329,6.988081,-3.127151,1.276858,-5.343287,0.889022,3.275929,-1.965981,-1.521473,0.155242,-8.851715,9.589855,5.006930,3.564440,-1.821865,-4.601930,-7.404227,9.045429,1.557881,-0.355435,9.236692,-8.007525,-9.396698,-9.778509,-2.457930,-1.366168,-3.525336,5.907465,1.382668,-4.538336,0.589647,-7.291910,-3.255918,-3.007709,-0.919098,2.592601,-1.890090,3.400328,-3.317628,7.227767,4.973779,1.936007,5.106646,0.798215,3.219816,-1.660525,8.399490,3.309222,0.732374,9.639316,-0.454906,3.734820,-8.283199,0.917888,-4.659459,2.900378,-3.890694,-1.853273,-7.611734,-6.659833,2.167490,-8.820496,-0.305491,-6.404084,7.870409,7.236209,-2.076128,-6.754412,3.501580,-7.672190,-6.764931,-3.198102,-5.344097,-2.025471,-2.099940,4.191625,6.294143,-8.774180,6.081406,2.479188,-1.100357,-9.665250,2.464985,-3.853818,6.183868,0.416236,-5.908515,-3.081505,-3.853357,2.134673,-6.336347,-8.998707,-5.069972,7.686579,0.232484,-5.986667,5.202639,-0.910467,5.195559,-5.478906,1.048174,-3.341327,3.264220,9.025988,7.150310,-3.948425,1.639436,-5.582872,-5.226486,5.926955,-6.725932,6.318445,-9.500385,6.344945,-5.219399,-1.855921,0.553981,-4.062427,-9.165392,-5.591447,-4.853718,5.076585,7.761572,-1.405764,6.040800,7.960152,1.210474,3.100000,-4.040902,-7.935898,-4.041066,2.481855,7.999693,-7.180552,9.743950,-3.708138,-7.654616,3.930939,0.297013,5.416535,5.757321,-0.276739,7.808871,-0.721239,-5.906553,9.293595,-9.245682,-5.200519,-3.197453,6.780204,1.711769,7.333246,9.749228,5.965770,-8.589907,6.631483,0.725559,5.665007,8.771542,1.961535,-4.080402,7.755960,5.787356,-4.255685,-4.854206,2.317780,4.361716,3.400221,6.447432,5.668992,7.140675,1.462064,8.594231,-3.356443,-3.617449,-0.687024,-6.043003,5.045163,-1.980130,6.725943,3.331500,-7.353777,8.785058,8.010895,4.258951,3.881342,3.121188,4.434368,4.410248,-6.469871,1.141079,-0.970146,-3.221575,4.295292,4.645835,9.585847,4.077769,-2.494193,-9.345533,7.472151,-9.351803,-8.618457,7.079687,-1.695519,7.176879,9.545661,-9.989988,-5.284411,7.318193,1.328680,-4.422678,-7.434210,-0.124725,7.271559,-9.180815,-3.864462,4.996519,5.996336,4.755744,6.630473,-6.205888,2.645075,-5.959115,1.908292,-2.008125,-5.348582,3.064394,-2.274940,1.742254,-6.699428,4.096513,8.342466,-4.321743,5.306701,-0.682809,-3.571917,1.235471,8.365470,-0.384765,-5.323232,2.274880,0.798305,6.474791,2.485488,2.722699,-1.749996,-6.307140,5.386129,-4.548338,-9.932505,3.280566,8.179371,2.760453,-1.636664,6.662333,-0.557933,-8.721840,-5.168490,6.760927,-2.876224,0.567738,6.418700,-6.298077,-5.295792,-1.553556,-4.986077,-5.809095,-2.473371,-4.529101,3.369586,4.791191,5.744041,0.595296,8.526101,5.667957], dtype = "float32")#candidate|13355|(975,)|const|float32
call_13354 = relay.TupleGetItem(func_13081_call(relay.reshape(const_13355.astype('float32'), [13, 5, 15])), 4)
call_13356 = relay.TupleGetItem(func_13084_call(relay.reshape(const_13355.astype('float32'), [13, 5, 15])), 4)
output = relay.Tuple([call_13352,call_13354,const_13355,])
output2 = relay.Tuple([call_13353,call_13356,const_13355,])
func_13360 = relay.Function([], output)
mod['func_13360'] = func_13360
mod = relay.transform.InferType()(mod)
mutated_mod['func_13360'] = func_13360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13360_call = mutated_mod.get_global_var('func_13360')
call_13361 = func_13360_call()
output = call_13361
func_13362 = relay.Function([], output)
mutated_mod['func_13362'] = func_13362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13017_call = mod.get_global_var('func_13017')
func_13019_call = mutated_mod.get_global_var('func_13019')
call_13413 = func_13017_call()
call_13414 = func_13017_call()
func_2670_call = mod.get_global_var('func_2670')
func_2674_call = mutated_mod.get_global_var('func_2674')
var_13424 = relay.var("var_13424", dtype = "float64", shape = (280,))#candidate|13424|(280,)|var|float64
const_13425 = relay.const([6,7,-3,2,2,-6,-3,8,3,-4,3,-9,-6,-1,1,-1,9,-5,-10,6,-8,-6,7,-9,-9,9,3,-8,-8,4,-2,8,-6,-4,1,6,-4,10,-6,10,-2,-7,7,-5,-6,-6,-5,10,7,-8,5,10,6,-1,-1,-8,-1,9,2,-3,-3,9,-3,-1,-4,-1,-3,-10,-2,-1,-1,-5,6,10,-8,-8,-2,-2,7,-7,4,-10,8,-6,-1,3,-6,6,-4,1,9,-4,-8,6,-2,4,1,-3,-6,-9,-5,-10,-5,-4,3,1,-7,-3,-3,-10,-9,9,10,9,10,-4,-4,-10,3,8,-1,7,5,-3,-6,3,7,7,5,-7,6,2,8,-9,-5,-6,-5,2,-3,-10,8,-6,9,-6,1,-9,-5,-9,2,1,-4,-4,9,10,-3,-1,-6,-7,2,9,-5,2,-9,10,-8,9,-9,2,-10,-8,-5,-3,-5,5,-4,-3,-1,8,8,3,2,-10,6,-6,6,-9,-4,9,-3,-9,7,7,-8,1,-6,4,8,-8,7,3,2,2,4,-5,6,-7,7,4,-10,5,-1,3,-2,8,-7,-3,-2,-2,6,7,-3,-8,6,-10,-9,2,2,9,-6,-5,7,1,5,-8,-3,5,-7,8,7,2,3,-3,-7,2,1,-8,7,10,3,3,2,3,2,-5,-1,2,8,8,-2,-1,-10,-1,-6,-9,8,-6,1,-10,-1,10,9,-4,1,-4,-4,6,-4,1,10,1,-1,8,6,-4,10,-7,-10,-6,4,-4,5,-2,-10,10,-2,-10,8,6,-4,9,4,5,-6,5,-10,-8,-10,3,3,10,4,10,-5,-6,-5,-7,2,5,2,7,8,7,4,-5,-1,2,-4,7,-9,2,-9,-4,-10,8,6,4,-9,-1,-10,1,3,9,6,-9,-1,8,10,3,-1,-4,8,-1,8,1,-10,1,6,1,6,-6,10,10,-5,2,6,3,5,-1,7,2,4,9,3,-1,-9,-7,10,9,-2,9,8,-2,-7,-5,-4,-2,-10,6,2,-4,4,-9,1,-10,-10,1,-3,2,-3,-6], dtype = "uint8")#candidate|13425|(400,)|const|uint8
call_13423 = relay.TupleGetItem(func_2670_call(relay.reshape(var_13424.astype('float64'), [7, 10, 4]), relay.reshape(var_13424.astype('float64'), [7, 10, 4]), relay.reshape(const_13425.astype('uint8'), [400,]), ), 3)
call_13426 = relay.TupleGetItem(func_2674_call(relay.reshape(var_13424.astype('float64'), [7, 10, 4]), relay.reshape(var_13424.astype('float64'), [7, 10, 4]), relay.reshape(const_13425.astype('uint8'), [400,]), ), 3)
output = relay.Tuple([call_13413,call_13423,var_13424,const_13425,])
output2 = relay.Tuple([call_13414,call_13426,var_13424,const_13425,])
func_13470 = relay.Function([var_13424,], output)
mod['func_13470'] = func_13470
mod = relay.transform.InferType()(mod)
var_13471 = relay.var("var_13471", dtype = "float64", shape = (280,))#candidate|13471|(280,)|var|float64
output = func_13470(var_13471)
func_13472 = relay.Function([var_13471], output)
mutated_mod['func_13472'] = func_13472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13360_call = mod.get_global_var('func_13360')
func_13362_call = mutated_mod.get_global_var('func_13362')
call_13474 = relay.TupleGetItem(func_13360_call(), 2)
call_13475 = relay.TupleGetItem(func_13362_call(), 2)
output = call_13474
output2 = call_13475
func_13485 = relay.Function([], output)
mod['func_13485'] = func_13485
mod = relay.transform.InferType()(mod)
mutated_mod['func_13485'] = func_13485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13485_call = mutated_mod.get_global_var('func_13485')
call_13486 = func_13485_call()
output = call_13486
func_13487 = relay.Function([], output)
mutated_mod['func_13487'] = func_13487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12987_call = mod.get_global_var('func_12987')
func_12988_call = mutated_mod.get_global_var('func_12988')
call_13493 = relay.TupleGetItem(func_12987_call(), 2)
call_13494 = relay.TupleGetItem(func_12988_call(), 2)
func_7327_call = mod.get_global_var('func_7327')
func_7329_call = mutated_mod.get_global_var('func_7329')
const_13496 = relay.const([[6],[-3],[6],[-10],[-1],[-6],[7],[-4]], dtype = "int64")#candidate|13496|(8, 1)|const|int64
call_13495 = relay.TupleGetItem(func_7327_call(relay.reshape(const_13496.astype('int64'), [4, 1, 2])), 0)
call_13497 = relay.TupleGetItem(func_7329_call(relay.reshape(const_13496.astype('int64'), [4, 1, 2])), 0)
func_3544_call = mod.get_global_var('func_3544')
func_3548_call = mutated_mod.get_global_var('func_3548')
const_13500 = relay.const(5, dtype = "uint8")#candidate|13500|()|const|uint8
const_13501 = relay.const([9,10,-3,-8,2,-7,-7,4,4,-2,7,10,1,9,-5,-3,-6,-10,7,-1,5,3,-10,6,6,3,-9,1,-10,-5,9,-9,-2,-5,8,7,-3,-7,-9,6,-3,1,1,-2,-6,-8,-7,-1,8,8,-1,9,-7,-8,-9,2,-3,-6,8,-5,-4,-9,-10,10,6,3,-2,3,1,4,6,-4,2,5,-7,-2,5], dtype = "uint8")#candidate|13501|(77,)|const|uint8
call_13499 = relay.TupleGetItem(func_3544_call(relay.reshape(const_13500.astype('uint8'), []), relay.reshape(const_13501.astype('uint8'), [11, 1, 7]), ), 1)
call_13502 = relay.TupleGetItem(func_3548_call(relay.reshape(const_13500.astype('uint8'), []), relay.reshape(const_13501.astype('uint8'), [11, 1, 7]), ), 1)
func_5136_call = mod.get_global_var('func_5136')
func_5140_call = mutated_mod.get_global_var('func_5140')
const_13521 = relay.const([1,-1,-4,3,4,6,1,-1,4,5,2,7,10,8,5,6,-5,-6,-10,6,6,-2,-9,-4,-5,-10,-5,-8,-3,7,-4,-5,-9,-5,-9,-7,-4,-4,1,9,-6,-4,-7,6,-1,-9,5,5,4,-7,2,10,2,-2,-1,-1,-1,8,1,6,-8,-8,-9,-10,-2,8,10,3,-1,9,7,10,4,4,3,-7,4,-5,8,-8,2,-8,3,6,-8,7,-4,-1,-9,6,-4,-5,8,-3,-5,9,-8,-2,10,-6,-3,-2,-4,-7,-10,4,-6,4,9,2,-10,-3,-10,9,3,8,10,2,3,-4], dtype = "int64")#candidate|13521|(120,)|const|int64
var_13522 = relay.var("var_13522", dtype = "int64", shape = (720, 1))#candidate|13522|(720, 1)|var|int64
const_13523 = relay.const([-2,-7,-5,1,-4,-8,-9,2,-8,-6,9,10,6,1,1,-2,-2,5,1,7,-5,6,5,-3,-4,-8,10,-3,2,-10,5,7,3,5,7,1,-8,-9,4,4,1,-1,1,-5,9,9,1,9,7,-10,-7,-8,8,6,7,10,-3,7,6,-9,1,-6,4,-6,3,-5,7,-7,-9,6,4,-6,-8,1,6,8,-9,-10,4,-4,-2,-9,-2,-3,-1,1,-9,-2,-9,-3,-4,4,9,-6,2,2,-1,-4,-7,-6,-9,4,3,5,9,-8,-10,6,-8,2,2,-5,-5,8,5,-2,2,-10,-4,-8,6,-5,10,-6,6,10,2,-3,-2,2,-4,2,2,10,1,-8,5,1,-7,-6,7,-2,-1,9,-5,-3,-5,4,8,-3,3,-6,-7,6,6,-6,9,-3,3,8,-2,7,-7,-5,5,6,1,6,8,1,-3,-8,-7,5,-4,-9,3,4,-7,6,8,7,3,7,-3,-7,7,9,8,-5,-6,-9,-10,-10,3,-6,8,-2,9,6,10,-10,-1,-3,4,3,2,-10,4,-9,6,2,1,8,-5,-3,10,-4,-2,-1,-6,-8,-6,-3,8,1,-7,9,7,9,-2,9,-6,2,-3,-8,-7,7,5,-6,-2,-9,10,-1,5,-10,-4,8,5,10,3,7,2,-7,-6,2,-2,8,-8,8,1,-10,-1,3,-8,-4,-10,-5,6,1,-5,-1,3,8,10,-5,-5,4,-1,2,1,-2,-8,5,-7,6,-1,-8,6,-8,-3,5,-5,-6,9,8,5,-1,5,6,4,5,-1,-10,8,-3,-10,-10,9,-3,-3,8,-3,2,-7,-1,4,-6,8,10,-3,-8,1,-8,-4,-9,-6,-7,-8,-6,-9,5,4,6,9,-9,-9,5,-4,10,-8,5,8,2,2,10,-6,5,-8,1,7,10,-8,5,2,10,-8,3,-10,9,-2,1,6,5,7,1,-5,-1,8,4,5,7,2,7,-4,2,-7,-3,1,7,3,5,9,-2,3,-4,-4,10,-2,10,5,-1,6,-7,1,8,-2,-5,-8,7,-6,10,3,-8,6,2,-9,-6,-6,-6,7,-4,-9,-1,7,-8,10,-3,-7,9,-8,-5,-3,-5,-3,9,-7,8,-1,2,-6,10,-8,10,-5,-9,9,3,-6,-4,-9,1,-3,9,8,9,4,10,4,9,7,4,3,-10,4,-10,-7,9,9,-2,-1,-1,-2,-7,8,-6,4,-3,-7,-8,8,-4,-10,-3,-10,6,-7,6,-5,-6,7,-10,-3,-9,-7,-1,-6,10,-7,5,-9,1,-9,7,-10,-8,6,9,10,-8,-3,-2,4,-5,4,-10,-2,-8,8,4,10,-4,-2,6,10,-9,-4,2,-4,1,-8,10,6,10,5,1,-7,-2,9,-1,3,-2,2,9,2,3,-2,9,-4,3,2,-7,-10,-6,-8,-8,6,1,5,-3,9,6,-10,1,-3,-3,8,-1,-10,9,-3,-2,8,-8,-3,-1,-6,6,-3,10,-1,8,5,-10,-6,7,-6,2,-2,9,1,10,9,3,-4,6,8,-7,-5,1,5,-3,-7,-7,5,-6,5,6,-1,6,2,3,7,-4,-6,-4,-3,6,-5,-8,-8,-9,-2,7,-3,-9,6,-6,1,-7,-7,1,-1,-9,-9,-7,5,10,-10,-1,1,-8,1,3,-6,-2,-1,-4,-10,-9,3,-4,5,-4,-2,-9,-4,-1,3,-8,2,3,-2,8,-1,9,-6,-10,8,7,8,2,-3,8,4,-6,-7,2,7,1,10,1,6,8,-9,3,-8,-1,7,6,5,-10,2,-2,-3,-6,3,-10,3,3,10,9,-1,9,-8,-1,-9,-5,-2,-10,10,-9,-5,3,4,8,-2,-4,-7,-2,7,10,-2,-7,-2,1,-4,6,-1,7,-5,-1,-4,-1,-7,-6,4,-10,-10,5,5,5,-8,9,2,-7,1,-3,3,7,-4,-4,-8,-7,3,-4,9,10,-2,7,4,-10,-1,1,-4,-2,1,9,2,2,9,6,7,5,4,5,7,-3,6,-2,4,1,2,7,-7,9,-4,5,-8,1,4,10,-1,10,8,-10,-8,8,-2,-1,-1,-8,-5,6,-3,7,-3,1,-9,3,-2,2,5,-9,-2,-7,-3,1,8,-3,-6,-10,-7,-5,1,6,9,5,-7,-1,7,3,5,-7,-1,5,9,8,-8,4,9,5,7,3,4,-4,-4,-10,3,3,8,-3,7,4,-2,-7,8,10,1,3,7,-8,-4,-1,6,3,4,-10,7,8,-2,-2,-6,10,-6,-7,-10,-6,-3,-1,3,-4,8,-9,8,6,-4,-4,1,-10,-7,-3,-1,-1,-8,-5,4,9,3,-9,-7,3,-3,2,3,2,8,-6,6,5,-10,4,-10,-10,-1,6,-3,-9,-7,10,-10,1,10,7,7,-8,4,2,5,9,-10,5,-5,2,3,6,-6,3,4,-2,4,9,5,4,-3,7,-7,1,-7,7,-6,-7,-8,10,2,5,5,-6,5,-10,10,-4,-10,-10,-7,-10,10,5,8,1,9,-6,2,-3,-1,-7,-2,9,-7,10,-7,-7,6,6,9,-3,-5,-1,10,-6,-8,-1,6,-2,-10,7,5,-4,-7,-6,-8,-3,8,2,9,-1,10,9,4,9,8,-1,1,3,-6,2,-9,-8,10,-7,7,8,-1,-5,10,7,1,10,-5,-10,3,-4,-7,-9,2,8,3,-7,2,-9,6,-10,-6,-1,-3,-10,2,-9,8,-8,6,-2,-1,-3,-10,7,8,7,10,-5,-6,1,10,-9,-8,1,-2,-2,1,-7,-8,1,4,2,-5,-6,1,-10,-7,-3,5,-8,-6,-1,-8,2,-5,-5,-2,-2,3,7,-7,-7,6,-9,6,2,-10,1,-3,5,9,-6,5,5,8,-4,-10,9,-2,1,-6,2,-5,-3,7,8,-5,6,-4,2,4,9,8,2,-6,10,5,9,4,-10,-9,-8,3,-8,4,1,5,-3,-5,5,-9,3,-4,6,4,10,4,-2,9,-6,-10,-10,-4,-8,-10,-2,5,-3,-10,8,6,-9,-3,9,-1,-4,1,-3,-8,6,3,7,5,-8,10,9,1,8,1,7,-4,2,-8,-2,8,-4,-8,-1,-2,8,-3,10,6,-10,-5,10,10,7,-9,-4,-9,-9,1,7,-7,7,-3,7,-5,8,-6,1,10,-3,9,7,-8,-2,-4,-4,4,-4,8,-8,-8,3,5,-1,-4,-6,-2,8,7,8,-10,6,-4,3,-2,3,5,6,-1,-7,-1,-7,-5,-2,-4,-6,3,-8,-2,8,-2,-6,8,7,8,6,8,-2,-8,-5,-7,7,-3,-8,8,9,-9,-6,-8,6,-8,7,6,9,6,-6,-3,4,10,10,-7,9,-7,-3,-8,3,3,-4,-1,-3,-4,-1,-4,4,-8,3,5,-3,4,7,7,2,2,-9,8,2,-2,3,-10,9,3,-5,-3,3,4,-1,-2,1,10,8,3,-4,-5,-9,3,-4,10,-5,10,10,9,-5,6,-6,-5,6,4,-2,-6,5,9,-6,-9,-3,10,-2,-9,-10,4,-3,10,-6,-9,5,-9,3,-10,-10,1,-9,-9,9,-10,2,7,-3,-5,5,-9,-9,1,-10,-2,-1,4,-3,-10,2,1,4,-9,7,9,-10,-2,-9,-1,-3,9,-8,-1,7,-3,-3,-3,4,-7,-10,3,-5,8,-10,-2,4,7,6,2,1,-4,-10,3,-3,-7,7,10,6,7,-7,-9,2,-2,3,-4,9,-1,7,5,8,-10,3,-8,-9,7,4,6,1,4,4,-2,-8,-2,-9,-4,6], dtype = "int8")#candidate|13523|(1440,)|const|int8
call_13520 = relay.TupleGetItem(func_5136_call(relay.reshape(const_13521.astype('int64'), [12, 10, 1]), relay.reshape(var_13522.astype('int64'), [12, 10, 6]), relay.reshape(const_13523.astype('int8'), [1440,]), ), 0)
call_13524 = relay.TupleGetItem(func_5140_call(relay.reshape(const_13521.astype('int64'), [12, 10, 1]), relay.reshape(var_13522.astype('int64'), [12, 10, 6]), relay.reshape(const_13523.astype('int8'), [1440,]), ), 0)
output = relay.Tuple([call_13493,call_13495,const_13496,call_13499,const_13500,const_13501,call_13520,const_13521,var_13522,const_13523,])
output2 = relay.Tuple([call_13494,call_13497,const_13496,call_13502,const_13500,const_13501,call_13524,const_13521,var_13522,const_13523,])
func_13527 = relay.Function([var_13522,], output)
mod['func_13527'] = func_13527
mod = relay.transform.InferType()(mod)
mutated_mod['func_13527'] = func_13527
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13528 = relay.var("var_13528", dtype = "int64", shape = (720, 1))#candidate|13528|(720, 1)|var|int64
func_13527_call = mutated_mod.get_global_var('func_13527')
call_13529 = func_13527_call(var_13528)
output = call_13529
func_13530 = relay.Function([var_13528], output)
mutated_mod['func_13530'] = func_13530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13360_call = mod.get_global_var('func_13360')
func_13362_call = mutated_mod.get_global_var('func_13362')
call_13550 = relay.TupleGetItem(func_13360_call(), 1)
call_13551 = relay.TupleGetItem(func_13362_call(), 1)
output = relay.Tuple([call_13550,])
output2 = relay.Tuple([call_13551,])
func_13565 = relay.Function([], output)
mod['func_13565'] = func_13565
mod = relay.transform.InferType()(mod)
mutated_mod['func_13565'] = func_13565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13565_call = mutated_mod.get_global_var('func_13565')
call_13566 = func_13565_call()
output = call_13566
func_13567 = relay.Function([], output)
mutated_mod['func_13567'] = func_13567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12987_call = mod.get_global_var('func_12987')
func_12988_call = mutated_mod.get_global_var('func_12988')
call_13617 = relay.TupleGetItem(func_12987_call(), 1)
call_13618 = relay.TupleGetItem(func_12988_call(), 1)
output = relay.Tuple([call_13617,])
output2 = relay.Tuple([call_13618,])
func_13624 = relay.Function([], output)
mod['func_13624'] = func_13624
mod = relay.transform.InferType()(mod)
mutated_mod['func_13624'] = func_13624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13624_call = mutated_mod.get_global_var('func_13624')
call_13625 = func_13624_call()
output = call_13625
func_13626 = relay.Function([], output)
mutated_mod['func_13626'] = func_13626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12987_call = mod.get_global_var('func_12987')
func_12988_call = mutated_mod.get_global_var('func_12988')
call_13629 = relay.TupleGetItem(func_12987_call(), 2)
call_13630 = relay.TupleGetItem(func_12988_call(), 2)
var_13664 = relay.var("var_13664", dtype = "float32", shape = (975,))#candidate|13664|(975,)|var|float32
bop_13665 = relay.bitwise_or(call_13629.astype('int8'), relay.reshape(var_13664.astype('int8'), relay.shape_of(call_13629))) # shape=(975,)
bop_13668 = relay.bitwise_or(call_13630.astype('int8'), relay.reshape(var_13664.astype('int8'), relay.shape_of(call_13630))) # shape=(975,)
func_10565_call = mod.get_global_var('func_10565')
func_10570_call = mutated_mod.get_global_var('func_10570')
const_13684 = relay.const([-6,9,4,-5,-6,-1,-8,-6,1,-9,4,-10,-6,5,10,8,-10,10,-9,-5,5,5,-6,-4,-6,10,8,-1,8,8,10,4,2,-2,-8,8,-2,7,-6,5,-3,10,-4,8,8,8,1,-8,7,-6,6,10,-6,7,7,-4,6,4,8,2,7,4,3,10,1,-6,-9,6,-5,-7,-7,-5,-6,5,-10,-10,6,-6,3,10,2,-10,4,6,10,-4,-6,-4,-7,-6,5,-7,-7,1,-10,3,-8,-5,-10,-4,4,-1,-8,-3,-3,5,5,10,-4,4,-1,6,-2,6,1,6,9,-8,-2,3,1,3,9,-10,4,6,10,9,-2,6,4,-1,-7,1,1,5,1,8,3,2,1,-7,2,5,-10,9,10,10,-10,-9,4,-3,-5,-4,8,-8,-5,-9,2,3,2,-7,-6,2,-9,-9,8,-9,-10,1,-10,-6,-5,-4,-7,-8,-2,3,-3,4,-9,-4,-4,8,-5,-3,-8,-4,3,8,6,1,3,6,3,8,4,9,-5,3,5,-9,-6,-4,10,1,9,3,-9,10,2,4,-1,5,9,8,-7,-7,-9,-2,-4,-4,-8,-7,-10,9,-6,-10,-7,3,-5,1,7,3,-8,4,9,-7,4,3,4,6,6,-6,-10,-10,9,7,7,3,-6,-9,2,-3,3,-2,10,4,-5,9,-9,-10,-10,6,6,7,4,-10,-4,-7,-9,-4,1,4,-10,1,6,10,10,-5,5,10,-10,8,-3,2,5,10,-6,2,-1,-5,-4,-3,3,1,-2,7,-1,-5,-3,-8,-1,-4,5,2,9,-3,4,-7,5,-3,3,6,-9,10,-8,-10,-7,7,-2,-7,6,-6,-7,-5,5,1,10,-1,10,2,-8,-6,-1,-6], dtype = "int16")#candidate|13684|(336,)|const|int16
var_13685 = relay.var("var_13685", dtype = "uint8", shape = (400,))#candidate|13685|(400,)|var|uint8
call_13683 = relay.TupleGetItem(func_10565_call(relay.reshape(const_13684.astype('int16'), [7, 16, 3]), relay.reshape(const_13684.astype('int16'), [7, 16, 3]), relay.reshape(var_13685.astype('uint8'), [400,]), ), 1)
call_13686 = relay.TupleGetItem(func_10570_call(relay.reshape(const_13684.astype('int16'), [7, 16, 3]), relay.reshape(const_13684.astype('int16'), [7, 16, 3]), relay.reshape(var_13685.astype('uint8'), [400,]), ), 1)
uop_13687 = relay.sqrt(call_13683.astype('float64')) # shape=(7, 16, 3)
uop_13689 = relay.sqrt(call_13686.astype('float64')) # shape=(7, 16, 3)
func_4654_call = mod.get_global_var('func_4654')
func_4656_call = mutated_mod.get_global_var('func_4656')
var_13701 = relay.var("var_13701", dtype = "float32", shape = (66,))#candidate|13701|(66,)|var|float32
call_13700 = func_4654_call(relay.reshape(var_13701.astype('float32'), [1, 11, 6]))
call_13702 = func_4654_call(relay.reshape(var_13701.astype('float32'), [1, 11, 6]))
output = relay.Tuple([bop_13665,const_13684,var_13685,uop_13687,call_13700,var_13701,])
output2 = relay.Tuple([bop_13668,const_13684,var_13685,uop_13689,call_13702,var_13701,])
func_13718 = relay.Function([var_13664,var_13685,var_13701,], output)
mod['func_13718'] = func_13718
mod = relay.transform.InferType()(mod)
mutated_mod['func_13718'] = func_13718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13718_call = mutated_mod.get_global_var('func_13718')
var_13720 = relay.var("var_13720", dtype = "float32", shape = (975,))#candidate|13720|(975,)|var|float32
var_13721 = relay.var("var_13721", dtype = "uint8", shape = (400,))#candidate|13721|(400,)|var|uint8
var_13722 = relay.var("var_13722", dtype = "float32", shape = (66,))#candidate|13722|(66,)|var|float32
call_13719 = func_13718_call(var_13720,var_13721,var_13722,)
output = call_13719
func_13723 = relay.Function([var_13720,var_13721,var_13722,], output)
mutated_mod['func_13723'] = func_13723
mutated_mod = relay.transform.InferType()(mutated_mod)
const_13727 = relay.const([[[8.542651,-1.369858,8.901402,4.899914,-2.774854,6.295425,-0.688228,-1.964255,-7.374950,7.288772,1.888110,-7.426627,-3.571426,7.568039,9.531507,2.331268],[7.725578,-6.598786,9.596706,8.877168,-6.337669,-9.309508,-7.999534,-5.564482,3.126538,-9.649080,3.761370,6.483934,7.197039,-0.802337,-6.289627,-8.986436],[-2.458443,-0.220423,-9.130474,2.919426,-0.926899,2.228372,-9.680401,-2.013589,4.218562,-8.067002,3.061747,-0.989382,-5.417600,1.768857,-2.263573,-0.860260],[-9.435392,-3.278999,2.941949,6.726499,1.744181,-6.474457,-2.230014,-6.741112,4.713302,6.720211,-9.340491,-6.359556,-4.592397,4.158709,3.582191,1.778950]],[[4.919897,-9.647072,0.840947,-1.871873,-0.676530,7.027509,0.696079,-3.246951,-7.300524,9.643507,4.554175,-5.954278,4.128679,-4.556379,3.250533,-5.923915],[-8.078390,6.577413,-5.615315,-7.155354,-2.500816,-5.455779,3.428759,0.653904,-2.184772,6.292934,-0.760391,1.706203,1.257874,-0.232630,-8.424081,7.243858],[7.027926,-4.768144,9.082715,-1.406409,-7.401099,1.083567,7.366598,-1.767667,-1.932267,2.617690,0.692939,-5.525066,-3.324019,6.640373,-8.234952,5.000517],[-5.156012,2.541922,8.201590,0.157166,-1.484330,7.694022,6.895843,8.700893,4.911623,-2.641263,-8.806433,-0.817004,9.351366,8.419562,-7.634111,0.555907]],[[-5.827761,-1.080113,-4.630948,-7.495286,7.335242,-2.477090,7.893459,-8.387264,-3.555113,6.766390,3.064631,-0.763630,2.710648,-2.141536,-1.454016,-4.543062],[0.938201,-8.184031,4.330209,-8.824462,2.475761,8.706142,1.023840,0.056346,1.985912,-3.288155,-4.557346,0.728287,-5.434475,-7.659608,-7.222198,2.515750],[2.927480,2.177495,-7.454090,9.202551,5.201200,-4.523070,-4.282341,-3.886876,-3.234899,6.960020,4.800220,0.267707,-3.628064,8.195683,-8.905211,-4.090861],[-2.575800,-8.328424,-0.807072,-2.757677,3.494587,-1.861725,9.145510,4.632797,8.269772,-6.283973,5.330270,-5.132270,1.393132,-6.523105,-6.558735,-7.937614]],[[1.194775,-7.229729,-1.182806,7.689396,6.566717,-2.395421,-3.282019,5.947838,-3.516468,4.502499,0.473212,3.391654,8.360092,-7.410180,7.099454,-6.494450],[-9.218367,-6.940978,-0.072608,-7.427278,8.854206,-4.697063,-6.817638,6.400569,6.071443,-4.720180,-7.461163,-7.537398,-1.635835,9.625073,2.294372,-1.219113],[-2.327536,-3.381845,-9.948341,7.270692,8.178532,3.905646,2.561661,-1.935270,5.888458,8.921467,7.246857,8.352201,-9.261497,4.421681,9.844736,6.003208],[-9.377354,-5.602010,-2.582653,-4.339140,8.362548,1.292280,-6.957963,6.765319,7.981272,7.624669,-8.834190,-2.687854,8.802936,-9.688121,0.134542,3.612415]],[[-1.029390,-0.166593,7.707496,-8.587671,-7.735192,6.376247,-9.916323,0.772442,2.278289,-0.627910,1.388421,-1.138727,-0.982967,2.824154,4.243770,5.216124],[-8.025619,-1.921115,-6.516618,-5.701288,1.128445,0.506937,6.343383,7.362064,9.522225,-6.464356,-0.819076,7.802619,-6.895643,-5.111107,5.566598,8.799030],[7.655642,4.279976,-5.607000,-0.689222,5.119536,8.376835,-2.837639,1.146091,-5.301424,1.258159,0.712348,8.542315,1.499145,0.063510,8.362999,3.297792],[-5.522706,-0.137421,-1.950855,-1.115885,-0.744671,-4.150513,-8.292881,-3.390805,-0.631860,2.791887,8.253956,8.359720,-9.387241,0.966362,7.292730,-2.979677]],[[-0.883027,-8.134455,-3.528186,-6.731635,8.746037,1.138332,7.251591,-6.294184,0.117672,4.778622,7.460241,-8.763372,3.543145,5.415574,-6.062881,-6.715314],[6.342059,2.924447,-2.421372,-8.974634,5.495791,8.964236,-1.384435,-8.388725,-8.243698,-7.261806,-4.798962,9.912244,-8.724457,-8.330671,9.706188,3.078361],[9.002963,-1.476944,7.001190,1.123169,-9.128857,0.178260,6.955538,1.795247,8.988475,8.891682,-1.834703,9.141570,8.426834,4.154954,-2.927476,6.393433],[3.385853,3.057195,6.254637,2.569110,-4.151617,-6.736308,-0.424399,7.441204,4.863630,1.368261,5.896976,-6.724615,-4.179678,9.886071,0.475937,8.660605]],[[-0.127214,5.598661,6.429104,-4.916519,8.891358,6.146693,-5.454839,8.986337,6.193799,6.349993,0.519593,-4.402948,1.658085,-3.553785,-2.020049,8.537821],[7.231112,-6.137449,-2.320881,-3.472282,2.913674,0.132531,-7.668565,0.436121,-1.838692,-7.575648,1.384963,5.418722,0.585500,8.796687,0.448639,-4.380041],[8.541852,-8.160568,0.287313,9.275204,-2.610582,-8.572274,6.024410,9.095242,-5.590118,1.423583,-3.535410,-1.781299,-2.609205,9.027074,5.281736,-5.933943],[9.822904,-0.199888,2.974682,9.916450,-1.908774,-3.480346,-4.637988,7.917072,-5.623421,-5.577749,-7.376724,-2.633056,-4.816302,-1.763874,2.370817,-8.375224]],[[8.271960,-4.042376,-1.990856,5.860331,1.927948,-2.150037,6.751511,9.519372,-4.900341,-3.333173,-3.186537,1.634629,-4.331276,-7.421503,6.033999,-6.457322],[6.092216,1.448888,4.572541,7.519904,1.733093,-5.706427,2.566624,-9.246212,2.370649,-8.376340,9.972223,-6.280962,-3.700971,7.504175,9.360936,-8.175535],[-7.210216,-1.727251,-4.895049,8.376470,0.933230,-7.784746,0.190996,-5.595565,5.946937,-8.005116,-9.445431,3.516843,-8.928298,-3.657692,-4.338996,-5.749885],[0.330634,-6.038939,-7.513372,5.917917,5.841854,2.606530,-4.654813,8.075047,-9.828062,-8.329599,-2.667383,5.241385,-4.665930,-2.617900,6.010102,-1.415076]],[[3.131215,-1.177523,-8.354875,4.816787,-8.635325,-4.281045,-9.059494,-8.825400,7.872834,-0.471460,-6.870454,-7.662643,5.246819,-8.260911,-1.093047,7.836325],[8.984031,7.498273,2.117755,-8.919624,0.166171,-8.591251,-6.898192,2.907124,0.113072,-2.286318,5.922146,0.720340,8.673807,2.029696,-5.233305,-1.501052],[0.166942,5.464950,-9.562574,-6.930285,-5.705718,-8.756814,7.258838,-7.715356,7.759195,6.620816,-2.772981,2.828747,-0.135977,6.293450,-0.677665,-3.212549],[1.158819,-5.144642,6.407801,-3.023785,-2.126026,6.818124,-6.741021,-1.358721,-4.842089,-2.577421,-4.625014,-7.020370,1.942101,5.610774,3.285142,3.450283]],[[0.998444,7.708147,-1.090069,-1.165925,-7.122139,-6.924445,-7.152655,-3.389026,-8.398574,6.061895,-9.279345,7.181809,8.612553,0.218261,9.116007,4.988030],[2.052844,1.096981,-6.819315,-1.797819,1.156675,9.142113,5.300005,-9.576464,1.006177,2.245363,-6.631920,4.276611,5.163586,-3.783257,4.356561,-2.965534],[-6.418269,-6.063517,8.525300,5.094164,7.677029,-2.788940,-2.597369,2.129540,-9.759724,-4.789239,5.858849,-4.141147,-9.021356,3.834752,0.406679,-1.083036],[-8.242282,-7.922701,6.950792,-6.542261,2.517570,-1.512329,-8.972752,2.970498,-9.947467,9.123431,2.913038,-0.662997,-9.084969,4.529278,9.057874,-5.182146]],[[-1.927244,-2.690863,-3.311522,-5.914959,0.291601,-8.914546,-2.884627,3.363100,5.248826,5.427503,-1.308071,-6.847071,6.685068,-4.834616,-9.857705,-9.281272],[-2.955007,-4.221980,-0.410723,-3.914788,9.336576,1.612702,-7.187781,-0.715236,9.621133,-2.447326,-8.013938,-3.092802,-3.761670,-8.152587,1.619574,8.971492],[3.574266,1.762872,-4.258329,-6.269646,-7.651973,-4.398354,-5.701940,-6.302991,-7.373880,5.726649,0.033546,-0.132850,2.509743,-3.756543,-0.333153,-1.500207],[-5.408411,8.880040,0.866342,-1.886355,3.532806,-1.545884,-4.523886,2.931803,6.990699,9.623586,-2.276300,-5.645641,-6.032855,4.876656,-5.249917,0.834363]],[[4.645710,1.820462,-3.754570,-4.095366,-0.485896,7.905616,8.953029,0.409537,4.481078,8.957729,1.925517,7.127520,3.115590,-9.331597,-3.520822,-0.735645],[-6.842380,-7.157535,0.278934,-2.422029,1.754310,-5.332778,-9.461381,1.811722,-7.775675,0.505219,-3.528738,-4.276633,3.840577,3.302855,-6.269805,4.074404],[-5.938085,2.610076,-5.059186,0.389999,3.202623,-8.597135,-9.906129,2.727959,4.628939,-4.291785,-4.255471,0.547156,1.542194,7.637385,-5.373108,-5.794147],[6.551164,-7.758380,2.898607,6.204799,-4.969381,-2.022271,-1.716868,8.251535,-9.378911,3.524641,-7.837568,8.792323,-0.954832,5.427579,1.646029,3.601089]],[[1.645321,7.517967,4.600989,1.274304,-2.405333,-0.191150,-0.915654,-1.329818,5.126485,4.447198,-1.855343,2.453257,7.857242,8.610121,-7.602027,9.971101],[1.867138,-4.810727,-7.489234,-9.539984,3.601358,1.230820,-3.218752,2.806972,9.798540,-9.518166,0.878558,-3.694690,-5.635315,4.368594,-5.369730,8.802439],[2.638164,0.769389,0.537103,3.095408,-4.456444,-8.279335,-6.024965,0.682582,-0.584965,-0.400777,8.570667,8.878720,-5.391023,5.609245,4.683351,-7.362624],[-8.411180,-3.769208,1.822835,0.315669,-2.230705,0.948867,0.252689,2.151117,-4.442790,3.163363,-8.828038,5.545640,9.292300,-9.458719,1.525678,-3.749824]],[[-8.434092,-1.096954,-8.828292,2.632551,5.555635,7.008050,7.365024,4.391752,-4.736438,-3.434176,6.320632,-4.858228,-4.283171,7.190403,6.815474,8.532888],[4.001130,-2.631593,1.752400,-5.455832,-8.637209,5.791534,-0.031255,1.264222,5.166148,-0.916535,7.843195,-2.726851,6.838614,-9.953318,7.714614,-3.513597],[9.677805,-1.641576,-5.157191,8.155327,-4.072332,5.365980,0.979146,-3.881735,-2.322092,8.791777,8.318375,7.054955,-8.556401,4.220007,8.204729,-7.810987],[-6.157268,-4.642010,0.902180,6.071602,-9.180200,3.844646,9.251891,1.105076,-9.954372,-3.959349,-2.944633,-8.009627,5.747749,-1.028358,5.720600,3.036327]],[[3.879318,-4.900378,5.993812,-1.973665,-9.855598,-4.799325,1.225439,0.930082,-9.235724,1.210360,6.459278,6.656625,-3.389841,-7.299042,-9.738050,6.305495],[4.361303,8.731492,-7.092215,-1.103104,1.594140,-1.823744,-2.131582,-2.772949,9.518744,3.361382,3.780154,3.056531,-7.397810,2.835944,9.488555,-8.536277],[-4.682906,-2.835038,-8.959025,-6.593388,4.385945,-3.663968,-4.473821,-7.717766,6.243004,8.325204,3.239547,-6.366921,-4.687702,-4.676194,-6.838523,-8.319116],[-9.610403,9.764064,2.978534,-2.696959,4.325025,6.727885,9.069376,4.652345,3.015603,0.410628,-9.588054,0.314958,4.748801,-0.477261,-7.786230,9.554690]]], dtype = "float64")#candidate|13727|(15, 4, 16)|const|float64
uop_13728 = relay.atanh(const_13727.astype('float64')) # shape=(15, 4, 16)
uop_13731 = relay.sinh(uop_13728.astype('float64')) # shape=(15, 4, 16)
output = uop_13731
output2 = uop_13731
func_13749 = relay.Function([], output)
mod['func_13749'] = func_13749
mod = relay.transform.InferType()(mod)
mutated_mod['func_13749'] = func_13749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13749_call = mutated_mod.get_global_var('func_13749')
call_13750 = func_13749_call()
output = call_13750
func_13751 = relay.Function([], output)
mutated_mod['func_13751'] = func_13751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13017_call = mod.get_global_var('func_13017')
func_13019_call = mutated_mod.get_global_var('func_13019')
call_13777 = func_13017_call()
call_13778 = func_13017_call()
output = call_13777
output2 = call_13778
func_13780 = relay.Function([], output)
mod['func_13780'] = func_13780
mod = relay.transform.InferType()(mod)
output = func_13780()
func_13781 = relay.Function([], output)
mutated_mod['func_13781'] = func_13781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13624_call = mod.get_global_var('func_13624')
func_13626_call = mutated_mod.get_global_var('func_13626')
call_13846 = relay.TupleGetItem(func_13624_call(), 0)
call_13847 = relay.TupleGetItem(func_13626_call(), 0)
func_13624_call = mod.get_global_var('func_13624')
func_13626_call = mutated_mod.get_global_var('func_13626')
call_13849 = relay.TupleGetItem(func_13624_call(), 0)
call_13850 = relay.TupleGetItem(func_13626_call(), 0)
func_4654_call = mod.get_global_var('func_4654')
func_4656_call = mutated_mod.get_global_var('func_4656')
const_13854 = relay.const([7.824010,5.384930,-3.541185,2.920581,-6.753311,8.415011,4.846721,6.934084,-5.192497,7.203883,6.089108,-6.035923,-6.310693,-9.517976,5.736386,-0.127304,6.692321,-0.126280,6.358650,-5.941273,-1.912396,6.538939,5.127546,-6.076275,-1.030021,4.281593,2.899518,6.899600,-7.803222,9.990591,8.042534,-5.074206,-9.146861,-4.640136,-5.167238,9.501852,-0.900564,7.047496,0.090758,3.244466,2.413053,-8.221555,8.104794,-9.140060,1.951197,3.477167,-8.128532,2.666267,-3.496872,-4.687880,0.354415,4.937670,-5.380900,7.594934,8.564417,7.947584,6.381698,3.716052,2.489300,8.002550,-9.275834,3.609196,-8.673590,4.642299,1.544225,-5.206476], dtype = "float32")#candidate|13854|(66,)|const|float32
call_13853 = func_4654_call(relay.reshape(const_13854.astype('float32'), [1, 11, 6]))
call_13855 = func_4654_call(relay.reshape(const_13854.astype('float32'), [1, 11, 6]))
func_2363_call = mod.get_global_var('func_2363')
func_2367_call = mutated_mod.get_global_var('func_2367')
var_13861 = relay.var("var_13861", dtype = "bool", shape = ())#candidate|13861|()|var|bool
var_13862 = relay.var("var_13862", dtype = "bool", shape = (22,))#candidate|13862|(22,)|var|bool
call_13860 = relay.TupleGetItem(func_2363_call(relay.reshape(var_13861.astype('bool'), []), relay.reshape(var_13862.astype('bool'), [2, 11, 1]), ), 0)
call_13863 = relay.TupleGetItem(func_2367_call(relay.reshape(var_13861.astype('bool'), []), relay.reshape(var_13862.astype('bool'), [2, 11, 1]), ), 0)
func_7809_call = mod.get_global_var('func_7809')
func_7811_call = mutated_mod.get_global_var('func_7811')
var_13865 = relay.var("var_13865", dtype = "float64", shape = (273,))#candidate|13865|(273,)|var|float64
call_13864 = relay.TupleGetItem(func_7809_call(relay.reshape(var_13865.astype('float64'), [7, 13, 3])), 0)
call_13866 = relay.TupleGetItem(func_7811_call(relay.reshape(var_13865.astype('float64'), [7, 13, 3])), 0)
func_11960_call = mod.get_global_var('func_11960')
func_11964_call = mutated_mod.get_global_var('func_11964')
const_13869 = relay.const([[-5.137860,-3.807351,-1.010213,1.002977,2.211932,-3.444363,-8.310659,2.796744,3.221652,-9.151980,-6.369131,5.542618,7.751177,5.361398,-4.773574,-5.076594,-7.874757,2.368034,2.270314,0.659018],[-1.649190,3.629851,-1.226355,-2.453169,-5.077565,8.056300,4.346161,-3.269943,2.789733,-6.087465,8.587200,9.577491,1.151989,-4.490314,7.254230,3.432176,5.472680,-8.558296,-2.164778,-9.857816],[-2.362826,6.579314,-3.396334,-6.479647,-2.145544,-1.817386,5.026976,2.455366,-4.196933,2.833906,7.721189,-3.241196,4.685386,-0.600359,8.357345,-3.639526,8.435929,1.774873,-2.484214,6.405581],[-6.141420,-3.919223,6.496347,-8.710585,7.729695,5.799725,8.795805,-9.836746,3.410440,-0.466401,3.006256,-3.693851,-8.971468,-0.066405,4.980754,8.951056,9.061811,6.123472,6.549307,6.078736],[9.868424,-3.500983,-5.355465,1.082848,7.658817,-1.992954,2.707379,0.774246,-2.509235,-2.007522,-9.258897,5.440467,6.485351,-0.289389,-5.149059,4.026155,1.381516,-8.921178,-6.377424,7.458427],[7.407585,-0.660527,-6.681713,3.941874,-7.791275,-3.738451,3.330248,-6.516838,-6.289261,-2.389272,-6.984289,-3.854813,4.178384,7.930753,-9.589378,0.516438,-4.754236,-9.621927,-0.277242,9.003577],[5.149176,6.883008,3.643187,5.348723,-4.252866,8.717915,-0.009840,-8.916724,-4.778615,2.470680,-0.475295,5.582856,1.189543,6.212320,8.323461,-7.683136,-4.424197,0.379095,4.775330,0.043315],[-7.087141,6.290426,-4.997427,-4.934159,9.751643,-3.422418,5.478342,0.916070,6.886053,-0.091625,3.169985,-6.981102,-5.122379,-5.020584,-3.758939,5.941408,-2.410838,4.245180,5.126724,4.660645],[-9.599687,-4.218316,9.286247,-8.434358,2.270484,5.690480,5.977787,-5.811267,-4.041453,1.979491,8.137788,0.813635,8.623004,-9.982577,6.689799,-7.665943,2.930833,5.935674,-7.680793,-2.346845],[-2.007757,-5.015369,4.720356,1.876398,0.219339,-6.116935,7.054653,-1.903848,8.590675,9.863094,2.964910,-1.313197,9.807910,3.431143,9.701444,7.114078,-0.977139,3.646334,-2.109321,3.331474],[3.455293,-0.816572,2.337892,-2.859062,-3.168798,4.418319,2.582389,-4.144783,7.997738,-2.984676,8.964053,-0.348935,8.832656,7.884541,-3.242484,-7.827085,1.276580,4.642243,6.325583,0.402364],[9.396920,2.876922,-7.044090,0.646874,-8.375112,-0.856865,6.973297,1.201890,-3.333805,0.035597,6.467843,-7.398243,-7.192866,5.739284,7.443558,7.699944,-7.799331,9.730580,1.405870,-5.101665],[-6.360716,2.234035,-0.008343,6.513669,-3.298886,4.096844,-0.392098,-1.629610,8.517687,-1.417185,-7.712073,-6.009427,4.647449,0.812332,-9.096154,-3.116764,-2.040333,7.642662,-8.936202,8.744277],[3.793686,-2.201840,-1.389767,-0.134693,-7.853705,7.396047,9.229021,8.440169,0.593981,6.061430,9.634241,8.325652,6.257418,-5.189585,4.784543,-3.996303,-9.600356,-3.183367,0.697575,2.584081],[4.637171,-6.244593,-1.495805,6.534298,-7.785243,3.825444,-2.955876,5.512505,9.500645,6.271723,1.856075,9.774635,-2.988931,9.997182,4.607305,-1.811160,6.576930,4.531989,-5.491405,5.185253],[8.978385,-4.481609,7.989006,8.449792,9.809885,5.004474,8.248438,6.311926,-9.229508,4.412271,2.267909,5.877633,0.107667,-0.730963,2.165995,-5.464986,-9.145318,0.636079,8.916216,3.841246],[3.122678,6.092782,8.417697,6.716691,4.667426,8.411069,-0.284840,3.663012,3.173968,5.826618,-1.021314,9.737929,1.664442,-2.246298,-9.765401,4.622849,5.379491,-4.802653,8.580235,-0.695179],[-1.363965,6.129265,-4.424031,-7.511340,-7.563879,5.919748,-4.355093,-9.220074,8.855311,-8.011463,-6.353742,3.048907,-1.486657,-2.751183,2.069817,5.777413,8.515204,-9.216268,0.407593,9.679633],[4.977228,-7.126958,-8.699605,9.545929,-7.451222,9.735764,0.108214,-3.891072,-5.526567,-6.175803,2.496122,8.403843,-9.464019,9.928318,3.652074,-4.451225,3.578154,-0.865223,3.653576,5.676900],[7.336489,-5.438344,3.130231,-3.428591,8.087147,-3.594745,-7.945311,2.139163,6.129137,2.748949,-5.501053,9.492653,-2.280729,1.404077,1.822106,7.084994,3.210351,-0.825363,-9.506306,-4.289095],[6.877976,5.590210,-3.432003,-2.016257,4.874116,-9.886805,6.849230,1.966602,4.844936,9.185737,5.032501,6.102750,-5.363142,5.648941,3.030469,8.280251,-6.676472,-0.741366,7.823004,6.555383],[-3.959826,-4.031718,5.273223,-7.666280,-3.243214,-1.985848,-8.958906,-7.804190,4.252394,-2.384955,1.096234,3.636091,-6.476605,8.177824,-4.269294,-7.839853,-1.112158,4.064419,-7.227009,1.850864],[8.944655,-5.668795,2.481882,6.381578,-8.705506,3.836639,1.320808,-4.005585,4.948467,6.677527,-6.645260,-9.862003,9.000277,-2.939879,0.072448,-0.492589,2.942801,3.202170,-8.991025,4.256921],[-3.014208,-6.622133,7.750739,5.052257,-3.552841,2.327514,-0.170357,-9.304766,5.114631,3.439121,-5.628291,1.740270,-3.006213,-5.003894,3.554853,2.605480,8.121442,9.494581,-6.439003,0.057485],[-4.040578,8.766745,-3.851091,-1.047639,7.865953,1.480980,1.762671,7.491053,2.323652,-5.045383,-2.613136,-3.811872,-2.386921,-4.874081,-7.994045,4.197077,-0.571998,1.861173,-9.636381,-0.543558],[1.430902,1.181785,5.210258,-2.788529,0.625117,7.870710,-9.962593,6.428809,-3.625664,-3.061809,9.231311,8.952770,-7.396893,-7.566282,-6.892431,-8.115741,-4.812804,-4.160178,9.783964,-9.428567],[-8.080546,-2.228351,8.537074,6.110935,1.237352,-9.978487,9.056039,3.865742,-4.398330,6.144844,-6.611620,-3.543481,3.047155,-2.186770,3.313444,5.259453,5.656217,3.636868,8.705403,-3.886011],[-1.214911,8.608956,-0.332970,7.407969,2.640415,7.710403,8.397007,-3.932783,-1.510461,2.104226,-6.829177,2.429926,-2.583020,-3.944956,4.703732,-3.124244,-8.742270,-5.455909,-8.047600,2.942596],[-2.540031,-4.758438,3.098244,-7.689703,6.538018,0.358903,7.677900,9.505352,3.413175,6.824286,-9.980807,-4.339816,-8.792372,9.764643,6.947985,-4.533754,4.371474,2.400168,9.149010,2.176473],[0.917611,-8.058396,5.983750,-4.747228,-0.147346,-6.037132,7.776641,1.384068,4.004235,5.472300,0.031050,-3.234825,-9.430359,1.227904,6.794109,-5.656800,-9.870964,3.269584,4.989972,-7.713187],[-9.165813,-8.665738,-0.608954,6.238322,5.609680,-3.919990,-8.053818,7.972278,-4.350964,-8.808227,8.486024,-8.861911,-6.095438,-7.460669,5.405632,5.910690,5.258806,2.449229,1.346770,7.975662],[9.634839,9.603956,-1.687364,-6.923810,-3.199621,-9.173439,-8.820981,9.148741,8.140707,-1.375650,-4.364955,-8.365673,9.138958,7.142500,-3.610993,9.430499,-4.042024,9.448336,-5.146068,0.017324],[-1.563740,-4.961519,-7.613756,5.779536,5.152217,-8.496419,3.235593,3.918999,3.707677,9.547201,9.063783,0.816116,-6.474011,-2.949474,2.525520,7.973930,-3.524068,-3.419298,3.879610,-7.097882],[2.167549,-6.742075,0.903969,4.069609,6.792008,-3.667393,-2.633293,-9.887681,-1.312323,5.682688,1.241145,3.220473,-8.541353,-4.184433,-2.722488,5.572132,-7.647087,-7.657296,8.477822,-7.759094],[3.596644,-1.842070,-8.490547,-0.076687,7.300390,-0.548762,-0.580856,-6.668532,5.760736,-2.392592,0.595330,0.654432,7.898091,6.886530,-3.692507,5.893983,-7.455633,4.393744,2.255154,4.936863],[2.843247,0.740831,-0.593660,-8.524589,-2.107996,2.324126,-7.984336,6.852951,-7.334010,9.285170,-9.055388,-3.418429,-3.676685,-5.869294,7.253600,-8.573101,8.594214,-7.349205,-5.342950,-3.878975],[7.182449,-9.462259,-1.497345,-3.718229,9.305076,8.404480,-0.328344,-3.557106,5.783977,-2.455568,5.460520,1.737037,-9.380777,-0.012821,2.243525,-6.780874,-0.185135,-6.107653,-1.022508,8.877403],[-0.579404,-4.504102,6.143781,9.534639,2.629251,6.841021,7.889798,8.053508,0.689684,-2.380040,-4.056669,4.004337,7.464042,-4.936904,-7.364360,6.735098,-2.602969,-3.387964,1.666983,5.906532],[1.236211,0.065719,0.014661,5.986961,-5.407236,2.603538,-3.671983,2.537727,5.585081,2.082315,0.344862,-3.481447,-8.893728,0.812730,5.017294,-8.671646,-5.999406,3.379124,4.396531,-9.088942],[-7.297638,-7.875564,-7.908133,-3.430129,8.663923,-5.797202,1.056417,7.869161,1.782552,3.482361,9.026967,5.096965,0.484411,8.324059,2.179082,-6.935712,-6.960351,-4.293286,-3.437198,-9.913386]], dtype = "float64")#candidate|13869|(40, 20)|const|float64
const_13870 = relay.const([[-1.719051,1.506490,1.332806,-3.762779,-7.064481,6.051933,-2.563902,2.959261,-6.439486,4.169537,-0.559173,-6.898290,-1.430947,0.329083,-5.774658,-9.379500,8.472354,-6.079308,-8.013309,-5.278604,-5.225563,-9.424357,-1.819779,8.305649,9.415977,-7.929465,-7.229169,-3.931916,-3.043909,0.001664,2.670924,1.255375,7.746625,6.321772,-2.439537,-5.015613,-5.274302,7.701863,-4.388707,7.464328,-8.148772,-0.141498,-5.843732,5.449556,-8.297471,3.310360,-1.420542,3.153201,-0.523336,7.032198,-3.954496,2.767655,-0.166936,7.043046,9.212868,0.890884,-4.029607,-1.400294,-6.775052,5.794180,5.415377,-1.532164,-5.022704,0.611666,1.928930,4.969891,0.946093,-7.944732,-2.236088,-2.713658,-9.754084,0.609713,6.162238,-3.935976,4.973189,7.131707,-3.001666,-7.100297,1.152483,-8.633778],[-8.304616,-7.642393,-1.220447,7.572648,-6.206102,5.397917,7.954168,-5.438670,-8.772855,7.658108,-4.057211,-1.557383,-5.670356,5.932611,7.750220,-2.579178,-3.428547,5.854172,6.034360,7.354292,-1.124201,7.505145,0.347919,0.908377,-6.016924,0.228029,8.592475,6.602984,-3.851122,2.842292,-7.173064,3.638203,-7.544082,-8.071753,9.892313,3.725687,-3.666878,-8.433757,-6.969667,3.800884,-2.245920,-6.826329,2.616516,3.988624,-5.394552,8.460791,2.998934,4.577129,2.197327,4.233535,8.741569,-1.988206,8.136813,5.482173,-7.960180,-8.766147,4.405559,-4.248422,4.986156,-1.401354,-0.226626,-4.096536,-3.954190,4.721765,5.494652,7.796501,-4.274071,-3.645190,-4.802061,5.749514,2.928119,2.135505,-9.881534,9.012314,8.627364,-7.405269,6.615701,8.620927,-1.698685,5.506999],[-7.027772,7.655857,-8.405695,-0.023444,8.624970,-9.133174,-4.903556,-1.853011,0.387899,-3.303044,0.993681,8.743454,9.628038,5.809541,2.269388,-9.369773,2.556604,-1.225588,7.845330,-6.302127,8.569283,0.628595,-4.737510,-6.142532,5.017325,-2.442149,0.285136,3.435751,2.654457,1.994474,8.512350,-7.556938,0.090363,0.652563,9.574731,9.314320,-2.520792,-9.737885,-6.033128,-1.319662,2.308398,2.832415,-4.153078,-0.719406,1.405782,7.394956,1.484777,4.045995,-8.100374,6.892230,-2.387016,-4.823352,-7.188820,0.128182,-7.908602,-6.992811,-8.349146,-5.363843,1.963050,-0.777272,-8.980095,0.412689,1.130014,-2.516699,3.747989,-3.055794,0.990344,-6.443791,1.142372,-5.966650,-9.672352,-5.926318,-5.731319,1.795850,7.274891,-9.987785,2.183875,2.216164,-3.845315,8.233879],[6.694783,9.583920,-8.003435,-7.209046,0.459885,4.842125,-2.700609,4.210113,0.831617,-5.617186,-8.631324,-1.017669,-8.241335,6.937597,-2.530580,8.793961,-5.614798,-8.394529,-5.750679,-5.633426,6.652970,2.302512,8.761820,4.101396,-8.788513,6.968315,-2.655252,-5.063803,0.338363,-7.991925,-1.313319,-2.699398,-5.164982,-0.296876,5.212261,1.153359,-5.387085,-1.913615,2.304615,-9.984975,4.440168,-4.249247,-5.864049,2.572226,-9.566554,7.504380,5.810567,2.892085,-3.358825,-2.887508,3.359053,-2.263541,7.341046,3.230942,-1.872021,-6.551563,-2.630855,-2.143973,2.611809,-7.507441,0.413110,7.993547,6.773048,-3.356642,-6.414113,-4.146514,-5.381695,0.897874,8.625046,-9.410050,0.260855,-9.740220,-9.938864,-4.425522,-2.829204,9.983501,-5.333481,-0.424966,-2.685010,9.571435],[1.285963,-2.669606,-1.151022,0.484850,-5.333320,-9.046512,-5.349782,3.241992,3.881419,0.471793,8.584594,8.968320,1.338250,8.487484,-1.591544,-0.769695,-1.689124,-6.534691,-1.804985,3.209688,0.172814,-5.711494,-1.795138,-4.019308,8.163173,4.190282,9.467464,-1.377767,-7.305908,-1.510871,-2.898594,-4.300191,7.498834,-9.328748,2.760922,-4.017306,9.690494,-8.995118,4.766967,0.399145,-1.435894,0.287104,9.138075,-8.484214,8.283644,-6.152037,1.381731,6.410032,0.706013,0.808653,9.574212,-9.941977,-5.982620,-7.642620,3.982807,5.031252,-4.526040,3.868801,-9.760114,9.661997,-8.494877,-6.963222,-2.047694,-2.232554,7.782671,-8.106306,-6.709378,7.175713,-2.317621,-5.326445,8.163257,4.584864,-6.159038,2.338804,7.957929,-3.319867,-0.965155,6.727680,-7.378983,6.491924],[4.824767,-0.973152,-1.719120,1.504103,5.904955,-9.452101,7.489357,-4.302891,9.011848,-0.475960,-5.674224,-8.037278,0.769540,-5.994073,-5.419002,7.341634,0.330969,2.332569,0.214405,-6.885309,-3.041565,8.238310,1.559547,6.595665,1.218247,3.274467,-4.889767,9.596583,7.304483,-2.558787,0.609092,-2.164082,8.261942,-1.747197,-9.993369,-0.447370,7.334947,-0.914542,6.745719,2.737091,7.539654,9.198319,1.647992,-9.111818,-2.246385,-3.254924,-5.993363,-6.498062,-5.576482,5.721774,-0.938479,2.023900,2.722139,-0.278632,6.237751,-3.317523,-5.732381,-4.475692,-1.918841,-6.905588,2.491956,-6.878592,1.886700,-9.536317,6.092182,-7.335075,8.578637,9.473305,7.688917,1.409426,-1.213158,-1.384805,0.882783,-1.369214,4.149077,-7.754878,5.441172,-8.960924,-4.561899,-4.643850],[-9.941602,7.281965,-2.661081,2.944382,-8.629441,-4.457168,-3.248812,1.271571,0.788634,6.325720,-4.302311,-6.705459,-5.264165,4.307328,6.333604,-5.701172,-9.418988,5.533998,-7.542273,9.577813,8.476087,3.155904,-6.573356,-7.729225,-8.666765,-7.280649,8.899320,-8.566823,0.891128,-9.117271,0.076727,8.789751,-0.399531,-6.947363,7.260793,0.931314,8.242569,-4.339043,3.262100,-5.093470,-3.615030,7.352573,3.455572,7.714897,4.286436,9.659561,-8.278952,-1.537855,4.475089,0.783722,-7.094815,1.910524,-0.360281,4.224816,-3.176481,2.732059,-4.398724,3.851978,2.812972,0.936184,-7.946249,7.664155,4.127275,-7.668369,1.695301,4.064437,-9.904055,5.147699,-4.102043,6.842415,-6.964114,7.864886,9.861929,-3.048779,6.481821,8.316762,-8.987415,-8.416018,-6.428762,-5.569971],[-6.452689,-5.243627,5.499382,1.926436,-6.258389,-8.482984,-6.802006,-5.719392,-0.762860,-8.572616,-9.066534,-2.875929,-3.032588,-8.745547,8.631437,-6.454025,-2.518878,-3.386897,9.074134,7.193186,-3.487036,-4.166334,0.966897,-3.684364,-2.420976,9.515160,-5.708242,8.922844,-1.648814,-5.823171,4.186231,3.978755,5.022562,8.486450,-2.616553,-6.847671,-4.859535,3.880253,0.711850,-6.955255,-5.458715,-7.068259,7.731874,5.070079,1.793606,8.822355,5.169932,-5.824352,-3.410614,4.249125,-2.649533,-6.769613,-9.466300,-0.276239,7.613182,7.314904,-3.157221,9.038587,-7.989369,5.890237,-8.753419,-8.990640,-5.543838,-6.518961,-9.477131,1.162372,8.223718,6.231482,3.149668,-1.862542,-6.489234,-0.246085,7.980717,-5.968667,-9.467722,-9.685568,-7.645678,-6.963930,8.279748,-1.487901],[-4.915985,4.211770,8.893306,-8.683959,-0.638812,0.691348,-1.224607,-9.308644,3.006399,7.996601,-8.144453,-6.473384,-8.518974,7.695080,3.394606,2.941833,4.581594,-6.841956,-2.643293,0.773084,4.962111,6.770390,-8.585783,2.482880,2.062277,-5.518162,-9.916870,-3.775416,4.965541,4.239607,5.479359,9.316079,3.562408,9.485162,-0.030160,-5.953086,-5.410447,8.421931,7.956091,-4.238265,-4.240851,3.216882,-6.441993,1.697332,9.178165,-7.783841,-9.817311,-1.827984,7.576106,3.790018,-3.552944,9.754378,3.519741,-7.927442,-2.933147,2.876728,7.992544,2.308286,8.257116,0.243142,1.520969,1.062018,0.842573,2.583981,-2.252930,-4.273735,4.966075,3.559992,2.205682,0.190003,-6.400498,-0.907782,8.919251,3.924435,-7.564166,-8.743082,6.992888,2.330664,7.939583,7.590181],[8.468640,-0.360750,-2.989628,-2.143557,0.150505,7.372528,-4.341017,2.320009,3.289511,-1.581724,-4.055218,-1.468652,3.115148,-2.674811,-5.502565,-8.259140,-1.946733,-0.895553,-4.982153,-4.299173,1.258738,4.947015,3.554893,5.626210,-7.969961,-2.776206,-8.370319,-7.855803,7.555416,-5.805570,-5.376822,4.315301,-1.424480,4.959446,-6.371065,-6.054476,6.997748,-7.680327,3.540985,-2.020775,7.180708,-2.425297,8.179745,6.732953,8.505229,-2.361896,-7.950734,-7.863566,-1.867216,8.470967,9.011483,-9.379061,-9.843817,7.369078,-9.751399,0.195859,9.291739,-6.989127,-2.655388,8.536748,7.908098,9.690244,4.581068,-6.499283,-9.659242,3.925013,-7.165824,-2.195223,-5.532902,-9.327182,6.172136,-8.200592,7.182950,2.990646,7.663050,3.158112,6.012305,-1.931536,8.022324,-3.167036],[8.079234,9.619143,7.370462,-1.916949,-0.764383,-1.288103,-6.873090,-0.225395,0.847420,6.588300,-6.312435,-1.412116,7.423873,-8.298293,3.831150,-4.237483,-2.635313,-0.156414,-2.717970,4.137266,7.683303,-4.374989,1.115194,8.434021,4.493686,5.500697,-3.961956,3.256159,-2.727487,-7.192283,-5.656721,-9.569614,-0.841677,-8.542411,4.818828,7.396822,1.938368,-9.039932,-0.242488,-8.626114,-5.402592,4.144335,9.997956,3.385779,7.008909,3.157160,-2.898662,-9.450539,7.561615,2.678756,8.957485,7.090701,2.986478,9.317492,-2.558105,8.023710,8.174004,2.990451,2.374877,-2.073419,-2.248396,-4.116014,-4.828688,0.323874,8.074698,-5.902327,-9.139398,9.677912,-4.432893,8.206327,-2.288245,2.440281,-3.177513,-9.872832,0.384795,-7.707933,2.730477,7.525893,7.554260,3.010240],[9.825793,8.442287,1.868005,6.755508,7.792698,-8.874694,7.733930,0.860533,-7.270526,6.164236,1.673009,6.564203,-4.716147,-7.950949,-8.704934,-1.504420,7.854063,4.334279,8.622582,-1.731199,0.728035,-1.675121,5.435189,-6.261484,-4.572153,8.597044,8.212177,-2.932784,9.060841,-2.257229,-9.268100,-4.693283,-1.098637,-9.379571,-2.655438,2.214126,-6.056835,8.802476,4.169956,2.637750,3.057247,6.637845,-3.480339,4.824466,-0.874128,2.895608,-2.212677,7.479658,4.067242,-4.859980,-0.523812,7.044976,-9.302368,-7.655872,9.270126,0.648644,4.757266,2.657526,-8.872814,6.125620,-2.929847,9.462421,-2.411936,-4.208329,-2.669822,-2.064026,-4.511965,3.373402,-2.840015,-2.845684,-1.715601,-0.520131,0.888988,1.508999,-0.417101,-8.265159,0.811658,-2.050840,-6.273711,8.826945],[9.755964,-4.000080,2.631483,-9.594275,4.978153,0.737500,-6.408803,4.687889,-1.613203,3.872791,-2.532677,6.585043,4.927661,0.121082,-9.618747,3.051884,-9.744866,6.755415,2.214914,1.143015,3.162953,-0.547892,2.261776,8.650885,-4.227033,-1.369807,-7.849473,-4.021082,8.366093,-2.609194,-6.199379,-4.745662,7.505940,9.360541,1.369538,0.207756,9.653645,1.745597,-7.917092,-6.067675,9.485299,0.240470,7.019969,-6.341268,3.117703,-1.379989,-2.006167,6.086528,3.263735,-8.226047,7.014427,6.554486,-8.774023,1.149826,9.037998,6.663220,9.427000,-9.513325,2.709809,1.129873,9.778554,-9.857568,-3.632291,3.809498,-0.518121,0.757166,-9.685508,6.109902,2.544664,2.157364,-0.987268,8.153242,4.423674,-9.362031,-2.467681,5.614184,-4.481549,5.530460,1.689350,-0.569572],[8.241701,-6.446398,-8.591510,-7.424151,-1.063260,-1.430531,-6.531861,-7.140597,4.644123,-2.933782,3.853113,-9.798545,-1.009391,-5.219823,-4.112743,3.930786,-6.324039,8.766885,7.167433,-3.348704,1.664249,2.793156,3.034502,8.238319,-9.424363,-3.301172,-4.961705,1.898761,8.898251,-3.555452,-5.589118,3.361293,0.824264,6.908185,-6.289705,3.419714,-3.706858,3.255373,-0.337032,4.761425,7.080055,-6.963866,-9.543763,-9.894125,-8.423655,0.910827,-2.962401,8.653962,-2.537077,2.109998,0.013419,-8.315044,2.143353,5.462873,1.040466,-5.926187,-4.617731,-8.541256,6.682442,-4.998933,9.677208,-5.236033,-8.732644,-8.707658,0.899659,7.305907,-8.145019,-0.676529,-1.460935,0.601779,-1.973983,-2.456582,5.517229,3.944340,3.460055,-4.508123,-3.698375,-2.398462,-3.152341,8.211424],[-6.015810,-5.675412,-9.867975,-4.918070,-1.324113,-9.508772,-0.014642,-2.267212,8.099018,-8.712053,9.144430,-4.839695,7.226511,3.169884,5.688785,7.366648,8.865657,-3.266346,3.462915,-3.073734,-0.128595,-4.930061,6.799487,-3.043571,7.595608,7.138443,7.425197,-7.649441,8.651586,2.186557,-7.468504,-4.711022,-1.480258,0.374460,-2.275278,-5.426192,9.035556,6.170966,1.572242,0.518630,-3.828783,6.483995,-9.935379,-7.689519,5.220418,-6.178035,0.405175,-9.289313,6.415391,2.831570,5.266238,9.909247,-7.554504,-2.912994,-5.800462,-2.347537,-6.243371,7.635240,6.951665,-1.448648,7.366940,-3.724990,-3.768155,-7.418800,4.625310,4.705041,0.044243,0.683687,3.391507,5.771790,0.461123,-1.866063,-3.071730,7.601208,0.506214,-7.716914,-5.001710,7.298937,4.599431,6.072795],[7.939629,-4.694742,5.954973,7.894367,9.839052,-0.318596,-1.054746,-9.456276,-4.847660,1.391764,-4.390850,-3.789061,-0.379921,6.747798,-1.851978,-3.082649,9.138456,-1.735978,-3.350316,1.465673,4.616436,9.791370,-6.455571,-8.434199,2.140602,-9.866588,2.978037,-8.403001,2.067292,-6.362435,-6.648674,6.530701,4.350687,-7.293591,4.051536,0.192101,-2.266502,5.680498,-5.987854,1.544206,7.262360,2.904747,8.334056,-5.643597,8.407371,-1.147680,-2.787010,0.767389,0.450243,4.863833,7.902734,1.203979,8.381879,-4.514874,-6.064592,2.724717,-5.362404,4.195075,4.712594,-0.218666,-9.476572,-0.951717,-8.604073,-2.194799,-9.828063,6.136517,-3.616565,7.216501,4.695781,7.321692,7.193491,7.163851,-0.846292,2.051654,-5.380719,-0.647577,-7.249649,6.049793,9.118408,9.091618],[-3.954219,0.343525,2.818246,-0.066650,3.320926,8.949970,4.674673,-3.118147,1.144720,0.228288,4.174145,-1.752051,-7.209934,-1.814083,8.540241,2.185655,-1.491424,-8.112496,4.529507,-2.293717,-1.159025,-7.685478,-6.377543,8.706349,-2.254622,-4.000283,1.571413,-0.917375,-6.072685,1.741282,-4.518163,4.803000,9.744329,-8.920987,8.925906,8.771439,-3.088385,7.580627,-7.833926,-7.114973,5.078937,-4.076819,0.243173,-7.207840,-2.604388,5.934835,1.037654,3.598719,-9.040397,8.800475,8.883679,-1.839812,-9.678157,-5.051946,-0.138180,-8.508250,8.133097,-4.011073,8.040472,5.809494,-6.310601,-8.851897,8.510641,7.038401,4.656830,3.037192,1.997803,4.391723,2.477553,4.465554,-3.663164,0.179777,-2.569380,9.968088,1.970217,6.148265,3.199456,1.919861,-6.518252,9.395991],[2.578847,-0.884930,-9.737850,8.186772,2.233939,3.005845,-5.752911,-8.238339,3.769398,-2.502338,-0.644222,-2.221372,9.124968,-1.044669,-5.578691,9.247709,6.700305,1.139719,9.812672,0.725268,9.915917,6.287897,-3.438911,-6.811906,6.043115,-0.091321,4.893551,6.624585,-2.059404,-3.426774,7.165453,-0.435436,1.720743,-4.516219,-4.484711,1.662178,7.685711,7.612079,-6.597238,5.186553,-3.067825,6.955956,-2.230457,-6.894458,1.651264,-3.950060,4.475633,0.099024,-6.632301,7.779675,1.627514,-2.119621,2.678846,-7.335678,3.612429,2.635652,1.291375,9.427554,-2.567686,-2.253952,-0.103818,-9.667321,-6.659625,-2.768161,-9.088469,3.480978,1.267296,-1.048953,-0.845193,-0.352302,-1.037547,4.104734,2.632321,5.384625,8.796906,4.374818,-5.183542,0.150368,3.936078,7.788905],[1.966283,8.638955,-1.049627,-1.937068,4.736305,7.644653,-4.822855,8.681801,5.615745,3.410594,0.033946,9.075436,8.729051,-9.958668,-0.617275,-9.919775,-6.011638,-4.383362,9.465860,2.558657,-8.355225,-1.638522,-4.661084,-2.044391,-1.508545,-4.735072,-6.131348,-6.242167,-2.237034,-4.106218,-8.116309,-8.281903,-3.771911,-2.279447,6.626382,-4.248510,-4.599142,7.102544,0.020471,-8.874248,8.304398,7.196417,-8.840062,3.406633,-6.642544,-6.228990,-2.604166,2.269358,7.142153,-2.753895,-9.889755,-4.393770,0.614491,3.606282,6.849384,1.708998,-5.014129,-4.240306,-5.890805,5.537906,5.925302,7.511062,-5.233369,9.652342,-7.188320,5.776792,-3.909915,1.628642,0.553520,-4.927708,0.350791,2.647621,-1.270244,-9.624542,-0.241082,2.203723,8.954091,6.012886,-2.445466,-2.776032],[4.165300,0.460106,2.303355,2.955673,0.411698,-5.881467,6.159943,-2.115794,8.650900,-9.585783,-1.652510,-8.161579,1.348169,0.485067,-0.237102,-7.317813,6.308813,0.056562,7.147065,1.659187,9.479826,5.297084,-5.558612,-0.790576,-5.466792,6.677662,7.058263,4.076378,1.328984,-3.281577,-8.715350,7.735967,-4.211106,-9.528182,-0.947422,-7.163441,4.840556,-4.447376,6.072081,-5.047295,-4.534195,-5.502415,1.137996,-6.795107,-3.256704,-6.283143,7.569244,6.357817,-7.892336,4.268654,1.545405,-2.883394,6.206497,-7.977464,-4.735002,6.008843,-2.466394,-0.678759,6.076333,8.360277,9.771464,-1.813323,9.157380,-4.655780,4.811602,-2.058431,2.902869,-5.269728,-8.273938,9.467013,3.707851,0.182917,-5.531761,7.364642,-4.407043,6.712604,-6.460389,-8.632814,7.170147,3.625830],[4.922841,-7.275545,8.620035,2.427705,1.035317,-7.792116,6.670896,2.405393,5.311964,6.113687,3.264426,8.969329,-8.225750,3.085513,-1.028691,6.924855,5.040238,-9.576634,-7.151803,-0.639923,-6.557173,-5.549661,-7.653117,7.379897,-9.235897,6.358596,4.408182,3.542773,-2.822852,-9.188126,4.830172,-7.434042,7.280932,6.565467,3.214192,5.468567,-7.592158,3.400888,7.943625,-3.469563,-7.620447,6.040494,-8.861479,6.064909,-2.389260,2.104645,4.689794,-6.900900,-8.184579,-8.478268,2.021880,6.017268,5.453968,-0.728783,2.198485,-6.174450,-8.079738,-2.428810,-5.658353,1.798046,3.446253,8.697659,5.898695,1.381786,7.524779,4.073486,2.720305,4.247094,9.669496,-7.048719,-5.483516,-0.019663,-7.646898,-9.522842,3.960875,1.127060,-4.489878,3.778254,-0.178539,-8.639885],[4.550996,-8.947617,-7.083210,5.180420,2.909290,8.884449,7.629582,-5.667314,-6.475234,-3.304922,4.474872,-9.964300,-3.918417,6.507651,-6.149593,0.475623,1.388532,-1.958413,2.711360,3.970671,3.926315,-8.753530,9.704350,2.465929,4.151600,2.512767,1.008931,3.287709,9.905982,7.762483,-5.748580,6.528000,-9.643541,8.377687,-9.460382,3.635120,7.981469,-7.126030,-3.047687,-1.351891,1.910022,-9.684415,4.385297,7.319789,-0.203950,-2.610402,7.517979,-7.133304,-5.306291,8.174626,9.621591,-6.143756,-2.399704,0.243046,-5.936884,1.299363,1.544556,3.278968,1.464206,0.252194,8.860536,-0.977402,-9.449089,-2.086941,-3.082345,8.715343,-3.763607,8.601288,-8.046359,-0.749272,-2.942197,-9.458643,2.919582,4.871979,-6.530188,0.897178,-0.929674,-4.994273,-4.896438,9.791505],[-0.596973,-2.638647,4.335764,-1.531461,-1.377293,-4.440031,-0.340894,-9.922362,-7.343725,-5.108651,3.402020,-2.245484,0.964049,-3.256846,-0.980096,-8.171465,-9.574555,7.582614,-1.243492,5.283296,-0.652034,-5.154618,-3.587058,6.126313,-9.501683,-1.249554,0.433654,7.807150,7.709187,-8.003578,-0.520891,7.050215,-3.456616,-8.216899,-9.889936,8.283795,5.780156,7.833492,7.564784,2.060734,-6.066936,5.157138,-6.430057,-1.803008,-6.526493,7.465027,4.974122,0.641592,-2.040438,6.170705,9.103866,3.511698,-3.847883,-5.795803,8.133351,0.919217,9.794336,0.214263,1.545586,-3.658271,3.087836,-1.801709,-1.580372,-1.242124,3.063869,4.344869,-2.451066,-1.020406,8.292118,-3.125727,-9.546835,-3.676233,-0.633337,1.728710,6.834072,0.230622,-5.827221,9.029913,8.136094,7.151844],[2.244258,3.296581,4.006164,-2.676253,2.969143,-7.534442,-9.016834,7.246841,-7.313594,9.727215,-7.116818,-2.023690,-6.755906,2.724671,3.469793,4.715759,7.823103,4.933942,-4.144924,1.337084,-6.617617,0.815677,-3.081994,-2.400243,9.256668,-6.362980,-9.848730,-9.193515,2.356530,7.462637,-8.361375,4.148826,9.868695,0.941292,5.863938,1.163000,-1.566417,-1.612788,-0.654363,3.918389,-6.095531,9.741940,6.118347,-3.249258,-7.640250,5.767083,-3.297036,-7.621891,7.888978,5.489591,8.808287,5.991969,6.054523,-8.379796,-2.100807,4.128951,-9.700136,0.010567,7.486690,-7.447454,7.807985,-6.510615,-2.190738,-6.196779,-3.704307,-5.699509,-9.111312,2.442208,-1.206698,0.940121,-9.081120,9.820751,-1.434908,-0.540236,-9.313552,1.612310,-8.164362,6.409051,-8.064875,2.071233]], dtype = "float32")#candidate|13870|(24, 80)|const|float32
call_13868 = relay.TupleGetItem(func_11960_call(relay.reshape(const_13869.astype('float64'), [10, 10, 8]), relay.reshape(const_13870.astype('float32'), [1920,]), ), 2)
call_13871 = relay.TupleGetItem(func_11964_call(relay.reshape(const_13869.astype('float64'), [10, 10, 8]), relay.reshape(const_13870.astype('float32'), [1920,]), ), 2)
bop_13872 = relay.logical_and(call_13860.astype('bool'), call_13853.astype('bool')) # shape=(2, 11, 6)
bop_13875 = relay.logical_and(call_13863.astype('bool'), call_13855.astype('bool')) # shape=(2, 11, 6)
func_7809_call = mod.get_global_var('func_7809')
func_7811_call = mutated_mod.get_global_var('func_7811')
call_13877 = relay.TupleGetItem(func_7809_call(relay.reshape(var_13865.astype('float64'), [7, 13, 3])), 0)
call_13878 = relay.TupleGetItem(func_7811_call(relay.reshape(var_13865.astype('float64'), [7, 13, 3])), 0)
bop_13888 = relay.multiply(const_13854.astype('uint8'), call_13860.astype('uint8')) # shape=(2, 11, 66)
bop_13891 = relay.multiply(const_13854.astype('uint8'), call_13863.astype('uint8')) # shape=(2, 11, 66)
func_13470_call = mod.get_global_var('func_13470')
func_13472_call = mutated_mod.get_global_var('func_13472')
var_13911 = relay.var("var_13911", dtype = "float64", shape = (280,))#candidate|13911|(280,)|var|float64
call_13910 = relay.TupleGetItem(func_13470_call(relay.reshape(var_13911.astype('float64'), [280,])), 3)
call_13912 = relay.TupleGetItem(func_13472_call(relay.reshape(var_13911.astype('float64'), [280,])), 3)
output = relay.Tuple([call_13846,call_13849,var_13861,var_13862,call_13864,var_13865,call_13868,const_13869,const_13870,bop_13872,call_13877,bop_13888,call_13910,var_13911,])
output2 = relay.Tuple([call_13847,call_13850,var_13861,var_13862,call_13866,var_13865,call_13871,const_13869,const_13870,bop_13875,call_13878,bop_13891,call_13912,var_13911,])
func_13915 = relay.Function([var_13861,var_13862,var_13865,var_13911,], output)
mod['func_13915'] = func_13915
mod = relay.transform.InferType()(mod)
mutated_mod['func_13915'] = func_13915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13915_call = mutated_mod.get_global_var('func_13915')
var_13917 = relay.var("var_13917", dtype = "bool", shape = ())#candidate|13917|()|var|bool
var_13918 = relay.var("var_13918", dtype = "bool", shape = (22,))#candidate|13918|(22,)|var|bool
var_13919 = relay.var("var_13919", dtype = "float64", shape = (273,))#candidate|13919|(273,)|var|float64
var_13920 = relay.var("var_13920", dtype = "float64", shape = (280,))#candidate|13920|(280,)|var|float64
call_13916 = func_13915_call(var_13917,var_13918,var_13919,var_13920,)
output = call_13916
func_13921 = relay.Function([var_13917,var_13918,var_13919,var_13920,], output)
mutated_mod['func_13921'] = func_13921
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13925 = relay.var("var_13925", dtype = "float32", shape = (16, 16, 15))#candidate|13925|(16, 16, 15)|var|float32
uop_13926 = relay.atanh(var_13925.astype('float32')) # shape=(16, 16, 15)
output = uop_13926
output2 = uop_13926
func_13940 = relay.Function([var_13925,], output)
mod['func_13940'] = func_13940
mod = relay.transform.InferType()(mod)
mutated_mod['func_13940'] = func_13940
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13941 = relay.var("var_13941", dtype = "float32", shape = (16, 16, 15))#candidate|13941|(16, 16, 15)|var|float32
func_13940_call = mutated_mod.get_global_var('func_13940')
call_13942 = func_13940_call(var_13941)
output = call_13942
func_13943 = relay.Function([var_13941], output)
mutated_mod['func_13943'] = func_13943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13749_call = mod.get_global_var('func_13749')
func_13751_call = mutated_mod.get_global_var('func_13751')
call_13957 = func_13749_call()
call_13958 = func_13749_call()
func_9294_call = mod.get_global_var('func_9294')
func_9297_call = mutated_mod.get_global_var('func_9297')
const_14015 = relay.const([0.720698,-1.894947,-8.874798,0.313623,5.213547,-8.417864,0.750545,-5.523312,0.560568,-8.734279,-8.744963,8.526182,7.367087,-9.148909,7.794056,2.897077,-6.529499,8.759583,5.899872,7.484728,-2.540726,-3.417858,-6.413585,2.487038,4.938814,4.193080,-4.138069,-8.650754,-2.021601,-6.935384,-3.202908,5.285845,0.512456,4.873430,3.901540,5.211626,-9.864445,0.877524,2.969590,-6.724180,4.142249,-7.195077,-9.208141,8.730432,4.011922,-6.676180,1.396439,-4.015347,5.089065,7.813183,-8.205387,-6.617191,9.122557,9.031490,-5.695375,3.851199,1.231178,6.153949,-9.579534,2.361218,-0.291167,7.925623,6.713389,-2.013925,-8.516800,6.479338,4.304621,5.985173,-8.186270,3.478088,8.203377,-0.995590,-2.794114,-8.866124,-3.366699,7.703970,-8.730361,-8.123151,-9.921148,-4.116507,1.794294,-1.698997,7.750299,2.493315,-1.062176,-7.055148,4.430127,6.200536,-3.408658,1.374838,6.936124,8.150473,0.397761,0.868344,-2.763677,-6.079667,9.088505,-1.454724,7.240286,-1.449344,-8.679041,4.093597,2.592813,-2.925375,-3.280807,-3.513478,-9.023161,0.511086,-2.625480,4.564037,-3.652671,-8.818848,-0.681538,-5.543111,-8.001305,-6.739186,9.303980,-3.893034,-5.964143,-2.053065,-9.501347,-2.416389,-9.408734,6.214498,-8.097609,-5.417616,-8.181513,-7.950358,4.997365,-9.666137,-4.120811,0.176417,-4.696432,-1.914971,-1.473252,-0.124326,-4.076346,6.939008,-2.327748,5.017282,6.604955,-6.242982,-4.315823,7.194787,5.245625,9.903460,-3.098288,-7.048950,-5.598137,5.564303,5.250583,-1.451145,-2.513007,2.427498,-2.282386,3.309330,-5.236143,8.405908,-8.711867,-4.533836,2.828456,0.551979,-7.945738,-1.479600,2.657384,5.046300,6.066777,-9.288395,7.916432,4.798068,-1.529312,-3.729817,-7.380459,5.734201,-2.079133,-4.389397,1.893599,4.780813,0.972187,-3.830621,6.285217,-1.856521,9.795355,-5.389991,-5.253224,-1.475385,-2.540910,3.287738,1.052395,0.337836,-8.710865,8.132972,-7.174688,-9.359523,-5.774651,-6.797185,-9.814447,7.674684,5.709284,7.944440,8.754787,-2.027556,-0.458457,-3.487985,-8.382716,4.597017,4.285630,-9.171787,6.420416,-4.937188,8.721309,7.224636,3.517390,-9.130935,-7.829700,-3.810975,4.676195,0.563837,-1.338364,8.112540,4.145548,0.861903,7.004334,-4.905289,-8.536450,4.693956,1.291596,-4.646180,8.700710,4.424162,-2.915499,6.204157,-9.192954,0.737043,-4.889751,7.294245,6.498711,-8.674122,-4.827445,4.282427,9.799826,8.158323,5.398079,2.294736,-7.604618,-2.611758,-4.598348,-0.348557,-8.718035,1.154069,7.375965,-8.608573,-1.798473,6.279049,-0.378251,0.391033,4.344616,-8.609575,-8.907130,5.783506,0.127622,8.502617,6.293061,-6.573084,4.584771,-7.678000,9.112393,5.842204,-2.003654,-9.302018,5.145200,-9.027034,-0.680880,9.029034,0.961480,5.957618,-7.755635,-0.057033,6.993805,0.640642,1.613057,9.962683,3.986330,-4.428383,2.453740,-0.875286,-3.835014,-1.288423,2.569477,-4.727578,-2.940225,8.814924,-2.020943,0.683067,6.437886,8.730869,-9.736120,2.847707,4.302289,5.762327,-5.225905,-8.069781,5.167439,-4.971094,-3.447870,9.886093,-8.743735,-8.098690,-4.447920,-0.119039,-6.216210,-5.329488,-5.210015,-2.534019,6.686274,3.072354,3.199882,7.362136,-0.717718,-0.339352,-6.361122,6.061313,-3.744029,5.082960,0.074793,-7.998377,8.075050,4.748591,-9.578011,-8.951862,6.030252,-5.809414,1.788443,4.689051,6.920993,-3.544567,1.089553,-5.454110,5.553588,8.154075,-0.330328,0.303537,-0.954573,2.722857,-5.104212,9.163896,6.097876,1.967761,3.085694,-9.826915,-3.492851,-8.467652,5.072442,0.926002,-2.624058,8.491731,5.874535,6.195458,2.938359,-7.435513,-6.478222,-7.911896,5.133296,-5.372763,-8.481785,2.288635,4.761226,9.247618,5.306999,-7.487776,5.225304,-9.667299,-3.012538,-8.803658,-2.114187,3.899595,-4.266757,2.395332,8.086749,-6.832415,-5.487318,-4.570863,7.712517,-2.027577,6.333786,0.684882,9.788710,4.012880,4.408298,1.369560,-3.518527,-8.714657,-6.980723,8.607854,3.360640,-7.567365,7.558472,6.299707,-9.846689,4.734454,-8.388522,-4.948122,-0.303281,9.410534,6.817414,-3.517042,-7.275146,9.113294,-0.027614,-3.131187,-3.552917,3.427042,-6.957871,8.770510,6.376429,-7.364307,1.977960,3.938636,-4.267960,8.553550,9.687560,0.577238,-5.972411,2.494714,8.126351,-1.094172,-6.582474,-9.752265,-2.012255,9.590560,-1.382794,-5.882353,-1.462972,-2.874319,-9.786162,-4.296720,1.570776,7.721576,-7.410966,-1.117526,7.071398,-0.257814,-3.580341,-1.140922,-1.901969,-1.959967,3.628366,-6.451853,-9.402194,-1.218176,-0.852472,2.114795,-4.987414,8.773993,8.201879,0.756768,-1.054788,-4.375280,-1.651457,1.618874,-6.342757,4.653336,-6.445740,9.026935,-8.459097,-0.479645,-6.930668,-9.260154,-4.724641,-7.271756,2.743028,-9.727434,9.346012,0.739270,3.953537,-0.169196,-9.378178,5.691488,6.360662,-9.326162,-9.843002,-0.706592,-2.127460,-8.470947,-9.836813,-0.638463,-9.114366,9.450267,0.121211,6.453538,0.175607,-8.382798,0.526135,6.181727,-8.260675,6.318937,-1.202378,9.357286,-7.983048,5.387669,-1.554732,6.201982,2.345614,-4.690730,1.172552,8.538249,6.219225,-2.993429,-7.240388,7.575735,0.941474,0.978815,-3.167130,-5.006659,-6.845381,4.190488,3.636982,9.442011,2.373209,5.074922,7.736447,-4.819182,-5.161116,-9.579789,-8.082624,1.143274,-9.117668,3.985425,-2.651163,9.898946,4.642961,8.394039,7.927119,2.182562,1.152392,3.056848,-4.290009,4.246810,4.859727,5.756889,-0.650000,7.373417,2.933368,6.583880,2.679210,9.157674,-8.020341,4.385543,0.332858,-4.581861,-6.813592,-8.973183,4.972277,4.667201,6.506161,-7.885952,-3.942742,-6.026422,-5.713040,1.166228,-2.434586,5.505582,0.378342,5.543728,2.902889,1.512915,1.915876,-0.458381,-7.955542,4.767710,-2.344713,0.639454,-8.075064,1.416662,0.853999,-6.301673,0.400306,-2.282287,-7.635806,5.128336,-2.430076,4.836092,-2.595367,-8.450567,-6.675283,-7.742754,-6.901722,6.828250,0.364481,7.861035,3.907878,6.866559,5.350245,5.219534,6.261025,-9.156224,-6.574833,1.083446,5.302524,9.984937,-3.841980,9.387261,8.348765,0.923279,2.424285,8.694869,-6.604785,9.232449,0.736487,7.932689,7.861248,-3.458695,-9.382364,8.721137,8.729638,3.047871,-9.688451,-7.913937,1.141180,6.399809,0.318013,3.930484,2.518813,2.619022,5.416240,3.927204,-6.597672,-0.956253,2.587821,4.663670,-0.209931,-5.259290,5.500679,-5.278891,-3.936557,8.815893,8.946263,9.943171,3.773908,9.332113,-0.892032,6.369271,-3.240124,8.697389,6.479898,-7.559481,7.282008,8.752612,-8.706495,1.370735,9.629358,-4.463707,4.252149,0.631336,-1.977391,3.215464,7.520748,-6.894558,8.791350,1.317260,-6.704461,-0.224473,9.965803,-3.718122,-8.847423,-2.303672,-6.826923,-2.220412,5.892864,-5.533603,-0.756542,-6.989297,-8.482285,0.971899,-9.261320,1.705798,-3.985557,-2.980660,6.725706,0.356137,-8.266695,8.098372,-8.227939,-7.414378,8.947999,-7.357991,-0.213560,0.746514,3.977973,-4.656043,4.616980,-8.139817,-7.596253,0.253712,3.000236,0.293928,6.503851,-4.081708,-0.536651,2.304176,5.787777,3.308191,-6.035549,-7.076258,6.470148,8.096279,-1.723718,-1.874565,-6.766687,-9.131057,9.892354,5.791209,-8.618939,-6.808943,-1.000730,-7.486711,5.392379,2.766247,-1.660975,0.155449,8.260290,1.482239,-9.497357,-9.414144,5.433525,-7.841022,-0.987355,2.830355,2.075504,8.467347,7.584412,8.519518,0.287207,-1.784490,7.062614,5.838229,-6.390250,-0.585824,-9.867135,1.110011,-4.047119,-6.273747,9.747398,8.930367,-8.821106,-8.362974,1.329228,-4.380016,8.899269,-5.029312,5.214680,8.897483,-7.169578,-3.824980,-2.624479,0.190736,-0.363419,3.411818,9.534952,-7.965173,2.556359,-5.865103,6.730758,6.172852,6.103605,0.546124,2.244407,3.651560,-9.120096,-5.696678,3.385803,9.566735,-2.745129,-3.027713,-3.337703,1.228365,3.497447,-4.344903,-5.628141,2.768441,4.097632,-2.584906,1.965070,7.320053,-5.336956,-9.950647,5.529388,1.879163,-1.805968,3.233941,-0.065245,-0.013168,-2.807552,-5.084609,-9.747389,9.321297,-9.939711,-7.235094,0.329871,-0.607681,-9.993661,8.277865,-0.202337,1.184200,-9.055654,3.459032,3.716570,1.676464,-1.418289,-1.990557,9.549162,6.735362,-1.087561,-9.550795,6.581758,7.845521,3.397256,9.412750,1.175427,3.647633,8.907875,-3.149135,-9.612424,6.007402,-2.916067,-6.875596,5.051998,1.042957,1.880199,7.042260,-3.713460,-0.841567,2.653299,-0.973463,-9.068334,4.312150,-6.996835,-5.275552,5.631101,-8.855023,-4.117655,8.425471,-1.186421,7.799343,-1.637837,-3.578847,6.910802,1.142319,-2.197995,3.659687,4.442122,-1.274354,-2.795916,-8.726300,-2.318591,2.046482,8.752719,-0.998832,-2.727220,-3.200616,-1.862367,9.781116,2.338605,6.192564,-2.938703,0.297019,8.450515,-3.238512,-2.976514,1.127579,8.192178,7.808986,6.000531,-1.787136,5.297218,2.340750,7.914162,0.360972,9.637805,-6.766539,7.597537,1.832861,7.527679,0.528099,-8.571990,9.595797,0.410497,0.463152,-1.584121,-1.962034,-7.904868,-0.818301,0.519114,-0.132189,-7.167381,-3.724289,-3.500655,-2.399593,1.899238,-0.121939,-7.120922,8.778273,-7.062323,-2.802216,-6.561347,2.258302,-4.011773,-4.016799,1.497073,-9.372181,3.375051,-7.077502,-4.775680,-0.116992,-8.682430,-7.243007,-2.234408,-9.638840,-0.929242,0.923721,-3.300648,5.320801,-7.180232,-3.637716,-1.490098,7.325227,2.175212,-5.599913,-4.390651,-9.712559,7.456992,1.705851,-0.237479,-4.420968,0.124477,-5.530439,-2.579143,-6.172414,1.955381,8.563536,-3.546801,-6.823295,-8.771188,2.032064,0.140971,4.912959,-5.484869,-1.870748,-7.718320,5.615531,-4.039479,7.117293,2.556965,-0.475671,-9.135296,8.824544,-8.686596,4.118667,-5.706890,-7.394566,-0.942426,-6.671797,-1.474230,0.657425,0.869038,-5.603459,-2.040465,0.391112,-2.006074,1.801113,9.596191,8.868492,-9.550036,-4.920869,8.128368,-7.528602,-1.554346,7.250653,8.739795,3.871164,4.691703,-8.395540,-0.555521,-0.104533,1.194181,6.622181,-1.709992,2.905759,7.442067,9.177963,-4.648873,-0.189334,-5.023869,5.670059,5.624347,-5.452748,3.410702,-5.749374,-0.457686,-3.605133,-9.091074,-4.830992,-3.140727,8.701947,3.586040,-8.803921,-3.359680,-4.817312,-3.379469,-6.415241,5.690030,7.590990,-1.213818,-8.499917,-4.032483,-4.342121,-1.475631,3.110730,-3.047598,9.133354,0.083653,0.217742,-5.889425,-8.049356,-9.202176,-5.740691,0.836146,-9.654818,-4.448550,1.885853,6.606703,3.309500,-9.496775,-1.912588,-2.768514,5.486653,7.003964,7.175813,-9.468556,1.125990,9.336678,-9.069240,3.660196,-1.854025,7.293472,-1.584028,9.903456,2.085806,-7.594518,9.069463,5.365690,-2.812655,5.286969,-3.239784,5.635256,-2.932482,-5.998588,0.365626,6.353474,6.347886,5.414796,4.449826,3.879132,0.105628,-2.835339,-7.440600,6.522194,9.217414,1.929020,-0.115829,9.334937,7.549782,-1.005487,3.939467,-4.740652,-5.873926,-9.346216,-8.266644,-0.082614,5.856811,-8.128816,-1.892157,-8.493722,8.266703,-3.187650,-6.862126,-8.097441,2.936982,-2.760162,4.334349,3.204654,8.522471,7.787078,4.950235,0.695588,2.664726,5.506845,9.305507,8.387516,6.449556,-7.642564,8.589565,7.678603,7.047229,2.795126,-7.892160,7.554109,-4.992384,9.271265,-7.525251,-0.275633,3.132351,-0.970740,0.764958,4.504505,8.232972,-2.131171,-2.411544,2.476273,6.234339,-6.324454,7.007374,1.579851,9.061735,4.705609,5.676138,4.829450,0.405495,8.156250,1.283651,9.825447,9.537865,8.173540,7.252137,0.777926,8.851100,-2.977584,8.612793,-2.157840,7.429675,5.769124,6.773675,7.578950,-7.553230,7.247113,4.901150,-6.907481,-5.525438,-8.701864,-6.226968,-6.166980,-0.499917,-5.930570,8.347974,-6.873359,-0.294479,1.328091,-4.990411,1.506191,-1.280898,-5.140724,1.858148,-9.519094,-7.166992,-9.135122,-6.954193,-2.346171,7.340086,4.886430,5.527988,3.259563,6.526319,4.420960,2.937114,-0.198559,5.722794,9.469217,9.304966,-5.603190,3.839207,-5.024064,4.858438,-5.380211,6.717806,5.412178,7.518757,-2.756058,-6.097029,-0.168579,-3.119937,1.392835,1.627702,2.621521,-5.090743,-4.915261,-3.057029,7.283510,3.719426,-4.757030,2.215958,3.949279,0.534242,7.439702,9.279161,5.435798,-6.614861,6.456201,-7.894125,-0.448121,-0.235228,-2.262578,9.873141,-7.760937,7.537459,0.801046,6.413671,5.007316,1.398991,-8.980261,-2.264846,-1.191578,-4.409628,-4.957726,-7.289952,6.470641,0.001931,2.073935,8.190829,4.304042,0.732290,-2.214557,0.870406,4.277734,-4.940210,2.461784,7.351413,-8.765311,0.971022,-4.481706,8.958828,-0.481258,9.257324,-4.329667,8.798068,5.577131,-8.595462,2.061516,5.147122,-4.055570,-6.061338,-6.620282,-3.086826,2.053201,6.964337,4.513566,1.722565,8.241013,-0.725320,-4.482590,1.016981,-1.356629,5.424326,5.083192,-6.124317,-6.983679,2.371594,-3.463813,9.392640,9.616839,-8.647375,-8.740276,-4.653254,-6.230806,1.333273,4.537078,3.331622,-6.508706,9.552348,2.006291,-9.186242,6.771166,5.826637,4.639252,7.633158,0.351673,7.328265,-6.804618,-5.581836,-9.717346,9.320309,-4.189991,2.847925,9.205276,4.640265,-9.952851,-9.300635,5.848939,-7.586976,1.405340,-5.232544,2.516087,-5.344237,8.942588,-8.344479,-4.861544,1.412066,-0.148318,7.070464,-2.075661,9.361222,-0.510004,-2.540904,7.905963,-4.873583,-1.043233,6.397353,0.683140,7.369352,-3.516405,-7.956993,2.991184,-8.896301,5.110323,4.191610,-8.383694,-0.624474,1.307884,-3.644588,7.065650,7.587406,0.092326,3.733356,-4.371777,-1.553281,6.598350,5.640611,-4.963569,-7.386815,1.020606,2.907586,-1.363056,7.252046,-0.912909,-4.685442,-7.037423,-1.942995,8.007123,-2.260382,-3.952903,-3.814822,-0.748327,5.792140,8.035507,-1.088249,9.789527,-2.332217,3.122110,1.342039,-6.225344,-0.298641,2.537520,-0.659459,-3.965249,-5.879189,5.856742,-9.228740,-1.731657,9.449295,-7.791490,6.994462,2.101505,7.608820,5.889435,0.002311,7.738851,-6.115372,-1.616898,6.094256,-7.780975,3.767646,-8.154096,8.327375,8.945758,5.321603,-7.629073,-3.522872,-9.915425,-2.035113,-8.059911,6.033107,7.834797,0.818487,9.113784,1.063664,-7.776999,3.591776,-9.915410,-1.039048,0.866675,6.711700,-8.959544,-9.252531,-6.025138,-9.083625,-7.018809,-9.947964,9.695057,9.304581,-2.496431,-9.553818,1.778657,2.876669,-4.032607,-0.287781,8.873341,9.796308,9.716559,6.186658,7.152021,-9.250708,2.642839,0.068237,-5.604900,9.308808,8.641442,-4.449846,-7.571190,7.051726,8.677470,-9.733955,5.921820,-4.052440,8.946364,-4.238770,3.394989,-5.092589,0.843825,2.032109,-1.535478,-8.461273,7.375943,4.001327,9.247616,-5.473409,-0.915120,2.254287,5.287433,-9.220255,8.364638,5.194816,7.011554,-7.811179,4.646302,9.197448,-6.560937,-9.923724,-8.825466,4.250224,-6.308745,-6.772510,4.061007,-1.247680,2.247028,4.453328,-4.255600,6.597763,8.556299,-8.993028,1.300923,-6.667706,-5.947415,1.690646,-1.337550,-9.198044,4.416196,9.400897,-9.542698,9.003699,-8.113610,4.477364,2.117856,4.756905,-9.139467,6.435685,1.995525,8.020011,-0.977248,-1.784045,-3.078396,8.157222,1.003306,-4.830735,2.181536,1.802559,-5.377163,-7.904854,9.863658,-3.992105,6.197014,5.665260,-7.564778,-8.602281,-5.635143,0.696585,1.918410,-2.147971,-9.695008,3.502333,-1.429432,5.296207,3.806731,-5.397102,4.875561,-2.290210,-7.627473,8.312543,-4.559175,-2.869593,-7.733388,5.097628,-8.207888,-6.268316,-8.984140,-9.436787,-4.580705,-0.512994,1.637927,-7.209175,9.974876,-4.308155,1.829573,-8.976584,7.449602,-6.185032,4.525193,-4.220387,5.496433,-5.095085,-9.971236,-7.085931,-6.994427,-9.709756,5.037196,0.846729,1.054337,-4.144095,6.778538,-9.525211,6.247204,5.350612,7.716646,4.474886,-3.135474,-1.196781,-0.647828,-6.079109,7.966192,2.520107,4.745451,-9.531212,-0.695231,1.568949,1.519806,-6.126338,-6.177926,0.529571,3.014717,-9.494038,-5.706525,-3.836917,8.562353,-2.625929,6.716395,4.196514,-3.182609,7.182721,1.057721,-8.767686,7.238409,9.451903,-8.873265,6.707079,8.783077,-5.763873,-0.682576,1.987856,6.047872,2.997344,6.900427,5.934938,-2.336577,-5.884644,-0.643289,-0.642477,8.890335,0.673197,4.590680,-9.641022,5.183818,-2.891104,5.746078,7.567477,3.730835,-2.588861,-3.543290,-8.020379,-5.945017,-6.223563,-1.370323,-8.746389,-1.446987,7.468133,-0.525067,0.146106,-3.143208,-5.825336,0.641822,-5.746588,-6.230273,3.054833,6.235991,3.680626,-0.371472,-3.605259,-6.152916,-0.134249,-4.421820,-6.537249,4.380431,-6.384422,-2.081624,-2.366702,0.500849,-0.343331,6.188448,-3.332863,-0.589647,-2.853937,9.097298,6.482754,-5.600406,-7.175565,9.567907,6.352711,-1.041364,4.714377,-1.673201,-5.443295,-1.184539,3.448089,-4.496607,-6.798172,7.878425,2.711350,3.241629,0.250880,5.525676,9.149214,-5.599923,3.101686,-7.445686,4.207988,-8.805481,-8.173320,5.027978,-0.345357,9.209432,-7.046334,-7.399362,0.648860,-0.338046,2.591538,9.418603,-4.696144,1.537498,-0.110951,-7.920997,8.212848,-2.291646,-2.955275,8.410069,6.865738,5.657846,-7.458327,-3.247831,-3.364665,-7.063390,-7.677569,-2.091888,9.537070], dtype = "float32")#candidate|14015|(1690,)|const|float32
call_14014 = relay.TupleGetItem(func_9294_call(relay.reshape(const_14015.astype('float32'), [13, 13, 10])), 1)
call_14016 = relay.TupleGetItem(func_9297_call(relay.reshape(const_14015.astype('float32'), [13, 13, 10])), 1)
func_10673_call = mod.get_global_var('func_10673')
func_10676_call = mutated_mod.get_global_var('func_10676')
const_14019 = relay.const([-10,-8,9,9,-3,8,-1,-2,7,-3,-10,1,5,-8,-3,-9,5,1,-7,1,-9,1,6,-10,-5,-8,-10,-2,6,-5,-2,-2,-2,-1,5,-6,-3,-4,-4,1,-9,-4,-5,-8,-4,-10,5,-3,6,3,-8,-6,10,9,6,1,7,6,10,3,-7,2,6,9,3,-1,-3,-3,9,-4,2,-10,-3,-2,-10,-10,-9,-9,10,-7,1,6,-7,6,-1,-8,-10,-5,-7,-7,-4,-4,-9,-10,-2,-2,4,-7,-6,-6,-5,-3,5,7,7,-8,1,5,-6,9,-1,1,8,8,-2,5,1,2,6,-7,-5,5,9,-6,-5,5,5,-5,5,-8,-8,-4,-1,-6,-10,-1,1,1,-5,5,1,10,-7,6,6,8,-9,6,3,-6,-8,7,2,-9,4,-9,-5,10,1,3,2,-5,8,-8,5,3,4,1,10,4,-4,-1,-1,-1,7,-4,-7,-7,-10,5,2,9,10,1,-1,-5,8,-4,-7,1,-10,2,-4,2,5,-1,7,-2,-1,-8,7,-5,-9,4,-5,9,-8,3,-9,5,-4,2,6,10,-8,10,-2,-10,6,-7,9,-8,-7,10,-8,2,3,3,8,9,-2,1,3,-4,-7,4,1,4,5,-3,-1,4,9,-3,3,-2,10,8,9,6,7,6,2,-5,4,-9,-5,8,2,-10,5,9,-9,1,-3,6,9,-7,1,-9,9,1,2,-7,-3,9,-1,3,9,8,5,1,7,6,-9,-5,2,4,5,8,8,-4,-8,-9,-5,1,2,-3,-10,-6,-3,-9,7,8,-3,-8,4,2,-10,-10,-9,-4,-3,-1,-5,3,-10,-2,-4,-6,7,-9,-5,4,3,2,-7,6,-5,-4,-6,10,-9,-10,3,1,-10,-10,3,-4,-9,10,-5,7,-5,-2,-10,-8,5,4,-6,7,-5,-2,-10,-7,-5,3,5,-9,1,-5,6,-9,-1,-8,-8,-4,-1,-3,5,7,9,7,2,-8,9,-5,5,5,-9,-5,-9,1,-7,10,6,-1,1,-1,-6,-7,2,-10,-10,-5,8,-7,10,7,-4,-1,-6,7,2,10,9,-5,-1,-10,-9,-1,6,4,-8,3,-9,2,7,-1,-9,9,10,1,-8,-4,5,-4,3,-6,2,-1,-6,-6,-4,3,10,1,5,-1,2,-10,9,7,5,-3,7,-5,8,-7,10,6,-2,-10,-1,-10,6,-10,-5,9,2,-6,-5,-3,4,-7,-10,2,2,-10,3,-7,-9,6,-4,3,-6,-7,2,5,-10,8,-7,-3,-2,-3,-3,4,7,-8,-4,9,2,10,-5,-7,9,-4,-6,7,-10,-5,-1,6,8,9,7,-9,-3,4,-7,-1,-8,3,2,4,-10,-4,5,-9,4,-4,-7,1,-5,7,7,8,-3,-9,-3,-6,1,6,-7,-10,6,-3,10,-2,-8,7,-9,1,8,-8], dtype = "int64")#candidate|14019|(546,)|const|int64
call_14018 = relay.TupleGetItem(func_10673_call(relay.reshape(const_14019.astype('int64'), [7, 6, 13]), relay.reshape(const_14019.astype('int64'), [7, 6, 13]), ), 0)
call_14020 = relay.TupleGetItem(func_10676_call(relay.reshape(const_14019.astype('int64'), [7, 6, 13]), relay.reshape(const_14019.astype('int64'), [7, 6, 13]), ), 0)
func_13780_call = mod.get_global_var('func_13780')
func_13781_call = mutated_mod.get_global_var('func_13781')
call_14026 = func_13780_call()
call_14027 = func_13780_call()
func_8750_call = mod.get_global_var('func_8750')
func_8755_call = mutated_mod.get_global_var('func_8755')
const_14041 = relay.const([-1,9,-4,-10,-9,8,5,10,-3,2,-1,3,6,10,1,8,-8,1,-4,-9,-7,8,10,-9,8,-10,-2,1,-4,-6,8,8,-10,2,-9,1,-9,7,-7,-4,-10,6,-9,9,-9,10,-10,-5,-7,-8,-9,-2,8,-10,8,1,-8,1,5,-3,-9,-2,-1,-3,6,-7,-10,3,-10,4,7,-9,4,2,-2,-4,8,-9,-2,7,4,3,3,-6,9,3,7,10,-2,1,-9,-4,-10,6,-7,-2,-5,7,-10,-2,-4,2,-5,-5,5,2,10,1,-10,3,-7,8,-9,3,9,6,-8,-5,1,1,-5,-1,8,-8,-6,6,6,-9,-1,4,-6,5,9,9,9,7,5,-2,10,1,-3,-1,-3,5,3,-3,-10,-2,-8,10,-3,5,4,2,7,10,-2,-10,1,8,3,-2,-10,3,-5,9,-9,-9,2,-7,-7,-1,-7,-4,4,-2,-3,-3,7,3,6,-4,-6,8,-6,-9,1,2,2,-6,-7,-5,-1,5,4,-3,-2,7,-2,8,-1,1,-10,10,10,-8,4,-7,-4,6,2,10,8,4,2,8,-10,7,-3,-1,3,-9,-3,-6,9,-4,-1,5,-2,9,-2,9,-7,3,1,4,3,3,-10,-2,-10,1,3,-1,6,8,9,1,2,-8,8,-9,5,-5,-2,5,-7,3,6,-2,-4,-2,8,8,7,-4,-8,-4,-8,8,-9,-2,-1,4,-9,-10,9,-7,-5,-8,1,-5,-7,-3,-9,-5,-6,-3,-3,4,7,6,-6,-4,8,-1,-6,-9,7,-9,5,-5,2,7,8,9,3,-3,10,10,-1,-8,-9,-1,-1,5,4,-6,-1,-2,-2,6,8,-4,7,6,-5,5,1,4,-6,-7,-10,-7,-4,2,9,1,7,6,9,4,-4,10,6,-7,-3,-3,7,-6,8,-9,7,-4,5,-10,10,6,4,-1,-10,-5,5,5,-7,-5,2,1,3,-6,7,-1,-2,3,3,-8,-4,-5,10,-1,5,-3,-9,6,2,-10,-8,6,-8,-7,4,-5,10,-7,1,9,-5,1,-7,-6,9,-5,-5,-10,-3,5,4,-6,-1,5,3,6,-4,-10,5,7,-1,4,7,-2,-9,-8,8,-7,6,-1,-4,7,-5,9,4,-6,2,3,-4,-10,4,7,-1,-3,4,8,-2,-8,-3,-8,6,-1,6,8,1,-2,-7,8,-1,8,4,5,-2,-2,-1,1,-4,6,8,-9,-5,5,10,-1,-2,-8,7,-10,-8,6,-3,-7,-7,9,8,-4,7,-4,-3,-7,5,1,9,-3,-6,-6,-3,-7,5,-8,4,-5,-3,9,3,-1,3,10,-7,-1,-1,-5,-10,-7,-8,8,-8,4,-2,-7,9,3,4,-4,-4,8,-1,-10,-3,6,3,-5,8,4,10,-5,1,-1,-9,8,9,1,-8,9,-9,5,10,2,-9,6,-8,-10,-6,8,5,1,1,-2,-2,-2,-7,-4,9,2,4,1,10,-3,-2,4,-6,-3,-6,7,7,10,6,-8,-9,5,10,-5,5,7,-10,9,5,-2,7,10,9,-6,5,10,-6,-7,-8,9,2,-5,6,-8,-5,3,-2,-4,6,-7,-5,2,1,2,-4,7,6,8,-7,4,-9,-2,1,-3,9,7,-7,7,-10,9,9,-2,9,6,8,-8,8,-7,7,7,8,-1,-3,-2,9,-9,-9,-5,2,-4,3,7,-3,10,4,7,-1,8,-7,1,6,-4,10,3,1,2,1,-5,4,4,5,4,10,-4,-4,2,-4,5,6,-7,7,-10,9,-5,-3,2,2,5,-8,8,-3,-2,-7,-10,6,9,-7,4,-8,-8,1,10,8,5,4,9,-4,-4,-7,3,4,-9,-4,-6,3,3,7,-5,-9,-10,6,10,-10,10,-1,-3,6,5,-4,-2,6,-10,9,8,8,10,-7,5,-5,7,9,-2,-1,-4,-9,-1,-2,-9,-6,8,5,9,6,-9,8,-10,3,9,10,-8,-2,7,-10,6,3,10,-9,8,-3,-10,-1,8,-4,-10,2,5,-7,-9,-9,2,8,8,3,5,-4,-8,7,1,-5,-8,-8,-3,7,1,7,-8,7,4,-5,-7,6,-4,-1,6,5,-3,9,10,-9,2,6,3,-9,3,-8,10,6,-8,-8,-5,8,-10,5,3,-2,-10,-6,-4,-9,-8,9,-2,-2,6,-5,-5,-8,-10,-6,4,7,-10,6,9,-3,4,-4,9,-5,6,-3,-10,7,-3,-2,-2,-1,-5,4,-4,-10,-1,3,8,4,-7,-8,-9,9,-7,8,-2,-10,8,1,-3,8,-3,5,-8,-9,7,4,-2,7,-5,-9,-6,4,-4,-5,5,-2,-6,-2,-5,3,-6,-7,9,-8,-1,-1,-5,-2,-1,-8,2,-5,-9,7,7,8,-7,4,9,10,8,-8,10,3,-6,-10,-3,1,3,9,-7,5,-2,-8,10,10,3,2,7,-5,-6,-3,1,4,1,-5,-10,2,1,2,10,-1,9,6,-9,-9,9,6,6,-3,-3,7,1,5,1,-3,-9,-6,6,-4,-7,9,-7,-4,-5,1,-7,1,-10,-10,-2,-4,5,-9,3,7,-8,-4,1,7,-8,4,-9,-5,-9,-1,-6,-4,-6,4,-8,-1,-7,-1,-4,-6,9,2,-3,8,-2,5,-6,10,1,3,-5,8,-9,2,-9,10,6,-7,-6,3,6,5,6,-7,-9,6,5,8,3,1,-8,-10,-2,-5,2,8,7,-3,1,10,10,-6,2,-1,3,6,3,-8,-3,-5,3,4,-7,3,-6,-7,-10,1,6,6,-4,-1,-8,-3,-3,7,-10,-6,-9,6,-3,-10,-6,5,-1,-1,3,3,2,4,2,1,-4,2,7,7,-9,-3,7,8,8,6,-3,5,-3,-1,10,-1,-1,8,-9,8,-3,4,10,2,3,-9,5,2,-3,-6,-6,-9,-8,-5,-3,6,5,-8,3,-10,5,3,-5,9,7,-5,2,8,-3,8,7,2,5,-4,9,7,7,-4,-4,-2,-10,-1,-1,4,-3,1,-8,1,-4,-4,-1,5,-2], dtype = "int32")#candidate|14041|(1152,)|const|int32
const_14042 = relay.const([-2,5,-4,-1,9,-10,8,10,-1,5,-9,-7,2,1,5,-6,-10,6,7,10,-3,-9,-10,-3,3,6,-4,-2,-9,6,10,2,2,-3,5,-7,4,9,6,-6,-9,2,7,8,8,9,-8,7,9,1,3,-2,3,-2,-3,-7,-1,6,2,4,-9,-9,6,-1,5,-8,-7,5,4,-8,-6,-1,-3,-4,2,8,-3,-2,-2,-3,-2,-3,-3,-10,8,4,-2,-10,2,3,-2,-7,7,-3,10,-6,-10,3,9,-10,1,10,1,-10,4,8,4,10,-5,-10,10,7,-5,3,4,-3,-7,8,-5,-10,-4,4,4,-1,6,3,-9,5,-3,-10,-2,-3,7,9,-4,10,9,-5,-7,-1,-10,-10,7,5,-8,8,-9,10,-4,8,2,-5,-2,-4,-9,-6,1,7,5,-7,-6,-2,-8,9,-5,-2,-6,8], dtype = "int8")#candidate|14042|(168,)|const|int8
call_14040 = relay.TupleGetItem(func_8750_call(relay.reshape(const_14041.astype('int32'), [16, 12, 6]), relay.reshape(const_14041.astype('int32'), [16, 12, 6]), relay.reshape(const_14042.astype('int8'), [168,]), ), 0)
call_14043 = relay.TupleGetItem(func_8755_call(relay.reshape(const_14041.astype('int32'), [16, 12, 6]), relay.reshape(const_14041.astype('int32'), [16, 12, 6]), relay.reshape(const_14042.astype('int8'), [168,]), ), 0)
uop_14057 = relay.sin(call_14014.astype('float64')) # shape=(8, 16, 15)
uop_14059 = relay.sin(call_14016.astype('float64')) # shape=(8, 16, 15)
output = relay.Tuple([call_13957,const_14015,call_14018,const_14019,call_14026,call_14040,const_14041,const_14042,uop_14057,])
output2 = relay.Tuple([call_13958,const_14015,call_14020,const_14019,call_14027,call_14043,const_14041,const_14042,uop_14059,])
func_14061 = relay.Function([], output)
mod['func_14061'] = func_14061
mod = relay.transform.InferType()(mod)
output = func_14061()
func_14062 = relay.Function([], output)
mutated_mod['func_14062'] = func_14062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13017_call = mod.get_global_var('func_13017')
func_13019_call = mutated_mod.get_global_var('func_13019')
call_14145 = func_13017_call()
call_14146 = func_13017_call()
output = relay.Tuple([call_14145,])
output2 = relay.Tuple([call_14146,])
func_14151 = relay.Function([], output)
mod['func_14151'] = func_14151
mod = relay.transform.InferType()(mod)
mutated_mod['func_14151'] = func_14151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14151_call = mutated_mod.get_global_var('func_14151')
call_14152 = func_14151_call()
output = call_14152
func_14153 = relay.Function([], output)
mutated_mod['func_14153'] = func_14153
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13017_call = mod.get_global_var('func_13017')
func_13019_call = mutated_mod.get_global_var('func_13019')
call_14159 = func_13017_call()
call_14160 = func_13017_call()
output = relay.Tuple([call_14159,])
output2 = relay.Tuple([call_14160,])
func_14169 = relay.Function([], output)
mod['func_14169'] = func_14169
mod = relay.transform.InferType()(mod)
output = func_14169()
func_14170 = relay.Function([], output)
mutated_mod['func_14170'] = func_14170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13565_call = mod.get_global_var('func_13565')
func_13567_call = mutated_mod.get_global_var('func_13567')
call_14235 = relay.TupleGetItem(func_13565_call(), 0)
call_14236 = relay.TupleGetItem(func_13567_call(), 0)
output = relay.Tuple([call_14235,])
output2 = relay.Tuple([call_14236,])
func_14241 = relay.Function([], output)
mod['func_14241'] = func_14241
mod = relay.transform.InferType()(mod)
output = func_14241()
func_14242 = relay.Function([], output)
mutated_mod['func_14242'] = func_14242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14151_call = mod.get_global_var('func_14151')
func_14153_call = mutated_mod.get_global_var('func_14153')
call_14249 = relay.TupleGetItem(func_14151_call(), 0)
call_14250 = relay.TupleGetItem(func_14153_call(), 0)
func_4833_call = mod.get_global_var('func_4833')
func_4837_call = mutated_mod.get_global_var('func_4837')
const_14262 = relay.const([-6,8,6,-4,-5,9,-8,2,2,-10,7,-1,8,-2,9,-2,6,4,10,-6,-8,-2,1,6,5,6,-3,-8,-3,9,-8,10,1,-5,-3,-3,-7,7,-1,1,10,-10,4,-3,6,2,3,7,5,2,-4,-7,3,9,9,-10,7,2,-7,2,-9,9,-4,5,-10,-7,3,5,10,-10,4,-7,-1,6,-4,-3,-1,-4,-9,-6,5,3,-9,-5], dtype = "int8")#candidate|14262|(84,)|const|int8
var_14263 = relay.var("var_14263", dtype = "int8", shape = (84, 2))#candidate|14263|(84, 2)|var|int8
call_14261 = func_4833_call(relay.reshape(const_14262.astype('int8'), [1, 6, 14]), relay.reshape(var_14263.astype('int8'), [2, 6, 14]), )
call_14264 = func_4833_call(relay.reshape(const_14262.astype('int8'), [1, 6, 14]), relay.reshape(var_14263.astype('int8'), [2, 6, 14]), )
func_13749_call = mod.get_global_var('func_13749')
func_13751_call = mutated_mod.get_global_var('func_13751')
call_14266 = func_13749_call()
call_14267 = func_13749_call()
uop_14274 = relay.sinh(call_14261.astype('float32')) # shape=(2, 6, 14)
uop_14276 = relay.sinh(call_14264.astype('float32')) # shape=(2, 6, 14)
func_1283_call = mod.get_global_var('func_1283')
func_1286_call = mutated_mod.get_global_var('func_1286')
const_14279 = relay.const([6,-5,-3,-3,9,7,-10,-6,9,5,3,8,-8,4,-7,-9,1,3,-5,3,2,-3,-6,3,2,7,9,-1,-8,-5,8,-9,-7,10,-9,-5,6,-3,9,-8,-6,-8,10,-2,-4,5,-2,-10,-9,1,7,10,6,-6,9,-3,10,-10,3,-9,2,9,-2,-2,-1,-8,-1,-4,2,-9,7,-8,7,7,3,-5,2,8,6,5,-7,8,3,-4,-3,10,6,6,9,3,1,-6,3,9,7,9,-8,1,-10,-8,7,2,7,9,3,-7,-10,-9,10,4,-1,1,-1,-3,-7,-1,-1,10,-1,6,-10,8,8,5,-7,-7,-4,-10,-3,6,-3,8,2,-4,8,-6,-2,8,-4,-10,-4,9,-9,4,1,-4,7,-10,10,1,-1,6,-1,-5,-1,-6,-6,-4,-6,-7,-8,-3,4,3,7,-2,1,4,-6,1,-8,10,-3,-8,-3,-8,-7,6,-6,5,-5,4,7,-1,10,8,-8,1,5,2,4,10,3,-1,9,2,5,3,7,4,-6,5,-3,7,4,9,-1,9,9,3,-8,-3,5,4,7,-9,-2,-1,1,-4,-9,-2,6,-6,-3,-2,-6,-5,-8,-10,9,-10,-4,-6,8,9,-7,-10,6,5,-5,-2,1,-1,-6,-5,-2,6,5,10,-3,5,-4,2,-2,-9,3,9,9,-2,1,-2,4,7,-1,5,10,4,6,1,-5,7,2,-4,4,-5,-3,7,4,-7,3,-9,-5,-6,-10,-10,-9,-3,-1,-1,-2,1,5,5,2,-4,-7,9,-7,2,1,-4,-7,3,-3,6,-3,3,4,7,9,2,-6,7,-5,-5,-8,-9,4,-6,6,-2,-8,-5,2,-10,-5,8,-1,-9,3,3,10,10,-3,5,-8,-8,-4,1,-9,9,-3,-7,4,-3,9,10,-9,7,7,-3,9,-3,6,-8,-5,9,4,6,-4,-4,-6,-6,5,1,7,4,5,10,-1,8,-5,-8,5,-8,-3,-3,7,6,-5,3,-8,10,6,9,-8,5,-4,-4,-5,7,5,6,1,5,6,-10,4,-2,-9,8,-7,-1,-6,-9,5,10,8,-3,8,9,-3,10,10,-8,2,6,-10,10,2,-8,7,-9,4,8,-10,-7,5,-2,1,5,7,5,-10,7,6,1,5,-10,5,-2,2,-10,9,3,-2,-3,2,10,5,-4,-3,4,-8,-9,-10,-8,2,-1,-9,-9,5,-2,2,-6,9,5,8,2,-4,9,-3,8,6,-4,-6,-6,7,-7,-1,-3,5,-4,9,-1,8,7,-10,5,-4,8,2,-2,-3,-7,2,-5,-9,-1,5,-1,3,-4,-3,-8,-8,7,-10,10,-8,8,-10,-8,-9,9,-3,9,-8,-1,-2,6,-5,1,-3,-9,-9,-8,9,9,-7,4,-9,-7,3,-6,5,4,-8,-5,7,10,2,-6,6,-9,-2,-2,-5,7,-5,5,-8,9,-6,-7,-10,-9,-8,3,8,8,6,-2,9,3,6,-5,8,2,-10,-7,9,5,10,-1,2,2,-9,1,8,5,3,-8,-6,7,1,-10,-1,-8,-3,-3,10,4,-10,9,-10,-1,4,6,-2,-8,10,-5,-3,3,-4,2,10,3,-3,-7,7,-8,9,-3,-8,4,-10,-8,-2,10,7,-9,-8,-10,-7,1,-7,6], dtype = "int8")#candidate|14279|(630,)|const|int8
call_14278 = relay.TupleGetItem(func_1283_call(relay.reshape(const_14279.astype('int8'), [9, 7, 10]), relay.reshape(const_14279.astype('int8'), [9, 7, 10]), ), 0)
call_14280 = relay.TupleGetItem(func_1286_call(relay.reshape(const_14279.astype('int8'), [9, 7, 10]), relay.reshape(const_14279.astype('int8'), [9, 7, 10]), ), 0)
output = relay.Tuple([call_14249,const_14262,var_14263,call_14266,uop_14274,call_14278,const_14279,])
output2 = relay.Tuple([call_14250,const_14262,var_14263,call_14267,uop_14276,call_14280,const_14279,])
func_14286 = relay.Function([var_14263,], output)
mod['func_14286'] = func_14286
mod = relay.transform.InferType()(mod)
var_14287 = relay.var("var_14287", dtype = "int8", shape = (84, 2))#candidate|14287|(84, 2)|var|int8
output = func_14286(var_14287)
func_14288 = relay.Function([var_14287], output)
mutated_mod['func_14288'] = func_14288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14061_call = mod.get_global_var('func_14061')
func_14062_call = mutated_mod.get_global_var('func_14062')
call_14295 = relay.TupleGetItem(func_14061_call(), 3)
call_14296 = relay.TupleGetItem(func_14062_call(), 3)
func_10565_call = mod.get_global_var('func_10565')
func_10570_call = mutated_mod.get_global_var('func_10570')
const_14318 = relay.const([-9,7,6,-1,7,1,10,9,5,-6,7,3,5,8,-4,-3,1,-1,1,4,-9,2,-3,9,-4,3,7,1,-5,-4,-5,-4,-8,-7,-6,9,-8,-5,1,6,-1,7,8,9,-9,2,1,-4,10,-10,-2,10,-1,8,-10,-7,5,6,2,-7,-10,8,-7,-2,4,3,-2,-8,9,5,2,10,-6,1,4,10,10,-7,10,4,-5,2,2,-10,-5,10,-7,-5,7,-2,7,-6,1,4,5,5,-4,7,6,9,-4,-9,1,5,-1,10,-10,2,10,-3,3,6,7,-7,3,-4,-5,10,-6,-6,2,4,-2,3,2,8,-6,-5,10,-5,8,-9,-2,-10,4,5,2,1,-6,6,2,5,10,8,4,4,3,-6,2,3,-2,5,-10,5,-1,-5,-9,-9,-2,1,-2,-7,-8,-10,-9,-8,3,-4,-8,-8,2,-9,4,9,7,-2,-5,-4,2,-3,6,3,-3,-2,-5,-9,4,7,-8,-3,-8,-5,-4,6,-4,-8,-8,-10,7,1,2,1,10,1,-6,-4,-9,-9,-10,10,2,4,8,-3,6,9,6,2,-7,5,-9,-10,-9,-3,2,3,-9,7,1,-4,-6,4,2,9,1,5,-4,-10,1,-4,-7,10,5,5,7,-4,-4,-6,-4,-10,-2,7,-9,1,-10,-7,-1,3,2,4,1,4,-6,-4,9,7,10,-7,1,-10,-2,-10,-4,9,-2,7,10,-9,-6,-9,8,6,8,-6,3,1,-5,-6,-3,4,9,9,7,-8,-2,7,10,9,-9,8,4,-5,10,7,8,9,7,9,-7,-4,-3,-2,-4,-5,-7,-5,2,-10,-1,8,-10,-9,6,-8,6,-1,-5,-3,3,4,-1,-2,6,9,-1,-1], dtype = "int16")#candidate|14318|(336,)|const|int16
const_14319 = relay.const([8,7,-4,1,-6,5,-8,-10,6,2,-7,10,4,-5,10,3,3,-8,-10,8,-4,4,7,-1,-4,-7,-7,6,-4,8,-6,-4,10,-5,-2,8,5,-10,-8,9,3,2,4,-3,-8,4,1,4,-1,6,1,1,-8,10,3,7,-7,8,-6,10,2,-9,-2,-6,1,6,8,7,10,9,9,9,-6,7,-6,5,1,-2,-8,-7,2,10,-3,-3,4,-4,9,-9,8,4,-3,3,6,6,-4,2,6,-4,-7,-2,1,6,-7,3,-4,-1,-10,10,2,10,1,-1,-4,-8,6,-3,-3,-6,-7,8,-8,8,-5,-3,-6,-2,5,-6,2,9,3,2,-3,6,7,-1,5,4,8,5,-10,-3,-2,-3,2,-10,-4,-10,-1,8,2,-5,-3,-5,8,-6,-8,-3,-7,-5,-10,1,7,2,-10,10,-4,-9,5,7,-5,-10,-2,-3,1,8,-3,7,2,2,2,4,-6,-2,-6,-2,3,-3,-9,4,6,-3,-10,-1,-8,4,4,7,-10,10,-9,8,6,-7,-10,7,10,7,8,2,-2,7,6,-5,-4,-4,-7,3,4,10,-10,3,7,-1,9,-3,2,8,-6,4,-8,-3,1,-10,-5,-2,-9,4,-7,3,8,9,-9,-8,10,7,2,-2,-5,9,-7,4,8,-4,-10,-2,-4,-10,8,10,-2,5,-6,-9,1,10,3,-6,9,-5,-8,9,8,6,7,-3,2,5,4,8,3,5,-9,4,-2,7,6,5,3,-9,9,9,9,-1,7,-8,7,-6,-4,-4,-3,-8,7,2,-5,2,4,-7,-7,-4,8,-7,-5,9,7,-6,6,-9,5,5,-6,-4,-2,3,-9,-6,-9,10,-7,-3,-4,-5,3,5,7,8,9,-4,-2,10,4,-8,10,8,9,-4,-2,-3,-6,1,-8,-7,-2,10,7,-7,8,5,3,7,-7,-5,3,4,-6,-3,5,-3,-2,-10,3,-10,-3,8,10,-10,-8,8,2,-1,8,-5,3,-9,-1,3,-6,-4,10,7,-9,1,-1,-1,2,3,5,2,-8,-4], dtype = "uint8")#candidate|14319|(400,)|const|uint8
call_14317 = relay.TupleGetItem(func_10565_call(relay.reshape(const_14318.astype('int16'), [7, 16, 3]), relay.reshape(const_14318.astype('int16'), [7, 16, 3]), relay.reshape(const_14319.astype('uint8'), [400,]), ), 1)
call_14320 = relay.TupleGetItem(func_10570_call(relay.reshape(const_14318.astype('int16'), [7, 16, 3]), relay.reshape(const_14318.astype('int16'), [7, 16, 3]), relay.reshape(const_14319.astype('uint8'), [400,]), ), 1)
func_6191_call = mod.get_global_var('func_6191')
func_6194_call = mutated_mod.get_global_var('func_6194')
call_14332 = relay.TupleGetItem(func_6191_call(relay.reshape(call_14317.astype('uint8'), [14, 8, 3]), relay.reshape(const_14318.astype('uint8'), [14, 8, 3]), ), 0)
call_14333 = relay.TupleGetItem(func_6194_call(relay.reshape(call_14317.astype('uint8'), [14, 8, 3]), relay.reshape(const_14318.astype('uint8'), [14, 8, 3]), ), 0)
func_13780_call = mod.get_global_var('func_13780')
func_13781_call = mutated_mod.get_global_var('func_13781')
call_14339 = func_13780_call()
call_14340 = func_13780_call()
output = relay.Tuple([call_14295,call_14317,const_14318,const_14319,call_14332,call_14339,])
output2 = relay.Tuple([call_14296,call_14320,const_14318,const_14319,call_14333,call_14340,])
func_14341 = relay.Function([], output)
mod['func_14341'] = func_14341
mod = relay.transform.InferType()(mod)
mutated_mod['func_14341'] = func_14341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14341_call = mutated_mod.get_global_var('func_14341')
call_14342 = func_14341_call()
output = call_14342
func_14343 = relay.Function([], output)
mutated_mod['func_14343'] = func_14343
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14362 = relay.var("var_14362", dtype = "float32", shape = (11, 13, 14))#candidate|14362|(11, 13, 14)|var|float32
uop_14363 = relay.cosh(var_14362.astype('float32')) # shape=(11, 13, 14)
output = uop_14363
output2 = uop_14363
func_14375 = relay.Function([var_14362,], output)
mod['func_14375'] = func_14375
mod = relay.transform.InferType()(mod)
var_14376 = relay.var("var_14376", dtype = "float32", shape = (11, 13, 14))#candidate|14376|(11, 13, 14)|var|float32
output = func_14375(var_14376)
func_14377 = relay.Function([var_14376], output)
mutated_mod['func_14377'] = func_14377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14169_call = mod.get_global_var('func_14169')
func_14170_call = mutated_mod.get_global_var('func_14170')
call_14390 = relay.TupleGetItem(func_14169_call(), 0)
call_14391 = relay.TupleGetItem(func_14170_call(), 0)
output = call_14390
output2 = call_14391
func_14400 = relay.Function([], output)
mod['func_14400'] = func_14400
mod = relay.transform.InferType()(mod)
output = func_14400()
func_14401 = relay.Function([], output)
mutated_mod['func_14401'] = func_14401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13485_call = mod.get_global_var('func_13485')
func_13487_call = mutated_mod.get_global_var('func_13487')
call_14411 = func_13485_call()
call_14412 = func_13485_call()
func_4470_call = mod.get_global_var('func_4470')
func_4472_call = mutated_mod.get_global_var('func_4472')
const_14419 = relay.const([-10,-1,8,7,4,-10,-10,-8,-3,-3,-7,8,2,-8,-4,3,8,8,-3,9,5,-4,-8,9,9,-8,6,-10,9,5,1,-9,2,-8,2,-6,-9,-4,-1,2,-5,-6,4,1,-4,-1,6,7,-7,7,-2,-6,1,10,3,4,10,-10,6,2,-2,6,-2,8,-7,9,-5,-2,7,10,2,9,-4,8,4,1,-2,-4,1,4,-6,-9,9,9,3,-7,1,-1,-7,-4,-1,-7,-5,7,-2,6,-5,-10,6,4,7,8,-7,3,-8,-5,4,-1,-4,5,-1,-3,-5,3,-2,-3,-8,7,10,1,8,4,-9,-1,5,-8,-6,-3,6,4,-4,-7,10,10,-5,-7,-7,7,7,-1,-5,-9,2,3,7,-7,8,3,-9,9,2,-1,8,8,-7,10,-8,4,-10,-7], dtype = "int16")#candidate|14419|(160,)|const|int16
call_14418 = func_4470_call(relay.reshape(const_14419.astype('int16'), [5, 8, 4]))
call_14420 = func_4470_call(relay.reshape(const_14419.astype('int16'), [5, 8, 4]))
func_13565_call = mod.get_global_var('func_13565')
func_13567_call = mutated_mod.get_global_var('func_13567')
call_14431 = relay.TupleGetItem(func_13565_call(), 0)
call_14432 = relay.TupleGetItem(func_13567_call(), 0)
output = relay.Tuple([call_14411,call_14418,const_14419,call_14431,])
output2 = relay.Tuple([call_14412,call_14420,const_14419,call_14432,])
func_14452 = relay.Function([], output)
mod['func_14452'] = func_14452
mod = relay.transform.InferType()(mod)
mutated_mod['func_14452'] = func_14452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14452_call = mutated_mod.get_global_var('func_14452')
call_14453 = func_14452_call()
output = call_14453
func_14454 = relay.Function([], output)
mutated_mod['func_14454'] = func_14454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13749_call = mod.get_global_var('func_13749')
func_13751_call = mutated_mod.get_global_var('func_13751')
call_14479 = func_13749_call()
call_14480 = func_13749_call()
uop_14488 = relay.exp(call_14479.astype('float64')) # shape=(15, 4, 16)
uop_14490 = relay.exp(call_14480.astype('float64')) # shape=(15, 4, 16)
func_2115_call = mod.get_global_var('func_2115')
func_2118_call = mutated_mod.get_global_var('func_2118')
var_14493 = relay.var("var_14493", dtype = "float32", shape = (96, 2))#candidate|14493|(96, 2)|var|float32
const_14494 = relay.const([-5.140293,-3.106957,-6.959680,-9.566030,8.788406,0.535018,4.054617,-7.286935,8.340937,-0.012806,5.818248,-5.103876,2.050861,4.997601,-2.866750,7.873400,8.729366,-4.884969,9.626599,-8.964885,-3.408160,-8.969662,-2.300164,0.247229,-7.523711,-9.491666,-4.310203,-8.796350,-7.967794,-6.670704,-0.217082,2.732881,3.093638,-4.214944,0.406896,-5.697590,-2.291490,2.702800,4.966649,6.942155,-6.875046,6.318296,-5.551896,-9.897120,1.003412,9.167723,8.402003,1.345042,-2.351799,3.327376,-1.009210,-3.639389,-5.834050,3.006882,-8.222077,-5.982795,-6.073543,6.977750,5.526978,-3.325475,-7.109022,-8.683428,-5.230166,-6.275448,8.531737,-1.975387,0.935623,6.125922,-2.843234,6.316453,7.575447,7.631213,2.667215,-9.191518,9.384685,-5.881833,-2.248345,2.831395,-9.629796,-6.341787,1.259070,-5.116064,8.717735,9.740789,-0.227332,-0.957957,-8.504355,-5.049276,-1.343624,-9.551670,2.721571,5.720426,2.948417,-6.776092,-7.315468,-3.645952,-8.825487,5.573094,-1.219413,1.327000,1.232194,-8.594652,-6.448531,-4.928969,2.281670,-6.788731,6.826204,-6.435503,-2.833439,-9.207495,2.838162,-6.706506,2.844856,6.126844,-6.782928,5.915004,-5.021019,2.859231,-9.956177,3.805821,-5.309737,-2.395182,1.916103,1.168718,4.876644,5.905856,-3.816622,-1.990780,7.473980,6.308977,8.026616,0.026294,-0.875761,-1.830995,-4.622799,-6.436030,2.834076,-8.014978,9.123029,-7.729448,-9.631034,-2.401174,7.415217,-7.707246,-3.746626,6.230567,-6.830499,-3.959791,4.453812,7.336701,-9.844375,7.228235,-3.372994,8.257888,2.207933,3.843062,0.562139,-6.952695,-1.048287,3.414784,-9.090693,-7.055837,4.366438,1.466728,4.069023,1.890558,-1.562846,7.591471,-9.836953,-2.123960,-4.146190,7.207140,6.453193,7.348793,6.143117,9.443319,0.100402,-2.085417,-8.518629,0.109063,8.070958,1.518905,4.870820,-3.728838,0.568717,5.276073,-7.156770,3.229587,-0.455764,-6.058685,1.874554,6.588995,8.930017,-4.908824,6.827370,-2.414129,-3.155177,-6.269005,-8.965607,5.278006,-6.610509,-2.153241,-1.991300,-1.120545,-7.079121,-1.076352,-6.339686,-4.019384,6.658635,5.448445,-7.193652,1.157537,-2.938503,5.323297,5.467542,-1.995927,6.425005,-5.545151,1.561335,5.868639,7.497992,8.335669,8.671159,-7.884306,-8.865455,-8.395875,0.605986,4.488802,5.816604,-4.596108,-4.625741,-6.522048,3.688695,3.913841,-6.817844,-8.785827,-9.511299,1.945815,2.940720,-3.936061,-9.088772,1.937238,9.051137,0.396535,4.021672,8.096049,-5.447780,7.212918,-9.427059,-5.343368,7.351667,8.017647,8.946160,-3.851471,-8.301303,-3.637186,8.523030,-8.940953,9.650757,4.935171,3.482912,-8.647067,1.951628,-3.220869,-8.040316,-6.427342,2.993985,8.487505,-2.414002,-1.751174,-6.908096,4.182441,-4.821333,-1.620105,1.788660,-7.950026,-6.858839,9.526802,-6.735255,-2.154830,-7.494613,4.462804,-3.052563,-9.838479,-4.659313,4.614192,-5.258472,-0.942929,-3.174558,-2.891370,-3.326101,-5.511860,4.666387,-0.472788,7.281720,-3.752442,1.516637,-6.515834,-1.097718,0.323758,6.604766,1.935338,9.951309,-7.056562,0.197653,-8.243214,6.313580,-8.067335,-2.421636,-7.802317,3.531366,7.227381,-9.523884,-5.436456,2.386402,9.741846,-5.336551,-6.531198,-8.434773,0.681587,5.083799,-0.261277,9.014894,3.856858,5.330367,7.744264,-7.549224,-2.523547,-9.410126,5.320289,-0.289118,-3.314062,1.444968,-3.752031,7.710760,8.287761,5.829281,8.972093,4.409778,-0.088749,7.516649,4.512281,8.452914,-5.932421,5.801421,1.490479,9.543682,-9.729255,-7.293474,-2.666850,9.573132,-8.016625,3.072509,3.682903,-5.603334,-3.139174,2.150951,8.229272,8.907021,8.230668,8.941272,-0.406249,-2.537637,2.643970,9.839695,8.299020,-9.461969,-9.466295,3.350920,-8.980968,8.897948,9.794584,-4.774941,9.600654,9.034169,-5.768212,2.050388,2.976219,-8.039181,-6.641274,-5.888430,-7.586587,3.967254,3.436011,-6.396099,-5.651715,-3.315814,-6.873048,-2.717624,-8.868255,-7.183604,-2.754854,1.300636,-3.046860,4.677140,5.658440,-0.960424,-5.895757,-0.766177,-7.896818,7.687724,1.390912,2.335878,-0.230715,8.463568,2.844476,-1.339782,-1.505231,9.676495,7.630525,1.283813,-7.502897,-6.857488,-6.673775,-6.871111,2.837317,3.048977,1.445658,-5.082444,9.242390,-3.259193,-8.158762,-2.253769,-1.206595,3.574791,-4.355125,9.386694,-7.408106,0.083827,-5.860441,7.458073,2.196249,-0.669164,4.958571,3.427918,8.892473,7.662474,-5.374534,-2.946009,9.367453,-9.169995,-8.724951,1.373365,2.681748,0.959313,-1.018208,9.968792,-1.750436,7.599746,-8.773141,-2.955991,-7.609987,5.801480,4.385808,-0.725237,1.199474,5.487829,-6.597607,-1.846845,9.239957,9.864566,1.506730,-5.155237,0.072762,5.632603,-6.965175,5.834148,-4.117278,2.787185,-0.422112,-7.728988,-1.590563,0.025747,-7.848306,-3.438305,-5.797010,-8.152846,-9.452074,5.202678,-1.703233,7.446590,-6.835264,1.608973,-0.450869,-5.508483,-8.540343,-1.757814,-2.606441,2.398004,-2.626636,5.072223,-0.639708,-7.694159,-4.544695,-3.090154,-9.927527,6.482728,-8.683609,2.549721,0.479104,7.292321,6.077651,-3.806040,8.379706,-7.996497,3.148851,-5.018074,8.913373,-5.182170,-7.194587,-8.047808,-1.376818,4.524730,6.076900,2.813899,8.375196,-8.566274,4.030234,-9.168464,6.770278,-2.621619,-9.430729,-6.341703,4.839658,4.384928,2.127349,-5.086963,0.905891,-8.428689,3.232095,1.211037,-0.562462,4.854751,-2.084133,-1.630082,-8.962875,-5.524093,-0.085809,9.940232,9.674926,6.768346,-3.525006,8.616561,-8.273913,-6.571361,2.283244,-0.716177,-9.315771,8.612461,8.579065,-5.391695,-4.930268,8.248181,1.956702,-7.864892,8.528158,9.644679,-0.729172,-6.973434,-5.696078,-4.813059,-6.962670,8.125194,-3.549452,-2.839007,-5.462519,8.590226,8.272115,3.023326,2.562254,-7.598264,-3.064976,8.612486,-0.296314,0.153347,-7.547314,-4.717788,-2.416594,3.027000,9.256610,-4.048774,-1.646530,-8.890511,-1.302213,-1.865543,-5.904412,0.392733,-2.282762,2.857532,-7.768188,4.345230,-3.936769,5.216824,2.133429,2.761640,-9.887987,2.662190,9.541723,0.694061,2.692977,-1.133386,-9.022094,-9.747451,-5.692232,4.991894,-5.297174,1.135024,-5.362041,8.148285,-2.689848,-1.262562,8.351098,8.925580,-1.671319,-7.750410,3.535228,6.255910,-2.339020,-8.210685,3.361461,7.558299,4.639304,-6.759200,-5.402425,8.962497,-1.719080,0.104101,1.948065,-3.447127,0.010245,-4.666265,6.771148,-9.523158,8.536479,-0.208564,-9.663973,2.217747,5.724115,-6.559990,7.243467,-2.735001,6.803159,8.290824,-0.260101,-6.977821,3.770525,-7.471204,-9.983201,-5.055832,-9.511176,-2.537845,6.208188,-4.065313,6.286269,-7.276704,-2.238837,-9.443864,-3.870878,6.089305,-4.571663,2.618029,-2.707519,-1.582954,-6.843343,-8.569853,-7.543990,-2.986853,-4.063641,-9.630523,6.005571,2.296763,0.861966,5.954091,7.197136,-2.576035,4.037312,2.279105,-4.326603,-8.259697,3.120801,1.082447,-3.404644,7.105799,-2.125172,-4.072611,-8.924538,3.550276,-2.409052,8.680979,6.460642,2.700338,5.001544,-8.899572,-8.556731,6.483513,-1.519434,1.471222,-9.455550,0.930433,-4.098974,-4.999422,0.887600,-4.817486,-6.366797,-8.235157,-2.791900,-7.944832,-6.289117,2.334465,-9.543975,-4.978408,2.468265,0.839713,-2.345373,-8.484165,-5.129243,1.315952,-7.649807,6.973554,-0.345599,2.428768,4.469051,-3.530748,-8.629939,8.106804,-5.249602,8.031208,7.593789,1.008938,-9.370973,0.022083,-3.495230,-3.509472,-3.865766,-7.253743,7.143882,0.332371,1.587453,3.782359,7.607483,-5.612246,-3.803324,3.525934,-7.178729,-8.101795,-5.960272,-1.160609,-3.058546,-0.694914,-7.682082,1.255659,-2.136983,5.691863,1.250700,3.059979,8.634647,-5.545856,-5.822561,7.378787,5.356114,8.310884,0.480206,-0.688700,-9.534597,8.354742,1.358292,4.163048,9.403948,-1.242660,3.779419,-6.460004,7.596493,-3.625951,-5.904284,0.709896,5.755527,-6.599982,-9.048159,3.049196,0.927988,2.329143,5.541845,-0.208163,0.872468,1.119756,-8.179708,5.879878,7.932392,1.801092,-7.481385,0.690334,4.543129,-7.427120,-9.862655,1.914710,-9.750549,1.758966,3.217604,5.209276,-4.692349,6.343628,-8.603968,-9.443582,-7.391615,8.241690,-2.791833,7.827182,-7.342758,7.895677,9.943180,-4.507512,-5.641693,6.107206,7.799708,-9.724707,-9.692397,4.393407,4.637808,-8.194891,8.759989,-2.325714,-9.758624,-6.806631,9.905598,5.724180,-7.553997,4.105278,0.589687,-7.333477,7.044052,-9.796571,-8.877916,-7.387702,-3.239713,3.716655,-5.679854,1.713372,2.551940,-7.669685,-1.586655,9.613198,4.532297,0.587709,-3.118611,-3.517117,-0.717610,6.771557,-6.754539,-9.885971,-5.343372,-6.152426,3.984271,6.720796,4.297405,-1.345794,3.258844,-5.845075,-4.968263,-6.285375,9.236785,-5.902421,9.863335,-6.992827,8.010752,-5.058814,3.102890,-6.610036,0.206484,7.126269,7.799167,-8.647979,-7.286884,-5.712218,-1.102159,5.021261,0.992000,2.044396,9.697320,-9.916680,2.284317,-0.786314,8.100744,2.720354,-7.716310,-6.953495,-6.171490,-6.809075,4.977631,7.183794,3.726899,-9.258122,-0.596635,-6.669220,0.775348,-3.461709,8.311873,9.054635,-8.428768,5.676152,-9.117044,-8.580708,-6.530268,9.084668,2.905618,1.130964,8.207953,4.849463,-0.813774,2.107829,-3.897064,-7.691770,-2.718108,1.719052,-9.350170,4.553617,-0.724349,-8.750819,-0.014535,-9.970762,-5.596710,9.423730,1.241104,-8.115215,-8.678457,-2.317364,2.517323,-0.727852,-8.635028,-0.375300,6.002953,0.332268,-5.203817,-1.375975,4.216520,-7.215716,2.964648,3.670991,7.302762,-4.617482,8.108205,-7.420407,7.326025,-4.772647,-6.524553,-6.748433,-4.271829,3.279891,1.480022,-5.009311,2.293993,5.355065,-8.329953,3.637108,-2.088207,9.608396,-7.035792,-6.897261,-5.653658,-3.765536,-8.123687,-1.194591,-1.199588,7.255851,-0.415896,3.530297,-4.594181,-0.110916,9.255202,-9.005570,9.201347,-1.893496,-2.680628,5.460395,5.962029,5.700866], dtype = "float32")#candidate|14494|(975,)|const|float32
call_14492 = relay.TupleGetItem(func_2115_call(relay.reshape(var_14493.astype('float32'), [3, 16, 4]), relay.reshape(const_14494.astype('float32'), [975,]), ), 2)
call_14495 = relay.TupleGetItem(func_2118_call(relay.reshape(var_14493.astype('float32'), [3, 16, 4]), relay.reshape(const_14494.astype('float32'), [975,]), ), 2)
uop_14502 = relay.acos(var_14493.astype('float64')) # shape=(96, 2)
output = relay.Tuple([uop_14488,call_14492,const_14494,uop_14502,])
output2 = relay.Tuple([uop_14490,call_14495,const_14494,uop_14502,])
func_14506 = relay.Function([var_14493,], output)
mod['func_14506'] = func_14506
mod = relay.transform.InferType()(mod)
var_14507 = relay.var("var_14507", dtype = "float32", shape = (96, 2))#candidate|14507|(96, 2)|var|float32
output = func_14506(var_14507)
func_14508 = relay.Function([var_14507], output)
mutated_mod['func_14508'] = func_14508
mutated_mod = relay.transform.InferType()(mutated_mod)
const_14533 = relay.const([[[-1.030421,9.724426,-4.002190,2.701299],[1.468830,-4.189915,-7.955141,0.328862],[-5.981564,9.203147,7.501897,-4.260142],[5.029681,-9.712439,-4.583441,-9.683111],[-6.781924,3.822818,5.153965,3.621397],[7.914344,8.641023,-0.800157,-4.046281],[-6.533544,9.146173,9.635206,3.596997],[-1.780839,-2.165041,9.081398,0.497444],[2.263455,-1.998687,0.652129,2.114697],[9.044027,-8.395582,-2.217098,-8.057987],[-3.292136,-0.087315,8.475207,6.821817],[-8.985507,-8.410465,-1.287440,3.497995],[-2.177050,-9.986477,6.841831,-8.567608],[-5.926440,1.872655,2.247732,7.596149],[0.515626,-6.717706,2.737263,-1.357931]],[[6.747329,9.335380,1.085800,4.704895],[-4.243808,3.713497,-0.526568,-9.175335],[0.878833,1.298520,0.052497,-6.143951],[-4.254867,4.940997,-7.156119,9.995933],[2.377321,1.624005,-1.571962,-2.520170],[-1.093642,-4.736858,-6.906626,8.262877],[-2.949959,-2.154670,1.800062,1.878222],[2.208125,2.417059,-5.034119,-5.627679],[7.920340,-9.974038,-8.311724,-4.693211],[4.021200,7.609601,5.491473,8.849449],[0.476160,3.429964,-4.756072,8.318468],[-8.499448,-5.870858,1.207622,-4.914950],[-1.056460,-1.335566,8.439066,-3.894841],[-7.489976,-9.330551,-1.585954,9.550677],[-0.076098,9.208929,7.327076,-1.465222]],[[3.405247,7.204062,2.970901,-6.356061],[-3.543894,3.430759,1.024124,-7.676592],[5.312574,-8.032269,-8.560549,-7.513548],[-3.151057,-1.594816,-1.037240,1.185842],[9.168760,-2.562831,-8.047716,-6.329151],[-0.514662,1.292233,0.742131,8.862754],[-1.040821,7.627038,4.269165,3.160801],[4.086622,-9.962384,1.560091,1.086423],[-8.204040,5.815885,-9.919536,3.949755],[3.574942,9.848508,7.634871,-5.914666],[-7.545410,-7.323182,6.340715,4.688873],[5.160082,-8.203145,-5.388380,9.556468],[4.200284,8.409846,5.507860,-5.350966],[4.267389,1.283702,-7.137117,9.342122],[1.457214,6.889109,5.019202,0.075324]],[[-5.715936,6.775137,-0.491959,8.274766],[-2.680144,3.695069,5.021745,-0.142614],[0.275048,4.715651,9.765155,-6.583819],[2.626242,8.252607,2.901160,6.559660],[-0.379238,-8.532628,-8.246716,2.495339],[-5.229053,-1.193415,-7.430912,5.723970],[-7.625998,-7.046837,9.800181,2.431616],[-0.098499,3.979662,6.349224,4.510319],[-0.809386,-7.456698,2.957921,4.459726],[2.781775,9.061526,-4.132545,5.646946],[-0.103289,8.853585,2.604288,-8.440197],[4.563058,9.255048,-3.495294,9.213664],[-5.588998,8.809965,6.976847,0.177039],[-5.868723,-8.777598,6.062291,-8.840899],[7.650221,1.897342,-2.827558,-9.872256]],[[-9.275767,-0.164990,-0.383616,1.985081],[-4.385222,-7.987372,4.405270,-6.153300],[0.367896,-0.217633,-4.149946,-5.001443],[-9.987065,-7.695110,9.693034,7.931269],[-5.046641,-1.128070,8.121714,3.795913],[4.155325,2.749747,-8.484445,-5.251145],[-8.282006,-0.414457,9.737610,3.157005],[2.319529,-7.111301,-5.559928,-8.221810],[-9.007669,-7.623873,-8.585021,8.866609],[4.272227,-6.020107,-7.177212,6.064267],[8.184001,8.895301,-2.451863,8.185094],[8.286268,-6.205922,4.680296,-0.263005],[-3.008780,1.052343,9.606890,-0.489189],[7.457866,-2.102394,0.424678,-8.394084],[0.933942,-8.333232,-6.022997,4.479362]],[[8.529213,-4.595209,-5.912789,-2.131705],[7.382801,4.449655,-3.483239,4.371972],[-3.217261,0.896664,-7.681421,7.492234],[-0.522944,4.737044,4.334083,-7.118153],[4.190179,1.219909,7.445900,-7.969149],[0.039102,4.893674,6.591730,7.126123],[-4.276928,9.772131,-8.529234,1.898066],[-3.976087,-6.043918,4.143675,3.906970],[7.915816,7.632803,-0.706631,5.641351],[9.843580,-4.358648,6.735668,2.418580],[-9.102476,-5.572389,9.661120,0.723174],[5.289114,9.719284,-0.444570,4.855611],[5.718918,8.696479,-5.749181,4.306359],[2.847505,-7.062015,5.054886,5.576300],[-7.723895,-8.439373,8.684091,-0.765964]]], dtype = "float32")#candidate|14533|(6, 15, 4)|const|float32
uop_14534 = relay.cosh(const_14533.astype('float32')) # shape=(6, 15, 4)
output = uop_14534
output2 = uop_14534
func_14560 = relay.Function([], output)
mod['func_14560'] = func_14560
mod = relay.transform.InferType()(mod)
mutated_mod['func_14560'] = func_14560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14560_call = mutated_mod.get_global_var('func_14560')
call_14561 = func_14560_call()
output = call_14561
func_14562 = relay.Function([], output)
mutated_mod['func_14562'] = func_14562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14241_call = mod.get_global_var('func_14241')
func_14242_call = mutated_mod.get_global_var('func_14242')
call_14578 = relay.TupleGetItem(func_14241_call(), 0)
call_14579 = relay.TupleGetItem(func_14242_call(), 0)
func_10161_call = mod.get_global_var('func_10161')
func_10164_call = mutated_mod.get_global_var('func_10164')
var_14604 = relay.var("var_14604", dtype = "float64", shape = (8, 144))#candidate|14604|(8, 144)|var|float64
call_14603 = relay.TupleGetItem(func_10161_call(relay.reshape(var_14604.astype('float64'), [6, 12, 16]), relay.reshape(var_14604.astype('float64'), [6, 12, 16]), ), 0)
call_14605 = relay.TupleGetItem(func_10164_call(relay.reshape(var_14604.astype('float64'), [6, 12, 16]), relay.reshape(var_14604.astype('float64'), [6, 12, 16]), ), 0)
var_14610 = relay.var("var_14610", dtype = "float64", shape = (8, 144))#candidate|14610|(8, 144)|var|float64
bop_14611 = relay.mod(var_14604.astype('float64'), relay.reshape(var_14610.astype('float64'), relay.shape_of(var_14604))) # shape=(8, 144)
uop_14615 = relay.tan(call_14603.astype('float64')) # shape=(6, 12, 16)
uop_14617 = relay.tan(call_14605.astype('float64')) # shape=(6, 12, 16)
output = relay.Tuple([call_14578,bop_14611,uop_14615,])
output2 = relay.Tuple([call_14579,bop_14611,uop_14617,])
func_14621 = relay.Function([var_14604,var_14610,], output)
mod['func_14621'] = func_14621
mod = relay.transform.InferType()(mod)
mutated_mod['func_14621'] = func_14621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14621_call = mutated_mod.get_global_var('func_14621')
var_14623 = relay.var("var_14623", dtype = "float64", shape = (8, 144))#candidate|14623|(8, 144)|var|float64
var_14624 = relay.var("var_14624", dtype = "float64", shape = (8, 144))#candidate|14624|(8, 144)|var|float64
call_14622 = func_14621_call(var_14623,var_14624,)
output = call_14622
func_14625 = relay.Function([var_14623,var_14624,], output)
mutated_mod['func_14625'] = func_14625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14241_call = mod.get_global_var('func_14241')
func_14242_call = mutated_mod.get_global_var('func_14242')
call_14671 = relay.TupleGetItem(func_14241_call(), 0)
call_14672 = relay.TupleGetItem(func_14242_call(), 0)
func_12009_call = mod.get_global_var('func_12009')
func_12012_call = mutated_mod.get_global_var('func_12012')
var_14683 = relay.var("var_14683", dtype = "float32", shape = (468,))#candidate|14683|(468,)|var|float32
call_14682 = relay.TupleGetItem(func_12009_call(relay.reshape(var_14683.astype('float32'), [4, 9, 13])), 0)
call_14684 = relay.TupleGetItem(func_12012_call(relay.reshape(var_14683.astype('float32'), [4, 9, 13])), 0)
output = relay.Tuple([call_14671,call_14682,var_14683,])
output2 = relay.Tuple([call_14672,call_14684,var_14683,])
func_14687 = relay.Function([var_14683,], output)
mod['func_14687'] = func_14687
mod = relay.transform.InferType()(mod)
var_14688 = relay.var("var_14688", dtype = "float32", shape = (468,))#candidate|14688|(468,)|var|float32
output = func_14687(var_14688)
func_14689 = relay.Function([var_14688], output)
mutated_mod['func_14689'] = func_14689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14151_call = mod.get_global_var('func_14151')
func_14153_call = mutated_mod.get_global_var('func_14153')
call_14695 = relay.TupleGetItem(func_14151_call(), 0)
call_14696 = relay.TupleGetItem(func_14153_call(), 0)
var_14706 = relay.var("var_14706", dtype = "float64", shape = (12, 6, 11))#candidate|14706|(12, 6, 11)|var|float64
bop_14707 = relay.minimum(call_14695.astype('uint16'), relay.reshape(var_14706.astype('uint16'), relay.shape_of(call_14695))) # shape=(12, 6, 11)
bop_14710 = relay.minimum(call_14696.astype('uint16'), relay.reshape(var_14706.astype('uint16'), relay.shape_of(call_14696))) # shape=(12, 6, 11)
func_7592_call = mod.get_global_var('func_7592')
func_7596_call = mutated_mod.get_global_var('func_7596')
const_14714 = relay.const([[-4],[-7],[-6],[2],[-3],[-5],[-7],[7],[3],[3],[7],[1],[5],[-6],[3],[-9],[9],[-3],[-8],[-2],[-6],[-1],[-6],[-10],[-6],[-8],[-5],[1],[-4],[-4],[-8],[-3],[-8],[3],[1],[-6],[10],[9],[-8],[8],[4],[-8],[-8],[10],[-7],[8],[7],[4],[6],[-3],[3],[-6],[-9],[-1],[-6],[2],[7],[-10],[9],[7],[-4],[1],[6],[7],[3],[1],[-9],[8],[-3],[-4],[2],[-8],[6],[-3],[10],[2],[7],[-5],[9],[7],[4],[-9],[-6],[-1],[-10],[6],[3],[-10],[-6],[5],[-5],[9],[-10],[-6],[-10],[2],[-2],[7],[10],[5],[-4],[-9],[-8],[5],[3],[9],[-5],[-1],[5],[-6],[10],[-7],[1],[-10],[-1],[-10],[-7],[2],[-9],[9],[-7],[10],[-7],[8],[8],[-6],[-2],[-3],[-8],[-3],[-8],[-4],[3],[2],[2],[-3],[-10],[-2],[-4],[10],[6],[10],[-3],[-2],[-6],[2],[9],[10],[-1],[-5],[-4],[6],[3],[-2],[2],[-9],[-1],[8],[-4],[5],[-7],[-3],[-2],[-10],[5],[-9],[-6],[-4],[5],[-6],[-1],[-3],[5],[-6],[-2],[-8],[-7],[-5],[6],[-3]], dtype = "uint8")#candidate|14714|(180, 1)|const|uint8
const_14715 = relay.const([-3.494540,-0.057988,8.062391,0.292355,7.768647,4.879600,-2.115169,-6.842205,9.320928,-2.936498,8.580607,9.020536,0.584432,-3.516344,6.795482,1.564925,8.714768,-8.254044,-1.975160,6.569388,-7.305561,0.859925,-3.040041,-1.990907,-0.134817,9.897437,-2.034756,7.419554,3.232663,-2.549940,-3.311407,-0.167358,7.034649,-3.928703,-6.298666,-3.196272,1.115184,6.553194,9.305615,5.338030,4.762386,-4.203446,5.321410,1.025726,2.279143,-5.142346,0.146604,1.844844,1.456392,2.558390,0.799951,-1.822630,1.612892,3.972862,-6.584035,-5.658780,7.943109,4.439244,-3.225588,4.342579,6.161958,8.132401,-8.689287,1.492845,1.008281,-0.729898,-5.881089,7.788444,-9.767463,9.129716,8.544820,-8.010970,-5.601092,2.445497,9.395206,-3.379456,-7.657648,7.948490,-7.501468,5.968162,4.412882,9.775418,-7.188587,7.301734,8.256719,0.979030,6.163986,9.332194,-9.162818,-5.014523,-0.218915,-9.692225,2.802208,7.104331,-4.523025,9.624416,-8.900184,-1.431597,9.454707,-7.356947,-0.040346,9.889247,8.966796,5.043207,2.852894,1.135088,-5.776907,3.805338,-2.389899,1.320909,5.097393,-7.917632,7.163696,-9.707472,7.658849,7.280369,0.223588,1.002121,-7.550439,-1.061949,-6.006214,0.203125,5.485849,-0.743235,1.150108,-5.416451,-5.446022,2.787732,6.378030,-8.912008,-6.459151,-8.030083,-2.519113,-2.263475,-2.078465,4.753380,3.029710,1.631521,3.893526,-8.327314,-0.901030,8.008166,8.571096,-8.188504,-8.220767,6.035599,4.002078,-2.709274,6.295059,-9.188789,1.187534,4.919611,-1.870849,8.052996,-8.567414,-8.828593,2.576660,-7.502078,-2.577167,6.773640,2.806244,8.445297,0.471616,7.844379,4.227205,-7.838660,1.064075,8.388208,7.939465,4.235337,-0.436152,-6.410836,2.957018,-5.538924,3.367749,-0.454121,6.459188,4.094463,-2.527628,3.942828,-0.035295,-4.847002,7.751807,9.765671,9.640404,8.219742,9.595001,1.832954,-8.256975,-0.323392,5.425799,-2.611332,6.849761,4.737860,-9.035785,1.408286,2.757347,-8.687019,4.035674,6.935640,-0.703922,-9.228289,-2.390866,-9.859735,4.039864,-0.661198,-8.006623,1.652300,0.880255,3.374140,-0.236501,-9.078044,-3.227503,-7.904382,7.880703,-0.831080,-7.256681,9.347901,-7.290114,2.743185,-7.516629,6.401044,1.333332,-7.882740,1.173275,-0.311873,-2.947356,9.406068,-9.457230,-2.246838,2.526117,4.968797,1.982330,-5.099826,7.687027,-7.075848,-1.141578,-4.786897,-7.510274,-0.515292,-4.498047,5.170399,7.705560,6.462043,8.431515,0.268867,4.840247,-8.238489,5.537917,-9.640072,0.534789,1.499640,-3.349604,5.361631,-6.482172,1.140560,-0.499331,-2.100170,5.876664,5.619935,8.760848,-5.093891,-3.521923,-0.866367,2.132037,-6.660951,8.188411,-0.738520,8.693122,-0.051607,7.589160,-1.377748,2.197490,-6.632561,-0.174806,9.673737,-1.598538,-3.981588,-8.740673,6.626114], dtype = "float64")#candidate|14715|(280,)|const|float64
call_14713 = relay.TupleGetItem(func_7592_call(relay.reshape(const_14714.astype('uint8'), [2, 9, 10]), relay.reshape(const_14715.astype('float64'), [280,]), ), 1)
call_14716 = relay.TupleGetItem(func_7596_call(relay.reshape(const_14714.astype('uint8'), [2, 9, 10]), relay.reshape(const_14715.astype('float64'), [280,]), ), 1)
output = relay.Tuple([bop_14707,call_14713,const_14714,const_14715,])
output2 = relay.Tuple([bop_14710,call_14716,const_14714,const_14715,])
func_14723 = relay.Function([var_14706,], output)
mod['func_14723'] = func_14723
mod = relay.transform.InferType()(mod)
var_14724 = relay.var("var_14724", dtype = "float64", shape = (12, 6, 11))#candidate|14724|(12, 6, 11)|var|float64
output = func_14723(var_14724)
func_14725 = relay.Function([var_14724], output)
mutated_mod['func_14725'] = func_14725
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14763 = relay.var("var_14763", dtype = "float32", shape = (12, 16, 12))#candidate|14763|(12, 16, 12)|var|float32
uop_14764 = relay.cosh(var_14763.astype('float32')) # shape=(12, 16, 12)
func_12987_call = mod.get_global_var('func_12987')
func_12988_call = mutated_mod.get_global_var('func_12988')
call_14777 = relay.TupleGetItem(func_12987_call(), 0)
call_14778 = relay.TupleGetItem(func_12988_call(), 0)
output = relay.Tuple([uop_14764,call_14777,])
output2 = relay.Tuple([uop_14764,call_14778,])
func_14787 = relay.Function([var_14763,], output)
mod['func_14787'] = func_14787
mod = relay.transform.InferType()(mod)
mutated_mod['func_14787'] = func_14787
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14788 = relay.var("var_14788", dtype = "float32", shape = (12, 16, 12))#candidate|14788|(12, 16, 12)|var|float32
func_14787_call = mutated_mod.get_global_var('func_14787')
call_14789 = func_14787_call(var_14788)
output = call_14789
func_14790 = relay.Function([var_14788], output)
mutated_mod['func_14790'] = func_14790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13360_call = mod.get_global_var('func_13360')
func_13362_call = mutated_mod.get_global_var('func_13362')
call_14848 = relay.TupleGetItem(func_13360_call(), 0)
call_14849 = relay.TupleGetItem(func_13362_call(), 0)
output = call_14848
output2 = call_14849
func_14855 = relay.Function([], output)
mod['func_14855'] = func_14855
mod = relay.transform.InferType()(mod)
mutated_mod['func_14855'] = func_14855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14855_call = mutated_mod.get_global_var('func_14855')
call_14856 = func_14855_call()
output = call_14856
func_14857 = relay.Function([], output)
mutated_mod['func_14857'] = func_14857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13780_call = mod.get_global_var('func_13780')
func_13781_call = mutated_mod.get_global_var('func_13781')
call_14887 = func_13780_call()
call_14888 = func_13780_call()
func_14400_call = mod.get_global_var('func_14400')
func_14401_call = mutated_mod.get_global_var('func_14401')
call_14889 = func_14400_call()
call_14890 = func_14400_call()
func_10161_call = mod.get_global_var('func_10161')
func_10164_call = mutated_mod.get_global_var('func_10164')
var_14901 = relay.var("var_14901", dtype = "float64", shape = (1152,))#candidate|14901|(1152,)|var|float64
call_14900 = relay.TupleGetItem(func_10161_call(relay.reshape(var_14901.astype('float64'), [6, 12, 16]), relay.reshape(var_14901.astype('float64'), [6, 12, 16]), ), 0)
call_14902 = relay.TupleGetItem(func_10164_call(relay.reshape(var_14901.astype('float64'), [6, 12, 16]), relay.reshape(var_14901.astype('float64'), [6, 12, 16]), ), 0)
func_8904_call = mod.get_global_var('func_8904')
func_8906_call = mutated_mod.get_global_var('func_8906')
const_14913 = relay.const([[7.268383,9.919502,-2.532474,-2.768131,-3.046646,6.810376,-0.946273,3.722634,-9.701580,1.405021,-0.256968,-0.370558,-6.271101,-4.205144,-2.019853,-2.148884,4.518400,-9.641293,9.586342,-7.091523],[3.901985,-4.175138,2.914529,3.500208,3.596824,-0.207733,-3.595425,-2.918299,1.675517,1.984631,-3.482248,1.307606,4.226502,3.638571,1.096110,-4.125509,2.287194,-4.195035,-3.546722,0.068630],[-2.651292,-4.099783,-0.027428,1.635388,5.955171,9.138792,-3.002243,4.485655,2.101319,-7.252158,2.408315,2.500946,7.611710,5.467065,2.895279,-1.279102,4.164499,-5.692339,4.900749,4.925430],[-8.139365,-3.897727,6.214406,-1.786101,9.911379,6.368508,-3.548785,9.222144,-2.758766,6.066927,3.827918,8.550299,-2.567323,3.070998,-4.241049,-9.964758,2.570884,4.495811,9.936131,5.693366],[4.234357,4.536004,-3.755786,2.692090,9.133299,-4.616249,-9.480286,7.869665,-8.633549,-2.885283,2.856458,4.588508,-8.618372,-1.557132,4.849703,-8.978552,-8.631607,-3.326950,-3.470755,-4.517399],[-7.753997,2.842967,-8.464399,-6.473571,8.943206,4.938305,7.199559,4.497504,-1.374103,5.208386,-8.526872,-0.718090,5.106246,1.448488,-4.668047,-2.545564,-8.907102,-8.996929,-5.459063,2.652077],[0.996542,5.181405,-2.794843,-2.722774,-4.676123,-3.381854,4.533919,8.614373,8.221405,2.146915,-8.416586,-0.992526,9.025861,-9.171663,3.326300,7.478448,-0.881675,-4.563447,6.540734,8.587450],[-6.447806,-1.909054,-1.641655,9.760772,-6.989501,-7.746052,-8.239700,-6.283538,4.544393,9.115687,-4.451191,0.327838,2.936955,4.460795,3.769216,-2.910279,-9.144599,3.175825,3.271533,-9.723049],[1.505573,-8.992766,-4.334918,5.811293,8.242722,-7.003866,3.127287,1.711996,7.197815,-5.643444,2.743315,3.320870,1.595587,7.399142,4.093074,6.046838,-2.775588,-6.116512,-3.188735,-9.768457],[-5.862788,6.086356,-6.714791,1.337872,-8.895288,-7.838973,-8.384405,8.107012,7.538660,-6.443273,4.772461,7.902710,-6.843834,-9.533190,-3.341121,-5.367799,4.938036,-3.187452,-0.670856,-7.667626],[4.118389,3.836979,-0.147356,-9.224464,6.026665,-9.459617,-8.846433,-5.510836,9.166013,9.275885,5.096584,-1.934764,7.239237,-1.199942,-8.203549,-2.503792,-5.762758,-6.031659,7.960093,-9.681571],[7.772523,0.299467,-2.352376,-5.753900,-2.052834,5.654174,-5.476694,-0.215710,0.393870,4.393690,6.466953,1.904699,6.322511,-1.615762,-5.346859,5.163558,2.796584,3.471217,-7.930834,1.802864],[6.834770,-9.071643,4.539282,-2.620719,-6.636069,-3.790208,9.191988,3.887118,4.231728,7.600501,-2.700970,-9.741190,1.572500,8.502021,5.408962,-8.090237,-6.966771,-6.949646,-2.298945,-9.789159],[4.876158,-8.144325,-2.344587,7.736365,-4.984565,-5.668404,-0.617090,-9.023534,-9.823502,2.287148,9.087456,2.477188,6.945805,5.922606,-7.193381,-4.044854,-0.349472,-2.996713,-2.626746,2.645025],[8.224169,6.120729,-9.826643,4.002323,9.430531,-3.674796,5.731619,-0.330986,-6.845266,-9.425952,5.358593,-3.104992,1.684110,1.994354,-6.307049,-1.877783,-8.121982,1.851248,-7.985872,9.985873],[-3.059047,-8.988294,1.232007,-3.313840,-1.333929,-5.489116,0.731998,3.634490,-4.249276,-7.550792,2.590061,-5.957023,-3.741687,-5.257052,-5.514872,-7.921329,-7.107599,-2.437105,-1.646963,3.581169],[8.940115,-9.118863,-0.829818,-8.880830,-5.000958,5.988918,1.221790,8.409846,-0.096478,-3.554022,-1.398591,7.487266,9.840655,-8.398432,-1.466512,-0.927022,-9.668875,-3.521568,4.019425,8.189077],[3.054653,7.400517,-4.019133,-1.769026,0.163565,4.045101,3.911431,-6.894403,7.331411,-2.166247,-8.662889,7.303041,-7.868398,5.807690,-0.116402,9.137425,8.237914,1.719596,-1.089939,-6.832785],[-2.371597,3.357167,-5.384473,3.119445,-9.082385,2.975495,-5.395127,1.718874,-6.779257,-0.410730,8.536385,-1.069808,5.583437,-3.302909,0.342793,3.925661,4.814272,-4.802201,-2.309985,9.785887],[6.006919,2.827892,7.785698,-1.699019,9.257723,3.181359,9.302434,1.402194,0.385560,-4.441397,2.738265,-5.149682,-3.601667,-0.165173,-1.893652,7.596844,4.336028,-0.673177,-8.009427,-3.238736],[1.387547,-1.501416,-5.083011,8.902877,-9.627128,-3.620940,4.575337,-6.084853,4.225227,-8.377123,-7.536211,-5.973468,-4.225671,-8.953321,5.107431,-9.013345,-1.906187,3.774146,8.160880,-7.803249],[-5.933856,5.984782,-5.190317,4.009174,-0.175406,3.467692,-8.998200,-3.981396,-9.970566,5.753497,-5.951246,4.192382,-6.264742,7.454471,8.434411,8.702976,-1.932888,-9.630312,-0.483636,2.042985],[9.873486,6.060081,-7.225554,6.440418,1.818766,-0.010326,-4.806630,-6.958718,8.656571,-0.551936,-4.510056,-5.857878,-1.189240,3.179269,1.055719,-8.657693,6.029095,-8.183117,7.916358,1.067790],[-2.714548,-8.940025,1.719930,4.434945,-4.364473,2.494971,-7.413923,-6.543297,-4.837157,9.149439,-5.466627,3.170316,-2.057557,2.231286,5.429175,-6.221206,-9.742293,-2.619161,2.441029,-9.367436],[-8.178021,-9.714011,-3.777026,9.540462,-4.556704,-5.368648,-6.827674,7.489579,2.483817,2.758082,3.436793,-7.481740,-8.117701,9.537300,-1.833650,-1.540504,1.474344,8.399982,5.783483,6.970236],[-9.578113,-6.174883,5.956245,8.449462,-2.205317,8.341016,-3.798215,5.900418,-9.611280,-7.564527,8.511120,1.537586,-7.925807,-6.454048,-2.941626,6.144329,0.022688,2.527735,5.078823,8.175701],[9.684571,2.152097,-5.576880,8.560355,7.509349,3.386983,-7.689009,-3.771993,-2.472586,-3.471532,-9.256310,4.582607,4.680111,-9.862557,4.379900,-9.081849,-1.195615,-8.900639,-9.111610,8.443762],[9.876835,-1.766580,-8.411786,-2.387457,2.435096,2.649331,0.863529,9.537945,1.922775,7.632430,5.219518,-4.359694,-6.413768,-7.955544,-8.989158,-7.355805,5.798235,2.280681,8.922191,-1.030667],[-2.510253,-7.420263,-9.049273,-9.504100,4.764318,-7.951511,1.070348,-7.738313,5.307639,-5.748095,5.016826,9.456085,-8.646505,-0.966132,4.974365,-5.877576,-5.373452,4.551406,9.081280,-9.430026],[8.985133,3.492472,2.232283,-5.851801,0.548069,-0.517975,-1.429254,7.600658,-3.861705,-0.530115,-0.891400,5.367614,-6.302382,2.091132,-3.151351,-7.902173,-3.080008,-6.541758,-8.379119,-7.914884],[-1.210553,-0.500947,-9.786486,2.637856,4.185033,-6.573527,-0.946263,-7.812917,-9.810439,-8.264088,0.592214,1.818300,7.580839,-0.679501,-1.575183,7.087305,1.278889,1.210355,6.203801,7.259132],[4.722499,-1.544256,0.572553,-4.419526,-8.616727,8.163718,0.510969,7.197006,-5.015391,-7.515333,-3.470544,0.196143,6.736015,3.336842,1.836280,7.643014,0.460586,5.330566,-9.992751,-8.512755],[-9.848994,9.248493,-8.713255,-2.259370,-0.670979,-1.734178,-1.439435,-3.135035,-6.366546,-1.366827,-9.841194,-8.042210,7.518828,2.910347,2.918838,-4.972000,0.237215,-7.138093,-4.603448,-4.425691],[3.369117,1.430003,6.146657,-8.249118,-0.300476,5.390777,-8.540804,-1.248992,8.302870,-7.395390,2.276294,4.153358,-2.144392,3.946641,-8.861305,5.614265,-1.767494,-1.120950,-3.169281,2.875157],[6.586590,-9.773830,7.502203,-1.944843,-4.331263,8.257182,8.983975,-2.799667,-9.018414,0.642534,7.666449,5.453496,6.752304,2.773618,-4.586804,-0.787037,-9.775264,2.868325,3.378066,-6.993951],[-9.439053,-6.484259,-7.117347,3.376466,-3.582198,-3.584753,5.604366,6.624063,6.563452,0.347568,9.638611,6.943771,-3.332032,4.402222,-9.080343,6.264165,-2.204861,3.054692,-8.590019,3.937338],[5.491215,-4.973515,9.176237,8.541425,6.922908,-1.156621,6.020300,-8.214360,5.323345,8.181264,9.453059,-0.873170,-6.709266,5.603987,8.061561,5.688535,-3.089559,2.564595,3.959198,-2.223827],[3.913822,-0.875190,-9.916963,-2.535942,-5.362022,-5.077459,-7.039700,0.167224,-7.479835,8.953757,-1.365021,-4.199666,5.106779,-1.764713,-8.875991,7.511195,-6.478190,-4.107508,-3.226034,-0.390578],[0.266066,-0.415589,3.348034,-7.374522,-3.763824,3.854921,6.245475,3.130542,-8.773488,8.111159,-8.830852,-7.686924,-2.517249,-1.140930,-8.417038,-6.174233,6.761321,0.909421,-2.565405,-9.748285],[-1.844672,9.954394,2.913425,-8.696588,5.549069,-5.133168,-6.658190,-8.304264,-2.667369,4.342544,6.277904,-4.706775,-8.839730,2.464139,4.901124,-6.802332,-2.739182,5.416845,-8.822089,7.976411],[-5.941944,-0.793161,-2.559945,9.545764,3.014938,2.137412,-0.717188,9.087117,-6.671863,-4.379075,-0.419009,0.429561,-8.718695,-0.032894,-6.857387,-3.630532,8.227373,4.381975,6.470172,-2.580718],[1.662503,2.070992,5.488120,-9.503555,-7.105405,-7.557092,0.905257,5.419011,-1.876145,3.163791,7.968342,2.098724,-2.266997,-7.414923,-3.221928,-2.099142,9.671506,2.166158,-5.665507,-8.638248],[-9.864793,3.196263,-5.818383,-0.064008,-1.853049,2.904910,6.147126,-1.060889,8.148488,-1.760957,-4.466735,2.771174,-9.315006,-6.625449,-6.948707,2.353796,1.953638,7.671331,0.810930,1.014901],[2.362095,4.337038,9.913813,-1.835607,5.549505,-2.291731,0.908224,4.084776,5.782125,-9.025879,-8.856102,-5.651172,-9.702067,9.128077,4.588851,2.583834,4.700012,-8.000735,-8.767491,3.100994],[2.246810,1.571430,0.147040,-0.907920,9.093148,-5.696538,7.636540,6.687307,-8.026864,6.211146,8.529580,-3.383026,-7.626734,-8.853419,1.541407,-1.722593,8.898795,8.963116,-6.287386,5.616021],[-8.966921,0.623408,0.857520,8.487296,8.921695,0.465107,4.215240,8.193182,-5.579977,9.756341,1.595822,-6.302284,8.260591,9.861578,-5.303160,2.537541,-8.672020,-8.257601,-3.079308,-4.157190],[-0.093125,-8.522650,4.254025,1.709658,2.660733,-3.756949,-5.138971,-5.337189,-9.206282,6.689872,-3.535367,-9.373550,4.322663,-1.996085,-8.598640,5.628491,0.132299,1.269264,6.510633,-7.185524],[3.468264,1.578098,-0.579843,5.575516,1.216016,6.260265,-3.031420,5.094247,-0.323309,1.222018,-4.289830,4.023425,-0.305750,-8.358331,-9.206627,4.773354,4.446690,0.326823,-0.771391,3.701721],[-2.456121,3.745435,-3.248240,-5.128411,4.677662,9.633828,4.107944,5.899197,8.841850,4.610478,-9.939977,3.869002,-5.783237,1.818785,-9.879648,-4.044278,9.764550,4.322125,-2.752977,-8.717904],[5.321600,7.895719,8.462638,-8.149724,0.719964,-6.341751,-8.801802,9.807591,-0.588656,0.135742,9.950643,7.417276,-0.246304,-5.487214,8.759368,-0.994946,0.649734,2.030049,-7.740310,2.993794],[7.930631,5.488593,-9.782185,-5.353459,-0.876500,4.419988,-8.922242,-1.950185,6.845367,1.415780,-5.427492,8.142023,-1.182232,-4.072617,-1.983906,-0.265994,5.429417,-0.672627,-1.282004,-7.105805],[-8.329507,9.215899,1.023887,0.755215,-4.298884,4.897949,-1.822472,-7.998026,4.835118,2.886524,6.678767,2.642908,-9.657396,-2.939629,3.923710,2.580608,-1.310563,-5.194576,-4.520854,-0.345679],[-5.745809,1.501621,-2.033478,9.654260,-5.036337,6.044626,-1.691258,-0.909077,-2.182554,-2.156049,-0.380554,-9.826720,-7.884509,-9.304960,-9.308838,3.613747,-8.243745,-2.684518,3.699687,-0.912771],[-5.666546,4.250634,-3.377799,8.113783,-6.823564,-0.053336,2.651160,8.431310,7.350313,2.339924,-2.049703,6.908813,2.012405,9.491896,2.055578,8.273765,9.044375,4.240874,-0.051193,4.806096],[-8.930907,0.395669,-3.291063,0.458932,-4.882392,9.255455,9.715253,8.680393,-1.282923,9.673607,-7.544034,-9.557705,9.409605,-9.802549,-4.838183,-9.805541,2.002073,5.572812,-8.832850,-1.533968],[1.671508,7.709428,-9.920816,9.467222,8.350199,-3.813899,4.181794,-8.142890,-0.925290,0.915546,-6.815162,6.020927,8.950198,8.053484,2.158823,0.427986,6.637366,-5.030317,2.021819,4.318349],[-0.544087,0.299868,-0.334926,4.438820,-4.162104,1.076597,-9.117906,-7.854094,1.270768,-5.515598,0.976804,3.883173,-2.222203,-8.278907,-7.354053,1.706283,-7.197339,-2.478039,-9.762687,6.683852],[-7.825071,5.220324,-5.720623,5.401537,1.141001,-2.730416,1.222708,2.796654,2.028792,3.574873,0.991627,2.267246,0.154655,-9.586447,8.213491,-8.864901,4.956933,-7.564037,-0.171118,6.734105],[2.895742,-7.262445,-8.958829,9.184531,-4.622257,4.359657,4.823526,1.799370,-0.122650,-2.011850,6.138901,-8.196085,-7.894604,-2.428043,-8.764968,-1.868687,-6.848916,-7.381714,-1.207608,-2.522410],[-5.530218,2.398539,-8.134640,8.600011,-6.082670,-8.086062,-5.133516,-4.521135,-6.756362,5.164486,0.275358,-5.628591,1.264902,-1.682487,-3.357011,-1.148335,-8.674657,-4.385911,-9.685472,6.029649],[9.214216,-2.972543,-7.421226,-4.550969,-0.269475,7.206818,4.769470,8.965780,-6.422558,8.438710,-1.453538,-0.202301,6.457481,-4.918751,-9.286988,-7.094632,0.817628,9.153448,-8.601916,-0.321912],[-7.807350,-2.064829,-4.947551,-6.989599,9.520656,6.345107,9.953265,-9.162431,8.396411,-9.551766,-4.022339,5.395365,7.632596,-0.336873,1.535962,-6.409525,-4.946711,9.383536,-3.926539,-4.770164],[0.752619,-9.933438,5.516617,4.912489,4.445730,-2.630551,3.584814,6.768616,-6.724797,-9.640337,9.338671,4.847213,6.597705,-3.880927,-0.729666,5.275425,-4.513986,-4.454896,-9.411203,-4.692467],[1.418854,2.323401,4.884565,-0.750597,-2.136095,8.392291,3.980866,-8.773057,4.903039,6.494658,4.559816,-7.737408,-1.455204,8.840901,-4.614431,-3.617816,-6.246659,-0.714378,-8.024859,7.839035],[9.698783,-3.913520,-7.115605,8.783341,8.904320,7.958497,7.711943,1.538852,4.949625,-5.754751,-8.281290,4.291375,6.446845,-9.672279,-7.920415,-6.306524,-7.717040,6.385356,8.157819,7.133594],[8.169351,5.368819,-7.747489,-5.227425,4.078308,3.519539,4.094929,-3.960673,9.325315,-2.139439,5.462936,8.786441,-2.675437,-2.585057,-3.557816,-2.155143,-9.502988,-6.499711,-8.770013,-5.097918],[-3.651118,-2.304326,2.404655,-0.484218,6.917005,-7.806823,3.010863,9.892973,-0.421110,-9.442640,3.540594,-6.348309,-0.976839,-3.366258,1.327767,9.763617,-8.793054,9.396147,-6.952315,-1.976922],[1.217642,-8.285865,2.702849,-8.828800,0.717781,-3.828895,0.142004,7.321111,1.323381,6.764091,-5.636262,-4.278452,-4.536502,-7.071830,4.097422,-8.267277,-9.014191,-6.326603,-1.681142,0.679894],[8.089595,-9.876641,6.615756,-6.417802,1.590227,5.455791,-9.807594,0.479352,-3.656661,-9.732949,-0.879384,-0.301358,4.737535,-9.322602,1.811437,-7.350042,1.154696,6.007722,-3.335914,-5.553493],[4.920145,7.736493,1.133850,-6.224726,5.842501,-1.258044,-7.184594,-4.042314,6.143117,6.232824,-5.708010,3.290139,9.754420,-9.113962,-6.965301,2.288668,8.460494,-5.311889,1.895013,-3.895651],[3.965845,4.764331,1.707367,2.239168,-6.644095,9.333404,-5.440386,4.595502,3.642721,7.400559,-4.843637,-4.466115,-7.917029,-0.531306,3.363020,-6.225699,5.172378,-6.341828,4.603462,9.011830],[3.473640,-8.988738,5.304312,2.722240,-9.107091,4.533342,8.208500,-6.208585,-2.933305,-3.030908,7.524419,-4.565057,-0.420047,7.543770,-3.169087,5.357223,5.695181,-7.501371,7.866059,6.181735],[-2.437417,-9.983242,-1.700842,7.439478,-6.663844,9.064177,-3.850672,-3.253855,-6.542018,-7.054526,2.504120,-4.519649,-8.743681,1.792255,-2.445959,5.816658,4.250598,0.683701,-9.850980,-5.767060],[-0.006333,-0.078469,6.404336,5.684665,-6.473864,1.795961,4.123460,-7.233924,-8.358306,-1.495391,-0.761148,5.179374,1.496857,-8.491260,-2.021627,-0.121062,-2.214936,6.531170,-4.199956,0.606536],[1.920487,-8.725508,6.486309,-6.719118,-3.923127,-6.526404,-7.748965,1.161971,-7.705809,3.648649,-6.044539,5.560886,-2.569943,3.068548,3.745083,4.057729,7.929122,-9.199469,-9.454092,-5.609692],[0.285385,7.546756,-7.980890,5.961378,-3.872870,3.383093,6.347678,5.277835,-3.783790,-5.280770,-3.359183,-8.287897,1.357612,-1.976693,3.784344,-3.052807,2.452444,-7.935885,-7.745385,8.304294],[-9.212154,-8.016910,3.875582,7.358171,-6.762598,-7.597164,0.667158,-8.550677,9.910527,-7.943377,2.327495,8.981461,-2.898619,-7.114037,3.115964,-4.923914,1.151186,2.342545,-0.921602,-8.106102],[-1.304147,5.010095,0.713682,-0.641263,-3.854324,8.293656,-4.007641,3.018324,-2.903729,3.312964,3.565429,3.326889,-1.698609,8.391650,0.010079,3.841979,-5.930245,4.899161,-8.579326,-1.792378],[-9.722252,-7.320502,-7.602337,8.947174,-9.234779,6.399495,-2.420458,-5.692806,9.528405,-2.862860,2.229179,4.144693,-8.207973,1.893574,-3.773335,-4.782366,0.158477,5.556200,-1.343987,-9.505179],[-4.715407,-2.251373,-2.820402,7.046890,-7.307388,-4.311768,-9.816523,-4.309367,-2.233336,3.255974,4.238685,9.320039,3.680240,1.821620,0.880303,-3.916519,7.387989,7.519738,2.452199,8.408182],[-8.447902,1.472068,2.007580,6.552533,8.584524,6.314610,-2.617512,4.862508,9.760044,9.452377,-5.848000,-1.524541,-9.439498,4.711349,7.970612,-9.407474,-1.663233,-7.410136,0.778257,1.612078],[-2.127984,8.848413,8.127229,-1.739795,8.500710,6.067396,5.877484,5.047354,6.974768,4.669686,-9.692065,-3.413475,8.744845,-5.390101,4.601613,7.175223,-6.540387,-2.744711,3.877366,8.809481],[9.176077,-4.774335,-0.566127,-4.805883,-3.830462,-1.973875,4.487018,0.051437,8.022310,3.626704,0.970910,0.114579,-7.828982,9.381812,-2.009307,-5.000367,-3.410389,8.558528,4.959649,-6.225738],[4.785230,-5.866811,-3.946395,-4.835904,2.686915,-4.436711,-4.978118,1.701641,4.572960,5.837930,4.343301,7.634186,-0.429096,-5.286191,8.242744,-8.189246,-8.423573,9.842791,-4.424895,-0.750629],[-0.348569,1.484990,-0.119660,6.481174,3.675192,-0.667649,-8.565457,-2.959291,-8.586105,-2.531742,-7.972110,-1.403244,8.921650,1.987240,7.075627,-7.167604,-1.203707,1.479256,-3.872710,-7.395516],[7.436103,-8.551714,9.136657,-9.079494,2.897812,7.430176,2.456691,-9.262385,2.360845,1.601349,-5.926188,-6.479580,1.744624,7.697450,-3.241039,9.612446,-0.838751,-8.416438,2.560881,6.858816],[1.755758,-3.115930,9.736412,-2.845353,-0.316847,7.844693,7.762900,5.271630,2.385098,-7.802945,-7.134755,7.536647,2.795794,-6.270590,1.151850,1.807500,-1.955745,6.590248,4.135511,6.899357],[7.444718,-9.071177,-2.655859,5.330559,-5.168604,-7.716108,-1.205158,-3.518295,1.604359,-4.606171,-7.565020,1.138531,7.506580,-5.487992,-6.430355,-3.670378,5.324573,-7.573438,-5.557618,3.026269],[2.347950,2.362299,-2.797273,5.573633,6.095764,-0.564639,-5.283268,-4.479322,-2.975060,-0.076457,-0.590184,6.154903,7.494656,-4.326331,2.428631,-1.264021,7.678349,-0.529108,5.191220,6.449660],[1.343803,9.468354,3.094982,0.110516,-5.538905,5.851522,-6.215255,-3.871632,-3.370606,2.073616,4.353101,9.403188,-3.209644,-4.246422,0.527862,-5.042987,7.045835,-5.438840,4.369925,-4.983894],[5.174376,1.336592,-3.621159,9.883946,-5.726645,1.988270,2.032765,-7.083549,-1.767378,2.541497,-4.247091,2.793194,6.133605,-3.929375,3.787976,1.863479,-8.964290,1.720091,-8.441468,-1.319674],[9.662043,-0.290498,-4.133023,-5.717216,5.597803,-5.344981,2.466358,5.025662,-6.736177,-7.011250,9.736229,-1.494553,-4.489497,-0.207220,7.168919,4.950648,-8.895132,6.459077,-0.909684,-3.253210],[5.406672,4.095720,-5.938555,-4.584022,-5.364180,-7.877156,-3.280642,-5.649987,-4.447840,3.813948,3.300831,2.374903,8.195698,-5.972101,-8.607315,5.381534,7.444490,0.580591,-1.550778,-1.819089],[-0.562020,-5.718790,-6.956166,5.877778,7.557024,-5.231320,7.909615,2.800983,-0.208970,-3.984415,-8.239291,-2.211225,-2.749952,8.911916,9.272594,5.120978,-4.796218,-4.324867,-3.598454,-6.110144],[4.021055,-6.024000,-2.591645,2.742684,0.503684,2.946523,3.745107,-4.743007,2.111954,-0.024443,7.861641,-2.002218,8.190925,-0.246339,-8.479297,-4.536777,2.390173,-4.934128,-6.086883,-5.360242],[4.575463,5.407188,-7.347639,-3.774767,7.869841,-7.629452,0.090701,-4.696764,-7.376137,-4.665399,2.311041,-9.178426,-7.985063,-1.389460,-7.938673,-0.327192,2.880602,-8.877246,3.817817,6.348178]], dtype = "float32")#candidate|14913|(96, 20)|const|float32
call_14912 = relay.TupleGetItem(func_8904_call(relay.reshape(const_14913.astype('float32'), [1920,])), 0)
call_14914 = relay.TupleGetItem(func_8906_call(relay.reshape(const_14913.astype('float32'), [1920,])), 0)
func_2034_call = mod.get_global_var('func_2034')
func_2038_call = mutated_mod.get_global_var('func_2038')
var_14916 = relay.var("var_14916", dtype = "int8", shape = (768,))#candidate|14916|(768,)|var|int8
var_14917 = relay.var("var_14917", dtype = "float32", shape = (975,))#candidate|14917|(975,)|var|float32
call_14915 = relay.TupleGetItem(func_2034_call(relay.reshape(var_14916.astype('int8'), [6, 8, 16]), relay.reshape(var_14917.astype('float32'), [975, 1]), ), 1)
call_14918 = relay.TupleGetItem(func_2038_call(relay.reshape(var_14916.astype('int8'), [6, 8, 16]), relay.reshape(var_14917.astype('float32'), [975, 1]), ), 1)
func_2115_call = mod.get_global_var('func_2115')
func_2118_call = mutated_mod.get_global_var('func_2118')
var_14923 = relay.var("var_14923", dtype = "float32", shape = (4, 48))#candidate|14923|(4, 48)|var|float32
call_14922 = relay.TupleGetItem(func_2115_call(relay.reshape(var_14923.astype('float32'), [3, 16, 4]), relay.reshape(call_14915.astype('float32'), [975,]), ), 3)
call_14924 = relay.TupleGetItem(func_2118_call(relay.reshape(var_14923.astype('float32'), [3, 16, 4]), relay.reshape(call_14915.astype('float32'), [975,]), ), 3)
output = relay.Tuple([call_14887,call_14889,call_14900,var_14901,call_14912,const_14913,call_14915,var_14916,var_14917,call_14922,var_14923,])
output2 = relay.Tuple([call_14888,call_14890,call_14902,var_14901,call_14914,const_14913,call_14918,var_14916,var_14917,call_14924,var_14923,])
func_14926 = relay.Function([var_14901,var_14916,var_14917,var_14923,], output)
mod['func_14926'] = func_14926
mod = relay.transform.InferType()(mod)
mutated_mod['func_14926'] = func_14926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14926_call = mutated_mod.get_global_var('func_14926')
var_14928 = relay.var("var_14928", dtype = "float64", shape = (1152,))#candidate|14928|(1152,)|var|float64
var_14929 = relay.var("var_14929", dtype = "int8", shape = (768,))#candidate|14929|(768,)|var|int8
var_14930 = relay.var("var_14930", dtype = "float32", shape = (975,))#candidate|14930|(975,)|var|float32
var_14931 = relay.var("var_14931", dtype = "float32", shape = (4, 48))#candidate|14931|(4, 48)|var|float32
call_14927 = func_14926_call(var_14928,var_14929,var_14930,var_14931,)
output = call_14927
func_14932 = relay.Function([var_14928,var_14929,var_14930,var_14931,], output)
mutated_mod['func_14932'] = func_14932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14452_call = mod.get_global_var('func_14452')
func_14454_call = mutated_mod.get_global_var('func_14454')
call_14977 = relay.TupleGetItem(func_14452_call(), 0)
call_14978 = relay.TupleGetItem(func_14454_call(), 0)
output = relay.Tuple([call_14977,])
output2 = relay.Tuple([call_14978,])
func_14990 = relay.Function([], output)
mod['func_14990'] = func_14990
mod = relay.transform.InferType()(mod)
mutated_mod['func_14990'] = func_14990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14990_call = mutated_mod.get_global_var('func_14990')
call_14991 = func_14990_call()
output = call_14991
func_14992 = relay.Function([], output)
mutated_mod['func_14992'] = func_14992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14855_call = mod.get_global_var('func_14855')
func_14857_call = mutated_mod.get_global_var('func_14857')
call_15000 = func_14855_call()
call_15001 = func_14855_call()
func_7327_call = mod.get_global_var('func_7327')
func_7329_call = mutated_mod.get_global_var('func_7329')
var_15015 = relay.var("var_15015", dtype = "int64", shape = (8,))#candidate|15015|(8,)|var|int64
call_15014 = relay.TupleGetItem(func_7327_call(relay.reshape(var_15015.astype('int64'), [4, 1, 2])), 0)
call_15016 = relay.TupleGetItem(func_7329_call(relay.reshape(var_15015.astype('int64'), [4, 1, 2])), 0)
output = relay.Tuple([call_15000,call_15014,var_15015,])
output2 = relay.Tuple([call_15001,call_15016,var_15015,])
func_15020 = relay.Function([var_15015,], output)
mod['func_15020'] = func_15020
mod = relay.transform.InferType()(mod)
mutated_mod['func_15020'] = func_15020
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15021 = relay.var("var_15021", dtype = "int64", shape = (8,))#candidate|15021|(8,)|var|int64
func_15020_call = mutated_mod.get_global_var('func_15020')
call_15022 = func_15020_call(var_15021)
output = call_15022
func_15023 = relay.Function([var_15021], output)
mutated_mod['func_15023'] = func_15023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13780_call = mod.get_global_var('func_13780')
func_13781_call = mutated_mod.get_global_var('func_13781')
call_15034 = func_13780_call()
call_15035 = func_13780_call()
output = relay.Tuple([call_15034,])
output2 = relay.Tuple([call_15035,])
func_15045 = relay.Function([], output)
mod['func_15045'] = func_15045
mod = relay.transform.InferType()(mod)
mutated_mod['func_15045'] = func_15045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15045_call = mutated_mod.get_global_var('func_15045')
call_15046 = func_15045_call()
output = call_15046
func_15047 = relay.Function([], output)
mutated_mod['func_15047'] = func_15047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14452_call = mod.get_global_var('func_14452')
func_14454_call = mutated_mod.get_global_var('func_14454')
call_15079 = relay.TupleGetItem(func_14452_call(), 3)
call_15080 = relay.TupleGetItem(func_14454_call(), 3)
output = call_15079
output2 = call_15080
func_15088 = relay.Function([], output)
mod['func_15088'] = func_15088
mod = relay.transform.InferType()(mod)
mutated_mod['func_15088'] = func_15088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15088_call = mutated_mod.get_global_var('func_15088')
call_15089 = func_15088_call()
output = call_15089
func_15090 = relay.Function([], output)
mutated_mod['func_15090'] = func_15090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13565_call = mod.get_global_var('func_13565')
func_13567_call = mutated_mod.get_global_var('func_13567')
call_15100 = relay.TupleGetItem(func_13565_call(), 0)
call_15101 = relay.TupleGetItem(func_13567_call(), 0)
func_13360_call = mod.get_global_var('func_13360')
func_13362_call = mutated_mod.get_global_var('func_13362')
call_15109 = relay.TupleGetItem(func_13360_call(), 1)
call_15110 = relay.TupleGetItem(func_13362_call(), 1)
output = relay.Tuple([call_15100,call_15109,])
output2 = relay.Tuple([call_15101,call_15110,])
func_15123 = relay.Function([], output)
mod['func_15123'] = func_15123
mod = relay.transform.InferType()(mod)
output = func_15123()
func_15124 = relay.Function([], output)
mutated_mod['func_15124'] = func_15124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15088_call = mod.get_global_var('func_15088')
func_15090_call = mutated_mod.get_global_var('func_15090')
call_15178 = func_15088_call()
call_15179 = func_15088_call()
func_4833_call = mod.get_global_var('func_4833')
func_4837_call = mutated_mod.get_global_var('func_4837')
var_15181 = relay.var("var_15181", dtype = "int8", shape = (84,))#candidate|15181|(84,)|var|int8
var_15182 = relay.var("var_15182", dtype = "int8", shape = (168,))#candidate|15182|(168,)|var|int8
call_15180 = func_4833_call(relay.reshape(var_15181.astype('int8'), [1, 6, 14]), relay.reshape(var_15182.astype('int8'), [2, 6, 14]), )
call_15183 = func_4833_call(relay.reshape(var_15181.astype('int8'), [1, 6, 14]), relay.reshape(var_15182.astype('int8'), [2, 6, 14]), )
func_14506_call = mod.get_global_var('func_14506')
func_14508_call = mutated_mod.get_global_var('func_14508')
var_15195 = relay.var("var_15195", dtype = "float32", shape = (192,))#candidate|15195|(192,)|var|float32
call_15194 = relay.TupleGetItem(func_14506_call(relay.reshape(var_15195.astype('float32'), [96, 2])), 1)
call_15196 = relay.TupleGetItem(func_14508_call(relay.reshape(var_15195.astype('float32'), [96, 2])), 1)
output = relay.Tuple([call_15178,call_15180,var_15181,var_15182,call_15194,var_15195,])
output2 = relay.Tuple([call_15179,call_15183,var_15181,var_15182,call_15196,var_15195,])
func_15203 = relay.Function([var_15181,var_15182,var_15195,], output)
mod['func_15203'] = func_15203
mod = relay.transform.InferType()(mod)
var_15204 = relay.var("var_15204", dtype = "int8", shape = (84,))#candidate|15204|(84,)|var|int8
var_15205 = relay.var("var_15205", dtype = "int8", shape = (168,))#candidate|15205|(168,)|var|int8
var_15206 = relay.var("var_15206", dtype = "float32", shape = (192,))#candidate|15206|(192,)|var|float32
output = func_15203(var_15204,var_15205,var_15206,)
func_15207 = relay.Function([var_15204,var_15205,var_15206,], output)
mutated_mod['func_15207'] = func_15207
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15234 = relay.var("var_15234", dtype = "float32", shape = (3, 5, 13))#candidate|15234|(3, 5, 13)|var|float32
uop_15235 = relay.atanh(var_15234.astype('float32')) # shape=(3, 5, 13)
output = relay.Tuple([uop_15235,])
output2 = relay.Tuple([uop_15235,])
func_15241 = relay.Function([var_15234,], output)
mod['func_15241'] = func_15241
mod = relay.transform.InferType()(mod)
mutated_mod['func_15241'] = func_15241
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15242 = relay.var("var_15242", dtype = "float32", shape = (3, 5, 13))#candidate|15242|(3, 5, 13)|var|float32
func_15241_call = mutated_mod.get_global_var('func_15241')
call_15243 = func_15241_call(var_15242)
output = call_15243
func_15244 = relay.Function([var_15242], output)
mutated_mod['func_15244'] = func_15244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13624_call = mod.get_global_var('func_13624')
func_13626_call = mutated_mod.get_global_var('func_13626')
call_15257 = relay.TupleGetItem(func_13624_call(), 0)
call_15258 = relay.TupleGetItem(func_13626_call(), 0)
func_5136_call = mod.get_global_var('func_5136')
func_5140_call = mutated_mod.get_global_var('func_5140')
const_15260 = relay.const([8,-9,-1,7,-9,-7,-1,1,4,-10,8,4,2,1,4,1,5,-6,-2,10,-10,-8,6,2,1,-8,7,10,-5,-9,6,3,-9,10,4,3,-9,-2,10,-8,8,-2,7,-6,3,-3,5,-4,5,-6,-6,-10,9,1,-7,-4,4,-2,8,-5,-3,-3,6,-3,-1,-9,-9,3,2,9,10,6,9,-7,8,-9,-2,-1,10,-9,-4,-10,-7,1,7,-9,-5,-3,7,-1,-3,7,-1,-4,-4,-3,-1,-9,6,-8,-2,-9,3,9,-3,-6,1,10,4,4,-8,4,8,8,3,-6,-2,-2,-9,5], dtype = "int64")#candidate|15260|(120,)|const|int64
const_15261 = relay.const([8,6,3,-3,6,2,1,-3,-7,-2,3,-9,10,-4,-2,6,7,8,-2,7,-2,-7,-2,-9,-9,1,6,-5,-2,1,-5,5,-1,-4,-4,8,-1,-9,5,1,1,-4,-5,-5,-9,2,5,8,10,8,2,-10,-3,7,6,-4,3,6,-8,-5,-7,-4,4,-10,-3,-8,6,-1,6,-1,-5,9,-2,6,-8,-8,1,9,6,-10,10,6,-6,9,5,6,2,10,2,5,-8,-5,6,4,5,-3,-4,3,5,3,1,-2,5,-10,-9,-7,9,-7,7,-9,7,-1,10,-10,7,7,-3,2,10,-6,-6,-5,6,2,-3,-10,-2,1,3,6,-7,8,9,-1,-2,7,10,3,-4,-1,-5,-7,-10,-8,2,-4,5,10,-2,7,7,-3,6,3,10,-8,3,-3,-6,5,-3,6,1,-5,8,-10,-6,2,-9,-3,-8,-8,-8,3,10,-9,-7,2,-2,2,1,-5,-4,-8,-1,-4,3,10,-10,5,-3,4,1,9,-5,5,2,2,6,-9,-2,-8,4,6,2,-6,6,-2,-8,-2,1,-8,7,1,1,-2,4,7,7,3,-7,-4,-9,-9,9,-9,-9,5,8,-7,9,-1,9,-2,5,8,4,-2,8,9,5,10,-4,7,-3,2,-6,-7,-5,3,-4,-10,5,-1,-5,10,6,-3,-7,6,-7,-3,5,9,-7,-8,5,9,-1,-3,-9,-6,5,9,10,-1,6,-1,4,-1,-2,1,-6,-9,1,3,7,8,1,-3,7,-9,9,-5,7,3,-4,1,7,7,2,-1,-1,2,-10,-2,-10,-9,-10,2,-10,-9,1,4,-9,-9,3,1,-1,-6,9,-8,-9,-8,5,8,-6,10,8,9,-7,10,10,-5,-6,6,1,4,2,10,-3,3,-5,1,6,-1,-10,-6,4,-3,-4,-4,2,-8,-10,-4,-9,4,-1,-7,5,-2,1,-7,-9,3,-9,2,-5,-10,9,7,2,-1,-6,-9,-10,-8,-9,4,-3,-3,6,-6,6,-5,1,-4,-5,5,5,2,5,6,3,5,-9,-2,4,7,5,6,5,-8,-4,10,7,5,-4,-9,1,4,-2,6,-4,7,-4,-7,2,-7,-8,-8,-3,-10,-3,3,-3,-7,-5,1,3,-1,3,-6,-3,3,-2,-10,-3,-1,9,2,2,7,2,9,7,4,9,-7,3,-8,9,9,8,10,-3,-9,4,4,-3,-1,6,2,-5,10,9,4,-5,1,2,-1,6,4,4,-5,-3,-7,4,-4,8,-1,-1,-6,10,10,-9,-9,-8,6,-2,-1,9,-6,7,6,-6,-4,-1,-5,-6,-3,7,1,-6,9,7,-7,-8,-9,-4,2,-1,-1,5,-3,3,9,1,-5,-6,-7,4,1,-6,9,-7,-2,-7,1,8,-4,-4,-1,2,2,-2,-3,4,10,-4,9,-10,-10,-3,9,-8,10,-6,7,-7,-6,-9,-7,2,-4,-8,8,6,-5,10,8,-8,8,-1,4,3,9,8,8,5,8,6,1,3,-1,-1,9,-1,-7,-3,2,-10,9,-9,10,8,5,-4,-6,-4,10,-5,-7,5,9,-5,-3,2,-3,-10,4,2,1,-8,1,-1,-7,9,5,10,-3,4,7,9,-6,-4,-6,-2,2,-2,-1,-5,1,2,9,7,6,7,9,5,4,8,8,7,-9,3,3,-6,-2,-8,2,-3,9,4,-8,5,-10,4,-10,-6,-1,9,-8,6,-5,1,2,-8,5,-10,10,-5,-6,-8,9,7,4,-1,3,2,-4,7,-8,8,8,-4,-1,9,-7,6,-1,-3,-1,7,2,1,-2,-1,-5,4,4,2,-9,5,-7,2,-5,5,9,-9,-9,8,-3,4,7,1,-7,1,5,-10,6,-4,-6,9,1,8,-10,-3,-7], dtype = "int64")#candidate|15261|(720,)|const|int64
const_15262 = relay.const([6,10,-9,7,-4,10,-10,-2,-3,4,1,-4,-10,4,-6,4,8,-3,-4,1,-9,9,-5,-8,4,-10,5,3,-3,-5,-1,10,4,6,-6,-5,8,-6,4,1,5,-2,9,6,-4,2,-1,-7,-6,2,-2,8,-10,4,8,4,9,2,1,2,10,-3,4,5,-2,3,3,-3,4,6,3,5,-6,-1,-6,4,-7,-8,-4,-3,1,10,7,-6,-1,5,4,9,9,-9,-5,3,-8,2,-6,-8,-1,3,-2,-1,3,6,-5,7,4,-9,9,-10,-4,10,-7,1,9,-8,-2,3,-6,-3,5,-7,8,-8,9,-5,-10,7,5,7,-1,-4,-7,-8,-5,4,-3,-9,-8,-9,6,-3,10,6,-7,1,10,-1,-2,10,2,-7,6,5,4,-2,-9,-9,-5,6,9,-2,-3,-8,3,-2,1,-9,7,4,9,2,-10,-9,-7,1,-4,-5,-7,4,8,-7,7,-9,-2,-6,8,9,10,-5,2,-10,-10,-3,-7,-8,-3,7,3,-4,8,3,9,-6,-7,7,6,6,-4,4,6,-8,7,10,-3,4,-6,9,-9,8,3,-7,-3,-6,4,8,-2,-10,4,-10,8,-10,10,-2,2,7,5,6,-7,-5,-2,2,1,-4,3,4,7,6,1,6,-9,-9,-7,10,-9,4,8,-7,7,6,5,-1,-3,-2,8,8,-3,10,3,-3,-7,-6,-2,-5,-6,10,10,8,2,-8,9,6,10,-1,7,7,-10,8,10,4,-4,-9,-8,8,6,8,9,-7,-9,-3,-2,-8,-5,-8,-10,1,7,-8,9,-2,-1,2,4,10,8,2,6,-4,-6,8,-3,10,10,-4,6,-4,6,-9,-5,-8,4,3,-9,5,-7,3,-1,-1,-3,-8,1,-5,9,-1,-3,-5,6,9,5,1,6,-4,-9,5,-2,-2,-8,1,-1,10,-1,2,-3,3,4,9,-7,4,2,9,-6,-8,-8,-10,3,-4,6,-2,-7,-8,8,-1,-4,1,8,-9,-9,-7,-6,-5,-8,1,-4,-5,-7,-4,-2,-10,-1,2,2,-4,-6,9,1,-9,2,-2,-5,7,-2,7,-5,-2,-9,-10,4,2,-6,-2,-5,-5,-2,-3,-6,1,3,-3,6,-9,-10,3,-2,3,-6,-4,-5,5,-5,-6,-1,10,6,4,-1,-4,9,-4,-2,8,2,-8,8,6,-4,-6,-1,8,-2,-9,5,-1,-1,-3,1,-3,-3,2,6,7,-2,4,-9,-3,5,3,3,4,8,1,1,4,6,-5,4,10,-7,9,9,9,4,-5,6,3,7,5,9,-1,-5,-7,2,-3,2,-7,6,6,-7,-8,-8,-1,6,-2,5,-10,-4,9,6,3,8,10,7,5,-5,-9,4,10,5,-5,-7,-3,3,5,6,7,1,7,3,1,4,1,-9,-8,-2,9,9,10,-5,-1,-6,-6,-8,-2,6,-7,3,-8,8,9,8,-9,1,9,6,-9,-10,1,8,7,9,4,-3,-6,-6,-10,4,-1,1,-3,4,3,-8,2,-8,-10,6,-8,-6,-9,-9,9,10,-10,-4,10,-6,-9,-5,-10,3,-9,6,7,2,-6,-5,-6,-7,-6,1,6,-6,4,10,-6,8,2,-1,-7,5,3,2,-4,8,-9,-5,8,2,5,-10,6,6,-1,9,9,-5,3,-4,6,7,2,-10,5,4,7,3,-1,1,8,-4,-3,1,-6,-5,10,-8,5,-5,-4,-2,-3,6,6,8,7,-10,2,-8,-8,-1,-4,1,10,2,4,-7,-9,-3,-10,8,4,10,9,2,-1,-6,-5,6,2,1,2,-3,1,-7,-8,2,10,5,2,-9,-4,9,1,-7,5,-10,-6,-1,10,1,2,-9,-5,-4,-6,9,-7,1,6,-2,6,10,-5,-2,-9,-5,4,5,-10,6,1,8,-6,9,-5,-10,5,4,1,6,-6,-8,5,-2,2,1,-5,-5,-7,2,-7,4,2,-1,1,2,-8,-2,4,10,-3,-3,-9,1,5,10,6,2,-2,-3,-2,-2,7,-3,-9,-9,3,3,2,-2,9,-9,-5,-5,5,10,4,8,-6,-2,-6,-7,5,-5,-8,-6,-6,-10,-7,6,4,9,-7,-7,10,10,-2,-4,-1,-6,3,-3,-10,-10,9,-8,3,3,6,7,-1,1,5,10,4,4,9,-8,4,5,7,8,-3,-2,-1,5,7,5,1,10,3,-3,-3,1,-1,3,-10,-8,2,-3,10,-6,2,-10,9,8,-4,-4,4,-6,-2,2,10,6,-1,-8,7,-7,7,1,7,-8,2,10,7,-10,-5,-10,4,10,5,6,3,-2,-3,8,4,-1,-10,-2,-6,-4,9,-7,-10,-8,-6,8,10,-4,4,-2,-10,7,-3,4,3,2,2,5,-10,-10,9,-8,9,-3,3,-1,10,2,-7,5,-6,4,-10,-1,-5,-7,-10,-5,-6,-10,-6,4,9,1,6,-7,-5,-10,1,-5,4,-1,8,3,-8,5,-4,-2,-6,-8,-9,5,-8,-8,10,-5,5,1,4,7,5,-6,10,-1,-10,-1,5,-2,-2,-4,-2,-9,5,-8,1,10,7,4,-5,6,-7,-2,-6,7,-5,-2,-8,-1,8,3,-5,5,1,1,-8,9,5,-8,-8,-1,-6,7,4,8,-9,3,-3,8,-2,10,-6,-5,-2,4,-8,2,-9,-7,-9,7,5,6,10,2,2,2,-10,-1,-10,2,-1,1,3,5,4,-2,3,4,1,-7,-7,1,8,10,8,-5,6,10,-5,-3,-8,5,-2,-7,7,8,-5,-1,-2,8,-3,-10,10,-10,7,-5,10,-6,-10,-9,-9,3,5,-4,5,6,6,8,-8,-4,-6,9,10,2,10,-9,8,10,5,10,-7,-9,4,10,8,4,4,1,9,-4,-5,-8,6,-4,-4,-1,3,-4,7,-7,-10,10,4,-6,5,4,4,10,-1,-2,-1,4,3,8,-1,-7,-6,5,-8,-5,-2,2,-2,-7,-9,8,2,-3,-9,6,-8,3,2,5,8,5,-10,5,1,7,-2,1,4,-10,-7,-4,-1,-10,-6,7,9,-3,8,3,1,9,-4,7,6,-2,4,-9,-5,-2,-6,-5,10,5,8,-7,-7,-2,9,-8,7,-8,-8,-7,-6,5,7,-8,-2,5,1,8,-10,-9,-10,-2,9,-7,6,3,5,7,-2,1,8,-1,-9,6,-9,-8,4,-7,1,1,10,-1,-3,-10,-3,-8,-8,9,8,-9,-2,8,-1,10,-9,-1,-8,5,-1,6,-6,7,3,-3,3,10,1,5,2,-3,-8,-1,7,8,1,-5,8,2,8,-2,7,8,9,7,-9,-4,5,3,-1,3,5,-10,-8,4,-8,-6,-10,3,10,-3,-10,-7,-4,8,-1,9,9,-1,-4,2,5,6,-4,7,9,-4,10,-8,10,-2,-9,1,2,2,8,7,3,1,10,-3,7,-10,7,-1,-3,1,6,9,-3,4,-4,7,2,-5,5,3,-3,10,2,8,6,9,-1,-10,9,8,-4,-1,2,-1,3,-10,9,-8,-3,10,8,-9,-8,-3,-2,-10,-5,-3,4,7,-9,6,9,1,-2,9,-10,9,7,5,-5,6,-6,9,4,-7,-3,3,7,-1,-6,-9,9,6,-1,7,-8,6,-5,-3,-10,-2,-5,4,10,3,8,-6,-1,4,5,-8,6,6,10,10,4,-5,-10,3,8,8,7,4,-8,9,-2,6,-4,9,6,6,-5,8,-1,5,-8,-5,7,-4,8,8,-4,-9,-1,-10,2,-6,6,10,9,-7,8,-2,3,-2,1], dtype = "int8")#candidate|15262|(1440,)|const|int8
call_15259 = relay.TupleGetItem(func_5136_call(relay.reshape(const_15260.astype('int64'), [12, 10, 1]), relay.reshape(const_15261.astype('int64'), [12, 10, 6]), relay.reshape(const_15262.astype('int8'), [1440,]), ), 0)
call_15263 = relay.TupleGetItem(func_5140_call(relay.reshape(const_15260.astype('int64'), [12, 10, 1]), relay.reshape(const_15261.astype('int64'), [12, 10, 6]), relay.reshape(const_15262.astype('int8'), [1440,]), ), 0)
func_9294_call = mod.get_global_var('func_9294')
func_9297_call = mutated_mod.get_global_var('func_9297')
var_15267 = relay.var("var_15267", dtype = "float32", shape = (169, 10))#candidate|15267|(169, 10)|var|float32
call_15266 = relay.TupleGetItem(func_9294_call(relay.reshape(var_15267.astype('float32'), [13, 13, 10])), 1)
call_15268 = relay.TupleGetItem(func_9297_call(relay.reshape(var_15267.astype('float32'), [13, 13, 10])), 1)
var_15272 = relay.var("var_15272", dtype = "float32", shape = (169, 10))#candidate|15272|(169, 10)|var|float32
bop_15273 = relay.right_shift(var_15267.astype('uint64'), relay.reshape(var_15272.astype('uint64'), relay.shape_of(var_15267))) # shape=(169, 10)
uop_15277 = relay.acos(var_15272.astype('float32')) # shape=(169, 10)
output = relay.Tuple([call_15257,call_15259,const_15260,const_15261,const_15262,call_15266,bop_15273,uop_15277,])
output2 = relay.Tuple([call_15258,call_15263,const_15260,const_15261,const_15262,call_15268,bop_15273,uop_15277,])
func_15287 = relay.Function([var_15267,var_15272,], output)
mod['func_15287'] = func_15287
mod = relay.transform.InferType()(mod)
var_15288 = relay.var("var_15288", dtype = "float32", shape = (169, 10))#candidate|15288|(169, 10)|var|float32
var_15289 = relay.var("var_15289", dtype = "float32", shape = (169, 10))#candidate|15289|(169, 10)|var|float32
output = func_15287(var_15288,var_15289,)
func_15290 = relay.Function([var_15288,var_15289,], output)
mutated_mod['func_15290'] = func_15290
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15305 = relay.var("var_15305", dtype = "uint16", shape = (8, 7, 8))#candidate|15305|(8, 7, 8)|var|uint16
var_15306 = relay.var("var_15306", dtype = "uint16", shape = (8, 7, 8))#candidate|15306|(8, 7, 8)|var|uint16
bop_15307 = relay.left_shift(var_15305.astype('uint16'), relay.reshape(var_15306.astype('uint16'), relay.shape_of(var_15305))) # shape=(8, 7, 8)
output = relay.Tuple([bop_15307,])
output2 = relay.Tuple([bop_15307,])
func_15323 = relay.Function([var_15305,var_15306,], output)
mod['func_15323'] = func_15323
mod = relay.transform.InferType()(mod)
mutated_mod['func_15323'] = func_15323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15323_call = mutated_mod.get_global_var('func_15323')
var_15325 = relay.var("var_15325", dtype = "uint16", shape = (8, 7, 8))#candidate|15325|(8, 7, 8)|var|uint16
var_15326 = relay.var("var_15326", dtype = "uint16", shape = (8, 7, 8))#candidate|15326|(8, 7, 8)|var|uint16
call_15324 = func_15323_call(var_15325,var_15326,)
output = call_15324
func_15327 = relay.Function([var_15325,var_15326,], output)
mutated_mod['func_15327'] = func_15327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13360_call = mod.get_global_var('func_13360')
func_13362_call = mutated_mod.get_global_var('func_13362')
call_15348 = relay.TupleGetItem(func_13360_call(), 1)
call_15349 = relay.TupleGetItem(func_13362_call(), 1)
uop_15353 = relay.log(call_15348.astype('float32')) # shape=(13, 5, 15)
uop_15355 = relay.log(call_15349.astype('float32')) # shape=(13, 5, 15)
bop_15368 = relay.minimum(call_15348.astype('uint16'), relay.reshape(uop_15353.astype('uint16'), relay.shape_of(call_15348))) # shape=(13, 5, 15)
bop_15371 = relay.minimum(call_15349.astype('uint16'), relay.reshape(uop_15355.astype('uint16'), relay.shape_of(call_15349))) # shape=(13, 5, 15)
func_11108_call = mod.get_global_var('func_11108')
func_11111_call = mutated_mod.get_global_var('func_11111')
var_15393 = relay.var("var_15393", dtype = "uint32", shape = (5, 28))#candidate|15393|(5, 28)|var|uint32
call_15392 = relay.TupleGetItem(func_11108_call(relay.reshape(var_15393.astype('uint32'), [5, 7, 4]), relay.reshape(var_15393.astype('uint32'), [5, 7, 4]), ), 0)
call_15394 = relay.TupleGetItem(func_11111_call(relay.reshape(var_15393.astype('uint32'), [5, 7, 4]), relay.reshape(var_15393.astype('uint32'), [5, 7, 4]), ), 0)
uop_15417 = relay.acosh(var_15393.astype('float64')) # shape=(5, 28)
output = relay.Tuple([bop_15368,call_15392,uop_15417,])
output2 = relay.Tuple([bop_15371,call_15394,uop_15417,])
func_15421 = relay.Function([var_15393,], output)
mod['func_15421'] = func_15421
mod = relay.transform.InferType()(mod)
mutated_mod['func_15421'] = func_15421
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15422 = relay.var("var_15422", dtype = "uint32", shape = (5, 28))#candidate|15422|(5, 28)|var|uint32
func_15421_call = mutated_mod.get_global_var('func_15421')
call_15423 = func_15421_call(var_15422)
output = call_15423
func_15424 = relay.Function([var_15422], output)
mutated_mod['func_15424'] = func_15424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15123_call = mod.get_global_var('func_15123')
func_15124_call = mutated_mod.get_global_var('func_15124')
call_15433 = relay.TupleGetItem(func_15123_call(), 0)
call_15434 = relay.TupleGetItem(func_15124_call(), 0)
func_14452_call = mod.get_global_var('func_14452')
func_14454_call = mutated_mod.get_global_var('func_14454')
call_15461 = relay.TupleGetItem(func_14452_call(), 0)
call_15462 = relay.TupleGetItem(func_14454_call(), 0)
output = relay.Tuple([call_15433,call_15461,])
output2 = relay.Tuple([call_15434,call_15462,])
func_15463 = relay.Function([], output)
mod['func_15463'] = func_15463
mod = relay.transform.InferType()(mod)
mutated_mod['func_15463'] = func_15463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15463_call = mutated_mod.get_global_var('func_15463')
call_15464 = func_15463_call()
output = call_15464
func_15465 = relay.Function([], output)
mutated_mod['func_15465'] = func_15465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13565_call = mod.get_global_var('func_13565')
func_13567_call = mutated_mod.get_global_var('func_13567')
call_15469 = relay.TupleGetItem(func_13565_call(), 0)
call_15470 = relay.TupleGetItem(func_13567_call(), 0)
output = call_15469
output2 = call_15470
func_15471 = relay.Function([], output)
mod['func_15471'] = func_15471
mod = relay.transform.InferType()(mod)
mutated_mod['func_15471'] = func_15471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15471_call = mutated_mod.get_global_var('func_15471')
call_15472 = func_15471_call()
output = call_15472
func_15473 = relay.Function([], output)
mutated_mod['func_15473'] = func_15473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14990_call = mod.get_global_var('func_14990')
func_14992_call = mutated_mod.get_global_var('func_14992')
call_15474 = relay.TupleGetItem(func_14990_call(), 0)
call_15475 = relay.TupleGetItem(func_14992_call(), 0)
func_14855_call = mod.get_global_var('func_14855')
func_14857_call = mutated_mod.get_global_var('func_14857')
call_15483 = func_14855_call()
call_15484 = func_14855_call()
func_15287_call = mod.get_global_var('func_15287')
func_15290_call = mutated_mod.get_global_var('func_15290')
var_15497 = relay.var("var_15497", dtype = "float32", shape = (169, 10))#candidate|15497|(169, 10)|var|float32
call_15496 = relay.TupleGetItem(func_15287_call(relay.reshape(var_15497.astype('float32'), [169, 10]), relay.reshape(var_15497.astype('float32'), [169, 10]), ), 0)
call_15498 = relay.TupleGetItem(func_15290_call(relay.reshape(var_15497.astype('float32'), [169, 10]), relay.reshape(var_15497.astype('float32'), [169, 10]), ), 0)
output = relay.Tuple([call_15474,call_15483,call_15496,var_15497,])
output2 = relay.Tuple([call_15475,call_15484,call_15498,var_15497,])
func_15510 = relay.Function([var_15497,], output)
mod['func_15510'] = func_15510
mod = relay.transform.InferType()(mod)
var_15511 = relay.var("var_15511", dtype = "float32", shape = (169, 10))#candidate|15511|(169, 10)|var|float32
output = func_15510(var_15511)
func_15512 = relay.Function([var_15511], output)
mutated_mod['func_15512'] = func_15512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14400_call = mod.get_global_var('func_14400')
func_14401_call = mutated_mod.get_global_var('func_14401')
call_15517 = func_14400_call()
call_15518 = func_14400_call()
func_15123_call = mod.get_global_var('func_15123')
func_15124_call = mutated_mod.get_global_var('func_15124')
call_15531 = relay.TupleGetItem(func_15123_call(), 1)
call_15532 = relay.TupleGetItem(func_15124_call(), 1)
func_11960_call = mod.get_global_var('func_11960')
func_11964_call = mutated_mod.get_global_var('func_11964')
var_15537 = relay.var("var_15537", dtype = "float64", shape = (800,))#candidate|15537|(800,)|var|float64
const_15538 = relay.const([-5.955639,-8.590530,4.889573,8.812264,5.208952,7.804248,-6.434485,-3.968851,-2.071524,8.108770,0.526931,8.379093,0.386365,7.400192,-8.425753,5.877223,4.817585,6.081881,6.360116,4.979335,5.794856,2.306383,-7.977045,-4.860616,-2.493102,9.771883,4.244261,5.341840,-1.804983,5.678770,3.717593,8.275004,3.050783,-9.782059,-3.473986,8.286249,-4.397376,7.949904,-2.830010,9.713802,9.654174,-7.934622,-7.590580,4.700838,-2.115213,1.181451,6.727414,2.540170,1.786448,4.172305,4.048867,-8.406887,-4.122307,-6.137370,2.231838,8.985797,-2.368802,-4.269685,-4.340100,3.149578,-9.015663,-5.283995,-1.811614,-4.036404,4.780071,5.818092,3.877104,-5.671582,8.099828,-9.134811,8.553975,4.195921,-0.669876,-0.376772,-1.331784,6.224197,-5.829913,-9.223307,5.760806,-4.288469,2.492625,9.127792,6.971400,-1.014349,-3.894319,-0.772451,-3.834448,4.592680,6.336237,2.781694,-0.044433,-1.746187,7.003875,5.808386,-3.254874,1.330011,7.889844,-6.235531,8.319677,6.340692,6.356524,0.094259,0.506036,-4.807775,-5.127254,-9.203297,5.859257,6.644613,-3.340413,8.200431,-6.923113,-3.086981,-9.204802,1.528631,4.131319,8.653319,-6.442529,-4.445101,-0.427175,-2.959816,8.734274,7.550696,0.355146,9.578085,9.706605,-2.419432,9.798867,4.075856,9.823928,7.520249,8.196415,-2.879304,2.307156,2.616016,5.153292,-7.661958,9.780741,1.483848,-2.708284,-1.293255,-3.889548,-7.229461,4.421137,3.600190,-0.194190,6.313518,9.498253,3.075997,-3.138428,-0.261641,-7.451168,-8.476313,-3.908400,-0.106882,-2.192166,-3.113696,-7.701275,6.908802,-3.107509,-3.253269,1.408592,-1.908545,1.243380,-0.469845,5.410732,-5.402860,0.948560,3.761437,-3.768419,2.287466,-0.238937,7.430167,-4.239881,-7.264079,9.703650,0.612479,-4.338110,-6.283872,4.364791,1.896051,0.033425,-4.087931,3.964588,5.171792,1.987451,-2.893099,-4.771248,-6.607813,-1.999045,-8.965378,-7.550621,5.733707,6.896283,-7.360210,-7.608776,1.132264,7.079360,-3.552155,2.080485,9.819805,-0.187134,-7.647193,5.318802,3.259139,5.181677,-0.045912,4.576403,-1.539644,9.487670,6.296868,3.694974,9.934193,-7.602415,9.711283,2.384666,6.780036,-9.126510,9.142109,-5.772250,-9.399988,-3.974442,7.156858,-8.386447,-6.419503,2.503464,0.476546,4.038960,3.630546,-7.696368,9.528582,6.784827,-9.016534,0.804179,-7.712900,-4.879609,2.011701,7.566118,3.945620,2.781849,7.636286,5.067794,3.450120,8.375331,1.572341,5.027619,-7.061958,9.366434,-5.142600,-1.843621,-8.430960,9.094423,0.309339,9.770209,-0.379477,-4.030343,7.099985,-5.972347,-4.621847,4.266728,-2.390483,0.493791,-6.336033,7.925993,6.982970,9.135204,-3.474017,2.829618,8.694395,-3.064377,3.740089,1.883935,4.072135,1.405776,4.385121,9.664588,9.479497,-2.970666,7.655862,8.316340,5.334615,-6.026806,6.335417,2.627351,-6.450854,4.054367,3.779098,-2.328748,-1.254774,-7.466673,2.902124,7.608806,-4.486502,-6.178101,4.381768,-3.842052,-5.333650,6.242748,0.497346,-1.671661,-6.416490,0.885420,-7.267197,-8.930949,-0.505162,-8.921998,-2.877468,-0.434857,-0.106382,-0.198298,-1.543406,-7.015331,-0.028360,3.268540,0.406531,6.705863,9.605996,8.764802,4.391683,-5.314018,-8.798688,8.724750,4.521171,-3.575344,-1.048801,7.355420,9.579930,7.454313,1.927908,6.367673,-8.773030,0.414413,-0.157792,0.244547,-8.771043,1.657150,-2.411392,-5.208425,-5.771629,8.869317,4.010034,-4.046039,2.270216,-1.547758,-7.953285,8.506157,7.454127,-8.623598,7.342232,0.999281,8.278222,-9.103104,6.606636,2.502706,7.280999,-5.308819,-4.616917,-0.166506,-1.501150,-9.773640,-2.839388,8.990400,-3.750353,6.146697,1.056459,-1.561470,6.193907,-4.909138,4.140923,3.974593,1.952211,8.879864,-3.155691,9.821026,3.522156,8.058008,1.891758,9.646774,-3.861084,6.332781,5.873211,-0.987623,-7.414762,2.898288,5.401219,2.306375,-6.100565,-7.909996,-2.577038,7.888485,2.140401,5.298407,4.349128,1.835694,-2.420646,0.603797,-9.371839,-2.065143,-8.812325,-0.742309,-9.714038,-1.091362,-7.301842,9.438763,-9.981932,-1.595041,1.685580,-9.115426,-1.168061,-9.936363,-4.659558,-2.873571,-8.243226,-9.697628,-8.811169,-2.623231,-7.738879,7.064481,6.210894,1.206644,0.097736,8.002390,6.210753,4.463180,0.730198,-6.960573,0.402439,-3.648559,-8.643581,0.416253,0.982288,6.119469,-5.633057,5.011722,-4.093669,-7.745132,-6.827490,-8.508487,9.522162,-7.781202,-5.915285,3.037627,9.843213,1.781647,-6.073236,3.298478,-7.029145,8.406472,8.424819,-0.079958,0.072095,-4.723490,-1.516656,8.497476,-7.015773,9.068854,1.529131,0.438200,-6.619704,-1.857622,1.631022,9.468823,-3.386289,-4.951165,2.811867,0.816290,7.065067,-4.250786,2.372905,-1.053525,5.179643,-2.108807,-9.026148,-5.871443,-1.507884,5.325236,-3.902709,7.878540,4.964286,-9.542616,-8.895149,3.896947,3.738795,8.078377,3.242396,3.040195,5.492305,6.736015,4.278459,2.708873,-1.125663,8.533393,3.286848,-1.095620,-5.149357,4.171575,-0.878863,6.948870,-3.398491,-9.901417,-5.193614,8.843729,2.898013,7.011454,-8.281579,-4.583325,6.290143,4.160580,-4.257850,2.667506,-1.024969,1.020527,7.793023,9.565540,-9.434404,0.869684,3.545356,-6.146437,-5.772727,9.910975,-0.225279,9.124982,8.441457,-7.977700,-3.643770,-6.709627,-4.810276,-0.727586,-6.892738,-5.632656,6.934261,1.525642,-2.550589,-6.202861,0.440106,9.854416,5.014501,0.075528,2.843974,1.452532,2.829612,-3.532428,4.289117,0.732591,-9.310521,-0.703469,-2.217734,-7.009990,-2.961664,8.491214,-7.119781,1.452314,1.011246,-9.858882,1.023418,5.660160,-4.701243,-1.095496,-3.097336,6.274901,7.666082,-0.618962,-8.821770,-7.020818,5.610359,-9.116427,-4.274604,-6.632542,5.190133,-5.570833,-1.896728,8.721112,-2.553172,-6.894988,-0.916136,6.031598,-8.506904,2.929646,9.060510,7.429884,0.282593,-3.395618,3.864778,6.855382,-0.339615,9.234241,2.913419,2.056680,3.480015,-4.825166,9.710806,6.098208,-9.129089,-6.651182,6.181157,-6.942984,-6.214482,-5.016666,0.481669,-9.708123,-3.858896,-6.122243,-1.695772,9.618663,-0.577331,2.925744,2.355679,0.270532,0.985822,5.709734,6.713369,0.960246,4.381328,4.061702,-5.098513,-3.896865,-5.016743,-3.647794,-1.154462,-9.639650,-9.273268,-8.957750,-5.476211,3.057053,-9.138093,-5.331124,-7.501686,4.974797,-4.908763,5.821667,-2.746908,2.767326,-8.959665,6.327583,2.111944,8.463589,-3.340663,3.532455,0.933923,-3.259856,-7.027321,3.789928,0.583063,-4.238009,-1.469202,-9.778007,8.975835,4.006392,4.877508,-7.384646,-4.952677,-1.959558,2.061350,9.920902,-6.585120,-2.812980,1.768562,-9.971234,-9.520449,-7.734522,-5.673258,7.129388,-4.479410,3.697497,-6.404927,-0.822116,-0.359135,0.720207,-4.609568,-1.347791,-5.834475,5.717913,2.349817,-4.852890,-0.897777,-4.892294,7.630045,-5.423135,-4.117144,-2.530825,4.974554,4.782717,7.256890,-1.545536,2.548153,2.752955,7.945317,6.011281,-0.114816,7.352636,-7.535199,1.234088,9.282758,9.163219,2.414956,-3.188133,-5.036426,-8.563385,-6.881301,-1.502305,-6.289465,-1.261375,-5.456557,-7.321690,8.865727,-3.078203,6.135853,-7.708658,3.890483,-5.050747,2.381778,-0.910792,-8.779677,3.803018,3.980496,-2.778760,5.664094,9.987523,9.429302,-7.367929,3.128770,-4.671439,-8.401747,-1.422056,4.795256,8.683780,1.795670,-8.435695,-5.735365,9.661481,0.358587,9.825552,-2.327755,4.414237,-5.013296,-7.718047,-8.937885,-9.462134,3.503052,-4.585179,2.484457,2.974833,9.459012,-3.065786,-1.428455,1.875376,-3.715863,-2.197036,-3.721799,-0.294941,-3.750039,-8.827843,6.598469,5.165611,8.137999,6.692775,5.898946,-0.451414,6.843715,7.753019,-8.684946,0.146188,1.620112,2.912336,7.968008,6.360997,-9.702751,-2.461102,-7.945811,6.433418,-0.875586,4.389288,9.348295,-6.251447,-8.540114,-9.673264,9.536353,2.592043,-4.902485,-4.541472,-7.856249,0.161807,5.124324,2.141973,5.870902,-7.848560,1.592081,-5.348536,8.870010,8.452208,-9.103543,-2.874591,-1.766547,-8.930429,-8.772932,-8.454614,-5.487234,1.907139,-2.225311,-5.132702,3.237683,5.522306,-0.476969,-7.178076,-3.655132,3.358821,0.653048,-4.448386,-0.932326,-6.078838,7.068388,3.109927,-3.573119,-3.229610,9.152327,4.679963,8.559090,-0.851880,-9.114942,6.415327,-7.022783,6.399136,-9.154895,6.050731,-5.853733,5.876724,1.944800,-8.158093,1.008297,-8.480309,4.667630,-4.280677,-9.758528,-1.868624,4.676565,9.716869,-8.196393,6.988516,4.189679,1.274860,2.859024,4.000696,-4.985321,-8.720833,-5.070045,-9.158037,-3.393208,-7.525382,0.782667,7.140091,-6.627117,7.057809,3.347794,5.994602,0.709209,8.794679,9.115837,0.965625,-7.441655,-6.119666,-7.951768,-3.128491,2.389933,5.659975,7.824274,8.629623,-3.294128,-3.993471,3.897163,-6.892163,8.924649,0.362910,-1.679509,-1.715338,6.933750,-5.027330,4.536112,-3.305275,4.690419,-7.565794,7.967049,2.942909,-5.362833,8.408995,2.044285,-1.354070,3.013294,-1.684186,0.526190,-6.891996,2.164902,-6.250975,5.695891,5.372527,1.248647,0.043592,2.367532,-8.269067,3.493435,1.902971,4.224267,9.115672,-0.037270,-2.384044,-7.232315,-7.214549,2.106947,-0.518872,4.811740,-3.560453,4.528755,5.763439,-9.980842,-4.197846,-9.806674,-2.231331,-6.838028,-3.157644,4.563711,-9.270914,-8.719657,9.417480,2.913091,-8.087852,4.801853,5.801349,1.086289,5.273185,-5.621763,1.965120,-6.438161,-0.848438,3.709438,4.218617,-7.019766,-8.557666,-1.065515,-8.353669,1.752526,-1.164983,5.849638,-2.423872,4.757132,-2.734627,5.755938,-7.292706,-5.991901,-7.717794,2.217314,-0.913248,7.705920,-8.791381,2.841714,-1.936556,-7.284917,0.100828,-1.238316,-5.167621,-0.673665,-2.582972,-0.698958,4.897170,1.273971,-2.459850,8.946950,-9.704417,8.034995,-3.306413,-4.916861,2.232995,4.976538,-2.828211,-7.903805,6.973630,-7.416865,5.290814,-9.794708,1.935305,-1.488542,5.375312,-9.289797,8.271773,-9.953807,-2.904541,-9.262146,5.013807,3.114386,2.386604,-9.897729,-1.524937,-0.640979,1.938055,-5.631279,5.360801,-0.258575,-4.303170,-8.333688,-3.453291,8.839794,0.584427,8.891341,2.818884,8.090017,-7.664816,-3.013556,-4.735338,-3.166096,8.388291,-2.890515,-2.973105,0.919381,8.939280,-9.433367,3.971098,6.549685,0.253938,5.078273,1.893753,7.309392,6.410090,-6.907977,1.586961,1.785392,6.559067,2.639224,8.489795,-5.590499,-5.164692,-2.149279,-1.883123,5.063405,-0.482015,-8.700908,3.228359,-1.825195,3.308399,-8.505801,3.623842,-7.974454,0.452087,-4.586563,-0.085690,5.358244,8.318774,-2.564482,6.180336,2.089249,2.686943,1.437743,-2.722463,9.607698,-6.820814,-5.731489,9.347424,-8.896902,-5.844490,5.264996,5.659740,5.644968,1.160223,-9.221214,2.819918,-3.050881,-0.427452,0.715061,0.928809,-6.561276,-8.249446,-8.841116,1.436367,-6.122026,2.750652,3.529608,9.037418,-6.887762,-7.714900,8.453576,-9.947393,-2.365300,-1.017552,2.911694,-7.913688,1.549930,-4.043914,1.419310,0.872939,9.619965,3.569108,5.828235,-6.190478,4.278683,4.613293,-6.469856,1.891554,-0.413518,2.885778,9.528223,1.910087,-4.120715,-3.934242,-4.516248,-3.325106,7.847766,-0.729644,-3.814606,-7.670224,2.164387,-5.356599,8.274410,6.646454,1.604091,-8.616630,-7.500161,-4.240556,6.051007,-9.374971,-6.857148,-4.859490,6.413998,-9.836151,1.753498,5.868084,-5.691073,-7.757022,4.874779,2.030287,-1.221935,-0.352639,-2.948501,-5.263556,7.752233,7.911275,3.323855,5.274592,-3.718220,-2.550219,-3.291078,-2.839340,9.977421,4.268730,-0.058538,-3.330518,-9.439678,-8.157667,8.676485,-9.072419,9.361589,-9.308640,2.225191,4.793875,3.840869,6.455324,-8.345460,7.431819,7.890920,-2.022962,3.591640,-6.778842,4.037390,-9.057010,1.730891,-3.306813,-8.351306,4.815640,-1.309806,2.327990,-7.733049,-4.710769,1.057734,7.216750,-8.813939,-5.030037,-1.991965,7.049469,9.710887,-8.751041,-6.601223,-3.511775,4.012122,8.990214,-7.452931,5.873481,7.654614,0.711223,4.174180,9.014097,4.483450,-2.408553,8.824127,5.175168,1.717633,1.268040,-8.209348,5.957085,-5.841780,-0.667979,5.612149,6.472790,0.997172,9.542047,4.031494,-2.588051,0.865050,-7.407154,-8.288175,0.746737,8.980914,8.543292,-6.047328,9.968853,9.673494,-6.065132,-0.566812,-1.699360,-7.180463,-9.599393,-6.822033,-6.261003,7.753095,-6.930918,5.498517,-7.752250,9.678440,-6.695349,-9.977909,-1.240318,8.613076,-8.698789,-3.474166,3.733542,8.247705,0.629586,-1.897976,3.316564,-8.105523,9.009064,4.999540,5.126993,-3.838932,3.002671,2.460355,-3.106369,-5.336873,-0.006934,0.892041,4.543463,-4.840671,7.894669,6.344966,-1.111031,-0.415931,3.662566,0.119135,-1.326297,-1.603642,-0.462644,3.878215,4.008373,-5.576066,9.161182,6.336843,-8.840096,5.674573,8.398370,-0.306167,-1.282196,3.947426,-0.877873,-2.819515,-4.759393,-8.229237,9.752411,-3.790116,5.107225,-1.024331,-8.076529,-8.701024,4.534800,-6.573565,-0.975734,6.122595,-8.480407,-1.813696,6.415837,4.105451,3.860755,5.647293,-9.531678,5.294224,-5.144840,-5.496147,-5.831431,4.969195,-1.555862,-6.595193,-1.410020,7.056821,-2.521261,2.871597,1.874845,-3.608622,3.800553,4.960061,6.529948,6.699615,-8.120669,-0.602588,-3.888263,3.755590,-2.161040,3.534828,8.437852,8.007677,-3.371064,2.469644,1.949573,9.210292,7.984992,-4.278676,7.469467,-6.353432,2.032347,-6.227178,-6.558405,-6.278483,6.861933,4.172127,4.839606,0.841417,-7.552870,6.017349,-3.238129,-2.957302,1.843117,-5.049222,-7.980237,-9.378413,0.558108,-0.093556,-0.227223,-0.402236,-0.629579,-0.675388,-7.154124,-5.871494,5.734886,9.346688,-9.259926,0.463026,-5.069339,-7.327869,9.236085,2.809469,-1.924380,-9.094099,-1.139992,-6.736093,8.852189,-7.231272,-5.523655,-5.022401,-0.790506,4.996609,4.916949,-8.328635,-3.224613,-9.655839,-3.404278,1.921487,4.191784,3.545259,-5.324049,6.664736,7.358944,-6.300152,-5.771557,9.221342,-5.155006,0.233429,7.337367,9.099217,-6.781837,8.320366,0.400919,0.277845,3.720045,9.154817,8.566421,9.794911,-3.437636,-1.441447,-6.550519,-2.545916,5.064970,-2.797416,3.987818,-2.757490,0.534924,-5.670027,-4.537308,-2.052181,0.534204,-3.512806,-3.154336,7.508193,6.518167,3.809817,7.134165,-0.770445,4.547549,8.412918,-9.689818,-7.293941,-8.523939,5.565394,5.602037,-6.741695,2.172705,2.773429,-6.765964,-5.082526,-9.883932,3.251146,8.238436,-1.545829,-3.816549,-1.357070,-0.055109,-8.617456,2.911009,9.803878,1.575419,0.073027,-7.452135,-1.028409,8.670008,-5.038172,-4.171948,1.040009,7.424279,-8.141996,-2.386034,5.325204,-6.885416,4.239605,7.310630,-0.080801,-3.029399,4.366487,-1.181968,9.315234,-7.963915,1.249860,5.483616,2.448501,4.218850,-5.521306,-2.225125,-0.434278,4.533952,-8.292208,-5.227050,-0.538733,1.282998,-3.110748,3.970270,5.683992,7.681942,3.322729,-8.490462,-3.881920,-0.752653,5.460562,-9.442396,3.416707,3.239681,-6.646533,-7.474237,-1.220907,-0.976778,0.037857,-1.759619,0.138727,-3.693810,-2.564458,8.194636,-4.777454,0.254804,-6.239539,8.111504,6.895505,-3.828281,-1.024379,-0.986680,-5.402893,1.167200,4.382806,-8.968848,-6.931181,2.237891,5.947610,1.763971,-6.168492,3.062602,-5.497765,0.964436,0.483763,9.780291,-8.621720,-6.769151,-1.215566,2.542640,1.814594,-2.161326,-3.318562,-2.548961,3.738507,6.170357,-2.523048,-9.785767,8.609311,4.165546,1.028949,-6.485054,-0.793202,-7.256355,9.967522,-8.700716,-4.077250,-1.504303,-6.559754,-1.261529,-2.062701,-1.561351,5.023695,0.956672,-9.314298,8.161121,2.473507,5.583619,0.764505,-7.076296,8.611783,7.763026,1.940124,-5.071697,5.120785,3.705201,-7.721740,-4.889189,3.191966,-8.621376,-6.747228,6.843143,-3.642997,-0.053935,7.174871,-6.444571,5.568347,-4.706850,3.005277,2.958276,1.760295,-2.065259,-2.514255,8.570020,-9.500832,0.182012,-8.104833,-2.533567,9.071503,-2.121412,1.248815,-1.482451,-8.587111,2.559556,2.679720,-5.262866,-5.431549,4.270547,-6.129921,-7.304536,-8.240725,1.884541,-3.969709,5.321246,-3.205892,-7.417648,-5.089970,0.306586,6.514412,-6.858119,2.803207,-8.636534,0.011669,-0.057651,-8.872375,-1.659575,-4.904486,2.922154,3.087263,-6.544038,-3.534951,1.102767,8.896212,-6.559250,-4.187924,-9.498954,6.643411,1.399681,-3.569425,-1.962893,-9.915935,5.046914,6.453458,3.573705,-2.611490,-5.068350,6.046309,5.123128,-4.118323,2.122778,4.255339,-5.249449,-4.101923,0.331077,9.249571,-9.175674,4.157995,-4.884466,-9.121224,9.911083,-2.141582,-1.246222,-7.929847,-1.580552,1.138675,7.108590,5.526038,5.595685,6.101271,-5.972933,2.827816,-1.308472,6.173261,5.743377,-2.524892,-7.102824,-9.656949,-1.421653,-3.279170,-4.539058,1.341117,-4.375886,5.437160,-0.213146,3.654406,-9.159007,5.667560,3.802035,7.155367,7.754647,9.191078,-8.651480,-2.260194,-8.123476,-8.397062,-0.364397,-2.819799,-9.373984,-5.484283,-5.293557,-9.248232,-2.613679,7.515619,-5.652692,-2.583544,0.134970,4.465217,-3.617406,-6.111047,-6.599031,0.730441,-4.190904,-4.936556,4.480480,-6.497090,-9.845583,-7.574704,-0.147688,-0.939853,2.512124,-5.962940,-2.294347,-4.166711,8.104948,-5.120226,4.015616,-3.585662,5.495563,0.240821,-8.992515,5.527600,-4.178921,0.677382,1.995646,1.928721,2.227419,1.131364,5.384644,-5.779529,3.010733,-6.466243,-5.156878,-6.323337,4.092005,-8.588979,5.966548,-1.826642,-1.574141,9.912039,7.419754,-9.983722,-9.309278,2.685893,6.828464,0.864428,-6.101870,-5.329581,-6.377525,-6.966269,-3.018850,1.827866,-8.032914,7.948635,-7.549383,1.592349,8.794114,-7.731303,2.992000,0.728248,5.983827,3.546250,-7.605177,-0.370144,2.605155,8.049719,0.674455,8.338376,-8.767750,-4.485892,6.735564,3.775188,3.130888,3.933528,2.532892,-3.056082,8.284675,-8.967843,4.356217,-2.317839,8.807759,-7.573498,5.578769,1.231657,-7.101787,-3.127640,7.511781,-0.648206,2.292093,2.787158,-7.483116,6.638371,-8.466693,1.837304,-8.693114,-1.820098,3.775498,-0.234617,-4.278474,6.140460,-7.018927,4.814682,2.059166,-8.337380,1.687777,3.097797,0.086417,8.114559,-4.819159,5.160886,-5.560248,-4.040852,-4.790822,-2.363760,-8.041113,0.075522,7.936345,-6.438577,-6.932277,5.838937,0.367020,4.374653,2.210219,-7.427744,-7.298238,-0.383592,0.004233,-3.703759,-9.953290,-5.258471,-5.528877,1.431458,-1.125857,-5.171456,-5.437840,-2.316360,-1.905804,7.002556,-2.343097,4.490499,6.835358,-2.519551,1.627769,2.943040,1.316800,-4.853809,7.864916,-5.551408,-3.855184,7.940568,-3.155244,-0.269542,4.854765,7.790391,9.416216,-0.324115,-2.755178,6.990238,-3.867745,7.835954,-3.191373,1.101490,0.974852,-0.089036,2.014725,2.602758,1.914612,-8.084963,2.426892,5.514977,3.551416,4.735894,-3.943091,7.397787,1.124135,-9.370096,-0.164980,-1.272943,1.827921,6.266459,-3.413289,2.403656,-5.885802,-5.862614,8.812732,-1.680912,-0.032896,-9.969862,-9.761126,0.399998,8.000550,-3.030631,1.316589,9.735004,2.108904,6.180906,7.594449,6.346854,9.944298,1.646466,4.262843,5.797862,-5.445517,-3.837981,4.711344,-2.322483,-3.137122,-3.624589,1.067637,-0.862743,5.187117,-5.618488,-5.800316,-0.946018,-0.643971,-4.974743,-2.392020,9.587340,-9.499517,0.583039,1.629050,-0.625910,-3.596186,2.533930,-3.142987,-5.404450,-4.520339,2.838052,2.974288,-6.480191,1.934720,9.113272,-2.939687,-2.012028,0.191445,-4.016866,-0.446614,-8.828952,3.372297,-0.617000], dtype = "float32")#candidate|15538|(1920,)|const|float32
call_15536 = relay.TupleGetItem(func_11960_call(relay.reshape(var_15537.astype('float64'), [10, 10, 8]), relay.reshape(const_15538.astype('float32'), [1920,]), ), 2)
call_15539 = relay.TupleGetItem(func_11964_call(relay.reshape(var_15537.astype('float64'), [10, 10, 8]), relay.reshape(const_15538.astype('float32'), [1920,]), ), 2)
func_14169_call = mod.get_global_var('func_14169')
func_14170_call = mutated_mod.get_global_var('func_14170')
call_15541 = relay.TupleGetItem(func_14169_call(), 0)
call_15542 = relay.TupleGetItem(func_14170_call(), 0)
output = relay.Tuple([call_15517,call_15531,call_15536,var_15537,const_15538,call_15541,])
output2 = relay.Tuple([call_15518,call_15532,call_15539,var_15537,const_15538,call_15542,])
func_15546 = relay.Function([var_15537,], output)
mod['func_15546'] = func_15546
mod = relay.transform.InferType()(mod)
var_15547 = relay.var("var_15547", dtype = "float64", shape = (800,))#candidate|15547|(800,)|var|float64
output = func_15546(var_15547)
func_15548 = relay.Function([var_15547], output)
mutated_mod['func_15548'] = func_15548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13624_call = mod.get_global_var('func_13624')
func_13626_call = mutated_mod.get_global_var('func_13626')
call_15641 = relay.TupleGetItem(func_13624_call(), 0)
call_15642 = relay.TupleGetItem(func_13626_call(), 0)
output = call_15641
output2 = call_15642
func_15684 = relay.Function([], output)
mod['func_15684'] = func_15684
mod = relay.transform.InferType()(mod)
output = func_15684()
func_15685 = relay.Function([], output)
mutated_mod['func_15685'] = func_15685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13360_call = mod.get_global_var('func_13360')
func_13362_call = mutated_mod.get_global_var('func_13362')
call_15688 = relay.TupleGetItem(func_13360_call(), 2)
call_15689 = relay.TupleGetItem(func_13362_call(), 2)
output = call_15688
output2 = call_15689
func_15696 = relay.Function([], output)
mod['func_15696'] = func_15696
mod = relay.transform.InferType()(mod)
mutated_mod['func_15696'] = func_15696
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15696_call = mutated_mod.get_global_var('func_15696')
call_15697 = func_15696_call()
output = call_15697
func_15698 = relay.Function([], output)
mutated_mod['func_15698'] = func_15698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13565_call = mod.get_global_var('func_13565')
func_13567_call = mutated_mod.get_global_var('func_13567')
call_15741 = relay.TupleGetItem(func_13565_call(), 0)
call_15742 = relay.TupleGetItem(func_13567_call(), 0)
output = relay.Tuple([call_15741,])
output2 = relay.Tuple([call_15742,])
func_15754 = relay.Function([], output)
mod['func_15754'] = func_15754
mod = relay.transform.InferType()(mod)
mutated_mod['func_15754'] = func_15754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15754_call = mutated_mod.get_global_var('func_15754')
call_15755 = func_15754_call()
output = call_15755
func_15756 = relay.Function([], output)
mutated_mod['func_15756'] = func_15756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12987_call = mod.get_global_var('func_12987')
func_12988_call = mutated_mod.get_global_var('func_12988')
call_15762 = relay.TupleGetItem(func_12987_call(), 2)
call_15763 = relay.TupleGetItem(func_12988_call(), 2)
func_14560_call = mod.get_global_var('func_14560')
func_14562_call = mutated_mod.get_global_var('func_14562')
call_15766 = func_14560_call()
call_15767 = func_14560_call()
func_15754_call = mod.get_global_var('func_15754')
func_15756_call = mutated_mod.get_global_var('func_15756')
call_15772 = relay.TupleGetItem(func_15754_call(), 0)
call_15773 = relay.TupleGetItem(func_15756_call(), 0)
output = relay.Tuple([call_15762,call_15766,call_15772,])
output2 = relay.Tuple([call_15763,call_15767,call_15773,])
func_15775 = relay.Function([], output)
mod['func_15775'] = func_15775
mod = relay.transform.InferType()(mod)
output = func_15775()
func_15776 = relay.Function([], output)
mutated_mod['func_15776'] = func_15776
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15790 = relay.var("var_15790", dtype = "float32", shape = (2, 14, 10))#candidate|15790|(2, 14, 10)|var|float32
var_15791 = relay.var("var_15791", dtype = "float32", shape = (2, 14, 10))#candidate|15791|(2, 14, 10)|var|float32
bop_15792 = relay.power(var_15790.astype('float32'), relay.reshape(var_15791.astype('float32'), relay.shape_of(var_15790))) # shape=(2, 14, 10)
func_13360_call = mod.get_global_var('func_13360')
func_13362_call = mutated_mod.get_global_var('func_13362')
call_15808 = relay.TupleGetItem(func_13360_call(), 1)
call_15809 = relay.TupleGetItem(func_13362_call(), 1)
func_15241_call = mod.get_global_var('func_15241')
func_15244_call = mutated_mod.get_global_var('func_15244')
const_15811 = relay.const([5.939491,5.992539,-2.673518,-1.400480,-4.470058,0.881125,-4.920305,-3.361174,4.483356,7.960501,1.869782,-5.457251,3.537298,4.267700,-1.005182,-0.642206,-8.411570,-6.648663,4.507231,7.346615,3.479063,-7.236416,-5.368719,-5.021683,9.582439,6.049256,-8.973685,2.567073,3.491946,-7.420431,-8.990711,6.221577,-8.564576,4.026788,5.332905,-0.722678,-4.593480,-4.699083,3.457592,-2.877378,-9.032323,4.923931,1.269050,-9.176021,4.164366,9.491449,3.149580,6.110762,-9.281458,0.819942,0.431024,1.110693,8.898295,-3.791193,-2.203179,4.766342,-0.951414,8.585812,9.380800,-4.339298,-2.691460,-7.377872,3.874758,-8.542712,5.912001,9.522594,0.004295,-5.262943,-7.508128,3.727331,6.504284,5.621924,8.840395,8.956887,-6.880376,-7.393269,1.329113,-5.896328,-0.416696,1.590078,3.176396,-4.209171,9.118923,5.219934,7.294116,-7.918574,4.189070,-2.679529,-0.482751,0.555658,0.606670,1.796637,-9.684486,0.288939,-6.968376,-4.081977,4.802240,-1.995733,3.626668,-0.982467,-9.550836,3.993716,-7.743120,6.037143,-7.929127,7.376304,-8.119303,-3.726413,8.691733,0.517663,-5.641462,7.796069,-0.103870,-7.144227,0.721964,-4.754343,9.915756,9.858071,4.983535,-7.653815,4.645559,2.215640,8.265886,-4.408479,-4.347084,-8.249245,-0.108694,-3.684738,-8.454814,-3.849816,-7.389370,2.358366,0.118683,4.214953,9.716555,-5.137207,-7.963905,-5.663425,0.641023,-8.978263,-3.930583,5.691179,-0.642581,1.097640,-9.913605,-2.295205,-4.595889,3.223999,-1.294546,-2.376643,-5.585986,-4.941197,9.714391,-0.996677,2.626512,-2.375711,-6.344558,-6.110052,6.793845,0.807985,-9.933054,-8.517674,1.805536,-4.382089,2.700937,-1.727538,6.748102,-1.671990,0.595804,9.444157,0.293323,7.447033,7.867204,-7.356707,2.604417,2.182856,5.895513,3.488760,5.713930,-5.879292,-1.339790,-5.686609,1.918279,-3.546287,-0.124718,5.268447,7.971696,4.634588,0.109279,-4.309179,0.225826,-4.603414,2.290233,1.980833,6.947884], dtype = "float32")#candidate|15811|(195,)|const|float32
call_15810 = relay.TupleGetItem(func_15241_call(relay.reshape(const_15811.astype('float32'), [3, 5, 13])), 0)
call_15812 = relay.TupleGetItem(func_15244_call(relay.reshape(const_15811.astype('float32'), [3, 5, 13])), 0)
func_14926_call = mod.get_global_var('func_14926')
func_14932_call = mutated_mod.get_global_var('func_14932')
const_15826 = relay.const([[9.707285,-1.569762,-0.580050,-7.897319,4.872766,8.028640,-8.412984,7.888010,5.860452,-3.757870,1.703234,8.634621],[-5.426371,4.423371,1.171928,-9.719772,6.682043,7.439917,4.002179,-4.951601,8.111272,5.637260,5.056365,8.928058],[0.176705,-3.185622,-5.351226,2.876857,-3.070719,7.922631,8.211818,4.798019,1.273330,-8.759827,-6.308315,7.923762],[9.478969,7.581331,5.973599,7.133580,6.470140,-9.675387,4.991455,-4.975830,-9.332173,-8.410379,3.402344,-2.179481],[-4.418630,4.311068,1.253108,8.387241,-4.832688,6.596950,7.532627,-1.577511,-0.984637,2.879462,6.448796,-6.049527],[0.808401,0.760885,-2.001961,4.033345,9.203706,9.817686,-1.675606,1.987434,-6.595948,-7.990137,2.405860,-5.732613],[6.023097,6.856410,8.530359,-8.372298,-7.582196,6.941657,1.773528,-6.949808,2.545267,7.747787,-2.202199,-1.413386],[0.813659,-3.094445,-7.394680,9.284669,-6.557201,-0.676383,-7.790559,7.838283,-4.177030,4.445367,7.765557,-9.635145],[6.380120,-9.831410,-2.116116,-4.212026,-1.059948,-2.845985,4.953514,-7.867243,7.844803,7.456037,-8.831323,-8.144709],[7.697188,-5.571263,7.172182,-1.611150,6.764269,-3.465237,3.272930,9.422326,-7.327131,-7.846756,2.110002,7.022434],[0.600893,-1.811611,7.344965,8.166463,-4.879822,-5.240053,-6.893434,9.599838,5.169838,-6.708238,-0.465420,-4.096036],[3.404420,0.727844,-6.834800,9.385743,8.223295,4.349462,2.888115,-1.500978,-7.954271,1.858747,2.038979,-7.624511],[2.102743,9.505033,9.563130,-5.932190,5.439388,2.863460,-2.168485,5.666388,8.715351,6.311215,7.326893,-9.943342],[-3.479046,8.580306,-3.287664,-5.152160,-6.670520,-1.365813,-3.277994,-8.356639,-8.675867,5.094760,8.192532,-8.270479],[9.841306,2.326741,0.635746,-8.621554,6.940597,0.339503,-6.852524,1.662447,-0.791631,-2.991306,-7.249907,-9.556994],[-4.499206,-0.047427,-4.614750,-3.940614,-6.654098,4.339591,-2.462282,2.438373,5.173654,7.725984,-6.226266,-1.404151],[-6.543050,7.612846,4.382988,1.418168,4.334116,4.902307,7.312428,9.543931,4.011421,8.315423,0.152344,-4.241624],[-0.013524,-9.809350,-3.108793,1.184867,3.190476,-3.246728,-7.706465,-0.111546,2.009260,5.507540,-2.274443,-7.742933],[3.616194,7.064545,-7.314422,6.714648,7.323699,6.286868,-0.976134,3.727035,-1.926586,8.382253,8.365256,-7.162093],[3.840682,2.945206,1.698432,-2.135162,-7.249373,8.880327,4.046466,3.235292,-2.700231,-4.462131,1.822681,-3.961049],[9.691639,-9.262897,1.311640,3.762554,-2.703576,-1.474678,-0.611893,8.550782,-0.487187,8.277183,1.232884,9.145406],[-6.223373,7.855897,4.914870,0.714048,6.404638,7.099142,-7.093600,1.131801,-4.389856,-2.240127,-3.970212,7.375706],[-6.798497,-1.886394,1.552691,9.030843,-8.185968,1.367472,-5.092725,-2.408384,-6.302002,4.324397,6.539087,7.270362],[-6.919872,-8.893592,0.740949,-5.138677,5.507189,-8.968673,-5.214137,-1.127061,-4.341216,-9.148623,-6.384827,-5.005030],[-3.504372,9.026872,-0.889390,1.073106,2.041907,-5.261655,0.127747,-9.666078,1.829524,5.684052,3.337826,-4.161437],[9.840257,-1.707916,-6.799167,-4.741896,-2.508536,-1.876392,2.512142,-9.123459,0.429719,9.024471,5.821198,0.752504],[-0.931046,-0.450592,-3.614692,5.192795,8.656034,2.393592,-3.964676,-1.217704,-8.270284,-8.081298,7.259209,-9.652887],[0.076884,2.744461,8.174207,8.593225,-4.117322,8.802862,1.389893,-6.338072,5.105969,-9.638398,-8.025044,-4.461805],[0.093169,-4.477857,9.711611,0.035896,-8.493625,9.795826,-3.147366,-9.638027,-1.012952,9.149483,-8.542535,-3.621320],[-4.833079,-4.001705,-8.822410,1.674460,8.741135,-5.315606,-4.516022,6.295323,-9.551236,-4.801427,3.992295,8.129089],[5.864918,2.850785,2.962701,3.385097,-1.142789,-3.808904,-5.547567,-7.362904,8.673557,3.747676,8.934828,-7.625031],[5.020795,-4.468750,8.045084,0.622243,-3.457651,4.437521,-3.064981,8.548606,-4.756990,8.677088,5.393834,-0.864051],[-3.161298,-7.557224,-3.854172,-7.803708,-8.648486,-0.600565,-3.272833,-0.646250,1.966645,-6.887329,-1.858910,-3.001887],[2.127995,9.521116,-3.707236,0.915133,0.947010,-0.263393,2.867311,-5.252645,8.180179,1.787323,-5.530635,-3.723038],[5.243521,1.477478,7.080101,-8.779061,-7.169969,8.163907,7.325495,6.858547,2.350062,-2.702468,-0.284300,-7.772267],[-6.353589,-2.215809,2.057497,-4.521268,1.366026,-5.803793,2.213027,-9.831329,-9.468782,-7.112872,-0.929002,8.386808],[3.206143,-9.716415,-4.631905,7.590065,8.777339,4.647846,0.633152,4.302823,9.440771,3.493189,0.890048,-3.988405],[8.798208,0.486842,8.693222,3.105093,6.658360,-6.594716,-3.004521,-9.893184,1.795223,-6.185116,6.548910,-4.435542],[8.697360,1.352154,8.591633,1.842294,5.690606,-0.235763,8.456486,6.752832,-8.454264,-1.111612,-3.097232,-2.164221],[-6.452357,-6.080864,-7.387373,-5.179595,-3.265076,-0.826629,-8.698570,-4.345101,2.483160,-6.285565,0.985610,1.217591],[8.397979,-0.174183,-9.815079,-8.610456,-3.888791,-4.807497,7.425575,-6.275460,-0.568713,4.524673,-2.541632,-1.425744],[-5.104297,-2.957077,4.564485,0.500333,0.463551,-4.488321,-6.937837,-1.707005,1.321504,-6.604652,-5.269461,-0.668219],[7.422768,7.176812,9.111532,1.937420,-6.998553,4.369842,9.272030,-1.966301,5.110804,-8.856160,9.634426,-0.907026],[4.503298,3.645598,4.689565,4.515078,0.899751,7.366589,-3.726259,2.456070,-0.102891,-6.030322,1.621244,9.369444],[6.573656,9.835625,-2.060178,8.356811,-2.709337,7.851123,-2.843259,-3.397327,0.483364,7.001091,0.036607,-2.547355],[3.083459,8.547945,-7.822327,4.957114,2.484769,-5.575488,-9.299925,6.356252,9.755711,8.066859,8.156779,5.855600],[4.525988,7.030573,2.500150,-9.977422,-2.169047,-3.756401,-9.809267,1.165384,-6.905423,-8.577443,4.746199,2.687675],[-0.507792,8.998907,-6.516989,5.287970,2.507585,-3.263323,-4.001129,8.569331,6.078026,2.044112,-2.138341,8.385472],[5.692301,0.004487,5.986727,7.732671,2.215641,-3.113147,7.315438,3.558459,-4.148968,-3.936170,0.049588,9.012389],[3.145425,-6.425693,4.687165,-9.193694,3.040528,-3.751761,-7.894737,8.045833,-9.356266,4.112034,1.439277,-0.072233],[5.197245,-6.196459,-6.798074,7.555523,7.204542,1.324647,4.490784,8.367089,-3.054237,6.635380,2.175482,-4.302021],[-8.389797,2.807016,6.060763,5.308167,-9.290628,1.540468,-2.864684,-4.661155,-6.260647,-5.147149,0.311491,1.526881],[6.589951,-2.937967,7.824886,-7.794437,4.366620,6.499726,3.097509,7.072363,-2.990075,4.113467,4.615956,-8.437354],[9.670883,5.465158,-7.705855,-5.516894,1.692612,-8.147231,-1.273976,8.758039,3.130320,-5.124202,7.291299,-4.758437],[-5.208392,-2.340505,-1.485875,7.658160,-2.809711,-7.709911,4.613881,-1.581942,-0.493785,4.863999,-5.475071,-6.300766],[0.989370,-8.441561,-4.099575,0.320240,-4.211491,-4.892267,-0.952189,5.491958,-9.914228,-0.604533,-9.161755,-3.294969],[0.293733,4.737341,-7.813057,2.147087,-4.849808,1.843497,8.346372,1.486291,-5.466855,-8.094305,-8.089473,4.914271],[8.705603,-6.628999,6.998198,-2.617458,8.874185,-9.060410,7.453973,9.710906,7.524403,-8.871212,9.448450,6.885720],[6.009205,2.225814,1.664917,-5.316837,-8.426535,-9.680417,-2.362283,-9.768182,7.573100,9.696079,6.347954,-8.007428],[4.929994,4.080463,6.820808,0.679275,-3.834124,-8.128714,0.667792,-4.492304,3.000248,6.911625,-4.861011,7.257782],[-0.529044,-7.197854,-9.579636,6.804679,-7.680793,-1.331161,4.722123,-4.732138,-1.758621,6.142174,-4.785705,7.225430],[-8.575360,6.085691,3.563387,-7.140914,7.326020,7.716745,-9.072068,-3.854094,4.209589,-4.471602,-5.072584,-2.449396],[5.979007,-9.469923,2.166463,6.785009,9.159234,-2.635374,-2.898361,-4.310031,-9.677535,2.976243,-2.448123,3.223442],[-9.339961,-8.219195,-4.952142,-1.782467,-8.182305,4.348020,-4.837096,-4.162375,8.251264,-3.130808,0.034631,-3.945273],[-8.638223,-1.366898,5.110285,-7.580866,0.200971,-0.727411,3.000966,2.570453,9.478875,-9.733064,-0.949765,5.285639],[1.641633,5.290411,1.677645,-9.564836,0.081090,-1.899950,-0.004911,-4.253626,-2.515897,-0.422443,4.752761,0.143081],[-9.226597,2.932562,-6.853309,6.328150,-3.203767,6.689284,-5.208368,-9.448246,-9.992950,-4.471683,6.811847,1.378622],[7.743691,-2.898532,5.654232,7.583681,9.722604,-6.774960,-0.379693,0.700818,-0.081125,-1.928170,7.145948,-0.090600],[2.194723,-6.373187,-2.705649,-8.937190,2.554602,-7.285920,7.360179,3.112094,-8.440208,-2.352046,7.246439,-1.741627],[-4.203813,-6.495253,3.533331,-7.861746,9.496171,0.485737,-4.456594,3.727100,-2.368908,-4.530942,5.566158,-1.300993],[-1.397269,-5.727814,2.435243,0.637417,2.715734,0.180963,7.140053,-2.941249,-5.168409,-8.811269,9.564699,7.811190],[7.100669,0.969109,0.043687,4.902170,9.996098,4.457001,-5.896984,-8.745543,-9.107329,-3.140963,3.154189,-2.400944],[-8.818996,-4.636488,-4.007717,-8.063761,-1.062120,-0.847438,4.188439,4.119952,-3.495613,8.703793,8.874094,-8.255940],[9.736478,4.309815,3.030220,8.727566,-2.869798,-4.959771,2.349570,5.005142,-7.639571,4.488985,7.542180,-7.744877],[8.438605,-3.339087,-6.561031,-6.800550,1.123293,-7.766361,4.928438,-5.687467,-2.844858,-1.373830,3.146947,6.144146],[9.826825,-4.946520,7.694003,-1.063918,-4.625465,7.029287,-1.720754,9.437799,-2.075920,-5.198957,3.391832,4.428790],[7.352163,5.480499,3.481540,9.626682,8.494050,5.523276,-2.304566,5.887090,-1.239245,1.202955,-5.181409,-0.608325],[0.231182,-1.289518,-4.820137,-0.531592,7.620253,-7.010847,-8.635748,2.866004,1.412897,-9.005432,7.920435,2.894685],[-9.530003,-2.883918,5.230550,9.246182,5.630596,2.580916,-7.717043,-0.273984,1.646550,-5.117499,-6.401216,5.084602],[3.096854,8.606045,4.579754,-6.237614,-3.986983,-2.064721,-9.967530,-5.037585,2.054389,3.076269,2.974051,0.599370],[-0.596868,-7.362927,5.847463,3.569734,6.522729,9.904581,9.989217,-2.670935,-7.509880,1.360793,0.167153,6.572284],[6.744617,-2.667843,-7.311742,0.863343,0.074293,6.334043,7.334060,4.793682,0.772879,1.989197,6.447022,-5.625141],[-4.714585,-3.463875,3.489641,-0.177806,-2.668245,3.325886,-9.712688,3.783177,-8.899954,-9.979893,8.374989,-8.911861],[7.744457,9.015645,-1.382217,-6.126304,6.175831,-3.572261,-5.599763,1.235271,7.857096,0.983735,8.098238,5.889335],[1.567216,5.419942,-3.364052,-2.780803,6.743897,-4.155244,3.163197,-2.818367,4.806970,-6.839672,7.893974,-4.228731],[-4.432296,-4.427084,-1.070063,-0.585596,-9.325807,4.053011,3.910302,-1.396198,7.664110,-3.441669,0.127135,-4.681482],[0.019453,9.986385,-3.598399,9.109030,5.386088,5.804717,-1.597130,-4.548109,3.678892,0.215819,9.771738,-5.244014],[-3.247331,7.947474,6.031833,-7.491127,-0.505780,-7.679971,6.657101,-4.971315,0.727427,-4.066173,6.120400,-2.694778],[-7.687366,3.428484,3.228507,8.341613,5.417975,-0.113382,-5.359753,3.019780,-6.121662,5.622451,-8.248848,-7.141358],[8.213471,5.222218,2.654970,-5.681387,5.103369,7.016964,4.297982,-1.326174,-2.495241,0.078561,6.667896,2.805670],[-6.884030,0.411264,-8.719482,0.337205,-7.659110,-4.556297,-1.844767,-2.829811,5.900563,9.656975,-3.757229,9.055184],[-8.988019,1.498296,8.666491,6.824523,3.867896,-4.216949,-2.784170,-3.061022,-7.489978,2.222992,6.230016,-0.711123],[2.969286,9.172955,3.247610,-3.511980,9.784583,3.768861,9.360245,3.443485,7.441698,-6.076522,2.429165,4.203620],[-3.667645,-9.028204,-8.088421,-4.338882,-7.193403,0.872425,-5.892661,6.084906,1.455261,-3.332253,6.118237,5.127176],[-5.834440,5.442662,-9.375697,6.323055,7.943300,-5.172498,2.516198,7.602516,-8.284062,4.292350,6.675168,3.768793],[-1.692376,6.823633,8.885544,-4.265563,-1.870977,6.167659,-7.909050,8.990603,-0.270595,9.959351,-4.237970,-8.329130]], dtype = "float64")#candidate|15826|(96, 12)|const|float64
const_15827 = relay.const([10,7,-10,5,6,-1,-1,7,-4,-1,3,10,-1,7,-7,-5,10,6,-8,-2,-2,3,9,5,-2,2,-2,-7,5,6,10,-10,-1,10,7,6,-6,3,9,-9,-2,8,-7,9,-1,-3,4,1,10,-7,-5,8,-9,7,9,-1,-6,7,6,-3,-10,-7,-2,2,-2,-10,-1,8,-1,10,-8,-3,1,-8,-5,-5,-9,-9,-3,-2,-9,1,3,10,4,-4,-2,-9,-6,-2,-9,-5,-9,1,7,-6,8,-8,7,-4,9,-3,2,6,8,8,2,6,-10,-1,2,7,5,8,-5,-2,10,-7,-9,2,-10,-5,-6,4,-7,6,4,-9,9,2,-2,10,4,-6,-10,-8,-1,-5,-3,-2,5,2,-1,2,-10,4,1,-6,1,7,10,-4,-10,7,-9,8,7,7,2,-8,4,-6,5,-1,4,10,7,5,4,-3,-1,8,10,7,-3,-4,-8,3,2,2,5,-10,-7,-10,-6,-5,-1,-6,6,-4,-8,-7,1,-2,7,-9,-7,5,-5,-4,-7,10,1,10,9,6,2,-6,5,-6,-1,5,3,1,-6,-8,5,2,4,-3,5,2,3,10,7,2,-10,-7,8,10,-6,-6,6,7,9,-3,-1,2,7,4,8,4,-3,-1,-1,-5,-9,8,-9,3,6,2,5,1,-8,5,-1,3,2,-4,-3,1,-10,-7,-5,6,-8,-9,4,6,7,5,-2,3,-10,-10,8,7,10,6,4,-9,2,-7,1,6,5,-7,10,3,-1,-7,4,-8,7,2,-7,6,-10,-6,6,-9,3,-10,-8,-5,5,7,-5,4,8,-3,-8,6,10,6,-4,-9,-1,-10,-1,5,8,-5,-6,4,8,2,-6,1,8,4,-10,-9,-9,9,5,-7,-7,-5,-3,8,-6,-5,-9,-8,4,1,4,-7,10,-4,10,-7,4,-10,10,-10,10,-1,-4,10,-3,-3,10,2,8,4,-9,-4,4,4,4,2,-9,-7,-4,-10,7,-5,-5,-6,5,10,-2,9,-10,1,6,10,-8,8,-3,8,4,-8,10,-2,5,-1,8,-2,-4,2,8,-5,10,-10,-2,4,4,4,5,1,10,6,5,-4,-5,-10,2,-9,9,-7,10,6,5,-7,10,2,-3,7,10,-6,-10,8,-2,-4,6,1,-5,9,-10,2,-6,7,-3,-7,6,8,2,7,2,-4,-5,6,3,-1,4,1,8,-9,-4,5,-2,7,-8,-7,-8,-9,-5,2,-10,2,-8,4,-3,-8,1,-9,8,-6,-10,7,5,10,10,-9,7,-6,4,-1,-5,8,-4,-9,-10,-9,10,-10,-3,-5,2,-5,5,2,-1,10,3,2,-4,-2,-7,-7,-8,-2,-5,3,-2,6,10,-1,-2,9,-9,-5,-1,7,7,-7,-9,3,9,-1,4,8,-7,9,10,-5,6,-1,-6,-6,-10,-5,5,5,3,3,-3,-5,2,10,-9,-2,-6,5,9,2,-6,10,-4,-5,1,6,1,-6,5,-6,4,1,-10,9,-8,1,-9,-7,-8,-10,10,-6,-9,-5,-10,-9,10,-4,8,2,-6,2,-5,-8,1,3,8,-2,2,1,10,-6,-2,3,-4,6,9,7,6,9,5,-9,-9,-8,-2,-3,-1,-5,9,-4,4,-5,9,6,-7,-5,7,3,-8,-9,2,-3,10,9,-5,-4,-5,1,-9,3,4,-8,3,6,-4,2,-6,-2,-2,-8,6,-7,1,8,6,7,9,-10,-7,-4,1,9,-10,8,4,8,-7,2,2,7,-1,-8,10,-3,-4,7,2,7,-1,-3,-10,-6,7,-5,9,-8,6,1,6,2,2,7,7,7,10,2,10,-7,5,-5,-5,5,9,-9,1,-4,1,6,-9,8,10,9,10,-6,-9,-1,5,6,-3,8,-6,-4,6,-7,-2,4,6,1,-9,-3,1,-3,-2,-8,-3,9,-1,-6,-5,-3,9,7,1,3,9,8,-2,4,-9,-8,-3,2,2,-10,-3,1,2,-7,-10,-5,-8,8,-4,-3,9,7,-10,3], dtype = "int8")#candidate|15827|(768,)|const|int8
var_15828 = relay.var("var_15828", dtype = "float32", shape = (96, 2))#candidate|15828|(96, 2)|var|float32
call_15825 = relay.TupleGetItem(func_14926_call(relay.reshape(const_15826.astype('float64'), [1152,]), relay.reshape(const_15827.astype('int8'), [768,]), relay.reshape(call_15808.astype('float32'), [975,]), relay.reshape(var_15828.astype('float32'), [4, 48]), ), 2)
call_15829 = relay.TupleGetItem(func_14932_call(relay.reshape(const_15826.astype('float64'), [1152,]), relay.reshape(const_15827.astype('int8'), [768,]), relay.reshape(call_15808.astype('float32'), [975,]), relay.reshape(var_15828.astype('float32'), [4, 48]), ), 2)
output = relay.Tuple([bop_15792,call_15808,call_15810,const_15811,call_15825,const_15826,const_15827,var_15828,])
output2 = relay.Tuple([bop_15792,call_15809,call_15812,const_15811,call_15829,const_15826,const_15827,var_15828,])
func_15832 = relay.Function([var_15790,var_15791,var_15828,], output)
mod['func_15832'] = func_15832
mod = relay.transform.InferType()(mod)
var_15833 = relay.var("var_15833", dtype = "float32", shape = (2, 14, 10))#candidate|15833|(2, 14, 10)|var|float32
var_15834 = relay.var("var_15834", dtype = "float32", shape = (2, 14, 10))#candidate|15834|(2, 14, 10)|var|float32
var_15835 = relay.var("var_15835", dtype = "float32", shape = (96, 2))#candidate|15835|(96, 2)|var|float32
output = func_15832(var_15833,var_15834,var_15835,)
func_15836 = relay.Function([var_15833,var_15834,var_15835,], output)
mutated_mod['func_15836'] = func_15836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14400_call = mod.get_global_var('func_14400')
func_14401_call = mutated_mod.get_global_var('func_14401')
call_15846 = func_14400_call()
call_15847 = func_14400_call()
var_15856 = relay.var("var_15856", dtype = "float64", shape = (12, 6, 11))#candidate|15856|(12, 6, 11)|var|float64
bop_15857 = relay.greater_equal(call_15846.astype('bool'), relay.reshape(var_15856.astype('bool'), relay.shape_of(call_15846))) # shape=(12, 6, 11)
bop_15860 = relay.greater_equal(call_15847.astype('bool'), relay.reshape(var_15856.astype('bool'), relay.shape_of(call_15847))) # shape=(12, 6, 11)
output = relay.Tuple([bop_15857,])
output2 = relay.Tuple([bop_15860,])
func_15861 = relay.Function([var_15856,], output)
mod['func_15861'] = func_15861
mod = relay.transform.InferType()(mod)
var_15862 = relay.var("var_15862", dtype = "float64", shape = (12, 6, 11))#candidate|15862|(12, 6, 11)|var|float64
output = func_15861(var_15862)
func_15863 = relay.Function([var_15862], output)
mutated_mod['func_15863'] = func_15863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13017_call = mod.get_global_var('func_13017')
func_13019_call = mutated_mod.get_global_var('func_13019')
call_15900 = func_13017_call()
call_15901 = func_13017_call()
output = call_15900
output2 = call_15901
func_15908 = relay.Function([], output)
mod['func_15908'] = func_15908
mod = relay.transform.InferType()(mod)
mutated_mod['func_15908'] = func_15908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15908_call = mutated_mod.get_global_var('func_15908')
call_15909 = func_15908_call()
output = call_15909
func_15910 = relay.Function([], output)
mutated_mod['func_15910'] = func_15910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14560_call = mod.get_global_var('func_14560')
func_14562_call = mutated_mod.get_global_var('func_14562')
call_15945 = func_14560_call()
call_15946 = func_14560_call()
output = relay.Tuple([call_15945,])
output2 = relay.Tuple([call_15946,])
func_15948 = relay.Function([], output)
mod['func_15948'] = func_15948
mod = relay.transform.InferType()(mod)
mutated_mod['func_15948'] = func_15948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15948_call = mutated_mod.get_global_var('func_15948')
call_15949 = func_15948_call()
output = call_15949
func_15950 = relay.Function([], output)
mutated_mod['func_15950'] = func_15950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14061_call = mod.get_global_var('func_14061')
func_14062_call = mutated_mod.get_global_var('func_14062')
call_15951 = relay.TupleGetItem(func_14061_call(), 7)
call_15952 = relay.TupleGetItem(func_14062_call(), 7)
func_13470_call = mod.get_global_var('func_13470')
func_13472_call = mutated_mod.get_global_var('func_13472')
const_15954 = relay.const([-2.985400,3.039875,3.972358,-1.777026,-7.354441,2.170321,7.600766,6.443176,4.303506,-4.994134,4.142364,-6.922582,8.100826,6.570013,-2.890372,-4.605978,-9.900988,3.263161,0.667067,-2.968197,-1.533377,-6.119650,-5.335422,-4.257118,8.074613,-3.394424,-7.278090,-8.233088,-4.763495,-2.885358,-1.848223,4.748706,-3.138681,5.903432,0.502893,2.881696,0.858413,3.508672,-5.179548,3.748014,-9.915630,-8.566597,-6.974589,-8.449729,4.416162,1.575526,-9.630264,-9.942485,-3.885843,-9.732901,4.561849,1.796616,9.756628,-7.733457,0.439986,2.529066,-6.854843,-3.041638,-3.478506,8.736312,8.152671,-8.782043,-5.773876,0.247544,-7.632193,-8.269489,8.265762,-3.814182,-1.937949,-4.001068,-1.842470,6.560483,-7.634020,3.979370,-3.097964,-7.693038,-3.059347,8.769609,5.018354,8.302164,-5.483786,7.491066,3.656896,-8.498916,-8.618067,2.784427,-4.427749,6.755087,-2.588995,-6.057459,-1.808536,7.663230,9.448369,1.600701,4.710818,-3.832372,-6.499918,6.418847,4.104180,6.890918,9.474127,-1.708543,5.134632,-6.737184,-4.898386,-8.781769,9.509640,8.361829,9.557742,7.502945,3.303056,-4.848958,0.771170,-5.267911,-0.088797,-9.368134,-1.787394,2.479744,9.043247,-9.539902,-6.618316,-5.260375,-5.714743,-8.887915,-6.690005,-7.633510,2.094338,2.511357,-7.381215,5.104218,7.948310,-9.374778,-9.749646,3.331649,9.608656,-1.831324,-6.555383,7.609472,-4.361395,-2.191070,9.387048,1.172072,-8.535129,0.443296,-5.449979,9.210586,7.853357,4.160099,9.596692,7.100838,-9.980968,5.574747,-9.908055,1.436493,-0.757494,3.520464,-6.107615,9.142530,4.632025,-8.855781,1.084530,2.007377,1.338172,8.722914,5.239723,-5.561770,-2.957383,-7.666471,-8.198635,4.182454,-6.359963,3.223713,8.194924,7.119636,9.722366,-6.188355,9.975308,0.920828,5.394671,5.436205,2.666028,-0.693959,8.441425,-5.809542,9.075514,9.080898,-7.817887,-4.868815,6.325825,-4.254679,5.507360,0.522270,-8.115630,-3.559278,3.436021,-4.870843,0.835621,-2.688455,-4.036836,-9.216347,0.876411,6.768036,-1.413318,7.352426,3.451601,1.867879,1.341362,9.032689,5.738177,2.639790,5.903601,-7.554998,-0.629310,-6.953762,4.052327,-0.194973,-6.937612,8.113271,-6.132308,-3.468894,-8.057758,-2.744256,-2.848116,-2.989416,6.535518,4.688571,2.633238,1.647354,-2.916006,-3.818684,9.548696,-3.594604,-8.869853,-9.934046,2.032411,-0.243380,-4.798689,8.543884,-5.945689,4.937911,4.579700,6.799751,-5.284994,-7.894266,-8.659073,-0.272870,-0.211857,1.377537,-3.147479,0.243334,-5.653038,-2.070004,-8.255586,9.079706,4.167519,0.192423,9.807037,5.700083,2.506595,8.297042,8.601956,9.082485,-6.258886,-2.739227,0.089817,-0.932530,-3.463518,-9.150357,-9.591260,7.161455,-1.150103,-7.116162,9.535616,2.776789,-4.101907,-9.037071,1.077445,4.983789,-6.582200,-8.487957], dtype = "float64")#candidate|15954|(280,)|const|float64
call_15953 = relay.TupleGetItem(func_13470_call(relay.reshape(const_15954.astype('float64'), [280,])), 2)
call_15955 = relay.TupleGetItem(func_13472_call(relay.reshape(const_15954.astype('float64'), [280,])), 2)
func_9294_call = mod.get_global_var('func_9294')
func_9297_call = mutated_mod.get_global_var('func_9297')
const_15968 = relay.const([[7.460378,-2.661619,6.274625,0.581088,-3.616720,2.534747,4.042663,-8.767959,-2.446430,0.451130,-2.646075,-8.870328,3.092748,7.066750,4.657051,-2.283600,8.235169,4.053181,-6.691496,4.510317,-1.899609,0.399718,4.250904,0.840390,-1.019145,-7.118622,1.801086,9.941700,-7.570356,-9.170544,-2.927258,2.770719,9.211464,-0.259678,9.992526,6.035598,5.934380,2.171653,-4.537371,-3.065486,7.173664,7.066168,0.291152,8.802870,6.354666,9.573397,3.565379,-8.520010,-7.667528,-7.193992,-2.012844,7.516328,-0.490806,-8.782947,3.643538,-9.058369,-5.047078,7.904027,-9.689325,4.732543,-2.113657,2.850277,0.336463,2.428085,-7.720730,-8.904648,5.250125,-3.642764,-9.542985,-0.538100,0.569254,1.993148,-8.582199,3.237231,8.169451,0.588710,-6.654386,1.108378,-2.465548,2.712388,2.477293,8.791794,4.069812,-5.135721,2.107450,-4.593200,0.577442,-7.829094,-7.164793,-2.402841,-6.650283,-5.558523,-7.377662,6.450327,-2.268747,-3.750945,-8.579339,-3.191573,1.564310,5.111565,0.008122,-6.910374,6.661918,-2.666248,-5.617538,-2.734538,-9.672256,8.718553,-6.084763,2.401612,1.683329,-1.408447,-6.184369,-1.068390,-8.152886,-6.596385,7.817199,-4.167779,3.451495,-9.169156,-3.925487,-6.589586,5.473578,9.944023,-4.997859,-9.713782,-6.042001,7.878342,9.485564,0.643438,-2.324893,4.328350,-5.539243,-7.881530,9.530515,5.739511,1.181746,-6.454845,-6.228396,9.276302,3.998892,-5.847696,-9.991188,-5.896414,9.265035,2.818238,5.089656,1.679933,6.745324,6.133768,5.048393,-6.564807,-6.341783,5.125616,-3.990628,-5.919963,8.244530,-8.243151,-5.926397,2.266036,-5.635651,0.380031,-7.515269,2.676578,8.428476,-4.160996,9.896858,7.742580,1.582725,-3.786499,9.215812,8.741603,-3.868516,9.803240,-2.420488,-3.098391,3.095894,-0.161221,1.681395,2.553150,-6.443433,9.924999,-2.544252,-7.111312,4.307803,-2.499025,6.758316,8.765085,6.023776,-0.898114,-7.328100,-9.837370,8.948527,1.411370,-4.101090,5.915407,-5.347000,-6.848909,2.992789,-1.100982,-5.039534,-9.127288,7.290254,9.509329,-0.996134,-1.648477,-2.911810,-9.515089,-1.184761,-0.622858,0.497341,8.099952,-2.814460,-8.635630,-4.455361,8.200877,0.756016,-3.527358,7.255344,5.403765,-5.362889,-9.233381,-0.008364,-1.485483,-0.931192,5.078807,-1.203899,7.290672,3.196224,-1.484571,7.374285,-1.132477,7.629439,9.632347,-7.409738,-4.025060,-8.353313,0.557756,-5.061518,0.024034,3.340807,-2.067404,-3.398907,-5.212987,7.705693,0.085787,-6.144649,-9.059016,5.024376,8.356355,-1.686365,-2.939544,-0.794864,-1.891323,9.717557,-8.920545,-9.131617,-2.927343,-1.999868,-1.250365,2.441901,-1.111909,8.940895,-4.557784,-1.892885,-6.126890,8.107422,-6.782199,2.643732,-5.125790,-3.402497,2.382343,3.302670,9.066282,-1.332831,-7.244518,-2.975321,-5.648606,2.698647,-6.229064,-5.627183,-1.251454,3.030958,7.292939,3.652103,2.559404,-3.333846,6.940910,-7.362611,-2.760030,-2.665133,-1.416135,6.144604,5.383454,1.663584,8.176957,-0.259359,-0.050333,-3.619902,-3.843553,0.457900,0.954960,-1.586762,-6.937965,-2.850147,-7.910560,5.685554,9.290238,4.864050,5.260211,-1.230659,-7.230921,-8.350866,-5.671846,-3.195202,4.964109,-2.196059,-6.812711,9.866085,1.311879,7.742519,-8.875920,-4.077999,6.471058,-4.038475,8.657327,4.836467,-7.703917,-5.554296,-0.758425,0.160895,-6.713826,6.887452,1.959227,9.357933,-5.963402,-6.211065,5.517751,-5.882296,-7.687772,5.616656,5.789956,0.876599,2.750910,-5.797862,-8.141490,1.259824,7.458930,9.799289,5.064314,9.602337,1.457014,-7.278029,-2.235411,-4.448028,-1.961443,-8.551353,-9.466719,2.637822,5.323220,-3.688949,6.668675,7.732545,-0.932602,1.709201,8.000493,8.493597,-5.622725,-7.299457,-0.172551,7.158373,-8.417996,-5.639135,6.364525,-2.657088,3.761706,5.368493,-8.339512,2.543550,0.189829,-1.247650,8.200224,-9.321832,-2.582352,-6.526130,6.558556,7.357272,-8.117179,-8.062893,9.803615,-7.896879,9.171691,5.279837,-5.430003,-4.410027,-2.830106,8.544043,-1.182972,7.639564,-4.834897,1.934709,-2.782612,9.267660,-9.232814,-2.041505,6.812964,-1.619775,-9.118215,-3.209388,-1.001874,8.878135,-3.314900,-2.841952,-7.247622,3.066004,-7.155514,-7.566753,9.336385,7.075216,5.917696,9.638675,-4.337921,-4.056747,8.733584,-6.777040,6.515088,-4.592288,-3.534727,0.193456,6.694912,6.468104,1.620077,-7.055519,5.316410,8.817746,3.630688,4.885962,-2.837951,6.168702,6.195577,-0.809404,8.199230,-6.206872,9.603231,-7.207959,-4.386269,-0.744832,7.194116,-1.190765,-8.395350,2.866951,-3.799732,-5.594927,-8.697093,-9.570853,4.011398,4.095969,-9.688554,-0.985958,1.588833,-0.295444,-0.980857,5.096775,7.736904,-9.603274,7.033891,0.669249,7.544265,6.737471,1.884780,0.238131,-3.708371,3.780176,-5.376486,-7.261871,-6.429543,4.058293,-9.086212,-5.738396,-5.417341,5.800159,2.494648,6.037931,-2.918925,-9.881683,-0.669280,-8.380047,-2.379289,3.625080,3.065457,-8.219469,-9.310802,-7.294481,9.924556,-5.357685,-1.327279,7.498348,2.697064,-6.817592,0.799798,1.681855,-3.028183,-6.637709,-1.180218,3.090309,-2.958659,1.102469,8.687723,7.591323,0.678701,-2.723268,6.325619,4.415662,-2.867319,8.534015,-1.393856,9.863411,-3.194966,-5.181930,-5.552206,4.543070,4.926142,3.166791,-3.426297,7.475447,3.648211,1.031512,-2.938605,5.877461,-3.296139,-5.034929,0.555700,2.724976,-2.798804,-1.225029,9.303792,5.994179,7.009330,6.801345,0.909598,7.278371,-5.544037,6.375776,4.704115,5.056246,7.925790,-3.706803,-7.003167,4.731872,6.931277,1.714940,7.466773,-0.812095,0.186644,-5.977276,-5.215251,3.028902,1.596102,5.592817,7.083554,-1.940815,0.411080,-6.943037,7.218185,-9.751013,8.360799,6.546223,-6.217297,7.038591,-3.332718,-8.445512,0.058690,9.750168,-3.841687,0.655626,-9.018014,4.689589,5.347285,1.559275,4.471893,8.689011,0.777860,5.841940,-6.947163,3.839340,-0.842090,-5.705255,-7.252250,-9.836650,-4.196682,-4.837811,-9.267817,-0.569107,4.467190,-7.296908,9.239038,-8.955984,-5.588317,-1.524994,-3.623517,0.884711,9.031020,5.770153,-7.617290,6.771558,1.846126,9.340105,5.512551,1.589653,6.978328,7.905278,-8.969546,8.803841,6.329217,0.231494,9.004787,-9.793395,-1.586944,-5.168781,-9.096819,-2.375243,-8.429368,8.036237,4.487598,-4.871081,-8.294282,-1.833360,3.115956,1.999623,5.599595,3.149844,-3.136386,-7.310547,0.418443,1.841173,-8.440211,9.486048,1.408607,-7.788222,-6.334210,5.210917,-8.900065,3.136415,1.643992,-7.767198,2.338736,4.434397,7.665059,7.821951,8.442557,-5.445966,-3.787616,-6.544320,-9.872732,-9.049041,2.092497,7.468246,7.124081,-8.292137,-1.709069,-2.276027,-2.024733,1.360833,6.520055,-0.044765,6.516114,-3.116349,-2.045256,4.979189,3.534289,8.565841,7.691849,-9.560913,1.309662,2.604441,1.122213,-2.715316,4.020195,8.898199,-7.295114,6.434677,1.572827,8.171640,-5.093621,-5.959420,-0.850762,3.019078,2.279542,7.174650,-5.748395,-5.664505,-7.073941,3.676727,-5.635049,-7.384521,-2.889203,-6.977501,5.894680,9.641782,-0.589541,3.322212,-4.364245,-5.315957,-1.580946,-9.623793,-2.405090,-7.783147,2.862708,-4.495874,-6.154054,-5.965195,1.325216,-5.438542,-8.145080,-5.480578,-7.887897,-2.402802,-6.486172,-0.353898,-6.587104,5.732286,7.683032,2.830131,4.604709,-2.841265,-5.928022,-3.480228,3.211536,-3.324304,5.153068,-1.136205,-5.139937,-7.949696,7.231353,6.686717,3.746303,-3.475495,-4.138740,-3.306547,8.351436,3.415765,1.250504,8.797459,2.523804,9.330868,2.193469,-4.875103,-1.301913,-6.977417,4.923026,8.817790,1.892722,8.398297,1.537206,9.612655,-8.254217,-6.505895,9.256695,-8.527555,9.861130,6.179271,7.562072,-9.309787,-0.218288,0.630707,-4.660192,-4.475274,-7.200763,0.025268,4.238213,-8.554090,9.991442,-0.130973,0.411244,9.836351,-6.428722,2.929829,-3.500977,0.583708,-6.294711,-8.030994,4.106617,-4.464037,-4.664245,0.984908,9.525558,9.136435,-2.669229,9.813815,-6.525138,-5.319291,8.477380,-5.860868,4.911036,-9.422566,-0.755503,-6.896005,8.034408,3.777348,-9.638370,-6.796488,1.299315,-8.229288,2.316149,2.300733,0.358097,-2.556656,9.447817,-9.392274,-9.647475,-5.686331,-6.333374,-7.033601,-8.704123,5.688007,-8.980932,-7.241689,-3.110252,4.181263,-4.724483,9.033165,-3.169335,-8.657978,0.415647,-8.207746,7.660901,-4.705534,5.544140,4.788230,3.031467,-4.971973,-4.093747,9.999647,7.684300,-3.109938,4.147702,2.748725,3.657798,1.944337,3.089360,-0.540207,-6.134613,-5.550539,8.431403,9.266222,-5.543000,-0.236532,-8.700915,9.846958,-1.206069,0.457362,-9.060499,5.809726,-0.334318,-2.079319,-0.459518,-0.405991,5.459099,-6.308044,7.240104,2.100920,5.231559,-0.034207,4.947956,-4.680770,-7.478532,7.873562,-8.417570,-6.110320,5.434325,-3.751899,-6.697875,8.958674,9.523676,-6.009615,7.015471,1.192982,-5.226219,8.663681,1.462131,5.027869,5.544205,-9.725019,-3.978567,5.248610,1.138282,6.388866,-4.452072,-2.081664,7.543678,-7.608439,-1.915254,1.187583,-3.651966,3.112484,-1.567784,3.409774,3.576495,-2.070030,-9.904091,-0.192572,5.117309,5.765202,-5.661506,-8.995160,9.158426,-5.249303,-5.512399,-0.684430,-0.563433,-5.495395,-7.434550,8.280594,-4.877351,2.569614,2.947806,-6.585147,-1.217481,-7.302482,9.903970,-2.937925,-0.823562,6.525788,-2.521999,2.817712,2.021402,-9.801262,5.217783,8.462835,1.188081,-8.788860,-1.065552,5.054512,0.346652,9.562226,-1.750484,4.813608,7.121616,6.291900,-5.646742,-8.891256,6.549370,5.450588,-4.609743,-6.160091,-8.280613,-6.412484,8.175478,7.468720,-3.694281,-2.463502,-5.798539,3.371589,-0.413223,6.922000,9.379808,-0.892800,-4.283983,5.676099,-2.180761,-5.097422,-9.417442,-3.474633,3.530244,-2.950483,-5.957828,-7.672845,-0.752355,-0.090585,2.192671,4.304781,-8.031252,5.601146,-3.156709,2.426834,-9.191106,1.641039,8.477355,-1.501142,4.164998,-0.037867,3.523401,-3.194837,-3.767202,-5.532730,-0.218924,-1.545805,5.985111,-7.817952,-1.463859,0.295897,7.249252,2.182976,-2.606783,0.032671,5.605937,4.468485,1.354058,-9.602985,2.477190,7.764318,8.768711,-8.188848,1.396652,-9.399748,-6.626137,-4.013874,-9.425208,-3.317473,9.775035,-8.341484,8.014608,-0.675913,9.101722,-7.856905,0.352978,-9.270460,9.749307,-8.218499,9.821988,-5.493935,-6.757639,-1.737258,3.848559,4.837127,-8.152817,9.914965,7.251484,-4.128266,-0.404025,5.273505,-3.674096,-4.948295,-1.273754,-2.037142,2.141758,-2.933438,5.336724,-2.748115,0.795230,-6.010525,1.039012,-1.020478,1.037118,7.666398,7.807879,8.075691,3.074464,-7.468522,-6.531502,9.860028,8.955600,2.748855,-8.204160,9.480120,6.240405,-5.148957,4.940304,-5.250227,9.041416,0.503733,-1.284115,5.863916,-5.990788,-3.374288,-2.681658,9.855776,3.759183,6.209189,-3.749810,1.202885,-8.636011,0.032093,-3.354871,-1.366681,5.903859,3.480958,-8.247347,2.615606,-6.789896,-9.071117,-1.385343,-3.902781,-5.571428,9.723116,7.420874,1.497033,-2.025611,1.578889,-6.417429,3.261864,3.688692,7.736915,4.838677,3.628782,-0.493994,-2.236321,6.718464,-5.714489,-3.716508,-1.042853,2.099648,1.371904,-8.385231,-5.868334,-3.536280,7.416342,-1.089513,-5.378143,2.679617,0.318166,3.876756,-0.334777,2.866400,-9.646922,0.883684,0.088486,-0.282868,-3.830589,4.461875,7.448698,-9.964194,-5.904463,-0.022428,-3.028528,-3.496393,4.073826,-1.267828,-1.350933,3.140032,9.987514,8.962384,5.941343,-1.190456,1.859695,-3.088641,5.572563,1.792166,-1.850928,-0.243980,2.690435,-7.100766,-4.638217,6.229747,-7.679010,-6.742716,9.324307,-5.904534,1.501623,-1.059667,6.786958,-1.186317,-3.488888,-4.445484,1.536656,0.734801,3.205422,5.230927,-8.584321,-9.528254,0.258009,5.728747,-5.157911,6.332573,-0.810005,-6.817030,7.235007,-9.736999,-3.028094,-3.110360,-6.110182,6.504947,4.960525,4.566767,0.075249,4.249625,-7.034299,6.162203,-1.393762,0.346210,-5.780128,-2.292104,-0.082467,4.267494,4.256619,-5.168930,-5.087684,6.178219,-8.930784,2.596707,-6.786975,6.415745,7.466432,-2.088337,6.791581,-0.144001,4.210579,5.299225,-6.908775,4.930355,-6.069433,2.062199,7.966588,0.832146,3.559451,4.204879,4.710535,5.924280,6.314313,-8.147882,9.859404,-1.081590,-2.677920,-9.207724,1.198183,-2.192427,9.586229,-2.179656,6.174368,-7.365613,-7.468964,-4.623222,-1.859630,0.553814,1.999749,0.441498,-4.636770,-7.424768,2.678576,3.002748,-0.851387,9.949712,1.155982,-0.268413,9.353238,-1.730913,-8.075963,0.432965,-0.723591,-0.610070,-2.676945,-0.876044,4.737694,7.143594,7.298335,6.496707,2.805370,8.624713,-1.832035,5.011639,-3.646235,-1.954400,-2.195275,-7.762381,-3.133958,5.050407,-4.264222,4.843321,-3.726254,-7.911605,-2.611391,2.811127,-0.258263,-5.269776,-9.255426,-6.374367,6.717228,3.592065,-5.470401,-7.361159,-7.467188,-0.845088,2.066091,-8.709166,-1.588988,7.716021,8.666554,-7.518111,4.560121,-1.753449,-9.451648,1.877252,9.694485,-4.090595,-3.009882,-0.845123,-6.313954,1.229517,3.445721,3.574148,-4.000890,-0.700539,6.162234,-0.258379,2.478351,-3.151637,5.508591,-9.243460,-5.677175,4.159764,4.557424,8.111462,-4.407816,-1.855942,-8.315080,3.003607,-7.596339,-5.429371,7.811980,8.568633,-5.580563,-7.393753,5.404199,-5.510397,8.720888,-5.392603,-0.579289,-4.296193,-9.135614,-7.076834,-1.896669,6.999105,9.641504,-1.267054,-9.971847,8.129317,1.299825,2.396848,-2.938302,-4.466962,3.969828,6.305790,-2.529862,-7.528045,-8.477625,-2.646475,-7.110296,0.216609,4.862846,-3.734740,2.176494,-6.349129,-8.360731,1.054769,-6.509045,-9.492004,-7.974807,9.173757,-5.016541,1.291029,-7.204712,6.877346,-1.367344,-7.493695,7.013867,5.464795,-7.921558,9.627988,7.971156,-6.967677,9.429975,8.802294,-2.280577,-6.645193,-8.346817,2.393071,8.044620,-2.516283,8.844136,-1.355236,9.497789,-0.407747,9.519829,-4.547571,-9.167868,-7.709008,-3.622538,-7.006783,-5.554390,4.206684,-6.915451,2.355004,0.354057,0.766687,-9.044062,3.892511,-8.247783,-0.153682,-7.776516,-5.912271,0.665116,-8.836141,9.256821,-2.279565,0.375877,-9.970311,-4.785740,-7.721396,8.223206,-4.039481,9.461839,-8.227490,0.942984,8.091657,6.228666,7.846101,2.623653,-1.348125,-7.862896,-2.557329,-7.795729,8.807942,6.815666,0.001041,-0.828914,-0.736999,2.468152,1.240539,8.113453,-8.224989,-1.150164,0.505043,4.229480,-6.989890,-0.898458,-0.905251,-8.098800,1.049285,1.927090,-1.180885,7.344344,9.674822,0.237316,6.351539,6.598008,-6.808448,1.773725,7.687897,7.878763,-8.007729,3.521294,7.507177,7.031229,9.585802,7.581697,-5.134879,-3.687914,8.901907,-6.990499,6.232155,4.446015,7.208207,0.533395,2.562084,9.393203,5.122798,-3.804439,-7.932781,6.991331,-3.375455,8.797088,4.782271,-8.495924,-3.385625,-4.083995,4.579319,9.411630,-4.256604,7.738390,6.588137,-3.579646,4.795369,2.058468,-8.455952,1.723403,8.874374,7.012619,2.604677,-6.135669,-6.896392,8.042113,-4.988075,-4.392907,6.481491,-4.355845,-7.228064,3.948407,-6.448634,8.439727,-0.422294,6.078295,-3.335856,-0.737395,5.608159,4.806964,9.847508,8.721312,5.331221,6.482841,1.271923,5.914689,-7.248909,-3.653190,-0.138622,0.518865,-9.117332,-7.296951,8.388044,-7.186759,5.533424,-5.292448,-5.102717,-9.577652,2.311142,0.804748,-2.493059,1.749480,4.159518,4.109048,4.439767,-5.842351,3.792414,-0.079185,-7.279952,6.866680,-6.241741,-7.685017,5.227915,-7.150991,-2.721585,-2.836496,7.396635,5.545705,6.536625,-5.718215,9.483864,-6.814124,0.101254,0.239507,-0.937659,-3.382683,-4.538847,6.172807,9.030471,1.875609,7.899690,-2.722930,2.074436,-6.090515,-9.612024,2.541120,1.907949,0.768480,6.805534,-2.288497,3.582378,-1.024988,-5.005819,-8.805348,-7.186242,5.038770,1.776657,-5.888538,-8.346510,9.771964,7.559810,-0.588205,-1.332402,0.863987,2.618555,7.411922,-1.899849,-5.534165,-4.695713,3.658467,-1.269267,-7.158323,-6.439301,-4.325577,9.378173,-6.452987,8.274440,-7.905216,-6.156000,0.877264,5.951148,-1.946720,-8.532914,-8.122482,6.939285,8.984655,7.164378,5.147157,-9.553611,-8.761234,3.102108,-6.148605,2.958330,0.064165,4.844339,2.138801,4.338060,-1.214988,8.466829,-7.051177,-1.981112,-3.227360,-3.996785,-4.250588,-5.173093,-1.246106,7.676185,-9.064623,3.703445,-1.846089,-0.165216,-6.268324,2.219984,7.553088,4.666373,-5.967776,-0.685569,3.151310,-4.945009,9.441930,-8.756055,1.037541,9.043255,7.398160,9.561854,1.327531,1.280522,9.212420,-5.237859,9.068352,9.596489,-6.575819,2.079233,-3.212858,7.368400,-9.053096,7.873913,0.354204,6.700639,-4.953937,-7.612364,-4.841998,0.436342,-8.828750,-4.045335,3.660612,6.171821,9.779278,-2.516901,2.716366,-7.024616,8.159969,6.639527,-3.350169,7.295520,4.826960,-7.794770,-1.752336,2.035777,4.687388,-3.811207,2.342298,-5.810052,-8.377226,-7.846452,-0.223865,6.818113,4.808855,-8.031346,1.933548,-3.383849,4.031222,-4.197918,-8.512735,0.817005,-0.218726,-8.607334,0.550435,-3.212419,2.751814,9.162231,0.272148,-7.801585,1.606136,-2.663573]], dtype = "float32")#candidate|15968|(1, 1690)|const|float32
call_15967 = relay.TupleGetItem(func_9294_call(relay.reshape(const_15968.astype('float32'), [13, 13, 10])), 0)
call_15969 = relay.TupleGetItem(func_9297_call(relay.reshape(const_15968.astype('float32'), [13, 13, 10])), 0)
bop_15977 = relay.less_equal(const_15968.astype('bool'), relay.reshape(call_15967.astype('bool'), relay.shape_of(const_15968))) # shape=(1, 1690)
bop_15980 = relay.less_equal(const_15968.astype('bool'), relay.reshape(call_15969.astype('bool'), relay.shape_of(const_15968))) # shape=(1, 1690)
var_15989 = relay.var("var_15989", dtype = "bool", shape = (10, 1690))#candidate|15989|(10, 1690)|var|bool
bop_15990 = relay.equal(bop_15977.astype('bool'), var_15989.astype('bool')) # shape=(10, 1690)
bop_15993 = relay.equal(bop_15980.astype('bool'), var_15989.astype('bool')) # shape=(10, 1690)
func_4833_call = mod.get_global_var('func_4833')
func_4837_call = mutated_mod.get_global_var('func_4837')
var_16018 = relay.var("var_16018", dtype = "int8", shape = (84,))#candidate|16018|(84,)|var|int8
call_16017 = func_4833_call(relay.reshape(var_16018.astype('int8'), [1, 6, 14]), relay.reshape(call_15951.astype('int8'), [2, 6, 14]), )
call_16019 = func_4833_call(relay.reshape(var_16018.astype('int8'), [1, 6, 14]), relay.reshape(call_15951.astype('int8'), [2, 6, 14]), )
output = relay.Tuple([call_15951,call_15953,const_15954,bop_15990,call_16017,var_16018,])
output2 = relay.Tuple([call_15952,call_15955,const_15954,bop_15993,call_16019,var_16018,])
func_16025 = relay.Function([var_15989,var_16018,], output)
mod['func_16025'] = func_16025
mod = relay.transform.InferType()(mod)
mutated_mod['func_16025'] = func_16025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16025_call = mutated_mod.get_global_var('func_16025')
var_16027 = relay.var("var_16027", dtype = "bool", shape = (10, 1690))#candidate|16027|(10, 1690)|var|bool
var_16028 = relay.var("var_16028", dtype = "int8", shape = (84,))#candidate|16028|(84,)|var|int8
call_16026 = func_16025_call(var_16027,var_16028,)
output = call_16026
func_16029 = relay.Function([var_16027,var_16028,], output)
mutated_mod['func_16029'] = func_16029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13017_call = mod.get_global_var('func_13017')
func_13019_call = mutated_mod.get_global_var('func_13019')
call_16119 = func_13017_call()
call_16120 = func_13017_call()
output = call_16119
output2 = call_16120
func_16123 = relay.Function([], output)
mod['func_16123'] = func_16123
mod = relay.transform.InferType()(mod)
output = func_16123()
func_16124 = relay.Function([], output)
mutated_mod['func_16124'] = func_16124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13565_call = mod.get_global_var('func_13565')
func_13567_call = mutated_mod.get_global_var('func_13567')
call_16149 = relay.TupleGetItem(func_13565_call(), 0)
call_16150 = relay.TupleGetItem(func_13567_call(), 0)
output = relay.Tuple([call_16149,])
output2 = relay.Tuple([call_16150,])
func_16151 = relay.Function([], output)
mod['func_16151'] = func_16151
mod = relay.transform.InferType()(mod)
output = func_16151()
func_16152 = relay.Function([], output)
mutated_mod['func_16152'] = func_16152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14560_call = mod.get_global_var('func_14560')
func_14562_call = mutated_mod.get_global_var('func_14562')
call_16165 = func_14560_call()
call_16166 = func_14560_call()
output = relay.Tuple([call_16165,])
output2 = relay.Tuple([call_16166,])
func_16173 = relay.Function([], output)
mod['func_16173'] = func_16173
mod = relay.transform.InferType()(mod)
output = func_16173()
func_16174 = relay.Function([], output)
mutated_mod['func_16174'] = func_16174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14452_call = mod.get_global_var('func_14452')
func_14454_call = mutated_mod.get_global_var('func_14454')
call_16206 = relay.TupleGetItem(func_14452_call(), 3)
call_16207 = relay.TupleGetItem(func_14454_call(), 3)
func_13485_call = mod.get_global_var('func_13485')
func_13487_call = mutated_mod.get_global_var('func_13487')
call_16208 = func_13485_call()
call_16209 = func_13485_call()
func_13470_call = mod.get_global_var('func_13470')
func_13472_call = mutated_mod.get_global_var('func_13472')
const_16214 = relay.const([1.748094,7.753096,6.729625,3.269325,7.904273,8.405469,-3.314314,8.665118,-5.592468,2.620364,-2.653801,6.026335,7.954252,-2.119404,7.769920,2.920460,-2.988906,-6.173657,-1.163825,-7.446227,1.073062,8.357071,-5.622607,0.011635,-1.936351,9.819074,-4.685068,0.944130,5.065276,-9.183715,-2.920412,5.325838,9.791459,-5.569646,2.365829,3.474459,-7.642793,-5.613866,9.751876,6.367163,-9.898397,-2.546062,-6.442001,-6.733163,7.014498,-2.514987,7.014129,-8.446927,3.277080,-7.664989,1.358372,1.792711,-2.657633,8.660220,1.355858,-9.773088,8.492133,2.994983,-3.376143,7.802873,-3.432149,-2.930893,6.507496,-9.010919,5.667849,5.101945,-6.908801,4.008580,-9.592453,0.345688,1.682803,-0.378236,-1.523228,-5.226971,2.384877,0.935881,3.827827,4.352482,-4.766610,6.454502,4.901454,8.259477,-8.293233,-7.486054,7.291289,-3.751965,5.823377,6.534551,-7.211771,7.228750,1.321356,-1.648513,-7.002528,1.287014,0.450174,-8.484622,5.243026,9.306291,-5.652777,-1.609129,3.121462,6.643297,5.823228,-0.272169,-4.306338,-3.966730,-9.813227,8.157221,-7.173076,-6.762604,5.905222,-3.501134,-8.721864,-2.022725,-6.262086,-9.565025,-8.871698,-4.703948,-0.441798,4.043034,-1.869453,-7.036719,-7.496996,2.730057,-2.670222,5.736809,5.203689,-6.665871,1.568314,-1.255138,7.849165,8.399913,-8.915594,-3.731127,-6.158198,-5.017904,5.015753,-8.631496,-3.479387,-7.502360,1.807939,-9.042233,-9.182137,-6.669149,-1.962582,8.943838,4.694968,4.644881,-1.658302,-8.980993,9.059558,-6.113804,9.921727,6.033237,-5.360576,-5.287541,2.414184,-5.861050,4.175263,7.712865,-9.407793,5.248857,6.550965,5.764445,-5.120833,-6.242774,-7.177161,-2.615256,5.253968,9.514021,-9.160761,9.142301,1.862540,3.004459,-3.465584,-3.740451,6.001232,-3.967472,-3.631453,-6.954946,2.147514,-2.467684,3.906684,3.983845,-7.759220,6.319525,-9.158349,-7.758667,-8.364050,-6.566365,-2.259959,5.882604,8.308954,-9.455476,-2.565425,-6.162699,-9.750822,2.641798,-3.372051,-7.235967,-6.408265,8.393459,8.799974,-8.074886,7.651128,-1.699372,2.760147,7.505398,-4.152520,-4.766955,-1.628693,-3.252809,2.559972,0.771709,8.804708,1.966037,7.638457,-4.920111,-0.447649,-2.777207,-2.949462,-6.843967,5.302970,-3.244566,3.548141,-7.334253,7.824132,-9.658859,-9.271468,-4.301888,-3.322414,0.494491,-7.869314,-0.933117,-2.409918,-0.596952,0.858967,-2.268263,-7.905075,-8.828716,0.220955,-7.428795,-0.618533,-4.656344,-6.755349,-3.170134,-9.164079,-7.996823,7.114082,6.005977,4.762346,-5.769279,-2.331998,2.555344,2.133931,9.414344,-2.465304,-8.636257,-0.266570,-9.721386,4.158436,7.753425,-9.158398,8.449844,-6.035256,-9.299363,-6.916294,8.326053,7.248334,-0.155852,-2.059385,-2.839968,5.964202,5.400365,9.810038,-3.137532,-9.158515,-9.366325,3.270468,5.718285], dtype = "float64")#candidate|16214|(280,)|const|float64
call_16213 = relay.TupleGetItem(func_13470_call(relay.reshape(const_16214.astype('float64'), [280,])), 2)
call_16215 = relay.TupleGetItem(func_13472_call(relay.reshape(const_16214.astype('float64'), [280,])), 2)
func_1283_call = mod.get_global_var('func_1283')
func_1286_call = mutated_mod.get_global_var('func_1286')
var_16217 = relay.var("var_16217", dtype = "int8", shape = (1, 630))#candidate|16217|(1, 630)|var|int8
call_16216 = relay.TupleGetItem(func_1283_call(relay.reshape(var_16217.astype('int8'), [9, 7, 10]), relay.reshape(var_16217.astype('int8'), [9, 7, 10]), ), 0)
call_16218 = relay.TupleGetItem(func_1286_call(relay.reshape(var_16217.astype('int8'), [9, 7, 10]), relay.reshape(var_16217.astype('int8'), [9, 7, 10]), ), 0)
output = relay.Tuple([call_16206,call_16208,call_16213,const_16214,call_16216,var_16217,])
output2 = relay.Tuple([call_16207,call_16209,call_16215,const_16214,call_16218,var_16217,])
func_16232 = relay.Function([var_16217,], output)
mod['func_16232'] = func_16232
mod = relay.transform.InferType()(mod)
mutated_mod['func_16232'] = func_16232
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16233 = relay.var("var_16233", dtype = "int8", shape = (1, 630))#candidate|16233|(1, 630)|var|int8
func_16232_call = mutated_mod.get_global_var('func_16232')
call_16234 = func_16232_call(var_16233)
output = call_16234
func_16235 = relay.Function([var_16233], output)
mutated_mod['func_16235'] = func_16235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14400_call = mod.get_global_var('func_14400')
func_14401_call = mutated_mod.get_global_var('func_14401')
call_16279 = func_14400_call()
call_16280 = func_14400_call()
output = call_16279
output2 = call_16280
func_16288 = relay.Function([], output)
mod['func_16288'] = func_16288
mod = relay.transform.InferType()(mod)
mutated_mod['func_16288'] = func_16288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16288_call = mutated_mod.get_global_var('func_16288')
call_16289 = func_16288_call()
output = call_16289
func_16290 = relay.Function([], output)
mutated_mod['func_16290'] = func_16290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15045_call = mod.get_global_var('func_15045')
func_15047_call = mutated_mod.get_global_var('func_15047')
call_16364 = relay.TupleGetItem(func_15045_call(), 0)
call_16365 = relay.TupleGetItem(func_15047_call(), 0)
func_2115_call = mod.get_global_var('func_2115')
func_2118_call = mutated_mod.get_global_var('func_2118')
var_16373 = relay.var("var_16373", dtype = "float32", shape = (192,))#candidate|16373|(192,)|var|float32
var_16374 = relay.var("var_16374", dtype = "float32", shape = (975,))#candidate|16374|(975,)|var|float32
call_16372 = relay.TupleGetItem(func_2115_call(relay.reshape(var_16373.astype('float32'), [3, 16, 4]), relay.reshape(var_16374.astype('float32'), [975,]), ), 0)
call_16375 = relay.TupleGetItem(func_2118_call(relay.reshape(var_16373.astype('float32'), [3, 16, 4]), relay.reshape(var_16374.astype('float32'), [975,]), ), 0)
output = relay.Tuple([call_16364,call_16372,var_16373,var_16374,])
output2 = relay.Tuple([call_16365,call_16375,var_16373,var_16374,])
func_16383 = relay.Function([var_16373,var_16374,], output)
mod['func_16383'] = func_16383
mod = relay.transform.InferType()(mod)
var_16384 = relay.var("var_16384", dtype = "float32", shape = (192,))#candidate|16384|(192,)|var|float32
var_16385 = relay.var("var_16385", dtype = "float32", shape = (975,))#candidate|16385|(975,)|var|float32
output = func_16383(var_16384,var_16385,)
func_16386 = relay.Function([var_16384,var_16385,], output)
mutated_mod['func_16386'] = func_16386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15754_call = mod.get_global_var('func_15754')
func_15756_call = mutated_mod.get_global_var('func_15756')
call_16401 = relay.TupleGetItem(func_15754_call(), 0)
call_16402 = relay.TupleGetItem(func_15756_call(), 0)
output = call_16401
output2 = call_16402
func_16406 = relay.Function([], output)
mod['func_16406'] = func_16406
mod = relay.transform.InferType()(mod)
output = func_16406()
func_16407 = relay.Function([], output)
mutated_mod['func_16407'] = func_16407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15754_call = mod.get_global_var('func_15754')
func_15756_call = mutated_mod.get_global_var('func_15756')
call_16450 = relay.TupleGetItem(func_15754_call(), 0)
call_16451 = relay.TupleGetItem(func_15756_call(), 0)
output = call_16450
output2 = call_16451
func_16452 = relay.Function([], output)
mod['func_16452'] = func_16452
mod = relay.transform.InferType()(mod)
mutated_mod['func_16452'] = func_16452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16452_call = mutated_mod.get_global_var('func_16452')
call_16453 = func_16452_call()
output = call_16453
func_16454 = relay.Function([], output)
mutated_mod['func_16454'] = func_16454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16452_call = mod.get_global_var('func_16452')
func_16454_call = mutated_mod.get_global_var('func_16454')
call_16455 = func_16452_call()
call_16456 = func_16452_call()
output = call_16455
output2 = call_16456
func_16460 = relay.Function([], output)
mod['func_16460'] = func_16460
mod = relay.transform.InferType()(mod)
output = func_16460()
func_16461 = relay.Function([], output)
mutated_mod['func_16461'] = func_16461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15775_call = mod.get_global_var('func_15775')
func_15776_call = mutated_mod.get_global_var('func_15776')
call_16495 = relay.TupleGetItem(func_15775_call(), 2)
call_16496 = relay.TupleGetItem(func_15776_call(), 2)
func_15908_call = mod.get_global_var('func_15908')
func_15910_call = mutated_mod.get_global_var('func_15910')
call_16497 = func_15908_call()
call_16498 = func_15908_call()
output = relay.Tuple([call_16495,call_16497,])
output2 = relay.Tuple([call_16496,call_16498,])
func_16502 = relay.Function([], output)
mod['func_16502'] = func_16502
mod = relay.transform.InferType()(mod)
mutated_mod['func_16502'] = func_16502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16502_call = mutated_mod.get_global_var('func_16502')
call_16503 = func_16502_call()
output = call_16503
func_16504 = relay.Function([], output)
mutated_mod['func_16504'] = func_16504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14169_call = mod.get_global_var('func_14169')
func_14170_call = mutated_mod.get_global_var('func_14170')
call_16547 = relay.TupleGetItem(func_14169_call(), 0)
call_16548 = relay.TupleGetItem(func_14170_call(), 0)
output = call_16547
output2 = call_16548
func_16552 = relay.Function([], output)
mod['func_16552'] = func_16552
mod = relay.transform.InferType()(mod)
mutated_mod['func_16552'] = func_16552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16552_call = mutated_mod.get_global_var('func_16552')
call_16553 = func_16552_call()
output = call_16553
func_16554 = relay.Function([], output)
mutated_mod['func_16554'] = func_16554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13624_call = mod.get_global_var('func_13624')
func_13626_call = mutated_mod.get_global_var('func_13626')
call_16585 = relay.TupleGetItem(func_13624_call(), 0)
call_16586 = relay.TupleGetItem(func_13626_call(), 0)
func_5735_call = mod.get_global_var('func_5735')
func_5738_call = mutated_mod.get_global_var('func_5738')
var_16599 = relay.var("var_16599", dtype = "float32", shape = (8, 240))#candidate|16599|(8, 240)|var|float32
call_16598 = func_5735_call(relay.reshape(var_16599.astype('float32'), [8, 16, 15]))
call_16600 = func_5735_call(relay.reshape(var_16599.astype('float32'), [8, 16, 15]))
func_16383_call = mod.get_global_var('func_16383')
func_16386_call = mutated_mod.get_global_var('func_16386')
var_16608 = relay.var("var_16608", dtype = "float32", shape = (4, 48))#candidate|16608|(4, 48)|var|float32
call_16607 = relay.TupleGetItem(func_16383_call(relay.reshape(var_16608.astype('float32'), [192,]), relay.reshape(call_16585.astype('float32'), [975,]), ), 0)
call_16609 = relay.TupleGetItem(func_16386_call(relay.reshape(var_16608.astype('float32'), [192,]), relay.reshape(call_16585.astype('float32'), [975,]), ), 0)
output = relay.Tuple([call_16585,call_16598,var_16599,call_16607,var_16608,])
output2 = relay.Tuple([call_16586,call_16600,var_16599,call_16609,var_16608,])
func_16626 = relay.Function([var_16599,var_16608,], output)
mod['func_16626'] = func_16626
mod = relay.transform.InferType()(mod)
mutated_mod['func_16626'] = func_16626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16626_call = mutated_mod.get_global_var('func_16626')
var_16628 = relay.var("var_16628", dtype = "float32", shape = (8, 240))#candidate|16628|(8, 240)|var|float32
var_16629 = relay.var("var_16629", dtype = "float32", shape = (4, 48))#candidate|16629|(4, 48)|var|float32
call_16627 = func_16626_call(var_16628,var_16629,)
output = call_16627
func_16630 = relay.Function([var_16628,var_16629,], output)
mutated_mod['func_16630'] = func_16630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16173_call = mod.get_global_var('func_16173')
func_16174_call = mutated_mod.get_global_var('func_16174')
call_16655 = relay.TupleGetItem(func_16173_call(), 0)
call_16656 = relay.TupleGetItem(func_16174_call(), 0)
func_1283_call = mod.get_global_var('func_1283')
func_1286_call = mutated_mod.get_global_var('func_1286')
const_16664 = relay.const([-7,-9,6,3,8,1,-2,3,-8,1,6,9,10,5,5,1,10,6,5,-2,-7,-6,6,5,8,-7,1,-6,-9,10,-8,-5,10,-4,1,2,7,-6,-9,6,-9,2,8,-1,-9,-1,2,5,5,1,-3,5,10,4,2,-7,-2,1,6,-7,4,4,-3,-2,-10,8,5,-5,5,-6,-9,8,-1,1,2,4,7,-6,9,-3,-10,-2,2,-1,9,4,10,9,-2,9,-10,1,-3,10,-4,2,-1,10,6,-2,1,-2,9,-10,-2,4,4,-9,-4,-2,1,-6,-10,10,10,-10,-8,-9,2,8,10,5,-9,2,5,-2,10,1,-6,6,2,4,8,9,-5,-5,-8,1,-7,1,-7,-2,-2,-8,5,2,-2,9,4,-2,-6,-3,9,2,-7,10,7,-4,7,5,6,1,-8,9,-10,-10,-8,-3,-9,5,-9,3,-8,-6,6,7,1,-3,-10,-2,3,-9,6,-10,-8,-2,-9,-4,1,2,-3,3,-8,-4,7,1,7,3,-1,-10,-5,9,-9,-10,4,10,-2,-9,7,1,9,-4,-1,10,9,2,-2,7,-3,-2,9,-2,2,3,9,5,-5,2,7,7,-2,7,9,5,-1,1,-8,-10,6,-2,-7,-3,-6,-10,9,-9,6,2,10,-1,6,-10,5,-7,-3,-8,-5,-7,-5,6,-4,-4,-2,8,-6,2,9,6,-2,-6,1,-9,4,1,-1,-3,3,5,-6,7,2,-3,3,-6,2,2,-6,2,-5,9,-2,-2,2,2,2,9,1,6,1,1,-6,5,-1,1,-1,-5,7,-2,5,-8,-5,1,-8,2,-1,-1,3,8,-6,-4,-1,2,6,-8,9,-6,-10,-10,3,10,-4,-2,8,5,-1,2,7,2,9,-4,4,3,-8,4,7,-7,4,10,-9,7,3,2,3,-7,1,-1,1,1,-6,-3,1,-2,9,-1,6,-6,7,-2,3,-5,1,1,7,-3,9,6,6,-8,-1,-3,7,9,-9,-6,-10,-7,4,-3,2,-4,2,2,9,10,9,6,-3,1,5,4,-6,-6,-1,-3,-5,-3,-6,-4,6,-4,7,2,4,4,9,-5,-3,7,-10,-4,-7,9,-3,-10,-6,6,4,-7,-1,8,-3,7,3,-7,-2,5,9,3,-8,-2,7,2,-6,-10,2,-7,10,-8,-7,6,-7,9,9,-1,-6,5,-1,-3,-6,3,10,10,5,-6,4,-4,-5,10,-6,2,3,3,4,10,10,7,-5,-3,6,5,-1,4,1,-1,6,8,3,-1,9,7,5,1,-3,-10,-2,-3,-1,9,3,-10,-5,6,10,-7,1,8,9,5,2,3,8,6,-10,-5,9,2,2,4,-7,10,-4,-1,-8,5,2,5,-1,-3,-10,-6,2,2,5,-5,-8,8,3,-7,8,2,-9,3,-10,4,5,-8,9,-10,-8,9,-1,-8,-8,7,6,-9,-8,8,9,7,-6,-10,5,-9,6,-8,5,-1,-10,3,10,2,2,-6,-4,4,6,-4,3,-3,-3,4,-7,-3,5,-5,-5,5,-9,-10,-1,-2,8,9,1,-8,5,2,-1,8,-10,3,10,-7,-6,-3,-9,6,-2,9,-9,8,1,5,-9,-7,6,8,-7,-6,-10,-2,3,-8,-4,-10,4,-6,-2,-8], dtype = "int8")#candidate|16664|(630,)|const|int8
call_16663 = relay.TupleGetItem(func_1283_call(relay.reshape(const_16664.astype('int8'), [9, 7, 10]), relay.reshape(const_16664.astype('int8'), [9, 7, 10]), ), 0)
call_16665 = relay.TupleGetItem(func_1286_call(relay.reshape(const_16664.astype('int8'), [9, 7, 10]), relay.reshape(const_16664.astype('int8'), [9, 7, 10]), ), 0)
output = relay.Tuple([call_16655,call_16663,const_16664,])
output2 = relay.Tuple([call_16656,call_16665,const_16664,])
func_16667 = relay.Function([], output)
mod['func_16667'] = func_16667
mod = relay.transform.InferType()(mod)
mutated_mod['func_16667'] = func_16667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16667_call = mutated_mod.get_global_var('func_16667')
call_16668 = func_16667_call()
output = call_16668
func_16669 = relay.Function([], output)
mutated_mod['func_16669'] = func_16669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15908_call = mod.get_global_var('func_15908')
func_15910_call = mutated_mod.get_global_var('func_15910')
call_16688 = func_15908_call()
call_16689 = func_15908_call()
output = call_16688
output2 = call_16689
func_16695 = relay.Function([], output)
mod['func_16695'] = func_16695
mod = relay.transform.InferType()(mod)
mutated_mod['func_16695'] = func_16695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16695_call = mutated_mod.get_global_var('func_16695')
call_16696 = func_16695_call()
output = call_16696
func_16697 = relay.Function([], output)
mutated_mod['func_16697'] = func_16697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16406_call = mod.get_global_var('func_16406')
func_16407_call = mutated_mod.get_global_var('func_16407')
call_16709 = func_16406_call()
call_16710 = func_16406_call()
output = call_16709
output2 = call_16710
func_16711 = relay.Function([], output)
mod['func_16711'] = func_16711
mod = relay.transform.InferType()(mod)
output = func_16711()
func_16712 = relay.Function([], output)
mutated_mod['func_16712'] = func_16712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13624_call = mod.get_global_var('func_13624')
func_13626_call = mutated_mod.get_global_var('func_13626')
call_16716 = relay.TupleGetItem(func_13624_call(), 0)
call_16717 = relay.TupleGetItem(func_13626_call(), 0)
output = call_16716
output2 = call_16717
func_16719 = relay.Function([], output)
mod['func_16719'] = func_16719
mod = relay.transform.InferType()(mod)
output = func_16719()
func_16720 = relay.Function([], output)
mutated_mod['func_16720'] = func_16720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16667_call = mod.get_global_var('func_16667')
func_16669_call = mutated_mod.get_global_var('func_16669')
call_16733 = relay.TupleGetItem(func_16667_call(), 2)
call_16734 = relay.TupleGetItem(func_16669_call(), 2)
func_13527_call = mod.get_global_var('func_13527')
func_13530_call = mutated_mod.get_global_var('func_13530')
const_16740 = relay.const([3,1,-5,-5,3,-8,10,7,-6,-2,-7,1,10,-6,-4,-10,-6,-8,5,-9,3,-1,5,-9,-8,-2,-2,4,6,-4,4,7,2,3,9,10,-9,-6,-10,-5,-4,5,1,9,-9,8,-6,3,2,-7,-8,-2,-7,3,-3,-6,-7,-2,-10,6,3,-3,10,-7,2,1,3,8,4,-7,-2,-4,6,1,-9,5,2,-3,4,3,5,7,-1,-8,-8,4,10,3,5,3,-1,-6,-8,3,8,-9,4,-1,-3,-2,5,-3,3,2,9,2,6,1,8,8,-4,8,-7,2,9,-10,-1,9,8,2,7,-7,3,-8,4,6,5,3,-5,1,-3,8,6,10,9,3,-5,8,8,8,4,-9,7,10,-9,8,3,-7,-3,5,8,-7,-10,-2,3,-10,3,-5,-1,4,7,3,-8,-1,7,1,5,8,-5,4,2,4,-3,-8,3,4,4,1,10,-10,-9,-2,-1,10,3,-5,-7,-10,7,5,-10,9,8,5,-4,-7,-10,-7,-1,8,-2,1,-1,10,-1,-7,3,6,-7,-3,9,-2,-1,1,-8,8,-3,9,-1,1,3,-6,3,-10,-6,1,-3,4,6,5,-4,3,-3,-1,-3,-10,-10,5,-8,-6,-7,10,2,3,-9,1,3,-1,8,3,-2,-10,-9,8,9,4,10,8,-9,-1,3,-2,-8,5,4,-9,-2,1,-1,1,-10,8,10,-6,-10,9,-9,-10,-5,2,4,6,-8,7,5,-1,-4,6,6,-3,9,10,3,2,6,7,-3,5,-1,3,10,-10,-3,-8,-8,-7,-3,2,8,5,-8,-3,-7,-6,-1,-2,-3,5,9,-6,6,-6,10,-6,4,2,4,-6,-4,-7,9,7,-4,-9,8,1,-1,-3,-5,-1,10,2,9,-5,10,9,3,-3,-8,1,-8,-10,-9,9,-3,6,4,-7,8,5,4,-7,-9,6,-3,-3,-9,-9,9,-6,-8,4,-10,6,-3,-6,-6,5,-5,3,8,-8,-1,7,7,-2,6,9,-9,4,6,8,-4,7,4,5,6,-8,2,-8,-9,-6,-8,-10,9,-6,3,7,7,-7,4,2,7,10,7,10,10,-10,-10,3,4,4,-5,7,7,-4,5,-10,8,-4,7,1,-10,6,-1,1,10,7,8,-9,7,5,-9,-6,4,4,-6,9,-9,-9,-3,8,-8,9,8,-3,1,-10,-3,-9,-8,8,-1,-1,-3,-1,-1,-2,-5,-4,-10,9,-5,2,-5,4,-8,-7,-3,-9,9,5,-10,-8,9,-7,1,8,5,3,-3,-3,-1,-9,-1,1,10,-9,-4,-7,-10,-1,2,-6,-1,9,6,-6,4,-1,6,4,-9,-8,1,7,-10,2,-10,-9,9,-7,-9,2,-8,8,-7,2,7,-1,7,-2,6,1,4,7,9,8,8,-3,5,2,6,-9,8,-3,-8,2,-9,-10,-4,-6,-2,10,4,-8,-5,-10,6,5,-9,-9,-3,1,-5,-3,-9,-1,-3,10,-4,-6,-9,-1,-10,-9,7,6,-10,-2,-7,3,5,-8,2,-6,8,-7,-2,2,-7,1,-10,3,-3,4,-1,-7,-8,5,-2,-8,6,-7,-6,-10,-1,-6,-7,8,6,-1,8,5,10,-10,2,-3,5,-7,-9,1,-10,-1,-8,9,1,-2,8,5,-7,2,-2,10,-5,8,5,-5,8,4,-5,1,10,4,-1,6,3,9,-3,5,-7,-3,2,-7,-4,-6,3,2,1,3,-7,9,-7,7,9,-9,5,-9,9,-9,9,9,-3,5,-9,3,7,5,-4,5,4,-10,-7,-10,-6,-1,-2,-5,3,8,-8,9,-5,-1,-7,-4,2,4,6,-6,-10,-7,7,-7,4,4,6,-1,-8,-4,9,-7,-6,10,4,-4,3,7,3,-2], dtype = "int64")#candidate|16740|(720,)|const|int64
call_16739 = relay.TupleGetItem(func_13527_call(relay.reshape(const_16740.astype('int64'), [720, 1])), 9)
call_16741 = relay.TupleGetItem(func_13530_call(relay.reshape(const_16740.astype('int64'), [720, 1])), 9)
output = relay.Tuple([call_16733,call_16739,const_16740,])
output2 = relay.Tuple([call_16734,call_16741,const_16740,])
func_16743 = relay.Function([], output)
mod['func_16743'] = func_16743
mod = relay.transform.InferType()(mod)
mutated_mod['func_16743'] = func_16743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16743_call = mutated_mod.get_global_var('func_16743')
call_16744 = func_16743_call()
output = call_16744
func_16745 = relay.Function([], output)
mutated_mod['func_16745'] = func_16745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16406_call = mod.get_global_var('func_16406')
func_16407_call = mutated_mod.get_global_var('func_16407')
call_16769 = func_16406_call()
call_16770 = func_16406_call()
func_12987_call = mod.get_global_var('func_12987')
func_12988_call = mutated_mod.get_global_var('func_12988')
call_16773 = relay.TupleGetItem(func_12987_call(), 1)
call_16774 = relay.TupleGetItem(func_12988_call(), 1)
func_5136_call = mod.get_global_var('func_5136')
func_5140_call = mutated_mod.get_global_var('func_5140')
const_16795 = relay.const([-3,-1,-8,-3,-4,-2,7,10,5,-3,7,7,-8,-5,-4,-5,-3,-3,1,6,4,10,-7,1,6,-7,2,7,2,10,-6,-2,-3,-10,1,-10,3,-6,-2,4,-3,-1,6,4,1,5,-10,6,2,-8,3,-5,9,9,-10,-1,8,7,-1,-4,-6,-10,8,2,6,-2,-7,5,2,-9,-1,-7,-2,2,7,6,9,-2,3,-6,3,8,-8,-5,-9,3,5,-6,6,2,6,-7,-3,-1,-2,-7,-8,4,-8,-6,-5,6,1,-9,-1,-8,-9,1,5,-10,10,1,-2,4,6,-6,9,5,5,-6], dtype = "int64")#candidate|16795|(120,)|const|int64
var_16796 = relay.var("var_16796", dtype = "int64", shape = (4, 180))#candidate|16796|(4, 180)|var|int64
var_16797 = relay.var("var_16797", dtype = "int8", shape = (1440,))#candidate|16797|(1440,)|var|int8
call_16794 = relay.TupleGetItem(func_5136_call(relay.reshape(const_16795.astype('int64'), [12, 10, 1]), relay.reshape(var_16796.astype('int64'), [12, 10, 6]), relay.reshape(var_16797.astype('int8'), [1440,]), ), 2)
call_16798 = relay.TupleGetItem(func_5140_call(relay.reshape(const_16795.astype('int64'), [12, 10, 1]), relay.reshape(var_16796.astype('int64'), [12, 10, 6]), relay.reshape(var_16797.astype('int8'), [1440,]), ), 2)
func_15241_call = mod.get_global_var('func_15241')
func_15244_call = mutated_mod.get_global_var('func_15244')
var_16800 = relay.var("var_16800", dtype = "float32", shape = (39, 5))#candidate|16800|(39, 5)|var|float32
call_16799 = relay.TupleGetItem(func_15241_call(relay.reshape(var_16800.astype('float32'), [3, 5, 13])), 0)
call_16801 = relay.TupleGetItem(func_15244_call(relay.reshape(var_16800.astype('float32'), [3, 5, 13])), 0)
func_2034_call = mod.get_global_var('func_2034')
func_2038_call = mutated_mod.get_global_var('func_2038')
var_16808 = relay.var("var_16808", dtype = "int8", shape = (768,))#candidate|16808|(768,)|var|int8
call_16807 = relay.TupleGetItem(func_2034_call(relay.reshape(var_16808.astype('int8'), [6, 8, 16]), relay.reshape(call_16773.astype('float32'), [975, 1]), ), 6)
call_16809 = relay.TupleGetItem(func_2038_call(relay.reshape(var_16808.astype('int8'), [6, 8, 16]), relay.reshape(call_16773.astype('float32'), [975, 1]), ), 6)
output = relay.Tuple([call_16769,call_16773,call_16794,const_16795,var_16796,var_16797,call_16799,var_16800,call_16807,var_16808,])
output2 = relay.Tuple([call_16770,call_16774,call_16798,const_16795,var_16796,var_16797,call_16801,var_16800,call_16809,var_16808,])
func_16818 = relay.Function([var_16796,var_16797,var_16800,var_16808,], output)
mod['func_16818'] = func_16818
mod = relay.transform.InferType()(mod)
mutated_mod['func_16818'] = func_16818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16818_call = mutated_mod.get_global_var('func_16818')
var_16820 = relay.var("var_16820", dtype = "int64", shape = (4, 180))#candidate|16820|(4, 180)|var|int64
var_16821 = relay.var("var_16821", dtype = "int8", shape = (1440,))#candidate|16821|(1440,)|var|int8
var_16822 = relay.var("var_16822", dtype = "float32", shape = (39, 5))#candidate|16822|(39, 5)|var|float32
var_16823 = relay.var("var_16823", dtype = "int8", shape = (768,))#candidate|16823|(768,)|var|int8
call_16819 = func_16818_call(var_16820,var_16821,var_16822,var_16823,)
output = call_16819
func_16824 = relay.Function([var_16820,var_16821,var_16822,var_16823,], output)
mutated_mod['func_16824'] = func_16824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14990_call = mod.get_global_var('func_14990')
func_14992_call = mutated_mod.get_global_var('func_14992')
call_16858 = relay.TupleGetItem(func_14990_call(), 0)
call_16859 = relay.TupleGetItem(func_14992_call(), 0)
func_13081_call = mod.get_global_var('func_13081')
func_13084_call = mutated_mod.get_global_var('func_13084')
call_16864 = relay.TupleGetItem(func_13081_call(relay.reshape(call_16858.astype('float32'), [13, 5, 15])), 4)
call_16865 = relay.TupleGetItem(func_13084_call(relay.reshape(call_16858.astype('float32'), [13, 5, 15])), 4)
func_16552_call = mod.get_global_var('func_16552')
func_16554_call = mutated_mod.get_global_var('func_16554')
call_16871 = func_16552_call()
call_16872 = func_16552_call()
uop_16876 = relay.sinh(call_16871.astype('float64')) # shape=(12, 6, 11)
uop_16878 = relay.sinh(call_16872.astype('float64')) # shape=(12, 6, 11)
output = relay.Tuple([call_16858,call_16864,uop_16876,])
output2 = relay.Tuple([call_16859,call_16865,uop_16878,])
func_16895 = relay.Function([], output)
mod['func_16895'] = func_16895
mod = relay.transform.InferType()(mod)
mutated_mod['func_16895'] = func_16895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16895_call = mutated_mod.get_global_var('func_16895')
call_16896 = func_16895_call()
output = call_16896
func_16897 = relay.Function([], output)
mutated_mod['func_16897'] = func_16897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14151_call = mod.get_global_var('func_14151')
func_14153_call = mutated_mod.get_global_var('func_14153')
call_16976 = relay.TupleGetItem(func_14151_call(), 0)
call_16977 = relay.TupleGetItem(func_14153_call(), 0)
uop_16987 = relay.sigmoid(call_16976.astype('float32')) # shape=(12, 6, 11)
uop_16989 = relay.sigmoid(call_16977.astype('float32')) # shape=(12, 6, 11)
uop_16992 = relay.erf(uop_16987.astype('float64')) # shape=(12, 6, 11)
uop_16994 = relay.erf(uop_16989.astype('float64')) # shape=(12, 6, 11)
output = uop_16992
output2 = uop_16994
func_17009 = relay.Function([], output)
mod['func_17009'] = func_17009
mod = relay.transform.InferType()(mod)
output = func_17009()
func_17010 = relay.Function([], output)
mutated_mod['func_17010'] = func_17010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16123_call = mod.get_global_var('func_16123')
func_16124_call = mutated_mod.get_global_var('func_16124')
call_17043 = func_16123_call()
call_17044 = func_16123_call()
output = call_17043
output2 = call_17044
func_17071 = relay.Function([], output)
mod['func_17071'] = func_17071
mod = relay.transform.InferType()(mod)
mutated_mod['func_17071'] = func_17071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17071_call = mutated_mod.get_global_var('func_17071')
call_17072 = func_17071_call()
output = call_17072
func_17073 = relay.Function([], output)
mutated_mod['func_17073'] = func_17073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17071_call = mod.get_global_var('func_17071')
func_17073_call = mutated_mod.get_global_var('func_17073')
call_17082 = func_17071_call()
call_17083 = func_17071_call()
output = relay.Tuple([call_17082,])
output2 = relay.Tuple([call_17083,])
func_17095 = relay.Function([], output)
mod['func_17095'] = func_17095
mod = relay.transform.InferType()(mod)
output = func_17095()
func_17096 = relay.Function([], output)
mutated_mod['func_17096'] = func_17096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15088_call = mod.get_global_var('func_15088')
func_15090_call = mutated_mod.get_global_var('func_15090')
call_17200 = func_15088_call()
call_17201 = func_15088_call()
func_15948_call = mod.get_global_var('func_15948')
func_15950_call = mutated_mod.get_global_var('func_15950')
call_17204 = relay.TupleGetItem(func_15948_call(), 0)
call_17205 = relay.TupleGetItem(func_15950_call(), 0)
func_16460_call = mod.get_global_var('func_16460')
func_16461_call = mutated_mod.get_global_var('func_16461')
call_17209 = func_16460_call()
call_17210 = func_16460_call()
func_5414_call = mod.get_global_var('func_5414')
func_5418_call = mutated_mod.get_global_var('func_5418')
var_17224 = relay.var("var_17224", dtype = "uint16", shape = (588,))#candidate|17224|(588,)|var|uint16
call_17223 = func_5414_call(relay.reshape(var_17224.astype('uint16'), [14, 3, 14]), relay.reshape(var_17224.astype('uint16'), [14, 3, 14]), )
call_17225 = func_5414_call(relay.reshape(var_17224.astype('uint16'), [14, 3, 14]), relay.reshape(var_17224.astype('uint16'), [14, 3, 14]), )
func_14452_call = mod.get_global_var('func_14452')
func_14454_call = mutated_mod.get_global_var('func_14454')
call_17227 = relay.TupleGetItem(func_14452_call(), 0)
call_17228 = relay.TupleGetItem(func_14454_call(), 0)
output = relay.Tuple([call_17200,call_17204,call_17209,call_17223,var_17224,call_17227,])
output2 = relay.Tuple([call_17201,call_17205,call_17210,call_17225,var_17224,call_17228,])
func_17234 = relay.Function([var_17224,], output)
mod['func_17234'] = func_17234
mod = relay.transform.InferType()(mod)
mutated_mod['func_17234'] = func_17234
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17235 = relay.var("var_17235", dtype = "uint16", shape = (588,))#candidate|17235|(588,)|var|uint16
func_17234_call = mutated_mod.get_global_var('func_17234')
call_17236 = func_17234_call(var_17235)
output = call_17236
func_17237 = relay.Function([var_17235], output)
mutated_mod['func_17237'] = func_17237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16695_call = mod.get_global_var('func_16695')
func_16697_call = mutated_mod.get_global_var('func_16697')
call_17280 = func_16695_call()
call_17281 = func_16695_call()
func_14990_call = mod.get_global_var('func_14990')
func_14992_call = mutated_mod.get_global_var('func_14992')
call_17306 = relay.TupleGetItem(func_14990_call(), 0)
call_17307 = relay.TupleGetItem(func_14992_call(), 0)
func_15948_call = mod.get_global_var('func_15948')
func_15950_call = mutated_mod.get_global_var('func_15950')
call_17310 = relay.TupleGetItem(func_15948_call(), 0)
call_17311 = relay.TupleGetItem(func_15950_call(), 0)
output = relay.Tuple([call_17280,call_17306,call_17310,])
output2 = relay.Tuple([call_17281,call_17307,call_17311,])
func_17313 = relay.Function([], output)
mod['func_17313'] = func_17313
mod = relay.transform.InferType()(mod)
mutated_mod['func_17313'] = func_17313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17313_call = mutated_mod.get_global_var('func_17313')
call_17314 = func_17313_call()
output = call_17314
func_17315 = relay.Function([], output)
mutated_mod['func_17315'] = func_17315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16288_call = mod.get_global_var('func_16288')
func_16290_call = mutated_mod.get_global_var('func_16290')
call_17330 = func_16288_call()
call_17331 = func_16288_call()
uop_17336 = relay.rsqrt(call_17330.astype('float64')) # shape=(12, 6, 11)
uop_17338 = relay.rsqrt(call_17331.astype('float64')) # shape=(12, 6, 11)
var_17340 = relay.var("var_17340", dtype = "float64", shape = (12, 6, 11))#candidate|17340|(12, 6, 11)|var|float64
bop_17341 = relay.logical_xor(call_17330.astype('uint16'), relay.reshape(var_17340.astype('uint16'), relay.shape_of(call_17330))) # shape=(12, 6, 11)
bop_17344 = relay.logical_xor(call_17331.astype('uint16'), relay.reshape(var_17340.astype('uint16'), relay.shape_of(call_17331))) # shape=(12, 6, 11)
output = relay.Tuple([uop_17336,bop_17341,])
output2 = relay.Tuple([uop_17338,bop_17344,])
func_17345 = relay.Function([var_17340,], output)
mod['func_17345'] = func_17345
mod = relay.transform.InferType()(mod)
var_17346 = relay.var("var_17346", dtype = "float64", shape = (12, 6, 11))#candidate|17346|(12, 6, 11)|var|float64
output = func_17345(var_17346)
func_17347 = relay.Function([var_17346], output)
mutated_mod['func_17347'] = func_17347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14452_call = mod.get_global_var('func_14452')
func_14454_call = mutated_mod.get_global_var('func_14454')
call_17352 = relay.TupleGetItem(func_14452_call(), 3)
call_17353 = relay.TupleGetItem(func_14454_call(), 3)
output = relay.Tuple([call_17352,])
output2 = relay.Tuple([call_17353,])
func_17365 = relay.Function([], output)
mod['func_17365'] = func_17365
mod = relay.transform.InferType()(mod)
mutated_mod['func_17365'] = func_17365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17365_call = mutated_mod.get_global_var('func_17365')
call_17366 = func_17365_call()
output = call_17366
func_17367 = relay.Function([], output)
mutated_mod['func_17367'] = func_17367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14241_call = mod.get_global_var('func_14241')
func_14242_call = mutated_mod.get_global_var('func_14242')
call_17385 = relay.TupleGetItem(func_14241_call(), 0)
call_17386 = relay.TupleGetItem(func_14242_call(), 0)
output = relay.Tuple([call_17385,])
output2 = relay.Tuple([call_17386,])
func_17388 = relay.Function([], output)
mod['func_17388'] = func_17388
mod = relay.transform.InferType()(mod)
mutated_mod['func_17388'] = func_17388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17388_call = mutated_mod.get_global_var('func_17388')
call_17389 = func_17388_call()
output = call_17389
func_17390 = relay.Function([], output)
mutated_mod['func_17390'] = func_17390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13017_call = mod.get_global_var('func_13017')
func_13019_call = mutated_mod.get_global_var('func_13019')
call_17398 = func_13017_call()
call_17399 = func_13017_call()
var_17403 = relay.var("var_17403", dtype = "float64", shape = (12, 6, 11))#candidate|17403|(12, 6, 11)|var|float64
bop_17404 = relay.floor_mod(call_17398.astype('float64'), relay.reshape(var_17403.astype('float64'), relay.shape_of(call_17398))) # shape=(12, 6, 11)
bop_17407 = relay.floor_mod(call_17399.astype('float64'), relay.reshape(var_17403.astype('float64'), relay.shape_of(call_17399))) # shape=(12, 6, 11)
func_15421_call = mod.get_global_var('func_15421')
func_15424_call = mutated_mod.get_global_var('func_15424')
const_17409 = relay.const([[-5,-2,6,-6,-1,-3,10,-2,5,10,-10,-7,8,5,-9,4,9,5,-3,-6,-2,7,-5,8,6,6,-5,-5,10,10,-5,5,10,1,-3,-10,-8,-8,-5,-2,8,-7,3,-8,1,2,4,-2,-9,10,2,10,-8,-10,7,-3,10,-10,3,-5,5,10,7,4,5,-8,5,-4,6,-5,7,-10,2,-1,-5,9,6,-9,-9,6,8,-10,2,7,1,-3,-2,7,-2,-8,5,-8,5,1,-2,-10,1,-5,-6,-2,-4,5,-7,-1,1,5,7,6,-3,-7,-5,7,-7,-10,-7,-9,-7,-9,7,3,-9,3,-2,-7,-5,9,-3,6,1,4,8,8,-10,-8,-9,4,-9,-4,-5,7]], dtype = "uint32")#candidate|17409|(1, 140)|const|uint32
call_17408 = relay.TupleGetItem(func_15421_call(relay.reshape(const_17409.astype('uint32'), [5, 28])), 0)
call_17410 = relay.TupleGetItem(func_15424_call(relay.reshape(const_17409.astype('uint32'), [5, 28])), 0)
func_15287_call = mod.get_global_var('func_15287')
func_15290_call = mutated_mod.get_global_var('func_15290')
const_17418 = relay.const([0.948098,3.618453,-2.253951,3.624635,-5.819618,-3.692255,-9.044827,-9.003605,-8.200702,-2.307672,-9.359737,-8.705775,6.627700,-8.844939,7.234888,-3.808175,-4.393182,6.070876,-3.963922,7.149022,2.403693,7.340121,-8.860488,9.777361,7.188639,8.337554,-0.486840,-3.717516,-7.418488,-4.937599,3.780963,-2.608388,-5.903730,-0.037959,-4.518607,-6.833594,0.078378,-7.206933,3.286545,-6.474164,2.176845,5.020253,3.391842,5.802652,-1.757933,-8.895925,-2.320782,2.666949,-3.060580,4.431552,4.462645,-2.003424,4.206130,-9.256894,7.744142,9.212334,4.267254,-5.323595,-5.731597,-1.765939,9.895460,-7.190334,6.159437,-3.459415,4.449064,-6.296086,0.820144,5.000999,7.865260,-0.939961,5.807254,6.118031,-4.192298,4.336275,1.265693,6.470304,-2.238376,-0.246371,-0.965257,3.801704,-8.396525,-4.437599,8.896528,-2.041134,-4.862922,1.123208,-5.362420,-6.460666,-0.040564,7.429634,5.006242,-3.169765,-0.722347,3.319889,6.551610,-5.153377,-7.294773,-3.774532,5.236125,1.971770,2.632014,0.459945,8.024162,-8.119322,0.476584,-5.263778,-7.131369,9.105262,2.794773,9.423787,4.459554,8.810806,0.837698,5.719418,-3.203740,-7.444699,4.263885,-6.516894,7.043686,-4.172175,-1.016139,1.543585,9.166150,-9.942047,0.163465,-5.404255,6.157057,-5.817157,5.990574,2.382400,-0.685958,1.882975,1.971557,3.261036,-1.298544,-0.538841,-9.644501,9.087988,-0.940635,-8.748763,-3.852131,-0.413329,-3.910729,-6.597292,2.518892,-6.288250,8.140407,8.277645,7.056863,2.365964,7.206166,-4.932480,9.407424,4.539472,3.791142,3.255022,-5.863152,-2.551592,-7.707683,-4.801901,-6.275561,-8.629767,-2.217772,5.818166,-2.645505,3.214356,-3.541535,7.194838,-7.462470,0.794917,-5.424691,6.547797,-1.584464,-6.096213,-9.637629,-8.814869,3.566359,-5.291941,7.624353,2.166691,-4.966177,5.606756,-5.626443,-6.935769,7.398428,8.572252,-3.302036,3.381598,-6.216893,0.650429,-7.246185,1.798049,-4.560402,-9.506835,6.982296,4.300360,-8.243786,-9.752767,4.057380,1.205120,-4.299233,9.692350,1.037758,-5.828700,-0.642012,-3.915281,5.026056,-3.708709,0.696826,6.544304,-9.019902,-8.752204,5.589642,7.033054,8.861666,-0.274670,7.144622,-0.403112,-7.876805,-5.003321,0.937266,0.001442,7.924020,-5.049344,-3.383816,3.939874,9.977133,-0.573921,9.842799,2.413030,-0.599724,-8.137764,2.609711,3.527675,7.507321,-8.627774,-3.792680,-4.815793,7.320304,6.062236,-5.222576,-9.326114,-3.353999,6.320028,0.173158,3.256503,-1.799091,5.120673,-8.790021,7.888283,8.328117,-2.319082,0.962186,4.729877,-0.456619,0.177742,6.199073,-3.270884,-0.207189,9.211689,-5.177157,4.791029,0.031275,0.134030,2.503789,9.682657,-4.598287,8.400721,-9.992995,9.204387,8.413295,-8.802325,-0.999789,-8.371650,-7.275613,-1.955357,-8.559976,0.166941,3.317584,-9.745541,4.664907,1.047883,0.818763,7.143814,2.927038,-4.601520,2.060269,1.797871,5.079329,-6.245440,-3.295823,5.212842,0.939693,-3.128394,8.700666,9.213116,-7.258595,-9.372753,3.956919,-6.494395,-7.261704,4.628201,5.945581,-8.928159,4.977610,-3.511006,2.807261,-0.734801,-1.315272,5.548385,7.715630,-9.754813,4.513860,-6.529635,-9.307713,4.224785,6.310307,7.333650,-1.301489,-2.034159,-0.443819,9.121618,-5.339638,-1.529567,-5.794468,-7.899334,5.840132,4.428575,3.557127,3.190100,-0.610438,3.631972,-1.223430,-7.266310,-5.333660,-6.667783,8.161337,-7.934705,7.933131,-7.846225,9.303531,-1.367629,4.373596,4.896587,3.759423,1.758069,-9.994120,7.722936,2.799516,0.474204,-8.741129,-2.105235,9.462315,3.466232,-9.469371,-0.043186,-2.635118,-7.168498,-3.235405,3.309330,-7.854064,-6.906088,2.863571,9.485743,4.776398,-0.496892,-5.473978,-4.981990,9.648394,4.254867,7.611671,4.695876,-2.823158,-0.400747,-2.715718,-4.034575,-9.839722,1.661227,-7.679198,-0.660627,0.872634,-2.947692,9.160963,3.439940,-2.581486,-4.262989,-2.192882,-8.812471,1.595680,1.407660,-6.716611,9.848570,-2.276752,-3.353703,0.107814,8.148602,0.493883,4.235997,-1.013260,1.608309,8.678510,-7.803383,-3.875698,-2.716955,8.009351,6.096195,6.807271,-5.789789,8.282655,-5.971425,1.230553,6.818467,6.598702,-0.862068,6.858582,6.769313,3.889882,-6.669922,-5.383932,-0.655753,-6.728503,3.595369,-1.237091,-1.033187,-5.617428,-1.921580,-4.995789,-3.627105,-3.242483,7.003108,-3.935670,-3.487023,-4.351459,3.723722,3.386127,2.274431,8.999165,5.035027,-0.401719,5.097095,3.594722,7.126629,0.667232,1.371944,-4.072083,3.586550,8.927010,-3.369590,-6.937119,-8.147976,3.012971,-4.344086,-2.337255,-8.184075,0.638424,4.575623,-9.641575,-7.550346,-9.928124,0.835640,-5.454325,-6.967739,6.446953,0.842386,-5.650870,9.966603,1.132057,4.670742,-5.379360,8.932681,9.867328,-1.800339,4.983030,-8.855800,-4.462573,-6.324444,-9.120616,6.945325,6.023358,-5.323847,-1.795846,-9.087407,1.958971,-9.538645,6.818794,3.303289,-1.913178,-3.201720,-1.310487,-6.683120,0.666667,2.010998,8.738476,9.165341,8.001320,-4.131044,8.226224,-8.722554,-8.334981,-5.792795,-3.055472,3.112292,5.528089,-3.799426,-5.726733,7.663793,9.269117,5.791347,2.949606,1.867092,-8.851020,-1.397023,-0.297440,-4.863662,8.172068,0.910054,-7.883479,5.359192,-0.170290,0.186178,-8.471542,-1.958311,3.509817,-8.353053,-4.732266,-2.455766,3.527668,5.853846,4.633583,1.910017,-6.250892,-0.332732,0.164693,1.303603,9.948877,-8.803084,0.522875,1.033839,-2.044640,4.196624,6.262773,-1.813718,-1.716049,2.199688,5.930076,6.671881,9.014034,2.012071,4.798071,-6.403683,2.611364,-6.763633,-3.259503,-1.152432,7.093154,1.821742,5.427384,2.676558,9.500389,0.816969,2.135569,8.100680,-5.955491,4.550616,7.539272,-2.727948,-7.418936,5.828862,-4.647704,-3.824848,5.459884,-0.156264,2.514807,-4.606916,-7.912967,6.894402,-5.597098,-4.164070,2.415992,-5.943238,-1.833231,-0.789041,2.046592,1.616864,7.012418,1.015183,1.985239,4.236946,-4.422526,-8.435827,3.986263,-5.904654,-6.796292,-8.161078,3.767797,-3.555700,4.106851,-4.353171,-2.908701,-4.441824,5.620766,-6.509795,6.737826,0.079981,0.542853,1.641459,-1.125973,7.427045,-8.249524,-2.999104,-8.058011,1.799944,6.309614,6.348590,0.090030,1.007574,7.061128,-8.955695,4.793859,-9.277666,6.439318,2.420174,-5.455094,-0.797864,-2.965776,-6.011607,3.484019,-5.304047,7.242259,-0.052357,4.549249,-2.687263,7.888289,-6.384033,-4.314138,2.276905,-3.075811,8.781926,2.079279,8.732016,9.856331,9.976077,-6.283893,1.131939,8.960268,-2.331806,-1.426944,8.687400,6.056155,-9.366913,8.526299,1.224506,0.683953,-5.655562,-8.907810,-5.314536,8.795141,-0.696785,-2.504252,3.930804,9.363616,-5.227126,-3.074130,2.320249,7.967462,-0.740656,-1.853819,-3.597400,-6.615310,-4.568510,4.825354,-3.392282,-8.377503,-9.499954,8.736739,-4.074898,1.468268,-5.977854,1.208941,-7.466506,6.736839,2.548543,-6.859639,9.106812,-8.617355,-8.358329,8.799311,-8.121359,4.904180,-5.308113,-8.719146,-1.790041,4.042709,-8.346054,-7.437441,-4.254668,7.284470,5.538234,7.820478,-2.416072,8.153806,9.507050,-8.385927,-1.090391,-2.217950,-6.264742,-4.188480,5.540181,7.072511,-9.913441,-1.116408,9.027011,-1.933858,8.677923,-5.552249,8.455418,-3.955274,-7.356915,-4.684245,5.156752,5.111412,2.112321,-9.229984,2.357840,-7.594883,0.489423,-0.388874,-5.936440,-4.878789,2.429613,-9.467365,-2.045000,9.271272,0.230660,9.952168,1.184002,-6.685281,-3.685732,1.902568,-0.809534,8.582800,-1.453908,-8.378445,-3.561459,-8.226917,9.685047,-4.454070,-1.829126,-4.369888,0.386678,-3.183613,-6.790906,-8.160252,1.519276,7.121534,0.284824,3.975426,-7.469258,0.097257,-0.366034,-5.792489,-3.707256,0.737264,6.175507,-5.885977,-1.350047,8.800245,6.674692,8.169798,1.611842,-5.193883,-6.580456,-9.150125,0.522196,9.014659,5.273830,-4.908359,0.842619,-1.012397,8.339873,5.729142,0.193278,8.653057,-8.950838,3.710925,9.628480,1.307628,-9.611813,-8.199337,8.372103,1.903995,-9.810412,-7.577327,-0.971389,-1.893626,7.389326,0.019722,-4.946504,5.289339,0.649051,-2.774707,-1.584134,-3.797947,4.044599,-7.072343,5.528996,2.949143,6.923020,0.702353,2.146726,-5.087365,4.679086,6.824240,-0.443125,4.301947,-4.873110,-4.517919,7.352450,2.990670,9.227090,5.914439,0.127880,-6.823673,-2.660692,-9.272708,7.062878,-2.639115,-4.489817,-2.643736,-2.649586,9.117033,7.713679,4.768078,-0.230746,7.843396,-0.959781,-0.967318,-2.325482,2.632149,-4.939670,-7.574141,-0.405585,0.551555,-7.979899,8.272330,3.028362,8.988998,-8.674402,0.993773,1.603531,-4.549300,0.090569,-9.731805,-6.416784,-2.573587,4.250750,-7.797744,3.414351,4.719205,-2.381248,-4.148296,2.468207,-5.853428,-8.451613,-4.550179,2.813862,4.886842,-5.558110,-5.944235,6.941158,8.027902,3.717178,-5.176930,1.847813,-5.106166,-6.095022,6.684477,8.970020,8.911719,4.332211,8.179165,5.671368,4.041902,-5.506555,-9.593709,-1.160744,4.889868,8.013602,-4.273095,3.381623,-6.152785,0.554084,1.576764,-9.226881,-9.953614,-9.467686,-2.934127,9.400263,6.291984,3.985963,7.961097,-7.606762,5.939151,7.946970,-3.394838,-9.815965,-7.656088,6.546300,-6.777631,2.414860,5.758583,5.615764,2.175389,-0.307271,-7.918187,-0.566474,3.967221,-6.302595,-6.787828,7.096778,-3.760809,-8.825114,7.397634,-7.755831,2.421807,8.763253,-6.169900,-0.649928,3.039296,-8.302313,-1.533097,8.954492,9.001705,-4.178767,4.216554,7.147666,3.554778,0.455263,9.612570,5.937734,0.793101,0.696667,3.862341,3.122434,-2.833061,-8.133055,-9.688497,0.123278,-9.859263,0.047950,0.410362,8.069419,-3.055711,2.992872,7.898979,-6.408129,0.016722,-7.808664,9.029842,9.743176,2.354937,-2.160938,-5.788188,-3.701461,8.329053,-9.054631,-1.918281,-5.496569,-2.023700,-8.704049,-3.590286,-3.132710,-5.256894,-3.989534,-0.481460,-3.520892,0.356313,2.478019,-2.652999,-4.838895,-6.321067,-2.823595,3.410885,6.583602,-0.146151,7.935931,7.093172,2.608906,-8.133565,5.984835,8.791000,-7.103135,5.990681,-2.735907,2.698117,0.655382,-7.411698,-5.007360,-0.377089,8.296137,9.485393,3.443656,3.699902,2.777102,-4.468756,-4.889862,-1.086864,8.709074,4.732707,3.009007,-1.045596,-6.296708,-9.211612,-4.977877,-5.680652,2.840300,-2.638030,-4.158962,4.341823,6.754614,3.300384,-2.338567,4.572522,3.205857,6.232901,2.949461,2.132643,-3.046218,8.032478,7.055454,6.339673,8.726734,4.631042,1.065025,6.831293,5.643242,-8.682226,-1.127059,5.363275,-5.012138,-8.652992,-3.108136,5.587536,3.258392,-4.293124,3.750651,-1.065431,8.183038,-7.219021,-3.508267,-8.433860,-8.112454,7.173384,-5.457852,-5.889783,-6.747579,-1.898310,9.627379,5.640222,-2.688063,5.008838,3.817424,1.119580,0.491252,2.894552,0.791987,3.374360,2.424430,0.508204,3.455538,-3.795603,-9.713857,6.808869,9.325676,6.478666,-3.400931,3.155707,-3.194040,-6.161147,-5.662886,4.658430,6.385687,-5.346552,-0.712077,-1.271300,1.932176,8.685481,-5.579270,3.648530,1.546374,0.884498,2.112014,-9.931663,0.709654,-2.018952,-4.024210,-3.610419,-3.832166,-1.728215,-1.649151,6.559092,-6.358184,5.872243,2.096298,-9.854623,3.184519,-7.891568,-8.001395,-8.751600,3.652786,3.047835,1.149537,-9.534143,-0.331356,-7.596379,6.418946,5.304099,-6.324657,-9.837854,7.531627,-2.753246,7.488892,-9.425962,7.499610,8.891442,5.907080,4.108338,-4.473929,-7.277668,-3.202775,0.880816,-0.923806,4.170320,-7.915724,-7.679934,-9.566298,-9.263212,4.897492,4.761179,-3.179446,-0.229385,-7.515220,-8.914793,1.451232,8.142400,0.178883,1.022752,5.258812,-8.783378,3.892977,-2.398282,9.902022,2.909670,1.192680,-6.728837,8.690085,3.593138,-1.479479,0.990865,-0.095566,2.469893,9.687820,-2.178064,-8.303412,-3.241105,6.922834,5.365838,-2.185132,-1.177126,-4.881244,0.246518,2.116222,2.265670,-8.470840,3.226379,3.237475,-7.114457,2.244642,-0.790063,2.232588,1.684819,8.038046,4.943774,3.964750,4.477035,-4.888920,-1.774590,8.552142,1.787026,-2.028112,-1.987541,-1.974345,-2.377972,0.144593,9.327737,-9.250164,-0.884244,3.417053,5.428847,7.734230,-8.612207,7.973590,4.894892,-2.752859,-4.901235,0.565973,3.926398,1.173753,7.812675,-7.726565,5.384116,-1.956645,-1.455106,4.672702,-2.509523,-6.504466,8.527548,4.834416,-5.869819,1.066401,-1.120754,2.359141,-4.307676,-6.581887,-6.777156,-8.082473,2.091174,8.991802,1.209341,9.580183,7.781237,-1.440471,9.042357,8.963495,-7.092094,-2.591262,3.244625,-8.245562,-3.023832,0.373973,3.438262,-7.768792,-4.572468,-6.285046,-0.747446,-1.549310,1.958820,-0.786442,-5.685617,-9.189955,2.148180,-1.124376,-3.215964,-3.511089,4.231653,4.446290,-3.143434,1.705400,3.391137,-1.385098,0.226688,3.047213,1.354949,4.509770,9.771693,-7.002480,-4.653239,0.747418,6.567594,5.274602,-6.438620,9.565082,-8.380151,8.285671,-6.101921,8.759477,-9.724624,-7.961231,7.095958,-5.037890,8.880593,0.350382,2.719037,1.120462,-0.803296,3.564443,9.816449,5.799889,8.228230,-0.670694,-6.564666,9.665841,-7.318386,8.503625,1.879178,6.660331,-2.903817,-3.713922,5.123589,8.731493,-2.528441,-6.803476,2.479785,4.275811,4.510083,3.417326,8.363638,-3.252332,-3.253786,0.245750,8.483693,1.246188,9.264931,5.403447,9.944218,9.926632,5.185232,2.950153,1.630182,5.856554,-9.517944,8.070405,0.530796,-7.823300,6.843961,8.983790,-3.603325,-7.373747,-2.978075,-6.323204,-9.186787,8.736886,-9.375462,5.869080,3.088150,-4.995523,7.672645,-9.241831,1.732366,-9.310972,-0.040572,-2.064062,-2.259211,3.440761,-1.710853,-5.338524,4.912608,8.819982,0.053905,4.243483,3.763525,-4.509751,6.798970,-4.312135,6.455144,8.093509,-1.629016,-1.396808,0.045773,-5.506121,-9.824842,-7.191796,-9.962411,5.003937,-6.637138,3.349922,-7.325158,-7.530773,-2.192123,-2.421326,-7.105413,2.910847,9.159693,3.824181,7.384337,2.711703,3.207785,9.022875,1.606133,4.584035,-5.651179,8.362543,-4.054153,-7.254328,-4.965677,0.589798,2.806143,-4.016474,-0.071792,3.693965,8.531542,9.927852,-9.149084,-0.098852,6.559554,-0.108524,-5.577272,-5.910858,7.483349,3.579152,-7.841161,-1.953038,-9.194977,-6.726211,9.132197,-7.476024,-5.424759,1.498042,9.519277,-2.136340,6.868770,-2.903727,1.827862,-1.438499,9.701236,-6.783251,-9.981738,3.986122,5.199807,-8.840171,5.814336,6.591655,-9.307889,2.644388,3.178464,3.927155,-3.067167,-4.745533,-2.605721,-0.820407,6.882674,7.235720,-6.559211,-4.641311,4.756084,-2.654367,6.554026,-2.855505,-6.819038,3.717717,-2.634480,-9.904642,-4.515037,-2.376298,2.609958,6.629369,9.581658,7.623485,4.743307,-1.990543,-7.986579,-7.145668,-8.710512,8.747626,-8.492365,-3.721291,4.621890,3.643345,-0.373348,4.794346,-0.786466,-9.082985,9.667816,3.357872,6.473452,2.910781,-1.494955,4.388927,2.052361,5.162054,-4.059334,-3.889785,-4.316317,3.752298,1.427300,3.580854,2.160681,1.906183,8.650962,-8.123790,-9.423290,-0.106995,9.242334,-0.281430,-4.989643,-7.576908,7.997992,8.362286,-3.280812,-6.648153,1.494835,0.824091,4.199651,5.071365,-8.210562,2.507058,-6.580946,3.180671,-2.958089,-9.882482,-9.651864,3.805527,9.474419,2.279692,0.700477,7.914594,8.450880,-1.056975,2.270019,9.991108,0.555799,9.391697,-2.224788,7.816674,-8.821597,-6.706677,-1.604177,-4.910202,-2.219256,8.075639,-6.614286,-6.053405,6.684055,-9.170363,-8.473869,-5.322922,6.019591,8.830603,4.414217,-2.990943,-1.517482,-9.734187,-5.471198,-9.299799,-6.568274,-3.563688,-5.181570,0.316316,0.511679,6.023222,6.241809,0.876388,9.999393,4.408624,8.081470,-2.520860,-4.144868,-8.583137,2.813793,2.430845,-0.192244,-9.290479,-0.163877,3.175569,-7.618850,8.766054,-6.712309,-1.455380,-9.862357,-3.458900,9.716511,1.953211,5.764585,-5.485469,6.655706,4.922918,4.296446,-1.140218,6.812800,-1.055771,-5.794458,8.575542,-1.759853,-7.962037,4.588602,3.647870,7.109557,-8.868383,-2.486532,-0.227958,-2.006390,-6.197736,2.372352,0.265584,-1.964387,-3.490168,-7.065053,5.860268,6.809884,9.309132,9.795646,8.425292,4.532391,7.868039,-4.727234,3.294708,1.392080,3.639662,4.970836,3.936700,-8.150376,-1.825994,-8.891306,8.510239,-1.969397,-9.338797,6.444764,-7.508929,-7.604155,6.043860,8.500645,9.725988,-2.348279,-1.336743,-5.174674,9.217325,1.445325,1.721860,4.070078,-9.903726,7.657845,3.402847,-2.209349,9.271400,-3.507722,-6.802912,-1.987870,-7.955997,-4.666888,-7.614454,4.046851,3.924610,6.737386,-1.532831,4.760956,-6.726762,2.750590,-2.706964,-9.259048,-9.764624,-8.353655,-6.791819,7.837046,5.576236,7.577075,-1.719971,4.814526,-9.263566,-2.941781,0.799950,7.924196,-8.573119,-4.960259,-6.766596,-3.020744,3.893811,1.528189,5.849081,-1.816067,-3.927040,-1.687474,-8.088292,-2.642090,8.048432,6.258540,7.297871,-7.603713,-4.035334,-9.990379,4.497798,7.302688,2.433739,7.982828,0.271571,6.960011,6.773481,-0.742435,2.100993,-2.399342,0.480507,9.293695,-0.400121,-0.053738,-9.014894,-3.766582,-2.791872,-8.649344,-7.799429,-5.652269,-1.551596], dtype = "float32")#candidate|17418|(1690,)|const|float32
call_17417 = relay.TupleGetItem(func_15287_call(relay.reshape(const_17418.astype('float32'), [169, 10]), relay.reshape(const_17418.astype('float32'), [169, 10]), ), 4)
call_17419 = relay.TupleGetItem(func_15290_call(relay.reshape(const_17418.astype('float32'), [169, 10]), relay.reshape(const_17418.astype('float32'), [169, 10]), ), 4)
output = relay.Tuple([bop_17404,call_17408,const_17409,call_17417,const_17418,])
output2 = relay.Tuple([bop_17407,call_17410,const_17409,call_17419,const_17418,])
func_17426 = relay.Function([var_17403,], output)
mod['func_17426'] = func_17426
mod = relay.transform.InferType()(mod)
mutated_mod['func_17426'] = func_17426
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17427 = relay.var("var_17427", dtype = "float64", shape = (12, 6, 11))#candidate|17427|(12, 6, 11)|var|float64
func_17426_call = mutated_mod.get_global_var('func_17426')
call_17428 = func_17426_call(var_17427)
output = call_17428
func_17429 = relay.Function([var_17427], output)
mutated_mod['func_17429'] = func_17429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16743_call = mod.get_global_var('func_16743')
func_16745_call = mutated_mod.get_global_var('func_16745')
call_17445 = relay.TupleGetItem(func_16743_call(), 1)
call_17446 = relay.TupleGetItem(func_16745_call(), 1)
output = relay.Tuple([call_17445,])
output2 = relay.Tuple([call_17446,])
func_17449 = relay.Function([], output)
mod['func_17449'] = func_17449
mod = relay.transform.InferType()(mod)
output = func_17449()
func_17450 = relay.Function([], output)
mutated_mod['func_17450'] = func_17450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17071_call = mod.get_global_var('func_17071')
func_17073_call = mutated_mod.get_global_var('func_17073')
call_17507 = func_17071_call()
call_17508 = func_17071_call()
output = call_17507
output2 = call_17508
func_17509 = relay.Function([], output)
mod['func_17509'] = func_17509
mod = relay.transform.InferType()(mod)
output = func_17509()
func_17510 = relay.Function([], output)
mutated_mod['func_17510'] = func_17510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14341_call = mod.get_global_var('func_14341')
func_14343_call = mutated_mod.get_global_var('func_14343')
call_17613 = relay.TupleGetItem(func_14341_call(), 2)
call_17614 = relay.TupleGetItem(func_14343_call(), 2)
func_16406_call = mod.get_global_var('func_16406')
func_16407_call = mutated_mod.get_global_var('func_16407')
call_17623 = func_16406_call()
call_17624 = func_16406_call()
func_14990_call = mod.get_global_var('func_14990')
func_14992_call = mutated_mod.get_global_var('func_14992')
call_17637 = relay.TupleGetItem(func_14990_call(), 0)
call_17638 = relay.TupleGetItem(func_14992_call(), 0)
func_17234_call = mod.get_global_var('func_17234')
func_17237_call = mutated_mod.get_global_var('func_17237')
var_17659 = relay.var("var_17659", dtype = "uint16", shape = (588,))#candidate|17659|(588,)|var|uint16
call_17658 = relay.TupleGetItem(func_17234_call(relay.reshape(var_17659.astype('uint16'), [588,])), 2)
call_17660 = relay.TupleGetItem(func_17237_call(relay.reshape(var_17659.astype('uint16'), [588,])), 2)
func_14560_call = mod.get_global_var('func_14560')
func_14562_call = mutated_mod.get_global_var('func_14562')
call_17663 = func_14560_call()
call_17664 = func_14560_call()
output = relay.Tuple([call_17613,call_17623,call_17637,call_17658,var_17659,call_17663,])
output2 = relay.Tuple([call_17614,call_17624,call_17638,call_17660,var_17659,call_17664,])
func_17666 = relay.Function([var_17659,], output)
mod['func_17666'] = func_17666
mod = relay.transform.InferType()(mod)
var_17667 = relay.var("var_17667", dtype = "uint16", shape = (588,))#candidate|17667|(588,)|var|uint16
output = func_17666(var_17667)
func_17668 = relay.Function([var_17667], output)
mutated_mod['func_17668'] = func_17668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17071_call = mod.get_global_var('func_17071')
func_17073_call = mutated_mod.get_global_var('func_17073')
call_17678 = func_17071_call()
call_17679 = func_17071_call()
output = call_17678
output2 = call_17679
func_17686 = relay.Function([], output)
mod['func_17686'] = func_17686
mod = relay.transform.InferType()(mod)
mutated_mod['func_17686'] = func_17686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17686_call = mutated_mod.get_global_var('func_17686')
call_17687 = func_17686_call()
output = call_17687
func_17688 = relay.Function([], output)
mutated_mod['func_17688'] = func_17688
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17696 = relay.var("var_17696", dtype = "int16", shape = (6, 8, 15))#candidate|17696|(6, 8, 15)|var|int16
var_17697 = relay.var("var_17697", dtype = "int16", shape = (6, 8, 15))#candidate|17697|(6, 8, 15)|var|int16
bop_17698 = relay.subtract(var_17696.astype('int16'), relay.reshape(var_17697.astype('int16'), relay.shape_of(var_17696))) # shape=(6, 8, 15)
func_14241_call = mod.get_global_var('func_14241')
func_14242_call = mutated_mod.get_global_var('func_14242')
call_17709 = relay.TupleGetItem(func_14241_call(), 0)
call_17710 = relay.TupleGetItem(func_14242_call(), 0)
output = relay.Tuple([bop_17698,call_17709,])
output2 = relay.Tuple([bop_17698,call_17710,])
func_17712 = relay.Function([var_17696,var_17697,], output)
mod['func_17712'] = func_17712
mod = relay.transform.InferType()(mod)
mutated_mod['func_17712'] = func_17712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17712_call = mutated_mod.get_global_var('func_17712')
var_17714 = relay.var("var_17714", dtype = "int16", shape = (6, 8, 15))#candidate|17714|(6, 8, 15)|var|int16
var_17715 = relay.var("var_17715", dtype = "int16", shape = (6, 8, 15))#candidate|17715|(6, 8, 15)|var|int16
call_17713 = func_17712_call(var_17714,var_17715,)
output = call_17713
func_17716 = relay.Function([var_17714,var_17715,], output)
mutated_mod['func_17716'] = func_17716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14151_call = mod.get_global_var('func_14151')
func_14153_call = mutated_mod.get_global_var('func_14153')
call_17720 = relay.TupleGetItem(func_14151_call(), 0)
call_17721 = relay.TupleGetItem(func_14153_call(), 0)
func_16123_call = mod.get_global_var('func_16123')
func_16124_call = mutated_mod.get_global_var('func_16124')
call_17723 = func_16123_call()
call_17724 = func_16123_call()
output = relay.Tuple([call_17720,call_17723,])
output2 = relay.Tuple([call_17721,call_17724,])
func_17741 = relay.Function([], output)
mod['func_17741'] = func_17741
mod = relay.transform.InferType()(mod)
output = func_17741()
func_17742 = relay.Function([], output)
mutated_mod['func_17742'] = func_17742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15045_call = mod.get_global_var('func_15045')
func_15047_call = mutated_mod.get_global_var('func_15047')
call_17837 = relay.TupleGetItem(func_15045_call(), 0)
call_17838 = relay.TupleGetItem(func_15047_call(), 0)
func_16667_call = mod.get_global_var('func_16667')
func_16669_call = mutated_mod.get_global_var('func_16669')
call_17859 = relay.TupleGetItem(func_16667_call(), 1)
call_17860 = relay.TupleGetItem(func_16669_call(), 1)
uop_17861 = relay.exp(call_17837.astype('float64')) # shape=(12, 6, 11)
uop_17863 = relay.exp(call_17838.astype('float64')) # shape=(12, 6, 11)
output = relay.Tuple([call_17859,uop_17861,])
output2 = relay.Tuple([call_17860,uop_17863,])
func_17870 = relay.Function([], output)
mod['func_17870'] = func_17870
mod = relay.transform.InferType()(mod)
output = func_17870()
func_17871 = relay.Function([], output)
mutated_mod['func_17871'] = func_17871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15684_call = mod.get_global_var('func_15684')
func_15685_call = mutated_mod.get_global_var('func_15685')
call_17878 = func_15684_call()
call_17879 = func_15684_call()
func_15088_call = mod.get_global_var('func_15088')
func_15090_call = mutated_mod.get_global_var('func_15090')
call_17880 = func_15088_call()
call_17881 = func_15088_call()
uop_17883 = relay.tan(call_17880.astype('float32')) # shape=(13, 5, 15)
uop_17885 = relay.tan(call_17881.astype('float32')) # shape=(13, 5, 15)
output = relay.Tuple([call_17878,uop_17883,])
output2 = relay.Tuple([call_17879,uop_17885,])
func_17914 = relay.Function([], output)
mod['func_17914'] = func_17914
mod = relay.transform.InferType()(mod)
mutated_mod['func_17914'] = func_17914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17914_call = mutated_mod.get_global_var('func_17914')
call_17915 = func_17914_call()
output = call_17915
func_17916 = relay.Function([], output)
mutated_mod['func_17916'] = func_17916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15696_call = mod.get_global_var('func_15696')
func_15698_call = mutated_mod.get_global_var('func_15698')
call_17926 = func_15696_call()
call_17927 = func_15696_call()
var_17937 = relay.var("var_17937", dtype = "float32", shape = (975,))#candidate|17937|(975,)|var|float32
bop_17938 = relay.bitwise_xor(call_17926.astype('uint32'), relay.reshape(var_17937.astype('uint32'), relay.shape_of(call_17926))) # shape=(975,)
bop_17941 = relay.bitwise_xor(call_17927.astype('uint32'), relay.reshape(var_17937.astype('uint32'), relay.shape_of(call_17927))) # shape=(975,)
func_16173_call = mod.get_global_var('func_16173')
func_16174_call = mutated_mod.get_global_var('func_16174')
call_17946 = relay.TupleGetItem(func_16173_call(), 0)
call_17947 = relay.TupleGetItem(func_16174_call(), 0)
func_4470_call = mod.get_global_var('func_4470')
func_4472_call = mutated_mod.get_global_var('func_4472')
var_17951 = relay.var("var_17951", dtype = "int16", shape = (2, 80))#candidate|17951|(2, 80)|var|int16
call_17950 = func_4470_call(relay.reshape(var_17951.astype('int16'), [5, 8, 4]))
call_17952 = func_4470_call(relay.reshape(var_17951.astype('int16'), [5, 8, 4]))
bop_17963 = relay.floor_divide(var_17937.astype('float64'), relay.reshape(call_17926.astype('float64'), relay.shape_of(var_17937))) # shape=(975,)
bop_17966 = relay.floor_divide(var_17937.astype('float64'), relay.reshape(call_17927.astype('float64'), relay.shape_of(var_17937))) # shape=(975,)
func_17509_call = mod.get_global_var('func_17509')
func_17510_call = mutated_mod.get_global_var('func_17510')
call_17980 = func_17509_call()
call_17981 = func_17509_call()
func_14990_call = mod.get_global_var('func_14990')
func_14992_call = mutated_mod.get_global_var('func_14992')
call_17984 = relay.TupleGetItem(func_14990_call(), 0)
call_17985 = relay.TupleGetItem(func_14992_call(), 0)
uop_17993 = relay.erf(call_17946.astype('float32')) # shape=(6, 15, 4)
uop_17995 = relay.erf(call_17947.astype('float32')) # shape=(6, 15, 4)
output = relay.Tuple([bop_17938,call_17950,var_17951,bop_17963,call_17980,call_17984,uop_17993,])
output2 = relay.Tuple([bop_17941,call_17952,var_17951,bop_17966,call_17981,call_17985,uop_17995,])
func_18006 = relay.Function([var_17937,var_17951,], output)
mod['func_18006'] = func_18006
mod = relay.transform.InferType()(mod)
mutated_mod['func_18006'] = func_18006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18006_call = mutated_mod.get_global_var('func_18006')
var_18008 = relay.var("var_18008", dtype = "float32", shape = (975,))#candidate|18008|(975,)|var|float32
var_18009 = relay.var("var_18009", dtype = "int16", shape = (2, 80))#candidate|18009|(2, 80)|var|int16
call_18007 = func_18006_call(var_18008,var_18009,)
output = call_18007
func_18010 = relay.Function([var_18008,var_18009,], output)
mutated_mod['func_18010'] = func_18010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16151_call = mod.get_global_var('func_16151')
func_16152_call = mutated_mod.get_global_var('func_16152')
call_18094 = relay.TupleGetItem(func_16151_call(), 0)
call_18095 = relay.TupleGetItem(func_16152_call(), 0)
output = call_18094
output2 = call_18095
func_18119 = relay.Function([], output)
mod['func_18119'] = func_18119
mod = relay.transform.InferType()(mod)
mutated_mod['func_18119'] = func_18119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18119_call = mutated_mod.get_global_var('func_18119')
call_18120 = func_18119_call()
output = call_18120
func_18121 = relay.Function([], output)
mutated_mod['func_18121'] = func_18121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16552_call = mod.get_global_var('func_16552')
func_16554_call = mutated_mod.get_global_var('func_16554')
call_18134 = func_16552_call()
call_18135 = func_16552_call()
output = call_18134
output2 = call_18135
func_18148 = relay.Function([], output)
mod['func_18148'] = func_18148
mod = relay.transform.InferType()(mod)
mutated_mod['func_18148'] = func_18148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18148_call = mutated_mod.get_global_var('func_18148')
call_18149 = func_18148_call()
output = call_18149
func_18150 = relay.Function([], output)
mutated_mod['func_18150'] = func_18150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13624_call = mod.get_global_var('func_13624')
func_13626_call = mutated_mod.get_global_var('func_13626')
call_18203 = relay.TupleGetItem(func_13624_call(), 0)
call_18204 = relay.TupleGetItem(func_13626_call(), 0)
func_5136_call = mod.get_global_var('func_5136')
func_5140_call = mutated_mod.get_global_var('func_5140')
var_18225 = relay.var("var_18225", dtype = "int64", shape = (120,))#candidate|18225|(120,)|var|int64
const_18226 = relay.const([-10,6,-4,-1,9,-5,-7,-5,3,10,-4,10,-9,8,-10,1,-1,-9,-3,1,10,-8,-3,6,1,-2,5,8,6,9,6,-5,-6,-10,-5,-3,-9,4,4,-9,-7,1,-2,10,-5,-3,-9,-8,7,8,-8,-8,1,-10,5,-1,10,-6,1,2,5,8,8,-10,3,6,8,10,-8,-6,2,5,9,6,-7,7,6,7,1,-8,7,6,7,-9,-8,10,-4,4,8,3,-10,9,-6,-9,-6,-1,-10,10,-5,-4,6,5,-1,-3,-8,-4,9,-4,2,3,-10,-10,-1,10,3,-1,10,-9,4,1,8,-2,-9,-3,-10,8,1,2,2,8,-8,2,-4,2,-3,-9,8,-10,-10,9,-7,1,7,-10,7,-4,-6,6,9,7,9,-5,-9,-4,-7,-8,10,-2,5,5,1,-9,-8,-8,-3,9,3,10,10,-1,-7,-1,8,-5,7,-5,1,-5,10,-4,-10,-4,-8,5,8,-4,4,-5,1,5,2,-6,5,2,9,-8,-2,10,-9,-9,-10,4,-10,-6,9,-1,-3,-5,-2,-4,4,8,6,-7,2,2,9,-5,4,-2,-5,5,-1,6,7,2,4,7,-9,-5,-10,-4,10,10,3,7,4,-3,2,8,-3,-1,10,7,4,-2,-6,5,-6,-1,4,6,-2,3,-10,3,1,10,-6,3,-10,4,1,-3,-2,-5,-4,6,-10,10,-2,-5,1,-4,-4,-6,-4,-10,10,2,-8,2,-8,10,9,-9,-4,-2,2,9,7,-10,-6,3,-6,1,4,7,-10,-1,6,-10,4,5,-9,2,2,4,2,7,6,3,-9,-1,7,10,2,4,-9,4,7,-4,7,8,-9,9,-1,3,-3,9,-6,3,-6,-6,8,-4,5,2,8,-3,-5,10,5,5,8,7,-4,4,7,-6,-9,10,8,5,-3,3,-1,5,-6,5,6,-10,4,8,-3,6,5,-3,7,-1,6,-8,6,-4,-4,8,3,-8,-3,6,-3,7,10,2,-8,8,8,-3,-9,-9,-6,-3,-7,3,9,6,-6,9,3,-1,-6,-4,-7,9,4,9,4,-8,-2,1,-2,3,-9,4,-4,2,-6,-6,-3,-6,-10,-6,8,-5,5,-2,-2,7,-7,-3,5,-3,-2,-3,2,2,8,-8,4,-7,-1,7,3,-7,4,9,5,-2,1,-4,7,-6,-5,-1,10,-7,-6,8,-6,-8,-7,2,1,1,-9,4,10,-3,4,4,-2,9,-3,5,-4,-2,2,-2,-7,-4,7,-4,-7,4,1,-7,8,10,5,-5,-10,7,-10,-2,4,-3,3,-2,4,-2,-3,-9,9,6,-7,-10,-9,-9,-7,-6,-7,6,8,-10,3,9,-5,10,-8,-7,-7,-1,3,5,-1,5,-2,1,8,-2,5,8,10,3,2,4,-6,-8,-7,3,6,7,10,7,9,-8,1,-6,3,8,1,9,-8,-8,-1,-2,-8,4,9,5,-1,4,-10,2,10,-1,3,-8,-6,-8,7,4,1,5,-1,7,5,5,-2,1,8,-4,-1,-6,9,5,-3,5,-1,5,-1,6,-4,1,10,9,-3,1,-5,2,10,-2,-8,-1,7,3,-10,2,-9,-1,5,9,1,2,8,10,3,4,-10,2,-3,-5,-3,-7,10,-5,8,-2,3,-4,10,-2,-9,6,-1,9,5,-7,1,-3,1,-5,-2,-7,1,-10,9,-5,6,8,-2,-1,10,-7,1,-1,10,3,-3,8,4,-6,-8,1,-2,1,-7,1,2,8,10,6,-5,1,-9,-1,-7,-6,-6,8,6,-2,-4,10,-10,9,-6,-9,6,-9,9,8,7,-8,2,10,7,-1,-4,-9,9,-6,5,-8,-5,5,-4,-9,-10,-5,5,10,-9,7,6,-2,5,2,3,-10], dtype = "int64")#candidate|18226|(720,)|const|int64
var_18227 = relay.var("var_18227", dtype = "int8", shape = (1440,))#candidate|18227|(1440,)|var|int8
call_18224 = relay.TupleGetItem(func_5136_call(relay.reshape(var_18225.astype('int64'), [12, 10, 1]), relay.reshape(const_18226.astype('int64'), [12, 10, 6]), relay.reshape(var_18227.astype('int8'), [1440,]), ), 1)
call_18228 = relay.TupleGetItem(func_5140_call(relay.reshape(var_18225.astype('int64'), [12, 10, 1]), relay.reshape(const_18226.astype('int64'), [12, 10, 6]), relay.reshape(var_18227.astype('int8'), [1440,]), ), 1)
func_13718_call = mod.get_global_var('func_13718')
func_13723_call = mutated_mod.get_global_var('func_13723')
var_18273 = relay.var("var_18273", dtype = "uint8", shape = (2, 200))#candidate|18273|(2, 200)|var|uint8
const_18274 = relay.const([6.626894,1.681187,-3.664116,-5.229919,-5.964085,-0.438885,-5.148106,6.101180,-1.122170,-1.315875,9.690947,-2.768871,5.165028,1.566040,9.908505,-0.455810,1.208416,-1.076238,-5.518474,4.446956,-7.594902,-0.380192,-1.810006,-0.110344,-6.410937,0.968011,4.993931,9.094490,-2.541278,3.981378,-9.872491,4.428628,-1.832095,3.672074,-8.144832,0.861027,-5.053349,1.589787,7.085144,-6.680757,9.103207,5.663937,0.012274,6.167044,8.699914,1.394282,-2.625169,2.663323,1.800378,5.297058,-6.218091,-0.758351,4.107502,6.509531,6.237339,-1.261668,4.663917,-8.304454,5.246411,-7.357321,-4.654614,-4.272937,-1.039942,4.936931,-7.591125,9.883581], dtype = "float32")#candidate|18274|(66,)|const|float32
call_18272 = relay.TupleGetItem(func_13718_call(relay.reshape(call_18203.astype('float32'), [975,]), relay.reshape(var_18273.astype('uint8'), [400,]), relay.reshape(const_18274.astype('float32'), [66,]), ), 2)
call_18275 = relay.TupleGetItem(func_13723_call(relay.reshape(call_18203.astype('float32'), [975,]), relay.reshape(var_18273.astype('uint8'), [400,]), relay.reshape(const_18274.astype('float32'), [66,]), ), 2)
output = relay.Tuple([call_18203,call_18224,var_18225,const_18226,var_18227,call_18272,var_18273,const_18274,])
output2 = relay.Tuple([call_18204,call_18228,var_18225,const_18226,var_18227,call_18275,var_18273,const_18274,])
func_18291 = relay.Function([var_18225,var_18227,var_18273,], output)
mod['func_18291'] = func_18291
mod = relay.transform.InferType()(mod)
var_18292 = relay.var("var_18292", dtype = "int64", shape = (120,))#candidate|18292|(120,)|var|int64
var_18293 = relay.var("var_18293", dtype = "int8", shape = (1440,))#candidate|18293|(1440,)|var|int8
var_18294 = relay.var("var_18294", dtype = "uint8", shape = (2, 200))#candidate|18294|(2, 200)|var|uint8
output = func_18291(var_18292,var_18293,var_18294,)
func_18295 = relay.Function([var_18292,var_18293,var_18294,], output)
mutated_mod['func_18295'] = func_18295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16452_call = mod.get_global_var('func_16452')
func_16454_call = mutated_mod.get_global_var('func_16454')
call_18307 = func_16452_call()
call_18308 = func_16452_call()
uop_18309 = relay.acos(call_18307.astype('float32')) # shape=(13, 5, 15)
uop_18311 = relay.acos(call_18308.astype('float32')) # shape=(13, 5, 15)
func_9294_call = mod.get_global_var('func_9294')
func_9297_call = mutated_mod.get_global_var('func_9297')
var_18325 = relay.var("var_18325", dtype = "float32", shape = (1690,))#candidate|18325|(1690,)|var|float32
call_18324 = relay.TupleGetItem(func_9294_call(relay.reshape(var_18325.astype('float32'), [13, 13, 10])), 0)
call_18326 = relay.TupleGetItem(func_9297_call(relay.reshape(var_18325.astype('float32'), [13, 13, 10])), 0)
output = relay.Tuple([uop_18309,call_18324,var_18325,])
output2 = relay.Tuple([uop_18311,call_18326,var_18325,])
func_18356 = relay.Function([var_18325,], output)
mod['func_18356'] = func_18356
mod = relay.transform.InferType()(mod)
mutated_mod['func_18356'] = func_18356
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18357 = relay.var("var_18357", dtype = "float32", shape = (1690,))#candidate|18357|(1690,)|var|float32
func_18356_call = mutated_mod.get_global_var('func_18356')
call_18358 = func_18356_call(var_18357)
output = call_18358
func_18359 = relay.Function([var_18357], output)
mutated_mod['func_18359'] = func_18359
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16743_call = mod.get_global_var('func_16743')
func_16745_call = mutated_mod.get_global_var('func_16745')
call_18363 = relay.TupleGetItem(func_16743_call(), 0)
call_18364 = relay.TupleGetItem(func_16745_call(), 0)
output = relay.Tuple([call_18363,])
output2 = relay.Tuple([call_18364,])
func_18368 = relay.Function([], output)
mod['func_18368'] = func_18368
mod = relay.transform.InferType()(mod)
output = func_18368()
func_18369 = relay.Function([], output)
mutated_mod['func_18369'] = func_18369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17870_call = mod.get_global_var('func_17870')
func_17871_call = mutated_mod.get_global_var('func_17871')
call_18393 = relay.TupleGetItem(func_17870_call(), 1)
call_18394 = relay.TupleGetItem(func_17871_call(), 1)
uop_18395 = relay.atanh(call_18393.astype('float64')) # shape=(12, 6, 11)
uop_18397 = relay.atanh(call_18394.astype('float64')) # shape=(12, 6, 11)
output = relay.Tuple([uop_18395,])
output2 = relay.Tuple([uop_18397,])
func_18434 = relay.Function([], output)
mod['func_18434'] = func_18434
mod = relay.transform.InferType()(mod)
output = func_18434()
func_18435 = relay.Function([], output)
mutated_mod['func_18435'] = func_18435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17365_call = mod.get_global_var('func_17365')
func_17367_call = mutated_mod.get_global_var('func_17367')
call_18459 = relay.TupleGetItem(func_17365_call(), 0)
call_18460 = relay.TupleGetItem(func_17367_call(), 0)
uop_18481 = relay.sigmoid(call_18459.astype('float64')) # shape=(13, 5, 15)
uop_18483 = relay.sigmoid(call_18460.astype('float64')) # shape=(13, 5, 15)
output = uop_18481
output2 = uop_18483
func_18492 = relay.Function([], output)
mod['func_18492'] = func_18492
mod = relay.transform.InferType()(mod)
mutated_mod['func_18492'] = func_18492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18492_call = mutated_mod.get_global_var('func_18492')
call_18493 = func_18492_call()
output = call_18493
func_18494 = relay.Function([], output)
mutated_mod['func_18494'] = func_18494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13749_call = mod.get_global_var('func_13749')
func_13751_call = mutated_mod.get_global_var('func_13751')
call_18495 = func_13749_call()
call_18496 = func_13749_call()
func_15421_call = mod.get_global_var('func_15421')
func_15424_call = mutated_mod.get_global_var('func_15424')
const_18506 = relay.const([10,8,5,1,6,6,-4,7,9,-9,-1,4,6,-4,7,-8,7,3,10,9,-5,-7,9,10,-9,4,4,3,6,-5,-3,9,10,1,7,5,6,2,3,-3,9,-4,7,-4,-5,5,-3,9,8,3,-1,-7,8,10,1,6,3,4,-7,5,9,-1,4,-6,-1,8,-5,7,-6,7,-10,-9,2,3,4,-5,-7,5,-6,6,10,-9,10,-10,-1,-6,-9,4,-2,3,6,-1,4,-6,7,-10,-5,3,3,4,8,6,6,-9,8,6,-9,7,-3,6,5,10,-4,-9,-4,-10,-4,-2,-6,-3,-4,-10,-6,-8,2,-2,1,8,2,-2,-2,-3,-9,-1,7,-3,2,5,10,8], dtype = "uint32")#candidate|18506|(140,)|const|uint32
call_18505 = relay.TupleGetItem(func_15421_call(relay.reshape(const_18506.astype('uint32'), [5, 28])), 1)
call_18507 = relay.TupleGetItem(func_15424_call(relay.reshape(const_18506.astype('uint32'), [5, 28])), 1)
output = relay.Tuple([call_18495,call_18505,const_18506,])
output2 = relay.Tuple([call_18496,call_18507,const_18506,])
func_18509 = relay.Function([], output)
mod['func_18509'] = func_18509
mod = relay.transform.InferType()(mod)
output = func_18509()
func_18510 = relay.Function([], output)
mutated_mod['func_18510'] = func_18510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17449_call = mod.get_global_var('func_17449')
func_17450_call = mutated_mod.get_global_var('func_17450')
call_18579 = relay.TupleGetItem(func_17449_call(), 0)
call_18580 = relay.TupleGetItem(func_17450_call(), 0)
func_16173_call = mod.get_global_var('func_16173')
func_16174_call = mutated_mod.get_global_var('func_16174')
call_18610 = relay.TupleGetItem(func_16173_call(), 0)
call_18611 = relay.TupleGetItem(func_16174_call(), 0)
output = relay.Tuple([call_18579,call_18610,])
output2 = relay.Tuple([call_18580,call_18611,])
func_18615 = relay.Function([], output)
mod['func_18615'] = func_18615
mod = relay.transform.InferType()(mod)
output = func_18615()
func_18616 = relay.Function([], output)
mutated_mod['func_18616'] = func_18616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16711_call = mod.get_global_var('func_16711')
func_16712_call = mutated_mod.get_global_var('func_16712')
call_18637 = func_16711_call()
call_18638 = func_16711_call()
func_18356_call = mod.get_global_var('func_18356')
func_18359_call = mutated_mod.get_global_var('func_18359')
const_18640 = relay.const([2.292606,-5.969432,-7.202977,5.860512,9.470738,8.165690,-3.946773,2.358614,-3.418344,-7.324931,-9.448081,-9.910120,-7.120281,8.507726,-7.406736,5.164571,-8.625760,7.447021,-9.819960,8.140747,-0.165437,-0.210042,-1.385405,-4.053017,-8.220067,3.040903,4.616116,-4.375651,9.406297,-4.489061,-8.102607,-3.721643,8.531410,1.097654,-9.842176,1.854155,-8.696720,8.348748,3.211439,3.238784,-4.653093,-4.427117,-7.089322,-1.220765,-5.239520,0.232985,-7.303750,1.940827,-5.186492,3.635625,7.616538,2.130548,-1.469399,4.474563,-1.378207,-3.763029,7.598275,2.664335,1.372673,-1.713704,-5.811815,-2.094229,7.351078,-3.492115,4.539501,-0.551615,-3.171731,-2.153749,-7.091467,-8.218653,-7.251609,-8.393860,9.507059,3.835475,8.541415,-3.373896,9.252548,-4.240612,4.785544,-0.526863,-1.445882,1.207090,2.321211,-8.730707,5.896584,-2.349110,8.827104,-0.457521,-7.475748,5.072735,3.867332,4.659352,-8.742068,4.882326,-3.224705,-6.757265,-4.464367,4.142509,5.549984,8.022326,-5.519583,-3.263032,-6.307071,-8.688120,-3.181863,-0.212239,-1.106673,4.726511,3.897117,-8.722024,-7.814365,5.834375,-9.133263,-3.835591,-8.314803,4.545166,-1.637011,-0.262864,-0.177424,3.530488,-4.058029,-1.813355,-0.616035,9.200205,-3.665248,4.466814,5.626936,1.792766,-7.248484,1.203685,0.569478,7.427410,8.901730,3.730616,5.753237,-1.806981,-0.395325,-7.331282,-5.458664,1.654456,0.283256,-3.774302,7.273708,-8.884476,6.035363,-4.864540,-1.355538,-8.015062,5.509270,3.596094,6.835299,-4.330904,-4.281072,-4.881372,-6.185603,7.320820,-4.774194,-8.398338,1.322379,4.265075,7.969544,-3.927229,-2.060287,2.216736,-7.598076,-7.089863,-9.280698,4.336998,0.722596,-9.734157,6.745195,4.068096,5.487629,7.787183,-0.088415,4.079829,-8.422638,-6.442967,6.781622,-8.551270,-8.544103,5.721544,8.489422,-6.213408,-3.041309,8.025300,-6.353211,2.301277,-4.784137,9.756226,-2.664428,-9.845143,-9.638640,9.424024,-8.200580,5.833780,-7.184966,-8.725319,9.703903,-9.310761,4.300633,-3.414748,-4.373556,8.742474,-6.288022,9.614225,4.375148,-7.138372,-5.619990,5.488271,7.375825,-0.743400,0.117350,-9.873153,7.174297,-3.524701,-1.418912,-5.035269,2.955697,4.251735,-0.809121,-9.986366,1.593622,5.424401,-7.129914,-1.757985,7.167772,2.132486,4.782388,-5.213357,-9.885840,9.781977,7.166024,8.530357,5.844646,-9.025795,0.143011,-8.909286,3.920037,5.959042,-9.309846,-9.770641,-5.968433,7.491541,9.327802,-3.591397,-8.398241,-8.291372,4.784960,-7.100660,-6.556145,1.025498,6.911395,-0.260708,6.005956,-0.436172,-0.938589,-0.974216,-1.005876,-9.983152,9.826141,8.437429,9.282899,3.537678,6.045535,0.247387,-9.915115,-7.871900,-0.486581,4.933754,-5.303586,-5.076215,-9.330670,4.188321,-7.232132,-4.587999,-4.891483,6.684009,8.851176,-0.259655,7.078678,-5.636948,-4.377370,2.316873,-4.508445,0.254012,2.611323,4.875410,-1.882197,-4.925986,-4.411046,-0.979975,2.129939,-0.965931,-6.166363,9.387324,2.175956,7.002532,-0.110641,-7.316735,9.507248,0.649009,2.240929,-7.518605,7.658514,-6.193224,1.246305,-8.807526,4.001140,7.742304,-6.332614,3.374411,2.861054,9.954408,9.269056,-6.025549,5.402092,5.658883,-9.246647,-3.340904,3.201209,7.949383,5.462158,5.703895,2.739139,-2.978505,4.892217,1.280342,7.060809,6.237230,-0.681268,1.345580,3.065256,6.005740,6.320199,-1.672448,-3.640582,0.767072,6.352080,-0.479082,-1.851469,-3.548400,-0.422871,-7.116412,4.489407,5.916130,8.376260,3.704731,7.575461,-1.545891,7.256724,4.410771,-0.688973,1.897850,0.939688,-3.015460,3.898337,-4.750610,-7.153784,1.128253,-8.561772,-8.647223,3.589775,-9.091978,-3.523799,8.664291,2.967155,2.744404,-7.967808,-1.169174,0.012842,8.308336,7.453151,-2.215730,-0.275243,0.189375,-0.972080,-8.965385,-1.114469,4.331029,2.914822,-2.259699,9.837848,-1.446261,-9.834105,-9.501767,-2.099091,-6.400107,6.003754,7.670431,-8.404106,-8.143301,-4.765394,4.865087,1.435325,2.471666,8.937385,-5.230684,-7.219826,-7.018278,6.345778,-6.467398,-3.112177,8.475237,4.955784,8.471360,-1.647863,2.432337,-7.017242,9.083185,6.663551,-6.310730,-7.696273,7.181057,-2.993631,2.099478,-2.932073,2.672306,4.103426,-1.572188,8.646597,-5.767487,1.127102,6.766908,-1.294904,-1.298002,4.505103,7.196564,8.376921,-5.954947,-6.536139,7.293061,5.647673,-3.299971,9.984565,-7.781843,-2.948704,-0.164775,-5.448144,-1.692898,-2.673756,-6.927338,3.920515,3.487202,-7.925146,-2.359624,-6.649868,-4.971307,-6.945718,-3.100121,3.371687,8.357015,5.080748,-8.343932,3.670643,6.179371,7.480631,1.047404,0.605084,1.936582,4.746973,-9.383969,3.329685,3.309510,6.008875,6.424576,-1.166571,0.266256,7.361932,8.399947,-8.398891,-4.205624,-1.471121,-1.657669,3.688036,-9.935240,-6.037294,-7.660660,2.883318,7.527601,0.407488,0.443711,2.780440,0.297314,-0.393433,9.270886,4.778041,-4.034959,-8.799432,3.026459,-1.184739,-6.341409,7.435568,-3.814450,-2.141365,5.484419,4.790083,-7.156562,8.032830,7.086187,-4.285584,-5.894366,-1.381289,-7.362294,-4.051516,-2.302543,5.821820,6.363560,5.998747,6.113187,8.958297,9.909519,4.699226,-1.266693,-1.632519,6.831909,-0.345286,-6.502224,-9.218948,0.568149,5.851938,-4.087055,-3.998024,6.759020,9.451591,-2.260176,7.990052,9.099480,9.471156,-1.959461,5.198835,-3.286907,5.029943,9.970992,2.479623,-9.095155,-6.576681,6.256674,-2.202264,6.020529,0.843658,7.471584,5.942747,-2.937035,-1.612508,-4.698254,-0.556852,2.258922,-3.116100,2.539187,-1.313872,-1.763073,-6.149927,6.284994,-9.722858,4.504778,-6.535921,-5.232699,5.517624,-0.483521,4.023478,-2.253861,-6.416020,-8.591733,-1.905683,-4.253457,4.413573,0.935084,2.376524,4.904278,1.276792,7.381427,4.941097,-8.015313,-3.890131,-2.906854,7.546711,2.826547,-9.901248,-5.488677,-6.353618,4.274052,3.143781,1.548671,-8.614391,-4.002007,3.063390,0.505077,-7.262654,-0.003984,2.534756,-6.966113,5.225078,-2.452181,1.692190,-3.912038,9.417025,-5.110618,-2.834083,2.383835,-2.025420,0.381229,-7.545274,-4.830146,-7.285753,4.465607,7.274078,-7.833912,-1.015641,-3.480594,-5.890996,8.337019,6.806483,-2.841937,9.684660,-4.532933,-1.876113,-6.328391,-3.785377,2.283290,8.331229,-1.026166,-4.179176,2.873633,1.929201,2.080324,-7.531079,-2.955828,-7.590547,7.204937,-2.403194,6.195683,6.200852,4.773484,-3.256668,-7.749267,-3.597622,-5.320446,-6.760389,6.761299,1.137560,8.053777,6.517924,0.800784,-4.717600,1.004709,-8.959361,5.828901,-0.277814,-9.677284,8.428687,-7.710492,4.941399,0.066106,-5.750489,-2.097304,9.398558,8.112785,8.841961,-9.837097,-5.366831,-8.063957,-9.825253,-3.791753,9.979260,1.846871,-9.378932,-7.449154,-5.678589,9.385164,-1.227974,-5.911253,9.806871,-9.687870,9.094902,-2.199959,-7.645500,-7.087775,9.174266,-4.559430,9.396606,5.091513,2.916394,-1.837365,0.284376,0.353228,2.285251,8.463518,1.111836,2.037612,-9.087562,-3.673563,-6.139345,2.196541,-5.167325,-2.600218,9.669461,1.273044,6.779835,-7.823078,3.286460,-2.520774,-9.405958,9.597392,6.172332,-0.172957,-7.665205,2.404937,4.651784,-9.076600,-5.847704,-5.411077,0.556219,-2.332235,4.086584,1.461326,-4.526960,6.535449,-3.910653,8.522034,5.844338,9.014005,-2.423794,-4.018684,-5.943984,2.138050,-9.980596,-5.158437,9.101249,-8.099386,-3.425181,2.875613,-2.155627,8.437993,2.511106,-2.884926,-7.079977,6.367675,-4.435991,-9.936309,-6.783149,2.438485,5.557530,-9.418570,2.897335,8.735700,6.049062,-9.018193,4.945418,-8.139649,-3.296328,4.895498,-6.788344,-6.948869,6.685288,3.660973,-1.995103,-4.868972,5.606575,5.992491,8.027209,-2.044471,7.175817,-6.585535,-6.851821,-3.873653,-9.421697,9.793368,-3.452438,3.583236,-0.893676,0.104802,-7.898391,0.689331,1.618802,-0.883912,4.934170,3.261762,4.881822,-0.782931,-2.847013,9.250834,-5.811676,7.499338,-4.405297,-6.572469,-4.098955,3.635819,0.846490,-6.235378,3.722928,-7.688586,6.929489,-4.379568,6.297505,-1.660713,0.952254,-6.860637,-3.571424,-8.742982,6.882144,2.869888,-4.621036,-9.537692,9.505644,-5.452189,4.134653,-9.175550,-9.306658,6.478932,9.828496,5.113568,6.746631,-8.019042,-2.947979,-2.463392,-1.037986,3.185978,8.812518,-0.219944,-5.587369,0.619241,6.874567,-2.928183,-8.866144,-3.632212,1.462026,-1.597793,4.667766,-6.521539,5.629860,1.124187,-5.836420,6.910398,-8.610957,5.201941,-2.710000,-2.294515,-8.942580,-9.501074,5.290352,-1.887986,-6.237196,9.813087,4.018894,4.918163,7.815589,-2.154389,6.018571,5.720554,-8.499999,-7.697058,5.054971,-5.742994,0.041385,4.540525,3.000044,8.888055,-2.252077,-4.807346,-6.499218,0.165563,-5.179260,-4.350429,8.152873,-0.275903,-4.753936,-4.752082,0.359274,5.934009,7.132416,7.279731,-1.862615,6.371970,-5.083394,-4.716655,7.965908,-1.549635,-8.595839,-3.429317,-7.513179,9.176815,4.118803,-1.784127,-5.318008,-0.565289,-3.984272,0.660459,-5.193129,-5.426064,-2.225049,-7.684466,-0.393161,1.395804,8.460678,-0.123240,-8.842362,-1.734827,1.122593,8.934909,-1.710229,-5.933703,5.113272,6.293660,-9.773139,-4.067516,-8.972441,-2.000388,4.613617,1.716106,2.265192,-0.576416,2.987198,-4.160740,-1.230537,3.060983,4.255434,6.016758,6.816860,-2.974156,-4.546158,-4.339655,6.002646,0.972377,-6.200879,2.473516,-4.555838,-4.877664,-9.315381,9.381968,-0.987383,3.058101,-4.876882,-7.034928,5.559444,7.926340,-0.421893,8.353812,-4.213816,-4.784726,9.475168,0.083153,-2.767072,-8.836310,-5.632502,9.602896,-7.744328,-4.027456,4.912948,-4.225224,7.155870,6.407824,7.085204,-6.299478,6.734241,-1.302960,-9.448522,7.789665,2.144036,-4.337009,5.200280,-0.887659,-3.418628,-8.183058,-3.655720,4.871438,-0.615016,7.985512,9.703500,0.742776,-0.103001,2.874970,6.021462,3.855534,-7.608653,-5.180610,7.742415,1.578100,7.730171,-1.168904,-2.713362,-1.840558,-8.193518,-2.426699,9.060359,-1.282647,-0.305966,-3.342838,-0.617405,-2.788510,4.984992,-7.699095,-6.002842,1.798027,2.023095,2.154156,5.964189,-4.123288,1.871322,9.156303,1.945864,-0.104300,4.990761,7.113335,7.980743,3.081366,2.828099,9.546934,6.175687,9.285462,-3.611051,8.443779,-5.598773,1.905037,-8.455149,-0.214977,1.323028,2.208822,-2.518664,-6.803791,6.508894,-3.712927,-3.063258,-7.331426,-1.584783,-3.227167,-9.279281,-6.857900,-9.366828,-7.618681,-5.337168,-2.263085,9.569206,5.772385,-3.909435,0.857856,6.947439,-5.494062,-1.353252,1.236338,4.994666,4.346823,9.571877,-6.819807,-2.219374,5.036361,-8.305473,-1.278786,3.644478,0.940252,6.079616,4.973870,-6.792248,-1.720360,-3.931607,-5.199590,-9.748790,1.525288,6.376365,7.063760,-3.898300,9.166139,-0.021800,7.841386,0.454941,6.826960,2.998520,1.115409,6.071825,-2.857293,4.424355,0.180312,1.711924,-2.799585,-1.365195,-3.694526,-7.320486,9.087366,4.664706,-4.055815,8.390296,7.606970,4.221389,8.714230,7.750470,-2.023212,-6.362859,-6.151086,3.609128,-5.514311,-4.591661,-2.214871,-9.858791,8.971163,-0.303283,-3.994238,5.900254,3.137352,-9.204026,2.444935,-0.570888,6.878242,1.035399,-6.363762,-4.650860,3.846626,8.737978,6.653248,3.476001,9.381984,-2.885991,-8.155066,-5.005442,-2.770206,-8.704013,-8.512901,-8.875208,1.370504,3.409186,-7.544962,-6.941969,-9.955300,0.969312,-1.936850,-4.911458,6.089241,5.750299,-2.830469,9.728297,2.631796,4.414265,-0.424317,5.615165,4.791583,-8.083750,-5.358141,0.320024,-8.315277,-9.075353,-7.691296,6.441356,3.259783,0.448223,-2.215693,9.581400,-5.675902,7.904726,-4.450366,-7.988907,9.729578,7.328664,9.621517,-0.211099,1.500412,-3.064970,4.268193,6.204443,8.026294,-5.930504,8.686367,3.701460,-1.586453,6.172511,1.677663,6.470302,-3.073622,-1.801036,8.960567,6.036965,6.863402,-0.595592,2.020561,4.154758,-6.595344,-7.231444,2.257446,9.870741,-3.956972,-6.820559,-5.257724,-8.630990,-3.807942,9.729653,6.501659,3.356100,-2.244540,8.724150,2.341908,-2.555461,2.301175,-0.324201,-9.105986,-4.805985,-0.833105,-9.442777,-0.395270,1.990379,4.865587,3.664368,3.291312,6.514062,-7.709469,-0.650222,-2.833411,-7.424569,2.558947,-3.530068,-9.114323,8.833455,-1.762147,-8.095699,-7.900512,4.316072,-4.411726,3.253415,1.982871,0.437493,5.556202,-7.518058,9.715625,1.721323,8.332363,-2.671231,2.107384,-5.181558,-5.540339,-4.115546,-3.724989,-9.635906,-9.042175,-1.965911,4.994184,-8.691754,7.846040,-1.258960,6.894243,-1.961503,7.215492,-2.223254,-7.852659,-2.659846,1.490744,9.511046,6.694515,-1.334477,2.140569,1.672206,6.322170,-6.474266,-7.251561,7.727604,-9.624095,-5.065100,-6.352956,-9.422833,5.352088,7.271673,-0.633946,-7.113660,1.924908,3.528495,-7.856485,9.232853,-1.388822,-0.297873,-1.329606,-2.916642,2.123802,-1.239630,-2.437193,-4.087533,-0.854494,-9.980659,8.967891,-8.181126,-3.454205,2.314870,-5.862283,-3.181331,-5.568195,-9.712290,-1.196895,-5.228492,4.654098,7.313460,0.815908,-0.443369,-6.451645,-3.706752,5.276251,-6.881598,1.806012,-4.714507,-0.616193,-5.016103,-8.273936,8.445403,-0.909689,-3.739097,-3.483691,9.583424,-1.538788,9.234978,-8.353931,-9.368647,-7.019588,0.580120,-9.170866,-6.159030,-5.018478,-4.022303,6.229604,6.879490,5.900256,8.065752,-8.936311,7.481522,-6.093097,9.916491,7.516218,4.678241,-5.044020,9.178802,-0.425682,8.724463,-1.747080,5.601791,2.649193,7.046837,1.442325,-8.323266,2.407444,-6.031413,8.082931,7.374854,3.184510,-6.999251,4.933521,-2.779319,2.444411,5.564526,3.886813,0.398735,5.049931,5.991465,-3.606323,-2.607585,-9.873731,6.824420,-4.071029,-0.384996,0.298010,7.540572,-5.086290,8.645554,0.371610,1.221659,1.188740,1.315072,-9.241343,8.492420,2.880275,-4.212225,-1.890486,3.842749,-4.433304,-6.597990,-4.659639,6.344842,-4.590318,3.680211,0.610105,-0.630792,7.000037,4.842092,1.631359,-9.850711,4.738852,-8.154836,3.351433,-7.904813,1.754848,4.081200,2.703185,-1.949901,8.846766,6.550070,-1.200536,-7.680337,-0.594815,9.097490,-7.056320,-9.931566,1.824650,-9.656970,-1.721686,-0.010221,8.817216,5.512284,-3.124549,-2.870388,2.677734,-2.190633,-9.044836,-0.658061,3.783391,-2.983284,7.830440,4.752270,9.757840,2.000746,-3.032592,1.790558,-9.026239,-6.519593,-9.510989,-1.712803,9.568849,1.295763,5.024193,-6.503536,-0.594535,1.395861,9.789339,-8.230949,-1.399578,-5.792467,7.740766,-4.959930,-4.064537,8.035594,-3.343003,9.711224,-2.203661,7.916615,-0.380550,-8.079010,-3.148324,-2.193963,-3.234516,-0.777083,6.389272,-5.091027,-5.008400,-8.042847,1.466838,0.423664,1.717872,5.947079,2.442413,-5.194663,-1.456752,-8.487453,-5.428265,-4.918517,4.439373,1.998696,5.178239,-8.024915,-9.659180,2.819934,-7.791138,1.532398,1.665304,2.931616,8.305178,-9.220590,8.584670,-9.045808,0.813999,-8.746865,5.404473,1.454225,6.972444,-7.194863,-9.942505,-5.046807,-3.447554,3.419305,-3.566017,9.390259,-7.953442,-8.581378,-3.662431,5.563550,0.076069,5.629990,4.179458,-3.135225,-3.867255,-7.654762,-4.770723,7.121909,8.179923,-2.737941,2.766099,8.132541,3.169680,8.109877,7.901638,2.550141,4.840643,1.657497,-0.502953,4.630601,2.785780,6.214101,-5.203660,-2.902674,4.217307,-1.066587,-2.319975,-7.441285,0.806618,-2.434099,-4.966598,8.481625,-9.343059,-4.775718,-0.550621,9.389974,-7.297054,6.890904,6.778445,-0.684306,-0.112102,9.676139,-2.098867,-3.311066,-2.171829,-6.000113,5.579992,-3.119154,0.974863,-1.877909,-6.901171,9.770612,-6.491559,-3.608190,-1.474425,3.812810,4.573576,-8.545235,-4.103047,5.497930,3.502055,-1.766306,1.435121,-8.988772,4.013131,1.481633,-3.489366,-5.600365,0.141359,-2.268693,1.247595,7.910719,-1.805943,0.226689,-0.840334,5.205290,-1.280348,-1.847104,-0.965284,-1.408888,5.658284,-6.553408,-0.170724,1.806028,1.928472,-3.006081,7.362705,9.486953,5.986436,-1.029000,0.432657,8.296365,1.965753,5.389379,-3.351714,-0.083411,4.819928,7.475023,0.454007,-1.407149,-3.858047,-3.500763,-7.462987,8.747090,-8.544842,1.100254,-5.860914,8.329244,1.535117,5.378670,5.102824,9.646126,-9.481054,-1.824962,9.523341,-2.286138,0.578828,8.636510,-0.996516,4.706218,2.544429,-1.662693,4.960280,3.276270,8.239778,-3.392393,-1.176116,5.694931,-4.381167,9.651359,-3.825641,9.302541,-4.268790,0.504575,-4.466981,6.842050,-2.367650,3.713629,2.418644,-1.076909,2.375862,7.559142,-0.869454,9.929523,3.186758,1.365802,-3.507399,3.373328,1.320914,-2.033839,-2.605476,0.287690,3.997810,-0.390737,-2.869805,5.573275,-5.690285,3.696130,-7.715459,8.170405,8.337944,7.569275,-5.211700,-4.661142,-6.206643,9.217227,-2.164993,6.445115,4.159104,1.936038,-1.872873,3.428543,3.866822,3.646915,7.488344,5.837297,1.017183,7.505265,-0.478520,-9.892901,-5.456483,7.276440,-8.557878,-2.604854,-9.488183,6.508266,9.240421,3.534316,-9.527465,-9.946825,-7.235227,-1.582186,-4.750370,2.548732,-5.127626,6.561695,4.145360,9.781445,4.355279,4.011053,0.184936,-2.467030,4.486887,-4.692603,6.177238], dtype = "float32")#candidate|18640|(1690,)|const|float32
call_18639 = relay.TupleGetItem(func_18356_call(relay.reshape(const_18640.astype('float32'), [1690,])), 2)
call_18641 = relay.TupleGetItem(func_18359_call(relay.reshape(const_18640.astype('float32'), [1690,])), 2)
func_17712_call = mod.get_global_var('func_17712')
func_17716_call = mutated_mod.get_global_var('func_17716')
const_18646 = relay.const([8,-10,-4,5,-7,-1,-1,-9,5,-8,-8,-8,-9,-4,-6,10,1,-9,7,4,4,-10,-6,-3,4,6,6,-2,-8,-10,1,2,-9,6,-6,1,-6,5,9,-4,3,5,-3,2,7,-8,3,-10,-1,-10,9,-7,2,6,3,-6,-8,-4,10,-2,8,-5,2,-5,6,-9,5,-7,-7,-10,-2,7,-7,-1,-6,6,-5,-7,8,9,5,8,-4,-9,-9,3,3,-9,10,-9,-5,4,-6,8,-3,10,2,10,-5,9,7,-3,-2,3,4,-10,-9,-10,5,2,2,-6,10,-2,-6,-6,3,-5,4,6,-2,-7,-1,7,-5,-4,1,-5,7,-5,-10,-7,-10,9,2,4,-2,-6,-7,8,4,-1,1,7,3,4,2,-6,4,8,1,-2,2,9,-5,-3,9,5,8,-2,3,-6,-7,-9,10,-9,-9,7,2,-1,2,-7,8,5,-5,8,-2,3,9,-2,-9,-9,3,10,-1,-2,6,4,-1,-9,5,-4,-4,-8,-9,1,3,-6,7,2,6,-10,5,-6,4,-3,-5,-10,4,-3,10,10,-7,10,2,-3,-7,-3,-9,-9,4,-6,10,9,3,8,-7,7,-7,-7,10,-9,3,9,3,-6,1,8,-7,-7,1,4,-6,-4,-9,-1,-1,5,-6,-5,-4,6,3,7,2,-10,9,-3,-6,-7,-7,1,-3,-1,1,-6,9,2,-5,-1,5,10,-7,9,9,6,4,-6,-6,-6,7,3,3,9,4,-2,3,-3,4,-4,7,3,-9,-10,7,1,-7,9,10,7,8,-3,1,1,-7,2,-5,7,1,-9,3,-2,4,2,9,-8,-9,10,-8,-9,6,-10,6,4,-7,8,5,-2,-1,-5,-4,-7,-5,-4,8,9,-5,-4,6,-8,3,3,-6,-6,-1,-7,-5,9,3,-4,-7,4,2,4,-6,-3,10,8,2,3,7,8,6,2,1,8,-1,-3,-10,2,-9,6,10,-5,8,-6,8,6,3,1,6,-3,2,9,-3,10,6,1,-2,8,2,4,10,-2,-10,7,2,4,-6,-10,3,-10,7,-7,-6,10,1,-10,6,5,4,-3,-4,4,9,10,5,-1,1,-3,4,-7,-9,-7,-8,2,-4,10,-9,7,-8,10,-5,6,-10,5,2,1,8,6,-8,-7,3,-8,2,2,2,-3,-4,5,10,10,-9,-5,8,-10,-2,-9,-4,9,4,-8,-3,3,4,3,-5,7,-5,2,6,8,-1,-4,5,3,-5,4,-3,-5,-7,2,1,-8,2,10,2,-9,-4,-9,6,-8,4,9,1,6,-2,9,-8,2,7,-9,9,-3,10,-1,4,9,1,9,2,9,-4,7,-5,1,10,-10,-9,-1,-5,-7,-2,-10,4,7,5,-10,-2,10,-8,7,2,-7,2,-1,-10,5,7,-7,5,9,-9,8,9,-9,8,7,5,4,-3,4,5,9,7,7,9,-9,-6,-10,-4,4,-6,5,-8,-9,-3,-6,4,-2,-1,-10,-4,9,-7,-7,-9,-4,-5,-6,-7,-5,8,9,-7,3,-8,2,-4,-2,-1,2,1,5,-7,8,-6,2,-4,-7,10,3,-3,-9,-6,-7,-1,7,7,7,-10,5,8,1,-10,5,8,-9,-10,5,-1,-3,3,6,9,-5,-8,7,10,10,-6,-10,-2,5,-7,-10,-5,3,-2,-10,-4,-9,5,-10,6,5,-6,6,3,-4,2,-1,6,4,4,-6,-9,1,-5,-9,3,-2,-8,-1,-2,1,6,2,9,9,-2,-4,-1,6,-7,6,-8,3,1,-5,8,8,10,-5,7,-4,8,-1,2,7,-2,-3,3,4,-1,-8,5,-10,-5,-5,10,3,-7,9,2,3,10,2,-4,-9,5,2,3,-6,1,-1,3,9,8,1], dtype = "int16")#candidate|18646|(720,)|const|int16
call_18645 = relay.TupleGetItem(func_17712_call(relay.reshape(const_18646.astype('int16'), [6, 8, 15]), relay.reshape(const_18646.astype('int16'), [6, 8, 15]), ), 0)
call_18647 = relay.TupleGetItem(func_17716_call(relay.reshape(const_18646.astype('int16'), [6, 8, 15]), relay.reshape(const_18646.astype('int16'), [6, 8, 15]), ), 0)
output = relay.Tuple([call_18637,call_18639,const_18640,call_18645,const_18646,])
output2 = relay.Tuple([call_18638,call_18641,const_18640,call_18647,const_18646,])
func_18664 = relay.Function([], output)
mod['func_18664'] = func_18664
mod = relay.transform.InferType()(mod)
mutated_mod['func_18664'] = func_18664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18664_call = mutated_mod.get_global_var('func_18664')
call_18665 = func_18664_call()
output = call_18665
func_18666 = relay.Function([], output)
mutated_mod['func_18666'] = func_18666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14241_call = mod.get_global_var('func_14241')
func_14242_call = mutated_mod.get_global_var('func_14242')
call_18689 = relay.TupleGetItem(func_14241_call(), 0)
call_18690 = relay.TupleGetItem(func_14242_call(), 0)
func_4470_call = mod.get_global_var('func_4470')
func_4472_call = mutated_mod.get_global_var('func_4472')
var_18714 = relay.var("var_18714", dtype = "int16", shape = (80, 2))#candidate|18714|(80, 2)|var|int16
call_18713 = func_4470_call(relay.reshape(var_18714.astype('int16'), [5, 8, 4]))
call_18715 = func_4470_call(relay.reshape(var_18714.astype('int16'), [5, 8, 4]))
output = relay.Tuple([call_18689,call_18713,var_18714,])
output2 = relay.Tuple([call_18690,call_18715,var_18714,])
func_18716 = relay.Function([var_18714,], output)
mod['func_18716'] = func_18716
mod = relay.transform.InferType()(mod)
mutated_mod['func_18716'] = func_18716
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18717 = relay.var("var_18717", dtype = "int16", shape = (80, 2))#candidate|18717|(80, 2)|var|int16
func_18716_call = mutated_mod.get_global_var('func_18716')
call_18718 = func_18716_call(var_18717)
output = call_18718
func_18719 = relay.Function([var_18717], output)
mutated_mod['func_18719'] = func_18719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14452_call = mod.get_global_var('func_14452')
func_14454_call = mutated_mod.get_global_var('func_14454')
call_18759 = relay.TupleGetItem(func_14452_call(), 3)
call_18760 = relay.TupleGetItem(func_14454_call(), 3)
func_2670_call = mod.get_global_var('func_2670')
func_2674_call = mutated_mod.get_global_var('func_2674')
const_18770 = relay.const([-3.892242,5.637138,1.109778,-0.766593,-9.271895,-1.021904,-2.046155,-6.732401,2.144431,8.898181,4.499941,-7.661425,5.110833,-2.108824,0.895542,-4.948680,-1.639957,8.103507,8.305124,-6.941489,-7.461613,0.843308,-6.123562,2.217302,4.829487,6.455995,-8.499835,-6.227320,5.971259,-8.415705,-3.496538,0.607354,5.137227,-6.912304,-3.733878,-8.355539,6.910922,7.205267,8.784726,-3.949398,1.388202,-6.431114,5.558286,0.326411,1.795239,5.783407,8.236603,-8.162274,-2.229681,9.807037,6.514435,1.975104,8.710567,-9.875305,5.754344,-6.630263,0.660471,-9.770806,0.145298,5.425830,-1.298236,6.717462,5.919302,-7.280026,-1.016224,-2.635979,8.111149,2.240939,1.767598,9.787438,-8.948690,3.573654,-9.266794,-6.906280,-0.439381,-4.057958,3.332173,-2.157385,-5.147446,-7.988481,-2.804754,-5.771649,-5.789698,-1.547000,-5.575750,9.013416,2.019732,-9.923559,-3.275455,-2.263251,-4.268227,2.077229,-4.043274,3.116807,-0.274035,8.852238,-2.074830,-8.711533,1.863775,-9.817891,3.612500,-1.459949,0.644058,-2.608335,-1.443897,-3.063307,-8.190987,-8.482802,4.408074,2.430289,7.496127,-5.886083,-4.240642,-7.745091,5.535794,8.259858,-1.366212,-3.483613,-5.000259,-8.522275,2.952158,-9.361077,-3.395310,-5.606093,-7.291892,-0.451774,-1.583126,1.025189,2.618271,5.222206,6.815147,5.244297,-4.118733,4.143808,3.190733,8.674622,-1.090310,-2.887583,-4.288059,-5.462814,-4.290900,-5.712752,6.123394,1.709488,-4.154210,3.122545,-8.792410,5.078822,-9.969128,0.314938,-9.805721,-8.107579,-0.395395,-5.094535,8.841826,0.766721,3.651875,5.801667,-3.353834,3.464142,7.781230,-2.587607,-1.991697,-2.501391,-7.519573,-2.066367,2.552292,8.303237,9.813404,-6.745453,-2.202957,-8.496837,-4.478411,-1.681344,-9.836736,0.935091,-8.174693,4.895197,9.219450,-6.435105,-0.888767,8.556803,6.865779,1.074610,-8.519680,-8.906460,-3.749749,-9.108974,-0.525258,4.418127,-9.117282,-8.334851,-8.150008,0.813250,3.550370,2.917177,-3.391980,5.774175,3.825346,-2.755976,3.925410,-1.184072,6.611849,-2.039755,7.506067,9.673325,-6.553713,-8.727956,5.332067,-4.285793,7.778531,-9.399230,-7.392978,-2.904585,6.935122,5.891851,5.900400,-0.535971,-0.653303,-0.260774,-5.229403,-3.204840,8.220760,2.074655,-8.337140,2.116296,8.883685,-3.004630,-3.048131,3.650471,4.509774,-1.930298,-1.987140,-7.454778,4.701034,-8.202662,-7.856948,-8.092087,0.008242,-0.463960,5.061927,-5.896316,-1.164962,8.328593,3.569001,-0.701723,2.267271,0.312196,9.508287,4.692637,-9.472957,-6.756189,-0.810391,-0.368181,-3.990863,5.649682,-0.712295,-9.827660,-5.729671,3.571309,-9.859853,7.147315,-4.334100,5.283507,-3.854129,-0.893163,-1.759263,3.636122,5.644810,-3.858375,-4.022254,-8.399417,7.270820,7.444380,-7.899696,5.691141,-7.361409,-8.257760,2.578710,-3.649192], dtype = "float64")#candidate|18770|(280,)|const|float64
var_18771 = relay.var("var_18771", dtype = "uint8", shape = (400,))#candidate|18771|(400,)|var|uint8
call_18769 = relay.TupleGetItem(func_2670_call(relay.reshape(const_18770.astype('float64'), [7, 10, 4]), relay.reshape(const_18770.astype('float64'), [7, 10, 4]), relay.reshape(var_18771.astype('uint8'), [400,]), ), 2)
call_18772 = relay.TupleGetItem(func_2674_call(relay.reshape(const_18770.astype('float64'), [7, 10, 4]), relay.reshape(const_18770.astype('float64'), [7, 10, 4]), relay.reshape(var_18771.astype('uint8'), [400,]), ), 2)
bop_18780 = relay.logical_and(call_18769.astype('bool'), relay.reshape(var_18771.astype('bool'), relay.shape_of(call_18769))) # shape=(400,)
bop_18783 = relay.logical_and(call_18772.astype('bool'), relay.reshape(var_18771.astype('bool'), relay.shape_of(call_18772))) # shape=(400,)
func_18148_call = mod.get_global_var('func_18148')
func_18150_call = mutated_mod.get_global_var('func_18150')
call_18784 = func_18148_call()
call_18785 = func_18148_call()
output = relay.Tuple([call_18759,const_18770,bop_18780,call_18784,])
output2 = relay.Tuple([call_18760,const_18770,bop_18783,call_18785,])
func_18793 = relay.Function([var_18771,], output)
mod['func_18793'] = func_18793
mod = relay.transform.InferType()(mod)
mutated_mod['func_18793'] = func_18793
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18794 = relay.var("var_18794", dtype = "uint8", shape = (400,))#candidate|18794|(400,)|var|uint8
func_18793_call = mutated_mod.get_global_var('func_18793')
call_18795 = func_18793_call(var_18794)
output = call_18795
func_18796 = relay.Function([var_18794], output)
mutated_mod['func_18796'] = func_18796
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18856 = relay.var("var_18856", dtype = "float32", shape = (3, 3, 5))#candidate|18856|(3, 3, 5)|var|float32
uop_18857 = relay.atan(var_18856.astype('float32')) # shape=(3, 3, 5)
func_17388_call = mod.get_global_var('func_17388')
func_17390_call = mutated_mod.get_global_var('func_17390')
call_18863 = relay.TupleGetItem(func_17388_call(), 0)
call_18864 = relay.TupleGetItem(func_17390_call(), 0)
func_16626_call = mod.get_global_var('func_16626')
func_16630_call = mutated_mod.get_global_var('func_16630')
var_18866 = relay.var("var_18866", dtype = "float32", shape = (1, 1920))#candidate|18866|(1, 1920)|var|float32
const_18867 = relay.const([4.642552,-9.133349,8.549676,5.731408,-2.231812,-4.901725,-5.077655,9.729040,-9.324808,-6.433317,9.399424,-6.744050,-3.265953,7.254495,-3.043090,8.579004,4.092197,-7.846944,2.553330,-8.149104,0.977223,-0.058930,4.938437,3.832220,-9.777708,1.374401,8.243876,6.048687,9.145462,9.980449,-0.737348,5.933376,-4.210482,6.846545,-8.788647,3.878845,-7.839393,1.574921,-2.393231,6.733270,9.578449,-9.704912,6.318901,-0.526195,-7.592711,-0.620059,9.251092,4.758046,1.059249,1.351077,-6.377674,-7.567061,8.525215,-1.004038,-5.739564,-4.110838,0.200232,-6.834024,0.917992,7.045864,-5.016146,-9.139398,-8.732031,2.852615,-1.277794,4.528778,-3.108672,8.228338,6.763348,9.276098,-2.829133,1.410532,-6.889896,-4.422697,7.710092,8.331993,2.750221,1.080332,1.141236,-5.125964,7.746235,-2.595898,5.407457,8.352291,-0.529130,-6.619267,4.022374,-5.625274,-8.607243,7.068188,-0.155346,6.113369,-6.178980,0.080719,-3.741027,-7.098380,6.490902,8.566530,-4.919073,-8.754212,8.659723,9.851480,-1.155155,-8.443783,-3.715896,-0.527409,-6.418942,2.078184,-5.243677,5.290622,-9.987235,0.793834,-3.548585,-7.422201,3.817604,3.585266,3.302661,9.667613,-7.042820,-5.446798,3.116202,-7.219979,5.495914,0.603946,-1.922615,-0.479945,-4.642074,2.092408,-0.032443,9.084461,-9.447699,-3.352108,-0.681714,7.206549,9.214140,3.312390,0.229059,-6.187876,1.239082,-6.716016,-3.001377,-3.403498,-4.409973,-1.519242,6.619083,2.765714,-4.464047,-1.833695,1.078851,-4.112262,7.430160,-4.833501,4.780525,9.197379,-4.360723,-6.632534,-8.357214,3.363944,-1.391610,4.875288,7.462667,2.788240,-2.911114,-1.162168,-6.130564,-9.751837,9.014960,-8.978235,-8.031557,6.283903,5.556074,0.608466,0.311531,2.624724,-0.465984,4.000243,4.947989,-5.148537,-4.613777,2.877147,5.196891,9.042968,-5.081014,8.231620,6.438739,8.139759,-9.800667,5.472032,4.062435,-7.405270,1.266576,-6.460445], dtype = "float32")#candidate|18867|(192,)|const|float32
call_18865 = relay.TupleGetItem(func_16626_call(relay.reshape(var_18866.astype('float32'), [8, 240]), relay.reshape(const_18867.astype('float32'), [4, 48]), ), 1)
call_18868 = relay.TupleGetItem(func_16630_call(relay.reshape(var_18866.astype('float32'), [8, 240]), relay.reshape(const_18867.astype('float32'), [4, 48]), ), 1)
output = relay.Tuple([uop_18857,call_18863,call_18865,var_18866,const_18867,])
output2 = relay.Tuple([uop_18857,call_18864,call_18868,var_18866,const_18867,])
func_18892 = relay.Function([var_18856,var_18866,], output)
mod['func_18892'] = func_18892
mod = relay.transform.InferType()(mod)
mutated_mod['func_18892'] = func_18892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18892_call = mutated_mod.get_global_var('func_18892')
var_18894 = relay.var("var_18894", dtype = "float32", shape = (3, 3, 5))#candidate|18894|(3, 3, 5)|var|float32
var_18895 = relay.var("var_18895", dtype = "float32", shape = (1, 1920))#candidate|18895|(1, 1920)|var|float32
call_18893 = func_18892_call(var_18894,var_18895,)
output = call_18893
func_18896 = relay.Function([var_18894,var_18895,], output)
mutated_mod['func_18896'] = func_18896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16711_call = mod.get_global_var('func_16711')
func_16712_call = mutated_mod.get_global_var('func_16712')
call_18903 = func_16711_call()
call_18904 = func_16711_call()
func_2034_call = mod.get_global_var('func_2034')
func_2038_call = mutated_mod.get_global_var('func_2038')
var_18906 = relay.var("var_18906", dtype = "int8", shape = (768,))#candidate|18906|(768,)|var|int8
call_18905 = relay.TupleGetItem(func_2034_call(relay.reshape(var_18906.astype('int8'), [6, 8, 16]), relay.reshape(call_18903.astype('float32'), [975, 1]), ), 1)
call_18907 = relay.TupleGetItem(func_2038_call(relay.reshape(var_18906.astype('int8'), [6, 8, 16]), relay.reshape(call_18903.astype('float32'), [975, 1]), ), 1)
func_13565_call = mod.get_global_var('func_13565')
func_13567_call = mutated_mod.get_global_var('func_13567')
call_18923 = relay.TupleGetItem(func_13565_call(), 0)
call_18924 = relay.TupleGetItem(func_13567_call(), 0)
output = relay.Tuple([call_18903,call_18905,var_18906,call_18923,])
output2 = relay.Tuple([call_18904,call_18907,var_18906,call_18924,])
func_18925 = relay.Function([var_18906,], output)
mod['func_18925'] = func_18925
mod = relay.transform.InferType()(mod)
var_18926 = relay.var("var_18926", dtype = "int8", shape = (768,))#candidate|18926|(768,)|var|int8
output = func_18925(var_18926)
func_18927 = relay.Function([var_18926], output)
mutated_mod['func_18927'] = func_18927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15463_call = mod.get_global_var('func_15463')
func_15465_call = mutated_mod.get_global_var('func_15465')
call_18952 = relay.TupleGetItem(func_15463_call(), 1)
call_18953 = relay.TupleGetItem(func_15465_call(), 1)
output = call_18952
output2 = call_18953
func_18964 = relay.Function([], output)
mod['func_18964'] = func_18964
mod = relay.transform.InferType()(mod)
output = func_18964()
func_18965 = relay.Function([], output)
mutated_mod['func_18965'] = func_18965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17914_call = mod.get_global_var('func_17914')
func_17916_call = mutated_mod.get_global_var('func_17916')
call_18980 = relay.TupleGetItem(func_17914_call(), 0)
call_18981 = relay.TupleGetItem(func_17916_call(), 0)
uop_19002 = relay.atanh(call_18980.astype('float64')) # shape=(13, 5, 15)
uop_19004 = relay.atanh(call_18981.astype('float64')) # shape=(13, 5, 15)
output = relay.Tuple([uop_19002,])
output2 = relay.Tuple([uop_19004,])
func_19007 = relay.Function([], output)
mod['func_19007'] = func_19007
mod = relay.transform.InferType()(mod)
mutated_mod['func_19007'] = func_19007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19007_call = mutated_mod.get_global_var('func_19007')
call_19008 = func_19007_call()
output = call_19008
func_19009 = relay.Function([], output)
mutated_mod['func_19009'] = func_19009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16151_call = mod.get_global_var('func_16151')
func_16152_call = mutated_mod.get_global_var('func_16152')
call_19063 = relay.TupleGetItem(func_16151_call(), 0)
call_19064 = relay.TupleGetItem(func_16152_call(), 0)
output = call_19063
output2 = call_19064
func_19065 = relay.Function([], output)
mod['func_19065'] = func_19065
mod = relay.transform.InferType()(mod)
output = func_19065()
func_19066 = relay.Function([], output)
mutated_mod['func_19066'] = func_19066
mutated_mod = relay.transform.InferType()(mutated_mod)
var_19122 = relay.var("var_19122", dtype = "int32", shape = ())#candidate|19122|()|var|int32
var_19123 = relay.var("var_19123", dtype = "int32", shape = (1, 7, 9))#candidate|19123|(1, 7, 9)|var|int32
bop_19124 = relay.bitwise_or(var_19122.astype('int32'), var_19123.astype('int32')) # shape=(1, 7, 9)
func_16695_call = mod.get_global_var('func_16695')
func_16697_call = mutated_mod.get_global_var('func_16697')
call_19142 = func_16695_call()
call_19143 = func_16695_call()
output = relay.Tuple([bop_19124,call_19142,])
output2 = relay.Tuple([bop_19124,call_19143,])
func_19147 = relay.Function([var_19122,var_19123,], output)
mod['func_19147'] = func_19147
mod = relay.transform.InferType()(mod)
var_19148 = relay.var("var_19148", dtype = "int32", shape = ())#candidate|19148|()|var|int32
var_19149 = relay.var("var_19149", dtype = "int32", shape = (1, 7, 9))#candidate|19149|(1, 7, 9)|var|int32
output = func_19147(var_19148,var_19149,)
func_19150 = relay.Function([var_19148,var_19149,], output)
mutated_mod['func_19150'] = func_19150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17388_call = mod.get_global_var('func_17388')
func_17390_call = mutated_mod.get_global_var('func_17390')
call_19170 = relay.TupleGetItem(func_17388_call(), 0)
call_19171 = relay.TupleGetItem(func_17390_call(), 0)
func_13017_call = mod.get_global_var('func_13017')
func_13019_call = mutated_mod.get_global_var('func_13019')
call_19172 = func_13017_call()
call_19173 = func_13017_call()
func_14855_call = mod.get_global_var('func_14855')
func_14857_call = mutated_mod.get_global_var('func_14857')
call_19174 = func_14855_call()
call_19175 = func_14855_call()
func_6191_call = mod.get_global_var('func_6191')
func_6194_call = mutated_mod.get_global_var('func_6194')
const_19183 = relay.const([[4,2],[-7,5],[-3,-10],[9,-2],[-10,-6],[8,-7],[-7,-7],[-2,8],[-7,7],[-1,3],[-7,6],[8,-2],[5,-7],[-6,-7],[1,3],[4,-1],[-4,-7],[1,9],[-5,-1],[-3,1],[-1,-2],[-3,9],[2,9],[-5,-9],[1,4],[-5,9],[5,5],[4,-9],[-6,-1],[1,-3],[4,-1],[6,-8],[3,10],[-4,-10],[-10,-1],[10,-1],[-9,5],[4,3],[4,9],[-3,9],[-10,3],[-10,4],[-5,6],[3,4],[-2,3],[7,-6],[-1,10],[-5,-9],[-10,10],[5,-1],[1,10],[9,-7],[10,-8],[8,-9],[10,-5],[10,1],[-8,1],[-7,6],[2,-1],[7,-1],[-9,-6],[-3,-8],[-6,-10],[-8,-8],[2,-10],[2,4],[-1,6],[-4,-6],[5,10],[7,-5],[-4,1],[5,-8],[7,-5],[-3,4],[5,-1],[8,-2],[7,5],[3,-1],[4,-8],[-9,6],[-4,6],[2,-9],[-3,-6],[8,-6],[-1,1],[10,8],[3,-10],[2,-10],[-7,-4],[-10,7],[-5,-4],[10,-8],[-10,4],[2,-3],[10,7],[9,10],[6,8],[9,9],[8,-5],[-3,9],[3,-5],[-7,-9],[-2,-1],[-6,9],[-7,7],[-2,-7],[10,-9],[6,-10],[3,-5],[-4,9],[3,-6],[-3,2],[-4,3],[5,-4],[-4,2],[3,3],[7,-6],[4,-6],[-5,7],[-1,-5],[6,-1],[-10,8],[10,-3],[1,-6],[-4,1],[10,-7],[4,-3],[1,-8],[-8,9],[-5,-9],[10,5],[10,2],[-8,3],[2,10],[-2,-9],[-3,-1],[7,8],[-1,-7],[10,2],[5,-5],[-7,-10],[-8,5],[5,4],[-2,-10],[7,2],[-4,-8],[-3,6],[4,-1],[-10,10],[-3,-10],[10,8],[-9,2],[6,-3],[-5,7],[-9,5],[6,4],[9,6],[10,2],[-7,3],[-9,-1],[1,5],[3,3],[7,-7],[4,-1],[-7,6],[-2,-1],[-9,7],[9,2]], dtype = "uint8")#candidate|19183|(168, 2)|const|uint8
call_19182 = relay.TupleGetItem(func_6191_call(relay.reshape(const_19183.astype('uint8'), [14, 8, 3]), relay.reshape(const_19183.astype('uint8'), [14, 8, 3]), ), 1)
call_19184 = relay.TupleGetItem(func_6194_call(relay.reshape(const_19183.astype('uint8'), [14, 8, 3]), relay.reshape(const_19183.astype('uint8'), [14, 8, 3]), ), 1)
func_17870_call = mod.get_global_var('func_17870')
func_17871_call = mutated_mod.get_global_var('func_17871')
call_19187 = relay.TupleGetItem(func_17870_call(), 0)
call_19188 = relay.TupleGetItem(func_17871_call(), 0)
func_15510_call = mod.get_global_var('func_15510')
func_15512_call = mutated_mod.get_global_var('func_15512')
var_19195 = relay.var("var_19195", dtype = "float32", shape = (169, 10))#candidate|19195|(169, 10)|var|float32
call_19194 = relay.TupleGetItem(func_15510_call(relay.reshape(var_19195.astype('float32'), [169, 10])), 3)
call_19196 = relay.TupleGetItem(func_15512_call(relay.reshape(var_19195.astype('float32'), [169, 10])), 3)
uop_19198 = relay.asin(const_19183.astype('float64')) # shape=(168, 2)
func_3544_call = mod.get_global_var('func_3544')
func_3548_call = mutated_mod.get_global_var('func_3548')
const_19201 = relay.const(-3, dtype = "uint8")#candidate|19201|()|const|uint8
const_19202 = relay.const([-3,8,6,3,-6,2,4,1,-1,9,-9,7,-2,4,-1,-10,-1,-8,-10,10,9,-5,-6,-6,-5,-9,2,2,9,1,8,4,8,6,-6,-5,2,7,6,7,10,10,1,8,-8,10,10,7,8,7,2,9,4,4,-3,3,-8,-7,-3,-1,-6,8,6,6,-1,-10,-7,-8,6,10,4,5,6,-1,9,-1,2], dtype = "uint8")#candidate|19202|(77,)|const|uint8
call_19200 = relay.TupleGetItem(func_3544_call(relay.reshape(const_19201.astype('uint8'), []), relay.reshape(const_19202.astype('uint8'), [11, 1, 7]), ), 1)
call_19203 = relay.TupleGetItem(func_3548_call(relay.reshape(const_19201.astype('uint8'), []), relay.reshape(const_19202.astype('uint8'), [11, 1, 7]), ), 1)
func_14169_call = mod.get_global_var('func_14169')
func_14170_call = mutated_mod.get_global_var('func_14170')
call_19213 = relay.TupleGetItem(func_14169_call(), 0)
call_19214 = relay.TupleGetItem(func_14170_call(), 0)
func_17449_call = mod.get_global_var('func_17449')
func_17450_call = mutated_mod.get_global_var('func_17450')
call_19223 = relay.TupleGetItem(func_17449_call(), 0)
call_19224 = relay.TupleGetItem(func_17450_call(), 0)
func_8857_call = mod.get_global_var('func_8857')
func_8862_call = mutated_mod.get_global_var('func_8862')
var_19234 = relay.var("var_19234", dtype = "uint64", shape = (480,))#candidate|19234|(480,)|var|uint64
const_19235 = relay.const([False,True,False,False,True,True,False,True,True,True,True,True,False,False,False,False,False,False,True,True,True,False], dtype = "bool")#candidate|19235|(22,)|const|bool
var_19236 = relay.var("var_19236", dtype = "int64", shape = (8,))#candidate|19236|(8,)|var|int64
call_19233 = relay.TupleGetItem(func_8857_call(relay.reshape(var_19234.astype('uint64'), [15, 2, 16]), relay.reshape(const_19201.astype('bool'), []), relay.reshape(const_19235.astype('bool'), [22,]), relay.reshape(var_19236.astype('int64'), [8,]), ), 0)
call_19237 = relay.TupleGetItem(func_8862_call(relay.reshape(var_19234.astype('uint64'), [15, 2, 16]), relay.reshape(const_19201.astype('bool'), []), relay.reshape(const_19235.astype('bool'), [22,]), relay.reshape(var_19236.astype('int64'), [8,]), ), 0)
func_16173_call = mod.get_global_var('func_16173')
func_16174_call = mutated_mod.get_global_var('func_16174')
call_19238 = relay.TupleGetItem(func_16173_call(), 0)
call_19239 = relay.TupleGetItem(func_16174_call(), 0)
output = relay.Tuple([call_19170,call_19172,call_19174,call_19182,call_19187,call_19194,var_19195,uop_19198,call_19200,const_19201,const_19202,call_19213,call_19223,call_19233,var_19234,const_19235,var_19236,call_19238,])
output2 = relay.Tuple([call_19171,call_19173,call_19175,call_19184,call_19188,call_19196,var_19195,uop_19198,call_19203,const_19201,const_19202,call_19214,call_19224,call_19237,var_19234,const_19235,var_19236,call_19239,])
func_19240 = relay.Function([var_19195,var_19234,var_19236,], output)
mod['func_19240'] = func_19240
mod = relay.transform.InferType()(mod)
var_19241 = relay.var("var_19241", dtype = "float32", shape = (169, 10))#candidate|19241|(169, 10)|var|float32
var_19242 = relay.var("var_19242", dtype = "uint64", shape = (480,))#candidate|19242|(480,)|var|uint64
var_19243 = relay.var("var_19243", dtype = "int64", shape = (8,))#candidate|19243|(8,)|var|int64
output = func_19240(var_19241,var_19242,var_19243,)
func_19244 = relay.Function([var_19241,var_19242,var_19243,], output)
mutated_mod['func_19244'] = func_19244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16151_call = mod.get_global_var('func_16151')
func_16152_call = mutated_mod.get_global_var('func_16152')
call_19273 = relay.TupleGetItem(func_16151_call(), 0)
call_19274 = relay.TupleGetItem(func_16152_call(), 0)
output = call_19273
output2 = call_19274
func_19281 = relay.Function([], output)
mod['func_19281'] = func_19281
mod = relay.transform.InferType()(mod)
output = func_19281()
func_19282 = relay.Function([], output)
mutated_mod['func_19282'] = func_19282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18119_call = mod.get_global_var('func_18119')
func_18121_call = mutated_mod.get_global_var('func_18121')
call_19344 = func_18119_call()
call_19345 = func_18119_call()
output = call_19344
output2 = call_19345
func_19363 = relay.Function([], output)
mod['func_19363'] = func_19363
mod = relay.transform.InferType()(mod)
mutated_mod['func_19363'] = func_19363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19363_call = mutated_mod.get_global_var('func_19363')
call_19364 = func_19363_call()
output = call_19364
func_19365 = relay.Function([], output)
mutated_mod['func_19365'] = func_19365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19007_call = mod.get_global_var('func_19007')
func_19009_call = mutated_mod.get_global_var('func_19009')
call_19415 = relay.TupleGetItem(func_19007_call(), 0)
call_19416 = relay.TupleGetItem(func_19009_call(), 0)
func_14169_call = mod.get_global_var('func_14169')
func_14170_call = mutated_mod.get_global_var('func_14170')
call_19421 = relay.TupleGetItem(func_14169_call(), 0)
call_19422 = relay.TupleGetItem(func_14170_call(), 0)
output = relay.Tuple([call_19415,call_19421,])
output2 = relay.Tuple([call_19416,call_19422,])
func_19423 = relay.Function([], output)
mod['func_19423'] = func_19423
mod = relay.transform.InferType()(mod)
mutated_mod['func_19423'] = func_19423
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19423_call = mutated_mod.get_global_var('func_19423')
call_19424 = func_19423_call()
output = call_19424
func_19425 = relay.Function([], output)
mutated_mod['func_19425'] = func_19425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17071_call = mod.get_global_var('func_17071')
func_17073_call = mutated_mod.get_global_var('func_17073')
call_19431 = func_17071_call()
call_19432 = func_17071_call()
func_16502_call = mod.get_global_var('func_16502')
func_16504_call = mutated_mod.get_global_var('func_16504')
call_19434 = relay.TupleGetItem(func_16502_call(), 0)
call_19435 = relay.TupleGetItem(func_16504_call(), 0)
output = relay.Tuple([call_19431,call_19434,])
output2 = relay.Tuple([call_19432,call_19435,])
func_19448 = relay.Function([], output)
mod['func_19448'] = func_19448
mod = relay.transform.InferType()(mod)
mutated_mod['func_19448'] = func_19448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19448_call = mutated_mod.get_global_var('func_19448')
call_19449 = func_19448_call()
output = call_19449
func_19450 = relay.Function([], output)
mutated_mod['func_19450'] = func_19450
mutated_mod = relay.transform.InferType()(mutated_mod)
var_19512 = relay.var("var_19512", dtype = "float32", shape = (5, 15, 7))#candidate|19512|(5, 15, 7)|var|float32
uop_19513 = relay.erf(var_19512.astype('float32')) # shape=(5, 15, 7)
func_16711_call = mod.get_global_var('func_16711')
func_16712_call = mutated_mod.get_global_var('func_16712')
call_19517 = func_16711_call()
call_19518 = func_16711_call()
output = relay.Tuple([uop_19513,call_19517,])
output2 = relay.Tuple([uop_19513,call_19518,])
func_19526 = relay.Function([var_19512,], output)
mod['func_19526'] = func_19526
mod = relay.transform.InferType()(mod)
mutated_mod['func_19526'] = func_19526
mutated_mod = relay.transform.InferType()(mutated_mod)
var_19527 = relay.var("var_19527", dtype = "float32", shape = (5, 15, 7))#candidate|19527|(5, 15, 7)|var|float32
func_19526_call = mutated_mod.get_global_var('func_19526')
call_19528 = func_19526_call(var_19527)
output = call_19528
func_19529 = relay.Function([var_19527], output)
mutated_mod['func_19529'] = func_19529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18434_call = mod.get_global_var('func_18434')
func_18435_call = mutated_mod.get_global_var('func_18435')
call_19564 = relay.TupleGetItem(func_18434_call(), 0)
call_19565 = relay.TupleGetItem(func_18435_call(), 0)
func_15684_call = mod.get_global_var('func_15684')
func_15685_call = mutated_mod.get_global_var('func_15685')
call_19575 = func_15684_call()
call_19576 = func_15684_call()
func_16406_call = mod.get_global_var('func_16406')
func_16407_call = mutated_mod.get_global_var('func_16407')
call_19590 = func_16406_call()
call_19591 = func_16406_call()
func_18925_call = mod.get_global_var('func_18925')
func_18927_call = mutated_mod.get_global_var('func_18927')
var_19603 = relay.var("var_19603", dtype = "int8", shape = (768,))#candidate|19603|(768,)|var|int8
call_19602 = relay.TupleGetItem(func_18925_call(relay.reshape(var_19603.astype('int8'), [768,])), 1)
call_19604 = relay.TupleGetItem(func_18927_call(relay.reshape(var_19603.astype('int8'), [768,])), 1)
func_17870_call = mod.get_global_var('func_17870')
func_17871_call = mutated_mod.get_global_var('func_17871')
call_19650 = relay.TupleGetItem(func_17870_call(), 1)
call_19651 = relay.TupleGetItem(func_17871_call(), 1)
func_4833_call = mod.get_global_var('func_4833')
func_4837_call = mutated_mod.get_global_var('func_4837')
var_19657 = relay.var("var_19657", dtype = "int8", shape = (84,))#candidate|19657|(84,)|var|int8
var_19658 = relay.var("var_19658", dtype = "int8", shape = (168,))#candidate|19658|(168,)|var|int8
call_19656 = func_4833_call(relay.reshape(var_19657.astype('int8'), [1, 6, 14]), relay.reshape(var_19658.astype('int8'), [2, 6, 14]), )
call_19659 = func_4833_call(relay.reshape(var_19657.astype('int8'), [1, 6, 14]), relay.reshape(var_19658.astype('int8'), [2, 6, 14]), )
output = relay.Tuple([call_19564,call_19575,call_19590,call_19602,var_19603,call_19650,call_19656,var_19657,var_19658,])
output2 = relay.Tuple([call_19565,call_19576,call_19591,call_19604,var_19603,call_19651,call_19659,var_19657,var_19658,])
func_19669 = relay.Function([var_19603,var_19657,var_19658,], output)
mod['func_19669'] = func_19669
mod = relay.transform.InferType()(mod)
var_19670 = relay.var("var_19670", dtype = "int8", shape = (768,))#candidate|19670|(768,)|var|int8
var_19671 = relay.var("var_19671", dtype = "int8", shape = (84,))#candidate|19671|(84,)|var|int8
var_19672 = relay.var("var_19672", dtype = "int8", shape = (168,))#candidate|19672|(168,)|var|int8
output = func_19669(var_19670,var_19671,var_19672,)
func_19673 = relay.Function([var_19670,var_19671,var_19672,], output)
mutated_mod['func_19673'] = func_19673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18119_call = mod.get_global_var('func_18119')
func_18121_call = mutated_mod.get_global_var('func_18121')
call_19681 = func_18119_call()
call_19682 = func_18119_call()
output = call_19681
output2 = call_19682
func_19690 = relay.Function([], output)
mod['func_19690'] = func_19690
mod = relay.transform.InferType()(mod)
output = func_19690()
func_19691 = relay.Function([], output)
mutated_mod['func_19691'] = func_19691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19448_call = mod.get_global_var('func_19448')
func_19450_call = mutated_mod.get_global_var('func_19450')
call_19710 = relay.TupleGetItem(func_19448_call(), 0)
call_19711 = relay.TupleGetItem(func_19450_call(), 0)
output = relay.Tuple([call_19710,])
output2 = relay.Tuple([call_19711,])
func_19718 = relay.Function([], output)
mod['func_19718'] = func_19718
mod = relay.transform.InferType()(mod)
mutated_mod['func_19718'] = func_19718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19718_call = mutated_mod.get_global_var('func_19718')
call_19719 = func_19718_call()
output = call_19719
func_19720 = relay.Function([], output)
mutated_mod['func_19720'] = func_19720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19423_call = mod.get_global_var('func_19423')
func_19425_call = mutated_mod.get_global_var('func_19425')
call_19727 = relay.TupleGetItem(func_19423_call(), 1)
call_19728 = relay.TupleGetItem(func_19425_call(), 1)
output = call_19727
output2 = call_19728
func_19746 = relay.Function([], output)
mod['func_19746'] = func_19746
mod = relay.transform.InferType()(mod)
mutated_mod['func_19746'] = func_19746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19746_call = mutated_mod.get_global_var('func_19746')
call_19747 = func_19746_call()
output = call_19747
func_19748 = relay.Function([], output)
mutated_mod['func_19748'] = func_19748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16695_call = mod.get_global_var('func_16695')
func_16697_call = mutated_mod.get_global_var('func_16697')
call_19792 = func_16695_call()
call_19793 = func_16695_call()
output = call_19792
output2 = call_19793
func_19797 = relay.Function([], output)
mod['func_19797'] = func_19797
mod = relay.transform.InferType()(mod)
output = func_19797()
func_19798 = relay.Function([], output)
mutated_mod['func_19798'] = func_19798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17313_call = mod.get_global_var('func_17313')
func_17315_call = mutated_mod.get_global_var('func_17315')
call_19833 = relay.TupleGetItem(func_17313_call(), 2)
call_19834 = relay.TupleGetItem(func_17315_call(), 2)
output = call_19833
output2 = call_19834
func_19844 = relay.Function([], output)
mod['func_19844'] = func_19844
mod = relay.transform.InferType()(mod)
output = func_19844()
func_19845 = relay.Function([], output)
mutated_mod['func_19845'] = func_19845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16288_call = mod.get_global_var('func_16288')
func_16290_call = mutated_mod.get_global_var('func_16290')
call_19876 = func_16288_call()
call_19877 = func_16288_call()
output = relay.Tuple([call_19876,])
output2 = relay.Tuple([call_19877,])
func_19882 = relay.Function([], output)
mod['func_19882'] = func_19882
mod = relay.transform.InferType()(mod)
output = func_19882()
func_19883 = relay.Function([], output)
mutated_mod['func_19883'] = func_19883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13565_call = mod.get_global_var('func_13565')
func_13567_call = mutated_mod.get_global_var('func_13567')
call_19929 = relay.TupleGetItem(func_13565_call(), 0)
call_19930 = relay.TupleGetItem(func_13567_call(), 0)
func_6191_call = mod.get_global_var('func_6191')
func_6194_call = mutated_mod.get_global_var('func_6194')
const_19949 = relay.const([7,9,10,-9,-10,10,-1,-2,-4,6,10,-8,-4,-8,1,5,-3,3,-8,-8,3,10,-3,-3,-3,-2,-8,8,7,7,9,-5,6,-8,2,7,-8,-9,9,-9,3,-5,-6,-3,9,2,-1,2,6,-4,-10,4,-7,-10,-7,7,2,10,-5,2,2,3,10,-3,-7,-7,-9,6,3,10,-5,-1,1,7,-4,-7,3,-2,-7,-1,3,3,8,7,5,3,-8,-9,8,2,-4,-10,1,2,-8,-4,1,-4,7,10,3,-2,-2,10,6,1,3,7,-7,3,1,8,-5,1,-8,-5,-6,1,-7,-7,-5,3,4,-3,10,-6,-5,1,1,-3,-4,-9,5,-10,3,7,8,7,1,-2,-7,-2,-5,4,6,4,-8,-2,-4,-7,-10,6,-6,9,-2,10,9,4,6,1,-7,-4,7,10,-8,8,-1,5,9,5,-7,3,-9,-2,-6,9,-8,-2,10,-6,-9,6,1,7,7,1,9,10,2,-4,-4,6,7,7,-8,-6,5,6,3,-6,-7,4,9,-5,7,1,-4,3,3,-1,-1,9,-8,4,10,4,6,-5,-4,-8,-2,2,6,-7,5,1,4,-6,6,-6,1,-8,-1,-2,5,-6,8,3,5,-2,-6,8,2,-4,5,9,-1,-3,-9,-9,-4,3,5,6,6,2,-1,-1,6,3,5,-9,6,1,6,4,-5,2,3,-9,5,10,-2,9,8,1,-2,2,-10,-7,-10,-8,8,-4,9,-9,-5,-10,-1,4,9,-3,-4,2,7,-2,-2,4,10,2,-3,4,1,-4,-1,10,-4,4,7,3,7,2,8,1,6,-7,-6,5,-5,8,7,-9,-2,-8,8,4,1,-7,4,6,3,6,-6,-7,-10,-8], dtype = "uint8")#candidate|19949|(336,)|const|uint8
call_19948 = relay.TupleGetItem(func_6191_call(relay.reshape(const_19949.astype('uint8'), [14, 8, 3]), relay.reshape(const_19949.astype('uint8'), [14, 8, 3]), ), 1)
call_19950 = relay.TupleGetItem(func_6194_call(relay.reshape(const_19949.astype('uint8'), [14, 8, 3]), relay.reshape(const_19949.astype('uint8'), [14, 8, 3]), ), 1)
func_4833_call = mod.get_global_var('func_4833')
func_4837_call = mutated_mod.get_global_var('func_4837')
var_19962 = relay.var("var_19962", dtype = "int8", shape = (21, 4))#candidate|19962|(21, 4)|var|int8
const_19963 = relay.const([-4,-10,-1,-2,1,-4,10,-6,-2,1,10,-4,-3,-8,-7,10,7,-6,2,-1,1,3,-7,-4,-7,-2,-2,-2,7,-3,-2,8,2,8,-10,-4,-2,-4,7,7,7,-1,-6,-4,-4,7,-10,5,-7,-4,10,9,7,1,1,8,-7,-7,-1,-8,-9,-10,10,-1,-8,5,6,-10,-7,-7,-8,8,-3,10,9,-10,3,-9,7,1,8,-5,-1,-5,5,9,-8,-3,-6,-6,3,5,-6,-8,-8,-10,6,-9,10,5,10,1,5,-9,-8,-5,-1,-6,7,-9,4,9,5,-9,6,10,-10,-1,6,-5,7,5,10,-2,-5,2,-2,-3,1,-10,6,2,-3,-10,-5,3,-2,-7,-8,-1,-3,6,6,-2,9,-5,-4,-10,9,3,-2,-7,5,-1,6,7,5,-5,-3,9,1,-7,-10,-1,9,-5,2,-9], dtype = "int8")#candidate|19963|(168,)|const|int8
call_19961 = func_4833_call(relay.reshape(var_19962.astype('int8'), [1, 6, 14]), relay.reshape(const_19963.astype('int8'), [2, 6, 14]), )
call_19964 = func_4833_call(relay.reshape(var_19962.astype('int8'), [1, 6, 14]), relay.reshape(const_19963.astype('int8'), [2, 6, 14]), )
func_18006_call = mod.get_global_var('func_18006')
func_18010_call = mutated_mod.get_global_var('func_18010')
var_19966 = relay.var("var_19966", dtype = "int16", shape = (160,))#candidate|19966|(160,)|var|int16
call_19965 = relay.TupleGetItem(func_18006_call(relay.reshape(call_19929.astype('float32'), [975,]), relay.reshape(var_19966.astype('int16'), [2, 80]), ), 4)
call_19967 = relay.TupleGetItem(func_18010_call(relay.reshape(call_19929.astype('float32'), [975,]), relay.reshape(var_19966.astype('int16'), [2, 80]), ), 4)
func_16552_call = mod.get_global_var('func_16552')
func_16554_call = mutated_mod.get_global_var('func_16554')
call_20000 = func_16552_call()
call_20001 = func_16552_call()
func_14286_call = mod.get_global_var('func_14286')
func_14288_call = mutated_mod.get_global_var('func_14288')
call_20011 = relay.TupleGetItem(func_14286_call(relay.reshape(const_19963.astype('int8'), [84, 2])), 5)
call_20012 = relay.TupleGetItem(func_14288_call(relay.reshape(const_19963.astype('int8'), [84, 2])), 5)
func_17095_call = mod.get_global_var('func_17095')
func_17096_call = mutated_mod.get_global_var('func_17096')
call_20020 = relay.TupleGetItem(func_17095_call(), 0)
call_20021 = relay.TupleGetItem(func_17096_call(), 0)
func_14375_call = mod.get_global_var('func_14375')
func_14377_call = mutated_mod.get_global_var('func_14377')
const_20023 = relay.const([-4.933335,-3.429267,3.616840,0.832750,4.455860,-0.976549,3.348595,-9.925510,-4.002141,6.617783,-9.250903,0.815820,-3.971751,-0.993290,8.032016,-9.233226,-8.091745,-8.186602,3.303185,-3.045603,5.126758,0.139441,6.553475,8.955739,8.583318,-4.416545,6.325104,-5.810956,-0.042746,-6.557866,-2.146821,7.076865,3.202415,2.752089,7.232706,2.551875,-8.169019,9.004513,-7.361317,0.616524,6.409078,7.814007,2.235155,-0.504091,-6.574489,-8.082580,2.413338,0.243614,9.652463,2.620115,-0.520063,2.674460,-1.223480,-4.306198,4.388825,-8.073072,2.930217,4.368046,5.168832,-6.321941,-3.886146,9.047219,-7.108501,-2.782529,9.679488,-3.942918,-4.085045,-0.005899,-8.729228,9.706724,2.790794,-3.965668,1.981728,7.190330,-8.198828,-8.423840,-1.320509,-4.056375,-9.105688,-7.673451,7.993183,-1.397273,-6.265058,-2.970811,5.499085,-8.565046,7.587081,-1.508291,8.861368,-0.788532,9.472669,-1.929929,-6.625922,2.123425,-6.653228,-9.284187,-7.141023,6.533491,9.078589,-2.170156,-0.936462,6.329703,9.379619,-6.835158,-0.391123,-9.927239,-1.789394,7.455887,-2.819388,5.176561,5.277950,-0.231479,-1.113264,-1.797211,7.975086,1.584603,-3.527417,4.400068,-3.893755,-4.262884,-7.807147,-0.096897,2.887957,2.344815,-9.933540,-9.538472,-9.222788,-5.987077,7.158379,6.243812,0.236005,-8.289352,5.281842,8.374092,3.707387,-8.183842,5.213656,-9.823254,8.528087,-8.092039,8.163671,7.399951,4.833710,-8.051470,-9.132984,7.289535,-9.783902,3.919246,9.502038,4.740173,-7.966494,3.382074,9.003540,2.235719,5.294651,-3.318644,-0.979623,5.328176,1.988498,-0.364518,2.362581,6.389773,9.488160,5.243551,-1.996491,-3.450394,6.067690,-9.791991,1.212532,5.390342,1.666338,0.564825,1.922156,5.011041,1.946780,-3.293135,4.728312,-3.164476,5.396734,4.218707,7.062675,-8.613146,5.140065,1.843134,-6.853512,-8.126440,-1.314260,-8.207235,-6.192562,4.230892,3.453616,-1.479426,7.352415,-4.655691,-6.417581,-8.975278,6.607628,-9.348077,3.017253,3.361629,-4.196536,3.727619,-5.106168,-3.414830,8.917974,-8.708210,-5.572305,8.362511,4.378974,-1.286242,-1.904737,1.397393,4.517622,-3.333599,2.782780,9.457821,1.788617,5.427379,-2.206201,-0.682095,8.725317,-3.435138,2.617108,1.415739,1.990099,9.747521,6.995382,4.977734,-5.830464,4.892462,-6.839922,-6.167227,-2.075358,9.581950,6.006985,-9.040331,-7.147453,-2.314643,7.449767,-2.202915,0.079048,-8.834033,7.590744,-1.680023,1.030348,8.784514,-9.795189,-0.164181,8.440170,4.989623,0.365978,8.667422,-4.023914,-8.818956,-4.809739,1.359269,-2.404612,-3.983051,7.446780,2.191283,-7.689210,-8.130173,-4.890109,8.254648,-4.960838,4.165983,0.825232,9.300827,-4.582689,3.393705,1.884629,5.305430,-9.903836,4.587119,-9.371243,-2.121295,6.425170,2.004181,1.870905,-8.700083,3.997058,-4.078508,-1.274725,-1.490254,0.676865,8.828270,-7.997962,-0.685903,-6.141555,7.980633,-6.908195,-0.433019,-8.251461,-6.629989,-2.958699,-5.628142,-3.825252,-9.517463,-0.572350,9.278521,-7.687169,-9.532523,6.852331,9.049957,-3.494257,-6.520879,7.060330,7.458146,-7.033594,1.273599,-8.320590,-8.976423,-2.075051,9.761085,-0.205516,-6.170146,-8.545339,6.508926,4.069543,3.393754,8.512458,4.290148,-1.872230,3.084650,-6.220952,-3.214744,-8.835144,8.588627,3.275707,2.782291,0.207968,4.615438,4.871356,-6.548183,2.004329,-6.307036,2.221807,9.543204,-0.324049,9.361013,-6.780788,9.803395,-5.386806,6.030520,-6.210768,0.811862,0.551949,8.545750,-8.227870,4.612332,9.492075,-2.213409,4.807804,3.418491,-7.646551,-0.177773,-9.427303,0.442935,-5.836426,-4.853700,-7.402799,4.480724,-9.830822,-1.502001,-9.413092,8.721530,5.615475,-8.440077,5.225974,6.057485,-8.254417,-0.893061,0.478410,-0.387424,5.094013,-9.672722,-5.531355,5.866465,-5.074834,4.374987,6.269856,8.205313,0.744112,-4.664701,5.566041,-3.564959,2.180845,-2.065611,7.510063,4.980888,0.229066,-8.768721,1.953197,8.396556,0.098822,-3.537633,5.598299,0.993746,3.181705,9.778079,7.055368,9.543793,9.688330,-3.543769,-0.047649,9.101021,3.930925,5.349820,2.182542,1.912661,-9.698491,1.420420,0.597873,-3.063196,-4.905651,4.256013,6.987737,5.541593,-8.353303,0.140779,7.400553,-1.103517,-3.770000,0.702931,-9.849483,-6.324602,-2.618949,-4.231307,2.636682,-8.721812,1.878392,6.463370,-9.099267,0.231079,-8.583151,4.179970,1.835086,0.928576,-0.968796,6.751894,1.528854,5.920616,4.551105,6.395557,-3.066547,9.008797,1.071221,-7.961480,4.348848,-9.375895,9.315185,6.736295,8.815781,-6.111116,3.681473,7.005802,-6.993903,-2.223561,-9.030067,-8.793952,1.861355,-7.918101,-3.530263,2.372363,-0.980830,-9.597998,9.792449,-9.628186,-5.688804,-5.142165,-1.236043,-1.526763,-1.426830,1.078161,-2.593339,7.128710,6.456350,-7.311980,0.083015,3.045319,1.983118,6.366014,8.070392,3.923180,-2.503476,2.233109,2.247070,6.410402,-7.103711,1.029893,-1.865292,-4.990979,-2.495079,-8.347668,-0.332143,-2.100890,2.582661,9.169814,8.814869,-3.435371,-4.716674,8.787182,6.835391,-0.200329,5.424715,-1.781081,-2.659266,9.302106,2.885701,-5.673413,3.036154,3.515278,-9.381414,3.841498,2.375188,-9.273064,8.034246,-8.632074,-9.518931,-9.734700,-7.817088,-7.586828,5.665639,5.127418,5.839102,1.937906,-4.631410,4.011656,5.940235,2.223523,-5.613326,-0.252934,1.185979,-6.953317,0.455865,1.900585,0.134004,1.909965,1.771489,2.459151,-0.699310,9.205124,9.113132,-2.614544,2.607727,1.766251,0.195795,6.260315,-6.302115,-2.804874,-7.746800,0.197326,6.888024,-7.176165,-9.010075,8.309821,-0.496845,8.350442,5.802496,-9.394877,9.990851,-6.996502,-3.760878,1.341021,1.160927,-3.612602,9.536040,6.704479,-0.080987,2.100203,8.803160,-2.950034,6.348538,6.671013,7.011610,4.476653,-8.298943,4.563585,5.976829,7.389696,-1.433465,-9.130496,-1.338626,8.179023,-1.717762,7.576204,4.271315,8.055876,9.835559,-8.951286,1.884098,-8.631945,3.214781,-8.298041,-7.644380,-4.318258,6.708767,5.386499,-5.197882,2.774236,9.396159,2.800666,-1.736291,-5.963217,8.329769,-8.434009,-8.706123,-3.806247,-1.892003,7.310147,5.168677,5.229365,-7.824879,-7.151025,8.444847,7.198990,-1.548406,-0.086723,-4.548586,-9.106256,3.248553,-8.164510,9.224797,2.968367,8.086391,2.930797,-2.733240,2.064583,5.914709,-2.378655,5.315506,8.115055,-9.661091,-1.112541,-9.836596,-6.664744,1.169612,-6.211399,-7.987316,-3.678030,-3.579534,-0.577071,0.822063,1.483666,3.994582,9.190112,-5.965120,-6.864998,-9.719476,9.654513,3.468259,-7.870747,-3.818375,-5.107252,7.445734,-7.204478,-7.301682,-0.522127,-0.116054,-9.190592,9.648925,3.110461,-0.040432,-1.995183,-3.812513,-0.320258,-9.025042,1.438164,2.512037,1.822170,-0.037503,-2.675569,-6.688876,-2.616014,-7.252438,-1.086370,3.302809,1.501727,7.351254,-2.470347,7.177917,2.140435,-5.867548,-6.720461,-9.214121,-0.690535,6.846038,1.366417,9.569907,5.692277,-6.517176,-2.132153,1.820549,-8.493001,3.816187,-8.067132,7.648942,-4.064384,-2.889034,4.539679,-7.702344,-8.273123,-1.679486,2.558603,2.120935,8.033720,-6.528016,9.654542,-2.861592,-4.743912,1.945557,-5.165283,1.574458,-6.848857,-5.478048,-9.153912,2.630309,-5.360014,8.214692,0.797296,-8.803673,-6.781944,-0.437728,-4.599993,9.032212,2.341653,-3.841088,8.366546,-4.130547,7.779424,6.972415,-1.330970,-7.200927,-2.002549,-1.462134,7.129096,6.786763,-0.528151,5.924450,-3.934072,3.808853,9.083316,0.789709,9.023304,-1.477960,-7.012786,2.914678,-6.140838,-1.162671,2.073047,6.338022,3.882684,-3.537549,-6.978243,2.256726,2.977530,-0.179254,-8.105661,7.955611,-5.804982,-7.513616,-5.687554,3.694797,-8.066121,7.300034,-3.992145,-8.432787,2.630863,7.727558,-6.198196,-3.218946,-7.780575,4.610784,2.670658,-0.504556,-6.929655,-0.010826,-4.825822,-2.912130,3.190311,-5.496249,-4.100395,-3.660646,-2.453144,5.095478,-6.764942,-4.723958,3.655364,8.266971,-3.172874,-4.956499,-3.038819,8.347036,-8.609368,9.422507,-4.037090,5.313398,-2.879237,-5.029281,-8.248613,-6.990858,-8.423680,7.773534,-2.359546,-5.554157,-5.739123,4.241540,6.885821,-8.963327,-3.845506,-7.464328,1.564549,1.785543,3.041008,-0.793879,-6.395085,-2.678964,3.690891,-0.472513,-3.501508,3.073640,9.537829,6.847863,0.397996,-2.769250,-6.567969,-5.100803,-4.987057,3.884981,-3.517972,9.125516,-6.748291,8.821856,7.914287,5.702885,-1.184324,5.692435,-7.186872,-2.976948,-6.588605,8.049098,7.060327,-4.750850,-3.560972,3.526496,-9.919669,8.596792,-6.633894,-6.251103,-8.445296,8.702055,-8.482816,-5.653022,-9.506866,6.774146,4.475143,4.080939,-0.596398,-4.910608,0.437107,8.461809,5.420865,5.670046,8.536102,8.128446,7.509590,-4.136201,1.451116,-6.825227,-1.828362,-7.561981,1.882187,-7.156178,-8.812192,-7.862246,8.562140,1.158651,-6.097608,-1.326332,-6.193276,2.890924,4.289093,-0.312732,-2.633841,-6.646793,-4.287743,-9.134413,-2.167099,9.058507,5.447951,-0.497132,-9.063719,8.060421,-7.852046,-6.992236,-4.880890,7.154510,-8.630764,-0.811053,-4.616409,3.308106,-5.386079,-6.752081,-6.030580,3.633523,9.012957,-1.497867,1.206686,-5.866620,-4.005292,-7.633462,-1.357334,-7.304090,9.846638,2.679810,7.659194,-1.072472,-2.858619,-9.115947,7.364393,1.991004,8.523480,-8.267099,7.147191,9.004086,0.142988,-2.141999,7.293074,-4.366312,-0.875852,-8.336606,-8.753216,6.603732,-5.291974,-5.355447,8.689160,-6.593475,9.104060,5.666888,-8.110882,-5.261775,-8.893433,8.430979,3.225926,1.572527,-0.082657,0.788623,-4.636406,2.955057,-9.809068,-7.690521,5.974082,9.781348,2.153389,-7.898641,1.573577,-8.919032,3.417647,5.699537,5.081284,-5.476758,-1.958746,5.606546,-5.220289,5.254355,-4.064037,-1.681242,6.076580,-3.388548,-9.603223,-8.570949,-3.337609,-8.443812,-9.775550,-9.211052,-7.717773,2.860471,3.839177,1.951190,-9.547686,-3.260926,7.413509,-4.309875,-4.853337,2.258957,9.227667,-8.177675,-2.790964,-7.436239,-6.293143,8.700517,9.672464,-3.736571,9.250184,7.269399,-9.234313,-6.721225,-1.376835,-9.502603,4.646026,-0.409737,2.443140,-5.554644,6.763731,3.717478,-7.130424,-9.571876,1.742041,-9.800019,-0.978594,-5.334590,6.106392,-2.929521,-4.610681,9.195716,3.910387,-6.491029,-4.898799,-1.262266,4.860981,-8.984904,-3.196971,-6.171401,3.521882,-7.919912,-6.776684,-0.997548,2.130568,6.565508,-5.861207,-7.695262,-9.626678,-2.023735,2.269823,-8.196481,-7.286410,-3.300937,2.435252,9.351393,7.455896,4.632676,-0.413291,-1.651677,-9.603924,5.965877,-2.381117,-7.759197,0.448355,5.172664,-7.403323,9.838168,-5.059268,4.456976,-9.173483,-6.303645,5.898774,6.966412,-6.836072,3.655179,-0.754918,4.435300,-5.152647,1.365758,-6.778569,5.007900,0.973537,-5.250652,-2.295542,6.876059,-1.652933,4.946104,3.833034,0.292637,-4.623685,1.429684,-5.903763,7.978187,-4.087363,-2.989072,4.009215,2.275372,-6.715625,0.614867,-4.635339,-2.472895,-2.062690,-1.710415,-5.273367,2.675873,-6.933650,8.808368,1.215729,-9.638224,-0.159790,1.897123,-4.771688,-7.034829,-8.664097,8.227169,-4.574039,6.864619,4.681176,8.786861,6.737130,-1.465929,4.462224,-7.900607,-0.740203,-8.207759,2.463712,4.307568,8.717671,1.848408,1.719861,-2.101469,-1.568304,-3.006205,6.849129,5.378358,3.899811,-8.079455,-5.888732,8.222491,8.831886,4.626861,6.066366,-5.921145,-8.008749,-8.356856,3.173919,7.540516,-3.295224,2.749088,8.501287,5.685463,9.143159,5.763254,-3.237817,-0.556366,9.730363,2.109109,-6.881792,3.631798,9.395841,-0.062329,-1.847318,-4.087321,-7.485410,-1.046459,-0.930995,-8.894245,1.615702,8.675428,-0.464989,-5.874514,9.775580,3.527519,2.874603,-6.526145,-5.298768,5.464693,7.218121,-8.894363,-0.539853,3.803041,-6.006714,-7.061335,-2.370476,5.879938,1.893167,-2.667838,2.258062,0.748352,-7.208387,3.030397,-3.289181,2.833353,-2.962767,9.519186,-6.143680,-7.269495,-6.078625,-7.475686,-5.689052,-9.613781,9.249160,8.362008,-0.378335,-2.698849,-8.791944,6.538575,-9.380647,-1.056210,-0.553669,4.113868,8.346438,6.548898,-3.632323,-2.227728,-6.276633,5.592864,4.069301,-8.038046,4.442255,-2.208286,7.366890,-2.779204,-8.745922,-8.901059,0.746361,0.469326,0.234576,-9.186365,-6.066178,8.018852,3.473825,1.681599,6.613029,-3.403222,-4.102910,-6.747219,8.548049,0.409835,-2.474986,-5.455934,-2.833824,-2.673355,1.716876,4.012941,0.639336,-6.879182,9.507477,9.334876,0.564616,0.609226,-7.097621,8.910840,3.452369,2.618095,5.324704,0.664644,4.802458,3.337331,-6.941831,-1.247421,5.342536,7.976115,-4.895434,1.512493,-8.685672,9.589767,4.924950,-5.718481,-7.093616,-0.852561,-8.239923,4.786961,4.489389,-4.857451,2.560851,9.363825,8.760839,-2.281543,8.048618,7.822528,-3.397081,-8.070564,-0.101023,-3.929535,-3.761041,-2.662956,-1.716414,-1.487406,-8.188336,-9.278919,6.237037,7.676421,-7.100703,9.145052,3.979921,2.003873,2.932578,0.213562,7.517814,-7.347510,-4.273003,-9.178918,-1.187026,-8.928487,0.105168,8.470625,-7.704810,9.563910,-6.573196,-3.880313,2.855053,5.893508,0.374280,-7.217429,6.234089,-8.056344,0.989164,-4.187864,6.161849,7.455599,3.118728,-5.799988,8.668032,-0.869406,-9.774529,2.991722,4.452074,-0.017589,-3.228758,2.657840,-3.975132,6.428163,-8.242893,9.737730,6.609851,-6.087282,2.618060,-4.682123,-0.368468,-8.902563,-2.422269,-5.720127,0.239157,-9.572033,-2.603776,5.949366,-1.216708,-1.657227,-2.863354,-2.690658,-0.944838,2.810294,7.002531,-9.432906,-2.779098,-8.719014,9.221244,-3.479730,-1.408408,-1.407669,-4.624014,1.835825,-4.115803,1.529508,8.343892,-2.800287,-2.342121,-9.015436,-5.120361,3.936236,8.190340,9.103009,9.858984,8.137034,-5.908169,-5.054017,3.941953,2.052577,9.405340,4.721963,1.664845,6.418294,2.699154,5.023631,-7.228432,-4.396293,7.184458,-4.598521,-8.480604,-8.759449,3.301181,6.869582,-8.480954,7.888767,-1.389544,-3.785700,-2.663667,6.789103,7.672991,6.126419,-3.722046,-5.757926,4.622314,-3.341362,-0.739875,2.681484,1.235324,1.422387,6.779407,9.175125,0.360139,9.786560,5.237359,4.758420,-1.861108,9.839934,-2.612915,-1.198681,-4.719523,3.913413,6.289204,8.107036,-9.529177,-7.979117,2.768334,2.720533,0.005235,-8.229103,1.547598,-9.578762,5.348076,-7.524710,8.172208,2.639577,0.639061,-6.050079,6.291334,9.539543,-6.009849,-4.138216,-0.506066,-9.222267,-2.474073,-3.855475,-6.415196,8.093776,-1.875178,-1.555342,-2.053943,-1.186347,-5.570072,-0.470716,-4.524397,1.232730,6.327391,-8.365898,2.020990,-4.133054,2.247364,-4.761383,5.013556,9.955882,0.381155,2.119081,-5.302118,-4.115851,-9.222310,-7.840024,-3.905827,-1.174239,4.836815,7.505515,6.040586,7.351754,8.404334,2.757947,9.189228,-5.410479,-1.054910,8.241906,6.541686,1.666780,-4.135151,-4.300563,-3.445948,6.087376,1.043791,-9.617489,-4.201261,-9.429688,4.092875,-4.207557,-5.887257,-4.383205,-1.323166,1.908453,8.057033,3.489448,4.900075,-7.658208,-8.351802,5.261025,6.631357,0.900939,3.408409,6.630291,7.634655,-6.463451,-3.545431,-3.025085,-5.627588,2.855436,-6.911748,0.116305,-9.437339,9.848884,7.084777,0.447802,6.668942,-3.541825,-6.621764,3.811329,0.404882,2.697229,-7.693720,-7.366913,-1.690805,-2.384630,8.160634,-2.264570,-5.987144,-7.766416,-9.141660,-6.545882,-5.936558,5.569719,-9.442773,-8.520842,-0.865228,2.817064,7.473201,7.546763,7.107330,5.424939,3.789890,8.703886,7.105137,-5.803140,7.744393,2.515076,0.224428,-5.756177,-1.515735,-6.153982,-2.952702,7.954077,6.205548,1.220560,8.855541,1.816527,-8.724182,-0.189653,6.565604,-7.620539,8.259847,-3.479533,-9.096636,-6.742011,-5.124822,1.653376,-9.730509,-0.815095,4.523691,8.294140,-4.631781,8.007990,0.667518,0.180283,-7.023472,6.751804,5.500107,8.221293,-0.020812,-5.563001,-9.513059,8.429142,7.607926,-6.692716,-6.406352,9.098621,6.734715,5.916383,-7.017893,8.835201,-9.273564,-1.573999,-7.006832,9.140431,6.114157,4.370563,8.837264,-9.095571,4.600098,7.719408,-4.867837,-1.161652,-5.366963,-9.739143,-1.327863,2.425529,-8.502357,2.071955,0.389355,7.454295,-0.510957,-3.711622,-2.321994,-9.925303,-7.460685,5.478157,-1.517644,-7.602585,3.753601,0.510443,-8.451751,3.209439,-0.686479,5.472202,0.063973,-4.332333,-3.632500,-3.417219,-8.396526,-3.408301,-7.791424,6.896038,3.610818,8.751909,3.592458,6.409336,-9.726844,-2.211982,6.375271,-6.376186,4.428210,-9.140978,-9.267814,-1.950876,-3.854599,4.076827,-8.444816,9.234377,-5.285938,-6.477402,-0.542140,6.853780,-6.181596,9.258555,3.624688,9.542353,3.824913,-2.984674,-2.634299,-1.302715,1.061148,7.746877,-4.224356,-3.481103,-0.582791,-6.254515,-7.920013,2.241812,-1.058395,-0.775465,-9.366121,-6.850589,1.730530,5.492794,4.318658,-3.230582,1.282486,-8.236151,7.923704,-7.187302,3.304920,-3.798640,-3.249912,4.273265,-6.595219,5.270347,0.704019,-5.242816,-1.946666,-5.888055,2.089396,1.316449,-6.381371,7.830494,-2.266825,7.765764,-9.067035,7.039797,3.595153,3.677754,-9.079201,9.788977,-8.487219,-3.708886,2.738467,-0.029829,-4.115903,-5.174215,4.480117,-0.078992,3.439978,-3.982569,0.947047,2.312121,-5.521589,-6.737754,9.173529,-6.887339,-5.720412,-1.797237,7.349307,-4.362340,-8.310004,-5.350776,-8.040059,8.679021,0.758290,-8.121562,1.669420,9.298127,-2.081686,-9.017145,2.091848,-0.133034,-0.650497,-6.195923,6.949114,0.674819,9.932675,-2.513358,-3.647349,7.197256,1.711668,-9.225822,4.180091,-0.889727,2.670264,8.297856,9.455969,-0.446781,7.920482,5.917968,-9.831656,-8.704076,-5.549251,7.700417,1.474505,-4.546195,-3.062550,2.204324,3.902755,-3.751038,4.712279,4.908258,7.826995,-0.455199,-5.066461,4.352253,-9.301018,-7.164411,-1.459445,8.656005,4.178811,-0.005902,-5.024145,9.437913,3.289093,-5.487327,-5.061242,1.212262,-7.373475,-3.143598,4.782293,5.750719,3.699555,5.766593,6.232923,3.602572,-4.274274,3.062622,-0.759938,-2.651709,-1.574480,-6.543000,4.558820,-3.124831,5.076034,-8.189435,-7.597680,-5.784072,-0.507055,-0.192515,-0.410127,-6.988970,5.789216,2.029694,-4.354267,-9.117827,-3.331096,2.296108,-5.515524,7.148359,-3.568726,9.763653,6.534620,3.434719,0.401743,-7.499442,9.675129,-5.507778,-2.571675,-3.179132,-8.378692,8.187901,2.547263,-8.618256,-6.615257,2.255812,6.093838,5.381955,-1.378180,-8.222650,-7.317115,5.897706,2.079474,1.896762,2.993318,9.372297,-4.396694,2.705744,5.698578,0.585550,6.920240,4.512468,4.798331,-6.600647,9.250703,2.463687,0.799434,1.405364,2.873017,-7.717711,9.072710,-7.692621,-3.378650,6.073684,9.128277,4.973368,-2.217453,7.156754,0.620039,2.619826,0.767332,7.558086,-1.458096,9.716357,4.298610,-8.763351,8.871284,-3.304846,-8.742187,-1.780472,-6.645138,8.824213,-7.326437,0.049622,-8.791314,-3.051192,5.591664,-3.695813,-3.998001,9.550982,7.400416,-7.415360,-4.170282,-7.154936,9.989299,-2.183862,-2.783480,-1.418153,6.409770,-0.685289,-0.352300,7.083625,-2.901627,9.834496,9.799253,-7.621966,5.632617,-1.994591,7.566770,-6.300914,7.390004,4.778415,-1.268151,-4.342955,9.472113,8.743941,7.924881,4.519083,-4.233241,-1.553194,-1.555922,-0.184554,-3.381911,8.990895,4.553679,-8.709055,5.775581,-8.152640,8.379128,7.582624,-5.363982,-3.422266,9.660870,9.656811,0.257071,0.955700,8.698635,0.902609,-1.527370,2.112939,-4.864701,-7.514164,9.657721,-3.614138,0.710600,3.496996,-3.347715,8.746600,-8.745551,-8.715987,8.652697,3.772460,1.908051,-1.586071,5.396921,-9.683906,3.440942,6.755564,2.688327,4.090695,7.847909,-6.502875,-1.978035,1.195350,0.043808,-9.191671,-1.966963,6.997657,-3.842936,7.970511,6.483598,-3.864775,0.679183,-0.293226,5.420350,7.363907,-3.918003,-9.427375,-8.038118,8.320530,5.575463,-7.913865,6.466140,-6.163741,2.374256,-0.203552,4.300076,6.743251,-5.996117,0.987966,0.756131,8.732547,9.813864,-5.152751,3.777970,0.965918,-1.547906,-8.095450,2.561572,0.374232,7.748999,4.451477,-1.416432,0.810088,-6.703659,-8.522545,6.071039,-3.507862,-4.309982,-9.280250,-4.820836,-8.984978,6.944876,5.544794,0.258620,6.902966,-8.762893,6.161210,4.772490,4.523785,-3.445188], dtype = "float32")#candidate|20023|(2002,)|const|float32
call_20022 = func_14375_call(relay.reshape(const_20023.astype('float32'), [11, 13, 14]))
call_20024 = func_14375_call(relay.reshape(const_20023.astype('float32'), [11, 13, 14]))
output = relay.Tuple([call_19929,call_19948,const_19949,call_19961,var_19962,const_19963,call_19965,var_19966,call_20000,call_20011,call_20020,call_20022,const_20023,])
output2 = relay.Tuple([call_19930,call_19950,const_19949,call_19964,var_19962,const_19963,call_19967,var_19966,call_20001,call_20012,call_20021,call_20024,const_20023,])
func_20045 = relay.Function([var_19962,var_19966,], output)
mod['func_20045'] = func_20045
mod = relay.transform.InferType()(mod)
var_20046 = relay.var("var_20046", dtype = "int8", shape = (21, 4))#candidate|20046|(21, 4)|var|int8
var_20047 = relay.var("var_20047", dtype = "int16", shape = (160,))#candidate|20047|(160,)|var|int16
output = func_20045(var_20046,var_20047,)
func_20048 = relay.Function([var_20046,var_20047,], output)
mutated_mod['func_20048'] = func_20048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16452_call = mod.get_global_var('func_16452')
func_16454_call = mutated_mod.get_global_var('func_16454')
call_20055 = func_16452_call()
call_20056 = func_16452_call()
output = relay.Tuple([call_20055,])
output2 = relay.Tuple([call_20056,])
func_20064 = relay.Function([], output)
mod['func_20064'] = func_20064
mod = relay.transform.InferType()(mod)
mutated_mod['func_20064'] = func_20064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20064_call = mutated_mod.get_global_var('func_20064')
call_20065 = func_20064_call()
output = call_20065
func_20066 = relay.Function([], output)
mutated_mod['func_20066'] = func_20066
mutated_mod = relay.transform.InferType()(mutated_mod)
var_20123 = relay.var("var_20123", dtype = "float64", shape = (5, 6, 7))#candidate|20123|(5, 6, 7)|var|float64
var_20124 = relay.var("var_20124", dtype = "float64", shape = (5, 6, 7))#candidate|20124|(5, 6, 7)|var|float64
bop_20125 = relay.equal(var_20123.astype('bool'), relay.reshape(var_20124.astype('bool'), relay.shape_of(var_20123))) # shape=(5, 6, 7)
output = bop_20125
output2 = bop_20125
F = relay.Function([var_20123,var_20124,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_20123,var_20124,], output2)
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
