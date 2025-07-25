import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_337 = relay.var("var_337", dtype = "int32", shape = ())#candidate|337|()|var|int32
var_338 = relay.var("var_338", dtype = "int32", shape = (8, 5, 7))#candidate|338|(8, 5, 7)|var|int32
bop_339 = relay.less_equal(var_337.astype('bool'), var_338.astype('bool')) # shape=(8, 5, 7)
output = relay.Tuple([bop_339,])
output2 = relay.Tuple([bop_339,])
func_342 = relay.Function([var_337,var_338,], output)
mod['func_342'] = func_342
mod = relay.transform.InferType()(mod)
var_343 = relay.var("var_343", dtype = "int32", shape = ())#candidate|343|()|var|int32
var_344 = relay.var("var_344", dtype = "int32", shape = (8, 5, 7))#candidate|344|(8, 5, 7)|var|int32
output = func_342(var_343,var_344,)
func_345 = relay.Function([var_343,var_344,], output)
mutated_mod['func_345'] = func_345
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1194 = relay.var("var_1194", dtype = "bool", shape = (8, 13, 12))#candidate|1194|(8, 13, 12)|var|bool
const_1195 = relay.const([[[True,False,False,True,True,False,False,False,False,True,False,True],[False,True,True,True,True,False,True,False,True,False,True,True],[False,False,False,True,True,True,True,True,True,False,False,False],[False,False,False,False,True,False,False,True,True,True,False,True],[False,False,True,True,False,False,False,True,True,True,False,False],[False,True,True,True,True,True,True,True,True,True,False,False],[False,False,False,True,True,False,False,True,False,True,True,True],[False,True,False,True,False,False,True,False,True,True,True,True],[False,False,False,False,False,False,False,False,False,False,True,False],[True,False,True,True,True,False,False,True,False,False,False,False],[False,False,True,False,True,False,True,True,True,True,True,True],[False,False,True,False,False,False,False,True,False,False,True,False],[False,True,True,False,False,False,True,False,False,False,False,True]],[[False,True,False,True,True,False,False,True,False,True,True,False],[False,False,False,False,False,True,False,False,False,False,True,False],[False,False,True,False,False,True,True,False,True,True,False,False],[True,False,True,True,False,False,False,False,False,False,False,False],[True,True,True,True,True,False,False,True,False,True,True,False],[False,False,False,True,True,False,True,True,True,False,False,True],[True,False,True,True,False,True,False,True,False,True,True,True],[True,True,False,True,False,True,True,False,True,True,False,True],[False,True,False,True,False,False,False,True,True,True,False,True],[False,False,True,True,True,False,False,False,True,True,True,True],[False,False,True,False,False,True,True,False,True,True,True,True],[True,True,False,False,False,False,False,False,True,True,True,False],[True,False,True,False,True,False,True,True,True,False,True,True]],[[False,False,True,True,True,False,False,True,True,False,True,True],[False,True,True,True,False,True,False,True,True,True,True,False],[True,False,True,False,True,True,True,True,True,False,False,True],[False,False,False,True,False,True,False,False,True,False,False,True],[True,False,True,False,True,False,False,False,True,True,True,False],[False,False,True,False,True,True,True,True,True,True,True,True],[False,True,True,True,True,True,True,False,True,False,False,False],[False,False,True,True,False,False,True,False,False,False,False,True],[True,True,True,False,False,False,True,True,True,True,False,True],[False,True,True,False,True,False,False,False,False,True,True,False],[True,True,True,False,True,True,True,True,True,False,True,True],[False,True,False,False,False,True,True,False,False,False,False,False],[False,True,False,True,False,True,True,False,False,False,False,False]],[[False,True,True,True,False,False,False,False,True,True,False,True],[False,True,False,False,False,False,False,False,True,False,True,False],[False,True,False,False,True,False,False,True,True,True,False,True],[False,True,False,True,False,False,True,False,False,True,False,False],[True,True,False,True,True,False,True,True,True,True,False,False],[True,False,False,False,False,False,False,False,True,False,True,True],[False,False,True,False,True,False,False,True,True,True,False,False],[True,True,False,False,False,False,False,True,False,False,True,False],[True,True,False,False,True,False,False,False,False,True,False,False],[True,True,True,False,False,True,True,True,False,True,True,False],[True,True,True,True,False,False,False,True,False,False,True,True],[False,True,True,True,True,False,True,False,True,False,True,True],[True,False,False,True,True,True,True,False,False,False,True,False]],[[False,True,True,False,False,True,False,False,False,True,True,True],[True,False,False,False,False,True,True,True,True,True,False,False],[False,True,False,True,True,True,True,False,True,True,False,True],[False,False,True,False,False,True,False,True,True,False,False,False],[True,True,True,False,True,False,False,True,True,False,False,True],[True,False,True,False,True,True,True,True,False,True,True,False],[False,True,True,True,True,True,True,False,True,True,False,False],[True,False,True,False,False,False,True,False,False,False,False,True],[False,False,False,False,True,True,False,True,True,True,False,False],[True,False,True,False,True,True,False,False,False,True,False,False],[True,False,False,True,False,True,False,False,True,False,False,False],[False,False,True,True,False,True,True,True,True,False,True,False],[False,True,False,False,False,True,False,False,True,True,True,True]],[[False,False,False,True,False,False,True,False,True,False,True,True],[True,True,False,True,True,True,True,True,False,False,True,False],[True,False,False,False,True,False,True,True,False,True,False,False],[False,True,True,True,True,False,False,False,True,False,True,True],[True,True,False,True,True,False,True,False,False,False,False,True],[False,True,False,False,True,False,False,True,True,True,False,False],[False,False,False,True,False,False,False,True,True,True,False,False],[True,True,False,True,True,False,False,True,True,False,True,False],[False,False,True,True,True,True,True,True,True,True,True,True],[True,True,False,False,False,False,False,True,False,False,False,True],[False,False,True,False,False,False,False,False,False,False,True,False],[True,False,True,True,False,False,False,True,False,True,False,False],[True,False,False,True,True,False,True,True,True,False,True,True]],[[False,False,False,True,False,True,True,True,False,False,False,False],[True,True,True,True,False,True,True,True,False,True,True,True],[False,False,False,True,False,False,False,False,False,False,True,False],[False,False,True,False,True,False,False,False,True,True,True,True],[True,False,False,True,False,True,False,False,True,False,True,True],[False,True,False,False,False,True,False,False,False,False,False,True],[False,False,True,True,True,False,False,False,False,False,True,False],[False,True,False,True,False,True,True,False,True,True,True,True],[False,True,True,False,True,True,True,True,True,False,False,False],[False,False,True,True,True,False,True,True,False,False,False,False],[True,True,False,False,False,True,True,True,True,False,True,False],[True,True,False,False,True,False,True,False,True,False,True,False],[False,False,True,False,False,True,False,False,True,True,False,True]],[[False,False,False,True,False,False,False,False,True,False,False,False],[False,True,False,True,True,True,True,False,False,False,False,False],[False,True,False,True,False,True,False,False,True,True,False,True],[True,False,True,False,False,False,False,False,True,True,False,True],[False,True,True,False,False,True,True,False,False,True,True,False],[False,True,True,True,False,True,True,True,True,False,True,True],[False,False,True,False,True,True,True,True,True,False,False,True],[True,True,True,False,False,False,False,True,True,True,False,False],[False,True,True,True,False,True,False,False,True,False,False,False],[True,True,True,False,True,True,True,True,False,False,True,True],[False,True,False,False,True,False,False,True,False,True,True,False],[False,True,False,True,True,True,True,True,False,True,True,False],[False,True,True,True,True,False,False,False,True,False,False,False]]], dtype = "bool")#candidate|1195|(8, 13, 12)|const|bool
bop_1196 = relay.logical_and(var_1194.astype('bool'), relay.reshape(const_1195.astype('bool'), relay.shape_of(var_1194))) # shape=(8, 13, 12)
output = bop_1196
output2 = bop_1196
func_1202 = relay.Function([var_1194,], output)
mod['func_1202'] = func_1202
mod = relay.transform.InferType()(mod)
var_1203 = relay.var("var_1203", dtype = "bool", shape = (8, 13, 12))#candidate|1203|(8, 13, 12)|var|bool
output = func_1202(var_1203)
func_1204 = relay.Function([var_1203], output)
mutated_mod['func_1204'] = func_1204
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1464 = relay.var("var_1464", dtype = "float64", shape = (1, 8, 12))#candidate|1464|(1, 8, 12)|var|float64
uop_1465 = relay.sigmoid(var_1464.astype('float64')) # shape=(1, 8, 12)
func_1202_call = mod.get_global_var('func_1202')
func_1204_call = mutated_mod.get_global_var('func_1204')
var_1476 = relay.var("var_1476", dtype = "bool", shape = (1248,))#candidate|1476|(1248,)|var|bool
call_1475 = func_1202_call(relay.reshape(var_1476.astype('bool'), [8, 13, 12]))
call_1477 = func_1202_call(relay.reshape(var_1476.astype('bool'), [8, 13, 12]))
func_1202_call = mod.get_global_var('func_1202')
func_1204_call = mutated_mod.get_global_var('func_1204')
call_1479 = func_1202_call(relay.reshape(call_1475.astype('bool'), [8, 13, 12]))
call_1480 = func_1202_call(relay.reshape(call_1475.astype('bool'), [8, 13, 12]))
func_342_call = mod.get_global_var('func_342')
func_345_call = mutated_mod.get_global_var('func_345')
var_1491 = relay.var("var_1491", dtype = "int32", shape = ())#candidate|1491|()|var|int32
const_1492 = relay.const([2,10,-7,-4,-3,6,9,10,-3,-8,-4,7,-6,-9,9,1,-7,-7,3,3,4,7,-3,9,6,2,6,7,-8,4,-8,9,7,10,-9,8,-10,-9,4,1,-3,-9,-2,-10,-1,-8,-9,-6,2,8,9,-7,3,-6,-3,-8,-9,7,1,4,2,-5,-6,9,7,3,5,6,5,-6,8,5,1,3,-7,-6,-6,2,-1,3,-10,5,6,5,5,8,-7,3,4,2,2,2,8,-9,7,-1,8,-4,9,-4,3,10,-6,10,10,5,9,-9,3,9,9,7,-8,-2,10,-3,-9,-5,-7,-8,8,-8,-3,5,6,6,-6,5,-5,10,2,-10,-6,7,-1,-2,-8,-7,9,7,-8,1,7,7,-10,7,2,-2,-2,6,5,4,10,2,-5,-5,3,8,-9,-2,-6,2,4,-8,6,-4,10,2,-1,-9,7,-1,9,10,8,10,9,-2,7,-3,-2,4,5,3,-4,4,8,10,9,-5,2,-3,-7,-5,-4,9,-5,1,-9,-8,9,-2,1,2,4,9,5,6,-4,6,7,-6,-8,-4,3,2,6,-7,-8,7,10,-7,-7,-5,-3,-10,8,-3,-5,5,-1,-8,-3,-3,7,2,-7,10,-3,4,-8,6,-10,-4,8,-1,-8,-3,5,1,-8,-7,3,9,-4,2,5,10,7,-10,-5,3,1,4,3,-8,-8,8,-4,-9,-7,-10,7,10,6,-10,-1,4,-8,-10], dtype = "int32")#candidate|1492|(280,)|const|int32
call_1490 = relay.TupleGetItem(func_342_call(relay.reshape(var_1491.astype('int32'), []), relay.reshape(const_1492.astype('int32'), [8, 5, 7]), ), 0)
call_1493 = relay.TupleGetItem(func_345_call(relay.reshape(var_1491.astype('int32'), []), relay.reshape(const_1492.astype('int32'), [8, 5, 7]), ), 0)
output = relay.Tuple([uop_1465,call_1475,var_1476,call_1479,call_1490,var_1491,const_1492,])
output2 = relay.Tuple([uop_1465,call_1477,var_1476,call_1480,call_1493,var_1491,const_1492,])
func_1505 = relay.Function([var_1464,var_1476,var_1491,], output)
mod['func_1505'] = func_1505
mod = relay.transform.InferType()(mod)
mutated_mod['func_1505'] = func_1505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1505_call = mutated_mod.get_global_var('func_1505')
var_1507 = relay.var("var_1507", dtype = "float64", shape = (1, 8, 12))#candidate|1507|(1, 8, 12)|var|float64
var_1508 = relay.var("var_1508", dtype = "bool", shape = (1248,))#candidate|1508|(1248,)|var|bool
var_1509 = relay.var("var_1509", dtype = "int32", shape = ())#candidate|1509|()|var|int32
call_1506 = func_1505_call(var_1507,var_1508,var_1509,)
output = call_1506
func_1510 = relay.Function([var_1507,var_1508,var_1509,], output)
mutated_mod['func_1510'] = func_1510
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1715 = relay.var("var_1715", dtype = "float32", shape = (4, 8, 9))#candidate|1715|(4, 8, 9)|var|float32
uop_1716 = relay.acosh(var_1715.astype('float32')) # shape=(4, 8, 9)
func_1202_call = mod.get_global_var('func_1202')
func_1204_call = mutated_mod.get_global_var('func_1204')
const_1722 = relay.const([False,True,True,False,True,True,False,True,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,True,True,True,True,True,True,False,False,True,True,True,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,True,False,False,False,True,True,True,False,True,True,False,True,True,True,False,False,True,True,False,False,False,False,True,False,False,True,False,False,True,True,False,False,True,False,False,False,False,False,True,True,True,True,False,False,False,False,False,True,True,False,False,False,False,True,False,False,False,False,True,True,True,True,True,True,False,False,True,False,False,False,True,True,True,True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,True,True,True,True,True,True,False,True,True,True,True,True,False,False,False,True,True,True,True,False,False,True,True,True,False,False,True,True,True,False,True,True,True,True,False,False,False,False,True,True,True,False,False,True,False,False,True,True,True,False,False,True,True,True,False,False,False,False,True,True,False,False,False,True,True,False,False,True,False,True,False,False,False,False,True,False,False,False,False,True,True,False,False,False,True,True,False,True,True,True,True,True,False,True,False,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,False,True,False,False,False,True,False,False,False,True,False,False,False,False,False,False,True,False,False,True,True,False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False,True,False,False,True,False,True,True,False,True,True,True,False,True,False,True,False,False,False,False,True,False,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,False,False,False,False,False,False,False,True,False,False,False,False,True,False,False,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True,True,True,False,True,True,False,True,False,False,True,False,False,False,False,False,False,True,True,False,False,False,True,False,True,True,True,False,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,False,False,True,False,False,False,False,False,True,False,True,True,False,True,False,False,True,True,False,False,True,True,False,True,True,False,False,False,False,False,True,False,True,False,False,True,False,False,False,True,True,True,True,True,False,True,True,True,True,True,False,False,False,False,True,False,False,True,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,True,False,True,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,True,False,True,False,False,True,False,True,False,True,True,False,True,False,False,False,True,False,True,True,False,False,True,False,False,False,False,False,False,False,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,True,True,True,False,False,False,False,False,False,True,False,False,True,True,False,False,True,False,False,True,True,True,False,True,False,True,True,False,False,True,False,True,False,False,True,False,False,False,False,False,True,True,False,False,False,True,False,True,True,True,False,False,False,False,False,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,True,False,False,True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,False,True,False,True,False,True,False,True,False,False,True,False,False,False,True,False,True,False,False,False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,True,True,False,True,False,False,False,True,False,False,False,True,False,True,False,False,True,False,True,True,False,True,False,True,True,True,True,True,True,True,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,False,True,False,False,True,True,False,False,False,False,True,True,True,False,False,False,True,False,True,False,True,False,False,False,False,True,False,True,False,True,False,False,True,True,False,False,False,True,False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,True,False,False,True,True,False,False,True,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False,False,True,True,True,False,True,True,True,False,True,True,True,False,True,False,True,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,True,False,True,True,False,False,False,True,True,True,False,False,True,True,False,False,False,False,False,False,True,True,False,True,False,False,False,False,False,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,True,True,True,True,False,False,False,False,True,False,False,False,False,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,False,True,True,True,False,False,False,False,False,True,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,True,True,False,False,True,False,True,False,False,True,False,False,True,False,True,False,False,False,True,False,True,False,True,True,True,True,True,False,True,True,False,False,False,False,False,True,True,True,False,True,False,False,True,True,True,True,True,True,True,False,True,True,True,False,False,False,False,True,False,True,False,False,True,False,False,True,False,True,False,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,False,True,False,False,True,False,True,True,False,False,False,True,True,False,False,True,False,True,True,False,True,False,False,False,True,False,False,True,False,False,True,False,True,False,False,False,False,True,False,True,True,False,False,False,False,False,True,False,True,False,False,False,False,False,False,False,True,True,True,True,True,False,True,False,False,True,True,True,False,True,False,True,True,False,True,True,False,False,True,False,False,True,False,False,False,True,False,True,False,True,False,True,False,True,True,False,False,False,True,False,True,True,True,False,True,False,True,False,False,False,False,False,False,False,False,False,True,True,True,True,False,True,False,False,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,True,False,True,True,False,False,True,False,True,False,True,True,True,False,True,True,False,True,False,False,False,True,False,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,False,True,True,False,True,True,True,True,False,True,True,True,True,True,False,True,False,False,True,True,True,True,False,True,True,False,False], dtype = "bool")#candidate|1722|(1248,)|const|bool
call_1721 = func_1202_call(relay.reshape(const_1722.astype('bool'), [8, 13, 12]))
call_1723 = func_1202_call(relay.reshape(const_1722.astype('bool'), [8, 13, 12]))
output = relay.Tuple([uop_1716,call_1721,const_1722,])
output2 = relay.Tuple([uop_1716,call_1723,const_1722,])
func_1733 = relay.Function([var_1715,], output)
mod['func_1733'] = func_1733
mod = relay.transform.InferType()(mod)
mutated_mod['func_1733'] = func_1733
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1734 = relay.var("var_1734", dtype = "float32", shape = (4, 8, 9))#candidate|1734|(4, 8, 9)|var|float32
func_1733_call = mutated_mod.get_global_var('func_1733')
call_1735 = func_1733_call(var_1734)
output = call_1735
func_1736 = relay.Function([var_1734], output)
mutated_mod['func_1736'] = func_1736
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1946 = relay.var("var_1946", dtype = "uint8", shape = (14, 12, 9))#candidate|1946|(14, 12, 9)|var|uint8
var_1947 = relay.var("var_1947", dtype = "uint8", shape = (14, 12, 9))#candidate|1947|(14, 12, 9)|var|uint8
bop_1948 = relay.greater_equal(var_1946.astype('bool'), relay.reshape(var_1947.astype('bool'), relay.shape_of(var_1946))) # shape=(14, 12, 9)
func_1202_call = mod.get_global_var('func_1202')
func_1204_call = mutated_mod.get_global_var('func_1204')
const_1960 = relay.const([True,True,True,False,True,False,True,False,True,True,True,False,True,True,True,True,False,True,True,False,True,True,False,True,True,True,False,False,False,False,False,True,True,True,True,False,True,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,True,True,False,False,False,False,False,False,False,False,True,False,True,False,False,True,True,True,False,False,True,True,True,False,True,False,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,True,True,True,False,False,True,False,False,False,True,False,True,False,False,False,True,True,True,False,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,True,True,True,True,False,True,True,False,False,False,True,False,False,True,False,False,True,True,True,True,False,True,False,True,False,True,True,False,False,True,False,True,False,True,False,False,False,False,False,False,False,True,False,True,True,True,True,False,False,False,True,False,False,True,True,False,False,False,False,False,False,False,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,True,True,True,True,False,False,False,True,False,True,False,True,True,False,False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,False,True,True,True,True,False,False,False,False,False,True,True,True,True,False,True,True,False,False,False,False,False,False,True,False,True,False,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,False,False,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,True,True,True,False,True,False,True,True,False,False,True,False,True,False,False,False,False,False,False,True,True,True,False,True,True,False,False,False,False,True,False,True,False,False,False,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,True,False,False,False,True,False,False,True,False,True,False,True,True,False,True,False,False,True,True,True,False,True,False,True,True,True,False,True,True,False,True,False,False,True,True,False,True,True,True,True,True,True,False,False,True,False,True,False,True,False,True,True,True,True,True,False,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,False,False,True,False,True,True,False,True,False,False,True,False,False,True,False,False,False,False,False,False,True,False,False,True,False,False,False,True,True,True,True,False,False,True,False,True,False,False,False,False,True,True,True,True,False,True,True,False,True,True,False,False,True,True,False,True,True,False,False,False,True,False,False,True,True,True,False,True,True,False,True,False,False,False,True,False,False,True,True,True,False,True,False,False,False,False,True,True,False,False,False,True,False,False,True,True,True,True,False,True,False,True,True,False,False,True,False,False,False,True,True,False,True,True,False,True,True,False,True,True,False,True,True,False,True,False,True,True,True,True,False,True,False,True,True,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True,False,True,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,False,False,True,True,True,True,False,False,False,True,False,True,True,True,False,False,True,True,False,False,True,False,True,False,False,True,False,False,True,False,False,False,False,True,True,False,False,True,False,True,False,False,False,True,True,False,False,False,False,False,False,True,False,True,True,False,True,True,False,False,False,True,False,False,False,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,True,True,True,True,False,False,False,True,False,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,True,True,False,False,True,True,True,True,False,True,False,True,False,True,False,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,False,True,True,True,True,False,True,False,False,True,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,True,True,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,True,True,False,False,True,False,False,True,False,True,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,True,True,False,True,False,True,True,False,True,False,False,False,False,False,True,True,True,True,True,False,True,True,False,False,False,True,False,False,True,False,True,False,False,True,True,False,False,False,False,False,True,False,False,True,True,True,False,False,True,True,False,False,True,True,False,True,False,False,True,True,False,True,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,True,False,True,False,True,True,True,False,True,False,False,True,False,True,False,True,False,False,True,False,True,False,True,True,True,True,False,False,False,False,True,True,True,False,False,False,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,True,False,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,False,False,False,False,True,True,True,True,False,False,True,False,False,True,True,False,False,True,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,True,False,False,False,True,False,False,True,False,True,False,True,True,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,True,True,True,False,True,False,False,False,False,True,True,False,True,True,True,False,False,False,False,True,True,False,True,True,False,True,False,False,True,True,True,False,False,True,True,True,True,True,False,True,False,True,False,False,False,True,False,False,False,False,False,True,False,True,True,False,False,True,True,True,True,False,True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,True,True,False,False,True,True,True,True,False,False,False,True], dtype = "bool")#candidate|1960|(1248,)|const|bool
call_1959 = func_1202_call(relay.reshape(const_1960.astype('bool'), [8, 13, 12]))
call_1961 = func_1202_call(relay.reshape(const_1960.astype('bool'), [8, 13, 12]))
output = relay.Tuple([bop_1948,call_1959,const_1960,])
output2 = relay.Tuple([bop_1948,call_1961,const_1960,])
func_1962 = relay.Function([var_1946,var_1947,], output)
mod['func_1962'] = func_1962
mod = relay.transform.InferType()(mod)
mutated_mod['func_1962'] = func_1962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1962_call = mutated_mod.get_global_var('func_1962')
var_1964 = relay.var("var_1964", dtype = "uint8", shape = (14, 12, 9))#candidate|1964|(14, 12, 9)|var|uint8
var_1965 = relay.var("var_1965", dtype = "uint8", shape = (14, 12, 9))#candidate|1965|(14, 12, 9)|var|uint8
call_1963 = func_1962_call(var_1964,var_1965,)
output = call_1963
func_1966 = relay.Function([var_1964,var_1965,], output)
mutated_mod['func_1966'] = func_1966
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2012 = relay.var("var_2012", dtype = "float32", shape = (1, 12, 14))#candidate|2012|(1, 12, 14)|var|float32
uop_2013 = relay.acos(var_2012.astype('float32')) # shape=(1, 12, 14)
bop_2033 = relay.greater_equal(uop_2013.astype('bool'), relay.reshape(var_2012.astype('bool'), relay.shape_of(uop_2013))) # shape=(1, 12, 14)
bop_2037 = relay.right_shift(bop_2033.astype('uint32'), relay.reshape(var_2012.astype('uint32'), relay.shape_of(bop_2033))) # shape=(1, 12, 14)
output = relay.Tuple([bop_2037,])
output2 = relay.Tuple([bop_2037,])
func_2044 = relay.Function([var_2012,], output)
mod['func_2044'] = func_2044
mod = relay.transform.InferType()(mod)
var_2045 = relay.var("var_2045", dtype = "float32", shape = (1, 12, 14))#candidate|2045|(1, 12, 14)|var|float32
output = func_2044(var_2045)
func_2046 = relay.Function([var_2045], output)
mutated_mod['func_2046'] = func_2046
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2201 = relay.var("var_2201", dtype = "float32", shape = ())#candidate|2201|()|var|float32
var_2202 = relay.var("var_2202", dtype = "float32", shape = (13, 16, 15))#candidate|2202|(13, 16, 15)|var|float32
bop_2203 = relay.power(var_2201.astype('float32'), var_2202.astype('float32')) # shape=(13, 16, 15)
output = relay.Tuple([bop_2203,])
output2 = relay.Tuple([bop_2203,])
func_2216 = relay.Function([var_2201,var_2202,], output)
mod['func_2216'] = func_2216
mod = relay.transform.InferType()(mod)
var_2217 = relay.var("var_2217", dtype = "float32", shape = ())#candidate|2217|()|var|float32
var_2218 = relay.var("var_2218", dtype = "float32", shape = (13, 16, 15))#candidate|2218|(13, 16, 15)|var|float32
output = func_2216(var_2217,var_2218,)
func_2219 = relay.Function([var_2217,var_2218,], output)
mutated_mod['func_2219'] = func_2219
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2332 = relay.var("var_2332", dtype = "uint32", shape = ())#candidate|2332|()|var|uint32
var_2333 = relay.var("var_2333", dtype = "uint32", shape = (1, 1, 15))#candidate|2333|(1, 1, 15)|var|uint32
bop_2334 = relay.add(var_2332.astype('uint32'), var_2333.astype('uint32')) # shape=(1, 1, 15)
output = bop_2334
output2 = bop_2334
func_2337 = relay.Function([var_2332,var_2333,], output)
mod['func_2337'] = func_2337
mod = relay.transform.InferType()(mod)
var_2338 = relay.var("var_2338", dtype = "uint32", shape = ())#candidate|2338|()|var|uint32
var_2339 = relay.var("var_2339", dtype = "uint32", shape = (1, 1, 15))#candidate|2339|(1, 1, 15)|var|uint32
output = func_2337(var_2338,var_2339,)
func_2340 = relay.Function([var_2338,var_2339,], output)
mutated_mod['func_2340'] = func_2340
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2389 = relay.const([[[4.019655,-1.438659,1.564680,1.693561,3.233138,-3.311236,-3.470405],[-7.214082,8.567732,6.387925,4.892661,-7.089592,3.522061,2.129118],[-7.856110,7.415079,6.289459,3.811923,-4.045400,-2.529574,3.635519],[6.499475,4.291489,-0.893521,-4.680077,8.042568,-4.882971,-5.773629]],[[-1.838194,-2.668742,-5.812350,-6.766049,6.554608,-3.963529,-7.508225],[9.911671,5.249547,-4.707645,-8.958968,3.756871,-4.440065,-2.450364],[-4.272050,-2.462991,-9.478989,7.921382,-6.476194,7.073223,-4.929832],[7.386953,-4.258207,-2.631207,9.762530,-2.326437,8.349703,-5.168857]],[[2.666916,-8.756206,3.442329,-5.777822,8.933400,-0.817978,-7.706327],[6.774638,5.334154,5.251645,3.834034,9.231796,-8.618879,-1.251783],[-2.770859,0.109833,-6.580693,1.081893,-8.662619,6.553688,-2.484392],[2.716725,5.132712,1.667412,9.970623,-6.875284,-3.176388,4.099868]],[[-6.807851,-5.714424,9.514191,-8.774797,-8.370366,3.523667,4.437374],[-6.981486,2.797361,-8.191012,6.756893,8.489547,6.201540,7.766059],[-8.264511,-6.740395,4.978671,1.195698,6.696251,-3.199831,4.333761],[-8.622266,-4.721925,-2.925928,7.664942,8.292844,-0.123294,4.549775]],[[-3.908688,5.546913,-7.743839,8.111319,0.175769,-4.575101,-5.615005],[-8.380415,-0.608257,8.845614,3.404058,-4.508027,-5.883947,3.376309],[4.266914,-1.275589,-1.683031,-0.315717,-5.896346,-9.101683,-8.481994],[-1.445936,5.886041,-2.349111,8.780218,-0.595477,-3.316153,5.033660]],[[-5.289492,0.861495,-8.122321,-6.590907,-3.959074,7.084837,-1.993101],[-1.267346,-2.249924,-2.000595,8.924462,2.727640,-4.568436,9.787523],[1.226883,5.445897,-3.354193,3.066559,1.925542,9.259227,-2.685511],[-6.895278,-4.980628,4.089411,0.122315,-5.412275,-0.950745,9.969541]],[[3.689708,1.182697,-7.443683,9.764397,-9.235800,3.692707,-0.964932],[3.282630,1.595309,0.323114,-4.799353,-9.472744,-5.246671,-9.092197],[-0.508833,1.682866,-9.629539,-5.227480,-0.156703,5.586233,-4.113799],[-8.138236,1.161130,5.768785,4.252207,-4.819796,7.495043,7.042987]],[[3.314850,1.343198,0.261371,-4.884115,4.448646,-4.017130,-0.186671],[-5.125017,-4.989017,3.940102,-6.543242,-9.653750,9.691199,8.784096],[8.884521,1.329194,-0.786825,3.783316,9.828135,-4.622252,-7.927724],[-9.425796,-8.525572,-2.562360,7.555337,3.004434,-3.323220,3.210753]],[[-7.168443,0.243441,1.775368,1.318121,5.951256,-6.245978,-9.767141],[1.206860,3.265609,1.639857,8.691936,5.622410,9.143726,-5.021184],[-5.155351,8.053590,7.906579,2.560242,1.248575,-4.367166,3.738633],[-0.212349,1.206776,-3.785242,3.740135,0.380467,3.045303,-8.181409]],[[5.834990,7.361544,-4.396026,-5.368982,8.602124,6.960203,-3.572911],[7.709523,-9.814198,1.966252,0.692815,-4.680019,7.038265,2.404067],[-5.450462,6.650613,0.412659,-6.901972,-0.373465,5.275198,-2.268197],[-9.966163,-0.667648,-4.460043,9.541195,9.054831,9.598770,-7.791474]],[[1.015029,-4.113751,2.637215,2.009404,-9.438527,-4.387580,-5.909190],[-7.469222,-6.986115,-9.355802,-0.922963,7.294215,-8.358615,-3.656430],[7.208114,0.717735,2.558100,-7.667410,1.325449,1.117053,1.954850],[-0.589115,5.660733,-1.643713,-0.214350,-1.132480,6.792277,-6.838686]],[[-4.494823,-5.001932,0.031802,-1.986775,8.688055,7.452318,-1.392667],[-1.799835,5.875007,-4.866812,7.235209,-8.709504,5.230208,-7.650667],[6.150490,-8.018673,5.325390,7.388258,-5.831099,1.171416,-7.406228],[5.786516,4.471325,1.566978,-5.567465,0.021704,-3.463938,8.479487]],[[7.811338,6.592697,2.909675,-6.239235,-3.564343,8.029676,-2.453053],[-9.141350,-3.665810,2.546530,3.581529,-4.135162,-4.686131,2.306062],[1.865286,-5.908330,-8.198550,2.288845,-0.529355,-4.562672,8.134624],[6.742236,0.919674,9.742979,0.869992,5.450700,1.802544,9.657669]],[[-8.948931,-3.843598,5.680829,-5.087049,-4.533636,1.075356,6.832999],[9.599648,-1.096496,-7.166788,-9.411258,3.254833,0.529420,-5.932416],[-1.307597,-3.706483,-0.606600,-8.064609,-1.651101,9.706274,1.178273],[3.099580,5.610581,7.125051,7.112735,2.676355,0.314443,-0.472855]],[[6.356373,7.939570,-8.775562,-7.887909,8.777026,-3.651415,7.454955],[-9.239663,5.044261,-3.824231,2.286903,-6.447283,3.522877,-3.174064],[-6.246302,3.823897,-5.242038,2.744877,5.513257,1.194658,-8.570040],[-6.907067,-1.866912,-5.301577,-6.572332,-7.112967,4.493642,-1.314587]],[[-0.297943,4.982416,8.531718,-6.661866,-9.545399,-7.041018,-9.431246],[-4.552360,-3.716688,-4.518550,5.653055,-3.956891,7.369021,0.001604],[8.880353,-9.833952,3.549507,-2.339981,-7.977211,-7.630156,-1.962962],[-4.639223,-5.688447,3.079644,3.400515,5.788580,2.780978,-8.841732]]], dtype = "float64")#candidate|2389|(16, 4, 7)|const|float64
uop_2390 = relay.sqrt(const_2389.astype('float64')) # shape=(16, 4, 7)
func_1505_call = mod.get_global_var('func_1505')
func_1510_call = mutated_mod.get_global_var('func_1510')
var_2394 = relay.var("var_2394", dtype = "float64", shape = (96, 1))#candidate|2394|(96, 1)|var|float64
const_2395 = relay.const([True,True,True,True,True,False,True,False,True,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,True,False,True,False,False,False,True,True,True,False,False,True,False,False,False,False,True,True,False,True,True,True,False,False,True,False,False,True,False,True,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,False,True,False,True,False,True,False,False,False,False,False,True,False,False,True,True,False,True,True,False,False,True,False,True,False,True,False,True,False,False,True,False,False,True,False,False,False,False,True,False,False,True,True,False,True,True,True,True,False,False,False,False,False,False,True,False,True,False,False,True,False,True,False,False,False,False,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,False,False,True,False,False,True,False,False,True,False,True,True,True,True,False,True,False,True,True,True,True,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,False,True,True,True,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True,False,False,False,False,True,True,False,True,False,True,False,True,True,False,True,True,True,True,False,False,True,True,True,True,True,True,False,False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,True,False,False,False,True,True,True,True,False,True,False,True,False,True,False,True,False,True,False,False,False,True,False,False,True,False,False,True,True,True,True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,True,False,True,False,False,True,True,True,True,True,True,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,True,True,False,True,False,True,True,False,True,False,True,True,False,False,False,True,False,False,True,False,True,True,False,True,False,True,False,True,True,True,True,False,False,True,False,True,True,True,True,False,True,False,True,True,True,True,False,True,True,True,True,False,False,True,True,True,False,False,False,True,True,True,False,True,False,False,False,True,True,True,True,False,False,False,True,True,False,True,False,True,False,True,False,False,False,True,True,False,True,True,True,False,False,True,False,True,True,False,False,False,False,False,False,False,False,True,True,False,False,True,False,False,False,False,True,False,True,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,False,True,False,False,True,True,True,True,False,True,False,False,True,True,False,False,True,False,True,True,True,True,False,False,False,True,True,False,True,False,False,True,True,False,False,False,True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,True,False,False,True,False,True,False,True,True,False,True,False,False,False,False,False,True,True,False,True,True,False,False,False,True,False,False,False,True,True,False,False,True,False,False,True,True,False,False,False,True,False,True,True,False,True,True,True,True,False,False,False,False,True,True,False,True,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,True,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,False,True,True,True,False,True,False,False,False,True,False,True,False,False,False,False,True,False,True,True,True,False,True,True,True,False,False,False,True,True,True,False,False,True,True,False,False,False,True,False,True,True,True,True,True,True,True,False,True,False,True,True,False,False,False,True,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,True,True,True,False,True,False,False,False,False,True,True,False,True,True,False,True,False,False,False,False,True,False,False,False,True,True,False,False,True,True,False,False,False,True,False,True,True,False,False,True,True,True,True,False,True,True,True,True,True,False,True,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,False,True,False,False,False,True,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,True,False,True,False,False,False,True,True,False,False,False,True,False,False,True,False,False,True,False,True,False,True,True,False,True,False,False,False,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,False,True,False,False,True,True,False,True,True,False,False,False,True,True,False,True,False,False,False,False,True,True,True,False,False,False,False,True,False,True,False,True,False,True,True,True,False,False,False,False,False,True,False,True,False,False,False,False,False,True,False,True,False,True,True,False,False,False,True,False,True,False,True,True,True,True,False,True,True,True,True,True,False,True,False,False,True,False,False,False,True,False,True,True,False,True,True,False,True,True,False,False,True,False,True,False,True,True,True,False,False,True,True,False,False,True,False,False,True,False,False,True,True,True,False,True,False,False,True,True,True,True,True,False,True,False,False,False,False,True,False,False,False,True,True,True,False,True,True,False,False,True,True,True,False,True,False,True,True,True,False,False,False,False,False,False,False,False,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,False,False,False,True,False,True,True,True,False,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,True,False,False,False,True,True,False,True,False,False,False,False,True,False,False,False,True,True,False,False,True,False,True,False,False,False,True,True,True,True,True,False,True,False,False,False,True,False,False,True,False,False,False,False,False,False,False,True,True,False,True,False,False,False,False,False,True,True,False,False,True,True,True,False,True,True,True,True,False,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,True,False,True,False,True,True,True,True,False,True,False,False,True,False,True,False,False,True,True,False,False,True,False,True,True,False,False,False,True,False,False,True,False,False,True,True,True,True,True,True,False,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,False,False,False,False,True,False,False,False,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,False,True,True,False,True,False,True,False,False,True,False,True,False,True,True,False,True,True,False,False], dtype = "bool")#candidate|2395|(1248,)|const|bool
var_2396 = relay.var("var_2396", dtype = "int32", shape = ())#candidate|2396|()|var|int32
call_2393 = relay.TupleGetItem(func_1505_call(relay.reshape(var_2394.astype('float64'), [1, 8, 12]), relay.reshape(const_2395.astype('bool'), [1248,]), relay.reshape(var_2396.astype('int32'), []), ), 6)
call_2397 = relay.TupleGetItem(func_1510_call(relay.reshape(var_2394.astype('float64'), [1, 8, 12]), relay.reshape(const_2395.astype('bool'), [1248,]), relay.reshape(var_2396.astype('int32'), []), ), 6)
output = relay.Tuple([uop_2390,call_2393,var_2394,const_2395,var_2396,])
output2 = relay.Tuple([uop_2390,call_2397,var_2394,const_2395,var_2396,])
func_2401 = relay.Function([var_2394,var_2396,], output)
mod['func_2401'] = func_2401
mod = relay.transform.InferType()(mod)
var_2402 = relay.var("var_2402", dtype = "float64", shape = (96, 1))#candidate|2402|(96, 1)|var|float64
var_2403 = relay.var("var_2403", dtype = "int32", shape = ())#candidate|2403|()|var|int32
output = func_2401(var_2402,var_2403,)
func_2404 = relay.Function([var_2402,var_2403,], output)
mutated_mod['func_2404'] = func_2404
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2580 = relay.var("var_2580", dtype = "float32", shape = (1, 11, 4))#candidate|2580|(1, 11, 4)|var|float32
uop_2581 = relay.sqrt(var_2580.astype('float32')) # shape=(1, 11, 4)
func_1202_call = mod.get_global_var('func_1202')
func_1204_call = mutated_mod.get_global_var('func_1204')
const_2590 = relay.const([[False,True,True,True,False,True,True,False,True,False,False,False],[False,True,True,False,False,True,True,False,True,True,False,True],[True,False,True,False,True,False,False,True,True,False,False,False],[True,True,False,False,False,False,False,False,False,True,False,False],[True,True,False,False,False,False,True,False,False,False,False,True],[True,False,True,False,False,True,False,True,True,False,False,True],[True,False,True,True,False,True,True,True,False,True,True,False],[True,False,False,True,False,False,True,True,True,False,False,True],[True,False,True,False,True,True,True,False,True,False,True,True],[True,False,False,True,True,True,False,False,True,False,True,False],[True,False,True,False,False,True,True,False,False,False,False,True],[True,False,True,True,False,False,False,False,False,True,True,True],[False,True,True,False,False,False,False,True,True,True,True,True],[True,False,True,True,True,False,False,False,False,True,True,False],[True,False,False,True,True,False,False,True,True,True,True,True],[True,True,False,False,True,True,False,False,False,True,True,True],[True,True,True,True,False,True,False,True,True,False,False,False],[False,False,True,False,True,True,True,False,False,False,True,True],[True,True,True,True,False,False,False,False,True,False,True,True],[True,True,False,False,False,False,False,False,False,True,False,True],[False,False,False,True,False,True,False,True,False,False,True,False],[False,True,False,False,True,False,True,False,True,False,False,True],[False,False,False,True,False,False,False,False,False,False,True,False],[True,False,False,True,False,True,False,False,False,False,False,False],[False,False,False,False,False,True,True,False,True,True,True,True],[False,False,False,False,False,True,True,False,True,True,True,True],[False,True,False,False,False,False,False,False,False,True,False,False],[False,False,True,True,True,False,True,True,False,True,False,True],[False,True,True,False,False,False,True,False,False,True,False,False],[False,True,False,False,False,True,True,False,True,False,True,False],[False,False,False,True,True,False,False,False,True,True,False,True],[True,True,True,True,True,True,True,True,False,False,True,False],[True,False,False,False,False,False,False,True,False,False,False,False],[False,False,False,True,True,False,False,False,True,True,False,False],[True,True,True,True,True,True,False,False,True,False,False,False],[False,True,True,True,True,True,True,False,True,True,True,False],[True,False,False,False,True,False,True,False,False,False,False,True],[True,False,False,True,False,False,True,True,True,False,False,True],[True,True,True,False,False,False,False,True,False,False,True,False],[True,False,False,True,True,False,False,False,False,False,True,True],[True,False,False,False,False,False,True,True,True,False,True,True],[True,True,False,True,False,True,True,True,False,False,False,True],[False,False,True,True,True,True,False,False,True,False,False,False],[False,False,True,True,False,True,False,True,False,False,True,False],[True,False,True,True,False,True,False,True,False,False,False,True],[True,False,True,False,False,True,False,False,True,False,True,False],[True,True,True,True,True,False,False,False,True,True,False,True],[True,False,False,True,False,False,False,True,False,True,False,False],[False,False,False,False,False,True,False,True,False,True,True,True],[False,True,False,True,False,False,False,True,False,True,False,True],[True,False,False,False,True,False,False,False,True,True,False,True],[False,False,True,True,True,False,False,True,True,False,False,True],[False,True,True,True,False,True,False,True,False,False,True,True],[True,False,True,False,True,True,True,True,True,False,False,True],[False,True,False,True,True,True,True,False,False,False,True,False],[True,True,True,True,True,True,True,False,True,False,False,False],[False,False,True,True,False,False,False,True,True,True,False,False],[False,True,False,False,True,True,False,True,False,True,False,False],[False,True,False,True,False,True,True,False,True,True,True,True],[True,False,False,False,True,True,False,True,False,True,True,False],[False,True,True,True,False,True,True,True,True,True,False,True],[False,False,True,True,True,False,True,False,False,True,False,True],[False,False,False,True,True,True,True,False,False,False,True,True],[True,False,False,False,True,False,True,False,False,False,True,True],[True,False,True,True,False,True,True,False,False,True,True,True],[True,False,True,True,False,False,False,False,False,False,False,False],[True,False,False,True,False,True,True,True,False,False,True,False],[False,False,False,False,True,False,True,False,False,True,False,True],[True,False,True,False,True,True,False,False,True,False,True,False],[True,False,True,True,True,False,True,True,False,False,True,False],[False,False,False,False,True,False,True,True,True,False,True,False],[False,True,False,True,True,True,True,False,False,True,False,True],[True,True,False,False,True,True,False,True,True,False,False,True],[True,True,False,False,False,True,False,False,False,False,True,True],[True,True,True,True,False,True,False,True,True,False,True,False],[True,True,False,True,False,False,False,True,True,False,True,True],[True,True,True,True,True,True,False,False,False,True,False,False],[True,False,True,False,True,True,False,False,False,False,True,False],[False,True,True,False,True,False,True,False,True,True,True,False],[False,True,True,False,True,True,False,False,True,True,False,False],[False,False,True,True,True,False,True,True,False,True,True,True],[True,True,False,True,False,True,True,False,True,False,False,False],[True,False,False,True,True,False,True,False,False,False,True,True],[True,False,True,True,True,False,False,True,True,False,False,True],[False,True,True,True,False,True,True,True,True,True,False,True],[True,False,True,True,False,False,True,True,False,False,False,False],[False,True,True,False,True,True,True,True,False,True,False,False],[False,True,False,False,False,False,True,True,False,False,True,True],[False,False,False,False,False,True,False,False,False,True,False,True],[False,False,True,True,True,True,True,True,True,True,True,True],[False,False,True,False,False,False,True,False,False,False,True,False],[True,True,False,True,True,True,False,True,True,True,False,False],[True,False,True,False,True,True,True,True,True,False,False,False],[False,True,False,False,True,True,False,False,True,True,True,False],[False,False,True,True,True,False,True,False,False,False,False,True],[True,False,True,True,False,True,True,True,False,True,True,False],[True,False,False,False,True,False,False,True,False,True,False,True],[True,True,False,True,True,False,True,True,False,False,False,True],[True,True,False,True,False,True,True,True,True,False,True,False],[False,True,True,False,True,True,True,False,False,True,False,False],[False,True,True,False,True,True,True,False,False,True,True,False],[True,True,False,False,True,True,True,True,True,False,True,False],[False,False,False,False,False,False,False,False,True,True,False,False],[False,False,False,False,True,False,True,False,True,True,True,False]], dtype = "bool")#candidate|2590|(104, 12)|const|bool
call_2589 = func_1202_call(relay.reshape(const_2590.astype('bool'), [8, 13, 12]))
call_2591 = func_1202_call(relay.reshape(const_2590.astype('bool'), [8, 13, 12]))
output = relay.Tuple([uop_2581,call_2589,const_2590,])
output2 = relay.Tuple([uop_2581,call_2591,const_2590,])
func_2615 = relay.Function([var_2580,], output)
mod['func_2615'] = func_2615
mod = relay.transform.InferType()(mod)
var_2616 = relay.var("var_2616", dtype = "float32", shape = (1, 11, 4))#candidate|2616|(1, 11, 4)|var|float32
output = func_2615(var_2616)
func_2617 = relay.Function([var_2616], output)
mutated_mod['func_2617'] = func_2617
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2987 = relay.var("var_2987", dtype = "int16", shape = ())#candidate|2987|()|var|int16
var_2988 = relay.var("var_2988", dtype = "int16", shape = (13, 14, 16))#candidate|2988|(13, 14, 16)|var|int16
bop_2989 = relay.left_shift(var_2987.astype('int16'), var_2988.astype('int16')) # shape=(13, 14, 16)
output = relay.Tuple([bop_2989,])
output2 = relay.Tuple([bop_2989,])
func_2998 = relay.Function([var_2987,var_2988,], output)
mod['func_2998'] = func_2998
mod = relay.transform.InferType()(mod)
var_2999 = relay.var("var_2999", dtype = "int16", shape = ())#candidate|2999|()|var|int16
var_3000 = relay.var("var_3000", dtype = "int16", shape = (13, 14, 16))#candidate|3000|(13, 14, 16)|var|int16
output = func_2998(var_2999,var_3000,)
func_3001 = relay.Function([var_2999,var_3000,], output)
mutated_mod['func_3001'] = func_3001
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3692 = relay.const([[[-5.680706,-5.944447,-4.920366,3.688766,2.046209,6.066161,-9.386443,6.438840,1.557425],[-0.804173,-2.345128,9.895830,0.005013,-9.445414,-2.617836,2.118153,8.404041,9.227208],[6.987948,-2.189858,0.876292,4.777094,8.135103,-6.382220,0.637853,9.600093,5.858046],[-9.245072,-8.288556,-8.009926,-4.133048,2.882788,7.731309,-4.991958,3.148849,6.244499],[-3.061044,9.834382,8.970045,-5.627670,-1.229930,7.887202,-8.709513,-7.853217,-8.346612],[4.679056,-6.975047,-0.410689,-4.110490,8.451179,-2.812855,-6.497065,4.570049,-7.009638],[1.516732,5.062963,9.531969,4.378609,0.758883,-7.888719,-8.415543,-9.268690,-0.998117],[-3.939909,7.050426,6.726611,7.607550,-4.968235,6.946334,1.333405,8.410999,-9.188963],[6.902007,-1.939068,-7.143536,-6.436185,9.658048,0.965907,-0.671101,-1.463968,5.142030],[0.037296,9.472296,-4.240481,-7.139535,5.238760,-9.323349,-1.033459,7.242212,-1.916608],[0.319082,1.332822,-0.871489,3.421768,-0.261594,-7.537168,2.125220,-2.810901,-2.670879],[1.761931,5.190527,-0.183272,-2.699961,6.912654,-1.147935,2.740548,7.933108,-3.804181],[-3.526170,-1.989036,5.405048,-0.615442,-6.095065,6.317810,4.566002,6.327639,8.130047],[8.214699,4.874002,5.423760,-8.012633,4.713471,9.704706,9.545866,8.991566,1.250805],[6.409920,8.853074,-4.336944,-8.591447,3.196661,-4.514942,0.132377,9.225449,6.257948]],[[-5.896339,8.709562,3.138823,7.369405,-1.112245,-4.014174,5.231908,-2.146218,6.014187],[7.000189,-6.773421,4.543404,7.654305,-7.426464,7.918058,-7.177821,-9.398876,-6.734774],[-7.914084,-4.245320,-8.831326,-1.463097,-4.575324,3.776239,-3.804117,7.709519,9.491395],[2.485923,-4.858210,4.925834,5.990623,2.340355,-7.980574,2.786833,-4.917221,3.001809],[-5.694695,-6.941244,-9.953820,-4.100225,8.203094,-6.856990,8.001382,4.413835,0.036281],[9.282122,-6.602748,-8.531789,-7.049204,-1.532479,-2.874929,-0.205751,8.105616,0.973215],[-0.238998,-6.585563,-2.342366,-0.511590,7.294375,3.026079,9.297177,4.321255,1.728727],[-2.393211,-7.485714,-0.871573,-3.253809,1.573046,-1.409503,-6.892958,6.094814,-8.478908],[9.514843,8.436657,-7.235843,1.608233,2.344661,-2.521605,0.099867,4.418252,2.201757],[-2.191773,-8.298250,1.202382,-4.356591,6.936685,7.463151,5.641227,-2.602717,4.770114],[4.621282,-6.607638,6.121467,-2.536694,2.060949,-0.582028,5.917414,7.940884,1.833834],[-6.385953,-8.104826,4.849635,7.322028,-5.374952,0.140624,0.723412,-0.925926,5.593789],[-1.288492,-3.802755,6.667138,-3.404711,7.724380,-5.614794,-2.047529,9.955429,-9.611835],[-4.392403,2.912923,-7.294464,-7.361319,-1.997544,5.540838,0.015598,0.994098,-4.737152],[-3.107487,2.177027,-2.233601,-6.297165,8.327568,9.011680,-7.861522,0.839370,-0.539151]],[[-1.732381,5.658098,8.855732,3.904369,-5.905890,5.158025,6.033519,2.404709,7.102225],[7.033791,2.202684,4.488060,-7.985470,-0.626374,-4.777552,6.646625,-6.440797,6.024271],[-7.016817,-2.519480,0.437937,5.225219,3.949982,9.317928,-4.075810,1.110718,5.508771],[-9.454928,-2.569270,-2.852162,6.789214,-3.097752,-4.624029,1.083719,-5.794712,-4.466111],[0.074706,-3.789350,-3.005690,-6.244358,-7.367114,-0.329846,-9.342549,-1.902572,-8.346106],[2.713979,-4.845806,4.900268,8.658794,3.700045,-0.812505,8.339155,3.398968,-0.065891],[-7.474493,-2.137437,-2.593164,-4.966290,8.003962,-2.666494,0.833929,6.511398,5.715339],[2.195168,-2.430342,-8.199198,-9.922332,-5.705848,9.116953,4.521355,5.757979,6.640452],[5.722327,2.057894,-4.842589,-9.575961,4.732264,5.343979,-7.413766,-5.636160,-7.722618],[9.687155,-5.587511,-8.070319,-2.882259,8.676749,-8.760886,-1.028086,8.734925,-5.038429],[4.570300,2.605604,5.800728,5.612220,1.381974,-0.255311,-4.200733,-4.253010,8.892758],[-3.656133,4.343228,-4.714273,-0.354586,2.665322,-0.706185,9.861215,-4.450992,-2.744966],[-9.283519,0.051018,7.996778,7.228824,6.298493,1.023778,-6.417854,-5.325354,5.482368],[9.713119,3.142707,9.996261,2.831834,5.097251,-6.526764,3.573426,6.951486,-4.669706],[-8.919409,-9.081049,-2.917198,-7.689382,-4.019331,-2.188741,6.154313,6.498888,-3.784570]],[[-9.666880,-4.758557,5.871886,-9.269486,1.704783,9.608240,-8.141009,9.043504,8.583342],[-1.306936,-3.270056,-7.668271,5.699902,6.122599,4.359287,7.732511,6.048955,5.235094],[-1.833990,4.232121,-4.747700,-0.863154,-4.134845,7.902227,2.224546,6.325902,-7.813717],[-3.547758,-8.278171,8.295353,6.779819,6.737078,-1.278895,6.669367,-7.577081,-3.243270],[8.341382,-8.904654,-6.080189,8.160605,9.869686,0.860058,-5.404169,4.438258,5.238834],[-5.889830,-2.699816,5.088803,6.475994,9.764731,0.916285,-4.976911,-3.008145,-4.343407],[-3.262535,-9.895141,3.189022,-6.911015,5.681575,-6.756609,-3.213693,2.601553,-3.939742],[5.320520,4.976240,-4.703412,-1.262070,4.548978,0.018762,2.302308,6.578591,1.654316],[6.698698,9.303891,-6.552828,-7.666513,-3.026361,9.506247,-9.736909,-6.311308,6.861429],[1.309174,5.649697,2.477100,-3.842806,7.191681,-1.618632,-5.764780,-7.596869,8.099049],[0.942043,5.742921,9.012302,1.191754,7.616330,-8.658394,-2.843815,-8.263207,-3.607497],[-3.544664,-0.127140,5.927076,-6.416768,-6.616144,2.549129,9.422582,2.283702,-6.188868],[4.714179,0.201086,-3.954056,-6.713796,8.029333,-2.246383,-9.476402,-9.768182,-3.240978],[4.022449,-3.632938,1.534553,3.966940,-7.766984,5.290004,-1.173933,-3.923591,8.637143],[4.734166,6.852108,-2.637742,-4.535824,-5.320377,1.630123,-1.940972,-7.145219,5.882496]],[[-8.410396,-9.457406,3.513049,-7.089529,6.159563,2.070657,4.859537,-6.825892,8.670380],[-8.222939,2.240229,2.981303,-7.715818,5.896804,-7.150872,-0.223764,-7.698137,6.284241],[4.286863,2.457195,5.484533,8.316232,8.444548,9.312090,4.188688,-6.907134,5.574524],[1.933562,-8.880910,-9.886733,3.696899,6.466923,1.733661,-0.795527,-9.814183,5.996917],[-6.609218,-6.030141,-5.252295,4.740961,-2.327479,-7.049896,0.209393,5.189809,5.294020],[-2.885650,-8.844591,-8.780143,-4.517870,-5.141936,-6.327436,-9.834043,8.372414,-5.446777],[8.865648,2.556516,8.549856,6.474974,4.004084,-9.309481,-1.435823,-3.554564,0.419472],[-7.885020,9.607918,-4.619407,2.900986,-2.341172,-5.670952,-4.594624,-4.620829,8.947409],[-7.560764,-0.264134,9.506468,-3.020748,5.216870,-6.599799,1.049087,5.375401,-8.244784],[-4.335108,-0.073174,-5.277886,8.239308,-1.261571,-3.122225,9.210805,-7.496840,-7.025972],[7.039549,1.068686,1.300291,8.787348,6.332047,7.610729,-3.508145,5.299577,2.060850],[0.284087,-0.383884,-5.560079,9.193918,2.466459,-1.824958,8.802985,-5.651091,-3.389248],[5.991551,-3.206320,-4.855181,-8.005105,7.345729,-2.217597,7.788312,4.001779,8.266464],[-0.439095,-8.311371,5.497291,9.747343,-3.595576,8.935783,-1.069454,-1.389503,7.625186],[-5.601120,8.403949,3.209955,-6.026458,-8.082785,8.360713,-9.708481,-9.545248,8.003448]],[[7.628697,1.313111,7.669266,-4.697264,8.765543,-5.690359,-1.779427,-9.627831,7.564802],[5.135026,-1.466576,7.617410,4.796104,0.240943,-0.484505,9.190696,1.856770,9.331456],[-5.177065,-3.220666,-3.287259,-4.724485,-4.825833,1.492544,2.670537,8.607102,-6.399150],[6.117076,-9.022468,1.570540,8.736619,-7.122088,9.793205,2.486769,-7.049623,6.234349],[1.721519,6.542882,-0.701963,4.336515,7.907654,5.380663,5.219916,7.230070,1.332958],[1.237019,-1.649248,-0.423583,1.744264,8.255041,4.849503,2.796701,-6.688693,-2.132804],[0.095017,-7.623701,1.520976,-9.454532,-9.851031,-3.627026,-6.677250,0.976964,-2.938579],[4.821747,3.252198,5.199216,4.682721,7.175589,8.967666,9.877594,6.107462,2.385267],[4.842765,-6.307550,5.980217,-4.139460,-1.432151,-7.890585,2.414071,-9.334444,-2.120409],[5.764203,-6.179790,-8.086629,4.221487,-8.266946,2.982137,4.537769,4.452885,2.875412],[-2.628137,2.399797,5.458857,1.388773,8.326872,8.629075,4.977512,6.364394,-4.065045],[4.496367,1.572688,-6.152036,4.711244,-7.452599,8.051593,-4.126731,4.161694,-5.945387],[3.171179,3.920007,-6.807606,0.327739,7.775467,9.206902,-4.916085,0.948079,0.035203],[-8.658986,9.207458,4.639431,-4.667176,6.252807,6.513310,-0.040119,2.749024,3.414620],[3.250109,-3.134408,-9.030468,-7.735609,-6.625642,-8.875587,0.697090,7.279246,3.291344]],[[-7.591734,-6.772123,9.540985,3.564166,-4.600869,1.114202,-3.901752,-8.130655,-4.480460],[9.019273,2.195085,-6.776635,9.947500,1.736893,0.728374,7.034525,-0.541202,8.170332],[-4.321693,-7.378117,4.206034,-6.364666,-9.351970,-0.667713,4.106764,1.827590,-4.848686],[7.540232,0.273460,-9.869639,9.543069,-7.167654,5.621570,-1.779777,7.790877,-8.163398],[-1.756255,-1.706609,-2.860445,4.340467,-0.328232,-1.527226,4.514858,-6.331937,-3.716616],[9.486855,3.276037,-1.896296,5.242083,-8.958292,6.324881,0.375100,3.288668,-7.577527],[4.909833,-1.529594,-5.204126,-4.237886,-7.003432,-3.021499,9.469333,-2.800985,-0.525658],[0.416672,9.098954,-8.202543,-9.470229,0.118386,4.253385,0.153472,7.937064,6.646401],[5.347034,6.197857,-8.894779,-6.978540,6.475064,-5.078005,8.562655,7.388638,4.525834],[4.199130,-3.733889,-7.849148,-5.075350,-0.391688,4.723921,8.291896,7.815152,-3.681203],[0.640156,0.971711,9.378908,-9.498391,4.405957,-6.947629,6.958314,-2.180214,-7.535312],[7.620920,8.864424,-5.721557,1.145874,0.821192,1.570035,7.805232,-6.825853,8.060413],[-7.696124,7.625630,-3.337391,3.588445,6.166419,0.349992,-2.824819,6.730404,-4.178322],[-8.632614,6.723119,-2.501209,3.770107,2.192526,-6.840543,9.739321,-2.485196,-3.944423],[-2.948029,-0.828185,8.584769,8.714677,5.860911,1.079917,5.605752,8.149225,3.794180]],[[5.570864,7.983629,3.911745,3.044280,9.820907,0.459860,-7.397642,3.158262,8.319692],[-7.140797,-7.629203,5.238255,3.936943,5.534455,-4.869628,-2.138772,9.232307,-2.812557],[7.373738,3.998397,-8.491033,-5.370053,6.305788,1.287114,5.217050,8.242663,3.770142],[1.005078,7.532023,-3.952159,-0.277010,3.668866,-3.132025,-4.457923,-3.548589,-2.369163],[-7.803937,2.699232,-4.999455,-6.047759,3.128747,6.405705,8.482200,3.776793,7.606107],[-1.488638,6.836450,0.189435,4.482701,3.476794,-1.276172,-9.962852,2.639651,-5.916351],[0.950739,7.075832,-9.824755,0.419513,1.037783,4.246928,-2.412744,-1.445978,0.848480],[-9.536803,8.869971,-0.207644,6.081269,-2.092679,1.807485,4.016998,-9.816033,2.629383],[4.793623,-8.007068,6.568607,-0.955531,2.725120,3.567104,-2.341868,3.503660,-2.756997],[1.813512,4.973767,-6.855965,-8.477748,7.289804,-9.931781,-8.044724,5.102444,-7.589375],[-9.239621,7.356754,-0.554099,-8.244743,-7.411650,-9.643266,-6.334977,-5.237540,-2.287941],[-2.918981,-1.178467,5.863510,-4.039396,9.555787,-2.777104,-5.685925,-8.532340,-8.742745],[7.633042,3.480769,-7.969655,-8.271019,-6.877277,-5.928285,6.069833,3.506850,-1.377668],[-0.184022,-1.883496,3.095479,0.762764,0.201002,0.102924,-3.968515,7.240253,-3.438292],[-8.172901,-7.404288,9.126210,6.113528,4.424943,4.323314,8.295180,-7.643766,7.245916]],[[-0.011498,2.854513,-0.802803,9.729408,1.985529,-9.061744,-2.558557,-9.653744,5.257855],[-3.102875,-8.156611,-0.057469,8.976123,4.226565,2.202313,2.015317,-8.295361,-0.738863],[8.830726,3.189352,-5.987014,-6.697819,-4.453913,7.057063,1.003539,-8.284766,2.480038],[4.205664,-8.032600,-2.523146,8.440829,2.374747,-8.926397,-4.775991,5.118475,5.829927],[7.850925,7.887386,-3.355363,-4.821521,-9.647469,-6.645507,4.000447,-2.875447,-4.790150],[3.523699,0.724256,5.236528,-9.403077,8.855252,-5.151078,2.335190,0.562065,9.937866],[4.528681,9.965848,4.021645,3.788166,2.834924,-4.389801,-6.726412,2.104028,8.483812],[-2.176451,-3.530904,9.239456,-2.746685,-8.999548,6.171612,8.761966,0.984777,-3.118481],[-4.535813,2.417417,-3.541768,-9.659688,-9.455451,-9.383377,-3.581576,1.903416,-7.063538],[9.102388,-5.752797,-6.897208,-1.581953,-9.668713,-9.043970,-2.572941,9.373913,-0.569715],[6.099340,-2.686714,-5.666336,5.566926,8.420623,0.461580,-3.314452,-5.991991,9.178532],[-6.925868,6.845378,7.780401,-4.955393,-6.421664,-6.131249,2.755504,8.657640,3.089378],[-1.527430,8.527823,9.783549,7.615827,3.842809,-2.707444,0.232963,-0.602256,-2.149601],[-2.144504,4.871135,-6.741391,-9.340810,-3.944986,4.326172,1.567890,-1.858069,-9.630524],[-0.341890,3.824132,3.032184,-2.646284,0.269631,6.205934,-5.910973,-9.944973,0.967069]],[[8.345140,-1.962412,1.016254,0.557513,8.901584,2.516135,-4.094111,9.060668,-7.358615],[4.356171,6.616225,0.338169,-4.211794,2.134299,-6.052861,3.948389,-4.813344,4.654780],[-8.809329,-9.486688,-4.433218,0.195242,5.715330,2.546480,5.107297,-9.115544,7.361057],[-3.236354,-8.368862,-8.398821,-1.933389,-8.514645,4.770533,-2.396572,6.014110,3.428383],[5.730907,-9.081086,6.067622,-2.732580,-8.030496,-4.738224,-4.257863,-4.236550,-1.513065],[4.858202,-4.946952,7.440643,7.770746,0.794234,-1.954947,7.000345,3.930573,3.058522],[8.661795,-3.033100,-9.221598,2.928360,3.297981,0.412036,-3.496723,-8.243337,7.233419],[-8.126830,2.258049,6.166913,-0.383996,0.291017,-8.076104,-2.652762,-8.551865,0.040364],[4.184153,-4.660737,-5.276898,-0.030084,-9.945809,-0.774387,-8.846879,9.230376,-7.095476],[-4.885927,4.691732,4.017392,-4.003109,6.336905,-7.572288,4.054387,7.889226,-1.648444],[-2.043065,-8.132708,9.693368,-8.220384,2.279683,4.504930,-9.963317,-9.102189,-3.249542],[1.832350,8.583660,2.608701,1.681816,-3.933936,-5.283320,1.782426,2.999679,-7.257302],[-4.920558,9.198315,-1.462353,9.217217,-9.982280,-3.229971,7.088346,8.642664,-1.298098],[-7.314203,8.860180,-8.457281,4.800772,-0.095387,5.701028,8.767778,9.835238,4.825776],[-9.327366,-6.023779,-8.850957,5.897358,-3.678785,-7.161808,3.346229,9.939383,4.450354]],[[0.509180,7.552224,-8.852350,-2.461736,-1.433769,-9.990023,3.187839,-6.840747,9.863751],[-5.881308,5.709897,1.561479,0.728411,-9.411012,5.375408,-8.906075,6.508415,6.401683],[-0.404182,7.345277,4.705727,-9.081918,-8.843592,1.732974,2.334670,-8.573940,-1.211917],[-6.677238,2.330293,-8.184302,5.694143,4.117513,-3.603952,-9.194843,-5.010413,6.475197],[0.283014,-3.500248,9.883840,3.277358,4.218740,5.606637,2.670866,8.834959,-4.847743],[7.096101,-1.697469,-5.147560,3.605524,4.703853,4.690838,-5.973437,-4.730087,-1.302230],[-1.335061,-0.808352,-0.179399,1.752829,4.019370,-0.673490,8.687521,8.747780,-3.616042],[-8.792664,-6.528256,0.826994,4.828352,-0.251112,-1.151785,3.980905,-4.857058,-3.038090],[7.222034,-9.681909,-7.670472,-1.780170,1.318055,1.317989,-0.147726,7.102064,3.929596],[-5.015466,-0.530928,-1.281798,1.366877,4.195179,8.108898,-5.488073,-9.987915,2.823283],[1.311641,-3.229554,-7.022243,-4.051649,8.556541,7.096346,-6.498228,3.368376,9.885579],[7.332976,4.420682,-0.405742,-5.756506,4.071924,-9.376945,3.560629,9.726608,-5.263266],[2.922007,-7.446448,-3.224709,2.903310,0.270048,-6.021371,-9.338024,5.024800,-1.883132],[-9.860316,8.124144,3.339691,5.126942,2.345819,-0.063810,-8.208769,4.029595,8.948245],[-2.724865,-5.793265,6.709773,-7.406487,8.092910,-2.704048,-3.361236,-9.563311,-6.805745]],[[8.873934,7.750049,-3.935137,-5.878182,4.846048,3.552813,5.920452,-8.374712,5.776703],[-9.868256,5.711112,-2.444303,-4.527809,6.269316,-8.031981,-2.894254,6.891962,-5.096682],[-8.428847,-3.739560,-4.636202,-3.000030,0.399854,-6.733723,-0.153888,2.994037,-9.220218],[4.938115,-0.669078,7.195320,7.364906,-0.759899,1.537090,-0.601803,7.761632,-7.710610],[9.621788,2.959904,2.931844,2.784461,9.730724,5.648387,-1.872141,-7.539725,1.742997],[8.395184,7.469475,8.171822,3.004534,-9.478506,-9.219348,-4.065328,2.620676,1.796811],[9.753540,9.548512,7.787379,-2.492606,1.556849,-7.484884,3.597203,2.581774,2.308872],[6.452580,3.054109,8.078507,-2.976872,8.407348,4.608807,-0.126384,5.084897,9.479796],[4.954784,7.993838,-2.828111,0.952742,3.703482,9.411551,-5.598001,7.013286,-8.150772],[8.628318,4.173781,1.321873,5.528577,5.792877,9.184160,3.483150,2.551316,9.290917],[-9.148839,6.711453,-6.332455,-3.181027,0.727892,-8.430919,-6.359147,0.131145,-3.915684],[6.827481,-8.277840,-6.722992,0.212117,-7.157536,-7.641678,7.997353,1.441065,3.783600],[0.948088,-2.828433,3.088000,-4.688318,-5.819767,1.131725,-6.437457,4.369644,-0.452315],[-4.861628,3.708362,-3.875119,0.112154,3.274693,-0.196493,-5.910327,-0.477255,-9.840181],[3.182277,-8.717799,-9.276684,-3.894942,-7.286675,-2.477682,3.038727,-5.330995,6.999922]],[[6.944611,-6.941586,4.962516,2.137525,-2.607754,-6.016978,5.204846,-8.741479,-6.170148],[-9.785454,5.968403,-3.141775,6.097878,6.379506,-4.822703,-2.708117,6.547620,-5.182919],[8.084911,-0.169415,-9.137247,-8.469899,-9.470386,2.418424,-0.727701,8.254352,-4.018062],[4.447884,3.792546,3.450119,1.603261,0.709223,3.355686,-8.008653,2.082367,-2.298325],[3.572962,-7.482042,5.241385,-7.942373,4.732106,-7.414299,4.836104,0.985580,-6.277141],[0.338976,-7.387391,-0.019075,-6.873408,-6.099430,7.401287,1.530465,3.656659,-6.516186],[6.501146,-3.643371,-9.336730,-1.927099,-5.366028,-8.718513,2.345738,2.627576,3.144306],[5.229280,-8.192643,6.468868,-9.191975,-2.882416,-1.261461,1.890200,-2.809924,-7.637355],[-4.742824,-0.190487,-2.383653,5.125457,-1.841065,5.266440,-8.516560,-2.979115,-1.697692],[-3.261781,-9.443817,6.208326,5.247180,5.018443,-3.233738,-5.998967,-1.512314,-9.763022],[5.006861,-3.685651,-9.547424,9.208492,-6.408666,0.359622,-6.195418,-6.550844,-3.131324],[5.298743,-7.858058,8.025550,9.368737,6.501559,5.844051,-7.505220,7.681945,-9.187362],[5.203214,-5.356808,5.185482,-3.806071,2.668609,9.097653,-4.082276,2.049528,9.501597],[-1.566119,-2.522583,-9.046513,4.817473,-4.452732,-2.158764,-1.139364,3.498486,4.374629],[-2.183871,-8.323926,-6.101305,1.249154,-1.249342,1.206275,-6.013457,-4.212232,0.924839]],[[-2.913477,-0.551999,9.538613,4.943800,-2.634127,-7.810737,-1.045264,0.092476,-9.751747],[-1.979523,3.884421,-9.713978,-6.363712,-5.862001,7.735597,0.787432,-6.862665,6.941218],[-7.900187,6.186741,0.540307,4.630270,-4.857319,-9.667699,-6.060981,-5.609948,9.740177],[5.492054,8.844007,3.273242,4.169768,-2.130788,-1.996320,-5.194762,3.512267,5.535744],[1.564783,-2.217565,3.589108,1.279247,7.990346,6.806237,-7.828511,-4.226820,-0.751733],[8.695484,-9.417565,9.390896,8.468897,-2.661789,8.408333,7.550364,-8.711458,-5.677602],[-4.476493,1.216022,-0.198254,-3.748461,8.367195,-4.773714,-6.222682,-5.357879,-3.783749],[7.860889,1.372508,-5.509351,8.646255,0.742579,6.851066,-0.233130,3.629239,8.744903],[-0.970478,0.648063,-1.619262,-7.523896,2.421046,5.069849,-2.379535,9.496949,-9.398007],[3.282930,6.975573,5.134125,-1.504263,-1.404783,-2.138333,6.303142,3.697627,-1.152877],[3.079517,6.376408,3.212816,-0.755112,9.050105,3.201658,8.603496,-9.695001,-6.389806],[1.982658,8.890161,-9.123183,3.483320,-7.151563,-8.016009,-2.040262,9.003790,-1.769145],[-7.333302,9.103018,-7.520380,-0.251484,7.295491,-3.801728,-7.372778,-4.560017,0.822996],[0.292704,8.073790,-1.370518,5.439466,5.839046,-2.597865,1.925101,-2.990625,-8.811857],[-4.896657,-9.444878,6.947834,0.205110,-5.844821,6.353566,-2.724200,-7.929526,2.771928]]], dtype = "float64")#candidate|3692|(14, 15, 9)|const|float64
uop_3693 = relay.asin(const_3692.astype('float64')) # shape=(14, 15, 9)
bop_3696 = relay.multiply(uop_3693.astype('int64'), relay.reshape(const_3692.astype('int64'), relay.shape_of(uop_3693))) # shape=(14, 15, 9)
bop_3699 = relay.floor_divide(uop_3693.astype('float64'), relay.reshape(const_3692.astype('float64'), relay.shape_of(uop_3693))) # shape=(14, 15, 9)
output = relay.Tuple([bop_3696,bop_3699,])
output2 = relay.Tuple([bop_3696,bop_3699,])
func_3703 = relay.Function([], output)
mod['func_3703'] = func_3703
mod = relay.transform.InferType()(mod)
output = func_3703()
func_3704 = relay.Function([], output)
mutated_mod['func_3704'] = func_3704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3703_call = mod.get_global_var('func_3703')
func_3704_call = mutated_mod.get_global_var('func_3704')
call_3748 = relay.TupleGetItem(func_3703_call(), 0)
call_3749 = relay.TupleGetItem(func_3704_call(), 0)
const_3752 = relay.const([[[8,8,-7,3,-7,2,-7,9,-10],[-8,-7,1,7,-10,-8,4,5,2],[-4,1,8,-5,-6,5,-5,-8,-3],[-10,3,-3,1,7,-1,7,5,-7],[1,6,-6,7,5,-4,6,-9,5],[10,-3,-1,7,2,-6,-5,-10,-6],[5,8,9,-10,-7,4,5,8,-2],[-2,7,-2,-2,-1,9,7,-1,6],[8,-4,7,4,1,-7,1,1,5],[2,-10,8,-10,-5,-1,-8,-7,3],[-10,3,1,2,1,-9,-7,-4,3],[8,8,-2,-4,-9,5,-4,-8,-4],[-7,10,-2,-4,1,-7,1,-8,7],[-9,2,-2,7,2,3,2,-4,1],[3,-6,5,-9,-7,3,-8,-6,8]],[[9,-6,-1,-9,-2,-7,-3,-8,5],[2,-8,-10,6,-5,10,2,1,2],[-8,6,6,-1,-4,-9,2,2,2],[-3,9,1,-1,9,-3,-1,2,9],[1,-8,-10,-1,-8,-2,-4,-9,1],[4,-4,-2,-2,8,-2,-5,-8,7],[1,10,-2,2,-7,1,-2,10,8],[5,-8,-5,1,-3,-2,-6,-10,-2],[1,10,-4,6,8,4,-9,-5,3],[9,-7,-2,5,-1,6,-9,7,3],[-4,9,-6,-5,3,3,-9,7,-5],[6,7,-6,1,8,-9,-9,-3,-5],[3,-3,10,-10,8,-7,-8,-4,-10],[-10,8,-1,10,-9,2,1,4,10],[1,4,-1,2,-4,6,7,-9,3]],[[-3,1,7,6,9,-1,-3,-10,4],[8,3,-4,-5,5,7,5,-1,2],[2,-6,-7,9,-1,-6,2,-3,-5],[-2,-10,-6,4,-9,-8,5,-8,-10],[-9,-6,7,7,6,-2,7,-1,2],[-5,7,-1,4,6,6,8,2,-6],[-6,8,-5,10,6,-10,-7,5,7],[-10,2,5,-9,-3,-7,-1,4,-4],[10,10,5,4,-2,-7,-5,-4,-4],[-6,1,7,-8,4,8,2,2,-5],[1,1,10,-6,9,-3,8,8,-9],[-9,1,-1,-1,-10,7,2,-7,-3],[4,-4,-7,8,8,-5,8,6,-9],[-2,-1,7,-8,-6,-3,3,-6,2],[6,1,3,1,-3,-5,-5,7,7]],[[-2,1,1,-6,-3,1,-10,-5,-3],[8,-2,-2,-5,3,-2,4,-7,-1],[2,1,2,3,1,2,6,7,-2],[4,5,-1,-10,-1,1,3,3,-1],[8,-8,1,2,-1,7,9,3,1],[-2,-9,5,-9,5,4,7,-7,-10],[5,6,-2,-9,4,-8,-8,-3,-5],[6,9,-6,-7,-5,-7,5,-9,-10],[-3,4,3,-4,2,7,-8,-3,-4],[9,1,-8,-1,2,5,2,1,7],[10,4,-9,-1,-3,5,3,-1,-10],[-3,-1,4,7,3,-2,1,-2,-3],[-5,9,9,5,7,-6,-2,-1,-8],[-10,9,-2,-4,4,-7,6,-3,9],[-8,-6,8,-4,-5,-7,8,-7,-1]],[[-9,-1,10,9,-1,2,6,4,-6],[8,-5,5,-5,9,1,10,-4,2],[-10,-1,-5,2,-6,-5,-1,4,-5],[7,-1,1,-6,-1,-1,-6,6,-3],[2,-2,4,-3,-2,10,-6,-7,-5],[1,9,-2,7,-5,-5,3,6,8],[-5,-4,9,-4,10,4,-10,-7,-8],[-3,-6,7,-7,-1,-6,-4,1,7],[9,-7,-3,-4,-7,-3,-9,2,-5],[9,9,-8,8,-7,-9,10,-6,-8],[-9,3,3,-1,-4,-10,-9,-4,8],[5,-3,6,7,-9,5,3,2,-10],[-3,9,-1,8,-9,-10,6,2,10],[-1,-8,-1,10,8,1,6,6,-1],[6,7,-6,2,-2,1,-4,8,-5]],[[-6,-4,-6,10,-9,7,3,3,-1],[-7,-9,9,3,-2,-5,2,1,-6],[1,9,4,1,-1,9,1,5,7],[10,7,-10,9,6,8,-7,9,10],[-1,-1,3,-4,-6,-4,5,2,8],[-8,6,8,-7,-4,10,10,-4,6],[2,4,1,10,4,9,8,8,3],[-9,-1,-9,-8,4,1,-9,-10,-1],[-1,-10,-5,-6,8,6,-9,4,-9],[-1,-3,8,3,-8,-10,-7,-10,-7],[-5,7,-6,7,-9,5,3,4,9],[1,-7,8,-8,10,1,4,-10,-1],[5,4,-10,-1,-3,8,-4,5,-10],[3,-9,7,-10,-7,-3,9,-8,-3],[1,1,8,7,10,5,8,-7,1]],[[-4,4,-3,2,8,-6,8,4,5],[-3,-4,-6,-5,7,9,6,10,7],[-1,-7,10,-8,5,10,-4,2,-7],[6,-3,2,2,-9,9,6,-6,-9],[-8,-7,-8,1,-1,9,1,8,2],[-10,-1,5,-7,-2,-3,1,5,-4],[-6,-7,6,-5,-3,3,-6,-10,-1],[8,7,1,8,-1,2,8,-10,7],[2,5,8,1,-2,-10,7,1,8],[1,-5,-3,-10,7,7,-6,-5,-4],[-10,6,7,4,-5,-5,-8,1,1],[-4,-6,-8,4,-9,4,1,-10,5],[4,9,-6,-4,-1,10,10,2,5],[-6,6,8,-1,-6,-8,6,10,-3],[10,-3,-4,-6,8,-10,-9,-2,4]],[[-7,-10,5,5,2,-9,-2,-4,-1],[-9,-5,-6,-8,5,-2,-1,-5,-3],[1,-4,-3,-9,3,1,4,-2,5],[-7,-2,4,-1,-2,-5,7,-1,10],[3,9,5,-1,-8,-9,8,7,-6],[4,5,4,-9,8,1,3,7,9],[4,10,-2,4,-5,-9,-1,8,9],[5,-2,-9,9,6,-6,8,6,1],[-7,7,-5,4,-1,1,4,-7,9],[9,10,5,-2,-5,1,6,2,-9],[-4,-4,-5,5,2,-8,-8,10,2],[-5,10,-3,-7,-8,-6,7,-10,-5],[5,-8,1,-8,3,-8,-5,1,2],[-4,-5,-7,9,-1,4,-8,5,6],[2,-7,-1,-1,-10,10,6,-1,8]],[[4,-2,8,2,-5,-4,4,-2,-10],[-8,9,-3,9,5,-2,8,10,-4],[7,6,4,-10,3,-1,-7,4,-8],[7,6,-9,-4,-6,-10,5,-8,-7],[9,3,9,7,-5,-2,-9,4,10],[6,2,-8,-4,-8,-4,-5,2,6],[-1,7,-7,-3,-7,-4,8,-1,-5],[3,-4,2,-5,2,4,-7,3,3],[3,8,10,-7,5,-1,8,10,4],[-1,-2,4,-1,10,-7,5,8,-1],[7,-9,7,3,-3,-1,-8,3,5],[5,-8,-1,-10,6,4,-6,-7,-3],[2,-2,-10,1,-7,-7,2,10,9],[-5,-10,4,-10,4,3,2,5,2],[8,5,-6,8,4,-7,9,-1,7]],[[-4,-6,-4,8,-6,-1,8,10,7],[-6,5,2,5,6,-2,-1,-9,5],[-8,7,-3,2,10,-7,-9,1,-4],[-8,4,-5,6,-1,5,-8,8,-4],[-6,4,-10,2,-3,5,-5,6,-6],[4,-1,7,-10,8,2,8,-10,-3],[-3,-10,-7,-4,6,2,5,6,-10],[1,-9,9,-10,-7,-9,-1,-7,-9],[-3,-9,-4,-5,-6,2,-3,7,9],[3,-4,2,-5,6,-1,6,-9,-7],[5,-10,2,-8,-7,8,2,-7,-6],[-10,1,10,-2,-8,-3,-3,-6,9],[9,2,4,-3,-3,-5,-9,-7,2],[2,6,-6,-4,7,-6,-7,-6,10],[-1,10,-3,-3,9,-3,-9,-6,5]],[[-6,-5,-9,1,-5,-3,9,-5,-7],[4,-1,2,-8,8,-8,8,-2,-6],[3,4,-6,-2,-2,6,5,9,-4],[1,4,6,2,5,-8,-4,-10,-10],[7,1,-8,1,8,-1,-3,-4,4],[6,-7,-2,3,7,-6,8,-10,-5],[8,4,-5,8,-9,-2,4,9,-10],[8,6,-7,-4,-6,-7,-3,-6,-1],[-3,-9,-3,5,3,-1,-4,-8,-6],[-5,-1,-7,1,-1,8,-7,3,5],[-9,3,4,-6,-5,-3,7,-5,8],[-7,3,-7,2,-4,-2,-8,9,4],[7,4,-2,3,6,10,-10,-4,-4],[6,6,10,-8,2,2,-3,-6,1],[5,-1,-1,-4,7,8,10,9,5]],[[-6,10,2,-4,2,-3,9,-6,8],[1,-10,1,-2,-1,9,-2,1,-2],[7,8,-7,-10,-9,-7,6,3,6],[4,-7,1,-3,10,7,6,10,-1],[7,3,10,4,-8,1,-3,2,-2],[-5,-5,10,10,4,-2,-7,8,4],[10,5,-7,1,-3,-9,5,-1,-2],[10,7,-2,-1,-7,-8,1,10,-5],[-2,4,-9,-2,8,5,-6,-10,1],[1,10,2,-8,-8,-9,-5,9,-6],[-2,-3,2,10,2,-1,3,-6,-2],[5,-3,10,5,-1,-5,-5,5,-9],[7,-5,1,-4,9,-1,8,3,-8],[3,6,-10,-1,10,-4,-3,10,9],[-3,10,-3,-3,7,-2,8,-6,1]],[[7,-10,8,-8,4,8,-1,-8,-2],[-4,-2,10,-3,1,-3,7,4,7],[-3,2,4,3,-10,-8,2,5,10],[9,-4,-7,1,-4,-3,-7,-7,6],[-9,-7,-1,-1,-7,-6,4,2,-6],[-2,3,3,9,4,1,7,10,10],[9,2,-10,2,-6,9,-5,8,-8],[-6,1,7,10,3,-8,-9,6,2],[2,7,10,9,-10,-3,-7,7,9],[-1,8,8,7,-6,1,-9,3,4],[-4,1,9,2,3,4,-5,-2,9],[2,9,8,-5,-6,5,-4,-10,-2],[-8,-5,-6,-4,3,8,6,-7,8],[-5,-4,-5,-1,-7,3,10,-6,4],[-3,6,4,8,-6,5,4,-8,2]],[[-9,-2,4,6,9,-8,-5,-1,8],[7,-7,5,-4,3,7,-7,8,3],[-5,7,-4,-4,7,1,3,3,8],[2,-7,6,-10,-2,-2,-10,7,-8],[-2,9,-2,-7,8,-4,10,-10,3],[-4,-1,-1,3,-10,1,-1,-4,4],[-3,-10,-3,-9,4,-1,-7,10,-1],[-3,-6,-7,10,-2,10,-10,-1,6],[-7,-6,-4,8,1,-1,10,-7,6],[-5,-1,3,-7,6,5,1,-7,-3],[-3,6,10,6,-1,10,6,4,-4],[-3,-9,-8,-1,6,-5,2,-3,-2],[4,-5,-3,-2,10,-8,-6,5,2],[-2,10,2,9,3,-10,5,5,1],[-6,-6,-3,-1,9,-4,9,1,-4]]], dtype = "int64")#candidate|3752|(14, 15, 9)|const|int64
bop_3753 = relay.right_shift(call_3748.astype('uint16'), relay.reshape(const_3752.astype('uint16'), relay.shape_of(call_3748))) # shape=(14, 15, 9)
bop_3756 = relay.right_shift(call_3749.astype('uint16'), relay.reshape(const_3752.astype('uint16'), relay.shape_of(call_3749))) # shape=(14, 15, 9)
output = relay.Tuple([bop_3753,])
output2 = relay.Tuple([bop_3756,])
func_3776 = relay.Function([], output)
mod['func_3776'] = func_3776
mod = relay.transform.InferType()(mod)
mutated_mod['func_3776'] = func_3776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3776_call = mutated_mod.get_global_var('func_3776')
call_3777 = func_3776_call()
output = call_3777
func_3778 = relay.Function([], output)
mutated_mod['func_3778'] = func_3778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3703_call = mod.get_global_var('func_3703')
func_3704_call = mutated_mod.get_global_var('func_3704')
call_3869 = relay.TupleGetItem(func_3703_call(), 0)
call_3870 = relay.TupleGetItem(func_3704_call(), 0)
output = relay.Tuple([call_3869,])
output2 = relay.Tuple([call_3870,])
func_3880 = relay.Function([], output)
mod['func_3880'] = func_3880
mod = relay.transform.InferType()(mod)
output = func_3880()
func_3881 = relay.Function([], output)
mutated_mod['func_3881'] = func_3881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3880_call = mod.get_global_var('func_3880')
func_3881_call = mutated_mod.get_global_var('func_3881')
call_3908 = relay.TupleGetItem(func_3880_call(), 0)
call_3909 = relay.TupleGetItem(func_3881_call(), 0)
uop_3910 = relay.cos(call_3908.astype('float64')) # shape=(14, 15, 9)
uop_3912 = relay.cos(call_3909.astype('float64')) # shape=(14, 15, 9)
output = relay.Tuple([uop_3910,])
output2 = relay.Tuple([uop_3912,])
func_3913 = relay.Function([], output)
mod['func_3913'] = func_3913
mod = relay.transform.InferType()(mod)
output = func_3913()
func_3914 = relay.Function([], output)
mutated_mod['func_3914'] = func_3914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3776_call = mod.get_global_var('func_3776')
func_3778_call = mutated_mod.get_global_var('func_3778')
call_3962 = relay.TupleGetItem(func_3776_call(), 0)
call_3963 = relay.TupleGetItem(func_3778_call(), 0)
func_2401_call = mod.get_global_var('func_2401')
func_2404_call = mutated_mod.get_global_var('func_2404')
var_3969 = relay.var("var_3969", dtype = "float64", shape = (96,))#candidate|3969|(96,)|var|float64
const_3970 = relay.const(-3, dtype = "int32")#candidate|3970|()|const|int32
call_3968 = relay.TupleGetItem(func_2401_call(relay.reshape(var_3969.astype('float64'), [96, 1]), relay.reshape(const_3970.astype('int32'), []), ), 1)
call_3971 = relay.TupleGetItem(func_2404_call(relay.reshape(var_3969.astype('float64'), [96, 1]), relay.reshape(const_3970.astype('int32'), []), ), 1)
output = relay.Tuple([call_3962,call_3968,var_3969,const_3970,])
output2 = relay.Tuple([call_3963,call_3971,var_3969,const_3970,])
func_4011 = relay.Function([var_3969,], output)
mod['func_4011'] = func_4011
mod = relay.transform.InferType()(mod)
mutated_mod['func_4011'] = func_4011
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4012 = relay.var("var_4012", dtype = "float64", shape = (96,))#candidate|4012|(96,)|var|float64
func_4011_call = mutated_mod.get_global_var('func_4011')
call_4013 = func_4011_call(var_4012)
output = call_4013
func_4014 = relay.Function([var_4012], output)
mutated_mod['func_4014'] = func_4014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3776_call = mod.get_global_var('func_3776')
func_3778_call = mutated_mod.get_global_var('func_3778')
call_4050 = relay.TupleGetItem(func_3776_call(), 0)
call_4051 = relay.TupleGetItem(func_3778_call(), 0)
output = relay.Tuple([call_4050,])
output2 = relay.Tuple([call_4051,])
func_4053 = relay.Function([], output)
mod['func_4053'] = func_4053
mod = relay.transform.InferType()(mod)
output = func_4053()
func_4054 = relay.Function([], output)
mutated_mod['func_4054'] = func_4054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3913_call = mod.get_global_var('func_3913')
func_3914_call = mutated_mod.get_global_var('func_3914')
call_4118 = relay.TupleGetItem(func_3913_call(), 0)
call_4119 = relay.TupleGetItem(func_3914_call(), 0)
output = relay.Tuple([call_4118,])
output2 = relay.Tuple([call_4119,])
func_4139 = relay.Function([], output)
mod['func_4139'] = func_4139
mod = relay.transform.InferType()(mod)
mutated_mod['func_4139'] = func_4139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4139_call = mutated_mod.get_global_var('func_4139')
call_4140 = func_4139_call()
output = call_4140
func_4141 = relay.Function([], output)
mutated_mod['func_4141'] = func_4141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3703_call = mod.get_global_var('func_3703')
func_3704_call = mutated_mod.get_global_var('func_3704')
call_4150 = relay.TupleGetItem(func_3703_call(), 1)
call_4151 = relay.TupleGetItem(func_3704_call(), 1)
output = relay.Tuple([call_4150,])
output2 = relay.Tuple([call_4151,])
func_4167 = relay.Function([], output)
mod['func_4167'] = func_4167
mod = relay.transform.InferType()(mod)
mutated_mod['func_4167'] = func_4167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4167_call = mutated_mod.get_global_var('func_4167')
call_4168 = func_4167_call()
output = call_4168
func_4169 = relay.Function([], output)
mutated_mod['func_4169'] = func_4169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4167_call = mod.get_global_var('func_4167')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_4292 = relay.TupleGetItem(func_4167_call(), 0)
call_4293 = relay.TupleGetItem(func_4169_call(), 0)
func_2401_call = mod.get_global_var('func_2401')
func_2404_call = mutated_mod.get_global_var('func_2404')
const_4296 = relay.const([[-7.730016,-8.654729,5.164299,-4.473980,-7.894869,-0.168108,-1.325937,3.869133,-2.519742,0.813684,-7.861830,0.693731,-6.416045,8.360886,-4.715341,3.751655,5.590753,-5.893546,7.959941,-1.997858,-8.770121,7.331013,0.444878,-3.040319,-0.687013,-4.629336,0.651648,-2.221301,-0.589467,-3.429066,2.692780,-8.650533,-0.209211,4.917762,8.561444,2.803583,6.228292,4.624369,-2.829159,-6.651374,9.194055,6.108298,-5.360145,7.521160,-1.830904,4.095222,7.125241,-4.736556,-0.652742,5.865166,7.580720,6.351605,-7.774056,8.699170,-8.482297,2.525183,-1.145382,2.962090,-6.148213,-0.731392,-4.132211,-9.418234,6.309224,8.522716,2.076848,5.478592,-2.253266,8.279550,6.176704,6.467142,-0.008493,-0.953962,9.583946,8.885919,-2.953540,-7.706680,-3.439698,-0.849198,1.994810,9.675425,-1.950969,1.908472,-7.286692,5.631152,8.908995,3.365343,-3.314269,7.393075,2.364887,5.538074,-2.488867,4.037282,0.022665,-9.903353,6.015871,1.521838]], dtype = "float64")#candidate|4296|(1, 96)|const|float64
var_4297 = relay.var("var_4297", dtype = "int32", shape = ())#candidate|4297|()|var|int32
call_4295 = relay.TupleGetItem(func_2401_call(relay.reshape(const_4296.astype('float64'), [96, 1]), relay.reshape(var_4297.astype('int32'), []), ), 2)
call_4298 = relay.TupleGetItem(func_2404_call(relay.reshape(const_4296.astype('float64'), [96, 1]), relay.reshape(var_4297.astype('int32'), []), ), 2)
output = relay.Tuple([call_4292,call_4295,const_4296,var_4297,])
output2 = relay.Tuple([call_4293,call_4298,const_4296,var_4297,])
func_4301 = relay.Function([var_4297,], output)
mod['func_4301'] = func_4301
mod = relay.transform.InferType()(mod)
mutated_mod['func_4301'] = func_4301
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4302 = relay.var("var_4302", dtype = "int32", shape = ())#candidate|4302|()|var|int32
func_4301_call = mutated_mod.get_global_var('func_4301')
call_4303 = func_4301_call(var_4302)
output = call_4303
func_4304 = relay.Function([var_4302], output)
mutated_mod['func_4304'] = func_4304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4053_call = mod.get_global_var('func_4053')
func_4054_call = mutated_mod.get_global_var('func_4054')
call_4407 = relay.TupleGetItem(func_4053_call(), 0)
call_4408 = relay.TupleGetItem(func_4054_call(), 0)
func_2998_call = mod.get_global_var('func_2998')
func_3001_call = mutated_mod.get_global_var('func_3001')
var_4420 = relay.var("var_4420", dtype = "int16", shape = ())#candidate|4420|()|var|int16
var_4421 = relay.var("var_4421", dtype = "int16", shape = (2912,))#candidate|4421|(2912,)|var|int16
call_4419 = relay.TupleGetItem(func_2998_call(relay.reshape(var_4420.astype('int16'), []), relay.reshape(var_4421.astype('int16'), [13, 14, 16]), ), 0)
call_4422 = relay.TupleGetItem(func_3001_call(relay.reshape(var_4420.astype('int16'), []), relay.reshape(var_4421.astype('int16'), [13, 14, 16]), ), 0)
output = relay.Tuple([call_4407,call_4419,var_4420,var_4421,])
output2 = relay.Tuple([call_4408,call_4422,var_4420,var_4421,])
func_4429 = relay.Function([var_4420,var_4421,], output)
mod['func_4429'] = func_4429
mod = relay.transform.InferType()(mod)
var_4430 = relay.var("var_4430", dtype = "int16", shape = ())#candidate|4430|()|var|int16
var_4431 = relay.var("var_4431", dtype = "int16", shape = (2912,))#candidate|4431|(2912,)|var|int16
output = func_4429(var_4430,var_4431,)
func_4432 = relay.Function([var_4430,var_4431,], output)
mutated_mod['func_4432'] = func_4432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4167_call = mod.get_global_var('func_4167')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_4535 = relay.TupleGetItem(func_4167_call(), 0)
call_4536 = relay.TupleGetItem(func_4169_call(), 0)
const_4537 = relay.const([[[-7.910726,-4.219463,8.467529,1.091593,0.692530,-1.084314,-7.482653,-1.279450,6.633825],[-1.330643,-6.227054,-6.105016,7.060770,3.820457,4.051254,-9.128975,-7.824868,-8.877153],[9.970069,8.898922,0.583895,0.041449,-8.672647,-0.300199,-3.993260,7.809357,-2.742407],[2.689859,7.634526,-4.339303,7.721127,-0.806791,4.480612,-9.837078,-2.492683,-5.452541],[6.976723,-8.306712,8.359972,-5.059334,7.606241,-5.700718,6.174128,1.079848,7.581087],[8.272931,5.578042,-9.832713,-6.071071,8.548705,0.744312,-1.815179,3.687711,-4.338354],[-8.599309,8.455336,-0.749063,6.353815,2.761255,-6.410433,-7.070831,-2.806981,-8.684110],[8.908434,8.237418,9.071190,-3.829472,8.485761,-1.443672,-2.909197,-1.442536,-3.999143],[-7.515582,-2.434197,5.159544,-8.966726,-9.487637,1.831655,4.774396,9.388341,2.800509],[1.582845,9.529385,6.453269,9.562441,-0.468321,2.682603,-7.998554,-1.756381,-5.054122],[-8.616973,5.655752,7.702678,0.196133,1.303547,3.865536,4.351906,-0.138269,6.617710],[3.043453,-5.219453,4.253886,-3.604942,3.800225,-4.253930,-6.272883,-4.139431,-8.670626],[-4.004328,-8.736772,-3.488294,-8.750655,5.908167,-9.860343,2.078910,0.124407,4.865660],[6.794680,-9.616972,-7.435160,-2.212747,5.234697,8.874783,-5.458865,2.226149,5.896109],[-9.765918,-1.063800,3.683281,4.616931,-8.656756,-1.315837,8.819744,3.698404,-3.805983]],[[-3.615641,9.609550,9.580538,5.440249,-2.399863,-1.605925,7.436223,-3.572996,-8.660799],[-7.595715,-4.519024,-8.069514,3.197406,-5.391407,-3.798578,-9.171642,-3.475040,-0.732122],[-8.176781,3.709488,9.527004,5.629084,9.730348,-8.565917,9.199268,2.693205,9.286436],[-5.259679,0.334412,7.694586,6.755829,-3.936055,3.338334,9.381714,8.245637,2.235038],[-2.482191,6.229307,-8.844510,-2.671668,-8.767085,7.009158,9.956396,-0.087765,-0.348293],[-6.775857,-8.607872,2.197101,-6.644878,4.786994,-0.242999,-9.542939,5.053031,-2.021040],[7.083089,7.412352,-5.756982,9.634464,-1.662579,-8.031041,9.207295,-1.222345,3.319331],[-7.559034,-8.425791,9.576216,-7.806885,-5.295928,7.001463,2.690093,6.523511,5.151865],[9.618808,8.881269,-1.905059,-8.676452,9.415303,9.239307,9.039171,-3.239544,-5.573399],[-2.188925,7.612823,-3.831921,8.483150,3.711944,6.456790,-7.359355,4.963461,-5.906460],[9.758761,0.338431,-6.813183,2.668320,-7.667225,2.275585,-4.008844,4.452863,-9.327715],[-3.739675,1.536736,-8.195875,-8.413128,0.882399,6.765013,-5.160856,3.243623,7.506765],[-2.614332,2.570479,-2.251812,4.210638,-7.848887,-5.931573,4.563630,-0.604454,-9.098471],[4.729148,0.979744,-8.514145,-8.728190,4.754518,-7.576653,4.788357,5.197111,-1.905738],[-3.800152,-7.961731,-8.467048,9.078957,-6.546691,1.648395,6.138523,8.663931,5.496394]],[[6.948224,-0.721061,1.933318,1.624385,-8.323180,6.477061,-1.582260,-7.976635,-6.082154],[7.144395,-0.916303,0.761055,-8.504292,-8.997629,9.927666,0.516353,-3.896093,8.478816],[-4.976265,-7.706473,-6.166848,4.228929,5.904006,2.662225,1.649172,-6.671736,-7.518803],[1.563821,-3.338837,9.944534,2.886870,-4.821932,-2.281538,-5.109956,-4.136097,2.495511],[-8.141595,2.360999,1.877627,-4.346778,6.464224,-3.372872,-4.802682,-9.004165,-5.292875],[2.891884,-3.314429,2.478993,6.058628,8.462802,-3.929937,-0.580826,-9.820899,2.550407],[4.964840,-9.583877,-5.382452,-6.277467,-8.090946,2.531771,-4.827518,-5.907707,-6.726649],[-2.340722,7.114277,7.574689,-5.336330,8.471533,7.415579,-2.281835,-0.693084,8.009987],[-2.203628,5.493604,-0.420154,7.308582,7.756130,4.024657,2.608173,-0.134889,2.935750],[-7.367954,1.331692,-1.708940,-5.089868,2.113640,8.328657,9.751013,6.950222,-7.701201],[9.724245,-4.400123,-1.698968,-5.264571,3.400093,-0.518907,-8.385195,3.616942,-6.195060],[-9.997698,-0.868889,9.021477,-4.982715,2.698364,-7.906468,9.379140,0.521776,-7.044830],[3.187329,0.610887,3.939313,-6.531400,4.120006,-2.494663,4.737657,-9.001415,-6.834750],[-9.244610,1.771416,-0.873177,2.611234,4.688219,-0.756226,-3.138913,8.962614,-9.288152],[-4.821600,-4.333352,-0.569102,6.757616,-5.089108,-9.214616,-2.390836,6.962210,-5.324091]],[[0.010970,-0.143563,7.347240,-7.061788,-9.550998,9.215747,0.121451,1.079926,7.486052],[-7.650247,-6.050417,8.415505,7.568044,6.466805,7.336151,6.607952,1.282305,2.265635],[-8.060065,1.087502,9.509183,2.961318,-1.563212,2.278717,3.165448,-0.822047,-2.171232],[-0.385783,8.971858,-2.689104,5.085529,8.392257,2.312954,2.890071,9.703314,9.639400],[-7.080851,9.079687,9.311374,-3.399014,-7.215137,-9.671472,-8.817597,-6.038518,-6.334517],[-8.876695,-2.723143,7.013571,4.257191,7.256220,9.106361,0.965242,-2.087449,-9.772201],[8.346819,-7.654758,7.335541,-4.737456,5.789429,-2.750870,-2.136427,6.655367,-6.383580],[-0.924510,-8.799146,-6.179809,-7.222036,6.422203,-5.935096,6.193734,-4.343972,4.390533],[-3.777271,-3.153359,1.684116,-4.772853,7.317996,-9.054754,-7.424140,0.675054,9.156860],[-3.668660,-7.592049,-1.589617,7.553833,-5.880931,6.628995,2.700761,-0.400662,9.649404],[-0.571921,1.402258,5.770020,-5.408016,-3.661614,-5.588651,1.214778,-2.842196,-8.693207],[7.179113,-4.884488,-3.967762,7.597219,9.772826,5.196597,1.847655,-6.638282,7.931638],[9.685030,1.119635,-1.871401,8.763406,-0.462450,0.527622,-1.934966,-1.651702,-9.152573],[-5.047210,0.993133,0.182938,-4.494745,-3.410987,9.237579,-0.383011,6.310263,8.574680],[-0.788897,-9.486407,-4.528373,8.905320,-7.124003,9.034806,-2.520475,-9.302861,8.700746]],[[-8.863043,0.964332,9.088360,7.167164,3.753404,0.815864,-9.630791,9.348830,4.514976],[-8.611446,-3.681050,-2.183109,5.911032,8.712431,-5.784829,-7.831770,-2.024477,-3.480533],[-8.403593,5.171028,-3.359543,-0.808795,-8.490875,7.072934,6.650432,1.144284,-6.004990],[9.486011,-3.158261,-1.436316,-8.574169,-0.496352,-4.220825,-6.748826,-6.748787,-5.434562],[-0.553960,7.237572,-4.062057,-7.514357,-3.238139,3.976825,-6.299726,-2.007573,5.336092],[7.707599,9.911926,-9.581469,-8.859101,0.056692,-4.991821,-9.928946,-7.464165,-5.006980],[-7.315473,3.694465,-3.677072,-6.369541,7.695475,4.922157,2.386205,-6.621381,-5.861554],[-0.578929,6.321765,7.671052,0.800833,1.846136,2.358246,-8.844161,-8.302239,-5.474153],[-6.636484,7.766491,-5.246830,-5.986168,-4.527599,-3.053387,2.374108,1.250848,-1.794005],[-9.598537,-8.267606,-0.321107,4.255512,-4.397788,-2.426245,-0.563367,1.702533,-0.397571],[3.717381,4.501523,-4.877941,-5.960881,-2.125571,-3.852847,1.536449,-0.925747,-6.614794],[4.268986,4.396396,-3.690049,8.896402,-1.814325,-4.765142,-0.191911,0.209849,8.548986],[8.106362,8.583338,-8.688719,0.282669,-6.413498,0.558242,-7.534281,7.954159,-2.316561],[9.834801,-9.350553,-2.781235,-4.440131,-1.096077,-5.167123,8.312998,-5.935744,3.535638],[8.770904,-5.734076,-2.155679,-6.840565,-4.980796,-2.083420,7.771403,-0.916069,4.422220]],[[6.435155,8.989666,5.639193,2.366546,-2.346214,0.821084,-5.722668,-2.979161,3.822109],[7.271847,5.613343,4.260397,-2.459338,1.929766,-6.057252,-7.231198,-4.474532,-5.031828],[4.404867,0.145640,8.628294,-3.451244,4.069418,-6.771048,9.143125,-1.559389,3.750137],[0.117296,6.234874,5.574773,8.367899,1.735215,6.190060,-2.007881,0.251129,-9.113381],[-7.303619,3.727328,2.817286,-8.667694,9.041164,3.560761,-8.169142,-5.748311,6.058358],[-2.818273,2.540912,6.731615,5.231276,-8.844899,8.295934,0.262953,3.906449,4.294332],[-2.513487,0.328916,-7.063006,-0.547011,7.323069,-0.095595,-4.949371,-3.843726,-9.056830],[4.294268,0.110160,8.596571,-9.305045,-4.060228,7.542225,3.363643,-6.765444,1.432539],[1.858875,2.947565,-0.029619,-7.317012,-7.725039,1.995982,-9.657145,-1.934358,-4.319293],[-5.629693,-0.183286,-8.954249,-4.007350,9.289030,-1.051760,8.625446,5.106831,0.055656],[3.913467,-7.116957,-5.286901,-2.265945,-4.797254,-4.170476,-5.573525,-4.289996,8.673431],[-5.087140,-4.290703,-5.839813,-7.217719,-4.997558,7.586925,-7.917473,1.151528,-1.218247],[-6.595408,-7.806914,-2.251080,8.602849,0.265995,0.272962,-0.634564,-7.601057,-6.214318],[3.023964,4.082845,-3.455632,0.510301,8.034830,4.405197,-8.738573,-8.636144,6.592787],[3.746335,-9.806863,-6.879549,-1.404313,4.257116,5.090403,7.657943,6.860940,-7.033851]],[[5.032864,-3.376169,7.319509,1.967359,8.825388,-7.172112,-0.954660,7.403727,2.042475],[-8.549446,-2.758031,-5.187368,4.361283,-5.347835,-7.701619,-9.254079,3.907482,-0.156233],[3.084457,-6.076686,-8.109725,6.247292,1.017204,6.530086,-7.227809,-5.893595,2.581976],[-1.603613,-7.255035,2.868829,4.723955,0.060391,-6.017248,9.423741,4.734831,-3.202207],[4.151195,-9.737217,-6.621663,1.091808,1.957715,1.808073,-1.544377,-5.174123,6.465164],[-2.262889,3.180441,5.714653,6.775518,2.885106,-9.439305,-7.355514,2.519710,-9.681904],[-8.975591,-0.799279,4.660725,8.643443,5.021613,4.145546,4.483893,-4.125552,2.914857],[3.277980,-3.934411,8.734958,-7.014532,-7.682794,-8.539069,-8.540849,-3.039901,-1.180355],[-6.222935,-1.933209,8.768051,-3.066230,1.470955,-6.828093,-4.585023,0.263954,-7.980528],[-5.422660,1.950620,5.984578,0.043114,-3.802040,-7.857222,-5.810188,-2.992077,3.407452],[-5.813177,1.788635,-9.554216,-4.341596,0.357821,9.715093,-8.058127,-3.851655,1.838982],[4.252300,2.174166,-7.471607,-1.916457,5.900843,1.706066,5.397469,-7.246551,3.371012],[-8.420294,-7.108118,-7.861777,0.605287,6.857225,-4.061860,7.246734,7.043414,7.658836],[0.868178,-5.095486,0.968291,7.126312,7.121062,0.281070,-5.754862,-1.607478,1.353205],[-0.126325,0.744484,-9.293388,-4.671614,3.956789,1.609210,-8.440048,9.896950,8.598173]],[[-0.470176,4.644839,-7.815218,7.034707,-6.429778,9.043590,-8.963493,-4.007732,2.652163],[6.720096,0.030851,-1.880605,9.776765,8.061915,1.825766,9.571872,3.937256,-6.448386],[1.963743,-5.318834,5.994903,5.128968,1.980434,-8.450759,6.233309,9.975436,-2.456729],[4.126133,-3.522525,-1.367890,1.172434,1.029467,-1.820430,-5.025783,8.492725,1.151461],[5.186423,-3.235226,2.295744,5.207627,-8.270888,5.181432,-4.797313,7.336236,2.815884],[3.525264,8.744324,9.752156,-4.021203,-8.663969,-4.669552,-5.681250,-9.695593,-5.883784],[2.532234,-2.871476,-9.680076,6.181132,-5.427978,7.279625,-3.607338,-7.655687,-3.412523],[-9.335241,-3.037004,-9.796505,-5.328507,-1.047303,-8.019346,-0.267880,-6.531034,6.243635],[-2.988443,-8.155214,4.082552,-0.064170,-3.465386,-9.645849,-0.468111,2.460888,3.598771],[4.720030,-8.135894,-9.112798,6.283086,0.210409,-4.391415,-5.518523,2.366709,8.647211],[7.197234,-1.438989,7.326516,-6.561187,4.163166,-9.372410,8.988645,7.449669,3.317721],[-6.134066,-5.171090,-2.422563,7.341235,-7.326717,2.274887,6.012151,6.166374,-4.715976],[-2.392531,8.155925,-5.928190,-2.137479,6.753816,-0.501982,-0.894977,1.551123,-2.261135],[8.595778,0.471579,-9.317790,8.390020,1.138999,9.514371,3.585111,-9.937519,-4.078171],[-4.408363,-2.584042,-0.182730,-2.617972,-6.130141,8.299333,-3.686897,-6.222383,-7.588044]],[[-3.086388,-2.725994,0.369612,-2.715524,-2.259791,6.733920,2.199326,6.920823,7.773406],[-1.038882,-3.452895,-9.982316,8.572674,-8.626106,-2.625277,-0.446945,3.617960,-6.386542],[0.770861,4.826334,8.356736,-5.977402,5.398254,-1.655105,1.095622,-5.334196,5.178143],[9.632427,5.967534,-9.487924,2.924674,3.034021,-5.111259,6.455904,-3.816790,3.226686],[6.138761,-0.044307,0.008217,5.434153,-5.026461,7.071966,-4.169026,-7.824040,-5.868555],[1.646080,-1.199473,-3.708626,-4.841921,-7.415672,0.326012,-8.455298,4.753229,3.699162],[-1.371049,7.165998,-0.179592,-7.215890,2.063715,6.709218,-6.294307,0.876566,5.569733],[5.360652,0.603066,-5.222262,2.761256,7.441149,8.245955,8.286733,-1.114714,-6.074454],[9.862194,9.839012,-6.371618,7.101819,-6.616109,3.112365,-5.129831,5.984690,-8.857947],[-6.959012,8.419280,-0.072732,-3.546071,-2.267143,-2.958346,-0.062688,3.932165,-3.697383],[-4.642090,-9.865324,2.374501,-8.950697,-6.552752,5.148639,7.851922,-4.157517,-2.784751],[9.446286,9.953098,1.851695,1.655707,4.780763,4.328619,-4.377788,6.882692,-5.974153],[-2.589358,4.342031,5.175183,5.032922,-0.911235,3.979234,-2.756159,-8.280164,-6.583769],[1.654693,5.167782,-6.989853,-8.669091,-8.634491,-8.241697,-7.743764,6.038406,8.804345],[5.997992,9.283219,5.458923,-4.272633,7.427813,3.975903,-1.772726,2.091459,6.924307]],[[-9.376572,-4.340686,-7.533484,-7.475588,9.523252,-9.996540,-2.259463,0.262074,7.860421],[-1.513032,-6.033302,-5.950000,9.607616,-7.575093,-1.418973,-5.597468,-4.297703,4.223424],[3.676462,6.761835,3.009193,-9.115691,0.373244,2.068593,-4.017222,-0.577995,-2.900369],[-6.849900,6.724998,-1.675372,-3.220349,1.487446,-8.913313,0.256390,-6.139235,-6.835434],[-0.372245,4.846861,2.623053,6.696876,-2.504297,-9.847445,-6.650730,-7.143826,-1.635532],[-8.085117,1.052872,4.571755,-9.653558,-2.392709,7.765685,8.997661,1.732915,-2.203528],[0.466780,-8.238122,9.858183,-9.904848,3.981088,-7.290260,-2.626709,-8.846109,-6.264356],[3.286305,6.634524,3.049609,-7.486244,-4.069134,0.677137,-0.585625,-3.110338,-3.970378],[-8.352457,-9.494575,7.356917,1.080386,8.617331,0.795901,4.248958,-9.726301,-3.301233],[3.599197,-7.074713,-7.606549,-7.005990,6.941988,7.483627,0.782528,-5.587268,4.953821],[-9.494133,9.425254,8.663642,9.093169,1.606853,5.943093,9.943169,8.119866,-3.576218],[6.475767,-1.670008,-9.794726,-2.415979,4.059948,1.471928,-0.558579,8.416620,9.744577],[-9.117984,2.378730,-8.538834,-2.161589,-4.040788,-4.569161,3.581238,3.358465,-6.844776],[-5.400226,7.994450,2.694250,-8.456753,-0.910539,-8.932228,-6.322516,-3.493747,-2.662056],[-1.579660,-4.438187,-2.609106,-5.821546,-5.626707,-5.077946,2.787924,0.208081,-2.633430]],[[7.685930,-6.125225,2.893254,6.514114,-6.717640,0.744295,-4.523384,2.930280,-7.538565],[0.602650,1.692321,7.573269,-0.010078,-7.353763,8.234173,1.516313,-5.926067,6.260751],[-5.886328,9.922990,-8.041606,1.068931,4.325866,-6.055734,2.837020,-2.564129,6.419133],[-2.952251,-0.091944,-8.368742,5.367501,-0.422851,3.729161,9.547451,-3.987112,-4.134968],[-0.434949,5.340957,-3.471297,7.921839,-1.504728,6.696237,6.097171,6.093454,-5.447717],[-0.351671,9.611931,8.624477,-1.976586,-8.293968,-2.418100,0.358046,0.470474,-4.248146],[-5.682323,3.316529,3.057341,2.575643,-1.576481,-2.762265,-9.427229,-0.135960,6.550461],[-5.554531,8.315988,-8.121870,-9.879238,-5.462847,-5.828840,8.585195,-7.846722,4.962379],[1.696396,6.907095,-6.422456,0.787158,-5.992185,-9.970872,5.550464,2.543738,-6.789241],[-1.840148,6.069715,-3.065429,7.174591,8.663324,-9.505159,4.283739,9.558949,0.642203],[-2.757661,-2.122804,-9.767791,-7.062426,4.615488,-3.356004,8.394049,-8.740587,6.134020],[2.307917,9.647335,5.767738,8.024687,3.390583,9.168635,-8.978362,9.891506,-4.006088],[-4.664897,-4.663989,-3.388318,4.559495,1.203830,-4.653218,-0.987178,-2.655553,-7.865873],[5.895079,-8.008730,-9.115292,5.209921,-1.941332,1.564283,-0.239423,5.388449,-2.836166],[-8.545670,-3.543816,9.226007,-3.511921,-6.911605,4.157262,-0.368085,-2.709502,-6.990040]],[[-3.082136,-4.306127,-2.247472,7.274668,2.077723,6.019000,-1.051335,1.823784,-2.988478],[-1.537717,-8.627080,5.175659,2.964727,-9.659464,-4.051731,3.039158,-5.541832,4.640451],[4.551536,0.340342,-9.544329,-5.256236,-6.044198,2.290321,2.428307,-1.745147,-9.175762],[9.806398,2.173778,5.908916,-3.577609,9.816019,-5.196062,-3.610183,6.898335,-4.800996],[-4.328471,8.332438,-4.034256,7.294544,-9.355626,7.402902,3.295882,-4.805693,-7.263904],[8.193350,-6.393188,6.989935,3.160867,4.493251,-0.159254,-6.995932,-5.880988,1.655844],[-4.716414,-8.198107,-4.819593,5.294356,1.198937,7.066919,-4.420701,-9.075281,9.886441],[8.235147,5.326303,1.814846,2.476168,7.836952,2.925674,-3.491557,9.404460,-9.551020],[9.431058,-5.589313,-8.125232,-7.424555,-6.022884,3.291127,4.680156,-0.516513,8.171812],[-1.541540,-3.565801,0.201521,-2.250990,1.994950,-3.515027,-1.087068,-9.650689,-9.371889],[-7.824299,0.924476,-5.386660,-8.811547,8.606765,-9.212678,-4.677812,2.662434,-9.205176],[1.573989,6.280051,9.111413,-1.026036,6.043566,-4.698070,6.905412,-1.076995,8.250859],[-1.417385,-8.198180,-6.514145,-0.133415,8.279731,1.763722,-1.019197,7.814864,-2.936624],[-2.650330,-0.967368,6.200485,5.205363,4.334559,8.166778,-2.083673,-0.139368,9.746474],[-0.847068,0.550963,-1.647967,5.584112,7.250594,-8.292125,6.413447,9.506679,-1.288433]],[[-3.382721,1.200969,3.613084,-7.505437,-2.243064,8.560186,-0.009989,-6.717148,7.265305],[-0.330571,0.109726,4.071662,8.455951,-6.046987,-6.653817,4.919198,9.129468,-7.625841],[0.051018,-3.096195,5.326989,-4.751882,1.732064,-6.940224,1.385715,-1.748664,-7.008817],[-7.308413,-1.866438,-0.266708,9.020492,-4.079333,2.137699,4.460882,8.406593,-8.020177],[0.427284,-2.353949,5.147280,-4.545044,-1.788058,-5.836223,-5.320281,-0.556113,0.187392],[-9.313246,8.545738,7.345996,3.971073,0.722969,6.262820,-9.204038,-2.279291,7.275875],[8.576528,-0.530992,-1.942891,-8.034164,6.054805,-5.238797,-2.930008,3.601688,5.579521],[-9.072901,-9.782522,3.355672,3.194062,-3.116697,4.897231,-4.691808,1.465922,-4.722723],[9.324645,5.418675,1.823000,8.755991,-4.237175,8.293926,-1.510473,-7.663820,-9.406452],[-6.831907,0.505004,2.314184,-7.390904,8.719338,9.770269,-0.204062,0.581216,8.139633],[8.249446,-9.360811,-7.132289,3.980058,1.708687,9.337174,7.476409,7.454470,-2.608847],[6.269233,-2.053364,1.080549,-5.914983,-2.298164,3.564741,7.986435,4.214831,-3.174562],[4.583444,-4.506236,6.997929,-9.676022,9.938480,-8.559284,8.597167,-6.456921,-3.195867],[2.804111,5.344094,-8.632048,6.940909,2.848421,7.084298,-7.583154,1.649794,5.021464],[-4.208495,-7.044021,-5.931046,-8.662647,-9.423458,2.871832,-9.267508,-1.620097,4.112249]],[[-1.631982,-9.048898,9.287381,6.872147,-3.967490,-9.555685,4.297262,-0.264771,-3.123497],[-2.894933,-1.323459,3.088292,-3.224945,-8.292376,-4.301986,9.408837,-3.463341,-7.770108],[-5.050724,-3.178502,8.492533,-8.176131,8.772189,-8.709441,5.834829,-9.148652,0.699583],[-8.537172,2.029587,-4.734548,-2.927446,-3.979037,2.829628,-9.123913,-4.621549,0.129464],[9.099980,2.345533,-6.942745,-7.116579,-3.630073,6.938557,-2.110346,8.806673,-0.932757],[5.894095,-2.660593,1.758952,0.828186,6.887951,-7.082041,6.456990,-1.404002,5.058439],[-9.463412,6.421558,-4.955329,-5.347955,-3.075550,5.542634,-4.884655,1.610029,-4.420730],[-7.925711,-5.178531,-1.757570,-4.482511,-8.619866,-5.634460,6.204820,7.205938,8.117339],[2.104671,-3.767846,-4.731451,-8.229301,4.536748,0.536127,9.267484,9.064401,7.157132],[-2.315379,2.138941,-8.655675,-9.490647,-6.403545,-0.205994,-8.945650,0.006183,5.499856],[-7.364881,-7.962451,8.953323,7.780839,-0.711240,-1.624761,-2.157083,3.308936,0.696651],[7.677719,-8.984888,7.716157,-1.503877,-1.699250,1.209221,5.921414,-3.730930,5.114304],[9.007914,-3.929940,4.335145,1.150884,7.224711,4.247747,-5.752961,1.286540,-4.528458],[-4.072578,-7.417318,-4.716118,-1.482144,9.803453,-4.898224,2.929275,5.185299,6.356909],[-8.543464,8.279705,4.261615,1.710075,0.242458,-0.942138,3.426859,-6.128329,-1.237945]]], dtype = "float64")#candidate|4537|(14, 15, 9)|const|float64
bop_4538 = relay.logical_and(call_4535.astype('bool'), relay.reshape(const_4537.astype('bool'), relay.shape_of(call_4535))) # shape=(14, 15, 9)
bop_4541 = relay.logical_and(call_4536.astype('bool'), relay.reshape(const_4537.astype('bool'), relay.shape_of(call_4536))) # shape=(14, 15, 9)
func_2998_call = mod.get_global_var('func_2998')
func_3001_call = mutated_mod.get_global_var('func_3001')
const_4556 = relay.const(-10, dtype = "int16")#candidate|4556|()|const|int16
var_4557 = relay.var("var_4557", dtype = "int16", shape = (2912,))#candidate|4557|(2912,)|var|int16
call_4555 = relay.TupleGetItem(func_2998_call(relay.reshape(const_4556.astype('int16'), []), relay.reshape(var_4557.astype('int16'), [13, 14, 16]), ), 0)
call_4558 = relay.TupleGetItem(func_3001_call(relay.reshape(const_4556.astype('int16'), []), relay.reshape(var_4557.astype('int16'), [13, 14, 16]), ), 0)
func_3703_call = mod.get_global_var('func_3703')
func_3704_call = mutated_mod.get_global_var('func_3704')
call_4560 = relay.TupleGetItem(func_3703_call(), 1)
call_4561 = relay.TupleGetItem(func_3704_call(), 1)
func_1505_call = mod.get_global_var('func_1505')
func_1510_call = mutated_mod.get_global_var('func_1510')
const_4577 = relay.const([[-7.394357],[-6.457255],[-7.254264],[-7.743758],[4.608203],[-0.392652],[8.449046],[-4.719827],[-8.703726],[-8.451555],[-4.932160],[-1.104757],[1.128033],[-4.469260],[-7.938062],[2.580799],[-5.971098],[0.802836],[0.142270],[5.426421],[-1.704611],[1.914852],[9.833845],[-0.281273],[-8.206741],[-0.627321],[-9.233606],[9.849844],[-2.043658],[6.382545],[-4.529990],[6.468786],[-6.982852],[7.094727],[-7.407114],[0.532094],[2.824242],[2.918754],[-2.804783],[-3.174871],[-8.713211],[5.431228],[0.441581],[-3.022237],[-0.313524],[-3.302046],[-8.055684],[5.571037],[-9.713796],[7.797842],[-2.876168],[3.847648],[1.774806],[-0.412389],[-6.796042],[-6.301026],[7.857566],[4.892327],[5.743802],[-8.930416],[5.383419],[-5.136807],[-4.263352],[3.038050],[-0.902964],[-1.117286],[3.738270],[-5.201109],[-5.033731],[-2.785317],[8.479355],[2.476308],[-9.822149],[3.632121],[-9.451607],[8.917995],[-8.165310],[-0.232575],[-3.794974],[3.454704],[-3.509856],[9.398562],[-4.590519],[-1.480079],[-2.919184],[7.447996],[-3.417435],[-4.950666],[-3.676221],[-6.121743],[2.141140],[-8.009955],[9.118145],[-0.619697],[-0.625390],[-2.573001]], dtype = "float64")#candidate|4577|(96, 1)|const|float64
const_4578 = relay.const([True,True,False,True,True,True,False,True,False,True,False,True,False,True,True,True,False,False,True,True,True,False,False,True,False,False,False,True,False,True,True,True,False,True,False,False,True,False,True,True,False,True,False,False,False,True,True,False,True,False,False,False,True,False,True,True,True,True,False,True,False,True,False,True,True,False,True,False,True,False,True,True,True,True,True,True,False,False,True,True,False,True,True,True,False,False,False,True,True,True,False,False,False,False,True,True,False,False,True,True,False,False,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,True,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,False,False,True,False,True,False,False,True,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,True,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False,True,True,True,False,False,False,False,True,False,True,False,False,True,False,False,False,True,True,True,True,True,True,True,False,False,True,False,True,True,True,False,False,False,True,False,True,False,True,False,False,False,False,False,True,False,True,False,False,False,True,True,False,False,False,False,True,True,False,False,False,False,False,True,False,False,True,True,False,False,True,False,False,False,True,False,False,False,False,False,False,True,True,False,False,False,False,True,True,True,True,False,True,False,True,True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,True,False,True,True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,False,True,True,True,False,False,False,False,True,False,True,True,True,True,True,False,False,True,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,True,False,True,True,True,False,True,True,True,False,False,False,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,True,False,True,False,True,True,True,False,False,False,False,True,False,False,False,False,True,True,True,False,False,True,False,True,False,False,False,True,True,False,False,False,False,True,True,True,True,False,True,True,False,False,False,False,False,False,True,True,False,False,True,False,True,True,False,False,False,False,True,True,False,True,True,False,True,False,True,False,False,True,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,False,False,True,True,True,True,True,True,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,False,False,True,True,True,True,False,False,False,True,False,True,False,False,True,True,False,False,False,True,True,True,True,True,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,True,True,False,True,False,False,True,False,False,True,True,True,False,True,False,True,True,True,True,False,False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,False,False,False,False,False,True,False,True,True,True,False,True,False,True,False,False,False,True,True,True,True,True,True,True,True,False,True,False,True,True,True,True,True,True,False,True,False,False,False,False,True,False,True,True,False,True,True,False,False,False,True,True,True,True,True,False,True,False,True,False,True,False,False,False,False,False,True,False,False,True,False,True,False,True,False,False,False,True,False,True,False,True,False,True,False,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,False,False,False,True,False,True,False,True,False,True,True,False,False,True,True,True,True,False,False,True,False,True,False,True,False,True,False,True,True,True,True,True,False,False,False,False,True,True,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,False,False,True,False,False,True,True,False,False,False,False,False,False,False,True,True,False,True,False,False,False,True,False,True,True,True,True,False,True,False,True,False,False,True,False,True,False,True,True,False,True,True,True,True,True,False,True,True,True,True,False,False,False,False,True,True,False,False,True,True,True,True,True,True,False,True,False,False,False,True,False,True,False,True,True,False,False,False,True,True,True,True,True,True,False,False,False,False,True,False,True,False,True,True,True,True,False,False,True,True,True,True,False,False,True,True,False,True,True,True,False,False,True,False,True,True,False,False,True,True,False,False,True,True,True,True,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,False,True,True,True,True,False,False,False,True,True,False,False,False,True,True,False,True,False,True,False,True,True,True,False,True,False,True,False,True,False,True,True,True,False,True,False,False,True,False,True,False,False,True,False,True,False,True,False,True,False,False,False,True,False,False,False,False,False,True,False,False,False,True,True,False,False,True,False,False,False,False,False,False,True,True,False,False,False,False,True,False,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,True,False,True,False,True,False,True,True,False,True,True,True,False,True,False,True,False,True,True,True,True,False,True,False,False,False,True,True,True,False,False,True,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,True,False,True,False,True,True,True,True,False,False,True,True,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,True,False,True,False,True,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,True,False,True,False,False,True,True,False,True,True,False,False,True,True,False,False,False,True,False,False,True,True,True,False,True,False,True,False,True,True,False,False,True,True,True,False,True,False,False,False,True,False,False,False,False,False,False,False,True,False,False,False,True,False,True,True,False,False,True,True,True,True,False,True,True,True,True,False,True,True,False,False,False,False,False,False,False,False,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,True,True,True,False,False,True,False,False,True,False,False,True,True,True,False,False,False,False,False,True,True,False,False,True,False,False,False,False,True,False,True,False,True,False,True,True,True,True,False], dtype = "bool")#candidate|4578|(1248,)|const|bool
call_4576 = relay.TupleGetItem(func_1505_call(relay.reshape(const_4577.astype('float64'), [1, 8, 12]), relay.reshape(const_4578.astype('bool'), [1248,]), relay.reshape(const_4556.astype('int32'), []), ), 6)
call_4579 = relay.TupleGetItem(func_1510_call(relay.reshape(const_4577.astype('float64'), [1, 8, 12]), relay.reshape(const_4578.astype('bool'), [1248,]), relay.reshape(const_4556.astype('int32'), []), ), 6)
bop_4580 = relay.less(call_4555.astype('bool'), const_4556.astype('bool')) # shape=(13, 14, 16)
bop_4583 = relay.less(call_4558.astype('bool'), const_4556.astype('bool')) # shape=(13, 14, 16)
uop_4588 = relay.sigmoid(call_4535.astype('float64')) # shape=(14, 15, 9)
uop_4590 = relay.sigmoid(call_4536.astype('float64')) # shape=(14, 15, 9)
output = relay.Tuple([bop_4538,var_4557,call_4560,call_4576,const_4577,const_4578,bop_4580,uop_4588,])
output2 = relay.Tuple([bop_4541,var_4557,call_4561,call_4579,const_4577,const_4578,bop_4583,uop_4590,])
func_4593 = relay.Function([var_4557,], output)
mod['func_4593'] = func_4593
mod = relay.transform.InferType()(mod)
mutated_mod['func_4593'] = func_4593
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4594 = relay.var("var_4594", dtype = "int16", shape = (2912,))#candidate|4594|(2912,)|var|int16
func_4593_call = mutated_mod.get_global_var('func_4593')
call_4595 = func_4593_call(var_4594)
output = call_4595
func_4596 = relay.Function([var_4594], output)
mutated_mod['func_4596'] = func_4596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4053_call = mod.get_global_var('func_4053')
func_4054_call = mutated_mod.get_global_var('func_4054')
call_4617 = relay.TupleGetItem(func_4053_call(), 0)
call_4618 = relay.TupleGetItem(func_4054_call(), 0)
output = call_4617
output2 = call_4618
func_4620 = relay.Function([], output)
mod['func_4620'] = func_4620
mod = relay.transform.InferType()(mod)
output = func_4620()
func_4621 = relay.Function([], output)
mutated_mod['func_4621'] = func_4621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4053_call = mod.get_global_var('func_4053')
func_4054_call = mutated_mod.get_global_var('func_4054')
call_4665 = relay.TupleGetItem(func_4053_call(), 0)
call_4666 = relay.TupleGetItem(func_4054_call(), 0)
func_2615_call = mod.get_global_var('func_2615')
func_2617_call = mutated_mod.get_global_var('func_2617')
const_4680 = relay.const([-2.992064,-5.580711,-6.592245,2.980292,-1.825373,8.624026,3.630211,-8.714353,8.648722,7.783509,-1.917777,6.602231,-1.862134,6.678172,3.440317,1.130786,6.586887,-8.172862,7.214173,-8.783903,0.794994,8.279792,6.027286,3.651553,9.395793,6.723700,0.507715,-6.273596,6.859916,5.468263,3.524527,0.775099,-7.084252,9.077310,8.516426,5.480835,6.167719,5.893936,-1.213150,8.416161,-3.783071,0.058666,3.325835,8.616593], dtype = "float32")#candidate|4680|(44,)|const|float32
call_4679 = relay.TupleGetItem(func_2615_call(relay.reshape(const_4680.astype('float32'), [1, 11, 4])), 0)
call_4681 = relay.TupleGetItem(func_2617_call(relay.reshape(const_4680.astype('float32'), [1, 11, 4])), 0)
output = relay.Tuple([call_4665,call_4679,const_4680,])
output2 = relay.Tuple([call_4666,call_4681,const_4680,])
func_4689 = relay.Function([], output)
mod['func_4689'] = func_4689
mod = relay.transform.InferType()(mod)
output = func_4689()
func_4690 = relay.Function([], output)
mutated_mod['func_4690'] = func_4690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4167_call = mod.get_global_var('func_4167')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_4718 = relay.TupleGetItem(func_4167_call(), 0)
call_4719 = relay.TupleGetItem(func_4169_call(), 0)
output = relay.Tuple([call_4718,])
output2 = relay.Tuple([call_4719,])
func_4726 = relay.Function([], output)
mod['func_4726'] = func_4726
mod = relay.transform.InferType()(mod)
output = func_4726()
func_4727 = relay.Function([], output)
mutated_mod['func_4727'] = func_4727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3703_call = mod.get_global_var('func_3703')
func_3704_call = mutated_mod.get_global_var('func_3704')
call_4758 = relay.TupleGetItem(func_3703_call(), 0)
call_4759 = relay.TupleGetItem(func_3704_call(), 0)
func_2216_call = mod.get_global_var('func_2216')
func_2219_call = mutated_mod.get_global_var('func_2219')
const_4761 = relay.const(-3.032111, dtype = "float32")#candidate|4761|()|const|float32
var_4762 = relay.var("var_4762", dtype = "float32", shape = (3120,))#candidate|4762|(3120,)|var|float32
call_4760 = relay.TupleGetItem(func_2216_call(relay.reshape(const_4761.astype('float32'), []), relay.reshape(var_4762.astype('float32'), [13, 16, 15]), ), 0)
call_4763 = relay.TupleGetItem(func_2219_call(relay.reshape(const_4761.astype('float32'), []), relay.reshape(var_4762.astype('float32'), [13, 16, 15]), ), 0)
uop_4775 = relay.log2(var_4762.astype('float64')) # shape=(3120,)
output = relay.Tuple([call_4758,call_4760,const_4761,uop_4775,])
output2 = relay.Tuple([call_4759,call_4763,const_4761,uop_4775,])
func_4784 = relay.Function([var_4762,], output)
mod['func_4784'] = func_4784
mod = relay.transform.InferType()(mod)
mutated_mod['func_4784'] = func_4784
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4785 = relay.var("var_4785", dtype = "float32", shape = (3120,))#candidate|4785|(3120,)|var|float32
func_4784_call = mutated_mod.get_global_var('func_4784')
call_4786 = func_4784_call(var_4785)
output = call_4786
func_4787 = relay.Function([var_4785], output)
mutated_mod['func_4787'] = func_4787
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4795 = relay.var("var_4795", dtype = "float32", shape = ())#candidate|4795|()|var|float32
var_4796 = relay.var("var_4796", dtype = "float32", shape = (13, 14, 3))#candidate|4796|(13, 14, 3)|var|float32
bop_4797 = relay.mod(var_4795.astype('float32'), var_4796.astype('float32')) # shape=(13, 14, 3)
output = relay.Tuple([bop_4797,])
output2 = relay.Tuple([bop_4797,])
func_4806 = relay.Function([var_4795,var_4796,], output)
mod['func_4806'] = func_4806
mod = relay.transform.InferType()(mod)
mutated_mod['func_4806'] = func_4806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4806_call = mutated_mod.get_global_var('func_4806')
var_4808 = relay.var("var_4808", dtype = "float32", shape = ())#candidate|4808|()|var|float32
var_4809 = relay.var("var_4809", dtype = "float32", shape = (13, 14, 3))#candidate|4809|(13, 14, 3)|var|float32
call_4807 = func_4806_call(var_4808,var_4809,)
output = call_4807
func_4810 = relay.Function([var_4808,var_4809,], output)
mutated_mod['func_4810'] = func_4810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3880_call = mod.get_global_var('func_3880')
func_3881_call = mutated_mod.get_global_var('func_3881')
call_4877 = relay.TupleGetItem(func_3880_call(), 0)
call_4878 = relay.TupleGetItem(func_3881_call(), 0)
uop_4886 = relay.sqrt(call_4877.astype('float32')) # shape=(14, 15, 9)
uop_4888 = relay.sqrt(call_4878.astype('float32')) # shape=(14, 15, 9)
func_2216_call = mod.get_global_var('func_2216')
func_2219_call = mutated_mod.get_global_var('func_2219')
var_4891 = relay.var("var_4891", dtype = "float32", shape = ())#candidate|4891|()|var|float32
const_4892 = relay.const([-7.294573,8.333438,6.818425,-6.892508,9.784849,0.632165,-3.144375,9.778646,8.616676,4.381249,-6.523401,-6.554206,-6.110984,-3.047156,9.377095,-7.133093,5.844895,-8.148080,-7.994992,-2.941281,-0.487312,-4.877635,6.837752,7.829518,-9.262173,-3.754572,8.196650,-1.857552,7.613595,6.714367,-1.901704,-8.942236,1.539734,5.059004,2.247364,1.798146,5.029817,-2.533381,-1.702252,3.362832,8.345498,5.548385,-7.742666,-2.287868,-0.137192,-7.321006,0.885722,5.088895,-0.474809,-5.283285,-6.237843,5.764893,-8.579777,-9.327095,-6.769630,2.369330,-9.470628,-8.697197,1.544251,-9.585566,5.060211,-0.263194,-4.077731,8.605156,-5.610006,-9.248353,-5.883312,8.606119,-6.173799,9.954661,3.309188,-4.256117,4.462814,6.698881,5.200857,4.666898,-8.398811,5.102614,8.330872,7.901372,-8.965662,-3.604740,-1.731251,1.148798,-5.315836,5.226688,-8.416030,8.391210,-1.206165,-9.146123,-3.803148,-4.084436,7.344181,2.312635,5.716280,8.728007,1.589891,-3.426512,8.461390,-5.765643,-4.890390,4.348611,7.976113,-1.037193,5.508257,6.063589,-6.829820,0.402171,3.864372,-0.726511,9.258051,-7.735267,-3.793520,-5.064333,3.770311,7.467641,-3.494377,-7.235822,4.717311,-1.913377,0.557223,-7.811879,1.630444,5.162825,1.144077,4.304614,2.513508,7.039244,-5.673933,0.203280,-1.743340,9.498019,-6.846910,-4.089121,3.108005,-9.008689,-8.668964,-4.468679,-4.614819,-8.617379,-4.682462,7.613826,4.846166,8.833707,-9.271508,0.259294,5.369073,-7.070804,-9.849861,0.210669,1.217325,-0.730606,-4.423798,5.349519,6.619623,-4.577579,-0.483384,8.420066,-7.126211,8.001311,-6.153643,4.750749,-4.964778,0.814659,-1.537426,-9.318788,-8.614748,2.842445,1.996430,-0.636862,-2.740814,-8.630901,-5.991226,1.314748,-1.738878,7.760563,6.461539,-3.593412,-9.411025,7.169245,-2.928920,-4.024934,-9.138234,-7.212587,6.559642,-6.821986,6.174758,-5.337709,4.096880,8.643008,-3.044410,-3.585331,1.130408,9.493530,-7.150063,3.491985,-4.987377,6.245176,1.754420,5.714979,-3.707657,9.355231,-9.374060,7.298882,8.404190,-6.483738,-5.420247,0.650171,8.352088,2.628066,5.229535,7.743176,4.418497,4.836770,-6.891884,2.442003,-4.206286,-5.543882,-8.364345,-8.410753,-5.538531,0.837767,6.580926,9.307815,-8.009487,-5.725353,7.710948,2.354238,6.246939,3.087347,7.409359,-5.038455,8.947834,1.816782,6.909254,2.007052,-6.995993,-1.257588,-2.627437,-9.180225,-7.340515,-9.159934,-4.386778,-9.253221,-2.565399,5.236633,-9.609695,-9.117357,2.926134,0.074606,6.916930,-4.384501,-4.959937,-3.346700,-1.477363,7.376485,2.215604,-0.254294,1.131794,8.810782,5.860178,-9.695449,0.406116,8.317174,-7.036427,8.759738,-1.988979,3.593250,-5.162658,4.922976,-4.812032,5.936332,-9.683762,-3.486821,4.820628,-0.600876,-2.423812,-7.578792,2.265617,-4.641750,2.784836,4.158701,-2.476576,-2.249941,-2.594604,7.939167,-4.070115,7.163386,7.279017,-2.509595,2.120583,8.325147,2.728714,8.876990,8.257551,-7.134023,9.018992,-9.164535,-6.499558,-3.600248,-2.187516,-6.086814,9.721205,-0.638466,6.958833,8.028640,5.718835,-6.505132,-8.063303,7.234571,-4.468970,-3.532277,5.884289,8.110515,3.295752,8.829581,6.802588,-3.632603,8.724842,2.797802,-9.470187,4.311737,9.969578,-8.331822,-6.674875,-0.586320,-2.825678,-1.308139,0.702764,4.399360,-7.137250,5.405236,-8.468129,-6.374199,-7.923815,-8.458881,-6.120002,-6.993763,-1.491692,6.684060,-9.747868,3.443183,3.361765,-5.314929,4.321626,1.206077,-6.284055,5.737712,0.423805,-2.430596,-7.207552,-7.783050,2.281813,-3.263730,6.491450,-8.597489,9.957271,-8.111645,1.324733,-2.341611,3.104604,-8.601661,-2.252411,-0.161443,0.231331,4.986571,-1.932840,-1.537548,-7.517420,5.424099,7.960728,5.655410,1.167066,6.332491,-9.536384,3.014771,5.353302,-8.012720,7.255591,2.537837,1.961858,-6.204585,-1.096045,4.965887,-4.053608,1.724072,-7.837623,-7.734602,-4.149054,8.494617,8.948507,-8.219208,-3.196071,-6.065262,-9.678966,5.531590,-4.146114,6.130591,-4.451718,7.075947,0.315659,-4.804228,8.837781,6.283140,-1.181321,3.366452,9.619825,4.823682,-2.491616,2.878849,7.190103,-4.447626,2.574803,1.408368,0.240491,-4.365331,0.885462,-2.111175,4.595163,-9.831776,-4.727359,-3.805506,-5.525013,-7.276303,0.911166,7.369066,-3.835173,3.593101,2.690058,0.340701,7.414806,1.826846,0.318341,-2.066043,7.699598,-8.746248,-2.455438,8.662793,-9.235323,1.849706,6.566617,1.917655,-8.433786,0.867533,4.078924,-7.143681,-8.200984,1.845619,-7.317516,9.229353,-3.093585,0.425564,-7.183578,9.004986,-3.023559,-8.238398,0.141184,2.316324,-8.614312,3.403402,-2.763670,9.174031,0.986360,-2.382434,-2.897698,2.429287,3.467175,1.234376,4.923025,1.122642,3.200428,-0.053309,6.969293,-6.379485,-3.772475,8.178221,-5.822231,-0.139089,5.474184,9.458752,-4.890975,-8.768126,0.954903,9.405448,2.632570,4.487707,-3.558617,2.158336,8.436705,-0.629928,-2.680882,-3.652690,-9.600452,-7.410294,4.542294,6.656639,3.661741,-7.617312,9.419764,1.800049,-9.924201,4.339756,-2.140611,-1.211596,-5.145499,-9.952722,-7.492695,1.889790,1.656784,-6.366719,8.948798,-1.592280,6.123931,-0.088396,-1.402024,3.462535,-0.635660,5.263710,-0.398310,-9.283378,-8.527763,7.537081,-2.844306,0.372669,-0.582030,-0.170269,5.763450,-9.280730,5.981785,3.524094,6.265587,-1.208655,3.328823,-2.899062,2.802656,3.837274,5.121450,-0.561557,6.578687,7.061617,5.755137,-5.276311,-8.551571,-2.657635,3.061950,2.608584,-8.591179,-4.649653,-1.263171,5.665415,7.662361,6.798182,7.423263,-0.437165,-2.099863,2.821072,-5.749651,-2.475489,-4.728007,-9.513071,8.802962,-9.037878,-8.596665,3.263236,-7.828633,-0.313162,7.842157,-9.287251,-3.641772,-8.806577,4.903130,-5.166621,5.300087,-5.278756,5.912195,2.701130,1.343863,1.568851,-5.598385,-6.275381,4.265659,-0.910025,-6.280291,-1.670522,-0.554570,6.170185,-7.508975,6.659227,5.825509,8.072894,-9.728756,2.773697,8.330929,5.807324,9.777574,-3.107226,8.679878,-8.911972,0.179827,-0.192775,1.558557,4.568143,2.734992,6.486322,5.322461,-3.675514,9.105549,4.652598,-1.675097,-1.714340,-2.180795,-0.763766,0.389592,1.146820,9.027406,-0.651916,-4.031498,-8.690243,-1.060661,-6.914362,2.646188,-2.257691,-2.223864,5.018170,-0.800095,-0.884773,-3.388493,-1.946027,6.412383,-9.078015,8.482363,4.490421,1.740701,-3.163411,8.513350,1.521614,1.418742,3.025854,8.741694,-2.530584,-4.583649,-1.972441,0.840880,4.547857,-5.440456,-7.060221,-0.565056,8.578794,7.920217,-3.246288,-3.873981,9.221033,2.415030,5.489608,3.126159,-9.074537,3.240399,-8.422218,-8.076771,4.567480,-5.327498,-8.598777,-1.749156,-4.666697,5.611006,-1.428722,-6.297217,1.413523,4.068035,-5.992284,-1.144368,-8.203658,7.789678,6.278876,-3.279022,-5.121087,-3.821957,-9.300293,7.308862,-8.692124,7.730127,-1.194550,4.144967,0.397285,6.615778,4.320662,-4.780480,5.405464,0.227100,4.244946,6.181960,-7.386968,1.747464,-4.305858,1.632457,3.867878,-1.976261,-7.168802,-1.059286,-6.456090,0.030936,7.682978,3.874571,6.246540,9.278621,1.681219,-1.263417,-6.868793,-4.247218,-4.242255,-4.875287,-0.803119,-5.408898,-7.950543,-9.007336,-8.611132,-4.885958,6.487597,-7.205856,-3.415687,-0.376811,-8.501442,3.465103,-2.646399,-8.572024,1.136611,-0.557811,1.095728,-2.859402,7.877617,-4.327807,-2.271138,-1.090579,-3.893656,-8.167519,-6.303123,-3.965211,-9.057758,-0.129717,5.477987,0.932864,3.249469,-5.428373,-5.379919,-7.958839,2.879293,3.754553,4.889443,-3.180716,-7.533265,7.918206,0.528611,-4.121435,0.383103,-2.647352,5.578242,-2.435688,4.965066,8.647439,9.124336,-4.859369,-3.722158,4.807110,7.182592,3.740976,-7.561679,-8.062649,2.070680,5.455057,0.408159,9.516790,-0.422479,0.722560,0.611014,7.713563,-2.065674,2.694470,-0.390501,8.080137,-5.679463,8.676093,0.152225,-4.149746,-5.246944,7.796290,4.109915,-8.816547,-9.687837,-7.752501,-9.405668,0.552817,6.136828,7.881462,2.791425,7.760217,-1.122300,-5.370902,-2.531823,-6.846938,9.696084,0.738657,-7.586841,-6.713921,1.823775,-7.607570,-4.780704,4.063507,7.171748,9.435339,6.435843,-2.117482,-4.105547,5.279589,-1.574729,0.727824,2.972417,-0.295529,7.101473,7.227277,7.365391,-0.971867,7.514620,0.153832,0.343145,3.183172,8.315335,-3.750131,-9.448195,9.388593,3.166373,-0.948867,8.221966,-1.694886,3.461818,7.661210,-6.551604,7.876501,2.049705,-6.434258,0.791155,7.634477,9.072563,-0.742139,2.204512,-6.994268,8.036209,-8.524652,-8.079805,5.210246,-4.873964,-4.813218,-0.402180,-4.286357,4.961283,-3.312256,-2.258883,3.915809,1.729090,8.182856,9.461870,6.754532,2.869004,0.204620,2.405509,3.799951,-1.460273,-5.231097,6.482134,-1.923799,3.324899,-2.725312,4.965181,7.008253,5.598040,0.902807,7.343917,5.353398,-8.638387,-6.458193,3.379502,7.682650,2.579769,6.123805,-3.534274,0.707383,-4.080519,4.687709,-9.820370,3.733265,-2.968689,-5.838858,5.786578,-0.452925,9.593682,9.671569,-5.591439,-6.515465,-2.755222,4.000720,8.429537,-8.628855,-0.991931,5.986730,1.068894,-7.539180,-2.030340,2.094987,9.448803,4.218861,-9.374626,4.284261,-1.146411,-3.482978,6.521204,4.900626,3.953426,9.900237,-6.612640,-5.643415,1.465009,5.478754,1.059819,0.174145,-3.024470,4.563817,-0.145372,8.134082,-0.988749,4.315773,1.869685,0.291512,3.967218,-3.760951,9.364248,1.253074,-4.556184,-8.688978,1.469790,-5.582213,9.088970,-9.256847,-2.064910,-1.513335,1.344735,3.798255,-3.614414,6.926453,4.606095,1.054699,-3.683174,7.891433,1.023342,8.234660,4.648219,-1.544815,3.063640,-9.259385,5.019944,2.745933,1.153630,2.816744,9.810988,0.004030,7.811611,0.387038,7.301882,-5.760336,4.806755,2.862781,2.414784,5.731891,-7.426942,-1.200975,-9.052499,-7.069088,-7.192990,5.710527,1.335035,-7.217760,-1.015931,-9.264133,-1.994843,-7.053097,-1.607775,9.023542,-0.711041,6.895939,-3.903166,-7.661822,8.518608,-7.171559,-5.777114,1.012635,-5.768175,-1.203233,8.484757,-5.660302,8.533392,1.018992,-2.722117,1.927330,1.467963,9.980262,9.369796,-2.098572,4.203062,-0.918081,4.642881,5.299881,-1.619413,-0.647269,-5.304924,9.428884,0.385927,-7.106867,2.529933,-5.105682,-9.313711,5.360448,1.571730,-6.639491,-2.955363,4.701558,-7.485577,-4.348741,-0.827604,-7.867358,5.290162,0.188794,9.652177,6.456351,2.753715,3.030976,6.465533,4.952353,2.890387,6.635135,5.488153,1.879139,8.066616,-7.143242,-9.547492,0.572033,-5.827874,-3.820213,-8.576277,8.100379,-8.130454,0.287190,6.742326,-1.598503,-2.569118,-5.885725,-7.272678,6.979791,2.232614,-3.388588,-8.882218,-2.180625,-0.303570,-3.422965,-4.064227,-4.970372,1.135193,-2.864757,5.546273,0.042589,1.107648,6.898622,1.275832,1.553531,-5.886726,-6.973686,6.296203,5.348543,9.013511,-2.317896,1.730505,-8.136094,-6.706700,2.620714,-3.186708,7.191343,6.974161,3.787820,6.146461,8.021243,-8.462761,1.942096,-1.531186,4.974253,-3.043494,0.590382,9.914977,-2.297154,1.426299,6.120364,-6.284589,8.390379,1.674549,-4.989675,4.698113,-7.243121,2.797920,-8.494360,-0.111298,-3.024526,2.036205,2.637662,5.573076,1.940665,3.834317,-7.278248,5.721657,2.001311,5.084739,-6.305940,-1.577691,-0.652344,-4.989354,0.866376,8.401565,6.050806,-0.077201,7.427156,1.821927,-5.811321,3.453969,-7.106377,-3.047838,7.579849,-4.908167,-0.468419,-6.918011,-9.297733,0.378784,2.372896,0.977855,-3.534672,4.362299,-2.342421,-2.205477,-8.407693,5.108388,-4.189387,-9.449242,8.901757,2.507234,1.938858,4.791289,-2.688020,-4.217853,5.412667,0.766031,3.668433,4.564302,3.722992,-9.389924,7.053541,-8.709824,9.623788,4.874197,9.586473,-7.363974,-5.536735,0.018106,8.940143,-5.874681,8.042103,-8.624931,5.482269,-0.127258,2.442830,-9.445046,7.664888,-4.515168,6.669758,1.669550,6.072802,-1.664806,6.705010,-4.584144,5.073249,7.432301,-9.325028,5.293683,9.788262,-2.692047,-2.617029,4.899393,-6.039678,-2.004157,6.881136,-0.645093,2.141975,-8.761193,-5.637033,3.172469,-0.459553,4.591026,-7.020649,-4.533073,-2.366312,-4.393792,0.068556,-7.085888,-9.946429,0.775007,0.001073,-0.983497,-2.155736,9.809126,1.450361,-5.594743,-6.740335,0.215332,-7.776541,-1.255404,-8.152246,4.987568,2.908183,0.160498,-6.378718,6.126655,5.942425,0.999879,1.249503,-4.801459,5.904436,-6.005232,-3.577023,5.014378,4.001747,-6.459066,-3.273751,7.142493,1.683607,5.427535,3.761102,0.308666,-8.691268,4.389204,-3.902999,0.690677,-6.095245,7.229224,7.141105,-1.900566,-8.220380,-4.825843,-8.258204,-0.492370,7.452582,-5.187049,1.316919,1.976089,-6.545956,4.243999,-9.190182,-1.366409,-0.025893,-4.551785,-1.165652,-1.723843,5.932981,-4.325051,-8.415019,5.611601,-9.098580,-6.801668,-2.983344,-6.928058,-3.632705,5.969506,-3.406319,-4.383057,3.947644,-9.842232,8.890751,-9.722376,5.800553,-1.038271,-1.482642,5.253600,5.769235,-1.338087,3.891018,-5.316961,-0.803604,7.887010,-6.304658,2.400980,-1.025346,2.418950,-6.053490,-0.625251,-0.438922,4.832862,-4.734659,-9.459931,-2.417878,5.239934,0.696694,-1.385319,4.581228,-4.234200,7.177491,7.233476,5.281409,8.532789,5.462775,3.462941,-1.648868,-4.808553,-8.677978,9.835858,8.146029,-8.230951,-0.348496,-6.161881,-0.475131,8.655972,-1.766459,2.670470,-8.570699,7.104432,-0.499832,1.862554,6.497317,-9.320321,-0.654801,-3.700782,-4.695510,-9.771794,3.577128,6.438977,0.665297,8.730600,8.412623,9.114836,5.304269,2.187894,-6.036564,4.733377,-6.919088,0.404666,6.031096,-6.883090,-0.488759,-5.219376,8.142459,-2.564058,1.314636,-5.888305,-3.020166,-1.034851,-3.616606,-8.062038,-0.233025,-5.645404,8.784619,-8.128472,-0.359080,-7.814605,0.088384,-2.162361,-0.898082,-0.002662,7.333647,6.591865,-3.902169,9.343441,1.896687,1.929192,2.743920,4.855371,1.462330,0.501780,-0.656844,3.688925,8.742552,0.428221,-6.410097,8.575277,-6.662613,8.972902,-8.316228,-2.883387,-3.297851,8.195830,9.489997,-8.025512,-6.410722,-6.758708,-1.794266,9.122083,-0.808660,2.931632,-1.055282,-8.268144,8.036782,0.979425,-3.388160,-9.075019,-6.844757,4.852641,-3.822194,-8.139838,8.109863,4.303781,-8.808750,8.732607,3.104852,1.799974,3.265348,6.269061,-5.607825,-6.938297,-1.148900,3.841080,3.913102,-9.639596,8.109867,-2.102664,-1.951019,-7.585683,-4.684243,1.678124,-2.628874,4.494376,-9.365766,3.338963,-4.522428,8.080362,-6.874039,6.976432,0.357730,5.527432,-0.549739,-8.309652,2.210573,-1.862449,-6.937983,-1.266492,-0.887460,0.648583,-0.615619,0.913300,-1.013542,3.689538,-2.756489,-2.331735,-7.157853,-5.010934,-6.761667,1.310124,2.545299,1.379949,7.509955,-3.462086,-5.494612,-7.101248,-8.708221,2.946157,8.924646,2.596821,5.873080,6.857205,1.205354,-0.132021,-4.737781,-6.093898,1.624743,-1.662790,0.897579,2.748833,-0.074570,-1.357084,8.899811,2.499067,-6.159944,-8.633550,1.280143,1.473569,6.210674,-3.210543,-5.543047,4.557048,-3.210421,-8.476228,3.815968,5.717422,-4.310447,-7.251209,8.450225,-9.672188,0.541834,0.882261,-7.916414,2.290905,7.463921,-1.915828,-6.065335,4.753262,2.358535,-6.350756,8.619334,-2.246119,9.497209,-8.015295,-6.066739,-0.499687,2.554517,-6.236479,5.696197,-4.987987,6.167567,-3.214793,-6.760844,0.280790,9.269931,-9.987405,8.971508,-7.129339,-5.791942,-5.122175,8.116538,-2.946133,-4.340793,7.031847,-7.448365,-5.991639,-9.837161,-7.695835,0.039801,-9.680663,6.967053,8.423792,6.720208,-5.974263,-8.285673,-7.519479,7.294618,0.689112,-7.454590,7.636613,-3.593629,-6.464544,-9.199404,9.473419,-8.953699,3.526888,2.912244,4.863599,-7.526240,-9.525113,-9.588041,7.174303,3.477487,5.950551,0.085214,-6.952649,8.538897,-4.744732,6.079033,7.995108,0.052077,-0.669653,3.741262,2.576983,3.884079,2.694811,-9.709210,0.737408,3.413147,6.197002,-9.845615,-8.029448,1.278756,8.244010,-0.606776,-9.690975,0.518032,-1.389169,-5.237915,0.406041,8.402013,6.239122,3.933760,9.403213,-1.224645,6.136211,6.880918,-5.329501,-5.372798,0.152409,-0.892724,-7.872933,-9.882738,-7.232127,-8.715450,-1.196996,-2.932569,4.272921,3.448626,-0.780314,-5.008866,-5.819533,1.119698,-3.982522,-0.134161,8.170952,5.349988,6.143773,-9.202755,9.589604,0.104181,8.278435,8.380805,3.375246,2.841383,-5.427282,0.088068,1.188708,8.279121,-1.884414,-4.040928,-6.922804,7.790074,3.630763,-8.974166,-1.758105,0.818952,3.459755,-2.503020,3.113745,9.083240,4.058220,-1.304366,3.559541,-8.792033,4.324128,4.851325,6.754165,1.600637,5.706563,3.359652,3.220118,9.328627,7.792920,7.293633,4.586345,2.652186,3.012918,-8.210494,5.036240,-7.939819,1.796804,9.719470,-5.555831,6.658962,-0.774372,8.230763,5.252127,-4.666957,5.434612,3.299304,-3.761429,3.315684,-1.023768,3.458294,9.207344,5.195611,7.949460,9.582369,7.257851,4.209760,9.338116,-7.776958,3.459280,0.565204,-8.566930,-7.567998,3.594762,2.788767,0.365197,-2.688542,-2.709290,2.949958,-5.938752,-8.143485,7.399035,4.696659,-7.909388,-0.178945,-5.429942,-1.886079,-6.015539,-3.030210,6.636675,-3.489083,-6.638475,0.306252,-5.332077,-8.038794,3.550204,-1.147309,4.159146,7.165393,8.831450,9.693812,8.460878,2.338909,-7.757935,-3.583644,6.572855,-6.314883,9.527305,-7.606044,-7.295353,-6.665360,5.629163,5.329711,-6.291601,2.053046,-5.407349,5.752711,-8.760675,4.426717,-2.819133,-2.120222,-5.800104,2.613299,-3.956847,7.058137,6.628008,-7.158248,8.659579,4.630600,-8.789818,1.403602,4.391691,4.695582,8.225997,5.417713,-0.221513,1.704371,-3.219493,-9.202837,3.308363,-4.155963,9.198949,0.962475,-1.381534,-3.279936,4.240298,0.231627,-5.809363,5.762152,0.405414,-0.272836,-4.726384,3.143099,-1.395931,-7.793341,7.474604,-8.994303,9.138800,2.705311,-3.941630,0.342681,-6.660908,6.018150,4.813287,-6.428794,8.518745,-5.778161,8.234035,-9.305992,2.767451,6.751633,0.890374,2.848201,7.986992,-3.806779,-4.912310,-2.060149,-1.888916,7.582050,-8.765494,2.340979,-7.665849,2.895599,3.781114,-1.164786,-5.931012,7.163204,0.124127,1.870270,-2.656909,5.594452,7.300895,3.461469,5.109350,0.803700,-4.906066,2.319494,-6.348275,-7.421253,-1.703741,-2.843070,-3.926534,9.431442,-2.598798,2.155185,-6.252038,8.701983,-7.542919,-3.510005,7.023426,2.086855,-1.424828,9.066523,6.088281,-6.801394,-0.295801,8.173402,-4.818244,-1.039504,3.664078,6.807943,-1.363045,4.924422,2.032488,-9.478932,9.413916,8.976765,-0.156975,-4.816705,-5.739961,-5.233810,4.724240,-2.234436,-5.528228,-6.337000,-2.811933,6.497877,-3.272539,7.008757,-9.251357,-0.623956,8.687895,3.947895,-9.994358,8.140136,-3.280587,7.089760,3.007627,-1.238017,6.489158,1.758523,-7.646115,-4.691328,4.285778,9.234059,-7.221333,4.985455,9.375426,2.331949,-9.339918,-7.620996,-1.410167,-1.951589,7.059039,4.917250,4.304179,-6.831729,-2.291602,-2.713838,-2.427532,0.101115,-5.480119,-0.386028,-1.283041,0.849199,3.391279,7.305543,-5.971145,9.972512,-3.847996,-4.119285,-1.601216,-4.472633,7.158407,-8.879975,-7.529766,-1.897158,9.636522,-6.054623,5.761944,-3.326601,3.158452,-9.183522,-1.638865,-6.068267,3.462854,-6.912780,4.307077,-0.232416,-6.397175,1.749574,-4.566290,1.626359,-3.657795,2.083621,5.731005,-6.588503,-0.761098,-2.166141,9.020579,8.000749,1.614521,-9.179139,-3.600930,-5.847937,1.168225,2.893503,9.987291,0.960987,-9.828895,4.453009,7.501338,0.439275,8.780664,-4.317841,-8.535278,4.733722,3.731221,-8.625416,-4.676130,-4.670161,-2.086507,3.312582,-3.158405,-5.375347,-0.894874,4.713493,6.128901,5.486253,-3.434950,3.795351,1.357466,2.467783,-2.302255,5.493448,-2.715146,9.546642,0.933949,-4.493662,6.721002,4.983550,7.225834,1.147196,6.718032,4.485296,-6.381517,-1.071613,9.795999,7.612973,9.293862,-8.733387,-8.537225,2.890571,-4.318680,-0.702303,-7.735736,2.587938,-4.146276,-6.378536,8.379521,7.464265,8.956267,-5.282412,6.055671,-4.885055,-1.371197,-1.208714,-7.105200,-8.541608,-1.919173,0.793534,-2.359958,-5.490759,0.660728,-9.929985,-6.112127,3.149431,9.976040,-1.199387,3.998666,-9.035209,6.272425,-2.108387,-2.239448,-1.801334,0.366481,9.166215,2.003773,-2.543381,-4.182345,3.036418,1.362390,-0.420464,-5.910394,7.926956,-3.455751,3.833852,0.748982,7.808550,7.070211,-0.732810,9.846963,-1.174376,4.633890,-8.141873,-3.307646,-8.548430,-8.781791,-8.281267,4.909101,-9.197071,1.914941,7.666931,5.169529,-8.850827,-7.503428,-7.618123,-5.939489,-1.545436,5.684285,-0.746957,8.938228,0.998995,1.100540,-9.335254,-3.858174,-8.805978,4.737782,-0.186911,5.640168,3.216954,2.367514,2.825793,-0.546132,4.024419,-2.111746,1.029403,-3.454925,0.655033,7.118111,-7.774237,-5.802995,7.616083,-1.455325,6.281629,6.334803,2.894650,-4.984196,-0.874846,1.916718,-9.049941,3.267023,0.958181,6.519390,-7.222112,-8.508106,-1.917488,9.794528,-2.381735,7.822555,6.234248,-9.027117,1.054646,-9.370646,-4.022586,4.342411,9.481352,-7.861064,-9.039829,-2.013191,-9.346969,2.462286,7.299074,5.023814,-4.805146,3.323944,0.686917,-4.686437,-4.146663,-4.514257,-0.686442,-8.336513,2.251731,-1.630307,-5.693361,-3.528755,-3.208448,9.641274,-1.775080,8.456439,8.774353,2.643434,2.035771,7.361198,-9.996830,-0.589750,2.752382,-0.282805,5.270799,-8.660561,6.300531,0.262010,-7.794529,-8.299863,6.751675,6.281296,-8.631069,4.236063,-5.928789,-2.957675,-9.612426,-3.634099,9.271533,-6.722202,5.572409,-0.890760,3.333285,-2.742231,-0.471851,6.579992,7.119637,-0.347522,3.579322,0.864471,-3.784912,-4.996285,-5.872044,-6.139861,3.949405,-2.391227,7.911367,-2.405402,-8.962296,-2.185701,9.776176,-2.413596,-1.387486,-3.655352,-5.307036,5.636474,4.327313,-3.680035,-9.448529,0.268815,9.708811,4.326777,-2.656763,-8.892149,-3.911901,6.876883,-1.710581,-0.436836,-8.396545,-5.944079,-3.240753,5.870290,3.481483,6.906382,-1.698497,5.537413,5.384242,-6.069958,-5.480891,-5.552409,7.956314,-7.114433,-7.101068,-9.626285,-9.106967,5.292459,1.337231,-0.142185,-3.602004,-9.309164,8.260639,2.814187,-2.715781,-6.754579,-2.641095,-5.167369,4.238508,1.259129,7.226242,-0.325179,-2.617933,6.295123,3.366722,-9.750596,8.527185,-4.461785,-6.466413,0.585028,-3.628983,-3.337569,8.055087,-0.460025,2.689177,-6.934948,-3.725290,-6.958394,-8.124336,-7.638433,-9.213824,-0.358008,8.766057,-4.890956,-3.952184,1.298954,5.507608,3.225270,-1.207260,3.852314,4.903505,-9.886011,9.990106,-3.202730,-1.899718,0.364959,7.533676,6.493321,-8.749048,-7.673370,1.197269,4.682637,4.735890,2.662893,2.768406,-7.320487,-4.629815,-2.149310,6.840148,-7.617390,6.483227,-1.381405,5.465253,4.733292,2.921551,-2.345311,9.583868,-5.924319,-6.260677,-6.610651,-7.060593,-3.573606,-6.206761,-4.503907,3.800053,2.830599,-1.016432,0.148827,7.170082,-7.238071,-2.288055,-7.862782,-5.647539,5.905512,-2.315499,-9.476333,-2.692147,-3.598401,9.574659,-9.684858,8.555772,4.758147,-8.607280,9.019993,-3.426343,-6.426694,-8.013894,-4.636791,2.867985,0.632558,-6.787332,4.753471,-1.035078,8.262337,-8.336179,-3.875621,1.600502,-0.903546,-8.739767,-1.109621,9.999531,3.975956,7.464232,-5.174845,3.230983,-9.732391,-9.411359,-9.614317,0.245863,-6.832330,-6.720385,9.611746,4.299862,3.801592,9.960136,-3.860007,-3.865214,-5.959741,1.326852,2.404695,-4.047197,-3.802556,5.826070,0.140587,-4.676039,-9.146620,-3.834180,0.739344,4.546155,2.954837,-2.844344,3.533572,-1.236154,-0.145624,0.064309,-9.518373,7.700689,-4.714480,-9.151426,-1.257442,9.051912,6.503015,-0.259375,6.497533,5.407967,8.617296,-9.241054,-3.129821,-8.764785,3.939776,-4.423930,-8.604652,-0.441974,-7.132343,-3.984156,-6.254458,-3.247496,-6.982033,-7.160505,-8.845115,-1.368204,9.445948,6.722176,5.632179,-6.177181,0.734833,6.243801,-5.066359,-4.931191,-0.587888,9.738303,-6.657144,-0.178221,1.074707,9.724316,-6.806228,4.113929,-6.603859,2.405043,-4.195995,-4.122848,5.855993,7.206473,-6.641082,-6.751142,2.055010,3.100951,0.754011,-9.594976,-4.416826,8.663420,6.105399,-7.652253,9.512016,-9.456861,1.510954,5.854365,-6.109551,-3.972752,-9.863181,1.833583,1.139151,0.465395,-2.497432,7.809699,0.268829,9.386793,7.259484,0.887621,8.300368,-6.141520,-8.729131,6.568091,2.759769,1.501720,1.607439,8.870225,3.872751,8.802656,-8.468515,-8.102948,8.220279,-9.971150,9.440160,7.497151,1.225881,3.530987,8.718171,-8.915634,0.789040,-0.649445,-5.007915,0.510209,5.305143,8.200515,8.500562,0.708097,3.019715,7.412984,1.657235,-1.904899,-2.567334,0.887829,-9.917481,-6.958357,8.176790,-3.087238,-8.523534,-4.671150,1.162006,4.226193,6.174152,1.309584,7.589680,-4.811109,-5.060842,0.213750,-4.518855,-2.174271,7.318218,-2.459138,-6.849494,-8.923407,-1.760374,-0.300394,4.061954,-0.603438,-2.444094,2.899413,-9.054589,4.592462,-3.869911,-5.875125,6.345483,-7.553195,2.104260,3.151946,1.205398,9.365379,-2.438490,4.064915,7.582935,5.111353,-3.086028,9.692440,-2.728461,3.983483,-8.022229,8.174705,-6.466467,-7.567808,5.038982,9.812745,7.552502,-6.308461,-6.947440,6.078511,-7.215058,-4.196342,-8.194987,0.104137,-5.395603,9.549596,-7.165788,-8.454090,-7.782782,3.031378,-0.424523,4.088395,4.984948,-6.922670,8.155178,0.011183,-0.955027,-3.377019,-6.568295,3.750038,-5.882391,8.834860,3.021778,-6.122441,-7.965375,5.378986,-2.586025,-1.570677,6.694099,-2.520225,7.607088,-4.409516,5.512216,-8.212718,-9.657293,-8.534091,-3.159776,-1.812026,4.849497,-6.156983,-8.434945,-1.442788,-1.554363,-8.224613,6.995440,-8.177548,-7.344608,-6.765642,-3.514574,5.855422,-6.023567,4.600672,8.444857,6.920099,-1.154251,-4.443927,5.119831,-5.808412,-3.681978,1.001903,8.175107,-1.445714,-1.612524,1.998365,1.660929,-5.333827,-8.151042,-6.903798,8.977202,-7.229747,0.550512,-9.592810,5.455644,-7.890002,3.124925,-7.362687,-6.623512,-8.395439,3.287940,2.719707,3.487436,6.559683,1.735169,6.810888,9.218304,5.441240,5.140923,5.892965,-0.754427,-9.257521,-0.909009,-3.212399,5.254522,0.734143,-3.267022,2.967068,-5.931181,1.586419,-4.277195,-5.589407,-4.251368,9.318596,1.902044,-0.514772,-3.636499,0.770577,3.645314,7.856302,8.000164,-0.583906,8.433929,1.851961,-9.337370,-0.891197,1.762942,-8.134003,-0.382114,2.005966,-1.028206,2.875870,-3.071991,8.351460,-4.503571,-8.714428,-8.763343,3.807526,-0.799192,1.604350,2.055827,-0.127746,1.977995,-7.675273,-1.184290,6.790680,5.152439,7.173915,-0.526241,-1.862051,-8.735846,-2.570538,9.061884,-6.530372,-5.024923,-0.308556,9.855924,-9.203089,9.853139,-7.989203,2.608718,-6.629797,-4.732082,-9.704044,5.815741,0.109660,-3.234193,-6.938750,5.902791,8.602836,-4.233601,3.329058,-1.047268,-3.445386,-1.842300,2.870184,6.800651,2.898398,-0.440713,-5.665033,-0.248405,6.627935,0.007161,-0.404867,-8.752406,-5.711982,4.108590,7.577925,6.506990,0.474202,-2.513175,9.850738,-5.177041,-1.845988,6.224375,-5.918808,-4.621708,-1.856800,9.786051,4.106710,-7.017658,0.530514,6.410532,-1.457157,-3.680950,2.459013,-1.190141,-9.829618,9.011538,6.503890,8.198305,-2.874538,8.483644,5.426618,7.379492,9.603791,-8.256071,6.365964,1.528616,5.518363,9.406437,-3.684700,9.612708,-8.027612,1.044278,5.738376,-5.551014,5.967171,-9.936450,-4.960666,8.255091,-2.060541,-8.946877,0.551696,7.170702,-3.931609,5.133696,-6.021831,8.420190,0.431177,0.328256,-4.289481,-8.343267,1.375601,-7.918371,-6.182235,8.191864,-7.925751,-7.490958,8.569721,-6.127556,-0.036864,8.900586,-4.414035,-7.870464,7.269019,4.416516,5.544305,0.790548,-1.499956,-1.657892,4.194893,8.020522,-8.697711,-6.041830,9.062531,7.770920,-5.747821,9.497828,4.697415,6.246289,2.933239,-8.950572,-1.614111,5.817715,-7.286293,-2.353221,-4.094500,8.098259,8.418907,-2.337715,-8.907875,7.683828,-0.032533,8.729550,-7.673005,7.882208,6.236103,-2.602236,1.097877,7.130423,3.276146,-6.356689,0.258104,-8.106790,9.041803,-1.428262,-2.249805,-8.965099,-5.017970,5.597205,-3.322284,-6.462851,-5.240251,-8.533103,-3.353061,7.190769,2.139947,3.404154,4.305317,5.683471,2.218999,-8.374756,3.042105,-7.389867,8.007540,-9.120312,-6.909653,1.527425,1.929386,1.667022,7.489659,-0.826283,-4.058606,-2.748606,7.667453,-3.746103,9.663290,5.418451,0.898393,-9.410767,5.168663,1.819384,6.726826,-7.322944,-4.945613,-2.925406,1.912052,-5.890800,9.492793,5.752640,-0.897076,5.526967,4.656439,1.545569,-1.175666,0.974133,-3.966159,-5.902529,3.148518,3.546744,-2.891395,-1.156934,-2.349666,1.745128,5.064039,-4.418879,-2.547851,4.140607,-9.526351,-6.855697,-8.963486,-2.444183,-0.625474,-1.998321,-7.394514,8.805801,9.868219,-4.918983,-7.396723,9.785938,-0.626160,-6.609595,2.297520,-5.226537,-2.919276,0.659470,-1.203798,2.270978,-9.331472,9.367288,8.374092,1.926336,-3.107457,-9.160270,0.675137,-7.196866,-6.478096,-5.322225,-1.709800,0.366775,9.998208,9.191792,9.890426,3.693752,-4.156866,-0.069943,3.620239,-4.893097,3.006038,5.959206,9.341417,-9.950795,-0.684691,8.325613,-8.121443,1.057893,0.828457,3.270084,2.296774,-6.029822,2.740064,-3.582964,-1.056516,-8.727614,0.280409,-2.036981,4.422480,-8.957148,4.564606,-0.727079,8.471611,-7.892624,-5.710053,8.777788,-9.367374,0.052828,-5.516167,-9.161587,9.099733,-8.860883,-4.943552,9.930656,1.943493,2.349715,6.865307,-9.841582,8.090416,-0.721493,3.773742,-3.569850,7.052177,3.081613,3.016912,9.982539,5.372266,9.500333,-8.177125,6.084511,4.999181,8.635891,7.595148,4.074960,-7.413910,-3.830920,4.101084,9.457787,6.906610,-3.769398,-4.590162,8.992323,2.841689,-4.156319,5.529171,3.676834,-0.878616,5.346317,8.051862,4.138390,-0.033959,4.187636,-5.494552,9.321932,8.784062,-3.302895,3.452355,6.632339,-6.634704,-5.640852,-6.200168,-7.483316,-1.463769,-6.890650,-9.969434,4.014771,3.901252,-7.637488,7.122098,9.809076,7.799889,8.302441,7.737813,3.442193,-4.964172,9.265696,-0.176480,8.555361,-2.400744,-3.864240,2.442716,9.787941,-4.458149,-2.110971,1.108926,-8.465966,8.732065,5.697509,9.791780,0.745769,2.861706,-1.982779,-6.173599,-7.789880,0.659152,-8.923401,8.205598,3.443970,1.504361,8.158708,-5.693264,-1.891258,3.841502,-0.342118,-7.097940,-9.372304,2.792044,2.960540,1.816491,-2.008795,-4.930187,6.281047,-0.164755,7.844982,9.749030,8.202355,9.214413,0.524902,9.570764,7.567802,4.430004,8.696564,-0.756542,6.573095,3.872428,-0.483350,-0.725904,7.320459,-6.264681,-0.462167,2.210211,8.631737,8.626599,-4.182923,5.078571,9.563794,0.252046,6.248694,2.090443,6.680769,-8.186889,3.107554,-7.825313,4.182561,9.784598,-7.128753,8.252890,7.736265,-4.799546,-0.288515,5.385603,9.593834,-6.880880,-7.344756,2.466255,-7.610960,7.808536,-7.753313,-2.956643,3.015087,7.131925,3.207319,8.756367,-6.103442,-0.382156,1.037593,-2.320799,-1.614033,4.692245,-1.273285,8.219085,-3.087546,-3.534029,-7.218132,8.370319,2.244444,7.736147,8.153408,5.221542,-2.985645,-4.162154,-8.823321,-9.590125,-7.445706,7.055558,-2.501161,1.773154,-8.348260,2.117960,5.967724,-0.680563,-8.831705,0.310852,-6.514852,1.992176,-3.212865,0.674462,-1.760021,1.318812,5.506195,2.980667,9.742817,9.495864,9.611073,-2.944683,5.176049,5.687318,-5.141840,1.699803,2.434083,-2.084257,5.151273,-6.809811,5.160696], dtype = "float32")#candidate|4892|(3120,)|const|float32
call_4890 = relay.TupleGetItem(func_2216_call(relay.reshape(var_4891.astype('float32'), []), relay.reshape(const_4892.astype('float32'), [13, 16, 15]), ), 0)
call_4893 = relay.TupleGetItem(func_2219_call(relay.reshape(var_4891.astype('float32'), []), relay.reshape(const_4892.astype('float32'), [13, 16, 15]), ), 0)
func_2044_call = mod.get_global_var('func_2044')
func_2046_call = mutated_mod.get_global_var('func_2046')
var_4900 = relay.var("var_4900", dtype = "float32", shape = (168,))#candidate|4900|(168,)|var|float32
call_4899 = relay.TupleGetItem(func_2044_call(relay.reshape(var_4900.astype('float32'), [1, 12, 14])), 0)
call_4901 = relay.TupleGetItem(func_2046_call(relay.reshape(var_4900.astype('float32'), [1, 12, 14])), 0)
func_1962_call = mod.get_global_var('func_1962')
func_1966_call = mutated_mod.get_global_var('func_1966')
const_4903 = relay.const([7,-7,8,10,-4,-10,2,-1,2,8,7,10,8,9,3,10,-1,3,-6,-1,-3,-7,8,3,-7,7,6,-5,9,-4,2,-2,-2,-10,-7,1,3,-8,-5,8,10,6,-5,10,-5,-6,-10,-9,3,-1,2,2,-9,6,-1,-7,-2,-7,-4,-8,-3,7,3,6,-5,6,-10,-5,-1,6,-5,-1,6,1,6,2,-6,-3,-4,4,-7,-9,3,5,-4,3,3,-6,3,10,9,-1,2,-5,-2,-8,-3,5,10,7,-10,-3,6,4,7,1,8,4,-7,-6,9,-7,10,6,1,-4,-6,3,-4,-1,1,-10,5,8,-2,10,-10,-2,8,-2,3,-9,-3,-1,9,2,6,-8,-4,3,-3,-5,-10,5,7,7,3,9,10,7,-1,-9,8,8,-6,-8,-1,-1,-4,-1,6,-2,-5,7,10,5,2,8,1,-4,4,7,-8,8,-7,-2,-6,3,5,7,5,-9,-5,-7,-5,-7,-4,6,-3,4,5,2,-10,5,5,3,5,5,10,-10,4,6,10,-9,-8,2,9,-7,6,-4,-5,1,8,-1,9,-3,-9,-2,-1,-1,-4,-4,-4,1,2,-3,10,-6,9,7,9,10,1,6,-2,2,-9,-8,7,2,-5,-6,-8,-3,2,-4,2,-10,3,4,2,-1,10,3,-1,7,-2,10,7,-9,-5,-1,-5,9,-8,5,-7,-2,-8,-6,-2,6,8,-5,1,-6,-5,3,-10,1,-5,10,3,-3,-7,-3,-2,4,-2,6,3,10,-9,-1,7,-6,6,-6,-8,-3,8,5,-2,-3,-9,10,1,1,4,10,2,4,4,1,1,-8,-10,10,-3,10,1,4,-1,3,-5,-7,-9,-8,-2,-6,3,-3,-8,-6,-7,-2,8,10,1,7,6,-4,6,9,-1,3,10,10,9,10,-4,-4,-8,-4,-10,6,6,3,4,-1,9,-10,2,-9,-7,8,-3,4,1,-10,-10,8,-6,7,5,4,4,2,-5,-8,2,-4,10,-6,-7,-1,3,-2,-10,-9,-6,8,-9,7,-3,-6,3,-2,9,6,-4,-4,8,-6,-4,-5,7,2,6,-10,6,-6,8,-4,3,7,-8,-2,9,-7,2,3,5,-5,-5,-10,3,-10,3,9,3,-3,9,9,5,10,8,-5,9,2,5,2,7,10,-7,5,-7,3,4,-5,-8,6,-8,-6,3,8,-1,7,-6,9,-7,3,3,-1,8,7,1,-1,-6,-4,7,8,-6,-10,-3,-6,-3,6,7,-6,3,2,-9,-3,-9,6,10,-8,1,1,-6,6,-7,7,10,-8,9,7,2,2,8,9,-2,-6,-2,-10,-5,-10,-1,-8,-10,-5,8,-6,-3,-2,-6,1,-8,2,-6,-10,1,5,7,-4,-2,8,3,8,2,-9,3,-6,-8,2,-3,7,2,-5,-7,-8,7,7,-9,10,-7,8,8,10,2,-2,-4,-8,-2,5,-1,-8,-8,10,4,-9,-8,2,10,-4,5,9,4,6,-10,7,6,2,2,5,4,6,10,-10,9,-5,9,-4,1,2,4,3,-5,-6,-8,1,-5,-4,5,5,9,10,2,-2,5,4,-3,9,-5,3,8,-5,-4,-7,-2,-5,-2,8,9,9,-6,-1,-2,-7,9,-10,5,-9,-4,-8,-9,-9,7,5,9,-8,-8,6,-3,-7,-2,-7,-4,-5,-5,9,7,-6,-5,-8,6,-3,-7,4,-9,-2,10,7,-8,-4,-7,-8,1,9,-7,-2,5,7,4,3,2,2,7,-8,4,-9,-7,7,2,-3,3,2,-1,-1,10,-8,-9,8,2,8,-2,-10,5,4,-3,6,4,-5,9,-2,10,-5,10,3,-9,-1,10,-9,-7,2,-10,10,-8,-1,-3,-8,-10,-1,4,4,7,-6,7,3,8,5,-6,4,-2,-3,-5,-5,1,7,10,-3,-9,5,4,-1,7,-2,3,-9,10,-9,2,-4,-9,-2,-4,-7,4,10,-2,-10,-9,4,-8,-6,-4,7,-8,-2,-2,8,-9,-1,-9,-1,-4,-3,-3,4,9,-4,-6,10,-2,10,9,9,7,1,3,-10,-2,9,-8,-9,-6,10,3,-3,-6,-6,5,3,7,7,-3,-6,-7,-10,-9,-2,1,-4,-5,1,4,-4,-5,8,-10,-10,1,8,3,5,-9,7,-10,-6,2,6,-5,2,7,1,-6,-10,9,6,-8,-3,9,-8,-3,-4,4,-10,2,10,-1,-9,-2,-5,-9,-4,-4,-7,-9,2,9,-6,7,1,-7,1,2,6,-10,-8,1,-7,8,-8,9,8,7,3,9,5,7,-3,-5,4,9,-4,1,-9,-7,6,8,-4,-6,-1,2,-3,4,-7,-7,4,-2,-10,2,-4,4,-5,-1,-9,5,-4,-8,6,-4,-10,-4,7,-5,-9,-4,-7,10,-3,10,-8,4,4,10,3,-10,3,9,8,-8,-4,1,-3,5,1,-9,-2,2,6,-3,6,-4,-9,-10,1,-5,10,-8,6,10,9,-8,-4,-7,4,1,-5,-8,10,-3,-6,7,4,-9,-9,10,10,-8,-10,-7,5,6,-5,-6,2,7,8,2,-1,2,9,5,2,6,-8,-8,-2,-3,-7,-3,8,7,-6,-8,1,7,4,1,-5,9,1,6,-10,-10,10,9,5,-4,4,-10,-3,-7,8,4,5,7,-1,-7,2,9,3,9,-4,1,-6,5,9,-8,-9,10,-6,-8,-2,7,4,-5,5,-7,9,-9,10,-6,-5,3,7,-8,4,9,2,-9,3,5,2,-9,1,-7,1,7,-8,-9,-8,7,2,-8,-3,3,5,-3,2,-9,9,4,-7,-7,-1,-9,3,1,-3,4,-9,9,-6,10,-6,3,-5,7,-7,-9,1,9,6,-3,-10,3,3,3,8,-1,4,-2,-2,3,3,10,-1,-2,-1,-4,-2,-10,10,-6,1,-5,-3,6,-7,-7,-2,-8,5,8,5,-7,-2,1,4,-2,-7,10,5,-7,6,5,-10,10,3,3,1,-4,-9,-7,-6,-6,8,-3,5,-5,4,8,3,9,-6,-3,-2,-4,-3,2,9,-2,-7,8,-7,-10,5,4,5,-3,8,2,2,-1,-4,-6,-2,-10,5,8,2,-2,-7,4,-10,5,-2,7,2,3,-10,2,7,-2,1,4,-9,2,-1,-10,-5,10,-3,-5,5,-4,7,1,-8,-8,-3,4,-7,8,5,10,4,-7,-6,-3,-10,-10,-2,1,-3,9,-9,8,1,5,-5,-4,-6,-3,3,5,-4,10,-7,-6,-10,-8,9,-7,1,4,9,-4,-1,7,-4,7,1,-2,8,9,-6,-9,3,5,9,2,9,3,5,-6,-4,5,-2,-4,-8,10,-1,8,4,10,3,9,7,4,2,1,2,-3,-6,5,-9,-7,-4,4,8,-9,-5,-5,-2,6,-8,2,-4,6,-2,-3,8,3,3,-7,-1,-2,-7,-1,-5,-5,-4,4,-3,-6,-3,-8,-9,10,10,2,6,-10,-2,-1,9,-1,2,1,-8,-10,7,10,1,-7,9,-4,5,5,-6,6,2,-6,-3,-10,5,-1,-10,-8,3,1,5,7,9,7,10,-9,-1,9,-6,-6,-10,3,2,-8,5,6,-5,1,-7,-9,2,-1,7,-8,10,-1,-4,10,-6,-10,-10,-10,-1,8,1,-7,7,7,-2,6,2,-4,-2,2,-3,-8,1,9,-10,4,-6,4,10,7,8,-4,1,-9,-2,-2,3,9,9,-10,5,-10,-4,4,10,8,5,10,-1,2,8,-10,3,7,-7,2,-10,3,-9,-9,-8,-8,-2,10,5,-7,-5,8,-8,1,3,-7,8,-8,-9,-7,-6,2,1,-1,6,-3,-7,-9,5,10,5,-10,1,1,5,-7,-1,8,2,2,7,9,4,9,-1,-7,8,9,-5,9,6,-2,-4,-1,-10,-4,-8,-3,4,2,-2,-10,-8,10,-9,3,5,-4,-6,5,10,6,-4,-10,2,-4,3,-5,-4,4,5,1,-5,-9,2,10,5], dtype = "uint8")#candidate|4903|(1512,)|const|uint8
call_4902 = relay.TupleGetItem(func_1962_call(relay.reshape(const_4903.astype('uint8'), [14, 12, 9]), relay.reshape(const_4903.astype('uint8'), [14, 12, 9]), ), 2)
call_4904 = relay.TupleGetItem(func_1966_call(relay.reshape(const_4903.astype('uint8'), [14, 12, 9]), relay.reshape(const_4903.astype('uint8'), [14, 12, 9]), ), 2)
func_2337_call = mod.get_global_var('func_2337')
func_2340_call = mutated_mod.get_global_var('func_2340')
const_4912 = relay.const([[3],[8],[-7],[3],[-8],[3],[6],[5],[4],[1],[9],[2],[-3],[-9],[-4]], dtype = "uint32")#candidate|4912|(15, 1)|const|uint32
call_4911 = func_2337_call(relay.reshape(var_4891.astype('uint32'), []), relay.reshape(const_4912.astype('uint32'), [1, 1, 15]), )
call_4913 = func_2337_call(relay.reshape(var_4891.astype('uint32'), []), relay.reshape(const_4912.astype('uint32'), [1, 1, 15]), )
bop_4922 = relay.power(var_4900.astype('float64'), const_4912.astype('float64')) # shape=(15, 168)
output = relay.Tuple([uop_4886,call_4890,var_4891,const_4892,call_4899,call_4902,const_4903,call_4911,bop_4922,])
output2 = relay.Tuple([uop_4888,call_4893,var_4891,const_4892,call_4901,call_4904,const_4903,call_4913,bop_4922,])
func_4941 = relay.Function([var_4891,var_4900,], output)
mod['func_4941'] = func_4941
mod = relay.transform.InferType()(mod)
var_4942 = relay.var("var_4942", dtype = "float32", shape = ())#candidate|4942|()|var|float32
var_4943 = relay.var("var_4943", dtype = "float32", shape = (168,))#candidate|4943|(168,)|var|float32
output = func_4941(var_4942,var_4943,)
func_4944 = relay.Function([var_4942,var_4943,], output)
mutated_mod['func_4944'] = func_4944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3913_call = mod.get_global_var('func_3913')
func_3914_call = mutated_mod.get_global_var('func_3914')
call_4946 = relay.TupleGetItem(func_3913_call(), 0)
call_4947 = relay.TupleGetItem(func_3914_call(), 0)
output = call_4946
output2 = call_4947
func_4949 = relay.Function([], output)
mod['func_4949'] = func_4949
mod = relay.transform.InferType()(mod)
mutated_mod['func_4949'] = func_4949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4949_call = mutated_mod.get_global_var('func_4949')
call_4950 = func_4949_call()
output = call_4950
func_4951 = relay.Function([], output)
mutated_mod['func_4951'] = func_4951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4139_call = mod.get_global_var('func_4139')
func_4141_call = mutated_mod.get_global_var('func_4141')
call_4994 = relay.TupleGetItem(func_4139_call(), 0)
call_4995 = relay.TupleGetItem(func_4141_call(), 0)
func_4806_call = mod.get_global_var('func_4806')
func_4810_call = mutated_mod.get_global_var('func_4810')
var_5003 = relay.var("var_5003", dtype = "float32", shape = ())#candidate|5003|()|var|float32
const_5004 = relay.const([-8.339594,3.254369,3.742111,5.193148,-4.330442,-9.806689,-8.648182,-2.625517,-5.577003,1.997421,-5.086365,3.093150,-9.734034,0.350770,7.196983,-6.416470,3.631116,0.173029,6.718355,-8.664225,-9.401800,-1.019375,0.587998,3.410437,8.729672,-5.769226,-3.815746,-8.735772,-0.727858,-7.636032,-3.383758,0.076017,8.682348,8.181225,7.695533,-3.540461,-2.449776,-8.642791,4.155530,-9.686802,-6.167277,-2.605157,-5.448221,-7.871018,-7.146467,-0.624490,2.105954,-5.239717,-0.870879,4.727367,3.339118,-5.553160,-2.674987,-9.768334,-8.260292,9.270381,4.699369,8.215822,-7.572812,-6.996536,2.075911,-3.261592,3.101011,8.851567,-3.980385,0.832695,-3.359217,1.501264,9.212346,-5.512607,-1.565528,-7.386580,9.753127,7.062719,6.289277,-2.390255,5.837615,3.916077,-3.905586,-9.808227,-6.224197,-2.594250,1.838349,8.504744,4.875688,-2.120198,3.165047,-3.690212,2.431541,4.152548,1.142637,6.401098,-1.743942,7.958707,7.976592,6.515581,-9.980957,-9.576050,5.908426,-7.519498,7.998421,7.933310,6.551212,5.080713,5.384235,-3.750539,-9.901616,1.466703,-4.598760,8.730086,0.387882,4.492902,8.518636,4.055091,-7.547405,4.150425,5.070164,-4.782700,-9.780890,5.657628,-0.313761,4.543455,8.958559,7.992724,7.340555,1.137566,2.010767,-6.121303,-6.439922,-1.725084,9.241056,-8.267857,-8.630628,-6.309645,-2.712728,-6.076494,5.924954,3.756716,0.740554,-1.179338,-7.145748,0.396946,1.012409,-7.549510,9.159674,-1.628834,-2.603695,6.836762,9.205947,-1.889090,5.209239,8.251712,-6.348695,5.879087,8.022380,-9.816452,0.348848,-1.809269,-8.802521,-6.248956,0.414042,-8.524192,7.939571,-6.845618,8.721521,-6.675721,0.193634,4.061516,9.481535,8.564861,4.308485,-0.116302,3.654115,0.164572,4.230321,-9.292150,-7.739014,-6.695340,-8.337710,-4.246642,6.656869,8.533667,-2.688409,-9.402185,9.137451,3.017574,-8.193529,-0.046355,-7.867329,1.105716,9.652832,-8.042127,-5.873545,-3.629493,1.810874,6.365575,5.718140,9.733047,7.045950,5.743883,-7.830338,7.618195,-2.967039,-0.033641,9.180211,-3.519564,4.520891,-5.182510,-0.140850,4.547733,-9.851576,-3.177306,3.893594,7.371593,-3.499031,8.002220,1.451483,3.978034,-6.486488,-1.734584,6.925427,9.117994,2.797110,-6.761807,-3.654858,8.767205,-5.369320,-9.345162,-7.288617,9.051898,2.129406,5.945737,9.509243,-7.565711,-9.689044,-2.548997,-2.987503,2.407334,3.653251,0.793569,7.343788,-7.715455,-9.995922,0.902966,4.337683,1.179057,0.459089,7.172859,0.643736,0.447707,1.043641,7.116994,5.485510,8.391869,4.825041,-3.332075,-4.028698,-9.599266,8.528072,6.849447,-4.106327,1.104373,0.126480,1.322753,8.185832,-4.046902,-7.408652,-0.229350,-3.224099,-5.173491,-2.998718,-3.161198,-4.028102,4.444992,-5.641580,-0.818897,-0.121985,7.542221,-1.742947,-6.133180,6.738348,-2.299347,4.040603,8.687351,8.723400,8.351602,-0.661850,-7.675926,-5.311823,-1.031782,-0.587350,-2.686524,5.897359,-9.727047,-1.376442,9.704868,7.953931,8.202322,-1.467770,0.419438,-9.572722,1.997072,-2.912912,9.268898,8.256754,-9.284756,-0.698179,-6.002295,-5.326707,-0.320539,-0.299365,-2.390273,3.914554,-4.583079,-0.597709,2.576484,-6.265950,5.393875,-8.565195,4.255373,-5.162702,2.766695,-2.234909,-8.903341,-0.764312,5.995223,-2.198599,9.358122,3.419545,7.242194,2.849266,1.059441,8.884573,-6.148154,8.139693,-7.563867,3.076567,3.886410,5.749060,-2.551170,-7.842711,-5.431817,5.849054,-3.886845,7.311173,-1.056069,7.933177,-3.694161,-7.002527,-1.838454,5.755937,-7.511590,8.789636,-6.809090,8.491803,-2.062635,2.097542,7.625401,-0.939903,2.668072,6.973139,-4.589562,6.645214,-9.339533,-7.007038,-5.850292,2.977073,-6.761109,-9.246938,1.908193,-2.161931,8.552510,5.510552,-0.109781,-1.358934,0.039440,-2.809083,-8.497909,4.388163,3.235243,-3.579927,8.150640,-8.404140,-3.354442,-1.614689,9.835947,4.370832,-1.469074,5.334172,6.240879,2.956890,7.580030,-7.651731,6.415797,-7.524922,2.234805,-2.597267,-0.778329,1.142560,5.603139,0.765693,-1.359941,0.537227,1.449934,6.457524,3.286020,6.381974,-3.506556,-9.500414,0.203971,4.690183,5.835355,3.583078,-4.355948,-4.444952,0.608697,-3.835316,7.803320,-9.621281,-3.111061,2.698504,-1.029384,4.062314,-1.038422,5.596807,-7.004612,9.231553,-3.220373,-1.968422,7.624208,1.191933,-6.289932,-9.624194,4.784333,-9.702802,-5.930793,0.919350,-4.771323,-9.789875,3.709579,5.857117,-6.250428,5.199488,5.385120,0.681687,5.851799,5.273637,4.580176,7.200648,8.488645,-0.060369,8.129698,-3.385392,-4.473718,-4.253271,-9.349892,-8.475262,-2.708435,-9.385716,8.798818,-9.445591,-6.663308,-8.719016,8.672479,-9.160534,3.152978,7.312403,8.120297,-5.931901,-8.785447,9.975078,-7.551777,6.431766,0.715120,3.930756,2.224061,6.190605,2.081968,0.549426,8.324692,8.611687,9.604357,3.513454,2.874365,-8.954728,2.742451,-8.211775,0.039043,-5.293952,5.700681,7.502579,-6.921480,-1.672977,-1.023619,-0.298823,-0.222911,-0.684491,-7.054968,-7.655748,-3.120130,7.755534,-3.506420,9.335305,8.634859,-1.167853,2.016561,-8.519040,1.629330,-1.198333,-9.188147,7.642967,-7.900306,-0.891702,-6.676173,-3.112531,-1.767330,-0.969178,-8.884999,-7.133420,5.115699,-0.884420,6.071559,-9.281222,-6.995853,-6.153137,-4.501342,5.970461,-1.731888,2.259184,-4.990862,3.253415,-3.787347,5.775430,3.378339,-5.662548,-0.296019,-4.745671,2.355199,-9.870357,5.084954,4.056175,3.791455,-6.227880,-8.964130,-5.279995,-4.530075], dtype = "float32")#candidate|5004|(546,)|const|float32
call_5002 = relay.TupleGetItem(func_4806_call(relay.reshape(var_5003.astype('float32'), []), relay.reshape(const_5004.astype('float32'), [13, 14, 3]), ), 0)
call_5005 = relay.TupleGetItem(func_4810_call(relay.reshape(var_5003.astype('float32'), []), relay.reshape(const_5004.astype('float32'), [13, 14, 3]), ), 0)
output = relay.Tuple([call_4994,call_5002,var_5003,const_5004,])
output2 = relay.Tuple([call_4995,call_5005,var_5003,const_5004,])
func_5012 = relay.Function([var_5003,], output)
mod['func_5012'] = func_5012
mod = relay.transform.InferType()(mod)
mutated_mod['func_5012'] = func_5012
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5013 = relay.var("var_5013", dtype = "float32", shape = ())#candidate|5013|()|var|float32
func_5012_call = mutated_mod.get_global_var('func_5012')
call_5014 = func_5012_call(var_5013)
output = call_5014
func_5015 = relay.Function([var_5013], output)
mutated_mod['func_5015'] = func_5015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3913_call = mod.get_global_var('func_3913')
func_3914_call = mutated_mod.get_global_var('func_3914')
call_5034 = relay.TupleGetItem(func_3913_call(), 0)
call_5035 = relay.TupleGetItem(func_3914_call(), 0)
var_5040 = relay.var("var_5040", dtype = "float64", shape = (14, 15, 9))#candidate|5040|(14, 15, 9)|var|float64
bop_5041 = relay.floor_mod(call_5034.astype('float64'), relay.reshape(var_5040.astype('float64'), relay.shape_of(call_5034))) # shape=(14, 15, 9)
bop_5044 = relay.floor_mod(call_5035.astype('float64'), relay.reshape(var_5040.astype('float64'), relay.shape_of(call_5035))) # shape=(14, 15, 9)
output = bop_5041
output2 = bop_5044
func_5048 = relay.Function([var_5040,], output)
mod['func_5048'] = func_5048
mod = relay.transform.InferType()(mod)
mutated_mod['func_5048'] = func_5048
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5049 = relay.var("var_5049", dtype = "float64", shape = (14, 15, 9))#candidate|5049|(14, 15, 9)|var|float64
func_5048_call = mutated_mod.get_global_var('func_5048')
call_5050 = func_5048_call(var_5049)
output = call_5050
func_5051 = relay.Function([var_5049], output)
mutated_mod['func_5051'] = func_5051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3880_call = mod.get_global_var('func_3880')
func_3881_call = mutated_mod.get_global_var('func_3881')
call_5053 = relay.TupleGetItem(func_3880_call(), 0)
call_5054 = relay.TupleGetItem(func_3881_call(), 0)
uop_5056 = relay.sin(call_5053.astype('float32')) # shape=(14, 15, 9)
uop_5058 = relay.sin(call_5054.astype('float32')) # shape=(14, 15, 9)
func_4620_call = mod.get_global_var('func_4620')
func_4621_call = mutated_mod.get_global_var('func_4621')
call_5071 = func_4620_call()
call_5072 = func_4620_call()
output = relay.Tuple([uop_5056,call_5071,])
output2 = relay.Tuple([uop_5058,call_5072,])
func_5088 = relay.Function([], output)
mod['func_5088'] = func_5088
mod = relay.transform.InferType()(mod)
mutated_mod['func_5088'] = func_5088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5088_call = mutated_mod.get_global_var('func_5088')
call_5089 = func_5088_call()
output = call_5089
func_5090 = relay.Function([], output)
mutated_mod['func_5090'] = func_5090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3880_call = mod.get_global_var('func_3880')
func_3881_call = mutated_mod.get_global_var('func_3881')
call_5231 = relay.TupleGetItem(func_3880_call(), 0)
call_5232 = relay.TupleGetItem(func_3881_call(), 0)
func_2998_call = mod.get_global_var('func_2998')
func_3001_call = mutated_mod.get_global_var('func_3001')
const_5256 = relay.const(-1, dtype = "int16")#candidate|5256|()|const|int16
var_5257 = relay.var("var_5257", dtype = "int16", shape = (2912,))#candidate|5257|(2912,)|var|int16
call_5255 = relay.TupleGetItem(func_2998_call(relay.reshape(const_5256.astype('int16'), []), relay.reshape(var_5257.astype('int16'), [13, 14, 16]), ), 0)
call_5258 = relay.TupleGetItem(func_3001_call(relay.reshape(const_5256.astype('int16'), []), relay.reshape(var_5257.astype('int16'), [13, 14, 16]), ), 0)
uop_5276 = relay.atanh(call_5255.astype('float64')) # shape=(13, 14, 16)
uop_5278 = relay.atanh(call_5258.astype('float64')) # shape=(13, 14, 16)
func_4301_call = mod.get_global_var('func_4301')
func_4304_call = mutated_mod.get_global_var('func_4304')
call_5279 = relay.TupleGetItem(func_4301_call(relay.reshape(const_5256.astype('int32'), [])), 0)
call_5280 = relay.TupleGetItem(func_4304_call(relay.reshape(const_5256.astype('int32'), [])), 0)
func_4167_call = mod.get_global_var('func_4167')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_5283 = relay.TupleGetItem(func_4167_call(), 0)
call_5284 = relay.TupleGetItem(func_4169_call(), 0)
func_4053_call = mod.get_global_var('func_4053')
func_4054_call = mutated_mod.get_global_var('func_4054')
call_5292 = relay.TupleGetItem(func_4053_call(), 0)
call_5293 = relay.TupleGetItem(func_4054_call(), 0)
output = relay.Tuple([call_5231,const_5256,var_5257,uop_5276,call_5279,call_5283,call_5292,])
output2 = relay.Tuple([call_5232,const_5256,var_5257,uop_5278,call_5280,call_5284,call_5293,])
func_5294 = relay.Function([var_5257,], output)
mod['func_5294'] = func_5294
mod = relay.transform.InferType()(mod)
mutated_mod['func_5294'] = func_5294
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5295 = relay.var("var_5295", dtype = "int16", shape = (2912,))#candidate|5295|(2912,)|var|int16
func_5294_call = mutated_mod.get_global_var('func_5294')
call_5296 = func_5294_call(var_5295)
output = call_5296
func_5297 = relay.Function([var_5295], output)
mutated_mod['func_5297'] = func_5297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4167_call = mod.get_global_var('func_4167')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_5307 = relay.TupleGetItem(func_4167_call(), 0)
call_5308 = relay.TupleGetItem(func_4169_call(), 0)
output = relay.Tuple([call_5307,])
output2 = relay.Tuple([call_5308,])
func_5319 = relay.Function([], output)
mod['func_5319'] = func_5319
mod = relay.transform.InferType()(mod)
mutated_mod['func_5319'] = func_5319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5319_call = mutated_mod.get_global_var('func_5319')
call_5320 = func_5319_call()
output = call_5320
func_5321 = relay.Function([], output)
mutated_mod['func_5321'] = func_5321
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5417 = relay.const([[[-6.500781,-2.951575,9.275382,3.850033,-5.522451,-4.659112,-0.600521,5.953075,-1.082861,-9.772718],[9.552009,-4.935945,1.781349,-7.614262,-8.945718,3.841631,-5.379104,0.817884,-5.755861,4.442661],[-6.813344,6.898980,-5.961355,-4.677316,3.996644,-5.810708,3.942548,-0.134113,7.411164,-2.963886],[-7.022185,-0.358338,7.882298,-4.097064,5.698924,8.738998,-0.460774,-4.149692,5.954385,6.590466],[9.371551,-7.804333,-4.762422,-6.637122,1.274148,-7.266572,-1.953331,-1.851983,-2.486363,8.110926],[-5.917708,1.780723,9.335475,7.838222,-2.612021,-3.457147,-7.890585,-0.338858,5.247743,0.082275],[-3.528604,-2.000988,-6.145229,-4.247578,9.252793,-1.316996,-5.938235,-4.696406,0.017442,8.920184],[-0.691143,-5.343944,-6.827018,-4.907199,4.983583,-2.180170,0.076712,-3.502730,6.640220,-4.831535],[9.779008,-3.897734,-8.380298,8.600045,-0.148047,8.176624,-1.345523,-5.548140,-6.426255,-3.998807],[-0.326025,1.216729,8.364154,2.741647,8.181185,-6.663459,0.206924,-8.886405,2.879024,7.683518],[-5.876671,4.332256,-7.153553,3.906089,-8.893859,-1.412705,-5.420299,-3.167594,-0.227800,-9.746547],[8.706023,-5.248371,1.174104,-2.250102,-5.932602,5.796098,-7.735906,-5.465234,-8.856822,3.357533],[4.034773,4.127870,-7.544940,-7.629633,8.070167,-2.114299,4.357102,6.334355,3.912549,8.872667],[-0.318865,5.996669,1.165494,3.663362,1.212875,-6.412502,4.648857,4.647665,8.912887,-4.162665]]], dtype = "float32")#candidate|5417|(1, 14, 10)|const|float32
var_5418 = relay.var("var_5418", dtype = "float32", shape = (6, 14, 10))#candidate|5418|(6, 14, 10)|var|float32
bop_5419 = relay.less_equal(const_5417.astype('bool'), var_5418.astype('bool')) # shape=(6, 14, 10)
output = bop_5419
output2 = bop_5419
func_5426 = relay.Function([var_5418,], output)
mod['func_5426'] = func_5426
mod = relay.transform.InferType()(mod)
var_5427 = relay.var("var_5427", dtype = "float32", shape = (6, 14, 10))#candidate|5427|(6, 14, 10)|var|float32
output = func_5426(var_5427)
func_5428 = relay.Function([var_5427], output)
mutated_mod['func_5428'] = func_5428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mod.get_global_var('func_4689')
func_4690_call = mutated_mod.get_global_var('func_4690')
call_5437 = relay.TupleGetItem(func_4689_call(), 2)
call_5438 = relay.TupleGetItem(func_4690_call(), 2)
func_4949_call = mod.get_global_var('func_4949')
func_4951_call = mutated_mod.get_global_var('func_4951')
call_5449 = func_4949_call()
call_5450 = func_4949_call()
func_1202_call = mod.get_global_var('func_1202')
func_1204_call = mutated_mod.get_global_var('func_1204')
const_5452 = relay.const([True,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,False,False,False,True,True,False,True,False,True,False,False,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,False,False,True,False,False,True,False,False,False,False,False,False,False,True,False,False,True,True,True,True,True,True,True,True,False,True,True,True,False,True,False,True,True,True,True,True,True,True,False,True,True,False,True,False,False,True,False,True,False,True,True,True,True,False,True,True,True,False,True,False,True,True,True,False,False,False,True,True,True,True,True,True,False,False,True,False,False,True,True,False,True,False,False,False,True,True,True,False,True,False,False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,False,True,False,True,True,True,True,True,False,True,True,False,True,False,True,False,True,True,True,False,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,False,True,True,True,True,True,False,True,False,False,False,False,True,True,True,True,True,True,False,False,True,True,False,True,True,True,False,True,False,False,True,False,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False,False,False,True,False,True,False,False,False,True,True,True,False,True,True,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,False,False,False,False,True,False,True,True,False,False,False,True,True,True,True,False,True,False,True,False,True,True,True,False,False,False,True,True,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,False,False,False,True,False,True,True,True,True,False,False,True,False,True,False,True,True,False,False,True,True,True,False,True,False,True,False,False,True,True,False,True,True,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,False,True,True,True,True,True,False,True,True,True,True,False,False,True,True,False,True,False,False,True,True,True,True,False,True,True,True,False,True,False,False,True,False,True,False,True,False,True,False,True,False,True,True,False,True,True,False,False,True,False,True,False,False,True,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,True,False,True,True,True,False,False,False,False,False,False,True,False,False,True,True,True,False,True,True,True,False,True,False,False,False,False,False,True,False,False,True,False,True,False,False,True,False,False,False,False,False,True,False,True,False,True,False,False,False,True,True,False,False,True,False,False,True,True,False,True,True,True,False,False,True,False,False,True,False,False,True,True,True,False,False,True,True,False,True,False,True,False,False,True,True,True,False,False,False,False,True,True,True,True,True,False,True,True,True,False,True,False,True,False,False,True,True,False,True,False,False,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,False,True,True,False,False,True,False,True,True,False,True,False,True,False,True,False,False,True,False,True,False,False,False,False,False,False,False,False,False,False,True,False,True,False,False,True,True,True,False,True,True,True,True,False,False,False,True,False,True,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,True,False,False,True,True,False,False,True,False,True,True,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,True,False,True,True,False,False,True,True,False,False,True,True,True,True,True,False,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,False,False,False,False,True,False,True,False,True,True,True,False,False,False,True,False,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,True,True,False,True,False,False,False,True,True,True,False,True,False,False,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,True,False,True,False,True,True,True,True,True,False,True,False,False,False,True,True,True,True,True,True,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,False,False,False,False,True,True,True,False,True,True,True,False,False,False,False,True,True,False,True,True,False,False,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,False,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True,False,True,True,False,True,False,False,True,False,True,True,True,False,True,False,False,False,False,False,False,True,True,False,True,True,True,True,False,True,True,True,True,False,False,True,True,False,True,True,False,False,False,True,True,False,True,True,False,True,True,False,False,False,True,False,True,False,True,True,True,False,False,False,False,False,True,True,False,False,False,False,True,True,True,False,True,False,True,True,False,True,False,False,True,True,False,True,True,True,False,False,True,True,False,True,True,True,True,False,True,True,False,False,False,False,False,True,False,False,True,False,True,True,True,False,False,True,True,True,True,False,True,False,True,True,False,False,False,True,False,True,False,True,False,True,True,False,False,True,False,True,False,True,False,True,False,False,False,True,True,True,True,False,False,False,True,False,True,True,True,True,True,True,False,True,False,True,True,True,True,False,False,True,True,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,False,True,True,True,False,False,False,True,True,False,False,False,False,False,True,True,True,True,True,True,False,False,False,False,False,True,False,True,False,False,True,True,True,True,False,True,True,True,False,False,True,False,True,True,True,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,False,True,False,True,False,True,False,True,False,True,True,True,True,False,False,False,True,False,True,True,False,False,True,True,False,True,True,True,True,True,False,True,False,True,False,False,False,False,True,False,True,False,True,True,True,True,True,False,True,False,True,True,True,False,True,True,True,False,False,False,True,False,True,True,True,True,True,True,True,False,True,True,True,False,False,False,True,True,False,True,False,True,False,True,True,True,False,False,False,False,False,True,False,True,True,False,False,False,True,True,True,True,False,False,True,False,False,True,False,False,False,False,True,False,True,False,False,True,False,False,True,False,True,True,True,False,True,True,True,True,False,False,False,True,False,True,True,False,False,True,False,False], dtype = "bool")#candidate|5452|(1248,)|const|bool
call_5451 = func_1202_call(relay.reshape(const_5452.astype('bool'), [8, 13, 12]))
call_5453 = func_1202_call(relay.reshape(const_5452.astype('bool'), [8, 13, 12]))
output = relay.Tuple([call_5437,call_5449,call_5451,const_5452,])
output2 = relay.Tuple([call_5438,call_5450,call_5453,const_5452,])
func_5489 = relay.Function([], output)
mod['func_5489'] = func_5489
mod = relay.transform.InferType()(mod)
output = func_5489()
func_5490 = relay.Function([], output)
mutated_mod['func_5490'] = func_5490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5088_call = mod.get_global_var('func_5088')
func_5090_call = mutated_mod.get_global_var('func_5090')
call_5544 = relay.TupleGetItem(func_5088_call(), 0)
call_5545 = relay.TupleGetItem(func_5090_call(), 0)
output = relay.Tuple([call_5544,])
output2 = relay.Tuple([call_5545,])
func_5548 = relay.Function([], output)
mod['func_5548'] = func_5548
mod = relay.transform.InferType()(mod)
mutated_mod['func_5548'] = func_5548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5548_call = mutated_mod.get_global_var('func_5548')
call_5549 = func_5548_call()
output = call_5549
func_5550 = relay.Function([], output)
mutated_mod['func_5550'] = func_5550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3880_call = mod.get_global_var('func_3880')
func_3881_call = mutated_mod.get_global_var('func_3881')
call_5558 = relay.TupleGetItem(func_3880_call(), 0)
call_5559 = relay.TupleGetItem(func_3881_call(), 0)
func_4011_call = mod.get_global_var('func_4011')
func_4014_call = mutated_mod.get_global_var('func_4014')
var_5569 = relay.var("var_5569", dtype = "float64", shape = (48, 2))#candidate|5569|(48, 2)|var|float64
call_5568 = relay.TupleGetItem(func_4011_call(relay.reshape(var_5569.astype('float64'), [96,])), 0)
call_5570 = relay.TupleGetItem(func_4014_call(relay.reshape(var_5569.astype('float64'), [96,])), 0)
uop_5575 = relay.tan(var_5569.astype('float64')) # shape=(48, 2)
uop_5584 = relay.erf(uop_5575.astype('float32')) # shape=(48, 2)
func_3776_call = mod.get_global_var('func_3776')
func_3778_call = mutated_mod.get_global_var('func_3778')
call_5588 = relay.TupleGetItem(func_3776_call(), 0)
call_5589 = relay.TupleGetItem(func_3778_call(), 0)
output = relay.Tuple([call_5558,call_5568,uop_5584,call_5588,])
output2 = relay.Tuple([call_5559,call_5570,uop_5584,call_5589,])
func_5597 = relay.Function([var_5569,], output)
mod['func_5597'] = func_5597
mod = relay.transform.InferType()(mod)
var_5598 = relay.var("var_5598", dtype = "float64", shape = (48, 2))#candidate|5598|(48, 2)|var|float64
output = func_5597(var_5598)
func_5599 = relay.Function([var_5598], output)
mutated_mod['func_5599'] = func_5599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mod.get_global_var('func_4689')
func_4690_call = mutated_mod.get_global_var('func_4690')
call_5604 = relay.TupleGetItem(func_4689_call(), 0)
call_5605 = relay.TupleGetItem(func_4690_call(), 0)
output = call_5604
output2 = call_5605
func_5618 = relay.Function([], output)
mod['func_5618'] = func_5618
mod = relay.transform.InferType()(mod)
mutated_mod['func_5618'] = func_5618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5618_call = mutated_mod.get_global_var('func_5618')
call_5619 = func_5618_call()
output = call_5619
func_5620 = relay.Function([], output)
mutated_mod['func_5620'] = func_5620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3913_call = mod.get_global_var('func_3913')
func_3914_call = mutated_mod.get_global_var('func_3914')
call_5626 = relay.TupleGetItem(func_3913_call(), 0)
call_5627 = relay.TupleGetItem(func_3914_call(), 0)
output = call_5626
output2 = call_5627
func_5641 = relay.Function([], output)
mod['func_5641'] = func_5641
mod = relay.transform.InferType()(mod)
mutated_mod['func_5641'] = func_5641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5641_call = mutated_mod.get_global_var('func_5641')
call_5642 = func_5641_call()
output = call_5642
func_5643 = relay.Function([], output)
mutated_mod['func_5643'] = func_5643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4949_call = mod.get_global_var('func_4949')
func_4951_call = mutated_mod.get_global_var('func_4951')
call_5658 = func_4949_call()
call_5659 = func_4949_call()
output = relay.Tuple([call_5658,])
output2 = relay.Tuple([call_5659,])
func_5660 = relay.Function([], output)
mod['func_5660'] = func_5660
mod = relay.transform.InferType()(mod)
mutated_mod['func_5660'] = func_5660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5660_call = mutated_mod.get_global_var('func_5660')
call_5661 = func_5660_call()
output = call_5661
func_5662 = relay.Function([], output)
mutated_mod['func_5662'] = func_5662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mod.get_global_var('func_4689')
func_4690_call = mutated_mod.get_global_var('func_4690')
call_5674 = relay.TupleGetItem(func_4689_call(), 0)
call_5675 = relay.TupleGetItem(func_4690_call(), 0)
uop_5676 = relay.erf(call_5674.astype('float32')) # shape=(14, 15, 9)
uop_5678 = relay.erf(call_5675.astype('float32')) # shape=(14, 15, 9)
func_4726_call = mod.get_global_var('func_4726')
func_4727_call = mutated_mod.get_global_var('func_4727')
call_5681 = relay.TupleGetItem(func_4726_call(), 0)
call_5682 = relay.TupleGetItem(func_4727_call(), 0)
output = relay.Tuple([uop_5676,call_5681,])
output2 = relay.Tuple([uop_5678,call_5682,])
func_5689 = relay.Function([], output)
mod['func_5689'] = func_5689
mod = relay.transform.InferType()(mod)
output = func_5689()
func_5690 = relay.Function([], output)
mutated_mod['func_5690'] = func_5690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5548_call = mod.get_global_var('func_5548')
func_5550_call = mutated_mod.get_global_var('func_5550')
call_5761 = relay.TupleGetItem(func_5548_call(), 0)
call_5762 = relay.TupleGetItem(func_5550_call(), 0)
func_4593_call = mod.get_global_var('func_4593')
func_4596_call = mutated_mod.get_global_var('func_4596')
var_5764 = relay.var("var_5764", dtype = "int16", shape = (1456, 2))#candidate|5764|(1456, 2)|var|int16
call_5763 = relay.TupleGetItem(func_4593_call(relay.reshape(var_5764.astype('int16'), [2912,])), 2)
call_5765 = relay.TupleGetItem(func_4596_call(relay.reshape(var_5764.astype('int16'), [2912,])), 2)
func_5426_call = mod.get_global_var('func_5426')
func_5428_call = mutated_mod.get_global_var('func_5428')
var_5772 = relay.var("var_5772", dtype = "float32", shape = (840,))#candidate|5772|(840,)|var|float32
call_5771 = func_5426_call(relay.reshape(var_5772.astype('float32'), [6, 14, 10]))
call_5773 = func_5426_call(relay.reshape(var_5772.astype('float32'), [6, 14, 10]))
func_5660_call = mod.get_global_var('func_5660')
func_5662_call = mutated_mod.get_global_var('func_5662')
call_5785 = relay.TupleGetItem(func_5660_call(), 0)
call_5786 = relay.TupleGetItem(func_5662_call(), 0)
uop_5788 = relay.sigmoid(var_5764.astype('float64')) # shape=(1456, 2)
output = relay.Tuple([call_5761,call_5763,call_5771,var_5772,call_5785,uop_5788,])
output2 = relay.Tuple([call_5762,call_5765,call_5773,var_5772,call_5786,uop_5788,])
func_5790 = relay.Function([var_5764,var_5772,], output)
mod['func_5790'] = func_5790
mod = relay.transform.InferType()(mod)
var_5791 = relay.var("var_5791", dtype = "int16", shape = (1456, 2))#candidate|5791|(1456, 2)|var|int16
var_5792 = relay.var("var_5792", dtype = "float32", shape = (840,))#candidate|5792|(840,)|var|float32
output = func_5790(var_5791,var_5792,)
func_5793 = relay.Function([var_5791,var_5792,], output)
mutated_mod['func_5793'] = func_5793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5548_call = mod.get_global_var('func_5548')
func_5550_call = mutated_mod.get_global_var('func_5550')
call_5833 = relay.TupleGetItem(func_5548_call(), 0)
call_5834 = relay.TupleGetItem(func_5550_call(), 0)
var_5843 = relay.var("var_5843", dtype = "float32", shape = (14, 15, 9))#candidate|5843|(14, 15, 9)|var|float32
bop_5844 = relay.power(call_5833.astype('float32'), relay.reshape(var_5843.astype('float32'), relay.shape_of(call_5833))) # shape=(14, 15, 9)
bop_5847 = relay.power(call_5834.astype('float32'), relay.reshape(var_5843.astype('float32'), relay.shape_of(call_5834))) # shape=(14, 15, 9)
func_4784_call = mod.get_global_var('func_4784')
func_4787_call = mutated_mod.get_global_var('func_4787')
const_5857 = relay.const([[-9.223503,-2.680240,-5.310424,-3.704281,7.251296,0.464501,0.105496,-4.583459,-3.082117,-9.697763,-5.248930,5.370710,2.307565,-8.499276,-7.323651,2.457258,-5.458518,8.412756,-2.334064,0.965384],[9.920313,0.535900,-8.191787,-9.629458,-3.256525,-8.034284,-7.541121,-1.060836,-8.493761,3.591478,-1.865795,-0.307597,-4.688967,0.110883,3.118031,4.616932,1.909046,-4.790988,-4.086734,2.194667],[9.078469,4.849391,8.810357,3.217212,-5.942756,-9.771789,6.269607,8.706197,-1.219139,-2.134941,5.545972,8.805272,2.291869,-7.452345,-8.190408,-0.723419,1.851192,8.292768,6.374539,5.023521],[9.648793,8.526921,-2.762793,3.349538,0.959752,-2.763718,7.242671,-1.127393,4.313102,-3.713776,-1.662519,1.455386,-7.689897,-8.294902,1.408213,6.762506,7.862819,6.915259,6.754231,-2.185066],[4.280804,8.376785,-4.673994,1.988217,-8.889146,6.351592,-7.969908,0.486348,7.716079,-2.468362,5.875263,-2.557558,-1.895404,-9.921108,-9.676658,2.563433,7.860331,-5.237087,-7.486641,-8.463003],[4.406315,6.331888,-7.993957,-4.689555,-2.914081,8.308954,-0.567838,-9.870876,2.989669,-6.526333,6.345490,6.374910,-3.205639,6.879563,4.193453,2.024624,1.211381,-2.729005,5.336190,-5.200339],[-7.304812,7.254173,7.439576,1.796569,-5.049175,-8.713938,3.407206,9.627209,8.433370,-6.808745,-3.640047,1.735501,-6.402602,1.920964,-4.541580,5.564825,7.721877,2.270096,-4.141383,-2.018578],[-6.601181,6.244520,-1.448771,6.488357,2.538194,3.063978,9.268354,3.141862,-6.570368,-6.875276,-0.303278,9.900707,-5.087670,-6.095901,-0.348405,-5.783311,3.659395,-6.289546,-7.480279,4.805130],[-4.289818,5.935871,6.306352,3.711749,1.179901,-1.993604,-8.154693,-7.422053,-8.605042,7.360737,5.229998,1.615375,1.199401,-2.281954,0.391859,4.366129,-1.189715,-2.530709,-8.324808,-8.360830],[6.588936,5.857348,-6.111912,-8.983497,2.438278,1.263994,0.868910,4.572800,5.143711,-2.296635,-9.978673,-3.712618,-0.592368,-7.779505,-6.121574,4.875607,-4.956249,9.073011,-5.968758,5.009230],[-9.319212,-5.023951,-2.197287,-5.514828,2.885941,-2.064467,2.805751,0.471098,1.702372,-3.064955,-1.439263,4.931550,-2.524937,1.453794,9.136472,-2.879028,-1.694419,2.967819,3.661739,-4.231833],[5.731446,-6.690349,5.866675,-9.853026,0.907433,-1.275492,-2.451422,-2.799636,3.403524,0.915538,3.160216,-6.912595,-8.879512,-7.451133,6.775931,9.031414,6.212355,0.181359,1.636273,-2.100297],[-8.517942,-2.922619,-8.284149,-5.118380,-3.709897,-8.410098,8.324266,9.478677,6.810097,7.097487,-0.399458,7.839985,-8.103969,-6.523334,-4.595588,9.034024,-5.898991,-0.496561,-0.163861,-6.126451],[-1.111384,-9.206330,0.498096,-9.442580,1.668609,6.314287,-3.194375,-8.683023,-4.135362,-3.611335,0.551191,9.291323,6.011981,-5.273465,-3.857372,-3.484925,-0.275050,8.603262,0.164754,-7.501452],[6.556928,-7.000521,-8.965959,6.688109,-2.748400,3.526897,7.172173,5.438335,-9.797656,-7.998354,-0.481544,-4.668617,-1.721391,-5.939882,0.246187,-5.001448,-1.086685,-1.207769,0.020061,0.256223],[2.008811,9.886848,-9.964837,3.437289,0.892466,3.778097,-5.254479,-6.463055,9.043608,-1.194679,4.477599,-6.278594,-0.358699,-8.840059,-6.199657,3.795869,-1.591175,-4.430494,6.314481,-3.427840],[0.740130,-9.765371,4.273571,-8.685168,7.811572,9.372324,-8.685532,-3.651166,-4.601327,-8.644869,4.887658,-0.924828,9.430164,-1.219224,-6.866791,4.085833,-4.147041,9.160611,-5.357604,9.683527],[5.258761,-2.646469,-7.392040,-2.097670,9.197678,6.734698,-0.679202,-9.107444,-6.882786,-7.469310,4.986132,-2.153835,4.556466,8.916217,-7.872891,3.238922,8.254533,2.156886,-9.529702,-2.418257],[-2.595134,-9.336886,4.565202,-3.695379,3.552863,-7.664159,-1.208806,5.829007,8.732748,2.594777,8.634819,4.556973,-9.619641,-8.829404,-8.281603,-1.532548,-7.986411,4.122007,-9.092632,2.659727],[-3.142282,-9.747838,-1.051457,-2.319461,7.257813,4.694015,-7.805588,1.496847,9.676610,2.090155,3.111297,8.559257,5.420165,8.962164,-9.988117,7.540786,6.806991,-2.858324,5.386791,6.931616],[-9.712914,4.870861,2.549062,-9.048070,-8.954956,-9.444978,9.409387,2.901663,-3.406945,-7.981196,4.402758,2.691970,-1.981950,1.679602,-0.061240,-6.697439,3.748684,1.877784,-0.233120,-0.538022],[4.633686,-4.916748,-4.858440,5.517054,6.533606,1.916458,-6.192160,3.721410,-2.847924,-6.588157,8.076903,-9.592872,1.309213,6.333529,9.074950,-8.137116,-0.505701,0.880485,6.720889,3.629601],[6.740272,9.327746,6.231585,-7.311818,5.055013,-6.545854,1.052751,-3.899991,-7.661875,-5.379476,0.242473,-6.287824,-6.063126,-7.545965,4.444660,-8.580748,-1.252806,-5.587233,-9.446571,-5.382762],[1.942553,-6.250755,5.363577,9.388333,-6.045598,6.638173,7.935273,8.464454,2.965792,9.380607,0.899498,7.984170,2.098060,5.852566,-2.930709,-1.221075,-1.821070,-5.838741,8.797678,6.997520],[-4.419920,1.971051,-9.062202,5.966711,-7.116849,-5.760520,-0.861591,4.713342,3.171106,4.956394,-8.262158,-3.183820,-7.136008,-8.601507,-6.493170,6.997586,-5.915640,-8.263259,2.725778,0.928425],[-6.177299,1.437449,8.051846,1.224846,7.756705,0.783282,-4.104928,-4.487693,-9.839119,-3.656367,-5.491935,0.287237,-3.863172,2.209591,0.615252,9.724397,0.660789,-1.463475,1.609665,6.995091],[-4.207871,0.452203,-0.370934,3.331407,-8.141427,-8.228675,2.676049,-6.023781,1.588924,3.920921,-2.998794,1.601258,3.875251,-9.806442,5.749179,4.439767,-4.438772,-2.195480,-7.748644,-8.903212],[7.712474,3.539269,-9.678944,-3.427866,-2.547848,3.663066,-3.395153,-7.183149,-2.232857,-1.123823,-5.943744,-5.707494,-1.720432,-1.319424,-7.762591,-6.690410,1.047084,8.154943,5.499431,5.028994],[1.449968,-2.383056,0.107691,-2.413069,5.385779,4.232008,-8.886384,0.571352,-1.746289,-3.651333,-4.434985,-8.813490,-1.997942,2.379935,9.209544,5.611210,6.375814,-7.050012,-3.808083,4.320514],[-3.680486,-5.214603,-5.974531,4.281623,5.538945,4.597016,-9.762455,6.438067,7.702133,-6.260402,4.516310,-0.555703,5.203225,-2.310921,6.841637,-8.888416,-8.644805,-1.071433,-6.545212,-1.417344],[7.269971,3.985058,8.953612,2.023757,5.464435,-5.415163,8.021860,-9.414459,2.422587,3.220881,-6.095559,-4.807925,-4.753270,4.443062,4.124690,-2.788519,9.115788,-3.462304,-2.574418,-4.066848],[-1.203661,-7.235207,1.329428,-8.229500,4.923272,9.971047,8.352707,4.972762,-0.432409,-7.021481,-5.762121,0.474375,-2.159288,-1.673256,8.733596,6.295811,7.012319,6.503187,-4.861380,-8.392022],[8.546731,9.525695,8.591641,-2.219409,3.972312,8.638156,9.052613,5.527984,7.955742,-5.416310,-7.590274,-5.708460,-0.446774,-1.153050,9.128175,-3.481382,-4.491421,-7.039849,-2.026826,-5.646883],[0.289803,4.114364,-2.882482,5.684479,7.700411,-0.755453,4.924183,5.095876,-9.133684,-9.925072,-5.400158,8.465384,-4.340190,7.228989,-4.506151,-7.206108,9.221337,2.995367,-4.954907,6.896253],[-1.685688,-1.924024,-5.131628,0.967889,8.457885,0.393113,5.229187,5.058750,-8.266005,-0.494302,-6.098538,-2.478849,9.107501,5.851413,-2.642427,7.663988,-5.552786,-3.208016,9.563523,9.461109],[6.132892,8.157351,0.717291,-1.186798,1.099929,6.683346,1.321879,0.753802,1.705934,1.623581,-3.625502,-9.406569,-2.154620,4.204534,3.629720,-9.808517,9.730026,0.772401,-8.234195,-3.983917],[-5.488315,3.751758,-4.910604,-4.515020,8.778090,3.006631,-2.098416,-4.279128,0.423392,9.821903,1.890373,6.306496,9.567292,3.960104,4.097572,3.432938,4.501602,4.003432,6.954728,6.646114],[2.535451,-6.781210,9.481131,-0.585787,2.565753,4.750780,-3.728051,3.634056,9.489982,9.289073,8.537467,-0.056314,-2.369408,-3.027819,-1.746042,-9.421322,-4.721616,2.277732,-7.220709,-2.559917],[8.286829,-8.590241,4.741290,8.835696,-4.822508,9.838365,5.882919,3.080459,7.007054,-8.792077,7.070655,-7.800197,9.229296,3.353376,9.686375,3.771390,4.473778,-1.397221,-6.431271,6.224473],[6.939790,-0.791507,4.261805,-3.185972,6.937072,-2.027816,1.845070,-7.734763,-5.732879,-4.586618,-8.032563,9.726041,1.075382,-6.935613,2.725852,3.945990,-8.234239,-7.113479,6.989364,-4.964286],[0.947038,7.284792,8.041373,0.527703,-0.920242,-7.888697,-8.539756,-6.827235,2.191838,8.195208,2.936650,0.793329,-4.058378,1.949996,-1.299734,-1.082378,-0.250484,8.133702,7.277964,9.010114],[-7.127979,-3.063006,1.351115,4.034613,6.639094,-8.533103,4.788226,-8.946050,5.623065,5.925529,-2.729273,8.587642,7.376806,-3.259828,8.818329,-5.244948,9.898992,-6.312021,-9.852817,-3.794771],[-6.170250,-2.959212,-9.778358,3.781532,-1.216042,-5.180633,-0.762932,7.341454,-0.093103,9.970219,2.056909,0.414211,-9.137635,-2.899338,9.641811,0.828246,0.683708,8.114365,-8.875617,2.475416],[7.790855,9.989028,6.214405,-9.414472,6.271152,2.581771,7.841432,5.224727,3.193084,-3.396186,-5.589502,-7.800486,2.247055,-9.237450,8.056147,-1.398691,9.754167,-7.790550,-7.371528,-0.674458],[-4.921177,7.410772,-8.177038,-6.643497,-1.626199,3.784898,-0.564376,-2.195529,0.246947,1.877353,-8.078793,-6.619829,-6.620687,-0.025596,2.196229,-5.872849,-8.958285,2.534098,-3.570716,-7.102425],[6.376137,-0.313991,-5.411749,7.704044,7.863938,-6.511326,2.958255,4.609535,0.610088,-8.460751,-4.029576,7.098416,-7.056722,8.688948,-9.770118,8.741656,3.830979,0.848788,-6.963290,-3.389879],[7.123716,5.072928,8.973940,-5.559503,-2.212658,0.689885,2.653250,-6.056583,3.965280,8.898172,1.509868,3.708583,-8.430552,-1.644261,-4.912961,-5.403169,7.545218,-4.806203,-2.784431,-0.675434],[7.557044,8.859042,-4.616467,7.866200,4.691773,8.193135,5.130278,-5.684977,6.491386,9.780751,7.520116,4.473533,2.593017,7.554059,8.381912,1.569464,2.862129,4.102525,-8.292257,5.667036],[5.057735,-5.672213,-5.893490,-6.021297,-5.873468,3.415997,0.637693,-1.326459,-2.555178,-0.827465,6.924021,-9.404915,-8.948599,-9.544467,-6.236410,2.840567,-3.563498,4.179713,-5.671511,-8.648480],[1.805426,-8.883074,2.457818,4.820432,-5.152111,8.432872,4.365484,-2.208777,8.220634,-5.168021,-0.864360,-4.434640,-9.033412,5.810702,3.708644,1.969044,3.757651,-1.562588,-9.449755,-1.322417],[1.190314,8.628146,-2.487648,0.022357,-8.210459,7.755709,3.951961,-1.846655,5.997666,-4.032122,4.571768,1.944235,3.935863,3.515195,-7.305248,-9.438455,1.402634,-4.850561,2.711516,-5.564784],[-9.806886,-4.937609,3.965090,6.098163,7.894977,1.722966,1.747856,9.345058,-1.953353,-9.739170,4.977171,6.001447,-3.392946,-8.880041,2.394494,-3.460524,-4.264076,7.756903,0.949092,7.485912],[-4.110014,5.991872,7.589432,-6.287281,-6.109432,-0.315843,7.100367,-7.107098,-9.944478,0.696026,7.677546,7.211090,-8.669266,8.319267,3.888920,-1.883521,-9.219591,2.014512,2.952164,4.176236],[-3.377873,3.554022,6.776486,-9.676772,-5.436108,5.065930,2.577143,5.059766,5.985496,3.520158,3.576133,-9.021582,3.452897,-9.308182,0.402300,-7.013705,4.451516,6.210106,-4.257117,-9.689405],[4.207025,-6.572788,-3.278639,1.898946,1.447836,-4.004916,-7.621659,-3.269966,-9.740909,-2.023542,-8.515379,-5.659282,-4.420150,9.762676,7.454953,7.270200,5.410393,7.911673,-9.468559,-5.871616],[9.461238,-3.486039,0.937591,8.951962,1.327525,-3.036453,1.945018,-4.000303,-0.605607,-2.018875,9.738164,6.761341,7.129111,2.181676,7.249002,5.423022,-2.641575,-9.194952,-4.024571,-3.171014],[-7.173254,-3.038722,9.556491,6.859549,-3.381130,6.859805,-9.787644,-6.349095,3.904030,7.760255,9.774792,2.816488,-5.855002,-9.242681,8.346151,1.082375,0.252123,4.073292,-7.537068,-4.702790],[-3.752220,-9.917725,-7.424976,3.913797,-0.502563,-0.071257,8.592959,-1.462424,-4.169881,6.027213,3.782999,3.022664,-2.787288,4.076905,3.888110,6.541825,0.251662,-6.506536,-7.220587,9.809027],[-2.964405,7.836704,4.174243,-1.110957,-7.580029,2.844095,-0.453360,-9.867333,-4.518794,7.918164,7.301776,6.324818,-5.400071,7.552630,0.062695,-9.017673,-1.325051,-8.132811,9.617866,0.531027],[-3.416770,7.976774,8.747092,0.008574,7.252333,-3.864617,6.356507,9.857989,3.933936,-7.012662,7.937319,5.372980,-4.143953,8.646527,-7.630056,7.236081,6.150452,1.821477,-1.616691,-7.091831],[1.616802,6.644784,9.524413,-4.920011,2.222692,8.646339,5.102459,-1.497485,-7.128428,8.302394,8.227502,6.179741,4.989315,5.450194,9.285991,8.599092,-1.251770,4.714145,8.767064,5.837940],[1.396802,7.057208,4.245903,-0.705582,3.716336,-8.223555,5.267348,-7.757302,-8.235515,-2.313584,2.798236,-5.161795,-5.650244,2.051341,5.095189,-2.562365,-0.828286,-4.666876,-2.984275,3.044504],[-7.855918,-8.550601,-7.180275,1.639964,-2.337937,-3.179298,7.242469,-5.697653,0.921264,-8.578490,-1.887667,4.097960,-4.436943,-0.630570,-5.992869,6.543367,0.386197,-7.722371,-4.866991,-1.064842],[-1.500240,-5.689045,0.918112,5.270979,9.890867,1.702765,9.650679,-8.264250,-5.184755,-9.943532,-6.428442,-1.242806,1.316759,1.597898,-4.923268,-0.400586,3.684126,-9.663598,3.830482,6.635033],[5.516488,-2.566296,9.753500,3.114638,0.935772,-8.782479,5.314512,7.990634,-5.352030,-3.091419,-3.457033,8.447544,2.100414,-3.207057,0.787576,0.381681,7.127410,8.771121,-6.423268,-8.194682],[-0.653041,-8.907118,1.526286,-0.346636,-0.159294,-1.354211,-9.050262,-5.135205,-0.428580,-5.767826,-3.370316,-7.669158,-8.321247,-5.418801,-4.414197,-2.567087,-6.523070,-0.274398,3.997359,7.831169],[6.996413,-8.496141,6.026326,-7.775411,-6.739755,3.077710,-8.263914,-7.289098,-4.993991,-8.950610,7.568932,1.808816,8.914301,-8.174114,6.094286,-1.547112,5.177966,-0.745563,-4.675742,-9.811814],[0.189373,0.423496,-1.616850,-3.312882,3.900353,5.276210,-7.006958,-3.391810,7.852896,-8.546354,-5.742676,8.790227,0.939407,-1.805400,-5.590539,-9.835509,-5.271850,-4.896163,3.998185,8.422365],[4.565708,-5.483157,-0.135103,2.466872,8.619481,-1.193295,-2.269925,9.343658,7.919753,5.318369,9.488526,3.496422,-0.114389,-2.843054,6.550499,-7.399275,-4.140664,-3.213982,3.900847,-0.003473],[6.172118,-9.632750,7.488280,1.166545,9.896837,-3.824155,3.175512,-7.587261,3.786056,3.968651,9.357552,6.102279,-0.669403,-9.149530,2.690995,-6.764088,9.437499,4.433082,3.418930,3.638178],[4.745430,7.168286,1.224018,-9.385766,-8.846942,5.779235,7.004078,3.508140,-0.360923,5.677539,4.292548,-5.072304,-4.452868,6.995064,0.872554,-2.656541,-4.786213,7.342580,-5.035752,3.671606],[8.886163,-6.421326,8.769806,6.882065,5.186788,-2.297064,-9.894408,1.185708,-2.850373,-8.822997,8.392223,-3.512878,-9.641828,1.169230,-8.124981,1.855454,-1.765334,-4.824191,-3.196013,6.698180],[3.060991,-5.053885,5.909832,-9.911547,-4.366740,5.737344,-6.726381,7.319579,5.427971,9.061668,5.080356,2.899226,-5.709881,-3.434107,6.434343,-3.361154,5.916293,1.078970,-2.482336,-7.730535],[-2.061734,-4.559099,0.025501,-7.945276,-3.106981,-0.374576,-3.677125,5.892661,-9.865180,4.703566,-4.753186,-7.016214,-4.485316,-7.547343,0.532401,5.648998,-3.871256,-7.504358,-8.219874,-8.744437],[-6.378012,-3.875941,-0.958066,2.154388,9.853610,9.676924,-5.141522,9.202864,7.594720,6.437610,-2.336730,-7.165393,-9.675617,4.878217,5.833382,-3.749229,-5.174605,0.216524,-1.409491,6.469455],[2.913144,6.516185,-0.970785,6.941236,-7.491079,1.255317,7.765507,1.506414,-2.764242,-3.629453,-1.606943,-1.594167,-3.547443,-5.034517,-1.608488,-5.221407,-8.326365,-3.409333,1.954617,-6.281495],[-6.152432,-6.002595,5.921227,-8.331941,-4.651022,-5.168220,1.571119,-6.162015,-1.295952,-6.267237,-9.799449,-6.049076,0.366970,-1.146573,-7.630309,-9.947257,-2.979363,6.646977,7.681399,1.612050],[-7.050828,-4.469959,-6.767220,5.177292,8.241056,-2.810092,7.599308,-6.389918,3.330181,2.955016,4.300452,-5.072131,-1.281918,-9.397256,6.228170,-2.234121,9.468680,0.679686,0.555855,-0.114563],[1.501914,-9.798596,3.523510,4.279613,3.911351,6.685954,-3.753604,-0.438525,1.263811,-5.442450,0.991463,-8.614654,-1.105873,-7.043036,7.763892,-1.119152,6.969784,4.481958,-6.892913,9.693571],[3.331803,-5.717048,1.107255,-0.046799,3.389954,1.897797,8.110083,2.275665,-6.556430,7.832129,-2.865490,-0.650029,2.432560,5.002899,-1.040777,4.754464,9.095300,8.951546,7.762040,3.947074],[1.665915,1.044453,-2.766850,-5.811874,-4.722935,-4.144276,2.862177,3.554421,-8.983934,-9.571676,7.001828,-3.490957,-6.243445,8.927047,-4.710091,-6.035150,-3.379971,-8.134436,9.522235,0.529726],[6.442037,-2.106125,-4.298065,0.832480,-2.198508,3.010842,2.954181,-6.810183,2.450275,9.790566,-3.093013,8.446321,0.047262,-5.690320,-9.264608,9.784609,3.691377,1.216097,6.933556,9.931739],[-0.444982,5.767919,-0.847890,9.414566,-5.260996,2.846385,3.267713,4.863369,0.568884,9.577357,2.768811,5.147241,-7.738074,-3.410670,5.005198,-2.590055,-6.788786,2.931184,5.232040,-9.305254],[-5.658089,7.123856,5.516758,-6.708588,-5.284009,-7.842224,-2.995044,-0.090568,-9.870394,-0.565180,-7.073427,-5.435832,6.737065,-2.697938,-5.370293,-1.464657,-4.407485,-3.567438,-4.359656,-8.535327],[-4.201482,-4.987255,-4.610664,-6.001551,3.128747,-8.615925,1.077038,-6.388759,9.937985,7.843709,4.368841,-4.065133,5.089278,6.158796,8.206114,-2.928209,0.498694,9.969613,-5.089165,-5.891044],[-2.438216,0.736277,1.729548,-3.312618,-1.242078,4.097564,9.285480,-9.033545,-2.830766,-5.455510,7.063849,-4.679183,0.871150,8.225576,2.276108,1.887496,-5.528720,5.084929,-1.864621,-4.108813],[9.201794,3.525872,1.268069,-7.215666,2.304768,-5.638468,5.145998,6.080110,-2.101966,-9.455758,6.114480,8.547790,9.376940,4.428941,5.642245,-2.491934,3.601060,2.764591,7.308315,9.047096],[0.118820,-2.163977,-8.471203,2.336741,-0.312348,-0.063281,-7.837077,8.657498,-0.230734,6.835944,0.772532,-5.901016,9.739374,6.824067,7.169377,-8.068291,-2.556469,-0.898146,-5.671716,7.650986],[6.744639,-1.991092,-5.502510,9.259089,2.462207,-1.775556,3.385694,6.402950,-1.997981,5.283951,1.174079,-5.911843,-9.576828,-2.559199,6.857451,5.228017,4.965371,-1.930791,-7.095917,-0.264272],[-3.510038,-1.522293,-2.701202,9.563582,-4.327998,-1.240232,-0.954922,-3.557480,5.109902,1.732625,-3.178411,-1.825549,2.386773,4.698022,-2.691906,0.487190,-3.987945,-6.515336,4.675469,-5.026736],[8.743566,-9.981681,9.463345,-5.988509,7.105493,8.781944,1.308111,-2.283615,-0.649117,-6.452227,3.453325,-9.394034,3.083717,-7.352484,-6.419260,-1.926413,-2.679874,5.379774,2.063142,-1.076380],[6.025953,0.273290,7.432299,8.262457,7.545497,4.927915,5.860846,3.390762,-0.045045,-0.732584,-5.884961,-3.486456,8.301089,-9.791019,-4.355283,2.563481,6.284646,-6.736083,-8.653278,-6.836602],[7.083628,1.062918,1.522911,0.783307,-9.223245,-7.373721,-7.447304,7.064630,-4.230538,4.768063,6.246432,3.981508,6.357165,1.954985,7.776143,1.415015,7.715703,-9.655356,6.349547,4.588623],[3.916434,-1.339752,-7.505567,4.195267,-4.747173,5.985349,3.980651,-2.268406,-9.975363,3.915063,4.897926,-6.751568,1.237933,-1.389749,-1.483173,-1.625169,6.930113,-2.392280,5.733673,9.708371],[-8.040433,1.982142,6.832654,-8.116411,1.342354,6.985557,-3.552665,-6.594672,-4.728484,9.194934,-5.008531,-1.928609,-8.590189,0.516128,-7.181358,3.145969,-4.946821,6.075378,-3.960963,4.073629],[4.389908,3.440110,7.059401,3.494671,-8.504083,-7.137043,-0.490173,-4.775854,1.542427,-1.035646,-6.296735,-9.556517,-9.634214,-6.289962,6.608900,9.884902,6.226424,3.321708,-7.087650,-2.049250],[5.757599,8.228107,-3.259562,-2.077228,9.956822,7.432604,6.893447,-6.145296,1.544064,-3.739145,2.557163,7.357197,-6.763596,4.938579,6.950842,7.272354,-0.363742,2.994366,4.373586,0.081771],[-6.485496,-6.406520,-5.872033,-8.473600,-5.180267,9.389970,-6.434565,-3.988032,6.709461,0.937023,8.086660,4.955222,7.173349,-1.684242,-6.619958,4.437033,7.278752,-4.592100,5.427680,9.994861],[-0.315594,9.071504,-7.291162,2.473161,0.573139,-1.344486,-1.986882,-5.479072,-3.916599,-3.497893,-4.777661,-3.842217,8.441664,-7.275906,6.832590,-9.307924,-8.207550,-2.182294,5.702053,-9.424535],[-1.735459,-6.077507,-5.232653,-6.426872,1.154051,3.738582,-4.858357,6.395819,6.616108,-2.087655,-9.284162,-7.755241,-9.906587,0.696285,-3.721120,-9.142849,-3.653321,2.470212,-3.720649,-0.708616],[-6.196462,4.502901,8.353181,9.634988,-4.843994,6.847573,-4.206043,1.584963,-2.693316,0.649775,-5.369761,8.510861,-7.049145,2.798912,-7.294900,-6.976278,-1.263984,5.107851,7.632229,-3.384932],[2.477146,-9.198589,1.983131,-7.621304,-7.370503,-3.474146,-2.756607,2.378096,4.662492,3.835114,-0.630904,-8.041814,8.277738,-3.878100,-3.958614,2.011002,-3.001970,-4.043612,0.416855,5.265032],[-7.196644,3.245899,6.827666,0.521920,7.121433,-9.202965,-7.210916,-0.716511,3.819516,-1.515713,3.251586,4.615004,7.403189,6.959592,-2.147309,-4.306659,9.041925,2.684073,4.094994,4.560098],[5.226214,-6.764396,-5.924096,-5.873622,-9.370069,-3.326590,-1.297795,9.616953,6.818364,-1.010567,-6.126944,-5.777849,-7.722509,-2.725305,-4.387879,2.788762,-8.383189,3.374387,-4.386200,-8.908623],[0.006875,2.596080,-1.377294,3.772340,0.960005,2.265751,3.630624,6.153789,-7.735351,6.184581,5.884617,-0.611861,-1.695729,4.195000,3.563328,2.810249,-5.376296,-9.840021,-6.810410,-3.688624],[-7.050460,7.823572,2.100498,5.572332,-3.954160,-3.021410,8.746108,5.853355,-2.170951,6.992539,-7.751424,-1.981858,1.064758,8.112599,2.384251,9.072298,-8.054772,4.036253,-1.096703,6.184251],[5.595090,-7.570941,-3.495684,-9.298151,-6.675707,0.113210,7.830630,9.718167,-4.968470,-2.452377,-0.269325,1.845506,-5.523132,-2.702195,-4.630790,6.706417,6.503963,-6.915409,-7.620356,1.444282],[-7.540593,4.898897,-8.732137,-3.584583,-0.032539,-3.714264,8.072579,6.090788,-2.927681,-3.733513,8.221899,-3.457052,5.243573,-5.285572,-9.039977,1.188598,-4.643646,-6.516154,1.668097,-2.091786],[3.251633,0.303974,-2.822733,-8.122904,-5.344917,7.033271,-7.327118,3.519216,0.051976,5.012323,7.079235,-2.442581,-5.844854,-9.364791,-9.648482,9.484748,-7.987108,-2.451779,7.998359,8.944950],[6.878585,9.956325,7.675633,7.334745,-9.633826,-9.038022,8.191447,-7.725560,1.087667,-5.622365,5.712259,8.598271,-2.032440,-8.759083,-6.506855,3.888027,9.475990,0.902115,6.597521,1.320301],[-3.263259,2.065190,-5.309787,9.565027,6.892416,9.964290,9.785952,-6.740449,-4.107409,5.631854,-4.554972,-1.286170,0.802107,-9.070079,8.995105,-5.224784,1.832380,4.051745,2.266646,7.227135],[-0.652547,4.863123,0.667731,2.727942,4.410133,-0.074964,-6.294223,3.090053,3.842177,-1.913691,3.086866,-8.808430,3.021680,-6.708658,-3.129306,2.099905,5.775344,-5.022563,-5.829610,-8.736722],[-8.460201,2.787565,-4.581049,-9.069702,0.443302,-5.508433,5.472033,6.607145,-4.988578,-5.105366,-7.319193,-0.590804,-6.270114,-3.272482,-4.204231,-1.613188,-6.957814,1.925683,-5.364129,-5.982907],[8.691188,-2.691323,6.257026,7.916548,-7.601997,-2.527272,2.550399,-6.982654,5.162080,-4.487775,1.421029,-1.154535,-5.575888,-4.884449,5.882784,-2.767273,1.429832,9.656909,6.503190,9.585536],[-7.411227,-7.247950,-9.600139,-9.831945,5.943686,5.857992,1.019794,-1.749562,-8.779838,3.067881,3.932247,-1.548569,-9.703857,8.920099,-4.943702,2.615635,-4.770376,-6.053693,-4.580060,-0.481108],[8.274848,6.503107,2.167987,-1.740072,-4.721076,5.341701,-6.393226,3.658351,-2.147536,-1.101862,7.369320,4.632028,6.779883,-2.094545,-9.154265,4.716393,-7.924523,5.147236,1.667273,4.670165],[9.728822,4.014429,-6.043589,-8.572933,-3.331643,9.062123,7.922830,2.455949,-0.724158,-4.245115,4.266707,-8.337355,-8.963945,2.166982,-2.474828,-5.345004,-1.524742,3.371047,-2.293077,8.532614],[-1.579425,-4.805421,0.341437,-1.062786,5.006751,6.071580,-8.031999,-9.030171,2.268786,-7.282185,4.982943,2.266742,0.970003,-7.010658,-9.381088,-3.432708,2.954130,-9.183485,-2.090430,-5.109870],[-3.648689,-2.717609,-9.480733,4.118793,9.730750,2.906917,-1.216520,-0.123514,4.603498,4.559251,-0.731120,-4.579109,-2.724412,-2.808680,8.941321,-8.162641,-8.631797,-0.535832,-5.785246,-7.362837],[-2.889452,-2.972776,-6.609769,-7.645541,1.138529,-5.841359,8.763254,4.989308,1.017405,-4.361844,4.048510,-4.632732,-6.089992,-9.524092,4.402728,-3.736190,-5.493037,-7.548677,3.406100,-6.898504],[0.129406,-8.748811,8.088960,-0.833923,9.213340,9.608649,-1.134723,8.414565,-3.384237,4.990297,-2.168560,3.482671,-4.661501,-9.623838,-4.490288,-1.436868,5.002466,-8.920659,6.267457,8.774380],[-6.892691,4.172328,9.182503,7.151371,-3.939336,1.350128,-2.630741,1.710146,-7.366898,-9.504804,-6.328389,-3.710781,9.221569,-1.219007,-7.598278,9.917881,-7.677643,2.552327,4.124105,4.217152],[6.585305,8.224259,-3.484832,-4.507837,-3.730214,5.990642,4.267627,-5.986524,5.671770,1.141695,-9.444687,-8.958788,4.988336,-5.035821,-0.274253,-8.123721,-2.839043,7.362889,-3.584276,-9.347985],[-1.068567,4.414444,5.510227,-1.597050,-9.469669,-1.196358,-4.514401,1.355359,-9.332098,7.049107,-1.256812,-7.402166,7.596864,2.038700,8.856112,-6.185881,4.177249,-0.635467,4.629801,8.249537],[-3.843509,-9.395357,-0.554606,3.215824,-9.820863,1.832520,-9.070763,2.247505,8.346167,-3.126067,-4.911374,-6.519886,-0.539639,2.969236,2.501945,-9.062492,-8.925174,2.364120,-9.574981,-9.936033],[0.044818,8.778134,4.563783,3.846978,9.619324,-7.955679,-0.985515,-1.565016,2.898373,-5.720443,-6.327440,-2.649501,8.903146,-9.689327,-1.815286,-3.129725,-2.580914,-0.826813,2.288264,2.162085],[5.176628,-4.330535,-0.578540,-2.952579,-8.788418,4.575834,2.822694,-5.343635,1.605604,8.738110,4.985295,5.423267,8.359600,3.312009,8.471885,-4.222042,-6.717677,-6.819199,0.310540,-7.175480],[9.770821,-1.043944,-7.589386,4.548935,9.472282,6.410587,8.282553,6.744288,-2.527719,4.746592,1.349130,-4.829008,-2.138222,-5.895156,-8.589244,-2.569093,-9.023172,-1.104533,8.603735,-9.403640],[-6.330584,3.110569,-2.581886,9.312726,8.552829,-3.360944,-1.440370,5.832163,6.101704,-9.170290,-3.109128,1.043664,4.173335,0.325474,-8.207770,-6.394612,-2.134284,-8.991940,-1.708708,2.826194],[-9.025133,-6.447909,4.214641,1.786719,8.797253,-5.086075,-0.792774,9.487814,2.236022,-4.906671,-7.980241,6.753682,-0.233995,-4.261136,8.580686,4.163189,8.185281,-0.175374,9.564339,-7.003040],[5.129315,-4.829382,-9.275542,6.539640,4.242306,9.069595,-2.353340,-4.642349,-9.550087,8.129566,-8.047716,4.695853,-6.549915,-0.078553,-1.245620,6.720230,8.838754,8.867589,2.693204,-9.168867],[5.492796,-7.515536,-1.987549,-5.010603,5.768581,-1.893238,-5.013515,-8.531641,2.503030,-0.236399,4.473538,0.959809,-9.519782,-4.156676,0.971003,-7.698972,1.269279,4.776239,3.006665,-0.781249],[0.090073,-1.040198,1.861768,2.194453,-3.244366,-5.998073,6.691963,-9.545683,-4.793544,0.617340,5.809403,-7.129887,-2.635064,-3.880214,-3.615599,9.434322,2.302795,6.037105,-1.410446,8.317142],[0.939566,-7.043700,3.026860,-4.689628,9.539234,-2.368497,5.115861,2.179463,-4.062973,5.032364,2.524880,-7.665008,-0.122144,1.880926,-4.350229,1.789783,-7.731328,-2.121198,2.803280,0.567097],[-5.479923,7.248767,4.419251,-3.804948,6.760390,-0.483847,-0.427776,7.392726,-2.004198,7.599612,-2.365722,-4.891242,-9.937975,-9.159318,3.605759,-9.985963,3.516936,7.983666,7.606507,-0.965363],[4.002140,3.852202,-2.367756,7.890429,5.037767,2.706949,1.033348,-3.371743,6.158240,3.773285,-6.190238,-3.135315,-1.494841,-8.985052,2.368945,-5.652166,9.222630,-1.842993,-2.574223,7.906186],[-6.491748,8.267891,-8.533973,3.505001,1.485438,9.653514,6.817948,1.048480,5.022682,9.635981,5.930524,-1.335204,8.019390,-1.705641,-2.558910,7.744349,-2.707931,-9.233472,-3.966875,-7.046215],[6.906910,9.221264,-5.999365,-9.473895,0.553286,-8.366076,7.238980,8.086652,-6.025316,-8.494409,4.697895,7.351526,7.006655,5.110045,-7.675543,2.447117,2.641378,-5.273976,6.499564,4.817147],[-9.551927,7.455349,-2.853367,-4.533410,-9.149956,2.655396,-7.290519,-6.379691,0.674602,0.853847,8.941446,4.235391,8.838281,-7.618347,-4.283789,0.618771,-0.705334,-3.700128,-1.948581,1.631545],[0.007337,-0.568243,3.300474,7.020099,-7.484128,-8.876628,7.699578,-5.000301,5.809005,-1.587378,5.639492,-6.498339,-5.176804,-0.545659,2.191141,-2.491045,8.162249,-4.204825,1.683989,6.276863],[-2.638548,2.213313,8.903811,3.873356,7.527877,-9.909303,8.866549,-2.658600,6.648703,-4.484269,-6.362377,8.194107,-5.844553,-4.953383,-1.872144,1.085811,-8.453476,-1.389128,3.122108,-2.128007],[8.209827,3.803810,-6.521943,4.577372,-1.345118,-9.897476,-2.858908,-3.394952,-3.986220,-5.590204,-5.192295,0.035687,-9.864655,-3.365481,0.290991,-1.523130,1.872638,-9.067691,3.873982,5.257605],[8.720964,-3.315139,-1.465097,-0.521651,-1.997933,1.402916,0.237572,3.922058,-2.952976,3.106856,-9.367728,5.598845,4.427487,0.834300,9.720748,-1.976599,4.502633,-4.044071,-1.108103,-5.381134],[5.245639,5.659427,-0.227643,-6.963155,2.044681,7.120503,-1.171537,3.785459,-0.117394,-2.284855,-5.903561,-8.237532,-0.345407,0.223650,-1.166131,8.580082,2.754593,-0.572114,2.168067,-9.766869],[-7.774261,-6.617093,-6.398557,-7.989691,9.637157,-6.130894,8.350521,1.455079,5.226318,-1.545355,-9.776306,9.712934,0.411714,6.938681,3.085967,6.874599,4.612540,-5.034304,5.040454,-5.747213],[8.330942,-1.401023,-1.268402,-2.052453,-0.283170,7.271700,-6.971939,-2.742927,-2.470350,-0.674949,-9.315541,0.759657,-3.566164,9.164515,-0.063011,-3.902249,7.483942,-3.700178,-0.549444,0.975959],[-6.763994,2.831691,-6.079059,-8.203356,9.442496,-3.017830,-8.777022,-0.481757,6.494747,-8.799481,6.262705,9.968076,-2.527808,-5.138088,4.869288,8.949126,-2.262941,-7.352517,6.432628,1.067855],[-9.358012,-1.208781,6.719558,0.058718,-0.767102,-0.137281,-6.221263,-8.563218,-8.224077,8.299247,8.587372,9.062206,1.529789,-2.253851,-9.133019,6.310720,2.959691,0.459466,-7.332200,6.959921],[-9.431310,5.671380,7.951668,2.656446,-3.189052,2.878165,-0.589660,-9.596729,6.000382,-3.497771,-6.721196,-2.674616,7.786209,9.309941,-5.970138,-3.431747,-5.652227,0.347930,-4.294576,6.701384],[7.108557,-4.735874,0.983242,0.872124,1.739739,-9.426845,8.123135,5.088958,-6.851931,4.869951,0.024568,-3.841509,0.916904,7.804100,-7.383198,-6.787323,-1.796880,9.338938,8.067445,-1.107997],[-1.537398,8.829439,1.791909,-2.124332,0.280910,-9.734277,-2.700245,-5.422112,-8.609277,8.314349,5.433039,-9.266883,-4.479440,2.922384,-6.681867,-6.849603,2.098253,-0.704546,-7.347244,-0.888274],[-1.697561,-4.746599,8.203669,-7.258994,-6.596895,6.303334,-2.093019,7.603353,4.711102,-3.097657,-8.360112,4.805235,-1.080200,-9.414624,-1.568765,-6.528771,4.700747,2.079170,-5.325818,-9.528740],[0.070591,-9.057064,9.081579,-0.106255,-9.109310,-8.181531,0.346940,-3.108274,-7.088577,-8.375026,-1.207694,9.439919,4.016035,-4.494625,1.868274,8.269820,-7.750985,-9.486402,8.543117,6.228455],[0.782259,1.343812,2.057383,8.890466,-4.016637,-9.167585,-0.039267,0.816408,1.503263,1.429633,-0.257648,8.731519,-6.106821,6.520470,2.781258,-7.494628,-2.359617,7.140418,3.620882,6.053556],[9.620575,-6.415279,-5.879168,5.965241,-4.123282,-4.554852,4.335527,9.982327,8.536701,-2.133580,1.521607,1.638891,-8.592853,9.222753,5.696841,2.730367,5.452822,3.313107,8.826191,3.365408],[9.710384,6.060054,4.981767,4.285586,5.365099,3.066592,-6.951789,-5.875742,-7.187296,-5.244196,1.404417,-8.720592,-5.791513,-9.769187,-2.771983,4.293578,7.942279,0.944201,3.695295,6.983617]], dtype = "float32")#candidate|5857|(156, 20)|const|float32
call_5856 = relay.TupleGetItem(func_4784_call(relay.reshape(const_5857.astype('float32'), [3120,])), 0)
call_5858 = relay.TupleGetItem(func_4787_call(relay.reshape(const_5857.astype('float32'), [3120,])), 0)
output = relay.Tuple([bop_5844,call_5856,const_5857,])
output2 = relay.Tuple([bop_5847,call_5858,const_5857,])
func_5860 = relay.Function([var_5843,], output)
mod['func_5860'] = func_5860
mod = relay.transform.InferType()(mod)
mutated_mod['func_5860'] = func_5860
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5861 = relay.var("var_5861", dtype = "float32", shape = (14, 15, 9))#candidate|5861|(14, 15, 9)|var|float32
func_5860_call = mutated_mod.get_global_var('func_5860')
call_5862 = func_5860_call(var_5861)
output = call_5862
func_5863 = relay.Function([var_5861], output)
mutated_mod['func_5863'] = func_5863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5618_call = mod.get_global_var('func_5618')
func_5620_call = mutated_mod.get_global_var('func_5620')
call_5878 = func_5618_call()
call_5879 = func_5618_call()
output = call_5878
output2 = call_5879
func_5926 = relay.Function([], output)
mod['func_5926'] = func_5926
mod = relay.transform.InferType()(mod)
output = func_5926()
func_5927 = relay.Function([], output)
mutated_mod['func_5927'] = func_5927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5641_call = mod.get_global_var('func_5641')
func_5643_call = mutated_mod.get_global_var('func_5643')
call_5936 = func_5641_call()
call_5937 = func_5641_call()
output = call_5936
output2 = call_5937
func_5941 = relay.Function([], output)
mod['func_5941'] = func_5941
mod = relay.transform.InferType()(mod)
mutated_mod['func_5941'] = func_5941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5941_call = mutated_mod.get_global_var('func_5941')
call_5942 = func_5941_call()
output = call_5942
func_5943 = relay.Function([], output)
mutated_mod['func_5943'] = func_5943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5319_call = mod.get_global_var('func_5319')
func_5321_call = mutated_mod.get_global_var('func_5321')
call_5971 = relay.TupleGetItem(func_5319_call(), 0)
call_5972 = relay.TupleGetItem(func_5321_call(), 0)
func_5689_call = mod.get_global_var('func_5689')
func_5690_call = mutated_mod.get_global_var('func_5690')
call_5974 = relay.TupleGetItem(func_5689_call(), 1)
call_5975 = relay.TupleGetItem(func_5690_call(), 1)
func_4167_call = mod.get_global_var('func_4167')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_5981 = relay.TupleGetItem(func_4167_call(), 0)
call_5982 = relay.TupleGetItem(func_4169_call(), 0)
func_5426_call = mod.get_global_var('func_5426')
func_5428_call = mutated_mod.get_global_var('func_5428')
var_5984 = relay.var("var_5984", dtype = "float32", shape = (840,))#candidate|5984|(840,)|var|float32
call_5983 = func_5426_call(relay.reshape(var_5984.astype('float32'), [6, 14, 10]))
call_5985 = func_5426_call(relay.reshape(var_5984.astype('float32'), [6, 14, 10]))
bop_5987 = relay.power(call_5983.astype('float32'), relay.reshape(var_5984.astype('float32'), relay.shape_of(call_5983))) # shape=(6, 14, 10)
bop_5990 = relay.power(call_5985.astype('float32'), relay.reshape(var_5984.astype('float32'), relay.shape_of(call_5985))) # shape=(6, 14, 10)
output = relay.Tuple([call_5971,call_5974,call_5981,bop_5987,])
output2 = relay.Tuple([call_5972,call_5975,call_5982,bop_5990,])
func_6001 = relay.Function([var_5984,], output)
mod['func_6001'] = func_6001
mod = relay.transform.InferType()(mod)
var_6002 = relay.var("var_6002", dtype = "float32", shape = (840,))#candidate|6002|(840,)|var|float32
output = func_6001(var_6002)
func_6003 = relay.Function([var_6002], output)
mutated_mod['func_6003'] = func_6003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5641_call = mod.get_global_var('func_5641')
func_5643_call = mutated_mod.get_global_var('func_5643')
call_6027 = func_5641_call()
call_6028 = func_5641_call()
uop_6033 = relay.tan(call_6027.astype('float64')) # shape=(14, 15, 9)
uop_6035 = relay.tan(call_6028.astype('float64')) # shape=(14, 15, 9)
func_4784_call = mod.get_global_var('func_4784')
func_4787_call = mutated_mod.get_global_var('func_4787')
const_6039 = relay.const([[-7.326800,-1.071300,3.995577,3.777241,-4.178620,2.884381,6.328162,-6.169785,0.465382,4.253280,-5.487918,1.310549,-9.594458,-8.774757,-5.428249,-1.231010,-9.073646,9.542796,-7.387686,-8.482262,5.952751,-7.410056,-5.450861,-9.170160,8.144324,0.761701,1.294313,4.318137,7.209099,8.262779,-9.895318,5.622714,-8.199123,-6.027854,4.105038,-8.692483,-3.993692,-4.444985,3.880214,7.160670,-8.220515,-8.015822,0.698926,6.770981,-6.371948,6.523567,-3.121435,7.739604,3.971753,-9.719012,-2.938544,1.003419,3.973542,0.629162,-6.503025,-2.032184,4.369331,1.465765,-2.466934,-9.896202,2.616404,-4.172721,-5.575009,-8.213942,9.047686,-6.421798,2.328859,8.057226,3.331484,-2.991206,5.894677,9.497506,3.874819,2.394705,0.754805,-4.926231,8.019470,6.654806,-1.495566,1.085289,-8.323852,-0.153097,7.826797,-1.638561,-3.851111,6.442070,4.141353,4.860592,7.566535,3.811288,-5.198011,6.995819,-0.352543,4.710866,-1.922200,-8.812475,-6.190393,9.692821,-5.231751,6.942659,-5.036611,-0.223025,6.489889,-0.076191,8.272668,7.148161,-9.944884,6.690637,3.244084,7.925825,-0.205743,-5.266185,-1.773353,-0.943271,-0.847580,-2.816736,-6.563696,-1.176368,-1.350546,-5.880524,-2.364861,1.823919,-8.960634,5.153829,7.078617,-6.563119,0.030790,-5.127600,-5.556421,-0.320665,-4.489344,9.594174,-2.102854,-1.094689,-1.800787,-5.355980,5.036513,1.640140,-2.623781,0.534699,-7.155155,6.682796,3.377446,1.407987,6.181617,-3.669063,-0.984241,-1.624749,1.033637,8.568209,-6.040376,8.530230,0.033565,1.865370,2.081458,3.874783,-9.657438,5.030679,9.148821,6.756606,2.016441,-3.273589,2.368420,-2.657208,-8.590313,6.266956,7.416282,-0.029335,3.322845,-4.889080,-5.054659,-1.441130,7.317774,-4.714582,9.043188,7.574282,6.132555,-5.530164,-7.310890,-0.771253,2.670260,8.753188,-4.306862,1.845671,-3.498547,-1.452457,-6.106642,7.963007,7.570935,-9.595115,-8.192067,4.176941,0.806771,-3.819526,-2.428762,-5.651300,-6.322050,-1.593636,6.114863,0.995983,5.452929,2.363294,-3.932995,4.922292,-6.747856,-9.131528,1.535599,2.182418,-5.418723,9.647272,-8.301243,-5.797061,6.311623,3.419608,-0.034993,-3.104698,-9.987306,4.849716,6.574226,-3.586262,-3.110787,-0.098451,-3.497296,6.062175,1.732479,0.128305,-0.388166,0.084770,-6.285834,2.254113,0.427542,2.123016,5.365235,-0.060692,7.966318,-7.489998,-0.840786,-0.934979,-4.935876,3.150226,-5.206182,8.561764,-7.990803,-3.467206,1.983987,3.643411,-8.065325,8.604795,-0.462473,-3.252887,-0.607609,7.937170,2.397268,-8.063421,1.448866,9.981534,-7.549388,8.048100,4.819346,-3.604694,7.132118,0.101639,-2.991718,7.320148,8.855333,-4.923190,-1.810077,-5.630930,2.733703,-2.410550,-4.185604,-5.792702,-5.656847,0.269023,-2.192585,8.174320,4.096300,1.714157,2.692592,-7.481016,-6.108950,-7.644939,3.110067,-8.843078,5.872511,5.036440,-9.279435,5.422738,5.566203,8.002093,-2.111200,0.283305,8.628549,0.221299,6.325737,7.544463,-0.915137,9.453345,-5.445433,1.971524,-9.783382,0.968318,-2.634777,1.954525,9.682883,3.514434,6.151094,-5.423002,3.135246,2.108530,9.486144,-8.120260,6.788024,9.186633,5.993195,3.568643,-9.786149,4.080985,6.371055,-3.432549,5.330612,-0.687685,6.902487,4.209444,-8.316123,0.647672,-4.204905,-8.031064,3.850055,1.169928,-5.343452,-5.233010,-1.809094,0.029581,3.359867,-9.828526,-8.785883,5.707370,7.795772,-5.301082,-3.684177,-8.886822,-3.204990,-6.733735,-4.402889,-9.320353,-5.166710,2.184703,-3.297853,6.510592,0.147657,-9.816540,-9.038081,9.372151,9.189793,-6.601113,7.418391,-6.321348,3.076669,-0.610290,-9.401042,-1.028433,8.389246,0.355566,-8.093272,5.728935,4.068938,3.817417,-4.236568,2.931661,7.433741,0.981754,-2.593647,-2.927998,-2.190346,-6.391388,2.305187,1.248295,-2.941253,1.183607,7.438617,-3.607236,-7.926199,6.315642,-7.182041,-2.412578,-1.908208,3.238157,5.395788,-0.722725,-3.386875,7.138696,0.088900,-1.089097,4.908551,-7.986161,9.921406,7.848970,3.814578,-8.186865,-3.070329,5.741088,-9.853015,6.748046,-9.904237,5.945027,-6.024544,-7.268509,8.919302,-7.836197,-8.010488,-1.948205,4.981343,-5.951052,-7.270452,2.949901,3.766814,2.027781,4.602273,-0.787229,-0.934157,-1.178452,-3.789747,-2.785665,1.425605,-2.755319,8.278700,6.201476,8.662890,0.415649,-1.687615,-4.452564,2.254176,7.597060,-5.866463,-4.555530,9.824952,-0.910384,-6.161740,-6.815845,1.373409,0.560914,9.234227,9.101522,-1.559012,-5.621011,8.538111,3.965785,-9.694365,7.311435,-8.248091,0.646120,-7.728286,0.998099,-6.352893,7.488025,-8.994546,-9.027372,4.268094,-9.676888,5.548837,2.263909,9.722180,0.473378,0.747228,9.292424,3.638128,-4.425145,-1.509931,-9.230913,2.744367,-6.979613,-3.559049,3.722935,-3.139930,-2.734640,-1.663538,4.656137,-0.479072,4.312103,2.480960,8.841968,4.065379,0.356730,7.476851,-0.901163,5.187905,-2.780423,7.621036,0.614484,-4.053706,4.388870,1.367665,-1.722199,-8.784969,-7.600422,-4.524396,-7.249073,4.521974,2.217828,7.294374,9.853761,-1.564018,-2.769159,0.593663,-9.863410,5.895404,-9.680923,-5.736851,-7.107198,-9.091921,-6.971247,-0.270013,-5.175009,-4.915742,-0.167152,1.115170,-2.774342,-0.254174,6.864035,9.654064,6.578371,-9.603682,3.025380,-8.846972,5.901620,-9.487586,-4.651137,-3.573699,-9.406462,-6.194875,-1.966156,-2.612248,-1.674721,7.582842,-3.891754,1.463707,-7.473420,9.152105,-1.005486,8.743797,-0.082104,0.056865,5.036726,8.708431,2.761782,-8.255122,5.368103,-1.573686,1.617902,-0.870947,-6.900843,4.129532,2.131056,1.572658,8.450309,9.178576,-0.938308,-6.181328,-3.818498,-7.828736,9.608484,9.554146,7.352338,-3.249511,7.825003,8.472694,-1.131672,-1.737622,3.569295,1.229661,8.958278,6.930469,-3.933314,8.534039,3.452883,-2.206037,-8.882569,-3.654899,5.258758,8.376089,3.102657,4.363577,2.095123,5.915964,4.114879,1.228643,8.609068,-5.514275,-5.940651,-8.508910,4.232926,3.264805,-4.176363,-0.525294,-5.029587,-7.842492,-5.076799,-6.757178,-2.618218,-3.533665,-2.019396,-0.146274,-5.209988,0.593307,-4.077555,6.786135,-2.238951,2.021842,-4.816075,8.376609,3.265105,-4.445270,4.999676,-1.115974,-6.625242,1.082290,-4.263102,-0.585043,-5.014695,-1.042499,8.016241,7.591988,-7.125044,-6.924897,-6.958718,8.604680,9.952748,0.736846,-7.077757,-0.266107,-6.135757,-6.836998,4.347673,-0.944900,-1.963048,-6.965423,-5.078785,-6.708595,3.502693,1.869590,-7.316312,3.950753,-8.580290,-8.879744,-5.496967,7.404863,-7.880801,-0.382950,-2.122694,6.403573,8.122017,-3.262784,8.285101,-4.343657,5.808200,-9.025433,-6.751668,9.364454,-0.120138,-6.107919,2.807498,-0.030835,1.190828,6.013154,9.055947,-2.109444,8.971868,-0.077834,4.061491,9.986803,-0.037329,-7.773555,6.113709,8.823975,6.414241,2.275181,0.547603,-6.817250,-5.979649,-6.264589,3.638510,-7.039028,9.564926,8.702911,2.439398,7.346092,0.190275,-5.171906,7.100972,-9.434099,5.852642,3.243621,6.693204,1.732574,-1.984806,0.781258,9.961657,-2.467325,-0.997324,7.114812,-6.912050,8.641417,8.730466,-1.225050,7.399541,6.887451,-3.874586,7.386804,6.865206,9.107060,-1.622108,6.445378,-3.473979,-3.253594,3.483111,-8.114744,-2.122654,7.060442,-2.396414,7.553871,1.236290,-9.528864,1.824289,3.286577,5.335164,-6.829356,-9.581341,3.494305,7.967042,4.286596,9.670314,-1.491939,-0.381606,8.984272,-3.545052,-2.214861,-8.869420,2.512851,0.916702,-0.987329,-4.085804,-3.359498,-9.632357,9.433869,-1.931731,-4.384883,3.872482,8.995158,8.122888,-4.888694,5.334695,0.717327,8.691862,-5.217552,2.169787,9.157023,3.997194,-8.926460,8.200001,-0.056075,6.917933,-2.413134,2.676119,-0.720029,-2.188704,-3.862867,8.690592,1.085234,9.948792,3.757725,-2.615840,-8.528486,7.225160,0.802123,-4.593608,-2.515544,5.361506,-1.182103,-5.836285,0.449392,7.720139,7.249746,4.889271,-5.947878,-5.919571,8.144064,-5.292149,-6.439624,7.876647,6.851841,0.037201,2.334598,-4.496768,-4.924423,-1.474709,2.298846,8.371032,-4.159141,-8.808143,1.598747,2.535625,4.957967,-4.874111,3.048405,-4.234044,-9.158103,-3.919701,-3.852912,9.340137,3.208709,-0.383122,-4.170352,5.417594,-3.751372,4.563623,-0.469604,-6.284040,-2.305121,-5.241560,-4.503210,-1.660408,-2.424963,-8.760754,1.255378,4.145550,4.476191,-0.109778,-9.767238,1.172469,5.132890,-9.946731,4.460166,8.767725,-5.127894,6.365130,-2.815630,6.222431,-5.290168,0.075853,6.493616,-9.296522,-6.601966,-3.720938,5.139843,2.048738,-3.870448,-9.250820,3.312050,-7.620510,7.346001,-6.092757,7.845306,2.507265,-4.581809,-3.105666,2.448389,-5.529758,0.585729,-6.625979,-4.034667,9.804310,-1.775076,-7.649542,6.549689,1.634950,-4.073846,7.876114,2.016880,8.087143,5.030607,6.128088,3.352450,7.368714,9.334740,6.568292,4.763683,-5.370831,-5.404629,8.556807,6.039598,0.444253,5.845596,-6.062566,8.070500,-3.514196,5.679667,5.186821,8.910752,0.201397,0.395794,1.420025,6.096872,-3.174226,-9.602397,2.195885,-3.865738,-7.334367,5.461705,-3.052792,-2.281970,-9.797238,-7.117926,-6.300274,-1.764427,-6.883327,-2.868947,-3.521879,-4.212101,-0.792424,3.679677,-2.686875,-6.946198,4.978849,8.198822,-8.060864,-3.651029,7.132279,-0.016828,-7.492341,2.385397,-5.832903,-9.554957,1.610736,2.886289,-4.768651,-4.148363,-1.196626,2.182311,-9.347049,6.297810,-8.142207,4.480170,5.983657,-8.518763,-3.057522,-4.927641,3.422407,-7.369072,1.399797,-5.665649,-4.171945,1.311633,2.120313,-0.914414,9.150232,-2.505943,4.072413,-9.048306,-8.121585,-7.683754,-7.644756,6.167125,-3.981287,9.376389,-2.452630,3.878523,-1.309134,7.491884,7.214728,3.734474,-2.285407,-3.867380,-9.425848,-1.363218,4.855044,9.063473,4.585103,-4.166169,-4.688225,-3.195409,6.217524,6.902959,-8.317974,-7.194284,-8.249736,-7.925873,4.817159,-9.477423,4.046589,-7.248363,-4.211946,2.545831,4.383456,0.093181,1.828380,-8.666617,0.079658,-6.235572,-2.511961,4.426712,-0.106155,0.185073,-3.417060,2.453966,-0.642866,4.698638,-0.471815,7.819721,-7.020094,8.007370,-4.503045,-2.927295,-0.346720,7.653473,2.787323,9.776266,-0.775879,-1.576446,2.470376,2.035096,1.299893,-7.586866,4.004467,8.575480,-7.242244,4.566196,-8.704447,-5.929632,-0.110843,-6.373629,-8.618999,5.693274,-2.369853,1.721734,-7.206618,-2.374040,2.637153,5.226326,-6.906228,-5.877151,1.299300,7.263965,-9.270634,-9.068635,6.518071,-5.114300,3.543808,-4.196056,6.395013,4.067720,-6.685534,-3.179251,-7.083059,-4.560661,-7.196112,9.228746,-9.827532,-1.017625,-4.428663,4.382869,0.990809,7.199855,-2.333647,-0.946775,6.397791,8.468389,8.084809,-8.549831,7.622877,-5.671598,7.329026,9.637310,-7.621656,-2.788812,6.925998,-4.954579,-0.623907,0.953134,-7.369014,-6.778098,3.971130,0.778942,7.350418,-8.061377,0.932746,0.484869,-7.074314,-2.788035,-9.821840,8.439180,2.849740,-1.890051,6.023542,-2.782881,5.980139,2.703039,-8.760301,-7.648317,-5.914736,-7.913812,4.903379,3.757904,-5.145071,8.462234,-7.753527,-8.372735,-6.192642,0.286013,-3.895394,5.597033,7.627410,-2.748474,-5.795571,1.826885,8.563284,-6.388671,9.499433,-8.933323,8.313085,-4.394766,-4.817612,5.654812,0.063435,-6.776953,-5.329503,-4.559509,1.523571,1.664986,2.330070,-4.425339,-2.210367,0.342899,-7.004324,-5.655901,5.739732,-3.901537,6.215635,0.347389,-3.936934,8.263619,9.458365,-7.618615,-1.975790,-9.088706,6.588226,2.546750,5.670958,0.205642,-2.299820,-1.847481,0.494571,-4.581290,-2.217347,0.246947,9.455398,-0.072067,-0.270315,8.556247,-9.167803,-7.792277,4.133400,-7.409872,5.855871,-2.624947,6.022258,1.622629,9.995004,4.398472,7.207619,7.897291,6.733084,-1.727463,-2.745112,3.836853,1.600762,-5.805588,8.318249,-2.406334,0.816032,-9.267615,2.142981,9.606045,0.029076,-0.103530,7.744247,-3.170079,0.842800,2.075642,-8.827731,6.151505,-3.425112,-5.852771,-6.536522,-1.791221,-6.330176,-6.327329,6.090354,-4.150745,-8.064274,3.966010,-8.710299,5.784769,-4.002209,-7.178349,1.994641,1.062820,6.267721,9.780819,-0.989606,2.161148,-0.008705,-7.479722,4.974469,5.097390,5.289912,-8.313836,-2.805205,-1.057296,-4.491299,5.085559,-2.912998,8.571769,2.995681,3.231119,2.361626,-8.774980,-2.771039,6.389810,8.919843,6.078775,2.621432,8.324365,6.315103,6.365262,-6.582946,6.110745,5.339308,-2.243374,1.195003,-1.459196,3.446916,5.072685,1.089227,3.323579,4.011206,9.626074,-1.844103,-2.670012,-2.528611,2.496598,-2.329624,2.093447,-8.210571,-1.620974,8.326712,-4.183343,6.974039,-3.798740,-8.607050,-3.997512,0.966284,-4.659990,-8.769664,3.629095,-2.137517,2.940969,-0.241967,-8.420768,-8.518915,-8.626004,9.760484,-6.203311,-5.103057,2.380214,9.254011,-2.793060,-7.418776,-7.518222,7.546864,5.598769,9.027172,3.328691,-8.054555,-8.724650,-7.619161,-3.595891,8.835636,1.592384,-4.079881,-3.765742,-6.026641,-3.639577,4.641507,9.980022,-5.929940,9.268255,5.362846,8.580921,-4.842608,-1.765690,2.428691,4.447377,-9.405541,-8.368481,5.389765,-4.297542,-8.166780,-6.694606,1.622918,-0.564799,8.607866,0.783712,-5.573946,-0.683481,-4.131581,-3.896556,7.783110,-2.723813,-9.189942,-8.828283,6.729879,1.911965,1.840535,-6.372543,9.585379,3.408810,-0.591272,8.355961,4.355704,8.560452,-7.559252,0.637038,7.555084,3.293351,8.966900,-5.126947,-9.985126,-9.514688,3.593156,8.880474,3.561619,7.832363,5.186874,4.034942,-4.048230,3.748493,-1.738451,0.640440,-0.291993,1.204408,-2.083733,6.444667,0.838438,2.870114,-1.394077,1.501170,9.220235,0.571745,1.869631,5.023666,0.635961,-1.639089,-9.366686,-3.052417,6.441415,-6.655029,2.629059,-7.296040,1.271349,4.854790,-0.938322,4.757595,-5.110734,0.667699,2.074225,7.985294,3.127645,-6.977903,1.437544,-5.183680,-8.358097,5.492963,-0.565831,-3.158437,5.376373,0.325213,-1.226235,3.907540,0.220700,-5.533591,6.223270,-8.591084,-8.471379,-6.939901,5.552833,-6.719629,8.321791,1.013884,9.510507,7.445883,0.233769,7.153518,-7.160316,-3.054803,7.368164,-7.202701,7.858368,9.820238,-8.722355,5.625279,-9.269788,1.602289,4.692928,-6.773527,8.355975,4.983448,-6.879365,-6.773607,4.053737,2.310357,-0.280657,-9.408876,-3.799581,1.289565,4.951443,-7.420522,-9.946934,-5.839120,-8.850896,-2.873150,-6.383331,-0.441114,-9.388091,1.797396,-9.010321,-5.073628,5.859662,-1.041502,-1.631349,-8.492930,-0.487047,-6.916449,-7.235804,6.455395,3.769905,-9.080173,4.110777,-4.853447,-1.958883,-6.889551,-4.097962,2.768881,5.043321,8.755672,2.576329,7.394050,-4.757197,-7.871753,-5.902187,6.989833,5.543845,-6.272490,0.734416,2.286706,-6.101679,-7.704407,-8.321002,-9.317811,5.404587,-6.922662,1.381953,-3.439318,6.983791,9.104536,-8.766050,4.505290,-2.901905,5.874885,-6.530259,4.343874,-4.092577,-3.114807,9.206652,-1.240344,-9.524104,3.549725,-9.230534,-6.944355,-7.471597,-1.156077,-7.442747,8.978948,0.772812,-5.558317,3.990049,-7.951184,6.975709,-9.430215,-9.361169,9.466435,2.359873,-8.369935,0.388939,1.539196,-6.661787,-8.260768,0.683137,-6.741176,-5.860675,7.785591,-7.498028,3.311530,-0.391672,4.991315,-7.188670,1.191233,8.711230,-3.211385,-5.643120,0.344796,1.259868,-8.249754,7.556974,8.425419,3.735503,3.901401,-0.762256,-1.607837,-2.888685,3.940817,-5.220265,2.582118,6.245734,-2.883019,8.071583,-7.102059,-3.946534,-8.950589,0.958176,8.228241,-9.832805,7.440031,-8.572315,1.845194,4.069384,7.675345,5.329265,6.256640,-5.483109,8.658280,8.184427,-3.249178,-0.276035,3.954576,-6.488884,-1.526431,3.777263,-1.055332,6.858421,3.965516,-8.064592,8.036064,2.460881,-6.070079,-8.883500,7.009518,-7.096037,1.380635,-9.820416],[-7.687062,-7.237793,0.543315,-4.499816,2.301428,2.865782,-5.941091,9.801845,-4.201715,0.025814,1.560260,-7.668059,9.936650,-9.128035,0.183072,-0.983450,-6.040893,-6.509372,-8.298060,6.381097,2.592961,-1.949839,-5.755180,6.247033,-6.329053,-1.673186,-4.333005,0.120025,6.187761,8.423028,-6.872225,-6.200505,-7.450146,5.294390,-7.827060,-2.329555,3.776093,7.968245,-5.027792,-4.852120,8.346220,-5.570614,3.733862,-9.820297,-0.456342,0.275419,2.277807,4.734969,2.468107,-0.203269,1.828884,7.356616,-8.787197,-3.775542,8.095359,2.357077,5.392584,-8.390637,9.930558,9.406590,-9.365548,0.459835,3.695809,0.043190,4.348573,-6.392720,-9.607860,5.671273,-7.439195,-2.659139,1.652297,3.961875,6.048506,0.654845,-4.806000,-5.389869,-0.826272,-5.112654,-0.797739,-1.284566,6.220622,-7.422397,-6.590927,-3.834842,-9.641848,-7.353394,7.136915,-2.189018,2.545945,4.730734,0.831919,9.094391,3.149344,2.597691,5.218270,1.616643,-4.007953,5.149142,-4.627482,6.622713,-8.340314,-6.878821,7.223665,-9.762926,-2.608804,-3.091584,-1.274081,5.682124,4.707196,5.746818,-8.272726,-9.867825,2.246610,0.873776,3.146987,-0.959671,-6.391877,2.599754,3.158930,5.099264,-6.022200,8.779328,5.661066,-2.492170,5.384663,9.744311,2.912659,-7.876091,8.545830,-6.162180,3.521231,-9.254316,2.937152,8.529201,-3.133949,-7.873196,1.514123,9.847508,4.979664,2.415471,3.815050,-5.913682,-7.988226,9.501759,3.515958,3.559460,-9.412278,-2.844139,4.413009,8.385274,-4.145387,-6.382409,4.257585,-7.893394,-4.125457,-1.895423,6.147328,-9.351233,7.722803,4.917020,4.450051,5.468642,9.513769,8.377939,-4.971940,-0.996345,-2.402851,-1.376461,-9.832432,-1.653179,-8.773678,-1.122787,-7.113564,-6.153031,3.847358,-5.006335,-4.595092,-4.265162,3.507676,-8.973364,-0.303113,4.004587,-6.780174,0.945317,-9.626048,3.371207,-2.205345,-1.679612,-1.834203,-6.821824,0.659245,-0.301590,4.034691,2.593783,-6.513729,-0.685231,-7.014580,1.152921,0.817973,3.617360,5.820104,-4.862187,-0.759564,-2.179480,8.917537,-0.449905,5.733248,-2.713639,-5.910153,5.450357,-6.060762,2.526098,8.970860,6.484984,5.288078,5.951444,6.134199,-4.365445,-8.355394,-4.757885,-6.545194,-0.428968,5.049886,-0.389585,-5.472775,-5.501294,6.903767,4.209159,-6.088405,3.077213,9.387465,-3.432338,-4.622240,9.009203,1.719737,3.104293,-9.043623,0.544936,-1.592221,3.014436,-6.488738,7.168269,-9.925253,-3.092919,3.865302,-6.079803,-6.634678,6.919165,-2.188438,-4.408960,-9.945643,1.551611,9.954500,-6.058540,-2.483201,6.682939,0.927913,-3.672457,0.518855,0.267283,-1.464362,-5.979278,-8.530200,9.901120,-9.230082,6.290023,8.100797,6.212553,9.595139,6.796309,-4.540728,-4.278386,4.318221,0.924951,-6.821715,-6.061540,-1.881366,9.283115,-6.648362,9.830344,-0.202972,-3.517422,9.139287,3.480416,6.110374,-0.968757,1.562859,-7.183113,2.071077,0.699083,-9.508390,-2.265905,-7.113074,4.794407,0.031655,9.384275,2.436966,7.504146,-4.488493,-5.748172,8.248685,8.924677,6.453789,-6.368658,7.815428,-6.228743,9.501969,-9.730262,1.306322,-0.008480,8.633837,-7.763111,2.731520,7.404426,-0.862687,-8.459671,4.298676,-1.724294,9.084688,5.747765,7.169908,-8.352977,4.023413,-0.672415,-8.206607,7.444811,0.987030,9.123742,8.349650,-5.990976,-0.111722,-6.972255,-6.937542,-0.692486,2.482475,-5.485191,-6.488096,6.032332,4.456032,-2.830398,-3.618771,3.320158,0.113846,0.582920,-7.616127,3.367740,-4.157768,-2.517894,-1.937637,-0.980233,-6.984701,-0.302313,7.584042,-8.175924,-6.373468,-5.454105,-1.626372,-8.693205,-9.945340,2.330697,4.513678,3.263016,-5.641180,-3.357980,2.995685,-5.349399,3.998659,-0.102990,-6.245843,4.190041,7.251413,7.359595,-7.054930,8.924842,7.670629,5.726273,3.560466,-1.780589,-5.815842,7.212527,0.631584,6.998619,-7.835958,0.207936,9.880849,7.499225,6.200671,-5.439609,-9.902054,-5.562427,-5.129768,-0.985568,0.986647,9.321351,8.869226,0.437625,-9.791716,7.641131,-2.463422,3.457933,-3.591811,-4.106052,-2.370828,7.847192,-6.311256,-9.934306,8.207669,4.816719,-4.777031,-2.987518,6.036164,-2.691674,-1.346677,-9.611601,1.060620,-2.671939,3.304482,7.728327,-8.531945,-2.956860,-0.287489,2.349780,-0.730069,-6.231824,-3.449994,-0.647017,-8.840334,7.332307,5.483225,0.991554,-3.198128,-4.348014,-8.743572,1.645940,-0.479615,-8.688052,-0.002249,-2.526764,-4.454102,2.891728,3.069332,-5.626594,6.112668,-8.600323,7.246054,2.866000,-2.466327,5.911832,4.039712,5.103394,2.048848,-7.475351,3.727172,-7.395147,-7.560230,-6.833892,8.290533,6.154080,3.528081,7.111542,-7.480471,-3.864775,-4.802317,9.788344,-2.762011,5.829367,-4.440714,1.104838,-0.807257,1.662137,-8.041678,-4.853966,-9.893980,-3.976855,-1.595483,7.657755,-1.588249,0.935024,8.361296,-7.140967,1.054517,0.762492,8.034533,7.439139,-3.749157,-8.643669,2.440839,0.593859,3.834099,0.861244,9.536373,-1.475055,-6.221401,6.624500,-2.754891,3.102192,2.542829,-9.176717,8.210341,1.436214,-1.590223,-3.779335,-0.269293,-8.368985,3.822700,8.737471,-3.208735,-9.626210,7.352447,-4.053488,8.824866,8.546984,1.602222,-4.652257,-7.424388,-0.709809,7.332669,-9.971484,-6.827409,4.454275,-2.006258,4.011778,-4.495771,7.520442,2.757385,-2.421625,1.048672,7.939529,3.940109,7.707495,7.484434,-8.122186,4.935163,7.082269,3.077139,4.335407,6.891478,-7.524776,3.378478,-2.787131,-6.152290,1.444753,-1.425342,-1.764297,-1.204100,9.988700,1.946423,2.101769,-8.252969,5.763880,8.275636,4.387424,7.539144,2.682759,1.637011,6.867085,-4.356538,3.492272,1.549132,-1.719935,-9.387902,-6.953452,9.127511,-0.586886,-3.279993,-5.581691,-2.422868,-1.589664,0.144731,-4.701425,6.744472,-7.021619,3.310468,9.320094,4.698772,-6.137105,7.615632,-1.681296,-8.559257,1.144968,-0.747208,5.535796,5.653887,-5.390165,7.775754,-9.790155,-3.229416,-3.327847,-5.411157,-9.921414,1.719665,1.005147,5.378932,0.044256,-7.613615,-0.635898,-2.136833,-1.515700,-6.876900,5.318079,2.751080,-4.983730,-6.349281,6.516439,-3.337301,0.382703,6.200370,1.724629,-2.011197,-2.078553,6.498112,2.788537,-3.041482,7.387965,-6.005900,-6.727728,-3.071142,2.861522,3.796160,-7.359101,-4.229397,2.903586,-4.597862,0.374628,-5.544666,-3.739825,-1.400925,7.995300,2.708801,4.751631,9.144259,4.692975,6.539314,4.144204,-8.569756,-2.584799,6.622875,-8.225519,-8.904403,-5.766451,8.367717,-8.655846,-0.058059,7.776227,1.108154,4.250846,-3.997622,-1.464509,8.048788,9.870223,5.355835,-5.682105,2.480174,8.896936,-2.214700,-2.324081,-5.511710,-8.673628,2.269185,-8.171220,-5.071427,7.443484,-2.279919,-0.752658,2.811511,5.053448,-2.798304,8.829134,-7.307790,9.924103,-2.184829,5.770953,0.247897,9.945734,7.738809,6.302622,2.829200,-5.223091,-1.874130,4.214248,-4.228067,5.855786,8.281690,4.646082,5.322402,-2.260738,-2.866540,-0.592401,2.707148,-8.320831,7.331623,8.687168,9.442365,-0.444099,-0.433627,8.661620,1.902845,5.627920,-4.838288,-7.409986,-6.297467,9.976276,-6.358025,-2.543661,-0.360016,-7.294771,-2.378583,-3.544843,-9.595504,6.476956,5.304263,2.920908,6.201304,1.707849,4.667687,4.452444,-1.619917,1.992272,-7.524211,4.657523,-8.444128,-4.841652,7.911386,-9.785056,-0.667641,-6.675888,7.522697,-5.256450,8.063976,-1.038112,9.089951,-4.570770,-9.026613,2.228367,9.477627,7.318396,-0.546221,-4.398532,6.196191,5.283467,-2.695989,0.867662,-4.873939,1.658113,6.322011,-2.971243,9.812074,-9.945185,-9.048376,9.797821,-7.566237,-2.553680,-6.873482,-8.306868,5.263055,1.286908,-4.494455,3.543385,-2.243634,-8.059755,-3.179115,1.288678,8.589724,-4.730277,5.638494,8.291960,-9.755327,-5.362132,-1.546211,-9.695456,6.639478,8.322911,-6.208498,-5.869219,6.216587,-8.074837,9.089464,-6.729304,-7.445529,8.373852,-6.832355,2.350171,-4.539467,7.388990,7.223410,-4.988602,-5.447366,-8.007738,7.419367,2.003680,9.289782,-3.289084,8.353735,9.317145,3.198691,6.397961,8.143500,3.330280,6.693558,-0.485786,-1.435114,4.796754,-0.063190,-2.166066,-4.903855,8.737755,9.098020,-6.515874,-5.438555,-5.957993,-2.618013,9.325633,9.736903,8.731641,9.965912,3.208640,6.712691,-4.301222,-2.246237,6.742184,0.047355,-0.358576,-7.718450,1.371051,-7.745104,2.334912,-4.165153,-4.852472,9.282018,-0.199952,7.246292,-1.105395,-0.187753,-7.021002,0.464104,4.095709,-9.848155,-1.498800,-8.092874,2.001410,9.632291,-8.460641,9.022591,1.787376,-5.385296,-5.086791,4.584884,-8.288739,4.190657,-6.733703,-2.859389,8.710755,5.107708,-8.384255,-2.897563,-9.580001,-5.338771,7.796753,5.571268,-0.174533,-1.922639,6.482423,3.155284,4.446837,3.611490,-9.965956,0.669980,-6.046394,3.842412,-6.739979,8.999010,1.438489,0.948805,3.859647,-5.275737,6.923318,-1.337387,-9.684758,-1.136870,3.631503,-5.134659,-0.703749,9.410683,-8.532652,2.268625,-8.899872,-3.395467,-7.411587,-3.945773,-3.291293,4.972108,5.517053,9.938633,8.179523,7.305969,0.849923,-8.739683,6.894261,-6.348631,-7.240691,3.963954,-0.423279,6.184768,1.516066,2.048918,-2.357750,7.927368,-5.863691,9.106279,9.748135,-2.028254,-2.433368,-3.999612,2.948876,-6.413734,-0.753527,-6.993434,1.768082,8.450979,-8.549791,-0.591217,4.956103,-1.083989,-5.834456,4.833839,5.131197,-3.242557,5.856351,4.938141,-7.220865,-4.603263,2.244710,7.888244,-3.029442,-2.608192,5.496509,9.089239,-9.291718,0.682345,-4.775335,-6.294866,-4.141508,5.815347,6.590301,-3.922633,-1.415413,-5.089397,-1.829101,-0.026868,-6.863859,1.093285,-8.756243,-5.345308,-4.005913,1.475980,2.535637,-1.695057,3.469994,6.816009,1.696472,-5.903143,-0.633883,0.557214,-0.298989,-0.097151,-6.824047,2.442932,-6.434006,-2.849717,8.227396,6.076533,0.053512,-0.895322,-1.509935,-7.406772,-1.303865,5.773389,1.418905,0.256142,8.520604,6.844125,4.072322,-6.187107,-3.170548,-6.300359,-9.282008,-7.428893,-1.451391,-1.990039,-9.183341,-9.367662,4.564092,-5.883442,-0.442696,2.269017,3.699816,-0.740371,0.992177,-0.269728,1.099213,1.404848,6.951587,5.708124,-0.126863,-2.166905,-2.590921,2.749557,-3.430538,2.117593,8.627460,-3.014510,4.644392,5.652555,2.169385,-7.492851,5.140481,5.421757,-6.346765,-1.276559,-6.470414,4.877888,2.050256,4.521358,-4.210035,-9.071692,3.042712,-6.719076,0.488925,9.619094,-7.094404,6.345835,3.308167,-2.942693,-0.536603,-9.598746,6.507549,6.287136,6.555917,-4.340696,0.393099,7.901770,-4.646710,7.458323,-9.852432,-8.763554,3.438583,-1.256458,-6.311646,-2.312177,8.961221,-1.111679,-8.002633,7.205834,-4.436293,-3.381562,-5.293150,-6.987194,4.477469,3.459057,-8.107510,-2.647483,8.314277,-3.078534,2.323189,-4.186284,3.450151,8.821314,8.010006,0.370441,0.129200,2.343607,-8.024891,-5.031803,-8.864344,4.901379,9.397306,-3.570612,-2.390657,9.361289,1.866042,-1.941381,-9.596689,-7.065522,-5.772568,4.895132,1.950125,6.334415,-9.399903,-9.149313,0.374010,3.488340,5.429176,-0.100798,-7.698606,-4.156544,1.115933,-9.283777,-1.383543,0.559835,9.877077,-8.469334,-8.979979,-7.798159,0.412060,6.360160,-5.687370,-1.548335,-5.986577,2.157119,-4.482343,-9.030243,-2.852714,2.415007,5.127024,0.729597,3.927025,-1.572239,7.687291,-4.341175,8.161097,-5.117287,-5.812733,4.997281,2.126103,2.234374,-3.368353,6.768163,-0.226766,-2.288795,-1.980305,-4.327393,6.809634,3.051827,6.904080,-4.840168,2.395349,-5.681752,3.203637,-1.088824,-9.007792,-3.779217,1.970592,6.723358,-5.568865,5.402447,1.136873,-4.964287,-2.930390,-5.968393,1.518910,-5.288185,6.360676,-5.179612,9.160811,7.675216,-6.472134,-8.005599,3.041300,4.426255,6.011214,-0.273408,3.373079,-2.259040,-2.812308,2.661823,2.891775,-4.251563,5.612042,1.925236,2.771702,-1.212795,-6.104574,3.063594,5.489082,7.456599,-5.602765,8.599476,-1.125891,2.289981,-2.600581,-2.903409,4.633223,-4.818561,4.788289,0.841680,-9.955628,-6.140967,-6.374040,6.391447,-3.763546,7.962108,-0.561610,-7.960905,-8.192722,-1.636640,4.256201,-5.603325,5.511668,5.130883,-9.555639,-2.942058,-4.665990,7.070800,-5.690101,-5.820337,7.944043,6.857875,0.545230,-8.610786,-0.855510,-1.179026,9.148729,-0.691817,-5.060529,4.673426,-3.724810,2.639421,-5.009657,7.260300,9.442719,2.447640,1.515966,5.175684,9.116812,-6.987550,-3.874935,6.819570,2.250579,-2.583524,2.887616,-9.591649,4.305760,-6.787743,-8.462922,3.428517,-2.404500,-9.396394,1.632564,-7.061904,0.760850,-0.224282,9.207997,4.149976,7.372366,-9.055461,5.182727,-7.757035,9.723673,-0.402138,1.988924,5.091862,7.542713,8.758081,1.608295,8.014075,0.067972,-4.994704,6.433438,2.520214,-6.828169,1.267873,0.732081,-3.870764,-0.691987,-4.233259,-6.686813,2.437544,-8.738255,5.261236,-8.700091,-4.142302,-7.185931,4.514243,0.137518,9.502402,-0.940683,6.926170,-3.986499,-7.268426,0.053954,-5.791341,2.477417,4.793758,2.726294,5.982696,8.270022,5.003049,4.150673,9.680881,0.832641,-4.431266,2.087845,5.011557,5.623921,-3.219740,9.634133,7.576992,0.387515,-6.072900,3.951697,-7.495615,3.874192,-3.277490,-6.194592,8.513621,-5.916422,-9.181115,-8.707119,-5.743297,6.311676,-0.267103,2.266324,5.686908,-7.167273,0.138388,-8.858105,-4.142993,9.401339,-8.298568,-5.487695,-2.843682,8.752163,-8.541159,-3.268331,4.729683,5.664415,-0.102079,9.972661,2.551704,3.189619,6.540335,6.584827,-4.864800,1.226077,-6.473896,-2.468019,-5.018956,4.229253,0.718739,7.340388,-7.834803,-4.426730,-9.141543,-2.615922,8.477226,-4.583156,3.877043,-4.440556,5.186901,-0.312695,7.909593,-3.013677,-1.839698,-3.976410,5.862615,8.170267,3.088514,8.671960,5.622942,1.885829,7.081452,-2.752422,4.628279,-1.425518,-7.629435,0.964965,-9.791846,2.604839,5.770642,-8.202633,-5.344270,-3.921616,-5.022722,9.285629,-9.012251,-4.238055,-5.811234,-2.075878,-0.018602,-4.919403,-2.188033,-1.601879,0.656352,0.543864,-3.776161,-6.378580,3.556286,-7.230667,-1.269417,-8.378003,-9.994507,-6.816161,1.389562,8.731862,-8.540660,-3.366427,2.726785,9.998148,-7.140215,9.739083,-0.736763,8.622321,4.948070,8.831408,4.977129,-6.468172,3.834712,9.502290,8.097633,-4.220947,-9.173843,-9.376974,9.701345,3.214166,2.002049,-2.634439,-0.342175,7.137183,3.317137,9.802634,-1.916860,9.959477,-6.780078,-6.267467,9.503168,2.079209,3.912449,3.360454,8.404309,2.119970,4.240990,2.064694,7.598096,5.654675,7.851370,-6.421378,-1.504774,6.604268,-8.444718,6.831837,-6.373442,2.601758,-0.699197,6.199088,0.245260,-0.764810,-5.119654,-5.632266,2.194018,3.209968,-7.356272,-7.271613,4.973777,-9.591715,-3.400546,1.794465,-3.082282,-9.013316,9.999042,4.736171,-8.836589,7.183487,9.643094,2.777156,-4.596742,4.623442,-4.320027,2.859526,-8.984267,3.797573,5.696548,3.349980,6.784256,3.834707,1.075150,-8.184951,-9.383026,0.756456,9.573379,-2.697203,2.394407,3.901671,-2.931496,3.844752,-1.956173,3.904417,1.227674,9.717095,-1.076638,6.451859,5.193925,-7.826373,3.680386,0.051086,-1.857066,-8.766394,-5.899129,5.543159,1.928527,2.670629,5.497634,2.683005,8.886663,3.384547,5.120854,-3.747717,-5.745023,6.397128,-5.125272,0.181497,-6.811591,-6.438708,4.755351,8.798456,-0.446652,-3.321737,3.363138,-8.419866,-7.643429,6.964652,-9.112164,6.476245,-6.497219,-3.919750,7.664506,2.733798,-9.048489,-2.274240,8.949689,-3.519877,-3.056566,2.087122,-4.544967,9.042937,5.784623,6.739575,-9.548605,9.185009,5.367968,5.175512,7.610929,-3.879036,-6.241918,5.773112,8.983774,0.400510,-9.283956,2.083188,-7.850427,0.829973,9.099277,5.274147,5.907337,-5.922054,-6.857531,-0.358523,-1.752526,9.962589,3.078035,-4.208885]], dtype = "float32")#candidate|6039|(2, 1560)|const|float32
call_6038 = relay.TupleGetItem(func_4784_call(relay.reshape(const_6039.astype('float32'), [3120,])), 2)
call_6040 = relay.TupleGetItem(func_4787_call(relay.reshape(const_6039.astype('float32'), [3120,])), 2)
output = relay.Tuple([uop_6033,call_6038,const_6039,])
output2 = relay.Tuple([uop_6035,call_6040,const_6039,])
func_6053 = relay.Function([], output)
mod['func_6053'] = func_6053
mod = relay.transform.InferType()(mod)
mutated_mod['func_6053'] = func_6053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6053_call = mutated_mod.get_global_var('func_6053')
call_6054 = func_6053_call()
output = call_6054
func_6055 = relay.Function([], output)
mutated_mod['func_6055'] = func_6055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6053_call = mod.get_global_var('func_6053')
func_6055_call = mutated_mod.get_global_var('func_6055')
call_6167 = relay.TupleGetItem(func_6053_call(), 1)
call_6168 = relay.TupleGetItem(func_6055_call(), 1)
func_1733_call = mod.get_global_var('func_1733')
func_1736_call = mutated_mod.get_global_var('func_1736')
const_6189 = relay.const([-7.585049,-4.032893,-0.963476,5.288264,-0.513648,-0.496902,-9.550258,9.583905,-5.064901,-3.489728,-2.139900,-9.894141,-9.079432,-3.107213,-4.214215,-8.528436,-6.511462,-7.940787,9.104152,-4.420047,-7.356820,-3.471329,-8.588062,3.216088,-3.910100,-6.740617,1.436837,-4.840985,-8.890532,7.706808,-3.806873,9.772341,6.163168,4.040858,-5.161142,-8.882860,-1.977318,5.121957,-2.584363,9.456978,-7.818154,-3.512071,-4.990260,0.514506,3.757945,1.078903,1.024467,-0.881493,0.544935,6.799806,-2.218184,-0.841953,-3.810626,0.011959,-5.378258,-2.601285,1.974432,6.067379,2.991582,-3.779919,1.526469,-0.897971,3.565729,3.613280,8.449933,-5.688057,0.495806,-6.180477,-1.862293,-5.386207,1.962433,2.389609,9.136734,-7.180335,5.714041,-5.618186,7.932676,7.641130,3.926321,7.413154,2.410562,-4.243205,-2.545127,7.411008,6.899763,-3.861139,-8.095342,7.791053,-7.986741,-5.792152,-5.712458,-7.942946,4.129471,-6.568358,0.319611,2.569688,2.762053,4.975719,2.214864,-3.221853,-9.892561,1.265896,-0.621578,5.633138,-3.196342,5.592752,-5.700086,-2.883199,6.043752,-7.665392,-3.614265,-5.600553,-4.863448,-0.654382,-2.126257,-0.155974,1.287767,4.337122,-5.151670,-1.305185,-5.805909,7.529135,3.604175,-2.102259,4.278873,1.972454,5.202952,2.375271,8.346858,1.569255,0.968552,9.073572,3.472821,-6.993590,2.771947,-9.791166,-4.114280,-1.118262,-3.785782,8.260829,1.449615,5.448164,-9.568319,-4.027713,-2.118028,1.303913,9.078069,-0.301147,0.719291,-3.394600,5.309054,-2.601069,2.739555,-9.565486,3.494887,6.136396,-9.832941,1.989309,8.227567,4.885259,3.431843,8.296182,9.060085,6.663562,2.738172,0.385168,9.837388,-4.535946,-2.560786,-6.437222,-1.227996,-9.992405,-4.851134,6.664257,-9.975149,-8.215931,6.571569,-0.889200,7.560860,9.690078,-0.737684,-3.301887,-2.902099,-7.902201,9.754828,1.869220,-5.647951,-0.316858,3.977005,-3.957925,-2.116440,-1.914746,8.772595,-5.539944,-2.423528,8.087529,-2.109526,-1.317804,-5.984683,1.308173,2.624218,-0.684450,1.543445,7.254700,-3.967569,-2.257991,-6.656640,8.692452,4.311497,-4.004536,1.820600,-3.660212,6.498101,1.744132,7.903778,7.599090,0.419608,-4.175001,4.615307,5.318884,-6.922941,-4.154743,-0.646525,-7.443337,-8.450975,-6.207351,-5.220673,7.281921,9.682981,4.169341,-9.415501,-3.867468,-1.582627,-9.810055,-9.114755,-3.303808,3.681639,5.899723,-5.182948,9.704733,-4.137814,-3.703037,2.518247,7.012841,-2.429872,0.540612,1.565333,-1.270380,2.481794,5.987315,5.938921,-6.236589,8.258390,-3.161297,3.620661,-1.880630,2.137981,-6.889000,-3.980700,-2.153755,-5.325440,5.953155,2.694414,-5.679205,-7.019460,-7.429274,3.125487,-2.261957,-0.302525,-9.443531,6.522103,0.629671,6.194063,5.600644,9.080628,3.631870,0.220755,-8.306432,-5.248897,5.122217,-1.521969,-5.856757,-6.475771,-7.686079,-4.587875,-2.849187,5.521995,-2.829836], dtype = "float32")#candidate|6189|(288,)|const|float32
call_6188 = relay.TupleGetItem(func_1733_call(relay.reshape(const_6189.astype('float32'), [4, 8, 9])), 2)
call_6190 = relay.TupleGetItem(func_1736_call(relay.reshape(const_6189.astype('float32'), [4, 8, 9])), 2)
func_4053_call = mod.get_global_var('func_4053')
func_4054_call = mutated_mod.get_global_var('func_4054')
call_6204 = relay.TupleGetItem(func_4053_call(), 0)
call_6205 = relay.TupleGetItem(func_4054_call(), 0)
output = relay.Tuple([call_6167,call_6188,const_6189,call_6204,])
output2 = relay.Tuple([call_6168,call_6190,const_6189,call_6205,])
func_6208 = relay.Function([], output)
mod['func_6208'] = func_6208
mod = relay.transform.InferType()(mod)
output = func_6208()
func_6209 = relay.Function([], output)
mutated_mod['func_6209'] = func_6209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3703_call = mod.get_global_var('func_3703')
func_3704_call = mutated_mod.get_global_var('func_3704')
call_6216 = relay.TupleGetItem(func_3703_call(), 0)
call_6217 = relay.TupleGetItem(func_3704_call(), 0)
func_4139_call = mod.get_global_var('func_4139')
func_4141_call = mutated_mod.get_global_var('func_4141')
call_6220 = relay.TupleGetItem(func_4139_call(), 0)
call_6221 = relay.TupleGetItem(func_4141_call(), 0)
output = relay.Tuple([call_6216,call_6220,])
output2 = relay.Tuple([call_6217,call_6221,])
func_6228 = relay.Function([], output)
mod['func_6228'] = func_6228
mod = relay.transform.InferType()(mod)
mutated_mod['func_6228'] = func_6228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6228_call = mutated_mod.get_global_var('func_6228')
call_6229 = func_6228_call()
output = call_6229
func_6230 = relay.Function([], output)
mutated_mod['func_6230'] = func_6230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4053_call = mod.get_global_var('func_4053')
func_4054_call = mutated_mod.get_global_var('func_4054')
call_6266 = relay.TupleGetItem(func_4053_call(), 0)
call_6267 = relay.TupleGetItem(func_4054_call(), 0)
func_4053_call = mod.get_global_var('func_4053')
func_4054_call = mutated_mod.get_global_var('func_4054')
call_6282 = relay.TupleGetItem(func_4053_call(), 0)
call_6283 = relay.TupleGetItem(func_4054_call(), 0)
func_6228_call = mod.get_global_var('func_6228')
func_6230_call = mutated_mod.get_global_var('func_6230')
call_6290 = relay.TupleGetItem(func_6228_call(), 0)
call_6291 = relay.TupleGetItem(func_6230_call(), 0)
output = relay.Tuple([call_6266,call_6282,call_6290,])
output2 = relay.Tuple([call_6267,call_6283,call_6291,])
func_6296 = relay.Function([], output)
mod['func_6296'] = func_6296
mod = relay.transform.InferType()(mod)
output = func_6296()
func_6297 = relay.Function([], output)
mutated_mod['func_6297'] = func_6297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3776_call = mod.get_global_var('func_3776')
func_3778_call = mutated_mod.get_global_var('func_3778')
call_6329 = relay.TupleGetItem(func_3776_call(), 0)
call_6330 = relay.TupleGetItem(func_3778_call(), 0)
uop_6331 = relay.log10(call_6329.astype('float64')) # shape=(14, 15, 9)
uop_6333 = relay.log10(call_6330.astype('float64')) # shape=(14, 15, 9)
bop_6341 = relay.not_equal(call_6329.astype('bool'), relay.reshape(uop_6331.astype('bool'), relay.shape_of(call_6329))) # shape=(14, 15, 9)
bop_6344 = relay.not_equal(call_6330.astype('bool'), relay.reshape(uop_6333.astype('bool'), relay.shape_of(call_6330))) # shape=(14, 15, 9)
func_3703_call = mod.get_global_var('func_3703')
func_3704_call = mutated_mod.get_global_var('func_3704')
call_6347 = relay.TupleGetItem(func_3703_call(), 0)
call_6348 = relay.TupleGetItem(func_3704_call(), 0)
bop_6355 = relay.bitwise_or(call_6347.astype('int16'), relay.reshape(bop_6341.astype('int16'), relay.shape_of(call_6347))) # shape=(14, 15, 9)
bop_6358 = relay.bitwise_or(call_6348.astype('int16'), relay.reshape(bop_6344.astype('int16'), relay.shape_of(call_6348))) # shape=(14, 15, 9)
output = relay.Tuple([bop_6355,])
output2 = relay.Tuple([bop_6358,])
func_6359 = relay.Function([], output)
mod['func_6359'] = func_6359
mod = relay.transform.InferType()(mod)
mutated_mod['func_6359'] = func_6359
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6359_call = mutated_mod.get_global_var('func_6359')
call_6360 = func_6359_call()
output = call_6360
func_6361 = relay.Function([], output)
mutated_mod['func_6361'] = func_6361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5926_call = mod.get_global_var('func_5926')
func_5927_call = mutated_mod.get_global_var('func_5927')
call_6431 = func_5926_call()
call_6432 = func_5926_call()
output = call_6431
output2 = call_6432
func_6435 = relay.Function([], output)
mod['func_6435'] = func_6435
mod = relay.transform.InferType()(mod)
output = func_6435()
func_6436 = relay.Function([], output)
mutated_mod['func_6436'] = func_6436
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6556 = relay.var("var_6556", dtype = "int32", shape = (9, 10, 2))#candidate|6556|(9, 10, 2)|var|int32
const_6557 = relay.const([[[-8,3],[6,1],[-6,-2],[-7,-10],[-5,-10],[-7,-10],[4,5],[-6,3],[1,5],[10,3]],[[-10,6],[7,-10],[6,-1],[-4,-10],[-4,10],[7,3],[9,-7],[-3,4],[-7,-3],[-6,-7]],[[2,-5],[-3,-5],[-1,7],[10,10],[-10,-10],[-7,-8],[-5,-1],[3,5],[-7,2],[-7,-5]],[[5,8],[3,-5],[-5,4],[9,8],[-3,7],[6,1],[-6,1],[3,-4],[9,-4],[-2,-3]],[[-3,-8],[-1,6],[-5,1],[-9,-5],[7,-8],[4,-9],[-4,7],[-1,2],[1,6],[-8,7]],[[-7,7],[1,1],[-9,-8],[-9,-10],[-1,10],[9,-4],[5,2],[4,9],[8,-7],[1,4]],[[-7,5],[-1,-10],[3,-2],[5,3],[-8,3],[4,3],[-9,8],[-8,-2],[-7,10],[3,10]],[[-3,8],[-2,8],[-6,2],[-5,4],[7,6],[6,-2],[-4,-3],[-4,2],[-5,7],[-3,-9]],[[-6,-1],[-8,-6],[8,-2],[-7,-7],[9,-9],[3,2],[2,-7],[-4,6],[-7,-2],[-3,-2]]], dtype = "int32")#candidate|6557|(9, 10, 2)|const|int32
bop_6558 = relay.left_shift(var_6556.astype('int32'), relay.reshape(const_6557.astype('int32'), relay.shape_of(var_6556))) # shape=(9, 10, 2)
func_2337_call = mod.get_global_var('func_2337')
func_2340_call = mutated_mod.get_global_var('func_2340')
const_6562 = relay.const(-10, dtype = "uint32")#candidate|6562|()|const|uint32
var_6563 = relay.var("var_6563", dtype = "uint32", shape = (15,))#candidate|6563|(15,)|var|uint32
call_6561 = func_2337_call(relay.reshape(const_6562.astype('uint32'), []), relay.reshape(var_6563.astype('uint32'), [1, 1, 15]), )
call_6564 = func_2337_call(relay.reshape(const_6562.astype('uint32'), []), relay.reshape(var_6563.astype('uint32'), [1, 1, 15]), )
func_5641_call = mod.get_global_var('func_5641')
func_5643_call = mutated_mod.get_global_var('func_5643')
call_6567 = func_5641_call()
call_6568 = func_5641_call()
bop_6574 = relay.maximum(call_6561.astype('int64'), relay.reshape(var_6563.astype('int64'), relay.shape_of(call_6561))) # shape=(1, 1, 15)
bop_6577 = relay.maximum(call_6564.astype('int64'), relay.reshape(var_6563.astype('int64'), relay.shape_of(call_6564))) # shape=(1, 1, 15)
uop_6588 = relay.atanh(call_6561.astype('float64')) # shape=(1, 1, 15)
uop_6590 = relay.atanh(call_6564.astype('float64')) # shape=(1, 1, 15)
func_5641_call = mod.get_global_var('func_5641')
func_5643_call = mutated_mod.get_global_var('func_5643')
call_6594 = func_5641_call()
call_6595 = func_5641_call()
output = relay.Tuple([bop_6558,const_6562,call_6567,bop_6574,uop_6588,call_6594,])
output2 = relay.Tuple([bop_6558,const_6562,call_6568,bop_6577,uop_6590,call_6595,])
func_6601 = relay.Function([var_6556,var_6563,], output)
mod['func_6601'] = func_6601
mod = relay.transform.InferType()(mod)
mutated_mod['func_6601'] = func_6601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6601_call = mutated_mod.get_global_var('func_6601')
var_6603 = relay.var("var_6603", dtype = "int32", shape = (9, 10, 2))#candidate|6603|(9, 10, 2)|var|int32
var_6604 = relay.var("var_6604", dtype = "uint32", shape = (15,))#candidate|6604|(15,)|var|uint32
call_6602 = func_6601_call(var_6603,var_6604,)
output = call_6602
func_6605 = relay.Function([var_6603,var_6604,], output)
mutated_mod['func_6605'] = func_6605
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6613 = relay.const([[[6.775455,-7.712931,0.116270,8.272032,-1.989259,4.429626,1.730133,-4.046306,0.102763,-2.759508,2.312174,7.807846,-8.320200,0.052438,7.497093,0.973018],[-0.927560,8.604692,9.644635,9.999039,-6.601699,-2.441240,9.867152,4.913688,-1.164626,-2.924827,-9.126594,1.780367,7.782927,9.579151,7.416299,9.266415],[8.552748,7.872607,-7.570753,-8.657704,-9.288526,-6.317217,6.957981,-0.365191,-6.377527,-0.195319,-6.018076,2.395995,-7.805840,-1.753747,4.949015,0.181863],[3.800369,5.864837,8.080589,-0.860556,-3.626561,-9.431371,-0.771420,1.546654,2.972721,-3.720038,-7.744523,-5.878280,-1.644879,-8.186235,-7.785566,-6.607498],[1.174410,3.849054,-6.266059,-6.855745,4.382070,-9.513782,0.357551,-7.557395,9.162829,3.663162,-2.114827,-1.401332,-2.730999,-5.022118,5.222275,-0.456522],[-5.485905,2.520058,0.854368,7.981445,-8.413108,1.308191,1.096003,0.995145,-5.920568,-5.014497,-1.288021,3.637013,-8.626741,0.116962,3.770685,-4.008059]],[[-1.414167,-5.419020,6.062038,-0.286168,5.710945,8.445319,8.731467,-8.903742,4.825840,-1.304582,5.348064,8.890985,9.607179,9.064358,-6.010934,-5.865524],[-2.190298,1.925012,-1.956110,3.962259,8.271072,-4.284651,0.719720,-3.427418,-6.265950,-2.734109,-7.900945,9.082130,7.916139,-4.494213,-0.729739,-2.577080],[4.702573,-1.807081,5.436505,-8.497882,-0.505430,4.143684,8.779923,9.671601,-6.654441,7.772700,1.481700,-0.302786,-4.258028,-9.447097,3.754149,3.431274],[-1.813451,-4.407706,9.283843,-7.793811,7.538074,-2.131042,2.438649,-9.626598,0.412173,4.075053,-0.832122,4.553893,-8.909654,2.479556,-9.708397,7.280866],[-1.955593,-8.390498,-3.791297,-5.458979,-3.103293,-5.033627,-4.115514,0.458156,-8.924135,-5.715209,-1.917324,1.017861,9.870197,-1.494181,4.016149,6.068738],[7.276550,-3.697107,-7.879344,-7.416218,5.611047,9.950317,5.863537,0.948053,6.530738,5.388118,-7.961904,-9.451909,7.778639,3.663674,-3.246604,7.605947]],[[8.894239,4.432496,-2.562617,-1.237703,-8.241314,6.314111,5.407662,-6.492454,-4.014468,-0.010771,-4.842338,-9.472499,-0.979500,3.969383,-4.060507,-7.822004],[-9.327652,-3.363453,9.052903,-2.410101,-5.595202,-1.995885,-0.005269,-3.611790,-8.839985,6.153067,7.334846,-0.830620,-5.901635,0.651983,-9.925448,-7.086223],[0.291127,1.634576,6.282429,2.931068,9.524348,8.137750,-8.404174,-8.286630,1.078173,8.608176,-3.664372,-3.401755,4.526488,2.126576,3.131913,-0.544031],[-4.624464,-8.707391,5.824951,9.527699,4.435886,3.465352,-2.328011,-0.760630,5.189775,5.631050,5.548659,-4.818014,6.265949,0.203766,8.036931,2.957600],[7.200265,-8.137709,2.459370,-2.316483,-3.092777,-2.882958,4.150131,-0.476351,3.111892,-3.084240,1.011049,4.210038,7.460963,-9.055225,8.926786,-4.758760],[2.113764,6.738152,0.334546,8.629469,2.473571,-4.603057,-5.644152,-3.756149,-8.235855,-5.220955,5.464784,-6.388847,-1.653485,-5.446878,2.175206,8.173748]],[[0.323688,6.301106,-7.357541,-2.948283,3.594309,-3.272888,-4.677977,9.594853,-6.702698,-1.426916,3.660390,-5.370977,7.609451,5.290608,6.349896,6.934521],[-5.166928,2.606353,2.365774,-7.947920,4.119400,-9.005007,8.265001,-2.769589,-7.541847,-1.862465,-6.538574,3.708984,2.957012,-5.076331,3.013162,8.151352],[-3.390028,-8.367160,-8.861507,-0.213535,-1.272683,4.117594,-9.832735,8.143505,5.431373,4.155527,-6.769832,1.565928,0.328066,-1.265235,-0.928028,-0.267060],[9.895260,-6.259257,-8.008485,5.632097,-7.767146,-0.232448,-5.648618,3.768301,6.821679,5.342829,6.763829,4.222647,-3.224305,-9.133225,2.719526,-7.445950],[2.598440,9.328277,3.790130,-9.521936,1.164392,4.016242,-6.534325,2.530113,8.170241,4.887413,-5.259234,0.174023,5.672560,2.193177,6.843674,5.884866],[-5.436100,-0.603421,4.515264,2.328955,5.809855,-6.436928,5.151372,-9.634959,5.395411,-9.969880,-8.148628,-5.332385,7.626405,8.307325,0.016567,9.154564]]], dtype = "float32")#candidate|6613|(4, 6, 16)|const|float32
uop_6614 = relay.sin(const_6613.astype('float32')) # shape=(4, 6, 16)
func_3776_call = mod.get_global_var('func_3776')
func_3778_call = mutated_mod.get_global_var('func_3778')
call_6617 = relay.TupleGetItem(func_3776_call(), 0)
call_6618 = relay.TupleGetItem(func_3778_call(), 0)
output = relay.Tuple([uop_6614,call_6617,])
output2 = relay.Tuple([uop_6614,call_6618,])
func_6649 = relay.Function([], output)
mod['func_6649'] = func_6649
mod = relay.transform.InferType()(mod)
mutated_mod['func_6649'] = func_6649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6649_call = mutated_mod.get_global_var('func_6649')
call_6650 = func_6649_call()
output = call_6650
func_6651 = relay.Function([], output)
mutated_mod['func_6651'] = func_6651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5689_call = mod.get_global_var('func_5689')
func_5690_call = mutated_mod.get_global_var('func_5690')
call_6657 = relay.TupleGetItem(func_5689_call(), 1)
call_6658 = relay.TupleGetItem(func_5690_call(), 1)
output = call_6657
output2 = call_6658
func_6664 = relay.Function([], output)
mod['func_6664'] = func_6664
mod = relay.transform.InferType()(mod)
output = func_6664()
func_6665 = relay.Function([], output)
mutated_mod['func_6665'] = func_6665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6053_call = mod.get_global_var('func_6053')
func_6055_call = mutated_mod.get_global_var('func_6055')
call_6706 = relay.TupleGetItem(func_6053_call(), 2)
call_6707 = relay.TupleGetItem(func_6055_call(), 2)
output = call_6706
output2 = call_6707
func_6729 = relay.Function([], output)
mod['func_6729'] = func_6729
mod = relay.transform.InferType()(mod)
output = func_6729()
func_6730 = relay.Function([], output)
mutated_mod['func_6730'] = func_6730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4620_call = mod.get_global_var('func_4620')
func_4621_call = mutated_mod.get_global_var('func_4621')
call_6733 = func_4620_call()
call_6734 = func_4620_call()
func_2337_call = mod.get_global_var('func_2337')
func_2340_call = mutated_mod.get_global_var('func_2340')
const_6746 = relay.const(-4, dtype = "uint32")#candidate|6746|()|const|uint32
const_6747 = relay.const([-1,-6,-3,-9,10,-1,10,7,-4,3,3,4,-9,-7,1], dtype = "uint32")#candidate|6747|(15,)|const|uint32
call_6745 = func_2337_call(relay.reshape(const_6746.astype('uint32'), []), relay.reshape(const_6747.astype('uint32'), [1, 1, 15]), )
call_6748 = func_2337_call(relay.reshape(const_6746.astype('uint32'), []), relay.reshape(const_6747.astype('uint32'), [1, 1, 15]), )
bop_6750 = relay.power(const_6746.astype('float64'), call_6745.astype('float64')) # shape=(1, 1, 15)
bop_6753 = relay.power(const_6746.astype('float64'), call_6748.astype('float64')) # shape=(1, 1, 15)
output = relay.Tuple([call_6733,const_6747,bop_6750,])
output2 = relay.Tuple([call_6734,const_6747,bop_6753,])
func_6754 = relay.Function([], output)
mod['func_6754'] = func_6754
mod = relay.transform.InferType()(mod)
output = func_6754()
func_6755 = relay.Function([], output)
mutated_mod['func_6755'] = func_6755
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6773 = relay.const([[[4.343617,-3.531337,7.204757,4.214341,-8.619172],[-5.702835,9.720928,-4.319687,5.564822,-8.346571],[8.779329,-0.052706,3.816519,-9.821296,0.816869],[-5.927947,8.201143,5.252633,-3.002309,5.554294],[-7.045368,0.450049,7.962002,7.126252,8.056134],[-0.782320,-8.644278,-7.160914,7.441938,9.626245],[-8.461296,0.686277,-5.771397,-4.486124,-3.642187],[8.358716,2.567874,-4.452931,-0.467974,9.435839]],[[4.288302,6.418339,9.071385,5.443445,-3.023919],[7.968783,-8.141168,-5.054552,0.289577,0.396551],[-5.330749,-2.904959,-9.646962,-4.975421,-2.652037],[-1.108583,-6.893687,-6.603392,4.953110,-2.854596],[-8.004350,-5.716801,1.934719,4.600961,-0.899574],[-2.445005,-6.292083,-4.474594,6.706802,5.439850],[6.303987,-4.424485,8.941343,0.948888,-2.335831],[7.931182,6.384102,-2.051918,-0.158131,1.652203]],[[-3.737546,-7.034898,-3.003095,2.107513,2.020552],[9.635095,-9.611519,-6.604012,-1.342712,-5.971089],[-5.674794,8.517376,-0.336216,-8.292551,-9.504187],[2.023343,5.259734,2.208139,-3.799884,1.821205],[3.733176,-9.812187,-6.703316,-9.705093,-3.277647],[-7.048672,-1.819092,-3.015098,8.754632,1.282497],[-4.703600,-2.699075,-1.681515,8.415905,3.083081],[8.065025,-6.738181,-1.142001,-9.193960,7.631662]],[[-4.900464,6.297218,-9.234459,2.852495,-1.254592],[3.534715,1.829335,-3.521087,8.558330,-3.260228],[1.756262,7.377161,-0.457825,-9.162301,-9.436617],[1.359005,3.188326,2.562576,0.645264,8.733818],[-2.044307,-3.654716,7.239564,5.384086,9.596717],[4.960607,9.417815,-3.776335,-0.883754,2.305599],[-4.998007,6.935561,7.840187,9.731610,2.821261],[6.125157,0.114299,8.383072,-0.075360,1.243789]],[[4.084264,-6.141895,-2.353418,-3.597513,-2.836122],[7.466047,-6.461062,-3.993633,-2.669887,-5.244574],[8.916872,6.902945,-7.877377,1.544054,1.503677],[-4.572122,0.432175,-3.873160,5.394621,-0.952493],[-0.830040,-3.353292,6.430043,-3.436042,5.986380],[3.251054,-2.421320,4.747412,-9.855570,-6.686734],[-4.375195,-1.204595,1.593723,1.607280,3.030350],[-0.150227,9.523600,-7.865043,-0.743814,-9.015192]],[[-3.700886,-6.167426,-9.067346,9.791556,-1.044142],[8.603955,-6.037515,-4.849341,-9.564367,-8.725771],[7.800728,8.617031,9.298450,0.747035,-9.723217],[8.412854,-0.262203,-0.476164,-3.617790,6.917151],[3.360320,2.183106,-7.593464,4.767661,4.873873],[-7.963860,9.363744,4.983255,9.377520,-2.566568],[5.036202,-6.457312,0.829950,-4.128193,-6.141332],[-6.483262,-4.779805,6.064086,0.267141,1.911171]],[[-6.706479,6.693561,1.275164,7.872255,-5.757828],[2.282525,0.742938,1.966327,-7.095415,-1.383995],[7.514036,-4.390534,-9.385034,-8.304844,-4.712841],[-3.084931,4.129010,-5.841886,9.957901,2.703149],[0.740016,2.152592,5.715826,8.735237,-5.241873],[-3.174117,-8.102773,-9.503261,8.735158,-9.642212],[-8.214146,-4.733042,5.931538,9.503901,-5.638919],[-6.880316,5.591934,1.483970,-5.385730,-2.818776]],[[-1.304882,-2.995696,7.549107,-9.726785,8.514226],[-4.513382,1.610729,7.524982,-2.750015,3.277170],[3.751813,-8.166003,3.188756,4.585567,6.667830],[3.879319,2.610974,-1.937023,-8.466642,2.866469],[-3.281926,6.523118,-7.466413,-9.456642,4.534887],[-9.038478,4.495148,1.982469,-7.034262,-6.678132],[-8.650911,6.256809,9.803383,-3.332648,-1.158555],[8.872405,-5.806434,7.241198,3.910054,1.122977]],[[9.057832,3.162325,-6.397628,-7.089599,-5.107199],[-2.773735,-5.609930,-5.733904,-5.336202,0.093961],[-1.398126,3.617742,7.073556,2.314221,-4.611006],[-0.324300,-9.767966,-6.975679,-0.546966,8.328269],[1.282142,-7.155531,-8.604662,9.229297,5.949024],[3.053376,4.275397,-9.315268,1.829402,6.575493],[-8.097355,-8.327844,1.040832,-6.817707,2.584871],[-5.302287,3.256392,-3.480186,1.064112,-7.033757]],[[-4.209318,-9.548619,-7.915137,-6.847937,3.054128],[5.080935,0.615437,-8.934220,-5.243867,9.065995],[1.947332,-3.015708,-2.470335,-7.410234,-1.462558],[-8.802409,-7.627074,-1.847248,-0.705413,7.134190],[-2.708979,8.784976,-5.653754,3.435389,-7.781417],[-9.849287,-7.361313,5.621808,4.092489,3.334441],[-0.513789,-4.780673,-8.984226,-5.066951,6.349709],[-3.878192,-2.472919,-7.986876,-1.890851,-3.634795]],[[-9.144810,-1.353496,0.018195,3.490084,6.310888],[8.992192,-8.392093,-9.263377,-0.331495,6.832647],[-5.135512,-2.709658,-3.252331,5.039873,-5.200050],[2.994691,-7.847333,2.400163,1.105936,-7.687643],[4.273107,9.924242,3.658313,0.739388,-3.106155],[-7.909207,-2.282949,5.894131,4.513229,1.616648],[-7.262108,-6.111869,-1.612662,9.070911,-3.932302],[-3.845627,2.957723,7.942463,-3.546585,-9.605695]],[[-4.210779,0.102388,5.956996,6.413927,-6.100033],[-1.175901,5.254389,6.826578,5.302100,-9.376547],[2.527460,7.884174,-7.786801,4.211767,5.380106],[1.325185,-9.656432,1.521163,5.734362,-3.149599],[6.193729,8.406677,0.106184,2.391359,2.275762],[-8.222527,-0.125057,7.665183,6.267071,5.404215],[-8.935021,-7.553092,-8.190117,0.553595,-2.116969],[5.193514,-0.706810,-3.911199,7.907487,-3.290683]],[[4.654703,8.618312,9.990279,-7.713458,-5.694368],[2.627655,-7.792625,1.623425,0.536704,1.424848],[2.843628,-8.903121,5.756059,4.887154,-3.274106],[3.509945,9.753237,9.705307,5.627595,3.797494],[-3.120525,-2.187481,-3.616806,5.090491,-5.644673],[8.713003,9.668892,-7.234571,-2.715966,1.658260],[0.725516,8.862390,-8.318440,0.470428,-5.780367],[8.511070,-3.629747,-7.283303,7.978802,-7.194829]],[[-8.055408,8.214184,1.293103,-1.695116,-0.543789],[-3.106368,-4.425904,-8.990950,4.499487,-0.954167],[-6.838765,-0.806877,9.922460,0.284310,-1.865859],[6.035522,1.525698,-1.725206,-4.073379,-6.015217],[-5.610517,-6.046231,-0.393290,9.914297,1.469656],[-4.972765,7.011633,-0.444623,4.836471,-1.794287],[0.814318,-6.878729,-3.207749,-2.710751,5.479370],[0.586621,7.549800,-4.625554,-5.400359,0.765616]],[[0.162312,6.024892,-5.834616,1.694846,0.041538],[2.558118,2.691966,3.570722,-1.932281,-1.293269],[7.024686,-7.581416,-5.114138,-2.574263,-0.158639],[-3.346261,4.087924,1.065068,4.537096,6.316735],[-1.594246,2.674675,-8.113525,2.058338,-7.126402],[-5.200563,-2.388643,2.425393,9.575121,1.189211],[0.306828,2.357388,-8.849603,7.888159,-9.230675],[-7.724549,6.014161,-5.728163,7.266340,1.457445]],[[-9.439447,7.842109,-3.682862,2.612565,-9.875415],[0.524778,-0.819086,8.750956,4.497319,-9.897418],[7.767374,-3.600716,-1.367477,7.141838,5.675075],[-5.540013,-7.203476,-1.848714,-8.220744,2.289343],[-7.416456,-3.482414,3.958608,1.256410,-3.707359],[-2.909533,3.630528,6.237972,-8.579647,3.818763],[4.968205,8.774081,7.203728,-9.344697,5.015399],[-8.638346,-3.611832,-4.049707,-9.830253,2.417878]]], dtype = "float32")#candidate|6773|(16, 8, 5)|const|float32
uop_6774 = relay.atan(const_6773.astype('float32')) # shape=(16, 8, 5)
output = uop_6774
output2 = uop_6774
func_6777 = relay.Function([], output)
mod['func_6777'] = func_6777
mod = relay.transform.InferType()(mod)
output = func_6777()
func_6778 = relay.Function([], output)
mutated_mod['func_6778'] = func_6778
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6835 = relay.var("var_6835", dtype = "uint64", shape = ())#candidate|6835|()|var|uint64
var_6836 = relay.var("var_6836", dtype = "uint64", shape = (15, 6, 14))#candidate|6836|(15, 6, 14)|var|uint64
bop_6837 = relay.subtract(var_6835.astype('uint64'), var_6836.astype('uint64')) # shape=(15, 6, 14)
output = relay.Tuple([bop_6837,])
output2 = relay.Tuple([bop_6837,])
func_6846 = relay.Function([var_6835,var_6836,], output)
mod['func_6846'] = func_6846
mod = relay.transform.InferType()(mod)
var_6847 = relay.var("var_6847", dtype = "uint64", shape = ())#candidate|6847|()|var|uint64
var_6848 = relay.var("var_6848", dtype = "uint64", shape = (15, 6, 14))#candidate|6848|(15, 6, 14)|var|uint64
output = func_6846(var_6847,var_6848,)
func_6849 = relay.Function([var_6847,var_6848,], output)
mutated_mod['func_6849'] = func_6849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4167_call = mod.get_global_var('func_4167')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_6860 = relay.TupleGetItem(func_4167_call(), 0)
call_6861 = relay.TupleGetItem(func_4169_call(), 0)
uop_6862 = relay.sinh(call_6860.astype('float32')) # shape=(14, 15, 9)
uop_6864 = relay.sinh(call_6861.astype('float32')) # shape=(14, 15, 9)
output = relay.Tuple([uop_6862,])
output2 = relay.Tuple([uop_6864,])
func_6870 = relay.Function([], output)
mod['func_6870'] = func_6870
mod = relay.transform.InferType()(mod)
output = func_6870()
func_6871 = relay.Function([], output)
mutated_mod['func_6871'] = func_6871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6664_call = mod.get_global_var('func_6664')
func_6665_call = mutated_mod.get_global_var('func_6665')
call_6894 = func_6664_call()
call_6895 = func_6664_call()
output = relay.Tuple([call_6894,])
output2 = relay.Tuple([call_6895,])
func_6898 = relay.Function([], output)
mod['func_6898'] = func_6898
mod = relay.transform.InferType()(mod)
mutated_mod['func_6898'] = func_6898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6898_call = mutated_mod.get_global_var('func_6898')
call_6899 = func_6898_call()
output = call_6899
func_6900 = relay.Function([], output)
mutated_mod['func_6900'] = func_6900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5548_call = mod.get_global_var('func_5548')
func_5550_call = mutated_mod.get_global_var('func_5550')
call_6904 = relay.TupleGetItem(func_5548_call(), 0)
call_6905 = relay.TupleGetItem(func_5550_call(), 0)
func_5941_call = mod.get_global_var('func_5941')
func_5943_call = mutated_mod.get_global_var('func_5943')
call_6917 = func_5941_call()
call_6918 = func_5941_call()
bop_6929 = relay.bitwise_and(call_6917.astype('int64'), relay.reshape(call_6904.astype('int64'), relay.shape_of(call_6917))) # shape=(14, 15, 9)
bop_6932 = relay.bitwise_and(call_6918.astype('int64'), relay.reshape(call_6905.astype('int64'), relay.shape_of(call_6918))) # shape=(14, 15, 9)
func_3880_call = mod.get_global_var('func_3880')
func_3881_call = mutated_mod.get_global_var('func_3881')
call_6944 = relay.TupleGetItem(func_3880_call(), 0)
call_6945 = relay.TupleGetItem(func_3881_call(), 0)
output = relay.Tuple([bop_6929,call_6944,])
output2 = relay.Tuple([bop_6932,call_6945,])
func_6950 = relay.Function([], output)
mod['func_6950'] = func_6950
mod = relay.transform.InferType()(mod)
output = func_6950()
func_6951 = relay.Function([], output)
mutated_mod['func_6951'] = func_6951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5618_call = mod.get_global_var('func_5618')
func_5620_call = mutated_mod.get_global_var('func_5620')
call_7010 = func_5618_call()
call_7011 = func_5618_call()
output = relay.Tuple([call_7010,])
output2 = relay.Tuple([call_7011,])
func_7013 = relay.Function([], output)
mod['func_7013'] = func_7013
mod = relay.transform.InferType()(mod)
output = func_7013()
func_7014 = relay.Function([], output)
mutated_mod['func_7014'] = func_7014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6870_call = mod.get_global_var('func_6870')
func_6871_call = mutated_mod.get_global_var('func_6871')
call_7015 = relay.TupleGetItem(func_6870_call(), 0)
call_7016 = relay.TupleGetItem(func_6871_call(), 0)
func_5641_call = mod.get_global_var('func_5641')
func_5643_call = mutated_mod.get_global_var('func_5643')
call_7017 = func_5641_call()
call_7018 = func_5641_call()
func_6359_call = mod.get_global_var('func_6359')
func_6361_call = mutated_mod.get_global_var('func_6361')
call_7033 = relay.TupleGetItem(func_6359_call(), 0)
call_7034 = relay.TupleGetItem(func_6361_call(), 0)
output = relay.Tuple([call_7015,call_7017,call_7033,])
output2 = relay.Tuple([call_7016,call_7018,call_7034,])
func_7042 = relay.Function([], output)
mod['func_7042'] = func_7042
mod = relay.transform.InferType()(mod)
mutated_mod['func_7042'] = func_7042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7042_call = mutated_mod.get_global_var('func_7042')
call_7043 = func_7042_call()
output = call_7043
func_7044 = relay.Function([], output)
mutated_mod['func_7044'] = func_7044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4139_call = mod.get_global_var('func_4139')
func_4141_call = mutated_mod.get_global_var('func_4141')
call_7068 = relay.TupleGetItem(func_4139_call(), 0)
call_7069 = relay.TupleGetItem(func_4141_call(), 0)
func_4941_call = mod.get_global_var('func_4941')
func_4944_call = mutated_mod.get_global_var('func_4944')
const_7092 = relay.const(3.661250, dtype = "float32")#candidate|7092|()|const|float32
var_7093 = relay.var("var_7093", dtype = "float32", shape = (84, 2))#candidate|7093|(84, 2)|var|float32
call_7091 = relay.TupleGetItem(func_4941_call(relay.reshape(const_7092.astype('float32'), []), relay.reshape(var_7093.astype('float32'), [168,]), ), 3)
call_7094 = relay.TupleGetItem(func_4944_call(relay.reshape(const_7092.astype('float32'), []), relay.reshape(var_7093.astype('float32'), [168,]), ), 3)
func_342_call = mod.get_global_var('func_342')
func_345_call = mutated_mod.get_global_var('func_345')
const_7100 = relay.const([[-5,-9,2,6,-2,3,-10,-9,-1,3,-5,-6,-6,9,-6,4,-7,4,4,-5,-2,-6,-9,9,8,-7,-2,-5],[10,2,2,9,10,-1,3,9,-4,10,-9,-5,-2,2,-7,-2,-1,-3,2,-2,-5,-5,9,-6,10,-8,4,10],[8,-9,8,-10,-8,2,6,2,-9,10,2,10,-1,-3,-2,10,-4,4,2,3,-8,-2,10,-6,3,-6,-3,7],[5,-10,4,8,2,-1,8,6,10,-2,2,-9,5,9,2,-5,-7,-7,-6,-10,8,5,-9,4,1,-2,-4,-7],[8,1,4,-10,-3,-4,1,9,7,-7,-5,6,5,-10,-10,-9,6,10,-6,-3,-5,-7,-2,8,-10,-6,4,-2],[3,-9,10,-1,8,6,-2,-4,-5,5,-7,9,-8,4,-10,-4,-10,-5,-10,9,-10,5,-6,-10,10,-10,-10,6],[-5,-3,-9,-5,-9,1,7,-9,-7,-8,3,-5,5,2,4,5,-8,-4,3,-8,-2,-2,-1,7,-5,-2,-4,1],[-2,-5,1,-6,8,8,1,-4,6,-3,6,6,6,-10,-5,-2,-4,-3,-6,-3,-1,6,6,-7,5,-9,2,2],[3,8,5,-3,8,-1,7,9,-7,-1,6,-5,-8,1,10,-7,7,9,5,10,-9,8,-7,5,-5,-6,4,1],[8,1,-5,-10,-4,-6,-2,4,5,9,-10,-5,1,-5,3,-5,8,-8,4,9,7,-9,-10,-2,5,-9,8,-2]], dtype = "int32")#candidate|7100|(10, 28)|const|int32
call_7099 = relay.TupleGetItem(func_342_call(relay.reshape(const_7092.astype('int32'), []), relay.reshape(const_7100.astype('int32'), [8, 5, 7]), ), 0)
call_7101 = relay.TupleGetItem(func_345_call(relay.reshape(const_7092.astype('int32'), []), relay.reshape(const_7100.astype('int32'), [8, 5, 7]), ), 0)
func_2044_call = mod.get_global_var('func_2044')
func_2046_call = mutated_mod.get_global_var('func_2046')
call_7115 = relay.TupleGetItem(func_2044_call(relay.reshape(var_7093.astype('float32'), [1, 12, 14])), 0)
call_7116 = relay.TupleGetItem(func_2046_call(relay.reshape(var_7093.astype('float32'), [1, 12, 14])), 0)
func_6729_call = mod.get_global_var('func_6729')
func_6730_call = mutated_mod.get_global_var('func_6730')
call_7127 = func_6729_call()
call_7128 = func_6729_call()
output = relay.Tuple([call_7068,call_7091,const_7092,var_7093,call_7099,const_7100,call_7115,call_7127,])
output2 = relay.Tuple([call_7069,call_7094,const_7092,var_7093,call_7101,const_7100,call_7116,call_7128,])
func_7133 = relay.Function([var_7093,], output)
mod['func_7133'] = func_7133
mod = relay.transform.InferType()(mod)
var_7134 = relay.var("var_7134", dtype = "float32", shape = (84, 2))#candidate|7134|(84, 2)|var|float32
output = func_7133(var_7134)
func_7135 = relay.Function([var_7134], output)
mutated_mod['func_7135'] = func_7135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4053_call = mod.get_global_var('func_4053')
func_4054_call = mutated_mod.get_global_var('func_4054')
call_7220 = relay.TupleGetItem(func_4053_call(), 0)
call_7221 = relay.TupleGetItem(func_4054_call(), 0)
func_5597_call = mod.get_global_var('func_5597')
func_5599_call = mutated_mod.get_global_var('func_5599')
const_7268 = relay.const([4.011813,2.086473,0.601449,-1.380610,9.925307,-9.389025,1.545326,9.358899,-0.910301,3.380378,1.839902,-3.081935,9.886450,1.011173,-3.146724,6.298484,-4.204999,0.218388,-1.271117,-0.176858,9.451098,-5.165357,-0.615213,-8.042886,-7.156817,9.277172,6.441494,5.421921,4.281700,-0.803696,-1.035833,-7.236125,-5.442129,-7.726295,6.714770,-8.479244,-0.920543,7.000059,-6.327175,5.919409,-2.569120,-8.410253,-2.664164,-0.258783,-3.059754,0.514299,-2.557444,-6.443706,5.121230,-2.787286,3.438753,6.557455,9.675325,-0.223247,1.092812,-4.041897,-9.846480,8.474745,-4.179741,8.820266,-6.535649,8.176764,-6.420082,1.255193,4.532068,-1.765006,-9.794722,-6.375090,7.557468,0.505634,-2.342372,-3.851519,5.382349,0.245547,5.971127,-7.673407,2.316545,5.930149,3.295802,2.673340,-2.179908,2.430354,-7.857590,-2.778598,-5.421640,-0.173928,2.750192,-6.836533,-7.295659,-8.101830,-5.517094,-7.181449,-2.870217,9.746849,-8.684334,-4.273104], dtype = "float64")#candidate|7268|(96,)|const|float64
call_7267 = relay.TupleGetItem(func_5597_call(relay.reshape(const_7268.astype('float64'), [48, 2])), 2)
call_7269 = relay.TupleGetItem(func_5599_call(relay.reshape(const_7268.astype('float64'), [48, 2])), 2)
output = relay.Tuple([call_7220,call_7267,const_7268,])
output2 = relay.Tuple([call_7221,call_7269,const_7268,])
func_7272 = relay.Function([], output)
mod['func_7272'] = func_7272
mod = relay.transform.InferType()(mod)
output = func_7272()
func_7273 = relay.Function([], output)
mutated_mod['func_7273'] = func_7273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7272_call = mod.get_global_var('func_7272')
func_7273_call = mutated_mod.get_global_var('func_7273')
call_7304 = relay.TupleGetItem(func_7272_call(), 1)
call_7305 = relay.TupleGetItem(func_7273_call(), 1)
const_7308 = relay.const([[5.704275,-0.573668],[-9.561137,-8.092653],[2.252527,5.791764],[-7.389047,-7.014904],[-3.274896,-0.858873],[-4.764451,4.672566],[3.088882,-9.959880],[1.557054,-9.245230],[-5.950081,-5.457296],[-5.048490,4.418952],[-0.198936,-1.828361],[8.929420,-3.462350],[3.543832,7.549845],[-3.121426,7.197142],[-3.617192,6.906086],[5.684724,-9.497740],[-1.372117,-5.133497],[4.644633,-1.612646],[-9.959770,-9.575939],[0.523243,-1.519990],[7.690302,-1.249089],[-3.581071,-7.682176],[-8.270114,1.743653],[6.039727,4.837973],[-5.888349,-7.641179],[-9.272567,5.508253],[6.498418,-1.759650],[-4.409594,7.344397],[-4.831830,-1.866125],[-7.397920,-0.586913],[-8.592082,-3.636998],[0.076201,4.014474],[-7.021043,-0.784437],[8.394021,2.958103],[8.019853,1.004872],[-8.773261,-8.141192],[2.704818,-4.762187],[6.643891,-8.567599],[-0.599995,3.355631],[-7.352407,8.563774],[-9.767774,4.427892],[6.270725,8.882764],[-2.032314,6.326772],[6.347484,-5.993283],[-1.037552,-3.239331],[9.801478,5.924008],[-8.637288,1.291352],[1.822614,5.845287]], dtype = "float32")#candidate|7308|(48, 2)|const|float32
bop_7309 = relay.power(call_7304.astype('float64'), relay.reshape(const_7308.astype('float64'), relay.shape_of(call_7304))) # shape=(48, 2)
bop_7312 = relay.power(call_7305.astype('float64'), relay.reshape(const_7308.astype('float64'), relay.shape_of(call_7305))) # shape=(48, 2)
func_6870_call = mod.get_global_var('func_6870')
func_6871_call = mutated_mod.get_global_var('func_6871')
call_7316 = relay.TupleGetItem(func_6870_call(), 0)
call_7317 = relay.TupleGetItem(func_6871_call(), 0)
output = relay.Tuple([bop_7309,call_7316,])
output2 = relay.Tuple([bop_7312,call_7317,])
func_7322 = relay.Function([], output)
mod['func_7322'] = func_7322
mod = relay.transform.InferType()(mod)
mutated_mod['func_7322'] = func_7322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7322_call = mutated_mod.get_global_var('func_7322')
call_7323 = func_7322_call()
output = call_7323
func_7324 = relay.Function([], output)
mutated_mod['func_7324'] = func_7324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4053_call = mod.get_global_var('func_4053')
func_4054_call = mutated_mod.get_global_var('func_4054')
call_7374 = relay.TupleGetItem(func_4053_call(), 0)
call_7375 = relay.TupleGetItem(func_4054_call(), 0)
uop_7376 = relay.asinh(call_7374.astype('float32')) # shape=(14, 15, 9)
uop_7378 = relay.asinh(call_7375.astype('float32')) # shape=(14, 15, 9)
func_5618_call = mod.get_global_var('func_5618')
func_5620_call = mutated_mod.get_global_var('func_5620')
call_7380 = func_5618_call()
call_7381 = func_5618_call()
output = relay.Tuple([uop_7376,call_7380,])
output2 = relay.Tuple([uop_7378,call_7381,])
func_7391 = relay.Function([], output)
mod['func_7391'] = func_7391
mod = relay.transform.InferType()(mod)
mutated_mod['func_7391'] = func_7391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7391_call = mutated_mod.get_global_var('func_7391')
call_7392 = func_7391_call()
output = call_7392
func_7393 = relay.Function([], output)
mutated_mod['func_7393'] = func_7393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5641_call = mod.get_global_var('func_5641')
func_5643_call = mutated_mod.get_global_var('func_5643')
call_7422 = func_5641_call()
call_7423 = func_5641_call()
func_6846_call = mod.get_global_var('func_6846')
func_6849_call = mutated_mod.get_global_var('func_6849')
var_7430 = relay.var("var_7430", dtype = "uint64", shape = ())#candidate|7430|()|var|uint64
const_7431 = relay.const([4,-7,10,4,1,1,-6,9,-6,-6,-1,1,8,7,-3,-4,-6,-8,4,6,-9,-1,-6,9,-3,1,5,7,-8,-9,-1,-9,-4,3,6,1,-8,2,-5,6,-7,-1,-6,6,-5,4,8,4,10,-7,-7,-4,5,9,-9,9,1,-8,10,-3,-9,-10,-2,-8,-2,-9,-7,5,10,-1,8,-5,-10,8,-9,5,-7,6,1,-2,-10,3,-5,-9,-2,-4,-2,1,-3,4,-9,-1,-7,-8,2,-1,-4,-10,-3,-3,-1,5,-7,-7,-5,-4,1,-5,-2,-5,6,7,-2,-8,-9,-8,-10,-6,-9,-9,4,-1,9,-1,10,5,4,3,-2,9,-1,-4,9,-10,-2,3,2,-3,1,-2,-2,6,-1,-1,9,4,10,5,-7,10,-3,9,8,-6,6,9,-3,3,3,6,-8,5,10,7,-2,9,9,-1,-10,5,3,1,8,-1,-9,-2,9,3,7,7,7,7,5,-3,6,-10,-2,6,-6,1,-6,-2,-2,4,-7,1,6,1,5,-6,-4,10,7,7,7,-1,-1,-7,10,-4,-2,-4,-10,-2,9,-8,4,10,-7,7,3,6,2,8,-5,-10,7,7,-9,6,5,-10,3,-2,-4,-4,-8,-4,-2,-4,-5,5,-8,-1,9,6,1,-5,-5,5,-8,10,-7,-8,-7,7,-7,-5,-5,4,4,-10,-6,-1,3,-4,-5,9,-7,1,7,7,2,-9,-10,1,-2,1,5,1,-8,-1,9,2,-6,9,5,-7,8,4,-10,-4,-5,2,-6,9,10,-6,-1,3,3,1,10,7,-6,7,-5,8,-5,3,5,-5,4,-2,-2,-2,-10,5,1,-1,-2,-2,-9,-8,-5,8,-2,5,-8,1,-3,-5,6,-5,3,-7,-4,3,-1,2,3,-6,-6,-3,7,2,-6,4,-8,-10,-5,-5,6,-6,8,-5,-7,6,-1,8,2,7,-9,-2,2,-8,-9,-7,1,-3,1,-2,8,-4,6,6,-1,7,-8,7,-1,6,-9,6,-8,1,-9,-8,10,8,3,7,1,-6,-3,8,1,3,-8,-10,-7,6,5,-5,-7,2,-8,-7,-2,-7,-7,8,-8,-6,7,-5,-10,-2,-6,-9,-1,6,-1,-8,6,-10,10,-9,-9,7,4,2,-2,6,-1,-2,7,2,10,2,7,9,2,-8,-4,8,-4,1,-3,3,-3,6,4,9,-8,-10,-5,-4,8,9,-4,1,5,3,10,-4,10,2,-6,10,1,10,-10,4,-4,-3,10,-6,7,-5,-7,1,-6,3,-3,9,2,2,4,1,3,-6,-7,9,6,-2,-10,-10,5,2,6,-4,1,-10,5,2,-5,-10,3,-8,-1,1,3,-2,5,-6,7,9,5,-2,-3,6,-3,2,-6,-6,-1,10,8,-10,-6,-4,-6,1,-4,-2,7,7,-6,7,-7,9,-8,2,9,-9,-10,-7,9,8,1,2,-9,8,-8,-7,8,5,-3,3,10,-8,-6,7,-5,1,-4,-3,-2,8,8,4,-1,3,7,9,-8,8,-4,-1,9,-6,-5,-7,10,6,1,3,3,10,-1,-7,-8,3,9,2,6,-2,6,7,-5,5,4,-9,-5,-5,10,5,7,1,-2,8,2,6,-9,8,-5,-1,-3,6,-1,-6,4,-10,-7,-1,-5,-6,8,7,-4,-3,-7,10,5,2,8,9,-7,-7,8,-5,6,10,-3,3,-1,8,1,10,5,-1,7,-7,7,-9,1,-9,-5,-2,5,8,4,-4,6,-8,-5,4,-9,6,-6,-2,-1,7,-10,-6,6,1,-2,4,8,-8,3,4,-6,7,-9,10,-1,-8,8,8,-8,4,5,-7,-10,-5,-1,-4,-3,-9,-1,2,10,5,-4,1,-3,1,5,-10,-4,-9,-7,-2,-5,3,-3,-9,5,-8,8,-10,-6,-10,6,7,8,5,-8,-6,-7,10,5,1,-5,10,10,-6,-8,9,-8,-6,-2,-2,7,5,8,-5,7,3,-7,-5,3,-5,-10,7,-1,-6,3,5,-5,-5,6,-6,-8,-4,3,1,-3,-7,1,4,-4,-4,8,8,-10,8,4,8,4,6,3,3,6,-10,-3,-10,5,-5,-3,-6,-7,10,8,-3,10,-2,-9,-9,-5,3,-5,7,4,3,-5,2,-1,3,-10,4,6,-5,10,-9,4,5,4,9,3,7,9,10,-4,3,-1,-6,-2,-3,6,9,5,-9,-5,-9,10,-6,7,-3,3,7,-3,-3,3,-9,-2,-8,4,8,-6,10,4,7,4,-4,-5,10,-3,5,1,-6,-2,-1,-2,6,7,7,1,-3,-5,-1,8,-10,-4,-9,-9,-9,-9,-9,-9,-10,2,8,-1,-8,9,-9,-3,-10,-6,-4,-3,-7,-3,-5,3,1,-3,9,-3,10,-8,-1,-10,8,3,2,-4,10,5,-2,-9,4,-3,5,1,7,6,10,2,-3,-1,1,-4,-3,-6,-9,-7,8,5,-5,1,-8,2,5,10,-9,3,-4,-2,-7,-3,5,1,-1,9,5,-10,8,-2,9,1,1,-9,2,-6,-2,-7,-1,2,-5,8,10,-4,3,1,8,-10,-7,-5,-10,10,-2,-1,-5,2,6,9,-1,6,9,-6,1,-7,4,-9,-5,-8,-6,-7,-4,1,1,7,5,6,1,2,-7,-2,10,-5,10,1,2,9,7,5,-1,1,-8,-1,-8,-2,-1,6,-6,6,2,-4,-5,10,2,-3,-10,3,1,6,9,6,2,1,3,-4,7,9,2,6,-7,-8,-3,-2,5,8,5,3,-8,-5,-4,-5,-8,4,4,-3,9,7,-4,-10,8,-2,4,2,2,2,-8,-8,1,-6,2,-5,3,-6,-10,6,4,3,-5,-1,-2,-6,10,-7,-6,4,-2,-2,1,-2,4,-9,5,-10,6,-1,2,9,1,-1,-8,-8,5,7,-8,5,6,2,-5,-4,-2,9,2,8,-3,2,-5,6,-8,6,-4,10,6,-1,-4,3,-2,4,10,7,10,-7,-10,6,5,-6,2,9,9,10,9,-3,-8,4,8,3,3,-4,-2,10,10,-8,-3,-2,-9,8,-6,6,6,1,-3,4,4,-6,-6,-8,6,1,-3,2,5,-9,-10,6,6,2,4,5,3,6,10,8,-10,-5,-3,-6,-10,-1,1,-8,7,-6,7,-8,-5,-2,10,10,10,-4,6,-3,-6,-5,-2,-6,7,9,-5,4,1,4,-7,-3,2,10,-9,2,-7,-4,4,-9,2,-4,-5,9,-6,9,-9,-10,2,-9,-5,6,-2,3,2,4,10,-3,8,-4,4,8,8,4,-2,-8,-6,8,-9,-3,-3,-5,4,-9,-9,-7,-8], dtype = "uint64")#candidate|7431|(1260,)|const|uint64
call_7429 = relay.TupleGetItem(func_6846_call(relay.reshape(var_7430.astype('uint64'), []), relay.reshape(const_7431.astype('uint64'), [15, 6, 14]), ), 0)
call_7432 = relay.TupleGetItem(func_6849_call(relay.reshape(var_7430.astype('uint64'), []), relay.reshape(const_7431.astype('uint64'), [15, 6, 14]), ), 0)
func_2998_call = mod.get_global_var('func_2998')
func_3001_call = mutated_mod.get_global_var('func_3001')
var_7437 = relay.var("var_7437", dtype = "int16", shape = (2912,))#candidate|7437|(2912,)|var|int16
call_7436 = relay.TupleGetItem(func_2998_call(relay.reshape(var_7430.astype('int16'), []), relay.reshape(var_7437.astype('int16'), [13, 14, 16]), ), 0)
call_7438 = relay.TupleGetItem(func_3001_call(relay.reshape(var_7430.astype('int16'), []), relay.reshape(var_7437.astype('int16'), [13, 14, 16]), ), 0)
output = relay.Tuple([call_7422,call_7429,var_7430,const_7431,call_7436,var_7437,])
output2 = relay.Tuple([call_7423,call_7432,var_7430,const_7431,call_7438,var_7437,])
func_7440 = relay.Function([var_7430,var_7437,], output)
mod['func_7440'] = func_7440
mod = relay.transform.InferType()(mod)
var_7441 = relay.var("var_7441", dtype = "uint64", shape = ())#candidate|7441|()|var|uint64
var_7442 = relay.var("var_7442", dtype = "int16", shape = (2912,))#candidate|7442|(2912,)|var|int16
output = func_7440(var_7441,var_7442,)
func_7443 = relay.Function([var_7441,var_7442,], output)
mutated_mod['func_7443'] = func_7443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4139_call = mod.get_global_var('func_4139')
func_4141_call = mutated_mod.get_global_var('func_4141')
call_7517 = relay.TupleGetItem(func_4139_call(), 0)
call_7518 = relay.TupleGetItem(func_4141_call(), 0)
output = call_7517
output2 = call_7518
func_7529 = relay.Function([], output)
mod['func_7529'] = func_7529
mod = relay.transform.InferType()(mod)
mutated_mod['func_7529'] = func_7529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7529_call = mutated_mod.get_global_var('func_7529')
call_7530 = func_7529_call()
output = call_7530
func_7531 = relay.Function([], output)
mutated_mod['func_7531'] = func_7531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6754_call = mod.get_global_var('func_6754')
func_6755_call = mutated_mod.get_global_var('func_6755')
call_7576 = relay.TupleGetItem(func_6754_call(), 2)
call_7577 = relay.TupleGetItem(func_6755_call(), 2)
func_3776_call = mod.get_global_var('func_3776')
func_3778_call = mutated_mod.get_global_var('func_3778')
call_7584 = relay.TupleGetItem(func_3776_call(), 0)
call_7585 = relay.TupleGetItem(func_3778_call(), 0)
func_6870_call = mod.get_global_var('func_6870')
func_6871_call = mutated_mod.get_global_var('func_6871')
call_7631 = relay.TupleGetItem(func_6870_call(), 0)
call_7632 = relay.TupleGetItem(func_6871_call(), 0)
var_7644 = relay.var("var_7644", dtype = "float64", shape = (15, 1, 15))#candidate|7644|(15, 1, 15)|var|float64
bop_7645 = relay.multiply(call_7576.astype('float32'), var_7644.astype('float32')) # shape=(15, 1, 15)
bop_7648 = relay.multiply(call_7577.astype('float32'), var_7644.astype('float32')) # shape=(15, 1, 15)
func_6649_call = mod.get_global_var('func_6649')
func_6651_call = mutated_mod.get_global_var('func_6651')
call_7652 = relay.TupleGetItem(func_6649_call(), 0)
call_7653 = relay.TupleGetItem(func_6651_call(), 0)
uop_7655 = relay.log2(var_7644.astype('float32')) # shape=(15, 1, 15)
output = relay.Tuple([call_7584,call_7631,bop_7645,call_7652,uop_7655,])
output2 = relay.Tuple([call_7585,call_7632,bop_7648,call_7653,uop_7655,])
func_7657 = relay.Function([var_7644,], output)
mod['func_7657'] = func_7657
mod = relay.transform.InferType()(mod)
var_7658 = relay.var("var_7658", dtype = "float64", shape = (15, 1, 15))#candidate|7658|(15, 1, 15)|var|float64
output = func_7657(var_7658)
func_7659 = relay.Function([var_7658], output)
mutated_mod['func_7659'] = func_7659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6435_call = mod.get_global_var('func_6435')
func_6436_call = mutated_mod.get_global_var('func_6436')
call_7672 = func_6435_call()
call_7673 = func_6435_call()
func_5926_call = mod.get_global_var('func_5926')
func_5927_call = mutated_mod.get_global_var('func_5927')
call_7687 = func_5926_call()
call_7688 = func_5926_call()
uop_7712 = relay.acosh(call_7687.astype('float64')) # shape=(14, 15, 9)
uop_7714 = relay.acosh(call_7688.astype('float64')) # shape=(14, 15, 9)
func_4620_call = mod.get_global_var('func_4620')
func_4621_call = mutated_mod.get_global_var('func_4621')
call_7719 = func_4620_call()
call_7720 = func_4620_call()
func_7133_call = mod.get_global_var('func_7133')
func_7135_call = mutated_mod.get_global_var('func_7135')
var_7736 = relay.var("var_7736", dtype = "float32", shape = (168,))#candidate|7736|(168,)|var|float32
call_7735 = relay.TupleGetItem(func_7133_call(relay.reshape(var_7736.astype('float32'), [84, 2])), 0)
call_7737 = relay.TupleGetItem(func_7135_call(relay.reshape(var_7736.astype('float32'), [84, 2])), 0)
output = relay.Tuple([call_7672,uop_7712,call_7719,call_7735,var_7736,])
output2 = relay.Tuple([call_7673,uop_7714,call_7720,call_7737,var_7736,])
func_7739 = relay.Function([var_7736,], output)
mod['func_7739'] = func_7739
mod = relay.transform.InferType()(mod)
mutated_mod['func_7739'] = func_7739
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7740 = relay.var("var_7740", dtype = "float32", shape = (168,))#candidate|7740|(168,)|var|float32
func_7739_call = mutated_mod.get_global_var('func_7739')
call_7741 = func_7739_call(var_7740)
output = call_7741
func_7742 = relay.Function([var_7740], output)
mutated_mod['func_7742'] = func_7742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5941_call = mod.get_global_var('func_5941')
func_5943_call = mutated_mod.get_global_var('func_5943')
call_7747 = func_5941_call()
call_7748 = func_5941_call()
func_5012_call = mod.get_global_var('func_5012')
func_5015_call = mutated_mod.get_global_var('func_5015')
var_7762 = relay.var("var_7762", dtype = "float32", shape = ())#candidate|7762|()|var|float32
call_7761 = relay.TupleGetItem(func_5012_call(relay.reshape(var_7762.astype('float32'), [])), 1)
call_7763 = relay.TupleGetItem(func_5015_call(relay.reshape(var_7762.astype('float32'), [])), 1)
func_5088_call = mod.get_global_var('func_5088')
func_5090_call = mutated_mod.get_global_var('func_5090')
call_7764 = relay.TupleGetItem(func_5088_call(), 1)
call_7765 = relay.TupleGetItem(func_5090_call(), 1)
uop_7770 = relay.asin(call_7761.astype('float32')) # shape=(13, 14, 3)
uop_7772 = relay.asin(call_7763.astype('float32')) # shape=(13, 14, 3)
var_7775 = relay.var("var_7775", dtype = "float32", shape = (13, 14, 3))#candidate|7775|(13, 14, 3)|var|float32
bop_7776 = relay.minimum(uop_7770.astype('float64'), relay.reshape(var_7775.astype('float64'), relay.shape_of(uop_7770))) # shape=(13, 14, 3)
bop_7779 = relay.minimum(uop_7772.astype('float64'), relay.reshape(var_7775.astype('float64'), relay.shape_of(uop_7772))) # shape=(13, 14, 3)
func_6001_call = mod.get_global_var('func_6001')
func_6003_call = mutated_mod.get_global_var('func_6003')
const_7793 = relay.const([3.216974,-3.407279,-5.371714,4.100517,-3.388031,2.110253,-9.958896,-2.613957,-6.004611,8.687507,2.108003,-4.517090,-7.482026,-5.374568,-0.039965,-0.620011,4.003738,7.086593,2.190632,3.631365,5.052148,-6.329127,8.899904,-1.885763,7.111370,-6.962344,1.328673,8.561414,5.451991,3.293480,-6.069516,-3.038676,7.615230,7.913909,-0.051564,-3.034923,-5.358016,8.662981,-7.821186,9.407046,-9.436499,-4.146851,-1.425449,1.126654,1.748231,2.781433,-8.163353,8.758415,8.226282,-8.220955,6.970130,4.097595,4.912436,-6.672527,-3.499904,5.437499,1.396035,-6.367144,4.927999,-5.333624,1.664331,0.022912,5.191477,6.003301,1.620907,-6.393315,-0.430773,-7.550436,5.522222,7.475697,-4.047449,-3.631515,5.165813,4.195152,-4.345721,4.117081,3.809705,9.386994,-0.304657,5.093330,-1.749775,-4.507097,3.479441,5.981137,4.747540,9.106802,9.346601,-6.397024,-9.455021,-5.302411,5.979041,-6.600964,-7.174812,3.195899,-6.514886,-8.940551,-0.955101,-5.663577,-5.946360,-4.406352,-0.055602,7.535311,8.573616,-3.773511,-3.435551,-4.675608,1.193660,-1.042524,-5.227248,-4.990984,8.890548,-7.906317,9.522575,3.560280,-3.927586,-4.342300,3.839043,-1.749049,3.050223,9.623836,4.951241,5.274074,-8.415887,-9.401190,3.405968,-0.511106,-4.673857,-8.913815,2.785504,3.364464,-2.002167,-0.898259,9.892154,-5.738494,-9.921364,-6.878244,-0.756759,-5.077444,-2.142091,1.131015,4.835182,-3.843188,-6.779740,6.511232,-5.698629,8.569683,-4.747328,2.616322,7.140724,-4.716512,5.119718,3.234541,-3.833841,-4.155546,1.888344,-5.643905,1.171280,-5.001216,-6.592559,4.020308,-9.980138,6.925007,3.453193,-6.032400,-0.569678,-8.562963,-0.085926,2.825061,4.155202,1.322444,-0.471216,2.750217,-5.657513,6.789488,2.311938,8.704027,-3.187336,3.825886,9.358867,-7.085104,-9.553980,1.983909,-7.061422,-8.542966,2.464391,-5.963087,3.512663,9.968260,4.075906,-9.670803,-4.414560,-4.525381,-7.287897,-2.177911,-7.273763,-4.310827,0.935707,8.246475,-8.656633,1.326301,5.851814,4.705919,1.298006,-0.098561,-7.343429,3.637738,-0.326328,0.227047,0.858361,0.687108,-7.346194,2.483398,0.775439,9.482176,-4.669293,6.472883,1.105415,-8.930485,-0.948162,3.579397,-5.577714,8.987611,8.347458,4.433669,-2.337679,-7.522377,-1.621401,-7.134458,-9.445465,-7.538820,-0.653528,-1.486732,-5.213611,-3.322997,5.948102,8.812126,-7.354742,-3.476662,2.088462,3.410650,-7.072391,-7.796551,9.686585,7.882055,2.217411,-1.202697,6.576995,0.337803,0.897167,-1.233707,9.548552,-2.550224,-7.413081,0.539881,3.169400,7.380685,-4.600186,-4.826112,-3.350439,7.997925,4.494147,1.164407,-7.972264,8.941306,-5.027337,-2.463016,0.686310,-9.536607,-6.844088,-3.593861,-8.174009,7.666573,1.594717,-5.721908,5.261593,3.630791,3.374243,-6.546053,7.881757,4.992357,5.632678,-8.574113,1.522763,5.411388,-0.501383,6.183231,8.686813,-1.114736,-0.658075,3.572411,-2.028586,8.139850,1.225515,-0.208643,8.650042,1.951486,4.788830,5.401824,-6.699502,-7.292830,-2.320251,9.928330,5.731722,5.213072,-8.722067,5.798993,3.722526,-0.122666,-0.100431,-1.955356,-7.637899,5.547464,2.865178,-5.199252,2.084708,-3.479232,-6.358853,5.252484,2.550820,-2.653197,2.386764,6.372342,-4.923319,-6.997605,-6.183022,-5.753787,-4.771622,-4.738293,-9.653206,0.899080,-0.935486,-5.892475,5.825249,-8.493986,-7.776648,-8.685850,-6.158945,-0.045216,5.176031,-2.557478,5.333655,-8.085720,-1.668190,1.757698,-9.163664,-5.792385,2.107043,8.940715,-2.586784,8.029409,-7.131915,8.253289,4.641564,3.457866,-4.435723,-3.880046,-8.565273,7.813002,-3.651375,-4.567449,5.700698,5.876844,2.109398,1.331569,-6.835746,-2.704316,-3.019724,6.973928,3.054407,-3.636478,-7.284675,-5.764869,7.801289,3.718054,-6.873461,-9.227843,-8.143492,-3.440921,5.656143,-1.045769,3.061194,-9.760009,-4.232895,9.384875,4.081044,9.159111,1.794720,-0.569621,4.192345,-4.558415,7.623753,2.729375,-8.919802,0.101732,5.683700,3.045350,-0.402673,-1.529582,9.386295,7.778006,5.772840,1.641468,-0.458625,3.103273,2.488150,0.698624,5.773450,6.928311,9.113852,5.478015,-7.619836,6.028616,-3.856946,5.831519,9.394504,-5.670199,0.078714,6.211072,-2.831237,6.452135,-9.902834,-6.298814,9.616138,2.298500,7.206700,2.081006,7.883445,-1.994431,-8.626106,-1.988527,-1.844650,-7.492255,-1.147117,8.495452,-4.080228,-3.937017,-6.769700,-2.484227,-3.312788,-6.155818,-3.299450,8.112894,-9.972875,-0.389067,4.937169,-9.629974,6.754182,5.672666,1.269699,-1.539610,1.307952,-7.983061,-1.853794,7.307719,3.723537,-7.250978,8.531512,1.588260,2.920913,-9.898380,-7.561617,8.833000,7.106727,9.263294,2.465038,2.472540,0.448583,-1.357950,-5.849372,-4.837353,6.707519,-4.056665,4.623091,-0.341820,7.972848,7.764040,-9.441176,8.458129,-2.182311,-5.274513,1.053815,-3.903384,7.752463,-2.222786,3.393345,7.543912,6.573170,1.234070,-5.394367,5.335882,2.049985,0.021384,5.721125,6.259316,-4.488910,-4.286820,0.539632,-9.518705,8.889635,9.637848,5.017630,-3.082958,-0.238787,9.133248,4.445457,-9.551601,-3.709935,-1.320154,-8.773481,6.443393,5.707522,-7.519950,-6.150996,-1.869122,3.373945,-3.889460,-8.919161,2.087095,2.432113,7.946759,-5.786201,6.069719,-4.408921,-3.893020,8.388659,3.354739,6.885770,-4.218916,-7.050416,-5.472906,-4.963226,-5.522330,4.150553,6.044271,0.637214,2.871206,-9.720260,-1.839695,3.067438,9.510448,-3.500698,4.821049,1.778655,7.021571,-9.964857,7.293084,6.382151,-0.434289,-1.238511,8.688805,-8.763462,9.172288,4.829050,5.665857,-2.670054,0.140630,9.937931,2.096327,-5.815294,-3.936957,-8.291084,5.358364,-7.842937,-6.064073,8.187404,-8.684594,-9.823327,-9.816756,3.569825,-6.113025,0.411748,-9.153251,7.320358,1.862299,-6.938315,-4.716400,2.356502,-2.569015,5.042441,-2.561527,-9.923149,6.858835,-9.299641,-5.468685,9.604753,-4.598754,1.817744,-8.448115,-6.099233,-2.737444,0.496858,5.172828,3.839741,-8.644922,-0.938039,3.444168,5.599384,4.275269,2.965783,0.791673,1.931850,3.005852,-0.655248,1.407053,5.023305,-5.170645,-8.029759,4.920758,1.757107,9.432843,0.585239,1.516664,5.153928,-4.937741,-9.882455,6.023376,8.023849,-9.263119,-2.411472,-3.808080,-6.727888,9.227340,-5.026824,-9.723472,-6.816963,4.291423,-5.330272,6.115974,-8.202965,-6.661074,3.714578,-4.993491,-6.529613,6.048860,-9.190720,-4.661537,-6.723099,7.716498,6.866734,-2.862849,1.009837,5.093110,-9.265970,7.017799,-1.161694,-5.361246,-2.403579,1.800907,2.590570,8.243831,-7.136598,-5.666429,0.988255,-3.528854,7.367185,9.500970,-7.045371,1.889578,5.039658,5.338309,-1.641804,5.873463,-5.895967,-4.558730,3.069940,6.006538,0.679198,-9.414433,-7.850938,0.290317,-7.011376,-7.940267,6.456100,7.737139,4.905186,8.748199,-4.397477,-3.765483,3.181710,5.354035,-1.723874,-1.505951,-4.400141,7.472287,1.005510,4.260492,1.732471,0.409125,4.357794,8.297325,4.957043,-9.661703,4.031907,4.531934,2.734891,-9.895860,5.629878,-5.938199,6.760414,-2.999139,-4.466813,-6.419915,-4.041165,6.740418,4.288075,-6.194526,1.290219,-4.602244,5.826571,9.557193,-4.623309,-0.767532,-6.420019,-8.701070,-4.936205,9.106348,-7.109909,-7.088047,9.436485,-1.025210,-6.076258,6.232005,2.011333,3.715489,8.482730,-8.432269,-8.253679,-5.968565,4.305462,-2.700694,6.554283,-3.266650,-9.788543,-5.550128,-2.248021,-5.484476,1.230399,-8.225479,9.233697,8.610910,-6.281930,3.393685,6.449415,-6.947245,-1.395549,-4.898769,-9.360594,6.899672,-1.553644,-1.154671,-7.068730,8.960452,-7.780129,-9.651748,5.956402,2.887413,4.321796,-8.023201,-7.181699,6.110642,-4.593156,-1.527508,2.925456,2.205346,-8.696708,-4.594983,-8.044668,-9.816473,-9.709736,-8.616925,4.581046,3.761899,-5.744416,7.130734,-3.200671,9.670629,-0.574787,3.249931,0.729480,9.032223,-9.415588,-0.611304,-3.723888,-6.310700,-7.973852,-8.324346,-8.100451,-8.735746,-8.115356,3.791921,4.722848,5.497985,-0.434922,0.098025,3.993004,5.008171,-3.008004,-9.985849,2.832639,1.462398,8.861550,7.375815,-4.259109,3.117399,6.555198,2.837535,1.674406,-8.288008,-8.214493,-7.275035,9.783821,7.323253,8.029195,-4.547391,-9.024183,-7.817993,7.498081,2.666642,-9.312820,-4.085245,6.850409,-8.022669,-1.909259,7.768235,-8.246052,-8.358024,5.158913,9.789749,3.019252,0.633833,-6.387901,-6.406049,3.658536,1.873995,-7.489313,0.840117,6.488368,-8.010527,3.805810,-4.066661], dtype = "float32")#candidate|7793|(840,)|const|float32
call_7792 = relay.TupleGetItem(func_6001_call(relay.reshape(const_7793.astype('float32'), [840,])), 1)
call_7794 = relay.TupleGetItem(func_6003_call(relay.reshape(const_7793.astype('float32'), [840,])), 1)
output = relay.Tuple([call_7747,var_7762,call_7764,bop_7776,call_7792,const_7793,])
output2 = relay.Tuple([call_7748,var_7762,call_7765,bop_7779,call_7794,const_7793,])
func_7796 = relay.Function([var_7762,var_7775,], output)
mod['func_7796'] = func_7796
mod = relay.transform.InferType()(mod)
var_7797 = relay.var("var_7797", dtype = "float32", shape = ())#candidate|7797|()|var|float32
var_7798 = relay.var("var_7798", dtype = "float32", shape = (13, 14, 3))#candidate|7798|(13, 14, 3)|var|float32
output = func_7796(var_7797,var_7798,)
func_7799 = relay.Function([var_7797,var_7798,], output)
mutated_mod['func_7799'] = func_7799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4139_call = mod.get_global_var('func_4139')
func_4141_call = mutated_mod.get_global_var('func_4141')
call_7817 = relay.TupleGetItem(func_4139_call(), 0)
call_7818 = relay.TupleGetItem(func_4141_call(), 0)
output = call_7817
output2 = call_7818
func_7823 = relay.Function([], output)
mod['func_7823'] = func_7823
mod = relay.transform.InferType()(mod)
output = func_7823()
func_7824 = relay.Function([], output)
mutated_mod['func_7824'] = func_7824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mod.get_global_var('func_4689')
func_4690_call = mutated_mod.get_global_var('func_4690')
call_7850 = relay.TupleGetItem(func_4689_call(), 1)
call_7851 = relay.TupleGetItem(func_4690_call(), 1)
func_5426_call = mod.get_global_var('func_5426')
func_5428_call = mutated_mod.get_global_var('func_5428')
const_7856 = relay.const([4.004402,-2.256432,-0.012571,-4.609495,-9.471117,-5.231724,-6.560002,6.583140,4.827137,6.063899,-7.317175,-3.297684,5.109907,-2.628881,4.612639,2.787104,3.792646,9.631103,-2.568481,-0.987826,-9.974482,-5.078457,-6.424407,-7.255774,-4.378740,6.788400,-5.763171,8.680361,-4.137804,-1.419171,-7.412092,-9.656774,-5.364901,0.067679,5.271379,8.375697,0.922125,8.136635,1.074206,8.837972,5.079212,0.022772,-9.086174,6.367907,-1.087907,4.306218,-2.444196,-1.594861,4.024416,4.915752,3.327410,0.473301,-8.273375,0.205353,-4.712180,8.349809,8.652149,9.977186,5.254493,-4.441647,-7.752055,7.721549,-0.600816,8.250823,6.295350,-2.838941,6.466865,8.189374,-8.366983,-1.992525,-7.589938,-6.171322,-5.047081,2.851838,5.087674,4.566663,5.725707,-4.372564,4.291221,-7.491350,-7.563620,1.549775,-4.253801,2.504040,5.202965,8.731562,1.638879,7.840662,6.238010,8.464030,8.850912,-5.358363,4.099763,-0.225125,3.416252,-4.799453,7.356314,5.391317,-7.762974,6.120854,-5.804034,9.222608,-6.381386,7.837328,-7.027952,-0.300489,-3.727405,-7.565420,1.195591,-5.009654,8.466770,-8.077136,-0.180700,-8.699678,-1.274440,8.673683,-7.031506,-6.660320,8.679522,-9.712700,8.613336,4.135588,-7.247249,0.065990,-2.164216,-9.517038,-2.269022,3.374522,-3.210364,-9.477250,8.578818,-5.043984,-2.411546,-9.026892,-6.776822,6.521266,-1.440186,3.726082,5.265559,-8.455414,-3.747719,8.358758,-0.828268,-9.324333,5.765537,2.838456,-1.899382,-9.739872,8.552198,-2.306305,-6.991148,4.144479,2.737596,7.018542,7.384587,-4.260605,-3.047064,8.141845,-1.892612,2.425717,-7.470932,-2.673178,-3.869935,9.346785,-8.695237,-5.892821,-2.435992,3.150432,-9.583393,-3.493088,-0.945443,-9.869373,-5.133671,4.611332,2.815798,-2.873574,-9.435532,-2.072149,-3.315114,-2.040379,7.826961,1.062643,-3.627162,3.098189,8.434493,-1.588790,4.989960,-3.223565,-0.769727,-6.503167,-3.993579,9.662141,-5.918237,-6.056833,-1.234262,5.935774,0.861892,2.331573,7.333614,-2.657526,-0.022478,-1.829790,6.192387,8.120917,9.808780,8.306799,4.272435,-0.593784,-2.426222,-2.369725,4.853389,5.613122,-3.079137,-4.168738,5.983630,-4.699809,8.476368,3.214339,3.258543,1.090989,1.008517,-9.227500,2.302133,-4.895161,7.931681,-0.765820,-4.983749,5.562628,-4.508589,-6.022472,4.681143,4.811055,8.508196,3.388108,-6.448259,9.685331,-3.581900,-1.081444,-5.346318,3.412246,9.804740,-4.773135,2.723550,-2.645260,2.822329,-6.434280,3.581958,-0.910564,-0.954685,0.646558,-3.533279,-6.788450,-5.347397,-1.718835,3.786241,7.444975,-9.173144,-7.609997,0.210648,3.898843,8.595736,8.523298,-9.477368,-3.016771,-1.053354,9.290078,-7.328191,8.442992,-7.337675,-9.174385,8.182534,-6.035613,8.506497,-2.741102,0.034852,-3.572626,7.744787,3.897942,9.566652,-2.642699,7.490388,-2.427376,-8.470748,-0.765370,1.161495,-6.521943,-1.531353,-8.409976,-0.347604,2.081169,8.191119,-2.004957,9.465105,-2.167297,4.884044,-7.377730,-7.625506,8.648098,-7.746379,0.100006,-6.568913,2.700985,-5.692005,-3.539017,-1.772550,-6.847915,2.416706,-5.757187,-2.526275,9.516856,9.479978,-2.685152,-2.676836,-8.520230,9.124218,8.152418,-9.108379,3.540340,-3.033230,9.936564,1.071804,-4.937840,-1.078240,2.896662,6.257349,1.406173,2.499695,-3.351316,1.667771,-7.484271,-2.005353,-7.074560,-9.877854,6.831592,3.759233,5.608650,-7.838924,-7.493357,-3.429381,2.068602,-5.564836,4.148839,-3.992829,-5.664235,-5.033343,4.846568,-1.506142,5.482805,3.636731,6.934082,1.528585,1.506579,0.235346,6.308677,6.537269,4.561462,4.150476,7.878893,9.001458,5.965941,0.019737,-4.500895,-0.874967,-9.285381,4.078674,-1.875454,9.328598,-8.833142,3.011273,-9.485235,3.272885,6.501441,-4.564831,-4.930994,-3.254913,-0.748558,-2.395948,0.177253,-2.948074,-2.720234,1.390795,6.639556,-0.231949,9.744637,2.013055,0.978164,-4.020476,9.835927,0.644098,-1.752456,7.099785,0.162539,3.387618,-9.264292,8.479572,5.248172,2.877668,8.057128,1.096160,-6.424739,-3.100872,2.779765,-8.937482,-7.560680,-4.431495,5.146704,2.712282,-0.145072,9.345277,-4.477443,3.141061,3.855129,-3.483619,5.783761,-7.009342,-3.195714,0.150156,6.109413,-5.406029,3.930999,-5.676444,-1.877284,-4.236197,-3.132640,4.307162,-2.361188,3.828266,-5.447283,-2.424451,9.278106,2.202421,4.954792,2.237818,-7.028939,-0.495699,-3.985930,-9.236929,-8.217381,1.753495,-7.552794,-9.345007,-5.023051,-5.875152,4.569334,-3.075182,9.767446,1.687326,-6.745287,0.345864,-7.776845,-7.600614,-0.915326,-5.598083,2.458173,-4.788132,-5.420363,-5.947069,-5.694890,3.485444,5.365197,-2.293696,8.579214,-5.265507,-0.231320,-7.926957,4.573921,2.315052,3.819825,3.110165,-9.390855,-8.964251,-5.206029,5.691489,-2.734999,-5.372064,-8.783729,-4.280099,-6.226861,7.015510,0.431057,-1.663930,-1.019987,-6.735052,3.177551,4.880454,1.258261,-4.373715,-9.368397,-1.473711,1.443949,6.733648,2.903959,5.720304,-5.403342,-9.010585,9.642266,-0.829069,5.516709,2.587195,-2.151129,-1.882376,2.793919,7.315110,-9.574110,-8.141687,8.544920,9.043853,4.569089,-6.947908,7.446547,5.209176,1.910142,-5.255657,0.806841,6.286388,-2.473424,2.511511,4.532220,-3.672457,4.672577,0.992354,-5.383148,1.402382,9.648593,2.461454,6.651927,7.486463,-4.851796,1.934837,-1.679663,-1.584872,-9.189098,-7.384691,-1.759684,5.780443,6.901850,-4.853882,9.652530,1.438304,-5.498121,5.622906,-8.992370,-7.367589,-2.739385,-5.517038,3.465940,-0.998783,-7.031506,2.855914,6.324066,-7.168546,4.296556,-5.979399,5.483770,0.845084,-8.008139,8.167802,-7.021437,0.718249,2.877733,9.424496,-0.012938,-5.728279,-7.775458,-9.389328,-2.092604,-2.489592,5.831411,-1.706908,-6.039891,-2.081715,-1.710986,7.374689,-5.048540,6.238888,-4.655959,-8.132653,-4.331796,-2.080771,-2.141305,-2.682296,1.224976,-7.050937,9.476690,4.850689,-2.847151,-2.054265,9.239514,2.052149,5.918883,9.279424,3.231047,-1.567050,-4.308961,-1.666549,5.765543,9.588292,6.482729,-0.014952,-4.327825,9.274624,9.156906,2.731065,8.954680,-5.312808,-8.162710,2.379458,0.794008,4.268991,-8.730219,-6.525247,7.203982,-2.939376,1.445900,3.427467,5.279965,5.121197,6.204708,1.793917,4.921600,5.958472,-5.030124,-9.307474,-9.544235,5.068510,3.876532,2.957422,-1.060100,-3.804793,-5.997357,8.774825,-1.691912,-7.612129,-8.517547,-7.415584,-2.142955,4.470961,-6.454458,-5.023652,0.904347,2.067712,-1.215042,7.945846,6.380258,-8.944074,-3.585198,1.536164,-6.080768,-9.949936,4.035831,3.833503,-7.173870,-1.899920,-8.525075,1.157911,7.351386,-3.736091,6.748317,-5.415931,6.963016,-7.678765,-7.993969,-8.978461,-8.243395,8.967703,-6.585694,0.581585,1.493129,5.224623,-2.176376,-1.563861,-9.001497,8.266739,-3.239841,-8.455954,5.798595,7.739221,-8.351710,-2.743548,-9.492183,-1.322012,-3.046023,1.979745,-7.749467,9.181555,-0.935309,-3.849031,1.979151,-8.024009,2.559833,0.111784,-9.808610,-4.050104,0.211271,1.027172,0.936816,-7.675775,8.196414,7.856402,-5.388372,-1.662821,-1.832493,2.219630,3.452980,-1.142426,-5.249810,8.764193,-5.761110,3.160800,-1.802639,-4.064329,6.848318,-9.537952,-5.710676,-0.487854,-1.432791,8.795121,4.214818,-3.324181,6.245342,1.143404,0.958919,-1.964170,-5.738822,2.584313,-0.868662,-4.358172,-9.337028,-4.452230,4.892903,6.078419,6.011051,-3.120986,-2.575581,6.098871,4.989688,9.544514,8.939403,8.096458,-3.932295,1.118902,-1.178281,-8.288865,-1.741978,7.398846,3.715339,8.414803,-3.859811,3.044586,7.459175,-5.731541,0.396611,9.464958,4.257958,-7.159267,5.548495,-2.546440,-9.286398,-3.757747,4.620629,-1.026296,-4.803147,7.259467,5.125779,3.554927,-0.662697,-9.967666,-0.831057,-5.935750,-0.713178,1.971040,-3.718590,1.646803,-1.433880,0.213065,1.143976,-2.760668,-4.036789,-0.647480,-0.323800,-1.519231,0.077093,-1.386701,-7.474471,7.651087,7.476878,-4.737988,-0.013625,-4.452349,9.328746,-0.541021,9.655016,-8.365925,3.845427,-2.680227,2.728473,-6.900836,5.041498,-0.884678,5.543717,-6.251868,-4.462589,2.470304,-5.519750,8.656118,3.344343,-1.800785,-0.090408,-0.462826,-5.792231,4.493811,2.809945,-0.470873,-8.116128,-7.141108,4.742020,-2.159844,5.563538,-4.831070,-4.476814,7.230043,-6.384403,-3.630334,9.468407,-0.885563,3.414026,7.814559,7.939415,2.207650,-6.934082,8.015852,-0.020632,4.670382,5.385893,4.841013,4.943556,-0.946695,1.128647,-0.858861,4.536698], dtype = "float32")#candidate|7856|(840,)|const|float32
call_7855 = func_5426_call(relay.reshape(const_7856.astype('float32'), [6, 14, 10]))
call_7857 = func_5426_call(relay.reshape(const_7856.astype('float32'), [6, 14, 10]))
func_4726_call = mod.get_global_var('func_4726')
func_4727_call = mutated_mod.get_global_var('func_4727')
call_7865 = relay.TupleGetItem(func_4726_call(), 0)
call_7866 = relay.TupleGetItem(func_4727_call(), 0)
func_342_call = mod.get_global_var('func_342')
func_345_call = mutated_mod.get_global_var('func_345')
const_7886 = relay.const(1, dtype = "int32")#candidate|7886|()|const|int32
var_7887 = relay.var("var_7887", dtype = "int32", shape = (280,))#candidate|7887|(280,)|var|int32
call_7885 = relay.TupleGetItem(func_342_call(relay.reshape(const_7886.astype('int32'), []), relay.reshape(var_7887.astype('int32'), [8, 5, 7]), ), 0)
call_7888 = relay.TupleGetItem(func_345_call(relay.reshape(const_7886.astype('int32'), []), relay.reshape(var_7887.astype('int32'), [8, 5, 7]), ), 0)
output = relay.Tuple([call_7850,call_7855,const_7856,call_7865,call_7885,const_7886,var_7887,])
output2 = relay.Tuple([call_7851,call_7857,const_7856,call_7866,call_7888,const_7886,var_7887,])
func_7894 = relay.Function([var_7887,], output)
mod['func_7894'] = func_7894
mod = relay.transform.InferType()(mod)
mutated_mod['func_7894'] = func_7894
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7895 = relay.var("var_7895", dtype = "int32", shape = (280,))#candidate|7895|(280,)|var|int32
func_7894_call = mutated_mod.get_global_var('func_7894')
call_7896 = func_7894_call(var_7895)
output = call_7896
func_7897 = relay.Function([var_7895], output)
mutated_mod['func_7897'] = func_7897
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7921 = relay.var("var_7921", dtype = "float32", shape = (5, 9, 11))#candidate|7921|(5, 9, 11)|var|float32
var_7922 = relay.var("var_7922", dtype = "float32", shape = (5, 9, 11))#candidate|7922|(5, 9, 11)|var|float32
bop_7923 = relay.maximum(var_7921.astype('float32'), relay.reshape(var_7922.astype('float32'), relay.shape_of(var_7921))) # shape=(5, 9, 11)
uop_7928 = relay.cosh(bop_7923.astype('float32')) # shape=(5, 9, 11)
func_5860_call = mod.get_global_var('func_5860')
func_5863_call = mutated_mod.get_global_var('func_5863')
var_7933 = relay.var("var_7933", dtype = "float32", shape = (1890, 1))#candidate|7933|(1890, 1)|var|float32
call_7932 = relay.TupleGetItem(func_5860_call(relay.reshape(var_7933.astype('float32'), [14, 15, 9])), 1)
call_7934 = relay.TupleGetItem(func_5863_call(relay.reshape(var_7933.astype('float32'), [14, 15, 9])), 1)
bop_7936 = relay.greater(uop_7928.astype('bool'), relay.reshape(bop_7923.astype('bool'), relay.shape_of(uop_7928))) # shape=(5, 9, 11)
output = relay.Tuple([call_7932,var_7933,bop_7936,])
output2 = relay.Tuple([call_7934,var_7933,bop_7936,])
func_7945 = relay.Function([var_7921,var_7922,var_7933,], output)
mod['func_7945'] = func_7945
mod = relay.transform.InferType()(mod)
var_7946 = relay.var("var_7946", dtype = "float32", shape = (5, 9, 11))#candidate|7946|(5, 9, 11)|var|float32
var_7947 = relay.var("var_7947", dtype = "float32", shape = (5, 9, 11))#candidate|7947|(5, 9, 11)|var|float32
var_7948 = relay.var("var_7948", dtype = "float32", shape = (1890, 1))#candidate|7948|(1890, 1)|var|float32
output = func_7945(var_7946,var_7947,var_7948,)
func_7949 = relay.Function([var_7946,var_7947,var_7948,], output)
mutated_mod['func_7949'] = func_7949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5689_call = mod.get_global_var('func_5689')
func_5690_call = mutated_mod.get_global_var('func_5690')
call_8046 = relay.TupleGetItem(func_5689_call(), 0)
call_8047 = relay.TupleGetItem(func_5690_call(), 0)
output = relay.Tuple([call_8046,])
output2 = relay.Tuple([call_8047,])
func_8052 = relay.Function([], output)
mod['func_8052'] = func_8052
mod = relay.transform.InferType()(mod)
output = func_8052()
func_8053 = relay.Function([], output)
mutated_mod['func_8053'] = func_8053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5926_call = mod.get_global_var('func_5926')
func_5927_call = mutated_mod.get_global_var('func_5927')
call_8132 = func_5926_call()
call_8133 = func_5926_call()
output = relay.Tuple([call_8132,])
output2 = relay.Tuple([call_8133,])
func_8138 = relay.Function([], output)
mod['func_8138'] = func_8138
mod = relay.transform.InferType()(mod)
output = func_8138()
func_8139 = relay.Function([], output)
mutated_mod['func_8139'] = func_8139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6359_call = mod.get_global_var('func_6359')
func_6361_call = mutated_mod.get_global_var('func_6361')
call_8158 = relay.TupleGetItem(func_6359_call(), 0)
call_8159 = relay.TupleGetItem(func_6361_call(), 0)
output = relay.Tuple([call_8158,])
output2 = relay.Tuple([call_8159,])
func_8173 = relay.Function([], output)
mod['func_8173'] = func_8173
mod = relay.transform.InferType()(mod)
output = func_8173()
func_8174 = relay.Function([], output)
mutated_mod['func_8174'] = func_8174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6053_call = mod.get_global_var('func_6053')
func_6055_call = mutated_mod.get_global_var('func_6055')
call_8177 = relay.TupleGetItem(func_6053_call(), 0)
call_8178 = relay.TupleGetItem(func_6055_call(), 0)
output = relay.Tuple([call_8177,])
output2 = relay.Tuple([call_8178,])
func_8179 = relay.Function([], output)
mod['func_8179'] = func_8179
mod = relay.transform.InferType()(mod)
output = func_8179()
func_8180 = relay.Function([], output)
mutated_mod['func_8180'] = func_8180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5618_call = mod.get_global_var('func_5618')
func_5620_call = mutated_mod.get_global_var('func_5620')
call_8234 = func_5618_call()
call_8235 = func_5618_call()
func_6649_call = mod.get_global_var('func_6649')
func_6651_call = mutated_mod.get_global_var('func_6651')
call_8239 = relay.TupleGetItem(func_6649_call(), 0)
call_8240 = relay.TupleGetItem(func_6651_call(), 0)
func_6754_call = mod.get_global_var('func_6754')
func_6755_call = mutated_mod.get_global_var('func_6755')
call_8259 = relay.TupleGetItem(func_6754_call(), 1)
call_8260 = relay.TupleGetItem(func_6755_call(), 1)
func_2044_call = mod.get_global_var('func_2044')
func_2046_call = mutated_mod.get_global_var('func_2046')
var_8266 = relay.var("var_8266", dtype = "float32", shape = (168,))#candidate|8266|(168,)|var|float32
call_8265 = relay.TupleGetItem(func_2044_call(relay.reshape(var_8266.astype('float32'), [1, 12, 14])), 0)
call_8267 = relay.TupleGetItem(func_2046_call(relay.reshape(var_8266.astype('float32'), [1, 12, 14])), 0)
output = relay.Tuple([call_8234,call_8239,call_8259,call_8265,var_8266,])
output2 = relay.Tuple([call_8235,call_8240,call_8260,call_8267,var_8266,])
func_8276 = relay.Function([var_8266,], output)
mod['func_8276'] = func_8276
mod = relay.transform.InferType()(mod)
var_8277 = relay.var("var_8277", dtype = "float32", shape = (168,))#candidate|8277|(168,)|var|float32
output = func_8276(var_8277)
func_8278 = relay.Function([var_8277], output)
mutated_mod['func_8278'] = func_8278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5641_call = mod.get_global_var('func_5641')
func_5643_call = mutated_mod.get_global_var('func_5643')
call_8291 = func_5641_call()
call_8292 = func_5641_call()
output = relay.Tuple([call_8291,])
output2 = relay.Tuple([call_8292,])
func_8295 = relay.Function([], output)
mod['func_8295'] = func_8295
mod = relay.transform.InferType()(mod)
output = func_8295()
func_8296 = relay.Function([], output)
mutated_mod['func_8296'] = func_8296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6777_call = mod.get_global_var('func_6777')
func_6778_call = mutated_mod.get_global_var('func_6778')
call_8315 = func_6777_call()
call_8316 = func_6777_call()
output = call_8315
output2 = call_8316
func_8319 = relay.Function([], output)
mod['func_8319'] = func_8319
mod = relay.transform.InferType()(mod)
output = func_8319()
func_8320 = relay.Function([], output)
mutated_mod['func_8320'] = func_8320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5618_call = mod.get_global_var('func_5618')
func_5620_call = mutated_mod.get_global_var('func_5620')
call_8357 = func_5618_call()
call_8358 = func_5618_call()
func_7013_call = mod.get_global_var('func_7013')
func_7014_call = mutated_mod.get_global_var('func_7014')
call_8366 = relay.TupleGetItem(func_7013_call(), 0)
call_8367 = relay.TupleGetItem(func_7014_call(), 0)
output = relay.Tuple([call_8357,call_8366,])
output2 = relay.Tuple([call_8358,call_8367,])
func_8372 = relay.Function([], output)
mod['func_8372'] = func_8372
mod = relay.transform.InferType()(mod)
output = func_8372()
func_8373 = relay.Function([], output)
mutated_mod['func_8373'] = func_8373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7322_call = mod.get_global_var('func_7322')
func_7324_call = mutated_mod.get_global_var('func_7324')
call_8376 = relay.TupleGetItem(func_7322_call(), 0)
call_8377 = relay.TupleGetItem(func_7324_call(), 0)
const_8379 = relay.const([[0.973670,-7.676511],[1.040441,-0.920532],[3.959996,-5.778130],[8.633317,-2.292203],[-1.773572,-2.348131],[-2.393490,-3.673844],[-9.811146,4.346279],[3.506465,2.292833],[-9.889858,0.120357],[9.909002,-7.330490],[1.970260,1.184705],[-3.919833,-9.039801],[6.076745,-1.409243],[6.759803,-4.347801],[8.385164,-7.322350],[-4.480880,-8.462669],[1.954480,-9.567022],[1.129915,9.485382],[9.175754,6.140489],[-0.586790,-2.296440],[-3.569191,8.582184],[8.852128,3.349686],[0.572321,-5.681794],[7.924211,-6.180415],[-5.893257,9.981623],[3.142688,-2.443897],[-6.055121,3.465769],[-0.084799,-9.750465],[-7.841236,-1.841897],[3.975399,-3.318408],[2.734876,-3.007544],[9.813184,2.005352],[2.640763,-7.858798],[-1.055665,-0.995394],[-0.711735,9.346017],[3.071267,-1.761386],[-7.867340,-7.309847],[-9.314217,-8.942619],[0.205193,7.089195],[-3.846519,-1.251695],[8.781141,-7.217774],[6.225809,-1.304126],[-8.164321,-7.438557],[-4.221647,1.377250],[7.634997,-1.368773],[4.589542,3.811468],[-7.857380,0.786517],[-2.946270,-2.520807]], dtype = "float64")#candidate|8379|(48, 2)|const|float64
bop_8380 = relay.mod(call_8376.astype('float64'), relay.reshape(const_8379.astype('float64'), relay.shape_of(call_8376))) # shape=(48, 2)
bop_8383 = relay.mod(call_8377.astype('float64'), relay.reshape(const_8379.astype('float64'), relay.shape_of(call_8377))) # shape=(48, 2)
func_3880_call = mod.get_global_var('func_3880')
func_3881_call = mutated_mod.get_global_var('func_3881')
call_8392 = relay.TupleGetItem(func_3880_call(), 0)
call_8393 = relay.TupleGetItem(func_3881_call(), 0)
output = relay.Tuple([bop_8380,call_8392,])
output2 = relay.Tuple([bop_8383,call_8393,])
func_8407 = relay.Function([], output)
mod['func_8407'] = func_8407
mod = relay.transform.InferType()(mod)
mutated_mod['func_8407'] = func_8407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8407_call = mutated_mod.get_global_var('func_8407')
call_8408 = func_8407_call()
output = call_8408
func_8409 = relay.Function([], output)
mutated_mod['func_8409'] = func_8409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7823_call = mod.get_global_var('func_7823')
func_7824_call = mutated_mod.get_global_var('func_7824')
call_8457 = func_7823_call()
call_8458 = func_7823_call()
output = relay.Tuple([call_8457,])
output2 = relay.Tuple([call_8458,])
func_8465 = relay.Function([], output)
mod['func_8465'] = func_8465
mod = relay.transform.InferType()(mod)
mutated_mod['func_8465'] = func_8465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8465_call = mutated_mod.get_global_var('func_8465')
call_8466 = func_8465_call()
output = call_8466
func_8467 = relay.Function([], output)
mutated_mod['func_8467'] = func_8467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6296_call = mod.get_global_var('func_6296')
func_6297_call = mutated_mod.get_global_var('func_6297')
call_8506 = relay.TupleGetItem(func_6296_call(), 1)
call_8507 = relay.TupleGetItem(func_6297_call(), 1)
func_8372_call = mod.get_global_var('func_8372')
func_8373_call = mutated_mod.get_global_var('func_8373')
call_8511 = relay.TupleGetItem(func_8372_call(), 0)
call_8512 = relay.TupleGetItem(func_8373_call(), 0)
func_8465_call = mod.get_global_var('func_8465')
func_8467_call = mutated_mod.get_global_var('func_8467')
call_8519 = relay.TupleGetItem(func_8465_call(), 0)
call_8520 = relay.TupleGetItem(func_8467_call(), 0)
func_5426_call = mod.get_global_var('func_5426')
func_5428_call = mutated_mod.get_global_var('func_5428')
var_8531 = relay.var("var_8531", dtype = "float32", shape = (840,))#candidate|8531|(840,)|var|float32
call_8530 = func_5426_call(relay.reshape(var_8531.astype('float32'), [6, 14, 10]))
call_8532 = func_5426_call(relay.reshape(var_8531.astype('float32'), [6, 14, 10]))
func_4726_call = mod.get_global_var('func_4726')
func_4727_call = mutated_mod.get_global_var('func_4727')
call_8533 = relay.TupleGetItem(func_4726_call(), 0)
call_8534 = relay.TupleGetItem(func_4727_call(), 0)
output = relay.Tuple([call_8506,call_8511,call_8519,call_8530,var_8531,call_8533,])
output2 = relay.Tuple([call_8507,call_8512,call_8520,call_8532,var_8531,call_8534,])
func_8537 = relay.Function([var_8531,], output)
mod['func_8537'] = func_8537
mod = relay.transform.InferType()(mod)
mutated_mod['func_8537'] = func_8537
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8538 = relay.var("var_8538", dtype = "float32", shape = (840,))#candidate|8538|(840,)|var|float32
func_8537_call = mutated_mod.get_global_var('func_8537')
call_8539 = func_8537_call(var_8538)
output = call_8539
func_8540 = relay.Function([var_8538], output)
mutated_mod['func_8540'] = func_8540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8465_call = mod.get_global_var('func_8465')
func_8467_call = mutated_mod.get_global_var('func_8467')
call_8592 = relay.TupleGetItem(func_8465_call(), 0)
call_8593 = relay.TupleGetItem(func_8467_call(), 0)
output = relay.Tuple([call_8592,])
output2 = relay.Tuple([call_8593,])
func_8611 = relay.Function([], output)
mod['func_8611'] = func_8611
mod = relay.transform.InferType()(mod)
mutated_mod['func_8611'] = func_8611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8611_call = mutated_mod.get_global_var('func_8611')
call_8612 = func_8611_call()
output = call_8612
func_8613 = relay.Function([], output)
mutated_mod['func_8613'] = func_8613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6664_call = mod.get_global_var('func_6664')
func_6665_call = mutated_mod.get_global_var('func_6665')
call_8614 = func_6664_call()
call_8615 = func_6664_call()
output = call_8614
output2 = call_8615
func_8619 = relay.Function([], output)
mod['func_8619'] = func_8619
mod = relay.transform.InferType()(mod)
output = func_8619()
func_8620 = relay.Function([], output)
mutated_mod['func_8620'] = func_8620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7013_call = mod.get_global_var('func_7013')
func_7014_call = mutated_mod.get_global_var('func_7014')
call_8621 = relay.TupleGetItem(func_7013_call(), 0)
call_8622 = relay.TupleGetItem(func_7014_call(), 0)
func_6664_call = mod.get_global_var('func_6664')
func_6665_call = mutated_mod.get_global_var('func_6665')
call_8623 = func_6664_call()
call_8624 = func_6664_call()
output = relay.Tuple([call_8621,call_8623,])
output2 = relay.Tuple([call_8622,call_8624,])
func_8633 = relay.Function([], output)
mod['func_8633'] = func_8633
mod = relay.transform.InferType()(mod)
output = func_8633()
func_8634 = relay.Function([], output)
mutated_mod['func_8634'] = func_8634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8372_call = mod.get_global_var('func_8372')
func_8373_call = mutated_mod.get_global_var('func_8373')
call_8649 = relay.TupleGetItem(func_8372_call(), 0)
call_8650 = relay.TupleGetItem(func_8373_call(), 0)
func_5860_call = mod.get_global_var('func_5860')
func_5863_call = mutated_mod.get_global_var('func_5863')
call_8652 = relay.TupleGetItem(func_5860_call(relay.reshape(call_8649.astype('float32'), [14, 15, 9])), 2)
call_8653 = relay.TupleGetItem(func_5863_call(relay.reshape(call_8649.astype('float32'), [14, 15, 9])), 2)
output = relay.Tuple([call_8649,call_8652,])
output2 = relay.Tuple([call_8650,call_8653,])
func_8696 = relay.Function([], output)
mod['func_8696'] = func_8696
mod = relay.transform.InferType()(mod)
output = func_8696()
func_8697 = relay.Function([], output)
mutated_mod['func_8697'] = func_8697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4167_call = mod.get_global_var('func_4167')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_8704 = relay.TupleGetItem(func_4167_call(), 0)
call_8705 = relay.TupleGetItem(func_4169_call(), 0)
func_5048_call = mod.get_global_var('func_5048')
func_5051_call = mutated_mod.get_global_var('func_5051')
call_8709 = func_5048_call(relay.reshape(call_8704.astype('float64'), [14, 15, 9]))
call_8710 = func_5048_call(relay.reshape(call_8704.astype('float64'), [14, 15, 9]))
output = relay.Tuple([call_8704,call_8709,])
output2 = relay.Tuple([call_8705,call_8710,])
func_8714 = relay.Function([], output)
mod['func_8714'] = func_8714
mod = relay.transform.InferType()(mod)
mutated_mod['func_8714'] = func_8714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8714_call = mutated_mod.get_global_var('func_8714')
call_8715 = func_8714_call()
output = call_8715
func_8716 = relay.Function([], output)
mutated_mod['func_8716'] = func_8716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6435_call = mod.get_global_var('func_6435')
func_6436_call = mutated_mod.get_global_var('func_6436')
call_8738 = func_6435_call()
call_8739 = func_6435_call()
output = call_8738
output2 = call_8739
func_8740 = relay.Function([], output)
mod['func_8740'] = func_8740
mod = relay.transform.InferType()(mod)
mutated_mod['func_8740'] = func_8740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8740_call = mutated_mod.get_global_var('func_8740')
call_8741 = func_8740_call()
output = call_8741
func_8742 = relay.Function([], output)
mutated_mod['func_8742'] = func_8742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4620_call = mod.get_global_var('func_4620')
func_4621_call = mutated_mod.get_global_var('func_4621')
call_8754 = func_4620_call()
call_8755 = func_4620_call()
uop_8758 = relay.exp(call_8754.astype('float64')) # shape=(14, 15, 9)
uop_8760 = relay.exp(call_8755.astype('float64')) # shape=(14, 15, 9)
func_5426_call = mod.get_global_var('func_5426')
func_5428_call = mutated_mod.get_global_var('func_5428')
var_8762 = relay.var("var_8762", dtype = "float32", shape = (12, 70))#candidate|8762|(12, 70)|var|float32
call_8761 = func_5426_call(relay.reshape(var_8762.astype('float32'), [6, 14, 10]))
call_8763 = func_5426_call(relay.reshape(var_8762.astype('float32'), [6, 14, 10]))
func_5048_call = mod.get_global_var('func_5048')
func_5051_call = mutated_mod.get_global_var('func_5051')
call_8767 = func_5048_call(relay.reshape(call_8754.astype('float64'), [14, 15, 9]))
call_8768 = func_5048_call(relay.reshape(call_8754.astype('float64'), [14, 15, 9]))
bop_8775 = relay.greater(uop_8758.astype('bool'), relay.reshape(call_8767.astype('bool'), relay.shape_of(uop_8758))) # shape=(14, 15, 9)
bop_8778 = relay.greater(uop_8760.astype('bool'), relay.reshape(call_8768.astype('bool'), relay.shape_of(uop_8760))) # shape=(14, 15, 9)
output = relay.Tuple([call_8761,var_8762,bop_8775,])
output2 = relay.Tuple([call_8763,var_8762,bop_8778,])
func_8784 = relay.Function([var_8762,], output)
mod['func_8784'] = func_8784
mod = relay.transform.InferType()(mod)
var_8785 = relay.var("var_8785", dtype = "float32", shape = (12, 70))#candidate|8785|(12, 70)|var|float32
output = func_8784(var_8785)
func_8786 = relay.Function([var_8785], output)
mutated_mod['func_8786'] = func_8786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5926_call = mod.get_global_var('func_5926')
func_5927_call = mutated_mod.get_global_var('func_5927')
call_8809 = func_5926_call()
call_8810 = func_5926_call()
func_5689_call = mod.get_global_var('func_5689')
func_5690_call = mutated_mod.get_global_var('func_5690')
call_8817 = relay.TupleGetItem(func_5689_call(), 0)
call_8818 = relay.TupleGetItem(func_5690_call(), 0)
func_8138_call = mod.get_global_var('func_8138')
func_8139_call = mutated_mod.get_global_var('func_8139')
call_8821 = relay.TupleGetItem(func_8138_call(), 0)
call_8822 = relay.TupleGetItem(func_8139_call(), 0)
output = relay.Tuple([call_8809,call_8817,call_8821,])
output2 = relay.Tuple([call_8810,call_8818,call_8822,])
func_8823 = relay.Function([], output)
mod['func_8823'] = func_8823
mod = relay.transform.InferType()(mod)
output = func_8823()
func_8824 = relay.Function([], output)
mutated_mod['func_8824'] = func_8824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7391_call = mod.get_global_var('func_7391')
func_7393_call = mutated_mod.get_global_var('func_7393')
call_8846 = relay.TupleGetItem(func_7391_call(), 0)
call_8847 = relay.TupleGetItem(func_7393_call(), 0)
output = call_8846
output2 = call_8847
func_8857 = relay.Function([], output)
mod['func_8857'] = func_8857
mod = relay.transform.InferType()(mod)
output = func_8857()
func_8858 = relay.Function([], output)
mutated_mod['func_8858'] = func_8858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8714_call = mod.get_global_var('func_8714')
func_8716_call = mutated_mod.get_global_var('func_8716')
call_8883 = relay.TupleGetItem(func_8714_call(), 0)
call_8884 = relay.TupleGetItem(func_8716_call(), 0)
output = call_8883
output2 = call_8884
func_8891 = relay.Function([], output)
mod['func_8891'] = func_8891
mod = relay.transform.InferType()(mod)
output = func_8891()
func_8892 = relay.Function([], output)
mutated_mod['func_8892'] = func_8892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7042_call = mod.get_global_var('func_7042')
func_7044_call = mutated_mod.get_global_var('func_7044')
call_8925 = relay.TupleGetItem(func_7042_call(), 0)
call_8926 = relay.TupleGetItem(func_7044_call(), 0)
func_4689_call = mod.get_global_var('func_4689')
func_4690_call = mutated_mod.get_global_var('func_4690')
call_8937 = relay.TupleGetItem(func_4689_call(), 0)
call_8938 = relay.TupleGetItem(func_4690_call(), 0)
output = relay.Tuple([call_8925,call_8937,])
output2 = relay.Tuple([call_8926,call_8938,])
func_8952 = relay.Function([], output)
mod['func_8952'] = func_8952
mod = relay.transform.InferType()(mod)
mutated_mod['func_8952'] = func_8952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8952_call = mutated_mod.get_global_var('func_8952')
call_8953 = func_8952_call()
output = call_8953
func_8954 = relay.Function([], output)
mutated_mod['func_8954'] = func_8954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8179_call = mod.get_global_var('func_8179')
func_8180_call = mutated_mod.get_global_var('func_8180')
call_8966 = relay.TupleGetItem(func_8179_call(), 0)
call_8967 = relay.TupleGetItem(func_8180_call(), 0)
func_7272_call = mod.get_global_var('func_7272')
func_7273_call = mutated_mod.get_global_var('func_7273')
call_8970 = relay.TupleGetItem(func_7272_call(), 0)
call_8971 = relay.TupleGetItem(func_7273_call(), 0)
uop_8977 = relay.log(call_8970.astype('float32')) # shape=(14, 15, 9)
uop_8979 = relay.log(call_8971.astype('float32')) # shape=(14, 15, 9)
func_5319_call = mod.get_global_var('func_5319')
func_5321_call = mutated_mod.get_global_var('func_5321')
call_8980 = relay.TupleGetItem(func_5319_call(), 0)
call_8981 = relay.TupleGetItem(func_5321_call(), 0)
func_8173_call = mod.get_global_var('func_8173')
func_8174_call = mutated_mod.get_global_var('func_8174')
call_9001 = relay.TupleGetItem(func_8173_call(), 0)
call_9002 = relay.TupleGetItem(func_8174_call(), 0)
func_8857_call = mod.get_global_var('func_8857')
func_8858_call = mutated_mod.get_global_var('func_8858')
call_9016 = func_8857_call()
call_9017 = func_8857_call()
func_5426_call = mod.get_global_var('func_5426')
func_5428_call = mutated_mod.get_global_var('func_5428')
var_9025 = relay.var("var_9025", dtype = "float32", shape = (840,))#candidate|9025|(840,)|var|float32
call_9024 = func_5426_call(relay.reshape(var_9025.astype('float32'), [6, 14, 10]))
call_9026 = func_5426_call(relay.reshape(var_9025.astype('float32'), [6, 14, 10]))
output = relay.Tuple([call_8966,uop_8977,call_8980,call_9001,call_9016,call_9024,var_9025,])
output2 = relay.Tuple([call_8967,uop_8979,call_8981,call_9002,call_9017,call_9026,var_9025,])
func_9027 = relay.Function([var_9025,], output)
mod['func_9027'] = func_9027
mod = relay.transform.InferType()(mod)
var_9028 = relay.var("var_9028", dtype = "float32", shape = (840,))#candidate|9028|(840,)|var|float32
output = func_9027(var_9028)
func_9029 = relay.Function([var_9028], output)
mutated_mod['func_9029'] = func_9029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mod.get_global_var('func_4689')
func_4690_call = mutated_mod.get_global_var('func_4690')
call_9099 = relay.TupleGetItem(func_4689_call(), 1)
call_9100 = relay.TupleGetItem(func_4690_call(), 1)
output = relay.Tuple([call_9099,])
output2 = relay.Tuple([call_9100,])
func_9101 = relay.Function([], output)
mod['func_9101'] = func_9101
mod = relay.transform.InferType()(mod)
mutated_mod['func_9101'] = func_9101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9101_call = mutated_mod.get_global_var('func_9101')
call_9102 = func_9101_call()
output = call_9102
func_9103 = relay.Function([], output)
mutated_mod['func_9103'] = func_9103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8407_call = mod.get_global_var('func_8407')
func_8409_call = mutated_mod.get_global_var('func_8409')
call_9115 = relay.TupleGetItem(func_8407_call(), 1)
call_9116 = relay.TupleGetItem(func_8409_call(), 1)
output = relay.Tuple([call_9115,])
output2 = relay.Tuple([call_9116,])
func_9123 = relay.Function([], output)
mod['func_9123'] = func_9123
mod = relay.transform.InferType()(mod)
output = func_9123()
func_9124 = relay.Function([], output)
mutated_mod['func_9124'] = func_9124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4949_call = mod.get_global_var('func_4949')
func_4951_call = mutated_mod.get_global_var('func_4951')
call_9189 = func_4949_call()
call_9190 = func_4949_call()
func_5426_call = mod.get_global_var('func_5426')
func_5428_call = mutated_mod.get_global_var('func_5428')
const_9246 = relay.const([-3.718924,5.303328,-0.875706,6.506395,-1.275903,-4.488660,-6.182368,-4.051072,5.303424,-6.089303,8.991223,-6.794526,-1.929335,-8.970555,3.969176,-3.126642,-7.984962,7.911915,7.108854,-1.030613,7.186032,5.909245,4.817121,2.198610,-9.875896,4.981785,2.766337,-3.963292,4.141131,1.143612,-4.848803,-9.533748,-8.963336,3.593047,-1.053201,4.998866,-7.693436,-2.571731,-6.282116,7.660920,6.523045,-0.121465,-6.584204,-5.922706,3.825382,1.144054,-0.315175,9.207111,6.607097,-0.091330,-9.650492,3.803951,7.651525,-4.749523,1.104873,-5.206704,-3.191054,8.838924,7.460058,-2.168867,-1.071368,-5.442761,0.685542,7.188683,-3.806273,5.786115,9.290441,-9.359310,-1.161745,-4.356223,-4.868894,-7.558848,-0.811881,5.010483,-8.767899,-8.269527,2.215783,6.679200,-4.608230,-3.765856,-7.175339,7.198794,-0.503154,-5.700404,-8.959314,8.900019,8.762231,6.938740,7.696023,4.954010,-7.356117,-6.186174,-1.128615,3.109428,-3.597481,-2.633324,8.083848,-8.753811,0.948668,-3.629522,-5.388010,-1.989861,2.590666,6.057643,-9.983922,-2.677217,-5.372665,8.612852,-6.999139,-6.123171,-5.298761,-9.796931,-1.802565,8.970005,8.177198,-2.040400,0.952529,-7.425504,-5.176742,-8.046888,-6.928961,-7.010946,7.607214,-0.153773,-5.062433,6.353941,4.116869,-0.808100,-2.350740,8.733985,2.477261,7.970976,-2.659692,5.088726,7.496240,6.519956,0.444186,3.487164,7.347454,-8.708905,-5.791934,-2.591275,6.249043,1.955933,8.111353,-2.360984,-2.684286,1.257954,3.363719,-0.077606,-0.784449,-5.537286,1.055580,6.889177,2.305420,-0.771767,6.499742,8.706958,0.301176,-2.236376,0.547249,5.579500,5.077454,-0.282766,3.360576,5.019016,6.357454,2.308639,8.112835,8.406064,5.034980,-2.333287,2.367404,2.835125,3.791829,3.028966,-7.879989,-7.831666,5.518570,-1.130797,7.297122,4.374196,-4.712662,3.057772,0.593588,-6.991110,-7.027803,4.918559,8.655678,-9.198174,-6.393234,4.919878,-5.050772,-1.522801,0.730516,6.816895,0.931456,3.566760,1.377377,0.911643,3.654161,4.557500,1.600108,3.167893,-3.598174,2.004431,6.060798,2.718944,-4.918053,-3.115766,0.934643,0.605596,-4.761319,-2.354827,3.697835,-4.495414,1.788510,6.245480,-4.767966,9.669158,-8.150419,5.837777,-7.647407,-6.235691,1.567918,-5.518521,-7.855027,2.181078,-0.756906,-1.448975,5.138220,-2.727390,4.214114,5.989401,8.421213,-9.877152,2.809950,0.875788,-1.228821,4.184002,-9.089132,-5.771448,3.050108,2.490501,1.327572,1.920934,-2.963498,-9.217328,9.639972,7.166635,-4.400679,9.344290,-6.672004,5.393098,-0.833756,-5.175206,-6.342596,4.564257,-9.560036,7.437164,-5.780462,-3.410528,1.583231,-7.863448,1.285133,0.017434,5.213490,6.749779,0.186294,4.337447,6.250366,5.808733,-4.393544,8.095111,3.846434,1.603726,-7.695604,5.083118,-8.050818,-1.440610,7.219492,6.517034,-2.353946,-3.427967,-8.055218,8.296009,9.897670,7.479627,7.268189,-1.340159,-8.143365,4.283403,-2.923584,-4.513751,-2.612004,-0.720361,-1.194478,2.468384,-0.020011,-3.741782,8.909182,9.460656,-4.009165,-4.360495,9.210754,1.057498,-2.357033,-9.244934,1.392080,5.113709,-3.356170,3.459234,-9.654414,2.760359,0.751195,0.636683,-9.502945,6.911469,0.289643,-7.133397,3.593220,-6.478190,-2.594104,-5.580010,1.892531,-5.201158,9.322229,-7.273126,-1.577883,-5.262789,-0.480733,-1.884424,-6.162208,6.289808,6.165554,6.373464,8.334581,6.931233,-3.543979,0.491252,3.682267,4.184174,-4.456806,-7.789306,-8.243475,-8.817487,-7.950408,1.293112,-8.208156,4.351629,-1.771285,-2.688969,-9.608008,-3.814453,4.764443,8.527812,9.481295,3.910826,-9.731235,-0.228821,6.908632,2.592855,7.583551,-1.571197,-4.665736,9.170487,-8.302621,-5.255456,9.117288,-0.768027,0.531387,-9.774582,-9.430487,-2.415221,0.812867,5.594817,0.329882,4.171590,2.020454,-3.383746,2.485786,2.204796,-3.605831,-8.095657,-0.244982,-8.674599,-0.620738,-3.601139,4.196153,-8.989034,6.200634,4.072583,-6.642854,0.001395,-2.833698,2.746873,3.100013,-5.869292,3.482349,-0.497408,9.335106,6.429832,9.021686,-9.191478,-3.277743,8.998279,7.886913,-3.174310,4.986185,2.104349,1.044151,3.935573,4.260379,-7.789391,6.483058,-2.270242,-6.799020,-2.768293,4.753574,-9.666241,5.422930,1.165048,-6.357440,0.863038,9.969232,9.025479,6.554827,-6.423793,-0.645469,3.431835,1.132618,-6.061898,7.809868,1.645775,-9.021686,-0.618452,1.663448,-1.272078,7.253130,-7.459354,-0.882084,-3.224617,-5.376179,6.397601,4.652600,-9.314328,-6.871191,-4.056736,-3.663049,0.580097,6.426173,-6.434481,8.516501,-9.703387,-7.997453,-0.130274,3.306968,8.821943,2.755684,-3.450361,5.402648,2.554355,-4.352550,-0.319426,6.896922,3.228763,6.284314,7.286321,-8.666620,-6.094967,-6.201752,7.899967,1.680153,-6.585540,8.862253,6.328053,3.625247,8.116831,9.098447,-9.443022,8.185498,7.009846,-6.115839,1.019364,0.672463,2.700926,-2.175615,0.405342,8.683891,-4.215148,-3.172031,-0.245472,-8.389857,9.024147,1.618265,-9.790513,4.164852,2.816836,6.911716,-9.771239,-3.996621,-0.610397,9.374611,-9.960214,0.215121,5.312890,6.124354,-9.504677,7.705866,8.450495,7.873426,0.328092,2.545504,-7.947047,-3.120222,8.205104,4.740364,2.390311,1.751487,6.630777,1.240653,8.291221,-8.453526,-4.126800,9.828276,-7.267914,-1.641323,-0.271022,6.699105,-9.364705,6.641488,-7.593732,9.665325,8.862824,-0.045247,-2.492211,-4.692599,-8.215142,7.720912,-5.252502,-9.643443,7.452443,5.072079,-0.440722,9.051802,-8.466432,9.599007,9.400583,-5.200881,4.167813,9.727895,-3.110291,8.286755,1.499544,-6.733990,-9.059305,-7.030704,0.935198,7.759989,-0.144067,-3.324099,7.904837,-0.134127,-9.774051,-6.900218,0.097526,4.904555,5.105825,-5.368049,8.623818,-1.229557,8.562773,-7.521492,-7.496531,-8.459904,-2.661663,5.536995,-8.283728,-4.241332,1.169129,4.706969,-3.432660,-4.033966,5.007598,-1.313249,4.480576,-2.829154,-8.083774,1.175369,-1.662181,6.689645,-9.758369,3.439124,-3.163539,-3.263806,-7.428091,-4.756685,-0.461776,-8.982801,9.977488,6.644350,6.226809,1.522841,-7.240279,1.386054,8.249832,3.417459,5.812762,-4.346165,-2.518421,1.079120,-4.548258,8.916278,8.627657,8.396484,7.055850,2.638293,-7.460830,-5.352857,-0.868396,-1.007062,-7.092496,7.869493,-4.860916,-0.649066,-4.751450,1.552338,6.416970,-2.038383,-1.659732,-6.849417,-3.402306,-4.075438,-8.839536,5.501781,-6.346881,-7.627070,8.027589,8.047882,-8.884984,-7.982470,7.717579,9.763128,-9.659562,8.944000,4.675223,-2.119493,-4.677985,2.545559,5.809368,8.477035,-6.222015,3.020980,2.516600,7.990618,-3.276624,6.495718,0.926609,-2.667600,-1.211973,-6.877939,3.075023,2.701622,7.200416,9.574025,8.700111,9.299275,-0.538549,3.447099,9.192346,8.110350,-2.658880,2.465737,-6.869758,8.507222,-6.115614,-2.512189,9.001927,3.593388,-4.380570,7.833562,0.363508,8.519462,0.215807,3.687478,0.830155,-3.325026,9.764843,5.479893,-9.785687,-2.193479,-7.856544,-6.752010,-0.139894,6.005500,-5.343973,-4.391557,6.438316,-4.550994,-2.253153,5.779550,-8.799837,3.472992,6.782249,6.345163,-7.582513,-0.167615,6.559885,-8.334595,-8.151044,-7.718102,-2.436051,-6.821437,0.590972,9.779689,0.359595,1.048054,-1.082092,2.474167,-2.415053,9.462634,6.692649,0.217405,2.604065,-6.000086,0.955247,-0.486585,-2.022002,5.710886,9.213612,3.411655,5.134113,6.176107,-1.746939,-2.705681,3.554502,8.412489,1.840550,8.872140,-3.362468,8.102473,7.727772,7.335615,-0.731792,7.307729,3.956481,-8.551355,9.209964,1.335667,6.553342,-5.974764,1.897766,9.626252,9.006352,2.814674,-2.160439,0.906289,4.803642,0.955511,-9.016345,6.558411,-1.683790,-4.351178,9.098823,5.652314,0.818682,-4.996033,2.389615,-4.812625,-9.792142,-2.490584,-8.862817,-7.988797,-5.317529,5.294610,-1.394721,1.072437,8.428454,8.239774,6.413021,5.777395,-7.449756,0.919384,6.746242,-0.627265,-3.926978,-3.216901,0.306060,-8.375789,4.407253,-0.084166,-8.581302,-9.885766,3.704110,1.752964,-7.984192,-7.583846,-7.466565,-0.901289,1.413017,7.605055,4.620904,-7.701054,0.927764,-2.922395,-4.095269,-3.034366,-3.792698,-4.911907,-3.598007,-0.513303,-5.206997,-2.113910,9.871682,-8.381289,2.418647,-4.601222,-9.468951,7.278289,5.697417,-9.253320,-6.626041,-1.066652,4.767381,8.290772,-4.625773,-1.929398,-9.439627,3.465790,8.399622,-2.328208,-2.978756,6.970060,4.622824,-4.855216,-1.068750,-7.790888,1.126302,-6.155797,-1.472306], dtype = "float32")#candidate|9246|(840,)|const|float32
call_9245 = func_5426_call(relay.reshape(const_9246.astype('float32'), [6, 14, 10]))
call_9247 = func_5426_call(relay.reshape(const_9246.astype('float32'), [6, 14, 10]))
func_1202_call = mod.get_global_var('func_1202')
func_1204_call = mutated_mod.get_global_var('func_1204')
const_9255 = relay.const([[False,False],[False,False],[False,False],[True,False],[True,True],[True,False],[True,True],[True,False],[True,False],[True,True],[False,False],[False,True],[True,True],[False,False],[True,False],[False,False],[False,True],[False,False],[True,False],[False,False],[True,False],[True,True],[True,False],[True,False],[False,True],[True,False],[True,False],[True,False],[True,True],[True,True],[True,True],[True,False],[False,True],[False,True],[True,True],[False,True],[True,True],[False,False],[True,True],[False,True],[False,False],[True,False],[False,False],[False,True],[True,True],[False,True],[True,True],[True,True],[True,True],[True,False],[False,True],[True,True],[False,True],[True,True],[True,False],[False,True],[False,True],[True,False],[True,False],[True,False],[True,False],[True,False],[True,False],[False,False],[False,True],[True,False],[False,False],[False,False],[False,True],[True,True],[True,True],[False,True],[False,False],[True,True],[False,True],[True,True],[True,True],[False,False],[True,False],[True,True],[True,False],[False,True],[False,False],[True,False],[True,False],[True,True],[True,False],[False,True],[False,False],[False,False],[True,True],[True,False],[False,True],[False,False],[True,True],[True,False],[True,True],[True,False],[True,False],[False,True],[False,False],[False,True],[False,False],[False,False],[False,False],[False,True],[False,True],[True,False],[True,False],[False,False],[True,False],[True,True],[True,False],[True,True],[True,True],[False,True],[True,False],[True,True],[False,True],[True,True],[False,True],[False,False],[True,False],[False,False],[False,True],[False,True],[True,True],[False,False],[False,True],[True,True],[True,True],[False,False],[True,True],[False,False],[True,True],[True,True],[True,True],[True,False],[True,True],[False,True],[False,False],[True,True],[False,True],[False,False],[True,True],[True,False],[True,True],[False,False],[True,False],[False,False],[False,True],[True,True],[True,False],[True,False],[True,True],[False,False],[True,True],[True,True],[False,True],[True,True],[True,False],[True,False],[False,False],[False,True],[False,True],[True,False],[False,False],[True,True],[False,False],[False,True],[True,False],[True,True],[True,True],[False,True],[False,False],[True,True],[False,False],[True,False],[False,False],[True,True],[True,False],[True,True],[False,True],[True,False],[True,True],[False,True],[True,True],[False,False],[False,False],[True,True],[False,False],[False,True],[True,False],[True,True],[False,True],[False,True],[True,False],[False,False],[True,True],[False,False],[False,False],[True,True],[False,True],[True,False],[False,True],[True,False],[True,False],[True,False],[False,True],[False,False],[False,False],[True,True],[False,True],[True,True],[True,False],[False,True],[False,True],[True,False],[True,False],[True,True],[True,False],[True,True],[False,True],[True,False],[False,True],[False,False],[False,True],[True,False],[True,True],[False,False],[True,False],[True,True],[True,False],[False,False],[True,True],[True,False],[True,True],[True,False],[False,True],[False,False],[False,True],[False,False],[False,True],[True,True],[False,True],[True,True],[True,True],[True,False],[True,True],[True,False],[False,False],[True,True],[True,False],[True,True],[True,False],[True,False],[True,True],[False,True],[True,True],[True,True],[False,False],[True,True],[True,False],[False,True],[True,True],[True,True],[True,False],[False,True],[True,False],[False,False],[False,False],[False,True],[True,True],[False,False],[False,True],[False,True],[False,True],[False,True],[True,False],[False,False],[True,False],[True,True],[False,True],[False,True],[True,False],[False,True],[False,False],[False,False],[True,True],[False,False],[False,False],[True,False],[True,True],[False,False],[False,False],[False,True],[False,True],[False,True],[True,False],[False,False],[True,False],[False,True],[True,False],[True,False],[True,False],[False,False],[False,True],[False,False],[True,False],[False,True],[True,True],[False,True],[False,True],[False,True],[True,True],[False,False],[True,False],[False,False],[False,True],[True,False],[True,True],[False,False],[True,False],[False,False],[True,False],[True,False],[True,True],[True,False],[False,False],[True,False],[True,True],[False,False],[True,False],[True,False],[False,False],[False,True],[True,False],[True,False],[False,True],[False,True],[False,True],[True,True],[True,True],[True,True],[True,True],[True,False],[False,False],[False,False],[False,True],[False,False],[True,False],[False,True],[False,True],[True,False],[True,False],[False,True],[True,True],[False,False],[False,False],[False,True],[True,True],[True,True],[True,False],[True,False],[True,True],[False,True],[True,False],[False,True],[False,True],[False,True],[True,False],[False,True],[True,False],[True,False],[False,True],[True,True],[True,True],[True,False],[True,False],[False,False],[False,True],[True,True],[True,True],[True,True],[True,True],[False,False],[True,False],[True,False],[True,True],[False,True],[False,False],[True,True],[True,False],[False,False],[False,False],[False,False],[True,False],[False,True],[True,True],[False,False],[False,True],[True,True],[True,False],[True,False],[True,False],[False,False],[False,True],[True,True],[True,True],[True,True],[False,True],[False,True],[True,False],[False,True],[True,True],[True,True],[False,False],[False,True],[True,True],[False,False],[True,False],[False,True],[True,False],[False,False],[True,True],[True,True],[True,True],[True,False],[True,True],[True,False],[False,True],[True,False],[True,True],[False,False],[True,False],[True,False],[False,True],[False,True],[True,False],[True,True],[False,False],[False,True],[False,True],[True,True],[True,True],[False,True],[False,True],[False,True],[True,False],[False,False],[False,True],[False,False],[False,False],[True,False],[True,False],[True,True],[False,True],[False,False],[True,True],[False,False],[False,False],[True,False],[True,True],[False,False],[True,False],[False,True],[True,True],[True,True],[True,False],[True,False],[False,False],[True,True],[False,True],[True,True],[True,True],[True,True],[True,False],[False,True],[False,False],[True,True],[False,False],[True,True],[True,False],[False,False],[True,False],[True,True],[False,False],[False,False],[False,False],[True,True],[True,False],[False,True],[True,False],[False,True],[False,True],[False,False],[True,True],[True,False],[False,False],[True,True],[False,False],[False,False],[False,True],[True,False],[True,False],[True,False],[True,False],[True,False],[False,True],[True,True],[True,True],[True,False],[True,True],[True,True],[True,False],[False,True],[False,False],[True,False],[True,False],[True,False],[True,False],[True,False],[False,False],[False,True],[False,True],[False,True],[False,True],[True,True],[False,False],[False,True],[False,False],[False,False],[True,False],[True,False],[False,False],[True,True],[False,False],[True,True],[False,True],[False,False],[False,False],[True,True],[True,True],[False,False],[True,True],[True,False],[True,False],[False,False],[False,True],[True,False],[True,False],[False,False],[False,True],[True,False],[True,True],[True,True],[True,False],[False,False],[True,True],[False,True],[False,False],[True,True],[False,True],[False,False],[True,True],[False,False],[True,False],[False,True],[False,True],[True,True],[False,False],[False,True],[True,True],[False,False],[False,False],[True,False],[False,False],[True,False],[False,True],[False,True],[False,True],[True,True],[True,False],[False,True],[True,False],[False,False],[False,True],[True,True],[False,True],[False,False],[False,True],[False,False],[False,True],[True,False],[True,True],[True,True],[False,False],[True,False],[False,True],[True,False],[True,False],[False,False],[True,True],[True,True],[True,True],[True,True],[True,True],[True,True],[False,False],[True,True],[False,False],[True,False],[False,False],[False,True],[True,False],[True,True],[False,True],[True,True],[False,False],[False,True],[False,True],[False,True],[False,False],[False,False]], dtype = "bool")#candidate|9255|(624, 2)|const|bool
call_9254 = func_1202_call(relay.reshape(const_9255.astype('bool'), [8, 13, 12]))
call_9256 = func_1202_call(relay.reshape(const_9255.astype('bool'), [8, 13, 12]))
output = relay.Tuple([call_9189,call_9245,const_9246,call_9254,const_9255,])
output2 = relay.Tuple([call_9190,call_9247,const_9246,call_9256,const_9255,])
func_9272 = relay.Function([], output)
mod['func_9272'] = func_9272
mod = relay.transform.InferType()(mod)
output = func_9272()
func_9273 = relay.Function([], output)
mutated_mod['func_9273'] = func_9273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6649_call = mod.get_global_var('func_6649')
func_6651_call = mutated_mod.get_global_var('func_6651')
call_9292 = relay.TupleGetItem(func_6649_call(), 1)
call_9293 = relay.TupleGetItem(func_6651_call(), 1)
output = relay.Tuple([call_9292,])
output2 = relay.Tuple([call_9293,])
func_9335 = relay.Function([], output)
mod['func_9335'] = func_9335
mod = relay.transform.InferType()(mod)
mutated_mod['func_9335'] = func_9335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9335_call = mutated_mod.get_global_var('func_9335')
call_9336 = func_9335_call()
output = call_9336
func_9337 = relay.Function([], output)
mutated_mod['func_9337'] = func_9337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5641_call = mod.get_global_var('func_5641')
func_5643_call = mutated_mod.get_global_var('func_5643')
call_9340 = func_5641_call()
call_9341 = func_5641_call()
output = call_9340
output2 = call_9341
func_9357 = relay.Function([], output)
mod['func_9357'] = func_9357
mod = relay.transform.InferType()(mod)
mutated_mod['func_9357'] = func_9357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9357_call = mutated_mod.get_global_var('func_9357')
call_9358 = func_9357_call()
output = call_9358
func_9359 = relay.Function([], output)
mutated_mod['func_9359'] = func_9359
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6777_call = mod.get_global_var('func_6777')
func_6778_call = mutated_mod.get_global_var('func_6778')
call_9393 = func_6777_call()
call_9394 = func_6777_call()
output = relay.Tuple([call_9393,])
output2 = relay.Tuple([call_9394,])
func_9401 = relay.Function([], output)
mod['func_9401'] = func_9401
mod = relay.transform.InferType()(mod)
output = func_9401()
func_9402 = relay.Function([], output)
mutated_mod['func_9402'] = func_9402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8052_call = mod.get_global_var('func_8052')
func_8053_call = mutated_mod.get_global_var('func_8053')
call_9461 = relay.TupleGetItem(func_8052_call(), 0)
call_9462 = relay.TupleGetItem(func_8053_call(), 0)
output = call_9461
output2 = call_9462
func_9467 = relay.Function([], output)
mod['func_9467'] = func_9467
mod = relay.transform.InferType()(mod)
mutated_mod['func_9467'] = func_9467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9467_call = mutated_mod.get_global_var('func_9467')
call_9468 = func_9467_call()
output = call_9468
func_9469 = relay.Function([], output)
mutated_mod['func_9469'] = func_9469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7823_call = mod.get_global_var('func_7823')
func_7824_call = mutated_mod.get_global_var('func_7824')
call_9547 = func_7823_call()
call_9548 = func_7823_call()
func_7322_call = mod.get_global_var('func_7322')
func_7324_call = mutated_mod.get_global_var('func_7324')
call_9559 = relay.TupleGetItem(func_7322_call(), 1)
call_9560 = relay.TupleGetItem(func_7324_call(), 1)
output = relay.Tuple([call_9547,call_9559,])
output2 = relay.Tuple([call_9548,call_9560,])
func_9579 = relay.Function([], output)
mod['func_9579'] = func_9579
mod = relay.transform.InferType()(mod)
mutated_mod['func_9579'] = func_9579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9579_call = mutated_mod.get_global_var('func_9579')
call_9580 = func_9579_call()
output = call_9580
func_9581 = relay.Function([], output)
mutated_mod['func_9581'] = func_9581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8611_call = mod.get_global_var('func_8611')
func_8613_call = mutated_mod.get_global_var('func_8613')
call_9603 = relay.TupleGetItem(func_8611_call(), 0)
call_9604 = relay.TupleGetItem(func_8613_call(), 0)
func_7391_call = mod.get_global_var('func_7391')
func_7393_call = mutated_mod.get_global_var('func_7393')
call_9615 = relay.TupleGetItem(func_7391_call(), 1)
call_9616 = relay.TupleGetItem(func_7393_call(), 1)
output = relay.Tuple([call_9603,call_9615,])
output2 = relay.Tuple([call_9604,call_9616,])
func_9641 = relay.Function([], output)
mod['func_9641'] = func_9641
mod = relay.transform.InferType()(mod)
output = func_9641()
func_9642 = relay.Function([], output)
mutated_mod['func_9642'] = func_9642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8952_call = mod.get_global_var('func_8952')
func_8954_call = mutated_mod.get_global_var('func_8954')
call_9699 = relay.TupleGetItem(func_8952_call(), 0)
call_9700 = relay.TupleGetItem(func_8954_call(), 0)
output = relay.Tuple([call_9699,])
output2 = relay.Tuple([call_9700,])
func_9760 = relay.Function([], output)
mod['func_9760'] = func_9760
mod = relay.transform.InferType()(mod)
output = func_9760()
func_9761 = relay.Function([], output)
mutated_mod['func_9761'] = func_9761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8372_call = mod.get_global_var('func_8372')
func_8373_call = mutated_mod.get_global_var('func_8373')
call_9770 = relay.TupleGetItem(func_8372_call(), 1)
call_9771 = relay.TupleGetItem(func_8373_call(), 1)
output = call_9770
output2 = call_9771
func_9774 = relay.Function([], output)
mod['func_9774'] = func_9774
mod = relay.transform.InferType()(mod)
mutated_mod['func_9774'] = func_9774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9774_call = mutated_mod.get_global_var('func_9774')
call_9775 = func_9774_call()
output = call_9775
func_9776 = relay.Function([], output)
mutated_mod['func_9776'] = func_9776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3880_call = mod.get_global_var('func_3880')
func_3881_call = mutated_mod.get_global_var('func_3881')
call_9814 = relay.TupleGetItem(func_3880_call(), 0)
call_9815 = relay.TupleGetItem(func_3881_call(), 0)
func_9123_call = mod.get_global_var('func_9123')
func_9124_call = mutated_mod.get_global_var('func_9124')
call_9828 = relay.TupleGetItem(func_9123_call(), 0)
call_9829 = relay.TupleGetItem(func_9124_call(), 0)
func_9123_call = mod.get_global_var('func_9123')
func_9124_call = mutated_mod.get_global_var('func_9124')
call_9836 = relay.TupleGetItem(func_9123_call(), 0)
call_9837 = relay.TupleGetItem(func_9124_call(), 0)
func_5012_call = mod.get_global_var('func_5012')
func_5015_call = mutated_mod.get_global_var('func_5015')
const_9846 = relay.const(-5.814946, dtype = "float32")#candidate|9846|()|const|float32
call_9845 = relay.TupleGetItem(func_5012_call(relay.reshape(const_9846.astype('float32'), [])), 3)
call_9847 = relay.TupleGetItem(func_5015_call(relay.reshape(const_9846.astype('float32'), [])), 3)
func_8740_call = mod.get_global_var('func_8740')
func_8742_call = mutated_mod.get_global_var('func_8742')
call_9877 = func_8740_call()
call_9878 = func_8740_call()
output = relay.Tuple([call_9814,call_9828,call_9836,call_9845,const_9846,call_9877,])
output2 = relay.Tuple([call_9815,call_9829,call_9837,call_9847,const_9846,call_9878,])
func_9884 = relay.Function([], output)
mod['func_9884'] = func_9884
mod = relay.transform.InferType()(mod)
output = func_9884()
func_9885 = relay.Function([], output)
mutated_mod['func_9885'] = func_9885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9272_call = mod.get_global_var('func_9272')
func_9273_call = mutated_mod.get_global_var('func_9273')
call_9899 = relay.TupleGetItem(func_9272_call(), 0)
call_9900 = relay.TupleGetItem(func_9273_call(), 0)
output = relay.Tuple([call_9899,])
output2 = relay.Tuple([call_9900,])
func_9919 = relay.Function([], output)
mod['func_9919'] = func_9919
mod = relay.transform.InferType()(mod)
output = func_9919()
func_9920 = relay.Function([], output)
mutated_mod['func_9920'] = func_9920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5319_call = mod.get_global_var('func_5319')
func_5321_call = mutated_mod.get_global_var('func_5321')
call_9927 = relay.TupleGetItem(func_5319_call(), 0)
call_9928 = relay.TupleGetItem(func_5321_call(), 0)
func_5294_call = mod.get_global_var('func_5294')
func_5297_call = mutated_mod.get_global_var('func_5297')
var_9953 = relay.var("var_9953", dtype = "int16", shape = (2912,))#candidate|9953|(2912,)|var|int16
call_9952 = relay.TupleGetItem(func_5294_call(relay.reshape(var_9953.astype('int16'), [2912,])), 2)
call_9954 = relay.TupleGetItem(func_5297_call(relay.reshape(var_9953.astype('int16'), [2912,])), 2)
func_2044_call = mod.get_global_var('func_2044')
func_2046_call = mutated_mod.get_global_var('func_2046')
var_9956 = relay.var("var_9956", dtype = "float32", shape = (168,))#candidate|9956|(168,)|var|float32
call_9955 = relay.TupleGetItem(func_2044_call(relay.reshape(var_9956.astype('float32'), [1, 12, 14])), 0)
call_9957 = relay.TupleGetItem(func_2046_call(relay.reshape(var_9956.astype('float32'), [1, 12, 14])), 0)
func_4167_call = mod.get_global_var('func_4167')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_9959 = relay.TupleGetItem(func_4167_call(), 0)
call_9960 = relay.TupleGetItem(func_4169_call(), 0)
output = relay.Tuple([call_9927,call_9952,var_9953,call_9955,var_9956,call_9959,])
output2 = relay.Tuple([call_9928,call_9954,var_9953,call_9957,var_9956,call_9960,])
func_9967 = relay.Function([var_9953,var_9956,], output)
mod['func_9967'] = func_9967
mod = relay.transform.InferType()(mod)
var_9968 = relay.var("var_9968", dtype = "int16", shape = (2912,))#candidate|9968|(2912,)|var|int16
var_9969 = relay.var("var_9969", dtype = "float32", shape = (168,))#candidate|9969|(168,)|var|float32
output = func_9967(var_9968,var_9969,)
func_9970 = relay.Function([var_9968,var_9969,], output)
mutated_mod['func_9970'] = func_9970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5489_call = mod.get_global_var('func_5489')
func_5490_call = mutated_mod.get_global_var('func_5490')
call_9989 = relay.TupleGetItem(func_5489_call(), 0)
call_9990 = relay.TupleGetItem(func_5490_call(), 0)
func_4301_call = mod.get_global_var('func_4301')
func_4304_call = mutated_mod.get_global_var('func_4304')
var_10000 = relay.var("var_10000", dtype = "int32", shape = ())#candidate|10000|()|var|int32
call_9999 = relay.TupleGetItem(func_4301_call(relay.reshape(var_10000.astype('int32'), [])), 0)
call_10001 = relay.TupleGetItem(func_4304_call(relay.reshape(var_10000.astype('int32'), [])), 0)
output = relay.Tuple([call_9989,call_9999,var_10000,])
output2 = relay.Tuple([call_9990,call_10001,var_10000,])
func_10011 = relay.Function([var_10000,], output)
mod['func_10011'] = func_10011
mod = relay.transform.InferType()(mod)
mutated_mod['func_10011'] = func_10011
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10012 = relay.var("var_10012", dtype = "int32", shape = ())#candidate|10012|()|var|int32
func_10011_call = mutated_mod.get_global_var('func_10011')
call_10013 = func_10011_call(var_10012)
output = call_10013
func_10014 = relay.Function([var_10012], output)
mutated_mod['func_10014'] = func_10014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6228_call = mod.get_global_var('func_6228')
func_6230_call = mutated_mod.get_global_var('func_6230')
call_10054 = relay.TupleGetItem(func_6228_call(), 1)
call_10055 = relay.TupleGetItem(func_6230_call(), 1)
output = relay.Tuple([call_10054,])
output2 = relay.Tuple([call_10055,])
func_10056 = relay.Function([], output)
mod['func_10056'] = func_10056
mod = relay.transform.InferType()(mod)
output = func_10056()
func_10057 = relay.Function([], output)
mutated_mod['func_10057'] = func_10057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9401_call = mod.get_global_var('func_9401')
func_9402_call = mutated_mod.get_global_var('func_9402')
call_10096 = relay.TupleGetItem(func_9401_call(), 0)
call_10097 = relay.TupleGetItem(func_9402_call(), 0)
output = relay.Tuple([call_10096,])
output2 = relay.Tuple([call_10097,])
func_10103 = relay.Function([], output)
mod['func_10103'] = func_10103
mod = relay.transform.InferType()(mod)
mutated_mod['func_10103'] = func_10103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10103_call = mutated_mod.get_global_var('func_10103')
call_10104 = func_10103_call()
output = call_10104
func_10105 = relay.Function([], output)
mutated_mod['func_10105'] = func_10105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6777_call = mod.get_global_var('func_6777')
func_6778_call = mutated_mod.get_global_var('func_6778')
call_10120 = func_6777_call()
call_10121 = func_6777_call()
func_8407_call = mod.get_global_var('func_8407')
func_8409_call = mutated_mod.get_global_var('func_8409')
call_10131 = relay.TupleGetItem(func_8407_call(), 1)
call_10132 = relay.TupleGetItem(func_8409_call(), 1)
func_8295_call = mod.get_global_var('func_8295')
func_8296_call = mutated_mod.get_global_var('func_8296')
call_10193 = relay.TupleGetItem(func_8295_call(), 0)
call_10194 = relay.TupleGetItem(func_8296_call(), 0)
func_8052_call = mod.get_global_var('func_8052')
func_8053_call = mutated_mod.get_global_var('func_8053')
call_10204 = relay.TupleGetItem(func_8052_call(), 0)
call_10205 = relay.TupleGetItem(func_8053_call(), 0)
output = relay.Tuple([call_10120,call_10131,call_10193,call_10204,])
output2 = relay.Tuple([call_10121,call_10132,call_10194,call_10205,])
func_10206 = relay.Function([], output)
mod['func_10206'] = func_10206
mod = relay.transform.InferType()(mod)
mutated_mod['func_10206'] = func_10206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10206_call = mutated_mod.get_global_var('func_10206')
call_10207 = func_10206_call()
output = call_10207
func_10208 = relay.Function([], output)
mutated_mod['func_10208'] = func_10208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9101_call = mod.get_global_var('func_9101')
func_9103_call = mutated_mod.get_global_var('func_9103')
call_10230 = relay.TupleGetItem(func_9101_call(), 0)
call_10231 = relay.TupleGetItem(func_9103_call(), 0)
func_6777_call = mod.get_global_var('func_6777')
func_6778_call = mutated_mod.get_global_var('func_6778')
call_10248 = func_6777_call()
call_10249 = func_6777_call()
output = relay.Tuple([call_10230,call_10248,])
output2 = relay.Tuple([call_10231,call_10249,])
func_10272 = relay.Function([], output)
mod['func_10272'] = func_10272
mod = relay.transform.InferType()(mod)
mutated_mod['func_10272'] = func_10272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10272_call = mutated_mod.get_global_var('func_10272')
call_10273 = func_10272_call()
output = call_10273
func_10274 = relay.Function([], output)
mutated_mod['func_10274'] = func_10274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4167_call = mod.get_global_var('func_4167')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_10307 = relay.TupleGetItem(func_4167_call(), 0)
call_10308 = relay.TupleGetItem(func_4169_call(), 0)
output = relay.Tuple([call_10307,])
output2 = relay.Tuple([call_10308,])
func_10318 = relay.Function([], output)
mod['func_10318'] = func_10318
mod = relay.transform.InferType()(mod)
mutated_mod['func_10318'] = func_10318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10318_call = mutated_mod.get_global_var('func_10318')
call_10319 = func_10318_call()
output = call_10319
func_10320 = relay.Function([], output)
mutated_mod['func_10320'] = func_10320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9335_call = mod.get_global_var('func_9335')
func_9337_call = mutated_mod.get_global_var('func_9337')
call_10336 = relay.TupleGetItem(func_9335_call(), 0)
call_10337 = relay.TupleGetItem(func_9337_call(), 0)
func_8295_call = mod.get_global_var('func_8295')
func_8296_call = mutated_mod.get_global_var('func_8296')
call_10346 = relay.TupleGetItem(func_8295_call(), 0)
call_10347 = relay.TupleGetItem(func_8296_call(), 0)
output = relay.Tuple([call_10336,call_10346,])
output2 = relay.Tuple([call_10337,call_10347,])
func_10358 = relay.Function([], output)
mod['func_10358'] = func_10358
mod = relay.transform.InferType()(mod)
mutated_mod['func_10358'] = func_10358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10358_call = mutated_mod.get_global_var('func_10358')
call_10359 = func_10358_call()
output = call_10359
func_10360 = relay.Function([], output)
mutated_mod['func_10360'] = func_10360
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10425 = relay.var("var_10425", dtype = "float32", shape = (13, 10, 6))#candidate|10425|(13, 10, 6)|var|float32
var_10426 = relay.var("var_10426", dtype = "float32", shape = (13, 10, 6))#candidate|10426|(13, 10, 6)|var|float32
bop_10427 = relay.less_equal(var_10425.astype('bool'), relay.reshape(var_10426.astype('bool'), relay.shape_of(var_10425))) # shape=(13, 10, 6)
func_9401_call = mod.get_global_var('func_9401')
func_9402_call = mutated_mod.get_global_var('func_9402')
call_10440 = relay.TupleGetItem(func_9401_call(), 0)
call_10441 = relay.TupleGetItem(func_9402_call(), 0)
func_8319_call = mod.get_global_var('func_8319')
func_8320_call = mutated_mod.get_global_var('func_8320')
call_10449 = func_8319_call()
call_10450 = func_8319_call()
func_5548_call = mod.get_global_var('func_5548')
func_5550_call = mutated_mod.get_global_var('func_5550')
call_10460 = relay.TupleGetItem(func_5548_call(), 0)
call_10461 = relay.TupleGetItem(func_5550_call(), 0)
uop_10473 = relay.exp(var_10426.astype('float32')) # shape=(13, 10, 6)
bop_10478 = relay.bitwise_and(uop_10473.astype('int32'), relay.reshape(var_10426.astype('int32'), relay.shape_of(uop_10473))) # shape=(13, 10, 6)
output = relay.Tuple([bop_10427,call_10440,call_10449,call_10460,bop_10478,])
output2 = relay.Tuple([bop_10427,call_10441,call_10450,call_10461,bop_10478,])
func_10482 = relay.Function([var_10425,var_10426,], output)
mod['func_10482'] = func_10482
mod = relay.transform.InferType()(mod)
var_10483 = relay.var("var_10483", dtype = "float32", shape = (13, 10, 6))#candidate|10483|(13, 10, 6)|var|float32
var_10484 = relay.var("var_10484", dtype = "float32", shape = (13, 10, 6))#candidate|10484|(13, 10, 6)|var|float32
output = func_10482(var_10483,var_10484,)
func_10485 = relay.Function([var_10483,var_10484,], output)
mutated_mod['func_10485'] = func_10485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6898_call = mod.get_global_var('func_6898')
func_6900_call = mutated_mod.get_global_var('func_6900')
call_10518 = relay.TupleGetItem(func_6898_call(), 0)
call_10519 = relay.TupleGetItem(func_6900_call(), 0)
output = relay.Tuple([call_10518,])
output2 = relay.Tuple([call_10519,])
func_10527 = relay.Function([], output)
mod['func_10527'] = func_10527
mod = relay.transform.InferType()(mod)
output = func_10527()
func_10528 = relay.Function([], output)
mutated_mod['func_10528'] = func_10528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8372_call = mod.get_global_var('func_8372')
func_8373_call = mutated_mod.get_global_var('func_8373')
call_10537 = relay.TupleGetItem(func_8372_call(), 0)
call_10538 = relay.TupleGetItem(func_8373_call(), 0)
func_6950_call = mod.get_global_var('func_6950')
func_6951_call = mutated_mod.get_global_var('func_6951')
call_10546 = relay.TupleGetItem(func_6950_call(), 1)
call_10547 = relay.TupleGetItem(func_6951_call(), 1)
output = relay.Tuple([call_10537,call_10546,])
output2 = relay.Tuple([call_10538,call_10547,])
func_10568 = relay.Function([], output)
mod['func_10568'] = func_10568
mod = relay.transform.InferType()(mod)
mutated_mod['func_10568'] = func_10568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10568_call = mutated_mod.get_global_var('func_10568')
call_10569 = func_10568_call()
output = call_10569
func_10570 = relay.Function([], output)
mutated_mod['func_10570'] = func_10570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9760_call = mod.get_global_var('func_9760')
func_9761_call = mutated_mod.get_global_var('func_9761')
call_10574 = relay.TupleGetItem(func_9760_call(), 0)
call_10575 = relay.TupleGetItem(func_9761_call(), 0)
func_8823_call = mod.get_global_var('func_8823')
func_8824_call = mutated_mod.get_global_var('func_8824')
call_10586 = relay.TupleGetItem(func_8823_call(), 1)
call_10587 = relay.TupleGetItem(func_8824_call(), 1)
output = relay.Tuple([call_10574,call_10586,])
output2 = relay.Tuple([call_10575,call_10587,])
func_10592 = relay.Function([], output)
mod['func_10592'] = func_10592
mod = relay.transform.InferType()(mod)
output = func_10592()
func_10593 = relay.Function([], output)
mutated_mod['func_10593'] = func_10593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9335_call = mod.get_global_var('func_9335')
func_9337_call = mutated_mod.get_global_var('func_9337')
call_10598 = relay.TupleGetItem(func_9335_call(), 0)
call_10599 = relay.TupleGetItem(func_9337_call(), 0)
output = relay.Tuple([call_10598,])
output2 = relay.Tuple([call_10599,])
func_10613 = relay.Function([], output)
mod['func_10613'] = func_10613
mod = relay.transform.InferType()(mod)
mutated_mod['func_10613'] = func_10613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10613_call = mutated_mod.get_global_var('func_10613')
call_10614 = func_10613_call()
output = call_10614
func_10615 = relay.Function([], output)
mutated_mod['func_10615'] = func_10615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10613_call = mod.get_global_var('func_10613')
func_10615_call = mutated_mod.get_global_var('func_10615')
call_10626 = relay.TupleGetItem(func_10613_call(), 0)
call_10627 = relay.TupleGetItem(func_10615_call(), 0)
func_3880_call = mod.get_global_var('func_3880')
func_3881_call = mutated_mod.get_global_var('func_3881')
call_10628 = relay.TupleGetItem(func_3880_call(), 0)
call_10629 = relay.TupleGetItem(func_3881_call(), 0)
output = relay.Tuple([call_10626,call_10628,])
output2 = relay.Tuple([call_10627,call_10629,])
func_10636 = relay.Function([], output)
mod['func_10636'] = func_10636
mod = relay.transform.InferType()(mod)
output = func_10636()
func_10637 = relay.Function([], output)
mutated_mod['func_10637'] = func_10637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10636_call = mod.get_global_var('func_10636')
func_10637_call = mutated_mod.get_global_var('func_10637')
call_10691 = relay.TupleGetItem(func_10636_call(), 0)
call_10692 = relay.TupleGetItem(func_10637_call(), 0)
func_342_call = mod.get_global_var('func_342')
func_345_call = mutated_mod.get_global_var('func_345')
const_10701 = relay.const(-7, dtype = "int32")#candidate|10701|()|const|int32
const_10702 = relay.const([10,10,-1,-2,5,-10,9,-2,7,-4,-7,3,5,3,-6,5,-4,3,-10,-10,9,9,-4,-5,-2,-9,3,10,3,-2,-2,7,4,1,-5,10,-1,-1,1,-3,7,4,6,-10,5,-10,-8,3,8,-7,-5,6,5,10,-3,9,-8,10,4,5,-1,-8,-3,-3,5,4,7,7,-7,-8,-3,-8,7,-5,7,2,-6,-9,1,9,-1,7,5,10,2,-10,-4,-6,-6,1,4,9,4,-10,-9,-3,4,-10,6,8,-9,-5,-7,-3,-5,-4,8,8,3,-8,-6,5,-1,-10,-5,6,-7,7,5,8,-4,8,8,-5,5,5,2,-3,5,1,2,-5,2,4,2,7,4,8,-5,-5,4,-2,-10,-1,-10,4,-2,10,1,-1,-8,8,6,-6,-9,-1,-2,1,-10,6,7,-2,9,10,10,2,10,1,-8,-6,9,1,-10,1,7,2,7,2,5,-7,-3,-2,1,-8,-2,5,2,1,10,-4,1,-2,7,4,6,-9,-2,-2,6,-3,4,10,-6,10,4,5,-9,2,1,-9,9,7,-3,-6,1,-9,-9,-3,-7,1,6,-7,-4,-2,-6,5,-1,9,-1,4,6,7,10,10,-2,1,10,-2,6,1,-4,-9,9,10,-3,-10,-8,6,-6,9,9,7,-7,-4,-4,7,1,5,-4,-10,3,-9,8,1,2,-3,10,-10,10,2,-9,3,6,2,5,10,3,-1,5,-6], dtype = "int32")#candidate|10702|(280,)|const|int32
call_10700 = relay.TupleGetItem(func_342_call(relay.reshape(const_10701.astype('int32'), []), relay.reshape(const_10702.astype('int32'), [8, 5, 7]), ), 0)
call_10703 = relay.TupleGetItem(func_345_call(relay.reshape(const_10701.astype('int32'), []), relay.reshape(const_10702.astype('int32'), [8, 5, 7]), ), 0)
func_4941_call = mod.get_global_var('func_4941')
func_4944_call = mutated_mod.get_global_var('func_4944')
var_10736 = relay.var("var_10736", dtype = "float32", shape = (168,))#candidate|10736|(168,)|var|float32
call_10735 = relay.TupleGetItem(func_4941_call(relay.reshape(const_10701.astype('float32'), []), relay.reshape(var_10736.astype('float32'), [168,]), ), 1)
call_10737 = relay.TupleGetItem(func_4944_call(relay.reshape(const_10701.astype('float32'), []), relay.reshape(var_10736.astype('float32'), [168,]), ), 1)
func_5489_call = mod.get_global_var('func_5489')
func_5490_call = mutated_mod.get_global_var('func_5490')
call_10739 = relay.TupleGetItem(func_5489_call(), 0)
call_10740 = relay.TupleGetItem(func_5490_call(), 0)
output = relay.Tuple([call_10691,call_10700,const_10701,const_10702,call_10735,var_10736,call_10739,])
output2 = relay.Tuple([call_10692,call_10703,const_10701,const_10702,call_10737,var_10736,call_10740,])
func_10746 = relay.Function([var_10736,], output)
mod['func_10746'] = func_10746
mod = relay.transform.InferType()(mod)
var_10747 = relay.var("var_10747", dtype = "float32", shape = (168,))#candidate|10747|(168,)|var|float32
output = func_10746(var_10747)
func_10748 = relay.Function([var_10747], output)
mutated_mod['func_10748'] = func_10748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8173_call = mod.get_global_var('func_8173')
func_8174_call = mutated_mod.get_global_var('func_8174')
call_10771 = relay.TupleGetItem(func_8173_call(), 0)
call_10772 = relay.TupleGetItem(func_8174_call(), 0)
func_5548_call = mod.get_global_var('func_5548')
func_5550_call = mutated_mod.get_global_var('func_5550')
call_10791 = relay.TupleGetItem(func_5548_call(), 0)
call_10792 = relay.TupleGetItem(func_5550_call(), 0)
output = relay.Tuple([call_10771,call_10791,])
output2 = relay.Tuple([call_10772,call_10792,])
func_10797 = relay.Function([], output)
mod['func_10797'] = func_10797
mod = relay.transform.InferType()(mod)
output = func_10797()
func_10798 = relay.Function([], output)
mutated_mod['func_10798'] = func_10798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8295_call = mod.get_global_var('func_8295')
func_8296_call = mutated_mod.get_global_var('func_8296')
call_10824 = relay.TupleGetItem(func_8295_call(), 0)
call_10825 = relay.TupleGetItem(func_8296_call(), 0)
output = call_10824
output2 = call_10825
func_10828 = relay.Function([], output)
mod['func_10828'] = func_10828
mod = relay.transform.InferType()(mod)
output = func_10828()
func_10829 = relay.Function([], output)
mutated_mod['func_10829'] = func_10829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9579_call = mod.get_global_var('func_9579')
func_9581_call = mutated_mod.get_global_var('func_9581')
call_10847 = relay.TupleGetItem(func_9579_call(), 1)
call_10848 = relay.TupleGetItem(func_9581_call(), 1)
func_342_call = mod.get_global_var('func_342')
func_345_call = mutated_mod.get_global_var('func_345')
var_10858 = relay.var("var_10858", dtype = "int32", shape = ())#candidate|10858|()|var|int32
var_10859 = relay.var("var_10859", dtype = "int32", shape = (280,))#candidate|10859|(280,)|var|int32
call_10857 = relay.TupleGetItem(func_342_call(relay.reshape(var_10858.astype('int32'), []), relay.reshape(var_10859.astype('int32'), [8, 5, 7]), ), 0)
call_10860 = relay.TupleGetItem(func_345_call(relay.reshape(var_10858.astype('int32'), []), relay.reshape(var_10859.astype('int32'), [8, 5, 7]), ), 0)
output = relay.Tuple([call_10847,call_10857,var_10858,var_10859,])
output2 = relay.Tuple([call_10848,call_10860,var_10858,var_10859,])
func_10868 = relay.Function([var_10858,var_10859,], output)
mod['func_10868'] = func_10868
mod = relay.transform.InferType()(mod)
mutated_mod['func_10868'] = func_10868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10868_call = mutated_mod.get_global_var('func_10868')
var_10870 = relay.var("var_10870", dtype = "int32", shape = ())#candidate|10870|()|var|int32
var_10871 = relay.var("var_10871", dtype = "int32", shape = (280,))#candidate|10871|(280,)|var|int32
call_10869 = func_10868_call(var_10870,var_10871,)
output = call_10869
func_10872 = relay.Function([var_10870,var_10871,], output)
mutated_mod['func_10872'] = func_10872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7823_call = mod.get_global_var('func_7823')
func_7824_call = mutated_mod.get_global_var('func_7824')
call_10876 = func_7823_call()
call_10877 = func_7823_call()
output = call_10876
output2 = call_10877
func_10898 = relay.Function([], output)
mod['func_10898'] = func_10898
mod = relay.transform.InferType()(mod)
output = func_10898()
func_10899 = relay.Function([], output)
mutated_mod['func_10899'] = func_10899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8465_call = mod.get_global_var('func_8465')
func_8467_call = mutated_mod.get_global_var('func_8467')
call_10910 = relay.TupleGetItem(func_8465_call(), 0)
call_10911 = relay.TupleGetItem(func_8467_call(), 0)
output = call_10910
output2 = call_10911
func_10929 = relay.Function([], output)
mod['func_10929'] = func_10929
mod = relay.transform.InferType()(mod)
mutated_mod['func_10929'] = func_10929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10929_call = mutated_mod.get_global_var('func_10929')
call_10930 = func_10929_call()
output = call_10930
func_10931 = relay.Function([], output)
mutated_mod['func_10931'] = func_10931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4139_call = mod.get_global_var('func_4139')
func_4141_call = mutated_mod.get_global_var('func_4141')
call_10952 = relay.TupleGetItem(func_4139_call(), 0)
call_10953 = relay.TupleGetItem(func_4141_call(), 0)
func_8138_call = mod.get_global_var('func_8138')
func_8139_call = mutated_mod.get_global_var('func_8139')
call_10954 = relay.TupleGetItem(func_8138_call(), 0)
call_10955 = relay.TupleGetItem(func_8139_call(), 0)
func_7823_call = mod.get_global_var('func_7823')
func_7824_call = mutated_mod.get_global_var('func_7824')
call_10957 = func_7823_call()
call_10958 = func_7823_call()
func_1202_call = mod.get_global_var('func_1202')
func_1204_call = mutated_mod.get_global_var('func_1204')
const_10966 = relay.const([False,False,False,False,False,True,False,True,False,False,True,True,False,True,True,False,False,True,False,False,False,True,True,True,False,False,True,True,False,True,True,False,True,True,False,True,True,False,False,True,True,False,True,True,True,False,True,False,True,True,False,True,False,True,True,False,True,False,True,True,True,False,True,False,False,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False,True,False,False,False,True,True,True,True,True,True,False,False,False,False,True,False,True,True,False,True,False,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False,True,True,True,False,False,True,False,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,True,True,False,False,True,True,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True,False,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,False,False,True,False,True,False,True,True,False,True,True,False,False,True,False,False,True,True,True,True,True,False,False,False,True,False,False,True,True,False,False,True,True,True,True,False,True,False,True,True,False,True,False,False,False,False,True,False,True,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,False,True,False,True,False,False,True,False,True,True,False,True,True,True,True,False,False,False,False,True,False,False,True,False,True,False,True,False,True,True,False,True,False,False,False,False,False,True,False,True,False,True,True,True,False,False,True,False,True,True,True,True,False,False,True,True,False,False,True,True,True,True,False,True,True,True,False,False,False,False,True,True,True,False,False,False,True,False,False,False,True,False,True,True,False,False,False,True,False,True,False,True,False,True,False,False,False,False,False,False,True,True,True,False,False,False,False,True,False,True,True,True,True,False,True,True,False,True,False,False,True,True,True,True,False,True,True,False,False,True,False,True,True,False,True,True,False,False,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,True,True,False,True,True,True,False,True,True,True,True,False,False,True,False,True,False,True,True,True,False,True,True,True,False,False,True,True,True,False,True,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,False,False,True,True,True,False,False,False,True,True,False,False,False,True,True,True,False,True,False,False,False,False,False,True,True,False,True,False,True,False,False,True,False,False,False,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,False,True,False,False,False,False,True,True,True,False,True,True,True,True,True,False,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,True,True,True,True,False,True,True,True,False,True,False,True,False,True,False,False,False,True,False,False,True,False,False,True,True,False,False,True,True,False,False,False,False,True,True,False,True,False,True,True,False,True,True,False,True,True,True,True,False,True,True,False,False,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,False,False,False,True,True,False,True,False,True,True,False,False,True,True,False,True,True,True,False,False,False,False,True,False,False,True,False,False,True,False,False,False,False,False,True,False,False,False,False,True,True,False,True,False,True,False,True,False,True,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,True,False,False,False,True,False,False,True,False,False,True,False,False,False,True,True,False,True,True,False,True,False,True,False,True,False,True,True,True,False,True,True,False,False,True,False,False,True,True,False,True,False,False,False,False,False,True,True,True,True,True,True,True,False,True,False,False,False,False,False,False,True,True,True,True,False,True,True,True,False,False,True,False,False,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,True,False,False,True,True,True,False,True,False,False,False,False,False,True,False,False,False,True,True,True,False,True,False,True,False,True,True,False,True,True,False,False,True,False,True,False,False,False,True,False,False,True,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,False,True,False,False,False,True,True,True,True,True,True,False,True,True,False,False,True,True,False,False,False,False,True,True,True,False,False,False,False,False,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,True,False,True,False,True,True,False,True,False,False,True,True,False,True,False,False,False,True,False,True,False,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,False,False,True,False,False,False,True,True,True,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,False,True,False,True,False,False,True,False,False,False,True,False,True,False,True,False,False,True,False,True,False,False,True,True,False,False,True,True,False,False,True,False,True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,True,False,True,False,True,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,True,True,False,False,True,True,True,True,True,False,True,False,False,False,False,False,True,False,True,True,True,False,False,False,False,False,True,True,False,True,True,True,False,True,False,True,False,True,True,True,True,False,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,False,True,True,False,False,False,True,False,False,False,True,False,False,True,False,True,True,False,True,False,True,False,False,True,True,True,False,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False,True,False,True,True,True,False,False,False,False,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,True,True,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False,True,True,False,False,True,False,True,False,True,False,True,False,False,False,True,True,False,False,True,False,False,True,False,False,False,False,True,True,True,False,True,False,True,True,False,False,True,False,False,False,False], dtype = "bool")#candidate|10966|(1248,)|const|bool
call_10965 = func_1202_call(relay.reshape(const_10966.astype('bool'), [8, 13, 12]))
call_10967 = func_1202_call(relay.reshape(const_10966.astype('bool'), [8, 13, 12]))
func_9101_call = mod.get_global_var('func_9101')
func_9103_call = mutated_mod.get_global_var('func_9103')
call_10968 = relay.TupleGetItem(func_9101_call(), 0)
call_10969 = relay.TupleGetItem(func_9103_call(), 0)
func_4011_call = mod.get_global_var('func_4011')
func_4014_call = mutated_mod.get_global_var('func_4014')
const_10974 = relay.const([-0.325327,3.401499,-1.213145,-2.369088,-0.017541,-9.850848,-3.375923,8.556397,-0.600430,5.660131,0.420448,-9.710404,-9.868690,5.829639,-2.617492,-3.937223,-1.515160,-6.233067,-4.786603,8.734431,7.903348,1.809025,5.796053,8.788408,-4.374701,-8.084487,7.587073,-1.276172,-0.390975,-5.662828,9.337917,5.903949,-5.354794,4.475716,-2.081239,9.662577,-4.083185,1.365557,8.303249,1.716355,2.236233,-9.765644,-6.808411,4.018438,-8.418975,5.094649,-5.134069,-7.303197,-2.677664,7.442847,-9.099685,0.482496,0.230582,5.946036,6.108868,-3.784867,-4.092953,-4.872245,9.377499,-6.489798,1.327566,-1.236633,-1.041790,-2.739369,-6.568353,-0.394277,4.737926,8.681994,-1.736741,3.779141,4.199588,9.117074,-4.707338,-0.149382,5.254435,-2.302277,-4.922145,-8.762499,6.648256,1.177952,-8.682530,-5.570166,7.075064,-3.411590,-7.796842,-5.012786,9.024580,-9.024619,0.686701,4.890947,1.152914,3.358561,-0.207591,-9.280281,-2.643235,5.046029], dtype = "float64")#candidate|10974|(96,)|const|float64
call_10973 = relay.TupleGetItem(func_4011_call(relay.reshape(const_10974.astype('float64'), [96,])), 0)
call_10975 = relay.TupleGetItem(func_4014_call(relay.reshape(const_10974.astype('float64'), [96,])), 0)
func_6208_call = mod.get_global_var('func_6208')
func_6209_call = mutated_mod.get_global_var('func_6209')
call_10979 = relay.TupleGetItem(func_6208_call(), 0)
call_10980 = relay.TupleGetItem(func_6209_call(), 0)
output = relay.Tuple([call_10952,call_10954,call_10957,call_10965,const_10966,call_10968,call_10973,const_10974,call_10979,])
output2 = relay.Tuple([call_10953,call_10955,call_10958,call_10967,const_10966,call_10969,call_10975,const_10974,call_10980,])
func_10983 = relay.Function([], output)
mod['func_10983'] = func_10983
mod = relay.transform.InferType()(mod)
mutated_mod['func_10983'] = func_10983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10983_call = mutated_mod.get_global_var('func_10983')
call_10984 = func_10983_call()
output = call_10984
func_10985 = relay.Function([], output)
mutated_mod['func_10985'] = func_10985
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11000 = relay.var("var_11000", dtype = "float32", shape = (8, 4, 6))#candidate|11000|(8, 4, 6)|var|float32
var_11001 = relay.var("var_11001", dtype = "float32", shape = (8, 4, 6))#candidate|11001|(8, 4, 6)|var|float32
bop_11002 = relay.floor_divide(var_11000.astype('float32'), relay.reshape(var_11001.astype('float32'), relay.shape_of(var_11000))) # shape=(8, 4, 6)
func_5790_call = mod.get_global_var('func_5790')
func_5793_call = mutated_mod.get_global_var('func_5793')
const_11016 = relay.const([-8,-3,2,-4,-5,4,5,4,10,-10,3,7,-7,10,9,4,-2,6,2,-6,3,6,-1,9,-2,2,-10,9,-9,-5,-10,6,5,7,3,4,-3,-5,-1,-8,5,8,-10,5,6,8,9,10,-9,9,8,10,-6,-8,1,-1,5,-4,-8,6,6,-10,9,9,4,-2,5,-6,8,9,-9,6,2,8,-6,4,10,9,3,-9,-7,-1,-4,-3,-10,-10,3,-2,-3,-4,5,-4,-9,4,10,1,6,-8,-9,-1,-3,8,8,-10,-10,-1,-2,2,8,5,1,5,-8,-8,-4,-7,-1,-3,-5,-9,9,2,4,3,9,-10,-4,8,8,8,-4,-10,-10,-3,10,-1,-1,-8,-6,9,-9,-6,3,-4,9,-6,-6,7,1,-2,1,10,8,-8,-9,10,5,-2,1,1,7,-4,-4,-3,-10,-8,10,-4,5,3,-9,5,-10,-10,10,-10,7,-4,-4,7,-1,8,2,10,-3,5,-5,-4,5,5,-5,4,10,4,4,1,-8,-9,-8,-10,-3,3,-3,-2,-2,4,3,-1,8,8,-9,-9,7,-7,-8,-7,10,-8,6,-1,-6,-6,-5,-3,-4,-6,9,10,-5,10,4,6,-7,8,4,-4,6,-1,-8,-5,5,-3,-7,10,-2,7,10,-1,-8,2,10,-4,7,7,-10,-6,-4,-9,4,4,2,1,5,-8,-10,-4,-6,5,4,7,-6,6,3,-2,-7,-4,-8,-8,6,-5,-6,-5,9,-6,-5,6,-9,5,10,-1,-4,5,-10,4,-2,-2,-1,-1,-8,3,3,9,4,3,1,-2,-9,-6,3,-6,-10,1,5,2,-2,-1,6,6,1,-5,-1,7,3,10,-3,9,3,7,-6,5,7,3,-3,-5,-6,9,5,-9,9,-4,-6,-8,-7,-10,5,10,-9,-7,-2,9,3,7,-3,-6,-10,5,-7,6,9,8,-1,-7,-3,-7,7,5,5,7,2,10,-8,-7,-7,1,-1,9,-9,-6,-3,9,10,-1,8,3,-5,-2,-8,-8,-6,-1,9,-10,-8,-3,1,2,-6,6,-3,5,-2,1,-10,4,-9,2,5,-10,-10,4,5,-3,-1,6,-8,1,10,1,-10,-3,-10,-1,-6,-7,-4,-8,-1,9,-9,-5,5,-10,-8,2,-8,1,1,4,-2,6,6,-4,-4,-6,-5,-2,8,5,5,-6,-2,2,8,1,-6,8,10,8,3,10,6,-10,6,-10,3,-3,-2,8,-10,2,7,-8,1,4,-10,6,6,8,-9,2,-4,-7,-9,-8,8,-5,-1,-6,10,8,4,-6,10,-2,-4,-3,1,-5,-8,1,5,3,-2,-8,-10,-4,2,7,-6,1,5,-8,-5,-1,8,-9,10,6,-2,6,-3,-6,-10,7,4,-6,3,7,9,-2,-10,9,-4,3,3,8,10,3,9,-6,9,1,-7,1,-6,4,-4,7,-10,-4,2,1,7,3,-1,10,10,1,10,5,4,10,-4,4,9,-9,9,2,1,4,4,-3,5,-4,-7,-9,-8,-7,-7,-6,-10,-7,4,-6,5,-8,-6,-5,-6,-8,-10,2,-7,2,-1,-2,5,9,-9,6,-7,-2,7,5,-8,6,9,8,8,-2,10,9,3,5,-5,3,5,-6,-7,-6,4,-5,-10,9,-4,-9,6,2,-6,-9,-7,-2,2,-7,-8,3,6,3,10,-6,-6,1,-2,9,-9,8,5,-2,-7,3,3,5,4,5,-3,-10,-5,9,5,5,10,-2,5,-9,1,10,-8,3,-5,7,9,-5,10,2,-3,9,-10,6,3,10,9,-9,-4,-10,1,7,5,-4,5,10,3,-1,10,-2,5,10,1,1,-4,-6,-8,-6,-4,-10,8,-9,1,6,1,6,-10,-10,-8,6,-3,6,5,4,2,-10,-6,-1,-1,8,-5,-8,3,-5,10,-2,6,-6,-9,2,-6,2,-1,9,-10,-6,3,1,3,-8,1,-7,9,-10,6,10,4,4,-6,9,-7,-2,-8,-8,-9,3,-8,9,-4,8,10,-1,-1,-10,-5,-3,-2,5,-6,-1,1,6,-6,9,-5,9,-4,-10,3,-9,8,3,7,-2,-10,9,-10,-3,2,-6,8,2,6,-6,-3,9,9,5,-9,8,-1,1,1,-10,5,-2,1,-4,10,-10,-6,-6,1,10,8,9,4,5,-5,10,10,2,10,10,5,2,-1,6,-2,3,-4,-3,2,6,10,-7,10,4,5,-9,-6,-4,1,-10,-6,-5,5,1,-6,5,2,8,3,-1,6,9,-3,8,4,-7,8,3,7,-1,10,9,-9,-4,-9,-1,7,4,4,3,9,-10,-1,-2,-6,3,10,8,9,4,-6,-2,6,2,9,9,5,-6,-4,-5,1,6,10,-3,-5,8,1,-6,-5,10,-4,-1,-10,-5,3,-5,-8,8,-5,8,7,3,5,6,10,3,6,-4,10,1,9,-10,8,-4,8,-5,7,2,9,-1,5,-4,-7,9,8,-3,-7,4,2,8,-2,-2,3,9,5,1,-4,-4,3,-10,-3,-8,7,-6,1,-6,7,10,-5,1,10,1,9,7,-9,3,-10,-4,4,-6,6,-6,4,-2,-6,9,5,2,-7,5,3,-10,8,2,4,7,-9,-2,10,2,-6,-3,-4,4,1,-7,-9,9,-1,-9,8,4,8,2,9,-5,-6,-8,1,-4,-3,-1,8,-10,-1,-3,-7,-8,-4,-3,6,-9,-4,5,-1,2,-9,-8,2,-7,9,4,8,10,-4,-6,1,-3,2,-2,8,-9,-6,-6,-5,3,-3,-9,-1,-5,-2,-5,4,-7,7,-1,5,2,7,2,-10,-5,4,-6,-2,9,-9,6,2,4,-3,4,5,1,-3,5,10,8,7,-2,-4,5,-7,1,-4,-9,-9,7,7,7,1,-5,5,8,7,1,10,7,4,-7,10,-5,8,-3,10,-7,4,-5,-5,-9,2,4,-5,-1,8,7,-5,6,-6,2,-1,-6,-3,3,3,-10,3,1,6,7,2,-1,8,-4,-6,-10,-7,1,-9,-10,10,1,6,3,6,6,-6,6,-2,-10,-9,5,-1,8,3,-4,7,-8,7,-5,-3,-10,-7,7,-1,8,-9,7,-1,10,2,9,-1,-4,-10,3,1,-4,-2,-8,8,-2,-10,7,-4,7,2,5,5,-4,-10,10,-10,10,7,-4,5,-4,-5,-8,9,-4,1,4,1,-1,-3,-2,7,-5,-9,9,-5,1,-3,8,4,5,-1,3,7,3,-7,4,-9,8,10,-4,-2,6,3,7,5,-5,1,10,-2,-9,-10,-2,-4,6,10,8,6,7,-7,9,6,-8,-1,-8,-1,-1,10,9,4,7,-9,3,-8,-5,5,-4,-7,2,3,1,7,-5,5,-2,-3,-2,5,-6,-8,-5,-4,-7,-5,8,-9,2,-1,4,2,5,-4,-6,2,1,4,4,6,10,10,-9,-9,4,7,7,3,-7,-9,-7,6,3,-3,1,-8,-3,10,-7,5,10,9,-3,9,1,-4,9,8,1,8,-3,2,-5,1,3,1,-8,-3,5,1,-2,-6,-7,4,8,-10,8,-10,-4,3,5,-3,6,-3,9,-1,-1,1,-3,-5,-7,-1,-7,-8,-10,-10,-6,-7,10,5,8,-10,3,8,-8,-7,8,-8,9,-7,6,5,10,-4,5,-2,7,1,-5,6,-2,8,10,-6,-1,-9,8,-1,-7,-1,-6,5,-6,3,-7,-5,-3,10,9,2,9,-1,7,-7,8,-7,2,-8,-2,2,-4,-8,-9,10,-6,-2,-6,-2,-4,9,9,-6,10,1,-9,-1,9,-9,10,8,2,1,-4,10,1,10,7,-3,4,-9,5,7,9,-4,-5,-7,4,-6,-2,-6,8,-5,6,2,-1,4,-10,2,8,10,-8,-10,-4,3,-5,-9,7,-5,-1,4,7,8,2,5,-5,3,2,8,-2,-4,-9,7,8,-10,9,10,5,-3,7,-9,5,-6,7,-4,2,-7,2,9,-8,-6,-7,4,4,1,5,4,1,-8,-3,-9,-10,-9,10,2,-9,6,-7,-7,10,-4,5,-7,-1,5,5,10,8,-10,7,8,-2,-9,-9,-2,4,3,8,-6,-3,1,-4,-7,-10,5,-1,-3,-9,4,1,-4,3,-4,7,8,-2,-8,-1,1,4,-3,8,7,-10,-5,6,6,7,10,2,4,6,10,-8,3,6,-6,1,10,-6,-2,4,-4,10,7,-2,7,2,7,8,-2,7,-9,-1,8,5,2,8,2,-9,-1,7,-9,5,9,-8,-10,-6,3,-7,7,-3,-1,6,-10,-2,6,-6,8,-2,7,-7,5,3,5,9,3,-2,4,8,2,4,9,2,-3,8,4,-4,-1,9,8,9,-1,-6,8,8,5,-10,3,-6,6,-6,-7,3,9,5,9,1,-4,4,10,-4,5,-1,-5,5,-9,6,-3,-6,-1,2,-5,-2,9,-1,-10,-5,-8,-3,1,6,1,8,1,6,6,-1,-2,-10,-1,-9,-5,-5,-1,5,8,-4,3,1,-7,-5,-9,-4,1,2,-6,-10,5,5,6,10,3,-3,7,2,4,-8,6,-2,7,-7,-6,5,4,9,-10,-6,-4,-9,4,6,-9,-1,-8,9,8,10,5,-5,-5,-3,-3,10,-9,-10,-10,-2,-5,-3,-7,-10,-2,-9,8,-8,-8,10,1,1,-8,-2,1,9,-7,9,-9,-9,1,-8,1,6,8,-5,7,-6,8,3,-1,5,7,2,-5,6,8,-9,-9,-2,-10,-5,-4,-1,-8,4,-9,9,-5,3,-1,-7,1,2,10,9,3,-8,5,-1,-6,-4,6,-2,-4,10,-1,8,3,-4,-6,-3,-6,-5,-10,4,1,-10,3,7,-6,7,-4,-9,-7,-9,5,1,3,-2,4,9,-6,-2,3,-6,-4,6,8,-4,10,7,5,9,-3,3,9,-3,-4,-3,4,-6,2,8,-7,6,-6,-5,10,3,4,-3,9,-5,-2,-10,10,7,-7,-4,9,-2,-3,-10,-10,6,-8,-5,4,-1,-10,5,6,4,8,8,7,4,8,3,-6,1,8,2,8,10,-4,-10,6,-2,3,2,1,-2,-2,6,-3,-2,3,-7,-7,2,2,10,7,2,3,2,2,4,10,-9,-6,-8,-7,3,1,-5,-7,-1,-10,-6,9,-8,3,-4,-1,8,8,-10,10,-8,9,4,-2,-2,-9,5,8,10,5,-6,1,-6,1,-3,-9,10,6,-4,8,-1,4,-7,-1,-4,3,5,-6,-10,-6,6,5,1,-9,-2,-1,-5,10,7,-9,8,-1,-3,-3,-1,-7,4,4,-7,-2,-1,-3,8,-10,-7,-6,-10,-9,5,7,10,-5,-10,-2,2,-6,-9,-3,4,-3,-2,-5,7,7,-5,10,-2,2,1,-9,-9,8,-5,4,4,-8,8,1,7,-9,-4,-10,1,-10,-5,7,-5,-2,6,8,5,8,-1,-9,9,-1,-7,1,2,-10,10,2,4,6,2,-2,1,-8,-1,1,7,6,4,9,9,-2,1,-6,8,5,-5,-4,-8,-9,1,2,-3,-1,-6,-10,4,-5,5,-7,3,-2,-10,-7,3,1,5,2,-2,4,5,-4,-7,1,-4,7,-2,-8,-7,3,10,-4,9,-4,10,10,3,4,7,-1,4,8,9,8,-10,8,7,8,9,-7,-9,6,-3,1,-6,8,-2,-7,2,-7,-8,-6,-6,-1,6,7,4,-7,-6,6,-1,-3,1,-4,-7,9,5,-2,-10,9,2,-1,-9,-3,7,6,-4,-2,9,9,-6,-3,4,5,10,-9,-10,-9,9,2,1,-5,-9,9,-3,-5,-7,-2,-6,2,-1,-6,-1,7,-7,3,1,3,5,7,10,-6,10,5,-5,10,10,-6,-1,1,4,-5,4,-4,-2,4,2,-9,8,-8,5,-8,6,-7,8,6,-2,6,1,-4,2,-4,-9,-7,-9,1,-5,-8,-4,-1,-3,-4,-9,2,2,-4,-5,9,1,3,2,-3,-5,-1,6,-9,10,5,-6,1,4,-2,-4,-6,-8,-7,5,9,-1,-8,2,-7,3,-2,-10,8,-10,6,3,9,1,2,-5,5,-3,4,-2,-8,4,3,6,-1,-2,-8,-9,6,4,7,3,7,4,-1,-4,-1,-2,-4,8,3,-2,-6,-10,2,-4,-5,-8,-3,4,1,5,-8,-10,3,10,7,7,-5,-6,2,4,7,10,6,-1,3,3,-3,4,1,2,-7,1,-7,-7,-9,6,4,-5,9,-9,4,-4,5,2,1,3,-2,-8,-3,8,7,-9,10,-3,-2,3,-6,-2,2,-6,6,1,-6,-7,-7,3,10,4,8,1,10,5,-9,-7,-8,8,-4,4,-9,9,7,-9,-5,-7,2,2,-1,8,-3,3,-9,7,-9,3,5,5,5,-1,8,-5,7,2,6,8,-8,1,3,1,3,3,6,-2,-1,-3,-10,-1,8,4,5,3,6,-3,4,-2,-9,-4,10,-8,-8,4,-1,-6,-8,3,4,-9,10,9,7,2,4,-3,-2,7,-3,-10,6,1,8,-1,10,3,3,5,-1,8,-2,2,-1,6,2,8,5,3,-5,-6,-4,4,-10,9,-3,9,-7,1,-9,-2,6,10,1,-5,-8,1,9,-3,-4,2,-9,-5,1,-6,7,-1,10,-4,-7,-7,-9,8,4,9,-4,-5,2,-1,8,-3,-9,-7,10,-10,-10,9,-5,-9,8,5,1,-7,2,7,-7,-6,-9,-5,-6,-3,2,-8,-10,-8,-7,10,-4,2,-7,7,-1,8,8,6,-8,10,10,-1,-7,9,-1,-3,-8,-3,5,-8,-3,-6,-2,4,-1,2,-2,-4,-1,4,-5,-6,-3,-9,9,7,-4,2,5,-5,-10,-2,1,1,10,-1,2,8,-6,-4,-4,8,3,-5,-8,7,-9,-10,4,2,7,-8,3,-4,5,-8,10,1,6,4,-8,1,9,-10,1,6,7,6,-2,-3,-10,-7,4,4,4,3,-8,-3,-4,-1,-7,4,10,4,-10,-8,7,-9,-3,-1,2,1,10,8,-7,10,5,-7,-4,9,-9,2,-4,5,7,-4,-3,8,9,7,6,-9,1,-10,-7,7,-7,10,-4,-9,-4,-8,8,-8,6,4,-3,5,-8,-7,3,1,-6,1,9,-9,-3,-9,6,1,-5,6,-7,-9,5,10,-3,9,-3,9,2,-6,-6,-9,4,-6,4,-6,2,-6,3,-4,8,-6,-8,6,3,-7,6,-3,6,1,1,1,-3,10,-4,4,10,6,5,7,1,-8,10,1,-1,5,8,-5,4,6,-10,1,-10,-7,6,-2,-8,8,-2,-3,9,-4,6,7,5,-8,-4,6,-4,7,-4,9,-9,-9,3,-3,2,9,-9,9,-10,10,6,5,6,3,3,4,-8,5,5,-6,-7,8,-3,-1,-6,4,6,3,3,4,8,10,-10,-9,-4,5,-2,-7,-10,6,9,9,1,-7,-7,-10,10,-3,6,-7,-7,-2,-5,-5,-9,-2,-1,2,-2,6,-2,4,-6,-2,9,3,-2,-6,-5,-4,2,-1,-7,-6,-5,-6,-9,-9,-9,7,2,3,-4,1,-2,4,-2,-8,9,6,6,-1,4,2,-10,-1,-1,-6,-5,-4,5,10,2,-4,2,5,4,5,-5,-1,-5,7,7,1,-4,9,-5,-5,-5,-8,-1,-6,-8,-2,5,-9,-4,-6,-2,2,-4,-5], dtype = "int16")#candidate|11016|(2912,)|const|int16
var_11017 = relay.var("var_11017", dtype = "float32", shape = (840,))#candidate|11017|(840,)|var|float32
call_11015 = relay.TupleGetItem(func_5790_call(relay.reshape(const_11016.astype('int16'), [1456, 2]), relay.reshape(var_11017.astype('float32'), [840,]), ), 1)
call_11018 = relay.TupleGetItem(func_5793_call(relay.reshape(const_11016.astype('int16'), [1456, 2]), relay.reshape(var_11017.astype('float32'), [840,]), ), 1)
func_8465_call = mod.get_global_var('func_8465')
func_8467_call = mutated_mod.get_global_var('func_8467')
call_11045 = relay.TupleGetItem(func_8465_call(), 0)
call_11046 = relay.TupleGetItem(func_8467_call(), 0)
func_9357_call = mod.get_global_var('func_9357')
func_9359_call = mutated_mod.get_global_var('func_9359')
call_11063 = func_9357_call()
call_11064 = func_9357_call()
output = relay.Tuple([bop_11002,call_11015,const_11016,var_11017,call_11045,call_11063,])
output2 = relay.Tuple([bop_11002,call_11018,const_11016,var_11017,call_11046,call_11064,])
func_11073 = relay.Function([var_11000,var_11001,var_11017,], output)
mod['func_11073'] = func_11073
mod = relay.transform.InferType()(mod)
mutated_mod['func_11073'] = func_11073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11073_call = mutated_mod.get_global_var('func_11073')
var_11075 = relay.var("var_11075", dtype = "float32", shape = (8, 4, 6))#candidate|11075|(8, 4, 6)|var|float32
var_11076 = relay.var("var_11076", dtype = "float32", shape = (8, 4, 6))#candidate|11076|(8, 4, 6)|var|float32
var_11077 = relay.var("var_11077", dtype = "float32", shape = (840,))#candidate|11077|(840,)|var|float32
call_11074 = func_11073_call(var_11075,var_11076,var_11077,)
output = call_11074
func_11078 = relay.Function([var_11075,var_11076,var_11077,], output)
mutated_mod['func_11078'] = func_11078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8295_call = mod.get_global_var('func_8295')
func_8296_call = mutated_mod.get_global_var('func_8296')
call_11162 = relay.TupleGetItem(func_8295_call(), 0)
call_11163 = relay.TupleGetItem(func_8296_call(), 0)
output = call_11162
output2 = call_11163
func_11187 = relay.Function([], output)
mod['func_11187'] = func_11187
mod = relay.transform.InferType()(mod)
output = func_11187()
func_11188 = relay.Function([], output)
mutated_mod['func_11188'] = func_11188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mod.get_global_var('func_4689')
func_4690_call = mutated_mod.get_global_var('func_4690')
call_11209 = relay.TupleGetItem(func_4689_call(), 1)
call_11210 = relay.TupleGetItem(func_4690_call(), 1)
output = relay.Tuple([call_11209,])
output2 = relay.Tuple([call_11210,])
func_11211 = relay.Function([], output)
mod['func_11211'] = func_11211
mod = relay.transform.InferType()(mod)
mutated_mod['func_11211'] = func_11211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11211_call = mutated_mod.get_global_var('func_11211')
call_11212 = func_11211_call()
output = call_11212
func_11213 = relay.Function([], output)
mutated_mod['func_11213'] = func_11213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6950_call = mod.get_global_var('func_6950')
func_6951_call = mutated_mod.get_global_var('func_6951')
call_11225 = relay.TupleGetItem(func_6950_call(), 1)
call_11226 = relay.TupleGetItem(func_6951_call(), 1)
output = call_11225
output2 = call_11226
func_11229 = relay.Function([], output)
mod['func_11229'] = func_11229
mod = relay.transform.InferType()(mod)
output = func_11229()
func_11230 = relay.Function([], output)
mutated_mod['func_11230'] = func_11230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8823_call = mod.get_global_var('func_8823')
func_8824_call = mutated_mod.get_global_var('func_8824')
call_11275 = relay.TupleGetItem(func_8823_call(), 1)
call_11276 = relay.TupleGetItem(func_8824_call(), 1)
output = call_11275
output2 = call_11276
func_11293 = relay.Function([], output)
mod['func_11293'] = func_11293
mod = relay.transform.InferType()(mod)
mutated_mod['func_11293'] = func_11293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11293_call = mutated_mod.get_global_var('func_11293')
call_11294 = func_11293_call()
output = call_11294
func_11295 = relay.Function([], output)
mutated_mod['func_11295'] = func_11295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11293_call = mod.get_global_var('func_11293')
func_11295_call = mutated_mod.get_global_var('func_11295')
call_11382 = func_11293_call()
call_11383 = func_11293_call()
output = call_11382
output2 = call_11383
func_11386 = relay.Function([], output)
mod['func_11386'] = func_11386
mod = relay.transform.InferType()(mod)
mutated_mod['func_11386'] = func_11386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11386_call = mutated_mod.get_global_var('func_11386')
call_11387 = func_11386_call()
output = call_11387
func_11388 = relay.Function([], output)
mutated_mod['func_11388'] = func_11388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9919_call = mod.get_global_var('func_9919')
func_9920_call = mutated_mod.get_global_var('func_9920')
call_11415 = relay.TupleGetItem(func_9919_call(), 0)
call_11416 = relay.TupleGetItem(func_9920_call(), 0)
output = relay.Tuple([call_11415,])
output2 = relay.Tuple([call_11416,])
func_11439 = relay.Function([], output)
mod['func_11439'] = func_11439
mod = relay.transform.InferType()(mod)
output = func_11439()
func_11440 = relay.Function([], output)
mutated_mod['func_11440'] = func_11440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5489_call = mod.get_global_var('func_5489')
func_5490_call = mutated_mod.get_global_var('func_5490')
call_11501 = relay.TupleGetItem(func_5489_call(), 1)
call_11502 = relay.TupleGetItem(func_5490_call(), 1)
output = call_11501
output2 = call_11502
func_11514 = relay.Function([], output)
mod['func_11514'] = func_11514
mod = relay.transform.InferType()(mod)
mutated_mod['func_11514'] = func_11514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11514_call = mutated_mod.get_global_var('func_11514')
call_11515 = func_11514_call()
output = call_11515
func_11516 = relay.Function([], output)
mutated_mod['func_11516'] = func_11516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5660_call = mod.get_global_var('func_5660')
func_5662_call = mutated_mod.get_global_var('func_5662')
call_11614 = relay.TupleGetItem(func_5660_call(), 0)
call_11615 = relay.TupleGetItem(func_5662_call(), 0)
func_5294_call = mod.get_global_var('func_5294')
func_5297_call = mutated_mod.get_global_var('func_5297')
var_11620 = relay.var("var_11620", dtype = "int16", shape = (2, 1456))#candidate|11620|(2, 1456)|var|int16
call_11619 = relay.TupleGetItem(func_5294_call(relay.reshape(var_11620.astype('int16'), [2912,])), 2)
call_11621 = relay.TupleGetItem(func_5297_call(relay.reshape(var_11620.astype('int16'), [2912,])), 2)
output = relay.Tuple([call_11614,call_11619,var_11620,])
output2 = relay.Tuple([call_11615,call_11621,var_11620,])
func_11637 = relay.Function([var_11620,], output)
mod['func_11637'] = func_11637
mod = relay.transform.InferType()(mod)
var_11638 = relay.var("var_11638", dtype = "int16", shape = (2, 1456))#candidate|11638|(2, 1456)|var|int16
output = func_11637(var_11638)
func_11639 = relay.Function([var_11638], output)
mutated_mod['func_11639'] = func_11639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6898_call = mod.get_global_var('func_6898')
func_6900_call = mutated_mod.get_global_var('func_6900')
call_11641 = relay.TupleGetItem(func_6898_call(), 0)
call_11642 = relay.TupleGetItem(func_6900_call(), 0)
func_8295_call = mod.get_global_var('func_8295')
func_8296_call = mutated_mod.get_global_var('func_8296')
call_11663 = relay.TupleGetItem(func_8295_call(), 0)
call_11664 = relay.TupleGetItem(func_8296_call(), 0)
func_3776_call = mod.get_global_var('func_3776')
func_3778_call = mutated_mod.get_global_var('func_3778')
call_11675 = relay.TupleGetItem(func_3776_call(), 0)
call_11676 = relay.TupleGetItem(func_3778_call(), 0)
output = relay.Tuple([call_11641,call_11663,call_11675,])
output2 = relay.Tuple([call_11642,call_11664,call_11676,])
func_11696 = relay.Function([], output)
mod['func_11696'] = func_11696
mod = relay.transform.InferType()(mod)
mutated_mod['func_11696'] = func_11696
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11696_call = mutated_mod.get_global_var('func_11696')
call_11697 = func_11696_call()
output = call_11697
func_11698 = relay.Function([], output)
mutated_mod['func_11698'] = func_11698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6228_call = mod.get_global_var('func_6228')
func_6230_call = mutated_mod.get_global_var('func_6230')
call_11779 = relay.TupleGetItem(func_6228_call(), 1)
call_11780 = relay.TupleGetItem(func_6230_call(), 1)
output = call_11779
output2 = call_11780
func_11784 = relay.Function([], output)
mod['func_11784'] = func_11784
mod = relay.transform.InferType()(mod)
output = func_11784()
func_11785 = relay.Function([], output)
mutated_mod['func_11785'] = func_11785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8857_call = mod.get_global_var('func_8857')
func_8858_call = mutated_mod.get_global_var('func_8858')
call_11820 = func_8857_call()
call_11821 = func_8857_call()
func_6664_call = mod.get_global_var('func_6664')
func_6665_call = mutated_mod.get_global_var('func_6665')
call_11854 = func_6664_call()
call_11855 = func_6664_call()
func_9272_call = mod.get_global_var('func_9272')
func_9273_call = mutated_mod.get_global_var('func_9273')
call_11859 = relay.TupleGetItem(func_9272_call(), 2)
call_11860 = relay.TupleGetItem(func_9273_call(), 2)
func_9335_call = mod.get_global_var('func_9335')
func_9337_call = mutated_mod.get_global_var('func_9337')
call_11863 = relay.TupleGetItem(func_9335_call(), 0)
call_11864 = relay.TupleGetItem(func_9337_call(), 0)
output = relay.Tuple([call_11820,call_11854,call_11859,call_11863,])
output2 = relay.Tuple([call_11821,call_11855,call_11860,call_11864,])
func_11867 = relay.Function([], output)
mod['func_11867'] = func_11867
mod = relay.transform.InferType()(mod)
mutated_mod['func_11867'] = func_11867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11867_call = mutated_mod.get_global_var('func_11867')
call_11868 = func_11867_call()
output = call_11868
func_11869 = relay.Function([], output)
mutated_mod['func_11869'] = func_11869
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11880 = relay.var("var_11880", dtype = "uint16", shape = (11, 16, 8))#candidate|11880|(11, 16, 8)|var|uint16
var_11881 = relay.var("var_11881", dtype = "uint16", shape = (11, 16, 8))#candidate|11881|(11, 16, 8)|var|uint16
bop_11882 = relay.equal(var_11880.astype('bool'), relay.reshape(var_11881.astype('bool'), relay.shape_of(var_11880))) # shape=(11, 16, 8)
uop_11886 = relay.sqrt(var_11880.astype('float64')) # shape=(11, 16, 8)
output = relay.Tuple([bop_11882,uop_11886,])
output2 = relay.Tuple([bop_11882,uop_11886,])
func_11892 = relay.Function([var_11880,var_11881,], output)
mod['func_11892'] = func_11892
mod = relay.transform.InferType()(mod)
var_11893 = relay.var("var_11893", dtype = "uint16", shape = (11, 16, 8))#candidate|11893|(11, 16, 8)|var|uint16
var_11894 = relay.var("var_11894", dtype = "uint16", shape = (11, 16, 8))#candidate|11894|(11, 16, 8)|var|uint16
output = func_11892(var_11893,var_11894,)
func_11895 = relay.Function([var_11893,var_11894,], output)
mutated_mod['func_11895'] = func_11895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9357_call = mod.get_global_var('func_9357')
func_9359_call = mutated_mod.get_global_var('func_9359')
call_11900 = func_9357_call()
call_11901 = func_9357_call()
func_8407_call = mod.get_global_var('func_8407')
func_8409_call = mutated_mod.get_global_var('func_8409')
call_11912 = relay.TupleGetItem(func_8407_call(), 0)
call_11913 = relay.TupleGetItem(func_8409_call(), 0)
var_11915 = relay.var("var_11915", dtype = "float64", shape = (48, 2))#candidate|11915|(48, 2)|var|float64
bop_11916 = relay.less_equal(call_11912.astype('bool'), relay.reshape(var_11915.astype('bool'), relay.shape_of(call_11912))) # shape=(48, 2)
bop_11919 = relay.less_equal(call_11913.astype('bool'), relay.reshape(var_11915.astype('bool'), relay.shape_of(call_11913))) # shape=(48, 2)
bop_11923 = relay.right_shift(var_11915.astype('int32'), relay.reshape(call_11912.astype('int32'), relay.shape_of(var_11915))) # shape=(48, 2)
bop_11926 = relay.right_shift(var_11915.astype('int32'), relay.reshape(call_11913.astype('int32'), relay.shape_of(var_11915))) # shape=(48, 2)
func_4301_call = mod.get_global_var('func_4301')
func_4304_call = mutated_mod.get_global_var('func_4304')
const_11946 = relay.const(3, dtype = "int32")#candidate|11946|()|const|int32
call_11945 = relay.TupleGetItem(func_4301_call(relay.reshape(const_11946.astype('int32'), [])), 0)
call_11947 = relay.TupleGetItem(func_4304_call(relay.reshape(const_11946.astype('int32'), [])), 0)
uop_11976 = relay.log(bop_11923.astype('float64')) # shape=(48, 2)
uop_11978 = relay.log(bop_11926.astype('float64')) # shape=(48, 2)
func_11696_call = mod.get_global_var('func_11696')
func_11698_call = mutated_mod.get_global_var('func_11698')
call_11987 = relay.TupleGetItem(func_11696_call(), 1)
call_11988 = relay.TupleGetItem(func_11698_call(), 1)
output = relay.Tuple([call_11900,bop_11916,call_11945,const_11946,uop_11976,call_11987,])
output2 = relay.Tuple([call_11901,bop_11919,call_11947,const_11946,uop_11978,call_11988,])
func_11995 = relay.Function([var_11915,], output)
mod['func_11995'] = func_11995
mod = relay.transform.InferType()(mod)
var_11996 = relay.var("var_11996", dtype = "float64", shape = (48, 2))#candidate|11996|(48, 2)|var|float64
output = func_11995(var_11996)
func_11997 = relay.Function([var_11996], output)
mutated_mod['func_11997'] = func_11997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mod.get_global_var('func_4689')
func_4690_call = mutated_mod.get_global_var('func_4690')
call_11999 = relay.TupleGetItem(func_4689_call(), 2)
call_12000 = relay.TupleGetItem(func_4690_call(), 2)
uop_12007 = relay.acos(call_11999.astype('float32')) # shape=(44,)
uop_12009 = relay.acos(call_12000.astype('float32')) # shape=(44,)
output = relay.Tuple([uop_12007,])
output2 = relay.Tuple([uop_12009,])
func_12016 = relay.Function([], output)
mod['func_12016'] = func_12016
mod = relay.transform.InferType()(mod)
mutated_mod['func_12016'] = func_12016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12016_call = mutated_mod.get_global_var('func_12016')
call_12017 = func_12016_call()
output = call_12017
func_12018 = relay.Function([], output)
mutated_mod['func_12018'] = func_12018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7272_call = mod.get_global_var('func_7272')
func_7273_call = mutated_mod.get_global_var('func_7273')
call_12019 = relay.TupleGetItem(func_7272_call(), 2)
call_12020 = relay.TupleGetItem(func_7273_call(), 2)
func_8611_call = mod.get_global_var('func_8611')
func_8613_call = mutated_mod.get_global_var('func_8613')
call_12030 = relay.TupleGetItem(func_8611_call(), 0)
call_12031 = relay.TupleGetItem(func_8613_call(), 0)
output = relay.Tuple([call_12019,call_12030,])
output2 = relay.Tuple([call_12020,call_12031,])
func_12037 = relay.Function([], output)
mod['func_12037'] = func_12037
mod = relay.transform.InferType()(mod)
output = func_12037()
func_12038 = relay.Function([], output)
mutated_mod['func_12038'] = func_12038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12016_call = mod.get_global_var('func_12016')
func_12018_call = mutated_mod.get_global_var('func_12018')
call_12068 = relay.TupleGetItem(func_12016_call(), 0)
call_12069 = relay.TupleGetItem(func_12018_call(), 0)
func_11784_call = mod.get_global_var('func_11784')
func_11785_call = mutated_mod.get_global_var('func_11785')
call_12072 = func_11784_call()
call_12073 = func_11784_call()
func_7894_call = mod.get_global_var('func_7894')
func_7897_call = mutated_mod.get_global_var('func_7897')
var_12088 = relay.var("var_12088", dtype = "int32", shape = (280,))#candidate|12088|(280,)|var|int32
call_12087 = relay.TupleGetItem(func_7894_call(relay.reshape(var_12088.astype('int32'), [280,])), 6)
call_12089 = relay.TupleGetItem(func_7897_call(relay.reshape(var_12088.astype('int32'), [280,])), 6)
output = relay.Tuple([call_12068,call_12072,call_12087,var_12088,])
output2 = relay.Tuple([call_12069,call_12073,call_12089,var_12088,])
func_12103 = relay.Function([var_12088,], output)
mod['func_12103'] = func_12103
mod = relay.transform.InferType()(mod)
mutated_mod['func_12103'] = func_12103
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12104 = relay.var("var_12104", dtype = "int32", shape = (280,))#candidate|12104|(280,)|var|int32
func_12103_call = mutated_mod.get_global_var('func_12103')
call_12105 = func_12103_call(var_12104)
output = call_12105
func_12106 = relay.Function([var_12104], output)
mutated_mod['func_12106'] = func_12106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5641_call = mod.get_global_var('func_5641')
func_5643_call = mutated_mod.get_global_var('func_5643')
call_12142 = func_5641_call()
call_12143 = func_5641_call()
func_8138_call = mod.get_global_var('func_8138')
func_8139_call = mutated_mod.get_global_var('func_8139')
call_12156 = relay.TupleGetItem(func_8138_call(), 0)
call_12157 = relay.TupleGetItem(func_8139_call(), 0)
func_8052_call = mod.get_global_var('func_8052')
func_8053_call = mutated_mod.get_global_var('func_8053')
call_12164 = relay.TupleGetItem(func_8052_call(), 0)
call_12165 = relay.TupleGetItem(func_8053_call(), 0)
output = relay.Tuple([call_12142,call_12156,call_12164,])
output2 = relay.Tuple([call_12143,call_12157,call_12165,])
func_12166 = relay.Function([], output)
mod['func_12166'] = func_12166
mod = relay.transform.InferType()(mod)
output = func_12166()
func_12167 = relay.Function([], output)
mutated_mod['func_12167'] = func_12167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5618_call = mod.get_global_var('func_5618')
func_5620_call = mutated_mod.get_global_var('func_5620')
call_12173 = func_5618_call()
call_12174 = func_5618_call()
func_9760_call = mod.get_global_var('func_9760')
func_9761_call = mutated_mod.get_global_var('func_9761')
call_12176 = relay.TupleGetItem(func_9760_call(), 0)
call_12177 = relay.TupleGetItem(func_9761_call(), 0)
func_4593_call = mod.get_global_var('func_4593')
func_4596_call = mutated_mod.get_global_var('func_4596')
var_12183 = relay.var("var_12183", dtype = "int16", shape = (2912,))#candidate|12183|(2912,)|var|int16
call_12182 = relay.TupleGetItem(func_4593_call(relay.reshape(var_12183.astype('int16'), [2912,])), 1)
call_12184 = relay.TupleGetItem(func_4596_call(relay.reshape(var_12183.astype('int16'), [2912,])), 1)
output = relay.Tuple([call_12173,call_12176,call_12182,var_12183,])
output2 = relay.Tuple([call_12174,call_12177,call_12184,var_12183,])
func_12189 = relay.Function([var_12183,], output)
mod['func_12189'] = func_12189
mod = relay.transform.InferType()(mod)
mutated_mod['func_12189'] = func_12189
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12190 = relay.var("var_12190", dtype = "int16", shape = (2912,))#candidate|12190|(2912,)|var|int16
func_12189_call = mutated_mod.get_global_var('func_12189')
call_12191 = func_12189_call(var_12190)
output = call_12191
func_12192 = relay.Function([var_12190], output)
mutated_mod['func_12192'] = func_12192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8052_call = mod.get_global_var('func_8052')
func_8053_call = mutated_mod.get_global_var('func_8053')
call_12196 = relay.TupleGetItem(func_8052_call(), 0)
call_12197 = relay.TupleGetItem(func_8053_call(), 0)
func_7945_call = mod.get_global_var('func_7945')
func_7949_call = mutated_mod.get_global_var('func_7949')
var_12220 = relay.var("var_12220", dtype = "float32", shape = (495,))#candidate|12220|(495,)|var|float32
call_12219 = relay.TupleGetItem(func_7945_call(relay.reshape(var_12220.astype('float32'), [5, 9, 11]), relay.reshape(var_12220.astype('float32'), [5, 9, 11]), relay.reshape(call_12196.astype('float32'), [1890, 1]), ), 1)
call_12221 = relay.TupleGetItem(func_7949_call(relay.reshape(var_12220.astype('float32'), [5, 9, 11]), relay.reshape(var_12220.astype('float32'), [5, 9, 11]), relay.reshape(call_12196.astype('float32'), [1890, 1]), ), 1)
func_9335_call = mod.get_global_var('func_9335')
func_9337_call = mutated_mod.get_global_var('func_9337')
call_12223 = relay.TupleGetItem(func_9335_call(), 0)
call_12224 = relay.TupleGetItem(func_9337_call(), 0)
func_11293_call = mod.get_global_var('func_11293')
func_11295_call = mutated_mod.get_global_var('func_11295')
call_12228 = func_11293_call()
call_12229 = func_11293_call()
var_12232 = relay.var("var_12232", dtype = "float32", shape = (1890, 16))#candidate|12232|(1890, 16)|var|float32
bop_12233 = relay.minimum(call_12219.astype('float64'), var_12232.astype('float64')) # shape=(1890, 16)
bop_12236 = relay.minimum(call_12221.astype('float64'), var_12232.astype('float64')) # shape=(1890, 16)
func_4620_call = mod.get_global_var('func_4620')
func_4621_call = mutated_mod.get_global_var('func_4621')
call_12239 = func_4620_call()
call_12240 = func_4620_call()
func_10103_call = mod.get_global_var('func_10103')
func_10105_call = mutated_mod.get_global_var('func_10105')
call_12247 = relay.TupleGetItem(func_10103_call(), 0)
call_12248 = relay.TupleGetItem(func_10105_call(), 0)
func_9467_call = mod.get_global_var('func_9467')
func_9469_call = mutated_mod.get_global_var('func_9469')
call_12252 = func_9467_call()
call_12253 = func_9467_call()
output = relay.Tuple([call_12196,var_12220,call_12223,call_12228,bop_12233,call_12239,call_12247,call_12252,])
output2 = relay.Tuple([call_12197,var_12220,call_12224,call_12229,bop_12236,call_12240,call_12248,call_12253,])
func_12257 = relay.Function([var_12220,var_12232,], output)
mod['func_12257'] = func_12257
mod = relay.transform.InferType()(mod)
var_12258 = relay.var("var_12258", dtype = "float32", shape = (495,))#candidate|12258|(495,)|var|float32
var_12259 = relay.var("var_12259", dtype = "float32", shape = (1890, 16))#candidate|12259|(1890, 16)|var|float32
output = func_12257(var_12258,var_12259,)
func_12260 = relay.Function([var_12258,var_12259,], output)
mutated_mod['func_12260'] = func_12260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5941_call = mod.get_global_var('func_5941')
func_5943_call = mutated_mod.get_global_var('func_5943')
call_12303 = func_5941_call()
call_12304 = func_5941_call()
output = call_12303
output2 = call_12304
func_12338 = relay.Function([], output)
mod['func_12338'] = func_12338
mod = relay.transform.InferType()(mod)
output = func_12338()
func_12339 = relay.Function([], output)
mutated_mod['func_12339'] = func_12339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10358_call = mod.get_global_var('func_10358')
func_10360_call = mutated_mod.get_global_var('func_10360')
call_12373 = relay.TupleGetItem(func_10358_call(), 0)
call_12374 = relay.TupleGetItem(func_10360_call(), 0)
output = call_12373
output2 = call_12374
func_12380 = relay.Function([], output)
mod['func_12380'] = func_12380
mod = relay.transform.InferType()(mod)
output = func_12380()
func_12381 = relay.Function([], output)
mutated_mod['func_12381'] = func_12381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10272_call = mod.get_global_var('func_10272')
func_10274_call = mutated_mod.get_global_var('func_10274')
call_12463 = relay.TupleGetItem(func_10272_call(), 0)
call_12464 = relay.TupleGetItem(func_10274_call(), 0)
func_10797_call = mod.get_global_var('func_10797')
func_10798_call = mutated_mod.get_global_var('func_10798')
call_12471 = relay.TupleGetItem(func_10797_call(), 0)
call_12472 = relay.TupleGetItem(func_10798_call(), 0)
output = relay.Tuple([call_12463,call_12471,])
output2 = relay.Tuple([call_12464,call_12472,])
func_12502 = relay.Function([], output)
mod['func_12502'] = func_12502
mod = relay.transform.InferType()(mod)
output = func_12502()
func_12503 = relay.Function([], output)
mutated_mod['func_12503'] = func_12503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11293_call = mod.get_global_var('func_11293')
func_11295_call = mutated_mod.get_global_var('func_11295')
call_12507 = func_11293_call()
call_12508 = func_11293_call()
func_12502_call = mod.get_global_var('func_12502')
func_12503_call = mutated_mod.get_global_var('func_12503')
call_12522 = relay.TupleGetItem(func_12502_call(), 1)
call_12523 = relay.TupleGetItem(func_12503_call(), 1)
output = relay.Tuple([call_12507,call_12522,])
output2 = relay.Tuple([call_12508,call_12523,])
func_12530 = relay.Function([], output)
mod['func_12530'] = func_12530
mod = relay.transform.InferType()(mod)
mutated_mod['func_12530'] = func_12530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12530_call = mutated_mod.get_global_var('func_12530')
call_12531 = func_12530_call()
output = call_12531
func_12532 = relay.Function([], output)
mutated_mod['func_12532'] = func_12532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11439_call = mod.get_global_var('func_11439')
func_11440_call = mutated_mod.get_global_var('func_11440')
call_12580 = relay.TupleGetItem(func_11439_call(), 0)
call_12581 = relay.TupleGetItem(func_11440_call(), 0)
func_7739_call = mod.get_global_var('func_7739')
func_7742_call = mutated_mod.get_global_var('func_7742')
const_12590 = relay.const([0.010276,1.718182,-5.628957,-3.400086,-8.245560,-7.214397,-7.798872,9.618072,9.912349,-0.746978,-4.200403,5.570596,-8.238456,-7.612881,-2.845583,3.539162,-9.359033,-9.189729,-0.053643,-8.105602,2.273845,4.731542,0.499596,-6.000018,3.291082,0.495074,1.571572,7.902871,1.980435,9.605424,5.679593,0.870813,3.667491,-1.514077,-3.985002,3.100400,5.515305,1.137850,2.579633,-1.248348,-0.836748,6.314964,-0.428121,0.527611,-4.735169,-4.147683,7.917563,7.658800,9.358822,-1.653929,-9.808753,9.705312,1.497923,-9.235614,4.357594,8.324339,6.254425,9.863833,8.793491,1.425178,7.719298,1.750615,4.230582,-7.415420,-2.023201,-5.965537,-2.716907,4.441154,6.044093,-5.457320,-0.243801,-9.409764,-3.733959,7.181395,7.369897,9.135796,-3.214890,0.341602,-4.630615,-6.852548,4.721554,5.195734,6.518310,5.030934,3.709629,2.112935,3.863839,3.298860,8.437675,6.964998,6.250074,4.032248,5.326307,9.235261,-4.009347,-1.917831,-7.276834,9.670492,-9.126281,-6.695597,1.805114,1.560347,-0.008172,-2.024564,-4.484326,-4.252980,1.773768,2.961627,-5.140620,-8.503368,0.883198,-8.057480,-5.196925,4.680276,-5.975914,-6.801415,4.202429,-8.405788,-1.794078,9.247932,-3.071594,-2.114191,6.693868,-6.513011,-0.250242,6.271200,-2.908771,-3.751070,1.438986,1.789176,9.104809,9.127564,-2.977730,-7.176625,6.622880,1.229577,7.980417,5.911532,9.336268,7.232594,-8.530933,5.371175,-1.518974,3.354999,6.411007,-3.350266,0.821753,5.880418,6.059503,-9.117889,7.097155,4.030261,-1.447762,-1.970166,-1.186930,2.525144,-1.767895,9.067171,-0.959819,-8.379363,-0.594338,9.781175,2.646326,7.063433,-5.487924,5.292722,3.581708,8.905370], dtype = "float32")#candidate|12590|(168,)|const|float32
call_12589 = relay.TupleGetItem(func_7739_call(relay.reshape(const_12590.astype('float32'), [168,])), 2)
call_12591 = relay.TupleGetItem(func_7742_call(relay.reshape(const_12590.astype('float32'), [168,])), 2)
func_7657_call = mod.get_global_var('func_7657')
func_7659_call = mutated_mod.get_global_var('func_7659')
var_12595 = relay.var("var_12595", dtype = "float64", shape = (225,))#candidate|12595|(225,)|var|float64
call_12594 = relay.TupleGetItem(func_7657_call(relay.reshape(var_12595.astype('float64'), [15, 1, 15])), 1)
call_12596 = relay.TupleGetItem(func_7659_call(relay.reshape(var_12595.astype('float64'), [15, 1, 15])), 1)
func_10272_call = mod.get_global_var('func_10272')
func_10274_call = mutated_mod.get_global_var('func_10274')
call_12611 = relay.TupleGetItem(func_10272_call(), 0)
call_12612 = relay.TupleGetItem(func_10274_call(), 0)
func_10206_call = mod.get_global_var('func_10206')
func_10208_call = mutated_mod.get_global_var('func_10208')
call_12627 = relay.TupleGetItem(func_10206_call(), 2)
call_12628 = relay.TupleGetItem(func_10208_call(), 2)
func_6898_call = mod.get_global_var('func_6898')
func_6900_call = mutated_mod.get_global_var('func_6900')
call_12635 = relay.TupleGetItem(func_6898_call(), 0)
call_12636 = relay.TupleGetItem(func_6900_call(), 0)
func_3703_call = mod.get_global_var('func_3703')
func_3704_call = mutated_mod.get_global_var('func_3704')
call_12645 = relay.TupleGetItem(func_3703_call(), 0)
call_12646 = relay.TupleGetItem(func_3704_call(), 0)
uop_12658 = relay.acos(call_12611.astype('float32')) # shape=(1, 11, 4)
uop_12660 = relay.acos(call_12612.astype('float32')) # shape=(1, 11, 4)
output = relay.Tuple([call_12580,call_12589,const_12590,call_12594,var_12595,call_12627,call_12635,call_12645,uop_12658,])
output2 = relay.Tuple([call_12581,call_12591,const_12590,call_12596,var_12595,call_12628,call_12636,call_12646,uop_12660,])
func_12665 = relay.Function([var_12595,], output)
mod['func_12665'] = func_12665
mod = relay.transform.InferType()(mod)
mutated_mod['func_12665'] = func_12665
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12666 = relay.var("var_12666", dtype = "float64", shape = (225,))#candidate|12666|(225,)|var|float64
func_12665_call = mutated_mod.get_global_var('func_12665')
call_12667 = func_12665_call(var_12666)
output = call_12667
func_12668 = relay.Function([var_12666], output)
mutated_mod['func_12668'] = func_12668
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12730 = relay.var("var_12730", dtype = "float32", shape = (14, 16, 12))#candidate|12730|(14, 16, 12)|var|float32
uop_12731 = relay.sinh(var_12730.astype('float32')) # shape=(14, 16, 12)
bop_12733 = relay.floor_mod(uop_12731.astype('float32'), relay.reshape(var_12730.astype('float32'), relay.shape_of(uop_12731))) # shape=(14, 16, 12)
output = bop_12733
output2 = bop_12733
func_12736 = relay.Function([var_12730,], output)
mod['func_12736'] = func_12736
mod = relay.transform.InferType()(mod)
mutated_mod['func_12736'] = func_12736
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12737 = relay.var("var_12737", dtype = "float32", shape = (14, 16, 12))#candidate|12737|(14, 16, 12)|var|float32
func_12736_call = mutated_mod.get_global_var('func_12736')
call_12738 = func_12736_call(var_12737)
output = call_12738
func_12739 = relay.Function([var_12737], output)
mutated_mod['func_12739'] = func_12739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8319_call = mod.get_global_var('func_8319')
func_8320_call = mutated_mod.get_global_var('func_8320')
call_12808 = func_8319_call()
call_12809 = func_8319_call()
output = call_12808
output2 = call_12809
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
func_10568_call = mod.get_global_var('func_10568')
func_10570_call = mutated_mod.get_global_var('func_10570')
call_12824 = relay.TupleGetItem(func_10568_call(), 1)
call_12825 = relay.TupleGetItem(func_10570_call(), 1)
output = call_12824
output2 = call_12825
func_12833 = relay.Function([], output)
mod['func_12833'] = func_12833
mod = relay.transform.InferType()(mod)
output = func_12833()
func_12834 = relay.Function([], output)
mutated_mod['func_12834'] = func_12834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9357_call = mod.get_global_var('func_9357')
func_9359_call = mutated_mod.get_global_var('func_9359')
call_12920 = func_9357_call()
call_12921 = func_9357_call()
func_4949_call = mod.get_global_var('func_4949')
func_4951_call = mutated_mod.get_global_var('func_4951')
call_12922 = func_4949_call()
call_12923 = func_4949_call()
func_8633_call = mod.get_global_var('func_8633')
func_8634_call = mutated_mod.get_global_var('func_8634')
call_12928 = relay.TupleGetItem(func_8633_call(), 0)
call_12929 = relay.TupleGetItem(func_8634_call(), 0)
func_9272_call = mod.get_global_var('func_9272')
func_9273_call = mutated_mod.get_global_var('func_9273')
call_12933 = relay.TupleGetItem(func_9272_call(), 1)
call_12934 = relay.TupleGetItem(func_9273_call(), 1)
output = relay.Tuple([call_12920,call_12922,call_12928,call_12933,])
output2 = relay.Tuple([call_12921,call_12923,call_12929,call_12934,])
func_12936 = relay.Function([], output)
mod['func_12936'] = func_12936
mod = relay.transform.InferType()(mod)
output = func_12936()
func_12937 = relay.Function([], output)
mutated_mod['func_12937'] = func_12937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10568_call = mod.get_global_var('func_10568')
func_10570_call = mutated_mod.get_global_var('func_10570')
call_12967 = relay.TupleGetItem(func_10568_call(), 0)
call_12968 = relay.TupleGetItem(func_10570_call(), 0)
func_11784_call = mod.get_global_var('func_11784')
func_11785_call = mutated_mod.get_global_var('func_11785')
call_12977 = func_11784_call()
call_12978 = func_11784_call()
func_2337_call = mod.get_global_var('func_2337')
func_2340_call = mutated_mod.get_global_var('func_2340')
const_12986 = relay.const(4, dtype = "uint32")#candidate|12986|()|const|uint32
var_12987 = relay.var("var_12987", dtype = "uint32", shape = (15,))#candidate|12987|(15,)|var|uint32
call_12985 = func_2337_call(relay.reshape(const_12986.astype('uint32'), []), relay.reshape(var_12987.astype('uint32'), [1, 1, 15]), )
call_12988 = func_2337_call(relay.reshape(const_12986.astype('uint32'), []), relay.reshape(var_12987.astype('uint32'), [1, 1, 15]), )
output = relay.Tuple([call_12967,call_12977,call_12985,const_12986,var_12987,])
output2 = relay.Tuple([call_12968,call_12978,call_12988,const_12986,var_12987,])
func_12994 = relay.Function([var_12987,], output)
mod['func_12994'] = func_12994
mod = relay.transform.InferType()(mod)
mutated_mod['func_12994'] = func_12994
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12995 = relay.var("var_12995", dtype = "uint32", shape = (15,))#candidate|12995|(15,)|var|uint32
func_12994_call = mutated_mod.get_global_var('func_12994')
call_12996 = func_12994_call(var_12995)
output = call_12996
func_12997 = relay.Function([var_12995], output)
mutated_mod['func_12997'] = func_12997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6950_call = mod.get_global_var('func_6950')
func_6951_call = mutated_mod.get_global_var('func_6951')
call_13034 = relay.TupleGetItem(func_6950_call(), 1)
call_13035 = relay.TupleGetItem(func_6951_call(), 1)
func_8891_call = mod.get_global_var('func_8891')
func_8892_call = mutated_mod.get_global_var('func_8892')
call_13046 = func_8891_call()
call_13047 = func_8891_call()
output = relay.Tuple([call_13034,call_13046,])
output2 = relay.Tuple([call_13035,call_13047,])
func_13053 = relay.Function([], output)
mod['func_13053'] = func_13053
mod = relay.transform.InferType()(mod)
mutated_mod['func_13053'] = func_13053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13053_call = mutated_mod.get_global_var('func_13053')
call_13054 = func_13053_call()
output = call_13054
func_13055 = relay.Function([], output)
mutated_mod['func_13055'] = func_13055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11187_call = mod.get_global_var('func_11187')
func_11188_call = mutated_mod.get_global_var('func_11188')
call_13115 = func_11187_call()
call_13116 = func_11187_call()
output = relay.Tuple([call_13115,])
output2 = relay.Tuple([call_13116,])
func_13156 = relay.Function([], output)
mod['func_13156'] = func_13156
mod = relay.transform.InferType()(mod)
mutated_mod['func_13156'] = func_13156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13156_call = mutated_mod.get_global_var('func_13156')
call_13157 = func_13156_call()
output = call_13157
func_13158 = relay.Function([], output)
mutated_mod['func_13158'] = func_13158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9774_call = mod.get_global_var('func_9774')
func_9776_call = mutated_mod.get_global_var('func_9776')
call_13169 = func_9774_call()
call_13170 = func_9774_call()
func_9641_call = mod.get_global_var('func_9641')
func_9642_call = mutated_mod.get_global_var('func_9642')
call_13174 = relay.TupleGetItem(func_9641_call(), 0)
call_13175 = relay.TupleGetItem(func_9642_call(), 0)
output = relay.Tuple([call_13169,call_13174,])
output2 = relay.Tuple([call_13170,call_13175,])
func_13200 = relay.Function([], output)
mod['func_13200'] = func_13200
mod = relay.transform.InferType()(mod)
output = func_13200()
func_13201 = relay.Function([], output)
mutated_mod['func_13201'] = func_13201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8714_call = mod.get_global_var('func_8714')
func_8716_call = mutated_mod.get_global_var('func_8716')
call_13225 = relay.TupleGetItem(func_8714_call(), 1)
call_13226 = relay.TupleGetItem(func_8716_call(), 1)
output = call_13225
output2 = call_13226
func_13227 = relay.Function([], output)
mod['func_13227'] = func_13227
mod = relay.transform.InferType()(mod)
mutated_mod['func_13227'] = func_13227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13227_call = mutated_mod.get_global_var('func_13227')
call_13228 = func_13227_call()
output = call_13228
func_13229 = relay.Function([], output)
mutated_mod['func_13229'] = func_13229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9123_call = mod.get_global_var('func_9123')
func_9124_call = mutated_mod.get_global_var('func_9124')
call_13234 = relay.TupleGetItem(func_9123_call(), 0)
call_13235 = relay.TupleGetItem(func_9124_call(), 0)
func_12502_call = mod.get_global_var('func_12502')
func_12503_call = mutated_mod.get_global_var('func_12503')
call_13252 = relay.TupleGetItem(func_12502_call(), 0)
call_13253 = relay.TupleGetItem(func_12503_call(), 0)
func_4167_call = mod.get_global_var('func_4167')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_13266 = relay.TupleGetItem(func_4167_call(), 0)
call_13267 = relay.TupleGetItem(func_4169_call(), 0)
func_11784_call = mod.get_global_var('func_11784')
func_11785_call = mutated_mod.get_global_var('func_11785')
call_13275 = func_11784_call()
call_13276 = func_11784_call()
func_2615_call = mod.get_global_var('func_2615')
func_2617_call = mutated_mod.get_global_var('func_2617')
call_13278 = relay.TupleGetItem(func_2615_call(relay.reshape(call_13252.astype('float32'), [1, 11, 4])), 0)
call_13279 = relay.TupleGetItem(func_2617_call(relay.reshape(call_13252.astype('float32'), [1, 11, 4])), 0)
output = relay.Tuple([call_13234,call_13252,call_13266,call_13275,call_13278,])
output2 = relay.Tuple([call_13235,call_13253,call_13267,call_13276,call_13279,])
func_13287 = relay.Function([], output)
mod['func_13287'] = func_13287
mod = relay.transform.InferType()(mod)
output = func_13287()
func_13288 = relay.Function([], output)
mutated_mod['func_13288'] = func_13288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9919_call = mod.get_global_var('func_9919')
func_9920_call = mutated_mod.get_global_var('func_9920')
call_13331 = relay.TupleGetItem(func_9919_call(), 0)
call_13332 = relay.TupleGetItem(func_9920_call(), 0)
func_6664_call = mod.get_global_var('func_6664')
func_6665_call = mutated_mod.get_global_var('func_6665')
call_13338 = func_6664_call()
call_13339 = func_6664_call()
output = relay.Tuple([call_13331,call_13338,])
output2 = relay.Tuple([call_13332,call_13339,])
func_13347 = relay.Function([], output)
mod['func_13347'] = func_13347
mod = relay.transform.InferType()(mod)
output = func_13347()
func_13348 = relay.Function([], output)
mutated_mod['func_13348'] = func_13348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mod.get_global_var('func_4689')
func_4690_call = mutated_mod.get_global_var('func_4690')
call_13365 = relay.TupleGetItem(func_4689_call(), 1)
call_13366 = relay.TupleGetItem(func_4690_call(), 1)
func_6208_call = mod.get_global_var('func_6208')
func_6209_call = mutated_mod.get_global_var('func_6209')
call_13378 = relay.TupleGetItem(func_6208_call(), 0)
call_13379 = relay.TupleGetItem(func_6209_call(), 0)
output = relay.Tuple([call_13365,call_13378,])
output2 = relay.Tuple([call_13366,call_13379,])
func_13388 = relay.Function([], output)
mod['func_13388'] = func_13388
mod = relay.transform.InferType()(mod)
output = func_13388()
func_13389 = relay.Function([], output)
mutated_mod['func_13389'] = func_13389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6950_call = mod.get_global_var('func_6950')
func_6951_call = mutated_mod.get_global_var('func_6951')
call_13420 = relay.TupleGetItem(func_6950_call(), 0)
call_13421 = relay.TupleGetItem(func_6951_call(), 0)
func_9884_call = mod.get_global_var('func_9884')
func_9885_call = mutated_mod.get_global_var('func_9885')
call_13422 = relay.TupleGetItem(func_9884_call(), 4)
call_13423 = relay.TupleGetItem(func_9885_call(), 4)
output = relay.Tuple([call_13420,call_13422,])
output2 = relay.Tuple([call_13421,call_13423,])
func_13433 = relay.Function([], output)
mod['func_13433'] = func_13433
mod = relay.transform.InferType()(mod)
output = func_13433()
func_13434 = relay.Function([], output)
mutated_mod['func_13434'] = func_13434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9774_call = mod.get_global_var('func_9774')
func_9776_call = mutated_mod.get_global_var('func_9776')
call_13441 = func_9774_call()
call_13442 = func_9774_call()
func_11784_call = mod.get_global_var('func_11784')
func_11785_call = mutated_mod.get_global_var('func_11785')
call_13456 = func_11784_call()
call_13457 = func_11784_call()
func_7322_call = mod.get_global_var('func_7322')
func_7324_call = mutated_mod.get_global_var('func_7324')
call_13460 = relay.TupleGetItem(func_7322_call(), 0)
call_13461 = relay.TupleGetItem(func_7324_call(), 0)
output = relay.Tuple([call_13441,call_13456,call_13460,])
output2 = relay.Tuple([call_13442,call_13457,call_13461,])
func_13466 = relay.Function([], output)
mod['func_13466'] = func_13466
mod = relay.transform.InferType()(mod)
mutated_mod['func_13466'] = func_13466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13466_call = mutated_mod.get_global_var('func_13466')
call_13467 = func_13466_call()
output = call_13467
func_13468 = relay.Function([], output)
mutated_mod['func_13468'] = func_13468
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13494 = relay.var("var_13494", dtype = "float64", shape = (11, 6, 9))#candidate|13494|(11, 6, 9)|var|float64
uop_13495 = relay.log(var_13494.astype('float64')) # shape=(11, 6, 9)
output = uop_13495
output2 = uop_13495
func_13498 = relay.Function([var_13494,], output)
mod['func_13498'] = func_13498
mod = relay.transform.InferType()(mod)
var_13499 = relay.var("var_13499", dtype = "float64", shape = (11, 6, 9))#candidate|13499|(11, 6, 9)|var|float64
output = func_13498(var_13499)
func_13500 = relay.Function([var_13499], output)
mutated_mod['func_13500'] = func_13500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4949_call = mod.get_global_var('func_4949')
func_4951_call = mutated_mod.get_global_var('func_4951')
call_13634 = func_4949_call()
call_13635 = func_4949_call()
func_13498_call = mod.get_global_var('func_13498')
func_13500_call = mutated_mod.get_global_var('func_13500')
var_13644 = relay.var("var_13644", dtype = "float64", shape = (594, 1))#candidate|13644|(594, 1)|var|float64
call_13643 = func_13498_call(relay.reshape(var_13644.astype('float64'), [11, 6, 9]))
call_13645 = func_13498_call(relay.reshape(var_13644.astype('float64'), [11, 6, 9]))
func_8179_call = mod.get_global_var('func_8179')
func_8180_call = mutated_mod.get_global_var('func_8180')
call_13649 = relay.TupleGetItem(func_8179_call(), 0)
call_13650 = relay.TupleGetItem(func_8180_call(), 0)
func_11867_call = mod.get_global_var('func_11867')
func_11869_call = mutated_mod.get_global_var('func_11869')
call_13672 = relay.TupleGetItem(func_11867_call(), 0)
call_13673 = relay.TupleGetItem(func_11869_call(), 0)
func_1202_call = mod.get_global_var('func_1202')
func_1204_call = mutated_mod.get_global_var('func_1204')
var_13677 = relay.var("var_13677", dtype = "bool", shape = (1248,))#candidate|13677|(1248,)|var|bool
call_13676 = func_1202_call(relay.reshape(var_13677.astype('bool'), [8, 13, 12]))
call_13678 = func_1202_call(relay.reshape(var_13677.astype('bool'), [8, 13, 12]))
bop_13682 = relay.equal(var_13677.astype('bool'), var_13644.astype('bool')) # shape=(594, 1248)
bop_13697 = relay.floor_mod(call_13676.astype('float64'), relay.reshape(var_13677.astype('float64'), relay.shape_of(call_13676))) # shape=(8, 13, 12)
bop_13700 = relay.floor_mod(call_13678.astype('float64'), relay.reshape(var_13677.astype('float64'), relay.shape_of(call_13678))) # shape=(8, 13, 12)
output = relay.Tuple([call_13634,call_13643,call_13649,call_13672,bop_13682,bop_13697,])
output2 = relay.Tuple([call_13635,call_13645,call_13650,call_13673,bop_13682,bop_13700,])
func_13705 = relay.Function([var_13644,var_13677,], output)
mod['func_13705'] = func_13705
mod = relay.transform.InferType()(mod)
mutated_mod['func_13705'] = func_13705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13705_call = mutated_mod.get_global_var('func_13705')
var_13707 = relay.var("var_13707", dtype = "float64", shape = (594, 1))#candidate|13707|(594, 1)|var|float64
var_13708 = relay.var("var_13708", dtype = "bool", shape = (1248,))#candidate|13708|(1248,)|var|bool
call_13706 = func_13705_call(var_13707,var_13708,)
output = call_13706
func_13709 = relay.Function([var_13707,var_13708,], output)
mutated_mod['func_13709'] = func_13709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10828_call = mod.get_global_var('func_10828')
func_10829_call = mutated_mod.get_global_var('func_10829')
call_13753 = func_10828_call()
call_13754 = func_10828_call()
func_8407_call = mod.get_global_var('func_8407')
func_8409_call = mutated_mod.get_global_var('func_8409')
call_13776 = relay.TupleGetItem(func_8407_call(), 0)
call_13777 = relay.TupleGetItem(func_8409_call(), 0)
var_13785 = relay.var("var_13785", dtype = "float64", shape = (48, 2))#candidate|13785|(48, 2)|var|float64
bop_13786 = relay.logical_or(call_13776.astype('bool'), relay.reshape(var_13785.astype('bool'), relay.shape_of(call_13776))) # shape=(48, 2)
bop_13789 = relay.logical_or(call_13777.astype('bool'), relay.reshape(var_13785.astype('bool'), relay.shape_of(call_13777))) # shape=(48, 2)
func_5941_call = mod.get_global_var('func_5941')
func_5943_call = mutated_mod.get_global_var('func_5943')
call_13797 = func_5941_call()
call_13798 = func_5941_call()
output = relay.Tuple([call_13753,bop_13786,call_13797,])
output2 = relay.Tuple([call_13754,bop_13789,call_13798,])
func_13804 = relay.Function([var_13785,], output)
mod['func_13804'] = func_13804
mod = relay.transform.InferType()(mod)
var_13805 = relay.var("var_13805", dtype = "float64", shape = (48, 2))#candidate|13805|(48, 2)|var|float64
output = func_13804(var_13805)
func_13806 = relay.Function([var_13805], output)
mutated_mod['func_13806'] = func_13806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8319_call = mod.get_global_var('func_8319')
func_8320_call = mutated_mod.get_global_var('func_8320')
call_13862 = func_8319_call()
call_13863 = func_8319_call()
uop_13866 = relay.rsqrt(call_13862.astype('float32')) # shape=(16, 8, 5)
uop_13868 = relay.rsqrt(call_13863.astype('float32')) # shape=(16, 8, 5)
output = uop_13866
output2 = uop_13868
func_13875 = relay.Function([], output)
mod['func_13875'] = func_13875
mod = relay.transform.InferType()(mod)
output = func_13875()
func_13876 = relay.Function([], output)
mutated_mod['func_13876'] = func_13876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12502_call = mod.get_global_var('func_12502')
func_12503_call = mutated_mod.get_global_var('func_12503')
call_13910 = relay.TupleGetItem(func_12502_call(), 0)
call_13911 = relay.TupleGetItem(func_12503_call(), 0)
func_9641_call = mod.get_global_var('func_9641')
func_9642_call = mutated_mod.get_global_var('func_9642')
call_13915 = relay.TupleGetItem(func_9641_call(), 0)
call_13916 = relay.TupleGetItem(func_9642_call(), 0)
uop_13930 = relay.asinh(call_13910.astype('float64')) # shape=(1, 11, 4)
uop_13932 = relay.asinh(call_13911.astype('float64')) # shape=(1, 11, 4)
func_6296_call = mod.get_global_var('func_6296')
func_6297_call = mutated_mod.get_global_var('func_6297')
call_13935 = relay.TupleGetItem(func_6296_call(), 0)
call_13936 = relay.TupleGetItem(func_6297_call(), 0)
bop_13942 = relay.logical_xor(uop_13930.astype('int64'), relay.reshape(call_13910.astype('int64'), relay.shape_of(uop_13930))) # shape=(1, 11, 4)
bop_13945 = relay.logical_xor(uop_13932.astype('int64'), relay.reshape(call_13911.astype('int64'), relay.shape_of(uop_13932))) # shape=(1, 11, 4)
output = relay.Tuple([call_13915,call_13935,bop_13942,])
output2 = relay.Tuple([call_13916,call_13936,bop_13945,])
func_13947 = relay.Function([], output)
mod['func_13947'] = func_13947
mod = relay.transform.InferType()(mod)
output = func_13947()
func_13948 = relay.Function([], output)
mutated_mod['func_13948'] = func_13948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6729_call = mod.get_global_var('func_6729')
func_6730_call = mutated_mod.get_global_var('func_6730')
call_13971 = func_6729_call()
call_13972 = func_6729_call()
uop_13982 = relay.exp(call_13971.astype('float64')) # shape=(2, 1560)
uop_13984 = relay.exp(call_13972.astype('float64')) # shape=(2, 1560)
output = relay.Tuple([uop_13982,])
output2 = relay.Tuple([uop_13984,])
func_13985 = relay.Function([], output)
mod['func_13985'] = func_13985
mod = relay.transform.InferType()(mod)
output = func_13985()
func_13986 = relay.Function([], output)
mutated_mod['func_13986'] = func_13986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10636_call = mod.get_global_var('func_10636')
func_10637_call = mutated_mod.get_global_var('func_10637')
call_14035 = relay.TupleGetItem(func_10636_call(), 1)
call_14036 = relay.TupleGetItem(func_10637_call(), 1)
output = call_14035
output2 = call_14036
func_14046 = relay.Function([], output)
mod['func_14046'] = func_14046
mod = relay.transform.InferType()(mod)
output = func_14046()
func_14047 = relay.Function([], output)
mutated_mod['func_14047'] = func_14047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8179_call = mod.get_global_var('func_8179')
func_8180_call = mutated_mod.get_global_var('func_8180')
call_14051 = relay.TupleGetItem(func_8179_call(), 0)
call_14052 = relay.TupleGetItem(func_8180_call(), 0)
func_8537_call = mod.get_global_var('func_8537')
func_8540_call = mutated_mod.get_global_var('func_8540')
var_14061 = relay.var("var_14061", dtype = "float32", shape = (840,))#candidate|14061|(840,)|var|float32
call_14060 = relay.TupleGetItem(func_8537_call(relay.reshape(var_14061.astype('float32'), [840,])), 2)
call_14062 = relay.TupleGetItem(func_8540_call(relay.reshape(var_14061.astype('float32'), [840,])), 2)
func_6664_call = mod.get_global_var('func_6664')
func_6665_call = mutated_mod.get_global_var('func_6665')
call_14090 = func_6664_call()
call_14091 = func_6664_call()
func_5926_call = mod.get_global_var('func_5926')
func_5927_call = mutated_mod.get_global_var('func_5927')
call_14102 = func_5926_call()
call_14103 = func_5926_call()
func_3880_call = mod.get_global_var('func_3880')
func_3881_call = mutated_mod.get_global_var('func_3881')
call_14134 = relay.TupleGetItem(func_3880_call(), 0)
call_14135 = relay.TupleGetItem(func_3881_call(), 0)
output = relay.Tuple([call_14051,call_14060,var_14061,call_14090,call_14102,call_14134,])
output2 = relay.Tuple([call_14052,call_14062,var_14061,call_14091,call_14103,call_14135,])
func_14141 = relay.Function([var_14061,], output)
mod['func_14141'] = func_14141
mod = relay.transform.InferType()(mod)
var_14142 = relay.var("var_14142", dtype = "float32", shape = (840,))#candidate|14142|(840,)|var|float32
output = func_14141(var_14142)
func_14143 = relay.Function([var_14142], output)
mutated_mod['func_14143'] = func_14143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9774_call = mod.get_global_var('func_9774')
func_9776_call = mutated_mod.get_global_var('func_9776')
call_14224 = func_9774_call()
call_14225 = func_9774_call()
func_13947_call = mod.get_global_var('func_13947')
func_13948_call = mutated_mod.get_global_var('func_13948')
call_14242 = relay.TupleGetItem(func_13947_call(), 1)
call_14243 = relay.TupleGetItem(func_13948_call(), 1)
func_9774_call = mod.get_global_var('func_9774')
func_9776_call = mutated_mod.get_global_var('func_9776')
call_14244 = func_9774_call()
call_14245 = func_9774_call()
output = relay.Tuple([call_14224,call_14242,call_14244,])
output2 = relay.Tuple([call_14225,call_14243,call_14245,])
func_14247 = relay.Function([], output)
mod['func_14247'] = func_14247
mod = relay.transform.InferType()(mod)
mutated_mod['func_14247'] = func_14247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14247_call = mutated_mod.get_global_var('func_14247')
call_14248 = func_14247_call()
output = call_14248
func_14249 = relay.Function([], output)
mutated_mod['func_14249'] = func_14249
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14253 = relay.var("var_14253", dtype = "uint16", shape = (12, 9, 15))#candidate|14253|(12, 9, 15)|var|uint16
var_14254 = relay.var("var_14254", dtype = "uint16", shape = (12, 9, 15))#candidate|14254|(12, 9, 15)|var|uint16
bop_14255 = relay.bitwise_and(var_14253.astype('uint16'), relay.reshape(var_14254.astype('uint16'), relay.shape_of(var_14253))) # shape=(12, 9, 15)
func_5048_call = mod.get_global_var('func_5048')
func_5051_call = mutated_mod.get_global_var('func_5051')
const_14264 = relay.const([[-4.462180,3.213704,2.504006,4.188362,4.129797,-7.048113,1.997178,6.105788,7.152365,2.686409,6.344798,9.012320,5.989042,2.138754],[-4.343430,7.196397,-2.261733,1.576804,8.030130,1.246942,-3.057138,-4.778836,-9.021650,8.428298,7.673206,5.638939,5.347690,-3.653044],[9.433776,-9.250796,8.798633,-3.211504,-2.925155,5.315733,-5.715817,-6.239585,-8.264178,9.440203,-6.095671,-8.189977,8.604659,-0.181316],[1.745345,3.880862,-5.032881,-1.325659,-7.284440,-4.441834,1.110805,-3.293306,-8.686038,-1.414967,-4.862077,5.722917,-6.715064,-7.108004],[5.841422,-1.893430,1.150548,-3.538064,-8.786258,9.401640,1.930697,7.343140,2.249215,5.793980,4.568723,6.166442,3.567107,-2.911079],[-2.901750,3.729285,-0.322798,-0.386297,0.525411,5.125036,-6.340273,-3.401921,-5.146796,-8.967250,-1.599107,0.595080,7.660335,3.544622],[5.466529,-4.832266,-4.793895,-5.313482,-2.899041,9.450960,9.468458,1.116168,7.989252,1.996439,5.998254,-8.643409,7.631036,1.576399],[-6.192764,3.934811,5.655841,4.165775,9.214064,-7.316764,9.565792,-9.407395,-7.838991,-3.291236,6.311705,-5.431204,1.697101,-7.364531],[-7.543207,7.399991,-1.218805,5.541149,-4.177018,-9.265936,-0.631199,1.347168,-6.702028,-4.250038,2.544569,-0.357913,-9.872223,-6.870970],[2.843358,3.084270,-2.503227,-3.857280,1.470898,-5.475047,8.371843,-1.818063,5.193175,9.540242,7.055444,2.234485,-8.006432,4.869920],[-6.268349,-7.858813,3.894598,5.613412,-3.149392,-0.836100,1.013039,9.733749,3.901086,-2.354033,-7.583570,-6.020742,6.598379,-4.422779],[-4.619188,3.734621,4.963309,-9.859199,7.102203,4.387192,-2.954944,5.179302,-9.176069,-6.004145,-2.820735,1.386446,-4.509448,-3.633177],[0.724209,1.417081,0.349088,-5.118541,-0.859216,3.341528,-6.682023,3.661804,-1.120876,6.314050,2.472870,0.413232,-6.506011,-0.040732],[-6.901384,2.376599,-8.836874,3.578701,7.136704,-9.707199,9.362034,4.395081,-4.476837,-9.292908,0.165205,-0.951041,1.686826,0.651567],[-3.503769,-9.211403,-1.717275,-9.017601,-2.077345,-5.955298,6.766306,1.707611,-1.666481,-9.129384,8.085409,-2.330079,-8.794274,2.283900],[-3.378094,-5.543668,5.406570,9.131132,-3.175498,-4.339508,-7.468743,-9.222009,8.284302,-9.045032,-8.305753,8.237319,2.643671,-7.057546],[-6.926504,3.280602,-2.777188,0.933488,-0.415110,-0.241439,-8.165648,7.475606,7.270864,-8.523919,7.633901,6.732631,4.780136,4.570898],[-4.960482,6.772126,9.396664,8.507646,-0.403934,0.751653,0.061952,2.538561,-9.275620,-9.356281,-0.363081,2.994508,7.624988,7.924447],[5.289595,9.553874,-8.161229,-2.241418,4.746902,-6.876525,-8.818653,-1.924873,4.468847,9.501331,-3.902351,8.658018,-5.398982,-7.647849],[0.415861,-6.736967,-0.726618,-0.216257,-2.266157,2.675314,-1.112271,4.638948,6.830388,2.960456,1.203052,8.249642,-7.766957,-4.684644],[6.626297,9.681882,-7.853561,2.872895,3.991914,-6.677637,-4.409203,-6.840107,8.184009,6.043430,0.842475,3.053881,7.807841,3.284104],[2.431265,-6.291629,-1.572258,-0.950973,5.402243,-3.133537,5.260647,3.914866,-7.499383,1.496414,7.603373,-4.075682,8.300233,-1.423294],[-5.441195,-8.060080,3.871996,-0.377059,-8.079510,3.541457,-0.447320,8.303497,-7.942071,0.144120,-0.254167,-6.168888,8.600263,-4.019738],[-4.980893,4.250757,-7.776602,-9.810984,-1.530502,-7.343880,1.511680,8.373985,2.658740,-8.685579,1.626865,-6.694432,-0.162043,7.208705],[6.635403,-6.615170,-4.591703,9.683001,0.365618,1.545576,-6.261073,5.508599,2.228068,-7.905057,0.031149,-8.793542,-0.691593,-4.519936],[7.423239,0.086998,9.684980,-2.929449,9.562143,5.792320,8.602178,3.147931,-5.977953,-2.811023,4.040544,-1.145828,9.805098,3.886497],[5.083633,-3.076656,5.512410,7.026232,3.674395,0.261790,9.820815,0.691530,0.958684,5.127889,1.835270,5.371307,-6.089269,9.770454],[-5.261587,5.045020,-7.272603,-8.878518,8.720217,7.937752,3.816581,-5.286828,8.562720,8.963776,-1.941699,-9.886582,-4.795504,-7.876420],[0.635113,-8.342632,-2.014827,9.313758,7.019896,-5.472509,4.567859,5.784847,-2.777165,-4.157035,-7.133915,-0.353820,-5.403736,-0.274044],[-8.161672,2.700475,6.929603,3.300615,5.565556,-2.228991,-8.076151,-3.580483,-2.572208,-5.629061,4.150386,-6.566196,1.753381,-0.532231],[7.311066,-3.786715,7.943889,7.829950,-3.488924,-2.470059,9.593480,-8.277200,1.157576,-8.082957,2.650073,1.145861,3.171487,-4.659137],[-5.901334,-0.342910,6.796686,-0.239561,-2.855501,9.995988,-9.612503,-3.000185,8.609534,-2.744095,1.169757,-9.921818,9.507874,8.926595],[-9.508193,8.506896,-7.200111,-7.287049,5.901892,-7.384375,4.015831,-5.953079,6.743502,8.335928,9.923760,-8.108793,-0.698613,2.252038],[-7.434911,-7.088569,-2.028666,1.355227,7.025759,1.134433,-7.268254,-7.656866,5.654690,-3.864042,-6.750241,9.459489,4.268465,-4.507520],[2.811282,7.587219,0.442759,-3.999042,-0.551103,-2.326478,9.639339,-4.251529,-0.437048,4.318653,3.713475,-4.219251,-7.501093,8.259147],[3.558125,7.203534,-3.096243,-3.528519,7.168742,0.564096,8.007655,5.245662,0.063838,-2.575777,6.190718,-5.913508,9.395915,-0.666250],[-9.114924,9.432465,9.105691,-9.628375,-2.899198,7.652905,8.799030,0.153200,8.444195,-0.094780,-9.007838,-0.094268,-6.288727,-0.323502],[0.193868,7.363039,-1.121711,-4.650448,-3.644464,7.258967,2.673805,-8.229948,-8.904397,8.723216,-9.893599,-3.271937,9.805203,-2.147655],[1.390279,9.967266,8.763872,9.030341,-4.652745,-3.453408,-0.670118,4.939570,-2.446012,3.970365,3.423018,-0.439775,-3.692818,-6.997959],[6.659939,8.537511,9.784464,-9.745752,-7.169469,-5.632233,2.162429,6.003876,1.745063,6.490959,-7.168076,-2.315023,-2.427405,2.436249],[2.527045,-3.074341,8.234563,-3.295018,-8.025704,3.533469,-5.593653,6.079057,-3.753129,3.099481,1.429808,-4.077776,3.469713,0.073785],[3.134324,-8.023137,-0.006596,-1.431762,4.453613,-2.681519,1.955883,-9.258022,-6.488210,5.774338,-3.400388,-9.904299,5.842030,6.594890],[7.698796,-0.326279,8.330788,5.007163,9.924810,7.247652,-3.359825,9.480077,-5.909738,3.523898,7.532479,3.816664,-9.002353,-5.499536],[-2.913889,-6.776073,-5.071966,4.471071,-7.656058,-6.192637,-0.903003,-4.836858,8.415328,-3.754583,3.781817,-8.888859,-5.660117,-7.189303],[3.010476,-3.087115,-9.403919,2.027824,-0.019105,-7.444255,-7.145556,-5.894874,4.992674,5.185416,-4.143206,-1.522036,-9.700212,9.745791],[-3.448029,8.552434,-3.154316,-8.968937,-3.273718,6.611508,-1.704781,9.570553,-1.112218,3.681570,-2.015946,1.702706,-9.128329,-7.175943],[-4.700141,9.466217,9.810191,5.316588,-1.995940,-9.314253,1.511968,7.373717,-4.956024,-2.367275,1.949165,-5.005838,8.339886,-0.262366],[0.069020,-9.596008,-8.962574,-0.643106,-5.394713,5.964439,8.124857,5.754692,-2.930726,-5.274611,-7.440442,8.824626,-3.338650,5.962036],[4.023881,2.181690,5.043010,6.456740,2.195081,8.800977,0.725615,3.694272,9.368522,5.671968,6.709673,-9.014587,5.932327,3.541172],[3.595392,6.498434,2.294422,7.813601,-0.808845,-0.816686,-8.719241,8.333349,2.767028,6.793254,6.027996,-6.312904,-9.459237,-4.765169],[-1.403046,-7.942837,4.181398,4.315670,-0.590634,5.623930,5.747161,4.155575,8.640940,3.482800,1.154576,7.757471,2.779458,0.493478],[-0.111172,5.558746,-9.141580,-3.650924,9.491901,-1.047862,-2.815873,-5.890918,9.276300,-2.952800,-6.755183,7.446517,-8.335400,1.406601],[-5.186188,4.788006,-9.288772,-2.316805,-4.006497,-6.678936,-0.099777,-4.513585,-8.921134,-4.068281,-9.963182,2.536069,-1.885784,-6.592859],[2.924583,-8.633647,-3.157641,3.494931,5.610282,4.767903,-2.336557,0.944073,-7.335925,-8.359743,5.773426,6.721360,6.314634,-2.828075],[1.593871,-1.637572,-6.817230,7.041348,-1.019796,-8.544514,-8.807410,-1.993691,8.677481,8.735571,0.200790,0.607246,-3.746592,-8.538953],[4.374753,4.964332,6.377353,3.505251,-5.065093,-9.886542,2.086830,-5.327564,5.350010,9.607565,4.505095,-6.335737,-9.999687,2.396304],[-3.003567,-5.691426,-2.303433,9.809480,3.028211,-0.448889,2.804627,-0.420306,2.524943,-9.817168,8.949720,0.028279,-5.820279,0.804218],[4.860185,7.349348,-8.886187,1.224873,0.263583,-2.127761,-6.036166,-5.351600,-9.385422,-3.602898,-9.591434,-1.469291,-8.475041,-7.313479],[2.571942,7.605997,-2.056559,5.934458,-4.572898,2.391241,8.056491,-5.700940,-3.542615,9.116760,-4.703778,-1.186862,-8.917862,-7.569732],[1.189966,4.847080,5.402846,3.510079,3.995068,-4.690676,-9.790615,6.989312,-1.958405,4.879924,-9.970701,3.723059,-8.858603,5.903740],[-5.737069,-4.601518,-9.603649,-1.302337,-8.820894,6.211674,-3.473902,-3.683468,-9.214767,-6.703120,1.715068,5.618095,-2.257636,-0.453932],[4.681025,8.819564,-4.343591,6.110212,3.348394,-5.938276,3.414129,1.442043,9.872262,-2.476140,3.905543,-0.868145,-8.413228,5.162536],[-6.392605,-3.595102,2.743257,0.324422,6.630744,2.081370,7.536020,-2.097336,3.780671,-9.942347,7.348641,-2.460176,-6.360348,-0.928019],[4.448220,1.691544,6.032405,2.334741,-7.502414,-9.018827,2.593794,-6.904784,9.287050,4.227278,4.557429,-4.996092,7.711470,8.973037],[0.142908,-2.344865,0.401460,7.736254,7.563081,-1.403437,7.014133,1.282182,-3.259582,1.919860,5.922017,-2.461241,4.705225,0.230214],[-0.428310,-6.748251,-2.177361,-5.115690,-3.388828,2.789974,-5.211533,3.077210,-3.337547,-8.915945,6.871166,2.717513,-1.099419,0.164588],[-9.091294,-4.243465,5.392271,-6.357250,-3.935817,-2.257160,-4.310866,-5.545164,6.270969,6.565830,6.745884,-3.105432,2.122764,2.640276],[3.952188,2.773585,1.452734,-4.258237,-9.737662,9.018362,9.540110,-7.793658,9.652361,-9.876361,-9.295542,-7.208944,8.878111,-9.553571],[-0.010039,2.417154,-8.765144,9.558224,-7.432705,2.707677,4.105915,9.345831,-5.409509,-5.321427,7.805774,-3.721486,-9.708462,5.092434],[9.782188,4.814716,0.585158,7.218229,3.756111,2.283084,1.976799,2.565705,8.578606,1.711123,-6.093938,8.781372,6.607074,1.051325],[8.557756,5.351315,1.037894,-8.414906,3.219881,-1.808468,3.500787,0.330156,-0.949182,1.825324,9.278370,1.144480,-6.319287,5.428004],[-8.045149,-6.480739,6.766900,-8.594473,-8.754665,5.141582,2.587672,-3.725459,-9.846912,1.928216,-7.717425,-4.888871,8.929402,0.039895],[8.896165,7.996564,-6.722791,9.646099,-7.528629,-9.622776,-9.677876,-3.208557,3.081191,-3.134011,-4.814383,3.270066,-1.843552,5.440368],[4.194525,-3.149910,3.970297,5.931345,9.212731,-0.273748,-7.425951,-7.711505,-8.633356,-2.901425,4.682829,1.625106,-3.222341,6.572811],[7.724154,5.698493,6.679145,3.489228,6.196143,-5.912021,6.255477,-3.558246,8.824163,-4.851148,-1.972997,-7.828340,-3.159074,6.355774],[-7.963694,1.642722,9.306291,-5.926681,-1.588933,-6.969059,-2.958967,-1.940733,5.650331,-3.637489,0.867246,-8.540869,6.268768,-9.634997],[8.907318,9.747112,-8.191041,8.096008,1.182378,-9.518006,9.571311,9.808366,-5.865625,3.210130,1.092849,-9.096242,-4.980583,-0.455380],[8.132079,7.091194,-7.614552,-0.227825,-4.860939,4.031614,-5.470022,9.554561,-9.824177,6.335354,4.093909,-1.067836,-8.961798,2.620717],[1.180829,3.284095,-1.321660,4.677059,8.438727,2.243727,7.319755,5.345736,4.736227,5.022752,3.221600,-7.455452,5.847426,7.958544],[3.120934,1.278648,-9.568677,-1.567462,4.367825,-4.250494,3.671696,-2.523961,-0.346617,-0.089291,0.950889,3.676067,0.675295,5.535562],[-4.001001,-9.808767,9.778204,-2.416831,-8.207644,2.085261,2.447035,-3.602293,8.955719,6.955526,-8.220994,0.085617,-3.439576,5.792958],[-9.740507,-1.464589,9.944513,1.500617,-4.447381,1.484696,-8.100607,1.912271,-2.662391,-0.732026,-4.582906,5.467320,-1.982620,-4.327852],[5.887401,-9.778687,-5.224371,-5.873149,3.104452,6.181678,1.024436,7.086058,3.135972,6.218679,-2.277212,2.871902,-0.723579,-0.143549],[-0.438005,3.662712,-1.792948,0.804451,-4.551087,-9.237186,1.130722,-9.016262,-4.427362,-0.999378,-5.031965,1.923779,-5.846469,9.913414],[0.278083,2.641599,4.440217,1.006621,-1.526343,-2.990819,-4.542433,-9.450487,-7.083180,7.478727,-3.919559,-3.517278,2.389159,-8.220000],[4.189479,-0.954341,1.058217,-0.095746,-0.638170,-3.756312,-5.346820,-0.267935,9.450990,7.098948,4.843150,4.142352,-6.763225,-0.523623],[7.291845,7.846417,-4.492724,-5.010743,8.687424,-0.734143,-3.213672,-1.665745,-9.047346,-6.944238,-4.465586,1.059991,-6.657047,5.156715],[0.168451,-6.527341,-9.860412,1.570948,-8.271134,-4.266333,-0.031638,2.697936,5.957466,3.192132,-2.180379,-9.510576,1.278175,-5.885616],[-9.888841,2.791110,2.222040,-0.031635,5.900991,8.112240,7.216599,-9.498968,-7.581818,8.554492,4.464645,2.913728,-9.156193,-7.209800],[-3.525532,6.832531,1.412374,-8.260586,-9.909788,-6.795655,-9.545093,1.360373,-1.683816,7.262775,-0.906455,-3.325695,9.359236,4.286791],[8.141044,-6.734105,6.974511,-4.149443,-3.230220,6.920729,-1.378888,-4.806101,2.993749,-1.148965,3.762773,3.923310,-0.272741,-2.525841],[0.993170,2.360462,2.987918,-1.067350,9.674373,4.779932,4.597998,0.287773,2.063598,-1.718418,5.967042,-3.806880,-5.696663,-2.805535],[2.781370,3.473801,1.328847,-2.161307,-0.484148,6.892277,1.169895,1.468363,8.742996,-5.109440,-8.912611,-9.112619,-9.945576,2.585304],[-0.548920,4.609188,-6.666414,-3.859861,-6.237135,-6.096461,-3.492337,-1.941062,2.323563,-3.581738,-3.781551,0.635732,-0.744513,1.257591],[-4.832526,5.921425,-5.402982,-3.190530,6.096129,-9.351212,4.794980,-6.380834,-0.728234,-5.335882,-8.398278,5.460991,4.131785,-9.489914],[-7.676067,-4.379503,-8.149186,2.073274,7.391841,1.700353,-0.081367,-8.571572,-2.774961,5.919542,1.809960,-3.030261,2.708254,5.589609],[-2.563104,-5.749297,9.445217,4.085318,-5.859684,-7.641720,4.179666,7.480515,-1.792718,5.145052,-9.584930,4.187087,-3.940101,-1.385526],[8.390109,4.599486,4.616568,-7.519121,-5.294669,-8.805953,-1.025265,-0.809030,-1.362505,-7.865921,7.194551,7.389647,-4.711767,-8.073430],[4.516363,-6.377788,-1.740599,-0.848642,5.942015,-1.769962,1.259631,5.788274,6.558379,0.399214,6.815671,-6.794936,2.834516,-4.965663],[8.432098,9.001404,3.662958,9.330227,4.695287,9.620659,0.791042,-4.357199,-4.833396,-0.279716,-8.762546,2.770241,5.366179,-9.323245],[-7.018596,4.484266,6.389875,-1.582049,-9.377770,-1.836041,7.287327,7.667201,7.419286,3.779798,4.955659,-5.719887,2.992614,2.617088],[7.834625,-0.282661,-1.523980,8.116770,-7.758970,9.445990,-9.003159,-1.311162,3.008270,-2.649767,8.174834,8.580968,7.245995,-2.111539],[0.907093,-0.699503,-9.096619,-6.917853,-4.184730,-9.509823,8.654984,7.564373,-5.304056,-1.927868,8.610566,-5.819329,-8.201860,6.533407],[9.570367,7.006121,5.993068,-9.432367,-3.926591,7.931193,-6.610348,9.054730,4.324349,3.000093,-6.219665,4.520225,-2.371559,-3.343752],[4.792665,1.260315,-8.112189,-9.838204,-5.854165,6.580659,4.814759,9.527791,-8.416215,-0.284680,1.030431,0.583468,6.564373,-4.619914],[8.364610,-0.256793,-3.592018,9.130666,-5.337944,0.388659,-6.265914,9.225924,4.704894,-2.911846,2.768789,8.838712,-1.454234,-6.027278],[0.066554,-8.027140,-8.682775,-3.470080,-7.698314,2.604963,3.133945,1.652881,1.509272,6.052698,8.573168,-0.159557,-2.282426,4.964118],[3.692380,-9.358172,-8.348939,4.395093,-8.092225,-1.722003,6.716326,8.991369,-7.742300,1.750429,-4.401400,-1.247914,-2.294764,-2.287399],[-2.836000,1.971054,-3.526011,-1.482004,-7.224366,9.641791,2.678974,5.414711,8.278874,6.808427,2.863243,0.522776,-2.774370,2.186632],[-8.197184,4.246626,-2.811160,-9.840243,2.413202,3.463819,-4.969164,-9.707818,-0.408937,5.898514,-4.590148,0.310921,2.596747,2.550486],[-9.385742,-5.740194,7.200002,3.185498,-8.790947,-4.323561,4.257264,-8.962716,-0.838873,5.095126,-6.229038,-1.017113,-6.507675,4.798480],[-4.813815,2.641852,0.030074,7.501476,7.573139,-1.655257,2.024691,7.363997,9.712625,-6.509243,-9.687941,-6.955036,-6.109871,-1.030481],[5.844612,-0.923472,-7.955837,-2.820226,0.915498,-3.801128,2.949667,7.137332,8.341996,1.605271,-6.608055,-0.084471,4.981201,5.694688],[0.119842,-7.903707,3.283496,-1.742581,-5.008530,-3.106103,3.433689,1.750823,0.787396,8.152465,3.019672,0.328108,-8.732979,8.651344],[1.908610,-6.156160,-1.836686,2.206819,6.292085,2.671163,-8.551691,-2.737401,2.641913,-8.018546,-7.307192,2.062407,-2.907431,5.807094],[0.859037,6.926561,4.572438,3.970260,-8.850158,-0.965464,0.489693,-6.778986,5.975197,6.131055,-5.166073,8.551949,4.878432,-6.992728],[-6.070213,-5.328816,-7.026769,-7.085634,2.419906,3.353178,-4.668228,-3.396368,-0.087441,4.006402,3.723710,-2.569676,5.351754,-6.569832],[-7.617891,-9.771746,-7.586187,-9.916610,-5.666569,-8.803743,2.133590,-1.105647,1.800646,7.610647,9.355970,4.798111,9.506492,-7.057331],[-1.474868,9.158023,1.725307,2.618351,-5.326017,3.367099,-4.783054,6.419068,1.983257,6.459148,-3.168488,-8.172284,4.070517,-0.554174],[3.918527,2.514761,9.338064,9.794972,7.236628,-7.197052,-0.332370,-0.908780,1.624330,-3.810322,5.803778,-4.258927,-9.211075,0.010231],[-5.567171,-2.676359,-5.554567,6.145302,-8.376405,2.570763,1.663739,-9.548761,9.395990,-7.072583,-3.119361,8.985323,-3.285333,8.762948],[9.782259,0.029709,-6.571827,5.231405,1.892307,-5.934522,6.209597,7.094895,9.019842,5.473035,4.480431,2.340288,-2.474249,2.155983],[-7.682390,-4.090034,-7.233452,-1.383147,5.611440,2.960642,-0.095804,3.426907,4.003036,9.889133,-7.994830,8.609527,-7.663475,2.754083],[-6.567277,-0.346577,5.830480,-1.105393,-4.161198,-3.348985,-0.705524,-8.180325,4.002265,7.031528,4.812030,5.034802,7.497721,1.555090],[4.283490,-2.672483,4.256761,7.958106,6.549320,-1.950491,-4.026105,-8.460177,5.019695,2.971571,-6.077768,5.035297,1.928794,3.158766],[-4.292633,6.020992,7.546971,7.126543,-6.640674,9.038136,-7.920449,3.796880,-8.837727,0.579397,-3.795582,-3.248619,2.690942,-3.931298],[-1.593864,5.591674,-1.182479,-9.557432,1.860514,2.050454,-7.976302,8.592607,-1.890809,3.647698,-6.530141,-5.463127,-6.388616,6.127974],[0.851146,-1.458023,6.489437,-5.490538,-8.990318,0.187650,-4.912634,9.649192,3.413805,2.712261,1.569351,-2.167630,0.948463,5.465988],[4.009773,-3.241068,-3.705261,-0.786056,-9.634928,-4.494996,-4.766664,-2.635813,-4.218950,7.629605,0.095623,2.817294,-5.756109,-3.684514],[3.095058,2.907836,9.187972,6.667178,-3.159855,3.760387,-7.885274,-3.171105,-8.542531,9.525569,-6.444317,-6.540072,4.482329,9.494704],[-9.604563,7.957580,9.578230,-1.274443,-3.029039,-8.652517,-5.474439,-9.111741,2.938397,5.282350,9.512201,-9.396699,3.380310,5.080520],[5.836408,-1.828655,0.571774,8.527913,-7.756432,8.188531,7.494116,-6.793465,4.953541,-0.052995,6.213526,-3.714651,-3.976653,-9.141106],[-9.044943,-5.897170,-0.601519,8.051220,-2.439213,-9.603052,-7.262330,-2.673475,-0.365617,6.664846,7.923049,-1.008672,6.408701,2.548247],[-9.882470,-9.943254,-0.789847,-2.501274,2.405210,-9.481723,-0.732971,0.866237,-6.801709,-9.120469,-7.270561,-1.760789,3.788244,-8.202999],[-3.679292,-7.012018,4.038882,3.697287,5.269181,1.421330,6.117835,-9.613525,-1.615137,-6.003262,0.668181,2.342829,2.615503,1.377679]], dtype = "float64")#candidate|14264|(135, 14)|const|float64
call_14263 = func_5048_call(relay.reshape(const_14264.astype('float64'), [14, 15, 9]))
call_14265 = func_5048_call(relay.reshape(const_14264.astype('float64'), [14, 15, 9]))
output = relay.Tuple([bop_14255,call_14263,const_14264,])
output2 = relay.Tuple([bop_14255,call_14265,const_14264,])
func_14275 = relay.Function([var_14253,var_14254,], output)
mod['func_14275'] = func_14275
mod = relay.transform.InferType()(mod)
mutated_mod['func_14275'] = func_14275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14275_call = mutated_mod.get_global_var('func_14275')
var_14277 = relay.var("var_14277", dtype = "uint16", shape = (12, 9, 15))#candidate|14277|(12, 9, 15)|var|uint16
var_14278 = relay.var("var_14278", dtype = "uint16", shape = (12, 9, 15))#candidate|14278|(12, 9, 15)|var|uint16
call_14276 = func_14275_call(var_14277,var_14278,)
output = call_14276
func_14279 = relay.Function([var_14277,var_14278,], output)
mutated_mod['func_14279'] = func_14279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5088_call = mod.get_global_var('func_5088')
func_5090_call = mutated_mod.get_global_var('func_5090')
call_14317 = relay.TupleGetItem(func_5088_call(), 0)
call_14318 = relay.TupleGetItem(func_5090_call(), 0)
func_13466_call = mod.get_global_var('func_13466')
func_13468_call = mutated_mod.get_global_var('func_13468')
call_14329 = relay.TupleGetItem(func_13466_call(), 1)
call_14330 = relay.TupleGetItem(func_13468_call(), 1)
func_5597_call = mod.get_global_var('func_5597')
func_5599_call = mutated_mod.get_global_var('func_5599')
var_14335 = relay.var("var_14335", dtype = "float64", shape = (96,))#candidate|14335|(96,)|var|float64
call_14334 = relay.TupleGetItem(func_5597_call(relay.reshape(var_14335.astype('float64'), [48, 2])), 2)
call_14336 = relay.TupleGetItem(func_5599_call(relay.reshape(var_14335.astype('float64'), [48, 2])), 2)
func_2337_call = mod.get_global_var('func_2337')
func_2340_call = mutated_mod.get_global_var('func_2340')
const_14352 = relay.const(-10, dtype = "uint32")#candidate|14352|()|const|uint32
var_14353 = relay.var("var_14353", dtype = "uint32", shape = (15,))#candidate|14353|(15,)|var|uint32
call_14351 = func_2337_call(relay.reshape(const_14352.astype('uint32'), []), relay.reshape(var_14353.astype('uint32'), [1, 1, 15]), )
call_14354 = func_2337_call(relay.reshape(const_14352.astype('uint32'), []), relay.reshape(var_14353.astype('uint32'), [1, 1, 15]), )
func_5012_call = mod.get_global_var('func_5012')
func_5015_call = mutated_mod.get_global_var('func_5015')
call_14359 = relay.TupleGetItem(func_5012_call(relay.reshape(const_14352.astype('float32'), [])), 1)
call_14360 = relay.TupleGetItem(func_5015_call(relay.reshape(const_14352.astype('float32'), [])), 1)
uop_14369 = relay.atan(call_14334.astype('float32')) # shape=(48, 2)
uop_14371 = relay.atan(call_14336.astype('float32')) # shape=(48, 2)
output = relay.Tuple([call_14317,call_14329,var_14335,call_14351,const_14352,var_14353,call_14359,uop_14369,])
output2 = relay.Tuple([call_14318,call_14330,var_14335,call_14354,const_14352,var_14353,call_14360,uop_14371,])
func_14378 = relay.Function([var_14335,var_14353,], output)
mod['func_14378'] = func_14378
mod = relay.transform.InferType()(mod)
var_14379 = relay.var("var_14379", dtype = "float64", shape = (96,))#candidate|14379|(96,)|var|float64
var_14380 = relay.var("var_14380", dtype = "uint32", shape = (15,))#candidate|14380|(15,)|var|uint32
output = func_14378(var_14379,var_14380,)
func_14381 = relay.Function([var_14379,var_14380,], output)
mutated_mod['func_14381'] = func_14381
mutated_mod = relay.transform.InferType()(mutated_mod)
const_14426 = relay.const([[[-5.441519,-8.510434,-9.097377,6.034715,-7.973585,3.502029,8.178086,-6.808698,-4.391988,7.974999,-1.287447,5.030702,-3.191311]],[[-5.035944,0.227006,-6.990462,2.685339,6.656317,-6.748976,7.081691,-7.551166,9.039310,-5.241195,-8.462996,-0.102617,9.732231]],[[2.436361,0.274767,5.316039,2.687982,4.450152,-5.287178,-6.738621,6.394002,-4.270646,1.257490,0.786065,1.117782,4.029691]],[[-3.567608,4.655852,-3.191092,4.251225,-7.133202,2.752624,8.204948,5.972874,4.876151,8.564344,9.515132,-3.830713,5.854919]],[[6.315848,2.409325,-2.408833,-1.344524,7.455406,-3.594532,-7.092459,-0.687527,-9.444109,5.146418,1.825768,3.800546,4.174749]],[[7.930975,-6.252824,2.911189,7.010647,-8.898015,-0.743149,5.947672,5.557120,-9.970314,-7.244625,2.026757,1.087495,-7.936023]]], dtype = "float32")#candidate|14426|(6, 1, 13)|const|float32
uop_14427 = relay.log(const_14426.astype('float32')) # shape=(6, 1, 13)
func_3703_call = mod.get_global_var('func_3703')
func_3704_call = mutated_mod.get_global_var('func_3704')
call_14440 = relay.TupleGetItem(func_3703_call(), 1)
call_14441 = relay.TupleGetItem(func_3704_call(), 1)
uop_14446 = relay.erf(uop_14427.astype('float32')) # shape=(6, 1, 13)
bop_14455 = relay.not_equal(uop_14427.astype('bool'), relay.reshape(uop_14446.astype('bool'), relay.shape_of(uop_14427))) # shape=(6, 1, 13)
bop_14460 = relay.mod(uop_14427.astype('float64'), relay.reshape(uop_14446.astype('float64'), relay.shape_of(uop_14427))) # shape=(6, 1, 13)
output = relay.Tuple([call_14440,bop_14455,bop_14460,])
output2 = relay.Tuple([call_14441,bop_14455,bop_14460,])
func_14464 = relay.Function([], output)
mod['func_14464'] = func_14464
mod = relay.transform.InferType()(mod)
output = func_14464()
func_14465 = relay.Function([], output)
mutated_mod['func_14465'] = func_14465
mutated_mod = relay.transform.InferType()(mutated_mod)
const_14488 = relay.const(1.168428, dtype = "float32")#candidate|14488|()|const|float32
var_14489 = relay.var("var_14489", dtype = "float32", shape = (7, 11, 9))#candidate|14489|(7, 11, 9)|var|float32
bop_14490 = relay.less_equal(const_14488.astype('bool'), var_14489.astype('bool')) # shape=(7, 11, 9)
func_2216_call = mod.get_global_var('func_2216')
func_2219_call = mutated_mod.get_global_var('func_2219')
var_14497 = relay.var("var_14497", dtype = "float32", shape = (2, 1560))#candidate|14497|(2, 1560)|var|float32
call_14496 = relay.TupleGetItem(func_2216_call(relay.reshape(const_14488.astype('float32'), []), relay.reshape(var_14497.astype('float32'), [13, 16, 15]), ), 0)
call_14498 = relay.TupleGetItem(func_2219_call(relay.reshape(const_14488.astype('float32'), []), relay.reshape(var_14497.astype('float32'), [13, 16, 15]), ), 0)
bop_14502 = relay.bitwise_xor(call_14496.astype('uint64'), const_14488.astype('uint64')) # shape=(13, 16, 15)
bop_14505 = relay.bitwise_xor(call_14498.astype('uint64'), const_14488.astype('uint64')) # shape=(13, 16, 15)
uop_14515 = relay.atanh(bop_14490.astype('float64')) # shape=(7, 11, 9)
func_8696_call = mod.get_global_var('func_8696')
func_8697_call = mutated_mod.get_global_var('func_8697')
call_14519 = relay.TupleGetItem(func_8696_call(), 0)
call_14520 = relay.TupleGetItem(func_8697_call(), 0)
uop_14522 = relay.cosh(bop_14502.astype('float32')) # shape=(13, 16, 15)
uop_14524 = relay.cosh(bop_14505.astype('float32')) # shape=(13, 16, 15)
func_6208_call = mod.get_global_var('func_6208')
func_6209_call = mutated_mod.get_global_var('func_6209')
call_14529 = relay.TupleGetItem(func_6208_call(), 2)
call_14530 = relay.TupleGetItem(func_6209_call(), 2)
func_12502_call = mod.get_global_var('func_12502')
func_12503_call = mutated_mod.get_global_var('func_12503')
call_14536 = relay.TupleGetItem(func_12502_call(), 1)
call_14537 = relay.TupleGetItem(func_12503_call(), 1)
bop_14548 = relay.greater(uop_14515.astype('bool'), relay.reshape(var_14489.astype('bool'), relay.shape_of(uop_14515))) # shape=(7, 11, 9)
output = relay.Tuple([var_14497,call_14519,uop_14522,call_14529,call_14536,bop_14548,])
output2 = relay.Tuple([var_14497,call_14520,uop_14524,call_14530,call_14537,bop_14548,])
func_14557 = relay.Function([var_14489,var_14497,], output)
mod['func_14557'] = func_14557
mod = relay.transform.InferType()(mod)
mutated_mod['func_14557'] = func_14557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14557_call = mutated_mod.get_global_var('func_14557')
var_14559 = relay.var("var_14559", dtype = "float32", shape = (7, 11, 9))#candidate|14559|(7, 11, 9)|var|float32
var_14560 = relay.var("var_14560", dtype = "float32", shape = (2, 1560))#candidate|14560|(2, 1560)|var|float32
call_14558 = func_14557_call(var_14559,var_14560,)
output = call_14558
func_14561 = relay.Function([var_14559,var_14560,], output)
mutated_mod['func_14561'] = func_14561
mutated_mod = relay.transform.InferType()(mutated_mod)
const_14573 = relay.const([[[False,False,True,True,False,True,False],[True,False,True,True,True,True,True],[True,False,True,False,False,True,False],[False,True,False,False,True,True,True],[True,False,True,False,False,False,True],[True,True,True,False,False,False,True],[True,False,False,False,False,False,False]]], dtype = "bool")#candidate|14573|(1, 7, 7)|const|bool
var_14574 = relay.var("var_14574", dtype = "bool", shape = (1, 7, 7))#candidate|14574|(1, 7, 7)|var|bool
bop_14575 = relay.logical_and(const_14573.astype('bool'), relay.reshape(var_14574.astype('bool'), relay.shape_of(const_14573))) # shape=(1, 7, 7)
output = bop_14575
output2 = bop_14575
func_14595 = relay.Function([var_14574,], output)
mod['func_14595'] = func_14595
mod = relay.transform.InferType()(mod)
var_14596 = relay.var("var_14596", dtype = "bool", shape = (1, 7, 7))#candidate|14596|(1, 7, 7)|var|bool
output = func_14595(var_14596)
func_14597 = relay.Function([var_14596], output)
mutated_mod['func_14597'] = func_14597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13347_call = mod.get_global_var('func_13347')
func_13348_call = mutated_mod.get_global_var('func_13348')
call_14714 = relay.TupleGetItem(func_13347_call(), 1)
call_14715 = relay.TupleGetItem(func_13348_call(), 1)
func_5319_call = mod.get_global_var('func_5319')
func_5321_call = mutated_mod.get_global_var('func_5321')
call_14717 = relay.TupleGetItem(func_5319_call(), 0)
call_14718 = relay.TupleGetItem(func_5321_call(), 0)
func_2337_call = mod.get_global_var('func_2337')
func_2340_call = mutated_mod.get_global_var('func_2340')
var_14726 = relay.var("var_14726", dtype = "uint32", shape = ())#candidate|14726|()|var|uint32
const_14727 = relay.const([-9,6,-7,-2,8,6,9,8,-2,4,3,-3,2,-10,-4], dtype = "uint32")#candidate|14727|(15,)|const|uint32
call_14725 = func_2337_call(relay.reshape(var_14726.astype('uint32'), []), relay.reshape(const_14727.astype('uint32'), [1, 1, 15]), )
call_14728 = func_2337_call(relay.reshape(var_14726.astype('uint32'), []), relay.reshape(const_14727.astype('uint32'), [1, 1, 15]), )
func_11696_call = mod.get_global_var('func_11696')
func_11698_call = mutated_mod.get_global_var('func_11698')
call_14738 = relay.TupleGetItem(func_11696_call(), 2)
call_14739 = relay.TupleGetItem(func_11698_call(), 2)
func_14557_call = mod.get_global_var('func_14557')
func_14561_call = mutated_mod.get_global_var('func_14561')
const_14741 = relay.const([[5.958601,-8.155085,6.010232],[-2.537781,-4.803967,3.854272],[-5.664673,-7.347126,1.037801],[8.186473,2.959224,8.353357],[3.364903,-7.366368,-7.235236],[-2.293016,-2.924375,-2.869897],[7.589945,7.671522,-5.317009],[-1.817991,-1.233949,9.911437],[6.113519,-3.502808,5.932545],[0.594640,-3.768985,5.125003],[8.463973,-1.191899,-4.567582],[-1.404252,6.926899,0.452810],[-6.886139,-7.158549,-9.377156],[-8.170365,-3.452948,-1.352424],[-0.915874,1.436262,-7.747773],[2.799659,-3.609086,6.023996],[-9.350254,-5.363369,1.556839],[-8.705937,5.348860,-1.890815],[-5.548712,3.573477,2.434944],[-7.545000,6.366920,-9.901771],[-5.601565,-4.720894,2.083846],[-5.425553,6.898799,6.496279],[-4.476177,-9.712370,-2.365821],[-3.609065,5.656314,-6.356456],[7.422885,-7.564308,-7.567689],[-0.798844,-2.949397,1.996482],[-8.444384,-6.067263,-8.190377],[5.406852,3.286021,7.667246],[-1.360607,-2.296934,8.401513],[3.684084,3.249650,-9.220896],[-4.256068,1.803743,7.838044],[7.484696,-8.300225,6.641480],[9.245341,1.266513,-7.239658],[0.822198,-7.064571,-7.474252],[-4.603661,4.848718,3.977640],[4.885199,-3.320496,-5.565503],[2.832884,-1.497907,8.296588],[-5.894179,-3.037175,1.617690],[-1.443609,0.006418,-7.133537],[7.653661,0.430949,6.691633],[-9.989729,7.932801,0.964420],[-7.238175,4.030211,-8.510462],[-0.190225,6.819348,-1.602643],[4.613889,5.943427,-6.090148],[-5.544693,-2.597798,-1.505572],[-9.336001,-2.954095,3.856145],[8.192128,-3.324033,-3.036154],[-2.243552,-9.041169,2.292737],[-9.902234,6.832400,-0.259077],[-5.610051,0.895035,-7.644275],[-2.567529,-0.502917,-9.559206],[-6.591669,6.692351,-2.407251],[2.265205,-3.842885,8.493327],[-7.311777,-8.532461,7.079375],[2.799465,9.280614,7.433557],[-9.595340,-8.920988,-0.182114],[5.642267,0.126589,-3.680491],[-4.510534,-6.516783,7.620619],[6.589633,5.803047,0.688812],[-1.990187,-6.035133,-8.104755],[8.163140,4.538235,6.704350],[5.873780,-7.823811,-4.238063],[-4.749410,-2.181468,8.923956],[-3.361356,-4.469359,6.175286],[0.980169,-2.352998,6.435404],[7.400557,-6.854596,4.817831],[-9.716083,-5.411304,0.104763],[0.384932,6.330750,-2.016330],[4.024778,8.774785,-3.830459],[-4.842419,-5.813760,-0.276910],[0.948068,3.576200,-4.078509],[0.248765,6.932069,-7.702452],[-1.911642,-4.040600,9.412318],[8.042399,-6.911658,-0.256964],[8.190164,-6.524992,-6.111579],[5.938034,-5.221158,4.692202],[4.087589,1.382830,-9.131112],[3.404048,-8.294711,-0.929177],[-6.465457,-1.152895,6.788877],[-5.900029,4.281721,-9.822248],[5.681950,0.463905,-6.889795],[-4.611784,-4.947357,-4.873112],[3.434227,3.538748,-4.795534],[-7.432312,4.517527,2.650332],[9.587804,7.761314,-9.708178],[-2.401722,-7.632602,1.131600],[-7.013085,-7.449137,2.811222],[2.908644,3.068477,-7.332486],[5.053460,-7.255172,-9.330408],[8.484194,4.618137,-0.615700],[-1.176488,8.992658,8.665689],[-3.745837,4.957163,-2.716974],[7.370639,3.131924,-1.453046],[-8.896294,-6.284294,5.923048],[-7.032224,2.319319,4.592962],[6.583790,-2.150957,-5.191483],[9.622213,-9.745590,-8.566815],[-8.599835,-7.121029,-8.865895],[3.797015,-0.314618,7.909730],[-8.005176,-3.821926,-9.782018],[-5.917585,-3.900082,-4.360012],[-2.166150,9.916020,-9.757132],[4.059427,2.371038,2.930507],[-3.092935,7.949703,-8.094543],[-4.483535,-9.335364,-3.167043],[4.923491,1.453518,-8.568546],[-0.625596,2.684685,2.492429],[0.718290,-1.404628,-7.017201],[-7.706539,2.893483,-9.430137],[3.301113,-7.026642,1.474259],[-0.984774,1.444517,-4.435646],[2.416343,-6.075326,-9.247565],[3.539451,-6.516717,4.153838],[2.012837,-1.313583,0.082599],[-3.128741,1.122224,-7.522547],[-7.851299,2.000188,-6.730282],[6.516184,6.673828,5.296017],[8.154381,0.324900,-4.994096],[-7.428913,8.643814,-4.855919],[7.970071,2.295577,-9.247776],[-7.648682,-7.387463,-3.724508],[7.265868,-3.408486,-3.957067],[3.730683,-6.903442,6.052005],[8.787513,-0.150452,-0.577041],[7.116751,-2.444060,0.015486],[-6.261961,3.259271,9.095973],[-4.617429,5.074880,8.788950],[-1.317717,5.967559,-3.733655],[1.094994,-6.854487,-4.743662],[1.217415,6.970022,-6.135185],[-6.534141,-3.918816,0.346564],[8.339190,-0.968456,-4.344760],[-8.658803,-7.154584,-8.169596],[4.582405,-6.178998,7.883626],[-8.596768,-2.973337,-0.297997],[-8.331629,-6.279283,-8.651765],[7.320594,9.886624,-4.544040],[9.258917,-9.545555,-2.109687],[-8.474662,-9.665955,-4.171763],[1.044043,-7.571821,-3.627928],[-6.592237,5.767196,2.500101],[-8.834867,-4.027882,-9.930355],[-1.760405,6.586927,-2.134393],[1.499183,1.673782,3.989091],[1.967085,5.764098,8.238105],[5.506502,-7.769705,-8.436285],[-3.634382,-4.256177,-3.914708],[-2.782021,4.045910,1.976359],[4.939998,-5.039590,-3.287079],[-2.014757,9.963042,-9.699824],[6.648028,-3.464021,-9.420431],[4.578570,-8.989113,3.117414],[2.532446,5.647263,-5.740173],[-9.935267,7.548443,-6.880942],[-7.856043,2.173646,-3.911078],[-9.871546,6.288229,-0.765997],[9.356587,5.304989,8.193254],[-9.197638,-5.939710,3.870972],[-6.547018,-2.167586,1.978095],[-3.450450,-9.540818,3.074781],[7.417030,-1.071693,-7.955950],[-8.532491,6.961705,3.256408],[5.259614,2.859737,4.607214],[-6.204095,-2.014402,8.939239],[5.209507,8.798851,-6.434656],[5.164129,8.407768,-5.095224],[-7.745217,4.023357,-5.918849],[-9.791263,3.454446,0.427439],[9.208235,-4.630908,5.370285],[6.085710,2.788313,-0.634400],[9.250853,9.714789,8.629993],[-6.184238,3.889285,4.586266],[0.139842,0.573828,8.732609],[0.648031,-5.193996,-7.150315],[-0.332486,-5.960405,3.947158],[4.476421,-5.734383,5.195979],[-8.136511,0.082947,9.729038],[-9.008147,4.614789,5.545834],[-2.764836,2.325419,2.148174],[-5.384125,2.095875,2.883352],[5.086938,1.303287,-8.742364],[-5.201459,-2.132778,-5.305386],[-0.791270,-8.247302,-5.863372],[1.629969,7.849047,6.324553],[-8.436864,-7.234950,-6.451927],[-6.294472,-9.264687,-8.214956],[-5.278623,8.739877,-6.836890],[0.319797,-3.447149,-3.877504],[1.590616,-7.719839,-8.129936],[8.960785,1.508442,-9.628465],[-1.223930,-5.565062,-2.322512],[3.482275,2.861733,-3.387014],[-6.474240,-2.663392,9.253113],[8.813960,-8.169160,4.672451],[8.242068,-1.918403,-8.695584],[-2.492503,4.565251,8.235882],[4.068240,5.768768,-1.471978],[9.198321,7.892677,8.999327],[-0.558074,1.556880,-4.294163],[-5.401059,-7.099445,2.746120],[3.858569,7.245487,-0.590474],[2.444393,7.323205,-7.397612],[-6.756828,-9.328131,7.411642],[-1.560828,-6.824007,2.497366],[5.206792,-9.853973,-8.378471],[-3.618867,4.702186,-7.316319],[4.076870,-0.127584,-5.465006],[-4.713918,-4.628966,-3.185240],[-8.099783,4.919139,7.926101],[-4.081885,-8.467153,-3.264475],[-3.334323,4.411294,-0.810274],[8.431504,9.003857,-5.774416],[-9.256483,-6.676620,7.692773],[-7.060806,8.865528,-1.019353],[-1.891988,3.327582,7.952200],[8.114170,6.484305,6.907710],[1.794516,7.449256,-5.650401],[-4.939317,-9.662640,3.265249],[-7.405514,4.646315,-7.678088],[-8.367337,-4.642674,0.112606],[0.930750,7.079548,3.483066],[-8.457663,1.781808,5.265351],[0.551093,-7.267461,-4.448700],[8.017251,-0.184110,3.004886],[-1.773859,7.510805,0.086333],[-1.966369,-2.814377,0.750629],[-4.408926,-4.153825,8.871478],[-1.148752,4.795559,-1.920399],[-3.813443,-8.808582,3.519277],[5.981211,1.378956,-8.759918],[-8.406947,4.311489,3.681110]], dtype = "float32")#candidate|14741|(231, 3)|const|float32
var_14742 = relay.var("var_14742", dtype = "float32", shape = (3120,))#candidate|14742|(3120,)|var|float32
call_14740 = relay.TupleGetItem(func_14557_call(relay.reshape(const_14741.astype('float32'), [7, 11, 9]), relay.reshape(var_14742.astype('float32'), [2, 1560]), ), 2)
call_14743 = relay.TupleGetItem(func_14561_call(relay.reshape(const_14741.astype('float32'), [7, 11, 9]), relay.reshape(var_14742.astype('float32'), [2, 1560]), ), 2)
output = relay.Tuple([call_14714,call_14717,call_14725,var_14726,const_14727,call_14738,call_14740,const_14741,var_14742,])
output2 = relay.Tuple([call_14715,call_14718,call_14728,var_14726,const_14727,call_14739,call_14743,const_14741,var_14742,])
func_14750 = relay.Function([var_14726,var_14742,], output)
mod['func_14750'] = func_14750
mod = relay.transform.InferType()(mod)
var_14751 = relay.var("var_14751", dtype = "uint32", shape = ())#candidate|14751|()|var|uint32
var_14752 = relay.var("var_14752", dtype = "float32", shape = (3120,))#candidate|14752|(3120,)|var|float32
output = func_14750(var_14751,var_14752,)
func_14753 = relay.Function([var_14751,var_14752,], output)
mutated_mod['func_14753'] = func_14753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8465_call = mod.get_global_var('func_8465')
func_8467_call = mutated_mod.get_global_var('func_8467')
call_14765 = relay.TupleGetItem(func_8465_call(), 0)
call_14766 = relay.TupleGetItem(func_8467_call(), 0)
output = relay.Tuple([call_14765,])
output2 = relay.Tuple([call_14766,])
func_14802 = relay.Function([], output)
mod['func_14802'] = func_14802
mod = relay.transform.InferType()(mod)
mutated_mod['func_14802'] = func_14802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14802_call = mutated_mod.get_global_var('func_14802')
call_14803 = func_14802_call()
output = call_14803
func_14804 = relay.Function([], output)
mutated_mod['func_14804'] = func_14804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10613_call = mod.get_global_var('func_10613')
func_10615_call = mutated_mod.get_global_var('func_10615')
call_14854 = relay.TupleGetItem(func_10613_call(), 0)
call_14855 = relay.TupleGetItem(func_10615_call(), 0)
func_7272_call = mod.get_global_var('func_7272')
func_7273_call = mutated_mod.get_global_var('func_7273')
call_14864 = relay.TupleGetItem(func_7272_call(), 1)
call_14865 = relay.TupleGetItem(func_7273_call(), 1)
output = relay.Tuple([call_14854,call_14864,])
output2 = relay.Tuple([call_14855,call_14865,])
func_14866 = relay.Function([], output)
mod['func_14866'] = func_14866
mod = relay.transform.InferType()(mod)
output = func_14866()
func_14867 = relay.Function([], output)
mutated_mod['func_14867'] = func_14867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13053_call = mod.get_global_var('func_13053')
func_13055_call = mutated_mod.get_global_var('func_13055')
call_14868 = relay.TupleGetItem(func_13053_call(), 0)
call_14869 = relay.TupleGetItem(func_13055_call(), 0)
output = call_14868
output2 = call_14869
func_14892 = relay.Function([], output)
mod['func_14892'] = func_14892
mod = relay.transform.InferType()(mod)
output = func_14892()
func_14893 = relay.Function([], output)
mutated_mod['func_14893'] = func_14893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6729_call = mod.get_global_var('func_6729')
func_6730_call = mutated_mod.get_global_var('func_6730')
call_14941 = func_6729_call()
call_14942 = func_6729_call()
func_11867_call = mod.get_global_var('func_11867')
func_11869_call = mutated_mod.get_global_var('func_11869')
call_14946 = relay.TupleGetItem(func_11867_call(), 1)
call_14947 = relay.TupleGetItem(func_11869_call(), 1)
output = relay.Tuple([call_14941,call_14946,])
output2 = relay.Tuple([call_14942,call_14947,])
func_14948 = relay.Function([], output)
mod['func_14948'] = func_14948
mod = relay.transform.InferType()(mod)
output = func_14948()
func_14949 = relay.Function([], output)
mutated_mod['func_14949'] = func_14949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5689_call = mod.get_global_var('func_5689')
func_5690_call = mutated_mod.get_global_var('func_5690')
call_14955 = relay.TupleGetItem(func_5689_call(), 1)
call_14956 = relay.TupleGetItem(func_5690_call(), 1)
output = relay.Tuple([call_14955,])
output2 = relay.Tuple([call_14956,])
func_14958 = relay.Function([], output)
mod['func_14958'] = func_14958
mod = relay.transform.InferType()(mod)
output = func_14958()
func_14959 = relay.Function([], output)
mutated_mod['func_14959'] = func_14959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13388_call = mod.get_global_var('func_13388')
func_13389_call = mutated_mod.get_global_var('func_13389')
call_14986 = relay.TupleGetItem(func_13388_call(), 0)
call_14987 = relay.TupleGetItem(func_13389_call(), 0)
func_6296_call = mod.get_global_var('func_6296')
func_6297_call = mutated_mod.get_global_var('func_6297')
call_14988 = relay.TupleGetItem(func_6296_call(), 0)
call_14989 = relay.TupleGetItem(func_6297_call(), 0)
output = relay.Tuple([call_14986,call_14988,])
output2 = relay.Tuple([call_14987,call_14989,])
func_14992 = relay.Function([], output)
mod['func_14992'] = func_14992
mod = relay.transform.InferType()(mod)
output = func_14992()
func_14993 = relay.Function([], output)
mutated_mod['func_14993'] = func_14993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7529_call = mod.get_global_var('func_7529')
func_7531_call = mutated_mod.get_global_var('func_7531')
call_15005 = func_7529_call()
call_15006 = func_7529_call()
output = relay.Tuple([call_15005,])
output2 = relay.Tuple([call_15006,])
func_15017 = relay.Function([], output)
mod['func_15017'] = func_15017
mod = relay.transform.InferType()(mod)
mutated_mod['func_15017'] = func_15017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15017_call = mutated_mod.get_global_var('func_15017')
call_15018 = func_15017_call()
output = call_15018
func_15019 = relay.Function([], output)
mutated_mod['func_15019'] = func_15019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14992_call = mod.get_global_var('func_14992')
func_14993_call = mutated_mod.get_global_var('func_14993')
call_15156 = relay.TupleGetItem(func_14992_call(), 0)
call_15157 = relay.TupleGetItem(func_14993_call(), 0)
func_11293_call = mod.get_global_var('func_11293')
func_11295_call = mutated_mod.get_global_var('func_11295')
call_15158 = func_11293_call()
call_15159 = func_11293_call()
func_14046_call = mod.get_global_var('func_14046')
func_14047_call = mutated_mod.get_global_var('func_14047')
call_15160 = func_14046_call()
call_15161 = func_14046_call()
func_10318_call = mod.get_global_var('func_10318')
func_10320_call = mutated_mod.get_global_var('func_10320')
call_15180 = relay.TupleGetItem(func_10318_call(), 0)
call_15181 = relay.TupleGetItem(func_10320_call(), 0)
output = relay.Tuple([call_15156,call_15158,call_15160,call_15180,])
output2 = relay.Tuple([call_15157,call_15159,call_15161,call_15181,])
func_15199 = relay.Function([], output)
mod['func_15199'] = func_15199
mod = relay.transform.InferType()(mod)
output = func_15199()
func_15200 = relay.Function([], output)
mutated_mod['func_15200'] = func_15200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9579_call = mod.get_global_var('func_9579')
func_9581_call = mutated_mod.get_global_var('func_9581')
call_15215 = relay.TupleGetItem(func_9579_call(), 0)
call_15216 = relay.TupleGetItem(func_9581_call(), 0)
func_7013_call = mod.get_global_var('func_7013')
func_7014_call = mutated_mod.get_global_var('func_7014')
call_15249 = relay.TupleGetItem(func_7013_call(), 0)
call_15250 = relay.TupleGetItem(func_7014_call(), 0)
func_2216_call = mod.get_global_var('func_2216')
func_2219_call = mutated_mod.get_global_var('func_2219')
var_15258 = relay.var("var_15258", dtype = "float32", shape = ())#candidate|15258|()|var|float32
var_15259 = relay.var("var_15259", dtype = "float32", shape = (3120,))#candidate|15259|(3120,)|var|float32
call_15257 = relay.TupleGetItem(func_2216_call(relay.reshape(var_15258.astype('float32'), []), relay.reshape(var_15259.astype('float32'), [13, 16, 15]), ), 0)
call_15260 = relay.TupleGetItem(func_2219_call(relay.reshape(var_15258.astype('float32'), []), relay.reshape(var_15259.astype('float32'), [13, 16, 15]), ), 0)
output = relay.Tuple([call_15215,call_15249,call_15257,var_15258,var_15259,])
output2 = relay.Tuple([call_15216,call_15250,call_15260,var_15258,var_15259,])
func_15262 = relay.Function([var_15258,var_15259,], output)
mod['func_15262'] = func_15262
mod = relay.transform.InferType()(mod)
mutated_mod['func_15262'] = func_15262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15262_call = mutated_mod.get_global_var('func_15262')
var_15264 = relay.var("var_15264", dtype = "float32", shape = ())#candidate|15264|()|var|float32
var_15265 = relay.var("var_15265", dtype = "float32", shape = (3120,))#candidate|15265|(3120,)|var|float32
call_15263 = func_15262_call(var_15264,var_15265,)
output = call_15263
func_15266 = relay.Function([var_15264,var_15265,], output)
mutated_mod['func_15266'] = func_15266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mod.get_global_var('func_4689')
func_4690_call = mutated_mod.get_global_var('func_4690')
call_15278 = relay.TupleGetItem(func_4689_call(), 0)
call_15279 = relay.TupleGetItem(func_4690_call(), 0)
output = call_15278
output2 = call_15279
func_15281 = relay.Function([], output)
mod['func_15281'] = func_15281
mod = relay.transform.InferType()(mod)
mutated_mod['func_15281'] = func_15281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15281_call = mutated_mod.get_global_var('func_15281')
call_15282 = func_15281_call()
output = call_15282
func_15283 = relay.Function([], output)
mutated_mod['func_15283'] = func_15283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6228_call = mod.get_global_var('func_6228')
func_6230_call = mutated_mod.get_global_var('func_6230')
call_15292 = relay.TupleGetItem(func_6228_call(), 0)
call_15293 = relay.TupleGetItem(func_6230_call(), 0)
func_7796_call = mod.get_global_var('func_7796')
func_7799_call = mutated_mod.get_global_var('func_7799')
const_15299 = relay.const(8.042854, dtype = "float32")#candidate|15299|()|const|float32
const_15300 = relay.const([3.732517,9.222253,6.254852,0.436451,3.251910,-1.824021,3.066221,6.917705,-6.254835,1.394813,7.795760,-9.912761,7.632939,2.921469,6.219594,7.709583,3.029723,1.224851,-2.584782,9.177187,6.683173,6.384959,0.430521,1.037614,4.605173,-7.335994,3.945177,7.604686,-2.312827,9.949165,1.199481,-3.795389,2.379668,-4.537948,-4.264640,2.519895,0.271695,6.982168,-0.577502,-4.424445,7.202006,-2.782584,4.202531,3.977532,-1.090160,5.229302,8.206499,2.251059,-0.126248,-7.267624,4.680664,-9.021927,3.495616,5.993813,-9.761108,8.416743,-8.352384,-2.218082,3.734871,7.295190,-5.720617,-2.701255,-4.059229,8.290562,3.534970,-3.837618,0.888708,1.218607,-3.678998,-2.470613,-0.366108,-2.877225,0.959107,-4.829167,-3.570269,8.069253,-4.621292,-4.067013,4.614582,4.874627,-5.531651,0.712632,5.109323,-9.911626,-9.825683,-6.890308,-2.473289,7.044263,-4.318637,-8.431480,-0.841535,8.326938,5.736348,7.198128,8.394200,2.634070,-8.928857,-5.470294,9.045874,3.759052,7.771574,-3.311368,-1.347721,-7.107963,0.395364,1.456087,-5.185748,4.121215,7.489850,-4.711464,8.507309,-5.371463,-0.042826,9.549331,1.963753,3.925714,0.998843,-1.826016,-5.309824,-5.107303,8.404924,6.054870,-4.754587,-2.520261,0.995483,0.937620,-0.422878,0.177336,-2.693980,2.766181,8.451085,-3.285162,-7.628208,3.468975,9.140497,2.639119,6.390864,-3.398389,3.334294,5.623630,4.698915,1.298401,-1.717772,9.993283,-9.450226,-7.771333,7.802107,-7.740348,9.321219,-9.318868,8.030658,-1.996821,-6.833043,-7.436465,7.313498,4.689702,-1.200040,-2.814034,4.419519,2.747868,-6.286622,6.696096,0.924774,-1.007098,0.547982,2.058874,-9.887423,-3.010482,4.179221,-0.638761,-6.307144,5.950401,-4.180883,-6.181198,0.326697,8.183939,5.735211,-6.386144,-7.713780,-6.249816,7.440609,-7.147994,0.471538,7.709806,-4.173669,6.894599,1.974532,8.435970,-1.276074,5.261649,-1.182460,-6.243257,2.507491,-6.735658,3.163653,-0.608081,-9.888811,-3.380595,3.716380,-4.664863,4.318548,-0.547020,9.486068,-5.053385,2.960855,0.910170,4.756308,-2.219500,-0.924774,-7.266211,6.481822,2.540995,-8.777601,1.127556,4.597722,1.781934,5.447408,4.102296,6.983525,-0.757944,0.177990,-8.782108,4.819794,8.714112,3.231465,2.133436,-1.960608,3.476649,-2.704799,-1.596059,-0.076181,-2.660908,-2.179094,-8.350066,-0.034229,-5.985431,4.229068,-6.275853,3.386705,-1.225722,4.583109,4.085693,-8.510629,-4.430741,3.004818,-3.312149,-7.532790,0.073221,-5.851295,7.560214,8.621814,-2.723074,-6.677049,2.975079,2.016847,1.073284,-4.096449,-0.644996,3.419187,6.156167,-7.674315,-6.080851,0.210934,3.271977,-5.119423,-0.147459,-3.081646,-5.076100,3.257973,3.259160,3.615700,7.877992,1.096269,2.983016,2.804281,-8.495803,-4.320819,-4.016004,-5.908756,-2.865771,-3.748946,-9.686987,8.181420,-3.899241,1.442298,8.812294,-7.793292,-9.692324,2.114362,-3.315674,-6.617245,-6.590929,9.737953,-4.647450,-3.649651,-5.486525,3.516169,0.562703,3.376990,4.388367,0.111475,-3.416989,-8.754711,-6.432310,-6.437836,-5.585707,6.351425,6.636459,8.162745,-7.518693,-1.279423,8.571597,-9.634462,5.037053,-0.169508,-8.825225,3.098329,8.279561,6.089965,8.332966,-8.035988,-7.036798,-6.594021,-1.499172,-7.613685,2.358429,-7.826999,-9.313355,-2.670429,-4.911220,1.375857,-0.444544,9.935804,-4.471147,6.042612,-9.352750,0.318764,5.793765,0.686129,8.145981,4.803843,-9.437046,5.518115,-1.191748,-8.821236,-7.862284,5.220426,5.764886,-4.402142,9.455227,6.246566,4.464613,-6.998615,0.953491,1.500080,8.489204,9.948489,-2.941426,1.772008,-5.936361,4.407407,6.232572,-7.524784,-0.332358,-0.750325,-4.450205,6.566160,-0.358603,1.121470,1.999793,-6.163229,7.322240,3.884238,4.783558,-8.671108,-1.907768,-1.032163,-9.294332,-6.146085,-8.839959,-0.668230,2.025257,-0.961227,3.225329,7.972794,-9.611792,-2.378185,5.670876,0.368230,-1.821489,6.217908,-9.554416,-2.041995,-8.435032,6.224711,5.698079,2.637522,3.266737,-9.590027,2.527819,-1.496786,8.580160,9.084983,-4.604642,2.976010,-6.351732,6.882104,9.877807,1.297070,2.868757,-4.517656,-5.053635,1.526463,5.633169,3.927270,5.816600,7.007208,-7.309868,5.081910,7.215763,8.182200,5.183812,-1.332108,-5.906061,-5.063145,-3.693482,-2.450876,7.525719,3.838862,8.898335,8.468808,-2.474563,7.173293,-7.880102,6.010686,-8.078460,1.480215,2.455233,-1.942722,-5.314922,2.919535,8.320779,6.001424,5.817169,5.181428,0.397596,6.696954,1.994452,-1.607526,-0.796879,-5.470868,-7.006177,-8.596478,6.413858,8.036826,-4.910697,8.254198,-7.243069,-3.150410,0.581009,-7.458890,-8.931131,-8.503061,5.684035,9.406287,-0.691300,-5.923364,-3.387799,-1.528175,8.739419,9.279598,7.905011,9.404284,3.293645,8.814371,3.350122,-1.864369,-4.663450,-1.348965,9.311442,1.636738,1.034066,8.844764,-9.689938,2.000068,0.843338,5.537984,0.515241,0.480876,-7.863347,7.751769,-8.894566,-1.444616,-3.626382,-5.973848,-3.420888,3.861550,4.946151,7.288948,5.604364,0.579798,0.223906,1.615622,1.919119,-8.363081,4.397604,-0.749721,3.717305,-5.528329,1.851671,7.446710,-5.158779,0.137236,5.505023,-7.006424,0.050813,-9.346994,-8.780208,-2.243929,-1.750525,-2.856328,-4.107703,6.842149,5.872207,-4.969674,1.572625,-3.403407,-5.813784,0.369711,3.524180,-3.375478,-6.855288,1.390338,-7.371271,-3.281282,-9.342291,2.116327,4.072323,-1.745491,-2.730417,0.061024,9.528212,-4.764248,3.552861,5.841901,5.576705], dtype = "float32")#candidate|15300|(546,)|const|float32
call_15298 = relay.TupleGetItem(func_7796_call(relay.reshape(const_15299.astype('float32'), []), relay.reshape(const_15300.astype('float32'), [13, 14, 3]), ), 2)
call_15301 = relay.TupleGetItem(func_7799_call(relay.reshape(const_15299.astype('float32'), []), relay.reshape(const_15300.astype('float32'), [13, 14, 3]), ), 2)
output = relay.Tuple([call_15292,call_15298,const_15299,const_15300,])
output2 = relay.Tuple([call_15293,call_15301,const_15299,const_15300,])
func_15317 = relay.Function([], output)
mod['func_15317'] = func_15317
mod = relay.transform.InferType()(mod)
mutated_mod['func_15317'] = func_15317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15317_call = mutated_mod.get_global_var('func_15317')
call_15318 = func_15317_call()
output = call_15318
func_15319 = relay.Function([], output)
mutated_mod['func_15319'] = func_15319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6296_call = mod.get_global_var('func_6296')
func_6297_call = mutated_mod.get_global_var('func_6297')
call_15333 = relay.TupleGetItem(func_6296_call(), 0)
call_15334 = relay.TupleGetItem(func_6297_call(), 0)
output = call_15333
output2 = call_15334
func_15352 = relay.Function([], output)
mod['func_15352'] = func_15352
mod = relay.transform.InferType()(mod)
output = func_15352()
func_15353 = relay.Function([], output)
mutated_mod['func_15353'] = func_15353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10898_call = mod.get_global_var('func_10898')
func_10899_call = mutated_mod.get_global_var('func_10899')
call_15357 = func_10898_call()
call_15358 = func_10898_call()
output = relay.Tuple([call_15357,])
output2 = relay.Tuple([call_15358,])
func_15360 = relay.Function([], output)
mod['func_15360'] = func_15360
mod = relay.transform.InferType()(mod)
output = func_15360()
func_15361 = relay.Function([], output)
mutated_mod['func_15361'] = func_15361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11187_call = mod.get_global_var('func_11187')
func_11188_call = mutated_mod.get_global_var('func_11188')
call_15364 = func_11187_call()
call_15365 = func_11187_call()
func_9579_call = mod.get_global_var('func_9579')
func_9581_call = mutated_mod.get_global_var('func_9581')
call_15371 = relay.TupleGetItem(func_9579_call(), 0)
call_15372 = relay.TupleGetItem(func_9581_call(), 0)
func_14595_call = mod.get_global_var('func_14595')
func_14597_call = mutated_mod.get_global_var('func_14597')
var_15382 = relay.var("var_15382", dtype = "bool", shape = (49,))#candidate|15382|(49,)|var|bool
call_15381 = func_14595_call(relay.reshape(var_15382.astype('bool'), [1, 7, 7]))
call_15383 = func_14595_call(relay.reshape(var_15382.astype('bool'), [1, 7, 7]))
bop_15403 = relay.add(var_15382.astype('uint16'), relay.reshape(call_15381.astype('uint16'), relay.shape_of(var_15382))) # shape=(49,)
bop_15406 = relay.add(var_15382.astype('uint16'), relay.reshape(call_15383.astype('uint16'), relay.shape_of(var_15382))) # shape=(49,)
func_5597_call = mod.get_global_var('func_5597')
func_5599_call = mutated_mod.get_global_var('func_5599')
var_15430 = relay.var("var_15430", dtype = "float64", shape = (96,))#candidate|15430|(96,)|var|float64
call_15429 = relay.TupleGetItem(func_5597_call(relay.reshape(var_15430.astype('float64'), [48, 2])), 2)
call_15431 = relay.TupleGetItem(func_5599_call(relay.reshape(var_15430.astype('float64'), [48, 2])), 2)
func_11514_call = mod.get_global_var('func_11514')
func_11516_call = mutated_mod.get_global_var('func_11516')
call_15432 = func_11514_call()
call_15433 = func_11514_call()
output = relay.Tuple([call_15364,call_15371,bop_15403,call_15429,var_15430,call_15432,])
output2 = relay.Tuple([call_15365,call_15372,bop_15406,call_15431,var_15430,call_15433,])
func_15436 = relay.Function([var_15382,var_15430,], output)
mod['func_15436'] = func_15436
mod = relay.transform.InferType()(mod)
var_15437 = relay.var("var_15437", dtype = "bool", shape = (49,))#candidate|15437|(49,)|var|bool
var_15438 = relay.var("var_15438", dtype = "float64", shape = (96,))#candidate|15438|(96,)|var|float64
output = func_15436(var_15437,var_15438,)
func_15439 = relay.Function([var_15437,var_15438,], output)
mutated_mod['func_15439'] = func_15439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10272_call = mod.get_global_var('func_10272')
func_10274_call = mutated_mod.get_global_var('func_10274')
call_15475 = relay.TupleGetItem(func_10272_call(), 1)
call_15476 = relay.TupleGetItem(func_10274_call(), 1)
output = relay.Tuple([call_15475,])
output2 = relay.Tuple([call_15476,])
func_15480 = relay.Function([], output)
mod['func_15480'] = func_15480
mod = relay.transform.InferType()(mod)
output = func_15480()
func_15481 = relay.Function([], output)
mutated_mod['func_15481'] = func_15481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10898_call = mod.get_global_var('func_10898')
func_10899_call = mutated_mod.get_global_var('func_10899')
call_15493 = func_10898_call()
call_15494 = func_10898_call()
output = relay.Tuple([call_15493,])
output2 = relay.Tuple([call_15494,])
func_15504 = relay.Function([], output)
mod['func_15504'] = func_15504
mod = relay.transform.InferType()(mod)
output = func_15504()
func_15505 = relay.Function([], output)
mutated_mod['func_15505'] = func_15505
mutated_mod = relay.transform.InferType()(mutated_mod)
const_15563 = relay.const([[[7.181603,-3.487398,2.822415,9.797302,4.724908,7.622890,-7.898591,-0.668116],[5.852573,6.722226,-7.027668,8.178858,-1.213423,4.478585,3.337520,4.270337],[4.204304,9.536092,-0.621895,-1.419506,0.489814,0.077818,-2.355898,1.663246],[5.631792,9.113987,-6.665683,-0.625830,-8.293886,-6.944748,-8.854522,-7.279778],[4.096882,-5.002050,-8.536450,7.428191,9.197172,-0.415250,-4.109219,8.661403],[-7.837872,-4.106635,7.883425,7.242640,-8.986637,7.544167,8.134492,-7.461808],[1.416566,9.097873,-4.633449,-9.677242,0.980900,7.915819,-2.348008,1.237899],[0.056511,8.916260,7.365645,3.234710,-4.957080,-2.647314,-8.978365,-7.031962],[-7.395377,-3.487523,-6.349559,-8.913520,2.926455,-9.554023,-4.506229,-1.788902],[0.112921,-1.351003,-8.815274,-7.006045,9.334479,-0.689965,-6.921464,9.618563]],[[-0.334215,1.962794,-6.420969,-4.719537,1.998224,5.456953,8.123182,-1.764327],[-1.974530,2.026569,-6.713967,6.418583,-3.595981,0.025159,3.998207,0.842865],[-3.761678,-2.890652,-9.953627,-8.960573,8.081767,5.768418,6.763896,0.174503],[3.647006,-8.066249,5.744647,3.482104,-9.340916,-5.347962,3.426115,5.495120],[-5.388764,4.909527,4.951333,-8.024785,9.987734,6.619152,8.342712,-7.795840],[3.053618,-3.745274,3.647613,-2.737305,7.948868,4.690248,6.753435,-7.315385],[-7.298554,-9.539903,-2.234431,1.962881,3.397598,-3.196930,3.204471,6.886298],[-5.348053,5.906850,3.822219,7.053199,-3.611273,4.358018,5.687178,2.253196],[0.509681,2.708425,1.121017,-3.528383,8.664337,6.470206,3.343419,2.023777],[6.593796,9.694406,5.181814,5.807307,7.930180,3.468881,-2.215714,9.909258]],[[-0.531647,0.423732,4.635921,-8.451663,0.551058,7.720225,-7.731748,-9.845408],[-9.602235,-4.746349,-1.257534,0.680777,0.992231,-2.200888,-9.188853,4.554821],[9.185117,-8.005850,-4.053728,6.322425,-0.503345,1.379049,-5.331330,-3.699538],[2.150044,-3.149832,-4.889180,-5.696984,-7.740775,-1.640437,-3.731911,1.353102],[-2.163084,-2.877323,8.237643,-2.218577,-8.423915,-2.881324,0.184515,6.236507],[-0.544567,-0.569644,-5.315178,-2.975977,-7.978913,9.891990,-7.135024,-1.829252],[-8.614923,-5.650414,-4.019473,9.054744,-8.152949,4.292382,3.707598,-4.871734],[-1.261512,-3.711716,8.913807,8.923273,6.683676,-6.835555,-2.422289,5.689489],[5.260494,-7.415124,-9.767944,4.617357,6.989088,6.281258,5.176358,-0.521240],[-2.365729,-6.689606,0.574506,4.533066,-0.072193,3.355644,-5.276896,5.514805]],[[-5.975940,-7.488532,-1.460889,8.258216,-0.416848,-9.603744,-4.439122,-6.347978],[9.933565,7.657032,-0.595219,-3.859845,-1.997870,2.844383,-1.396883,0.214640],[-4.328998,8.210733,9.662000,0.804280,5.998813,7.360767,-0.843485,7.553108],[4.547431,9.633819,4.341197,-8.006940,3.810508,7.501311,9.406148,-5.804631],[-8.224361,-6.659697,-1.547211,6.903607,6.069549,4.493723,-1.611630,9.176307],[5.735867,-3.608250,-0.333498,4.612905,-3.301135,3.237624,1.543497,-1.885561],[-1.681793,2.882564,-9.729381,-3.466946,1.606545,0.881700,-2.795714,4.783350],[8.299509,5.796750,2.276054,9.096383,3.886547,1.471137,-3.035837,-7.957351],[-3.847838,8.419408,-2.523999,-3.416191,-7.089754,-8.468172,-6.277504,-7.766555],[4.668366,-9.722133,-6.240558,-9.757375,-2.885371,-0.831908,9.202838,6.953501]],[[-4.061874,-9.438808,3.433375,4.445547,6.285241,-1.677138,3.695434,0.078160],[-2.737040,9.120367,-3.662676,-9.352763,0.157724,6.270927,5.259477,-5.226345],[-2.244370,8.783784,6.071087,8.453130,-4.353716,0.329184,-4.596177,-2.479886],[-9.514538,-7.314811,5.081891,3.759617,2.038608,-6.805488,-6.512700,3.841688],[1.281317,-0.867519,3.839545,0.221720,2.385608,4.423251,-1.928485,6.102837],[-7.150345,4.033212,-5.905680,-6.036153,6.911841,9.550468,-3.410997,-7.055060],[5.556488,-4.056445,-3.923142,-1.737996,-8.485886,-6.573780,0.834640,5.143375],[0.052032,8.286319,-5.828558,1.159684,-8.514123,1.103664,1.260063,9.807648],[-5.022895,2.040808,6.565047,-7.083931,-1.319050,-2.092812,-3.562815,4.487996],[-4.295315,-9.825243,-8.203648,1.110349,-1.057106,4.401751,-2.259707,-8.474395]],[[4.226983,-0.022314,5.012321,-3.320383,9.097957,3.541470,4.351348,0.421210],[9.975722,-2.028515,2.414171,6.019760,-0.411857,-7.205896,0.729754,6.767100],[-2.308330,3.032443,-9.730113,0.005465,0.227613,-4.877713,2.822320,-5.250806],[8.614224,7.335595,-7.640481,-3.720480,9.550400,-3.087021,5.873501,8.868593],[5.083829,7.168208,5.931277,0.086119,6.259082,2.825416,9.437007,8.634517],[-4.673245,9.987220,7.685524,0.256039,-1.002938,4.863917,2.981265,-6.304684],[-3.412371,-7.355127,-6.151590,-7.814428,5.602216,7.229952,5.441104,8.078331],[6.134553,5.126429,-7.328256,4.546412,-1.736091,-0.822594,-7.909033,-2.265701],[-0.324591,-0.137069,-7.337794,-9.604994,-4.581246,-9.809334,4.624013,6.038803],[-3.897320,2.935317,6.551782,-3.443687,-7.031238,6.095465,8.314178,6.436830]]], dtype = "float64")#candidate|15563|(6, 10, 8)|const|float64
uop_15564 = relay.asinh(const_15563.astype('float64')) # shape=(6, 10, 8)
bop_15572 = relay.floor_mod(uop_15564.astype('float64'), relay.reshape(const_15563.astype('float64'), relay.shape_of(uop_15564))) # shape=(6, 10, 8)
func_8295_call = mod.get_global_var('func_8295')
func_8296_call = mutated_mod.get_global_var('func_8296')
call_15578 = relay.TupleGetItem(func_8295_call(), 0)
call_15579 = relay.TupleGetItem(func_8296_call(), 0)
bop_15586 = relay.right_shift(uop_15564.astype('int64'), relay.reshape(bop_15572.astype('int64'), relay.shape_of(uop_15564))) # shape=(6, 10, 8)
output = relay.Tuple([call_15578,bop_15586,])
output2 = relay.Tuple([call_15579,bop_15586,])
F = relay.Function([], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([], output2)
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
