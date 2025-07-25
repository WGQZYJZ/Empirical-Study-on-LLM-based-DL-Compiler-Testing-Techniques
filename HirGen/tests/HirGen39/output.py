import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_284 = relay.var("var_284", dtype = "bool", shape = ())#candidate|284|()|var|bool
const_285 = relay.const([[[False,True,True,False,True,True,True,True],[False,False,False,True,False,True,False,True],[False,False,True,False,True,False,False,True],[False,True,False,False,True,True,False,False],[False,True,False,True,False,True,True,True],[True,True,False,True,False,False,True,True],[True,False,True,False,False,True,True,True],[True,False,True,False,True,True,False,False],[True,False,True,True,False,False,False,True],[True,True,True,False,True,False,True,False],[False,False,False,False,False,False,True,True]],[[False,False,True,True,False,False,True,True],[False,True,False,False,True,True,False,True],[False,True,True,True,True,False,False,True],[False,False,True,False,False,True,True,False],[True,True,False,True,True,True,False,True],[False,True,False,False,False,False,True,False],[True,False,True,False,False,True,True,False],[False,False,True,False,True,False,True,True],[True,True,False,False,False,True,False,True],[False,False,True,False,False,False,False,True],[False,True,True,False,True,False,False,True]],[[False,True,True,False,False,False,True,True],[True,True,False,False,False,False,True,False],[False,False,False,False,False,False,True,False],[False,False,False,True,False,False,False,False],[False,True,False,False,False,True,True,True],[True,True,True,True,True,False,False,True],[False,False,True,False,True,False,False,True],[False,False,False,False,True,False,True,True],[True,True,True,True,True,False,True,False],[False,False,True,True,True,True,True,True],[False,False,False,True,True,False,False,True]],[[True,False,False,False,False,True,True,True],[False,False,True,True,False,False,True,False],[False,True,False,True,False,True,True,False],[True,True,True,False,True,True,False,False],[True,False,False,True,True,True,True,True],[True,False,True,False,False,False,False,False],[True,False,False,False,True,True,False,True],[False,False,True,True,True,True,False,True],[True,False,False,False,False,True,False,True],[True,True,True,True,True,False,False,True],[False,False,True,False,True,True,True,True]],[[True,False,False,True,False,False,False,True],[True,False,False,True,False,False,False,True],[True,False,True,False,False,True,True,False],[True,False,False,False,False,True,True,True],[False,True,False,False,False,False,True,True],[True,True,False,True,True,False,False,False],[False,True,True,False,False,False,True,True],[True,True,True,True,True,False,False,True],[False,True,True,False,True,False,True,False],[False,True,True,True,True,False,False,False],[True,True,False,False,True,True,True,False]],[[True,True,True,False,True,False,True,True],[True,False,True,False,False,False,True,False],[True,False,False,True,False,False,True,False],[True,True,False,False,True,True,True,False],[False,False,False,False,False,True,True,True],[True,True,False,True,True,True,False,True],[True,False,False,False,False,True,False,True],[False,False,True,True,True,False,True,False],[True,True,False,True,False,True,True,True],[False,True,True,False,False,True,True,True],[True,True,True,True,False,True,False,False]]], dtype = "bool")#candidate|285|(6, 11, 8)|const|bool
bop_286 = relay.logical_and(var_284.astype('bool'), const_285.astype('bool')) # shape=(6, 11, 8)
output = bop_286
output2 = bop_286
func_289 = relay.Function([var_284,], output)
mod['func_289'] = func_289
mod = relay.transform.InferType()(mod)
var_290 = relay.var("var_290", dtype = "bool", shape = ())#candidate|290|()|var|bool
output = func_289(var_290)
func_291 = relay.Function([var_290], output)
mutated_mod['func_291'] = func_291
mutated_mod = relay.transform.InferType()(mutated_mod)
var_673 = relay.var("var_673", dtype = "float64", shape = (4, 3, 9))#candidate|673|(4, 3, 9)|var|float64
var_674 = relay.var("var_674", dtype = "float64", shape = (4, 3, 9))#candidate|674|(4, 3, 9)|var|float64
bop_675 = relay.floor_divide(var_673.astype('float64'), relay.reshape(var_674.astype('float64'), relay.shape_of(var_673))) # shape=(4, 3, 9)
func_289_call = mod.get_global_var('func_289')
func_291_call = mutated_mod.get_global_var('func_291')
const_681 = relay.const(False, dtype = "bool")#candidate|681|()|const|bool
call_680 = func_289_call(relay.reshape(const_681.astype('bool'), []))
call_682 = func_289_call(relay.reshape(const_681.astype('bool'), []))
func_289_call = mod.get_global_var('func_289')
func_291_call = mutated_mod.get_global_var('func_291')
call_684 = func_289_call(relay.reshape(const_681.astype('bool'), []))
call_685 = func_289_call(relay.reshape(const_681.astype('bool'), []))
output = relay.Tuple([bop_675,call_680,const_681,call_684,])
output2 = relay.Tuple([bop_675,call_682,const_681,call_685,])
func_696 = relay.Function([var_673,var_674,], output)
mod['func_696'] = func_696
mod = relay.transform.InferType()(mod)
var_697 = relay.var("var_697", dtype = "float64", shape = (4, 3, 9))#candidate|697|(4, 3, 9)|var|float64
var_698 = relay.var("var_698", dtype = "float64", shape = (4, 3, 9))#candidate|698|(4, 3, 9)|var|float64
output = func_696(var_697,var_698,)
func_699 = relay.Function([var_697,var_698,], output)
mutated_mod['func_699'] = func_699
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1236 = relay.const([[[True,False,False,True,False,False,True,True,True,True,True,True],[False,False,True,True,True,True,True,False,False,True,True,True],[False,False,False,False,True,True,False,True,True,False,False,True],[False,True,False,True,False,False,False,False,False,False,False,False],[True,True,False,False,True,False,True,True,False,True,True,True],[False,True,False,True,True,False,False,True,True,False,False,True],[False,True,False,True,True,False,True,False,True,True,False,False],[True,True,False,True,False,True,True,False,True,True,True,False]],[[False,True,False,True,False,False,True,False,True,True,True,False],[True,False,True,False,False,True,True,True,True,True,True,True],[False,False,False,True,True,True,False,True,True,False,True,True],[False,False,True,False,True,True,False,False,True,True,False,True],[True,True,True,False,False,False,True,True,False,True,False,True],[True,False,True,False,False,False,True,True,False,False,True,True],[True,True,True,True,True,True,False,False,True,True,False,True],[True,True,False,True,True,True,True,False,True,False,False,False]]], dtype = "bool")#candidate|1236|(2, 8, 12)|const|bool
const_1237 = relay.const([[[True,True,False,True,False,True,True,True,False,False,False,True],[False,False,False,False,False,False,True,False,False,True,True,True],[False,True,True,False,True,True,False,False,False,False,True,False],[True,False,True,True,False,False,False,True,False,True,True,True],[True,False,True,True,True,False,True,True,True,False,True,False],[True,True,False,True,True,True,True,False,False,False,True,False],[False,False,True,True,True,False,False,False,True,True,True,False],[True,False,False,False,False,True,False,True,True,False,False,False]],[[True,True,True,True,False,False,False,False,False,True,True,True],[False,True,True,True,False,True,True,True,True,True,True,False],[True,True,True,False,True,False,False,True,True,True,False,True],[False,False,False,False,False,True,False,False,True,True,True,True],[False,False,True,False,False,False,False,True,False,True,True,True],[True,True,False,True,True,True,False,True,True,False,True,True],[False,True,True,True,True,False,False,True,True,True,True,True],[False,True,False,False,True,True,True,False,False,False,True,True]]], dtype = "bool")#candidate|1237|(2, 8, 12)|const|bool
bop_1238 = relay.logical_and(const_1236.astype('bool'), relay.reshape(const_1237.astype('bool'), relay.shape_of(const_1236))) # shape=(2, 8, 12)
bop_1241 = relay.bitwise_and(const_1236.astype('int32'), relay.reshape(const_1237.astype('int32'), relay.shape_of(const_1236))) # shape=(2, 8, 12)
func_696_call = mod.get_global_var('func_696')
func_699_call = mutated_mod.get_global_var('func_699')
const_1246 = relay.const([-1.006597,4.327662,-2.222573,9.264396,-0.835104,-1.559559,1.387901,-2.909033,-6.905131,8.557867,-1.673252,2.136982,4.853662,-0.085489,6.200035,5.910648,-1.857751,2.901332,-1.619336,-6.367079,3.684305,7.916175,-2.995058,9.228838,2.509149,-0.029530,-4.789504,0.259516,-3.576208,-9.680193,-1.278189,6.955887,-1.972960,-7.972888,8.917940,5.664764,0.216752,1.308549,-8.162672,-1.595927,2.789264,1.468430,-6.818838,2.791825,3.565733,-0.133068,-2.280187,-3.584004,9.166198,8.550340,9.996848,8.107131,1.008281,5.729064,6.333457,-7.916782,-7.729950,-3.729992,-4.830833,9.924453,3.950349,9.653217,2.560601,-0.302483,-1.855319,2.869132,-5.176556,-1.864350,-7.034905,9.731009,0.492419,-5.557638,-8.180984,-5.598557,0.018728,-6.649436,-7.981351,-1.484294,0.415241,-1.909349,-3.622961,-6.727523,-3.129885,-6.162808,-2.614267,-8.077712,5.934318,5.644552,6.177382,-5.623826,-6.528359,3.709366,5.770239,-8.440419,-2.551570,-7.252445,8.411066,8.744944,-5.019768,-2.815195,4.732907,-6.313031,8.578845,-2.619112,-6.437866,2.020331,0.987991,8.229255], dtype = "float64")#candidate|1246|(108,)|const|float64
call_1245 = relay.TupleGetItem(func_696_call(relay.reshape(const_1246.astype('float64'), [4, 3, 9]), relay.reshape(const_1246.astype('float64'), [4, 3, 9]), ), 3)
call_1247 = relay.TupleGetItem(func_699_call(relay.reshape(const_1246.astype('float64'), [4, 3, 9]), relay.reshape(const_1246.astype('float64'), [4, 3, 9]), ), 3)
func_289_call = mod.get_global_var('func_289')
func_291_call = mutated_mod.get_global_var('func_291')
const_1264 = relay.const(False, dtype = "bool")#candidate|1264|()|const|bool
call_1263 = func_289_call(relay.reshape(const_1264.astype('bool'), []))
call_1265 = func_289_call(relay.reshape(const_1264.astype('bool'), []))
uop_1267 = relay.sqrt(const_1236.astype('float64')) # shape=(2, 8, 12)
output = relay.Tuple([bop_1238,bop_1241,call_1245,const_1246,call_1263,const_1264,uop_1267,])
output2 = relay.Tuple([bop_1238,bop_1241,call_1247,const_1246,call_1265,const_1264,uop_1267,])
func_1277 = relay.Function([], output)
mod['func_1277'] = func_1277
mod = relay.transform.InferType()(mod)
mutated_mod['func_1277'] = func_1277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1277_call = mutated_mod.get_global_var('func_1277')
call_1278 = func_1277_call()
output = call_1278
func_1279 = relay.Function([], output)
mutated_mod['func_1279'] = func_1279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1277_call = mod.get_global_var('func_1277')
func_1279_call = mutated_mod.get_global_var('func_1279')
call_1311 = relay.TupleGetItem(func_1277_call(), 5)
call_1312 = relay.TupleGetItem(func_1279_call(), 5)
func_1277_call = mod.get_global_var('func_1277')
func_1279_call = mutated_mod.get_global_var('func_1279')
call_1319 = relay.TupleGetItem(func_1277_call(), 0)
call_1320 = relay.TupleGetItem(func_1279_call(), 0)
uop_1332 = relay.sigmoid(call_1319.astype('float32')) # shape=(2, 8, 12)
uop_1334 = relay.sigmoid(call_1320.astype('float32')) # shape=(2, 8, 12)
output = relay.Tuple([call_1311,uop_1332,])
output2 = relay.Tuple([call_1312,uop_1334,])
func_1337 = relay.Function([], output)
mod['func_1337'] = func_1337
mod = relay.transform.InferType()(mod)
output = func_1337()
func_1338 = relay.Function([], output)
mutated_mod['func_1338'] = func_1338
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1339 = relay.var("var_1339", dtype = "float64", shape = (7, 12, 14))#candidate|1339|(7, 12, 14)|var|float64
var_1340 = relay.var("var_1340", dtype = "float64", shape = (7, 12, 14))#candidate|1340|(7, 12, 14)|var|float64
bop_1341 = relay.less(var_1339.astype('bool'), relay.reshape(var_1340.astype('bool'), relay.shape_of(var_1339))) # shape=(7, 12, 14)
func_1277_call = mod.get_global_var('func_1277')
func_1279_call = mutated_mod.get_global_var('func_1279')
call_1346 = relay.TupleGetItem(func_1277_call(), 5)
call_1347 = relay.TupleGetItem(func_1279_call(), 5)
output = relay.Tuple([bop_1341,call_1346,])
output2 = relay.Tuple([bop_1341,call_1347,])
func_1348 = relay.Function([var_1339,var_1340,], output)
mod['func_1348'] = func_1348
mod = relay.transform.InferType()(mod)
var_1349 = relay.var("var_1349", dtype = "float64", shape = (7, 12, 14))#candidate|1349|(7, 12, 14)|var|float64
var_1350 = relay.var("var_1350", dtype = "float64", shape = (7, 12, 14))#candidate|1350|(7, 12, 14)|var|float64
output = func_1348(var_1349,var_1350,)
func_1351 = relay.Function([var_1349,var_1350,], output)
mutated_mod['func_1351'] = func_1351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1277_call = mod.get_global_var('func_1277')
func_1279_call = mutated_mod.get_global_var('func_1279')
call_1404 = relay.TupleGetItem(func_1277_call(), 0)
call_1405 = relay.TupleGetItem(func_1279_call(), 0)
func_696_call = mod.get_global_var('func_696')
func_699_call = mutated_mod.get_global_var('func_699')
var_1409 = relay.var("var_1409", dtype = "float64", shape = (108,))#candidate|1409|(108,)|var|float64
call_1408 = relay.TupleGetItem(func_696_call(relay.reshape(var_1409.astype('float64'), [4, 3, 9]), relay.reshape(var_1409.astype('float64'), [4, 3, 9]), ), 3)
call_1410 = relay.TupleGetItem(func_699_call(relay.reshape(var_1409.astype('float64'), [4, 3, 9]), relay.reshape(var_1409.astype('float64'), [4, 3, 9]), ), 3)
var_1427 = relay.var("var_1427", dtype = "bool", shape = (2, 8, 12))#candidate|1427|(2, 8, 12)|var|bool
bop_1428 = relay.greater(call_1404.astype('bool'), relay.reshape(var_1427.astype('bool'), relay.shape_of(call_1404))) # shape=(2, 8, 12)
bop_1431 = relay.greater(call_1405.astype('bool'), relay.reshape(var_1427.astype('bool'), relay.shape_of(call_1405))) # shape=(2, 8, 12)
bop_1438 = relay.logical_xor(bop_1428.astype('int16'), relay.reshape(call_1404.astype('int16'), relay.shape_of(bop_1428))) # shape=(2, 8, 12)
bop_1441 = relay.logical_xor(bop_1431.astype('int16'), relay.reshape(call_1405.astype('int16'), relay.shape_of(bop_1431))) # shape=(2, 8, 12)
bop_1447 = relay.divide(var_1427.astype('float32'), relay.reshape(bop_1428.astype('float32'), relay.shape_of(var_1427))) # shape=(2, 8, 12)
bop_1450 = relay.divide(var_1427.astype('float32'), relay.reshape(bop_1431.astype('float32'), relay.shape_of(var_1427))) # shape=(2, 8, 12)
output = relay.Tuple([call_1408,var_1409,bop_1438,bop_1447,])
output2 = relay.Tuple([call_1410,var_1409,bop_1441,bop_1450,])
func_1460 = relay.Function([var_1409,var_1427,], output)
mod['func_1460'] = func_1460
mod = relay.transform.InferType()(mod)
mutated_mod['func_1460'] = func_1460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1460_call = mutated_mod.get_global_var('func_1460')
var_1462 = relay.var("var_1462", dtype = "float64", shape = (108,))#candidate|1462|(108,)|var|float64
var_1463 = relay.var("var_1463", dtype = "bool", shape = (2, 8, 12))#candidate|1463|(2, 8, 12)|var|bool
call_1461 = func_1460_call(var_1462,var_1463,)
output = call_1461
func_1464 = relay.Function([var_1462,var_1463,], output)
mutated_mod['func_1464'] = func_1464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1337_call = mod.get_global_var('func_1337')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_1471 = relay.TupleGetItem(func_1337_call(), 0)
call_1472 = relay.TupleGetItem(func_1338_call(), 0)
output = call_1471
output2 = call_1472
func_1498 = relay.Function([], output)
mod['func_1498'] = func_1498
mod = relay.transform.InferType()(mod)
mutated_mod['func_1498'] = func_1498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1498_call = mutated_mod.get_global_var('func_1498')
call_1499 = func_1498_call()
output = call_1499
func_1500 = relay.Function([], output)
mutated_mod['func_1500'] = func_1500
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1550 = relay.var("var_1550", dtype = "float32", shape = (3, 14, 2))#candidate|1550|(3, 14, 2)|var|float32
var_1551 = relay.var("var_1551", dtype = "float32", shape = (3, 14, 2))#candidate|1551|(3, 14, 2)|var|float32
bop_1552 = relay.subtract(var_1550.astype('float32'), relay.reshape(var_1551.astype('float32'), relay.shape_of(var_1550))) # shape=(3, 14, 2)
func_1337_call = mod.get_global_var('func_1337')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_1562 = relay.TupleGetItem(func_1337_call(), 1)
call_1563 = relay.TupleGetItem(func_1338_call(), 1)
func_289_call = mod.get_global_var('func_289')
func_291_call = mutated_mod.get_global_var('func_291')
var_1591 = relay.var("var_1591", dtype = "bool", shape = ())#candidate|1591|()|var|bool
call_1590 = func_289_call(relay.reshape(var_1591.astype('bool'), []))
call_1592 = func_289_call(relay.reshape(var_1591.astype('bool'), []))
bop_1596 = relay.logical_or(call_1590.astype('bool'), var_1591.astype('bool')) # shape=(6, 11, 8)
bop_1599 = relay.logical_or(call_1592.astype('bool'), var_1591.astype('bool')) # shape=(6, 11, 8)
output = relay.Tuple([bop_1552,call_1562,bop_1596,])
output2 = relay.Tuple([bop_1552,call_1563,bop_1599,])
func_1601 = relay.Function([var_1550,var_1551,var_1591,], output)
mod['func_1601'] = func_1601
mod = relay.transform.InferType()(mod)
mutated_mod['func_1601'] = func_1601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1601_call = mutated_mod.get_global_var('func_1601')
var_1603 = relay.var("var_1603", dtype = "float32", shape = (3, 14, 2))#candidate|1603|(3, 14, 2)|var|float32
var_1604 = relay.var("var_1604", dtype = "float32", shape = (3, 14, 2))#candidate|1604|(3, 14, 2)|var|float32
var_1605 = relay.var("var_1605", dtype = "bool", shape = ())#candidate|1605|()|var|bool
call_1602 = func_1601_call(var_1603,var_1604,var_1605,)
output = call_1602
func_1606 = relay.Function([var_1603,var_1604,var_1605,], output)
mutated_mod['func_1606'] = func_1606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1337_call = mod.get_global_var('func_1337')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_1634 = relay.TupleGetItem(func_1337_call(), 0)
call_1635 = relay.TupleGetItem(func_1338_call(), 0)
output = call_1634
output2 = call_1635
func_1636 = relay.Function([], output)
mod['func_1636'] = func_1636
mod = relay.transform.InferType()(mod)
mutated_mod['func_1636'] = func_1636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1636_call = mutated_mod.get_global_var('func_1636')
call_1637 = func_1636_call()
output = call_1637
func_1638 = relay.Function([], output)
mutated_mod['func_1638'] = func_1638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1498_call = mod.get_global_var('func_1498')
func_1500_call = mutated_mod.get_global_var('func_1500')
call_1653 = func_1498_call()
call_1654 = func_1498_call()
output = relay.Tuple([call_1653,])
output2 = relay.Tuple([call_1654,])
func_1665 = relay.Function([], output)
mod['func_1665'] = func_1665
mod = relay.transform.InferType()(mod)
mutated_mod['func_1665'] = func_1665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1665_call = mutated_mod.get_global_var('func_1665')
call_1666 = func_1665_call()
output = call_1666
func_1667 = relay.Function([], output)
mutated_mod['func_1667'] = func_1667
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1688 = relay.var("var_1688", dtype = "float32", shape = (6, 9, 13))#candidate|1688|(6, 9, 13)|var|float32
var_1689 = relay.var("var_1689", dtype = "float32", shape = (6, 9, 13))#candidate|1689|(6, 9, 13)|var|float32
bop_1690 = relay.mod(var_1688.astype('float32'), relay.reshape(var_1689.astype('float32'), relay.shape_of(var_1688))) # shape=(6, 9, 13)
bop_1693 = relay.logical_or(bop_1690.astype('bool'), relay.reshape(var_1688.astype('bool'), relay.shape_of(bop_1690))) # shape=(6, 9, 13)
uop_1707 = relay.asin(bop_1693.astype('float64')) # shape=(6, 9, 13)
output = uop_1707
output2 = uop_1707
func_1709 = relay.Function([var_1688,var_1689,], output)
mod['func_1709'] = func_1709
mod = relay.transform.InferType()(mod)
mutated_mod['func_1709'] = func_1709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1709_call = mutated_mod.get_global_var('func_1709')
var_1711 = relay.var("var_1711", dtype = "float32", shape = (6, 9, 13))#candidate|1711|(6, 9, 13)|var|float32
var_1712 = relay.var("var_1712", dtype = "float32", shape = (6, 9, 13))#candidate|1712|(6, 9, 13)|var|float32
call_1710 = func_1709_call(var_1711,var_1712,)
output = call_1710
func_1713 = relay.Function([var_1711,var_1712,], output)
mutated_mod['func_1713'] = func_1713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1665_call = mod.get_global_var('func_1665')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_1751 = relay.TupleGetItem(func_1665_call(), 0)
call_1752 = relay.TupleGetItem(func_1667_call(), 0)
output = relay.Tuple([call_1751,])
output2 = relay.Tuple([call_1752,])
func_1760 = relay.Function([], output)
mod['func_1760'] = func_1760
mod = relay.transform.InferType()(mod)
mutated_mod['func_1760'] = func_1760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1760_call = mutated_mod.get_global_var('func_1760')
call_1761 = func_1760_call()
output = call_1761
func_1762 = relay.Function([], output)
mutated_mod['func_1762'] = func_1762
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1766 = relay.const([[[-0.023386,6.146647,5.508928,5.819339,-9.426252,-3.325039,5.540282,-2.906539,9.298978,1.990441,-8.838586,-0.560809],[8.394448,-2.775314,-0.363414,-3.853385,-8.299576,-2.350291,8.029832,9.361914,4.718759,-7.991552,-3.880772,1.184402],[4.153589,0.213850,-2.049149,-6.282751,-2.495665,5.582632,-4.145875,-4.194219,3.300834,-9.513340,-7.786165,-6.416244],[-2.147099,-3.852993,1.057646,-4.100595,-7.094562,-6.242325,3.565055,-0.056002,2.524079,1.534117,-0.252854,-8.181609],[-4.234738,-6.018195,-2.087441,-6.280162,6.215900,7.882933,-5.657986,3.888809,8.123999,8.726668,-1.397644,8.497508],[1.078895,-6.647490,-1.238932,1.056709,0.436007,4.022906,-4.313067,-0.318899,-7.117051,-9.861270,9.600294,0.191864]],[[-3.233058,-8.212746,9.559541,-2.855625,-1.120659,-4.851706,-1.830552,0.372828,0.970599,9.567875,5.169945,7.480663],[-8.354853,-4.512958,-9.885763,-1.156236,9.509254,6.561789,-6.981031,3.718145,-7.737401,9.698588,-2.330433,3.953174],[9.774733,2.068442,-2.106549,-3.778964,4.592216,7.124832,1.180403,-8.898357,-2.471373,1.985638,7.244265,3.496358],[-6.644063,-8.883883,5.433352,-2.575296,6.674505,0.336396,-1.588407,-0.018413,5.199640,7.691386,1.412853,5.510710],[-2.597861,3.460373,0.514941,3.946059,0.612748,-0.130413,3.320565,-8.571205,8.653514,9.356932,0.672135,6.867213],[9.595545,0.792505,-5.332767,-8.029332,0.737311,-0.915556,-4.977703,-9.841036,-5.148803,-1.346759,6.033045,-8.940490]],[[8.850251,5.825393,6.584422,3.718230,1.661059,7.302972,0.222321,-7.123717,1.146658,1.217379,5.733596,-9.957205],[1.511680,6.847793,6.818331,2.979720,0.440269,1.134077,0.392910,5.865527,-6.290446,-1.663621,-8.610773,-7.566176],[2.826205,0.920447,-9.025412,-9.042465,0.965526,-6.199458,2.802282,2.304798,-2.220169,5.405642,4.059886,7.570042],[-7.908704,3.040038,-2.164006,-2.871986,7.300914,-8.531491,0.868465,0.491728,0.884977,9.710918,4.320421,1.059640],[-7.903881,2.968912,-5.584257,7.038006,-6.949287,8.433192,-2.461576,6.122142,-7.588196,6.131426,-3.326516,-7.642219],[3.293824,6.251203,-8.008394,-1.312948,5.862066,-6.137818,-4.040336,-9.866545,-0.491052,-4.967670,-4.588255,-2.121876]],[[8.974778,-2.930598,7.068809,0.453783,4.944397,3.825974,-1.553802,-1.908785,-7.841141,4.240370,-0.122499,6.592072],[1.380046,3.201358,7.195400,-2.434360,-5.386415,6.086603,8.391705,-6.314251,1.641646,-0.075208,9.503065,5.580147],[6.961366,6.041870,1.424203,-6.693612,-0.316586,-8.506783,-0.731817,-6.058031,3.094202,-6.011707,1.330859,2.548310],[-1.027757,-0.366738,-7.207606,3.660370,-5.057077,8.893161,-5.534884,-8.154294,-6.534301,-2.688175,-0.310428,4.838049],[-7.162613,-9.451032,-4.335466,-6.388267,-8.590485,-4.593612,3.937567,-0.276788,-4.175962,8.446318,-3.727484,3.175233],[-8.277314,4.175085,5.361951,-6.018287,-3.087733,4.161997,5.920180,4.879106,-3.478809,-9.440958,-9.903157,6.050126]],[[7.858323,1.423471,-1.935567,-8.928174,-5.602236,4.835707,-2.442645,-5.392597,5.089473,5.134792,0.317131,-4.216484],[-2.400195,4.566715,2.222049,-3.176845,2.420163,-4.723844,-0.638622,-9.079977,-2.505605,-8.037427,-0.822706,6.359731],[-3.128194,-9.356615,-8.847360,3.567381,2.906540,0.696511,2.152227,4.985216,3.759049,6.666655,-5.758113,-7.365319],[7.875978,2.399101,6.481025,1.200530,5.253529,-0.874442,-2.160623,7.652349,-3.403229,0.602750,-4.889399,8.041531],[-3.598729,5.809804,-4.061229,-5.373563,2.482216,7.966083,-3.265540,-6.570973,-2.341621,3.465590,3.603811,4.409484],[7.344046,2.705952,5.683154,8.740129,7.341930,9.291700,2.261110,-8.723746,4.774208,2.116293,-5.304494,-1.475108]],[[-4.230577,-6.668700,-2.037693,-0.172131,-5.856275,9.681642,-3.109823,8.991523,6.079481,1.820653,-2.414709,9.649147],[-5.556365,-7.136226,5.556455,9.187823,-4.628772,6.625931,9.892818,0.794890,7.285370,-6.555361,3.345361,-7.575320],[-2.890070,8.509497,8.980710,-7.005501,-7.256310,-6.020876,7.769463,7.224750,9.221970,-7.390950,-8.234752,-3.195496],[-7.337404,1.911485,5.702410,4.344909,-7.219923,-5.693222,8.383115,9.030220,3.163989,8.000978,2.784720,9.435238],[4.103174,-9.435574,5.016839,-4.551620,4.915651,4.484277,1.628316,-2.059640,-4.569538,4.249523,3.324499,6.053162],[-6.952795,-5.225557,9.253822,9.671615,0.144396,5.024529,-5.406279,4.527560,3.770969,-1.876134,0.438056,-3.665349]],[[-9.453201,9.274280,-2.936241,-3.284421,-0.695560,2.385661,-0.727285,-8.608663,-1.292075,-1.749407,7.669483,-3.388279],[8.670025,8.395013,6.336072,-2.584939,6.388096,2.000408,-2.685239,9.882008,-0.190994,-2.079005,1.736610,7.529921],[-8.736212,-7.009874,9.324689,1.855375,-6.228950,2.685324,-6.596471,2.202994,2.895554,-0.873564,-2.002754,-5.314811],[-3.324662,-9.376258,-9.146977,3.363646,7.630067,-1.854794,-3.566833,9.413356,3.407327,-6.903400,-0.134688,1.599819],[-1.693636,5.242033,3.217218,-0.326097,2.175165,7.588754,-6.554103,-0.861247,3.513761,-8.015168,-6.822049,-9.462699],[-4.007530,-0.654104,-2.504924,-1.234421,2.466232,1.636312,-7.060207,-1.243155,-5.267217,0.422397,-1.916679,7.455063]],[[-0.691787,4.468567,3.051509,-0.541772,-0.438251,0.596205,0.671444,8.069561,1.352728,1.077290,-0.648954,3.187628],[-0.542834,0.165374,0.632839,-7.418513,-4.238745,-6.007429,5.967452,3.569476,9.485713,-5.638207,0.657659,9.167921],[-2.117669,-9.966967,-9.614225,-8.166509,-1.176161,2.824667,-0.745251,2.130847,9.963032,-0.419568,7.236494,-1.459149],[-7.780968,5.934532,8.081066,7.409950,4.231427,-1.473858,9.362712,-5.418984,5.215892,5.538668,1.810429,-4.614353],[3.241260,1.036485,8.300011,3.434483,-1.936967,3.204910,-0.506819,-9.181284,-8.725909,3.200987,0.573938,3.447401],[-3.002949,-6.376044,9.953461,-0.018163,7.234162,5.659025,-4.833062,7.800179,1.203215,-0.667650,0.104338,-7.777589]],[[0.049374,0.895430,0.602230,7.372020,-9.145798,-1.714461,8.673420,-6.162183,-0.095643,6.700978,-7.056329,-4.546767],[0.285823,5.411338,1.769230,-0.044771,-1.931592,5.515890,-8.211738,0.028242,-1.669980,-3.369052,-9.453718,-2.841035],[8.978793,9.639777,-4.723335,0.687510,-3.702448,-4.075655,-9.692194,6.776436,1.653256,1.485287,8.421970,-4.652267],[-4.142243,0.100042,9.380372,5.434680,6.716466,-6.486756,-6.166020,8.313354,8.417561,-8.366931,-1.177169,-1.232153],[-7.190238,4.905089,-0.191017,2.073670,2.666567,1.332412,8.505784,9.141294,-8.770257,-2.217430,5.693030,9.052930],[-4.013141,9.708787,0.047807,-4.073442,6.650964,-5.545553,2.279857,-8.529540,-1.661202,0.697754,-5.654360,6.553585]],[[-3.679357,-7.539408,9.725032,-3.498577,6.352884,0.958295,4.512989,1.434980,0.675160,-4.291399,9.799262,0.557265],[6.155520,6.054557,7.612560,-6.969475,1.978856,-8.749243,-5.735903,-7.457322,-2.026631,8.840306,1.143074,-4.578149],[-7.413879,0.962516,7.789880,0.824239,6.289366,-9.626642,9.300587,-1.024337,8.459690,-6.895940,-7.785062,-6.730869],[-6.283703,-7.177520,-1.973680,-8.827475,-3.484951,-7.055721,1.336608,-2.206490,7.675053,1.370050,8.235595,0.469733],[-2.763086,-2.705483,-9.707108,9.009214,-3.406260,-9.462917,-4.557615,0.950202,-6.311432,-7.972822,-9.363497,-0.142351],[-6.762591,-7.243284,6.089244,-8.402200,1.776384,-1.909734,3.502670,-3.067992,-1.598232,-6.598795,-8.945384,0.358886]]], dtype = "float32")#candidate|1766|(10, 6, 12)|const|float32
uop_1767 = relay.cos(const_1766.astype('float32')) # shape=(10, 6, 12)
func_1760_call = mod.get_global_var('func_1760')
func_1762_call = mutated_mod.get_global_var('func_1762')
call_1770 = relay.TupleGetItem(func_1760_call(), 0)
call_1771 = relay.TupleGetItem(func_1762_call(), 0)
output = relay.Tuple([uop_1767,call_1770,])
output2 = relay.Tuple([uop_1767,call_1771,])
func_1776 = relay.Function([], output)
mod['func_1776'] = func_1776
mod = relay.transform.InferType()(mod)
output = func_1776()
func_1777 = relay.Function([], output)
mutated_mod['func_1777'] = func_1777
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1760_call = mod.get_global_var('func_1760')
func_1762_call = mutated_mod.get_global_var('func_1762')
call_1783 = relay.TupleGetItem(func_1760_call(), 0)
call_1784 = relay.TupleGetItem(func_1762_call(), 0)
func_1348_call = mod.get_global_var('func_1348')
func_1351_call = mutated_mod.get_global_var('func_1351')
var_1790 = relay.var("var_1790", dtype = "float64", shape = (1176,))#candidate|1790|(1176,)|var|float64
call_1789 = relay.TupleGetItem(func_1348_call(relay.reshape(var_1790.astype('float64'), [7, 12, 14]), relay.reshape(var_1790.astype('float64'), [7, 12, 14]), ), 1)
call_1791 = relay.TupleGetItem(func_1351_call(relay.reshape(var_1790.astype('float64'), [7, 12, 14]), relay.reshape(var_1790.astype('float64'), [7, 12, 14]), ), 1)
output = relay.Tuple([call_1783,call_1789,var_1790,])
output2 = relay.Tuple([call_1784,call_1791,var_1790,])
func_1796 = relay.Function([var_1790,], output)
mod['func_1796'] = func_1796
mod = relay.transform.InferType()(mod)
var_1797 = relay.var("var_1797", dtype = "float64", shape = (1176,))#candidate|1797|(1176,)|var|float64
output = func_1796(var_1797)
func_1798 = relay.Function([var_1797], output)
mutated_mod['func_1798'] = func_1798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1636_call = mod.get_global_var('func_1636')
func_1638_call = mutated_mod.get_global_var('func_1638')
call_1800 = func_1636_call()
call_1801 = func_1636_call()
output = call_1800
output2 = call_1801
func_1805 = relay.Function([], output)
mod['func_1805'] = func_1805
mod = relay.transform.InferType()(mod)
mutated_mod['func_1805'] = func_1805
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1805_call = mutated_mod.get_global_var('func_1805')
call_1806 = func_1805_call()
output = call_1806
func_1807 = relay.Function([], output)
mutated_mod['func_1807'] = func_1807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1277_call = mod.get_global_var('func_1277')
func_1279_call = mutated_mod.get_global_var('func_1279')
call_1826 = relay.TupleGetItem(func_1277_call(), 2)
call_1827 = relay.TupleGetItem(func_1279_call(), 2)
var_1833 = relay.var("var_1833", dtype = "bool", shape = (6, 11, 8))#candidate|1833|(6, 11, 8)|var|bool
bop_1834 = relay.right_shift(call_1826.astype('uint64'), relay.reshape(var_1833.astype('uint64'), relay.shape_of(call_1826))) # shape=(6, 11, 8)
bop_1837 = relay.right_shift(call_1827.astype('uint64'), relay.reshape(var_1833.astype('uint64'), relay.shape_of(call_1827))) # shape=(6, 11, 8)
func_1601_call = mod.get_global_var('func_1601')
func_1606_call = mutated_mod.get_global_var('func_1606')
const_1847 = relay.const([[-0.087150],[-2.218924],[6.819190],[-8.667673],[4.678033],[3.299089],[3.098831],[7.620855],[-0.440012],[-1.847125],[0.752569],[3.188780],[-7.412165],[-1.319771],[0.360069],[2.591816],[8.201791],[-5.879606],[-2.631890],[5.648460],[3.153169],[3.598878],[1.825392],[-4.756781],[-0.503890],[-3.873892],[4.424609],[2.624099],[-6.385456],[-7.440814],[8.179650],[5.824270],[7.127262],[8.161888],[-6.925226],[4.240410],[9.625517],[-2.149301],[-1.666662],[-5.999682],[3.143524],[-9.191682],[2.188972],[4.356091],[4.011823],[1.912605],[0.706005],[5.815627],[9.875816],[-0.480267],[8.004443],[0.242968],[0.821707],[9.718494],[-6.209563],[-4.784316],[-3.673477],[-5.469525],[-4.520921],[9.577837],[-8.785999],[-3.320808],[-4.282556],[-9.748463],[8.916879],[3.961756],[2.617245],[6.633197],[0.845964],[-0.413268],[5.492752],[9.787650],[4.281658],[2.956494],[4.198648],[9.521618],[3.314251],[4.491292],[2.498373],[5.604738],[3.311041],[7.470557],[9.051115],[3.500660]], dtype = "float32")#candidate|1847|(84, 1)|const|float32
var_1848 = relay.var("var_1848", dtype = "bool", shape = ())#candidate|1848|()|var|bool
call_1846 = relay.TupleGetItem(func_1601_call(relay.reshape(const_1847.astype('float32'), [3, 14, 2]), relay.reshape(const_1847.astype('float32'), [3, 14, 2]), relay.reshape(var_1848.astype('bool'), []), ), 2)
call_1849 = relay.TupleGetItem(func_1606_call(relay.reshape(const_1847.astype('float32'), [3, 14, 2]), relay.reshape(const_1847.astype('float32'), [3, 14, 2]), relay.reshape(var_1848.astype('bool'), []), ), 2)
output = relay.Tuple([bop_1834,call_1846,const_1847,var_1848,])
output2 = relay.Tuple([bop_1837,call_1849,const_1847,var_1848,])
func_1852 = relay.Function([var_1833,var_1848,], output)
mod['func_1852'] = func_1852
mod = relay.transform.InferType()(mod)
mutated_mod['func_1852'] = func_1852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1852_call = mutated_mod.get_global_var('func_1852')
var_1854 = relay.var("var_1854", dtype = "bool", shape = (6, 11, 8))#candidate|1854|(6, 11, 8)|var|bool
var_1855 = relay.var("var_1855", dtype = "bool", shape = ())#candidate|1855|()|var|bool
call_1853 = func_1852_call(var_1854,var_1855,)
output = call_1853
func_1856 = relay.Function([var_1854,var_1855,], output)
mutated_mod['func_1856'] = func_1856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1776_call = mod.get_global_var('func_1776')
func_1777_call = mutated_mod.get_global_var('func_1777')
call_1877 = relay.TupleGetItem(func_1776_call(), 0)
call_1878 = relay.TupleGetItem(func_1777_call(), 0)
output = relay.Tuple([call_1877,])
output2 = relay.Tuple([call_1878,])
func_1879 = relay.Function([], output)
mod['func_1879'] = func_1879
mod = relay.transform.InferType()(mod)
mutated_mod['func_1879'] = func_1879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1879_call = mutated_mod.get_global_var('func_1879')
call_1880 = func_1879_call()
output = call_1880
func_1881 = relay.Function([], output)
mutated_mod['func_1881'] = func_1881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1760_call = mod.get_global_var('func_1760')
func_1762_call = mutated_mod.get_global_var('func_1762')
call_1909 = relay.TupleGetItem(func_1760_call(), 0)
call_1910 = relay.TupleGetItem(func_1762_call(), 0)
output = call_1909
output2 = call_1910
func_1913 = relay.Function([], output)
mod['func_1913'] = func_1913
mod = relay.transform.InferType()(mod)
mutated_mod['func_1913'] = func_1913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1913_call = mutated_mod.get_global_var('func_1913')
call_1914 = func_1913_call()
output = call_1914
func_1915 = relay.Function([], output)
mutated_mod['func_1915'] = func_1915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1913_call = mod.get_global_var('func_1913')
func_1915_call = mutated_mod.get_global_var('func_1915')
call_1932 = func_1913_call()
call_1933 = func_1913_call()
output = call_1932
output2 = call_1933
func_1936 = relay.Function([], output)
mod['func_1936'] = func_1936
mod = relay.transform.InferType()(mod)
mutated_mod['func_1936'] = func_1936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1936_call = mutated_mod.get_global_var('func_1936')
call_1937 = func_1936_call()
output = call_1937
func_1938 = relay.Function([], output)
mutated_mod['func_1938'] = func_1938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1665_call = mod.get_global_var('func_1665')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_1942 = relay.TupleGetItem(func_1665_call(), 0)
call_1943 = relay.TupleGetItem(func_1667_call(), 0)
output = call_1942
output2 = call_1943
func_1957 = relay.Function([], output)
mod['func_1957'] = func_1957
mod = relay.transform.InferType()(mod)
mutated_mod['func_1957'] = func_1957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1957_call = mutated_mod.get_global_var('func_1957')
call_1958 = func_1957_call()
output = call_1958
func_1959 = relay.Function([], output)
mutated_mod['func_1959'] = func_1959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1636_call = mod.get_global_var('func_1636')
func_1638_call = mutated_mod.get_global_var('func_1638')
call_1989 = func_1636_call()
call_1990 = func_1636_call()
func_1665_call = mod.get_global_var('func_1665')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_2028 = relay.TupleGetItem(func_1665_call(), 0)
call_2029 = relay.TupleGetItem(func_1667_call(), 0)
output = relay.Tuple([call_1989,call_2028,])
output2 = relay.Tuple([call_1990,call_2029,])
func_2054 = relay.Function([], output)
mod['func_2054'] = func_2054
mod = relay.transform.InferType()(mod)
mutated_mod['func_2054'] = func_2054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2054_call = mutated_mod.get_global_var('func_2054')
call_2055 = func_2054_call()
output = call_2055
func_2056 = relay.Function([], output)
mutated_mod['func_2056'] = func_2056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1665_call = mod.get_global_var('func_1665')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_2059 = relay.TupleGetItem(func_1665_call(), 0)
call_2060 = relay.TupleGetItem(func_1667_call(), 0)
func_1277_call = mod.get_global_var('func_1277')
func_1279_call = mutated_mod.get_global_var('func_1279')
call_2086 = relay.TupleGetItem(func_1277_call(), 1)
call_2087 = relay.TupleGetItem(func_1279_call(), 1)
output = relay.Tuple([call_2059,call_2086,])
output2 = relay.Tuple([call_2060,call_2087,])
func_2094 = relay.Function([], output)
mod['func_2094'] = func_2094
mod = relay.transform.InferType()(mod)
mutated_mod['func_2094'] = func_2094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2094_call = mutated_mod.get_global_var('func_2094')
call_2095 = func_2094_call()
output = call_2095
func_2096 = relay.Function([], output)
mutated_mod['func_2096'] = func_2096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1636_call = mod.get_global_var('func_1636')
func_1638_call = mutated_mod.get_global_var('func_1638')
call_2101 = func_1636_call()
call_2102 = func_1636_call()
func_1776_call = mod.get_global_var('func_1776')
func_1777_call = mutated_mod.get_global_var('func_1777')
call_2115 = relay.TupleGetItem(func_1776_call(), 1)
call_2116 = relay.TupleGetItem(func_1777_call(), 1)
func_1805_call = mod.get_global_var('func_1805')
func_1807_call = mutated_mod.get_global_var('func_1807')
call_2117 = func_1805_call()
call_2118 = func_1805_call()
func_289_call = mod.get_global_var('func_289')
func_291_call = mutated_mod.get_global_var('func_291')
call_2127 = func_289_call(relay.reshape(call_2115.astype('bool'), []))
call_2128 = func_289_call(relay.reshape(call_2115.astype('bool'), []))
func_1498_call = mod.get_global_var('func_1498')
func_1500_call = mutated_mod.get_global_var('func_1500')
call_2132 = func_1498_call()
call_2133 = func_1498_call()
output = relay.Tuple([call_2101,call_2115,call_2117,call_2127,call_2132,])
output2 = relay.Tuple([call_2102,call_2116,call_2118,call_2128,call_2133,])
func_2148 = relay.Function([], output)
mod['func_2148'] = func_2148
mod = relay.transform.InferType()(mod)
output = func_2148()
func_2149 = relay.Function([], output)
mutated_mod['func_2149'] = func_2149
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2158 = relay.var("var_2158", dtype = "float64", shape = (9, 16, 9))#candidate|2158|(9, 16, 9)|var|float64
uop_2159 = relay.log2(var_2158.astype('float64')) # shape=(9, 16, 9)
func_1957_call = mod.get_global_var('func_1957')
func_1959_call = mutated_mod.get_global_var('func_1959')
call_2168 = func_1957_call()
call_2169 = func_1957_call()
output = relay.Tuple([uop_2159,call_2168,])
output2 = relay.Tuple([uop_2159,call_2169,])
func_2170 = relay.Function([var_2158,], output)
mod['func_2170'] = func_2170
mod = relay.transform.InferType()(mod)
mutated_mod['func_2170'] = func_2170
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2171 = relay.var("var_2171", dtype = "float64", shape = (9, 16, 9))#candidate|2171|(9, 16, 9)|var|float64
func_2170_call = mutated_mod.get_global_var('func_2170')
call_2172 = func_2170_call(var_2171)
output = call_2172
func_2173 = relay.Function([var_2171], output)
mutated_mod['func_2173'] = func_2173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2054_call = mod.get_global_var('func_2054')
func_2056_call = mutated_mod.get_global_var('func_2056')
call_2175 = relay.TupleGetItem(func_2054_call(), 1)
call_2176 = relay.TupleGetItem(func_2056_call(), 1)
func_1936_call = mod.get_global_var('func_1936')
func_1938_call = mutated_mod.get_global_var('func_1938')
call_2184 = func_1936_call()
call_2185 = func_1936_call()
func_1913_call = mod.get_global_var('func_1913')
func_1915_call = mutated_mod.get_global_var('func_1915')
call_2188 = func_1913_call()
call_2189 = func_1913_call()
output = relay.Tuple([call_2175,call_2184,call_2188,])
output2 = relay.Tuple([call_2176,call_2185,call_2189,])
func_2193 = relay.Function([], output)
mod['func_2193'] = func_2193
mod = relay.transform.InferType()(mod)
output = func_2193()
func_2194 = relay.Function([], output)
mutated_mod['func_2194'] = func_2194
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2278 = relay.var("var_2278", dtype = "int8", shape = (11, 6, 3))#candidate|2278|(11, 6, 3)|var|int8
var_2279 = relay.var("var_2279", dtype = "int8", shape = (11, 6, 3))#candidate|2279|(11, 6, 3)|var|int8
bop_2280 = relay.minimum(var_2278.astype('int8'), relay.reshape(var_2279.astype('int8'), relay.shape_of(var_2278))) # shape=(11, 6, 3)
func_289_call = mod.get_global_var('func_289')
func_291_call = mutated_mod.get_global_var('func_291')
const_2300 = relay.const(False, dtype = "bool")#candidate|2300|()|const|bool
call_2299 = func_289_call(relay.reshape(const_2300.astype('bool'), []))
call_2301 = func_289_call(relay.reshape(const_2300.astype('bool'), []))
func_1957_call = mod.get_global_var('func_1957')
func_1959_call = mutated_mod.get_global_var('func_1959')
call_2310 = func_1957_call()
call_2311 = func_1957_call()
output = relay.Tuple([bop_2280,call_2299,const_2300,call_2310,])
output2 = relay.Tuple([bop_2280,call_2301,const_2300,call_2311,])
func_2320 = relay.Function([var_2278,var_2279,], output)
mod['func_2320'] = func_2320
mod = relay.transform.InferType()(mod)
mutated_mod['func_2320'] = func_2320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2320_call = mutated_mod.get_global_var('func_2320')
var_2322 = relay.var("var_2322", dtype = "int8", shape = (11, 6, 3))#candidate|2322|(11, 6, 3)|var|int8
var_2323 = relay.var("var_2323", dtype = "int8", shape = (11, 6, 3))#candidate|2323|(11, 6, 3)|var|int8
call_2321 = func_2320_call(var_2322,var_2323,)
output = call_2321
func_2324 = relay.Function([var_2322,var_2323,], output)
mutated_mod['func_2324'] = func_2324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2054_call = mod.get_global_var('func_2054')
func_2056_call = mutated_mod.get_global_var('func_2056')
call_2343 = relay.TupleGetItem(func_2054_call(), 0)
call_2344 = relay.TupleGetItem(func_2056_call(), 0)
output = relay.Tuple([call_2343,])
output2 = relay.Tuple([call_2344,])
func_2366 = relay.Function([], output)
mod['func_2366'] = func_2366
mod = relay.transform.InferType()(mod)
output = func_2366()
func_2367 = relay.Function([], output)
mutated_mod['func_2367'] = func_2367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1636_call = mod.get_global_var('func_1636')
func_1638_call = mutated_mod.get_global_var('func_1638')
call_2399 = func_1636_call()
call_2400 = func_1636_call()
output = relay.Tuple([call_2399,])
output2 = relay.Tuple([call_2400,])
func_2406 = relay.Function([], output)
mod['func_2406'] = func_2406
mod = relay.transform.InferType()(mod)
mutated_mod['func_2406'] = func_2406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2406_call = mutated_mod.get_global_var('func_2406')
call_2407 = func_2406_call()
output = call_2407
func_2408 = relay.Function([], output)
mutated_mod['func_2408'] = func_2408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2406_call = mod.get_global_var('func_2406')
func_2408_call = mutated_mod.get_global_var('func_2408')
call_2427 = relay.TupleGetItem(func_2406_call(), 0)
call_2428 = relay.TupleGetItem(func_2408_call(), 0)
output = call_2427
output2 = call_2428
func_2446 = relay.Function([], output)
mod['func_2446'] = func_2446
mod = relay.transform.InferType()(mod)
output = func_2446()
func_2447 = relay.Function([], output)
mutated_mod['func_2447'] = func_2447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1936_call = mod.get_global_var('func_1936')
func_1938_call = mutated_mod.get_global_var('func_1938')
call_2505 = func_1936_call()
call_2506 = func_1936_call()
output = relay.Tuple([call_2505,])
output2 = relay.Tuple([call_2506,])
func_2521 = relay.Function([], output)
mod['func_2521'] = func_2521
mod = relay.transform.InferType()(mod)
output = func_2521()
func_2522 = relay.Function([], output)
mutated_mod['func_2522'] = func_2522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2094_call = mod.get_global_var('func_2094')
func_2096_call = mutated_mod.get_global_var('func_2096')
call_2523 = relay.TupleGetItem(func_2094_call(), 0)
call_2524 = relay.TupleGetItem(func_2096_call(), 0)
func_1460_call = mod.get_global_var('func_1460')
func_1464_call = mutated_mod.get_global_var('func_1464')
var_2536 = relay.var("var_2536", dtype = "float64", shape = (108,))#candidate|2536|(108,)|var|float64
const_2537 = relay.const([True,True,False,False,True,True,True,True,False,False,False,True,False,False,False,False,True,True,False,True,False,True,False,False,True,True,False,False,True,False,False,False,False,False,False,True,True,True,True,True,False,True,True,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,True,False,True,True,True,True,True,True,False,False,True,True,False,True,False,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,True,False,True,False,True,False,True,True,True,False,False,False,False,True,True,True,False,True,True,True,True,True,False,False,True,False,False,True,False,False,True,False,True,True,False,False,True,False,True,False,False,True,True,False,False,False,True,False,True,False,True,False,True,True,False,False,True,True,True,False,True,False,False,False,True,False,True,True,False,False,True,False,False,False,False,False,False,True,True,True,True,False,False,False,False,False,False,True,True,True,True,True,False,True,True,True,False,False,False,False,True,False,True], dtype = "bool")#candidate|2537|(192,)|const|bool
call_2535 = relay.TupleGetItem(func_1460_call(relay.reshape(var_2536.astype('float64'), [108,]), relay.reshape(const_2537.astype('bool'), [2, 8, 12]), ), 2)
call_2538 = relay.TupleGetItem(func_1464_call(relay.reshape(var_2536.astype('float64'), [108,]), relay.reshape(const_2537.astype('bool'), [2, 8, 12]), ), 2)
func_1498_call = mod.get_global_var('func_1498')
func_1500_call = mutated_mod.get_global_var('func_1500')
call_2540 = func_1498_call()
call_2541 = func_1498_call()
output = relay.Tuple([call_2523,call_2535,var_2536,const_2537,call_2540,])
output2 = relay.Tuple([call_2524,call_2538,var_2536,const_2537,call_2541,])
func_2545 = relay.Function([var_2536,], output)
mod['func_2545'] = func_2545
mod = relay.transform.InferType()(mod)
mutated_mod['func_2545'] = func_2545
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2546 = relay.var("var_2546", dtype = "float64", shape = (108,))#candidate|2546|(108,)|var|float64
func_2545_call = mutated_mod.get_global_var('func_2545')
call_2547 = func_2545_call(var_2546)
output = call_2547
func_2548 = relay.Function([var_2546], output)
mutated_mod['func_2548'] = func_2548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1957_call = mod.get_global_var('func_1957')
func_1959_call = mutated_mod.get_global_var('func_1959')
call_2562 = func_1957_call()
call_2563 = func_1957_call()
output = relay.Tuple([call_2562,])
output2 = relay.Tuple([call_2563,])
func_2628 = relay.Function([], output)
mod['func_2628'] = func_2628
mod = relay.transform.InferType()(mod)
output = func_2628()
func_2629 = relay.Function([], output)
mutated_mod['func_2629'] = func_2629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2628_call = mod.get_global_var('func_2628')
func_2629_call = mutated_mod.get_global_var('func_2629')
call_2660 = relay.TupleGetItem(func_2628_call(), 0)
call_2661 = relay.TupleGetItem(func_2629_call(), 0)
var_2664 = relay.var("var_2664", dtype = "bool", shape = (2, 10, 13))#candidate|2664|(2, 10, 13)|var|bool
bop_2665 = relay.add(call_2660.astype('int32'), var_2664.astype('int32')) # shape=(2, 10, 13)
bop_2668 = relay.add(call_2661.astype('int32'), var_2664.astype('int32')) # shape=(2, 10, 13)
bop_2670 = relay.subtract(call_2660.astype('uint16'), var_2664.astype('uint16')) # shape=(2, 10, 13)
bop_2673 = relay.subtract(call_2661.astype('uint16'), var_2664.astype('uint16')) # shape=(2, 10, 13)
output = relay.Tuple([bop_2665,bop_2670,])
output2 = relay.Tuple([bop_2668,bop_2673,])
func_2675 = relay.Function([var_2664,], output)
mod['func_2675'] = func_2675
mod = relay.transform.InferType()(mod)
var_2676 = relay.var("var_2676", dtype = "bool", shape = (2, 10, 13))#candidate|2676|(2, 10, 13)|var|bool
output = func_2675(var_2676)
func_2677 = relay.Function([var_2676], output)
mutated_mod['func_2677'] = func_2677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1337_call = mod.get_global_var('func_1337')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_2691 = relay.TupleGetItem(func_1337_call(), 0)
call_2692 = relay.TupleGetItem(func_1338_call(), 0)
output = call_2691
output2 = call_2692
func_2712 = relay.Function([], output)
mod['func_2712'] = func_2712
mod = relay.transform.InferType()(mod)
mutated_mod['func_2712'] = func_2712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2712_call = mutated_mod.get_global_var('func_2712')
call_2713 = func_2712_call()
output = call_2713
func_2714 = relay.Function([], output)
mutated_mod['func_2714'] = func_2714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2366_call = mod.get_global_var('func_2366')
func_2367_call = mutated_mod.get_global_var('func_2367')
call_2720 = relay.TupleGetItem(func_2366_call(), 0)
call_2721 = relay.TupleGetItem(func_2367_call(), 0)
func_289_call = mod.get_global_var('func_289')
func_291_call = mutated_mod.get_global_var('func_291')
call_2731 = func_289_call(relay.reshape(call_2720.astype('bool'), []))
call_2732 = func_289_call(relay.reshape(call_2720.astype('bool'), []))
func_289_call = mod.get_global_var('func_289')
func_291_call = mutated_mod.get_global_var('func_291')
call_2741 = func_289_call(relay.reshape(call_2720.astype('bool'), []))
call_2742 = func_289_call(relay.reshape(call_2720.astype('bool'), []))
uop_2743 = relay.sin(call_2731.astype('float64')) # shape=(6, 11, 8)
uop_2745 = relay.sin(call_2732.astype('float64')) # shape=(6, 11, 8)
func_1936_call = mod.get_global_var('func_1936')
func_1938_call = mutated_mod.get_global_var('func_1938')
call_2753 = func_1936_call()
call_2754 = func_1936_call()
func_1776_call = mod.get_global_var('func_1776')
func_1777_call = mutated_mod.get_global_var('func_1777')
call_2755 = relay.TupleGetItem(func_1776_call(), 1)
call_2756 = relay.TupleGetItem(func_1777_call(), 1)
func_1665_call = mod.get_global_var('func_1665')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_2760 = relay.TupleGetItem(func_1665_call(), 0)
call_2761 = relay.TupleGetItem(func_1667_call(), 0)
uop_2769 = relay.rsqrt(uop_2743.astype('float64')) # shape=(6, 11, 8)
uop_2771 = relay.rsqrt(uop_2745.astype('float64')) # shape=(6, 11, 8)
bop_2774 = relay.mod(uop_2769.astype('float64'), call_2753.astype('float64')) # shape=(6, 11, 8)
bop_2777 = relay.mod(uop_2771.astype('float64'), call_2754.astype('float64')) # shape=(6, 11, 8)
bop_2778 = relay.logical_xor(uop_2743.astype('int64'), relay.reshape(bop_2774.astype('int64'), relay.shape_of(uop_2743))) # shape=(6, 11, 8)
bop_2781 = relay.logical_xor(uop_2745.astype('int64'), relay.reshape(bop_2777.astype('int64'), relay.shape_of(uop_2745))) # shape=(6, 11, 8)
bop_2790 = relay.less_equal(uop_2769.astype('bool'), relay.reshape(bop_2778.astype('bool'), relay.shape_of(uop_2769))) # shape=(6, 11, 8)
bop_2793 = relay.less_equal(uop_2771.astype('bool'), relay.reshape(bop_2781.astype('bool'), relay.shape_of(uop_2771))) # shape=(6, 11, 8)
func_2446_call = mod.get_global_var('func_2446')
func_2447_call = mutated_mod.get_global_var('func_2447')
call_2796 = func_2446_call()
call_2797 = func_2446_call()
func_1957_call = mod.get_global_var('func_1957')
func_1959_call = mutated_mod.get_global_var('func_1959')
call_2801 = func_1957_call()
call_2802 = func_1957_call()
uop_2811 = relay.log(uop_2769.astype('float64')) # shape=(6, 11, 8)
uop_2813 = relay.log(uop_2771.astype('float64')) # shape=(6, 11, 8)
output = relay.Tuple([call_2720,call_2741,call_2755,call_2760,bop_2790,call_2796,call_2801,uop_2811,])
output2 = relay.Tuple([call_2721,call_2742,call_2756,call_2761,bop_2793,call_2797,call_2802,uop_2813,])
func_2820 = relay.Function([], output)
mod['func_2820'] = func_2820
mod = relay.transform.InferType()(mod)
output = func_2820()
func_2821 = relay.Function([], output)
mutated_mod['func_2821'] = func_2821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1498_call = mod.get_global_var('func_1498')
func_1500_call = mutated_mod.get_global_var('func_1500')
call_2827 = func_1498_call()
call_2828 = func_1498_call()
output = call_2827
output2 = call_2828
func_2858 = relay.Function([], output)
mod['func_2858'] = func_2858
mod = relay.transform.InferType()(mod)
output = func_2858()
func_2859 = relay.Function([], output)
mutated_mod['func_2859'] = func_2859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1498_call = mod.get_global_var('func_1498')
func_1500_call = mutated_mod.get_global_var('func_1500')
call_2909 = func_1498_call()
call_2910 = func_1498_call()
func_1636_call = mod.get_global_var('func_1636')
func_1638_call = mutated_mod.get_global_var('func_1638')
call_2921 = func_1636_call()
call_2922 = func_1636_call()
output = relay.Tuple([call_2909,call_2921,])
output2 = relay.Tuple([call_2910,call_2922,])
func_2923 = relay.Function([], output)
mod['func_2923'] = func_2923
mod = relay.transform.InferType()(mod)
mutated_mod['func_2923'] = func_2923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2923_call = mutated_mod.get_global_var('func_2923')
call_2924 = func_2923_call()
output = call_2924
func_2925 = relay.Function([], output)
mutated_mod['func_2925'] = func_2925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1337_call = mod.get_global_var('func_1337')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_2939 = relay.TupleGetItem(func_1337_call(), 0)
call_2940 = relay.TupleGetItem(func_1338_call(), 0)
output = relay.Tuple([call_2939,])
output2 = relay.Tuple([call_2940,])
func_2948 = relay.Function([], output)
mod['func_2948'] = func_2948
mod = relay.transform.InferType()(mod)
mutated_mod['func_2948'] = func_2948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2948_call = mutated_mod.get_global_var('func_2948')
call_2949 = func_2948_call()
output = call_2949
func_2950 = relay.Function([], output)
mutated_mod['func_2950'] = func_2950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1277_call = mod.get_global_var('func_1277')
func_1279_call = mutated_mod.get_global_var('func_1279')
call_2991 = relay.TupleGetItem(func_1277_call(), 6)
call_2992 = relay.TupleGetItem(func_1279_call(), 6)
uop_3000 = relay.acosh(call_2991.astype('float32')) # shape=(2, 8, 12)
uop_3002 = relay.acosh(call_2992.astype('float32')) # shape=(2, 8, 12)
func_1636_call = mod.get_global_var('func_1636')
func_1638_call = mutated_mod.get_global_var('func_1638')
call_3003 = func_1636_call()
call_3004 = func_1636_call()
bop_3008 = relay.less(call_3003.astype('bool'), uop_3000.astype('bool')) # shape=(2, 8, 12)
bop_3011 = relay.less(call_3004.astype('bool'), uop_3002.astype('bool')) # shape=(2, 8, 12)
bop_3017 = relay.greater_equal(uop_3000.astype('bool'), relay.reshape(call_2991.astype('bool'), relay.shape_of(uop_3000))) # shape=(2, 8, 12)
bop_3020 = relay.greater_equal(uop_3002.astype('bool'), relay.reshape(call_2992.astype('bool'), relay.shape_of(uop_3002))) # shape=(2, 8, 12)
func_1776_call = mod.get_global_var('func_1776')
func_1777_call = mutated_mod.get_global_var('func_1777')
call_3021 = relay.TupleGetItem(func_1776_call(), 1)
call_3022 = relay.TupleGetItem(func_1777_call(), 1)
uop_3041 = relay.sinh(uop_3000.astype('float64')) # shape=(2, 8, 12)
uop_3043 = relay.sinh(uop_3002.astype('float64')) # shape=(2, 8, 12)
output = relay.Tuple([bop_3008,bop_3017,call_3021,uop_3041,])
output2 = relay.Tuple([bop_3011,bop_3020,call_3022,uop_3043,])
func_3068 = relay.Function([], output)
mod['func_3068'] = func_3068
mod = relay.transform.InferType()(mod)
mutated_mod['func_3068'] = func_3068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3068_call = mutated_mod.get_global_var('func_3068')
call_3069 = func_3068_call()
output = call_3069
func_3070 = relay.Function([], output)
mutated_mod['func_3070'] = func_3070
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3190 = relay.const([[[-2.886325,4.248222,-0.745412,-6.260278,3.570993,-4.635432,-1.227550,6.963610,-7.912754,-6.506665,0.235759,5.763281,-8.876238,-1.769972,-8.653412]],[[1.820071,0.184224,-9.901132,1.662786,-9.704509,-2.456095,-5.992390,-9.926096,5.567368,-6.586512,-2.359415,-5.782481,8.176195,-3.348478,5.958116]],[[2.188779,4.330327,1.887574,-6.917030,-5.584547,1.920086,-9.307148,7.418064,-7.021809,5.015159,-3.272513,-1.343846,6.658957,4.647202,9.916585]],[[-0.559838,-0.593933,-3.195854,-7.173802,-7.078884,7.667515,3.110097,6.419321,-9.234558,0.207270,-5.199008,9.659777,-0.259250,-7.036752,-9.623508]],[[-5.809849,5.702487,-6.051822,-8.130848,-0.282017,6.862113,0.363121,2.708997,0.346012,-4.325393,-5.686874,-7.937947,3.156647,-9.087932,4.262714]],[[4.891434,-7.423146,-2.350408,-6.972669,9.949895,8.259743,2.830418,5.067607,9.353730,-2.412369,2.009398,-1.248781,8.915740,-1.428660,-4.803382]],[[-7.987191,-9.163531,-4.080486,-8.358786,8.458575,9.344387,-1.188686,2.708440,-8.202505,4.425461,-6.207281,6.254153,-4.652319,-0.802623,-0.536120]]], dtype = "float64")#candidate|3190|(7, 1, 15)|const|float64
uop_3191 = relay.sigmoid(const_3190.astype('float64')) # shape=(7, 1, 15)
func_696_call = mod.get_global_var('func_696')
func_699_call = mutated_mod.get_global_var('func_699')
const_3195 = relay.const([-4.363048,1.074028,6.926912,-9.649553,7.252250,-7.004026,0.829847,-1.083828,0.227827,-3.275676,-8.082139,8.948448,-6.874493,5.254540,-1.358524,-1.692464,-5.713234,-0.956542,1.476596,-6.854133,-5.810180,0.595978,-3.355479,-2.967522,7.845581,0.131586,5.167643,-2.981733,2.418011,9.755097,-7.760632,-6.917954,-0.097969,-9.112650,1.340267,-9.708756,5.406055,2.906061,6.960802,8.433160,9.423479,-8.009368,-8.688378,-3.884929,-4.971725,7.600445,5.920205,-6.921331,4.464286,3.987345,1.060460,-7.450514,5.343931,-8.021605,1.819086,-0.446925,-0.743083,4.509993,2.516126,-2.678305,-5.371819,-4.495208,7.156262,6.120736,-4.080272,4.952772,-6.277019,-8.973946,-5.663314,-4.882435,7.744166,-2.945280,8.093263,-1.989425,9.036448,6.844582,-7.539873,2.854127,-1.278831,-8.103902,1.875062,-8.137218,6.761473,-0.427249,3.182768,-7.096653,3.898119,-6.215874,-8.526129,4.402769,-0.803069,3.878310,-1.466166,-1.573308,9.097838,2.498408,0.090320,-5.674912,8.199420,-8.710297,6.865034,0.512421,0.076950,-8.795927,-5.689179,6.145366,-9.935726,3.449171], dtype = "float64")#candidate|3195|(108,)|const|float64
call_3194 = relay.TupleGetItem(func_696_call(relay.reshape(const_3195.astype('float64'), [4, 3, 9]), relay.reshape(const_3195.astype('float64'), [4, 3, 9]), ), 1)
call_3196 = relay.TupleGetItem(func_699_call(relay.reshape(const_3195.astype('float64'), [4, 3, 9]), relay.reshape(const_3195.astype('float64'), [4, 3, 9]), ), 1)
func_2446_call = mod.get_global_var('func_2446')
func_2447_call = mutated_mod.get_global_var('func_2447')
call_3200 = func_2446_call()
call_3201 = func_2446_call()
func_2193_call = mod.get_global_var('func_2193')
func_2194_call = mutated_mod.get_global_var('func_2194')
call_3202 = relay.TupleGetItem(func_2193_call(), 1)
call_3203 = relay.TupleGetItem(func_2194_call(), 1)
output = relay.Tuple([uop_3191,call_3194,const_3195,call_3200,call_3202,])
output2 = relay.Tuple([uop_3191,call_3196,const_3195,call_3201,call_3203,])
func_3204 = relay.Function([], output)
mod['func_3204'] = func_3204
mod = relay.transform.InferType()(mod)
output = func_3204()
func_3205 = relay.Function([], output)
mutated_mod['func_3205'] = func_3205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2858_call = mod.get_global_var('func_2858')
func_2859_call = mutated_mod.get_global_var('func_2859')
call_3279 = func_2858_call()
call_3280 = func_2858_call()
var_3292 = relay.var("var_3292", dtype = "bool", shape = (11, 8, 1))#candidate|3292|(11, 8, 1)|var|bool
bop_3293 = relay.greater(call_3279.astype('bool'), var_3292.astype('bool')) # shape=(11, 8, 1)
bop_3296 = relay.greater(call_3280.astype('bool'), var_3292.astype('bool')) # shape=(11, 8, 1)
func_2193_call = mod.get_global_var('func_2193')
func_2194_call = mutated_mod.get_global_var('func_2194')
call_3300 = relay.TupleGetItem(func_2193_call(), 1)
call_3301 = relay.TupleGetItem(func_2194_call(), 1)
func_696_call = mod.get_global_var('func_696')
func_699_call = mutated_mod.get_global_var('func_699')
const_3315 = relay.const([[-9.934753,2.124949,3.201659,6.206700,6.321362,-4.216599,6.160442,3.427759,-9.572530,1.054782,3.269533,8.453887,7.979829,7.981681,3.552759,3.964640,8.713755,-5.526012,-7.033489,-6.598736,6.448017,-6.359315,0.622333,-4.575113,2.667083,-8.309263,0.601775,-1.919738,-5.951539,-4.475904,9.309003,1.049338,-5.256716,3.593474,1.725848,-9.181694,4.975273,-7.756682,-4.559570,-7.625330,-9.411373,-3.883636,-2.595777,-0.429942,-2.693653,-6.656777,7.885654,-3.678624,4.893262,-5.605349,7.970221,-6.590137,0.211161,-6.955331,5.008797,-8.236742,1.611305,1.516028,6.079186,-1.292725,-7.537638,5.774337,-9.549866,7.758663,-4.402152,3.990635,-5.415927,-0.636694,-7.026230,8.556812,2.576018,8.109769,2.257265,-2.691095,4.791268,-6.305790,-0.083401,9.887370,-5.371772,-8.884828,-9.116905,-0.515387,4.021288,-1.887499,6.146117,1.454551,2.318762,0.178395,6.823664,-0.155560,-9.556660,-5.769451,-9.368255,-5.580439,-7.466625,4.736721,-2.103130,0.478821,-0.326641,3.578253,-4.013038,-1.920366,8.690679,-5.672442,-5.873044,1.878676,4.332289,4.751824]], dtype = "float64")#candidate|3315|(1, 108)|const|float64
call_3314 = relay.TupleGetItem(func_696_call(relay.reshape(const_3315.astype('float64'), [4, 3, 9]), relay.reshape(const_3315.astype('float64'), [4, 3, 9]), ), 1)
call_3316 = relay.TupleGetItem(func_699_call(relay.reshape(const_3315.astype('float64'), [4, 3, 9]), relay.reshape(const_3315.astype('float64'), [4, 3, 9]), ), 1)
output = relay.Tuple([bop_3293,call_3300,call_3314,const_3315,])
output2 = relay.Tuple([bop_3296,call_3301,call_3316,const_3315,])
func_3317 = relay.Function([var_3292,], output)
mod['func_3317'] = func_3317
mod = relay.transform.InferType()(mod)
var_3318 = relay.var("var_3318", dtype = "bool", shape = (11, 8, 1))#candidate|3318|(11, 8, 1)|var|bool
output = func_3317(var_3318)
func_3319 = relay.Function([var_3318], output)
mutated_mod['func_3319'] = func_3319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3204_call = mod.get_global_var('func_3204')
func_3205_call = mutated_mod.get_global_var('func_3205')
call_3329 = relay.TupleGetItem(func_3204_call(), 0)
call_3330 = relay.TupleGetItem(func_3205_call(), 0)
output = call_3329
output2 = call_3330
func_3347 = relay.Function([], output)
mod['func_3347'] = func_3347
mod = relay.transform.InferType()(mod)
mutated_mod['func_3347'] = func_3347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3347_call = mutated_mod.get_global_var('func_3347')
call_3348 = func_3347_call()
output = call_3348
func_3349 = relay.Function([], output)
mutated_mod['func_3349'] = func_3349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1277_call = mod.get_global_var('func_1277')
func_1279_call = mutated_mod.get_global_var('func_1279')
call_3436 = relay.TupleGetItem(func_1277_call(), 3)
call_3437 = relay.TupleGetItem(func_1279_call(), 3)
output = call_3436
output2 = call_3437
func_3453 = relay.Function([], output)
mod['func_3453'] = func_3453
mod = relay.transform.InferType()(mod)
mutated_mod['func_3453'] = func_3453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3453_call = mutated_mod.get_global_var('func_3453')
call_3454 = func_3453_call()
output = call_3454
func_3455 = relay.Function([], output)
mutated_mod['func_3455'] = func_3455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1665_call = mod.get_global_var('func_1665')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_3493 = relay.TupleGetItem(func_1665_call(), 0)
call_3494 = relay.TupleGetItem(func_1667_call(), 0)
func_1665_call = mod.get_global_var('func_1665')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_3495 = relay.TupleGetItem(func_1665_call(), 0)
call_3496 = relay.TupleGetItem(func_1667_call(), 0)
output = relay.Tuple([call_3493,call_3495,])
output2 = relay.Tuple([call_3494,call_3496,])
func_3498 = relay.Function([], output)
mod['func_3498'] = func_3498
mod = relay.transform.InferType()(mod)
output = func_3498()
func_3499 = relay.Function([], output)
mutated_mod['func_3499'] = func_3499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2948_call = mod.get_global_var('func_2948')
func_2950_call = mutated_mod.get_global_var('func_2950')
call_3512 = relay.TupleGetItem(func_2948_call(), 0)
call_3513 = relay.TupleGetItem(func_2950_call(), 0)
func_3347_call = mod.get_global_var('func_3347')
func_3349_call = mutated_mod.get_global_var('func_3349')
call_3521 = func_3347_call()
call_3522 = func_3347_call()
bop_3530 = relay.right_shift(call_3512.astype('uint16'), call_3521.astype('uint16')) # shape=(7, 1, 15)
bop_3533 = relay.right_shift(call_3513.astype('uint16'), call_3522.astype('uint16')) # shape=(7, 1, 15)
uop_3555 = relay.sinh(bop_3530.astype('float32')) # shape=(7, 1, 15)
uop_3557 = relay.sinh(bop_3533.astype('float32')) # shape=(7, 1, 15)
uop_3559 = relay.log(call_3521.astype('float64')) # shape=(7, 1, 15)
uop_3561 = relay.log(call_3522.astype('float64')) # shape=(7, 1, 15)
var_3562 = relay.var("var_3562", dtype = "uint16", shape = (7, 10, 15))#candidate|3562|(7, 10, 15)|var|uint16
bop_3563 = relay.divide(bop_3530.astype('float32'), var_3562.astype('float32')) # shape=(7, 10, 15)
bop_3566 = relay.divide(bop_3533.astype('float32'), var_3562.astype('float32')) # shape=(7, 10, 15)
uop_3575 = relay.acosh(var_3562.astype('float32')) # shape=(7, 10, 15)
output = relay.Tuple([uop_3555,uop_3559,bop_3563,uop_3575,])
output2 = relay.Tuple([uop_3557,uop_3561,bop_3566,uop_3575,])
func_3577 = relay.Function([var_3562,], output)
mod['func_3577'] = func_3577
mod = relay.transform.InferType()(mod)
mutated_mod['func_3577'] = func_3577
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3578 = relay.var("var_3578", dtype = "uint16", shape = (7, 10, 15))#candidate|3578|(7, 10, 15)|var|uint16
func_3577_call = mutated_mod.get_global_var('func_3577')
call_3579 = func_3577_call(var_3578)
output = call_3579
func_3580 = relay.Function([var_3578], output)
mutated_mod['func_3580'] = func_3580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2193_call = mod.get_global_var('func_2193')
func_2194_call = mutated_mod.get_global_var('func_2194')
call_3594 = relay.TupleGetItem(func_2193_call(), 0)
call_3595 = relay.TupleGetItem(func_2194_call(), 0)
output = relay.Tuple([call_3594,])
output2 = relay.Tuple([call_3595,])
func_3625 = relay.Function([], output)
mod['func_3625'] = func_3625
mod = relay.transform.InferType()(mod)
mutated_mod['func_3625'] = func_3625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3625_call = mutated_mod.get_global_var('func_3625')
call_3626 = func_3625_call()
output = call_3626
func_3627 = relay.Function([], output)
mutated_mod['func_3627'] = func_3627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2948_call = mod.get_global_var('func_2948')
func_2950_call = mutated_mod.get_global_var('func_2950')
call_3654 = relay.TupleGetItem(func_2948_call(), 0)
call_3655 = relay.TupleGetItem(func_2950_call(), 0)
func_696_call = mod.get_global_var('func_696')
func_699_call = mutated_mod.get_global_var('func_699')
const_3659 = relay.const([[2.971638],[-3.232196],[5.598229],[-4.162922],[0.932374],[8.823987],[-9.727479],[-3.940091],[4.224119],[-4.798712],[0.089566],[-6.616854],[9.253932],[-9.247390],[8.898206],[-1.807871],[8.478398],[-9.943619],[5.761743],[-2.650231],[0.347611],[-5.943152],[4.149369],[2.644385],[-8.934128],[7.522572],[-8.807911],[-8.638131],[4.528937],[0.800481],[9.444436],[4.091797],[2.878980],[5.060059],[9.068877],[6.758027],[-7.201078],[-7.696801],[-9.089085],[-1.302268],[9.540762],[3.902394],[6.589993],[8.891349],[-4.370762],[8.305635],[-0.292695],[-3.604582],[8.895959],[-9.819975],[3.874087],[8.149418],[1.892837],[2.412556],[1.150157],[-2.333138],[-6.738039],[-0.820258],[4.054542],[-5.160087],[8.088128],[3.660271],[0.308578],[8.261379],[-2.566883],[8.281900],[0.372454],[4.742429],[-7.490770],[-0.984824],[-1.084934],[-0.586660],[-9.738449],[-0.403064],[-0.594775],[-9.646623],[-6.221808],[2.397076],[6.476321],[-1.774049],[-4.421617],[-0.272278],[2.308891],[4.463123],[-0.055091],[5.529744],[-4.495789],[1.401629],[6.904875],[6.690452],[5.231226],[9.087878],[6.326537],[0.214783],[4.212870],[-8.720595],[4.174157],[7.251062],[-4.231722],[-5.336892],[-7.244031],[0.240820],[6.728558],[-8.956977],[-4.670993],[-7.227411],[6.847289],[-3.873605]], dtype = "float64")#candidate|3659|(108, 1)|const|float64
call_3658 = relay.TupleGetItem(func_696_call(relay.reshape(const_3659.astype('float64'), [4, 3, 9]), relay.reshape(const_3659.astype('float64'), [4, 3, 9]), ), 2)
call_3660 = relay.TupleGetItem(func_699_call(relay.reshape(const_3659.astype('float64'), [4, 3, 9]), relay.reshape(const_3659.astype('float64'), [4, 3, 9]), ), 2)
output = relay.Tuple([call_3654,call_3658,const_3659,])
output2 = relay.Tuple([call_3655,call_3660,const_3659,])
func_3667 = relay.Function([], output)
mod['func_3667'] = func_3667
mod = relay.transform.InferType()(mod)
output = func_3667()
func_3668 = relay.Function([], output)
mutated_mod['func_3668'] = func_3668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2406_call = mod.get_global_var('func_2406')
func_2408_call = mutated_mod.get_global_var('func_2408')
call_3749 = relay.TupleGetItem(func_2406_call(), 0)
call_3750 = relay.TupleGetItem(func_2408_call(), 0)
const_3756 = relay.const([[[True,False,True,True,False,False,True,True,False,False],[True,False,True,False,True,False,True,True,False,False],[True,False,True,True,True,True,False,True,False,True],[True,False,True,False,True,False,True,False,True,True],[True,False,True,False,False,True,False,False,False,True],[False,True,True,True,False,False,False,False,True,True],[False,False,True,True,True,False,True,False,False,True],[True,True,True,False,True,False,True,False,False,False],[True,False,True,False,False,False,False,False,False,False],[True,False,False,False,False,True,False,True,True,True],[False,False,False,False,True,False,False,False,False,False],[False,True,False,False,True,False,False,True,True,False]],[[True,False,True,False,True,True,True,True,False,True],[False,True,True,True,True,False,True,True,True,True],[True,True,False,True,True,True,False,True,False,True],[False,False,True,True,False,False,False,True,False,False],[False,False,True,False,True,False,False,False,True,True],[True,False,True,True,False,False,False,False,False,True],[True,False,True,False,True,True,True,True,False,True],[True,True,True,True,True,True,True,True,True,True],[True,True,True,False,False,True,False,True,True,False],[False,False,False,True,True,True,False,False,False,False],[True,False,True,False,True,False,True,False,False,True],[True,True,False,True,True,False,False,True,True,False]],[[False,True,False,False,False,True,False,False,True,False],[True,False,False,False,True,True,True,False,False,True],[True,True,False,True,False,True,False,True,False,True],[True,False,True,True,True,True,True,True,False,False],[True,True,True,False,True,False,True,False,False,True],[True,False,True,True,True,True,False,True,False,True],[True,True,True,False,True,False,True,False,True,True],[False,True,False,True,True,False,True,False,False,False],[False,False,False,True,True,True,False,False,True,True],[True,False,False,False,False,True,True,True,True,False],[True,False,True,True,True,False,True,True,True,False],[True,True,False,True,False,True,False,False,True,True]],[[True,False,True,False,True,True,True,False,True,True],[False,False,True,False,True,False,False,True,True,True],[True,False,False,True,True,False,False,False,True,False],[True,False,False,True,False,True,False,False,True,True],[True,False,True,False,False,True,False,False,False,False],[False,True,False,False,False,False,True,False,False,False],[False,True,False,True,False,True,False,True,True,False],[False,False,False,False,False,False,True,False,False,True],[False,False,False,True,True,False,True,False,False,True],[False,True,False,False,False,True,True,False,False,False],[False,False,False,False,False,False,False,True,True,True],[False,True,True,False,False,False,False,True,False,True]]], dtype = "bool")#candidate|3756|(4, 12, 10)|const|bool
bop_3757 = relay.equal(call_3749.astype('bool'), const_3756.astype('bool')) # shape=(4, 12, 10)
bop_3760 = relay.equal(call_3750.astype('bool'), const_3756.astype('bool')) # shape=(4, 12, 10)
output = bop_3757
output2 = bop_3760
func_3762 = relay.Function([], output)
mod['func_3762'] = func_3762
mod = relay.transform.InferType()(mod)
mutated_mod['func_3762'] = func_3762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3762_call = mutated_mod.get_global_var('func_3762')
call_3763 = func_3762_call()
output = call_3763
func_3764 = relay.Function([], output)
mutated_mod['func_3764'] = func_3764
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3778 = relay.var("var_3778", dtype = "float64", shape = (8, 14, 16))#candidate|3778|(8, 14, 16)|var|float64
uop_3779 = relay.cos(var_3778.astype('float64')) # shape=(8, 14, 16)
bop_3786 = relay.logical_xor(var_3778.astype('uint8'), relay.reshape(uop_3779.astype('uint8'), relay.shape_of(var_3778))) # shape=(8, 14, 16)
output = relay.Tuple([bop_3786,])
output2 = relay.Tuple([bop_3786,])
func_3794 = relay.Function([var_3778,], output)
mod['func_3794'] = func_3794
mod = relay.transform.InferType()(mod)
mutated_mod['func_3794'] = func_3794
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3795 = relay.var("var_3795", dtype = "float64", shape = (8, 14, 16))#candidate|3795|(8, 14, 16)|var|float64
func_3794_call = mutated_mod.get_global_var('func_3794')
call_3796 = func_3794_call(var_3795)
output = call_3796
func_3797 = relay.Function([var_3795], output)
mutated_mod['func_3797'] = func_3797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3762_call = mod.get_global_var('func_3762')
func_3764_call = mutated_mod.get_global_var('func_3764')
call_3841 = func_3762_call()
call_3842 = func_3762_call()
var_3846 = relay.var("var_3846", dtype = "bool", shape = (4, 12, 10))#candidate|3846|(4, 12, 10)|var|bool
bop_3847 = relay.bitwise_and(call_3841.astype('int8'), relay.reshape(var_3846.astype('int8'), relay.shape_of(call_3841))) # shape=(4, 12, 10)
bop_3850 = relay.bitwise_and(call_3842.astype('int8'), relay.reshape(var_3846.astype('int8'), relay.shape_of(call_3842))) # shape=(4, 12, 10)
uop_3851 = relay.acos(bop_3847.astype('float32')) # shape=(4, 12, 10)
uop_3853 = relay.acos(bop_3850.astype('float32')) # shape=(4, 12, 10)
output = relay.Tuple([uop_3851,])
output2 = relay.Tuple([uop_3853,])
func_3860 = relay.Function([var_3846,], output)
mod['func_3860'] = func_3860
mod = relay.transform.InferType()(mod)
var_3861 = relay.var("var_3861", dtype = "bool", shape = (4, 12, 10))#candidate|3861|(4, 12, 10)|var|bool
output = func_3860(var_3861)
func_3862 = relay.Function([var_3861], output)
mutated_mod['func_3862'] = func_3862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1879_call = mod.get_global_var('func_1879')
func_1881_call = mutated_mod.get_global_var('func_1881')
call_3872 = relay.TupleGetItem(func_1879_call(), 0)
call_3873 = relay.TupleGetItem(func_1881_call(), 0)
output = call_3872
output2 = call_3873
func_3877 = relay.Function([], output)
mod['func_3877'] = func_3877
mod = relay.transform.InferType()(mod)
mutated_mod['func_3877'] = func_3877
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3877_call = mutated_mod.get_global_var('func_3877')
call_3878 = func_3877_call()
output = call_3878
func_3879 = relay.Function([], output)
mutated_mod['func_3879'] = func_3879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2406_call = mod.get_global_var('func_2406')
func_2408_call = mutated_mod.get_global_var('func_2408')
call_3887 = relay.TupleGetItem(func_2406_call(), 0)
call_3888 = relay.TupleGetItem(func_2408_call(), 0)
func_1337_call = mod.get_global_var('func_1337')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_3891 = relay.TupleGetItem(func_1337_call(), 1)
call_3892 = relay.TupleGetItem(func_1338_call(), 1)
func_1957_call = mod.get_global_var('func_1957')
func_1959_call = mutated_mod.get_global_var('func_1959')
call_3896 = func_1957_call()
call_3897 = func_1957_call()
func_2545_call = mod.get_global_var('func_2545')
func_2548_call = mutated_mod.get_global_var('func_2548')
const_3903 = relay.const([6.215048,-0.759690,1.433225,6.392389,-7.278486,-8.876777,-6.127039,3.764059,-2.242585,-2.853272,3.102984,1.541002,-8.070886,1.587081,7.784956,-4.776733,9.294498,-4.286050,2.185438,-1.981426,-3.359380,-2.373302,-2.016150,5.781934,3.567171,-8.373415,-5.003379,-9.157778,0.747715,-6.793709,3.423311,6.001785,-1.052722,3.637328,-0.530975,4.152497,-2.099797,7.321406,4.241410,-2.044015,3.242373,6.059932,-0.901178,-9.435060,8.556169,-1.117491,0.160860,9.586899,5.842805,7.205230,-7.153375,-2.402142,-7.783825,2.039182,5.800605,-6.426763,4.286830,-9.249225,5.408028,3.127892,-0.528207,6.592734,-6.229738,2.726260,-6.164684,5.770492,4.167862,6.321086,5.748441,5.291422,-1.191353,8.924806,8.825135,0.260898,-1.330160,7.920804,-7.953876,-5.630681,4.254769,-6.886547,-4.954505,4.965342,-2.825606,1.880888,6.687310,-4.898520,1.213415,0.360515,3.549824,9.942154,-7.613499,-1.533996,-8.358483,8.415126,-6.104160,1.877019,1.631581,-2.384586,9.183371,3.217536,-7.615352,3.424229,-0.809733,-1.146869,5.597954,1.915043,-1.983788,2.634736], dtype = "float64")#candidate|3903|(108,)|const|float64
call_3902 = relay.TupleGetItem(func_2545_call(relay.reshape(const_3903.astype('float64'), [108,])), 4)
call_3904 = relay.TupleGetItem(func_2548_call(relay.reshape(const_3903.astype('float64'), [108,])), 4)
output = relay.Tuple([call_3887,call_3891,call_3896,call_3902,const_3903,])
output2 = relay.Tuple([call_3888,call_3892,call_3897,call_3904,const_3903,])
func_3906 = relay.Function([], output)
mod['func_3906'] = func_3906
mod = relay.transform.InferType()(mod)
mutated_mod['func_3906'] = func_3906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3906_call = mutated_mod.get_global_var('func_3906')
call_3907 = func_3906_call()
output = call_3907
func_3908 = relay.Function([], output)
mutated_mod['func_3908'] = func_3908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1277_call = mod.get_global_var('func_1277')
func_1279_call = mutated_mod.get_global_var('func_1279')
call_3965 = relay.TupleGetItem(func_1277_call(), 5)
call_3966 = relay.TupleGetItem(func_1279_call(), 5)
func_2521_call = mod.get_global_var('func_2521')
func_2522_call = mutated_mod.get_global_var('func_2522')
call_3967 = relay.TupleGetItem(func_2521_call(), 0)
call_3968 = relay.TupleGetItem(func_2522_call(), 0)
var_3970 = relay.var("var_3970", dtype = "bool", shape = (1, 8))#candidate|3970|(1, 8)|var|bool
bop_3971 = relay.divide(call_3967.astype('float32'), var_3970.astype('float32')) # shape=(1, 8)
bop_3974 = relay.divide(call_3968.astype('float32'), var_3970.astype('float32')) # shape=(1, 8)
func_2948_call = mod.get_global_var('func_2948')
func_2950_call = mutated_mod.get_global_var('func_2950')
call_3996 = relay.TupleGetItem(func_2948_call(), 0)
call_3997 = relay.TupleGetItem(func_2950_call(), 0)
func_1796_call = mod.get_global_var('func_1796')
func_1798_call = mutated_mod.get_global_var('func_1798')
var_4001 = relay.var("var_4001", dtype = "float64", shape = (1176,))#candidate|4001|(1176,)|var|float64
call_4000 = relay.TupleGetItem(func_1796_call(relay.reshape(var_4001.astype('float64'), [1176,])), 2)
call_4002 = relay.TupleGetItem(func_1798_call(relay.reshape(var_4001.astype('float64'), [1176,])), 2)
func_2545_call = mod.get_global_var('func_2545')
func_2548_call = mutated_mod.get_global_var('func_2548')
const_4017 = relay.const([-5.402938,-3.269010,-5.734724,-0.736213,-7.412553,-0.478462,9.172301,-1.061672,-3.372203,1.084634,4.505045,1.335042,-0.027255,-4.578729,9.581839,-1.259664,6.517206,7.320919,1.023840,8.999674,-0.588805,-7.644950,-4.254302,0.663709,-5.508043,-0.609115,-1.320489,-5.718179,-6.860775,-5.490650,-3.565305,9.816662,8.240065,7.752836,-5.884450,3.620238,-2.855696,0.718719,-9.020938,3.495803,9.065919,-9.233831,-8.181911,-0.090341,9.557695,-4.197697,3.776581,-8.006294,-6.836539,4.192529,-1.360460,-6.803792,1.030839,1.624920,-0.500957,-3.033261,-8.834411,-9.709233,1.953412,8.277947,3.793245,-8.766685,7.374294,-9.321234,-5.095097,6.667161,-5.448355,-3.439826,1.682368,9.399238,-2.949018,9.486713,-6.345046,3.559290,1.108463,-1.724668,-9.771785,2.061094,3.001645,-7.341914,-1.901757,-7.733170,6.466760,-8.710686,-7.170945,-8.423062,3.939324,6.124741,5.468072,7.193427,7.131880,-7.495176,7.288412,-0.528487,6.504717,-7.213692,-0.502530,-4.775343,2.013580,-6.316597,-2.872280,7.337994,-9.767002,7.906323,1.494739,-1.019291,-1.989470,7.968402], dtype = "float64")#candidate|4017|(108,)|const|float64
call_4016 = relay.TupleGetItem(func_2545_call(relay.reshape(const_4017.astype('float64'), [108,])), 0)
call_4018 = relay.TupleGetItem(func_2548_call(relay.reshape(const_4017.astype('float64'), [108,])), 0)
func_2148_call = mod.get_global_var('func_2148')
func_2149_call = mutated_mod.get_global_var('func_2149')
call_4021 = relay.TupleGetItem(func_2148_call(), 1)
call_4022 = relay.TupleGetItem(func_2149_call(), 1)
output = relay.Tuple([call_3965,bop_3971,call_3996,call_4000,var_4001,call_4016,const_4017,call_4021,])
output2 = relay.Tuple([call_3966,bop_3974,call_3997,call_4002,var_4001,call_4018,const_4017,call_4022,])
func_4041 = relay.Function([var_3970,var_4001,], output)
mod['func_4041'] = func_4041
mod = relay.transform.InferType()(mod)
var_4042 = relay.var("var_4042", dtype = "bool", shape = (1, 8))#candidate|4042|(1, 8)|var|bool
var_4043 = relay.var("var_4043", dtype = "float64", shape = (1176,))#candidate|4043|(1176,)|var|float64
output = func_4041(var_4042,var_4043,)
func_4044 = relay.Function([var_4042,var_4043,], output)
mutated_mod['func_4044'] = func_4044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1957_call = mod.get_global_var('func_1957')
func_1959_call = mutated_mod.get_global_var('func_1959')
call_4080 = func_1957_call()
call_4081 = func_1957_call()
output = relay.Tuple([call_4080,])
output2 = relay.Tuple([call_4081,])
func_4084 = relay.Function([], output)
mod['func_4084'] = func_4084
mod = relay.transform.InferType()(mod)
output = func_4084()
func_4085 = relay.Function([], output)
mutated_mod['func_4085'] = func_4085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2148_call = mod.get_global_var('func_2148')
func_2149_call = mutated_mod.get_global_var('func_2149')
call_4104 = relay.TupleGetItem(func_2148_call(), 4)
call_4105 = relay.TupleGetItem(func_2149_call(), 4)
func_3667_call = mod.get_global_var('func_3667')
func_3668_call = mutated_mod.get_global_var('func_3668')
call_4122 = relay.TupleGetItem(func_3667_call(), 0)
call_4123 = relay.TupleGetItem(func_3668_call(), 0)
output = relay.Tuple([call_4104,call_4122,])
output2 = relay.Tuple([call_4105,call_4123,])
func_4130 = relay.Function([], output)
mod['func_4130'] = func_4130
mod = relay.transform.InferType()(mod)
output = func_4130()
func_4131 = relay.Function([], output)
mutated_mod['func_4131'] = func_4131
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4138 = relay.var("var_4138", dtype = "float64", shape = (9, 10, 3))#candidate|4138|(9, 10, 3)|var|float64
var_4139 = relay.var("var_4139", dtype = "float64", shape = (9, 10, 3))#candidate|4139|(9, 10, 3)|var|float64
bop_4140 = relay.floor_divide(var_4138.astype('float64'), relay.reshape(var_4139.astype('float64'), relay.shape_of(var_4138))) # shape=(9, 10, 3)
func_4084_call = mod.get_global_var('func_4084')
func_4085_call = mutated_mod.get_global_var('func_4085')
call_4147 = relay.TupleGetItem(func_4084_call(), 0)
call_4148 = relay.TupleGetItem(func_4085_call(), 0)
output = relay.Tuple([bop_4140,call_4147,])
output2 = relay.Tuple([bop_4140,call_4148,])
func_4153 = relay.Function([var_4138,var_4139,], output)
mod['func_4153'] = func_4153
mod = relay.transform.InferType()(mod)
var_4154 = relay.var("var_4154", dtype = "float64", shape = (9, 10, 3))#candidate|4154|(9, 10, 3)|var|float64
var_4155 = relay.var("var_4155", dtype = "float64", shape = (9, 10, 3))#candidate|4155|(9, 10, 3)|var|float64
output = func_4153(var_4154,var_4155,)
func_4156 = relay.Function([var_4154,var_4155,], output)
mutated_mod['func_4156'] = func_4156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1957_call = mod.get_global_var('func_1957')
func_1959_call = mutated_mod.get_global_var('func_1959')
call_4204 = func_1957_call()
call_4205 = func_1957_call()
func_1796_call = mod.get_global_var('func_1796')
func_1798_call = mutated_mod.get_global_var('func_1798')
var_4212 = relay.var("var_4212", dtype = "float64", shape = (1176,))#candidate|4212|(1176,)|var|float64
call_4211 = relay.TupleGetItem(func_1796_call(relay.reshape(var_4212.astype('float64'), [1176,])), 0)
call_4213 = relay.TupleGetItem(func_1798_call(relay.reshape(var_4212.astype('float64'), [1176,])), 0)
func_3204_call = mod.get_global_var('func_3204')
func_3205_call = mutated_mod.get_global_var('func_3205')
call_4218 = relay.TupleGetItem(func_3204_call(), 2)
call_4219 = relay.TupleGetItem(func_3205_call(), 2)
output = relay.Tuple([call_4204,call_4211,var_4212,call_4218,])
output2 = relay.Tuple([call_4205,call_4213,var_4212,call_4219,])
func_4222 = relay.Function([var_4212,], output)
mod['func_4222'] = func_4222
mod = relay.transform.InferType()(mod)
var_4223 = relay.var("var_4223", dtype = "float64", shape = (1176,))#candidate|4223|(1176,)|var|float64
output = func_4222(var_4223)
func_4224 = relay.Function([var_4223], output)
mutated_mod['func_4224'] = func_4224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1913_call = mod.get_global_var('func_1913')
func_1915_call = mutated_mod.get_global_var('func_1915')
call_4226 = func_1913_call()
call_4227 = func_1913_call()
func_1913_call = mod.get_global_var('func_1913')
func_1915_call = mutated_mod.get_global_var('func_1915')
call_4232 = func_1913_call()
call_4233 = func_1913_call()
output = relay.Tuple([call_4226,call_4232,])
output2 = relay.Tuple([call_4227,call_4233,])
func_4237 = relay.Function([], output)
mod['func_4237'] = func_4237
mod = relay.transform.InferType()(mod)
output = func_4237()
func_4238 = relay.Function([], output)
mutated_mod['func_4238'] = func_4238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2858_call = mod.get_global_var('func_2858')
func_2859_call = mutated_mod.get_global_var('func_2859')
call_4242 = func_2858_call()
call_4243 = func_2858_call()
output = relay.Tuple([call_4242,])
output2 = relay.Tuple([call_4243,])
func_4244 = relay.Function([], output)
mod['func_4244'] = func_4244
mod = relay.transform.InferType()(mod)
output = func_4244()
func_4245 = relay.Function([], output)
mutated_mod['func_4245'] = func_4245
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4258 = relay.var("var_4258", dtype = "float64", shape = (6, 2, 4))#candidate|4258|(6, 2, 4)|var|float64
uop_4259 = relay.tan(var_4258.astype('float64')) # shape=(6, 2, 4)
bop_4265 = relay.mod(uop_4259.astype('float32'), relay.reshape(var_4258.astype('float32'), relay.shape_of(uop_4259))) # shape=(6, 2, 4)
func_1636_call = mod.get_global_var('func_1636')
func_1638_call = mutated_mod.get_global_var('func_1638')
call_4277 = func_1636_call()
call_4278 = func_1636_call()
func_1348_call = mod.get_global_var('func_1348')
func_1351_call = mutated_mod.get_global_var('func_1351')
var_4283 = relay.var("var_4283", dtype = "float64", shape = (1, 1176))#candidate|4283|(1, 1176)|var|float64
call_4282 = relay.TupleGetItem(func_1348_call(relay.reshape(var_4283.astype('float64'), [7, 12, 14]), relay.reshape(var_4283.astype('float64'), [7, 12, 14]), ), 0)
call_4284 = relay.TupleGetItem(func_1351_call(relay.reshape(var_4283.astype('float64'), [7, 12, 14]), relay.reshape(var_4283.astype('float64'), [7, 12, 14]), ), 0)
func_3453_call = mod.get_global_var('func_3453')
func_3455_call = mutated_mod.get_global_var('func_3455')
call_4285 = func_3453_call()
call_4286 = func_3453_call()
output = relay.Tuple([bop_4265,call_4277,call_4282,var_4283,call_4285,])
output2 = relay.Tuple([bop_4265,call_4278,call_4284,var_4283,call_4286,])
func_4298 = relay.Function([var_4258,var_4283,], output)
mod['func_4298'] = func_4298
mod = relay.transform.InferType()(mod)
mutated_mod['func_4298'] = func_4298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4298_call = mutated_mod.get_global_var('func_4298')
var_4300 = relay.var("var_4300", dtype = "float64", shape = (6, 2, 4))#candidate|4300|(6, 2, 4)|var|float64
var_4301 = relay.var("var_4301", dtype = "float64", shape = (1, 1176))#candidate|4301|(1, 1176)|var|float64
call_4299 = func_4298_call(var_4300,var_4301,)
output = call_4299
func_4302 = relay.Function([var_4300,var_4301,], output)
mutated_mod['func_4302'] = func_4302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3762_call = mod.get_global_var('func_3762')
func_3764_call = mutated_mod.get_global_var('func_3764')
call_4339 = func_3762_call()
call_4340 = func_3762_call()
output = call_4339
output2 = call_4340
func_4349 = relay.Function([], output)
mod['func_4349'] = func_4349
mod = relay.transform.InferType()(mod)
mutated_mod['func_4349'] = func_4349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4349_call = mutated_mod.get_global_var('func_4349')
call_4350 = func_4349_call()
output = call_4350
func_4351 = relay.Function([], output)
mutated_mod['func_4351'] = func_4351
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4440 = relay.const([[[10,-10,-4,2,-2,5,-6],[-5,-1,7,-1,-3,-6,-3],[3,-5,-6,8,9,7,5],[-9,-1,9,7,-5,8,5],[-2,-1,4,10,2,-9,7],[2,8,-4,-10,-2,6,-7],[-7,10,-3,-8,8,9,5],[-1,-4,4,-6,2,1,5],[5,-4,6,-4,7,-6,-10],[-3,2,5,8,-1,-8,-2],[-9,8,9,-6,6,-4,4],[7,4,6,3,6,-3,-8],[2,-1,7,6,-1,-10,4],[9,-3,-1,6,7,-1,3],[-1,-4,-2,-3,4,6,-4],[2,2,8,-10,4,-8,-7]],[[5,-2,10,-9,-5,-1,4],[4,-4,5,-2,1,4,7],[-8,3,-4,-10,-5,9,1],[-8,-9,-2,1,-1,2,4],[-1,8,-5,3,-7,8,-1],[-9,8,5,2,-2,-5,-7],[-5,3,-1,-5,3,10,10],[2,-2,4,-10,7,6,-6],[-2,-10,-1,-3,3,3,-8],[5,-8,1,-8,1,-6,2],[10,5,-9,9,7,6,-1],[-7,9,-9,9,-8,7,-6],[10,6,-6,-9,5,8,-1],[-5,3,-3,4,-9,4,-1],[-9,-3,-7,-8,-10,-7,-5],[1,9,-8,8,5,3,-6]],[[-3,9,5,10,1,-4,-3],[7,8,-5,4,9,7,3],[-8,-9,7,3,-10,-4,1],[1,3,-3,6,7,-5,1],[2,4,-2,-3,2,2,10],[-4,-6,-6,-5,-9,9,2],[-4,-8,8,8,-6,10,8],[-2,8,9,1,2,-4,-6],[6,-9,-2,7,-10,9,-6],[5,-10,4,1,1,-1,-5],[-1,2,-2,8,-9,-3,1],[-4,-2,3,-4,-10,-2,-6],[-4,-8,5,-4,10,-10,-8],[9,-4,6,-1,-7,-6,1],[-10,1,-1,2,-10,2,10],[-10,-2,10,1,3,-7,-9]],[[9,-2,-1,6,-3,-6,7],[-4,10,9,-4,-10,-5,9],[5,-6,9,7,3,10,2],[-1,-5,-5,-1,-7,-3,10],[-3,-1,-6,-5,7,5,-3],[-7,4,-3,-3,4,-5,8],[9,8,-6,10,-10,-7,5],[8,-10,5,3,10,8,-9],[-4,-5,-5,-5,-5,-3,10],[-3,-5,-4,-6,-6,9,-4],[-10,4,-9,9,1,7,10],[1,1,8,-5,-8,3,1],[-1,-1,-7,7,3,2,-1],[-9,6,-3,-4,-2,5,-1],[3,10,-4,-5,7,8,7],[3,-6,10,-4,10,4,-6]],[[-1,7,6,8,-10,2,-4],[-9,-10,-10,7,-10,-3,-9],[-2,5,-2,9,-2,10,9],[-3,-4,-7,-7,1,-7,4],[-3,6,-10,1,5,-9,-5],[1,3,-1,4,-1,5,4],[-5,9,-5,-3,5,-4,4],[-7,4,-6,-10,4,-5,7],[-9,9,1,-1,-2,-1,10],[7,-1,-4,-10,4,7,6],[-6,-9,3,-8,5,-3,6],[4,-1,4,5,9,-8,7],[-4,5,-5,-3,-2,5,2],[6,3,-8,1,6,-9,1],[-9,-3,1,-1,4,-5,6],[-6,9,8,2,-6,-7,-8]],[[9,-2,-6,-1,2,-3,7],[5,-9,4,2,2,10,-8],[-4,1,-6,4,-9,8,7],[10,-1,-9,-7,-8,7,-5],[-2,3,-9,-9,-1,-6,-8],[-6,8,-10,10,-7,6,-7],[9,-1,-5,7,1,7,-7],[-4,9,-1,-5,-4,-2,-3],[-8,1,-2,-8,-7,9,1],[1,2,4,-5,-8,5,7],[-3,-6,-1,-10,-9,8,-3],[7,-6,3,-4,-9,9,-1],[-9,2,9,5,-4,10,5],[-1,-6,4,7,-2,-2,3],[-8,6,3,9,5,-9,-9],[2,9,-4,-2,-1,-6,1]],[[1,1,-8,-7,6,-10,-8],[-10,2,-4,-5,-9,9,-7],[10,2,2,3,2,-9,-5],[-9,-2,3,1,6,-6,-3],[3,-9,-8,6,-6,-9,10],[7,9,-8,5,4,7,-1],[4,-9,6,2,8,-3,9],[-5,10,-2,-9,9,-2,-9],[-2,3,6,3,-9,-5,2],[-3,2,8,1,-10,-10,6],[3,-2,-8,10,-6,-8,-9],[2,-3,-2,5,8,2,8],[-8,-6,10,5,-3,-3,-2],[-2,4,-2,-10,-3,-6,1],[-10,10,3,-10,-1,10,1],[-3,-4,4,10,6,-2,-5]],[[9,-4,6,8,7,-10,-2],[4,-6,6,1,-8,8,3],[3,6,-5,-3,-4,8,-9],[-4,3,-6,-5,8,4,1],[2,-2,1,8,-2,-8,-4],[-10,7,5,3,8,4,6],[-4,2,10,-2,5,8,5],[-4,2,-1,9,10,7,-10],[6,9,-2,7,-6,-4,10],[-6,7,3,3,10,-2,-2],[10,10,-7,-5,1,-2,2],[-5,7,9,-9,-5,8,4],[8,9,-9,4,-9,4,3],[-4,-9,9,-10,10,-1,-6],[2,9,6,-8,8,-1,-10],[-6,3,8,-10,-10,5,4]],[[6,-5,9,-8,3,-2,-9],[7,-9,4,2,4,1,4],[3,-2,-5,-7,2,-1,-3],[-5,5,-2,4,4,8,-9],[9,4,9,-1,4,3,5],[-2,-5,9,-8,2,-6,9],[-4,4,-10,-9,6,-7,10],[-6,-4,-1,5,8,-2,-7],[-9,-4,-5,-10,9,-7,-9],[-3,4,4,-8,-6,-5,-10],[5,5,6,-8,-10,-5,8],[-1,-6,-6,6,10,-4,-10],[-9,8,-8,9,-6,2,-5],[-6,10,-10,4,9,-7,-5],[-5,2,3,-9,6,-2,7],[10,-4,-5,-4,1,10,-7]]], dtype = "uint64")#candidate|4440|(9, 16, 7)|const|uint64
var_4441 = relay.var("var_4441", dtype = "uint64", shape = (9, 16, 7))#candidate|4441|(9, 16, 7)|var|uint64
bop_4442 = relay.subtract(const_4440.astype('uint64'), relay.reshape(var_4441.astype('uint64'), relay.shape_of(const_4440))) # shape=(9, 16, 7)
uop_4447 = relay.sinh(var_4441.astype('float32')) # shape=(9, 16, 7)
bop_4454 = relay.logical_and(uop_4447.astype('bool'), relay.reshape(bop_4442.astype('bool'), relay.shape_of(uop_4447))) # shape=(9, 16, 7)
func_4244_call = mod.get_global_var('func_4244')
func_4245_call = mutated_mod.get_global_var('func_4245')
call_4458 = relay.TupleGetItem(func_4244_call(), 0)
call_4459 = relay.TupleGetItem(func_4245_call(), 0)
bop_4463 = relay.divide(const_4440.astype('float64'), relay.reshape(bop_4442.astype('float64'), relay.shape_of(const_4440))) # shape=(9, 16, 7)
func_1936_call = mod.get_global_var('func_1936')
func_1938_call = mutated_mod.get_global_var('func_1938')
call_4472 = func_1936_call()
call_4473 = func_1936_call()
func_3347_call = mod.get_global_var('func_3347')
func_3349_call = mutated_mod.get_global_var('func_3349')
call_4475 = func_3347_call()
call_4476 = func_3347_call()
func_4298_call = mod.get_global_var('func_4298')
func_4302_call = mutated_mod.get_global_var('func_4302')
const_4479 = relay.const([[5.066944,9.769614,8.024255,-9.003725,-2.149769,5.175525,-2.126018,-4.745383,7.544829,1.355045,-5.333128,-1.420620,-5.117030,-2.801502,-0.702239,2.322077,-9.958061,3.445186,2.780818,9.988133,-6.246613,-8.011240,-8.282823,-5.712015,-8.249754,-9.914042,2.525152,0.194750,9.929880,-7.872240,-3.945683,6.186142,-4.298457,-8.309712,2.800688,5.163168,-6.826708,-1.405430,3.152504,-5.623323,-9.544240,-3.357171,-6.616290,8.694975,7.922164,8.161118,6.440534,-6.673134]], dtype = "float64")#candidate|4479|(1, 48)|const|float64
const_4480 = relay.const([-2.828345,-0.987043,-5.264231,6.056397,-3.259533,7.784332,8.348290,-9.388519,-0.609312,5.902187,1.096679,3.926833,6.322270,-1.259399,-4.435799,7.726423,-1.165142,7.699662,-0.483540,-1.178226,-7.081965,5.550214,2.921651,7.019810,4.714247,1.887040,8.092032,6.138982,4.951493,-4.184025,-3.531782,-5.447709,6.462009,3.584498,1.044768,-1.605677,-0.834464,8.459048,1.353957,4.806832,4.475884,4.357490,7.019501,9.201461,-6.174189,-2.696129,-6.492823,-4.633860,-0.361280,5.049193,7.769985,1.952913,-9.079367,-3.557760,-5.114103,-2.814986,-3.068804,-7.729485,7.996465,-9.883480,5.268048,-0.307256,-4.437871,-3.244838,-9.215811,-9.537415,2.732875,6.019090,-5.408680,-5.051973,4.184998,-2.164118,-4.950200,6.821894,-4.918861,-0.577519,-8.974772,1.529348,1.478106,4.345647,-3.881190,1.406953,-0.662590,2.834000,-9.462514,7.090913,-1.175598,-3.943152,-9.780827,-6.276746,4.733823,0.819076,9.888694,-2.593430,-7.963997,8.310032,7.400169,-5.592947,0.318603,-2.147149,1.033255,-8.533135,1.921853,9.702019,-5.932710,5.039643,-4.019516,-4.978258,6.345597,-5.864767,-5.715586,-2.903686,-7.134473,5.365626,-8.497620,-2.486296,2.813106,-8.352562,6.828768,8.094589,1.471555,5.852223,8.118188,-8.510666,0.349359,-4.066397,-0.957223,0.818010,1.232639,-3.013354,0.688631,-3.021212,7.316931,9.530954,-2.943063,5.869492,3.110604,7.571189,-1.653810,-6.052975,-7.755531,1.910194,2.489559,3.140841,-4.096684,4.540349,-3.058090,-1.395506,-1.969419,-1.318480,-7.998506,-6.556537,9.182201,-3.758539,9.750620,1.964810,2.327598,-6.835165,7.508680,-4.816060,-2.544898,6.231299,7.338981,-8.508771,-6.816247,-5.744106,-7.447399,-9.148681,-8.441576,7.333583,0.742530,9.971293,-4.729481,-5.454865,2.215254,7.283676,-5.149540,8.688427,-1.766569,1.581416,-6.918857,-2.316792,-4.826355,-7.511297,1.208711,1.853030,-8.387149,-8.905841,-1.596196,5.585821,7.221542,3.980326,6.738426,3.546903,5.854661,-8.833976,-1.178164,-2.944789,-3.845815,5.546969,6.009270,-5.429496,5.152704,-2.184366,0.614798,6.164952,-0.195500,-3.672916,2.150418,9.711592,-6.897018,9.732975,-7.950766,-6.845240,-1.781333,7.251342,-3.187491,-6.999568,-6.534786,6.569770,-2.887615,-7.013446,-4.719658,-4.257503,-7.851972,-8.407949,-5.729353,8.873585,7.766720,1.637653,6.834986,1.110654,-2.723536,1.914362,-7.542493,6.436653,6.887974,7.354943,-5.895214,-0.463849,-4.329843,-3.309535,-0.247270,8.368941,8.265148,7.612001,4.110489,-8.658562,-1.204125,-0.709141,-5.044776,8.605627,5.342079,8.295931,6.816498,-2.626810,-0.073212,-1.240463,-7.723269,1.846009,-1.885217,-9.742047,4.363431,3.092594,-1.428821,0.107621,6.584142,0.228366,4.433896,3.054629,-6.830203,-5.698196,-2.492284,2.800689,1.962653,-1.456252,7.599394,9.913256,3.510801,5.253248,5.845588,-9.578293,6.181344,4.631285,7.393578,5.084466,1.935543,-2.900992,-5.374844,-0.913224,-8.521648,2.940988,-9.385420,8.435651,-4.543892,5.922516,7.989623,-1.797602,8.868940,3.113009,-2.410423,-2.321304,9.490645,4.024889,-1.575216,8.445007,-6.788794,2.485497,1.038404,-5.008124,3.371665,0.980919,-8.713459,4.213982,-1.496431,-8.454289,-3.620962,-2.228691,8.616567,9.388839,8.416768,0.883958,-4.280184,-2.924342,5.157370,2.973641,5.608188,3.393939,-4.744990,9.825135,9.419174,-3.177623,1.507276,5.221401,-9.434184,-3.048620,2.354460,-3.178165,-8.057683,-6.235071,5.115122,-8.535053,-8.464868,-1.691306,7.761720,0.039154,0.885550,-8.106561,-3.555140,-0.101275,-2.071387,0.400107,-7.680060,7.122081,-2.547885,-6.564563,7.303833,-9.191633,-9.551385,0.783613,3.259969,-3.163665,-1.078221,8.235049,1.603018,7.298322,-1.429625,3.471802,-3.748813,-4.442481,-2.994648,2.976510,3.305363,-5.334414,-3.043055,8.477120,-5.058919,0.363931,-4.560973,-9.580435,-1.849752,-3.478845,-4.344307,0.584238,-1.277998,5.862567,-7.511174,7.235968,4.595136,2.610538,4.453828,4.882161,-6.583678,-3.285936,8.626236,-0.516575,-2.126370,-6.161019,8.497214,-2.694821,4.510670,-4.229101,-8.201811,-7.611901,2.394093,5.128394,-9.247507,5.554013,9.293691,-3.981787,-0.009443,-3.925972,2.489824,9.003673,-7.398567,-6.961128,9.119001,5.985770,-0.852545,2.029461,4.962134,-9.370920,1.844601,9.313253,5.500284,6.073687,-3.516796,5.278802,7.969867,-2.428875,-1.684617,4.124744,-0.838326,0.951362,-7.771065,-9.013590,0.737918,-6.482685,-0.395155,-5.276717,7.200138,9.793494,0.371220,4.309989,7.653505,6.553826,-9.716721,-1.260798,9.207829,-5.996993,-4.444211,-6.104629,5.195115,5.930222,-7.413421,-2.781793,1.036454,4.026137,-0.988136,2.542911,5.363072,4.308654,-9.654858,-9.242129,1.901538,7.064679,2.649534,1.737424,-0.274413,5.962001,-1.447516,-7.200135,6.094619,1.886459,-0.271198,-7.951472,1.096485,-3.056687,7.947746,3.742569,2.349386,-6.178150,-6.546848,1.591264,-2.842367,5.709516,-5.339949,1.568357,-3.102760,8.024423,6.073052,-2.580493,2.240490,-3.557982,8.205311,4.517454,9.766338,8.894422,-0.010449,-8.256228,5.235438,4.309703,-1.097706,-3.853153,5.963286,2.303319,6.441680,2.676060,-5.294252,0.031664,-3.415059,-6.464634,-2.497147,4.850838,2.897688,-7.221405,-2.988032,-8.465317,-3.211954,6.542276,2.090571,-5.320150,-1.220900,1.408822,-7.157002,-9.217090,-9.755497,-2.145132,-5.769388,1.005053,4.719084,9.467699,7.370263,-5.124370,-7.193843,-0.518655,3.194268,-5.206825,-8.682705,-6.319631,-0.387076,7.098633,-4.626586,7.070783,-8.455492,-1.368158,-6.959716,8.511964,5.184645,0.239987,6.118580,2.963475,0.819077,-7.971731,-6.756137,-8.664610,3.123683,3.668136,7.051109,-6.891202,0.325824,2.970917,-4.408982,3.225986,2.058161,6.727954,-3.568031,8.188238,-0.090015,-1.300105,-8.139262,5.025807,-6.727763,7.866194,-8.356319,5.525656,-1.612258,0.930141,4.309981,1.004417,-4.651972,9.995475,7.831535,-9.161382,-4.622571,-9.558569,0.591334,-1.015320,-3.495855,6.248619,-1.747019,-9.035468,1.089825,4.401738,1.164039,9.498534,-0.461472,-2.211167,1.214345,7.673160,0.526864,6.848558,-2.916263,1.409257,7.927010,8.897931,8.851276,8.599869,2.209124,-7.283125,3.996659,-6.950629,-7.197288,6.511250,5.957167,-5.006749,0.682152,2.326904,1.857387,-6.844360,1.683416,-7.251823,-3.288685,-4.533590,9.342321,-3.392091,-7.622082,-5.095024,2.762621,2.708344,-7.359303,-5.094964,0.063071,4.774915,-9.760046,3.054167,6.328699,-3.805855,7.834778,-5.245306,1.339856,7.986126,3.545400,4.465722,-0.239813,-1.850334,-7.102973,-5.457981,-9.419526,-2.743030,5.404732,3.183792,-1.816242,-9.150546,-2.474675,-2.957969,9.977480,5.926330,7.455300,-6.804779,7.477552,-4.378526,6.845996,2.644320,8.667839,-5.315754,-1.039498,1.881220,7.899769,-0.213729,-5.876725,-4.308326,9.924780,7.287314,-0.337136,-9.183153,-3.582749,5.688280,1.809770,3.839235,-2.444042,1.970628,1.627908,3.392382,9.134725,-4.239692,-2.670764,3.058233,8.826830,-0.529284,-8.860355,5.938680,-8.806451,-4.247964,-6.613114,-3.493078,1.399179,9.542577,-1.381067,-9.913771,-6.013193,-3.037359,5.654836,-4.743465,-3.577810,-8.046036,0.257809,7.114859,-8.334501,4.918719,5.633422,4.902948,-3.709525,-0.421254,-2.800060,-1.013475,2.422234,4.406544,-7.972192,1.194459,7.796772,-0.263635,-7.683559,-4.101475,7.525890,9.174211,0.033550,-9.164176,8.689330,-7.661840,1.563296,-8.358525,2.105907,8.699158,-7.572713,-4.433238,-0.022189,-1.846382,-6.802872,5.647137,8.182364,8.302725,8.244775,-7.981497,-1.367614,-3.396307,2.387986,-8.437506,2.501986,-2.553390,2.101772,4.756819,1.097759,-4.843813,-3.591402,-1.412281,-7.077710,-8.753928,9.827606,-5.690834,1.670291,4.201245,7.771733,-4.153826,7.078169,-8.869130,0.325155,-9.152158,-0.165929,4.564120,-1.483555,-8.126576,2.429570,-8.303656,5.702536,-6.368572,-8.603958,6.130018,1.307532,-0.757388,-8.973024,1.803333,-4.418154,0.411392,-3.338633,4.825875,-6.435355,4.211141,-0.107887,-5.903791,-2.164552,-1.073102,-1.485693,1.598729,4.009924,-9.058177,-2.141548,-8.507756,7.457458,8.177351,-0.924535,-3.300753,-5.597208,-4.587497,8.362898,-7.931713,7.528212,-8.169618,-6.628945,7.156906,0.948806,-3.181468,-9.609670,-8.970921,-0.788006,8.989310,-3.910416,2.011827,-9.396877,2.213180,-4.371315,1.391700,0.833496,8.676247,9.753871,3.220281,-7.765126,7.570989,-1.292381,-3.211470,7.196580,4.058498,4.511090,8.350952,-8.896522,3.886182,-0.445657,-3.849027,0.165109,-6.705102,1.709914,8.039764,0.962970,-9.335128,2.691904,-7.254455,-8.799866,-4.522288,-0.013978,4.051779,5.401160,0.499698,-8.054286,3.884699,2.473150,-9.299482,5.982298,-7.613260,-5.896252,1.471801,7.639584,8.588705,7.876199,4.151200,1.270055,8.019209,7.421632,-4.314102,-0.071510,3.497505,3.387077,-0.576438,-1.550210,5.927239,1.671397,-6.657747,-0.636376,1.616759,7.222123,0.420710,7.434641,6.247494,8.539842,-5.847028,2.514227,7.697359,-0.679609,-5.277223,-1.605676,3.369385,-7.830778,-0.405914,0.608854,-8.978203,-3.896599,6.122555,-7.719358,4.674834,4.172821,-9.943349,0.228093,7.137500,2.174753,-8.068231,-5.651182,-0.445575,7.726555,6.009002,-9.390098,-7.642138,-0.383100,-3.803086,-9.965392,-1.940024,-7.196937,8.181088,7.941168,3.911338,-0.825914,-4.870898,1.187527,0.954454,-0.956886,-3.884960,-9.654599,4.379182,-2.866466,-7.316098,4.201395,-3.195711,7.802200,-5.924894,7.739545,8.343114,2.071578,-2.243147,-3.414062,-3.985493,-4.317037,2.209651,0.522418,8.546365,7.601854,-1.261483,1.751910,-8.505458,-9.432438,8.568669,-0.356629,1.612812,-3.427460,-5.207132,3.858281,6.979136,3.915781,4.317515,-1.455467,8.305474,-5.813501,-8.606958,-2.029878,-3.546032,1.148918,-7.256842,-8.802406,-2.127289,4.108464,-9.598133,5.995191,8.749146,-4.932326,6.292007,4.417591,-9.013353,-2.111009,6.363186,0.579998,-5.409517,1.029183,-6.868043,-7.722646,0.206455,-1.825701,3.479048,0.762536,-5.842121,6.017484,-7.281871,-4.582387,-8.092483,-1.281090,-8.716752,8.083882,-2.317304,9.909859,-6.995740,5.043636,-5.532718,2.193101,0.142803,-0.449779,7.418195,5.599417,-3.671513,-1.417266,9.153518,3.517071,3.597114,-7.151316,7.228805,-3.323999,6.078230,1.289782,4.769967,7.359301,-0.974498,9.873557,7.901004,1.053292,-1.541805,-7.275400,-5.392479,3.174550,-8.734467,-3.070819,-6.915055,-7.932256,-1.171406,6.200316,-0.461324,7.281605,-8.470544,-4.761570,9.459140,0.041811,-4.509493,7.040030,4.785438,-5.486364,-2.603298,-5.689672,8.523133,6.209160,-7.776363,-6.559186,9.909230,4.720952,-4.627739,-2.731589,-4.528886,7.577958,5.102775,2.874590,-9.319577,5.189255,-6.379821,2.878321,-7.791076,-5.608783,8.968153,3.415677,-3.741298,-9.426033,2.091503,-6.073491,-9.726007,-5.831588,4.451199,4.826356,9.096656,-3.216626,-6.968577,2.407536,-4.703807,9.835240,-3.089726,9.040485,-8.722911,6.977882,-7.953008,6.009066,-5.837167,-7.666615,2.335793,4.756150,-8.510047,0.096857,9.486620,3.018165,-8.796796,4.404440,-7.838816,1.692484,-0.068614,-2.529078,-5.672299,5.407468,2.187453,-0.528273,7.178183,6.776266,-3.961763,-2.741606,1.538280,4.551410,9.307356,9.246865,5.507519,-8.457455,1.001811,-8.534131,-9.123114,-7.869969,-8.487902,-4.503984,-4.549390,4.669781,-2.800135,-3.455810,-6.525101,0.005677,-8.601969,7.523046,4.790683,8.142280,-2.328369,6.442344,-6.299524,-7.147273,-6.472143,-1.862053,-6.720005,3.120803,-2.083106,-0.698374,-7.828043,-0.098759,-8.681710,-4.902684,7.336549,4.332781,-4.493235,-3.225580,-6.388149,4.830406,3.646363,-4.907792,1.189295,5.236703,5.203932,-0.187601,0.616878,9.519317,-2.179878,-8.497144,5.697302,7.496448,-5.332859,-5.651412,-3.479071,3.662474,-8.445824,9.066441,-4.351143,2.138196,0.958721,6.558967,-2.885893,-4.934103,-3.806686,-9.343682,-7.027574,0.727700,9.486074,-1.191775,1.430847], dtype = "float64")#candidate|4480|(1176,)|const|float64
call_4478 = relay.TupleGetItem(func_4298_call(relay.reshape(const_4479.astype('float64'), [6, 2, 4]), relay.reshape(const_4480.astype('float64'), [1, 1176]), ), 4)
call_4481 = relay.TupleGetItem(func_4302_call(relay.reshape(const_4479.astype('float64'), [6, 2, 4]), relay.reshape(const_4480.astype('float64'), [1, 1176]), ), 4)
bop_4485 = relay.multiply(uop_4447.astype('int64'), call_4458.astype('int64')) # shape=(9, 16, 7)
bop_4488 = relay.multiply(uop_4447.astype('int64'), call_4459.astype('int64')) # shape=(9, 16, 7)
var_4493 = relay.var("var_4493", dtype = "bool", shape = (9, 16, 7))#candidate|4493|(9, 16, 7)|var|bool
bop_4494 = relay.maximum(bop_4454.astype('float32'), relay.reshape(var_4493.astype('float32'), relay.shape_of(bop_4454))) # shape=(9, 16, 7)
func_1936_call = mod.get_global_var('func_1936')
func_1938_call = mutated_mod.get_global_var('func_1938')
call_4497 = func_1936_call()
call_4498 = func_1936_call()
var_4502 = relay.var("var_4502", dtype = "bool", shape = (9, 16, 7))#candidate|4502|(9, 16, 7)|var|bool
bop_4503 = relay.less_equal(bop_4454.astype('bool'), relay.reshape(var_4502.astype('bool'), relay.shape_of(bop_4454))) # shape=(9, 16, 7)
uop_4510 = relay.cos(bop_4494.astype('float64')) # shape=(9, 16, 7)
output = relay.Tuple([bop_4463,call_4472,call_4475,call_4478,const_4479,const_4480,bop_4485,call_4497,bop_4503,uop_4510,])
output2 = relay.Tuple([bop_4463,call_4473,call_4476,call_4481,const_4479,const_4480,bop_4488,call_4498,bop_4503,uop_4510,])
func_4521 = relay.Function([var_4441,var_4493,var_4502,], output)
mod['func_4521'] = func_4521
mod = relay.transform.InferType()(mod)
var_4522 = relay.var("var_4522", dtype = "uint64", shape = (9, 16, 7))#candidate|4522|(9, 16, 7)|var|uint64
var_4523 = relay.var("var_4523", dtype = "bool", shape = (9, 16, 7))#candidate|4523|(9, 16, 7)|var|bool
var_4524 = relay.var("var_4524", dtype = "bool", shape = (9, 16, 7))#candidate|4524|(9, 16, 7)|var|bool
output = func_4521(var_4522,var_4523,var_4524,)
func_4525 = relay.Function([var_4522,var_4523,var_4524,], output)
mutated_mod['func_4525'] = func_4525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2858_call = mod.get_global_var('func_2858')
func_2859_call = mutated_mod.get_global_var('func_2859')
call_4544 = func_2858_call()
call_4545 = func_2858_call()
func_4041_call = mod.get_global_var('func_4041')
func_4044_call = mutated_mod.get_global_var('func_4044')
var_4557 = relay.var("var_4557", dtype = "bool", shape = (1, 8))#candidate|4557|(1, 8)|var|bool
var_4558 = relay.var("var_4558", dtype = "float64", shape = (1176,))#candidate|4558|(1176,)|var|float64
call_4556 = relay.TupleGetItem(func_4041_call(relay.reshape(var_4557.astype('bool'), [1, 8]), relay.reshape(var_4558.astype('float64'), [1176,]), ), 3)
call_4559 = relay.TupleGetItem(func_4044_call(relay.reshape(var_4557.astype('bool'), [1, 8]), relay.reshape(var_4558.astype('float64'), [1176,]), ), 3)
func_2948_call = mod.get_global_var('func_2948')
func_2950_call = mutated_mod.get_global_var('func_2950')
call_4577 = relay.TupleGetItem(func_2948_call(), 0)
call_4578 = relay.TupleGetItem(func_2950_call(), 0)
var_4592 = relay.var("var_4592", dtype = "float64", shape = (1176,))#candidate|4592|(1176,)|var|float64
bop_4593 = relay.add(var_4558.astype('uint16'), relay.reshape(var_4592.astype('uint16'), relay.shape_of(var_4558))) # shape=(1176,)
func_4153_call = mod.get_global_var('func_4153')
func_4156_call = mutated_mod.get_global_var('func_4156')
const_4599 = relay.const([-3.030801,7.857842,0.591257,8.924799,-9.513248,9.282260,4.212564,1.220704,-0.654131,-4.069644,-6.178649,-2.814140,-0.689702,-6.876507,8.999610,7.810823,6.817495,5.217492,-5.143097,6.953159,-9.661260,3.004023,6.597447,2.630888,-4.351210,6.480774,7.446253,-7.259888,1.874754,7.349671,-9.657631,-8.497584,6.276984,-8.039583,6.268830,-3.417895,-6.604731,2.165807,1.073103,7.724145,-3.012940,-5.639016,-3.191035,-7.063734,2.712113,-7.702072,-9.293425,-7.786418,-1.217340,4.352575,-7.611868,3.034407,6.083418,-9.983277,-0.657513,7.492985,-3.599528,-0.029389,-3.662477,-2.961016,-0.810871,0.687289,-0.161710,-0.302056,-7.433349,-8.514749,-6.565934,-3.743731,-9.110100,-6.985397,-8.825818,3.469876,5.689754,-0.069861,-3.747645,-3.894946,2.845699,0.834576,5.599052,9.318694,-8.859148,-3.735785,5.046853,-0.415263,1.521238,-0.043821,-8.840424,-6.799868,7.337105,5.843267,-5.061494,-1.769806,1.462076,2.835405,-4.564000,2.166539,-7.711591,3.181504,-8.020094,6.560232,-2.120796,4.474063,8.363603,-1.591367,-5.818114,7.174293,7.582768,9.145825,2.748904,9.546657,3.009629,-3.083510,-7.030430,4.573330,-7.565847,-6.895113,8.156431,0.883651,-8.523990,9.251573,-9.402048,0.398348,0.395823,-9.280114,5.614244,-0.770063,-5.449077,-4.223871,-1.267377,5.847003,-4.385121,9.814555,-0.161810,-2.172532,-8.021019,5.091858,-8.258709,8.355788,6.211922,7.429044,8.686041,8.646311,-6.819134,6.397934,-6.223451,3.031224,-4.082198,-8.962442,-9.427490,9.066677,-4.521665,1.841514,6.092222,-4.024769,-3.117371,0.044803,9.817220,-4.959809,-1.782702,-8.160552,-0.450460,4.586654,-0.150542,1.502542,1.478328,-6.586902,-6.500954,-0.969297,-6.247128,-7.892889,-0.689628,-2.572957,8.682033,-6.983169,-8.563402,-4.897063,-7.449259,-3.591698,1.354851,8.733347,-8.498690,-4.461292,5.216921,9.904511,-4.153813,0.001813,9.362492,-3.329330,-0.704204,6.995802,-1.685836,0.471270,9.302578,1.270992,-9.176092,1.114959,-8.312488,1.764058,2.079414,8.613998,-8.196823,-3.758485,4.644915,-2.602880,8.397200,-8.488568,3.182463,7.661934,4.902312,1.275462,7.045998,7.267079,5.484114,-3.415814,5.110687,-6.869012,-5.234774,1.849447,9.515808,1.466636,3.041478,-6.204465,2.803763,-9.437252,4.287040,-4.157489,-0.289412,-8.774548,-4.304308,-9.810754,3.928155,-7.201230,-7.045602,7.447441,6.080210,-5.049769,-6.871212,-6.503388,-1.818679,7.193530,-9.062950,2.528973,6.172054,-2.367812,-1.646286,9.114459,7.166411,0.342552,2.787890,-7.829883,5.560993,-3.198293,4.876580,4.567107,2.388218,1.939563,2.624864,-9.034649,2.874238,-4.632828,-2.997800,1.838997,8.637211,3.192207,1.710180,-7.586972,-7.433537,-7.137253,5.366938,-4.289631], dtype = "float64")#candidate|4599|(270,)|const|float64
call_4598 = relay.TupleGetItem(func_4153_call(relay.reshape(const_4599.astype('float64'), [9, 10, 3]), relay.reshape(const_4599.astype('float64'), [9, 10, 3]), ), 1)
call_4600 = relay.TupleGetItem(func_4156_call(relay.reshape(const_4599.astype('float64'), [9, 10, 3]), relay.reshape(const_4599.astype('float64'), [9, 10, 3]), ), 1)
func_2820_call = mod.get_global_var('func_2820')
func_2821_call = mutated_mod.get_global_var('func_2821')
call_4609 = relay.TupleGetItem(func_2820_call(), 3)
call_4610 = relay.TupleGetItem(func_2821_call(), 3)
func_3347_call = mod.get_global_var('func_3347')
func_3349_call = mutated_mod.get_global_var('func_3349')
call_4612 = func_3347_call()
call_4613 = func_3347_call()
output = relay.Tuple([call_4544,call_4556,var_4557,call_4577,bop_4593,call_4598,const_4599,call_4609,call_4612,])
output2 = relay.Tuple([call_4545,call_4559,var_4557,call_4578,bop_4593,call_4600,const_4599,call_4610,call_4613,])
func_4629 = relay.Function([var_4557,var_4558,var_4592,], output)
mod['func_4629'] = func_4629
mod = relay.transform.InferType()(mod)
var_4630 = relay.var("var_4630", dtype = "bool", shape = (1, 8))#candidate|4630|(1, 8)|var|bool
var_4631 = relay.var("var_4631", dtype = "float64", shape = (1176,))#candidate|4631|(1176,)|var|float64
var_4632 = relay.var("var_4632", dtype = "float64", shape = (1176,))#candidate|4632|(1176,)|var|float64
output = func_4629(var_4630,var_4631,var_4632,)
func_4633 = relay.Function([var_4630,var_4631,var_4632,], output)
mutated_mod['func_4633'] = func_4633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3204_call = mod.get_global_var('func_3204')
func_3205_call = mutated_mod.get_global_var('func_3205')
call_4647 = relay.TupleGetItem(func_3204_call(), 0)
call_4648 = relay.TupleGetItem(func_3205_call(), 0)
const_4655 = relay.const([[[-7.343765,-8.670106,-0.730163,-3.141521,5.482967,3.443310,-2.829443,0.575620,-0.277909,1.811276,5.495512,-6.409564,-5.964076,-4.338068,4.292035],[3.626438,-1.880720,-7.373004,-5.952414,6.754598,-3.523497,7.680517,-9.011766,-2.361408,4.811848,1.959309,4.795958,4.339469,-3.953018,-1.516301],[-0.923761,1.140670,7.271151,9.455482,0.092892,6.625879,-9.253327,-9.307787,-8.328762,0.386658,-9.665728,-5.809824,4.544742,-7.400680,5.995320],[8.275212,-7.074029,7.756173,-3.318205,-5.297395,3.487453,-8.437790,-9.933680,1.862775,4.974050,7.358188,1.184074,1.734747,1.996126,-4.536894]],[[-7.135594,-9.411425,8.295042,-3.432929,8.638833,8.399934,9.603265,-1.592254,-7.473464,-2.012982,-3.084933,8.964050,7.520167,-8.660577,-7.894242],[-1.009638,3.739305,-8.932668,-6.023184,-9.507390,4.367371,-7.162682,8.803740,-8.854057,-1.888176,3.854597,-6.789217,0.193871,2.240934,5.977639],[-4.597193,-0.271345,-1.490205,-6.369909,-4.778634,-3.572820,-5.439594,-9.067791,8.273093,3.635658,6.707812,7.068831,-4.151916,5.635909,-1.774545],[4.689859,-5.612398,-2.426659,-5.472734,0.127323,-3.790440,-9.486233,5.298702,-5.086860,-9.347368,-7.140239,5.719546,9.777666,-1.836168,0.757271]],[[3.694254,-2.154799,5.041657,7.214738,3.759603,-3.798487,-8.276847,6.559751,8.421288,3.953602,8.275243,9.556849,1.802022,-8.349944,0.681731],[-1.174698,7.558868,7.186933,-7.112029,-1.861099,9.691144,2.534781,-0.080547,2.355452,-7.818071,3.952084,9.344106,-7.784811,2.160082,-8.365572],[2.877726,-7.825083,9.273271,2.404863,-0.554949,-1.412049,-1.920201,7.586988,-4.797998,-4.333783,1.925794,-0.248648,-8.942180,6.656535,-9.233569],[-8.523298,4.495069,-5.445706,-2.529663,-2.226258,7.207383,6.025577,-8.588350,-8.504427,9.488274,8.666370,-0.701972,9.280013,0.765369,6.285457]],[[5.426008,1.899086,-1.731115,4.621237,3.866827,3.358457,-5.283584,-4.763982,2.186051,6.765211,3.686185,-2.838701,7.820928,-4.917771,-1.294385],[-3.702978,8.511717,-2.625223,0.353598,8.368012,8.696358,7.765862,8.164320,-8.471661,6.923581,0.790187,8.593684,-8.711315,-0.249949,0.835125],[-6.651338,-4.086882,8.900896,3.463757,-0.547304,2.749912,0.637185,-2.643335,-2.730181,-6.952866,-8.397978,-1.134824,4.980356,-6.988517,3.213570],[-4.061227,9.390608,6.175627,-0.987718,0.220405,5.697728,-2.719253,-1.242480,7.535608,-3.073193,-6.083743,-3.444407,-5.399995,3.373436,1.147428]],[[-7.317372,4.536353,-7.376586,-2.983739,0.520276,7.579843,-3.454994,-3.446061,-0.177918,0.849921,0.108303,-0.904084,-6.277793,3.615482,7.719667],[-7.946296,-9.725080,-0.163855,-6.606427,7.618324,-8.385530,2.422419,3.069993,7.900882,8.422880,-6.133049,-4.362390,-2.026334,5.641909,7.536177],[-7.280529,-9.978758,4.756393,7.273425,7.882580,2.536330,-2.714082,-3.966761,-3.959296,2.641470,-6.288576,-7.788387,-1.092798,7.319936,-0.750428],[4.041738,-9.555591,-8.625003,-4.376112,2.712874,-2.246675,2.464637,1.923522,-9.148701,-0.615915,-5.757808,2.120199,6.968082,2.533670,7.063526]],[[7.030549,7.722681,-2.695304,7.727122,4.371809,-5.887644,-4.343457,-6.495882,6.314951,9.045320,2.203202,-0.811320,7.140881,-1.963320,-1.289831],[-5.321433,-3.025139,0.751525,4.414273,9.310686,-5.838853,6.391930,-7.063354,-0.686887,-3.793165,1.383117,4.188465,8.372985,1.387439,-1.225108],[6.256296,-2.790944,-6.576760,8.791956,-7.361009,-0.417875,-8.703705,0.740297,-3.366504,2.318865,-1.533678,-0.058962,-0.981991,-5.063639,7.955723],[-1.579020,7.640299,6.201704,-7.728371,-6.515663,5.300772,2.189234,-2.391939,-0.198738,2.678656,4.869036,-9.858966,9.398820,7.289441,7.863434]],[[-7.919729,-1.382856,-3.289996,5.022057,-9.118415,0.962544,1.876457,5.926822,-6.438884,-3.039975,0.943617,6.292878,0.706683,5.297088,-0.574753],[3.514861,-1.332190,-7.826510,7.314525,4.988432,3.422763,-6.918782,-0.410570,-0.217006,9.055147,-7.603362,3.632027,9.923085,-7.229996,2.911419],[1.812507,-5.641809,-9.664970,-6.173460,-7.357879,6.937125,-1.042033,-6.776007,-2.780633,8.845306,9.082293,-3.231750,3.194309,0.183021,-1.958579],[-1.705914,-7.058448,7.577651,-3.865896,-4.077153,-9.523390,-5.373699,7.806158,4.738409,-4.785201,-1.470390,-3.524883,-6.966796,-8.574396,2.410752]]], dtype = "float64")#candidate|4655|(7, 4, 15)|const|float64
bop_4656 = relay.equal(call_4647.astype('bool'), const_4655.astype('bool')) # shape=(7, 4, 15)
bop_4659 = relay.equal(call_4648.astype('bool'), const_4655.astype('bool')) # shape=(7, 4, 15)
bop_4660 = relay.greater(const_4655.astype('bool'), call_4647.astype('bool')) # shape=(7, 4, 15)
bop_4663 = relay.greater(const_4655.astype('bool'), call_4648.astype('bool')) # shape=(7, 4, 15)
bop_4684 = relay.logical_or(const_4655.astype('bool'), relay.reshape(bop_4660.astype('bool'), relay.shape_of(const_4655))) # shape=(7, 4, 15)
bop_4687 = relay.logical_or(const_4655.astype('bool'), relay.reshape(bop_4663.astype('bool'), relay.shape_of(const_4655))) # shape=(7, 4, 15)
output = relay.Tuple([bop_4656,bop_4684,])
output2 = relay.Tuple([bop_4659,bop_4687,])
func_4688 = relay.Function([], output)
mod['func_4688'] = func_4688
mod = relay.transform.InferType()(mod)
output = func_4688()
func_4689 = relay.Function([], output)
mutated_mod['func_4689'] = func_4689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4084_call = mod.get_global_var('func_4084')
func_4085_call = mutated_mod.get_global_var('func_4085')
call_4690 = relay.TupleGetItem(func_4084_call(), 0)
call_4691 = relay.TupleGetItem(func_4085_call(), 0)
func_1796_call = mod.get_global_var('func_1796')
func_1798_call = mutated_mod.get_global_var('func_1798')
const_4698 = relay.const([3.668156,-1.839431,-3.397382,2.456488,-6.618893,8.604165,-5.111579,9.309658,-7.914273,1.918912,4.386513,5.462299,-0.421009,-8.801229,7.267517,8.956409,0.020928,4.730195,-7.459278,7.741026,6.818064,5.053388,-0.908605,7.623183,5.912827,4.832181,-6.864547,-5.966790,-0.959340,0.587367,-3.824381,-3.968106,-9.838217,8.900085,-3.403972,3.742058,6.313342,7.737005,4.361364,-4.197314,1.785111,7.259116,-7.999773,-8.657151,-0.459121,7.520082,8.187043,7.082976,3.955929,-7.153769,8.353084,0.222431,6.457981,-3.443229,-3.061546,5.512539,7.737437,1.172107,8.619843,-2.110213,0.058034,-2.596860,6.213902,-0.293049,-6.469525,-5.034742,-7.423391,-9.709251,-1.943691,-9.565359,6.809022,-1.708052,2.163626,9.906193,9.160203,-1.732179,7.448541,3.537334,-9.638156,3.378877,4.625192,-1.966732,3.929762,4.677760,-5.884407,-0.866988,2.227012,-8.911713,3.110360,7.252505,5.643056,6.987697,-3.574577,3.878766,0.634516,6.822349,-4.527912,-1.504902,-5.726073,4.267392,-3.121878,2.049027,-2.741539,-4.777384,9.074221,-6.939018,0.154750,5.733360,1.762266,2.855698,3.111248,3.361211,-0.136833,5.173618,0.309865,6.315822,1.850083,2.445538,-9.986839,4.971805,-9.761193,-3.916429,4.157842,8.078949,-2.986660,0.209617,-2.055952,3.047839,9.317857,8.960777,9.214794,-5.526933,8.882138,-6.762147,3.307547,3.877428,-1.543359,3.299734,1.032167,-0.975632,6.143876,0.337017,-6.458124,8.980733,-9.547453,-5.303328,0.438865,-8.855681,-9.125152,4.963884,-8.400517,4.855728,-9.161701,-7.028384,-9.257653,-0.417931,7.373108,2.584899,-5.336147,7.376308,9.512922,2.431552,-6.394257,-1.643875,-1.772955,-5.358975,-6.969252,8.952995,-3.241184,5.655061,-3.594368,7.746463,2.643330,8.637046,8.824555,-2.693331,-1.158666,6.934229,6.680287,-1.508182,9.388446,-7.977186,-7.307089,3.962638,-4.544243,5.189076,-5.829086,-1.910275,4.407612,8.888221,-7.819030,-2.869307,5.363887,2.353089,3.771393,1.384273,-1.513358,-6.890822,8.586316,3.882021,-2.579718,0.718993,7.366421,7.940843,0.575007,3.119285,-8.704573,8.497067,-4.654455,4.093403,-8.593873,-9.792814,-5.674547,8.686609,-8.456560,9.277610,-9.484389,2.860281,-3.963503,-2.306220,-4.613400,5.207873,9.481015,-6.486283,5.750116,5.248395,-7.074550,-7.188013,5.786253,0.162864,9.572850,-1.066172,1.853510,8.137411,-0.723381,8.887936,-1.280038,-7.451551,9.766202,6.263399,-3.452848,-1.838353,-9.047314,8.222879,2.827259,-5.151145,-0.839918,-4.001719,-6.119390,1.935426,0.718686,9.764641,-0.972464,-6.060750,6.450048,-8.197404,-1.446253,-0.807386,-5.644593,-9.459729,-2.429494,-1.113820,-1.528947,-6.599229,-7.110191,6.718011,4.810388,0.220700,-0.527926,7.085359,5.196290,5.160856,5.151723,5.594337,-3.831630,3.948795,-7.555545,4.515789,-5.068599,8.612467,2.207400,-5.177130,-4.561348,-9.986518,9.946987,-9.857386,-5.114182,3.915008,2.770588,1.328819,-2.869548,1.365311,-7.219833,8.467573,-6.701658,5.162053,-0.169813,-4.348077,-9.604481,5.084113,6.308853,-7.031539,-1.228741,2.156652,-8.007252,3.508643,5.563292,0.003289,8.012111,-9.783523,-5.222946,4.448926,8.878907,3.148477,3.787871,-3.954088,-7.569978,-9.665951,-5.735312,-1.324435,-3.375414,3.342389,-2.946205,0.893639,-6.446626,-1.296779,1.889301,1.992569,7.410844,-0.437584,2.705207,9.413901,-2.971476,-7.693211,3.332011,0.943449,-1.254157,5.044384,-8.574104,-7.062078,-2.337641,7.224171,6.891578,5.367359,0.400988,3.553043,-8.924982,-0.588304,-9.219962,6.935662,9.732135,9.532127,8.199435,1.934163,4.002328,-6.907283,-2.403006,3.468397,-3.869568,-2.885562,1.942915,8.436729,2.443983,-1.855332,-3.877482,2.378752,-6.276351,-0.560223,-7.967805,3.556215,0.711191,4.380923,6.474871,0.118312,4.033787,5.059944,7.233759,-1.905544,-3.349294,-3.978800,-5.828464,1.445798,-5.748549,6.548027,2.254319,-7.020947,-8.114691,-3.222893,5.323365,-4.190088,5.466739,3.627664,-7.235305,4.417643,-2.861587,5.387594,-6.680773,5.194986,-0.093432,0.439099,-7.968161,4.358468,0.688929,-8.551573,0.792631,-2.699410,7.266120,-3.126704,6.830459,-8.122036,8.569416,2.788505,-2.191447,9.859388,8.709712,-0.224195,-3.326167,-9.169268,8.957598,-6.852045,5.639663,-6.649810,-4.076035,-8.394319,-7.563105,3.488114,0.959598,7.648176,-4.268551,-6.122414,6.908515,9.539368,-5.004156,-5.916020,-3.461498,5.413443,9.069932,-6.482214,-1.651827,9.860263,-1.268365,-8.294127,6.843240,1.694595,-3.397847,3.135359,5.893357,-2.642653,7.051223,2.201096,6.536536,3.841263,-4.813939,3.615347,4.581656,-9.050738,5.414224,4.404395,-2.723424,-5.454595,-9.313998,7.377273,-3.967389,-9.209006,-9.617140,-3.292036,-8.446730,-2.903575,1.299668,8.084504,-4.035595,-8.170451,-6.958564,8.927505,4.774143,-6.438745,6.204411,1.969785,5.318598,3.854187,0.495137,9.755625,-2.480392,6.748131,8.322813,-6.047399,-8.051393,-8.501187,-2.079698,2.195810,2.012187,9.581922,0.437766,1.749034,-7.548140,-2.539819,-6.939835,9.849589,1.258340,-0.581744,2.229484,5.942399,-6.526065,1.757525,3.835421,-1.673796,-3.479701,5.252158,-5.010316,-7.337424,-0.083793,-2.423846,-2.761782,5.834364,-7.830797,0.904502,-0.683844,4.432991,-1.426783,5.435115,-0.623605,-2.433086,6.705644,-0.859777,-0.874574,6.500888,-0.003864,1.830823,4.441338,-5.083377,3.740356,-4.012562,-4.576110,-6.051995,-3.410619,-5.873008,8.214526,5.145674,5.976707,-6.251695,-5.256768,-8.519037,6.973355,2.643250,-2.196707,7.623109,1.708124,1.627087,3.288134,-5.984561,2.986161,-7.693736,-1.651063,6.414436,-6.607341,0.619389,2.508897,7.766425,-6.936612,-2.384407,-3.950301,-8.713795,6.689600,-7.495688,1.787628,-3.198731,8.928683,6.255820,-7.491033,0.593527,-1.676348,2.906211,-0.216737,-0.304433,9.437445,0.272893,-1.756523,-8.405020,7.853746,5.809479,7.261244,6.628931,-4.011006,-7.348529,-7.477213,7.202020,5.278881,-5.933915,7.871198,-3.726642,9.590619,6.904435,3.637742,9.964946,-6.529310,0.728244,-5.583841,-7.019461,7.037627,1.510791,7.740294,-0.121719,4.506759,-2.052036,9.207120,-6.851304,4.835294,0.918563,6.745907,1.548440,1.484431,0.532921,-1.759876,-2.730275,7.855623,9.627162,8.650553,9.599107,-2.280420,7.637684,-3.317261,7.339190,2.653247,-1.973314,7.413617,-0.263023,-0.196884,4.835488,-3.104640,-2.263524,4.805987,-1.522263,4.556508,-9.068427,1.656441,7.591425,7.220021,3.822328,3.371264,8.825886,-5.555904,3.640080,8.280450,5.765530,1.681580,1.266284,5.236241,0.739588,9.879566,-4.304227,9.337148,-8.106214,-1.643085,-9.479589,5.320154,2.218741,0.668858,-5.544199,6.364353,-0.258461,8.934589,1.258941,2.979120,5.153653,-6.798377,-8.848189,-5.943865,-8.952356,-0.095040,-7.595979,-7.137659,7.862531,1.748395,6.440577,3.790745,9.394494,5.064070,8.517541,6.486669,-6.042818,8.298083,9.038672,6.684099,-8.666099,-7.564234,-6.658937,-4.856356,7.733071,4.341868,-0.366676,-1.106317,-4.180294,2.338305,5.262628,-3.234342,-9.072440,-7.719141,2.133800,-3.317753,6.272853,9.088764,1.159449,-2.137296,9.571504,8.775563,-5.226137,3.588391,-5.166460,3.339143,3.840254,9.836791,0.199411,5.619034,8.532027,-7.395580,9.903116,-7.888292,-3.369554,1.232396,9.039814,8.742332,-0.309685,-1.033198,6.045791,-4.653909,2.767887,6.480797,4.982514,-9.250039,-6.615058,-6.147083,-1.604565,-2.008658,9.497102,-2.842556,0.776144,-6.942118,-3.054846,-4.343262,-6.266126,-0.069587,-4.472820,-5.553023,-8.735789,-9.475057,-0.399287,-2.473989,-1.821398,5.812117,-0.714985,-7.831309,3.641090,-3.474105,1.388138,-6.371980,0.153993,5.019723,-7.837984,-6.433150,-3.346400,5.009114,8.357316,7.760012,-1.197033,3.979827,-2.892892,-8.524478,-1.708785,4.832584,3.829974,-0.157108,-6.710333,-6.978489,1.901192,-1.123654,-4.038981,-5.777456,8.303213,2.337919,-5.215378,1.532420,-7.921007,1.046100,-3.294076,-3.083384,-3.143938,-9.124883,-8.864838,2.932721,4.048258,-6.780400,1.107022,3.397177,-8.065797,-0.872278,8.320456,-8.551298,-4.771607,7.713706,-3.088716,-1.530717,-4.433430,-8.700149,-7.863755,-7.142306,7.657146,4.403915,-6.559268,0.781703,4.155493,5.927685,6.185680,-7.291821,8.600002,-0.100419,5.004882,-9.558399,-0.088981,-7.491229,-8.271050,-9.314733,4.301634,-0.496633,8.613448,5.283736,-3.683252,9.333746,-1.889095,8.932143,7.128146,9.209563,-6.461450,-2.586798,-2.405701,5.371805,-2.741631,-0.251156,2.760799,0.532983,8.196451,1.219114,6.041598,6.829868,-0.120429,-2.866243,2.568341,-5.679196,1.894617,-6.987011,-2.360710,5.678853,2.341953,-1.412809,-3.065649,8.626247,-4.296202,9.805894,-5.076830,8.711232,2.895540,-3.144855,-6.868495,9.419339,-8.811341,1.438561,8.183074,6.713015,8.450621,-6.245935,6.942182,2.133507,-8.243148,8.685243,2.468495,-8.189463,-8.344183,0.608429,7.465601,8.874944,-2.626404,-7.278726,6.531625,5.273906,-7.720371,-8.510379,8.763986,9.285498,3.417783,-4.789588,-8.733604,2.022097,-0.639452,8.238219,1.225475,7.557505,8.471472,-2.240927,2.073757,3.750753,1.857735,8.861560,7.846408,-4.155822,4.854686,-4.292950,1.318944,3.768937,-7.149450,-9.801599,0.412484,-6.169326,2.150059,7.734560,-6.620780,-7.727487,-1.991609,-1.940683,7.193461,-3.216491,-8.589726,-8.951706,4.591154,3.545334,-4.301596,6.831677,1.555800,-3.396805,-0.939989,3.963651,1.121084,-3.604274,6.321314,0.016587,-8.584721,4.186759,-0.549986,-8.606126,6.269320,-6.268173,9.361101,8.276914,1.884695,-4.456731,9.717897,-8.358560,7.369729,1.377214,8.937149,3.341339,-9.406989,-2.876817,-0.719470,-6.877883,-0.102767,6.157046,4.617155,-9.406353,6.459385,-6.616904,-2.287533,5.152209,-5.450013,-1.400617,9.746142,6.479492,4.502012,6.069640,-1.104590,8.706114,-6.615886,2.471081,-0.175035,-5.858131,-7.075472,-9.249204,4.579945,-9.960399,-0.422708,1.541002,2.012387,-3.175026,0.174644,-3.463271,9.915638,-2.679063,4.073368,9.273385,-0.519576,3.861054,3.557358,5.995149,1.638070,-3.264054,6.891240,9.729526,-4.508031,3.993148,9.696779,8.137357,5.484388,-0.212436,9.236862,-7.437464,3.807326,-0.756303,-9.109281,5.912960,-5.044810,9.118769,-1.768717,-2.403128,-8.589044,-7.692242,8.152220,5.419627,0.640924,2.446237,9.347591,-0.951712,3.301760,2.779100,6.006668,3.876141,-5.824265,2.245262,-2.901214,3.886775,2.387141,-5.138954,-2.889090,9.253250,-2.904265,-0.682067,2.179157,-8.740918,-8.071857,-9.944886,3.648519,2.962196,-0.988879,-7.482999,-5.954548,-2.878561,6.576933,-8.214030,-0.520482,1.593152,8.007161,-7.573077,7.867176,6.318444,2.727115,9.928909,-0.065638,-3.923346,2.497247,1.759899,4.663956,6.445390,-2.723291,-2.447871,9.011078,8.375041,8.708927,6.283247,4.249002,-5.647987,-7.967794,3.049844,-0.201152,-5.018903,-3.777673,9.403684,4.659100,-5.258285,2.093398,-7.661234,-1.625398,3.611472,1.528127,-4.209921,1.304162,6.772276,-7.323403,-8.461901,3.540022,-2.003501,-8.579575,3.393010,-7.508421,-6.559573,-4.758312,7.479952,-9.729945,-5.480017,6.365164,-8.501593,-8.748542,8.984472,-3.381072,0.787293,-0.100999,2.184291,-5.764269,-3.955497,-4.288339,-7.628410,6.417763,-9.817803,-0.375285,5.822085,0.178482,-2.860024,-2.948074,2.743647,-7.312780,-5.223191,-9.689690,7.454953,-8.778193,-1.645418,-3.667038,1.074561,-9.301854,-8.695959,-7.923906,-3.019894,9.467278,7.870480,-3.648675,2.527993,-4.751297,3.725889,2.666328,5.164900,-8.666569,5.646356,-1.311955,-5.026346,-0.901436,9.492155,7.915414,-2.691958,-3.281462,-0.489243,-9.788231,9.008937,5.725398,-8.710770,-2.735454,-1.745701,6.906239,3.985849,-8.252067,-6.813291,-9.827047,5.846249,3.008934,5.141230,-4.040985,9.350757,6.484955,3.178867,8.277783,1.741695,2.755810,2.697340,5.665241,-2.598037,-6.866379,-8.356676,-6.234054,-1.097785,-2.838638,0.386016,3.353900], dtype = "float64")#candidate|4698|(1176,)|const|float64
call_4697 = relay.TupleGetItem(func_1796_call(relay.reshape(const_4698.astype('float64'), [1176,])), 2)
call_4699 = relay.TupleGetItem(func_1798_call(relay.reshape(const_4698.astype('float64'), [1176,])), 2)
func_3577_call = mod.get_global_var('func_3577')
func_3580_call = mutated_mod.get_global_var('func_3580')
var_4719 = relay.var("var_4719", dtype = "uint16", shape = (5, 210))#candidate|4719|(5, 210)|var|uint16
call_4718 = relay.TupleGetItem(func_3577_call(relay.reshape(var_4719.astype('uint16'), [7, 10, 15])), 2)
call_4720 = relay.TupleGetItem(func_3580_call(relay.reshape(var_4719.astype('uint16'), [7, 10, 15])), 2)
output = relay.Tuple([call_4690,call_4697,const_4698,call_4718,var_4719,])
output2 = relay.Tuple([call_4691,call_4699,const_4698,call_4720,var_4719,])
func_4731 = relay.Function([var_4719,], output)
mod['func_4731'] = func_4731
mod = relay.transform.InferType()(mod)
var_4732 = relay.var("var_4732", dtype = "uint16", shape = (5, 210))#candidate|4732|(5, 210)|var|uint16
output = func_4731(var_4732)
func_4733 = relay.Function([var_4732], output)
mutated_mod['func_4733'] = func_4733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2712_call = mod.get_global_var('func_2712')
func_2714_call = mutated_mod.get_global_var('func_2714')
call_4783 = func_2712_call()
call_4784 = func_2712_call()
output = call_4783
output2 = call_4784
func_4785 = relay.Function([], output)
mod['func_4785'] = func_4785
mod = relay.transform.InferType()(mod)
output = func_4785()
func_4786 = relay.Function([], output)
mutated_mod['func_4786'] = func_4786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3347_call = mod.get_global_var('func_3347')
func_3349_call = mutated_mod.get_global_var('func_3349')
call_4814 = func_3347_call()
call_4815 = func_3347_call()
func_3577_call = mod.get_global_var('func_3577')
func_3580_call = mutated_mod.get_global_var('func_3580')
const_4834 = relay.const([[-1,10,-5,-2,-2,-8,-7,-6,-6,6,-7,-5,10,-6,-9,5,-7,9,-6,6,10,-6,-1,-2,9,-8,10,-3,1,-7,-8,-2,7,-8,4,2,-10,-3,-1,9,-10,-6,2,1,9,-6,10,1,-1,10,-4,1,1,4,-6,-1,2,9,7,7,-9,10,-1,7,-1,-7,-1,9,-2,-5,-6,7,4,-1,-7,4,9,7,8,-2,-5,5,7,10,-7,-10,-9,-10,-4,-3,-9,-10,2,8,3,10,9,4,1,7,-8,10,5,-2,3,1,2,-10,-1,6,-2,-2,4,-9,1,-3,-3,6,-7,9,4,1,3,2,-4,10,7,-7,9,7,3,8,-5,6,-3,-1,6,10,-7,-3,-3,9,4,-4,-3,4,-3,2,7,9,2,4,5,-7,-10,-3,3,4,9,4,-1,6,1,1,7,-7,-1,6,8,-10,6,-1,7,-10,-5,6,1,7,3,9,7,8,-8,6,10,4,1,-6,-3,3,-9,2,-5,3,7,8,9,-4,2,4,-7,-9,6,-7,2,-6,8,-2,-7,1],[-8,-9,-4,-7,-6,8,3,-4,-3,-7,10,5,-1,1,3,-3,-10,9,7,10,-10,7,-8,-10,1,-5,5,8,-8,-6,-2,3,3,-8,9,-4,-8,10,-1,6,-2,-2,2,2,9,-2,-9,3,-6,-2,8,-4,6,-2,-6,8,1,4,-8,-5,6,-7,10,-7,-2,-9,-5,-7,-7,-8,7,-3,-6,2,-5,2,-2,-8,-3,-7,6,-5,1,1,-3,4,-5,-8,6,-6,7,-2,-8,-1,7,-6,-8,-3,-5,10,3,5,1,-10,3,7,5,9,2,-4,2,2,-1,10,9,-3,1,2,-1,-6,10,6,-3,-1,-7,-3,-5,10,10,-3,7,1,3,-10,6,1,-1,1,4,-10,7,1,-10,9,8,-9,9,4,3,-6,-4,-5,6,1,-8,-2,-8,-6,-3,-8,-10,-7,-9,10,-7,-1,5,-5,1,-2,1,-3,-4,-9,5,-7,6,-3,7,7,10,-6,-3,8,9,3,2,10,5,5,7,-5,8,-8,-1,-10,2,-8,6,-10,-5,-6,-9,7,6,-3,3,-5,-6,-7],[-7,-8,10,-3,3,3,6,-7,6,8,5,4,-3,-9,2,-6,3,-6,-1,1,-2,-3,4,3,3,3,-5,6,-5,-7,-2,-6,10,-8,-2,-6,-5,-5,9,10,-9,10,9,-4,-2,3,-7,-7,-2,-9,-7,-3,5,1,3,-6,4,10,1,-8,-6,-6,-2,9,9,-10,-6,9,10,3,-1,8,4,-9,-2,9,9,-1,8,5,-10,6,-10,5,-6,1,-9,5,7,-10,2,-4,-3,-2,-5,-10,3,-2,2,-1,8,-6,-5,10,-4,8,10,-6,9,5,6,10,3,2,-1,-4,9,6,10,3,-8,1,-4,-10,7,-6,3,10,-10,-3,-5,10,6,7,3,9,10,-7,7,9,3,4,-3,-3,-9,6,3,8,-1,3,-5,-3,-4,-3,-8,-4,-8,-8,-7,6,7,-9,-7,10,-4,-1,-9,5,-5,-4,-9,-5,-1,9,-5,-1,6,-5,-7,-10,9,-9,6,-2,2,-3,6,-1,-8,-6,-5,7,7,6,-4,6,-10,2,10,-4,-9,5,-2,6,-7,4,9,5,1,3],[-10,3,-3,3,-8,-6,-3,-6,-7,8,5,6,-3,-2,-4,4,-4,-3,1,-8,4,-5,5,3,-4,-8,5,2,6,-6,9,-4,6,-9,1,5,-3,2,4,2,10,-6,3,-3,-4,-9,9,-7,9,4,-3,-7,9,-4,9,-10,5,2,-6,9,5,2,-3,1,-2,4,-3,-2,4,-5,2,-2,3,-9,10,-8,7,-3,8,-2,8,-8,9,-3,-7,-6,8,-8,-3,-10,6,-9,8,3,5,-8,3,6,-5,-5,-9,-1,-10,-8,7,-5,5,-8,-8,-9,-6,8,3,1,2,10,10,6,4,2,-1,-4,1,-9,3,-1,-7,10,2,-7,9,4,3,-9,6,-6,-8,-5,-4,-9,-4,-8,1,8,9,-8,7,8,-3,-4,-8,-10,-5,-7,-9,6,7,4,-3,-9,-2,-1,-8,6,9,4,2,-4,-9,6,5,3,7,10,-2,2,-8,10,5,-9,7,10,7,6,6,4,-3,3,-6,10,4,9,-7,7,-6,4,2,-5,-1,5,-3,9,9,8,7,-1,-9,2,-1,8],[7,-5,10,-10,-10,-6,-7,9,-7,9,-4,-6,3,3,-8,3,4,4,5,5,-10,-8,-8,-1,5,-10,10,-6,-3,-7,9,-6,-8,-9,6,-10,-8,1,7,-10,2,3,-7,5,7,1,-1,-1,9,2,7,-10,-10,1,-1,-2,-3,4,-4,-2,-10,9,9,-10,1,4,6,2,-2,-5,-4,-7,4,10,2,-8,-4,6,6,-4,10,4,-1,-9,-1,-8,-3,-3,8,-4,-5,7,-9,5,-8,4,-8,-1,-7,1,-7,3,4,7,-1,-6,-3,-8,-5,2,5,-9,-6,-1,3,3,9,-1,5,-8,-9,5,-5,-4,9,4,-2,6,-5,3,8,-9,-3,1,8,-4,-4,-9,-3,9,-9,-7,-8,-10,-1,3,10,-8,4,-1,-9,-1,4,-1,-5,1,5,-6,3,8,-1,-5,4,-4,-1,3,9,-2,-6,-2,-5,-4,2,-5,-7,1,3,9,-9,8,-7,1,-8,1,-6,-4,7,-3,-7,-6,-1,-4,-4,4,7,3,-6,2,-7,-8,5,6,-10,-2,5,-3,6,-1,-2,4]], dtype = "uint16")#candidate|4834|(5, 210)|const|uint16
call_4833 = relay.TupleGetItem(func_3577_call(relay.reshape(const_4834.astype('uint16'), [7, 10, 15])), 0)
call_4835 = relay.TupleGetItem(func_3580_call(relay.reshape(const_4834.astype('uint16'), [7, 10, 15])), 0)
uop_4845 = relay.asinh(const_4834.astype('float32')) # shape=(5, 210)
func_3347_call = mod.get_global_var('func_3347')
func_3349_call = mutated_mod.get_global_var('func_3349')
call_4855 = func_3347_call()
call_4856 = func_3347_call()
var_4857 = relay.var("var_4857", dtype = "float32", shape = (5, 210))#candidate|4857|(5, 210)|var|float32
bop_4858 = relay.bitwise_and(uop_4845.astype('uint32'), relay.reshape(var_4857.astype('uint32'), relay.shape_of(uop_4845))) # shape=(5, 210)
output = relay.Tuple([call_4814,call_4833,call_4855,bop_4858,])
output2 = relay.Tuple([call_4815,call_4835,call_4856,bop_4858,])
func_4861 = relay.Function([var_4857,], output)
mod['func_4861'] = func_4861
mod = relay.transform.InferType()(mod)
var_4862 = relay.var("var_4862", dtype = "float32", shape = (5, 210))#candidate|4862|(5, 210)|var|float32
output = func_4861(var_4862)
func_4863 = relay.Function([var_4862], output)
mutated_mod['func_4863'] = func_4863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2712_call = mod.get_global_var('func_2712')
func_2714_call = mutated_mod.get_global_var('func_2714')
call_4886 = func_2712_call()
call_4887 = func_2712_call()
func_1913_call = mod.get_global_var('func_1913')
func_1915_call = mutated_mod.get_global_var('func_1915')
call_4911 = func_1913_call()
call_4912 = func_1913_call()
func_3498_call = mod.get_global_var('func_3498')
func_3499_call = mutated_mod.get_global_var('func_3499')
call_4917 = relay.TupleGetItem(func_3498_call(), 0)
call_4918 = relay.TupleGetItem(func_3499_call(), 0)
func_1665_call = mod.get_global_var('func_1665')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_4925 = relay.TupleGetItem(func_1665_call(), 0)
call_4926 = relay.TupleGetItem(func_1667_call(), 0)
var_4933 = relay.var("var_4933", dtype = "bool", shape = (8, 1))#candidate|4933|(8, 1)|var|bool
bop_4934 = relay.logical_and(call_4925.astype('bool'), var_4933.astype('bool')) # shape=(8, 1)
bop_4937 = relay.logical_and(call_4926.astype('bool'), var_4933.astype('bool')) # shape=(8, 1)
func_4298_call = mod.get_global_var('func_4298')
func_4302_call = mutated_mod.get_global_var('func_4302')
const_4955 = relay.const([6.566439,1.249079,8.756411,9.918255,-2.026917,-3.168170,-5.569666,-6.473987,5.351009,6.593637,4.711664,2.110763,-6.063300,-0.822989,-9.999824,9.849929,5.555196,0.162182,-0.364181,-0.974792,9.328660,-1.566793,9.162196,8.885325,-3.774609,6.747463,1.572025,8.561244,-7.468880,-9.730201,-4.382489,-0.807392,-8.164036,0.278388,-5.163501,-2.915699,-9.394648,5.255290,7.189786,1.211211,5.715436,9.720639,6.582141,-9.605293,-7.814003,-9.662798,-9.552347,8.700778], dtype = "float64")#candidate|4955|(48,)|const|float64
var_4956 = relay.var("var_4956", dtype = "float64", shape = (588, 2))#candidate|4956|(588, 2)|var|float64
call_4954 = relay.TupleGetItem(func_4298_call(relay.reshape(const_4955.astype('float64'), [6, 2, 4]), relay.reshape(var_4956.astype('float64'), [1, 1176]), ), 0)
call_4957 = relay.TupleGetItem(func_4302_call(relay.reshape(const_4955.astype('float64'), [6, 2, 4]), relay.reshape(var_4956.astype('float64'), [1, 1176]), ), 0)
output = relay.Tuple([call_4886,call_4911,call_4917,bop_4934,call_4954,const_4955,var_4956,])
output2 = relay.Tuple([call_4887,call_4912,call_4918,bop_4937,call_4957,const_4955,var_4956,])
func_4963 = relay.Function([var_4933,var_4956,], output)
mod['func_4963'] = func_4963
mod = relay.transform.InferType()(mod)
var_4964 = relay.var("var_4964", dtype = "bool", shape = (8, 1))#candidate|4964|(8, 1)|var|bool
var_4965 = relay.var("var_4965", dtype = "float64", shape = (588, 2))#candidate|4965|(588, 2)|var|float64
output = func_4963(var_4964,var_4965,)
func_4966 = relay.Function([var_4964,var_4965,], output)
mutated_mod['func_4966'] = func_4966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1936_call = mod.get_global_var('func_1936')
func_1938_call = mutated_mod.get_global_var('func_1938')
call_4983 = func_1936_call()
call_4984 = func_1936_call()
func_4963_call = mod.get_global_var('func_4963')
func_4966_call = mutated_mod.get_global_var('func_4966')
var_4992 = relay.var("var_4992", dtype = "bool", shape = (8,))#candidate|4992|(8,)|var|bool
const_4993 = relay.const([[-5.748517,-9.255192],[9.689356,-4.322691],[-3.890756,8.694911],[6.501994,-3.345033],[-3.661504,4.951902],[0.458237,-9.920703],[6.324121,-7.171805],[1.891539,3.430880],[-4.949793,2.263915],[-4.460589,6.650902],[-3.021436,4.865546],[-0.406129,-7.799202],[-5.250238,7.527407],[9.318196,-6.109479],[1.869346,-1.326640],[-4.047473,-9.202303],[-5.080421,-9.813625],[7.418294,6.422394],[7.969463,1.633063],[-9.139809,-5.369563],[-4.005066,7.621533],[5.344281,-5.225645],[-3.273758,2.025534],[-6.457288,3.478315],[-9.316501,1.867692],[-4.007068,6.226307],[7.656833,9.503393],[-6.247249,-9.602069],[3.422390,-3.186940],[-9.824797,0.104095],[-4.231821,5.599850],[-7.497923,1.388417],[9.052527,-1.098538],[3.323879,5.946591],[9.447572,8.670060],[-5.807040,-4.223673],[8.315558,-8.446768],[0.997230,-0.637339],[6.178799,-3.102934],[6.731661,-5.709474],[-8.981332,-3.424273],[-3.640276,5.047998],[-7.689287,5.391080],[-5.661272,7.194980],[-2.308610,7.959059],[8.455691,6.835656],[-2.576283,5.301566],[1.278396,-0.556016],[-7.113518,-4.179363],[-9.872916,-3.739076],[-4.828218,5.929250],[3.731092,-2.894101],[-5.453997,3.791103],[6.440051,-1.858233],[-2.027052,4.649426],[1.378759,-6.408902],[-5.457806,-4.024180],[-5.819082,-4.077061],[-0.863954,0.701004],[-4.786318,-9.056745],[-7.146924,-6.331355],[-1.819392,8.200163],[-0.480774,8.725990],[-2.820209,-6.696850],[-4.823828,3.278865],[8.738632,8.665093],[8.989511,-3.716537],[-8.406372,-3.383755],[-9.623767,-1.115180],[-2.414344,-4.829596],[0.054683,-9.128009],[3.084268,-8.637603],[-4.166128,-4.564185],[5.021799,9.794842],[-8.940849,-9.358673],[-1.777213,3.544313],[-4.895422,-7.478502],[1.278672,6.304059],[-7.533286,-9.618809],[-6.810960,2.379103],[-1.550068,7.904385],[3.523655,-9.803362],[-7.224169,-3.714682],[-6.859566,3.251632],[9.851814,2.181556],[-1.067706,2.946619],[-9.529064,-5.548525],[8.897216,8.748038],[5.459827,2.066617],[-1.589473,8.486813],[7.411834,5.991302],[0.530052,-3.925021],[-2.261926,-7.279627],[-7.633333,2.430413],[8.687269,-3.894730],[7.677503,4.508248],[-0.708565,2.010798],[-2.289025,4.484059],[-7.618894,0.425123],[1.949836,5.576556],[4.740493,0.261300],[9.486879,8.599176],[-1.351059,9.608831],[2.769402,9.283744],[-9.754422,-3.339833],[4.494997,-9.706136],[7.780967,4.296249],[8.455043,-3.897693],[-4.820221,-7.653469],[9.281619,1.942223],[2.498512,8.334338],[6.598322,-6.554078],[-4.574280,-8.864560],[-4.075522,2.022850],[6.718668,6.977751],[5.091950,8.446665],[5.802237,-5.727268],[9.471305,-7.806533],[-0.280053,-7.473395],[-3.409037,9.183030],[4.220035,-7.980401],[-9.621608,6.092895],[5.582803,-5.249322],[0.517050,-3.030281],[-6.808282,8.321918],[-3.938673,-9.954356],[3.426770,-9.829757],[-8.867994,-3.022071],[-4.030005,7.208053],[4.835838,-6.233435],[2.982073,0.949025],[-9.763593,6.521958],[-0.740125,5.851023],[3.148633,-7.724563],[-7.429864,-8.682650],[-0.249378,-8.692214],[-3.702420,-4.122563],[2.303867,-0.329153],[2.960851,3.713470],[1.523660,-7.724509],[6.258240,8.887132],[-7.940097,9.256309],[-2.356930,7.970939],[4.973749,2.270272],[6.272226,7.672423],[-2.310151,-4.436672],[9.227808,-7.452495],[-6.330875,9.920775],[-6.875685,-2.387262],[-6.741999,4.799092],[-3.087650,7.483303],[-2.671399,6.622081],[-1.384871,-8.691727],[-6.249312,1.950911],[-7.619284,-2.410840],[-3.815593,-5.908405],[-3.551983,9.082096],[3.812049,-4.767134],[2.197229,9.460333],[-0.486977,-7.733601],[5.894303,-5.018496],[9.345750,5.007556],[9.884682,-5.493714],[8.120206,-3.733191],[-3.892975,-3.850880],[-9.791419,9.761283],[2.319986,6.218471],[4.692748,-8.453939],[7.143753,-1.938123],[-8.082779,-7.302458],[0.952764,-6.895556],[-0.062092,9.920325],[-7.113871,-4.675961],[-2.077683,2.447112],[-3.103004,2.747841],[-8.092625,-5.595749],[-9.943048,-3.156808],[-3.768789,-1.567270],[4.612169,9.763176],[0.691995,-1.394554],[-3.054018,-1.735212],[-6.282001,-3.083047],[0.709644,-3.820022],[-5.902662,4.959039],[5.249795,5.469747],[-9.164467,-9.480981],[-6.093075,5.104036],[-6.071819,-2.029532],[-1.438337,3.286325],[-6.552125,1.280193],[7.800976,4.653315],[-9.291296,3.864707],[-2.136325,-3.066030],[-5.396114,-8.146474],[-7.032434,4.866985],[-7.297356,7.811384],[-3.026881,0.925906],[4.784335,-4.348341],[3.170284,-5.989963],[-1.391371,2.717398],[-5.324476,-6.177726],[-3.557239,-7.014469],[-8.631030,0.738201],[4.797435,-7.209231],[2.975401,-2.396933],[-1.836570,-0.146107],[-2.333909,-9.793108],[-9.458626,1.201682],[8.225607,8.814241],[-9.284769,-7.558262],[8.862835,0.135016],[-0.800741,0.208782],[-4.781385,-2.952129],[-6.528002,-6.671192],[8.115562,-1.394068],[-4.956317,7.987818],[8.672370,-0.542223],[-4.369009,-8.243892],[-6.917947,-0.841309],[0.183858,6.007019],[0.827923,7.775073],[-9.892508,-9.061339],[-8.601738,1.323238],[-4.659783,-8.343325],[5.012629,3.238597],[3.037855,-3.546088],[-2.686006,-3.759284],[-2.424204,2.777712],[-1.754606,3.397050],[-9.242759,-0.662281],[-3.415047,8.211696],[-7.744464,-5.874673],[-3.086227,6.053257],[-7.799456,-5.919551],[-3.485678,-8.359712],[-5.754114,-5.353883],[-5.828477,1.041633],[3.473402,5.764259],[7.364279,-3.016620],[-6.576013,8.324072],[4.322168,-6.904328],[-5.180461,-2.719251],[-8.538250,8.162303],[-0.398293,6.557808],[-4.529146,9.517805],[-6.157886,7.226685],[8.074135,-5.521997],[0.084910,5.735646],[-0.888064,-2.818435],[-4.740063,-4.992326],[6.279358,5.291600],[8.225338,3.021553],[4.362037,-2.703213],[0.039751,5.050129],[6.777546,2.935310],[7.860408,5.388153],[-4.111909,7.181336],[-7.767111,6.067209],[9.173089,7.306826],[5.446513,-9.745189],[2.866176,3.716564],[9.042824,-3.372640],[-5.411408,8.453700],[-8.946731,8.590923],[-2.797126,4.848548],[-2.772641,-7.221494],[3.005231,4.932207],[-6.332445,1.669483],[-8.423864,8.714768],[8.512003,-8.996340],[7.878406,4.586333],[9.520732,-2.960038],[3.997128,-9.160931],[1.162721,-8.331044],[9.429874,2.709571],[0.279755,5.646772],[5.574113,2.226350],[-4.088221,-6.711128],[7.754220,3.753206],[3.345066,-3.272832],[1.150198,-6.317916],[-2.612046,6.363518],[-1.154253,9.862027],[3.308847,9.617783],[2.054657,1.603433],[7.072019,8.591500],[-9.724636,0.505505],[2.573763,-4.273655],[-8.582255,8.596029],[1.713600,-3.237762],[0.162026,-5.986586],[2.505153,-0.893791],[-3.472278,-0.490349],[9.033042,1.961435],[1.602248,7.235121],[-1.858953,3.351084],[6.207195,6.592757],[-4.707960,-9.280958],[-1.442342,-9.053870],[0.508230,-1.748829],[6.576099,4.778300],[4.759756,-1.003490],[7.138023,0.219778],[3.104909,-5.462517],[7.607999,-3.051631],[-4.288430,6.117184],[3.548134,-2.998641],[-2.487749,-2.436619],[7.711597,1.436277],[-0.131106,9.162967],[2.048093,-6.581585],[-9.678882,5.237577],[-2.619819,2.042715],[3.286358,1.523544],[-5.311990,2.153128],[9.304952,-3.456887],[7.536971,4.277063],[2.675115,3.657794],[8.097773,-3.774504],[-3.543733,9.603612],[0.031343,6.171990],[9.408383,5.198359],[-5.394425,6.704673],[-3.490065,0.198787],[6.607926,-0.886326],[5.824171,6.600219],[4.789348,-7.546600],[-0.475468,-5.662563],[-3.034537,-1.608001],[5.991158,-9.902818],[-9.273234,4.715423],[1.872659,-6.379413],[2.790151,-2.807066],[-4.549374,0.919052],[8.605887,8.884467],[2.833196,0.630659],[-4.451837,7.752543],[5.986035,3.323058],[1.277256,-2.494786],[6.380003,0.641313],[9.822846,-0.259618],[-4.926754,6.736592],[4.954184,5.944503],[0.857106,0.524397],[-1.113607,1.314128],[-1.123942,6.302947],[5.203029,-6.638293],[-5.650769,9.025557],[3.481856,1.529230],[8.219752,6.357968],[8.656951,0.104928],[5.560133,-6.544926],[2.107592,5.124090],[5.618814,-4.472131],[7.000082,7.083129],[-6.035524,1.130252],[-0.930044,8.943178],[-0.180774,6.811917],[2.772549,-5.570908],[6.034470,-4.990008],[-6.151613,-8.470216],[-7.030087,-3.205014],[8.853914,6.056333],[-2.501521,-1.288326],[3.786301,-4.259034],[-7.748167,-5.700335],[-7.472326,1.864339],[4.387824,-4.840604],[7.420980,9.228159],[0.902697,0.457446],[-0.389187,2.342859],[-1.498884,0.397254],[0.720002,2.911757],[7.036391,-4.671145],[-7.585363,9.446073],[5.093612,4.585832],[-5.081554,0.643474],[-3.503715,9.133241],[5.574892,2.819815],[-1.351798,-4.574090],[-2.668649,0.925366],[0.999434,3.060149],[1.715928,3.846397],[-8.344558,-4.770355],[-8.966968,1.132039],[-9.443741,9.642875],[1.835022,0.666333],[3.959871,1.697573],[6.710977,-9.481282],[-0.885952,-2.297986],[-6.795743,8.422301],[-6.767569,-6.303710],[7.480615,4.170816],[-8.402806,9.717573],[1.974226,8.354570],[-1.466115,-2.306139],[7.498966,-9.315785],[-4.865106,-1.019821],[1.528309,-2.433034],[7.731887,-8.547547],[-4.724763,-6.155857],[-2.322683,-8.653655],[8.969507,-9.085790],[-0.336816,9.698208],[4.865206,-5.529134],[4.615229,6.742196],[-4.279358,-0.395328],[-7.927200,-5.780270],[3.897200,8.346995],[-5.972666,5.500006],[0.868123,-2.657423],[2.843058,0.468696],[4.968157,-6.520110],[-4.965886,3.287345],[3.941108,-6.042701],[-9.279514,-1.907210],[-4.962830,2.632736],[7.185976,-2.612387],[2.253774,9.170039],[-7.167464,5.487554],[-2.461661,-0.278682],[7.430584,5.405850],[-5.218929,-6.793438],[-7.584637,-2.151461],[-2.579812,8.754917],[-6.833968,-1.569981],[-9.901471,-7.660032],[8.782708,1.581738],[-9.459080,-5.859852],[7.919385,-1.660999],[-9.863801,0.764456],[-0.935073,1.728774],[2.883230,-4.650730],[-5.827201,3.787595],[-9.705484,9.624873],[-9.752243,3.300556],[3.556089,-5.413591],[8.309408,-4.671880],[-8.454630,-2.523012],[3.329789,9.550224],[9.256030,-6.797296],[2.862013,-3.743910],[-6.605946,0.280618],[-9.258630,2.722817],[-4.738925,7.843088],[-8.475331,9.821681],[1.532625,2.137004],[9.828135,5.428312],[5.362325,-8.765620],[-4.168531,-9.579166],[2.667049,0.536168],[0.763930,8.760683],[-5.664559,3.396713],[-3.996942,7.356015],[6.900760,-9.973579],[-1.928737,1.028136],[7.092232,-4.364792],[-7.123685,-4.739742],[-5.749906,-3.425631],[-9.832243,6.774951],[-8.291368,-8.929222],[-2.600757,-5.736852],[-8.355540,-9.339634],[-6.984292,-8.582169],[-2.655553,9.370046],[-2.054372,-2.569539],[5.897086,-6.326030],[-5.217798,4.719936],[-8.815556,5.258171],[3.401342,-5.020410],[-5.771590,-1.696868],[-9.024261,-8.424399],[8.582205,-1.540907],[-8.361527,-0.704093],[7.135436,1.146788],[3.219915,-2.016457],[-3.110975,-4.302052],[2.691850,-0.927164],[3.978971,-3.816103],[9.081260,-4.568725],[6.006319,-8.975124],[5.658681,4.266743],[2.751762,-9.397043],[4.487367,8.398708],[-4.310305,-1.127047],[-9.478835,2.609786],[6.519363,-6.229471],[1.510646,-1.161531],[5.672070,-9.516365],[9.371585,5.611033],[-9.670716,5.047535],[-8.270027,-2.385087],[-9.769918,-9.593146],[2.064943,8.209438],[0.203370,5.031983],[-5.853218,5.723112],[4.316977,0.337590],[-3.540396,5.028095],[-5.580712,-2.676811],[5.693259,-9.818655],[8.972530,2.310981],[-7.753234,-1.161143],[-5.158864,-0.200625],[1.544672,-4.589101],[5.527324,8.648823],[-1.669995,5.757458],[-6.570820,3.383780],[-7.253235,3.190666],[-5.294213,-2.730852],[1.798099,-7.095031],[-5.303534,9.945922],[2.508110,-1.001764],[8.873655,-7.144820],[2.374272,-9.380970],[3.502427,7.745353],[2.154123,-5.307899],[5.938836,1.250689],[8.935221,-8.892579],[-6.212322,1.215578],[7.344197,2.356552],[9.247118,-8.523563],[1.513542,-4.381422],[-1.567707,-8.847602],[0.372741,5.140502],[7.686527,3.629654],[3.749738,-9.239267],[4.882468,9.347644],[-1.244623,3.534301],[-0.932852,-9.238275],[8.738432,-2.950921],[-2.143720,9.503436],[6.255517,4.822638],[9.151882,8.911369],[-4.205780,6.473837],[6.941008,5.564900],[4.599828,-4.173818],[-7.318747,8.005259],[1.373976,-0.163043],[-3.458657,8.774354],[-4.217258,-0.138333],[-1.598743,-4.325648],[8.590402,-9.070211],[-5.583403,-4.125305],[5.828857,8.829852],[5.729689,6.425844],[8.252105,2.497460],[1.237621,3.804019],[4.251179,-2.265204],[-0.334530,-2.471326],[-0.268961,-7.441925],[-5.176179,-9.787860],[2.556684,-2.449859],[-1.180135,-6.295176],[9.979513,7.330842],[-6.633677,-3.398647],[-5.729130,1.671502],[-9.102715,-8.403203],[7.391304,7.481576],[-8.758331,2.414786],[-4.735526,-5.430126],[7.952581,-1.205032],[-4.003545,1.991755],[-0.009294,-6.478484],[-9.534087,4.747199],[-0.913770,3.625915],[3.195574,9.719683],[-1.584460,2.803784],[-0.642699,3.556101],[-4.614006,-8.259609],[8.764928,-9.203760],[-5.834901,-6.897749],[-2.175549,9.014220],[-5.932049,-5.926460],[1.701987,5.688194],[-1.584835,-3.151390],[-5.025526,-9.241381],[0.140795,-9.240230],[8.029660,0.415426],[0.220318,-0.735373],[3.722414,-5.548335],[4.688979,7.645933],[5.038086,-7.094928],[-7.753088,-0.704746],[7.985753,7.311885],[-1.567238,6.291233],[-2.957921,2.254177],[0.044378,-4.260960],[7.030030,-7.800387]], dtype = "float64")#candidate|4993|(588, 2)|const|float64
call_4991 = relay.TupleGetItem(func_4963_call(relay.reshape(var_4992.astype('bool'), [8, 1]), relay.reshape(const_4993.astype('float64'), [588, 2]), ), 0)
call_4994 = relay.TupleGetItem(func_4966_call(relay.reshape(var_4992.astype('bool'), [8, 1]), relay.reshape(const_4993.astype('float64'), [588, 2]), ), 0)
func_4688_call = mod.get_global_var('func_4688')
func_4689_call = mutated_mod.get_global_var('func_4689')
call_4996 = relay.TupleGetItem(func_4688_call(), 1)
call_4997 = relay.TupleGetItem(func_4689_call(), 1)
output = relay.Tuple([call_4983,call_4991,var_4992,const_4993,call_4996,])
output2 = relay.Tuple([call_4984,call_4994,var_4992,const_4993,call_4997,])
func_5001 = relay.Function([var_4992,], output)
mod['func_5001'] = func_5001
mod = relay.transform.InferType()(mod)
var_5002 = relay.var("var_5002", dtype = "bool", shape = (8,))#candidate|5002|(8,)|var|bool
output = func_5001(var_5002)
func_5003 = relay.Function([var_5002], output)
mutated_mod['func_5003'] = func_5003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2094_call = mod.get_global_var('func_2094')
func_2096_call = mutated_mod.get_global_var('func_2096')
call_5005 = relay.TupleGetItem(func_2094_call(), 0)
call_5006 = relay.TupleGetItem(func_2096_call(), 0)
func_2820_call = mod.get_global_var('func_2820')
func_2821_call = mutated_mod.get_global_var('func_2821')
call_5025 = relay.TupleGetItem(func_2820_call(), 5)
call_5026 = relay.TupleGetItem(func_2821_call(), 5)
output = relay.Tuple([call_5005,call_5025,])
output2 = relay.Tuple([call_5006,call_5026,])
func_5042 = relay.Function([], output)
mod['func_5042'] = func_5042
mod = relay.transform.InferType()(mod)
output = func_5042()
func_5043 = relay.Function([], output)
mutated_mod['func_5043'] = func_5043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4785_call = mod.get_global_var('func_4785')
func_4786_call = mutated_mod.get_global_var('func_4786')
call_5107 = func_4785_call()
call_5108 = func_4785_call()
func_1337_call = mod.get_global_var('func_1337')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_5113 = relay.TupleGetItem(func_1337_call(), 1)
call_5114 = relay.TupleGetItem(func_1338_call(), 1)
func_2170_call = mod.get_global_var('func_2170')
func_2173_call = mutated_mod.get_global_var('func_2173')
var_5138 = relay.var("var_5138", dtype = "float64", shape = (1296,))#candidate|5138|(1296,)|var|float64
call_5137 = relay.TupleGetItem(func_2170_call(relay.reshape(var_5138.astype('float64'), [9, 16, 9])), 1)
call_5139 = relay.TupleGetItem(func_2173_call(relay.reshape(var_5138.astype('float64'), [9, 16, 9])), 1)
output = relay.Tuple([call_5107,call_5113,call_5137,var_5138,])
output2 = relay.Tuple([call_5108,call_5114,call_5139,var_5138,])
func_5150 = relay.Function([var_5138,], output)
mod['func_5150'] = func_5150
mod = relay.transform.InferType()(mod)
mutated_mod['func_5150'] = func_5150
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5151 = relay.var("var_5151", dtype = "float64", shape = (1296,))#candidate|5151|(1296,)|var|float64
func_5150_call = mutated_mod.get_global_var('func_5150')
call_5152 = func_5150_call(var_5151)
output = call_5152
func_5153 = relay.Function([var_5151], output)
mutated_mod['func_5153'] = func_5153
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2858_call = mod.get_global_var('func_2858')
func_2859_call = mutated_mod.get_global_var('func_2859')
call_5181 = func_2858_call()
call_5182 = func_2858_call()
func_2820_call = mod.get_global_var('func_2820')
func_2821_call = mutated_mod.get_global_var('func_2821')
call_5211 = relay.TupleGetItem(func_2820_call(), 6)
call_5212 = relay.TupleGetItem(func_2821_call(), 6)
output = relay.Tuple([call_5181,call_5211,])
output2 = relay.Tuple([call_5182,call_5212,])
func_5231 = relay.Function([], output)
mod['func_5231'] = func_5231
mod = relay.transform.InferType()(mod)
output = func_5231()
func_5232 = relay.Function([], output)
mutated_mod['func_5232'] = func_5232
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5253 = relay.var("var_5253", dtype = "float32", shape = (5, 14, 11))#candidate|5253|(5, 14, 11)|var|float32
uop_5254 = relay.cos(var_5253.astype('float32')) # shape=(5, 14, 11)
func_4521_call = mod.get_global_var('func_4521')
func_4525_call = mutated_mod.get_global_var('func_4525')
var_5262 = relay.var("var_5262", dtype = "uint64", shape = (1008,))#candidate|5262|(1008,)|var|uint64
call_5261 = relay.TupleGetItem(func_4521_call(relay.reshape(var_5262.astype('uint64'), [9, 16, 7]), relay.reshape(var_5262.astype('bool'), [9, 16, 7]), relay.reshape(var_5262.astype('bool'), [9, 16, 7]), ), 1)
call_5263 = relay.TupleGetItem(func_4525_call(relay.reshape(var_5262.astype('uint64'), [9, 16, 7]), relay.reshape(var_5262.astype('bool'), [9, 16, 7]), relay.reshape(var_5262.astype('bool'), [9, 16, 7]), ), 1)
bop_5268 = relay.logical_xor(uop_5254.astype('uint8'), relay.reshape(var_5253.astype('uint8'), relay.shape_of(uop_5254))) # shape=(5, 14, 11)
output = relay.Tuple([call_5261,var_5262,bop_5268,])
output2 = relay.Tuple([call_5263,var_5262,bop_5268,])
func_5282 = relay.Function([var_5253,var_5262,], output)
mod['func_5282'] = func_5282
mod = relay.transform.InferType()(mod)
mutated_mod['func_5282'] = func_5282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5282_call = mutated_mod.get_global_var('func_5282')
var_5284 = relay.var("var_5284", dtype = "float32", shape = (5, 14, 11))#candidate|5284|(5, 14, 11)|var|float32
var_5285 = relay.var("var_5285", dtype = "uint64", shape = (1008,))#candidate|5285|(1008,)|var|uint64
call_5283 = func_5282_call(var_5284,var_5285,)
output = call_5283
func_5286 = relay.Function([var_5284,var_5285,], output)
mutated_mod['func_5286'] = func_5286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2193_call = mod.get_global_var('func_2193')
func_2194_call = mutated_mod.get_global_var('func_2194')
call_5318 = relay.TupleGetItem(func_2193_call(), 2)
call_5319 = relay.TupleGetItem(func_2194_call(), 2)
output = relay.Tuple([call_5318,])
output2 = relay.Tuple([call_5319,])
func_5348 = relay.Function([], output)
mod['func_5348'] = func_5348
mod = relay.transform.InferType()(mod)
mutated_mod['func_5348'] = func_5348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5348_call = mutated_mod.get_global_var('func_5348')
call_5349 = func_5348_call()
output = call_5349
func_5350 = relay.Function([], output)
mutated_mod['func_5350'] = func_5350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2948_call = mod.get_global_var('func_2948')
func_2950_call = mutated_mod.get_global_var('func_2950')
call_5355 = relay.TupleGetItem(func_2948_call(), 0)
call_5356 = relay.TupleGetItem(func_2950_call(), 0)
output = relay.Tuple([call_5355,])
output2 = relay.Tuple([call_5356,])
func_5363 = relay.Function([], output)
mod['func_5363'] = func_5363
mod = relay.transform.InferType()(mod)
mutated_mod['func_5363'] = func_5363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5363_call = mutated_mod.get_global_var('func_5363')
call_5364 = func_5363_call()
output = call_5364
func_5365 = relay.Function([], output)
mutated_mod['func_5365'] = func_5365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4688_call = mod.get_global_var('func_4688')
func_4689_call = mutated_mod.get_global_var('func_4689')
call_5402 = relay.TupleGetItem(func_4688_call(), 1)
call_5403 = relay.TupleGetItem(func_4689_call(), 1)
output = call_5402
output2 = call_5403
func_5412 = relay.Function([], output)
mod['func_5412'] = func_5412
mod = relay.transform.InferType()(mod)
output = func_5412()
func_5413 = relay.Function([], output)
mutated_mod['func_5413'] = func_5413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4237_call = mod.get_global_var('func_4237')
func_4238_call = mutated_mod.get_global_var('func_4238')
call_5427 = relay.TupleGetItem(func_4237_call(), 0)
call_5428 = relay.TupleGetItem(func_4238_call(), 0)
func_2675_call = mod.get_global_var('func_2675')
func_2677_call = mutated_mod.get_global_var('func_2677')
var_5430 = relay.var("var_5430", dtype = "bool", shape = (260,))#candidate|5430|(260,)|var|bool
call_5429 = relay.TupleGetItem(func_2675_call(relay.reshape(var_5430.astype('bool'), [2, 10, 13])), 1)
call_5431 = relay.TupleGetItem(func_2677_call(relay.reshape(var_5430.astype('bool'), [2, 10, 13])), 1)
output = relay.Tuple([call_5427,call_5429,var_5430,])
output2 = relay.Tuple([call_5428,call_5431,var_5430,])
func_5436 = relay.Function([var_5430,], output)
mod['func_5436'] = func_5436
mod = relay.transform.InferType()(mod)
mutated_mod['func_5436'] = func_5436
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5437 = relay.var("var_5437", dtype = "bool", shape = (260,))#candidate|5437|(260,)|var|bool
func_5436_call = mutated_mod.get_global_var('func_5436')
call_5438 = func_5436_call(var_5437)
output = call_5438
func_5439 = relay.Function([var_5437], output)
mutated_mod['func_5439'] = func_5439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5042_call = mod.get_global_var('func_5042')
func_5043_call = mutated_mod.get_global_var('func_5043')
call_5441 = relay.TupleGetItem(func_5042_call(), 0)
call_5442 = relay.TupleGetItem(func_5043_call(), 0)
output = relay.Tuple([call_5441,])
output2 = relay.Tuple([call_5442,])
func_5468 = relay.Function([], output)
mod['func_5468'] = func_5468
mod = relay.transform.InferType()(mod)
output = func_5468()
func_5469 = relay.Function([], output)
mutated_mod['func_5469'] = func_5469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1498_call = mod.get_global_var('func_1498')
func_1500_call = mutated_mod.get_global_var('func_1500')
call_5585 = func_1498_call()
call_5586 = func_1498_call()
output = call_5585
output2 = call_5586
func_5603 = relay.Function([], output)
mod['func_5603'] = func_5603
mod = relay.transform.InferType()(mod)
output = func_5603()
func_5604 = relay.Function([], output)
mutated_mod['func_5604'] = func_5604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3204_call = mod.get_global_var('func_3204')
func_3205_call = mutated_mod.get_global_var('func_3205')
call_5612 = relay.TupleGetItem(func_3204_call(), 2)
call_5613 = relay.TupleGetItem(func_3205_call(), 2)
func_1665_call = mod.get_global_var('func_1665')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_5622 = relay.TupleGetItem(func_1665_call(), 0)
call_5623 = relay.TupleGetItem(func_1667_call(), 0)
output = relay.Tuple([call_5612,call_5622,])
output2 = relay.Tuple([call_5613,call_5623,])
func_5628 = relay.Function([], output)
mod['func_5628'] = func_5628
mod = relay.transform.InferType()(mod)
mutated_mod['func_5628'] = func_5628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5628_call = mutated_mod.get_global_var('func_5628')
call_5629 = func_5628_call()
output = call_5629
func_5630 = relay.Function([], output)
mutated_mod['func_5630'] = func_5630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3762_call = mod.get_global_var('func_3762')
func_3764_call = mutated_mod.get_global_var('func_3764')
call_5708 = func_3762_call()
call_5709 = func_3762_call()
const_5712 = relay.const([[[False,False,False,True,True,True,True,False,False,True],[False,True,True,True,False,False,False,True,True,True],[False,False,True,True,False,True,False,False,True,False],[True,True,False,True,False,False,False,True,False,False],[False,False,False,False,False,False,False,False,True,True],[True,False,True,False,True,True,False,True,False,True],[False,True,False,False,False,True,False,False,False,True],[False,True,True,False,True,True,True,True,True,False],[False,False,False,True,True,False,False,True,True,False],[False,True,True,False,False,True,True,False,True,False],[True,False,True,True,False,False,False,True,True,False],[False,True,False,False,False,True,False,False,False,False]],[[True,False,True,False,True,True,False,False,False,True],[False,True,True,True,False,False,True,True,True,False],[True,True,True,True,False,True,True,False,False,True],[False,True,False,False,True,True,True,True,True,True],[True,False,True,False,True,True,False,True,False,False],[True,True,True,True,True,True,False,False,False,False],[True,False,True,True,False,True,False,False,False,False],[True,True,False,False,False,True,False,False,False,False],[False,False,False,False,True,True,True,True,True,True],[False,False,False,True,False,False,False,False,False,True],[False,False,False,False,False,False,False,False,True,False],[True,True,False,True,True,True,False,True,True,True]],[[False,True,True,False,False,True,True,True,False,True],[False,False,True,False,True,False,True,True,False,False],[True,True,True,False,False,True,True,False,False,False],[True,False,True,True,True,False,False,False,True,False],[True,True,True,True,True,False,True,False,True,True],[False,False,True,False,False,True,True,False,False,True],[False,True,True,False,False,False,False,True,False,True],[True,False,False,False,True,True,False,False,False,True],[True,False,False,False,False,False,False,True,False,False],[False,True,True,False,True,False,False,True,True,True],[False,False,True,False,True,False,True,True,False,True],[True,True,False,True,False,False,True,False,False,False]],[[False,False,True,True,False,False,True,True,True,False],[False,True,True,True,True,False,True,False,True,True],[False,False,False,False,True,False,False,True,False,False],[True,False,True,False,False,True,False,True,False,True],[False,False,False,True,True,True,True,False,True,False],[True,True,True,False,True,False,False,False,True,True],[False,False,True,True,False,True,True,False,True,True],[True,True,False,True,False,True,False,True,False,False],[True,True,True,False,True,True,True,False,True,False],[True,True,True,False,True,True,False,False,False,True],[True,True,False,True,True,False,True,True,True,True],[True,False,False,True,True,False,False,False,False,True]]], dtype = "bool")#candidate|5712|(4, 12, 10)|const|bool
bop_5713 = relay.left_shift(call_5708.astype('int64'), relay.reshape(const_5712.astype('int64'), relay.shape_of(call_5708))) # shape=(4, 12, 10)
bop_5716 = relay.left_shift(call_5709.astype('int64'), relay.reshape(const_5712.astype('int64'), relay.shape_of(call_5709))) # shape=(4, 12, 10)
uop_5727 = relay.cosh(bop_5713.astype('float64')) # shape=(4, 12, 10)
uop_5729 = relay.cosh(bop_5716.astype('float64')) # shape=(4, 12, 10)
output = relay.Tuple([uop_5727,])
output2 = relay.Tuple([uop_5729,])
func_5732 = relay.Function([], output)
mod['func_5732'] = func_5732
mod = relay.transform.InferType()(mod)
output = func_5732()
func_5733 = relay.Function([], output)
mutated_mod['func_5733'] = func_5733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4244_call = mod.get_global_var('func_4244')
func_4245_call = mutated_mod.get_global_var('func_4245')
call_5743 = relay.TupleGetItem(func_4244_call(), 0)
call_5744 = relay.TupleGetItem(func_4245_call(), 0)
func_3498_call = mod.get_global_var('func_3498')
func_3499_call = mutated_mod.get_global_var('func_3499')
call_5781 = relay.TupleGetItem(func_3498_call(), 1)
call_5782 = relay.TupleGetItem(func_3499_call(), 1)
var_5784 = relay.var("var_5784", dtype = "bool", shape = (9, 15, 16))#candidate|5784|(9, 15, 16)|var|bool
bop_5785 = relay.left_shift(call_5743.astype('uint32'), var_5784.astype('uint32')) # shape=(9, 15, 16)
bop_5788 = relay.left_shift(call_5744.astype('uint32'), var_5784.astype('uint32')) # shape=(9, 15, 16)
func_1337_call = mod.get_global_var('func_1337')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_5799 = relay.TupleGetItem(func_1337_call(), 0)
call_5800 = relay.TupleGetItem(func_1338_call(), 0)
func_2320_call = mod.get_global_var('func_2320')
func_2324_call = mutated_mod.get_global_var('func_2324')
const_5805 = relay.const([-8,5,-6,-10,-2,-9,-8,9,1,8,8,-5,4,1,8,10,-4,3,-5,-3,8,8,-4,5,10,-9,5,7,5,-7,-7,8,4,-1,6,8,7,10,-4,7,8,4,-3,-3,8,9,1,-9,1,-3,-8,-3,-6,8,-7,6,2,9,1,-2,-5,6,-10,-8,7,-10,-2,-1,5,10,4,-9,8,-2,3,-9,6,-4,-2,-9,-4,7,-1,4,-8,10,-4,8,9,10,5,10,-7,-10,-5,-2,-10,-4,-7,-9,-7,-7,-9,3,-7,2,4,-3,-4,-2,2,9,4,4,-6,-6,-3,-3,10,-4,9,-10,6,6,6,1,3,-1,7,-8,-10,5,-9,-8,2,-7,8,6,1,-5,9,9,10,-10,-5,8,-5,9,-9,5,8,6,9,9,-1,1,2,1,9,-9,-10,-10,-9,-10,-7,-2,7,1,8,-8,-8,-1,8,-4,-3,-1,-7,-9,1,5,-4,-3,4,7,-5,3,5,-6,5,-9,-3,3,-3,-8,-4,10,-1,1], dtype = "int8")#candidate|5805|(198,)|const|int8
call_5804 = relay.TupleGetItem(func_2320_call(relay.reshape(const_5805.astype('int8'), [11, 6, 3]), relay.reshape(const_5805.astype('int8'), [11, 6, 3]), ), 1)
call_5806 = relay.TupleGetItem(func_2324_call(relay.reshape(const_5805.astype('int8'), [11, 6, 3]), relay.reshape(const_5805.astype('int8'), [11, 6, 3]), ), 1)
output = relay.Tuple([call_5781,bop_5785,call_5799,call_5804,const_5805,])
output2 = relay.Tuple([call_5782,bop_5788,call_5800,call_5806,const_5805,])
func_5821 = relay.Function([var_5784,], output)
mod['func_5821'] = func_5821
mod = relay.transform.InferType()(mod)
mutated_mod['func_5821'] = func_5821
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5822 = relay.var("var_5822", dtype = "bool", shape = (9, 15, 16))#candidate|5822|(9, 15, 16)|var|bool
func_5821_call = mutated_mod.get_global_var('func_5821')
call_5823 = func_5821_call(var_5822)
output = call_5823
func_5824 = relay.Function([var_5822], output)
mutated_mod['func_5824'] = func_5824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2094_call = mod.get_global_var('func_2094')
func_2096_call = mutated_mod.get_global_var('func_2096')
call_5866 = relay.TupleGetItem(func_2094_call(), 1)
call_5867 = relay.TupleGetItem(func_2096_call(), 1)
uop_5868 = relay.asinh(call_5866.astype('float32')) # shape=(2, 8, 12)
uop_5870 = relay.asinh(call_5867.astype('float32')) # shape=(2, 8, 12)
func_4963_call = mod.get_global_var('func_4963')
func_4966_call = mutated_mod.get_global_var('func_4966')
const_5882 = relay.const([False,False,True,True,True,False,False,False], dtype = "bool")#candidate|5882|(8,)|const|bool
var_5883 = relay.var("var_5883", dtype = "float64", shape = (2, 588))#candidate|5883|(2, 588)|var|float64
call_5881 = relay.TupleGetItem(func_4963_call(relay.reshape(const_5882.astype('bool'), [8, 1]), relay.reshape(var_5883.astype('float64'), [588, 2]), ), 3)
call_5884 = relay.TupleGetItem(func_4966_call(relay.reshape(const_5882.astype('bool'), [8, 1]), relay.reshape(var_5883.astype('float64'), [588, 2]), ), 3)
output = relay.Tuple([uop_5868,call_5881,const_5882,var_5883,])
output2 = relay.Tuple([uop_5870,call_5884,const_5882,var_5883,])
func_5889 = relay.Function([var_5883,], output)
mod['func_5889'] = func_5889
mod = relay.transform.InferType()(mod)
mutated_mod['func_5889'] = func_5889
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5890 = relay.var("var_5890", dtype = "float64", shape = (2, 588))#candidate|5890|(2, 588)|var|float64
func_5889_call = mutated_mod.get_global_var('func_5889')
call_5891 = func_5889_call(var_5890)
output = call_5891
func_5892 = relay.Function([var_5890], output)
mutated_mod['func_5892'] = func_5892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4349_call = mod.get_global_var('func_4349')
func_4351_call = mutated_mod.get_global_var('func_4351')
call_5899 = func_4349_call()
call_5900 = func_4349_call()
uop_5915 = relay.sqrt(call_5899.astype('float64')) # shape=(4, 12, 10)
uop_5917 = relay.sqrt(call_5900.astype('float64')) # shape=(4, 12, 10)
bop_5919 = relay.bitwise_or(call_5899.astype('uint32'), relay.reshape(uop_5915.astype('uint32'), relay.shape_of(call_5899))) # shape=(4, 12, 10)
bop_5922 = relay.bitwise_or(call_5900.astype('uint32'), relay.reshape(uop_5917.astype('uint32'), relay.shape_of(call_5900))) # shape=(4, 12, 10)
uop_5930 = relay.sigmoid(call_5899.astype('float64')) # shape=(4, 12, 10)
uop_5932 = relay.sigmoid(call_5900.astype('float64')) # shape=(4, 12, 10)
uop_5936 = relay.atan(call_5899.astype('float32')) # shape=(4, 12, 10)
uop_5938 = relay.atan(call_5900.astype('float32')) # shape=(4, 12, 10)
func_4688_call = mod.get_global_var('func_4688')
func_4689_call = mutated_mod.get_global_var('func_4689')
call_5940 = relay.TupleGetItem(func_4688_call(), 0)
call_5941 = relay.TupleGetItem(func_4689_call(), 0)
uop_5966 = relay.atanh(call_5899.astype('float64')) # shape=(4, 12, 10)
uop_5968 = relay.atanh(call_5900.astype('float64')) # shape=(4, 12, 10)
func_1636_call = mod.get_global_var('func_1636')
func_1638_call = mutated_mod.get_global_var('func_1638')
call_5969 = func_1636_call()
call_5970 = func_1636_call()
output = relay.Tuple([bop_5919,uop_5930,uop_5936,call_5940,uop_5966,call_5969,])
output2 = relay.Tuple([bop_5922,uop_5932,uop_5938,call_5941,uop_5968,call_5970,])
func_5972 = relay.Function([], output)
mod['func_5972'] = func_5972
mod = relay.transform.InferType()(mod)
mutated_mod['func_5972'] = func_5972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5972_call = mutated_mod.get_global_var('func_5972')
call_5973 = func_5972_call()
output = call_5973
func_5974 = relay.Function([], output)
mutated_mod['func_5974'] = func_5974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2923_call = mod.get_global_var('func_2923')
func_2925_call = mutated_mod.get_global_var('func_2925')
call_6003 = relay.TupleGetItem(func_2923_call(), 1)
call_6004 = relay.TupleGetItem(func_2925_call(), 1)
func_5972_call = mod.get_global_var('func_5972')
func_5974_call = mutated_mod.get_global_var('func_5974')
call_6007 = relay.TupleGetItem(func_5972_call(), 0)
call_6008 = relay.TupleGetItem(func_5974_call(), 0)
func_2406_call = mod.get_global_var('func_2406')
func_2408_call = mutated_mod.get_global_var('func_2408')
call_6017 = relay.TupleGetItem(func_2406_call(), 0)
call_6018 = relay.TupleGetItem(func_2408_call(), 0)
func_2320_call = mod.get_global_var('func_2320')
func_2324_call = mutated_mod.get_global_var('func_2324')
const_6051 = relay.const([-3,6,4,1,-1,4,6,2,-7,-3,6,3,-5,-10,-5,5,9,8,-5,7,-8,10,9,1,2,10,7,3,-4,3,9,-7,-9,10,-6,2,7,9,5,-2,7,6,-5,7,3,9,6,-10,1,-1,-6,10,-6,-9,-10,-7,-5,10,-1,9,7,-5,6,-7,5,3,-10,7,5,-6,-1,3,-3,5,-1,7,-4,10,8,-6,-7,6,-5,5,1,4,-2,5,1,-3,-6,-10,-3,-2,-8,-3,9,-2,2,-4,-7,-2,-7,-8,1,-3,-2,-9,3,-7,10,-6,9,5,5,6,-10,-3,-9,7,4,7,3,10,-7,-7,-7,6,-10,9,10,9,6,-7,5,-3,6,-5,-5,-4,-2,-9,-5,6,6,3,3,-8,-4,-1,10,9,5,-4,-9,-3,1,-1,-9,-4,-2,-2,8,1,-6,-4,8,2,-7,4,-7,6,-10,-6,4,5,8,-9,7,2,-4,-10,10,-8,10,-3,-10,7,-8,1,3,-7,3,-9,8,4,10,6], dtype = "int8")#candidate|6051|(198,)|const|int8
call_6050 = relay.TupleGetItem(func_2320_call(relay.reshape(const_6051.astype('int8'), [11, 6, 3]), relay.reshape(const_6051.astype('int8'), [11, 6, 3]), ), 3)
call_6052 = relay.TupleGetItem(func_2324_call(relay.reshape(const_6051.astype('int8'), [11, 6, 3]), relay.reshape(const_6051.astype('int8'), [11, 6, 3]), ), 3)
func_3577_call = mod.get_global_var('func_3577')
func_3580_call = mutated_mod.get_global_var('func_3580')
var_6064 = relay.var("var_6064", dtype = "uint16", shape = (1050,))#candidate|6064|(1050,)|var|uint16
call_6063 = relay.TupleGetItem(func_3577_call(relay.reshape(var_6064.astype('uint16'), [7, 10, 15])), 1)
call_6065 = relay.TupleGetItem(func_3580_call(relay.reshape(var_6064.astype('uint16'), [7, 10, 15])), 1)
output = relay.Tuple([call_6003,call_6007,call_6017,call_6050,const_6051,call_6063,var_6064,])
output2 = relay.Tuple([call_6004,call_6008,call_6018,call_6052,const_6051,call_6065,var_6064,])
func_6084 = relay.Function([var_6064,], output)
mod['func_6084'] = func_6084
mod = relay.transform.InferType()(mod)
mutated_mod['func_6084'] = func_6084
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6085 = relay.var("var_6085", dtype = "uint16", shape = (1050,))#candidate|6085|(1050,)|var|uint16
func_6084_call = mutated_mod.get_global_var('func_6084')
call_6086 = func_6084_call(var_6085)
output = call_6086
func_6087 = relay.Function([var_6085], output)
mutated_mod['func_6087'] = func_6087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5732_call = mod.get_global_var('func_5732')
func_5733_call = mutated_mod.get_global_var('func_5733')
call_6111 = relay.TupleGetItem(func_5732_call(), 0)
call_6112 = relay.TupleGetItem(func_5733_call(), 0)
uop_6113 = relay.asinh(call_6111.astype('float32')) # shape=(4, 12, 10)
uop_6115 = relay.asinh(call_6112.astype('float32')) # shape=(4, 12, 10)
bop_6126 = relay.logical_xor(call_6111.astype('int8'), relay.reshape(uop_6113.astype('int8'), relay.shape_of(call_6111))) # shape=(4, 12, 10)
bop_6129 = relay.logical_xor(call_6112.astype('int8'), relay.reshape(uop_6115.astype('int8'), relay.shape_of(call_6112))) # shape=(4, 12, 10)
output = bop_6126
output2 = bop_6129
func_6151 = relay.Function([], output)
mod['func_6151'] = func_6151
mod = relay.transform.InferType()(mod)
mutated_mod['func_6151'] = func_6151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6151_call = mutated_mod.get_global_var('func_6151')
call_6152 = func_6151_call()
output = call_6152
func_6153 = relay.Function([], output)
mutated_mod['func_6153'] = func_6153
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6151_call = mod.get_global_var('func_6151')
func_6153_call = mutated_mod.get_global_var('func_6153')
call_6154 = func_6151_call()
call_6155 = func_6151_call()
var_6157 = relay.var("var_6157", dtype = "int8", shape = (4, 12, 10))#candidate|6157|(4, 12, 10)|var|int8
bop_6158 = relay.power(call_6154.astype('float32'), relay.reshape(var_6157.astype('float32'), relay.shape_of(call_6154))) # shape=(4, 12, 10)
bop_6161 = relay.power(call_6155.astype('float32'), relay.reshape(var_6157.astype('float32'), relay.shape_of(call_6155))) # shape=(4, 12, 10)
func_4688_call = mod.get_global_var('func_4688')
func_4689_call = mutated_mod.get_global_var('func_4689')
call_6164 = relay.TupleGetItem(func_4688_call(), 1)
call_6165 = relay.TupleGetItem(func_4689_call(), 1)
output = relay.Tuple([bop_6158,call_6164,])
output2 = relay.Tuple([bop_6161,call_6165,])
func_6168 = relay.Function([var_6157,], output)
mod['func_6168'] = func_6168
mod = relay.transform.InferType()(mod)
var_6169 = relay.var("var_6169", dtype = "int8", shape = (4, 12, 10))#candidate|6169|(4, 12, 10)|var|int8
output = func_6168(var_6169)
func_6170 = relay.Function([var_6169], output)
mutated_mod['func_6170'] = func_6170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1879_call = mod.get_global_var('func_1879')
func_1881_call = mutated_mod.get_global_var('func_1881')
call_6172 = relay.TupleGetItem(func_1879_call(), 0)
call_6173 = relay.TupleGetItem(func_1881_call(), 0)
func_1277_call = mod.get_global_var('func_1277')
func_1279_call = mutated_mod.get_global_var('func_1279')
call_6176 = relay.TupleGetItem(func_1277_call(), 1)
call_6177 = relay.TupleGetItem(func_1279_call(), 1)
output = relay.Tuple([call_6172,call_6176,])
output2 = relay.Tuple([call_6173,call_6177,])
func_6193 = relay.Function([], output)
mod['func_6193'] = func_6193
mod = relay.transform.InferType()(mod)
output = func_6193()
func_6194 = relay.Function([], output)
mutated_mod['func_6194'] = func_6194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5732_call = mod.get_global_var('func_5732')
func_5733_call = mutated_mod.get_global_var('func_5733')
call_6201 = relay.TupleGetItem(func_5732_call(), 0)
call_6202 = relay.TupleGetItem(func_5733_call(), 0)
output = relay.Tuple([call_6201,])
output2 = relay.Tuple([call_6202,])
func_6216 = relay.Function([], output)
mod['func_6216'] = func_6216
mod = relay.transform.InferType()(mod)
output = func_6216()
func_6217 = relay.Function([], output)
mutated_mod['func_6217'] = func_6217
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6253 = relay.var("var_6253", dtype = "float64", shape = (7, 10, 4))#candidate|6253|(7, 10, 4)|var|float64
uop_6254 = relay.acos(var_6253.astype('float64')) # shape=(7, 10, 4)
output = relay.Tuple([uop_6254,])
output2 = relay.Tuple([uop_6254,])
func_6268 = relay.Function([var_6253,], output)
mod['func_6268'] = func_6268
mod = relay.transform.InferType()(mod)
var_6269 = relay.var("var_6269", dtype = "float64", shape = (7, 10, 4))#candidate|6269|(7, 10, 4)|var|float64
output = func_6268(var_6269)
func_6270 = relay.Function([var_6269], output)
mutated_mod['func_6270'] = func_6270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3453_call = mod.get_global_var('func_3453')
func_3455_call = mutated_mod.get_global_var('func_3455')
call_6521 = func_3453_call()
call_6522 = func_3453_call()
output = relay.Tuple([call_6521,])
output2 = relay.Tuple([call_6522,])
func_6565 = relay.Function([], output)
mod['func_6565'] = func_6565
mod = relay.transform.InferType()(mod)
output = func_6565()
func_6566 = relay.Function([], output)
mutated_mod['func_6566'] = func_6566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3906_call = mod.get_global_var('func_3906')
func_3908_call = mutated_mod.get_global_var('func_3908')
call_6601 = relay.TupleGetItem(func_3906_call(), 4)
call_6602 = relay.TupleGetItem(func_3908_call(), 4)
var_6673 = relay.var("var_6673", dtype = "float64", shape = (108,))#candidate|6673|(108,)|var|float64
bop_6674 = relay.not_equal(call_6601.astype('bool'), relay.reshape(var_6673.astype('bool'), relay.shape_of(call_6601))) # shape=(108,)
bop_6677 = relay.not_equal(call_6602.astype('bool'), relay.reshape(var_6673.astype('bool'), relay.shape_of(call_6602))) # shape=(108,)
output = relay.Tuple([bop_6674,])
output2 = relay.Tuple([bop_6677,])
func_6678 = relay.Function([var_6673,], output)
mod['func_6678'] = func_6678
mod = relay.transform.InferType()(mod)
var_6679 = relay.var("var_6679", dtype = "float64", shape = (108,))#candidate|6679|(108,)|var|float64
output = func_6678(var_6679)
func_6680 = relay.Function([var_6679], output)
mutated_mod['func_6680'] = func_6680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3877_call = mod.get_global_var('func_3877')
func_3879_call = mutated_mod.get_global_var('func_3879')
call_6759 = func_3877_call()
call_6760 = func_3877_call()
func_2446_call = mod.get_global_var('func_2446')
func_2447_call = mutated_mod.get_global_var('func_2447')
call_6767 = func_2446_call()
call_6768 = func_2446_call()
output = relay.Tuple([call_6759,call_6767,])
output2 = relay.Tuple([call_6760,call_6768,])
func_6789 = relay.Function([], output)
mod['func_6789'] = func_6789
mod = relay.transform.InferType()(mod)
output = func_6789()
func_6790 = relay.Function([], output)
mutated_mod['func_6790'] = func_6790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2948_call = mod.get_global_var('func_2948')
func_2950_call = mutated_mod.get_global_var('func_2950')
call_6853 = relay.TupleGetItem(func_2948_call(), 0)
call_6854 = relay.TupleGetItem(func_2950_call(), 0)
output = call_6853
output2 = call_6854
func_6871 = relay.Function([], output)
mod['func_6871'] = func_6871
mod = relay.transform.InferType()(mod)
output = func_6871()
func_6872 = relay.Function([], output)
mutated_mod['func_6872'] = func_6872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6151_call = mod.get_global_var('func_6151')
func_6153_call = mutated_mod.get_global_var('func_6153')
call_6916 = func_6151_call()
call_6917 = func_6151_call()
func_2675_call = mod.get_global_var('func_2675')
func_2677_call = mutated_mod.get_global_var('func_2677')
var_6921 = relay.var("var_6921", dtype = "bool", shape = (260,))#candidate|6921|(260,)|var|bool
call_6920 = relay.TupleGetItem(func_2675_call(relay.reshape(var_6921.astype('bool'), [2, 10, 13])), 0)
call_6922 = relay.TupleGetItem(func_2677_call(relay.reshape(var_6921.astype('bool'), [2, 10, 13])), 0)
output = relay.Tuple([call_6916,call_6920,var_6921,])
output2 = relay.Tuple([call_6917,call_6922,var_6921,])
func_6923 = relay.Function([var_6921,], output)
mod['func_6923'] = func_6923
mod = relay.transform.InferType()(mod)
var_6924 = relay.var("var_6924", dtype = "bool", shape = (260,))#candidate|6924|(260,)|var|bool
output = func_6923(var_6924)
func_6925 = relay.Function([var_6924], output)
mutated_mod['func_6925'] = func_6925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2366_call = mod.get_global_var('func_2366')
func_2367_call = mutated_mod.get_global_var('func_2367')
call_6940 = relay.TupleGetItem(func_2366_call(), 0)
call_6941 = relay.TupleGetItem(func_2367_call(), 0)
func_1852_call = mod.get_global_var('func_1852')
func_1856_call = mutated_mod.get_global_var('func_1856')
const_6949 = relay.const([True,True,True,False,True,True,False,False,True,False,False,False,False,True,False,True,True,True,True,False,False,True,False,False,True,False,True,True,True,True,True,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,False,True,True,False,False,True,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,False,False,False,True,True,True,False,False,True,True,False,True,False,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,False,False,False,False,True,False,True,False,True,True,False,False,True,False,True,True,True,True,True,False,True,True,True,True,False,False,False,False,True,True,True,True,True,True,False,False,True,True,False,False,True,False,True,False,True,False,True,False,True,True,False,True,False,True,False,True,True,False,True,False,True,False,True,True,False,True,True,True,True,False,False,False,False,True,False,True,True,True,True,True,False,True,False,True,False,False,False,True,False,True,True,False,True,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,True,False,False,True,True,False,False,False,False,False,True,True,True,True,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,False,False,False,False,False,True,False,True,False,False,True,False,True,False,False,False,True,True,False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,True,False,False,True,False,True,True,False,True,True,True,True,True,False,True,False,False,False,False,True,False,True,False,True,False,True,False,False,False,False,False,False,False,True,True,False,False,False,False,True,True,True,True,True,True,False,True,False,False,True,True,True,False,False,False,True,True,True,True,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False,True,False,False,False,False,False,False,True,True,False,True,False,True,False,True,True,False,False,True,True,True,False,False,False,True,False,True,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,True,False,True,True,False,True,False,True,True,False,False,True,True,False,True,True,True,True,False,False,False,True,False,False,False,False,False,False,True,False,True,False,False,True,True,False,False,False,True,True,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,False,False,False,True,True,False,False,True,False,True,True,True,True,True,False,False,True,False,False,False,False,False,False,True,True,True,False,False,False,False,False,False,False,True,True,True,True,False,False,False,True,True,True,True,False,True,True,True,True,False,True,True,False,False,False,True,True,True,True,True,True,False,False,True,True,True], dtype = "bool")#candidate|6949|(528,)|const|bool
call_6948 = relay.TupleGetItem(func_1852_call(relay.reshape(const_6949.astype('bool'), [6, 11, 8]), relay.reshape(call_6940.astype('bool'), []), ), 3)
call_6950 = relay.TupleGetItem(func_1856_call(relay.reshape(const_6949.astype('bool'), [6, 11, 8]), relay.reshape(call_6940.astype('bool'), []), ), 3)
func_3453_call = mod.get_global_var('func_3453')
func_3455_call = mutated_mod.get_global_var('func_3455')
call_6960 = func_3453_call()
call_6961 = func_3453_call()
func_1852_call = mod.get_global_var('func_1852')
func_1856_call = mutated_mod.get_global_var('func_1856')
call_6999 = relay.TupleGetItem(func_1852_call(relay.reshape(const_6949.astype('bool'), [6, 11, 8]), relay.reshape(call_6940.astype('bool'), []), ), 0)
call_7000 = relay.TupleGetItem(func_1856_call(relay.reshape(const_6949.astype('bool'), [6, 11, 8]), relay.reshape(call_6940.astype('bool'), []), ), 0)
output = relay.Tuple([call_6940,call_6948,const_6949,call_6960,call_6999,])
output2 = relay.Tuple([call_6941,call_6950,const_6949,call_6961,call_7000,])
func_7006 = relay.Function([], output)
mod['func_7006'] = func_7006
mod = relay.transform.InferType()(mod)
mutated_mod['func_7006'] = func_7006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7006_call = mutated_mod.get_global_var('func_7006')
call_7007 = func_7006_call()
output = call_7007
func_7008 = relay.Function([], output)
mutated_mod['func_7008'] = func_7008
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7009 = relay.var("var_7009", dtype = "float64", shape = (12, 3, 15))#candidate|7009|(12, 3, 15)|var|float64
uop_7010 = relay.log(var_7009.astype('float64')) # shape=(12, 3, 15)
func_5042_call = mod.get_global_var('func_5042')
func_5043_call = mutated_mod.get_global_var('func_5043')
call_7016 = relay.TupleGetItem(func_5042_call(), 1)
call_7017 = relay.TupleGetItem(func_5043_call(), 1)
bop_7018 = relay.logical_xor(uop_7010.astype('int16'), call_7016.astype('int16')) # shape=(12, 3, 15)
bop_7021 = relay.logical_xor(uop_7010.astype('int16'), call_7017.astype('int16')) # shape=(12, 3, 15)
bop_7022 = relay.bitwise_xor(uop_7010.astype('int32'), relay.reshape(bop_7018.astype('int32'), relay.shape_of(uop_7010))) # shape=(12, 3, 15)
bop_7025 = relay.bitwise_xor(uop_7010.astype('int32'), relay.reshape(bop_7021.astype('int32'), relay.shape_of(uop_7010))) # shape=(12, 3, 15)
func_1277_call = mod.get_global_var('func_1277')
func_1279_call = mutated_mod.get_global_var('func_1279')
call_7026 = relay.TupleGetItem(func_1277_call(), 0)
call_7027 = relay.TupleGetItem(func_1279_call(), 0)
uop_7029 = relay.sigmoid(uop_7010.astype('float64')) # shape=(12, 3, 15)
output = relay.Tuple([bop_7022,call_7026,uop_7029,])
output2 = relay.Tuple([bop_7025,call_7027,uop_7029,])
func_7046 = relay.Function([var_7009,], output)
mod['func_7046'] = func_7046
mod = relay.transform.InferType()(mod)
var_7047 = relay.var("var_7047", dtype = "float64", shape = (12, 3, 15))#candidate|7047|(12, 3, 15)|var|float64
output = func_7046(var_7047)
func_7048 = relay.Function([var_7047], output)
mutated_mod['func_7048'] = func_7048
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7056 = relay.const([[[2,10,1,-1,3,-2,5,-1,-1,3,3,10],[6,-5,-10,8,1,5,9,1,-4,-9,6,-4]]], dtype = "uint16")#candidate|7056|(1, 2, 12)|const|uint16
var_7057 = relay.var("var_7057", dtype = "uint16", shape = (12, 2, 12))#candidate|7057|(12, 2, 12)|var|uint16
bop_7058 = relay.bitwise_xor(const_7056.astype('uint16'), var_7057.astype('uint16')) # shape=(12, 2, 12)
output = bop_7058
output2 = bop_7058
func_7063 = relay.Function([var_7057,], output)
mod['func_7063'] = func_7063
mod = relay.transform.InferType()(mod)
var_7064 = relay.var("var_7064", dtype = "uint16", shape = (12, 2, 12))#candidate|7064|(12, 2, 12)|var|uint16
output = func_7063(var_7064)
func_7065 = relay.Function([var_7064], output)
mutated_mod['func_7065'] = func_7065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5412_call = mod.get_global_var('func_5412')
func_5413_call = mutated_mod.get_global_var('func_5413')
call_7077 = func_5412_call()
call_7078 = func_5412_call()
func_6084_call = mod.get_global_var('func_6084')
func_6087_call = mutated_mod.get_global_var('func_6087')
const_7084 = relay.const([4,-6,4,6,-5,2,-9,7,9,-4,4,7,-1,3,2,-7,3,3,9,9,-2,-4,-10,-2,10,9,6,-5,7,-3,2,-7,-5,-2,10,10,10,2,-8,8,-4,10,-7,7,3,-2,9,-9,10,1,-1,-3,-9,-3,-1,3,-2,-5,9,10,3,-8,1,-9,7,2,-2,-2,-2,-8,-10,10,5,8,9,-8,9,-7,3,1,7,-9,10,10,6,5,-10,-7,-2,10,4,4,-6,-4,-8,-9,10,-5,-9,2,-4,3,-4,8,-5,5,-8,3,-1,-3,3,5,-7,-6,7,4,-7,-5,5,-6,2,8,-2,6,-9,4,10,-7,-2,-5,-3,10,4,-10,9,-9,-7,2,9,5,-8,10,-10,7,2,-3,-1,-4,8,-5,-9,-9,3,-8,-3,10,3,9,7,-7,10,-3,-3,-7,10,-2,-8,9,-4,4,1,-9,2,-8,-6,7,5,8,-6,10,8,-8,3,-10,6,4,-7,-2,3,-9,6,-4,7,-10,-8,10,-4,-6,8,6,9,-1,-5,9,-4,-6,8,3,3,-8,-4,8,-9,-5,-10,10,2,-8,-4,-2,7,1,7,1,-7,-10,-9,9,5,-4,-4,6,4,1,-3,8,-3,7,3,2,7,1,2,-4,1,-2,2,10,-2,-6,6,-4,5,10,9,7,4,2,5,1,-5,2,-8,5,-5,-4,-7,1,2,-9,3,-5,-4,-3,2,-9,-6,4,5,-6,10,-3,-10,8,-8,-3,3,-8,-6,9,4,6,-9,5,-10,6,3,-7,-6,7,4,-6,7,-5,6,10,4,-1,-6,8,-9,6,-6,7,9,-7,-3,9,1,-10,2,9,5,8,10,7,-10,3,9,-9,3,3,-1,5,-8,10,-8,3,-1,-7,9,-10,1,7,3,-8,2,-4,4,6,8,-2,-3,10,-8,-4,-2,-5,6,-1,-8,9,10,2,5,-8,1,9,-6,9,5,10,8,10,-7,-4,10,4,7,6,5,-4,3,-2,2,3,-7,-7,-8,8,8,2,-5,9,-6,5,6,-8,5,-8,-5,8,-3,6,2,1,-8,-7,1,7,1,-9,-5,8,10,9,-6,-7,2,2,-9,-1,8,-10,-3,8,-2,1,-5,7,4,3,3,-10,-3,-6,-7,-9,-4,-6,7,1,3,7,2,5,2,-5,-8,-9,-9,-3,-3,-1,-3,-5,5,2,-9,-7,-4,4,-2,10,-6,-3,3,9,-8,2,1,2,5,-3,-2,3,3,-2,8,7,3,7,5,2,8,7,-3,-5,-2,3,7,1,-3,8,-7,3,2,5,-8,3,5,7,-8,8,-9,5,5,7,-9,7,-10,5,2,9,9,8,-9,-1,5,6,-8,-9,7,1,1,-1,2,-2,5,6,3,-7,-7,1,8,6,-8,-3,3,10,-5,6,6,2,9,-5,-10,-7,3,-8,5,10,-9,8,-6,5,-9,9,-8,7,8,2,-6,-8,-10,3,2,-1,-6,-4,-9,-6,-1,4,-7,-9,-4,-5,-3,-1,-1,8,-8,6,-8,-8,9,-5,-8,-10,-9,10,-9,4,-9,-4,-9,-4,9,-1,-10,6,-3,-10,10,-6,8,-10,2,-10,7,1,-6,3,7,-4,2,-6,1,-8,7,-7,9,-3,-1,1,-9,-4,-1,10,-2,5,-4,-3,-7,3,-4,-9,10,-3,9,7,-8,2,-1,-7,9,-8,-3,6,-1,-3,1,-5,6,-10,-4,2,1,3,-8,-4,2,-8,5,6,4,9,1,-8,4,9,-8,-1,-5,-10,5,-8,10,-4,1,-10,-9,-4,-5,-5,-2,-8,-7,1,1,5,-7,-5,-10,-1,8,7,10,-8,-4,3,-9,-8,8,-10,-1,9,9,-7,2,9,-7,9,-8,2,10,-7,6,7,5,5,2,5,7,-8,10,-10,4,4,-6,3,4,7,9,4,-1,1,-2,-5,-8,9,-4,5,-2,-1,7,-6,-8,-9,-9,1,3,-5,6,-5,7,-2,-6,-1,6,-7,-6,4,-8,-10,-7,8,1,-4,-7,3,6,5,10,10,-7,-9,-2,8,-5,8,9,3,-9,-9,7,-10,-7,4,-2,3,3,-4,-6,-6,1,4,-10,-10,-3,7,10,2,-4,-7,1,8,4,1,-4,-3,-1,-3,-4,-9,-1,-7,-4,10,-5,6,7,-2,-8,2,-1,7,10,4,4,-10,-10,7,8,-5,4,-1,-7,-3,9,9,8,2,7,-1,9,-7,10,6,1,1,5,6,6,-9,5,-4,3,1,4,-2,-7,4,10,5,3,7,-9,-8,-4,-9,4,-2,-1,-8,6,8,6,1,3,-9,4,-2,3,-10,-8,4,4,10,8,10,7,-9,9,-1,8,9,-10,-6,1,-7,-7,-3,-8,8,-1,2,-6,1,1,-10,-5,-2,9,7,-6,-1,5,3,6,-9,-10,7,2,-3,-3,3,-9,-3,2,10,-4,10,4,-5,5,-1,5,-10,5,1,4,6,-8,4,8,-8,7,-2,-1,5,-10,-10,-2,3,4,7,-7,-5,-3,5,-5,4,10,2,2,9,4,7,10,7,-6,-5,-9,-8,-9,4,7,-5,1,-10,7,-4,-9,-6,3,-6,-8,-3,-9,-9,-5,2,10,-1,-7,3,2,-2,10,-3,-1,-1,-10,-8,-5,-7,10,2,-9,1,6,7,-3,3,8,6,5,-10,4,-3,-5,-1,2,-2,-10,4,-9,6,-1,-5,4,-8,-3,-5,-8,-7,-1,-9,6,1,-6,-2,7,5,8,4,-3,5], dtype = "uint16")#candidate|7084|(1050,)|const|uint16
call_7083 = relay.TupleGetItem(func_6084_call(relay.reshape(const_7084.astype('uint16'), [1050,])), 0)
call_7085 = relay.TupleGetItem(func_6087_call(relay.reshape(const_7084.astype('uint16'), [1050,])), 0)
func_1805_call = mod.get_global_var('func_1805')
func_1807_call = mutated_mod.get_global_var('func_1807')
call_7087 = func_1805_call()
call_7088 = func_1805_call()
output = relay.Tuple([call_7077,call_7083,const_7084,call_7087,])
output2 = relay.Tuple([call_7078,call_7085,const_7084,call_7088,])
func_7097 = relay.Function([], output)
mod['func_7097'] = func_7097
mod = relay.transform.InferType()(mod)
mutated_mod['func_7097'] = func_7097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7097_call = mutated_mod.get_global_var('func_7097')
call_7098 = func_7097_call()
output = call_7098
func_7099 = relay.Function([], output)
mutated_mod['func_7099'] = func_7099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3877_call = mod.get_global_var('func_3877')
func_3879_call = mutated_mod.get_global_var('func_3879')
call_7116 = func_3877_call()
call_7117 = func_3877_call()
func_4041_call = mod.get_global_var('func_4041')
func_4044_call = mutated_mod.get_global_var('func_4044')
const_7120 = relay.const([[True,False],[True,True],[False,True],[False,False]], dtype = "bool")#candidate|7120|(4, 2)|const|bool
var_7121 = relay.var("var_7121", dtype = "float64", shape = (1176,))#candidate|7121|(1176,)|var|float64
call_7119 = relay.TupleGetItem(func_4041_call(relay.reshape(const_7120.astype('bool'), [1, 8]), relay.reshape(var_7121.astype('float64'), [1176,]), ), 5)
call_7122 = relay.TupleGetItem(func_4044_call(relay.reshape(const_7120.astype('bool'), [1, 8]), relay.reshape(var_7121.astype('float64'), [1176,]), ), 5)
func_4222_call = mod.get_global_var('func_4222')
func_4224_call = mutated_mod.get_global_var('func_4224')
call_7138 = relay.TupleGetItem(func_4222_call(relay.reshape(var_7121.astype('float64'), [1176,])), 0)
call_7139 = relay.TupleGetItem(func_4224_call(relay.reshape(var_7121.astype('float64'), [1176,])), 0)
output = relay.Tuple([call_7116,call_7119,const_7120,var_7121,call_7138,])
output2 = relay.Tuple([call_7117,call_7122,const_7120,var_7121,call_7139,])
func_7144 = relay.Function([var_7121,], output)
mod['func_7144'] = func_7144
mod = relay.transform.InferType()(mod)
mutated_mod['func_7144'] = func_7144
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7145 = relay.var("var_7145", dtype = "float64", shape = (1176,))#candidate|7145|(1176,)|var|float64
func_7144_call = mutated_mod.get_global_var('func_7144')
call_7146 = func_7144_call(var_7145)
output = call_7146
func_7147 = relay.Function([var_7145], output)
mutated_mod['func_7147'] = func_7147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5231_call = mod.get_global_var('func_5231')
func_5232_call = mutated_mod.get_global_var('func_5232')
call_7165 = relay.TupleGetItem(func_5231_call(), 1)
call_7166 = relay.TupleGetItem(func_5232_call(), 1)
output = call_7165
output2 = call_7166
func_7189 = relay.Function([], output)
mod['func_7189'] = func_7189
mod = relay.transform.InferType()(mod)
output = func_7189()
func_7190 = relay.Function([], output)
mutated_mod['func_7190'] = func_7190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3625_call = mod.get_global_var('func_3625')
func_3627_call = mutated_mod.get_global_var('func_3627')
call_7218 = relay.TupleGetItem(func_3625_call(), 0)
call_7219 = relay.TupleGetItem(func_3627_call(), 0)
func_5889_call = mod.get_global_var('func_5889')
func_5892_call = mutated_mod.get_global_var('func_5892')
var_7228 = relay.var("var_7228", dtype = "float64", shape = (1176,))#candidate|7228|(1176,)|var|float64
call_7227 = relay.TupleGetItem(func_5889_call(relay.reshape(var_7228.astype('float64'), [2, 588])), 0)
call_7229 = relay.TupleGetItem(func_5892_call(relay.reshape(var_7228.astype('float64'), [2, 588])), 0)
uop_7252 = relay.atan(var_7228.astype('float32')) # shape=(1176,)
const_7256 = relay.const([5.872135,-4.447865,-0.389611,-1.861214,3.144272,9.436139,3.058398,4.596694,-5.849737,5.550717,3.933725,3.725049,-3.507888,-7.148449,-0.011858,8.070104,8.107816,-0.975667,9.125915,6.265500,-6.616158,7.458851,8.598399,4.438018,7.755547,-0.669577,-7.958419,-0.287901,-8.809541,-2.492204,-8.134011,1.056855,0.380484,9.153901,-7.076146,6.301519,6.223550,2.282927,4.635541,-3.424684,0.830942,4.661826,-0.430573,-1.025658,-3.850086,5.214408,-9.004506,-2.518536,1.374017,8.337866,-9.156396,-8.741773,9.430245,-4.197827,7.462182,8.228631,-6.508127,-1.098021,-3.601248,3.629205,4.931226,5.300628,0.551496,4.192970,2.033055,5.971018,-2.833237,7.140877,2.485920,-2.446577,-1.628129,2.065292,2.435278,1.053286,-8.281691,-8.809790,-3.669688,-9.306412,-3.391303,-0.492975,-1.795165,9.942383,5.467583,-5.357579,6.073624,0.779879,-3.217880,-7.749577,-7.964706,0.134167,-5.844711,-0.260217,6.669814,4.245570,1.519631,1.176145,1.799783,-0.721137,0.720351,2.417254,7.926388,-2.878108,7.517651,0.080237,-7.060236,-4.785042,5.578903,2.965690,9.709083,-8.516245,-0.363005,-4.377510,-9.718466,8.521179,6.324710,-4.960339,2.304567,-2.350701,4.565238,6.854192,-6.075124,9.327124,-6.296248,-5.833690,7.845445,-2.997426,-6.746232,9.566759,0.318296,-1.505338,0.400740,-6.743849,3.217106,3.429511,-9.733137,4.905159,-7.229560,-9.056776,4.835904,8.291674,3.496629,3.949448,-9.121304,0.385656,2.876792,0.645749,-2.932468,4.330577,-1.893596,4.289693,2.556685,-6.275360,7.954711,2.184537,0.892967,9.499991,-0.488328,7.842012,6.195009,4.049630,-3.231534,2.983629,-6.569827,7.654397,5.385736,7.416505,7.528854,-5.899556,5.471264,6.712454,-3.673262,0.421795,9.355350,-4.752906,5.957567,6.958148,-0.604498,7.234831,-9.254895,4.062483,2.549655,-5.481452,-4.166617,9.101086,-3.010556,4.446303,0.722130,-1.166459,5.989671,5.681406,-9.678879,-7.233260,8.609729,2.934492,-2.826770,5.382582,4.330930,-3.849665,-9.278266,4.980811,7.698230,-6.683333,-5.565389,7.727033,7.123331,-3.329523,-9.506284,-9.017696,-2.727749,5.653473,-0.947722,-6.743980,-8.762272,-0.502133,-6.677981,-4.551170,-2.824570,-7.472826,2.938354,-8.031152,-6.586398,-2.109542,7.642750,-0.032231,-1.020568,8.128511,-8.152211,-7.784087,-1.688907,-2.416514,2.433536,-8.061645,2.101614,-4.882033,4.908964,2.529607,3.566971,-4.807430,-9.958007,4.487934,-2.384130,4.311698,-6.113436,4.076835,-6.316732,-3.790336,-3.507254,0.973064,8.483606,-5.511155,-9.965566,6.226977,4.256566,7.733070,-5.904056,-6.412541,3.711351,-1.389152,-1.427678,-8.752360,3.275043,-9.243105,-2.256842,6.373536,7.616846,-7.617385,8.521406,2.557924,4.814099,-9.732478,4.898795,-1.580156,-2.349118,9.061431,-3.286436,-6.870790,-8.510772,-9.488231,-4.492790,-6.022146,6.916888,-3.242812,-7.598963,-8.100128,-0.167779,-8.686346,0.506940,-0.642559,0.503605,-3.385264,9.147215,5.083023,3.774245,-6.213265,2.457260,3.134364,3.696170,5.447294,-2.057003,9.631327,-4.736018,-2.443865,-8.191989,6.211903,-5.003129,-6.995218,-3.772217,4.934830,6.220248,-2.600794,5.950131,2.344929,0.313538,-2.603398,-8.621890,-4.443941,0.211082,1.639219,1.606593,2.591547,-0.849679,5.498426,2.526703,9.765435,8.027225,3.250757,5.837030,6.351349,4.961232,-6.686253,-6.911678,-1.717053,-2.652729,5.433829,4.734438,7.035142,-7.742357,-5.694329,-2.901999,-4.939825,5.758577,-8.585128,4.963059,9.543955,2.996724,-8.159001,-5.805484,-2.837309,-5.525744,-6.032935,-0.241120,-8.010628,5.683876,4.417512,-2.163834,9.411379,7.748229,-2.731551,5.631785,-0.906913,-7.302717,-5.707893,8.832758,6.990948,5.995467,3.658601,5.818498,-9.551467,4.041501,-6.354114,-8.145682,7.002663,0.876558,-9.753382,-9.041824,-0.282088,4.519712,5.065741,5.218734,0.631425,0.275225,-1.592762,-8.908536,7.101381,-3.304815,5.437200,4.385154,7.785720,-4.381699,4.164772,-8.040696,6.048055,3.797260,-5.037889,6.804962,2.691285,7.115877,-5.051338,-3.827956,4.271535,1.431214,1.306423,9.246006,-2.877743,-0.319212,-2.951033,4.227967,9.491437,7.974721,1.572306,1.231966,3.058512,-3.258633,-7.847982,3.117777,-8.049167,-0.049409,6.244286,-8.985065,0.953811,3.686281,5.929572,-0.314171,1.779157,-0.953927,-9.804706,8.907596,-7.926964,1.982903,6.899875,-6.093971,-7.390795,3.655878,6.399952,1.057555,3.643716,-5.619352,2.253956,8.528265,-2.828711,3.996435,9.614698,-1.856140,-7.725234,-4.789906,-5.415260,5.369819,2.312289,-1.242000,-3.724063,6.154836,5.308095,-0.114022,-3.207432,4.013139,-2.955139,-4.392238,-0.682270,7.012561,-2.498482,-8.180558,0.921749,5.442570,-2.563020,8.322819,5.492660,-4.888596,-3.950685,2.997262,-1.847401,-8.165124,4.742421,-5.323933,6.478413,5.960369,7.585910,8.466712,8.784371,9.560693,-2.093305,2.611672,-3.466703,-9.631447,-8.571462,5.332444,7.212533,2.369719,-4.547465,-2.584442,-1.654814,-7.118119,8.972457,-6.637820,-3.970129,-5.521439,-3.979455,1.495194,-9.683896,9.207022,7.933540,6.927788,-0.725269,-4.124805,0.747722,7.228192,-9.439324,0.084773,8.890446,-4.939937,-7.788842,-9.656746,-2.617888,7.902807,-1.063119,-5.384112,9.391455,-8.979584,-7.227466,6.208211,5.398036,0.077582,-3.001686,3.841860,-2.400188,5.399370,-0.189255,6.192373,0.911366,6.187493,-1.488247,-8.737409,-5.723226,3.436860,9.053703,-1.284796,1.534822,-8.545890,-3.707902,2.649996,2.605530,0.023483,7.602117,9.471067,4.786617,-4.996059,-2.652085,-9.352080,3.613779,2.103859,-4.021997,9.980372,-0.663548,1.101237,7.028023,7.400319,8.509813,-6.199681,-3.846793,-1.803107,4.159053,7.765242,5.529993,-2.733960,9.259495,9.977584,6.650964,-9.779522,-3.585620,-0.357718,-8.946046,-3.633449,1.528355,-9.434541,-9.419173,4.087394,2.563338,1.958360,-4.942890,7.403166,-1.376917,2.701064,3.772667,8.935904,5.926623,6.912670,7.235149,-0.654966,7.332772,-1.597117,8.666569,8.503714,-8.087400,7.098681,-6.537853,4.876425,3.252863,-3.018413,-3.558708,-3.756927,9.241508,1.798710,6.763080,5.353455,1.257359,9.083054,-9.466341,1.110634,5.368955,4.875742,-6.924576,-3.486187,-1.049283,-8.355115,-6.969484,-1.333050,6.651946,6.768300,3.999756,1.116021,-5.551081,1.522434,2.006441,-1.796127,4.943026,-0.437194,-4.150043,1.756069,0.960480,0.158609,-1.230144,1.989960,9.948258,9.434974,-2.560345,3.427311,1.978307,9.047553,-6.795123,7.531861,9.012910,1.610256,0.222874,-5.391845,-2.528763,-6.790889,-6.302703,-2.966897,-3.072310,-0.476194,-5.848808,-4.847979,9.828776,-8.304899,2.098354,6.087703,3.997173,-7.819960,-1.219271,7.740273,-3.742465,9.296067,-0.720477,-5.869498,9.641800,3.442234,2.060879,7.709159,2.947505,-6.537567,-8.657755,3.505174,-0.918066,-6.892082,1.514220,7.522747,8.963011,-7.759431,2.273945,2.304744,7.191184,-4.958430,-3.808086,3.536615,-1.205348,-3.288525,-8.269509,-5.417658,6.454545,4.275632,3.064099,-6.086591,2.251338,-5.408648,3.000830,-5.244189,-0.500117,5.543578,-2.107451,-9.907784,-1.187257,5.103643,-3.033393,4.223010,-2.802226,-8.905286,-4.126910,3.075343,9.247623,-8.795990,9.251650,-8.807843,8.036559,-4.865407,-3.150538,-5.165548,5.291644,7.958296,-2.073879,8.715544,0.058726,-1.343855,-8.046600,-7.081173,6.537796,-9.764975,7.173116,-1.673589,4.661008,-5.948895,0.147539,-5.621827,0.308021,-8.369980,1.398279,-6.478441,-3.236697,-6.218920,-5.540661,-9.639195,4.697204,-9.402253,3.730466,9.703115,1.706561,2.814476,5.774250,9.108321,3.698703,-7.200705,4.122359,-6.214243,4.512657,-2.576761,1.480453,4.817389,-2.697424,0.898154,-6.445473,-4.713693,-7.755245,-5.169778,6.490486,-7.042127,4.137026,7.364133,-9.295030,-9.657245,-5.360996,2.945969,-9.547020,-8.412033,0.469089,-6.202923,3.822634,2.063728,-8.627562,1.895199,-8.222861,8.296247,-8.629440,-4.553810,-3.019774,-8.998753,-1.157436,-6.646736,-8.109963,1.997583,-6.882139,3.630656,-1.728019,4.103559,-8.092119,-8.213521,8.040690,-9.872739,1.467513,-7.214649,-8.403800,-2.315437,-4.242995,3.484308,-9.885853,-2.648167,-7.427673,-5.469775,5.398644,-7.634143,-3.668348,-7.837002,-2.135481,2.903740,8.837795,7.636494,-7.946354,-2.383928,-3.589807,1.449915,-2.232491,9.686944,5.225197,3.791898,8.462828,-1.698201,1.464245,4.730280,2.027465,2.601564,-9.532238,-0.039774,-6.726609,-5.760730,-9.286684,8.236642,2.463361,-4.400518,-5.896987,8.322196,1.271537,8.351164,-8.612366,-2.929010,4.977855,8.287096,-4.602653,-1.881558,-5.331782,3.127544,-2.238978,-5.731954,1.948820,-6.312875,-3.137964,9.960499,5.540387,-8.456152,-5.179086,-5.671195,-9.558061,7.667736,4.686298,-7.911005,-5.740373,1.988067,-2.989379,2.825771,-7.591511,-4.210210,0.428864,-6.727437,-8.200223,8.495002,7.323399,1.094254,6.327331,-7.903898,-1.333813,-9.814701,-4.033855,-3.928507,4.822218,-2.811390,8.046430,1.846628,-3.861251,-4.391267,-9.574795,4.259227,6.534880,-5.099246,-9.797438,4.597236,6.566350,7.397120,3.138770,-6.599561,8.132580,-1.813090,7.267696,-0.959799,3.682801,0.727034,-8.607510,4.283752,1.250345,-5.023515,-0.295461,-2.765484,0.980845,3.381963,5.928322,-9.548045,-5.470707,-4.015078,-3.023449,-2.050525,0.342098,2.430623,-0.209642,7.799589,-9.024982,3.577388,8.482762,-1.768128,-3.515918,-0.188919,-5.309070,-2.669922,3.433436,-6.858689,5.855429,-8.999709,-6.564326,-5.796521,-2.065115,-5.393450,9.953050,-3.255435,-4.949284,-9.567850,-4.099043,-4.129411,3.392228,-5.121040,7.996972,-6.211700,8.740898,3.345970,-3.705568,-5.638354,0.372064,-2.680025,2.460024,-3.499156,3.566016,-8.426101,1.906403,-9.010324,3.625366,2.538319,-0.243050,-3.468014,-8.084072,6.799144,5.103798,-9.032974,5.621738,-5.227639,2.736979,-9.631611,7.086095,-0.834130,9.335972,3.772571,3.263263,-3.547176,-2.419750,9.200225,-8.685706,3.711580,0.542499,7.481051,-6.357631,3.779138,-7.818029,2.137207,-2.994835,-0.819921,-9.589983,-5.360955,-0.136826,3.898185,4.211472,-7.935603,-1.436585,-1.149200,6.159971,-1.507311,9.346789,4.414461,8.975710,7.429118,-0.191141,4.938619,5.133950,4.848868,-7.704953,-0.711517,7.369368,-1.910296,-7.121912,6.802052,-1.819437,-5.080392,9.246444,3.740770,-5.677488,-0.258515,-6.910083,0.698482,-8.580178,1.955748,-6.683945,-6.088087,-4.152188,8.645050,0.037193,-6.448619,-4.532942,3.970465,-7.666063,-7.782612,2.615020,-6.015554,-8.332783,7.146085,-4.663488,-8.454861,-9.967188,-8.321636,7.891432,-8.976668,4.034937,-2.027052,6.210854,0.046221,-9.574882,-2.553058,1.644345,1.829175,-1.305777,-8.468839,8.680965,7.094325,5.905463,9.742999,2.163391,-4.820915,-0.198790,-0.206254,-8.942364,-1.531120,9.555961,3.612455,4.730133,5.513758,1.689944,-6.334478,-7.138743,0.809264,6.705583,-1.068888,-1.521343,8.316478,2.303610,-7.357464,-5.329543,-8.911579,5.128444,-6.666765,-2.959907,-1.404951,3.225094,-6.526687,9.094139,5.254959,-2.532954,1.261597,-5.558444,-8.903371,0.155711,-1.321864,4.375669,8.538925,-4.721973,1.052785,3.738739,-0.237372,-1.539069,-1.818714,-0.883993,-6.500113,4.762657,6.316836,6.601541,8.115629,-2.492229,-2.041332,-3.965760,-7.377633,8.342706,9.375042,-5.681188,8.630350,9.236234,-8.785148,0.773764,-0.357244,-0.011312,3.176611,4.410027,-0.367483,-7.103153,6.827205,0.796682,8.377494,4.702100,0.665830,-7.172063,-5.669318,5.284743,-2.143601,-6.893232,9.275500,-3.690030,-0.772096,-9.927120,-5.676733,4.694136,3.833830,0.309580,4.939736,-3.878666,-1.921035,5.154737,-7.145644,1.773002,8.698521,9.584202,6.553316,5.540054,-0.827583,-5.870799,-9.661709,-1.714884,-3.934147,-1.139107,0.701138,0.845941,-1.593440,-6.391434,6.932554,3.531722,6.776117,3.360261,-9.508633,-5.902849,-9.321742,5.131440,-0.436674,6.514870,-2.127868,-8.496301,-4.752033,4.917661,-4.062632,6.734859], dtype = "float32")#candidate|7256|(1176,)|const|float32
bop_7257 = relay.floor_mod(uop_7252.astype('float64'), relay.reshape(const_7256.astype('float64'), relay.shape_of(uop_7252))) # shape=(1176,)
output = relay.Tuple([call_7218,call_7227,bop_7257,])
output2 = relay.Tuple([call_7219,call_7229,bop_7257,])
func_7280 = relay.Function([var_7228,], output)
mod['func_7280'] = func_7280
mod = relay.transform.InferType()(mod)
var_7281 = relay.var("var_7281", dtype = "float64", shape = (1176,))#candidate|7281|(1176,)|var|float64
output = func_7280(var_7281)
func_7282 = relay.Function([var_7281], output)
mutated_mod['func_7282'] = func_7282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1957_call = mod.get_global_var('func_1957')
func_1959_call = mutated_mod.get_global_var('func_1959')
call_7313 = func_1957_call()
call_7314 = func_1957_call()
func_5732_call = mod.get_global_var('func_5732')
func_5733_call = mutated_mod.get_global_var('func_5733')
call_7317 = relay.TupleGetItem(func_5732_call(), 0)
call_7318 = relay.TupleGetItem(func_5733_call(), 0)
output = relay.Tuple([call_7313,call_7317,])
output2 = relay.Tuple([call_7314,call_7318,])
func_7336 = relay.Function([], output)
mod['func_7336'] = func_7336
mod = relay.transform.InferType()(mod)
output = func_7336()
func_7337 = relay.Function([], output)
mutated_mod['func_7337'] = func_7337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2628_call = mod.get_global_var('func_2628')
func_2629_call = mutated_mod.get_global_var('func_2629')
call_7341 = relay.TupleGetItem(func_2628_call(), 0)
call_7342 = relay.TupleGetItem(func_2629_call(), 0)
output = relay.Tuple([call_7341,])
output2 = relay.Tuple([call_7342,])
func_7366 = relay.Function([], output)
mod['func_7366'] = func_7366
mod = relay.transform.InferType()(mod)
output = func_7366()
func_7367 = relay.Function([], output)
mutated_mod['func_7367'] = func_7367
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7456 = relay.const(-1, dtype = "int16")#candidate|7456|()|const|int16
var_7457 = relay.var("var_7457", dtype = "int16", shape = (15, 13, 1))#candidate|7457|(15, 13, 1)|var|int16
bop_7458 = relay.subtract(const_7456.astype('int16'), var_7457.astype('int16')) # shape=(15, 13, 1)
uop_7465 = relay.tan(var_7457.astype('float32')) # shape=(15, 13, 1)
output = relay.Tuple([bop_7458,uop_7465,])
output2 = relay.Tuple([bop_7458,uop_7465,])
func_7478 = relay.Function([var_7457,], output)
mod['func_7478'] = func_7478
mod = relay.transform.InferType()(mod)
mutated_mod['func_7478'] = func_7478
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7479 = relay.var("var_7479", dtype = "int16", shape = (15, 13, 1))#candidate|7479|(15, 13, 1)|var|int16
func_7478_call = mutated_mod.get_global_var('func_7478')
call_7480 = func_7478_call(var_7479)
output = call_7480
func_7481 = relay.Function([var_7479], output)
mutated_mod['func_7481'] = func_7481
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7483 = relay.const(-9.022819, dtype = "float64")#candidate|7483|()|const|float64
const_7484 = relay.const([[[5.772147,1.337199],[-5.804286,-5.282461],[4.065537,1.087526],[-9.289511,3.602213],[5.867536,-4.559716],[7.856699,6.772128],[7.641247,-9.559383],[3.848248,-3.895586],[-9.384546,-2.772028],[-4.572088,-1.749143],[-5.442984,0.658948],[-3.313150,6.029380],[4.432494,6.615213]],[[-0.263552,2.900357],[9.732734,-0.637465],[7.976258,3.928144],[-5.484783,-3.961306],[-0.174428,-4.164156],[-3.797343,-0.667866],[6.193954,-4.896586],[6.626621,8.982130],[2.422517,4.712294],[9.711647,8.954905],[-7.509347,-6.930254],[-0.414245,7.247093],[7.743431,2.812845]],[[3.913534,3.236780],[7.036746,1.903377],[2.525451,4.030575],[9.669764,-0.768177],[-0.970044,-9.989616],[-0.085501,9.553918],[5.324326,-1.581693],[9.046238,2.758971],[3.313750,8.991841],[-0.760313,3.822742],[0.044258,-5.320874],[9.219901,3.184914],[-9.998195,-2.820175]]], dtype = "float64")#candidate|7484|(3, 13, 2)|const|float64
bop_7485 = relay.subtract(const_7483.astype('float64'), const_7484.astype('float64')) # shape=(3, 13, 2)
func_2820_call = mod.get_global_var('func_2820')
func_2821_call = mutated_mod.get_global_var('func_2821')
call_7488 = relay.TupleGetItem(func_2820_call(), 4)
call_7489 = relay.TupleGetItem(func_2821_call(), 4)
output = relay.Tuple([bop_7485,call_7488,])
output2 = relay.Tuple([bop_7485,call_7489,])
func_7495 = relay.Function([], output)
mod['func_7495'] = func_7495
mod = relay.transform.InferType()(mod)
mutated_mod['func_7495'] = func_7495
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7495_call = mutated_mod.get_global_var('func_7495')
call_7496 = func_7495_call()
output = call_7496
func_7497 = relay.Function([], output)
mutated_mod['func_7497'] = func_7497
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7519 = relay.var("var_7519", dtype = "float64", shape = (1, 2))#candidate|7519|(1, 2)|var|float64
uop_7520 = relay.tan(var_7519.astype('float64')) # shape=(1, 2)
output = relay.Tuple([uop_7520,])
output2 = relay.Tuple([uop_7520,])
func_7544 = relay.Function([var_7519,], output)
mod['func_7544'] = func_7544
mod = relay.transform.InferType()(mod)
var_7545 = relay.var("var_7545", dtype = "float64", shape = (1, 2))#candidate|7545|(1, 2)|var|float64
output = func_7544(var_7545)
func_7546 = relay.Function([var_7545], output)
mutated_mod['func_7546'] = func_7546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5468_call = mod.get_global_var('func_5468')
func_5469_call = mutated_mod.get_global_var('func_5469')
call_7551 = relay.TupleGetItem(func_5468_call(), 0)
call_7552 = relay.TupleGetItem(func_5469_call(), 0)
output = relay.Tuple([call_7551,])
output2 = relay.Tuple([call_7552,])
func_7554 = relay.Function([], output)
mod['func_7554'] = func_7554
mod = relay.transform.InferType()(mod)
mutated_mod['func_7554'] = func_7554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7554_call = mutated_mod.get_global_var('func_7554')
call_7555 = func_7554_call()
output = call_7555
func_7556 = relay.Function([], output)
mutated_mod['func_7556'] = func_7556
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2858_call = mod.get_global_var('func_2858')
func_2859_call = mutated_mod.get_global_var('func_2859')
call_7569 = func_2858_call()
call_7570 = func_2858_call()
func_7097_call = mod.get_global_var('func_7097')
func_7099_call = mutated_mod.get_global_var('func_7099')
call_7575 = relay.TupleGetItem(func_7097_call(), 3)
call_7576 = relay.TupleGetItem(func_7099_call(), 3)
func_3453_call = mod.get_global_var('func_3453')
func_3455_call = mutated_mod.get_global_var('func_3455')
call_7588 = func_3453_call()
call_7589 = func_3453_call()
output = relay.Tuple([call_7569,call_7575,call_7588,])
output2 = relay.Tuple([call_7570,call_7576,call_7589,])
func_7591 = relay.Function([], output)
mod['func_7591'] = func_7591
mod = relay.transform.InferType()(mod)
output = func_7591()
func_7592 = relay.Function([], output)
mutated_mod['func_7592'] = func_7592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5363_call = mod.get_global_var('func_5363')
func_5365_call = mutated_mod.get_global_var('func_5365')
call_7651 = relay.TupleGetItem(func_5363_call(), 0)
call_7652 = relay.TupleGetItem(func_5365_call(), 0)
output = call_7651
output2 = call_7652
func_7655 = relay.Function([], output)
mod['func_7655'] = func_7655
mod = relay.transform.InferType()(mod)
mutated_mod['func_7655'] = func_7655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7655_call = mutated_mod.get_global_var('func_7655')
call_7656 = func_7655_call()
output = call_7656
func_7657 = relay.Function([], output)
mutated_mod['func_7657'] = func_7657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7591_call = mod.get_global_var('func_7591')
func_7592_call = mutated_mod.get_global_var('func_7592')
call_7706 = relay.TupleGetItem(func_7591_call(), 1)
call_7707 = relay.TupleGetItem(func_7592_call(), 1)
func_5282_call = mod.get_global_var('func_5282')
func_5286_call = mutated_mod.get_global_var('func_5286')
const_7719 = relay.const([-7.941843,7.789769,-1.458488,1.985289,-8.115860,-4.746643,5.355382,1.702914,-8.604104,-7.988196,6.864141,0.395136,4.783818,1.088236,5.933275,4.455265,-9.585991,8.287762,7.547108,-9.677726,7.919178,6.994789,-4.719391,-9.365997,-0.088347,-8.127035,-0.112439,-9.858711,1.131298,-1.488562,-1.121594,-3.997631,-5.108494,-2.418983,7.827875,-9.189702,5.716775,6.677453,-6.437049,-5.539666,-3.060584,5.852614,-6.743966,-4.219790,8.593146,-7.381694,0.691299,7.926510,-8.305073,6.377713,-3.927297,-9.946174,3.469177,-1.044487,-3.276932,-2.807403,2.755137,7.595025,-3.299302,7.266032,0.912908,3.983457,-3.101917,-1.324684,-3.663607,-5.756791,7.755874,-0.672451,-0.815359,7.120706,-3.164820,2.053449,2.110654,9.551501,3.888469,1.800642,5.494122,4.710858,3.833690,-2.116501,9.217579,7.562427,-5.207305,8.027049,-8.160179,1.566152,6.187341,-6.496063,5.789914,-5.447948,-6.866291,3.210031,-8.345034,5.160179,8.881389,-8.278011,9.241730,8.267756,4.339459,-7.052962,8.593890,-3.762096,5.597978,3.993822,4.693029,0.493393,-1.292159,8.695465,4.356953,-1.907041,-6.804488,0.322362,-4.590959,8.409077,6.615069,0.626752,2.357157,6.606765,-7.353956,-3.420931,-1.678126,5.685369,-6.080782,-0.034655,-2.761237,-1.362615,1.068061,-9.520393,3.456305,7.956022,9.723885,6.693885,4.631074,5.834685,-6.494259,8.287072,4.778022,2.003714,4.207222,2.661467,-9.592473,-7.895525,1.006409,-6.088175,4.502508,-1.382270,-7.963197,2.419120,-5.238955,-2.597425,-9.405917,-3.702562,-3.812427,-6.829292,8.211554,3.906779,3.350001,1.521934,-5.024102,2.776002,1.613748,3.027167,-9.366427,9.293057,0.790172,8.276677,4.695803,-5.932271,2.953709,2.850274,-6.840245,-6.686940,0.987940,1.241403,0.872238,3.323362,-6.149828,3.874928,7.068463,2.450163,-5.345023,4.239635,-1.743997,9.627765,-5.919861,-4.026790,-5.073062,-7.728217,-4.957998,4.906367,6.283812,9.311492,0.295785,-8.517916,2.569370,-5.939177,-3.669586,-6.657947,4.781471,-8.948211,-8.001573,-6.022976,9.597554,-3.433844,-7.220861,-8.230488,-8.656686,8.508257,-0.996085,2.907510,-0.413644,2.652346,2.036727,3.212963,3.187381,-5.273962,3.081419,-8.006423,9.679486,-7.752362,3.176141,7.395685,-6.847843,3.935989,-8.937730,2.273031,-6.036676,1.889130,-3.608044,-8.190201,-4.812546,5.737123,-3.118657,3.649939,6.980072,3.478401,-0.435292,-7.996039,-4.921814,9.104157,-5.491450,4.077921,0.408699,-3.416813,2.184556,2.775188,6.339804,4.751336,2.360775,-8.449861,5.858203,6.095473,-6.845235,-1.544472,3.270160,-9.625077,-9.618013,6.369048,-9.978650,8.016269,-3.419823,-1.343756,-7.701500,3.213286,-4.272092,-4.144488,-8.073627,7.273332,7.944277,2.700808,4.396970,8.513931,5.063247,0.597700,-1.363773,5.559249,2.047174,2.065930,-7.196658,4.467564,-0.038106,-9.786491,9.156952,7.000664,4.776462,-8.878495,-0.159203,8.178969,-8.246355,-1.936980,6.087397,3.632897,3.297110,-2.097427,-3.592590,-4.702834,9.012317,9.390929,-0.848163,-8.003937,9.238217,-5.711394,-2.091730,7.418998,-4.163403,0.253720,9.097709,-4.398792,7.561260,-7.201399,5.237182,-8.220582,7.779518,4.675518,2.690979,-5.421751,-3.256564,-1.211103,-3.327751,1.932912,0.661518,-6.198887,-7.949755,3.989715,-6.091771,6.906555,-0.030963,-8.572213,0.582063,5.948301,3.819344,1.786386,-0.816631,-0.808263,6.097592,2.899653,1.320422,7.991871,9.052585,2.687894,2.705335,5.785662,3.887573,1.599623,6.897536,8.418170,-7.466108,0.063900,-9.916344,8.893293,3.804314,8.320923,3.479975,-0.587983,0.453548,-6.050729,-2.278458,0.392026,4.188971,-5.919356,5.879715,-7.294514,-5.931707,5.169375,8.003094,-3.476435,7.837033,7.324693,6.071910,2.411124,-7.170506,6.364544,8.926654,-3.753311,1.445496,-5.966497,-7.306478,1.346337,-6.278954,4.904024,7.764413,-6.029712,3.221595,0.317565,-0.803702,-8.584918,-8.731685,5.025141,-2.294737,2.913945,3.949303,-3.794329,-0.048915,-9.054704,-9.829679,-2.227411,-0.032003,5.818053,6.479447,-6.713756,1.994088,-7.445847,-0.501855,-8.240744,7.522022,-7.780133,3.275769,-5.753509,-2.401818,-5.522132,-0.485100,1.703882,4.231947,8.132672,2.331204,-1.537756,-7.372214,5.387097,7.306245,6.698317,0.242978,9.557820,-6.334332,-5.696241,-6.719217,-3.810089,0.175939,5.080440,-7.198701,9.211895,-2.420168,-9.706747,-4.821663,2.978802,5.452476,-9.522377,3.388980,3.424240,9.698125,-1.466027,-3.242264,1.853462,-4.811527,0.633947,0.077657,6.558985,-6.999695,-9.505959,0.893739,-5.579258,-1.634775,8.078848,-4.899266,1.168782,-6.605962,-1.650954,-8.224704,-9.060505,-2.841512,2.578421,0.028706,-5.515476,1.738236,-6.012305,-7.106191,9.053341,-3.379823,-5.875730,-4.537018,-6.223598,-6.452977,6.086755,-2.047533,9.407405,9.861760,-7.386591,4.998867,4.535065,9.116258,7.618270,-4.527095,-9.583840,0.698082,-7.658489,1.270291,-2.216198,4.942882,-6.668203,-0.188357,-8.686950,4.714012,-7.149119,2.702930,9.290519,4.255093,1.520206,1.192995,-3.782923,-0.225081,-7.497882,-5.746300,6.582082,1.882274,2.798139,-7.658046,5.189917,9.740166,-8.974819,8.050650,0.921130,2.034910,8.705954,0.192291,6.651798,-8.557062,3.000797,6.468946,-9.182535,-4.266010,-7.734364,3.123395,-0.561866,6.695721,-4.382343,-1.720033,2.061443,-5.235705,1.525607,7.450471,3.762040,-1.950550,-1.649012,-2.133220,-4.503969,-1.205494,8.203757,3.254031,-6.152156,-1.518826,7.774423,8.483794,-1.029794,9.499307,8.730603,4.376647,-2.055527,8.081352,5.055093,6.483511,-4.703735,-1.116395,-4.538900,-0.631113,-4.243781,0.140038,8.961952,-1.905535,-5.079017,7.280878,-7.330182,-3.349220,7.252888,1.307834,4.101312,-5.005002,9.758850,6.222106,-8.369731,-6.526105,3.414422,9.245646,-2.175535,-2.782473,2.036470,-0.719123,-0.854814,3.905772,-6.822343,-6.264571,9.253956,-1.828115,1.335372,-6.576546,4.908482,-2.615986,-2.436531,9.261251,-8.590703,2.834026,-3.432374,4.777505,7.933220,-2.991244,-1.652872,3.345255,0.785266,-8.881134,-5.102707,3.187221,1.690321,-3.647760,1.983262,9.264228,3.909065,2.817157,-1.031048,1.286806,3.776313,-1.057685,-8.868640,-9.770635,4.374774,7.182060,2.099546,9.489185,-3.626410,7.806356,3.734906,6.091885,0.545662,-4.497412,-2.220013,9.703739,6.278381,5.361015,-8.274723,-6.662858,-7.287596,0.576726,-6.269704,-3.619388,-4.048660,-8.882232,-3.656428,-5.883424,-6.601756,-0.219087,-1.261876,9.267216,1.768722,-5.055511,-0.771480,7.067815,-6.049904,-7.248626,0.086091,7.622587,-9.840523,4.729643,-6.462535,8.574979,6.756033,2.051727,0.294217,7.972981,6.737128,-4.551991,-6.759714,-1.522356,-2.606426,4.005433,1.539637,4.513862,-3.620373,6.960379,7.246431,-1.266975,-8.357520,-3.212379,-0.225024,-8.467082,1.982695,1.824838,-5.382483,-3.794485,-1.913727,-3.266161,3.664223,-1.138133,-1.249816,-5.295321,-2.771654,-7.747057,-3.780142,-5.376611,4.363108,-3.753910,-6.202887,-4.099620,6.429402,3.222372,4.724211,6.248377,-6.501282,-8.587386,2.495864,-6.087237,6.521904,-8.972207,4.122915,-7.965350,4.578652,-6.136516,-7.715413,-3.801122,9.696574,-6.288674,7.230601,3.007487,5.292819,2.082678,-0.762467,-5.642566,-1.233191,4.461161,6.694040,-0.734550,-3.120649,-6.236950,-0.864441,-6.606239,2.422088,-0.243946,9.686404,-8.144004,2.210151,5.282528,2.074153,-5.635725,4.753326,2.835495,9.323088,8.760175,-9.504144,0.952280,2.368089,5.636951,-9.208242,5.655696,6.590750,-6.385170,3.399772,7.784634,6.580454,1.214825,9.517857,4.901430,-7.472223,3.890193,5.207089,2.657029,-7.712566,3.551852,-9.888215,-2.653817,-5.174706,5.975517,8.287838,-1.544485,-2.118722,6.082386,-5.136735,-8.433183,0.312210,-9.613481,-6.040705,7.200741,-5.968197,6.068293,-5.993477], dtype = "float32")#candidate|7719|(770,)|const|float32
var_7720 = relay.var("var_7720", dtype = "uint64", shape = (2, 504))#candidate|7720|(2, 504)|var|uint64
call_7718 = relay.TupleGetItem(func_5282_call(relay.reshape(const_7719.astype('float32'), [5, 14, 11]), relay.reshape(var_7720.astype('uint64'), [1008,]), ), 0)
call_7721 = relay.TupleGetItem(func_5286_call(relay.reshape(const_7719.astype('float32'), [5, 14, 11]), relay.reshape(var_7720.astype('uint64'), [1008,]), ), 0)
var_7722 = relay.var("var_7722", dtype = "uint64", shape = (2, 504))#candidate|7722|(2, 504)|var|uint64
bop_7723 = relay.right_shift(var_7720.astype('uint8'), relay.reshape(var_7722.astype('uint8'), relay.shape_of(var_7720))) # shape=(2, 504)
func_2406_call = mod.get_global_var('func_2406')
func_2408_call = mutated_mod.get_global_var('func_2408')
call_7726 = relay.TupleGetItem(func_2406_call(), 0)
call_7727 = relay.TupleGetItem(func_2408_call(), 0)
output = relay.Tuple([call_7706,call_7718,const_7719,bop_7723,call_7726,])
output2 = relay.Tuple([call_7707,call_7721,const_7719,bop_7723,call_7727,])
func_7729 = relay.Function([var_7720,var_7722,], output)
mod['func_7729'] = func_7729
mod = relay.transform.InferType()(mod)
mutated_mod['func_7729'] = func_7729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7729_call = mutated_mod.get_global_var('func_7729')
var_7731 = relay.var("var_7731", dtype = "uint64", shape = (2, 504))#candidate|7731|(2, 504)|var|uint64
var_7732 = relay.var("var_7732", dtype = "uint64", shape = (2, 504))#candidate|7732|(2, 504)|var|uint64
call_7730 = func_7729_call(var_7731,var_7732,)
output = call_7730
func_7733 = relay.Function([var_7731,var_7732,], output)
mutated_mod['func_7733'] = func_7733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2366_call = mod.get_global_var('func_2366')
func_2367_call = mutated_mod.get_global_var('func_2367')
call_7737 = relay.TupleGetItem(func_2366_call(), 0)
call_7738 = relay.TupleGetItem(func_2367_call(), 0)
output = call_7737
output2 = call_7738
func_7756 = relay.Function([], output)
mod['func_7756'] = func_7756
mod = relay.transform.InferType()(mod)
output = func_7756()
func_7757 = relay.Function([], output)
mutated_mod['func_7757'] = func_7757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3498_call = mod.get_global_var('func_3498')
func_3499_call = mutated_mod.get_global_var('func_3499')
call_7814 = relay.TupleGetItem(func_3498_call(), 0)
call_7815 = relay.TupleGetItem(func_3499_call(), 0)
output = relay.Tuple([call_7814,])
output2 = relay.Tuple([call_7815,])
func_7819 = relay.Function([], output)
mod['func_7819'] = func_7819
mod = relay.transform.InferType()(mod)
mutated_mod['func_7819'] = func_7819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7819_call = mutated_mod.get_global_var('func_7819')
call_7820 = func_7819_call()
output = call_7820
func_7821 = relay.Function([], output)
mutated_mod['func_7821'] = func_7821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5348_call = mod.get_global_var('func_5348')
func_5350_call = mutated_mod.get_global_var('func_5350')
call_7844 = relay.TupleGetItem(func_5348_call(), 0)
call_7845 = relay.TupleGetItem(func_5350_call(), 0)
func_4153_call = mod.get_global_var('func_4153')
func_4156_call = mutated_mod.get_global_var('func_4156')
var_7850 = relay.var("var_7850", dtype = "float64", shape = (3, 90))#candidate|7850|(3, 90)|var|float64
call_7849 = relay.TupleGetItem(func_4153_call(relay.reshape(var_7850.astype('float64'), [9, 10, 3]), relay.reshape(var_7850.astype('float64'), [9, 10, 3]), ), 1)
call_7851 = relay.TupleGetItem(func_4156_call(relay.reshape(var_7850.astype('float64'), [9, 10, 3]), relay.reshape(var_7850.astype('float64'), [9, 10, 3]), ), 1)
func_4629_call = mod.get_global_var('func_4629')
func_4633_call = mutated_mod.get_global_var('func_4633')
const_7870 = relay.const([[True,True,True,False,True,False,True,True]], dtype = "bool")#candidate|7870|(1, 8)|const|bool
var_7871 = relay.var("var_7871", dtype = "float64", shape = (1176,))#candidate|7871|(1176,)|var|float64
call_7869 = relay.TupleGetItem(func_4629_call(relay.reshape(const_7870.astype('bool'), [1, 8]), relay.reshape(var_7871.astype('float64'), [1176,]), relay.reshape(var_7871.astype('float64'), [1176,]), ), 0)
call_7872 = relay.TupleGetItem(func_4633_call(relay.reshape(const_7870.astype('bool'), [1, 8]), relay.reshape(var_7871.astype('float64'), [1176,]), relay.reshape(var_7871.astype('float64'), [1176,]), ), 0)
func_1665_call = mod.get_global_var('func_1665')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_7884 = relay.TupleGetItem(func_1665_call(), 0)
call_7885 = relay.TupleGetItem(func_1667_call(), 0)
output = relay.Tuple([call_7844,call_7849,var_7850,call_7869,const_7870,var_7871,call_7884,])
output2 = relay.Tuple([call_7845,call_7851,var_7850,call_7872,const_7870,var_7871,call_7885,])
func_7886 = relay.Function([var_7850,var_7871,], output)
mod['func_7886'] = func_7886
mod = relay.transform.InferType()(mod)
var_7887 = relay.var("var_7887", dtype = "float64", shape = (3, 90))#candidate|7887|(3, 90)|var|float64
var_7888 = relay.var("var_7888", dtype = "float64", shape = (1176,))#candidate|7888|(1176,)|var|float64
output = func_7886(var_7887,var_7888,)
func_7889 = relay.Function([var_7887,var_7888,], output)
mutated_mod['func_7889'] = func_7889
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7908 = relay.var("var_7908", dtype = "float64", shape = (16, 2, 7))#candidate|7908|(16, 2, 7)|var|float64
uop_7909 = relay.erf(var_7908.astype('float64')) # shape=(16, 2, 7)
bop_7912 = relay.bitwise_or(var_7908.astype('uint16'), relay.reshape(uop_7909.astype('uint16'), relay.shape_of(var_7908))) # shape=(16, 2, 7)
uop_7926 = relay.sigmoid(bop_7912.astype('float32')) # shape=(16, 2, 7)
output = relay.Tuple([uop_7926,])
output2 = relay.Tuple([uop_7926,])
func_7932 = relay.Function([var_7908,], output)
mod['func_7932'] = func_7932
mod = relay.transform.InferType()(mod)
var_7933 = relay.var("var_7933", dtype = "float64", shape = (16, 2, 7))#candidate|7933|(16, 2, 7)|var|float64
output = func_7932(var_7933)
func_7934 = relay.Function([var_7933], output)
mutated_mod['func_7934'] = func_7934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1776_call = mod.get_global_var('func_1776')
func_1777_call = mutated_mod.get_global_var('func_1777')
call_7979 = relay.TupleGetItem(func_1776_call(), 0)
call_7980 = relay.TupleGetItem(func_1777_call(), 0)
func_4861_call = mod.get_global_var('func_4861')
func_4863_call = mutated_mod.get_global_var('func_4863')
const_7984 = relay.const([[-6.420894,2.252158,0.414177,5.142483,-4.049496,-7.291507,-0.613099,-8.291194,-9.527072,-6.997672,8.054589,0.195262,4.731763,-7.319922,2.382344,8.564814,6.120421,5.750370,6.418826,-2.909740,-6.360942,-6.056219,0.589758,-4.701415,6.676501,3.869059,2.979914,-7.075023,1.149980,-4.357628,-8.602669,-3.591162,-3.453783,-2.710527,-9.083906,4.118467,8.190501,0.543589,-7.284841,-2.552164,-7.410784,-4.322255,-4.057209,-4.541752,-9.600397,-9.377842,-2.876169,-8.762300,-4.154194,-9.099006,8.639611,-1.443853,-1.373500,1.601475,4.382683,-0.203606,5.998836,8.584912,3.212725,8.569669,-0.812023,-8.235600,6.869943,4.673896,3.825693,-9.107719,-9.644676,-0.401431,6.439704,5.001326,6.913622,-5.483178,0.811260,5.180459,-4.611096,-1.410902,-9.810907,5.186007,5.009680,-2.465241,3.451213,3.595770,9.891588,-5.334221,6.777246,7.814950,9.896488,-3.057730,-0.465674,-9.171027,-7.654188,3.247911,1.698180,-7.324284,-2.457649,-1.228480,-3.352555,6.182474,5.061396,-9.138251,2.584833,0.253481,1.011111,0.563108,4.991673,-5.147365,-2.717654,2.338808,5.606120,-1.290093,-0.228069,8.922131,-7.355181,-5.142511,-3.451387,9.982785,-5.882742,-2.012310,-1.918766,6.507826,4.160124,8.939465,-2.029037,-3.720364,5.047293,3.298218,7.630356,-9.214339,2.014300,3.334621,6.096161,0.012488,8.082474,5.319714,-7.134430,-3.467983,1.186664,9.000539,-0.586571,2.747846,3.503773,7.942455,2.775803,-7.635509,-3.306249,-4.356967,-4.277114,3.131663,8.471611,0.600551,-2.859818,-5.028663,-3.013573,5.157651,6.836495,-3.628995,2.303019,6.768513,0.697272,2.630188,2.760676,1.147296,2.714251,4.014854,4.313418,-5.296909,-9.046789,0.687023,0.072404,6.221719,4.277719,5.976458,4.422066,2.015257,-0.258293,-4.141729,-0.377774,-6.939649,1.809749,1.107561,-7.668591,-2.401287,-1.195705,2.403172,-3.360028,-5.717342,-8.477958,-8.752104,-6.691945,-5.822170,-8.585810,-3.370532,-8.751662,-5.526802,-3.289304,4.523639,-5.594523,-4.431389,3.327523,-2.730097,-4.095634,-7.193120,-4.432051,2.842461,-4.988933,5.897553,-7.640493,-1.150759,-5.667854,-2.940962,-3.883246,-9.133969,7.609583,7.302667,-3.277891,-9.924219,-1.621175,-3.554306,2.999177,5.471808,0.098685,-7.758441,-4.644698,1.519164,-3.635501,4.343501,4.022016,5.390404,-5.754663,3.438985,-9.864931,-6.606074,-9.547752,2.048408,-3.420945,-1.395353,3.127808,0.219686,6.182157,2.234801,2.152191,-6.002109,-8.363504,5.195749,-3.366925,4.567059,3.572873,8.861003,-1.343784,7.022912,0.618334,8.790197,8.588429,-2.586144,1.251187,-3.435897,-1.300635,4.024353,-6.817941,-8.652336,5.159186,6.916446,6.546673,5.243494,1.171220,-0.185729,-9.519647,8.487758,-7.510989,-2.640184,6.067540,-7.561490,7.309594,-7.601782,2.914065,-6.714990,6.051411,0.067182,-2.661749,-2.867071,4.848706,-4.553154,-7.417861,3.293118,3.211578,-3.708624,-5.277289,-8.096050,-2.387482,2.462939,7.286338,4.739241,3.979751,0.280262,4.018837,4.141130,-7.109304,-9.168166,-8.602324,-6.571456,5.037977,-0.428091,9.272924,1.291670,-8.728559,7.836233,-8.207759,-6.989747,3.792274,0.333061,7.497759,-7.459391,-4.162009,3.875791,-0.295011,-6.651177,-6.899157,-1.912597,3.263539,-8.048617,-7.794629,-2.553613,-9.860197,5.714263,-9.911738,-0.563634,6.751231,-1.293299,3.380486,-3.941368,9.763588,2.112825,-2.016739,5.200250,2.667627,2.094259,-5.890732,-3.040456,-0.377395,-1.803179,-4.854421,-6.373535,0.204502,3.198803,-8.057585,8.128301,-9.321153,-2.155934,-7.877598,-0.687882,4.801337,9.835153,1.520445,-5.777880,3.669761,8.952899,4.305994,-6.939188,-9.909695,8.627888,2.293972,-9.173292,5.931157,-1.285236,-7.676838,9.874888,-3.468819,1.775217,-9.838141,8.113284,8.251064,2.796902,6.695703,7.240460,7.290369,-2.761054,6.614122,-6.917852,2.135965,-4.565250,3.822104,7.690874,3.209355,-3.024591,-0.133108,0.153799,-4.329289,-1.993558,-7.449973,3.819743,-7.117531,9.224808,-6.213777,-3.621215,-5.014797,7.024700,-2.564905,-7.113883,-8.685967,1.398746,-6.238879,-4.194456,8.588580,-4.975217,-3.586287,9.341622,-0.638591,8.700678,-6.860374,-6.972171,-0.038328,6.467036,4.937251,-4.597236,-6.831249,-7.459861,4.203996,5.504746,-2.295155,-5.245098,8.209654,6.222951,-5.256063,-3.580234,6.135698,-6.605089,-9.130352,-0.581724,2.467972,3.870562,6.316911,-2.387524,-3.297923,9.230175,-9.827214,-5.752948,-5.445036,2.726219,-0.341773,7.182175,-5.986604,3.401471,1.576074,-7.825848,5.188020,-3.684913,-6.421765,5.093670,-2.363521,6.282826,-8.685974,-1.122238,8.210601,-6.892302,5.147561,9.935048,8.329116,0.989374,6.759900,8.711782,8.420125,6.418003,-0.262635,3.231917,3.649426,7.398345,-4.049459,-9.595872,1.088472,8.646327,3.029530,4.509795,4.334988,0.219804,-5.078158,3.937354,5.646992,1.182600,3.430813,-8.531869,3.514974,9.971862,-3.365122,-8.390074,-2.809029,-8.573660,-1.760599,-4.056725,-3.154930,-4.104302,-8.584123,3.444165,-8.157912,6.198650,1.358800,1.284874,-3.369355,-5.234898,-6.146384,-0.502281,-4.988849,-6.460504,-3.705696,-2.648880,9.669844,-3.435314,0.907952,5.348257,-4.216535,3.782944,-9.417254,4.143154,0.244817,6.877623,-9.754319,-4.549899,4.690354,1.399074,8.842740,-3.268897,4.222466,-5.200408,-5.096861,-7.687231,8.043691,-6.764532,-6.121020,-5.785462,7.386788,-3.543452,8.777801,-2.339148,8.391994,7.478740,-4.014178,1.510453,-7.723105,-4.183040,0.330983,1.982618,-3.368341,4.290973,7.211002,2.762089,4.573339,-7.020996,-0.802319,3.567664,7.405413,5.145945,9.822219,6.035906,-9.726934,-0.018057,-1.261281,-3.430046,-1.649880,-5.831530,1.454704,-8.539986,0.774635,-7.826426,-5.065707,7.328940,-9.460476,1.299375,-1.251993,5.459249,-3.102500,-5.349461,6.360529,6.539312,-8.523868,-9.643778,6.465688,0.789065,0.847750,0.796557,0.461269,3.094675,3.661827,2.333977,8.873783,-3.990744,9.262046,2.928330,-4.906043,-1.101413,-1.958174,-3.747048,7.210984,-4.419869,6.424364,-2.616426,-9.619009,-2.210034,-0.589176,9.259713,-9.799628,6.471957,1.056777,6.867472,-0.695208,-3.997024,-1.318667,-3.223026,-7.421918,-1.135269,-0.869284,4.830561,8.122275,-5.679183,2.609017,4.556799,-5.653781,3.638655,6.086642,6.232164,-3.539804,-1.284000,-1.830019,7.381017,1.823817,2.560608,-7.407582,9.570174,-0.775198,-1.579951,4.625260,-8.303756,-5.351029,1.478128,-7.632484,9.151527,1.984931,1.618130,9.757302,-9.016754,-1.366854,-9.314154,-7.835489,-3.404305,-6.838490,4.816078,3.680157,1.045432,7.735224,0.729098,1.431122,8.328546,1.862158,-9.509516,9.409427,8.257442,-4.190488,-3.601960,4.685986,-7.983955,0.593804,-8.726562,1.450626,8.988432,-0.954997,-9.217964,3.229911,-6.061999,-2.026837,8.557702,-7.176322,9.069973,1.254695,6.063015,5.606227,-8.187559,9.076248,9.157550,-0.689921,-9.584098,9.112306,-0.300287,-0.763564,1.425823,8.850389,-8.358308,-9.077699,8.996860,4.961620,-2.822773,-0.127451,-6.235791,6.878010,-5.228702,-6.756073,0.651652,3.055287,-0.431000,-6.882505,-5.649201,0.867576,1.284251,-0.398505,5.680055,-4.643052,-7.181765,-1.708226,-0.018068,-8.907762,7.376606,3.231869,7.644059,-7.695782,-5.724641,0.039667,-7.651310,9.966407,-9.405826,-4.686880,-7.882392,-9.311699,1.310659,7.045071,-4.013749,-4.152942,-4.703578,-6.803383,-7.281266,4.968856,-8.936137,9.076008,8.379172,-6.504659,1.481362,9.799753,1.441552,-8.706098,-2.040854,9.355223,-9.522741,-5.019214,9.926635,-5.841474,5.004910,0.466987,-1.633852,0.594338,4.242483,-6.727158,-0.351510,-9.961117,1.072511,1.899006,-8.686237,-5.914068,-3.409690,7.669998,-4.190877,-2.831277,-9.861922,4.183565,-6.554883,-3.054447,-9.233184,-7.247736,9.190247,7.415239,-2.583838,-3.084116,0.806476,4.228740,-9.360195,9.771258,-7.661561,-8.024993,1.091853,8.795898,-3.272020,-0.031799,-7.288001,-1.106343,2.131990,-0.229439,-1.474768,1.690882,-8.451895,5.131996,4.703075,0.798605,-8.957509,-0.001157,3.153255,-8.902655,-9.967608,-9.903511,5.453358,-5.283662,-4.035548,-5.052320,2.066828,-6.012533,-4.299969,-7.543547,5.269983,1.036944,-8.534970,0.978191,-8.784877,0.814804,-6.369449,5.263651,-7.684685,9.133569,0.815518,9.340160,0.510555,-0.916852,-2.262290,6.871072,-1.261535,7.097077,1.885471,-6.264766,-7.250525,-5.404510,1.071189,3.839876,6.820149,6.635438,-7.635827,0.511542,-2.096700,-3.093949,3.096300,-9.622739,-9.345528,-2.847967,8.169308,8.972449,-3.028050,-0.895337,-2.294657,-0.714377,-3.943054,-6.742210,-4.079562,-8.726786,1.271161,1.923813,5.113892,-3.885694,-2.161956,8.870092,5.269303,8.129082,-3.110163,1.353656,8.950230,-7.798495,7.238762,4.255725,-9.266985,4.664535,-4.844208,-1.746128,-0.262429,8.126763,2.591110,-9.810088,-6.478387,8.144915,-9.215123,4.423665,-4.141132,3.347310,-6.053812,1.426524,9.616658,-4.414419,-6.651152,0.963200,9.387575,0.800320,2.655672,9.386136,8.660695,-8.018627,8.314808,-9.529902,5.387447,-9.067734,-1.035794,-4.581067,-8.263177,1.418549,-2.515327,8.212609,1.844985,-9.700572,3.599832,-7.668141,-4.167153,-8.749625,-1.191345,8.969459,-6.703612,3.364670,-7.266773,-2.282174,-9.331521,5.564705,-5.455103,-3.982647,5.544618,-2.139086,-2.518855,4.216844,4.379996,3.890906,-5.107534,1.354048,-1.123605,5.580619,4.052257,1.203039,8.794412,-6.516897,7.812088,-8.674218,1.952087,7.935214,7.287605,8.360654,-7.723787,1.280841,7.056399,-1.369085,3.278646,-0.119699,6.996231,7.001159,-9.949198,4.648921,-8.582569,-3.292488,-8.968563,-4.256378,0.584200,7.349465,-4.030074,-2.623957,9.871181,4.528490,9.746608,5.615953,4.881380,4.013794,-7.617381,3.839722,-9.716455,2.600682,-6.943909,3.509946,3.418230,5.784216,3.995716,4.044812,-4.694410,4.854479,6.958166,2.494946,0.991872,-3.596023,2.761196,7.090182,-4.614313,-4.484191,-7.716740,-2.483367,-0.896343,4.369507,1.625670,6.120872,1.416663,8.750929,7.895821,3.838886,-5.735785,7.292732,7.944121,0.134680,3.700667,-4.899150,3.011602,1.884895,3.743153,4.305267,0.089014,-4.529352,-8.760612,3.875774,-2.948052,-9.262943,4.165129,-2.544775,-8.588051,-2.228907,-9.728824,1.241970,6.662182,2.257512,0.915738,0.338275,5.279193,5.468766,-9.283484,-9.285382,9.135354,7.034328,-3.579839,-9.133151,2.963040,-3.416234,7.263222,-8.868588,-8.323965,7.147277,-7.368360,-2.337105,5.104503,5.891377,4.920398,-1.630243,2.548385,7.355028,-3.844920,-5.794024,-8.416013,4.996569,6.342352,-8.820748,7.138744,7.759820,-8.579774,-9.768867,-3.554132,8.367098,1.045765,-7.633612,1.592338,-0.522213,4.126552]], dtype = "float32")#candidate|7984|(1, 1050)|const|float32
call_7983 = relay.TupleGetItem(func_4861_call(relay.reshape(const_7984.astype('float32'), [5, 210])), 2)
call_7985 = relay.TupleGetItem(func_4863_call(relay.reshape(const_7984.astype('float32'), [5, 210])), 2)
output = relay.Tuple([call_7979,call_7983,const_7984,])
output2 = relay.Tuple([call_7980,call_7985,const_7984,])
func_7997 = relay.Function([], output)
mod['func_7997'] = func_7997
mod = relay.transform.InferType()(mod)
output = func_7997()
func_7998 = relay.Function([], output)
mutated_mod['func_7998'] = func_7998
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5363_call = mod.get_global_var('func_5363')
func_5365_call = mutated_mod.get_global_var('func_5365')
call_8011 = relay.TupleGetItem(func_5363_call(), 0)
call_8012 = relay.TupleGetItem(func_5365_call(), 0)
func_4298_call = mod.get_global_var('func_4298')
func_4302_call = mutated_mod.get_global_var('func_4302')
var_8022 = relay.var("var_8022", dtype = "float64", shape = (48,))#candidate|8022|(48,)|var|float64
var_8023 = relay.var("var_8023", dtype = "float64", shape = (1176,))#candidate|8023|(1176,)|var|float64
call_8021 = relay.TupleGetItem(func_4298_call(relay.reshape(var_8022.astype('float64'), [6, 2, 4]), relay.reshape(var_8023.astype('float64'), [1, 1176]), ), 4)
call_8024 = relay.TupleGetItem(func_4302_call(relay.reshape(var_8022.astype('float64'), [6, 2, 4]), relay.reshape(var_8023.astype('float64'), [1, 1176]), ), 4)
func_2366_call = mod.get_global_var('func_2366')
func_2367_call = mutated_mod.get_global_var('func_2367')
call_8026 = relay.TupleGetItem(func_2366_call(), 0)
call_8027 = relay.TupleGetItem(func_2367_call(), 0)
output = relay.Tuple([call_8011,call_8021,var_8022,var_8023,call_8026,])
output2 = relay.Tuple([call_8012,call_8024,var_8022,var_8023,call_8027,])
func_8037 = relay.Function([var_8022,var_8023,], output)
mod['func_8037'] = func_8037
mod = relay.transform.InferType()(mod)
mutated_mod['func_8037'] = func_8037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8037_call = mutated_mod.get_global_var('func_8037')
var_8039 = relay.var("var_8039", dtype = "float64", shape = (48,))#candidate|8039|(48,)|var|float64
var_8040 = relay.var("var_8040", dtype = "float64", shape = (1176,))#candidate|8040|(1176,)|var|float64
call_8038 = func_8037_call(var_8039,var_8040,)
output = call_8038
func_8041 = relay.Function([var_8039,var_8040,], output)
mutated_mod['func_8041'] = func_8041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3347_call = mod.get_global_var('func_3347')
func_3349_call = mutated_mod.get_global_var('func_3349')
call_8075 = func_3347_call()
call_8076 = func_3347_call()
output = relay.Tuple([call_8075,])
output2 = relay.Tuple([call_8076,])
func_8077 = relay.Function([], output)
mod['func_8077'] = func_8077
mod = relay.transform.InferType()(mod)
mutated_mod['func_8077'] = func_8077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8077_call = mutated_mod.get_global_var('func_8077')
call_8078 = func_8077_call()
output = call_8078
func_8079 = relay.Function([], output)
mutated_mod['func_8079'] = func_8079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1277_call = mod.get_global_var('func_1277')
func_1279_call = mutated_mod.get_global_var('func_1279')
call_8097 = relay.TupleGetItem(func_1277_call(), 3)
call_8098 = relay.TupleGetItem(func_1279_call(), 3)
output = relay.Tuple([call_8097,])
output2 = relay.Tuple([call_8098,])
func_8106 = relay.Function([], output)
mod['func_8106'] = func_8106
mod = relay.transform.InferType()(mod)
output = func_8106()
func_8107 = relay.Function([], output)
mutated_mod['func_8107'] = func_8107
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8130 = relay.const([[[-8.411960,-3.127100,6.308656,-2.418596,-8.021484,-4.918632],[7.052704,-8.316300,-8.449401,2.082459,3.573834,-4.988322],[8.546724,9.482277,-0.427126,5.984995,-8.862643,4.643047],[-3.624609,-1.068374,5.068982,2.745016,7.879661,2.435071],[-9.980717,7.268060,-5.732264,-5.806489,-8.571932,-4.597005],[-1.573104,3.942682,6.680147,-5.120062,5.509938,3.268557],[-8.829412,7.169198,-3.069793,5.742773,8.342387,-5.531198],[-0.151373,-6.532696,-8.142797,1.931963,-5.786641,-3.497450],[4.812233,2.006575,0.606842,7.304288,8.801181,5.974781],[4.403902,-8.788364,-8.095085,0.004671,7.079774,7.457599],[-1.969327,9.660518,7.091263,-3.512618,-6.486703,6.817092]],[[-3.274757,0.192601,-1.070931,6.397257,4.183792,-2.115375],[-4.453771,-9.755389,7.088419,-9.892928,-4.453177,7.801868],[4.545717,-8.687168,3.257454,2.608368,3.555011,-8.409580],[0.680198,2.061910,3.928957,-1.069705,8.073763,-8.964856],[-3.319478,-3.913810,-3.405778,5.420583,-6.009482,1.281401],[4.893535,4.272479,-5.475216,-6.573027,-1.011305,-9.739159],[-5.274959,9.208141,-0.982112,-2.287921,-5.816708,1.038801],[-6.493059,-7.483874,9.542607,7.946594,-8.672667,4.214067],[-8.116222,0.631555,1.314946,-7.430596,-3.771770,-7.305530],[4.665327,-5.196910,7.235602,-2.412518,-4.564741,-5.688973],[0.344899,-3.340206,7.777522,-2.811324,-9.885448,-3.519358]],[[0.309632,6.786980,-7.667217,-1.350942,-9.382334,-5.525530],[1.507688,-3.277408,3.641453,0.217246,-5.507421,2.127274],[3.750951,6.061638,5.428091,7.917057,-0.806122,-7.867819],[-2.750553,7.499352,6.884765,9.349109,-3.176779,-1.366122],[-0.727512,-3.024533,-0.914922,-1.207315,0.269082,0.642314],[3.007165,-3.262323,4.568302,5.973912,7.375957,-5.481542],[-1.934580,8.579569,7.559798,-4.273650,1.652273,-7.712856],[-8.493903,9.623504,-6.894155,-2.862278,-2.644594,-4.159549],[-1.049297,4.220552,-3.039058,-3.117003,9.993285,0.370467],[-8.677322,2.433563,1.440837,2.136263,-7.561615,6.631962],[4.483853,1.104931,-5.796626,5.833623,0.295658,0.005465]],[[-1.867683,-5.505638,0.127453,8.728897,6.970548,-2.764738],[-0.267062,0.611274,-8.264991,-1.934235,-3.079161,8.398749],[3.251683,7.027810,-5.026646,-2.694396,3.383977,-8.033858],[-1.087561,-5.742196,-9.155825,-4.074632,-5.629293,-5.843479],[5.201316,-4.483018,-4.469575,-4.038036,-5.868101,-3.713853],[-4.786485,9.683178,8.998820,7.307237,9.428508,8.625297],[-0.248945,9.602755,4.446891,9.725184,-3.544204,1.091084],[-8.782759,-9.202303,8.951676,0.505753,6.777356,6.419863],[-3.065917,-1.660608,-6.987306,-6.756952,-7.102843,8.242846],[8.684990,-7.340548,-3.903997,-9.888459,2.946520,0.263636],[0.587965,1.901474,-5.155715,1.463293,8.104354,-4.788382]],[[3.165969,-5.453800,-9.625849,-3.766412,-8.689115,0.379577],[-5.049762,5.621231,-7.165325,-7.622191,1.817926,-8.621435],[2.739683,4.171976,-1.317075,-4.300763,-8.494972,6.011893],[5.833168,-1.277700,-3.148306,-0.242416,3.768538,-0.568614],[8.537017,8.246202,-5.519863,-9.959849,0.242169,-8.259779],[1.964171,0.761349,0.514772,6.906171,-9.335818,1.650081],[3.753225,5.588821,1.110576,6.180939,3.957681,-3.087484],[-0.579470,2.654762,-1.460633,4.881855,-1.979432,9.890155],[7.166728,-3.906371,-2.109252,-8.708962,-0.459095,-9.149296],[-9.631239,-0.690131,-7.964871,4.256665,3.889610,-4.680597],[0.946977,0.388913,-0.322258,2.760912,3.406311,-1.072115]],[[6.893074,-1.915101,-5.573257,-4.361326,-2.917683,-7.754042],[9.977844,9.338466,-4.761773,-8.629330,-6.928682,-1.247366],[-3.786783,-7.442044,7.227967,1.946858,-4.365470,-7.268533],[-7.219134,5.216183,7.230740,0.729487,7.969818,6.125708],[-5.822362,3.501561,-2.357193,8.182647,-3.551481,-1.640209],[-3.705488,-1.390396,8.782100,-7.384024,5.049981,-1.378604],[8.664230,2.005183,1.200351,1.710042,-5.670508,-6.519229],[-3.308660,3.373557,3.259680,-9.852969,2.050901,-5.835813],[-1.295521,-2.000340,-1.181527,-8.697428,-6.380508,8.612753],[6.447953,1.451739,8.947257,-2.105440,-4.498005,-8.025711],[2.871920,0.435484,-2.211912,-0.037250,-8.122628,-8.070660]],[[7.781270,1.204366,2.788166,9.731480,6.136521,-4.622066],[-9.456821,-5.042142,9.825843,4.710039,5.228847,0.851051],[-2.759169,-2.836452,6.968973,-4.392559,-4.777157,-7.990055],[-7.090043,-2.553542,1.214811,-0.144451,0.973833,-1.634711],[-5.711677,6.469900,-1.127105,4.055137,-3.582933,-0.507001],[-3.898211,9.558461,-7.717858,-5.672672,0.519606,-8.194680],[-4.614088,1.093196,6.182695,-7.138907,8.229511,8.290862],[-9.060001,-2.119506,3.678661,-1.815825,4.507935,-7.375278],[-7.493394,-2.044930,9.879894,-6.519389,-4.828406,8.573052],[8.523770,7.415297,5.917158,-4.273444,7.865492,6.072412],[1.211110,-1.172298,0.070333,-0.253559,-6.769756,8.832225]],[[3.506593,9.037256,2.282759,3.512267,-1.844351,8.851380],[-2.976513,0.910880,5.675643,-9.218608,6.710839,8.171796],[7.943010,-4.658211,9.878137,6.792009,0.568197,-0.430772],[2.925491,4.981754,-8.082319,0.587796,-4.212693,-3.864911],[4.349148,2.545241,4.703558,2.862248,-4.789315,-9.514347],[-5.593010,1.891215,-7.735836,-0.048917,3.414967,0.524541],[0.992913,-5.548066,-5.833651,5.850502,2.610840,-6.326347],[3.337016,3.300188,3.123299,4.789497,8.815726,0.114739],[-3.316138,3.902702,1.052913,1.103241,-9.922811,-8.166287],[-4.165917,-4.992594,-2.541621,5.429149,8.801994,-1.852915],[-7.930518,-5.899876,-5.710579,-1.922555,4.783660,-1.491497]],[[-4.771824,1.819916,-3.143332,0.879257,6.856204,-3.802483],[-2.202848,-1.972952,0.632612,-2.014552,-4.769152,4.579617],[-2.495689,-1.226858,-9.908248,-6.353154,-8.996780,6.620760],[-0.943882,-2.794594,-1.330433,1.418506,-8.727299,-0.571833],[-1.330551,4.459328,2.333771,6.779163,-2.902372,-8.128747],[3.882025,-2.812209,-7.010119,-2.230592,-0.341531,3.932663],[6.663931,-8.055892,-2.032280,7.990274,6.852266,3.031658],[-2.041425,8.301927,-8.121070,1.635062,-8.909007,-5.587520],[0.297734,7.276771,7.105359,-2.411447,-6.217088,-1.448250],[-6.142950,0.790714,-2.938784,-8.707258,-9.260674,-3.419456],[2.355728,-9.736921,2.213731,9.728495,0.582260,-2.241306]],[[0.428075,0.959177,1.662107,-8.958214,-2.681980,-4.670326],[-8.962917,1.750941,-8.374762,-9.753875,2.571776,1.786126],[3.692562,1.047412,-1.009166,4.020064,-2.783224,9.844557],[-5.259474,6.784915,8.021031,0.598718,2.090104,-9.918964],[-1.646570,2.637714,2.692879,-0.601393,1.954482,4.667922],[-7.163006,0.092905,-2.501482,-0.290036,-6.978511,3.380106],[6.336978,-1.053350,4.375602,-3.792077,2.593648,6.477259],[9.360576,5.726157,1.832570,-5.809287,5.481246,-4.647471],[-0.987031,-7.064960,6.413448,-6.616614,-4.986759,9.126855],[-0.610584,-5.315204,9.787382,-4.667806,9.211097,-4.330432],[1.806054,-6.527272,-1.139872,-7.063230,-3.999311,-2.255474]],[[-1.122157,-0.223408,0.080632,-2.495701,-9.947458,8.205546],[-7.844521,-4.753856,9.915626,-5.475218,2.843557,3.279563],[5.338092,-8.558683,-6.503716,4.191081,2.613552,5.739461],[2.285318,-8.180345,-6.505744,-6.241176,-5.061379,4.154291],[9.907522,-5.770665,-0.988310,-6.679603,4.204972,7.480553],[6.669869,-2.863542,8.578317,5.861175,3.793690,-7.887597],[0.717294,-4.569166,0.302277,2.479117,9.046514,6.338928],[1.723052,5.757868,-6.691486,-2.884604,-5.331187,-1.407007],[9.424952,-7.036210,-8.067547,-2.985818,4.681311,4.315585],[-1.485005,4.674897,-8.641459,-4.559395,9.700441,-0.387173],[-5.942262,9.911311,6.421817,-5.281528,-2.022124,8.464407]],[[3.660996,-6.766851,-5.364814,7.910718,6.995154,-1.782350],[5.768564,7.303721,-1.192066,-8.396101,2.706327,9.975109],[-9.868053,6.551627,0.522609,3.969881,-2.186554,2.736870],[3.850548,-6.201096,-2.463195,-0.496048,7.634811,-4.148790],[4.709497,-3.638207,-0.226541,7.259326,-6.747189,3.733076],[2.013437,-1.962598,0.356811,-8.971042,6.272302,4.715056],[9.049337,8.248297,2.676533,-4.951145,7.665303,0.561616],[6.282484,-1.695780,1.245216,7.690909,-5.541031,2.721882],[9.969675,-4.815152,-6.830293,-0.789327,7.004150,-9.407768],[0.384217,5.169965,8.919755,2.172043,5.617156,-5.601312],[6.817517,9.911341,-9.617049,3.249699,-7.777234,-2.504485]],[[9.376193,-9.928515,-7.335747,-4.753057,7.803243,-0.539573],[-4.615417,5.421025,7.484106,2.142854,7.968032,-3.560823],[0.371336,-0.695962,9.185270,-2.091560,8.785634,8.861587],[7.430436,-9.915885,5.790170,6.029117,-5.192412,4.394757],[7.092030,-0.337091,1.277203,-4.176921,7.234343,-9.584905],[1.938031,2.948106,7.285777,-5.184942,-2.858373,-5.180243],[-6.791067,-1.826469,-2.107676,-4.603858,-2.486038,1.114139],[-9.379432,-1.973267,-4.464083,-9.204067,2.036055,-6.955693],[6.022246,0.325691,7.464188,9.053989,1.493534,-2.416122],[-0.323995,9.402399,-0.293385,-3.801434,-5.248917,-2.351707],[-3.010888,-7.239244,-9.193184,-2.895853,-4.402145,-5.599509]],[[8.038099,3.939941,9.520415,1.816445,-9.441394,-9.276289],[4.722200,4.942410,4.769000,-1.748242,3.037411,8.879153],[3.855882,4.184248,8.538827,-8.204786,5.051891,6.471145],[4.414687,-3.373768,-7.587523,-4.243736,-0.438822,4.497294],[2.109183,9.239460,7.483243,6.673410,-1.858214,-5.141615],[-1.404401,7.578688,-7.736243,-5.132500,0.599925,0.306882],[4.614935,1.959345,-2.584386,8.212416,-9.787772,-8.993895],[1.082177,-9.304600,-9.419483,3.219450,9.758816,-0.928726],[7.342336,-4.019311,-8.816213,-8.329367,8.522724,9.611632],[7.138941,-6.704707,9.118142,2.707542,-9.137360,-0.979017],[-4.674738,5.027085,-8.373046,9.725123,-5.445942,-1.349999]],[[3.981262,-0.101385,-3.784225,-5.432868,-0.131097,8.609932],[7.636061,-1.479496,7.679610,-9.589637,-0.051290,2.331899],[-7.149283,-3.551151,-7.181511,5.311979,-9.854701,4.114616],[0.078355,-0.090406,-9.638047,0.130733,-9.017109,4.752816],[-4.469433,6.606681,8.492327,-5.250663,4.054794,-6.234947],[2.678127,1.135212,6.323273,1.808089,4.829913,-5.429510],[3.867087,4.288043,2.423317,4.183275,8.321475,-3.432949],[-2.463270,-7.444628,9.276064,0.545968,-0.273178,-8.656507],[3.603387,-9.394402,4.130709,-4.430654,-7.901999,-9.991361],[-6.279854,3.917406,-4.408691,-0.518534,-6.858968,-8.563720],[5.783097,7.570662,2.976022,0.262036,5.689648,9.366057]]], dtype = "float64")#candidate|8130|(15, 11, 6)|const|float64
uop_8131 = relay.cos(const_8130.astype('float64')) # shape=(15, 11, 6)
uop_8133 = relay.acos(uop_8131.astype('float64')) # shape=(15, 11, 6)
uop_8136 = relay.sinh(const_8130.astype('float32')) # shape=(15, 11, 6)
func_3317_call = mod.get_global_var('func_3317')
func_3319_call = mutated_mod.get_global_var('func_3319')
const_8144 = relay.const([[True,False,False,True],[False,False,False,True],[True,False,False,True],[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,True,True],[False,False,False,True],[False,True,True,True],[True,True,False,False],[True,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,True],[False,False,False,False],[False,True,False,True],[False,True,False,True],[False,False,True,True],[False,True,True,False],[True,True,False,True],[False,False,False,False],[True,True,True,True]], dtype = "bool")#candidate|8144|(22, 4)|const|bool
call_8143 = relay.TupleGetItem(func_3317_call(relay.reshape(const_8144.astype('bool'), [11, 8, 1])), 3)
call_8145 = relay.TupleGetItem(func_3319_call(relay.reshape(const_8144.astype('bool'), [11, 8, 1])), 3)
output = relay.Tuple([uop_8133,uop_8136,call_8143,const_8144,])
output2 = relay.Tuple([uop_8133,uop_8136,call_8145,const_8144,])
func_8148 = relay.Function([], output)
mod['func_8148'] = func_8148
mod = relay.transform.InferType()(mod)
mutated_mod['func_8148'] = func_8148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8148_call = mutated_mod.get_global_var('func_8148')
call_8149 = func_8148_call()
output = call_8149
func_8150 = relay.Function([], output)
mutated_mod['func_8150'] = func_8150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6151_call = mod.get_global_var('func_6151')
func_6153_call = mutated_mod.get_global_var('func_6153')
call_8156 = func_6151_call()
call_8157 = func_6151_call()
const_8159 = relay.const([[[-4,2,9,8,4,-2,-6,6,4,-6],[-6,-10,6,10,1,5,-6,-5,-1,-10],[2,7,-6,7,2,-3,-2,-7,-4,8],[10,1,10,-2,8,7,-3,7,-9,3],[10,10,-1,-4,-3,10,-4,1,6,5],[5,-3,-8,10,-7,-1,-1,2,-5,4],[-7,-1,-5,4,-6,-7,-5,-1,-3,2],[-6,-8,3,8,6,-6,-8,5,3,-7],[2,-2,-4,-10,4,8,7,8,6,8],[9,9,2,1,5,4,1,4,7,-2],[-10,-2,6,4,7,8,-5,3,8,3],[-3,-3,-3,10,3,-2,2,-9,-5,2]],[[7,7,-4,-1,8,8,-1,4,7,5],[-7,4,-2,-8,8,-8,-10,8,9,8],[3,7,-8,7,6,-7,8,2,6,6],[2,10,-3,7,10,-7,3,7,8,9],[6,9,-7,4,1,-9,6,-6,-10,10],[8,10,-3,3,1,-7,7,-10,7,10],[-2,2,8,6,8,-7,3,-10,-4,-10],[-6,-1,3,1,-5,-9,-2,6,8,10],[-8,-4,4,-9,-8,3,-4,-9,8,-6],[-1,-4,5,-4,2,10,-1,-2,10,-3],[-8,4,-3,-10,3,5,-2,-8,1,-1],[8,-4,8,3,-5,8,-3,7,5,8]],[[-3,3,-4,-2,7,-7,-5,-3,4,2],[-2,-5,1,2,1,-6,-3,-10,2,-3],[7,1,10,6,-1,5,7,10,-4,-5],[-2,-9,-10,3,5,8,-5,-8,4,-9],[2,-10,-6,10,3,-6,6,2,-8,-7],[-1,7,-5,-9,6,-6,1,-1,8,-8],[-7,-6,2,9,2,-3,1,9,2,7],[-7,10,8,-7,-3,7,-1,-2,-2,-3],[7,9,5,-5,5,8,-2,-2,-10,-9],[3,-10,3,-7,3,9,-7,9,6,2],[-4,5,-1,-8,-5,-1,-5,3,4,-10],[4,-8,-10,5,-9,-1,-9,8,-5,-10]],[[-3,9,3,5,3,-4,-9,-8,-9,6],[3,-8,-6,-2,-5,9,3,-8,-9,-6],[10,-9,-4,7,3,-9,3,-9,-6,-9],[-5,-8,6,9,-9,-2,-4,-10,-10,-2],[-2,-9,10,5,-3,4,-5,-10,-10,-10],[1,10,3,-8,6,-7,-10,-7,-6,-4],[-7,9,-3,-4,-6,-4,4,-6,1,-9],[-3,7,-3,-2,7,10,-8,-7,-9,-6],[5,4,1,8,6,-10,6,-2,2,-1],[-2,2,-1,-3,-1,-5,-6,-10,1,-8],[7,-5,5,-3,-1,-5,-5,-5,7,-7],[4,7,-1,6,4,8,-3,-6,10,7]]], dtype = "int8")#candidate|8159|(4, 12, 10)|const|int8
bop_8160 = relay.logical_and(call_8156.astype('bool'), relay.reshape(const_8159.astype('bool'), relay.shape_of(call_8156))) # shape=(4, 12, 10)
bop_8163 = relay.logical_and(call_8157.astype('bool'), relay.reshape(const_8159.astype('bool'), relay.shape_of(call_8157))) # shape=(4, 12, 10)
output = bop_8160
output2 = bop_8163
func_8190 = relay.Function([], output)
mod['func_8190'] = func_8190
mod = relay.transform.InferType()(mod)
mutated_mod['func_8190'] = func_8190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8190_call = mutated_mod.get_global_var('func_8190')
call_8191 = func_8190_call()
output = call_8191
func_8192 = relay.Function([], output)
mutated_mod['func_8192'] = func_8192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3347_call = mod.get_global_var('func_3347')
func_3349_call = mutated_mod.get_global_var('func_3349')
call_8220 = func_3347_call()
call_8221 = func_3347_call()
var_8222 = relay.var("var_8222", dtype = "float64", shape = (7, 3, 15))#candidate|8222|(7, 3, 15)|var|float64
bop_8223 = relay.bitwise_xor(call_8220.astype('uint64'), var_8222.astype('uint64')) # shape=(7, 3, 15)
bop_8226 = relay.bitwise_xor(call_8221.astype('uint64'), var_8222.astype('uint64')) # shape=(7, 3, 15)
func_7655_call = mod.get_global_var('func_7655')
func_7657_call = mutated_mod.get_global_var('func_7657')
call_8234 = func_7655_call()
call_8235 = func_7655_call()
func_4731_call = mod.get_global_var('func_4731')
func_4733_call = mutated_mod.get_global_var('func_4733')
const_8262 = relay.const([1,-1,1,10,7,9,8,5,7,1,-6,-9,-1,-4,-9,1,8,8,-10,-3,6,-6,5,2,-5,5,-1,-4,1,1,3,-1,6,2,10,4,-1,-10,2,-8,7,10,-10,-2,4,-1,7,-10,1,-10,-9,-9,-5,-7,-5,5,8,1,10,9,9,1,-3,-1,-4,9,7,6,-7,10,7,3,3,-5,9,8,-7,-8,-1,7,1,-9,-4,-2,-5,2,-2,-9,-10,9,-10,1,-6,-8,-7,-2,-2,7,-3,6,3,-2,-4,-9,5,8,-5,-3,-8,-7,5,-3,10,3,-9,5,-9,-9,10,-9,-6,-10,-6,9,1,8,7,5,9,3,8,-4,-5,-10,-10,9,6,4,-2,5,-1,1,2,5,5,3,-6,-8,9,5,7,-5,3,6,-4,-9,3,3,8,-1,8,6,-3,4,-4,-3,-2,5,-8,1,1,-7,9,-2,-9,-10,6,-8,10,-1,10,-7,-2,8,-3,-2,-8,-1,-8,-4,3,-2,7,6,-4,6,-10,-8,7,-10,6,7,10,1,-8,-3,-6,-9,-8,4,3,8,3,6,4,10,-10,4,-2,6,-7,-2,7,-7,10,7,-1,7,-10,4,8,6,9,-8,4,-3,-4,-7,10,-5,5,-4,-4,-2,3,-10,10,-1,-7,-1,4,3,1,-8,-4,-1,-5,-9,5,5,7,-1,3,-5,-10,1,-10,-1,-6,4,-3,1,10,-7,1,-1,7,-5,-5,-1,9,-8,-8,-2,1,6,-2,2,-9,5,2,10,9,10,-8,-10,2,-5,-8,-7,-6,-2,10,-10,-4,-8,-2,-6,4,6,6,10,-3,-10,-6,1,10,10,-9,6,7,10,2,2,-1,-1,-6,6,-8,2,5,-5,7,4,6,-9,-6,2,-4,-6,-5,-3,8,10,-6,-7,8,-6,9,-10,2,10,2,-5,-8,-3,-8,4,6,9,8,4,9,-10,-10,5,-4,9,7,-2,5,-6,2,8,-3,9,-6,-7,3,-5,-8,4,-5,5,6,-5,-3,-3,-2,-2,-9,-8,3,10,-1,-8,5,-2,-6,-2,-6,-5,-9,-3,-1,-8,7,-7,-1,6,-2,-2,10,-9,3,-1,8,8,-6,8,6,-10,-4,-5,4,7,-10,4,5,6,-5,-4,5,-8,-3,-8,4,3,-5,-3,2,4,10,-9,3,10,-4,-9,-8,-10,5,1,-6,-9,3,-9,-1,6,-2,4,-4,-1,3,-9,-9,10,-7,-7,-5,7,8,4,10,1,-7,-7,-1,9,-10,-5,-7,7,7,-10,-10,-2,-2,8,-6,-4,-3,-4,-1,8,-1,-4,-9,-6,-3,-9,-3,1,-5,9,-5,-6,4,-3,-5,8,-6,-6,-3,1,9,9,9,9,-9,9,1,-2,-5,2,8,6,4,8,6,-5,7,9,4,-2,-6,6,-6,4,3,-3,-10,4,-3,-3,-2,-4,-2,7,-10,-8,-1,6,3,1,8,5,-3,3,-1,-6,7,-4,-2,-5,-1,3,-9,1,10,6,-6,-7,-7,-8,9,1,-2,4,-5,10,-4,-10,-3,5,-3,-1,-1,1,-1,8,10,5,-4,10,10,5,-5,8,-6,-9,-1,1,1,2,2,3,9,6,8,3,7,3,5,-8,-2,1,9,7,-5,-5,9,10,7,9,3,-5,-2,-10,8,7,7,7,-1,10,-5,4,3,2,-10,-5,-5,-3,7,-3,3,8,7,8,10,-3,-2,-1,-8,5,3,1,8,-6,-7,-3,6,-10,7,-10,-7,3,7,4,-6,3,9,-9,6,-4,-4,-3,10,-3,3,-5,-6,2,4,-1,5,10,-10,2,4,-10,5,-9,9,4,-5,4,7,7,4,-2,1,-4,10,-6,-2,-3,10,-1,-3,-10,-4,-2,-2,4,4,-6,7,8,4,2,-10,2,-6,-10,-10,9,-7,-6,-9,-7,-8,2,1,-5,-3,10,1,-7,4,7,-8,-9,9,-5,8,5,-3,3,4,8,4,-5,9,-3,-9,-9,9,1,-3,-8,8,-9,10,-4,10,4,-1,9,10,7,2,-6,5,-1,-4,1,2,-3,-2,7,-3,3,9,-6,-2,8,-10,-7,2,3,-4,-9,4,9,1,5,-8,-7,-10,7,7,-8,-2,4,-10,9,1,4,-10,-1,-10,4,-5,-6,4,-9,-1,-8,1,-4,-8,8,-10,7,5,2,2,-3,5,-2,-1,9,-7,4,10,-10,10,10,-8,2,4,-9,8,-5,-1,1,9,5,-9,-3,-4,9,-1,-6,7,4,-3,-10,-7,3,2,-2,-6,-7,4,3,-5,4,3,-6,-9,2,5,3,6,10,2,1,6,2,-9,10,9,-9,7,3,-6,-9,6,1,-10,2,-10,9,-2,-8,7,-5,3,7,9,-5,4,6,-6,3,-7,-7,9,-4,6,-2,-1,9,10,1,7,-4,10,2,8,-9,4,3,1,-4,1,-1,-2,-6,6,4,3,-6,-10,8,-6,3,2,-1,5,-1,-3,1,-1,-2,4,2,-3,-2,-7,-9,7,10,7,-4,1,1,8,-3,-8,-7,10,2,10,-4,-2,1,-4,1,-6,-6,-2,3,10,8,1,-10,9,-2,-6,7,1,7,10,-1,-5,-3,5,-7,-2,-2,-2,-1,6,1,4,-10,-7,2,-9,6,-1,2,-3,-10,-6,7,9,-1,3,-9,-2,-2,9,10,9,3,3,6,4,10,-2,-8,-4,10,-10,4,9,5,-2,-8,-9,10,6,-9,-4,10,7,-9,-4,-10,-7,10,-2,7,-8,-4,-6,10], dtype = "uint16")#candidate|8262|(1050,)|const|uint16
call_8261 = relay.TupleGetItem(func_4731_call(relay.reshape(const_8262.astype('uint16'), [5, 210])), 2)
call_8263 = relay.TupleGetItem(func_4733_call(relay.reshape(const_8262.astype('uint16'), [5, 210])), 2)
func_1665_call = mod.get_global_var('func_1665')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_8264 = relay.TupleGetItem(func_1665_call(), 0)
call_8265 = relay.TupleGetItem(func_1667_call(), 0)
func_5821_call = mod.get_global_var('func_5821')
func_5824_call = mutated_mod.get_global_var('func_5824')
const_8269 = relay.const([False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,False,False,False,False,True,False,False,True,False,False,True,True,True,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False,True,True,False,True,True,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,True,True,False,True,False,True,False,True,False,False,True,True,True,True,True,False,False,True,True,True,True,False,False,False,True,False,False,False,True,True,True,False,False,True,True,True,False,True,False,False,True,True,False,False,True,True,False,True,False,False,False,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,True,True,True,True,False,False,True,False,False,False,True,False,True,True,False,True,False,False,True,False,False,True,True,True,False,True,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,False,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,True,False,True,False,True,False,True,True,True,False,True,False,True,True,False,True,False,False,False,True,False,False,False,False,False,False,False,True,True,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,False,False,True,False,True,False,True,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True,False,True,True,True,True,True,False,False,True,False,False,True,False,True,True,True,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,True,True,True,False,True,True,False,True,False,True,True,True,False,False,False,True,True,False,False,True,True,False,True,False,False,False,True,False,False,True,False,True,True,False,False,False,True,False,False,True,True,True,True,True,False,True,False,True,True,False,False,False,False,True,False,False,False,False,False,False,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,False,False,False,True,True,False,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,True,False,False,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,False,True,True,False,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,True,True,False,False,True,True,True,False,True,True,True,False,True,True,True,False,True,False,False,False,False,False,True,True,False,True,False,True,True,True,True,True,True,False,True,False,True,False,True,True,True,False,True,True,True,True,True,True,True,True,True,False,True,True,True,False,False,True,True,False,False,True,True,True,True,False,False,False,True,True,True,False,True,True,True,True,False,True,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,False,True,True,False,True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,False,True,True,True,False,True,False,True,False,True,True,True,True,True,False,True,False,False,True,True,False,True,True,False,False,False,True,True,True,True,False,True,False,True,False,False,False,False,False,False,True,True,True,False,False,False,False,True,False,True,False,False,False,True,True,False,True,False,True,False,True,True,True,True,False,False,False,False,False,False,True,False,True,False,False,False,False,False,True,True,True,True,True,True,False,False,False,True,False,True,True,True,True,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,True,True,False,False,True,False,True,True,True,True,False,False,True,True,True,False,True,True,True,True,False,False,False,True,False,True,True,True,True,True,False,False,False,True,True,True,True,False,False,True,True,True,True,False,False,False,False,True,False,True,False,False,True,False,False,False,False,True,True,True,False,True,False,False,False,True,False,False,True,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,False,True,False,False,False,True,False,False,True,False,True,True,True,True,True,False,True,False,False,True,True,True,True,False,True,False,True,False,False,False,False,True,False,True,True,False,False,True,True,True,True,False,True,False,True,False,False,False,True,True,True,False,False,False,False,True,True,True,True,True,True,False,False,True,True,False,False,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,True,True,False,True,True,True,False,False,True,False,False,True,True,True,True,True,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,True,False,False,True,True,False,True,True,True,True,False,False,True,True,False,False,False,True,True,False,True,False,False,False,False,True,False,False,True,False,False,False,False,False,True,True,False,True,True,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,True,False,True,False,True,True,False,True,False,False,True,False,True,False,False,True,True,False,True,True,False,True,False,True,False,False,True,True,False,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,True,False,True,False,True,True,False,True,True,True,True,True,False,False,False,False,True,False,True,True,True,True,True,False,True,False,True,False,False,True,True,False,True,False,False,False,True,False,True,False,False,False,True,False,True,True,False,False,False,True,True,True,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,False,False,True,False,False,True,False,True,False,False,True,False,True,False,True,True,True,True,False,True,True,True,False,True,False,True,True,False,True,False,False,True,False,True,True,False,False,True,False,True,True,True,True,False,False,True,True,True,False,True,False,True,False,True,False,False,False,False,True,True,False,True,False,False,False,True,False,True,False,False,False,True,False,True,True,False,False,False,True,False,True,True,False,False,False,False,False,True,False,True,False,False,False,True,False,True,False,True,False,True,True,False,False,True,True,False,True,False,False,False,False,False,False,False,False,False,True,False,True,True,False,False,False,False,True,False,True,True,True,True,False,True,True,True,False,True,True,False,True,True,False,True,True,False,False,True,True,True,False,False,False,False,False,False,False,True,True,False,True,False,True,True,True,True,False,False,False,True,False,True,True,False,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,False,True,True,True,True,True,True,True,True,False,False,False,False,False,True,True,False,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,False,True,True,True,True,True,False,False,False,True,True,True,False,True,False,False,False,False,False,False,False,True,True,False,True,False,True,True,True,True,True,True,False,False,False,False,False,True,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,False,False,False,False,True,True,False,True,True,True,True,True,False,True,True,True,True,True,True,False,False,True,True,False,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,True,False,False,True,True,True,False,True,False,True,True,True,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,False,True,False,False,False,False,False,True,True,True,False,False,True,True,False,False,True,True,True,False,False,True,False,True,True,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,True,False,False,True,False,True,False,True,True,True,True,True,False,False,True,True,False,False,True,True,False,False,False,True,True,True,False,False,True,False,True,False,False,True,True,True,False,False,False,False,True,True,True,True,False,False,False,False,True,True,True,True,True,True,False,False,False,False,True,True,True,False,False,True,False,True,False,False,True,True,False,False,False,False,True,False,False,True,False,True,False,True,True,True,False,True,False,False,False,True,False,True,True,False,False,True,True,True,False,True,False,False,True,False,False,True,True,True,False,True,False,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,False,True,True,False,False,True,False,True,False,True,False,True,True,True,False,True,True,True,False,True,False,True,True,True,False,False,True,True,True,False,True,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,True,False,True,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,False,True,True,False,False,False,False,True,False,True,True,False,False,False,True,False,False,True,False,True,True,False,False,False,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,False,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,True,True,False,False,True,False,True,False,True,True,True,False,True,True,True,True,False,False,True,True,False,True,True,False,False,True,False,False,True,False,False,False,True,True,False,True,True,False,True,False,True,False,False,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,False,False,False,False,False,False,True,True,True,True,True,False,True,False,False,False,True,True,True,False,False,True,True,True,True,True,True,True,True,True,True,True,True,False,False,False,False,True,True,True,False,False,True,False,False,True,False,True,False,True,False,False,False,True,False,True,True,True,False,False,False,False,False,False,False,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,True,True,True,False,False,True,True,True,True,False,False,True,False,False,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,True,True,True,False,True,True,False,False,True,True,False,True,False,False,True,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,False,True,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True,True,True,True,True,True,True,True,True,False,True,True,True,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,False,False,True,True,True,False,True,False,False,False,True,False,False,False,True,False,True,True,True,True,False,True,True,True,False,False,True,True,True,False,True,True,True,False,True,False,True,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,False,True,False,True,False,True,False,False,False,False,True,True,True,False,False,True,False,True,True,False,False,True,False,False,True,True,False,False,False,False,False,True,True,True,False,True,False,False,True,True,False,True,False,True,True,False,False,True,True,True,True,True,False,True,True,True,True,True,True,True,True,False,False,False,True,False,True,True,True,True,False,True,False,False,True,True,False,True,False,True,True], dtype = "bool")#candidate|8269|(2160,)|const|bool
call_8268 = relay.TupleGetItem(func_5821_call(relay.reshape(const_8269.astype('bool'), [9, 15, 16])), 2)
call_8270 = relay.TupleGetItem(func_5824_call(relay.reshape(const_8269.astype('bool'), [9, 15, 16])), 2)
func_6565_call = mod.get_global_var('func_6565')
func_6566_call = mutated_mod.get_global_var('func_6566')
call_8283 = relay.TupleGetItem(func_6565_call(), 0)
call_8284 = relay.TupleGetItem(func_6566_call(), 0)
bop_8291 = relay.not_equal(bop_8223.astype('bool'), call_8234.astype('bool')) # shape=(7, 3, 15)
bop_8294 = relay.not_equal(bop_8226.astype('bool'), call_8235.astype('bool')) # shape=(7, 3, 15)
bop_8295 = relay.less(call_8268.astype('bool'), call_8220.astype('bool')) # shape=(7, 1, 15)
bop_8298 = relay.less(call_8270.astype('bool'), call_8221.astype('bool')) # shape=(7, 1, 15)
output = relay.Tuple([call_8261,const_8262,call_8264,const_8269,call_8283,bop_8291,bop_8295,])
output2 = relay.Tuple([call_8263,const_8262,call_8265,const_8269,call_8284,bop_8294,bop_8298,])
F = relay.Function([var_8222,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8222,], output2)
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
